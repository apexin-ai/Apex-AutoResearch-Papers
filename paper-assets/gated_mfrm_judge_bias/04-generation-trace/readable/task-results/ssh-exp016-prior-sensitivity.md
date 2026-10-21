# ssh exp016 prior sensitivity

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp016_prior_sensitivity_20260523T054734_result.json`
- **Structured JSON:** [`f18c096b6f8da3269229.json`](../../sessions/f1/f18c096b6f8da3269229.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job submitted.

- **exp_id**: exp-016
- **server**: autodl-8gpu, cuda:2
- **tmux session**: `exp-016`
- **log**: `~/runs/gated_mfrm_judge_bias/exp-016.log`

脚本会依次跑 4 种 c_n 先验（HalfNormal(1.5) → Exponential(1.0) → LogNormal(0,1) → Gamma(2,1)），每种 4 chains × 2000 warmup + 4000 samples。预计总耗时 1-2 小时。结果输出到 `/root/gated_mfrm_judge_bias/exp016/results/prior_sensitivity.csv`。

---
