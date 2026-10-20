# ssh mcmc trigger check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mcmc-trigger-check_20260524T204020_result.json`
- **Structured JSON:** [`9ad6cb80b3c2ea5ce82d.json`](../../sessions/9a/9ad6cb80b3c2ea5ce82d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

### MCMC Phase 1
- **已成功自动启动**，PID 614592，04:39:29 CST 触发
- 当前正在跑 `mfrm_only` 模型的 warmup 阶段（~3% / 10000 iterations，~4.33 it/s，acc. prob=0.92）
- `raw_average` 模型已完成
- 使用 GPU 0，占用 667 MiB，利用率 76%

### 数据汇总
- 6 个 judge 纳入建模（排除了 mistral-large-2），33931 observations
- N=18 models, I=500 items, J=6 judges

### Qwen3 最终行数
- `qwen3-235b-proxy`: 2091 行（n=1）
- `qwen3-235b-proxy_n17`: 21519 行（n17）

### DeepSeek 当前进度
- `deepseek-v4-pro-proxy`: 1433 行（n=1，与启动 MCMC 时相同）
- `deepseek-v4-pro-proxy_n17`: 16257 行（从 16219 增长到 16257，仍在采集中）

### GPU 使用
| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 667 MiB | 76% (MCMC) |
| 1-3 | 0 MiB | 0% |

GPU 1-3 空闲，DeepSeek 走的是 API proxy 所以不占本地 GPU。一切按预期运行。

---
