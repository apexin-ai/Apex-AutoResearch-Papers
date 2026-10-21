# code check olmo1b 10k done

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_olmo1b_10k_done_20260522T223326_result.json`
- **Structured JSON:** [`269371681049214f64a0.json`](../../sessions/26/269371681049214f64a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已无活跃任务，无需清除。

---

**exp_olmo1b_10k 实验报告**

**状态：成功完成**

**关键 Metrics：**

| Pairwise AUC | 值 |
|---|---|
| 0v1 | **0.9871** |
| 1v2 | 0.4984 |
| 2v3 | 0.5059 |
| 3v4 | 0.5061 |
| 4v5 | 0.5074 |

- **K\* = 1**（仅 depth-0 vs depth-1 可区分，AUC 接近 1.0；更深层全部退化至随机水平 ~0.50）
- JSD 同样印证：0v1 = 0.230，其余均 < 0.002
- Ordinal 分类：MAE = 1.41, Accuracy = 31.5%
- Top 特征：freq_entropy, surp_d1_mean, freq_kurtosis

**已完成操作：**
- Registry 已更新为 DONE/success，metrics 已记录
- Cron 本 session 无活跃任务，无需删除

---
