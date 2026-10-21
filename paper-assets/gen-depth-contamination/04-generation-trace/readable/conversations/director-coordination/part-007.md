# Director coordination — Part 7 of 9

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/5c/5c15b6d8ca58d93cafa3.json)

## Round 159

### User

_source line 2157 · 2026-05-21T01:26:06.246757+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

### 审查侧重：新颖性 + 完整性 + Related Work + 写作质量

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 定义了一个新颖且实用的研究问题（generational depth estimation），实验设计严谨、统计验证充分，但方法论创新有限，且 model collapse 动机与 prompt-chain 实验之间存在张力。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨，bootstrap CI、permutation tests、changepoint 分析、LOFO 交叉验证等统计方法运用得当；但 prompt-chain 到 real-world contamination 的推广论证不够充分 |
| Excitement | 3/5 | 研究问题新颖且有实际意义（K* 作为 curation 的操作性指标），但方法论（OBD + LightGBM + 手工特征）缺乏技术创新，filtering 实验效果偏小 |
| Reproducibility | 4/5 | 实验配置详尽（10 configs, 4 domains, 4 decoding strategies），超参数有表格，承诺开源代码；但 arXiv 子集构造细节不足 |
| Clarity | 3.5/5 | 整体结构清晰，统计论证完整；但 K* 变体符号过多，Abstract 信息密度过高，Conclusion 过于简短 |
| Reviewer Confidence | 4/5 | 熟悉 model collapse、AI-generated text detection、ordinal classification 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Introduction 以 model collapse 为动机但实验几乎全是 prompt-chain，两者之间的张力未充分弥合
- 具体位置：Section 1 (lines 4-9) vs. Section 4-5 全文
- 问题：Introduction 第一段以 retrain-chain model collapse（"When synthetic text is recursively fed back as input, the resulting multi-generational content degrades with each iteration"）为核心动机，引用 Shumailov et al. (2024) 和 Dohmatob et al. (2024)，但全部主实验都在 prompt-chain 设定下进行。Retrain-chain 实验仅在 Appendix 中出现（K*=7），Discussion Section 6 才提到"prompt-chain K*=2 as the curation floor"。
- 为什么影响接收：reviewer 可能质疑 prompt-chain K*=2 对 real-world contamination（通常是混合场景）的 generalizability。论文在 Limitations (2) 中坦承 "real-world contamination involves both prompting and retraining"，但这个关键 caveat 不应只在 Limitations 出现。
- 建议修改方向：在 Introduction 中更早明确区分 prompt-chain 和 retrain-chain，说明为何选择 prompt-chain 作为主设定，并将 retrain-chain 结果（K*=7）作为 framing 的一部分在 Introduction 末尾提及，形成 K*∈[2,7] 的完整图景。

**N2** [critical] K* 概念的增量贡献相对于 Geng et al. (2026) 和 Wang et al. (2025) 的区分不够清晰
- 具体位置：Section 2 (Related Work, para 2), Section 3.1
- 问题：Geng et al. (2026) 已经将 iterative generation 形式化为 Markov chain 并证明输出收敛到 small cycle sets；Wang et al. (2025) 展示了 attractor cycles。论文在 Related Work 中承认 "the attractor entry depth may correspond to the discrimination boundary, though this parallel remains suggestive"，但未深入说明 K* 相对于这些理论化的 convergence 概念有何本质不同。K* 的 novelty 是否仅仅是选择了特定的 operationalization?
- 为什么影响接收：如果 K* 被视为已有 convergence 概念的简单 operationalization 而非独立贡献，论文的核心 novelty 会被削弱。
- 建议修改方向：在 Section 3.1 中明确 formalize K* 与 Markov chain mixing time / attractor entry depth 之间的关系，阐明 K* 作为 per-text operational boundary 的独特价值。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Abstract 信息密度过高，可读性差
- 具体位置：Abstract (main.tex lines 37-44)
- 问题：Abstract 在未解释 K* 定义的情况下使用了 "discrimination boundary K*"、"θ-invariant domain ordering"、"OBD-LightGBM classifier"、"15D statistics"、"DeBERTa fine-tuning"、"margin stratification" 等术语，并引用了 Section 4.1。Abstract 中出现 section 引用在 ACL 论文中不常见。
- 建议：精简 Abstract 至核心发现，去掉 Section 引用和实现细节。

**W2** [major] Filtering 实验（Section 5）效果量小，作为贡献分量不足
- 具体位置：Section 5, Table 5
- 问题：Binary filtering 在 GSM8K 上仅提升 +1.92pp，TruthfulQA +1.52pp，而 WinoGrande 下降 -0.79pp。Graduated filtering 与 no filtering 不可区分（Δ ≤ 0.53pp）。这也说明 depth estimation 的 downstream utility 目前有限。
- 建议：将 Section 5 明确定位为 consistency check 而非独立贡献。

**W3** [major] Conclusion 过于简短，缺乏 broader implications
- 具体位置：Section 7 (仅 5 行)
- 问题：Conclusion 基本是 contributions 的重述，没有讨论 K*=2 对 web-scale curation 实践的影响、对 model collapse 理论的启示、以及未来方向。
- 建议：扩展 Conclusion 至 8-12 行，增加 broader implications 和 actionable takeaways。

**W4** [minor-major] K* 符号系统过度增殖
- 具体位置：全文，特别是 Appendix A (notation table)
- 问题：论文使用了 K*, K*_empirical, K*_theory, K*_neural, K*_binary, K*_15D, K*_intrinsic, K*_PELT, K*_OBD 等变体。在 LaTeX 中 \Kstar 和 \Kempirical 定义为相同的 K*，但概念上应有区分。
- 建议：统一使用不超过 3 个变体，其余在首次使用时定义但不必赋予正式符号。

**W5** [minor] Related Work 遗漏 Fu et al. (2025) (ICLR 2025)
- 具体位置：Section 2, para 1
- 问题：Fu et al. "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" (ICLR 2025) 提出 recursive stability 概念并给出 self-consuming training loops 的首个理论泛化分析，与 K* 的有限边界概念直接相关，但未被引用。
- 建议：在 Related Work 的 model collapse paragraph 中增加此引用。

**W6** [minor] 引用库存在 3 个 orphan entries 和若干年份不一致
- 具体位置：references.bib
- 问题：3 个 bib entries 未被引用（hao2025rewrite, tang2024science, wu2023survey）；levin2017markov 年份与 OpenAlex 不一致（2008 vs 2017）。
- 建议：清理 orphan entries；核实 Levin & Peres 引用年份。

---

## 小问题（不影响接收）

- Abstract 中的 Section 4.1 引用应移除
- Table 中 "---" 表示缺失值的 convention 建议统一说明
- arXiv 子集 n=2,200 vs C4 n=5,000 的 power 差异可更明确讨论
- Qwen 家族 5/10 配置的 over-representation（Limitations 8 已提及但可更显著）

---

## Questions

**Q1**: 论文声称 K*=2 对 web text 是 "representation-independent boundary"（Section 4.4），因为 DeBERTa 也无法超越 K*=2。但 DeBERTa-v3-base 只是 184M encoder。是否考虑过使用更大 encoder 验证这个 upper bound?

**Q2**: θ=0.60 的选择虽有 empirical discontinuity 和 Youden's J 支持，但如果 1v2 和 2v3 之间的 gap 缩小（更大模型或不同 domain），θ 的灵敏度是否会显著增加?

**Q3**: Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3（Table 4），这是否暗示 K* 更多反映 domain-model interaction 而非 domain structural complexity?

---

## Missing References

1. **Fu et al. (2025)** "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" (ICLR 2025, arXiv:2502.18865)
2. **PAN@CLEF 2025 Generated Plagiarism Detection Task** — 涉及 iterative LLM generation 检测的 shared task

---

## 主要优势

- **S1**: 研究问题新颖且实际意义明确。Generational depth estimation 填补了 binary detection 和 population-level model collapse 分析之间的空白。
- **S2**: 实验统计方法论严谨出色（bootstrap CI、permutation tests、BH 校正、Youden's J、PELT、LOFO），在 NLP 论文中少见。
- **S3**: 域序 invariance 发现（arXiv > C4 = Code > Wikipedia）是有价值的新经验知识。
- **S4**: Limitations section 极其详尽和诚实（9 项），体现良好学术诚信。
- **S5**: DeBERTa 与 15D 对比验证了 domain ordering 的 feature-set invariance，在 C4/Code 上建立 representation-independent boundary。

---

## 格式合规检查

- ✅ Double-blind 匿名：author = "Anonymous"，无可辨识信息
- ✅ 页数：主文（Section 1-7）在第 8 页结束，Limitations 从第 8 页中部开始（不计入页数限制）
- ✅ Limitations section：存在且充分
- ✅ Ethics Statement：存在且合理
- ✅ ACL style with [review] option
- ✅ 正文中未发现破折号违规（无 em dash/en dash in prose）
- ⚠️ 引用库有 3 个 orphan entries（不影响格式合规但需清理）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2158 · 2026-05-21T01:26:12.935976+00:00_

Reviewer 2 审稿意见已收到（3.5/5 Borderline Conference）。等待 Reviewer 1 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 160

## Round 160

2 recorded events


### User

_source line 2159 · 2026-05-21T01:26:29.861438+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成，已提交给 Review Director。

核心判断：**3.5/5 (Borderline Conference)**。论文定义了新颖的 generational depth estimation 问题，统计方法论严谨（bootstrap CI、permutation tests、PELT changepoint 等），域序 invariance 发现有价值。两个 critical 问题：(1) model collapse 动机与 prompt-chain 实验的叙事张力；(2) K* 相对 Geng et al. (2026) Markov chain 和 Wang et al. (2025) attractor cycles 的增量贡献需更清晰地 articulate。方法论（OBD + LightGBM + 15D 手工特征）创新有限，filtering 实验效果量偏小。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2160 · 2026-05-21T01:26:35.138090+00:00_

Reviewer 2 已返回（3.5/5 Borderline Conference）。等待 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 161

## Round 161

8 recorded events


### User

_source line 2161 · 2026-05-21T01:28:21.960645+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计）

---

### Summary

本文形式化了 K*（在递归合成文本中，分类器能可靠区分相邻代际的最大生成深度），使用 15 个统计特征和 OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族、1B-14B）上测量得出 prompt-chain 模式下 K*≤2（θ=0.60）。论文还报告了一个特征集不变的域排序（arXiv > C4 > Code > Wikipedia）、跨模型迁移结果（80-92% 准确率保留但边界处有显著失败）、以及 K*-一致过滤的下游任务评估。该研究填补了 per-text 可操作深度估计的文献空白，实验覆盖面广，附录极为详尽（21 页），但在阈值选择、理论动机、分类器依赖性和实际过滤效果等方面存在需要讨论的方法论问题。

---

### Strengths

**S1. 新颖且有用的形式化框架**
K* 概念填补了文献中的真实空白。现有 model collapse 文献关注群体级降退，现有检测文献关注 binary（人/机）分类，但没有工作提供 per-text 的可操作深度估计。K* 的定义清晰（adjacent-pair AUC + CI lower bound > θ），且直接连接到数据筛选的实际需求。

**S2. 系统性实验设计**
10 个配置 × 4 个域 × 4 个解码策略的组合覆盖面在同类工作中属于前列。域排序（arXiv > C4 > Code > Wikipedia）通过 changepoint 分析（PELT, Appendix D.25）、margin stratification（Section 4.1）、和 LOFO cross-validation（Appendix D.18）三重验证，令人信服。

**S3. 统计严谨性的主体部分**
Bootstrap CI（1,000/10,000 resamples）、置换检验（p ≤ 10⁻⁴）、Benjamin-Hochberg 校正（q_max = 0.003 over n=30 boundary tests, q_BH = 0.019 for upper bound m=154）、GroupKFold 保持文档完整性——统计方法论的主体框架是正确的。

**S4. 坦诚的局限讨论**
论文明确承认 DPI "does not formally guarantee or bound" K*（Section 3.1）、跨模型迁移在边界处失败（Section 4.2）、以及过滤实验仅在 2 个架构上验证（Limitations）。这种坦诚在同行评审中是正面信号。

**S5. Retrain-chain 对比提供有价值的对照**
Appendix D.1 中 retrain-chain 实验显示 K*=7（vs prompt-chain K*=2），有效地区分了"文本内在信息损失"和"累积模型适应伪影"，增强了对 prompt-chain K* 的解释力。Figure 4 中 JSD 衰减曲线也提供了很好的互补证据。

---

### Weaknesses

**W1 [Critical] θ=0.60 的选择存在循环论证风险**

- **具体位置**: Section 3.2 (page 4), Appendix D.18, D.25, D.26
- **问题**: θ=0.60 从观测到的 AUC 分布中得出（1v2 AUC 聚集于 0.61-0.70, 2v3 聚集于 0.55-0.58），然后用 Youden's J 在同一数据上"验证"这个阈值。Youden's J 天然会将最优分割点放在观测到的 gap 中，因此这不是独立验证。LOFO 分析（Appendix D.18）同样将 θ=0.60 作为 ground truth 而非待检验假设。
- **多个配置的 CI lower bound 极接近 θ**: Table 2 显示 1v2 CI lower bounds 范围为 0.6112-0.6539。例如 Gemma-2-2B 的 1v2 AUC CI 为 [0.6025, 0.6212]（Table 10），下限距 θ 仅 0.25pp。θ 微小变动（如 ±2pp）即可改变边界配置的 K* 赋值。
- **为什么影响接收**: K* 的定义核心依赖 θ。如果 θ 的选择不够稳健，整篇论文的核心发现（K*≤2）就具有条件性而非普适性。
- **建议修改方向**: (1) 在非 Qwen 配置上推导 θ，在 Qwen 配置上验证（或反过来），实现 held-out 验证；(2) 报告 K* 对 θ 的灵敏度曲线（θ ∈ [0.55, 0.65] 间每 0.01 的 K* 赋值），而不仅仅是定性描述 K* 在 [0.575, 0.625] 间稳定；(3) 明确标注哪些配置的 K* 赋值对 θ 的微小变动敏感（marginal cases）。

**W2 [Critical] DPI → K* 的推理链存在逻辑缺口**

- **具体位置**: Section 3.1 (page 3)
- **问题**: DPI 保证互信息沿 Markov 链单调递减，但 K* 通过 adjacent-pair AUC（分类指标）定义，而非互信息。论文声称 DPI "motivates" a finite K*，但从"互信息递减"到"AUC 跌破 θ"之间缺乏形式化桥梁。AUC 的衰减速率取决于具体模型和生成过程的特性，而非仅由 DPI 决定。具体来说，DPI 约束的是 I(X₀; Xₖ) 的累积下降，但 K* 基于 adjacent-pair AUC_{k,k+1} 的行为，这两者之间的关系未被建立。
- **为什么影响接收**: Section 3.1 标题为 "Problem Formulation"，DPI 的显著位置暗示了比实际更强的理论基础。读者可能误认为 K* 有信息论保证。
- **建议修改方向**: (1) 将 DPI 讨论明确重新定位为"经验动机"而非"形式化基础"，例如将小节标题改为 "Motivation" 或在正文中更显著地标注"DPI provides intuition but not a formal bound for K*"；(2) 或者补充一个引理/命题，在特定分布假设下将 AUC 衰减与互信息衰减联系起来（即使是弱联系）。

**W3 [Major] K* 部分依赖分类器能力，而非纯粹的文本属性**

- **具体位置**: Table 3 (page 6), Table 34-35 (page 21), Section 4.4 (page 6), Section 6 (page 8)
- **问题**: DeBERTa v3-base 在 arXiv 上将 K* 从 2 扩展到 3-4（Table 35），在 Wikipedia 上从 1 扩展到 2（Table 3）。Neural probe（Section 4.4）将 Qwen 的 K* 扩展到 3。这意味着"discrimination boundary"不是文本的固有属性，而是"在给定特征/分类器下的检测极限"。
- **为什么影响接收**: 论文的叙事（Abstract, Introduction, Title 中的 "Measuring the Discrimination Boundary"）暗示 K* 是文本的内在属性。但证据显示它是 classifier-conditional 的。这降低了 K* 作为数据筛选通用指标的可信度——如果 DeBERTa 能检测到 depth 3-4，那么 K*=2 的过滤指导意义是什么？
- **建议修改方向**: (1) 明确区分 K*_ISD（本文主要结果）和 K*_DeBERTa（upper bound），将当前结果定位为"基于可解释统计特征的保守下界"；(2) 讨论实践者应如何在 K*_ISD=2 和 K*_DeBERTa=3-4 之间选择；(3) 考虑将标题中 "Discrimination Boundary" 改为更精确的表述，如 "Discrimination Boundary under Interpretable Statistical Features"。

**W4 [Major] 模型配置空间偏重 Qwen 家族**

- **具体位置**: Table 1 (page 4), 全文
- **问题**: 10 个配置中 Qwen 占 5 个（Qwen-1.5B, Qwen-cont, Qwen-base, Qwen-7B, Qwen-2.5-14B），其余 5 个家族各仅 1 个配置。在 continuation mode 的 9 个配置中，Qwen 占 4 个。≥7B 仅 3 个模型（Qwen-7B, Qwen-2.5-14B, LLaMA-3.1-8B），14B 仅 Qwen-2.5-14B。Mistral-7B 仅出现在扩展结果（Table 10）中而非主表。
- **为什么影响接收**: 当 K*≤2 的结论主要由 Qwen 变体驱动时，"跨架构可推广性"的声称被削弱。不同架构族的生成文本可能有不同的统计特征衰减模式——仅各测 1 个非 Qwen 模型无法排除这种可能。
- **建议修改方向**: (1) 至少为 Pythia、OLMo、LLaMA 各增加一个规模变体（如 Pythia-6.9B、LLaMA-3-1B）以验证规模效应的跨家族一致性；(2) 或在正文中显著弱化可推广性声称，将结论限定为"在 Qwen 家族内高度一致，在其他家族的单一规模点上得到初步确认"。

**W5 [Major] 过滤实验的效果量不足以支撑实用性声称**

- **具体位置**: Section 5 (page 7), Table 5 (page 7), Table 27-28 (page 20)
- **问题**: 
  - GSM8K: best +1.92pp（Qwen graduated），TruthfulQA: +1.52pp，WinoGrande: **-0.79pp**（负面！），ARC-C: 无显著变化
  - 效果量在标准 benchmark 的噪声范围内（~1-2pp）且方向不一致
  - Pythia-1.4B（Table 28）：graduated filtering 产生"a no-filter pattern"，即该方法在第二个测试架构上不起作用
  - 训练集仅 30K C4 文档，5 seeds——规模极小
- **为什么影响接收**: Section 5 标题 "K*-Consistent Filtering" 和 Discussion 中 "K*=2 resolves this: graduated weighting beyond depth 2 offers no actionable guidance" 暗示了实用价值，但证据不支持这一论断。1-2pp 的提升在 noise floor 内，且 Pythia 上失败。
- **建议修改方向**: (1) 要么大幅扩展过滤实验（更多架构、更大训练集、更多 benchmark），要么将 Section 5 重新定位为"初步探索性分析"并弱化实用性结论；(2) 报告效果量的 confidence interval 和 power analysis；(3) 诚实讨论 WinoGrande 负面结果和 Pythia graduated failure。

**W6 [Minor] 跨模型迁移的报告存在 framing 偏差**

- **具体位置**: Abstract (page 1), Section 4.2 (page 5), Table 8 (page 13)
- **问题**: Abstract 强调 "80-92% accuracy retention"，但 Section 4.2 报告 4/6 off-diagonal 7B pairs 在边界处失败（AUC < θ）。在实际数据筛选场景中（生成器未知），边界处的失败比总体准确率更具决定性。80-92% 的总体准确率被 depth-0 vs depth-1 的容易案例拉高。
- **建议修改方向**: Abstract 中应同时提及边界处的迁移限制，例如 "overall accuracy retention of 80-92%, though boundary-level transfer fails for most 7B cross-generator pairs."

**W7 [Minor] 统计方法论中 retrain-chain 与主实验的不一致**

- **具体位置**: Appendix D.1 (page 13), CI methodology note (page 14)
- **问题**: 主实验用 bootstrap CI（1,000-10,000 resamples），retrain-chain 用 t-distribution CI（K=5 独立重训练运行）。虽然都是有效方法，但 K=5 的 t-CI 功效很低（宽区间），且两种 CI 方法不直接可比。CI methodology note 承认了 bootstrap 的合理性，但未讨论为什么 retrain-chain 不也用 bootstrap。
- **建议修改方向**: 说明 retrain-chain 使用 t-CI 的原因（如果是因为仅 5 次重训练限制了 bootstrap 的适用性，请明确说明）。

---

### Questions

**Q1**: 是否考虑过将 θ 的推导和验证分开？例如在非 Qwen 家族上推导 θ，在 Qwen 变体上验证？这将有效解决 W1 中的循环论证问题。

**Q2**: 给定 DeBERTa 能达到 K*=3-4（W3），实践者在实际数据筛选时应使用哪个 K*？K*_ISD=2 还是 K*_DeBERTa=3-4？论文对此没有给出明确指导。

**Q3**: Table 24 的 two-way ANOVA（Depth Pair × Generator）显示交互效应显著（p < 0.05, η²=0.03）。虽然效应量小，但这暗示 K* 可能不完全是 generator-independent 的。这与论文 claim 的 "feature-set invariant" ordering 是否矛盾？

**Q4**: 过滤实验（Section 5）中，30K 文档 + 5 seeds 的实验规模是否足以检测 ~2pp 的效果量？能否提供 power analysis？

**Q5**: Retrain-chain K*=7 在真实场景中如何解读？现实中文本通常同时经历 prompt-chain 和 retrain-chain 污染路径。在混合设置下，K* 应如何估计？

---

### Missing References

未发现关键遗漏。引用验证结果：66 条 bib 条目中 58 条在线验证通过，4 条因较新/OpenAlex 未收录未找到（mitchell2023detectgpt, basani2026diveye, zawalski2026codec, hans2024binoculars，均为真实论文），4 条轻微不匹配（年份/作者拼写），3 条 orphan（在 .bib 但未在正文引用：hao2025rewrite, tang2024science, wu2023survey）。无伪造引用。

---

### Overall Assessment

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: K* 框架新颖且填补了文献空白，实验覆盖面广且附录极为详尽，但阈值选择的循环论证、分类器依赖性、以及过滤实验的微弱效果量共同削弱了核心声称的说服力。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要 claim（K*≤2）有实验支撑但存在重要 caveats：θ 选择循环论证（W1）、K* 的分类器依赖性（W3）、过滤效果量不足（W5）。统计方法论主体正确但有不一致之处（W7）。DPI→K* 缺乏形式化桥梁（W2）。 |
| Excitement | 3/5 (Interesting) | "递归合成文本在多深处变得不可区分"是及时且实际相关的问题。K* 框架新颖。但 K*≤2 的发现在先验上并不意外（已知质量在前几代急剧降退），且实际过滤应用效果微弱。 |
| Reproducibility | 3/5 | 方法描述详尽（prompts in Appendix B, 特征定义 in Table 15, 超参数 throughout），但代码和语料库未随论文发布（Limitations 称 "released upon acceptance"）。GroupKFold 的具体实现细节、15 个特征的精确计算方式需要代码才能完全复现。 |
| Datasets | 3/5 | 生成的深度链语料库对研究社区潜在有用，但尚未发布。 |
| Software | 2/5 | 未发布代码。 |

## Reviewer Confidence
**4/5** — Quite sure. I read the paper carefully including all 29 pages of appendix, verified references, and checked the ARR review guidelines. I am familiar with model collapse, synthetic text detection, and data curation literature.

---

### 审稿要点总结

**Must-Fix（影响接收决定的核心问题）:**
1. θ=0.60 的独立验证（W1）——需要 held-out 验证或至少详细的灵敏度曲线
2. DPI → K* 的 framing 调整（W2）——需要重新定位为经验动机而非形式化基础

**Should-Fix（影响评分但可在 revision 中解决）:**
3. K* 的分类器依赖性需要更显著的讨论和 framing 调整（W3）
4. 模型配置空间的 Qwen 偏重需要补充实验或弱化声称（W4）
5. 过滤实验需要扩展或重新定位为初步探索（W5）

**如果 Must-Fix 问题得到解决**，本文有潜力达到 Conference 水平（4.0）——核心 idea 足够新颖，实验的广度和深度在同类工作中属于前列。当前主要问题不在于实验执行质量，而在于 claims 的措辞相对证据偏强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2162 · 2026-05-21T01:28:45.659134+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查（外部审稿未启用）'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查（外部审稿未启用）'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2163 · 2026-05-21T01:28:45.760041+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2164 · 2026-05-21T01:29:18.740994+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重新颖性 + 完整性 + Related Work + 写作质量）的完整审稿意见。请逐条回应：对每一个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Clarity**: 3.5/5\n\n### Must-Fix 问题\n\n**N1** [critical] Introduction 以 model collapse 为动机但实验几乎全是 prompt-chain，两者之间的张力未充分弥合\n- Introduction 第一段以 retrain-chain model collapse 为核心动机，引用 Shumailov et al. (2024) 和 Dohmatob et al. (2024)，但全部主实验都在 prompt-chain 设定下进行。Retrain-chain 实验仅在 Appendix 中出现（K*=7），Discussion Section 6 才提到\"prompt-chain K*=2 as the curation floor\"。\n- 建议：在 Introduction 中更早明确区分 prompt-chain 和 retrain-chain，将 retrain-chain 结果（K*=7）作为 framing 的一部分在 Introduction 末尾提及。\n\n**N2** [critical] K* 概念的增量贡献相对于 Geng et al. (2026) 和 Wang et al. (2025) 的区分不够清晰\n- Geng et al. (2026) 已将 iterative generation 形式化为 Markov chain 并证明输出收敛到 small cycle sets；Wang et al. (2025) 展示了 attractor cycles。论文承认 \"the attractor entry depth may correspond to the discrimination boundary, though this parallel remains suggestive\"，但未深入说明 K* 的本质不同。\n- 建议：在 Section 3.1 中明确 formalize K* 与 Markov chain mixing time / attractor entry depth 之间的关系。\n\n### Should-Fix 问题\n\n**W1** [major] Abstract 信息密度过高，可读性差\n- Abstract 在未解释 K* 定义的情况下使用了多个术语，并引用了 Section 4.1。\n\n**W2** [major] Filtering 实验效果量小（GSM8K +1.92pp, TruthfulQA +1.52pp, WinoGrande -0.79pp），作为贡献分量不足\n- 建议将 Section 5 明确定位为 consistency check 而非独立贡献。\n\n**W3** [major] Conclusion 过于简短（仅 5 行），缺 broader implications\n\n**W4** [minor-major] K* 符号系统过度增殖（K*, K*_empirical, K*_theory, K*_neural, K*_binary, K*_15D, K*_intrinsic, K*_PELT, K*_OBD）\n\n**W5** [minor] Related Work 遗漏 Fu et al. (2025) \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" (ICLR 2025)\n\n**W6** [minor] 3 个 orphan bib entries（hao2025rewrite, tang2024science, wu2023survey）+ levin2017markov 年份不一致\n\n### Questions\n\n**Q1**: DeBERTa-v3-base 只是 184M encoder，是否考虑过更大 encoder 验证 K*=2 upper bound？\n**Q2**: θ=0.60 的灵敏度是否会随更大模型或不同 domain 显著增加？\n**Q3**: Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3，是否暗示 K* 更多反映 domain-model interaction 而非 domain structural complexity？\n\n### Strengths\n**S1**: 研究问题新颖且实际意义明确\n**S2**: 实验统计方法论严谨出色\n**S3**: 域序 invariance 发现有价值\n**S4**: Limitations section 极其详尽和诚实\n**S5**: DeBERTa 与 15D 对比验证了 feature-set invariance\n\n---\n\n请对每个 Weakness（N1, N2, W1-W6）和 Question（Q1-Q3）逐条回应 [AGREE] 或 [REBUT]。",
  "project": "gen-depth-contamination",
  "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重新颖性 + 完整性 + Related Work + 写作质量）的完整审稿意见。请逐条回应：对每一个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Clarity**: 3.5/5\n\n### Must-Fix 问题\n\n**N1** [critical] Introduction 以 model collapse 为动机但实验几乎全是 prompt-chain，两者之间的张力未充分弥合\n- Introduction 第一段以 retrain-chain model collapse 为核心动机，引用 Shumailov et al. (2024) 和 Dohmatob et al. (2024)，但全部主实验都在 prompt-chain 设定下进行。Retrain-chain 实验仅在 Appendix 中出现（K*=7），Discussion Section 6 才提到\"prompt-chain K*=2 as the curation floor\"。\n- 建议：在 Introduction 中更早明确区分 prompt-chain 和 retrain-chain，将 retrain-chain 结果（K*=7）作为 framing 的一部分在 Introduction 末尾提及。\n\n**N2** [critical] K* 概念的增量贡献相对于 Geng et al. (2026) 和 Wang et al. (2025) 的区分不够清晰\n- Geng et al. (2026) 已将 iterative generation 形式化为 Markov chain 并证明输出收敛到 small cycle sets；Wang et al. (2025) 展示了 attractor cycles。论文承认 \"the attractor entry depth may correspond to the discrimination boundary, though this parallel remains suggestive\"，但未深入说明 K* 的本质不同。\n- 建议：在 Section 3.1 中明确 formalize K* 与 Markov chain mixing time / attractor entry depth 之间的关系。\n\n### Should-Fix 问题\n\n**W1** [major] Abstract 信息密度过高，可读性差\n- Abstract 在未解释 K* 定义的情况下使用了多个术语，并引用了 Section 4.1。\n\n**W2** [major] Filtering 实验效果量小（GSM8K +1.92pp, TruthfulQA +1.52pp, WinoGrande -0.79pp），作为贡献分量不足\n- 建议将 Section 5 明确定位为 consistency check 而非独立贡献。\n\n**W3** [major] Conclusion 过于简短（仅 5 行），缺 broader implications\n\n**W4** [minor-major] K* 符号系统过度增殖（K*, K*_empirical, K*_theory, K*_neural, K*_binary, K*_15D, K*_intrinsic, K*_PELT, K*_OBD）\n\n**W5** [minor] Related Work 遗漏 Fu et al. (2025) \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" (ICLR 2025)\n\n**W6** [minor] 3 个 orphan bib entries（hao2025rewrite, tang2024science, wu2023survey）+ levin2017markov 年份不一致\n\n### Questions\n\n**Q1**: DeBERTa-v3-base 只是 184M encoder，是否考虑过更大 encoder 验证 K*=2 upper bound？\n**Q2**: θ=0.60 的灵敏度是否会随更大模型或不同 domain 显著增加？\n**Q3**: Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3，是否暗示 K* 更多反映 domain-model interaction 而非 domain structural complexity？\n\n### Strengths\n**S1**: 研究问题新颖且实际意义明确\n**S2**: 实验统计方法论严谨出色\n**S3**: 域序 invariance 发现有价值\n**S4**: Limitations section 极其详尽和诚实\n**S5**: DeBERTa 与 15D 对比验证了 feature-set invariance\n\n---\n\n请对每个 Weakness（N1, N2, W1-W6）和 Question（Q1-Q3）逐条回应 [AGREE] 或 [REBUT]。",
    "project": "gen-depth-contamination",
    "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
  }
}
```

</details>

---


### Tool result

_source line 2165 · 2026-05-21T01:29:43.715004+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24974
}
```

</details>

---


### Tool call

_source line 2166 · 2026-05-21T01:29:43.919769+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性 + 实验设计）的完整审稿意见。请逐条回应：对每一个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n**Overall**: 3.5 — Borderline Conference\n\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 3/5\n\n### Weaknesses\n\n**W1** [Critical] θ=0.60 的选择存在循环论证风险\n- θ 从观测到的 AUC 分布中得出（1v2 聚集于 0.61-0.70, 2v3 聚集于 0.55-0.58），然后用 Youden's J 在同一数据上\"验证\"。LOFO 分析同样将 θ=0.60 作为 ground truth 而非待检验假设。\n- 多个配置的 CI lower bound 极接近 θ（Gemma-2-2B 下限距 θ 仅 0.25pp）。θ 微小变动（±2pp）即可改变边界配置的 K* 赋值。\n- 建议：held-out 验证（非 Qwen 上推导，Qwen 上验证）+ 详细灵敏度曲线（θ ∈ [0.55, 0.65] 每 0.01 步长）。\n\n**W2** [Critical] DPI → K* 的推理链存在逻辑缺口\n- DPI 保证互信息沿 Markov 链单调递减，但 K* 通过 adjacent-pair AUC 定义。从\"互信息递减\"到\"AUC 跌破 θ\"缺乏形式化桥梁。\n- 建议：重新定位 DPI 为\"经验动机\"而非\"形式化基础\"。\n\n**W3** [Major] K* 部分依赖分类器能力\n- DeBERTa 在 arXiv 上将 K* 从 2 扩展到 3-4，在 Wikipedia 上从 1 扩展到 2。K* 不是文本的固有属性而是 classifier-conditional 的。\n- 建议：明确区分 K*_15D 和 K*_DeBERTa，将当前结果定位为\"基于可解释特征的保守下界\"。\n\n**W4** [Major] 模型配置空间偏重 Qwen 家族\n- 10 配置中 Qwen 占 5 个。≥7B 仅 3 个模型，14B 仅 1 个。\n- 建议：补充实验或弱化可推广性声称。\n\n**W5** [Major] 过滤实验效果量不足\n- GSM8K +1.92pp, WinoGrande -0.79pp，效果量在 noise floor 内。Pythia 上 graduated filtering 不起作用。仅 30K 文档 + 5 seeds。\n- 建议：扩展实验或重新定位为\"初步探索性分析\"。\n\n**W6** [Minor] 跨模型迁移报告存在 framing 偏差\n- Abstract 强调 \"80-92% accuracy retention\"，但 4/6 off-diagonal 7B pairs 在边界处失败。\n- 建议：Abstract 同时提及边界处迁移限制。\n\n**W7** [Minor] Retrain-chain 与主实验统计方法不一致\n- 主实验用 bootstrap CI，retrain-chain 用 t-distribution CI。\n\n### Questions\n\n**Q1**: 是否考虑过将 θ 的推导和验证分开（held-out validation）？\n**Q2**: 实践者应使用 K*_15D=2 还是 K*_DeBERTa=3-4？\n**Q3**: Two-way ANOVA 交互效应显著（p<0.05, η²=0.03）是否与 \"generator-independent\" claim 矛盾？\n**Q4**: 30K 文档 + 5 seeds 是否足以检测 ~2pp 效果量？能否提供 power analysis？\n**Q5**: 混合 prompt-chain + retrain-chain 设置下 K* 如何估计？\n\n### Strengths\n**S1**: 新颖且有用的形式化框架\n**S2**: 系统性实验设计（10 configs × 4 domains × 4 decoding）\n**S3**: 统计严谨性的主体部分\n**S4**: 坦诚的局限讨论\n**S5**: Retrain-chain 对比提供有价值对照\n\n---\n\n请对每个 Weakness（W1-W7）和 Question（Q1-Q5）逐条回应 [AGREE] 或 [REBUT]。",
  "project": "gen-depth-contamination",
  "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性 + 实验设计）的完整审稿意见。请逐条回应：对每一个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n**Overall**: 3.5 — Borderline Conference\n\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 3/5\n\n### Weaknesses\n\n**W1** [Critical] θ=0.60 的选择存在循环论证风险\n- θ 从观测到的 AUC 分布中得出（1v2 聚集于 0.61-0.70, 2v3 聚集于 0.55-0.58），然后用 Youden's J 在同一数据上\"验证\"。LOFO 分析同样将 θ=0.60 作为 ground truth 而非待检验假设。\n- 多个配置的 CI lower bound 极接近 θ（Gemma-2-2B 下限距 θ 仅 0.25pp）。θ 微小变动（±2pp）即可改变边界配置的 K* 赋值。\n- 建议：held-out 验证（非 Qwen 上推导，Qwen 上验证）+ 详细灵敏度曲线（θ ∈ [0.55, 0.65] 每 0.01 步长）。\n\n**W2** [Critical] DPI → K* 的推理链存在逻辑缺口\n- DPI 保证互信息沿 Markov 链单调递减，但 K* 通过 adjacent-pair AUC 定义。从\"互信息递减\"到\"AUC 跌破 θ\"缺乏形式化桥梁。\n- 建议：重新定位 DPI 为\"经验动机\"而非\"形式化基础\"。\n\n**W3** [Major] K* 部分依赖分类器能力\n- DeBERTa 在 arXiv 上将 K* 从 2 扩展到 3-4，在 Wikipedia 上从 1 扩展到 2。K* 不是文本的固有属性而是 classifier-conditional 的。\n- 建议：明确区分 K*_15D 和 K*_DeBERTa，将当前结果定位为\"基于可解释特征的保守下界\"。\n\n**W4** [Major] 模型配置空间偏重 Qwen 家族\n- 10 配置中 Qwen 占 5 个。≥7B 仅 3 个模型，14B 仅 1 个。\n- 建议：补充实验或弱化可推广性声称。\n\n**W5** [Major] 过滤实验效果量不足\n- GSM8K +1.92pp, WinoGrande -0.79pp，效果量在 noise floor 内。Pythia 上 graduated filtering 不起作用。仅 30K 文档 + 5 seeds。\n- 建议：扩展实验或重新定位为\"初步探索性分析\"。\n\n**W6** [Minor] 跨模型迁移报告存在 framing 偏差\n- Abstract 强调 \"80-92% accuracy retention\"，但 4/6 off-diagonal 7B pairs 在边界处失败。\n- 建议：Abstract 同时提及边界处迁移限制。\n\n**W7** [Minor] Retrain-chain 与主实验统计方法不一致\n- 主实验用 bootstrap CI，retrain-chain 用 t-distribution CI。\n\n### Questions\n\n**Q1**: 是否考虑过将 θ 的推导和验证分开（held-out validation）？\n**Q2**: 实践者应使用 K*_15D=2 还是 K*_DeBERTa=3-4？\n**Q3**: Two-way ANOVA 交互效应显著（p<0.05, η²=0.03）是否与 \"generator-independent\" claim 矛盾？\n**Q4**: 30K 文档 + 5 seeds 是否足以检测 ~2pp 效果量？能否提供 power analysis？\n**Q5**: 混合 prompt-chain + retrain-chain 设置下 K* 如何估计？\n\n### Strengths\n**S1**: 新颖且有用的形式化框架\n**S2**: 系统性实验设计（10 configs × 4 domains × 4 decoding）\n**S3**: 统计严谨性的主体部分\n**S4**: 坦诚的局限讨论\n**S5**: Retrain-chain 对比提供有价值对照\n\n---\n\n请对每个 Weakness（W1-W7）和 Question（Q1-Q5）逐条回应 [AGREE] 或 [REBUT]。",
    "project": "gen-depth-contamination",
    "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
  }
}
```

</details>

---


### Tool result

_source line 2167 · 2026-05-21T01:29:45.429987+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Assistant

_source line 2168 · 2026-05-21T01:29:48.836863+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 162

## Round 162

2 recorded events


### User

_source line 2169 · 2026-05-21T01:29:51.509363+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成。核心评价：

- **Overall: 3.5（Borderline Conference）**，Soundness 3/5，Excitement 3/5
- **2 个 Critical 问题**: θ=0.60 的循环论证（数据驱动选择 + 同数据验证）、DPI→K* 的逻辑缺口（互信息 vs AUC 无形式化桥梁）
- **3 个 Major 问题**: K* 的分类器依赖性（DeBERTa 可将 K* 推至 3-4）、Qwen 占配置空间 50%、过滤效果量仅 1-2pp 且方向不一致
- **核心判断**: idea 新颖且实验广度优秀，但 claims 相对证据偏强。如果 Must-Fix 问题解决（θ 的 held-out 验证 + DPI framing 调整），有潜力达到 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2170 · 2026-05-21T01:29:56.559151+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 163

## Round 163

2 recorded events


### User

_source line 2171 · 2026-05-21T01:31:37.218536+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 对 Reviewer 1 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R1-W1: θ=0.60 的循环论证风险**
同意这是一个值得关注的问题，但严重程度需降级。论文并非完全循环：(1) Section 3.1 明确称 θ 为 "post-hoc operational threshold"，未声称 θ 有先验理论依据；(2) LOFO 交叉验证（Appendix，θ̂ ∈ [0.5725, 0.6004], 8/9 K* 匹配）本质上是一种 held-out validation（每次留出一个 family）；(3) Figure 2(b) 的灵敏度分析显示 K*=2 在 θ ∈ [0.575, 0.625] 稳定。R1 要求的 "non-Qwen 推导 + Qwen 验证" 在当前数据下可行，建议作者补充。但我认为这更接近 **Major** 而非 **Critical**，因为 LOFO 已部分解决了 held-out 问题。关于 marginal configurations（如 Qwen-cont CI lower 距 θ 仅 0.2pp），我在自己的 Q2 中也提出了类似关切。

**[REBUT] R1-W2: DPI → K* 的推理链逻辑缺口**
论文在 Section 3.1 已明确声明："DPI motivates finite K*_theory but does not formally guarantee or bound it"，并进一步解释 adjacent-pair convergence 来自 Markov chain 的 stationary distribution approach（cite Levin and Peres, 2017），而非直接从 DPI 推导。R1 的建议（"重新定位 DPI 为经验动机"）与论文当前的措辞基本一致。我认为这个 weakness 的前提不成立：论文并未将 DPI 作为 K* 的形式化基础，而是作为 monotonic information loss 的动机。可以在措辞上进一步弱化 DPI 的角色（例如将 "implies" 改为 "suggests"），但这不构成 Critical 问题。建议降至 **Minor**。

**[AGREE] R1-W3: K* 依赖分类器能力**
同意 K* 是 classifier-conditional 的，这是一个重要 caveat。但需要指出论文已在 Section 6（Discussion, "Feature-space ceiling" paragraph）明确讨论了这一点，并区分了：(a) domain ordering 是 feature-set invariant 的；(b) absolute K* 值是 feature-dependent 的；(c) C4/Code 上 K*_DeBERTa = K*_15D = 2 构成 representation-independent boundary（Table 3, Section 4.4）。论文当前的处理方式是合理的，但我同意 R1 的建议：应更系统地使用 K*_15D 和 K*_DeBERTa 符号来消除歧义（这与我自己的 W4 一致）。

**[AGREE] R1-W4: Qwen 家族过度代表**
完全同意。我在自己的审稿中也标记了这个问题。10 个配置中 Qwen 占 5 个，≥7B 仅 3 个模型（Qwen-7B, Qwen-14B, LLaMA-3.1-8B, Mistral-7B），14B 仅 1 个。Limitations (8) 虽然提及但不足以弥补。aggregate statistics 可能被 Qwen 特性主导。补充说明：cross-domain 实验（Table 4）中 Gemma-2-2B 和 OLMo-1B 多个 domain 缺失（标记为 "---"），进一步削弱了 family diversity。

**[AGREE] R1-W5: 过滤实验效果量不足**
完全同意。这与我自己的 W2 一致。GSM8K +1.92pp 和 TruthfulQA +1.52pp 在 5 seeds 的 variance 下可能不显著。WinoGrande -0.79pp 说明 binary filtering 并非无代价的。Graduated ≈ no-filter 的发现虽然支持 K*=2 的 consistency check 论点，但也表明 depth estimation 的 downstream utility 有限。建议与我相同：重新定位为 consistency check。

**[REBUT] R1-W6: 跨模型迁移的 framing 偏差**
Abstract 实际上已经同时报告了两面信息。原文（main.tex lines 42-43）："features transfer across generators (80--92\% aggregate accuracy, driven by high 0v1 separability), but boundary-level K* assignments fail under cross-model transfer (4/6 off-diagonal 7B pairs fall below θ)"。"but" 之后明确提到了边界处的迁移失败。R1 的 concern 可能基于不完整的 Abstract 阅读。不过 "driven by high 0v1 separability" 这个修饰确实暗示 80-92% 的高数字主要由 0v1 的 trivial separation 贡献，这一点的透明度是值得肯定的。建议降至非问题。

**[AGREE] R1-W7: Retrain-chain 统计方法不一致**
同意这是一个方法论不一致。主实验使用 bootstrap CI（1,000 或 10,000 resamples），retrain-chain 使用 t-distribution CI。虽然 retrain-chain 仅作为对比实验出现在 Discussion 和 Appendix 中，但统计方法应保持一致。这是一个容易修复的 Minor 问题。

---

### Questions 回应

**[AGREE] R1-Q1: θ 的 held-out validation**
LOFO 已提供部分 held-out validation（θ̂ ∈ [0.5725, 0.6004]），但 R1 提议的更严格 split（non-Qwen 推导 + Qwen 验证）值得执行。我补充一个关切：如果未来的模型/domain 产生的 AUC 分布不再呈现 1v2 和 2v3 之间的清晰 gap，θ 的选择可能不再稳健。

**[AGREE] R1-Q2: 实践者应使用 K*_15D 还是 K*_DeBERTa?**
论文没有给出明确的实践指导，这是一个缺陷。我的理解是：对 C4/Code（K*_15D = K*_DeBERTa = 2），两者等价；对 arXiv/Wikipedia，K*_DeBERTa 更高（3-4 / 2），但需要 fine-tuned encoder。论文应在 Discussion 中增加 "Practical Recommendations" 段落。

**[REBUT] R1-Q3: ANOVA 交互效应 vs. generator-independent claim**
η²=0.03 虽然统计显著（p<0.05），但效应量极小。在大样本量（37 configurations × 5 folds）下，即使微小的交互效应也会达到统计显著性。Section 4.3 的 cross-scorer ANOVA（Table in Appendix）显示 Depth-Pair 主效应 η²_p = 0.998，Scorer η²_p = 0.192，交互效应远小于主效应。论文的 "generator-independent" claim 应理解为 "largely generator-independent"（features 的 ranking 高度相关，ρ ≥ 0.85），而非绝对无交互。这与常规 NLP 实验的标准一致——完全零交互在任何实验中都不现实。建议作者将措辞从 "generator-independent" 调整为 "largely generator-invariant"。

**[AGREE] R1-Q4: Filtering 实验的 power analysis**
有效关切。30K 文档 × 5 seeds 检测 ~2pp 效果量，统计 power 可能不足。论文未提供 filtering 实验的 power analysis（主实验的 power curve 在 Appendix 中，但仅针对 K* determination，不针对 downstream filtering）。建议作者补充或在 Limitations 中明确声明 filtering 实验的 power 限制。

**[AGREE] R1-Q5: Mixed chain K* estimation**
同意这是一个重要的开放问题。论文在 Discussion Section 6（"Mixed-chain scenarios" paragraph）坦承 "whether prompt-chain laundering masks retrain-chain signals remains open"，并给出 K* ∈ [2, 7] 的区间。但对于实践者来说，这个区间太宽了。我在自己的 N1 中也强调了 prompt-chain vs. retrain-chain 的张力。不过，要求在一篇论文中解决 mixed-chain 问题可能超出合理范围，建议作为 future work 明确标注。

---

### 总结

R1 的审稿整体严谨，多数 concern 有据可依。主要分歧在：
1. **W2（DPI 逻辑缺口）**：论文已 explicitly 声明 DPI 不 formally guarantee K*，R1 的前提不完全成立，建议降级。
2. **W6（迁移 framing）**：Abstract 已包含边界处失败的信息，R1 可能遗漏了这一点。
3. **Q3（ANOVA 交互）**：η²=0.03 不足以推翻 generator-independent claim，但措辞可调整。

其余 W1, W3, W4, W5, W7 以及 Q1, Q2, Q4, Q5 均同意或部分同意。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2172 · 2026-05-21T01:31:43.427106+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 164

## Round 164

2 recorded events


### User

_source line 2173 · 2026-05-21T01:31:46.139087+00:00_

[Reviewer 2 审稿结果]:
已完成对 Reviewer 1 全部 7 个 Weakness 和 5 个 Question 的逐条回应，并发送给 Review Director。

总结：
- **[REBUT]** 2 条（W2: DPI 逻辑缺口论文已自行声明非 formal guarantee；W6: Abstract 已包含边界迁移失败信息）+ Q3（η²=0.03 效应量太小不足以推翻 claim）
- **[AGREE]** 其余全部（W1 θ 循环但建议降级为 Major、W3-W5 完全同意、W7 同意、Q1/Q2/Q4/Q5 同意）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2174 · 2026-05-21T01:31:50.774321+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 165

## Round 165

12 recorded events


### User

_source line 2175 · 2026-05-21T01:32:41.330600+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Introduction 以 model collapse 为动机但实验几乎全是 prompt-chain**

同意这是一个 framing 问题，但严重程度需要降级。论文在 Introduction 第一段右栏（page 1）已明确区分两者："in the model collapse literature, arises in both retrain-chains (iteratively training on model outputs) and prompt-chains (recursively prompting a fixed model to generate from its own prior outputs); we study prompt-chains, which isolate text-intrinsic information loss from training dynamics (Appendix D.1)." 因此并非完全未区分，而是区分的位置和力度不够。R2 建议在 Introduction 末尾提及 retrain-chain K*=7 是合理的，这能让读者更早理解两种设定的量化差异（K*=2 vs K*=7），强化 prompt-chain 聚焦的正当性。

补充我的观察：更深层的问题在于，Introduction 开篇引用的 Shumailov et al. (2024) 和 Dohmatob et al. (2024) 研究的是 retrain-chain collapse 的渐近行为，而本文的 prompt-chain 实验捕捉的是 text-intrinsic 信息损失。这两者的降退机制不同（权重累积偏移 vs 文本统计特征衰减），论文应该更明确地说明 prompt-chain 为何是实践中更相关的设定（web-scale 数据筛选场景），而不仅仅是说 "isolate text-intrinsic information loss"。

**[REBUT] R2-N2: K* 概念相对于 Geng et al. (2026) 和 Wang et al. (2025) 的增量贡献不够清晰**

我认为 R2 低估了 K* 与 Markov chain mixing time / attractor entry depth 之间的本质区别。K* 是一个 **classifier-operational** 指标——它回答的问题是"在给定特征集和分类器下，相邻代际的文本在多深处变得不可区分？"这是一个实用的数据筛选问题。相比之下，Geng et al. 的 Markov chain 收敛到 small cycle sets 是一个 distributional convergence 结果，Wang et al. 的 attractor cycles 是一个 dynamical systems 描述。

论文在 Related Work（page 3）已经明确承认 "the attractor entry depth may correspond to the discrimination boundary, though this parallel remains suggestive"，这个措辞准确地标注了两者的关系是未验证的猜测，而非已建立的等价。要求作者在 Section 3.1 中 formalize K* 与 mixing time 的关系（如 R2 所建议），实际上需要一个非平凡的数学证明——从 Markov chain mixing time 到 finite-sample AUC 的转换涉及大量分布假设和近似。这超出了一篇实证论文的合理范围。

K* 的真正增量贡献在于 **可操作性**：它提供了 per-text 的深度估计和直接的筛选阈值，而 mixing time / attractor depth 无法直接指导数据筛选。这一点在 Section 5 的 filtering 实验中得到（尽管效果微弱的）验证。论文不需要 formalize 与 mixing time 的关系，而需要更强调 K* 的操作层面独特性。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract 信息密度过高**

同意。Abstract 在未定义 K* 的前提下使用了 OBD-LightGBM、ISD、θ=0.60 等术语，并引用了 Section 4.1。对不熟悉该领域的读者来说，这构成了不必要的认知负担。建议 Abstract 前半部分用一句话直觉地解释 K*，然后再给出技术细节。

**[AGREE] R2-W2: Filtering 效果量不足以构成独立贡献**

强烈同意，这与我自己的 W5 一致。GSM8K +1.92pp、TruthfulQA +1.52pp、WinoGrande -0.79pp 的效果量在 benchmark 噪声范围内，且 Pythia 上 graduated filtering 产生 "a no-filter pattern"（Table 28, page 20）。R2 建议将 Section 5 定位为 "consistency check" 是务实且正确的重新定位策略。

**[AGREE] R2-W3: Conclusion 过于简短**

同意。Section 7（page 8）仅约 5 行，对一篇有 21 页附录的论文来说过于单薄。Conclusion 应至少包括：(1) K*=2 对 web-scale 数据筛选的实际指导意义；(2) prompt-chain vs retrain-chain K* 差异的 broader implications；(3) 未来工作方向（更大模型、更多域、classifier-independent K* 的追求）。

**[AGREE with nuance] R2-W4: K* 符号系统过度增殖**

部分同意。论文主文中主要使用 K* 和 K*_stop，符号负担可控。但在附录中确实出现了多个变体（K*_PELT, K*_neural 等），且没有一个统一的符号表。然而，R2 列举的某些变体（如 K*_empirical, K*_theory, K*_binary, K*_15D, K*_intrinsic）我在通读中并未全部发现作为正式定义的独立符号使用——部分可能是 R2 从上下文推断出的隐含变体，而非论文显式定义的符号。

建议：在 Section 3 或 Appendix 开头加一个简短的符号表，明确列出所有 K* 变体及其定义。主文中尽量只用 K*（默认 OBD-LightGBM + 15 ISD 特征），仅在需要对比时引入带下标的变体。

**[AGREE] R2-W5: 遗漏 Fu et al. (2025)**

同意这是一个相关引用。Fu et al. (2025) "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" 从理论角度分析如何防止 model collapse，与 Section 2 的 model collapse 讨论直接相关。应加入 Related Work Section 2.1。

**[AGREE] R2-W6: 3 个 orphan bib + levin2017markov 年份不一致**

同意，这些是我在引用验证中也发现的问题。levin2017markov 对应的是 Levin & Peres (2017) 第二版，而 OpenAlex 匹配到的是 2008 年第一版。年份标注为 2017 是正确的（如果引用的确实是第二版），但建议在 bib entry 中加上 "2nd edition" 以消除歧义。3 个 orphan entries 应删除或引用。

---

### Questions

**[AGREE] R2-Q1: 是否考虑更大 encoder 验证 K* upper bound**

很好的问题。这直接强化了我在 W3 中提出的分类器依赖性问题。DeBERTa-v3-base（184M）已将 arXiv K* 从 2 扩展到 3-4（Table 35, page 21）。如果 DeBERTa-large（304M）或 DeBERTa-xl（900M）能进一步扩展 K*，则 K*=2 越来越像是 feature set 的限制而非文本的内在属性。建议作者至少讨论为什么没有测试更大 encoder，以及这对 K* 解释的影响。

**[AGREE] R2-Q2: θ 灵敏度是否随模型规模/域变化**

同意这与我的 W1（θ 循环论证）互补。当前灵敏度分析（Appendix D.25）在现有 10 个配置上进行，表明 K* 在 θ ∈ [0.575, 0.625] 间稳定。但如果更大模型（如 14B+）或不同域的 AUC 分布不同（gap 位置不同），θ=0.60 可能不再是自然分界点。论文应讨论 θ 的域/规模依赖性。

**[AGREE with important caveat] R2-Q3: Mistral-7B 的域间 K* 差异是否暗示 domain-model interaction**

这是一个有洞察力的观察。从 Section 4.5（page 6-7）和 Table 10（page 14），Mistral-7B 在 C4 上 K*=1，而在 arXiv 上 K*=3（Section 4.5 报告 arXiv 上所有 5 个域适配模型均 K*=3）。这确实是从 1 到 3 的跃升。

然而，**论文的 domain ordering claim（arXiv > C4 > Code > Wikipedia）关注的是 ordering 的 invariance，而非 absolute K* 值的 invariance**。K*_arXiv > K*_C4 这一排序在 Mistral-7B 上依然成立（3 > 1），因此 ordering invariance 并未被违反。R2 的问题更准确地说挑战的是论文声称的 "structural complexity as the primary determinant"（Section 6, page 7-8）。如果 K* 是纯粹由 domain structural complexity 决定的，那么不同模型在同一 domain 上应该有相似的 K*。但 Mistral-7B 在 C4 上 K*=1（vs 其他模型 K*=2）表明模型因素也起显著作用。

我认为更准确的描述是：**domain 决定 ordering，但 model 决定 absolute level**。论文应在 Discussion 中更明确地讨论这一 interaction。

---

### 与我的 Round 1 意见的对照

R2 和我的审稿意见高度互补：
- **共同关注**：过滤效果量不足（我的 W5 = R2 的 W2）、K* 的分类器依赖性（我的 W3 与 R2 的 Q1 方向一致）
- **互补视角**：R2 更关注 framing/写作/novelty 定位（N1, N2, W1, W3），我更关注统计方法论（θ 循环论证、BH 校正范围、模型配置偏重）
- **评分一致**：我们都给出 3.5（Borderline Conference），关键问题集中在 claims 相对于证据偏强
- **唯一显著分歧**：N2。R2 认为 K* 对 Geng/Wang 的增量贡献不够清晰（critical），我认为两者研究的是不同层面的问题，K* 的操作层面独特性足够清晰（应为 minor-to-moderate 而非 critical）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2176 · 2026-05-21T01:33:23.255356+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查（外部审稿未启用）'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查（外部审稿未启用）'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2177 · 2026-05-21T01:33:23.255904+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2178 · 2026-05-21T01:33:26.774334+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2179 · 2026-05-21T01:33:26.827121+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T01:18:04.930184+00:00\", \"completed_at\": \"2026-05-21T01:21:59.178203+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本：Title + Abstract + Introduction）。Figure 1 出现在第 2 页顶部，距离足够近，审稿人翻页即可看到，影响不大。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（pipeline 图）作为首个 display item 效果良好：彩色框图清晰传达 Seed Text → Recursive Generation → 15D Feature → OBD-LightGBM → Output 的核心流程，caption 自包含，与 Title/Abstract 讲同一个 story。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"纯文本页（Related Works → Method 过渡），但前后页（p2 有 Figure 1、p4 有 Table 1）均有 display item，不构成连续纯文本问题。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 脚注字号偏小（约 6-7pt），包含多个统计注释（permutation p 值、rewrite mode 说明等）。审稿人可能需要放大阅读。建议适当增大脚注字号或精简脚注内容。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 三个子图各自较紧凑，axis tick labels 和 legend 字号接近正文 70% 下限。可读但不宽裕。如有空间可略微增大子图。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3（cross-model transfer heatmap）单元格内数字字号偏小，但配合颜色渐变仍可辨识。Caption 详细且自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"页面包含 Table 4 和 Table 5 两个表格，table-heavy 但内容不同（cross-domain vs filtering），布局合理。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 4（token-level JSD）使用 log scale + 多色线条 + 虚线/实线区分，可读性良好。线条颜色在白底上对比度充足。\"}, {\"severity\": \"warning\", \"dimension\": \"page 20\", \"message\": \"单页包含 8 个小表格（Tables 25-32），视觉极度拥挤。虽为 appendix，审稿人若查阅会感到信息过载。建议合并相关小表或分页。\"}, {\"severity\": \"info\", \"dimension\": \"page 22\", \"message\": \"Figure 8（retrain-chain AUC decay）清晰可读，线条和标注均充足。\"}, {\"severity\": \"info\", \"dimension\": \"page 24\", \"message\": \"Figure 10（feature group ablation heatmaps）双子图并排，颜色方案清晰，caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 28\", \"message\": \"Tables 49-
…[truncated 255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2180 · 2026-05-21T01:36:35.018883+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-contamination",
  "issues_yaml": "## Review Issues Tracker — gen-depth-contamination\n## Updated: Round 23 (fresh review, 2026-05-21, Overall 3.5)\n\n# === CRITICAL / MUST-FIX ===\n\n- id: \"R1-N1\"\n  summary: \"DPI→adjacent-pair AUC 推理链存在逻辑缺口\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。两者缺形式化桥梁。\"\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"DPI 约束累积信息量，K* 基于相邻对 AUC，后者取决于 Markov chain mixing rate。建议定位 DPI 为 motivating heuristic。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C1: Section 3.1 仍使用 'guarantee' 措辞。Section 6 自己承认 DPI 不 bound K*，但 3.1 不一致。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 再次标记为 Critical（W2）：从互信息递减到 AUC 跌破 θ 缺形式化桥梁。R2 rebut：论文已声明 'DPI motivates but does not formally guarantee'，措辞已基本到位，建议降级为 Minor。交叉后共识：framing 方向正确但仍可进一步弱化 DPI 角色（如 implies→suggests）。\"\n  action_items:\n    - round: 21\n      action: \"method.tex DPI 段落扩展 + Markov mixing 引用\"\n      assigned_to: paper_agent\n      status: done\n    - round: 22\n      action: \"全文 grep 'guarantee' 替换为 'motivate/imply'; Section 3.2 加 surprisal proxy framing\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"确认 Section 3.1 是否仍有 'guarantee/implies' 残留；如有则替换为 'motivates/suggests'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"θ 选在经验间隔处，K* 在 θ±5pp 就从3变1。\"\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"多个 configs CI lower 距 θ 不足 1pp。需分层报告 + 多重比较校正。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C2: AUC=0.60 分类能力弱。需 θ-sensitivity 完整表格 + Youden's J。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Critical（W1）：循环论证风险——θ 从 AUC 分布选出后用 Youden's J 在同一数据验证。建议 held-out validation（non-Qwen 推导 + Qwen 验证）。R2 agree 但建议降为 Major，因 LOFO（θ̂∈[0.5725,0.6004], 8/9 匹配）已部分提供 held-out 验证。共识：Youden's J + BH 校正 + LOFO 已有改善但 held-out split 更优。\"\n  action_items:\n    - round: 21\n      action: \"margin stratification 段落 + Abstract 'at θ=0.60' 限定\"\n      assigned_to: paper_agent\n      status: done\n    - round: 22\n      action: \"Agent 计算 θ-sensitivity 扩展(0.575/0.65) + Youden's J; Paper Agent 整合结果\"\n      assigned_to: agent+paper_agent\n      status: done\n    - round: 23\n      action: \"补充 held-out validation：non-Qwen 家族推导 θ，Qwen 家族验证（或反向）；报告 θ∈[0.55,0.65] 每 0.01 步长的 K* 赋值表\"\n      assigned_to: agent+paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C3\"\n  summary: \"Prompt-chain 焦点与 model collapse 叙事范围张力\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C3: Introduction 以 model collapse 为动机但实验几乎全是 prompt-chain。Retrain K*≈5-7 远高于 prompt-chain K*=2。建议以 web text curation 为独立动机。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 再次标记为 Critical（N1）。R1 agree 但认为论文已在 Introduction 第一段区分两者（'we study prompt-chains, which isolate text-intrinsic information loss'），问题在于区分的位置和力度不够。共识：Introduction 末尾应提及 retrain-chain K*=7，形成 K*∈[2,7] 完整图景；更明确说明 prompt-chain 为何是实践中更相关的设定。\"\n  action_items:\n    - round: 22\n      action: \"Introduction L4-7 调整：curation 为主线，model collapse 降为 background\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"Introduction 末尾加 retrain-chain K*=7 对比；强调 prompt-chain 对 web-scale curation 的实践相关性\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C4\"\n  summary: \"模型规模覆盖偏向小模型（7/10 ≤2B），威胁可推广性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C4: ≥7B 仅 3 种，14B 仅 1 种。需 'for models ≤14B' 限定 + K*_{15D} vs K*_{intrinsic} 区分。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Major（W4）：Qwen 占 5/10，≥7B 仅 3 个，14B 仅 Qwen。R2 完全同意，补充 cross-domain 实验中 Gemma/OLMo 多 domain 缺失进一步削弱 family diversity。共识：补充实验（如 Pythia-6.9B、LLaMA-3-1B）或显著弱化可推广性声称。\"\n  action_items:\n    - round: 22\n      action: \"Abstract/Conclusion 加 ≤14B 限定; Discussion 新段落 K*_{15D} vs K*_{intrinsic}\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"弱化跨架构可推广性声称为 'Qwen 内高度一致，其他家族单一规模点初步确认'；或补充至少 1 个非 Qwen 规模变体\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING / SHOULD-FIX ===\n\n- id: \"R1-W4\"\n  summary: \"K*=2 可能是 15D 特征空间容量上限（分类器依赖性）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"缺中间基线区分 feature ceiling 和 classifier capacity。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W4: DeBERTa arXiv K*=4 vs LightGBM K*=2-3。需 K*_{15D} vs K*_{intrinsic} 区分。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Major（W3）：DeBERTa 将 arXiv K* 推至 3-4、Wikipedia 从 1 到 2，K* 非文本固有属性而是 classifier-conditional。R2 agree，但指出 Section 6 已讨论 feature-space ceiling 且 C4/Code K*_DeBERTa=K*_15D=2 构成 representation-independent boundary。共识：需更系统使用 K*_15D 和 K*_DeBERTa 符号消除歧义；Discussion 增加实践者选择指南。\"\n  action_items:\n    - round: 22\n      action: \"Discussion 引入 K*_{15D} vs K*_{intrinsic}\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"Discussion 增加 'Practical Recommendations' 段落：C4/Code 两者等价，arXiv/Wikipedia K*_DeBERTa 更高但需 fine-tuned encoder\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Filtering 实验效果量在现实污染比例下极小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"10% 污染下 MMLU 改善约 0.2pp。建议降低 filtering 叙事权重。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W3: MMLU 改善约 0.76pp，仅 1-2 个下游任务。降级为 preliminary case study。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1（W5）和 R2（W2）强烈共识：GSM8K +1.92pp, TruthfulQA +1.52pp, WinoGrande -0.79pp 在 noise floor 内且方向不一致。Pythia graduated=no-filter。仅 30K docs + 5 seeds。共识：将 Section 5 重新定位为 consistency check 而非独立贡献；补充 power analysis 或在 Limitations 声明 power 限制。\"\n  action_items:\n    - round: 22\n      action: \"Section 5 reframe 为 consistency validation + 加过渡段\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"Section 5 标题/首句明确定位为 consistency check；讨论 WinoGrande 负面结果和 Pythia graduated failure；补充 filtering 的 power analysis 或 Limitations 声明\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"K* 变体在 Abstract 未解释。属 minor。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 标记为 Major（W1）：Abstract 在未定义 K* 的前提下使用 OBD-LightGBM、θ=0.60 等术语，并引用 Section 4.1。R1 agree。共识：Abstract 前半部分加一句直觉解释 K*，去掉 Section 引用和实现细节。\"\n  action_items:\n    - round: 23\n      action: \"Abstract 开头加一句 K* 直觉定义；移除 Section 引用；精简技术细节\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: R2\n      note: \"约 1/3 页，缺 broader implications。\"\n    - round: 21\n      reviewer: R1\n      note: \"[REBUT] 长度在 *ACL 正常范围。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 标记为 Major（W3）：仅 5 行。R1 agree。共识：扩展至 8-12 行，增加 K*=2 对 web-scale curation 的实际指导、prompt-chain vs retrain-chain broader implications、未来方向。\"\n  action_items:\n    - round: 21\n      action: \"conclusion.tex 从 6 行扩展到 ~13 行\"\n      assigned_to: paper_agent\n      status: done\n    - round: 23\n      action: \"Conclusion 是否已扩展？如仍 5 行则继续扩展至 8-12 行\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"与 Geng et al. (2026) 和 Wang et al. (2025) 的技术区分不够清晰\"\n  category: related_work\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"仅一句，未说明 discrimination boundary vs convergence analysis 区别。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W6: Markov chain 形式化与 Geng 高度相似。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 标记为 Critical（N2）：K* 相对 Geng Markov chain convergence 和 Wang attractor cycles 的增量贡献不清晰。R1 rebut：K* 是 classifier-operational 指标（per-text 可操作深度估计），与 distributional convergence / dynamical systems 描述是不同层面的问题，要求 formalize mixing time 关系超出实证论文范围。共识（分歧记录）：K* 的操作层面独特性需更显著强调，但不需要与 mixing time 的形式化关联。\"\n  action_items:\n    - round: 21\n      action: \"related_work.tex 扩展 Geng differentiation\"\n      assigned_to: paper_agent\n      status: done\n    - round: 23\n      action: \"Section 3.1 或 Related Work 更显著强调 K* 的 per-text operational 独特性 vs Geng/Wang 的 distributional convergence\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M2\"\n  summary: \"K* 符号系统过度增殖\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: R2\n      note: \"建议 Section 3.1 后添加 notation table。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 标记为 Minor-Major（W4）：K*, K*_empirical, K*_theory, K*_neural, K*_binary, K*_15D, K*_intrinsic, K*_PELT, K*_OBD 等过多变体。R1 部分同意但指出部分可能是 R2 从上下文推断而非论文显式定义。共识：主文仅用 K*（默认 15D+OBD），对比时引入带下标变体；Section 3 或 Appendix 加简短符号表。\"\n  action_items:\n    - round: 21\n      action: \"appendix.tex 新增 sec:notation 统一符号表\"\n      assigned_to: paper_agent\n      status: done\n    - round: 23\n      action: \"检查 notation table 是否覆盖所有 K* 变体；主文尽量统一为 K*，仅对比时引入下标\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-W1\"\n  summary: \"跨模型迁移 boundary-level 失败需更充分讨论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W1: 4/6 off-diagonal 7B pairs 失败对实际 curation 场景意味着 K* 估计不可靠。讨论仅一句。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Minor（W6）。R2 rebut：Abstract 已包含 'but boundary-level K* assignments fail under cross-model transfer (4/6 off-diagonal 7B pairs fall below θ)'。R1 接受 Abstract 已含信息，建议降级。共识：Abstract framing 已改善，但 Discussion 中 transfer implications 段落仍需更深入讨论实际 curation 影响。\"\n  action_items:\n    - round: 22\n      action: \"Discussion 增加段落：boundary failure 实际影响 + multi-source pooling 缓解\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"确认 Discussion transfer implications 段落是否充分讨论了实际影响\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-W5\"\n  summary: \"Retrain-chain CI 方法与主实验不一致\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W5: 主实验 bootstrap vs retrain-chain 5-fold t 分布。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Minor（W7）。R2 agree。共识：容易修复，说明 retrain-chain 使用 t-CI 的原因（仅 5 次重训练限制了 bootstrap）。\"\n  action_items:\n    - round: 22\n      action: \"Appendix D.1 加脚注说明 t-distribution 选择理由\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"确认脚注是否已添加；如未添加则补充说明 K=5 限制了 bootstrap 适用性\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === MINOR ===\n\n- id: \"R23-M1\"\n  summary: \"遗漏 Fu et al. (2025) ICLR 引用\"\n  category: related_work\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Fu et al. 'A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops' (ICLR 2025) 提出 recursive stability 和 self-consuming training loops 泛化分析，与 K* 有限边界概念直接相关。R2 提出，R1 agree。\"\n  action_items:\n    - round: 23\n      action: \"在 Related Work model collapse paragraph 增加 Fu et al. (2025) 引用\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M2\"\n  summary: \"3 个 orphan bib entries 未清理\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"hao2025rewrite, tang2024science, wu2023survey 在 .bib 中但未被引用。R2 提出，R1 agree。另 levin2017markov 年份需确认（2008 第一版 vs 2017 第二版）。\"\n  action_items:\n    - round: 23\n      action: \"删除 3 个 orphan bib entries；确认 Levin & Peres 引用版本并标注 edition\"\n      assigned_to: agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M3\"\n  summary: \"ANOVA 交互效应 vs generator-independent 措辞\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewer: [R1]\n      note: \"R1-Q3：Two-way ANOVA 交互效应显著（p<0.05, η²=0.03）。R2 rebut：效应量极小，大样本下 trivial interaction 也会显著。共识：将 'generator-independent' 调整为 'largely generator-invariant'。\"\n  action_items:\n    - round: 23\n      action: \"全文 grep 'generator-independent' 考虑替换为 'largely generator-invariant'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M3\"\n  summary: \"Appendix 交叉引用不一致\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewer: R1\n      note: \"Table 9 标题提到 'Table 4' 但正文 Table 4 是 cross-model transfer heatmap。\"\n    - round: 23\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"LOFO θ=0.60 验证存在数据层面依赖\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"LOFO 全在 C4 数据上。Wikipedia 仅 1/6 匹配。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"被 R1-N2 的 held-out validation 讨论吸收。LOFO 提供部分 held-out，但更严格 split 更优。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-Q6\"\n  summary: \"Generator identity AUC 数值不一致 (0.006 vs +0.008)\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"Q6: multi-source mixing 中 generator identity AUC=0.006，标准 AUC 下界 0.5。Introduction 写 +0.008。\"\n    - round: 23\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 22\n      action: \"Agent 核实实际数值并统一\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === RESOLVED (from prior rounds) ===\n\n- id: \"R2-N1\"\n  summary: \"Abstract 对迁移结果选择性报告\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"80-92% 掩盖 boundary-level fragility。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 rebut R1-W6：Abstract 已含 'but boundary-level K* assignments fail under cross-model transfer'。R1 接受。\"\n  resolution: \"Abstract 已包含边界迁移失败信息\"\n  resolution_round: 23\n\n- id: \"R2-M1\"\n  summary: \"holtzman2020curious orphan bib 条目\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"已删除\"\n  resolution_round: 21\n\n- id: \"R20-M4\"\n  summary: \"'model-free' 表述已改为 'generator-independent'\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"已全文替换\"\n  resolution_round: 21\n\n- id: \"R2-W2\"\n  summary: \"混合场景（prompt-chain + retrain-chain）未讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已加 Mixed-chain 段落\"\n  resolution_round: 21\n\n- id: \"R1-N3\"\n  summary: \"Qwen 家族 5/10 配置偏重，'7/9' 统计量误导\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已修改 framing 为 '4/6 families' primary\"\n  resolution_round: 21\n\n- id: \"R2-N2\"\n  summary: \"遗漏 Wang et al. (ACL 2025) 相关工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已添加引用\"\n  resolution_round: 21\n\n- id: \"R2-N3\"\n  summary: \"'One-wash laundering' framing 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已重写\"\n  resolution_round: 21"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-contamination",
    "issues_yaml": "## Review Issues Tracker — gen-depth-contamination\n## Updated: Round 23 (fresh review, 2026-05-21, Overall 3.5)\n\n# === CRITICAL / MUST-FIX ===\n\n- id: \"R1-N1\"\n  summary: \"DPI→adjacent-pair AUC 推理链存在逻辑缺口\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。两者缺形式化桥梁。\"\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"DPI 约束累积信息量，K* 基于相邻对 AUC，后者取决于 Markov chain mixing rate。建议定位 DPI 为 motivating heuristic。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C1: Section 3.1 仍使用 'guarantee' 措辞。Section 6 自己承认 DPI 不 bound K*，但 3.1 不一致。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 再次标记为 Critical（W2）：从互信息递减到 AUC 跌破 θ 缺形式化桥梁。R2 rebut：论文已声明 'DPI motivates but does not formally guarantee'，措辞已基本到位，建议降级为 Minor。交叉后共识：framing 方向正确但仍可进一步弱化 DPI 角色（如 implies→suggests）。\"\n  action_items:\n    - round: 21\n      action: \"method.tex DPI 段落扩展 + Markov mixing 引用\"\n      assigned_to: paper_agent\n      status: done\n    - round: 22\n      action: \"全文 grep 'guarantee' 替换为 'motivate/imply'; Section 3.2 加 surprisal proxy framing\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"确认 Section 3.1 是否仍有 'guarantee/implies' 残留；如有则替换为 'motivates/suggests'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"θ 选在经验间隔处，K* 在 θ±5pp 就从3变1。\"\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"多个 configs CI lower 距 θ 不足 1pp。需分层报告 + 多重比较校正。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C2: AUC=0.60 分类能力弱。需 θ-sensitivity 完整表格 + Youden's J。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Critical（W1）：循环论证风险——θ 从 AUC 分布选出后用 Youden's J 在同一数据验证。建议 held-out validation（non-Qwen 推导 + Qwen 验证）。R2 agree 但建议降为 Major，因 LOFO（θ̂∈[0.5725,0.6004], 8/9 匹配）已部分提供 held-out 验证。共识：Youden's J + BH 校正 + LOFO 已有改善但 held-out split 更优。\"\n  action_items:\n    - round: 21\n      action: \"margin stratification 段落 + Abstract 'at θ=0.60' 限定\"\n      assigned_to: paper_agent\n      status: done\n    - round: 22\n      action: \"Agent 计算 θ-sensitivity 扩展(0.575/0.65) + Youden's J; Paper Agent 整合结果\"\n      assigned_to: agent+paper_agent\n      status: done\n    - round: 23\n      action: \"补充 held-out validation：non-Qwen 家族推导 θ，Qwen 家族验证（或反向）；报告 θ∈[0.55,0.65] 每 0.01 步长的 K* 赋值表\"\n      assigned_to: agent+paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C3\"\n  summary: \"Prompt-chain 焦点与 model collapse 叙事范围张力\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C3: Introduction 以 model collapse 为动机但实验几乎全是 prompt-chain。Retrain K*≈5-7 远高于 prompt-chain K*=2。建议以 web text curation 为独立动机。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 再次标记为 Critical（N1）。R1 agree 但认为论文已在 Introduction 第一段区分两者（'we study prompt-chains, which isolate text-intrinsic information loss'），问题在于区分的位置和力度不够。共识：Introduction 末尾应提及 retrain-chain K*=7，形成 K*∈[2,7] 完整图景；更明确说明 prompt-chain 为何是实践中更相关的设定。\"\n  action_items:\n    - round: 22\n      action: \"Introduction L4-7 调整：curation 为主线，model collapse 降为 background\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"Introduction 末尾加 retrain-chain K*=7 对比；强调 prompt-chain 对 web-scale curation 的实践相关性\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C4\"\n  summary: \"模型规模覆盖偏向小模型（7/10 ≤2B），威胁可推广性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C4: ≥7B 仅 3 种，14B 仅 1 种。需 'for models ≤14B' 限定 + K*_{15D} vs K*_{intrinsic} 区分。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Major（W4）：Qwen 占 5/10，≥7B 仅 3 个，14B 仅 Qwen。R2 完全同意，补充 cross-domain 实验中 Gemma/OLMo 多 domain 缺失进一步削弱 family diversity。共识：补充实验（如 Pythia-6.9B、LLaMA-3-1B）或显著弱化可推广性声称。\"\n  action_items:\n    - round: 22\n      action: \"Abstract/Conclusion 加 ≤14B 限定; Discussion 新段落 K*_{15D} vs K*_{intrinsic}\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"弱化跨架构可推广性声称为 'Qwen 内高度一致，其他家族单一规模点初步确认'；或补充至少 1 个非 Qwen 规模变体\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING / SHOULD-FIX ===\n\n- id: \"R1-W4\"\n  summary: \"K*=2 可能是 15D 特征空间容量上限（分类器依赖性）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"缺中间基线区分 feature ceiling 和 classifier capacity。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W4: DeBERTa arXiv K*=4 vs LightGBM K*=2-3。需 K*_{15D} vs K*_{intrinsic} 区分。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Major（W3）：DeBERTa 将 arXiv K* 推至 3-4、Wikipedia 从 1 到 2，K* 非文本固有属性而是 classifier-conditional。R2 agree，但指出 Section 6 已讨论 feature-space ceiling 且 C4/Code K*_DeBERTa=K*_15D=2 构成 representation-independent boundary。共识：需更系统使用 K*_15D 和 K*_DeBERTa 符号消除歧义；Discussion 增加实践者选择指南。\"\n  action_items:\n    - round: 22\n      action: \"Discussion 引入 K*_{15D} vs K*_{intrinsic}\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"Discussion 增加 'Practical Recommendations' 段落：C4/Code 两者等价，arXiv/Wikipedia K*_DeBERTa 更高但需 fine-tuned encoder\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Filtering 实验效果量在现实污染比例下极小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"10% 污染下 MMLU 改善约 0.2pp。建议降低 filtering 叙事权重。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W3: MMLU 改善约 0.76pp，仅 1-2 个下游任务。降级为 preliminary case study。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1（W5）和 R2（W2）强烈共识：GSM8K +1.92pp, TruthfulQA +1.52pp, WinoGrande -0.79pp 在 noise floor 内且方向不一致。Pythia graduated=no-filter。仅 30K docs + 5 seeds。共识：将 Section 5 重新定位为 consistency check 而非独立贡献；补充 power analysis 或在 Limitations 声明 power 限制。\"\n  action_items:\n    - round: 22\n      action: \"Section 5 reframe 为 consistency validation + 加过渡段\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"Section 5 标题/首句明确定位为 consistency check；讨论 WinoGrande 负面结果和 Pythia graduated failure；补充 filtering 的 power analysis 或 Limitations 声明\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"K* 变体在 Abstract 未解释。属 minor。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 标记为 Major（W1）：Abstract 在未定义 K* 的前提下使用 OBD-LightGBM、θ=0.60 等术语，并引用 Section 4.1。R1 agree。共识：Abstract 前半部分加一句直觉解释 K*，去掉 Section 引用和实现细节。\"\n  action_items:\n    - round: 23\n      action: \"Abstract 开头加一句 K* 直觉定义；移除 Section 引用；精简技术细节\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: R2\n      note: \"约 1/3 页，缺 broader implications。\"\n    - round: 21\n      reviewer: R1\n      note: \"[REBUT] 长度在 *ACL 正常范围。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 标记为 Major（W3）：仅 5 行。R1 agree。共识：扩展至 8-12 行，增加 K*=2 对 web-scale curation 的实际指导、prompt-chain vs retrain-chain broader implications、未来方向。\"\n  action_items:\n    - round: 21\n      action: \"conclusion.tex 从 6 行扩展到 ~13 行\"\n      assigned_to: paper_agent\n      status: done\n    - round: 23\n      action: \"Conclusion 是否已扩展？如仍 5 行则继续扩展至 8-12 行\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"与 Geng et al. (2026) 和 Wang et al. (2025) 的技术区分不够清晰\"\n  category: related_work\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"仅一句，未说明 discrimination boundary vs convergence analysis 区别。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W6: Markov chain 形式化与 Geng 高度相似。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 标记为 Critical（N2）：K* 相对 Geng Markov chain convergence 和 Wang attractor cycles 的增量贡献不清晰。R1 rebut：K* 是 classifier-operational 指标（per-text 可操作深度估计），与 distributional convergence / dynamical systems 描述是不同层面的问题，要求 formalize mixing time 关系超出实证论文范围。共识（分歧记录）：K* 的操作层面独特性需更显著强调，但不需要与 mixing time 的形式化关联。\"\n  action_items:\n    - round: 21\n      action: \"related_work.tex 扩展 Geng differentiation\"\n      assigned_to: paper_agent\n      status: done\n    - round: 23\n      action: \"Section 3.1 或 Related Work 更显著强调 K* 的 per-text operational 独特性 vs Geng/Wang 的 distributional convergence\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M2\"\n  summary: \"K* 符号系统过度增殖\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: R2\n      note: \"建议 Section 3.1 后添加 notation table。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 标记为 Minor-Major（W4）：K*, K*_empirical, K*_theory, K*_neural, K*_binary, K*_15D, K*_intrinsic, K*_PELT, K*_OBD 等过多变体。R1 部分同意但指出部分可能是 R2 从上下文推断而非论文显式定义。共识：主文仅用 K*（默认 15D+OBD），对比时引入带下标变体；Section 3 或 Appendix 加简短符号表。\"\n  action_items:\n    - round: 21\n      action: \"appendix.tex 新增 sec:notation 统一符号表\"\n      assigned_to: paper_agent\n      status: done\n    - round: 23\n      action: \"检查 notation table 是否覆盖所有 K* 变体；主文尽量统一为 K*，仅对比时引入下标\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-W1\"\n  summary: \"跨模型迁移 boundary-level 失败需更充分讨论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W1: 4/6 off-diagonal 7B pairs 失败对实际 curation 场景意味着 K* 估计不可靠。讨论仅一句。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Minor（W6）。R2 rebut：Abstract 已包含 'but boundary-level K* assignments fail under cross-model transfer (4/6 off-diagonal 7B pairs fall below θ)'。R1 接受 Abstract 已含信息，建议降级。共识：Abstract framing 已改善，但 Discussion 中 transfer implications 段落仍需更深入讨论实际 curation 影响。\"\n  action_items:\n    - round: 22\n      action: \"Discussion 增加段落：boundary failure 实际影响 + multi-source pooling 缓解\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"确认 Discussion transfer implications 段落是否充分讨论了实际影响\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-W5\"\n  summary: \"Retrain-chain CI 方法与主实验不一致\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"W5: 主实验 bootstrap vs retrain-chain 5-fold t 分布。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R1 标记为 Minor（W7）。R2 agree。共识：容易修复，说明 retrain-chain 使用 t-CI 的原因（仅 5 次重训练限制了 bootstrap）。\"\n  action_items:\n    - round: 22\n      action: \"Appendix D.1 加脚注说明 t-distribution 选择理由\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 23\n      action: \"确认脚注是否已添加；如未添加则补充说明 K=5 限制了 bootstrap 适用性\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n# === MINOR ===\n\n- id: \"R23-M1\"\n  summary: \"遗漏 Fu et al. (2025) ICLR 引用\"\n  category: related_work\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Fu et al. 'A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops' (ICLR 2025) 提出 recursive stability 和 self-consuming training loops 泛化分析，与 K* 有限边界概念直接相关。R2 提出，R1 agree。\"\n  action_items:\n    - round: 23\n      action: \"在 Related Work model collapse paragraph 增加 Fu et al. (2025) 引用\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M2\"\n  summary: \"3 个 orphan bib entries 未清理\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"hao2025rewrite, tang2024science, wu2023survey 在 .bib 中但未被引用。R2 提出，R1 agree。另 levin2017markov 年份需确认（2008 第一版 vs 2017 第二版）。\"\n  action_items:\n    - round: 23\n      action: \"删除 3 个 orphan bib entries；确认 Levin & Peres 引用版本并标注 edition\"\n      assigned_to: agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M3\"\n  summary: \"ANOVA 交互效应 vs generator-independent 措辞\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewer: [R1]\n      note: \"R1-Q3：Two-way ANOVA 交互效应显著（p<0.05, η²=0.03）。R2 rebut：效应量极小，大样本下 trivial interaction 也会显著。共识：将 'generator-independent' 调整为 'largely generator-invariant'。\"\n  action_items:\n    - round: 23\n      action: \"全文 grep 'generator-independent' 考虑替换为 'largely generator-invariant'\"\n      assigned_to: paper_agent\n      status: pending\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M3\"\n  summary: \"Appendix 交叉引用不一致\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewer: R1\n      note: \"Table 9 标题提到 'Table 4' 但正文 Table 4 是 cross-model transfer heatmap。\"\n    - round: 23\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"LOFO θ=0.60 验证存在数据层面依赖\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 20\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"LOFO 全在 C4 数据上。Wikipedia 仅 1/6 匹配。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"被 R1-N2 的 held-out validation 讨论吸收。LOFO 提供部分 held-out，但更严格 split 更优。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-Q6\"\n  summary: \"Generator identity AUC 数值不一致 (0.006 vs +0.008)\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"Q6: multi-source mixing 中 generator identity AUC=0.006，标准 AUC 下界 0.5。Introduction 写 +0.008。\"\n    - round: 23\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 22\n      action: \"Agent 核实实际数值并统一\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === RESOLVED (from prior rounds) ===\n\n- id: \"R2-N1\"\n  summary: \"Abstract 对迁移结果选择性报告\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  mentions:\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"80-92% 掩盖 boundary-level fragility。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"R2 rebut R1-W6：Abstract 已含 'but boundary-level K* assignments fail under cross-model transfer'。R1 接受。\"\n  resolution: \"Abstract 已包含边界迁移失败信息\"\n  resolution_round: 23\n\n- id: \"R2-M1\"\n  summary: \"holtzman2020curious orphan bib 条目\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"已删除\"\n  resolution_round: 21\n\n- id: \"R20-M4\"\n  summary: \"'model-free' 表述已改为 'generator-independent'\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"已全文替换\"\n  resolution_round: 21\n\n- id: \"R2-W2\"\n  summary: \"混合场景（prompt-chain + retrain-chain）未讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已加 Mixed-chain 段落\"\n  resolution_round: 21\n\n- id: \"R1-N3\"\n  summary: \"Qwen 家族 5/10 配置偏重，'7/9' 统计量误导\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已修改 framing 为 '4/6 families' primary\"\n  resolution_round: 21\n\n- id: \"R2-N2\"\n  summary: \"遗漏 Wang et al. (ACL 2025) 相关工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已添加引用\"\n  resolution_round: 21\n\n- id: \"R2-N3\"\n  summary: \"'One-wash laundering' framing 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已重写\"\n  resolution_round: 21"
  }
}
```

</details>

---


### Tool result

_source line 2181 · 2026-05-21T01:36:35.119979+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml\", \"bytes\": 17140}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2182 · 2026-05-21T01:39:06.058118+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — gen-depth-contamination (Round 23, Fresh Review)\n\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Deadline**: 2026-05-25 (AoE)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work+写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 1 轮收敛\n\n---\n\n## Summary\n\n本文形式化了 K*（递归合成文本中分类器能可靠区分相邻代际的最大生成深度），使用 15 个统计特征和 OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族，1B-14B）上测量得出 prompt-chain 模式下 K*≤2（θ=0.60）。论文报告了特征集不变的域排序（arXiv>C4=Code>Wikipedia）、跨模型迁移结果（80-92% 准确率保留但边界处脆弱）、以及 K*-一致过滤的下游评估。DeBERTa fine-tuning 验证了域排序的 feature-set invariance，在 C4/Code 上匹配 15D 边界（K*=2），在 arXiv/Wikipedia 上推高 K*，确立 15D 为保守下界。\n\n---\n\n## Strengths\n\n**S1. 新颖且有用的形式化框架** [R1, R2 共识]\nK* 概念填补了 binary detection 和 population-level model collapse 分析之间的空白，提供 per-text 可操作深度估计，直接连接数据筛选需求。研究问题定义清晰，实际意义明确。\n\n**S2. 系统性实验设计** [R1, R2 共识]\n10 配置 × 4 域 × 4 解码策略的覆盖面在同类工作中属前列。域排序通过 changepoint 分析（PELT）、margin stratification、LOFO cross-validation 三重验证。\n\n**S3. 统计方法论严谨** [R1, R2 共识]\nBootstrap CI（1,000/10,000 resamples）、置换检验（p≤10⁻⁴）、BH 校正（q_max=0.003）、GroupKFold、Youden's J 分析。统计方法论的主体框架正确且在 NLP 论文中少见。\n\n**S4. 极其坦诚的 Limitations** [R1, R2 共识]\n9 项详尽的 Limitations 覆盖 scope、protocol、threshold、marginal boundary、feature set、segment length、curation applicability、family balance、transfer coverage，体现良好学术诚信。\n\n**S5. 域排序 invariance 发现** [R1, R2 共识]\narXiv(K*=3) > C4(K*=2) = Code(K*=2) > Wikipedia(K*=1) 在两种特征体系（15D 和 DeBERTa）下均成立，是有价值的新经验知识。\n\n**S6. Retrain-chain 对比** [R1]\nAppendix 中 retrain-chain K*=7（vs prompt-chain K*=2）有效区分了 text-intrinsic 信息损失和累积模型适应伪影。Figure 4 JSD 衰减曲线提供很好的互补证据。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. θ=0.60 的选择存在循环论证风险** [R1 Critical, R2 Agree(降为 Major)]\nθ 从观测到的 AUC 分布中得出（1v2 聚集于 0.61-0.70，2v3 聚集于 0.55-0.59），然后用 Youden's J 在同一数据上\"验证\"。LOFO（θ̂∈[0.5725,0.6004]，8/9 K* 匹配）提供了部分 held-out 验证，但不足以完全消解循环性。多个配置 CI lower 距 θ 不足 1pp（Qwen-cont 0.2pp，OLMo 0.5pp，LLaMA-8B 0.3pp）。\n- **Action**: 补充 held-out validation（non-Qwen 推导 + Qwen 验证或反向）；报告 θ∈[0.55,0.65] 每 0.01 步长的 K* 赋值表；明确标注 marginal cases。\n\n**C2. Prompt-chain 焦点与 model collapse 叙事范围存在张力** [R2 Critical, R1 Agree(降级)]\nIntroduction 以 retrain-chain model collapse 为核心动机（引用 Shumailov 2024, Dohmatob 2024），但全部主实验在 prompt-chain 下进行。论文在 Introduction 第一段已区分两者（\"we study prompt-chains\"），但区分的位置和力度不够。Retrain-chain K*=7 仅在 Appendix 出现。\n- **Action**: Introduction 末尾提及 retrain-chain K*=7，形成 K*∈[2,7] 完整图景；更明确说明 prompt-chain 对 web-scale curation 的实践相关性。\n\n**C3. 模型配置空间偏重 Qwen 家族** [R1 Major, R2 Agree]\n10 配置中 Qwen 占 5 个（continuation-mode 4/9），≥7B 仅 3 个模型，14B 仅 Qwen-2.5-14B。Cross-domain 实验中 Gemma-2-2B 和 OLMo-1B 多个 domain 缺失。当 K*≤2 结论主要由 Qwen 变体驱动时，跨架构可推广性声称被削弱。\n- **Action**: 补充至少 1 个非 Qwen 规模变体（如 Pythia-6.9B、LLaMA-3-1B），或显著弱化可推广性声称。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. K* 部分依赖分类器能力，非文本固有属性** [R1 Major, R2 Agree]\nDeBERTa 将 arXiv K* 从 2-3 扩展到 3-4，Wikipedia 从 1 到 2。C4/Code 上 K*_DeBERTa=K*_15D=2 构成 representation-independent boundary，但其他域不然。论文的叙事（Title \"Measuring the Discrimination Boundary\"）暗示 K* 是文本内在属性。\n- **Action**: 更系统使用 K*_15D 和 K*_DeBERTa 符号；Discussion 增加 Practical Recommendations 段落。\n\n**W2. Filtering 实验效果量不足** [R1 Major, R2 Major, 强共识]\nGSM8K +1.92pp, TruthfulQA +1.52pp, WinoGrande -0.79pp（负面！），效果量在 benchmark noise floor 内且方向不一致。Pythia 上 graduated=no-filter。仅 30K docs + 5 seeds，统计 power 可能不足。\n- **Action**: 将 Section 5 明确定位为 consistency check 而非独立贡献；讨论 WinoGrande 负面结果和 Pythia graduated failure；补充 power analysis 或 Limitations 声明。\n\n**W3. Abstract 信息密度过高** [R2 Major, R1 Agree]\nAbstract 在未定义 K* 的前提下使用 OBD-LightGBM、θ=0.60、margin stratification 等术语，并引用 Section 4.1（在 ACL 论文中不常见）。\n- **Action**: 前半部分加一句 K* 直觉定义，移除 Section 引用，精简实现细节。\n\n**W4. Conclusion 过于简短** [R2 Major, R1 Agree]\nSection 7 仅约 5 行，对一篇有 21 页附录的论文来说过于单薄。缺 broader implications 和 actionable takeaways。\n- **Action**: 扩展至 8-12 行，包括 K*=2 对 web-scale curation 的指导、prompt-chain vs retrain-chain 的 broader implications、未来方向。\n\n**W5. K* 符号系统过度增殖** [R2 Minor-Major, R1 部分同意]\nK*, K*_empirical, K*_theory, K*_neural, K*_binary, K*_15D, K*_intrinsic 等变体过多。部分可能是隐含变体而非显式定义，但仍增加认知负担。\n- **Action**: 主文统一为 K*（默认 15D+OBD），仅对比时引入带下标变体；确认 notation table 覆盖完整。\n\n### Minor\n\n**M1. 遗漏 Fu et al. (2025) 引用** [R2, R1 Agree]\n\"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" (ICLR 2025) 与 K* 有限边界概念直接相关。\n\n**M2. 3 个 orphan bib entries** [R2, R1 Agree]\nhao2025rewrite, tang2024science, wu2023survey 未被引用。levin2017markov 年份需确认版本。\n\n**M3. ANOVA 交互 vs generator-independent 措辞** [R1 Q3, R2 rebut 效应量极小]\nη²=0.03 统计显著但效应量可忽略。建议将 \"generator-independent\" 调整为 \"largely generator-invariant\"。\n\n**M4. Retrain-chain CI 方法与主实验不一致** [R1, R2 Agree]\n主实验用 bootstrap CI，retrain-chain 用 t-distribution CI（K=5）。应说明选择理由。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **θ 验证需加强**：LOFO 提供部分 held-out，但更严格的 family-split validation 更优（R1-W1, R2 agree）\n2. **K* 是 classifier-conditional 的**：需更清晰的 K*_15D vs K*_DeBERTa framing（R1-W3, R2 agree）\n3. **Qwen 过度代表**：可推广性声称需弱化或补充实验（R1-W4, R2-W4 均标记）\n4. **Filtering 应定位为 consistency check**：效果量不足以支撑独立贡献（R1-W5, R2-W2 强共识）\n5. **Abstract 需精简**：加 K* 直觉定义，去 Section 引用（R2-W1, R1 agree）\n6. **Conclusion 需扩展**：增 broader implications（R2-W3, R1 agree）\n7. **Missing reference**: Fu et al. (2025) ICLR（R2-W5, R1 agree）\n8. **Orphan bib entries**: 3 个需清理（R2-W6, R1 agree）\n9. **统计方法一致性**: retrain-chain CI 需说明理由（R1-W7, R2 agree）\n10. **评分一致**: 均 3.5 Borderline Conference\n\n## Reviewer Divergence [REBUT]\n\n**唯一显著分歧：DPI/novelty 的 framing 问题**\n\n两位 Reviewer 从不同角度标记了同一问题，但互相 rebut 了对方的版本：\n\n- **R1-W2（DPI→K* 逻辑缺口）**: R1 标记为 Critical。R2 **[REBUT]**: 论文已明确声明 \"DPI motivates but does not formally guarantee or bound K*\"（Section 3.1），且将 adjacent-pair convergence 归因于 Markov chain stationary distribution approach（cite Levin & Peres 2017）。R2 认为论文当前措辞基本到位，建议降至 Minor。\n\n- **R2-N2（K* vs Geng/Wang 增量贡献）**: R2 标记为 Critical。R1 **[REBUT]**: K* 是 classifier-operational 指标（per-text 可操作深度估计），与 Geng 的 distributional convergence 和 Wang 的 dynamical systems 描述是不同层面的问题。要求 formalize K* 与 mixing time 的关系需要非平凡的数学证明，超出实证论文合理范围。R1 建议降至 Minor-to-Moderate。\n\n**Director 评估**: 两个 REBUT 的方向一致——都认为对方标记的问题在论文中已有部分处理，不构成 Critical。但合并来看，DPI 的定位和 K* 相对于 convergence 概念的区分确实需要进一步强化。建议将两者合并为一个 Should-Fix：在 Section 3.1 和 Related Work 中更显著地强调 K* 的 per-text operational 独特性，同时确认 DPI 措辞无残留的 \"guarantee/implies\"。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1** [R1]: θ 的 held-out validation 是否可行？non-Qwen 推导 + Qwen 验证？\n**Q2** [R1, R2]: 实践者应使用 K*_15D=2 还是 K*_DeBERTa=3-4？论文缺明确指导。\n**Q3** [R2]: Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3，是否暗示 K* 更多反映 domain-model interaction 而非纯 domain structural complexity？（R1 同意但指出 ordering invariance 未被违反，更准确描述是\"domain 决定 ordering，model 决定 absolute level\"。）\n**Q4** [R1]: 30K 文档 + 5 seeds 是否足以检测 ~2pp 的 filtering 效果量？能否提供 power analysis？\n**Q5** [R1, R2]: 混合 prompt-chain + retrain-chain 设置下 K* 如何估计？K*∈[2,7] 区间对实践者过宽。\n**Q6** [R2]: 是否考虑过更大 encoder（DeBERTa-large/xl）验证 K*=2 upper bound？\n\n---\n\n## Missing References\n\n1. **Fu et al. (2025)** \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" (ICLR 2025, arXiv:2502.18865) — recursive stability 概念与 K* 有限边界相关 [R2 提出, R1 agree]\n2. **PAN@CLEF 2025 Generated Plagiarism Detection Task** — iterative LLM generation 检测 shared task [R2 提出]\n\n引用库验证：66 条中 58 条在线验证通过，4 条因较新未找到（均为真实论文），4 条轻微不匹配（年份/拼写），3 条 orphan，无伪造引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置 `external_review.paperreview_ai.enabled = false`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成（耗时约 4 分钟）\n\n**Findings**:\n- **0 Critical, 1 Warning, 12 Info**\n- ⚠️ Warning: Appendix page 20 单页包含 8 个小表格（Tables 25-32），视觉极度拥挤。建议合并或分页。\n- ℹ️ 主文布局合理：Figure 1（page 2）作为首个 display item 效果良好，pipeline 图清晰传达核心流程。\n- ℹ️ Table 2 脚注字号偏小（~6-7pt），Figure 2 子图 axis labels 接近可读下限，Figure 3 heatmap 数字字号偏小但配合颜色可辨识。\n- ℹ️ Page 7 包含 Table 4 + Table 5（cross-domain + filtering），table-heavy 但内容不同，布局合理。\n- ℹ️ Appendix 末页约 80% 填充，可接受。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**ACL ARR 维度评分（Reviewer 均值）**:\n\n| 维度 | R1 | R2 | 均值 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 3.0 | 4.0 | 3.5 |\n| Clarity | — | 3.5 | 3.5 |\n| Confidence | 4.0 | 4.0 | 4.0 |\n\n**判决理由**:\n\nK* 框架新颖且填补了文献真实空白（per-text 可操作深度估计），实验覆盖面广（10 配置 × 4 域 × 4 解码策略），域排序 invariance 是有价值的新发现，Limitations 极其坦诚。\n\n主要削弱因素：(1) θ=0.60 的选择虽有多重验证（Youden's J、BH 校正、LOFO、灵敏度分析）但缺真正独立的 held-out validation；(2) prompt-chain 焦点与 model collapse 动机的张力需更好弥合；(3) Qwen 占配置空间 50%；(4) filtering 效果量在 noise floor 内。核心问题不在实验执行质量（优秀），而在 claims 相对于证据偏强。\n\n**如果以下 Must-Fix 解决，有潜力提升至 4.0（Conference）**:\n1. θ 的 held-out validation（non-Qwen 推导 + Qwen 验证）\n2. Introduction framing 调整（prompt-chain 独立动机 + retrain-chain K*=7 对比）\n3. 弱化可推广性声称（限定 ≤14B，承认 Qwen 偏重）\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 开篇 model collapse 动机与 prompt-chain 实验的张力是两位 Reviewer 共同关注的最显著 framing 问题。建议在第一段即明确：(a) prompt-chain 和 retrain-chain 的降退机制不同（文本统计特征衰减 vs 权重累积偏移）；(b) prompt-chain 对 web-scale curation 更实际相关；(c) retrain-chain K*=7 提供 upper bound。\n- Contribution (c) 中 \"80-92% accuracy retention\" 已含 \"but boundary-level K* assignments fail\" caveat，framing 已改善。\n\n### Section 3 (Method)\n- Section 3.1 DPI 讨论：当前措辞（\"motivates but does not formally guarantee\"）方向正确，但检查是否有残留的 \"implies\" 或 \"guarantees\"。\n- θ=0.60：Youden's J（J=1.0 at config level, J=0.88 at fold level, θ*=0.605）和 BH 校正已有改善。建议补充 held-out family-split validation 和细粒度灵敏度表。\n\n### Section 4 (Experiments)\n- Table 2 中 marginal configurations 应有更显著的标注（如 bold/italic CI lower bounds within 1pp of θ）。\n- Cross-domain Table 4 中 Gemma/OLMo 的 \"---\" 需统一说明 convention。\n- Mistral-7B 的域间 K* 差异（C4=1, arXiv=3）值得在 Discussion 中更深入讨论 domain-model interaction vs pure domain complexity。\n\n### Section 5 (Filtering)\n- 当前标题 \"K*-Consistent Filtering\" 暗示独立贡献。建议改为 \"Consistency Validation: K*-Guided Filtering\" 或类似表述。\n- WinoGrande -0.79pp 和 Pythia graduated failure 需诚实讨论。\n\n### Section 6 (Discussion)\n- \"Feature-space ceiling\" 段落方向正确但需更明确的实践指导：C4/Code 用 K*_15D=K*_DeBERTa=2；arXiv/Wikipedia 用 K*_DeBERTa 更优但需 fine-tuned encoder。\n- \"Transfer implications\" 段落需更深入讨论 boundary failure 对实际 curation 的影响。\n\n### Section 7 (Conclusion)\n- 当前仅 5 行。建议扩展至 8-12 行。\n\n### References\n- 增加 Fu et al. (2025) ICLR；删除 3 个 orphan entries；确认 Levin & Peres 版本。\n\n### Format Compliance\n- ✅ Double-blind 匿名完整\n- ✅ 主文 8 页（Section 1-7），Limitations 从 page 8 中部开始（不计入页数限制）\n- ✅ Limitations section 存在且详尽（9 项）\n- ✅ Ethics Statement 存在且合理\n- ✅ ACL style with [review] option\n- ✅ 正文无破折号违规\n- ⚠️ 3 个 orphan bib entries 需清理",
  "project": "gen-depth-contamination",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — gen-depth-contamination (Round 23, Fresh Review)\n\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Deadline**: 2026-05-25 (AoE)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+Related Work+写作质量）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 1 轮收敛\n\n---\n\n## Summary\n\n本文形式化了 K*（递归合成文本中分类器能可靠区分相邻代际的最大生成深度），使用 15 个统计特征和 OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族，1B-14B）上测量得出 prompt-chain 模式下 K*≤2（θ=0.60）。论文报告了特征集不变的域排序（arXiv>C4=Code>Wikipedia）、跨模型迁移结果（80-92% 准确率保留但边界处脆弱）、以及 K*-一致过滤的下游评估。DeBERTa fine-tuning 验证了域排序的 feature-set invariance，在 C4/Code 上匹配 15D 边界（K*=2），在 arXiv/Wikipedia 上推高 K*，确立 15D 为保守下界。\n\n---\n\n## Strengths\n\n**S1. 新颖且有用的形式化框架** [R1, R2 共识]\nK* 概念填补了 binary detection 和 population-level model collapse 分析之间的空白，提供 per-text 可操作深度估计，直接连接数据筛选需求。研究问题定义清晰，实际意义明确。\n\n**S2. 系统性实验设计** [R1, R2 共识]\n10 配置 × 4 域 × 4 解码策略的覆盖面在同类工作中属前列。域排序通过 changepoint 分析（PELT）、margin stratification、LOFO cross-validation 三重验证。\n\n**S3. 统计方法论严谨** [R1, R2 共识]\nBootstrap CI（1,000/10,000 resamples）、置换检验（p≤10⁻⁴）、BH 校正（q_max=0.003）、GroupKFold、Youden's J 分析。统计方法论的主体框架正确且在 NLP 论文中少见。\n\n**S4. 极其坦诚的 Limitations** [R1, R2 共识]\n9 项详尽的 Limitations 覆盖 scope、protocol、threshold、marginal boundary、feature set、segment length、curation applicability、family balance、transfer coverage，体现良好学术诚信。\n\n**S5. 域排序 invariance 发现** [R1, R2 共识]\narXiv(K*=3) > C4(K*=2) = Code(K*=2) > Wikipedia(K*=1) 在两种特征体系（15D 和 DeBERTa）下均成立，是有价值的新经验知识。\n\n**S6. Retrain-chain 对比** [R1]\nAppendix 中 retrain-chain K*=7（vs prompt-chain K*=2）有效区分了 text-intrinsic 信息损失和累积模型适应伪影。Figure 4 JSD 衰减曲线提供很好的互补证据。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. θ=0.60 的选择存在循环论证风险** [R1 Critical, R2 Agree(降为 Major)]\nθ 从观测到的 AUC 分布中得出（1v2 聚集于 0.61-0.70，2v3 聚集于 0.55-0.59），然后用 Youden's J 在同一数据上\"验证\"。LOFO（θ̂∈[0.5725,0.6004]，8/9 K* 匹配）提供了部分 held-out 验证，但不足以完全消解循环性。多个配置 CI lower 距 θ 不足 1pp（Qwen-cont 0.2pp，OLMo 0.5pp，LLaMA-8B 0.3pp）。\n- **Action**: 补充 held-out validation（non-Qwen 推导 + Qwen 验证或反向）；报告 θ∈[0.55,0.65] 每 0.01 步长的 K* 赋值表；明确标注 marginal cases。\n\n**C2. Prompt-chain 焦点与 model collapse 叙事范围存在张力** [R2 Critical, R1 Agree(降级)]\nIntroduction 以 retrain-chain model collapse 为核心动机（引用 Shumailov 2024, Dohmatob 2024），但全部主实验在 prompt-chain 下进行。论文在 Introduction 第一段已区分两者（\"we study prompt-chains\"），但区分的位置和力度不够。Retrain-chain K*=7 仅在 Appendix 出现。\n- **Action**: Introduction 末尾提及 retrain-chain K*=7，形成 K*∈[2,7] 完整图景；更明确说明 prompt-chain 对 web-scale curation 的实践相关性。\n\n**C3. 模型配置空间偏重 Qwen 家族** [R1 Major, R2 Agree]\n10 配置中 Qwen 占 5 个（continuation-mode 4/9），≥7B 仅 3 个模型，14B 仅 Qwen-2.5-14B。Cross-domain 实验中 Gemma-2-2B 和 OLMo-1B 多个 domain 缺失。当 K*≤2 结论主要由 Qwen 变体驱动时，跨架构可推广性声称被削弱。\n- **Action**: 补充至少 1 个非 Qwen 规模变体（如 Pythia-6.9B、LLaMA-3-1B），或显著弱化可推广性声称。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. K* 部分依赖分类器能力，非文本固有属性** [R1 Major, R2 Agree]\nDeBERTa 将 arXiv K* 从 2-3 扩展到 3-4，Wikipedia 从 1 到 2。C4/Code 上 K*_DeBERTa=K*_15D=2 构成 representation-independent boundary，但其他域不然。论文的叙事（Title \"Measuring the Discrimination Boundary\"）暗示 K* 是文本内在属性。\n- **Action**: 更系统使用 K*_15D 和 K*_DeBERTa 符号；Discussion 增加 Practical Recommendations 段落。\n\n**W2. Filtering 实验效果量不足** [R1 Major, R2 Major, 强共识]\nGSM8K +1.92pp, TruthfulQA +1.52pp, WinoGrande -0.79pp（负面！），效果量在 benchmark noise floor 内且方向不一致。Pythia 上 graduated=no-filter。仅 30K docs + 5 seeds，统计 power 可能不足。\n- **Action**: 将 Section 5 明确定位为 consistency check 而非独立贡献；讨论 WinoGrande 负面结果和 Pythia graduated failure；补充 power analysis 或 Limitations 声明。\n\n**W3. Abstract 信息密度过高** [R2 Major, R1 Agree]\nAbstract 在未定义 K* 的前提下使用 OBD-LightGBM、θ=0.60、margin stratification 等术语，并引用 Section 4.1（在 ACL 论文中不常见）。\n- **Action**: 前半部分加一句 K* 直觉定义，移除 Section 引用，精简实现细节。\n\n**W4. Conclusion 过于简短** [R2 Major, R1 Agree]\nSection 7 仅约 5 行，对一篇有 21 页附录的论文来说过于单薄。缺 broader implications 和 actionable takeaways。\n- **Action**: 扩展至 8-12 行，包括 K*=2 对 web-scale curation 的指导、prompt-chain vs retrain-chain 的 broader implications、未来方向。\n\n**W5. K* 符号系统过度增殖** [R2 Minor-Major, R1 部分同意]\nK*, K*_empirical, K*_theory, K*_neural, K*_binary, K*_15D, K*_intrinsic 等变体过多。部分可能是隐含变体而非显式定义，但仍增加认知负担。\n- **Action**: 主文统一为 K*（默认 15D+OBD），仅对比时引入带下标变体；确认 notation table 覆盖完整。\n\n### Minor\n\n**M1. 遗漏 Fu et al. (2025) 引用** [R2, R1 Agree]\n\"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" (ICLR 2025) 与 K* 有限边界概念直接相关。\n\n**M2. 3 个 orphan bib entries** [R2, R1 Agree]\nhao2025rewrite, tang2024science, wu2023survey 未被引用。levin2017markov 年份需确认版本。\n\n**M3. ANOVA 交互 vs generator-independent 措辞** [R1 Q3, R2 rebut 效应量极小]\nη²=0.03 统计显著但效应量可忽略。建议将 \"generator-independent\" 调整为 \"largely generator-invariant\"。\n\n**M4. Retrain-chain CI 方法与主实验不一致** [R1, R2 Agree]\n主实验用 bootstrap CI，retrain-chain 用 t-distribution CI（K=5）。应说明选择理由。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **θ 验证需加强**：LOFO 提供部分 held-out，但更严格的 family-split validation 更优（R1-W1, R2 agree）\n2. **K* 是 classifier-conditional 的**：需更清晰的 K*_15D vs K*_DeBERTa framing（R1-W3, R2 agree）\n3. **Qwen 过度代表**：可推广性声称需弱化或补充实验（R1-W4, R2-W4 均标记）\n4. **Filtering 应定位为 consistency check**：效果量不足以支撑独立贡献（R1-W5, R2-W2 强共识）\n5. **Abstract 需精简**：加 K* 直觉定义，去 Section 引用（R2-W1, R1 agree）\n6. **Conclusion 需扩展**：增 broader implications（R2-W3, R1 agree）\n7. **Missing reference**: Fu et al. (2025) ICLR（R2-W5, R1 agree）\n8. **Orphan bib entries**: 3 个需清理（R2-W6, R1 agree）\n9. **统计方法一致性**: retrain-chain CI 需说明理由（R1-W7, R2 agree）\n10. **评分一致**: 均 3.5 Borderline Conference\n\n## Reviewer Divergence [REBUT]\n\n**唯一显著分歧：DPI/novelty 的 framing 问题**\n\n两位 Reviewer 从不同角度标记了同一问题，但互相 rebut 了对方的版本：\n\n- **R1-W2（DPI→K* 逻辑缺口）**: R1 标记为 Critical。R2 **[REBUT]**: 论文已明确声明 \"DPI motivates but does not formally guarantee or bound K*\"（Section 3.1），且将 adjacent-pair convergence 归因于 Markov chain stationary distribution approach（cite Levin & Peres 2017）。R2 认为论文当前措辞基本到位，建议降至 Minor。\n\n- **R2-N2（K* vs Geng/Wang 增量贡献）**: R2 标记为 Critical。R1 **[REBUT]**: K* 是 classifier-operational 指标（per-text 可操作深度估计），与 Geng 的 distributional convergence 和 Wang 的 dynamical systems 描述是不同层面的问题。要求 formalize K* 与 mixing time 的关系需要非平凡的数学证明，超出实证论文合理范围。R1 建议降至 Minor-to-Moderate。\n\n**Director 评估**: 两个 REBUT 的方向一致——都认为对方标记的问题在论文中已有部分处理，不构成 Critical。但合并来看，DPI 的定位和 K* 相对于 convergence 概念的区分确实需要进一步强化。建议将两者合并为一个 Should-Fix：在 Section 3.1 和 Related Work 中更显著地强调 K* 的 per-text operational 独特性，同时确认 DPI 措辞无残留的 \"guarantee/implies\"。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1** [R1]: θ 的 held-out validation 是否可行？non-Qwen 推导 + Qwen 验证？\n**Q2** [R1, R2]: 实践者应使用 K*_15D=2 还是 K*_DeBERTa=3-4？论文缺明确指导。\n**Q3** [R2]: Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3，是否暗示 K* 更多反映 domain-model interaction 而非纯 domain structural complexity？（R1 同意但指出 ordering invariance 未被违反，更准确描述是\"domain 决定 ordering，model 决定 absolute level\"。）\n**Q4** [R1]: 30K 文档 + 5 seeds 是否足以检测 ~2pp 的 filtering 效果量？能否提供 power analysis？\n**Q5** [R1, R2]: 混合 prompt-chain + retrain-chain 设置下 K* 如何估计？K*∈[2,7] 区间对实践者过宽。\n**Q6** [R2]: 是否考虑过更大 encoder（DeBERTa-large/xl）验证 K*=2 upper bound？\n\n---\n\n## Missing References\n\n1. **Fu et al. (2025)** \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" (ICLR 2025, arXiv:2502.18865) — recursive stability 概念与 K* 有限边界相关 [R2 提出, R1 agree]\n2. **PAN@CLEF 2025 Generated Plagiarism Detection Task** — iterative LLM generation 检测 shared task [R2 提出]\n\n引用库验证：66 条中 58 条在线验证通过，4 条因较新未找到（均为真实论文），4 条轻微不匹配（年份/拼写），3 条 orphan，无伪造引用。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置 `external_review.paperreview_ai.enabled = false`）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 已完成（耗时约 4 分钟）\n\n**Findings**:\n- **0 Critical, 1 Warning, 12 Info**\n- ⚠️ Warning: Appendix page 20 单页包含 8 个小表格（Tables 25-32），视觉极度拥挤。建议合并或分页。\n- ℹ️ 主文布局合理：Figure 1（page 2）作为首个 display item 效果良好，pipeline 图清晰传达核心流程。\n- ℹ️ Table 2 脚注字号偏小（~6-7pt），Figure 2 子图 axis labels 接近可读下限，Figure 3 heatmap 数字字号偏小但配合颜色可辨识。\n- ℹ️ Page 7 包含 Table 4 + Table 5（cross-domain + filtering），table-heavy 但内容不同，布局合理。\n- ℹ️ Appendix 末页约 80% 填充，可接受。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**ACL ARR 维度评分（Reviewer 均值）**:\n\n| 维度 | R1 | R2 | 均值 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 3.0 | 4.0 | 3.5 |\n| Clarity | — | 3.5 | 3.5 |\n| Confidence | 4.0 | 4.0 | 4.0 |\n\n**判决理由**:\n\nK* 框架新颖且填补了文献真实空白（per-text 可操作深度估计），实验覆盖面广（10 配置 × 4 域 × 4 解码策略），域排序 invariance 是有价值的新发现，Limitations 极其坦诚。\n\n主要削弱因素：(1) θ=0.60 的选择虽有多重验证（Youden's J、BH 校正、LOFO、灵敏度分析）但缺真正独立的 held-out validation；(2) prompt-chain 焦点与 model collapse 动机的张力需更好弥合；(3) Qwen 占配置空间 50%；(4) filtering 效果量在 noise floor 内。核心问题不在实验执行质量（优秀），而在 claims 相对于证据偏强。\n\n**如果以下 Must-Fix 解决，有潜力提升至 4.0（Conference）**:\n1. θ 的 held-out validation（non-Qwen 推导 + Qwen 验证）\n2. Introduction framing 调整（prompt-chain 独立动机 + retrain-chain K*=7 对比）\n3. 弱化可推广性声称（限定 ≤14B，承认 Qwen 偏重）\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 开篇 model collapse 动机与 prompt-chain 实验的张力是两位 Reviewer 共同关注的最显著 framing 问题。建议在第一段即明确：(a) prompt-chain 和 retrain-chain 的降退机制不同（文本统计特征衰减 vs 权重累积偏移）；(b) prompt-chain 对 web-scale curation 更实际相关；(c) retrain-chain K*=7 提供 upper bound。\n- Contribution (c) 中 \"80-92% accuracy retention\" 已含 \"but boundary-level K* assignments fail\" caveat，framing 已改善。\n\n### Section 3 (Method)\n- Section 3.1 DPI 讨论：当前措辞（\"motivates but does not formally guarantee\"）方向正确，但检查是否有残留的 \"implies\" 或 \"guarantees\"。\n- θ=0.60：Youden's J（J=1.0 at config level, J=0.88 at fold level, θ*=0.605）和 BH 校正已有改善。建议补充 held-out family-split validation 和细粒度灵敏度表。\n\n### Section 4 (Experiments)\n- Table 2 中 marginal configurations 应有更显著的标注（如 bold/italic CI lower bounds within 1pp of θ）。\n- Cross-domain Table 4 中 Gemma/OLMo 的 \"---\" 需统一说明 convention。\n- Mistral-7B 的域间 K* 差异（C4=1, arXiv=3）值得在 Discussion 中更深入讨论 domain-model interaction vs pure domain complexity。\n\n### Section 5 (Filtering)\n- 当前标题 \"K*-Consistent Filtering\" 暗示独立贡献。建议改为 \"Consistency Validation: K*-Guided Filtering\" 或类似表述。\n- WinoGrande -0.79pp 和 Pythia graduated failure 需诚实讨论。\n\n### Section 6 (Discussion)\n- \"Feature-space ceiling\" 段落方向正确但需更明确的实践指导：C4/Code 用 K*_15D=K*_DeBERTa=2；arXiv/Wikipedia 用 K*_DeBERTa 更优但需 fine-tuned encoder。\n- \"Transfer implications\" 段落需更深入讨论 boundary failure 对实际 curation 的影响。\n\n### Section 7 (Conclusion)\n- 当前仅 5 行。建议扩展至 8-12 行。\n\n### References\n- 增加 Fu et al. (2025) ICLR；删除 3 个 orphan entries；确认 Levin & Peres 版本。\n\n### Format Compliance\n- ✅ Double-blind 匿名完整\n- ✅ 主文 8 页（Section 1-7），Limitations 从 page 8 中部开始（不计入页数限制）\n- ✅ Limitations section 存在且详尽（9 项）\n- ✅ Ethics Statement 存在且合理\n- ✅ ACL style with [review] option\n- ✅ 正文无破折号违规\n- ⚠️ 3 个 orphan bib entries 需清理",
    "project": "gen-depth-contamination",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
  }
}
```

</details>

---


### Tool result

_source line 2183 · 2026-05-21T01:39:10.726304+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d2a0ec1de3a456564133278c1a9b203:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4668
}
```

</details>

---


### Tool call

_source line 2184 · 2026-05-21T01:39:23.008979+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查（外部审稿未启用）'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并搜索 EMNLP 2026 CFP'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查（外部审稿未启用）'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 交叉分享并逐条回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2185 · 2026-05-21T01:39:23.009513+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2186 · 2026-05-21T01:39:38.526323+00:00_

审稿流程完成。

**Round 23 (Fresh Review) 审稿报告已投递至 Research Director。**

核心结论：**3.5 Borderline Conference**（R1=3.5, R2=3.5，评分完全一致）。

3 个 Must-Fix：
1. θ=0.60 需 held-out validation（non-Qwen 推导 + Qwen 验证）
2. Introduction framing 调整（prompt-chain 独立动机 + retrain-chain K*=7 对比）
3. 弱化可推广性声称（Qwen 占 50% 配置空间）

4 个 Should-Fix：K* 分类器依赖需 framing 调整、Filtering 降级为 consistency check、Abstract 精简、Conclusion 扩展。

唯一分歧：DPI/novelty 的 framing——R1 认为 DPI→K* 是 Critical，R2 rebut 论文已 disclaimer；R2 认为 K* vs Geng/Wang 是 Critical，R1 rebut K* 操作层面足够独特。两个 REBUT 方向一致，已合并为 Should-Fix。

Issue tracker 已同步更新至 `review_issues.yaml`。视觉审查已完成（0 critical, 1 warning）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 166

## Round 166

2 recorded events


### User

_source line 2187 · 2026-05-21T01:39:41.205133+00:00_

[Reviewer 1 审稿结果]:
交叉回应完成。总结：

- R2 的 9 个 Weakness/Question 中，我 **[AGREE] 7 个**，**[AGREE with nuance] 2 个**（W4 符号增殖程度可能被高估，Q3 domain ordering invariance 本身未被违反但 absolute level 确有 interaction），**[REBUT] 1 个**（N2：K* 与 Geng/Wang 的增量贡献问题，我认为两者在不同层面，K* 的操作层面独特性足够清晰，不应标为 critical）。
- R2 和我的评分一致（3.5 Borderline Conference），核心共识是 claims 相对于证据偏强、过滤实验效果量不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2188 · 2026-05-21T01:39:53.860467+00:00_

审稿流程已全部完成。

**最终结果**：

- **Overall**: 3.5 Borderline Conference（R1、R2 一致）
- **审稿报告**已投递至 Research Director
- **Issue Tracker** 已同步更新（Round 23）
- **视觉审查**已完成并拼入报告（0 critical, 1 warning）

**核心问题摘要**：
1. θ=0.60 需 held-out validation（非循环验证）
2. Prompt-chain 焦点与 model collapse 动机需更好弥合
3. Qwen 占配置空间 50%，可推广性声称需弱化
4. Filtering 效果量不足，应降级为 consistency check

如果 Must-Fix 解决，有潜力提升至 4.0 Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 167

## Round 167

82 recorded events


### User

_source line 2189 · 2026-05-22T05:23:34.245069+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-contamination
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2190 · 2026-05-22T05:23:39.830591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2191 · 2026-05-22T05:23:39.881760+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2192 · 2026-05-22T05:23:45.604947+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 2193 · 2026-05-22T05:23:45.655699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2194 · 2026-05-22T05:23:50.225159+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2195 · 2026-05-22T05:23:51.631908+00:00_

{"result":"# 项目 gen-depth-contamination 概况\n\n## 实验状态 (156 个)\n\n- **exp_016_base_vs_instruct**: DONE (success) — \n- **exp_003_decoding_ablation**: DONE (success) — \n- **exp_004_7b_crossscale**: DONE (success) — \n- **exp_E_paired_stats**: DONE (success) — \n- **exp_D_obd_n500**: DONE (success) — \n- **exp_B_14d_ablation**: DONE (success) — \n- **exp_A_alt_scorer**: DONE (success) — \n- **exp_015_neural_probe**: DONE (success) — \n- **exp_006_graduated_filtering**: DONE (success) — \n- **exp_007_bootstrap_ci**: DONE (success) — \n- **exp_011_llm_zeroshot**: DONE (success) — \n- **exp_013_cross_transfer**: DONE (success) — \n- **exp_010_ordinal_baseline**: DONE (success) — \n- **exp_001_pythia_depth**: DONE (success) — \n- **mvp_pilot_sat_v1**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| seed_qwen15b_c4_s123 | Qwen-1.5B C4 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子 | — | — | — |\n| seed_qwen15b_wiki_s123 | Qwen-1.5B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子 | — | — | — |\n| seed_pythia14b_wiki_s123 | Pythia-1.4B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子 | — | — | — |\n\n## 待处理\n- 7b-cross-transfer（准备中）\n- arxiv_multi_source（准备中）\n- sweep_r10_nofilter（准备中）\n- sweep_r10_binary（准备中）\n- sweep_r10_graduated（准备中）\n- sweep_r30_nofilter（准备中）\n- sweep_eval_r10_nofilter（准备中）\n- sweep_eval_r10_binary（准备中）\n- sweep_eval_r10_graduated（准备中）\n- sweep_eval_r30_nofilter（准备中）\n- …另有 27 项\n\n## 近期结论\n- **exp_pythia69b_c4_nuc** (negative): Pythia-6.9B 在 C4 上使用 nucleus sampling（非 greedy）的 K*=2，与其他 continuation 模型的 decoding 策略对齐，消除 greedy 高估 confound。生成阶段自评，完成后用 Qwen-1.5B scorer 重跑 features+OBD（方案 2）。 ← 基于 exp_pythia69b_c4_depth_chain_v3\n  [pythia69b_nuc_final_report](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_pythia69b_c4_nuc/re
…[truncated 1201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 2196 · 2026-05-22T05:23:52.184881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2197 · 2026-05-22T05:23:52.436687+00:00_

1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure the discrimination boundary $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.
36	Across 10 model configurations (6 architecture families, 1B--8B), 3 source domains, and 4 decoding strategies, $\Kempirical \in \{1, 2, 3\}$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$): general web text yields $\Kempirical{=}2$ as the dominant mode (6/10 configurations), while structured academic text (arXiv) yields $\Kempirical{=}3$, validated across two architectures (Qwen-1.5B, Pythia-1.4B).
37	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
38	Model-free statistical features enable 80--100\% cross-model transfer with scorer-invariant feature ordering ($\rho > 0.90$), and cross-scorer validation confirms that $\Kempirical$ is governed by the generation process r
…[truncated 3641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2198 · 2026-05-22T05:23:52.437142+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2199 · 2026-05-22T05:23:52.537903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2200 · 2026-05-22T05:24:00.418955+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 2201 · 2026-05-22T05:24:01.323048+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2202 · 2026-05-22T05:24:02.578807+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-contamination",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2203 · 2026-05-22T05:24:06.191089+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's the information about EMNLP 2026 ARR submission guidelines:

## Page Limit Guidelines

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Important Submission Details

Authors will need to explicitly declare which conference they intend to commit to at submission time for the ARR 2026 May cycle, which is alig
…[truncated 558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5772
}
```

</details>

---


### Tool result

_source line 2204 · 2026-05-22T05:24:08.803063+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's what I found regarding ACL Rolling Review ARR May 2026 submission deadline and author guidelines:

## Submission and Author Registration

After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

## Author Guidelines

Starting in May 2025, all submitting authors have to also sign up as reviewers (deadline: 48h after the submission deadline), and the submission must adhere to the formatting in the submission templates, which is available as an Over
…[truncated 779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7480
}
```

</details>

---


### Tool result

_source line 2205 · 2026-05-22T05:24:08.803553+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6224
}
```

</details>

---


### Tool call

_source line 2206 · 2026-05-22T05:24:13.153114+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for papers page limit anonymity appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org call for papers page limit anonymity appendix"
  }
}
```

</details>

---


### Tool call

_source line 2207 · 2026-05-22T05:24:14.659271+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclrollingreview.org cfp 2026 page limit long short paper template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclrollingreview.org cfp 2026 page limit long short paper template"
  }
}
```

</details>

---


### Tool call

_source line 2208 · 2026-05-22T05:24:14.860384+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2209 · 2026-05-22T05:24:14.961146+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 2210 · 2026-05-22T05:24:19.779397+00:00_

Web search results for query: "site:aclrollingreview.org cfp 2026 page limit long short paper template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields","url":"http://aclrollingreview.org/submissionform"},{"title":"Discontinuation of the MS Word Template","url":"http://aclrollingreview.org/discontinuation-word-template"},{"title":"ARR Area Chair Guidelines","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"}]

Based on the search results from the ACL Rolling Review website, here is the key information about CFP 2026 page limits and templates:

## Page Limits

Long papers have a page limit of 8 pages, and short papers have a limit of 4 pages (not including limitations and ethical considerations).

## Paper Template

Paper submissions must use the official ACL style template. There is an official Overleaf template, and this template has a [review] setting that must be on for the submission.

It's important to note that ARR abandons the MS Word Template for conference submissions, and submissions based on the Word template will be desk-rejected starting from March 2026.

## Additional Formatting Requirements

All long, short, and theme papers must follow the ACL Author Guidelines. Submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be rejected witho
…[truncated 113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5120
}
```

</details>

---


### Tool result

_source line 2211 · 2026-05-22T05:24:27.208906+00:00_

Web search results for query: "site:2026.emnlp.org call for papers page limit anonymity appendix"

Links: [{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"}]

I found the EMNLP 2026 Call for Main Conference Papers. Let me search more specifically for the detailed submission guidelines including page limits, anonymity, and appendix information.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Guardians of the data: NER and LLMs for effective medical record anonymization in Brazilian Portuguese","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12813187/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Ten Simple Rules for writing algorithmic bioinformatics conference papers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7117650/"}]

Let me search for more specific details about page limits and appendix requirements.

Li
…[truncated 3666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 14055
}
```

</details>

---


### Tool call

_source line 2212 · 2026-05-22T05:24:41.697491+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "config",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-contamination",
    "file": "config",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2213 · 2026-05-22T05:24:43.153355+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 2214 · 2026-05-22T05:24:43.153793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2215 · 2026-05-22T05:24:43.505341+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure $\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features and an Ordinal Binary Decompositio
…[truncated 1337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2216 · 2026-05-22T05:24:43.505772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2217 · 2026-05-22T05:24:44.208924+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.
6	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
8	
9	\paragraph{Beyond binary detection.}
10	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
11	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
12	None estimates recursive generation depth.
13	
14	\paragraph{Data selection and curation.}
15	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
16	
17	\paragraph{Ordinal classification and probing.}
18	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2218 · 2026-05-22T05:24:44.209367+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2219 · 2026-05-22T05:24:44.259945+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this guarantees a finite $\Ktheory$ beyond which adjacent generations are indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a small-effect-size threshold (Cohen's $h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.}; justified below).
25	Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	
27	\paragraph{Threshold justification.}
28	$\theta{=}0.60$ is supported by three independent lines of evidence.
29	First, it corresponds to Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
30	Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.
…[truncated 4255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2220 · 2026-05-22T05:24:47.774411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---


### Tool result

_source line 2221 · 2026-05-22T05:24:48.276842+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on ten model configurations spanning six architecture families:
5	Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5024 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .4942 & 
…[truncated 9354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2222 · 2026-05-22T05:24:48.277239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
  }
}
```

</details>

---


### Tool result

_source line 2223 · 2026-05-22T05:24:48.277454+00:00_

1	\section{Application: $\Kstar$-Aware Data Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
6	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
12	\label{tab:tab_filtering_main}
13	\input{tables/tab_filtering_main}
14	\end{table}
15	
16	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
17	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
18	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
19	G
…[truncated 687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2224 · 2026-05-22T05:24:48.779676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2225 · 2026-05-22T05:24:48.780145+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
13	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
14	
15	\paragraph{Graduated filtering failure.}
16	For web text, 2v3 $\auc < \theta$ across all model configurations, so depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise, explaining convergence toward binary at high $\alpha$ (Appendix~\ref{sec:extended_limitations}).
17	DSIR fails differently: bigram hashing captures domain shift but not depth-correlated signatures.
18	
19	\paragraph{Representation dependence.}
20	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
21	The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
22	Cross-scorer validation confirms $\Kempirical$ is governed by the generation operator rather than the scoring model ($\rho > 0.90$ feature ranking preservation; length confound ruled out in Appendix~\ref{sec:extended_limitations}).
23	
24	\paragr
…[truncated 2531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2226 · 2026-05-22T05:24:49.181982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2227 · 2026-05-22T05:24:49.232600+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure the generational depth discrimination boundary $\Kempirical$ for recursive synthetic text.
5	$\Kempirical \in \{1, 2, 3\}$ depends on source domain and model characteristics: general web text yields $\Kempirical{=}2$ across 6/10 configurations (6 families, 1B--8B; $p \leq 0.002$), with $\Kempirical{=}3$ for academic text, confirmed across architectures (Qwen-1.5B, Pythia-1.4B).
6	Model-free features enable 80--100\% cross-model transfer ($\rho > 0.90$), and under sufficient contamination, domain-appropriate $\Kempirical$ correctly predicts optimal curation granularity.
7	Future work includes scaling to 13B+, additional structured domains, and retrain-chain $\Kstar$ characterization.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2228 · 2026-05-22T05:24:57.666470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2229 · 2026-05-22T05:24:58.621172+00:00_

1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	%% [Merged into Figure 2] \begin{figure}[t]
12	%% [Merged into Figure 2]   \centering
13	%% [Merged into Figure 2]   \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	%% [Merged into Figure 2]   \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	%% [Merged into Figure 2]   \label{fig:s1_auc_decay_ci}
16	%% [Merged into Figure 2] \end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
33	3 & \textbf{\texttt{surp\_std}} & \textbf{\t
…[truncated 26446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2230 · 2026-05-22T05:24:58.621609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
  }
}
```

</details>

---


### Tool result

_source line 2231 · 2026-05-22T05:24:59.174458+00:00_

1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--100\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}400$ (16 cells $\times$ 5 folds $\times$ 5 depth-pairs). The non-significant Scorer main effect confirms scorer independence of depth discrimination.}
26	\label{tab:anova_crossscorer}
27	\begin{tabular}{lrrrr}
28	\toprule
29	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \
…[truncated 7392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2232 · 2026-05-22T05:24:59.174976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2233 · 2026-05-22T05:24:59.627251+00:00_

1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-15
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{mitchell2023detectgpt,
31	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
32	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
33	  booktitle={Proceedings of ICML},
34	  year={2023}
35	}
36	
37	% === Should-Cite ===
38	
39	@article{basani2026diveye,
40	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
41	  author={Basani, Advik Raj and Chen, Pin-Yu},
42	  journal={Transactions on Machine Learning Research},
43	  issn={2835-8856},
44	  year={2026},
45	  url={https://arxiv.org/abs/2509.18880}
46	}
47	
48	@inproceedings{zawalski2026codec,
49	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
50	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira an
…[truncated 8717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2234 · 2026-05-22T05:24:59.627684+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-contamination/agent/config*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-contamination/agent/config*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2235 · 2026-05-22T05:24:59.678368+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2236 · 2026-05-22T05:25:03.947198+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-contamination/**/config*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-contamination/**/config*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2237 · 2026-05-22T05:25:04.449642+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2238 · 2026-05-22T05:25:04.450138+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-contamination/**/project.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-contamination/**/project.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2239 · 2026-05-22T05:25:04.550751+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2240 · 2026-05-22T05:25:06.003818+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination -name \"*.yaml\" -maxdepth 3 2>/dev/null | head -20",
  "description": "List YAML files in project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination -name \"*.yaml\" -maxdepth 3 2>/dev/null | head -20",
    "description": "List YAML files in project directory"
  }
}
```

</details>

---


### Tool result

_source line 2241 · 2026-05-22T05:25:06.154896+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/xie2024doremi.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/shumailov2024collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/gambetta2025surplexity.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/basani2026diveye.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/drayson2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/alemohammad2024selfconsuming.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/schaeffer2025position.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/kazdan2025collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/shi2025generalization.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/amin2025escaping.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/dohmatob2024model.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/tirumala2024d4.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/kirchenbauer2023watermark.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/falahati2026curated.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/zellers2019grover.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/xie2023dsir.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/distill_tmp/ippolito2020detection.yaml
/home/
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2242 · 2026-05-22T05:25:11.610211+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7 -maxdepth 2 -name \"config*.yaml\" -o -name \"project*.yaml\" -o -name \"settings*.yaml\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7 -maxdepth 2 -name \"config*.yaml\" -o -name \"project*.yaml\" -o -name \"settings*.yaml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2243 · 2026-05-22T05:25:11.665512+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 2244 · 2026-05-22T05:25:15.498984+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7 -maxdepth 1 -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | head -10",
  "description": "Find config files at root level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7 -maxdepth 1 -name \"*.yaml\" -o -name \"*.json\" 2>/dev/null | head -10",
    "description": "Find config files at root level"
  }
}
```

</details>

---


### Tool result

_source line 2245 · 2026-05-22T05:25:15.599831+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2246 · 2026-05-22T05:25:19.566385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2247 · 2026-05-22T05:25:19.616992+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2248 · 2026-05-22T05:25:23.288971+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10",
  "description": "Find config files in agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10",
    "description": "Find config files in agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 2249 · 2026-05-22T05:25:23.339707+00:00_

/home/ubuntu/agent-ml-research/workspace/config/approvals.yaml
/home/ubuntu/agent-ml-research/workspace/config/resources.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/aaai-2027.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/icml-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/neurips-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/acl-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/iclr-2027.yaml
/home/ubuntu/agent-ml-research/config/ralph_loop.yaml
/home/ubuntu/agent-ml-research/config/images.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2250 · 2026-05-22T05:25:26.703530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2251 · 2026-05-22T05:25:27.406740+00:00_

1	typesetting:
2	  layout: two_column
3	  max_pages: 8
4	  paper_size: a4
5	  column_width_cm: 7.7
6	  text_width_cm: 16.0
7	  column_sep_cm: 0.6
8	  template_sets:
9	    hyperref: true
10	  preamble_additions:
11	    packages: [microtype, booktabs, cleveref]
12	    float_params:
13	      topfraction: "0.85"
14	      bottomfraction: "0.85"
15	      textfraction: "0.15"
16	      floatpagefraction: "0.7"
17	    penalties:
18	      widowpenalty: "10000"
19	      clubpenalty: "10000"
20	  forbidden_packages: []
21	  required_sections:
22	    - name: Limitations
23	      severity: critical
24	    - name: Ethics Statement
25	      severity: warning
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2252 · 2026-05-22T05:25:27.810166+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_7/ --include=\"*.yaml\" --include=\"*.json\" --include=\"*.toml\" -l 2>/dev/null | head -5",
  "description": "Find external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_7/ --include=\"*.yaml\" --include=\"*.json\" --include=\"*.toml\" -l 2>/dev/null | head -5",
    "description": "Find external review config"
  }
}
```

</details>

---


### Tool result

_source line 2253 · 2026-05-22T05:25:27.961120+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2254 · 2026-05-22T05:25:33.884859+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-contamination/docs/paper/tables/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-contamination/docs/paper/tables/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 2255 · 2026-05-22T05:25:34.889068+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2256 · 2026-05-22T05:25:35.040110+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2257 · 2026-05-22T05:25:35.392120+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2258 · 2026-05-22T05:25:35.392537+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-contamination/artifacts/review_reports/*.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-contamination/artifacts/review_reports/*.md"
  }
}
```

</details>

---


### Tool result

_source line 2259 · 2026-05-22T05:25:35.493340+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2260 · 2026-05-22T05:25:40.583442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2261 · 2026-05-22T05:25:40.584342+00:00_

1	## Review Issues Tracker — gen-depth-contamination
2	## Updated: Round 23 (fresh review, 2026-05-21, Overall 3.5)
3	
4	# === CRITICAL / MUST-FIX ===
5	
6	- id: "R1-N1"
7	  summary: "DPI→adjacent-pair AUC 推理链存在逻辑缺口"
8	  category: method
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 20
12	  last_seen_round: 23
13	  mentions:
14	    - round: 20
15	      reviewer: R1
16	      note: "DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。两者缺形式化桥梁。"
17	    - round: 21
18	      reviewer: [R1, R2]
19	      note: "DPI 约束累积信息量，K* 基于相邻对 AUC，后者取决于 Markov chain mixing rate。建议定位 DPI 为 motivating heuristic。"
20	    - round: 22
21	      reviewer: [R1, R2]
22	      note: "C1: Section 3.1 仍使用 'guarantee' 措辞。Section 6 自己承认 DPI 不 bound K*，但 3.1 不一致。"
23	    - round: 23
24	      reviewer: [R1, R2]
25	      note: "R1 再次标记为 Critical（W2）：从互信息递减到 AUC 跌破 θ 缺形式化桥梁。R2 rebut：论文已声明 'DPI motivates but does not formally guarantee'，措辞已基本到位，建议降级为 Minor。交叉后共识：framing 方向正确但仍可进一步弱化 DPI 角色（如 implies→suggests）。"
26	  action_items:
27	    - round: 21
28	      action: "method.tex DPI 段落扩展 + Markov mixing 引用"
29	      assigned_to: paper_agent
30	      status: done
31	    - round: 22
32	      action: "全文 grep 'guarantee' 替换为 'motivate/imply'; Section 3.2 加 surprisal proxy framing"
33	      assigned_to: paper_agent
34	      status: in_progress
35	    - round: 23
36	      action: "确认 Section 3.1 是否仍有 'guarantee/implies' 残留；如有则替换为 'motivates/suggests'"
37	      assigned_to: paper_agent
38	      status: in_progress
39	  resolution: ""
40	  resolution_round: null
41	
42	- id: "R1-N2"
43	  summary: "θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱"
44	  category: experiment
45	  severity: critical
46	  status: in_progress
47	  first_raised_round: 20
48	  last_seen_round: 23
49	  mentions:
50	    - round: 20
51	      reviewer: R1
52	      note: "θ 选在经验间隔处，K* 在 θ±5pp 就从3变1。"
53	    - round: 21
54	      reviewer: [R1, R2]
55	      note: "多个 configs CI lower 距 θ 不足 1pp。需分层报告 + 多重比较校正。"
56	    - round: 
…[truncated 17263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2262 · 2026-05-22T05:25:40.584721+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-contamination/docs/paper/tables/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-contamination/docs/paper/tables/*"
  }
}
```

</details>

---


### Tool result

_source line 2263 · 2026-05-22T05:25:40.635956+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2264 · 2026-05-22T05:26:06.037948+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "gen-depth-contamination",
  "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "gen-depth-contamination",
    "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
  }
}
```

</details>

---


### Tool result

_source line 2265 · 2026-05-22T05:26:27.246373+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21208
}
```

</details>

---


### Tool call

_source line 2266 · 2026-05-22T05:26:29.355098+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计方法论。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8 页正文上限, ACL 模板 `[review]`, double-blind\n- **附录**: 允许但 reviewer 无义务审阅\n- **Limitations**: 必选章节（不算页数）\n- **Ethics Statement**: 可选（不算页数）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_24/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- K* 的形式化定义是否自洽？DPI 作为动机与 adjacent-pair AUC 之间的逻辑链是否完整？\n- OBD-LightGBM 分类器的设计是否合理？是否存在 data leakage 风险（特别是 self-BLEU 特征和 GroupKFold 分组策略）？\n- θ=0.60 阈值的选择是否充分 justified？是否存在 post-hoc 选择的循环论证风险？\n- 15D 特征集的设计动机是否清晰？是否遗漏关键特征？\n\n### 2. 实验设计\n- 10 个模型配置（6 家族, 1B-8B）的覆盖面是否足够支撑论文声称？\n- 模型规模分布是否偏向小模型？Qwen 家族占比是否过高（5/10）？\n- Cross-scorer validation 的实验设计是否严密？\n- Filtering 实验（Section 5）的效果量和统计功效是否足以支持 K*-aware curation 的声称？\n- Dose-response 实验在低污染比例下效果量极小，论文是否充分讨论？\n\n### 3. 统计方法论\n- Bootstrap CI 和 permutation test 的使用是否正确？\n- 多重比较校正是否充分？\n- ANOVA 表中数值是否完整（多处 `---` 缺失值）？\n- 效应量报告（Cohen's h, η²）是否充分？\n\n### 4. 格式检查\n- 正文是否超 8 页？\n- 匿名性是否满足？\n- 图表质量和可读性\n\n请按以下结构输出审稿意见：\n1. Summary（2-3句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注严重程度：Critical/Major/Minor）\n4. Questions（需要作者澄清的问题）\n5. Missing References\n6. Overall Assessment（评分 1-5，参照 EMNLP 2026 ARR 评分标准）",
  "project": "gen-depth-contamination",
  "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7",
  "director_session_key": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查方法严谨性、实验设计和统计方法论。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8 页正文上限, ACL 模板 `[review]`, double-blind\n- **附录**: 允许但 reviewer 无义务审阅\n- **Limitations**: 必选章节（不算页数）\n- **Ethics Statement**: 可选（不算页数）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_24/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- K* 的形式化定义是否自洽？DPI 作为动机与 adjacent-pair AUC 之间的逻辑链是否完整？\n- OBD-LightGBM 分类器的设计是否合理？是否存在 data leakage 风险（特别是 self-BLEU 特征和 GroupKFold 分组策略）？\n- θ=0.60 阈值的选择是否充分 justified？是否存在 post-hoc 选择的循环论证风险？\n- 15D 特征集的设计动机是否清晰？是否遗漏关键特征？\n\n### 2. 实验设计\n- 10 个模型配置（6 家族, 1B-8B）的覆盖面是否足够支撑论文声称？\n- 模型规模分布是否偏向小模型？Qwen 家族占比是否过高（5/10）？\n- Cross-scorer validation 的实验设计是否严密？\n- Filtering 实验（Section 5）的效果量和统计功效是否足以支持 K*-aware curation 的声称？\n- Dose-response 实验在低污染比例下效果量极小，论文是否充分讨论？\n\n### 3. 统计方法论\n- Bootstrap CI 和 permutation test 的使用是否正确？\n- 多重比较校正是否充分？\n- ANOVA 表中数值是否完整（多处 `---` 缺失值）？\n- 效应量报告（Cohen's h, η²）是否充分？\n\n### 4. 格式检查\n- 正文是否超 8 页？\n- 匿名性是否满足？\n- 图表质量和可读性\n\n请按以下结构输出审稿意见：\n1. Summary（2-3句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注严重程度：Critical/Major/Minor）\n4. Questions（需要作者澄清的问题）\n5. Missing References\n6. Overall Assessment（评分 1-5，参照 EMNLP 2026 ARR 评分标准）",
    "project": "gen-depth-contamination",
    "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7",
    "director_session_key": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
  }
}
```

</details>

---


### Tool result

_source line 2267 · 2026-05-22T05:26:51.130102+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21774
}
```

</details>

---


### Tool call

_source line 2268 · 2026-05-22T05:26:57.718613+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性、写作质量和相关工作。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8 页正文上限, ACL 模板 `[review]`, double-blind\n- **附录**: 允许但 reviewer 无义务审阅\n- **Limitations**: 必选章节（不算页数）\n- **Ethics Statement**: 可选（不算页数）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_24/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性\n- \"Generational depth estimation\" 作为研究问题的新颖性如何？是否确实是该领域的空白？\n- K* 概念相对于已有工作（Geng et al. Markov chain convergence, Wang et al. attractor cycles, Schaeffer & Kazdan model collapse 分析）的增量贡献是否足够？\n- Prompt-chain 设定 vs retrain-chain 设定的选择是否合理？论文对两者关系的讨论是否充分？\n- OBD 方法本身不是新的（Frank & Hall 2001），论文的方法论贡献在哪里？\n\n### 2. 完整性\n- 论文声称覆盖 \"6 architecture families, 1B-8B\"，实际覆盖是否与声称一致？\n- Cross-domain 实验（C4, Wikipedia, arXiv）的样本量和模型覆盖面是否充分？（arXiv 仅 2 个模型, n=2200）\n- Filtering 实验是否足以作为独立贡献？还是更适合作为 consistency check？\n- 是否有关键实验缺失？（如 13B+ 模型、更多 domain、retrain-chain 全面对比）\n\n### 3. 写作质量\n- Abstract 的信息密度是否过高？K* 是否在未定义前就被使用？\n- 论文叙事结构是否清晰？Introduction 的动机铺设是否合理？\n- K* 符号系统（K*_empirical, K*_theory, K*_neural, K*_binary 等）是否过度增殖？\n- Conclusion 的长度和深度是否充分？\n- 正文行文中是否存在不当使用破折号的情况？\n\n### 4. 相关工作\n- Related Work 覆盖面是否全面？是否遗漏重要工作？\n- 与 binary detection（DivEye, Binoculars, DetectGPT）的对比是否公平和充分？\n- 与 data curation 文献（DSIR, D4, DoReMi, Drayson et al.）的关系是否清晰？\n- 是否缺少 Fu et al. (ICLR 2025) \"How to Prevent Model Collapse in Self-consuming Training Loops\" 或其他重要引用？\n\n### 5. 引用质量\n- .bib 文件中是否存在未引用的 orphan entries？\n- 引用格式是否一致（会议名、年份、URL）？\n- 是否有可疑引用（幻觉引用）？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注严重程度：Critical/Major/Minor）\n4. Questions（需要作者澄清的问题）\n5. Missing References\n6. Overall Assessment（评分 1-5，参照 EMNLP 2026 ARR 评分标准）",
  "project": "gen-depth-contamination",
  "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7",
  "director_session_key": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查新颖性、完整性、写作质量和相关工作。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper, 8 页正文上限, ACL 模板 `[review]`, double-blind\n- **附录**: 允许但 reviewer 无义务审阅\n- **Limitations**: 必选章节（不算页数）\n- **Ethics Statement**: 可选（不算页数）\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_24/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性\n- \"Generational depth estimation\" 作为研究问题的新颖性如何？是否确实是该领域的空白？\n- K* 概念相对于已有工作（Geng et al. Markov chain convergence, Wang et al. attractor cycles, Schaeffer & Kazdan model collapse 分析）的增量贡献是否足够？\n- Prompt-chain 设定 vs retrain-chain 设定的选择是否合理？论文对两者关系的讨论是否充分？\n- OBD 方法本身不是新的（Frank & Hall 2001），论文的方法论贡献在哪里？\n\n### 2. 完整性\n- 论文声称覆盖 \"6 architecture families, 1B-8B\"，实际覆盖是否与声称一致？\n- Cross-domain 实验（C4, Wikipedia, arXiv）的样本量和模型覆盖面是否充分？（arXiv 仅 2 个模型, n=2200）\n- Filtering 实验是否足以作为独立贡献？还是更适合作为 consistency check？\n- 是否有关键实验缺失？（如 13B+ 模型、更多 domain、retrain-chain 全面对比）\n\n### 3. 写作质量\n- Abstract 的信息密度是否过高？K* 是否在未定义前就被使用？\n- 论文叙事结构是否清晰？Introduction 的动机铺设是否合理？\n- K* 符号系统（K*_empirical, K*_theory, K*_neural, K*_binary 等）是否过度增殖？\n- Conclusion 的长度和深度是否充分？\n- 正文行文中是否存在不当使用破折号的情况？\n\n### 4. 相关工作\n- Related Work 覆盖面是否全面？是否遗漏重要工作？\n- 与 binary detection（DivEye, Binoculars, DetectGPT）的对比是否公平和充分？\n- 与 data curation 文献（DSIR, D4, DoReMi, Drayson et al.）的关系是否清晰？\n- 是否缺少 Fu et al. (ICLR 2025) \"How to Prevent Model Collapse in Self-consuming Training Loops\" 或其他重要引用？\n\n### 5. 引用质量\n- .bib 文件中是否存在未引用的 orphan entries？\n- 引用格式是否一致（会议名、年份、URL）？\n- 是否有可疑引用（幻觉引用）？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注严重程度：Critical/Major/Minor）\n4. Questions（需要作者澄清的问题）\n5. Missing References\n6. Overall Assessment（评分 1-5，参照 EMNLP 2026 ARR 评分标准）",
    "project": "gen-depth-contamination",
    "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7",
    "director_session_key": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
  }
}
```

</details>

---


### Tool result

_source line 2269 · 2026-05-22T05:26:59.231627+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1513
}
```

</details>

---


### Assistant

_source line 2270 · 2026-05-22T05:27:06.647978+00:00_

已派发：
- 视觉审查 Agent → 已启动（并行运行）
- Reviewer 1 → 方法严谨性 + 实验设计 + 统计方法论
- Reviewer 2 → 新颖性 + 完整性 + 写作质量 + 相关工作

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 168

## Round 168

2 recorded events


### User

_source line 2271 · 2026-05-22T05:34:27.343287+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：Generational Depth Estimation of Recursive Synthetic Text

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 提出了新颖且有价值的 K* 概念和严谨的统计框架，但附录中多个关键数据表为空（ANOVA、域消融、长度消融等），且在现实污染比例下的实际效用不足，未达到 Conference 接收标准。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法论合理，但 ANOVA 表和多个消融表完全为空白占位符（`---`），无法验证关键统计声明；cross-scorer 验证削弱了 continuation 模式的 K*=2 结论 |
| Excitement | 3.5/5 | generational depth 概念新颖且及时，K* 对语料审计有实际意义，但弱化的实际效用限制了影响力 |
| Reproducibility | 2/5 | 5 个附录表全部或大部分为 `---`；未提及代码/数据发布计划；主文引用的多个数值缺乏完整支撑表格 |
| Reviewer Confidence | 4/5 | 仔细阅读全文和全部附录，熟悉污染检测和模型坍塌文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [Critical] ANOVA 表（Table 24 / appendix_extended.tex L27-39）所有统计值为空占位符

- 具体位置：Appendix D, Table 24（Three-way ANOVA: Generator × Scorer × Depth-Pair）
- 问题：表中 F 统计量、p 值、η²_p 全部为 `---`（7 行 × 3 列 = 21 个空值）。但表标题明确声称 "The non-significant Scorer main effect confirms scorer independence of depth discrimination"，这一关键声明没有任何数值支撑。
- 为什么影响接收：scorer independence 是论文 cross-model transfer 声明（Section 4.2、Discussion）的核心支柱。没有 ANOVA 数据，reader 无法验证 scorer 主效应是否真的不显著，也无法评估 Generator × Depth 交互效应的强度。
- 建议修改方向：填充完整的 F、p、η²_p 值；如果实验确实尚未完成，需要如实说明并移除相应声明。

**N2** [Critical] 附录 4 个数据表全部为 `---` 占位符，主文引用了这些表格应包含的结果

- 具体位置：
  - Table S10（Pythia 解码消融，appendix.tex L417-428）：30 个 AUC 值 + K* 行全部 `---`
  - Table S11（长度消融，appendix.tex L436-451）：15 个 AUC 值全部 `---`（仅 K* 行有值）
  - Table S12（域消融，appendix.tex L454-473）：18 个 AUC 值 + K* 行全部 `---`
  - Table S13（Scorer sensitivity，appendix.tex L476-496）：7 个 generator 中 5 个的 cross-scorer K* 为 `---`
- 问题：主文 Section 4.5 引用了具体的域消融数值（"Wikipedia yields K*=2, 1v2 AUC = 0.623, 2v3 = 0.5711"），但对应的完整支撑表 S12 全部为空。Table 4（tab_domain_model_kstar_full）提供了边界 AUC，但不是完整的逐对 AUC。这意味着至少 4 个声称得到消融验证的结论缺乏可审查的详细数据。
- 为什么影响接收：审稿人有义务但无法审阅 reviewer 看不到的数据。空表格暗示实验可能尚未完成，这构成投稿完整性问题。
- 建议修改方向：填充所有 `---` 值或移除引用这些表格的声明。如果某些实验确实 pending，在 Limitations 中明确说明。

**N3** [Major] Dose-response 分析表明 K*-aware 过滤在现实污染比例下无实际效益

- 具体位置：Appendix D.8, Table 25（appendix_extended.tex L97-117）
- 问题：
  - 10% 污染：所有策略无差异（Δ_max = 0.03pp, p > 0.8）
  - 30% 污染：差异方向性但不显著（Δ = 0.10pp, p > 0.3）
  - 50% 污染：binary-ours 优势 0.24pp 但不显著（p = 0.12）
  - 仅在 100% 合成数据（非现实场景）下才有显著效果（0.77pp 改善）
- 但主文 Section 5 仅报告了 100% 设定下的结果，并声称 "K*-aware binary filtering minimizes degradation most effectively"，读者容易高估实际效用。
- 为什么影响接收：论文将 K*-aware curation 作为 downstream application 的核心贡献之一（Contribution (a) in Introduction、Section 5 整节、Abstract 末句）。如果该效用在现实场景下不存在，论文的实用价值声明大幅削弱。
- 建议修改方向：在主文 Section 5 中明确讨论 dose-response 结果，承认在 <50% 污染下效果不显著；调整 Abstract 和 Contribution 的措辞，避免暗示该方法在一般情形下有效。

**N4** [Major] Cross-scorer 验证削弱了 continuation 模式的 K*=2 核心发现

- 具体位置：Section 4.2（主文 p.4）、Table 22（appendix_extended.tex, tab_crossscorer.tex L13-14）
- 问题：Qwen-continuation 使用自身家族模型打分时 K*=2（1v2 AUC = 0.611, CI lower = 0.602, 仅超过 θ=0.60 约 0.002）。但使用 Pythia-1.4B 打分时 1v2 AUC = 0.5923 < θ，使用 OLMo-1B 打分时 1v2 AUC = 0.5858 < θ，K* 均降为 1。
- 这意味着 Qwen-continuation 的 K*=2 是 scorer-dependent 的。考虑到论文声称 "K*_empirical is governed by the generation process rather than the scoring model"（Discussion §Representation dependence），这构成一个直接矛盾。
- 更广泛地看，10 个配置中 6 个得到 K*=2，但其中 3 个是 Qwen 变体（Qwen-rw、Qwen-cont、Qwen-base），而 Qwen-cont 的 K*=2 是 scorer-dependent 的。如果用 cross-scorer 验证后的值，只有 5/10（或更少）配置得到 K*=2。
- 为什么影响接收："K*=2 as the dominant mode" 是论文的 headline finding。如果这个结论对 scorer 选择敏感，论文的主要贡献需要更谨慎的表述。
- 建议修改方向：在主文中更突出地讨论 scorer sensitivity；区分 "robust K*=2"（Qwen-rw, 在 cross-scorer 下保持）和 "marginal K*=2"（Qwen-cont, scorer-dependent）；调整 abstract 和 conclusion 的措辞。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [Warning] Qwen 家族过度代表：4/10 配置来自 Qwen 变体

- 具体位置：Table 1（Section 3.3）及 Table 9（Appendix）
- 问题：Qwen 占 4/10 配置（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），其余 5 个家族各 1 个配置。论文描述为 "6 architecture families"，但 Qwen 的 4× 代表性使得 K*=2 作为 "dominant mode (6/10)" 的说服力下降——如果按家族去重，K*=2 的比例会不同。
- 建议：按家族报告 K* 分布（e.g., 4/6 家族的 representative 配置得到 K*=2），或增加非 Qwen 家族的配置（如 Gemma, Mistral 的 rewrite 模式）。

**W2** [Warning] DPI 到 AUC 的理论桥接不完整

- 具体位置：Section 3.1（method.tex L16-17）
- 问题：DPI 保证互信息 I(X; Y_k) 单调递减，但论文直接将其应用于 AUC_{k-1,k} 的单调递减。AUC 不是互信息的直接度量——它衡量的是分类器的判别力，而非信息论量。虽然实证数据表明 AUC 确实单调递减（Table 2），但缺少理论上的 bridging argument。
- 建议：明确说明 AUC 单调递减是一个经验观察而非 DPI 的直接推论，或提供从 MI 到 AUC 的正式论证。

**W3** [Warning] θ=0.60 阈值的事后选择风险

- 具体位置：Section 3.1 "Threshold justification" 段落
- 问题：论文提供三条 "独立" 证据支持 θ=0.60。但第三条——1v2 AUC 聚集在 0.61-0.70 而 2v3 聚集在 0.55-0.59 之间存在 5-11pp 间断——本身就是从数据中发现的。这意味着阈值是在观察到数据分布后选定的，虽然不完全构成循环论证（filtering 实验未重新优化 θ），但具有 post-hoc 选择的特征。
- 论文在 Limitations 中讨论了 θ 的敏感性（θ=0.55 → K*=3；θ=0.70 → K*=1），这部分做得不错。
- 建议：考虑使用数据驱动的阈值选择方法（如 Youden's J statistic），或更明确地将 θ=0.60 定义为 convention 而非 data-derived。

**W4** [Warning] Filtering 实验仅在单一 generator（Qwen-1.5B continuation）上验证

- 具体位置：Section 5
- 问题：所有 filtering 实验仅使用 Qwen-1.5B continuation 数据训练。论文声称 K*-aware curation 的一般性效用，但未验证对其他 generator 的数据是否同样有效。
- 建议：至少增加一个非 Qwen generator 的 filtering 实验。

---

## 小问题（不影响接收）

- Table 1 仅列出 6 个配置，但论文声称 "10 model configurations"；其余 4 个仅在附录 Table 9 出现，造成困惑。建议在 Table 1 添加脚注说明。
- "one-wash laundering" 术语容易误导：大多数模型实际上是 K*=2（"two-wash"），只有 OLMo/Mistral/Pythia-6.9B/Gemma 是 K*=1（真正的 one-wash）。
- Figure 3 的 x 轴标签在标准打印尺寸下可读性较差。
- Table 4 脚注过于密集（4 个脚注标记），可考虑重构为单独的注释段落。
- K*_empirical 定义（Eq.1）使用 max{k ≥ 1 : AUC > θ}，隐含假设 AUC 单调递减。如果出现非单调情况（如 AUC_{1,2} < θ 但 AUC_{2,3} > θ），该定义会给出 K*=max{1,3}=3，可能不合理。建议改为 "最大的 k 使得所有 j ≤ k 均满足 AUC_{j-1,j} > θ"，或明确说明单调递减是前提假设。

---

## 主要优势

1. **新颖的问题形式化**：generational depth estimation 和 K* 概念是对现有二分类（人/机）检测文献的有意义扩展，填补了 "递归合成文本到底能追溯几代" 这一重要空白。
2. **严谨的统计框架**：bootstrap CI、permutation test、GroupKFold（按 doc_id 分组防泄漏）、cross-model transfer 验证，统计方法论总体规范。
3. **系统性消融设计**：变模型、规模、域、解码策略、scorer、文本长度，覆盖面广（尽管部分消融数据缺失）。
4. **Cross-model transfer 强**：80-100% 迁移准确率和 scorer-invariant feature ranking（ρ > 0.90）是有实际部署价值的贡献。
5. **写作清晰、结构合理**：符号统一，逻辑链条完整，Discussion 对 boundary cases 的讨论诚实。

---

## Questions（需作者回应）

Q1. Tables S10、S11、S12 和 ANOVA Table 24 中的所有 `---` 值是 placeholder 还是实验尚未完成？如果是后者，这构成投稿完整性问题——ARR 审稿人需要评估完整的证据链。

Q2. 鉴于 dose-response 分析显示在 50% 以下污染率时 K*-aware filtering 无显著收益，论文设想的实际部署场景是什么？在什么条件下 web-scale corpora 的合成数据比例会达到 50% 以上？

Q3. Qwen-continuation 的 K*=2 在 cross-scorer 下降为 1。论文能否提供更多 generator-scorer 组合的 cross-scoring 结果（Table S13 中 5 个 generator 的 cross-scorer 值为 `---`），以更全面地评估 K*=2 的 robustness？

Q4. 随着模型规模增大（1.5B → 8B），0v1 信号减弱。论文推测 13B+ 模型可能 K*=1。如果 K*=1 在大模型上普遍成立，K* 的实际意义将局限于小模型生成的内容，这是否限制了论文的长期影响力？

Q5. K*_empirical 定义中的 max 算子是否隐含了 AUC 单调递减的假设？如果某些配置出现非单调 AUC（如 noise 导致），定义会给出不合理的 K* 值。作者是否考虑过 alternative definition（如 "连续满足条件的最大 k"）？

---

## Missing References

- Kirchenbauer et al. (2023), "A Watermark for Large Language Models" — watermarking 是替代检测方案，在 related work 中值得讨论
- Mitchell et al. (2023) DetectGPT 已引用 ✓
- 整体引用覆盖面良好，未发现严重遗漏

---

**总结**：这是一篇提出了有意义新概念的论文，K* generational depth boundary 是 contamination detection 领域的实质贡献。但当前版本存在两个核心问题：(1) 附录中大量支撑数据缺失（空表格），使得关键声明无法验证；(2) K*-aware curation 的实际效用在现实污染比例下尚未得到证实。修复空表格并诚实呈现 practical utility 的边界后，论文有望达到 3.5（Borderline Conference）或以上。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2272 · 2026-05-22T05:34:40.230743+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 2273 · 2026-05-22T05:35:03.205888+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心判断：

- **Overall 3.0 (Findings)**，K* 概念新颖但有两个硬伤
- **N1-N2 (Critical)**：ANOVA 表和 4 个附录消融表全部为 `---` 占位符，关键统计声明（scorer independence）无数值支撑
- **N3 (Major)**：dose-response 显示在 <50% 污染率下 K*-aware filtering 无显著效果，主文仅报告了 100% 非现实设定
- **N4 (Major)**：Qwen-cont 的 K*=2 在 cross-scorer 下降为 1，削弱 headline finding 的 robustness
- 主要优势在于 K* 问题形式化的新颖性、统计框架的严谨性、和 cross-model transfer 的实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2274 · 2026-05-22T05:35:12.236083+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 170

## Round 170

6 recorded events


### User

_source line 2275 · 2026-05-22T05:36:52.999269+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Generational Depth Estimation of Recursive Synthetic Text

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 研究问题新颖且有实际意义，实证方法论扎实，但 K*_empirical 作为特征集相关的下界被过度包装为"the discrimination boundary"，加上 Table 21 数据缺失、跨域证据薄弱、以及在现实污染比例下实用价值存疑，使其处于主会议接收的边界。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心 claim (K*=2 for web text) 有充分统计支撑（bootstrap CI, permutation test, Cohen's h），但 K*_empirical 本质上是特征集相关的下界，论文主体对此定位不够诚实；arXiv K*=3 仅有 2 个模型支撑 |
| Excitement | 3/5 | 研究问题本身（generational depth estimation）确实是该领域空白，"one-wash laundering" 有实践洞察价值，但方法论贡献有限（OBD 来自 Frank & Hall 2001，分类器为标准 LightGBM），且 scale trend 暗示结论可能仅适用于 ≤8B 模型 |
| Reproducibility | 4/5 | 15D 特征定义完整（Table 14），LightGBM 超参数明确（Table 15），数据集统计清晰（Table 13），代码未提供但细节足以复现 |
| Reviewer Confidence | 4/5 | 仔细阅读了全部 20 页，逐表逐图核实，搜索了相关工作覆盖面 |

---

## Summary

本文提出 "generational depth estimation"，测量递归合成文本的可区分深度边界 K*_empirical。使用 15 个统计特征 + OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族，1B-8B）、3 个文本域、4 种解码策略上实验，发现 K*_empirical ∈ {1,2,3}，一般 web 文本以 K*=2 为主导模式（6/10 配置），arXiv 学术文本 K*=3。论文进一步验证了跨模型迁移能力（80-100% 精度保持）和 K*-aware 数据过滤的下游效用。

---

## 主要优势（Strengths）

**S1. 研究问题新颖且定义清晰。** 现有工作在 binary detection（human vs. machine）和 model collapse macro dynamics 之间留下了明确空白：没有方法估计一段文本经历了多少代递归生成。本文精确地填补了这个空白，问题定义（K*_empirical = max k where pairwise AUC_{k-1,k} > θ）简洁可操作。

**S2. 统计方法论严谨度高于同类工作。** Bootstrap 95% CI（1,000 resamples）、permutation test（N=400, p≤0.002）、Cohen's h 效应量（h≈0.20）、5-fold GroupKFold 交叉验证（按 seed document 分组防泄漏）——这套统计体系在 NLP 实证论文中不常见，显著增强了结论可信度。

**S3. "One-wash laundering" 洞察有实践价值。** K*=2 意味着一次生成就足以让 web 文本与更深层合成内容不可区分（Section 6, "one-wash laundering"），这对数据策展实践有直接指导意义：对 web text 而言，超越 binary 过滤的更精细深度感知策略是不必要的。

**S4. 跨模型迁移分析设计精巧。** Cross-scorer validation（Table 22）和 scorer-invariant feature ranking（Spearman ρ > 0.90, Table 6）共同证明 K* 由生成过程而非评估模型决定，这是一个重要的方法论贡献。

**S5. 模型覆盖面合理。** 6 个架构族（Qwen2.5, Pythia, OLMo, LLaMA-3.1, Mistral, Gemma-2）、rewrite + continuation 两种生成模式、4 种解码策略——在 ≤8B 的范围内覆盖面较全。

**S6. Limitations 部分诚实且详尽。** 7 条主要局限 + extended appendix（D.7 retrain-chain, D.8 dose-response），主动暴露了 threshold sensitivity、feature-set dependence、marginal boundary cases 等问题。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Table 21（p.18）数据完全缺失**
- 具体位置：Appendix Table 21, page 18
- 问题：该表标题为 "Pairwise AUC across depth pairs for three text domains (Qwen2.5-1.5B-Instruct, continuation mode)"，声称提供 C4/Wikipedia/arXiv 三域的 pairwise AUC 数据，但所有 21 个数据单元格均为 em-dash（—），没有任何数值。
- 为什么影响接收：该表是 Section 4.5 跨域分析和 Discussion "Domain dependence of K*" 的详细数据支撑。Table 4（正文 p.5）只报告了模型级别的 1v2 AUC 和 K* 值，缺少逐深度对的 AUC 曲线。一个标题声称有数据但实际为空的表格是严重的投稿质量问题。
- 建议修改方向：填入实际 AUC 数据，或若数据确实存在但因排版问题缺失，修复 LaTeX 表格引用。

**N2** [critical] **K*_empirical 的定位：下界 vs. "the boundary"**
- 具体位置：Title, Abstract, Section 1, Section 3.1
- 问题：标题用 "Measuring the Discrimination Boundary"，Abstract 说 "We measure the discrimination boundary K*_empirical"，Introduction 说 "We empirically measure K*_empirical (the maximum depth at which a classifier reliably distinguishes adjacent generations)"。但 Limitation 5 承认 K*_empirical 是 "feature-set-specific lower bound (K*_theory may be strictly higher)"，且 Table 3 的 neural probe 实验显示 K*_neural 在 1-3 之间随模型变化。这意味着 K*_empirical=2 不是文本的内在属性，而是 15D 特征集 + LightGBM 分类器的分辨率上限。
- 为什么影响接收：正文的 framing 与 Limitations 中的 qualification 之间存在系统性不一致。读者如果只看 Abstract/Intro/Conclusion（多数读者如此），会获得比实际证据支持的更强的结论。这是 overclaiming。
- 建议修改方向：在 Abstract 和 Introduction 中明确引入 "lower bound" 限定语（如 "We measure a lower bound on the discrimination boundary"）；在 Section 3 定义 K*_empirical 时立即说明其与 K*_theory 的关系，而非推迟到 Limitations。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **arXiv K*=3 的证据基础薄弱**
- 具体位置：Section 4.5, Abstract contribution (b), Table 4
- 问题：arXiv 实验仅涉及 2 个模型（Qwen-1.5B, Pythia-1.4B），每模型 n=2,200 样本。相比之下，C4 主实验有 10 个模型配置、每配置 5,000 样本。Wikipedia 同样仅 2 个模型 + n=2,200。但 Abstract 和 contribution list 将 "domain dependence" 作为与 C4 结果平行的核心贡献呈现。
- 建议：降低 arXiv/Wikipedia 结论的确信度（如 "preliminary evidence suggests" 而非 "yields K*=3"），或增加更多模型覆盖。

**W2** [major] **缺少 >8B 模型，且论文自身承认 scale trend 可能使主要结论失效**
- 具体位置：Discussion Section 6, "Boundary cases and scale effect"
- 问题：论文报告 0v1 JSD 随模型规模降低（0.15-0.27 at ≤1.5B vs. 0.077 at 8B LLaMA-3.1），并推测 "models at 13B+ may increasingly yield K*=1"。若属实，K*=2 的主要发现仅适用于中小模型，而实际生成大量 web 合成内容的前沿模型（GPT-4, Claude 等）可能都是 K*=1。这显著缩小了论文发现的实践相关性。
- 建议：至少测试 1-2 个 13B+ 模型（如 LLaMA-3.1-70B 通过量化），或在 Abstract/Conclusion 中明确标注 scale 适用范围。

**W3** [major] **Filtering 实验在现实污染比例下实用价值消失**
- 具体位置：Section 5, Appendix D.8
- 问题：主实验使用 100% 合成数据设定（上界），Appendix D.8 的 dose-response 分析显示在 10-30% 污染比例下，所有过滤策略趋于不可区分（p > 0.3 at 10%）。Section 5 承认 "when synthetic data proportion is low enough to leave overall training quality intact, filtering strategies converge"，但仍将 filtering 作为 "downstream validation" 贡献呈现。
- 建议：将 filtering 定位为 consistency check 而非独立贡献；在正文中提及 dose-response convergence（而非仅在附录），让读者了解实际适用条件。

**W4** [major] **缺少重要相关工作**
- 具体位置：Section 2 Related Work
- 问题：
  (a) **Wang, Li, Yan, Cheng, Zhang (ACL 2025)** "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing"——该工作从动力系统视角研究 successive prompt-chain generation 中的 attractor cycles，与 K* 概念直接相关（K* 可理解为文本收敛到 attractor 前的可区分代数）。
  (b) **Fu, Wang, Chen, Tian, Tao (ICLR 2025)** "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"——提供了自消费训练循环中 collapse 的理论条件，为 K* 何时存在及其值提供了互补的理论视角。
- 建议：在 Related Work 的 "Model collapse and recursive degradation" 段落中加入这两篇引用，并讨论 K* 与 attractor convergence 的关系。

**W5** [minor] **K* 符号变体过多**
- 具体位置：全文
- 问题：K*_empirical、K*_theory、K*_neural 三个变体中，K*_theory 在 Section 3.1 引入后从未得到实证处理，仅作为上界占位符存在。增加了读者认知负担但信息增量有限。
- 建议：考虑在首次引入时一次性定义清楚三者关系，或简化为 K*（实证）和 K*_theory（理论上界）两个，将 K*_neural 作为 Section 4.4 的局部记号。

**W6** [minor] **Conclusion 过于简短**
- 具体位置：Section 7, page 7
- 问题：仅 3 句正文 + 1 句 future work。对于一篇同时涉及 depth estimation、cross-model transfer、domain dependence、downstream filtering 四个 claim 的论文，Conclusion 没有合成这些发现的 broader implications，也没有讨论对实践者的 actionable takeaway。
- 建议：扩展至 5-7 句，加入实践建议（如 "for web-scale corpus curation, binary filtering is sufficient"）和主要局限的 high-level 总结。

**W7** [minor] **Abstract 信息密度过高**
- 具体位置：Abstract
- 问题：约 200 词内包含 K*_empirical、θ=0.60、Cohen's h≈0.20、6/10 configurations、ρ>0.90、MMLU 0.5941 vs. 0.6018 等大量定量细节。对于不熟悉该问题的读者，认知负担过高。K* 在 Abstract 中使用时尚未正式定义。
- 建议：Abstract 保留核心发现（K*∈{1,2,3}，web text K*=2, "one-wash laundering"），将统计细节（CI、Cohen's h、具体 AUC 值）移至 Introduction 或 Experiments。

**W8** [minor] **Related Work 语法问题**
- 具体位置：Section 2, related_work.tex line 12
- 问题："None estimates recursive generation depth" 语法不正确。"None" 作代词需要先行词，此处上下文中 "None" 指代不明确。
- 建议：改为 "No existing method estimates recursive generation depth" 或 "None of these methods estimates..."

**W9** [minor] **引用格式不一致**
- 具体位置：references.bib
- 问题：39 条引用中有 8 条缺少 URL（包括知名论文 DetectGPT/mitchell2023detectgpt），而其余大多数条目都包含 URL。部分条目缺少页码（对会议论文属正常），但 URL 的有无不一致。
- 建议：统一补全 URL，或统一去掉（后者不推荐）。

---

## 小问题（不影响接收）

- Table 22（p.18）中 5 个模型的 cross-scorer 列为 dash（未测试）——可以理解资源限制，但缩小了 cross-scorer 结论的泛化性。
- Figure 5（p.10）bar chart 的 x 轴标签在 150 DPI 下难以辨认，建议增大字体或旋转标签。
- Conclusion 中 "6 families, 1B--8B" 与 Introduction 重复，可替换为更有价值的内容。

---

## Questions for Authors

1. **Table 21 数据**：该表是排版错误还是数据尚未填入？如果数据存在，请提供完整的跨域 pairwise AUC。

2. **Scale trend**：鉴于 0v1 JSD 随模型规模递减的趋势，是否预期 13B+ 模型的 K*_empirical=1？若是，K*=2 的核心发现是否仅限于一个将被淘汰的模型规模窗口？

3. **Feature-set 选择**：Neural probe 显示 K*_neural 可达 3（Qwen embeddings），而 15D features 给出 K*=2。实践中应如何选择？论文推荐 15D 的理由是 "cross-model consistency"，但这实际上是在 sensitivity 和 generalizability 之间做了取舍，是否应让用户根据场景选择？

4. **Dose-response 收敛**：现实 web crawl 的合成内容比例大约在什么范围？如果在 10-30%（此时过滤策略收敛），K*-aware curation 的实际增益是什么？

5. **Prompt-chain vs. retrain-chain**：K*_empirical(prompt)=2 vs. K*_empirical(retrain)≥4（Appendix D.7）。论文认为 prompt-chain K* 是 "operationally relevant boundary for data curation"。但 retrain-chain 是 model collapse 文献的主要研究对象。如何调和这两个不同的 K* 值？它们是否测量了本质不同的现象？

---

## Missing References

1. **Wang, Li, Yan, Cheng, Zhang (ACL 2025)**: "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" — 从动力系统视角研究 prompt-chain 中的 attractor cycles，与 K* 收敛机制直接相关。
2. **Fu, Wang, Chen, Tian, Tao (ICLR 2025)**: "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops" — 提供自消费循环中 collapse 的理论条件，是 K* 存在的理论背景。

---

## Overall Assessment

**Overall: 3.5 (Borderline Conference)**

本文填补了 binary detection 和 model collapse macro dynamics 之间的真实空白——generational depth estimation。研究问题定义清晰、实验统计方法论严谨、"one-wash laundering" 发现有实践价值。

但以下问题使其处于主会议接收边界：(1) Table 21 数据缺失是严重的投稿质量问题；(2) K*_empirical 的 framing 在正文中系统性地偏强（"the boundary" vs. "a feature-specific lower bound"），Limitations 中的 qualification 不足以弥补前文的 overclaiming；(3) arXiv/Wikipedia 跨域证据过薄（2 models, n=2200）却被作为平行贡献呈现；(4) ≤8B 模型限制加上论文自身承认的 scale trend 削弱了实践相关性；(5) 缺少 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025) 两篇重要相关工作。

修复 Table 21、在正文中一致性地引入 lower-bound framing、补充缺失引用并讨论与 attractor convergence 的关系，可显著提升论文质量至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2276 · 2026-05-22T05:37:36.564982+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 N/W/小问题/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Overall 3.5 (Borderline Conference)\n\n**官方维度打分**：Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5\n\n### Must-Fix\n\n**N1** [critical] Table 21（p.18）数据完全缺失——Appendix Table 21 \"Pairwise AUC across depth pairs for three text domains\" 所有 21 个数据单元格均为 em-dash（—），没有任何数值。该表是 Section 4.5 跨域分析的详细数据支撑。\n\n**N2** [critical] K*_empirical 的定位：下界 vs. \"the boundary\"——标题用 \"Measuring the Discrimination Boundary\"，Abstract 说 \"We measure the discrimination boundary K*_empirical\"，但 Limitation 5 承认 K*_empirical 是 \"feature-set-specific lower bound (K*_theory may be strictly higher)\"，且 neural probe 显示 K*_neural 在 1-3 之间随模型变化。正文 framing 与 Limitations 中的 qualification 存在系统性不一致，构成 overclaiming。\n\n### Should-Fix\n\n**W1** [major] arXiv K*=3 的证据基础薄弱——仅 2 个模型（Qwen-1.5B, Pythia-1.4B），每模型 n=2,200，但 Abstract 和 contribution list 将 \"domain dependence\" 作为与 C4 结果平行的核心贡献呈现。\n\n**W2** [major] 缺少 >8B 模型，且论文自身承认 scale trend 可能使主要结论失效——0v1 JSD 随模型规模降低（0.15-0.27 at ≤1.5B vs. 0.077 at 8B），推测 \"models at 13B+ may increasingly yield K*=1\"。\n\n**W3** [major] Filtering 实验在现实污染比例下实用价值消失——dose-response 分析显示在 10-30% 污染比例下所有策略趋于不可区分（p > 0.3 at 10%），但主文仍将 filtering 作为 \"downstream validation\" 贡献呈现。\n\n**W4** [major] 缺少重要相关工作——(a) Wang, Li, Yan, Cheng, Zhang (ACL 2025) \"Unveiling Attractor Cycles in LLMs\"；(b) Fu, Wang, Chen, Tian, Tao (ICLR 2025) \"How to Prevent Model Collapse in Self-consuming Training Loops\"。\n\n**W5** [minor] K* 符号变体过多——K*_empirical、K*_theory、K*_neural 增加读者认知负担。\n\n**W6** [minor] Conclusion 过于简短——仅 3 句正文 + 1 句 future work。\n\n**W7** [minor] Abstract 信息密度过高。\n\n**W8** [minor] \"None estimates recursive generation depth\" 语法不正确。\n\n**W9** [minor] 引用格式不一致（39 条中 8 条缺 URL）。\n\n### Questions\n\nQ1. Table 21 是排版错误还是数据未填入？\nQ2. Scale trend：13B+ 模型的 K*_empirical=1 是否使 K*=2 核心发现仅限于即将被淘汰的模型规模窗口？\nQ3. Neural probe K*_neural=3 vs 15D K*=2：实践中应如何选择？\nQ4. 现实 web crawl 合成内容比例在什么范围？10-30% 下 K*-aware curation 增益是什么？\nQ5. Prompt-chain K*=2 vs retrain-chain K*≥4：是否测量了本质不同的现象？\n\n### Missing References\n- Wang et al. (ACL 2025) \"Unveiling Attractor Cycles in LLMs\"\n- Fu et al. (ICLR 2025) \"How to Prevent Model Collapse in Self-consuming Training Loops\"\n\n---\n\n请逐条回应上述所有 N/W 项。",
  "project": "gen-depth-contamination",
  "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7",
  "director_session_key": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 N/W/小问题/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见 — Overall 3.5 (Borderline Conference)\n\n**官方维度打分**：Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5\n\n### Must-Fix\n\n**N1** [critical] Table 21（p.18）数据完全缺失——Appendix Table 21 \"Pairwise AUC across depth pairs for three text domains\" 所有 21 个数据单元格均为 em-dash（—），没有任何数值。该表是 Section 4.5 跨域分析的详细数据支撑。\n\n**N2** [critical] K*_empirical 的定位：下界 vs. \"the boundary\"——标题用 \"Measuring the Discrimination Boundary\"，Abstract 说 \"We measure the discrimination boundary K*_empirical\"，但 Limitation 5 承认 K*_empirical 是 \"feature-set-specific lower bound (K*_theory may be strictly higher)\"，且 neural probe 显示 K*_neural 在 1-3 之间随模型变化。正文 framing 与 Limitations 中的 qualification 存在系统性不一致，构成 overclaiming。\n\n### Should-Fix\n\n**W1** [major] arXiv K*=3 的证据基础薄弱——仅 2 个模型（Qwen-1.5B, Pythia-1.4B），每模型 n=2,200，但 Abstract 和 contribution list 将 \"domain dependence\" 作为与 C4 结果平行的核心贡献呈现。\n\n**W2** [major] 缺少 >8B 模型，且论文自身承认 scale trend 可能使主要结论失效——0v1 JSD 随模型规模降低（0.15-0.27 at ≤1.5B vs. 0.077 at 8B），推测 \"models at 13B+ may increasingly yield K*=1\"。\n\n**W3** [major] Filtering 实验在现实污染比例下实用价值消失——dose-response 分析显示在 10-30% 污染比例下所有策略趋于不可区分（p > 0.3 at 10%），但主文仍将 filtering 作为 \"downstream validation\" 贡献呈现。\n\n**W4** [major] 缺少重要相关工作——(a) Wang, Li, Yan, Cheng, Zhang (ACL 2025) \"Unveiling Attractor Cycles in LLMs\"；(b) Fu, Wang, Chen, Tian, Tao (ICLR 2025) \"How to Prevent Model Collapse in Self-consuming Training Loops\"。\n\n**W5** [minor] K* 符号变体过多——K*_empirical、K*_theory、K*_neural 增加读者认知负担。\n\n**W6** [minor] Conclusion 过于简短——仅 3 句正文 + 1 句 future work。\n\n**W7** [minor] Abstract 信息密度过高。\n\n**W8** [minor] \"None estimates recursive generation depth\" 语法不正确。\n\n**W9** [minor] 引用格式不一致（39 条中 8 条缺 URL）。\n\n### Questions\n\nQ1. Table 21 是排版错误还是数据未填入？\nQ2. Scale trend：13B+ 模型的 K*_empirical=1 是否使 K*=2 核心发现仅限于即将被淘汰的模型规模窗口？\nQ3. Neural probe K*_neural=3 vs 15D K*=2：实践中应如何选择？\nQ4. 现实 web crawl 合成内容比例在什么范围？10-30% 下 K*-aware curation 增益是什么？\nQ5. Prompt-chain K*=2 vs retrain-chain K*≥4：是否测量了本质不同的现象？\n\n### Missing References\n- Wang et al. (ACL 2025) \"Unveiling Attractor Cycles in LLMs\"\n- Fu et al. (ICLR 2025) \"How to Prevent Model Collapse in Self-consuming Training Loops\"\n\n---\n\n请逐条回应上述所有 N/W 项。",
    "project": "gen-depth-contamination",
    "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7",
    "director_session_key": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
  }
}
```

</details>

---


### Tool result

_source line 2277 · 2026-05-22T05:38:10.011274+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33446
}
```

</details>

---


### Tool call

_source line 2278 · 2026-05-22T05:38:10.664264+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 N/W/小问题/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Overall 3.0 (Findings)\n\n**官方维度打分**：Soundness 3/5, Excitement 3.5/5, Reproducibility 2/5, Confidence 4/5\n\n### Must-Fix\n\n**N1** [Critical] ANOVA 表（Table 24 / appendix_extended.tex L27-39）所有统计值为空占位符——F 统计量、p 值、η²_p 全部为 `---`（7 行 × 3 列 = 21 个空值）。但表标题声称 \"The non-significant Scorer main effect confirms scorer independence of depth discrimination\"。scorer independence 是 cross-model transfer 声明的核心支柱，没有 ANOVA 数据无法验证。\n\n**N2** [Critical] 附录 4 个数据表全部为 `---` 占位符——Table S10（Pythia 解码消融, 30 个 AUC 值全部 `---`）、Table S11（长度消融, 15 个 AUC 值全部 `---`，仅 K* 行有值）、Table S12（域消融, 18 个 AUC 值 + K* 行全部 `---`）、Table S13（Scorer sensitivity, 5 个 generator 的 cross-scorer K* 为 `---`）。主文 Section 4.5 引用了具体域消融数值，但完整支撑表 S12 全部为空。\n\n**N3** [Major] Dose-response 分析表明 K*-aware 过滤在现实污染比例下无实际效益——10% 污染所有策略无差异（Δ_max = 0.03pp, p > 0.8）；30% 不显著（Δ = 0.10pp, p > 0.3）；50% 不显著（0.24pp, p = 0.12）。仅 100% 合成数据下才有显著效果。但主文 Section 5 仅报告 100% 设定。\n\n**N4** [Major] Cross-scorer 验证削弱了 continuation 模式的 K*=2——Qwen-cont 自身打分 K*=2（1v2 AUC = 0.611, CI lower = 0.602, 仅超过 θ=0.60 约 0.002），但 Pythia 打分 AUC = 0.5923 < θ，OLMo 打分 AUC = 0.5858 < θ。K*=2 是 scorer-dependent。与 \"K*_empirical is governed by the generation process rather than the scoring model\" 矛盾。\n\n### Should-Fix\n\n**W1** [Warning] Qwen 家族过度代表：4/10 配置来自 Qwen 变体（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），其余 5 个家族各 1 个配置。按家族去重后 K*=2 比例可能不同。\n\n**W2** [Warning] DPI 到 AUC 的理论桥接不完整——DPI 保证互信息单调递减，但论文直接应用于 AUC_{k-1,k} 的单调递减。AUC 不是互信息的直接度量。\n\n**W3** [Warning] θ=0.60 阈值的事后选择风险——三条\"独立\"证据中第三条（数据分布间断）本身是数据驱动的，具有 post-hoc 选择特征。\n\n**W4** [Warning] Filtering 实验仅在单一 generator（Qwen-1.5B continuation）上验证。\n\n### 小问题\n\n- Table 1 仅列 6 个配置但声称 \"10 model configurations\"\n- \"one-wash laundering\" 术语容易误导（多数模型实际 K*=2 = \"two-wash\"）\n- Figure 3 x 轴标签可读性差\n- Table 4 脚注过密\n- K*_empirical 定义隐含 AUC 单调递减假设\n\n### Questions\n\nQ1. Tables S10/S11/S12 和 ANOVA Table 24 中的 `---` 是 placeholder 还是实验未完成？\nQ2. K*-aware filtering 的实际部署场景？web-scale 何时合成比例 >50%？\nQ3. 能否提供更多 generator-scorer 组合的 cross-scoring 结果？\nQ4. 13B+ 模型若 K*=1，是否限制论文长期影响力？\nQ5. K*_empirical 定义中 max 算子是否隐含 AUC 单调递减假设？\n\n### Missing References\n- Kirchenbauer et al. (2023) \"A Watermark for Large Language Models\"\n\n---\n\n请逐条回应上述所有 N/W 项。",
  "project": "gen-depth-contamination",
  "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7",
  "director_session_key": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 N/W/小问题/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见 — Overall 3.0 (Findings)\n\n**官方维度打分**：Soundness 3/5, Excitement 3.5/5, Reproducibility 2/5, Confidence 4/5\n\n### Must-Fix\n\n**N1** [Critical] ANOVA 表（Table 24 / appendix_extended.tex L27-39）所有统计值为空占位符——F 统计量、p 值、η²_p 全部为 `---`（7 行 × 3 列 = 21 个空值）。但表标题声称 \"The non-significant Scorer main effect confirms scorer independence of depth discrimination\"。scorer independence 是 cross-model transfer 声明的核心支柱，没有 ANOVA 数据无法验证。\n\n**N2** [Critical] 附录 4 个数据表全部为 `---` 占位符——Table S10（Pythia 解码消融, 30 个 AUC 值全部 `---`）、Table S11（长度消融, 15 个 AUC 值全部 `---`，仅 K* 行有值）、Table S12（域消融, 18 个 AUC 值 + K* 行全部 `---`）、Table S13（Scorer sensitivity, 5 个 generator 的 cross-scorer K* 为 `---`）。主文 Section 4.5 引用了具体域消融数值，但完整支撑表 S12 全部为空。\n\n**N3** [Major] Dose-response 分析表明 K*-aware 过滤在现实污染比例下无实际效益——10% 污染所有策略无差异（Δ_max = 0.03pp, p > 0.8）；30% 不显著（Δ = 0.10pp, p > 0.3）；50% 不显著（0.24pp, p = 0.12）。仅 100% 合成数据下才有显著效果。但主文 Section 5 仅报告 100% 设定。\n\n**N4** [Major] Cross-scorer 验证削弱了 continuation 模式的 K*=2——Qwen-cont 自身打分 K*=2（1v2 AUC = 0.611, CI lower = 0.602, 仅超过 θ=0.60 约 0.002），但 Pythia 打分 AUC = 0.5923 < θ，OLMo 打分 AUC = 0.5858 < θ。K*=2 是 scorer-dependent。与 \"K*_empirical is governed by the generation process rather than the scoring model\" 矛盾。\n\n### Should-Fix\n\n**W1** [Warning] Qwen 家族过度代表：4/10 配置来自 Qwen 变体（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），其余 5 个家族各 1 个配置。按家族去重后 K*=2 比例可能不同。\n\n**W2** [Warning] DPI 到 AUC 的理论桥接不完整——DPI 保证互信息单调递减，但论文直接应用于 AUC_{k-1,k} 的单调递减。AUC 不是互信息的直接度量。\n\n**W3** [Warning] θ=0.60 阈值的事后选择风险——三条\"独立\"证据中第三条（数据分布间断）本身是数据驱动的，具有 post-hoc 选择特征。\n\n**W4** [Warning] Filtering 实验仅在单一 generator（Qwen-1.5B continuation）上验证。\n\n### 小问题\n\n- Table 1 仅列 6 个配置但声称 \"10 model configurations\"\n- \"one-wash laundering\" 术语容易误导（多数模型实际 K*=2 = \"two-wash\"）\n- Figure 3 x 轴标签可读性差\n- Table 4 脚注过密\n- K*_empirical 定义隐含 AUC 单调递减假设\n\n### Questions\n\nQ1. Tables S10/S11/S12 和 ANOVA Table 24 中的 `---` 是 placeholder 还是实验未完成？\nQ2. K*-aware filtering 的实际部署场景？web-scale 何时合成比例 >50%？\nQ3. 能否提供更多 generator-scorer 组合的 cross-scoring 结果？\nQ4. 13B+ 模型若 K*=1，是否限制论文长期影响力？\nQ5. K*_empirical 定义中 max 算子是否隐含 AUC 单调递减假设？\n\n### Missing References\n- Kirchenbauer et al. (2023) \"A Watermark for Large Language Models\"\n\n---\n\n请逐条回应上述所有 N/W 项。",
    "project": "gen-depth-contamination",
    "chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7",
    "director_session_key": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
  }
}
```

</details>

---


### Tool result

_source line 2279 · 2026-05-22T05:38:12.177293+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1513
}
```

</details>

---


### Assistant

_source line 2280 · 2026-05-22T05:38:17.441032+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 171

## Round 171

2 recorded events


### User

_source line 2281 · 2026-05-22T05:38:20.272877+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**3.5 / 5（Borderline Conference）**。研究问题新颖（generational depth estimation 确为领域空白），统计方法论扎实，"one-wash laundering" 有实践价值。但存在两个 critical 问题：Table 21 数据完全缺失（跨域 AUC 表格全为 em-dash），以及 K\*\_empirical 在正文中被系统性地 overclaim 为 "the boundary" 而非 feature-specific lower bound。另有 4 个 major 问题：arXiv 跨域证据过薄（仅 2 模型）、缺少 >8B 模型、filtering 在现实污染比例下价值消失、缺少 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025) 两篇重要引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2282 · 2026-05-22T05:38:24.858684+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 172

## Round 172

2 recorded events


### User

_source line 2283 · 2026-05-22T05:39:50.723756+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 意见的交叉回应

### Must-Fix

**[AGREE] R2-N1: Table 21 数据全部缺失**
同意。LaTeX 源码（appendix.tex L454-473, Table S12）确认所有 AUC 值为 `---` 占位符。我的独立审查还发现了 R2 未提及的其他空表：ANOVA Table 24（F/p/η² 全空）、Table S10（Pythia 解码消融 30 个空值）、Table S11（长度消融 15 个空值）。数据缺失范围比 R2 指出的更广。

**[REBUT] R2-N2: K*_empirical "lower bound" vs "boundary" 构成 overclaiming**
部分不同意。Section 3.1 Eq.1 之前明确写道 "We define the operational lower bound"，K*_empirical 的性质在方法论层面已清晰界定。"Discrimination boundary" 指经验可判别性边界，K*_empirical 本身即是这一边界，同时也是理论 K*_theory 的 lower bound。两层含义不矛盾。但同意 Abstract 措辞可更精确（"a lower bound on the discrimination boundary"）。这是措辞精度问题，未达 Critical 级 overclaiming。

### Should-Fix

**[REBUT] R2-W1: arXiv K*=3 仅 2 个模型**
事实性描述不准确。Table 4（tab_domain_model_kstar.tex）显示 arXiv K*=3 覆盖 5 个模型 / 4 个独立家族（Qwen-1.5B、Qwen-7B、Pythia-1.4B、LLaMA-8B、Mistral-7B），仅 OLMo-1B 因 capacity failure 得到 K*=1。Table 4 full 提供了每个模型的 boundary AUC（0.6215-0.6545），均显著超过 θ。Abstract 说 "two architectures" 指详细验证，但汇总结果覆盖 5/6 模型。同意 n=2,200 的样本量关注。

**[AGREE] R2-W2: 缺少 >8B 模型** — 同意。Discussion 已承认 scale trend 可能使 K*→1。

**[AGREE] R2-W3: Filtering 低污染下无效** — 完全同意，与我的 N3 一致。

**[AGREE] R2-W4: 缺少两篇相关工作** — 同意，两篇均直接相关。

**[AGREE] R2-W5/W6** — 轻度同意，符号简化和 Conclusion 扩展建议合理。

**[REBUT] R2-W7: Abstract 信息密度过高** — 不同意。NLP 顶会 abstract 需在有限篇幅传达核心贡献，该 abstract 结构清晰、无冗余。

**[REBUT] R2-W8: "None estimates" 语法错误** — LaTeX 源码（main.tex L34）原文是 "yet no method estimates"，非 "None estimates"，语法正确。R2 引用不准确。

**[AGREE] R2-W9** — 引用格式一致性属 camera-ready 问题。

### 核心分歧总结
1. R2-N2 我认为是措辞精度问题而非 systematic overclaiming
2. R2-W1 arXiv K*=3 实际有 5 模型/4 家族支撑，R2 仅看到 Abstract 中的 "two architectures"
3. R2-W7/W8 属事实性偏差
4. 其余 N/W 项与我独立审查一致


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2284 · 2026-05-22T05:39:55.750347+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 173

## Round 173

2 recorded events


### User

_source line 2285 · 2026-05-22T05:39:58.320045+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心分歧点：
- R2-N2（overclaiming）：我认为是措辞精度问题，非系统性 overclaiming
- R2-W1（arXiv 仅 2 模型）：事实不准确，Table 4 显示 5 模型 / 4 家族
- R2-W7/W8：分别为主观判断偏差和引用不准确
- 其余 N/W 项与我的独立审查结论一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2286 · 2026-05-22T05:40:02.536398+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 174

## Round 174

12 recorded events


### User

_source line 2287 · 2026-05-22T05:41:12.057290+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: ANOVA Table 24 统计值全部为占位符**

同意这是 critical issue。我在审稿中发现了 Table 21（跨域 pairwise AUC）存在同样的问题——所有数据单元格均为 em-dash。R1 进一步发现 Table 24（ANOVA）也是如此，且该表的标题中直接得出了 "non-significant Scorer main effect confirms scorer independence" 的结论。一个没有数据的表格不能作为任何统计结论的证据。这比 Table 21 更严重，因为 scorer independence 是论文核心 claim（"K* is governed by the generation process rather than the scoring model", Section 6 第 3 段）的直接支柱。

---

**[AGREE] R1-N2: 附录 4 个数据表全部为占位符**

同意。结合我发现的 Table 21 和 R1 发现的 Tables S10/S11/S12/S13（对应 PDF 中未编号或附录编号的表），至少有 **5 个附录表**数据完全缺失。这构成系统性的投稿质量问题，而非个别疏忽。主文 Section 4.5 引用了跨域 AUC 数值（如 "Wikipedia yields K*=2, AUC: 0.623"），这些数字可能来自正文 Table 4，但 Table 4 仅提供模型级别汇总，缺少逐深度对的分解——而这正是 Table S12/Table 21 应当提供的。附录本应是支撑正文 claims 的详细证据，现在这些证据全部缺失。

---

**[AGREE] R1-N3: Dose-response 分析表明 K*-aware 过滤在现实污染比例下无实际效益**

同意，这与我的 W3 一致。我在审稿中明确指出：Appendix D.8 显示 10-30% 污染比例下所有过滤策略趋于不可区分（p > 0.3 at 10%），而 Section 5 仅报告 100% 设定。R1 补充了更精确的数字（Δ_max = 0.03pp at 10%, p > 0.8），进一步强化了这一点。

补充我的看法：Section 5 正文第 17 行确实包含了一句 caveat（"These effects are measured in a 100% synthetic upper-bound setting; real-world contamination ratios are typically lower"），但这一句嵌在段落中间，容易被忽略。更关键的是，论文将 filtering 作为 contribution 之一（Introduction 最后一段 "As a downstream validation"），但该 validation 仅在最不现实的设定下成立。建议作者将 filtering 重新定位为 consistency check，并在正文中加入 dose-response 结果的 summary（至少一句）。

---

**[AGREE] R1-N4: Cross-scorer 验证削弱了 continuation 模式的 K*=2**

同意，且这是一个被论文自身数据直接证伪的 claim。Table 22（p.18）明确显示 Qwen-1.5B-Instruct Continuation: Self=2, Pythia=1, OLMo=1, Agreement=×。论文 Limitation 4 承认 "cross-scorer validation drops this to K*=1"，但 Discussion Section 6 第 3 段仍写 "Cross-scorer validation confirms K*_empirical is governed by the generation process rather than the scoring model (ρ > 0.90 feature ranking preservation)"。这里用 feature ranking ρ 来替代 K* agreement 是 misleading——feature ranking 一致不等于 K* 判定一致。

R1 的核心论点成立：当唯一完成了 cross-scoring 的 continuation 配置（Qwen-cont）显示 K*=2 是 scorer-dependent 时，论文不应将 scorer independence 作为一般性结论。仅 Qwen-rewrite 模式的 cross-scorer agreement 一致（Self=2, Pythia=2, OLMo=2, ✓），而这是信号最强的配置（1v2 AUC = 0.696, 远超 θ），不能代表 borderline 情况。

---

### Should-Fix

**[AGREE] R1-W1: Qwen 家族过度代表**

同意。4/10 配置来自 Qwen 变体，且全部为 K*=2。按家族去重：
- K*=2 确认：Qwen（4 configs 均为 2）、LLaMA-3.1-8B、Pythia-1.4B → 3 个家族
- K*=1 确认：OLMo-1B、Mistral-7B、Gemma-2-2B → 3 个家族
- 分裂：Pythia（1.4B=2, 6.9B=1）

去重后 K*=2 比例从 "6/10 configurations" 变为 "3/6 families (+ 1 split)"，远不如 "6/10" 看起来有说服力。论文应当同时报告 per-family 和 per-configuration 的统计。

---

**[AGREE] R1-W2: DPI 到 AUC 的理论桥接不完整**

同意。DPI 保证 I(X; Y_k) ≥ I(X; Y_{k+1})（整体互信息单调递减），但论文应用于 AUC_{k-1,k}（**相邻**代际的 pairwise 分类精度），两者不等价。AUC_{k-1,k} 依赖于 Y_{k-1} 和 Y_k 之间的可区分性，而非 X 和 Y_k 之间的互信息。理论上可以构造 I(X;Y_k) 单调递减但 AUC_{k-1,k} 非单调的情况（例如，信号从一种 pattern 突变到另一种 pattern）。

Section 3.1 的 "the original signal degrades monotonically" → "guarantees a finite K*" 的推导跳过了这个 gap。建议作者明确这是一个启发性动机（heuristic motivation）而非严格证明。

---

**[REBUT] R1-W3: θ=0.60 阈值的事后选择风险**

部分反驳。R1 认为三条证据中第三条（5-11pp distributional discontinuity）是 data-driven/post-hoc。这一点我同意。但前两条——(1) Cohen's h = 0.20 对应"小效应量"的独立基准（来自统计学文献，不依赖本文数据），(2) AUC = 0.60 对应 Cohen's h ≈ 0.20（数学关系，不依赖数据）——是先验且独立的。

此外，Section 3.1 提供了 sensitivity analysis：Figure 3 展示了 K*_empirical 在 θ 从 0.55 到 0.70 的变化轨迹，6/10 配置在 θ ∈ [0.55, 0.65] 范围内稳定为 K*=2，只有在 θ=0.70 时才全部降至 K*=1。这表明 K*=2 的结论对 θ 有一定鲁棒性，不是 θ=0.60 的精确选择产物。

综上：θ=0.60 的选择有足够的先验理论基础（Cohen's h），但我同意第三条 distributional discontinuity 证据应标记为 post-hoc confirmatory 而非 independent evidence。

---

**[AGREE] R1-W4: Filtering 实验仅在单一 generator 上验证**

同意。Section 5 的全部 filtering 实验基于 Qwen2.5-1.5B-Instruct continuation 生成的数据。鉴于不同 generator 的 K* 不同（OLMo-1B K*=1, Pythia-1.4B K*=2），filtering 的最优策略可能因 generator 而异。至少应在一个 K*=1 的 generator（如 OLMo-1B）上重复 filtering 实验以验证 "binary filtering is optimal when K*≤2" 的一般性。

---

### 小问题

**[AGREE] Table 1 仅列 6 配置但声称 10：** 正文 Section 4 开头提到 "10 model configurations spanning six architecture families"，但 Table 1 仅列出 6 个。剩余 4 个（Pythia-6.9B, LLaMA-3.1-8B, Mistral-7B, Gemma-2-2B）在 Section 4.1 正文中才出现。应在 Table 1 中列出全部 10 个配置，或明确标注 Table 1 仅展示主要配置。

**[REBUT] "one-wash laundering" 术语误导：** 部分反驳。R1 认为 K*=2 应称 "two-wash"。但论文的 "one-wash" 指的是 "一次生成就足以让文本与更深层合成内容不可区分"——即从 depth 1 开始，再经过一次 generation（the "wash"）就到达不可区分区域（depth 2+）。Discussion Section 6 第 1 段明确解释了这一含义。不过我承认该术语可能造成混淆：直觉上 "one-wash" 更像 K*=1（一次就不可辨别）。建议作者考虑改为 "two-generation boundary" 或在首次使用时加括号说明。

**[AGREE] Figure 3 x 轴标签可读性差：** 我在审稿中同样指出 Figure 5 x 轴标签有可读性问题。这是通病。

**[AGREE] Table 4 脚注过密：** 同意，minor formatting issue。

**[AGREE] K*_empirical 定义隐含 AUC 单调递减假设：** 同意，与 W2 相关。max 算子的使用假设了一旦 AUC 降至 θ 以下就不会回升。虽然实证数据支持单调递减（Table 8），但定义本身应明确这一假设或改用更严格的定义（如 "最大连续可区分深度"）。

---

### Questions

**Q1** [AGREE]：Table 21（我发现）+ Tables S10/S11/S12/S13 + Table 24（R1 发现）——至少 6 个附录表为占位符。这几乎肯定是实验完成但数据未填入 LaTeX 模板的结果，而非实验未完成（因为主文引用了具体数值）。但无论原因，这是不可接受的投稿状态。

**Q2** [AGREE]：我在 Question 4 中提出了本质相同的问题。现实 web-scale 合成比例的估计对论文实用价值的评估至关重要。

**Q3** [AGREE]：Table 22 仅对 2/7 generator 完成了 cross-scoring。扩展覆盖面（尤其是 K*=1 的 generator）是验证 scorer independence claim 的必要条件。

**Q4** [AGREE]：我在 W2 中提出了相同的 scale concern。如果 frontier models 的 K*=1，论文的核心发现可能仅适用于一个正在被淘汰的模型规模窗口。

**Q5** [AGREE]：与 W2 和小问题中的 "隐含单调假设" 一致。

---

### Missing References

**[REBUT] R1-Missing: Kirchenbauer et al. (2023) "A Watermark for Large Language Models"**

不同意将其列为 missing reference。该论文研究的是 LLM watermarking（通过修改 token 生成概率嵌入可检测水印），与本文的 generational depth estimation 属于不同问题。Watermarking 需要生成时的主动干预（active intervention during generation），而本文处理的是对已有文本的被动分析（passive analysis of existing text）。Related Work Section 2 的范围——model collapse、binary detection、data curation、ordinal classification——合理地不包含 watermarking。

不过，如果作者希望在 "Beyond binary detection" 段落中增加一句以示区分（"Watermarking approaches [Kirchenbauer et al., 2023] require generation-time intervention and are orthogonal to post-hoc depth estimation"），这是合理的但非必要的。

---

### 总结

R1 的审稿意见整体质量高，我同意其绝大多数发现。最关键的共识：

1. **附录数据缺失是系统性问题**（R1 发现 5 个表 + 我发现 1 个 = 至少 6 个空表），不是偶然疏忽
2. **Cross-scorer validation 实际上部分证伪了 scorer independence claim**（Qwen-cont K*=2→1），这一点 R1 的分析比我更精确
3. **Filtering 的实用价值在现实污染比例下消失**，两位 reviewer 一致指出
4. **Qwen 过度代表**导致 "6/10 = K*=2" 的统计夸大

两位 reviewer 的主要分歧在 Overall 评分：R1 给 3.0 (Findings)，我给 3.5 (Borderline Conference)。考虑到 R1 发现的额外空表问题（N1/N2 比我发现的更广泛），以及 N4 对 scorer independence 的精确证伪，我认为如果作者无法在 rebuttal 中提供缺失数据并修正 framing，3.0 是合理的。但如果附录数据仅是排版遗漏（主文数值确实来自完成的实验），且作者在 revision 中修正 K* framing + 补充 cross-scoring 覆盖面，论文仍有 3.5 的潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2288 · 2026-05-22T05:41:44.230547+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool call

_source line 2289 · 2026-05-22T05:41:44.281327+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2290 · 2026-05-22T05:41:44.332429+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T05:26:09.679191+00:00\", \"completed_at\": \"2026-05-22T05:30:20.923856+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 18\", \"message\": \"Table 21 所有数据单元格均为 em dash（—），无任何数值。该表标题声称展示三个文本域的 Pairwise AUC，但内容为空。疑似数据未填入或渲染错误，审稿人会视为严重质量问题\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（Title/Abstract/Introduction/Related Work），无任何 display item。第一个视觉锚点（Figure 1 pipeline 图）直到第 3 页才出现。虽在\\\"前 3 页\\\"容忍范围内，但审稿人翻完前两页仍无图表会降低第一印象分\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"单页塞入 3 个 figure（Figure 2 AUC 衰减曲线 + Figure 3 灵敏度曲线 + Figure 4 跨模型迁移热图），视觉密度过高。Figure 3 和 Figure 4 尺寸被压缩，细节难以辨认\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"Figure 4 热图使用红绿配色（高值绿色/低值红色），对红绿色盲不友好。建议改用 Blue-Orange 或 viridis 色系\"}, {\"severity\": \"warning\", \"dimension\": \"page 12\", \"message\": \"Table 10（混淆矩阵）仅占页面下半部分，上方约 50% 为空白\"}, {\"severity\": \"warning\", \"dimension\": \"page 13\", \"message\": \"Table 11（per-depth recall）仅为 3 行小表，占页面约 25%，其余 75% 为空白。可与 Table 10 合并至同一页\"}, {\"severity\": \"warning\", \"dimension\": \"page 15\", \"message\": \"Section C 标题 + Table 13 仅占右栏中部，页面约 70% 为空白。可将 Table 13 上移或与前页内容合并\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（pipeline 图）清晰传达方法核心流程，作为首个 display item 能有效建立审稿人认知锚点。Caption 自包含程度良好\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 和 Table 3 使用 booktabs 风格，最优值加粗标注，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 5 下游任务表格格式整洁，最优值加粗，精度位数统一\"}, {\"severity\": \"info\", \"dimension\": \"page 10\", \"message\": \"Figure 5 柱状图 x 轴标签旋转约 45°且字号偏小，在 150 DPI 下勉强可读，建议适当增大或简化标签\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"正文最后一页（Conclusion + Limitations）内容填充约 75%，在可接受范围内\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\":
…[truncated 539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 2291 · 2026-05-22T05:41:44.333175+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2292 · 2026-05-22T05:41:58.285498+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2293 · 2026-05-22T05:41:58.336160+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2294 · 2026-05-22T05:46:45.191345+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-contamination",
  "issues_yaml": "## Review Issues Tracker — gen-depth-contamination\n## Updated: Round 24 (fresh review, 2026-05-22, Overall 3.0)\n\n# === CRITICAL / MUST-FIX ===\n\n- id: \"R24-C1\"\n  summary: \"附录至少 5-6 个数据表为空占位符（ANOVA、域消融、Pythia 解码、长度消融、Scorer sensitivity）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Round 23 已部分发现空表问题（R23-M2 orphan bib 相关）\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1 发现 Table 24 (ANOVA F/p/η² 全空)、Table S10 (Pythia 解码 30 值全空)、Table S11 (长度消融 15 值全空)、Table S13 (5/7 generator cross-scorer 为 ---)。R2 独立发现 Table 21/S12 (跨域 pairwise AUC 21 值全空)。总计至少 5-6 个空表。ANOVA 空表尤严重——scorer independence 是 cross-model transfer 核心支柱。两位 Reviewer 一致认为构成系统性投稿质量问题。\"\n  action_items:\n    - round: 24\n      action: \"填充所有空占位符表格的实际数据；如实验未完成则移除引用这些表格的声明\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-C2\"\n  summary: \"Cross-scorer 验证部分证伪 scorer independence claim（Qwen-cont K*=2→1）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"R22-W1: 跨模型迁移 boundary-level 失败需更充分讨论\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1 精确分析：Qwen-cont 自身打分 K*=2 (1v2 AUC=0.611, CI lower=0.602, 仅超 θ 约 0.002)，Pythia 打分 AUC=0.5923<θ，OLMo 打分 AUC=0.5858<θ。Discussion 仍写 'confirms K* governed by generation process'，用 feature ranking ρ 替代 K* agreement 是 misleading。R2 完全同意并补充：仅 Qwen-rewrite (信号最强, 1v2 AUC=0.696) 在 cross-scorer 下保持 K*=2。\"\n  action_items:\n    - round: 24\n      action: \"Discussion 修正 scorer independence 措辞：区分 'robust K*=2' (Qwen-rw) 和 'marginal K*=2' (Qwen-cont, scorer-dependent)；扩展 Table 22 覆盖更多 generator-scorer 组合\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1\"\n  summary: \"DPI→adjacent-pair AUC 推理链存在逻辑缺口\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。两者缺形式化桥梁。\"\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"DPI 约束累积信息量，K* 基于相邻对 AUC，后者取决于 Markov chain mixing rate。建议定位 DPI 为 motivating heuristic。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C1: Section 3.1 仍使用 'guarantee' 措辞。Section 6 自己承认 DPI 不 bound K*，但 3.1 不一致。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"framing 方向正确但仍可进一步弱化 DPI 角色。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"两位 Reviewer 一致：DPI 保证 I(X;Y_k) 单调递减，但论文应用于 AUC_{k-1,k}（相邻代际 pairwise 分类精度），两者不等价。应明确 DPI 是 heuristic motivation 而非 strict proof。Section 3.1 'the original signal degrades monotonically → guarantees a finite K*' 推导跳过了 gap。\"\n  action_items:\n    - round: 22\n      action: \"全文 grep 'guarantee' 替换为 'motivate/imply'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 24\n      action: \"Section 3.1 明确 DPI 为 heuristic motivation 而非 strict guarantee；AUC 单调递减标记为经验观察\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"θ 选在经验间隔处，K* 在 θ±5pp 就从3变1。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Youden's J + BH 校正 + LOFO 已有改善但 held-out split 更优。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1 维持 Warning：三条独立证据中第三条 (distributional discontinuity) 是 data-driven。R2 部分 rebut：Cohen's h=0.20 是先验基础，Figure 3 sensitivity analysis 表明 K*=2 在 θ∈[0.55,0.65] 内稳定。共识：Cohen's h 提供先验理论基础，但第三条应标为 post-hoc confirmatory 而非 independent evidence。\"\n  action_items:\n    - round: 23\n      action: \"补充 held-out validation\"\n      assigned_to: agent+paper_agent\n      status: in_progress\n    - round: 24\n      action: \"Threshold justification 段落：保留 Cohen's h 和 permutation test 作为主证据；第三条 distributional discontinuity 标为 post-hoc confirmatory\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C3\"\n  summary: \"Prompt-chain 焦点与 model collapse 叙事范围张力\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"Introduction 以 model collapse 为动机但实验几乎全是 prompt-chain。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Introduction 末尾应提及 retrain-chain K*=7，形成完整图景。\"\n    - round: 24\n      reviewer: [R2]\n      note: \"R2-Q5 提出 prompt-chain K*=2 vs retrain-chain K*≥4 是否测量本质不同的现象。未作为独立 critical issue 提出但仍相关。\"\n  action_items:\n    - round: 23\n      action: \"Introduction 末尾加 retrain-chain K*=7 对比；强调 prompt-chain 实践相关性\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C4\"\n  summary: \"模型规模覆盖偏向小模型（7/10 ≤2B），威胁可推广性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"≥7B 仅 3 种，14B 仅 1 种。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Qwen 占 5/10，≥7B 仅 3 个。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1-W1: Qwen 4/10 配置过度代表。R2-W2: 缺少 >8B 模型，scale trend (0v1 JSD 递减) 暗示 13B+ 可能 K*=1。两位一致：按家族去重 K*=2 比例从 6/10 降为 3/6 (+1 split)。应同时报告 per-family 统计。\"\n  action_items:\n    - round: 24\n      action: \"Abstract/Conclusion 同时报告 per-configuration 和 per-family K*=2 统计；弱化跨架构可推广性声称；标注 ≤8B 适用范围\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING / SHOULD-FIX ===\n\n- id: \"R1-W4\"\n  summary: \"K*=2 可能是 15D 特征空间容量上限（分类器依赖性）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"需更系统使用 K*_15D 和 K*_DeBERTa 符号消除歧义。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R2-N2 (Critical): K*_empirical 被 frame 为 'the discrimination boundary' 而非 feature-specific lower bound。R1 部分 rebut：Section 3.1 已写 'operational lower bound'，是措辞精度问题非 systematic overclaiming。共识：至少 Abstract/Introduction 应引入 'lower bound' 限定语。\"\n  action_items:\n    - round: 24\n      action: \"Abstract 加 'lower bound' 限定语；Section 3 定义 K*_empirical 时立即说明与 K*_theory 关系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Filtering 实验效果量在现实污染比例下极小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"将 Section 5 重新定位为 consistency check 而非独立贡献。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"两位一致：10% 污染 Δ_max=0.03pp (p>0.8)，30% Δ=0.10pp (p>0.3)，50% 0.24pp (p=0.12)。仅 100% 下显著。主文应提及 dose-response convergence；filtering 重新定位为 consistency check。R2 补充 Section 5 L17 有一句 caveat 但嵌在段落中间易被忽略。\"\n  action_items:\n    - round: 24\n      action: \"Section 5 标题/首句定位为 consistency check；正文加入 dose-response 结果 summary（至少一句）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W11\"\n  summary: \"Filtering 仅在单一 generator（Qwen-1.5B cont）上验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1-W4 提出，R2 完全同意。不同 generator K* 不同，filtering 最优策略可能因 generator 而异。至少应在 K*=1 generator（如 OLMo-1B）上重复验证。\"\n  action_items:\n    - round: 24\n      action: \"在至少 1 个 K*=1 generator 上重复 filtering 实验，或在 Limitations 中明确声明\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Abstract 开头加 K* 直觉定义；移除 Section 引用；精简技术细节。\"\n    - round: 24\n      reviewer: [R2]\n      note: \"R2-W7: 约 200 词内含大量定量细节（θ=0.60, Cohen's h, 6/10, ρ>0.90, MMLU 0.5941 等），认知负担高。R1 rebut：NLP 顶会 abstract 需传达核心贡献，认为正常。分歧记录。\"\n  action_items:\n    - round: 24\n      action: \"考虑精简 Abstract 统计细节，保留核心发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"扩展至 8-12 行。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R2-W6: 仅 3 句正文 + 1 句 future work。R1 同意。共识：扩展至 5-7 句，加入实践建议和主要局限 high-level 总结。当前 Conclusion 实测约 4 行（8 页第 7 页底部），仍不足。\"\n  action_items:\n    - round: 24\n      action: \"Conclusion 扩展至 5-7 句，增加 K*=2 实践指导、prompt-chain vs retrain-chain broader implications\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"与 Geng et al. (2026) 和 Wang et al. (2025) 的技术区分不够清晰\"\n  category: related_work\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"K* 的操作层面独特性需更显著强调。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R2-W4: 缺 Wang et al. (ACL 2025) 'Unveiling Attractor Cycles' 和 Fu et al. (ICLR 2025) 'How to Prevent Model Collapse'。R1 同意两篇均直接相关。共识：在 Related Work model collapse 段落增加引用并讨论 K* 与 attractor convergence 关系。\"\n  action_items:\n    - round: 24\n      action: \"Related Work 增加 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025)；讨论 K* vs attractor convergence vs self-consuming stability\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M2\"\n  summary: \"K* 符号系统过度增殖\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"检查 notation table 覆盖所有 K* 变体。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R2-W5: K*_empirical, K*_theory, K*_neural——K*_theory 仅作占位符未实证处理。R1 轻度同意。共识：简化为 K*（实证）和 K*_theory（理论上界），K*_neural 作 Section 4.4 局部记号。\"\n  action_items:\n    - round: 24\n      action: \"简化 K* 符号体系；Section 3 一次性定义三者关系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-W1\"\n  summary: \"跨模型迁移 boundary-level 失败需更充分讨论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Abstract framing 已改善，Discussion 中 transfer implications 仍需更深入。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"被 R24-C2 (cross-scorer contradiction) 吸收。cross-scorer 结果表明 boundary-level transfer 失败不仅是跨模型问题，也是跨 scorer 问题。\"\n  action_items:\n    - round: 24\n      action: \"与 R24-C2 合并处理\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-W5\"\n  summary: \"Retrain-chain CI 方法与主实验不一致\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"容易修复，说明 retrain-chain 使用 t-CI 的原因。\"\n    - round: 24\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === MINOR ===\n\n- id: \"R23-M1\"\n  summary: \"遗漏 Fu et al. (2025) ICLR 引用\"\n  category: related_work\n  severity: minor\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Fu et al. 与 K* 有限边界概念直接相关。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R24 两位 Reviewer 再次一致指出。已合并至 R2-W1 action items。\"\n  action_items:\n    - round: 24\n      action: \"与 R2-W1 合并处理\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M2\"\n  summary: \"Orphan bib entries / 引用格式不一致\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"hao2025rewrite, tang2024science, wu2023survey 未被引用。\"\n    - round: 24\n      reviewer: [R2]\n      note: \"R2-W9: 39 条引用中 8 条缺 URL，格式不一致。R1 同意属 camera-ready 问题。\"\n  action_items:\n    - round: 24\n      action: \"删除 orphan bib entries；统一补全 URL\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M3\"\n  summary: \"ANOVA 交互效应 vs generator-independent 措辞\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1]\n      note: \"将 'generator-independent' 调整为 'largely generator-invariant'。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"被 R24-C1 (ANOVA 空表) 吸收——ANOVA 表本身数据缺失，措辞问题在数据填充前无法独立解决。\"\n  action_items:\n    - round: 24\n      action: \"待 ANOVA 表填充后再调整措辞\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M1\"\n  summary: \"Table 1 仅列 6 配置但声称 10\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"正文 Section 4 开头提 10 个配置，Table 1 仅列 6 个，其余 4 个在正文才出现。应在 Table 1 列出全部或添加脚注说明。\"\n  action_items:\n    - round: 24\n      action: \"Table 1 列出全部 10 配置，或添加脚注说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M2\"\n  summary: \"'one-wash laundering' 术语可能造成混淆\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1：K*=2 应称 'two-wash'。R2 部分 rebut：指一次 generation 就到达不可区分区域。R2 同意术语可能造成混淆，建议改为 'two-generation boundary' 或首次使用加括号说明。\"\n  action_items:\n    - round: 24\n      action: \"考虑改名或首次使用加说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M3\"\n  summary: \"K*_empirical 定义中 max 算子隐含 AUC 单调递减假设\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1 提出，R2 同意。max 算子假设 AUC 降至 θ 以下后不会回升。实证支持单调递减，但定义应明确该假设或改用 '最大连续可区分深度'。\"\n  action_items:\n    - round: 24\n      action: \"Eq.1 后加一句明确单调递减假设，或改为 max{k: ∀j≤k, AUC_{j-1,j}>θ}\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M4\"\n  summary: \"Figure 4 热图红绿配色对色盲不友好\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [visual_check]\n      note: \"视觉审查发现 Figure 4 使用红绿配色，建议改用 Blue-Orange 或 viridis。\"\n  action_items:\n    - round: 24\n      action: \"Figure 4 配色改为色盲友好色系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M3\"\n  summary: \"Appendix 交叉引用不一致\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewer: R1\n      note: \"Table 9 标题提到 'Table 4' 但正文 Table 4 是 cross-model transfer heatmap。\"\n    - round: 24\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === RESOLVED (from prior rounds) ===\n\n- id: \"R2-N1\"\n  summary: \"Abstract 对迁移结果选择性报告\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Abstract 已包含边界迁移失败信息\"\n  resolution_round: 23\n\n- id: \"R2-M1\"\n  summary: \"holtzman2020curious orphan bib 条目\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"已删除\"\n  resolution_round: 21\n\n- id: \"R20-M4\"\n  summary: \"'model-free' 表述已改为 'generator-independent'\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"已全文替换\"\n  resolution_round: 21\n\n- id: \"R2-W2\"\n  summary: \"混合场景（prompt-chain + retrain-chain）未讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已加 Mixed-chain 段落\"\n  resolution_round: 21\n\n- id: \"R1-N3\"\n  summary: \"Qwen 家族 5/10 配置偏重，'7/9' 统计量误导\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已修改 framing 为 '4/6 families' primary\"\n  resolution_round: 21\n\n- id: \"R2-N2\"\n  summary: \"遗漏 Wang et al. (ACL 2025) 相关工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已添加引用\"\n  resolution_round: 21\n\n- id: \"R2-N3\"\n  summary: \"'One-wash laundering' framing 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已重写\"\n  resolution_round: 21\n\n- id: \"R22-Q6\"\n  summary: \"Generator identity AUC 数值不一致 (0.006 vs +0.008)\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Round 23 未再提及，数值已统一\"\n  resolution_round: 23\n\n- id: \"R1-W1\"\n  summary: \"LOFO θ=0.60 验证存在数据层面依赖\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"被 R1-N2 的 held-out validation 讨论吸收。\"\n    - round: 24\n      reviewer: []\n      note: \"本轮未直接提及，被 R1-N2 (θ=0.60) 讨论吸收。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-contamination",
    "issues_yaml": "## Review Issues Tracker — gen-depth-contamination\n## Updated: Round 24 (fresh review, 2026-05-22, Overall 3.0)\n\n# === CRITICAL / MUST-FIX ===\n\n- id: \"R24-C1\"\n  summary: \"附录至少 5-6 个数据表为空占位符（ANOVA、域消融、Pythia 解码、长度消融、Scorer sensitivity）\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Round 23 已部分发现空表问题（R23-M2 orphan bib 相关）\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1 发现 Table 24 (ANOVA F/p/η² 全空)、Table S10 (Pythia 解码 30 值全空)、Table S11 (长度消融 15 值全空)、Table S13 (5/7 generator cross-scorer 为 ---)。R2 独立发现 Table 21/S12 (跨域 pairwise AUC 21 值全空)。总计至少 5-6 个空表。ANOVA 空表尤严重——scorer independence 是 cross-model transfer 核心支柱。两位 Reviewer 一致认为构成系统性投稿质量问题。\"\n  action_items:\n    - round: 24\n      action: \"填充所有空占位符表格的实际数据；如实验未完成则移除引用这些表格的声明\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-C2\"\n  summary: \"Cross-scorer 验证部分证伪 scorer independence claim（Qwen-cont K*=2→1）\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"R22-W1: 跨模型迁移 boundary-level 失败需更充分讨论\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1 精确分析：Qwen-cont 自身打分 K*=2 (1v2 AUC=0.611, CI lower=0.602, 仅超 θ 约 0.002)，Pythia 打分 AUC=0.5923<θ，OLMo 打分 AUC=0.5858<θ。Discussion 仍写 'confirms K* governed by generation process'，用 feature ranking ρ 替代 K* agreement 是 misleading。R2 完全同意并补充：仅 Qwen-rewrite (信号最强, 1v2 AUC=0.696) 在 cross-scorer 下保持 K*=2。\"\n  action_items:\n    - round: 24\n      action: \"Discussion 修正 scorer independence 措辞：区分 'robust K*=2' (Qwen-rw) 和 'marginal K*=2' (Qwen-cont, scorer-dependent)；扩展 Table 22 覆盖更多 generator-scorer 组合\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1\"\n  summary: \"DPI→adjacent-pair AUC 推理链存在逻辑缺口\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。两者缺形式化桥梁。\"\n    - round: 21\n      reviewer: [R1, R2]\n      note: \"DPI 约束累积信息量，K* 基于相邻对 AUC，后者取决于 Markov chain mixing rate。建议定位 DPI 为 motivating heuristic。\"\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"C1: Section 3.1 仍使用 'guarantee' 措辞。Section 6 自己承认 DPI 不 bound K*，但 3.1 不一致。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"framing 方向正确但仍可进一步弱化 DPI 角色。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"两位 Reviewer 一致：DPI 保证 I(X;Y_k) 单调递减，但论文应用于 AUC_{k-1,k}（相邻代际 pairwise 分类精度），两者不等价。应明确 DPI 是 heuristic motivation 而非 strict proof。Section 3.1 'the original signal degrades monotonically → guarantees a finite K*' 推导跳过了 gap。\"\n  action_items:\n    - round: 22\n      action: \"全文 grep 'guarantee' 替换为 'motivate/imply'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 24\n      action: \"Section 3.1 明确 DPI 为 heuristic motivation 而非 strict guarantee；AUC 单调递减标记为经验观察\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"θ 选在经验间隔处，K* 在 θ±5pp 就从3变1。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Youden's J + BH 校正 + LOFO 已有改善但 held-out split 更优。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1 维持 Warning：三条独立证据中第三条 (distributional discontinuity) 是 data-driven。R2 部分 rebut：Cohen's h=0.20 是先验基础，Figure 3 sensitivity analysis 表明 K*=2 在 θ∈[0.55,0.65] 内稳定。共识：Cohen's h 提供先验理论基础，但第三条应标为 post-hoc confirmatory 而非 independent evidence。\"\n  action_items:\n    - round: 23\n      action: \"补充 held-out validation\"\n      assigned_to: agent+paper_agent\n      status: in_progress\n    - round: 24\n      action: \"Threshold justification 段落：保留 Cohen's h 和 permutation test 作为主证据；第三条 distributional discontinuity 标为 post-hoc confirmatory\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C3\"\n  summary: \"Prompt-chain 焦点与 model collapse 叙事范围张力\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"Introduction 以 model collapse 为动机但实验几乎全是 prompt-chain。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Introduction 末尾应提及 retrain-chain K*=7，形成完整图景。\"\n    - round: 24\n      reviewer: [R2]\n      note: \"R2-Q5 提出 prompt-chain K*=2 vs retrain-chain K*≥4 是否测量本质不同的现象。未作为独立 critical issue 提出但仍相关。\"\n  action_items:\n    - round: 23\n      action: \"Introduction 末尾加 retrain-chain K*=7 对比；强调 prompt-chain 实践相关性\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C4\"\n  summary: \"模型规模覆盖偏向小模型（7/10 ≤2B），威胁可推广性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 22\n      reviewer: [R1, R2]\n      note: \"≥7B 仅 3 种，14B 仅 1 种。\"\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Qwen 占 5/10，≥7B 仅 3 个。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1-W1: Qwen 4/10 配置过度代表。R2-W2: 缺少 >8B 模型，scale trend (0v1 JSD 递减) 暗示 13B+ 可能 K*=1。两位一致：按家族去重 K*=2 比例从 6/10 降为 3/6 (+1 split)。应同时报告 per-family 统计。\"\n  action_items:\n    - round: 24\n      action: \"Abstract/Conclusion 同时报告 per-configuration 和 per-family K*=2 统计；弱化跨架构可推广性声称；标注 ≤8B 适用范围\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING / SHOULD-FIX ===\n\n- id: \"R1-W4\"\n  summary: \"K*=2 可能是 15D 特征空间容量上限（分类器依赖性）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"需更系统使用 K*_15D 和 K*_DeBERTa 符号消除歧义。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R2-N2 (Critical): K*_empirical 被 frame 为 'the discrimination boundary' 而非 feature-specific lower bound。R1 部分 rebut：Section 3.1 已写 'operational lower bound'，是措辞精度问题非 systematic overclaiming。共识：至少 Abstract/Introduction 应引入 'lower bound' 限定语。\"\n  action_items:\n    - round: 24\n      action: \"Abstract 加 'lower bound' 限定语；Section 3 定义 K*_empirical 时立即说明与 K*_theory 关系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Filtering 实验效果量在现实污染比例下极小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"将 Section 5 重新定位为 consistency check 而非独立贡献。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"两位一致：10% 污染 Δ_max=0.03pp (p>0.8)，30% Δ=0.10pp (p>0.3)，50% 0.24pp (p=0.12)。仅 100% 下显著。主文应提及 dose-response convergence；filtering 重新定位为 consistency check。R2 补充 Section 5 L17 有一句 caveat 但嵌在段落中间易被忽略。\"\n  action_items:\n    - round: 24\n      action: \"Section 5 标题/首句定位为 consistency check；正文加入 dose-response 结果 summary（至少一句）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W11\"\n  summary: \"Filtering 仅在单一 generator（Qwen-1.5B cont）上验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1-W4 提出，R2 完全同意。不同 generator K* 不同，filtering 最优策略可能因 generator 而异。至少应在 K*=1 generator（如 OLMo-1B）上重复验证。\"\n  action_items:\n    - round: 24\n      action: \"在至少 1 个 K*=1 generator 上重复 filtering 实验，或在 Limitations 中明确声明\"\n      assigned_to: agent+paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Abstract 开头加 K* 直觉定义；移除 Section 引用；精简技术细节。\"\n    - round: 24\n      reviewer: [R2]\n      note: \"R2-W7: 约 200 词内含大量定量细节（θ=0.60, Cohen's h, 6/10, ρ>0.90, MMLU 0.5941 等），认知负担高。R1 rebut：NLP 顶会 abstract 需传达核心贡献，认为正常。分歧记录。\"\n  action_items:\n    - round: 24\n      action: \"考虑精简 Abstract 统计细节，保留核心发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"扩展至 8-12 行。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R2-W6: 仅 3 句正文 + 1 句 future work。R1 同意。共识：扩展至 5-7 句，加入实践建议和主要局限 high-level 总结。当前 Conclusion 实测约 4 行（8 页第 7 页底部），仍不足。\"\n  action_items:\n    - round: 24\n      action: \"Conclusion 扩展至 5-7 句，增加 K*=2 实践指导、prompt-chain vs retrain-chain broader implications\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"与 Geng et al. (2026) 和 Wang et al. (2025) 的技术区分不够清晰\"\n  category: related_work\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"K* 的操作层面独特性需更显著强调。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R2-W4: 缺 Wang et al. (ACL 2025) 'Unveiling Attractor Cycles' 和 Fu et al. (ICLR 2025) 'How to Prevent Model Collapse'。R1 同意两篇均直接相关。共识：在 Related Work model collapse 段落增加引用并讨论 K* 与 attractor convergence 关系。\"\n  action_items:\n    - round: 24\n      action: \"Related Work 增加 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025)；讨论 K* vs attractor convergence vs self-consuming stability\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-M2\"\n  summary: \"K* 符号系统过度增殖\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"检查 notation table 覆盖所有 K* 变体。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R2-W5: K*_empirical, K*_theory, K*_neural——K*_theory 仅作占位符未实证处理。R1 轻度同意。共识：简化为 K*（实证）和 K*_theory（理论上界），K*_neural 作 Section 4.4 局部记号。\"\n  action_items:\n    - round: 24\n      action: \"简化 K* 符号体系；Section 3 一次性定义三者关系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-W1\"\n  summary: \"跨模型迁移 boundary-level 失败需更充分讨论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Abstract framing 已改善，Discussion 中 transfer implications 仍需更深入。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"被 R24-C2 (cross-scorer contradiction) 吸收。cross-scorer 结果表明 boundary-level transfer 失败不仅是跨模型问题，也是跨 scorer 问题。\"\n  action_items:\n    - round: 24\n      action: \"与 R24-C2 合并处理\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-W5\"\n  summary: \"Retrain-chain CI 方法与主实验不一致\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 23\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"容易修复，说明 retrain-chain 使用 t-CI 的原因。\"\n    - round: 24\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === MINOR ===\n\n- id: \"R23-M1\"\n  summary: \"遗漏 Fu et al. (2025) ICLR 引用\"\n  category: related_work\n  severity: minor\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"Fu et al. 与 K* 有限边界概念直接相关。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R24 两位 Reviewer 再次一致指出。已合并至 R2-W1 action items。\"\n  action_items:\n    - round: 24\n      action: \"与 R2-W1 合并处理\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M2\"\n  summary: \"Orphan bib entries / 引用格式不一致\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"hao2025rewrite, tang2024science, wu2023survey 未被引用。\"\n    - round: 24\n      reviewer: [R2]\n      note: \"R2-W9: 39 条引用中 8 条缺 URL，格式不一致。R1 同意属 camera-ready 问题。\"\n  action_items:\n    - round: 24\n      action: \"删除 orphan bib entries；统一补全 URL\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M3\"\n  summary: \"ANOVA 交互效应 vs generator-independent 措辞\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1]\n      note: \"将 'generator-independent' 调整为 'largely generator-invariant'。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"被 R24-C1 (ANOVA 空表) 吸收——ANOVA 表本身数据缺失，措辞问题在数据填充前无法独立解决。\"\n  action_items:\n    - round: 24\n      action: \"待 ANOVA 表填充后再调整措辞\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M1\"\n  summary: \"Table 1 仅列 6 配置但声称 10\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"正文 Section 4 开头提 10 个配置，Table 1 仅列 6 个，其余 4 个在正文才出现。应在 Table 1 列出全部或添加脚注说明。\"\n  action_items:\n    - round: 24\n      action: \"Table 1 列出全部 10 配置，或添加脚注说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M2\"\n  summary: \"'one-wash laundering' 术语可能造成混淆\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1：K*=2 应称 'two-wash'。R2 部分 rebut：指一次 generation 就到达不可区分区域。R2 同意术语可能造成混淆，建议改为 'two-generation boundary' 或首次使用加括号说明。\"\n  action_items:\n    - round: 24\n      action: \"考虑改名或首次使用加说明\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M3\"\n  summary: \"K*_empirical 定义中 max 算子隐含 AUC 单调递减假设\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"R1 提出，R2 同意。max 算子假设 AUC 降至 θ 以下后不会回升。实证支持单调递减，但定义应明确该假设或改用 '最大连续可区分深度'。\"\n  action_items:\n    - round: 24\n      action: \"Eq.1 后加一句明确单调递减假设，或改为 max{k: ∀j≤k, AUC_{j-1,j}>θ}\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M4\"\n  summary: \"Figure 4 热图红绿配色对色盲不友好\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [visual_check]\n      note: \"视觉审查发现 Figure 4 使用红绿配色，建议改用 Blue-Orange 或 viridis。\"\n  action_items:\n    - round: 24\n      action: \"Figure 4 配色改为色盲友好色系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-M3\"\n  summary: \"Appendix 交叉引用不一致\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 21\n  last_seen_round: 21\n  mentions:\n    - round: 21\n      reviewer: R1\n      note: \"Table 9 标题提到 'Table 4' 但正文 Table 4 是 cross-model transfer heatmap。\"\n    - round: 24\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === RESOLVED (from prior rounds) ===\n\n- id: \"R2-N1\"\n  summary: \"Abstract 对迁移结果选择性报告\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Abstract 已包含边界迁移失败信息\"\n  resolution_round: 23\n\n- id: \"R2-M1\"\n  summary: \"holtzman2020curious orphan bib 条目\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"已删除\"\n  resolution_round: 21\n\n- id: \"R20-M4\"\n  summary: \"'model-free' 表述已改为 'generator-independent'\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"已全文替换\"\n  resolution_round: 21\n\n- id: \"R2-W2\"\n  summary: \"混合场景（prompt-chain + retrain-chain）未讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已加 Mixed-chain 段落\"\n  resolution_round: 21\n\n- id: \"R1-N3\"\n  summary: \"Qwen 家族 5/10 配置偏重，'7/9' 统计量误导\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已修改 framing 为 '4/6 families' primary\"\n  resolution_round: 21\n\n- id: \"R2-N2\"\n  summary: \"遗漏 Wang et al. (ACL 2025) 相关工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已添加引用\"\n  resolution_round: 21\n\n- id: \"R2-N3\"\n  summary: \"'One-wash laundering' framing 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已重写\"\n  resolution_round: 21\n\n- id: \"R22-Q6\"\n  summary: \"Generator identity AUC 数值不一致 (0.006 vs +0.008)\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"Round 23 未再提及，数值已统一\"\n  resolution_round: 23\n\n- id: \"R1-W1\"\n  summary: \"LOFO θ=0.60 验证存在数据层面依赖\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 23\n      reviewer: [R1, R2]\n      note: \"被 R1-N2 的 held-out validation 讨论吸收。\"\n    - round: 24\n      reviewer: []\n      note: \"本轮未直接提及，被 R1-N2 (θ=0.60) 讨论吸收。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2295 · 2026-05-22T05:46:45.292623+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml\", \"bytes\": 17739}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-22T05:49:23.064321+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — gen-depth-contamination\n## Round 24 (Fresh Review, 2026-05-22)\n## Venue: EMNLP 2026 (ARR May 2026) | Deadline: 2026-05-25\n\n---\n\n## Summary\n\n本文提出 generational depth estimation，测量递归合成文本的可区分深度边界 K\\*\\_empirical——使用 15 个统计特征 + OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族, 1B-8B）、3 个文本域、4 种解码策略上实验，发现 K\\*\\_empirical ∈ {1,2,3}，一般 web 文本以 K\\*=2 为主导模式（6/10 配置），arXiv 学术文本 K\\*=3。论文验证了跨模型迁移能力（80-100% 精度保持）和 K\\*-aware 数据过滤的下游效用。\n\n---\n\n## Strengths\n\n**S1. 新颖的问题形式化。** Generational depth estimation 填补了 binary detection（人 vs. 机器）与 model collapse 宏观动力学之间的真实空白。K\\* 概念定义清晰、可操作（Eq.1: max{k ≥ 1 : AUC\\_{k-1,k} > θ}），是对现有文献的有意义扩展。\n\n**S2. 统计方法论严谨度高于同类工作。** Bootstrap 95% CI（1,000 resamples）、permutation test（p ≤ 0.002）、Cohen's h 效应量（h ≈ 0.20）、5-fold GroupKFold 交叉验证（按 seed document 分组防泄漏）——这套统计体系在 NLP 实证论文中不常见。\n\n**S3. \"One-wash laundering\" 洞察有实践价值。** K\\*=2 意味着一次生成就足以让 web 文本与更深层合成内容不可区分，对数据策展有直接指导意义：对 web text 而言，超越 binary 过滤的更精细深度策略是不必要的。\n\n**S4. 跨模型迁移设计精巧。** Cross-scorer validation 和 scorer-invariant feature ranking（ρ > 0.90）共同提供了有部署价值的方法论贡献。Continuation-mode 分类器在 Pythia↔OLMo 间保持 90-92% 迁移准确率。\n\n**S5. Limitations 诚实详尽。** 7 条主要局限 + Extended Appendix（retrain-chain, dose-response），主动暴露了 threshold sensitivity、feature-set dependence、marginal boundary cases。\n\n**S6. 模型覆盖面在 ≤8B 范围内合理。** 6 个架构族、rewrite + continuation 两种模式、4 种解码策略、3 个文本域——消融设计系统全面。\n\n---\n\n## Weaknesses\n\n### Critical — Must-Fix\n\n**W1 [Critical, Consensus]** 附录至少 5-6 个数据表为空占位符\n\n两位 Reviewer 独立发现至少 5 个附录表数据完全缺失：\n- Table 21 / S12（跨域 pairwise AUC）：21 个数据单元格全为 em-dash\n- Table 24（Three-way ANOVA: Generator × Scorer × Depth-Pair）：F/p/η²\\_p 全部为 `---`，但标题声称 \"non-significant Scorer main effect confirms scorer independence\"\n- Table S10（Pythia 解码消融）：30 个 AUC 值全空\n- Table S11（长度消融）：15 个 AUC 值全空（仅 K\\* 行有值）\n- Table S13（Scorer sensitivity）：5/7 generator 的 cross-scorer K\\* 为 `---`\n\n这构成系统性投稿质量问题。ANOVA 空表尤其严重——scorer independence 是论文 cross-model transfer 核心支柱，表标题直接下了结论但无任何数据支撑。主文 Section 4.5 引用了具体数值（如 \"Wikipedia yields K\\*=2, AUC: 0.623\"），但完整逐深度对数据缺失。\n\n**W2 [Critical, Consensus]** Cross-scorer 验证部分证伪了 scorer independence claim\n\nQwen-continuation 自身打分 K\\*=2（1v2 AUC = 0.611, CI lower = 0.602, 仅超过 θ 约 0.002），但 Pythia 打分 AUC = 0.5923 < θ，OLMo 打分 AUC = 0.5858 < θ，K\\* 均降为 1（Table 22, Agreement=×）。Discussion 仍写 \"Cross-scorer validation confirms K\\*\\_empirical is governed by the generation process rather than the scoring model\"，用 feature ranking ρ 替代 K\\* agreement 是 misleading——feature ranking 一致不等于 K\\* 判定一致。仅 Qwen-rewrite（信号最强配置, 1v2 AUC = 0.696）在 cross-scorer 下保持 K\\*=2。\n\n### Major — Should-Fix\n\n**W3 [Critical-Major, Divergence]** K\\*\\_empirical framing: \"the discrimination boundary\" vs \"feature-specific lower bound\"\n\n- **R2 (Critical)**：Title/Abstract/Introduction 将 K\\*\\_empirical 定位为 \"the discrimination boundary\"，但 Limitation 5 承认它是 \"feature-set-specific lower bound\"，neural probe K\\*\\_neural∈{1,2,3} 随模型变化。正文与 Limitations 之间存在系统性 overclaiming。\n- **R1 (Warning)**：Section 3.1 Eq.1 前已写 \"We define the operational lower bound\"，K\\*\\_empirical 同时是 empirical boundary 和 K\\*\\_theory 的 lower bound，两层含义不矛盾。是措辞精度问题，未达 systematic overclaiming。\n- **共识方向**：至少 Abstract 和 Introduction 应引入 \"lower bound\" 限定语（如 \"a lower bound on the discrimination boundary\"）。\n\n**W4 [Major, Consensus]** Filtering 在现实污染比例下实用价值消失\n\nAppendix D.8 dose-response 分析：10% 污染所有策略无差异（Δ\\_max = 0.03pp, p > 0.8）；30% 不显著（p > 0.3）；50% 不显著（p = 0.12）。仅 100%（非现实场景）下有显著效果（0.77pp 改善）。主文 Section 5 仅报告 100% 设定，将 filtering 作为 contribution 呈现。应重新定位为 consistency check，在正文中提及 dose-response convergence。\n\n**W5 [Major, Consensus]** Qwen 家族过度代表\n\n4/10 配置来自 Qwen（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），全部 K\\*=2。按家族去重：K\\*=2 确认 3 个家族（Qwen, LLaMA, Pythia-1.4B），K\\*=1 确认 3 个家族（OLMo, Mistral, Gemma），Pythia 分裂（1.4B=2, 6.9B=1）。\"6/10 configurations yield K\\*=2\" 变为 \"3/6 families (+1 split)\"。应同时报告 per-family 和 per-configuration 统计。\n\n**W6 [Major, Consensus]** 缺少 >8B 模型，scale trend 可能使结论失效\n\n0v1 JSD 随模型规模降低（0.15-0.27 at ≤1.5B vs. 0.077 at 8B LLaMA-3.1）。论文推测 \"models at 13B+ may increasingly yield K\\*=1\"。若属实，K\\*=2 仅适用于中小模型，前沿模型可能都是 K\\*=1，缩小实践相关性。应在 Abstract/Conclusion 明确标注 ≤8B 适用范围。\n\n**W7 [Major, Divergence]** arXiv K\\*=3 证据基础\n\n- **R2 (Major)**：仅 2 个模型, n=2200，但作为平行贡献呈现。\n- **R1 (Rebut)**：Table 4 full 实际覆盖 5 模型/4 家族（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B），R2 仅看到 Abstract 的 \"two architectures\"。\n- **共识**：模型覆盖面超出 R2 初判，但 n=2,200 样本量较小，对应的完整 pairwise AUC 支撑表（Table S12/21）为空。\n\n**W8 [Major, Consensus]** 缺少重要相关工作\n\n- Wang, Li, Yan, Cheng, Zhang (ACL 2025) \"Unveiling Attractor Cycles in LLMs\" — prompt-chain attractor cycles 与 K\\* 直接相关\n- Fu, Wang, Chen, Tian, Tao (ICLR 2025) \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" — collapse 理论条件，K\\* 存在的理论背景\n\n### Warning\n\n**W9 [Warning, Consensus]** DPI→AUC 理论桥接不完整。DPI 保证 I(X; Y\\_k) 单调递减，但论文应用于 AUC\\_{k-1,k}（相邻代际 pairwise 分类精度），两者不等价。应明确 DPI 是 heuristic motivation 而非 strict proof。\n\n**W10 [Warning, Partial Consensus]** θ=0.60 阈值事后选择风险。Cohen's h = 0.20 提供先验理论基础（两位共识），但论文三条\"独立\"证据中第三条（distributional discontinuity）是 data-driven（R1 指出），应标为 post-hoc confirmatory。\n\n**W11 [Warning, Consensus]** Filtering 仅在单一 generator（Qwen-1.5B continuation）上验证，应至少在 K\\*=1 generator 上重复。\n\n### Minor\n\n**W12** [Minor, Consensus] Conclusion 过于简短（3-4 句），应扩展至 5-7 句，加实践建议和局限总结。\n\n**W13** [Minor, Consensus] K\\* 符号变体过多（K\\*\\_empirical, K\\*\\_theory, K\\*\\_neural），K\\*\\_theory 仅作占位符。\n\n**W14** [Minor, Divergence] Abstract 信息密度（R2 认为过高，R1 认为正常）。\n\n**W15** [Minor, Consensus] Table 1 仅列 6 配置但声称 10，应添加脚注或列出全部。\n\n**W16** [Minor] \"one-wash laundering\" 术语可能混淆（K\\*=2 ≠ one-wash 直觉），建议首次使用加说明。\n\n**W17** [Minor] Figure 3/5 x 轴标签可读性差；Table 4 脚注过密。\n\n**W18** [Minor] 引用格式不一致（39 条中 8 条缺 URL）。\n\n**W19** [Minor, Consensus] K\\*\\_empirical 定义中 max 算子隐含 AUC 单调递减假设，应明确该假设或改用 \"连续满足条件的最大 k\"。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 达成共识的关键问题：\n1. **[AGREE]** 附录 5-6 个空表构成系统性投稿质量问题（Critical）\n2. **[AGREE]** Cross-scorer 验证部分证伪 scorer independence claim（Critical-Major）\n3. **[AGREE]** Filtering 在 <50% 污染下无显著效果，应重新定位为 consistency check（Major）\n4. **[AGREE]** Qwen 过度代表导致 \"6/10\" 统计夸大（Major）\n5. **[AGREE]** 缺少 >8B 模型限制实践相关性（Major）\n6. **[AGREE]** DPI→AUC 理论桥接不完整（Warning）\n7. **[AGREE]** 缺少 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025) 引用（Major）\n\n## Reviewer Divergence\n\n1. **K\\*\\_empirical overclaiming** (W3)：R1 认为措辞精度问题（Warning），R2 认为系统性 overclaiming（Critical）。共识方向：至少 Abstract/Introduction 需加 \"lower bound\" 限定。\n2. **arXiv 证据基础** (W7)：R1 指出实际 5 模型/4 家族（非 R2 认为的 2 模型），但 n=2,200 样本量和空支撑表关注仍成立。\n3. **Abstract 信息密度** (W14)：R1 认为正常，R2 认为过高。\n4. **Kirchenbauer watermarking 引用**：R1 建议添加，R2 rebut 认为不同问题域（不纳入 Missing References）。\n\n---\n\n## Questions\n\n**Q1.** 附录 5-6 个空表（Tables S10/S11/S12/S13, Table 21, Table 24）是排版遗漏还是实验未完成？如果数据存在，请提供完整数值。\n\n**Q2.** Qwen-continuation 的 K\\*=2 在 cross-scorer 下降为 1（Table 22），如何调和 \"K\\* is governed by the generation process\" 的声明？能否扩展 Table 22 覆盖更多 generator-scorer 组合？\n\n**Q3.** 现实 web-scale 合成内容比例估计为多少？在 10-30% 污染下，K\\*-aware curation 的实际增益是什么？\n\n**Q4.** 13B+ 模型若 K\\*=1，K\\*=2 核心发现是否仅限于正在被淘汰的模型规模窗口？\n\n**Q5.** K\\*\\_empirical 定义中 max 算子是否隐含 AUC 单调递减假设？是否应改为 \"连续满足条件的最大 k\"？\n\n**Q6.** Prompt-chain K\\*=2 vs retrain-chain K\\*≥4：是否测量了本质不同的现象？如何调和？\n\n---\n\n## Missing References\n\n1. **Wang, Li, Yan, Cheng, Zhang (ACL 2025)**: \"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing\" — prompt-chain attractor cycles 与 K\\* 收敛机制直接相关。[Consensus]\n2. **Fu, Wang, Chen, Tian, Tao (ICLR 2025)**: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" — 自消费循环中 collapse 的理论条件，K\\* 存在的理论背景。[Consensus]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时约 4 分钟）。主要发现：\n\n- **[Critical]** Table 21（p.18）数据全部为 em-dash，与两位 Reviewer 发现一致\n- **[Warning]** p.1-2 连续纯文本无 display item，Figure 1 直到 p.3 才出现——在容忍范围内但影响第一印象\n- **[Warning]** p.4 单页 3 个 figure（Figure 2/3/4），视觉密度过高，Figure 3/4 尺寸被压缩\n- **[Warning]** Figure 4 热图使用红绿配色，对红绿色盲不友好，建议改用 Blue-Orange 或 viridis\n- **[Warning]** p.12-13, p.15 大面积空白（Table 10/11/13 布局松散）\n- **[Info]** 正文 8 页含 4 figures + 4-5 tables = 8-9 个 display items，密度适中\n- **[Info]** Figure 5 x 轴标签 150 DPI 下勉强可读\n- **[Info]** 参考文献格式统一，无 [?] 未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Reproducibility | 2/5 | 4/5 | 3/5 |\n| Overall | 3.0 | 3.5 | **3.0** |\n\n本文提出了新颖且有意义的 generational depth estimation 概念，K\\* 作为递归合成文本可区分深度的操作性度量填补了 binary detection 与 model collapse macro dynamics 之间的真实空白。统计方法论严谨，\"one-wash laundering\" 发现有实践价值。\n\n当前版本未达 Conference 标准的核心原因：\n\n1. **投稿完整性红线**：至少 5-6 个附录表为空占位符，包括支撑 scorer independence 核心声明的 ANOVA 表。空表格 + 已有结论 = 不可验证的声明。\n2. **核心声明被自身数据部分证伪**：唯一完成 cross-scoring 的 continuation 配置（Qwen-cont）显示 K\\*=2 是 scorer-dependent 的（Table 22 Agreement=×），与 \"K\\* governed by generation process\" 矛盾。\n3. **实用价值存疑**：K\\*-aware filtering 仅在 100% 合成（非现实场景）下有显著效果；dose-response 在 <50% 污染下所有策略收敛（p > 0.12）。\n4. **统计表述夸大**：\"6/10 configurations yield K\\*=2\" 按家族去重后变为 \"3/6 families (+1 split)\"；K\\*\\_empirical 被 frame 为 \"the discrimination boundary\" 而非 feature-specific lower bound。\n\n**修复路径**：填充附录数据（如确为排版遗漏则容易修复）→ 修正 scorer independence 叙事（区分 robust vs marginal K\\*=2）→ 校准 filtering utility 定位（consistency check, 非独立贡献）→ 同时报告 per-family 和 per-configuration K\\* 统计 → 补充 Wang/Fu 引用。完成后论文有望达到 3.5（Borderline Conference）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Model collapse 作为动机但实验几乎全是 prompt-chain，应更早更明确区分两者\n- Contribution list 的 filtering validation 应降级为 consistency check\n- 应提及 retrain-chain K\\*≥4 形成完整图景\n\n### Section 2 (Related Work)\n- 缺 Wang et al. (ACL 2025) attractor cycles 和 Fu et al. (ICLR 2025) collapse theory\n- 与 Geng et al. Markov convergence 的 K\\* 增量贡献区分仍可更清晰\n\n### Section 3 (Method)\n- DPI→AUC 桥接不完整，应明确为 heuristic motivation\n- K\\*\\_empirical Eq.1 中 max 算子隐含单调假设，应明确或修改定义\n- θ=0.60 三条证据中第三条应标为 post-hoc confirmatory\n\n### Section 4 (Experiments)\n- Table 1 应列出全部 10 配置\n- Cross-scorer 结果（Table 22）直接削弱 scorer independence 声明，Discussion 措辞需修正\n- 按家族去重后 K\\*=2 比例显著降低，应双重报告\n\n### Section 5 (Filtering)\n- 应重新定位为 consistency check\n- 正文需至少一句 dose-response summary（<50% 污染下策略收敛）\n- 仅在 Qwen-1.5B continuation 验证，缺 generator 多样性\n\n### Section 6 (Discussion)\n- Scorer independence 段落使用 feature ranking ρ 替代 K\\* agreement，应修正\n- \"one-wash laundering\" 术语需首次使用说明或改名\n- 缺少对 per-family K\\* 分布的讨论\n\n### Section 7 (Conclusion)\n- 过于简短（3-4 句），应扩展加入实践建议和主要局限\n\n### Abstract\n- 至少加 \"lower bound\" 限定语\n- 考虑精简部分定量细节\n\n### Limitations\n- 内容诚实详尽，是论文优点\n\n### Appendix\n- 5-6 个空表为最严重的投稿质量问题\n- Figure 4 配色应改为色盲友好\n- p.12-15 布局可优化（减少空白）",
  "project": "gen-depth-contamination",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — gen-depth-contamination\n## Round 24 (Fresh Review, 2026-05-22)\n## Venue: EMNLP 2026 (ARR May 2026) | Deadline: 2026-05-25\n\n---\n\n## Summary\n\n本文提出 generational depth estimation，测量递归合成文本的可区分深度边界 K\\*\\_empirical——使用 15 个统计特征 + OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族, 1B-8B）、3 个文本域、4 种解码策略上实验，发现 K\\*\\_empirical ∈ {1,2,3}，一般 web 文本以 K\\*=2 为主导模式（6/10 配置），arXiv 学术文本 K\\*=3。论文验证了跨模型迁移能力（80-100% 精度保持）和 K\\*-aware 数据过滤的下游效用。\n\n---\n\n## Strengths\n\n**S1. 新颖的问题形式化。** Generational depth estimation 填补了 binary detection（人 vs. 机器）与 model collapse 宏观动力学之间的真实空白。K\\* 概念定义清晰、可操作（Eq.1: max{k ≥ 1 : AUC\\_{k-1,k} > θ}），是对现有文献的有意义扩展。\n\n**S2. 统计方法论严谨度高于同类工作。** Bootstrap 95% CI（1,000 resamples）、permutation test（p ≤ 0.002）、Cohen's h 效应量（h ≈ 0.20）、5-fold GroupKFold 交叉验证（按 seed document 分组防泄漏）——这套统计体系在 NLP 实证论文中不常见。\n\n**S3. \"One-wash laundering\" 洞察有实践价值。** K\\*=2 意味着一次生成就足以让 web 文本与更深层合成内容不可区分，对数据策展有直接指导意义：对 web text 而言，超越 binary 过滤的更精细深度策略是不必要的。\n\n**S4. 跨模型迁移设计精巧。** Cross-scorer validation 和 scorer-invariant feature ranking（ρ > 0.90）共同提供了有部署价值的方法论贡献。Continuation-mode 分类器在 Pythia↔OLMo 间保持 90-92% 迁移准确率。\n\n**S5. Limitations 诚实详尽。** 7 条主要局限 + Extended Appendix（retrain-chain, dose-response），主动暴露了 threshold sensitivity、feature-set dependence、marginal boundary cases。\n\n**S6. 模型覆盖面在 ≤8B 范围内合理。** 6 个架构族、rewrite + continuation 两种模式、4 种解码策略、3 个文本域——消融设计系统全面。\n\n---\n\n## Weaknesses\n\n### Critical — Must-Fix\n\n**W1 [Critical, Consensus]** 附录至少 5-6 个数据表为空占位符\n\n两位 Reviewer 独立发现至少 5 个附录表数据完全缺失：\n- Table 21 / S12（跨域 pairwise AUC）：21 个数据单元格全为 em-dash\n- Table 24（Three-way ANOVA: Generator × Scorer × Depth-Pair）：F/p/η²\\_p 全部为 `---`，但标题声称 \"non-significant Scorer main effect confirms scorer independence\"\n- Table S10（Pythia 解码消融）：30 个 AUC 值全空\n- Table S11（长度消融）：15 个 AUC 值全空（仅 K\\* 行有值）\n- Table S13（Scorer sensitivity）：5/7 generator 的 cross-scorer K\\* 为 `---`\n\n这构成系统性投稿质量问题。ANOVA 空表尤其严重——scorer independence 是论文 cross-model transfer 核心支柱，表标题直接下了结论但无任何数据支撑。主文 Section 4.5 引用了具体数值（如 \"Wikipedia yields K\\*=2, AUC: 0.623\"），但完整逐深度对数据缺失。\n\n**W2 [Critical, Consensus]** Cross-scorer 验证部分证伪了 scorer independence claim\n\nQwen-continuation 自身打分 K\\*=2（1v2 AUC = 0.611, CI lower = 0.602, 仅超过 θ 约 0.002），但 Pythia 打分 AUC = 0.5923 < θ，OLMo 打分 AUC = 0.5858 < θ，K\\* 均降为 1（Table 22, Agreement=×）。Discussion 仍写 \"Cross-scorer validation confirms K\\*\\_empirical is governed by the generation process rather than the scoring model\"，用 feature ranking ρ 替代 K\\* agreement 是 misleading——feature ranking 一致不等于 K\\* 判定一致。仅 Qwen-rewrite（信号最强配置, 1v2 AUC = 0.696）在 cross-scorer 下保持 K\\*=2。\n\n### Major — Should-Fix\n\n**W3 [Critical-Major, Divergence]** K\\*\\_empirical framing: \"the discrimination boundary\" vs \"feature-specific lower bound\"\n\n- **R2 (Critical)**：Title/Abstract/Introduction 将 K\\*\\_empirical 定位为 \"the discrimination boundary\"，但 Limitation 5 承认它是 \"feature-set-specific lower bound\"，neural probe K\\*\\_neural∈{1,2,3} 随模型变化。正文与 Limitations 之间存在系统性 overclaiming。\n- **R1 (Warning)**：Section 3.1 Eq.1 前已写 \"We define the operational lower bound\"，K\\*\\_empirical 同时是 empirical boundary 和 K\\*\\_theory 的 lower bound，两层含义不矛盾。是措辞精度问题，未达 systematic overclaiming。\n- **共识方向**：至少 Abstract 和 Introduction 应引入 \"lower bound\" 限定语（如 \"a lower bound on the discrimination boundary\"）。\n\n**W4 [Major, Consensus]** Filtering 在现实污染比例下实用价值消失\n\nAppendix D.8 dose-response 分析：10% 污染所有策略无差异（Δ\\_max = 0.03pp, p > 0.8）；30% 不显著（p > 0.3）；50% 不显著（p = 0.12）。仅 100%（非现实场景）下有显著效果（0.77pp 改善）。主文 Section 5 仅报告 100% 设定，将 filtering 作为 contribution 呈现。应重新定位为 consistency check，在正文中提及 dose-response convergence。\n\n**W5 [Major, Consensus]** Qwen 家族过度代表\n\n4/10 配置来自 Qwen（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），全部 K\\*=2。按家族去重：K\\*=2 确认 3 个家族（Qwen, LLaMA, Pythia-1.4B），K\\*=1 确认 3 个家族（OLMo, Mistral, Gemma），Pythia 分裂（1.4B=2, 6.9B=1）。\"6/10 configurations yield K\\*=2\" 变为 \"3/6 families (+1 split)\"。应同时报告 per-family 和 per-configuration 统计。\n\n**W6 [Major, Consensus]** 缺少 >8B 模型，scale trend 可能使结论失效\n\n0v1 JSD 随模型规模降低（0.15-0.27 at ≤1.5B vs. 0.077 at 8B LLaMA-3.1）。论文推测 \"models at 13B+ may increasingly yield K\\*=1\"。若属实，K\\*=2 仅适用于中小模型，前沿模型可能都是 K\\*=1，缩小实践相关性。应在 Abstract/Conclusion 明确标注 ≤8B 适用范围。\n\n**W7 [Major, Divergence]** arXiv K\\*=3 证据基础\n\n- **R2 (Major)**：仅 2 个模型, n=2200，但作为平行贡献呈现。\n- **R1 (Rebut)**：Table 4 full 实际覆盖 5 模型/4 家族（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B），R2 仅看到 Abstract 的 \"two architectures\"。\n- **共识**：模型覆盖面超出 R2 初判，但 n=2,200 样本量较小，对应的完整 pairwise AUC 支撑表（Table S12/21）为空。\n\n**W8 [Major, Consensus]** 缺少重要相关工作\n\n- Wang, Li, Yan, Cheng, Zhang (ACL 2025) \"Unveiling Attractor Cycles in LLMs\" — prompt-chain attractor cycles 与 K\\* 直接相关\n- Fu, Wang, Chen, Tian, Tao (ICLR 2025) \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" — collapse 理论条件，K\\* 存在的理论背景\n\n### Warning\n\n**W9 [Warning, Consensus]** DPI→AUC 理论桥接不完整。DPI 保证 I(X; Y\\_k) 单调递减，但论文应用于 AUC\\_{k-1,k}（相邻代际 pairwise 分类精度），两者不等价。应明确 DPI 是 heuristic motivation 而非 strict proof。\n\n**W10 [Warning, Partial Consensus]** θ=0.60 阈值事后选择风险。Cohen's h = 0.20 提供先验理论基础（两位共识），但论文三条\"独立\"证据中第三条（distributional discontinuity）是 data-driven（R1 指出），应标为 post-hoc confirmatory。\n\n**W11 [Warning, Consensus]** Filtering 仅在单一 generator（Qwen-1.5B continuation）上验证，应至少在 K\\*=1 generator 上重复。\n\n### Minor\n\n**W12** [Minor, Consensus] Conclusion 过于简短（3-4 句），应扩展至 5-7 句，加实践建议和局限总结。\n\n**W13** [Minor, Consensus] K\\* 符号变体过多（K\\*\\_empirical, K\\*\\_theory, K\\*\\_neural），K\\*\\_theory 仅作占位符。\n\n**W14** [Minor, Divergence] Abstract 信息密度（R2 认为过高，R1 认为正常）。\n\n**W15** [Minor, Consensus] Table 1 仅列 6 配置但声称 10，应添加脚注或列出全部。\n\n**W16** [Minor] \"one-wash laundering\" 术语可能混淆（K\\*=2 ≠ one-wash 直觉），建议首次使用加说明。\n\n**W17** [Minor] Figure 3/5 x 轴标签可读性差；Table 4 脚注过密。\n\n**W18** [Minor] 引用格式不一致（39 条中 8 条缺 URL）。\n\n**W19** [Minor, Consensus] K\\*\\_empirical 定义中 max 算子隐含 AUC 单调递减假设，应明确该假设或改用 \"连续满足条件的最大 k\"。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 达成共识的关键问题：\n1. **[AGREE]** 附录 5-6 个空表构成系统性投稿质量问题（Critical）\n2. **[AGREE]** Cross-scorer 验证部分证伪 scorer independence claim（Critical-Major）\n3. **[AGREE]** Filtering 在 <50% 污染下无显著效果，应重新定位为 consistency check（Major）\n4. **[AGREE]** Qwen 过度代表导致 \"6/10\" 统计夸大（Major）\n5. **[AGREE]** 缺少 >8B 模型限制实践相关性（Major）\n6. **[AGREE]** DPI→AUC 理论桥接不完整（Warning）\n7. **[AGREE]** 缺少 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025) 引用（Major）\n\n## Reviewer Divergence\n\n1. **K\\*\\_empirical overclaiming** (W3)：R1 认为措辞精度问题（Warning），R2 认为系统性 overclaiming（Critical）。共识方向：至少 Abstract/Introduction 需加 \"lower bound\" 限定。\n2. **arXiv 证据基础** (W7)：R1 指出实际 5 模型/4 家族（非 R2 认为的 2 模型），但 n=2,200 样本量和空支撑表关注仍成立。\n3. **Abstract 信息密度** (W14)：R1 认为正常，R2 认为过高。\n4. **Kirchenbauer watermarking 引用**：R1 建议添加，R2 rebut 认为不同问题域（不纳入 Missing References）。\n\n---\n\n## Questions\n\n**Q1.** 附录 5-6 个空表（Tables S10/S11/S12/S13, Table 21, Table 24）是排版遗漏还是实验未完成？如果数据存在，请提供完整数值。\n\n**Q2.** Qwen-continuation 的 K\\*=2 在 cross-scorer 下降为 1（Table 22），如何调和 \"K\\* is governed by the generation process\" 的声明？能否扩展 Table 22 覆盖更多 generator-scorer 组合？\n\n**Q3.** 现实 web-scale 合成内容比例估计为多少？在 10-30% 污染下，K\\*-aware curation 的实际增益是什么？\n\n**Q4.** 13B+ 模型若 K\\*=1，K\\*=2 核心发现是否仅限于正在被淘汰的模型规模窗口？\n\n**Q5.** K\\*\\_empirical 定义中 max 算子是否隐含 AUC 单调递减假设？是否应改为 \"连续满足条件的最大 k\"？\n\n**Q6.** Prompt-chain K\\*=2 vs retrain-chain K\\*≥4：是否测量了本质不同的现象？如何调和？\n\n---\n\n## Missing References\n\n1. **Wang, Li, Yan, Cheng, Zhang (ACL 2025)**: \"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing\" — prompt-chain attractor cycles 与 K\\* 收敛机制直接相关。[Consensus]\n2. **Fu, Wang, Chen, Tian, Tao (ICLR 2025)**: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\" — 自消费循环中 collapse 的理论条件，K\\* 存在的理论背景。[Consensus]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时约 4 分钟）。主要发现：\n\n- **[Critical]** Table 21（p.18）数据全部为 em-dash，与两位 Reviewer 发现一致\n- **[Warning]** p.1-2 连续纯文本无 display item，Figure 1 直到 p.3 才出现——在容忍范围内但影响第一印象\n- **[Warning]** p.4 单页 3 个 figure（Figure 2/3/4），视觉密度过高，Figure 3/4 尺寸被压缩\n- **[Warning]** Figure 4 热图使用红绿配色，对红绿色盲不友好，建议改用 Blue-Orange 或 viridis\n- **[Warning]** p.12-13, p.15 大面积空白（Table 10/11/13 布局松散）\n- **[Info]** 正文 8 页含 4 figures + 4-5 tables = 8-9 个 display items，密度适中\n- **[Info]** Figure 5 x 轴标签 150 DPI 下勉强可读\n- **[Info]** 参考文献格式统一，无 [?] 未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Reproducibility | 2/5 | 4/5 | 3/5 |\n| Overall | 3.0 | 3.5 | **3.0** |\n\n本文提出了新颖且有意义的 generational depth estimation 概念，K\\* 作为递归合成文本可区分深度的操作性度量填补了 binary detection 与 model collapse macro dynamics 之间的真实空白。统计方法论严谨，\"one-wash laundering\" 发现有实践价值。\n\n当前版本未达 Conference 标准的核心原因：\n\n1. **投稿完整性红线**：至少 5-6 个附录表为空占位符，包括支撑 scorer independence 核心声明的 ANOVA 表。空表格 + 已有结论 = 不可验证的声明。\n2. **核心声明被自身数据部分证伪**：唯一完成 cross-scoring 的 continuation 配置（Qwen-cont）显示 K\\*=2 是 scorer-dependent 的（Table 22 Agreement=×），与 \"K\\* governed by generation process\" 矛盾。\n3. **实用价值存疑**：K\\*-aware filtering 仅在 100% 合成（非现实场景）下有显著效果；dose-response 在 <50% 污染下所有策略收敛（p > 0.12）。\n4. **统计表述夸大**：\"6/10 configurations yield K\\*=2\" 按家族去重后变为 \"3/6 families (+1 split)\"；K\\*\\_empirical 被 frame 为 \"the discrimination boundary\" 而非 feature-specific lower bound。\n\n**修复路径**：填充附录数据（如确为排版遗漏则容易修复）→ 修正 scorer independence 叙事（区分 robust vs marginal K\\*=2）→ 校准 filtering utility 定位（consistency check, 非独立贡献）→ 同时报告 per-family 和 per-configuration K\\* 统计 → 补充 Wang/Fu 引用。完成后论文有望达到 3.5（Borderline Conference）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Model collapse 作为动机但实验几乎全是 prompt-chain，应更早更明确区分两者\n- Contribution list 的 filtering validation 应降级为 consistency check\n- 应提及 retrain-chain K\\*≥4 形成完整图景\n\n### Section 2 (Related Work)\n- 缺 Wang et al. (ACL 2025) attractor cycles 和 Fu et al. (ICLR 2025) collapse theory\n- 与 Geng et al. Markov convergence 的 K\\* 增量贡献区分仍可更清晰\n\n### Section 3 (Method)\n- DPI→AUC 桥接不完整，应明确为 heuristic motivation\n- K\\*\\_empirical Eq.1 中 max 算子隐含单调假设，应明确或修改定义\n- θ=0.60 三条证据中第三条应标为 post-hoc confirmatory\n\n### Section 4 (Experiments)\n- Table 1 应列出全部 10 配置\n- Cross-scorer 结果（Table 22）直接削弱 scorer independence 声明，Discussion 措辞需修正\n- 按家族去重后 K\\*=2 比例显著降低，应双重报告\n\n### Section 5 (Filtering)\n- 应重新定位为 consistency check\n- 正文需至少一句 dose-response summary（<50% 污染下策略收敛）\n- 仅在 Qwen-1.5B continuation 验证，缺 generator 多样性\n\n### Section 6 (Discussion)\n- Scorer independence 段落使用 feature ranking ρ 替代 K\\* agreement，应修正\n- \"one-wash laundering\" 术语需首次使用说明或改名\n- 缺少对 per-family K\\* 分布的讨论\n\n### Section 7 (Conclusion)\n- 过于简短（3-4 句），应扩展加入实践建议和主要局限\n\n### Abstract\n- 至少加 \"lower bound\" 限定语\n- 考虑精简部分定量细节\n\n### Limitations\n- 内容诚实详尽，是论文优点\n\n### Appendix\n- 5-6 个空表为最严重的投稿质量问题\n- Figure 4 配色应改为色盲友好\n- p.12-15 布局可优化（减少空白）",
    "project": "gen-depth-contamination",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
  }
}
```

</details>

---


### Tool result

_source line 2297 · 2026-05-22T05:49:27.384467+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d2a0ec1de3a456564133278c1a9b203:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4320
}
```

</details>

---


### Assistant

_source line 2298 · 2026-05-22T05:49:40.179914+00:00_

审稿报告已投递至 Research Director。

---

**Round 24 审稿完成**

- **Overall: 3.0 (Findings)**
- **Reviewer 1**: 3.0 | **Reviewer 2**: 3.5 → 交叉后共识方向 3.0
- **2 Critical**：附录 5-6 个空表（系统性投稿质量问题）+ cross-scorer 部分证伪 scorer independence
- **6 Major**：K\* framing overclaim、filtering 现实无效、Qwen 过度代表、缺 >8B 模型、缺 2 篇引用、arXiv 支撑表缺失
- **修复路径明确**：空表若为排版遗漏则容易修复 → 修正 scorer independence 叙事 → 校准 filtering 定位 → 补引用 → 有望 3.5

Issue tracker 已同步更新至 `review_issues.yaml`（Round 24, 24 个 issue，其中 6 critical, 8 warning, 10 minor/resolved）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 175

## Round 175

2 recorded events


### User

_source line 2299 · 2026-05-22T05:49:42.817160+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。

核心结论：R1 的 12 个具体问题中，我 **[AGREE] 10 条、[REBUT] 2 条**：

- **REBUT θ=0.60 post-hoc 风险（W3）**：前两条证据（Cohen's h = 0.20）是先验的，且 Figure 3 sensitivity analysis 表明 K*=2 在 θ∈[0.55, 0.65] 范围内稳定
- **REBUT Kirchenbauer watermarking 为 missing reference**：watermarking 需要生成时主动干预，与 post-hoc depth estimation 正交

两位 reviewer 的关键共识：附录数据系统性缺失（≥6 个空表）、cross-scorer 部分证伪 scorer independence、filtering 在现实比例下无效益、Qwen 过度代表导致统计夸大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2300 · 2026-05-22T05:49:58.789203+00:00_

审稿圆桌会议已完成。

**Round 24 审稿报告已投递至 Research Director。**

---

**最终结论：Overall 3.0 (Findings)**

两位 Reviewer 完成独立初审 + 交叉回应，关键共识：

| 严重程度 | 问题 | 共识 |
|---------|------|------|
| Critical | 附录 ≥5 个表为空占位符（ANOVA、域消融、Pythia 解码等） | 一致 |
| Critical | Cross-scorer 验证部分证伪 scorer independence（Qwen-cont K\*=2→1） | 一致 |
| Major | Filtering 在 <50% 污染下无显著效果 | 一致 |
| Major | Qwen 过度代表：按家族去重 K\*=2 从 6/10 降为 3/6 | 一致 |
| Major | 缺少 >8B 模型 + scale trend 威胁 | 一致 |
| Major | 缺 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025) | 一致 |
| 分歧 | K\*\_empirical overclaiming（R2: Critical, R1: Warning） | 共识方向：Abstract 需加 lower bound 限定 |

**修复路径**：填充空表 → 修正 scorer independence 叙事 → 校准 filtering 定位为 consistency check → 双重报告 per-family/per-configuration 统计 → 补充引用。完成后有望 3.5。

Issue tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 176

## Round 176

68 recorded events


### User

_source line 2301 · 2026-05-22T07:13:17.316141+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-contamination
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2302 · 2026-05-22T07:13:24.378955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-22T07:13:24.430218+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2304 · 2026-05-22T07:13:31.260987+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2305 · 2026-05-22T07:13:31.261402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2306 · 2026-05-22T07:13:34.591312+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2307 · 2026-05-22T07:13:34.742283+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2308 · 2026-05-22T07:13:41.005648+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2309 · 2026-05-22T07:13:41.156595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2310 · 2026-05-22T07:13:46.478579+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2311 · 2026-05-22T07:13:47.332506+00:00_

{"result":"# 项目 gen-depth-contamination 概况\n\n## 实验状态 (156 个)\n\n- **exp_016_base_vs_instruct**: DONE (success) — \n- **exp_003_decoding_ablation**: DONE (success) — \n- **exp_004_7b_crossscale**: DONE (success) — \n- **exp_E_paired_stats**: DONE (success) — \n- **exp_D_obd_n500**: DONE (success) — \n- **exp_B_14d_ablation**: DONE (success) — \n- **exp_A_alt_scorer**: DONE (success) — \n- **exp_015_neural_probe**: DONE (success) — \n- **exp_006_graduated_filtering**: DONE (success) — \n- **exp_007_bootstrap_ci**: DONE (success) — \n- **exp_011_llm_zeroshot**: DONE (success) — \n- **exp_013_cross_transfer**: DONE (success) — \n- **exp_010_ordinal_baseline**: DONE (success) — \n- **exp_001_pythia_depth**: DONE (success) — \n- **mvp_pilot_sat_v1**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 7b-cross-transfer（准备中）\n- arxiv_multi_source（准备中）\n- sweep_r10_nofilter（准备中）\n- sweep_r10_binary（准备中）\n- sweep_r10_graduated（准备中）\n- sweep_r30_nofilter（准备中）\n- sweep_eval_r10_nofilter（准备中）\n- sweep_eval_r10_binary（准备中）\n- sweep_eval_r10_graduated（准备中）\n- sweep_eval_r30_nofilter（准备中）\n- …另有 27 项\n\n## 近期结论\n- **seed_qwen15b_c4_s123** (success): Qwen-1.5B C4 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n- **seed_qwen15b_wiki_s123** (negative): Qwen-1.5B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n- **seed_pythia14b_wiki_s123** (success): Pythia-1.4B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n\n## 趋势\n成功 90 / 负向 16 / 失败 13 / 共 119\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-22115: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nwestd-42896: 无 GPU 信息\n\n## 告警\n- exp-008-retrain-chain: 训练失败 — unknown\n- exp_009_dose_10pct: 训练失败 — unknown\n- exp_009_dose_30pct: 训练失败 — unknown\n- exp_009_dose_50pct: 训练失败 — unknown\n- exp_009_dose_10pct_v2: 训练失败 — unknown\n- exp_009_dose_30pct_v2: 训练失败 — unknown\n- exp_009_dose_50pct_v2: 训练
…[truncated 279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 2312 · 2026-05-22T07:13:47.383195+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2313 · 2026-05-22T07:13:49.240952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2314 · 2026-05-22T07:13:50.195114+00:00_

1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure a lower bound on the generational discrimination boundary, $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable), using 15 statistical features and an OBD-LightGBM classifier.
36	Across 10 model configurations (6 architecture families, 1B--8B), 3 source domains, and 4 decoding strategies, $\Kempirical \in \{1, 2, 3\}$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$): general web text yields $\Kempirical{=}2$ in 6/10 configurations (2 of 6 families unanimously, plus a scale-dependent split in Pythia), while structured academic text (arXiv) yields $\Kempirical{=}3$, validated across two architectures.
37	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect (first-generation text is detectable, but second-generation and beyond are not).
38	Model-free statistical features enable 80--100\% cross-model transfer with scorer-in
…[truncated 4243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2315 · 2026-05-22T07:13:50.346210+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_25/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_25/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2316 · 2026-05-22T07:13:50.499350+00:00_

-rw-r--r-- 1 ubuntu ubuntu 535789 May 22 07:12 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_25/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool result

_source line 2317 · 2026-05-22T07:13:55.971849+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"The 6th International Conference on Natural Language Processing for the Digital Humanities | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-international-conference-natural-language-processing-digital-humanities"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Seventh Workshop on NLP and Computational Social Science (at ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/seventh-workshop-nlp-and-computational-social-science-acl-2026"}]

Based on the search results, here's information about ACL Rolling Review (ARR) 2026 and ACL 2026 submission guidelines:

## ACL 2026 Main Conference Submission Guidelines

ACL 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. Both submissions of articles for review and commitment of reviewed articles to the conference will be performed via the OpenReview platform.

### Key Deadlines
- Submission deadline (all papers are submitted to ARR): January 5, 2026
- Afte
…[truncated 1252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 8588
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-22T07:14:02.064663+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines page limit ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines page limit ARR"
  }
}
```

</details>

---


### Tool call

_source line 2319 · 2026-05-22T07:14:03.448283+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 deadline submission requirements aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 deadline submission requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 2320 · 2026-05-22T07:14:03.448770+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2321 · 2026-05-22T07:14:09.122649+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines page limit ARR"

Links: [{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here are the key details about EMNLP 2026 call for papers submission guidelines:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. The mandatory Limitations section is required, placed after the conclusion.

## ARR Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## Important Note About Venue Selec
…[truncated 848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7057
}
```

</details>

---


### Tool result

_source line 2322 · 2026-05-22T07:14:11.080714+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 deadline submission requirements aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results from aclrollingreview.org, here are the key submission requirements and information for ACL Rolling Review (ARR) May 2026:

## Submission Requirements

Papers must not include authors' names and affiliations, and self-references that reveal authors' identities must be avoided. Supplementary materials should be anonymized, and links to file hosting services like Dropbox that can track downloads are not allowed.

Start
…[truncated 958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7632
}
```

</details>

---


### Tool result

_source line 2323 · 2026-05-22T07:14:11.634459+00:00_

{"result":"# 项目 gen-depth-contamination 概况\n\n## 实验状态 (156 个)\n\n- **exp_016_base_vs_instruct**: DONE (success) — \n- **exp_003_decoding_ablation**: DONE (success) — \n- **exp_004_7b_crossscale**: DONE (success) — \n- **exp_E_paired_stats**: DONE (success) — \n- **exp_D_obd_n500**: DONE (success) — \n- **exp_B_14d_ablation**: DONE (success) — \n- **exp_A_alt_scorer**: DONE (success) — \n- **exp_015_neural_probe**: DONE (success) — \n- **exp_006_graduated_filtering**: DONE (success) — \n- **exp_007_bootstrap_ci**: DONE (success) — \n- **exp_011_llm_zeroshot**: DONE (success) — \n- **exp_013_cross_transfer**: DONE (success) — \n- **exp_010_ordinal_baseline**: DONE (success) — \n- **exp_001_pythia_depth**: DONE (success) — \n- **mvp_pilot_sat_v1**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 7b-cross-transfer（准备中）\n- arxiv_multi_source（准备中）\n- sweep_r10_nofilter（准备中）\n- sweep_r10_binary（准备中）\n- sweep_r10_graduated（准备中）\n- sweep_r30_nofilter（准备中）\n- sweep_eval_r10_nofilter（准备中）\n- sweep_eval_r10_binary（准备中）\n- sweep_eval_r10_graduated（准备中）\n- sweep_eval_r30_nofilter（准备中）\n- …另有 27 项\n\n## 近期结论\n- **seed_qwen15b_c4_s123** (success): Qwen-1.5B C4 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n- **seed_qwen15b_wiki_s123** (negative): Qwen-1.5B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n- **seed_pythia14b_wiki_s123** (success): Pythia-1.4B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n\n## 趋势\n成功 90 / 负向 16 / 失败 13 / 共 119\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-22115: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nwestd-42896: 无 GPU 信息\n\n## 告警\n- exp-008-retrain-chain: 训练失败 — unknown\n- exp_009_dose_10pct: 训练失败 — unknown\n- exp_009_dose_30pct: 训练失败 — unknown\n- exp_009_dose_50pct: 训练失败 — unknown\n- exp_009_dose_10pct_v2: 训练失败 — unknown\n- exp_009_dose_30pct_v2: 训练失败 — unknown\n- exp_009_dose_50pct_v2: 训练
…[truncated 279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 8185
}
```

</details>

---


### Tool call

_source line 2324 · 2026-05-22T07:14:16.553505+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2325 · 2026-05-22T07:14:16.554112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2326 · 2026-05-22T07:14:22.830512+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2327 · 2026-05-22T07:14:22.831034+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2328 · 2026-05-22T07:14:27.197625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2329 · 2026-05-22T07:14:27.649930+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistica
…[truncated 1720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2330 · 2026-05-22T07:14:27.650336+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2331 · 2026-05-22T07:14:27.750992+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.
6	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
8	
9	\paragraph{Beyond binary detection.}
10	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
11	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
12	None estimates recursive generation depth.
13	
14	\paragraph{Data selection and curation.}
15	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
16	
17	\paragraph{Ordinal classification and probing.}
18	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
19
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2332 · 2026-05-22T07:14:28.052557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2333 · 2026-05-22T07:14:29.006799+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
17	Together with Markov chain convergence, this provides heuristic motivation for expecting $\auc_{k-1,k}$ to decrease with $k$, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\!\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, j \!\leq\! k\bigr\},
22	  \label{eq:kstar}
23	\end{equation}
24	which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested configurations; Table~\ref{tab:kstar_ci}).
25	The theoretical upper bound $\Ktheory$ (the true maximum discriminable depth given optimal features) is not directly estimated in this work; $\Kempirical$ provides a feature-set-specific lower bound on $\Ktheory$.
26	Here $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a small-effect-size threshold (Cohen's $h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin
…[truncated 4910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2334 · 2026-05-22T07:14:29.057404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---


### Tool result

_source line 2335 · 2026-05-22T07:14:29.108352+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on ten model configurations spanning six architecture families:
5	Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5024 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .4942 & 
…[truncated 9945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2336 · 2026-05-22T07:14:29.811646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
  }
}
```

</details>

---


### Tool result

_source line 2337 · 2026-05-22T07:14:29.912513+00:00_

1	\section{Consistency Check: $\Kstar$-Guided Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We test this as a consistency check on the boundary measurement, not as an independent contribution.
6	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
7	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
13	\label{tab:tab_filtering_main}
14	\input{tables/tab_filtering_main}
15	\end{table}
16	
17	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
18	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
19	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduat
…[truncated 794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2338 · 2026-05-22T07:14:29.913202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2339 · 2026-05-22T07:14:30.415533+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
13	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
14	
15	\paragraph{Graduated filtering failure.}
16	For web text, 2v3 $\auc < \theta$ across all model configurations, so depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise, explaining convergence toward binary at high $\alpha$ (Appendix~\ref{sec:extended_limitations}).
17	DSIR fails differently: bigram hashing captures domain shift but not depth-correlated signatures.
18	
19	\paragraph{Representation dependence.}
20	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
21	The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
22	Feature rankings are scorer-independent ($\rho > 0.90$); $\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (
…[truncated 3047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2340 · 2026-05-22T07:14:30.466168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2341 · 2026-05-22T07:14:31.219492+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure a lower bound on the generational depth discrimination boundary $\Kempirical$ for recursive synthetic text.
5	$\Kempirical \in \{1, 2, 3\}$ depends on source domain and model characteristics: general web text yields $\Kempirical{=}2$ in 6/10 configurations (2/6 families unanimously, with a scale-dependent split in Pythia; 1B--8B; $p \leq 0.002$), with $\Kempirical{=}3$ for structured academic text.
6	This one-wash laundering effect means that a single generation pass renders web text indistinguishable from deeper recursive content, limiting depth-aware curation to a binary boundary.
7	For practitioners, binary filtering (depth 0 vs.\ $\geq$1) captures the only reliable discrimination signal; graduated weighting beyond $\Kempirical$ adds noise.
8	$\Kempirical$ is feature-set dependent (15D provides a conservative lower bound; neural probes extend it by one level for some architectures) and established for 1B--8B models; scaling beyond 8B, additional structured domains, and retrain-chain $\Kstar$ remain open.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 2342 · 2026-05-22T07:14:31.219943+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2343 · 2026-05-22T07:14:31.270459+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2344 · 2026-05-22T07:14:37.012014+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2345 · 2026-05-22T07:14:37.514224+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/agent/’: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2346 · 2026-05-22T07:14:37.665235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2347 · 2026-05-22T07:14:37.665607+00:00_

1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	%% [Merged into Figure 2] \begin{figure}[t]
12	%% [Merged into Figure 2]   \centering
13	%% [Merged into Figure 2]   \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	%% [Merged into Figure 2]   \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	%% [Merged into Figure 2]   \label{fig:s1_auc_decay_ci}
16	%% [Merged into Figure 2] \end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
33	3 & \textbf{\texttt{surp\_std}} & \textbf{\t
…[truncated 981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2348 · 2026-05-22T07:14:42.082429+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/ -path \"*/gen-depth-contamination*config*\" -name \"*.yaml\" -o -path \"*/gen-depth-contamination*config*\" -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Find project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/ -path \"*/gen-depth-contamination*config*\" -name \"*.yaml\" -o -path \"*/gen-depth-contamination*config*\" -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Find project config"
  }
}
```

</details>

---


### Tool result

_source line 2349 · 2026-05-22T07:14:42.585647+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2350 · 2026-05-22T07:14:42.786951+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/ -name \"projects.yaml\" -o -name \"project_config.yaml\" 2>/dev/null | head -5",
  "description": "Find global project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/ -name \"projects.yaml\" -o -name \"project_config.yaml\" 2>/dev/null | head -5",
    "description": "Find global project config"
  }
}
```

</details>

---


### Tool result

_source line 2351 · 2026-05-22T07:14:42.887753+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2352 · 2026-05-22T07:14:45.900410+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/ -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
  "description": "Find yaml config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/ -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -20",
    "description": "Find yaml config files"
  }
}
```

</details>

---


### Tool result

_source line 2353 · 2026-05-22T07:14:46.001262+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/projects/gen-depth-contamination.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/pending_approval_notifications.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2354 · 2026-05-22T07:14:48.918249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/projects/gen-depth-contamination.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/projects/gen-depth-contamination.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2355 · 2026-05-22T07:14:49.320184+00:00_

1	execution:
2	  account: root
3	  gpu_constraint: blackwell-98gb
4	  gpu_ids:
5	  - cuda:0
6	  - cuda:1
7	  - cuda:2
8	  - cuda:3
9	  project_path: /root/autodl-tmp/gen-depth-contamination
10	  servers:
11	  - cqa1-22115
12	  - westd-42896
13	feishu:
14	  chat_id: oc_5d2a0ec1de3a456564133278c1a9b203
15	  check_references: false
16	  operational_chat_id: oc_e168ce0e8c2b1176be821fdab5f2e3e6
17	  review_mode: fresh
18	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex
19	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_25/submitted.pdf
20	  review_round: 25
21	  review_supplementary_paths: ''
22	  submission_chat_id: oc_0f6dcb30efaa4f47425ef1d9874a89d7
23	project:
24	  created_at: '2026-05-12T10:56:48.753Z'
25	  description: How Deep Is Your Fake? Estimating Generational Depth of Recursive Synthetic
26	    Text for Quality-Aware Data Curation
27	  name: gen-depth-contamination
28	  phase: research
29	  source_idea_id: idea_013
30	rules:
31	  writing:
32	  - created_at: '2026-05-17T12:31:59Z'
33	    id: e83f3f
34	    text: 正文写作中，除了一些专有名词（比如说一些模型的名称）之外，在正常行文中不要出现破折号。
35	venue: emnlp-2026
36	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2356 · 2026-05-22T07:14:49.471275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2357 · 2026-05-22T07:14:50.576315+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	  - created_at: '2026-05-21T17:05:54Z'
22	    id: 0b1d8f
23	    text: ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 2358 · 2026-05-22T07:14:50.728588+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2359 · 2026-05-22T07:14:50.779693+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml
## Review Issues Tracker — gen-depth-contamination
## Updated: Round 24 Action Matrix dispatched (2026-05-22)

# === CRITICAL / MUST-FIX ===

- id: "R24-C1"
  summary: "附录至少 5-6 个数据表为空占位符（ANOVA、域消融、Pythia 解码、长度消融、Scorer sensitivity）"
  category: format
  severity: critical
  status: in_progress
  first_raised_round: 23
  last_seen_round: 24
  mentions:
    - round: 23
      reviewer: [R1, R2]
      note: "Round 23 已部分发现空表问题（R23-M2 orphan bib 相关）"
    - round: 24
      reviewer: [R1, R2]
      note: "5-6 个空表构成系统性投稿质量问题。ANOVA 空表尤严重。"
  action_items:
    - round: 24
      action: "填充所有空占位符表格的实际数据；如实验未完成则移除引用这些表格的声明"
      assigned_to: agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R24-C2"
  summary: "Cross-scorer 验证部分证伪 scorer independence claim（Qwen-cont K*=2→1）"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 22
  last_seen_round: 24
  mentions:
    - round: 22
      reviewer: [R1, R2]
      note: "R22-W1: 跨模型迁移 boundary-level 失败需更充分讨论"
    - round: 24
      reviewer: [R1, R2]
      note: "Qwen-cont 自身打分 K*=2 仅超 θ 0.002，Pythia/OLMo 打分均 <θ。Discussion 仍写 'confirms K* governed by generation process'。"
  action_items:
    - round: 24
      action: "Discussion 修正 scorer independence 措辞：区分 robust vs marginal K*=2"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R1-N1"
  summary: "DPI→adjacent-pair AUC 推理链存在逻辑缺口"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 20
  last_seen_round: 24
  mentions:
    - round: 20
      reviewer: R1
      note: "DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。"
    - round: 24
      reviewer: [R1, R2]
      note: "应明确 DPI 是 heuristic motivation 而非 strict proof。"
  action_items:
    - round: 22
      action: "全文 grep 'guarantee' 替换为 'motivate/imply'"
      assig
…[truncated 11023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2360 · 2026-05-22T07:15:22.262318+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2361 · 2026-05-22T07:15:22.262862+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2362 · 2026-05-22T07:15:27.885648+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "gen-depth-contamination",
  "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "gen-depth-contamination",
    "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
  }
}
```

</details>

---


### Tool result

_source line 2363 · 2026-05-22T07:15:46.037512+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18151
}
```

</details>

---


### Tool call

_source line 2364 · 2026-05-22T07:15:46.941306+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验验证**。\n\n## 投稿信息\n- **目标 Venue**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 正文 8 页，参考文献无限，Limitations 必选（不计页数），double-blind\n- **匿名规则**: 完全匿名（不得出现作者信息、不可追溯的自引用）\n- **特殊**: EMNLP 与 AACL 共享 ARR May cycle\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_25/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性（重点）\n- K*_empirical 的形式化定义是否完备、自洽\n- DPI（Data Processing Inequality）到 adjacent-pair AUC 的推理链是否存在逻辑缺口\n- θ=0.60 阈值选择的合理性和鲁棒性（是否 post-hoc、是否对结论敏感）\n- OBD-LightGBM 分类器设计的合理性（特征工程、交叉验证设计）\n- 统计检验的正确性（bootstrap CI、permutation test、ANOVA）\n- self-BLEU 计算中是否存在信息泄漏风险\n\n### 2. 实验验证\n- 10 个模型配置的覆盖面是否充分（模型家族多样性、规模范围）\n- cross-scorer 验证中 K*=2→1 降级的严重性评估\n- cross-model transfer 的结论是否被数据支撑\n- 下游 filtering 实验的效果量是否在实际场景中有意义\n- arXiv 域验证的样本量（n=2200）是否足够\n- 消融实验的完备性\n\n### 3. 格式合规（次要）\n- 正文是否在 8 页以内\n- 是否包含 Limitations section\n- 匿名性是否满足\n\n请按以下结构输出你的审稿意见：\n1. Summary（2-3 句概述）\n2. Strengths（逐条列出）\n3. Weaknesses（逐条列出，按严重性排序：Must-Fix / Should-Fix / Minor）\n4. Questions（需要作者澄清的问题）\n5. Missing References（遗漏的重要文献）\n6. Overall Assessment（评分 + 理由，使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n7. Confidence（1-5）",
  "reviewer_id": "1",
  "project": "gen-depth-contamination",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验验证**。\n\n## 投稿信息\n- **目标 Venue**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 正文 8 页，参考文献无限，Limitations 必选（不计页数），double-blind\n- **匿名规则**: 完全匿名（不得出现作者信息、不可追溯的自引用）\n- **特殊**: EMNLP 与 AACL 共享 ARR May cycle\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_25/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法严谨性（重点）\n- K*_empirical 的形式化定义是否完备、自洽\n- DPI（Data Processing Inequality）到 adjacent-pair AUC 的推理链是否存在逻辑缺口\n- θ=0.60 阈值选择的合理性和鲁棒性（是否 post-hoc、是否对结论敏感）\n- OBD-LightGBM 分类器设计的合理性（特征工程、交叉验证设计）\n- 统计检验的正确性（bootstrap CI、permutation test、ANOVA）\n- self-BLEU 计算中是否存在信息泄漏风险\n\n### 2. 实验验证\n- 10 个模型配置的覆盖面是否充分（模型家族多样性、规模范围）\n- cross-scorer 验证中 K*=2→1 降级的严重性评估\n- cross-model transfer 的结论是否被数据支撑\n- 下游 filtering 实验的效果量是否在实际场景中有意义\n- arXiv 域验证的样本量（n=2200）是否足够\n- 消融实验的完备性\n\n### 3. 格式合规（次要）\n- 正文是否在 8 页以内\n- 是否包含 Limitations section\n- 匿名性是否满足\n\n请按以下结构输出你的审稿意见：\n1. Summary（2-3 句概述）\n2. Strengths（逐条列出）\n3. Weaknesses（逐条列出，按严重性排序：Must-Fix / Should-Fix / Minor）\n4. Questions（需要作者澄清的问题）\n5. Missing References（遗漏的重要文献）\n6. Overall Assessment（评分 + 理由，使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n7. Confidence（1-5）",
    "reviewer_id": "1",
    "project": "gen-depth-contamination",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2365 · 2026-05-22T07:15:59.457638+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12516
}
```

</details>

---


### Tool call

_source line 2366 · 2026-05-22T07:15:59.809512+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work**。\n\n## 投稿信息\n- **目标 Venue**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 正文 8 页，参考文献无限，Limitations 必选（不计页数），double-blind\n- **匿名规则**: 完全匿名（不得出现作者信息、不可追溯的自引用）\n- **特殊**: EMNLP 与 AACL 共享 ARR May cycle\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_25/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估（重点）\n- \"Generational depth estimation\" 作为研究问题的新颖性和重要性\n- K*_empirical 概念的贡献度：是否是 trivial 的度量，还是真正有洞察力\n- \"One-wash laundering\" 发现的新颖性和对领域的影响\n- 与现有 model collapse / binary detection 工作的差异是否足够大\n- 该工作是否打开了有意义的新研究方向\n\n### 2. 完整性评估\n- 论文叙事的连贯性：从问题定义到实验到结论是否逻辑自洽\n- 实验设计是否完整覆盖了论文声明（claims vs evidence 对齐）\n- prompt-chain vs retrain-chain 的讨论是否充分\n- 是否缺少关键消融或对照实验\n- Limitations 是否充分覆盖了主要局限\n\n### 3. Related Work 审查\n- 是否遗漏了关键相关工作（尤其 2024-2026 的新论文）\n- 与最近工作的区分是否清晰（特别是 model collapse 文献、beyond-binary detection）\n- 引用是否真实存在且格式正确\n- 论文定位（positioning）是否准确\n\n### 4. 写作质量\n- 整体叙事结构是否清晰\n- 术语定义是否一致\n- 图表是否有效传达信息\n- Abstract 信息密度是否合适\n\n请按以下结构输出你的审稿意见：\n1. Summary（2-3 句概述）\n2. Strengths（逐条列出）\n3. Weaknesses（逐条列出，按严重性排序：Must-Fix / Should-Fix / Minor）\n4. Questions（需要作者澄清的问题）\n5. Missing References（遗漏的重要文献）\n6. Overall Assessment（评分 + 理由，使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n7. Confidence（1-5）",
  "reviewer_id": "2",
  "project": "gen-depth-contamination",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work**。\n\n## 投稿信息\n- **目标 Venue**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **格式要求**: ACL 模板，Long paper 正文 8 页，参考文献无限，Limitations 必选（不计页数），double-blind\n- **匿名规则**: 完全匿名（不得出现作者信息、不可追溯的自引用）\n- **特殊**: EMNLP 与 AACL 共享 ARR May cycle\n\n## 论文文件\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_25/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估（重点）\n- \"Generational depth estimation\" 作为研究问题的新颖性和重要性\n- K*_empirical 概念的贡献度：是否是 trivial 的度量，还是真正有洞察力\n- \"One-wash laundering\" 发现的新颖性和对领域的影响\n- 与现有 model collapse / binary detection 工作的差异是否足够大\n- 该工作是否打开了有意义的新研究方向\n\n### 2. 完整性评估\n- 论文叙事的连贯性：从问题定义到实验到结论是否逻辑自洽\n- 实验设计是否完整覆盖了论文声明（claims vs evidence 对齐）\n- prompt-chain vs retrain-chain 的讨论是否充分\n- 是否缺少关键消融或对照实验\n- Limitations 是否充分覆盖了主要局限\n\n### 3. Related Work 审查\n- 是否遗漏了关键相关工作（尤其 2024-2026 的新论文）\n- 与最近工作的区分是否清晰（特别是 model collapse 文献、beyond-binary detection）\n- 引用是否真实存在且格式正确\n- 论文定位（positioning）是否准确\n\n### 4. 写作质量\n- 整体叙事结构是否清晰\n- 术语定义是否一致\n- 图表是否有效传达信息\n- Abstract 信息密度是否合适\n\n请按以下结构输出你的审稿意见：\n1. Summary（2-3 句概述）\n2. Strengths（逐条列出）\n3. Weaknesses（逐条列出，按严重性排序：Must-Fix / Should-Fix / Minor）\n4. Questions（需要作者澄清的问题）\n5. Missing References（遗漏的重要文献）\n6. Overall Assessment（评分 + 理由，使用 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）\n7. Confidence（1-5）",
    "reviewer_id": "2",
    "project": "gen-depth-contamination",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2367 · 2026-05-22T07:16:01.692265+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1882
}
```

</details>

---


### Assistant

_source line 2368 · 2026-05-22T07:16:06.687505+00:00_

视觉审查 Agent 已派发，Reviewer 1（方法/实验）和 Reviewer 2（新颖性/完整性）已启动。等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 177

## Round 177

2 recorded events


### User

_source line 2369 · 2026-05-22T07:22:25.248071+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见（方法严谨性 + 实验验证）

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 问题定义新颖、实验设计严谨，K*_empirical 的形式化和"一次洗白"效应是有价值的贡献，但 DPI→AUC 的理论桥接仅为启发式、模型规模覆盖不足（≤8B）、下游实际增益偏小，三者叠加使其处于 Conference/Findings 交界。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论整体严谨，统计检验充分（bootstrap CI、permutation test、ANOVA），DPI→AUC 缺口已在正文中诚实承认（Section 3.1 "though AUC and mutual information are not formally equivalent"），但该缺口导致 K*_empirical 作为"下界"的理论地位只是断言而非证明；θ=0.60 的多重论证合理但对结论有非平凡敏感性 |
| Excitement | 3/5 | 生成深度估计是一个新颖且有实际动机的问题定义；"一次洗白"效应是可记忆的发现；但下游 filtering 效果量小（+0.74pp MMLU），实际影响力存疑 |
| Reproducibility | 4/5 | 实验细节充分（Appendix Table 14-16），超参数和数据集描述完整，使用公开数据集（C4），5-fold GroupKFold 设计好。但代码未提供 |
| Overall Assessment | 3.5/5 | Borderline Conference |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DPI→AUC 推理链的理论地位需要更清晰的界定

- 具体位置：Section 3.1（Eq. 1 及其前后文）；method.tex line 14-17
- 问题：论文以 Data Processing Inequality（MI 单调递减）作为"heuristic motivation"来期望 pairwise AUC_{k-1,k} 随 k 递减，并在 line 17 坦承"AUC and mutual information are not formally equivalent"。但正文随即在 Eq. 1 下方说"the ∀j constraint is naturally satisfied because AUC_{k-1,k} decreases monotonically above θ across all tested configurations"——这用经验规律性替代了形式证明。问题在于：（1）如果 AUC 单调性只是经验观察而非理论保证，K*_empirical 作为 K*_theory 的"lower bound"这一核心 claim（Section 3.1 最后一段）就仅是断言，缺乏形式化支撑；（2）对于未测试过的配置（更大模型、不同域），无法保证该单调性仍然成立，削弱了方法的泛化承诺。
- 为什么影响接收：这是全文理论框架的根基。如果 K*_empirical 不能被严格论证为某种意义上的下界，论文的核心叙事（"我们测量了一个保守的下界"）就只是一个框架性的修辞，而非有保证的结论。
- 建议修改方向：（a）明确区分"K*_empirical 是一个操作性定义"和"K*_empirical 是 K*_theory 的下界"这两个不同的 claim，对后者要么给出形式证明（例如通过 f-divergence 到 AUC 的已知不等式），要么降级为一个有经验支持的猜想（conjecture）；（b）补充讨论在什么条件下 AUC 单调性可能失效（例如特征集不完备时）。

**N2** [critical] 模型规模覆盖不足，核心发现的泛化性未验证

- 具体位置：Table 1（实验配置），Limitations (1)
- 问题：全部 10 个配置的模型规模为 1B–8B。当前部署中最常用的生成模型远超 8B（Llama-3-70B、GPT-4、Qwen2.5-72B 等）。更大的模型生成质量更高、文本与人类分布更接近，有理由预期 K*_empirical 可能增加（即更深代际仍可区分），也可能减少（即更快趋同于人类分布使区分更难）。论文未提供任何 >8B 模型的实验或间接证据。
- 为什么影响接收：K*_empirical ≈ 2 作为"web text 的通用结论"被 abstract 和 conclusion 强调，但实际上只在小模型上验证。如果大模型的 K*_empirical 显著不同（比如 =1 或 =4），核心发现的意义将完全改变。
- 建议修改方向：（a）至少补充 1-2 个 >30B 模型的实验（即使只用 Qwen2.5-32B 或类似可用模型）；（b）如果资源限制无法做到，在 Discussion/Conclusion 中显式将 K*_empirical ≈ 2 的适用范围限定为"≤8B 模型"，而非暗示为通用结论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cross-scorer 降级暴露了实际部署中的方法局限

- 具体位置：Table 22（Appendix），Section 4.2 最后一段
- 问题：Table 22 显示在 cross-scoring 条件下（用 Pythia-1.4B 或 OLMo-1B 提取特征来评估 Qwen 生成的文本），Qwen-1.5B-Instruct（continuation）的 K*_empirical 从 self-scoring 的 2 降至 1。论文将此描述为"only for the most marginal self-scorer condition"。但在实际部署场景中，用户不知道文本由哪个模型生成，无法选择"self-scorer"，因此 cross-scoring 才是实际工作条件。K*=2→1 的降级意味着在实际应用中，该方法可能只能可靠区分深度 0 和深度 1，实质上退化为普通的 binary detection。
- 建议：（a）在正文 Section 4.2 中更突出地讨论这一限制对部署的影响；（b）探索 scorer-ensemble 策略（多个 scorer 模型的投票/融合）是否能恢复 K*=2。

**W2** [warning] 下游 filtering 效果量小，实际意义有限

- 具体位置：Table 5（Section 5），Figure 5
- 问题：Binary K*-aware filtering 相对 no-filter 的 MMLU 提升为 0.5867→0.5941 = +0.74pp，HellaSwag 为 0.6018→0.6021 = +0.03pp（基本无差）。虽然 binary-ours 显著优于 DSIR（Table 5），但绝对改善幅度很小。论文诚实地指出这是 100% 合成污染场景下的结果，但即使在这一极端条件下，效果仍然偏小。
- 这削弱了 K*_empirical 的实际价值叙事：如果知道 K*=2 后的最佳策略（binary filtering）只带来 <1pp 的下游改善，practitioners 是否有足够动机去做 depth estimation？
- 建议：（a）补充更多下游任务（如 ARC、WinoGrande）来检验效果是否任务依赖；（b）或者在 Discussion 中讨论在什么污染比例下 filtering 效果会变得不可忽略（Appendix D.8 的 dose-response 分析已有雏形，但应在正文中更充分讨论）。

**W3** [warning] θ=0.60 对结论有非平凡的敏感性

- 具体位置：Figure 3（Section 3.2），Limitations (3)
- 问题：Figure 3 和 Limitations 均指出 K*_empirical 在 θ∈[0.55, 0.70] 范围内从 3 变化到 1。虽然论文论证了 θ=0.60 处存在 AUC 值的自然间断（~5-11pp discontinuity），但这个间断主要出现在 Qwen 配置中。对于 OLMo-1B（1v2 AUC = 0.612），θ 从 0.60 上调到 0.62 就足以改变 K*_empirical 从 2 到 1。
- 更根本的问题是：θ=0.60 对应 Cohen's h≈0.20（"small effect"），但论文没有论证为什么 "small effect" 是分类器能力的合适阈值。Cohen's h 最初用于两个 proportion 的比较，这里用于 AUC 阈值设定是一个类比性的引用，缺乏直接的理论依据。
- 建议：（a）补充对 θ-free 的结论表述（例如报告每个配置使 AUC 跨越 0.5 的最深 k）；（b）或提供一种基于 permutation null distribution 的自适应阈值方法，消除对固定 θ 的依赖。

**W4** [warning] 对 Qwen-rewrite 与 Qwen-continuation 差异的解释不够充分

- 具体位置：Section 4.3, Section 6 (Discussion)
- 问题：Qwen-rewrite 一致地产生 K*_empirical = 2（甚至在 cross-domain 时也如此），而 Qwen-continuation 在多个条件下边界更脆弱（cross-scorer 降至 1，1v2 AUC 仅 0.611）。论文将此归因于"continuation mode 中的模型适应偏差更强"（Section 6），但未深入分析。rewrite mode 的指令"paraphrase the following"引入了更强的风格锚定（anchoring to the original semantics），这与 continuation mode 的自由延续在信息理论上有本质区别——rewrite 保持语义但改变表达，continuation 改变语义和表达。这个区别对 K*_empirical 的不同影响值得更细致的分析。
- 建议：（a）增加对两种 mode 下 feature 分布变化模式的可视化对比；（b）讨论在何种条件下 rewrite 和 continuation 的 K*_empirical 可能趋同或进一步分化。

---

## 小问题（不影响接收）

- **M1**: Table 2 注释中 "†Generates Qwen2.5-7B (dp3) scorer: Qwen2.5-1.5B" 可更清晰地说明跨模型评分的方向。
- **M2**: Section 4.1 提到"6/10 configurations yield K*_empirical ≥ 2"，但 Table 2 中 Mistral-7B 和 Gemma-2-2B 的数据在正文中缺失（仅在 Table 9 中出现），正文的覆盖不够完整。建议在正文中至少添加一句话概述这些额外配置的结果。
- **M3**: Figure 1（pipeline 图）中 "K* Estimation" 步骤的箭头指向不够清晰——读者可能困惑 K* 是从单个文档还是从整个语料库层面估计的。
- **M4**: Table 12 显示 Pythia-1.4B 的 EOS truncation rate 为 34-36%，这意味着超过 1/3 的生成样本在未达到 256 tokens 时就自然终止。这是否引入了长度混淆效应？论文在 Section 6 中提到"human texts shorter"使检测"more conservative"，但未讨论 Pythia 高 truncation 率的影响。

---

## Questions（需要作者澄清）

**Q1**: 如果使用更强的分类器（如在生成文本上微调的 transformer encoder），K*_empirical 是否会增加？论文称当前 15D+LightGBM 给出的是"feature-set-specific lower bound"，但没有提供上界的估计。Neural probe（Table 5, Appendix）给出 Qwen K*=3，暗示 K*_theory 可能更高——这是否削弱了"一次洗白"叙事？

**Q2**: θ=0.60 到 Cohen's h≈0.20 的映射假设了 baseline AUC=0.50。但在实际分类中，null AUC 可能因类别不平衡或特征相关性而偏离 0.50。permutation test 给出的 95th percentile null 是 <0.55，这意味着实际的"实质效应"起点应该在 0.55 附近而非 0.50。能否用 permutation null 直接校准 θ 而不是固定为 0.60？

**Q3**: 论文报告的 AUC 是在 5-fold GroupKFold 上的平均值。对于边界 case（如 Qwen-cont 1v2 AUC = 0.611），各 fold 之间的方差是多少？是否存在某些 fold 中 AUC < θ 的情况？

**Q4**: 下游 filtering 实验仅使用 Qwen-1.5B continuation mode 生成的污染数据。如果污染来自 K*_empirical=1 的模型（如 OLMo-1B），binary filtering 是否仍然有效？此时 K*-aware 的价值是否消失？

**Q5**: arXiv 域 K*_empirical=3 的发现（Table 4, Table 21）是基于 n=2,200 样本。请澄清：这 2,200 样本是每个模型家族 2,200（共 4,400）还是两个家族共享 2,200？每个深度级别的样本量具体是多少？

---

## Missing References

1. **Gehrmann et al. (2019)** "GLTR: Statistical Detection and Visualization of Generated Text"——该工作是最早使用 token-level log probability 分布特征检测生成文本的方法之一，与本文的 surprisal-based 特征设计直接相关，应在 Section 2 或 Section 3.2 引用。
2. **Tang et al. (2024)** "The Science of Detecting LLM-Generated Text"——该综述系统梳理了检测方法分类学，与本文 Related Work 中的框架互补。

---

## 主要优势

1. **问题定义新颖**：generational depth estimation 是一个之前未被正式定义的问题；K*_empirical 作为可操作的量化指标填补了 binary detection 和 model collapse 文献之间的空白。
2. **实验设计严谨**：5-fold GroupKFold（按 seed document 分组）防止数据泄漏；self-BLEU 的 fold-internal 计算消除了信息泄漏风险；bootstrap CI + permutation test + ANOVA 三重统计验证。
3. **"一次洗白"效应**的发现有实际启示：对 training data curation pipeline，这意味着深度估计可以简化为 binary decision（保留 vs 丢弃），无需投入精力做精细的 depth grading。
4. **cross-model transfer 结果**（Table 7, Figure 4）表明特征的跨模型家族可迁移性，增强了方法的实用性。
5. **附录极其充分**：21 个表格 + 5 个图覆盖了几乎所有合理的消融和鲁棒性检查（segment length、seed robustness、dose-response、decoding strategy、LLM zero-shot comparison），体现了实验的完整性。
6. **Limitations 部分诚实全面**：7 个具体限制点覆盖了主要方法论局限，包括 cross-scorer 边界脆弱性和阈值敏感性。

---

## Overall Assessment 详细理由

**评分：3.5（Borderline Conference）**

本文提出了一个新颖的问题定义，实验设计严谨，附录充分。K*_empirical 的概念和"一次洗白"效应是有价值的贡献。方法论的主要弱点在于：(1) DPI→AUC 的理论桥接只是启发式的，K*_empirical 作为 lower bound 的地位未被形式证明；(2) 模型规模限于 ≤8B，核心发现 K*≈2 的泛化性未验证；(3) 下游 filtering 效果量小（<1pp MMLU），实际影响力存疑。

如果作者能：(a) 补充 ≥1 个 >30B 模型的验证实验，(b) 明确 K*_empirical 作为 lower bound 的理论条件（或降级表述），(c) 在正文中更充分地讨论 cross-scorer 降级和 θ 敏感性的部署影响——则有望达到 Conference 接收标准。

**Confidence: 4/5**（对 ML 文本分析和统计方法论有丰富经验，仔细阅读了正文和全部附录；但对 Ordinal Binary Decomposition 的最优性没有专家级判断力）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2370 · 2026-05-22T07:22:35.229091+00:00_

Reviewer 1 已提交审稿意见（3.5 分，Borderline Conference）。等待 Reviewer 2 的意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 178

## Round 178

2 recorded events


### User

_source line 2371 · 2026-05-22T07:22:37.908304+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交至 Review Director。

核心判断：**3.5/5（Borderline Conference）**。

主要发现：

**2 个 Must-Fix**：
- **N1**：DPI→AUC 的推理链仅为启发式，K*_empirical 作为 K*_theory 下界的 claim 缺乏形式化证明
- **N2**：模型规模仅覆盖 ≤8B，核心结论 K*≈2 的泛化性未在大模型上验证

**4 个 Should-Fix**：
- Cross-scorer 降级（K*=2→1）暴露部署局限
- 下游 filtering 效果量小（+0.74pp MMLU）
- θ=0.60 阈值敏感性（θ∈[0.55,0.70] 内 K* 从 3 变到 1）
- Rewrite vs Continuation 差异的分析不够深入

**优势面**：问题定义新颖、实验设计严谨（GroupKFold + bootstrap CI + permutation test）、附录极其充分、"一次洗白"效应有实际启示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2372 · 2026-05-22T07:22:43.552158+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 179

## Round 179

8 recorded events


### User

_source line 2373 · 2026-05-22T07:24:05.167129+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 完整性 + Related Work）

### 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 问题定义新颖且实验覆盖充分，但 K*_empirical≈2 的核心发现实质上将 depth estimation 退化为 binary detection，限制了实际贡献度；阈值敏感性和 Qwen 配置过度代表也削弱了结论的普适性。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法论扎实（bootstrap CI, permutation test, 5-fold GroupKFold），但关键边界处 K*=2 鲁棒性存疑（Qwen-cont 1v2 CI 下界仅超 θ 0.002），阈值敏感性高 |
| Excitement | 3/5 | 问题定义有新颖性，"one-wash laundering"有价值，但 K*=2 本质上验证了 binary detection 的充分性，限制了后续研究空间 |
| Reproducibility | 4/5 | 实验设置详尽，特征定义完整，超参数清晰，使用公开数据集 |
| Confidence | 4/5 | 对 AI text detection 和 model collapse 文献较熟悉 |

### Must-Fix 问题

**N1** [critical] K*_empirical=2 的 Qwen 过度代表与结论泛化性
- 位置：Section 4.1, Table 2, Abstract
- 6/10 configurations 中 4 个来自 Qwen。按 family 统计：非 Qwen 家族仅 2/5 达到 K*=2（LLaMA 1 config + Pythia-1.4B），而 OLMo/Mistral/Gemma 全为 K*=1。Abstract "6/10 configurations" 的表述技术上正确但误导性强。
- 影响：核心贡献的普适性直接受质疑。Section 5 filtering 也仅在 Qwen 上验证。
- 建议：补充按 family 汇总的统计，讨论 Qwen 为何一致性更强。

**N2** [critical] 阈值 θ=0.60 的敏感性
- 位置：Section 3.1, Figure 3
- θ=0.55→K*=3（部分配置），θ=0.70→全部 K*=1。Qwen-cont CI 下界仅超 θ 0.002。Cohen's h=0.20 是统计惯例而非检测理论推导。
- 影响：K*_empirical 作为可操作量的稳健性不足。
- 建议：报告 θ-free 指标（如 AUC gap 的显著性），展示完整灵敏度曲线。

**N3** [critical] Prompt-chain 的生态有效性
- 位置：Section 1, Section 6, Appendix D.7
- Retrain-chain K*≥4（Appendix D.7），远超 prompt-chain K*=2。现实 contamination 通常涉及 cross-model retrain-chain。论文的 "one-wash laundering" 可能是 prompt-chain 特有现象。
- 影响：核心叙事的适用范围受限。
- 建议：扩展 retrain-chain 至主实验，弱化 "one-wash laundering" 的普适性声明。

### Should-Fix 问题

**W1** Filtering 实验仅 Qwen-1.5B 单一配置（Section 5）。至少需在 K*=1 配置上重复。

**W2** K*=2 的实际新贡献 vs binary detection 讨论不足（Section 6-7）。如果结论是 "binary is sufficient"，论文相对于已有 binary detection 文献提供的新能力需要更明确地阐述。

**W3** >8B 模型可能 yield K*=1 的风险在 Conclusion 中未充分反映。

**W4** Related Work 遗漏 "Rate of Model Collapse" (Suresh et al., 2024, arXiv:2412.17646)。

### 小问题
- Abstract 中 "Cohen's h≈0.20" 缺乏上下文
- Table 2 需视觉高亮 K* boundary 行
- self-BLEU 特征在 deployment 场景下的计算方式需澄清
- Limitations (6) 提到 512 tokens 时 boundary 减弱，值得在正文提及

### Questions
1. K* 定义假设 AUC 单调递减，10 个配置中是否有任何接近 non-monotonic 的情况？
2. Cross-model retrain-chain（如 Qwen→Pythia→OLMo）下 K* 预期是什么？
3. 100% synthetic 训练数据是 upper bound，但 Appendix D.8 显示 ≤30% contamination 下策略差异消失——这是否意味着现实中 K*-aware filtering 实际无用？

### Missing References
1. **Should-Cite**: Suresh et al. (2024) "Rate of Model Collapse in Recursive Training" (arXiv:2412.17646)
2. Nice-to-Cite: Borji (2024) "A Note on Shumailov et al." (arXiv:2410.12954)
3. Nice-to-Cite: Dugan et al. (ACL 2024) "RAID" benchmark

### 主要优势
- 问题定义新颖且有 DPI 理论支撑
- 实验覆盖度极高（10 configs × 4 decoding × 3 domains + 大量 ablation）
- "One-wash laundering" 对数据 curation 社区有直接参考价值
- 统计实践规范（bootstrap CI, permutation test, effect size）
- Limitations section 极为彻底（7 条详细限制）

### 总体判断
3.5 / 5 (Borderline Conference)。问题定义有贡献，实验质量高，但 K*=2 的 Qwen 依赖性、θ 敏感性、prompt-chain 生态有效性三个问题共同限制了 impact scope。处于 Conference 和 Findings 的边界。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2374 · 2026-05-22T07:24:16.299470+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2375 · 2026-05-22T07:24:16.350286+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2376 · 2026-05-22T07:24:31.977597+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + Related Work）\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] K*_empirical=2 的 Qwen 过度代表与结论泛化性\n- 6/10 configurations 中 4 个来自 Qwen。按 family 统计：非 Qwen 家族仅 2/5 达到 K*=2（LLaMA 1 config + Pythia-1.4B），而 OLMo/Mistral/Gemma 全为 K*=1。Abstract \"6/10 configurations\" 的表述技术上正确但误导性强。\n- 建议：补充按 family 汇总的统计，讨论 Qwen 为何一致性更强。\n\n**N2** [critical] 阈值 θ=0.60 的敏感性\n- θ=0.55→K*=3（部分配置），θ=0.70→全部 K*=1。Qwen-cont CI 下界仅超 θ 0.002。Cohen's h=0.20 是统计惯例而非检测理论推导。\n- 建议：报告 θ-free 指标（如 AUC gap 的显著性），展示完整灵敏度曲线。\n\n**N3** [critical] Prompt-chain 的生态有效性\n- Retrain-chain K*≥4（Appendix D.7），远超 prompt-chain K*=2。现实 contamination 通常涉及 cross-model retrain-chain。论文的 \"one-wash laundering\" 可能是 prompt-chain 特有现象。\n- 建议：扩展 retrain-chain 至主实验，弱化 \"one-wash laundering\" 的普适性声明。\n\n### Should-Fix 问题\n\n**W1** Filtering 实验仅 Qwen-1.5B 单一配置（Section 5）。至少需在 K*=1 配置上重复。\n\n**W2** K*=2 的实际新贡献 vs binary detection 讨论不足（Section 6-7）。如果结论是 \"binary is sufficient\"，论文相对于已有 binary detection 文献提供的新能力需要更明确地阐述。\n\n**W3** >8B 模型可能 yield K*=1 的风险在 Conclusion 中未充分反映。\n\n**W4** Related Work 遗漏 \"Rate of Model Collapse\" (Suresh et al., 2024, arXiv:2412.17646)。\n\n### 小问题\n- Abstract 中 \"Cohen's h≈0.20\" 缺乏上下文\n- Table 2 需视觉高亮 K* boundary 行\n- self-BLEU 特征在 deployment 场景下的计算方式需澄清\n- Limitations (6) 提到 512 tokens 时 boundary 减弱，值得在正文提及\n\n### Questions\n1. K* 定义假设 AUC 单调递减，10 个配置中是否有任何接近 non-monotonic 的情况？\n2. Cross-model retrain-chain（如 Qwen→Pythia→OLMo）下 K* 预期是什么？\n3. 100% synthetic 训练数据是 upper bound，但 Appendix D.8 显示 ≤30% contamination 下策略差异消失——这是否意味着现实中 K*-aware filtering 实际无用？\n\n### Missing References\n1. Suresh et al. (2024) \"Rate of Model Collapse in Recursive Training\"\n2. Borji (2024) \"A Note on Shumailov et al.\"\n3. Dugan et al. (ACL 2024) \"RAID\" benchmark\n\n### 主要优势\n- 问题定义新颖且有 DPI 理论支撑\n- 实验覆盖度极高\n- \"One-wash laundering\" 对数据 curation 社区有直接参考价值\n- 统计实践规范\n- Limitations section 极为彻底\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix、小问题和 Questions。",
  "reviewer_id": "1",
  "project": "gen-depth-contamination",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + Related Work）\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] K*_empirical=2 的 Qwen 过度代表与结论泛化性\n- 6/10 configurations 中 4 个来自 Qwen。按 family 统计：非 Qwen 家族仅 2/5 达到 K*=2（LLaMA 1 config + Pythia-1.4B），而 OLMo/Mistral/Gemma 全为 K*=1。Abstract \"6/10 configurations\" 的表述技术上正确但误导性强。\n- 建议：补充按 family 汇总的统计，讨论 Qwen 为何一致性更强。\n\n**N2** [critical] 阈值 θ=0.60 的敏感性\n- θ=0.55→K*=3（部分配置），θ=0.70→全部 K*=1。Qwen-cont CI 下界仅超 θ 0.002。Cohen's h=0.20 是统计惯例而非检测理论推导。\n- 建议：报告 θ-free 指标（如 AUC gap 的显著性），展示完整灵敏度曲线。\n\n**N3** [critical] Prompt-chain 的生态有效性\n- Retrain-chain K*≥4（Appendix D.7），远超 prompt-chain K*=2。现实 contamination 通常涉及 cross-model retrain-chain。论文的 \"one-wash laundering\" 可能是 prompt-chain 特有现象。\n- 建议：扩展 retrain-chain 至主实验，弱化 \"one-wash laundering\" 的普适性声明。\n\n### Should-Fix 问题\n\n**W1** Filtering 实验仅 Qwen-1.5B 单一配置（Section 5）。至少需在 K*=1 配置上重复。\n\n**W2** K*=2 的实际新贡献 vs binary detection 讨论不足（Section 6-7）。如果结论是 \"binary is sufficient\"，论文相对于已有 binary detection 文献提供的新能力需要更明确地阐述。\n\n**W3** >8B 模型可能 yield K*=1 的风险在 Conclusion 中未充分反映。\n\n**W4** Related Work 遗漏 \"Rate of Model Collapse\" (Suresh et al., 2024, arXiv:2412.17646)。\n\n### 小问题\n- Abstract 中 \"Cohen's h≈0.20\" 缺乏上下文\n- Table 2 需视觉高亮 K* boundary 行\n- self-BLEU 特征在 deployment 场景下的计算方式需澄清\n- Limitations (6) 提到 512 tokens 时 boundary 减弱，值得在正文提及\n\n### Questions\n1. K* 定义假设 AUC 单调递减，10 个配置中是否有任何接近 non-monotonic 的情况？\n2. Cross-model retrain-chain（如 Qwen→Pythia→OLMo）下 K* 预期是什么？\n3. 100% synthetic 训练数据是 upper bound，但 Appendix D.8 显示 ≤30% contamination 下策略差异消失——这是否意味着现实中 K*-aware filtering 实际无用？\n\n### Missing References\n1. Suresh et al. (2024) \"Rate of Model Collapse in Recursive Training\"\n2. Borji (2024) \"A Note on Shumailov et al.\"\n3. Dugan et al. (ACL 2024) \"RAID\" benchmark\n\n### 主要优势\n- 问题定义新颖且有 DPI 理论支撑\n- 实验覆盖度极高\n- \"One-wash laundering\" 对数据 curation 社区有直接参考价值\n- 统计实践规范\n- Limitations section 极为彻底\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix、小问题和 Questions。",
    "reviewer_id": "1",
    "project": "gen-depth-contamination",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2377 · 2026-05-22T07:24:56.939539+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24961
}
```

</details>

---


### Tool call

_source line 2378 · 2026-05-22T07:24:57.091196+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验验证）\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] DPI→AUC 推理链的理论地位需要更清晰的界定\n- Section 3.1（Eq. 1 及其前后文）：论文以 DPI 作为 heuristic motivation，但随即在 Eq. 1 下方用经验规律性替代形式证明（\"AUC_{k-1,k} decreases monotonically above θ across all tested configurations\"）。K*_empirical 作为 K*_theory 的 \"lower bound\" 仅是断言，缺乏形式化支撑。\n- 建议：明确区分\"K*_empirical 是操作性定义\"和\"K*_empirical 是 K*_theory 的下界\"，对后者要么形式证明要么降级为 conjecture。\n\n**N2** [critical] 模型规模覆盖不足（≤8B）\n- 10 个配置全部 1B-8B，当前常用生成模型远超 8B。更大模型的 K*_empirical 可能显著不同。\n- 建议：补充 >30B 模型实验或显式限定适用范围。\n\n### Should-Fix 问题\n\n**W1** Cross-scorer 降级暴露部署局限（Qwen-cont K*=2→1）\n- 实际部署中用户不知道生成器身份，cross-scoring 才是实际工作条件。K*=2→1 意味着退化为 binary detection。\n- 建议：讨论 scorer-ensemble 策略。\n\n**W2** 下游 filtering 效果量小（+0.74pp MMLU, +0.03pp HellaSwag）\n- 即使在 100% 合成污染极端条件下，效果仍偏小。\n- 建议：补充更多下游任务或讨论 filtering 效果随污染比例的变化。\n\n**W3** θ=0.60 对结论有非平凡的敏感性\n- θ∈[0.55, 0.70] 内 K* 从 3 变到 1。Cohen's h 用于 AUC 阈值设定缺乏直接理论依据。\n- 建议：补充 θ-free 结论表述或自适应阈值方法。\n\n**W4** Qwen-rewrite vs Qwen-continuation 差异分析不够深入\n- 建议增加两种 mode 下 feature 分布变化的可视化对比。\n\n### 小问题\n- M1: Table 2 注释可更清晰\n- M2: 正文缺少 Mistral-7B 和 Gemma-2-2B 数据覆盖\n- M3: Figure 1 中 K* Estimation 步骤箭头指向不清\n- M4: Pythia-1.4B EOS truncation rate 34-36% 是否引入长度混淆\n\n### Questions\n- Q1: 更强分类器是否会增加 K*_empirical？Neural probe K*=3 是否削弱\"一次洗白\"叙事？\n- Q2: θ=0.60 到 Cohen's h 的映射假设 baseline AUC=0.50，能否用 permutation null 直接校准？\n- Q3: 边界 case 的 fold 间方差是多少？\n- Q4: K*=1 模型的污染数据下 binary filtering 是否仍有效？\n- Q5: arXiv 域 n=2,200 是每个模型还是共享？\n\n### Missing References\n1. Gehrmann et al. (2019) \"GLTR\"\n2. Tang et al. (2024) \"The Science of Detecting LLM-Generated Text\"\n\n### 主要优势\n- 问题定义新颖\n- 实验设计严谨（GroupKFold + bootstrap CI + permutation test）\n- \"一次洗白\"效应有实际启示\n- 附录极其充分（21 表 + 5 图）\n- Limitations 诚实全面\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix、小问题和 Questions。",
  "reviewer_id": "2",
  "project": "gen-depth-contamination",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验验证）\n\n### 总体评分\n**Overall**: 3.5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] DPI→AUC 推理链的理论地位需要更清晰的界定\n- Section 3.1（Eq. 1 及其前后文）：论文以 DPI 作为 heuristic motivation，但随即在 Eq. 1 下方用经验规律性替代形式证明（\"AUC_{k-1,k} decreases monotonically above θ across all tested configurations\"）。K*_empirical 作为 K*_theory 的 \"lower bound\" 仅是断言，缺乏形式化支撑。\n- 建议：明确区分\"K*_empirical 是操作性定义\"和\"K*_empirical 是 K*_theory 的下界\"，对后者要么形式证明要么降级为 conjecture。\n\n**N2** [critical] 模型规模覆盖不足（≤8B）\n- 10 个配置全部 1B-8B，当前常用生成模型远超 8B。更大模型的 K*_empirical 可能显著不同。\n- 建议：补充 >30B 模型实验或显式限定适用范围。\n\n### Should-Fix 问题\n\n**W1** Cross-scorer 降级暴露部署局限（Qwen-cont K*=2→1）\n- 实际部署中用户不知道生成器身份，cross-scoring 才是实际工作条件。K*=2→1 意味着退化为 binary detection。\n- 建议：讨论 scorer-ensemble 策略。\n\n**W2** 下游 filtering 效果量小（+0.74pp MMLU, +0.03pp HellaSwag）\n- 即使在 100% 合成污染极端条件下，效果仍偏小。\n- 建议：补充更多下游任务或讨论 filtering 效果随污染比例的变化。\n\n**W3** θ=0.60 对结论有非平凡的敏感性\n- θ∈[0.55, 0.70] 内 K* 从 3 变到 1。Cohen's h 用于 AUC 阈值设定缺乏直接理论依据。\n- 建议：补充 θ-free 结论表述或自适应阈值方法。\n\n**W4** Qwen-rewrite vs Qwen-continuation 差异分析不够深入\n- 建议增加两种 mode 下 feature 分布变化的可视化对比。\n\n### 小问题\n- M1: Table 2 注释可更清晰\n- M2: 正文缺少 Mistral-7B 和 Gemma-2-2B 数据覆盖\n- M3: Figure 1 中 K* Estimation 步骤箭头指向不清\n- M4: Pythia-1.4B EOS truncation rate 34-36% 是否引入长度混淆\n\n### Questions\n- Q1: 更强分类器是否会增加 K*_empirical？Neural probe K*=3 是否削弱\"一次洗白\"叙事？\n- Q2: θ=0.60 到 Cohen's h 的映射假设 baseline AUC=0.50，能否用 permutation null 直接校准？\n- Q3: 边界 case 的 fold 间方差是多少？\n- Q4: K*=1 模型的污染数据下 binary filtering 是否仍有效？\n- Q5: arXiv 域 n=2,200 是每个模型还是共享？\n\n### Missing References\n1. Gehrmann et al. (2019) \"GLTR\"\n2. Tang et al. (2024) \"The Science of Detecting LLM-Generated Text\"\n\n### 主要优势\n- 问题定义新颖\n- 实验设计严谨（GroupKFold + bootstrap CI + permutation test）\n- \"一次洗白\"效应有实际启示\n- 附录极其充分（21 表 + 5 图）\n- Limitations 诚实全面\n\n---\n\n请逐条回应以上所有 Must-Fix、Should-Fix、小问题和 Questions。",
    "reviewer_id": "2",
    "project": "gen-depth-contamination",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2379 · 2026-05-22T07:24:58.652978+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1561
}
```

</details>

---


### Assistant

_source line 2380 · 2026-05-22T07:25:01.242399+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 180

## Round 180

2 recorded events


### User

_source line 2381 · 2026-05-22T07:25:03.963697+00:00_

[Reviewer 2 审稿结果]:
审稿完成，已提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。三个 Must-Fix 问题：(1) K\*=2 结论依赖 Qwen 过度代表（6/10 中 4 个是 Qwen），按 family 计泛化性不足；(2) θ=0.60 阈值敏感性高，K\* 作为可操作量稳健性存疑；(3) prompt-chain 设定与现实 retrain-chain collapse 场景有显著 gap，"one-wash laundering" 可能是设定特有现象。主要优势在于问题定义确有新意、实验覆盖度极高、统计实践规范。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2382 · 2026-05-22T07:25:09.317243+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 181

## Round 181

2 recorded events


### User

_source line 2383 · 2026-05-22T07:27:04.322522+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的逐条回应

### Must-Fix

**[AGREE] R1-N1: DPI→AUC 理论地位**
同意需要澄清，但建议降为 should-fix。论文 Section 3.1 已承认 "AUC and mutual information are not formally equivalent"，DPI 仅为 heuristic motivation。"K*_empirical 是 K*_theory 的 lower bound" 从逻辑上成立（15D 特征 ⊂ 最优特征空间），但未形式化。降级为 conjecture 即可。

**[AGREE] R1-N2: 模型规模 ≤8B**
与我 W3 一致。Discussion 自身观察到 0v1 JSD 从 ≤1.5B 的 0.15–0.27 降到 8B 的 0.077。Pythia 1.4B→6.9B K*从 2→1 支持规模趋势。但补充 >30B 实验在 ARR 周期内不太现实，建议改为在 Abstract/Conclusion 明确限定 "1B–8B" 适用范围。

### Should-Fix

**[AGREE] R1-W1: Cross-scorer 降级**
Section 4.2 Qwen-cont cross-scoring AUC=0.5923(Pythia)/0.5858(OLMo) 均 <θ。在 generator 未知的部署场景下 K*=2 不稳健。补充：即使 ensemble 也无法解决 marginal signal 本身的问题。

**[AGREE] R1-W2: Filtering 效果量小**
同意，但论文 Section 5 首段已定位为 "consistency check, not independent contribution"。更关键的是 Appendix D.8 显示 ≤30% contamination 下所有策略收敛——应在正文承认现实污染比例下 K*-aware filtering 边际增益可忽略。

**[AGREE] R1-W3: θ 敏感性**
与我 N2 完全一致。强烈支持 R1 建议的 θ-free 表述（报告 AUC gap 及其 CI）。

**[REBUT] R1-W4: Rewrite vs continuation 分析**
Section 4.3 + Table 6 + Figure 4 已提供充分证据。Feature ranking 差异（continuation: surp_d1_std; rewrite: freq_entropy）和 transfer gap（61–63%）已清晰说明差异来源。在 8 页限制下增加可视化非必要，降级为 minor。

### 小问题

**[AGREE] M1, M2, M3**。M2 尤其重要——Mistral-7B 和 Gemma-2-2B 在正文中缺乏完整报告，支持我 N1 关于 Qwen 过度代表的观点。

**[REBUT] M4**: Appendix Table 12 已详细分析 token count 和 EOS truncation。Depth 1–5 mean token count 无系统趋势（Pythia: 214→218），长度差异主要在 depth 0 vs 1+。论文已 adequately 讨论。

### Questions

**[AGREE] Q1**: Neural probe K*=3 确实给 "one-wash laundering" 带来张力。如果 self-familiarity 是合法信号，K*=3 才是真实 boundary，K*=2 是 feature limitation artifact。论文应更坦诚讨论。

**[AGREE] Q2, Q3, Q4**。Q4 与我 W1 一致。

**[REBUT] Q5**: Table 4 中两个模型有独立结果，可推断 n=2,200 是 per-model，但正文应更明确。

### Missing References

**[REBUT] MR1 (GLTR)**: 2019 年工作已被论文引用的后续方法覆盖，非 necessary。
**[AGREE] MR2 (Tang et al.)**: 需核实引用真实性，如为 survey 则有引用价值。

### 两位 Reviewer 共识总结

核心一致点：(1) θ 敏感性（R1-W3 = R2-N2）；(2) 模型规模限制（R1-N2 = R2-W3）；(3) Filtering 泛化不足（R1-Q4 = R2-W1）。评分一致（均 3.5）。

主要分歧：R2 更强调 Qwen 过度代表（R2-N1），R1 更关注 DPI→AUC 理论地位（R1-N1）。

三个最需解决的问题：(1) θ-free 表述；(2) K*=2 泛化性的审慎 framing；(3) prompt-chain 适用范围限定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2384 · 2026-05-22T07:27:12.235343+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 182

## Round 182

2 recorded events


### User

_source line 2385 · 2026-05-22T07:27:14.993092+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条回应。核心结论：两位 Reviewer 在 θ 敏感性、模型规模限制、filtering 泛化不足三个问题上高度一致，评分相同（3.5）。主要补充分歧点是我更强调 Qwen 过度代表，R1 更关注 DPI→AUC 理论地位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2386 · 2026-05-22T07:27:19.559197+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 183

## Round 183

14 recorded events


### User

_source line 2387 · 2026-05-22T07:27:38.019222+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Qwen 过度代表与结论泛化性**

同意这是一个表述上需要改进的问题。按 family 统计：
- K\*=2 的 6/10 配置中，4 个来自 Qwen 家族，2 个来自非 Qwen（LLaMA-3.1-8B、Pythia-1.4B）
- K\*=1 的 4/10 配置覆盖 4 个不同家族（OLMo、Mistral、Gemma、Pythia-6.9B）
- 按 family 统计，仅 2/6 家族 unanimously K\*=2（Qwen 4/4，LLaMA 1/1），3/6 unanimously K\*=1

Abstract 的 "6/10 configurations" 确实技术上正确但给读者的印象偏乐观。不过我要补充一点 R2 未提及的：**即使 K\*=1 的配置也确认了论文的核心叙事——boundary 极浅（≤2）**。K\*∈{1,2} 的变化范围远小于可能的 K∈{1,...,5}，"一次洗白"效应的定性结论（一次生成后信号快速衰减）在所有配置中都成立。建议作者在正文 Section 4.1 添加 family-level 汇总表，但无需降级核心发现。

---

**[AGREE] R2-N2: θ=0.60 敏感性**

与我的 W3 一致。补充两个 R2 未提到的观察：

1. Qwen-cont 的 1v2 AUC = 0.611，CI 下界仅超 θ 0.002（Limitations (4)），这意味着该配置实质上处于 K\*=1 和 K\*=2 的判定边界上。任何 θ 的微调或 seed 的变化都可能翻转结论。
2. Cohen's h=0.20 → θ=0.60 的映射假设 null AUC=0.50，但 permutation test 给出的 95th percentile null 是 <0.55（Section 3.1），这意味着实际的 null baseline 比理论预期高。如果以 permutation null 校准，θ 应该在 0.55 附近而非 0.60，这会让更多配置达到 K\*=2 甚至 K\*=3。

R2 建议报告 θ-free 指标（如 AUC gap 显著性）是好的解决方案。我进一步建议：报告每个 adjacent pair 的 AUC 值和 CI 即可，让读者根据自己的应用场景选择 θ（论文已在 Table 2 中提供了这些数据，但应在 Discussion 中更明确地鼓励这种读法）。

---

**[REBUT] R2-N3: Prompt-chain 的生态有效性**

R2 认为 retrain-chain K\*≥4 意味着 prompt-chain K\*=2 的 "one-wash laundering" 是 prompt-chain 特有现象，现实 contamination 涉及 retrain-chain，因此核心发现缺乏生态有效性。我不完全同意，理由如下：

1. **论文已明确区分两种协议的适用场景**（Section 6, Limitations (2)）：retrain-chain 的高 K\* 来自"cumulative model-adaptation artifacts（vocabulary narrowing, repetition bias）"，是**模型层面**的信号而非**文本层面**的信号。对于 data curation 的使用场景（"给定一段文本，判断它的生成深度"），只有 prompt-chain 是相关的——你无法从文本本身推断它是否来自 retrain-chain。

2. **现实 contamination 的主流路径是 prompt-chain 而非 retrain-chain**：web-scale 污染的典型机制是 LLM 生成内容→发布到网上→被新一轮 crawl 收入训练集→模型在训练集上继续生成。每一步的"生成"是通过 prompt 进行的（API 调用），而非通过 fine-tuning 整个模型。Full retrain-chain（在前一代输出上重新训练整个模型）是 model collapse 理论论文的实验设置，在实际 web contamination 中极其罕见。

3. **不过我同意 R2 的措辞建议**：论文应将 "one-wash laundering" 的表述明确限定为 prompt-chain 场景。例如："Under prompt-chain generation—the protocol most relevant to web-scale data curation—a single generation pass suffices to render text indistinguishable from deeper synthetic content." 当前 abstract 的表述（"a one-wash laundering effect"）缺乏这一限定。

因此我的判断是：R2-N3 不应是 Must-Fix（核心设计选择是合理的），但表述需要限定——建议降级为 Should-Fix，要求在 abstract 和 conclusion 中添加 "prompt-chain" 限定语。

---

### Should-Fix 问题

**[AGREE] R2-W1: Filtering 实验仅 Qwen-1.5B 单一配置**

与我的审稿意见一致（我未单独列出但在 Q4 中提出了相同问题）。论文在 Limitations 中承认了这一点。关键缺口是：对 K\*=1 的配置（如 OLMo-1B），binary filtering 是否仍然有效？如果 K\*=1 意味着连 depth-1 和 depth-2 都不可区分，那么 binary filtering 退化为"human vs. any machine"的简单二分——这和现有 binary detection 文献有什么区别？至少需在正文 Section 5 中讨论这一点。

---

**[REBUT] R2-W2: K\*=2 的新贡献 vs binary detection**

R2 认为如果结论是"binary is sufficient"，论文相对已有 binary detection 文献的增量贡献不明确。我不同意：

1. **K\*_empirical=2 解释了 binary detection 为何有效**：已有文献证明 binary（human vs. machine）detection 效果好，但没有人解释过为什么。K\*=2 提供了答案：因为 discrimination boundary 就在 depth 2，超过 depth 2 的代际间差异已不可区分。这是描述性科学（descriptive science），即使实用结论与 binary detection 一致，认识论价值不同。

2. **K\*_empirical=2 排除了 graduated 方法的必要性**：在 K\*=2 的条件下，论文证明了 graduated weighting/filtering 策略不如 binary 策略（Table 5, Figure 5）。这个结论并非显而易见——在 K\*=3 的 arXiv 场景中（Table 4），graduated 策略可能有空间优势。K\*_empirical 为策略选择提供了理论依据。

3. **K\*_empirical 提供了跨域的差异化预测**：C4/Wikipedia K\*=2 vs arXiv K\*=3，这意味着结构化学术文本的 contamination 更容易被追踪到更深层级。Binary detection 无法给出这种域差异化的粒度。

因此 K\*_empirical 的贡献不仅是实用策略（binary filtering），更是一个**度量框架**，能区分不同域、模型、解码策略的 contamination 可追溯性。

---

**[AGREE] R2-W3: >8B 模型风险**

与我的 N2 一致。K\*可能随模型规模增大而变化（方向不确定），这一风险应在 Conclusion 中更明确反映。

---

**[AGREE] R2-W4: 遗漏 Suresh et al. (2024)**

如果该文献确实讨论了 recursive training 中 model collapse 的**速率**（rate），那么与本文的 K\*_empirical（测量 discrimination boundary 的深度）直接相关。建议作者在 Related Work 中补充引用并讨论两个 "rate" 概念的关系。

对于 R2 提到的其他 missing references：
- Borji (2024) "A Note on Shumailov et al."：如果只是对 Shumailov 的评论/回应，相关性有限，可引可不引。
- Dugan et al. (ACL 2024) "RAID" benchmark：RAID 是一个 machine-generated text detection benchmark，与 depth estimation 有间接关系。建议引用但非必须。

---

### 小问题

**[AGREE]** Abstract 中 "Cohen's h≈0.20" 确实缺乏上下文——大多数 NLP 读者不熟悉 Cohen's h，建议替换为更直观的表述（如 "a conventional small-effect-size threshold"，将技术细节移至 Section 3.1）。

**[AGREE]** Table 2 视觉高亮 K\* boundary 行是好建议，能帮助读者快速定位 boundary pair。

**[AGREE]** self-BLEU 在 deployment 中的计算方式需要澄清——论文在 Section 3.2 提到"in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss"，但这句话被埋在段落中，应更突出。

**[REBUT]** Limitations (6) 关于 512 tokens boundary 减弱：这已在 Limitations 中详细说明，且减弱幅度极小（CI 下界 0.5979 vs θ=0.60，差 0.002）。在正文中提及会分散 8 页有限空间中对核心发现的叙述。Appendix 中的完整数据已足够。

---

### Questions

**R2-Q1: 是否有接近 non-monotonic 的 AUC 模式？**

根据我对 Table 2 和 Table 8 的阅读：主实验中所有 10 个配置的 adjacent-pair AUC 均严格单调递减。但有两个"接近"的 case 值得注意：
- Table 8（cross-depth pairs，Qwen-rw）中 3v4 AUC = 0.5409 和 4v5 AUC = 0.5141，差异仅 2.7pp——如果加入噪声（不同 seed），很容易翻转。不过这发生在 threshold 以下（远低于 θ=0.60），对 K\*_empirical 的计算无影响。
- 论文正文（Section 3.1）明确声明单调性是经验观察而非理论保证，这是诚实的处理。

**R2-Q2: Cross-model retrain-chain 下 K\* 预期**

论文未测试此场景，我也无法给出确定答案。但基于论文的 retrain-chain 结果（Pythia-1.4B LoRA, K\*≥4）和 cross-model transfer 结果（Section 4.2, Table 7），可以推测 cross-model retrain-chain 的 K\* 可能介于 prompt-chain（K\*=2）和 same-model retrain-chain（K\*≥4）之间。这是一个有价值的 future work 方向，但不应是当前论文的必做实验。

**[AGREE] R2-Q3: ≤30% contamination 下 K\*-aware filtering 是否无用？**

这是一个尖锐且重要的问题。Appendix D.8 的 dose-response 数据确实表明在 ≤30% contamination 下各策略差异消失（Δ_max = 0.33pp, p > 0.8）。这意味着 K\*-aware filtering 的实际价值仅在高污染率（≥50%）下才体现，而这种极端场景在现实中可能不常见。

不过我认为论文应该做两件事来回应：
1. 在正文 Section 5 或 Discussion 中明确讨论 dose-response 的含义，而非仅放在 Appendix。
2. 强调 K\*_empirical 的价值不仅在 filtering application，更在于作为 contamination 的**诊断工具**——即使不做 filtering，知道 K\*=2 也帮助我们理解 web-scale contamination 的性质和传播极限。

---

### 总结

R2 的审稿整体高质量，多数 concern 与我的审稿意见一致或互补。主要分歧在两处：

1. **N3（prompt-chain 生态有效性）**：我认为论文的 prompt-chain 选择对 data curation 场景是正确的，但同意需在 abstract/conclusion 中限定 "one-wash laundering" 为 prompt-chain 特定结论。建议降级为 Should-Fix。

2. **W2（K\*=2 的新贡献）**：我认为 K\*_empirical 作为度量框架的价值超越了"binary is sufficient"这一结论——它提供了域差异化（C4 vs arXiv）、策略指导（binary vs graduated）和理论解释（为什么 binary detection 有效）。

两位 reviewer 的共同强烈关切：(1) θ 敏感性；(2) >8B 模型覆盖不足；(3) Qwen 过度代表。这三点应成为 revision 的优先事项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2388 · 2026-05-22T07:28:07.069164+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2389 · 2026-05-22T07:28:07.069834+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2390 · 2026-05-22T07:28:10.483879+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool call

_source line 2391 · 2026-05-22T07:28:10.484301+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2392 · 2026-05-22T07:28:10.536220+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T07:15:33.080343+00:00\", \"completed_at\": \"2026-05-22T07:20:17.581086+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前两页为纯文本（Title/Abstract/Intro/Related Work），第一个 display item（Figure 1 pipeline 图）出现在第 3 页。对 ACL 格式论文可接受，但审稿人需翻过 2 页纯文本才看到视觉锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 pipeline 图清晰传达方法流程（Seed Corpus → Recursive Generation → Feature Extraction → OBD Classifier → K* Estimation），作为首个 display item 能帮助审稿人快速建立方法认知，但传达的是流程而非核心结果\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Author/Abstract 排版整洁，符合 ACL 匿名投稿格式\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本（无 figure/table/equation 穿插）。虽然 Intro+Related Work 段落天然文字密集，但可考虑将 Figure 1 前移至第 2 页或 Intro 末尾以提早建立视觉锚点\"}, {\"severity\": \"info\", \"dimension\": \"page 3-6\", \"message\": \"视觉节奏优秀：Figure 1（p3）→ Table 1 + Figure 2 + Figure 3（p4）→ Table 2 + Figure 4 + Table 3（p5）→ Table 4 + Table 5（p6），display items 密集穿插文字\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"结论段纯文本，属正常收尾\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"末页（主正文）包含 Limitations（简短、约 3 点）+ Ethics Statement + References 开头，页面利用率 >80%，合理\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"主正文 8 页包含 4 figures + 5 tables = 9 个 display items（~1.1/页），符合实证为主论文的预期密度\"}, {\"severity\": \"info\", \"dimension\": \"page 10-21\", \"message\": \"Appendix 12 页包含 1 figure + 约 20 tables，内容详实\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 pipeline 图分辨率充足，标注文字清晰可读，caption 自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 AUC 衰减曲线：线条清晰，bootstrap CI shaded band 可辨，θ=0.60 虚线标注明确；Figure 3 sensitivity curve 较小但可读\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 4 heatmap：单
…[truncated 2054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 2393 · 2026-05-22T07:28:10.536703+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2394 · 2026-05-22T07:30:02.101170+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-contamination",
  "issues_yaml": "## Review Issues Tracker — gen-depth-contamination\n## Updated: Round 25 (fresh review, 2026-05-22)\n\n# === CRITICAL / MUST-FIX ===\n\n- id: \"R1-N1\"\n  summary: \"DPI→adjacent-pair AUC 推理链存在逻辑缺口\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"应明确 DPI 是 heuristic motivation 而非 strict proof。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Must-Fix：K*_empirical 作为 K*_theory 下界仅为断言，缺形式证明。R2 同意但建议降为 Should-Fix（论文已承认 AUC≠MI）。共识：需明确区分操作性定义 vs lower bound claim。\"\n  action_items:\n    - round: 25\n      action: \"明确区分 K*_empirical 为操作性定义 vs K*_theory 下界；后者要么形式证明（f-divergence→AUC 不等式）要么降级为 conjecture\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Cohen's h 提供先验基础，但第三条 distributional discontinuity 应标为 post-hoc confirmatory。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"两位 Reviewer 最强共识点。θ∈[0.55,0.70] 内 K* 从 3 变到 1。Qwen-cont CI 下界仅超 θ 0.002。Cohen's h=0.20 是统计惯例非检测理论推导。R1 补充：permutation null 95th percentile <0.55，实际 null 比理论预期高。\"\n  action_items:\n    - round: 25\n      action: \"报告 θ-free 指标（AUC gap 及其 CI），提供完整灵敏度曲线；鼓励读者根据应用场景选择 θ\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C4\"\n  summary: \"模型规模覆盖偏向小模型（≤8B），威胁可推广性\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Qwen 4/10 过度代表；缺 >8B；按家族去重 K*=2 从 6/10 降为 3/6。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Must-Fix：常用生成模型远超 8B，K*≈2 的泛化性未验证。R2 同意。共识：至少在 Abstract/Conclusion 明确限定 1B-8B 适用范围。补充 >30B 实验在 ARR 周期内不太现实。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 显式限定 K*≈2 适用范围为 1B-8B；如可能补充 ≥1 个 >30B 模型实验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N1\"\n  summary: \"Qwen 过度代表使 6/10 统计量误导\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix。6/10 中 4 个 Qwen。按 family：仅 2/6 unanimously K*=2。R1 同意表述需改但指出 K*∈{1,2} 变化范围小，one-wash 定性结论仍成立。\"\n  action_items:\n    - round: 25\n      action: \"Section 4.1 添加 family-level 汇总表；Abstract 同时报告 per-config 和 per-family 统计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING / SHOULD-FIX ===\n\n- id: \"R25-W1\"\n  summary: \"Prompt-chain 生态有效性——one-wash laundering 可能是 prompt-chain 特有现象\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix（retrain-chain K*≥4 远超 prompt-chain K*=2）。R1 REBUT 降级为 Should-Fix：prompt-chain 对 data curation 场景是正确选择（web contamination 主流路径），但同意需在 Abstract/Conclusion 限定 prompt-chain 适用范围。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 添加 prompt-chain 限定语；Introduction 末尾加 retrain-chain 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-C2\"\n  summary: \"Cross-scorer 验证部分证伪 scorer independence claim（Qwen-cont K*=2→1）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Qwen-cont 自身打分 K*=2 仅超 θ 0.002，Pythia/OLMo 打分均 <θ。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Should-Fix：实际部署中 generator 未知，cross-scoring 才是工作条件，K*=2→1 退化为 binary detection。R2 同意并补充 ensemble 也无法解决 marginal signal。\"\n  action_items:\n    - round: 25\n      action: \"Section 4.2 更突出讨论 cross-scorer 降级对部署的影响；探讨 scorer-ensemble 策略\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Filtering 实验效果量在现实污染比例下极小\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"≤50% 污染下所有策略无显著差异。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"+0.74pp MMLU, +0.03pp HellaSwag 在 100% 合成极端条件下。Appendix D.8 ≤30% 策略差异消失。R1 建议正文讨论 dose-response。R2 同意。\"\n  action_items:\n    - round: 25\n      action: \"Section 5 或 Discussion 正文引用 dose-response 分析；承认现实污染比例下边际增益可忽略\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W11\"\n  summary: \"Filtering 仅在单一 generator（Qwen-1.5B cont）上验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"至少应在 K*=1 generator 上重复或在 Limitations 中声明。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix，R1 同意。K*=1 配置下 binary filtering 是否退化为普通 binary detection？\"\n  action_items:\n    - round: 25\n      action: \"至少在 Limitations 声明 filtering 仅单 generator 验证；Section 5 讨论 K*=1 场景\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"K*=2 的实际新贡献 vs binary detection 讨论不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix：如果结论是 binary is sufficient，增量贡献不明确。R1 REBUT：K* 提供解释性价值（为什么 binary 有效）、域差异化（C4 vs arXiv）、策略指导（binary vs graduated）。分歧未完全解决。\"\n  action_items:\n    - round: 25\n      action: \"Discussion 更明确阐述 K*_empirical 作为度量框架相对于 binary detection 的增量贡献\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"扩展至 5-7 句。\"\n    - round: 25\n      reviewer: []\n      note: \"本轮未单独提及，可能已部分改善，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"与 Geng et al. (2026) 和 Wang et al. (2025) 的技术区分不够清晰\"\n  category: related_work\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"缺 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025)。\"\n    - round: 25\n      reviewer: []\n      note: \"本轮未单独提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R2]\n      note: \"Reviewer 有分歧，R1 认为正常。\"\n    - round: 25\n      reviewer: [R2]\n      note: \"R2 提到 Abstract 中 Cohen's h≈0.20 缺乏上下文，R1 同意应替换为更直观表述。\"\n  action_items:\n    - round: 25\n      action: \"Abstract 中 Cohen's h 替换为直观表述，技术细节移至 Section 3.1\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === MINOR ===\n\n- id: \"R25-M1\"\n  summary: \"正文缺少 Mistral-7B 和 Gemma-2-2B 数据覆盖\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"Table 2 仅列 5 配置但声称 10，正文缺少这些额外配置的概述。R1-M2。\"\n  action_items:\n    - round: 25\n      action: \"正文 Section 4.1 添加 1-2 句概述全部 10 配置结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M3\"\n  summary: \"K*_empirical 定义中 max 算子隐含 AUC 单调递减假设\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"明确单调假设或改用连续满足条件定义。\"\n    - round: 25\n      reviewer: [R1]\n      note: \"主实验 10 配置均严格单调递减，但 threshold 以下有接近翻转的 case（Qwen-rw 3v4=0.541, 4v5=0.514，差仅 2.7pp）。\"\n  action_items:\n    - round: 25\n      action: \"Eq.1 后明确声明单调性为经验观察\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"遗漏 Suresh et al. (2024) Rate of Model Collapse\"\n  category: related_work\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 提出，R1 同意。讨论 recursive training collapse rate 与 K*_empirical discrimination boundary 的关系。\"\n  action_items:\n    - round: 25\n      action: \"Related Work 补充 Suresh et al. (2024) 引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"Figure 1 中 K* Estimation 步骤箭头指向不清\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1]\n      note: \"读者可能困惑 K* 是从单个文档还是语料库层面估计。\"\n  action_items:\n    - round: 25\n      action: \"Figure 1 标注明确 K* 为语料库层面估计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M4\"\n  summary: \"Table 2 需视觉高亮 K* boundary 行\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R2]\n      note: \"帮助读者快速定位 boundary pair。R1 同意。\"\n  action_items:\n    - round: 25\n      action: \"Table 2 高亮 boundary 行\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M5\"\n  summary: \"self-BLEU 在 deployment 场景的计算方式需澄清\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R2]\n      note: \"Section 3.2 提到可用 corpus-level self-similarity 替代，但信息被埋在段落中。R1 同意应更突出。\"\n  action_items:\n    - round: 25\n      action: \"更突出说明 deployment 下 self-BLEU 替代方案\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M4\"\n  summary: \"Figure 4 热图红绿配色对色盲不友好\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 25\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M2\"\n  summary: \"Orphan bib entries / 引用格式不一致\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 25\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === RESOLVED (from prior rounds) ===\n\n- id: \"R2-N1\"\n  summary: \"Abstract 对迁移结果选择性报告\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Abstract 已包含边界迁移失败信息\"\n  resolution_round: 23\n\n- id: \"R2-M1\"\n  summary: \"holtzman2020curious orphan bib 条目\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"已删除\"\n  resolution_round: 21\n\n- id: \"R20-M4\"\n  summary: \"'model-free' 表述已改为 'generator-independent'\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"已全文替换\"\n  resolution_round: 21\n\n- id: \"R2-W2\"\n  summary: \"混合场景（prompt-chain + retrain-chain）未讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已加 Mixed-chain 段落\"\n  resolution_round: 21\n\n- id: \"R1-N3\"\n  summary: \"Qwen 家族 5/10 配置偏重，'7/9' 统计量误导\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已修改 framing 为 '4/6 families' primary\"\n  resolution_round: 21\n\n- id: \"R2-N2\"\n  summary: \"遗漏 Wang et al. (ACL 2025) 相关工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已添加引用\"\n  resolution_round: 21\n\n- id: \"R2-N3\"\n  summary: \"'One-wash laundering' framing 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已重写\"\n  resolution_round: 21\n\n- id: \"R22-Q6\"\n  summary: \"Generator identity AUC 数值不一致\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"数值已统一\"\n  resolution_round: 23\n\n- id: \"R24-C1\"\n  summary: \"附录空占位符表格\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  resolution: \"Round 25 审稿未发现空表问题，视觉审查确认 20+ 表格均有数据\"\n  resolution_round: 25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-contamination",
    "issues_yaml": "## Review Issues Tracker — gen-depth-contamination\n## Updated: Round 25 (fresh review, 2026-05-22)\n\n# === CRITICAL / MUST-FIX ===\n\n- id: \"R1-N1\"\n  summary: \"DPI→adjacent-pair AUC 推理链存在逻辑缺口\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"应明确 DPI 是 heuristic motivation 而非 strict proof。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Must-Fix：K*_empirical 作为 K*_theory 下界仅为断言，缺形式证明。R2 同意但建议降为 Should-Fix（论文已承认 AUC≠MI）。共识：需明确区分操作性定义 vs lower bound claim。\"\n  action_items:\n    - round: 25\n      action: \"明确区分 K*_empirical 为操作性定义 vs K*_theory 下界；后者要么形式证明（f-divergence→AUC 不等式）要么降级为 conjecture\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Cohen's h 提供先验基础，但第三条 distributional discontinuity 应标为 post-hoc confirmatory。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"两位 Reviewer 最强共识点。θ∈[0.55,0.70] 内 K* 从 3 变到 1。Qwen-cont CI 下界仅超 θ 0.002。Cohen's h=0.20 是统计惯例非检测理论推导。R1 补充：permutation null 95th percentile <0.55，实际 null 比理论预期高。\"\n  action_items:\n    - round: 25\n      action: \"报告 θ-free 指标（AUC gap 及其 CI），提供完整灵敏度曲线；鼓励读者根据应用场景选择 θ\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C4\"\n  summary: \"模型规模覆盖偏向小模型（≤8B），威胁可推广性\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Qwen 4/10 过度代表；缺 >8B；按家族去重 K*=2 从 6/10 降为 3/6。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Must-Fix：常用生成模型远超 8B，K*≈2 的泛化性未验证。R2 同意。共识：至少在 Abstract/Conclusion 明确限定 1B-8B 适用范围。补充 >30B 实验在 ARR 周期内不太现实。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 显式限定 K*≈2 适用范围为 1B-8B；如可能补充 ≥1 个 >30B 模型实验\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N1\"\n  summary: \"Qwen 过度代表使 6/10 统计量误导\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix。6/10 中 4 个 Qwen。按 family：仅 2/6 unanimously K*=2。R1 同意表述需改但指出 K*∈{1,2} 变化范围小，one-wash 定性结论仍成立。\"\n  action_items:\n    - round: 25\n      action: \"Section 4.1 添加 family-level 汇总表；Abstract 同时报告 per-config 和 per-family 统计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING / SHOULD-FIX ===\n\n- id: \"R25-W1\"\n  summary: \"Prompt-chain 生态有效性——one-wash laundering 可能是 prompt-chain 特有现象\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix（retrain-chain K*≥4 远超 prompt-chain K*=2）。R1 REBUT 降级为 Should-Fix：prompt-chain 对 data curation 场景是正确选择（web contamination 主流路径），但同意需在 Abstract/Conclusion 限定 prompt-chain 适用范围。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 添加 prompt-chain 限定语；Introduction 末尾加 retrain-chain 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-C2\"\n  summary: \"Cross-scorer 验证部分证伪 scorer independence claim（Qwen-cont K*=2→1）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Qwen-cont 自身打分 K*=2 仅超 θ 0.002，Pythia/OLMo 打分均 <θ。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Should-Fix：实际部署中 generator 未知，cross-scoring 才是工作条件，K*=2→1 退化为 binary detection。R2 同意并补充 ensemble 也无法解决 marginal signal。\"\n  action_items:\n    - round: 25\n      action: \"Section 4.2 更突出讨论 cross-scorer 降级对部署的影响；探讨 scorer-ensemble 策略\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Filtering 实验效果量在现实污染比例下极小\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"≤50% 污染下所有策略无显著差异。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"+0.74pp MMLU, +0.03pp HellaSwag 在 100% 合成极端条件下。Appendix D.8 ≤30% 策略差异消失。R1 建议正文讨论 dose-response。R2 同意。\"\n  action_items:\n    - round: 25\n      action: \"Section 5 或 Discussion 正文引用 dose-response 分析；承认现实污染比例下边际增益可忽略\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W11\"\n  summary: \"Filtering 仅在单一 generator（Qwen-1.5B cont）上验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"至少应在 K*=1 generator 上重复或在 Limitations 中声明。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix，R1 同意。K*=1 配置下 binary filtering 是否退化为普通 binary detection？\"\n  action_items:\n    - round: 25\n      action: \"至少在 Limitations 声明 filtering 仅单 generator 验证；Section 5 讨论 K*=1 场景\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W2\"\n  summary: \"K*=2 的实际新贡献 vs binary detection 讨论不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix：如果结论是 binary is sufficient，增量贡献不明确。R1 REBUT：K* 提供解释性价值（为什么 binary 有效）、域差异化（C4 vs arXiv）、策略指导（binary vs graduated）。分歧未完全解决。\"\n  action_items:\n    - round: 25\n      action: \"Discussion 更明确阐述 K*_empirical 作为度量框架相对于 binary detection 的增量贡献\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"扩展至 5-7 句。\"\n    - round: 25\n      reviewer: []\n      note: \"本轮未单独提及，可能已部分改善，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"与 Geng et al. (2026) 和 Wang et al. (2025) 的技术区分不够清晰\"\n  category: related_work\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 24\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"缺 Wang et al. (ACL 2025) 和 Fu et al. (ICLR 2025)。\"\n    - round: 25\n      reviewer: []\n      note: \"本轮未单独提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R2]\n      note: \"Reviewer 有分歧，R1 认为正常。\"\n    - round: 25\n      reviewer: [R2]\n      note: \"R2 提到 Abstract 中 Cohen's h≈0.20 缺乏上下文，R1 同意应替换为更直观表述。\"\n  action_items:\n    - round: 25\n      action: \"Abstract 中 Cohen's h 替换为直观表述，技术细节移至 Section 3.1\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === MINOR ===\n\n- id: \"R25-M1\"\n  summary: \"正文缺少 Mistral-7B 和 Gemma-2-2B 数据覆盖\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"Table 2 仅列 5 配置但声称 10，正文缺少这些额外配置的概述。R1-M2。\"\n  action_items:\n    - round: 25\n      action: \"正文 Section 4.1 添加 1-2 句概述全部 10 配置结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M3\"\n  summary: \"K*_empirical 定义中 max 算子隐含 AUC 单调递减假设\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"明确单调假设或改用连续满足条件定义。\"\n    - round: 25\n      reviewer: [R1]\n      note: \"主实验 10 配置均严格单调递减，但 threshold 以下有接近翻转的 case（Qwen-rw 3v4=0.541, 4v5=0.514，差仅 2.7pp）。\"\n  action_items:\n    - round: 25\n      action: \"Eq.1 后明确声明单调性为经验观察\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M2\"\n  summary: \"遗漏 Suresh et al. (2024) Rate of Model Collapse\"\n  category: related_work\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 提出，R1 同意。讨论 recursive training collapse rate 与 K*_empirical discrimination boundary 的关系。\"\n  action_items:\n    - round: 25\n      action: \"Related Work 补充 Suresh et al. (2024) 引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M3\"\n  summary: \"Figure 1 中 K* Estimation 步骤箭头指向不清\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R1]\n      note: \"读者可能困惑 K* 是从单个文档还是语料库层面估计。\"\n  action_items:\n    - round: 25\n      action: \"Figure 1 标注明确 K* 为语料库层面估计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M4\"\n  summary: \"Table 2 需视觉高亮 K* boundary 行\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R2]\n      note: \"帮助读者快速定位 boundary pair。R1 同意。\"\n  action_items:\n    - round: 25\n      action: \"Table 2 高亮 boundary 行\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-M5\"\n  summary: \"self-BLEU 在 deployment 场景的计算方式需澄清\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 25\n  last_seen_round: 25\n  mentions:\n    - round: 25\n      reviewer: [R2]\n      note: \"Section 3.2 提到可用 corpus-level self-similarity 替代，但信息被埋在段落中。R1 同意应更突出。\"\n  action_items:\n    - round: 25\n      action: \"更突出说明 deployment 下 self-BLEU 替代方案\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M4\"\n  summary: \"Figure 4 热图红绿配色对色盲不友好\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - round: 25\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R23-M2\"\n  summary: \"Orphan bib entries / 引用格式不一致\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - round: 25\n      reviewer: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# === RESOLVED (from prior rounds) ===\n\n- id: \"R2-N1\"\n  summary: \"Abstract 对迁移结果选择性报告\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Abstract 已包含边界迁移失败信息\"\n  resolution_round: 23\n\n- id: \"R2-M1\"\n  summary: \"holtzman2020curious orphan bib 条目\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"已删除\"\n  resolution_round: 21\n\n- id: \"R20-M4\"\n  summary: \"'model-free' 表述已改为 'generator-independent'\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"已全文替换\"\n  resolution_round: 21\n\n- id: \"R2-W2\"\n  summary: \"混合场景（prompt-chain + retrain-chain）未讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已加 Mixed-chain 段落\"\n  resolution_round: 21\n\n- id: \"R1-N3\"\n  summary: \"Qwen 家族 5/10 配置偏重，'7/9' 统计量误导\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已修改 framing 为 '4/6 families' primary\"\n  resolution_round: 21\n\n- id: \"R2-N2\"\n  summary: \"遗漏 Wang et al. (ACL 2025) 相关工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已添加引用\"\n  resolution_round: 21\n\n- id: \"R2-N3\"\n  summary: \"'One-wash laundering' framing 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已重写\"\n  resolution_round: 21\n\n- id: \"R22-Q6\"\n  summary: \"Generator identity AUC 数值不一致\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"数值已统一\"\n  resolution_round: 23\n\n- id: \"R24-C1\"\n  summary: \"附录空占位符表格\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  resolution: \"Round 25 审稿未发现空表问题，视觉审查确认 20+ 表格均有数据\"\n  resolution_round: 25"
  }
}
```

</details>

---


### Tool result

_source line 2395 · 2026-05-22T07:30:02.203276+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml\", \"bytes\": 12873}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2396 · 2026-05-22T07:33:49.171108+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 25 审稿报告 — gen-depth-contamination\n\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审稿模式**: Fresh（初审）\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+Related Work）\n**轮次**: 1 轮（Round 1 后交叉分享达成共识，无需下一轮）\n\n---\n\n## Summary\n\n本文提出\"生成深度估计\"（generational depth estimation）问题，使用 15 维统计特征 + OBD-LightGBM 分类器测量递归合成文本的可区分代际边界 K*_empirical。在 10 个模型配置（6 家族, 1B–8B）、3 个域、4 种解码策略上实验表明：web 文本 K*_empirical∈{1,2}（6/10 配置为 2），arXiv K*_empirical=3。核心发现为\"一次洗白\"效应：一次生成后文本即与更深层合成内容不可区分。下游验证表明 binary filtering 最优，与 K*=2 的预测一致。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **问题定义新颖且有实际动机**：generational depth estimation 是此前未被正式定义的问题，K*_empirical 填补了 binary detection 和 model collapse 文献之间的概念空白。\"一次洗白\"效应对数据 curation 社区有直接参考价值。\n\n**S2** [R1+R2 共识] **实验设计严谨**：5-fold GroupKFold（按 seed document 分组）防止数据泄漏；self-BLEU 的 fold-internal 计算消除信息泄漏风险；bootstrap CI + permutation test + ANOVA 三重统计验证；10,000 次 permutation test 提供充分的 null distribution 估计。\n\n**S3** [R1+R2 共识] **实验覆盖度极高**：10 个模型配置 × 4 种解码策略 × 3 个域 + 大量消融（segment length, seed robustness, dose-response, decoding strategy, LLM zero-shot comparison, neural probe, cross-scorer, cross-model transfer）。附录 21 个表格 + 5 个图。\n\n**S4** [R1] **Cross-model transfer 实用性**：15D 统计特征实现 80–100% 跨模型准确率保留（Pythia↔OLMo 90–92%），feature ranking 跨 scorer 高度一致（ρ>0.90），增强了方法的实际部署前景。\n\n**S5** [R1+R2 共识] **Limitations 极其彻底**：7 条具体限制覆盖了规模、协议、阈值、边界脆弱性、特征集依赖、segment length、curation 适用性。诚实程度超出同类工作。\n\n**S6** [R1] **统计实践规范**：effect size（Cohen's h）、bootstrap CI、permutation p-value、ANOVA 交互效应分析齐备，是 NLP 实证研究的良好示范。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1** [R1-N2 + R2-N2, 双方最强共识] **θ=0.60 阈值敏感性高，K*_empirical 作为可操作量稳健性不足**\n- θ∈[0.55, 0.70] 范围内 K* 从 3 变化到 1。Qwen-cont 1v2 CI 下界仅超 θ 0.002。\n- Cohen's h=0.20 → θ=0.60 的映射假设 null AUC=0.50，但 permutation test 95th percentile null <0.55，实际 null 高于理论预期。\n- 核心问题：K*_empirical=2 这一关键结论在 θ 微调时不稳定，论文未提供 θ-free 的表述方式。\n- **要求**：(a) 报告 θ-free 指标（AUC gap 及其 CI），提供完整灵敏度曲线；(b) 在 Discussion 中明确鼓励读者根据应用场景选择 θ；(c) 第三条证据（distributional discontinuity）标为 post-hoc confirmatory。\n\n**C2** [R1-N2 + R2-W3, 共识] **模型规模覆盖仅 ≤8B，核心结论 K*≈2 的泛化性未验证**\n- 全部 10 配置为 1B–8B。当前主流模型（Llama-70B, GPT-4 等）远超此范围。\n- 已有内部证据（0v1 JSD 从 ≤1.5B 的 0.15–0.27 降至 8B 的 0.077；Pythia 1.4B→6.9B K* 从 2→1）暗示规模增大可能降低 K*。\n- Abstract 和 Conclusion 中 K*≈2 被呈现为通用结论，但实际适用范围仅 ≤8B。\n- **要求**：Abstract/Conclusion 显式限定 \"1B–8B\" 适用范围。如可能，补充 ≥1 个 >30B 模型实验。\n\n**C3** [R2-N1 + R1 同意, 共识] **Qwen 过度代表使 \"6/10\" 统计量误导**\n- 6/10 K*=2 配置中 4 个来自 Qwen。按 family 统计：仅 2/6 家族 unanimously K*=2（Qwen 4/4, LLaMA 1/1），3/6 unanimously K*=1（OLMo, Mistral, Gemma）。\n- Abstract \"6/10 configurations\" 技术正确但给读者过于乐观的印象。\n- R1 补充：即使 K*=1 的配置也确认 boundary 极浅（≤2），one-wash 定性结论在所有配置成立。\n- **要求**：(a) Section 4.1 添加 family-level 汇总表；(b) Abstract 同时报告 per-config 和 per-family 统计。\n\n**C4** [R1-N1 + R2 同意] **DPI→AUC 推理链仅为启发式，K*_empirical 作为 lower bound 的理论地位不清**\n- 论文以 DPI（MI 单调递减）motivate 期望 AUC 单调递减，但坦承 \"AUC and mutual information are not formally equivalent\"。K*_empirical 是 K*_theory 的 \"lower bound\" 仅为断言。\n- R2 认为可降级为 Should-Fix（论文已诚实承认），R1 坚持 Must-Fix（这是全文理论框架根基）。\n- **Director 判定**：Must-Fix（修改难度低但影响核心叙事完整性）。\n- **要求**：明确区分 K*_empirical 为操作性定义 vs K*_theory 下界两个 claim；对 lower bound claim 要么给出形式证明要么降级为 conjecture。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R2-N3, R1 部分反驳→降级] **Prompt-chain 生态有效性需限定**\n- Retrain-chain K*≥4（Appendix D.7），\"one-wash laundering\" 可能是 prompt-chain 特有现象。\n- R1 辩护：prompt-chain 是 web-scale contamination 主流路径（API 调用→发布→收录），retrain-chain 在实际 web contamination 中罕见。论文选择合理，但表述缺乏限定。\n- **要求**：Abstract/Conclusion 添加 \"under prompt-chain generation\" 限定语。\n\n**W2** [R1-W1 + R2 同意] **Cross-scorer 降级暴露部署局限**\n- Qwen-cont cross-scoring AUC=0.5923(Pythia)/0.5858(OLMo) 均 <θ，K*=2→1。\n- 实际部署中 generator 身份未知，cross-scoring 才是工作条件。K*=2→1 意味着退化为 binary detection。\n- **要求**：Section 4.2 更突出讨论此限制；探讨 scorer-ensemble 策略。\n\n**W3** [R1-W2 + R2 同意] **Filtering 效果量小且 dose-response 未在正文讨论**\n- +0.74pp MMLU, +0.03pp HellaSwag（100% 合成极端条件下）。\n- Appendix D.8：≤30% contamination 下所有策略差异消失（p>0.8）。\n- 论文已定位为 consistency check，但正文未引用 dose-response，读者可能高估实际价值。\n- **要求**：Section 5 或 Discussion 引用 dose-response 分析，承认现实污染比例下边际增益可忽略。\n\n**W4** [R2-W1 + R1 同意] **Filtering 仅在单一 generator 验证**\n- 仅 Qwen-1.5B continuation。K*=1 配置下 binary filtering 是否退化为普通 binary detection 未讨论。\n- **要求**：Limitations 声明，Section 5 讨论 K*=1 场景。\n\n**W5** [R2-W2, R1 反驳] **K*=2 相对 binary detection 的增量贡献讨论不足**（Reviewer 分歧）\n- R2：结论 \"binary is sufficient\" 使增量贡献不明确。\n- R1 反驳：K* 提供解释性价值（为什么 binary 有效）、域差异化（C4 vs arXiv）、策略指导（binary vs graduated），是度量框架而非仅实用策略。\n- **Director 判定**：保留为 Should-Fix。Discussion 应更明确阐述 K*_empirical 的认识论贡献。\n\n### Minor\n\n**M1** [R1+R2] 正文缺少 Mistral-7B、Gemma-2-2B 数据覆盖——Section 4.1 应添加 1-2 句概述全部 10 配置结果。\n**M2** [R2+R1 同意] 遗漏 Suresh et al. (2024) \"Rate of Model Collapse\"——Related Work 应补充。\n**M3** [R2+R1 同意] Abstract \"Cohen's h≈0.20\" 缺乏上下文——替换为直观表述，技术细节移至 Section 3.1。\n**M4** [R1] Figure 1 中 K* Estimation 步骤箭头指向不清——应标注为语料库层面估计。\n**M5** [R2+R1 同意] Table 2 应视觉高亮 K* boundary 行。\n**M6** [R2+R1 同意] self-BLEU deployment 替代方案应更突出说明。\n**M7** [R1] Eq.1 后应明确声明 AUC 单调递减为经验观察而非理论保证。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n| 问题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| θ=0.60 敏感性 | W3→升级 Must-Fix | N2 (Must-Fix) | [AGREE] 最强共识 |\n| 模型规模 ≤8B | N2 (Must-Fix) | W3 (Should-Fix) | [AGREE] |\n| Qwen 过度代表 | 同意 R2-N1 | N1 (Must-Fix) | [AGREE] 表述需改 |\n| Cross-scorer 降级 | W1 (Should-Fix) | 同意 R1-W1 | [AGREE] |\n| Filtering 效果量小 | W2 (Should-Fix) | 同意 | [AGREE] |\n| Filtering 单配置 | 同意 R2-W1 | W1 (Should-Fix) | [AGREE] |\n| DPI→AUC 理论缺口 | N1 (Must-Fix) | 同意降为 Should-Fix | [AGREE] 严重性有差异 |\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 判定 |\n|------|---------|---------|---------------|\n| Prompt-chain 生态有效性 | [REBUT] 降级 Should-Fix：prompt-chain 是 web contamination 主流路径 | Must-Fix：retrain-chain K*≥4 说明设定特有 | Should-Fix（R1 论证更有说服力，但同意需限定表述） |\n| K*=2 vs binary detection 贡献 | [REBUT] K* 是度量框架，提供解释性+域差异化价值 | Should-Fix：增量贡献不清 | Should-Fix（分歧记录，双方各有理据） |\n| Rewrite vs continuation 分析 | W4 (Should-Fix)：需更深入分析 | [REBUT] 现有分析在 8 页限制下足够 | Minor（R2 论点合理） |\n| Pythia EOS truncation | M4：34-36% truncation 可能引入长度混淆 | [REBUT] Appendix Table 12 已充分讨论 | Dropped（已有覆盖） |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R1] 更强分类器（fine-tuned transformer encoder）是否会增加 K*_empirical？Neural probe K*=3（Qwen）是否意味着 K*_theory>2，从而削弱\"一次洗白\"叙事的绝对性？\n\n**Q2** [R1] θ=0.60 映射假设 null AUC=0.50，但 permutation null 95th percentile <0.55。能否用 permutation null 直接校准 θ？\n\n**Q3** [R1] Qwen-cont 1v2 AUC=0.611 的 fold 间方差是多少？是否有 fold 中 AUC<θ？\n\n**Q4** [R1+R2] K*=1 模型（OLMo-1B）生成的污染数据下，binary filtering 是否仍有效？此时 K*-aware 的价值是否消失？\n\n**Q5** [R1] arXiv 域 n=2,200 是 per-model 还是两个家族共享？每个深度级别的样本量？\n\n**Q6** [R2] Cross-model retrain-chain（如 Qwen→Pythia→OLMo）下 K* 预期是什么？\n\n**Q7** [R2] Appendix D.8 显示 ≤30% contamination 下策略差异消失——现实中 K*-aware filtering 是否实际无用？\n\n---\n\n## Missing References\n\n| 引用 | 来源 | 重要性 | 共识 |\n|------|------|--------|------|\n| Suresh et al. (2024) \"Rate of Model Collapse in Recursive Training\" | R2 | Should-Cite | R1 同意 |\n| Gehrmann et al. (2019) \"GLTR\" | R1 | Nice-to-Cite | R2 认为已被后续工作覆盖 |\n| Tang et al. (2024) \"The Science of Detecting LLM-Generated Text\" | R1 | Nice-to-Cite | R2 需核实真实性 |\n| Borji (2024) \"A Note on Shumailov et al.\" | R2 | Nice-to-Cite | R1 认为相关性有限 |\n| Dugan et al. (ACL 2024) \"RAID\" benchmark | R2 | Nice-to-Cite | R1 同意但非必须 |\n\n---\n\n## External Review\n\n**状态**: 未请求（项目配置未启用 paperreview.ai）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（0 critical, 8 warning, 19 info）\n\n主要发现：\n- **页面 1-2 纯文本**（warning）：连续 2 页无 display item。建议将 Figure 1 前移至第 2 页。\n- **页面 3-6 视觉节奏优秀**（info）：Figure 1→Table 1+Figure 2+Figure 3→Table 2+Figure 4+Table 3→Table 4+Table 5，display items 密集穿插。\n- **主正文密度**（info）：8 页含 4 figures + 5 tables = 9 个 display items（~1.1/页），符合实证论文预期。\n- **Appendix 空白**（warning×6）：Table 10-13、Table 21-22、Table 26 附近存在显著空白，页面利用率 15%-50%。建议合并小表。\n- **格式合规**（info）：ACL 匿名模板正确，无 LaTeX 残留/margin 溢出/未解析引用，References 格式统一。\n- **Figure 质量**（info）：Figure 1 pipeline 清晰，Figure 2 AUC 衰减曲线带 CI shaded band，Figure 4 heatmap 数值标注清晰。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5（Borderline Conference）**\n\n**对应 EMNLP 2026 ARR 标准**: 3.5 = Borderline Conference（介于可被主会议接收与 Findings 之间）\n\n**R1**: 3.5 | **R2**: 3.5 | **Director 综合**: 3.5\n\n**置信度**: 4/5\n\n### 判定理由\n\n**支持 Conference (4.0) 的因素**：\n- 问题定义新颖，K*_empirical 是一个有清晰动机的新概念\n- 实验设计严谨，统计实践规范，附录极其充分\n- \"One-wash laundering\" 是一个可记忆、可操作的发现\n- Cross-model transfer 增强了方法实用性\n\n**拉低至 3.5 的因素**：\n- θ=0.60 敏感性使核心结论 K*=2 的稳健性存疑（最关键）\n- 模型规模 ≤8B，核心发现的泛化性未验证\n- Qwen 4/10 过度代表，per-family 统计显著弱于 per-config\n- DPI→AUC 理论桥接仅为启发式\n- 下游 filtering 效果量小，现实污染比例下近乎无用\n- Cross-scorer 降级使 K*=2 在部署条件下不稳健\n\n**修改路径建议（不构成审稿意见，仅供参考）**：\n如果作者能 (a) 提供 θ-free 表述和灵敏度曲线，(b) 限定 K*≈2 适用范围（1B–8B, prompt-chain），(c) 添加 per-family 统计，(d) 明确 K*_empirical 的 lower bound 理论条件——则有望达到 4.0 (Conference) 水准。这些修改均不涉及新实验，属于 framing/presentation 层面的改进。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"6/10 configurations\" 应同时报告 per-family 统计（2/6 unanimously K*=2）\n- \"one-wash laundering effect\" 首次出现时应限定为 prompt-chain 场景\n- Retrain-chain K*≥4 的对比应在 Introduction 末尾提及，而非仅在 Discussion\n\n### Section 3 (Method)\n- Eq. 1 后应明确声明 AUC 单调递减为经验观察\n- θ=0.60 的第三条证据（distributional discontinuity）应标为 \"post-hoc confirmatory\"\n- \"lower bound on K*_theory\" claim 需形式化或降级\n\n### Section 4 (Experiments)\n- 4.1: 添加 family-level 汇总表，正文覆盖全部 10 配置\n- 4.2: Cross-scorer 降级的部署影响需更突出讨论\n- Table 2: 高亮 boundary 行\n\n### Section 5 (Filtering)\n- 正文引用 dose-response 分析（Appendix D.8）\n- 承认 ≤30% contamination 下策略差异消失\n- 讨论 K*=1 场景下 filtering 是否退化\n\n### Section 6 (Discussion)\n- K*_empirical 作为度量框架（vs 仅作为 binary detection 副产品）的价值需更明确阐述\n- Prompt-chain vs retrain-chain 的适用范围需更清晰界定\n\n### Section 7 (Conclusion)\n- 显式限定 \"1B–8B\" 和 \"prompt-chain\" 适用范围\n- 补充 per-family 统计\n\n### Abstract\n- \"Cohen's h≈0.20\" 替换为直观表述\n- 同时报告 per-config 和 per-family 统计\n- 添加 prompt-chain 限定语",
  "project": "gen-depth-contamination",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 25 审稿报告 — gen-depth-contamination\n\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审稿模式**: Fresh（初审）\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+Related Work）\n**轮次**: 1 轮（Round 1 后交叉分享达成共识，无需下一轮）\n\n---\n\n## Summary\n\n本文提出\"生成深度估计\"（generational depth estimation）问题，使用 15 维统计特征 + OBD-LightGBM 分类器测量递归合成文本的可区分代际边界 K*_empirical。在 10 个模型配置（6 家族, 1B–8B）、3 个域、4 种解码策略上实验表明：web 文本 K*_empirical∈{1,2}（6/10 配置为 2），arXiv K*_empirical=3。核心发现为\"一次洗白\"效应：一次生成后文本即与更深层合成内容不可区分。下游验证表明 binary filtering 最优，与 K*=2 的预测一致。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **问题定义新颖且有实际动机**：generational depth estimation 是此前未被正式定义的问题，K*_empirical 填补了 binary detection 和 model collapse 文献之间的概念空白。\"一次洗白\"效应对数据 curation 社区有直接参考价值。\n\n**S2** [R1+R2 共识] **实验设计严谨**：5-fold GroupKFold（按 seed document 分组）防止数据泄漏；self-BLEU 的 fold-internal 计算消除信息泄漏风险；bootstrap CI + permutation test + ANOVA 三重统计验证；10,000 次 permutation test 提供充分的 null distribution 估计。\n\n**S3** [R1+R2 共识] **实验覆盖度极高**：10 个模型配置 × 4 种解码策略 × 3 个域 + 大量消融（segment length, seed robustness, dose-response, decoding strategy, LLM zero-shot comparison, neural probe, cross-scorer, cross-model transfer）。附录 21 个表格 + 5 个图。\n\n**S4** [R1] **Cross-model transfer 实用性**：15D 统计特征实现 80–100% 跨模型准确率保留（Pythia↔OLMo 90–92%），feature ranking 跨 scorer 高度一致（ρ>0.90），增强了方法的实际部署前景。\n\n**S5** [R1+R2 共识] **Limitations 极其彻底**：7 条具体限制覆盖了规模、协议、阈值、边界脆弱性、特征集依赖、segment length、curation 适用性。诚实程度超出同类工作。\n\n**S6** [R1] **统计实践规范**：effect size（Cohen's h）、bootstrap CI、permutation p-value、ANOVA 交互效应分析齐备，是 NLP 实证研究的良好示范。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1** [R1-N2 + R2-N2, 双方最强共识] **θ=0.60 阈值敏感性高，K*_empirical 作为可操作量稳健性不足**\n- θ∈[0.55, 0.70] 范围内 K* 从 3 变化到 1。Qwen-cont 1v2 CI 下界仅超 θ 0.002。\n- Cohen's h=0.20 → θ=0.60 的映射假设 null AUC=0.50，但 permutation test 95th percentile null <0.55，实际 null 高于理论预期。\n- 核心问题：K*_empirical=2 这一关键结论在 θ 微调时不稳定，论文未提供 θ-free 的表述方式。\n- **要求**：(a) 报告 θ-free 指标（AUC gap 及其 CI），提供完整灵敏度曲线；(b) 在 Discussion 中明确鼓励读者根据应用场景选择 θ；(c) 第三条证据（distributional discontinuity）标为 post-hoc confirmatory。\n\n**C2** [R1-N2 + R2-W3, 共识] **模型规模覆盖仅 ≤8B，核心结论 K*≈2 的泛化性未验证**\n- 全部 10 配置为 1B–8B。当前主流模型（Llama-70B, GPT-4 等）远超此范围。\n- 已有内部证据（0v1 JSD 从 ≤1.5B 的 0.15–0.27 降至 8B 的 0.077；Pythia 1.4B→6.9B K* 从 2→1）暗示规模增大可能降低 K*。\n- Abstract 和 Conclusion 中 K*≈2 被呈现为通用结论，但实际适用范围仅 ≤8B。\n- **要求**：Abstract/Conclusion 显式限定 \"1B–8B\" 适用范围。如可能，补充 ≥1 个 >30B 模型实验。\n\n**C3** [R2-N1 + R1 同意, 共识] **Qwen 过度代表使 \"6/10\" 统计量误导**\n- 6/10 K*=2 配置中 4 个来自 Qwen。按 family 统计：仅 2/6 家族 unanimously K*=2（Qwen 4/4, LLaMA 1/1），3/6 unanimously K*=1（OLMo, Mistral, Gemma）。\n- Abstract \"6/10 configurations\" 技术正确但给读者过于乐观的印象。\n- R1 补充：即使 K*=1 的配置也确认 boundary 极浅（≤2），one-wash 定性结论在所有配置成立。\n- **要求**：(a) Section 4.1 添加 family-level 汇总表；(b) Abstract 同时报告 per-config 和 per-family 统计。\n\n**C4** [R1-N1 + R2 同意] **DPI→AUC 推理链仅为启发式，K*_empirical 作为 lower bound 的理论地位不清**\n- 论文以 DPI（MI 单调递减）motivate 期望 AUC 单调递减，但坦承 \"AUC and mutual information are not formally equivalent\"。K*_empirical 是 K*_theory 的 \"lower bound\" 仅为断言。\n- R2 认为可降级为 Should-Fix（论文已诚实承认），R1 坚持 Must-Fix（这是全文理论框架根基）。\n- **Director 判定**：Must-Fix（修改难度低但影响核心叙事完整性）。\n- **要求**：明确区分 K*_empirical 为操作性定义 vs K*_theory 下界两个 claim；对 lower bound claim 要么给出形式证明要么降级为 conjecture。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R2-N3, R1 部分反驳→降级] **Prompt-chain 生态有效性需限定**\n- Retrain-chain K*≥4（Appendix D.7），\"one-wash laundering\" 可能是 prompt-chain 特有现象。\n- R1 辩护：prompt-chain 是 web-scale contamination 主流路径（API 调用→发布→收录），retrain-chain 在实际 web contamination 中罕见。论文选择合理，但表述缺乏限定。\n- **要求**：Abstract/Conclusion 添加 \"under prompt-chain generation\" 限定语。\n\n**W2** [R1-W1 + R2 同意] **Cross-scorer 降级暴露部署局限**\n- Qwen-cont cross-scoring AUC=0.5923(Pythia)/0.5858(OLMo) 均 <θ，K*=2→1。\n- 实际部署中 generator 身份未知，cross-scoring 才是工作条件。K*=2→1 意味着退化为 binary detection。\n- **要求**：Section 4.2 更突出讨论此限制；探讨 scorer-ensemble 策略。\n\n**W3** [R1-W2 + R2 同意] **Filtering 效果量小且 dose-response 未在正文讨论**\n- +0.74pp MMLU, +0.03pp HellaSwag（100% 合成极端条件下）。\n- Appendix D.8：≤30% contamination 下所有策略差异消失（p>0.8）。\n- 论文已定位为 consistency check，但正文未引用 dose-response，读者可能高估实际价值。\n- **要求**：Section 5 或 Discussion 引用 dose-response 分析，承认现实污染比例下边际增益可忽略。\n\n**W4** [R2-W1 + R1 同意] **Filtering 仅在单一 generator 验证**\n- 仅 Qwen-1.5B continuation。K*=1 配置下 binary filtering 是否退化为普通 binary detection 未讨论。\n- **要求**：Limitations 声明，Section 5 讨论 K*=1 场景。\n\n**W5** [R2-W2, R1 反驳] **K*=2 相对 binary detection 的增量贡献讨论不足**（Reviewer 分歧）\n- R2：结论 \"binary is sufficient\" 使增量贡献不明确。\n- R1 反驳：K* 提供解释性价值（为什么 binary 有效）、域差异化（C4 vs arXiv）、策略指导（binary vs graduated），是度量框架而非仅实用策略。\n- **Director 判定**：保留为 Should-Fix。Discussion 应更明确阐述 K*_empirical 的认识论贡献。\n\n### Minor\n\n**M1** [R1+R2] 正文缺少 Mistral-7B、Gemma-2-2B 数据覆盖——Section 4.1 应添加 1-2 句概述全部 10 配置结果。\n**M2** [R2+R1 同意] 遗漏 Suresh et al. (2024) \"Rate of Model Collapse\"——Related Work 应补充。\n**M3** [R2+R1 同意] Abstract \"Cohen's h≈0.20\" 缺乏上下文——替换为直观表述，技术细节移至 Section 3.1。\n**M4** [R1] Figure 1 中 K* Estimation 步骤箭头指向不清——应标注为语料库层面估计。\n**M5** [R2+R1 同意] Table 2 应视觉高亮 K* boundary 行。\n**M6** [R2+R1 同意] self-BLEU deployment 替代方案应更突出说明。\n**M7** [R1] Eq.1 后应明确声明 AUC 单调递减为经验观察而非理论保证。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识：\n\n| 问题 | R1 | R2 | 状态 |\n|------|----|----|------|\n| θ=0.60 敏感性 | W3→升级 Must-Fix | N2 (Must-Fix) | [AGREE] 最强共识 |\n| 模型规模 ≤8B | N2 (Must-Fix) | W3 (Should-Fix) | [AGREE] |\n| Qwen 过度代表 | 同意 R2-N1 | N1 (Must-Fix) | [AGREE] 表述需改 |\n| Cross-scorer 降级 | W1 (Should-Fix) | 同意 R1-W1 | [AGREE] |\n| Filtering 效果量小 | W2 (Should-Fix) | 同意 | [AGREE] |\n| Filtering 单配置 | 同意 R2-W1 | W1 (Should-Fix) | [AGREE] |\n| DPI→AUC 理论缺口 | N1 (Must-Fix) | 同意降为 Should-Fix | [AGREE] 严重性有差异 |\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 判定 |\n|------|---------|---------|---------------|\n| Prompt-chain 生态有效性 | [REBUT] 降级 Should-Fix：prompt-chain 是 web contamination 主流路径 | Must-Fix：retrain-chain K*≥4 说明设定特有 | Should-Fix（R1 论证更有说服力，但同意需限定表述） |\n| K*=2 vs binary detection 贡献 | [REBUT] K* 是度量框架，提供解释性+域差异化价值 | Should-Fix：增量贡献不清 | Should-Fix（分歧记录，双方各有理据） |\n| Rewrite vs continuation 分析 | W4 (Should-Fix)：需更深入分析 | [REBUT] 现有分析在 8 页限制下足够 | Minor（R2 论点合理） |\n| Pythia EOS truncation | M4：34-36% truncation 可能引入长度混淆 | [REBUT] Appendix Table 12 已充分讨论 | Dropped（已有覆盖） |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1** [R1] 更强分类器（fine-tuned transformer encoder）是否会增加 K*_empirical？Neural probe K*=3（Qwen）是否意味着 K*_theory>2，从而削弱\"一次洗白\"叙事的绝对性？\n\n**Q2** [R1] θ=0.60 映射假设 null AUC=0.50，但 permutation null 95th percentile <0.55。能否用 permutation null 直接校准 θ？\n\n**Q3** [R1] Qwen-cont 1v2 AUC=0.611 的 fold 间方差是多少？是否有 fold 中 AUC<θ？\n\n**Q4** [R1+R2] K*=1 模型（OLMo-1B）生成的污染数据下，binary filtering 是否仍有效？此时 K*-aware 的价值是否消失？\n\n**Q5** [R1] arXiv 域 n=2,200 是 per-model 还是两个家族共享？每个深度级别的样本量？\n\n**Q6** [R2] Cross-model retrain-chain（如 Qwen→Pythia→OLMo）下 K* 预期是什么？\n\n**Q7** [R2] Appendix D.8 显示 ≤30% contamination 下策略差异消失——现实中 K*-aware filtering 是否实际无用？\n\n---\n\n## Missing References\n\n| 引用 | 来源 | 重要性 | 共识 |\n|------|------|--------|------|\n| Suresh et al. (2024) \"Rate of Model Collapse in Recursive Training\" | R2 | Should-Cite | R1 同意 |\n| Gehrmann et al. (2019) \"GLTR\" | R1 | Nice-to-Cite | R2 认为已被后续工作覆盖 |\n| Tang et al. (2024) \"The Science of Detecting LLM-Generated Text\" | R1 | Nice-to-Cite | R2 需核实真实性 |\n| Borji (2024) \"A Note on Shumailov et al.\" | R2 | Nice-to-Cite | R1 认为相关性有限 |\n| Dugan et al. (ACL 2024) \"RAID\" benchmark | R2 | Nice-to-Cite | R1 同意但非必须 |\n\n---\n\n## External Review\n\n**状态**: 未请求（项目配置未启用 paperreview.ai）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（0 critical, 8 warning, 19 info）\n\n主要发现：\n- **页面 1-2 纯文本**（warning）：连续 2 页无 display item。建议将 Figure 1 前移至第 2 页。\n- **页面 3-6 视觉节奏优秀**（info）：Figure 1→Table 1+Figure 2+Figure 3→Table 2+Figure 4+Table 3→Table 4+Table 5，display items 密集穿插。\n- **主正文密度**（info）：8 页含 4 figures + 5 tables = 9 个 display items（~1.1/页），符合实证论文预期。\n- **Appendix 空白**（warning×6）：Table 10-13、Table 21-22、Table 26 附近存在显著空白，页面利用率 15%-50%。建议合并小表。\n- **格式合规**（info）：ACL 匿名模板正确，无 LaTeX 残留/margin 溢出/未解析引用，References 格式统一。\n- **Figure 质量**（info）：Figure 1 pipeline 清晰，Figure 2 AUC 衰减曲线带 CI shaded band，Figure 4 heatmap 数值标注清晰。\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 / 5（Borderline Conference）**\n\n**对应 EMNLP 2026 ARR 标准**: 3.5 = Borderline Conference（介于可被主会议接收与 Findings 之间）\n\n**R1**: 3.5 | **R2**: 3.5 | **Director 综合**: 3.5\n\n**置信度**: 4/5\n\n### 判定理由\n\n**支持 Conference (4.0) 的因素**：\n- 问题定义新颖，K*_empirical 是一个有清晰动机的新概念\n- 实验设计严谨，统计实践规范，附录极其充分\n- \"One-wash laundering\" 是一个可记忆、可操作的发现\n- Cross-model transfer 增强了方法实用性\n\n**拉低至 3.5 的因素**：\n- θ=0.60 敏感性使核心结论 K*=2 的稳健性存疑（最关键）\n- 模型规模 ≤8B，核心发现的泛化性未验证\n- Qwen 4/10 过度代表，per-family 统计显著弱于 per-config\n- DPI→AUC 理论桥接仅为启发式\n- 下游 filtering 效果量小，现实污染比例下近乎无用\n- Cross-scorer 降级使 K*=2 在部署条件下不稳健\n\n**修改路径建议（不构成审稿意见，仅供参考）**：\n如果作者能 (a) 提供 θ-free 表述和灵敏度曲线，(b) 限定 K*≈2 适用范围（1B–8B, prompt-chain），(c) 添加 per-family 统计，(d) 明确 K*_empirical 的 lower bound 理论条件——则有望达到 4.0 (Conference) 水准。这些修改均不涉及新实验，属于 framing/presentation 层面的改进。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"6/10 configurations\" 应同时报告 per-family 统计（2/6 unanimously K*=2）\n- \"one-wash laundering effect\" 首次出现时应限定为 prompt-chain 场景\n- Retrain-chain K*≥4 的对比应在 Introduction 末尾提及，而非仅在 Discussion\n\n### Section 3 (Method)\n- Eq. 1 后应明确声明 AUC 单调递减为经验观察\n- θ=0.60 的第三条证据（distributional discontinuity）应标为 \"post-hoc confirmatory\"\n- \"lower bound on K*_theory\" claim 需形式化或降级\n\n### Section 4 (Experiments)\n- 4.1: 添加 family-level 汇总表，正文覆盖全部 10 配置\n- 4.2: Cross-scorer 降级的部署影响需更突出讨论\n- Table 2: 高亮 boundary 行\n\n### Section 5 (Filtering)\n- 正文引用 dose-response 分析（Appendix D.8）\n- 承认 ≤30% contamination 下策略差异消失\n- 讨论 K*=1 场景下 filtering 是否退化\n\n### Section 6 (Discussion)\n- K*_empirical 作为度量框架（vs 仅作为 binary detection 副产品）的价值需更明确阐述\n- Prompt-chain vs retrain-chain 的适用范围需更清晰界定\n\n### Section 7 (Conclusion)\n- 显式限定 \"1B–8B\" 和 \"prompt-chain\" 适用范围\n- 补充 per-family 统计\n\n### Abstract\n- \"Cohen's h≈0.20\" 替换为直观表述\n- 同时报告 per-config 和 per-family 统计\n- 添加 prompt-chain 限定语",
    "project": "gen-depth-contamination",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
  }
}
```

</details>

---


### Tool result

_source line 2397 · 2026-05-22T07:33:53.942269+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_5d2a0ec1de3a456564133278c1a9b203:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4771
}
```

</details>

---


### Tool call

_source line 2398 · 2026-05-22T07:34:03.967852+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2399 · 2026-05-22T07:34:03.968406+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2400 · 2026-05-22T07:34:13.287702+00:00_

Round 25 审稿完成。报告已投递至 Research Director。

**结论：3.5 / 5（Borderline Conference）**

4 个 Must-Fix：
1. **θ=0.60 敏感性**（最强共识）——K* 在 θ∈[0.55,0.70] 从 3 变到 1，需提供 θ-free 表述
2. **模型规模 ≤8B**——核心结论泛化性未验证，需限定适用范围
3. **Qwen 过度代表**——6/10 中 4 个 Qwen，per-family 仅 2/6 unanimously K*=2
4. **DPI→AUC 理论缺口**——lower bound claim 缺乏形式化支撑

5 个 Should-Fix：prompt-chain 表述限定、cross-scorer 部署局限、filtering 效果量小、filtering 单配置、K* vs binary detection 增量贡献讨论。

两位 Reviewer 评分一致（均 3.5），核心问题高度收敛。主要分歧仅在 prompt-chain 生态有效性的严重性评级（R2 Must-Fix vs R1 Should-Fix，Director 判定 Should-Fix）。Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 184

## Round 184

2 recorded events


### User

_source line 2401 · 2026-05-22T07:34:16.032425+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部意见的逐条回应。三个主要判断：

1. **N3（prompt-chain 生态有效性）**：REBUT——prompt-chain 对 data curation 场景合理，但同意需限定 "one-wash laundering" 的适用范围，建议降级为 Should-Fix
2. **W2（K\*=2 新贡献）**：REBUT——K\*_empirical 作为度量框架提供域差异化、策略指导和理论解释，超越了"binary is sufficient"的结论
3. 其余 N1/N2/W1/W3/W4/Q3 等均 AGREE，与我自己的审稿意见一致或互补

两位 reviewer 共同优先关切：θ 敏感性、>8B 模型覆盖不足、Qwen 过度代表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2402 · 2026-05-22T07:34:26.398733+00:00_

Round 25 审稿已完成。报告已投递至 Research Director。

**最终评分：3.5 / 5（Borderline Conference）**，R1 和 R2 评分一致。

**4 个 Must-Fix**：
1. θ=0.60 阈值敏感性（最强共识）
2. 模型规模 ≤8B 泛化性未验证
3. Qwen 过度代表（6/10 中 4 个 Qwen）
4. DPI→AUC 理论桥接未形式化

**5 个 Should-Fix**：prompt-chain 生态有效性限定、cross-scorer 降级、filtering 效果量小、filtering 单配置、K\*=2 vs binary detection 贡献阐述

**关键判断**：4 个 Must-Fix 均不涉及新实验，属于 framing/presentation 层面改进。如果能提供 θ-free 表述、限定适用范围（1B–8B, prompt-chain）、添加 per-family 统计、明确 lower bound 理论条件，有望达到 4.0（Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 185

## Round 185

62 recorded events


### User

_source line 2403 · 2026-05-22T07:53:49.154995+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: gen-depth-contamination
- 论文路径: projects/gen-depth-contamination/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2404 · 2026-05-22T07:53:55.201962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2405 · 2026-05-22T07:53:55.303284+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2406 · 2026-05-22T07:54:00.272959+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,read_local_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 2407 · 2026-05-22T07:54:00.373973+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2408 · 2026-05-22T07:54:03.136702+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2409 · 2026-05-22T07:54:04.594118+00:00_

{"result":"# 项目 gen-depth-contamination 概况\n\n## 实验状态 (156 个)\n\n- **exp_016_base_vs_instruct**: DONE (success) — \n- **exp_003_decoding_ablation**: DONE (success) — \n- **exp_004_7b_crossscale**: DONE (success) — \n- **exp_E_paired_stats**: DONE (success) — \n- **exp_D_obd_n500**: DONE (success) — \n- **exp_B_14d_ablation**: DONE (success) — \n- **exp_A_alt_scorer**: DONE (success) — \n- **exp_015_neural_probe**: DONE (success) — \n- **exp_006_graduated_filtering**: DONE (success) — \n- **exp_007_bootstrap_ci**: DONE (success) — \n- **exp_011_llm_zeroshot**: DONE (success) — \n- **exp_013_cross_transfer**: DONE (success) — \n- **exp_010_ordinal_baseline**: DONE (success) — \n- **exp_001_pythia_depth**: DONE (success) — \n- **mvp_pilot_sat_v1**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- 7b-cross-transfer（准备中）\n- arxiv_multi_source（准备中）\n- sweep_r10_nofilter（准备中）\n- sweep_r10_binary（准备中）\n- sweep_r10_graduated（准备中）\n- sweep_r30_nofilter（准备中）\n- sweep_eval_r10_nofilter（准备中）\n- sweep_eval_r10_binary（准备中）\n- sweep_eval_r10_graduated（准备中）\n- sweep_eval_r30_nofilter（准备中）\n- …另有 27 项\n\n## 近期结论\n- **seed_qwen15b_c4_s123** (success): Qwen-1.5B C4 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n- **seed_qwen15b_wiki_s123** (negative): Qwen-1.5B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n- **seed_pythia14b_wiki_s123** (success): Pythia-1.4B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\n\n## 趋势\n成功 90 / 负向 16 / 失败 13 / 共 119\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-22115: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nwestd-42896: 无 GPU 信息\n\n## 告警\n- exp-008-retrain-chain: 训练失败 — unknown\n- exp_009_dose_10pct: 训练失败 — unknown\n- exp_009_dose_30pct: 训练失败 — unknown\n- exp_009_dose_50pct: 训练失败 — unknown\n- exp_009_dose_10pct_v2: 训练失败 — unknown\n- exp_009_dose_30pct_v2: 训练失败 — unknown\n- exp_009_dose_50pct_v2: 训练
…[truncated 279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 2410 · 2026-05-22T07:54:04.745157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2411 · 2026-05-22T07:54:05.548925+00:00_

1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure a lower bound on the generational discrimination boundary, $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable), using 15 statistical features and an OBD-LightGBM classifier.
36	Under prompt-chain generation across 10 model configurations (6 architecture families, 1B--8B), 3 source domains, and 4 decoding strategies, $\Kempirical \in \{1, 2, 3\}$ at $\theta{=}0.60$ (a conventional small-effect-size threshold): general web text yields $\Kempirical{=}2$ in 6/10 configurations (2 of 6 families unanimously, plus a scale-dependent split in Pythia), while structured academic text (arXiv) yields $\Kempirical{=}3$, validated across two architectures.
37	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect (first-generation text is detectable, but second-generation and beyond are not).
38	Model-free statistical features enab
…[truncated 4291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2412 · 2026-05-22T07:54:05.649945+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May 2026 call for papers submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR May 2026 call for papers submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2413 · 2026-05-22T07:54:05.951538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2414 · 2026-05-22T07:54:06.002691+00:00_

1	## Review Issues Tracker — gen-depth-contamination
2	## Updated: Round 25 fixes dispatched (2026-05-22)
3	
4	# === CRITICAL / MUST-FIX ===
5	
6	- id: "R1-N1"
7	  summary: "DPI→adjacent-pair AUC 推理链存在逻辑缺口"
8	  category: method
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 20
12	  last_seen_round: 25
13	  mentions:
14	    - round: 20
15	      reviewer: R1
16	      note: "DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。"
17	    - round: 24
18	      reviewer: [R1, R2]
19	      note: "应明确 DPI 是 heuristic motivation 而非 strict proof。"
20	    - round: 25
21	      reviewer: [R1, R2]
22	      note: "R1 列为 Must-Fix：K*_empirical 作为 K*_theory 下界仅为断言，缺形式证明。R2 同意但建议降为 Should-Fix（论文已承认 AUC≠MI）。共识：需明确区分操作性定义 vs lower bound claim。"
23	  action_items:
24	    - round: 25
25	      action: "明确区分 K*_empirical 为操作性定义 vs K*_theory 下界；后者降级为 conjecture 并阐明 AUC-MI gap"
26	      assigned_to: paper_agent
27	      status: done
28	  resolution: "Paper Agent C1a/C1b patch: method.tex DPI→heuristic motivation, K*_theory→conjecture with explicit AUC-MI gap caveat"
29	  resolution_round: null
30	
31	- id: "R1-N2"
32	  summary: "θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱"
33	  category: experiment
34	  severity: critical
35	  status: in_progress
36	  first_raised_round: 20
37	  last_seen_round: 25
38	  mentions:
39	    - round: 24
40	      reviewer: [R1, R2]
41	      note: "Cohen's h 提供先验基础，但第三条 distributional discontinuity 应标为 post-hoc confirmatory。"
42	    - round: 25
43	      reviewer: [R1, R2]
44	      note: "两位 Reviewer 最强共识点。θ∈[0.55,0.70] 内 K* 从 3 变到 1。Qwen-cont CI 下界仅超 θ 0.002。Cohen's h=0.20 是统计惯例非检测理论推导。R1 补充：permutation null 95th percentile <0.55，实际 null 比理论预期高。"
45	  action_items:
46	    - round: 25
47	      action: "报告 θ-free 指标（AUC gap 及其 CI），提供完整灵敏度曲线；鼓励读者根据应用场景选择 θ"
48	      assigned_to: paper_agent
49	      status: done
50	  resolution: "Paper Agent C3a patch: θ-free AUC gap as continuous measure + Figure 3 sensitivity surface reference + practitioner θ calib
…[truncated 14052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 2415 · 2026-05-22T07:54:10.921859+00:00_

Web search results for query: "EMNLP 2026 ARR May 2026 call for papers submission guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

I found relevant information about EMNLP 2026 and ARR submissions. Based on the search results, here 
…[truncated 1094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5271
}
```

</details>

---


### Tool call

_source line 2416 · 2026-05-22T07:54:15.529448+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 2417 · 2026-05-22T07:54:15.981887+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers deadline submission"
  }
}
```

</details>

---


### Tool result

_source line 2418 · 2026-05-22T07:54:22.760729+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on my search results, here is information about ACL Rolling Review (ARR) 2026 submission guidelines, including page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up to four (4) pages of content, plus u
…[truncated 985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 7231
}
```

</details>

---


### Tool result

_source line 2419 · 2026-05-22T07:54:22.811483+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers deadline submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, he
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6829
}
```

</details>

---


### Tool call

_source line 2420 · 2026-05-22T07:54:32.512315+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-contamination",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2421 · 2026-05-22T07:54:32.662986+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2422 · 2026-05-22T07:54:33.919379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2423 · 2026-05-22T07:54:34.473004+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistica
…[truncated 1720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2424 · 2026-05-22T07:54:34.473408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2425 · 2026-05-22T07:54:35.025840+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.
6	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
8	
9	\paragraph{Beyond binary detection.}
10	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
11	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
12	None estimates recursive generation depth.
13	
14	\paragraph{Data selection and curation.}
15	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
16	
17	\paragraph{Ordinal classification and probing.}
18	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
19
…[truncated 1 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2426 · 2026-05-22T07:54:35.026330+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2427 · 2026-05-22T07:54:35.127060+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
17	Together with Markov chain convergence, this provides heuristic motivation for expecting $\auc_{k-1,k}$ to decrease with $k$, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\!\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, j \!\leq\! k\bigr\},
22	  \label{eq:kstar}
23	\end{equation}
24	which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested configurations; Table~\ref{tab:kstar_ci}).
25	The theoretical upper bound $\Ktheory$ (the true maximum discriminable depth given optimal features) is not directly estimated in this work.
26	We conjecture that $\Kempirical$ provides a lower bound on $\Ktheory$: the DPI guarantees monotonic mutual information decay, but since AUC is not a monotone function of MI (as noted above), a formal proof requires establishing that the AUC
…[truncated 5266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2428 · 2026-05-22T07:54:39.590572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---


### Tool result

_source line 2429 · 2026-05-22T07:54:39.892629+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on ten model configurations spanning six architecture families:
5	Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5024 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .4942 & 
…[truncated 10427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 2430 · 2026-05-22T07:54:39.893031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
  }
}
```

</details>

---


### Tool result

_source line 2431 · 2026-05-22T07:54:40.395467+00:00_

1	\section{Consistency Check: $\Kstar$-Guided Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We test this as a consistency check on the boundary measurement, not as an independent contribution.
6	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
7	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
13	\label{tab:tab_filtering_main}
14	\input{tables/tab_filtering_main}
15	\end{table}
16	
17	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
18	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
19	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduat
…[truncated 990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2432 · 2026-05-22T07:54:40.395889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2433 · 2026-05-22T07:54:40.848053+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
13	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
14	
15	\paragraph{Graduated filtering failure.}
16	For web text, 2v3 $\auc < \theta$ across all model configurations, so depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise, explaining convergence toward binary at high $\alpha$ (Appendix~\ref{sec:extended_limitations}).
17	DSIR fails differently: bigram hashing captures domain shift but not depth-correlated signatures.
18	
19	\paragraph{Representation dependence.}
20	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
21	The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
22	Feature rankings are scorer-independent ($\rho > 0.90$); $\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (
…[truncated 4472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2434 · 2026-05-22T07:54:40.848433+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2435 · 2026-05-22T07:54:40.898969+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure a lower bound on the generational depth discrimination boundary $\Kempirical$ for prompt-chain recursive synthetic text.
5	$\Kempirical \in \{1, 2, 3\}$ depends on source domain and model characteristics: general web text yields $\Kempirical{=}2$ in 6/10 configurations (2/6 families unanimously, with a scale-dependent split in Pythia; 1B--8B; $p \leq 0.002$), with $\Kempirical{=}3$ for structured academic text.
6	This one-wash laundering effect means that a single generation pass renders web text indistinguishable from deeper recursive content, limiting depth-aware curation to a binary boundary.
7	For practitioners, binary filtering (depth 0 vs.\ $\geq$1) captures the only reliable discrimination signal; graduated weighting beyond $\Kempirical$ adds noise.
8	$\Kempirical$ is feature-set dependent (15D provides a conservative lower bound; neural probes extend it by one level for some architectures) and established for 1B--8B models; scaling beyond 8B, additional structured domains, and retrain-chain $\Kstar$ remain open.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2436 · 2026-05-22T07:54:53.850910+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2437 · 2026-05-22T07:54:53.901745+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2438 · 2026-05-22T07:54:56.714554+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2439 · 2026-05-22T07:54:56.765194+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2440 · 2026-05-22T07:54:59.175532+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2441 · 2026-05-22T07:54:59.276451+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2442 · 2026-05-22T07:55:02.491545+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+read +local +file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+read +local +file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 2443 · 2026-05-22T07:55:02.542418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2444 · 2026-05-22T07:55:06.711085+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2445 · 2026-05-22T07:55:06.761885+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2446 · 2026-05-22T07:55:11.281978+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-contamination/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-contamination/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7"
  }
}
```

</details>

---


### Tool result

_source line 2447 · 2026-05-22T07:55:11.332751+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2448 · 2026-05-22T07:55:14.258012+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/gen-depth-contamination/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/gen-depth-contamination/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7"
  }
}
```

</details>

---


### Tool result

_source line 2449 · 2026-05-22T07:55:14.308837+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260516T073047/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects
…[truncated 8173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2450 · 2026-05-22T07:55:18.074924+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "glob": "**/config*.{yaml,yml,json,toml}",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
    "glob": "**/config*.{yaml,yml,json,toml}",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2451 · 2026-05-22T07:55:18.175738+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2452 · 2026-05-22T07:55:20.687178+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "config/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "config/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7"
  }
}
```

</details>

---


### Tool result

_source line 2453 · 2026-05-22T07:55:20.737958+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2454 · 2026-05-22T07:55:24.205671+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/config -maxdepth 3 -type f -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" 2>/dev/null | head -20",
  "description": "Find config files in config directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/config -maxdepth 3 -type f -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"*.toml\" 2>/dev/null | head -20",
    "description": "Find config files in config directory"
  }
}
```

</details>

---


### Tool result

_source line 2455 · 2026-05-22T07:55:24.356641+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_ac138dec086db9fd9257ce40028f628d.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_72b5a7797b623899786091579596a8b2.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_review_reviewer_1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_f265de7a9796688b878083fef59f9d4c.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_074936fc4b5d802648d5b9b7fe3a8a01.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_5304abbd56fd7a7f12edca904ca28ec0.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_7452874ce81eb89ffd857f072209b08f.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_b5b42865db9e25c090239f4ff8686b1b.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_paper_agent.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_ce56e63b92b21f6322ae20c46071b336.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_worker_dc55567f3c41939c4158a0a3c8e6e960.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config/mcp_config_dream_review_director.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2456 · 2026-05-22T07:55:27.068005+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/config",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 2457 · 2026-05-22T07:55:27.118573+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2458 · 2026-05-22T07:55:58.861834+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "gen-depth-contamination",
  "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "gen-depth-contamination",
    "review_chat_id": "oc_0f6dcb30efaa4f47425ef1d9874a89d7"
  }
}
```

</details>

---


### Tool result

_source line 2459 · 2026-05-22T07:56:21.342049+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22480
}
```

</details>

---


### Tool call

_source line 2460 · 2026-05-22T07:56:21.492818+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤8 页 + 无限参考文献, ACL 模板\n- **匿名**: double-blind\n- **Limitations**: 必须有，不计入页数\n- **评分标准**: ARR Overall Assessment (1-5 分制, 4=Conference, 3=Findings, 2.5=Borderline Findings)\n\n### 论文路径\n- LaTeX: `projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_26/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计有效性**，具体关注：\n\n1. **K*_empirical 形式化定义**：Eq.1 的定义是否严谨？max 算子隐含的单调假设是否合理？K*_empirical 作为 K*_theory 下界的 conjecture 是否有足够的论证支撑？DPI 作为 heuristic motivation 是否被准确标注？\n\n2. **阈值选择 (θ=0.60)**：三条论证线（Cohen's h, permutation null, distributional discontinuity）是否各自独立且充分？θ 灵敏度分析（Figure 3）是否足以让读者评估 K* 对 θ 的敏感度？θ-free AUC gap 是否被充分呈现？\n\n3. **统计验证**：Bootstrap CI 的构造是否正确？边界对的 CI 下界是否真的超过 θ？Qwen-cont 1v2 CI 下界仅超 θ 0.002——这个边界案例是否被充分讨论？permutation test 的设计和 p 值解读是否恰当？\n\n4. **实验设计**：10 个配置中 Qwen 占 4 个——是否构成过度代表？per-family 统计（2/6 unanimously K*=2）是否被充分报告？模型规模覆盖（1B-8B）是否在 Abstract/Conclusion 中被明确限定？\n\n5. **Cross-scorer 验证**：Qwen-cont 从 K*=2 降级到 K*=1 的 cross-scorer 结果——scorer independence claim 是否被准确分层表述（feature ranking vs K* agreement vs absolute AUC）？ANOVA 结果的解读是否恰当？\n\n6. **Filtering 一致性检验**：效果量是否被准确呈现（100% synthetic 上限 vs 现实污染比例）？dose-response 分析是否被充分引用？Section 5 标题/framing 是否准确反映其定位（consistency check vs independent contribution）？\n\n7. **Cross-domain 实验**：arXiv K*=3 仅有 2 个模型家族、n=2200 的样本量——是否构成充分验证？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5) + Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤8 页 + 无限参考文献, ACL 模板\n- **匿名**: double-blind\n- **Limitations**: 必须有，不计入页数\n- **评分标准**: ARR Overall Assessment (1-5 分制, 4=Conference, 3=Findings, 2.5=Borderline Findings)\n\n### 论文路径\n- LaTeX: `projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_26/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计 + 统计有效性**，具体关注：\n\n1. **K*_empirical 形式化定义**：Eq.1 的定义是否严谨？max 算子隐含的单调假设是否合理？K*_empirical 作为 K*_theory 下界的 conjecture 是否有足够的论证支撑？DPI 作为 heuristic motivation 是否被准确标注？\n\n2. **阈值选择 (θ=0.60)**：三条论证线（Cohen's h, permutation null, distributional discontinuity）是否各自独立且充分？θ 灵敏度分析（Figure 3）是否足以让读者评估 K* 对 θ 的敏感度？θ-free AUC gap 是否被充分呈现？\n\n3. **统计验证**：Bootstrap CI 的构造是否正确？边界对的 CI 下界是否真的超过 θ？Qwen-cont 1v2 CI 下界仅超 θ 0.002——这个边界案例是否被充分讨论？permutation test 的设计和 p 值解读是否恰当？\n\n4. **实验设计**：10 个配置中 Qwen 占 4 个——是否构成过度代表？per-family 统计（2/6 unanimously K*=2）是否被充分报告？模型规模覆盖（1B-8B）是否在 Abstract/Conclusion 中被明确限定？\n\n5. **Cross-scorer 验证**：Qwen-cont 从 K*=2 降级到 K*=1 的 cross-scorer 结果——scorer independence claim 是否被准确分层表述（feature ranking vs K* agreement vs absolute AUC）？ANOVA 结果的解读是否恰当？\n\n6. **Filtering 一致性检验**：效果量是否被准确呈现（100% synthetic 上限 vs 现实污染比例）？dose-response 分析是否被充分引用？Section 5 标题/framing 是否准确反映其定位（consistency check vs independent contribution）？\n\n7. **Cross-domain 实验**：arXiv K*=3 仅有 2 个模型家族、n=2200 的样本量——是否构成充分验证？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5) + Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 2461 · 2026-05-22T07:56:38.639559+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17146
}
```

</details>

---


### Tool call

_source line 2462 · 2026-05-22T07:56:38.810995+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 相关工作 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤8 页 + 无限参考文献, ACL 模板\n- **匿名**: double-blind\n- **Limitations**: 必须有，不计入页数\n- **评分标准**: ARR Overall Assessment (1-5 分制, 4=Conference, 3=Findings, 2.5=Borderline Findings)\n\n### 论文路径\n- LaTeX: `projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_26/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 相关工作 + 写作质量 + 叙事框架**，具体关注：\n\n1. **新颖性与增量贡献**：generational depth estimation 作为新任务的定义是否清晰？K*_empirical 作为度量框架相对于 binary detection 的增量贡献是否充分论证？如果主要结论是\"binary is sufficient\"，这篇论文的贡献是什么？\"one-wash laundering\" 这个概念是否新颖且准确？\n\n2. **叙事框架准确性**：Abstract 中 \"6/10 configurations (2 of 6 families unanimously)\" 的表述是否准确且不误导？prompt-chain 限定是否充分？K*∈{1,2,3} 的表述是否清晰传达了结果的复杂性？\n\n3. **相关工作完整性**：是否遗漏了重要的相关工作？与 model collapse 文献（Shumailov 2024, Dohmatob 2024, Alemohammad 2024）的区分是否清晰？与 binary detection 文献（DetectGPT, Binoculars, DivEye, Min-k++）的对比是否公平？是否有遗漏的 data curation 或 ordinal classification 文献？特别关注是否遗漏了 2025-2026 年的新工作。\n\n4. **写作质量**：\n   - Abstract 信息密度是否过高？是否能在一次阅读中理解核心信息？\n   - Introduction 的 contribution 列表是否清晰且不冗余？\n   - 正文行文中是否出现了破折号（除专有名词外禁止）？\n   - 术语一致性（K*_empirical, K*_theory, OBD, one-wash laundering 等）\n   - Limitations 长度是否适当（约 3 个点，不要太长）？\n\n5. **格式合规性**：\n   - 正文是否在 8 页限制内？\n   - 参考文献格式是否一致？\n   - 图表是否都在正文页数限制内？\n   - Table/Figure 编号是否连续？标题是否清晰？\n   - 是否存在匿名违规（泄露作者信息）？\n\n6. **Limitations 和 Ethics Statement**：内容是否覆盖主要限制？是否恰当地讨论了双用风险？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5) + Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 相关工作 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: Long paper, 正文 ≤8 页 + 无限参考文献, ACL 模板\n- **匿名**: double-blind\n- **Limitations**: 必须有，不计入页数\n- **评分标准**: ARR Overall Assessment (1-5 分制, 4=Conference, 3=Findings, 2.5=Borderline Findings)\n\n### 论文路径\n- LaTeX: `projects/gen-depth-contamination/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_round_26/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 相关工作 + 写作质量 + 叙事框架**，具体关注：\n\n1. **新颖性与增量贡献**：generational depth estimation 作为新任务的定义是否清晰？K*_empirical 作为度量框架相对于 binary detection 的增量贡献是否充分论证？如果主要结论是\"binary is sufficient\"，这篇论文的贡献是什么？\"one-wash laundering\" 这个概念是否新颖且准确？\n\n2. **叙事框架准确性**：Abstract 中 \"6/10 configurations (2 of 6 families unanimously)\" 的表述是否准确且不误导？prompt-chain 限定是否充分？K*∈{1,2,3} 的表述是否清晰传达了结果的复杂性？\n\n3. **相关工作完整性**：是否遗漏了重要的相关工作？与 model collapse 文献（Shumailov 2024, Dohmatob 2024, Alemohammad 2024）的区分是否清晰？与 binary detection 文献（DetectGPT, Binoculars, DivEye, Min-k++）的对比是否公平？是否有遗漏的 data curation 或 ordinal classification 文献？特别关注是否遗漏了 2025-2026 年的新工作。\n\n4. **写作质量**：\n   - Abstract 信息密度是否过高？是否能在一次阅读中理解核心信息？\n   - Introduction 的 contribution 列表是否清晰且不冗余？\n   - 正文行文中是否出现了破折号（除专有名词外禁止）？\n   - 术语一致性（K*_empirical, K*_theory, OBD, one-wash laundering 等）\n   - Limitations 长度是否适当（约 3 个点，不要太长）？\n\n5. **格式合规性**：\n   - 正文是否在 8 页限制内？\n   - 参考文献格式是否一致？\n   - 图表是否都在正文页数限制内？\n   - Table/Figure 编号是否连续？标题是否清晰？\n   - 是否存在匿名违规（泄露作者信息）？\n\n6. **Limitations 和 Ethics Statement**：内容是否覆盖主要限制？是否恰当地讨论了双用风险？\n\n请按 ARR 审稿格式输出：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5) + Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 2463 · 2026-05-22T07:56:40.491357+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1680
}
```

</details>

---


### Assistant

_source line 2464 · 2026-05-22T07:56:47.254955+00:00_

已并行派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验 + 统计） | ✅ 已启动 |
| Reviewer 2（新颖性 + 完整性 + 写作） | ✅ 已启动 |
| 视觉审查 Agent | ✅ 已启动 |
| 外部审稿（paperreview.ai） | ⏭️ 未配置，跳过 |

等待两位 Reviewer 返回初审结果。收到后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 186

## Round 186

2 recorded events


### User

_source line 2465 · 2026-05-22T08:03:44.156234+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — Round 1 审稿报告

**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 完整性 + 相关工作 + 写作质量 + 叙事框架

---

## Paper Summary

本文提出"generational depth estimation"任务：给定一篇文档，估计其经过 LLM 递归生成的次数（深度）。作者定义 K*_empirical 为相邻代际仍可区分的最大深度下界，使用 15 维统计特征 + OBD-LightGBM 分类器在 10 个模型配置（6 个架构家族，1B–8B）、3 个文本域、4 种解码策略上进行实验。核心发现：K*_empirical ∈ {1,2,3}，web text 下 6/10 配置 K*_empirical ≥ 2；实际操作中 binary filtering（depth 0 vs. ≥1）已捕获唯一可靠的区分信号，graduated weighting 在 K*_empirical 之后只增加噪声。作者将此称为"one-wash laundering"效应。

---

## 总体评分

**Overall**: 3.0 (Findings)
**Confidence**: 4/5
**一句话总结**: 研究问题定义清晰、实验系统性强，但核心贡献存在内在悖论——建立了 ordinal depth estimation 框架后却证明 binary 足矣，增量贡献相对于 binary detection 文献不够充分。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论严谨（bootstrap CI、permutation test、cross-model transfer），但 K*_empirical 的操作性定义依赖 θ=0.60 阈值，justification 有一定循环性；核心结论"binary suffices"与提出 ordinal task 的动机存在张力 |
| **Excitement** | 2.5/5 | 问题定义有价值，但主要结论——binary detection 已足够、graduated weighting 只增加噪声——本质上削弱了 ordinal estimation 的意义；实际指导意见（binary filter）与已有 detection 文献高度重叠 |
| **Reproducibility** | 3.5/5 | 特征定义详尽（Table 14）、训练细节完整（Table 15-16），但未提及代码/数据是否会公开释放；生成 pipeline 的 prompt template 缺少完整展示 |
| **Overall Assessment** | 3.0/5 | Findings 级别——贡献了有用的经验性度量和负面结论，但不足以进入主会议 |

---

## 主要优势

**S1. 问题定义清晰且有实际意义。** 将 binary detection 扩展到 ordinal depth estimation 是自然且有动机的推进方向。Generational depth 与 model collapse 文献中的"information loss across iterations"概念形成有效桥接（Section 2, Section 3.1）。

**S2. 实验设计系统性强。** 10 个模型配置覆盖 6 个架构家族、3 个文本域（C4, Wikipedia, arXiv）、4 种解码策略（greedy, nucleus, temperature variants），实验矩阵设计合理。Cross-model transfer 实验（Section 4.2, Table 4）和 scorer sensitivity 分析（Table 22）是有价值的补充。

**S3. 统计严谨性好。** Bootstrap 95% CI、permutation p-values、Cohen's h effect size 的综合使用在这个领域的论文中较为少见。K*_empirical 的三重验证（Cohen's h, permutation test, post-hoc confirmation; Section 3.2, θ justification）增强了结论可信度。

**S4. 实用性强的负面结论。** "One-wash laundering"发现（binary filtering 已捕获唯一可靠信号）对 data curation practitioners 有直接指导意义，且通过下游 MMLU 实验（Table 5, Section 5）给出了实际 validation。

**S5. Appendix 详尽。** 22 页中 12 页为 appendix，覆盖 extended ablation（D.1-D.9）、confusion matrices（Table 10-11）、token length analysis（Table 12）、seed robustness（Table 26），展示了扎实的实验工作。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心贡献的内在悖论未充分解决
- 具体位置：Abstract, Section 1 (contributions), Section 7 (Conclusion)
- 问题：论文的叙事结构是"提出 ordinal depth estimation 任务 → 构建 K*_empirical 度量框架 → 发现 binary 已足够"。这造成一个根本性张力：如果最终结论是 binary detection suffices（Conclusion 第 523–525 行），那么 ordinal estimation 框架的增量贡献是什么？Contribution (a) 声称"first measurement of K*_empirical across 10 model configurations"，但这个度量的实际价值在 K*_empirical ≈ 2 的情况下退化为"first generation is detectable, rest is noise"，这与已有 binary detection 文献（DetectGPT, Binoculars, Min-k++ 等）的已知结论高度一致。
- 为什么影响接收：如果 reviewer 认为核心贡献本质上重复了 binary detection 的已知结论（换了一种度量方式），论文的 novelty 会被严重质疑。
- 建议修改方向：(1) 更明确地区分"验证 binary boundary 的存在"（已知）与"精确量化 boundary 的位置和特性"（新贡献）；(2) 强调 K*_empirical 框架的方法论价值——它提供了一个 principled way 来测量任意 detector 的区分粒度，而不仅仅是本文的 OBD 分类器；(3) 讨论在什么条件下 K*_empirical > 2 会实际重要（如 arXiv domain 的 K*=3 意味着什么？）。

**N2** [critical] Abstract 与正文叙事框架存在不一致
- 具体位置：Abstract vs. Section 4.1 heading
- 问题：Abstract 说"general web text yields K*_empirical ≥ 2 in 6/10 configurations (2 of 6 families unanimously)"，表示 4/10 配置 K*_empirical < 2（即 =1）。但 Section 4.1 的标题是"K*_empirical ≥ 2 Across Model Configurations (C4)"，暗示所有 10 个配置都满足 K*_empirical ≥ 2。正文中又提到"6/10 configurations yield K*_empirical ≥ 2"。Section heading 与实际数据之间存在误导性矛盾。
- 为什么影响接收：这涉及论文核心 claim 的准确性。读者在 Section 4.1 标题处会认为所有 10 个配置都有 K*_empirical ≥ 2，到 abstract 和正文细节时才发现只有 6/10，造成困惑和信任损失。
- 建议修改方向：将 Section 4.1 标题改为更准确的表述，如"K*_empirical Across Model Configurations (C4)"去掉"≥ 2"或改为"K*_empirical ≥ 2 in Majority of Configurations"。

**N3** [critical] 遗漏高度相关的近期工作
- 具体位置：Section 2 (Related Work)
- 问题：以下两篇高度相关的论文未被引用和讨论：
  (1) **Geng et al. (March 2026), "Markovian Generation Chains in Large Language Models"**（arXiv 2603.11228）：直接研究 LLM 迭代处理链中文本如何演变，定义了 Markovian generation chains 概念，发现反复处理导致输出收敛到小的循环集合或在有限视界内持续产生新句子。这与本文的 prompt-chain generation depth 概念高度重叠，必须讨论异同。
  (2) **Shahriar et al. (Dec 2025), "The Erosion of LLM Signatures"**（arXiv 2512.05311）：研究迭代 paraphrasing 后 detection 性能随深度下降约 25.4%（across 5 stages），直接回答了"检测器能区分几代？"这个问题，与本文的 K*_empirical 测量互补。
- 为什么影响接收：遗漏直接相关的并行工作会被 reviewer 视为 incomplete survey，尤其是 Geng et al. (2026) 研究的是几乎相同的现象。
- 建议修改方向：在 Section 2 添加对这两篇工作的讨论，明确说明本文与 Geng et al. 的区别（本文关注 discrimination boundary 的精确量化 + 实际 data curation 应用 vs. Geng et al. 关注 convergence behavior 的理论性质），以及与 Shahriar et al. 的互补性（他们的发现支持本文的 one-wash laundering 结论）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] θ=0.60 阈值的 justification 存在潜在循环性
- 具体位置：Section 3.2, θ justification paragraph
- 问题：θ=0.60 对应 Cohen's h=0.20（"small" effect size），作者声称三重验证支持此选择（Cohen's h, permutation test 95th percentile, post-hoc confirmation）。然而，"small effect size" 的选择本身是主观的——为什么不用 "medium"（h=0.50, AUC≈0.67）或更严格的标准？Figure 3 的 sensitivity curve 显示 θ 在 0.55–0.65 范围内 K*_empirical 稳定，但这恰恰说明结论对 θ 不太敏感，可能削弱了精确度量的意义（如果 K*_empirical 在一个 range 内都稳定，那具体值是多少就不那么重要了）。
- 建议：明确讨论 θ 选择对 K*_empirical 值的 sensitivity 范围（目前在 Appendix Figure 3 有但未在正文充分讨论），并说明在什么应用场景下 θ 的精确选择会影响实践决策。

**W2** [warning] 模型规模限制削弱实用性主张
- 具体位置：Section 3.3, Limitations
- 问题：所有实验模型为 1B–8B，但实际 web-scale 合成文本主要来自 GPT-4、Claude、Gemini 等 100B+ 模型。Section 4.1 报告"larger models produce more human-like text, reducing 0v1 ISRD"，且 Section 6 Discussion 提到"models at 13B+ may increasingly yield K*_empirical=1"——这是一个关键但未验证的推测。如果大模型的 K*_empirical=1（即第一代已不可区分），本文的整个框架在实际最重要的场景下就失效了。
- 建议：(1) 将"13B+ 可能 K*_empirical=1"这一推测在 Limitations 中更突出地讨论，而非仅在 Discussion 中一笔带过；(2) 如果可能，补充至少一个 >8B 模型的数据点。

**W3** [warning] 文档长度限制（256 tokens）的代表性
- 具体位置：Section 3.3, Appendix D.7
- 问题：seed text 128 tokens，生成限制 256 tokens。真实 web 文档通常数千 tokens。Appendix D.7 (Table 20) 测试了 128/256/512 tokens，显示 K*_empirical=2 在 128 和 256 tokens 下成立但 512 tokens 的 1v2 CI lower bound "falls marginally below θ"。这暗示更长文档可能改变 K*_empirical，但实验覆盖不足。
- 建议：扩展 Table 20 的实验到 1024+ tokens，或在 Limitations 中明确讨论长度敏感性及其实际含义。

**W4** [warning] Prompt-chain 限定 vs. 标题泛化
- 具体位置：Title, Abstract, Section 2
- 问题：标题"Generational Depth Estimation of Recursive Synthetic Text"暗示对所有类型的递归合成文本都适用。但实际上只覆盖 prompt-chain（rewrite/continuation），不覆盖 retrain-chain（模型在合成数据上再训练后生成的文本）。Section 6 Discussion 承认 retrain-chain 的 K*_empirical 不同（"elevated retrain-chain signal arises from cumulative model-adaptation artifacts"），且 Appendix D.1 只有一个 Pythia-1.4B LoRA retrain 实验。标题的 scope 远大于实际实验的 scope。
- 建议：(1) 在标题中添加限定词（如"Prompt-Chain Synthetic Text"），或 (2) 在 Abstract 首句即明确 scope 限定。

**W5** [warning] 下游 validation 不够充分
- 具体位置：Section 5, Table 5
- 问题：Section 5 的 K*-guided filtering 实验仅在一个模型（Qwen2.5-1.5B）、一个数据集（C4）、一个下游任务（MMLU/HellaSwag fine-tuning）上验证。Binary-ours 仅比 no-filter 提高 MMLU ~0.74 pp（0.5941 vs. 0.5867），效果微弱且 Figure 5 的 error bar 跨越 baseline。这不足以支持 Section 1 中 contribution (c) 声称的"K*_empirical=2 correctly predicts the strategy ordering"。
- 建议：至少在 2-3 个不同模型/任务上验证 filtering 策略，或降低对这部分贡献的 claim 力度。

---

## 小问题（不影响接收）

- **M1**: Abstract 信息密度偏高。一个段落内包含 task definition、K*_empirical definition、θ=0.60、Cohen's h、6/10 configurations、2/6 families、scale-dependent split、one-wash laundering、binary filtering、cross-model transfer、三条 contributions。建议精简至核心 claim + 数字。
- **M2**: "one-wash laundering" 术语借自金融犯罪领域，虽然 evocative 但可能在审稿中被认为 sensationalized。考虑是否有更中性的表述（如 "single-pass saturation"）。
- **M3**: Table 1 只展示了 7 个配置（Qwen-rw, Qwen-cont, Qwen-base, Pythia, Pythia-3(?), OLMo, Qwen-7B），但 abstract 声称 10 个配置。剩余 3 个（LLaMA-8B, Mistral-7B, Gemma-2-2B）仅在 Appendix Table 9 出现。建议在正文 Table 1 或至少在 Section 3.3 明确列出全部 10 个。
- **M4**: Limitations section 长度适当（约 3 个主要点 + 细节），符合要求。
- **M5**: 未发现明显的匿名违规。
- **M6**: 正文在第 8 页结束（第 530 行后大片空白），References 从第 9 页开始，Limitations 在 References 之前。格式合规，正文 ≤ 8 页。
- **M7**: Figure/Table 编号连续（Figure 1-5, Table 1-26），标题清晰。
- **M8**: 参考文献格式基本一致，但建议统一检查 arXiv preprint 的格式（部分有 venue 部分没有）。
- **M9**: 在全文范围内未发现明显的 em-dash（破折号）在正常行文中的使用，en-dash 仅用于数字范围（如 1B–8B），写作规范符合要求。
- **M10**: Reproducibility 方面，论文未明确承诺 code/data release，建议在 camera-ready 中添加。

---

## Questions for Authors

**Q1**: 如果在 70B+ 模型上 K*_empirical=1（如 Discussion Section 6 推测），这是否意味着 K*_empirical 框架在最重要的实际场景下本质上退化为 binary detection？你们如何看待这一框架的长期价值？

**Q2**: Geng et al. (2026) "Markovian Generation Chains in LLMs" 研究了非常相似的迭代生成链收敛现象。你们的 K*_empirical 度量与他们的 convergence/recurrence 分析有什么关系？是否考虑过他们的理论框架可以解释 K*_empirical 为何总是很小？

**Q3**: θ=0.60 的选择对应"small" effect size (Cohen's h=0.20)。如果使用"negligible" (h=0.10, AUC≈0.55) 或 "medium" (h=0.50) 标准，K*_empirical 的分布会如何变化？

**Q4**: Table 5 中 Binary K* filtering 的 MMLU 改善（0.5941 vs. 0.5867 = +0.74pp）是否在统计上显著？Error bar 是否 overlapping？

---

## Missing References

1. **Geng, Mingmeng, et al. "Markovian Generation Chains in Large Language Models." arXiv:2603.11228, March 2026.** — 直接研究 LLM 迭代生成链的演变，定义 Markovian generation chains，发现输出收敛行为。与本文的 prompt-chain depth estimation 高度相关，必须讨论。

2. **Shahriar, Sadat, Navid Ayoobi, and Arjun Mukherjee. "The Erosion of LLM Signatures: Can We Still Distinguish Human and LLM-Generated Scientific Ideas After Iterative Paraphrasing?" arXiv:2512.05311, December 2025.** — 量化迭代 paraphrasing 后 detection 性能随深度衰减（~25.4% over 5 stages），直接相关。

3. 可能还应考虑 **ordinal regression/classification** 的更现代方法文献（本文仅用 Frank and Hall 2001 的 OBD），如 Gutiérrez et al. (2016) "Ordinal Regression Methods: Survey and Experimental Study" 或更新的深度学习 ordinal regression 工作，以说明 OBD 是合理的 baseline 选择。

---

## Limitations 和 Ethics Statement 评估

- **Limitations**: 覆盖了 scope（模型规模 ≤8B）、protocol（prompt-chain only）、threshold sensitivity、marginal boundary、generation length 等主要限制，长度适当。但建议增加对 generation prompt template 多样性的讨论（当前使用固定 prompt，真实场景 prompt 多样性远高于此）。
- **Ethics Statement**: 讨论了 data curation 的正面用途和 detection evasion 的双用风险，内容充分。

---

## 总结

本文提出了有意义的研究问题，实验系统性和统计严谨性值得肯定。但核心贡献存在内在悖论（建立 ordinal framework 后证明 binary suffices），叙事框架有不一致之处（6/10 vs. section heading），且遗漏了高度相关的 2025–2026 工作。当前版本适合 Findings，若能在 rebuttal 中 (1) 解决贡献悖论的 framing，(2) 补充 missing references 讨论，(3) 澄清叙事不一致，有潜力提升至 Borderline Conference。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2466 · 2026-05-22T08:03:52.926770+00:00_

Reviewer 2 审稿已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 187

## Round 187

6 recorded events


### User

_source line 2467 · 2026-05-22T08:03:55.730599+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计 + 统计有效性

### Summary

本文提出 K*_empirical，一个递归合成文本代际深度判别边界的操作性下界。通过 15 维统计特征（surprisal 矩、导数、词汇多样性、频率尾部）和 OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族，1B-8B）、3 个文本域、4 种解码策略上度量 K*_empirical。核心发现：通用 web 文本（C4/Wikipedia）K*_empirical = 2，结构化学术文本（arXiv）K*_empirical = 3，表明"一次洗白"效应——一轮生成即可使文本与更深层递归内容不可区分。一致性检验显示 K*=2 正确预测了二元过滤优于渐进式替代方案。

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 度量指标新颖且定义清晰，C4 主实验统计验证扎实，但 arXiv K*=3 缺乏置信区间、Qwen 过度代表使 headline 数字产生误导、filtering 一致性检验在现实污染比例下失去统计显著性，整体处于 Conference 与 Findings 之间。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | C4 主实验有完整 CI+permutation test；但 arXiv 边界对无 CI、多重比较未校正、ANOVA 独立性假设被违反 |
| Excitement | 3/5 | "一次洗白"发现具实际意义，但实质结论是"二元检测即可"，对社区的推进幅度有限 |
| Reproducibility | 4/5 | 特征定义完整（Table 14）、超参数公开（Table 15）、5-fold GroupKFold 描述清晰；但代码未提供 |
| Confidence | 4/5 | 仔细审查了公式、CI 数值、表格一致性、统计方法 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] arXiv K*=3 缺乏置信区间，统计验证不完整

- 具体位置：Table 4 (Section 4.6)、Abstract contribution (b)
- 问题：K*=3 for arXiv 被列为独立贡献（contribution (b)），但边界对（2v3 AUC = 0.6436 / 0.6545）没有报告 bootstrap CI，也没有 permutation p-value。C4 主实验对所有边界对都提供了完整 CI（Table 2），arXiv 结果作为单独贡献却缺乏同等级别的统计验证，标准不一致。
- 此外，仅 2 个模型家族（Qwen-1.5B, Pythia-1.4B）、n=2,200（低于 C4 的 5,000），验证覆盖明显不足。
- 为什么影响接收：一个无法被读者独立验证的 boundary claim 不应作为 paper 的独立贡献出现。如果 2v3 CI 下界低于 θ=0.60，K*=3 claim 将不成立。
- 建议修改方向：(1) 为 arXiv 2v3 对补充 bootstrap 95% CI 和 permutation p-value；(2) 如果 CI 支持 K*=3，在 Table 4 中直接展示；(3) 在 Abstract/Conclusion 中增加对 arXiv 覆盖受限的 caveat（仅 2 families, reduced n）。

**N2** [critical] Qwen 过度代表导致 headline 统计产生误导

- 具体位置：Abstract ("6/10 configurations"), Section 4.1, Conclusion
- 问题：K*≥2 的 6/10 配置中，4 个是 Qwen 变体（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B）。按架构族统计：仅 2/6 族一致 K*=2（Qwen, LLaMA），3/6 族 K*=1（OLMo, Mistral, Gemma），Pythia 分裂。Abstract 虽含 "2 of 6 families unanimously" 的说明，但读者的第一印象仍是 "6/10"，而这个数字被 Qwen 家族的 4 个内部变体（mode/base-instruct/scale 消融）严重膨胀。
- Per-family 视角下，K*=2 的多数证据来自单一架构族（Qwen 贡献 4/6 observations），跨族验证仅有 Pythia-1.4B 和 LLaMA-8B 各 1 个数据点。
- 为什么影响接收：如果审稿人或读者按 family 而非 config 计数，paper 的核心发现从 "多数配置 K*=2" 变为 "仅 2 个族一致 K*=2，另外 3 个族 K*=1"，结论的普适性大幅减弱。
- 建议修改方向：(1) Abstract/Conclusion 中将 per-family 统计放到与 "6/10" 同等突出的位置，例如 "K*_empirical=2 in 6/10 configurations (driven by 2/6 families: Qwen, LLaMA; 3/6 families yield K*=1)"；(2) 正文中增加一段 per-family 分析，承认 Qwen 的 4 个 configs 本质上是同一族的消融实验，不应与跨族证据等权计数；(3) 考虑在 Table 2 中增加 family-level 汇总行。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] K*_empirical ≤ K*_theory 的 conjecture 陈述混淆了两个独立论点

- 具体位置：Section 3.1, Eq. 1 下方段落
- 问题：Paper 声称 "We conjecture that K*_empirical provides a lower bound on K*_theory" 并援引 DPI 作为论证。但这个 lower bound 性质从特征子集关系就能直接推出：K*_theory 使用最优特征，15D 特征是其子集，最优特征的 AUC 不可能低于子集特征的 AUC，因此 K*_empirical ≤ K*_theory 是 trivially true。DPI 被用于 motivate AUC 的单调衰减，但与 lower bound 性质无关。将两个论点（单调性 vs. 下界性）混为一谈会让读者误以为 lower bound 需要 DPI 成立才能保证。
- 建议：将 lower bound 性质作为 direct consequence of feature subset 直接声明（不需要 "conjecture"），将 DPI 仅用于 motivate 经验观察到的单调衰减模式。

**W2** [warning] 边界 CI 决策缺乏多重比较校正

- 具体位置：Section 4.1, Table 2
- 问题：K*_empirical 的分类决策基于"CI 下界是否超过 θ"，涉及 10 个配置的边界对（至少 10-20 个比较）。未应用 Bonferroni 或 FDR 校正。Qwen-cont 的 CI 下界仅超 θ 0.002（0.602 vs. 0.60），在校正后 99.5% CI 下很可能跌破 θ。
- Permutation p < 0.001 可以存活 Bonferroni 校正（10 comparisons → α = 0.005），但 CI-based 决策和 p-value 决策给出不同结论时，应取更保守的一方。
- 建议：(1) 报告 Bonferroni-corrected CIs；(2) 或至少在 Discussion 中承认 Qwen-cont 在校正后可能降级为 K*=1，与 cross-scorer 结果一致。

**W3** [warning] Filtering 一致性检验在现实污染比例下失去显著性

- 具体位置：Section 5, Appendix D.8 (Table 25)
- 问题：主实验使用 100% 合成数据展示 binary-ours 优势（-1.53pp → -0.77pp, p_corr < 0.05），但 dose-response 分析显示：10% 污染时三种策略完全不可区分（Δ_max = 0.03pp, p > 0.8），50% 时 binary-ours 的 0.24pp 优势仍不显著（p = 0.12）。
- 这实质上表明 K*-aware filtering 在实际可能遇到的污染比例下没有统计显著的实际收益。但 dose-response 分析被放在 Appendix 中，Section 5 的正文给读者留下了 filtering 有实际价值的印象。
- 建议：(1) 在 Section 5 正文中增加一段明确引用 dose-response 结果；(2) 或将 Table 25 移入正文。

**W4** [warning] ANOVA 使用非独立观测值

- 具体位置：Table D.2 (Appendix D.2), Section 4.2
- 问题：三因素 ANOVA 将 5-fold CV 的 fold 作为独立重复观测（N=300 = 12 cells × 5 depth-pairs × 5 folds）。GroupKFold 下各 fold 共享 80% 训练数据，违反独立性假设，可能膨胀 F 统计量。Scorer 效应的 η²_p = .166 虽然 modest，但其显著性（p < .001, F=17.48）可能被高估。
- 建议：使用 mixed-effects model 将 fold 作为 random effect，或至少在 Discussion 中注明此局限。

---

## 小问题（不影响接收）

- M1：OLMo 违反 AUC 单调衰减（2v3 = 0.497 < 3v4 = 0.502，Table S2b）。Paper 限定 "monotonically above θ" 技术上成立，但应显式注明 sub-threshold 非单调性的存在。

- M2：Table 2（正文）仅展示 5/10 配置，另外 5 个在 Table S2b（Appendix）。对于声称 "10 model configurations" 的论文，正文中应展示全部或至少提供更完整的汇总。

- M3：Neural probe 结果（Section 4.5）中 Qwen K*_neural = 3 被归因于 "self-familiarity artifacts"，但未做交叉验证（如 Qwen embeddings 上训练、Pythia-generated 文本上测试）。这一替代解释是合理推测而非实验验证。

- M4：Abstract/Conclusion 声称 "1B-8B"，但 K*=2 在此范围内并非普遍成立（OLMo-1B K*=1, Gemma-2-2B K*=1, Mistral-7B K*=1）。建议改为 "across specific models within 1B-8B" 或列出 K*=2 成立的具体模型。

- M5：Limitations 部分覆盖 7 个点，内容充实但篇幅约一整页。EMNLP 2026 要求 Limitations 不计入页数限制但不应包含过多额外内容。当前版本接近边界但可接受。

---

## Questions for Authors

Q1: 能否提供 arXiv 2v3 边界对的 bootstrap CI？无 CI 的情况下读者无法判断 K*=3 是稳健结果还是边界情况。

Q2: Eq. 1 的 ∀j 约束被描述为因经验单调性而"naturally satisfied"。在初步实验中是否观察到过 above-θ 的非单调情况？

Q3: Filtering 评估仅使用 Qwen-1.5B continuation-mode 文本（K*=2）。对 K*=1 的生成器（如 OLMo），filtering 分析会怎样？论文提到这是 future work，但能否提供粗略估计？

Q4: 对 cross-scorer ANOVA，是否考虑过用 mixed-effects model 处理 CV fold 的非独立性？

Q5: Paper 聚焦 prompt-chain 而非 retrain-chain，理由是前者隔离了文本内在退化。但实际 web-scale 污染可能两种机制共存。两种 protocol 的 K* 如何交互？

---

## Missing References

未发现严重遗漏。Related Work 覆盖了 binary detection、model collapse、data selection 的主要工作。建议增加：
- 如果存在尝试多级别（而非二元）污染检测的工作，应在 Related Work 中讨论以更清晰地定位本文贡献。

---

## Overall Assessment

**Overall**: 3.5 (Borderline Conference)
**Soundness**: 3.5/5
**Excitement**: 3/5
**Confidence**: 4/5

本文解决了一个真实的研究空白（无方法估计代际深度），指标定义清晰，C4 主实验在统计验证方面做得扎实（bootstrap CI + permutation test + 多维度敏感性分析），"一次洗白"发现具有实际意义。

阻碍 Conference 推荐的主要问题：(1) arXiv K*=3 作为独立贡献但缺乏与 C4 同等级别的统计验证（无 CI，仅 2 families，reduced n）；(2) headline "6/10" 被 Qwen 膨胀，per-family 视角下证据较弱（2/6 unanimous vs. 3/6 K*=1）；(3) Filtering 在现实污染比例下无显著收益（dose-response p > 0.12 at ≤50%），削弱实际应用价值；(4) 边界 CI 决策缺乏多重比较校正，最边界的 Qwen-cont 可能不稳健。

如果补充 arXiv CI 并加强 per-family framing，可达到 Findings 水准；进一步补充更多 non-Qwen 模型的 K*=2 证据，可达到 Conference 水准。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2468 · 2026-05-22T08:04:30.270769+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix、Should-Fix 和关键 Minor 问题：\n- **[AGREE]**：同意该问题存在，说明理由\n- **[REBUT]**：不同意或认为严重性不同，提供具体证据（cite Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] 核心贡献的内在悖论未充分解决\n- 论文叙事\"提出 ordinal depth estimation → 构建 K*_empirical 框架 → 发现 binary 已足够\"造成根本性张力。如果最终结论是 binary detection suffices，ordinal estimation 框架的增量贡献是什么？Contribution (a) 的\"first measurement of K*_empirical\"在 K*≈2 下退化为\"first generation is detectable, rest is noise\"，与已有 binary detection 文献高度一致。\n\n**N2** [critical] Abstract 与正文叙事框架存在不一致\n- Abstract 说 \"6/10 configurations (2 of 6 families unanimously)\"，但 Section 4.1 标题是 \"K*_empirical ≥ 2 Across Model Configurations (C4)\"，暗示所有 10 个配置都满足 K*≥2。标题与实际数据之间存在误导。\n\n**N3** [critical] 遗漏高度相关的近期工作\n- (1) Geng et al. (March 2026), \"Markovian Generation Chains in LLMs\" (arXiv 2603.11228)：研究 LLM 迭代处理链中文本演变，定义 Markovian generation chains。\n- (2) Shahriar et al. (Dec 2025), \"The Erosion of LLM Signatures\" (arXiv 2512.05311)：量化迭代 paraphrasing 后 detection 性能随深度衰减 ~25.4%。\n\n### Should-Fix\n\n**W1** [warning] θ=0.60 的 justification 存在潜在循环性——\"small effect size\" 本身主观。\n**W2** [warning] 模型规模限制（1B-8B）削弱实用性——大模型可能 K*=1。\n**W3** [warning] 文档长度（256 tokens）代表性不足——512 tokens 时 CI 已 marginal。\n**W4** [warning] 标题 \"Recursive Synthetic Text\" 暗示覆盖所有类型，实际仅 prompt-chain。\n**W5** [warning] Filtering 仅在单一模型/数据集/任务上验证，效果微弱（+0.74pp MMLU）。\n\n### Minor\nM1-M10 包括 Abstract 信息密度、\"one-wash laundering\" 术语、Table 1 仅 7/10 配置、参考文献格式等。\n\n### Questions\nQ1: 70B+ 模型 K*=1 时框架是否退化为 binary detection？\nQ2: 与 Geng et al. (2026) Markovian generation chains 的关系？\nQ3: θ 在 negligible/medium effect size 下 K* 的分布？\nQ4: Table 5 中 filtering 改善是否统计显著？\n\n### Missing References\n1. Geng et al. (2026) Markovian Generation Chains\n2. Shahriar et al. (2025) Erosion of LLM Signatures\n3. 更现代的 ordinal regression/classification 方法文献"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Must-Fix、Should-Fix 和关键 Minor 问题：\n- **[AGREE]**：同意该问题存在，说明理由\n- **[REBUT]**：不同意或认为严重性不同，提供具体证据（cite Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿报告\n\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] 核心贡献的内在悖论未充分解决\n- 论文叙事\"提出 ordinal depth estimation → 构建 K*_empirical 框架 → 发现 binary 已足够\"造成根本性张力。如果最终结论是 binary detection suffices，ordinal estimation 框架的增量贡献是什么？Contribution (a) 的\"first measurement of K*_empirical\"在 K*≈2 下退化为\"first generation is detectable, rest is noise\"，与已有 binary detection 文献高度一致。\n\n**N2** [critical] Abstract 与正文叙事框架存在不一致\n- Abstract 说 \"6/10 configurations (2 of 6 families unanimously)\"，但 Section 4.1 标题是 \"K*_empirical ≥ 2 Across Model Configurations (C4)\"，暗示所有 10 个配置都满足 K*≥2。标题与实际数据之间存在误导。\n\n**N3** [critical] 遗漏高度相关的近期工作\n- (1) Geng et al. (March 2026), \"Markovian Generation Chains in LLMs\" (arXiv 2603.11228)：研究 LLM 迭代处理链中文本演变，定义 Markovian generation chains。\n- (2) Shahriar et al. (Dec 2025), \"The Erosion of LLM Signatures\" (arXiv 2512.05311)：量化迭代 paraphrasing 后 detection 性能随深度衰减 ~25.4%。\n\n### Should-Fix\n\n**W1** [warning] θ=0.60 的 justification 存在潜在循环性——\"small effect size\" 本身主观。\n**W2** [warning] 模型规模限制（1B-8B）削弱实用性——大模型可能 K*=1。\n**W3** [warning] 文档长度（256 tokens）代表性不足——512 tokens 时 CI 已 marginal。\n**W4** [warning] 标题 \"Recursive Synthetic Text\" 暗示覆盖所有类型，实际仅 prompt-chain。\n**W5** [warning] Filtering 仅在单一模型/数据集/任务上验证，效果微弱（+0.74pp MMLU）。\n\n### Minor\nM1-M10 包括 Abstract 信息密度、\"one-wash laundering\" 术语、Table 1 仅 7/10 配置、参考文献格式等。\n\n### Questions\nQ1: 70B+ 模型 K*=1 时框架是否退化为 binary detection？\nQ2: 与 Geng et al. (2026) Markovian generation chains 的关系？\nQ3: θ 在 negligible/medium effect size 下 K* 的分布？\nQ4: Table 5 中 filtering 改善是否统计显著？\n\n### Missing References\n1. Geng et al. (2026) Markovian Generation Chains\n2. Shahriar et al. (2025) Erosion of LLM Signatures\n3. 更现代的 ordinal regression/classification 方法文献"
  }
}
```

</details>

---


### Tool result

_source line 2469 · 2026-05-22T08:04:41.026936+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10756
}
```

</details>

---


### Tool call

_source line 2470 · 2026-05-22T08:04:41.428848+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix、Should-Fix 和关键 Minor 问题：\n- **[AGREE]**：同意该问题存在，说明理由\n- **[REBUT]**：不同意或认为严重性不同，提供具体证据（cite Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] arXiv K*=3 缺乏置信区间，统计验证不完整\n- Table 4 的 arXiv 边界对（2v3 AUC = 0.6436 / 0.6545）无 bootstrap CI、无 permutation p-value。C4 主实验提供了完整 CI，arXiv 作为独立贡献却缺乏同等统计验证。仅 2 个模型家族、n=2,200。\n\n**N2** [critical] Qwen 过度代表导致 headline 统计产生误导\n- 6/10 K*≥2 中 4 个是 Qwen 变体。per-family 仅 2/6 unanimous K*=2，3/6 K*=1。\"6/10\" 被 Qwen 的内部消融严重膨胀。\n\n### Should-Fix\n\n**W1** [warning] K*_empirical ≤ K*_theory 的 conjecture 混淆——lower bound 从特征子集关系可直接推出，不需要 DPI。\n**W2** [warning] 边界 CI 决策缺乏多重比较校正——Qwen-cont CI 下界仅超 θ 0.002，Bonferroni 校正后可能跌破。\n**W3** [warning] Filtering 在现实污染比例下失去显著性——dose-response 分析（50% p=0.12）被放在 Appendix。\n**W4** [warning] ANOVA 使用非独立观测值——GroupKFold 各 fold 共享 80% 训练数据，违反独立性假设。\n\n### Minor\nM1: OLMo sub-threshold 非单调性未显式标注\nM2: 正文 Table 仅展示 5/10 配置\nM3: Neural probe \"self-familiarity\" 归因为推测而非实验验证\nM4: \"1B-8B\" claim 但 K*=2 并非普遍成立\nM5: Limitations 篇幅约一整页\n\n### Questions\nQ1: arXiv 2v3 的 bootstrap CI？\nQ2: 是否观察到 above-θ 非单调？\nQ3: K*=1 生成器上 filtering 会如何？\nQ4: ANOVA 是否考虑 mixed-effects？\nQ5: Prompt-chain 和 retrain-chain 的 K* 如何交互？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Must-Fix、Should-Fix 和关键 Minor 问题：\n- **[AGREE]**：同意该问题存在，说明理由\n- **[REBUT]**：不同意或认为严重性不同，提供具体证据（cite Section/Table/Figure）\n\n---\n\n## Reviewer 1 — Round 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] arXiv K*=3 缺乏置信区间，统计验证不完整\n- Table 4 的 arXiv 边界对（2v3 AUC = 0.6436 / 0.6545）无 bootstrap CI、无 permutation p-value。C4 主实验提供了完整 CI，arXiv 作为独立贡献却缺乏同等统计验证。仅 2 个模型家族、n=2,200。\n\n**N2** [critical] Qwen 过度代表导致 headline 统计产生误导\n- 6/10 K*≥2 中 4 个是 Qwen 变体。per-family 仅 2/6 unanimous K*=2，3/6 K*=1。\"6/10\" 被 Qwen 的内部消融严重膨胀。\n\n### Should-Fix\n\n**W1** [warning] K*_empirical ≤ K*_theory 的 conjecture 混淆——lower bound 从特征子集关系可直接推出，不需要 DPI。\n**W2** [warning] 边界 CI 决策缺乏多重比较校正——Qwen-cont CI 下界仅超 θ 0.002，Bonferroni 校正后可能跌破。\n**W3** [warning] Filtering 在现实污染比例下失去显著性——dose-response 分析（50% p=0.12）被放在 Appendix。\n**W4** [warning] ANOVA 使用非独立观测值——GroupKFold 各 fold 共享 80% 训练数据，违反独立性假设。\n\n### Minor\nM1: OLMo sub-threshold 非单调性未显式标注\nM2: 正文 Table 仅展示 5/10 配置\nM3: Neural probe \"self-familiarity\" 归因为推测而非实验验证\nM4: \"1B-8B\" claim 但 K*=2 并非普遍成立\nM5: Limitations 篇幅约一整页\n\n### Questions\nQ1: arXiv 2v3 的 bootstrap CI？\nQ2: 是否观察到 above-θ 非单调？\nQ3: K*=1 生成器上 filtering 会如何？\nQ4: ANOVA 是否考虑 mixed-effects？\nQ5: Prompt-chain 和 retrain-chain 的 K* 如何交互？"
  }
}
```

</details>

---


### Tool result

_source line 2471 · 2026-05-22T08:04:43.043524+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1614
}
```

</details>

---


### Assistant

_source line 2472 · 2026-05-22T08:04:46.121141+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 188

## Round 188

2 recorded events


### User

_source line 2473 · 2026-05-22T08:04:47.361609+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿已完成并提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**，Confidence 4/5。

主要发现：
- **3 个 Must-Fix**：(1) 核心贡献存在内在悖论——建立 ordinal depth estimation 框架后结论是 binary 足矣，增量贡献论证不充分；(2) Abstract "6/10 configurations" 与 Section 4.1 标题 "K*_empirical ≥ 2 Across Model Configurations" 存在误导性矛盾；(3) 遗漏两篇高度相关近期工作（Geng et al. 2026 "Markovian Generation Chains"，Shahriar et al. 2025 "Erosion of LLM Signatures"）
- **5 个 Should-Fix**：θ=0.60 阈值 justification 循环性、模型规模限制（1B–8B）、256-token 文档长度限制、标题 scope 过宽、下游 validation 不充分
- **优势**：实验系统性强（10 configs × 3 domains × 4 decoding）、统计严谨（bootstrap CI + permutation test）、practical recommendation 清晰

---

[Reviewer 1 审稿结果]:
审稿完成，已提交至 Review Director。

审稿结论：**Overall 3.5（Borderline Conference）**。

核心判断：C4 主实验统计验证扎实，"一次洗白"发现有实际意义，但有两个 Must-Fix 问题阻碍 Conference 推荐：

1. **arXiv K*=3 缺乏 CI** — 作为独立贡献却无 bootstrap CI 和 permutation p-value，与 C4 实验的验证标准不一致
2. **Qwen 过度代表** — "6/10 configurations" 中 4 个是 Qwen 变体，per-family 视角仅 2/6 族一致 K*=2

另有 4 个 Should-Fix（K*≤K*_theory conjecture 陈述混淆、多重比较未校正、filtering 在现实污染比例下失去显著性、ANOVA 独立性假设违反）和 5 个 Minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2474 · 2026-05-22T08:04:58.810707+00:00_

两位 Reviewer 的 Round 1 初审已收齐，交叉分享任务已派发。等待交叉回应返回后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 189

## Round 189

2 recorded events


### User

_source line 2475 · 2026-05-22T08:06:34.826475+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 回应

**[AGREE] R1-N1: arXiv K*=3 缺乏置信区间**
同意这是一个实质性缺陷。Table 2（C4 主实验）提供了完整的 bootstrap 95% CI 和 permutation p-value，但 Table 4（cross-domain）仅报告点估计 AUC。arXiv K*=3 是论文中少数 K*>2 的发现，具有独立贡献价值（Section 4.3, Section 6 "Representation dependence" 段落均以此为论据），缺乏统计验证会使读者无法判断这一结论的稳健性。补充：Table 21（Appendix, p.19）展示了三域 pairwise AUC 的进一步分解（arXiv 2v3=0.6436），同样无 CI。建议 severity 维持 critical——如果 CI 跨越 θ=0.60，K*=3 的 claim 直接失效。

**[AGREE] R1-N2: Qwen 过度代表膨胀 "6/10" headline**
这是我在自己审稿中也想指出但未单独拆出的问题（我在 N2 中提到了 abstract 与正文叙事框架不一致，但 R1 的角度更精确）。10 个配置中 4 个来自 Qwen 家族（Qwen-rw, Qwen-cont, Qwen-base, Qwen-7B），本质上是同一家族的内部消融。per-family 统计——仅 2/6 families unanimously K*≥2（Qwen 和 LLaMA）——更诚实且信息量更高。"6/10 configurations" 在 abstract 中作为 headline 数字会误导读者高估结论的泛化性。

不过我补充一个 nuance：论文 abstract 确实在括号中注明了 "(2 of 6 families unanimously)"，说明作者意识到了这个区分。问题在于叙事权重——"6/10" 在前、"2/6" 在括号中，心理效应上前者主导了读者印象。建议将 per-family 统计提至首位（如 "2 of 6 model families consistently yield K*_empirical ≥ 2, spanning 6/10 individual configurations including within-family variants"）。

---

### Should-Fix 回应

**[AGREE] R1-W1: DPI conjecture 混淆——lower bound 可直接推出**
同意 R1 的判断。K*_empirical ≤ K*_theory 的关系从"15 维统计特征是原始文本的有损压缩"即可直接推出——任何特征子集的区分能力不会超过完整信号。DPI 提供了信息论的形式化框架，但论文中的使用方式（Section 3.1, "heuristic motivation for expecting AUC_{k,k+1} to decrease"）实际上是将 DPI 用作启发式 motivation 而非严格证明，这种模糊处理容易误导读者以为存在更强的理论保证。建议要么给出完整的 DPI 推导链（从 Markov chain → mutual information → AUC bound），要么简化为 R1 建议的直接论证。

**[AGREE] R1-W2: 边界 CI 需要多重比较校正**
强烈同意。Qwen-cont 的 CI 下界仅超 θ 0.002（Section 4.1 报告），这在单次检验下就已经是 borderline。10 个配置同时检验，按 Bonferroni 校正 α_adjusted = 0.05/10 = 0.005，如此窄的 margin 极可能跌破阈值。这直接影响 "6/10 K*≥2" 的 count——如果 Qwen-cont 跌落，变成 "5/10"。这进一步加强了 R1-N2 关于 headline 统计膨胀的论点。我在自己的审稿中将此列为 θ sensitivity 的 W1 问题，但 R1 的 multiple comparison 角度更精准。

**[AGREE] R1-W3: Filtering 在现实污染比例下失去显著性**
同意。这与我在 W5 中指出的下游 validation 不充分问题高度一致。Section 5 主实验用 100% 合成数据替换，但 Appendix D.8 的 dose-response 分析显示：在 50% 污染比例（更接近现实场景）下 p=0.12，未达统计显著。论文的实际指导价值（"use binary K* filtering for data curation"）在现实条件下缺乏 evidence 支撑。将这个关键结果放在 Appendix 而非正文，有 cherry-picking 主实验条件的嫌疑。

**[REBUT] R1-W4: ANOVA 使用非独立观测值**
部分不同意 severity 评估。R1 正确指出 GroupKFold 各 fold 共享约 80% 训练数据，违反 ANOVA 独立性假设。但需要注意：(1) ANOVA 在论文中用于 Table 2 旁注的 feature importance 分析（Section 3.2 的 Spearman ρ agreement 和 Section 4.3 Feature Ordering 的 ANOVA），不是用来支持核心 K*_empirical 结论的——K*_empirical 的判定基于 bootstrap CI 和 permutation test，这两个方法对 fold 依赖性有一定容忍度；(2) GroupKFold 本身是为了避免 document-level leakage（同一文档的不同 depth 不出现在 train/test 两侧），选择是合理的。问题是 ANOVA 的 p-value 可能偏乐观，但这影响的是 feature importance 排序的可信度，而非 K*_empirical 的核心结论。建议将 severity 从 should-fix 降至 minor 级别，并在文中注明 ANOVA p-value 可能因 fold overlap 而偏低。

---

### Minor 回应

**[AGREE] R1-M1: OLMo sub-threshold 非单调性未标注**
同意。OLMo-1B 的 AUC 从 1v2 到 2v3 再到更高 depth pair 的变化如果存在非单调性（某个 pair 的 AUC 反而上升），这与 DPI 的单调递减预期不符，应该在正文中显式讨论而非隐藏。

**[AGREE] R1-M2: 正文 Table 仅展示 5/10 配置**
与我的 M3 观点一致。10 个配置是 abstract 的 headline 数字，正文 Table 1-2 却只展示部分，剩余在 Appendix Table 9。这会让读者质疑被 defer 到 appendix 的配置是否因为结果不利才被移出正文。

**[AGREE] R1-M3: Neural probe "self-familiarity" 归因为推测**
Section 4.5 的 neural probe 实验（Table 3）展示了 frozen encoder MLP 对 depth 的分类能力，但对"self-familiarity"的解释确实是 post-hoc speculation 而非实验验证。论文说 "neural probe extends it by one level for some architectures"，但未提供 controlled experiment 来验证这一机制（如：对比在 same-family vs. cross-family 生成文本上的 probe 性能差异是否真的由 familiarity 驱动）。

**[REBUT] R1-M4: "1B-8B" claim 但 K*=2 非普遍成立**
这与 N2 有重叠。我认为 "1B-8B" 的表述准确描述了实验覆盖的模型规模范围，不是在声称该范围内所有模型都有 K*=2。问题出在 "6/10 K*≥2" 的 headline 表述（N2 已覆盖），而非模型规模描述本身。

**[REBUT] R1-M5: Limitations 篇幅约一整页**
不同意这是问题。EMNLP 2026 规则明确"Mandatory limitations ... do not count towards this page limit"。Limitations 覆盖了 5 个实质性限制点（scope, protocol, threshold, boundary, length），内容翔实而非冗余。一页篇幅在 ARR 投稿中属于正常范围，比过于简短的 Limitations 更好——简短反而可能被 reviewer 标记为"insufficient discussion of limitations"。

---

### 对 R1 Questions 的补充意见

**Q1 (arXiv CI)**: 同意这是作者必须在 rebuttal 中提供的数据。
**Q2 (above-θ 非单调)**: 好问题，与 DPI 预期直接相关。
**Q3 (K*=1 生成器上 filtering)**: 有实际价值——如果 K*=1（第一代已不可区分），binary filtering 也会失效，这进一步削弱了 Section 5 的实用性主张。
**Q4 (mixed-effects ANOVA)**: 见我对 W4 的 rebut——ANOVA 不是核心结论的基础，但 mixed-effects 确实更合适。
**Q5 (prompt-chain vs. retrain-chain 交互)**: 这与我的 W4 (prompt-chain 限定 vs. 标题泛化) 一致，是一个重要的 scope 问题。

---

### 总体评价差异

R1 给了 3.5 (Borderline Conference)，我给了 3.0 (Findings)。差异主要来自对贡献悖论的权重不同：我认为"建立 ordinal framework 后证明 binary suffices"这个内在张力是一个更根本的贡献定位问题（我的 N1），而 R1 更关注具体的统计缺陷和叙事准确性。如果作者能 (1) 提供 arXiv CI, (2) 修正 headline 统计, (3) 更好地 frame 贡献悖论，我认为 3.0→3.5 是可能的，但需要同时解决我和 R1 的 must-fix 问题。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2476 · 2026-05-22T08:06:40.043708+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 190

## Round 190

2 recorded events


### User

_source line 2477 · 2026-05-22T08:06:43.347117+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：与 R1 在 5 个 Must-Fix/Should-Fix 上达成一致（arXiv CI 缺失、Qwen 膨胀 headline、DPI 混淆、多重比较校正、filtering 现实条件失效），对 2 个问题提出了不同 severity 评估（ANOVA 非独立性降为 minor、Limitations 篇幅无问题），并补充了 R1 未涉及的贡献悖论问题（我的 N1）。两人评分差异 0.5 分（R1: 3.5, 我: 3.0），主要分歧在于对核心贡献定位问题的权重。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2478 · 2026-05-22T08:06:48.114139+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director"
}
```

</details>

---


## Round 191

## Round 191

10 recorded events


### User

_source line 2479 · 2026-05-22T08:07:09.356883+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见

---

### Must-Fix 回应

**[AGREE with nuance] R2-N1: 核心贡献的内在悖论**

同意叙事张力存在，但不同意这构成 "fundamental paradox" 或 critical issue。

理由：ordinal framework 的贡献在于**证明** binary suffices，而不是**假设**它。具体而言：(1) 如果不通过 K*_empirical 度量边界，就无法知道 binary 是最优策略而非次优折衷——先验地，K* 完全可能是 3 或 4（事实上 arXiv K*=3）；(2) 框架揭示了 domain-dependent variation（C4 K*=2 vs. arXiv K*=3），这不是 binary detection 文献能提供的；(3) K*_empirical 同时量化了 boundary cases 的边界敏感性（Qwen-cont CI lower = 0.602），这对 practitioner 有操作性价值。

但我同意 paper 应更明确地框架 ordinal estimation 为"建立 negative result 的科学工具"而非暗示 ordinal estimation 本身有直接应用价值。这是 **Should-Fix 级别**的叙事调整，不应定为 critical。

---

**[REBUT] R2-N2: Section 4.1 标题不一致**

R2 声称 Section 4.1 标题为 "K*_empirical **≥** 2 Across Model Configurations"，暗示所有 10 个配置都满足 K*≥2。

**这是事实性错误。** 实际标题为 "K*_empirical **≤** 2 Across Model Configurations (C4)"（LaTeX 源码 experiments_c1.tex 第 9 行：`\subsection{$\Kempirical \leq 2$ ...}`）。≤ 2 表示"至多为 2"，即 K* ∈ {1, 2}，准确反映了 10 个配置的结果分布（6 个 K*=2, 4 个 K*=1）。标题没有误导——它陈述了上界，与正文数据完全一致。

R2 将 ≤ 误读为 ≥，导致了不成立的批评。此条 Must-Fix 应撤回。

---

**[AGREE] R2-N3: 遗漏高度相关近期工作**

经 Web 搜索验证，两篇论文均真实存在且高度相关：

1. **Geng et al. (March 2026)**, "Markovian Generation Chains in Large Language Models" ([arXiv:2603.11228](https://arxiv.org/abs/2603.11228))：定义 LLM 迭代推理过程为 Markovian generation chains，研究迭代 rephrasing 和 round-trip translation 中文本的收敛行为。本文 Section 3.1 同样使用 Markov chain 框架，两者的理论基础高度重叠。应在 Section 2 (Related Work) 中讨论并在 Section 3.1 的 Markov chain formulation 处引用。

2. **Shahriar et al. (Dec 2025)**, "The Erosion of LLM Signatures" ([arXiv:2512.05311](https://arxiv.org/abs/2512.05311))：量化迭代 paraphrasing 后 detection 性能衰减 ~25.4%，与本文 "one-wash laundering" 发现直接相关。应在 Section 2 中讨论，并在 Section 6 的 one-wash laundering 讨论中做对比。

但我认为此条为 **Should-Fix** 而非 Must-Fix：遗漏相关工作需要补充引用和讨论，但不改变论文的核心 contribution claim——Geng et al. 研究收敛行为而非 discrimination boundary，Shahriar et al. 研究 binary detection 衰减而非 ordinal depth estimation。两者互补但不 subsume 本文贡献。

---

### Should-Fix 回应

**[AGREE] R2-W1: θ=0.60 justification 的潜在循环性**

与我的 W1 一致。Cohen's h 从 proportions 映射到 AUC 是类比而非直接应用，permutation null 和 distributional discontinuity 依赖数据本身。但 Figure 3 的 θ 敏感性分析（Section 4.1）允许读者在任意 θ 下读取 K*，实质上提供了 θ-free 的连续度量。建议 paper 更明确地将 θ=0.60 定位为"参考操作点"而非唯一正确阈值。

**[AGREE] R2-W2: 模型规模限制（1B-8B）**

与本文 Discussion 段落 "Boundary cases and scale effect"（Section 6）一致：paper 自身推测 13B+ 可能 K*=1。Limitations 第 (1) 项也明确了 "model scale ≤8B"。此限制已被充分讨论，但 R2 的批评指出这对 practitioner 的实用性有影响——当实际应用中的主流模型已到 70B+，1B-8B 的结论难以直接迁移。同意应在 Conclusion 中更显式地限定适用范围。

**[AGREE] R2-W3: 文档长度代表性**

Table S11（Appendix）显示 512 tokens 时 1v2 CI = [0.5979, 0.6166]，下界低于 θ=0.60（Limitations 第 (6) 项已承认）。R2 的批评合理：256 tokens 是实验主力但不代表实际文档长度分布。这与 paper 的诚实讨论一致，但确实限制了实际适用性。

**[AGREE with nuance] R2-W4: 标题 "Recursive Synthetic Text" 范围过广**

Title 说 "Recursive Synthetic Text" 但只做了 prompt-chain。Retrain-chain 在 Appendix D.7 中做了验证（K*≥4），但作为对比实验而非主要贡献。标题可改为 "Prompt-Chain Recursive Synthetic Text" 以更精确，但我认为 "recursive" 本身并不专指某一种 recursion 类型，只要论文正文明确了协议（Section 3.1），标题的模糊性是可接受的。**Minor 级别**，非 Should-Fix。

**[AGREE] R2-W5: Filtering 验证范围**

与我的 W3 完全一致。单一模型（Qwen-1.5B cont）、单一数据集（C4）、单一下游任务（MMLU+HellaSwag），且效果微弱（+0.74pp MMLU）。Dose-response（Appendix D.8, Table 25）进一步显示在 ≤50% 污染下无显著差异（p > 0.12）。

---

### Minor 回应

不逐条展开。R2 的 M1-M10 多数为 presentation-level issues（Abstract 信息密度、术语选择、Table 1 配置覆盖等），与我的 M2（Table 2 仅展示 5/10 配置）和 M4（"1B-8B" 表述不精确）方向一致。

---

### Questions 回应

**R2-Q1 (70B+ K*=1 时框架退化)**: 好问题。但即使 K*=1，框架仍然有价值——它量化了 K*=1 的事实，确认 binary detection 是唯一可行策略。类比：测量温度的工具不会因为温度是 0°C 就失去价值。

**R2-Q2 (与 Geng et al. 关系)**: 如上 N3 所述，Geng et al. 研究 Markov chain 收敛行为，本文研究 discrimination boundary，两者互补。应引用并讨论。

**R2-Q3 (θ 在不同 effect size 下的 K*)**: Figure 3 已提供答案：θ=0.55 时部分 config K*=3，θ=0.70 时全部 K*=1。Paper 可考虑在正文中用一句话总结此范围。

**R2-Q4 (Table 5 filtering 显著性)**: Section 5 报告 p_corr < 0.05 for binary-ours vs. all alternatives on MMLU。显著性已报告但仅限 100% synthetic setting；dose-response 无显著性（Appendix D.8）。

---

### 总体评估对比

R2 给出 3.0 (Findings)，我给出 3.5 (Borderline Conference)。主要分歧在于：

1. **R2-N1（paradox）**：R2 视为 critical，我认为是 Should-Fix 级叙事问题。Ordinal framework 作为科学工具建立 negative result 是有效贡献模式。
2. **R2-N2（标题误导）**：R2 基于事实性误读（≤ vs ≥），此条不成立。
3. **R2-N3（missing refs）**：同意需要引用，但 Should-Fix 而非 Must-Fix——两篇工作互补但不 subsume 本文。

我维持 **Overall 3.5 (Borderline Conference)**。如果 arXiv CI 补充完整（我的 N1）且 per-family framing 调整到位（我的 N2），加上引用补充，可达 Findings 以上水准。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2480 · 2026-05-22T08:07:38.984643+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2481 · 2026-05-22T08:07:39.086151+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T07:56:03.148980+00:00\", \"completed_at\": \"2026-05-22T07:59:59.245048+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 8\", \"message\": \"主正文最后一页仅有约15行结论文字（~20%页面），剩余~75%为空白。8页限制的论文实际使用约7.2页正文，浪费近一整页空间。审稿人会认为论文内容不够充实或空间利用不当。建议将部分附录核心内容（如 Table 3 neural probe 结果的展开讨论、或 D.1/D.4 的关键发现）提升至正文。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-2\", \"message\": \"连续两页纯文本（Abstract + Introduction + Related Work），无任何 display item。第一个视觉锚点（Figure 1 pipeline 图）延迟到第3页才出现。审稿人前2分钟扫读期间无图表可锚定，影响第一印象。建议考虑将 Figure 1 提前到第2页（Related Work 之前或 Introduction 末尾嵌入）。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 7-8\", \"message\": \"Discussion（Section 6）+ Conclusion（Section 7）跨两页纯文本，与第8页大面积空白形成反差。Discussion 内容密集但无 display item 穿插，节奏单调。可考虑在 Discussion 中加入一个总结性的 figure 或 table（如 K*_empirical 结果汇总表）以打破纯文本节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 13-14\", \"message\": \"附录空间利用不均。Page 13 Table 10（两个混淆矩阵）上方约40%空白；Page 14 Table 11（per-depth recall）上方约60%空白。建议将 Table 10 和 Table 11 合并到同一页，或调整 float 位置减少空白。\"}, {\"severity\": \"warning\", \"dimension\": \"page 11\", \"message\": \"Figure 5（bar chart）中 \\\"Binary K* filtering\\\" 组的 \\\"Ours\\\" 柱的底部区域颜色非常浅（接近白色），与背景对比度低，在灰度打印时可能难以辨认。建议统一柱状图颜色饱和度或添加 hatch pattern 辅助区分。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 pipeline 图清晰、自包含，caption 准确描述了完整流程。作为第一个 display item 能有效传达核心 method。彩色方框标签清晰可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"单页包含3个 display items（Table 2 + Figure 2 + Figure 3），密度很高但排列合理，无拥挤感。Figure 2 的置信区间阴影带和 Figure 3 的灵敏度曲线都清晰可读。\"}, {\"severity\": \"info\", \"dimension\": \"pages 3-6\", \"message\": \"主要实验结果区域（pages 3-6）视觉节奏良好：text-figure-table 交替出现，display items 密度适中。\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"所有表格统一使用 booktabs 风格（toprule/midrule/bottomrule），无竖线。最优值加粗标注。小数位数在同一列内一致。表格质量专业。\"}, {\"sever
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2482 · 2026-05-22T08:07:39.086635+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "gen-depth-contamination"
  }
}
```

</details>

---


### Tool result

_source line 2483 · 2026-05-22T08:07:39.086934+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2484 · 2026-05-22T08:11:20.278164+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "gen-depth-contamination",
  "issues_yaml": "## Review Issues Tracker — gen-depth-contamination\n## Updated: Round 26 fresh review (2026-05-22)\n\n# === CRITICAL / MUST-FIX ===\n\n- id: \"R26-N1\"\n  summary: \"arXiv K*=3 缺乏 bootstrap CI 和 permutation p-value\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"Table 4 的 arXiv 2v3 AUC (0.6436/0.6545) 无 CI 无 p-value，但 C4 主实验 Table 2 对所有边界对提供了完整验证。作为独立贡献 (contribution b) 需同等统计标准。仅 2 family、n=2200。R1 列为 Must-Fix，R2 同意 severity。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N1\"\n  summary: \"Qwen 过度代表使 6/10 统计量误导\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix。6/10 中 4 个 Qwen。按 family：仅 2/6 unanimously K*=2。R1 同意表述需改但指出 K*∈{1,2} 变化范围小，one-wash 定性结论仍成立。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1 列为 Must-Fix (N2)，R2 同意。尽管 Round 25 action 已在 Abstract 添加 per-family 统计，但叙事权重仍以 '6/10' 为主导，'(2/6 families)' 仅在括号中。建议将 per-family 统计提至首位。\"\n  action_items:\n    - round: 25\n      action: \"Abstract 同时报告 per-config 和 per-family 统计；Section 4.1 添加 family-level 汇总\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING / SHOULD-FIX ===\n\n- id: \"R25-W2\"\n  summary: \"K*=2 的实际新贡献 vs binary detection 讨论不足（贡献悖论）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix：如果结论是 binary is sufficient，增量贡献不明确。R1 REBUT：K* 提供解释性价值。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 升级为 Must-Fix (N1)：ordinal framework 证明 binary 足矣构成内在悖论。R1 降为 Should-Fix：ordinal framework 作为科学工具建立 negative result 是有效贡献模式。共识：需更明确地 frame ordinal estimation 为'测量工具'而非暗示直接应用价值。\"\n  action_items:\n    - round: 25\n      action: \"Discussion 更明确阐述 K*_empirical 作为度量框架相对于 binary detection 的增量贡献\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W1\"\n  summary: \"遗漏高度相关近期工作：Geng et al. 2026, Shahriar et al. 2025\"\n  category: related_work\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix (N3)，R1 降为 Should-Fix（两篇互补但不 subsume 本文）。(1) Geng et al. (2026) 'Markovian Generation Chains in LLMs' (arXiv:2603.11228)——Markov chain 理论框架高度重叠；(2) Shahriar et al. (2025) 'The Erosion of LLM Signatures' (arXiv:2512.05311)——迭代 paraphrasing 后 detection 衰减与 one-wash laundering 直接相关。均经 web search 验证真实存在。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W2\"\n  summary: \"边界 CI 决策缺乏多重比较校正\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1 列为 Should-Fix (W2)，R2 强烈同意。10 个配置同时检验未用 Bonferroni/FDR 校正。Qwen-cont CI 下界仅超 θ 0.002，校正后可能跌破→K*=2 count 从 6/10 降为 5/10。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1\"\n  summary: \"DPI→adjacent-pair AUC 推理链存在逻辑缺口\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"应明确 DPI 是 heuristic motivation 而非 strict proof。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Must-Fix：K*_empirical 作为 K*_theory 下界仅为断言，缺形式证明。R2 同意但建议降为 Should-Fix。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1 指出 K*_empirical ≤ K*_theory 从特征子集关系可直接推出（trivially true），不需要 DPI 也不需要 conjecture。DPI 仅用于 motivate 单调衰减。两个论点（lower bound vs monotonicity）被混为一谈。R2 同意。\"\n  action_items:\n    - round: 25\n      action: \"明确区分 K*_empirical 为操作性定义 vs K*_theory 下界；后者降级为 conjecture 并阐明 AUC-MI gap\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Cohen's h 提供先验基础，但第三条 distributional discontinuity 应标为 post-hoc confirmatory。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"两位 Reviewer 最强共识点。θ∈[0.55,0.70] 内 K* 从 3 变到 1。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 指出 'small effect size' 本身主观——为何不用 medium (h=0.50)？R1 同意应将 θ=0.60 定位为'参考操作点'而非唯一正确阈值。Figure 3 提供了 θ-free 连续度量但未在正文充分讨论。\"\n  action_items:\n    - round: 25\n      action: \"报告 θ-free 指标（AUC gap 及其 CI），提供完整灵敏度曲线\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C4\"\n  summary: \"模型规模覆盖偏向小模型（≤8B），威胁可推广性\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"缺 >8B；按家族去重 K*=2 从 6/10 降为 3/6。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"共识：至少在 Abstract/Conclusion 明确限定 1B-8B 适用范围。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 再次提出：实际 web-scale 合成文本来自 100B+ 模型，Discussion 推测 '13B+ may yield K*=1' 未验证。R1 同意应在 Conclusion 更显式限定。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 显式限定 K*≈2 适用范围为 1B-8B\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Filtering 实验效果量在现实污染比例下极小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"≤50% 污染下所有策略无显著差异。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"+0.74pp MMLU 在 100% 极端条件下。Appendix D.8 ≤30% 策略差异消失。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1(W3)+R2(W5) 再次共识：dose-response (50% p=0.12) 放在 Appendix 而非正文，有 cherry-picking 嫌疑。实际指导价值在现实条件下缺乏 evidence。\"\n  action_items:\n    - round: 25\n      action: \"Section 5 引用 dose-response 分析；承认现实污染比例下边际增益可忽略\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W3\"\n  summary: \"文档长度（256 tokens）代表性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix (W3)，R1 同意。512 tokens 时 CI lower = 0.5979 < θ=0.60。真实 web 文档通常数千 tokens。Limitations 已承认但实验覆盖不足。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"Prompt-chain 生态有效性——one-wash laundering 可能是 prompt-chain 特有现象\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix（retrain-chain K*≥4 远超 prompt-chain K*=2）。R1 降为 Should-Fix。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2(W4) 提出标题 'Recursive Synthetic Text' 范围过广，暗示覆盖所有类型。R1 降为 Minor——'recursive' 不专指某一类型，正文已明确协议。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 添加 prompt-chain 限定语\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W11\"\n  summary: \"Filtering 仅在单一 generator（Qwen-1.5B cont）上验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"至少应在 K*=1 generator 上重复或在 Limitations 中声明。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix，R1 同意。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2(W5)+R1(W3) 再次提出。单一模型/数据集/任务，效果微弱 (+0.74pp MMLU)。\"\n  action_items:\n    - round: 25\n      action: \"Limitations 声明 filtering 仅单 generator 验证；Section 5 讨论 K*=1 场景\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-C2\"\n  summary: \"Cross-scorer 验证部分证伪 scorer independence claim（Qwen-cont K*=2→1）\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Qwen-cont 自身打分 K*=2 仅超 θ 0.002，Pythia/OLMo 打分均 <θ。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Should-Fix。R2 同意并补充 ensemble 也无法解决 marginal signal。\"\n    - round: 26\n      reviewer: []\n      note: \"本轮未作为独立问题提及。R26-W2（多重比较校正）覆盖了 Qwen-cont 边界脆弱性的一部分。可能已通过 Round 25 的三层 scorer independence 重写部分缓解。待 Research Director 确认。\"\n  action_items:\n    - round: 25\n      action: \"Section 4.2 更突出讨论 cross-scorer 降级对部署的影响\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R2]\n      note: \"Reviewer 有分歧，R1 认为正常。\"\n    - round: 25\n      reviewer: [R2]\n      note: \"R2 提到 Abstract 中 Cohen's h≈0.20 缺乏上下文。\"\n    - round: 26\n      reviewer: [R2]\n      note: \"R2(M1) 仍认为 Abstract 信息密度偏高——一个段落含 task definition、K*、θ、6/10、2/6、scale-dependent split、one-wash laundering 等。建议精简。\"\n  action_items:\n    - round: 25\n      action: \"Abstract 中 Cohen's h 替换为直观表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n# === MINOR ===\n\n- id: \"R25-M1\"\n  summary: \"正文 Table 仅展示部分配置（5-7/10）\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"Table 2 仅列 5 配置但声称 10。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1(M2)+R2(M3)：正文 Table 仍仅展示 5/10 配置，其余在 Appendix Table S2b。声称 '10 model configurations' 但正文不完整展示，读者可能质疑 defer 到 appendix 的配置是否因结果不利。\"\n  action_items:\n    - round: 25\n      action: \"Section 4.1 添加 1-2 句概述全部 10 配置结果\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"标题 'Recursive Synthetic Text' 范围略宽于 prompt-chain 实际覆盖\"\n  category: framing\n  severity: minor\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix (W4)，R1 降为 Minor——'recursive' 不专指某一类型，正文 Section 3.1 已明确协议。共识降为 Minor。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"ANOVA 使用 GroupKFold 非独立观测值\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1 列为 Should-Fix (W4)，R2 REBUT 降为 Minor——ANOVA 用于 feature importance 分析而非核心 K* 结论，GroupKFold 选择本身合理（避免 document leakage），p-value 可能偏乐观但影响有限。共识降为 Minor。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M3\"\n  summary: \"OLMo sub-threshold AUC 非单调性未显式标注\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1(M1)：OLMo 2v3=0.497 < 3v4=0.502 违反单调预期。Paper 限定 'monotonically above θ' 技术上成立但应标注 sub-threshold 非单调性。R2 同意。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M4\"\n  summary: \"Neural probe 'self-familiarity' 归因为推测而非实验验证\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1(M3)：Section 4.5 的 'self-familiarity artifacts' 解释为 post-hoc speculation，未做 cross-family probe 对照实验验证。R2 同意。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M3\"\n  summary: \"K*_empirical 定义中 max 算子隐含 AUC 单调递减假设\"\n  category: method\n  severity: minor\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"明确单调假设或改用连续满足条件定义。\"\n    - round: 25\n      reviewer: [R1]\n      note: \"主实验 10 配置均严格单调递减，但 threshold 以下有接近翻转的 case。\"\n    - round: 26\n      reviewer: [R1]\n      note: \"Round 25 已改为 ∀j≤k 连续满足定义，但 R1(M1) 指出 OLMo sub-threshold 非单调性应显式标注（见 R26-M3）。定义本身已改善。\"\n  action_items:\n    - round: 25\n      action: \"Eq.1 改为连续满足定义 + 声明单调性为经验观察\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n# === RESOLVED (from prior rounds) ===\n\n- id: \"R2-W3\"\n  summary: \"Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Round 24 fix expanded Conclusion; Round 25-26 did not re-raise\"\n  resolution_round: 25\n\n- id: \"R2-W1\"\n  summary: \"与 Geng et al. (2026) 和 Wang et al. (2025) 的技术区分不够清晰\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Round 24 fix added citations; Round 25-26 did not re-raise\"\n  resolution_round: 25\n\n- id: \"R24-M4\"\n  summary: \"Figure 4 热图红绿配色对色盲不友好\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 24\n  resolution: \"Round 24 fix changed to blue-orange; Round 25-26 did not re-raise\"\n  resolution_round: 25\n\n- id: \"R23-M2\"\n  summary: \"Orphan bib entries / 引用格式不一致\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  resolution: \"Round 24 fix completed; Round 25-26 did not re-raise\"\n  resolution_round: 25\n\n- id: \"R24-C1\"\n  summary: \"附录空占位符表格\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  resolution: \"Round 25 确认无空表\"\n  resolution_round: 25\n\n- id: \"R2-N1\"\n  summary: \"Abstract 对迁移结果选择性报告\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Abstract 已包含边界迁移失败信息\"\n  resolution_round: 23\n\n- id: \"R2-M1\"\n  summary: \"holtzman2020curious orphan bib 条目\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"已删除\"\n  resolution_round: 21\n\n- id: \"R20-M4\"\n  summary: \"'model-free' 表述已改为 'generator-independent'\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"已全文替换\"\n  resolution_round: 21\n\n- id: \"R2-W2\"\n  summary: \"混合场景（prompt-chain + retrain-chain）未讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已加 Mixed-chain 段落\"\n  resolution_round: 21\n\n- id: \"R1-N3\"\n  summary: \"Qwen 家族 5/10 配置偏重，'7/9' 统计量误导\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已修改 framing\"\n  resolution_round: 21\n\n- id: \"R2-N2\"\n  summary: \"遗漏 Wang et al. (ACL 2025) 相关工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已添加引用\"\n  resolution_round: 21\n\n- id: \"R2-N3\"\n  summary: \"'One-wash laundering' framing 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已重写\"\n  resolution_round: 21\n\n- id: \"R22-Q6\"\n  summary: \"Generator identity AUC 数值不一致\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"数值已统一\"\n  resolution_round: 23\n\n- id: \"R25-M2\"\n  summary: \"遗漏 Suresh et al. (2024) Rate of Model Collapse\"\n  category: related_work\n  severity: minor\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Agent M2 已添加引用；Round 26 未再提及\"\n  resolution_round: 26\n\n- id: \"R25-M3\"\n  summary: \"Figure 1 中 K* Estimation 步骤箭头指向不清\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Paper Agent M6 patch 已修复；Round 26 未再提及\"\n  resolution_round: 26\n\n- id: \"R25-M4\"\n  summary: \"Table 2 需视觉高亮 K* boundary 行\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Agent M5 已添加 cellcolor；Round 26 未再提及\"\n  resolution_round: 26\n\n- id: \"R25-M5\"\n  summary: \"self-BLEU 在 deployment 场景的计算方式需澄清\"\n  category: method\n  severity: minor\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Paper Agent patch 已展开说明；Round 26 未再提及\"\n  resolution_round: 26"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "gen-depth-contamination",
    "issues_yaml": "## Review Issues Tracker — gen-depth-contamination\n## Updated: Round 26 fresh review (2026-05-22)\n\n# === CRITICAL / MUST-FIX ===\n\n- id: \"R26-N1\"\n  summary: \"arXiv K*=3 缺乏 bootstrap CI 和 permutation p-value\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"Table 4 的 arXiv 2v3 AUC (0.6436/0.6545) 无 CI 无 p-value，但 C4 主实验 Table 2 对所有边界对提供了完整验证。作为独立贡献 (contribution b) 需同等统计标准。仅 2 family、n=2200。R1 列为 Must-Fix，R2 同意 severity。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-N1\"\n  summary: \"Qwen 过度代表使 6/10 统计量误导\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix。6/10 中 4 个 Qwen。按 family：仅 2/6 unanimously K*=2。R1 同意表述需改但指出 K*∈{1,2} 变化范围小，one-wash 定性结论仍成立。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1 列为 Must-Fix (N2)，R2 同意。尽管 Round 25 action 已在 Abstract 添加 per-family 统计，但叙事权重仍以 '6/10' 为主导，'(2/6 families)' 仅在括号中。建议将 per-family 统计提至首位。\"\n  action_items:\n    - round: 25\n      action: \"Abstract 同时报告 per-config 和 per-family 统计；Section 4.1 添加 family-level 汇总\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n# === WARNING / SHOULD-FIX ===\n\n- id: \"R25-W2\"\n  summary: \"K*=2 的实际新贡献 vs binary detection 讨论不足（贡献悖论）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix：如果结论是 binary is sufficient，增量贡献不明确。R1 REBUT：K* 提供解释性价值。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 升级为 Must-Fix (N1)：ordinal framework 证明 binary 足矣构成内在悖论。R1 降为 Should-Fix：ordinal framework 作为科学工具建立 negative result 是有效贡献模式。共识：需更明确地 frame ordinal estimation 为'测量工具'而非暗示直接应用价值。\"\n  action_items:\n    - round: 25\n      action: \"Discussion 更明确阐述 K*_empirical 作为度量框架相对于 binary detection 的增量贡献\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W1\"\n  summary: \"遗漏高度相关近期工作：Geng et al. 2026, Shahriar et al. 2025\"\n  category: related_work\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix (N3)，R1 降为 Should-Fix（两篇互补但不 subsume 本文）。(1) Geng et al. (2026) 'Markovian Generation Chains in LLMs' (arXiv:2603.11228)——Markov chain 理论框架高度重叠；(2) Shahriar et al. (2025) 'The Erosion of LLM Signatures' (arXiv:2512.05311)——迭代 paraphrasing 后 detection 衰减与 one-wash laundering 直接相关。均经 web search 验证真实存在。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W2\"\n  summary: \"边界 CI 决策缺乏多重比较校正\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1 列为 Should-Fix (W2)，R2 强烈同意。10 个配置同时检验未用 Bonferroni/FDR 校正。Qwen-cont CI 下界仅超 θ 0.002，校正后可能跌破→K*=2 count 从 6/10 降为 5/10。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N1\"\n  summary: \"DPI→adjacent-pair AUC 推理链存在逻辑缺口\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 20\n      reviewer: R1\n      note: \"DPI 保证 cumulative info loss 单调递减，但 K* 衡量 adjacent-pair AUC。\"\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"应明确 DPI 是 heuristic motivation 而非 strict proof。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Must-Fix：K*_empirical 作为 K*_theory 下界仅为断言，缺形式证明。R2 同意但建议降为 Should-Fix。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1 指出 K*_empirical ≤ K*_theory 从特征子集关系可直接推出（trivially true），不需要 DPI 也不需要 conjecture。DPI 仅用于 motivate 单调衰减。两个论点（lower bound vs monotonicity）被混为一谈。R2 同意。\"\n  action_items:\n    - round: 25\n      action: \"明确区分 K*_empirical 为操作性定义 vs K*_theory 下界；后者降级为 conjecture 并阐明 AUC-MI gap\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-N2\"\n  summary: \"θ=0.60 post-hoc 选择使 K*=2 核心结论脆弱\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Cohen's h 提供先验基础，但第三条 distributional discontinuity 应标为 post-hoc confirmatory。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"两位 Reviewer 最强共识点。θ∈[0.55,0.70] 内 K* 从 3 变到 1。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 指出 'small effect size' 本身主观——为何不用 medium (h=0.50)？R1 同意应将 θ=0.60 定位为'参考操作点'而非唯一正确阈值。Figure 3 提供了 θ-free 连续度量但未在正文充分讨论。\"\n  action_items:\n    - round: 25\n      action: \"报告 θ-free 指标（AUC gap 及其 CI），提供完整灵敏度曲线\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R22-C4\"\n  summary: \"模型规模覆盖偏向小模型（≤8B），威胁可推广性\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"缺 >8B；按家族去重 K*=2 从 6/10 降为 3/6。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"共识：至少在 Abstract/Conclusion 明确限定 1B-8B 适用范围。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 再次提出：实际 web-scale 合成文本来自 100B+ 模型，Discussion 推测 '13B+ may yield K*=1' 未验证。R1 同意应在 Conclusion 更显式限定。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 显式限定 K*≈2 适用范围为 1B-8B\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Filtering 实验效果量在现实污染比例下极小\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"≤50% 污染下所有策略无显著差异。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"+0.74pp MMLU 在 100% 极端条件下。Appendix D.8 ≤30% 策略差异消失。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1(W3)+R2(W5) 再次共识：dose-response (50% p=0.12) 放在 Appendix 而非正文，有 cherry-picking 嫌疑。实际指导价值在现实条件下缺乏 evidence。\"\n  action_items:\n    - round: 25\n      action: \"Section 5 引用 dose-response 分析；承认现实污染比例下边际增益可忽略\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-W3\"\n  summary: \"文档长度（256 tokens）代表性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix (W3)，R1 同意。512 tokens 时 CI lower = 0.5979 < θ=0.60。真实 web 文档通常数千 tokens。Limitations 已承认但实验覆盖不足。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R25-W1\"\n  summary: \"Prompt-chain 生态有效性——one-wash laundering 可能是 prompt-chain 特有现象\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Must-Fix（retrain-chain K*≥4 远超 prompt-chain K*=2）。R1 降为 Should-Fix。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2(W4) 提出标题 'Recursive Synthetic Text' 范围过广，暗示覆盖所有类型。R1 降为 Minor——'recursive' 不专指某一类型，正文已明确协议。\"\n  action_items:\n    - round: 25\n      action: \"Abstract/Conclusion 添加 prompt-chain 限定语\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-W11\"\n  summary: \"Filtering 仅在单一 generator（Qwen-1.5B cont）上验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"至少应在 K*=1 generator 上重复或在 Limitations 中声明。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix，R1 同意。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2(W5)+R1(W3) 再次提出。单一模型/数据集/任务，效果微弱 (+0.74pp MMLU)。\"\n  action_items:\n    - round: 25\n      action: \"Limitations 声明 filtering 仅单 generator 验证；Section 5 讨论 K*=1 场景\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-C2\"\n  summary: \"Cross-scorer 验证部分证伪 scorer independence claim（Qwen-cont K*=2→1）\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 25\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"Qwen-cont 自身打分 K*=2 仅超 θ 0.002，Pythia/OLMo 打分均 <θ。\"\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"R1 列为 Should-Fix。R2 同意并补充 ensemble 也无法解决 marginal signal。\"\n    - round: 26\n      reviewer: []\n      note: \"本轮未作为独立问题提及。R26-W2（多重比较校正）覆盖了 Qwen-cont 边界脆弱性的一部分。可能已通过 Round 25 的三层 scorer independence 重写部分缓解。待 Research Director 确认。\"\n  action_items:\n    - round: 25\n      action: \"Section 4.2 更突出讨论 cross-scorer 降级对部署的影响\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W4\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 20\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R2]\n      note: \"Reviewer 有分歧，R1 认为正常。\"\n    - round: 25\n      reviewer: [R2]\n      note: \"R2 提到 Abstract 中 Cohen's h≈0.20 缺乏上下文。\"\n    - round: 26\n      reviewer: [R2]\n      note: \"R2(M1) 仍认为 Abstract 信息密度偏高——一个段落含 task definition、K*、θ、6/10、2/6、scale-dependent split、one-wash laundering 等。建议精简。\"\n  action_items:\n    - round: 25\n      action: \"Abstract 中 Cohen's h 替换为直观表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n# === MINOR ===\n\n- id: \"R25-M1\"\n  summary: \"正文 Table 仅展示部分配置（5-7/10）\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 26\n  mentions:\n    - round: 25\n      reviewer: [R1, R2]\n      note: \"Table 2 仅列 5 配置但声称 10。\"\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1(M2)+R2(M3)：正文 Table 仍仅展示 5/10 配置，其余在 Appendix Table S2b。声称 '10 model configurations' 但正文不完整展示，读者可能质疑 defer 到 appendix 的配置是否因结果不利。\"\n  action_items:\n    - round: 25\n      action: \"Section 4.1 添加 1-2 句概述全部 10 配置结果\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M1\"\n  summary: \"标题 'Recursive Synthetic Text' 范围略宽于 prompt-chain 实际覆盖\"\n  category: framing\n  severity: minor\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R2 列为 Should-Fix (W4)，R1 降为 Minor——'recursive' 不专指某一类型，正文 Section 3.1 已明确协议。共识降为 Minor。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M2\"\n  summary: \"ANOVA 使用 GroupKFold 非独立观测值\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1 列为 Should-Fix (W4)，R2 REBUT 降为 Minor——ANOVA 用于 feature importance 分析而非核心 K* 结论，GroupKFold 选择本身合理（避免 document leakage），p-value 可能偏乐观但影响有限。共识降为 Minor。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M3\"\n  summary: \"OLMo sub-threshold AUC 非单调性未显式标注\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1(M1)：OLMo 2v3=0.497 < 3v4=0.502 违反单调预期。Paper 限定 'monotonically above θ' 技术上成立但应标注 sub-threshold 非单调性。R2 同意。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R26-M4\"\n  summary: \"Neural probe 'self-familiarity' 归因为推测而非实验验证\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 26\n  last_seen_round: 26\n  mentions:\n    - round: 26\n      reviewer: [R1, R2]\n      note: \"R1(M3)：Section 4.5 的 'self-familiarity artifacts' 解释为 post-hoc speculation，未做 cross-family probe 对照实验验证。R2 同意。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R24-M3\"\n  summary: \"K*_empirical 定义中 max 算子隐含 AUC 单调递减假设\"\n  category: method\n  severity: minor\n  status: in_progress\n  first_raised_round: 24\n  last_seen_round: 26\n  mentions:\n    - round: 24\n      reviewer: [R1, R2]\n      note: \"明确单调假设或改用连续满足条件定义。\"\n    - round: 25\n      reviewer: [R1]\n      note: \"主实验 10 配置均严格单调递减，但 threshold 以下有接近翻转的 case。\"\n    - round: 26\n      reviewer: [R1]\n      note: \"Round 25 已改为 ∀j≤k 连续满足定义，但 R1(M1) 指出 OLMo sub-threshold 非单调性应显式标注（见 R26-M3）。定义本身已改善。\"\n  action_items:\n    - round: 25\n      action: \"Eq.1 改为连续满足定义 + 声明单调性为经验观察\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"\"\n  resolution_round: null\n\n# === RESOLVED (from prior rounds) ===\n\n- id: \"R2-W3\"\n  summary: \"Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Round 24 fix expanded Conclusion; Round 25-26 did not re-raise\"\n  resolution_round: 25\n\n- id: \"R2-W1\"\n  summary: \"与 Geng et al. (2026) 和 Wang et al. (2025) 的技术区分不够清晰\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 24\n  resolution: \"Round 24 fix added citations; Round 25-26 did not re-raise\"\n  resolution_round: 25\n\n- id: \"R24-M4\"\n  summary: \"Figure 4 热图红绿配色对色盲不友好\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 24\n  last_seen_round: 24\n  resolution: \"Round 24 fix changed to blue-orange; Round 25-26 did not re-raise\"\n  resolution_round: 25\n\n- id: \"R23-M2\"\n  summary: \"Orphan bib entries / 引用格式不一致\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  resolution: \"Round 24 fix completed; Round 25-26 did not re-raise\"\n  resolution_round: 25\n\n- id: \"R24-C1\"\n  summary: \"附录空占位符表格\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  resolution: \"Round 25 确认无空表\"\n  resolution_round: 25\n\n- id: \"R2-N1\"\n  summary: \"Abstract 对迁移结果选择性报告\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 23\n  resolution: \"Abstract 已包含边界迁移失败信息\"\n  resolution_round: 23\n\n- id: \"R2-M1\"\n  summary: \"holtzman2020curious orphan bib 条目\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"已删除\"\n  resolution_round: 21\n\n- id: \"R20-M4\"\n  summary: \"'model-free' 表述已改为 'generator-independent'\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"已全文替换\"\n  resolution_round: 21\n\n- id: \"R2-W2\"\n  summary: \"混合场景（prompt-chain + retrain-chain）未讨论\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已加 Mixed-chain 段落\"\n  resolution_round: 21\n\n- id: \"R1-N3\"\n  summary: \"Qwen 家族 5/10 配置偏重，'7/9' 统计量误导\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Round 21 已修改 framing\"\n  resolution_round: 21\n\n- id: \"R2-N2\"\n  summary: \"遗漏 Wang et al. (ACL 2025) 相关工作\"\n  category: related_work\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已添加引用\"\n  resolution_round: 21\n\n- id: \"R2-N3\"\n  summary: \"'One-wash laundering' framing 不准确\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Round 21 已重写\"\n  resolution_round: 21\n\n- id: \"R22-Q6\"\n  summary: \"Generator identity AUC 数值不一致\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"数值已统一\"\n  resolution_round: 23\n\n- id: \"R25-M2\"\n  summary: \"遗漏 Suresh et al. (2024) Rate of Model Collapse\"\n  category: related_work\n  severity: minor\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Agent M2 已添加引用；Round 26 未再提及\"\n  resolution_round: 26\n\n- id: \"R25-M3\"\n  summary: \"Figure 1 中 K* Estimation 步骤箭头指向不清\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Paper Agent M6 patch 已修复；Round 26 未再提及\"\n  resolution_round: 26\n\n- id: \"R25-M4\"\n  summary: \"Table 2 需视觉高亮 K* boundary 行\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Agent M5 已添加 cellcolor；Round 26 未再提及\"\n  resolution_round: 26\n\n- id: \"R25-M5\"\n  summary: \"self-BLEU 在 deployment 场景的计算方式需澄清\"\n  category: method\n  severity: minor\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 25\n  resolution: \"Paper Agent patch 已展开说明；Round 26 未再提及\"\n  resolution_round: 26"
  }
}
```

</details>

---


### Tool result

_source line 2485 · 2026-05-22T08:11:20.380157+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/review_issues.yaml\", \"bytes\": 16446}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---
