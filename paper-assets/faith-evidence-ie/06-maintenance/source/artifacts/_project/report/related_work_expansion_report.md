# FREIGE Related Work Expansion Report

**Date**: 2026-05-15
**Scope**: 5 directions, 17 new papers added (68 → 85 total)

---

## 1. Evidence-based / Explainable Relation Extraction (3 new papers)

### 1.1 EAAGRE (2024, Computer Speech & Language)
**Evidence and Axial Attention Guided Document-level Relation Extraction**
- 直接引导 PLM encoder 最后层 top-k token attention 到 evidence sentences，不引入额外参数
- Axial attention 建模 relation triple 间全局依赖
- **与 FREIGE 关系 (support)**: 与 DREEAM 同属 evidence-guided attention 范式。EAAGRE 在 encoder 内部注入 evidence signal，我们 CED reranker 在 generation 后验证，两者互补证明 evidence 信号无论注入位置都有效

### 1.2 GEGA (2024, arXiv 2407.21384)
**Graph Convolutional Networks and Evidence Retrieval Guided Attention**
- GCN 构建多权重矩阵引导 attention 到 evidence sentences
- Teacher-Student 框架：Teacher 全监督推断 evidence，Student 用权重作监督信号
- **与 FREIGE 关系 (support)**: Teacher-Student evidence distillation 与 CED reranker 动机一致——外部注入 evidence quality 信号。差异：GEGA 是 training-time，我们是 inference-time

### 1.3 KnowRA (2025, IJCAI 2025)
**Knowledge Retrieval Augmented Method for DocRE with Comprehensive Reasoning**
- 外部知识库检索增强 DocRE 推理 + 知识过滤 + axial attention 跨句推理
- **与 FREIGE 关系 (contrast)**: 代表"检索 evidence"路线 vs 我们的"生成 evidence"路线。我们发现生成有 faithfulness tax，KnowRA 通过检索绕过这个问题

---

## 2. Faithfulness in Structured Output (4 new papers)

### 2.1 G&O (2024, arXiv 2402.13364)
**A Simple but Effective Approach to Improve Structured Language Model Output for IE**
- 将 structured IE 拆为两步：先自然语言生成内容，再组织为目标结构
- 分离内容生成和结构化过程，减轻同时完成两个正交任务的压力
- **与 FREIGE 关系 (support)**: 直接支持核心发现——RE + evidence generation 相当于内容+结构化的同时任务，存在固有冲突。G&O 是 prompting 层面解耦，我们发现 RL training 中的自发解耦

### 2.2 Evidence Extraction Metrics (2026, arXiv 2601.02627)
**Improved Evidence Extraction and Metrics for Document Inconsistency Detection with LLMs**
- 新 evidence extraction 评估指标 + redact-and-retry 框架
- **与 FREIGE 关系 (extend)**: 我们的 EDCR 指标从 DocRE 角度评估 evidence quality，该工作从 inconsistency detection 角度——两者互补

### 2.3 Structural Failures in Evidence Extraction (2026, arXiv 2602.10881)
**Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis**
- LLM 在需要稳定绑定 variables/roles/methods 时性能急剧下降
- 识别 role reversal、binding drift、instance compression、numeric misattribution
- **与 FREIGE 关系 (support)**: 强化核心论点——faithfulness tax 是 structural failure 在 DocRE 的具体表现

### 2.4 APIE (2025, AAAI 2026)
**Reflect then Learn: Active Prompting for IE Guided by Introspective Confusion**
- Dual-component uncertainty: Format Uncertainty + Content Uncertainty
- **与 FREIGE 关系 (support)**: Format vs content uncertainty 分解与 RE vs evidence 冲突类似，为理解 faithfulness tax 来源提供理论视角

---

## 3. RLHF/GRPO for Structured Tasks (4 new papers)

### 3.1 GRPO-LEAD (2025, EMNLP 2025)
**Difficulty-Aware RL Approach for Concise Mathematical Reasoning**
- Length-regularized rewards + 错误惩罚 + difficulty-aware advantage reweighting
- **与 FREIGE 关系 (extend)**: Length penalty 与 evidence generation 增加输出长度相关，difficulty-aware reweighting 可启发 CED reward 差异化处理

### 3.2 E-GRPO (2025, ICLR 2026)
**Entity-Aware Reward for GRPO**
- Entity-aware partial credit：对 negative samples 基于 entity match rate 给部分奖励
- 区分 "near-miss" 和完全失败
- **与 FREIGE 关系 (support)**: 与 CED reward 理念高度一致——task-specific fine-grained reward signal。E-GRPO 用 entity match，我们用 NLI-based evidence quality

### 3.3 SFT vs RL Fine-Tuning (2025, arXiv 2508.16546)
**RL Is Neither a Panacea Nor a Mirage**
- RL-FT 可恢复 SFT 的 OOD 损失，但严重 overfitting 时无法完全恢复
- 性能与 singular vector 方向旋转相关
- **与 FREIGE 关系 (support)**: 解释 RSFT→GRPO pipeline 合理性及 QLoRA GRPO 限制

### 3.4 Multi-objective RL for Event Extraction (2025, Springer)
**Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective RL**
- 多目标 RL 用于事件抽取
- **与 FREIGE 关系 (support)**: 同属"RL 优化 IE 任务"范式，事件抽取的多目标与 DocRE 多目标结构相似

---

## 4. QLoRA vs Full Fine-tuning Discrepancies (2 new papers)

### 4.1 LoRA Rank Trade-offs (2025, IJCNLP-AACL 2025)
**How Much is Too Much? Exploring LoRA Rank Trade-offs for Knowledge and Robustness**
- 中等 rank (r=32-64) 为最佳平衡点
- **与 FREIGE 关系 (extend)**: 我们 QLoRA (r=16) 可能处于 rank 不足区间，解释 task decoupling

### 4.2 RandLoRA (2025, ICLR 2025)
**Full-rank Parameter-Efficient Fine-tuning of Large Models**
- 学习 fixed random matrices 的 diagonal scaling 实现 full-rank 更新
- 保持参数效率同时突破 low-rank 限制
- **与 FREIGE 关系 (extend)**: 直接回应 QLoRA 限制——full-rank PEFT 可能解决 multi-objective GRPO 中 task decoupling

---

## 5. Multi-task Learning Trade-offs in IE (3 new papers + 1 survey)

### 5.1 C-LoRAE (2025, arXiv 2505.06303)
**Collaborative Multi-LoRA Experts for Unified Multimodal IE**
- Universal expert + task-specific experts + mutual information maximization
- Achievement-based multi-task loss 动态平衡任务进度
- **与 FREIGE 关系 (support)**: Universal + task-specific expert 直接对应 RE + evidence 多任务。Achievement-based loss 可启发 CED reward 动态权重

### 5.2 Ortho-LoRA (2026, arXiv 2601.09684)
**Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection**
- 将冲突任务梯度投影到正交补空间
- **与 FREIGE 关系 (support)**: 直接解释 QLoRA GRPO task decoupling——RE 和 evidence 的 gradient 在 low-rank 空间冲突

### 5.3 Proactive Gradient Conflict Mitigation (2024, arXiv 2411.18615)
**A Sparse Training Perspective on Multi-Task Learning**
- 选择参数子集学习多任务，冻结其余参数
- **与 FREIGE 关系 (support)**: QLoRA 本质是 task-agnostic sparse training，其 sparsity 模式非为多任务设计，解释多目标 GRPO 表现不佳

### 5.4 Generative IE Survey (2024, Frontiers of Computer Science)
**Large Language Models for Generative Information Extraction: A Survey**
- 全面综述 LLM 在 IE 各子任务中的应用
- **与 FREIGE 关系 (context)**: 定位 FREIGE 在 generative IE 生态中的位置

---

## Summary of Key Findings

| Direction | New Papers | Key Insight for FREIGE |
|-----------|-----------|----------------------|
| Evidence-based DocRE | 3 | Evidence signal 在 encoding/retrieval/generation 各阶段都有效，但生成路线有独特的 faithfulness tax |
| Faithfulness Structured | 4 | 多项独立证据表明 LLM 在 structured evidence extraction 中存在系统性困难，支持 faithfulness tax 发现 |
| GRPO for Structured Tasks | 4 | Entity-aware / difficulty-aware reward 设计趋势与 CED 理念一致；SFT→RL pipeline 有理论支撑 |
| QLoRA Gaps | 2 | Low rank 是 task decoupling 的可能根因；full-rank PEFT 是潜在解决方案 |
| MTL Trade-offs in IE | 4 | Gradient conflict 在 LoRA multi-task 中已被系统研究，提供 task decoupling 的理论框架 |

## Novelty Positioning Update

新增文献进一步巩固 FREIGE 的 novelty：
1. **Faithfulness tax 概念**：无竞争者。最近的 structural failure 和 G&O 工作从不同角度佐证这一现象，但都未在 DocRE 中系统量化
2. **QLoRA-specific task decoupling**：Ortho-LoRA 和 RandLoRA 从理论层面支持我们的发现，但无人在 RL+DocRE 场景中报告过
3. **CED reranker**：E-GRPO 是最接近的工作（entity-aware reward），但 CED 的 NLI-based evidence quality + inference-time reranking 组合仍然独特
4. **EvidenceRL** (已在现有文献中)：仍是最大 novelty 威胁，但聚焦 QA 而非 DocRE
