from numpy import *
from kmeans_cluster import getcluster
from catchfreq import getfreq


if __name__=='__main__':
    datanames=[
               'aman',
               'meld'
    ]
    kcluster=getcluster()
    freqdict=getfreq()
    for dataname in datanames:
        label_names = ['joy', 'anger', 'sadness', 'surprise', 'disgust',  'fear']
        freqKcluster={}
        for label_name in label_names:
            freqKcluster[label_name]={}
            for k in [7]:
                idx=[]
                freq=freqdict[label_name]
                freqidx = list(enumerate(freq))
                cluster = kcluster[label_name][k]
                for word in cluster:
                    infreq = False
                    for f in range(len(freqidx)):
                        if word in freqidx[f]:
                            idx.append(f)
                            infreq = True
                    if infreq == False:
                        print(label_name, word)
                orderedcluster = []
                for id in sorted(idx):
                    orderedcluster.append(freqidx[id][1])
                freqKcluster[label_name][k]=orderedcluster

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

                list=freqKcluster[label_name][k]
                template_emo_syns_LTOS[k][label_name] = [', '.join([str(i) for i in list])]
                template_emo_synspace_LTOS[k][label_name] = [' '.join([str(i) for i in list])]
                template_emo_synslash_LTOS[k][label_name] = ['/ '.join([str(i) for i in list])]
                template_emo_synsand_LTOS[k][label_name] = [' and '.join([str(i) for i in list])]

        outputfile = f'./{dataname}_EDef_freqknowledge.txt'

        with open(outputfile, 'a') as f:
            f.write(f'template_emo_syns_LTOS={template_emo_syns_LTOS}\n\n\n')
            f.write(f'template_emo_synspace_LTOS={template_emo_synspace_LTOS}\n\n\n')
            f.write(f'template_emo_synslash_LTOS={template_emo_synslash_LTOS}\n\n\n')
            f.write(f'template_emo_synsand_LTOS={template_emo_synsand_LTOS}\n\n\n')

