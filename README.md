
# EDEntail: Entailment-based Few-shot Text Classification with Extensional Definition

## 📁 Dataset and Template

The template, raw dataset, and 32-shot (per label) train/dev/test CSV files are located in the `32-shot-dataset` folder.

If you want to create a different *k*-shot split, run:

```bash
python split_kshot_dataset.py
````

> **Note**: Please double-check that the raw data folder is correctly specified in the script.

---



## 🧱 Build EDEntail Dataset

To build the train/dev/test sets for EDEntail, run:

```bash
python entailmentdatasetbuild_embeded.py
```

---

## 🧪 Evaluation on Downstream Tasks

To evaluate performance on few-shot classification tasks, run:

```bash
python fewshot.py
```

> **Note**: Modify the dataset name in the script as needed.

---

## 📂 Class-Related Words (Waiting for entailProb fixing)

Class-related words for each dataset (e.g., TREC, SST) are located in the `class_related_word` folder.

You can extract frequency-based and entailment-based knowledge by running:

```bash
python catchfreq.py
python catchentailProb.py (need to be fixed)
```

then run

```bash
python EDef_FreqKnowledge.py
python EDef_EntailKnowledge.py
```

Alternatively, you may directly use the processed results in the `entail_freq_label_results` folder. (We have already copied in entailmentdatasetbuild_embeded.py)

---


## 📄 Citation

If you use our code or dataset, please cite the following paper:

```bibtex
@inproceedings{zhu2024edentail,
  title={EDEntail: An Entailment-based Few-shot Text Classification with Extensional Definition},
  author={Zhu, Zixiao and Qian, Junlang and Feng, Zijian and Zhou, Hanzhang and Mao, Kezhi},
  booktitle={Findings of the Association for Computational Linguistics: NAACL 2024},
  pages={1124--1137},
  year={2024}
}
```
