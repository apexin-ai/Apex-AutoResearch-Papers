# ROC-AUC Baselines (Binary: gen-1 vs gen-2+)

LOGO evaluation, 8 generators, document-level bootstrap CI (N=1000).

| Method | Binary F1 | ROC-AUC | 95% CI |
| --- | --- | --- | --- |
| FastDetectGPT | 0.5805 | 0.5796 | [0.5717, 0.5873] |
| Binoculars | 0.5327 | 0.6203 | [0.6133, 0.6271] |
| AvgLogProb | 0.6785 | 0.7844 | [0.7780, 0.7906] |
| LD-Score | 0.6758 | 0.7507 | [0.7422, 0.7584] |
| 4-Det Ensemble | 0.6983 | 0.8175 | [0.8116, 0.8234] |
| 7-Feature (Ours) | 0.6935 | 0.8111 | [0.8050, 0.8169] |
| Combined (4-Det + 7-Feature) | 0.7127 | 0.8304 | [0.8248, 0.8358] |

## Key observations

- All AUCs substantially exceed their corresponding F1 scores, indicating the XGBoost probability outputs are well-calibrated for ranking.
- 7-Feature (Ours) achieves AUC 0.811, competitive with the 4-Det Ensemble (0.818) despite using no external detector scores.
- Combined (all 11 features) reaches 0.830, the best overall.
- FastDetectGPT is near-random in AUC (0.58) for this binary depth task, consistent with its low F1.

## Reproduction

```bash
source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint
CUDA_VISIBLE_DEVICES="" python roc_auc_baselines.py
```

Results: `results/roc_auc_baselines.json`
