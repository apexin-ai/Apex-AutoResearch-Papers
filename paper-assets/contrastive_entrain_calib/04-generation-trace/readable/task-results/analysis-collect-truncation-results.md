# analysis collect truncation results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect-truncation-results_20260522T151739_result.json`
- **Structured JSON:** [`993b524eb3e3966b97b6.json`](../../sessions/99/993b524eb3e3966b97b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成（耗时 278.8 秒）。结果文件已读取成功。

## Truncation AUROC 最终结果

### asst_first 位置（第一个 assistant token）

| 条件 | AUROC | Cosine Gap | Syc Mean | Valid Mean |
|------|-------|------------|----------|------------|
| Full response | **0.76** | 0.0035 | 0.024 | 0.0205 |
| Truncated 256 | **0.60** | 0.0044 | 0.0507 | 0.0463 |
| **AUROC diff** | **0.16** | | | |

### mean_position（全序列均值）

| 条件 | AUROC | Cosine Gap | Syc Mean | Valid Mean |
|------|-------|------------|----------|------------|
| Full response | **0.71** | 0.0025 | -0.0034 | -0.0059 |
| Truncated 256 | **0.62** | 0.0043 | 0.016 | 0.0117 |
| **AUROC diff** | **0.09** | | | |

### Response Length Stats
- Mean: 651.5 tokens, Median: 638, P25-P75: [524, 795]
- **100% 的 response 超过 256 tokens**（截断是有效的）

### 关键结论

1. **Full response d_syc 判别力显著优于 truncated**：asst_first 位置 AUROC 从 0.76 降到 0.60（Δ=0.16），mean_position 从 0.71 降到 0.62（Δ=0.09）
2. 截断后 cosine gap 反而略增（0.0035→0.0044），但 AUROC 下降——说明截断后 d_syc 的分布 overlap 增大，即 signal 变得更 noisy
3. 截断后两个 condition 的绝对 cosine 值都升高了（从 ~0.02 升到 ~0.05），可能因为前 256 tokens 的 hidden state 包含更集中的 sycophancy 信号，但缺乏后续 response 的区分性信息

---
