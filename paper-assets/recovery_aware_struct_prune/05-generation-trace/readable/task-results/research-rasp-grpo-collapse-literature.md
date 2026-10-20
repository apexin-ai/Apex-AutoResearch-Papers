# research rasp grpo collapse literature

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_rasp-grpo-collapse-literature_20260515T183848_result.json`
- **Structured JSON:** [`a341b6fcba7f7d0a6d30.json`](../../sessions/a3/a341b6fcba7f7d0a6d30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/literature_review_cka_rl_stability.md`。核心结论：

**四个问题的回答：**

1. **CKA-guided pruning 在 RL 场景的失败先例** — 没有。文献空白。Self-Healing 等工作只用 standard importance pruning。

2. **功能多样性如何影响 RL 稳定性** — 有间接证据链但无直接研究：Abbas (Nature 2024) 证明 plasticity 需要持续多样性注入；Obando-Ceron (ICML 2024) 证明 element-wise pruning 减少 gradient interference 有利于 RL；Choice of Divergence (2025) 证明 RLVR 本身有 diversity collapse 倾向。但**没有人研究过"去除冗余保留多样性"反而损害 RL 训练**。

3. **Self-Healing 是否测试了其他 pruning criterion** — 没有。他们只用 standard structured pruning，聚焦 recovery method 创新。

4. **"Pruning criterion × recovery method interaction"** — 仅有 supervised 场景先例（Renda ICLR 2020; PASER 2025; Think Before You Prune 2025）。**RL recovery 场景完全没有**。

**Novelty 评级：高。** 

最强支撑假说的论文是 **Choice of Divergence (2509.07430)**——RLVR 的 reverse-KL 天然 mode-seeking，会压缩输出多样性。如果 CKA pruning 已经移除了结构冗余（减少表征空间的"备用路径"），GRPO 的 mode-seeking 机制会加速 collapse。Standard pruning 偶然保留冗余 = 天然的 plasticity buffer。这条"CKA 去冗余 + RLVR mode-seeking = 双重压缩"的机制链是完整的，且无人提出过。

---
