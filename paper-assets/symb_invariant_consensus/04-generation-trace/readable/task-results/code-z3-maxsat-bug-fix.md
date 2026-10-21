# code z3 maxsat bug fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_z3-maxsat-bug-fix_20260515T154902_result.json`
- **Structured JSON:** [`9d0ec1dcb79efbfb8fa8.json`](../../sessions/9d/9d0ec1dcb79efbfb8fa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地目录是项目管理目录，代码只在远程服务器上。修复已完成，总结如下：

## Bug 根因

`parse_z3_formula` 返回类型检查过宽：
```python
# 旧代码
if isinstance(result, (z3.ExprRef, z3.BoolRef)):
    return result
```
`ArithRef`（如 `x + y`、`x * 2`）是 `z3.ExprRef` 的子类，会通过检查。这些非布尔表达式传入 `z3.Implies(ind, ArithRef)` 时抛出 `Z3Exception: "Value cannot be converted into a Z3 Boolean value"`。

P2 的 LLM 约束提取产生了纯算术表达式（如变量名 `total`、算术 `n + m`），这些是 ArithRef 而非 BoolRef。

## 修复内容（3 处）

**1. `parse_z3_formula`**（源头过滤）：
```python
# 新代码：只接受布尔排序的表达式
if isinstance(result, z3.ExprRef) and z3.is_bool(result):
    return result
```

**2. `check_equivalence`**（防御性检查）：
```python
if not z3.is_bool(f1) or not z3.is_bool(f2):
    return False
```

**3. `MaxSATSolver.solve`**（安全网）：
- 增加 `active_mask` 跟踪哪些约束被实际加入优化器
- `Implies` 调用包裹 try/except
- 全部非布尔时直接返回空结果，不执行无意义的 `opt.check()`
- model 评估只检查 active 约束，非 active 直接归入 excluded

## 测试结果

35/35 通过，覆盖：
- 布尔表达式正常解析 ✓
- 非布尔表达式（ArithRef）被过滤 ✓
- 逻辑域公式（Implies/And/Or/Not）正常 ✓
- 边界情况（空串、None、纯常量）✓
- `check_equivalence` 排序安全 ✓
- P2 类混合约束不崩溃 ✓
- 全非布尔约束不崩溃 ✓
- P1/P3/P4 回归正常 ✓

## 重跑 P2

修复不需要重跑整个实验。如果 v2 实验仍在运行，修复已生效（代码已覆盖）。如果需要单独重跑 P2：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/symb_invariant_consensus
python run_full_mvp.py --mode vllm --k 12 --resume --output results/aime30_v2.json
```

`--resume` 会跳过已完成的题目，但 P2 由于 error 状态可能需要手动从 JSON 中删除 P2 条目后再 resume。

---
