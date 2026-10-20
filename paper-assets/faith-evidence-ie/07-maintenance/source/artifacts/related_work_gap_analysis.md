# Related Work Gap Analysis — Re-dream 审稿补全

> 生成日期：2026-05-15
> 针对 dream_20260515T132059 三档审稿意见中 Related Work 缺失的系统调研

---

## 1. 审稿人点名必引论文

### 1.1 R1-RE (arXiv:2507.04642) — GRPO for Sentence-level RE

- **标题**: R1-RE: Cross-Domain Relation Extraction with RLVR
- **作者**: Runpeng Dai, Tong Zheng, Run Yang, Kaixian Yu, Hongtu Zhu
- **Venue**: arXiv, July 2025
- **核心方法**: 将关系抽取重新定义为推理任务，引入 RLVR（Reinforcement Learning with Verifiable Rewards）框架，使用 GRPO 算法优化 LLM 的 RE 能力。采用二元准确率 reward + 格式 reward 的规则化奖励方案。R1-RE-7B 在 OOD 场景下达到 ~70% 准确率，媲美 GPT-4o。
- **与 FREIGE 的关系**: **核心对比论文**。R1-RE 在 sentence-level RE 上 GRPO 成功，而 FREIGE 在 document-level RE 上 GRPO 失败转向 RSFT，构成天然的正反对比。差异来源可能在于 document-level 的长序列、多关系、高复杂度导致 GRPO 的 reward signal 过于稀疏。
- **引用方式**: Related Work (RLVR for IE) + 实验分析部分（sentence vs document level GRPO 对比讨论），**must-cite**。

### 1.2 RelPrior (arXiv:2511.08143) — Relation as a Prior for LLM DocRE

- **标题**: Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction
- **作者**: Qiankun Pi, Yepeng Sun, Jicang Lu, Qinlong Fan, Ningbo Huang, Shiyu Wang
- **Venue**: arXiv, November 2025
- **核心方法**: 提出两阶段范式——(1) Binary Relation Prior 过滤无关 entity pairs；(2) Predefined Relation Prior 做 entity matching 而非直接预测 relation label。在 Qwen2.5-7B 和 DeepSeek-R1-Distill-LLaMA3-8B 上测试，在 DocRED 和 RE-DocRED 上达到 SOTA。
- **与 FREIGE 的关系**: **竞争方法**。RelPrior 走 SFT + prompt engineering 路线取得 SOTA，FREIGE 走 RSFT（rejection sampling）路线。两者都用 7-8B 规模 LLM 做 DocRE，直接可比。
- **引用方式**: Related Work (LLM-based DocRE methods) + baseline 对比讨论。

### 1.3 Ru-LLM — Logical Rule-Constrained LLM for DocRE

- **标题**: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction
- **作者**: Kunli Zhang, Pengcheng Wu, Bohan Yu, Yunlong Li, Dezhi Kong, Hongying Zan, Min Peng, Yu Song
- **Venue**: NLPCC 2025 (Springer LNAI)
- **核心方法**: 用频繁模式挖掘 + LLM 辅助补全获取候选谓词池，通过 Monte Carlo Tree Search 搜索生成逻辑规则。将规则转化为 prompt 引导 LLM 初始生成，再用 CoT 验证过程保留满足所有规则的三元组。在 DWIE、DocRED、Re-DocRED 上超越现有方法。
- **与 FREIGE 的关系**: **互补方法**。Ru-LLM 用显式逻辑规则约束 LLM 输出，FREIGE 用 faithful evidence 约束。两者都旨在提高 LLM DocRE 的可靠性，但路径不同（规则 vs 证据）。
- **引用方式**: Related Work (LLM-based DocRE methods)。

### 1.4 AutoRE (arXiv:2403.14888) — RHF Paradigm for DocRE

- **标题**: AutoRE: Document-Level Relation Extraction with Large Language Models
- **作者**: Lilong Xue, Dan Zhang, Yuxiao Dong, Jie Tang
- **Venue**: ACL 2024 (System Demonstrations)
- **核心方法**: 提出 RHF（Relation-Head-Facts）三阶段范式，不依赖已知关系选项假设。用 QLoRA 微调 Mistral-7B，三个独立 QLoRA 模块分别负责 relation extraction、head entity identification、triple fact extraction。在 RE-DocRED 上超越 TAG 10.03%/9.03%（dev/test）。
- **与 FREIGE 的关系**: **竞争方法**。AutoRE 用分治策略（三模块 QLoRA），FREIGE 用端到端 + RSFT。两者都用 7B 规模 LLM，是直接可比的 baseline。
- **引用方式**: Related Work (LLM-based DocRE methods) + baseline 对比。

### 1.5 GLiDRE (arXiv:2508.00757) — Lightweight Generalist DocRE

- **标题**: GLiDRE: Generalist Lightweight model for Document-level Relation Extraction
- **作者**: Robin Armingaud, Romaric Besançon
- **Venue**: arXiv, August 2025 (submitted to ARR October 2025)
- **核心方法**: 基于 GLiNER 思路的轻量级 DocRE 模型，双编码器架构（文本编码器 + 标签编码器），entity pair 拼接后经 FFN 打分。在 few-shot 和低资源场景下达到 SOTA，强调数据效率。
- **与 FREIGE 的关系**: **互补方法**。GLiDRE 走轻量级/few-shot 路线（非 LLM），FREIGE 走 LLM + RL 路线。GLiDRE 在 low-resource 场景有优势，可讨论两类方法的适用场景差异。
- **引用方式**: Related Work (DocRE methods, non-LLM approaches)。

### 1.6 DAPO (arXiv:2503.14476) — Entropy Collapse in GRPO

- **标题**: DAPO: An Open-Source LLM Reinforcement Learning System at Scale
- **作者**: Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan 等 30+ 位作者 (ByteDance Seed)
- **Venue**: arXiv, March 2025
- **核心方法**: 识别 GRPO 中的 entropy collapse 问题并提出四项技术：(1) Clip-Higher（非对称裁剪缓解 entropy collapse）；(2) Dynamic Sampling（过滤无效梯度批次）；(3) Token-Level Policy Gradient Loss（不同长度序列的适当加权）；(4) Overlong Reward Shaping（处理截断噪声）。基于 Qwen2.5-32B 在 AIME 2024 达到 50 分。
- **与 FREIGE 的关系**: **理论支撑**。FREIGE 在 DocRE 上观察到的 GRPO 训练不稳定/失败，可能与 DAPO 识别的 entropy collapse 问题直接相关。DAPO 的发现解释了为什么 FREIGE 需要从 GRPO 转向 RSFT。
- **引用方式**: 方法分析部分（解释 GRPO 失败原因）+ Related Work (RL optimization)。

### 1.7 Dr. GRPO (arXiv:2503.20783) — Normalization Bias in GRPO

- **标题**: Understanding R1-Zero-Like Training: A Critical Perspective
- **作者**: Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, Min Lin
- **Venue**: COLM 2025, arXiv March 2025
- **核心方法**: 识别 GRPO 中的两类偏差：(1) 长度偏差——按序列长度归一化导致错误回复的长度惩罚不足；(2) 标准差偏差——按 std(r) 归一化导致难度不同的问题权重失衡。Dr. GRPO 用固定常数替代长度归一化，移除标准差归一化项。7B 模型在 AIME 2024 达到 43.3%。
- **与 FREIGE 的关系**: **理论支撑**。Dr. GRPO 识别的 length bias 在 DocRE 中可能更严重（document-level 输出远长于 sentence-level），进一步解释 FREIGE 中 GRPO 效果不佳的原因。
- **引用方式**: 方法分析部分（GRPO 偏差分析）+ Related Work (RL optimization)。

### 1.8 Contrastive Reward Methods

#### 1.8a arXiv:2403.07708 — Contrastive Rewards for RLHF

- **标题**: Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards
- **作者**: Wei Shen, Xiaoying Zhang, Yuanshun Yao, Rui Zheng, Hongyi Guo, Yang Liu
- **Venue**: arXiv, March 2024
- **核心方法**: 在 RLHF 中引入 contrastive reward 惩罚项——离线采样 baseline 回复，在 PPO 阶段计算对比 reward。目标：惩罚 reward 不确定性、提高鲁棒性、鼓励超越 baseline、根据任务难度校准、降低 PPO 方差。
- **与 FREIGE 的关系**: **方法启发**。Contrastive reward 思路可用于改进 FREIGE 的 reward 设计，减少 reward hacking 和不稳定性。
- **引用方式**: Related Work (reward design in RL)。

#### 1.8b EMNLP 2024 — Contrastive Learning for Reward Models

- **标题**: Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning
- **作者**: Lu Chen, Rui Zheng, Binghai Wang, Senjie Jin, Caishuang Huang, Junjie Ye, Zhihao Zhang, Yuhao Zhou, Zhiheng Xi, Tao Gui, Qi Zhang, Xuanjing Huang
- **Venue**: EMNLP 2024, pages 15270–15283
- **核心方法**: 将对比学习引入 reward model 训练，结合监督排序损失和无监督对比损失。解决 reward model 对噪声和模糊数据的脆弱性，提高泛化能力和训练稳定性。
- **与 FREIGE 的关系**: **互补技术**。更好的 reward model 可能改善 FREIGE 的 RL 训练效果，与 FREIGE 从 GRPO 转向 RSFT 的决策形成对比——是否用更好的 reward model 就能挽救 GRPO？
- **引用方式**: Related Work (reward modeling)。

### 1.9 Minimalist Approach to LLM Reasoning (arXiv:2504.11343) — RSFT 理论基础

- **标题**: A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce
- **作者**: Wei Xiong, Jiarui Yao, Yuhui Xu, Bo Pang, Lei Wang, Doyen Sahoo, Junnan Li, Nan Jiang, Tong Zhang, Caiming Xiong, Hanze Dong
- **Venue**: arXiv, April 2025
- **核心方法**: 证明简单的 rejection sampling baseline（RAFT，仅用正确样本训练）在推理任务上与 GRPO 和 PPO 效果相当。关键发现：GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。提出 Reinforce-Rej，过滤全错和全对样本，提升效率和稳定性。
- **与 FREIGE 的关系**: **核心理论支撑**。直接为 FREIGE 的 RSFT 方法提供理论正当性——如果 rejection sampling 在推理任务上已经能匹配 GRPO/PPO，那么在更复杂的 DocRE 任务上选择 RSFT 而非 GRPO 是合理且有理论依据的决策。
- **引用方式**: 方法动机部分（RSFT 的理论基础）+ Related Work (RL vs SFT for LLM)，**must-cite**。

---

## 2. 额外发现：2025-2026 DocRE 新方法

### 2.1 LMRC (arXiv:2408.13889) — LLM + Relation Classifier

- **标题**: LLM with Relation Classifier for Document-Level Relation Extraction
- **作者**: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang
- **Venue**: arXiv, August 2024
- **核心方法**: 两阶段 DocRE——先用分类器筛选有潜在关系的 entity pair，再用 LLM 做最终关系分类。解决 LLM 注意力在无关 entity pair 上分散的问题。
- **与 FREIGE 的关系**: 竞争方法。LMRC 用 pre-classifier + LLM 的两阶段方案，FREIGE 用端到端方案 + RSFT。
- **引用方式**: Related Work (LLM-based DocRE methods)。

### 2.2 ToolRE (ICIC 2025) — Tool-Assisted DocRE

- **标题**: Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning
- **作者**: (ICIC 2025, Springer)
- **Venue**: ICIC 2025
- **核心方法**: 设计三个工具分别处理 entity extraction、explicit RE、complex RE。采用 tuning-free 策略，LLM 推理 trigger words 和 relations，加入 backward verification 获得可解释的验证分数。
- **与 FREIGE 的关系**: 互补方法。ToolRE 走 agent/tool-use 路线（无需微调），FREIGE 走微调路线。
- **引用方式**: Related Work (LLM-based DocRE methods)。

---

## 3. 额外发现：GRPO/RL 在结构化 IE 上的应用

### 3.1 R²GRPO (arXiv:2505.22068) — GRPO for Scientific IE

- **标题**: Beyond Path Selection: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced (R²)GRPO
- **作者**: Ran Li, Shimin Di, Yuchen Liu, Chen Jing, Yu Qiu, Lei Chen
- **Venue**: arXiv, May 2025
- **核心方法**: MimicSFT（结构化推理模板的 SFT）+ R²GRPO（relevance + rule-based dual reward 的 GRPO）。专门针对 SciIE 场景，解决推理 LLM 在结构化 IE 上不如 BERT 的问题。MimicSFT + R²GRPO 组合比标准 SFT 提升 24.59 点 Rel F1。
- **与 FREIGE 的关系**: **高度相关**。R²GRPO 是目前唯一成功将 GRPO 应用于关系抽取任务的工作。与 FREIGE 的 GRPO 失败形成有趣对比——R²GRPO 通过 rule-based reward 设计克服了 GRPO 在 IE 上的困难。
- **引用方式**: Related Work (RL for IE) + 方法对比讨论，**建议重点引用**。

---

## 4. 额外发现：Rejection Sampling 理论分析

### 4.1 RFT 原始论文 (arXiv:2308.01825)

- **标题**: Scaling Relationship on Learning Mathematical Reasoning with Large Language Models
- **作者**: Zheng Yuan, Hongyi Yuan, Chengpeng Li, Guanting Dong, Keming Lu, Chuanqi Tan, Chang Zhou, Jingren Zhou
- **Venue**: arXiv, August 2023
- **核心方法**: 提出 Rejection sampling Fine-Tuning (RFT)，用监督模型生成正确推理路径作为增强数据集。发现 RFT 对弱模型提升更大，augmented samples 中不同推理路径越多效果越好。LLaMA-7B 在 GSM8K 上从 SFT 的 35.9% 提升到 RFT 的 49.3%。
- **与 FREIGE 的关系**: **方法先驱**。FREIGE 的 RSFT 直接继承 RFT 的思路，应用于 DocRE。
- **引用方式**: Related Work (rejection sampling 方法溯源)。

---

## 5. 总结：引用优先级

### Must-cite（审稿人点名 + 核心理论支撑）
1. **R1-RE** — sentence-level GRPO 成功 vs 我们 doc-level GRPO 失败
2. **Minimalist Approach (2504.11343)** — RSFT 理论正当性
3. **DAPO** — entropy collapse 解释 GRPO 失败
4. **Dr. GRPO** — length/normalization bias 解释 GRPO 失败

### Should-cite（同类竞争方法）
5. **RelPrior** — 最新 LLM DocRE SOTA
6. **AutoRE** — ACL 2024 LLM DocRE
7. **Ru-LLM** — NLPCC 2025 规则约束 DocRE
8. **GLiDRE** — 轻量级 few-shot DocRE
9. **R²GRPO** — GRPO 在 SciIE 上成功应用

### Nice-to-cite（补充参考）
10. **Contrastive Rewards (2403.07708)** — reward 设计
11. **EMNLP 2024 Contrastive RM** — reward model 改进
12. **RFT (2308.01825)** — rejection sampling 方法溯源
13. **LMRC** — LLM + classifier DocRE
14. **ToolRE** — tool-use DocRE
