# eval v4 random fixed inject10 eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v4-random-fixed-inject10-eval_20260515T013008_result.json`
- **Structured JSON:** [`9c2a863ecb286ed27531.json`](../../sessions/9c/9c2a863ecb286ed27531.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## v4-random-fixed-inject10 结果

### 训练
- train_loss: 0.4226, final_step_loss: 0.3079, token_acc: ~0.90
- 1635 steps, 3 epochs, 57 min

### Eval: **68.1% (32/47)**

| Task Type | Success | Rate |
|-----------|---------|------|
| look_at_obj_in_light | 5/6 | 83.3% |
| pick_heat_then_place | 7/8 | 87.5% |
| pick_two_obj_and_place | 5/7 | 71.4% |
| pick_and_place_simple | 5/8 | 62.5% |
| pick_cool_then_place | 4/7 | 57.1% |
| pick_clean_then_place | 6/11 | 54.5% |

### 对比分析

| Model | Success Rate |
|-------|-------------|
| **Random 10% (this)** | **68.1%** |
| TaxEI 10% | 61.7% |
| Vanilla (no inject) | 61.7% |

Random 10% injection **高出 TaxEI 10% 达 6.4pp**。这对 taxonomy-guided injection 的假设不利——在 10% 注入比例下，随机错误注入反而优于 taxonomy 标签引导的注入。可能的解释：随机注入提供了更多样化的错误分布，而 taxonomy 标签在低比例时可能过于集中在特定错误模式上。

---
