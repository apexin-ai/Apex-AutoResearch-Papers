# ssh check exp017 status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_exp017_status_20260513T061553_result.json`
- **Structured JSON:** [`779558066a1f3c786bc8.json`](../../sessions/77/779558066a1f3c786bc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-017 已完成，状态：SUCCESS。** GPU 空闲，进程已退出，EXIT_CODE=0。

## 结果摘要

| 指标 | 值 |
|------|-----|
| **K\*** | **2** |
| AUC 0v1 | 0.9972 ± 0.0009 |
| AUC 1v2 | 0.6114 ± 0.0073 |
| AUC 2v3 | 0.5609 |
| AUC 3v4 | 0.5408 |
| AUC 4v5 | 0.5139 |
| JSD 0v1 | 0.2863 |
| JSD 1v2 | 0.0051 |
| Ordinal MAE | 1.1547 |
| Ordinal Acc | 0.3819 |
| Top features | freq_entropy, surp_mean, surp_std |
| 运行时间 | ~3.7 GPU-hours |

**关键发现**：Qwen continuation 模式下 K\*=2，depth 0→1 信号极强 (AUC=0.997)，1→2 仍可区分 (AUC=0.611>0.60)，之后迅速衰减至近随机。JSD 也呈同样模式——0v1 有数量级跳跃 (0.286)，之后均 <0.006。

Registry 已更新为 DONE/success，所有指标已入库。

---
