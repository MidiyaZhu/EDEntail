
import torch
import csv
from numpy import *
from transformers import RobertaTokenizer,RobertaModel



if __name__ == '__main__':
    transfomer = "roberta-large"
    model = RobertaModel.from_pretrained(transfomer)
    tokenizer = RobertaTokenizer.from_pretrained(transfomer)
    label_names = [
                    'sadness',
                   'anger',
                   'disgust',
                   'fear',
                   'joy',
                   'surprise',
        'love'
                   ]

    for label_name in label_names:
        word_embedding_vocab = {}
        relatedwordfile = './' + str(label_name) + '.csv'
        rows = []
        count =0
        with open(relatedwordfile) as f:
            relatedwords = csv.reader(f)
            for relatedword in relatedwords:
                token = tokenizer.tokenize(' '+relatedword[0])  # sadness token

                if len(token) ==1:
                    token_token = tokenizer(' '+relatedword[0], padding=True, return_tensors='pt')
                    token_emb= model(token_token['input_ids'], attention_mask=token_token['attention_mask'])['last_hidden_state'][0][1]
                    word_embedding_vocab[relatedword[0]] =token_emb
                    count+=1

        '''save embedding with text_index in word_embedding_vocab as .pt file'''
        print(f'{label_name}  {count-1}')
        torch.save(word_embedding_vocab, r'./save_'+ str(label_name) +'.pt')



