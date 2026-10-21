# review reference audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_reference-audit_20260515T042703_result.json`
- **Structured JSON:** [`27f705384be2f593ce5e.json`](../../sessions/27/27f705384be2f593ce5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存到 `artifacts/reference_audit_report.md`。

核心发现：

- **0 fake citations** — 28 条 bib 全部验真
- **2 条缺失引用需补**：ProofWriter（论文提到 legacy 文件名但未引）、Qwen3 Technical Report（基础模型未引）
- **9 条孤立 bib 条目**未被任何 .tex 引用，其中 `spurious-rewards`、`metr-reward-hacking`、`gao-effective-rl-reward` 三条与论文高度相关，建议补引
- **2 条 author 小错**：Math-Shepherd 的 "R.X. Xu" → "Runxin Xu"，Logic-LM 的 "William Wang" → "William Yang Wang"
- v1 发现的 `rlsf`、`kwa-catastrophic-goodhart` 等严重问题已在昨天修复

---
