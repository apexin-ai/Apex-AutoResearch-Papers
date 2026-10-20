# analysis ic formula code audit

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ic_formula_code_audit_20260514T122154_result.json`
- **Structured JSON:** [`15b31aa92a375a4d8551.json`](../../sessions/15/15b31aa92a375a4d8551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部代码已审完。以下是三个问题的回答。

---

## Q1: IC 的具体计算公式

**代码位置**: `z3_checker.py:81-134`

**核心逻辑** (行 112-134):
```python
# 行 112: 分母选择
denom = total_claims if total_claims > 0 else len(formalized)

# 行 114-118: Z3 满足性检查
solver = z3.Solver()
solver.add(*exprs)          # 把所有 formalized claims 的 FOL 加入
result = solver.check()     # SAT check: ∃ model s.t. C1 ∧ C2 ∧ ... ∧ Cn ?

# 行 120-123: SAT 分支
if result == z3.sat:
    ic_score = len(formalized) / denom   # ← 关键行
    return (True, ic_score, len(formalized))

# 行 125-129: UNSAT 分支
if result == z3.unsat:
    mcs, mcs_size = self.greedy_mcs(formalized, vocab)
    ic_score = mcs_size / denom
    return (False, ic_score, mcs_size)
```

**调用方** (`scoring.py:71-78`):
```python
total = len(claims)                    # 所有 claims（含未 formalize 的）
formalized = [c for c in claims if c.z3_parseable and c.fol]
formalized_count = len(formalized)
ic_sat, ic_score, mcs_size = z3_checker.check_internal_consistency(
    claims, vocab, total_claims=total)  # ← total_claims = total
```

**公式**:
- **SAT 时**: `IC = formalized_claims / total_claims` = **formalization rate 本身**
- **UNSAT 时**: `IC = mcs_size / total_claims`
- **timeout 时**: 同 SAT

---

## Q2: Z3 solver 调用逻辑

**代码位置**: `z3_checker.py:114-118`

Z3 做的是 **满足性检查 (SAT check)**:
```
check(C1 ∧ C2 ∧ ... ∧ Cn)  →  是否存在一个模型使所有 claim 同时为真？
```

这 **不是** validity check（`check(¬(premises → conclusion))` UNSAT）。它只是问"这些 claim 有没有矛盾"。

**关键问题**: 对于 autoformalize 生成的 FOL，不同 claim 通常使用不同的谓词（`StepValid(x)` vs `ConclusionFollows(y)`），它们在语义上是独立的。独立命题的合取几乎总是 SAT——除非出现 `P(a) ∧ ¬P(a)` 这种显式矛盾，而 autoformalize 很难产生这种结构化矛盾。

**没有 PCV（Premise-Conditioned Verification）**。代码中 premises 完全没参与 Z3 验证——只是把 chain 自身的 formalized claims 扔进 solver，不引入任何来自题目的前提。

---

## Q3: formalization 失败的 claim 怎么处理

**代码位置**: `z3_checker.py:98-101, 112`

```python
formalized = [c for c in claims if c.z3_parseable and c.fol]  # 行 98

if not formalized:
    return (True, 0.0, 0)    # 行 100-101: 全部失败 → IC=0

denom = total_claims if total_claims > 0 else len(formalized)  # 行 112: 分母用 total
```

处理方式：
- 未 formalize 的 claim **不进分子**（不参与 Z3 检查）
- **计入分母**（`denom = total_claims`）
- 效果：formalization 失败越多，IC 越低

这意味着 IC 分数被 formalization rate 从上方严格限制：`IC ≤ formalization_rate`，且 SAT 时 `IC = formalization_rate`。

---

## 最终结论

**IC 已退化为 formalization rate 的代理指标。** 原因链条：

1. Z3 做的是 SAT check（`∃ model: C1 ∧ ... ∧ Cn`），不是 validity check
2. Autoformalized claims 几乎总是使用不同谓词，互相独立 → 合取几乎总是 SAT
3. SAT 时 `IC = formalized_claims / total_claims` = formalization rate
4. 没有引入 premises，Z3 不验证推理步骤是否从前提正确推导
5. 结果：IC 完全由"LLM 能否输出可解析的 FOL"决定，与推理链的逻辑正确性无关

**Cohen's d = -0.04 的根本原因**：正确链和错误链的 formalization rate 没有显著差异（LLM 对两者都能以相似的成功率生成 FOL），所以 IC 无法区分它们。这是 **实现 bug**，不是假设失败。

---
