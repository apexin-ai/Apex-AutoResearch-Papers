# Related Work Survey: Model Collapse Detection & Data Mixing

> 调研日期：2026-05-14 | 调研范围：2024-2026（含少量经典工作）

## 1. Representation Diversity 检测 Collapse

| 论文 | 会议/年份 | 核心方法 | 与我们的关系 |
|------|-----------|----------|-------------|
| Jha & Reagen, "Spectral Scaling Laws in Language Models" | EMNLP 2025 | Hard Rank / Soft Rank / Spectral Utilization Index 量化 FFN 对 latent space 的利用率；发现 soft rank 随 width 呈 power law，hard rank 增长亚线性 | **最直接相关**。他们发现宽 FFN 大量 latent directions 未被利用（spectral concentration），但这衡量的是 model capacity utilization，不是 iterative collapse。我们的 negative result 进一步说明：即使 spectral metrics 能捕捉 capacity 问题，也未必能检测 generative collapse |
| "On the Spectral Flattening of Quantized Embeddings" | arXiv 2602.00969 (2025) | 量化引入噪声 floor → 截断 SV 谱尾 → stable rank 上升 → representational collapse | **有趣的反面发现**：他们发现 effective rank 上升反而意味着 collapse（因为丧失了语义区分能力）。这与我们观察到的 "collapse 时 eff_rank 反升" 现象一致，支持我们的 negative result |
| Gambetta et al., "Learning by Surprise: Surplexity for Mitigating Model Collapse" | arXiv 2410.12341 (2024) | 提出 surplexity（模型对数据的"surprise"程度）作为 collapse 指标和数据筛选标准；不需区分 human/AI 数据 | **替代 spectral metrics 的候选检测方案**。Surplexity 本质是基于 perplexity 的变体，与我们发现的 "n-gram entropy 比 spectral eff_rank 更有效" 一致 |
| Gambetta et al., "Characterizing Model Collapse Using Semantic Networks and Next-Token Probability" | arXiv 2410.12341v2 (2024) | 语义网络（图结构分析重复性/多样性）+ next-token 概率分布演化来量化 collapse | 提供了比 linguistic diversity metrics 更深入的 collapse 刻画方法，但未使用 spectral 方法 |
| Shi et al., "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective" | NeurIPS 2025 Spotlight | 识别 collapse 中 generalization→memorization 转变；合成训练数据熵值下降是关键 indicator；提出 entropy-based data selection 缓解方案 | **重要对照**。他们也发现 entropy（而非 spectral metrics）是有效的 collapse 指示器，与我们结论一致 |
| "Preventing Dimensional Collapse in Self-Supervised Learning via Orthogonality Regularization" | NeurIPS 2024 | eigenvalue domination → dimensional collapse；对 encoder 的 weight matrices 施加正交正则化防止 collapse | 虽然是 SSL 场景，但验证了 spectral methods 在 *preventive*（非 detective）角色的有效性 |
| Qiu et al., "Scaling Collapse Reveals Universal Dynamics" | ICML 2025 | Compute-optimal 训练下 loss 曲线归一化后 collapse 到 universal curve（"supercollapse"） | 此 "collapse" 指 loss 曲线的 universal scaling，非 generative collapse。但其 spectral power-law 分析框架可参考 |
| "Small Singular Values Matter: A Random Matrix Analysis of Transformer Models" | arXiv 2410.17770 (2024) | 用 RMT 分析 pretrained transformer 的权重谱；发现小 SV 包含重要信息，移除会增加 perplexity | 支持 SV 分布与模型质量相关，但未直接研究 iterative collapse 场景 |
| Zhai et al., "Stabilizing Transformer Training by Preventing Attention Entropy Collapse" | ICML 2023 | Attention entropy 与权重矩阵 spectral norm 直接关联；attention entropy collapse 导致训练不稳定 | 经典工作。关注的是 training stability 而非 synthetic data collapse，但确立了 entropy-spectral 连接 |

### 关键发现

- **没有工作成功用 spectral effective rank 检测 iterative model collapse**。现有 spectral 工作要么关注 model capacity（Jha & Reagen），要么关注 quantization degradation，要么关注 SSL dimensional collapse。
- **Spectral Flattening 论文**发现 effective rank 上升 = representational collapse，与我们的观察（collapse 时 holdout eff_rank 反升）高度一致，是支持我们 negative result 的关键证据。
- **Entropy-based 指标**（surplexity、n-gram entropy、训练数据熵）被多个独立工作验证为更有效的 collapse 检测手段。
- 我们的 negative result（spectral eff_rank 与 generative collapse 解耦）在文献中是**独特贡献**，没有发现矛盾的工作。

---

## 2. Data Mixing 应对 Synthetic Data Pollution

| 论文 | 会议/年份 | 核心方法 | 与我们的关系 |
|------|-----------|----------|-------------|
| Shumailov et al., "AI Models Collapse When Trained on Recursively Generated Data" | Nature 2024 | 首次系统证明 recursive training on synthetic data → distribution tail 消失 → model collapse；在 LLM、VAE、GMM 上验证 | **领域奠基论文**，定义了我们要解决的问题 |
| Dohmatob & Feng, "Strong Model Collapse" | ICLR 2025 | 证明即使 0.1% 的 synthetic data 也可导致 collapse；larger models amplify collapse | 警示信号：说明即使小比例 synthetic 污染也需要主动应对机制 |
| Schaeffer et al., "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" | arXiv 2404.01413 (2024) | Replace 场景必然 collapse；Accumulate（保留全部 real + synthetic）可避免 collapse，test error 有有限上界 | 为 mixing 策略提供理论基础：关键是 accumulate 而非 replace |
| Kazdan et al., "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World" | ICML 2025 | 三种 workflow（Replace / Accumulate / Fixed Compute）的系统比较；Fixed Compute 介于两者之间 | 最贴近现实的分析框架；Fixed Compute 场景正是我们 adaptive mixing 的动机 |
| "Escaping Model Collapse via Synthetic Data Verification" | arXiv 2510.16657 (2025) | 引入外部 verifier 过滤低质量 synthetic data；near-term improvements + long-term convergence 保证 | 验证策略可与我们的 collapse-aware mixing 互补 |
| "How Bad is Training on Synthetic Data? A Statistical Analysis" | arXiv 2404.05090 (2024) | 给出 synthetic data 最大安全比例的理论估计；纯 synthetic 必然 collapse | 为我们的 PI 控制器设定 mixing ratio 上界提供理论依据 |
| Kang et al., "Demystifying Synthetic Data in LLM Pre-training" | EMNLP 2025 | 1000+ LLM 实验；rephrased data 1/3 mixed 可 5-10x 加速；textbook-style synthetic 单独训练出现 collapse 模式 | **重要实证参考**。区分了 synthetic data 类型对 collapse 的不同影响 |
| El Firdoussi et al., "Maximizing the Potential of Synthetic Data" | ICLR 2025 | Random Matrix Theory 分析 real+pruned synthetic 混合分类器性能；给出 synthetic data 改善性能的条件 | 理论方法与我们的 spectral 分析思路有共鸣，但他们用 RMT 分析 classifier 而非 generator |
| Sang et al., "Position: Model Collapse Does Not Mean What You Think" | arXiv 2503.03150 (2025), ICML 2025 invited talk | 指出 "model collapse" 包含 8 种矛盾定义；许多 collapse 场景基于不现实假设；呼吁关注 "diversity collapse" | **重要 framing 参考**。强调不同定义下结论可能矛盾，帮助我们精确定位 contribution |
| "Curated Synthetic Data Doesn't Have to Collapse" | arXiv 2605.07724 (2025) | 基于 pluralistic preferences 的多 reward function curation 防止 collapse；收敛到 Nash bargaining solution | 最新工作。提供了另一种避免 collapse 的理论框架，但需要多个 reward signals |

### 关键发现

- **Accumulate > Replace** 是最一致的结论（Schaeffer et al.、Kazdan et al.）。
- **Synthetic data 类型很重要**：rephrased data 相对安全，textbook-style 纯生成 data 危险更大（Kang et al.）。
- **即使极少量 synthetic data 也有风险**（Dohmatob & Feng），说明被动混合不够，需要**主动检测+调节**。
- "Model Collapse" 定义混乱（Sang et al.），我们的论文需要明确使用哪种定义。

---

## 3. Collapse-Aware / Adaptive Mixing

| 论文 | 会议/年份 | 核心方法 | 与我们的关系 |
|------|-----------|----------|-------------|
| Xie et al., "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining" | NeurIPS 2023 | 小 proxy model 用 Group DRO 学 domain weights → 大模型用该 weights 训练；8B 模型 2.6x training efficiency | **Adaptive mixing 先驱**。但它优化 domain-level mixing（code/law/math），不针对 real/synthetic 区分，且是 offline 优化 |
| Fan et al., "DoGE: Domain Reweighting with Generalization Estimation" | ICML 2024 | 改进 DoReMi：bi-level optimization 直接估计 domain contribution，不依赖 reference model | 比 DoReMi 更鲁棒的 domain weights，但仍是 offline、domain-level |
| Bai et al., "Aioli: A Unified Optimization Framework for Language Model Data Mixing" | ICLR 2025 | **Online** 方法：训练中实时估计 mixing law 参数并动态调节比例；6/6 datasets 超过 stratified sampling | **最接近我们的竞争工作**。Aioli 做 online adaptive mixing，但基于 loss-proportion 关系而非 collapse 检测信号。我们用 collapse metrics 驱动调节是不同的 |
| Liu et al., "RegMix: Data Mixture as Regression" | ICLR 2025 Spotlight | 训练大量小模型 → 回归预测最优混合 → 应用到大模型；10% DoReMi 算力达到同等效果 | 高效的 offline 方法，但不处理训练过程中 data 分布变化 |
| Ye et al., "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance" | ICLR 2025 | 发现 model performance 与 mixture proportions 的可预测函数关系（data mixing laws） | 理论基础工作。证明 mixing ratios 可以被 predictably 建模 |
| Xie et al., "Chameleon: A Flexible Data-mixing Framework" | ICML 2025 | Kernel Ridge Leverage Scores 量化 domain representativeness；pretraining 用 inverse KRLS，finetuning 用 KRLS | 灵活框架但仍是 domain-level（非 real/synthetic-aware），不含 collapse 检测 |
| Zeng et al., "AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization" | ACL 2025 | Specialist-generalist gap 驱动的 minimax optimization；动态调整 task-level mixing | 动态调整思路与我们类似，但面向 multi-task alignment 而非 collapse prevention |

### 关键发现

- **现有 adaptive mixing 方法全部基于 loss/performance 信号**（DoReMi 用 DRO loss，Aioli 用 mixing law parameters，RegMix 用回归预测 loss）。**没有方法使用 collapse-specific 检测信号**来驱动 mixing ratio 调节。
- **Online vs Offline**：DoReMi/DoGE/RegMix 是 offline（先学 weights 再训练），Aioli 是 online（训练中动态调）。我们的 PI 控制器方案属于 online。
- **Domain-level vs Real/Synthetic**：所有现有方法关注 domain mixing（code vs text vs math），**没有方法专门处理 real/synthetic data mixing ratio**。
- **控制论视角缺失**：没有工作将 data mixing 框架化为一个反馈控制问题（用 monitoring signal → controller → actuator 范式）。

---

## 4. 综合分析

### 当前领域的 Gap（我们的 Novelty 空间）

1. **Spectral metrics 作为 collapse detector 的 negative result**：没有其他工作系统测试并报告 spectral effective rank 对 iterative collapse 的检测失败。Spectral Flattening 论文的发现（eff_rank 上升 = collapse）间接支持我们，但他们的场景是 quantization 而非 iterative training。

2. **Real/Synthetic mixing 的 adaptive 调节**：所有现有 adaptive mixing（DoReMi/Aioli/RegMix/Chameleon）关注 domain-level mixing。没有工作专门做 real vs synthetic 比例的动态调节。

3. **Collapse-aware feedback control**：没有工作将 collapse detection 信号（无论是 spectral、entropy 还是其他）接入一个闭环控制器来动态调节训练数据配比。所有 adaptive mixing 方法用的是 loss-based 信号。

4. **Simple baselines 的重要性**：我们发现 n-gram entropy 比 spectral eff_rank 更有效，这与 Surplexity 论文（perplexity variant）和 NeurIPS 2025 论文（训练数据 entropy）的发现一致，但没有人做过系统对比。

### 最接近的竞争工作及差异

| 竞争工作 | 与我们的关键差异 |
|----------|----------------|
| **Aioli** (ICLR 2025) | Online mixing 但基于 loss-proportion law，非 collapse detection；不区分 real/synthetic |
| **Surplexity** (2024) | 用 surprise 检测 collapse data 但不做 adaptive mixing ratio 调节 |
| **Shi et al.** (NeurIPS 2025) | 用 entropy 检测 collapse 但仅做 data selection（过滤），不做 ratio 控制 |
| **Kazdan et al.** (ICML 2025) | 分析 accumulate/replace 策略但不做 adaptive 调节 |
| **Dohmatob et al.** (ICLR 2025) | 理论分析但不提供 mitigation 机制 |

### 值得引用的关键论文清单

**必引（定义问题+核心对比）：**
- Shumailov et al. (Nature 2024) — 奠基论文
- Dohmatob & Feng (ICLR 2025) — Strong Model Collapse
- Kazdan et al. (ICML 2025) — Collapse or Thrive（workflow taxonomy）
- Sang et al. (2025) — Model Collapse 定义辨析
- Aioli (ICLR 2025) — 最接近的 online adaptive mixing
- Shi et al. (NeurIPS 2025) — entropy 作为 collapse indicator

**强烈建议引（支撑 negative result + 方法论）：**
- "On the Spectral Flattening" (2025) — eff_rank 上升 = collapse（支持我们的发现）
- Jha & Reagen (EMNLP 2025) — Spectral Scaling Laws（spectral metrics baseline）
- Gambetta et al. (2024) — Surplexity（alternative detection metric）
- Schaeffer et al. (2024) — Accumulate vs Replace 理论
- Kang et al. (EMNLP 2025) — Synthetic data 类型对 collapse 的差异影响

**推荐引（broader context）：**
- DoReMi (NeurIPS 2023) — adaptive mixing 先驱
- DoGE (ICML 2024) — domain reweighting
- RegMix (ICLR 2025) — regression-based mixing
- Chameleon (ICML 2025) — flexible mixing framework
- Data Mixing Laws (ICLR 2025) — mixing 可预测性
- "How Bad is Training on Synthetic Data?" (2024) — synthetic ratio 上界理论
- "Maximizing the Potential of Synthetic Data" (ICLR 2025) — RMT 分析
- NeurIPS 2024 Dimensional Collapse — orthogonal regularization
