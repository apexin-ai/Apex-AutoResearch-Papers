# Related Work 结构笔记

> 四个 thread 的核心论文梳理，每个 thread 说明与本工作的定位关系。

---

## Thread 1: Binary Synthetic Text Detection → 我们扩展到 Ordinal Depth

**核心问题**：现有检测方法将合成文本视为 binary label（human vs. machine），忽略了代际深度这一关键维度。

**核心论文**：

1. **Min-K%++ (Zhang et al., ICLR 2025)**
   - 通过 token probability 分析检测 pre-training membership，改进了 Min-K% 基线
   - 局限：membership inference ≠ ordinal depth estimation；仅判断"是否在训练集中"，无法回答"经过了几代生成"
   - 与我们的关系：Min-K% 的 low-probability token fraction 是我们 token-level 特征的子集；我们证明这些特征可以做更细粒度的 ordinal prediction

2. **DivEye (Basani & Chen, TMLR 2026)**
   - 9 个 surprisal-based 统计特征（分布矩 + 一阶/二阶差分）用于可解释的 binary 检测，超过 zero-shot baseline 33.2%
   - 局限：纯 binary 分类，未利用特征随 depth 变化的系统性趋势
   - 与我们的关系：DivEye 的 9 维 surprisal 特征是我们特征集的核心子集；我们扩展为 ordinal regression 输入，证明同一特征集可支撑 depth 分辨

3. **DetectGPT (Mitchell et al., ICML 2023)**
   - 利用 log probability curvature（perturbation-based）检测 machine-generated text
   - 后续改进：DNA-GPT、Fast-DetectGPT 等
   - 与我们的关系：zero-shot detection 方法的 confidence score 理论上可作为 depth proxy（confidence ↑ with depth），但我们在 baseline 对比中验证其与 true depth 的 Spearman 相关性，预期弱于专用 ordinal classifier

4. **Binoculars (Hans et al., ICML 2024)**
   - 使用两个 LM 的 perplexity 比值检测合成文本
   - 与我们的关系：另一种 binary detection confidence → depth proxy 的 baseline

**我们的定位**：从 binary classification 升级为 ordinal regression。不是提出新的检测特征，而是证明已有特征（DivEye-style + 扩展）在 ordinal depth 维度上有系统性可分辨结构，且 ordinal signal 对下游 data curation 有实用价值。

---

## Thread 2: Model Collapse / Iterative Retraining → 我们量化代际退化边界

**核心问题**：递归训练导致的模型坍缩已被广泛研究，但缺少从 forensic 视角量化单个文档"经历了几代"的工具。

**核心论文**：

1. **Shumailov et al. (Nature 2024)**
   - 首次系统证明递归训练导致 tail disappearance → diversity loss → mode conflation 的三阶段坍缩
   - 早期坍缩（tail loss）比晚期坍缩（mode conflation）发生得更早、更剧烈
   - 与我们的关系：他们刻画了 macro 现象（population-level collapse dynamics），我们构建 micro 工具（单文档 depth forensics）。他们的"早期退化最剧烈"观察是我们 K* 假设的经验基础（K* ≈ 3-5）

2. **Alemohammad et al. (ICLR 2024)**
   - "Self-consuming generative models go MAD"——证明迭代训练在缺乏新鲜数据注入时导致 Model Autophagy Disorder
   - 关注图像生成，但核心机制（diversity collapse under recursive feedback）跨模态通用
   - 与我们的关系：跨模态的理论对应；他们的 MAD 概念对应我们的 depth → quality 单调衰减假设

3. **Dohmatob et al. (ICLR 2025)**
   - "Strong Model Collapse"——提供理论基础，证明在 data replacement 设定下 collapse 是不可避免的
   - 与我们的关系：他们的理论 bound 可与我们的信道级联 DPI 框架互补——DPI 给出 information-theoretic 视角，Strong Collapse 给出 statistical learning 视角

4. **Schaeffer et al. (2025)**
   - "Position: Model Collapse Does Not Mean What You Think"——识别了 8 种不同的 collapse 定义，指出在 data accumulation（非 replacement）条件下，catastrophic collapse 需要"trillions of models"
   - 关键承认：tail disappearance 和 diversity loss 是真实的、有实际危害的现象，即使不达到 catastrophic collapse
   - 与我们的关系：他们的 nuanced position 支持我们的 framing——不需要 catastrophic collapse 也有 graduated degradation，K* 度量的正是这种 non-catastrophic but real 的退化边界

**我们的定位**：Model collapse 文献研究"递归训练会发生什么"（understanding），我们研究"给定一段文本，它经历了几代"（forensics/estimation）。宏观理解 vs. 微观工具。我们的 K* 量化了 collapse 文献一直在定性讨论的"可区分性边界"。

---

## Thread 3: Verification-Based Data Curation → Graduated Filtering 替代 Binary

**核心问题**：现有数据质量控制要么不区分合成/人类文本（Surplexity），要么用 binary quality gate（verification 方法），丢失了 depth 提供的 graded quality signal。

**核心论文**：

1. **Feng et al. (ICLR 2025)**
   - "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification"
   - 理论 + 实验证明 verification（外部信号筛选高质量合成样本）可防止 collapse
   - 提出 imperfect verifier 的充分条件
   - 局限：verification 是 binary pass/fail gate，不估计深度，不提供 graded signal
   - 与我们的关系：他们证明了"筛选有用"，我们证明"按深度 graded 筛选更好"——从 binary gate 到 ordinal weighting

2. **Yi et al. (arXiv 2510.16657, 2025)**
   - 通过外部 verifier 注入信息逆转 collapse trajectory
   - 发现长期性能收敛到 verifier 的 knowledge center
   - 局限：同样是 binary verification，不估计 depth
   - 与我们的关系：如果 verifier 能利用 depth signal 做 graduated verification，理论上可延缓 convergence to knowledge center

3. **Surplexity (Gambetta et al., 2024)**
   - "Learning by Surprise"——按 surprise 值过滤训练数据缓解 collapse
   - 不区分 human vs. AI text，完全基于 perplexity 信号
   - 与我们的关系：Surplexity 是我们 downstream curation 实验的 baseline 之一；depth-aware filtering 预期优于 surprise-only filtering，因为 depth 编码了更多 provenance 信息

4. **Alemohammad et al. (ICLR 2024) — "Self-Consuming Generative Models Go MAD"**
   - 理论与实验分析自消费训练循环（model autophagy disorder），证明迭代训练导致分布退化
   - 关键贡献：形式化了 fully synthetic / synthetic augmentation / fresh data 三种数据混合策略的退化速率差异
   - 局限：关注宏观训练退化现象，未提供逐代检测或 depth estimation 工具
   - 与我们的关系：为递归退化提供了互补的理论视角（自消费 vs 我们的 iterated channel），其 depth-wise 退化曲线与我们的 JSD 衰减一致

5. **Drayson et al. (EMNLP 2025) — "On the Role of Synthetic Text Detection in Model Collapse Prevention"**
   - 训练 MGT 检测器做 importance resampling 防止 model collapse，在 GPT-2 和 SmolLM2 (124M–1.7B) 上实验
   - 关键贡献：首次将 binary MGT detection 作为 data curation 手段应用于 model collapse prevention
   - 局限：仍是 binary detection（synthetic vs human），不估计生成深度（depth）
   - 与我们的关系：**最接近的先行工作 (closest prior work)**。他们用 binary MGT detection 做 data curation 防 collapse，我们扩展为 ordinal depth estimation 做 graduated curation——从 binary filtering → graduated weighting 的自然推广。我们的工作回答了 Drayson 未触及的问题：不仅区分 human/synthetic，还估计文本经历了几代递归生成

**我们的定位**：从 binary quality gate → graduated quality signal。类比：二值化 vs. 灰度图。Depth-graduated curation 是 provenance-aware domain reweighting 的一种形式，比 binary filtering 在 threshold 附近信息损失更小。

---

## Thread 4: Data Mixing / Contamination Estimation → Depth-Aware Mixing

**核心问题**：大规模预训练数据混合已有系统方法论，但现有方法不考虑合成文本的 depth 维度。

**核心论文**：

1. **DoReMi (Xie et al., NeurIPS 2023)**
   - 使用 proxy model 学习 domain weights，优化 worst-group downstream performance
   - 与我们的关系：depth-graduated weighting 是 provenance-aware domain reweighting——与 DoReMi 的 domain weighting 理念一致，但我们的 weighting 来自 estimated depth 而非 domain identity，语义更可解释

2. **Data Mixing Laws (Ye et al., ICLR 2025)**
   - 研究不同数据源混合比例对 LLM 性能的 scaling law
   - 与我们的关系：如果 depth 是一个新的 mixing dimension，depth-aware mixing law 可以指导实际预训练数据配比

3. **ConStat (Dekoninck et al., NeurIPS 2024)**
   - Performance-based contamination detection：通过 rephrased samples 上的性能差异检测 benchmark contamination
   - 与我们的关系：ConStat 检测 benchmark contamination（eval-side），我们估计 training data depth contamination（data-side）——互补视角

4. **DATAPROPHET (Qi et al., ICLR 2026)**
   - Training-free data quality metrics（perplexity + similarity + diversity）用于多模态合成数据选择
   - 与我们的关系：他们的 quality metrics 可作为我们 depth-quality 单调性验证的 baseline quality proxy

**我们的定位**：在 data mixing 框架中引入 depth 作为新的数据维度。现有方法按 domain/source/quality 分层，我们增加 generational depth 维度，使 provenance 信息进入 mixing 决策。

---

## 总结：四线交汇

```
Thread 1 (Binary Detection)    →  我们：binary → ordinal
Thread 2 (Model Collapse)      →  我们：macro understanding → micro forensics
Thread 3 (Verification/Curation) →  我们：binary gate → graduated signal
Thread 4 (Data Mixing)          →  我们：depth as new mixing dimension
```

核心差异化一句话：**No existing work estimates how many recursive generation steps a text has undergone — we fill this gap with the first ordinal depth classifier and demonstrate its utility for graduated data curation.**
