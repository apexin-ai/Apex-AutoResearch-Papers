# diagnose westd27271 process gone

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd27271_process_gone_20260525T165943_result.json`
- **Structured JSON:** [`94e9d9c8c68e5260677e.json`](../../sessions/94/94e9d9c8c68e5260677e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新。汇总：

| exp_id | conclusion | overall_sr | baseline | 退化幅度 |
|--------|-----------|-----------|----------|---------|
| eval_openvla_random_k05_spatial_seed42 | success | **50.0%** (250/500) | 80.0% | -30.0pp |
| eval_openvla_random_k05_goal_seed42 | success | **52.2%** (261/500) | 74.8% | -22.6pp |

两个 Random k=0.5 实验均成功完成，50% 随机裁剪在两个 suite 上都造成了显著退化（Spatial -30pp, Goal -22.6pp），符合退化曲线中间点预期。

---
