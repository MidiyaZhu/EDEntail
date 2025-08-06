from numpy import *
from kmeans_cluster import getcluster
from catchentailProb import getentail

if __name__=='__main__':
    datanames=['aman','meld']

    entaildict=getentail()
    kcluster = getcluster()
    for dataname in datanames:
        label_names = ['joy', 'anger', 'sadness', 'surprise', 'disgust',  'fear']
        entailKcluster={}
        for label_name in label_names:
            entailKcluster[label_name]={}
            for k in [7]:
                idx=[]
                entail=entaildict[label_name]
                cluster=kcluster[label_name][k]
                for word in cluster:
                    for f in range(len(entail)):
                        if word in entail[f]:
                            idx.append(f)
                if len(idx)!=len(cluster):
                    print(f'{cluster}\n{entail}\nerror!')
                    exit()
                orderedcluster=[]
                for id in sorted(idx):
                    orderedcluster.append(entail[id][0])
                entailKcluster[label_name][k]=orderedcluster

        template_emo_syns_LTOS,  template_emo_synspace_LTOS, template_emo_synslash_LTOS, template_emo_synsand_LTOS, = {}, {}, {}, {}

        for k in [7]:
            template_emo_syns_LTOS[k] = {}
            template_emo_synspace_LTOS[k] = {}
            template_emo_synslash_LTOS[k] = {}
            template_emo_synsand_LTOS[k] = {}
            template_emo_syns_LTOS[k]['noemo'] = ['others, no emotion']
            template_emo_synspace_LTOS[k]['noemo'] = ['others no emotion']
            template_emo_synsand_LTOS[k]['noemo'] = ['others and no emotion']
            template_emo_synslash_LTOS[k]['noemo'] = ['others/ no emotion']
            for label_name in label_names:
                template_emo_syns_LTOS[k][label_name] = []
                template_emo_synspace_LTOS[k][label_name] = []
                template_emo_synslash_LTOS[k][label_name] = []
                template_emo_synsand_LTOS[k][label_name] = []

                list=entailKcluster[label_name][k]
                template_emo_syns_LTOS[k][label_name] = [', '.join([str(i) for i in list])]
                template_emo_synspace_LTOS[k][label_name] = [' '.join([str(i) for i in list])]
                template_emo_synslash_LTOS[k][label_name] = ['/ '.join([str(i) for i in list])]
                template_emo_synsand_LTOS[k][label_name] = [' and '.join([str(i) for i in list])]

        outputfile = f'./{dataname}_EDef_entailknowledge.txt'

        with open(outputfile, 'a') as f:
            f.write(f'template_emo_syns_LTOS={template_emo_syns_LTOS}\n\n\n')
            f.write(f'template_emo_synspace_LTOS={template_emo_synspace_LTOS}\n\n\n')
            f.write(f'template_emo_synslash_LTOS={template_emo_synslash_LTOS}\n\n\n')
            f.write(f'template_emo_synsand_LTOS={template_emo_synsand_LTOS}\n\n\n')


