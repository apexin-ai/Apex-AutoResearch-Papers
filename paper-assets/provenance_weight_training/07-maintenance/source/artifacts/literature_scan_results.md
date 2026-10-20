# Literature Scan: Data Weighting / Selection for LLM Pretraining
# Target: EMNLP 2026 Related Work
# Date: 2026-05-15
# Focus: 2024-2026 papers relevant to dual-constrained adaptive b* for provenance-based pretraining data weighting

---

## Category 1: Direct Competitors (detect-and-reweight / provenance-based weighting)

### 1.1 Drayson et al. — Machine-Generated Text Detection Prevents Language Model Collapse
- **Authors**: George Drayson, Emine Yilmaz, Vasileios Lampos
- **Year**: 2025 | **Venue**: EMNLP 2025
- **ArXiv**: 2502.15654
- **Method**: Detect-and-reweight with w=(1-q)^b, b via validation-based grid search (WikiText-2), fixed during training. SIR resampling. ModernBERT 150M detector (AUC=0.986).
- **Relation**: **COMPETITOR** — 最直接竞争者。共享加权公式，但 b 选取方法根本不同。我们的核心贡献正是替代其 empirical grid search。
- **In literature_map.yaml**: YES

### 1.2 He et al. — Golden Ratio Weighting Prevents Model Collapse
- **Authors**: Hengzhi He, Shirong Xu, Guang Cheng
- **Year**: 2025 | **Venue**: Under review at JRSSB
- **ArXiv**: 2502.18049
- **Method**: 理论推导合成/真实数据混合最优权重 w*=1/φ (~0.62)，假设已知混合比例 k。
- **Relation**: **COMPETITOR** — 同为理论推导最优权重，但假设已知比例，不处理 online/unknown 设置。可作 oracle baseline。
- **In literature_map.yaml**: YES

### 1.3 Feng et al. — Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification
- **Authors**: Yunzhen Feng, Elvis Dohmatob, Pu Yang, François Charton, Julia Kempe
- **Year**: 2024 | **Venue**: arXiv
- **ArXiv**: 2406.07515
- **Method**: Verifier 过滤合成数据防止 model collapse。即使不完美 verifier 也有效。Hard filtering。
- **Relation**: **COMPETITOR** — 都用检测器置信度处理合成数据，但他们做 hard filtering，我们做 soft reweighting。
- **In literature_map.yaml**: YES

### 1.4 Sow et al. — Dynamic Loss-Based Sample Reweighting for Improved LLM Pretraining
- **Authors**: Daouda Sow et al.
- **Year**: 2025 | **Venue**: ICLR 2025
- **ArXiv**: 2502.06733
- **Method**: 基于 loss 值动态调整每个样本权重，online fashion。理论框架分析 loss-based reweighting 对收敛界的影响。7B/1.4B 模型验证。
- **Relation**: **COMPETITOR/COMPLEMENTARY** — 同为 instance-level dynamic reweighting，但信号来源不同（loss vs provenance/detector score）。收敛性理论框架可参考。
- **In literature_map.yaml**: YES

### 1.5 He et al. — SoftDedup: Efficient Data Reweighting for Speeding Up LM Pre-training
- **Authors**: Nan He et al.
- **Year**: 2024 | **Venue**: ACL 2024
- **ArXiv**: 2407.06654
- **Method**: N-gram commonness 指标做软去重加权（高频降权低频升权），vs 硬删除。26% 效率提升 + 1.77% 准确率提升。
- **Relation**: **COMPLEMENTARY** — 软加权 > 硬过滤的思路与我们一致。但信号是重复度，不是合成来源。
- **In literature_map.yaml**: YES

---

## Category 2: Domain/Group-Level Data Selection (不同粒度的对比方法)

### 2.1 Xie et al. — DoReMi: Optimizing Data Mixtures Speeds Up LM Pretraining
- **Authors**: Sang Michael Xie, Hieu Pham et al.
- **Year**: 2023 | **Venue**: NeurIPS 2023
- **ArXiv**: 2305.10429
- **Method**: 小代理模型 + Group DRO 优化域级别混合权重。不处理 instance-level 污染。
- **Relation**: **COMPLEMENTARY** — 域级 reweighting baseline。我们在 instance-level 操作，粒度更细。
- **In literature_map.yaml**: YES

### 2.2 Fan et al. — DoGE: Domain Reweighting with Generalization Estimation
- **Authors**: Simin Fan, Matteo Pagliardini, Martin Jaggi
- **Year**: 2024 | **Venue**: ICML 2024
- **ArXiv**: 2310.15393
- **Method**: 两阶段域权重优化：(i) proxy model + bi-level optimization 学习域权重; (ii) 大模型按学到的权重采样训练。SlimPajama 上优于 baseline。
- **Relation**: **COMPLEMENTARY** — 域级 reweighting，与 DoReMi 同类。我们做 instance-level provenance-based。
- **In literature_map.yaml**: NO — **建议添加**

### 2.3 Ye et al. — Data Mixing Laws: Optimizing Data Mixtures by Predicting LM Performance
- **Authors**: Jiasheng Ye et al.
- **Year**: 2025 | **Venue**: ICLR 2025
- **ArXiv**: 2403.16952
- **Method**: 混合比例与模型性能的定量可预测性。小规模训练预测大模型在不同混合下的性能。
- **Relation**: **COMPLEMENTARY** — 验证不同 b 下 mixing 效果的理论框架。域级方法。
- **In literature_map.yaml**: YES

### 2.4 Liu et al. — RegMix: Data Mixture as Regression for LM Pre-training
- **Authors**: Qian Liu et al.
- **Year**: 2025 | **Venue**: ICLR 2025 (Spotlight)
- **ArXiv**: 2407.01492
- **Method**: 训练 512 个 1M 模型，用回归预测最优混合比例，应用于 1B-7B 模型。匹配/超越 DoReMi 仅用 10% 计算。Web data > Wikipedia 的反直觉发现。
- **Relation**: **COMPLEMENTARY** — 离线域级混合优化。与我们的 online instance-level 方法正交。Related work 中作为域级方法代表。
- **In literature_map.yaml**: NO — **建议添加**

### 2.5 Shukor et al. — Scaling Laws for Optimal Data Mixtures
- **Authors**: Mustafa Shukor, Louis Bethune et al. (Sorbonne/Apple)
- **Year**: 2025 | **Venue**: ICLR 2025 Workshop
- **ArXiv**: 2507.09404
- **Method**: 系统化方法用 scaling laws 确定最优域混合比例。小规模发现的最优系数可迁移到大模型。跨 LLM/NMM/LVM 验证。
- **Relation**: **BACKGROUND** — scaling laws 视角下的域混合优化。我们可引用说明域级方法不处理 instance-level 污染。
- **In literature_map.yaml**: NO — **可选添加**

---

## Category 3: Instance-Level / Model-Aware Data Selection

### 3.1 Xie et al. — DSIR: Data Selection for Language Models via Importance Resampling
- **Authors**: Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang
- **Year**: 2023 | **Venue**: NeurIPS 2023
- **ArXiv**: 2302.03169
- **Method**: N-gram 特征 importance resampling 匹配目标分布。比启发式 filtering 更 principled。
- **Relation**: **COMPLEMENTARY** — 同用 importance resampling，但目标是分布匹配而非污染处理。与 Drayson SIR 有方法论联系。
- **In literature_map.yaml**: YES

### 3.2 Yu et al. — MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models
- **Authors**: Yu et al. (CMU)
- **Year**: 2024 | **Venue**: NeurIPS 2024
- **ArXiv**: 2406.06046
- **Method**: Data influence model 持续适应预训练模型的数据偏好，online 选择当前阶段最有效数据。410M/1B 模型在 C4 上验证。比 DSIR 等 2× 增益。
- **Relation**: **COMPETITOR** — 同为 online adaptive 数据选择，但信号是 data influence 而非 provenance。不处理合成污染。需在 related work 中区分：MATES 优化 task performance，我们优化 contamination robustness。
- **In literature_map.yaml**: NO — **建议添加，标注为 competitor**

### 3.3 Engstrom et al. — DsDm: Model-Aware Dataset Selection with Datamodels
- **Authors**: Logan Engstrom et al.
- **Year**: 2024 | **Venue**: ICML 2024
- **ArXiv**: 2401.12926
- **Method**: Datamodels 近似学习算法如何使用数据来预测任务表现。DsDm-selected 数据集提供 2× compute multiplier。
- **Relation**: **COMPLEMENTARY** — 基于 data influence 的离线选择，不处理污染。需区分信号类型。
- **In literature_map.yaml**: NO — **建议添加**

### 3.4 Gu et al. — PDS: Data Selection via Optimal Control for Language Models
- **Authors**: Yuxian Gu et al. (Microsoft/Tsinghua)
- **Year**: 2025 | **Venue**: ICLR 2025 (Oral, top 1.8%)
- **ArXiv**: 2410.07064
- **Method**: 数据选择建模为最优控制问题，用 Pontryagin's Maximum Principle 求解。CommonCrawl 选择加速学习，扩展至 ~400B 模型 ~10T tokens。数据需求降低 1.8×。
- **Relation**: **COMPLEMENTARY** — 理论优雅的离线选择方法。与我们的 online adaptive 方法互补。Related work 中作为 principled data selection 的代表。
- **In literature_map.yaml**: NO — **建议添加**

### 3.5 Yu et al. — Group-MATES: Group-Level Data Selection for Efficient Pretraining
- **Authors**: Zichun Yu, Fei Peng et al. (Meta)
- **Year**: 2025 | **Venue**: NeurIPS 2025
- **ArXiv**: 2502.14709
- **Method**: 关系数据影响模型参数化 group-level 选择。3.5%-9.4% 相对增益，几乎翻倍 individual 选择 baseline。理论分析 group vs individual influence 交互。
- **Relation**: **COMPLEMENTARY** — group-level influence 视角。理论分析 data interaction 对我们理解 batch-level 统计有参考价值。
- **In literature_map.yaml**: NO — **可选添加**

### 3.6 Zhang et al. — Quad: Harnessing Diversity for Important Data Selection in Pretraining LLMs
- **Authors**: Chi Zhang et al.
- **Year**: 2025 | **Venue**: ICLR 2025
- **ArXiv**: 2409.16986
- **Method**: Data influence + MAB 聚类，同时考虑质量和多样性。SlimPajama/FineWeb 上 7B 模型验证。
- **Relation**: **COMPLEMENTARY** — quality + diversity 的双重考量与我们 quality + stability 的双约束有哲学共鸣，但技术路线完全不同。
- **In literature_map.yaml**: NO — **可选添加**

### 3.7 QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining
- **Authors**: ByteDance
- **Year**: 2025 | **Venue**: arXiv (2504.16511)
- **Method**: 统一参数化采样函数，sigmoid-based 函数同时控制质量和域多样性。7.2% 平均基准提升。
- **Relation**: **COMPLEMENTARY** — 统一框架平衡 quality/diversity。我们的 α_eff/ESS 双约束是不同维度的平衡（quality/stability）。
- **In literature_map.yaml**: NO — **可选添加**

### 3.8 Grangier et al. — Task-Adaptive Pretrained LMs via Clustered-Importance Sampling
- **Authors**: David Grangier, Simin Fan, Skyler Seto, Pierre Ablin
- **Year**: 2025 | **Venue**: ICLR 2025
- **ArXiv**: 2410.03735
- **Method**: 聚类 generalist 数据集，按 specialist 数据的聚类直方图重采样。350M-7B 验证。适用于 pretraining 和 continued pretraining。
- **Relation**: **COMPLEMENTARY** — importance sampling 用于域适配，不处理污染。方法论上与 DSIR 相关。
- **In literature_map.yaml**: NO — **可选添加**

---

## Category 4: Model Collapse Theory & Synthetic Data

### 4.1 Shumailov et al. — AI Models Collapse When Trained on Recursively Generated Data
- **Authors**: Ilia Shumailov et al.
- **Year**: 2024 | **Venue**: Nature 2024
- **Relation**: **BACKGROUND** — 奠基性工作，model collapse 核心动机。
- **In literature_map.yaml**: YES

### 4.2 Alemohammad et al. — Self-Consuming Generative Models Go MAD
- **Authors**: Sina Alemohammad et al.
- **Year**: 2024 | **Venue**: ICLR 2024
- **Relation**: **BACKGROUND** — MAD 概念，三种自消费循环分析。
- **In literature_map.yaml**: YES

### 4.3 Dohmatob et al. — Strong Model Collapse
- **Authors**: Elvis Dohmatob, Yunzhen Feng et al.
- **Year**: 2025 | **Venue**: ICLR 2025 (Spotlight)
- **ArXiv**: 2410.04840
- **Relation**: **BACKGROUND** — 即使 1/1000 合成数据也致 collapse。强化我们工作的必要性。
- **In literature_map.yaml**: YES

### 4.4 Kazdan et al. — Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data
- **Authors**: Rylan Schaeffer, Yuanzhi Li et al.
- **Year**: 2025 | **Venue**: ICML 2025
- **ArXiv**: 2404.01413
- **Method**: 证明数据替换导致 collapse，但数据累积（保留真实数据）可避免 collapse。测试误差有有限上界。跨 LLM/diffusion/VAE 验证。
- **Relation**: **BACKGROUND** — 为 "accumulate vs replace" 提供理论框架。我们的 soft reweighting 可视为一种加权累积。
- **In literature_map.yaml**: NO — **建议添加**

### 4.5 Dohmatob et al. — Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World
- **Authors**: Elvis Dohmatob et al.
- **Year**: 2025 | **Venue**: ICML 2025
- **ArXiv**: 2410.16713
- **Method**: 分析三种训练工作流（replace/accumulate/fixed compute）。Replace 导致 collapse，accumulate 可避免。
- **Relation**: **BACKGROUND** — 与 4.4 互补的理论分析。进一步支撑 "不要完全丢弃合成数据" 的论点，为 soft reweighting 提供理论支持。
- **In literature_map.yaml**: NO — **建议添加**

### 4.6 Liu et al. — Demystifying Synthetic Data in LLM Pre-training: Scaling Laws, Benefits, and Pitfalls
- **Authors**: (Multiple)
- **Year**: 2025 | **Venue**: EMNLP 2025
- **ArXiv**: 2510.01631
- **Method**: 1000+ LLM / 100K+ GPU hours 系统实验。最优合成比例 ~30% (rephrased)。Rephrased 无 collapse，textbook-style 有 collapse。>8B 生成器不一定更好。
- **Relation**: **BACKGROUND** — 大规模实证研究，为合成数据混合提供 scaling law 视角。我们可引用说明合成数据的 nuanced 效果。
- **In literature_map.yaml**: NO — **建议添加**

### 4.7 Guo et al. — Escaping Model Collapse via Synthetic Data Verification
- **Year**: 2025 | **ArXiv**: 2510.16657
- **Relation**: **BACKGROUND** — verification-based prevention。已在 literature_map.yaml 中。
- **In literature_map.yaml**: YES

---

## Category 5: Importance Weighting Theory & ESS

### 5.1 Vehtari et al. — Pareto Smoothed Importance Sampling
- **Year**: 2024 | **Venue**: JMLR 2024
- **Relation**: **METHOD-COMPONENT** — ESS 估计和收敛诊断理论来源。
- **In literature_map.yaml**: YES

### 5.2 Kimura & Hino — A Short Survey on Importance Weighting for Machine Learning
- **Year**: 2024 | **Venue**: TMLR 2024
- **Relation**: **METHOD-COMPONENT** — importance weighting 综述。
- **In literature_map.yaml**: YES

### 5.3 Elvira et al. — Effective Sample Size Approximations as Entropy Measures
- **Authors**: Victor Elvira et al.
- **Year**: 2025 | **Venue**: Computational Statistics 2025
- **Method**: 建立 ESS 表达式与 Rényi/Tsallis 熵的联系。ESS 家族的统一理论框架。连接 Hill numbers (生态学)、Gini 系数 (经济学)、Gini impurity (ML)。
- **Relation**: **BACKGROUND** — 为我们使用 Kish's ESS 提供更广泛的理论背景。说明 ESS 是跨学科的稳健度量。
- **In literature_map.yaml**: NO — **可选添加**

### 5.4 Huang et al. — Importance Weighting Can Help Large Language Models Self-Improve
- **Authors**: Huang et al.
- **Year**: 2025 | **Venue**: AAAI 2025
- **ArXiv**: 2408.09849
- **Method**: DS weight (distribution shift extent) 过滤 self-generated samples。仅需 5% valid set 近似 DSE。提升 LLM self-improvement reasoning。
- **Relation**: **COMPLEMENTARY** — importance weighting 在 LLM 训练中的新应用。信号是 distribution shift 而非 provenance。
- **In literature_map.yaml**: NO — **可选添加**

---

## Category 6: Curriculum Learning & Data Ordering

### 6.1 Curriculum Learning for LLM Pretraining: An Analysis of Learning Dynamics
- **Year**: 2025 | **ArXiv**: 2601.21698
- **Method**: 系统分析 curriculum learning 在 LLM pretraining 中的效果。压缩比、词汇多样性、可读性作为难度信号。收敛加速 18-45%。
- **Relation**: **BACKGROUND** — 数据排序 vs 数据加权是不同但相关的数据优化维度。我们做 instance-level weighting，curriculum 做 ordering。
- **In literature_map.yaml**: NO — **可选添加**

---

## Category 7: Data Quality & Filtering

### 7.1 Nait Saada et al. — The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining
- **Year**: 2025 | **ArXiv**: 2510.00866
- **Relation**: **BACKGROUND** — 质疑分类器质量评分的有效性。提醒 q 不等于真实质量。
- **In literature_map.yaml**: YES

### 7.2 Penedo et al. — The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale
- **Authors**: Guilherme Penedo et al. (HuggingFace)
- **Year**: 2024 | **Venue**: arXiv / NeurIPS 2024 Datasets Track
- **ArXiv**: 2406.17557
- **Method**: 15T tokens 的 web pretraining 数据集。多阶段过滤：语言分类 → URL 过滤 → 启发式过滤 → 去重。FineWeb-Edu 用 Llama3-70B 评分教育质量。
- **Relation**: **BACKGROUND** — 我们的实验用 FineWeb subset。需在 paper 中引用作为数据来源。
- **In literature_map.yaml**: NO — **建议添加（实验基础设施）**

### 7.3 Xie et al. — Training Data Provenance Verification: Did Your Model Use Synthetic Data?
- **Authors**: Yuechen Xie et al.
- **Year**: 2025 | **Venue**: CVPR 2025
- **ArXiv**: 2503.09122
- **Method**: TrainProVe 通过假设检验验证模型是否使用了特定生成模型的合成数据训练。99%+ 准确率。
- **Relation**: **BACKGROUND** — "provenance" 的另一层含义（溯源验证 vs 训练加权）。我们可在 intro 中区分。
- **In literature_map.yaml**: NO — **可选添加（区分 provenance 含义）**

---

## Category 8: Detection Methods (检测器相关)

### 8.1 Mitchell et al. — DetectGPT
- **Year**: 2023 | **Venue**: ICML 2023
- **In literature_map.yaml**: YES

### 8.2 Shi et al. — Min-K% Prob (Detecting Pretraining Data from LLMs)
- **Year**: 2024 | **Venue**: ICLR 2024
- **In literature_map.yaml**: YES

### 8.3 Kuo et al. — Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification
- **Year**: 2024 | **Venue**: arXiv
- **In literature_map.yaml**: YES

---

## Summary: Priority Additions to literature_map.yaml

### Must-Add (直接竞争者或重要对比方法，related work 必须讨论)

| Paper | Category | Why |
|-------|----------|-----|
| DoGE (Fan et al., ICML 2024) | domain-level reweighting | 用户指定的对比方法之一，域级 reweighting 代表 |
| MATES (Yu et al., NeurIPS 2024) | instance-level selection | 用户指定的对比方法之一，online adaptive 的直接对比 |
| DsDm (Engstrom et al., ICML 2024) | instance-level selection | 用户指定的对比方法之一，datamodels 代表 |
| PDS (Gu et al., ICLR 2025 Oral) | principled selection | 最优控制理论的 principled 方法，需对比理论优雅度 |
| RegMix (Liu et al., ICLR 2025 Spotlight) | domain mixing | 域混合优化 SOTA，Related work 域级方法代表 |
| Kazdan et al. (ICML 2025) | model collapse theory | 累积 vs 替换理论，soft reweighting 的理论支持 |
| Dohmatob et al. Collapse or Thrive (ICML 2025) | model collapse theory | 与上文互补，三种工作流分析 |
| Demystifying Synthetic Data (EMNLP 2025) | synthetic data scaling | 大规模实证，同 venue (EMNLP)，reviewer 可能熟悉 |
| FineWeb (Penedo et al., 2024) | dataset | 实验数据来源 |

### Should-Add (丰富 related work 的补充方法)

| Paper | Category | Why |
|-------|----------|-----|
| Group-MATES (Yu et al., NeurIPS 2025) | group selection | group-level influence 新视角 |
| Quad (Zhang et al., ICLR 2025) | quality+diversity | 双重标准选择，与我们双约束有哲学共鸣 |
| QuaDMix (ByteDance, 2025) | quality+diversity | 统一框架 |
| Clustered IS (Grangier et al., ICLR 2025) | importance sampling | IS 在预训练中的方法论参考 |
| ESS as Entropy (Elvira et al., 2025) | ESS theory | ESS 的理论背景扩展 |

### Optional (扩展引用池)

| Paper | Category | Why |
|-------|----------|-----|
| IW for LLM Self-Improve (AAAI 2025) | importance weighting | IW 在 LLM 中的新应用 |
| Curriculum Learning (2025) | data ordering | 数据优化的相关维度 |
| TrainProVe (CVPR 2025) | provenance verification | 区分 provenance 含义 |
| Scaling Laws for Optimal Mixtures (Apple, 2025) | scaling laws | 域混合的 scaling law 视角 |

---

## Key Positioning Insights for Related Work Section

### 1. Instance-Level vs Domain-Level 
- 域级: DoReMi, DoGE, RegMix, Data Mixing Laws, Scaling Laws for Mixtures
- 实例级: DSIR, DsDm, MATES, PDS, SoftDedup, **Ours**
- **我们的区分**: 实例级且基于 provenance (检测器置信度)，不是 loss-based 或 influence-based

### 2. Online/Adaptive vs Offline/Static
- Offline: DSIR, DsDm, D4, PDS, RegMix
- Online: DoReMi, MATES, Dynamic Loss Reweighting, **Ours**
- **我们的区分**: per-batch adaptive b*，无需 proxy model 或 validation set

### 3. Contamination-Aware vs Quality-Oriented
- Quality: DSIR, D4, FineWeb, QuaDMix, PDS
- Contamination: Drayson, Golden Ratio, Beyond Collapse, **Ours**
- **我们的区分**: 唯一同时做 principled b* 推导 + contamination-aware + online adaptive

### 4. Hard Filtering vs Soft Reweighting
- Hard: Beyond Collapse (verifier), D4 (dedup), FineWeb (quality filter)
- Soft: Drayson (SIR), SoftDedup (commonness), Dynamic Loss, **Ours (loss reweighting)**
- **我们的区分**: continuous loss reweighting vs Drayson 的 SIR (离散重采样)

### 5. Model Collapse Theory Chain
Shumailov (Nature 2024) → MAD (ICLR 2024) → Strong Collapse (ICLR 2025) → Is Collapse Inevitable (ICML 2025) → Collapse or Thrive (ICML 2025) → Demystifying Synthetic (EMNLP 2025)
- 趋势：从 "collapse 不可避免" 到 "有条件可避免"（累积、验证、加权）
- **我们在这条链上的位置**: 提供 principled adaptive 加权方案
