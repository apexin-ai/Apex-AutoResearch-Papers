# eval qwen recovery random s123

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen-recovery-random-s123_20260516T115632_result.json`
- **Structured JSON:** [`9f4c661be0cf5a664c7f.json`](../../sessions/9f/9f4c661be0cf5a664c7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成，registry 已更新。

## 结果

| 指标 | Random s123 | Random s0 |
|------|------------|-----------|
| **recovery_rate** | **66.0%** | 55.3% |
| **detection_rate** | 0.0% | — |

### 按 operator 分解

| Operator | Recovery Rate |
|----------|--------------|
| C1_context_truncation | 75.0% (9/12) |
| P2_sub_goal_deletion | 75.0% (9/12) |
| P1_step_order_swap | 58.3% (7/12) |
| C4_observation_masking | 54.5% (6/11) |

Random s123 (66.0%) 比 Random s0 (55.3%) 高 ~10.7pp，显示 seed 间存在一定方差。Detection rate 为 0，符合 Random baseline 预期（无针对性的错误检测训练）。

---
