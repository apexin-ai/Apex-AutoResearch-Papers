---
round: 23
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T19:59:54.087083+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 23 (Fresh)

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR Long Paper)
**Deadline**: 2026-05-25

---

## Summary

论文研究 reasoning model 中 hidden-state (HS) safety probe 的 layer selection sensitivity。在 4 个模型（R1-8B/Llama, OT-7B/Qwen, QwQ-32B/Qwen, R1-32B/Qwen）和 HarmThoughts 数据集上实验，发现 crossing-rate composite metric 系统性选择 shallow layers 而 threshold-based metrics 选择 deep layers，且这一选择差异可完全逆转 HS vs. text probe 的模态优势结论。论文定义了 Safety Commitment Point (CP)，报告了 7 种替代方法的 negative results，并提供了大量 ablation 分析（31 页附录）。

---

## Strengths

**S1. 统计方法论在 NLP probing 论文中属上乘水平。** BCa bootstrap（10,000 resamples）+ Holm-Bonferroni correction（12 tests）+ exact sign-flip permutation tests（exhaustive 2^n enumeration）三层验证体系严谨。[R1, R2 一致]

**S2. Bug Disclosure 和科学透明度极高。** Appendix N 主动披露 QwQ-32B text probe bug 及其影响；7 种替代方法（BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-model transfer）的系统性失败诚实报告，避免 publication bias。[R1, R2 一致]

**S3. 实验覆盖全面。** 31 页附录涵盖 layer sweep、window ablation、encoder robustness、random projection、LLM-based encoder、cross-model transfer、GRU variants、two-stage detection、multi-metric ensemble 等，远超同类论文标准。[R1, R2 一致]

**S4. 核心发现确有实践价值。** 同一数据在 CR-composite layer 上给出 p=0.83（不显著），在 threshold-based layer 上给出 p<0.005（显著），这一逆转效应对依赖单一 metric 做 layer selection 的研究者有直接警示价值。[R1, R2 一致]

**S5. 因果推理尝试有层次。** Position residualization、random-label control、random projection baseline、control task selectivity、split-half internal validity——从不同角度排除混淆变量。[R1]

---

## Weaknesses

### Critical（影响接收决定）

**C1. 32B 模型样本量严重不足，但 Contribution 1 依赖其 reversal 证据。** [R1-N1; R2 AGREE]
- Test set n=19-20，validation set ~4 traces/class，超参选择近似随机
- Bootstrap CI 过宽（MDE 8.6-9.5pp, Appendix Z.2）
- 论文标记 32B 为 "exploratory"，但 C1 的核心论证（"Had we reported only CR-composite-layer results, we would have concluded a scale-dependent HS advantage..."）恰恰依赖 32B 的 underpowered reversal
- **建议**：降级 32B 为 "illustrative"；在主文展示 power analysis；增加 32B 数据量或用 LOO

**C2. 架构多样性不足以支撑 "cross-architecture" 声明。** [R1-N2; R2 AGREE]
- 3/4 模型为 Qwen 架构，仅 R1-8B (Llama) 提供 cross-architecture evidence
- 无法排除 crossing-rate shallow-layer bias 是 Qwen-specific（如 embedding normalization、attention pattern）
- **建议**：修正措辞为 "two architecture families"；讨论 Qwen-specific 可能性；补充非 Qwen/Llama 架构验证

**C3. 核心贡献与 probing 领域已有认知的区分不够清晰。** [R2-N1; R1 AGREE with nuance]
- Belinkov (2022) survey 已指出 probing 对 layer/metric/complexity 敏感
- 论文本质上是在 safety probes 上 demonstrate 已知问题
- **R1 补充 nuance**：本文的具体贡献在于展示 crossing-rate vs. threshold-based 的 **系统性方向偏差**（总是 shallow vs. deep），且由 representation geometry 驱动——这超越了 Belinkov 讨论的 general sensitivity，但论文未清晰区分
- **建议**：明确 frame 为 "known sensitivity → new directional systematicity"

**C4. 未提出原则性解决方案。** [R2-N3; R1 AGREE]
- Multi-metric ensemble (Appendix Z.1) 的 Ens-Best 差异全部不显著（p>0.27）
- Section 5 的 "multi-metric audit protocol" 缺乏具体 decision criteria
- **建议**：将 Z.1 提升到主文；发展 actionable decision criteria；测试 learned weighting

**C5. 单数据集限制所有核心 claims。** [R1-N7, R2-N2; 双方一致]
- 所有实验仅在 HarmThoughts 上进行
- AdvBench 有 388 traces 但未用于验证 layer selection reversal
- **建议**：至少在 AdvBench 上验证 crossing-rate bias 是否 reproduce

### Warning（影响评分但非否决）

**W1. QwQ-32B HS 优势在 quadratic position residualization 后完全消失。** [R1-N4; R2 AGREE]
- Table 29: quadratic control 下 -1.0pp，暗示 HS probe 可能主要是 position detector
- R1-8B/OT-7B 不受影响（位置伪影是 QwQ-32B specific）
- Abstract 和 Discussion 未充分反映严重性
- **建议**：Discussion 中更显著报告；讨论对 C2 的影响

**W2. R1-32B control task selectivity 仅 3.0pp，低于 Hewitt 5pp 阈值。** [R1-N5; R2 AGREE]
- 结合 n=20 和 position confound，R1-32B 全部结论高度可疑
- **建议**：标注为 "inconclusive" 而非 "exploratory"

**W3. CP binary formulation 过于粗糙。** [R2-W1; R1 AGREE]
- Oscillating traces 可能被 misclassified
- Section 9 承认但未量化 oscillating traces 比例和 error rate
- **建议**：量化 oscillating traces 比例；考虑 soft CP robustness check

**W4. Abstract 信息过载。** [R2-W3; R1 AGREE]
- ~190 词塞入过多具体数字，牺牲可读性
- **建议**：减少数字，聚焦 conceptual contribution

**W5. Negative results 失败分析深度不足。** [R2-W5; R1 AGREE]
- 7 种方法失败原因各仅 1-2 句描述性观察
- **建议**：至少对 BOCPD 和 RepE 做更深入的 failure analysis

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下问题上完全一致：
1. **单数据集限制**（C5）：所有核心 claims 仅 HarmThoughts 验证，AdvBench 可用但未用
2. **Novelty 边界模糊**（C3）：与 Belinkov (2022) 已有认知的区分不够清晰
3. **缺少 actionable solution**（C4）：ensemble 不显著优于 best single metric
4. **32B underpowered**（C1）：n=19-20 不足以承载 main contribution 的论证
5. **架构多样性**（C2）：3/4 Qwen 使 cross-architecture claim 过度
6. **统计严谨性是核心亮点**（S1）：HB + bootstrap + permutation test 三层验证属上乘
7. **Overall 3.0 (Findings)**：贡献真实但 incremental，scope 和 novelty 受限

---

## Reviewer Divergence [REBUT]

| 问题 | R1 | R2 | 判定 |
|------|-----|-----|------|
| R1-N3: Upstream multiple testing 严重低估 | Critical | Partial rebut（nested CV + standard split 已部分缓解） | **R2 更准确**：7-8B 有 nested CV 保护，但 32B 缺乏验证仍是问题 |
| R1-N6: Crossing-rate shallow bias trivially expected | Warning | Partial rebut（causal chain 的 empirical demonstration 有价值） | **R2 更准确**：individual steps 可能 known，但完整链条的量化不 trivial；论文需更好 frame |
| R2-W2: Section 编号 5→7 | — | Should-Fix | **R1 更准确**：降级为 typo |
| R2-W4: "Retrospective" 反复强调削弱 impact | Rebut（scope discipline 是 strength） | Warning | **分歧保留**：R1 认为 scope discipline 负责任，R2 认为过度 hedging 削弱 impact。建议在 Intro 一次声明 scope 后，后续正面表述 retrospective 价值 |

---

## Questions（需作者澄清）

**Q1.** [R1-Q1, R2 AGREE] QwQ-32B 的 quadratic residualization 完全吸收了 HS 优势（Table 29: -1.0pp）。这是否意味着 QwQ-32B 的 HS probe 本质上是 position detector？Contribution 2 的 "doubly conditional" framing 是否需要修正？

**Q2.** [R1-Q2, R2 AGREE] Nested 5-fold CV 为什么没在 32B 上执行？n=95 做 5-fold 给出 ~76 train / 19 test per fold，与现有 holdout 规模相当。真正障碍是什么？

**Q3.** [R1-Q3, R2 REBUT] Random-label control 中 100% 选 shallow layers 是否只因 shallow layers 更 noisy？R2 反驳：若 noise 解释成立，threshold-based metrics 也应 prefer shallow layers，但 Table 2 显示相反——threshold-based 一致选 deep layers。R2 反驳更有说服力。

**Q4.** [R1-Q4, R2 AGREE] HarmThoughts CP annotation 无 IAA。能否量化 CP position 与 chain length 相关性以评估 systematic bias 风险？

**Q5.** [R1-Q5, R2 AGREE] Multi-metric ensemble Ens-Best 不显著（p>0.27），其作为 "solution" 的实用价值有多大？是否尝试过 learned weighting？

**Q6.** [R2-Q2] AdvBench 上是否也观察到了 layer selection reversal phenomenon？若是，将显著加强 generalizability claim。

**Q7.** [R2-Q4] Oscillating traces 的 binary CP false positive/negative rate 是多少？

---

## Missing References

### R1 建议（R2 认为均非 must-cite）
1. Nanda et al. (2023), "Progress Measures for Grokking via Mechanistic Interpretability"
2. Gurnee et al. (2023), "Finding Neurons in a Haystack"
3. Li et al. (2024), "The Geometry of Categorical and Hierarchical Concepts in LLMs"

### R2 建议（可能 concurrent）
1. "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (arXiv 2605.18549, May 2026) — 与 temporal probe analysis 高度相关
2. "Truth as a Trajectory" (arXiv 2603.01326, March 2026) — layerwise trajectory 分析
3. "Reasoning Models Know When They're Right" (arXiv 2504.05419, April 2025) — reasoning model probing methodology

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Visual Layout Check（非评分项）

**状态**：已完成（耗时 ~3 分钟）

**4 个 Warning**：
1. **Pages 3-5 文字墙**：连续 3 页纯文本无 display item（Related Work + Methods + Evaluation），审稿人翻到第 5 页仍未见实验图表
2. **Figure 1 延迟到 Page 6**：前 5 页仅有 Table 1（4 行小表），第一印象偏 text-heavy
3. **Page 9 全文字**：Discussion 续写 + caveats，主文最后一页缺视觉收束
4. **Display item 密度偏低**：主文 8 页仅 2 figures + 4 tables = 6 items（同类论文通常 7-10 个）

**8 个 Info**：Figure 1 子图字号偏小、颜色映射含义不直观；Figure 2 清晰可读；Tables 遵循 booktabs；Tables 3-4 缺 bold 标注最优值；末页空白；References 排版正常；无 LaTeX 渲染错误。

---

## Overall Assessment

**Overall Score**: 3.0 (Findings)
**Confidence**: 4/5

### 评分理由

| 维度 | 分数 | 说明 |
|------|------|------|
| Soundness | 3.5/5 | 统计框架扎实，但 32B underpowered + position confound 削弱部分 claims |
| Excitement | 2.5/5 | 方法论警示有价值，但本质 incremental（已知问题在新 domain 上 demonstrate）且缺 solution |
| Reproducibility | 4.0/5 | 承诺代码开源，超参完整，但 HarmThoughts CP annotation 缺 IAA |

**判断**：论文识别了一个真实的方法论问题（metric-induced layer selection bias），统计处理在同领域论文中属上乘，negative results 和 bug disclosure 展现了高度科学诚信。但以下问题限制其 impact 至 Findings 级别：
1. 核心贡献（layer selection sensitivity）与 probing 领域已有认知（Belinkov 2022）的区分度不够
2. 32B reversal evidence underpowered（n=19-20），但 C1 论证依赖此
3. 3/4 Qwen 架构使 cross-architecture claim 过度
4. 单数据集（HarmThoughts）限制所有核心 claims
5. 缺乏 actionable solution

**升级条件（→ 3.5 Borderline Conference）**：
- 修正 framing（降低 32B 权重，明确 "two architectures"）
- 在 AdvBench 上验证 layer selection reversal
- 将 multi-metric audit protocol 发展为 actionable decision criteria 并放入主文
- 更清晰地区分 "known sensitivity" vs "new directional systematicity"

---

## Detailed Comments

### Section 1 (Introduction)
- 叙事结构清晰但 hedging 偏多（"initial characterization"、"retrospective" 反复出现）
- "four reasoning LLMs" 和 "cross-architecture" 措辞暗示了超出实际的架构多样性
- Table 1 放在 Introduction 末尾是好的设计选择

### Section 2 (Related Work)
- 覆盖全面（78 条引用），concurrent work (chan2025probing) 区分到位
- 建议检查 R2 提出的 3 篇 2025-2026 concurrent work

### Section 3 (Methods)
- Layer selection sensitivity 分析框架设计良好（5 metrics, threshold vs CR-composite taxonomy）
- Evaluation protocol 的 metric 排除理由（F1, AUROC, MCC）有据
- K=5 的选择和 cross-model fixed 的设计合理

### Section 4 (Experiments)
- Evidence gradient (cross-validated → significant → exploratory) 是好的分层呈现
- Table 2 (layer selection) 是论文最有力的证据
- Table 3 (HS vs text) 信息密度高但可读性尚可
- 32B analysis (Section 4.4) 篇幅适当但 power limitation 应更显著标注
- Negative results (Section 4.6) 诚实但分析深度不足

### Section 5 (Discussion)
- "Researcher degree of freedom" framing 有学术价值
- Encoder-quality boundary 和 guidance for future research 段落有用
- Multi-metric audit protocol 过于宽泛

### Section 6/7 (Conclusion / Limitations)
- Section 编号从 5 跳到 7（minor typo）
- Conclusion 过于简短（3 行）
- Limitations section 极其诚实和全面——这是论文的一个 hidden strength

### Appendix
- 覆盖面极广（40 张表、5 张图）
- Nested CV (W.1)、multi-seed (X)、split-half (X.1) 提供了强 robustness evidence
- 建议将 nested CV 和 power analysis 的关键数字提升到主文