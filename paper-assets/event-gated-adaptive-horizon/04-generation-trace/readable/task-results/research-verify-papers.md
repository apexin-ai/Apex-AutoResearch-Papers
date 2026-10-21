# research verify papers

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-papers_20260513T095035_result.json`
- **Structured JSON:** [`44c5682a925d775b26de.json`](../../sessions/44/44c5682a925d775b26de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 核实结果

### 1. ASI (Adaptive Skip Intervals) — Neitz et al., NeurIPS 2018

**原论文实际做法：** 对所有 H 个未来输入评估 reconstruction loss，仅对最小 loss 的那个做反向传播（"akin to pooling over losses"）。方法针对 recurrent dynamical models 的时间抽象，不涉及 MBRL planning/policy 集成。

**我们的描述准确性：✅ 准确**

"min-pooling over reconstruction losses" 和 "without MBRL integration" 均与原论文一致。

---

### 2. LS-Imagine — Li/Wang et al., ICLR 2025 Oral

**原论文实际做法：** 引入 jumping flag 控制 long-term（jumpy）和 short-term 状态转移的切换。当 affordance map 的 kurtosis 较高时（表示远处有 task-related target），触发 jumpy transition。Jumpy transition 是 **goal-conditioned**（以目标状态为条件），通过 image zoom-in 生成 affordance maps。在 MineDojo 上评估。

**我们的描述准确性：⚠️ 部分准确**

- "jumping flags based on affordance-map kurtosis" ✅
- "MineDojo" ✅
- **"action-independent jumps" 不精确** → 原论文的 jumpy transitions 是 **goal-conditioned**，不是 action-independent。跳跃决策基于 affordance map kurtosis（与 action 无关），但 transition 本身是以 goal 为条件的。

**修正建议：** 将 "with action-independent jumps" 改为 "with goal-conditioned jumpy state transitions"。

---

### 3. DyMoDreamer — Zhang et al., NeurIPS 2025

**原论文实际做法：** 用 inter-frame differencing mask 从观测中提取 differential observations，编码运动线索。Dynamic modulation 建模为 stochastic categorical distributions，**集成到 RSSM 潜在空间中**，增强对 reward-relevant dynamics 的感知。基于 DreamerV3 架构。

**我们的描述准确性：⚠️ 部分准确**

- "inter-frame differencing masks" ✅
- "stochastic categorical dynamic modulation" ✅
- "focus RSSM attention on motion-relevant features" ✅
- **"Operates at observation/pixel level" 不精确** → inter-frame differencing 在 observation level 提取特征，但 dynamic modulation 集成到 RSSM latent space。方法跨越 observation 和 latent 两个层级，不是仅在 pixel level 操作。

**修正建议：** 将 "Operates at observation/pixel level" 改为 "extracts motion cues at the observation level and integrates dynamic modulation into the RSSM latent space" 或更简洁地 "bridges observation-level motion cues with latent-space dynamics modeling"。

---

Sources:
- [ASI - NeurIPS 2018 proceedings](https://proceedings.neurips.cc/paper/2018/hash/0f0ee3310223fe38a989b2c818709393-Abstract.html)
- [ASI - arXiv](https://arxiv.org/abs/1808.04768)
- [LS-Imagine - arXiv](https://arxiv.org/abs/2410.03618)
- [LS-Imagine - OpenReview](https://openreview.net/forum?id=vzItLaEoDa)
- [LS-Imagine - arXiv HTML](https://arxiv.org/html/2410.03618)
- [DyMoDreamer - arXiv](https://arxiv.org/abs/2509.24804)
- [DyMoDreamer - OpenReview](https://openreview.net/forum?id=SYKwGnik3w)

---
