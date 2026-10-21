# Related Work 完整性审查

审查日期: 2026-05-14
审查范围: `related_work.tex` (54行, 5个段落)

---

## 已覆盖

### Model Collapse and Recursive Generation
- Shumailov et al. (2024, Nature): line 6, tail-distribution degradation
- Alemohammad et al. (2024, ICLR): line 7, self-consuming models, fixed point convergence
- Dohmatob et al. (2024, ICML): line 8, scaling laws for tail loss
- Schaeffer et al. (2025, ICML): line 9-10, 8-definition taxonomy, K* 与 Family B 对齐
- Kazdan et al. (2025, ICML): line 11-12, replace vs accumulate regimes
- Shi et al. (2025, NeurIPS Spotlight): line 13, generalization-to-memorization transition
- Amin et al. (2025, NeurIPS): line 47, weak signals suffice to escape collapse
- Gambetta et al. (2025): line 48, surplexity metric

### Binary Synthetic Text Detection
- GLTR (Gehrmann et al. 2019): line 18, token-level likelihood visualization
- Grover (Zellers et al. 2019): line 19, generator-as-detector
- Ippolito et al. (2020): line 19, detection difficulty vs generation quality
- DetectGPT (Mitchell et al. 2023): line 20, probability curvature
- Binoculars (Hans et al. 2024): line 21, cross-perplexity ratio
- DivEye (Basani et al. 2026): line 22, surprisal diversity
- Min-K%++ (Zhang et al. 2024): line 22, outlier token likelihoods
- CoDeC (Zawalski et al. 2026): line 23, in-context learning contamination detection

### Ordinal Classification
- CORAL (Cao et al. 2020): line 32-33, rank-consistent ordinal regression

### Data Selection and Curation
- DSIR (Xie et al. 2023): line 40, importance resampling
- D4 (Tirumala et al. 2023): line 41, deduplication + diversification
- DoReMi (Xie et al. 2023): line 41, domain weight optimization
- Drayson et al. (2025): line 44-46, binary detection + SIR (positioned as special case of our framework)

### Watermarking
- Kirchenbauer et al. (2023): line 52-53, statistical watermarking

---

## 需要补充

### 1. [高优先] Probing Classifiers 文献 — 支撑 Neural Probe 实验

**Gap**: discussion.tex (lines 29-35, 123-129) 和 conclusion.tex (line 45) 大量讨论 frozen-encoder + MLP probe 实验，但 Related Work 中完全没有 probing classifiers 的文献支撑。审稿人会质疑方法选择的依据。

**建议**: 在 Ordinal Classification 段落之后新增一个段落，或在 Ordinal Classification 段末追加 2-3 句。

**需要引用**:
- Alain & Bengio (2017), "Understanding intermediate layers using linear classifier probes" — 提出用线性探针分析网络中间表征，是 frozen-encoder probing 的方法论基础
- Conneau et al. (2018), "What you can cram into a single $&!#* vector: Probing sentence embeddings for linguistic properties" (ACL) — 系统研究 sentence embedding 编码了哪些语言学属性
- Belinkov (2022), "Probing Classifiers: Promises, Shortcomings, and Advances" (CL) — probing 方法的综述，讨论了 probe 复杂度与结论有效性的权衡

**建议文本**:

> \paragraph{Probing Classifiers.}
> Linear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\cite{alain2017understanding,conneau2018probing}.
> Belinkov~\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.
> Our neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects information present in the representations rather than learned de novo.

### 2. [中优先] Fast-DetectGPT — Binary Detection 段落补充

**Gap**: DetectGPT 已引用，但其改进版 Fast-DetectGPT 在 2024 年成为 zero-shot 检测的新 SOTA，被广泛引用。

**建议**: 在 line 20 (DetectGPT 之后) 追加一句。

**需要引用**:
- Bao et al. (2024), "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature" (ICLR 2024)

**建议文本**: 在 Mitchell et al. 句后加:

> Bao et al.~\cite{bao2024fastdetectgpt} improved efficiency by replacing perturbation sampling with conditional probability curvature, achieving comparable accuracy with orders-of-magnitude speedup.

### 3. [中优先] Gerstgrasser et al. (2024) — Model Collapse 理论补充

**Gap**: 现有 model collapse 覆盖全面，但缺少 Gerstgrasser et al. 关于 collapse 可避免条件的理论分析。该工作与本文的 data curation 动机直接相关——他们证明保留足够的原始数据可以避免 collapse，本文的 depth-aware filtering 正是实现这一点的工具。

**建议**: 在 line 13 (Shi et al.) 之后追加一句。

**需要引用**:
- Gerstgrasser et al. (2024), "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" (arXiv 2404.01413)

**建议文本**:

> Gerstgrasser et al.~\cite{gerstgrasser2024inevitable} proved that collapse is avoidable when sufficient original data is retained alongside synthetic samples, a condition that depth-aware curation can enforce by construction.

### 4. [低-中优先] Ordinal Classification 补充

**Gap**: 仅引用 CORAL 一篇。Ordinal classification 是本文方法的核心组件（OBD head），仅一篇引用显得单薄。

**建议**: 在 CORAL 引用后追加 1-2 篇经典方法。

**需要引用**:
- Frank & Hall (2001), "A Simple Approach to Ordinal Classification" (ECML) — 将 ordinal 问题分解为一系列二分类的开创性工作，与 OBD head 的 boundary detection 思路直接对应
- Diaz & Marathe (2019), "Soft Labels for Ordinal Regression" (CVPR) — soft label 方法，与 OBD 的 monotonic probability 设计相关

**建议文本**: 在 line 33 CORAL 句后追加:

> The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \& Hall~\cite{frank2001ordinal}; our OBD head follows this principle by learning $K\!-\!1$ cumulative boundary classifiers.

---

## 可选改进

### 1. Self-Refinement 文献补充

**理由**: Related Work line 27 提到 "beneficial recursive generation (e.g., self-refinement)" 但没有引用。添加一篇可以增强论点。

**建议引用**: Madaan et al. (2023), "Self-Refine: Iterative Refinement with Self-Feedback" (NeurIPS 2023)

**位置**: line 27, 将 "self-refinement" 处加引用即可。

### 2. Trained/Fine-tuned 检测器覆盖

**理由**: Binary Detection 段落偏重 zero-shot 和 statistical 方法。如有 fine-tuned detector 的工作（如 OpenAI text classifier, Ghostbuster），可以在 line 19 附近用一句话覆盖 supervised 检测方向，说明本文的 ordinal approach 与之的关系。但这不是必须的，因为本文聚焦 post-hoc 无训练数据场景。

### 3. Multi-class AI Text Attribution

**理由**: 有一些工作不只做二分类，而是区分不同 LLM 生成的文本（source attribution）。与本文的 ordinal depth 不同但相关。如果空间允许可以提一句以示区分。

**建议引用**: Uchendu et al. (2020), "Authorship Attribution for Neural Text Generation" (EMNLP)

### 4. Data Contamination (Benchmark) 文献

**理由**: CoDeC 已覆盖 benchmark contamination detection，但该方向有更多工作（Golchin & Surdeanu 2024, Oren et al. 2024）。不过本文的 "contamination" 指 recursive generation contamination 而非 benchmark data leakage，过多引用可能造成混淆。现有覆盖已足够。

---

## 总结

| 类别 | 状态 | 行动 |
|------|------|------|
| Model collapse | ✅ 充分 | 可选补 Gerstgrasser (collapse avoidability) |
| Binary detection | ✅ 充分 | 可选补 Fast-DetectGPT |
| Ordinal classification | ⚠️ 偏薄 | 建议补 Frank & Hall |
| Data selection | ✅ 充分 | 无需补充 |
| Watermarking | ✅ 充分 | 无需补充 |
| **Probing classifiers** | ❌ **缺失** | **必须补充** — neural probe 实验缺文献支撑 |

**最高优先级**: 补充 Probing Classifiers 段落（Alain & Bengio 2017, Conneau et al. 2018, Belinkov 2022），直接支撑 discussion.tex 中的 neural probe 实验设计。
