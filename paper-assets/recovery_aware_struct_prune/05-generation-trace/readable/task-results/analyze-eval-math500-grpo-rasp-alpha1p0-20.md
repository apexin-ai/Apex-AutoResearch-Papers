# analyze eval math500 grpo rasp alpha1p0 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_math500_grpo_rasp_alpha1p0_20_20260523T044344_result.json`
- **Structured JSON:** [`f1d4ddb202c7361ce257.json`](../../sessions/f1/f1d4ddb202c7361ce257.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## 汇总

| 指标 | 值 |
|------|-----|
| **accuracy** | **22.6%** (113/500) |
| **avg_response_length** | **903.5** |
| **stderr** | ±1.87% |
| **truncated** | 180/500 (36%) |
| **conclusion** | success |

### C1 decoupling 检验

- SFT α=1.0 MATH-500: 21.2%
- GRPO α=1.0 MATH-500: 22.6%
- **|Δ| = 1.4pp < 2pp** → C1 decoupling 在 MATH-500 上成立

---
