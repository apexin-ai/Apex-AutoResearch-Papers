# code proofwriter prompt

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_proofwriter-prompt_20260515T110657_result.json`
- **Structured JSON:** [`0a755f41f705285bd107.json`](../../sessions/0a/0a755f41f705285bd107.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tests pass. Here's the summary:

### 1. 逻辑域 Prompt 内容摘要

`LOGIC_EXTRACTION_PROMPT`（3229 chars）包含：
- 变量命名规范：一元属性 `property_entity`，二元关系 `relation_subject_object`
- 三种约束类型：`fact`（事实）、`rule`（规则/蕴含）、`derived`（推导结论）
- Z3 运算符：`Implies(a, b)`、`And(a, b, ...)`、`Or(a, b, ...)`、`Not(a)`、`== True/False`
- 3 个 few-shot 示例：简单推理（kind→nice）、二元关系（eats→red）、多条件规则（And+Implies）+ Unknown 答案

### 2. z3_maxsat.py 布尔/FOL 支持改动

- `parse_z3_formula` 新增 `var_type` 参数（默认 `"auto"`）
- 自动检测布尔公式：正则匹配 `Implies(`、`== True`、`== False`、`Not(`、`And(`、`Or(`
- 布尔模式下变量声明为 `z3.Bool`，算术模式保持 `z3.Real`
- 命名空间增加 `Bool`、`Real` 构造函数支持显式声明
- 验证：`kind_anne == True` + `Implies(kind_anne, nice_anne)` + `Not(nice_anne == True)` → **unsat** ✓

### 3. Domain 自动选择实现

- **pipeline.py** `run_single()`：`domain = "logic" if problem.get("dataset") == "proofwriter" else "math"`，自动设置 `self.constraint_extractor.domain`
- **pipeline.py**：逻辑域使用 `_group_logic_answers()`（大小写不敏感精确匹配），数学域保持 `group_equivalent_answers()`
- **run_mvp.py**：`_check_answer()` 函数根据 `dataset` 选择比较方式（ProofWriter 用字符串比较，数学题用 `is_equiv`）

### 4. 验证结果

| 测试 | 结果 |
|------|------|
| Z3 布尔解析（Fact/Rule/Derived/And/Or/Not） | ✓ |
| Z3 一致性检查（kind+Implies+¬nice → unsat） | ✓ |
| 数学公式自动识别（x+y==14 → Real） | ✓ |
| 逻辑域 Prompt 加载（含 Implies/fact/rule/derived） | ✓ |
| MockLLM 逻辑域 mock 提取 3 条约束 | ✓ |
| 数学域 MockLLM 仍正常工作 | ✓ |
| Pipeline domain 自动检测 | ✓ |

---
