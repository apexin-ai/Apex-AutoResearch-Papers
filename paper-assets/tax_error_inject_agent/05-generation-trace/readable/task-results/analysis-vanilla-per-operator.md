# analysis vanilla per operator

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vanilla-per-operator_20260515T032830_result.json`
- **Structured JSON:** [`e968e26c85825afeae6e.json`](../../sessions/e9/e968e26c85825afeae6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated, artifact registered.

**结果总结：**

Vanilla per-operator recovery (seed=42):
- C1: 75.0% (9/12) — 最高，context truncation 容忍度好
- C4: 54.5% (6/11)
- P1: 58.3% (7/12)
- P2: 58.3% (7/12)

**Fig 2 delta 验证：4 个中 3 个有误。** 只有 P2 (-8.3 vs claimed -8.4) 基本正确。C4 实际 +9.1 (claimed +6.1)，C1 实际 -8.3 (claimed -5.6)，P1 实际 0.0 (claimed -2.7)。方向大致对（C4 唯一正 delta），但数值和 P1 方向需要修正。

---
