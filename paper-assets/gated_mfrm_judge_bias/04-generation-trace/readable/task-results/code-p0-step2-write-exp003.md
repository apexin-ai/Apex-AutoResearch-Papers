# code p0 step2 write exp003

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0_step2_write_exp003_20260522T123425_result.json`
- **Structured JSON:** [`3ed8fd5025daf8f30bbc.json`](../../sessions/3e/3ed8fd5025daf8f30bbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run passed all three verification criteria:

1. **Data loaded successfully**: 12,166 raw records → 4,250 binary observations after preprocessing (8 models, 316 items, 9 judges, 18.7% sparsity)
2. **Models ran without errors**: raw_average (0s), mfrm_only (116s), joint_gmfrm (~90s)
3. **No shape mismatches or index errors**: Evaluation completed, plots generated, results.json saved

Key results from dry-run (50 warmup/50 samples, not converged but structurally correct):
- **Arena Elo correlation**: Kendall-τ = 0.733 (p=0.056), Spearman-ρ = 0.886 (p=0.019) — strong agreement
- **Theta ranking**: gpt-4o > qwen2.5-72b > gpt-4o-mini > llama-3.3-70b > qwen3-8b > gemma-2-9b > gpt-4-0613 > gpt-3.5-turbo-0125
- **Contamination (c)**: gpt-4-0613 (3.80) and gpt-3.5-turbo-0125 (3.77) show highest susceptibility — both are older models heavily represented in training data
- **Output files**: 4 plots (theta_comparison, contamination_c, judge_severity, theta_vs_elo) + results.json + npy arrays

Files created in `/root/gated_mfrm_judge_bias/exp003/`:
- `data_loader.py` — loads/preprocesses judgment JSONL + exposure CSV
- `models.py` — 4 fitting methods (sparse observation format)
- `evaluation.py` — convergence diagnostics, WAIC, Arena correlation, plots
- `run_exp003.py` — main entry point with CLI args
- `README.md` — design decisions documentation

---
