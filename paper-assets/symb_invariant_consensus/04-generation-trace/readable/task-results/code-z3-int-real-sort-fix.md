# code z3 int real sort fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_z3-int-real-sort-fix_20260515T175527_result.json`
- **Structured JSON:** [`1b77b0d7ab1903e11a42.json`](../../sessions/1b/1b77b0d7ab1903e11a42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修改总结：**

**改了什么（`sica/z3_maxsat.py`）：**

1. **`parse_z3_formula()`** — 默认使用 `z3.Int()` 而非 `z3.Real()`。Int 解析失败时回退到 Real（处理 `1/2` 等分数常量场景）。
2. **`_try_eval()`** — uninterpreted functions（log, log2）的 sort 跟随 `use_int` 参数自适应，不再硬编码 RealSort。
3. **新增 `_collect_free_vars()` + `_unify_sorts_for_equiv()`** — 在 `check_equivalence()` 中，若两个公式的同名变量 sort 不同（Int vs Real），将 Real 变量替换为 `ToReal(Int(name))`，统一到同一变量空间后再比较。
4. **`check_equivalence()`** — 调用 sort 统一后再做等价性判定。

**Dedup 效果：**
- 修复前：`N % 7 == 0`（Int）和 `N >= 100`（Real）使用不同 N 变量，P7 的 4 个约束无法合并
- 修复后：两者都用 `z3.Int('N')`，4 个约束正确 dedup 为 2 个（各 weight=2）

**测试结果：**
- 原有 15 个测试：全部通过（无回归）
- 新增 10 个测试：全部通过（覆盖 sort 统一、cross-sort equivalence、P7 dedup 场景、Real fallback、Bool 不受影响）

---
