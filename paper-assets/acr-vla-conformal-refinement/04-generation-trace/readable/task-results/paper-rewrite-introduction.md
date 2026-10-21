# paper rewrite introduction

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rewrite-introduction_20260515T194914_result.json`
- **Structured JSON:** [`47817b32931fdb45959c.json`](../../sessions/47/47817b32931fdb45959c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存至 `artifacts/_project/paper/introduction_scenarioC.tex` 并注册。

结构概要：
- **Para 1** — 问题：VLA 在分布偏移下退化；现有 inference-time 方法的局限（ReconVLA 只做 selection，SC-VLA 需 RL，VLA-Pilot 延迟高，A2C2 非 post-hoc）
- **Para 2** — Gap：selection 受限于候选质量；learned correction 可以超越，但 conditioning 选什么？
- **Para 3** — ACR-VLA pipeline：K=10 sampling → CGS argmin selection → CRM bounded residual（329K params, obs embedding input, offline L2 training）
- **Para 4** — 三个发现：(1) sample-then-correct +7.0pp on Object；(2) per-DOF conformal features 是 honest negative（11.0% vs 19.0%）；(3) magnitude control 关键（1.42→0%, [0.05,0.2] safe）；Spatial null result 显著报告
- **Para 5** — 三个 contributions（编号列表，与任务要求一致）

所有数字来自 paper_framing.md/writing_plan.yaml，无 overclaim，无 statistical significance 声明，Spatial null result 未隐藏。

---
