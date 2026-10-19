# 竞品论文验证报告 (2026-05-17)

## 1. GAGPO (2605.13217) — 验证通过

- **arXiv ID**: 2605.13217 → 指向正确论文
- **标题**: "GAGPO: Generalized Advantage Grouped Policy Optimization"
  - 注意：任务描述中的 "Grouped Value Proxy + Temporal Credit Propagation" 不是论文标题组成部分，但 "Grouped Value Proxy" 是论文中核心机制的术语，"recursively propagating outcome supervision backward through time" 对应 Temporal Credit Propagation 概念
- **作者**: Siyuan Zhu, Chao Yu, Rongxin Yang, Zongkai Liu, Jinjun Hu, Qiwen Chen, Yibo Zhang
- **Venue/Year**: arXiv, May 2026
- **关键实验数据**:
  - ALFWorld 93.5±1.3% (Qwen2.5-1.5B) — 与声称一致
  - ALFWorld 95.6±0.9% (Qwen2.5-7B)
  - WebShop 88.6±3.3 score / 78.1% success (1.5B)
  - GRPO baseline: 70.3% (1.5B), 73.2% (7B)
  - GiGPO baseline: 88.1% (1.5B), 88.8% (7B)
- **方法**: 非参数 grouped value proxy + TD/GAE-style step advantages + group-normalized PPO update, critic-free
- **与我们的关系**: 追求更细粒度 credit assignment 以提高性能；我们诊断为什么 step-independent 失败

## 2. MT-GRPO (2505.11821) — 验证通过（需修正描述）

- **arXiv ID**: 2505.11821 → 指向正确论文
- **标题**: "Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design"
- **作者**: Quan Wei, Siliang Zeng, Chenliang Li, William Brown, Oana Frunza, Wei Deng, Anderson Schneider, Yuriy Nevmyvaka, Yang Katie Zhao, Alfredo Garcia, Mingyi Hong
- **Venue/Year**: arXiv, May 2025 (revised Oct 2025)
- **关键实验数据**:
  - 评测在 QA 数据集（NQ, TriviaQA, PopQA, HotpotQA, 2WikiMultiHopQA, Musique）
  - 不包含 ALFWorld
  - 使用 Qwen2.5-7B
  - MT-GRPO 术语在 Section 3.2 中正式使用
  - 近 100% format correctness, answer correctness ~0.45-0.65 across datasets
- **修正**: 该论文是 turn-level reward design for search/QA tasks，非 ALFWorld agent 任务
- **与我们的关系**: 同样发现 turn-level credit 优于 trajectory-level；我们的 contrarian 结论是 episode-level (coarser) 反而消除 sign misattribution

## 3. iStar (2509.19199) — 验证通过

- **arXiv ID**: 2509.19199 → 指向正确论文
- **标题**: "Agentic Reinforcement Learning with Implicit Step Rewards"
- **作者**: Xiaoqian Liu, Ke Wang, Yuchuan Wu, Fei Huang, Yongbin Li, Junge Zhang, Jianbin Jiao
- **Venue/Year**: ICLR 2026（OpenReview 确认: openreview.net/forum?id=ooROvpmxMV）
- **关键实验数据**:
  - WebShop: 86.5±2.8% success, 93.6±1.0 score (Qwen2.5-7B)
  - VisualSokoban: 91.7% success (Qwen2.5-VL-7B)
  - SOTOPIA: +48% goal completion vs GPT-4o (Llama3.1-8B)
  - 不包含 ALFWorld 评测
- **方法**: Implicit PRM (trajectory DPO objective) + dual advantage (step-level + episode-level)
- **与我们的关系**: 追求更细粒度 step-level credit (通过学习 implicit rewards)；我们展示 episode-level 单独即可消除 sign misattribution

## 4. ArCHer (2402.19446) — 验证通过

- **arXiv ID**: 2402.19446 → 指向正确论文
- **标题**: "ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL"
- **作者**: Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, Aviral Kumar
- **Venue/Year**: ICML 2024（icml.cc/virtual/2024/poster/33654 确认）
- **关键实验数据**:
  - ~100x sample efficiency improvement over flat RL
  - 验证至 7B 参数规模
  - 评测：web interaction, tool use, customer support
- **方法**: 高层 off-policy value-based RL（utterance 级 Q-function）+ 低层 token policy (within-turn)
- **与我们的关系**: 开创性框架，建立 multi-turn RL 需要层次结构的共识；我们具体诊断为什么 flat step-independent 失败

## 5. CA Survey (2604.09459) — 验证通过

- **arXiv ID**: 2604.09459 → 指向正确论文
- **标题**: "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models"
- **作者**: Chenchen Zhang（单一作者）
- **Venue/Year**: arXiv, April 2026
- **关键内容**:
  - 47 种 CA 方法（41 core + 6 adjacent enablers），2024-2026 时间范围
  - 二维分类：粒度（token, segment, step, turn, multi-agent）x 方法论（MC, TD, model-based, game-theoretic, information-theoretic）
  - 涵盖 reasoning RL 和 agentic RL 两个 regime
  - 附带 reporting checklist + benchmark protocol specification + method selection decision tree
- **与我们的关系**: 提供 credit assignment 全景图；我们的 sign misattribution 诊断属于其分类中 under-explored 的 failure mode 分析

## 6. HiPER (2602.16165) — 实验设置确认

- **arXiv ID**: 2602.16165 → 指向正确论文
- **标题**: "HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents"
- **作者**: Jiangweizhi Peng, Yuanxin Liu, Ruida Zhou, Charles Fleming, Zhaoran Wang, Alfredo Garcia, Mingyi Hong
- **Venue/Year**: arXiv, February 2026
- **实验设置详细数据**:
  - 模型：Qwen2.5-1.5B-Instruct, Qwen2.5-7B-Instruct
  - ALFWorld: 95.3% (1.5B), 97.4% (7B)
  - GRPO baseline: 71.1% (1.5B), 85.4% (7B)
  - GiGPO baseline: 被引为 "best prior method"（HiPER +8.6% over GiGPO on 1.5B, +6.6% on 7B）
  - WebShop: 83.3% (7B)
  - 训练：150 epochs, 3 random seeds
  - Prompt template: Plan-Execute (HiPER) vs ReAct (baselines)
  - 训练效率：7B 约 50 steps 超过 80% success（PPO/GRPO 需 ~140 steps, 2.8x 加速）
- **与我们的关系**: 追求 SOTA performance via hierarchical architecture；我们做 mechanism diagnosis

---

## 总结表

| 论文 | 验证状态 | arXiv ID | Venue | 关键修正/备注 |
|------|---------|----------|-------|--------------|
| GAGPO | PASS | 2605.13217 | arXiv 2026 | 标题 "Generalized Advantage"（"Grouped Value Proxy" 是方法术语） |
| MT-GRPO | PASS | 2505.11821 | arXiv 2025 | 不含 ALFWorld，评测在 QA 数据集 |
| iStar | PASS | 2509.19199 | ICLR 2026 | 不含 ALFWorld，评测在 WebShop/VisualSokoban/SOTOPIA |
| ArCHer | PASS | 2402.19446 | ICML 2024 | 确认 venue |
| CA Survey | PASS | 2604.09459 | arXiv 2026 | 单一作者，47 方法确认 |
| HiPER | CONFIRMED | 2602.16165 | arXiv 2026 | 97.4%(7B)/95.3%(1.5B), GRPO 71.1%/85.4% |

## Positioning 启示

1. **共识趋势**: 竞品一致走向 finer-grained credit (turn-level, step-level, hierarchical)
2. **我们的 contrarian**: Episode-level (coarser) 消除 sign misattribution，诊断 "更细不一定更好" 的反直觉结论
3. **差异化轴**: 竞品追求 performance improvement；我们做 mechanism diagnosis + contrarian solution
4. **Turn-PPO 最直接竞品**: 发现相似问题 ("uniform advantage" ≈ 我们的 sign misattribution subset)，但解法相反（finer vs coarser）
