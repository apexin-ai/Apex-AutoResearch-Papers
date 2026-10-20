# code svs local verify

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_svs_local_verify_20260514T051804_result.json`
- **Structured JSON:** [`046e02c52cd20117f4a2.json`](../../sessions/04/046e02c52cd20117f4a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | 所有模块可导入 | **PASS** |
| 2 | SVSResult 有 chain_verifications 字段 | **PASS** — fields: `chain_verifications, correct_sc, correct_svs, gold_label, group_scores, problem_id, sc_answer, selected_answer` |
| 3 | Config 默认值正确 | **PASS** — 50 problems × 8 chains, d>0.15, p<0.05, CI excludes 0=True |
| 4 | Z3 checker IC 修复 (Fix 2) | **PASS** — `total_claims` 参数存在 |
| 5 | scoring.py 返回 chain_verifications | **PASS** |
| 6 | run_mvp.py P2 逻辑用 chain-level IC | **PASS** — 按 gold answer 分组，包含 Mann-Whitney U + Wilcoxon signed-rank |
| 7 | CCLC trivially-SAT 诊断 (Fix 3) | **PASS** |
| 8 | 全部 17 个 .py 文件编译通过 | **PASS** — 0 FAIL |

**全部 8 项检查通过，代码完整性验证无问题。** 本地 venv 额外安装了 `openai`、`z3-solver`、`scipy`、`pyyaml` 作为运行时依赖。

---
