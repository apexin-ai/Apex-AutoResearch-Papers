# analysis simulation binary recovery

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_simulation_binary_recovery_20260521T093639_result.json`
- **Structured JSON:** [`cf55245f27103f976117.json`](../../sessions/cf/cf55245f27103f976117.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Simulation complete. Results saved to `results/analysis/simulation_binary_recovery.json` on server.

## Results Summary

**Design**: 100 replications × 4 accuracy levels (p=0.5–0.8) × 3 sample sizes (n=50, 100, 200), 432 conditions/item, probit latent model with 22 known variance components.

**Validation**: Fast numpy Henderson I matches DataFrame implementation (max diff = 1.39e-17).

### Key Findings

| Metric | Result |
|---|---|
| **item_id dominant** (excl. residual) | **99–100%** across all conditions |
| **Spearman rho** (excl. residual) | **0.685–0.734** (mean 0.708) |
| **Top-5 systematic set correct** | **58–82%** (mean 72%) |
| **Coverage (95% CI)** | **86–100%** |

### Binary vs Continuous Control

| | Binary (mean) | Continuous (mean) |
|---|---|---|
| Spearman rho (no residual) | 0.708 | 0.703 |

Binary performs **equivalently** to continuous — the probit binarization does not degrade ranking recovery.

### Binary-Scale Distortion

Residual inflates from 16% (latent) to ~40% (binary scale) because it absorbs the within-cell Bernoulli variance p(1-p). However, the **systematic component ordering is perfectly preserved** in the oracle:

- Latent: item_id (50%) > prec:item (7%) > temp:item (6%) > prompt:item (5%)
- Binary oracle: item_id (33%) > prec:item (6.3%) > temp:item (5.1%) > prompt:item (4.3%)

### Robustness

- **Bias by accuracy**: 0.34–0.42% (flat, no increase at p=0.8)
- **Rho by accuracy**: 0.70–0.71 (stable)
- **Rho improves with n_items**: 0.69 (n=50) → 0.72 (n=200)

---
