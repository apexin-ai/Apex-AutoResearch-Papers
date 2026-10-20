# ssh p0 exp003 readiness and launch

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0_exp003_readiness_and_launch_20260522T121335_result.json`
- **Structured JSON:** [`f343e90e86ef2cf440f0.json`](../../sessions/f3/f343e90e86ef2cf440f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the readiness report.

---

## exp-003 Readiness Report

### 1. Coverage Matrix (exp-001)

**9 judges × 9 models, 12,122 total judgments. THRESHOLD MET: YES**

All 9 models have ≥5 judges with ≥20 items. Minor gaps:
- `gemma-2-9b`: 8/9 judges ≥20 (mistral-large-2 only 14)
- `qwen3-8b`: 7/9 judges ≥20 (deepseek 19, llama 19)

Data sufficient to proceed.

### 2. exp-002 Inputs

**Available and complete:**
- `exposure_scores.csv` — 493 items, columns: `item_id, e_i, source_a_z, source_b_z, source_c_z, n_sources`
- `summary.json` — 493 items, 10 judges, 2 target models (`gpt-3.5-turbo-0125`, `gpt-4-0613`), ref=`gpt-4-0314`
- `model_abilities.csv` — `model, ability, n_items`
- `win_rates_with_residuals.csv` — `item_id, model, win_rate, n_judgments, difficulty, expected_wr, residual`

### 3. exp-003 Code Status

**exp003/ directory does NOT exist. No exp003 code anywhere. Must be created from mvp_003.**

### 4. MVP → Real Data Gap Analysis

| Component | MVP (synthetic) | Real Data | Change needed |
|-----------|----------------|-----------|---------------|
| **Data format** | 3D tensor Y[N,I,J] from `generate_mvp002_data()` | Pairwise JSONL: `{item_id, model_a, model_b, judge, score(0/0.5/1), position}` | Build data loader to convert pairwise judgments → binary response tensor |
| **Dimensions** | N=50 models, I=100 items, J=8 judges | N=9 models, I=493 items, J=9 judges | Parametric, just feed real dims |
| **e_i values** | `data["true_params"]["e"]` (synthetic) | `exp002/results/exposure_scores.csv` → `e_i` column | Load CSV, match by item_id |
| **Evaluation** | `compute_metrics(theta_hat, theta_true)` — RMSE/Kendall-τ vs ground truth | **No ground truth θ** in real data | Need alternative: convergence (R-hat, ESS), model comparison (WAIC/LOO), win-rate calibration, c_hat analysis |
| **Model code** | `models_v3.py` — MFRM + G-MFRM NumPyro | Reusable as-is | Copy to exp003, adjust `numpyro.set_host_device_count` |
| **Seeding** | 20 seeds × same DGP | Single real dataset, no reseeding | One fit per method (or multi-chain for uncertainty) |

### 5. Key Engineering Tasks to Create exp003

1. **Data loader**: Parse exp-001 JSONL → construct Y[N,I,J] tensor. Handle: binarization of 0/0.5/1 scores, position debiasing (AB/BA), missing cells (sparse matrix), item_id → index mapping.
2. **e_i loader**: Read `exposure_scores.csv`, align item indices with judgment data.
3. **Model adaptation**: Copy `models_v3.py`, handle sparse observations (mask missing cells in likelihood).
4. **Evaluation framework**: Replace synthetic-truth metrics with: (a) convergence diagnostics, (b) WAIC/LOO model comparison, (c) calibrated win-rate analysis, (d) c_hat interpretation.
5. **Output**: Results JSON + CSV + diagnostic plots.

### 6. Verdict

**Cannot launch exp-003 immediately — needs ~2-3 hours of code writing.**

The critical blocker is the data loader (pairwise JSONL → tensor) and the evaluation framework (no ground truth). The MCMC model code from mvp_003 is directly reusable. exp-002's e_i outputs are ready.

---
