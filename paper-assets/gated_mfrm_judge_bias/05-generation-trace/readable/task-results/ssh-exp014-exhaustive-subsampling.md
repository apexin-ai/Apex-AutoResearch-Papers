# ssh exp014 exhaustive subsampling

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp014_exhaustive_subsampling_20260523T052727_result.json`
- **Structured JSON:** [`7c29414f73ad5a95bc5f.json`](../../sessions/7c/7c29414f73ad5a95bc5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正常运行中。第一个 subset (k=2) 的 MCMC warmup 已开始，约 ~140 it/s。

**已完成：**
- 创建 `/root/gated_mfrm_judge_bias/exp014/run_exp014.py`，穷举 C(9,k) 共 247 个 judge 组合
- 每个 subset 跑 3 种方法 (raw_average, sequential, joint_gmfrm)，MCMC 参数 warmup=1000, samples=1000, chains=2
- 支持断点续跑（已完成的 subset 会跳过）
- 每完成一个 subset 立即 flush 写入 CSV
- 已通过 `submit_training_job` 提交到 autodl-8gpu cuda:0，tmux session `exp-014`，日志 `~/runs/gated_mfrm_judge_bias/exp-014.log`

---
