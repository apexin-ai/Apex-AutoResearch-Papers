# code fix c5 circular

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_c5_circular_20260514T143525_result.json`
- **Structured JSON:** [`1bc64b3248baeb556f6a.json`](../../sessions/1b/1bc64b3248baeb556f6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**C5 循环论证 bug 已修复**：
- **修改**：`evaluate_mvp.py` C5 的 `predicted` 从 `disagreement.error_side`（GT 派生）改为只使用 `stability.predicted_error_side`（ground-truth-free），跳过 `ambiguous` 样本
- **修正前**：C5 = 100.0% (35/35) — 数学恒等
- **修正后**：C5 = 80.0% (12/15) all / 88.9% (8/9) excl. Unknown — 仍然 PASS (≥60%)
- **MVP 总结**：5/5 PASS -> PROCEED（结论不变，但 C5 数值现在有意义了）

审计文档已写入 `artifacts/c1c5_audit.md`（本地 + 服务器）。

---
