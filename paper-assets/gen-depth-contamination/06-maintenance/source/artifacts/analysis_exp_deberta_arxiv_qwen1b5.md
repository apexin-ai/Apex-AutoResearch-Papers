# Experiment Analysis: exp_deberta_arxiv_qwen1b5

## Summary

| Item | Value |
|------|-------|
| K*(DeBERTa) | **4** |
| K*(OBD) | **3** |
| Hypothesis (K*=3 match) | **NEGATIVE** |
| Status | Completed successfully (EXIT_CODE=0) |
| Runtime | 1972s (~33min) |
| Date | 2026-05-20 |

## Result: K*(DeBERTa)=4 ≠ K*(OBD)=3

DeBERTa supervised classifier yields K*=4 on arXiv domain, **not** K*=3 as hypothesized. The representation-independent domain ceiling claim does NOT hold for arXiv: a stronger classifier pushes the distinguishability boundary one depth further than OBD.

## Pairwise AUC (5-fold GroupKFold OOF, n_boot=10000, theta=0.6)

| Pair | DeBERTa AUC | 95% CI | CI_lower > θ | OBD AUC | Delta |
|------|-------------|--------|--------------|---------|-------|
| 0v1 | 0.9997 | [0.9992, 1.0000] | YES | 0.9948 | +0.0049 |
| 1v2 | 0.9214 | [0.9143, 0.9285] | YES | 0.8581 | +0.0633 |
| 2v3 | 0.7446 | [0.7333, 0.7559] | YES | 0.6436 | +0.1010 |
| 3v4 | 0.6238 | [0.6127, 0.6349] | YES (borderline) | 0.5440 | +0.0798 |
| 4v5 | 0.5771 | [0.5659, 0.5882] | NO | 0.5299 | +0.0472 |

## K* Calculation Logic

K* = max consecutive depth pairs from 0v1 where CI_lower > theta (0.6). If any pair fails, stop.

- 0v1: 0.9992 > 0.6 -> K>=1
- 1v2: 0.9143 > 0.6 -> K>=2
- 2v3: 0.7333 > 0.6 -> K>=3
- 3v4: 0.6127 > 0.6 -> K>=4 **(borderline: only 0.0127 above threshold)**
- 4v5: 0.5659 < 0.6 -> STOP

**K* = 4**

## Critical Observation: 3v4 is Borderline

The 3v4 pair is the pivotal discrepancy. DeBERTa's CI_lower (0.6127) exceeds θ=0.6 by only **0.0127**. This is statistically significant per the bootstrap test but practically marginal. The OBD method scores 0.544 on the same pair, well below threshold.

This means DeBERTa extracts enough signal from raw text to weakly distinguish depth-3 vs depth-4 in arXiv, while OBD statistical features cannot. The distinction is representation-dependent at this boundary.

## Training Diagnostics

- Loss curves show normal convergence across all 5 folds
- Epoch progression (representative fold): 1.27 -> 0.98 -> 0.87 (avg loss)
- No signs of overfitting (loss consistently decreasing through epoch 3)
- All folds show consistent patterns (train=10560, val=2640 per fold)
- DeBERTa-v3-base loaded correctly (expected MISSING keys for classifier head, UNEXPECTED keys for MLM head)

## Implications for Paper

1. **arXiv breaks the representation-independence narrative.** The other 3 domains (C4 K*=2, wiki K*=3, code K*=2) showed DeBERTa K* = OBD K*. arXiv is the exception where DeBERTa pushes K* from 3 to 4.

2. **Possible framings:**
   - The ceiling is *approximately* representation-independent: 3/4 domains match exactly, and the 4th (arXiv) differs by only one depth level at a borderline margin.
   - Report as a nuance: OBD provides a conservative lower bound; supervised classifiers can push slightly further in some domains.
   - The 3v4 margin (CI_lower=0.6127) is so close to threshold that a slightly different θ (e.g., 0.62) would recover K*=3.

3. **Sensitivity analysis recommended:** Test θ in {0.55, 0.60, 0.62, 0.65} to show how borderline this is.

## Configuration

- Model: microsoft/deberta-v3-base
- Data: data/exp_024_arxiv/, 13200 samples (2200 docs x 6 depths)
- 5-fold GroupKFold (group by doc_id)
- Epochs: 3, BS: 16, grad_accum: 2 (effective BS=32), LR: 2e-5
- Max length: 512, warmup: 10%, weight decay: 0.01
- Bootstrap CI: n_boot=10000, 95% CI
- Threshold θ=0.60

## File Locations

- Log: `~/runs/gen-depth-contamination/exp_deberta_arxiv_qwen1b5.log`
- Results JSON: `/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_arxiv/arxiv_qwen1b5.json`
- Script: `/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_arxiv.py`
