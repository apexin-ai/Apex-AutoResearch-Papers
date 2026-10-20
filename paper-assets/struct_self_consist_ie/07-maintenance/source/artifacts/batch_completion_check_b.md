# Batch Completion Check B — 2026-05-16

## 1. exp_026_t05 (T=0.5 SciERC NER inference)

**Status**: COMPLETE  
**Path**: `output/exp_026_t05/`  
**Files**: `samples.jsonl` (551 lines, 20.7MB), `report.json` (1.7KB)  
**Timestamp**: 2026-05-16 20:23

### Key Metrics
| Metric | Value |
|--------|-------|
| Greedy F1 | 0.6647 |
| Oracle F1 | 0.7423 |
| Oracle headroom | 0.0776 |
| Fleiss κ mean | 0.5769 |
| Soft Jaccard mean | 0.8334 |
| ρ(SJ, F1) full | 0.2970 |
| ρ(FK, F1) full | 0.2563 |
| SJ rho advantage over FK | +0.0407 |
| Logprob AUROC (full) | 0.5781 |
| Logprob AUROC (conditional) | 0.5921 |
| Verdict | **FAIL** |

---

## 2. exp_026_t08 (T=0.8 SciERC NER inference)

**Status**: COMPLETE  
**Path**: `output/exp_026_t08/`  
**Files**: `samples.jsonl` (551 lines, 20.3MB), `report.json` (1.7KB)  
**Timestamp**: 2026-05-16 21:01

### Key Metrics
| Metric | Value |
|--------|-------|
| Greedy F1 | 0.6633 |
| Oracle F1 | 0.7684 |
| Oracle headroom | 0.1051 |
| Fleiss κ mean | 0.4514 |
| Soft Jaccard mean | 0.7491 |
| ρ(SJ, F1) full | 0.3589 |
| ρ(FK, F1) full | 0.2498 |
| SJ rho advantage over FK | +0.1091 |
| Logprob AUROC (full) | 0.5890 |
| Logprob AUROC (conditional) | 0.5509 |
| Verdict | **MARGINAL** |

### T=0.5 vs T=0.8 Comparison
| Metric | T=0.5 | T=0.8 | Δ |
|--------|-------|-------|---|
| Oracle headroom | 0.0776 | 0.1051 | +0.0275 |
| SJ ρ (full) | 0.2970 | 0.3589 | +0.0619 |
| SJ ρ advantage | 0.0407 | 0.1091 | +0.0684 |
| Logprob AUROC | 0.5781 | 0.5890 | +0.0109 |

T=0.8 has more headroom and SJ correlation advantage is much larger.

---

## 3. exp_019 Trained Verifier (Logistic Regression) — N=8

**Status**: COMPLETE  
**Path**: `output/exp_019_trained_verifier/`  
**Seeds**: [42, 123, 789], Dataset: SciERC NER, N=8

### Selection F1
| Method | Mean ± σ | vs Greedy |
|--------|----------|-----------|
| Greedy | 0.6469 ± 0.0037 | — |
| LR (supervised) | **0.6480 ± 0.0012** | **+0.0011** |
| LP (best unsup) | 0.6472 ± 0.0033 | +0.0003 |
| Oracle | 0.7816 ± 0.0064 | +0.1347 |

**Oracle gap closure: 0.8%** (LR closes 0.0011 of 0.1347 gap)

### Instance AUROC
| Method | Mean ± σ |
|--------|----------|
| VC (best single) | 0.7064 ± 0.0173 |
| LR (5 signals) | 0.6973 ± 0.0161 |
| SJ | 0.6842 ± 0.0111 |
| EM | 0.6512 ± 0.0073 |

LR AUROC vs best single (VC): **-0.0090** (does not exceed)

### LR Feature Coefficients (mean)
| Signal | Coefficient |
|--------|-------------|
| VC | **0.7474** |
| LP | 0.1049 |
| EM | 0.1021 |
| FK | 0.0894 |
| SJ | -0.1193 |

VC dominates; signals largely redundant.

---

## 4. exp_027 MLP + RF Verifiers — N=16

**Status**: COMPLETE  
**Path**: `output/exp_027_mlp_verifier/`  
**Seeds**: [42, 123, 456], Dataset: SciERC NER, N=16

### Main Results (3-seed mean)
| Model | Features | AUROC | Selection F1 | vs Greedy (0.6441) |
|-------|----------|-------|-------------|-----|
| LR | 5 | 0.6522 ± 0.0130 | 0.6406 ± 0.0010 | -0.0035 |
| MLP | 5 | 0.6393 ± 0.0209 | 0.6377 ± 0.0031 | -0.0064 |
| RF | 5 | 0.5868 ± 0.0208 | 0.6133 ± 0.0120 | -0.0308 |
| MLP | 15 | 0.6322 ± 0.0165 | 0.6339 ± 0.0079 | -0.0102 |
| RF | 15 | 0.6043 ± 0.0314 | 0.6143 ± 0.0148 | -0.0298 |
| Best unsup (LP) | 1 | — | 0.6470 | +0.0029 |
| Best single AUROC (EM) | 1 | 0.6476 | — | — |
| Oracle | — | — | 0.8231 | +0.1790 |

### Key Finding
**Features are the bottleneck, not model capacity.**
- MLP ≈ LR (AUROC delta = -0.0129): nonlinear model does NOT improve over LR
- RF underperforms both (AUROC = 0.5868)
- Interaction features (15-feat) provide marginal or no gain
- All supervised models FAIL to beat greedy on selection F1
- Best supervised AUROC (LR=0.6522) only marginally exceeds best single signal (EM=0.6476, delta=+0.0046)

### RF Feature Importance (15-feat, top 5)
| Feature | Importance |
|---------|-----------|
| FKxLP | 0.0888 |
| LPxEM | 0.0780 |
| LP | 0.0768 |
| SJxLP | 0.0761 |
| SJxEM | 0.0729 |

---

## Summary

| Experiment | Status | Key Result |
|-----------|--------|------------|
| exp_026_t05 | ✓ Complete | FAIL verdict; SJ ρ=0.297, headroom=0.078 |
| exp_026_t08 | ✓ Complete | MARGINAL verdict; SJ ρ=0.359, headroom=0.105 |
| exp_019 LR verifier | ✓ Complete | Gap closure 0.8%; LR barely beats greedy (+0.0011) |
| exp_027 MLP/RF verifier | ✓ Complete | Features are bottleneck; MLP/RF cannot beat LR |
