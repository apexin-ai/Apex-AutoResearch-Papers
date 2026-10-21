# Related Work 文献调研

## 1. Dream 审稿指出缺失的论文

### FANG: Function-Aware Neuron Grouping (arXiv Dec 2025)
- **arXiv/DOI**: arXiv:2512.23014
- **核心方法**: 按功能角色分组神经元，组内根据语义对齐程度加权 importance，共享神经元保留机制 + adaptive block-wise sparsity
- **与 RASP 的关系**: 竞品/互补。FANG 和 RASP 都利用 functional specialization 指导剪枝，但 FANG 用 neuron grouping + semantic alignment，RASP 用 CKA overlap。FANG 不考虑 recovery
- **Related Work 中怎么引**: "Concurrently, FANG (2025) groups neurons by functional roles and prunes within each group using semantically aligned importance scores, achieving SOTA structured pruning results. Unlike RASP, FANG does not consider post-pruning recoverability."
- **BibTeX key 建议**: `fang2025function`

### FuncNet: Functional Network Pruning (arXiv Aug 2025)
- **arXiv/DOI**: arXiv:2508.05239
- **核心方法**: 借鉴认知神经科学，用 ICA 分解 LLM 为 functional networks（类似大脑功能网络），保留关键功能网络中的神经元
- **与 RASP 的关系**: 互补。FuncNet 和 RASP 都关注 functional structure，但 FuncNet 用 ICA 分解，RASP 用 CKA overlap 度量
- **Related Work 中怎么引**: "FuncNet (2025) draws on cognitive neuroscience to decompose LLMs into functional networks via ICA, preserving key neurons within each network. While sharing our functional perspective, RASP uses CKA to quantify pairwise overlap rather than ICA decomposition."
- **BibTeX key 建议**: `funcnet2025pruning`

### RestoreLCC: Lost Component Compensation (NeurIPS 2025)
- **arXiv/DOI**: arXiv:2510.21834
- **核心方法**: 对比式探测关键 attention heads 的 activation differences，提取 lost components 并注入回 pruned heads 做补偿。Plug-and-play，兼容 structured/semi-structured/unstructured pruning
- **与 RASP 的关系**: 互补。RestoreLCC 做 post-pruning activation compensation，RASP 做 pre-pruning overlap-aware selection + RLVR recovery。两者可叠加
- **Related Work 中怎么引**: "RestoreLCC (NeurIPS 2025) recovers pruning loss by contrastively probing critical attention heads and reinjecting lost activation components. This plug-and-play approach is complementary to RASP's strategy of preserving functionally unique heads before pruning."
- **BibTeX key 建议**: `restorelcc2025`

### PAT: Pruning-Aware Tuning (AAAI 2025)
- **arXiv/DOI**: arXiv:2408.14721
- **核心方法**: 在 Attention 和 FFN 之间插入 Hybrid Sparsification Modules (HSMs)，含轻量算子 + 全局共享 trainable mask，Identity Loss 解耦 transformation 和 scaling
- **与 RASP 的关系**: 竞品。PAT 将 pruning 和 fine-tuning 统一，RASP 分两阶段（CKA-guided pruning → RLVR recovery）。PAT 用 SFT-like recovery，RASP 用 RL
- **Related Work 中怎么引**: "PAT (AAAI 2025) unifies pruning and fine-tuning via Hybrid Sparsification Modules with LoRA-comparable overhead. RASP differs by decoupling pruning from recovery and employing RLVR instead of supervised tuning for the recovery stage."
- **BibTeX key 建议**: `pat2025pruning`

---

## 2. 已知竞品

### Self-Healing: Recovering Pruned LRMs via RL (OpenReview Oct 2025)
- **arXiv/DOI**: OpenReview ID: Cy8Qa4gAst（未找到独立 arXiv ID）
- **核心方法**: 用 RLVR 替代 SFT 做剪枝后恢复训练。在 25% 压缩下 RLVR 将性能从 ~80%（SFT）提升到 >95%
- **与 RASP 的关系**: 最直接竞品。Self-Healing 证明 RLVR > SFT 做 recovery，但不考虑剪哪些结构。RASP 的核心贡献是 pruning selection 也要考虑 recoverability
- **Related Work 中怎么引**: "Self-Healing (2025) demonstrates that RLVR-based recovery dramatically outperforms SFT for pruned reasoning models. RASP builds on this insight by further showing that which structures are pruned significantly affects recovery efficiency—CKA-guided selection creates a more favorable starting point for RLVR."
- **BibTeX key 建议**: `selfhealing2025`

### GRASPrune: Global Gating for Budgeted Structured Pruning (ACL 2026)
- **arXiv/DOI**: arXiv:2604.19398
- **核心方法**: 联合剪枝 FFN channels 和 KV head groups，用 projected straight-through estimator 学习 gate scores，全局 budget 约束，calibration scaling factors 缓解 scale mismatch
- **与 RASP 的关系**: 竞品。GRASPrune 用 learned gating，RASP 用 CKA-based importance scoring。GRASPrune 不考虑 recovery
- **Related Work 中怎么引**: "GRASPrune (ACL 2026) jointly prunes FFN channels and KV head groups under a global budget using learned gate scores. While achieving strong one-shot pruning, it does not account for post-pruning recoverability, which RASP addresses via the functional overlap term."
- **BibTeX key 建议**: `graspprune2026`

### RESP / Think Before You Prune (Dec 2025)
- **arXiv/DOI**: arXiv:2512.02185
- **核心方法**: 自生成推理 traces 做 calibration，decode-time gradient importance，progressive regeneration。首个针对 reasoning LLMs 的 structured pruning
- **与 RASP 的关系**: 竞品。RESP 用 self-generated calibration + gradient importance，RASP 用 CKA overlap。RESP 不用 RL recovery
- **Related Work 中怎么引**: "RESP (2025) is the first to address structured pruning specifically for reasoning LLMs, using self-generated traces for calibration and decode-time gradients for importance estimation. RASP complements this line by introducing a functional overlap criterion and leveraging RLVR for recovery."
- **BibTeX key 建议**: `resp2025pruning`

### MPruner: CKA-Based Mutual Information Pruning (Aug 2024)
- **arXiv/DOI**: arXiv:2408.13482
- **核心方法**: 用 CKA 做 layer clustering，度量 multi-layer cluster 的全局贡献，accuracy threshold 而非 sparsity level 做剪枝标准。~50% 参数缩减
- **与 RASP 的关系**: 互补/背景。MPruner 也用 CKA 但做 layer-level clustering，RASP 用 CKA 做 head-level functional overlap。MPruner 不针对 reasoning models
- **Related Work 中怎么引**: "MPruner (2024) applies CKA-based layer clustering for model compression, demonstrating ~50% parameter reduction. RASP extends the use of CKA from layer-level redundancy detection to head-level functional overlap scoring, specifically targeting reasoning model recoverability."
- **BibTeX key 建议**: `mpruner2024`

---

## 3. Structured Pruning Baselines

### LLM-Pruner (NeurIPS 2023)
- **arXiv/DOI**: arXiv:2305.11627
- **核心方法**: 基于 gradient information 的 task-agnostic structural pruning，LoRA 3h 恢复。支持 LLaMA/Vicuna/ChatGLM
- **与 RASP 的关系**: 背景 baseline。经典 LLM structured pruning 方法
- **Related Work 中怎么引**: "LLM-Pruner (Ma et al., NeurIPS 2023) performs task-agnostic structural pruning based on gradient information, recovering performance via LoRA fine-tuning."
- **BibTeX key 建议**: `llmpruner2023`

### SliceGPT (ICLR 2024)
- **arXiv/DOI**: arXiv:2401.15024
- **核心方法**: 利用 computational invariance（正交变换保持预测不变），直接删除 weight matrix 的整行/列，减小 embedding dimension
- **与 RASP 的关系**: 背景 baseline
- **Related Work 中怎么引**: "SliceGPT (ICLR 2024) exploits computational invariance to slice entire rows and columns from weight matrices, reducing the embedding dimension without retraining."
- **BibTeX key 建议**: `slicegpt2024`

### Wanda (ICLR 2024)
- **arXiv/DOI**: arXiv:2306.11695
- **核心方法**: 按 weight magnitude × input activation 剪枝，per-output basis，无需 retraining
- **与 RASP 的关系**: 背景 baseline（unstructured，但 widely cited）
- **Related Work 中怎么引**: "Wanda (Sun et al., ICLR 2024) prunes by the product of weight magnitude and input activation, achieving competitive sparsity without retraining."
- **BibTeX key 建议**: `wanda2024`

### SparseGPT (ICML 2023)
- **arXiv/DOI**: arXiv:2301.00774
- **核心方法**: One-shot pruning via large-scale sparse regression，OPT-175B 和 BLOOM-176B 达 60% sparsity with negligible perplexity loss
- **与 RASP 的关系**: 背景 baseline
- **Related Work 中怎么引**: "SparseGPT (Frantar & Alistarh, ICML 2023) enables one-shot pruning of 100B+ parameter models to 60% sparsity via sparse regression."
- **BibTeX key 建议**: `sparsegpt2023`

### FLAP: Fluctuation-based Adaptive Structured Pruning (AAAI 2024)
- **arXiv/DOI**: arXiv:2312.11983
- **核心方法**: Fluctuation pruning metric + adaptive global compression + bias compensation。3-5 分钟单 GPU 完成，无需 retraining
- **与 RASP 的关系**: 背景 baseline。FANG 在 FLAP 基础上取得 SOTA
- **Related Work 中怎么引**: "FLAP (AAAI 2024) uses fluctuation-based metrics with adaptive per-layer sparsity and bias compensation for retraining-free structured pruning."
- **BibTeX key 建议**: `flap2024`

### ShortGPT: Layer Removal via Block Influence (2024)
- **arXiv/DOI**: arXiv:2403.03853
- **核心方法**: Block Influence (BI) score 度量层重要性（input/output 相似度），直接删除冗余层
- **与 RASP 的关系**: 背景。Depth pruning 方向，与 RASP 的 width pruning 互补
- **Related Work 中怎么引**: "ShortGPT (2024) identifies layer redundancy via Block Influence scores and directly removes entire layers, demonstrating significant redundancy in LLM depth."
- **BibTeX key 建议**: `shortgpt2024`

---

## 4. Reasoning LLM Pruning 专题

### From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models (Jan 2026)
- **arXiv/DOI**: arXiv:2601.18091
- **核心方法**: 首个系统比较 instruction-following LLMs vs reasoning-augmented LLMs 的 pruning 行为。Depth/width/dynamic pruning across 17 tasks
- **与 RASP 的关系**: 背景/motivation。证明 pruning strategies 不能从 LLMs 直接迁移到 LRMs
- **Related Work 中怎么引**: "Recent work (2026) reveals that pruning strategies optimized for instruction-following LLMs do not transfer to reasoning models, motivating the need for reasoning-aware pruning criteria like RASP's functional overlap score."
- **BibTeX key 建议**: `llms2lrms2026`

### When Reasoning Meets Compression (Apr 2025)
- **arXiv/DOI**: arXiv:2504.02010
- **核心方法**: Benchmark quantized/distilled/pruned DeepSeek-R1 on reasoning tasks。发现 weight count 对 knowledge memorization 影响 > reasoning，保护 2% excessively compressed weights 可提升 6.57%
- **与 RASP 的关系**: 背景/motivation。支持 RASP 的论点：不是所有 weights 对 reasoning recovery 同等重要
- **Related Work 中怎么引**: "Analysis of compressed DeepSeek-R1 (2025) shows that weight count affects knowledge memorization more than reasoning ability, and protecting a small fraction of critical weights yields outsized accuracy gains—consistent with RASP's premise that preserving functionally unique heads is key."
- **BibTeX key 建议**: `reasoning_compression2025`

### Doing More With Less: LLM Pruning for Test-Time Scaling (Apr 2026)
- **arXiv/DOI**: arXiv:2604.25098
- **核心方法**: Unstructured pruning 可增强 test-time scaling 性能，甚至优于 unpruned models。Structured pruning 则严重损害 test-time reasoning
- **与 RASP 的关系**: 背景。进一步说明 structured pruning 对 reasoning 的特殊挑战
- **Related Work 中怎么引**: "Recent findings (2026) show that while unstructured pruning can enhance test-time scaling, structured pruning severely degrades reasoning—underscoring the need for careful structure selection as in RASP."
- **BibTeX key 建议**: `doingmorewithless2026`

---

## 5. RLVR / GRPO 基础

### DeepSeek-R1: Incentivizing Reasoning via RL (Jan 2025)
- **arXiv/DOI**: arXiv:2501.12948
- **核心方法**: 纯 RL (GRPO) 激励 reasoning emergence：self-reflection, verification, dynamic strategy adaptation。开源 R1-Zero, R1, 6 个 distilled models
- **与 RASP 的关系**: 基础。RASP 的目标模型（DeepSeek-R1-Distill-Qwen-7B）和 recovery 方法（GRPO）均来自此
- **Related Work 中怎么引**: "DeepSeek-R1 (2025) demonstrates that pure RL with GRPO can incentivize advanced reasoning patterns in LLMs, producing the distilled models we use as our base for pruning."
- **BibTeX key 建议**: `deepseekr1_2025`

### DeepSeekMath: GRPO Origin (Feb 2024)
- **arXiv/DOI**: arXiv:2402.03300
- **核心方法**: 引入 GRPO（Group Relative Policy Optimization），去掉 value network，用 group-relative advantage estimation 替代 PPO 的 critic
- **与 RASP 的关系**: 基础。GRPO 是 RASP recovery 阶段的核心算法
- **Related Work 中怎么引**: "GRPO (Shao et al., 2024), originally introduced in DeepSeekMath, replaces the value network in PPO with group-relative advantage estimation, forming the basis for RLVR-based recovery in our framework."
- **BibTeX key 建议**: `deepseekmath2024`

### RL Squeezes, SFT Expands (ICLR 2026)
- **arXiv/DOI**: arXiv:2509.21128
- **核心方法**: RL 压缩 incorrect trajectories（集中到 hub nodes），SFT 扩展 correct trajectories（均匀化）。RL 使 reasoning graph 更高效
- **与 RASP 的关系**: 理论支撑。解释为什么 RLVR recovery 比 SFT recovery 更有效——RL 压缩错误路径而非简单模仿
- **Related Work 中怎么引**: "RL Squeezes, SFT Expands (ICLR 2026) reveals that RL concentrates reasoning into efficient hub structures while SFT disperses it, providing theoretical grounding for why RLVR-based recovery outperforms SFT in RASP."
- **BibTeX key 建议**: `rlsqueezes2026`

---

## 6. CKA 及表征相似性度量

### Kornblith et al.: CKA 原始论文 (ICML 2019)
- **arXiv/DOI**: arXiv:1905.00414
- **核心方法**: 提出 CKA，基于 centered Gram matrices + HSIC。Invariant to orthogonal transform + isotropic scaling。99.3% layer correspondence accuracy vs CCA 的 1.4%-45.4%
- **与 RASP 的关系**: 基础。RASP 的 F(h) functional overlap 基于 CKA
- **Related Work 中怎么引**: "Centered Kernel Alignment (Kornblith et al., ICML 2019) measures representational similarity via the Hilbert-Schmidt Independence Criterion on centered Gram matrices, achieving 99.3% accuracy in identifying corresponding layers across networks—far surpassing CCA variants."
- **BibTeX key 建议**: `kornblith2019cka`

### SVCCA (NeurIPS 2017)
- **arXiv/DOI**: arXiv:1706.05806
- **核心方法**: SVD 降维 + CCA 做 affine-invariant 表征比较。揭示网络 bottom-up 收敛、过参数化等
- **与 RASP 的关系**: CKA 的前驱方法，用于 CKA 选择论证
- **Related Work 中怎么引**: "SVCCA (Raghu et al., NeurIPS 2017) combines SVD with CCA for affine-invariant representation comparison but fails to identify layer correspondences across different initializations—a limitation that CKA overcomes."
- **BibTeX key 建议**: `raghu2017svcca`

### PWCCA: Projection Weighted CCA (NeurIPS 2018)
- **arXiv/DOI**: arXiv:1806.05759
- **核心方法**: 用 projection weights 替代 mean CCA coefficient，给 better-explaining components 更高权重
- **与 RASP 的关系**: CKA alternative，用于论证
- **Related Work 中怎么引**: "PWCCA (Morcos et al., NeurIPS 2018) improves upon SVCCA by weighting CCA components by their projection importance, but remains sensitive to the number of retained dimensions."
- **BibTeX key 建议**: `morcos2018pwcca`

### Reliability of CKA (ICLR 2023)
- **arXiv/DOI**: arXiv:2210.16156
- **核心方法**: 形式化分析 CKA 对 simple transformations 的敏感性，证明 CKA 值可被操纵而不改变模型功能行为
- **与 RASP 的关系**: 重要反面论据。需在论文中 acknowledge CKA limitations 并论证为何在 RASP 场景下仍合理
- **Related Work 中怎么引**: "Davari et al. (ICLR 2023) show that CKA can be manipulated without changing functional behavior, cautioning against uncritical use. In RASP, we mitigate this by using CKA in a relative ranking setting (comparing heads within the same model) rather than absolute similarity measurement."
- **BibTeX key 建议**: `davari2023cka_reliability`

### Deceiving the CKA Measure (NeurIPS 2022 Workshop)
- **arXiv/DOI**: OpenReview ID: hITONWhDIIJ
- **核心方法**: Optimization-based approach 修改 representations 维持功能但改变 CKA 值
- **与 RASP 的关系**: 与上一篇同团队，补充 CKA limitations 讨论
- **Related Work 中怎么引**: 可与 Davari et al. 2023 合并引用
- **BibTeX key 建议**: `horoi2022deceiving_cka`

### MINE: Mutual Information Neural Estimation (ICML 2018)
- **arXiv/DOI**: arXiv:1801.04062
- **核心方法**: 基于 Donsker-Varadhan 表示的 MI 估计器。Scalable 但在高维/高 MI 场景有 bias/variance 问题
- **与 RASP 的关系**: CKA vs MI 论证素材。MI estimation 在高维不稳定，CKA 更 practical
- **Related Work 中怎么引**: "Mutual information estimation (Belghazi et al., ICML 2018) is theoretically appealing but suffers from severe bias and variance in high-dimensional settings, making CKA a more practical choice for head-level overlap quantification."
- **BibTeX key 建议**: `belghazi2018mine`

---

## 7. Taylor Importance 基础

### Molchanov et al.: Importance Estimation for Neural Network Pruning (CVPR 2019)
- **arXiv/DOI**: arXiv:1906.10771
- **核心方法**: First/second-order Taylor expansion 估计 neuron/filter 对 loss 的贡献。>93% correlation with true importance
- **与 RASP 的关系**: 基础。RASP 的 I(h) importance score 基于 Taylor approximation
- **Related Work 中怎么引**: "We estimate head importance I(h) using first-order Taylor approximation (Molchanov et al., CVPR 2019), which achieves >93% correlation with true importance across network layers."
- **BibTeX key 建议**: `molchanov2019importance`

---

## 8. CKA 选择论证素材

### CKA vs SVCCA/CCA/MI 优劣对比

| 度量 | 不变性 | Layer Correspondence Accuracy | 高维稳定性 | 计算效率 | 主要缺陷 |
|------|--------|-------------------------------|-----------|---------|---------|
| **CKA** | Orthogonal transform + isotropic scaling | 99.3% | 稳定 | 仅需内积 | 可被刻意操纵（Davari 2023）；对 outliers 敏感 |
| **SVCCA** | Orthogonal transform（近似 invertible linear） | 1.4%-45.4% | 依赖 SVD truncation threshold | 需 SVD + CCA | Threshold 选择敏感；不能捕捉 non-isotropic scaling |
| **PWCCA** | 同 SVCCA + projection weighting | 优于 SVCCA | 仍依赖 retained dimensions | 需 SVD + CCA + weighting | 继承 CCA invariance 过强的问题 |
| **CCA** | Invertible linear transform | 低 | 受样本量限制 | 需矩阵分解 | 过强的 invariance 丢失 structure；高维 > 样本数时不可靠 |
| **MI** | 无假设（nonparametric） | N/A | 极不稳定（bias/variance） | 需 neural estimator 训练 | 高维估计 heavily biased；收敛慢；不 practical |

### 论证要点

1. **CKA 优势**：在 head-level overlap 度量场景，我们需要 (a) 跨不同 heads 的 representations 可比较，(b) 对 isotropic scaling invariant 但对 non-isotropic 变化 sensitive（因为 non-isotropic 变化反映 functional specialization），(c) 高效可计算。CKA 满足所有三点。

2. **为什么不用 CCA/SVCCA**：CCA 对 invertible linear transform invariant，这意味着两个 functionally different heads 如果存在 linear mapping 就会被判为 identical——在我们的 overlap 检测场景这是 false positive。SVCCA 在 layer correspondence 上仅 1.4%-45.4% 准确率（vs CKA 99.3%），说明其 similarity signal 过于嘈杂。

3. **为什么不用 MI**：MI 在 attention head 维度（768-4096 dim per head）的高维空间中估计 heavily biased，需要大量样本和 neural estimator 训练，不 practical 也不 reproducible。

4. **Acknowledge CKA 缺陷**：CKA 可被操纵（Davari et al., 2023; Horoi et al., 2022），且对 outliers 敏感。但在 RASP 中我们用 CKA 做 relative ranking（同一模型内 heads 的 pairwise overlap），而非 cross-model absolute comparison，因此操纵风险低且 outlier 影响在 heads 间一致。

5. **Claim 2 循环性讨论**：Dream 审稿指出 "CKA predicts recoverability" 可能是 tautological。回应：CKA 度量的是 functional overlap（表征冗余度），recoverability 是 RLVR training 的 emergent outcome。两者之间的相关性是 empirical finding 而非 definitional circularity。类比：BMI 预测心血管风险不是 tautological，即使两者有 biological correlation。我们在 Section 4 提供 ablation 证明 CKA overlap ≠ trivially recoverability（e.g., random overlap scores 不预测 recovery）。

---

## 9. 引用清单（按 Related Work 子节分组）

### §2.1 Structured Pruning for LLMs
1. LLM-Pruner (Ma et al., NeurIPS 2023) — `llmpruner2023`
2. SparseGPT (Frantar & Alistarh, ICML 2023) — `sparsegpt2023`
3. Wanda (Sun et al., ICLR 2024) — `wanda2024`
4. SliceGPT (Ashkboos et al., ICLR 2024) — `slicegpt2024`
5. FLAP (AAAI 2024) — `flap2024`
6. ShortGPT (2024) — `shortgpt2024`
7. GRASPrune (ACL 2026) — `graspprune2026`
8. PAT (AAAI 2025) — `pat2025pruning`

### §2.2 Function-Aware / Representation-Guided Pruning
9. FANG (2025) — `fang2025function`
10. FuncNet (2025) — `funcnet2025pruning`
11. MPruner (2024) — `mpruner2024`

### §2.3 Pruning Reasoning LLMs
12. RESP / Think Before You Prune (2025) — `resp2025pruning`
13. Self-Healing (2025) — `selfhealing2025`
14. From LLMs to LRMs (2026) — `llms2lrms2026`
15. When Reasoning Meets Compression (2025) — `reasoning_compression2025`
16. Doing More With Less (2026) — `doingmorewithless2026`

### §2.4 Post-Pruning Recovery & RLVR
17. RestoreLCC (NeurIPS 2025) — `restorelcc2025`
18. DeepSeek-R1 (2025) — `deepseekr1_2025`
19. DeepSeekMath / GRPO (2024) — `deepseekmath2024`
20. RL Squeezes, SFT Expands (ICLR 2026) — `rlsqueezes2026`

### §2.5 Representation Similarity Measures
21. CKA (Kornblith et al., ICML 2019) — `kornblith2019cka`
22. SVCCA (Raghu et al., NeurIPS 2017) — `raghu2017svcca`
23. PWCCA (Morcos et al., NeurIPS 2018) — `morcos2018pwcca`
24. Reliability of CKA (Davari et al., ICLR 2023) — `davari2023cka_reliability`
25. Deceiving CKA (Horoi et al., NeurIPS 2022 WS) — `horoi2022deceiving_cka`
26. MINE (Belghazi et al., ICML 2018) — `belghazi2018mine`

### §2.6 Importance Estimation
27. Taylor Importance (Molchanov et al., CVPR 2019) — `molchanov2019importance`

**总计: 27 篇引用**（满足 25+ 要求）
