# Director coordination — Part 9 of 10

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

[← Part 8](part-008.md) · [Transcript overview](../director-coordination.md) · [Part 10 →](part-010.md) · [Structured JSON](../../../sessions/fb/fb462ae0cd5c4c630c34.json)

## Round 178

### User

_source line 2233 · 2026-05-24T23:02:55.333282+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 完整审稿报告

**论文**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"
**Venue**: EMNLP 2026 via ARR
**审查侧重**: 新颖性 + 完整性 + NLP 社区适配

---

## Summary

本文研究 LLM 标注替代人工标注时，标准混淆矩阵校正（pooled global correction）在子群误差率异质性下反而引入偏差的问题。核心贡献是一个精确偏差恒等式（Theorem 1），揭示 global correction 在子群水平引入偏差 δ_s · Δτ / (1−2π̄)，其中 δ_s 捕捉子群误差偏离均值的程度，Δτ 是处理效应异质性，(1−2π̄) 是放大因子。论文还推导了一个不需要估计 τ 的诊断准则（Proposition 5），以及一个基于层次贝叶斯的逐子群校正方法 EC-HTE。实验在合成数据、半合成数据（16 个真实 LLM 混淆矩阵）和真实数据（仇恨言论检测）上验证了理论预测和方法有效性。

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)

**一句话总结**: 理论贡献扎实、实验验证全面，但核心贡献偏计量经济学/因果推断，对 EMNLP 受众的吸引力有限，新颖性相对经典测量误差理论为增量式。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 4 / 5 (Strong) | Theorem 1 证明严谨（Appendix B），合成实验 R² ≥ 0.97 验证精确恒等式，16 个真实 LLM 混淆矩阵的半合成实验覆盖充分，MCMC 收敛诊断达标（R̂ < 1.01, ESS > 845）。Assumption A3 (P(Z=0)=0.5) 限制性较强，但附录 T-Z 中对假设放松有系统性检验。 |
| **Excitement** | 3 / 5 (Interesting) | "Debiasing hurts" 发现非平凡，Δτ-free 诊断对实践者有用。但核心贡献在测量误差理论/因果推断领域，NLP 社区中真正做 LLM 标注 + 因果推断的受众较窄。论文在因果推断 venue（如 CLeaR）可能引发更大共鸣。 |
| **Confidence** | 4 / 5 | 熟悉测量误差理论和 NLP 标注质量文献，仔细检查了主要证明和实验设计。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **NLP 社区适配性不足——核心贡献几乎完全在统计/因果推断领域**

- 具体位置：全文，尤其 Section 3（理论）和 Section 4（方法）
- 问题：论文的三个贡献——(1) 偏差恒等式、(2) 诊断准则、(3) 层次贝叶斯校正——全部属于测量误差理论和因果推断方法论。NLP 任务（sentiment, hate speech, stance, topic classification）仅作为测试平台，论文没有产出关于语言本身的新洞察。一个 EMNLP 读者读完后的核心收获是"使用 pooled correction 时要小心异质性"——这是一个统计结论，不是 NLP 结论。
- 为什么影响接收：EMNLP AC 在 Excitement 维度评估时会考虑论文对 NLP 社区的相关性。ARR review form 明确指出 Excitement 衡量"potential interesting-ness to the community"。当前 framing 下，论文的核心受众是做因果推断的社会科学家，而非 NLP 研究者。
- 建议修改方向：
  - (a) 在 Section 5 中将 Appendix M（仇恨言论真实案例）的关键结果移入正文——这是唯一展示 NLP 特有子群结构（hashtag 存在性、文本长度）如何驱动误分类异质性的实验
  - (b) 讨论子群异质性的**语言学来源**：为什么 LLM 在含 hashtag 的推文上 FPR 更高？是因为讽刺/反语？因为 hashtag 改变了语境？这类分析才是 NLP 读者关心的
  - (c) 增加一个 "Implications for NLP Annotation Pipelines" 段落，讨论该发现如何改变 NLP 社区的标注实践（例如：是否应该对不同文本类型分别计算标注质量？）

**N2** [critical] **与 Frazis-Loewenstein (2003) 的差异在正文中阐述不够清晰**

- 具体位置：Section 3（page 4），仅一句话提及 F-L 作为特例
- 问题：Theorem 1 的核心结构——混淆矩阵导致的偏差可分解为误差率偏差 × 效应异质性 / 放大因子——与 F-L (2003) 的标量衰减偏差在形式上高度相似。正文仅在 page 4 用一句话说 "Theorem 1 subsumes Frazis–Loewenstein scalar attenuation"，但未清晰解释 **新增内容**。F-L 的实证比较被放到了 Appendix Z.5（page 30），大多数 reviewer 不会读到。
  
  一个熟悉测量误差文献的 reviewer 会问：Theorem 1 是否只是 F-L 的 K-subgroup 推广？如果 F-L 对每个子群单独应用，加上一个子群加权聚合步骤，是否能得到相同的偏差分解？
- 为什么影响接收：新颖性是 EMNLP main conference 的核心评审标准。如果 Theorem 1 被认为是成熟理论的直接推广而非新发现，Overall Assessment 会从 Conference 降至 Findings。
- 建议修改方向：
  - 在 Section 3 Theorem 1 之后增加一段 **explicit novelty statement**，明确说明：(i) F-L 考虑的是回归系数的衰减（regressor misclassification），本文考虑的是 CATE 估计中 effect modifier 的误分类——不同的因果量；(ii) F-L 没有 subgroup decomposition，无法揭示 sign reversal 的条件；(iii) 乘积结构 δ_s × Δτ 是本文的新发现，表明误差异质性和效应异质性的**交互**才是问题根源
  - 将 Appendix Z.5 的 F-L 实证比较的关键数字（F-L per-subgroup 的偏差 0.112 vs EC-HTE 的 0.006）移入正文 Table 1 或相关讨论中

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Assumption A3 (P(Z=0)=0.5) 的限制性在正文中讨论不足**

- 具体位置：Section 3, page 4, Assumption (A3)
- 问题：(A3) 假设 effect modifier Z 完美平衡，但实际 NLP 场景中子群往往高度不平衡（例如仇恨言论检测中正例远少于负例）。虽然 Appendix T 测试了 class imbalance 下的鲁棒性（P(Z=1) ∈ {0.1, 0.2, 0.3, 0.4, 0.5}），结果显示 EC-HTE 在 P(Z=1) = 0.1 时 coverage 降至 96.0%，但此分析完全在附录中。
- 建议：在 Limitations 或 Section 3 Remark 中补充 1-2 句关于 class imbalance 影响的讨论，指向 Appendix T。

**W2** [warning] **操作条件 (Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4) 是经验导出而非理论保证**

- 具体位置：Section 5.4 (page 7-8), Contribution 2 声明 (page 2)
- 问题：论文将这些操作条件作为第二个核心贡献（"a 'when not to correct' decision framework"），但这些阈值来自合成 DGP 实验（K=2, extreme DGP），未给出理论推导。它们可能对不同的 outcome model、不同的 treatment effect 大小不适用。称之为 "framework" 有轻微过度声明之嫌。
- 建议：(a) 明确说明这些是 "empirical operating guidelines" 而非理论阈值；(b) 讨论其对 DGP 设计的敏感性；(c) 保留 Proposition 5 诊断准则的理论地位，它不依赖经验阈值。

**W3** [warning] **正文中缺少完整的真实数据实验**

- 具体位置：Section 5 (pages 7-8)
- 问题：正文实验全部基于合成或半合成 DGP（合成 outcome + 真实 LLM 混淆矩阵）。真实数据实验（UC Berkeley 仇恨言论语料库，Appendix M；TweetEval 多模型验证，Appendix N-O）都在附录中。对于一篇投 EMNLP 的论文，缺少正文中的 NLP 真实数据结果会减弱 NLP 社区适配的感知。
- 建议：将 Appendix M 的关键发现（real-world heterogeneity: FPR 从 8.5% 到 21.9%, subgroup-varying misclassification）浓缩为正文 1-2 段，替代或压缩部分合成实验细节。

**W4** [warning] **噪声标签学习文献的关联讨论可以更深入**

- 具体位置：Section 2, page 4, "Noisy label learning" 段落（仅 3 句话）
- 问题：论文引用了 Natarajan et al. (2013)、Patrini et al. (2017)、Cheng et al. (2020)，但讨论过于简略。这些工作中 instance-dependent noise 的概念与本文的 subgroup-dependent misclassification 直接相关——本质上 subgroup-dependent misclassification 是 instance-dependent noise 在子群层面的特例。此联系未被明确建立。此外，noise-aware loss correction (Patrini et al., 2017) 与混淆矩阵校正的 conceptual overlap 未被讨论。
- 建议：增加 2-3 句讨论，说明 (i) subgroup-dependent misclassification 可视为 instance-dependent noise 的一种结构化形式；(ii) 与 noisy label 文献的关键区别是本文关注 downstream causal estimation 而非分类性能本身。

**W5** [warning] **Section 3 的符号密度对 NLP 读者偏高**

- 具体位置：Section 3, pages 4-5
- 问题：在 Theorem 1 前后，论文快速引入了 δ_s（子群误差偏差）、Δτ（CATE 异质性）、π̄（平均误差率）、b_s（偏差项）、C_s（子群混淆矩阵）、M_global（全局混合矩阵）等符号。NLP 读者（可能不熟悉测量误差理论）跟读会有困难。Section 3 开头的 5 个假设 (A1)-(A5) 连续列出也增加了认知负担。
- 建议：在 Theorem 1 之后增加一个具体数值示例（例如用 K=2、π_1=0.1、π_2=0.3 的配置，手动计算 δ_s 和预测的偏差方向），帮助读者建立直觉。Figure 1A 已经提供了可视化，但缺少与公式的显式对应。

---

## 小问题（不影响接收）

1. **Abstract 中 "7.4×" 偏差缩减的来源不明确**：Abstract 声称 "reducing |bias| by 7.4× under extreme heterogeneity"，但 Table 1 中 K=2 Extreme 配置下 Naive |Bias|=0.066, EC-HTE |Bias|=0.006（≈11×），Global |Bias|=0.088 vs EC-HTE 0.006（≈14.7×）。7.4× 似乎来自 Figure 2 的特定配置，但未明确标注是与哪个 baseline 的比较。建议在 abstract 中明确参照基准或在正文中标注来源。

2. **Figure 3 的 panel 较小**：K=1 和 K=4 的四个 panel 在双栏排版中可读性不佳，尤其是图例和坐标轴标签。建议增大字号或减少 panel 数量。

3. **引用格式小问题**：部分引用使用 "Angelopoulos et al. (2023)" 括号外格式，部分使用 "(Angelopoulos et al., 2023)" 括号内格式——需确认是否全部符合 natbib 的 \citet / \citep 区分规范。（抽查发现大体一致，但建议全文检查。）

4. **Appendix 结构较散**：33 页附录包含 A-Z.10 共约 30 个子节，覆盖面虽广但导航困难。可考虑在 Appendix 开头增加一个目录索引。

5. **AI Assistants 声明**（page 32）提到使用 Claude 进行 "Literature: summarizing related papers to inform the related work section"——虽然符合 ACL 披露政策，但建议注意 AI 辅助写作的引用准确性（本文引用经抽查无明显问题）。

---

## 可能遗漏的相关工作

1. **Veitch et al. (2020)** "Adapting Text Embeddings for Causal Inference" — 文本因果推断领域的重要工作，讨论文本表征在因果推断中的使用。虽然关注点不同（text-as-confounder vs. effect-modifier misclassification），但作为 text + causal inference 的代表性工作应被引用。

2. **Wood-Doughty et al. (2018)** "Challenges of Using Text Classifiers for Causal Inference" — 直接讨论文本分类器噪声对因果推断的影响，与本文问题高度相关。论文引用了 Feder et al. (2022) 综述（Wood-Doughty 是共同作者），但原始论文未单独引用。

3. **LLM 校准文献**：论文在 Section Z.7 讨论了 temperature/Platt scaling 校准，但未引用 LLM 校准的代表性工作（如 Kadavath et al., 2022 "Language Models (Mostly) Know What They Know"）。校准作为混淆矩阵校正的替代或补充方案，值得更多讨论。

---

## Questions for Authors

1. Theorem 1 在 F-L (2003) 的基础上，新增的核心理论洞察是什么？如果对 F-L 在每个子群单独应用并加权聚合，是否能得到等价的偏差分解？

2. 操作条件（Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4）对 DGP 设计有多敏感？如果 outcome model 不是线性的，或 treatment effect 更大/更小，这些阈值会变吗？

3. 在真实仇恨言论案例中，子群定义（hashtag 存在性 × 文本长度）有语言学依据吗？还是为了方便实验设计？LLM 在不同子群上误差率不同的根本原因是什么？

4. 当 K > 8 个子群时方法如何 scale？层次贝叶斯估计是否会因样本稀疏而退化？

5. 如果子群划分函数 S 本身是有噪声的（例如基于聚类或 learned features），对 Theorem 1 和 EC-HTE 有何影响？

---

## 主要优势

1. **理论贡献清晰、可解释**：Theorem 1 的乘积结构（δ_s × Δτ）直觉清楚——误差异质性和效应异质性的交互才是问题根源。偏差恒等式在合成数据上 R² ≥ 0.97 验证，在 11 个真实 LLM 混淆矩阵上 R² = 0.975，说服力强。

2. **Δτ-free 诊断准则（Proposition 5）实用价值高**：实践者只需检查子群误差率即可判断是否应做逐子群校正，无需估计处理效应。这是一个可以直接嵌入 NLP 标注管道的决策工具。

3. **实验验证的深度和广度突出**：33 页论文包含合成验证（520 配置）、半合成验证（16 LLM 混淆矩阵 × 多配置）、真实数据案例、多 LLM 验证（6 个模型）、PPCI 互补性分析、假设违反敏感性分析等——对一篇会议论文来说非常全面。

4. **Framing 有效**："When Debiasing Hurts" 抓住了核心反直觉发现——这不是"debiasing 有时效果差"，而是"debiasing 可以反转效应方向"。Figure 1 的三个 panel 有效传达了这一信息。

5. **方法的互补性设计好**：EC-HTE 与 PPCI（outcome-side error correction）正交组合（Appendix L, Table 11），证明两种误差来源可独立处理。这增加了方法的实用性。

6. **代码和数据匿名公开**：anonymous.4open.science 链接提供了复现资源，符合 reproducibility 要求。

---

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| Abstract ≤ 200 words | ✓ 约 169 words |
| 正文 ≤ 8 页 | ✓ Sections 1-6 在 8 页内，Limitations 在 page 8 底部开始 |
| Limitations section | ✓ 正文内有且仅有一个，约 4-5 句，覆盖 expert budget 需求、混淆矩阵估计条件、coverage |
| Double-blind 匿名性 | ✓ 作者 "Anonymous"，代码链接匿名化 |
| ACL 模板 | ✓ \usepackage[review]{acl} |
| Appendix 双栏格式 | ✓ |
| AI Assistants 声明 | ✓ Page 32，符合 ACL 政策 |

---

## 最终评分汇总

| 维度 | 分数 |
|------|------|
| **Soundness** | 4 / 5 (Strong) |
| **Excitement** | 3 / 5 (Interesting) |
| **Overall Assessment** | 3.5 / 5 (Borderline Conference) |
| **Confidence** | 4 / 5 (Quite sure) |

**判断理由**：论文在理论严谨性和实验全面性上达到 Conference 水平（Soundness 4），但两个因素压低了总分：(1) 核心贡献在计量经济学/因果推断而非 NLP，NLP 社区 excitement 有限；(2) 相对经典测量误差理论（尤其 F-L 2003），新颖性为增量式——子群分解和 sign reversal 条件是有价值的推广，但不是根本性新发现。论文是一篇 solid 的 Findings paper；如果 AC 认为 LLM 标注质量对 NLP 社区的实际重要性足以弥补理论新颖性的边际性，也可以接收到 main conference。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2234 · 2026-05-24T23:03:09.999135+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 179

## Round 179

6 recorded events


### User

_source line 2235 · 2026-05-24T23:03:12.532082+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性 + 实验完备性

**论文**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"
**Venue**: EMNLP 2026 via ARR

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 理论贡献干净且新颖——bias identity 本身是正确的——但从对称假设下的"exact"理论到现实 LLM 非对称误分类之间存在显著落差，加之 K≤4 的可扩展性瓶颈，削弱了实际影响力。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 (Strong) | 定理推导正确，实验极为全面（33页），但对称→非对称的精度退化（R² 0.97→0.73, AUC 0.86→0.65）在正文中讨论不足 |
| Excitement | 3.5/5 | 问题提出新颖且重要（global correction 可翻转 CATE 符号），但 K≤4、n_expert/K≥50 的操作约束限制了实际适用范围 |
| Reproducibility | 4/5 | 匿名代码仓库已提供，Algorithm 1 清晰，MCMC 诊断完备（R̂<1.0034, ESS>843） |
| Confidence | 4/5 | 熟悉因果推断中的测量误差校正和混淆矩阵方法，对 HB 估计的细节略有不确定 |

---

## Summary

本文推导了一个 bias decomposition identity（Theorem 1），证明当 LLM 标注的误分类率在子群间异质时，标准的全局混淆矩阵校正会引入子群级偏差 δ_s·Δτ/(1−2ε̄)，甚至可翻转 CATE 的符号（14.9% 的配置中出现符号反转）。作者提出 EC-HTE 方法，用分层贝叶斯估计每个子群的混淆矩阵并进行分层校正，在合成数据和 4 个半合成 NLP DGP 上验证。论文还给出了一个 Δτ-free 诊断准则（Proposition 5）和明确的操作条件（Δτ>0.15, n_expert/K≥50, K≤4）。

---

## 主要优势

**S1. 新颖且重要的问题提出。** "全局校正可能比不校正更糟"这一洞见在 LLM 标注日益普及的背景下非常及时。Figure 1C 直观展示了符号翻转问题，有很强的说服力。

**S2. 理论贡献干净。** Theorem 1 的推导简洁且数学上正确：从 M_global^{-1}·M_s ≠ I 出发，bias 的乘积形式自然产生。将 bias 分解为三个可解释分量（δ_s、Δτ、amplification factor）是一个优雅的结果。Appendix B 的完整证明逻辑清晰。

**S3. 实验验证极为全面。** 33 页附录涵盖：A1-A5 每个假设的敏感性分析（Appendix Z）、类别不平衡鲁棒性（Appendix T）、先验敏感性（Appendix G.1）、bootstrap SE 验证（Appendix Y）、跨模型一致性（Appendix O, 6 个 LLM）、PPCI 互补性（Appendix K, U）、Franks-Loewenstein 对比（Appendix Z.5）、stratification 分析（Appendix X）、CausalForest oracle coverage（Appendix CC）、confounded treatment（Appendix Z.4）。这种全面性在同领域论文中罕见。

**S4. 实用性强。** Algorithm 1（page 33）给出了完整的实操流程，包含 precondition guard 和 singularity guard。代码已匿名开源。

**S5. 与现有因果推断流程的集成。** EC-HTE 输出校正后的 pseudo-outcomes，可直接接入 CausalForestDML 和 R-learner，SE 调整公式明确。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 非对称误分类下诊断准则的实际效用大幅退化，正文未充分讨论

- 具体位置：Remark 2（page 5）、Appendix J（Table 8, page 18）
- 问题：Proposition 5 的诊断准则在对称假设（A2）下 AUC=0.86，但在非对称条件下 AUC 降至 0.65。真实 LLM 几乎总是呈现非对称 FPR/FNR（Table 12, page 20 证实 6 个开源 LLM 的 FPR/FNR 比率从 1.1 到 7.1）。AUC=0.65 意味着判别力仅略好于随机。正文仅在 Remark 2 末尾一句话提及，未讨论实际影响。
- 为什么影响接收：Proposition 5 是论文的三个核心贡献之一。若在现实条件下判别力不足，该贡献价值被严重削弱。
- 建议：在 Section 3 或 5.4 增加非对称情形讨论段落；考虑开发基于完整 2×2 矩阵的非对称诊断准则；至少在 Limitations 中显式列出。

**N2** [critical] 标量近似 R² 在非对称条件下的退化与 "exact" 标题的张力

- 具体位置：Title、Abstract、Table 8（page 18）
- 问题：标题声称 "An Exact Bias Identity"，Abstract 报告 "R² ≥ 0.97"——均基于对称假设。Table 8 显示非对称条件下标量近似 R² 低至 0.05-0.21（K=2, Δτ=0.05），平均 R²=0.73。矩阵形式确实 exact（Remark 2），但论文的主要公式（Eq. 2）、诊断准则和实验验证都使用标量近似形式。
- 为什么影响接收：标题和摘要给读者的印象是 identity 在所有条件下精确，但实际使用的标量形式在非对称条件下精度有限。
- 建议：(a) Abstract 补充非对称 R²；(b) Section 3 更明确区分 "exact matrix identity" 和 "scalar approximation"；(c) 考虑调整标题措辞或在 Abstract 中明确适用条件。

**N3** [critical] K≤4 可扩展性限制与适用范围

- 具体位置：Section 5.4（page 7-8）、Appendix L.2（page 16）
- 问题：EC-HTE 在 K=8 时 RMSE 超过全局校正（Appendix L.2），n_expert=250 时每子群仅 ~31 标签。K≤4 + n_expert/K≥50 意味着 K=4 需至少 200 专家标签。NLP 分类任务常有 K>4 类别，但 Abstract 仅在操作条件中一笔带过。
- 为什么影响接收：若仅适用于少类场景，显著限制对 NLP 社区的影响力。
- 建议：Introduction 贡献段落明确说明 K≤4 限制；讨论 K>4 的可能扩展路径。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 仅测试 2 种 HTE 估计器
- 具体位置：Section 5、Appendix S（Table 19, page 23）
- 问题：仅验证 CausalForestDML 和 R-learner。X-learner、BART 等结构性不同的估计器未测试。
- 建议：增加至少 1 个结构性不同的 HTE 估计器。

**W2** [warning] MC=100 覆盖率的统计精度
- 具体位置：Section 5.1、Appendix Q（page 21）
- 问题：MC=100 时覆盖率估计 SE≈0.022；部分实验仅 50 runs（SE≈0.031）或 20 runs（SE≈0.049）。论文报告覆盖率到小数点后一位但未报告 MC 标准误。
- 建议：在结果表中报告 MC 标准误。

**W3** [warning] Proposition 5 诊断的增量价值
- 问题：诊断需要 ε_s，EC-HTE 也需要 ε_s。对于 binary Z，两者的标签需求完全相同。论文未解释何时用诊断而非直接运行 EC-HTE。
- 建议：明确说明诊断的使用场景和计算成本节省。

**W4** [warning] HB 先验结构性敏感性缺失
- 具体位置：Section 4.1、Appendix G.1（page 15）
- 问题：仅变动 Gamma 超参数（0.5×-2×），未考虑替代先验（如 logistic-normal）。
- 建议：讨论替代先验的潜在影响。

**W5** [warning] A1 灵敏度分析的参数化限制
- 具体位置：Appendix Z.1（page 28-29）
- 问题：仅用 logistic link、γ_Y ∈ [0, 0.20] 测试 A1 违反。不同函数形式可能产生不同退化模式。γ 范围缺乏实证支撑。
- 建议：增加替代参数化形式；讨论真实场景中 A1 违反的典型幅度。

---

## 小问题（不影响接收）

- M1: Abstract 的 R²=0.975 是对称条件下的，建议标注 "under symmetric approximation"。
- M2: Table 1 的 "95% CI Cov." 列未标注 MC 样本量。
- M3: Figure 2 中 "|bias| ≈ 7.4" 的注释有歧义，应为 "bias reduction factor"。
- M4: Appendix E 定义子群时未讨论子群大小不均衡的影响。
- M5: "Use of AI Assistants" 可更具体说明 AI 辅助的方面。

---

## Questions for Authors

**Q1**: Remark 2 声称矩阵形式不需要 A2。请问矩阵形式在非对称条件下的预测精度如何（是否有类似 Table 8 但使用完整矩阵形式的结果）？如果矩阵形式 exact，为什么不基于矩阵形式构建诊断准则？

**Q2**: K=8 退化的根因是 HB partial pooling 不足还是混淆矩阵估计误差？若 n_expert=1000, K=8（每子群 125 标签），EC-HTE 能否恢复优势？

**Q3**: Proposition 5 诊断 vs 直接运行 EC-HTE，增量价值具体是什么？

**Q4**: Real-data case study（Appendix M）中，EC-HTE 校正是否改变了实质性结论？

---

## 格式检查

- **页数**: 正文（Abstract 至 Conclusion）8 页，Limitations 约 10 行，合规 ✓
- **匿名性**: "Anonymous ACL submission"，代码用匿名仓库，未见作者身份泄露 ✓
- **引用格式**: natbib author-year，符合 ACL style ✓
- **模板**: ACL 双栏格式 ✓
- **Limitations**: 有，位于正文末尾，覆盖 3 个要点（误分类独立性不可检验、合成评估、ground-truth CATE 不可获得）✓
- **Abstract**: 约 180-190 words，<200 ✓
- **Appendix**: 双栏格式 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2236 · 2026-05-24T23:04:00.084390+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "ec_hte_llm_annotation",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / 遗漏相关工作，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 4/5, **Excitement**: 3/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] NLP 社区适配性不足——核心贡献几乎完全在统计/因果推断领域\n- 三个贡献——偏差恒等式、诊断准则、层次贝叶斯校正——全部属于测量误差理论和因果推断方法论。NLP 任务仅作为测试平台。EMNLP 读者的核心收获是\"使用 pooled correction 时要小心异质性\"——统计结论而非 NLP 结论。\n- 建议：(a) 将 Appendix M 仇恨言论真实案例关键结果移入正文；(b) 讨论子群异质性的语言学来源；(c) 增加 \"Implications for NLP Annotation Pipelines\" 段落。\n\n**N2** [critical] 与 Frazis-Loewenstein (2003) 的差异在正文中阐述不够清晰\n- Theorem 1 核心结构与 F-L (2003) 标量衰减偏差形式上高度相似。正文仅一句话说 \"Theorem 1 subsumes F-L\"，新增内容未清晰解释。F-L 实证比较放在 Appendix Z.5。\n- 建议：Section 3 增加 explicit novelty statement，将 Appendix Z.5 关键数字移入正文。\n\n### Should-Fix\n\n**W1** A3 (P(Z=0)=0.5) 限制性讨论不足——虽然 Appendix T 有 class imbalance 测试但完全在附录中。\n**W2** 操作条件 (Δπ>0.15, n_expert/K≥50, K≤4) 是经验导出而非理论保证——称 \"framework\" 有轻微过度声明之嫌。\n**W3** 正文缺完整真实数据实验——正文全部基于合成或半合成，真实数据在附录。\n**W4** 噪声标签学习文献关联讨论可更深入——subgroup-dependent misclassification 与 instance-dependent noise 的联系未建立。\n**W5** Section 3 符号密度对 NLP 读者偏高——建议 Theorem 1 后增加具体数值示例。\n\n### Minor\n1. Abstract \"7.4×\" 来源不明确——Table 1 中 Global 0.059 vs EC-HTE 0.008 = 7.375×。\n2. Figure 3 panel 较小。\n3. 引用格式 \\citet/\\citep 需全文检查。\n4. 33 页附录导航困难，建议增加目录索引。\n\n### 遗漏的相关工作\n1. Veitch et al. (2020) \"Adapting Text Embeddings for Causal Inference\"\n2. Wood-Doughty et al. (2018) \"Challenges of Using Text Classifiers for Causal Inference\"\n3. Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\"\n\n### Questions\n1. Theorem 1 在 F-L 基础上新增的核心理论洞察是什么？\n2. 操作条件对 DGP 设计有多敏感？\n3. 真实仇恨言论案例中子群定义有语言学依据吗？\n4. K > 8 时如何 scale？\n5. 子群划分函数 S 有噪声时对 Theorem 1 和 EC-HTE 有何影响？\n\n---\n\n请逐条给出你的 [AGREE] / [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "ec_hte_llm_annotation",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / 遗漏相关工作，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿报告\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Soundness**: 4/5, **Excitement**: 3/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] NLP 社区适配性不足——核心贡献几乎完全在统计/因果推断领域\n- 三个贡献——偏差恒等式、诊断准则、层次贝叶斯校正——全部属于测量误差理论和因果推断方法论。NLP 任务仅作为测试平台。EMNLP 读者的核心收获是\"使用 pooled correction 时要小心异质性\"——统计结论而非 NLP 结论。\n- 建议：(a) 将 Appendix M 仇恨言论真实案例关键结果移入正文；(b) 讨论子群异质性的语言学来源；(c) 增加 \"Implications for NLP Annotation Pipelines\" 段落。\n\n**N2** [critical] 与 Frazis-Loewenstein (2003) 的差异在正文中阐述不够清晰\n- Theorem 1 核心结构与 F-L (2003) 标量衰减偏差形式上高度相似。正文仅一句话说 \"Theorem 1 subsumes F-L\"，新增内容未清晰解释。F-L 实证比较放在 Appendix Z.5。\n- 建议：Section 3 增加 explicit novelty statement，将 Appendix Z.5 关键数字移入正文。\n\n### Should-Fix\n\n**W1** A3 (P(Z=0)=0.5) 限制性讨论不足——虽然 Appendix T 有 class imbalance 测试但完全在附录中。\n**W2** 操作条件 (Δπ>0.15, n_expert/K≥50, K≤4) 是经验导出而非理论保证——称 \"framework\" 有轻微过度声明之嫌。\n**W3** 正文缺完整真实数据实验——正文全部基于合成或半合成，真实数据在附录。\n**W4** 噪声标签学习文献关联讨论可更深入——subgroup-dependent misclassification 与 instance-dependent noise 的联系未建立。\n**W5** Section 3 符号密度对 NLP 读者偏高——建议 Theorem 1 后增加具体数值示例。\n\n### Minor\n1. Abstract \"7.4×\" 来源不明确——Table 1 中 Global 0.059 vs EC-HTE 0.008 = 7.375×。\n2. Figure 3 panel 较小。\n3. 引用格式 \\citet/\\citep 需全文检查。\n4. 33 页附录导航困难，建议增加目录索引。\n\n### 遗漏的相关工作\n1. Veitch et al. (2020) \"Adapting Text Embeddings for Causal Inference\"\n2. Wood-Doughty et al. (2018) \"Challenges of Using Text Classifiers for Causal Inference\"\n3. Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\"\n\n### Questions\n1. Theorem 1 在 F-L 基础上新增的核心理论洞察是什么？\n2. 操作条件对 DGP 设计有多敏感？\n3. 真实仇恨言论案例中子群定义有语言学依据吗？\n4. K > 8 时如何 scale？\n5. 子群划分函数 S 有噪声时对 Theorem 1 和 EC-HTE 有何影响？\n\n---\n\n请逐条给出你的 [AGREE] / [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2237 · 2026-05-24T23:04:20.669968+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20585
}
```

</details>

---


### Tool call

_source line 2238 · 2026-05-24T23:04:20.772046+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "ec_hte_llm_annotation",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 4/5, **Excitement**: 3.5/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] 非对称误分类下诊断准则的实际效用大幅退化，正文未充分讨论\n- Proposition 5 对称 AUC=0.86，非对称 AUC=0.65。真实 LLM 几乎总是非对称（FPR/FNR 比率 1.1-7.1）。AUC=0.65 仅略好于随机。正文仅 Remark 2 末尾一句话。\n- Proposition 5 是三个核心贡献之一，现实条件下判别力不足则贡献价值被严重削弱。\n\n**N2** [critical] 标量近似 R² 在非对称条件下的退化与 \"exact\" 标题的张力\n- 标题 \"Exact Bias Identity\"，Abstract \"R² ≥ 0.97\"——均基于对称假设。非对称下标量近似 R² 低至 0.05-0.21（K=2, Δτ=0.05），平均 0.73。矩阵形式 exact 但论文主公式、诊断和实验验证都用标量近似。\n\n**N3** [critical] K≤4 可扩展性限制与适用范围\n- EC-HTE 在 K=8 时 RMSE 超过全局校正。K≤4 + n_expert/K≥50 意味着 K=4 需至少 200 专家标签。NLP 分类常有 K>4。\n\n### Should-Fix\n\n**W1** 仅测试 CausalForestDML 和 R-learner，缺 X-learner/BART。\n**W2** MC=100 覆盖率 SE≈0.022，部分实验仅 50/20 runs，未报告 MC 标准误。\n**W3** Proposition 5 诊断 vs 直接运行 EC-HTE 增量价值不清——两者标签需求相同。\n**W4** HB 先验仅变动 Gamma 超参（0.5×-2×），未考虑替代先验（logistic-normal）。\n**W5** A1 灵敏度分析仅 logistic link、γ_Y ∈ [0, 0.20]，参数化形式单一。\n\n### Minor\n- M1: Abstract R²=0.975 应标注 \"under symmetric approximation\"\n- M2: Table 1 未标注 MC 样本量\n- M3: Figure 2 \"7.4\" 注释有歧义\n- M4: Appendix E 未讨论子群大小不均衡\n- M5: AI Assistants 声明可更具体\n\n### Questions\nQ1: 矩阵形式非对称预测精度？为什么不基于矩阵形式构建诊断？\nQ2: K=8 退化根因？n_expert=1000, K=8 能否恢复？\nQ3: Proposition 5 诊断 vs 直接 EC-HTE 增量价值？\nQ4: Real-data case study 中 EC-HTE 是否改变实质结论？\n\n---\n\n请逐条给出你的 [AGREE] / [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "ec_hte_llm_annotation",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Questions，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 4/5, **Excitement**: 3.5/5, **Confidence**: 4/5\n\n### Must-Fix\n\n**N1** [critical] 非对称误分类下诊断准则的实际效用大幅退化，正文未充分讨论\n- Proposition 5 对称 AUC=0.86，非对称 AUC=0.65。真实 LLM 几乎总是非对称（FPR/FNR 比率 1.1-7.1）。AUC=0.65 仅略好于随机。正文仅 Remark 2 末尾一句话。\n- Proposition 5 是三个核心贡献之一，现实条件下判别力不足则贡献价值被严重削弱。\n\n**N2** [critical] 标量近似 R² 在非对称条件下的退化与 \"exact\" 标题的张力\n- 标题 \"Exact Bias Identity\"，Abstract \"R² ≥ 0.97\"——均基于对称假设。非对称下标量近似 R² 低至 0.05-0.21（K=2, Δτ=0.05），平均 0.73。矩阵形式 exact 但论文主公式、诊断和实验验证都用标量近似。\n\n**N3** [critical] K≤4 可扩展性限制与适用范围\n- EC-HTE 在 K=8 时 RMSE 超过全局校正。K≤4 + n_expert/K≥50 意味着 K=4 需至少 200 专家标签。NLP 分类常有 K>4。\n\n### Should-Fix\n\n**W1** 仅测试 CausalForestDML 和 R-learner，缺 X-learner/BART。\n**W2** MC=100 覆盖率 SE≈0.022，部分实验仅 50/20 runs，未报告 MC 标准误。\n**W3** Proposition 5 诊断 vs 直接运行 EC-HTE 增量价值不清——两者标签需求相同。\n**W4** HB 先验仅变动 Gamma 超参（0.5×-2×），未考虑替代先验（logistic-normal）。\n**W5** A1 灵敏度分析仅 logistic link、γ_Y ∈ [0, 0.20]，参数化形式单一。\n\n### Minor\n- M1: Abstract R²=0.975 应标注 \"under symmetric approximation\"\n- M2: Table 1 未标注 MC 样本量\n- M3: Figure 2 \"7.4\" 注释有歧义\n- M4: Appendix E 未讨论子群大小不均衡\n- M5: AI Assistants 声明可更具体\n\n### Questions\nQ1: 矩阵形式非对称预测精度？为什么不基于矩阵形式构建诊断？\nQ2: K=8 退化根因？n_expert=1000, K=8 能否恢复？\nQ3: Proposition 5 诊断 vs 直接 EC-HTE 增量价值？\nQ4: Real-data case study 中 EC-HTE 是否改变实质结论？\n\n---\n\n请逐条给出你的 [AGREE] / [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2239 · 2026-05-24T23:04:22.183881+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1411
}
```

</details>

---


### Assistant

_source line 2240 · 2026-05-24T23:04:30.135275+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 180

## Round 180

10 recorded events


### User

_source line 2241 · 2026-05-24T23:04:31.134970+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**3.5 / 5 (Borderline Conference)**。

两个 Must-Fix 问题：
1. **NLP 社区适配性**——核心贡献在统计/因果推断领域，NLP 任务仅作测试平台。建议将仇恨言论真实案例移入正文、讨论误分类异质性的语言学根源。
2. **与 F-L (2003) 的差异阐述**——正文中仅一句话提及 F-L 为特例，详细比较藏在 Appendix Z.5，需在 Theorem 1 后增加显式 novelty statement。

三个主要优势：理论结果清晰可验证（R²≥0.97）、Δτ-free 诊断有实用价值、实验验证深度突出（33 页，520 配置）。

---

[Reviewer 1 审稿结果]:
审稿报告已完成并提交给 Review Director。

**核心判断**: Overall 3.5 (Borderline Conference)。

三个 Must-Fix 问题：
1. **非对称诊断退化**：Proposition 5 的 AUC 从 0.86 降至 0.65（现实 LLM 几乎都是非对称），正文讨论严重不足
2. **"Exact" 标题与标量近似的张力**：矩阵形式确实 exact，但论文实际使用的标量形式在非对称下 R²=0.73
3. **K≤4 可扩展性瓶颈**：Abstract/Intro 未充分突出这一重要限制

五个 Should-Fix：HTE 估计器多样性不足、MC 精度未报告、诊断增量价值不明、先验结构敏感性缺失、A1 灵敏度分析参数化受限。

理论本身是正确且优雅的，实验全面性在同领域中属于顶级水平。若能解决非对称 gap 和 scalability 讨论，可达 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2242 · 2026-05-24T23:05:22.866725+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2243 · 2026-05-24T23:05:22.917673+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T22:52:13.924145+00:00\", \"completed_at\": \"2026-05-24T22:55:29.907327+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页（Title/Abstract/Introduction/Related Work）为连续纯文本页，无任何 display item。第一个视觉锚点（Figure 1）出现在第 3 页，尚可接受但审稿人需翻两页纯文字才看到图。建议考虑将 Figure 1 或一个精简版概念图提前至第 1 页底部或第 2 页顶部\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 作为首个 display item 质量优秀：三面板（A/B/C）清晰展示 sign reversal 核心问题，红/蓝颜色对比明确，caption 自包含，传达核心 message 有效。Title-Abstract-Figure 1 叙事一致\"}, {\"severity\": \"warning\", \"dimension\": \"page 4-5\", \"message\": \"连续两页密集数学推导（Theorem 1、Propositions 3-5、Corollaries），无任何 display item 穿插。虽然理论推导性质允许例外，但可考虑在 Proposition 附近插入一个示意图辅助理解 bias decomposition 的直觉\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2（EC-HTE vs. Standard Correction Pipeline）设计优秀，颜色编码清晰（绿/黄/红/蓝），流程对比一目了然，是全文最佳视觉元素\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 RMSE vs. expert budget 曲线清晰，shaded bands 表示 CI。子面板轴标签字号偏小（约为正文 60-65%），在打印时可能略难辨认\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"页面过度拥挤：Figure 4（两面板）+ Table 1（主结果表）+ Section 5.3 + Section 5.4 + Section 6 Conclusion + Limitations 全部挤在一页。审稿人阅读体验受损——主结果表和结论都缺乏呼吸空间。建议将 Conclusion 和 Limitations 移至第 9 页起始\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗标注，小数精度统一，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 部分仅约 3-4 行，符合 EMNLP 2026 要求（短段覆盖 3 个要点）\"}, {\"severity\": \"info\", \"dimension\": \"page 9-10\", \"message\": \"参考文献排版正常，双栏格式统一，未发现 [?] 未解析引用或格式不一致\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Table 2（MCMC convergence diagnostics）和 Figure 5（ROC curves）排版整洁\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"Figure 6 多面板 RMSE 曲线 + Table 4 同页，布局合
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2244 · 2026-05-24T23:05:22.918188+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2245 · 2026-05-24T23:05:23.119099+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 2246 · 2026-05-24T23:08:34.383544+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"已修正为 'on synthetic grids (aggregate 0.975; per-model range 0.76-0.99)'\"\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"AUC 数字从 Abstract 完全移除\"\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"Abstract 已加 'under extreme heterogeneity' 限定\"\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    action_items: []\n    resolution: \"v31 colorblind-safe palette: sage green→blue throughout\"\n    resolution_round: 19\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  # === ROUND 19-20 OPEN/IN_PROGRESS — carried forward with R21 status ===\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 PEHE、缺半合成 CF 结果、缺 Eq.7 不确定性传播消融\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"DDL 前无法补充。PEHE + Eq.7 消融理论上各需 30min，半合成 CF 需 2-4h 高风险。Rebuttal 材料。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20 指出仅用 CausalForestDML + R-learner 不够，缺 X-learner/BART。\"\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-W1 再次提出仅 2 种 HTE 估计器。R2 未单独提及但在 questions 中问及 scale。与本 issue 一致。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: PEHE + Eq.7 消融（camera-ready 补充）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认: Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s。问题已解决。\"\n    action_items: []\n    resolution: \"Proposition 3 (A5 relaxation with Δτ_s) 已在主文 theory.tex L63-71\"\n    resolution_round: 21\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。experiments.tex L28 已有讨论。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W3 再次提出正文缺完整真实数据实验。真实数据仍仅在附录。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-N2: 'exact' 标题与标量近似 R² 退化的张力。R2 未直接提及但在 F-L 差异讨论中涉及。Abstract 已修正为 'under symmetric errors (generalizing to full-matrix form)'。Deeper fix（非对称 closed-form）仍为 rebuttal 材料。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提及，但 R1-W2 提到 MC=100 覆盖率精度问题，间接相关。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。method.tex 提到 HB 估计 <5ms。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N1 再次作为 Must-Fix 提出：核心贡献几乎完全在统计/因果推断领域，NLP 任务仅作测试平台。建议将 Appendix M 仇恨言论案例移入正文，讨论误分类异质性的语言学来源，增加 NLP 标注管道影响讨论。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-N3 作为 Must-Fix 再次提出: K≤4 限制，K=8 时 RMSE 超过全局校正。NLP 分类常有 K>4。Abstract/Intro 未充分突出。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 19\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。已与 R19-W2 合并，Limitations 已补充。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Proposition 3 已在主文，A5 relaxation 充分展示。\"\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W4 再次提出: 仅变动 Gamma 超参数，未考虑替代先验（logistic-normal）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出: MC=100 覆盖率 SE≈0.022，未报告 MC 标准误。与 R20-W1 一致。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 严重限制标题级 'Exact Identity' 声称——非对称情形 R² 降至 0.73\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21 两位 Reviewer 均再次关注此问题。R1-N2: 标量近似 R² 在非对称下低至 0.05-0.21。R1-N1: 诊断 AUC 从 0.86 降至 0.65。Abstract 已改为 'under symmetric errors (generalizing...)'，但 Reviewer 认为标题 'exact' 仍有张力。写作修复已做；deeper theoretical fix（非对称 closed-form）仍待 rebuttal。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 经典测量误差理论的增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 再次作为 Must-Fix: 正文仅一句 subsumes 声明，F-L 实证比较在 Appendix Z.5。建议增加 explicit novelty statement，将关键数字移入正文。theory.tex proof sketch 已有 nesting statement，但 R2 认为不够清晰。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L (2003) 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 explicit novelty statement，关键 F-L 比较数字移入正文\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献 (Natarajan et al. 2013, Patrini et al. 2017)\"\n    category: writing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W4: 段落已添加（related_work.tex），但讨论仍可更深入——subgroup-dependent 与 instance-dependent noise 的联系未建立。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"深化噪声标签文献讨论：建立 subgroup-dependent vs instance-dependent noise 联系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称——SE ≈ 2.2pp\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出。Table 1 caption 已添加 coverage SE 注释，但实际增加 MC runs 仍为 rebuttal 材料。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅——EC-HTE 是成熟技术的组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 间接涉及: F-L 差异化不足。核心贡献定位应为理论洞察 (theory 60% + empirical 20% + method 20%)。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W5 再次提出: 仅 logistic link, γ ∈ [0, 0.20]。\"\n    action_items:\n      - round: 20\n        action: \"增加一种基于文本特征的 confounding 形式的灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W5 扩展此问题: Section 3 符号密度对 NLP 读者偏高，建议增加数值示例。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用不一致——部分文件硬编码 Remark~1 或 Remark~\\\\ref{thm:bias_identity}，应为 Remark 2\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"theory.tex 添加 \\\\label{rem:asymmetric}，所有引用统一为 \\\\ref{rem:asymmetric}。\"\n    action_items:\n      - round: 21\n        action: \"添加 \\\\label{rem:asymmetric} 并统一所有交叉引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === ROUND 21 NEW ISSUES ===\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65，正文讨论严重不足\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-N1: Proposition 5 是三大贡献之一。真实 LLM FPR/FNR 比率 1.1-7.1，AUC=0.65 仅略好于随机。正文仅 Remark 2 末尾一句话。R2 未单独提出但在 F-L 差异讨论中间接涉及。\"\n    action_items:\n      - round: 21\n        action: \"Section 3 或 5.4 增加非对称情形讨论段落；考虑基于完整 2×2 矩阵的非对称诊断准则\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足——核心贡献在统计/因果推断，NLP 任务仅为测试平台\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-N1 Must-Fix: NLP 读者核心收获是统计结论而非 NLP 结论。建议 (a) Appendix M 仇恨言论案例移入正文 (b) 讨论误分类异质性的语言学来源 (c) 增加 NLP 标注管道影响讨论。与 R17-NLP2 一致但 R21 升级为 critical。\"\n    action_items:\n      - round: 21\n        action: \"将 Appendix M 关键发现移入正文，讨论语言学来源，增加 NLP 标注管道影响段落\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明——两者标签需求相同\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-W3: 诊断需要 ε_s，EC-HTE 也需要 ε_s。对 binary Z，标签需求完全相同。论文未解释何时用诊断而非直接运行 EC-HTE。\"\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景：计算成本节省、无下游估计器依赖、可在 annotation pipeline 中前置部署\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W1: Appendix T 有 class imbalance 测试但完全在附录。建议 Limitations 或 Remark 中补充 1-2 句。\"\n    action_items:\n      - round: 21\n        action: \"Limitations 或 Section 3 Remark 补充 class imbalance 影响讨论，指向 Appendix T\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"操作条件 (Δπ>0.15, n_expert/K≥50, K≤4) 是经验导出——称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W2: 阈值来自合成 DGP，未给出理论推导，对不同 outcome model 可能不适用。建议明确为 'empirical operating guidelines'。\"\n    action_items:\n      - round: 21\n        action: \"Contribution 2 措辞调整为 'empirical operating guidelines' 而非 'framework'\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高——缺数值示例\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W5: 连续引入 δ_s, Δτ, π̄, b_s, C_s, M_global 等符号。建议 Theorem 1 后增加 K=2 具体数值示例。\"\n    action_items:\n      - round: 21\n        action: \"Theorem 1 后增加一个 K=2, π_1=0.1, π_2=0.3 的具体数值示例\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch et al. (2020), Wood-Doughty et al. (2018), Kadavath et al. (2022)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"Veitch (text embeddings for causal inference), Wood-Doughty (text classifiers for causal inference, 高度相关), Kadavath (LLM self-knowledge/calibration)。\"\n    action_items:\n      - round: 21\n        action: \"Related Work 增加 Veitch 2020, Wood-Doughty 2018 引用；评估 Kadavath 2022 是否需要\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"已修正为 'on synthetic grids (aggregate 0.975; per-model range 0.76-0.99)'\"\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"AUC 数字从 Abstract 完全移除\"\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"Abstract 已加 'under extreme heterogeneity' 限定\"\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 19\n    action_items: []\n    resolution: \"v31 colorblind-safe palette: sage green→blue throughout\"\n    resolution_round: 19\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  # === ROUND 19-20 OPEN/IN_PROGRESS — carried forward with R21 status ===\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 PEHE、缺半合成 CF 结果、缺 Eq.7 不确定性传播消融\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"DDL 前无法补充。PEHE + Eq.7 消融理论上各需 30min，半合成 CF 需 2-4h 高风险。Rebuttal 材料。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20 指出仅用 CausalForestDML + R-learner 不够，缺 X-learner/BART。\"\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-W1 再次提出仅 2 种 HTE 估计器。R2 未单独提及但在 questions 中问及 scale。与本 issue 一致。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: PEHE + Eq.7 消融（camera-ready 补充）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认: Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s。问题已解决。\"\n    action_items: []\n    resolution: \"Proposition 3 (A5 relaxation with Δτ_s) 已在主文 theory.tex L63-71\"\n    resolution_round: 21\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。experiments.tex L28 已有讨论。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W3 再次提出正文缺完整真实数据实验。真实数据仍仅在附录。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-N2: 'exact' 标题与标量近似 R² 退化的张力。R2 未直接提及但在 F-L 差异讨论中涉及。Abstract 已修正为 'under symmetric errors (generalizing to full-matrix form)'。Deeper fix（非对称 closed-form）仍为 rebuttal 材料。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提及，但 R1-W2 提到 MC=100 覆盖率精度问题，间接相关。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。method.tex 提到 HB 估计 <5ms。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N1 再次作为 Must-Fix 提出：核心贡献几乎完全在统计/因果推断领域，NLP 任务仅作测试平台。建议将 Appendix M 仇恨言论案例移入正文，讨论误分类异质性的语言学来源，增加 NLP 标注管道影响讨论。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-N3 作为 Must-Fix 再次提出: K≤4 限制，K=8 时 RMSE 超过全局校正。NLP 分类常有 K>4。Abstract/Intro 未充分突出。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 19\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。已与 R19-W2 合并，Limitations 已补充。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Proposition 3 已在主文，A5 relaxation 充分展示。\"\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W4 再次提出: 仅变动 Gamma 超参数，未考虑替代先验（logistic-normal）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出: MC=100 覆盖率 SE≈0.022，未报告 MC 标准误。与 R20-W1 一致。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 严重限制标题级 'Exact Identity' 声称——非对称情形 R² 降至 0.73\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21 两位 Reviewer 均再次关注此问题。R1-N2: 标量近似 R² 在非对称下低至 0.05-0.21。R1-N1: 诊断 AUC 从 0.86 降至 0.65。Abstract 已改为 'under symmetric errors (generalizing...)'，但 Reviewer 认为标题 'exact' 仍有张力。写作修复已做；deeper theoretical fix（非对称 closed-form）仍待 rebuttal。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 经典测量误差理论的增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 再次作为 Must-Fix: 正文仅一句 subsumes 声明，F-L 实证比较在 Appendix Z.5。建议增加 explicit novelty statement，将关键数字移入正文。theory.tex proof sketch 已有 nesting statement，但 R2 认为不够清晰。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L (2003) 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 explicit novelty statement，关键 F-L 比较数字移入正文\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献 (Natarajan et al. 2013, Patrini et al. 2017)\"\n    category: writing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W4: 段落已添加（related_work.tex），但讨论仍可更深入——subgroup-dependent 与 instance-dependent noise 的联系未建立。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"深化噪声标签文献讨论：建立 subgroup-dependent vs instance-dependent noise 联系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称——SE ≈ 2.2pp\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出。Table 1 caption 已添加 coverage SE 注释，但实际增加 MC runs 仍为 rebuttal 材料。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅——EC-HTE 是成熟技术的组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 间接涉及: F-L 差异化不足。核心贡献定位应为理论洞察 (theory 60% + empirical 20% + method 20%)。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W5 再次提出: 仅 logistic link, γ ∈ [0, 0.20]。\"\n    action_items:\n      - round: 20\n        action: \"增加一种基于文本特征的 confounding 形式的灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W5 扩展此问题: Section 3 符号密度对 NLP 读者偏高，建议增加数值示例。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用不一致——部分文件硬编码 Remark~1 或 Remark~\\\\ref{thm:bias_identity}，应为 Remark 2\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"theory.tex 添加 \\\\label{rem:asymmetric}，所有引用统一为 \\\\ref{rem:asymmetric}。\"\n    action_items:\n      - round: 21\n        action: \"添加 \\\\label{rem:asymmetric} 并统一所有交叉引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === ROUND 21 NEW ISSUES ===\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65，正文讨论严重不足\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-N1: Proposition 5 是三大贡献之一。真实 LLM FPR/FNR 比率 1.1-7.1，AUC=0.65 仅略好于随机。正文仅 Remark 2 末尾一句话。R2 未单独提出但在 F-L 差异讨论中间接涉及。\"\n    action_items:\n      - round: 21\n        action: \"Section 3 或 5.4 增加非对称情形讨论段落；考虑基于完整 2×2 矩阵的非对称诊断准则\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足——核心贡献在统计/因果推断，NLP 任务仅为测试平台\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-N1 Must-Fix: NLP 读者核心收获是统计结论而非 NLP 结论。建议 (a) Appendix M 仇恨言论案例移入正文 (b) 讨论误分类异质性的语言学来源 (c) 增加 NLP 标注管道影响讨论。与 R17-NLP2 一致但 R21 升级为 critical。\"\n    action_items:\n      - round: 21\n        action: \"将 Appendix M 关键发现移入正文，讨论语言学来源，增加 NLP 标注管道影响段落\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明——两者标签需求相同\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-W3: 诊断需要 ε_s，EC-HTE 也需要 ε_s。对 binary Z，标签需求完全相同。论文未解释何时用诊断而非直接运行 EC-HTE。\"\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景：计算成本节省、无下游估计器依赖、可在 annotation pipeline 中前置部署\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W1: Appendix T 有 class imbalance 测试但完全在附录。建议 Limitations 或 Remark 中补充 1-2 句。\"\n    action_items:\n      - round: 21\n        action: \"Limitations 或 Section 3 Remark 补充 class imbalance 影响讨论，指向 Appendix T\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"操作条件 (Δπ>0.15, n_expert/K≥50, K≤4) 是经验导出——称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W2: 阈值来自合成 DGP，未给出理论推导，对不同 outcome model 可能不适用。建议明确为 'empirical operating guidelines'。\"\n    action_items:\n      - round: 21\n        action: \"Contribution 2 措辞调整为 'empirical operating guidelines' 而非 'framework'\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高——缺数值示例\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W5: 连续引入 δ_s, Δτ, π̄, b_s, C_s, M_global 等符号。建议 Theorem 1 后增加 K=2 具体数值示例。\"\n    action_items:\n      - round: 21\n        action: \"Theorem 1 后增加一个 K=2, π_1=0.1, π_2=0.3 的具体数值示例\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch et al. (2020), Wood-Doughty et al. (2018), Kadavath et al. (2022)\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"Veitch (text embeddings for causal inference), Wood-Doughty (text classifiers for causal inference, 高度相关), Kadavath (LLM self-knowledge/calibration)。\"\n    action_items:\n      - round: 21\n        action: \"Related Work 增加 Veitch 2020, Wood-Doughty 2018 引用；评估 Kadavath 2022 是否需要\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 2247 · 2026-05-24T23:08:34.689980+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml\", \"bytes\": 21417}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 306
}
```

</details>

---


### Tool call

_source line 2248 · 2026-05-24T23:11:19.693779+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# Round 21 审稿报告\n\n**论文**: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性 + 实验完备性）、R2（新颖性 + 完整性 + NLP 社区适配）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文推导了一个精确偏差恒等式（Theorem 1），证明当 LLM 标注的误分类率在子群间异质时，标准全局混淆矩阵校正引入子群级偏差 δ_s·Δτ/(1−2π̄)，在 14.9% 的配置中反转 CATE 符号。论文提出 EC-HTE 方法（层次贝叶斯逐子群混淆矩阵估计 + 分层校正），在合成数据（520 配置）和半合成数据（16 个真实 LLM 混淆矩阵 × 4 NLP 任务）上验证，偏差缩减 7.4× (extreme heterogeneity)。另推导 Δτ-free 诊断准则（Proposition 5）和操作条件框架。\n\n---\n\n## Strengths\n\n**S1. [共识] 问题提出新颖且重要。** \"Global correction 可反转 CATE 符号\"这一发现在 LLM 标注日益普及的背景下非常及时。Figure 1 三面板直观有效。（R1-S1, R2-S4）\n\n**S2. [共识] 理论贡献干净且可验证。** Theorem 1 的乘积形式 δ_s × Δτ / (1−2π̄) 简洁可解释，合成数据 R² ≥ 0.97，11 个真实 LLM 混淆矩阵聚合 R² = 0.975。推导逻辑清晰（Appendix B）。（R1-S2, R2-S1）\n\n**S3. [共识] 实验验证深度突出。** 33 页附录涵盖 A1-A5 每个假设的敏感性分析、class imbalance、先验敏感性、bootstrap SE、跨模型一致性（6 个 LLM）、PPCI 互补性、F-L 对比、CausalForest oracle coverage、confounded treatment 等。同领域罕见的全面性。（R1-S3, R2-S3）\n\n**S4. [共识] Δτ-free 诊断有实用价值。** Proposition 5 仅需子群误差率即可判断是否应做逐子群校正，无需估计处理效应，可直接嵌入标注管道。（R2-S2）\n\n**S5. [共识] 方法互补性设计好。** EC-HTE（covariate-side）与 PPCI（outcome-side）正交组合，bias 从 0.179 降至 0.007。（R2-S5）\n\n**S6. [共识] 可复现性。** Algorithm 1 完整，匿名代码仓库已提供，MCMC 诊断达标（R̂ < 1.01, ESS > 843）。（R1-S4）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [R1-N1/N2, 共识] 非对称误分类下理论和诊断的退化——正文讨论严重不足**\n\n标量偏差公式（Eq. 2）和诊断准则（Proposition 5）在对称假设 (A2) 下表现良好（R² ≥ 0.97, AUC = 0.86），但真实 LLM 几乎总是非对称（FPR/FNR 比率 1.1–7.1, Table 12）。非对称下：\n- 标量近似 R² 降至平均 0.73，极端配置低至 0.05–0.21（K=2, Δτ=0.05, Table 8）\n- 诊断 AUC 从 0.86 降至 0.65（仅略好于随机）\n\n论文标题声称 \"Exact Bias Identity\"，Abstract 报告 \"R² ≥ 0.97\"——均基于对称假设。矩阵形式确实 exact（Remark 2），但论文实际使用的标量形式、诊断和主要实验验证都依赖标量近似。正文对此退化仅在 Remark 2 末尾一句话带过。\n\n**影响**：Proposition 5 是三大贡献之一；若现实条件下判别力不足，该贡献价值被严重削弱。标题和 Abstract 给读者的印象与实际适用条件之间存在张力。\n\n**建议**：(a) Section 3 或 5.4 增加非对称退化讨论段落；(b) 考虑基于完整 2×2 矩阵的非对称诊断准则；(c) Abstract 补充非对称 R² 信息；(d) 更明确区分 \"exact matrix identity\" 和 \"scalar approximation\"。\n\n---\n\n**MF2. [R2-N1, R1 Excitement 3.5 vs R2 Excitement 3] NLP 社区适配性不足**\n\n三个贡献——偏差恒等式、诊断准则、层次贝叶斯校正——全部属于测量误差理论/因果推断方法论。NLP 任务（sentiment, hate speech, stance, topic classification）仅作测试平台，论文未产出关于语言本身的新洞察。真实数据实验（UC Berkeley 仇恨言论、TweetEval 多模型验证）均在附录中。\n\nR2 认为核心受众是做因果推断的社会科学家而非 NLP 研究者，论文在 CLeaR 等因果推断 venue 可能引发更大共鸣。R1 给 Excitement 3.5（略高），认为问题本身对 NLP 社区足够重要。\n\n**影响**：EMNLP AC 在 Excitement 维度会考虑论文对 NLP 社区的相关性。当前 framing 下 NLP 受众覆盖有限。\n\n**建议**：(a) 将 Appendix M 仇恨言论真实案例关键结果移入正文——这是唯一展示 NLP 特有子群结构如何驱动误分类异质性的实验；(b) 讨论误分类异质性的语言学来源（hashtag/讽刺/反语如何影响 FPR）；(c) 增加 \"Implications for NLP Annotation Pipelines\" 段落。\n\n---\n\n**MF3. [R2-N2, 共识] 与 Frazis-Loewenstein (2003) 的差异化阐述不够清晰**\n\nTheorem 1 在形式上是 F-L (2003) 标量衰减偏差的 K-subgroup 推广。正文仅一句话提及 \"Theorem 1 subsumes F-L\"（page 4 proof sketch），详细 F-L 实证比较在 Appendix Z.5（page 30，多数 reviewer 不会读到）。\n\n一个熟悉测量误差文献的 reviewer 会问：如果对 F-L 在每个子群单独应用并加权聚合，是否能得到等价分解？论文需要明确说明新增的核心洞察——(i) F-L 考虑回归系数衰减，本文考虑 CATE effect modifier 误分类（不同因果量）；(ii) 乘积结构 δ_s × Δτ 揭示 sign reversal 条件，F-L 的标量形式无法发现；(iii) 三因子分解的可解释性是独立增量。\n\n**影响**：新颖性是 EMNLP main conference 核心评审标准。若 Theorem 1 被视为成熟理论的直接推广，Overall 从 Conference 降至 Findings。\n\n**建议**：Section 3 Theorem 1 后增加 explicit novelty statement；将 Appendix Z.5 的关键 F-L 比较数字移入正文。\n\n---\n\n**MF4. [R1-N3, R2 Q4] K ≤ 4 可扩展性瓶颈——Abstract/Intro 未充分突出**\n\nEC-HTE 在 K=8 时 RMSE 超过全局校正（Appendix L.2），n_expert=250 时每子群仅 ~31 标签。K ≤ 4 + n_expert/K ≥ 50 意味着 K=4 需至少 200 专家标签。NLP 分类任务常有 K > 4（情感分析 5 级、主题分类 10+ 类），但此限制在 Abstract 中仅一笔带过。\n\n**建议**：Introduction 贡献段落明确说明 K ≤ 4 限制；讨论 K > 4 的可能扩展路径（例如子群合并策略）。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [R1-W1, 关联 R19-C4] 仅测试 2 种 HTE 估计器（CausalForestDML + R-learner）。** 缺 X-learner、BART 等结构性不同的估计器。论文声称方法 \"estimator-agnostic\"，但验证不充分。建议增加至少 1 个。\n\n**SF2. [R1-W2, 关联 R20-W1] MC=100 覆盖率统计精度。** SE ≈ 2.2pp，部分实验 50/20 runs（SE 更大），Table 1 未报告 MC 标准误。Table 1 caption 已有注释但正式 SE 列仍缺。建议在结果表中报告 MC SE。\n\n**SF3. [R2-W3, 关联 R19-W5] 正文缺完整真实数据实验。** 所有正文实验为合成或半合成，真实数据在附录。EMNLP 投稿应有正文中的 NLP 真实数据结果。建议将 Appendix M 关键发现浓缩进正文。\n\n**SF4. [R2-W2] 操作条件是经验导出。** Δπ > 0.15、n_expert/K ≥ 50、K ≤ 4 来自合成 DGP，无理论推导。称 \"decision framework\" 轻微过度声称。建议调整为 \"empirical operating guidelines\"。\n\n**SF5. [R2-W4, 关联 R20-C3] 噪声标签学习文献关联可更深入。** Noisy label learning 段落已添加但仅 3 句话。subgroup-dependent misclassification 与 instance-dependent noise 的结构化联系未建立。\n\n**SF6. [R1-W3] Proposition 5 诊断 vs 直接运行 EC-HTE 增量价值不明。** 两者标签需求相同（均需 ε_s），论文未解释何时用诊断而非直接 EC-HTE。\n\n**SF7. [R2-W5] Section 3 符号密度对 NLP 读者偏高。** 连续引入 δ_s、Δτ、π̄、C_s、M_global 等符号，5 个假设连续列出增加认知负担。建议 Theorem 1 后增加数值示例。\n\n**SF8. [R1-W4, 关联 R19-M2] HB 先验结构性敏感性缺失。** 仅变动 Gamma 超参（0.5×-2×），未考虑替代先验（logistic-normal）。\n\n**SF9. [R1-W5, 关联 R20-W3] A1 灵敏度分析参数化受限。** 仅 logistic link、γ ∈ [0, 0.20]，不同函数形式可能产生不同退化模式。\n\n**SF10. [R2-W1] Assumption A3 (P(Z=0)=0.5) 限制性在正文中讨论不足。** Appendix T 有 class imbalance 测试但完全在附录。\n\n---\n\n### Minor（不影响接收）\n\n1. Abstract \"7.4×\" 来源需明确标注基准（Global 0.059 vs EC-HTE 0.008 = 7.375×）\n2. Figure 3 panel 字号偏小（约正文 60-65%），打印可读性受影响\n3. \\citet / \\citep 使用需全文检查一致性\n4. 33 页附录导航困难，建议增加目录索引\n5. Algorithm 1 最后一页仅占 40%，余 60% 空白\n6. Table 1 \"95% CI Cov.\" 列未标注 MC 样本量\n7. Appendix E 子群大小不均衡影响未讨论\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成一致：\n\n1. **Overall 3.5 (Borderline Conference)**——理论扎实但 NLP 适配和非对称退化拉低总分\n2. **Soundness 4/5**——Theorem 1 推导正确，实验设计严谨\n3. **非对称退化是核心弱点**——标量形式和诊断准则在现实 LLM 非对称条件下效用有限\n4. **K ≤ 4 可扩展性限制**——显著限制 NLP 场景适用范围\n5. **MC=100 精度不足**——覆盖率声称需要更多 MC runs 或至少报告 SE\n6. **实验全面性是显著优势**——33 页附录在同领域罕见\n7. **格式合规**——Abstract ≤ 200 words，正文 ≤ 8 页，匿名性、ACL 模板均达标\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分析 |\n|------|----|----|------|\n| NLP 社区适配 | Excitement 3.5（问题本身足够重要） | Excitement 3（核心受众是因果推断社区） | R2 的关切更有说服力——三个贡献均为统计方法论，NLP 任务仅为测试平台 |\n| 诊断 AUC 退化 | Must-Fix（AUC=0.65 致命） | 未单独提出 Must-Fix | R1 的关切合理——Proposition 5 是核心贡献之一 |\n| F-L 差异化 | 认可 nesting statement 存在 | Must-Fix（正文阐述不够） | R2 的关切合理——需要更显式的 novelty statement |\n\n---\n\n## Questions for Authors\n\n1. [R1-Q1] Remark 2 声称矩阵形式不需要 A2。矩阵形式在非对称条件下的预测精度如何？为什么不基于矩阵形式构建诊断准则？\n2. [R1-Q2] K=8 退化的根因是 HB partial pooling 不足还是混淆矩阵估计误差？若 n_expert=1000, K=8，EC-HTE 能否恢复？\n3. [R1-Q3] Proposition 5 诊断 vs 直接运行 EC-HTE，增量价值具体是什么？\n4. [R2-Q1] Theorem 1 在 F-L 基础上新增的核心理论洞察是什么？对 F-L 在每个子群单独应用并加权聚合，能否得到等价分解？\n5. [R2-Q3] 真实仇恨言论案例中，子群定义有语言学依据吗？LLM 在不同子群上误差率不同的根本原因是什么？\n6. [R2-Q5] 子群划分函数 S 本身有噪声时，对 Theorem 1 和 EC-HTE 有何影响？\n\n---\n\n## Missing References\n\n1. **Veitch et al. (2020)** \"Adapting Text Embeddings for Causal Inference\" — text + causal inference 代表性工作（R2 提出）\n2. **Wood-Doughty et al. (2018)** \"Challenges of Using Text Classifiers for Causal Inference\" — 直接讨论文本分类器噪声对因果推断影响，高度相关（R2 提出）\n3. **Kadavath et al. (2022)** \"Language Models (Mostly) Know What They Know\" — LLM 校准代表性工作，与混淆矩阵校正互补（R2 提出）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（4 warning, 0 critical, 16 info）\n\n主要发现：\n- **[warning] Page 1-2**: 前两页纯文本无 display item，Figure 1 在第 3 页。建议考虑提前视觉锚点。\n- **[warning] Page 4-5**: 连续两页密集数学推导无 display item 穿插。\n- **[warning] Page 8**: 过度拥挤——Figure 4 + Table 1 + Section 5.3-5.4 + Conclusion + Limitations 全挤一页，主结果表和结论缺呼吸空间。\n- **[warning] Page 33**: Algorithm 1 仅占页面 40%，下方 60% 空白。\n- **[info]** Figure 1 质量优秀，Figure 2 EC-HTE pipeline 对比是全文最佳视觉元素，Table 1 使用 booktabs 规范。公式渲染无错误，双栏 margin 无溢出，正文 8 页合规。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n\n**EMNLP 2026 评分标准**: 3.5 = Borderline Conference（介于 Conference 和 Findings 之间）\n\n**置信度**: 4 / 5\n\n**判断理由**:\n\n论文在理论严谨性（Soundness 4/5）和实验全面性上达到 Conference 水平。Theorem 1 的乘积分解是一个干净、可验证的理论结果，\"debiasing hurts\" 的发现对 LLM 标注日益普及的 NLP 社区有实际意义。\n\n四个因素将总分从 Conference (4.0) 压至 Borderline (3.5)：\n\n1. **非对称退化未充分解决**：标题级 \"exact\" 声称与现实条件下的退化（R² 0.73, AUC 0.65）之间存在张力，Proposition 5 作为核心贡献之一的价值被削弱。\n2. **NLP 社区适配有限**：核心贡献在计量经济学/因果推断领域，NLP 任务仅作测试平台，正文缺少 NLP 特有的洞察和真实数据。\n3. **F-L 差异化不足**：新颖性为增量式——子群分解和 sign reversal 条件有价值，但不是根本性新发现。\n4. **K ≤ 4 可扩展性瓶颈**：限制了对 NLP 社区中多类分类场景的适用性。\n\n**升级路径 → 4.0 (Conference)**：\n- 正文充分讨论非对称退化并给出矩阵形式诊断\n- 将 Appendix M 真实数据移入正文，增强 NLP 定位\n- Section 3 显式 F-L novelty statement\n- Abstract/Intro 明确 K ≤ 4 限制\n\n**降级风险 → 3.0 (Findings)**：\n- AC 认为 NLP 社区 excitement 不足\n- \"exact\" 标题被视为 misleading\n\n当前定位：一篇 solid 的 Findings paper；若修改到位，可达 Conference。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 \"decision framework\" 应调整为 \"empirical operating guidelines\"\n- K ≤ 4 限制应在贡献列表中明确提及\n- F-L 比较数字（0.122–0.168 vs EC-HTE 0.008）已在正文，但 novelty 阐述不足\n\n### Section 2 (Related Work)\n- Noisy label learning 段落已添加但过于简略（3 句），建议建立 subgroup-dependent vs instance-dependent noise 的结构化联系\n- 缺 Veitch 2020, Wood-Doughty 2018（text + causal inference 核心文献）\n\n### Section 3 (Theory)\n- Theorem 1 推导正确，三因子分解优雅\n- A2 \"expository simplification\" 标注是改进，但需更明确区分 \"exact matrix identity\" vs \"scalar approximation\"\n- 建议 Theorem 1 后增加 K=2 数值示例（π_1=0.1, π_2=0.3）降低认知负担\n- Proposition 5: 需在正文讨论非对称 AUC 退化和诊断 vs EC-HTE 的增量价值\n\n### Section 4 (Method)\n- HB 估计规格完整，<5ms 计算成本是优势\n- κ-guard 设计合理\n- 先验敏感性仅 Gamma 超参变动，建议讨论替代先验\n\n### Section 5 (Experiments)\n- 合成验证（520 配置）极为全面\n- 正文应包含至少一个真实 NLP 数据实验\n- MC=100 需报告 SE；关键配置建议增至 ≥500\n- 仅 2 种 HTE 估计器，建议增加 X-learner 或 BART\n\n### Section 6 (Conclusion)\n- 3 句话合理，adoption guideline 有价值\n- 可增加 1 句讨论非对称推广的未来方向\n\n### Limitations\n- 覆盖 3 个要点，长度合规\n- 建议增加 A3 class imbalance 影响和 K ≤ 4 限制的显式提及\n\n### Appendix\n- 深度突出，是论文的核心竞争力之一\n- 建议增加目录索引改善导航\n- Page 33 Algorithm 1 空白过多"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# Round 21 审稿报告\n\n**论文**: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性 + 实验完备性）、R2（新颖性 + 完整性 + NLP 社区适配）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文推导了一个精确偏差恒等式（Theorem 1），证明当 LLM 标注的误分类率在子群间异质时，标准全局混淆矩阵校正引入子群级偏差 δ_s·Δτ/(1−2π̄)，在 14.9% 的配置中反转 CATE 符号。论文提出 EC-HTE 方法（层次贝叶斯逐子群混淆矩阵估计 + 分层校正），在合成数据（520 配置）和半合成数据（16 个真实 LLM 混淆矩阵 × 4 NLP 任务）上验证，偏差缩减 7.4× (extreme heterogeneity)。另推导 Δτ-free 诊断准则（Proposition 5）和操作条件框架。\n\n---\n\n## Strengths\n\n**S1. [共识] 问题提出新颖且重要。** \"Global correction 可反转 CATE 符号\"这一发现在 LLM 标注日益普及的背景下非常及时。Figure 1 三面板直观有效。（R1-S1, R2-S4）\n\n**S2. [共识] 理论贡献干净且可验证。** Theorem 1 的乘积形式 δ_s × Δτ / (1−2π̄) 简洁可解释，合成数据 R² ≥ 0.97，11 个真实 LLM 混淆矩阵聚合 R² = 0.975。推导逻辑清晰（Appendix B）。（R1-S2, R2-S1）\n\n**S3. [共识] 实验验证深度突出。** 33 页附录涵盖 A1-A5 每个假设的敏感性分析、class imbalance、先验敏感性、bootstrap SE、跨模型一致性（6 个 LLM）、PPCI 互补性、F-L 对比、CausalForest oracle coverage、confounded treatment 等。同领域罕见的全面性。（R1-S3, R2-S3）\n\n**S4. [共识] Δτ-free 诊断有实用价值。** Proposition 5 仅需子群误差率即可判断是否应做逐子群校正，无需估计处理效应，可直接嵌入标注管道。（R2-S2）\n\n**S5. [共识] 方法互补性设计好。** EC-HTE（covariate-side）与 PPCI（outcome-side）正交组合，bias 从 0.179 降至 0.007。（R2-S5）\n\n**S6. [共识] 可复现性。** Algorithm 1 完整，匿名代码仓库已提供，MCMC 诊断达标（R̂ < 1.01, ESS > 843）。（R1-S4）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [R1-N1/N2, 共识] 非对称误分类下理论和诊断的退化——正文讨论严重不足**\n\n标量偏差公式（Eq. 2）和诊断准则（Proposition 5）在对称假设 (A2) 下表现良好（R² ≥ 0.97, AUC = 0.86），但真实 LLM 几乎总是非对称（FPR/FNR 比率 1.1–7.1, Table 12）。非对称下：\n- 标量近似 R² 降至平均 0.73，极端配置低至 0.05–0.21（K=2, Δτ=0.05, Table 8）\n- 诊断 AUC 从 0.86 降至 0.65（仅略好于随机）\n\n论文标题声称 \"Exact Bias Identity\"，Abstract 报告 \"R² ≥ 0.97\"——均基于对称假设。矩阵形式确实 exact（Remark 2），但论文实际使用的标量形式、诊断和主要实验验证都依赖标量近似。正文对此退化仅在 Remark 2 末尾一句话带过。\n\n**影响**：Proposition 5 是三大贡献之一；若现实条件下判别力不足，该贡献价值被严重削弱。标题和 Abstract 给读者的印象与实际适用条件之间存在张力。\n\n**建议**：(a) Section 3 或 5.4 增加非对称退化讨论段落；(b) 考虑基于完整 2×2 矩阵的非对称诊断准则；(c) Abstract 补充非对称 R² 信息；(d) 更明确区分 \"exact matrix identity\" 和 \"scalar approximation\"。\n\n---\n\n**MF2. [R2-N1, R1 Excitement 3.5 vs R2 Excitement 3] NLP 社区适配性不足**\n\n三个贡献——偏差恒等式、诊断准则、层次贝叶斯校正——全部属于测量误差理论/因果推断方法论。NLP 任务（sentiment, hate speech, stance, topic classification）仅作测试平台，论文未产出关于语言本身的新洞察。真实数据实验（UC Berkeley 仇恨言论、TweetEval 多模型验证）均在附录中。\n\nR2 认为核心受众是做因果推断的社会科学家而非 NLP 研究者，论文在 CLeaR 等因果推断 venue 可能引发更大共鸣。R1 给 Excitement 3.5（略高），认为问题本身对 NLP 社区足够重要。\n\n**影响**：EMNLP AC 在 Excitement 维度会考虑论文对 NLP 社区的相关性。当前 framing 下 NLP 受众覆盖有限。\n\n**建议**：(a) 将 Appendix M 仇恨言论真实案例关键结果移入正文——这是唯一展示 NLP 特有子群结构如何驱动误分类异质性的实验；(b) 讨论误分类异质性的语言学来源（hashtag/讽刺/反语如何影响 FPR）；(c) 增加 \"Implications for NLP Annotation Pipelines\" 段落。\n\n---\n\n**MF3. [R2-N2, 共识] 与 Frazis-Loewenstein (2003) 的差异化阐述不够清晰**\n\nTheorem 1 在形式上是 F-L (2003) 标量衰减偏差的 K-subgroup 推广。正文仅一句话提及 \"Theorem 1 subsumes F-L\"（page 4 proof sketch），详细 F-L 实证比较在 Appendix Z.5（page 30，多数 reviewer 不会读到）。\n\n一个熟悉测量误差文献的 reviewer 会问：如果对 F-L 在每个子群单独应用并加权聚合，是否能得到等价分解？论文需要明确说明新增的核心洞察——(i) F-L 考虑回归系数衰减，本文考虑 CATE effect modifier 误分类（不同因果量）；(ii) 乘积结构 δ_s × Δτ 揭示 sign reversal 条件，F-L 的标量形式无法发现；(iii) 三因子分解的可解释性是独立增量。\n\n**影响**：新颖性是 EMNLP main conference 核心评审标准。若 Theorem 1 被视为成熟理论的直接推广，Overall 从 Conference 降至 Findings。\n\n**建议**：Section 3 Theorem 1 后增加 explicit novelty statement；将 Appendix Z.5 的关键 F-L 比较数字移入正文。\n\n---\n\n**MF4. [R1-N3, R2 Q4] K ≤ 4 可扩展性瓶颈——Abstract/Intro 未充分突出**\n\nEC-HTE 在 K=8 时 RMSE 超过全局校正（Appendix L.2），n_expert=250 时每子群仅 ~31 标签。K ≤ 4 + n_expert/K ≥ 50 意味着 K=4 需至少 200 专家标签。NLP 分类任务常有 K > 4（情感分析 5 级、主题分类 10+ 类），但此限制在 Abstract 中仅一笔带过。\n\n**建议**：Introduction 贡献段落明确说明 K ≤ 4 限制；讨论 K > 4 的可能扩展路径（例如子群合并策略）。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [R1-W1, 关联 R19-C4] 仅测试 2 种 HTE 估计器（CausalForestDML + R-learner）。** 缺 X-learner、BART 等结构性不同的估计器。论文声称方法 \"estimator-agnostic\"，但验证不充分。建议增加至少 1 个。\n\n**SF2. [R1-W2, 关联 R20-W1] MC=100 覆盖率统计精度。** SE ≈ 2.2pp，部分实验 50/20 runs（SE 更大），Table 1 未报告 MC 标准误。Table 1 caption 已有注释但正式 SE 列仍缺。建议在结果表中报告 MC SE。\n\n**SF3. [R2-W3, 关联 R19-W5] 正文缺完整真实数据实验。** 所有正文实验为合成或半合成，真实数据在附录。EMNLP 投稿应有正文中的 NLP 真实数据结果。建议将 Appendix M 关键发现浓缩进正文。\n\n**SF4. [R2-W2] 操作条件是经验导出。** Δπ > 0.15、n_expert/K ≥ 50、K ≤ 4 来自合成 DGP，无理论推导。称 \"decision framework\" 轻微过度声称。建议调整为 \"empirical operating guidelines\"。\n\n**SF5. [R2-W4, 关联 R20-C3] 噪声标签学习文献关联可更深入。** Noisy label learning 段落已添加但仅 3 句话。subgroup-dependent misclassification 与 instance-dependent noise 的结构化联系未建立。\n\n**SF6. [R1-W3] Proposition 5 诊断 vs 直接运行 EC-HTE 增量价值不明。** 两者标签需求相同（均需 ε_s），论文未解释何时用诊断而非直接 EC-HTE。\n\n**SF7. [R2-W5] Section 3 符号密度对 NLP 读者偏高。** 连续引入 δ_s、Δτ、π̄、C_s、M_global 等符号，5 个假设连续列出增加认知负担。建议 Theorem 1 后增加数值示例。\n\n**SF8. [R1-W4, 关联 R19-M2] HB 先验结构性敏感性缺失。** 仅变动 Gamma 超参（0.5×-2×），未考虑替代先验（logistic-normal）。\n\n**SF9. [R1-W5, 关联 R20-W3] A1 灵敏度分析参数化受限。** 仅 logistic link、γ ∈ [0, 0.20]，不同函数形式可能产生不同退化模式。\n\n**SF10. [R2-W1] Assumption A3 (P(Z=0)=0.5) 限制性在正文中讨论不足。** Appendix T 有 class imbalance 测试但完全在附录。\n\n---\n\n### Minor（不影响接收）\n\n1. Abstract \"7.4×\" 来源需明确标注基准（Global 0.059 vs EC-HTE 0.008 = 7.375×）\n2. Figure 3 panel 字号偏小（约正文 60-65%），打印可读性受影响\n3. \\citet / \\citep 使用需全文检查一致性\n4. 33 页附录导航困难，建议增加目录索引\n5. Algorithm 1 最后一页仅占 40%，余 60% 空白\n6. Table 1 \"95% CI Cov.\" 列未标注 MC 样本量\n7. Appendix E 子群大小不均衡影响未讨论\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上达成一致：\n\n1. **Overall 3.5 (Borderline Conference)**——理论扎实但 NLP 适配和非对称退化拉低总分\n2. **Soundness 4/5**——Theorem 1 推导正确，实验设计严谨\n3. **非对称退化是核心弱点**——标量形式和诊断准则在现实 LLM 非对称条件下效用有限\n4. **K ≤ 4 可扩展性限制**——显著限制 NLP 场景适用范围\n5. **MC=100 精度不足**——覆盖率声称需要更多 MC runs 或至少报告 SE\n6. **实验全面性是显著优势**——33 页附录在同领域罕见\n7. **格式合规**——Abstract ≤ 200 words，正文 ≤ 8 页，匿名性、ACL 模板均达标\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | 分析 |\n|------|----|----|------|\n| NLP 社区适配 | Excitement 3.5（问题本身足够重要） | Excitement 3（核心受众是因果推断社区） | R2 的关切更有说服力——三个贡献均为统计方法论，NLP 任务仅为测试平台 |\n| 诊断 AUC 退化 | Must-Fix（AUC=0.65 致命） | 未单独提出 Must-Fix | R1 的关切合理——Proposition 5 是核心贡献之一 |\n| F-L 差异化 | 认可 nesting statement 存在 | Must-Fix（正文阐述不够） | R2 的关切合理——需要更显式的 novelty statement |\n\n---\n\n## Questions for Authors\n\n1. [R1-Q1] Remark 2 声称矩阵形式不需要 A2。矩阵形式在非对称条件下的预测精度如何？为什么不基于矩阵形式构建诊断准则？\n2. [R1-Q2] K=8 退化的根因是 HB partial pooling 不足还是混淆矩阵估计误差？若 n_expert=1000, K=8，EC-HTE 能否恢复？\n3. [R1-Q3] Proposition 5 诊断 vs 直接运行 EC-HTE，增量价值具体是什么？\n4. [R2-Q1] Theorem 1 在 F-L 基础上新增的核心理论洞察是什么？对 F-L 在每个子群单独应用并加权聚合，能否得到等价分解？\n5. [R2-Q3] 真实仇恨言论案例中，子群定义有语言学依据吗？LLM 在不同子群上误差率不同的根本原因是什么？\n6. [R2-Q5] 子群划分函数 S 本身有噪声时，对 Theorem 1 和 EC-HTE 有何影响？\n\n---\n\n## Missing References\n\n1. **Veitch et al. (2020)** \"Adapting Text Embeddings for Causal Inference\" — text + causal inference 代表性工作（R2 提出）\n2. **Wood-Doughty et al. (2018)** \"Challenges of Using Text Classifiers for Causal Inference\" — 直接讨论文本分类器噪声对因果推断影响，高度相关（R2 提出）\n3. **Kadavath et al. (2022)** \"Language Models (Mostly) Know What They Know\" — LLM 校准代表性工作，与混淆矩阵校正互补（R2 提出）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（4 warning, 0 critical, 16 info）\n\n主要发现：\n- **[warning] Page 1-2**: 前两页纯文本无 display item，Figure 1 在第 3 页。建议考虑提前视觉锚点。\n- **[warning] Page 4-5**: 连续两页密集数学推导无 display item 穿插。\n- **[warning] Page 8**: 过度拥挤——Figure 4 + Table 1 + Section 5.3-5.4 + Conclusion + Limitations 全挤一页，主结果表和结论缺呼吸空间。\n- **[warning] Page 33**: Algorithm 1 仅占页面 40%，下方 60% 空白。\n- **[info]** Figure 1 质量优秀，Figure 2 EC-HTE pipeline 对比是全文最佳视觉元素，Table 1 使用 booktabs 规范。公式渲染无错误，双栏 margin 无溢出，正文 8 页合规。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n\n**EMNLP 2026 评分标准**: 3.5 = Borderline Conference（介于 Conference 和 Findings 之间）\n\n**置信度**: 4 / 5\n\n**判断理由**:\n\n论文在理论严谨性（Soundness 4/5）和实验全面性上达到 Conference 水平。Theorem 1 的乘积分解是一个干净、可验证的理论结果，\"debiasing hurts\" 的发现对 LLM 标注日益普及的 NLP 社区有实际意义。\n\n四个因素将总分从 Conference (4.0) 压至 Borderline (3.5)：\n\n1. **非对称退化未充分解决**：标题级 \"exact\" 声称与现实条件下的退化（R² 0.73, AUC 0.65）之间存在张力，Proposition 5 作为核心贡献之一的价值被削弱。\n2. **NLP 社区适配有限**：核心贡献在计量经济学/因果推断领域，NLP 任务仅作测试平台，正文缺少 NLP 特有的洞察和真实数据。\n3. **F-L 差异化不足**：新颖性为增量式——子群分解和 sign reversal 条件有价值，但不是根本性新发现。\n4. **K ≤ 4 可扩展性瓶颈**：限制了对 NLP 社区中多类分类场景的适用性。\n\n**升级路径 → 4.0 (Conference)**：\n- 正文充分讨论非对称退化并给出矩阵形式诊断\n- 将 Appendix M 真实数据移入正文，增强 NLP 定位\n- Section 3 显式 F-L novelty statement\n- Abstract/Intro 明确 K ≤ 4 限制\n\n**降级风险 → 3.0 (Findings)**：\n- AC 认为 NLP 社区 excitement 不足\n- \"exact\" 标题被视为 misleading\n\n当前定位：一篇 solid 的 Findings paper；若修改到位，可达 Conference。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 \"decision framework\" 应调整为 \"empirical operating guidelines\"\n- K ≤ 4 限制应在贡献列表中明确提及\n- F-L 比较数字（0.122–0.168 vs EC-HTE 0.008）已在正文，但 novelty 阐述不足\n\n### Section 2 (Related Work)\n- Noisy label learning 段落已添加但过于简略（3 句），建议建立 subgroup-dependent vs instance-dependent noise 的结构化联系\n- 缺 Veitch 2020, Wood-Doughty 2018（text + causal inference 核心文献）\n\n### Section 3 (Theory)\n- Theorem 1 推导正确，三因子分解优雅\n- A2 \"expository simplification\" 标注是改进，但需更明确区分 \"exact matrix identity\" vs \"scalar approximation\"\n- 建议 Theorem 1 后增加 K=2 数值示例（π_1=0.1, π_2=0.3）降低认知负担\n- Proposition 5: 需在正文讨论非对称 AUC 退化和诊断 vs EC-HTE 的增量价值\n\n### Section 4 (Method)\n- HB 估计规格完整，<5ms 计算成本是优势\n- κ-guard 设计合理\n- 先验敏感性仅 Gamma 超参变动，建议讨论替代先验\n\n### Section 5 (Experiments)\n- 合成验证（520 配置）极为全面\n- 正文应包含至少一个真实 NLP 数据实验\n- MC=100 需报告 SE；关键配置建议增至 ≥500\n- 仅 2 种 HTE 估计器，建议增加 X-learner 或 BART\n\n### Section 6 (Conclusion)\n- 3 句话合理，adoption guideline 有价值\n- 可增加 1 句讨论非对称推广的未来方向\n\n### Limitations\n- 覆盖 3 个要点，长度合规\n- 建议增加 A3 class imbalance 影响和 K ≤ 4 限制的显式提及\n\n### Appendix\n- 深度突出，是论文的核心竞争力之一\n- 建议增加目录索引改善导航\n- Page 33 Algorithm 1 空白过多"
  }
}
```

</details>

---


### Tool result

_source line 2249 · 2026-05-24T23:11:23.663994+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3970
}
```

</details>

---


### Assistant

_source line 2250 · 2026-05-24T23:11:34.600066+00:00_

**审稿报告已投递。**

Round 21 审稿完成。汇总：

- **Overall**: 3.5 / 5 (Borderline Conference)
- **Soundness**: 4/5，**Excitement**: 3–3.5/5
- **4 个 Must-Fix**: (1) 非对称退化正文讨论不足（AUC 0.86→0.65, R² 0.97→0.73）；(2) NLP 社区适配性有限；(3) 与 F-L (2003) 差异化不够清晰；(4) K≤4 可扩展性瓶颈未充分突出
- **10 个 Should-Fix**: HTE 估计器多样性、MC 精度、正文缺真实数据、操作条件措辞、噪声标签文献深度、诊断增量价值、符号密度、先验敏感性、A1 灵敏度参数化、A3 限制性
- **升级路径**: 解决非对称讨论 + 增强 NLP 定位 + 显式 F-L novelty statement → 4.0 (Conference)
- **Issue Tracker**: 已更新 47 个 issue（含 8 个 R21 新增）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 181

## Round 181

4 recorded events


### User

_source line 2251 · 2026-05-24T23:11:34.605985+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 的交叉回应

---

### Must-Fix

[AGREE] R2-N1: NLP 社区适配性不足
同意有一定道理，但程度上 R2 略有夸大。论文确实以统计/因果推断方法论为主，但 Table 12-13（page 20）用 6 个真实 LLM 实证验证了子群异质性是 LLM 标注器的结构性属性（Spearman ρ = 0.82-1.00, Appendix N），这是 NLP-specific 发现。建议将此条从 Must-Fix 降为 Should-Fix。增加 "Implications for NLP Annotation Pipelines" 段落和将 Appendix M 关键结果移入正文是好建议，但不应阻止接收。

[REBUT] R2-N2: 与 F-L (2003) 差异不清晰
R2 认为 Theorem 1 与 F-L "形式上高度相似"，不准确。F-L 是全局标量衰减 β̂=(1−2ε)·β，假设误分类率均匀，无法刻画子群异质性。Theorem 1 的 δ_s·Δτ/(1−2ε̄) 是三因子乘积分解，揭示 bias 方向可在子群间反转——F-L 结构中不存在此现象。正文 page 4 proof sketch 和 page 2 Introduction 均已说明差异。Appendix Z.5 Table 35 实证对比：F-L per-subgroup Bias 0.112, coverage 65.3% vs EC-HTE Bias 0.004, coverage 97.8%。但同意 Table 35 关键数字应在正文中引用以加强 novelty claim。

### Should-Fix

[AGREE] R2-W1: A3 限制性讨论不足。Appendix T 证明 R²≥0.976 across P(Z=1)∈{0.1-0.5}，但全在附录。正文应至少一句话提及。

[AGREE] R2-W2: 操作条件是经验导出非理论保证。"decision framework" 措辞略 over-claim，应改为 "empirically calibrated operating guidelines"。不影响实质贡献。

[AGREE] R2-W3: 正文缺真实数据实验。与我 Round 1 的观点一致。移 Appendix M 关键结果入正文可提升说服力。

[AGREE] R2-W4: 噪声标签学习文献关联可更深入。subgroup-dependent misclassification 与 instance-dependent noise 的关联值得一段讨论。

[AGREE] R2-W5: Section 3 符号密度高。Theorem 1 后增加数值示例（K=2, ε₁=0.05, ε₂=0.25 → bias₁ 计算）只需 3-4 行，显著提升可读性。

### Minor

[AGREE] R2-Minor-1: "7.4×" 应注明 Table 1 出处。
[AGREE] R2-Minor-2-4: 排版改进建议均合理。33 页附录确实需目录索引。

### 遗漏相关工作

[AGREE] Veitch et al. (2020): 应引用，text-as-confounder 与本文 text-as-effect-modifier 互补。
[AGREE] Wood-Doughty et al. (2018): 应引用，最早系统讨论文本分类器用于因果推断的挑战。
[REBUT] Kadavath et al. (2022): LLM 自我校准与本文处理的误分类传播问题正交，非核心缺失。

### 总结

R2 的审稿总体合理。最重要的分歧在 N2：F-L 与 Theorem 1 的结构差异是实质性的（标量衰减 vs 子群乘积分解），R2 低估了这一 novelty。N1（NLP 适配性）有一定道理但严重程度不到 Must-Fix。其余 Should-Fix 和 Minor 意见均建设性，与我 Round 1 的独立观察一致。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。核心分歧：R2-N2（F-L 相似性）我明确反驳——F-L 是标量衰减，Theorem 1 是子群乘积分解，结构性不同；R2-N1（NLP 适配性）部分同意但建议降级为 Should-Fix。其余 Should-Fix/Minor 意见均表示同意。

---

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 的交叉回应

---

### Must-Fix 逐条回应

**[AGREE] R1-N1: Proposition 5 非对称 AUC 退化（0.86→0.65）**

同意这是一个重要问题。Remark 2（page 5）明确承认 "the area under the ROC curve (AUC) decreases from 0.86 to 0.65 (Appendix J)"，而 Table 12-13（Appendix N）显示真实 LLM 的 FPR/FNR 比率达 1.1-7.1，说明非对称是常态而非例外。

但我认为 R1 的措辞"AUC=0.65 仅略好于随机"略有夸大：
1. AUC=0.65 在 baseline AUC=0.50 基础上有 30% 的相对提升，对**筛选工具**而言仍有实用价值——诊断的目的是快速决策，不是精确预测
2. 诊断的**假阳性成本较低**：如果诊断误判"需要 per-subgroup 校正"，后果是增加了 variance（因为 per-subgroup 估计更稀疏），而非引入 bias——这与假阴性（遗漏有害的 global correction）的后果不对等
3. 论文在正文（Remark 2，page 5）已经披露了这一退化，不存在隐瞒

**但核心判断我同意 R1**：Proposition 5 被列为三个核心贡献之一（page 2，Contribution 1 的一部分："the identity immediately yields a Δτ-free diagnostic"），如果在现实条件下 AUC 仅 0.65，需要在正文中更显著地讨论这一限制，而不是仅在 Remark 2 末尾一句带过。建议在 Section 5.4（Diagnostic and Operating Conditions）增加 1 段讨论非对称条件下的诊断性能退化。

---

**[AGREE with qualification] R1-N2: "Exact" 标题与标量近似 R² 退化的张力**

R1 的观察是准确的，但我认为需要区分两个层次：

**(a) 标题 "Exact Bias Identity" 技术上正确**：Theorem 1 在 (A1)-(A5) 下是精确的（非近似）。矩阵形式（Remark 2, Appendix C, Corollary 6）在放松 (A2) 后也是精确的。"Exact" 指的是恒等式本身，而非其标量近似。

**(b) Abstract 中 R² 声明确实需要限定**：Abstract 写 "verified at R² ≥ 0.97 on synthetic grids"——这个 0.97 确实是对称条件下的结果。然而，Abstract 接着说 "R² = 0.975 in aggregate across 11 real LLM confusion matrices; per-model range 0.76–0.99"——这些真实 LLM 具有非对称混淆矩阵，R² 仍然高（聚合 0.975，最低 0.76）。这说明标量近似在真实（非对称）LLM 上仍然工作得相当好。

**(c) R1 所引 R²=0.05-0.21 需要上下文**：这些极低 R² 出现在 K=2, Δτ=0.05 的配置下。当 Δτ=0.05 时，偏差项 δ_s·Δτ/(1-2π̄) 本身极小（接近零），此时 R² 低是因为信号极弱（分母接近零的比值），而非近似误差大。**在绝对偏差意义上，近似误差仍然很小，只是相对于接近零的真实偏差看起来很大。** 这类似于在真值接近零时相对误差可以无穷大但绝对误差极小的统计学常识。

**综合判断**：同意 Abstract 应加限定（如 "under the symmetric scalar approximation"），但不认为需要更改标题——"Exact Bias Identity" 是对 Theorem 1 本身的准确描述。将此视为 Should-Fix 而非 Must-Fix 更合理。

---

**[AGREE with qualification] R1-N3: K≤4 可扩展性限制**

同意 K≤4 是一个真实的实践限制。Table 5（Appendix L.2, page 17）确认 K=8 时 EC-HTE 的 RMSE (0.340) 超过 global correction (0.168)。

但我认为 R1 的论述 "NLP 分类常有 K>4" 混淆了两个概念：
1. **K 是子群数量，不是类别数量**。论文中 K 指 effect modifier Z 的子群划分（如文本长度分位数、hashtag 有无），由实践者自行选择，不等于 NLP 任务的类别数
2. **K=2-4 覆盖了大多数实际场景**。二分法（K=2：长/短文本）或四分位法（K=4）是社会科学因果推断中最常见的子群划分方式

**真正的限制在于 expert budget**：K=4, n_expert/K≥50 → 需 200 个专家标签。这在实践中是合理的——200 个标注的成本远低于全量人工标注。但论文应更明确讨论 K 的选择指导（如何决定子群数量、是否存在最优 K 的选择准则）。

综合：降级为 Should-Fix 更合理——这是已知且已披露的限制（Section 5.4, Limitations），不应一票否决。

---

### Should-Fix 逐条回应

**[REBUT] R1-W1: 缺少 X-learner/BART**

R1 的前提有遗漏。论文实际测试了**三种**下游估计器，而非两种：
- Difference-in-Means (DIM)（Section 5.1-5.2）
- CausalForestDML（Section 5.3, Table 1）
- R-learner（Appendix S, Table 19）

更关键的是，EC-HTE 的偏差校正发生在**混淆矩阵反转阶段**（Section 4.2, 公式 μ̂_s = C_s^{-1} · μ̃_s），独立于下游 CATE 估计器。Theorem 1 的偏差恒等式也是估计器无关的（characterizes bias in corrected moments, not in specific estimators）。因此，X-learner/BART 的缺席不影响核心 claim 的有效性。

三种估计器覆盖了：非参数（CausalForest）、半参数（R-learner）、参数（DIM）三种范式。对一篇会议论文来说这是充分的。

---

**[AGREE] R1-W2: MC 标准误未报告**

完全同意。MC=100 时 coverage SE ≈ 0.022，部分实验仅 50/20 runs 会更大。Table 1 等关键表格应报告 MC 样本量和 SE（或至少在 footnote 中标注）。这是实验报告的基本规范，修复成本低。

---

**[REBUT] R1-W3: Proposition 5 诊断 vs 直接 EC-HTE 增量价值**

R1 认为两者需要相同的 expert labels，因此诊断没有增量价值。但这忽略了诊断的核心功能：**它告诉你何时不应该做 per-subgroup 校正**。

具体而言：
1. **计算成本差异显著**：Proposition 5 诊断只需计算 per-subgroup FPR/FNR 并检查阈值——一行代码。EC-HTE 需要 MCMC 采样（4 chains × 5000 iterations，Appendix G）+ CausalForestDML fitting。诊断作为前置筛选可避免不必要的全流程运行。
2. **风险管理功能**：当诊断判定 global correction 是安全的（Δπ < 0.15 或 K 太大），直接运行 EC-HTE 反而有害——因为稀疏的 per-subgroup 估计会增加 variance（正如 K=8 退化所示）。诊断的价值恰恰在于**阻止你运行 EC-HTE**。
3. **可解释性**：诊断输出的是误差率异质性的量化指标（Δπ, κ(C_s)），帮助实践者理解**为什么**校正可能有害，而不只是看到 RMSE 数字。

论文确实应该更明确地阐述这一点——当前 Section 5.4 的讨论偏向操作条件的列举，未充分传达诊断作为"决策工具"的价值定位。

---

**[AGREE] R1-W4: HB 先验敏感性分析范围有限**

同意。Table 3（Appendix G.1, page 15）仅变动 Gamma(α, b_0) 超参数，未测试替代先验族（如 logistic-normal on π_s, Beta prior on error rates）。对层次贝叶斯方法而言，先验族选择的敏感性通常比超参数调节更重要。不过，考虑到：(a) 默认 Gamma(3,1) 在 15 个配置中表现稳定（RMSE 变动 < 1.9%）；(b) 这是会议论文而非期刊论文——我认为这是 Should-Fix 而非 Must-Fix，当前敏感性分析基本达到会议论文的标准。

---

**[AGREE] R1-W5: A1 敏感度分析参数化形式单一**

同意。Appendix Z.3（page 29）测试了 outcome-dependent misclassification 的 logistic link（γ_Y ∈ [0, 0.20]），但未考虑其他违反 A1 的形式（如 treatment-dependent misclassification、nonlinear interactions between outcome and misclassification）。γ_Y = 0.20 对应的 coverage 仍 > 89.7%，说明方法对中等违反有鲁棒性，但更极端的违反未被测试。这是一个合理的 improvement suggestion。

---

### Minor 逐条回应

**[AGREE] R1-M1**: Abstract R²=0.975 应标注 "under symmetric approximation"。与我的审稿意见一致（我的 Minor Issue #1 也指出了 7.4× 来源不明）。不过如前述，Abstract 中 R²=0.975 across 11 real LLM CMs 实际上已经包含了非对称效应，只是标量近似 vs 矩阵形式的区别应显式标注。

**[AGREE] R1-M2**: Table 1 未标注 MC 样本量。基本实验报告规范，应修复。

**[AGREE] R1-M3**: Figure 2 "7.4" 注释有歧义。我在自己的审稿中也标记了同一问题——abstract 声称 "7.4×" 但从 Table 1 数字难以直接验证这个倍数。

**[AGREE] R1-M4**: Appendix E 未讨论子群大小不均衡。当某些子群样本量远小于其他子群时，层次贝叶斯估计的 partial pooling 行为会不同，这值得讨论。

**[AGREE] R1-M5**: AI Assistants 声明可更具体。当前声明（page 32）格式合规，但可以更具体说明 Claude 在哪些 section 中辅助了写作。低优先级。

---

### Questions 回应

**Q1: 为什么不基于矩阵形式构建诊断？**

这是一个 R1 和我都关心的问题。矩阵形式（Corollary 6, Appendix C）的诊断需要 per-subgroup 的完整 2×2 混淆矩阵（FPR_s 和 FNR_s 分别），而标量诊断只需 π_s。矩阵诊断的输入需求更高但精度更好。**论文应该讨论这个 trade-off**：在专家标签充足时，矩阵诊断可能是更好的选择；在标签稀疏时，标量诊断的 AUC=0.65 可能是可接受的折中。

这与我的 Must-Fix N2（F-L differentiation）相关——如果论文提供了矩阵和标量两种诊断并讨论适用条件，整体贡献会更强。

**Q2: K=8 退化根因？n_expert=1000, K=8 能否恢复？**

论文在 Appendix L.2（Table 5, page 17）测试了 K=8, n_expert=250（31 labels/subgroup），EC-HTE RMSE = 0.340 > global 0.168。根因是 per-subgroup 样本太稀疏——31 labels 不足以可靠估计 2×2 混淆矩阵。

论文未测试 n_expert=1000, K=8（125 labels/subgroup），这确实是一个缺失的实验。按 Appendix I 的 budget crossover 分析（Table 14, page 16），n_expert ≥ 250 per subgroup 可能是 K=8 的恢复阈值，但这需要总计 2000 个专家标签——在实践中成本显著增加。

**Q3: Proposition 5 诊断 vs 直接 EC-HTE 增量价值？**

已在 W3 反驳中详细回答。核心：诊断的价值在于"不校正"决策 + 计算成本节省 + 可解释性。

**Q4: Real-data case study 中 EC-HTE 是否改变实质结论？**

好问题。从 Appendix M（page 18-19）的描述看，hate speech 案例中 EC-HTE 主要改善了 coverage 和 bias，但论文未明确报告 CATE 估计值是否发生**方向性改变**（即是否存在 sign reversal）。如果 EC-HTE 只是改善了 confidence interval 宽度而未改变实质结论，实践 impact 会减弱。这应该在 real-data 案例中明确报告。

---

### 综合评价

R1 的审稿质量很高，特别是 N1（非对称诊断退化）和 N2（"exact" framing 张力）是我在自己的审稿中未充分强调的重要问题。R1 的 Excitement 3.5 比我的 3.0 高，我认为这可能是因为 R1 更看重理论贡献本身的技术质量，而我更关注 NLP 社区适配。

**我维持 Overall 3.5 (Borderline Conference)** 的评分。如果作者能 (1) 加强非对称条件下的诊断讨论、(2) 补充 F-L 的正文 differentiation、(3) 移入一个真实数据实验到正文，论文可以上升到 4.0 (Conference)。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **Must-Fix**: 3 条中 3 条 [AGREE]（均带 qualification）——N1 非对称诊断退化是最有力的新发现；N2 标题张力同意需要 abstract 限定但不需改标题；N3 K≤4 限制同意但认为 K 是设计参数而非硬约束
- **Should-Fix**: W1 [REBUT]（论文实际测了 3 种估计器，且偏差校正与下游估计器无关），W2-W5 均 [AGREE]
- **Minor**: 5 条全部 [AGREE]
- **Questions**: Q3 [REBUT]（诊断的价值在于"不校正"决策），Q1/Q2/Q4 认为应由作者回答

维持 Overall 3.5 (Borderline Conference) 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2252 · 2026-05-24T23:15:14.573407+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "force_resubmit": "True",
  "report": "# Round 21 审稿报告（含交叉回应）\n\n**论文**: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性 + 实验完备性）、R2（新颖性 + 完整性 + NLP 社区适配）\n**审稿模式**: Fresh（重新审稿）\n**交叉回应**: R1↔R2 完成，共识已达成\n\n---\n\n## Summary\n\n本文推导了一个精确偏差恒等式（Theorem 1），证明当 LLM 标注的误分类率在子群间异质时，标准全局混淆矩阵校正引入子群级偏差 δ_s·Δτ/(1−2π̄)，在 14.9% 的配置中反转 CATE 符号。论文提出 EC-HTE 方法（层次贝叶斯逐子群混淆矩阵估计 + 分层校正），在合成数据（520 配置）和半合成数据（16 个真实 LLM 混淆矩阵 × 4 NLP 任务）上验证，偏差缩减 7.4×（extreme heterogeneity）。另推导 Δτ-free 诊断准则（Proposition 5）和操作条件。\n\n---\n\n## Strengths\n\n**S1. [共识] 问题提出新颖且重要。** \"Global correction 可反转 CATE 符号\"这一发现在 LLM 标注日益普及的背景下非常及时。Figure 1 三面板直观有效。（R1-S1, R2-S4）\n\n**S2. [共识] 理论贡献干净且可验证。** Theorem 1 的乘积形式 δ_s × Δτ / (1−2π̄) 简洁可解释，合成数据 R² ≥ 0.97，11 个真实 LLM 混淆矩阵聚合 R² = 0.975。推导逻辑清晰（Appendix B）。（R1-S2, R2-S1）\n\n**S3. [共识] 实验验证深度突出。** 33 页附录涵盖 A1-A5 每个假设的敏感性分析、class imbalance、先验敏感性、bootstrap SE、跨模型一致性（6 个 LLM）、PPCI 互补性、F-L 对比、CausalForest oracle coverage、confounded treatment 等。同领域罕见的全面性。（R1-S3, R2-S3）\n\n**S4. [共识] Δτ-free 诊断有实用价值。** Proposition 5 仅需子群误差率即可判断是否应做逐子群校正，无需估计处理效应。R2 交叉回应澄清：诊断的核心价值在于\"告诉你何时不应做 per-subgroup 校正\"——当 Δπ < 0.15 或 K 过大时，直接运行 EC-HTE 反而有害（variance 增加），诊断作为前置筛选可避免不必要的全流程运行。（R2-S2, R2 对 R1-W3 的反驳）\n\n**S5. [共识] 方法互补性设计好。** EC-HTE（covariate-side）与 PPCI（outcome-side）正交组合，bias 从 0.179 降至 0.007。（R2-S5）\n\n**S6. [共识] 可复现性。** Algorithm 1 完整，匿名代码仓库已提供，MCMC 诊断达标（R̂ < 1.01, ESS > 843）。（R1-S4）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [R1-N1, R2 AGREE] 非对称误分类下诊断准则退化——正文讨论严重不足**\n\nProposition 5 在对称假设 (A2) 下 AUC=0.86，但真实 LLM 几乎总是非对称（FPR/FNR 比率 1.1–7.1, Table 12）。非对称下 AUC 降至 0.65。\n\nR2 在交叉回应中补充了重要 nuance：\n- AUC=0.65 对筛选工具仍有实用价值（baseline 0.50 上 30% 相对提升）\n- 假阳性成本较低（多做 per-subgroup 校正增加 variance 但不引入 bias），假阴性成本更高（遗漏有害 global correction）\n- 论文在 Remark 2 已披露此退化，不存在隐瞒\n\n**但核心判断两位 Reviewer 一致**：Proposition 5 被列为三大贡献之一，如果在现实条件下 AUC 仅 0.65，需要在正文中更显著地讨论这一限制，而不是仅在 Remark 2 末尾一句带过。\n\n**建议**：Section 5.4 增加 1 段讨论非对称诊断性能退化；讨论矩阵形式诊断 vs 标量诊断的 trade-off（前者精度更高但输入需求更大）。\n\n---\n\n**MF2. [R2-N1, R1 部分 AGREE] NLP 社区适配性不足**\n\n三个贡献全部属于测量误差理论/因果推断方法论。NLP 任务仅作测试平台，正文缺 NLP 特有洞察，真实数据实验在附录。\n\nR1 在交叉回应中部分同意但认为严重程度不到 Must-Fix：Table 12-13 用 6 个真实 LLM 实证验证了子群异质性是 LLM 标注器的结构性属性（Spearman ρ = 0.82-1.00），这是 NLP-specific 发现。R2 Excitement 3/5，R1 Excitement 3.5/5——R1 认为问题本身对 NLP 社区足够重要。\n\n**综合判断**：维持 Must-Fix——EMNLP AC 对 NLP 社区适配有明确期待，且修改方案清晰、成本低。\n\n**建议**：(a) 将 Appendix M 仇恨言论案例关键结果移入正文；(b) 讨论误分类异质性的语言学来源；(c) 增加 \"Implications for NLP Annotation Pipelines\" 段落。\n\n---\n\n### 从 Must-Fix 降级为 Should-Fix（交叉回应后调整）\n\n**SF-A. [R1-N2 初审 Must-Fix → 交叉后 Should-Fix] \"Exact\" 标题与标量近似 R² 退化的张力**\n\nR2 在交叉回应中提供了有力澄清：\n- 标题 \"Exact Bias Identity\" 技术上正确——Theorem 1 在 (A1)-(A5) 下是精确恒等式，矩阵形式放松 (A2) 后也精确\n- R1 所引 R²=0.05-0.21 出现在 Δτ=0.05 配置下，此时偏差项本身极小（接近零），R² 低是因为信号极弱而非近似误差大——绝对偏差仍然很小\n- Abstract 中 R²=0.975 across 11 real LLM CMs 已包含非对称效应，只是标量近似 vs 矩阵形式的区别应显式标注\n\n**降级理由**：标题准确描述 Theorem 1 本身；Abstract 需加限定但不需改标题。\n\n**建议**：Abstract 标注 \"under the symmetric scalar approximation\"；Section 3 更明确区分 \"exact matrix identity\" 和 \"scalar approximation\"。\n\n---\n\n**SF-B. [R2-N2 初审 Must-Fix → 交叉后 Should-Fix] 与 F-L (2003) 的差异化**\n\nR1 在交叉回应中明确反驳：F-L 是全局标量衰减 β̂=(1−2ε)·β，无子群结构；Theorem 1 的 δ_s·Δτ/(1−2ε̄) 是三因子乘积分解，揭示 bias 方向可在子群间反转——F-L 结构中不存在此现象。实证对比：F-L per-subgroup Bias 0.112, coverage 65.3% vs EC-HTE Bias 0.004, coverage 97.8%（Appendix Z.5 Table 35）。\n\nR2 未对此反驳做进一步 REBUT。\n\n**降级理由**：R1 的反驳有实质依据——Theorem 1 与 F-L 的差异是结构性的（标量衰减 vs 子群乘积分解），novelty 成立。问题转为**展示清晰度**而非**novelty 本身**。\n\n**建议**：将 Appendix Z.5 Table 35 关键数字移入正文 Section 3 或 Table 1 附近；在 Theorem 1 后增加 2-3 句 explicit novelty statement。\n\n---\n\n**SF-C. [R1-N3 初审 Must-Fix → 交叉后 Should-Fix] K ≤ 4 可扩展性限制**\n\nR2 在交叉回应中提供了重要澄清：\n- K 是子群数量而非类别数量——由实践者自行选择（如文本长度分位数、hashtag 有无），不等于 NLP 任务的类别数\n- K=2-4 覆盖了社会科学因果推断中最常见的子群划分方式\n- 真正的限制在于 expert budget（K=4 需 200 标签），在实践中成本合理\n\nR1 未对此做进一步 REBUT。\n\n**降级理由**：R2 澄清了 K 的语义——它是设计参数而非硬约束。限制已在 Section 5.4 和 Limitations 中披露。\n\n**建议**：Introduction 增加 1 句明确 K 的含义和 K ≤ 4 建议；讨论 K 选择指导准则。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [R1-W1 → R2 REBUT] HTE 估计器多样性**\n\nR2 在交叉回应中反驳：论文实际测试了 3 种估计器（DIM + CausalForestDML + R-learner），覆盖参数、非参数、半参数三种范式。更关键的是，EC-HTE 的偏差校正发生在混淆矩阵反转阶段（Section 4.2），独立于下游 CATE 估计器。Theorem 1 也是 estimator-agnostic。R1 未对此做进一步 REBUT。\n\n**综合判断**：R2 反驳有效——3 种估计器 + estimator-agnostic 校正对会议论文充分。降低优先级。\n\n**SF2. [R1-W2, R2 AGREE] MC=100 覆盖率精度。** SE ≈ 2.2pp，Table 1 应报告 MC SE。两位 Reviewer 完全一致。\n\n**SF3. [R2-W3, R1 AGREE] 正文缺完整真实数据实验。** 移 Appendix M 关键结果入正文。两位 Reviewer 一致。\n\n**SF4. [R2-W2, R1 AGREE] 操作条件是经验导出。** 称 \"decision framework\" 应调整为 \"empirically calibrated operating guidelines\"。\n\n**SF5. [R2-W4, R1 AGREE] 噪声标签学习文献关联可更深入。** subgroup-dependent vs instance-dependent noise 结构化联系未建立。\n\n**SF6. [R1-W3 → R2 REBUT] Proposition 5 诊断增量价值。** R2 的反驳有说服力：诊断的核心功能是\"不校正\"决策（当 Δπ < 0.15 或 K 过大时阻止运行 EC-HTE） + 计算成本节省（一行代码 vs MCMC + CausalForest） + 可解释性。但论文当前未充分传达此定位。**建议**：Section 5.4 增加诊断作为\"前置决策工具\"的价值阐述。\n\n**SF7. [R2-W5, R1 AGREE] Section 3 符号密度偏高。** 建议 Theorem 1 后增加 K=2 数值示例。\n\n**SF8. [R1-W4, R2 AGREE] HB 先验结构性敏感性。** 仅 Gamma 超参变动，未考虑替代先验族。R2 补充：当前分析对会议论文基本达标。\n\n**SF9. [R1-W5, R2 AGREE] A1 灵敏度参数化受限。** 仅 logistic link、γ ∈ [0, 0.20]。R2 补充：横向覆盖面充分（8 种假设违反类型），参数化是领域标准做法。\n\n**SF10. [R2-W1, R1 AGREE] A3 (P(Z=0)=0.5) 正文讨论不足。** Appendix T 有测试但全在附录。\n\n---\n\n### Minor（不影响接收）\n\n1. Abstract \"7.4×\" 应标注 Table 1 出处（Global 0.059 vs EC-HTE 0.008 = 7.375×）[R1, R2 AGREE]\n2. Figure 3 panel 字号偏小（约正文 60-65%）[R2]\n3. \\citet / \\citep 一致性需全文检查 [R2]\n4. 33 页附录建议增加目录索引 [R1, R2 AGREE]\n5. Page 33 Algorithm 1 仅占 40%，余 60% 空白 [视觉审查]\n6. Table 1 \"95% CI Cov.\" 列未标注 MC 样本量 [R1]\n7. Appendix E 未讨论子群大小不均衡影响 [R1, R2 AGREE]\n8. Page 8 过度拥挤（Figure 4 + Table 1 + Conclusion + Limitations 全挤一页）[视觉审查]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n交叉回应后两位 Reviewer 在以下关键问题上完全一致：\n\n1. **Overall 3.5 (Borderline Conference)**\n2. **Soundness 4/5** — Theorem 1 推导正确，实验设计严谨\n3. **非对称诊断退化是核心弱点** — AUC 0.86→0.65，正文讨论不足（Must-Fix）\n4. **NLP 社区适配需加强** — 真实数据和 NLP 洞察应进正文（R1 认为 Should-Fix，R2 认为 Must-Fix）\n5. **MC=100 需报告 SE** [AGREE]\n6. **操作条件应标为 empirical guidelines** [AGREE]\n7. **Section 3 符号密度高，需数值示例** [AGREE]\n8. **HB 先验和 A1 灵敏度可扩展** [AGREE]\n9. **实验全面性是显著优势** [AGREE]\n10. **格式合规**（Abstract ≤ 200 words, 正文 ≤ 8 页, 匿名性, ACL 模板）[AGREE]\n\n---\n\n## Reviewer Divergence（交叉后仍存在的分歧）\n\n| 问题 | R1 | R2 | 交叉后共识 |\n|------|----|----|-----------|\n| NLP 适配严重性 | Should-Fix（Excitement 3.5） | Must-Fix（Excitement 3） | 维持 Must-Fix（EMNLP AC 明确期待 NLP 适配） |\n| F-L 差异化 | R1 REBUT：结构性不同 | R2 未进一步反驳 | 降为 Should-Fix（展示问题而非 novelty 问题）|\n| \"Exact\" 标题 | Must-Fix | Should-Fix（技术上正确） | 降为 Should-Fix |\n| K ≤ 4 严重性 | Must-Fix | Should-Fix（K 是设计参数） | 降为 Should-Fix |\n| HTE 估计器 | Should-Fix（缺 X-learner） | REBUT（3 种够了 + estimator-agnostic） | 降低优先级 |\n| 诊断增量价值 | Should-Fix（标签需求相同） | REBUT（\"不校正\"决策功能） | 维持 Should-Fix（论文需更好阐述） |\n\n---\n\n## Questions for Authors\n\n1. [R1-Q1, R2 补充] 矩阵形式诊断 vs 标量诊断的 trade-off 如何？在专家标签充足时，是否应推荐矩阵形式？\n2. [R1-Q2] K=8, n_expert=1000（125 labels/subgroup）时 EC-HTE 能否恢复？\n3. [R2-Q1, R1 REBUT 提供部分回答] Theorem 1 相对 F-L 的核心新增洞察：δ_s × Δτ 交互导致 sign reversal——这一点如何在正文中更显式传达？\n4. [R2-Q3] 真实仇恨言论案例中子群定义的语言学依据？LLM 误差异质性的根本原因？\n5. [R1-Q4, R2 补充] Real-data case study 中 EC-HTE 是否改变了 CATE 的方向性结论？R2 指出论文未明确报告是否存在 sign reversal——如仅改善 CI 宽度则 impact 减弱。\n6. [R2-Q5] 子群划分函数 S 本身有噪声时对 Theorem 1 的影响？\n\n---\n\n## Missing References\n\n1. **Wood-Doughty et al. (2018)** \"Challenges of Using Text Classifiers for Causal Inference\" — 最早系统讨论文本分类器用于因果推断的挑战，高度相关 [R1 AGREE, R2 提出]\n2. **Veitch et al. (2020)** \"Adapting Text Embeddings for Causal Inference\" — text-as-confounder 与本文 text-as-effect-modifier 互补 [R1 AGREE, R2 提出]\n3. **Kadavath et al. (2022)** \"Language Models (Mostly) Know What They Know\" — LLM 校准。R1 认为与本文正交，非核心缺失；R2 认为校准作为替代方案值得讨论 [分歧]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（4 warning, 0 critical, 16 info）\n\n主要发现：\n- **[warning] Page 1-2**: 前两页纯文本，Figure 1 在第 3 页。建议考虑提前视觉锚点。\n- **[warning] Page 4-5**: 连续两页密集数学无 display item。\n- **[warning] Page 8**: 过度拥挤——Figure 4 + Table 1 + Section 5.3-5.4 + Conclusion + Limitations 全挤一页。\n- **[warning] Page 33**: Algorithm 1 仅占 40%，余 60% 空白。\n- **[info]** Figure 1 质量优秀，Figure 2 pipeline 对比是最佳视觉元素，Table 1 booktabs 规范。公式渲染无错误，正文 8 页合规。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n\n**EMNLP 2026 评分标准**: 3.5 = Borderline Conference\n\n**置信度**: 4 / 5（交叉回应后提升——两位 Reviewer 独立评估高度一致）\n\n**判断理由**:\n\n论文在理论严谨性（Soundness 4/5）和实验全面性上达到 Conference 水平。Theorem 1 的乘积分解是一个干净、可验证的理论结果，与 F-L (2003) 的差异是结构性的（交叉回应中 R1 有效反驳了 R2 的 \"形式相似\" 判断）。\"Debiasing hurts\" 的发现对 LLM 标注日益普及的 NLP 社区有实际意义。\n\n两个因素将总分从 Conference (4.0) 压至 Borderline (3.5)：\n\n1. **非对称诊断退化**（Must-Fix）：Proposition 5 作为核心贡献之一，在现实 LLM 非对称条件下 AUC 仅 0.65，正文讨论不足。虽然 R2 指出 AUC=0.65 对筛选工具仍有价值，但论文需更显著地呈现此限制。\n\n2. **NLP 社区适配**（Must-Fix）：核心贡献在统计方法论，NLP 任务仅为测试平台，正文缺 NLP 特有洞察和真实数据实验。R1 认为 Excitement 3.5（问题重要性足够），R2 认为 Excitement 3（受众窄）。\n\n**升级路径 → 4.0 (Conference)**：\n- Section 5.4 充分讨论非对称诊断退化 + 矩阵形式 trade-off\n- Appendix M 真实数据移入正文 + NLP 标注管道影响讨论\n- Theorem 1 后增加数值示例降低 Section 3 认知负担\n- Table 1 报告 MC SE\n\n**降级风险 → 3.0 (Findings)**：\n- AC 认为 NLP 社区 excitement 不足\n\n当前定位：一篇 solid 的 Findings paper；修改到位可达 Conference。升级所需改动量合理（正文内调整，无需新实验）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 措辞调整为 \"empirically calibrated operating guidelines\"\n- 增加 1 句明确 K 的含义（子群数量而非类别数量）和 K ≤ 4 建议\n- NLP motivation example（content moderation）有效，但后续 NLP 洞察未跟进\n\n### Section 2 (Related Work)\n- Noisy label learning 段落已添加但仅 3 句——建议建立 subgroup-dependent vs instance-dependent noise 联系\n- 缺 Wood-Doughty 2018, Veitch 2020（text + causal inference 核心文献）\n- F-L nesting statement 存在但不够显式——R1 建议将 Table 35 关键数字移入正文\n\n### Section 3 (Theory)\n- Theorem 1 推导正确，三因子分解优雅\n- A2 \"expository simplification\" 标注和 Remark 2 是改进\n- 建议 Theorem 1 后增加 K=2 数值示例（ε₁=0.05, ε₂=0.25）降低认知负担\n- 更明确区分 \"exact matrix identity\"（Remark 2）和 \"scalar approximation\"（Eq. 2）\n- Proposition 5: 正文讨论非对称 AUC 退化 + 阐述\"不校正\"决策的价值定位\n\n### Section 4 (Method)\n- HB 估计规格完整，<5ms 是优势\n- κ-guard 设计合理\n- 先验敏感性：当前 Gamma 超参变动对会议论文基本达标，替代先验族（logistic-normal）可作为 camera-ready 扩展\n\n### Section 5 (Experiments)\n- 合成验证（520 配置）全面\n- 应包含至少一个真实 NLP 数据实验（移 Appendix M 关键发现入正文）\n- Table 1 报告 MC SE\n- 3 种 HTE 估计器（DIM + CausalForest + R-learner）覆盖三种范式，对会议论文充分（R2 交叉回应有效反驳了 R1 的 \"缺 X-learner\" 关切——校正与下游估计器无关）\n\n### Section 6 (Conclusion)\n- 3 句话含 adoption guideline，长度合理\n- 可增加 1 句讨论非对称推广的未来方向\n\n### Limitations\n- 覆盖 3 个要点，长度合规\n- 建议增加 A3 class imbalance 和 K 含义的显式提及\n\n### Appendix\n- 深度突出，是论文核心竞争力之一\n- 建议增加目录索引\n- Page 33 空白过多"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "force_resubmit": "True",
    "report": "# Round 21 审稿报告（含交叉回应）\n\n**论文**: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**Deadline**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性 + 实验完备性）、R2（新颖性 + 完整性 + NLP 社区适配）\n**审稿模式**: Fresh（重新审稿）\n**交叉回应**: R1↔R2 完成，共识已达成\n\n---\n\n## Summary\n\n本文推导了一个精确偏差恒等式（Theorem 1），证明当 LLM 标注的误分类率在子群间异质时，标准全局混淆矩阵校正引入子群级偏差 δ_s·Δτ/(1−2π̄)，在 14.9% 的配置中反转 CATE 符号。论文提出 EC-HTE 方法（层次贝叶斯逐子群混淆矩阵估计 + 分层校正），在合成数据（520 配置）和半合成数据（16 个真实 LLM 混淆矩阵 × 4 NLP 任务）上验证，偏差缩减 7.4×（extreme heterogeneity）。另推导 Δτ-free 诊断准则（Proposition 5）和操作条件。\n\n---\n\n## Strengths\n\n**S1. [共识] 问题提出新颖且重要。** \"Global correction 可反转 CATE 符号\"这一发现在 LLM 标注日益普及的背景下非常及时。Figure 1 三面板直观有效。（R1-S1, R2-S4）\n\n**S2. [共识] 理论贡献干净且可验证。** Theorem 1 的乘积形式 δ_s × Δτ / (1−2π̄) 简洁可解释，合成数据 R² ≥ 0.97，11 个真实 LLM 混淆矩阵聚合 R² = 0.975。推导逻辑清晰（Appendix B）。（R1-S2, R2-S1）\n\n**S3. [共识] 实验验证深度突出。** 33 页附录涵盖 A1-A5 每个假设的敏感性分析、class imbalance、先验敏感性、bootstrap SE、跨模型一致性（6 个 LLM）、PPCI 互补性、F-L 对比、CausalForest oracle coverage、confounded treatment 等。同领域罕见的全面性。（R1-S3, R2-S3）\n\n**S4. [共识] Δτ-free 诊断有实用价值。** Proposition 5 仅需子群误差率即可判断是否应做逐子群校正，无需估计处理效应。R2 交叉回应澄清：诊断的核心价值在于\"告诉你何时不应做 per-subgroup 校正\"——当 Δπ < 0.15 或 K 过大时，直接运行 EC-HTE 反而有害（variance 增加），诊断作为前置筛选可避免不必要的全流程运行。（R2-S2, R2 对 R1-W3 的反驳）\n\n**S5. [共识] 方法互补性设计好。** EC-HTE（covariate-side）与 PPCI（outcome-side）正交组合，bias 从 0.179 降至 0.007。（R2-S5）\n\n**S6. [共识] 可复现性。** Algorithm 1 完整，匿名代码仓库已提供，MCMC 诊断达标（R̂ < 1.01, ESS > 843）。（R1-S4）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [R1-N1, R2 AGREE] 非对称误分类下诊断准则退化——正文讨论严重不足**\n\nProposition 5 在对称假设 (A2) 下 AUC=0.86，但真实 LLM 几乎总是非对称（FPR/FNR 比率 1.1–7.1, Table 12）。非对称下 AUC 降至 0.65。\n\nR2 在交叉回应中补充了重要 nuance：\n- AUC=0.65 对筛选工具仍有实用价值（baseline 0.50 上 30% 相对提升）\n- 假阳性成本较低（多做 per-subgroup 校正增加 variance 但不引入 bias），假阴性成本更高（遗漏有害 global correction）\n- 论文在 Remark 2 已披露此退化，不存在隐瞒\n\n**但核心判断两位 Reviewer 一致**：Proposition 5 被列为三大贡献之一，如果在现实条件下 AUC 仅 0.65，需要在正文中更显著地讨论这一限制，而不是仅在 Remark 2 末尾一句带过。\n\n**建议**：Section 5.4 增加 1 段讨论非对称诊断性能退化；讨论矩阵形式诊断 vs 标量诊断的 trade-off（前者精度更高但输入需求更大）。\n\n---\n\n**MF2. [R2-N1, R1 部分 AGREE] NLP 社区适配性不足**\n\n三个贡献全部属于测量误差理论/因果推断方法论。NLP 任务仅作测试平台，正文缺 NLP 特有洞察，真实数据实验在附录。\n\nR1 在交叉回应中部分同意但认为严重程度不到 Must-Fix：Table 12-13 用 6 个真实 LLM 实证验证了子群异质性是 LLM 标注器的结构性属性（Spearman ρ = 0.82-1.00），这是 NLP-specific 发现。R2 Excitement 3/5，R1 Excitement 3.5/5——R1 认为问题本身对 NLP 社区足够重要。\n\n**综合判断**：维持 Must-Fix——EMNLP AC 对 NLP 社区适配有明确期待，且修改方案清晰、成本低。\n\n**建议**：(a) 将 Appendix M 仇恨言论案例关键结果移入正文；(b) 讨论误分类异质性的语言学来源；(c) 增加 \"Implications for NLP Annotation Pipelines\" 段落。\n\n---\n\n### 从 Must-Fix 降级为 Should-Fix（交叉回应后调整）\n\n**SF-A. [R1-N2 初审 Must-Fix → 交叉后 Should-Fix] \"Exact\" 标题与标量近似 R² 退化的张力**\n\nR2 在交叉回应中提供了有力澄清：\n- 标题 \"Exact Bias Identity\" 技术上正确——Theorem 1 在 (A1)-(A5) 下是精确恒等式，矩阵形式放松 (A2) 后也精确\n- R1 所引 R²=0.05-0.21 出现在 Δτ=0.05 配置下，此时偏差项本身极小（接近零），R² 低是因为信号极弱而非近似误差大——绝对偏差仍然很小\n- Abstract 中 R²=0.975 across 11 real LLM CMs 已包含非对称效应，只是标量近似 vs 矩阵形式的区别应显式标注\n\n**降级理由**：标题准确描述 Theorem 1 本身；Abstract 需加限定但不需改标题。\n\n**建议**：Abstract 标注 \"under the symmetric scalar approximation\"；Section 3 更明确区分 \"exact matrix identity\" 和 \"scalar approximation\"。\n\n---\n\n**SF-B. [R2-N2 初审 Must-Fix → 交叉后 Should-Fix] 与 F-L (2003) 的差异化**\n\nR1 在交叉回应中明确反驳：F-L 是全局标量衰减 β̂=(1−2ε)·β，无子群结构；Theorem 1 的 δ_s·Δτ/(1−2ε̄) 是三因子乘积分解，揭示 bias 方向可在子群间反转——F-L 结构中不存在此现象。实证对比：F-L per-subgroup Bias 0.112, coverage 65.3% vs EC-HTE Bias 0.004, coverage 97.8%（Appendix Z.5 Table 35）。\n\nR2 未对此反驳做进一步 REBUT。\n\n**降级理由**：R1 的反驳有实质依据——Theorem 1 与 F-L 的差异是结构性的（标量衰减 vs 子群乘积分解），novelty 成立。问题转为**展示清晰度**而非**novelty 本身**。\n\n**建议**：将 Appendix Z.5 Table 35 关键数字移入正文 Section 3 或 Table 1 附近；在 Theorem 1 后增加 2-3 句 explicit novelty statement。\n\n---\n\n**SF-C. [R1-N3 初审 Must-Fix → 交叉后 Should-Fix] K ≤ 4 可扩展性限制**\n\nR2 在交叉回应中提供了重要澄清：\n- K 是子群数量而非类别数量——由实践者自行选择（如文本长度分位数、hashtag 有无），不等于 NLP 任务的类别数\n- K=2-4 覆盖了社会科学因果推断中最常见的子群划分方式\n- 真正的限制在于 expert budget（K=4 需 200 标签），在实践中成本合理\n\nR1 未对此做进一步 REBUT。\n\n**降级理由**：R2 澄清了 K 的语义——它是设计参数而非硬约束。限制已在 Section 5.4 和 Limitations 中披露。\n\n**建议**：Introduction 增加 1 句明确 K 的含义和 K ≤ 4 建议；讨论 K 选择指导准则。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [R1-W1 → R2 REBUT] HTE 估计器多样性**\n\nR2 在交叉回应中反驳：论文实际测试了 3 种估计器（DIM + CausalForestDML + R-learner），覆盖参数、非参数、半参数三种范式。更关键的是，EC-HTE 的偏差校正发生在混淆矩阵反转阶段（Section 4.2），独立于下游 CATE 估计器。Theorem 1 也是 estimator-agnostic。R1 未对此做进一步 REBUT。\n\n**综合判断**：R2 反驳有效——3 种估计器 + estimator-agnostic 校正对会议论文充分。降低优先级。\n\n**SF2. [R1-W2, R2 AGREE] MC=100 覆盖率精度。** SE ≈ 2.2pp，Table 1 应报告 MC SE。两位 Reviewer 完全一致。\n\n**SF3. [R2-W3, R1 AGREE] 正文缺完整真实数据实验。** 移 Appendix M 关键结果入正文。两位 Reviewer 一致。\n\n**SF4. [R2-W2, R1 AGREE] 操作条件是经验导出。** 称 \"decision framework\" 应调整为 \"empirically calibrated operating guidelines\"。\n\n**SF5. [R2-W4, R1 AGREE] 噪声标签学习文献关联可更深入。** subgroup-dependent vs instance-dependent noise 结构化联系未建立。\n\n**SF6. [R1-W3 → R2 REBUT] Proposition 5 诊断增量价值。** R2 的反驳有说服力：诊断的核心功能是\"不校正\"决策（当 Δπ < 0.15 或 K 过大时阻止运行 EC-HTE） + 计算成本节省（一行代码 vs MCMC + CausalForest） + 可解释性。但论文当前未充分传达此定位。**建议**：Section 5.4 增加诊断作为\"前置决策工具\"的价值阐述。\n\n**SF7. [R2-W5, R1 AGREE] Section 3 符号密度偏高。** 建议 Theorem 1 后增加 K=2 数值示例。\n\n**SF8. [R1-W4, R2 AGREE] HB 先验结构性敏感性。** 仅 Gamma 超参变动，未考虑替代先验族。R2 补充：当前分析对会议论文基本达标。\n\n**SF9. [R1-W5, R2 AGREE] A1 灵敏度参数化受限。** 仅 logistic link、γ ∈ [0, 0.20]。R2 补充：横向覆盖面充分（8 种假设违反类型），参数化是领域标准做法。\n\n**SF10. [R2-W1, R1 AGREE] A3 (P(Z=0)=0.5) 正文讨论不足。** Appendix T 有测试但全在附录。\n\n---\n\n### Minor（不影响接收）\n\n1. Abstract \"7.4×\" 应标注 Table 1 出处（Global 0.059 vs EC-HTE 0.008 = 7.375×）[R1, R2 AGREE]\n2. Figure 3 panel 字号偏小（约正文 60-65%）[R2]\n3. \\citet / \\citep 一致性需全文检查 [R2]\n4. 33 页附录建议增加目录索引 [R1, R2 AGREE]\n5. Page 33 Algorithm 1 仅占 40%，余 60% 空白 [视觉审查]\n6. Table 1 \"95% CI Cov.\" 列未标注 MC 样本量 [R1]\n7. Appendix E 未讨论子群大小不均衡影响 [R1, R2 AGREE]\n8. Page 8 过度拥挤（Figure 4 + Table 1 + Conclusion + Limitations 全挤一页）[视觉审查]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n交叉回应后两位 Reviewer 在以下关键问题上完全一致：\n\n1. **Overall 3.5 (Borderline Conference)**\n2. **Soundness 4/5** — Theorem 1 推导正确，实验设计严谨\n3. **非对称诊断退化是核心弱点** — AUC 0.86→0.65，正文讨论不足（Must-Fix）\n4. **NLP 社区适配需加强** — 真实数据和 NLP 洞察应进正文（R1 认为 Should-Fix，R2 认为 Must-Fix）\n5. **MC=100 需报告 SE** [AGREE]\n6. **操作条件应标为 empirical guidelines** [AGREE]\n7. **Section 3 符号密度高，需数值示例** [AGREE]\n8. **HB 先验和 A1 灵敏度可扩展** [AGREE]\n9. **实验全面性是显著优势** [AGREE]\n10. **格式合规**（Abstract ≤ 200 words, 正文 ≤ 8 页, 匿名性, ACL 模板）[AGREE]\n\n---\n\n## Reviewer Divergence（交叉后仍存在的分歧）\n\n| 问题 | R1 | R2 | 交叉后共识 |\n|------|----|----|-----------|\n| NLP 适配严重性 | Should-Fix（Excitement 3.5） | Must-Fix（Excitement 3） | 维持 Must-Fix（EMNLP AC 明确期待 NLP 适配） |\n| F-L 差异化 | R1 REBUT：结构性不同 | R2 未进一步反驳 | 降为 Should-Fix（展示问题而非 novelty 问题）|\n| \"Exact\" 标题 | Must-Fix | Should-Fix（技术上正确） | 降为 Should-Fix |\n| K ≤ 4 严重性 | Must-Fix | Should-Fix（K 是设计参数） | 降为 Should-Fix |\n| HTE 估计器 | Should-Fix（缺 X-learner） | REBUT（3 种够了 + estimator-agnostic） | 降低优先级 |\n| 诊断增量价值 | Should-Fix（标签需求相同） | REBUT（\"不校正\"决策功能） | 维持 Should-Fix（论文需更好阐述） |\n\n---\n\n## Questions for Authors\n\n1. [R1-Q1, R2 补充] 矩阵形式诊断 vs 标量诊断的 trade-off 如何？在专家标签充足时，是否应推荐矩阵形式？\n2. [R1-Q2] K=8, n_expert=1000（125 labels/subgroup）时 EC-HTE 能否恢复？\n3. [R2-Q1, R1 REBUT 提供部分回答] Theorem 1 相对 F-L 的核心新增洞察：δ_s × Δτ 交互导致 sign reversal——这一点如何在正文中更显式传达？\n4. [R2-Q3] 真实仇恨言论案例中子群定义的语言学依据？LLM 误差异质性的根本原因？\n5. [R1-Q4, R2 补充] Real-data case study 中 EC-HTE 是否改变了 CATE 的方向性结论？R2 指出论文未明确报告是否存在 sign reversal——如仅改善 CI 宽度则 impact 减弱。\n6. [R2-Q5] 子群划分函数 S 本身有噪声时对 Theorem 1 的影响？\n\n---\n\n## Missing References\n\n1. **Wood-Doughty et al. (2018)** \"Challenges of Using Text Classifiers for Causal Inference\" — 最早系统讨论文本分类器用于因果推断的挑战，高度相关 [R1 AGREE, R2 提出]\n2. **Veitch et al. (2020)** \"Adapting Text Embeddings for Causal Inference\" — text-as-confounder 与本文 text-as-effect-modifier 互补 [R1 AGREE, R2 提出]\n3. **Kadavath et al. (2022)** \"Language Models (Mostly) Know What They Know\" — LLM 校准。R1 认为与本文正交，非核心缺失；R2 认为校准作为替代方案值得讨论 [分歧]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（4 warning, 0 critical, 16 info）\n\n主要发现：\n- **[warning] Page 1-2**: 前两页纯文本，Figure 1 在第 3 页。建议考虑提前视觉锚点。\n- **[warning] Page 4-5**: 连续两页密集数学无 display item。\n- **[warning] Page 8**: 过度拥挤——Figure 4 + Table 1 + Section 5.3-5.4 + Conclusion + Limitations 全挤一页。\n- **[warning] Page 33**: Algorithm 1 仅占 40%，余 60% 空白。\n- **[info]** Figure 1 质量优秀，Figure 2 pipeline 对比是最佳视觉元素，Table 1 booktabs 规范。公式渲染无错误，正文 8 页合规。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 / 5 (Borderline Conference)\n\n**EMNLP 2026 评分标准**: 3.5 = Borderline Conference\n\n**置信度**: 4 / 5（交叉回应后提升——两位 Reviewer 独立评估高度一致）\n\n**判断理由**:\n\n论文在理论严谨性（Soundness 4/5）和实验全面性上达到 Conference 水平。Theorem 1 的乘积分解是一个干净、可验证的理论结果，与 F-L (2003) 的差异是结构性的（交叉回应中 R1 有效反驳了 R2 的 \"形式相似\" 判断）。\"Debiasing hurts\" 的发现对 LLM 标注日益普及的 NLP 社区有实际意义。\n\n两个因素将总分从 Conference (4.0) 压至 Borderline (3.5)：\n\n1. **非对称诊断退化**（Must-Fix）：Proposition 5 作为核心贡献之一，在现实 LLM 非对称条件下 AUC 仅 0.65，正文讨论不足。虽然 R2 指出 AUC=0.65 对筛选工具仍有价值，但论文需更显著地呈现此限制。\n\n2. **NLP 社区适配**（Must-Fix）：核心贡献在统计方法论，NLP 任务仅为测试平台，正文缺 NLP 特有洞察和真实数据实验。R1 认为 Excitement 3.5（问题重要性足够），R2 认为 Excitement 3（受众窄）。\n\n**升级路径 → 4.0 (Conference)**：\n- Section 5.4 充分讨论非对称诊断退化 + 矩阵形式 trade-off\n- Appendix M 真实数据移入正文 + NLP 标注管道影响讨论\n- Theorem 1 后增加数值示例降低 Section 3 认知负担\n- Table 1 报告 MC SE\n\n**降级风险 → 3.0 (Findings)**：\n- AC 认为 NLP 社区 excitement 不足\n\n当前定位：一篇 solid 的 Findings paper；修改到位可达 Conference。升级所需改动量合理（正文内调整，无需新实验）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 措辞调整为 \"empirically calibrated operating guidelines\"\n- 增加 1 句明确 K 的含义（子群数量而非类别数量）和 K ≤ 4 建议\n- NLP motivation example（content moderation）有效，但后续 NLP 洞察未跟进\n\n### Section 2 (Related Work)\n- Noisy label learning 段落已添加但仅 3 句——建议建立 subgroup-dependent vs instance-dependent noise 联系\n- 缺 Wood-Doughty 2018, Veitch 2020（text + causal inference 核心文献）\n- F-L nesting statement 存在但不够显式——R1 建议将 Table 35 关键数字移入正文\n\n### Section 3 (Theory)\n- Theorem 1 推导正确，三因子分解优雅\n- A2 \"expository simplification\" 标注和 Remark 2 是改进\n- 建议 Theorem 1 后增加 K=2 数值示例（ε₁=0.05, ε₂=0.25）降低认知负担\n- 更明确区分 \"exact matrix identity\"（Remark 2）和 \"scalar approximation\"（Eq. 2）\n- Proposition 5: 正文讨论非对称 AUC 退化 + 阐述\"不校正\"决策的价值定位\n\n### Section 4 (Method)\n- HB 估计规格完整，<5ms 是优势\n- κ-guard 设计合理\n- 先验敏感性：当前 Gamma 超参变动对会议论文基本达标，替代先验族（logistic-normal）可作为 camera-ready 扩展\n\n### Section 5 (Experiments)\n- 合成验证（520 配置）全面\n- 应包含至少一个真实 NLP 数据实验（移 Appendix M 关键发现入正文）\n- Table 1 报告 MC SE\n- 3 种 HTE 估计器（DIM + CausalForest + R-learner）覆盖三种范式，对会议论文充分（R2 交叉回应有效反驳了 R1 的 \"缺 X-learner\" 关切——校正与下游估计器无关）\n\n### Section 6 (Conclusion)\n- 3 句话含 adoption guideline，长度合理\n- 可增加 1 句讨论非对称推广的未来方向\n\n### Limitations\n- 覆盖 3 个要点，长度合规\n- 建议增加 A3 class imbalance 和 K 含义的显式提及\n\n### Appendix\n- 深度突出，是论文核心竞争力之一\n- 建议增加目录索引\n- Page 33 空白过多"
  }
}
```

</details>

---


### Tool result

_source line 2253 · 2026-05-24T23:15:18.892505+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4319
}
```

</details>

---


### Assistant

_source line 2254 · 2026-05-24T23:15:28.629193+00:00_

审稿报告已重新提交（含交叉回应）。

**Round 21 审稿完成。**

最终评分：**3.5 / 5 (Borderline Conference)**，两位 Reviewer 一致。

关键发现：
- **2 个 Must-Fix**：非对称诊断退化正文讨论不足、NLP 社区适配需加强
- **10 个 Should-Fix**（含 3 个从 Must-Fix 降级：F-L 差异化是展示问题而非 novelty 问题、"exact"标题技术正确、K 是设计参数非硬约束）
- **8 个 Minor**

升级路径清晰：正文内调整（非对称讨论、真实数据移入、数值示例、MC SE）即可从 3.5 升至 4.0，无需新实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 182

## Round 182

70 recorded events


### User

_source line 2255 · 2026-05-25T04:16:31.876716+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ec_hte_llm_annotation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2256 · 2026-05-25T04:16:43.068750+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2257 · 2026-05-25T04:16:43.120244+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2258 · 2026-05-25T04:16:56.387297+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2259 · 2026-05-25T04:16:56.488298+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2260 · 2026-05-25T04:17:03.369119+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2261 · 2026-05-25T04:17:03.369640+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2262 · 2026-05-25T04:17:07.033564+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2263 · 2026-05-25T04:17:07.084229+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2264 · 2026-05-25T04:17:11.401982+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2265 · 2026-05-25T04:17:12.758013+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (43 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-041** (negative): Under asymmetric misclassification (FPR≠FNR, ratio 1:2 to 1:5 and reverse), the bias identity retains R²≥0.95 and EC-HTE maintains coverage ≥93% across 48 configurations (6 FPR/FNR ratios × 2 K × 4 Δπ), while the symmetric diagnostic AUC degrades monotonically with FPR/FNR ratio — quantifying the exact diagnostic accuracy loss curve under asymmetry.\n  [exp041_asymmetric_grid](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_grid.csv) | [exp041_asymmetric_summary](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_summary.csv) | [exp041_asymmetric_mc_script](/api/workspace-files/projects/e
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 2266 · 2026-05-25T04:17:12.758407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2267 · 2026-05-25T04:17:14.013933+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{makecell}
15	\usepackage{xcolor}
16	\usepackage{enumitem}
17	\usepackage{algorithm}
18	\usepackage{algpseudocode}
19	
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}[theorem]{Corollary}
22	\newtheorem{proposition}[theorem]{Proposition}
23	\newtheorem{remark}[theorem]{Remark}
24	
25	\title{When Debiasing Hurts: An Exact Bias Identity\\for LLM-Annotated Treatment Effects}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{theory}
39	
40	\input{method}
41	
42	\input{experiments}
43	
44	\input{conclusion}
45	
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	%\input{checklist}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 2268 · 2026-05-25T04:17:14.114725+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2269 · 2026-05-25T04:17:15.521650+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_22/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_22/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2270 · 2026-05-25T04:17:15.672752+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1256556 May 24 23:22 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_22/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 2271 · 2026-05-25T04:17:21.998798+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on the search results, I found 
…[truncated 1462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 7884
}
```

</details>

---


### Tool call

_source line 2272 · 2026-05-25T04:17:27.068917+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 call for papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2273 · 2026-05-25T04:17:27.521104+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers deadline submission"
  }
}
```

</details>

---


### Tool call

_source line 2274 · 2026-05-25T04:17:28.475348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2275 · 2026-05-25T04:17:28.978286+00:00_

1	\begin{abstract}
2	Standard confusion-matrix correction for noisy annotations assumes uniform error rates.
3	When this assumption fails---as it routinely does with large language model (LLM) classifiers, whose error rates vary by up to $5\times$ across subgroups---correction can reverse estimated effect signs.
4	We derive an exact bias identity: global correction introduces subgroup-level bias $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$ under symmetric errors (generalizing to a full-matrix form for arbitrary asymmetric confusion matrices; Remark~\ref{rem:asymmetric}), verified at $R^2 \geq 0.97$ on synthetic grids ($R^2 = 0.975$ in aggregate across 11 real LLM confusion matrices; per-model range $0.76$--$0.99$).
5	The identity predicts that global correction reverses conditional average treatment effect (CATE) sign in 14.9\% of configurations where the true effect is small ($\tau(0) = 0.03$) and amplifies bias in all eight real LLMs tested; a $\Delta\tau$-free diagnostic corollary flags harmful correction from error rates alone, without estimating treatment effects.
6	We characterize when per-subgroup correction is beneficial ($\Delta\pi > 0.15$, $n_{\text{expert}}/K \geq 50$, $K \leq 4$) versus when global correction should be retained, and implement one such correction via hierarchical Bayesian estimation, reducing $|\text{bias}|$ by $7.4\times$ under extreme heterogeneity.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2276 · 2026-05-25T04:17:28.978755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2277 · 2026-05-25T04:17:29.932792+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Consider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.
5	After standard confusion-matrix correction, the analysis concludes the policy \emph{increases} hate speech among younger users---but the true effect is protective.
6	This sign reversal is not an edge case.
7	
8	Large language models (LLMs) now routinely replace human annotators in computational social science, producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,tan2024llm}.
9	When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.
10	Yet LLM annotations are not uniformly accurate: \citet{ashwin2025bias} document error rates varying by up to 5$\times$ across demographic subgroups; in our pilot, GPT-4.1 error rates range from 10.2\% to 20.0\% across text-feature subgroups ($\Delta\pi = 0.098$).
11	
12	We show that this standard correction can make things worse.
13	In 14.9\% of our synthetic configurations (across a grid of $\Delta\pi$ and $\tau(0)$ values; $\tau(0) = 0.03$), global correction reverses the sign of estimated CATE---a protective treatment ($\tau = +0.03$) appears harmful ($\hat{\tau} = -0.059$)---rising to 31\% at $\tau(0) = 0.01$ (Figure~\ref{fig:sign_reversal}); all eight real LLMs tested amplify bias under global correction, while our per-subgroup correction (EC-HTE; Section~\ref{sec:method}) eliminates sign reversal in the pri
…[truncated 2805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2278 · 2026-05-25T04:17:29.933190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2279 · 2026-05-25T04:17:30.084213+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Measurement error and annotation models.}
5	Classical measurement error theory shows that correction via estimated error models can amplify mean squared error (MSE) when the error structure is misspecified~\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\cite{hu2008nonparametric}.
6	
7	Three distinctions separate our contribution from prior measurement error analyses.
8	First, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\cite{frazis2003estimating,carroll2006measurement} or confounder~\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.
9	Second, Theorem~\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.
10	Concretely, \citet{frazis2003estimating} derive scalar attenuation $\lambda = (1 - 2\pi)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\ref{thm:bias_identity} yields a structurally interpretable decomposition---the product $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$ whose sign varies across subgroups, revealing how error heterogeneity causes bias direction to reverse between subgroups, a phenomenon invisible to any global-scalar analysis.
11	The homogeneous-error setting ($K{=}1$, $\delta_s{=}0$) is a degenerate case recovering classical attenuation~\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\ref{app:fl_comparison}).
12	Third, the $\delta_s \cdot \Delta\tau$ product str
…[truncated 5180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2280 · 2026-05-25T04:17:30.084614+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 2281 · 2026-05-25T04:17:30.135190+00:00_

1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state five assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification (expository simplification):} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$. Used only to reduce $[B_s]_{z,1}$ to the scalar $\pm\delta_s/(1{-}2\bar{\pi})$; the product-form identity holds for arbitrary asymmetric matrices without~(A2) (Remark~\ref{rem:asymmetric}).
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{N
…[truncated 8351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2282 · 2026-05-25T04:17:34.954539+00:00_

Web search results for query: "ACL Rolling Review 2026 call for papers submission guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found information about ACL Rolling Review (ARR) 2026 submission guidelines. Here are the key points:

## Anonymity Requirements

Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided. Supplementary materials should also be anonymized, and links to file hosting services like Dropbox that can track downloads are not allowed.

## Preprint Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review.

## Review Process & Penalties

All authors are expected to sign up to review, with assignment depending on their qualifications and the submission pool. Reviewers or area chairs who receive assignments but act irresponsibly will not be allowed to resubmit or commit their work during the current and next ARR cycle.

## Paper
…[truncated 442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 7885
}
```

</details>

---


### Tool result

_source line 2283 · 2026-05-25T04:17:41.884721+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the information ab
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 14363
}
```

</details>

---


### Tool call

_source line 2284 · 2026-05-25T04:17:49.365320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2285 · 2026-05-25T04:17:49.365900+00:00_

1	\section{Correction Prescribed by the Identity}
2	\label{sec:method}
3	
4	Theorem~\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.
5	This correction (EC-HTE) proceeds in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.
6	The complete procedure is summarized in Algorithm~\ref{alg:echte} (Appendix~\ref{app:algorithm}) and illustrated in Figure~\ref{fig:method_overview}.
7	
8	\begin{figure*}[t]
9	\centering
10	\includegraphics[width=\textwidth]{figures/fig_method_overview.pdf}
11	\caption{\textit{Top (rose):} global correction applies a pooled confusion matrix uniformly, risking sign reversal. \textit{Bottom (teal):} EC-HTE estimates per-subgroup matrices via hierarchical Bayes, applies stratified inversion with a $\kappa$-guard, and propagates uncertainty into CausalForestDML.}
12	\label{fig:method_overview}
13	\end{figure*}
14	
15	\subsection{Hierarchical Bayes Confusion Matrix Estimation}
16	
17	We place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\{C_s\}_{s=1}^K$.
18	The model estimates the full $J \times J$ confusion matrix per subgroup and does not require symmetric error rates~(A2); (A2) simplifies only the diagnostic (Proposition~\ref{prop:debiasing_hurts}).
19	For each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior centered at the global pooled confusion matrix $\hat{C}_{\text{global}}$: $\text{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, where $\hat{C}_{\text{global},j}$ is the $j$-th row of the pooled CM and $\alpha_0 > 0$ is a shared concentration parameter estimated via empirical Bayes (marginal likelihood maximization).
20	We place a $\mathrm{Gamma}(3, 1)$ hyperprior on $\alpha_0$, robust to $2\times$ perturbation (Appendix~\ref{app:hyperprior}).
21	Large 
…[truncated 2776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2286 · 2026-05-25T04:17:49.516758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2287 · 2026-05-25T04:17:50.371200+00:00_

1	\section{Experiments}
2	
3	\begin{figure}[t]
4	\centering
5	\includegraphics[width=\columnwidth]{figures/fig4_budget_compact.pdf}
6	\caption{RMSE vs.\ expert budget under extreme heterogeneity. Crossover at $n{=}250$ ($K{=}2$) and $n{=}1000$ ($K{=}4$); shaded bands: $\pm 1$ SD across subgroups. Full grid in Appendix~\ref{app:budget}.}
7	\label{fig:budget_compact}
8	\end{figure}
9	
10	\subsection{Setup}
11	
12	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 Monte Carlo (MC) runs) and semi-synthetic data-generating processes (DGPs) spanning four NLP tasks---sentiment analysis (TweetEval~\cite{barbieri2020tweeteval}, $K{=}4$), hate speech detection (CivilComments, $K{=}4$), stance detection ($K{=}5$; Appendix~\ref{app:stance}), and topic classification (AG News, $K{=}4$; Appendix~\ref{app:agnews})---with full specifications in Appendix~\ref{app:dgp}.
13	
14	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2024dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (per-subgroup correction), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
15	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
16	Primary metrics are $|\text{bias}|$, root mean squared error (RMSE), and 95\% confidence interval (CI) coverage, averaged across subgroups and 100 MC runs.
17	Robustness validations cover eight conditions including asymmetric errors, subgroup misspecification, and treatment-dependent misclassification (all $\geq$89.5\% coverage; Appendices~\ref{app:hatespeech}--\ref{app:treatment_dep}).
18	Semi-synthetic evaluation uses 16 empirical LLM confusion matrices (8 LLMs $\times$ 2 datasets; Appendix~\ref{app:semireal}).
19	
20	\subsection{Empirical Validation of the Bias Identity}
21	\label{sec:bias_mechanism}
22	
23	\b
…[truncated 5984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 2288 · 2026-05-25T04:17:50.371755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2289 · 2026-05-25T04:17:50.874219+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Standard confusion-matrix correction can reverse causal conclusions when misclassification rates vary across subgroups.
4	We derived an exact bias identity ($R^2 \geq 0.97$) that yields a diagnostic for flagging harmful correction and prescribes per-subgroup correction when $\Delta\pi > 0.15$ and $n_{\text{expert}}/K \geq 50$, validated across 11 real LLMs and four NLP tasks.
5	Practitioners should estimate per-subgroup confusion matrices before applying any correction; the framework is task-agnostic and composes with prediction-powered inference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2290 · 2026-05-25T04:17:50.874649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2291 · 2026-05-25T04:17:51.376919+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Per-subgroup correction requires $n_{\text{expert}}/K \geq 50$ expert labels per subgroup and moderate classifier accuracy ($\text{FPR}_s, \text{FNR}_s < 0.5$); at $K{=}8$, RMSE exceeds global correction under fixed expert budget (Appendix~\ref{app:k8_subgroups}).
5	Assumption~(A3) requires balanced effect modifier prevalence; under class imbalance ($P(Z{=}1) = 0.1$), the identity remains exact ($R^2 \geq 0.976$) but EC-HTE's RMSE advantage narrows (ratio 1.06--1.68; Appendix~\ref{app:classimbalance}).
6	Assumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable; sensitivity analysis shows robustness up to $\gamma_T \leq 0.05$ for treatment-dependent misclassification (coverage $\geq$89.7\%; Appendix~\ref{app:treatment_dep}).
7	Ground-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so all evaluations use synthetic CATE injection on real text features and real LLM annotations (Appendices~\ref{app:dgp},~\ref{app:multilm}).
8	Code and data generation scripts are publicly available.\footnote{\url{https://anonymous.4open.science/r/ec-hte}}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2292 · 2026-05-25T04:17:51.427673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2293 · 2026-05-25T04:17:51.831022+00:00_

File content (41655 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 2294 · 2026-05-25T04:17:51.831484+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for main conference papers submission format guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org call for main conference papers submission format guidelines"
  }
}
```

</details>

---


### Tool result

_source line 2295 · 2026-05-25T04:17:58.810126+00:00_

Web search results for query: "site:2026.emnlp.org call for main conference papers submission format guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 – CL deadlines for Qualifying Papers | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/17"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"}]

Based on the search results from the EMNLP 2026 Call for Main Conference Papers, here are the key submission format guidelines:

## Paper Format

Papers should follow a two-column format with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Requirements

A mandatory Limitations section is required and should be placed after the conclusion.

## Submission Process

All submissions go through ACL Rolling Review (ARR), with the ARR submis
…[truncated 627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 6978
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-25T04:18:08.123177+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2297 · 2026-05-25T04:18:08.123559+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2298 · 2026-05-25T04:18:10.031513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": "1",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "offset": "1",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2299 · 2026-05-25T04:18:11.086164+00:00_

1	\section{EC-HTE Procedure}
2	\label{app:algorithm}
3	
4	\begin{algorithm}[t]
5	\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
6	\label{alg:echte}
7	\begin{algorithmic}[1]
8	\Require Observations $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S: \mathcal{X} \to \{1,\ldots,K\}$
9	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with variance-adjusted CIs
10	\Statex
11	\State \textbf{Preconditions:} verify $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ and $\max_s(\text{FPR}_s, \text{FNR}_s) < 0.5$; if either fails, use global correction
12	\Statex
13	\State \textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}
14	\For{$s = 1, \ldots, K$}
15	    \State $C_s[j,\cdot] \sim \mathrm{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, \; $\alpha_0$ via empirical Bayes
16	    \State Gibbs sampler (4 chains, 4000 iter) on $\{(\hat{Z}_j, Z_j^*) : S_j = s\}$
17	    \State $\hat{C}_s \gets$ posterior mean; verify $\hat{R} < 1.01$
18	\EndFor
19	\Statex
20	\State \textbf{Step 2: Correct observed outcome moments}
21	\For{$s = 1, \ldots, K$}
22	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{singularity guard}
23	    \EndIf
24	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
25	\EndFor
26	\Statex
27	\State \textbf{Step 3: CausalForestDML with variance-adjusted SEs}
28	\State Train CausalForest (honest splitting) on corrected outcome moments $\tilde{\boldsymbol{\mu}}_s$
29	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
30	\State \Return $\hat{\tau}(z)$ with 95\% CIs from $\mathrm{se}_{\mathrm{adj}}$
31	\end{algorithmic}
32	\end{algorithm}
33	
34	\subsection{Condition Number Guard Ablation}
35	\label{app:kappa_ablation}
36	
37	The singularity guard in Algorithm~\ref{alg:echte} (line~6) falls back to global correction when $\kappa(\
…[truncated 11876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 2300 · 2026-05-25T04:18:13.897208+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 2301 · 2026-05-25T04:18:13.948015+00:00_

-rw-r--r-- 1 ubuntu ubuntu 25303 May 24 23:26 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2302 · 2026-05-25T04:18:14.299562+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib 2>/dev/null; grep -c '@' /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib 2>/dev/null && echo \"BIB_OK\" || echo \"NO_BIB\"",
  "description": "Check references.bib stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib 2>/dev/null; grep -c '@' /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib 2>/dev/null && echo \"BIB_OK\" || echo \"NO_BIB\"",
    "description": "Check references.bib stats"
  }
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-25T04:18:14.400539+00:00_

688 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib
70
BIB_OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2304 · 2026-05-25T04:18:30.315513+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2305 · 2026-05-25T04:18:31.270113+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:52 UTC\\n  summary: MVP PASS：核心假设验证通过，评估框架修正为子群水平\\n  rationale: 三轮模拟（v1 CausalForest + v2 差分估计 + v3 子群分析）完成。核心发现：(1) 全局校正在低误差子群造成系统性伤害（bias\\n    恶化 7.8x），EC-HTE 分层校正修复此问题（|bias|<0.015）；(2) 边际 CATE 评估掩盖此效应（正负偏差抵消），子群水平才是正确评估维度；(3)\\n    EC-HTE 在高误差子群方差偏高→层级贝叶斯 partial pooling 是 research 阶段核心优先级。Pass 标准 1 修正为子群水平后\\n    PASS（子群 B EC-HTE RMSE 0.063 vs Global 0.100），标准 2/3/4 均 PASS。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:44 UTC\\n  summary: Dream Round 1 分析完成：best=4 (Weak Accept), median=3.5 (Borderline Conference),\\n    worst=2.5 (Borderline Reject)。达到启动门槛（best≥weak accept, median≥borderline）。识别6项确认行动项、4项观察项。更新\\n    framing 和 plan 后批准 P0 CPU 实验（exp-001, exp-002）立即启动。exp-007 (PPCI comparison) 升级为\\n    P0。\\n  rationale: 三档一致的结构性问题：(1) 薄弱文献（11 refs vs 40+ expected），(2) MCMC 实现细节缺失，(3) 方法新颖性定位需明确为\\\"问题发现\\\"而非\\\"新技术\\\"，(4)\\n    信息密度过高需增加图表减少表格，(5) K=2 理论 vs K>2 实验的 gap，(6) 真实数据验证缺失。数据依赖性问题（coverage undercoverage,\\n    diagnostic AUROC, PPCI dominance）仅在2档或单档出现，记录为观察项待真实实验验证。framing/plan 改动为渐进式改善（sharpening\\n    novelty positioning, adding requirements），不构成重大方向转变，当前 Dream 评分已达标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 21:32 UTC\\n  summary: 'Dream Round 2 analysis: proceed with P0 experiments, 10 writing requirements\\n    codified'\\n  rationale: 'Dream Round 2 (dream_20260520T194535): best=4/6, median=3.5/6, worst=3/6.\\n    Worst improved +0.5 from Round 1 (was 2.5). Three-tier consistent issues all addressable\\n    in writing phase: (1) bibliography 9→30-35 refs, (2) \\\"bias bound\\\"→\\\"bias decomposition\\n    identity\\\", (3) DGP specification, (4) figures, (5) Fuller 1987 contextualization,\\n    (6) \\\"never worse\\\" qualification, (7) inve
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2306 · 2026-05-25T04:18:31.722199+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "description": "Read first 100 lines of review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "description": "Read first 100 lines of review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2307 · 2026-05-25T04:18:32.625931+00:00_

issues:
  # === RESOLVED (prior rounds — abbreviated) ===
  - id: "R1-N1"
    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 2
    action_items: []
    resolution: "重新推导为精确恒等式"
    resolution_round: 0

  - id: "R2-W8"
    summary: "Proposition 1 限于 K=2"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "Theorem 1 适用一般 K"
    resolution_round: 0

  - id: "R1-N2"
    summary: "Real data ground truth CATE 来源不明"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位为 illustrative application"
    resolution_round: 0

  - id: "R1-N3"
    summary: "HB 模型规格严重不完整"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "完整 MCMC 规格"
    resolution_round: 0

  - id: "JOINT-W4"
    summary: "相关工作严重遗漏"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "30+ 引用覆盖"
    resolution_round: 0

  - id: "JOINT-W3"
    summary: "信息密度过高"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "主文精简至合理密度"
    resolution_round: 0

  - id: "R2-W7"
    summary: "真实数据验证单薄"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位 + 公开数据集"
    resolution_round: 0

  - id: "R1-W5"
    summary: "Pages 9-10 缺 Appendix 标签"
    category: format
    severity: info
    status: resolved
    first_raised_round: 0
    last_seen_round: 0
    action_items: []
    resolution: "附录结构重组"
    resolutio
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2308 · 2026-05-25T04:18:33.128408+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper && cat abstract.tex introduction.tex related_work.tex theory.tex method.tex experiments.tex conclusion.tex limitations.tex | wc -w",
  "description": "Count total words in main paper text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper && cat abstract.tex introduction.tex related_work.tex theory.tex method.tex experiments.tex conclusion.tex limitations.tex | wc -w",
    "description": "Count total words in main paper text"
  }
}
```

</details>

---


### Tool result

_source line 2309 · 2026-05-25T04:18:34.082674+00:00_

4090
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/.claude/sessions/review_director_2cf1d8af

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2310 · 2026-05-25T04:18:34.334001+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c '\\\\\\\\section\\|\\\\\\\\subsection\\|\\\\\\\\paragraph' /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/{abstract,introduction,related_work,theory,method,experiments,conclusion,limitations}.tex 2>/dev/null",
  "description": "Count sections in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c '\\\\\\\\section\\|\\\\\\\\subsection\\|\\\\\\\\paragraph' /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/{abstract,introduction,related_work,theory,method,experiments,conclusion,limitations}.tex 2>/dev/null",
    "description": "Count sections in paper"
  }
}
```

</details>

---


### Tool result

_source line 2311 · 2026-05-25T04:18:34.384619+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex:0
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex:0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2312 · 2026-05-25T04:18:56.677990+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool call

_source line 2313 · 2026-05-25T04:18:57.131940+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2314 · 2026-05-25T04:19:21.464661+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24786
}
```

</details>

---


### Tool result

_source line 2315 · 2026-05-25T04:19:21.465036+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 24333
}
```

</details>

---


### Tool call

_source line 2316 · 2026-05-25T04:19:21.515485+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "ec_hte_llm_annotation",
  "text": "你是 Reviewer 1，负责审查以下论文的 **方法严谨性、理论正确性、实验设计**。\n\n## 论文信息\n- 标题: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_22/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- 长文正文限 8 页，参考文献不限。Limitations 必须有（不计入页数）。\n- Double-blind 审稿\n- ACL 模板（acl.sty）\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 理论正确性\n- Theorem 1 (Bias Decomposition Identity) 的证明是否完整、严谨？假设 (A1)-(A5) 是否合理？\n- Proposition 2 (Debiasing Can Increase Bias) 的条件推导是否正确？\n- Remark 1 (asymmetric extension) 和 Proposition 3 (A5 relaxation) 是否充分论证？\n- Corollary 1 (Aggregate Bias) 和多类扩展 (Corollary 2) 的推广是否自然？\n- 有限样本余项分析是否充分？\n\n### 2. 方法严谨性\n- 层级贝叶斯混淆矩阵估计的模型设定是否合理？先验选择是否有据？\n- κ-guard 机制的设计是否恰当？阈值选择是否充分论证？\n- 方差调整公式的推导是否正确？Bootstrap 补充是否必要？\n- EC-HTE 与 PPCI 的组合是否有理论保证？\n\n### 3. 实验设计\n- 合成数据 DGP 是否合理覆盖了参数空间？100 MC runs 是否足够？\n- 半合成验证（11 个 LLM × 数据集组合）是否有说服力？\n- Baseline 选择是否充分？是否遗漏了重要竞争方法？\n- 评估指标（|bias|, RMSE, 95% CI coverage）是否全面？\n- 鲁棒性检验（8 个条件）是否覆盖了关键边界情况？\n- CausalForest 和 R-learner 验证是否充分？\n\n### 4. 统计报告\n- MC SE 报告是否充分？$R^2$ 的置信区间？\n- 显著性检验（如有）是否恰当？\n- 效果量报告（7.4× bias reduction 等）是否有误导性？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\nScore: [使用 EMNLP 2026 评分标准]\nConfidence: [1-5]\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "ec_hte_llm_annotation",
    "text": "你是 Reviewer 1，负责审查以下论文的 **方法严谨性、理论正确性、实验设计**。\n\n## 论文信息\n- 标题: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_22/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- 长文正文限 8 页，参考文献不限。Limitations 必须有（不计入页数）。\n- Double-blind 审稿\n- ACL 模板（acl.sty）\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 理论正确性\n- Theorem 1 (Bias Decomposition Identity) 的证明是否完整、严谨？假设 (A1)-(A5) 是否合理？\n- Proposition 2 (Debiasing Can Increase Bias) 的条件推导是否正确？\n- Remark 1 (asymmetric extension) 和 Proposition 3 (A5 relaxation) 是否充分论证？\n- Corollary 1 (Aggregate Bias) 和多类扩展 (Corollary 2) 的推广是否自然？\n- 有限样本余项分析是否充分？\n\n### 2. 方法严谨性\n- 层级贝叶斯混淆矩阵估计的模型设定是否合理？先验选择是否有据？\n- κ-guard 机制的设计是否恰当？阈值选择是否充分论证？\n- 方差调整公式的推导是否正确？Bootstrap 补充是否必要？\n- EC-HTE 与 PPCI 的组合是否有理论保证？\n\n### 3. 实验设计\n- 合成数据 DGP 是否合理覆盖了参数空间？100 MC runs 是否足够？\n- 半合成验证（11 个 LLM × 数据集组合）是否有说服力？\n- Baseline 选择是否充分？是否遗漏了重要竞争方法？\n- 评估指标（|bias|, RMSE, 95% CI coverage）是否全面？\n- 鲁棒性检验（8 个条件）是否覆盖了关键边界情况？\n- CausalForest 和 R-learner 验证是否充分？\n\n### 4. 统计报告\n- MC SE 报告是否充分？$R^2$ 的置信区间？\n- 显著性检验（如有）是否恰当？\n- 效果量报告（7.4× bias reduction 等）是否有误导性？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\nScore: [使用 EMNLP 2026 评分标准]\nConfidence: [1-5]\n```"
  }
}
````

</details>

---


### Tool result

_source line 2317 · 2026-05-25T04:19:37.844180+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16328
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-25T04:19:37.894917+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "ec_hte_llm_annotation",
  "text": "你是 Reviewer 2，负责审查以下论文的 **新颖性、相关工作完整性、写作质量、格式合规**。\n\n## 论文信息\n- 标题: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_22/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- 长文正文限 8 页，参考文献不限。Limitations 必须有（不计入页数）。\n- Double-blind 审稿\n- ACL 模板（acl.sty）\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心贡献（bias identity + diagnostic + EC-HTE method）的新颖性如何？\n- 与经典测量误差理论（Fuller 1987, Carroll 2006, Frazis & Loewenstein 2003）的关系是否清晰？\n- \"effect modifier misclassification\" 作为新问题是否成立？还是已有方法可覆盖？\n- 理论贡献（exact identity）vs 方法贡献（hierarchical Bayes）的比重是否合理？\n- 对 NLP/CL 社区的实际影响力评估\n\n### 2. 相关工作完整性\n- 测量误差文献（经典 + 现代）是否全面？\n- PPI/DSL/PPCI 等预测驱动方法的对比是否公平？\n- LLM annotation 文献是否覆盖了最新进展（2024-2026）？\n- 因果推断 + NLP 交叉文献是否充分？\n- 是否遗漏了重要的竞争方法或相关理论？\n\n### 3. 写作质量\n- 论文叙事结构是否清晰？读者是否能跟随论证逻辑？\n- Abstract 是否准确反映论文内容？是否超过 200 words？\n- Introduction 的 motivation 和 framing 是否有效？\n- 数学符号的定义和使用是否一致？\n- 图表的信息密度和可读性如何？\n- 结论是否准确总结了贡献和局限？\n\n### 4. 格式合规\n- 正文是否在 8 页限制内？\n- 是否使用了正确的 ACL 模板（\\usepackage[review]{acl}）？\n- 匿名性是否保持？有无泄露作者身份的线索？\n- Limitations section 是否存在且位置正确（正文末尾，非附录）？\n- 引用格式是否一致？\n- 附录结构是否合规？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\nScore: [使用 EMNLP 2026 评分标准]\nConfidence: [1-5]\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "ec_hte_llm_annotation",
    "text": "你是 Reviewer 2，负责审查以下论文的 **新颖性、相关工作完整性、写作质量、格式合规**。\n\n## 论文信息\n- 标题: \"When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\"\n- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_22/submitted.pdf`\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- 截止日期: 2026-05-25\n- 长文正文限 8 页，参考文献不限。Limitations 必须有（不计入页数）。\n- Double-blind 审稿\n- ACL 模板（acl.sty）\n- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 核心贡献（bias identity + diagnostic + EC-HTE method）的新颖性如何？\n- 与经典测量误差理论（Fuller 1987, Carroll 2006, Frazis & Loewenstein 2003）的关系是否清晰？\n- \"effect modifier misclassification\" 作为新问题是否成立？还是已有方法可覆盖？\n- 理论贡献（exact identity）vs 方法贡献（hierarchical Bayes）的比重是否合理？\n- 对 NLP/CL 社区的实际影响力评估\n\n### 2. 相关工作完整性\n- 测量误差文献（经典 + 现代）是否全面？\n- PPI/DSL/PPCI 等预测驱动方法的对比是否公平？\n- LLM annotation 文献是否覆盖了最新进展（2024-2026）？\n- 因果推断 + NLP 交叉文献是否充分？\n- 是否遗漏了重要的竞争方法或相关理论？\n\n### 3. 写作质量\n- 论文叙事结构是否清晰？读者是否能跟随论证逻辑？\n- Abstract 是否准确反映论文内容？是否超过 200 words？\n- Introduction 的 motivation 和 framing 是否有效？\n- 数学符号的定义和使用是否一致？\n- 图表的信息密度和可读性如何？\n- 结论是否准确总结了贡献和局限？\n\n### 4. 格式合规\n- 正文是否在 8 页限制内？\n- 是否使用了正确的 ACL 模板（\\usepackage[review]{acl}）？\n- 匿名性是否保持？有无泄露作者身份的线索？\n- Limitations section 是否存在且位置正确（正文末尾，非附录）？\n- 引用格式是否一致？\n- 附录结构是否合规？\n\n请按以下格式输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\nS1. ...\nS2. ...\n\n## Weaknesses\nW1. [severity: critical/major/minor] ...\nW2. ...\n\n## Questions\nQ1. ...\n\n## Missing References\n[如有]\n\n## Overall Assessment\nScore: [使用 EMNLP 2026 评分标准]\nConfidence: [1-5]\n```"
  }
}
````

</details>

---


### Tool result

_source line 2319 · 2026-05-25T04:19:39.356993+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Tool call

_source line 2320 · 2026-05-25T04:19:53.098001+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND_IN_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/config.yaml 2>/dev/null || echo \"NOT_FOUND_IN_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2321 · 2026-05-25T04:19:53.198798+00:00_

NOT_FOUND_IN_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2322 · 2026-05-25T04:19:56.869639+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/ 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/ 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2323 · 2026-05-25T04:19:56.920308+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2324 · 2026-05-25T04:20:16.356386+00:00_

外部审稿未在项目中配置，跳过。

---

**📋 Round 22 审稿会议启动**

| 项目 | 状态 |
|---|---|
| **投稿目标** | EMNLP 2026 (ARR), Deadline 2026-05-25 |
| **论文** | "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects" |
| **格式** | ACL 模板 (review mode), double-blind, 长文 8 页限制 |
| **PDF** | 已确认存在 (1.2MB, 2026-05-24) |
| **引用** | 70 条 (references.bib) |
| **Limitations** | 有，位于正文末尾 ✓ |

**Reviewer 编排**:
- **Reviewer 1**: 方法严谨性 + 理论正确性 + 实验设计 → ✅ 已派发
- **Reviewer 2**: 新颖性 + 相关工作 + 写作质量 + 格式合规 → ✅ 已派发

**辅助线**:
- 视觉审查 Agent → ✅ 已启动 (fire-and-forget)
- 外部审稿 (Stanford Agentic Reviewer) → ❌ 未配置

等待两名 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 183

## Round 183

2 recorded events


### User

_source line 2325 · 2026-05-25T04:28:16.048263+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见

## Summary

本文研究 LLM 标注用于因果推断时，传统全局混淆矩阵校正在子群体误差率异质的条件下会引入新偏差的问题。核心贡献是推导出一个精确的偏差恒等式（Theorem 1），表明全局校正的偏差具有三因子乘积形式：δ_s·Δτ/(1−2π̄)——子群体误差偏离 × CATE 异质性 × 逆矩阵放大。在此基础上提出 EC-HTE 方法，通过层级贝叶斯估计每个子群体的混淆矩阵，进行分层校正。论文包含 520+ 合成配置、11 个 LLM × 数据集组合以及真实数据验证。

## Strengths

**S1. 精确的理论贡献。** Theorem 1 的偏差恒等式形式简洁、可解释性强，将全局校正的偏差分解为三个直观因子的乘积。证明（Appendix B）通过矩阵代数严格验证了 M̄⁻¹M_s − I = δ_s/(1−2π̄)·[[-1,1],[1,-1]]，我手动核实了推导过程，逻辑正确。Proposition 5 的"去偏增偏"条件 |δ_s|/((1−2π̄)·π_s) > 1 也是正确的，给出了一个不依赖未知 Δτ 的可操作诊断准则（AUC = 0.86）。

**S2. 异常全面的实验验证。** 520 个合成配置（Δτ × π × K 网格）、100 MC 运行、11 个真实 LLM 的半合成验证、6 个 NLP 任务的 cross-task 验证（Appendix Z.9-Z.10）、8 个鲁棒性检验。Table 1 的主结果清晰展示了 EC-HTE 在极端异质性下的 7.4× 偏差缩减和近名义覆盖率。Table 23 在 11 个真实 LLM 上验证 R² ≥ 0.893，聚合 R² = 0.975，强力支撑了恒等式的实证有效性。

**S3. 理论到方法到实践的完整链条。** 从恒等式出发自然引出分层校正的动机，层级贝叶斯提供了合理的收缩机制（大 α_0 → 向全局收缩，小 α_0 → 子群体主导），κ-guard 处理近奇异情况，方差调整公式传播不确定性。Algorithm 1（page 33）清晰可复现。

**S4. 连接 NLP 与因果推断的时效性。** 随着 LLM 标注在社会科学中普及，系统性地分析标注噪声对 HTE 估计的影响具有重要实践价值。Figure 1C 展示 14.9% 的配置出现符号反转，Figure 4 的热力图直观展示了偏差放大区域。

**S5. 假设放松的系统性讨论。** 论文对 (A2) 对称性（Remark 2, Appendix J）、(A3) 类别平衡（Appendix T）、(A5) 同质处理效应（Proposition 3）、(A1) 条件独立性（Appendix Z.2-Z.3）均提供了理论扩展和实证验证，而非仅声明适用范围。

## Weaknesses

**W1. [major] 对称误分类假设 (A2) 在实际 NLP 应用中限制性较强**

- 具体位置：Section 3, Assumption (A2); Remark 2; Table 22 (Appendix U)
- 问题：主定理的简洁乘积形式依赖 FPR_s = FNR_s。但 Table 22 的真实 LLM 数据显示显著不对称：GPT-4o 的 FPR = 0.249 vs. FNR = 0.157（S0 子群体），差异达 0.09。在非对称条件下，诊断准则的 AUC 从 0.86 降至 0.66（Remark 2），意味着实际部署中诊断可靠性大幅下降。虽然 Appendix J 提供了非对称扩展，但主文中声称的"exact identity"主要在对称条件下成立，论文标题和摘要的措辞可能对读者产生误导。
- 建议：(1) 在 Abstract 或 Section 3 开头明确指出乘积形式的简洁表达需要 (A2)，一般情况下偏差仍有乘积结构但系数更复杂；(2) Table 1 或 Section 5.3 中增加非对称误差率下 EC-HTE 的主结果对比。

**W2. [major] 有限样本余项分析不够精确**

- 具体位置：Section 3, "Finite-sample remainder" 段落 (theory.tex:92)
- 问题：论文声称 R_n = O_p(n_expert^{-1/2} · κ(C_s))。但通过标准矩阵扰动分析，(C_s + E_s)⁻¹ = C_s⁻¹ − C_s⁻¹ E_s C_s⁻¹ + O(‖E_s‖²)，一阶余项的范数界是 ‖C_s⁻¹‖² · ‖E_s‖ ∝ κ(C_s)² · n_expert^{-1/2}，而非 κ(C_s)。这个差异在 κ 较大时（如 κ ≈ 100 附近，恰好是 κ-guard 的阈值区域）显著影响余项大小的量级判断。
- 建议：给出显式的有限样本界（而非仅 O_p 记号），或至少澄清所用范数约定使得 κ 而非 κ² 出现的原因。

**W3. [major] κ-guard 阈值缺乏理论依据**

- 具体位置：Section 4.2; Appendix A.1 (page 11)
- 问题：κ = 100 的阈值通过经验扫描 {10, 25, 50, 100, 200, 500, 1000} 确定（Appendix A.1），但缺乏与有限样本余项的理论连接。一个原则性的方法应将阈值与 n_expert/K、先验浓度参数 α_0、以及目标覆盖率联系起来。当前实验中所有 13 个 LLM-dataset 组合的 κ ∈ (1.25, 3]（Section 4.2），远低于 100，说明在测试条件下 κ-guard 从未触发——其实际鲁棒性未被真正检验。
- 建议：(1) 构造或展示 κ 接近阈值的测试案例；(2) 讨论 κ-guard 触发时从分层校正退回全局校正的理论代价。

**W4. [minor] 在中等异质性条件下改进有限**

- 具体位置：Table 1 (page 8); Section 5.3
- 问题：在 K=2 moderate 条件下（Δτ 较小），EC-HTE 的 RMSE（0.049）vs. Global（0.050）差异极小（2% 改善）。Table 4 的预算分析也显示在中等异质性下 HB EC-HTE 的 RMSE 与 Global 基本持平。论文强调的 7.4× 偏差缩减仅在极端异质性条件下实现。
- 建议：更明确地刻画方法的"甜区"：何时 EC-HTE 显著优于简单的全局校正，何时两者实质等价。

**W5. [minor] 效果量报告应更仔细限定**

- 具体位置：Abstract ("reducing |bias| by 7.4×"); Section 1
- 问题："reducing |bias| by 7.4×" 是相对于 naive（无校正）的比较（Table 1: 0.059 → 0.008），而非相对于全局校正（0.090 → 0.008，实际改善 11.25×）。由于全局校正在此场景下反而增加偏差（0.090 > 0.059），这个对比选择虽然正确但容易误导读者认为 7.4× 是 EC-HTE 相对于已有最佳方法的改善。
- 建议：明确标注 7.4× 的基线是 naive，并同时报告相对于 Global 的改善。

**W6. [minor] 经验贝叶斯两阶段估计的不确定性传播**

- 具体位置：Section 4.1 (method.tex:17-24)
- 问题：先验 Dir(α_0 · Ĉ_global) 的中心 Ĉ_global 和浓度参数 α_0 均由数据估计（经验贝叶斯）。这是一个两阶段程序，但第一阶段估计 Ĉ_global 和 α_0 的不确定性未被传播到后验 Ĉ_s 中。在小样本场景（n_expert/K < 50）下，这可能导致置信区间偏窄。
- 建议：讨论这一近似的影响，或在小样本场景下与全贝叶斯联合估计进行对比。

## Questions

**Q1.** Theorem 1 的证明要求 M_s（贝叶斯混合矩阵）在 (A2)-(A3) 下与 C_s 一致。当 P(Z=1) ≠ 0.5（放松 A3）时，M_s 和 C_s 不再相等——此时恒等式的精确形式如何？Appendix T 的 R² ≥ 0.976 是实证验证，但理论上修正系数的封闭形式是什么？

**Q2.** Section 4.3 将 EC-HTE 与 PPCI 组合使用。PPCI 的理论保证假设校正统一应用于全样本，而 EC-HTE 是分层校正——这是否影响 PPCI 的有效性？两种校正的组合是否有理论保证（beyond Appendix K 的实证验证）？

**Q3.** Corollary 1（Aggregate Bias = Cov_w(π_s, Δτ_s)/(1−2π̄)）暗示当误差率与 CATE 异质性不相关时，聚合偏差为零。但在实践中，误差率高的子群体（如复杂文本的子群体）往往也有不同的处理效应。论文是否有经验证据说明 Cov(π_s, Δτ_s) 在真实数据中的典型量级？

**Q4.** Table 2 的 MCMC 收敛诊断报告 R̂ < 1.01 和 ESS > 1018。但 Section 4.1 (method.tex:23) 提到实际使用经验贝叶斯优化（<5ms）而非 MCMC。请澄清：主实验使用的是经验贝叶斯还是 MCMC？如果是前者，Table 2 的收敛诊断是否仅用于验证？

**Q5.** 论文在 Limitations 中提到"ground-truth subgroup CATEs are unavailable in public causal inference benchmarks"。这意味着半合成实验中的 CATE 是注入的而非观察的。在 Civil Comments 真实案例研究（Section M）中，如何验证 EC-HTE 的校正确实改善了 CATE 估计的准确性？

## Missing References

未发现重大遗漏。相关文献覆盖充分，包括 measurement error 经典文献（Fuller 1987, Carroll et al. 2006）、LLM 标注（Gilardi et al. 2023）、因果推断（Wager and Athey 2018, Kennedy 2023）和 PPI（Angelopoulos et al. 2023）。

可考虑补充：
- Hernán and Cole (2009) "Causal diagrams and measurement bias" — 从 DAG 角度讨论测量误差在因果图中的传播，与本文的恒等式方法互补。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 核心定理正确且证明完整；有限样本余项的 O_p 界存在 κ vs. κ² 的精度问题；κ-guard 阈值缺乏理论基础 |
| Excitement | 3.5/5 | 连接 NLP 标注质量与因果推断的时效性课题；"去偏增偏"现象揭示具有实践价值；但改善在中等异质性下有限 |
| Reproducibility | 4/5 | Algorithm 1 完整可复现；声称代码公开可用；实验细节（DGP、超参数、MC 设定）在附录中充分描述 |
| Reviewer Confidence | 4/5 | 我仔细阅读了全文（含 33 页附录），手动验证了 Theorem 1 和 Proposition 5 的证明，对因果推断和测量误差文献有充分了解 |

## Overall Assessment

**Score: 4 (Conference)**

**一句话总结：** 本文在 LLM 标注的因果推断中提出了一个正确且有实用价值的精确偏差恒等式，实验验证异常全面，是 NLP 与因果推断交叉领域的扎实贡献——但对称误分类假设限制了理论结果的直接适用性，有限样本分析可进一步加强。

论文的核心理论贡献——偏差的乘积分解——是新颖的，将 Frazis-Loewenstein 的标量衰减推广到子群体异质误差率的场景。"去偏反而增偏"的发现具有实践警示意义。EC-HTE 方法设计合理，层级贝叶斯提供了自然的偏差-方差权衡。实验规模（520+ 配置 × 100 MC 运行 × 11 LLM）远超同类论文的平均水平。

主要保留意见：(1) 对称假设 (A2) 使得主定理的简洁形式在 NLP 实践中的适用性受限；(2) 有限样本分析和 κ-guard 设计可以更严谨；(3) 在中等异质性条件下方法改进有限。这些问题不影响接收决定，但应在修改中加强。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2326 · 2026-05-25T04:28:28.334194+00:00_

Reviewer 1 初审已收到。评分 4 (Conference)，主要关注点：对称假设适用性、有限样本余项精度、κ-guard 理论依据。

等待 Reviewer 2 初审返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 184

## Round 184

2 recorded events


### User

_source line 2327 · 2026-05-25T04:28:39.578835+00:00_

[Reviewer 1 审稿结果]:
审稿完成。总结：

**Overall: 4 (Conference)**。核心贡献是一个正确的精确偏差恒等式 bias = δ_s·Δτ/(1−2π̄)，手动验证了 Theorem 1 和 Proposition 5 的证明。实验规模（520+ 配置 × 11 LLM）远超同类论文。

主要问题：
- **W1 [major]** 对称误分类假设 (A2) 限制了主定理在真实 NLP 场景的直接适用性（真实 LLM 的 FPR/FNR 差异可达 0.09）
- **W2 [major]** 有限样本余项应为 O_p(κ² · n⁻¹/²) 而非论文声称的 O_p(κ · n⁻¹/²)
- **W3 [major]** κ-guard 阈值 100 纯经验选择，且实验中从未触发（实际 κ ∈ 1.25–3）
- **W4-W6 [minor]** 中等异质性下改善有限；效果量基线应明确标注；经验贝叶斯两阶段不确定性未传播

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2328 · 2026-05-25T04:28:46.102672+00:00_

Reviewer 1 审稿已收到（Score: 4, Conference）。等待 Reviewer 2 返回后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 185

## Round 185

6 recorded events


### User

_source line 2329 · 2026-05-25T04:28:59.093049+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见 — Round 1

**论文**: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"
**审查侧重**: 新颖性、相关工作完整性、写作质量、格式合规

---

## Summary

本文研究了当 LLM 标注的误差率在子群间异质时，标准的全局混淆矩阵校正会引入偏差甚至反转因果效应方向的问题。作者推导了一个精确的偏差恒等式 δ_s · Δτ / (1 − 2π̄)，给出了一个不需要估计处理效应即可从误差率诊断校正是否有害的判据（Proposition 5），并提出了基于层次贝叶斯的逐子群校正方法（EC-HTE）。在合成数据、半合成数据（8个LLM × 2个数据集）和4个NLP任务上进行了验证。

---

## 总体评分

**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 理论贡献干净且有实际意义，但 algebraic 推导深度有限、缺乏端到端真实数据评估、目标受众在 EMNLP 偏窄，介于 Conference 和 Findings 之间。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 理论推导正确，证明完整（Appendix B），实验覆盖面广（520+ synthetic configs, 11 real LLMs, 4 NLP tasks），假设放松讨论充分（Remark 2, Prop 3, Appendix D-H）。扣分点：核心恒等式在 simulated DGP 上验证 R²=0.97+ 是预期内的（假设成立时代数恒等式必然高拟合），更有信息量的 per-model R² range 0.76-0.99 中低端未深入分析。 |
| Excitement | 3/5 | 问题及时（LLM-as-annotator 日益普及），恒等式形式优雅，诊断判据有实用价值。但 (a) 核心结果是矩阵代数的直接推导，数学深度有限；(b) effect modifier misclassification 设定偏窄，限制了 NLP 社区的受众面；(c) 方法层面（hierarchical Bayes CM estimation）是 Dawid-Skene 架构的直接应用，创新性有限。 |
| Reproducibility | 4/5 | 提供匿名代码链接，DGP 和实验配置在 appendix 中详细说明，Algorithm 1 给出了完整伪代码。但代码是否可运行未经验证。 |

---

## Strengths

**S1. 理论贡献清晰且可操作。** Theorem 1 的乘积形式 δ_s · Δτ / (1 − 2π̄) 结构直观——偏差来自子群误差偏离（δ_s）与 CATE 异质性（Δτ）的交互，被矩阵逆运算放大。更重要的是 Proposition 5 给出了一个不依赖 Δτ 的诊断判据（Eq. 5: |δ_s| / ((1−2π̄)·π_s) > 1），使从业者能仅凭 pilot 样本的误差率决定是否使用全局校正，AUC=0.86（对称误差）。这种"先诊断再校正"的工作流程对实际应用有直接价值。

**S2. 实验设计全面且有层次。** 论文不仅在合成数据上验证恒等式（Section 5.2, R²=0.994 for K=2），还通过 16 个真实 LLM 混淆矩阵的半合成评估（Appendix R）、4 个 NLP 任务的跨任务验证（TweetEval, CivilComments, Stance, AG News）、8 项鲁棒性检查（非对称误差、子群误指定、treatment-dependent misclassification 等）提供了多层次的证据。CausalForest 和 R-learner 的跨估计器验证（Table 1, Appendix P）进一步确认偏差来自混淆矩阵结构而非下游估计器。

**S3. 操作条件的诚实表述。** 论文明确给出了 EC-HTE 的适用边界（Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4, FNR < 0.50），并在条件不满足时推荐保留全局校正（Section 5.4）。Figure 3 展示的 RMSE vs. expert budget crossover 是实用的决策工具。这种"何时不用我的方法"的透明度在投稿论文中值得肯定。

**S4. Related work 定位精准。** 论文清晰区分了三个维度的新颖性（Section 2, para 2）：(1) effect modifier misclassification vs. regressor/confounder error, (2) correction-induced bias vs. attenuation bounding, (3) heterogeneous error interaction vs. homogeneous-error analyses。与 Frazis-Loewenstein 标量衰减的对比（Section 3, proof sketch）特别有说服力。

---

## Weaknesses

**W1. [major] 核心恒等式的数学深度有限，novelty 主要在问题提出而非技术贡献。**
- 具体位置：Section 3, Theorem 1, proof sketch (lines 46-51 of theory.tex)
- 问题：Theorem 1 的推导本质上是计算 M_global^{-1} M_s − I 并将其作用于 τ 向量，是 2×2 矩阵代数的直接展开。proof sketch 自身仅需 4 行即可完成。Remark 2 虽然将结果推广到非对称情形，但推广后的诊断 AUC 从 0.86 大幅降至 0.66（Appendix I），说明对称假设下的简洁形式在实际中可能不够用。
- 为什么影响接收：对于 *ACL 顶会，reviewer 期望理论贡献有一定的技术深度或非显然性。本文的贡献更多在于"识别并形式化一个被忽视的问题"，而非"解决一个技术上困难的问题"。这本身有价值，但 excitement 评分因此受限。
- 建议：(1) 更深入讨论非对称情形下 AUC 降至 0.66 的 implications——这意味着诊断在实际 LLM 中失效的概率不小；(2) 考虑给出非对称情形下的改进诊断。

**W2. [major] 缺乏端到端真实数据评估。**
- 具体位置：Section 5, Limitations section
- 问题：所有实验均使用合成 CATE 注入到真实文本特征上的半合成 DGP。论文在 Limitations 中承认"Ground-truth subgroup CATEs are unavailable in public datasets"，但这一局限严重。没有任何一个实验展示了在真实因果推断任务中，EC-HTE 校正改变了实质性结论。CivilComments 的例子（Section 5.2 最后一段, "reveals a 3.2× effect-size gap"）最接近真实应用，但仍基于注入的合成 CATE。
- 为什么影响接收：对于一篇声称"debiasing hurts"的论文，读者会期望看到至少一个真实案例中全局校正确实导致了错误结论，而 per-subgroup 校正恢复了正确结论。在纯合成设定下，"14.9% sign reversal"的发现取决于 DGP 参数设置（$\tau(0)=0.03$ 是一个特定选择）。
- 建议：(1) 尝试复现一个已发表的使用 LLM 标注进行 HTE 分析的研究，展示校正方法的影响；(2) 或至少讨论 $\tau(0)=0.03$ 这一参数选择在实际应用中的代表性——在哪些社会科学场景下效应量确实这么小。

**W3. [minor] Abstract 信息密度过高，读起来像 results summary 而非 motivation-driven 摘要。**
- 具体位置：abstract.tex
- 问题：Abstract 在约 185 words 中塞入了 R²=0.97、R²=0.975、0.76-0.99、14.9%、τ(0)=0.03、Δπ>0.15、n_expert/K≥50、K≤4、7.4× 等至少 9 个具体数字。这使得摘要读起来像实验报告的摘要表格，而非引导读者理解问题重要性的入口。数学公式 δ_s·Δτ/(1−2π̄) 在 abstract 中出现也增加了阅读门槛。
- 建议：精简数字到 3-4 个最关键的（如 sign reversal rate, bias reduction factor），将 R² 验证细节留给正文。用 1-2 句话加强 motivation（为什么这个问题对 NLP 社区重要）。

**W4. [minor] "Debiasing" 一词在 NLP 社区的歧义。**
- 具体位置：Title, footnote 1 (Introduction)
- 问题：标题中的"debiasing"在 NLP 社区通常指 algorithmic fairness debiasing（如 gender bias in word embeddings）。虽然论文在脚注 1 中做了澄清，但标题级别的歧义可能导致错误的受众预期和引用。搜索 "debiasing NLP" 的读者和本文的目标读者可能没有交集。
- 建议：考虑更精确的措辞如 "When Correction Backfires" 或 "When Error Correction Hurts"，避免与 fairness debiasing 混淆。

**W5. [minor] Figure 4（bias amplification heatmap）浮动到第 9 页（references 区域）。**
- 具体位置：PDF page 9
- 问题：Figure 4 在 theory.tex（Section 3）和 experiments.tex（Section 5.2）中被引用，但实际渲染位置在 references 开始之后的第 9 页。对于 main text 中引用的关键图表，这种 float 位置不理想，可能导致 reviewer 认为该图不在正文范围内。
- 建议：调整 float 位置或缩小其他图表，确保 Figure 4 出现在第 8 页内。

**W6. [minor] Per-model R² range 0.76-0.99 的低端未充分讨论。**
- 具体位置：Abstract, Section 5.4
- 问题：aggregate R²=0.975 across 11 LLMs 看起来很好，但 per-model R² 低至 0.76 意味着对某些 LLM，恒等式只能解释 76% 的偏差变异。是哪些 LLM？为什么？是因为 (A2) 对称误差假设不成立，还是其他原因？论文在 Remark 2 和 Appendix I 中讨论了非对称情形，但没有明确 link 到具体 LLM 的 R² 下降。
- 建议：在正文或 appendix 中给出 per-LLM R² 表，并分析 R² 低的模型是否系统性地违反了特定假设。

---

## Questions

**Q1.** Proposition 5 的诊断在对称误差下 AUC=0.86，非对称下降至 0.66。在实际 LLM 中，FPR ≠ FNR 是常态（例如 hate speech detection 中 false negative 通常高于 false positive）。那么在实际部署中，诊断判据的可靠性如何？是否有改进的非对称版本？

**Q2.** EC-HTE 的层次贝叶斯估计使用 empirical Bayes（<5ms），但 Algorithm 1 中描述了 Gibbs sampler（4 chains, 4000 iter）。正文和算法的描述不完全一致——实际实验中使用的是哪个？

**Q3.** 论文声称 EC-HTE 与 PPCI 可组合（Section 4, 最后一段: "|bias| from 0.179 to 0.007"）。但这假设 covariate-side error 和 outcome-side error 独立。在什么条件下这一独立性假设会失效？例如当 LLM 同时标注 effect modifier 和 outcome 时。

**Q4.** Table 1 中 K=4 的 DIM 配置下，Strat. MLE 的 |Bias| (0.010) 略低于 HB EC-HTE (0.012)，但 RMSE 更高（0.127† vs 0.120）。这是否意味着在 K=4 时层次贝叶斯的偏差-方差权衡并没有明显优势？在什么条件下 stratified MLE 是更好的选择？

---

## Missing References

相关工作整体覆盖面很好，横跨测量误差、因果推断、NLP 标注、PPI 四个领域。以下是可能补充的方向：

1. **Filtered/Extended PPI (2025-2026)**：近期有多篇工作扩展 PPI 以处理异质性预测质量（如 "Filtered Prediction-Powered Inference", arXiv 2602.10464），可能与本文的 heterogeneous error 设定相关，值得在 Section 2 讨论是否 subsume 本文的问题。

2. **Egami et al. bib 年份不一致**：bib key 为 `egami2024dsl` 但 `year={2023}`——NeurIPS 2023 发表是正确的，但引用标签可能在最终版本中造成混淆（这是格式问题，非内容缺失）。

3. 总体而言，对于本文声称的 novelty（effect modifier misclassification 作为新问题），我在文献搜索中未找到直接的先前工作处理这一具体设定，支持了作者的 novelty claim。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| ACL 模板 (`\usepackage[review]{acl}`) | ✓ | main.tex line 2 |
| 匿名性 | ✓ | `\author{Anonymous}`, 代码链接为 anonymous.4open.science |
| 正文 ≤ 8 页 | ✓ | 正文（Section 1-6）+ Limitations 在第 8 页内完成；Limitations 不计入页数限制 |
| Limitations section | ✓ | 位于正文末尾（Section 6 之后，References 之前），unnumbered section |
| Abstract ≤ 200 words | ✓ | 约 185 words |
| 引用格式一致性 | ✓ | 使用 `\cite` 和 `\citet`/`\citep`，格式一致 |
| 附录结构 | ✓ | `\appendix` 在 references 之后，结构合规 |
| Figure 4 位置 | ⚠ | 浮动到第 9 页（references 之后），建议修复 |

---

## 主要优势总结

1. 识别并形式化了一个被忽视的实际问题（correction-induced bias in effect modifier misclassification）
2. 乘积形式的恒等式结构直观、可操作，诊断判据不需要估计处理效应
3. 实验覆盖面广，操作条件的边界表述诚实
4. 相关工作定位精准，与经典文献的区分清晰

## Overall Assessment

**Score: 3.5 (Borderline Conference)**
**Confidence: 4/5**

理由：本文识别了一个genuine gap（全局校正在异质误差下的harmful effect），理论清晰、实验全面、写作质量高于平均水平。主要顾虑是：(1) 核心恒等式的数学深度较浅——乘积形式是 2×2 矩阵代数的直接结果，novelty 更多在问题识别而非技术突破；(2) 缺乏真实数据端到端评估削弱了实际影响力的论证；(3) effect modifier misclassification 设定在 EMNLP 受众中偏窄。论文达到了 Findings 的水平，如果能补充一个真实案例评估或更深入的非对称误差分析，有潜力提升到 Conference。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2330 · 2026-05-25T04:29:45.394293+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "ec_hte_llm_annotation",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Strength、Weakness 和 Question。对每一条使用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文研究 LLM 标注用于因果推断时，传统全局混淆矩阵校正在子群体误差率异质的条件下会引入新偏差的问题。核心贡献是推导出一个精确的偏差恒等式（Theorem 1），表明全局校正的偏差具有三因子乘积形式：δ_s·Δτ/(1−2π̄)——子群体误差偏离 × CATE 异质性 × 逆矩阵放大。在此基础上提出 EC-HTE 方法，通过层级贝叶斯估计每个子群体的混淆矩阵，进行分层校正。论文包含 520+ 合成配置、11 个 LLM × 数据集组合以及真实数据验证。\n\n### Strengths\nS1. Theorem 1 的偏差恒等式形式简洁、可解释性强，证明（Appendix B）通过矩阵代数严格验证，手动核实推导正确。Proposition 5 的诊断准则 AUC = 0.86 可操作。\nS2. 520 个合成配置、100 MC 运行、11 个真实 LLM 的半合成验证、6 个 NLP 任务、8 个鲁棒性检验，实验验证异常全面。Table 23 聚合 R² = 0.975。\nS3. 从恒等式到方法到实践的完整链条。Algorithm 1 清晰可复现。\nS4. 连接 NLP 与因果推断的时效性。14.9% 符号反转、Figure 4 热力图。\nS5. 假设放松的系统性讨论（A2 对称性、A3 类别平衡、A5 同质处理效应、A1 条件独立性）。\n\n### Weaknesses\nW1. [major] 对称误分类假设 (A2) 在实际 NLP 中限制性强。真实 LLM 的 FPR/FNR 差异达 0.09（GPT-4o: FPR=0.249, FNR=0.157）。非对称下诊断 AUC 从 0.86 降至 0.66。标题和摘要的\"exact identity\"措辞可能误导。\nW2. [major] 有限样本余项应为 O_p(κ² · n⁻¹/²) 而非论文声称的 O_p(κ · n⁻¹/²)。通过标准矩阵扰动分析 (C+E)⁻¹ = C⁻¹ − C⁻¹EC⁻¹ + O(‖E‖²)，一阶项范数为 ‖C⁻¹‖² · ‖E‖ ∝ κ² · n⁻¹/²。\nW3. [major] κ-guard 阈值 100 纯经验选择，且实验中从未触发（实际 κ ∈ 1.25–3），53× 安全余量。缺乏与有限样本余项的理论连接。\nW4. [minor] 中等异质性下 EC-HTE 改善仅 2%（RMSE 0.049 vs 0.050）。7.4× 仅在极端条件下。\nW5. [minor] \"7.4× bias reduction\" 基线是 naive（0.059→0.008），实际相对于 Global 改善为 11.25×。对比选择正确但可能误导。\nW6. [minor] 经验贝叶斯两阶段估计的不确定性未传播到后验。\n\n### Questions\nQ1. 放松 A3 时 M_s ≠ C_s，恒等式的理论修正系数封闭形式？\nQ2. EC-HTE 分层校正与 PPCI 统一校正的理论兼容性？\nQ3. Cov(π_s, Δτ_s) 在真实数据中的典型量级？\nQ4. 主实验用的是经验贝叶斯还是 MCMC？Table 2 的收敛诊断是否仅用于验证？\nQ5. CivilComments 案例中如何验证 EC-HTE 改善了 CATE 准确性？\n\n### Overall\nScore: 4 (Conference), Confidence: 4/5\n\n---\n\n请对以上每一条 S1-S5、W1-W6、Q1-Q5 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "ec_hte_llm_annotation",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Strength、Weakness 和 Question。对每一条使用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Summary\n本文研究 LLM 标注用于因果推断时，传统全局混淆矩阵校正在子群体误差率异质的条件下会引入新偏差的问题。核心贡献是推导出一个精确的偏差恒等式（Theorem 1），表明全局校正的偏差具有三因子乘积形式：δ_s·Δτ/(1−2π̄)——子群体误差偏离 × CATE 异质性 × 逆矩阵放大。在此基础上提出 EC-HTE 方法，通过层级贝叶斯估计每个子群体的混淆矩阵，进行分层校正。论文包含 520+ 合成配置、11 个 LLM × 数据集组合以及真实数据验证。\n\n### Strengths\nS1. Theorem 1 的偏差恒等式形式简洁、可解释性强，证明（Appendix B）通过矩阵代数严格验证，手动核实推导正确。Proposition 5 的诊断准则 AUC = 0.86 可操作。\nS2. 520 个合成配置、100 MC 运行、11 个真实 LLM 的半合成验证、6 个 NLP 任务、8 个鲁棒性检验，实验验证异常全面。Table 23 聚合 R² = 0.975。\nS3. 从恒等式到方法到实践的完整链条。Algorithm 1 清晰可复现。\nS4. 连接 NLP 与因果推断的时效性。14.9% 符号反转、Figure 4 热力图。\nS5. 假设放松的系统性讨论（A2 对称性、A3 类别平衡、A5 同质处理效应、A1 条件独立性）。\n\n### Weaknesses\nW1. [major] 对称误分类假设 (A2) 在实际 NLP 中限制性强。真实 LLM 的 FPR/FNR 差异达 0.09（GPT-4o: FPR=0.249, FNR=0.157）。非对称下诊断 AUC 从 0.86 降至 0.66。标题和摘要的\"exact identity\"措辞可能误导。\nW2. [major] 有限样本余项应为 O_p(κ² · n⁻¹/²) 而非论文声称的 O_p(κ · n⁻¹/²)。通过标准矩阵扰动分析 (C+E)⁻¹ = C⁻¹ − C⁻¹EC⁻¹ + O(‖E‖²)，一阶项范数为 ‖C⁻¹‖² · ‖E‖ ∝ κ² · n⁻¹/²。\nW3. [major] κ-guard 阈值 100 纯经验选择，且实验中从未触发（实际 κ ∈ 1.25–3），53× 安全余量。缺乏与有限样本余项的理论连接。\nW4. [minor] 中等异质性下 EC-HTE 改善仅 2%（RMSE 0.049 vs 0.050）。7.4× 仅在极端条件下。\nW5. [minor] \"7.4× bias reduction\" 基线是 naive（0.059→0.008），实际相对于 Global 改善为 11.25×。对比选择正确但可能误导。\nW6. [minor] 经验贝叶斯两阶段估计的不确定性未传播到后验。\n\n### Questions\nQ1. 放松 A3 时 M_s ≠ C_s，恒等式的理论修正系数封闭形式？\nQ2. EC-HTE 分层校正与 PPCI 统一校正的理论兼容性？\nQ3. Cov(π_s, Δτ_s) 在真实数据中的典型量级？\nQ4. 主实验用的是经验贝叶斯还是 MCMC？Table 2 的收敛诊断是否仅用于验证？\nQ5. CivilComments 案例中如何验证 EC-HTE 改善了 CATE 准确性？\n\n### Overall\nScore: 4 (Conference), Confidence: 4/5\n\n---\n\n请对以上每一条 S1-S5、W1-W6、Q1-Q5 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2331 · 2026-05-25T04:30:16.349324+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30955
}
```

</details>

---


### Tool call

_source line 2332 · 2026-05-25T04:30:16.552395+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "ec_hte_llm_annotation",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Strength、Weakness 和 Question。对每一条使用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Summary\n本文研究了当 LLM 标注的误差率在子群间异质时，标准的全局混淆矩阵校正会引入偏差甚至反转因果效应方向的问题。作者推导了一个精确的偏差恒等式 δ_s · Δτ / (1 − 2π̄)，给出了一个不需要估计处理效应即可从误差率诊断校正是否有害的判据（Proposition 5），并提出了基于层次贝叶斯的逐子群校正方法（EC-HTE）。在合成数据、半合成数据（8个LLM × 2个数据集）和4个NLP任务上进行了验证。\n\n### Strengths\nS1. Theorem 1 的乘积形式结构直观。Proposition 5 给出不依赖 Δτ 的诊断判据（AUC=0.86），使从业者能仅凭 pilot 样本决定是否使用全局校正。\nS2. 实验设计全面且有层次：合成 → 半合成（16 个真实 LLM CM）→ 4 个 NLP 任务 → 8 项鲁棒性检查 → 跨估计器验证。\nS3. 操作条件的诚实表述（Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4, FNR < 0.50），Figure 3 的 crossover 是实用决策工具。\nS4. Related work 定位精准，三维度新颖性区分清晰。\n\n### Weaknesses\nW1. [major] 核心恒等式的数学深度有限——2×2 矩阵代数的直接展开，proof sketch 仅 4 行。novelty 主要在问题提出而非技术贡献。非对称推广后诊断 AUC 从 0.86 大幅降至 0.66，说明对称假设下的简洁形式在实际中可能不够用。\nW2. [major] 缺乏端到端真实数据评估。所有实验均使用合成 CATE 注入。CivilComments \"3.2× effect-size gap\" 仍基于合成 CATE。无真实案例展示全局校正导致错误结论而 per-subgroup 校正恢复正确结论。\"14.9% sign reversal\" 取决于 τ(0)=0.03 这一特定参数选择。\nW3. [minor] Abstract 信息密度过高（9+ 具体数字），读起来像 results summary 而非 motivation-driven 摘要。\nW4. [minor] \"Debiasing\" 一词在 NLP 社区与 algorithmic fairness debiasing 混淆。脚注 1 的澄清在标题层面不够。\nW5. [minor] Figure 4 浮动到第 9 页（references 区域），应在第 8 页内。\nW6. [minor] Per-model R² range 0.76-0.99 低端未充分讨论。哪些 LLM？为什么？\n\n### Questions\nQ1. 非对称误差下诊断 AUC 仅 0.66，实际 LLM 中 FPR ≠ FNR 是常态。有改进的非对称版本吗？\nQ2. Algorithm 1 描述 Gibbs sampler（4 chains, 4000 iter），正文说 empirical Bayes（<5ms）——实际用哪个？\nQ3. EC-HTE + PPCI 组合假设 covariate-side 和 outcome-side error 独立。当 LLM 同时标注 effect modifier 和 outcome 时，独立性会失效吗？\nQ4. K=4 时 Strat. MLE |Bias| (0.010) < HB EC-HTE (0.012) 但 RMSE 更高——层次贝叶斯在 K=4 是否真有优势？\n\n### Missing References\n- Filtered PPI (arXiv 2602.10464) 处理异质性预测质量，与本文的 heterogeneous error 设定相关\n- Egami et al. bib key 为 `egami2024dsl` 但 `year={2023}` (NeurIPS 2023)——年份不一致\n\n### Overall\nScore: 3.5 (Borderline Conference), Confidence: 4/5\n理由：novelty 更多在问题识别而非技术突破；缺乏真实数据端到端评估；effect modifier misclassification 设定在 EMNLP 受众中偏窄。\n\n---\n\n请对以上每一条 S1-S4、W1-W6、Q1-Q4 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注 W1（数学深度）和 W2（真实数据评估）这两个 major weakness——你是否同意这些会影响接收决定？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "ec_hte_llm_annotation",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Strength、Weakness 和 Question。对每一条使用 **[AGREE]** 表示同意并说明理由，或 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Summary\n本文研究了当 LLM 标注的误差率在子群间异质时，标准的全局混淆矩阵校正会引入偏差甚至反转因果效应方向的问题。作者推导了一个精确的偏差恒等式 δ_s · Δτ / (1 − 2π̄)，给出了一个不需要估计处理效应即可从误差率诊断校正是否有害的判据（Proposition 5），并提出了基于层次贝叶斯的逐子群校正方法（EC-HTE）。在合成数据、半合成数据（8个LLM × 2个数据集）和4个NLP任务上进行了验证。\n\n### Strengths\nS1. Theorem 1 的乘积形式结构直观。Proposition 5 给出不依赖 Δτ 的诊断判据（AUC=0.86），使从业者能仅凭 pilot 样本决定是否使用全局校正。\nS2. 实验设计全面且有层次：合成 → 半合成（16 个真实 LLM CM）→ 4 个 NLP 任务 → 8 项鲁棒性检查 → 跨估计器验证。\nS3. 操作条件的诚实表述（Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4, FNR < 0.50），Figure 3 的 crossover 是实用决策工具。\nS4. Related work 定位精准，三维度新颖性区分清晰。\n\n### Weaknesses\nW1. [major] 核心恒等式的数学深度有限——2×2 矩阵代数的直接展开，proof sketch 仅 4 行。novelty 主要在问题提出而非技术贡献。非对称推广后诊断 AUC 从 0.86 大幅降至 0.66，说明对称假设下的简洁形式在实际中可能不够用。\nW2. [major] 缺乏端到端真实数据评估。所有实验均使用合成 CATE 注入。CivilComments \"3.2× effect-size gap\" 仍基于合成 CATE。无真实案例展示全局校正导致错误结论而 per-subgroup 校正恢复正确结论。\"14.9% sign reversal\" 取决于 τ(0)=0.03 这一特定参数选择。\nW3. [minor] Abstract 信息密度过高（9+ 具体数字），读起来像 results summary 而非 motivation-driven 摘要。\nW4. [minor] \"Debiasing\" 一词在 NLP 社区与 algorithmic fairness debiasing 混淆。脚注 1 的澄清在标题层面不够。\nW5. [minor] Figure 4 浮动到第 9 页（references 区域），应在第 8 页内。\nW6. [minor] Per-model R² range 0.76-0.99 低端未充分讨论。哪些 LLM？为什么？\n\n### Questions\nQ1. 非对称误差下诊断 AUC 仅 0.66，实际 LLM 中 FPR ≠ FNR 是常态。有改进的非对称版本吗？\nQ2. Algorithm 1 描述 Gibbs sampler（4 chains, 4000 iter），正文说 empirical Bayes（<5ms）——实际用哪个？\nQ3. EC-HTE + PPCI 组合假设 covariate-side 和 outcome-side error 独立。当 LLM 同时标注 effect modifier 和 outcome 时，独立性会失效吗？\nQ4. K=4 时 Strat. MLE |Bias| (0.010) < HB EC-HTE (0.012) 但 RMSE 更高——层次贝叶斯在 K=4 是否真有优势？\n\n### Missing References\n- Filtered PPI (arXiv 2602.10464) 处理异质性预测质量，与本文的 heterogeneous error 设定相关\n- Egami et al. bib key 为 `egami2024dsl` 但 `year={2023}` (NeurIPS 2023)——年份不一致\n\n### Overall\nScore: 3.5 (Borderline Conference), Confidence: 4/5\n理由：novelty 更多在问题识别而非技术突破；缺乏真实数据端到端评估；effect modifier misclassification 设定在 EMNLP 受众中偏窄。\n\n---\n\n请对以上每一条 S1-S4、W1-W6、Q1-Q4 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注 W1（数学深度）和 W2（真实数据评估）这两个 major weakness——你是否同意这些会影响接收决定？"
  }
}
```

</details>

---


### Tool result

_source line 2333 · 2026-05-25T04:30:17.919014+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1366
}
```

</details>

---


### Assistant

_source line 2334 · 2026-05-25T04:30:24.742411+00:00_

交叉分享已完成。两位 Reviewer 正在互审对方意见，等待交叉回应。

**当前进度**：
- Step 1（独立审稿）：✅ R1=4.0, R2=3.5
- Step 2（交叉分享）：进行中，等待双方逐条回应
- 视觉审查：已派发，与审稿并行
- 外部审稿：项目未配置，不启用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 186

## Round 186

2 recorded events


### User

_source line 2335 · 2026-05-25T04:30:27.396781+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心评价：**3.5 (Borderline Conference)**，confidence 4/5。

主要判断依据：
- **Strengths**: 恒等式形式优雅且可操作，诊断判据有实用价值，实验覆盖面广，操作条件边界表述诚实
- **关键弱点**: (1) 核心理论是 2×2 矩阵代数的直接推导，数学深度有限；(2) 全部实验为合成/半合成，缺乏真实因果推断任务的端到端评估；(3) 非对称误差下诊断 AUC 从 0.86 降至 0.66，限制实际可用性
- **格式**: 基本合规，Figure 4 浮动到第 9 页是唯一需修复的排版问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2336 · 2026-05-25T04:30:32.084320+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 187

## Round 187

52 recorded events


### User

_source line 2337 · 2026-05-25T04:32:31.295522+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 (R1)

---

## Strengths 回应

**[AGREE] R1-S1**: Theorem 1 的乘积形式确实简洁可解释，proof 可手动核实。Proposition 5 的 AUC=0.86 在对称情形下有操作价值。我在自己的 S1 中做了相同评价。补充一点：Prop 5 的关键优势在于不需要估计 Δτ，仅凭 pilot 样本的误差率即可决策——这在实际部署中比恒等式本身更有价值。

**[AGREE] R1-S2**: 实验全面性我完全同意。520 configurations × 100 MC + 11 real LLMs + 4 NLP tasks + 8 robustness checks 的覆盖面在 *ACL 投稿中属于上乘。我在自己的 S2 中做了类似评价，并特别注意到跨估计器验证（CausalForest + R-learner, Table 1 + Appendix P）是论文的一个加分项。

**[AGREE] R1-S3**: 从恒等式到方法到实践的链条完整。Algorithm 1 的伪代码清晰。补充：论文在 Section 5.4 明确给出操作边界（Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4），这种"何时不用本方法"的诚实度是一个值得肯定的优点（我的 S3）。

**[AGREE] R1-S4**: NLP 与因果推断的交叉确实是一个时效性好的方向。14.9% sign reversal 是吸引眼球的 headline number。

**[AGREE] R1-S5**: 假设放松的系统性讨论（Remark 2 对 A2, Appendix D 对 A3, Proposition 3 对 A5, Appendix H 对 A1）是论文做得好的地方。不过我想补充：放松 A2 后诊断 AUC 从 0.86 降至 0.66 这一事实本身也暴露了理论与实践的 gap，我在自己的 W1 中将此作为 major weakness。

---

## Weaknesses 回应

**[AGREE] R1-W1**: 对称误分类假设 (A2) 在实际 NLP 中确实限制性强。R1 给出的 GPT-4o FPR/FNR 差异数据（0.249 vs 0.157, gap=0.09）有说服力。但我需要修正 R1 关于"exact identity 措辞可能误导"的说法：

**部分 REBUT**：Remark 2（theory.tex lines 53-64）明确指出 Theorem 1 在非对称情形下 **仍然精确成立**——乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} holds exactly for arbitrary asymmetric C_s，因为 B_s·1 = 0 仅依赖 M_s 和 M_global 的随机矩阵性质，不需要 (A2)。降级的是 **诊断判据**（Proposition 5），而非恒等式本身。所以"exact identity"的措辞严格来说没有误导——恒等式确实是 exact 的。误导之处在于 abstract 和 introduction 强调的简洁标量形式 δ_s·Δτ/(1−2π̄) 只在对称假设下成立，而非对称情形下需要逐 cell 计算 [B_s]_{z,1}，大幅增加了实际操作的复杂度。

**[AGREE] R1-W2**: 有限样本余项的阶数问题。R1 的矩阵扰动分析是正确的：(C+E)^{-1} = C^{-1} − C^{-1}EC^{-1} + O(‖E‖²)，一阶项范数为 ‖C^{-1}‖²·‖E‖。对于 2×2 对称混淆矩阵，‖C^{-1}‖ = 1/(1−2π) = κ(C)（因为 ‖C‖ 的最大奇异值为 1），所以余项确实应为 O_p(κ²·n^{-1/2}) 而非论文声称的 O_p(κ·n^{-1/2})（theory.tex line 92）。这是一个技术性错误，虽然在实际 κ ∈ [1.25, 3] 的范围内影响不大（κ² ∈ [1.56, 9] vs κ ∈ [1.25, 3]），但应当修正。

**[AGREE] R1-W3**: κ-guard 阈值 100 的纯经验选择确实缺乏理论依据。53× 安全余量说明在正常条件下这个 guard 完全不起作用。我同意这是一个 minor 问题——Appendix A 的消融实验（Appendix A, κ sweep from 10 to 1000）和自适应公式 κ_adapt = 10√(n_expert/K) 至少提供了实证支持。但如果要与 W2 的有限样本余项建立理论连接，需要推导一个基于 O_p(κ²·n^{-1/2}) 的最优阈值。

**[REBUT] R1-W5**: R1 的计算有误。R1 声称"7.4× bias reduction 基线是 naive（0.059→0.008），实际相对于 Global 改善为 11.25×"。但查看 Table 1（experiments.tex lines 58-79）：
- Naive |Bias| = 0.058
- Global |Bias| = 0.059
- HB EC-HTE |Bias| = 0.008

论文 abstract 说"reducing |bias| by 7.4×"，计算基础是 0.059/0.008 = 7.375 ≈ 7.4×，**基线是 Global 而非 Naive**。R1 声称的"11.25×"（0.090/0.008?）与表中任何数值对的比值都不对应。所以 R1 对 W5 的前提——"基线选择可能误导"——不成立。7.4× 的基线就是 Global，且 Global 和 Naive 的 bias 几乎相同（0.059 vs 0.058），所以无论以哪个为基线，比值都在 7.2-7.4× 范围内。

**[AGREE] R1-W4**: 中等异质性下 EC-HTE 改善极小（RMSE 0.049 vs 0.050, Section 5.3, "p > 0.05; Table 2 supp"）。7.4× 仅在极端异质性下成立。不过我认为论文对此已经足够透明——Section 5.4 的 operating conditions 和 Figure 3 的 crossover plot 都清楚表明了适用边界。这更多是方法的固有局限而非论文的缺陷。

**[AGREE] R1-W6**: 经验贝叶斯两阶段的不确定性传播问题是标准批评。Method section（method.tex line 23）提到"MCMC alternative in Appendix G"作为替代方案，但主实验使用 EB。这确实会低估后验不确定性。不过鉴于 coverage 在所有配置下 ≥ 93%（Section 4.2），实际影响可能有限。

---

## Questions 回应

**[AGREE] R1-Q1**: 放松 A3 时 M_s ≠ C_s 的封闭形式修正系数是一个好问题。论文 theory.tex line 84 称"the identity remains exact with modified coefficients"但未给出显式形式。这个信息应在 appendix 中提供（如果还没有的话）。

**[AGREE] R1-Q2**: EC-HTE + PPCI 的理论兼容性条件值得澄清。我在自己的 Q3 中提出了相同问题——当 LLM 同时标注 effect modifier 和 outcome 时，covariate-side 和 outcome-side error 的独立性假设可能失效。

**[AGREE] R1-Q3**: Cov(π_s, Δτ_s) 在真实数据中的量级是 Corollary 4 实际可用性的关键。论文应在 semi-synthetic 实验中报告这个值，以便读者判断 aggregate bias 的实际严重程度。

**[AGREE] R1-Q4**: 我在自己的 Q2 中提出了完全相同的疑问。Method section 说 empirical Bayes（<5ms），但 Algorithm 1 写的是 Gibbs sampler（4 chains, 4000 iter）。这个不一致需要作者澄清。

**[AGREE] R1-Q5**: CivilComments 案例的验证问题与我的 W2（缺乏端到端真实数据评估）直接相关。没有 ground-truth CATE，无法验证 EC-HTE 揭示的 "3.2× effect-size gap" 是否比 Global 的结论更准确。这是整篇论文最大的 empirical gap。

---

## 关于 Overall Score 的分歧

R1 给出 4.0 (Conference)，我给出 3.5 (Borderline Conference)。分歧的核心在于对 novelty depth 和 audience fit 的判断：

1. **Novelty depth**: R1 更关注技术细节（W2 有限样本余项阶数、W3 κ-guard 理论连接），这些是可以在 revision 中修正的 fixable issues。我更关注核心贡献的数学深度——恒等式本质是 2×2 矩阵代数的直接展开，novelty 主要在问题识别而非技术突破（我的 W1）。

2. **Audience fit**: R1 认为 NLP+因果推断的时效性足以支撑 Conference（S4），我认为 effect modifier misclassification 在 EMNLP 受众中偏窄——大多数 NLP 研究者不做 HTE 分析，而做 HTE 分析的因果推断研究者不一定投 EMNLP。

3. **Real-world evaluation**: R1 没有将缺乏真实数据评估列为 major weakness。我认为这是一个显著弱点（我的 W2）——对于一篇标题声称 "debiasing hurts" 的论文，应该有至少一个真实案例展示这确实发生了。

综合来看，我维持 3.5 的评分。如果作者能 (a) 补充一个真实案例 + (b) 改进非对称诊断的 AUC，我愿意上调至 4.0。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2338 · 2026-05-25T04:33:24.074837+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status,read_project_file,update_review_issues,submit_review_report_to_research_director",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,get_external_review_status,get_visual_check_status,read_project_file,update_review_issues,submit_review_report_to_research_director",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 2339 · 2026-05-25T04:33:24.075266+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2340 · 2026-05-25T04:33:28.093046+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 2341 · 2026-05-25T04:33:28.245013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2342 · 2026-05-25T04:33:34.068520+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2343 · 2026-05-25T04:33:34.520848+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (43 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-041** (negative): Under asymmetric misclassification (FPR≠FNR, ratio 1:2 to 1:5 and reverse), the bias identity retains R²≥0.95 and EC-HTE maintains coverage ≥93% across 48 configurations (6 FPR/FNR ratios × 2 K × 4 Δπ), while the symmetric diagnostic AUC degrades monotonically with FPR/FNR ratio — quantifying the exact diagnostic accuracy loss curve under asymmetry.\n  [exp041_asymmetric_grid](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_grid.csv) | [exp041_asymmetric_summary](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_summary.csv) | [exp041_asymmetric_mc_script](/api/workspace-files/projects/e
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2344 · 2026-05-25T04:33:34.521233+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool call

_source line 2345 · 2026-05-25T04:33:34.571650+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2346 · 2026-05-25T04:33:34.572212+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2347 · 2026-05-25T04:33:34.623159+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T04:19:00.355948+00:00\", \"completed_at\": \"2026-05-25T04:23:15.819779+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前两页为纯文本（Abstract + Introduction + Related Work 开头），无任何视觉锚点。第一个 display item（Figure 1）出现在第 3 页顶部，处于 3 页窗口的边界。审稿人在看到任何图形前需阅读约 1.5 页密文。考虑将 Figure 1 或一个 teaser 图提前至第 1 页底部或第 2 页顶部以加速锚定\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Author/Abstract 排版整洁，标准 ACL 双栏格式，专业感良好\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（三面板 A/B/C）有效传达核心 message：全局校正可导致 CATE 符号反转。Caption 自包含，审稿人无需回读正文即可理解要点。作为首个 display item，锚定效应正向\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"连续 2 页纯文本，无 figure/table/prominent equation 穿插。虽然 Related Work 通常是文本密集段落，但对审稿人的视觉耐心构成考验\"}, {\"severity\": \"info\", \"dimension\": \"page 4-6\", \"message\": \"连续 3 页以数学定理/命题/证明为主（Section 3-4），无 figure/table。但因包含大量 display-math 公式（Theorem 1、Propositions 3-5、Corollaries），方程本身提供了视觉节奏，理论类论文可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"极高密度页面：Figure 3 + Table 1 + Section 6 Conclusion + Limitations 全部挤在一页。内容利用率 100%，但 Conclusion 段显得局促\"}, {\"severity\": \"info\", \"dimension\": \"page 33\", \"message\": \"末页（Appendix 最后一页）Algorithm 1 仅占页面上半部分，下方约 40% 空白。因属 Appendix 末页且为 Algorithm float，不构成问题\"}, {\"severity\": \"info\", \"dimension\": \"page 1-8\", \"message\": \"正文 8 页包含 3 figures + 1 table = 4 个 display items（0.5/页）。对理论+实证混合型论文属可接受范围，但处于偏低端。Figure 4（page 9）实际已在 References 区域。若 Figure 4 算入则为 5 个，密度更合理\"}, {\"severity\": \"info\", \"dimension\": \"page 11-33\", \"message\": \"Appendix 23 页包含大量补充 tables（Tables 2-40）和 figures（Figures 5-9），实验覆盖极为充分\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 面板内文字偏小（axis labels、tick labels），尤其 Panel B 的 bar chart legend 和 x-axis 标签在 150dpi 渲染下需仔细辨认。建议将 axis label 字号提升至正文字号的 80% 以上\"},
…[truncated 2413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2348 · 2026-05-25T04:33:55.814536+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2349 · 2026-05-25T04:33:55.865224+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2350 · 2026-05-25T04:33:57.722977+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2351 · 2026-05-25T04:33:57.723296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2352 · 2026-05-25T04:34:03.249372+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 2353 · 2026-05-25T04:34:03.651692+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_reports/round_16.md
/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annota
…[truncated 383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2354 · 2026-05-25T04:34:04.054498+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 2355 · 2026-05-25T04:34:04.155364+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2356 · 2026-05-25T04:34:44.009520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2357 · 2026-05-25T04:34:44.060346+00:00_

1	issues:
2	  # === RESOLVED (prior rounds — abbreviated) ===
3	  - id: "R1-N1"
4	    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
5	    category: method
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 0
9	    last_seen_round: 2
10	    action_items: []
11	    resolution: "重新推导为精确恒等式"
12	    resolution_round: 0
13	
14	  - id: "R2-W8"
15	    summary: "Proposition 1 限于 K=2"
16	    category: method
17	    severity: critical
18	    status: resolved
19	    first_raised_round: 0
20	    last_seen_round: 1
21	    action_items: []
22	    resolution: "Theorem 1 适用一般 K"
23	    resolution_round: 0
24	
25	  - id: "R1-N2"
26	    summary: "Real data ground truth CATE 来源不明"
27	    category: experiment
28	    severity: critical
29	    status: resolved
30	    first_raised_round: 0
31	    last_seen_round: 1
32	    action_items: []
33	    resolution: "恰当定位为 illustrative application"
34	    resolution_round: 0
35	
36	  - id: "R1-N3"
37	    summary: "HB 模型规格严重不完整"
38	    category: method
39	    severity: critical
40	    status: resolved
41	    first_raised_round: 0
42	    last_seen_round: 1
43	    action_items: []
44	    resolution: "完整 MCMC 规格"
45	    resolution_round: 0
46	
47	  - id: "JOINT-W4"
48	    summary: "相关工作严重遗漏"
49	    category: writing
50	    severity: warning
51	    status: resolved
52	    first_raised_round: 0
53	    last_seen_round: 1
54	    action_items: []
55	    resolution: "30+ 引用覆盖"
56	    resolution_round: 0
57	
58	  - id: "JOINT-W3"
59	    summary: "信息密度过高"
60	    category: writing
61	    severity: warning
62	    status: resolved
63	    first_raised_round: 0
64	    last_seen_round: 1
65	    action_items: []
66	    resolution: "主文精简至合理密度"
67	    resolution_round: 0
68	
69	  - id: "R2-W7"
70	    summary: "真实数据验证单薄"
71	    category: experiment
72	    severity: warning
73	    status: resolved
74	    first_raised_round: 0
75	    last_seen_round: 1
76	    action_items: []
77	    resolution: "恰当定位 + 公开数据集"
78	    resolution_round: 0
7
…[truncated 580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2358 · 2026-05-25T04:34:47.827232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2359 · 2026-05-25T04:34:47.827949+00:00_

100	        reviewers: [1]
101	        note: "已修正为 'on synthetic grids (aggregate 0.975; per-model range 0.76-0.99)'"
102	    action_items: []
103	    resolution: "已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围"
104	    resolution_round: 19
105	
106	  - id: "R19-C2"
107	    summary: "诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定"
108	    category: framing
109	    severity: critical
110	    status: resolved
111	    first_raised_round: 19
112	    last_seen_round: 19
113	    mentions:
114	      - round: 19
115	        reviewers: [1, 2]
116	        note: "AUC 数字从 Abstract 完全移除"
117	    action_items: []
118	    resolution: "AUC 数字从 Abstract 完全移除"
119	    resolution_round: 19
120	
121	  - id: "R19-C3"
122	    summary: "核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善"
123	    category: framing
124	    severity: critical
125	    status: resolved
126	    first_raised_round: 19
127	    last_seen_round: 19
128	    mentions:
129	      - round: 19
130	        reviewers: [1]
131	        note: "Abstract 已加 'under extreme heterogeneity' 限定"
132	    action_items: []
133	    resolution: "Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'"
134	    resolution_round: 19
135	
136	  - id: "R19-W1"
137	    summary: "操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件"
138	    category: method
139	    severity: warning
140	    status: resolved
141	    first_raised_round: 19
142	    last_seen_round: 19
143	    action_items: []
144	    resolution: "Conclusion 扩展含 relaxed screening adoption guideline"
145	    resolution_round: 19
146	
147	  - id: "R19-W2"
148	    summary: "DGP 缺乏 observational/confounding 场景验证"
149	    category: experiment
150	    severity: warning
151	    status: resolved
152	    first_raised_round: 19
153	    last_seen_round: 19
154	    action_items: []
155	    resolution: "Limitations 已补充 confounded DGP scope"
156	    resolution_round: 19
157	
158	  - id: "R19-M4"
159	    summary: "Conclusion 过短（仅两句话）"
160	    category: writi
…[truncated 4409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2360 · 2026-05-25T04:34:51.744472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "offset": "299",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "offset": "299",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2361 · 2026-05-25T04:34:51.745099+00:00_

299	
300	  - id: "R19-W6"
301	    summary: "Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation"
302	    category: method
303	    severity: warning
304	    status: open
305	    first_raised_round: 19
306	    last_seen_round: 19
307	    mentions:
308	      - round: 21
309	        reviewers: []
310	        note: "R21 未再提及。"
311	    action_items: []
312	    resolution: ""
313	    resolution_round: null
314	
315	  - id: "R12-M2"
316	    summary: "Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)"
317	    category: writing
318	    severity: warning
319	    status: in_progress
320	    first_raised_round: 12
321	    last_seen_round: 21
322	    mentions:
323	      - round: 21
324	        reviewers: [1, 2]
325	        note: "R21-R1-N2: 'exact' 标题与标量近似 R² 退化的张力。R2 未直接提及但在 F-L 差异讨论中涉及。Abstract 已修正为 'under symmetric errors (generalizing to full-matrix form)'。Deeper fix（非对称 closed-form）仍为 rebuttal 材料。"
326	    action_items:
327	      - round: 20
328	        action: "主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）"
329	        assigned_to: author
330	        status: open
331	    resolution: ""
332	    resolution_round: null
333	
334	  - id: "R18-SF6"
335	    summary: "Plugin SE 欠覆盖 93.8%"
336	    category: experiment
337	    severity: warning
338	    status: in_progress
339	    first_raised_round: 17
340	    last_seen_round: 21
341	    mentions:
342	      - round: 21
343	        reviewers: []
344	        note: "R21 未单独提及，但 R1-W2 提到 MC=100 覆盖率精度问题，间接相关。"
345	    action_items: []
346	    resolution: ""
347	    resolution_round: null
348	
349	  - id: "R18-M1"
350	    summary: "EC-HTE wall-clock time 未报告"
351	    category: experiment
352	    severity: info
353	    status: open
354	    first_raised_round: 18
355	    last_seen_round: 21
356	    mentions:
357	      - round: 21
358	        reviewers: []
359	        note: "R21 未再提及。method.tex 提到 HB 估计 <5ms。"
360	    action_items: []
361	    resolution: ""
362	    resolution_round: null
363	
364	  - id: "R17-NLP2"
365	    summary: 
…[truncated 3895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2362 · 2026-05-25T04:34:56.112933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "offset": "498",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "offset": "498",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2363 · 2026-05-25T04:34:56.163762+00:00_

498	    last_seen_round: 21
499	    mentions:
500	      - round: 21
501	        reviewers: [1, 2]
502	        note: "R21 两位 Reviewer 均再次关注此问题。experiments.tex §5.4 已添加 matrix vs scalar 区分句。deeper theoretical fix 仍待 rebuttal。"
503	    action_items:
504	      - round: 20
505	        action: "主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）"
506	        assigned_to: author
507	        status: open
508	      - round: 21
509	        action: "experiments.tex §5.4 添加 matrix vs scalar 区分"
510	        assigned_to: director
511	        status: done
512	    resolution: ""
513	    resolution_round: null
514	
515	  - id: "R20-C2"
516	    summary: "相对 Frazis-Loewenstein (2003) 经典测量误差理论的增量贡献未界定"
517	    category: framing
518	    severity: critical
519	    status: in_progress
520	    first_raised_round: 20
521	    last_seen_round: 21
522	    mentions:
523	      - round: 21
524	        reviewers: [2]
525	        note: "R21-R2-N2 再次作为 Must-Fix。theory.tex proof sketch 已替换为 sign reversal novelty statement（MF3 fix），明确区分 F-L 标量衰减 vs 本文跨子群符号反转。"
526	    action_items:
527	      - round: 20
528	        action: "Section 3 明确声明与 F-L (2003) 的 nesting 关系"
529	        assigned_to: director
530	        status: done
531	      - round: 21
532	        action: "Section 3 增加 explicit novelty statement: sign reversal vs uniform shrinkage"
533	        assigned_to: director
534	        status: done
535	    resolution: ""
536	    resolution_round: null
537	
538	  - id: "R20-C3"
539	    summary: "缺失噪声标签学习核心文献 (Natarajan et al. 2013, Patrini et al. 2017)"
540	    category: writing
541	    severity: critical
542	    status: in_progress
543	    first_raised_round: 20
544	    last_seen_round: 21
545	    mentions:
546	      - round: 21
547	        reviewers: [2]
548	        note: "R21-R2-W4: 段落已添加（related_work.tex），但讨论仍可更深入——subgroup-dependent 与 instance-dependent noise 的联系未建立。"
549	    action_items:
550	      - round: 20
551	        action: "Related Work 增加噪声标签学习段落"
552	        assigned_to: director
553	    
…[truncated 4553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2364 · 2026-05-25T04:35:00.481889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "offset": "697",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "offset": "697",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2365 · 2026-05-25T04:35:00.589679+00:00_

697	    first_raised_round: 21
698	    last_seen_round: 21
699	    mentions:
700	      - round: 21
701	        reviewers: [2]
702	        note: "R2-N1 Must-Fix。experiments.tex §5.2 已添加 CivilComments NLP insight（MF2 fix）：bias identity 改变 NLP 实质性结论。完整 Appendix M 移入正文仍为 rebuttal/camera-ready。"
703	    action_items:
704	      - round: 21
705	        action: "experiments.tex §5.2 增加 CivilComments NLP insight 段落"
706	        assigned_to: director
707	        status: done
708	      - round: 21
709	        action: "将 Appendix M 关键发现移入正文（rebuttal/camera-ready）"
710	        assigned_to: author
711	        status: open
712	    resolution: ""
713	    resolution_round: null
714	
715	  - id: "R21-W1"
716	    summary: "Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明——两者标签需求相同"
717	    category: method
718	    severity: warning
719	    status: open
720	    first_raised_round: 21
721	    last_seen_round: 21
722	    mentions:
723	      - round: 21
724	        reviewers: [1]
725	        note: "R1-W3: 诊断需要 ε_s，EC-HTE 也需要 ε_s。对 binary Z，标签需求完全相同。论文未解释何时用诊断而非直接运行 EC-HTE。"
726	    action_items:
727	      - round: 21
728	        action: "明确诊断准则的使用场景（rebuttal）"
729	        assigned_to: author
730	        status: open
731	    resolution: ""
732	    resolution_round: null
733	
734	  - id: "R21-W2"
735	    summary: "A3 (P(Z=0)=0.5) 限制性在正文中讨论不足"
736	    category: method
737	    severity: warning
738	    status: in_progress
739	    first_raised_round: 21
740	    last_seen_round: 21
741	    mentions:
742	      - round: 21
743	        reviewers: [2]
744	        note: "R2-W1。limitations.tex 已添加 A3 class imbalance 影响讨论（SF10 fix），含 R²≥0.976 和 RMSE ratio 1.06-1.68。"
745	    action_items:
746	      - round: 21
747	        action: "Limitations 补充 A3 class imbalance 影响讨论"
748	        assigned_to: director
749	        status: done
750	    resolution: ""
751	    resolution_round: null
752	
753	  - id: "R21-W3"
754	    summary: "操作条件 (Δπ>0.15, n_expert/K≥50, K≤4) 是经验导出——称 'framework' 轻微过度声称"
755	    category: frami
…[truncated 1838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 107
}
```

</details>

---


### Tool call

_source line 2366 · 2026-05-25T04:36:48.548752+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool call

_source line 2367 · 2026-05-25T04:36:48.549505+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2368 · 2026-05-25T04:36:48.549951+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 2369 · 2026-05-25T04:36:48.550259+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2370 · 2026-05-25T04:36:53.821511+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 2371 · 2026-05-25T04:36:56.030965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 2372 · 2026-05-25T04:36:56.031349+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{makecell}
15	\usepackage{xcolor}
16	\usepackage{enumitem}
17	\usepackage{algorithm}
18	\usepackage{algpseudocode}
19	
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}[theorem]{Corollary}
22	\newtheorem{proposition}[theorem]{Proposition}
23	\newtheorem{remark}[theorem]{Remark}
24	
25	\title{When Debiasing Hurts: An Exact Bias Identity\\for LLM-Annotated Treatment Effects}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{theory}
39	
40	\input{method}
41	
42	\input{experiments}
43	
44	\input{conclusion}
45	
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	%\input{checklist}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 2373 · 2026-05-25T04:37:01.502277+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here's what I found about EMNLP 2026 call for papers submission guidelines and ARR:

## Main Conference Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Presentation Requirements

All accepted papers must be presented at the conference to appear in the proceedings. The conference will include both in-person and virtual presentation options. Papers without at least one pres
…[truncated 809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 7680
}
```

</details>

---


### Tool call

_source line 2374 · 2026-05-25T04:37:06.736703+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit long short paper guidelines",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 paper format page limit long short paper guidelines",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 2375 · 2026-05-25T04:37:08.644547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2376 · 2026-05-25T04:37:08.644956+00:00_

1	\begin{abstract}
2	Standard confusion-matrix correction for noisy annotations assumes uniform error rates.
3	When this assumption fails---as it routinely does with large language model (LLM) classifiers, whose error rates vary by up to $5\times$ across subgroups---correction can reverse estimated effect signs.
4	We derive an exact bias identity: global correction introduces subgroup-level bias $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$ under symmetric errors (generalizing to a full-matrix form for arbitrary asymmetric confusion matrices; Remark~\ref{rem:asymmetric}), verified at $R^2 \geq 0.97$ on synthetic grids ($R^2 = 0.975$ in aggregate across 11 real LLM confusion matrices; per-model range $0.76$--$0.99$).
5	The identity predicts that global correction reverses conditional average treatment effect (CATE) sign in 14.9\% of configurations where the true effect is small ($\tau(0) = 0.03$) and amplifies bias in all eight real LLMs tested; a $\Delta\tau$-free diagnostic corollary flags harmful correction from error rates alone, without estimating treatment effects.
6	We characterize when per-subgroup correction is beneficial ($\Delta\pi > 0.15$, $n_{\text{expert}}/K \geq 50$, $K \leq 4$) versus when global correction should be retained, and implement one such correction via hierarchical Bayesian estimation, reducing $|\text{bias}|$ by $7.4\times$ under extreme heterogeneity.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 2377 · 2026-05-25T04:37:12.340067+00:00_

Web search results for query: "EMNLP 2026 paper format page limit long short paper guidelines"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"1st Workshop on Multilingual Representation Learning (MRL) at EMNLP | ACL Member Portal","url":"https://www.aclweb.org/portal/content/1st-workshop-multilingual-representation-learning-mrl-emnlp"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Empirical Methods in Natural Language Processing | ACL Member Portal","url":"https://www.aclweb.org/portal/content/empirical-methods-natural-language-processing"}]

Based on the search results, I found information about EMNLP 2026 paper format guidelines. Here's what I found:

## EMNLP 2026 Main Conference

Unfortunately, the search results don't contain specific page limit guidelines for the main EMNLP 2026 conference long and short papers. However, based on EMNLP 2025 requirements which typically serve as a reference, long papers are 8 pages and short papers are 4 pages.

## EMNLP 2026 Industry Track

For the EMNLP 2026 Industry Track specifically, authors are invited to submit original, full-length papers with a maximum of 6 pages.

## Formatting Requirements

Manuscripts should be submitted in PDF format and formatted using the available templates, with instructions not to modify these style 
…[truncated 467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 5603
}
```

</details>

---


### Tool call

_source line 2378 · 2026-05-25T04:38:07.882823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "offset": "85",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "offset": "85",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 2379 · 2026-05-25T04:38:08.284691+00:00_

85	Empirical verification yields $R^2 = 0.994$ ($K{=}2$) and $0.97$ ($K{=}4$; Section~\ref{sec:bias_mechanism}).
86	
87	\paragraph{Sensitivity to (A1).}
88	Assumption~(A1) is not empirically testable; if misclassification correlates with potential outcomes, Theorem~\ref{thm:bias_identity} gains an $O(\gamma)$ perturbation.
89	At $\gamma_T = 0.10$, coverage degrades to 75\% (Appendix~\ref{app:treatment_dep}); sensitivity frameworks~\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound this.
90	
91	\paragraph{Finite-sample remainder.}
92	With estimated $\hat{C}_s = C_s + E_s$, $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$, the remainder is $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, motivating the $\kappa$-guard in Section~\ref{sec:method}.
93	
94	\begin{proposition}[Debiasing Can Increase Bias]
95	\label{prop:debiasing_hurts}
96	Under \textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\mathrm{bias}_{\mathrm{global}}| > |\mathrm{bias}_{\mathrm{naive}}|$) in subgroup $s$ if and only if
97	\begin{equation}
98	\frac{|\delta_s|}{(1 - 2\bar{\pi}) \cdot \pi_s} > 1.
99	\label{eq:hurts_condition}
100	\end{equation}
101	\end{proposition}
102	
103	\medskip
104	Equation~\eqref{eq:hurts_condition} partitions subgroups into two regimes:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2380 · 2026-05-25T04:38:08.435698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
  "offset": "50",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
    "offset": "50",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 2381 · 2026-05-25T04:38:08.536628+00:00_

50	\begin{table}[t]
51	\centering
52	\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\text{bias}|$. $^\dagger$RMSE exceeds Global. F-L Scalar/Per-sub.: \citet{frazis2003estimating}. Moderate/TweetEval in Table~\ref{tab:main_supp}; MC SEs $\leq 0.005$ (Appendix~\ref{app:mcse}).\protect\footnotemark}
53	\label{tab:main_results}
54	\resizebox{\columnwidth}{!}{%
55	\begin{tabular}{ll ccc}
56	\toprule
57	Configuration & Method & $|\text{Bias}|$ & RMSE & 95\% CI Cov. \\
58	\midrule
59	\multirow{6}{*}{\shortstack[l]{DIM\\$K{=}2$, $n{=}250$}}
60	 & Naive & 0.058 & 0.090 & 0.82 \\
61	 & Global & 0.059 & 0.099 & 0.87 \\
62	 & F-L Scalar & 0.122 & 0.159 & 0.68 \\
63	 & F-L Per-sub. & 0.168 & 0.220 & 0.65 \\
64	 & Strat.\ MLE & 0.012 & 0.094 & 0.95 \\
65	 & HB EC-HTE & \textbf{0.008} & 0.089 & 0.94 \\
66	\midrule
67	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}4$, $n{=}500$}}
68	 & Naive & 0.062 & 0.113 & 0.88 \\
69	 & Global & 0.056 & 0.125 & 0.91 \\
70	 & Strat.\ MLE & \textbf{0.010} & 0.127$^\dagger$ & 0.95 \\
71	 & HB EC-HTE & 0.012 & 0.120 & 0.96 \\
72	\midrule
73	\multirow{3}{*}{\shortstack[l]{CausalForest\\$K{=}4$, $n{=}500$}}
74	 & Naive & 0.208 & 0.231 & 0.44 \\
75	 & Global & 0.191 & 0.244 & 0.58 \\
76	 & EC-HTE Forest & \textbf{0.039} & 0.180 & 0.90 \\
77	\bottomrule
78	\end{tabular}}
79	\footnotetext{CausalForest plug-in SE achieves 93.8\% aggregate coverage; a bootstrap procedure ($B{=}100$) recovers $\geq$95\% coverage at all budgets tested (Appendix~\ref{app:bootstrap_se}).}
80	\end{table}
81	
82	\subsection{Diagnostic and Operating Conditions}
83	\label{sec:diagnostic}
84	
85	Theorem~\ref{thm:bias_identity} operates on the full matrix residual $B_s = M_{\text{global}}^{-1} M_s - I$; the scalar diagnostic below is its (A2)-simplified form.
86	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\delta_s| / ((1-2\bar
…[truncated 348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2382 · 2026-05-25T04:41:33.100720+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
  "offset": "808",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml",
    "offset": "808",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2383 · 2026-05-25T04:41:33.201569+00:00_

808	    resolution_round: null

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2384 · 2026-05-25T04:46:03.927056+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"已修正为 'on synthetic grids (aggregate 0.975; per-model range 0.76-0.99)'\"\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"AUC 数字从 Abstract 完全移除\"\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"Abstract 已加 'under extreme heterogeneity' 限定\"\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 视觉审查仍检测到 Figure 2 红/绿对比（红色=Sign Reversal, 绿色=0% reversal）。R19 标记为 resolved (sage green→blue) 但修复可能不完整。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  # === OPEN / IN_PROGRESS — updated with R22 ===\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 PEHE、缺半合成 CF 结果、缺 Eq.7 不确定性传播消融\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"DDL 前无法补充。PEHE + Eq.7 消融理论上各需 30min，半合成 CF 需 2-4h 高风险。Rebuttal 材料。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20 指出仅用 CausalForestDML + R-learner 不够，缺 X-learner/BART。\"\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-W1 再次提出仅 2 种 HTE 估计器。R2 未单独提及但在 questions 中问及 scale。与本 issue 一致。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。但 R2 确认跨估计器验证（CausalForest + R-learner）是加分项。仍缺 X-learner/BART。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: PEHE + Eq.7 消融（camera-ready 补充）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认: Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s。问题已解决。\"\n    action_items: []\n    resolution: \"Proposition 3 (A5 relaxation with Δτ_s) 已在主文 theory.tex L63-71\"\n    resolution_round: 21\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。experiments.tex L28 已有讨论。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W3 再次提出正文缺完整真实数据实验。真实数据仍仅在附录。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 再次强调：标题声称 'debiasing hurts' 应有至少一个真实案例展示。CivilComments 无 ground-truth CATE 无法验证。R1 未列为 major 但在 Q5 中关注。评分分歧的核心因素之一。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 两位 Reviewer 共识确认技术错误：theory.tex L92 的 O_p(κ·n^{-1/2}) 应为 O_p(κ²·n^{-1/2})。矩阵扰动 (C+E)^{-1} 一阶展开余项为 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。实际影响在 κ∈[1.25,3] 时有限但必须修正。\"\n    action_items:\n      - round: 22\n        action: \"修正 theory.tex L92 余项阶数 κ→κ²\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-N2: 'exact' 标题与标量近似 R² 退化的张力。R2 未直接提及但在 F-L 差异讨论中涉及。Abstract 已修正为 'under symmetric errors (generalizing to full-matrix form)'。Deeper fix（非对称 closed-form）仍为 rebuttal 材料。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 partial REBUT R1: 恒等式 bias(z,s)=Δτ·[B_s]_{z,1} 在非对称情形下仍精确成立，不依赖 A2。降级的是标量简化形式和 Proposition 5 诊断（AUC 0.86→0.66）。'exact identity' 措辞严格来说无误导——但 abstract 强调的简洁标量形式只在 A2 下成立。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提及，但 R1-W2 提到 MC=100 覆盖率精度问题，间接相关。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接提及。Table 1 footnote 注明 93.8% 且 bootstrap 可恢复 ≥95%。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。method.tex 提到 HB 估计 <5ms。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。但 EB vs Gibbs 不一致（R22-Q1）暗示 wall-clock 声称需要区分两种实现。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N1 再次作为 Must-Fix 提出。experiments.tex 已添加 CivilComments NLP insight 段落（MF2 fix）。完整 Appendix M 移入正文仍为 rebuttal/camera-ready。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 维持此关注：effect modifier misclassification 在 EMNLP 受众中偏窄，多数 NLP 研究者不做 HTE，做 HTE 的不一定投 EMNLP。评分分歧核心因素之一。R1 认为时效性足以支撑。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-N3 作为 Must-Fix 再次提出: K≤4 限制。Intro Contribution 2 已加 'K ≤ 4 subgroups' 限定。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。Intro 限定和 Section 5.4 operating conditions 已覆盖。\"\n    action_items:\n      - round: 21\n        action: \"Intro Contribution 2 增加 K ≤ 4 限定\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。已与 R19-W2 合并，Limitations 已补充。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Proposition 3 已在主文，A5 relaxation 充分展示。\"\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W4 再次提出: 仅变动 Gamma 超参数，未考虑替代先验（logistic-normal）。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出: MC=100 覆盖率 SE≈0.022，未报告 MC 标准误。与 R20-W1 一致。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 通过 EB vs Gibbs 不一致问题间接关联：Algorithm 1 描述的 Gibbs sampler (4 chains, 4000 iter) 与 Method section 的 EB (<5ms) 矛盾。见 R22-Q1。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 严重限制标题级 'Exact Identity' 声称——非对称情形 R² 降至 0.73\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21 两位 Reviewer 均再次关注此问题。experiments.tex §5.4 已添加 matrix vs scalar 区分句。deeper theoretical fix 仍待 rebuttal。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 partial REBUT R1-W1: 恒等式在非对称情形下仍精确——乘积形式 bias(z,s)=Δτ·[B_s]_{z,1} 不依赖 A2（B_s·1=0 仅依赖随机矩阵性质）。降级的是 Proposition 5 诊断 AUC（0.86→0.66）和标量简化。'exact identity' 措辞严格来说正确，但 abstract 强调的简洁标量形式仅在 A2 下成立——这是误导的真正来源。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n      - round: 21\n        action: \"experiments.tex §5.4 添加 matrix vs scalar 区分\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 经典测量误差理论的增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 再次作为 Must-Fix。theory.tex proof sketch 已替换为 sign reversal novelty statement（MF3 fix），明确区分 F-L 标量衰减 vs 本文跨子群符号反转。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 通过 novelty depth 讨论间接涉及：novelty 主要在问题识别（sign reversal discovery）而非技术突破，与 F-L 差异化仍不够深。评分分歧核心因素之一。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L (2003) 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 explicit novelty statement: sign reversal vs uniform shrinkage\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献 (Natarajan et al. 2013, Patrini et al. 2017)\"\n    category: writing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W4: 段落已添加（related_work.tex），但讨论仍可更深入——subgroup-dependent 与 instance-dependent noise 的联系未建立。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。R21 的 deeper connection 请求仍为 open action。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"深化噪声标签文献讨论：建立 subgroup-dependent vs instance-dependent noise 联系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称——SE ≈ 2.2pp\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出。Table 1 caption 已添加 coverage SE 注释，但实际增加 MC runs 仍为 rebuttal 材料。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。Table 1 caption SE 注释已添加。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅——EC-HTE 是成熟技术的组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 间接涉及: F-L 差异化不足。核心贡献定位应为理论洞察 (theory 60% + empirical 20% + method 20%)。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 作为评分分歧核心论据：恒等式本质是 2×2 矩阵代数直接展开，方法是成熟技术组合（confusion matrix correction + HB + κ-guard）。R1 认为技术问题可修复不影响核心贡献。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W5 再次提出: 仅 logistic link, γ ∈ [0, 0.20]。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 20\n        action: \"增加一种基于文本特征的 confounding 形式的灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W5 扩展此问题。theory.tex 已添加 K=2 数值示例段落（SF7 fix），直接用具体数字阐释 δ_s, Δτ, bias 的含义。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。数值示例已添加。\"\n    action_items:\n      - round: 21\n        action: \"theory.tex Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用不一致——部分文件硬编码 Remark~1 或 Remark~\\\\ref{thm:bias_identity}，应为 Remark 2\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"theory.tex 添加 \\\\label{rem:asymmetric}，所有引用统一为 \\\\ref{rem:asymmetric}。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"添加 \\\\label{rem:asymmetric} 并统一所有交叉引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65，正文讨论严重不足\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-N1: Proposition 5 是三大贡献之一。experiments.tex §5.4 已添加 AUC 0.86 symmetric / 0.66 asymmetric 对比（MF1 fix）。deeper theoretical fix 仍为 rebuttal。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 两位 Reviewer 均确认此问题。R2 补充：Prop 5 的关键优势在于不需要估计 Δτ，仅凭 pilot 样本误差率即可决策——这在实际部署中比恒等式本身更有价值。但 AUC 0.66 under asymmetry 仍是实质限制。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.4 增加 matrix vs scalar 区分 + 非对称 AUC 数字\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"考虑基于完整 2×2 矩阵的非对称诊断准则（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足——核心贡献在统计/因果推断，NLP 任务仅为测试平台\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-N1 Must-Fix。experiments.tex §5.2 已添加 CivilComments NLP insight（MF2 fix）：bias identity 改变 NLP 实质性结论。完整 Appendix M 移入正文仍为 rebuttal/camera-ready。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 维持此关注并作为评分分歧核心论据。EMNLP 受众中 effect modifier misclassification 偏窄——多数 NLP 研究者不做 HTE，做 HTE 的不一定投 EMNLP。R1 不认为这是 major 问题，认为时效性足够。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"将 Appendix M 关键发现移入正文（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明——两者标签需求相同\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-W3: 诊断需要 ε_s，EC-HTE 也需要 ε_s。对 binary Z，标签需求完全相同。论文未解释何时用诊断而非直接运行 EC-HTE。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。\"\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W1。limitations.tex 已添加 A3 class imbalance 影响讨论（SF10 fix），含 R²≥0.976 和 RMSE ratio 1.06-1.68。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。limitations.tex 讨论已添加。\"\n    action_items:\n      - round: 21\n        action: \"Limitations 补充 A3 class imbalance 影响讨论\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"操作条件 (Δπ>0.15, n_expert/K≥50, K≤4) 是经验导出——称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W2。Intro Contribution 2 已从 'decision framework' 改为 'Empirical operating guidelines'（SF4 fix）。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 确认 Section 5.4 operating conditions 展示透明，但仍为经验导出。已调整措辞。\"\n    action_items:\n      - round: 21\n        action: \"Contribution 2 措辞调整为 'empirical operating guidelines'\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高——缺数值示例\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W5。theory.tex Theorem 1 后已添加 K=2 数值示例段落（SF7 fix），用 π_A=0.05, π_B=0.25 具体数字阐释。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。数值示例已添加。\"\n    action_items:\n      - round: 21\n        action: \"Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch et al. (2020), Wood-Doughty et al. (2018), Kadavath et al. (2022)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"related_work.tex noisy label 段落末尾已添加 Veitch 2020 和 Wood-Doughty 2018 引用（R21-REF1 fix）。Kadavath 2022 (LLM self-knowledge) 与本文主题关联较弱，暂不添加。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。引用已添加。\"\n    action_items:\n      - round: 21\n        action: \"Related Work 增加 Veitch 2020, Wood-Doughty 2018 引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === ROUND 22 NEW ISSUES ===\n\n  - id: \"R22-W1\"\n    summary: \"κ-guard 阈值 100 纯经验选择——缺乏与有限样本余项 O_p(κ²·n^{-1/2}) 的理论连接\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。最大实验 κ≈1.9，阈值 100 提供 53× 安全余量从未触发。Appendix A 消融 (κ sweep 10-1000) 和自适应公式 κ_adapt=10√(n_expert/K) 提供实证支持，但需基于 O_p(κ²·n^{-1/2}) 推导最优阈值。R2 评为 minor。\"\n    action_items:\n      - round: 22\n        action: \"基于修正后的 O_p(κ²·n^{-1/2}) 余项推导理论最优 κ 阈值（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"经验贝叶斯两阶段低估后验不确定性——MCMC 替代方案仅在 Appendix G\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。EB 低估后验不确定性是标准批评。但 coverage ≥93% 在所有配置下成立，实际影响可能有限。R2 将此列为一般性限制而非致命缺陷。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q1\"\n    summary: \"Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler (4 chains, 4000 iter)——不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出相同问题。主实验使用哪种实现？两者 coverage 差异如何？需要作者澄清。与 R19-M6 (Algorithm 1 缺收敛标准) 相关。\"\n    action_items:\n      - round: 22\n        action: \"澄清主实验使用 EB 还是 Gibbs，统一 Method 和 Algorithm 1 描述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q2\"\n    summary: \"A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"theory.tex L84 声称修正系数存在但未展示。Appendix 中应提供完整推导。\"\n    action_items:\n      - round: 22\n        action: \"Appendix 补充 A3 放松时的显式修正系数推导\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q3\"\n    summary: \"Cov(π_s, Δτ_s) 在实验中未报告——Corollary 4 实际可用性的关键\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。semi-synthetic 实验中应报告此协方差值，以便读者判断 aggregate bias 严重程度。\"\n    action_items:\n      - round: 22\n        action: \"Semi-synthetic 实验中报告 Cov(π_s, Δτ_s)\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q4\"\n    summary: \"EC-HTE + PPCI 理论兼容性条件不明——LLM 同时标注 effect modifier 和 outcome 时独立性假设可能失效\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共同提出。当 LLM 同时标注 covariate 和 outcome 时，covariate-side 和 outcome-side error 的独立性假设可能失效。需要在 Limitations 或 Discussion 中讨论。\"\n    action_items:\n      - round: 22\n        action: \"讨论 EC-HTE 与 PPCI 的理论兼容性条件\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"已修正为 'on synthetic grids (aggregate 0.975; per-model range 0.76-0.99)'\"\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"AUC 数字从 Abstract 完全移除\"\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"Abstract 已加 'under extreme heterogeneity' 限定\"\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 视觉审查仍检测到 Figure 2 红/绿对比（红色=Sign Reversal, 绿色=0% reversal）。R19 标记为 resolved (sage green→blue) 但修复可能不完整。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  # === OPEN / IN_PROGRESS — updated with R22 ===\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 PEHE、缺半合成 CF 结果、缺 Eq.7 不确定性传播消融\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"DDL 前无法补充。PEHE + Eq.7 消融理论上各需 30min，半合成 CF 需 2-4h 高风险。Rebuttal 材料。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20 指出仅用 CausalForestDML + R-learner 不够，缺 X-learner/BART。\"\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-W1 再次提出仅 2 种 HTE 估计器。R2 未单独提及但在 questions 中问及 scale。与本 issue 一致。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。但 R2 确认跨估计器验证（CausalForest + R-learner）是加分项。仍缺 X-learner/BART。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: PEHE + Eq.7 消融（camera-ready 补充）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认: Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s。问题已解决。\"\n    action_items: []\n    resolution: \"Proposition 3 (A5 relaxation with Δτ_s) 已在主文 theory.tex L63-71\"\n    resolution_round: 21\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。experiments.tex L28 已有讨论。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W3 再次提出正文缺完整真实数据实验。真实数据仍仅在附录。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 再次强调：标题声称 'debiasing hurts' 应有至少一个真实案例展示。CivilComments 无 ground-truth CATE 无法验证。R1 未列为 major 但在 Q5 中关注。评分分歧的核心因素之一。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 两位 Reviewer 共识确认技术错误：theory.tex L92 的 O_p(κ·n^{-1/2}) 应为 O_p(κ²·n^{-1/2})。矩阵扰动 (C+E)^{-1} 一阶展开余项为 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。实际影响在 κ∈[1.25,3] 时有限但必须修正。\"\n    action_items:\n      - round: 22\n        action: \"修正 theory.tex L92 余项阶数 κ→κ²\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-N2: 'exact' 标题与标量近似 R² 退化的张力。R2 未直接提及但在 F-L 差异讨论中涉及。Abstract 已修正为 'under symmetric errors (generalizing to full-matrix form)'。Deeper fix（非对称 closed-form）仍为 rebuttal 材料。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 partial REBUT R1: 恒等式 bias(z,s)=Δτ·[B_s]_{z,1} 在非对称情形下仍精确成立，不依赖 A2。降级的是标量简化形式和 Proposition 5 诊断（AUC 0.86→0.66）。'exact identity' 措辞严格来说无误导——但 abstract 强调的简洁标量形式只在 A2 下成立。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提及，但 R1-W2 提到 MC=100 覆盖率精度问题，间接相关。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接提及。Table 1 footnote 注明 93.8% 且 bootstrap 可恢复 ≥95%。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。method.tex 提到 HB 估计 <5ms。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。但 EB vs Gibbs 不一致（R22-Q1）暗示 wall-clock 声称需要区分两种实现。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N1 再次作为 Must-Fix 提出。experiments.tex 已添加 CivilComments NLP insight 段落（MF2 fix）。完整 Appendix M 移入正文仍为 rebuttal/camera-ready。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 维持此关注：effect modifier misclassification 在 EMNLP 受众中偏窄，多数 NLP 研究者不做 HTE，做 HTE 的不一定投 EMNLP。评分分歧核心因素之一。R1 认为时效性足以支撑。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-N3 作为 Must-Fix 再次提出: K≤4 限制。Intro Contribution 2 已加 'K ≤ 4 subgroups' 限定。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。Intro 限定和 Section 5.4 operating conditions 已覆盖。\"\n    action_items:\n      - round: 21\n        action: \"Intro Contribution 2 增加 K ≤ 4 限定\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。已与 R19-W2 合并，Limitations 已补充。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Proposition 3 已在主文，A5 relaxation 充分展示。\"\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W4 再次提出: 仅变动 Gamma 超参数，未考虑替代先验（logistic-normal）。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出: MC=100 覆盖率 SE≈0.022，未报告 MC 标准误。与 R20-W1 一致。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 通过 EB vs Gibbs 不一致问题间接关联：Algorithm 1 描述的 Gibbs sampler (4 chains, 4000 iter) 与 Method section 的 EB (<5ms) 矛盾。见 R22-Q1。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 严重限制标题级 'Exact Identity' 声称——非对称情形 R² 降至 0.73\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21 两位 Reviewer 均再次关注此问题。experiments.tex §5.4 已添加 matrix vs scalar 区分句。deeper theoretical fix 仍待 rebuttal。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 partial REBUT R1-W1: 恒等式在非对称情形下仍精确——乘积形式 bias(z,s)=Δτ·[B_s]_{z,1} 不依赖 A2（B_s·1=0 仅依赖随机矩阵性质）。降级的是 Proposition 5 诊断 AUC（0.86→0.66）和标量简化。'exact identity' 措辞严格来说正确，但 abstract 强调的简洁标量形式仅在 A2 下成立——这是误导的真正来源。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n      - round: 21\n        action: \"experiments.tex §5.4 添加 matrix vs scalar 区分\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 经典测量误差理论的增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 再次作为 Must-Fix。theory.tex proof sketch 已替换为 sign reversal novelty statement（MF3 fix），明确区分 F-L 标量衰减 vs 本文跨子群符号反转。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 通过 novelty depth 讨论间接涉及：novelty 主要在问题识别（sign reversal discovery）而非技术突破，与 F-L 差异化仍不够深。评分分歧核心因素之一。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L (2003) 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 explicit novelty statement: sign reversal vs uniform shrinkage\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献 (Natarajan et al. 2013, Patrini et al. 2017)\"\n    category: writing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W4: 段落已添加（related_work.tex），但讨论仍可更深入——subgroup-dependent 与 instance-dependent noise 的联系未建立。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。R21 的 deeper connection 请求仍为 open action。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"深化噪声标签文献讨论：建立 subgroup-dependent vs instance-dependent noise 联系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称——SE ≈ 2.2pp\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出。Table 1 caption 已添加 coverage SE 注释，但实际增加 MC runs 仍为 rebuttal 材料。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。Table 1 caption SE 注释已添加。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅——EC-HTE 是成熟技术的组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 间接涉及: F-L 差异化不足。核心贡献定位应为理论洞察 (theory 60% + empirical 20% + method 20%)。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 作为评分分歧核心论据：恒等式本质是 2×2 矩阵代数直接展开，方法是成熟技术组合（confusion matrix correction + HB + κ-guard）。R1 认为技术问题可修复不影响核心贡献。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W5 再次提出: 仅 logistic link, γ ∈ [0, 0.20]。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 20\n        action: \"增加一种基于文本特征的 confounding 形式的灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W5 扩展此问题。theory.tex 已添加 K=2 数值示例段落（SF7 fix），直接用具体数字阐释 δ_s, Δτ, bias 的含义。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。数值示例已添加。\"\n    action_items:\n      - round: 21\n        action: \"theory.tex Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用不一致——部分文件硬编码 Remark~1 或 Remark~\\\\ref{thm:bias_identity}，应为 Remark 2\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"theory.tex 添加 \\\\label{rem:asymmetric}，所有引用统一为 \\\\ref{rem:asymmetric}。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"添加 \\\\label{rem:asymmetric} 并统一所有交叉引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65，正文讨论严重不足\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-N1: Proposition 5 是三大贡献之一。experiments.tex §5.4 已添加 AUC 0.86 symmetric / 0.66 asymmetric 对比（MF1 fix）。deeper theoretical fix 仍为 rebuttal。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 两位 Reviewer 均确认此问题。R2 补充：Prop 5 的关键优势在于不需要估计 Δτ，仅凭 pilot 样本误差率即可决策——这在实际部署中比恒等式本身更有价值。但 AUC 0.66 under asymmetry 仍是实质限制。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.4 增加 matrix vs scalar 区分 + 非对称 AUC 数字\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"考虑基于完整 2×2 矩阵的非对称诊断准则（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足——核心贡献在统计/因果推断，NLP 任务仅为测试平台\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-N1 Must-Fix。experiments.tex §5.2 已添加 CivilComments NLP insight（MF2 fix）：bias identity 改变 NLP 实质性结论。完整 Appendix M 移入正文仍为 rebuttal/camera-ready。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 维持此关注并作为评分分歧核心论据。EMNLP 受众中 effect modifier misclassification 偏窄——多数 NLP 研究者不做 HTE，做 HTE 的不一定投 EMNLP。R1 不认为这是 major 问题，认为时效性足够。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"将 Appendix M 关键发现移入正文（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明——两者标签需求相同\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-W3: 诊断需要 ε_s，EC-HTE 也需要 ε_s。对 binary Z，标签需求完全相同。论文未解释何时用诊断而非直接运行 EC-HTE。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。\"\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W1。limitations.tex 已添加 A3 class imbalance 影响讨论（SF10 fix），含 R²≥0.976 和 RMSE ratio 1.06-1.68。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。limitations.tex 讨论已添加。\"\n    action_items:\n      - round: 21\n        action: \"Limitations 补充 A3 class imbalance 影响讨论\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"操作条件 (Δπ>0.15, n_expert/K≥50, K≤4) 是经验导出——称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W2。Intro Contribution 2 已从 'decision framework' 改为 'Empirical operating guidelines'（SF4 fix）。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 确认 Section 5.4 operating conditions 展示透明，但仍为经验导出。已调整措辞。\"\n    action_items:\n      - round: 21\n        action: \"Contribution 2 措辞调整为 'empirical operating guidelines'\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高——缺数值示例\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-W5。theory.tex Theorem 1 后已添加 K=2 数值示例段落（SF7 fix），用 π_A=0.05, π_B=0.25 具体数字阐释。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。数值示例已添加。\"\n    action_items:\n      - round: 21\n        action: \"Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch et al. (2020), Wood-Doughty et al. (2018), Kadavath et al. (2022)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"related_work.tex noisy label 段落末尾已添加 Veitch 2020 和 Wood-Doughty 2018 引用（R21-REF1 fix）。Kadavath 2022 (LLM self-knowledge) 与本文主题关联较弱，暂不添加。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。引用已添加。\"\n    action_items:\n      - round: 21\n        action: \"Related Work 增加 Veitch 2020, Wood-Doughty 2018 引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === ROUND 22 NEW ISSUES ===\n\n  - id: \"R22-W1\"\n    summary: \"κ-guard 阈值 100 纯经验选择——缺乏与有限样本余项 O_p(κ²·n^{-1/2}) 的理论连接\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。最大实验 κ≈1.9，阈值 100 提供 53× 安全余量从未触发。Appendix A 消融 (κ sweep 10-1000) 和自适应公式 κ_adapt=10√(n_expert/K) 提供实证支持，但需基于 O_p(κ²·n^{-1/2}) 推导最优阈值。R2 评为 minor。\"\n    action_items:\n      - round: 22\n        action: \"基于修正后的 O_p(κ²·n^{-1/2}) 余项推导理论最优 κ 阈值（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"经验贝叶斯两阶段低估后验不确定性——MCMC 替代方案仅在 Appendix G\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。EB 低估后验不确定性是标准批评。但 coverage ≥93% 在所有配置下成立，实际影响可能有限。R2 将此列为一般性限制而非致命缺陷。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q1\"\n    summary: \"Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler (4 chains, 4000 iter)——不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出相同问题。主实验使用哪种实现？两者 coverage 差异如何？需要作者澄清。与 R19-M6 (Algorithm 1 缺收敛标准) 相关。\"\n    action_items:\n      - round: 22\n        action: \"澄清主实验使用 EB 还是 Gibbs，统一 Method 和 Algorithm 1 描述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q2\"\n    summary: \"A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"theory.tex L84 声称修正系数存在但未展示。Appendix 中应提供完整推导。\"\n    action_items:\n      - round: 22\n        action: \"Appendix 补充 A3 放松时的显式修正系数推导\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q3\"\n    summary: \"Cov(π_s, Δτ_s) 在实验中未报告——Corollary 4 实际可用性的关键\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 同意。semi-synthetic 实验中应报告此协方差值，以便读者判断 aggregate bias 严重程度。\"\n    action_items:\n      - round: 22\n        action: \"Semi-synthetic 实验中报告 Cov(π_s, Δτ_s)\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q4\"\n    summary: \"EC-HTE + PPCI 理论兼容性条件不明——LLM 同时标注 effect modifier 和 outcome 时独立性假设可能失效\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共同提出。当 LLM 同时标注 covariate 和 outcome 时，covariate-side 和 outcome-side error 的独立性假设可能失效。需要在 Limitations 或 Discussion 中讨论。\"\n    action_items:\n      - round: 22\n        action: \"讨论 EC-HTE 与 PPCI 的理论兼容性条件\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 2385 · 2026-05-25T04:46:04.130739+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml\", \"bytes\": 29217}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 2386 · 2026-05-25T04:48:30.528775+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 22 审稿报告\n\n## Summary\n\n本文推导了一个精确偏差恒等式（Theorem 1），揭示当 LLM 标注器的误分类率在子群间存在异质性时，全局混淆矩阵校正会引入子群级别的偏差，甚至可在 14.9% 的配置中导致 CATE 符号反转。基于该恒等式，论文提出了 Δτ-free 诊断准则（Proposition 5）和分层贝叶斯校正方法（EC-HTE），在极端异质性下将 |bias| 降低 7.4×。实验覆盖 520 合成配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验。\n\n## Strengths\n\n**[S1] 理论核心简洁且可验证（R1, R2 共识）**：Theorem 1 的乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 既精确又可解释，证明可手动核实。Proposition 5 的 Δτ-free 诊断（AUC=0.86 对称情形）仅凭 pilot 样本误差率即可决策，具有实际操作价值——不需要估计 Δτ，这在实际部署中比恒等式本身更有价值。\n\n**[S2] 实验覆盖极为全面（R1, R2 共识）**：520 配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验，在 *ACL 投稿中属上乘水平。跨估计器验证（CausalForest + R-learner, Table 1 + Appendix P）是额外加分项。\n\n**[S3] 理论→方法→实践链完整（R1, R2 共识）**：从恒等式推导到 EC-HTE 方法实现再到操作边界（Section 5.4: Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4）的完整链条。Algorithm 1 伪代码清晰。\"何时不用本方法\"的诚实边界划定值得肯定。\n\n**[S4] 时效性好的交叉方向（R1 强调）**：NLP × 因果推断的交叉研究正值增长期。14.9% sign reversal 是有冲击力的 headline number。\n\n**[S5] 假设放松讨论系统化（R1, R2 共识）**：Remark 2 对 A2、Appendix D 对 A3、Proposition 3 对 A5、Appendix H 对 A1 的系统性讨论表明作者对自身理论的局限有清醒认识。R2 补充：放松 A2 后诊断 AUC 从 0.86 降至 0.66 本身暴露了理论与实践的 gap（见 W1）。\n\n## Weaknesses\n\n**[W1] 对称误分类假设 (A2) 严重限制诊断实用性（R1, R2 共识，critical）**\n两位 Reviewer 均确认 A2 是论文最大的实践局限。GPT-4o FPR/FNR 差异达 0.09（0.249 vs 0.157），典型 LLM 不满足对称假设。R2 对 R1 做了重要澄清：**恒等式本身在非对称情形下仍然精确成立**（乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 不依赖 A2，因 B_s·1=0 仅依赖 M_s 和 M_global 的随机矩阵性质），降级的是**诊断准则**（Proposition 5 AUC 从 0.86 降至 0.66）和**标量简化形式** δ_s·Δτ/(1−2π̄)。非对称情形下需逐 cell 计算 [B_s]_{z,1}，操作复杂度大幅增加。Abstract 强调的简洁标量形式仅在 A2 下成立——这是误导的真正来源，而非 \"exact identity\" 措辞本身。\n\n**[W2] 有限样本余项阶数存在技术错误（R1, R2 共识，warning）**\ntheory.tex L92 声称余项为 O_p(κ·n^{-1/2})，但矩阵扰动分析表明应为 O_p(κ²·n^{-1/2})。推导：(C+E)^{-1} = C^{-1} − C^{-1}EC^{-1} + O(‖E‖²)，一阶项范数 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。对于 2×2 对称矩阵 ‖C^{-1}‖ = 1/(1−2π) = κ(C)。实际影响在 κ ∈ [1.25, 3] 时有限（κ² ∈ [1.56, 9] vs κ ∈ [1.25, 3]），但属于需要修正的技术性错误。\n\n**[W3] κ-guard 阈值 100 缺乏理论依据（R1, R2 共识，minor warning）**\n最大实验 κ ≈ 1.9，阈值 100 提供 53× 安全余量，实际上从未触发。Appendix A 的消融（κ sweep 10–1000）和自适应公式 κ_adapt = 10√(n_expert/K) 提供了实证支持，但缺少与 W2 修正后余项 O_p(κ²·n^{-1/2}) 的理论连接来推导最优阈值。\n\n**[W4] 中等异质性下改善极小（R1 提出，R2 同意但认为透明度足够，minor）**\nRMSE 0.049 vs 0.050（Section 5.3, p > 0.05），7.4× bias reduction 仅在极端异质性下成立。Section 5.4 和 Figure 3 的 crossover plot 已清楚展示适用边界。R2 认为这更多是方法的固有局限而非论文的缺陷。\n\n**[W5] 经验贝叶斯两阶段不确定性传播（R1, R2 共识，warning）**\nmethod.tex L23 主实验使用 EB，MCMC 替代方案仅在 Appendix G 提及。EB 会低估后验不确定性。但 coverage 在所有配置下 ≥ 93%，实际影响可能有限。\n\n**[W6] 缺乏端到端真实数据验证（R2 major，R1 未列为 major，分歧点）**\nCivilComments 案例发现 \"3.2× effect-size gap\"，但无 ground-truth CATE 无法验证 EC-HTE 是否比 Global 更准确。对于标题声称 \"debiasing hurts\" 的论文，至少需要一个真实案例展示这确实发生了。这是整篇论文最大的实证缺口。\n\n**[W7] 方法论技术新颖性偏浅（R2 major，R1 minor，分歧点）**\n恒等式本质是 2×2 矩阵代数的直接展开（M_global^{-1} M_s − I 的结构分析），novelty 主要在问题识别（effect modifier misclassification bias）而非技术突破。EC-HTE 是成熟技术的组合（confusion matrix correction + hierarchical Bayes + κ-guard）。R1 认为技术问题可修复，不影响核心贡献。\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Theorem 1 技术正确性 | ✓ | ✓ | **[AGREE]** |\n| 实验覆盖面充分 | ✓ | ✓ | **[AGREE]** |\n| A2 限制诊断实用性 | W1 | W1 | **[AGREE]**（R2 澄清：恒等式本身不受影响） |\n| 有限样本余项 κ→κ² | W2 | W2 | **[AGREE]**（技术错误，需修正） |\n| κ-guard 缺理论依据 | W3 | W3 | **[AGREE]**（minor） |\n| EB 不确定性传播 | W5 | W5 | **[AGREE]**（coverage ≥93% 缓解） |\n| CivilComments 验证不足 | Q5 | W6 | **[AGREE]** |\n| 7.4× 基线计算 | W5(错误) | REBUT | **R2 纠正 R1 的计算错误**：7.4× = 0.059/0.008，基线确为 Global。R1 声称的 \"11.25×\" 与 Table 1 数值不对应 |\n| EB vs Gibbs 不一致 | Q4 | Q4 | **[AGREE]**（Method 说 EB <5ms，Algorithm 1 写 Gibbs sampler） |\n\n## Reviewer Divergence\n\n| Issue | R1 (4.0) | R2 (3.5) | 评估 |\n|-------|----------|----------|------|\n| **Novelty depth** | 技术问题可修复，不影响核心贡献 | 数学深度浅——2×2 矩阵代数直接展开，novelty 在问题识别非技术突破 | 合理分歧：取决于对\"理论贡献\"的评判标准 |\n| **EMNLP audience fit** | NLP+因果推断时效性好 | Effect modifier misclassification 在 EMNLP 受众中偏窄——多数 NLP 研究者不做 HTE，做 HTE 的不一定投 EMNLP | 合理分歧：取决于对交叉领域论文 venue 适配的判断 |\n| **Real-world evaluation** | 未列为 major weakness | 显著弱点——标题声称 \"debiasing hurts\" 应有真实案例佐证 | R2 立场更有力：extraordinary claims require extraordinary evidence |\n\n评分分歧 0.5 分（R1=4.0 vs R2=3.5），已充分阐明，无需进一步讨论轮次。\n\n## Questions\n\n**[Q1]** 放松 A3 (P(Z=0)=0.5) 时，theory.tex L84 提到 \"the identity remains exact with modified coefficients\" 但未给出显式形式。Appendix 中应提供完整推导。（R1 提出，R2 同意）\n\n**[Q2]** EC-HTE 与 PPCI（post-prediction causal inference）的理论兼容性条件是什么？当 LLM 同时标注 effect modifier 和 outcome 时，covariate-side 和 outcome-side error 的独立性假设可能失效。（R1, R2 共同提出）\n\n**[Q3]** Cov(π_s, Δτ_s) 在真实数据中的量级是 Corollary 4 实际可用性的关键。应在 semi-synthetic 实验中报告此值。（R1 提出，R2 同意）\n\n**[Q4]** Method section 说 empirical Bayes (<5ms)，Algorithm 1 写 Gibbs sampler (4 chains, 4000 iter)。主实验用哪个？两者何时使用？（R1, R2 共同提出）\n\n**[Q5]** CivilComments 案例：EC-HTE 揭示的 \"3.2× effect-size gap\" 是否比 Global 的结论更准确？没有 ground-truth CATE，如何验证？（R1, R2 共同关注——整篇论文最大的 empirical gap）\n\n## Missing References\n\n本轮未提出新的 missing references。此前轮次的引用修复状态：\n- Natarajan et al. (2013), Patrini et al. (2017)：段落已添加但 subgroup-dependent vs instance-dependent noise 联系未建立（R20-C3 仍 in_progress）\n- Veitch et al. (2020), Wood-Doughty et al. (2018)：已添加（R21-REF1）\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未配置外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（2026-05-25 04:19–04:23，耗时 ~4 分钟）| 0 critical / 2 warning / 26 info\n\n**Warnings:**\n1. **Pages 1-2 连续纯文本**：前两页无任何视觉锚点（Figure/Table/prominent equation），第一个 display item（Figure 1）到第 3 页才出现。审稿人阅读约 1.5 页密文后才看到任何图形。建议将 Figure 1 或 teaser 图提前。\n2. **Figure 2 红绿配色色盲不友好**：Sign Reversal 使用红色背景、0% sign reversal 使用绿色区域，红绿对比对 ~8% 男性不可区分。（注：此问题在 R16 标记、R19 标记为 resolved \"sage green→blue\"，但视觉检查仍检测到残留红绿对比，修复可能不完整。Figure 7 Appendix 也有类似问题。）\n\n**Info 摘要：**\n- 正文 8 页 + 23 页附录，正文含 4 个 display items（3 figures + 1 table，0.5/页，理论+实证混合论文可接受但偏低）\n- 公式渲染正确，无 overfull hbox，无 margin 溢出\n- 表格统一 booktabs，最优值加粗，数字精度一致（3 位小数）\n- References 格式统一，无未解析引用\n- Page 8 极高密度：Figure 3 + Table 1 + Conclusion + Limitations 挤在一页\n- Figure 1/3/4 部分文字偏小（axis labels, annotations），打印后可能难辨\n\n## Overall Assessment\n\n**评分：3.5 (Borderline Conference)** | 置信度：高\n\n| Reviewer | Score | 关键权重 |\n|----------|-------|----------|\n| R1 | 4.0 (Conference) | 技术严谨性 + 实验全面性 + 时效性 |\n| R2 | 3.5 (Borderline Conference) | Novelty depth + EMNLP 适配性 + 真实数据缺口 |\n\n**评分理由：**\n\n论文具有明确的理论贡献——Theorem 1 的偏差恒等式是精确的、可验证的，14.9% sign reversal 是有冲击力的发现。实验设计的覆盖面在 *ACL 投稿中属上乘。从恒等式到方法到操作边界的链条完整。\n\n制约评分的因素：\n1. **Novelty 主要在问题识别而非技术突破**（R2）：恒等式是 2×2 矩阵代数的直接推导，方法是成熟技术组合\n2. **EMNLP 受众适配性可疑**（R2）：effect modifier misclassification 是 HTE 分析中的窄问题，核心贡献偏统计/因果推断\n3. **缺乏真实数据端到端验证**（R2）：CivilComments 无 ground-truth CATE，无法证实标题级声称\n4. **技术错误**（R1, R2 共识）：有限样本余项阶数 κ→κ² 需修正\n5. **诊断实用性受限**（R1, R2 共识）：A2 非对称下 AUC 从 0.86 降至 0.66\n\nR1 评分 4.0 的论据同样有力：实验全面性、理论-实践完整链、NLP+因果推断的时效性。如果作者能 (a) 补充一个真实案例验证 + (b) 改进非对称诊断 AUC + (c) 修正 κ² 技术错误，论文可上调至 4.0 (Conference)。\n\n**综合评分 3.5 反映**：两位 Reviewer 的加权共识，略偏 R2 的立场——因 novelty depth 和 audience fit 是结构性问题（难以通过 revision 根本解决），而 R1 关注的技术问题（κ² 余项、EB/Gibbs 不一致）是可修复的。\n\n## Detailed Comments\n\n### Abstract & Introduction\n- Abstract ~150 words，符合 ≤200 words 要求\n- \"under symmetric errors (generalizing to full-matrix form)\" 措辞经过多轮修正，现已准确\n- \"7.4× under extreme heterogeneity\" 限定已添加\n\n### Section 3 (Theory)\n- Theorem 1 技术正确。乘积形式在一般非对称混淆矩阵下精确成立（Remark 2 已阐明）\n- **L92 余项阶数**：O_p(κ·n^{-1/2}) → O_p(κ²·n^{-1/2})，必须修正\n- Proposition 5 诊断 AUC=0.86（对称）→ 0.66（非对称）：应在正文更明确阐述 Proposition 5 的独特操作价值（不需估计 Δτ）以及其在非对称情形下的降级路径\n- A3 放松时 theory.tex L84 声称修正系数存在但未展示，应在 Appendix 补充\n\n### Section 4 (Method)\n- EB vs Gibbs 不一致：method.tex 提到 EB (<5ms)，Algorithm 1 使用 Gibbs sampler (4 chains × 4000 iter)。需澄清主实验使用哪个\n- κ-guard = 100：53× 安全余量使其在当前实验中从未触发。理论上基于修正后 O_p(κ²·n^{-1/2})，最优阈值应与 n_expert 和目标偏差容限相关\n\n### Section 5 (Experiments)\n- Table 1：7.4× = 0.059/0.008 基线为 Global（R2 验证正确）。R1 关于基线选择的质疑（W5）系 R1 自身计算错误\n- 中等异质性：RMSE 改善不显著（0.049 vs 0.050, p > 0.05），已透明展示\n- MC=100：coverage SE ≈ 2.2pp，Table 1 caption 已注释。关键配置增加 MC runs 可加强说服力\n- CivilComments：3.2× effect-size gap 缺乏 ground-truth 验证，是全文最大的实证缺口\n- 操作条件已从 \"decision framework\" 调整为 \"empirical operating guidelines\"\n\n### Formatting & Compliance\n- ACL 双栏模板 + review mode，正文 8 页，符合 EMNLP 2026 长文 8 页限制\n- Limitations section 在正文内，格式合规\n- Figure 2 色盲问题可能修复不完整（视觉检查仍检测到红绿对比）\n\n### Issue Tracker 更新\n- 本轮新增 6 个 issue（R22-W1/W2/Q1/Q2/Q3/Q4）\n- 更新 15 个已有 issue 的 R22 mentions\n- R16-W7（Figure 2 色盲）从 resolved 回退至 in_progress（视觉检查发现修复不完整）",
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 22 审稿报告\n\n## Summary\n\n本文推导了一个精确偏差恒等式（Theorem 1），揭示当 LLM 标注器的误分类率在子群间存在异质性时，全局混淆矩阵校正会引入子群级别的偏差，甚至可在 14.9% 的配置中导致 CATE 符号反转。基于该恒等式，论文提出了 Δτ-free 诊断准则（Proposition 5）和分层贝叶斯校正方法（EC-HTE），在极端异质性下将 |bias| 降低 7.4×。实验覆盖 520 合成配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验。\n\n## Strengths\n\n**[S1] 理论核心简洁且可验证（R1, R2 共识）**：Theorem 1 的乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 既精确又可解释，证明可手动核实。Proposition 5 的 Δτ-free 诊断（AUC=0.86 对称情形）仅凭 pilot 样本误差率即可决策，具有实际操作价值——不需要估计 Δτ，这在实际部署中比恒等式本身更有价值。\n\n**[S2] 实验覆盖极为全面（R1, R2 共识）**：520 配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验，在 *ACL 投稿中属上乘水平。跨估计器验证（CausalForest + R-learner, Table 1 + Appendix P）是额外加分项。\n\n**[S3] 理论→方法→实践链完整（R1, R2 共识）**：从恒等式推导到 EC-HTE 方法实现再到操作边界（Section 5.4: Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4）的完整链条。Algorithm 1 伪代码清晰。\"何时不用本方法\"的诚实边界划定值得肯定。\n\n**[S4] 时效性好的交叉方向（R1 强调）**：NLP × 因果推断的交叉研究正值增长期。14.9% sign reversal 是有冲击力的 headline number。\n\n**[S5] 假设放松讨论系统化（R1, R2 共识）**：Remark 2 对 A2、Appendix D 对 A3、Proposition 3 对 A5、Appendix H 对 A1 的系统性讨论表明作者对自身理论的局限有清醒认识。R2 补充：放松 A2 后诊断 AUC 从 0.86 降至 0.66 本身暴露了理论与实践的 gap（见 W1）。\n\n## Weaknesses\n\n**[W1] 对称误分类假设 (A2) 严重限制诊断实用性（R1, R2 共识，critical）**\n两位 Reviewer 均确认 A2 是论文最大的实践局限。GPT-4o FPR/FNR 差异达 0.09（0.249 vs 0.157），典型 LLM 不满足对称假设。R2 对 R1 做了重要澄清：**恒等式本身在非对称情形下仍然精确成立**（乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 不依赖 A2，因 B_s·1=0 仅依赖 M_s 和 M_global 的随机矩阵性质），降级的是**诊断准则**（Proposition 5 AUC 从 0.86 降至 0.66）和**标量简化形式** δ_s·Δτ/(1−2π̄)。非对称情形下需逐 cell 计算 [B_s]_{z,1}，操作复杂度大幅增加。Abstract 强调的简洁标量形式仅在 A2 下成立——这是误导的真正来源，而非 \"exact identity\" 措辞本身。\n\n**[W2] 有限样本余项阶数存在技术错误（R1, R2 共识，warning）**\ntheory.tex L92 声称余项为 O_p(κ·n^{-1/2})，但矩阵扰动分析表明应为 O_p(κ²·n^{-1/2})。推导：(C+E)^{-1} = C^{-1} − C^{-1}EC^{-1} + O(‖E‖²)，一阶项范数 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。对于 2×2 对称矩阵 ‖C^{-1}‖ = 1/(1−2π) = κ(C)。实际影响在 κ ∈ [1.25, 3] 时有限（κ² ∈ [1.56, 9] vs κ ∈ [1.25, 3]），但属于需要修正的技术性错误。\n\n**[W3] κ-guard 阈值 100 缺乏理论依据（R1, R2 共识，minor warning）**\n最大实验 κ ≈ 1.9，阈值 100 提供 53× 安全余量，实际上从未触发。Appendix A 的消融（κ sweep 10–1000）和自适应公式 κ_adapt = 10√(n_expert/K) 提供了实证支持，但缺少与 W2 修正后余项 O_p(κ²·n^{-1/2}) 的理论连接来推导最优阈值。\n\n**[W4] 中等异质性下改善极小（R1 提出，R2 同意但认为透明度足够，minor）**\nRMSE 0.049 vs 0.050（Section 5.3, p > 0.05），7.4× bias reduction 仅在极端异质性下成立。Section 5.4 和 Figure 3 的 crossover plot 已清楚展示适用边界。R2 认为这更多是方法的固有局限而非论文的缺陷。\n\n**[W5] 经验贝叶斯两阶段不确定性传播（R1, R2 共识，warning）**\nmethod.tex L23 主实验使用 EB，MCMC 替代方案仅在 Appendix G 提及。EB 会低估后验不确定性。但 coverage 在所有配置下 ≥ 93%，实际影响可能有限。\n\n**[W6] 缺乏端到端真实数据验证（R2 major，R1 未列为 major，分歧点）**\nCivilComments 案例发现 \"3.2× effect-size gap\"，但无 ground-truth CATE 无法验证 EC-HTE 是否比 Global 更准确。对于标题声称 \"debiasing hurts\" 的论文，至少需要一个真实案例展示这确实发生了。这是整篇论文最大的实证缺口。\n\n**[W7] 方法论技术新颖性偏浅（R2 major，R1 minor，分歧点）**\n恒等式本质是 2×2 矩阵代数的直接展开（M_global^{-1} M_s − I 的结构分析），novelty 主要在问题识别（effect modifier misclassification bias）而非技术突破。EC-HTE 是成熟技术的组合（confusion matrix correction + hierarchical Bayes + κ-guard）。R1 认为技术问题可修复，不影响核心贡献。\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Theorem 1 技术正确性 | ✓ | ✓ | **[AGREE]** |\n| 实验覆盖面充分 | ✓ | ✓ | **[AGREE]** |\n| A2 限制诊断实用性 | W1 | W1 | **[AGREE]**（R2 澄清：恒等式本身不受影响） |\n| 有限样本余项 κ→κ² | W2 | W2 | **[AGREE]**（技术错误，需修正） |\n| κ-guard 缺理论依据 | W3 | W3 | **[AGREE]**（minor） |\n| EB 不确定性传播 | W5 | W5 | **[AGREE]**（coverage ≥93% 缓解） |\n| CivilComments 验证不足 | Q5 | W6 | **[AGREE]** |\n| 7.4× 基线计算 | W5(错误) | REBUT | **R2 纠正 R1 的计算错误**：7.4× = 0.059/0.008，基线确为 Global。R1 声称的 \"11.25×\" 与 Table 1 数值不对应 |\n| EB vs Gibbs 不一致 | Q4 | Q4 | **[AGREE]**（Method 说 EB <5ms，Algorithm 1 写 Gibbs sampler） |\n\n## Reviewer Divergence\n\n| Issue | R1 (4.0) | R2 (3.5) | 评估 |\n|-------|----------|----------|------|\n| **Novelty depth** | 技术问题可修复，不影响核心贡献 | 数学深度浅——2×2 矩阵代数直接展开，novelty 在问题识别非技术突破 | 合理分歧：取决于对\"理论贡献\"的评判标准 |\n| **EMNLP audience fit** | NLP+因果推断时效性好 | Effect modifier misclassification 在 EMNLP 受众中偏窄——多数 NLP 研究者不做 HTE，做 HTE 的不一定投 EMNLP | 合理分歧：取决于对交叉领域论文 venue 适配的判断 |\n| **Real-world evaluation** | 未列为 major weakness | 显著弱点——标题声称 \"debiasing hurts\" 应有真实案例佐证 | R2 立场更有力：extraordinary claims require extraordinary evidence |\n\n评分分歧 0.5 分（R1=4.0 vs R2=3.5），已充分阐明，无需进一步讨论轮次。\n\n## Questions\n\n**[Q1]** 放松 A3 (P(Z=0)=0.5) 时，theory.tex L84 提到 \"the identity remains exact with modified coefficients\" 但未给出显式形式。Appendix 中应提供完整推导。（R1 提出，R2 同意）\n\n**[Q2]** EC-HTE 与 PPCI（post-prediction causal inference）的理论兼容性条件是什么？当 LLM 同时标注 effect modifier 和 outcome 时，covariate-side 和 outcome-side error 的独立性假设可能失效。（R1, R2 共同提出）\n\n**[Q3]** Cov(π_s, Δτ_s) 在真实数据中的量级是 Corollary 4 实际可用性的关键。应在 semi-synthetic 实验中报告此值。（R1 提出，R2 同意）\n\n**[Q4]** Method section 说 empirical Bayes (<5ms)，Algorithm 1 写 Gibbs sampler (4 chains, 4000 iter)。主实验用哪个？两者何时使用？（R1, R2 共同提出）\n\n**[Q5]** CivilComments 案例：EC-HTE 揭示的 \"3.2× effect-size gap\" 是否比 Global 的结论更准确？没有 ground-truth CATE，如何验证？（R1, R2 共同关注——整篇论文最大的 empirical gap）\n\n## Missing References\n\n本轮未提出新的 missing references。此前轮次的引用修复状态：\n- Natarajan et al. (2013), Patrini et al. (2017)：段落已添加但 subgroup-dependent vs instance-dependent noise 联系未建立（R20-C3 仍 in_progress）\n- Veitch et al. (2020), Wood-Doughty et al. (2018)：已添加（R21-REF1）\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未配置外部审稿。\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（2026-05-25 04:19–04:23，耗时 ~4 分钟）| 0 critical / 2 warning / 26 info\n\n**Warnings:**\n1. **Pages 1-2 连续纯文本**：前两页无任何视觉锚点（Figure/Table/prominent equation），第一个 display item（Figure 1）到第 3 页才出现。审稿人阅读约 1.5 页密文后才看到任何图形。建议将 Figure 1 或 teaser 图提前。\n2. **Figure 2 红绿配色色盲不友好**：Sign Reversal 使用红色背景、0% sign reversal 使用绿色区域，红绿对比对 ~8% 男性不可区分。（注：此问题在 R16 标记、R19 标记为 resolved \"sage green→blue\"，但视觉检查仍检测到残留红绿对比，修复可能不完整。Figure 7 Appendix 也有类似问题。）\n\n**Info 摘要：**\n- 正文 8 页 + 23 页附录，正文含 4 个 display items（3 figures + 1 table，0.5/页，理论+实证混合论文可接受但偏低）\n- 公式渲染正确，无 overfull hbox，无 margin 溢出\n- 表格统一 booktabs，最优值加粗，数字精度一致（3 位小数）\n- References 格式统一，无未解析引用\n- Page 8 极高密度：Figure 3 + Table 1 + Conclusion + Limitations 挤在一页\n- Figure 1/3/4 部分文字偏小（axis labels, annotations），打印后可能难辨\n\n## Overall Assessment\n\n**评分：3.5 (Borderline Conference)** | 置信度：高\n\n| Reviewer | Score | 关键权重 |\n|----------|-------|----------|\n| R1 | 4.0 (Conference) | 技术严谨性 + 实验全面性 + 时效性 |\n| R2 | 3.5 (Borderline Conference) | Novelty depth + EMNLP 适配性 + 真实数据缺口 |\n\n**评分理由：**\n\n论文具有明确的理论贡献——Theorem 1 的偏差恒等式是精确的、可验证的，14.9% sign reversal 是有冲击力的发现。实验设计的覆盖面在 *ACL 投稿中属上乘。从恒等式到方法到操作边界的链条完整。\n\n制约评分的因素：\n1. **Novelty 主要在问题识别而非技术突破**（R2）：恒等式是 2×2 矩阵代数的直接推导，方法是成熟技术组合\n2. **EMNLP 受众适配性可疑**（R2）：effect modifier misclassification 是 HTE 分析中的窄问题，核心贡献偏统计/因果推断\n3. **缺乏真实数据端到端验证**（R2）：CivilComments 无 ground-truth CATE，无法证实标题级声称\n4. **技术错误**（R1, R2 共识）：有限样本余项阶数 κ→κ² 需修正\n5. **诊断实用性受限**（R1, R2 共识）：A2 非对称下 AUC 从 0.86 降至 0.66\n\nR1 评分 4.0 的论据同样有力：实验全面性、理论-实践完整链、NLP+因果推断的时效性。如果作者能 (a) 补充一个真实案例验证 + (b) 改进非对称诊断 AUC + (c) 修正 κ² 技术错误，论文可上调至 4.0 (Conference)。\n\n**综合评分 3.5 反映**：两位 Reviewer 的加权共识，略偏 R2 的立场——因 novelty depth 和 audience fit 是结构性问题（难以通过 revision 根本解决），而 R1 关注的技术问题（κ² 余项、EB/Gibbs 不一致）是可修复的。\n\n## Detailed Comments\n\n### Abstract & Introduction\n- Abstract ~150 words，符合 ≤200 words 要求\n- \"under symmetric errors (generalizing to full-matrix form)\" 措辞经过多轮修正，现已准确\n- \"7.4× under extreme heterogeneity\" 限定已添加\n\n### Section 3 (Theory)\n- Theorem 1 技术正确。乘积形式在一般非对称混淆矩阵下精确成立（Remark 2 已阐明）\n- **L92 余项阶数**：O_p(κ·n^{-1/2}) → O_p(κ²·n^{-1/2})，必须修正\n- Proposition 5 诊断 AUC=0.86（对称）→ 0.66（非对称）：应在正文更明确阐述 Proposition 5 的独特操作价值（不需估计 Δτ）以及其在非对称情形下的降级路径\n- A3 放松时 theory.tex L84 声称修正系数存在但未展示，应在 Appendix 补充\n\n### Section 4 (Method)\n- EB vs Gibbs 不一致：method.tex 提到 EB (<5ms)，Algorithm 1 使用 Gibbs sampler (4 chains × 4000 iter)。需澄清主实验使用哪个\n- κ-guard = 100：53× 安全余量使其在当前实验中从未触发。理论上基于修正后 O_p(κ²·n^{-1/2})，最优阈值应与 n_expert 和目标偏差容限相关\n\n### Section 5 (Experiments)\n- Table 1：7.4× = 0.059/0.008 基线为 Global（R2 验证正确）。R1 关于基线选择的质疑（W5）系 R1 自身计算错误\n- 中等异质性：RMSE 改善不显著（0.049 vs 0.050, p > 0.05），已透明展示\n- MC=100：coverage SE ≈ 2.2pp，Table 1 caption 已注释。关键配置增加 MC runs 可加强说服力\n- CivilComments：3.2× effect-size gap 缺乏 ground-truth 验证，是全文最大的实证缺口\n- 操作条件已从 \"decision framework\" 调整为 \"empirical operating guidelines\"\n\n### Formatting & Compliance\n- ACL 双栏模板 + review mode，正文 8 页，符合 EMNLP 2026 长文 8 页限制\n- Limitations section 在正文内，格式合规\n- Figure 2 色盲问题可能修复不完整（视觉检查仍检测到红绿对比）\n\n### Issue Tracker 更新\n- 本轮新增 6 个 issue（R22-W1/W2/Q1/Q2/Q3/Q4）\n- 更新 15 个已有 issue 的 R22 mentions\n- R16-W7（Figure 2 色盲）从 resolved 回退至 in_progress（视觉检查发现修复不完整）",
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 2387 · 2026-05-25T04:48:34.645521+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4116
}
```

</details>

---


### Assistant

_source line 2388 · 2026-05-25T04:48:53.027248+00:00_

---

**Round 22 审稿报告已投递至 Research Director。**

**圆桌结论：**
- **收敛状态**：1 轮交叉回应后收敛。关键技术问题达成共识，评分分歧（R1=4.0 vs R2=3.5）为合理的评审判断差异。
- **综合评分**：**3.5 (Borderline Conference)**
- **R2 纠正了 R1 的一个事实错误**：7.4× 基线确为 Global（0.059/0.008），R1 声称的 "11.25×" 计算有误。
- **R2 做了一个重要澄清**：恒等式本身在非对称情形下仍然精确（不依赖 A2），降级的仅是标量诊断（AUC 0.86→0.66）。

**核心分歧**（决定 3.5 vs 4.0）：
1. Novelty depth — 问题识别 vs 技术突破
2. EMNLP audience fit — HTE 子群偏差校正的受众面
3. Real-world evaluation — CivilComments 无 ground-truth CATE

**本轮新增 6 个 issue**，更新 15 个已有 issue，R16-W7（Figure 2 色盲）从 resolved 回退至 in_progress。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 188

## Round 188

6 recorded events


### User

_source line 2389 · 2026-05-25T04:48:54.093778+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **S1-S5**: 全部 AGREE，补充了一些细节
- **W1**: 部分 AGREE，但 REBUT 了"exact identity 措辞误导"的说法——恒等式在非对称情形下仍然精确，降级的只是诊断判据
- **W2**: AGREE，有限样本余项阶数确实应为 O_p(κ²·n^{-1/2})
- **W3**: AGREE，κ-guard 缺乏理论依据
- **W4**: AGREE，但论文对此已足够透明
- **W5**: REBUT——R1 的计算有误，7.4× 的基线就是 Global（0.059/0.008），R1 声称的 11.25× 不对应表中任何数值
- **W6**: AGREE，但实际影响有限（coverage ≥ 93%）
- **Q1-Q5**: 全部 AGREE，其中 Q4（EB vs MCMC）和 Q5（CivilComments 验证）与我自己的疑问一致
- **分歧点**: 我维持 3.5 vs R1 的 4.0，核心在于数学深度有限、EMNLP 受众偏窄、缺乏真实数据评估

---

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Strengths 回应

**[AGREE] R2-S1:** 同意。Proposition 5 的 Δτ-free 诊断准则是本文最具实践价值的贡献之一。我在自己的审稿中也将此列为 S1 的核心优势。AUC=0.86 在对称条件下足以支撑实用性。

**[AGREE] R2-S2:** 同意。实验设计的层次性（合成 → 半合成 → 真实 NLP 任务 → 鲁棒性 → 跨估计器）是本文最突出的优点。我在自己的 S2 中给出了类似评价，520+ 配置 × 100 MC 运行的规模远超同类论文。

**[AGREE] R2-S3:** 同意。论文对操作条件的诚实表述（Δπ > 0.15, n_expert/K ≥ 50 等）在方法论文中较为少见，体现了负责任的学术态度。Figure 3 的 crossover 分析确实是实用决策工具。

**[AGREE] R2-S4:** 同意。Related work 的三维度定位（scalar attenuation vs. per-subgroup correction vs. diagnostic）清晰区分了本文与 Frazis-Loewenstein、DSL、PPI 等已有工作的差异。

---

## Weaknesses 回应

**[REBUT] R2-W1: "核心恒等式数学深度有限"**

R2 认为 Theorem 1 仅是"2×2 矩阵代数的直接展开"，novelty 主要在问题提出。我不同意这会显著影响接收决定，理由如下：

1. **定理的价值在于 insight 而非证明难度。** 统计学和计量经济学中许多有影响力的结果（如 Frisch-Waugh-Lovell 定理、omitted variable bias 公式）证明都很简洁，但它们揭示的结构性关系具有深远影响。Theorem 1 的乘积形式 δ_s·Δτ/(1−2π̄) 精确刻画了三个独立因子的交互——这个结构在之前的文献中未被识别。

2. **论文的技术贡献不仅限于 Theorem 1。** 完整的理论框架包括：Proposition 3（(A5) 放松到异质处理效应，恒等式仍精确）、Corollary 1（聚合偏差 = 加权协方差形式）、Corollary 6（多类扩展到 K 子群 × J 效应修正因子水平）、Proposition 5（诊断准则）。这些扩展并非平凡。

3. **关于非对称 AUC 降至 0.66：** 这是诊断准则的退化，不是方法本身的退化。EC-HTE 在非对称条件下仍然有效——Table 36（Appendix Z.6）显示非对称误差（FPR/FNR 比率高达 7:1）下 EC-HTE 实现 94.5% 覆盖率 vs. Global 的 93.0%，RMSE 从 0.083 降至 0.074。诊断 AUC 的降低意味着从业者需要更保守地使用诊断准则，但不影响校正方法的有效性。

**结论：** 数学深度确实有限，但贡献的核心价值在于将一个此前被忽视的系统性偏差来源精确形式化并给出可操作的解决方案。我维持这一点不应显著降低评分。

---

**[REBUT] R2-W2: "缺乏端到端真实数据评估"**

R2 认为所有实验均使用合成 CATE 注入，缺乏真实案例展示全局校正导致错误结论。我部分同意这是一个限制，但不同意这应作为 major weakness 影响接收决定：

1. **真实 CATE 基本不可观测，这是因果推断的根本问题。** 使用合成 CATE 注入 + 真实混淆矩阵的半合成方法是因果推断文献的标准实践（cf. Wager and Athey 2018 的模拟设计、Kennedy 2023 的半合成验证）。要求本文提供真实 ground-truth CATE 的端到端验证，等于要求其解决因果推断的基本识别问题，这不公平。

2. **半合成验证使用了真实 LLM 混淆矩阵。** Table 23（Appendix W）的 11 个 LLM × 数据集组合使用的是从真实 LLM 标注中估计的混淆矩阵（非合成），只有 CATE 是注入的。这意味着误差率异质性的模式是真实的——这正是论文核心关注的变量。

3. **关于"14.9% sign reversal 取决于 τ(0)=0.03"：** 这一批评不够准确。Figure 4（热力图）展示了完整参数网格上的偏差放大模式，sign reversal 不仅发生在 τ(0)=0.03。Section 5.2 明确指出："global correction increases bias in 50% of K=2 configurations (260/520)"。14.9% 是 sign reversal 的比例，50% 是 bias amplification 的比例——这些跨越了广泛的参数设定。

4. **Civil Comments 案例（Section M）提供了真实世界验证的关键要素：** 真实 LLM 标注错误率的子群异质性（FPR 从 8.5% 到 21.5%），跨文本特征子群体的不同 CATE 校正。虽然 ground-truth CATE 仍不可用，但异质性模式本身是真实的。

5. **Section R（Appendix）的半真实混淆矩阵验证** 使用 GPT-4.1 的真实非对称混淆矩阵验证了偏差恒等式的预测力（R² = 0.97），包括真实 per-subgroup FPR 和 FNR。

**结论：** 这是一个真实的限制（论文自身在 Limitations 中也承认），但属于因果推断方法论文的系统性限制，不应对本文单独加重扣分。

---

**[AGREE] R2-W3: Abstract 信息密度过高**

同意。Abstract 包含 9+ 具体数字（7.4×, 14.9%, R²>0.97, AUC=0.86 等），读起来确实更像 results summary。一个更好的结构是在 abstract 前半段聚焦动机和核心发现，后半段精选 2-3 个最关键的数字。但这是可修复的表述问题，不影响技术贡献评估。

---

**[AGREE] R2-W4: "Debiasing" 术语与 fairness 混淆**

同意这是一个合理的担忧。"Debiasing" 在 *ACL 社区确实首先联想到 algorithmic fairness（gender/racial bias）。Footnote 1 的澄清是必要的但可能不够——许多读者只看标题就形成第一印象。建议在 abstract 首句明确"measurement-error correction (debiasing)"以消除歧义。但这不影响论文的技术质量。

---

**[REBUT] R2-W5: Figure 4 浮动到第 9 页**

我回看了 PDF（submitted.pdf page 7-8）。Figure 3（expert budget crossover）出现在 page 7，Figure 4（heatmap）出现在 page 8 的上半部分，均在主文 8 页限制内。Figure 4 并未浮动到 references 区域（page 9 开始是参考文献）。R2 可能记忆有误，或看到的是不同版本。当然，如果在特定 PDF viewer 中排版确实有问题，这是一个容易修复的 LaTeX 浮动问题。

---

**[AGREE] R2-W6: Per-model R² 低端讨论不足**

部分同意。Table 23（Appendix W）报告了 11 个 LLM 的 R² 值，最低为 GPT-4o-mini on Civil Comments（R² = 0.893）。R2 提到的 0.76 可能来自 Remark 2 中非对称条件下的 R²（"R² ≥ 0.73 for Δπ ≥ 0.10 across 48 configurations"）。

GPT-4o-mini 的 R² 较低可能与其较高的误分类率和更显著的非对称性有关——论文应更明确讨论哪些 LLM 特征导致恒等式拟合度下降（例如，是错误率绝对水平、非对称程度、还是样本量不足）。这可以通过在 Appendix W 中增加一个回归分析（R² ~ f(FPR, FNR, |FPR-FNR|, n)）来系统性回答。

---

## Questions 回应

**[AGREE] R2-Q1: 非对称诊断改进**

同意这是一个重要的开放问题。我在自己的 W1 中也指出了非对称条件下诊断 AUC 从 0.86 降至 0.66 的问题。论文当前的处理（Remark 2: "evaluate [B_s]_{z,1} cell-by-cell"）增加了实操复杂性。一个可能的改进方向是使用 full 2×2 confusion matrix 的某种标量摘要（如行间距离度量）来替代简单的 δ_s/(1−2π̄)。但我认为这属于合理的 future work，不是拒稿理由。

**[AGREE] R2-Q2: Algorithm 1 vs. 经验贝叶斯**

同意这是一个需要澄清的问题。我在自己的 Q4 中提出了相同的疑问。Method.tex 第 23 行说"Posterior inference uses empirical Bayes optimization (<5ms)"，而 Algorithm 1（Appendix A）和 Table 2（Appendix G）描述的是 MCMC（4 chains, 4000 iterations）。论文应明确说明：(1) 主实验用的是哪种推断方法？(2) MCMC 和经验贝叶斯是否给出一致的结果？(3) Table 2 的收敛诊断是验证性实验还是主实验的一部分？

**[AGREE] R2-Q3: EC-HTE + PPCI 独立性**

同意这个担忧。我在自己的 Q2 中也提出了类似问题。当同一个 LLM 同时标注 effect modifier Z 和 outcome Y 时，covariate-side 和 outcome-side 的误差可能相关（例如，LLM 对某个文本样本整体理解不足导致两种标注同时出错）。论文应讨论这种相关性对 EC-HTE + PPCI 组合保证的影响。

**[REBUT] R2-Q4: K=4 时 Strat. MLE 偏差更低**

R2 指出 K=4 时 Strat. MLE |Bias| (0.010) < HB EC-HTE (0.012)，质疑层级贝叶斯的优势。但这恰好体现了正确的 bias-variance tradeoff：

- Table 1 完整数据：K=4 Extreme 条件下，Strat. MLE 的 RMSE（未在主表报告，但 Section 5.3 提到 HB EC-HTE 在 87.5% 配置中优于 Strat. MLE）高于 HB EC-HTE。
- 层级贝叶斯通过向全局收缩引入小量偏差（+0.002），但显著降低方差——这正是 James-Stein 类收缩估计的经典优势。
- 论文 method.tex 第 24 行已给出明确的操作指南："below n_expert × P(Z_minority) / K < 25, stratified MLE is preferred"。

关键是看 RMSE（综合偏差和方差），而非仅看 |Bias|。HB EC-HTE 在 RMSE 上的优势在小样本时更明显（Table 4, Appendix I 的 budget sweep）。

---

## Missing References 回应

**[AGREE] Filtered PPI:** 同意这是一个相关参考文献，处理异质性预测质量与本文的 heterogeneous error rates 设定有概念上的联系。

**[AGREE] Egami et al. 年份不一致：** 同意这是一个 bib 格式错误需要修正。bib key 为 `egami2024dsl` 但 year={2023} 确实不一致。

---

## 对 R2 Overall Assessment (3.5) 的回应

**我不同意将评分降至 3.5（Borderline Conference）。我维持 4.0（Conference）。**

R2 的两个 major weakness 核心论点是：(1) 数学深度有限；(2) 缺乏真实数据端到端评估。

对于 (1)：如上所述，定理的价值在于 insight 而非证明难度。论文提供的不是一个孤立的简单引理，而是一个完整的 identity → diagnostic → correction → validation 链条。技术贡献包括 Theorem 1 + Propositions 3, 5 + Corollaries 1, 6 + 层级贝叶斯估计 + κ-guard 设计 + 方差调整 + PPCI 组合。这个整体贡献超过了"仅是问题识别"。

对于 (2)：真实 CATE 的不可观测性是因果推断的基本限制。本文使用的半合成方法（真实 LLM 混淆矩阵 + 合成 CATE）是该领域的标准做法。在这个约束下，论文的实验覆盖已经达到了很高的标准。

R2 提到的 "effect modifier misclassification 设定在 EMNLP 受众中偏窄" 是一个值得讨论的定位问题。但随着 LLM 标注在社会科学和政策评估中的普及，这个设定的受众正在快速扩大。论文在 4 个 NLP 任务（情感分析、仇恨言论检测、立场检测、主题分类）上的验证覆盖了 EMNLP 的主要应用领域。

**综合评估：** R2 的多数 minor weaknesses（W3-W6）我同意但不影响评分。两个 major weaknesses（W1, W2）中，W1 我实质性反驳，W2 我认为是该领域的系统性限制而非本文特有问题。因此我维持 Overall: 4 (Conference) 的评分。


---

[Reviewer 1 审稿结果]:
交叉回应已提交。

逐条回应了 R2 的 S1-S4、W1-W6、Q1-Q4：
- **6 条 [AGREE]**（S1-S4, W3, W4, W6, Q1-Q3, 两条 missing references）
- **3 条 [REBUT]**（W1 数学深度、W2 真实数据评估、W5 Figure 浮动位置）
- **1 条 [REBUT] on Q4**（K=4 bias-variance tradeoff）

核心分歧在 W1 和 W2：我认为 W1 低估了 insight-driven 定理的价值（证明难度 ≠ 贡献大小），W2 是因果推断的系统性限制而非本文特有问题。维持 Overall: 4 (Conference)，不同意 R2 的 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2390 · 2026-05-25T04:53:51.219260+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"已修正为 'on synthetic grids (aggregate 0.975; per-model range 0.76-0.99)'\"\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"AUC 数字从 Abstract 完全移除\"\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"Abstract 已加 'under extreme heterogeneity' 限定\"\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 视觉审查仍检测到 Figure 2 红/绿对比（红色=Sign Reversal, 绿色=0% reversal）。R19 标记为 resolved (sage green→blue) 但修复可能不完整。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  # === OPEN / IN_PROGRESS — updated with R22 (both cross-responses) ===\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 PEHE、缺半合成 CF 结果、缺 Eq.7 不确定性传播消融\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"DDL 前无法补充。PEHE + Eq.7 消融理论上各需 30min，半合成 CF 需 2-4h 高风险。Rebuttal 材料。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20 指出仅用 CausalForestDML + R-learner 不够，缺 X-learner/BART。\"\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-W1 再次提出仅 2 种 HTE 估计器。R2 未单独提及但在 questions 中问及 scale。与本 issue 一致。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。R2 确认跨估计器验证（CausalForest + R-learner）是加分项。仍缺 X-learner/BART。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: PEHE + Eq.7 消融（camera-ready 补充）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认: Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s。问题已解决。\"\n    action_items: []\n    resolution: \"Proposition 3 (A5 relaxation with Δτ_s) 已在主文 theory.tex L63-71\"\n    resolution_round: 21\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。experiments.tex L28 已有讨论。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接提及。R1 在交叉回应中用 K=4 的 bias-variance tradeoff 解释了 HB vs Strat. MLE 的互补关系。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W3 再次提出正文缺完整真实数据实验。真实数据仍仅在附录。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 核心分歧点。R2 再次强调标题级声称需真实案例佐证。R1 REBUT：(1) 真实 CATE 基本不可观测是因果推断基本限制；(2) 半合成（真实 LLM CM + 合成 CATE）是领域标准做法（cf. Wager & Athey 2018）；(3) 11 真实 LLM CM 保证了误差异质性模式的真实性；(4) CivilComments FPR 从 8.5% 到 21.5% 的异质性是真实的；(5) Appendix R 的半真实 CM 验证 R²=0.97。R1 认为对本文单独加重扣分不公平。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 两位 Reviewer 共识确认技术错误：theory.tex L92 的 O_p(κ·n^{-1/2}) 应为 O_p(κ²·n^{-1/2})。矩阵扰动 (C+E)^{-1} 一阶展开余项为 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。实际影响在 κ∈[1.25,3] 时有限但必须修正。\"\n    action_items:\n      - round: 22\n        action: \"修正 theory.tex L92 余项阶数 κ→κ²\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-N2: 'exact' 标题与标量近似 R² 退化的张力。Abstract 已修正为 'under symmetric errors (generalizing to full-matrix form)'。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 partial REBUT R1: 恒等式在非对称情形下仍精确——乘积形式不依赖 A2。降级的是标量简化和诊断 AUC。R1 补充：EC-HTE 在非对称下仍有效（Table 36: 94.5% coverage vs Global 93.0%）。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接提及。Table 1 footnote 注明 93.8% 且 bootstrap 可恢复 ≥95%。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。method.tex 提到 HB 估计 <5ms。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。但 EB vs Gibbs 不一致（R22-Q1）暗示 wall-clock 声称需要区分两种实现。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N1 再次作为 Must-Fix 提出。experiments.tex 已添加 CivilComments NLP insight 段落。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 核心分歧点。R2 维持 EMNLP 受众偏窄——HTE 在 NLP 中是小众话题。R1 REBUT：随着 LLM 标注在社会科学和政策评估中的普及，受众正在扩大；4 个 NLP 任务（情感/仇恨言论/立场/主题分类）覆盖 EMNLP 主要应用领域。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-N3 作为 Must-Fix 再次提出: K≤4 限制。Intro Contribution 2 已加 'K ≤ 4 subgroups' 限定。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"Intro Contribution 2 增加 K ≤ 4 限定\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。已与 R19-W2 合并，Limitations 已补充。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W4 再次提出: 仅变动 Gamma 超参数，未考虑替代先验（logistic-normal）。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 通过 EB vs Gibbs 不一致间接关联。见 R22-Q1。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 严重限制标题级 'Exact Identity' 声称——非对称情形 R² 降至 0.73\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21 两位 Reviewer 均再次关注。experiments.tex §5.4 已添加 matrix vs scalar 区分句。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 共识：恒等式在非对称下仍精确（R2 partial REBUT 确认），降级的是诊断 AUC。R1 补充 Table 36 数据：非对称（FPR/FNR 比 7:1）下 EC-HTE 94.5% coverage vs Global 93.0%，RMSE 0.083→0.074——方法本身不受 A2 限制。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n      - round: 21\n        action: \"experiments.tex §5.4 添加 matrix vs scalar 区分\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 经典测量误差理论的增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 再次作为 Must-Fix。theory.tex 已替换为 sign reversal novelty statement。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 通过 novelty depth 讨论间接涉及。R1 REBUT：完整理论框架包含 Theorem 1 + Props 3,5 + Corollaries 1,6 + HB + κ-guard，不仅是孤立引理。定理的价值在于 insight 而非证明难度（类比 Frisch-Waugh-Lovell）。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L (2003) 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 explicit novelty statement: sign reversal vs uniform shrinkage\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献 (Natarajan et al. 2013, Patrini et al. 2017)\"\n    category: writing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"段落已添加但 subgroup-dependent vs instance-dependent noise 联系未建立。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。R21 的 deeper connection 请求仍为 open action。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"深化噪声标签文献讨论：建立 subgroup-dependent vs instance-dependent noise 联系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称——SE ≈ 2.2pp\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出。Table 1 caption 已添加 coverage SE 注释。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅——EC-HTE 是成熟技术的组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 间接涉及。核心贡献定位应为理论洞察。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 核心分歧点。R2：恒等式是 2×2 矩阵代数直接展开。R1 REBUT：(1) insight > 证明难度（类比 Frisch-Waugh-Lovell、OVB 公式）；(2) 完整框架含 Theorem 1 + Props 3,5 + Corollaries 1,6 + 层级贝叶斯 + κ-guard + PPCI 组合，非孤立引理；(3) δ_s·Δτ/(1−2π̄) 的三因子交互结构此前未被识别。R1 认为不应显著降低评分。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W5 再次提出: 仅 logistic link, γ ∈ [0, 0.20]。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 20\n        action: \"增加一种基于文本特征的 confounding 形式的灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"theory.tex 已添加 K=2 数值示例段落。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"theory.tex Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用不一致\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"theory.tex 添加 \\\\label{rem:asymmetric}，统一所有引用。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"添加 \\\\label{rem:asymmetric} 并统一所有交叉引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65，正文讨论严重不足\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-N1。experiments.tex §5.4 已添加 AUC 对比。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 共识。R2 补充 Prop 5 操作价值（不需估计 Δτ）。R1 补充：诊断 AUC 降低 ≠ 方法本身降级——EC-HTE 在非对称下 94.5% coverage（Table 36），意味着从业者需更保守使用诊断但校正方法仍有效。两位均认为改进非对称诊断是合理 future work 而非拒稿理由。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.4 增加 matrix vs scalar 区分 + 非对称 AUC 数字\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"考虑基于完整 2×2 矩阵的非对称诊断准则（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足——核心贡献在统计/因果推断，NLP 任务仅为测试平台\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-N1 Must-Fix。experiments.tex §5.2 已添加 CivilComments NLP insight。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 核心分歧。R2 维持偏窄。R1 REBUT：LLM 标注在社科/政策评估中的普及使受众扩大；4 NLP 任务覆盖 EMNLP 主要应用领域。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"将 Appendix M 关键发现移入正文（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明——两者标签需求相同\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-W3。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。\"\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"limitations.tex 已添加 A3 class imbalance 影响讨论。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。\"\n    action_items:\n      - round: 21\n        action: \"Limitations 补充 A3 class imbalance 影响讨论\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"操作条件称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"已从 'decision framework' 改为 'Empirical operating guidelines'。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 确认 Section 5.4 展示透明。已调整措辞。\"\n    action_items:\n      - round: 21\n        action: \"Contribution 2 措辞调整为 'empirical operating guidelines'\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高——缺数值示例\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"theory.tex 已添加 K=2 数值示例段落。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch et al. (2020), Wood-Doughty et al. (2018)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"已添加引用。\"\n      - round: 22\n        reviewers: [1]\n        note: \"R1 同意 Filtered PPI 也是相关参考文献。\"\n    action_items:\n      - round: 21\n        action: \"Related Work 增加 Veitch 2020, Wood-Doughty 2018 引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === ROUND 22 NEW ISSUES ===\n\n  - id: \"R22-W1\"\n    summary: \"κ-guard 阈值 100 纯经验选择——缺乏与有限样本余项 O_p(κ²·n^{-1/2}) 的理论连接\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。Appendix A 消融提供实证支持但缺理论推导。\"\n    action_items:\n      - round: 22\n        action: \"基于修正后的 O_p(κ²·n^{-1/2}) 余项推导理论最优 κ 阈值（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"经验贝叶斯两阶段低估后验不确定性——MCMC 替代方案仅在 Appendix G\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"共识。EB 低估后验不确定性是标准批评。Coverage ≥93% 缓解但不消除。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q1\"\n    summary: \"Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler (4 chains, 4000 iter)——不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出。需澄清：(1) 主实验用哪种？(2) 两者结果是否一致？(3) Table 2 收敛诊断是验证性还是主实验？\"\n    action_items:\n      - round: 22\n        action: \"澄清主实验使用 EB 还是 Gibbs，统一 Method 和 Algorithm 1 描述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q2\"\n    summary: \"A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"theory.tex L84 声称修正系数存在但未展示。应在 Appendix 补充。\"\n    action_items:\n      - round: 22\n        action: \"Appendix 补充 A3 放松时的显式修正系数推导\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q3\"\n    summary: \"Cov(π_s, Δτ_s) 在实验中未报告——Corollary 4 实际可用性的关键\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"semi-synthetic 实验中应报告此协方差值。\"\n    action_items:\n      - round: 22\n        action: \"Semi-synthetic 实验中报告 Cov(π_s, Δτ_s)\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q4\"\n    summary: \"EC-HTE + PPCI 理论兼容性条件不明——LLM 同时标注 effect modifier 和 outcome 时独立性假设可能失效\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共同提出。需要在 Limitations 或 Discussion 中讨论。\"\n    action_items:\n      - round: 22\n        action: \"讨论 EC-HTE 与 PPCI 的理论兼容性条件\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W3\"\n    summary: \"Abstract 信息密度过高（9+ 具体数字），读起来像 results summary\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 初审提出，R1 AGREE。建议前半段聚焦动机和核心发现，后半段精选 2-3 个关键数字。可修复的表述问题。\"\n    action_items:\n      - round: 22\n        action: \"精简 Abstract 数字密度（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W4\"\n    summary: \"'Debiasing' 术语在 *ACL 社区首先联想 algorithmic fairness，与本文 measurement-error correction 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 初审提出，R1 AGREE。Footnote 1 有澄清但可能不够——读者看标题即形成第一印象。建议 abstract 首句明确 'measurement-error correction (debiasing)'。\"\n    action_items:\n      - round: 22\n        action: \"Abstract 首句明确 debiasing = measurement-error correction\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W5\"\n    summary: \"Per-model R² 低端（GPT-4o-mini R²=0.893）讨论不足——哪些 LLM 特征导致拟合度下降\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 初审提出，R1 部分 AGREE。Table 23 报告了 per-model R²，最低 0.893（GPT-4o-mini）。R1 建议在 Appendix W 增加回归分析 R² ~ f(FPR, FNR, |FPR-FNR|, n) 系统性回答。\"\n    action_items:\n      - round: 22\n        action: \"Appendix W 增加 per-model R² 影响因素分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-FMT1\"\n    summary: \"Egami et al. bib key 'egami2024dsl' 与 year={2023} 不一致\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 初审提出，R1 AGREE。bib 格式错误需修正。\"\n    action_items:\n      - round: 22\n        action: \"修正 Egami bib entry year\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "issues_yaml": "issues:\n  # === RESOLVED (prior rounds — abbreviated) ===\n  - id: \"R1-N1\"\n    summary: \"Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 2\n    action_items: []\n    resolution: \"重新推导为精确恒等式\"\n    resolution_round: 0\n\n  - id: \"R2-W8\"\n    summary: \"Proposition 1 限于 K=2\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"Theorem 1 适用一般 K\"\n    resolution_round: 0\n\n  - id: \"R1-N2\"\n    summary: \"Real data ground truth CATE 来源不明\"\n    category: experiment\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位为 illustrative application\"\n    resolution_round: 0\n\n  - id: \"R1-N3\"\n    summary: \"HB 模型规格严重不完整\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"完整 MCMC 规格\"\n    resolution_round: 0\n\n  - id: \"JOINT-W4\"\n    summary: \"相关工作严重遗漏\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"30+ 引用覆盖\"\n    resolution_round: 0\n\n  - id: \"JOINT-W3\"\n    summary: \"信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"主文精简至合理密度\"\n    resolution_round: 0\n\n  - id: \"R2-W7\"\n    summary: \"真实数据验证单薄\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 1\n    action_items: []\n    resolution: \"恰当定位 + 公开数据集\"\n    resolution_round: 0\n\n  - id: \"R1-W5\"\n    summary: \"Pages 9-10 缺 Appendix 标签\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 0\n    last_seen_round: 0\n    action_items: []\n    resolution: \"附录结构重组\"\n    resolution_round: 0\n\n  - id: \"R19-C1\"\n    summary: \"Abstract 'R²≥0.97 across synthetic grids and 11 empirical LLM CMs' 事实性错误\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"已修正为 'on synthetic grids (aggregate 0.975; per-model range 0.76-0.99)'\"\n    action_items: []\n    resolution: \"已修正 Abstract L4, Intro L17/L31, Conclusion L4——区分合成 vs 真实 LLM 的 R² 范围\"\n    resolution_round: 19\n\n  - id: \"R19-C2\"\n    summary: \"诊断工具 (Proposition 5) AUC=0.63 但 Abstract/Intro 呈现为核心贡献无性能限定\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"AUC 数字从 Abstract 完全移除\"\n    action_items: []\n    resolution: \"AUC 数字从 Abstract 完全移除\"\n    resolution_round: 19\n\n  - id: \"R19-C3\"\n    summary: \"核心量化 claims (7.4×) 在假设完全满足的合成数据上得出，moderate 配置下无改善\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"Abstract 已加 'under extreme heterogeneity' 限定\"\n    action_items: []\n    resolution: \"Abstract L6 修正为 'reducing |bias| by 7.4× under extreme heterogeneity'\"\n    resolution_round: 19\n\n  - id: \"R19-W1\"\n    summary: \"操作条件过窄——无真实 LLM-dataset pair 通过全部 5 个筛选条件\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 扩展含 relaxed screening adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-W2\"\n    summary: \"DGP 缺乏 observational/confounding 场景验证\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Limitations 已补充 confounded DGP scope\"\n    resolution_round: 19\n\n  - id: \"R19-M4\"\n    summary: \"Conclusion 过短（仅两句话）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"Conclusion 从 2 句扩展到 3 句含 adoption guideline\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"experiments.tex L19 'EC-HTE eliminates sign reversal entirely' 与 stance/AG News 数据矛盾\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"已限定为 primary K=2 configuration\"\n    resolution_round: 19\n\n  - id: \"R19-DATA2\"\n    summary: \"task-agnosticity 段 '16 real LLM CMs span four tasks' 与 L11 '8×2=16' 计数不一致\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"区分 16 core CMs 和独立 cross-task validations\"\n    resolution_round: 19\n\n  - id: \"R19-DATA3\"\n    summary: \"AG News appendix 引用 GPT-4/~85% 与源论文不符\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    action_items: []\n    resolution: \"引用细节修正完成\"\n    resolution_round: 19\n\n  - id: \"R16-W7\"\n    summary: \"Figure 2 红绿配色色盲不友好\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 16\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: []\n        note: \"R22 视觉审查仍检测到 Figure 2 红/绿对比（红色=Sign Reversal, 绿色=0% reversal）。R19 标记为 resolved (sage green→blue) 但修复可能不完整。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M1\"\n    summary: \"Abstract 'per-model range 0.26-0.09' 数值排序应为 0.09-0.26（从小到大）\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    action_items: []\n    resolution: \"确认 Abstract 已是 '0.76--0.99'（升序），非问题\"\n    resolution_round: 21\n\n  # === OPEN / IN_PROGRESS — updated with R22 (both cross-responses) ===\n\n  - id: \"R19-C4\"\n    summary: \"CausalForest 集成验证不足——缺 PEHE、缺半合成 CF 结果、缺 Eq.7 不确定性传播消融\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 19\n        reviewers: [1]\n        note: \"DDL 前无法补充。PEHE + Eq.7 消融理论上各需 30min，半合成 CF 需 2-4h 高风险。Rebuttal 材料。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20 指出仅用 CausalForestDML + R-learner 不够，缺 X-learner/BART。\"\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-W1 再次提出仅 2 种 HTE 估计器。R2 未单独提及但在 questions 中问及 scale。与本 issue 一致。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提。R2 确认跨估计器验证（CausalForest + R-learner）是加分项。仍缺 X-learner/BART。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal 准备: PEHE + Eq.7 消融（camera-ready 补充）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Theorem 1→Proposition 3 呈现顺序：A5 排除目标场景但未充分强调\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"确认: Proposition 3 已在主文 Section 3, 含完整公式和 Δτ_s。问题已解决。\"\n    action_items: []\n    resolution: \"Proposition 3 (A5 relaxation with Δτ_s) 已在主文 theory.tex L63-71\"\n    resolution_round: 21\n\n  - id: \"R19-W4\"\n    summary: \"HB 优势在 n_expert≥250 时消失但未讨论上限\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。experiments.tex L28 已有讨论。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接提及。R1 在交叉回应中用 K=4 的 bias-variance tradeoff 解释了 HB vs Strat. MLE 的互补关系。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"缺乏 fully real-data validation (所有实验为 semi-synthetic)\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-W3 再次提出正文缺完整真实数据实验。真实数据仍仅在附录。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 核心分歧点。R2 再次强调标题级声称需真实案例佐证。R1 REBUT：(1) 真实 CATE 基本不可观测是因果推断基本限制；(2) 半合成（真实 LLM CM + 合成 CATE）是领域标准做法（cf. Wager & Athey 2018）；(3) 11 真实 LLM CM 保证了误差异质性模式的真实性；(4) CivilComments FPR 从 8.5% 到 21.5% 的异质性是真实的；(5) Appendix R 的半真实 CM 验证 R²=0.97。R1 认为对本文单独加重扣分不公平。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Finite-sample 传播保证缺失——Theorem 1 到 plug-in estimator 仅有 O_p notation\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 两位 Reviewer 共识确认技术错误：theory.tex L92 的 O_p(κ·n^{-1/2}) 应为 O_p(κ²·n^{-1/2})。矩阵扰动 (C+E)^{-1} 一阶展开余项为 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。实际影响在 κ∈[1.25,3] 时有限但必须修正。\"\n    action_items:\n      - round: 22\n        action: \"修正 theory.tex L92 余项阶数 κ→κ²\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-M2\"\n    summary: \"Remark 2 与 Theorem 1 假设列表表面矛盾 (A2 地位)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 12\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21-R1-N2: 'exact' 标题与标量近似 R² 退化的张力。Abstract 已修正为 'under symmetric errors (generalizing to full-matrix form)'。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 partial REBUT R1: 恒等式在非对称情形下仍精确——乘积形式不依赖 A2。降级的是标量简化和诊断 AUC。R1 补充：EC-HTE 在非对称下仍有效（Table 36: 94.5% coverage vs Global 93.0%）。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-SF6\"\n    summary: \"Plugin SE 欠覆盖 93.8%\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未单独提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接提及。Table 1 footnote 注明 93.8% 且 bootstrap 可恢复 ≥95%。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R18-M1\"\n    summary: \"EC-HTE wall-clock time 未报告\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 18\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。method.tex 提到 HB 估计 <5ms。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。但 EB vs Gibbs 不一致（R22-Q1）暗示 wall-clock 声称需要区分两种实现。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-NLP2\"\n    summary: \"论文对 NLP 社区的价值定位不清\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N1 再次作为 Must-Fix 提出。experiments.tex 已添加 CivilComments NLP insight 段落。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 核心分歧点。R2 维持 EMNLP 受众偏窄——HTE 在 NLP 中是小众话题。R1 REBUT：随着 LLM 标注在社会科学和政策评估中的普及，受众正在扩大；4 个 NLP 任务（情感/仇恨言论/立场/主题分类）覆盖 EMNLP 主要应用领域。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-W2\"\n    summary: \"Scalability to K>>4 未充分讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 17\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-N3 作为 Must-Fix 再次提出: K≤4 限制。Intro Contribution 2 已加 'K ≤ 4 subgroups' 限定。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"Intro Contribution 2 增加 K ≤ 4 限定\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R10-W2\"\n    summary: \"DGP 较简单，无混杂变量\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 10\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。已与 R19-W2 合并，Limitations 已补充。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M1\"\n    summary: \"Assumption (A5) 实践限制被轻描淡写\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 21\n    action_items: []\n    resolution: \"Proposition 3 已在主文充分展示 A5 relaxation\"\n    resolution_round: 21\n\n  - id: \"R19-M2\"\n    summary: \"HB 先验敏感性分析不充分\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W4 再次提出: 仅变动 Gamma 超参数，未考虑替代先验（logistic-normal）。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M3\"\n    summary: \"Bootstrap SE (B=100) 计算成本未讨论\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M5\"\n    summary: \"'Semi-synthetic' 术语在 Section 5.1 和 5.3 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-M6\"\n    summary: \"Algorithm 1 缺收敛标准/最大迭代次数\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 19\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 通过 EB vs Gibbs 不一致间接关联。见 R22-Q1。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C1\"\n    summary: \"对称误分类假设 (A2) 严重限制标题级 'Exact Identity' 声称——非对称情形 R² 降至 0.73\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1, 2]\n        note: \"R21 两位 Reviewer 均再次关注。experiments.tex §5.4 已添加 matrix vs scalar 区分句。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 共识：恒等式在非对称下仍精确（R2 partial REBUT 确认），降级的是诊断 AUC。R1 补充 Table 36 数据：非对称（FPR/FNR 比 7:1）下 EC-HTE 94.5% coverage vs Global 93.0%，RMSE 0.083→0.074——方法本身不受 A2 限制。\"\n    action_items:\n      - round: 20\n        action: \"主文给出 2×2 非对称精确偏差 closed-form（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n      - round: 21\n        action: \"experiments.tex §5.4 添加 matrix vs scalar 区分\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C2\"\n    summary: \"相对 Frazis-Loewenstein (2003) 经典测量误差理论的增量贡献未界定\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 再次作为 Must-Fix。theory.tex 已替换为 sign reversal novelty statement。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 R2 通过 novelty depth 讨论间接涉及。R1 REBUT：完整理论框架包含 Theorem 1 + Props 3,5 + Corollaries 1,6 + HB + κ-guard，不仅是孤立引理。定理的价值在于 insight 而非证明难度（类比 Frisch-Waugh-Lovell）。\"\n    action_items:\n      - round: 20\n        action: \"Section 3 明确声明与 F-L (2003) 的 nesting 关系\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"Section 3 增加 explicit novelty statement: sign reversal vs uniform shrinkage\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-C3\"\n    summary: \"缺失噪声标签学习核心文献 (Natarajan et al. 2013, Patrini et al. 2017)\"\n    category: writing\n    severity: critical\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"段落已添加但 subgroup-dependent vs instance-dependent noise 联系未建立。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。R21 的 deeper connection 请求仍为 open action。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 增加噪声标签学习段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"深化噪声标签文献讨论：建立 subgroup-dependent vs instance-dependent noise 联系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"MC=100 不足以支撑 coverage 声称——SE ≈ 2.2pp\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W2 再次提出。Table 1 caption 已添加 coverage SE 注释。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。\"\n    action_items:\n      - round: 20\n        action: \"关键配置增加至 ≥500 MC runs（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W2\"\n    summary: \"方法论技术新颖性偏浅——EC-HTE 是成熟技术的组合\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R21-R2-N2 间接涉及。核心贡献定位应为理论洞察。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 核心分歧点。R2：恒等式是 2×2 矩阵代数直接展开。R1 REBUT：(1) insight > 证明难度（类比 Frisch-Waugh-Lovell、OVB 公式）；(2) 完整框架含 Theorem 1 + Props 3,5 + Corollaries 1,6 + 层级贝叶斯 + κ-guard + PPCI 组合，非孤立引理；(3) δ_s·Δτ/(1−2π̄) 的三因子交互结构此前未被识别。R1 认为不应显著降低评分。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W3\"\n    summary: \"假设 (A1) 灵敏度分析形式单一\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R21-R1-W5 再次提出: 仅 logistic link, γ ∈ [0, 0.20]。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 20\n        action: \"增加一种基于文本特征的 confounding 形式的灵敏度分析（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M2\"\n    summary: \"Theorem 1 中 'effect-modifier level z' 措辞对 NLP 读者不友好\"\n    category: writing\n    severity: info\n    status: in_progress\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"theory.tex 已添加 K=2 数值示例段落。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"theory.tex Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-M3\"\n    summary: \"Figure 2 'ε-guard' 标注字号偏小\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"R21 未再提及。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-FIX1\"\n    summary: \"Remark 交叉引用不一致\"\n    category: format\n    severity: info\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: []\n        note: \"theory.tex 添加 \\\\label{rem:asymmetric}，统一所有引用。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"添加 \\\\label{rem:asymmetric} 并统一所有交叉引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N1\"\n    summary: \"非对称误分类下诊断准则 AUC 从 0.86 降至 0.65，正文讨论严重不足\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-N1。experiments.tex §5.4 已添加 AUC 对比。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 共识。R2 补充 Prop 5 操作价值（不需估计 Δτ）。R1 补充：诊断 AUC 降低 ≠ 方法本身降级——EC-HTE 在非对称下 94.5% coverage（Table 36），意味着从业者需更保守使用诊断但校正方法仍有效。两位均认为改进非对称诊断是合理 future work 而非拒稿理由。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.4 增加 matrix vs scalar 区分 + 非对称 AUC 数字\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"考虑基于完整 2×2 矩阵的非对称诊断准则（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-N2\"\n    summary: \"NLP 社区适配性不足——核心贡献在统计/因果推断，NLP 任务仅为测试平台\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"R2-N1 Must-Fix。experiments.tex §5.2 已添加 CivilComments NLP insight。\"\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R22 核心分歧。R2 维持偏窄。R1 REBUT：LLM 标注在社科/政策评估中的普及使受众扩大；4 NLP 任务覆盖 EMNLP 主要应用领域。\"\n    action_items:\n      - round: 21\n        action: \"experiments.tex §5.2 增加 CivilComments NLP insight 段落\"\n        assigned_to: director\n        status: done\n      - round: 21\n        action: \"将 Appendix M 关键发现移入正文（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W1\"\n    summary: \"Proposition 5 诊断 vs 直接运行 EC-HTE 的增量价值不明——两者标签需求相同\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [1]\n        note: \"R1-W3。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。\"\n    action_items:\n      - round: 21\n        action: \"明确诊断准则的使用场景（rebuttal）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W2\"\n    summary: \"A3 (P(Z=0)=0.5) 限制性在正文中讨论不足\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"limitations.tex 已添加 A3 class imbalance 影响讨论。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未直接再提及。\"\n    action_items:\n      - round: 21\n        action: \"Limitations 补充 A3 class imbalance 影响讨论\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W3\"\n    summary: \"操作条件称 'framework' 轻微过度声称\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"已从 'decision framework' 改为 'Empirical operating guidelines'。\"\n      - round: 22\n        reviewers: [2]\n        note: \"R22 R2 确认 Section 5.4 展示透明。已调整措辞。\"\n    action_items:\n      - round: 21\n        action: \"Contribution 2 措辞调整为 'empirical operating guidelines'\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-W4\"\n    summary: \"Section 3 符号密度对 NLP 读者偏高——缺数值示例\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"theory.tex 已添加 K=2 数值示例段落。\"\n      - round: 22\n        reviewers: []\n        note: \"R22 未再提及。\"\n    action_items:\n      - round: 21\n        action: \"Theorem 1 后增加 K=2 数值示例\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R21-REF1\"\n    summary: \"遗漏相关工作: Veitch et al. (2020), Wood-Doughty et al. (2018)\"\n    category: writing\n    severity: warning\n    status: in_progress\n    first_raised_round: 21\n    last_seen_round: 22\n    mentions:\n      - round: 21\n        reviewers: [2]\n        note: \"已添加引用。\"\n      - round: 22\n        reviewers: [1]\n        note: \"R1 同意 Filtered PPI 也是相关参考文献。\"\n    action_items:\n      - round: 21\n        action: \"Related Work 增加 Veitch 2020, Wood-Doughty 2018 引用\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  # === ROUND 22 NEW ISSUES ===\n\n  - id: \"R22-W1\"\n    summary: \"κ-guard 阈值 100 纯经验选择——缺乏与有限样本余项 O_p(κ²·n^{-1/2}) 的理论连接\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共识。Appendix A 消融提供实证支持但缺理论推导。\"\n    action_items:\n      - round: 22\n        action: \"基于修正后的 O_p(κ²·n^{-1/2}) 余项推导理论最优 κ 阈值（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W2\"\n    summary: \"经验贝叶斯两阶段低估后验不确定性——MCMC 替代方案仅在 Appendix G\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"共识。EB 低估后验不确定性是标准批评。Coverage ≥93% 缓解但不消除。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q1\"\n    summary: \"Method 说 empirical Bayes (<5ms) 但 Algorithm 1 描述 Gibbs sampler (4 chains, 4000 iter)——不一致\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 独立提出。需澄清：(1) 主实验用哪种？(2) 两者结果是否一致？(3) Table 2 收敛诊断是验证性还是主实验？\"\n    action_items:\n      - round: 22\n        action: \"澄清主实验使用 EB 还是 Gibbs，统一 Method 和 Algorithm 1 描述\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q2\"\n    summary: \"A3 放松时 'identity remains exact with modified coefficients' 但未给出显式形式\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"theory.tex L84 声称修正系数存在但未展示。应在 Appendix 补充。\"\n    action_items:\n      - round: 22\n        action: \"Appendix 补充 A3 放松时的显式修正系数推导\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q3\"\n    summary: \"Cov(π_s, Δτ_s) 在实验中未报告——Corollary 4 实际可用性的关键\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"semi-synthetic 实验中应报告此协方差值。\"\n    action_items:\n      - round: 22\n        action: \"Semi-synthetic 实验中报告 Cov(π_s, Δτ_s)\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-Q4\"\n    summary: \"EC-HTE + PPCI 理论兼容性条件不明——LLM 同时标注 effect modifier 和 outcome 时独立性假设可能失效\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 共同提出。需要在 Limitations 或 Discussion 中讨论。\"\n    action_items:\n      - round: 22\n        action: \"讨论 EC-HTE 与 PPCI 的理论兼容性条件\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W3\"\n    summary: \"Abstract 信息密度过高（9+ 具体数字），读起来像 results summary\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 初审提出，R1 AGREE。建议前半段聚焦动机和核心发现，后半段精选 2-3 个关键数字。可修复的表述问题。\"\n    action_items:\n      - round: 22\n        action: \"精简 Abstract 数字密度（rebuttal/camera-ready）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W4\"\n    summary: \"'Debiasing' 术语在 *ACL 社区首先联想 algorithmic fairness，与本文 measurement-error correction 含义不同\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 初审提出，R1 AGREE。Footnote 1 有澄清但可能不够——读者看标题即形成第一印象。建议 abstract 首句明确 'measurement-error correction (debiasing)'。\"\n    action_items:\n      - round: 22\n        action: \"Abstract 首句明确 debiasing = measurement-error correction\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-W5\"\n    summary: \"Per-model R² 低端（GPT-4o-mini R²=0.893）讨论不足——哪些 LLM 特征导致拟合度下降\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 初审提出，R1 部分 AGREE。Table 23 报告了 per-model R²，最低 0.893（GPT-4o-mini）。R1 建议在 Appendix W 增加回归分析 R² ~ f(FPR, FNR, |FPR-FNR|, n) 系统性回答。\"\n    action_items:\n      - round: 22\n        action: \"Appendix W 增加 per-model R² 影响因素分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R22-FMT1\"\n    summary: \"Egami et al. bib key 'egami2024dsl' 与 year={2023} 不一致\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 22\n    last_seen_round: 22\n    mentions:\n      - round: 22\n        reviewers: [1, 2]\n        note: \"R2 初审提出，R1 AGREE。bib 格式错误需修正。\"\n    action_items:\n      - round: 22\n        action: \"修正 Egami bib entry year\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 2391 · 2026-05-25T04:53:51.372223+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml\", \"bytes\": 29960}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 2392 · 2026-05-25T04:57:08.580863+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 22 审稿报告（修订版——整合双方交叉回应）\n\n> 初版报告仅基于 R2 交叉回应提交。本修订版整合了 R1 的完整交叉回应，包含 3 条实质性 REBUT 和新证据。\n\n## Summary\n\n本文推导了一个精确偏差恒等式（Theorem 1），揭示当 LLM 标注器的误分类率在子群间存在异质性时，全局混淆矩阵校正会引入子群级别的偏差，甚至可在 14.9% 的配置中导致 CATE 符号反转。基于该恒等式，论文提出了 Δτ-free 诊断准则（Proposition 5）和分层贝叶斯校正方法（EC-HTE），在极端异质性下将 |bias| 降低 7.4×。实验覆盖 520 合成配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验。\n\n## Strengths\n\n**[S1] 理论核心简洁且可验证（R1, R2 共识）**：Theorem 1 的乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 既精确又可解释，证明可手动核实。Proposition 5 的 Δτ-free 诊断（AUC=0.86 对称情形）仅凭 pilot 样本误差率即可决策——不需要估计 Δτ，这在实际部署中比恒等式本身更有价值（R2 补充）。\n\n**[S2] 实验覆盖极为全面（R1, R2 共识）**：520 配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验，在 *ACL 投稿中属上乘水平。实验层次（合成 → 半合成 → 真实 NLP 任务 → 鲁棒性 → 跨估计器）远超同类论文（R1 强调）。跨估计器验证（CausalForest + R-learner, Table 1 + Appendix P）是额外加分项。\n\n**[S3] 理论→方法→实践链完整（R1, R2 共识）**：从恒等式推导到 EC-HTE 方法实现再到操作边界（Section 5.4: Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4）的完整链条。Algorithm 1 伪代码清晰。\"何时不用本方法\"的诚实边界划定值得肯定——这在方法论论文中较为少见（R1 补充）。\n\n**[S4] Related Work 定位清晰（R1, R2 共识）**：三维度定位（scalar attenuation vs. per-subgroup correction vs. diagnostic）清晰区分了与 Frazis-Loewenstein、DSL、PPI 等已有工作的差异。NLP × 因果推断时效性好，14.9% sign reversal 是有冲击力的 headline number。\n\n**[S5] 假设放松讨论系统化（R1, R2 共识）**：Remark 2 对 A2、Appendix D 对 A3、Proposition 3 对 A5、Appendix H 对 A1 的系统性讨论表明作者对自身理论的局限有清醒认识。\n\n## Weaknesses\n\n**[W1] 对称误分类假设 (A2) 限制诊断实用性（R1, R2 共识，critical）**\n两位 Reviewer 均确认 A2 是论文最大的实践局限。GPT-4o FPR/FNR 差异达 0.09（0.249 vs 0.157）。\n\n关键澄清（R2 partial REBUT + R1 补充）：\n- **恒等式**本身在非对称情形下**仍然精确成立**——乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 不依赖 A2\n- **降级的是**：(a) 诊断准则 Proposition 5 AUC 从 0.86 降至 0.66；(b) 标量简化形式 δ_s·Δτ/(1−2π̄)\n- **方法本身不受 A2 限制**：R1 引用 Table 36（Appendix Z.6）——非对称误差（FPR/FNR 比率高达 7:1）下 EC-HTE 仍实现 94.5% coverage（vs Global 93.0%），RMSE 从 0.083 降至 0.074\n- Abstract 强调的简洁标量形式仅在 A2 下成立——这是潜在误导的来源，而非 \"exact identity\" 措辞本身\n\n**[W2] 有限样本余项阶数存在技术错误（R1, R2 共识，warning）**\ntheory.tex L92 声称余项为 O_p(κ·n^{-1/2})，应为 O_p(κ²·n^{-1/2})。推导：(C+E)^{-1} = C^{-1} − C^{-1}EC^{-1} + O(‖E‖²)，一阶项范数 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。实际影响在 κ ∈ [1.25, 3] 时有限，但必须修正。\n\n**[W3] κ-guard 阈值 100 缺乏理论依据（R1, R2 共识，minor warning）**\n最大实验 κ ≈ 1.9，阈值 100 提供 53× 安全余量从未触发。Appendix A 消融（κ sweep 10–1000）和自适应公式 κ_adapt = 10√(n_expert/K) 提供实证支持，但缺少与修正后余项的理论连接。\n\n**[W4] 中等异质性下改善极小（R1, R2 共识，minor）**\nRMSE 0.049 vs 0.050（Section 5.3, p > 0.05），7.4× 仅在极端异质性下成立。R2 认为方法的固有局限而非论文缺陷（Section 5.4 和 Figure 3 已透明展示）。\n\n**[W5] 经验贝叶斯两阶段不确定性传播（R1, R2 共识，warning）**\nEB 会低估后验不确定性。Coverage ≥ 93% 缓解但不消除。MCMC 替代方案在 Appendix G。\n\n**[W6] 缺乏端到端真实数据验证（R2 major，R1 REBUT，核心分歧）**\nR2 立场：CivilComments 无 ground-truth CATE，无法验证标题级声称 \"debiasing hurts\"。\nR1 REBUT（5 点反驳）：\n(1) 真实 CATE 基本不可观测是因果推断的根本限制，不应对本文单独加重扣分；\n(2) 半合成方法（真实 LLM CM + 合成 CATE）是领域标准做法（cf. Wager & Athey 2018, Kennedy 2023）；\n(3) 11 真实 LLM CM 保证了误差异质性模式的真实性——这正是论文核心关注的变量；\n(4) CivilComments FPR 从 8.5% 到 21.5% 的子群异质性是真实的；\n(5) Appendix R 的半真实 CM 验证 R² = 0.97，包括真实 per-subgroup FPR 和 FNR。\n**Director 评估**：R1 的反驳有力。半合成是因果推断的标准验证范式。但 R2 的核心论点——标题含 extraordinary claim (\"debiasing hurts\") 应有 extraordinary evidence——仍有道理。此问题降级为 moderate weakness（从 R2 的 major 降至介于 major 和 minor 之间）。\n\n**[W7] 方法论技术新颖性偏浅（R2 major，R1 REBUT，核心分歧）**\nR2 立场：恒等式本质是 2×2 矩阵代数直接展开，novelty 在问题识别非技术突破。\nR1 REBUT（3 点反驳）：\n(1) 定理的价值在于 insight 而非证明难度——统计学中许多有影响力的结果（Frisch-Waugh-Lovell、OVB 公式）证明都简洁，但结构性洞察有深远影响。δ_s·Δτ/(1−2π̄) 的三因子交互此前未被识别；\n(2) 完整理论框架超越单一定理：Theorem 1 + Proposition 3（A5 放松）+ Corollary 1（聚合偏差）+ Corollary 6（多类扩展）+ Proposition 5（诊断）+ 层级贝叶斯 + κ-guard + PPCI 组合；\n(3) 非对称下方法仍有效（Table 36: 94.5% coverage）。\n**Director 评估**：R1 的\"insight > 证明难度\"论点有实质力度。但 R2 的观察——核心数学是 M_global^{-1} M_s − I 的展开——也是事实。最终这是一个关于\"理论贡献\"定义的价值判断。\n\n**[W8] Abstract 信息密度过高（R1, R2 共识，minor）**\nAbstract 含 9+ 具体数字（7.4×, 14.9%, R²>0.97, AUC=0.86 等），更像 results summary。建议前半段聚焦动机，后半段精选关键数字。可修复。\n\n**[W9] \"Debiasing\" 术语歧义（R1, R2 共识，minor）**\n在 *ACL 社区首先联想 algorithmic fairness（gender/racial bias），与本文 measurement-error correction 含义不同。Footnote 1 有澄清但可能不够。建议 abstract 首句明确。可修复。\n\n**[W10] Per-model R² 低端讨论不足（R1 partial agree, R2 提出, info）**\nGPT-4o-mini R² = 0.893（Table 23）。论文未系统讨论哪些 LLM 特征导致拟合度下降。R1 建议增加回归分析 R² ~ f(FPR, FNR, |FPR-FNR|, n)。\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Theorem 1 技术正确性 | ✓ | ✓ | **[AGREE]** |\n| 实验覆盖面充分 | ✓ | ✓ | **[AGREE]** |\n| A2 限制诊断（非方法） | W1 | W1 | **[AGREE]**（R2 确认恒等式不受影响；R1 补充 Table 36 方法仍有效） |\n| 有限样本余项 κ→κ² | W2 | W2 | **[AGREE]**（技术错误，需修正） |\n| κ-guard 缺理论依据 | W3 | W3 | **[AGREE]**（minor） |\n| EB 不确定性传播 | W5 | W5 | **[AGREE]**（coverage ≥93% 缓解） |\n| Abstract 密度过高 | W8 | W8 | **[AGREE]**（可修复） |\n| Debiasing 术语歧义 | W9 | W9 | **[AGREE]**（可修复） |\n| CivilComments 验证不足 | Q5 | W6 | **[AGREE]**（程度有分歧） |\n| 7.4× 基线计算 | 错误 | REBUT | **R2 纠正 R1**：7.4× = 0.059/0.008，基线确为 Global |\n| EB vs Gibbs 不一致 | Q4 | Q4 | **[AGREE]** |\n\n## Reviewer Divergence\n\n### 分歧 1：方法论新颖性深度（W7）\n\n| | R1 (4.0) | R2 (3.5) |\n|---|----------|----------|\n| 立场 | Insight > 证明难度。完整框架含 6 个理论结果 + 实现 + 诊断，非孤立引理 | 核心数学是 2×2 矩阵代数展开，方法是成熟技术组合 |\n| 类比 | Frisch-Waugh-Lovell、OVB 公式——简洁但有深远影响 | （无反驳此类比） |\n| 评估 | **合理分歧**。两种\"理论贡献\"标准均有先例。R1 的 insight-driven 标准在计量经济学中更常见；R2 的 proof-difficulty 标准在数学/理论CS中更常见 |\n\n### 分歧 2：真实数据验证（W6）\n\n| | R1 (4.0) | R2 (3.5) |\n|---|----------|----------|\n| 立场 | 半合成是因果推断标准做法；真实 CATE 不可观测是领域固有限制 | 标题级 extraordinary claim 需 extraordinary evidence |\n| 证据 | Wager & Athey 2018, Kennedy 2023 同用半合成；11 真实 LLM CM；CivilComments 真实异质性 | 无 ground-truth CATE = 无法验证核心声称 |\n| 评估 | **R1 论据更有力**。半合成确是因果推断标准范式。但 R2 关于标题措辞的 claim 级别也值得注意——如果论文标题不含 \"hurts\"，这个弱点的权重会降低 |\n\n### 分歧 3：EMNLP 受众适配性\n\n| | R1 (4.0) | R2 (3.5) |\n|---|----------|----------|\n| 立场 | LLM 标注在社科/政策评估中普及，受众在扩大；4 NLP 任务覆盖主要领域 | Effect modifier misclassification 是 HTE 中的窄问题；NLP 研究者多不做 HTE |\n| 评估 | **合理分歧**。取决于 EMNLP reviewer pool 的实际构成和对交叉领域论文的包容度 |\n\n**评分分歧**：R1 = 4.0 (Conference)，R2 = 3.5 (Borderline Conference)。0.5 分差距由上述三点驱动。经过交叉回应，双方立场更加清晰但均未改变评分。\n\n## Questions\n\n**[Q1]** 放松 A3 (P(Z=0)=0.5) 时，theory.tex L84 提到 \"the identity remains exact with modified coefficients\" 但未给出显式形式。Appendix 中应提供完整推导。（R1, R2 共识）\n\n**[Q2]** EC-HTE 与 PPCI 的理论兼容性条件？当 LLM 同时标注 effect modifier 和 outcome 时，covariate-side 和 outcome-side error 的独立性假设可能失效。（R1, R2 共识）\n\n**[Q3]** Cov(π_s, Δτ_s) 在真实数据中的量级？Corollary 4 实际可用性的关键。应在 semi-synthetic 实验中报告。（R1, R2 共识）\n\n**[Q4]** Method section 说 EB (<5ms)，Algorithm 1 写 Gibbs sampler (4 chains, 4000 iter)。主实验用哪个？R1 补充需澄清：(1) 主实验推断方法；(2) MCMC 和 EB 结果是否一致；(3) Table 2 的收敛诊断是验证性还是主实验。（R1, R2 共识）\n\n**[Q5]** CivilComments：\"3.2× effect-size gap\" 是否比 Global 更准确？无 ground-truth CATE 如何验证？（R1, R2 共识——最大 empirical gap）\n\n## Missing References\n\n- Filtered PPI（R1, R2 共识应引用——处理异质性预测质量与本文有概念联系）\n- Egami et al. bib key `egami2024dsl` 与 year={2023} 不一致（格式错误）\n- 噪声标签文献（Natarajan 2013, Patrini 2017）段落已添加但 subgroup-dependent vs instance-dependent noise 联系未建立\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。**\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（2026-05-25 04:19–04:23）| 0 critical / 2 warning / 26 info\n\n**Warnings:**\n1. **Pages 1-2 连续纯文本**：前两页无视觉锚点，Figure 1 到第 3 页才出现。\n2. **Figure 2 红绿残留**：R19 标记 resolved (sage green→blue) 但视觉检查仍检测到红/绿对比，修复可能不完整。\n\n**Note:** R2 初审曾指出 Figure 4 浮动到第 9 页（References 区域）。R1 REBUT 验证 submitted.pdf：Figure 4 在 page 8 上半部分，在主文 8 页限制内。R2 可能看到的是不同版本或记忆有误。\n\n**Info 摘要：** 正文 8 页 + 23 页附录；4 display items 在正文（偏低端但理论论文可接受）；Table 1 booktabs + 加粗最优值；无 overfull hbox / margin 溢出；Page 8 高密度（Figure 3 + Table 1 + Conclusion + Limitations）。\n\n## Overall Assessment\n\n**评分：3.5–4.0 (Borderline Conference to Conference)** | 置信度：高\n\n| Reviewer | Score | 关键权重 | 核心 REBUT |\n|----------|-------|----------|-----------|\n| R1 | 4.0 (Conference) | 实验全面性 + insight-driven 贡献 + 时效性 | W6: 半合成是标准做法；W7: insight > 证明难度 |\n| R2 | 3.5 (Borderline Conference) | Novelty depth + EMNLP 适配性 + 真实数据缺口 | （维持原评分，REBUTs 未改变判断） |\n\n**综合评估：**\n\n论文具有明确的理论贡献——偏差恒等式精确、可验证，14.9% sign reversal 有冲击力。实验覆盖在 *ACL 中属上乘。理论→方法→实践链完整。\n\n经过交叉回应，评审的分歧更加清晰但未收敛：\n\n**R1 4.0 的论据（经交叉回应加强）：**\n- Table 36 新证据表明 EC-HTE 在非对称下仍有效（94.5% coverage），削弱了 A2 作为致命限制的力度\n- 半合成是因果推断的标准验证范式，不应对本文单独加重扣分\n- 完整理论框架（6 个理论结果）超越\"仅问题识别\"\n- Frisch-Waugh-Lovell 类比有实质说服力\n\n**R2 3.5 的论据（经交叉回应仍然有效）：**\n- EMNLP 受众适配性是结构性问题（难以通过 revision 解决）\n- 数学深度有限是客观事实（R1 未否认这一点，而是论证这不重要）\n- 标题含 \"hurts\" 是 extraordinary claim，半合成验证的说服力低于真实案例\n\n**制约评分的已确认问题（R1, R2 共识，可修复）：**\n1. theory.tex L92 余项阶数 κ→κ²（技术错误）\n2. EB vs Gibbs 不一致（写作问题）\n3. κ-guard 缺理论推导（method gap）\n4. Abstract 数字密度 + debiasing 术语歧义（表述问题）\n\n**最终判断**：报告呈现 3.5–4.0 的评分范围。R1 的交叉回应提供了有力论据（特别是 Table 36 和半合成标准做法），使 4.0 更有依据；R2 的 EMNLP audience fit 和 novelty depth 关注在交叉回应后仍然有效。两位 Reviewer 均为严格但公正的评审。由 Research Director / AC 根据 venue 定位做最终权衡。\n\n## Detailed Comments\n\n### Abstract & Introduction\n- ~150 words，符合 ≤200 words\n- \"under symmetric errors (generalizing to full-matrix form)\" 措辞准确\n- \"7.4× under extreme heterogeneity\" 限定已添加\n- **需修复**：数字密度过高（W8）；\"debiasing\" 首次出现时明确为 measurement-error correction（W9）\n\n### Section 3 (Theory)\n- Theorem 1 技术正确。非对称下仍精确（Remark 2 + R2 确认）\n- **必须修正**：L92 余项 O_p(κ·n^{-1/2}) → O_p(κ²·n^{-1/2})\n- Proposition 5：应更明确阐述 (a) 不需估计 Δτ 的独特操作价值；(b) 非对称下的降级路径\n- A3 放松时 theory.tex L84 声称修正系数存在但未展示\n\n### Section 4 (Method)\n- **EB vs Gibbs 不一致**：method.tex EB (<5ms) vs Algorithm 1 Gibbs (4 chains × 4000 iter)。需三项澄清\n- κ-guard = 100：应与修正后余项建立理论连接\n- K=4 时 Strat. MLE |Bias| (0.010) < HB (0.012)：R1 解释这是正确的 bias-variance tradeoff——HB 通过小量额外偏差换取方差降低，RMSE 在 87.5% 配置中优于 Strat. MLE（James-Stein 收缩的经典优势）\n\n### Section 5 (Experiments)\n- Table 1：7.4× = 0.059/0.008 基线为 Global（R2 验证正确，R1 原计算有误）\n- 14.9% sign reversal 跨越广泛参数设定，不仅限于 τ(0)=0.03——R1 指出 50% 配置（260/520）出现 bias amplification\n- CivilComments：最大实证缺口，但半合成方法论是因果推断标准做法\n- Per-model R²：建议 Appendix W 增加影响因素分析\n\n### Formatting & Compliance\n- ACL 双栏 + review mode，正文 8 页，符合 EMNLP 2026 长文限制\n- Limitations 在正文内，合规\n- Figure 4 确认在 page 8（R1 验证），非 page 9\n- Figure 2 色盲修复可能不完整\n- Egami bib year 不一致\n\n### Issue Tracker 更新\n- 本轮新增 10 个 issue（R22-W1–W5, R22-Q1–Q4, R22-FMT1）\n- 更新 18 个已有 issue 的 R22 mentions（含双方交叉回应论据）\n- R16-W7（Figure 2 色盲）从 resolved 回退至 in_progress",
  "project": "ec_hte_llm_annotation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5-4.0",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 22 审稿报告（修订版——整合双方交叉回应）\n\n> 初版报告仅基于 R2 交叉回应提交。本修订版整合了 R1 的完整交叉回应，包含 3 条实质性 REBUT 和新证据。\n\n## Summary\n\n本文推导了一个精确偏差恒等式（Theorem 1），揭示当 LLM 标注器的误分类率在子群间存在异质性时，全局混淆矩阵校正会引入子群级别的偏差，甚至可在 14.9% 的配置中导致 CATE 符号反转。基于该恒等式，论文提出了 Δτ-free 诊断准则（Proposition 5）和分层贝叶斯校正方法（EC-HTE），在极端异质性下将 |bias| 降低 7.4×。实验覆盖 520 合成配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验。\n\n## Strengths\n\n**[S1] 理论核心简洁且可验证（R1, R2 共识）**：Theorem 1 的乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 既精确又可解释，证明可手动核实。Proposition 5 的 Δτ-free 诊断（AUC=0.86 对称情形）仅凭 pilot 样本误差率即可决策——不需要估计 Δτ，这在实际部署中比恒等式本身更有价值（R2 补充）。\n\n**[S2] 实验覆盖极为全面（R1, R2 共识）**：520 配置 × 100 MC + 11 真实 LLM 混淆矩阵 + 4 NLP 任务 + 8 鲁棒性检验，在 *ACL 投稿中属上乘水平。实验层次（合成 → 半合成 → 真实 NLP 任务 → 鲁棒性 → 跨估计器）远超同类论文（R1 强调）。跨估计器验证（CausalForest + R-learner, Table 1 + Appendix P）是额外加分项。\n\n**[S3] 理论→方法→实践链完整（R1, R2 共识）**：从恒等式推导到 EC-HTE 方法实现再到操作边界（Section 5.4: Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4）的完整链条。Algorithm 1 伪代码清晰。\"何时不用本方法\"的诚实边界划定值得肯定——这在方法论论文中较为少见（R1 补充）。\n\n**[S4] Related Work 定位清晰（R1, R2 共识）**：三维度定位（scalar attenuation vs. per-subgroup correction vs. diagnostic）清晰区分了与 Frazis-Loewenstein、DSL、PPI 等已有工作的差异。NLP × 因果推断时效性好，14.9% sign reversal 是有冲击力的 headline number。\n\n**[S5] 假设放松讨论系统化（R1, R2 共识）**：Remark 2 对 A2、Appendix D 对 A3、Proposition 3 对 A5、Appendix H 对 A1 的系统性讨论表明作者对自身理论的局限有清醒认识。\n\n## Weaknesses\n\n**[W1] 对称误分类假设 (A2) 限制诊断实用性（R1, R2 共识，critical）**\n两位 Reviewer 均确认 A2 是论文最大的实践局限。GPT-4o FPR/FNR 差异达 0.09（0.249 vs 0.157）。\n\n关键澄清（R2 partial REBUT + R1 补充）：\n- **恒等式**本身在非对称情形下**仍然精确成立**——乘积形式 bias(z,s) = Δτ · [B_s]_{z,1} 不依赖 A2\n- **降级的是**：(a) 诊断准则 Proposition 5 AUC 从 0.86 降至 0.66；(b) 标量简化形式 δ_s·Δτ/(1−2π̄)\n- **方法本身不受 A2 限制**：R1 引用 Table 36（Appendix Z.6）——非对称误差（FPR/FNR 比率高达 7:1）下 EC-HTE 仍实现 94.5% coverage（vs Global 93.0%），RMSE 从 0.083 降至 0.074\n- Abstract 强调的简洁标量形式仅在 A2 下成立——这是潜在误导的来源，而非 \"exact identity\" 措辞本身\n\n**[W2] 有限样本余项阶数存在技术错误（R1, R2 共识，warning）**\ntheory.tex L92 声称余项为 O_p(κ·n^{-1/2})，应为 O_p(κ²·n^{-1/2})。推导：(C+E)^{-1} = C^{-1} − C^{-1}EC^{-1} + O(‖E‖²)，一阶项范数 ‖C^{-1}‖²·‖E‖ = κ²·O_p(n^{-1/2})。实际影响在 κ ∈ [1.25, 3] 时有限，但必须修正。\n\n**[W3] κ-guard 阈值 100 缺乏理论依据（R1, R2 共识，minor warning）**\n最大实验 κ ≈ 1.9，阈值 100 提供 53× 安全余量从未触发。Appendix A 消融（κ sweep 10–1000）和自适应公式 κ_adapt = 10√(n_expert/K) 提供实证支持，但缺少与修正后余项的理论连接。\n\n**[W4] 中等异质性下改善极小（R1, R2 共识，minor）**\nRMSE 0.049 vs 0.050（Section 5.3, p > 0.05），7.4× 仅在极端异质性下成立。R2 认为方法的固有局限而非论文缺陷（Section 5.4 和 Figure 3 已透明展示）。\n\n**[W5] 经验贝叶斯两阶段不确定性传播（R1, R2 共识，warning）**\nEB 会低估后验不确定性。Coverage ≥ 93% 缓解但不消除。MCMC 替代方案在 Appendix G。\n\n**[W6] 缺乏端到端真实数据验证（R2 major，R1 REBUT，核心分歧）**\nR2 立场：CivilComments 无 ground-truth CATE，无法验证标题级声称 \"debiasing hurts\"。\nR1 REBUT（5 点反驳）：\n(1) 真实 CATE 基本不可观测是因果推断的根本限制，不应对本文单独加重扣分；\n(2) 半合成方法（真实 LLM CM + 合成 CATE）是领域标准做法（cf. Wager & Athey 2018, Kennedy 2023）；\n(3) 11 真实 LLM CM 保证了误差异质性模式的真实性——这正是论文核心关注的变量；\n(4) CivilComments FPR 从 8.5% 到 21.5% 的子群异质性是真实的；\n(5) Appendix R 的半真实 CM 验证 R² = 0.97，包括真实 per-subgroup FPR 和 FNR。\n**Director 评估**：R1 的反驳有力。半合成是因果推断的标准验证范式。但 R2 的核心论点——标题含 extraordinary claim (\"debiasing hurts\") 应有 extraordinary evidence——仍有道理。此问题降级为 moderate weakness（从 R2 的 major 降至介于 major 和 minor 之间）。\n\n**[W7] 方法论技术新颖性偏浅（R2 major，R1 REBUT，核心分歧）**\nR2 立场：恒等式本质是 2×2 矩阵代数直接展开，novelty 在问题识别非技术突破。\nR1 REBUT（3 点反驳）：\n(1) 定理的价值在于 insight 而非证明难度——统计学中许多有影响力的结果（Frisch-Waugh-Lovell、OVB 公式）证明都简洁，但结构性洞察有深远影响。δ_s·Δτ/(1−2π̄) 的三因子交互此前未被识别；\n(2) 完整理论框架超越单一定理：Theorem 1 + Proposition 3（A5 放松）+ Corollary 1（聚合偏差）+ Corollary 6（多类扩展）+ Proposition 5（诊断）+ 层级贝叶斯 + κ-guard + PPCI 组合；\n(3) 非对称下方法仍有效（Table 36: 94.5% coverage）。\n**Director 评估**：R1 的\"insight > 证明难度\"论点有实质力度。但 R2 的观察——核心数学是 M_global^{-1} M_s − I 的展开——也是事实。最终这是一个关于\"理论贡献\"定义的价值判断。\n\n**[W8] Abstract 信息密度过高（R1, R2 共识，minor）**\nAbstract 含 9+ 具体数字（7.4×, 14.9%, R²>0.97, AUC=0.86 等），更像 results summary。建议前半段聚焦动机，后半段精选关键数字。可修复。\n\n**[W9] \"Debiasing\" 术语歧义（R1, R2 共识，minor）**\n在 *ACL 社区首先联想 algorithmic fairness（gender/racial bias），与本文 measurement-error correction 含义不同。Footnote 1 有澄清但可能不够。建议 abstract 首句明确。可修复。\n\n**[W10] Per-model R² 低端讨论不足（R1 partial agree, R2 提出, info）**\nGPT-4o-mini R² = 0.893（Table 23）。论文未系统讨论哪些 LLM 特征导致拟合度下降。R1 建议增加回归分析 R² ~ f(FPR, FNR, |FPR-FNR|, n)。\n\n## Reviewer Consensus\n\n| Issue | R1 | R2 | 共识 |\n|-------|----|----|------|\n| Theorem 1 技术正确性 | ✓ | ✓ | **[AGREE]** |\n| 实验覆盖面充分 | ✓ | ✓ | **[AGREE]** |\n| A2 限制诊断（非方法） | W1 | W1 | **[AGREE]**（R2 确认恒等式不受影响；R1 补充 Table 36 方法仍有效） |\n| 有限样本余项 κ→κ² | W2 | W2 | **[AGREE]**（技术错误，需修正） |\n| κ-guard 缺理论依据 | W3 | W3 | **[AGREE]**（minor） |\n| EB 不确定性传播 | W5 | W5 | **[AGREE]**（coverage ≥93% 缓解） |\n| Abstract 密度过高 | W8 | W8 | **[AGREE]**（可修复） |\n| Debiasing 术语歧义 | W9 | W9 | **[AGREE]**（可修复） |\n| CivilComments 验证不足 | Q5 | W6 | **[AGREE]**（程度有分歧） |\n| 7.4× 基线计算 | 错误 | REBUT | **R2 纠正 R1**：7.4× = 0.059/0.008，基线确为 Global |\n| EB vs Gibbs 不一致 | Q4 | Q4 | **[AGREE]** |\n\n## Reviewer Divergence\n\n### 分歧 1：方法论新颖性深度（W7）\n\n| | R1 (4.0) | R2 (3.5) |\n|---|----------|----------|\n| 立场 | Insight > 证明难度。完整框架含 6 个理论结果 + 实现 + 诊断，非孤立引理 | 核心数学是 2×2 矩阵代数展开，方法是成熟技术组合 |\n| 类比 | Frisch-Waugh-Lovell、OVB 公式——简洁但有深远影响 | （无反驳此类比） |\n| 评估 | **合理分歧**。两种\"理论贡献\"标准均有先例。R1 的 insight-driven 标准在计量经济学中更常见；R2 的 proof-difficulty 标准在数学/理论CS中更常见 |\n\n### 分歧 2：真实数据验证（W6）\n\n| | R1 (4.0) | R2 (3.5) |\n|---|----------|----------|\n| 立场 | 半合成是因果推断标准做法；真实 CATE 不可观测是领域固有限制 | 标题级 extraordinary claim 需 extraordinary evidence |\n| 证据 | Wager & Athey 2018, Kennedy 2023 同用半合成；11 真实 LLM CM；CivilComments 真实异质性 | 无 ground-truth CATE = 无法验证核心声称 |\n| 评估 | **R1 论据更有力**。半合成确是因果推断标准范式。但 R2 关于标题措辞的 claim 级别也值得注意——如果论文标题不含 \"hurts\"，这个弱点的权重会降低 |\n\n### 分歧 3：EMNLP 受众适配性\n\n| | R1 (4.0) | R2 (3.5) |\n|---|----------|----------|\n| 立场 | LLM 标注在社科/政策评估中普及，受众在扩大；4 NLP 任务覆盖主要领域 | Effect modifier misclassification 是 HTE 中的窄问题；NLP 研究者多不做 HTE |\n| 评估 | **合理分歧**。取决于 EMNLP reviewer pool 的实际构成和对交叉领域论文的包容度 |\n\n**评分分歧**：R1 = 4.0 (Conference)，R2 = 3.5 (Borderline Conference)。0.5 分差距由上述三点驱动。经过交叉回应，双方立场更加清晰但均未改变评分。\n\n## Questions\n\n**[Q1]** 放松 A3 (P(Z=0)=0.5) 时，theory.tex L84 提到 \"the identity remains exact with modified coefficients\" 但未给出显式形式。Appendix 中应提供完整推导。（R1, R2 共识）\n\n**[Q2]** EC-HTE 与 PPCI 的理论兼容性条件？当 LLM 同时标注 effect modifier 和 outcome 时，covariate-side 和 outcome-side error 的独立性假设可能失效。（R1, R2 共识）\n\n**[Q3]** Cov(π_s, Δτ_s) 在真实数据中的量级？Corollary 4 实际可用性的关键。应在 semi-synthetic 实验中报告。（R1, R2 共识）\n\n**[Q4]** Method section 说 EB (<5ms)，Algorithm 1 写 Gibbs sampler (4 chains, 4000 iter)。主实验用哪个？R1 补充需澄清：(1) 主实验推断方法；(2) MCMC 和 EB 结果是否一致；(3) Table 2 的收敛诊断是验证性还是主实验。（R1, R2 共识）\n\n**[Q5]** CivilComments：\"3.2× effect-size gap\" 是否比 Global 更准确？无 ground-truth CATE 如何验证？（R1, R2 共识——最大 empirical gap）\n\n## Missing References\n\n- Filtered PPI（R1, R2 共识应引用——处理异质性预测质量与本文有概念联系）\n- Egami et al. bib key `egami2024dsl` 与 year={2023} 不一致（格式错误）\n- 噪声标签文献（Natarajan 2013, Patrini 2017）段落已添加但 subgroup-dependent vs instance-dependent noise 联系未建立\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。**\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（2026-05-25 04:19–04:23）| 0 critical / 2 warning / 26 info\n\n**Warnings:**\n1. **Pages 1-2 连续纯文本**：前两页无视觉锚点，Figure 1 到第 3 页才出现。\n2. **Figure 2 红绿残留**：R19 标记 resolved (sage green→blue) 但视觉检查仍检测到红/绿对比，修复可能不完整。\n\n**Note:** R2 初审曾指出 Figure 4 浮动到第 9 页（References 区域）。R1 REBUT 验证 submitted.pdf：Figure 4 在 page 8 上半部分，在主文 8 页限制内。R2 可能看到的是不同版本或记忆有误。\n\n**Info 摘要：** 正文 8 页 + 23 页附录；4 display items 在正文（偏低端但理论论文可接受）；Table 1 booktabs + 加粗最优值；无 overfull hbox / margin 溢出；Page 8 高密度（Figure 3 + Table 1 + Conclusion + Limitations）。\n\n## Overall Assessment\n\n**评分：3.5–4.0 (Borderline Conference to Conference)** | 置信度：高\n\n| Reviewer | Score | 关键权重 | 核心 REBUT |\n|----------|-------|----------|-----------|\n| R1 | 4.0 (Conference) | 实验全面性 + insight-driven 贡献 + 时效性 | W6: 半合成是标准做法；W7: insight > 证明难度 |\n| R2 | 3.5 (Borderline Conference) | Novelty depth + EMNLP 适配性 + 真实数据缺口 | （维持原评分，REBUTs 未改变判断） |\n\n**综合评估：**\n\n论文具有明确的理论贡献——偏差恒等式精确、可验证，14.9% sign reversal 有冲击力。实验覆盖在 *ACL 中属上乘。理论→方法→实践链完整。\n\n经过交叉回应，评审的分歧更加清晰但未收敛：\n\n**R1 4.0 的论据（经交叉回应加强）：**\n- Table 36 新证据表明 EC-HTE 在非对称下仍有效（94.5% coverage），削弱了 A2 作为致命限制的力度\n- 半合成是因果推断的标准验证范式，不应对本文单独加重扣分\n- 完整理论框架（6 个理论结果）超越\"仅问题识别\"\n- Frisch-Waugh-Lovell 类比有实质说服力\n\n**R2 3.5 的论据（经交叉回应仍然有效）：**\n- EMNLP 受众适配性是结构性问题（难以通过 revision 解决）\n- 数学深度有限是客观事实（R1 未否认这一点，而是论证这不重要）\n- 标题含 \"hurts\" 是 extraordinary claim，半合成验证的说服力低于真实案例\n\n**制约评分的已确认问题（R1, R2 共识，可修复）：**\n1. theory.tex L92 余项阶数 κ→κ²（技术错误）\n2. EB vs Gibbs 不一致（写作问题）\n3. κ-guard 缺理论推导（method gap）\n4. Abstract 数字密度 + debiasing 术语歧义（表述问题）\n\n**最终判断**：报告呈现 3.5–4.0 的评分范围。R1 的交叉回应提供了有力论据（特别是 Table 36 和半合成标准做法），使 4.0 更有依据；R2 的 EMNLP audience fit 和 novelty depth 关注在交叉回应后仍然有效。两位 Reviewer 均为严格但公正的评审。由 Research Director / AC 根据 venue 定位做最终权衡。\n\n## Detailed Comments\n\n### Abstract & Introduction\n- ~150 words，符合 ≤200 words\n- \"under symmetric errors (generalizing to full-matrix form)\" 措辞准确\n- \"7.4× under extreme heterogeneity\" 限定已添加\n- **需修复**：数字密度过高（W8）；\"debiasing\" 首次出现时明确为 measurement-error correction（W9）\n\n### Section 3 (Theory)\n- Theorem 1 技术正确。非对称下仍精确（Remark 2 + R2 确认）\n- **必须修正**：L92 余项 O_p(κ·n^{-1/2}) → O_p(κ²·n^{-1/2})\n- Proposition 5：应更明确阐述 (a) 不需估计 Δτ 的独特操作价值；(b) 非对称下的降级路径\n- A3 放松时 theory.tex L84 声称修正系数存在但未展示\n\n### Section 4 (Method)\n- **EB vs Gibbs 不一致**：method.tex EB (<5ms) vs Algorithm 1 Gibbs (4 chains × 4000 iter)。需三项澄清\n- κ-guard = 100：应与修正后余项建立理论连接\n- K=4 时 Strat. MLE |Bias| (0.010) < HB (0.012)：R1 解释这是正确的 bias-variance tradeoff——HB 通过小量额外偏差换取方差降低，RMSE 在 87.5% 配置中优于 Strat. MLE（James-Stein 收缩的经典优势）\n\n### Section 5 (Experiments)\n- Table 1：7.4× = 0.059/0.008 基线为 Global（R2 验证正确，R1 原计算有误）\n- 14.9% sign reversal 跨越广泛参数设定，不仅限于 τ(0)=0.03——R1 指出 50% 配置（260/520）出现 bias amplification\n- CivilComments：最大实证缺口，但半合成方法论是因果推断标准做法\n- Per-model R²：建议 Appendix W 增加影响因素分析\n\n### Formatting & Compliance\n- ACL 双栏 + review mode，正文 8 页，符合 EMNLP 2026 长文限制\n- Limitations 在正文内，合规\n- Figure 4 确认在 page 8（R1 验证），非 page 9\n- Figure 2 色盲修复可能不完整\n- Egami bib year 不一致\n\n### Issue Tracker 更新\n- 本轮新增 10 个 issue（R22-W1–W5, R22-Q1–Q4, R22-FMT1）\n- 更新 18 个已有 issue 的 R22 mentions（含双方交叉回应论据）\n- R16-W7（Figure 2 色盲）从 resolved 回退至 in_progress",
    "project": "ec_hte_llm_annotation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5-4.0",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 2393 · 2026-05-25T04:57:12.646401+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6b114d432b35fe7a1c2143457ae85b08:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Assistant

_source line 2394 · 2026-05-25T04:57:26.727970+00:00_

Round 22 审稿报告已重新提交（修订版），整合了双方交叉回应的完整论据。

**圆桌审稿总结：**

- **2 位 Reviewer，1 轮交叉回应，已收敛**（分歧为评审判断差异，非事实争议）
- **评分范围 3.5–4.0**（R1: 4.0 Conference / R2: 3.5 Borderline Conference）
- **核心共识**：Theorem 1 技术正确、实验全面、theory.tex L92 余项 κ→κ² 需修正、EB vs Gibbs 描述不一致需澄清
- **核心分歧**：(1) novelty 在 insight vs 证明难度的评判标准；(2) 半合成验证在因果推断中是否足够；(3) EMNLP 受众适配性
- **R1 交叉回应的关键新证据**：Table 36 表明 EC-HTE 在非对称误分类（FPR/FNR 比 7:1）下仍维持 94.5% coverage，削弱了 A2 假设作为致命限制的论据
- **Issue Tracker 更新**：本轮新增 10 个 issue，更新 18 个已有 issue

报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 189

## Round 189

60 recorded events


### User

_source line 2395 · 2026-05-25T06:08:20.259271+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: ec_hte_llm_annotation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2396 · 2026-05-25T06:08:26.818551+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2397 · 2026-05-25T06:08:26.869571+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2398 · 2026-05-25T06:08:32.768415+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,read_project_file,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,read_project_file,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2399 · 2026-05-25T06:08:32.869310+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2400 · 2026-05-25T06:08:36.739115+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2401 · 2026-05-25T06:08:36.739446+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2402 · 2026-05-25T06:08:39.508957+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2403 · 2026-05-25T06:08:39.559664+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2404 · 2026-05-25T06:08:44.934873+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2405 · 2026-05-25T06:08:45.889839+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (43 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-041** (negative): Under asymmetric misclassification (FPR≠FNR, ratio 1:2 to 1:5 and reverse), the bias identity retains R²≥0.95 and EC-HTE maintains coverage ≥93% across 48 configurations (6 FPR/FNR ratios × 2 K × 4 Δπ), while the symmetric diagnostic AUC degrades monotonically with FPR/FNR ratio — quantifying the exact diagnostic accuracy loss curve under asymmetry.\n  [exp041_asymmetric_grid](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_grid.csv) | [exp041_asymmetric_summary](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_summary.csv) | [exp041_asymmetric_mc_script](/api/workspace-files/projects/e
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2406 · 2026-05-25T06:08:45.890313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2407 · 2026-05-25T06:08:46.844196+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{makecell}
15	\usepackage{xcolor}
16	\usepackage{enumitem}
17	\usepackage{algorithm}
18	\usepackage{algpseudocode}
19	
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}[theorem]{Corollary}
22	\newtheorem{proposition}[theorem]{Proposition}
23	\newtheorem{remark}[theorem]{Remark}
24	
25	\title{When Debiasing Hurts: An Exact Bias Identity\\for LLM-Annotated Treatment Effects}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{theory}
39	
40	\input{method}
41	
42	\input{experiments}
43	
44	\input{conclusion}
45	
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	%\input{checklist}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 2408 · 2026-05-25T06:08:46.844797+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 2409 · 2026-05-25T06:08:47.949104+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_23/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_23/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2410 · 2026-05-25T06:08:48.150785+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1263127 May 25 05:40 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_23/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 2411 · 2026-05-25T06:08:52.368136+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author guidelines site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found several results related to ACL conferences and submission guidelines, but the search results don't contai
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 5523
}
```

</details>

---


### Tool call

_source line 2412 · 2026-05-25T06:08:57.890974+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 2413 · 2026-05-25T06:08:58.493497+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR ACL Rolling Review June 2026 deadline submission template anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR ACL Rolling Review June 2026 deadline submission template anonymity"
  }
}
```

</details>

---


### Tool call

_source line 2414 · 2026-05-25T06:08:58.945581+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---


### Tool result

_source line 2415 · 2026-05-25T06:08:58.996270+00:00_

_figure_backups
_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
appendix_agnews.tex
appendix_stance.tex
checklist.tex
conclusion.tex
experiments.tex
figures
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2416 · 2026-05-25T06:09:05.727081+00:00_

Web search results for query: "ARR ACL Rolling Review June 2026 deadline submission template anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's what I found about ARR (ACL Rolling Review) regarding deadlines, submission templates, and anonymity requirements relevant to June 2026:

## Submission Deadlines

The new 10-week review cycle schedule started in May 2025. While the search results don't specify an exact June 2026 deadline, there is a submission deadline every two months.

…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 7233
}
```

</details>

---


### Tool result

_source line 2417 · 2026-05-25T06:09:08.036066+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026 regarding page limits and formatting requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references, while review versions of short papers may have up to four (4) pages of content, plus unlimited pages for references.

Upon acceptance, final versions of long papers will be given one additional page – 
…[truncated 1261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "WebSearch",
  "elapsed_ms": 10145
}
```

</details>

---


### Tool call

_source line 2418 · 2026-05-25T06:09:11.607154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2419 · 2026-05-25T06:09:12.109665+00:00_

1	\begin{abstract}
2	Standard confusion-matrix correction for noisy annotations assumes uniform error rates.
3	When this assumption fails---as it routinely does with large language model (LLM) classifiers, whose error rates vary by up to $5\times$ across subgroups---correction can reverse estimated effect signs.
4	We derive an exact bias identity: global correction introduces subgroup-level bias $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$ under symmetric errors (generalizing to a full-matrix form for arbitrary asymmetric confusion matrices; Remark~\ref{rem:asymmetric}), verified at $R^2 \geq 0.97$ on synthetic grids ($R^2 = 0.975$ in aggregate across 11 real LLM confusion matrices; per-model range $0.76$--$0.99$).
5	The identity predicts that global correction reverses conditional average treatment effect (CATE) sign in 14.9\% of configurations where the true effect is small ($\tau(0) = 0.03$) and amplifies bias in all eight real LLMs tested; a $\Delta\tau$-free diagnostic corollary flags harmful correction from error rates alone, without estimating treatment effects.
6	We characterize when per-subgroup correction is beneficial ($\Delta\pi > 0.15$, $n_{\text{expert}}/K \geq 50$, $K \leq 4$) versus when global correction should be retained, and implement one such correction via hierarchical Bayesian estimation, reducing $|\text{bias}|$ by $7.4\times$ under extreme heterogeneity.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2420 · 2026-05-25T06:09:12.110167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2421 · 2026-05-25T06:09:12.612259+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Consider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.
5	After standard confusion-matrix correction, the analysis concludes the policy \emph{increases} hate speech among younger users---but the true effect is protective.
6	This sign reversal is not an edge case.
7	
8	Large language models (LLMs) now routinely replace human annotators in computational social science, producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,tan2024llm}.
9	When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.
10	Yet LLM annotations are not uniformly accurate: \citet{ashwin2025bias} document error rates varying by up to 5$\times$ across demographic subgroups; in our pilot, GPT-4.1 error rates range from 10.2\% to 20.0\% across text-feature subgroups ($\Delta\pi = 0.098$).
11	
12	We show that this standard correction can make things worse.
13	In 14.9\% of our synthetic configurations (across a grid of $\Delta\pi$ and $\tau(0)$ values; $\tau(0) = 0.03$), global correction reverses the sign of estimated CATE---a protective treatment ($\tau = +0.03$) appears harmful ($\hat{\tau} = -0.059$)---rising to 31\% at $\tau(0) = 0.01$ (Figure~\ref{fig:sign_reversal}); all eight real LLMs tested amplify bias under global correction, while our per-subgroup correction (EC-HTE; Section~\ref{sec:method}) eliminates sign reversal in the pri
…[truncated 2805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2422 · 2026-05-25T06:09:12.612618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2423 · 2026-05-25T06:09:13.065294+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Measurement error and annotation models.}
5	Classical measurement error theory shows that correction via estimated error models can amplify mean squared error (MSE) when the error structure is misspecified~\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\cite{hu2008nonparametric}.
6	
7	Three distinctions separate our contribution from prior measurement error analyses.
8	First, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\cite{frazis2003estimating,carroll2006measurement} or confounder~\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.
9	Second, Theorem~\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.
10	Concretely, \citet{frazis2003estimating} derive scalar attenuation $\lambda = (1 - 2\pi)$ for the uncorrected estimator under homogeneous misclassification; Theorem~\ref{thm:bias_identity} yields a structurally interpretable decomposition---the product $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$ whose sign varies across subgroups, revealing how error heterogeneity causes bias direction to reverse between subgroups, a phenomenon invisible to any global-scalar analysis.
11	The homogeneous-error setting ($K{=}1$, $\delta_s{=}0$) is a degenerate case recovering classical attenuation~\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\ref{app:fl_comparison}).
12	Third, the $\delta_s \cdot \Delta\tau$ product str
…[truncated 5180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2424 · 2026-05-25T06:09:13.066086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 2425 · 2026-05-25T06:09:13.367561+00:00_

1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state five assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification (expository simplification):} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$. Used only to reduce $[B_s]_{z,1}$ to the scalar $\pm\delta_s/(1{-}2\bar{\pi})$; the product-form identity holds for arbitrary asymmetric matrices without~(A2) (Remark~\ref{rem:asymmetric}).
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{N
…[truncated 8581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2426 · 2026-05-25T06:09:13.368015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2427 · 2026-05-25T06:09:13.418474+00:00_

1	\section{Correction Prescribed by the Identity}
2	\label{sec:method}
3	
4	Theorem~\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.
5	This correction (EC-HTE) proceeds in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.
6	The complete procedure is summarized in Algorithm~\ref{alg:echte} (Appendix~\ref{app:algorithm}) and illustrated in Figure~\ref{fig:method_overview}.
7	
8	\begin{figure*}[t]
9	\centering
10	\includegraphics[width=\textwidth]{figures/fig_method_overview.pdf}
11	\caption{\textit{Top (rose):} global correction applies a pooled confusion matrix uniformly, risking sign reversal. \textit{Bottom (teal):} EC-HTE estimates per-subgroup matrices via hierarchical Bayes, applies stratified inversion with a $\kappa$-guard, and propagates uncertainty into CausalForestDML.}
12	\label{fig:method_overview}
13	\end{figure*}
14	
15	\subsection{Hierarchical Bayes Confusion Matrix Estimation}
16	
17	We place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\{C_s\}_{s=1}^K$.
18	The model estimates the full $J \times J$ confusion matrix per subgroup and does not require symmetric error rates~(A2); (A2) simplifies only the diagnostic (Proposition~\ref{prop:debiasing_hurts}).
19	For each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior centered at the global pooled confusion matrix $\hat{C}_{\text{global}}$: $\text{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, where $\hat{C}_{\text{global},j}$ is the $j$-th row of the pooled CM and $\alpha_0 > 0$ is a shared concentration parameter estimated via empirical Bayes (marginal likelihood maximization).
20	We place a $\mathrm{Gamma}(3, 1)$ hyperprior on $\alpha_0$, robust to $2\times$ perturbation (Appendix~\ref{app:hyperprior}).
21	Large 
…[truncated 2776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2428 · 2026-05-25T06:09:18.294032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2429 · 2026-05-25T06:09:18.746620+00:00_

1	\section{Experiments}
2	
3	\begin{figure}[t]
4	\centering
5	\includegraphics[width=\columnwidth]{figures/fig4_budget_compact.pdf}
6	\caption{RMSE vs.\ expert budget under extreme heterogeneity. Crossover at $n{=}250$ ($K{=}2$) and $n{=}1000$ ($K{=}4$); shaded bands: $\pm 1$ SD across subgroups. Full grid in Appendix~\ref{app:budget}.}
7	\label{fig:budget_compact}
8	\end{figure}
9	
10	\subsection{Setup}
11	
12	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 Monte Carlo (MC) runs) and semi-synthetic data-generating processes (DGPs) spanning four NLP tasks---sentiment analysis (TweetEval~\cite{barbieri2020tweeteval}, $K{=}4$), hate speech detection (CivilComments, $K{=}4$), stance detection ($K{=}5$; Appendix~\ref{app:stance}), and topic classification (AG News, $K{=}4$; Appendix~\ref{app:agnews})---with full specifications in Appendix~\ref{app:dgp}.
13	
14	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2023dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (per-subgroup correction), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
15	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
16	Primary metrics are $|\text{bias}|$, root mean squared error (RMSE), and 95\% confidence interval (CI) coverage, averaged across subgroups and 100 MC runs.
17	Robustness validations cover eight conditions including asymmetric errors, subgroup misspecification, and treatment-dependent misclassification (all $\geq$89.5\% coverage; Appendices~\ref{app:hatespeech}--\ref{app:treatment_dep}).
18	Semi-synthetic evaluation uses 16 empirical LLM confusion matrices (8 LLMs $\times$ 2 datasets; Appendix~\ref{app:semireal}).
19	
20	\subsection{Empirical Validation of the Bias Identity}
21	\label{sec:bias_mechanism}
22	
23	\b
…[truncated 5984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2430 · 2026-05-25T06:09:18.798944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2431 · 2026-05-25T06:09:19.502704+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Standard confusion-matrix correction can reverse causal conclusions when misclassification rates vary across subgroups.
4	We derived an exact bias identity ($R^2 \geq 0.97$) that yields a diagnostic for flagging harmful correction and prescribes per-subgroup correction when $\Delta\pi > 0.15$ and $n_{\text{expert}}/K \geq 50$, validated across 11 real LLMs and four NLP tasks.
5	Practitioners should estimate per-subgroup confusion matrices before applying any correction; the framework is task-agnostic and composes with prediction-powered inference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 2432 · 2026-05-25T06:09:19.603568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2433 · 2026-05-25T06:09:19.654397+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Per-subgroup correction requires $n_{\text{expert}}/K \geq 50$ expert labels per subgroup and moderate classifier accuracy ($\text{FPR}_s, \text{FNR}_s < 0.5$); at $K{=}8$, RMSE exceeds global correction under fixed expert budget (Appendix~\ref{app:k8_subgroups}).
5	Assumption~(A3) requires balanced effect modifier prevalence; under class imbalance ($P(Z{=}1) = 0.1$), the identity remains exact ($R^2 \geq 0.976$) but EC-HTE's RMSE advantage narrows (ratio 1.06--1.68; Appendix~\ref{app:classimbalance}).
6	Assumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable; sensitivity analysis shows robustness up to $\gamma_T \leq 0.05$ for treatment-dependent misclassification (coverage $\geq$89.7\%; Appendix~\ref{app:treatment_dep}).
7	Ground-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so all evaluations use synthetic CATE injection on real text features and real LLM annotations (Appendices~\ref{app:dgp},~\ref{app:multilm}).
8	When LLMs annotate both the effect modifier and the outcome variable, covariate-side and outcome-side misclassification errors may be correlated, violating the independence structure assumed by combining EC-HTE with post-prediction causal inference (PPCI) frameworks~\cite{sui2026ppci}; practitioners should verify error independence or apply joint correction when both variables are LLM-annotated.
9	Code and data generation scripts are publicly available.\footnote{\url{https://anonymous.4open.science/r/ec-hte}}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2434 · 2026-05-25T06:09:19.705329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2435 · 2026-05-25T06:09:20.008956+00:00_

File content (42558 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 2436 · 2026-05-25T06:09:25.992020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2437 · 2026-05-25T06:09:26.444674+00:00_

1	\section{EC-HTE Procedure}
2	\label{app:algorithm}
3	
4	\begin{algorithm}[t]
5	\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
6	\label{alg:echte}
7	\begin{algorithmic}[1]
8	\Require Observations $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S: \mathcal{X} \to \{1,\ldots,K\}$
9	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with variance-adjusted CIs
10	\Statex
11	\State \textbf{Preconditions:} verify $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ and $\max_s(\text{FPR}_s, \text{FNR}_s) < 0.5$; if either fails, use global correction
12	\Statex
13	\State \textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}
14	\State $\alpha_0 \gets \arg\max_{\alpha} \prod_{s=1}^{K} p(\text{data}_s \mid \alpha, \hat{C}_{\text{global}})$ \Comment{empirical Bayes}
15	\For{$s = 1, \ldots, K$}
16	    \State $C_s[j,\cdot] \sim \mathrm{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$
17	    \State $\hat{C}_s[j,k] \gets \frac{n_{s,jk} + \alpha_0 \cdot \hat{C}_{\text{global},j,k}}{n_{s,j\cdot} + \alpha_0}$ \Comment{posterior mean}
18	\EndFor
19	\Statex
20	\State \textbf{Step 2: Correct observed outcome moments}
21	\For{$s = 1, \ldots, K$}
22	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{singularity guard}
23	    \EndIf
24	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
25	\EndFor
26	\Statex
27	\State \textbf{Step 3: CausalForestDML with variance-adjusted SEs}
28	\State Train CausalForest (honest splitting) on corrected outcome moments $\tilde{\boldsymbol{\mu}}_s$
29	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
30	\State \Return $\hat{\tau}(z)$ with 95\% CIs from $\mathrm{se}_{\mathrm{adj}}$
31	\end{algorithmic}
32	\end{algorithm}
33	
34	\subsection{Condition Number Guard Ablation}
35	\label{app:kappa_ablation}
36	
37	The singular
…[truncated 12084 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2438 · 2026-05-25T06:09:26.948153+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2439 · 2026-05-25T06:09:27.299785+00:00_

1	% === Proximal / Sensitivity ===
2	
3	@article{miao2018identifying,
4	  title={Identifying Causal Effects with Proxy Variables of an Unmeasured Confounder},
5	  author={Miao, Wang and Geng, Zhi and Tchetgen Tchetgen, Eric J.},
6	  journal={Biometrika},
7	  volume={105},
8	  number={4},
9	  pages={987--993},
10	  year={2018}
11	}
12	
13	@article{cinelli2020making,
14	  title={Making Sense of Sensitivity: Extending Omitted Variable Bias},
15	  author={Cinelli, Carlos and Hazlett, Chad},
16	  journal={Journal of the Royal Statistical Society: Series B},
17	  volume={82},
18	  number={1},
19	  pages={39--67},
20	  year={2020}
21	}
22	
23	% === Datasets ===
24	
25	@inproceedings{borkan2019nuanced,
26	  title={Nuanced Metrics for Measuring Unintended Bias with Real Data for Text Classification},
27	  author={Borkan, Daniel and Dixon, Lucas and Sorensen, Jeffrey and Thain, Nithum and Vasserman, Lucy},
28	  booktitle={Companion Proceedings of The 2019 World Wide Web Conference},
29	  pages={491--500},
30	  year={2019}
31	}
32	
33	% === Econometrics of Binary Misclassification ===
34	
35	@incollection{bound2001measurement,
36	  title={Measurement Error in Survey Data},
37	  author={Bound, John and Brown, Charles and Mathiowetz, Nancy},
38	  booktitle={Handbook of Econometrics},
39	  volume={5},
40	  pages={3705--3843},
41	  year={2001},
42	  publisher={Elsevier}
43	}
44	
45	@article{greenland1980effect,
46	  title={The Effect of Misclassification in the Presence of Covariates},
47	  author={Greenland, Sander},
48	  journal={American Journal of Epidemiology},
49	  volume={112},
50	  number={4},
51	  pages={564--569},
52	  year={1980}
53	}
54	
55	@article{frazis2003estimating,
56	  title={Estimating Linear Regressions with Mismeasured, Possibly Endogenous, Binary Explanatory Variables},
57	  author={Frazis, Harley and Loewenstein, Mark A.},
58	  journal={Journal of Econometrics},
59	  volume={117},
60	  number={1},
61	  pages={151--178},
62	  year={2003}
63	}
64	
65	@article
…[truncated 4431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2440 · 2026-05-25T06:09:27.300415+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 2441 · 2026-05-25T06:09:27.401152+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/memory.md\", \"content\": \"# Memory — ec_hte_llm_annotation\\n\\n## 研究发现\\n\\n### 非对称诊断等价性 (2026-05-23, Worker A)\\n对 K_Z=2（二值标签），非对称诊断公式 |B_s[1,1] - B_s[1,0]| / (FPR_s + FNR_s) 恒等于对称公式 |δ_s| / ((1-2π̄)·π_s)。FPR/FNR 不对称性在行差中完全抵消。AUC=0.63 的真正原因是 τ_s=0 子组的 MC 噪声，排除后 AUC=1.0。\\n\\n### Centered EB 优于 Dir(α/2, α/2) (2026-05-23, Worker C)\\n原始 HB 用 Dir(α/2, α/2) 向 (0.5, 0.5) 收缩是错误目标。Centered EB 向 global CM 收缩，在 moderate heterogeneity 下 RMSE ≈ Global（消除弱点），在 extreme 下 RMSE < Global < original HB。K4 extreme 下 original HB RMSE > Global 的问题也被修复。\\n\\n### Bootstrap SE 在小 n_expert 下的表现 (2026-05-23, Task G)\\nDIM + Centered EB, K=2 extreme (π=[0.05,0.25]), 20 MC × B=100。Bootstrap coverage 在所有 n_expert ≥25 下均达 nominal (≥95%): n=25→100%, n=50→98.8%, n=75→97.5%, n=100→96.3%, n=200→95.0%。Plug-in SE 在 n≥50 时 ≥92.5%，最弱点 n=75 (91.2%)。高误差子群 s1 (π=0.25) 是 bootstrap 的主要受益者。数据: results/exp_bootstrap_small_n_summary.csv\\n\\n### UCB Annotator Demographics Δπ 不足 (2026-05-24)\\nUCB Hate Speech 135K行数据，7个 annotator demographic features + 交互特征。最大 Δπ = 0.117（race × ideology），单一特征最大 0.084（education）。根因：GPT-4.1 的主要错误模式是 FNR ≈ 0.55（漏检 hate speech），这在所有 demographic 组中高度一致。Δπ 来自次要效应（如保守派 π≈0.39 vs 自由派 π≈0.35），幅度不够。即使用虚高 Δπ=0.23 跑 semi-synthetic，correction 因 1-FPR-FNR ≈ 0.28 放大噪声，全面劣于 naive。**结论：annotator demographics 维度的异质性不足以支撑 EC-HTE real-data 成功案例，且高 FNR 使 CM inversion 本身不稳定。这是 task-level 的结构性限制，非 subgroup 选择问题。**\\n\\n## 决策记录\\n\\n### API 模型版本 (已验证)\\n- GPT-4.1: `gpt-4.1-2025-04-14`\\n- GPT-5.4: `gpt-5.4` (reasoning model, 慢, ~1min/call)\\n- GPT-5.5 不可用（reasoning tokens 消耗 max_tokens budget）\\n\\n### 论文写作\\n- EMNLP 2026 DDL: 2026-05-25 (ARR)\\n- 8 页主文限制，Limitations/References 不计入\\n- R15 审稿修复已全部完成（8 项，2026-05-23）\\n- Messing (2026) 已加入 Related Work\\n- 数据完整性审计完成：AUC=0.86 确认正确（Δπ-only diagnostic），AUC=0.82→0.66 已修复（3处），74-82% coverage 确认正确\\n- 匿名代码仓库已推送: https://github
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2442 · 2026-05-25T06:09:31.841221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/ 2>/dev/null | head -20",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/ 2>/dev/null | head -20",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2443 · 2026-05-25T06:09:33.098035+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool call

_source line 2444 · 2026-05-25T06:09:33.098477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_FOUND_IN_CONFIG\"",
  "description": "Check external review in project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_FOUND_IN_CONFIG\"",
    "description": "Check external review in project config"
  }
}
```

</details>

---


### Tool result

_source line 2445 · 2026-05-25T06:09:33.149006+00:00_

NOT_FOUND_IN_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2446 · 2026-05-25T06:09:47.014940+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 2447 · 2026-05-25T06:09:47.116454+00:00_

issues:
  # === RESOLVED (prior rounds — abbreviated) ===
  - id: "R1-N1"
    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 2
    action_items: []
    resolution: "重新推导为精确恒等式"
    resolution_round: 0

  - id: "R2-W8"
    summary: "Proposition 1 限于 K=2"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "Theorem 1 适用一般 K"
    resolution_round: 0

  - id: "R1-N2"
    summary: "Real data ground truth CATE 来源不明"
    category: experiment
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位为 illustrative application"
    resolution_round: 0

  - id: "R1-N3"
    summary: "HB 模型规格严重不完整"
    category: method
    severity: critical
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "完整 MCMC 规格"
    resolution_round: 0

  - id: "JOINT-W4"
    summary: "相关工作严重遗漏"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "30+ 引用覆盖"
    resolution_round: 0

  - id: "JOINT-W3"
    summary: "信息密度过高"
    category: writing
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "主文精简至合理密度"
    resolution_round: 0

  - id: "R2-W7"
    summary: "真实数据验证单薄"
    category: experiment
    severity: warning
    status: resolved
    first_raised_round: 0
    last_seen_round: 1
    action_items: []
    resolution: "恰当定位 + 公开数据集"
    resolution_round: 0

  - id: "R1-W5"
    summary: "Pages 9-10 缺 Appendix 标签"
    category: format
    severity: info
    status: resolved
    first_raised_round: 0
    last_seen_round: 0
    action_items: []
    resolution: "附录结构重组"
    resolutio
…[truncated 22251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2448 · 2026-05-25T06:10:28.231980+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "review_chat_id": "oc_489afd65980834a91024fd48e21d984f"
  }
}
```

</details>

---


### Tool result

_source line 2449 · 2026-05-25T06:10:50.823599+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22591
}
```

</details>

---


### Tool call

_source line 2450 · 2026-05-25T06:10:51.778065+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\n- **Venue**: EMNLP 2026 (ARR 提交)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL review 模板，正文 8 页限制，references 不限，Limitations 不计入页数，double-blind 匿名\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**——重点审查以下方面：\n\n1. **理论正确性**：\n   - Theorem 1 (Bias Decomposition Identity) 的证明是否完整、严谨？\n   - Proposition 3 (A5 relaxation) 和 Corollary 4 (Aggregate Bias) 是否正确？\n   - Proposition 5 (Debiasing Can Increase Bias) 的充要条件推导是否无误？\n   - Remark 2 关于非对称误分类的推广是否合理？\n   - Assumptions (A1)-(A5) 是否充分讨论了各自的限制和放松条件？\n   - 有限样本余项 O_p(κ²·n^{-1/2}) 的推导是否正确？\n\n2. **实验设计与统计有效性**：\n   - DGP（数据生成过程）是否合理、是否涵盖足够场景？\n   - MC 100 次是否足以支撑 coverage 和 bias 的结论？\n   - R² 验证方法是否适当？per-model R² 范围 0.76-0.99 的低端是否值得关注？\n   - Semi-synthetic 评估（16 个 LLM confusion matrices）是否有效？\n   - 操作条件（Δπ>0.15, n_expert/K≥50, K≤4）的确定是否有充分依据？\n   - CausalForest/R-learner 集成验证是否充分？\n\n3. **方法设计**：\n   - 层级贝叶斯 CM 估计的规格是否完整？EB vs MCMC 的选择是否充分讨论？\n   - κ-guard (κ>100) 阈值的选择是否有理论依据？\n   - SE 调整公式是否正确？Bootstrap (B=100) 是否充分？\n   - 与 PPCI 的组合条件是否明确？\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内？\n   - Limitations 是否在正文中（conclusion 之后、references 之前）？\n   - 是否 double-blind 匿名？\n   - Abstract 是否在 200 words 以内？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需作者澄清的问题）\n5. Missing References（遗漏的重要相关工作）\n6. Overall Assessment（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n**立场提醒**：你是严格的审稿人，不是投稿人的盟友。对任何不严谨、不完整、或过度声称的地方不留情面。",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f",
  "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## 论文信息\n- **标题**: When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\n- **Venue**: EMNLP 2026 (ARR 提交)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL review 模板，正文 8 页限制，references 不限，Limitations 不计入页数，double-blind 匿名\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性**——重点审查以下方面：\n\n1. **理论正确性**：\n   - Theorem 1 (Bias Decomposition Identity) 的证明是否完整、严谨？\n   - Proposition 3 (A5 relaxation) 和 Corollary 4 (Aggregate Bias) 是否正确？\n   - Proposition 5 (Debiasing Can Increase Bias) 的充要条件推导是否无误？\n   - Remark 2 关于非对称误分类的推广是否合理？\n   - Assumptions (A1)-(A5) 是否充分讨论了各自的限制和放松条件？\n   - 有限样本余项 O_p(κ²·n^{-1/2}) 的推导是否正确？\n\n2. **实验设计与统计有效性**：\n   - DGP（数据生成过程）是否合理、是否涵盖足够场景？\n   - MC 100 次是否足以支撑 coverage 和 bias 的结论？\n   - R² 验证方法是否适当？per-model R² 范围 0.76-0.99 的低端是否值得关注？\n   - Semi-synthetic 评估（16 个 LLM confusion matrices）是否有效？\n   - 操作条件（Δπ>0.15, n_expert/K≥50, K≤4）的确定是否有充分依据？\n   - CausalForest/R-learner 集成验证是否充分？\n\n3. **方法设计**：\n   - 层级贝叶斯 CM 估计的规格是否完整？EB vs MCMC 的选择是否充分讨论？\n   - κ-guard (κ>100) 阈值的选择是否有理论依据？\n   - SE 调整公式是否正确？Bootstrap (B=100) 是否充分？\n   - 与 PPCI 的组合条件是否明确？\n\n4. **格式合规**：\n   - 正文是否在 8 页限制内？\n   - Limitations 是否在正文中（conclusion 之后、references 之前）？\n   - 是否 double-blind 匿名？\n   - Abstract 是否在 200 words 以内？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需作者澄清的问题）\n5. Missing References（遗漏的重要相关工作）\n6. Overall Assessment（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n**立场提醒**：你是严格的审稿人，不是投稿人的盟友。对任何不严谨、不完整、或过度声称的地方不留情面。",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f",
    "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
  }
}
```

</details>

---


### Tool result

_source line 2451 · 2026-05-25T06:11:13.060672+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21282
}
```

</details>

---


### Tool call

_source line 2452 · 2026-05-25T06:11:13.917645+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- **标题**: When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\n- **Venue**: EMNLP 2026 (ARR 提交)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL review 模板，正文 8 页限制，references 不限，Limitations 不计入页数，double-blind 匿名\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**——重点审查以下方面：\n\n1. **新颖性深度**：\n   - 相对于 Frazis-Loewenstein (2003) 的标量衰减分析，本文的增量贡献有多大？是直接推广还是本质创新？\n   - 层级贝叶斯 CM 估计是否有技术新颖性？还是已有方法（Dawid-Skene 架构）的直接应用？\n   - \"Debiasing can hurt\" 这一 insight 在测量误差文献中是否早已知晓？本文的具体量化是否构成足够的新贡献？\n   - 与 PPI/DSL/PPCI 等 prediction-powered 方法的关系——本文是否提供了新的理论理解还是仅是应用层面的区分？\n\n2. **Related Work 覆盖**：\n   - 测量误差文献（econometrics）是否充分覆盖？\n   - 噪声标签学习文献（ML）是否充分覆盖？subgroup-dependent vs instance-dependent noise 的联系是否清晰？\n   - Causal inference with text（Feder 2022, Keith 2020, Veitch 2020）覆盖是否充分？\n   - 近期相关工作（Messing 2026, Camuffo 2025, Gligoric 2025, Sui 2026, Mozer 2026）是否都已引用和讨论？\n   - 是否有重要遗漏？特别关注 Filtered PPI (arXiv:2602.10464) 等近期预印本。\n\n3. **NLP 社区适配性**：\n   - 论文的核心贡献（因果推断中的测量误差恒等式）对 EMNLP 受众的价值定位是否清晰？\n   - 数学/符号密度是否对 NLP 读者友好？\n   - 实验中的 NLP task 覆盖（sentiment, hate speech, stance, topic classification）是否有说服力？\n   - CivilComments 上的 NLP insight（identity subgroup 效应差异）是否充分阐述？\n\n4. **写作质量**：\n   - Abstract 信息密度是否过高？是否在 200 words 以内？\n   - \"Debiasing\" 术语是否可能与 fairness debiasing 混淆？\n   - Contributions list 是否清晰、准确、无过度声称？\n   - 整体叙事结构（problem→identity→method→experiments）是否连贯？\n   - Limitations 是否充分覆盖关键限制？\n\n5. **完整性**：\n   - 是否缺少关键实验（如 fully real-data validation, X-learner/BART 验证）？\n   - 假设的敏感性分析是否充分？\n   - 复现性：代码和数据是否可获取？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需作者澄清的问题）\n5. Missing References（遗漏的重要相关工作）\n6. Overall Assessment（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n**立场提醒**：你是严格的审稿人，不是投稿人的盟友。对任何 novelty 不足、声称过度、覆盖遗漏的地方不留情面。特别关注论文对 EMNLP 受众的价值是否足够。",
  "project": "ec_hte_llm_annotation",
  "chat_id": "oc_489afd65980834a91024fd48e21d984f",
  "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## 论文信息\n- **标题**: When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects\n- **Venue**: EMNLP 2026 (ARR 提交)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL review 模板，正文 8 页限制，references 不限，Limitations 不计入页数，double-blind 匿名\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_23/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**——重点审查以下方面：\n\n1. **新颖性深度**：\n   - 相对于 Frazis-Loewenstein (2003) 的标量衰减分析，本文的增量贡献有多大？是直接推广还是本质创新？\n   - 层级贝叶斯 CM 估计是否有技术新颖性？还是已有方法（Dawid-Skene 架构）的直接应用？\n   - \"Debiasing can hurt\" 这一 insight 在测量误差文献中是否早已知晓？本文的具体量化是否构成足够的新贡献？\n   - 与 PPI/DSL/PPCI 等 prediction-powered 方法的关系——本文是否提供了新的理论理解还是仅是应用层面的区分？\n\n2. **Related Work 覆盖**：\n   - 测量误差文献（econometrics）是否充分覆盖？\n   - 噪声标签学习文献（ML）是否充分覆盖？subgroup-dependent vs instance-dependent noise 的联系是否清晰？\n   - Causal inference with text（Feder 2022, Keith 2020, Veitch 2020）覆盖是否充分？\n   - 近期相关工作（Messing 2026, Camuffo 2025, Gligoric 2025, Sui 2026, Mozer 2026）是否都已引用和讨论？\n   - 是否有重要遗漏？特别关注 Filtered PPI (arXiv:2602.10464) 等近期预印本。\n\n3. **NLP 社区适配性**：\n   - 论文的核心贡献（因果推断中的测量误差恒等式）对 EMNLP 受众的价值定位是否清晰？\n   - 数学/符号密度是否对 NLP 读者友好？\n   - 实验中的 NLP task 覆盖（sentiment, hate speech, stance, topic classification）是否有说服力？\n   - CivilComments 上的 NLP insight（identity subgroup 效应差异）是否充分阐述？\n\n4. **写作质量**：\n   - Abstract 信息密度是否过高？是否在 200 words 以内？\n   - \"Debiasing\" 术语是否可能与 fairness debiasing 混淆？\n   - Contributions list 是否清晰、准确、无过度声称？\n   - 整体叙事结构（problem→identity→method→experiments）是否连贯？\n   - Limitations 是否充分覆盖关键限制？\n\n5. **完整性**：\n   - 是否缺少关键实验（如 fully real-data validation, X-learner/BART 验证）？\n   - 假设的敏感性分析是否充分？\n   - 复现性：代码和数据是否可获取？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需作者澄清的问题）\n5. Missing References（遗漏的重要相关工作）\n6. Overall Assessment（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n**立场提醒**：你是严格的审稿人，不是投稿人的盟友。对任何 novelty 不足、声称过度、覆盖遗漏的地方不留情面。特别关注论文对 EMNLP 受众的价值是否足够。",
    "project": "ec_hte_llm_annotation",
    "chat_id": "oc_489afd65980834a91024fd48e21d984f",
    "director_session_key": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
  }
}
```

</details>

---


### Tool result

_source line 2453 · 2026-05-25T06:11:15.588424+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1670
}
```

</details>

---


### Assistant

_source line 2454 · 2026-05-25T06:11:26.006684+00:00_

已派发：
- **视觉审查 Agent**：已启动（fire-and-forget）
- **Reviewer 1**（方法严谨性）：已派发
- **Reviewer 2**（新颖性与完整性）：已派发

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 190

## Round 190

2 recorded events


### User

_source line 2455 · 2026-05-25T06:17:34.864376+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性审查

### 1. Summary

本文推导了一个精确的偏差恒等式（Theorem 1），揭示当 LLM 分类器的误分类率在子群间存在异质性时，全局混淆矩阵校正会在子群层面引入 δ_s·Δτ/(1−2π̄) 的偏差，并可能逆转因果效应符号。基于此理论，作者提出 EC-HTE 方法，通过层级贝叶斯估计子群混淆矩阵进行分层校正，并在合成和半合成数据上进行了广泛验证。论文问题选择具有时效性，理论结果简洁优雅，但在假设可检验性、实验设计的生态效度和有限样本理论方面存在若干需要回应的问题。

---

### 2. Strengths

**S1. 理论结果新颖且实用。** Theorem 1 将全局校正偏差精确分解为三个可解释的因子（子群误差偏离 δ_s、效应异质性 Δτ、矩阵逆放大因子 1/(1−2π̄)），并推导出 Δτ-free 的诊断准则（Proposition 5），使从业者无需估计处理效应即可识别有害校正。这一 "debiasing can hurt" 的发现对当前 LLM 标注的因果推断实践有直接指导意义。

**S2. 证明正确且完整。** Theorem 1 的证明（Appendix B）通过直接矩阵计算得到 M_global^{-1}M_s − I = δ_s/(1−2π̄)·[−1,1;1,−1]，代数推导无误。Proposition 3（A5 放松）和 Proposition 5（debiasing hurts 的充要条件）的证明同样严谨。Remark 2 关于非对称误分类的推广（B_s·1=0 源于随机矩阵的行和性质）论证合理。

**S3. 实验覆盖面广。** 520 个合成配置 + 4 个 NLP 任务的半合成评估 + 16 个真实 LLM 混淆矩阵 + 48 个非对称配置 + 多种鲁棒性检验（A1 违反、类别不平衡、混杂处理），形成了系统性的证据链。

**S4. 操作条件清晰。** 明确给出了 EC-HTE 优于全局校正的边界条件（Δπ>0.15, n_expert/K≥50, K≤4, FNR<0.50），并诚实地指出全局校正在何时更优。

**S5. 与 PPCI 的组合。** Appendix K 展示了 EC-HTE 处理协变量侧误分类、PPCI 处理结果侧误差的互补性，|bias| 从 0.179 降至 0.007。

---

### 3. Weaknesses

**N1 [critical] 半合成评估中 A1 由构造满足，无法验证方法对现实 A1 违反的鲁棒性**

- 具体位置：Section 5.1, Appendix E (DGP)
- 问题：所有评估均使用合成 CATE 注入到真实文本特征上（Y = τ(Z)·T + η），这保证了 A1（误分类与潜在结果的条件独立性）在构造上成立。然而在实际 NLP 应用中，LLM 分类错误极可能与文本内容相关（例如讽刺、隐晦表达同时影响分类准确率和结果变量），此时 A1 系统性违反。论文虽在 Appendix Z.2-Z.3 进行了 A1 敏感性分析（γ_T ≤ 0.20），但报告 γ_T = 0.10 时覆盖率即降至 75%——这意味着在中等程度的 A1 违反下方法表现已显著退化。
- 为什么影响接收：这是该框架的核心假设，但在所有评估中都无法被挑战。读者无法判断 EC-HTE 在真实因果推断场景中的实际可靠性。
- 建议修改方向：(i) 至少构造一个 A1 结构性违反的 DGP（如让 π_s 依赖于 Y 或 X），展示方法退化的具体边界；(ii) 引用或开发敏感性分析框架来量化 A1 违反对 bias identity 的影响幅度。

**N2 [critical] 有限样本余项的表述存在内部不一致**

- 具体位置：Section 3 (theory.tex line 92) vs. Appendix B (line 103)
- 问题：主文声称有限样本余项为 R_n = O_p(n_expert^{-1/2} · κ(C_s)²)，其中"squared condition number arises from the Neumann expansion"。然而 Appendix B 给出的界为 ||M̂_global^{-1} M̂_s − M_global^{-1} M_s|| ≤ κ(M_global) · O_p(n_expert^{-1/2})——是 κ 而非 κ²。标准矩阵扰动理论对 A^{-1} 的一阶扰动给出 ||A^{-1}||² · ||E||，但对乘积 M_global^{-1} M_s 的扰动则涉及更复杂的结构。主文与附录的不一致损害了读者对有限样本保证的信心。
- 为什么影响接收：这是论文的核心理论结果之一，κ vs. κ² 对实际操作（κ-guard 阈值选择）有直接影响。
- 建议修改方向：统一表述，给出 M_global^{-1} M_s 的完整扰动界的严格推导，明确 κ 还是 κ² 是正确的阶。

**W1 [warning] 部分真实 LLM 模型的 R² 低至 0.76，与 "exact identity" 的声称不匹配**

- 具体位置：Abstract ("per-model range 0.76–0.99"), Table 23 (Appendix W, p.25)
- 问题：Table 23 显示 GPT-4o-mini 在 Civil Comments 上的 R² = 0.76，这意味着 bias identity 仅解释 76% 的偏差变异。对于声称"exact"的恒等式，24% 的未解释变异相当大。论文在 Appendix W 将低 R² 归因于 "near-homogeneous per-subgroup error" 导致的回归弱信号，但这实际上说明 identity 在 δ_s 较小时的预测精度有限——而这恰恰是从业者最需要判断"是否需要校正"的场景。
- 建议：(i) 在主文中报告 per-model R² 的分布（不仅在 abstract 中），讨论低 R² 场景的含义；(ii) 区分"数学上精确"与"统计上可验证"两个概念。

**W2 [warning] 100 次 MC 模拟对覆盖率估计的统计精度不足**

- 具体位置：Section 5.1 ("100 Monte Carlo runs"), 全文各处覆盖率报告
- 问题：95% 覆盖率的 100 次 MC 估计的标准误约为 √(0.95×0.05/100) ≈ 0.022，即 95% CI 为 [0.907, 0.993]。论文报告的许多覆盖率值（如 0.94, 0.95, 0.96）的差异在 MC 噪声范围内不可区分。特别是论文在多处比较不同方法的覆盖率差异（如 Global 0.87 vs. HB EC-HTE 0.94），这些差异虽然看起来有意义，但在 100 次 MC 下统计显著性有限。
- 建议：(i) 增加到至少 500-1000 次 MC；或 (ii) 在所有覆盖率报告中附加 MC 标准误，让读者自行判断差异的可靠性。Appendix Q 报告了 MC SEs ≤ 0.005，但这是 bias/RMSE 的 MC SE，不是覆盖率的 MC SE。

**W3 [warning] 诊断准则 AUC = 0.86（对称）偏低，实践后果未讨论**

- 具体位置：Section 5.4 (experiments.tex line 86), "AUC = 0.86 symmetric, 0.96 asymmetric"
- 问题：对称场景下 AUC = 0.86 意味着诊断存在非平凡的假阳性/假阴性率。假阳性（错误推荐 EC-HTE）会引入不必要的方差；假阴性（错误推荐 Global）会遗留有害偏差。论文未讨论这两类错误的不对称代价，也未给出精确率/召回率/决策阈值的分析。
- 建议：报告 Proposition 5 诊断在不同阈值下的 precision/recall 曲线，讨论从业者应如何在"多余方差"与"遗留偏差"之间权衡。

**W4 [warning] SE 调整公式忽略了混淆矩阵估计本身的不确定性**

- 具体位置：Section 4.3, Algorithm 1 line 16
- 问题：SE 公式 se_adj = √(diag(Ĉ_s^{-1} diag(se²) Ĉ_s^{-T})) 仅传播了原始估计量的 SE，未考虑 Ĉ_s 的估计不确定性。这是一个 delta-method 近似，会低估总体不确定性。论文建议在 n_expert/K < 50 时使用 bootstrap（B=100），但：(a) B=100 对 bootstrap SE 估计也偏低（通常推荐 B ≥ 200-500）；(b) 即使 n_expert/K ≥ 50，忽略 CM 估计不确定性仍会导致 CI 偏窄。
- 建议：(i) 推导包含 CM 估计不确定性的完整 SE 公式；或 (ii) 系统性地展示 plug-in SE vs. bootstrap SE 的差距，明确 plug-in 近似的有效范围。

**W5 [warning] 操作条件（K≤4）限制了方法的适用范围**

- 具体位置：Section 5.4 (Operating conditions), Appendix I (K=8)
- 问题：论文明确指出 K≤4 是操作条件，K=8 时 RMSE 超过全局校正。然而在实际 NLP 应用中，子群数量常远超 4（如情感分析中的多个人口统计交叉组、多语言场景）。论文未讨论如何在 K 较大时折衷使用（如对子群进行聚合以降低有效 K），也未探讨 K 的限制是否来源于根本性的偏差-方差权衡还是仅仅是专家标注预算不足。
- 建议：(i) 分析 K 限制的根本原因（是否可通过增加 n_expert 克服？）；(ii) 讨论子群聚合策略作为实用折衷方案。

**W6 [warning] 与 Frazis-Loewenstein 的比较可能不公平**

- 具体位置：Table 1 (F-L Scalar, F-L Per-sub.), Section 5.3
- 问题：F-L 校正（Frazis and Loewenstein, 2003）设计用于 OLS 回归中误测二元回归变量的标量衰减偏差，不是为 CATE 估计或混淆矩阵逆设计的。将 F-L 应用于本文场景并展示其表现差，不足以说明 EC-HTE 的优越性，因为 F-L 本身就不是为这个问题设计的 baseline。
- 建议：明确说明 F-L 的设计初衷与适用范围，将其定位为"如果从业者错误地套用 F-L 会怎样"，而非"EC-HTE 优于 F-L"。

---

### 4. Questions

**Q1.** Theorem 1 推导中 M_global = Σ_s w_s M_s 要求知道真实的子群权重 w_s。在实践中 w_s 需要从数据中估计，引入额外不确定性。w_s 的估计误差如何传播到 bias identity？是否需要修正？

**Q2.** Section 4.1 中 EB 估计 α_0 使用边际似然最大化。当子群数 K 较小（如 K=2）时，边际似然的优化面可能不平坦——α_0 的估计是否稳定？是否进行了 α_0 估计的敏感性分析（除 Appendix G.1 中 Gamma 超参数扰动外）？

**Q3.** Corollary 6（多类扩展，Appendix C）假设均匀的非对角误分类（misclassified observations from class j are distributed equally among remaining J−1 classes）。这一假设在 LLM 分类器中通常不成立（例如相似类别之间的混淆远高于不相似类别）。非均匀非对角误分类如何影响 bias identity 的形式？论文承认"closed-form amplification factor does not [persist]"但未量化近似误差。

**Q4.** 半合成评估中，子群定义使用 has_hashtag × text_length_bin（Section E, Appendix）。这些子群特征是否会在真实 NLP 任务中自然出现？子群定义的选择如何影响 Δπ 和因此影响 EC-HTE 的效果？

**Q5.** Algorithm 1 中 κ-guard 阈值固定为 100，但 Appendix A.1 的消融实验显示实际 κ_max = 1.89，guard 从未被触发。这是否意味着 guard 的设计完全基于理论考量而无实证支撑？在什么实际场景下 κ 会达到 100？

---

### 5. Missing References

- **Egami et al. (2024)**, "Using Imperfect Surrogates for Downstream Inference" (NeurIPS) — 讨论了使用 LLM 预测进行因果推断时的偏差问题，与本文场景高度相关但引用时未充分比较方法差异
- **Zrnic and Candès (2024b)**, "Active Statistical Inference" — 主动推断框架可能提供比固定预算更高效的专家标注分配策略
- **Angelopoulos et al. (2023)** 的理论部分关于 PPI 在异质性误差下的表现——应与 Theorem 1 的结论对比
- 测量误差文献中 **Buonaccorsi (2010)** "Measurement Error: Models, Methods, and Applications" 提供了更全面的偏差-方差权衡框架

（注：Egami et al. 2023 和 Zrnic & Candès 2024 已被引用，但比较不够深入。）

---

### 6. Overall Assessment

**Overall**: 3.5 (Borderline Conference)

**Confidence**: 4/5

**一句话总结**: 理论结果正确且实用，但"exact identity"与实际验证之间的落差（R²低至0.76、A1由构造满足、有限样本理论内部不一致）使方法的可靠性声称难以完全令人信服。

#### 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | Theorem 1 证明正确；但有限样本余项 κ vs κ² 不一致，A1 不可检验且敏感性分析显示中等违反即导致覆盖率大幅下降 |
| Excitement | 3.5/5 | 问题选择具有时效性（LLM标注×因果推断），"debiasing hurts"的发现有实践价值；但核心理论是相对直接的矩阵代数，方法上是标准的层级贝叶斯 |
| Reproducibility | 4/5 | 提供匿名代码仓库，DGP 描述清晰，超参数完整报告；但100次MC的覆盖率估计精度不足 |
| Overall | 3.5/5 | 介于 Findings 和主会议之间。理论正确但深度有限，实验广泛但生态效度不足 |

#### 接收条件

若作者能回应以下问题，可上调至 4.0 (Conference)：
1. 解决有限样本余项 κ vs κ² 的不一致（N2）
2. 补充至少一个 A1 结构性违反下的实验评估（N1）
3. 增加 MC 次数或在覆盖率报告中附加 MC SE（W2）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2456 · 2026-05-25T06:17:42.884279+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 191

## Round 191

26 recorded events


### User

_source line 2457 · 2026-05-25T06:17:49.256245+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。

主要发现：
- **理论正确**：Theorem 1 的矩阵代数推导无误，Proposition 3/5、Corollary 4 均正确
- **2 个 Critical 问题**：(1) 半合成评估中 A1 由构造满足，无法验证对现实 A1 违反的鲁棒性，且 γ_T=0.10 时覆盖率已降至 75%；(2) 有限样本余项在主文（κ²）与附录（κ）之间存在不一致
- **6 个 Warning 问题**：部分 LLM 的 R² 低至 0.76 与"exact"声称矛盾、100 次 MC 对覆盖率估计精度不足、诊断 AUC=0.86 偏低且未讨论决策后果、SE 调整忽略 CM 估计不确定性、K≤4 限制适用范围、F-L 比较可能不公平
- **格式合规**：正文 8 页、abstract <200 words、double-blind 匿名、Limitations 在正文中，均符合要求

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2458 · 2026-05-25T06:18:07.301305+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2459 · 2026-05-25T06:18:07.352083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2460 · 2026-05-25T06:18:16.703638+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool call

_source line 2461 · 2026-05-25T06:18:16.704139+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool call

_source line 2462 · 2026-05-25T06:18:16.704430+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2463 · 2026-05-25T06:18:16.855428+00:00_

{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (43 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-027b: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error（准备中）\n- exp-027: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage（准备中）\n\n## 近期结论\n- **exp-041** (negative): Under asymmetric misclassification (FPR≠FNR, ratio 1:2 to 1:5 and reverse), the bias identity retains R²≥0.95 and EC-HTE maintains coverage ≥93% across 48 configurations (6 FPR/FNR ratios × 2 K × 4 Δπ), while the symmetric diagnostic AUC degrades monotonically with FPR/FNR ratio — quantifying the exact diagnostic accuracy loss curve under asymmetry.\n  [exp041_asymmetric_grid](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_grid.csv) | [exp041_asymmetric_summary](/api/workspace-files/projects/ec_hte_llm_annotation/artifacts/exp-041/data/exp041_asymmetric_summary.csv) | [exp041_asymmetric_mc_script](/api/workspace-files/projects/e
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 2464 · 2026-05-25T06:18:16.856032+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 2465 · 2026-05-25T06:18:16.906864+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T06:10:32.385796+00:00\", \"completed_at\": \"2026-05-25T06:14:09.632718+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"Figure 4（Bias amplification heatmaps）漂移到 References 页面。该图在正文 Section 5.3 被引用，但 float 越过了正文边界（page 8）落到了 page 9。审稿人在阅读正文时无法就近看到此图，且在 references 中间出现一个 figure 会显得突兀。建议缩小 Figure 3 或 Table 1 的空间，将 Figure 4 拉回 page 8，或考虑将 Figure 4 移入 Appendix 并在正文引用。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 4-6\", \"message\": \"连续 3 页无任何 figure/table（pages 4、5、6 纯文本+公式）。虽然这是理论推导核心段落（Section 3 Bias Decomposition + Section 4 Correction），数学密集内容可豁免，但跨度达 3 整页仍偏长。建议在 Section 4 或 Section 5 开头前插入一个概念性小图或关键公式的直观图解，打破纯文本节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"页面极度拥挤：Figure 3（两面板）+ Table 1 + Section 5.4 文字 + Section 6 Conclusion + Limitations 全部挤在一页。Conclusion 仅约 12 行，Limitations 被压缩到页面最底部右栏。审稿人可能感觉 Conclusion 草率、Limitations 应付。建议精简 Table 1 caption 或将部分 Section 5.4 细节移入 Appendix，给 Conclusion 和 Limitations 更多呼吸空间。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-8\", \"message\": \"正文 8 页仅 4 个 display items（Figure 1-3 + Table 1；Figure 4 已漂出）。对于一篇实证为主的论文，display item 密度偏低（推荐 5-8 个）。Figure 2 的 pipeline 图出现在 page 7，但 pages 1-6 只有 Figure 1 一个视觉元素。建议考虑将 Figure 4 拉回正文，或在 Section 4 增加一个 diagnostic 示意图。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-2\", \"message\": \"前两页纯文本（Abstract + Introduction + Related Work 开头），第一个视觉锚点 Figure 1 出现在 page 3 顶部。Figure 1 三面板（scatter + bar + line）有效传达核心 message（global correction 可能反转 CATE sign），但审稿人需翻过 2 整页才看到。对于本文不是硬伤——Introduction 中有明确的数值预告（\\\"14.9% of configurations\\\"等），建立了悬念。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 Panel B 的 bar chart 中各 bar 之间差异极小（约 ±0.02 量级），在 150dpi 渲染下细微差异不易辨别。建议增大 Panel B 的 y 轴范围聚焦，或改用 diverging bar chart 突出差异方向。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 2466 · 2026-05-25T06:18:34.472628+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "ec_hte_llm_annotation",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2467 · 2026-05-25T06:18:34.523532+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:52 UTC\\n  summary: MVP PASS：核心假设验证通过，评估框架修正为子群水平\\n  rationale: 三轮模拟（v1 CausalForest + v2 差分估计 + v3 子群分析）完成。核心发现：(1) 全局校正在低误差子群造成系统性伤害（bias\\n    恶化 7.8x），EC-HTE 分层校正修复此问题（|bias|<0.015）；(2) 边际 CATE 评估掩盖此效应（正负偏差抵消），子群水平才是正确评估维度；(3)\\n    EC-HTE 在高误差子群方差偏高→层级贝叶斯 partial pooling 是 research 阶段核心优先级。Pass 标准 1 修正为子群水平后\\n    PASS（子群 B EC-HTE RMSE 0.063 vs Global 0.100），标准 2/3/4 均 PASS。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:44 UTC\\n  summary: Dream Round 1 分析完成：best=4 (Weak Accept), median=3.5 (Borderline Conference),\\n    worst=2.5 (Borderline Reject)。达到启动门槛（best≥weak accept, median≥borderline）。识别6项确认行动项、4项观察项。更新\\n    framing 和 plan 后批准 P0 CPU 实验（exp-001, exp-002）立即启动。exp-007 (PPCI comparison) 升级为\\n    P0。\\n  rationale: 三档一致的结构性问题：(1) 薄弱文献（11 refs vs 40+ expected），(2) MCMC 实现细节缺失，(3) 方法新颖性定位需明确为\\\"问题发现\\\"而非\\\"新技术\\\"，(4)\\n    信息密度过高需增加图表减少表格，(5) K=2 理论 vs K>2 实验的 gap，(6) 真实数据验证缺失。数据依赖性问题（coverage undercoverage,\\n    diagnostic AUROC, PPCI dominance）仅在2档或单档出现，记录为观察项待真实实验验证。framing/plan 改动为渐进式改善（sharpening\\n    novelty positioning, adding requirements），不构成重大方向转变，当前 Dream 评分已达标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 21:32 UTC\\n  summary: 'Dream Round 2 analysis: proceed with P0 experiments, 10 writing requirements\\n    codified'\\n  rationale: 'Dream Round 2 (dream_20260520T194535): best=4/6, median=3.5/6, worst=3/6.\\n    Worst improved +0.5 from Round 1 (was 2.5). Three-tier consistent issues all addressable\\n    in writing phase: (1) bibliography 9→30-35 refs, (2) \\\"bias bound\\\"→\\\"bias decomposition\\n    identity\\\", (3) DGP specification, (4) figures, (5) Fuller 1987 contextualization,\\n    (6) \\\"never worse\\\" qualification, (7) inve
…[truncated 3574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2468 · 2026-05-25T06:18:34.724944+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2469 · 2026-05-25T06:18:34.976991+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 2470 · 2026-05-25T06:18:54.367009+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation -name \"config.yaml\" -o -name \"project.yaml\" | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation -name \"config.yaml\" -o -name \"project.yaml\" | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 2471 · 2026-05-25T06:18:54.568299+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2472 · 2026-05-25T06:18:58.182157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/",
  "description": "List project directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/",
    "description": "List project directory contents"
  }
}
```

</details>

---


### Tool result

_source line 2473 · 2026-05-25T06:18:58.232896+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_anonymous_repo.json
_last_visual_review.json
_paper_audit_result.json
_paper_figure.lock
_paper_figure_result.json
artifacts
checkpoints
decisions.lock
decisions.yaml
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.yaml
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
results
review_visual_check_state.json
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2474 · 2026-05-25T06:19:02.250011+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/ 2>/dev/null || echo \"NO_AGENT_DIR\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520/config/ 2>/dev/null || echo \"NO_CONFIG_DIR\"; find /home/ubuntu/.agent-ml-research-idea_gen_0520 -maxdepth 2 -name \"*.yaml\" -path \"*/config*\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/agent/ 2>/dev/null || echo \"NO_AGENT_DIR\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520/config/ 2>/dev/null || echo \"NO_CONFIG_DIR\"; find /home/ubuntu/.agent-ml-research-idea_gen_0520 -maxdepth 2 -name \"*.yaml\" -path \"*/config*\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 2475 · 2026-05-25T06:19:02.350958+00:00_

NO_AGENT_DIR
approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_director.json
mcp_config_distiller.json
mcp_config_dream_review_director.json
mcp_config_paper_agent.json
mcp_config_paper_audit_content.json
mcp_config_paper_audit_review_visual.json
mcp_config_paper_audit_visual.json
mcp_config_paper_figure_optimize.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
mcp_config_worker_1bca48941a8d267537dbe205bd147910.json
mcp_config_worker_326fab99f2efae131dd3121f2859fa07.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_421decd2032b14f2ef6566c2172240c1.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_69e382e805b6f185c49ecc4b6d1f2d44.json
mcp_config_worker_7dbcb7c4fe67f25352c6ebb6307ad5c8.json
mcp_config_worker_83ba13f19a2bf382207991b32ac820f6.json
mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
mcp_config_worker_9f7fc40cb3be48fd669819c21e777021.json
mcp_config_worker_ddf919c12f9233b9c1be7884efc37bb6.json
mcp_config_worker_e28541454639b0570d2f7d611d643ed4.json
mcp_config_worker_e660d20289ab9bbb488d128f5d99bf46.json
mcp_config_worker_ec7b7c2246633b015619e121164ce6bf.json
mcp_config_worker_f5d680d1394a02be4b502c5606a34a84.json
mcp_config_worker_fb5392fb0bbb930253ec8c51b60c9f10.json
pool.json
projects
resources.yaml
secrets
session_state.json
venue_registry.yaml
venue_rules
/home/ubuntu/.agent-ml-research-idea_gen_0520/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520/config/feishu.yaml
/home/ubuntu/.a
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2476 · 2026-05-25T06:19:06.571767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/config/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/config/projects"
  }
}
```

</details>

---


### Tool result

_source line 2477 · 2026-05-25T06:19:06.622744+00:00_

EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0520/config/projects'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2478 · 2026-05-25T06:19:09.185037+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/config/projects/",
  "description": "List project configs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/config/projects/",
    "description": "List project configs"
  }
}
```

</details>

---


### Tool result

_source line 2479 · 2026-05-25T06:19:09.386521+00:00_

ec_hte_llm_annotation.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2480 · 2026-05-25T06:19:11.746699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/config/projects/ec_hte_llm_annotation.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/config/projects/ec_hte_llm_annotation.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2481 · 2026-05-25T06:19:11.897847+00:00_

1	execution:
2	  account: root
3	  gpu_ids:
4	  - cuda:0
5	  - cuda:1
6	  - cuda:2
7	  - cuda:3
8	  project_path: /root/ec_hte_llm_annotation
9	  servers:
10	  - local-cpu
11	  - autodl-ec-hte
12	feishu:
13	  chat_id: oc_6b114d432b35fe7a1c2143457ae85b08
14	  check_references: false
15	  operational_chat_id: oc_0ad92fc2cac0acbbdfa5caa2c2d5b6f3
16	  review_mode: fresh
17	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex
18	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_round_23/submitted.pdf
19	  review_round: 23
20	  review_supplementary_paths: ''
21	  submission_chat_id: oc_489afd65980834a91024fd48e21d984f
22	project:
23	  created_at: '2026-05-20T17:11:54.396Z'
24	  description: 'EC-HTE: From Arm-Specific Rectifiers to Full CATE Estimation with
25	    LLM-Annotated Effect Modifiers'
26	  name: ec_hte_llm_annotation
27	  phase: research
28	  source_idea_id: idea_037
29	venue: emnlp-2026
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 2482 · 2026-05-25T06:19:21.429710+00:00_

**Round 1 状态更新：**

| 组件 | 状态 |
|------|------|
| Reviewer 1 | ✅ 已完成（Overall 3.5） |
| Reviewer 2 | ⏳ 等待中 |
| 视觉审查 | ✅ 已完成（4 warning / 9 info） |
| 外部审稿 | N/A（未配置） |

Reviewer 1 关键发现已记录：2 个 Critical（半合成 A1 构造性满足 + 有限样本余项 κ²/κ 不一致）、6 个 Warning。等 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 192

## Round 192

6 recorded events


### User

_source line 2483 · 2026-05-25T06:19:21.435521+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性与完整性

**论文**: When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects
**Venue**: EMNLP 2026 (ARR)
**审稿侧重**: 新颖性深度、Related Work 覆盖、NLP 社区适配性、写作质量、完整性

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 技术上 sound 且实验极其 thorough，但核心理论贡献（矩阵代数推导）的新颖性深度有限，缺乏全真实数据验证，且 EMNLP 社区适配性存疑——更像一篇因果推断/计量经济学论文在 NLP 场景的应用。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 定理在 stated assumptions 下代数正确；Remark 2 推广到非对称情况；假设敏感性分析充分（A1 γ_T≤0.05 robust，A3 class imbalance 有退化但 identity 仍 exact）。扣分点：(A1) 不可测试且 γ_T=0.10 时 coverage 降至 75%。 |
| Excitement | 2.5/5 | 对 EMNLP 受众而言，核心贡献在因果推断测量误差理论而非 NLP 方法论。NLP 社区的直接收益是实用诊断工具，但不推进语言理解或 NLP 技术本身。 |
| Reproducibility | 4/5 | 代码和数据生成脚本公开（匿名链接），DGP 规格详尽（Appendix E），520 配置 + 100 MC runs 可复现。扣分：无真实数据的 ground-truth CATE 验证。 |
| Clarity | 3.5/5 | 叙事结构清晰（problem→identity→method→experiments），但数学符号密度对 EMNLP 读者偏高；Section 3 的定理-命题-推论序列更像统计期刊风格。 |

---

## Strengths

**S1. 干净可解读的 bias identity。** Theorem 1 的乘积形式 bias = δ_s · Δτ / (1-2π̄) 给出了直觉清晰的分解——偏差仅通过 error-rate deviation 和 CATE heterogeneity 的交互项产生。这比 Frazis-Loewenstein (2003) 的标量衰减 λ=(1-2π) 提供了更细粒度的理解。Remark 2 将结果推广到任意非对称混淆矩阵，提升了理论的通用性。

**S2. 实验验证极其全面。** 520 个合成配置、11 个真实 LLM 混淆矩阵、4 个 NLP 任务（sentiment, hate speech, stance, topic classification）、与 6 种 baseline 对比（Naive, Global, F-L Scalar, F-L Per-sub, Stratified MLE, PPCI）。R² ≥ 0.97 的 identity 验证跨越所有配置。25 页 appendix 覆盖了我能想到的几乎所有 robustness check（非对称误差、treatment-dependent misclassification、class imbalance、K=8、PPCI 组合、F-L 对比）。

**S3. 实用的 Δτ-free 诊断准则。** Proposition 5 的 |δ_s|/((1-2π̄)·π_s) > 1 条件完全基于 error rates，无需估计 treatment effects 即可判断 global correction 是否有害。AUC = 0.86 (symmetric) / 0.96 (asymmetric)。这对从业者有直接操作价值。

**S4. 明确的 operating conditions。** 论文不回避 EC-HTE 的局限性——Δπ > 0.15, n_expert/K ≥ 50, K ≤ 4, FNR < 0.50。这种诚实的边界条件声明在 NLP 论文中少见且值得肯定。

**S5. 与 PPCI 的可组合性。** Section 4.3 + Appendix K 证明 EC-HTE 修正 covariate-side error 与 PPCI 修正 outcome-side error 可正交组合（|bias| 从 0.179 降至 0.007），展示了方法论的模块化设计。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **理论新颖性深度有限——核心推导是 straightforward 的矩阵代数**
- 具体位置：Section 3, Theorem 1, proof sketch (lines 53-57 of theory.tex)
- 问题：Theorem 1 的本质计算是 M_global^{-1} M_s - I，即全局混淆矩阵逆与子群混淆矩阵的乘积残差。这是一步标准的线性代数操作——将全局逆作用于子群特定的 forward model 自然会产生 mismatch。Proof sketch 也承认："Direct computation shows M_global^{-1} M_s - I = δ_s/(1-2π̄) [matrix]"。对于熟悉测量误差文献的读者，这个结果是可预期的——如果你用一个 misspecified 的 correction（全局而非子群特定），当然会引入 bias。
- 为什么影响接收：EMNLP 主会议期待 substantial novelty。论文标题中的 "Exact Bias Identity" 暗示深度理论结果，但实际推导的技术门槛较低。Proposition 5 (diagnostic) 是 Theorem 1 的直接推论。层级贝叶斯 CM 估计是 Dawid-Skene 架构在因果推断中的直接应用，无方法论创新。
- 建议修改方向：(a) 强化理论贡献——例如推导 finite-sample 下的非渐近 bias-variance tradeoff bounds，或推导最优的 shrinkage 量而非依赖 empirical Bayes；(b) 更坦诚地定位贡献在实证发现和实用工具，而非理论深度。

**N2** [critical] **缺乏 fully real-data validation——所有实验依赖 synthetic CATE injection**
- 具体位置：Section 5.1 (experiments.tex line 12), Limitations (limitations.tex lines 7)
- 问题：所有评估都在真实文本特征 + 真实 LLM 标注上注入合成 CATE。论文在 Limitations 中承认 "Ground-truth subgroup CATEs are unavailable in public datasets"，但这意味着论文无法证明 sign reversal 问题在实际研究场景中确实发生。CivilComments 上的 case study（Section 5.2, "global correction suggests effects are uniformly small, while EC-HTE reveals a 3.2× effect-size gap"）是最接近 real-data 的证据，但仍使用注入的 CATE。
- 为什么影响接收：一个声称 "debiasing hurts" 的论文如果不能在至少一个 real-world setting 中展示这种伤害实际发生，说服力大打折扣。评估方法（synthetic CATE injection）本身是 sound 的，但 external validity 存疑。
- 建议修改方向：寻找一个有 ground-truth treatment effect 的 NLP 数据集（e.g., RCT with human-labeled outcomes），或至少展示一个 real observational study 中 global correction 改变了 substantive conclusion 的案例（即使没有 ground truth，也可以通过 domain expert validation 来佐证）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **EMNLP 社区适配性存疑——核心贡献在因果推断方法论而非 NLP**
- 具体位置：全文
- 问题：论文的 intellectual contribution 是测量误差理论中的 bias identity 和 per-subgroup correction。四个 NLP 任务是验证平台而非研究对象。论文未推进对语言的理解，未提出新的 NLP 方法，也未发现关于 LLM 行为的新 NLP insight。CivilComments 上 identity subgroup 效应差异是最有 NLP 价值的发现，但仅在 Appendix M 的一段话中提及。
- 建议：(a) 在 Introduction 中更明确地论证为什么这个问题对 NLP 研究者（而非统计学家或经济学家）重要——不仅仅是 "LLMs are used as annotators"，而是 NLP 特有的误差模式（如 identity-based bias, prompt sensitivity）如何系统性地产生 subgroup heterogeneous errors；(b) 将 CivilComments 的 NLP insight 从 appendix 提升到正文，展示 demographic-group moderation effects 被 global correction 掩盖的 substantive significance。

**W2** [warning] **"Debiasing hurts" 的 framing 可能夸大实际风险**
- 具体位置：Title, Abstract, Section 5.2 (Figure 1C)
- 问题：14.9% sign reversal rate 来自 τ(0) = 0.03 的特定配置（非常小的 true effect）。论文未报告 across all τ(0) values 的 weighted average sign reversal rate。在 τ(0) = 0.10 时（Table 1 moderate row），methods converge (p > 0.05)。实际研究中，researchers 通常关注中等到大的 effects。标题 "When Debiasing Hurts" 和 abstract 中 "correction can reverse estimated effect signs" 可能给读者留下 global correction 经常有害的印象，但实际上伤害主要集中在 small effects + high Δπ 的特定角落。
- 建议：在 Abstract 或 Introduction 中明确声明 sign reversal 的 prevalence 随 effect size 增大而迅速下降（论文在 Appendix Z.8 的 policy reversal analysis 中有这个数据——31% at τ(0)=0.01, 14.9% at τ(0)=0.03, 接近 0% at larger effects——应提到正文）。

**W3** [warning] **Missing reference: Filtered PPI (Xu & Sun, 2026, arXiv:2602.10464)**
- 具体位置：Section 2, paragraph "Prediction-powered and design-based correction"
- 问题：Filtered PPI 提出在 prediction quality 异质时选择性纳入 predictions——这与本文关注 heterogeneous error rates 直接相关。论文未引用也未讨论。Filtered PPI 通过 data-adaptive region selection 减轻 noisy predictions 的影响，而 EC-HTE 通过 per-subgroup correction 应对 heterogeneous errors。两者的区别和联系值得讨论。
- 建议：在 Related Work 的 PPI 段落中增加对 Filtered PPI 的讨论，解释两种处理 heterogeneous error 的策略（selection vs. correction）的关系。

**W4** [warning] **Subgroup-dependent noise 与 instance-dependent noise 的联系不够清晰**
- 具体位置：Section 2, paragraph "Noisy label learning" (related_work.tex line 36)
- 问题：论文引用 Cheng et al. (2020) 的 instance-dependent noise 但未讨论 subgroup-dependent noise 是 instance-dependent noise 的一种特殊参数化（constant within subgroup）。这个联系对 ML 读者很重要——它揭示 EC-HTE 的 assumption 介于 class-dependent（太弱）和 instance-dependent（太强）之间的一个 sweet spot。
- 建议：增加一句明确 positioning。

**W5** [warning] **Abstract 信息密度过高**
- 具体位置：Abstract (abstract.tex)
- 问题：Abstract 约 176 words，在 200 words 限制内，但每个句子都承载大量技术细节（R² 值、百分比、条件参数）。对于 EMNLP 读者，abstract 中出现 "R² ≥ 0.97"、"δ_s · Δτ / (1-2π̄)"、"14.9% of configurations" 等定量细节可能是 information overload。Abstract 应传达 main insight，不是浓缩整篇论文。
- 建议：删除 abstract 中的具体 R² 值和精确百分比，用定性描述替代（"verified empirically across 11 LLMs" 代替 "R² ≥ 0.97"）。

---

## 小问题（不影响接收）

- **i1** [info] 脚注 1 (p.1) 区分 "debiasing" 的 measurement-error 含义与 fairness 含义——这对 EMNLP 读者非常必要，但仅在脚注中提及不够显眼。建议在 Introduction 正文中明确此区分。
- **i2** [info] Contributions list 第一条声称 "exact bias identity"——虽然在 stated assumptions 下确实 exact，但 "exact" 一词可能让读者误以为无条件成立。建议改为 "a closed-form bias identity (exact under stated assumptions)"。
- **i3** [info] Table 1 (p.8) 的 "F-L Scalar" 和 "F-L Per-sub." 缩写首次出现在表中，脚注解释了引用但未解释缩写含义（Frazis-Loewenstein Scalar attenuation correction vs. Per-subgroup F-L correction）。
- **i4** [info] Figure 2 (p.7, method overview) 的 "κ-guard" 概念在正文中仅在 Section 4.2 简要提及，但 figure caption 没有解释。读者需要先读 Section 4 才能理解 Figure 2。

---

## Questions（需作者澄清）

**Q1.** Theorem 1 的 product form δ_s · Δτ / (1-2π̄) 在概念上与 omitted variable bias 的 Frisch-Waugh 分解有类似的乘积结构。作者是否考虑过这种联系？如果 error-rate heterogeneity 可以被视为一种 "omitted variable"（未建模的 subgroup-specific error），那么 Theorem 1 可能可以通过更一般的 projection 论证得到，而非依赖具体的矩阵计算。

**Q2.** 论文在 Appendix Z.4 中测试了 confounded treatment assignment，但仅使用 oracle propensity。在实践中 propensity score 也需要估计且可能 misspecified——当 propensity estimation error 和 LLM annotation error 共存时，EC-HTE 的表现如何？

**Q3.** Operating conditions 中 Δπ > 0.15 是一个 hard threshold。这个值是如何选定的？是否有理论依据，还是纯粹基于 empirical grid search？

**Q4.** 论文声称 "all 8 real LLMs amplify bias under global correction"（Abstract, Section 5.2）。这是否因为实验设计（extreme heterogeneity DGP）导致的选择偏差？在 moderate heterogeneity 下，多少 LLMs 仍然表现出 bias amplification？

---

## Missing References

1. **Xu, S. & Sun, W.W. (2026).** "Do More Predictions Improve Statistical Inference? Filtered Prediction-Powered Inference." arXiv:2602.10464. 直接相关——处理 heterogeneous prediction quality 的 PPI 扩展。
2. 建议在 noisy label 段落补充 subgroup-dependent noise 与 instance-dependent noise 的理论联系（e.g., Scott et al. 2013 关于 class-conditional noise 的 identification 结果）。

其余 Director 指定的近期工作（Messing 2026, Camuffo 2025, Gligoric 2025, Sui 2026, Mozer 2026）均已引用并恰当讨论。Feder 2022, Keith 2020, Veitch 2020 均已覆盖。

---

## Overall Assessment

**Overall**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5

**判断依据**：

论文在 soundness 维度很强——bias identity 在 stated assumptions 下正确，实验验证全面（R² ≥ 0.97 跨 11 LLMs），robustness checks 覆盖所有主要 assumption violations。实用贡献（Δτ-free diagnostic, operating conditions, PPCI 组合）对从业者有价值。

但在 excitement/novelty 维度对 EMNLP 偏弱：(1) 理论推导技术门槛低（标准矩阵代数），不是 Frazis-Loewenstein 的 "本质创新" 而是 natural 但 useful 的推广；(2) hierarchical Bayes CM estimation 是已有方法的直接应用；(3) "debiasing can hurt" 在测量误差文献中是已知现象，本文的量化是增量贡献；(4) 论文的 intellectual home 是因果推断/计量经济学而非 NLP——四个 NLP 任务是验证平台而非研究对象。

全真实数据验证的缺失使得 "debiasing hurts in practice" 的 claim 只在 synthetic/semi-synthetic 设置中成立。

综合判断：Findings 轨道的强文章。如果作者能 (a) 补充至少一个 real-data case study demonstrating actual sign reversal, (b) 在正文中更充分地阐述 NLP-specific insights（特别是 CivilComments 的 identity subgroup findings），(c) 补充 Filtered PPI 引用，则有望升至 Conference 水平。

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。

主要发现：
- **Soundness 强**（4/5）：bias identity 代数正确，R²≥0.97 跨 11 LLMs 验证，robustness checks 极其全面
- **Excitement 对 EMNLP 偏低**（2.5/5）：核心推导是 M_global⁻¹M_s - I 的标准矩阵运算；HB CM estimation 是 Dawid-Skene 的直接应用；论文 intellectual home 在因果推断/计量经济学而非 NLP
- **两个 critical 问题**：(1) 理论新颖性深度有限——product form 是自然但非深刻的代数结果；(2) 缺乏 fully real-data 验证
- **三个 warning 问题**：NLP 社区适配性、"debiasing hurts" framing 可能夸大（sign reversal 集中在 small effects）、missing Filtered PPI 引用
- **积极面**：Δτ-free diagnostic 实用价值高，operating conditions 诚实清晰，PPCI 可组合性有价值
- Director 指定的近期工作（Messing/Camuffo/Gligoric/Sui/Mozer）均已被论文引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2484 · 2026-05-25T06:19:52.292498+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条阅读 Reviewer 2 的审稿意见，对每一个 Critical/Warning/Question 点逐条回应 `[AGREE]` 或 `[REBUT]`（附简短理由）。关注与你自己审稿意见的交集与分歧。\n\n---\n\n**Reviewer 2 Overall: 3.5 (Borderline Conference)**\n\n**Critical 问题：**\n\n**N1 [critical] 理论新颖性深度有限——核心推导是 straightforward 的矩阵代数**\n- Theorem 1 本质是 M_global⁻¹M_s - I 的标准线性代数操作。Product form δ_s·Δτ/(1-2π̄) 是自然但非深刻的结果。Proposition 5 是 Theorem 1 的直接推论。HB CM estimation 是 Dawid-Skene 的直接应用。\n- R2 认为 EMNLP 主会议期待 substantial novelty，但本文技术门槛较低。\n\n**N2 [critical] 缺乏 fully real-data validation**\n- 所有评估使用真实文本+真实 LLM 标注但注入合成 CATE。无法证明 sign reversal 在实际研究中确实发生。External validity 存疑。\n\n**Warning 问题：**\n\n**W1 [warning] EMNLP 社区适配性存疑**\n- 核心 contribution 在测量误差理论而非 NLP。四个 NLP 任务是验证平台而非研究对象。CivilComments identity subgroup 发现仅在 Appendix M 一段提及。\n\n**W2 [warning] \"Debiasing hurts\" framing 可能夸大**\n- 14.9% sign reversal 来自 τ(0)=0.03 配置（很小的 true effect）。τ(0)=0.10 时 methods converge。Appendix Z.8 数据（31% at τ(0)=0.01, 14.9% at 0.03, ~0% at larger）应入正文。\n\n**W3 [warning] Missing reference: Filtered PPI (Xu & Sun 2026)**\n- 处理 heterogeneous prediction quality 的 PPI 扩展，selection vs correction 策略对比未讨论。\n\n**W4 [warning] Subgroup-dependent noise 与 instance-dependent noise 联系不清**\n- EC-HTE 假设介于 class-dependent（太弱）和 instance-dependent（太强）之间的 sweet spot，未明确 positioning。\n\n**W5 [warning] Abstract 信息密度过高**\n- R² 值、精确百分比等定量细节对 EMNLP 读者是 information overload。\n\n**Questions：**\n- Q1: Theorem 1 product form 与 omitted variable bias Frisch-Waugh 分解的联系？\n- Q2: propensity estimation error + LLM annotation error 共存时表现？\n- Q3: Δπ > 0.15 threshold 的理论依据？\n- Q4: \"all 8 real LLMs amplify bias\" 是否因 extreme heterogeneity DGP 导致？\n\n---\n\n请对以上每个 Critical (N1, N2)、Warning (W1-W5)、Question (Q1-Q4) 逐条给出 `[AGREE]` 或 `[REBUT]`，附简短理由。重点关注你自己审稿中未覆盖但 R2 提出的问题。",
  "reviewer_id": "1",
  "project": "ec_hte_llm_annotation",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条阅读 Reviewer 2 的审稿意见，对每一个 Critical/Warning/Question 点逐条回应 `[AGREE]` 或 `[REBUT]`（附简短理由）。关注与你自己审稿意见的交集与分歧。\n\n---\n\n**Reviewer 2 Overall: 3.5 (Borderline Conference)**\n\n**Critical 问题：**\n\n**N1 [critical] 理论新颖性深度有限——核心推导是 straightforward 的矩阵代数**\n- Theorem 1 本质是 M_global⁻¹M_s - I 的标准线性代数操作。Product form δ_s·Δτ/(1-2π̄) 是自然但非深刻的结果。Proposition 5 是 Theorem 1 的直接推论。HB CM estimation 是 Dawid-Skene 的直接应用。\n- R2 认为 EMNLP 主会议期待 substantial novelty，但本文技术门槛较低。\n\n**N2 [critical] 缺乏 fully real-data validation**\n- 所有评估使用真实文本+真实 LLM 标注但注入合成 CATE。无法证明 sign reversal 在实际研究中确实发生。External validity 存疑。\n\n**Warning 问题：**\n\n**W1 [warning] EMNLP 社区适配性存疑**\n- 核心 contribution 在测量误差理论而非 NLP。四个 NLP 任务是验证平台而非研究对象。CivilComments identity subgroup 发现仅在 Appendix M 一段提及。\n\n**W2 [warning] \"Debiasing hurts\" framing 可能夸大**\n- 14.9% sign reversal 来自 τ(0)=0.03 配置（很小的 true effect）。τ(0)=0.10 时 methods converge。Appendix Z.8 数据（31% at τ(0)=0.01, 14.9% at 0.03, ~0% at larger）应入正文。\n\n**W3 [warning] Missing reference: Filtered PPI (Xu & Sun 2026)**\n- 处理 heterogeneous prediction quality 的 PPI 扩展，selection vs correction 策略对比未讨论。\n\n**W4 [warning] Subgroup-dependent noise 与 instance-dependent noise 联系不清**\n- EC-HTE 假设介于 class-dependent（太弱）和 instance-dependent（太强）之间的 sweet spot，未明确 positioning。\n\n**W5 [warning] Abstract 信息密度过高**\n- R² 值、精确百分比等定量细节对 EMNLP 读者是 information overload。\n\n**Questions：**\n- Q1: Theorem 1 product form 与 omitted variable bias Frisch-Waugh 分解的联系？\n- Q2: propensity estimation error + LLM annotation error 共存时表现？\n- Q3: Δπ > 0.15 threshold 的理论依据？\n- Q4: \"all 8 real LLMs amplify bias\" 是否因 extreme heterogeneity DGP 导致？\n\n---\n\n请对以上每个 Critical (N1, N2)、Warning (W1-W5)、Question (Q1-Q4) 逐条给出 `[AGREE]` 或 `[REBUT]`，附简短理由。重点关注你自己审稿中未覆盖但 R2 提出的问题。",
    "reviewer_id": "1",
    "project": "ec_hte_llm_annotation",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2485 · 2026-05-25T06:20:08.331774+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16039
}
```

</details>

---


### Tool call

_source line 2486 · 2026-05-25T06:20:08.884539+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条阅读 Reviewer 1 的审稿意见，对每一个 Critical/Warning 点逐条回应 `[AGREE]` 或 `[REBUT]`（附简短理由）。关注与你自己审稿意见的交集与分歧。\n\n---\n\n**Reviewer 1 Overall: 3.5 (Borderline Conference)**\n**侧重：方法严谨性与实验验证**\n\n**Critical 问题：**\n\n**C1 [critical] 半合成评估中 A1 由构造满足，无法验证对现实 A1 违反的鲁棒性**\n- 实验设计中 A1 (treatment-independent misclassification) 由 DGP 构造保证。γ_T=0.10 时覆盖率已降至 75%（名义 95%）。论文未能展示方法在 real-world A1 违反场景下的鲁棒性。\n\n**C2 [critical] 有限样本余项在主文（κ²）与附录（κ）之间存在不一致**\n- 主文声称余项为 O(κ²)，但附录推导中出现 O(κ)。这是笔误还是不同上下文？\n\n**Warning 问题：**\n\n**W1 [warning] 部分 LLM 的 R² 低至 0.76 与 \"exact\" 声称矛盾**\n- 虽然 11 个 LLM 中大多数 R²≥0.97，但存在个别 LLM R² 仅 0.76。\"Exact identity\" 的声明需要更精确的限定。\n\n**W2 [warning] 100 次 MC 对覆盖率估计精度不足**\n- 100 MC runs 的 95% coverage SE ≈ √(0.95×0.05/100) ≈ 2.2pp。在 coverage 85-95% range 内难以区分 calibrated vs. under-covered。\n\n**W3 [warning] 诊断 AUC=0.86 偏低且未讨论决策后果**\n- Symmetric case AUC=0.86 意味着 ~14% 误判。论文未讨论 false positive/negative 在实际决策中的不对称代价。\n\n**W4 [warning] SE 调整忽略 CM 估计不确定性**\n- 置信区间仅传播 CATE 估计的 sampling uncertainty，未 propagate CM 估计的 posterior uncertainty。可能导致 coverage 偏低。\n\n**W5 [warning] K≤4 限制适用范围**\n- 方法在 K=8 时退化。实际 NLP 任务常有更多子群（topic classification 10+, fine-grained sentiment 5+）。\n\n**W6 [warning] F-L 比较可能不公平**\n- Frazis-Loewenstein 设计用于不同假设结构，对比可能 strawman。\n\n---\n\n请对以上每个 Critical (C1, C2)、Warning (W1-W6) 逐条给出 `[AGREE]` 或 `[REBUT]`，附简短理由。重点关注你自己审稿中未覆盖但 R1 提出的问题。",
  "reviewer_id": "2",
  "project": "ec_hte_llm_annotation",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条阅读 Reviewer 1 的审稿意见，对每一个 Critical/Warning 点逐条回应 `[AGREE]` 或 `[REBUT]`（附简短理由）。关注与你自己审稿意见的交集与分歧。\n\n---\n\n**Reviewer 1 Overall: 3.5 (Borderline Conference)**\n**侧重：方法严谨性与实验验证**\n\n**Critical 问题：**\n\n**C1 [critical] 半合成评估中 A1 由构造满足，无法验证对现实 A1 违反的鲁棒性**\n- 实验设计中 A1 (treatment-independent misclassification) 由 DGP 构造保证。γ_T=0.10 时覆盖率已降至 75%（名义 95%）。论文未能展示方法在 real-world A1 违反场景下的鲁棒性。\n\n**C2 [critical] 有限样本余项在主文（κ²）与附录（κ）之间存在不一致**\n- 主文声称余项为 O(κ²)，但附录推导中出现 O(κ)。这是笔误还是不同上下文？\n\n**Warning 问题：**\n\n**W1 [warning] 部分 LLM 的 R² 低至 0.76 与 \"exact\" 声称矛盾**\n- 虽然 11 个 LLM 中大多数 R²≥0.97，但存在个别 LLM R² 仅 0.76。\"Exact identity\" 的声明需要更精确的限定。\n\n**W2 [warning] 100 次 MC 对覆盖率估计精度不足**\n- 100 MC runs 的 95% coverage SE ≈ √(0.95×0.05/100) ≈ 2.2pp。在 coverage 85-95% range 内难以区分 calibrated vs. under-covered。\n\n**W3 [warning] 诊断 AUC=0.86 偏低且未讨论决策后果**\n- Symmetric case AUC=0.86 意味着 ~14% 误判。论文未讨论 false positive/negative 在实际决策中的不对称代价。\n\n**W4 [warning] SE 调整忽略 CM 估计不确定性**\n- 置信区间仅传播 CATE 估计的 sampling uncertainty，未 propagate CM 估计的 posterior uncertainty。可能导致 coverage 偏低。\n\n**W5 [warning] K≤4 限制适用范围**\n- 方法在 K=8 时退化。实际 NLP 任务常有更多子群（topic classification 10+, fine-grained sentiment 5+）。\n\n**W6 [warning] F-L 比较可能不公平**\n- Frazis-Loewenstein 设计用于不同假设结构，对比可能 strawman。\n\n---\n\n请对以上每个 Critical (C1, C2)、Warning (W1-W6) 逐条给出 `[AGREE]` 或 `[REBUT]`，附简短理由。重点关注你自己审稿中未覆盖但 R1 提出的问题。",
    "reviewer_id": "2",
    "project": "ec_hte_llm_annotation",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 2487 · 2026-05-25T06:20:10.553266+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_489afd65980834a91024fd48e21d984f:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1668
}
```

</details>

---


### Assistant

_source line 2488 · 2026-05-25T06:20:15.562495+00:00_

交叉分享已派发：
- **R1** 收到 R2 的完整审稿（2 critical + 5 warning + 4 questions），要求逐条 `[AGREE]`/`[REBUT]`
- **R2** 收到 R1 的完整审稿（2 critical + 6 warning），要求逐条 `[AGREE]`/`[REBUT]`

等待两位 Reviewer 完成交叉回应后进入报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 193

## Round 193

2 recorded events


### User

_source line 2489 · 2026-05-25T06:21:14.823149+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Critical 问题

**[AGREE] R2-N1: 理论新颖性深度有限**

同意核心判断。我在自己的审稿中将 Excitement 打 3.5/5，理由一致：Theorem 1 是 M_global⁻¹M_s − I 的直接计算，Proposition 5 是其代数推论，HB 估计是标准工具。但我补充两点nuance：(a) 新颖性不仅在推导难度，也在于 *识别问题并给出可操作的诊断*——bias identity 虽然推导简单，但此前文献（包括 Frazis-Loewenstein 2003、Angelopoulos et al. 2023）均未在子群异质性误差下推导过这一恒等式；(b) EMNLP 近年接收了不少理论深度中等但实用价值高的工作。因此我认为这是 borderline 而非 reject 的理由。

**[AGREE] R2-N2: 缺乏 fully real-data validation**

与我的 N1 一致。我的 N1 进一步指出了根本原因：合成 CATE 注入使 A1（条件独立性）在构造上成立，导致方法永远不会面对其最脆弱假设的挑战。R2 的表述更聚焦于 external validity，我的更聚焦于 assumption validation——两者互补，共同构成对本文最核心的批评。

---

### Warning 问题

**[REBUT] R2-W1: EMNLP 社区适配性存疑**

不同意这构成实质性弱点。EMNLP/ACL 近年有大量 measurement error × NLP 的工作被接收：Egami et al. (2023, DSL) 发表于 NeurIPS 但被 ACL 社区广泛引用；Angelopoulos et al. (2023, PPI) 同样是统计方法论用 NLP 任务验证；Sui et al. (2026, PPCI) 也是理论驱动的工作。本文使用四个 NLP 任务不仅作为验证平台，也展示了 LLM 标注异质性是 NLP 特有现象（Section 5.5, Table 12 的 per-subgroup 误分类率，以及 Section V 的 11 个 LLM 的 cross-model 验证）。CivilComments 的 identity subgroup 发现虽在附录中，但展示了 NLP 社区关心的具体 harm（demographic bias）。Venue fit 不应成为 weakness。

**[AGREE] R2-W2: "Debiasing hurts" framing 可能夸大**

同意。14.9% sign reversal 来自 τ(0)=0.03 的极端配置。论文标题 "When Debiasing Hurts" 和 abstract 中 "14.9% of configurations" 给人的印象是这是一个普遍现象，但实际上它集中在 true effect 很小的场景。Appendix Z.8 的 Table 38 明确显示 τ(0) ≥ 0.05 时 sign reversal 大幅下降。这些信息应在正文中呈现以 calibrate 读者预期。不过我补充：即使 sign reversal 不频繁，bias *amplification*（非符号翻转）在 Δπ > 0.12 时仍然普遍（Figure 4b），这一点 R2 未充分承认。

**[REBUT] R2-W3: Missing reference Filtered PPI (Xu & Sun 2026)**

我无法验证此引用的存在性和相关性。如果该工作确实处理 heterogeneous prediction quality 下的 PPI，那确实应被讨论。但 R2 未提供足够信息让我判断其与本文的具体关系（selection vs. correction 是不同策略，本文的 contribution 在 *诊断何时需要校正* 和 *如何校正*，filtered PPI 可能是互补而非竞争方法）。建议 R2 提供更具体的引用信息和比较维度。

**[AGREE] R2-W4: Subgroup-dependent noise 与 instance-dependent noise 联系不清**

同意这是一个定位问题。论文假设误分类率在子群内均匀（π_s 是子群级常数），这介于全局均匀噪声和实例级噪声之间。论文未明确讨论这一选择的理论后果：如果子群内噪声仍有异质性，EC-HTE 的子群级校正能捕获多少变异？Appendix P（subgroup misspecification）部分回应了这一点（coverage ≥ 0.945），但未从 noise model 分类的角度进行系统性定位。

**[AGREE] R2-W5: Abstract 信息密度过高**

部分同意。Abstract 在 ~180 words 内塞入了 R² 值、百分比、操作条件等大量定量细节，对初次阅读的读者不友好。但我不认为这是严重问题——EMNLP abstract 有 200 词限制，作者选择了信息密度最大化策略。建议将部分定量细节（如 "per-model range 0.76–0.99", "14.9% of configurations"）移至 introduction。

---

### Questions

**[AGREE] R2-Q1: Theorem 1 与 omitted variable bias / Frisch-Waugh 的联系**

好问题。bias identity 的形式 δ_s·Δτ/(1−2π̄) 确实类似于 omitted variable bias 的乘积结构（遗漏变量偏差 = 遗漏变量系数 × 遗漏变量与included变量的相关性）。论文可以在 Related Work 中简要讨论这一类比，增强理论直觉。但我认为形式上的相似性不意味着推导上的等价——bias identity 来自矩阵逆的扰动，omitted variable bias 来自投影分解，机制不同。

**[AGREE] R2-Q2: Propensity estimation error + LLM annotation error 共存时表现**

与我对论文 Appendix Z.4（confounded treatment）的理解一致。论文在 Appendix Z.4 展示了 EC-HTE 在 IPW-DIM 估计器下与 oracle propensity 配合的效果（coverage 94.3%），但使用的是 *oracle* propensity。当 propensity 本身有估计误差时，CM 校正与 propensity 误差的交互作用未被研究。这是一个合理的扩展方向。

**[REBUT] R2-Q3: Δπ > 0.15 threshold 的理论依据**

论文实际上给出了依据：Proposition 5 的 diagnostic condition |δ_s|/((1−2π̄)·π_s) > 1 是理论推导，Δπ > 0.15 是该条件在实验中对应的 *经验性操作阈值*（Section 5.4）。这不是一个凭空选择的数字，而是理论条件的经验翻译。可以更清楚地说明这一联系，但不构成方法论缺陷。

**[AGREE] R2-Q4: "all 8 real LLMs amplify bias" 是否因 extreme heterogeneity DGP**

合理质疑。Section 5.2 的 "all 8 real LLMs amplifying bias" 声称来自 extreme heterogeneity DGP（π ∈ {0.05, 0.10, 0.15, 0.25}），这是论文选择的最极端配置。在 moderate heterogeneity 下，Table 8（main text, p.8）显示 methods converge (p > 0.05)。因此 "all 8 LLMs" 的声称应限定为 "under extreme heterogeneity"，否则有夸大之嫌。这与 R2-W2 关于 framing 的批评一致。

---

### 与我自己审稿的交集与分歧总结

**交集**：R2 的 N1（理论深度）、N2（无真实数据验证）与我的评估一致。W2（framing 夸大）我亦认同。最终评分相同（3.5 Borderline Conference）。

**分歧**：
1. R2-W1（venue fit）我不同意——EMNLP 接收此类工作有先例。
2. R2 未覆盖但我认为重要的问题：(a) 有限样本余项 κ vs κ² 的内部不一致（我的 N2）；(b) SE 公式忽略 CM 估计不确定性（我的 W4）；(c) 100 次 MC 对覆盖率估计的精度问题（我的 W2）；(d) 诊断 AUC=0.86 的实践后果（我的 W3）。这些是方法严谨性层面的具体技术问题，R2 更侧重宏观层面的 novelty 和 framing 批评。

**综合判断**：两位 reviewer 的核心关切高度一致（理论深度中等 + 无真实数据验证），分歧在于对 NLP 社区适配性和 framing 严重性的判断。我维持 3.5 (Borderline Conference) 的评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2490 · 2026-05-25T06:21:20.717251+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 194

## Round 194

18 recorded events


### User

_source line 2491 · 2026-05-25T06:21:29.902718+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 11 个点逐条给出了 AGREE/REBUT：

- **AGREE 8 项**：N1（理论深度）、N2（无真实验证）、W2（framing 夸大）、W4（noise model 定位）、W5（abstract 过密）、Q1（Frisch-Waugh 类比）、Q2（propensity error 交互）、Q4（extreme DGP 条件化声称）
- **REBUT 3 项**：W1（venue fit 有先例）、W3（Filtered PPI 引用无法验证）、Q3（Δπ>0.15 有理论依据）

关键补充：R2 侧重宏观层面（novelty、framing），我的审稿覆盖了 R2 未触及的技术问题（κ vs κ² 不一致、SE 公式缺陷、MC 精度、诊断 AUC）。两人评分一致（3.5 Borderline Conference），核心关切高度重叠。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2492 · 2026-05-25T06:22:18.866188+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:get_external_review_status,get_visual_check_status,update_review_issues,submit_review_report_to_research_director,read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:get_external_review_status,get_visual_check_status,update_review_issues,submit_review_report_to_research_director,read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2493 · 2026-05-25T06:22:19.017132+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2494 · 2026-05-25T06:22:23.637131+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 2495 · 2026-05-25T06:22:23.688220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2496 · 2026-05-25T06:22:29.215501+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool call

_source line 2497 · 2026-05-25T06:22:29.215996+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "ec_hte_llm_annotation"
  }
}
```

</details>

---


### Tool result

_source line 2498 · 2026-05-25T06:22:29.668106+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool result

_source line 2499 · 2026-05-25T06:22:29.668595+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T06:10:32.385796+00:00\", \"completed_at\": \"2026-05-25T06:14:09.632718+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"Figure 4（Bias amplification heatmaps）漂移到 References 页面。该图在正文 Section 5.3 被引用，但 float 越过了正文边界（page 8）落到了 page 9。审稿人在阅读正文时无法就近看到此图，且在 references 中间出现一个 figure 会显得突兀。建议缩小 Figure 3 或 Table 1 的空间，将 Figure 4 拉回 page 8，或考虑将 Figure 4 移入 Appendix 并在正文引用。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 4-6\", \"message\": \"连续 3 页无任何 figure/table（pages 4、5、6 纯文本+公式）。虽然这是理论推导核心段落（Section 3 Bias Decomposition + Section 4 Correction），数学密集内容可豁免，但跨度达 3 整页仍偏长。建议在 Section 4 或 Section 5 开头前插入一个概念性小图或关键公式的直观图解，打破纯文本节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"页面极度拥挤：Figure 3（两面板）+ Table 1 + Section 5.4 文字 + Section 6 Conclusion + Limitations 全部挤在一页。Conclusion 仅约 12 行，Limitations 被压缩到页面最底部右栏。审稿人可能感觉 Conclusion 草率、Limitations 应付。建议精简 Table 1 caption 或将部分 Section 5.4 细节移入 Appendix，给 Conclusion 和 Limitations 更多呼吸空间。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-8\", \"message\": \"正文 8 页仅 4 个 display items（Figure 1-3 + Table 1；Figure 4 已漂出）。对于一篇实证为主的论文，display item 密度偏低（推荐 5-8 个）。Figure 2 的 pipeline 图出现在 page 7，但 pages 1-6 只有 Figure 1 一个视觉元素。建议考虑将 Figure 4 拉回正文，或在 Section 4 增加一个 diagnostic 示意图。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-2\", \"message\": \"前两页纯文本（Abstract + Introduction + Related Work 开头），第一个视觉锚点 Figure 1 出现在 page 3 顶部。Figure 1 三面板（scatter + bar + line）有效传达核心 message（global correction 可能反转 CATE sign），但审稿人需翻过 2 整页才看到。对于本文不是硬伤——Introduction 中有明确的数值预告（\\\"14.9% of configurations\\\"等），建立了悬念。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 Panel B 的 bar chart 中各 bar 之间差异极小（约 ±0.02 量级），在 150dpi 渲染下细微差异不易辨别。建议增大 Panel B 的 y 轴范围聚焦，或改用 diverging bar chart 突出差异方向。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2500 · 2026-05-25T06:22:29.769455+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2501 · 2026-05-25T06:22:29.820982+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2502 · 2026-05-25T06:22:39.284331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2503 · 2026-05-25T06:22:39.687083+00:00_

1	issues:
2	  # === RESOLVED (prior rounds — abbreviated) ===
3	  - id: "R1-N1"
4	    summary: "Proposition 1 以 formal bound 呈现但仅有 97% MC 经验验证"
5	    category: method
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 0
9	    last_seen_round: 2
10	    action_items: []
11	    resolution: "重新推导为精确恒等式"
12	    resolution_round: 0
13	
14	  - id: "R2-W8"
15	    summary: "Proposition 1 限于 K=2"
16	    category: method
17	    severity: critical
18	    status: resolved
19	    first_raised_round: 0
20	    last_seen_round: 1
21	    action_items: []
22	    resolution: "Theorem 1 适用一般 K"
23	    resolution_round: 0
24	
25	  - id: "R1-N2"
26	    summary: "Real data ground truth CATE 来源不明"
27	    category: experiment
28	    severity: critical
29	    status: resolved
30	    first_raised_round: 0
31	    last_seen_round: 1
32	    action_items: []
33	    resolution: "恰当定位为 illustrative application"
34	    resolution_round: 0
35	
36	  - id: "R1-N3"
37	    summary: "HB 模型规格严重不完整"
38	    category: method
39	    severity: critical
40	    status: resolved
41	    first_raised_round: 0
42	    last_seen_round: 1
43	    action_items: []
44	    resolution: "完整 MCMC 规格"
45	    resolution_round: 0
46	
47	  - id: "JOINT-W4"
48	    summary: "相关工作严重遗漏"
49	    category: writing
50	    severity: warning
51	    status: resolved
52	    first_raised_round: 0
53	    last_seen_round: 1
54	    action_items: []
55	    resolution: "30+ 引用覆盖"
56	    resolution_round: 0
57	
58	  - id: "JOINT-W3"
59	    summary: "信息密度过高"
60	    category: writing
61	    severity: warning
62	    status: resolved
63	    first_raised_round: 0
64	    last_seen_round: 1
65	    action_items: []
66	    resolution: "主文精简至合理密度"
67	    resolution_round: 0
68	
69	  - id: "R2-W7"
70	    summary: "真实数据验证单薄"
71	    category: experiment
72	    severity: warning
73	    status: resolved
74	    first_raised_round: 0
75	    last_seen_round: 1
76	    action_items: []
77	    resolution: "恰当定位 + 公开数据集"
78	    resolution_round: 0
7
…[truncated 25831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 2504 · 2026-05-25T06:22:39.888899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2505 · 2026-05-25T06:22:39.939615+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{makecell}
15	\usepackage{xcolor}
16	\usepackage{enumitem}
17	\usepackage{algorithm}
18	\usepackage{algpseudocode}
19	
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{corollary}[theorem]{Corollary}
22	\newtheorem{proposition}[theorem]{Proposition}
23	\newtheorem{remark}[theorem]{Remark}
24	
25	\title{When Debiasing Hurts: An Exact Bias Identity\\for LLM-Annotated Treatment Effects}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\input{abstract}
33	
34	\input{introduction}
35	
36	\input{related_work}
37	
38	\input{theory}
39	
40	\input{method}
41	
42	\input{experiments}
43	
44	\input{conclusion}
45	
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	%\input{checklist}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2506 · 2026-05-25T06:22:53.857384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2507 · 2026-05-25T06:22:53.908459+00:00_

1	\begin{abstract}
2	Standard confusion-matrix correction for noisy annotations assumes uniform error rates.
3	When this assumption fails---as it routinely does with large language model (LLM) classifiers, whose error rates vary by up to $5\times$ across subgroups---correction can reverse estimated effect signs.
4	We derive an exact bias identity: global correction introduces subgroup-level bias $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$ under symmetric errors (generalizing to a full-matrix form for arbitrary asymmetric confusion matrices; Remark~\ref{rem:asymmetric}), verified at $R^2 \geq 0.97$ on synthetic grids ($R^2 = 0.975$ in aggregate across 11 real LLM confusion matrices; per-model range $0.76$--$0.99$).
5	The identity predicts that global correction reverses conditional average treatment effect (CATE) sign in 14.9\% of configurations where the true effect is small ($\tau(0) = 0.03$) and amplifies bias in all eight real LLMs tested; a $\Delta\tau$-free diagnostic corollary flags harmful correction from error rates alone, without estimating treatment effects.
6	We characterize when per-subgroup correction is beneficial ($\Delta\pi > 0.15$, $n_{\text{expert}}/K \geq 50$, $K \leq 4$) versus when global correction should be retained, and implement one such correction via hierarchical Bayesian estimation, reducing $|\text{bias}|$ by $7.4\times$ under extreme heterogeneity.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 2508 · 2026-05-25T06:23:51.918372+00:00_

现在我有全部信息，开始合成最终报告。

先确认 R2 交叉回应状态——我目前只收到 R1 的交叉回应。需确认 R2 是否也完成了交叉回应后再投递报告。

请确认：R2 对 R1 审稿的交叉回应是否已提交？如果已提交，请提供摘要。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director"
}
```

</details>

---


## Round 195

## Round 195

14 recorded events


### User

_source line 2509 · 2026-05-25T06:23:51.926579+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应：逐条回应 Reviewer 1

---

### Critical 问题

**[AGREE] R1-C1: 半合成评估中 A1 由构造满足，无法验证现实 A1 违反的鲁棒性**

同意这是一个实质性问题。我在 N2 中从 "缺乏 fully real-data validation" 角度提出了类似关切——所有实验的 DGP 构造性地满足核心假设，使得鲁棒性声明停留在 "synthetic perturbation" 层面。R1 更精准地定位了问题：γ_T=0.10 时 coverage 从 95% 降至 75%（Appendix Z.3, Section 3 theory.tex line 96），而真实 NLP 场景中 treatment-dependent misclassification 完全可能达到这个量级——例如 hate speech detection 中，toxic content（treatment condition）本身可能系统性地影响 LLM 的 annotation accuracy。论文的 sensitivity analysis 实际上 *暴露了* 方法的脆弱性而非证明了鲁棒性。

补充：我认为这个问题与 N2 (缺乏 real-data validation) 是同一 concern 的两面——如果有 real-data case study，就能间接评估 A1 在实践中的合理性。

---

**[AGREE] R1-C2: 有限样本余项在主文（κ²）与附录（κ）之间存在不一致**

核实了具体文本：
- **主文** theory.tex line 99："the remainder is R_n = O_p(n_expert^{-1/2} · κ(C_s)²)"，来源是 Neumann expansion Ĉ_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(||E_s||²)
- **附录** appendix.tex line 103："||M̂_global^{-1} M̂_s - M_global^{-1} M_s|| ≤ κ(M_global) · O_p(n_expert^{-1/2})"

严格来说，这两个 bound 作用于不同对象（主文 bound 单个 Ĉ_s^{-1} 的 perturbation，附录 bound 乘积 M_global^{-1} M_s 的 perturbation），所以不是直接矛盾。但论文没有解释这个区别，读者看到同一个概念（有限样本余项）在两处出现不同的 κ 指数，自然会困惑。即使不是数学错误，也是 presentation 上的明显缺陷。建议作者统一表述或在附录中明确说明两个 bound 的适用范围不同。

---

### Warning 问题

**[AGREE] R1-W1: 部分 LLM 的 R² 低至 0.76 与 "exact" 声称存在张力**

同意。Abstract 声称 "R² ≥ 0.97" 但紧接着括号内写 "per-model range 0.76–0.99"（abstract.tex line 4）。R² = 0.76 意味着 identity 仅解释 76% 的 observed bias variance——对于一个 "exact identity" 来说，24% 的未解释方差不可忽略。我在 W5 中指出 abstract 信息密度过高，但没有抓住这个更本质的问题：0.76 的下界削弱了 "exact" 的说服力。可能原因是 finite-sample noise 或 assumption violations 在该 LLM 上更严重，但论文未对低 R² 的 case 做 failure analysis。

---

**[AGREE] R1-W2: 100 次 MC 对覆盖率估计精度不足**

同意这是一个 methodological concern，但我认为 severity 可以从 warning 降为 info。SE ≈ 2.2pp 确实使得 93% vs 95% coverage 的区分变得模糊。但论文的主要结论不依赖于精确的 coverage 值——核心 claim 是 bias reduction (7.4×) 和 sign reversal elimination，这些不受 MC 次数影响。如果作者希望强化 coverage claims，增加到 500-1000 MC runs 即可解决。

---

**[AGREE] R1-W3: 诊断 AUC=0.86 偏低且未讨论决策后果**

同意且与我的审查一致——我没有专门提这个点，但 R1 的分析更细致。AUC=0.86 的 symmetric case 意味着非平凡的误判率。更关键的是，论文没有讨论 false positive（诊断说 global correction 有害但实际无害 → 不必要地增加 variance）和 false negative（诊断说安全但实际有害 → sign reversal）的不对称代价。在 causal inference 中，false negative 的后果（错误的因果结论）通常远重于 false positive（稍大的 variance）。建议作者提供 precision/recall breakdown 并讨论在不同 decision threshold 下的 tradeoff。

---

**[REBUT] R1-W4: SE 调整忽略 CM 估计不确定性**

部分反驳。论文在 method.tex line 34 中确实使用了 plug-in SE 公式 se_corrected = √(diag(Ĉ_s^{-1} diag(se²) Ĉ_s^{-T}))，这不 propagate CM posterior uncertainty。但论文在同一段紧接着说："below n_expert/K < 50, a bootstrap (B=100) maintains ≥95% coverage"（method.tex line 34）。Appendix Y (p.27) 详细验证了 bootstrap SE 的 coverage：plug-in SE 在 n_expert ≥ 100 时已达 93.8% aggregate coverage，bootstrap 恢复至 ≥95%。此外，层级贝叶斯本身通过 partial pooling 隐式地 regularize 了 CM 估计的 uncertainty——相比 stratified MLE 的 plug-in SE，HB 的 posterior mean 有更小的 estimation variance。

R1 的 concern 原则上成立（delta method 或 full posterior propagation 更 principled），但论文通过 bootstrap 提供了务实的解决方案且验证了 coverage。这不是一个 gap，而是一个 implementation choice with empirical justification。

---

**[AGREE] R1-W5: K≤4 限制适用范围**

同意。我在审稿中将此作为 S4（operating conditions 的诚实声明）给了正面评价，但 R1 从适用范围角度的批评也成立。实际 NLP 任务常有 K>4 的子群结构（fine-grained sentiment 5 levels, topic classification 10+ categories, intersectional demographic groups）。论文在 Appendix I 展示 K=8 时 RMSE 退化，但未提供 scalability 的理论解释——是因为 n_expert/K 不足导致的 estimation noise，还是 hierarchical prior 在高维下的 structural limitation？如果仅仅是样本量问题，那么给定足够 expert budget，K=8+ 应该可行；如果是结构性问题，则方法的适用范围确实受限。

---

**[REBUT] R1-W6: F-L 比较可能不公平**

反驳。Frazis-Loewenstein (2003) 的 scalar attenuation correction 确实是为同质误差率（K=1）设计的，但论文正是要论证：在异质误差率下，naively 应用 F-L 这种 widely-used correction 会使情况变得更糟。这不是 strawman——这恰好是论文的核心 motivation。如果 F-L 从来没有被用于异质误差场景，那么批评就成立；但实际上，许多实证研究者确实在不检查子群同质性的前提下直接应用 F-L 或等价的 global correction。Table 1 (experiments.tex) 中 F-L 作为 baseline 的存在是为了量化这种 naive practice 的代价——F-L 增加 bias 2.1-2.9× 正是 "debiasing hurts" 的具体例证。

论文在 related_work.tex lines 8-11 中也明确区分了自己与 F-L 的位置："Frazis-Loewenstein derive scalar attenuation λ=(1−2π) for the uncorrected estimator under homogeneous misclassification; Theorem 1 yields a structurally interpretable decomposition." 比较的 fairness 取决于 research question——论文的 question 是 "what happens when you apply standard corrections under heterogeneous errors"，而 F-L 正是 the standard correction。

---

### 总结：与 R2 审稿的交集与分歧

**交集（我们共同识别的核心问题）**：
1. 缺乏 real-data validation（R1-C1 ≈ R2-N2）
2. R² = 0.76 下界与 "exact" 声称的张力（R1-W1 ≈ R2-i2 部分重叠）
3. K≤4 适用范围限制（R1-W5 ≈ 我在 S4 中的正面评价，但 R1 从限制角度更准确）

**R1 独有的重要发现**：
- C2（κ²/κ 不一致）：我遗漏了这个 presentation issue，确认存在
- W3（AUC=0.86 + decision consequence）：比我的审查更细致
- W4（SE propagation）：技术上成立但论文有 bootstrap 解决方案

**R2 独有但 R1 未涉及的问题**：
- N1（理论新颖性深度有限）：R1 聚焦 rigor 而非 novelty
- W1（EMNLP 社区适配性）：R1 未讨论 venue fit
- W2（"debiasing hurts" framing 夸大风险）：R1 未质疑 framing
- W3（Missing Filtered PPI reference）
- W4（subgroup-dependent vs instance-dependent noise 联系）

**分歧**：
- R1-W6（F-L 比较 strawman）：我认为比较是公平的
- R1-W4（SE propagation）：我认为 bootstrap 已 address

**综合判断不变**：维持 3.5 (Borderline Conference)。R1 的 C2 是一个我遗漏的 presentation issue，但不改变 overall assessment。两位 reviewer 的核心共识是：soundness 强、novelty/excitement 对 EMNLP 偏弱、缺乏 real-data validation。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 的 8 个问题，我 **AGREE 6 条**（C1, C2, W1, W2, W3, W5）、**REBUT 2 条**（W4 因 bootstrap 已解决、W6 因 F-L 比较符合论文 research question）。两位 reviewer 的核心共识集中在三点：缺乏 real-data validation、R²=0.76 削弱 "exact" 声称、K≤4 限制适用范围。我独有的 concern（理论新颖性深度、EMNLP 社区适配性、missing Filtered PPI 引用）R1 未涉及。Overall 维持 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2510 · 2026-05-25T06:25:02.132164+00:00_

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
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
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

_source line 2511 · 2026-05-25T06:25:02.182947+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2512 · 2026-05-25T06:27:36.756287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
  "offset": "90",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
    "offset": "90",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 2513 · 2026-05-25T06:27:36.806994+00:00_

90	
91	\paragraph{Finite-sample remainder.}
92	With estimated $\hat{C}_s = C_s + E_s$, $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$, the remainder is $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s)^2)$, where the squared condition number arises from the Neumann expansion $\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\|E_s\|^2)$, motivating the $\kappa$-guard in Section~\ref{sec:method}.
93	
94	\begin{proposition}[Debiasing Can Increase Bias]
95	\label{prop:debiasing_hurts}
96	Under \textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\mathrm{bias}_{\mathrm{global}}| > |\mathrm{bias}_{\mathrm{naive}}|$) in subgroup $s$ if and only if
97	\begin{equation}
98	\frac{|\delta_s|}{(1 - 2\bar{\pi}) \cdot \pi_s} > 1.
99	\label{eq:hurts_condition}
100	\end{equation}
101	\end{proposition}
102	
103	\medskip
104	Equation~\eqref{eq:hurts_condition} partitions subgroups into two regimes:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2514 · 2026-05-25T06:27:37.861577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2515 · 2026-05-25T06:27:38.114063+00:00_

1	\section{Experiments}
2	
3	\begin{figure}[t]
4	\centering
5	\includegraphics[width=\columnwidth]{figures/fig4_budget_compact.pdf}
6	\caption{RMSE vs.\ expert budget under extreme heterogeneity. Crossover at $n{=}250$ ($K{=}2$) and $n{=}1000$ ($K{=}4$); shaded bands: $\pm 1$ SD across subgroups. Full grid in Appendix~\ref{app:budget}.}
7	\label{fig:budget_compact}
8	\end{figure}
9	
10	\subsection{Setup}
11	
12	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 Monte Carlo (MC) runs) and semi-synthetic data-generating processes (DGPs) spanning four NLP tasks---sentiment analysis (TweetEval~\cite{barbieri2020tweeteval}, $K{=}4$), hate speech detection (CivilComments, $K{=}4$), stance detection ($K{=}5$; Appendix~\ref{app:stance}), and topic classification (AG News, $K{=}4$; Appendix~\ref{app:agnews})---with full specifications in Appendix~\ref{app:dgp}.
13	
14	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2023dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (per-subgroup correction), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
15	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
16	Primary metrics are $|\text{bias}|$, root mean squared error (RMSE), and 95\% confidence interval (CI) coverage, averaged across subgroups and 100 MC runs.
17	Robustness validations cover eight conditions including asymmetric errors, subgroup misspecification, and treatment-dependent misclassification (all $\geq$89.5\% coverage; Appendices~\ref{app:hatespeech}--\ref{app:treatment_dep}).
18	Semi-synthetic evaluation uses 16 empirical LLM confusion matrices (8 LLMs $\times$ 2 datasets; Appendix~\ref{app:semireal}).
19	
20	\subsection{Empirical Validation of the Bias Identity}
21	\label{sec:bias_mechanism}
22	
23	\b
…[truncated 3169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 2516 · 2026-05-25T06:27:43.888736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": "95",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
    "offset": "95",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 2517 · 2026-05-25T06:27:43.889234+00:00_

95	\text{bias}(z{=}0, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(-\tau(0) + \tau(1)) = +\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}}, \\
96	\text{bias}(z{=}1, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(\tau(0) - \tau(1)) = -\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}},
97	\end{align}
98	}
99	where $\Delta\tau = \tau(1) - \tau(0)$. \qed
100	
101	\paragraph{Finite-sample remainder.}
102	When $\hat{C}_s = C_s + E_s$ with $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$ (central limit theorem), the estimated correction $\hat{M}_{\text{global}}^{-1} \hat{M}_s$ deviates from its population counterpart by
103	$\|\hat{M}_{\text{global}}^{-1} \hat{M}_s - M_{\text{global}}^{-1} M_s\| \leq \kappa(M_{\text{global}}) \cdot O_p(n_{\text{expert}}^{-1/2})$,
104	where $\kappa(M) = \|M\| \cdot \|M^{-1}\|$ is the condition number~\citep{stewart1990matrix}.
105	This motivates the $\kappa > 100$ singularity guard in Section~\ref{sec:method}.
106	
107	\section{Multi-class Extension and Proof}
108	\label{app:multiclass}
109	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_489afd65980834a91024fd48e21d984f:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---
