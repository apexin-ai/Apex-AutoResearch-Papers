# review data correctness audit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_data_correctness_audit_20260523T191757_result.json`
- **Structured JSON:** [`6139a345731ed77fa390.json`](../../sessions/61/6139a345731ed77fa390.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完成。结果：

**105项检查，102 PASS，2 FAIL（已修复），1 UNVERIFIED**

### 已修复（experiments.tex line 120）
1. **83.3% → 83.2%**：Qwen-72B item_id 源值 83.2482%，四舍五入应为 83.2%
2. **8.8pp → 8.7pp**：83.25−74.51=8.74pp，四舍五入应为 8.7pp

LaTeX 重新编译成功，PDF 已更新。

### 未验证
- §4.1 text-exact-match "temperature dominates at 79.7%" — 服务器上未找到对应的 259K text-exact-match 分析 JSON。风险低（辅助对比分析），但建议找到或重跑该分析确认。

完整报告：`artifacts/verification_report.md`

---
