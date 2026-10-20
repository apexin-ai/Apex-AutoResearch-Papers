# research maniskill3 literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_maniskill3-literature_20260516T044820_result.json`
- **Structured JSON:** [`f7c5b3e629e0fe91d04e.json`](../../sessions/f7/f7c5b3e629e0fe91d04e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心发现：

**1. DreamerV3 在 ManiSkill3 上没有公开 benchmark** — 我们的工作填补空白。ManiSkill3 官方 baseline 只有 PPO/SAC/TD-MPC2/RFCL，其中 TD-MPC2（唯一 model-based）在 sparse reward 长 horizon 任务上几乎失效。

**2. World Model + Manipulation 近期活跃** — DiWA（frozen WM + diffusion policy RL）、World4RL（diffusion WM + end-to-end optimization）、HarmonyDream（+10-69% on visual robotic tasks）都是 2024-2025 新工作。核心趋势是从 planning-only 转向直接 policy optimization in learned simulators。

**3. Temporal Abstraction 直接支持 event-gated hypothesis** — THICK（ICLR 2024）学习 adaptive temporal hierarchy in world model；"When to Re-Commit"（2025）证明 state-conditioned commitment depth 优于 fixed depth（+12.5pp solve rate）；VTS-RL 将 action duration 集成到 action space。Manipulation 的 phase structure（approach→contact→manipulation→release）天然适合 event-gated 而非 fixed-rate abstraction。

**4. 实验设计 implications** — 优先选 PegInsertionSide / PlugCharger 等有明确 phase transition 的任务；baseline 对比 DreamerV3 (fixed) vs event-gated vs TD-MPC2 vs PPO；同时测 dense/sparse reward。

推荐 15 篇论文加入 literature_map.yaml，详见报告第 5 节。

---
