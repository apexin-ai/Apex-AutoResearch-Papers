# analyze eval supp obj adapt tau025 s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-obj-adapt-tau025-s42_20260523T100543_result.json`
- **Structured JSON:** [`d662e52afb6bf132f865.json`](../../sessions/d6/d662e52afb6bf132f865.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Object Adaptive CRM (τ=0.25, seed=42) 结果

**Overall: 81.0% (162/200)**

### Per-task

| Task | Rate | Succ/Total |
|------|------|------------|
| alphabet_soup | 80% | 16/20 |
| cream_cheese | 80% | 16/20 |
| salad_dressing | **90%** | 18/20 |
| bbq_sauce | **90%** | 18/20 |
| ketchup | 85% | 17/20 |
| tomato_sauce | 80% | 16/20 |
| butter | **65%** | 13/20 |
| milk | 75% | 15/20 |
| chocolate_pudding | 75% | 15/20 |
| orange_juice | **90%** | 18/20 |

### Adaptive Stats

- **trigger_rate**: 3.55% (1236/34838 steps)
- **mean_uncertainty**: 0.1090
- **τ**: 0.25
- **max_correction_norm**: 0.2

### 对比

| Method | Object SR |
|--------|-----------|
| VLA-only | 79% |
| CRM (always-on) | 77% |
| ReConVLA | 79% |
| **Adaptive CRM τ=0.25** | **81%** |

τ=0.25 比之前错误的 τ=0.074855 (77.5%) 高 3.5pp，超过所有 baseline。trigger rate 从之前的高频触发降到 3.55%，说明只在高不确定性时介入，效果更好。

---
