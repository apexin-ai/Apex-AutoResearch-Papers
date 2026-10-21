# audit ty granger canonical consistency

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ty_granger_canonical_consistency_20260520T180340_result.json`
- **Structured JSON:** [`116f60e468bdc79a3cb5.json`](../../sessions/11/116f60e468bdc79a3cb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告写入 `artifacts/ty_granger_canonical_audit.md`。

**核心发现：**

1. **Matmul bug：不存在。** Canonical 脚本使用 statsmodels 内置 `test_causality()`，无手写 Wald、无 `cov_params` 操作。

2. **新发现 Direction Reversal Bug：存在。** `test_causality(causing=1, caused=0)` 在 `data=[canary, downstream]` 下测试的是 downstream→canary（反向因果），但被标记为 forward。修复：改为 `causing=0, caused=1`。

3. **对论文影响：无。** TY 从未在任何实验中提供 consensus 的 swing vote。移除所有 TY 票后 robust pairs 计数不变（t20_a050: 6/8, t20_a100: 6/8, 14b: 8/8）。

4. **T=20 数据来源：确认均为 canonical 脚本生成**（字段格式 `f_stat`/`order`/`k_opt`/`d_max` 匹配）。

建议修复 direction bug 并重跑，但不阻塞论文提交。

---
