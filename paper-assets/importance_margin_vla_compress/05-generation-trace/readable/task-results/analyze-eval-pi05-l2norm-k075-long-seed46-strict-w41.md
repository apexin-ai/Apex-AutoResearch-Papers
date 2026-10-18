# analyze eval pi05 l2norm k075 long seed46 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k075_long_seed46_strict_w41_20260528T082147_result.json`
- **Structured JSON:** [`afc3755c5e342e8b8938.json`](../../sessions/af/afc3755c5e342e8b8938.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## 结果摘要

**π0.5 L2norm k=0.75 LIBERO-Long seed46: SR = 73.2%**

Per-task breakdown:

| Task | SR |
|------|-----|
| T0 alphabet soup & tomato | 88% |
| T1 cream cheese & butter | 86% |
| T2 stove & moka pot | 76% |
| T3 black bowl drawer | 86% |
| T4 white mug & plate | 70% |
| T5 book back shelf | 82% |
| T6 mug plate combo | 54% |
| T7 alphabet soup & cream | 74% |
| T8 both moka pots | 26% |
| T9 yellow mug microwave | 90% |

## 5-seed 汇总

| Seed | SR |
|------|------|
| 42 | 70.8% |
| 43 | 73.2% |
| 44 | 67.4% |
| 45 | 68.4% |
| 46 | **73.2%** |

**Mean = 70.6%, Std = 2.7pp**

seed46 与 seed43 并列最高（73.2%），range 收窄至 67.4–73.2（5.8pp）。第 5 seed 落在高端，没有进一步收窄 variance（std 从 4-seed 的 2.6pp 微升到 2.7pp），但 mean 稳定在 70.6%，置信区间良好。

---
