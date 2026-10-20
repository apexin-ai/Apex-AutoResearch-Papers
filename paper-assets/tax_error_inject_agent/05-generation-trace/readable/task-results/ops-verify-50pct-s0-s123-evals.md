# ops verify 50pct s0 s123 evals

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-50pct-s0-s123-evals_20260516T013534_result.json`
- **Structured JSON:** [`44832ae2c9049867eaed.json`](../../sessions/44/44832ae2c9049867eaed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 50% inject eval 结果（valid_unseen, 47 episodes）

| 文件 | success_rate | successes | total |
|------|-------------|-----------|-------|
| **v4_taxei_fixed_inject50_s0** | **0.702** | 33 | 47 |
| **v4_taxei_fixed_inject50_s123** | **0.468** | 22 | 47 |
| v4_taxei_fixed_inject50 (无种子后缀) | 0.511 | — | 47 |
| **v4_random_fixed_inject50_s0** | **0.468** | 22 | 47 |
| **v4_random_fixed_inject50_s123** | **0.702** | 33 | 47 |
| v4_random_fixed_inject50 (无种子后缀) | 0.574 | — | 47 |

### s0/s123 按 task_type 明细

| task_type | taxei_s0 | taxei_s123 | random_s0 | random_s123 |
|-----------|----------|------------|-----------|-------------|
| look_at_obj_in_light (6) | 5/6 (0.833) | 4/6 (0.667) | 4/6 (0.667) | 6/6 (1.000) |
| pick_and_place_simple (8) | 4/8 (0.500) | 4/8 (0.500) | 3/8 (0.375) | 5/8 (0.625) |
| pick_clean_then_place (11) | 9/11 (0.818) | 4/11 (0.364) | 6/11 (0.545) | 8/11 (0.727) |
| pick_cool_then_place (7) | 4/7 (0.571) | 2/7 (0.286) | 1/7 (0.143) | 4/7 (0.571) |
| pick_heat_then_place (8) | 6/8 (0.750) | 5/8 (0.625) | 5/8 (0.625) | 6/8 (0.750) |
| pick_two_obj_and_place (7) | 5/7 (0.714) | 3/7 (0.429) | 3/7 (0.429) | 4/7 (0.571) |

值得注意：taxei_s0 和 random_s123 都是 0.702，taxei_s123 和 random_s0 都是 0.468——两组在不同种子下表现交叉对称，方差较大。

---
