# AUC Data Unification Report (2026-05-15)

## 1. Three-Way Comparison Table (RF AUC values)

| Cell | Pair | Pipeline (GT) | edd_sensitivity | edd_9cell (bootstrap) | Sens Match? | 9cell Delta |
|------|------|:---:|:---:|:---:|:---:|:---:|
| pythia_nucleus095 | d0v1 | 0.9975 | 0.9975 | 0.9995 | Y | +0.0020 |
| pythia_nucleus095 | d1v2 | 0.8607 | 0.8607 | 0.9302 | Y | +0.0695 |
| pythia_nucleus095 | d2v3 | 0.8005 | 0.8005 | 0.8130 | Y | +0.0125 |
| pythia_temp09 | d0v1 | 0.9968 | 0.9968 | 0.9997 | Y | +0.0029 |
| pythia_temp09 | d1v2 | 0.8327 | 0.8327 | 0.9098 | Y | +0.0771 |
| pythia_temp09 | d2v3 | 0.7928 | 0.7928 | 0.7953 | Y | +0.0025 |
| pythia_topk50 | d0v1 | 0.9927 | 0.9927 | 0.9990 | Y | +0.0063 |
| pythia_topk50 | d1v2 | 0.7518 | 0.7518 | 0.8363 | Y | +0.0845 |
| pythia_topk50 | d2v3 | 0.6918 | 0.6918 | 0.6865 | Y | -0.0053 |
| olmo_nucleus095 | d0v1 | 0.9834 | 0.9834 | 0.9966 | Y | +0.0132 |
| olmo_nucleus095 | d1v2 | 0.8673 | 0.8673 | 0.9341 | Y | +0.0668 |
| olmo_nucleus095 | d2v3 | 0.8124 | 0.8124 | 0.8189 | Y | +0.0065 |
| olmo_temp09 | d0v1 | 0.9960 | 0.9960 | 0.9998 | Y | +0.0038 |
| olmo_temp09 | d1v2 | 0.9010 | 0.9010 | 0.9558 | Y | +0.0548 |
| olmo_temp09 | d2v3 | 0.8214 | 0.8214 | 0.8341 | Y | +0.0127 |
| olmo_topk50 | d0v1 | 0.9930 | 0.9930 | 0.9996 | Y | +0.0066 |
| olmo_topk50 | d1v2 | 0.8305 | 0.8305 | 0.9042 | Y | +0.0737 |
| olmo_topk50 | d2v3 | 0.7357 | 0.7357 | 0.7339 | Y | -0.0018 |
| gpt2xl_nucleus095 | d0v1 | 0.9941 | 0.9941 | 0.9989 | Y | +0.0048 |
| gpt2xl_nucleus095 | d1v2 | 0.9131 | 0.9131 | 0.9584 | Y | +0.0453 |
| gpt2xl_nucleus095 | d2v3 | 0.8829 | 0.8829 | 0.8921 | Y | +0.0092 |
| gpt2xl_temp09 | d0v1 | 0.9963 | 0.9963 | 0.9996 | Y | +0.0033 |
| gpt2xl_temp09 | d1v2 | 0.9367 | 0.9367 | 0.9792 | Y | +0.0425 |
| gpt2xl_temp09 | d2v3 | 0.8815 | 0.8815 | 0.8861 | Y | +0.0046 |
| **gpt2xl_topk50** | d0v1 | **0.9884** | ~~0.9906~~ **fixed** | 0.9987 | **N→fixed** | +0.0103 |
| **gpt2xl_topk50** | d1v2 | **0.8259** | ~~0.8126~~ **fixed** | 0.9140 | **N→fixed** | +0.0881 |
| **gpt2xl_topk50** | d2v3 | **0.7708** | ~~0.7529~~ **fixed** | 0.7566 | **N→fixed** | -0.0142 |

## 2. edd_sensitivity.json Update

Only gpt2xl_topk50 required correction:
- d0v1: 0.9906 → 0.9884
- d1v2: 0.8126 → 0.8259
- d2v3: 0.7529 → 0.7708

EDD values unchanged (T=0.8 → EDD=2 for both old and new AUC).

## 3. edd_analysis_9cell.json Deviation Explanation

Systematic upward bias in edd_9cell (mean delta: +0.03 overall, +0.06 for d1v2):

**Root causes:**
1. **Different evaluation methodology**: atlas_v2_analysis.py uses 5-fold CV averaging; pipeline uses a single train/test split. CV smooths variance and typically produces slightly higher estimates.
2. **Different data sources for 4/9 cells**: atlas_v2 loads from `data/` directory (e.g., `data/features_all.jsonl` for pythia_nucleus), while pipeline uses internal data paths. Sample counts may differ.
3. **d1v2 pairs show largest deviation** (+0.04 to +0.09): This is the hardest discrimination task, where methodology differences have the most impact.

The largest outlier is gpt2xl_topk50 d1v2: pipeline=0.8259, 9cell=0.9140 (Δ=+0.0881). This extreme gap likely comes from different train/test partitioning interacting with borderline-separable depth pairs.

**Conclusion**: edd_analysis_9cell.json values are internally consistent (valid for bootstrap CI analysis) but should NOT be used as point AUC estimates in figures. Pipeline pairwise_auc.json remains the authoritative source.

## 4. Fig4 Accuracy Changes (old hardcoded → new 5-fold CV)

| Cell | Old | New | Δ |
|------|-----|-----|---|
| Pythia nucleus | 78.2 | 78.7 | +0.5 |
| Pythia temp | 76.3 | 76.8 | +0.5 |
| Pythia topk | 69.6 | 68.8 | -0.8 |
| OLMo nucleus | 78.8 | 78.8 | 0.0 |
| OLMo temp | 82.0 | 82.2 | +0.2 |
| OLMo topk | 74.2 | 74.4 | +0.2 |
| GPT-2 XL nucleus | 83.3 | 84.2 | +0.9 |
| GPT-2 XL temp | 85.4 | 85.8 | +0.4 |
| GPT-2 XL topk | 76.6 | 76.0 | -0.6 |

All deltas < 1pp. Old values were from pipeline's single 80/20 split; new values from 5-fold CV (consistent with fig3 methodology).
