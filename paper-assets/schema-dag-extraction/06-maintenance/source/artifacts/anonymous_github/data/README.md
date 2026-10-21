# Data

This directory should contain the following datasets. Due to licensing, we do not redistribute them directly.

## Datasets

### Few-NERD (NER, 66 fine-grained entity types)
- **Reference:** Ding et al., "Few-NERD: A Few-shot Named Entity Recognition Dataset", ACL 2021
- **Download:** https://ningding97.github.io/fewnerd/
- **Split used:** `supervised` test split
- **Format:** Place downloaded files in `data/fewnerd/` or use HuggingFace Hub (`DFKI-SLT/few-nerd`)

### FewRel (RE, 80 relation types)
- **Reference:** Han et al., "FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset", EMNLP 2018
- **Download:** https://thunlp.github.io/fewrel.html
- **Split used:** `val_wiki.json` (validation set with 80 relations)
- **Format:** Place `val_wiki.json` and `pid2name.json` in `data/fewrel/`

### DocRED (RE, 96 relation types)
- **Reference:** Yao et al., "DocRED: A Large-Scale Document-Level Relation Extraction Dataset", ACL 2019
- **Download:** https://github.com/thunlp/DocRED
- **Split used:** dev set
- **Format:** Place downloaded JSON files in `data/docred/`

### MAVEN (Event Detection, 168 event types)
- **Reference:** Wang et al., "MAVEN: A Massive General Domain Event Detection Dataset", EMNLP 2020
- **Download:** https://github.com/THU-KEG/MAVEN-dataset
- **Split used:** `train.jsonl` for type extraction, `valid.jsonl` for evaluation
- **Format:** Place `train.jsonl` and `valid.jsonl` in `data/maven/`

## Preprocessing

After downloading, run preprocessing scripts:

```bash
# Convert Few-NERD to parquet
python src/few_nerd_utils.py

# Convert FewRel to parquet
python src/preprocess_fewrel.py

# Convert MAVEN to parquet
python src/preprocess_maven.py
```

## Type Embeddings

BCS/SCS computation requires type embeddings. Generate them with:

```bash
# E5-large embeddings (default)
python scripts/compute_e5_embeddings.py

# Alternative: Qwen3 embeddings
python scripts/compute_fewrel_qwen3_embeddings.py
python scripts/compute_maven_qwen3_embeddings.py
```
