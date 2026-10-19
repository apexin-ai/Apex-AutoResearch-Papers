# research phase b literature

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_phase-b-literature_20260514T043356_result.json`
- **Structured JSON:** [`3c81b5079aa56af03ff6.json`](../../sessions/3c/3c81b5079aa56af03ff6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研完成，已注册为 artifact `art_20260514_5cbffb`。

**核心发现**：

4 个方向共 12 篇论文，B-IAVR 的 novelty 定位清晰——它处于四个方向的交汇点：

- **最接近的工作**是 *Learning When to Plan* (Paglieri 2025)，但它不使用 action change 信号且无 budget 约束
- **Lagrangian 实现**建议用 PID Lagrangian (Stooke 2020) 而非朴素 dual ascent，避免验证率振荡
- **训练解耦**可借鉴 DeGRPO (Thinkless, Fang 2025)，分离 verification decision 与 task performance 的学习信号
- **Action change 信号的理论锚点**是 Causal Influence Detection (Seitzer 2021)，但 B-IAVR 度量的是反向因果：verification→action 而非 action→state

Phase B 实现时的关键对标：always-on (SCoRe)、random verification、fixed-ratio 作为 baseline，报告 verification ratio 和 budget utilization 指标。

---
