import torch
from copy import deepcopy
from numpy import *
from transformers import RobertaTokenizer,RobertaModel
import matplotlib.pyplot as plt
from numpy import where
from sklearn.cluster import KMeans,MiniBatchKMeans
from scipy.spatial.distance import euclidean,cosine
from sklearn.metrics import silhouette_score, silhouette_samples

def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

def inter_word_cosim_sort(min_center_word_emb,min_center_word,LtoS):
    interwordcosim = {}
    interwordcosimlist = []
    for i in range(len(min_center_word_emb)):
        cosim = []
        for j in range(len(min_center_word_emb)):
            cosim.append(cosine(min_center_word_emb[i], min_center_word_emb[j]))
        interwordcosim[min_center_word[i]] = mean(cosim)
        interwordcosimlist.append(mean(cosim))
    interwordcosimlist.sort(reverse=LtoS)  # reverse=False small to large (most similar to dissimilar) (cosine)
    sortinterwordcosim = []
    for item in interwordcosimlist:
        sortinterwordcosim.append(get_keys(interwordcosim, item)[0])
    return sortinterwordcosim

def inter_word_cosim(word_emb,word):
    interwordcosim = {}
    interwordcosimlist = []
    for i in range(len(word_emb)):
        cosim = []
        for j in range(len(word_emb)):
            cosim.append(1-cosine(word_emb[i], word_emb[j]))
        interwordcosim[word[i]] = mean(cosim)
        interwordcosimlist.append(mean(cosim))
    interwordcosimlist.sort(reverse=True)  # reverse=True large to small (most similar to dissimilar) (1-cosine)
    sortinterwordcosim = {}
    for item in interwordcosimlist:
        sortinterwordcosim[get_keys(interwordcosim, item)[0]]=item
    return sortinterwordcosim

def inter_word_dist(word_emb,word):
    interwordeuclidean = {}
    interwordeuclideanlist = []
    for i in range(len(word_emb)):
        deuclidean = []
        for j in range(len(word_emb)):
            deuclidean.append(euclidean(word_emb[i], word_emb[j]))
        interwordeuclidean[word[i]] = mean(deuclidean)
        interwordeuclideanlist.append(mean(deuclidean))
    interwordeuclideanlist.sort(reverse=True)  # reverse=True large to small (most similar to dissimilar) (euclidean)
    sortinterwordeuclidean = {}
    for item in interwordeuclideanlist:
        sortinterwordeuclidean[get_keys(interwordeuclidean, item)[0]]=item
    return sortinterwordeuclidean

def seconde_min(lt,idx):
    d={}
    for i, v in enumerate(lt):
        d[v]=i
    ltc=deepcopy(lt)
    ltc.sort()
    y=ltc[idx]
    return d[y]


def dic_average(dic):
    distance = []
    for i in dic:
        distance.append(dic[i])
    return mean(distance)


def getcluster():
    label_names = [
                    'sadness',
                   'joy',
                   'anger',
                   'disgust',
                   'fear',
                   'surprise',
                 'love'
                   ]

    tokennums=[
        '1' ]
    for tokennum in tokennums:
        label_length=[]
        for label_name in label_names:

            word_embedding_dict = torch.load( r'./save_' + str( label_name) + 'pooler.pt')
            words=[]
            X=[]
            for word,emb in word_embedding_dict.items():
                words.append(word)
                try:
                    X = torch.cat((X, emb.detach().unsqueeze(0)))  #[14,1024[
                except:
                    X = emb.detach().unsqueeze(0)
            label_length.append(len(X))
        labelcentercluster=[]
        n_clusternum = arange(2, int(min(label_length)))

        for label_name in label_names:


            word_embedding_dict = torch.load( r'./save_' + str( label_name) + 'pooler.pt')
            words = []
            X = []
            for word, emb in word_embedding_dict.items():
                words.append(  word)
                try:
                    X = torch.cat((X, emb.detach().unsqueeze(0)))
                except:
                    X = emb.detach().unsqueeze(0)

            '''step 1: same label: synonyms inter-distance'''
            sscore, s_centerword_list={}, {}
            for n_clusters in n_clusternum:
                print(n_clusters)
                sscore[n_clusters]=[]
                s_centerword_list[n_clusters]=[]
                inter_clusterword_distance=[]
                for repeat in range(20):
                    s_large = 0
                    model = KMeans(n_clusters=n_clusters)
                    model.fit(X)
                    yhat = model.predict(X)
                    min_center_word_emb_dist, min_center_word_dist = [], []
                    dict_cluster, dict_cluster_dist , sorteddict_cluster_dist = {},{},{}
                    for n in range(n_clusters):
                        dict_cluster[n] = []
                        dict_cluster_dist[n] =[]
                        sorteddict_cluster_dist[n] =[]

                    for iclust in range(model.n_clusters):
                        cluster_pts_indices = where(model.labels_ == iclust)[0]
                        cluster_cen = model.cluster_centers_[iclust]  #center of the cluster

                        distlist = [euclidean(X[idx], cluster_cen) for idx in cluster_pts_indices]

                        min_dist_idx = argmin([euclidean(X[idx], cluster_cen) for idx in cluster_pts_indices])
                        sorted_id_dist = sorted(range(len(distlist)), key=lambda k:distlist[k], reverse=False)
                        dict_cluster_dist_iclustemb=[]
                        for inclust_dist in sorted_id_dist:
                            dict_cluster_dist[iclust].append(words[cluster_pts_indices[inclust_dist]])  #words belongs to cluster[iclust]
                            dict_cluster_dist_iclustemb.append(X[cluster_pts_indices[inclust_dist]]) #the embedding of words belongs to cluster[iclust]
                        sorteddict_cluster_dist[iclust]=inter_word_dist(dict_cluster_dist_iclustemb, dict_cluster_dist[iclust])  #words belongs to cluster[iclust]: inter-cosim of word in cluster[iclust]
                        min_emb_dist=X[cluster_pts_indices[min_dist_idx]] #embdding of centerword in cluster[iclust]
                        min_word_dist=words[cluster_pts_indices[min_dist_idx]] #centerword in cluster[iclust]
                        min_center_word_emb_dist.append(min_emb_dist) #centerword embedding based on euclidean
                        min_center_word_dist.append(min_word_dist) #centerword based on euclidean



                    '''step 2: same label: inter-clusterword-cosim'''
                    interclusterworddist = inter_word_dist(min_center_word_emb_dist, min_center_word_dist)
                    sorted_min_center_word_dist,reversesorted_min_center_word_dist=[],[]
                    if n_clusters == 2:
                        sorted_min_center_word_dist=min_center_word_dist
                    else:
                        for kk in interclusterworddist:
                            sorted_min_center_word_dist.append(kk)
                    inter_clusterword_distance.append(dic_average(interclusterworddist))
                    '''step 2: same label: inter-clusterword-clusterword-distance'''
                    '''step 3: silhouete score'''

                    s = silhouette_score(X, yhat)
                    if s>s_large:
                        s_large=s
                        s_centerword_list[n_clusters]=sorted_min_center_word_dist
                    sscore[n_clusters].append(s)
                    '''step 3: silhouete score'''
            labelcentercluster[label_name]=s_centerword_list
        return labelcentercluster



        #     for key in sscore:
        #         print(f'\n\n\n{label_name}-{key}: {mean(sscore[key])}\n')
        #         hypothesis_emo_syns_LTOS[key][label_name] =[ ', '.join([str(i) for i in s_centerword_list[key]])]
        #         hypothesis_emo_synspace_LTOS[key][label_name] =[ ' '.join([str(i) for i in s_centerword_list[key]])]
        #         hypothesis_emo_synsand_LTOS[key][label_name] = [' and '.join([str(i) for i in s_centerword_list[key]])]
        #         hypothesis_emo_synslash_LTOS[key][label_name] = ['/ '.join([str(i) for i in s_centerword_list[key]])]
        #
        # with open(outputfile2, 'a') as f:
        #     f.write(f'hypothesis_emo_syns_LTOS={hypothesis_emo_syns_LTOS}\n\n\n')
        #     f.write(f'hypothesis_emo_synspace_LTOS={hypothesis_emo_synspace_LTOS}\n\n\n')
        #     f.write(f'hypothesis_emo_synsand_LTOS={hypothesis_emo_synsand_LTOS}\n\n\n')
        #     f.write(f'hypothesis_emo_synslash_LTOS={hypothesis_emo_synslash_LTOS}\n\n\n')
        #
        # with open(outputfile3, 'a') as f:
        #     f.write(f'{labelcentercluster}\n')


