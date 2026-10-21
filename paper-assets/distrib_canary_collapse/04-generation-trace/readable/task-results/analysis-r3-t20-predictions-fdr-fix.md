# analysis r3 t20 predictions fdr fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r3_t20_predictions_fdr_fix_20260520T165339_result.json`
- **Structured JSON:** [`f601d693e5eedcf00caa.json`](../../sessions/f6/f601d693e5eedcf00caa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v2 已生成。变更摘要：

**`t20_a060` 修正**:
| 字段 | v1 | v2 |
|------|----|----|
| `predicted_permg_count` | 3 | 0 |
| `predicted_rate` | 0.3261 | 0.015 |
| `t10_rate_used` | 0.375 (3/8 pre-FDR) | 0.0625 (0/8 + continuity correction) |
| `t10_source` | actual (sync dip) | actual_fdr (sync dip) |
| `z_t10` | -0.3186 | -1.5341 |
| `z_t20` | -0.4506 | -2.1696 |
| `predicted_range` | [2, 3] | [0, 0] |

`t10_data.permg_counts[9]` (α=0.60) 也从 3 → 0。其余 4 个预测不变，sigmoid fit 参数不变。v1 原文件保留。

---
