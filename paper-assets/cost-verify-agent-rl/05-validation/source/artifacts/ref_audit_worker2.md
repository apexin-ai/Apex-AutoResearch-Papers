# Reference Audit Report (Worker 2)

**Date**: 2026-05-26
**Bib file**: `docs/paper/references.bib`
**Total entries**: 48
**Method**: Each entry verified via WebSearch (title + first author, arXiv ID where applicable)

## Verification Table

| # | bib key | 标题 | 存在 | 作者 | 年份 | 标题准确 | Venue | 备注 |
|---|---------|------|------|------|------|----------|-------|------|
| 1 | qwen3_2025 | Qwen3 Technical Report | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2505.09388 | |
| 2 | shridhar2021alfworld | ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2021 | |
| 3 | digiRL2024 | DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2024 | |
| 4 | feng2025gigpo | GiGPO: Group-in-Group Policy Optimization for LLM Agent Training | ✓ | ✓ | ✓ | ✗ | ✓ NeurIPS 2025 | 官方标题无 "GiGPO:" 前缀，应为 "Group-in-Group Policy Optimization for LLM Agent Training" |
| 5 | kim2025reflact | ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection | ✓ | ✓ | ✓ | ✓ | ✓ EMNLP 2025 | |
| 6 | ragen2025 | RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2504.20073 | |
| 7 | schulman2016gae | High-Dimensional Continuous Control Using Generalized Advantage Estimation | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2016 | |
| 8 | selfguide2026 | Co-Evolution of Policy and Internal Reward for Language Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2604.03098 | |
| 9 | shao2024deepseekmath | DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2402.03300 | |
| 10 | spear2025 | Learn the Ropes, Then Trust the Wins: Self-Imitation with Progressive Exploration for Agentic RL | ✓ | ✓ | ✓ | ✓ | ✗ | **已被 ICLR 2026 接收**，bib 中 venue 为 ICLR（year=2026，正确），但 bib key 含 "2025" 有误导性 |
| 11 | sutton1988td | Learning to Predict by the Methods of Temporal Differences | ✓ | ✓ | ✓ | ✓ | ✓ Machine Learning 3(1) | 经典论文 |
| 12 | wang2022scienceworld | ScienceWorld: Is Your Agent Smarter Than a 5th Grader? | ✓ | ✓ | ✓ | ✓ | ✓ EMNLP 2022 | 官方标题小写 "your"/"than"，但 BibTeX 大小写由模板控制，非实质错误 |
| 13 | williams1992reinforce | Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ Machine Learning 8(3-4) | 经典论文 |
| 14 | irc2026 | Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2604.02869 | |
| 15 | mcgrpo2026 | MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout RL | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2601.22582 | |
| 16 | grpolambda2025 | GRPO-λ: Credit Assignment improves LLM Reasoning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2510.00194 | |
| 17 | oar2026 | Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2601.07408 | |
| 18 | ragen2_2026 | RAGEN-2: Reasoning Collapse in Agentic RL | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2604.06268 | |
| 19 | grpocollapse2025 | On Group Relative Policy Optimization Collapse in Agent Search: The Lazy Likelihood-Displacement | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2512.04220 | 使用 v2 标题（v1 标题含 "GRPO" 和 "Search-R1"） |
| 20 | gradientcoupling2025 | Rethinking Reward Miscalibration of GRPO in Agentic RL | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2509.23870 | **未在任何 tex 文件中被引用** |
| 21 | turnppo2025 | Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs | ✓ | ✓ | ✓ | ✓ | ✗ | **已被 EACL 2026 Findings 接收**（pp. 6227-6243），bib 仍标为 arXiv preprint |
| 22 | gagpo2026 | GAGPO: Generalized Advantage Grouped Policy Optimization | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2605.13217 | |
| 23 | mtgrpo2025 | Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2505.11821 | 使用 v2 标题（v1 为 "Turn-Level Credit Assignment"）；**未在任何 tex 文件中被引用** |
| 24 | sweetrl2025 | SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2503.15478 | **未在任何 tex 文件中被引用** |
| 25 | schulman2017ppo | Proximal Policy Optimization Algorithms | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:1707.06347 | 从未正式发表于会议 |
| 26 | foerster2018coma | Counterfactual Multi-Agent Policy Gradients | ✓ | ✓ | ✓ | ✓ | ✓ AAAI 2018 | **未在任何 tex 文件中被引用** |
| 27 | schulman2015trpo | Trust Region Policy Optimization | ✓ | ✗ | ✓ | ✓ | ✓ ICML 2015 | **作者顺序错误**：bib 为 Schulman, Levine, Abbeel, Jordan, Moritz；正确顺序为 Schulman, Levine, **Moritz**, **Jordan**, **Abbeel**。**未在任何 tex 文件中被引用** |
| 28 | wang2024mathshepherd | Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | ✓ | ✓ | ✓ | ✓ | ✗ | Venue 应为 "Proceedings of the **Annual Meeting of the** Association for Computational Linguistics"（缺少 "Annual Meeting of"）；**未在任何 tex 文件中被引用** |
| 29 | lightman2024lets | Let's Verify Step by Step | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2024 | |
| 30 | yao2023react | ReAct: Synergizing Reasoning and Acting in Language Models | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2023 | |
| 31 | andrychowicz2017her | Hindsight Experience Replay | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2017 | **未在任何 tex 文件中被引用** |
| 32 | ng1999shaping | Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping | ✓ | ✓ | ✓ | ✓ | ✓ ICML 1999 | **未在任何 tex 文件中被引用** |
| 33 | ouyang2022instructgpt | Training Language Models to Follow Instructions with Human Feedback | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2022 | |
| 34 | rafailov2023dpo | Direct Preference Optimization: Your Language Model is Secretly a Reward Model | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2023 | |
| 35 | hcapo2026 | Hindsight Credit Assignment for Long-Horizon LLM Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2603.08754 | |
| 36 | rcgrpo2026 | RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2602.03025 | |
| 37 | istar2025 | Agentic Reinforcement Learning with Implicit Step Rewards | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2509.19199 | 使用 v3 标题（v1/v2 为 "Online Process Reward Learning for Agentic RL"）；**未在任何 tex 文件中被引用** |
| 38 | agenticrl_survey2026 | From Reasoning to Agentic: Credit Assignment in RL for Large Language Models | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2604.09459 | **未在任何 tex 文件中被引用** |
| 39 | edgegrpo2025 | EDGE-GRPO: Entropy-Driven GRPO with Guided Error Correction for Advantage Diversity | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2507.21848 | |
| 40 | harutyunyan2019hindsight | Hindsight Credit Assignment | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2019 | **未在任何 tex 文件中被引用** |
| 41 | arjona2019rudder | RUDDER: Return Decomposition for Delayed Rewards | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2019 | **未在任何 tex 文件中被引用** |
| 42 | kaelbling1998planning | Planning and Acting in Partially Observable Stochastic Domains | ✓ | ✓ | ✓ | ✓ | ✓ Artificial Intelligence 101(1-2) | 经典论文 |
| 43 | dapo2025 | DAPO: An Open-Source LLM Reinforcement Learning System at Scale | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2503.14476 | **未在任何 tex 文件中被引用** |
| 44 | vapo2025 | VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2504.05118 | |
| 45 | prime2025 | Process Reinforcement through Implicit Rewards | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2502.01456 | |
| 46 | zhou2024archer | ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL | ✓ | ✓ | ✓ | ✓ | ✓ ICML 2024 | |
| 47 | kazemnejad2024vineppo | VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2024 | 标题在不同版本间有变化，bib 使用 OpenReview/NeurIPS 版本 |
| 48 | ahmadian2024back | Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs | ✓ | ✓ | ✓ | ✗ | ✓ ACL 2024 | 官方标题为 "REINFORCE-Style"（带连字符），bib 写作 "REINFORCE Style"；**未在任何 tex 文件中被引用** |

## Citation Context Verification

All 34 cited references' citation contexts were checked against paper content. No citation-content mismatches found — each `\cite{}` usage accurately describes the cited paper's contribution.

## Summary

### 严重问题（需修复）

1. **schulman2015trpo (#27): 作者顺序错误** — Abbeel 和 Moritz 位置互换。正确顺序：Schulman, Levine, Moritz, Jordan, Abbeel。
2. **turnppo2025 (#21): Venue 过时** — 已被 EACL 2026 Findings 接收（pages 6227-6243），应从 `@article` 改为 `@inproceedings`。
3. **14 条 bib entry 未被引用**：gradientcoupling2025, mtgrpo2025, sweetrl2025, foerster2018coma, schulman2015trpo, wang2024mathshepherd, andrychowicz2017her, ng1999shaping, istar2025, agenticrl_survey2026, harutyunyan2019hindsight, arjona2019rudder, dapo2025, ahmadian2024back。应删除未引用条目或补充引用。

### 中等问题

4. **feng2025gigpo (#4): 标题含非官方前缀** — 官方标题无 "GiGPO:" 前缀。BibTeX 中用 `{GiGPO}` 保护大小写是常见做法，但标题本身应与官方一致。
5. **wang2024mathshepherd (#28): Venue 名不完整** — 缺少 "Annual Meeting of"，应为 "Proceedings of the Annual Meeting of the Association for Computational Linguistics"。
6. **ahmadian2024back (#48): 标题轻微不准** — 官方标题为 "REINFORCE-Style"（有连字符），bib 写作 "REINFORCE Style"。

### 轻微问题

7. **spear2025 (#10)**: bib key 含 "2025" 但论文发表年份为 2026（ICLR 2026），bib 中 year=2026 是正确的，仅 key 名有误导性。
8. **wang2022scienceworld (#12)**: 标题大小写与官方版本略有差异（"Your"/"Than" vs "your"/"than"），由 BibTeX 样式控制，非实质问题。

### 统计

- 全部 48 条引用**均真实存在**，无虚构论文
- 作者错误：1 条（#27）
- 标题不准确：2 条（#4 前缀、#48 连字符）
- Venue 需更新：2 条（#21 已被会议接收、#28 名称不完整）
- 未引用条目：14 条
