# code r4 m3q3 semantic only et

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r4_m3q3_semantic_only_et_20260517T110021_result.json`
- **Structured JSON:** [`daa766d7d30a349cf304.json`](../../sessions/da/daa766d7d30a349cf304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。写入 `artifacts/r4_m3q3_semantic_et_analysis.md`。

核心发现：

1. **851 中的 355 个额外 ET 违规全部来自 relation 的 head_type/tail_type 字段**，entity list 的违规数量（496）与 unconstrained 完全一致。

2. **机制**：`_apply_type_mask` 只屏蔽 6 个 entity type 的 first token，剩余 ~150k vocab token 不受影响。在 full_s1 中 XGrammar 的 enum 约束保证输出只能是合法类型；semantic-only 没有 grammar 层，模型在被 D/R mask 屏蔽掉正确 type token 后会逃逸到 OOV 类型（如 "ORGB"=57, "OR"=48, "EVENT"=55）。

3. **SciERC 不受影响的原因**：SciERC 每个 entity type 在所有 7 个 relation 中都是合法的 head 和 tail（type-level blocking = 0%），D/R mask 从未真正屏蔽任何 token。DocRED 则相反：NUM 在 92% 的 relation 中被屏蔽，TIME 在 88% 中被屏蔽——高屏蔽率 + 无 grammar = 频繁 OOV 逃逸。

---
