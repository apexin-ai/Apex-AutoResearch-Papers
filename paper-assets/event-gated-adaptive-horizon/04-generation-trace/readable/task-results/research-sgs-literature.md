# research sgs literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sgs_literature_20260515T221833_result.json`
- **Structured JSON:** [`f8190d5a464c7c4f929c.json`](../../sessions/f8/f8190d5a464c7c4f929c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研已完成，写入 `artifacts/literature_sgs_survey.md`。

**核心发现**：

**方向1 — Stop-Gradient in MBRL**：所有主流MBRL方法（DreamerV3, TD-MPC2, MuZero, EfficientZero）的reward head都**没有**使用stop-gradient。sg仅用于consistency targets防collapse和value bootstrapping。DreamerV2有一个ablation发现停掉所有reward梯度可以改善某些任务，但这是粗暴的on/off，不是针对性的intervention。

**方向2 — Value Overestimation**：没有论文从gradient pathway角度分析MBRL中的value overestimation。MAAC (ICLR 2020)分析了梯度通过模型的instability，但关注explosion而非systematic positive bias。我们的CIVO机制（reward→dt_emb→critic）是一个全新的因果路径。

**方向3 — Temporal Embedding**：TAWM (ICML 2025)最相关——它condition world model on variable dt，但用numerical input + log scaling，不用learned embedding，且报告了"linear dt integration导致convergence failure"。没有prior work在Dreamer RSSM上加learned dt embedding，更没有人发现过reward梯度co-opt dt_emb的failure mode。

**方向4 — Gradient Surgery**：HarmonyDream (ICML 2024)最接近——处理world model中observation vs reward的梯度不平衡，但用loss-scale balancing，不是direction-aware surgery。PCGrad/CAGrad等从未被用于world model multi-head training。

**Novelty结论**：SGS在四个维度上都与现有工作有明确差异化——targeted sg on specific input to specific head，motivated by a diagnosed causal pathway (CIVO via dt_emb corruption)。这不是DreamerV2的blunt sg、不是HarmonyDream的loss reweighting、不是PCGrad的generic surgery。

---
