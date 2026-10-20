---
round: 30
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T21:47:18.274396+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 30 审稿报告 — Generational Depth Estimation of Recursive Synthetic Text

**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewers**: R1（方法严谨性 + 实验设计 + 统计有效性）、R2（新颖性 + 贡献 + 相关工作 + 写作质量）
**审稿模式**: Fresh（独立初审 + 交叉分享）

---

## Summary

本文定义了"生成深度估计"（generational depth estimation）问题，提出 K\*\_empirical 度量递归合成文本的可辨别深度边界。使用 15 维统计特征 + OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族，1B-8B）上实验。核心发现：web text K\*≤2（"one-wash laundering"），arXiv K\*=3，跨模型迁移保持 80-92% 准确率（continuation mode）。Section 5 的 filtering 实验在 ~83% 污染下验证 binary 过滤优于渐进式策略。

---

## Strengths

1. **问题定义新颖且重要**：将 generational depth estimation 从模糊直觉转化为可操作的度量（K\*\_empirical），为 model collapse 和数据治理研究提供量化工具。[共识]
2. **实验覆盖面广**：10 个模型配置、6 个架构族、4 个领域、4 种解码策略，附带充分消融实验（长度、seed、scorer、样本量）。[共识]
3. **统计实践规范**：permutation test + Bonferroni 校正、bootstrap CI、GroupKFold 防泄漏、self-BLEU 折内计算，多处主动标注 marginal cases。[共识]
4. **"One-wash laundering"概念有传播价值**：将 K\*=2 的发现包装为直观概念，对数据治理实践有 messaging value。[共识]
5. **跨模型迁移（80-92%）是实用贡献**：15D generator-agnostic 特征集在 continuation mode 下的高迁移率使无需知道生成模型即可部署。[共识]
6. **DeBERTa 上界实验提供有用对比**：15D 特征给出 lower bound，表征模型可将 K\* 推至 4（arXiv），量化了 generator-agnostic 特征的代价。[共识]
7. **可复现性好**：超参数、特征定义、数据集构造、匿名代码/数据链接均已提供。[共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [共识 critical] **Bonferroni 校正下仅 3/6 K\*=2 配置统计显著，且全为 Qwen 变体**

论文声称"K\*=2 for 6/10 configurations"（Abstract, Section 4.1），但 Table 27 (Bonferroni-corrected 99.5% CI) 显示 Pythia-1.4B (CI lower 0.593)、Qwen-cont (0.598)、LLaMA-8B (0.599) 三个配置的 CI 下界均未超过 θ=0.60，统计不显著。仅 Qwen-rw、Qwen-base、Qwen-7B 三个 Qwen 变体的 CI 下界稳定超过 θ。论文在 Section 4.1 用"marginal"描述，但 Abstract/Introduction 未反映此限制。

按 family 去重后，robust K\*=2 仅 Qwen family；Pythia 和 LLaMA 为 marginal；OLMo、Gemma、Mistral 为 K\*=1。"K\*≤2 universally"的泛化性显著弱于论文所宣称。

（来源：R1-N1 + R1-N2，R2 交叉回应 AGREE）

**MF-2** [共识 critical] **4/10 配置 K\*=1 削弱"K\*≤2 universally holds"的主张**

40% 配置（OLMo 全配置、Gemma-2-2B、Mistral-7B、Pythia-6.9B 部分）给出 K\*=1，甚至无法区分 depth 1 和 depth 2。论文将 OLMo 称为"sole exception"，但 40% 比例不再是"exception"。论文缺乏对 K\*=1 出现原因的系统性分析（模型容量、训练数据、架构差异还是特征集局限）。

与 MF-1 共振：statistically significant K\*=2 仅 3 configs（全 Qwen），K\*=1 有 4 configs，论文实际发现更准确地说是"Qwen family robustly achieves K\*=2，其他 family 的 K\* 在 1 和 2 之间模糊"。

（来源：R2-N2，R1 交叉回应 AGREE）

**MF-3** [分歧 critical] **贡献悖论：K\*≤2 使 depth estimation 框架退化为 binary detection**

论文核心 framing 是"generational depth estimation"这一新问题，但 K\*≤2 意味着深度估计在 web text 上等价于二分类（human vs. machine）。Section 5 的 filtering 实验进一步证实 binary filtering 是最优策略——这与现有 binary detector 的功能一致。论文未充分论证 depth framework 相比 binary detection 的增量价值。

- **R2 立场（3.0）**：框架的实际产出等价于已有工作，novelty 和 practical contribution 不足以支撑 Main Conference。即使修复统计问题，conceptual contribution 仍停留在 Findings 水平。
- **R1 立场（3.5）**：K\*=2 作为 characterization result 有独立价值（解释 WHY binary suffices），且 K\*>2 场景（arXiv K\*=3, retrain-chain K\*≥4, neural probe K\*=3-4）证明框架有 beyond-binary 的扩展潜力。降至 Findings 过重。
- **两人共识**：论文的 framing 确有张力（Title/Abstract 强调 depth estimation，但 web text 的 actionable conclusion 是 binary suffices），需要更好地区分理论贡献（characterization of information loss dynamics）和实践贡献。

（来源：R2-N1，R1 REBUT severity 但 AGREE 诊断准确）

### Should-Fix（影响评分但不一票否决）

**SF-1** [共识] **DPI→AUC 单调递减的推理链有逻辑缺口**

Section 3.1 用 DPI 论证 I(X; Y\_k) 单调递减，但论文衡量的是 AUC\_{k-1,k}（对应 I(Y\_{k-1}; Y\_k)），两者不等价。OLMo 的非单调 AUC（Table 2 脚注 §: 2v3=0.497, 3v4=0.503）构成实证反例。当前 "The DPI motivates the empirical observation" 措辞模糊了理论保证与经验观察的边界。建议明确 DPI 仅保证 seed-to-generation MI，降级为 motivating intuition。

**SF-2** [共识] **θ=0.60 阈值 post-hoc 选取，存在 circularity 风险**

θ 基于观察到的 AUC cluster gap 选择，构成弱 circularity。Figure 3 的 sensitivity analysis 缓解但不消除此问题——稳定窗口仅 1pp（θ∈[0.59, 0.60]），θ=0.61 时 Pythia-1.4B 已 drop 到 K\*=1。应承认 post-hoc 性质，并报告基于 permutation null 99th percentile 推导的 principled threshold。

**SF-3** [共识] **Cross-model transfer claim 范围过大**

Abstract "depth estimation on corpora from unknown generators requires no retraining" 远超实际验证范围：(a) 仅覆盖 continuation mode，rewrite mode 迁移仅 61-63%；(b) K\*=1 模型的迁移在 depth estimation 意义上 trivial；(c) 有效迁移仅在 3 个 continuation-mode 模型间验证。应限定为 "across continuation-mode generators with K\*≥2"。

**SF-4** [共识] **Filtering 实验的实际意义有限**

Appendix B.8 显示在现实污染比例（≤50%）下，所有策略差异 <0.3pp，且 MMLU 均高于 base model——filtering 在现实场景下无实际效果。但 Abstract/contributions 的表述给人 practical contribution 的印象。应在 Section 5 开头直接说明 ≤50% 下效果消失，Abstract 限定适用范围。

**SF-5** [共识] **Watermarking 作为 provenance tracking 替代方案的讨论不足**

Text watermarking（Kirchenbauer et al., 2023）是 generational provenance tracking 的直接对标方案。论文仅一句"complementary post-hoc scenario"带过，应补 1-2 句讨论互补性。

**SF-6** [共识] **Bootstrap CI 方法不一致**

Table 27 使用 normal-approximation，Table 28 使用 percentile CI。AUC 在 0.50-0.60 区间 bootstrap 分布可能偏斜。核心发现高度依赖 CI 是否跨越 θ，方法一致性重要。

**SF-7** [共识] **正文叙事密度过高，insight 深度不足**

Section 4-5 塞入过多实验，每个实验讨论空间极有限（Section 4.3 仅 7 行，Section 4.6 仅 4 行）。建议将 binary detector confidence、feature ordering 等边缘实验移入 appendix，腾出空间深入讨论核心发现。

**SF-8** [分歧] **Retrain-chain K\*≥4 声明方法论支撑不足**

R2 认为正文仅一句话提及，无方法/统计检验。R1 反驳：Appendix B.7 提供了模型（Pythia-1.4B LoRA）、代数（5）、具体 AUC 数值，非 unsupported，但缺 LoRA 超参数和 CI。建议补充完整细节。

**SF-9** [共识偏 minor] **OBD vs ordinal regression 对比公平性**

Ordinal regression AUC 均值 0.4883 < 0.50 暗示调参可能不充分。论文解释为 collapsing，但 collapsing 应产生 ~0.50 而非 <0.50。R2 认为不影响核心结论（OBD 是工具选择非核心贡献），建议降级为 Minor。

---

## Reviewer Consensus [AGREE]

1. **Bonferroni 显著性分层**（MF-1）：statistically significant K\*=2 仅 3/6 configs（全 Qwen），Abstract/Introduction 的"6/10"表述需修改为 per-family 去重报告
2. **Qwen 过度代表**（MF-1/MF-2）：per-family 分析应为主体，Qwen self-familiarity artifact 需排查
3. **K\*=1 比例**（MF-2）：40% configs K\*=1 不是"exception"，需系统分析原因
4. **θ=0.60 post-hoc**（SF-2）：两人一致要求承认 post-hoc 并报告 principled threshold
5. **DPI→AUC 逻辑缺口**（SF-1）：降级为 motivating intuition
6. **Transfer overclaim**（SF-3）：限定 continuation mode + K\*≥2
7. **Filtering 实际意义**（SF-4）：在现实污染下效果消失，表述需限定
8. **Watermarking 讨论**（SF-5）：补 1-2 句
9. **Bootstrap CI 不一致**（SF-6）：统一方法
10. **叙事密度**（SF-7）：重组结构，腾出讨论空间

## Reviewer Divergence [REBUT]

1. **贡献悖论的杀伤力**（MF-3）：R2 认为 K\*≤2 = binary detection，降至 3.0（Findings）；R1 认为 characterization result 有独立价值 + K\*>2 场景，维持 3.5（Borderline Conference）。两人均承认论文 framing 有张力，但对可修复性判断不同。
2. **Retrain-chain K\*≥4 支撑**（SF-8）：R2 认为 unsupported claim；R1 认为 Appendix B.7 有数据但不够详尽。
3. **"One-wash laundering"术语**：R1 建议解释为隐喻；R2 认为 vivid imagery 是传播价值，不应削弱。
4. **Ordinal regression**（SF-9）：R1 标 Should-Fix；R2 认为应降级 Minor。

---

## Questions for Authors

1. 如果以 Bonferroni CI 下界而非点估计判定 K\*=2，核心结论从"6/10"变为"3/10 (all Qwen)"——论文的 framing 会如何修改？
2. Qwen family 在 K\*=2 中的 dominant 表现是否源于 Qwen 特有的 self-familiarity artifact（neural probe K\*\_neural=3 vs Pythia K\*\_neural=2 暗示此可能）？
3. Ordinal regression AUC 均值 0.4883 < 0.50 的各 depth pair 分解是什么？是否调参过？
4. Rewrite mode 迁移失败（61-63%）对实际部署的限制有多大？互联网文本可能由多种 mode 生成。
5. 在什么条件下（更强特征、更大模型、structured domains）depth estimation 可能变得 non-trivially useful（K\*>2 for web text）？

---

## Missing References

- Kirchenbauer et al. (2023): text watermarking 作为 proactive provenance tracking（论文仅一句带过）
- 无其他重大遗漏

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求

---

## Visual Layout Check（非评分项）

状态：**已完成**（2026-05-25 21:16–21:19, 约 3 分钟）

发现摘要（3 warning, 13 info, 0 critical）：
- **[warning] Pages 1-2**: 连续 2 页纯文本无 display item，首个视觉锚点（Figure 1）直到 page 3 才出现。建议考虑 teaser figure 或提前 Figure 1。
- **[warning] Page 5**: Table 2 全宽大表占页面 ~40%，视觉节奏偏单调（可接受）。
- **[warning] Page 6**: 三个 display items（Figure 3 + Figure 4 + Table 3）挤在单页。Figure 4 heatmap 标签偏小，打印后可能难辨。建议 Figure 4 改用 figure\*（全宽）。
- **[info]**: 正文 8 页内 6 figures + 5 tables = 11 个 display items，密度 1.375/页，充足。颜色方案色盲友好。无 margin 溢出或公式渲染错误。匿名规则、页数限制、Limitations 格式均合规。AI Assistance 披露声明已有。

---

## Overall Assessment

**Overall**: 3.0 (Findings) — 置信度 4/5

**维度评分（两人共识）**：
| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.0-3.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | **3.0** |

**评分理由**：

问题定义新颖，实验覆盖面广，统计实践规范——这些是明确的 strengths。但论文面临两个层面的挑战：

1. **Empirical robustness 层面**（R1 主导）：K\*=2 的核心 claim 在 Bonferroni 校正下仅 3/6 配置（全 Qwen）统计显著，40% 配置 K\*=1，per-family 去重后 robust K\*=2 仅 Qwen family。这些可通过修改 claim scope 和补充 per-family 分析解决。

2. **Conceptual contribution 层面**（R2 主导）：即使修复所有统计问题，K\*≤2 使 depth estimation 框架的实际效用等价于 binary detection，论文 ambition（depth estimation framework）与 conclusion（binary suffices）之间的根本张力仍在。这更难通过 revision 解决。

综合两位 Reviewer 的判断，Overall 取 3.0（Findings）。R1 维持 3.5 认为 characterization result 有独立价值——这一分歧适合由 AC 在 meta-review 中裁定。

**升分路径**：如果 revision 能 (a) 以 per-family 分析为主体，诚实报告 Bonferroni 显著性分层；(b) 正面回应贡献悖论，强化 K\*>2 场景（arXiv K\*=3, retrain-chain K\*≥4, neural probe K\*=3-4）作为框架价值的核心证据；(c) 修复 θ post-hoc、transfer overclaim、filtering scope 等表述问题——整体可提升至 3.5（Borderline Conference）。

---

## Detailed Comments

### Section 1 (Introduction)
- Contributions 列表中的"generational depth estimation"framing 与 K\*≤2 结论之间的张力需正面处理（MF-3）
- "6/10 configurations"需改为 per-family 去重表述（MF-1）

### Section 3.1 (Method - K\* Definition)
- Eq.1 应处理 AUC\_{0,1} < θ 的边界情况（约定 K\*=0）
- DPI motivation 应明确降级为 intuition，标注 DPI 保证 I(X;Y\_k) 而非 I(Y\_{k-1};Y\_k) 的单调性（SF-1）
- θ=0.60 应承认 post-hoc 性质，报告 permutation null 推导的 principled threshold（SF-2）

### Section 3.2 (Method - OBD Classifier)
- Ordinal regression AUC < 0.50 需分解各 depth pair，说明是否调参（SF-9）

### Section 4.1 (Core Results)
- 主报告应区分"statistically significant K\*=2"（3 configs, all Qwen）和"point-estimate K\*=2"（6 configs）（MF-1）
- 需系统分析 K\*=1 出现的原因（MF-2）
- Bootstrap CI 方法应统一（SF-6）

### Section 4.2 (Cross-Model Transfer)
- "requires no retraining"限定为 continuation mode + K\*≥2（SF-3）

### Section 4.3-4.6 (Secondary Results)
- Feature Ordering (7行) 和 Binary Detector (4行) 建议移入 appendix，腾出空间深入讨论核心发现（SF-7）

### Section 5 (Filtering)
- 开头直接说明 ≤50% 污染下效果消失（SF-4）
- Abstract 相应限定

### Section 6 (Discussion)
- Retrain-chain K\*≥4 补充完整实验细节和 CI（SF-8）
- "One-wash laundering"从信号集中度角度精确定义

### Related Work (Section 2)
- 补 watermarking 讨论 1-2 句（SF-5）

### Abstract
- "6/10 configurations"→ per-family 表述
- "across four independent architecture families (arXiv)"→ 标注 OLMo 例外
- Transfer claim 限定 continuation mode
- Filtering claim 限定 high contamination ratios