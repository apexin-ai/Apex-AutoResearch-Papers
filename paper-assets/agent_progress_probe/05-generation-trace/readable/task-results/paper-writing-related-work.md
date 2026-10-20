# paper writing related work

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260514T220345_result.json`
- **Structured JSON:** [`48aef9d127de95d4768d.json`](../../sessions/48/48aef9d127de95d4768d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Related Work 已写入 `docs/paper/sections/related_work.tex` 并注册。

**结构**（4 subsections，~750 词）：

1. **LLM Agent Monitoring and Evaluation** — failure taxonomies (Cemri, Zhu), degradation benchmarks (SlopCodeBench), self-reflection 的局限性 (Reflexion/ToT/LATS + self-correction 负面证据), cycle detection, weak-to-strong monitoring。定位：我们问的是 *what signals*，不是提新 method。

2. **Process Reward Models for Agents** — AgentPRM, InversePRM, ToolPRMBench, PlanRewardBench, Agent-RRM, DataPRM 全覆盖。三点差异：window-level vs step-level、无需 outcome labels、monitoring vs training signal。

3. **Data Programming and Weak Supervision** — Snorkel 体系 (data programming → Snorkel → FlyingSquid → WRENCH) + sequential extensions (linked HMM, multi-resolution WS, HMM-Crowd/Dawid-Skene)。定位：novel domain (agent trajectories) + TLM negative finding。

4. **Anomaly Detection in Agent Trajectories** — TrajAD 对比。定位：stagnation 是 persistent regime (28.5% prevalence)，不是 rare anomaly；structural features 无需训练即达 0.995 F1。

所有引用均取自现有 `references.bib`，无编造条目。

---
