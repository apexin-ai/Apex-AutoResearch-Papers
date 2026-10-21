# Citation Audit — 2026-05-15

对 `literature_map.yaml` 中全部 27 篇论文进行 arXiv ID、标题、作者、会议验证。额外验证用户指定的 Thinkless。

---

## 严重问题（必须修正）

| 论文 | 问题 | 详情 | 建议修正 |
|------|------|------|----------|
| **AgentPRM** (`chatterjee2025agentprm`) | arXiv ID 错误、作者错误、标题映射错误 | 当前 ID `2502.10325` 实际是 Sanjiban Choudhury 的 "Process Reward Models for LLM Agents: Practical Framework and Directions"，与 AgentPRM 无关。真正的 AgentPRM 论文是 `2511.08325`（Xi et al.）。作者写的 "Chatterjee et al." 在两篇论文中均不存在。 | `arxiv_id: "2511.08325"`，`authors: "Xi et al."`，`title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"` |
| **Huang2024** (`huang2024self-correction-survey`) | 作者错误 | 文献 map 写 "Huang et al."，但该论文第一作者是 Ryo Kamoi，五位作者中无人姓 Huang。 | `authors: "Kamoi et al."`，citation key 改为 `kamoi2024self-correction-survey` |
| **DAPO** (`dapo2025`) | 标题错误 | 文献 map 标题 "DAPO: Decoupled Clip and Dynamic Sampling Policy Optimization"，实际标题 "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"。"Decoupled Clip and Dynamic Sampling" 是技术描述，非论文标题。 | `title: "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"` |

## 中等问题（建议修正）

| 论文 | 问题 | 详情 | 建议修正 |
|------|------|------|----------|
| **CFGM** (`cfgm2026`) | 会议和年份错误，缺 arXiv ID | 文献 map 标记为 "arXiv" 2026，实际已发表于 **EMNLP 2025**（ACL Anthology 确认）。arXiv ID 为 2508.15305。 | `venue: "EMNLP 2025"`，`year: 2025`，`arxiv_id: "2508.15305"` |
| **WebAgent-R1** (`pei2025webagent-r1`) | 作者引用 key 错误 | Citation key 为 "pei2025" 暗示第一作者姓 Pei，但实际第一作者为 Zhepei Wei。 | `authors: "Wei et al."`，citation key 改为 `wei2025webagent-r1` |

## 轻微问题（可选修正）

| 论文 | 问题 | 详情 |
|------|------|------|
| **Singhi2025** (`singhi2025when-to-verify`) | 标题略有出入 | Map: "...Compute-Optimal Verification for LLM Reasoning"；实际: "...Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning" |
| **AutoThink** (`tu2025autothink`) | 标题格式 | Map: "AutoThink: Learning When to Think via Multi-Stage RL"；实际: "Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL"（"AutoThink" 是项目名非论文标题） |

---

## 验证通过

| # | 论文 | arXiv ID | 标题 | 会议 | 状态 |
|---|------|----------|------|------|------|
| 1 | Self-Guide | 2604.03098 | Co-Evolution of Policy and Internal Reward for Language Agents | arXiv 2026 | ✅ ID/标题/作者均匹配 |
| 2 | ARES | 2603.07915 | Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents | arXiv 2026 | ✅ 匹配（注：论文用 "Ares" 非全大写 "ARES"） |
| 3 | Self-Verification Dilemma | 2602.03485 | Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning | arXiv 2026 | ✅ |
| 4 | Zhang2025 Self-Verify | 2506.01369 | Incentivizing LLMs to Self-Verify Their Answers | arXiv 2025 | ✅ |
| 5 | MAR | 2512.20845 | MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs | arXiv 2025 | ✅ |
| 6 | SSR | 2511.10621 | SSR: Socratic Self-Refine for Large Language Model Reasoning | arXiv 2025 | ✅ |
| 7 | Sherlock | 2511.00330 | Sherlock: Reliable and Efficient Agentic Workflow Execution | arXiv 2025 | ✅ |
| 8 | Singhi2025 | 2504.01005 | When To Solve, When To Verify... | arXiv 2025 | ✅ (标题略有缩写) |
| 9 | Efficient Agents | 2508.02694 | Efficient Agents: Building Effective Agents While Reducing Cost | arXiv 2025 | ✅ |
| 10 | Trust but Verify | 2508.16665 | Trust but Verify! A Survey on Verification Design for Test-time Scaling | arXiv 2025 | ✅ |
| 11 | SORL | 2511.20718 | Stabilizing Off-Policy Training for Long-Horizon LLM Agent... | arXiv 2025 | ✅ (map 用缩写标题) |
| 12 | Agentic RL Survey | 2509.02547 | The Landscape of Agentic Reinforcement Learning for LLMs: A Survey | TMLR 2026 | ✅ (OpenReview 确认 TMLR) |
| 13 | ReSpAct | 2411.00927 | ReSpAct: Harmonizing Reasoning, Speaking, and Acting... | arXiv 2024 | ✅ |
| 14 | ReflAct | 2505.15182 | ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection | EMNLP 2025 | ✅ (需补 arXiv ID) |
| 15 | GiGPO | 2505.10978 | Group-in-Group Policy Optimization for LLM Agent Training | NeurIPS 2025 | ✅ (需补 arXiv ID) |
| 16 | SPEAR | 2509.22601 | Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration... | ICLR 2026 | ✅ (需补 arXiv ID) |
| 17 | Derailer-Rerailer | 2408.13940 | Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning | ACL 2025 Findings | ✅ (需补 arXiv ID) |
| 18 | AutoThink | 2505.10832 | Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models... | NeurIPS 2025 | ✅ (需补 arXiv ID) |
| 19 | CorrectBench | 2510.16062 | Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs | NeurIPS 2025 D&B | ✅ (需补 arXiv ID) |
| 20 | DigiRL | 2406.11896 | DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL | NeurIPS 2024 | ✅ (需补 arXiv ID) |
| 21 | Retrospex | 2505.11807 | Retrospex: Language Agent Meets Offline Reinforcement Learning Critic | EMNLP 2024 | ✅ (需补 arXiv ID) |
| 22 | WebAgent-R1 | 2505.16421 | WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL | EMNLP 2025 | ✅ (需补 arXiv ID) |

## 用户指定的额外验证

| 论文 | 结果 |
|------|------|
| **Thinkless** | ✅ 真实存在。arXiv 2505.13379，NeurIPS 2025 poster 确认。作者：Gongfan Fang, Xinyin Ma, Xinchao Wang。**注意：Thinkless 未收录在 literature_map.yaml 中，与 AutoThink 是不同论文。** |

## 缺失 arXiv ID 汇总（建议补充）

以下论文在 literature_map.yaml 中 `arxiv_id: null`，已通过搜索找到：

| 论文 | 应补充的 arXiv ID |
|------|-------------------|
| CorrectBench | 2510.16062 |
| GiGPO | 2505.10978 |
| SPEAR | 2509.22601 |
| WebAgent-R1 | 2505.16421 |
| DigiRL | 2406.11896 |
| Derailer-Rerailer | 2408.13940 |
| AutoThink | 2505.10832 |
| ReflAct | 2505.15182 |
| Retrospex | 2505.11807 |
| CFGM | 2508.15305 |
