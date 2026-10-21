# review reference audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_reference-audit_20260514T214406_result.json`
- **Structured JSON:** [`59a79e28e1a2f72f4dcb.json`](../../sessions/59/59a79e28e1a2f72f4dcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成，报告写入 `artifacts/reference_audit_report.md`。

**核心结论**：
- **0 条虚假引用**——所有 33 条都指向真实可查的文献，9 条 2025-2026 高风险 arXiv ID 全部验证为真。
- **4 条需要修正元信息**（按严重程度）：
  1. `rlsf` (arXiv:2405.16661)：标题和作者**全错**。应为 "RLSF: Fine-tuning LLMs via Symbolic Feedback"，作者是 Piyush Jha 等（不是 Abhinav Jha / Shikhar Murty / Zico Kolter）。
  2. `kwa-catastrophic-goodhart`：前两位作者名字错。应为 **Thomas Kwa**（不是 Tat-Thang Kwa）和 **Drake Thomas**（不是 Rachel Thomas）。
  3. `spurious-rewards` (arXiv:2506.10947)：第一作者错。应为 **Rulin Shao**（不是 Ruixin Yang）。
  4. `rubric-grpo`：标题轻微差异（"Reinforcement Learning" vs "RL"），非阻塞。
- **引用图干净**：33 条 cite key 与 33 条 bib 条目完全匹配，无缺失也无未使用。

---
