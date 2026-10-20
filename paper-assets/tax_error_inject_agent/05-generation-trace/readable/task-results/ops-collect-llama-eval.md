# ops collect llama eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-llama-eval_20260516T091303_result.json`
- **Structured JSON:** [`f0651afbed771db537bc.json`](../../sessions/f0/f0651afbed771db537bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LLaMA s42 Eval 结果

| Metric | TaxEI s42 | Random s42 |
|--------|-----------|------------|
| **Recovery Rate** | **0.745** | **0.766** |
| **Detection Rate** | **0.298** | **0.298** |
| Total Episodes | 47 | 47 |

### By Operator

| Operator | TaxEI Recovery | TaxEI Detection | Random Recovery | Random Detection |
|----------|---------------|-----------------|-----------------|------------------|
| C1_context_truncation | 0.833 | 0.167 | 0.667 | 0.417 |
| C4_observation_masking | 0.727 | 0.364 | 0.727 | 0.364 |
| P1_step_order_swap | 0.583 | 0.250 | **0.917** | 0.333 |
| P2_sub_goal_deletion | 0.833 | **0.417** | 0.750 | 0.083 |

### By Task Type

| Task Type | TaxEI Rate | Random Rate |
|-----------|-----------|-------------|
| look_at_obj_in_light | 0.833 | 0.833 |
| pick_and_place_simple | 0.625 | 0.750 |
| pick_clean_then_place | 0.636 | 0.636 |
| pick_cool_then_place | 0.714 | 0.571 |
| pick_heat_then_place | 0.875 | **1.000** |
| pick_two_obj_and_place | 0.857 | 0.857 |

### GPU 状态

- **GPU 0-2**: 空闲（0% utilization, 0 MiB），可用于下一步 LLaMA s0 训练
- **GPU 3**: 占用中（99%, 28751 MiB）

整体来看 Random s42 的 recovery rate 略高于 TaxEI（0.766 vs 0.745），detection rate 相同（0.298）。TaxEI 在 C1 和 P2 上 recovery 更强，Random 在 P1 上 recovery 显著更高（0.917 vs 0.583）。

---
