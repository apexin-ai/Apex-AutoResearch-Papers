# research bernoulli st literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bernoulli_st_literature_20260514T004550_result.json`
- **Structured JSON:** [`d4d42f9bb4726deaae42.json`](../../sessions/d4/d4d42f9bb4726deaae42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。核心发现：

**新颖性**：在 RSSM imagination 中用 Bernoulli ST gate 做 binary skip/no-skip 尚无完全相同工作，但需与两个强竞争者仔细区分：
- **THICK** (ICLR 2024) — 同在 Dreamer 上做 adaptive temporal abstraction，但用隐状态变化检测（被动），不是显式 gate（主动）
- **MetaController** (DeepMind 2025) — switching gate β_t 功能等价于我们的 Bernoulli gate，且实验证明 gate 自发趋向 quasi-binary，但应用在 autoregressive model 上而非 RSSM

**Framing 建议**：定位为"第一个用显式 binary gate 在 RSSM imagination rollout 中做 event-driven adaptive horizon"，引用 MetaController 的发现（gate 趋向二值）作为直接用 Bernoulli ST 的理论支撑。

产出已注册：`literature_map.yaml`（17篇论文）+ `literature_survey_summary.md`（摘要）。

---
