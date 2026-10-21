# analyze eval supp k2mean object s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-k2mean-object-s42_20260523T100431_result.json`
- **Structured JSON:** [`293483d4f72804ffcb75.json`](../../sessions/29/293483d4f72804ffcb75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。结果如下：

## Overall

**Success Rate: 79.5% (159/200)** — mode: vla_only, K=2, baseline_mode=mean

## Per-Task Results

| Task | SR | Successes/Rollouts |
|------|----|--------------------|
| alphabet_soup | 75.0% | 15/20 |
| cream_cheese | 70.0% | 14/20 |
| salad_dressing | 85.0% | 17/20 |
| bbq_sauce | 90.0% | 18/20 |
| ketchup | 95.0% | 19/20 |
| tomato_sauce | 85.0% | 17/20 |
| butter | 60.0% | 12/20 |
| milk | 70.0% | 14/20 |
| chocolate_pudding | 70.0% | 14/20 |
| orange_juice | 95.0% | 19/20 |

## 对比

| Method | Object s42 |
|--------|-----------|
| VLA-only | 79.0% |
| K=2 mean (本实验) | **79.5%** |
| CRM | 77.0% |
| Reconvla | 79.0% |

K=2 mean baseline 略高于 VLA-only 0.5pp，基本持平。JSON 结果已保存到 `logs/eval_object_vla_only_seed42.json`。

---
