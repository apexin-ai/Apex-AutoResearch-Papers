# Literature Scan Report — 2026-05-16

**Project:** provenance_weight_training  
**目标会议:** EMNLP 2026 ARR May 25 (DDL: 9 days)  
**扫描范围:** 2025.06–2026.05, 重点 arXiv preprints + ICLR 2025/2026, ICML 2025, NeurIPS 2025, EMNLP 2025, ACL 2025

---

## 1. Novelty Threat Assessment

### 🟢 无直接威胁

经过全面搜索，**未发现任何论文做了与我们完全相同的事情**（即：在 w=(1-q)^b 公式上通过 α_eff + ESS dual constraint 推导 per-batch adaptive b*）。Drayson et al. 仍是最近的 direct competitor，已在 literature_map 中。

### 🟡 需要关注的间接威胁

| 论文 | 威胁点 | 为何不构成直接威胁 |
|------|--------|-------------------|
| Subramanyam et al. 2025 (Scaling Laws Revisited) | 用 ESS + 信息论动机建模数据质量 Q | 目标是 scaling law 预测，不做 instance-level reweighting，不涉及检测器 |
| LiLAW (2025) | 3参数自适应权重，处理 synthetic data | 基于 loss difficulty 的 meta-learning，不用检测器概率，不推导理论最优解 |
| Amin et al. 2025 (Escaping Collapse) | Boosting-inspired 理论：minimal curation 即可避免 collapse | 证明 existence，不提供具体加权公式或 b 选取机制 |

---

## 2. 新发现的相关论文

### 2.1 High Priority — 建议新增引用

#### (1) Subramanyam, Chen & Grossman 2025
- **Title:** Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining
- **Venue:** arXiv preprint (under review, ICLR 2026 OpenReview)
- **URL:** https://arxiv.org/abs/2510.03313
- **Category:** theoretical-foundation
- **关系:** 用 effective-sample-size 和信息论视角建模数据质量参数 Q，提出 quality-aware scaling law。与我们的 α_eff(b) 共享 ESS 理论动机。
- **引用建议:** ✅ 必须引用。在 Related Work 中作为 "ESS-based data quality formalization" 引用，强调我们是 instance-level adaptive 而他们是 corpus-level static。
- **Differentiation:** 他们的 Q 是 corpus-level 静态参数（用于预测 loss），我们的 α_eff(b) 是 per-batch 动态量（用于选 b*）；他们不涉及检测器或加权公式。

#### (2) Amin et al. 2025
- **Title:** Escaping Collapse: The Strength of Weak Data for Large Language Model Training
- **Venue:** NeurIPS 2025
- **URL:** https://arxiv.org/abs/2502.08924
- **Category:** theoretical-foundation
- **关系:** Boosting-inspired 理论证明 nearly minimal curation 即可避免 collapse。为我们的 "lightweight detector sufficiency" claim 提供理论支撑。
- **引用建议:** ✅ 强烈建议引用。支撑我们的 Claim "even weak detectors (TF-IDF+LR) suffice"。

#### (3) Kang et al. 2025
- **Title:** Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls
- **Venue:** EMNLP 2025
- **URL:** https://arxiv.org/abs/2510.01631
- **Category:** background
- **关系:** 1000+ LLM 实验揭示合成数据 mixing 最佳比例 ~30%，rephrased 数据不导致 collapse 但 textbook-style 会。为我们的 contamination setting 提供 empirical context。
- **引用建议:** ✅ 建议引用。在 Introduction 中说明 synthetic data 在 pretraining 中的规模和风险。

#### (4) Kazdan et al. 2025
- **Title:** Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World
- **Venue:** ICML 2025
- **URL:** https://arxiv.org/abs/2410.16713
- **Category:** background
- **关系:** 系统分析 replace/accumulate/fixed-size 三种 workflow 下 synthetic data 的影响。我们的场景是 "unknown contamination in accumulated web data"。
- **引用建议:** ✅ 建议引用。Background section 引述不同 data workflow 设置。

#### (5) Martino et al. 2025/2026
- **Title:** Effective Sample Size Approximations as Entropy Measures
- **Venue:** Computational Statistics, Vol. 40, 2025 (arXiv: 2602.22954)
- **URL:** https://arxiv.org/abs/2602.22954
- **Category:** theoretical-foundation
- **关系:** 分析 ESS 与 Rényi/Tsallis 熵族的关系，提出多种 ESS 度量。直接服务于我们的 ESS stability constraint 理论基础。
- **引用建议:** ✅ 建议引用。在 Method section 讨论 ESS 约束时引用，强化 ESS 理论的严谨性。

#### (6) Grangier, Fan, Seto & Ablin 2025 (CRISP)
- **Title:** Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2410.03735
- **Category:** method-component
- **关系:** Clustered IS for pretraining distribution matching。与 Drayson 的 SIR 和 Xie 的 DSIR 在方法论上相关——同属 importance sampling 用于 pretraining。
- **引用建议:** ✅ 建议引用。Related Work 的 importance sampling for pretraining 段落。

### 2.2 Medium Priority — 可选引用

#### (7) ToReMi (Zhu et al. 2025)
- **Title:** ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data Selection
- **Venue:** arXiv preprint (2504.00695)
- **URL:** https://arxiv.org/abs/2504.00695
- **Category:** method-component
- **关系:** Topic-level 动态重加权（两阶段：先 loss-based 后 topic-aware），与我们的 instance-level provenance-based 互补。
- **引用建议:** 可选。如需展示 "dynamic reweighting" 是活跃方向可引。
- **Differentiation:** Topic-level granularity, loss-driven（不用检测器），无 ESS 约束。

#### (8) QuaDMix (ByteDance, 2025)
- **Title:** QuaDMix: Quality-Diversity Balanced Data Selection for Efficient LLM Pretraining
- **Venue:** arXiv preprint (2504.16511)
- **URL:** https://arxiv.org/abs/2504.16511
- **Category:** method-component
- **关系:** 多质量标准 + diversity 的统一选择框架，用 proxy model + LightGBM 回归预测性能。
- **引用建议:** 可选。如需 broader data selection 对比。

#### (9) LiLAW (Morales et al. 2025)
- **Title:** LiLAW: Lightweight Learnable Adaptive Weighting to Meta-Learn Sample Difficulty
- **Venue:** arXiv preprint (2509.20786, updated 2026.03)
- **URL:** https://arxiv.org/abs/2509.20786
- **Category:** method-component
- **关系:** 3 可学习参数做 sample-adaptive weighting，应用于 synthetic data 和 noisy training。
- **引用建议:** 可选。如需讨论 "adaptive weighting without detection" 替代方案。
- **Differentiation:** Meta-learning（需验证集），不基于 provenance/detection，不同理论动机。

#### (10) Schaeffer et al. 2025
- **Title:** Position: Model Collapse Does Not Mean What You Think
- **Venue:** arXiv preprint (2503.03150)
- **URL:** https://arxiv.org/abs/2503.03150
- **Category:** background
- **关系:** 指出 model collapse 有 8 种定义，某些 collapse 场景在现实条件下可避免。
- **引用建议:** 可选。如在 Discussion 中讨论 collapse 定义的 nuance。

#### (11) Beyond Surface-Level Similarity (2025)
- **Title:** Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models
- **Venue:** arXiv preprint (2511.17602)
- **URL:** https://arxiv.org/abs/2511.17602
- **Category:** background
- **关系:** 4层级 contamination detection（token/semantic/reasoning/performance cliff）。与我们的检测器组件相关。
- **引用建议:** 可选。如讨论检测器泛化性问题。

#### (12) Gerstgrasser et al. 2024
- **Title:** Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data
- **Venue:** ICML 2024
- **URL:** https://arxiv.org/abs/2404.01413
- **Category:** background
- **关系:** 证明 data accumulation 避免 collapse（test error 有限上界）。我们的场景是 web data 自然积累。
- **引用建议:** 可选。Background section 引用。

### 2.3 Low Priority — 知道即可

| 论文 | 关系 |
|------|------|
| Quad (ICLR 2025) - Harnessing Diversity for Important Data Selection | Domain-level influence + diversity, 不涉及 contamination |
| Curió-Edu 7B (arxiv 2512.12770) - Data Selection for Continued Pretraining | 教育领域 case study |
| ProX (ICLR 2025) - Programming Every Example | 数据清洗/重写，不做 reweighting |

---

## 3. 已有文献状态确认

以下已在 literature_map.yaml 中的论文经搜索确认信息准确，无需更新：
- Drayson et al. 2025 ✓
- He 2025 Golden Ratio ✓
- Feng 2025 Beyond Collapse ✓
- Sow et al. 2025 Dynamic Reweighting (ICLR 2025) ✓
- Dohmatob et al. 2025 Strong Collapse (ICLR 2025) ✓
- Chen et al. 2025 Aioli (ICLR 2025) ✓

---

## 4. 行动建议

### 必须做（DDL 前）
1. **新增 5-6 篇引用**（上述 High Priority #1-6），重点是 Subramanyam 2025 和 Amin 2025
2. 在 Related Work 中增加一段 "ESS-based Quality Formalization"，讨论 Subramanyam 的 corpus-level Q 与我们 per-batch α_eff(b) 的区别
3. 在 Introduction 引用 Kang 2025 和 Kazdan 2025 强化问题动机

### 可选做
- 引用 LiLAW/ToReMi 作为 "alternative adaptive weighting" 对比
- 引用 Martino 2025 强化 ESS 理论

### Novelty 声明建议
论文中可以自信声明：
> "To our knowledge, we are the first to derive a per-batch adaptive b* for the (1-q)^b weighting scheme via dual α_eff/ESS constraints, eliminating the need for validation-based grid search (Drayson et al. 2025) or fixed corpus-level quality parameters (Subramanyam et al. 2025)."

---

## 5. 总结

| 类别 | 数量 |
|------|------|
| 新发现相关论文 | 12 |
| 建议必须引用 | 6 |
| 可选引用 | 6 |
| Novelty 直接威胁 | 0 |
| Novelty 间接威胁 | 3（均已有清晰 differentiation）|

**结论：我们的核心贡献（dual-constraint adaptive b*）在 2025-2026 文献中仍具独特性。无直接 novelty 威胁。建议补充 5-6 篇最新引用以展示 awareness。**
