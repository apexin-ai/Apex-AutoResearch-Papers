# data cliff curve csv

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_cliff_curve_csv_20260527T042929_result.json`
- **Structured JSON:** [`815db7451b13581e3d44.json`](../../sessions/81/815db7451b13581e3d44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已生成并注册。

**文件**: `artifacts/cliff_curve_data.csv`
**数据量**: 210 行（150 reliable, 60 unreliable）

覆盖范围:
- **OpenVLA**: Object/Goal/Long/Spatial × l2norm/attention/random, k=0.3-0.95 + baseline(k=1.0)
- **π0.5**: Object/Goal/Long/Spatial × l2norm/attention/random, k=0.1-0.95 + baseline(k=1.0)

注意:
- π0.5 Goal 和 Long baseline 来自 cqa1，标记 reliable=no（lenient condition）
- 所有 cqa1 上的 π0.5 非 strict 实验均标记 reliable=no
- π0.5 Long attention 全部数据为 cqa1 unreliable（无 westd strict 重跑）

---
