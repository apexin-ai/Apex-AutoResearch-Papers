# code math equiv fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_math-equiv-fix_20260515T094849_result.json`
- **Structured JSON:** [`739f57f7e58bff270cdd.json`](../../sessions/73/739f57f7e58bff270cdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### 结果

1. **is_equiv 单元测试**：全部 7 个 assert 通过，分组测试正确（5 个答案归为 2 组）

2. **修改的文件**：
   - **`utils/math_equiv.py`**（新建）：`is_equiv()` + `group_equivalent_answers()`，优先用 math_verify，sympy fallback，最后数值 fallback
   - **`utils/__init__.py`**（新建）：空文件
   - **`run_mvp.py`**：import `is_equiv`，`sica_ok`/`sc_ok` 从 `==` 改为 `is_equiv()`
   - **`baselines/self_consistency.py`**：`Counter(valid)` 替换为 `group_equivalent_answers(valid)`
   - **`sica/pipeline.py`**：候选答案先做等价归组，trace answers 统一映射为 canonical form 后再送 scorer

3. **Mock 端到端**：通过，50 题正常跑完无报错

4. **math_verify**：已安装 v0.9.0（底层用 `latex2sympy2_extended`），作为主判定层

---
