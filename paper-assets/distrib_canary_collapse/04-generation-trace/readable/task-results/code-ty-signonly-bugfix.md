# code ty signonly bugfix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ty_signonly_bugfix_20260520T060407_result.json`
- **Structured JSON:** [`36e1cf3d9a2195e8b8b0.json`](../../sessions/36/36e1cf3d9a2195e8b8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇总：

**Bug**: `run_5method_analysis_d102.py:223` 调用 `test_causality(signonly=False)` — `signonly` 不是 statsmodels 0.14.6 的合法参数，导致所有 TY 检验异常，静默返回 0/8。

**Fix**: 移除 `signonly`，改用 `kind="f"`；结果提取从 `summary().data` 改为直接访问 `test_result.test_statistic` / `test_result.pvalue`。

**验证结果**:

| 实验 | α | TY 修复前 | TY 修复后 | K≥3 变化 |
|------|---|----------|----------|---------|
| a050_s42 | 0.50 | 0/8 | **3/8** | 5→**6**/8 |
| a075_s42 | 0.75 | 0/8 | **3/8** | 6/8 不变 |
| pythia410m | 1.0 | 0/8 | **4/8** | 6/8 不变 |

**19828 不受影响** — 它使用手动 OLS+Wald 实现，不调用 `test_causality()`。

**附带发现**: 表格打印有列对齐 bug（TY_F 列误显示 PermFDR 值），JSON 数据正确。

---
