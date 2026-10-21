# eval collect s0 40k 45k results

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_s0_40k_45k_results_20260521T013450_result.json`
- **Structured JSON:** [`189c338a2443cbb5b9b8.json`](../../sessions/18/189c338a2443cbb5b9b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已完成。**vanilla_s0 完整 learning curve：**

| Step | TSR | CAR | Collisions/200 |
|------|-----|-----|-----------------|
| 35K | 90.5% | 69.5% | 61 |
| **40K** | **95.0%** | **70.0%** | **60** |
| **45K** | **95.5%** | **74.5%** | **51** |
| 50K | 91.0% | 77.5% | 45 |

趋势：
- **TSR** 在 40K-45K 达到峰值 (95-95.5%)，50K 回落到 91%——可能出现轻微过拟合
- **CAR** 单调递增 69.5% → 70% → 74.5% → 77.5%，安全性持续改善
- **Collisions** 单调递减 61 → 60 → 51 → 45

TSR 最佳 checkpoint 是 45K（95.5% TSR + 74.5% CAR），综合最优可能也是 45K（TSR 高且 CAR 已较好）。50K 的 CAR/collisions 最优但 TSR 下降了 4.5 个百分点。

---
