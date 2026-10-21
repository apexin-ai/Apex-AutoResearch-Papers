# analyze eval pi05 random k07 long seed45 strict w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k07_long_seed45_strict_w38_20260528T074050_result.json`
- **Structured JSON:** [`4a054ca7797accfe6e36.json`](../../sessions/4a/4a054ca7797accfe6e36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**Overall SR: 61.6%** (308/500), keep=179/256 tokens (k=0.7 confirmed), EXIT_CODE=0

### Per-task SR

| Task | SR |
|------|----|
| T0 alphabet soup+tomato | 84% |
| T1 cream cheese+butter | 62% |
| T2 stove+moka pot | 68% |
| T3 black bowl→drawer | 80% |
| T4 white mug+plate | 74% |
| T5 book→back | 38% |
| T6 mug+plate combo | 62% |
| T7 alphabet soup+cream | 74% |
| T8 both moka pots | 4% |
| T9 yellow mug→microwave | 70% |

### 4-seed 对比 (Random k=0.7 Long)

| Seed | SR |
|------|----|
| seed42 | 64.4% |
| seed43 | 66.0% |
| seed44 | 63.4% |
| **seed45** | **61.6%** |
| **4-seed mean** | **63.85% ± 1.6** |

seed45 是四个 seed 中最低的，拉低了均值。4-seed mean 从 3-seed 的 ~64.6% 降至 63.85%，标准差从之前较窄的范围扩大到 ±1.6。

---
