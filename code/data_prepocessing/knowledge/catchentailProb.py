import csv
import numpy as np

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from sklearn.metrics import classification_report, accuracy_score, f1_score, recall_score, precision_score

device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")

def getsplitdataet(dataname,joy, anger, sadness,disgust, fear,surprise ):
    for repeatnum in range(5):

        loadpath = './data/' + dataname.upper() + '/' + dataname.lower() + 'select_train_' + str( repeatnum) + '.csv'


        csvFile = open(loadpath, "r")
        reader = csv.reader(csvFile)

        for item in reader:
            if item[1]=='joy':
                st=[]
                st.append(item[0])
                st.append(item[1])
                joy.append(st)
            elif item[1]=='anger':
                st=[]
                st.append(item[0])
                st.append(item[1])
                anger.append(st)
            elif item[1]=='sadness':
                st=[]
                st.append(item[0])
                st.append(item[1])
                sadness.append(st)
            elif item[1]=='disgust':
                st=[]
                st.append(item[0])
                st.append(item[1])
                disgust.append(st)
            elif item[1]=='fear':
                st=[]
                st.append(item[0])
                st.append(item[1])
                fear.append(st)
            elif item[1]=='surprise':
                st=[]
                st.append(item[0])
                st.append(item[1])
                surprise.append(st)
    return joy, anger, sadness,disgust, fear,surprise


def compute_metrics(data, y_true, y_pred, probs_emotions, id_prompt, output_file, result_file):
    print(classification_report(y_true, y_pred))
    with open(result_file, 'a') as f:
        f.write(f"{classification_report(y_true, y_pred)}")
    data[id_prompt] = y_pred
    data['prob_' + id_prompt] = probs_emotions
    data.to_csv(output_file, sep="\t", index=False)


def report_evaluation(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)  # y_true  y_pred ['joy']
    f1_weight = f1_score(y_true, y_pred, average='weighted')
    r_weight = recall_score(y_true, y_pred, average='weighted')
    p_weight = precision_score(y_true, y_pred, average='weighted')
    f1_macro = f1_score(y_true, y_pred, average='macro')
    r_macro = recall_score(y_true, y_pred, average='macro')
    p_macro = precision_score(y_true, y_pred, average='macro')
    frcreport = classification_report(y_true, y_pred)
    print(classification_report(y_true, y_pred))
    return acc, f1_weight, r_weight, p_weight, frcreport, f1_macro, r_macro, p_macro


def compute_entailment(datafile, transfomer, template,kv):
    print("Loading model...")

    model = AutoModelForSequenceClassification.from_pretrained(transfomer)
    tokenizer = AutoTokenizer.from_pretrained(transfomer)

    model.to(device)
    model.eval()

    entail_dict={}
    for label in kv:  # 6
        probs = []
        with open(datafile) as f:
            csv_read = csv.reader(f)
            for rows in csv_read:
                premise = rows[0]
                with torch.no_grad():
                    for tem in template:
                        context = tem.replace("M", label)
                        x = tokenizer.encode(premise, context, return_tensors='pt', truncation_strategy='only_first')
                        x = x.to(device)  # [1,25]
                        logits = model(x)[0]  # logits [1,3]
                        entail_contradiction_logits = torch.concat( (torch.max(logits[:, 0:2], dim=1, keepdim=True)[0], logits[:, 2:3]),dim=1)  # [b,2]
                        prob_label_is_true = entail_contradiction_logits.softmax(dim=1)[:, 1]  # 1
                        probs.append(prob_label_is_true.detach().cpu().numpy()[0])
        entail_dict[label]=np.mean(probs)
    return entail_dict


def getentail():
    dataname='aman'
    joy, anger, sadness,disgust, fear,surprise =[], [], [], [], [], []
    kjoy, kanger, ksadness,  kdisgust, kfear, ksurprise= getsplitdataet(dataname,joy, anger, sadness,disgust, fear,surprise)
    hypothesis = f'./hypothesis_final/hypothesis_{dataname.lower()}.csv'
    with open(hypothesis) as tf:
        template = csv.reader(tf)
    entaildict={}
    labels = ['joy', 'anger', 'sadness', 'surprise', 'disgust', 'noemo', 'fear']
    for labelname in labels:
        result_file = f'/media/server01/sda2/zixiao/SAwithTime/code/zsl_nli_emotion_prompts-main/output/ER2TO11/SPromptselect/Spromptrank_{dataname}_{labelname}_template{str(len(template))}.txt'
        print(result_file)
        if labelname=='joy':
            kv=kjoy
        elif labelname=='anger':
            kv = kanger
        elif labelname=='sadness':
            kv=ksadness
        elif labelname=='disgust':
            kv = kdisgust
        elif labelname=='fear':
            kv=kfear
        elif labelname=='surprise':
            kv = ksurprise

        data_file = '/media/server01/sda2/zixiao/SAwithTime/code/zsl_nli_emotion_prompts-main/code/Spromptselection/ER/dataset/'  + dataname.lower() + '_select_train_' + labelname + '.csv'
        transfomer = 'roberta-large-mnli'

        print(f"\n {labelname} for {dataname}\n")
        entailment_dict= compute_entailment(data_file,transfomer, template,kv)
        sort_entailment_dict=sorted(entailment_dict.items(), key=lambda x:x[1],reverse=True)
        entaildict[labelname]=sort_entailment_dict
    return entaildict

