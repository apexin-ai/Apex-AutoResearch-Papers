# R12: 5-Seed Holm-Bonferroni Analysis — HS vs Text (384d MiniLM)

## Setup
- **Method**: Paired bootstrap permutation test (1000 resamples, null-centered, two-sided)
- **Correction**: Holm-Bonferroni on 3 metrics per model-seed (bal_acc, precision, pre-CP FPR)
- **Split**: 70/30 train/test per seed
- **Classifier**: LogisticRegression(solver='lbfgs', C=1.0, class_weight='balanced', max_iter=2000)
- **Text baseline**: all-MiniLM-L6-v2 (384d)
- **Seeds**: [42, 123, 456, 789, 1024]

## Table 1: Per-seed results (4 models x 5 seeds)

| Model    |  Seed |     BA p |   Prec p |    FPR p |  3/3 HB |
|----------|-------|----------|----------|----------|---------|
| R1-8B    |    42 |   0.0040 |   0.0140 |   0.0140 |    PASS |
| R1-8B    |   123 |   0.0070 |   0.0030 |   0.2620 |    FAIL |
| R1-8B    |   456 |   0.0010 |   0.0700 |   0.9520 |    FAIL |
| R1-8B    |   789 |   0.0010 |   0.0000 |   0.0340 |    PASS |
| R1-8B    |  1024 |   0.0000 |   0.0000 |   0.0090 |    PASS |
| OT-7B    |    42 |   0.0000 |   0.0000 |   0.0000 |    PASS |
| OT-7B    |   123 |   0.0000 |   0.0000 |   0.0000 |    PASS |
| OT-7B    |   456 |   0.0000 |   0.0000 |   0.0000 |    PASS |
| OT-7B    |   789 |   0.0000 |   0.0000 |   0.0000 |    PASS |
| OT-7B    |  1024 |   0.0000 |   0.0000 |   0.0000 |    PASS |
| R1-32B   |    42 |   0.0000 |   0.0010 |   0.0120 |    PASS |
| R1-32B   |   123 |   0.0000 |   0.0000 |   0.0000 |    PASS |
| R1-32B   |   456 |   0.0060 |   0.0000 |   0.0000 |    PASS |
| R1-32B   |   789 |   0.0030 |   0.0000 |   0.0020 |    PASS |
| R1-32B   |  1024 |   0.0000 |   0.0010 |   0.0010 |    PASS |
| QwQ-32B  |    42 |   0.0000 |   0.0000 |   0.0010 |    PASS |
| QwQ-32B  |   123 |   0.0120 |   0.0080 |   0.0010 |    PASS |
| QwQ-32B  |   456 |   0.0120 |   0.0010 |   0.0000 |    PASS |
| QwQ-32B  |   789 |   0.0000 |   0.0000 |   0.0000 |    PASS |
| QwQ-32B  |  1024 |   0.0020 |   0.0010 |   0.0000 |    PASS |

## Table 2: Summary

| Model    | Pass  | Mean DPrec (pp)    | Mean DBA (pp)      |
|----------|-------|--------------------|--------------------|
| R1-8B    |   3/5 |  +14.62 +/-  4.49  |   +9.41 +/-  2.37  |
| OT-7B    |   5/5 |  +20.90 +/-  1.27  |  +11.34 +/-  1.48  |
| R1-32B   |   5/5 |  +13.71 +/-  1.99  |  +11.83 +/-  2.41  |
| QwQ-32B  |   5/5 |  +19.85 +/-  2.50  |  +11.44 +/-  3.18  |

## Key findings

1. **18/20 model-seed combos pass 3/3 HB** (90% overall passing rate)
2. **OT-7B, R1-32B, QwQ-32B**: 5/5 seeds pass (100%), all p-values well below HB thresholds
3. **R1-8B**: 3/5 seeds pass (60%); the 2 failures are driven by FPR (seed 123: p=0.262, seed 456: p=0.952), meaning HS does not consistently lower pre-CP FPR vs text on all R1-8B splits
4. **Largest HS advantage**: OT-7B (+20.90pp precision, +11.34pp BA) and QwQ-32B (+19.85pp precision, +11.44pp BA)
5. **Most stable**: OT-7B (std of DPrec = 1.27pp, DBA = 1.48pp)
6. **R1-8B instability**: FPR metric is seed-sensitive (std of DPrec = 4.49pp), likely due to small test set (63 traces at 30% split) and W=15 window creating high-dimensional features

## Data location
- Full JSON: `/root/autodl-tmp/contrastive_trace_safety/artifacts/r12_5seed_hb/full_results.json`
- Run log: `/root/autodl-tmp/contrastive_trace_safety/artifacts/r12_5seed_hb/run.log`
- Script: `/root/autodl-tmp/contrastive_trace_safety/scripts/r12_run_all.py`
