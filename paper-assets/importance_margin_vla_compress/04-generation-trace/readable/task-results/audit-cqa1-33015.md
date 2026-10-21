# audit cqa1 33015

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1-33015_20260522T015249_result.json`
- **Structured JSON:** [`906eb3f8ea1961486509.json`](../../sessions/90/906eb3f8ea1961486509.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。

**结论：cqa1-33015 (58.144.141.28:33015) 完全不可达。** 三个实验（提交于 ~25 小时前）状态无法确认：

| GPU | 实验 | Registry 状态 |
|-----|------|--------------|
| 0 | eval_pi05_random_k085_object_seed43_v2 | RUNNING |
| 2 | eval_pi05_random_k03_object_seed43_v2 | RUNNING |
| 3 | eval_pi05_l2norm_k07_object_seed43_v3 | PREPARING |

典型 pi05 eval 只需 1-3 小时，这些大概率已完成或已死。需要你去 AutoDL 控制台确认实例状态——如果端口变了请告诉我新端口，我可以重新巡检。

---
