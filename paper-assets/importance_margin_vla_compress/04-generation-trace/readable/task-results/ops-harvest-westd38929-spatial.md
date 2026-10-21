# ops harvest westd38929 spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_westd38929_spatial_20260522T122906_result.json`
- **Structured JSON:** [`d7abd8863307ffee2ef9.json`](../../sessions/d7/d7abd8863307ffee2ef9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

conclusion 只接受枚举值，已经是 `success`。3 个实验收割完成。

**汇总：**

| 实验 | SR | vs Baseline | 结论 |
|------|-----|-------------|------|
| **L2norm k=0.95 Spatial s42** | **97.8%** | 93.0% → +4.8pp | L2norm Spatial 完全免疫 cliff |
| **Random k=0.85 Spatial s42** | **58.4%** | 93.0% → -34.6pp | cliff 中但比 Object k=0.85 (5%) 浅很多 |
| **Random k=0.925 Object s43** | **30.0%** | 99.6% → -69.6pp | 与 s42=27.6% 一致，确认 cliff 入口 |

registry 已更新：hypothesis、metrics（含 per-task）均已规范化，状态 DONE。

---
