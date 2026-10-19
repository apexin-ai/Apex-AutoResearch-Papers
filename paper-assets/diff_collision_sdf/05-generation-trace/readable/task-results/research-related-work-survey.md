# research related work survey

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_survey_20260523T030015_result.json`
- **Structured JSON:** [`12e37f40bfdb9cb7b71a.json`](../../sessions/12/12e37f40bfdb9cb7b71a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/related_work_survey.md`。

**核心发现：**

- **方向1 (VLA Safety)**: 找到5篇直接相关论文（SafeVLA, AEGIS, CoFreeVLA, SAFE, CompliantVLA-adaptor）。最直接的竞品是 AEGIS（推理时 CBF 修正）和 SafeVLA（RL 约束优化）。**没有任何工作在训练时用连续 SDF 信号做 auxiliary loss**——这是明确的 novelty gap。

- **方向2 (Fake Safety)**: **显著 novelty gap**。"overly conservative policy"被多篇论文提及（FISOR, POLICEd RL），但无人定义指标来检测"因不动而安全"。frozen_rate 是原创贡献。

- **方向3 (SDF in Manipulation)**: SDF 在传统规划中成熟（RDF, CDF, iSDF），但从未用于 VLA 模型的 auxiliary training signal。我们在几何规划和端到端 VLA 学习之间架桥。

- **方向4 (Safety Metrics)**: Safety-Gymnasium、GUARD 提供方法论模板，VLA Safety Survey (2026) 直接讨论 VLA 安全评估。

- **方向5 (Auxiliary Loss)**: RAIL（推理时安全滤波）、Reward Training Wheels（自适应权重调度）可借鉴；Diehl et al. 是重要反方——主张硬约束优于软 auxiliary loss，需要在论文中讨论这个 trade-off。

---
