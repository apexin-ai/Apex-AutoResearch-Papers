# analysis eval obs only object norm03 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-obs-only-object-norm03-seed44_20260516T193637_result.json`
- **Structured JSON:** [`b09675753767de1f09a4.json`](../../sessions/b0/b09675753767de1f09a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 结果汇总

**Overall SR: 18% (18/100)**

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 10% |
| salad_dressing | 20% |
| bbq_sauce | 40% |
| ketchup | 10% |
| tomato_sauce | 10% |
| butter | 10% |
| milk | 20% |
| chocolate_pudding | 30% |
| orange_juice | 30% |

## 跨 seed 对比 (norm=0.3, obs_only)

| seed | SR |
|------|-----|
| 42 | 19% |
| 44 | 18% |

**差异仅 1 个百分点**，确认 magnitude curve 在 norm=0.3 处跨 seed 高度一致。

结合 seed=44 norm=0.2 的 16%，seed=44 的 magnitude curve 趋势与 seed=42 基本一致（都是 norm=0.2~0.3 区间达到峰值附近），支持 obs_only 方法在该 norm range 内的稳定性结论。

---
