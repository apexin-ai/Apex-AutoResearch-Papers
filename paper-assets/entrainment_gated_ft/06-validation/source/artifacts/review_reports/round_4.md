---
round: 4
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-21T08:16:17.220668+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Per-Example Predictive Multiplicity in Hybrid Recurrent Architectures

**Venue**: EMNLP 2026 via ARR (May cycle) | **类别**: Long Paper | **截止日期**: 2026-05-25
**审稿模式**: Fresh (Round 5) | **Reviewer**: 2 名 | **轮次**: 1 轮收敛

---

## Summary

本文利用 Wang et al. (2025) 的 controlled hybrid recurrent model zoo（GatedDeltaNet, RetNet, HGRN2，5 个 attention ratio，2 个 scale），系统分析 attention 对跨架构 per-example 行为的影响。核心发现：(1) aggregate 收敛仅在 LAMBADA 出现（ρ = −1.0, Bonferroni-adjusted p = .100, 未显著）；(2) per-example multiplicity 呈 task-dependent spectrum（α = 0.10–0.30）；(3) aggregate 收敛与 per-example 分歧解耦。论文统计方法透明，实验设计干净，但核心 claim 的统计证据不足，新颖性有限，且每个配置单一 training run 无法区分架构效应和 seed 效应。

## Strengths

**S1. 控制良好的实验设计。** Model zoo 共享训练数据、tokenizer、超参数，有效隔离架构变量。这是当前条件下研究架构效应的最佳方法学选择。[R1-S1, R2-S2 共识]

**S2. 统计方法透明诚实。** 坦诚报告不显著结果（Bonferroni p = .100）、bootstrap 局限性（n=3, "heuristic indicators"）、负面结果（BoolQ 混合显著性）、GDN confound。没有选择性隐藏。[R1-S2, R2-S1, S4 共识]

**S3. 详尽的附录。** 9 页 13 个 Appendix，包括 normalized Jaccard ES、跨 benchmark confidence margin、跨 scale 比较、架构内稳定性、permutation tests 等。可复现性材料充分。[R1-S3, R2-S5 共识]

**S4. 有实际意义的研究问题。** Aggregate benchmark 可能掩盖 per-example 分歧，对部署可靠性和 ensemble 构建有直接指导意义。通过 predictive multiplicity 框架（Marx et al., 2020）进行理论锚定恰当。[R1-S4, R2-S3 共识]

**S5. 审慎的 claim 限定。** 使用恰当的 scope 限定语言（"preliminary observation"、"task-dependent spectrum"）。[R1-S5, R2-S4 共识]

## Weaknesses

**W1 [Critical] 架构效应 vs. seed 效应无法区分。** 30 个配置每个仅一个 training run。论文声称 multiplicity "arising from architectural variation rather than random initialization"（§4.3），但无多 seed 数据支撑此归因。Prior work（McCoy et al. 2020; D'Amour et al. 2022; Sellam et al. 2022）已证明 seed variation 本身可产生显著 per-example disagreement。观察到的跨架构 Jaccard ~0.10 无法被确认为架构 multiplicity 而非 seed noise，除非提供同架构跨 seed 的 Jaccard baseline。[R1-W1 Critical, R2-W3+Q3 支持]

**W2 [Critical] 核心收敛 claim 统计不显著且依赖 confound。** LAMBADA ρ = −1.0 的 Bonferroni-adjusted p = .100 未达 α = 0.05。BCa 95% CI [−1.0, −0.7] 基于 n=3 架构（27 unique resamples, 11.25% degenerate），论文自身承认为 "heuristic indicators"（§3.5），但在 abstract 中呈现为正式统计结果，存在内部矛盾。移除有 head-count confound 的 GDN 后弱化至 ρ = −0.7（p = .233）。收敛虽已从标题移除，但仍占主文约 2 页且在 abstract/intro 中显著出现，prominence 与证据强度不匹配。[R1-W2 Critical + W3 Major, R2-W1 Critical + W3 Major 共识]

**W3 [Major] "Task-dependent spectrum" 仅基于 3 个 benchmark，存在评估格式 confound。** α = 0.10（HellaSwag, 4-way MC）、0.21（ARC-Easy, 4-way MC）、0.30（LAMBADA, open-ended）。3 个数据点称 "spectrum" 过度表述。α 的变异可能反映评估格式（open-ended vs multiple choice）而非 task type。BoolQ（α ≈ 0.45, binary）如果纳入会打破 retrieval > mixed > reasoning 排序。每个 task category 仅 1 个代表性 benchmark，无法区分 task-specificity 与 benchmark-specificity。[R1-W4 Major, R2-W4 Major 共识]

**W4 [Major] 新颖性有限。** 核心概念工具（ambiguity α, Jaccard overlap, helped/hurt decomposition）均为已有指标（Marx 2020, D'Amour 2022）的直接套用。"Decoupling" 在概念上不算意外——aggregate mean 和 per-example overlap 是数学上不同的对象。无新方法、新指标或新理论框架。贡献本质是 "在新 setting 上测量已知量"。[R2-W2 Major, R1 Excitement 2.5/5 方向一致]

**W5 [Major] 正文页数超限。** 主文（Abstract → §5 Conclusion）约 8.2–8.3 页，超出 EMNLP 2026 Long Paper 8 页限制。§4.5 尾部和 §5 位于第 9 页。[R1-W5 Major, R2-W6 Minor, Visual Check 确认]

**W6 [Major] 遗漏关键相关工作：Zoology (Arora et al., 2024, ICLR)。** 该文系统证明 attention-free 和 attention 模型 82% 性能差距由 associative recall 能力解释，直接为本文 task-specific convergence 提供理论解释。Based (Arora et al., 2024, ICML) 和 Samba (Ren et al., 2024) 也缺失。[R2-W5 Major]

**W7 [Minor] Ensemble 建议缺乏实验支撑。** Conclusion 中 "diverse hybrid ensembles may offer complementary coverage" 无实验支持。Low Jaccard 不直接意味着 ensemble 收益（Kuncheva & Whitaker 2003）。[R1-W6 Minor]

**W8 [Minor] Binary decomposition 可能低估多选题一致性。** Attention 可能增加 confidence 而不翻转 binary outcome，低估跨架构功能相似性。[R1-W7 Minor]

**W9 [Minor] Abstract 信息密度过高。** 统计量堆砌（ρ, CI, σ, α, Jaccard, p-values），第一遍阅读难以 parse。[R2-W7 Minor]

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
- 核心收敛 claim 统计不显著，evidence presentation 与 evidence strength 不匹配
- GDN confound 部分解释了 ρ = −1.0，abstract 应反映 sensitivity analysis
- "Spectrum" 基于 3 个数据点证据不足，存在格式 confound
- 页数超限需修复
- 总体评分 3.0 (Findings)——soundness 足以发表但 excitement 不足以 Conference

## Reviewer Divergence

- **Seed confound 的严重性**：R1 视为最根本限制 [Critical]，R2 提出但未列为独立 Critical weakness。**Director 判定**：R1 立场更严格且合理——单一 training run 确实是根本性限制，归因到 "architectural multiplicity" 需要 seed baseline。
- **Zoology 遗漏**：R2 视为 Major missing reference，R1 未提及。**Director 判定**：Zoology 直接解释了 task-specific convergence 的 recall 机制，应纳入。
- **新颖性评估**：R2 明确列为 Major weakness，R1 通过 Excitement 2.5/5 暗示但未单独列出。**Director 判定**：新颖性确实有限，同意 R2 判断。

## Questions

**Q1.** 同架构跨 seed 的 per-example Jaccard baseline 是多少？如果与跨架构 ~0.10 可比，"architectural multiplicity" claim 需重新评估。

**Q2.** GDN/RetNet/HGRN2 在 pure 和 h3-1 配置下的绝对 accuracy 差异？GDN net −153 是否为 regression to the mean？

**Q3.** Confidence margin 分析中 GDN 使用 h12-1 而 RetNet/HGRN2 使用 h3-1，不一致是否影响可比性？

**Q4.** Transformer entrainment Δ = 0.005–0.029 (Appendix J) 是否统计显著？

**Q5.** ρ_α = −0.8（HellaSwag）是否暗示被 "variation < 0.03" 阈值掩盖的 attention-dose dependency？

**Q6.** BoolQ α ≈ 0.45 如何与 retrieval > mixed > reasoning 排序调和？

## Missing References

1. **Arora, S. et al. (2024). "Zoology: Measuring and Improving Recall in Efficient Language Models." ICLR.** — 直接解释 LAMBADA task-specific convergence 的理论基础。
2. **Arora, S. et al. (2024). "Simple Linear Attention Language Models Balance the Recall-Throughput Tradeoff." ICML.** — recall-throughput 框架。
3. **Ren, L. et al. (2024). "Samba." arXiv.** — 补充 hybrid architecture 覆盖。
4. **Black et al. (2022, FAccT)** — Multiplicity 在算法公平性中的影响（可选）。

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用）。

## Visual Layout Check（非评分项）

视觉审查已完成。0 critical, 4 warnings, 6 info。

**Warnings：**
1. Pages 3-6 连续 4 页纯文本（Figure 1 p2 → Table 1 p7 间隔 5 页），Method 段缺架构图/pipeline 示意图
2. 主体正文仅 4 个 display items（2 figure + 2 table），实证论文典型 5-8 个
3. 主体正文约 8.2 页，超出 8 页限制
4. Method §3.3-3.5 数学定义适合 display equation，可打破文字墙

**Info：** Figure 1 字号偏小；Figure 2 黑白打印区分不足；Table 1/2 格式规范（booktabs）；参考文献无 [?]；附录 19 表可接受。

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Confidence: 4/5**

**官方维度打分（两位 Reviewer 均值）：**

| 维度 | R1 | R2 | 均值 |
|------|----|----|------|
| Soundness | 3.0/5 | 3.0/5 | 3.0 |
| Excitement | 2.5/5 | 2.5/5 | 2.5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0 |
| Overall | 3.0 | 3.0 | **3.0** |

**理由：**

论文提出了一个有实际意义的研究问题（aggregate benchmark 掩盖 per-example 分歧），通过 controlled model zoo 提供了系统性实证分析。方法学设计合理，统计报告透明诚实，附录分析详尽全面。

但以下问题阻止 Conference-level 接收：

**(a) 核心归因无法验证 [W1 Critical]。** 每个配置单一 training run，无法区分架构效应和 seed 效应。"Architectural multiplicity" 归因缺乏 within-architecture seed baseline。

**(b) 收敛 claim 统计不显著 [W2 Critical]。** Bonferroni p = .100 + GDN confound + n=3 heuristic CI 组合使证据基础薄弱，但收敛在论文中获得过高 prominence。

**(c) 新颖性不足 [W4 Major]。** 无新方法/指标/理论，是已知框架在新 setting 的直接应用。

**(d) 证据基础偏窄 [W3 Major]。** "Task-dependent spectrum" 仅 3 benchmark，存在评估格式 confound。

**(e) 格式不合规 [W5 Major]。** 正文约 8.2 页超限。

**Findings 级别的论证：** Per-example 分析方法论有价值，decoupling 量化（Jaccard 4% 饱和 vs σ 持续下降）是 solid empirical observation，统计透明性值得鼓励。足以支撑 Findings 发表，但证据强度、新颖性和范围不足以构成 Conference 贡献。

**升级至 Conference 需要：** (1) 至少 1 个架构的多 seed baseline 以区分架构和 seed 效应；(2) 扩展 per-example 分析至更多 benchmark；(3) 压缩收敛 prominence 或提供更强统计证据；(4) 修复页数超限。

## Detailed Comments

**Title & Abstract**：标题已缩小范围。Abstract 中 "BCa 95% CI [−1.0, −0.7]" 应注明 n=3 caveat。统计量堆砌过多。

**§1 Introduction**：Contributions list 仍以 convergence 为先——建议将 per-example multiplicity 作为第一条 contribution。

**§2 Related Work**：覆盖全面但缺少 Zoology/Based 的 recall-throughput 视角。

**§3 Method**：描述清晰。Task taxonomy pre-specification 好。§3.3-3.5 建议 display equation。

**§4.1**：Table 1 信息密度高。BoolQ ratio = 0.69（attention 增加 variance）值得讨论。

**§4.2**："sufficient model capacity may facilitate complete equalization" 措辞偏强。

**§4.3**：最核心贡献。HGRN2 唯一 net positive 值得更多讨论。

**§4.4**：Decoupling 量化有价值。"Different timescales" 暗示 temporal process，但 attention ratio 是 hyperparameter 非时间变量。

**§4.5**：GDN confound 讨论好，但实际 undermines convergence claim，应更 prominently 反映在 abstract。

**Limitations**：全面。Seed confound 影响应在主文 discussion 更突出。

**ARR Checklist**：完整。C1 报告 ~5 GPU-hours on RTX PRO 6000。

**匿名性**：通过。

**引用核查**：42 篇引用全部真实，无虚假引用。