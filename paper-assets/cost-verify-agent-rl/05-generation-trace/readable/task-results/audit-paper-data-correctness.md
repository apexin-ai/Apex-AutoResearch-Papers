# audit paper data correctness

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_data_correctness_20260523T191551_result.json`
- **Structured JSON:** [`929d6973f11cfeec7f91.json`](../../sessions/92/929d6973f11cfeec7f91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

自查完成。覆盖全部 60+ 数据点，修复了 2 处问题：

**已修复：**
1. **theoretical_analysis.tex**: p=5% K=8 的上界从错误的 "5.1%" 改为正确的 "14.9%"（精确值 14.86%）
2. **experiments.tex Table 1 caption**: 消除 "mean OOD=17.2%" 被错误归属于 11-seed 均值的歧义（17.2% 是 Cell D 2-seed 均值，11-seed 均值实际为 17.71%）

**8 处待确认疑点** 已详列于审计报告，严重程度均为低或极低，不影响论文结论。

审计报告写入 `artifacts/data_correctness_audit.md`。论文已重新编译，无错误。

---
