---
round: 24
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T12:40:17.846022+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models

**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)
**Reviewers**: R1 (方法严谨性 + 统计有效性), R2 (新颖性 + framing + Related Work)
**审稿轮次**: Round 24 (fresh review)
**Review Director 合成日期**: 2026-05-21

---

## Summary

本文研究推理模型中 hidden-state (HS) 安全探针的层选择敏感性问题。作者定义了 Safety Commitment Point (CP)——推理链中安全审议永久终止的第一步，并在 HarmThoughts 基准上评估 4 个推理 LLM（1 个 Llama, 3 个 Qwen）的 HS vs. text 探针 CP 检测能力。核心发现是方法论性的：crossing-rate composite metric 系统性选择浅层（所有模型），threshold-based metrics 收敛于深层——同一数据可从 +19pp significant (p<0.005) 翻转为 non-significant (p=0.83)。论文进一步展示 HS 优势是"doubly conditional"的（依赖编码器质量和 position 控制），并系统评估了 7 种替代方法均失败。

---

## Strengths

**S1. 方法论发现具有实践警示价值。** [R1 AGREE, R2 AGREE] 层选择 metric 可逆转 safety probe 结论的演示——QwQ-32B 在 CR-composite 层 p=0.83、threshold-based 层 p<0.005——对 hidden-state safety monitoring 社区有直接指导意义。这一发现虽建立在 probing 文献已知的层选择敏感性之上（Belinkov 2022），但在安全领域的定量严重程度和 crossing-rate × cosine compression 的机制分析是新的。

**S2. 7-8B 模型统计框架严谨。** [R1, R2 consensus] Nested 5-fold CV + BCa bootstrap + Holm-Bonferroni 组合设计恰当，正确报告了 13-25% validation→holdout shrinkage。Control task selectivity (11.1-16.8pp)、random-label decomposition、position residualization 构成了多层证据链。

**S3. 控制实验设计突出。** [R1, R2 consensus] Random-label control 尤为有说服力：QwQ-32B 随机标签下 crossing-rate 100% 选择相同浅层（证实几何伪影），R1-8B 呈标签依赖散布（证实机制差异跨架构）。

**S4. 报告透明度高。** [R1, R2 consensus] Bug disclosure (Section N) 罕见且值得赞赏。Negative results 的系统报告 (7 methods, Table 24) 有效对冲 p-hacking 嫌疑。附录 20 页覆盖 layer sweep、window ablation、threshold sensitivity、power analysis 等——对潜在审稿质疑的系统性预防。

**S5. Negative results 系统性有价值。** [R2 强调, R1 同意] BOCPD/CUSUM/Mahalanobis/RepE/MLP/CCS/cross-transfer 的失败不是简单堆砌，每种有明确动机和失败原因分析，定义了方法边界。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. 多重比较校正范围与搜索空间严重不匹配。** [R1 raised, R2 agrees with nuance]
- Holm-Bonferroni 仅覆盖 12 个最终测试（4 models × 3 metrics），但实际搜索空间涵盖 ~2,240 配置（5 metrics × 7 windows × 25-64 layers）。K=5 阈值、metric taxonomy、window 大小均从该空间中选定。
- R2 补充 nuance：nested CV 从结构上控制了 layer/window 选择（ML 标准做法），真正的 researcher degrees of freedom 是 metric taxonomy 定义和 K=5 选择。
- **共识修复路径**：(a) 定量论证（permutation-based global null 或有效独立测试数估计）；或 (b) 将核心论点改为 "direction of effect is robust" 而非依赖具体 p-values + 强调 effect sizes。
- *Section 3.5, W.1*

**N2. 32B 模型结论基于严重欠功效的数据。** [R1 raised, R2 raised independently, full consensus]
- n=19-20, MDE=8.6-9.5pp (80% power)。R1-32B HS advantage (+1.9pp) 远低于 MDE，p=0.83 无法区分"无效应"与"功效不足"。
- R2 补充关键观察："doubly conditional" 概念严重依赖 32B non-significance，但该 non-significance 可能纯粹是 underpowering 的结果。
- 32B 占 2/4 模型——折扣后仅剩 2 个 7-8B 模型（1 Llama + 1 Qwen）支撑泛化性。
- **共识修复路径**：标记所有 32B 结论为 "underpowered and provisional"，与 7-8B 结论明确分级表述；Table 4 caption 显著标注。
- *Section 4.4, Table 4, Section Z*

**N3. 架构多样性不足削弱泛化性声明。** [R2 raised critical, R1 rebuts severity but agrees hedging needed]
- 4 个模型中 3 个为 Qwen 架构，仅 R1-8B 为 Llama。R1 在交叉回应中误将 OT-7B 归为 Llama-family（实际为 Qwen，见 Table 1），高估了跨架构证据强度。
- **R1 有效反驳**：核心现象（metric choice 影响 layer selection）已在 Llama R1-8B 上验证——CR-composite 同样选择 L0，threshold-based 选择 L14，分歧跨架构存在。
- **R2 有效坚持**：geometric bias 机制是 Qwen-specific（random-label control 证实），3 个 contributions 中的 mechanism 分析泛化性不足。
- **Director 裁定**：现象跨架构验证（should-fix level），但 Abstract/Intro 需明确注明 "primarily Qwen-based (3/4 models)" 并区分现象 vs. 机制的泛化边界。
- *Table 1, Abstract, Section 5, Limitations*

### Should-Fix（影响评分但不一票否决）

**W1. C1 新颖性定位需更诚实。** [R2 raised, R1 agrees]
- 层选择影响 probing 结果是 Belinkov (2022) 等已讨论的方法论关切。Introduction C1 应明确承认已知性，聚焦安全领域的定量发现和 cosine compression × crossing-rate 机制分析作为新颖性所在。
- *Section 1 contributions list, Section 5 Discussion*

**W2. 单一 benchmark 限制 generalizability。** [R1 raised, R2 agrees]
- 所有主要实验使用 HarmThoughts。AdvBench 验证仅覆盖几何前提条件（cosine volatility 1.67×），未复现完整 layer selection sensitivity finding。核心发现（metric reversal）仅在一个数据集上展示。
- *Section 4.1, Limitations*

**W3. AUROC 排除理由有循环论证嫌疑。** [R1 raised, R2 agrees]
- 排除理由"threshold-free, cannot diagnose layer selection bias"——但 taxonomy 本身围绕 threshold-based metrics 定义。AUROC 作为 reference metric 可低成本地独立验证 taxonomy 有效性。
- *Section 3.5*

**W4. CP 标注可靠性讨论不充分。** [R1 raised, R2 agrees]
- LLM annotator 间 CP 位置 mean abs diff = 8.5 steps。Section J.1 称"supports robustness assumption"的逻辑跳跃不清晰。建议 CP ±3 步 perturbation sensitivity analysis。
- *Section J.1*

**W5. Ensemble 方案 (Section Z.1) 不成熟。** [R1 raised, R2 agrees]
- 简单平均策略缺乏理论动机和失败模式分析。应发展为正式 contribution 或降级为 preliminary observation。
- *Section Z.1*

**W6. C2 "doubly conditional" 贡献定位模糊。** [R2 raised, R1 partially rebuts]
- R2 认为是观察总结而非方法论贡献；R1 反驳称提供了可独立验证的 failure mode 分析框架。建议改为 "empirical characterization of necessary conditions for HS advantage"。
- *Abstract, Section 1 C2*

**W7. Chan & Yong (2025) bib 标题错误。** [R2 raised critical, R1 agrees but downgrades]
- `chan2025probing` bib 标题与 arXiv:2507.12428 实际标题不匹配。R1 正确指出这是 editorial error 不影响结论，但对论文反复引用的关键 concurrent work 标题错误是审稿中的严重质量问题。需修正标题并补充第三作者 Bach。
- *References*

### Minor Issues（不影响接收）

- **M1**: 3 个 orphan bib entries 未被引用（bansal2021stitching, kornblith2019cka, li2024iti），应清理。[R1, R2 consensus]
- **M2**: Figure 2 图例部分遮挡数据区域，建议 bbox_to_anchor 放置于图外。[R2 raised, R1 agrees]
- **M3**: "Doubly conditional" 在 p2 首次出现时未即时定义。[R1 raised]
- **M4**: Figure 1 heatmap 字号偏小，可读性可改善。[R1 raised]
- **M5**: Discussion (Section 5) 在 p8 极度压缩，可读性受影响。[R1 raised]
- **M6**: Table 1 caption "step-level CP annotations" 可对不熟悉读者增加说明。[R1 raised]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致 [AGREE]：
1. 32B 统计功效不足是 critical issue（R1-N2 = R2-W4）
2. 7-8B 实验设计严谨，controls 全面且有说服力
3. Bug disclosure 值得赞赏，增强可信度
4. Orphan bib entries 应清理
5. Ensemble 方案不成熟，需发展或降级
6. C1 应更诚实地承认 Belinkov (2022) 已知性
7. 单一 benchmark 限制 generalizability
8. AUROC 排除理由循环
9. CP 标注可靠性讨论逻辑不清晰
10. Chan & Yong 标题错误需修正（严重程度有分歧）

---

## Reviewer Divergence

**D1. 架构多样性问题的严重程度。**
- R2：Critical — 3/4 Qwen 使核心 contributions 泛化性存疑。
- R1：Should-fix — 核心现象（metric reversal）已在 Llama R1-8B 上验证。
- R2 事实纠正：R1 误将 OT-7B 归为 Llama-family，实际为 Qwen。这强化了 R2 的关切。
- **Director 裁定**：R2 的事实基础更准确。现象层面有跨架构支撑（R1-8B），但机制层面（geometric bias Qwen-specific）泛化性不足。Abstract/Intro 需加 hedging，严重程度介于两者之间（strong should-fix）。

**D2. Novelty / Excitement 评估。**
- R1：Excitement 3.0 — metric-specific mechanism 识别和 modality comparison 翻转的定量发现超出简单 domain application。
- R2：Excitement 2.5 — 层选择敏感性是已知现象，domain-specific 应用 incremental。
- **Director 裁定**：倾向 R2。cosine compression × crossing-rate 的机制分析确有增量新颖性，但 conceptual contribution 不足以达到 Main conference (4.0) 标准。安全领域的定量展示有实践价值，更适合 Findings。

**D3. Chan & Yong 标题错误严重程度。**
- R2：Critical — 关键 concurrent work 标题错误影响审稿人验证。
- R1：Should-fix — editorial error，不影响实验结论。
- **Director 裁定**：Should-fix（warning）。标题错误需修正，但不构成接收决定的阻碍。

**D4. 缺失引用 arXiv:2601.13288。**
- R2：必须补充 — 直接研究 LLM layer selection for probing。
- R1：持保留态度 — 无法独立验证，ARR H13 不应要求特定引用。
- **Director 裁定**：建议验证并考虑引用，但不列为 must-fix。

**D5. Overall 评分。**
- R1：3.5 (Borderline Conference)
- R2：3.0 (Findings)

---

## Questions（需要作者澄清）

1. **多重比较**：若对 ~2,240 配置搜索空间（而非仅 12 tests）施加 Bonferroni 校正，或估计有效独立测试数，当前显著结果中有多少能存活？
2. **CP 标注鲁棒性**：是否测试过 CP 标签偏移 ±3 步后主要发现的鲁棒性？
3. **AUROC layer selection**：AUROC-based selection 选择哪些层？与 threshold-based 还是 crossing-rate 对齐？
4. **因果方向**：浅层是否可能确实在检测不同的 safety signal，而非纯粹是几何伪影？R1-8B 上 random labels 不选择相同浅层暗示部分信号依赖。
5. **Non-reasoning models**：layer selection sensitivity 是否预期对标准 instruction-tuned LLMs 同样成立？

---

## Missing References

1. **[建议验证]** arXiv:2601.13288 "A BERTology View of LLM Orchestrations: Token- and Layer-Selective Probes" — R2 建议，R1 存疑
2. **[修正]** Chan & Yong (2025) bib 标题需修正为 arXiv:2507.12428 实际标题
3. **[可选]** Vig et al. (2020) "Causal Mediation Analysis for Interpreting Neural NLP" — R1 建议
4. **[清理]** 3 个 orphan bib entries

---

## External Review (Stanford Agentic Reviewer)

**状态**: 已跳过（用户未提交）

---

## Visual Layout Check（非评分项）

**状态**: 完成（3 warnings, 10 info）

**主要发现**:
- **[warning]** Pages 3-5 连续约 3 页无 display item（Related Work → Methods 全为纯文本），审稿人翻到 p6 才看到第一个实验结果图表
- **[warning]** 前 3 页缺少传达核心 message 的视觉锚点，Table 1 (p2) 仅是模型概况表
- **[warning]** Display items 分布不均：p1-5 仅 1 表，p6-8 集中 3 表 + 2 图
- **[info]** 主体 8 页 6 个 display items（2 figure + 4 table），在可接受下限
- **[info]** Figure 1/2 质量良好，booktabs 风格规范，无渲染错误
- **[info]** 全文排版专业，无 margin 溢出、LaTeX 错误、公式乱码

**视觉审查结论**：8 页预算极限下（已使用 enlargethispage），增加 display item 有溢出风险。前半部分文本密度偏高是结构性限制而非质量问题。

---

## Overall Assessment

**综合评分: 3.0 / 5 (Findings)**

**置信度**: 4/5

**评分依据**:

本文提供了对 hidden-state safety probing 中层选择敏感性的有价值的实证警示，实验设计严谨程度远超该领域同类工作（nested CV、random-label controls、position residualization、Holm-Bonferroni corrections）。核心演示——同一数据在不同 metric 下 HS 优势从 +19pp significant 翻转为 non-significant——对快速增长的 hidden-state safety monitoring 方向有直接实践指导意义。附录深度和广度突出（20 页），negative results 系统性有方法论贡献。

但以下因素限制了 Main conference (4.0) 评分：

1. **Novelty 有上限**：层选择影响 probing 是已知方法论关切 (Belinkov 2022)。本文贡献在于安全领域的定量展示和 cosine compression × crossing-rate 机制分析——实践价值高但 conceptual novelty incremental。
2. **架构覆盖窄**：3/4 模型为 Qwen，仅 1 个 Llama 提供跨架构证据。geometric bias 已确认 Qwen-specific，机制泛化性不足。
3. **32B 严重欠功效**：n=19-20, MDE=8.6-9.5pp。"doubly conditional" 概念依赖 32B non-significance，但这可能是纯 underpowering 的结果。去除 32B 后仅剩 2 个 7-8B 模型支撑结论。
4. **单一数据集**：HarmThoughts 是唯一有 step-level CP 的公开数据集（客观限制），但核心 layer selection reversal 未在第二数据集复现。
5. **多重比较校正范围**：12 tests vs ~2,240 搜索空间的覆盖差距需定量回应或 p-value 声明弱化。

作为 Findings 论文，方法论贡献（层选择警示 + 控制实验范式）和实验深度完全达标。R1 给 3.5 (Borderline Conference) 的理由——mechanism identification 超出简单 domain application——有一定道理，但综合架构覆盖、数据集覆盖和 32B 功效问题，3.0 (Findings) 更准确。

---

## Detailed Comments（逐节）

**Abstract**: 信息密度高但已优化至 ~192 words。需加 "primarily Qwen-based" 架构分布说明。"Doubly conditional" 应在首次出现时有简要定义。

**Introduction**: C1 应先承认 Belinkov (2022) 已知性再定位安全领域新颖性。C2 改为 "empirical characterization of necessary conditions"。Table 1 caption 可增加 CP 说明。

**Related Work**: 覆盖全面，三个文献领域（safety reasoning, HS detection, probing methodology）均有深度。Chan & Yong (2025) 标题需修正。可考虑验证并添加 arXiv:2601.13288。

**Methods**: 5-metric taxonomy 清晰但 AUROC 排除理由需加强或补充 AUROC reference point。CP 定义清晰实用。Evaluation protocol 的 search space quantification 已有但需定量回应 multiple comparison concern。

**Experiments**: 7-8B 结果扎实。32B 分析需更显著的 exploratory 标记——当前 Table 4 的结论性语言与 underpowered 数据不匹配。Section 4.3 encoder robustness 和 position mediation 分析充分。

**Discussion**: 过度压缩（p8），核心观点需更多空间。Layer selection 作为 researcher degree of freedom 的讨论有价值。

**Conclusion**: 简洁适当。

**Limitations**: 3 点覆盖（单数据集、32B 功效、架构覆盖），符合 EMNLP 要求。可加强 CP 标注 IAA 的限制讨论。

**格式**: 合规——8 页正文、double-blind、ACL template、Limitations/Ethics Statement 均存在。3 个 orphan bib entries 需清理。Figure 2 图例位置需调整。