# ssh quick status all

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_quick_status_all_20260522T234328_result.json`
- **Structured JSON:** [`77f3291eda09036e6031.json`](../../sessions/77/77f3291eda09036e6031.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### autodl-8gpu

| 实验 | GPU | 进度 | ETA | 状态 |
|------|-----|------|-----|------|
| **exp-006** (sensitivity full) | cuda:1 (68%, 865M) | [26/31] configs, MCMC 2613/3000 (87%) | ~45-60min (sensitivity 部分) + LOOCV | 🟢 运行中 |
| **W7 ablation** | cuda:2 (65%, 4.9G) | [17/20] seeds, binary_gating ~400s/method | ~30-45min | 🟢 运行中 |
| **WAIC/orchestrator2** | cuda:0 (0%, 0M) | — | — | ⚪ 无活跃进程，GPU 空闲 |

### rtx6000-4x

| 实验 | GPU | 进度 | ETA | 状态 |
|------|-----|------|-----|------|
| **Mistral judge** | cuda:3 (100%, 90G) | 7500/8742 (86%) | ~107min (~1.8h) | 🟢 运行中 |
| **Llama shard A** | cuda:2 (100%, 91G) | 30/2664 (刚启动) | ~477min (~8h) | 🟢 刚启动 |
| **Llama shard B** | cuda:1 (100%, 91G) | 30/2135 (刚启动) | ~477min (~8h) | 🟢 刚启动 |
| — | cuda:0 (0%, 0M) | — | — | ⚪ 空闲 |

**要点：**
- autodl-8gpu 的 exp-006 和 w7 ablation 预计 1h 内完成 sensitivity/ablation 部分（exp-006 还有 LOOCV 待跑）
- rtx6000-4x 的 Mistral 约 2h 完成；Llama 双分片刚启动，预计 8h+
- autodl-8gpu cuda:0 和 rtx6000-4x cuda:0 均空闲

---
