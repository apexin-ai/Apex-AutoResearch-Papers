# writing related work draft

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-draft_20260513T081949_result.json`
- **Structured JSON:** [`8ab1eaffdaf04c33b556.json`](../../sessions/8a/8ab1eaffdaf04c33b556.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/section_related_work_draft.md` 并注册。

**覆盖情况**：
- §2.1 引用 8 篇（yao2024taubench, liu2024agentbench, wang2024mint, naous2025flipping, sekulic2024daus, ahmad2025diversity, nakash2026divert, sim2real2026gap, seshadri2026lost）
- §2.2 引用 6 篇（zhao2021calibrate, abdulhai2025consistent, basil2025playing_pretend, hu2026expert_persona, li2025persona）— gap 指向 BCP 在 agent dialogue 中的 completion collapse
- §2.3 引用 5 篇（rafailov2023dpo, wang2024alignment, khan2026decoding, lee2024dpo_toxicity, gupta2026intra_fairness）— gap 指向 DPO+BCP 交互反转
- §2.4 引用 8 篇（rickford1999aave, kachru2008cultures, joshi2025dialect_survey, faisal2024dialectbench, lin2025redial, gupta2025endive, haq2026dialect, gallegos2024bias）— gap 指向无人测量 agent dialogue 中的行为率偏差

28 篇文献中引用 25 篇（未用：parrish2022bbq 低相关性，wang2024alignment 在 §2.3 已用作 survey reference，abdulhai 放在了 §2.2）。每节末尾均以 novelty gap 收尾。

---
