# check eval m32 official

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_m32_official_20260519T110812_result.json`
- **Structured JSON:** [`499000be569a7c48d44e.json`](../../sessions/49/499000be569a7c48d44e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果汇总：

**eval_smart_compress_m32_official — Overall SR: 53.4% (267/500)**
- 95% Wilson CI: [49.0%, 57.7%]
- Baseline (official SmolVLA): 59.2%
- **差距: -5.8 个点**

Per-task SR:

| Task | SR |
|---|---|
| T6 butter | **78%** |
| T8 chocolate pudding | 66% |
| T0 alphabet soup | 64% |
| T9 orange juice | 60% |
| T2 salad dressing | 56% |
| T1 cream cheese | 48% |
| T3 bbq sauce | 46% |
| T4 ketchup | 46% |
| T7 milk | 42% |
| T5 tomato sauce | **28%** |

假设验证：official checkpoint + Smart Compress M=32 得到 53.4%，低于 smolvla_base M=32 的 61.6%，也低于 official baseline 的 59.2%。Official pretrained features 在压缩场景下并未带来更好表现。

---
