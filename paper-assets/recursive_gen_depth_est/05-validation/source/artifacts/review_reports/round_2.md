---
round: 2
overall_score: weak reject
timestamp: 2026-05-15T16:22:58.291465+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints

**目标会议**：EMNLP 2026 Main Conference (ARR May cycle)
**审稿轮次**：Round 3（fresh review）
**Reviewer 编排**：2 人（R1: 方法严谨性+实验设计 / R2: 新颖性+完整性）
**交叉回应**：完成，1 轮收敛

---

## Summary

本文将递归生成深度估计形式化为有序分类任务，提出从参考模型计算的 19 维统计特征（perplexity 分位数、surprisal 矩、词汇多样性指标），用 Random Forest 在 3 模型 × 3 解码策略 × 4 深度的 Depth Degradation Atlas 上达到 70-85% 的 4-class 准确率（chance=25%）。论文引入 Effective Discriminable Depth (EDD) 指标量化深度可辨别性极限（EDD₀.₇₅=4），展示跨模型迁移 66.4%、跨策略迁移 59.1%，并报告 end-to-end PLM 微调（~59%）相比特征方法的 19pp 差距作为 negative result。

---

## Strengths

1. **新颖且及时的任务定义**：在 binary AI text detection 和 model collapse theory 之间建立了 ordinal depth estimation 这一中间层，填补了真实的研究空白。EDD 指标概念清晰，提供了量化深度可辨别性的有效工具。

2. **系统性实验设计**：3 模型 × 3 解码策略 × 4 深度的 Atlas 设计覆盖了主要变量空间。多轴 generalization 测试（跨模型、跨策略、端到端学习）展示了全面的实验视野。180K 样本 benchmark 对后续研究有较高价值。

3. **Feature universality 发现有经验价值**：p90_ppl 在 9/9 cells 排名前二、var_surprisal 在 7/9（permutation importance 下 8/9）排名前二，跨配置 Spearman ρ=0.868——如果在更广泛条件下成立，将是对递归生成理解的有意义贡献。

4. **诚实报告负面结果**：温度采样的 AUC 反转、端到端学习的 19pp 差距、d0 膨胀效应——均被诚实报告。Limitations section 覆盖 6 个具体局限，比大多数投稿更详尽。

5. **统计实践良好**：Bootstrap CI、Bonferroni 校正、排列重要性交叉验证、决策边界稀释分析——方法使用得当。fold-level std 0.2-0.9pp 确认极高稳定性。

6. **Related Work 全面**：38 条引用全部真实存在（经 OpenAlex + arXiv 验证），无虚假引用、无孤立条目。Model collapse、binary detection、adjacent tasks、decoding strategies 四个方向的定位清晰。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] 19 维特征共线性未量化，缺 top-2/top-5/per-category 消融** [R1-N2 + R2-W4, 双方一致 critical]
- 12/19 特征来自同一 reference model 的 token-level 分布，必然高度相关（mean_surprisal 与 mean_ppl 存在单调变换关系）。论文唯一消融跨度为 1 特征 (25.1%) → 19 特征 (78.2%)，中间无数据点。需 top-2 / top-5 / per-category 消融和相关矩阵。若 2-3 个特征即可接近 78%，须调整 "19-dimensional feature representation" 的 contribution 表述。

**[MF-2] Attention-importance 相关性方法论有缺陷** [R1-N3 + R2-W5, 共识 warning-to-critical]
- 用 DeBERTa/RoBERTa 的 attention weight 与 RF permutation importance 做 Spearman 相关（ρ=-0.484/-0.456）得出 "complementary representations" 结论，但 attention weight 不是模型使用信息的可靠指标（Jain & Wallace 2019）。度量粒度不匹配（token-level vs feature-level）。Appendix D 的线性探测负 R² 提供了独立支持，但论文未将其作为主论据。end-to-end 实验仅在一个 pipeline 上做。建议替换为 integrated gradients / SHAP，或以线性探测为主论据，且将 "requires" 改为 "benefits from"。

### Should-Fix（影响评分但不一票否决）

**[SF-1] EDD max 算子不要求连续可判别性** [R1-N1, R2 同意降级]
- 当前 EDD 定义在 AUC 非单调时可能给出误导性高值。论文中所有 EDD 计算的 AUC 恰好单调衰减（当前定义与连续版给出相同值），但作为打算被复用的 metric 应修复数学鲁棒性。建议改为 EDD_T = max{d*+1 : ∀d'≤d*, AUC(d',d'+1)≥T}。

**[SF-2] 递归生成定义过窄，与野外场景脱节** [R2-N1, R1 同意降级]
- 论文定义的"递归生成"仅覆盖同模型 LoRA 微调+采样这一种极其受控的场景。现实中存在 prompt-based 再生成、跨模型跨代污染、RLHF 管线间接吸收等多种机制。Abstract 的 "universal stability" 措辞虽限于 9 cells，但读者容易过度泛化。需显式界定 scope，考虑 pilot experiment 测试跨域迁移。

**[SF-3] 跨策略 d1/d2 AUC 反转限制部署可行性** [R2-N2, R1 同意降级]
- GPT-2 XL 的 d1/d2 AUC 降至 0.129（低于随机且反转），z-score 无法修复反而恶化。Discussion §6 提出的 depth-graduated data curation 应用场景在未知解码策略时不可行。需降低应用期望，分析 strategy-conditioned pipeline 可行性。

**[SF-4] d0 recall >98% 严重膨胀 headline accuracy** [R1-W1 + R2-W1, 完全一致]
- d0 vs d1+ 的分离更接近 domain classification 而非 depth estimation。Abstract 和 Table 2 的 headline 应并列报告含/不含 d0 的 accuracy。Cross-model transfer 66.4% 中 d2 recall 最低 26.8%，headline 具有误导性。

**[SF-5] Discussion §6 过于简短** [R2-N3 critical, R1 REBUT → warning, Director 裁定 warning]
- 仅 2 段 ~80 词，对提出新任务的论文不足。应扩展覆盖：混合深度语料库、对抗攻击鲁棒性、数据溯源联系、规模扩展预测。Limitations section 的 6 段详细讨论不能替代 Discussion 的前瞻性分析。

**[SF-6] "geometry-level shift" overclaim** [R1-W2, R2 同意]
- 仅凭 z-score normalization（最简单方法）失败就推断 "genuine geometry-level shift"，推理跳步过大。应测试更多 domain adaptation 方法或弱化措辞。

**[SF-7] Experiment ID 违反 double-blind** [R1-W3 + R2-W2, 完全一致]
- Table 3/4/5 caption 中含 experiment tracking ID（如 depth_extension_binary_pairwise_002），可能通过搜索反推作者身份。删除或匿名化。

**[SF-8] DeepSeek V3.2 zero-shot baseline 统计力度不足** [R1-W4 + R2-W3, 完全一致]
- 仅 200 样本（~50/class），95% CI ±6.8pp，且 prompt 设计未报告。增至 1000+ 样本或在 abstract 标注 CI。

**[SF-9] 缺少混合深度语料库讨论** [R2-W6, R1 同意]
- 所有实验假设 passage 来自单一深度，现实中文档可能混合不同深度段落。至少在 Discussion/Limitations 中讨论。

### Minor Issues（不影响接收）

- §3 标题 "Task Formulation" 实际包含完整方法论，建议改为 "Method" 或 "Task Formulation and Method"
- 图片路径 `../../figures/paper/` 暴露目录结构
- 引用年份轻微不一致：holtzman2020_nucleus (arXiv 2019)、basu2021_mirostat (arXiv 2020)
- alemohammad2024_mad 的 OpenAlex 第一作者匹配不一致
- Abstract 中 "mean Spearman ρ=0.868" 过于细节化
- 缺少 Ethics Statement（非强制但对检测任务论文有加分）
- "standard LoRA hyperparameters" 表述不严谨，建议改为 "commonly used"
- 缺少 gradient boosting baseline（nice-to-have，低优先级）

---

## Reviewer Consensus

两位 Reviewer 在以下问题上完全一致（无 REBUT）：

| 问题 | R1 | R2 | 共识严重性 |
|------|----|----|-----------|
| 特征消融缺失 | N2 (critical) | W4 (warning→升级 critical) | **critical** |
| d0 膨胀 headline | W1 | W1 | warning |
| Experiment ID 匿名性 | W3 | W2 | warning |
| LLM baseline 统计力度 | W4 | W3 | warning |
| 混合深度语料库 | — | W6 | warning (R1 同意) |

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | Director 裁定 |
|------|---------|---------|--------------|
| EDD 定义缺陷 | critical | warning (AGREE w/ qualification) | **warning** — 当前数据不受影响 |
| 递归生成定义脱节 | should-fix | critical | **warning** — claim 范围实际准确，需显式 scope 声明 |
| 跨策略部署限制 | should-fix | critical | **warning** — 核心 contribution 是任务+特征，非 deployment |
| Discussion 不足 | warning (REBUT) | critical | **warning** — Limitations 已有详细讨论，Discussion 偏短是写作问题 |
| Attention 方法论 | critical | warning-critical | **warning-to-critical** — 线性探测提供独立支持 |

---

## Questions（需作者澄清）

1. 仅用 top-2 特征（p90_ppl + var_surprisal）的 4-class accuracy 是多少？top-5 呢？
2. end-to-end PLM 微调是否尝试过更大的训练集（如合并多个 cell 的数据）或更长的训练？
3. 自动策略识别（先分类解码策略再分类深度的 two-stage pipeline）的可行性如何？
4. 如果在非 Wikipedia 种子文本上构建 pipeline，p90_ppl 和 var_surprisal 的 dominance 是否仍然成立？
5. DeepSeek V3.2 使用了什么 prompt？是否测试过 few-shot 设置？

---

## Missing References

以下 3 篇建议但非必须纳入：
1. **Ghostbuster** (Verma et al., ICML 2024)：使用结构化搜索选择统计特征进行 AI 文本检测，方法论直接可比
2. **M4/SemEval-2024 Task 8** Subtask B（multi-generator classification）：最近的多类 AI 文本分类基准
3. **DNA-GPT** (Yang et al., 2023)：divergent n-gram 方法，与本文 repetition features 有交集

---

## External Review (Stanford Agentic Reviewer)

外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**评分：Weak Reject（Findings 可接收，主会议不足）**
**置信度：4/5**

**理由**：论文提出了一个真正新颖的任务定义，实验在受控设置内系统全面，统计实践良好。但存在两个实质性方法论缺陷——特征消融缺失（无法判断 19 维中有多少独立信号）和 attention-importance 分析方法论问题（Contribution 4 的核心证据不可靠）——以及多个 framing/scope 问题（"universal" 措辞、d0 膨胀的 headline、geometry-level shift overclaim、Discussion 过短）。

**Findings 可接收的理由**：任务形式化本身有价值、Atlas 的系统设计和 feature universality 发现具有经验贡献、诚实报告负面结果体现良好学术规范。

**主会议不足的理由**：(1) MF-1 特征消融缺失使 "19-dimensional feature representation" 的 contribution 存疑——如果 2-3 个特征即可达到接近性能，contribution 需大幅调整；(2) MF-2 attention 分析不可靠，Contribution 4 的机制解释站不稳；(3) 多个 should-fix 累积（EDD 定义、scope overclaim、d0 inflation、Discussion 不足）进一步削弱论文的整体完成度。

**修改路径**：若能补充特征消融实验（确认独立信号维度数）、替换 attention 分析为更可靠方法、修复 EDD 定义、调整 framing（scope、d0、geometry-level shift）、扩展 Discussion——论文有潜力升至 borderline accept / weak accept。

---

## Detailed Comments

### §1 Introduction
- "universal stability across model families and decoding strategies"：R2 正确指出此措辞暗示过广适用性。建议限定为 "universal across the model-strategy grid studied"。
- "a zero-shot LLM baseline reaches only 40%"：此结果基于仅 200 样本 ±6.8pp CI，不应在 abstract/intro 中不加限定地使用。

### §2 Task Formulation (Method)
- Eq. 1 EDD 定义应改为连续版本 max{d*+1 : ∀d'≤d*, AUC(d',d'+1)≥T}
- Table 1 的 19 特征缺少 VIF/相关矩阵支持
- §2.2 LoRA 参数引用 Hu et al. 2022 是改进（vs Round 1/2），但 "standard" 应改为 "commonly used"

### §3 Atlas
- Table 2 应增加 d1-d3 3-class accuracy 行
- Table 3, 4, 5 caption 删除 experiment ID
- §4.3 "genuine geometry-level shift" 应弱化

### §4 Generalization
- §5.4 "requires explicit distributional statistics" → "benefits from"
- attention-importance 相关性应替换或降级，以线性探测为主论据
- Table 7 footnote 的 200 样本限制应更显著标注

### §5 Discussion
- 从 2 段扩展至至少 1 栏，覆盖：混合深度语料库处理、对抗攻击鲁棒性、数据溯源联系、规模扩展预测
- depth-graduated data curation 的应用期望应降低（given d1/d2 AUC inversion）

### §6 Conclusion + Limitations
- Limitations 内容详尽（6 段），质量好
- 可增加一段讨论 EDD 定义在 transfer 设置下的适用边界