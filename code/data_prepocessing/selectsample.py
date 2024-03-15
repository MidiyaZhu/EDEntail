import csv
from random import sample
import random


def mainaman(k):
    dataname='aman'
    for n in range(5):
        trainfile='./data/'+str(k)+'/' + dataname.upper() + '/' + dataname.lower() +'select_train_'+str(n)+'.csv'
        selectfile='./data/' + dataname.upper() + '/' + dataname.lower() +'.csv'
        trainsample = []
        with open(selectfile) as f:
            csv_read = csv.reader(f)
            count=0 #''' angry, disgust, happy, neutral,surprise, sad, and fear'''
            joy, anger, sadness, disgust, fear, neutral, surprise = [], [], [], [], [], [], [],
            for row in csv_read:
                if row[1] == 'joy':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    joy.append(st)
                elif row[1] == 'sadness':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    sadness.append(st)
                elif row[1] == 'anger':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    anger.append(st)
                elif row[1] == 'disgust':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    disgust.append(st)
                elif row[1] == 'fear':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    fear.append(st)
                elif row[1] == 'noemo':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    neutral.append(st)
                elif row[1] == 'surprise':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    surprise.append(st)

        joyselect = sample(joy, k)
        fearselect = sample(fear, k)
        disgustselect = sample(disgust, k)
        angerselect = sample(anger, k)
        sadnessselect = sample(sadness, k)
        neutralselect = sample(neutral, k)
        surpriseselect = sample(surprise, k)
        for c in range(len(joyselect)):
            trainsample.append(joyselect[c])
            trainsample.append(fearselect[c])
            trainsample.append(disgustselect[c])
            trainsample.append(angerselect[c])
            trainsample.append(sadnessselect[c])
            trainsample.append(neutralselect[c])
            trainsample.append(surpriseselect[c])

        with open(trainfile, 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(trainsample)
        '''train'''

        '''dev'''
        devfile = './data/'+str(k)+'/' +dataname.upper() + '/' + dataname.lower() + 'select_dev_' + str(n) + '.csv'

        devsmaple = []

        with open(selectfile) as f:
            csv_read = csv.reader(f)
            count = 0
            joy, anger, sadness, disgust, fear, neutral, surprise = [], [], [], [], [], [], [],
            for row in csv_read:
                if row not in trainsample:
                    if row[1] == 'joy':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        joy.append(st)
                    elif row[1] == 'sadness':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        sadness.append(st)
                    elif row[1] == 'anger':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        anger.append(st)
                    elif row[1] == 'disgust':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        disgust.append(st)
                    elif row[1] == 'fear':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        fear.append(st)
                    elif row[1] == 'noemo':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        neutral.append(st)
                    elif row[1] == 'surprise':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        surprise.append(st)

        joyselect = sample(joy, k)
        fearselect = sample(fear, k)
        disgustselect = sample(disgust, k)
        angerselect = sample(anger, k)
        sadnessselect = sample(sadness, k)
        neutralselect = sample(neutral, k)
        surpriseselect = sample(surprise, k)
        for c in range(len(joyselect)):
            devsmaple.append(joyselect[c])
            devsmaple.append(fearselect[c])
            devsmaple.append(disgustselect[c])
            devsmaple.append(angerselect[c])
            devsmaple.append(sadnessselect[c])
            devsmaple.append(neutralselect[c])
            devsmaple.append(surpriseselect[c])

        with open(devfile, 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(devsmaple)

        '''dev'''

        '''test'''
        allsmaple = []
        with open(selectfile) as ts:
            csv_readall = csv.reader(ts)
            for allrow in csv_readall:
                allsmaple.append(allrow)
        L1 = random.sample(range(0, len(allsmaple)), len(allsmaple))
        print(len(L1))
        count=0
        selectsample = []
        for l in L1:
            if allsmaple[l] not in devsmaple and allsmaple[l] not in trainsample and count<int(len(allsmaple)*0.2):
                selectsample.append(allsmaple[l])
                count += 1

        testfile = './data/'+str(k)+'/' + dataname.upper() + '/' + dataname.lower() + 'select_test02_'+str(n)+'.csv'

        with open(testfile, 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(selectsample)
        '''test'''

def mainmeld(k):
    dataname = 'meld'
    for n in range(5):
        trainfile = '/media/server01/sda2/zixiao/SAwithTime/code/zsl_nli_emotion_prompts-main/data/data2/' + dataname.upper() + '/' + dataname.lower() + 'select_train_' + str(
            n) + '.csv'
        selectfiletrain = '/media/server01/sda2/zixiao/SAwithTime/code/zsl_nli_emotion_prompts-main/data/' + dataname.upper() + '/' + dataname.lower() + '_train.csv'

        trainsample = []

        with open(selectfiletrain) as f:
            csv_read = csv.reader(f)
            joy, anger, sadness, disgust, fear, neutral, surprise = [], [], [], [], [], [], []
            for row in csv_read:
                if row[1] == 'joy':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    joy.append(st)
                elif row[1] == 'sadness':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    sadness.append(st)
                elif row[1] == 'anger':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    anger.append(st)
                elif row[1] == 'disgust':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    disgust.append(st)
                elif row[1] == 'fear':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    fear.append(st)
                elif row[1] == 'noemo':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    neutral.append(st)
                elif row[1] == 'surprise':
                    st = []
                    st.append(row[0])
                    st.append(row[1])
                    surprise.append(st)

        joyselect = sample(joy, k)
        fearselect = sample(fear, k)
        disgustselect = sample(disgust, k)
        angerselect = sample(anger, k)
        sadnessselect = sample(sadness, k)
        neutralselect = sample(neutral, k)
        surpriseselect = sample(surprise, k)
        for c in range(len(joyselect)):
            trainsample.append(joyselect[c])
            trainsample.append(fearselect[c])
            trainsample.append(disgustselect[c])
            trainsample.append(angerselect[c])
            trainsample.append(sadnessselect[c])
            trainsample.append(neutralselect[c])
            trainsample.append(surpriseselect[c])

        with open(trainfile, 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(trainsample)
        '''train'''

        '''dev'''
        devfile = '/media/server01/sda2/zixiao/SAwithTime/code/zsl_nli_emotion_prompts-main/data/data2/' + dataname.upper() + '/' + dataname.lower() + 'select_dev_' + str(
            n) + '.csv'
        selectfiledev = '/media/server01/sda2/zixiao/SAwithTime/code/zsl_nli_emotion_prompts-main/data/' + dataname.upper() + '/' + dataname.lower() + '_dev.csv'
        devsmaple = []

        with open(selectfiledev) as f:
            csv_read = csv.reader(f)
            joy, anger, sadness, disgust, fear, neutral, surprise = [], [], [], [], [], [], []
            for row in csv_read:
                if row not in trainsample:
                    if row[1] == 'joy':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        joy.append(st)
                    elif row[1] == 'sadness':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        sadness.append(st)
                    elif row[1] == 'anger':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        anger.append(st)
                    elif row[1] == 'disgust':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        disgust.append(st)
                    elif row[1] == 'fear':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        fear.append(st)
                    elif row[1] == 'noemo':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        neutral.append(st)
                    elif row[1] == 'surprise':
                        st = []
                        st.append(row[0])
                        st.append(row[1])
                        surprise.append(st)

        joyselect = sample(joy, k)
        fearselect = sample(fear, k)
        disgustselect = disgust
        angerselect = sample(anger, k)
        sadnessselect = sample(sadness, k)
        neutralselect = sample(neutral, k)
        surpriseselect = sample(surprise, k)
        for c in range(len(joyselect)):
            devsmaple.append(joyselect[c])
            devsmaple.append(fearselect[c])

            devsmaple.append(angerselect[c])
            devsmaple.append(sadnessselect[c])
            devsmaple.append(neutralselect[c])
            devsmaple.append(surpriseselect[c])
        for c in range(len(disgustselect)):
            devsmaple.append(disgustselect[c])

        with open(devfile, 'w', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(devsmaple)

        '''dev'''
if __name__ == '__main__':
    k = 32
    mainaman(k)
    mainaman(k)