# code phase1 e2e test

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1_e2e_test_20260513T205838_result.json`
- **Structured JSON:** [`53052930c81244b788dc.json`](../../sessions/53/53052930c81244b788dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12/12 通过，3.49s。

产出：
- `compiler/tests/__init__.py` — 空 init
- `compiler/tests/test_e2e.py` — 12 个 e2e 测试，覆盖：
  - `test_entity_type_masking` — entity type 位置全类型放行
  - `test_head_type_constraint` — head_type 位置按 relation 约束 mask
  - `test_tail_type_constraint` — tail_type 位置按 (relation, head) 约束 mask，验证至少 1 个类型被 mask
  - `test_entity_registry_tracking` — 生成实体后 registry 记录 text→type
  - `test_semantic_mask_nonempty_for_all_relations` — 所有 (relation, head_type) 组合至少有 1 个合法 tail
  - `test_semantic_mask_intersection_with_grammar` — 语义 mask 只修改 type first tokens，不影响其他 vocab
  - `test_full_triple_generation` — 完整 triple 三阶段（relation_type→head_type→tail_type）
  - `test_prompt_offset` — prompt_length 正确隔离 prompt 与生成文本
  - `test_free_text_no_masking` — 自由文本位置无 mask
  - `test_multiple_relations_independent_state` — 多 relation 独立约束
  - `test_first_token_ids_match_tokenizer` / `test_first_token_uniqueness` — tokenizer 对齐验证

---
