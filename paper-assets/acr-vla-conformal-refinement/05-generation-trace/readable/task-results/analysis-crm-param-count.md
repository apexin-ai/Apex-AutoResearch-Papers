# analysis crm param count

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crm-param-count_20260515T191317_result.json`
- **Structured JSON:** [`4541496d23ce77c7a342.json`](../../sessions/45/4541496d23ce77c7a342.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

| 变体 | 总参数量 | Keys | 输入维度 | 架构 |
|------|---------|------|---------|------|
| **obs_only** | **329,178** | 8 | 990 | 990→256→256→30 |
| **perdof** | **339,498** | 8 | 1,030 | 1030→256→256→30 |
| **scalar_unc** | **329,952** | 8 | 993 | 993→256→256→30 |

关键发现：
- 三个变体**架构相同**：3 层 MLP（input→256→256→30），都含 input_mean/input_std 归一化参数
- **参数量不同**，差异仅来自输入维度不同（obs_only=990, scalar_unc=993, perdof=1030），隐藏层和输出层完全一致（256→256→30）
- 参数量级都在 **~330K**，非常轻量

---
