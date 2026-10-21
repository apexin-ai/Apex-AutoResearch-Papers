# writing related work

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work_20260516T015413_result.json`
- **Structured JSON:** [`97fef6db92101125812c.json`](../../sessions/97/97fef6db92101125812c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。Related Work 写入 `paper/sections/related_work.md`，~1200 words，覆盖全部 6 个要求主题：

- **TAWM 定位**（第 3 段）：MPC vs imagination-based AC 的核心区别，明确 "dt-conditioning is not inherently broken; the vulnerability is specific to imagination-based actor-critic training"
- **Model-free temporal abstraction**：Options, FiGAR, TempoRL, action repetition, frame skip, time discretization sensitivity
- **World-model RL**：DreamerV1/V2/V3, TD-MPC2, Director, THICK, Hieros
- **Value overestimation**：Thrun, TD3, SAC, MBPO, MOPO + CIVO 与 Lu et al. delusional bias 的显式区分 + 梯度分解（HarmonyDream, GradNorm）
- **Multi-step prediction error**：Ke, Asadi, Lambert；排除 compounding error 作为主因
- **Diagnostic methodology**：Engstrom, Andrychowicz；定位 non-method contribution 的价值

35 篇引用，全部使用 `\cite{paper_id}` 格式。D061 必引文献（hafner2023dreamerv3, ma2024harmonydream, chen2018gradnorm）均已覆盖。未使用 "delusional critic" 指代本文机制。

---
