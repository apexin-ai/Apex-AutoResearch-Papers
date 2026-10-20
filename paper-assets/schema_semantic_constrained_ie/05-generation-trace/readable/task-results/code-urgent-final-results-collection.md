# code urgent final results collection

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_final_results_collection_20260518T013943_result.json`
- **Structured JSON:** [`c81dfc38ba82968082dd.json`](../../sessions/c8/c81dfc38ba82968082dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16980 GPU 状态
- cuda:0: **空闲** (0%, 0 MiB)
- cuda:1: **运行中** (79%, 39809/97887 MiB) — Llama 16K retry

## Qwen Constrained 最终结果 (retry 8192 后)
- 状态: **完成** (246/246)
- Parse Success: 206/246 (83.7%)
- Violation: ET=0.0%, EV=0.0%, RoV=0.3%, AC=2.1%, CF=21.1%
- F1: Trigger=0.1339, Argument=0.0168, Entity=0.1409

## Llama Constrained (16K retry)
- 状态: **运行中** (233/246)
- Parse Success (当前): 215/233 (92.3%)
- Violation/Eval: 待完成后运行

## westd-21461 GPU 状态
- cuda:0: **空闲** (0%, 0 MiB)
- cuda:1: **空闲** (0%, 0 MiB)

## Mistral v2 最终结果
- 状态: **完成** (246/246)
- Parse Success: 178/246 (72.4%)
- Violation: ET=0.0%, EV=0.0%, RoV=0.1%, AC=16.6%, CF=13.9%
- F1: Trigger=0.0508, Argument=0.0047, Entity=0.1245

## Grammar-only mode
`--mode` 可用值: `unconstrained`, `grammar_only`, `semantic_only`, `full_s1`, `full_s2`

`grammar_only` = 只启用 grammar constraint（GBNF 结构约束），不含 semantic mask。其他相关 flag: `--type_consensus` 启用 Layer 3 全局类型一致性约束 (CF=0%)。

## 空闲 GPU
- westd-16980 cuda:0
- westd-21461 cuda:0
- westd-21461 cuda:1

---
