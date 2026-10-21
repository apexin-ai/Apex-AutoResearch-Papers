# ssh mcmc phase1 complete analysis

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mcmc-phase1-complete-analysis_20260525T045424_result.json`
- **Structured JSON:** [`e3fa08bf991df57be5d1.json`](../../sessions/e3/e3fa08bf991df57be5d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the status report.

---

## MCMC Phase 1 — Status Report

### COMPLETION STATUS
```
Status: FAILED (previous run killed during joint_gmfrm chain 3/4 at 90%)
Re-launched: PID 2598, robust script with incremental saving
Estimated completion: ~8h from now (~21:00 UTC+8)
```

**Root cause:** Process killed externally during joint_gmfrm's 3rd chain at sample 9038/10000. No OOM, no Python error. All 4 methods ran sequentially; mfrm_only (9208.8s) and sequential (9585.5s) completed but nothing was saved because the script only writes output at the end. The new script saves each method immediately.

**Data update:** Current run has more data than the killed run — 88,803 raw records (was 83,311). deepseek-v4-pro-proxy grew from 4,993 to 7,293 obs (81% coverage now).

### DRY RUN RESULTS (warmup=10, samples=10, chains=1 — DIRECTIONAL ONLY)

These are from the N=17 dry run with trivial MCMC budget. raw_average is deterministic and reliable; MCMC-based methods are noise.

**τ/ρ Table (dry run):**

| Method | N=17 τ | N=17 ρ | N=7† τ | N=7† ρ |
|--------|--------|--------|--------|--------|
| raw_average | **0.824** | 0.939 | 0.810 | 0.893 |
| mfrm_only | 0.691 | 0.846 | 0.905 | 0.964 |
| sequential | 0.588 | 0.775 | 0.810 | 0.893 |
| joint_gmfrm | 0.779 | 0.919 | 0.810 | 0.893 |

†N=7 = subset of models overlapping with N=8 experiment (excl. qwen3-8b)

**D045 gate (dry run, UNRELIABLE):** Δτ = 0.779 - 0.824 = **-4.5pp → FAIL** (but 10 samples is noise)

**c_n from dry run (unreliable extremes):**
- gpt-4-turbo: 6.63 (extreme, likely noise)
- claude-3-5-sonnet: 3.69
- gpt-4-0613: 3.08

**d_j judge severity (dry run):**

| Judge | d_j | Interpretation | Coverage |
|-------|-----|---------------|----------|
| deepseek-v4-pro-proxy | +0.44 | Lenient | 81.0% |
| gemini-2.5-pro-proxy | +0.34 | Lenient | 33.4% |
| claude-sonnet-4.6-proxy | +0.31 | Lenient | 48.6% |
| qwen3-235b-proxy | -0.12 | Neutral | 81.3% |
| qwen2.5-72b | -0.46 | Strict | 79.1% |
| llama-3.3-70b | -0.51 | Strict | 79.1% |

### N=8 BASELINE (output_003b, RELIABLE)

| Metric | Value |
|--------|-------|
| R-hat max | 1.04 (PASS) |
| ESS min | 174 (PASS) |
| Divergences | 0 |
| joint_gmfrm τ | **0.857** (p=0.002) |
| joint_gmfrm ρ | 0.952 (p=0.0003) |

**N=8 → N=17 comparison (dry run):**
- θ rank τ between N=8 and N=17: 0.905 (high consistency)
- c rank τ: 0.143 (contamination estimates differ drastically — noise from 10-sample dry run)
- d rank τ: 0.867
- Arena τ delta: N=8 0.857 → N=17 0.779, Δ = -0.078

### WHAT'S RUNNING

```
PID: 2598 on autodl-8gpu (4× RTX PRO 6000 Blackwell, 1TB RAM)
Script: run_n17_phase1_robust.py
Config: warmup=6000, samples=4000, chains=4, target_accept=0.95
Data: N=18, I=500, J=6, n_obs=36,231
GPU: CUDA:0 (single GPU to reduce memory pressure)
```

**Progress:** mfrm_only chain 1 warmup started, ~4 it/s. Each method takes ~2h48m. Total ~8h.

### NEXT STEPS

When the MCMC completes, I need to:
1. Verify convergence (R-hat < 1.05, ESS > 100)
2. Run the analysis pipeline (`compute_tau_n17.py`, `gen_table_latex.py`, `compare_n8_n17.py`)
3. Extract full d_j posteriors (95% CI) and c_n distributions
4. Evaluate D045 decision gate with real estimates

Want me to check progress periodically, or should I wait for you to prompt me?

---
