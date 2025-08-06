import numpy as np
from torch.utils.data import DataLoader
import time
import csv
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, RobertaTokenizer
from tqdm import tqdm
from sklearn.metrics import classification_report, accuracy_score, f1_score, recall_score, precision_score
from math import ceil
import statistics

device = torch.device("cuda:3" if torch.cuda.is_available() else "cpu")
'''PLM-NLI task 0 contradiction 1 neutral 2 entailment
    NLI-EMOTION task 0 contradiction(non-entailment)  1 entailment'''

transfomer = "roberta-larnlige-m"


class CSVDatasettrain(object):
    def __init__(self, data_dir):  # false, false, train
        label_dict3 = {"contradiction": 0, "neutral": 1, "entailment": 2}
        label_dict2 = {"contradiction": 0, "entailment": 1}
        self.label2, self.label3 = list(), list()
        self.premisehypothesis = list()
        csvFile = open(data_dir, "r")
        reader = csv.reader(csvFile)
        for data in reader:
            self.premisehypothesis.append(data[2].lower())
            self.label2.append(label_dict2[data[3]])
            self.label3.append(label_dict3[data[3]])
    def __len__(self):
        return len(self.label2)
    def __getitem__(self, idx):
        premisehypothesis = self.premisehypothesis[idx]
        label3 = self.label3[idx]
        label2 = self.label2[idx]
        return premisehypothesis, label3, label2


class CSVDatasettest(object):
    def __init__(self, data_dir):
        self.text, self.emotion = list(), list()
        csvFile = open(data_dir, "r")
        reader = csv.reader(csvFile)

        for data in reader:
            self.text.append(data[0].lower())
            self.emotion.append(data[1])
    def __len__(self):
        return len(self.text)
    def __getitem__(self, idx):
        premise = self.text[idx]
        emotion = self.emotion[idx]
        return premise, emotion

class CSVDatasettestlist(object):
    def __init__(self, data_dir, emotion_dict):
        self.text, self.emotion = list(), list()
        csvFile = open(data_dir, "r")
        reader = csv.reader(csvFile)

        for data in reader:
            self.text.append(data[0].lower())
            self.emotion.append(emotion_dict[data[1]])
    def __len__(self):
        return len(self.text)
    def __getitem__(self, idx):
        premise = self.text[idx]
        emotion = self.emotion[idx]
        return premise, emotion



def report_evaluation(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)  # y_true  y_pred ['joy']
    f1_weight = f1_score(y_true, y_pred, average='weighted')
    r_weight = recall_score(y_true, y_pred, average='weighted')
    p_weight = precision_score(y_true, y_pred, average='weighted')
    f1_macro = f1_score(y_true, y_pred, average='macro')
    r_macro = recall_score(y_true, y_pred, average='macro')
    p_macro = precision_score(y_true, y_pred, average='macro')
    frcreport = classification_report(y_true, y_pred, output_dict=True)

    return acc, f1_weight, r_weight, p_weight, f1_macro, r_macro, p_macro, frcreport



def report_evaluationnli(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)  # y_true  y_pred ['joy']
    f1_weight = f1_score(y_true, y_pred, average='weighted')
    r_weight = recall_score(y_true, y_pred, average='weighted')
    p_weight = precision_score(y_true, y_pred, average='weighted')
    f1_macro = f1_score(y_true, y_pred, average='macro')
    r_macro = recall_score(y_true, y_pred, average='macro')
    p_macro = precision_score(y_true, y_pred, average='macro')
    frcreport = classification_report(y_true, y_pred, output_dict=True)

    return acc, f1_weight, r_weight, p_weight, f1_macro, r_macro, p_macro, frcreport

def evaluatelogitsnlifewshot_ecbatch(model, tokenizer, test_dataset, eval_dataset, batch_size, eval_loader,type):
    y_truenli = []
    y_prednli = []
    text_list = test_dataset.text
    label_list = test_dataset.emotion
    unique_labels = sorted(list(set(label_list)))
    model.eval()
    with torch.no_grad():
        with tqdm(total=ceil(len(eval_dataset) / batch_size), desc='test_' + type, unit='batch') as pbar:
            for premisehypothesis, label3, label2 in eval_loader:

                inputs = tokenizer(premisehypothesis, padding=True, return_tensors='pt').to(device)
                label3 = label3.to(device)
                logit = model(inputs['input_ids'], attention_mask=inputs['attention_mask'], labels=label3)[
                    'logits']  # [b,3]
                logit_softmax = logit.softmax(dim=1)
                entail_contradiction_logits = torch.concat(
                    (torch.max(logit_softmax[:, 0:2], dim=1, keepdim=True)[0], logit_softmax[:, 2:3]), dim=1)  # [b,2]

                y_prednli += torch.argmax(entail_contradiction_logits, axis=1).detach().cpu().tolist()
                y_truenli += label2.detach().cpu().tolist()
                try:
                    prob_label_is_true_batch = torch.cat((prob_label_is_true_batch, logit_softmax[:, 2]))
                except:
                    prob_label_is_true_batch = logit_softmax[:, 2]
                pbar.update(1)

    prob_label_is_true = torch.reshape(prob_label_is_true_batch,(len(text_list), len(unique_labels), int(len(prob_label_is_true_batch)/(len(text_list)*len(unique_labels))))) # 3142,4,26

    entail_prob = torch.mean(prob_label_is_true, dim=2)
    y_pred = torch.argmax(entail_prob, axis=1).detach().cpu()

    acc, f1_weight, r_weight, p_weight, f1_macro, r_macro, p_macro, frcreport = report_evaluation(label_list,y_pred)
    accnli, f1_weightnli, r_weightnli, p_weightnli, f1_macronli, r_macronli, p_macronli, frcreportnli = report_evaluation(y_truenli, y_prednli)
    return acc, f1_weight, r_weight, p_weight, f1_macro, r_macro, p_macro, f1_weightnli, r_weightnli, p_weightnli, f1_macronli, r_macronli, p_macronli, accnli, frcreportnli, frcreport

def train(model, train_dataset, batch_size, train_loader, tokenizer, optimizer, criterion):
    correct_count = 0
    total_loss = 0

    model.train()
    with tqdm(total=ceil(len(train_dataset) / batch_size), desc='train', unit='batch') as pbar:
        for premisehypothesis, label3, label2 in train_loader:
            inputs = tokenizer(premisehypothesis, padding=True, return_tensors='pt').to(device)

            label3 = label3.to(device)
            label2 = label2.to(device)
            label2onehot = torch.nn.functional.one_hot(label2, num_classes=2).to(torch.float)
            optimizer.zero_grad()
            logit = model(inputs['input_ids'], attention_mask=inputs['attention_mask'], labels=label3)[
                'logits']  # [b,3]
            logit_softmax = logit.softmax(dim=1)
            entail_contradiction_logits = torch.concat(
                (torch.max(logit_softmax[:, 0:2], dim=1, keepdim=True)[0], logit_softmax[:, 2:3]), dim=1)  # [b,2]
            loss2 = criterion(entail_contradiction_logits, label2onehot)
            loss2.backward()
            optimizer.step()
            preds = torch.argmax(entail_contradiction_logits, axis=1)  # (2,)) [0,0]
            correct_count += (preds == label2).sum().item()
            total_loss += loss2.item()
            pbar.update(1)
    return correct_count / len(train_dataset), total_loss / len(train_dataset)


def evaluate(model, dev_dataset, batch_size, dev_loader, tokenizer, criterion):
    correct_count = 0
    total_loss = 0

    model.eval()
    with torch.no_grad():
        with tqdm(total=ceil(len(dev_dataset) / batch_size), desc='dev', unit='batch') as pbar:
            for premisehypothesis, label3, label2 in dev_loader:
                inputs = tokenizer(premisehypothesis, padding=True, return_tensors='pt').to(device)
                label3 = label3.to(device)
                label2 = label2.to(device)
                label2onehot = torch.nn.functional.one_hot(label2, num_classes=2).to(torch.float)

                logit = model(inputs['input_ids'], attention_mask=inputs['attention_mask'], labels=label3)[
                    'logits']  # [b,3]
                logit_softmax = logit.softmax(dim=1)

                entail_contradiction_logits = torch.concat(
                    (torch.max(logit_softmax[:, 0:2], dim=1, keepdim=True)[0], logit_softmax[:, 2:3]), dim=1)  # [b,2]
                loss2 = criterion(entail_contradiction_logits, label2onehot)

                preds = torch.argmax(entail_contradiction_logits, axis=1)  # (2,)) [0,0]
                correct_count += (preds == label2).sum().item()
                total_loss += loss2.item()
                pbar.update(1)
    return correct_count / len(dev_dataset), total_loss / len(dev_dataset)


def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs



def mainentail():
    datanames = [
        'meld'
    ]
    hy=['syns'] #   'syns','synspace', 'synslash','synsand'

    n_clusternum=[i for i in range(2,12)]
    orders = ['LTOS' ]
    for dataname in datanames:
        emotion_dict = {'joy': 0, 'anger': 1, 'sadness': 2, 'surprise': 3, 'disgust': 4, 'noemo': 5,
                            'fear': 6}
        for num in n_clusternum:
            for order in orders:
                for hypothesis in hy:
                    acclistsyns, acclistsynsnli, f1_weightlistsyns, r_weightlistsyns, p_weightlistsyns, f1_macrolistsyns, r_macrolistsyns, p_macrolistsyns, f1_weightlistsynsnli, r_weightlistsynsnli, p_weightlistsynsnli, f1_macrolistsynsnli, r_macrolistsynsnli, p_macrolistsynsnli = [], [], [], [], [], [], [], [], [], [], [], [], [], []
                    for repeatnum in range(5):
                        train_file = f'./embed/entail/entail/' + dataname.lower() + '_' + str(
                            num) + '_' + hypothesis + '_' + 'trainentail_' + str(repeatnum) + '.csv'
                        dev_file = f'./embed/entail/entail/' + dataname.lower() + '_' + str(
                            num) + '_' + hypothesis + '_' + 'deventail_' + str(repeatnum) + '.csv'
                        test_file = '32-shot-dataset/er/' + dataname.upper() + '/' + dataname.lower() + '_test.csv'

                        testsyns_file = f'./embed/entail/entail/' + dataname.lower() + '_' + str(
                            num) + '_' + hypothesis + '_' + 'testentail.csv'

                        test_dataset = CSVDatasettestlist(test_file, emotion_dict)

                        testsyns_dataset = CSVDatasettrain(testsyns_file)

                        batch_sizetest =200

                        testsyns_loader = DataLoader(dataset=testsyns_dataset,
                                                     batch_size=batch_sizetest,
                                                     shuffle=False)


                        print(testsyns_file)
                        print(test_file)
                        print(train_file)
                        print(dev_file)
                        modelpath = './' + dataname.lower() + 'freq.pt'

                        print(f"\nrepeated time {repeatnum + 1} for {dataname}\n")
                        train_dataset = CSVDatasettrain(train_file)
                        dev_dataset = CSVDatasettrain(dev_file)
                        model = AutoModelForSequenceClassification.from_pretrained(transfomer)
                        tokenizer = RobertaTokenizer.from_pretrained(transfomer)
                        model.to(device)
                        learning_rate = 1e-5
                        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
                        criterion = torch.nn.CrossEntropyLoss().to(device)
                        epochs = 6
                        batch_size =10
                        bestl_dev_acc = float(0)
                        for epoch in range(epochs):
                            start_time = time.time()
                            train_loader = DataLoader(dataset=train_dataset,
                                                      batch_size=batch_size,
                                                      shuffle=True)
                            dev_loader = DataLoader(dataset=dev_dataset,
                                                    batch_size=batch_size,
                                                    shuffle=False)
                            train_acc, train_loss = train(model, train_dataset, batch_size, train_loader, tokenizer,
                                                          optimizer,
                                                          criterion)
                            dev_acc, dev_loss = evaluate(model, dev_dataset, batch_size, dev_loader, tokenizer,
                                                         criterion)
                            end_time = time.time()
                            epoch_mins, epoch_secs = epoch_time(start_time, end_time)

                            if dev_acc >= bestl_dev_acc:
                                bestl_dev_acc = dev_acc
                                torch.save(model.state_dict(), modelpath)

                            print(f'Epoch: {epoch + 1:02} | Epoch Time: {epoch_mins}m {epoch_secs}s')
                            print(f'\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc * 100:.2f}%')
                            print(f'\tVal. Loss: {dev_loss:.3f} | Val. Acc: {dev_acc * 100:.2f}%')


                        model.load_state_dict(torch.load(modelpath))
                        test_accsyns, f1_weightsyns, r_weightsyns, p_weightsyns, f1_macrosyns, r_macrosyns, p_macrosyns, f1_weightnlisyns, r_weightnlisyns, p_weightnlisyns, f1_macronlisyns, r_macronlisyns, p_macronlisyns, test_accnlisyns, frcreportnlisyns, frcreportsyns = evaluatelogitsnlifewshot_ecbatch(
                            model, tokenizer, test_dataset, testsyns_dataset, batch_sizetest, testsyns_loader,
                            'syns')
                        print(
                            f'\t syns: Test. Acc: {test_accsyns * 100:.2f}% | Test f1: {f1_weightsyns * 100:.2f}% | Test r: {r_weightsyns * 100:.2f}% | Test p: {p_weightsyns * 100:.2f}%')
                        print(
                            f'\t syns: Test. NLI_Acc: {test_accnlisyns * 100:.2f}% | Test f1: {f1_weightnlisyns * 100:.2f}% | Test r: {r_weightnlisyns * 100:.2f}% | Test p: {p_weightnlisyns * 100:.2f}%')


                        acclistsyns.append(test_accsyns)
                        r_weightlistsyns.append(r_weightsyns)
                        p_weightlistsyns.append(p_weightsyns)
                        f1_weightlistsyns.append(f1_weightsyns)
                        r_macrolistsyns.append(r_macrosyns)
                        p_macrolistsyns.append(p_macrosyns)
                        f1_macrolistsyns.append(f1_macrosyns)
                        acclistsynsnli.append(test_accnlisyns)
                        r_weightlistsynsnli.append(r_weightnlisyns)
                        p_weightlistsynsnli.append(p_weightnlisyns)
                        f1_weightlistsynsnli.append(f1_weightnlisyns)
                        r_macrolistsynsnli.append(r_macronlisyns)
                        p_macrolistsynsnli.append(p_macronlisyns)
                        f1_macrolistsynsnli.append(f1_macronlisyns)


                    result_file = f'./entail/{dataname.lower()}_{str(num)}_{order}_{hypothesis}.txt'

                    with open(result_file, 'a') as f:

                        f.write(
                            f"the average accuracy: {round(float(np.mean(acclistsyns)), 4)} | + {round(float(max(acclistsyns)), 4)} | - {round(float(min(acclistsyns)), 4)}\n")


def mainfreq():
    datanames = [

        'meld'

    ]
    hy = ['syns']  # 'syns','synspace', 'synslash','synsand'

    orders = [  'LTOS'    ]
    for dataname in datanames:
        emotion_dict = {'joy': 0, 'anger': 1, 'sadness': 2, 'surprise': 3, 'disgust': 4, 'noemo': 5,
                        'fear': 6}  # aman
        for num in range(2,12):
            for order in orders:
                for hypothesis in hy:
                    acclistsyns, acclistsynsnli, f1_weightlistsyns, r_weightlistsyns, p_weightlistsyns, f1_macrolistsyns, r_macrolistsyns, p_macrolistsyns, f1_weightlistsynsnli, r_weightlistsynsnli, p_weightlistsynsnli, f1_macrolistsynsnli, r_macrolistsynsnli, p_macrolistsynsnli = [], [], [], [], [], [], [], [], [], [], [], [], [], []
                    for repeatnum in range(5):
                        train_file =f'./embed/entail/freq/' + dataname.lower() + '_' + str(num) +  '_' + hypothesis + '_' + 'trainentail_' + str(repeatnum) + '.csv'
                        dev_file = f'./embed/entail/freq/' + dataname.lower() + '_' + str(num) +  '_' + hypothesis + '_' + 'deventail_' + str(repeatnum) + '.csv'
                        test_file = '32-shot-dataset/er/' + dataname.upper() + '/' + dataname.lower()+'_test.csv'

                        testsyns_file =f'./embed/entail/freq/' + dataname.lower() + '_' + str(num) +  '_' + hypothesis + '_' + 'testentail.csv'

                        test_dataset = CSVDatasettestlist(test_file, emotion_dict)

                        testsyns_dataset = CSVDatasettrain(testsyns_file)

                        batch_sizetest =200

                        testsyns_loader = DataLoader(dataset=testsyns_dataset,
                                                     batch_size=batch_sizetest,
                                                     shuffle=False)


                        print(testsyns_file)
                        print(test_file)
                        print(train_file)
                        print(dev_file)
                        modelpath = './' + dataname.lower() + 'freq.pt'

                        print(f"\nrepeated time {repeatnum + 1} for {dataname}\n")
                        train_dataset = CSVDatasettrain(train_file)
                        dev_dataset = CSVDatasettrain(dev_file)
                        model = AutoModelForSequenceClassification.from_pretrained(transfomer)
                        tokenizer = RobertaTokenizer.from_pretrained(transfomer)
                        model.to(device)
                        learning_rate = 1e-5
                        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
                        criterion = torch.nn.CrossEntropyLoss().to(device)
                        epochs = 6
                        batch_size =10
                        bestl_dev_acc = float(0)
                        best_test_acc = float(0)
                        for epoch in range(epochs):
                            start_time = time.time()
                            train_loader = DataLoader(dataset=train_dataset,
                                                      batch_size=batch_size,
                                                      shuffle=True)
                            dev_loader = DataLoader(dataset=dev_dataset,
                                                    batch_size=batch_size,
                                                    shuffle=False)
                            train_acc, train_loss = train(model, train_dataset, batch_size, train_loader, tokenizer,
                                                          optimizer,
                                                          criterion)
                            dev_acc, dev_loss = evaluate(model, dev_dataset, batch_size, dev_loader, tokenizer,
                                                         criterion)
                            end_time = time.time()
                            epoch_mins, epoch_secs = epoch_time(start_time, end_time)

                            if dev_acc >= bestl_dev_acc:
                                bestl_dev_acc = dev_acc
                                torch.save(model.state_dict(), modelpath)

                            print(f'Epoch: {epoch + 1:02} | Epoch Time: {epoch_mins}m {epoch_secs}s')
                            print(f'\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc * 100:.2f}%')
                            print(f'\tVal. Loss: {dev_loss:.3f} | Val. Acc: {dev_acc * 100:.2f}%')


                        model.load_state_dict(torch.load(modelpath))
                        test_accsyns, f1_weightsyns, r_weightsyns, p_weightsyns, f1_macrosyns, r_macrosyns, p_macrosyns, f1_weightnlisyns, r_weightnlisyns, p_weightnlisyns, f1_macronlisyns, r_macronlisyns, p_macronlisyns, test_accnlisyns, frcreportnlisyns, frcreportsyns = evaluatelogitsnlifewshot_ecbatch(
                            model, tokenizer, test_dataset, testsyns_dataset, batch_sizetest, testsyns_loader,
                            'syns')
                        print(
                            f'\t syns: Test. Acc: {test_accsyns * 100:.2f}% | Test f1: {f1_weightsyns * 100:.2f}% | Test r: {r_weightsyns * 100:.2f}% | Test p: {p_weightsyns * 100:.2f}%')
                        print(
                            f'\t syns: Test. NLI_Acc: {test_accnlisyns * 100:.2f}% | Test f1: {f1_weightnlisyns * 100:.2f}% | Test r: {r_weightnlisyns * 100:.2f}% | Test p: {p_weightnlisyns * 100:.2f}%')


                        acclistsyns.append(test_accsyns)
                        r_weightlistsyns.append(r_weightsyns)
                        p_weightlistsyns.append(p_weightsyns)
                        f1_weightlistsyns.append(f1_weightsyns)
                        r_macrolistsyns.append(r_macrosyns)
                        p_macrolistsyns.append(p_macrosyns)
                        f1_macrolistsyns.append(f1_macrosyns)
                        acclistsynsnli.append(test_accnlisyns)
                        r_weightlistsynsnli.append(r_weightnlisyns)
                        p_weightlistsynsnli.append(p_weightnlisyns)
                        f1_weightlistsynsnli.append(f1_weightnlisyns)
                        r_macrolistsynsnli.append(r_macronlisyns)
                        p_macrolistsynsnli.append(p_macronlisyns)
                        f1_macrolistsynsnli.append(f1_macronlisyns)


                    result_file = f'./freq/{dataname.lower()}_{str(num)}_{order}_{hypothesis}.txt'

                    with open(result_file, 'a') as f:

                        f.write(
                            f"the average accuracy: {round(float(np.mean(acclistsyns)), 4)} | + {round(float(max(acclistsyns)), 4)} | - {round(float(min(acclistsyns)), 4)}\n")

if __name__ == "__main__":
    mainentail()
    mainfreq()