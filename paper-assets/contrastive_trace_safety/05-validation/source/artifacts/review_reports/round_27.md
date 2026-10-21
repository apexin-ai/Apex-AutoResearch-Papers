---
round: 27
review_mode: continue
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T15:00:25.612293+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# Round 27 Consolidated Review Report
**Paper**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR Long Paper, deadline 2026-05-25)
**Reviewers**: R1 (统计严谨性 + 实验充分性), R2 (新颖性 + 叙事/方法论完整性)
**Mode**: Continue (Round 27, based on Round 26 findings)
**Note**: 论文在 Round 26 → Round 27 之间无任何修改（无新 commit、无未提交变更），本轮为验证性审稿。

---

## Summary

本文研究推理模型隐藏状态安全探针中的层选择敏感性问题。核心发现：选择层的度量标准（metric）可以逆转安全探针研究的核心结论——对 QwQ-32B，同一数据在不同 metric 下给出 p=0.83 或 p<0.005。论文提出 5-metric 分类法、识别出浅层余弦压缩机制、并发现隐藏状态（HS）优势对编码器质量和位置重叠存在双重条件依赖。实验涵盖 4 个推理模型（3 Qwen + 1 Llama），使用 HarmThoughts 数据集的 Safety Commitment Point (CP) 标注。统计框架包含 BCa bootstrap、Holm-Bonferroni 校正和 evidence gradient 三级分层。

---

## Strengths

**S1. 层选择敏感性的系统性揭示 [R1+R2 共识]**
5-metric 分类法清晰展示不同度量如何系统性地选择不同深度的层，cosine compression 机制解释了 crossing rate 偏向浅层的原因。这一发现对领域内所有基于层选择的 probe 研究具有方法论警示价值。

**S2. 统计框架严谨 [R1 主导]**
Two-stage 设计（2,240 配置探索 → 12 final HB-corrected tests）、BCa bootstrap（10K resamples, cluster-level）、evidence gradient 三级分层（cross-validated / significant / exploratory†）、Cohen's d 效应量——统计处理远超同领域平均水平。

**S3. 诚实的 Limitations 和 Negative Results [R1+R2 共识]**
Section 4.6 报告了 4 项 negative results（含 R1-32B 仅在 W=1 达到显著性、false positive rates 11-50%）。Limitations 明确承认单数据集、32B 统计功效不足、架构覆盖有限。这种坦诚在同类论文中罕见。

**S4. 写作密度与信息效率 [R2 主导]**
8 页主文承载了完整的方法 + 4 模型实验 + 消融 + negative results + discussion，信息密度高。23 页附录提供充分的细节支撑，附录引用路径清晰。

**S5. 实用建议 [R1+R2 共识]**
Multi-metric audit 准则（≥3 metrics 偏差 >20% depth → metric-dependent）和 three-layer ensemble（p≤0.002）提供了可操作的实践指导。

---

## Weaknesses

### Critical (阻止主会议接收)

**W-C1. Safety Commitment Point (CP) 标注质量不足 [R1-N2 + R2-N2 共识]**
CP 定义为"安全审议永久停止的首个推理步骤"，但验证仅依赖 LLM proxy 在 AdvBench 上的 κ=0.606（moderate agreement）。HarmThoughts 数据集本身无 IAA 报告。"永久停止"的判断在长 CoT 中存在歧义（安全考量可能在后续步骤以不同形式复现）。所有依赖 CP 的下游结论（temporal windowing、pre/post-CP 对比）的可靠性受此限制。
- **升级路径**: 在 HarmThoughts 子集上报告人工标注者 IAA（至少 50 traces × 2 annotators），或提供 CP 标注的 sensitivity analysis（±1 step 偏移对主要结论的影响）。

**W-C2. Metric × Layer 交互效应的因果归因不充分 [R2-N1, R1 部分同意]**
论文核心叙事从"metric 选择可逆转结论"出发，但未充分区分：(a) metric 确实引入了伪影（如 cosine compression）vs (b) 不同 metric 捕捉了不同的genuine信号维度。当前证据（cosine volatility 分析）支持 (a) 对 crossing rate 成立，但 precision/FPR 选择深层是否也是 metric artifact 尚无等价分析。叙事倾向于将所有 metric-layer 变异归因为"sensitivity problem"，但部分变异可能反映真实的层级功能分化。
- **升级路径**: 对 threshold-based metrics（precision, inverse FPR）提供类似 cosine compression 的机制分析，或明确标注哪些 metric-layer 关联是 artifact vs genuine。

### Major (显著影响评分)

**W-M1. 架构覆盖严重偏斜 [R1-W4 + R2-W3 共识]**
3/4 模型为 Qwen 架构，仅 R1-8B (Llama) 提供跨架构证据。Random-label controls 确认 crossing rate 几何偏差是 Qwen-specific 的。这意味着 Contribution 1（metric-induced bias）的跨架构推广性高度不确定。论文在 Limitations 中承认了这一点，但主文叙事中 "metric selection can reverse the central conclusion" 的表述未加架构限定。
- **建议**: 主文的 general claims 需添加架构限定语（如 "in Qwen-family models"），或在 Discussion 中更显著地标注跨架构风险。

**W-M2. Conclusion 混合已验证与探索性结论 [R1+R2 共识]**
Conclusion 中 "The HS advantage (+15-22pp against 384d encoders) is doubly conditional on encoder quality and position overlap" 未区分 7-8B（nested CV 验证）和 32B（n≤20, 探索性†）结果。Section 4.4 和 Limitations 正确标注了 † 级别，但 Conclusion 未保持一致。
- **建议**: Conclusion 中对 32B 结论保留 † 标记或明确限定为 "exploratory"。

**W-M3. 32B 结果的统计功效不足但占据大量篇幅 [R1-N2]**
n=19-20 traces, MDE 8.6-9.5pp (power analysis in appendix)。R1-32B 仅在 W=1 (25% coverage) 达到显著性，false positive rates 11-50%。然而 Table 4 和 Section 4.4 占据主文约 1/3 页，给读者的印象是这些结果比实际 evidence level 更可靠。
- **建议**: 压缩 32B 主文篇幅，或在 Table 4 caption 中更醒目地标注统计功效限制。

**W-M4. FWER 控制不完整 [R1-N1, R2 认为 Warning 级别]**
Stage 1 (2,240 configurations) 的选择过程引入了 pre-registration 问题：最终 12 tests 的选择基于 Stage 1 的结果，但 Stage 1 本身无 FWER 校正。Two-stage 设计虽然比纯 post-hoc 好，但不等价于真正的预注册。论文未讨论 Stage 1 → Stage 2 的选择偏差对最终 p-values 的影响。
- **升级路径**: 在 appendix 中添加 Stage 1 selection criteria 的敏感性分析，或明确标注 "conditional inference" 的性质。

### Minor (不影响评分但应修复)

**W-m1. 参考文献孤儿条目 [R1-W5]**
`zou2024improving` 在 bib 中存在但正文未引用。

**W-m2. Figure 2 (forest plot) 可读性 [Visual Check]**
单栏宽度下置信区间 whisker 和模型标签字号偏小，打印后可读性存疑。

**W-m3. 视觉节奏 [Visual Check]**
Pages 3-5 连续纯文本（Related Work + Methods），全文第一张 figure 直到 page 7 才出现。主文仅 2 张 figure，对实证论文偏少。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致：
1. **CP 标注质量**是最核心的方法论弱点（W-C1）
2. **Conclusion 混合 evidence levels** 需要修复（W-M2）
3. **架构覆盖偏斜**限制了 generalizability claims（W-M1）
4. **统计框架和 negative results 的诚实报告**是主要优点（S2, S3）
5. **论文整体水平在 Borderline Conference / Findings 之间**，核心方法论贡献（metric sensitivity）有价值但条件依赖性限制了影响力

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | 影响 |
|------|---------|---------|------|
| R2-N1 Metric×Layer 因果归因 | Should-Fix (partial agree) | Critical (核心叙事缺陷) | R2 认为这是阻止主会议的问题，R1 认为 cosine compression 分析已部分回应 |
| R1-N1 FWER 完整性 | Critical (two-stage ≠ preregistration) | Warning (two-stage 已足够 conservative) | R1 要求 sensitivity analysis，R2 认为现有框架可接受 |
| 新颖性水平 | Borderline Conference (方法论警示价值) | Findings (描述性研究，无新方法/新任务) | R2 对 novelty 评价更严格 |
| Chan & Yong 对比 | 需要加强 | 已在 Related Work 中充分讨论 | R1 未完全认可当前讨论的充分性 |

---

## Questions for Authors

**Q1 [Critical]**: CP 标注的 sensitivity analysis——如果 CP 位置系统性偏移 ±1 step，主要结论（特别是 pre/post-CP 的 temporal windowing 结果）是否仍然成立？

**Q2 [Critical]**: 对 threshold-based metrics（precision, inverse FPR）选择深层的现象，是否有类似 cosine compression 的机制解释？如果没有，如何区分"metric artifact"和"genuine layer-level functional differentiation"？

**Q3 [Major]**: Stage 1 的 2,240 configuration space 中，最终选入 Stage 2 的 12 tests 的选择标准是什么？是否存在对 Stage 1 结果的依赖？如果有，final p-values 应如何解读？

**Q4 [Major]**: 如果增加一个非 Qwen 架构模型（如 Llama-based reasoning model ≥32B），你预期 crossing rate 的 shallow-layer bias 是否仍然存在？基于什么推理？

**Q5 [Minor]**: Three-layer ensemble 的 p≤0.002 是否同样受到 CP 标注质量的影响？如果 CP 标注存在系统性偏差，ensemble 方法能否缓解？

---

## Missing References

两位 Reviewer 未发现明确遗漏的关键引用。以下为建议性补充：
- Causal intervention 方法（DAS, activation patching）的代表性工作——论文在 Limitations 中提到但未引用具体文献
- 非推理模型的 layer selection 敏感性研究（如果存在）——可强化 "metric sensitivity is not reasoning-model-specific" 的论点

---

## External Review

**状态**: 未请求（项目配置未启用外部审稿）

---

## Visual Layout Check (非评分项)

**状态**: 已完成 | 0 Critical, 4 Warning, 6 Info

**Warnings**:
1. Pages 3-5 连续 3 页纯文本（Related Work + Methods），无 figure/table 穿插，阅读节奏断裂
2. 全文第一张 figure (Figure 1 heatmap) 直到 page 7 才出现，前 6 页无视觉锚点
3. Figure 2 (forest plot) 压缩在单栏宽度内，CI whisker 和标签字号偏小，打印可读性存疑
4. 附录末页 (page 32) 仅 ~15% 内容，>3/4 页空白

**Info highlights**:
- Table 1 (page 2) 仅列模型元信息，信息价值低，建议用 teaser figure 替代视觉锚点角色
- 主文仅 2 张 figure，对实证论文偏少（建议 3-4 张），附录有优质图表可提入主文
- 附录 table-heavy（~42 表 vs 3 图），部分表格密集字号小
- 格式规范：booktabs 风格、最优值加粗、公式渲染正确、参考文献格式统一

---

## Overall Assessment

**Score: 3.5 — Borderline Conference**

**Justification**:

本文揭示了一个对 hidden-state safety probe 领域具有系统性影响的方法论问题（layer selection metric 可逆转研究结论），统计框架严谨，negative results 报告坦诚。这些优点使论文具有超出单项研究的方法论警示价值。

然而，两个 Critical 级别弱点限制了论文的可靠性和影响力：(1) CP 标注质量未经充分验证（κ=0.606 via LLM proxy, 无人工 IAA），所有 CP-dependent 结论的根基不牢；(2) metric-layer 交互效应的因果归因不完整——cosine compression 仅解释了 crossing rate 的浅层偏好，其他 metrics 缺乏等价的机制分析。架构覆盖偏斜（3/4 Qwen）进一步限制了 generalizability claims。

论文当前水平介于主会议接收（4.0）和 Findings（3.0）之间。如果能解决 CP 标注的 sensitivity analysis（W-C1 升级路径）和 metric-layer 因果归因（W-C2 升级路径），有望升至 Conference (4.0)。若仅做 minor fixes，Findings (3.0) 是更可能的着陆点。

**R1 评分**: 3.5 (Borderline Conference) — 统计框架好但 FWER 和 CP 标注是硬伤
**R2 评分**: 3.5 (Borderline Conference) — 方法论贡献有价值但偏 descriptive，novelty 有限

---

## Detailed Comments

### 升级至 Conference (4.0) 的最小修改集

1. **[W-C1] CP Sensitivity Analysis**: 在 appendix 中添加 CP ±1 step 偏移的 sensitivity analysis，展示主要结论的鲁棒性（或如实报告不鲁棒）
2. **[W-C2] Metric 机制补全**: 对 threshold-based metrics 添加 1-2 段机制讨论（即使是 "we lack a mechanistic explanation for deep-layer preference" 也比当前的沉默好）
3. **[W-M2] Conclusion 修复**: 32B 结论添加 † 或 "exploratory" 限定
4. **[W-M1] Architecture 限定**: 主文 general claims 添加 "in Qwen-family models" 限定语
5. **[W-m1] Bib 清理**: 删除 `zou2024improving` 孤儿条目

### 从 R26 遗留的 Open Issues（本轮确认未修复）

由于论文在两轮之间无修改，R26 发现的所有 open issues 均维持 open 状态：
- R26-R1-N1 (FWER) → 本轮 W-M4
- R26-R1-N2 (32B power) → 本轮 W-M3
- R26-R1-W1 (CP IAA) → 本轮 W-C1
- R26-R1-W2 (crossing rate mechanism) → 本轮 W-C2 子项
- R26-R1-W5 (orphan bib) → 本轮 W-m1
