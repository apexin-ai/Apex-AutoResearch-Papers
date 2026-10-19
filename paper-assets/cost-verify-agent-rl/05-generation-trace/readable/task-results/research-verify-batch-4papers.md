# research verify batch 4papers

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-batch-4papers_20260517T120548_result.json`
- **Structured JSON:** [`20ead170c302d5751c2f.json`](../../sessions/20/20ead170c302d5751c2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完毕，汇总如下：

---

## 论文 1: MT-GRPO (arXiv: 2505.11821)

1. **存在性**: ✅ 真实存在
2. **标题**: "Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design" | 作者: Quan Wei, Siliang Zeng, Chenliang Li, William Brown, Oana Frunza, Wei Deng, Anderson Schneider, Yuriy Nevmyvaka, Yang Katie Zhao, Alfredo Garcia, Mingyi Hong | 日期: 2025-05-17 (v1), 2025-10-23 (v2) | Venue: 未标注会议
3. **核心贡献**: 将 GRPO/PPO 扩展为 multi-turn 版本（MT-GRPO/MT-PPO），引入两类 turn-level reward（verifiable reward + LLM-as-judge），实现细粒度 credit assignment。实验基于 Qwen2.5-7B + TriviaQA 搜索任务，8×H100，基于 vLLM rollout。
4. **与我们的关系**: **direct competitor** — 同样解决 multi-turn agent 中 episode-level reward 的 credit assignment 问题，方法路线高度重叠（turn-level reward + GRPO 改造）
5. **威胁程度**: **HIGH** — 方向完全对标，已有 v2 版本且有 GitHub 代码开源。需要明确与其差异化。

---

## 论文 2: GAGPO (arXiv: 2605.13217)

1. **存在性**: ✅ 真实存在
2. **标题**: "GAGPO: Generalized Advantage Grouped Policy Optimization" | 作者: Siyuan Zhu, Chao Yu, Rongxin Yang, Zongkai Liu, Jinjun Hu, Qiwen Chen, Yibo Zhang | 日期: 2026-05-13 | Venue: 未标注
3. **核心贡献**: Critic-free 的 step-level credit assignment — 从 rollout 构建非参数化 grouped value proxy，用 TD/GAE 风格递归反向传播 advantage，无需训练 value model。在 **ALFWorld 和 WebShop**（multi-turn agent 任务）上超越 PPO/RLOO/GRPO/GiGPO。
4. **与我们的关系**: **direct competitor** — critic-free step-level credit assignment 在 multi-turn agent 环境上的方案，与我们解决同一问题
5. **威胁程度**: **HIGH** — 2026-05-13 刚发布（4天前），方法新颖（critic-free TD/GAE proxy），且在 ALFWorld/WebShop 上有强 baseline 对比。非常新的竞争者。

---

## 论文 3: Survey (arXiv: 2604.09459)

1. **存在性**: ✅ 真实存在
2. **标题**: "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models" | 作者: Chenchen Zhang | 日期: 2026-04-10 (v1), 2026-04-13 (v2) | Venue: arXiv preprint
3. **核心贡献**: 综述 47 种 credit assignment 方法，建立二维 taxonomy（粒度维度: token/segment/step/turn/multi-agent × 方法维度: MC/TD/model-based/game-theoretic/info-theoretic）。明确覆盖 episode-level vs step-level 对比，指出 episode-level credit 在 agentic 场景下越来越 uninformative。
4. **与我们的关系**: **complementary** — 我们的工作会被归入这个 taxonomy，survey 帮助我们 positioning，同时我们需要确保被引用
5. **威胁程度**: **LOW** — survey 不是竞争者，但需要确保我们的 framing 和 taxonomy 对齐，且投稿时引用此 survey。

---

## 论文 4: Practitioner's Guide (arXiv: 2510.01132)

1. **存在性**: ✅ 真实存在
2. **标题**: "A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning" | 作者: Ruiyi Wang, Prithviraj Ammanabrolu | 日期: 2025-10-01 (v1), 2025-12-06 (v2) | Venue: **submitted to ICLR 2026**（OpenReview 可查，未见接收决定）
3. **核心贡献**: 系统分析 multi-turn agentic RL 的三大 design pillar（environment / reward / policy），在 TextWorld、ALFWorld、SWE-Gym 上实证 ablation。关键发现：dense turn-level reward 加速训练但效果高度依赖 RL 算法选择；分析了 PPO/GRPO/RLOO 在不同 reward sparsity 下的表现；给出 SFT→RL 最优预算分配。**明确分析了 episode-level vs step-level reward。**
4. **与我们的关系**: **complementary** — 提供了实证 recipe，不是提出新算法。但其 ablation 结果直接影响我们的实验设计和 claim
5. **威胁程度**: **MEDIUM** — 不是直接竞争者（empirical guide vs 新方法），但其 findings 可能 challenge 我们的某些 design choice。submitted to ICLR 2026，有代码开源。需要引用并确保我们的方法在其 framework 下 make sense。

---

### 总结

| 论文 | 存在性 | 关系 | 威胁 |
|------|--------|------|------|
| MT-GRPO (2505.11821) | ✅ | direct competitor | **HIGH** |
| GAGPO (2605.13217) | ✅ | direct competitor | **HIGH** |
| Survey (2604.09459) | ✅ | complementary | LOW |
| Practitioner's Guide (2510.01132) | ✅ | complementary | MEDIUM |

**最需关注**: GAGPO 4 天前刚发布，critic-free step-level credit assignment 路线与我们高度相关；MT-GRPO 已有 v2 和代码，是最成熟的直接竞争者。

Sources:
- [MT-GRPO (2505.11821)](https://arxiv.org/abs/2505.11821)
- [GAGPO (2605.13217)](https://arxiv.org/abs/2605.13217)
- [Survey (2604.09459)](https://arxiv.org/abs/2604.09459)
- [Practitioner's Guide (2510.01132)](https://arxiv.org/abs/2510.01132)
- [Practitioner's Guide OpenReview](https://openreview.net/forum?id=K6T0o875zF)
- [MT-GRPO GitHub](https://github.com/SiliangZeng/Multi-Turn-RL-Agent)

---
