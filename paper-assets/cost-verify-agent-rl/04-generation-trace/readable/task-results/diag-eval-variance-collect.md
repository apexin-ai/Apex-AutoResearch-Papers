# diag eval variance collect

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_variance_collect_20260523T222329_result.json`
- **Structured JSON:** [`6a65d13d966cf8fc383b.json`](../../sessions/6a/6a65d13d966cf8fc383b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data. Here's the complete report:

## Eval Variance P1 Results

**Experiment**: 3 checkpoints × 3 eval seeds, 134 OOD tasks, τ=0.4
**Duration**: 2026-05-24 02:40–06:19 CST (~3h40m)
**Server**: bjb1-17606, 1× RTX PRO 6000 Blackwell (CUDA 13.1)

| checkpoint | run | success_rate | n_tasks | wandb_run_id | status |
|------------|-----|-------------|---------|--------------|--------|
| seed300 | s0 | 0.0% (0/134) | 134 | 917iymuy | done (invalid: enable_think=False) |
| seed300 | s1 | 0.0% (0/134) | 134 | xkd98fme | done (invalid: enable_think=False) |
| seed300 | s2 | 0.0% (0/134) | 134 | fztzhfcc | done (invalid: enable_think=False) |
| seed7hk | s0 | — | — | zcqqnd4c | **CRASHED** |
| seed7hk | s1 | — | — | pl1gnbps | **CRASHED** |
| seed7hk | s2 | — | — | 27nyg5ej | **CRASHED** |
| seed200 | s0 | 11.19% (15/134) | 134 | w6llb7y4 | done |
| seed200 | s1 | 11.19% (15/134) | 134 | 6c1cxb7m | done |
| seed200 | s2 | 13.43% (18/134) | 134 | 9h7yctzz | done |

### seed7hk crash root cause
All 3 runs hit `ValueError: Unsupported model: /root/autodl-tmp/checkpoints/exp029_seed7_high_kl_step5_hf` in `ctx_manager.py:35 get_special_tokens()`. The tokenizer's `name_or_path` is a local path that doesn't match any recognized model name. The crash occurs during `formulate_rollouts()` — env interactions ran for ~25 minutes but results were lost when post-processing failed.

### seed200 variance summary
- Rates: 11.19%, 11.19%, 13.43%
- Mean: 11.94%
- Std: 1.29 pp (sample std)
- Raw counts: 15, 15, 18 out of 134

### Key observations
1. **seed300**: 0% across all seeds confirms this checkpoint is non-functional (enable_think=False as expected)
2. **seed7hk**: needs code fix in `get_special_tokens()` to handle local checkpoint paths, then re-run
3. **seed200**: moderate variance (~1.3 pp), with 2/3 runs identical and 1 outlier — 3 more tasks solved in s2

---
