# analyze eval mlp adapter seed44

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_mlp_adapter_seed44_20260519T143455_result.json`
- **Structured JSON:** [`5e0b11a9ff1c1f675dd6.json`](../../sessions/5e/5e0b11a9ff1c1f675dd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

## eval_mlp_adapter_seed44 结果

| 指标 | 值 |
|---|---|
| Overall SR | **60.4%** |
| Wilson CI 95% | [56.1%, 64.6%] |
| Total | 302/500 |

**Per-task SR:**

| Task | SR |
|---|---|
| 0 alphabet_soup | 54% |
| 1 cream_cheese | 68% |
| 2 salad_dressing | 58% |
| 3 bbq_sauce | 50% |
| 4 ketchup | 80% |
| 5 tomato_sauce | 58% |
| 6 butter | 82% |
| 7 milk | 58% |
| 8 chocolate_pudding | 54% |
| 9 orange_juice | 42% |

## 3-seed 汇总 (MLP Adapter Control)

| Seed | SR |
|---|---|
| 42 | 65.2% |
| 43 | 64.6% |
| 44 | 60.4% |
| **Mean ± Std** | **63.4 ± 2.6%** |

Conclusion: **negative** — MLP adapter 3-seed mean 63.4±2.6% 与 cross-attention compressor 3-seed 61.2±1.4% 性能相当（差异在标准差范围内），不支持 re-encoding 优于 capacity matching 的 claim。

---
