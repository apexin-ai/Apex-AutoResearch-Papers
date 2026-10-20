## Citation Verification Report

Date: 2025-05-15

### 1. Ye et al. ICLR 2025
- **Status: VERIFIED**
- **Correct title**: Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance
- **Correct authors**: Jiasheng Ye, Peiju Liu, Tianxiang Sun, Jun Zhan, Yunhua Zhou, Xipeng Qiu
- **Correct venue**: ICLR 2025 (poster)
- **arXiv**: 2403.16952
- **Notes**: Title, venue, year all match literature_map.yaml. No corrections needed.

### 2. Dohmatob & Feng ICLR 2025
- **Status: PARTIALLY CORRECT**
- **Correct title**: Strong Model Collapse
- **Correct authors**: Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe
- **Correct venue**: ICLR 2025 (spotlight)
- **arXiv**: 2410.04840
- **Notes**: Title and venue are correct. Author list in literature_map.yaml ("Dohmatob & Feng") is incomplete — the paper has 4 authors, not 2. Arjun Subramonian and Julia Kempe are missing. Affiliations: Meta FAIR, Concordia University, Mila, NYU, UCLA.

### 3. Seddik et al.
- **Status: PARTIALLY CORRECT — title is fabricated/paraphrased**
- **Recorded title**: "Upper Bounds on Synthetic Data Proportion to Avoid Model Collapse"
- **Actual title**: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
- **Correct authors**: Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Mérouane Debbah
- **Correct venue**: arXiv preprint, April 2024 (also presented at SynthData workshop @ ICLR 2025)
- **arXiv**: 2404.05090
- **Notes**: The paper exists and does discuss upper bounds on synthetic data proportions, but the title in literature_map.yaml is a hallucinated paraphrase of the paper's content, not its actual title. The id `seddik2024synthetic_bound` year (2024) is correct. Must fix title and add arXiv ID.

### Summary
- **1/3 fully verified** (Ye et al.)
- **2/3 need correction** (Dohmatob et al.: missing authors; Seddik et al.: wrong title)
- **0/3 hallucinated** (all papers exist)

### Recommended Fixes for literature_map.yaml

1. `dohmatob2025collapse`: Update author list to include all 4 authors
2. `seddik2024synthetic_bound`: Change title to "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse", add arXiv ID 2404.05090

### Sources
- [OpenReview — Ye et al.](https://openreview.net/forum?id=jjCB27TMK3)
- [arXiv — Ye et al.](https://arxiv.org/abs/2403.16952)
- [ICLR proceedings — Dohmatob et al.](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- [arXiv — Dohmatob et al.](https://arxiv.org/abs/2410.04840)
- [arXiv — Seddik et al.](https://arxiv.org/abs/2404.05090)
- [Semantic Scholar — Seddik et al.](https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3)
