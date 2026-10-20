---
round: 7
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T23:55:47.795155+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7 (Fresh Review)

**论文**: "What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?"
**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)
**Deadline**: 2026-05-25 (AoE)
**审稿编排**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性/完整性），1 轮独立审稿 + 交叉分享收敛

---

## Summary

本文将教育测量学中的 IRT person-fit 统计量（ℓz*，Snijders 校正）应用于 LLM SFT 阶段基准污染检测。通过对三个 7-8B 模型族（Qwen2.5-7B、Llama-3.1-8B、Mistral-7B）进行 QLoRA 控制污染实验（MMLU + ARC-Challenge），报告三个发现：(1) θ-shift absorption 模型能力调节检测灵敏度；(2) 检测-诊断权衡——简单统计量检测力更强但 ℓz* 提供机制性洞察；(3) 能力依赖的非单调剂量-响应（exploratory）。核心方法创新是 Δℓz* matched-difference design，通过组内差分消除 LLM 对 IRT 假设的系统性违反。

---

## Strengths

**[S1] Matched-difference design 是本文最核心且扎实的方法论贡献。** 57/60 模型-基准组合的绝对 ℓz* 超过 1.96 使传统阈值完全失效。Δℓz* 设计通过组内差分将系统性模型误配从噪声转化为可控因素，优雅地解决了 IRT 模型在 LLM 场景下的适用性问题。（R1-S1, R2-S1 一致认可）

**[S2] 鲁棒性分析深度超过多数同类论文。** Appendix A-K 覆盖：simulation validation、4PL vs 3PL 消融、seed sensitivity、cross-seed consistency（n=3 seeds for Qwen）、局部依赖鲁棒性（shared + asymmetric LD）、item parameter perturbation（≤10% noise）、BCa bootstrap 校正。（R1-S2, R2-S4 一致认可）

**[S3] θ-shift absorption 的实证量化有理论贡献。** Table 2 中 Qwen 50% free-θ |d|=1.90 → fixed-θ |d|=14.52 的对比，直接验证了 MLE θ 估计吸收污染信号的机制。虽然方向可从 IRT 理论预测，但幅度和边界条件（如 Δθ>0.2 经验阈值、ARC-C 天花板效应逆转）是纯理论无法推导的实证发现。（R1-S3, R2 部分认可——R2 认为应明确区分 confirmatory quantification 与 novel discovery）

**[S4] Confirmatory vs exploratory 区分透明。** 论文明确标注 Finding 1-2 为 confirmatory、Finding 3 为 exploratory，在 ML 论文中少见且值得肯定。（R1-S4, R2-S3 一致认可）

**[S5] 检测-诊断权衡的实证发现有实用价值。** Table 3 展示 accuracy z-score |d|=68.7 远超 ℓz* |d|=1.90，论文坦诚承认简单统计量检测力更强，并将 ℓz* 价值定位在诊断（seen/unseen 分解、θ-shift 机制、结构敏感性）。两阶段工作流建议实用合理。（R1-S5, R2-S2）

**[S6] 信息效率高——仅需 binary response pattern。** 不需 logits/weights/training data，在 API-only 评估场景有实际价值。（R2-S2）

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] CI 系统性低估不确定性 + Table 1 seed 选择性报告。**（R1-W1, R2 交叉强烈 AGREE）

Bootstrap CI 仅反映 n=10 clean seeds 的抽样不确定性，将单个 contaminated observation 视为固定常量。对 Llama/Mistral 所有污染条件仅 n=1 污染运行，其变异性完全未被 CI 捕获。

Appendix K 揭示问题严重程度：Qwen 50% free-θ 三种子 |d| 分别为 1.90、5.42、7.91（CV=59.6%）。**主文 Table 1 报告 |d|=1.90（seed 42）——三种子中最小值**，恰好最有利于 inverted-U 叙事。多种子均值 |d|=5.08 与 15% 的 |d|=5.36 几乎无差异。

核心问题：主文声称 "All confidence intervals exclude zero"，但这些 CI 仅捕获不确定性的一个来源。一篇以统计方法为核心贡献的论文，其 CI 构造存在方法论缺陷。Table 1 报告单种子而非多种子聚合的做法，构成**结果呈现的公正性问题**。

**[MF-2] Inverted-U（非单调剂量-响应）证据被过度呈现，实为 θ 估计伪迹。**（R1-W2, R2-N2, 交叉双方一致）

(a) 主文 inverted-U 主要由 seed 42 驱动。多种子均值轨迹（5.36→7.44→5.08）显示 15% 和 50% 基本持平，"inverted-U" 在聚合层面基本消失。
(b) Fixed-θ 消除 inverted-U 后变为单调递增（均值 |d|: 6.85→5.89→12.32），说明 inverted-U 本质是 free-θ estimation 在高污染下的 artifact，不是污染的固有特征。
(c) Llama 的 inverted-U 统计不显著（CI 大幅重叠），Mistral 仅两个条件无法判断。
(d) Finding 3 仅基于 Qwen 单模型族，但在 Abstract 中与 N=3 families 的 confirmatory findings 并列为同等贡献。

R2 交叉后修正判断：不仅是 "exploratory finding"，而是 "可能由种子选择和 θ 估计伪迹共同驱动的虚假模式"。

**[MF-3] 核心新颖性以确认性发现为主，最具新意的发现证据不足。**（R2-N1, R1 部分 AGREE）

Finding 1（θ-shift absorption）和 Finding 2（detection-diagnosis tradeoff）在 IRT 文献中有理论预期（Meijer & Sijtsma 2001; Sinharay 2017a）。论文的贡献在于量化幅度和边界条件，但 Introduction/Abstract 未充分区分 confirmatory quantification 与 novel discovery 的权重层级。

R1 部分反驳：跨学科迁移本身有价值，ARC-C 天花板逆转和 fixed-θ 边界条件是理论无法预测的实证发现。但 R1 也同意需更诚实地分层呈现贡献。

### Should-Fix（影响评分但不一票否决）

**[SF-1] Cohen's d 解读不当——单观测标准化偏离量被与双样本效应量 benchmarks 类比。**（R1-W3, R2 AGREE 但认为严重程度较低）

d = (ℓz*_contam − mean_clean) / SD_clean 在 n_contam=1 下本质是 z-score。主文多处与 Cohen's benchmarks (0.2/0.5/0.8) 做隐性类比。在 |d|>1.5 量级下结论方向不变，问题是术语规范性而非实质性错误。建议全文改用 "standardized departure"。

**[SF-2] 缺少与现有方法的对比。**（R2-N3, R1 部分 REBUT → 降级为 should-fix。**分歧点**）

R2 列为 must-fix：完全没有与 MIA/ConStat 做 head-to-head 对比，Table 8 AUROC=0.63 无 baseline。
R1 部分反驳：(a) Table 3 已与 accuracy z-score/HT 做系统性对比；(b) ConStat 需多次运行，信息层级不同；(c) 论文明确定位为 characterization。R1 将其降级为 should-fix，但同意应展示诊断维度的对比优势。
本报告采纳 R1 的定位：**should-fix**，理由是论文已有与同层级方法的对比（Table 3），且明确定位为 characterization 而非 detection tool。但建议补充诊断维度的系统性对比。

**[SF-3] ARC-Challenge 统计力不足，跨基准推广性证据薄弱。**（R1-W4, R2-W2 一致）

295 items，模拟功效仅 0.087（15%）和 0.285（50%），远低于 0.80 标准。仅在 Qwen 上测试。ARC-C 结论可能依赖 Qwen 90% baseline 的天花板效应。MMLU vs ARC-C 差异根源（item 数量 vs benchmark 结构）未充分讨论。

**[SF-4] 实验矩阵不完整。**（R2-W1, R1 AGREE）

Mistral 缺 5%/25%，ARC-C 仅 Qwen，Post-RL N=1，仅 7-8B 规模，仅 QLoRA。论文以 computational budget 解释，但 "systematic" 等措辞暗示全面覆盖。

**[SF-5] PSN-IRT 参数 circularity 问题未讨论。**（R2-W3, R1 AGREE）

PSN-IRT 从 13,000+ 模型校准参数——若包含已污染模型则 item parameters 可能被系统偏置。Appendix F 的随机噪声鲁棒性 ≠ 系统性偏差鲁棒性。

**[SF-6] Mistral fixed-θ 缺失 seeds 4-7 未解释。**（R1-W6, R2 AGREE）

10 个 clean seeds 中 4 个不可用，原因未说明。若与模型行为相关则可能引入选择偏倚。

**[SF-7] 污染数据混合细节不够清晰。**（R1-W8, R2 AGREE）

"15% contamination" 的操作定义不明确（benchmark items 占训练数据 15% vs 15% benchmark items 加入训练数据？）。Non-contaminated training data 组成和训练数据总量未说明。

### Minor

- [m1] 模拟功效分析与真实实验对应关系不够清晰——模拟假设 4PL 正确但 57/60 系统性违反（R1-W7）
- [m2] Figure 2 heatmap 内标注字号偏小，灰色与浅蓝灰度打印区分度下降（Visual Check + R5-M1 延续）
- [m3] Pages 3-4 连续两页纯文本，建议加入 framework 示意图（Visual Check + R6-M2 延续）
- [m4] 缺少近期 contamination detection 综合 survey 引用（R2）
- [m5] Δℓz* vs Cohen's d of Δℓz* 符号在正文和图中不完全一致（R2）
- [m6] R1-W5 多重比较校正：R2 部分反驳——受控实验已知 ground truth，核心推断对象是效应量大小而非 p-value。但选择性报告风险仍需讨论。（**分歧点**，最终定级为 minor）

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致：

1. **[AGREE] CI 低估不确定性 + seed 选择性报告是最严重的方法论问题**。Table 1 报告 seed 42 单次结果而非多种子聚合，构成结果呈现公正性问题。R2 交叉后认为这比初轮评估更严重。
2. **[AGREE] Inverted-U 证据被过度呈现**。多种子均值显示效应大幅减弱，fixed-θ 下消失变单调。R2 修正为 "可能由种子选择和 θ 估计伪迹共同驱动的虚假模式"。
3. **[AGREE] 实验矩阵不完整**。Mistral 缺条件、ARC-C 仅 Qwen、仅 7-8B、仅 QLoRA。
4. **[AGREE] ARC-C 统计力不足**。模拟功效远低于 0.80。
5. **[AGREE] Matched-difference design 是最核心贡献**。
6. **[AGREE] 鲁棒性分析深度令人印象深刻**。
7. **[AGREE] Confirmatory/exploratory 区分透明值得肯定**。
8. **[AGREE] PSN-IRT circularity 需讨论**。
9. **[AGREE] Mistral seeds 4-7 缺失需解释**。
10. **[AGREE] 污染数据混合定义需澄清**。

---

## Reviewer Divergence

1. **[分歧] 缺少 head-to-head 对比的严重程度**。R2 列为 must-fix（缺少与 MIA/ConStat 对比），R1 降级为 should-fix（Table 3 已有同层级对比；信息层级差异使跨层级对比不具操作性；论文定位为 characterization）。本报告采纳 should-fix。
2. **[分歧] 跨学科迁移的贡献价值**。R2 认为 confirmatory findings 的 novelty bar 对 EMNLP main conference 偏低；R1 认为实证量化（ARC-C 天花板逆转、fixed-θ 边界条件）和跨学科迁移本身有独立价值。
3. **[分歧] 多重比较校正**。R1 认为应至少讨论；R2 反驳受控实验已知 ground truth 下多重比较校正主要价值在控制 FPR 而此处不适用。

---

## Questions（需要作者澄清）

1. **Q1** Table 1 中 Qwen 50% 报告的是 seed 42 单次结果还是聚合？如果是 seed 42，为什么选择报告这个特定种子而非多种子均值？（R1-Q1, R2 强烈关注）
2. **Q2** Llama/Mistral 的 n=1 污染运行，种子间变异性是否会低于 Qwen（CV=59.6%）？"All CIs exclude zero" 对这两个模型族是否过于强烈？（R1-Q2）
3. **Q3** Section 5 提到的 cross-benchmark comparison 方案是否有任何实验验证？（R1-Q3）
4. **Q4** Mistral seeds 4-7 在 fixed-θ 分析中不可用的具体原因？（R1-Q4, R2 AGREE）
5. **Q5** "15% contamination" 确切含义——benchmark items 占训练数据 15% 还是 15% benchmark items 加入？训练数据总量？（R1-Q5, R2 AGREE）
6. **Q6** PSN-IRT item bank 校准数据集是否包含已污染模型的 response data？是否存在 circularity？（R2-Q1）
7. **Q7** Table 8 AUROC=0.63——接近 random chance (0.5) 还是有实际可用性？（R2-Q2）
8. **Q8** Finding 3 是否可能是 QLoRA rank=16 特定配置的 artifact？（R2-Q3）
9. **Q9** Post-RL GRPO 1,500 步如何选择？更长训练是否改变 person-fit 信号？（R2-Q5）

---

## Missing References

1. **Han, Song, Lee, and Jo (2026)** "Quantifying Data Contamination in Psychometric Evaluations of LLMs", Findings of EACL 2026 — R2 建议引用。R1 指出论文 Related Work 已引用此工作。**确认：已引用，无需补充。**
2. **Contamination detection 综合 survey**（arXiv 2502.14425, arXiv 2502.17521）— R2 建议引用以提供领域全貌。R1 AGREE。**建议补充。**
3. **Wang et al. in-context learning contamination** — R2 建议引用。需确认是否与已引用的 wang2025fragility 为同一文。
4. **Pretraining-stage 方法的系统性定位** — R1 建议 Related Work 更明确地讨论 IRT person-fit 相对于 Min-K% Prob、MIA 等方法的信息需求层次差异。R2 同意。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 external_review）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-22 23:36-23:38）。0 critical / 1 warning / 5 info。

- **[warning] Page 6**: Figure 2 heatmap 内标注文字（Cohen's d 数值 + 95% CI）字号偏小，打印或低分辨率屏幕可能难以辨认。建议增大字号或仅保留色块（Table 1 已有对应数值）。灰色（未测试）与浅蓝色灰度打印区分度下降。
- **[info] Pages 3-4**: Related Work + Method 约 2 页纯文本，建议加入 framework overview 示意图。
- **[info] Page 8**: Discussion + Conclusion + Limitations 压缩同一页，密度高但排版无问题。
- **[info] Page 15**: 附录末页底部空白较多。
- **[info] Page 7**: Figure 3 色彩区分度良好，色盲友好。

---

## Overall Assessment

**Overall: 3.5 — Borderline Conference**（R1: 3.5, R2: 3.5）

**Confidence: 4/5**（两位 Reviewer 均为 4/5，分别熟悉 IRT person-fit 方法论和 LLM contamination detection 领域）

**理由**：

本文提出了一个有创意的跨学科方向——将教育测量学中成熟的 person-fit 统计量引入 LLM 基准污染检测。Matched-difference design（S1）是一个扎实的方法创新，鲁棒性分析（S2）深度超过多数同类论文，θ-shift absorption 的实证量化（S3）对后续研究有指导价值。

但三个核心问题限制了论文的当前水平：

1. **CI 构造 + seed 选择性报告**（MF-1）是最严重的方法论缺陷。一篇以统计方法为核心贡献的论文，其不确定性量化不完整且主文结果呈现存在公正性问题。
2. **Inverted-U 证据被过度呈现**（MF-2），多种子聚合和 fixed-θ 分析均表明这是 θ 估计伪迹而非污染的固有特征。
3. **新颖性以确认性发现为主**（MF-3），唯一具有发现性质的 Finding 3 恰好是证据最弱的。

如果作者能修复：(a) Table 1 改用多种子均值±SD；(b) 将 inverted-U 明确定位为 θ 估计伪迹并降低叙事权重；(c) Introduction/Abstract 诚实分层 confirmatory vs discovery 贡献——论文可达 4.0（Conference）水平。

**ACL ARR 维度打分**：

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 — CI 仅反映部分不确定性，inverted-U 证据在多种子下大幅减弱 |
| Excitement | 3.5/5 | 3/5 | 3/5 — 跨学科方向新颖但核心发现以 confirmatory 为主 |
| Reproducibility | 4/5 | 4/5 | 4/5 — 超参数详尽，PSN-IRT 公开，代码承诺发布 |

---

## Detailed Comments（逐节意见）

### Title
当前标题 "What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?" 比前版改善（含 IRT、限定 SFT-Stage），疑问句式恰当定位为 characterization。保持。

### Abstract
- "n=10 independent seeds per condition" 歧义——实际仅 clean baseline 有 n=10。R6 修复为 "n=10 clean baseline seeds" 需确认已生效。
- Finding 3 应明确标注为 θ 估计伪迹的 exploratory observation，不应与 Findings 1-2 并列。
- 首句 "yet most detection methods require privileged access" 暗示填补检测空白，与 characterization 定位有张力。建议更早引入 characterization 框架。

### Section 1 (Introduction)
- 需分层呈现贡献：confirmatory quantification (Findings 1-2 的幅度和边界条件) vs exploratory observation (Finding 3)。
- 论文已声明 "Rather than proposing ℓz* as a ready-to-deploy detection tool, we characterize the behavior boundaries"——这一定位正确且应维持。

### Section 2 (Related Work)
- 需补充近期 contamination detection survey（arXiv 2502.14425, 2502.17521）。
- 需更系统定位 IRT person-fit 相对于 Min-K% Prob / MIA / ConStat 的信息需求层次差异。

### Section 3 (Method)
- §3.2: Cohen's d 的数学定义和 one-sample standardized departure 的说明需加强。全文改用 "standardized departure" 术语。
- §3.2: CI 含义需更明确——"conditional on the observed contaminated run, reflecting clean-seed variability only"。
- §3.3: "15% contamination" 操作定义需补充（训练数据总量、非污染数据组成、比例的精确含义）。
- §3.3: Mistral 缺 5%/25% 条件应正面说明原因。

### Section 4 (Results)
- **Table 1**: 需改用多种子均值±SD（至少 Qwen 条件），或明确标注为 seed 42 单次结果。当前呈现方式有公正性问题。
- **Table 2**: Mistral seeds 4-7 缺失需解释。
- §4.3 / Figure 3: Inverted-U 需降级为 "free-θ estimation artifact"。引用多种子均值而非单种子结果。

### Section 5 (Discussion)
- "Characterization over tool" 定位正确。
- 需添加 PSN-IRT circularity 讨论。
- 需添加 confirmatory vs novel 的坦诚讨论（R6 已有初步版本，R7 要求加强）。
- Cross-benchmark comparison 方案缺乏实验验证——如果作为 future work 应明确标注为未验证的建议。

### Limitations
- 当前覆盖合理但可更具体：列出实验矩阵缺失条件（Mistral 5%/25%, ARC-C 非 Qwen 模型）。
- 低污染（<5%）检测力未知应保留。

### Appendix
- Appendix K 的多种子数据很有价值，但其与主文 Table 1 的不一致性是核心问题。建议将多种子聚合提升至主文。
