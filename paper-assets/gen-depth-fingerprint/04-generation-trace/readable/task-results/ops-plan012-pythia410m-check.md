# ops plan012 pythia410m check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan012-pythia410m-check_20260516T005024_result.json`
- **Structured JSON:** [`6d8fdccaf85b5d066961.json`](../../sessions/6d/6d8fdccaf85b5d066961.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 auto-resolve 时已被清理）。

**plan-012-pythia410m 实验结果汇总：**

| 指标 | QLoRA Pythia-410M | XGBoost baseline | Delta |
|------|------------------|-----------------|-------|
| 5-class macro F1 | 0.5564 ± 0.0158 | 0.5028 | **+0.0536** |
| 3-class macro F1 | 0.8703 ± 0.0220 | 0.7815 | **+0.0888** |

Per-class F1 (5-class): depth_0=0.991, depth_1=0.733, depth_2=0.347, depth_3=0.291, depth_4=0.420

Registry 已更新为 `DONE / success`，metrics 已写入。运行耗时 61.8 分钟。

---
