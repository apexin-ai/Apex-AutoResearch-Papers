# harvest pi05 vla only baseline all6

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_pi05-vla-only-baseline-all6_20260521T122006_result.json`
- **Structured JSON:** [`6b6e37711249346ea504.json`](../../sessions/6b/6b6e37711249346ea504.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已存在且数据完整准确，无需更新。汇总：

| Benchmark | Mean SR | Std |
|---|---|---|
| **Object** (seed 42/43/44) | **81.50%** | ±0.50 |
| **Spatial** (seed 42/43/45) | **84.17%** | ±1.04 |

跨 seed 方差很低，结果稳定。瓶颈任务：Object `tomato_sauce` 56.7%、`salad_dressing` 65.0%；Spatial `on_ramekin` 25.0%、`top_drawer` 68.3%。无 W&B run ID，无错误/异常。报告已在 `artifacts/pi05_baseline_harvest.md`。

---
