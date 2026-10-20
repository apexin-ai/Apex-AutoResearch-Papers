# research plan017 literature linkage

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan017-literature-linkage_20260514T053739_result.json`
- **Structured JSON:** [`13ed612c92fdc0fdbe55.json`](../../sessions/13/13ed612c92fdc0fdbe55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have everything I need. Here are the results.

---

## 文献搜索结果

### 高相关（直接支持你的发现）

**1. Spurious Rewards: Rethinking Training Signals in RLVR**
- 作者: Ruixin Yang et al.
- 年份: 2025, arXiv:2506.10947
- Venue: NeurIPS 2025 submission
- **关联**: 最直接相关。发现 GRPO+随机 reward 在 Qwen2.5-Math 上提升 21.4%，几乎追平 ground-truth reward 的 29.1%。这与你的 additive random (PR=48%) > additive ISR (PR=18%) 完全一致——说明看似信息量丰富的结构指标可能比随机噪声更有害，因为它引入了系统性偏差而非单纯噪声。但该文也发现这种效应在 Llama3 上不成立，说明与预训练数据有关。
- **加入 literature_map**: 是。role: `direct-evidence`, category: `reward-hacking`

**2. Scaling Laws for Reward Model Overoptimization**
- 作者: Leo Gao, John Schulman, Jacob Hilton (OpenAI)
- 年份: 2023, ICML 2023 (arXiv:2210.10760)
- Venue: ICML 2023
- **关联**: 奠基性工作。用 gold/proxy reward 实验范式量化了 Goodhart 效应——proxy reward 持续上升但 gold reward 先升后降。你的 ISR 就是一个 proxy reward，其"持续上升"但 true performance (PR) 下降，完美符合此框架。
- **加入 literature_map**: 是。role: `theoretical-foundation`, category: `reward-hacking`

**3. Goodhart's Law in Reinforcement Learning**
- 作者: Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse
- 年份: 2024, ICLR 2024 (arXiv:2310.09144)
- Venue: ICLR 2024
- **关联**: 提供了 Goodhart's Law 在 MDP 中的几何解释——优化不完美 proxy 超过临界点后 true objective 下降。你的 ISR additive 实验可以用这个框架解释：ISR 作为 proxy 与 execution correctness 只有部分相关，超过临界优化点后策略转向高 ISR 但低 correctness 的方向。
- **加入 literature_map**: 是。role: `theoretical-foundation`, category: `reward-hacking`

**4. The Lessons of Developing Process Reward Models in Mathematical Reasoning**
- 作者: Zhenru Zhang et al. (Qwen Team, Alibaba)
- 年份: 2025, ACL 2025 Findings (arXiv:2501.07301)
- Venue: ACL 2025 Findings
- **关联**: 发现 MC estimation 合成的 PRM 数据质量差，导致 PRM 性能劣于 ORM。关键发现：policy model 生成"答案正确但推理过程有缺陷"的 response，导致 process reward 与 outcome 的 misalignment。这与你的 ISR 问题相似——结构正确但语义错误的 proof trace 获得高 ISR 但低 execution reward。
- **加入 literature_map**: 是。role: `supporting-evidence`, category: `reward-shaping`

### 中等相关（理论框架支持）

**5. Reward Shaping to Mitigate Reward Hacking in RLHF**
- 作者: Fu et al.
- 年份: 2025, arXiv:2502.18770
- Venue: arXiv preprint
- **关联**: 发现 PPO 训练中存在 reward threshold——超过阈值后 reward hacking 启动，win rate 下降。提出 reward 应 bounded 且 rapid initial growth + gradual convergence。你的 additive ISR 可能违反了这两个原则——ISR 信号过强且无上界约束。
- **加入 literature_map**: 可选。role: `background`, category: `reward-hacking`

**6. RL with Verifiable yet Noisy Rewards under Imperfect Verifiers**
- 作者: arXiv:2510.00915
- 年份: 2025
- **关联**: 形式化了 verifier 噪声（false positive/negative）对 GRPO 训练的影响。你的 ISR 可以视为一个 systematically biased verifier——不是随机噪声，而是系统性地对 "structurally correct but semantically wrong" 的 traces 给出 false positive。该文表明随机噪声可以校正，但系统性偏差更难处理。
- **加入 literature_map**: 可选。role: `background`, category: `reward-shaping`

### 文献空白分析

搜索未找到以下内容的直接文献：
- **结构/质量指标"仅适合诊断不适合训练"的明确讨论**：现有文献将 Goodhart's Law 和 reward hacking 作为一般性现象讨论，但没有论文明确提出"某些指标天然适合 post-hoc 诊断但不适合作为训练信号"这一范式区分。这是你们论文的独特贡献点。
- **formal verification/Prolog 领域的结构 reward 实验**：reward hacking 文献集中在 math reasoning 和 general RLHF，formal proof generation 领域是空白。

**结论：你的 "diagnostic-only metric" 发现是一个真正的文献空白**。Gao et al. 和 Karwowski et al. 提供理论框架（Goodhart's Law），Spurious Rewards 提供经验佐证（random > structured reward 的现象），但没有论文将这些整合为"某些指标仅适合诊断"的规范性主张。这对 novelty 是好事。

Sources:
- [Spurious Rewards: Rethinking Training Signals in RLVR](https://arxiv.org/abs/2506.10947)
- [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760)
- [Goodhart's Law in Reinforcement Learning](https://arxiv.org/abs/2310.09144)
- [The Lessons of Developing Process Reward Models in Mathematical Reasoning](https://arxiv.org/abs/2501.07301)
- [Reward Shaping to Mitigate Reward Hacking in RLHF](https://arxiv.org/abs/2502.18770)
- [RL with Verifiable yet Noisy Rewards under Imperfect Verifiers](https://arxiv.org/abs/2510.00915)
- [Defining and Characterizing Reward Hacking (Skalse et al., NeurIPS 2022)](https://arxiv.org/abs/2209.13085)
- [The Effects of Reward Misspecification (Pan et al., 2022)](https://arxiv.org/abs/2201.03544)

---
