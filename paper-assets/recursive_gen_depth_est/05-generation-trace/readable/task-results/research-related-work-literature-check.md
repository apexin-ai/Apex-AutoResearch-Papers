# research related work literature check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_literature_check_20260518T232412_result.json`
- **Structured JSON:** [`1889f5127b3609461834.json`](../../sessions/18/1889f5127b3609461834.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 领域 1: Model Collapse

### Bertrand et al. "On the Stability of Iterative Retraining of Generative Models on their Own Data"
- **Venue**: ICLR 2024 (Spotlight)
- **作者**: Bertrand, Bose, Duplessis, Jiralerspong, Gidel
- **关系**: 建立了迭代重训练稳定性的理论条件，其 "iterative generation" 概念直接对应你们的 "generation depth"
- **应引用**: Yes
- **建议位置**: Related Work model collapse 段
- **理由**: Shumailov 之外最重要的理论互补，分析了 real/synthetic 混合比例对 collapse 的影响

### Alemohammad et al. "Self-Consuming Generative Models Go MAD"
- **Venue**: ICLR 2024
- **作者**: Alemohammad et al.
- **关系**: 提出 Model Autophagy Disorder (MAD) 框架，形式化了自消费循环中 quality/diversity 随代数递减的过程
- **应引用**: Yes
- **建议位置**: Related Work model collapse 段 / Introduction
- **理由**: 形式化了 autophagous loops 的三种模式，你的 depth estimation 直接度量这种退化

### Kazdan et al. "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
- **Venue**: ICML 2025
- **作者**: Kazdan, Schaeffer, Dey, Gerstgrasser, Rafailov, Donoho, Koyejo
- **关系**: 综合研究 synthetic data 何时导致 collapse 何时有益，建立稳定/不稳定条件
- **应引用**: Yes
- **建议位置**: Related Work model collapse 段
- **理由**: 最全面的 synthetic data 生态综述，你的 depth estimation 可作为评估该论文所识别风险条件的工具

### Dohmatob et al. "Strong Model Collapse"
- **Venue**: ICLR 2025 (Spotlight)
- **作者**: Dohmatob, Feng, Subramonian, Kempe
- **关系**: 证明即使 1/1000 的 synthetic data 也导致 collapse，大模型放大效应
- **应引用**: Maybe — 如果已引 Dohmatob 2024 是 "A Tale of Tails" (ICML 2024)，则这篇是更强的后续结果，应单独引用
- **建议位置**: Related Work model collapse 段
- **理由**: 比 2024 版本证明了严格更强的结论

### Drayson et al. "Machine-Generated Text Detection Prevents Language Model Collapse"
- **Venue**: EMNLP 2025
- **作者**: Drayson, Yilmaz, Lampos
- **关系**: 证明检测并过滤 machine-generated text 可防止 collapse，桥接了检测与 collapse 预防
- **应引用**: Yes
- **建议位置**: Related Work collapse/detection 交界处；Introduction 可强化 depth estimation 的实用价值
- **理由**: 直接验证了你们方法的应用场景：如果能估计 generation depth，就能过滤/加权污染数据

---

## 领域 2: AI Text Detection 新方法

### Guo et al. "BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens"
- **Venue**: NeurIPS 2024
- **作者**: Guo et al.
- **关系**: 用 bi-directional cross-entropy (forward loss + backward memorization) 做 zero-shot 检测，与你们用 token-level 统计特征的范式一致
- **应引用**: Yes
- **建议位置**: Related Work statistical detection 段
- **理由**: NeurIPS 级别的最新 zero-shot 统计检测方法，与你们的特征工程方法直接可比

### Verma et al. "Ghostbuster: Detecting Text Ghostwritten by Large Language Models"
- **Venue**: NAACL 2024
- **作者**: Verma et al.
- **关系**: 用结构化特征搜索 + 训练分类器的 pipeline，方法论上最接近你们的 RF + 19 统计特征
- **应引用**: Yes
- **建议位置**: Related Work feature-based detection 段
- **理由**: 特征工程 + 分类器 pipeline 与你们方法最相似，证明 crafted features 可优于 end-to-end 方法

### Li et al. "MAGE: Machine-generated Text Detection in the Wild"
- **Venue**: ACL 2024
- **作者**: Li et al.
- **关系**: 跨 27 个 LLM 的大规模检测 benchmark，评估 domain shift 和 paraphrase robustness
- **应引用**: Yes
- **建议位置**: Related Work benchmarks/evaluation 段
- **理由**: 最大规模的检测 benchmark，展示 distributional overlap 增加检测难度，justifies depth estimation 的挑战性

### Yang et al. "A Survey on Detection of LLMs-Generated Content"
- **Venue**: EMNLP 2024 Findings
- **作者**: Yang et al.
- **关系**: 覆盖 watermarking、statistical、classifier-based 检测方法的综合 survey
- **应引用**: Yes
- **建议位置**: Related Work 开头作为领域概览引用
- **理由**: 顶会 peer-reviewed survey，让读者一站式了解检测领域全貌

### Zhang et al. "Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy"
- **Venue**: ICLR 2024
- **作者**: Zhang et al.
- **关系**: 处理不同 LLM 生成文本形成多子群的分布差异问题，类比你们不同 depth 形成的子群
- **应引用**: Maybe
- **建议位置**: Related Work statistical detection 段
- **理由**: multi-population 分析与你的 multi-depth 设定有概念联系，但方法差异较大

---

## 领域 3: Recursive Generation / Iterative Self-Improvement

### Mohamed et al. "LLM as a Broken Telephone: Iterative Generation Distorts Information"
- **Venue**: ACL 2025
- **作者**: Mohamed, Geng, Vazirgiannis, Shang
- **关系**: 直接研究 iterative LLM generation 中信息如何随链深度失真，是同一现象的信息论视角
- **应引用**: Yes
- **建议位置**: Related Work iterative generation 段；Introduction 也可引用
- **理由**: 最直接的并行工作——研究相同核心现象（迭代生成退化），从不同角度（信息失真 vs 统计特征分类）

### Chen et al. "Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models" (SPIN)
- **Venue**: ICML 2024
- **作者**: Chen, Deng, Yuan, Ji, Gu
- **关系**: 用 self-play 让 LLM 迭代生成训练数据并学会区分自生成与人类数据，判别机制与你的分类任务概念平行
- **应引用**: Maybe
- **建议位置**: Related Work iterative self-improvement 段
- **理由**: 展示 generation depth 的区别是可学习的（正面案例：improvement 而非 collapse）

### Gambetta et al. "Characterizing Model Collapse in LLMs Using Semantic Networks and Next-Token Probability"
- **Venue**: arXiv 2024 (2410.12341, 未确认顶会)
- **作者**: Gambetta, Gezici, Giannotti, Pedreschi, Knott, Pappalardo
- **关系**: 用语义网络和 next-token 分布特征来刻画 collapse 跨代变化，方法论上最接近你们的工作
- **应引用**: Maybe — 仅 arXiv，如提交时已被顶会接收则引用
- **建议位置**: Related Work
- **理由**: 共享目标（用统计/结构特征刻画 generation depth 效应），但特征不同（语义网络 vs 你的 19 个统计特征）

---

## 领域 4: Ordinal Classification

### Kasa et al. "Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques"
- **Venue**: Findings of ACL 2024
- **作者**: Kasa, Goel, Gupta, Roychowdhury, Priyatam, Bhanushali, Murthy
- **关系**: 系统比较 explicit ordinal loss (包括 CORAL) 和 implicit PLM 方法用于有序文本分类
- **应引用**: Yes
- **建议位置**: Related Work ordinal classification 段；Method 中 justify CORAL loss 选择
- **理由**: 2024-2025 唯一一篇 top NLP venue 系统研究 ordinal loss for text 的论文，直接验证你的方法设计空间

### Cao et al. "CORAL: Rank Consistent Ordinal Regression for Neural Networks"
- **Venue**: Pattern Recognition Letters, 2020
- **作者**: Cao, Mirjalili, Raschka
- **关系**: CORAL 原始论文，你的 ordinal loss 的直接方法来源
- **应引用**: Yes (如果用 CORAL loss 则必引)
- **建议位置**: Method section
- **理由**: 方法论主要引用

### Wang et al. "A Survey on Ordinal Regression: Applications, Advances and Prospects"
- **Venue**: arXiv 2025 (2503.00952)
- **作者**: Wang et al.
- **关系**: 2025 年 ordinal regression 综合 survey，覆盖 CORAL/CORN/soft labeling 等
- **应引用**: Maybe — arXiv-only，未 peer-reviewed
- **建议位置**: Related Work ordinal 段作为一般引用
- **理由**: 如果需要 ordinal regression 领域的概览引用可以用；空间紧张则跳过

---

## 汇总：推荐引用优先级

| 优先级 | 论文 | Venue | 领域 |
|--------|------|-------|------|
| **必引** | Bertrand et al. "Stability of Iterative Retraining" | ICLR 2024 | Model Collapse |
| **必引** | Alemohammad et al. "Self-Consuming Models Go MAD" | ICLR 2024 | Model Collapse |
| **必引** | Drayson et al. "Detection Prevents Collapse" | EMNLP 2025 | Collapse + Detection |
| **必引** | Mohamed et al. "LLM as Broken Telephone" | ACL 2025 | Recursive Generation |
| **必引** | BiScope (Guo et al.) | NeurIPS 2024 | AI Detection |
| **必引** | Ghostbuster (Verma et al.) | NAACL 2024 | AI Detection |
| **必引** | Kasa et al. "Exploring Ordinality" | ACL Findings 2024 | Ordinal Classification |
| **强烈推荐** | Kazdan et al. "Collapse or Thrive" | ICML 2025 | Model Collapse |
| **强烈推荐** | MAGE (Li et al.) | ACL 2024 | AI Detection |
| **强烈推荐** | Yang et al. Detection Survey | EMNLP Findings 2024 | AI Detection |
| **强烈推荐** | CORAL (Cao et al.) | PRL 2020 | Ordinal (方法来源) |
| **视情况** | Dohmatob et al. "Strong Collapse" | ICLR 2025 | Model Collapse |
| **视情况** | SPIN (Chen et al.) | ICML 2024 | Iterative Self-Improvement |
| **视情况** | MMD-MP (Zhang et al.) | ICLR 2024 | AI Detection |

共 14 篇，其中 7 篇必引，4 篇强烈推荐，3 篇视空间和上下文决定。

---
