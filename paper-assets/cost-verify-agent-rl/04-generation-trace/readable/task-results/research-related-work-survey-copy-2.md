# research related work survey

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_survey_20260515T161717_result.json`
- **Structured JSON:** [`ec6113a8833bb7d45e9b.json`](../../sessions/ec/ec6113a8833bb7d45e9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。汇总：

**线 1: Self-verification / Self-correction** — 7 篇论文
- 最强竞争：**Self-Guide** (2604.03098) — 直接对标，B-IAVR 的基础框架
- 最大 gap：现有工作全部是 always-on verification 或 test-time heuristic，**无人用 RL 训练 selective verification policy**

**线 2: RL for Interactive Agents** — 7 篇论文
- 最强参考：**GiGPO** (NeurIPS 2025) 和 **SPEAR** (ICLR 2026) — ALFWorld/WebShop 上最新 SOTA
- 最大 gap：credit assignment / exploration / dense reward 被充分研究，但 **verification as learnable agent action** 未被探索

**线 3: Cost-aware / Selective Computation** — 7+1 篇论文（Self-Verification Dilemma 跨线）
- 最强竞争：**Thinkless** (NeurIPS 2025) — 方法论最相近（RL-trained "when to X" via control tokens + DeGRPO）
- 最大 gap："when to compute more" 思想未被应用到 **interactive agent verification**

**B-IAVR 的核心 novelty 定位**：位于三条线交汇处 — 首个在 interactive agent 场景中用 RL 训练 selective verification policy，以 action change 作为 verification informativeness 的 reward signal。

---
