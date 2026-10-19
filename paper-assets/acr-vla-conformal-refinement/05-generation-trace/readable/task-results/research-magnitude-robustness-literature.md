# research magnitude robustness literature

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_magnitude-robustness-literature_20260515T155457_result.json`
- **Structured JSON:** [`71586e7de5ecdc4a8195.json`](../../sessions/71/71586e7de5ecdc4a8195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Literature map updated with 3 new entries. Here's the summary:

---

**文献覆盖度总结（correction magnitude robustness 角度）**

这个角度的文献覆盖度较低，是一个明确的 novelty 点。具体发现：

1. **无直接先例**：没有任何 prior work 研究过 per-DOF conformal correction 在高 norm bound 下崩塌的现象。最接近的是 TRANSIC（Jiang 2024）发现 ungated residual 导致 model collapse，以及 PLD（Xiao 2026）在 VLA 上做 magnitude scheduling，但它们都是 RL-based 且未涉及 conformal decomposition 方式的对比。

2. **CP 文献提供间接理论支撑**：Sampson (2024) 的 Conformal Multi-Target Hyperrectangles 证明 per-dimension Bonferroni 方法会产生 imbalanced marginal coverage——这从统计角度解释了 perdof 为什么在高 norm bound 下失败：各 DOF 的 interval 独立膨胀，丧失 inter-DOF 方向一致性。TRACE（Fang 2026）展示了 flow matching 中的 scalar transport alignment score 自然保持方向一致性，概念上支持 obs_only 的优势。

3. **Residual RL 文献关注 magnitude 但不关注 direction robustness**：Johannink (2019)、DRC (2025)、DAWN (2026) 都研究 magnitude bound/decay/scale，但无一研究 correction 方向质量与 magnitude 鲁棒性之间的关系。Dodeja (2025) 将 uncertainty 引导 residual correction，但仍是 RL 框架。

4. **我们的 novelty**：首次实证表明 observation-conditioned scalar correction 对 norm bound 天然鲁棒（因为它学到了好的方向），而 per-DOF conformal quantile correction 在高 norm bound 下方向失控导致崩塌。这揭示了 correction parameterization（scalar/joint vs per-DOF）与 magnitude robustness 之间此前未被认识到的联系。

---
