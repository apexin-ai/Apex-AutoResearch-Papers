# code r4 prompt sensitivity

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r4_prompt_sensitivity_20260517T122157_result.json`
- **Structured JSON:** [`9432ab6496bfeac63700.json`](../../sessions/94/9432ab6496bfeac63700.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并运行中：

- **GPU 0**: `minimal` unconstrained → `minimal` full_s1（串行）
- **GPU 1**: `detailed` unconstrained → `detailed` full_s1（串行）
- **基线**: 已有 `default` 的两组结果

3 个 prompt 变体设计：
1. **default** — 原始 prompt（有"expert"角色、标准格式描述）
2. **minimal** — 极简指令（无角色 framing、紧凑格式描述）
3. **detailed** — 详细指令（每个 entity/relation type 带定义和示例、额外规则说明）

预计 ~2.5h 后全部完成，之后运行 violation checker + F1 分析并汇总。

---
