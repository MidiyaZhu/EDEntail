1. run selectsample.py
please obtain the vocabulary for each label
2. knowledge/save_embedding.py

Get EDef based on Knowledge 
entailment knowledge:
3. knowledge/EDef_EntailKnowledge
frequency knowledge:
3. knowledge/EDef_FreqKnowledge.py

For saved EDef in four formats,chosen the one you need and copy into entialmentdatasetbuild_embeded.py
4. entialmentdatasetbuild_embeded.py
In entialmentdatasetbuild_embeded.py, if you want only one hypothesis, change the hypothesis file.

We only give dataset preprocessing examples on AMAN and MELD, if you want to re-run SST2, CR or other dataset, just change the filepath and the corresponding class label.

The train, dev, test datasets is used in EDEntail/fewshot.py for classification