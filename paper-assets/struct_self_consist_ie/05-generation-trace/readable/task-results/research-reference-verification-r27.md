# research reference verification r27

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference_verification_r27_20260521T120017_result.json`
- **Structured JSON:** [`55bed6cba648e56c9f08.json`](../../sessions/55/55bed6cba648e56c9f08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，artifact 已注册（`art_20260521_002dd8`）。

**结果汇总：**

| # | Reviewer 引用 | 状态 | 正确引用 | Venue |
|---|-------------|------|---------|-------|
| 1 | DeNero et al. 2009 | ✅ | DeNero, Chiang & Knight | ACL-IJCNLP 2009 |
| 2 | Desai & Durrett 2020 | ✅ | Desai & Durrett | EMNLP 2020 |
| 3 | Huang et al. 2024 | ✅ | Huang et al. | ICLR 2024 |
| 4 | "Aronica et al. 2024" | ⚠️ 作者名错误 | **Li, Ramprasad & Zhang 2024** | Findings of EMNLP 2024 |

**关键发现**：第 4 篇 "Aronica et al. 2024" 是 Reviewer 2 的 AI 幻觉——实际论文是 Li et al. "A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction"（arXiv: 2402.13364），作者中无 Aronica。补引时需用正确作者。

---
