# ssh exp013 status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp013_status_check_20260523T043953_result.json`
- **Structured JSON:** [`d0b5eead4d37082bd294.json`](../../sessions/d0/d0b5eead4d37082bd294.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-013 仍在运行中。**

| 项目 | 状态 |
|------|------|
| PID 558426 | 运行中，已 30 分 14 秒 |
| GPU cuda:0 | 占用 73,530 MiB |
| MCMC 进度 | `sample 3497/4000`（87%），~4.09 it/s，acc. prob=0.95 |
| 结果目录 | 已创建但为空，尚无 `weight_sensitivity.csv` |

当前正在拟合 joint G-MFRM（warmup=2000, samples=2000, chains=2），数据规模：9 个 judge、402 items、17,537 observations。当前 chain 剩余 ~503 iterations，约 2 分钟完成此 chain。

因为实验包含 4 种权重配置，每个都要跑完整 MCMC，当前看起来还在第一个配置（或前几个），预计还需 15-30 分钟。

---
