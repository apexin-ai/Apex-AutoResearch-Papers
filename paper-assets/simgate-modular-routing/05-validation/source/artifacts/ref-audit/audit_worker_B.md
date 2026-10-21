# Reference Audit — Worker B

## 总结
- 总条目数：68
- ✓ 确认正确：58
- ✗ 发现问题：10

### 严重问题（作者错误/缺失）
| # | cite_key | 问题 |
|---|----------|------|
| 19 | amitai2024explaining | 第二作者 "Guy Septon" 应为 "Yael Septon" |
| 23 | reflexion-2023 | 缺少作者 Edward Berman |
| 33 | toolace-2025 | 第一作者 "Zhang, Weiwen" 应为 "Liu, Weiwen" |
| 46 | salt-2026 | 作者 "David Yan" 应为 "Qiaojing Yan" |
| 51 | agent-safetybench-2024 | 多个作者名错误，含两个不存在的作者 |
| 59 | automix-2024 | 严重作者列表错误：多个名字错误，缺少7位共同作者 |

### 轻微问题
| # | cite_key | 问题 |
|---|----------|------|
| 15 | dagger-2011 | 作者 "Drew Bagnell" 正式发表名为 "J. Andrew Bagnell" |
| 54 | switch-transformer-2022 | 页码 1-39 应为 1-40 |
| 62 | bonagiri2025check | 作者顺序错误（bib: Bonagiri/Nguyen/Plaut/Kumaraguru → arXiv: Bonagiri/Kumaraguru/Nguyen/Plaut） |

### Cite Key 不一致
| # | cite_key | 问题 |
|---|----------|------|
| 45 | axis-2026 | cite key 标 2026，但 year 字段和 arXiv 提交日期均为 2025 |

## 正文引用上下文核查
所有 \cite{} 引用在正文中的使用均与被引论文的实际内容一致，未发现张冠李戴的引用错误。

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
- 标题：✓ (BibTeX title casing vs arXiv lowercase — 非实质性差异)
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
- 作者：✓
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
- 标题：✓
- Venue：✓ (ACL 2026)
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
- 作者：✗ (第三作者 "Drew Bagnell" 正式发表名为 "J. Andrew Bagnell"。"Drew" 是常用昵称但非 AISTATS 论文集的正式署名)
- 年份：✓ (2011)
- 标题：✓
- Venue：✓ (AISTATS 2011)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

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
- Venue：✓ (JMLR vol 16)
- ID：N/A
- 正文引用上下文：✓

### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes
- 真实性：✓
- 作者：✗ (第二作者 "Guy Septon" 应为 **"Yael Septon"**)
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (AAAI 2024)
- ID：N/A
- 正文引用上下文：✓

### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents
- 真实性：✓ (AAMAS 2023 Doctoral Consortium 论文)
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (AAMAS 2023)
- ID：N/A
- 正文引用上下文：✓

### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (Artificial Intelligence, vol 295)
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
- 作者：✗ (缺少作者 **Edward Berman**。完整作者列表: Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao)
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
- 正文引用上下文：✓（在 Limitations 中提及）

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
- 作者：✓
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
- Venue：✓ (Review of Economics and Statistics, vol 90, no 3, pp 414-427)
- ID：N/A
- 正文引用上下文：✓

### 32. [achiam2017cpo] — Constrained Policy Optimization
- 真实性：✓
- 作者：✓
- 年份：✓ (2017)
- 标题：✓
- Venue：✓ (ICML 2017)
- ID：N/A
- 正文引用上下文：✓

### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling
- 真实性：✓
- 作者：✗ (第一作者 "Zhang, Weiwen" 应为 **"Liu, Weiwen"**（Weiwen Liu）。完整作者列表由 27 位作者组成，以 Weiwen Liu 为首)
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
- Venue：✓ (Canadian Journal of Economics, vol 56, no 3)
- ID：N/A
- 正文引用上下文：✓

### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes
- 真实性：✓
- 作者：✓
- 年份：✓ (2012)
- 标题：✓
- Venue：✓ (ICML 2012)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

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
- 作者：✓ (bib 用 "and others" 省略，首作者 Lee, Seanie 正确)
- 年份：✓ (2025)
- 标题：✓
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
- 正文引用上下文：✓（未在正文中直接引用）

### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2002)
- 标题：✓
- Venue：✓ (Machine Learning, vol 49)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

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
- Venue：✓ (arXiv:2506.02946)
- ID：✓
- 正文引用上下文：✓

### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents
- 真实性：✓
- 作者：✓
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv:2602.03412)
- ID：✓
- 正文引用上下文：✓

### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour
- 真实性：✓
- 作者：✓
- 年份：✓ (bib year 字段为 2025，正确；但 cite key "axis-2026" 暗示 2026，不一致)
- 标题：✓
- Venue：✓ (arXiv:2505.17801)
- ID：✓
- 正文引用上下文：✓
- 备注：cite key 与实际年份不一致（key 写 2026，实际为 2025）

### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph
- 真实性：✓
- 作者：✗ (第三作者 "David Yan" 应为 **"Qiaojing Yan"**，ACL Anthology 确认)
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (Findings of EACL 2026)
- ID：N/A
- 正文引用上下文：✓

### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size
- 真实性：✓
- 作者：✓
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
- Venue：✓ (JAIR, vol 70)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning
- 真实性：✓
- 作者：✓
- 年份：✓ (2020)
- 标题：✓
- Venue：✓ (ICLR 2020)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

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
- 作者：✗ (严重错误。bib 列出 9 位作者，但实际论文仅有 7 位。具体问题：(1) "Yang Junhao" 应为 **"Yang Junxiao"**；(2) "Wang Renhao" 应为 **"Wang Hongning"**；(3) "Liu Jie" 和 "Li Jiangjie" 在实际论文中不存在，为虚构作者。正确的完整作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang)
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
- Venue：✓ (Journal of Educational Psychology, vol 66, no 5)
- ID：N/A
- 正文引用上下文：✓

### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
- 真实性：✓
- 作者：✓
- 年份：✓ (2022)
- 标题：✓
- Venue：✗ (页码错误：bib 写 pages={1--39}，JMLR 论文实际为 **1--40**)
- ID：N/A
- 正文引用上下文：✓

### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
- 真实性：✓
- 作者：✓
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (ICLR 2021)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

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
- 作者：✗ (严重错误。bib 列出 6 位作者，但 NeurIPS 2024 论文实际有 13 位作者。具体问题：(1) "Anand, Prakhar" 应为 **"Anand, Ankit"**；(2) "Potdar, Srividya" 应为 **"Potharaju, Srividya Pranavi"**；(3) "Gupta, Swaroop" 应为 **"Mishra, Swaroop"**；(4) "Tandon, Niket" 不在论文作者列表中；(5) 缺少 7 位共同作者：Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam)
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (NeurIPS 2024)
- ID：N/A
- 正文引用上下文：✓

### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2024)
- 标题：✓
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
- 正文引用上下文：✓（未在正文中直接引用）

### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety
- 真实性：✓
- 作者：✗ (作者顺序错误。bib: Bonagiri, Nguyen, Plaut, Kumaraguru → arXiv 实际顺序: **Bonagiri, Kumaraguru, Nguyen, Plaut**)
- 年份：✓ (2025)
- 标题：✓
- Venue：✓ (arXiv:2510.16492)
- ID：✓
- 正文引用上下文：✓（未在正文中直接引用）

### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models
- 真实性：✓
- 作者：✓
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (EMNLP 2023)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know
- 真实性：✓
- 作者：✓
- 年份：✓ (2022)
- 标题：✓
- Venue：✓ (arXiv:2207.05221)
- ID：✓
- 正文引用上下文：✓（未在正文中直接引用）

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
- 正文引用上下文：✓（未在正文中直接引用）

### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach
- 真实性：✓
- 作者：✓
- 年份：✓ (2015)
- 标题：✓
- Venue：✓ (NeurIPS 2015)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）

### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling
- 真实性：✓
- 作者：✓
- 年份：✓ (2015)
- 标题：✓
- Venue：✓ (AAAI 2015)
- ID：N/A
- 正文引用上下文：✓（未在正文中直接引用）
