# Reference Audit Report — Worker 3

**审核日期**: 2026-05-26
**bib 文件**: `docs/paper/references.bib`
**总条目数**: 48

## 核查结果总表

| # | bib key | 标题 | 存在 | 作者 | 年份 | 标题准确 | Venue | 备注 |
|---|---------|------|------|------|------|----------|-------|------|
| 1 | `qwen3_2025` | Qwen3 Technical Report | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2505.09388 | |
| 2 | `shridhar2021alfworld` | ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2021 | |
| 3 | `digiRL2024` | DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2024 | arXiv:2406.11896 |
| 4 | `feng2025gigpo` | GiGPO: Group-in-Group Policy Optimization for LLM Agent Training | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2025 | arXiv:2505.10978 |
| 5 | `kim2025reflact` | ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection | ✓ | ✓ | ✓ | ✓ | ✓ EMNLP 2025 | |
| 6 | `ragen2025` | RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2504.20073 | |
| 7 | `schulman2016gae` | High-Dimensional Continuous Control Using Generalized Advantage Estimation | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2016 | |
| 8 | `selfguide2026` | Co-Evolution of Policy and Internal Reward for Language Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2604.03098 | |
| 9 | `shao2024deepseekmath` | DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models | ✓ | ✗ | ✓ | ✓ | ✓ arXiv:2402.03300 | 作者列表中 "Li, Y.K." "Wu, Y." 使用缩写，应写全名 |
| 10 | `spear2025` | SPEAR: Learn the Ropes, Then Trust the Wins... | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2026 | bib key 名含 2025 仅为命名；year 字段已正确写 2026 |
| 11 | `sutton1988td` | Learning to Predict by the Methods of Temporal Differences | ✓ | ✓ | ✓ | ✓ | ✓ ML 3(1), 9–44 | 经典文献 |
| 12 | `wang2022scienceworld` | ScienceWorld: Is Your Agent Smarter Than a 5th Grader? | ✓ | ✓ | ✓ | ✓ | ✓ EMNLP 2022 | |
| 13 | `williams1992reinforce` | Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ ML 8(3–4), 229–256 | 经典文献 |
| 14 | `irc2026` | Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2604.02869 | |
| 15 | `mcgrpo2026` | MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2601.22582 | |
| 16 | `grpolambda2025` | GRPO-λ: Credit Assignment improves LLM Reasoning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2510.00194 | 曾投 ICLR 2026 后 Withdrawn |
| 17 | `oar2026` | Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2601.07408 | 2026年1月提交，ID 正确 |
| 18 | `ragen2_2026` | RAGEN-2: Reasoning Collapse in Agentic RL | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2604.06268 | |
| 19 | `grpocollapse2025` | On Group Relative Policy Optimization Collapse in Agent Search: The Lazy Likelihood-Displacement | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2512.04220 | 标题匹配最新版本（v1 标题含 "Death Spiral" 后缀） |
| 20 | `gradientcoupling2025` | Rethinking Reward Miscalibration of GRPO in Agentic RL | ✓ | ✓ | ✓ | ✗ | ✗ | **标题已过时**：最新版已更名为 "Gradient Coupling: The Hidden Barrier to Generalization in Agentic Reinforcement Learning" |
| 21 | `turnppo2025` | Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs | ✓ | ✓ | ✓ | ✓ | ✗ | **已被 Findings of EACL 2026 接收**（ACL Anthology: 2026.findings-eacl.328），bib 仍标为 arXiv preprint |
| 22 | `gagpo2026` | GAGPO: Generalized Advantage Grouped Policy Optimization | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2605.13217 | |
| 23 | `mtgrpo2025` | Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2505.11821 | NeurIPS 2025 Workshop / ICML 2025 Workshop（非主会议） |
| 24 | `sweetrl2025` | SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks | ✓ | ✓ | ✓ | ✓ | ✗ | **已被 ICML 2025 接收**，bib 仍标为 arXiv preprint |
| 25 | `schulman2017ppo` | Proximal Policy Optimization Algorithms | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:1707.06347 | 从未正式发表于会议，arXiv preprint 正确 |
| 26 | `foerster2018coma` | Counterfactual Multi-Agent Policy Gradients | ✓ | ✓ | ✓ | ✓ | ✓ AAAI 2018 | ⚠️ **未在任何 tex 文件中引用** |
| 27 | `schulman2015trpo` | Trust Region Policy Optimization | ✓ | ✓ | ✓ | ✓ | ✓ ICML 2015, pp.1889–1897 | ⚠️ **未在任何 tex 文件中引用** |
| 28 | `wang2024mathshepherd` | Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations | ✓ | ✓ | ✓ | ✓ | ✓ ACL 2024 | ⚠️ **未在任何 tex 文件中引用** |
| 29 | `lightman2024lets` | Let's Verify Step by Step | ✓ | ✗ | ✓ | ✓ | ✓ ICLR 2024 | **作者名错误**："Yuri Burda" → "Yura Burda"；"Harrison Edwards" → "Harri Edwards" |
| 30 | `yao2023react` | ReAct: Synergizing Reasoning and Acting in Language Models | ✓ | ✓ | ✓ | ✓ | ✓ ICLR 2023 | |
| 31 | `andrychowicz2017her` | Hindsight Experience Replay | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2017 | ⚠️ **未在任何 tex 文件中引用** |
| 32 | `ng1999shaping` | Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping | ✓ | ✓ | ✓ | ✓ | ✓ ICML 1999, pp.278–287 | ⚠️ **未在任何 tex 文件中引用** |
| 33 | `ouyang2022instructgpt` | Training Language Models to Follow Instructions with Human Feedback | ✓ | ✗ | ✓ | ✓ | ✓ NeurIPS 2022 | **作者名**：NeurIPS proceedings 列为 "Jeff Wu"，bib 写 "Jeffrey Wu" |
| 34 | `rafailov2023dpo` | Direct Preference Optimization: Your Language Model is Secretly a Reward Model | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2023 | |
| 35 | `hcapo2026` | Hindsight Credit Assignment for Long-Horizon LLM Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2603.08754 | |
| 36 | `rcgrpo2026` | RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2602.03025 | |
| 37 | `istar2025` | Agentic Reinforcement Learning with Implicit Step Rewards | ✓ | ✓ | ✓ | ✓ | ✗ | **已被 ICLR 2026 接收**（OpenReview 确认），bib 仍标为 arXiv preprint，year 应改为 2026 |
| 38 | `agenticrl_survey2026` | From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2604.09459 | ⚠️ **未在任何 tex 文件中引用** |
| 39 | `edgegrpo2025` | EDGE-GRPO: Entropy-Driven GRPO with Guided Error Correction for Advantage Diversity | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2507.21848 | 曾投 ICLR 2026 后 Withdrawn |
| 40 | `harutyunyan2019hindsight` | Hindsight Credit Assignment | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2019 | ⚠️ **未在任何 tex 文件中引用** |
| 41 | `arjona2019rudder` | RUDDER: Return Decomposition for Delayed Rewards | ✓ | ✓ | ✓ | ✓ | ✓ NeurIPS 2019 | ⚠️ **未在任何 tex 文件中引用** |
| 42 | `kaelbling1998planning` | Planning and Acting in Partially Observable Stochastic Domains | ✓ | ✓ | ✓ | ✓ | ✓ AI 101(1–2), 99–134 | 经典文献 |
| 43 | `dapo2025` | DAPO: An Open-Source LLM Reinforcement Learning System at Scale | ✓ | ✓ | ✓ | ✓ | ✗ | **已被 NeurIPS 2025 接收**（poster），bib 仍标为 arXiv preprint。⚠️ **未在任何 tex 文件中引用** |
| 44 | `vapo2025` | VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2504.05118 | |
| 45 | `prime2025` | Process Reinforcement through Implicit Rewards | ✓ | ✓ | ✓ | ✓ | ✓ arXiv:2502.01456 | 已提交 ICLR 2026，状态待定 |
| 46 | `zhou2024archer` | ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL | ✓ | ✓ | ✓ | ✓ | ✓ ICML 2024 | |
| 47 | `kazemnejad2024vineppo` | VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment | ✓ | ✓ | ✓ | ✗ | ✗ | **标题与 NeurIPS 2024 proceedings 不一致**：正式标题为 "VinePPO: Accurate Credit Assignment in RL for LLM Mathematical Reasoning" |
| 48 | `ahmadian2024back` | Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs | ✓ | ✓ | ✓ | ✗ | ✓ ACL 2024 | **标题缺连字符**：ACL Anthology 正式标题为 "REINFORCE-Style"（有连字符）。⚠️ **未在任何 tex 文件中引用** |

## 问题汇总

### 必须修正的错误（5 项）

1. **`lightman2024lets` (#29)** — 作者名拼写错误：
   - `Burda, Yuri` → `Burda, Yura`
   - `Edwards, Harrison` → `Edwards, Harri`

2. **`kazemnejad2024vineppo` (#47)** — 标题与 NeurIPS 2024 正式 proceedings 不匹配：
   - bib: "VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment"
   - 正式: "VinePPO: Accurate Credit Assignment in RL for LLM Mathematical Reasoning"

3. **`gradientcoupling2025` (#20)** — 标题已过时，论文已从 v1 更名：
   - bib: "Rethinking Reward Miscalibration of GRPO in Agentic RL"
   - 最新版: "Gradient Coupling: The Hidden Barrier to Generalization in Agentic Reinforcement Learning"

4. **`ouyang2022instructgpt` (#33)** — 作者名：NeurIPS proceedings 使用 "Jeff Wu"，bib 写 "Jeffrey Wu"

5. **`ahmadian2024back` (#48)** — 标题缺连字符："REINFORCE Style" → "REINFORCE-Style"

### 建议更新 Venue（4 项）

6. **`istar2025` (#37)** — 已被 ICLR 2026 正式接收，建议改为 `@inproceedings`，year 改为 2026
7. **`sweetrl2025` (#24)** — 已被 ICML 2025 接收，建议改为 `@inproceedings`
8. **`turnppo2025` (#21)** — 已被 Findings of EACL 2026 接收（ACL Anthology: 2026.findings-eacl.328），建议更新
9. **`dapo2025` (#43)** — 已被 NeurIPS 2025 接收为 poster，建议改为 `@inproceedings`

### 未引用条目（10 项）

以下 bib 条目存在于 `references.bib` 中，但**未在任何 .tex 文件中被 `\cite` 引用**：

| # | bib key | 说明 |
|---|---------|------|
| 26 | `foerster2018coma` | COMA: Counterfactual Multi-Agent Policy Gradients (AAAI 2018) |
| 27 | `schulman2015trpo` | TRPO (ICML 2015) |
| 28 | `wang2024mathshepherd` | Math-Shepherd (ACL 2024) |
| 31 | `andrychowicz2017her` | Hindsight Experience Replay (NeurIPS 2017) |
| 32 | `ng1999shaping` | Reward Shaping (ICML 1999) |
| 38 | `agenticrl_survey2026` | Credit Assignment Survey |
| 40 | `harutyunyan2019hindsight` | Hindsight Credit Assignment (NeurIPS 2019) |
| 41 | `arjona2019rudder` | RUDDER (NeurIPS 2019) |
| 43 | `dapo2025` | DAPO (NeurIPS 2025) |
| 48 | `ahmadian2024back` | REINFORCE-Style (ACL 2024) |

BibTeX + natbib/acl 样式通常只输出被 `\cite` 引用的条目，因此这些不会出现在编译后的 PDF 中。如果不打算引用，建议从 bib 文件中移除以保持整洁。

### 次要备注

- **`shao2024deepseekmath` (#9)**：作者列表使用了缩写 "Li, Y.K." "Wu, Y."，不规范但 LaTeX 可正常渲染
- **`grpolambda2025` (#16)**：曾投 ICLR 2026 后被作者 Withdrawn，当前状态为 arXiv preprint
- **`edgegrpo2025` (#39)**：曾投 ICLR 2026 后被作者 Withdrawn
- **`grpocollapse2025` (#19)**：v1 标题含 "Death Spiral" 后缀，bib 使用最新版标题，正确
- **`mtgrpo2025` (#23)**：在 NeurIPS 2025 Workshop 和 ICML 2025 Workshop 发表（非主会议）
- **全部 48 篇论文均真实存在**，无虚构引用

## 统计

| 类别 | 数量 |
|------|------|
| 总条目 | 48 |
| 真实存在 | 48/48 (100%) |
| 信息完全正确 | 29/48 (60%) |
| 有错误需修正 | 5 |
| 建议更新 Venue | 4 |
| 未引用 | 10 |
