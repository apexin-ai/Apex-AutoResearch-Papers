# Rho Consistency Audit Report

**Date**: 2026-05-15
**Trigger**: Reviewer flagged large discrepancies between registry rho values and bootstrap CI rho values

## Root Cause

The discrepancy comes from two different evaluation pipelines using different instance filtering:

### Old Pipeline (`compute_metrics.py`)
- **No filtering**: uses ALL instances including gold-empty ones
- **FK bug**: `compute_fk()` returns 0.0 when all samples predict no entities (should be 1.0 = perfect agreement on empty set)
- **F1 convention**: returns 0.0 when tp=0, including when both pred and gold are empty

### New Pipeline (`eval_n16_5signal.py`, `fk_bootstrap_ci.py`, `analyze_exp017_*.py`)
- **Filters out gold-empty instances**: `len(gold.get("entities", [])) > 0`
- **Uses `consistency.py`**: `fleiss_kappa_surface()` returns 1.0 for all-empty (correct)
- **Reports n_valid** separate from n_total

### Mechanism of Inflation / Deflation

For CoNLL2003 (3453 test sentences), **697 instances (20.2%) have zero gold entities**.

For these gold-empty instances in the old pipeline:
- All samples typically predict few/no entities → **FK ≈ 0.04** (buggy), **F1 = 0.0**
- All samples agree on empty output → **SJ ≈ 0.98**, **F1 = 0.0**

Adding 697 points at (FK≈0, F1=0) creates a strong artificial cluster that inflates Spearman rho for FK.
Adding 697 points at (SJ≈1, F1=0) creates an anti-correlated cluster that deflates Spearman rho for SJ.

This is why FK rho jumped from 0.48 to 0.81, while SJ rho dropped from 0.48 to 0.18 — a complete **rank reversal**.

## Affected Experiments

| exp_id | Signal | Old (registry) | New (correct) | Delta | Instance Change |
|--------|--------|----------------|---------------|-------|-----------------|
| exp_017_llama_conll_n16_r1024 | FK | **0.8095** | **0.4752** | -0.3343 | 3453→2756 |
| exp_017_llama_conll_n16_r1024 | SJ | **0.1815** | **0.4836** | +0.3021 | 3453→2756 |
| exp_017_llama_conll_n16_s456_r1024 | FK | **0.8085** | **0.4690** | -0.3395 | 3453→2756 |
| exp_017_llama_conll_n16_s456_r1024 | SJ | **0.1895** | **0.4734** | +0.2839 | 3453→2756 |
| exp_001_n16_seed456 | FK | **0.3448** | **0.2723** | -0.0725 | 551→529 |
| exp_001_n16_seed456 | SJ | **0.4134** | **0.4098** | -0.0036 | 551→529 |
| exp_011_ood_conll_to_scierc | FK | -0.069 | -0.0695 | ~0 | Already correct |
| exp_011_ood_conll_to_scierc | SJ | -0.186 | -0.1857 | ~0 | Already correct |

## Correct (Unified) Pipeline Specification

**Filter**: Exclude instances where `len(gold.get("entities", [])) == 0`
**FK implementation**: `consistency.py::fleiss_kappa_surface()` (returns 1.0 for all-empty samples)
**SJ implementation**: `consistency.py::structural_consistency_soft_jaccard()`
**F1**: `evaluation.py::per_instance_f1()` (per-instance, not micro-averaged)
**Spearman rho**: `scipy.stats.spearmanr` on (signal, F1) pairs, excluding NaN

## Unified Rho Values (Full Split, Gold-Filtered)

### LLaMA CoNLL seed42 (n=2756)
| Signal | rho | AUROC |
|--------|-----|-------|
| FK | 0.4752 | 0.7467 |
| SJ | 0.4836 | 0.7496 |
| VC | 0.4746 | 0.7529 |
| EM | 0.4818 | 0.7508 |
| LP | 0.3136 | 0.7661 |

### LLaMA CoNLL seed456 (n=2756)
| Signal | rho | AUROC |
|--------|-----|-------|
| FK | 0.4690 | 0.7408 |
| SJ | 0.4734 | 0.7428 |
| VC | 0.4722 | 0.7495 |
| EM | 0.4752 | 0.7444 |
| LP | 0.3099 | 0.7628 |

### Qwen SciERC seed456 NER (n=529)
| Signal | rho | AUROC |
|--------|-----|-------|
| FK | 0.2723 | 0.6179 |
| SJ | 0.4098 | 0.6823 |
| VC | 0.4449 | 0.6981 |
| EM | 0.3363 | 0.6490 |
| LP | 0.2415 | 0.5885 |

### Qwen SciERC seed456 RE (n=397)
| Signal | rho |
|--------|-----|
| FK | 0.2929 |
| SJ | 0.2835 |

### OOD ConLL→SciERC (n=529, already correct in registry)
| Signal | rho |
|--------|-----|
| FK | -0.0695 |
| SJ | -0.1857 |

## Impact on Paper

1. **LLaMA CoNLL results need correction**: The claim that FK dominates (rho=0.81) is wrong. With correct filtering, all structural signals have similar rho (~0.47-0.48), and SJ slightly edges FK.
2. **Rank reversal resolved**: SJ and FK are now comparable rather than opposite.
3. **SciERC seed456 minor change**: FK drops from 0.34 to 0.27; SJ essentially unchanged.
4. **Key narrative change**: The story shifts from "FK is best for NER" to "all structural signals are comparable; logprob is weaker" — which is actually a cleaner finding.

## Registry Updates Required

- `exp_017_llama_conll_n16_r1024`: replace flat rho metrics with new pipeline values
- `exp_017_llama_conll_n16_s456_r1024`: replace flat rho metrics with new pipeline values
- `exp_001_n16_seed456`: replace flat rho metrics with new pipeline values
- `exp_011_ood_conll_to_scierc`: no change needed (already correct)
