# Reference Audit — Worker A

## 总结
- 总条目数：68
- ✓ 确认正确：57
- ⚠ Minor 问题：6
- ✗ 发现问题：5
- 幻觉论文：0（全部 68 篇均真实存在）

### 问题严重程度分级

**严重错误（必须修正）：5 条**
| # | cite_key | 问题 |
|---|----------|------|
| 33 | toolace-2025 | 第一作者姓氏错误（Zhang → Liu） |
| 19 | amitai2024explaining | 第二作者名字错误（Guy → Yael） |
| 23 | reflexion-2023 | 遗漏第三作者 Edward Berman |
| 51 | agent-safetybench-2024 | 作者列表严重错误：2 名虚构作者、2 名错误名字、从 7 人膨胀为 9 人 |
| 59 | automix-2024 | 作者列表严重错误：多人姓名错误、包含非作者、遗漏 7+ 共同作者 |

**Minor 问题（建议修正）：6 条**
| # | cite_key | 问题 |
|---|----------|------|
| 8 | ares-2026 | "and others" 但实际只有 5 位作者，应列全 |
| 38 | saferoute-2025 | 标题用 "LLMs" 而非原文 "Large Language Models" |
| 46 | salt-2026 | 作者 "David Yan" vs ACL Anthology 官方 "Qiaojing Yan" |
| 62 | bonagiri2025check | 作者顺序错误（Kumaraguru 应为第二作者） |
| 20 | gajcin2023counterfactual | 标题省略 "Doctoral Consortium" 后缀 |
| 43 | pona2025abstract | arXiv 预印本，实际已被 NeurIPS 2025 接收，可更新 venue |

### 正文引用上下文问题：2 处
| 位置 | cite_key | 问题 |
|------|----------|------|
| related_work.tex L15 | axis-2026 | 被描述为 "axis-aligned perturbations"，但论文标题为 "Integrating Counterfactual Simulations..."，描述可能不准确 |
| related_work.tex L15 | cso-2026 | 被描述为 "causal structure discovery"，但论文是 "Verified Critical Step Optimization"，描述不够精确 |

---

## 逐条核对

### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?
- 真实性：✓
- 作者：✓
- 年份：✓ (2022)
- 标题：✓
- Venue：✓ (EMNLP 2022)
- ID：N/A
- 正文引用上下文：✓

### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (ICLR 2023)
- ID：N/A
- 正文引用上下文：✓

### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A
- 正文引用上下文：✓

### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓ (标题大小写与 arXiv 原文略有差异，"Multi-step" vs "multi-step"，属 bib style 常规处理)
- Venue：✓ (arXiv:2303.09014)
- ID：✓
- 正文引用上下文：✓

### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A
- 正文引用上下文：✓

### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs
- 真实性：✓
- 作者：✓
- 年份：✓ (2025)
- 标题：✓
- Venue：✓ (arXiv:2504.11536)
- ID：✓
- 正文引用上下文：✓

### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2602.12662)
- ID：✓
- 正文引用上下文：✓

### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents
- 真实性：✓
- 作者：⚠ bib 用 "and others" 但实际只有 5 位作者（Yang, Jingbo; Hou, Bairu; Wei, Wei; Bao, Yujia; Chang, Shiyu），应列出全部
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2603.07915)
- ID：✓
- 正文引用上下文：✓

### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation
- 真实性：✓
- 作者：✓
- 年份：✓ (2025)
- 标题：✓
- Venue：✓ (NeurIPS 2025)
- ID：N/A
- 正文引用上下文：✓

### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓ (en-dash vs hyphen 差异属排版问题)
- Venue：✓ (ACL 2026 Main Conference)
- ID：N/A
- 正文引用上下文：✓

### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2604.19749)
- ID：✓
- 正文引用上下文：✓

### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2605.09252)
- ID：✓
- 正文引用上下文：✓

### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2605.00136)
- ID：✓
- 正文引用上下文：✓

### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2605.00737)
- ID：✓
- 正文引用上下文：✓

### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2011)
- 标题：✓
- Venue：✓ (AISTATS 2011)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (ICLR 2021)
- ID：N/A
- 正文引用上下文：✓

### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2015)
- 标题：✓
- Venue：✓ (JMLR, vol. 16(1), pp. 1437-1480)
- ID：N/A
- 正文引用上下文：✓

### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes
- 真实性：✓
- 作者：✗ 第二作者 "Guy Septon" 应为 **"Yael Septon"**
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (AAAI 2024)
- ID：N/A
- 正文引用上下文：✓

### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：⚠ 原文全标题含 "Doctoral Consortium" 后缀，bib 中省略
- Venue：✓ (AAMAS 2023)
- ID：N/A
- 正文引用上下文：✓

### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (Artificial Intelligence, vol. 295, p. 103455)
- ID：N/A
- 正文引用上下文：✓

### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data
- 真实性：✓
- 作者：✓
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (arXiv:2406.18665)
- ID：✓
- 正文引用上下文：✓

### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning
- 真实性：✓
- 作者：✗ 遗漏第三作者 **Edward Berman**。完整列表：Shinn, Noah; Cassano, Federico; **Berman, Edward**; Gopinath, Ashwin; Narasimhan, Karthik; Yao, Shunyu
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A
- 正文引用上下文：✓

### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey
- 真实性：✓
- 作者：✓
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (arXiv:2405.17935)
- ID：✓
- 正文引用上下文：✓

### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents
- 真实性：✓
- 作者：✓
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (ICLR 2024)
- ID：N/A
- 正文引用上下文：✓

### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (ICML 2024)
- ID：N/A
- 正文引用上下文：✓

### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset
- 真实性：✓
- 作者：✓
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)
- ID：N/A
- 正文引用上下文：✓

### 29. [qwen25-2024] — Qwen2.5 Technical Report
- 真实性：✓
- 作者：✓
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (arXiv:2412.15115)
- ID：✓
- 正文引用上下文：✓

### 30. [llama3-2024] — The Llama 3 Herd of Models
- 真实性：✓
- 作者：✓ (Grattafiori 为 v3 第一作者，与最新 arXiv 版本一致)
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (arXiv:2407.21783)
- ID：✓
- 正文引用上下文：✓

### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors
- 真实性：✓
- 作者：✓
- 年份：✓ (2008)
- 标题：✓
- Venue：✓ (The Review of Economics and Statistics, vol. 90(3), pp. 414-427)
- ID：N/A
- 正文引用上下文：✓

### 32. [achiam2017cpo] — Constrained Policy Optimization
- 真实性：✓
- 作者：✓
- 年份：✓ (2017)
- 标题：✓
- Venue：✓ (ICML 2017, pp. 22-31)
- ID：N/A
- 正文引用上下文：✓

### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling
- 真实性：✓
- 作者：✗ 第一作者姓氏错误：bib 写 **"Zhang, Weiwen"**，实际应为 **"Liu, Weiwen"**（刘维文）。经 arXiv:2409.00920 和 ICLR 2025 proceedings 确认。
- 年份：✓ (2025)
- 标题：✓
- Venue：✓ (ICLR 2025)
- ID：N/A
- 正文引用上下文：✓

### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (Canadian Journal of Economics, vol. 56(3), pp. 839-858)
- ID：N/A
- 正文引用上下文：✓

### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes
- 真实性：✓
- 作者：✓
- 年份：✓ (2012)
- 标题：✓
- Venue：✓ (ICML 2012)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks
- 真实性：✓
- 作者：✓
- 年份：✓ (2016)
- 标题：✓
- Venue：✓ (arXiv:1603.08983)
- ID：✓
- 正文引用上下文：✓

### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox
- 真实性：✓
- 作者：✓
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (ICLR 2024, Spotlight)
- ID：N/A
- 正文引用上下文：✓

### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs
- 真实性：✓
- 作者：✓
- 年份：✓ (2025)
- 标题：⚠ bib 用缩写 "LLMs"，原文标题用 "Large Language Models"
- Venue：✓ (Findings of ACL 2025)
- ID：N/A
- 正文引用上下文：✓

### 39. [altman1999constrained] — Constrained Markov Decision Processes
- 真实性：✓
- 作者：✓
- 年份：✓ (1999)
- 标题：✓
- Venue：✓ (Chapman & Hall/CRC)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2002)
- 标题：✓
- Venue：✓ (Machine Learning, vol. 49(2-3), pp. 267-290)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 41. [natarajan2013learning] — Learning with Noisy Labels
- 真实性：✓
- 作者：✓
- 年份：✓ (2013)
- 标题：✓
- Venue：✓ (NeurIPS 2013)
- ID：N/A
- 正文引用上下文：✓

### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2602.21227)
- ID：✓
- 正文引用上下文：✓

### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents
- 真实性：✓
- 作者：✓
- 年份：✓ (2025)
- 标题：✓
- Venue：⚠ bib 标为 arXiv，实际已被 NeurIPS 2025 接收（poster）
- ID：✓ (arXiv:2506.02946)
- 正文引用上下文：✓

### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2602.03412)
- ID：✓
- 正文引用上下文：⚠ related_work.tex 中描述为 "causal structure discovery"，但论文实际是 Critical Step Optimization，描述不够精确

### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour
- 真实性：✓
- 作者：✓
- 年份：✓ (2025，bib year 字段正确；cite key 中 "2026" 仅为命名习惯)
- 标题：✓
- Venue：✓ (arXiv:2505.17801)
- ID：N/A
- 正文引用上下文：⚠ related_work.tex 中描述为 "axis-aligned perturbations"，但论文标题和内容是关于 counterfactual simulations，描述可能不准确

### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph
- 真实性：✓
- 作者：⚠ bib 列 "Yan, David"，ACL Anthology 官方列 "Yan, Qiaojing"（可能为同一人的不同名）
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (Findings of EACL 2026)
- ID：N/A
- 正文引用上下文：✓

### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size
- 真实性：✓
- 作者：✓ (Gemma Team)
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (arXiv:2408.00118)
- ID：✓
- 正文引用上下文：✓

### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels
- 真实性：✓
- 作者：✓
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (JAIR, vol. 70, pp. 1373-1411)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2020)
- 标题：✓
- Venue：✓ (ICLR 2020)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping
- 真实性：✓
- 作者：✓
- 年份：✓ (1999)
- 标题：✓
- Venue：✓ (ICML 1999)
- ID：N/A
- 正文引用上下文：✓

### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents
- 真实性：✓
- 作者：✗ 严重错误。bib 列 9 位作者，实际仅 7 位。具体：
  - "Yang, Junhao" → 应为 **"Yang, Junxiao"**
  - "Wang, Renhao" → 应为 **"Wang, Hongning"**
  - **"Liu, Jie"** 和 **"Li, Jiangjie"** 为虚构作者，不在该论文中
  - 正确完整列表：Zhang, Zhexin; Cui, Shiyao; Lu, Yida; Zhou, Jingzhuo; Yang, Junxiao; Wang, Hongning; Huang, Minlie
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (arXiv:2412.14470)
- ID：✓
- 正文引用上下文：✓

### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference
- 真实性：✓
- 作者：✓
- 年份：✓ (2009)
- 标题：✓
- Venue：✓ (Cambridge University Press, 2nd edition)
- ID：N/A
- 正文引用上下文：✓

### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies
- 真实性：✓
- 作者：✓
- 年份：✓ (1974)
- 标题：✓
- Venue：✓ (Journal of Educational Psychology, vol. 66(5), pp. 688-701)
- ID：N/A
- 正文引用上下文：✓

### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
- 真实性：✓
- 作者：✓
- 年份：✓ (2022)
- 标题：✓
- Venue：✓ (JMLR, vol. 23(120), pp. 1-39)
- ID：N/A
- 正文引用上下文：✓

### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
- 真实性：✓
- 作者：✓
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (ICLR 2021)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding
- 真实性：✓
- 作者：✓
- 年份：✓ (2018)
- 标题：✓
- Venue：✓ (AAAI 2018)
- ID：N/A
- 正文引用上下文：✓

### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data
- 真实性：✓
- 作者：✓
- 年份：✓ (2020)
- 标题：✓
- Venue：✓ (ICLR 2020)
- ID：N/A
- 正文引用上下文：✓

### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (arXiv:2305.05176)
- ID：✓
- 正文引用上下文：✓

### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models
- 真实性：✓
- 作者：✗ 严重错误。bib 列 6 位作者，实际 13 位，且多人姓名错误：
  - "Anand, Prakhar" → 应为 **"Anand, Ankit"**
  - "Potdar, Srividya" → 应为 **"Potharaju, Srividya Pranavi"**
  - "Gupta, Swaroop" → 实际是两人：**"Mishra, Swaroop"** 和 **"Gupta, Aditya"**
  - **"Tandon, Niket"** 不在作者列表中
  - 遗漏：Pei Zhou, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam
  - 正确完整列表：Aggarwal, Pranjal; Madaan, Aman; Anand, Ankit; Potharaju, Srividya Pranavi; Mishra, Swaroop; Zhou, Pei; Gupta, Aditya; Rajagopal, Dheeraj; Kappaganthu, Karthik; Yang, Yiming; Upadhyay, Shyam; Faruqui, Manaal; Mausam
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (NeurIPS 2024)
- ID：N/A
- 正文引用上下文：✓

### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2024)
- 标题：✓ (大小写差异属 bib style 常规处理)
- Venue：✓ (ICML 2024)
- ID：N/A
- 正文引用上下文：✓

### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (ICML 2023)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety
- 真实性：✓
- 作者：⚠ 作者顺序错误。bib 为 Bonagiri, Nguyen, Plaut, Kumaraguru；实际应为 **Bonagiri, Kumaraguru, Nguyen, Plaut**
- 年份：✓ (2025)
- 标题：✓
- Venue：✓ (arXiv:2510.16492)
- ID：✓
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (EMNLP 2023)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know
- 真实性：✓
- 作者：✓ (多作者论文，列出部分代表性作者合理)
- 年份：✓ (2022)
- 标题：✓
- Venue：✓ (arXiv:2207.05221)
- ID：✓
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference
- 真实性：✓
- 作者：✓
- 年份：✓ (2020)
- 标题：✓
- Venue：✓ (ACL 2020)
- ID：N/A
- 正文引用上下文：✓

### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit
- 真实性：✓
- 作者：✓
- 年份：✓ (2020)
- 标题：✓
- Venue：✓ (NeurIPS 2020)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach
- 真实性：✓
- 作者：✓
- 年份：✓ (2015)
- 标题：✓
- Venue：✓ (NeurIPS 2015)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling
- 真实性：✓
- 作者：✓
- 年份：✓ (2015)
- 标题：✓
- Venue：✓ (AAAI 2015)
- ID：N/A
- 正文引用上下文：N/A (bib 中存在但未在正文中被引用)

---

## 附录：未被正文引用的 bib 条目

以下 bib 条目存在于 references.bib 中但未在任何 tex 文件中被 `\cite`/`\citep`/`\citet` 引用：

1. dagger-2011
2. toolkengpt-2023
3. moldovan2012safe
4. altman1999constrained
5. mihatsch2002risk
6. northcutt2021confident
7. li2020dividemix
8. gshard-2021
9. leviathan2023speculative
10. bonagiri2025check
11. manakul2023selfcheckgpt
12. kadavath2022language
13. zhou2020bert
14. chow2015risk
15. tamar2015optimizing
16. tot-2023

注意：这些条目可能在 appendix 或其他未检查的 tex 文件中被引用（当前检查范围：main.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex, responsibleNLPchecklist.tex）。
