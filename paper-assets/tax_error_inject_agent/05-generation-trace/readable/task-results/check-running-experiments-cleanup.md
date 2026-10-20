# check running experiments cleanup

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running-experiments-cleanup_20260514T214111_result.json`
- **Structured JSON:** [`8f65578065cd6f81beae.json`](../../sessions/8f/8f65578065cd6f81beae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，Registry 已更新为 DONE。

## 汇总报告

| 实验 | 状态 | Recovery Rate | Detection Rate |
|------|------|--------------|----------------|
| **v4-random-recovery-eval** | completed | **0.638** (30/47) | 0.0 |
| **v4-taxei-recovery-eval-r2** | completed | **0.596** (28/47) | 0.0 |

### Per-operator 对比

| Operator | Random Recovery | TaxEI Recovery |
|----------|----------------|----------------|
| C1_context_truncation | 8/12 (0.667) | 8/12 (0.667) |
| C4_observation_masking | 6/11 (0.545) | 7/11 (0.636) |
| P1_step_order_swap | 9/12 (0.750) | 7/12 (0.583) |
| P2_sub_goal_deletion | 7/12 (0.583) | 6/12 (0.500) |

两个模型的 detection rate 均为 0，说明 think analysis 未能检测到注入的错误。Random SFT 的整体 recovery rate (0.638) 略高于 TaxEI SFT (0.596)，主要优势来自 P1 和 P2 算子。

---
