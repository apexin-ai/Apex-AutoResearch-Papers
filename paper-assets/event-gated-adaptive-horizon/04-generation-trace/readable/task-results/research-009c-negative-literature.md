# research 009c negative literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_009c-negative-literature_20260514T142523_result.json`
- **Structured JSON:** [`71bec197af98fc79c3a5.json`](../../sessions/71/71bec197af98fc79c3a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已更新 memory.md，在末尾追加了 "## 2026-05-14: 009c Negative 文献联动" section。核心结论：

**最相关的 3 篇文献：**
- **Nikishin et al. 2022 (ICML)** — primacy bias，agent 对早期经验过拟合，不同 seed → 不同表征质量。最强候选机制。
- **Janner et al. 2019 (NeurIPS)** — compounding error 随 rollout 长度指数增长，temporal abstraction 等效延长 rollout。
- **Lambert et al. 2020 (L4DC)** — objective mismatch，1-step loss 好不代表多步 rollout 好。

**对 009c 的解释：** primacy bias + compounding error amplification 的组合。Temporal abstraction 将 effective horizon 从 H 放大到 H×dt，指数级放大 seed 间 world model 质量的微小差异，导致 seed 2 崩塌而 seed 1 正常。与 delusional critic 正交。

**Paper framing 建议：** 不要声称新失败模式，而是展示 temporal abstraction 如何将已知的 seed variance 从可控变为灾难性。这一交互效应在文献中未被报告，是新颖的贡献点。

---
