# ssh exp006 k9 parallel

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp006_k9_parallel_20260523T002423_result.json`
- **Structured JSON:** [`d56ad7e41d52f9d74e72.json`](../../sessions/d5/d56ad7e41d52f9d74e72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已成功启动。

**汇报：**

- **启动命令**：`CUDA_VISIBLE_DEVICES=3 python3 run_exp006.py --methods raw_average joint_gmfrm sequential --judge-counts 9 --output-dir results_k9`（tmux session: `exp006_k9`）
- **状态**：已启动，MCMC sampling 进行中（GPU 3 占用 667MiB, 62% util）
- **k=9 只有 1 个 subset**（9 个 judges 里选 9 个，只有 C(9,9)=1 种组合），所以是 1 subset × 3 methods = **3 fits**（不是 30）
- **预估 ETA**：3 个 MCMC fits（raw_average 不需要 MCMC，实际 2 个 MCMC fits: joint_gmfrm + sequential），每个 ~3-5 分钟，总计约 **10-15 分钟**

---
