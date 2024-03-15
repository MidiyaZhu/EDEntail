import requests
import pandas as pd
import csv
from numpy import *
from transformers import RobertaTokenizer
transfomer = "roberta-large"

tokenizer = RobertaTokenizer.from_pretrained(transfomer)

def getfreq():
    label_names=[
        'sadness',
        'anger',
                 'disgust',
                 'fear',
        'joy',
        'surprise',
        'love'
                 ]
    freqdict={}
    for label_name in label_names:
        freqdict[label_name]={}
        relatedwordfile = ',/' + str( label_name) + '.csv'
        rows=[]
        count=0
        with open(relatedwordfile) as f:
            relatedwords = csv.reader(f)
            for relatedword in relatedwords:
                token = tokenizer.tokenize(' '+relatedword[0])  # sadness token
                if len(token)==1:
                    rows.append(relatedword[0])
                    count+=1

        for word in rows:
            params = {
                "content": word,
                "year_start": "2018",
                "year_end": "2019"
            }

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
            }
            print(params)
            html = requests.get("https://books.google.com/ngrams/json", params=params, headers=headers, timeout=3).text
            time_series = pd.read_json(html, typ="series")

            year_values = list(range(int(params['year_start']), int(params['year_end']) + 1))

            for series in time_series:
                freqdict[label_name][series["ngram"]] = series["timeseries"][1]
                print(f'word" {series["ngram"]}  frequence: {series["timeseries"][1]}')


    return freqdict