# harvest eval xvla l2norm k05 object seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_xvla_l2norm_k05_object_seed43_20260523T230742_result.json`
- **Structured JSON:** [`3bf8e7bbfeeec4d8a4f3.json`](../../sessions/3b/3bf8e7bbfeeec4d8a4f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

**eval_xvla_l2norm_k05_object_seed43** — DONE (negative)

| 指标 | 值 |
|------|-----|
| Overall SR | **43.0%** (215/500) |
| 95% Wilson CI | [38.7%, 47.4%] |
| 耗时 | 76.3 min |

**Per-task SR:**
| Task | SR |
|------|-----|
| T0 alphabet soup | 52% |
| T1 cream cheese | 6% |
| T2 salad dressing | 76% |
| T3 bbq sauce | 70% |
| T4 ketchup | 52% |
| T5 tomato sauce | 56% |
| T6 butter | 2% |
| T7 milk | 38% |
| T8 chocolate pudding | 16% |
| T9 orange juice | 62% |

**vs Random k=0.5 Object seed43:** L2norm 43.0% vs Random 71.0% → **-28pp**，L2norm 在 Object suite 上灾难性地差于 random。

**Seed42 对比:** 无 seed42 Object 数据可供 CV 对比。

**GPU 状态:** westd-38929 GPU 1 已空闲（1 MiB used, 0% util），可用于新任务。

---
