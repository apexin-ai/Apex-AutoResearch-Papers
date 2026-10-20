# ssh b7 adaptive sampling budget

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b7-adaptive-sampling-budget_20260520T090154_result.json`
- **Structured JSON:** [`44cb547e9e4383b7d2c0.json`](../../sessions/44/44cb547e9e4383b7d2c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

### FewNERD (Qwen3 8B, 37648 instances)

| Strategy | Micro F1 | Δ vs U8 | Samples | Savings |
|---|---|---|---|---|
| Greedy | 78.84 | +0.65 | 37648 | 87.5% |
| Uniform N=8 | 78.19 | — | 301184 | — |
| **Adaptive h1/l8** | **78.49** | **+0.30** | **169416** | **43.8%** |
| Adaptive h2/l8 | 76.00 | -2.19 | 188240 | 37.5% |
| Adaptive h4/l8 | 77.81 | -0.38 | 225888 | 25.0% |

**关键发现**：FewNERD 上 greedy 已优于 SC N=8（78.84 vs 78.19）。最优策略是 **adaptive_h1_l8**（高置信度用 greedy，低置信度用 N=8 SC），F1 比 uniform N=8 **提升 +0.30** 同时节省 43.8% 样本。N=2 majority vote 反而伤害高置信度组的精度。

### SciERC (Qwen3 8B, 551 instances)

| Strategy | Micro F1 | Δ vs U8 | Samples | Savings |
|---|---|---|---|---|
| Greedy | 65.92 | -1.20 | 551 | 87.5% |
| Uniform N=8 | 67.12 | — | 4408 | — |
| Adaptive h2/l8 | 66.99 | -0.13 | 2752 | 37.6% |
| **top67% h2/l8** | **67.07** | **-0.05** | **2194** | **50.2%** |
| top75% h2/l8 | 66.97 | -0.15 | 1930 | 56.2% |

**关键发现**：SciERC 上 adaptive 极为有效——top 67% 用 N=2 仅损失 0.05 F1 却省 50% 样本。SciERC 对 sample 数不敏感，即使 top 75% 只用 N=2 也仅损失 0.15。

### 推荐策略
- **FewNERD**: 用 adaptive_h1_l8（高置信度直接用 greedy，低置信度用 N=8 SC）—— 效果更好且省 44% 算力
- **SciERC**: 用 top67%_h2_l8 —— 仅 -0.05 F1 损失，省 50% 算力

---
