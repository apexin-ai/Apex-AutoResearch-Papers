# analysis long curve data collect

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_long_curve_data_collect_20260524T144020_result.json`
- **Structured JSON:** [`733ff3484a25268861e5.json`](../../sessions/73/733ff3484a25268861e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已整理完毕，保存在 `artifacts/_project/data/long_curve_data.md`。

**摘要：**

**Random Long** — 4/6 个 k 值有 postfix 数据，2 个 RUNNING：
| k | SR (%) | 版本 |
|---|--------|------|
| 0.95 | 63.2 | postfix ✅ |
| 0.90 | 31.8 | prefix ⚠️ postfix RUNNING |
| 0.85 | 45.2 | postfix ✅ |
| 0.70 | **65.8** | postfix ✅ (peak) |
| 0.50 | 46.8 | postfix ✅ |
| 0.30 | 29.0 | prefix ⚠️ postfix RUNNING |

**L2norm Long** — 2/6 个 k 值有 postfix 数据，3 个 RUNNING，k=0.3 无 postfix：
| k | SR (%) | 版本 |
|---|--------|------|
| 0.95 | **87.0** | postfix ✅ |
| 0.90 | 81.0 | prefix ⚠️ postfix_v2 RUNNING |
| 0.85 | 78.4 | postfix ✅ |
| 0.70 | 60.0 | prefix ⚠️ postfix RUNNING |
| 0.50 | 51.4 | prefix ⚠️ postfix RUNNING |
| 0.30 | 39.0 | prefix（无 postfix 计划）|

**Long 是所有 suite 中保留率最高的**：L2norm k=0.95 保留基线 95% 的性能（87.0/91.6）。Random 在 k=0.7 达到 peak (65.8%)，k=0.85–0.9 出现 U 型下降，与其他 suite 的 pattern 一致。

---
