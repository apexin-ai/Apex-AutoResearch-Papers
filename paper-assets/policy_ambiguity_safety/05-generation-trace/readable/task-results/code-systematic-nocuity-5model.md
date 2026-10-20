# code systematic nocuity 5model

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_systematic_nocuity_5model_20260520T192833_result.json`
- **Structured JSON:** [`dba6011828e4f08a6752.json`](../../sessions/db/dba6011828e4f08a6752.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本执行完成，结果已输出到 `systematic_nocuity_5model.json`。

关键发现：
- **Ambiguous**: 124/300 (41.3%) clauses 有 majority+ convergent violation（≥3/5 模型）。其中 universal (5/5) 39 个，strong (4/5) 32 个，majority (3/5) 53 个。
- **Unambiguous control**: 仅 5/300 (1.7%) majority+ convergent violation，对照效果显著。
- **Ambiguity type 最高**: incompleteness (universal=12) 远超其他类型。
- **Severity agreement**: Fleiss' κ = 0.141 (slight)，模型在"是否违规"上趋同，但对违规严重程度的判定不一致。

---
