# research reference audit

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference-audit_20260513T063327_result.json`
- **Structured JSON:** [`160f534c8ed00048e6f5.json`](../../sessions/16/160f534c8ed00048e6f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。报告已写入 `artifacts/reference_audit_report.md`。

**结果：0 篇幻觉论文，8 篇均真实存在。**

需要修正的问题：

| 严重度 | 论文 | 问题 |
|--------|------|------|
| **必须修** | `gupta2026intra_fairness` (2602.16438) | 作者错误：实际首作者是 **Paraschou**，不是 Gupta。论文真实但作者张冠李戴 |
| 建议修 | `sim2real2026gap` (2603.11245) | 作者写了 "Anonymous" 但论文已有实名作者（Zhou, Sun 等，CMU） |
| 建议修 | `anonymous2026expert_persona` (2603.18507) | 作者写了 "Anonymous" 但实际是 Hu, Rostami, Thomason |
| 可选 | `basil2025playing_pretend` (2512.05858) | 标题省略了系列前缀 "Prompting Science Report 4:" |

---
