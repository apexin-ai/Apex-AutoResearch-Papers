# ssh exp013 weight sensitivity

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp013_weight_sensitivity_20260523T040709_result.json`
- **Structured JSON:** [`3ab61f367d3e439b06a6.json`](../../sessions/3a/3ab61f367d3e439b06a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交。配置：
- 4 种权重配置（50/50, 75/25, 90/10, 100/0）
- 每种：加载对应 exposure scores → joint G-MFRM MCMC (warmup=2000, samples=2000, chains=2) → Kendall τ vs Arena Elo + exposure Spearman ρ vs default
- 输出：`exp013/results/weight_sensitivity.csv` + 每个配置的 theta/c JSON

MCMC 用了 chains=2、samples=2000 的配置（任务说明允许的较短 chain），4 个配置串行，预计总运行 30-60 分钟。需要我过一会儿检查进度吗？

---
