# analysis r3 t20 predictions fdr fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r3_t20_predictions_fdr_fix_20260520T163325_result.json`
- **Structured JSON:** [`83a1ebb1913fd4d4291a.json`](../../sessions/83/83a1ebb1913fd4d4291a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`t20_predictions_locked_v2.json` 已生成，α=0.60 修正摘要：

| 字段 | v1 (pre-FDR) | v2 (FDR-corrected) |
|------|-------------|-------------------|
| t10_rate_used | 0.375 | 0.0 |
| z_t10 | -0.3186 | -1.5341 |
| z_t20 | -0.4506 | -2.1696 |
| predicted_rate | 0.3261 | 0.0150 |
| predicted_permg_count | 3 | 0 |

其他 α 值（0.45/0.50/0.75/1.00）均基于 sigmoid fit，不受 FDR 修正影响，未变动。`t10_data.permg_counts[9]` 也从 3 → 0 同步修正。

---
