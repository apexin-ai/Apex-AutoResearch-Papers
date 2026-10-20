# analysis metrics aggregation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_metrics-aggregation_20260515T041903_result.json`
- **Structured JSON:** [`a7c8a5737b2f672ef34c.json`](../../sessions/a7/a7c8a5737b2f672ef34c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。

**文件位置：**
- Markdown: `artifacts/_project/report/metrics_table.md` (art_20260515_dd2f16)
- CSV: `artifacts/_project/data/metrics_table.csv` (art_20260515_6b454d)

**覆盖 12 个实验**（10 个主实验 + 2 个诊断），核心发现：

| 对比组 | nve 范围 | 结论 |
|--------|---------|------|
| 008d (dt_emb=32, sub ON, dt=2) | **1.71-2.09x** | 病态 → 崩溃 (C1/C3) |
| 008f (dt_emb=0, sub ON, dt=2) | 0.30-0.83x | 无病态但性能差 (C1/C3) |
| 008e_v3 (dt_emb=32, sub ON, dt=1) | 0.72-0.94x | 正常 + 性能保持 (**C6 crown jewel**) |
| 008a (dt_emb=32, sub OFF, dt=2) | 0.59-0.71x | value suppression (C2) |
| 009b/009c (seed 2 验证) | 符合 seed 1 模式 | 多 seed 一致性确认 |

---
