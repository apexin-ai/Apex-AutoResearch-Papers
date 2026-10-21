# analyze eval crm object k20 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-crm-object-k20-seed44_20260520T105005_result.json`
- **Structured JSON:** [`4b9447ba4075b0528e94.json`](../../sessions/4b/4b9447ba4075b0528e94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 分析摘要

**eval-crm-object-k20-seed44** — CRM obs_only, K=20, LIBERO-Object, seed=44

| 指标 | 值 |
|---|---|
| **Overall SR** | **18.0% (18/100)** |
| 总 rollouts | 100 (10 tasks × 10) |
| EXIT_CODE | 0, 无异常 |
| W&B run ID | 无 |
| 耗时 | ~2h (7329s), 2.04 GPU-hours |

**Per-task SR:**

| Task | SR |
|---|---|
| chocolate_pudding | 40% |
| salad_dressing | 30% |
| bbq_sauce | 30% |
| milk | 30% |
| orange_juice | 30% |
| tomato_sauce | 10% |
| butter | 10% |
| alphabet_soup | 0% |
| cream_cheese | 0% |
| ketchup | 0% |

**K=20 vs K=10 对比**: 本 seed 18.0%，K=10 均值 16.8%±1.8%。K=20 seed44 略高于 K=10 均值约 1.2pp，在 K=10 的 1σ 范围边缘。需要汇总 K=20 的全部 3 个 seed 才能做统计对比，但初步看 K=20 相对 K=10 提升有限，2x compute 换来的增益可能不显著。

---
