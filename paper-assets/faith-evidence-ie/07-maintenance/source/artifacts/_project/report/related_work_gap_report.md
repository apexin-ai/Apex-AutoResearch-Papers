# Related Work Gap Report — Dream v2 审稿缺口补全

生成日期：2026-05-15

---

## 1. R1-RE

- **论文标题**: R1-RE: Cross-Domain Relation Extraction with RLVR
- **作者**: Runpeng Dai, Tong Zheng, Run Yang, Kaixian Yu, Hongtu Zhu
- **Venue/年份**: arXiv preprint, July 2025
- **URL**: https://arxiv.org/abs/2507.04642
- **Category**: ie_method / rl_training
- **Role**: direct-competitor

**Key Finding**: 首个将 RLVR（Reinforcement Learning with Verifiable Reward）应用于关系抽取的框架。将 RE 重新定义为推理任务，以标注指南为导向引导 LLM 的多步推理。使用 GRPO 算法和 rule-based reward（类似 DeepSeek-R1-Zero 和 Logic-R1），R1-RE-7B 在 OOD 设置下达到约 70% 准确率，与 GPT-4o 持平。

**Relevance**: 与 FREIGE 高度相关——同样使用 GRPO 做 RE/IE，但 R1-RE 聚焦 cross-domain generalization，而 FREIGE 聚焦 evidence grounding 和 faithfulness。两者形成互补视角：R1-RE 证明 RLVR+GRPO 在 RE 上可行，FREIGE 则深入分析 QLoRA-specific GRPO 行为和 evidence extraction decoupling。需在 related work 中作为最直接的 concurrent work 讨论。

---

## 2. RelPrior

- **论文标题**: Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction
- **作者**: Qiankun Pi et al.
- **Venue/年份**: arXiv preprint, November 2025
- **URL**: https://arxiv.org/abs/2511.08143
- **Category**: docre_method
- **Role**: direct-competitor

**Key Finding**: 提出 "Relation as a Prior" 范式：先用二分类 LLM 判断实体对是否有关系（过滤噪声），再用预定义 relation 匹配实体对（避免关系误判）。在 DocRED 上比 AutoRE_LLaMA3-8B 的 F1 提升 2.06%（dev）和 2.38%（test），达到 LLM-based DocRE SOTA。

**Relevance**: RelPrior 是 LLM-based DocRE 的最新 SOTA，其两阶段过滤策略（binary filtering + relation matching）与 FREIGE 的 evidence-grounded 方法形成对比。RelPrior 解决的是实体对噪声问题，FREIGE 解决的是 evidence grounding 问题——两者关注 DocRE 的不同瓶颈。应在 related work 中作为 LLM-based DocRE 方法的代表讨论。

---

## 3. Ru-LLM

- **论文标题**: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction
- **作者**: Kunli Zhang, Pengcheng Wu, Bohan Yu, Yunlong Li, Dezhi Kong, Hongying Zan, Min Peng, Yu Song
- **Venue/年份**: NLPCC 2025, Springer
- **URL**: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11
- **Category**: docre_method
- **Role**: direct-competitor

**Key Finding**: 提出 Ru-LLM 框架，通过频繁模式挖掘和 LLM 辅助补全获取候选谓词池，用 Monte Carlo Tree Search（MCTS）搜索生成逻辑规则，将规则转化为 prompt 引导 LLM 生成初始结果，再通过 Chain-of-Thought 验证过滤不满足规则的三元组。在 DWIE、DocRED、Re-DocRED 三个数据集上超越现有 implicit reasoning、LLM-based 和 rule-based 方法。

**Relevance**: Ru-LLM 代表了 rule-constrained LLM for DocRE 的路线，与 FREIGE 的 RL-based 方法形成方法论对比。Ru-LLM 用显式逻辑规则约束 LLM 输出，FREIGE 用 GRPO reward 隐式引导 evidence grounding。可在 related work 中讨论 explicit rule vs. implicit RL reward 的 trade-off。

---

## 4. AutoRE

- **论文标题**: AutoRE: Document-Level Relation Extraction with Large Language Models
- **作者**: Lilong Xue, Dan Zhang, Yuxiao Dong, Jie Tang
- **Venue/年份**: ACL 2024 System Demonstrations
- **URL**: https://arxiv.org/abs/2403.14888 / https://aclanthology.org/2024.acl-demos.20/
- **Category**: docre_method
- **Role**: direct-competitor

**Key Finding**: 提出 RHF（Relation-Head-Facts）三阶段抽取范式，不依赖已知关系选项，更贴近真实场景。使用 QLoRA 微调 Mistral-7B，三个独立 QLoRA 模块分别负责关系抽取、头实体识别和三元组事实抽取。在 Re-DocRED 上超越 TAG 方法 10.03%（dev）和 9.03%（test）。

**Relevance**: AutoRE 与 FREIGE 共享多个技术特征：QLoRA 微调、LLM-based DocRE、模块化抽取。AutoRE 是 RelPrior 的直接 baseline（被 RelPrior 超越）。FREIGE 可与 AutoRE 对比：AutoRE 是纯 SFT/QLoRA，FREIGE 在此基础上加入 GRPO 强化学习和 evidence grounding。AutoRE 是 related work 中必须引用的 LLM-based DocRE baseline。

---

## 5. GLiDRE

- **论文标题**: GLiDRE: Generalist Lightweight model for Document-level Relation Extraction
- **作者**: Robin Armingaud, Romaric Besançon
- **Venue/年份**: arXiv preprint, August 2025（CEA-List, France）
- **URL**: https://arxiv.org/abs/2508.00757
- **Category**: docre_method
- **Role**: related_method

**Key Finding**: 基于 GLiNER 构建的轻量级 DocRE 模型，采用 dual-encoder 架构（text encoder + label encoder），支持 zero-shot 和 few-shot 关系分类。在低资源和 few-shot meta-learning 基准上超越现有方法，在 few-shot DocRE 上达到 SOTA。

**Relevance**: GLiDRE 代表了非 LLM generative 的 DocRE 路线（encoder-based，非 decoder-based），与 FREIGE 的 LLM-based generative 方法形成架构对比。GLiDRE 聚焦 data-constrained 场景（zero/few-shot），FREIGE 聚焦 evidence-grounded 全监督/RL 训练场景。在 related work 中可作为 non-generative DocRE 方法的代表简要提及。

---

## 6. INFUSE (InFusE)

- **论文标题**: Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks
- **作者**: Huajian Zhang, Yumo Xu, Laura Perez-Beltrachini
- **Venue/年份**: arXiv preprint, February 2024（University of Edinburgh）
- **URL**: https://arxiv.org/abs/2402.17630
- **Category**: evaluation
- **Role**: evaluation

**Key Finding**: 提出 InFusE，一种增量式 NLI-based faithfulness 评估方法。通过逐步扩展 context（添加 document sentences）评估 summary 的忠实性，同时通过 sentence simplification 分解 summary 句子进行细粒度分析。引入 DiverSumm 基准，涵盖长文档摘要、会议摘要和多文档摘要等多样化任务。

**Relevance**: InFusE 的 NLI-based faithfulness evaluation 与 FREIGE 的 EDCR 诊断指标在精神上相关——两者都关注 output 是否 faithful to evidence/source。InFusE 评估 summarization faithfulness，EDCR 评估 RE 中的 evidence consistency。可在 related work 的 evaluation metrics 部分讨论，作为 faithfulness evaluation 的相关工作。

---

## 7. TRUE

- **论文标题**: TRUE: Re-evaluating Factual Consistency Evaluation
- **作者**: Or Honovich, Roee Aharoni, Jonathan Herzig, Hagai Taitelbaum, Doron Kukliansky, Vered Cohen, Thomas Scialom, Idan Szpektor, Avinatan Hassidim, Yossi Matias
- **Venue/年份**: NAACL 2022（Google Research）
- **URL**: https://arxiv.org/abs/2204.04991 / https://aclanthology.org/2022.naacl-main.287/
- **Category**: evaluation
- **Role**: evaluation / background

**Key Finding**: 对 factual consistency metrics 进行全面标准化评估，覆盖 11 个数据集和多种 SOTA 指标。发现 large-scale NLI 和 QG-QA-based 方法取得了强且互补的结果。提出 example-level meta-evaluation protocol，比之前的相关性报告更具可操作性和可解释性。

**Relevance**: TRUE 建立了 factual consistency evaluation 的标准化框架，与 FREIGE 的 EDCR 指标在评估 faithfulness/factual consistency 方面有概念关联。TRUE 聚焦 NLG 通用 faithfulness，EDCR 聚焦 RE-specific evidence consistency。在 related work 中可作为 faithfulness evaluation 的经典工作引用，说明 EDCR 是将 faithfulness evaluation 思想引入 RE 领域的尝试。

---

## 总结

| 方法 | Category | Role | 与 FREIGE 关系 |
|------|----------|------|----------------|
| R1-RE | ie_method / rl_training | direct-competitor | 同用 GRPO 做 RE，最直接 concurrent work |
| RelPrior | docre_method | direct-competitor | LLM-based DocRE SOTA，解决实体对噪声 |
| Ru-LLM | docre_method | direct-competitor | Rule-constrained LLM for DocRE，explicit rule vs. implicit RL |
| AutoRE | docre_method | direct-competitor | QLoRA + LLM DocRE baseline，被 RelPrior 超越 |
| GLiDRE | docre_method | related_method | Encoder-based zero/few-shot DocRE，非 generative |
| InFusE | evaluation | evaluation | NLI-based faithfulness evaluation，与 EDCR 概念相关 |
| TRUE | evaluation | background | Factual consistency evaluation 经典框架 |
