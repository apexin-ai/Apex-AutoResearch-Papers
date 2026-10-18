# code data integrity fix

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-integrity-fix_20260523T112330_result.json`
- **Structured JSON:** [`fde880d38e16217d14fd.json`](../../sessions/fd/fde880d38e16217d14fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**3 个问题中，只有 1 个需要修复：**

| 问题 | 结论 | 操作 |
|------|------|------|
| AUC=0.86 | **正确**，来自 Δπ-only 诊断 (AUC=0.865)，非 exp-005 的 correlation。审计报告误判。 | 无修改 |
| AUC=0.82 | **不可追溯**。实际值 0.66（exp_asym_diag_v2: all-subgroup Sym AUC=0.6571） | 修改 3 处：theory.tex:58, limitations.tex:23, appendix.tex:170 |
| 74–82% coverage | **正确**，对应受影响子组覆盖率 (0.74, 0.78, 0.78, 0.82)。审计的 84.5% 是含未受影响子组的均值。 | 无修改 |

编译通过，0 errors，29 页。报告已注册至 `artifacts/data_integrity_fixes.md`。

---
