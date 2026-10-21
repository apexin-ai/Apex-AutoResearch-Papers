# research competitor analysis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_competitor-analysis_20260514T071515_result.json`
- **Structured JSON:** [`6ca79cb55a7db800f7fa.json`](../../sessions/6c/6ca79cb55a7db800f7fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`artifacts/competitor_analysis.md` 已完成并注册（`art_20260514_621600`）。

文档包含：
- **方法对比表**：10 个维度横向对比 ACR-VLA vs SC-VLA / VLA-Pilot / ACoT-VLA / ReconVLA
- **逐竞品深度分析**：方法、设计决策、实验结果、局限性、与 ACR-VLA 的本质区别
- **4 个 USP 提炼**：Per-DOF granularity、learned correction、statistical guarantees、online adaptation
- **Related Work 定位建议**：5 段叙事结构 + 可直接用于论文的差异化表述

核心发现：ReconVLA 是最直接竞争者（同用 CP + frozen VLA），但 ACR-VLA 在三个层面超越——Per-DOF vs scalar UQ、learned CRM vs sample selection、ACI+COC online adaptation vs static calibration。

---
