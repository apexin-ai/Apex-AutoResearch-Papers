# research paper literature prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-literature-prep_20260515T011405_result.json`
- **Structured JSON:** [`d19b0b315911d097e22e.json`](../../sessions/d1/d19b0b315911d097e22e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心结论：

**未被 scoop**。18 篇相关文献中，没有任何一篇诊断过 DreamerV3 的 trained dt_embedding 导致 delusional critic / value overestimation 的问题。

最相关的 3 篇竞品：
- **THICK** (ICLR 2024) — 加层级，不诊断 dt_embedding 病理
- **TAWM** (ICML 2025) — 变步长 world model，但基于 TD-MPC2，不涉及 RSSM
- **Chatterjee & Khardon** (NeurIPS 2025) — 变时长 action 加速 planning，不分析 critic 过估

"Delusional" 术语在 RL 中主要追溯到 Lu & Schuurmans (NeurIPS 2018)，指 function approximation 下 Q-backup 的 policy inconsistency。我们的用法是对该概念在 model-based imagination 中的新实例化——critic 利用 dt_embedding 到达不可达的时间状态——属于合理的术语扩展，需在论文中明确引用和区分。

---
