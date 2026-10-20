# 引用核对清单 — Worker 1

总计: 52 条引用, 9 条有问题 (另有 17 条未在正文中引用)

**所有 52 篇论文均真实存在，无虚构引用。**

## 问题汇总

### 高严重性
| # | cite_key | 问题 |
|---|----------|------|
| 1 | wang2025relprior | 标题错误：bib 写 "RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction"，实际标题是 "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction" |
| 2 | tang2025rsftppo | 缺少 2 位作者：Shaan Ul Haque 和 Nithish Kannen（实际 6 人，bib 只列 4 人） |

### 中严重性
| # | cite_key | 问题 |
|---|----------|------|
| 3 | li2026qurl | Venue 过时：bib 写 "arXiv preprint"，实际已被 ICLR 2026 接收发表 |
| 4 | wang2025rullm | 标题添加了不存在的 "Ru-LLM:" 前缀；entry type 应从 @article 改为 @inproceedings |
| 5 | gulcehre2023rest | 格式错误：使用 @inproceedings 但 booktitle 是 "arXiv preprint"，应改为 @article |
| 6 | ma2023dreeam | Venue 可能不准确：bib 写 "Findings of EACL 2023"，ACL Anthology 路径 2023.eacl-main.145 表明是 EACL 2023 main，非 Findings |

### 低严重性（命名/格式）
| # | cite_key | 问题 |
|---|----------|------|
| 7 | xu2024lmrc | cite key "xu" 但第一作者是 Li；标题添加了 "LMRC:" 前缀（arXiv 原标题无此前缀） |
| 8 | ito2025mogrpo | cite key "ito" 但第一作者是 Ichihara |
| 9 | liu2026gdpo | 标题大小写微差：bib "Reward-Decoupled" / "Multi-Reward"，arXiv 用 "reward-Decoupled" / "Multi-reward" |

### cite key 与第一作者不匹配（不影响渲染，仅供参考）
| cite_key | key 姓氏 | 实际第一作者 |
|----------|----------|-------------|
| wang2025rear | wang | Luo, Jianwen |
| wang2025relprior | wang | Pi, Qiankun |
| zhang2025glidre | zhang | Armingaud, Robin |
| tang2025rsftppo | tang | Anil, Gautham Govind |
| wang2025rullm | wang | Zhang, Kunli |
| xu2024lmrc | xu | Li, Xingzuo |
| ito2025mogrpo | ito | Ichihara, Yuki |

### 未在正文引用的 bib 条目（17 条）
moskovitz2024constrained, dong2023raft, ito2025mogrpo, li2025drift, liu2026gdpo, zhang2025glidre, wang2025rullm, standley2020tasks, yu2020gradient, wang2023selfconsistency, ethayarajh2024kto, coste2024reward, hoffmann2022chinchilla, liu2026rift, deng2026trajfusion, tian2026mugrpo, ji2026treegrpo

---

## 逐条结果

### 1. [autore2024] — ✓
- 真实性: ✓
- 作者: ✓ (Xue, Lilong and Zhang, Dan and Dong, Yuxiao and Tang, Jie)
- 年份: ✓ (2024)
- 标题: ✓ ("AutoRE: Document-Level Relation Extraction with Large Language Models")
- Venue: ✓ (ACL 2024 System Demonstrations)
- arXiv ID: ✓ (2403.14888)
- 正文用法: ✓ (introduction: "fine-tune LLMs with structured decomposition")
- 备注: 无问题

### 2. [xu2025docksrag] — ✓
- 真实性: ✓
- 作者: ✓ (Xu, Xiaolong et al.)
- 年份: ✓ (2025)
- 标题: ✓ ("DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning")
- Venue: ✓ (ICML 2025)
- arXiv ID: N/A
- 正文用法: ✓ (introduction: "combine retrieval-augmented generation with structured knowledge")
- 备注: 无问题

### 3. [dai2025r1re] — ✓
- 真实性: ✓
- 作者: ✓ (Dai, Runpeng et al.)
- 年份: ✓ (2025)
- 标题: ✓ ("R1-RE: Cross-Domain Relation Extraction with RLVR")
- Venue: ✓ (arXiv preprint arXiv:2507.04642)
- arXiv ID: ✓ (2507.04642)
- 正文用法: ✓ (related_work: "applications to structured IE include R1-RE")
- 备注: 无问题

### 4. [gao2023scaling] — ✓
- 真实性: ✓
- 作者: ✓ (Gao, Leo and Schulman, John and Hilton, Jacob)
- 年份: ✓ (2023)
- 标题: ✓ ("Scaling Laws for Reward Model Overoptimization")
- Venue: ✓ (ICML 2023)
- arXiv ID: ✓ (2210.10760)
- 正文用法: ✓ (spectrum section: "the reward signal preferentially optimizes the easier sub-task")
- 备注: 无问题

### 5. [hu2022lora] — ✓
- 真实性: ✓
- 作者: ✓ (Hu, Edward J. et al.)
- 年份: ✓ (2022)
- 标题: ✓ ("LoRA: Low-Rank Adaptation of Large Language Models")
- Venue: ✓ (ICLR 2022)
- arXiv ID: ✓ (2106.09685)
- 正文用法: ✓ (method: "Low-Rank Adaptation (LoRA)")
- 备注: 无问题

### 6. [li2026qurl] — ✗
- 真实性: ✓
- 作者: ✓ (Li, Yuhang et al.)
- 年份: ✓ (2026)
- 标题: ✓ ("QuRL: Efficient Reinforcement Learning with Quantized Rollout")
- Venue: ✗ (bib 写 "arXiv preprint"，实际已发表于 ICLR 2026)
- arXiv ID: ✓ (2602.13953)
- 正文用法: ✓ (spectrum: "resembling the quantized-actor divergence")
- 备注: 需更新 venue 为 ICLR 2026，entry type 改为 @inproceedings

### 7. [laban2022summac] — ✓
- 真实性: ✓
- 作者: ✓ (Laban, Philippe et al.)
- 年份: ✓ (2022)
- 标题: ✓ ("SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization")
- Venue: ✓ (TACL, vol 10, pp 163-177)
- arXiv ID: N/A
- 正文用法: ✓ (related_work: "NLI-based faithfulness evaluation")
- 备注: 无问题

### 8. [li2025srvf] — ✓
- 真实性: ✓
- 作者: ✓ (Li, Yongqi et al.)
- 年份: ✓ (2025)
- 标题: ✓ ("Enhancing Relation Extraction via Supervised Rationale Verification and Feedback")
- Venue: ✓ (AAAI 2025)
- arXiv ID: ✓ (2412.07289)
- 正文用法: ✓ (related_work: "reward-based evidence grounding")
- 备注: 无问题

### 9. [jin2025rl_panacea] — ✓
- 真实性: ✓
- 作者: ✓ (Jin, Hangzhan et al.)
- 年份: ✓ (2025)
- 标题: ✓ ("RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs")
- Venue: ✓ (arXiv preprint arXiv:2508.16546)
- arXiv ID: ✓ (2508.16546)
- 正文用法: ✓ (related_work: "catastrophic forgetting in RL alignment")
- 备注: 无问题

### 10. [ma2023dreeam] — ✗
- 真实性: ✓
- 作者: ✓ (Ma, Youmi and Wang, An and Okazaki, Naoaki)
- 年份: ✓ (2023)
- 标题: ✓ ("DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction")
- Venue: ✗ (bib 写 "Findings of EACL 2023"，ACL Anthology 路径 2023.eacl-main.145 表明是 EACL 2023 main conference)
- arXiv ID: ✓ (2302.08675)
- 正文用法: ✓ (introduction/method: evidence retrieval through memory attention)
- 备注: 建议将 venue 从 "Findings of EACL 2023" 改为 "Proceedings of EACL 2023"

### 11. [moskovitz2024constrained] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Moskovitz, Ted et al.)
- 年份: ✓ (2024)
- 标题: ✓ ("Confronting Reward Model Overoptimization with Constrained RLHF")
- Venue: ✓ (ICLR 2024)
- arXiv ID: N/A
- 正文用法: N/A (未在正文中引用)
- 备注: bib 中存在但未被 \cite，可考虑删除

### 12. [rafailov2023direct] — ✓
- 真实性: ✓
- 作者: ✓ (Rafailov, Rafael et al.)
- 年份: ✓ (2023)
- 标题: ✓ ("Direct Preference Optimization: Your Language Model is Secretly a Reward Model")
- Venue: ✓ (NeurIPS 2023)
- arXiv ID: ✓ (2305.18290)
- 正文用法: ✓ (introduction/method/related_work: DPO)
- 备注: 无问题

### 13. [shao2024deepseekmath] — ✓
- 真实性: ✓
- 作者: ✓ (Shao, Zhihong et al.)
- 年份: ✓ (2024)
- 标题: ✓ ("DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models")
- Venue: ✓ (arXiv preprint arXiv:2402.03300)
- arXiv ID: ✓ (2402.03300)
- 正文用法: ✓ (introduction/method/related_work: GRPO)
- 备注: 无问题

### 14. [tan2022redocred] — ✓
- 真实性: ✓
- 作者: ✓ (Tan, Qingyu et al.)
- 年份: ✓ (2022)
- 标题: ✓ ("Revisiting DocRED: Addressing the False Negative Problem in Relation Extraction")
- Venue: ✓ (EMNLP 2022)
- arXiv ID: N/A
- 正文用法: ✓ (introduction/experiments: Re-DocRED dataset)
- 备注: 无问题

### 15. [xiao2022sais] — ✓
- 真实性: ✓
- 作者: ✓ (Xiao, Yuxin et al.)
- 年份: ✓ (2022)
- 标题: ✓ ("SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction")
- Venue: ✓ (NAACL 2022)
- arXiv ID: N/A
- 正文用法: ✓ (introduction/method/related_work: evidence supervision)
- 备注: 无问题

### 16. [xie2022eider] — ✓
- 真实性: ✓
- 作者: ✓ (Xie, Yiqing et al.)
- 年份: ✓ (2022)
- 标题: ✓ ("EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion")
- Venue: ✓ (Findings of ACL 2022)
- arXiv ID: ✓ (2106.08657)
- 正文用法: ✓ (related_work: "fuses evidence into the relation classifier")
- 备注: 无问题

### 17. [xu2024lmrc] — ✗
- 真实性: ✓
- 作者: ✓ (Li, Xingzuo and Chen, Kehai and Long, Yunfei and Zhang, Min — bib 内容正确)
- 年份: ✓ (2024)
- 标题: ✗ (arXiv 原标题 "LLM with Relation Classifier for Document-Level Relation Extraction"，bib 添加了 "LMRC:" 前缀)
- Venue: ✓ (arXiv preprint arXiv:2408.13889)
- arXiv ID: ✓ (2408.13889)
- 正文用法: ✓ (introduction: "frame it as multi-choice reading comprehension")
- 备注: cite key "xu2024" 但第一作者是 Li；标题 "LMRC:" 前缀为添加

### 18. [yao2019docred] — ✓
- 真实性: ✓
- 作者: ✓ (Yao, Yuan et al.)
- 年份: ✓ (2019)
- 标题: ✓ ("DocRED: A Large-Scale Document-Level Relation Extraction Dataset")
- Venue: ✓ (ACL 2019)
- arXiv ID: N/A
- 正文用法: ✓ (introduction/experiments: DocRED dataset)
- 备注: 无问题

### 19. [zelikman2022star] — ✓
- 真实性: ✓
- 作者: ✓ (Zelikman, Eric et al.)
- 年份: ✓ (2022)
- 标题: ✓ ("STaR: Bootstrapping Reasoning With Reasoning")
- Venue: ✓ (NeurIPS 2022)
- arXiv ID: ✓ (2203.14465)
- 正文用法: ✓ (introduction/method/related_work: STaR iterative self-improvement)
- 备注: 无问题

### 20. [dong2023raft] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Dong, Hanze et al.)
- 年份: ✓ (2023)
- 标题: ✓ ("RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment")
- Venue: ✓ (TMLR)
- arXiv ID: ✓ (2304.06767)
- 正文用法: N/A (未在正文中引用)
- 备注: bib 中存在但未被 \cite，可考虑删除

### 21. [ito2025mogrpo] — ✗ (未引用)
- 真实性: ✓
- 作者: ✓ (Ichihara, Yuki et al. — bib 内容正确)
- 年份: ✓ (2025)
- 标题: ✓ ("MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems")
- Venue: ✓ (arXiv preprint arXiv:2509.22047)
- arXiv ID: ✓ (2509.22047)
- 正文用法: N/A (未在正文中引用)
- 备注: cite key "ito2025" 但第一作者是 Ichihara；未被引用，可考虑删除

### 22. [li2025drift] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Li, Jiazheng et al.)
- 年份: ✓ (2025)
- 标题: ✓ ("Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference")
- Venue: ✓ (ACL 2025)
- arXiv ID: N/A
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 23. [liu2026gdpo] — ✗ (未引用)
- 真实性: ✓
- 作者: ✓ (Liu, Shih-Yang et al.)
- 年份: ✓ (2026)
- 标题: ✗ (大小写微差：bib "Reward-Decoupled" / "Multi-Reward"，arXiv 用 "reward-Decoupled" / "Multi-reward")
- Venue: ✓ (arXiv preprint arXiv:2601.05242)
- arXiv ID: ✓ (2601.05242)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 24. [liu2025drgrpo] — ✓
- 真实性: ✓
- 作者: ✓ (Liu, Zichen et al.)
- 年份: ✓ (2025)
- 标题: ✓ ("Understanding R1-Zero-Like Training: A Critical Perspective")
- Venue: ✓ (Conference on Language Modeling / COLM 2025)
- arXiv ID: ✓ (2503.20783)
- 正文用法: ✓ (related_work: "length bias")
- 备注: 无问题

### 25. [yu2025dapo] — ✓
- 真实性: ✓
- 作者: ✓ (Yu, Qiying et al.)
- 年份: ✓ (2025)
- 标题: ✓ ("DAPO: An Open-Source LLM Reinforcement Learning System at Scale")
- Venue: ✓ (arXiv preprint arXiv:2503.14476)
- arXiv ID: ✓ (2503.14476)
- 正文用法: ✓ (related_work: "entropy collapse")
- 备注: 无问题

### 26. [zhang2024infuse] — ✓
- 真实性: ✓
- 作者: ✓ (Zhang, Huajian et al.)
- 年份: ✓ (2024)
- 标题: ✓ ("Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks")
- Venue: ✓ (EACL 2024)
- arXiv ID: N/A
- 正文用法: ✓ (related_work: "NLI-based faithfulness evaluation")
- 备注: 无问题

### 27. [wang2025rear] — ✓ (cite key 不匹配)
- 真实性: ✓
- 作者: ✓ (Luo, Jianwen and Hong, Yu and Yang, Shuai and Yao, Jianmin)
- 年份: ✓ (2025)
- 标题: ✓ ("REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support")
- Venue: ✓ (Findings of EMNLP 2025)
- arXiv ID: N/A
- 正文用法: ✓ (related_work: "applications to structured IE include ... REAR")
- 备注: cite key "wang2025" 但第一作者是 Luo。注意 REAR 是 Event Argument Extraction 方法，正文称其为 "structured IE" 应用，用法基本合理

### 28. [wang2025relprior] — ✗
- 真实性: ✓
- 作者: ✓ (Pi, Qiankun et al. — bib 内容正确)
- 年份: ✓ (2025)
- 标题: ✗ (bib: "RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction"; 实际 arXiv 标题: "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction")
- Venue: ✓ (arXiv preprint arXiv:2511.08143)
- arXiv ID: ✓ (2511.08143)
- 正文用法: ✓ (related_work: "RelPrior leverages relation priors"; 脚注引用了其 LLaMA3-8B 复现数据)
- 备注: cite key "wang2025" 但第一作者是 Pi；标题被修改（添加 "RelPrior:" 前缀、改写措辞）

### 29. [zhang2025glidre] — ✓ (未引用, cite key 不匹配)
- 真实性: ✓
- 作者: ✓ (Armingaud, Robin and Besançon, Romaric)
- 年份: ✓ (2025)
- 标题: ✓ (大小写微差可忽略)
- Venue: ✓ (arXiv preprint arXiv:2508.00757)
- arXiv ID: ✓ (2508.00757)
- 正文用法: N/A (未在正文中引用)
- 备注: cite key "zhang2025" 但作者是 Armingaud/Besançon；未被引用，可考虑删除

### 30. [tang2025rsftppo] — ✗
- 真实性: ✓
- 作者: ✗ (缺少 2 位作者：Shaan Ul Haque 和 Nithish Kannen。实际 6 人，bib 只列 4 人)
- 年份: ✓ (2025)
- 标题: ✓ ("Rejection Sampling Based Fine Tuning Secretly Performs PPO")
- Venue: ✓ (ICML 2025 Workshop PUT)
- arXiv ID: N/A
- 正文用法: ✓ (related_work: "theoretical connections to PPO")
- 备注: cite key "tang2025" 但第一作者是 Anil；作者列表不完整

### 31. [wang2025rullm] — ✗ (未引用)
- 真实性: ✓
- 作者: ✓ (Zhang, Kunli et al. — bib 内容正确)
- 年份: ✓ (2025)
- 标题: ✗ (bib 添加了 "Ru-LLM:" 前缀，Springer 出版物标题无此前缀)
- Venue: ✓ (NLPCC 2025)
- arXiv ID: N/A
- 正文用法: N/A (未在正文中引用)
- 备注: cite key "wang2025" 但第一作者是 Zhang；entry type @article 应为 @inproceedings；未被引用，可考虑删除

### 32. [zhou2021atlop] — ✓
- 真实性: ✓
- 作者: ✓ (Zhou, Wenxuan et al.)
- 年份: ✓ (2021)
- 标题: ✓ ("Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling")
- Venue: ✓ (AAAI 2021)
- arXiv ID: ✓ (2010.11304)
- 正文用法: ✓ (introduction/related_work: ATLOP encoder baseline)
- 备注: 无问题

### 33. [ruder2017overview] — ✓
- 真实性: ✓
- 作者: ✓ (Ruder, Sebastian)
- 年份: ✓ (2017)
- 标题: ✓ ("An Overview of Multi-Task Learning in Deep Neural Networks")
- Venue: ✓ (arXiv preprint arXiv:1706.05098)
- arXiv ID: ✓ (1706.05098)
- 正文用法: ✓ (related_work: "negative transfer in multi-task learning")
- 备注: 无问题

### 34. [standley2020tasks] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Standley, Trevor et al.)
- 年份: ✓ (2020)
- 标题: ✓ ("Which Tasks Should Be Learned Together in Multi-task Learning?")
- Venue: ✓ (ICML 2020)
- arXiv ID: N/A
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 35. [yu2020gradient] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Yu, Tianhe et al.)
- 年份: ✓ (2020)
- 标题: ✓ ("Gradient Surgery for Multi-Task Learning")
- Venue: ✓ (NeurIPS 2020)
- arXiv ID: ✓ (2001.06782)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 36. [wang2023selfconsistency] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Wang, Xuezhi et al.)
- 年份: ✓ (2023)
- 标题: ✓ ("Self-Consistency Improves Chain of Thought Reasoning in Language Models")
- Venue: ✓ (ICLR 2023)
- arXiv ID: ✓ (2203.11171)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 37. [ouyang2022instructgpt] — ✓
- 真实性: ✓
- 作者: ✓ (Ouyang, Long et al.)
- 年份: ✓ (2022)
- 标题: ✓ ("Training Language Models to Follow Instructions with Human Feedback")
- Venue: ✓ (NeurIPS 2022)
- arXiv ID: ✓ (2203.02155)
- 正文用法: ✓ (related_work/method: RLHF)
- 备注: 无问题

### 38. [schulman2017ppo] — ✓
- 真实性: ✓
- 作者: ✓ (Schulman, John et al.)
- 年份: ✓ (2017)
- 标题: ✓ ("Proximal Policy Optimization Algorithms")
- Venue: ✓ (arXiv preprint arXiv:1707.06347)
- arXiv ID: ✓ (1707.06347)
- 正文用法: ✓ (related_work: PPO)
- 备注: 无问题

### 39. [zeng2020gain] — ✓
- 真实性: ✓
- 作者: ✓ (Zeng, Shuang et al.)
- 年份: ✓ (2020)
- 标题: ✓ ("Double Graph Based Reasoning for Document-level Relation Extraction")
- Venue: ✓ (EMNLP 2020)
- arXiv ID: N/A
- 正文用法: ✓ (related_work: "GAIN modeling inter-sentence reasoning")
- 备注: 无问题

### 40. [ethayarajh2024kto] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Ethayarajh, Kawin et al.)
- 年份: ✓ (2024)
- 标题: ✓ ("KTO: Model Alignment as Prospect Theoretic Optimization")
- Venue: ✓ (ICML 2024)
- arXiv ID: ✓ (2402.01306)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 41. [coste2024reward] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Coste, Thomas et al.)
- 年份: ✓ (2024)
- 标题: ✓ ("Reward Model Ensembles Help Mitigate Overoptimization")
- Venue: ✓ (ICLR 2024)
- arXiv ID: ✓ (2310.02743)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 42. [he2023debertav3] — ✓
- 真实性: ✓
- 作者: ✓ (He, Pengcheng et al.)
- 年份: ✓ (2023)
- 标题: ✓ ("DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing")
- Venue: ✓ (ICLR 2023)
- arXiv ID: ✓ (2111.09543)
- 正文用法: ✓ (method: NLI model for CED scoring)
- 备注: 无问题

### 43. [dettmers2023qlora] — ✓
- 真实性: ✓
- 作者: ✓ (Dettmers, Tim et al.)
- 年份: ✓ (2023)
- 标题: ✓ ("QLoRA: Efficient Finetuning of Quantized LLMs")
- Venue: ✓ (NeurIPS 2023)
- arXiv ID: ✓ (2305.14314)
- 正文用法: ✓ (related_work/method: QLoRA quantization)
- 备注: 无问题

### 44. [hoffmann2022chinchilla] — ✓ (未引用)
- 真实性: ✓
- 作者: ✓ (Hoffmann, Jordan et al.)
- 年份: ✓ (2022)
- 标题: ✓ ("Training Compute-Optimal Large Language Models")
- Venue: ✓ (NeurIPS 2022)
- arXiv ID: ✓ (2203.15556)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 45. [yuan2023rft] — ✓
- 真实性: ✓
- 作者: ✓ (Yuan, Zheng et al.)
- 年份: ✓ (2023)
- 标题: ✓ ("Scaling Relationship on Learning Mathematical Reasoning with Large Language Models")
- Venue: ✓ (arXiv preprint arXiv:2308.01825)
- arXiv ID: ✓ (2308.01825)
- 正文用法: ✓ (related_work: "subsequent scaling analyses")
- 备注: 无问题

### 46. [tamo2026evidencerl] — ✓
- 真实性: ✓ (2026年3月提交，Georgia Tech / Peking University)
- 作者: ✓ (Tamo, J. Ben et al.)
- 年份: ✓ (2026)
- 标题: ✓ ("EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models")
- Venue: ✓ (arXiv preprint arXiv:2603.19532)
- arXiv ID: ✓ (2603.19532)
- 正文用法: ✓ (related_work: "reward-based evidence grounding")
- 备注: 非伪造，论文确实存在

### 47. [liu2026rift] — ✓ (未引用)
- 真实性: ✓ (2026年1月提交)
- 作者: ✓ (Liu, Zehua et al.)
- 年份: ✓ (2026)
- 标题: ✓ ("RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning")
- Venue: ✓ (arXiv preprint arXiv:2601.09253)
- arXiv ID: ✓ (2601.09253)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 48. [deng2026trajfusion] — ✓ (未引用)
- 真实性: ✓ (2026年2月提交)
- 作者: ✓ (Deng, Jie et al.)
- 年份: ✓ (2026)
- 标题: ✓ ("Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning")
- Venue: ✓ (arXiv preprint arXiv:2602.04391)
- arXiv ID: ✓ (2602.04391)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 49. [tian2026mugrpo] — ✓ (未引用)
- 真实性: ✓ (2026年5月提交，Rice University)
- 作者: ✓ (Tian, Minghao et al.)
- 年份: ✓ (2026)
- 标题: ✓ (μ vs Mu 为风格差异，非实质错误)
- Venue: ✓ (arXiv preprint arXiv:2605.17570)
- arXiv ID: ✓ (2605.17570)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 50. [ji2026treegrpo] — ✓ (未引用)
- 真实性: ✓ (2025年9月提交，ICLR 2026 接收)
- 作者: ✓ (Ji, Yuxiang et al.)
- 年份: ✓ (2026)
- 标题: ✓ ("Tree Search for LLM Agent Reinforcement Learning")
- Venue: ✓ (ICLR 2026)
- arXiv ID: ✓ (2509.21240)
- 正文用法: N/A (未在正文中引用)
- 备注: 未被引用，可考虑删除

### 51. [deepseek2025r1] — ✓
- 真实性: ✓
- 作者: ✓ (DeepSeek-AI)
- 年份: ✓ (2025)
- 标题: ✓ ("DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning")
- Venue: ✓ (arXiv preprint arXiv:2501.12948)
- arXiv ID: ✓ (2501.12948)
- 正文用法: ✓ (related_work: "demonstrates its effectiveness at scale")
- 备注: 无问题

### 52. [gulcehre2023rest] — ✗
- 真实性: ✓
- 作者: ✓ (Gulcehre, Caglar et al.)
- 年份: ✓ (2023)
- 标题: ✓ ("Reinforced Self-Training (ReST) for Language Modeling")
- Venue: ✓ (arXiv preprint — 未被正式会议接收)
- arXiv ID: ✓ (2308.08998)
- 正文用法: ✓ (related_work: "subsequent scaling analyses")
- 备注: **格式错误**——使用 @inproceedings 但 booktitle 是 "arXiv preprint arXiv:2308.08998"，应改为 @article 类型
