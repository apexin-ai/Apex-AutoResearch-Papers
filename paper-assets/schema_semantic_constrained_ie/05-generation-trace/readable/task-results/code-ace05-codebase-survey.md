# code ace05 codebase survey

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ace05_codebase_survey_20260517T141448_result.json`
- **Structured JSON:** [`aa03199859208b71e87f.json`](../../sessions/aa/aa03199859208b71e87f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。报告已注册为 `art_20260517_da95d0`。

**核心发现**：

1. **架构清晰，扩展性好**：Grammar Layer (XGrammar CFG) 和 Semantic Layer (TypeConstraintProcessor) 分离设计，可以独立扩展

2. **最大改动在 Semantic Layer** (`type_mask_processor.py`)：需要新增 3 个 FieldPosition（EVENT_TYPE, ARGUMENT_ROLE, ARGUMENT_ENTITY_TYPE）和 3 个对应的 mask 函数，以及 PositionDetector 的 regex 扩展

3. **Grammar Layer 改动适中**：新增 `EventConstraint` dataclass 和 event JSON Schema 构建函数，XGrammar 编译流程完全复用

4. **高复用率**：EntityRegistry、first-token masking、XGrammar 编译、beam search 适配、推理框架（resume/batch/timing）均可直接复用

5. **Violation 类别映射**：RE 的 4 类 violation (ET/RV/DR/CF) 映射为 EE 的 5 类 (ET/EV/RoV/AC/CF)，新增 Role Vocabulary 检查

6. **预估 ~18h，4 天完成**：Phase 1 ontology+grammar → Phase 2 semantic mask → Phase 3 推理流程 → Phase 4 评估

---
