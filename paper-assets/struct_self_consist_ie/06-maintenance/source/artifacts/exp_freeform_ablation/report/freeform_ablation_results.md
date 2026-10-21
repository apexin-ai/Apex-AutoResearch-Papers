# Free-form vs Constrained Decoding Ablation (Qwen SciERC N=8)

**Date**: 2026-05-15
**Constrained baseline**: exp_012_rerun_1024 (551 instances × 8 samples)
**Free-form**: exp_freeform_ablation (551 instances × 8 samples, 4408 total)

---

## 1. Logprob Distribution Comparison

| Metric | Constrained | Free-form | Ratio (F/C) |
|--------|------------|-----------|-------------|
| Mean LP std | 0.0206 | 0.0199 | 0.97x |
| Median LP std | 0.0136 | 0.0137 | 1.01x |
| Mean LP range | 0.0623 | 0.0599 | 0.96x |
| Median LP range | 0.0413 | 0.0418 | 1.01x |
| Tied fraction (ε=0.05) | 59.7% | 57.7% | -2.0pp |
| N instances | 551 | 551 | — |

## 2. Selection F1

### NER

| Method | Constrained | Free-form |
|--------|------------|-----------|
| Greedy F1 | 0.6182 | 0.6204 |
| LP-selected F1 | 0.6241 | 0.6222 |
| Selection gap | +0.0059 | +0.0018 |

### RE

| Method | Constrained | Free-form |
|--------|------------|-----------|
| Greedy F1 | 0.2913 | 0.2880 |
| LP-selected F1 | 0.2845 | 0.3050 |
| Selection gap | -0.0068 | +0.0169 |

## 3. QE Signals: Spearman ρ and AUROC

### NER (n=529)

| Signal | C_ρ | C_AUROC | F_ρ | F_AUROC | Δρ |
|--------|-----|---------|-----|---------|-----|
| SJ | 0.3599 | 0.7180 | 0.3774 | 0.7463 | +0.0175 |
| FK | 0.2665 | 0.7478 | 0.3197 | 0.7621 | +0.0532 |
| LP | 0.2052 | 0.6548 | 0.2129 | 0.6984 | +0.0077 |
| EM | 0.2945 | 0.4998 | 0.3171 | 0.5190 | +0.0225 |
| VC | 0.3792 | 0.7721 | 0.4089 | 0.7958 | +0.0297 |

### RE (n=397)

| Signal | C_ρ | C_AUROC | F_ρ | F_AUROC | Δρ |
|--------|-----|---------|-----|---------|-----|
| SJ | 0.2503 | 0.6099 | 0.2728 | 0.6173 | +0.0225 |
| FK | 0.2752 | 0.6638 | 0.3145 | 0.6837 | +0.0393 |
| LP | 0.2662 | 0.6780 | 0.3042 | 0.7025 | +0.0379 |
| EM | 0.1344 | 0.4886 | 0.1367 | 0.4877 | +0.0024 |
| VC | 0.3498 | 0.6820 | 0.3234 | 0.6553 | -0.0263 |

## 4. Parse Rate Statistics

| Metric | Value |
|--------|-------|
| Total samples | 4408 |
| Successfully parsed | 4406 |
| Parse rate | 99.95% |
| 8/8 valid instances | 549 (99.6%) |
| 7/8 valid instances | 2 (0.4%) |
| Total failed samples | 2 |

## 5. Key Findings

1. **Score compression hypothesis NOT confirmed**: Free-form LP variance is virtually identical to constrained (ratio 0.97x for std, 0.96x for range). Removing constrained decoding did NOT meaningfully increase logprob spread. The tied fraction decreased by only 2.0pp (59.7% → 57.7%). This suggests logprob compression is intrinsic to the model/task, not an artifact of constrained decoding.

2. **QE signals uniformly improve under free-form** (except RE voting_conf): All 5 signals show higher ρ in NER (+0.0077 to +0.0532). In RE, 4 of 5 signals improve (+0.0024 to +0.0393), with only VC declining (-0.0263). FK shows the largest consistent gains (NER +0.0532, RE +0.0393).

3. **LP selection shows divergent behavior by subtask**: NER selection gain shrinks from +0.0059 (constrained) to +0.0018 (free-form). RE selection flips from negative (-0.0068) to strongly positive (+0.0169). Free-form enables effective LP-based selection for RE where constrained decoding failed.

4. **Near-perfect parse rate (99.95%)**: Only 2 of 4408 samples failed parsing, and 549/551 instances (99.6%) have all 8 samples valid. Free-form decoding with Qwen on SciERC is highly reliable — constrained decoding is not needed for format compliance.

5. **Greedy F1 is comparable across conditions**: NER greedy F1 differs by only 0.0022 (0.6182 vs 0.6204) and RE by 0.0033 (0.2913 vs 0.2880), confirming the comparison is apples-to-apples on a well-matched task difficulty.
