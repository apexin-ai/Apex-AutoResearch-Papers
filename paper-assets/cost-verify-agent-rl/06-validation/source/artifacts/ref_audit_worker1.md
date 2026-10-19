# Reference Audit Report (Worker 1/3)

**Date**: 2026-05-26
**Bib file**: `docs/paper/references.bib`
**Total entries**: 48
**Method**: Each entry verified via WebSearch (title + first author)

---

## Verification Table

| # | Bib Key | 标题 | 存在 | 作者 | 年份 | 标题准确 | Venue | 备注 |
|---|---------|------|------|------|------|----------|-------|------|
| 1 | `qwen3_2025` | Qwen3 Technical Report | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2505.09388 | — |
| 2 | `shridhar2021alfworld` | ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2021 | — |
| 3 | `digiRL2024` | DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2024 | — |
| 4 | `feng2025gigpo` | GiGPO: Group-in-Group Policy Optimization for LLM Agent Training | ✓ | ✓ | ✓ | ⚠️ | ✓ NeurIPS 2025 | 官方标题可能不含 "GiGPO:" 前缀（OpenReview 标题为 "Group-in-Group Policy Optimization for LLM Agent Training"）。多数 bib 风格可接受，**低风险** |
| 5 | `kim2025reflact` | ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection | ✓ | ✓ | ✓ | ✓ | ✓ EMNLP 2025 | — |
| 6 | `ragen2025` | RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn RL | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2504.20073 | — |
| 7 | `schulman2016gae` | High-Dimensional Continuous Control Using Generalized Advantage Estimation | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2016 | — |
| 8 | `selfguide2026` | Co-Evolution of Policy and Internal Reward for Language Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2604.03098 | — |
| 9 | `shao2024deepseekmath` | DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2402.03300 | — |
| 10 | `spear2025` | Learn the Ropes, Then Trust the Wins: Self-Imitation with Progressive Exploration for Agentic RL | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2026 | bib key 名含 "2025" 但 year 字段正确为 2026 |
| 11 | `sutton1988td` | Learning to Predict by the Methods of Temporal Differences | ✓ | ✓ | ✓ | ✓ | ✓ Machine Learning 3(1):9-44 | — |
| 12 | `wang2022scienceworld` | ScienceWorld: Is Your Agent Smarter Than a 5th Grader? | ✓ | ✓ | ✓ | ✓ | ✓ EMNLP 2022 | — |
| 13 | `williams1992reinforce` | Simple Statistical Gradient-Following Algorithms for Connectionist RL | ✓ | ✓ | ✓ | ✓ | ✓ Machine Learning 8(3-4):229-256 | — |
| 14 | `irc2026` | Multi-Turn RL for Tool-Calling Agents with Iterative Reward Calibration | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2604.02869 | — |
| 15 | `mcgrpo2026` | MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout RL | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2601.22582 | — |
| 16 | `grpolambda2025` | GRPO-λ: Credit Assignment improves LLM Reasoning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2510.00194 | — |
| 17 | `oar2026` | Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2601.07408 | — |
| 18 | `ragen2_2026` | RAGEN-2: Reasoning Collapse in Agentic RL | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2604.06268 | — |
| 19 | `grpocollapse2025` | On Group Relative Policy Optimization Collapse in Agent Search: The Lazy Likelihood-Displacement | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2512.04220 | bib 使用 v2 标题（正确），v1 标题不同 |
| 20 | `gradientcoupling2025` | Rethinking Reward Miscalibration of GRPO in Agentic RL | ✓ | ✓ | ✓ | **✗** | ✓ arXiv 2509.23870 | **标题为 v1 版**。v2 已改名为 "Gradient Coupling: The Hidden Barrier to Generalization in Agentic Reinforcement Learning"。bib key 名 "gradientcoupling" 暗示作者知道 v2，但 title 字段未更新 |
| 21 | `turnppo2025` | Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs | ✓ | ✓ | ✓ | ✓ | **⚠️** arXiv 2512.17008 | 已被 **EACL 2026 Findings** 接收，bib 仍标为 arXiv preprint |
| 22 | `gagpo2026` | GAGPO: Generalized Advantage Grouped Policy Optimization | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2605.13217 | — |
| 23 | `mtgrpo2025` | Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2505.11821 | bib 使用 v2 标题（正确） |
| 24 | `sweetrl2025` | SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2503.15478 | — |
| 25 | `schulman2017ppo` | Proximal Policy Optimization Algorithms | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 1707.06347 | — |
| 26 | `foerster2018coma` | Counterfactual Multi-Agent Policy Gradients | ✓ | ✓ | ✓ | ✓ | ✓ AAAI 2018 | — |
| 27 | `schulman2015trpo` | Trust Region Policy Optimization | ✓ | **✗** | ✓ | ✓ | ✓ ICML 2015 | **作者顺序错误**。bib: Schulman, Levine, Abbeel, Jordan, Moritz → 正确顺序: Schulman, Levine, **Moritz**, **Jordan**, **Abbeel** |
| 28 | `wang2024mathshepherd` | Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | ✓ | ✓ | ✓ | ✓ | ✓ ACL 2024 | — |
| 29 | `lightman2024lets` | Let's Verify Step by Step | ✓ | **✗** | ✓ | ✓ | ✓ ICLR 2024 | **两个作者名拼写错误**："Yuri Burda" → **"Yura Burda"**；"Harrison Edwards" → **"Harri Edwards"** |
| 30 | `yao2023react` | ReAct: Synergizing Reasoning and Acting in Language Models | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2023 | — |
| 31 | `andrychowicz2017her` | Hindsight Experience Replay | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2017 | — |
| 32 | `ng1999shaping` | Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping | ✓ | ✓ | ✓ | ✓ | ✓ ICML 1999 | — |
| 33 | `ouyang2022instructgpt` | Training Language Models to Follow Instructions with Human Feedback | ✓ | **⚠️** | ✓ | ✓ | ✓ NeurIPS 2022 | 第二作者 "Jeffrey Wu" 在论文原文和 NeurIPS 记录中为 **"Jeff Wu"** |
| 34 | `rafailov2023dpo` | Direct Preference Optimization: Your Language Model is Secretly a Reward Model | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2023 | — |
| 35 | `hcapo2026` | Hindsight Credit Assignment for Long-Horizon LLM Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2603.08754 | — |
| 36 | `rcgrpo2026` | RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2602.03025 | — |
| 37 | `istar2025` | Agentic Reinforcement Learning with Implicit Step Rewards | ✓ | ✓ | **✗** | ✓ | **✗** | **已被 ICLR 2026 接收**，bib 仍标为 arXiv preprint 且 year=2025，应更新为 ICLR 2026 (year=2026) |
| 38 | `agenticrl_survey2026` | From Reasoning to Agentic: Credit Assignment in RL for Large Language Models | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2604.09459 | — |
| 39 | `edgegrpo2025` | EDGE-GRPO: Entropy-Driven GRPO with Guided Error Correction for Advantage Diversity | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2507.21848 | — |
| 40 | `harutyunyan2019hindsight` | Hindsight Credit Assignment | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2019 | — |
| 41 | `arjona2019rudder` | RUDDER: Return Decomposition for Delayed Rewards | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2019 | — |
| 42 | `kaelbling1998planning` | Planning and Acting in Partially Observable Stochastic Domains | ✓ | ✓ | ✓ | ✓ | ✓ Artificial Intelligence 101(1-2):99-134 | — |
| 43 | `dapo2025` | DAPO: An Open-Source LLM Reinforcement Learning System at Scale | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2503.14476 | — |
| 44 | `vapo2025` | VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2504.05118 | — |
| 45 | `prime2025` | Process Reinforcement through Implicit Rewards | ✓ | ✓ | ✓ | ✓ | ✓ arXiv 2502.01456 | — |
| 46 | `zhou2024archer` | ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL | ✓ | ✓ | ✓ | ✓ | ✓ ICML 2024 | — |
| 47 | `kazemnejad2024vineppo` | VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment | ✓ | ✓ | ✓ | **✗** | ✓ NeurIPS 2024 | **标题为旧版 preprint 标题**。NeurIPS 正式发表标题为 "VinePPO: Refining Credit Assignment in RL Training of LLMs" |
| 48 | `ahmadian2024back` | Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs | ✓ | ✓ | ✓ | **⚠️** | ✓ ACL 2024 | ACL Anthology 标题使用 "REINFORCE**-**Style"（带连字符），bib 缺连字符 |

---

## 问题汇总

### 严重问题（需修复）

| # | Bib Key | 问题 | 建议修复 |
|---|---------|------|----------|
| 1 | `schulman2015trpo` | **作者顺序错误**：Abbeel 和 Moritz 位置互换 | 改为 `Schulman, John and Levine, Sergey and Moritz, Philipp and Jordan, Michael and Abbeel, Pieter` |
| 2 | `lightman2024lets` | **两个作者名拼写错误** | "Yuri Burda" → "Yura Burda"；"Harrison Edwards" → "Harri Edwards" |
| 3 | `istar2025` | **Venue 和 Year 过时**：已被 ICLR 2026 接收 | 改为 `@inproceedings`，booktitle = ICLR，year = 2026 |
| 4 | `kazemnejad2024vineppo` | **标题为旧 preprint 版本** | 改为 "VinePPO: Refining Credit Assignment in RL Training of LLMs" |
| 5 | `gradientcoupling2025` | **标题为 v1 版本，论文已在 v2 更名** | 改为 "Gradient Coupling: The Hidden Barrier to Generalization in Agentic Reinforcement Learning" |

### 中等问题（建议修复）

| # | Bib Key | 问题 |
|---|---------|------|
| 6 | `turnppo2025` | 已被 EACL 2026 Findings 接收，bib 仍为 arXiv preprint |
| 7 | `ouyang2022instructgpt` | 第二作者 "Jeffrey Wu" 在原文为 "Jeff Wu" |
| 8 | `ahmadian2024back` | ACL 正式标题用 "REINFORCE-Style"（带连字符） |

### 低风险（可选修复）

| # | Bib Key | 问题 |
|---|---------|------|
| 9 | `feng2025gigpo` | 标题含 "GiGPO:" 前缀，OpenReview 官方标题可能不含该前缀 |

---

## 引用使用检查

### 已引用的 34 个 bib key

所有引用均在正确的上下文中使用，无明显错引。引用分布：
- `introduction.tex`: 8 个 key
- `related_work.tex`: 20 个 key（引用最密集）
- `method.tex`: 3 个 key
- `experiments.tex`: 5 个 key
- `discussion.tex`: 2 个 key
- `appendix.tex`: 5 个 key

### 未引用的 14 个 bib key（建议清理或补引）

| Bib Key | 主题 | 建议 |
|---------|------|------|
| `gradientcoupling2025` | GRPO reward miscalibration / gradient coupling | **强烈建议引用**——与本文主题高度相关 |
| `sweetrl2025` | SWEET-RL multi-turn LLM agents | **建议引用**——直接竞品 |
| `mtgrpo2025` | Multi-turn reasoning via turn-level reward design | **建议引用**——直接竞品 |
| `istar2025` | Implicit step rewards for agentic RL | **建议引用**——直接竞品（且已在 bib 中） |
| `ahmadian2024back` | Revisiting REINFORCE for RLHF | 建议引用（appendix 中提到 REINFORCE++ 但未引此文） |
| `foerster2018coma` | COMA counterfactual multi-agent policy gradients | 建议引用（appendix 中有 multi-agent 类比但未引） |
| `wang2024mathshepherd` | Math-Shepherd step-by-step verification | 可选引用（process supervision 相关） |
| `ng1999shaping` | Reward shaping theory | 可选引用（reward shaping 理论基础） |
| `agenticrl_survey2026` | Credit assignment in RL for LLMs survey | 可选引用 |
| `harutyunyan2019hindsight` | Hindsight credit assignment (classic RL) | 可选引用（经典 credit assignment） |
| `andrychowicz2017her` | Hindsight Experience Replay | 可选引用 |
| `arjona2019rudder` | RUDDER return decomposition | 可选引用 |
| `dapo2025` | DAPO open-source LLM RL system | 可选引用 |
| `schulman2015trpo` | TRPO | 可选引用 |

---

## 总结

- **48 条引用全部真实存在**，无虚构论文
- **5 个严重问题**需修复：作者顺序（TRPO）、作者名拼写（Let's Verify Step by Step）、venue/year 过时（istar）、标题过时（VinePPO、gradientcoupling）
- **3 个中等问题**建议修复
- **14 个 bib entry 未被引用**，其中 4 个与论文主题高度相关，建议补引或清理
- 所有已引用的 34 条引用在 tex 中的使用上下文均正确，无错引
