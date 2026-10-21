---
round: 9
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T02:58:33.789944+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告 — Round 10 (Fresh Review)

**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models
**Venue**: EMNLP 2026 (via ARR)
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性与完整性）；Reviewer 3 本轮未分配任务（EMNLP 一般会议标准编排为 2 人）
**审稿模式**: Fresh（重新审稿，无上轮记忆）

---

## Summary

本文将 Generalizability theory (G-theory) 应用于 LLM 评估方差分解，在 8 个 7–9B 开源指令微调模型和 5 个 benchmark 上交叉 7 个 facets（item, model, precision, prompt, seed, temperature, ordering），生成约 230 万条 binary 评估记录。核心产出是 D-study 可复现性预算：推荐 3-prompt × 3-seed 设计以 178 items 达到 G ≥ 0.80（vs. 单条件设计 552 items），并发现 MC 与 FF benchmarks 的方差结构存在格式相关的差异模式。

---

## Strengths

**S1** [强] 实验规模与设计严谨性突出——230 万条记录、7 facets 全交叉、8 模型 × 5 benchmarks 的 factorial design 在 LLM 评估方差分析文献中属最大规模之一。Henderson Method I + 1,000 resample bootstrap CI 的统计方法选择恰当。

**S2** [强] 鲁棒性验证异常充分——9 项独立分析（GLMM complement, REML comparison, probit simulation, null calibration, LOMO, CI method comparison, inter-model agreement, facet specification sensitivity, reduced crossing validation）系统性排除了几乎所有可预见的方法论质疑。论文最突出的技术优势。

**S3** [强] 实用产出具体可操作——D-study budget recommendations（3×3 design with 178 items）和 intermediate design gradient（Table 9: minimal upgrade 2p → standard 4p×4s×2t）为 evaluation practitioners 提供即时可用的决策工具。承诺开源 G-theory pipeline 和 D-study calculator。

**S4** [中] Binary scoring conditionality 的透明处理——§3.5 首次声明、§4.1 text-exact-match 实验佐证（G=0.936 vs 0.007）、Appendix A partial-credit pilot 验证（G 0.76→0.55, ρ=0.26）、§4.3 再次提醒——多次多角度披露远超同类论文水平。

**S5** [中] IRT+G-theory 互补性分析（Table 4）——证明 item selection（IRT）和 protocol optimization（G-theory）正交：IRT 116 items 在 single-condition 下 G=0.457 但 multi-facet 下 G=0.895。值得独立突出的洞见。

**S6** [中] Subject-level 分析有洞察价值——Table 10 揭示 reasoning-heavy subjects（high_school_math: G=0.614）与 knowledge-intensive subjects（international_law: G=0.930）的显著差异，对 benchmark 设计者有直接参考价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 强共识] D-study item budget 公式不完整，核心贡献不可独立验证

Equation 1 定义 G_item = σ²_p / (σ²_p + σ²_rel)，其中 σ²_rel 仅依赖各 facet 条件数，不含 item 数量 n_p。据此公式 G 与 n_p 无关，但 Table 4 的 budget（55/178/552 items for G≥0.80）和 Figure 1 的 D-study 曲线明显依赖 item 数。反推显示实际使用了 Spearman-Brown 类公式（G(n) = nG₁/(1+(n-1)G₁)），但论文从未给出。论文实际存在两个不同的 G 指标但只明确定义了一个。D-study 预算是论文的核心实用贡献（标题和摘要的主角），读者无法独立验证关键数字——这是可复现性的根本问题。

→ 建议：§3.1 或附录完整给出 D-study 投影公式（含 n_p），区分 per-item G 和 aggregate-score G，提供从 variance components 到 Table 4 数值的完整计算示例。

**MF2** [critical, 强共识] Binary scoring scope 未在 title/abstract 中限定

Title "Reproducibility Budgets for Open-Weight LLM Evaluation" 暗示 budgets 适用于通用 LLM evaluation，但所有 D-study budgets 仅对 binary correctness scoring 有效。Partial-credit pilot 显示 G 从 0.76 降至 0.55（ρ=0.26），text-exact-match 更极端（G=0.936 vs 0.007）。实际 LLM evaluation 中大量场景使用 continuous scoring（MT-Bench, AlpacaEval win rate, LLM-as-judge），论文 budgets 对这些场景无指导价值。§3.5 的声明（"All findings are conditioned on binary correctness scoring"）正确但位置过深，title/abstract 未反映。

→ 建议：Title 加 "under Binary Scoring" 或 "for Binary Benchmarks"；Abstract 首处提及 D-study budget 时立即声明 scope。

**MF3** [warning→critical, 共识 with nuance] Binary scoring 对 D-study projection 精度的系统偏差未量化

Probit simulation 报告 binary 与 continuous variance components 之间 ρ=0.732（excluding residual），top-5 ordering 仅 79% correct，|bias|=0.28–0.37（中等难度 items）。Bootstrap CIs 捕捉 item-sampling variability 但不含 binary scoring 的系统偏差。如果 variance components 因 binary scoring 存在系统偏差，D-study 的具体 item 数推荐可能不准确。R2 指出 null calibration（ratio=1.0008）和 component ordering consistency（100%）说明 relative ranking 稳健，认为严重程度略低于 R1 评估——但双方同意需量化影响。

→ 建议：从 probit simulation 的 continuous variance components 计算 D-study projections 并与 binary 版本比较；报告 D-study budget 在 binary vs. continuous 下的差异（绝对 item 数和百分比）。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, 强共识] G_item 与模型比较可靠性的概念鸿沟

论文以 item 为 object of measurement，G_item 衡量 item 难度在方法论条件下的泛化性。但读者更关心的是模型比较可靠性（model ranking reliability）。σ²_model 仅 2.8%，G_model 可能显著低于 G_item=0.896。论文以 "reproducibility budget for evaluation" 措辞呈现结果，构成 framing mismatch。

→ 建议：显式计算 G_model（models 为 object），讨论 G_item ≥ 0.80 蕴含（或不蕴含）model ranking reliability 的条件。

**SF2** [warning, 持续分歧——5 轮] 相对于 Messing (2026) TEE 的增量贡献定位

R2 认为三个扩展方向（infrastructure facets, cross-benchmark, D-study budgets）均非 methodological advance，novelty 不足。R1 反驳：fully crossed multi-benchmark design 使 infrastructure × methodology interaction 首次可估计，是 design-level 创新；binary data adaptation 非平凡。R1 建议从 critical 降为 should-fix。双方一致认为 IRT+G-theory 互补性（Table 4）是最有价值但被低估的贡献点。

→ 建议：将 IRT+G-theory 互补性提升至 Contributions；Positioning 段对三个扩展方向标注方法论层级（methodological extension vs. empirical scale-up）。

**SF3** [warning, 强共识] "3.1× item reduction" framing 隐藏 total evaluation 增长

Abstract 和 Contribution C1 强调 item 减少（552→178）但 total evaluations 从 552 增至 1,602（2.9× 增长）。这不是 reduction 而是 resource reallocation。§4.5 的讨论（"trading approximately 3× more evaluations per item for 3× fewer items"）比 Abstract 更诚实。

→ 建议：Abstract 和 C1 对称呈现 item reduction (3.1×) 和 total evaluation increase (2.9×)。

**SF4** [warning, 强共识] 模型可交换性 out-of-sample 验证不足

LOMO（CV ≤ 1.25%）和 four-model subset check（|ΔG| ≤ 0.029/0.065）是 within-sample stability，非 out-of-sample generalization。72B validation 仅 Qwen2.5 family（共享 tokenizer 和训练方法）。8 个模型的时间同质性（2024-2025 训练周期、training data overlap）可能高估 variance structure 稳定性。

→ 建议：获取至少一个 cross-family validation point（如 Llama-3 70B）；更明确限定 budget 推荐适用范围。

**SF5** [warning, 强共识] Format-associated pattern 统计支撑不足且占用过多篇幅

n=5 benchmarks, permutation p=0.10, benchmark-level CI 含零 [-1.7, 5.1]。设计不对称（ordering 仅 MC, prompt 类型不同）是额外 confound。§4.3 约 1 页正文（~12.5%）对于 p=0.10 的 exploratory observation 在 8 页限制下偏奢侈。已标注 "exploratory" 处理透明。

→ 建议：§4.3 正文压缩至 1 段核心发现，详细讨论移至附录。

**SF6** [warning, 共识] Partial-credit pilot 基于单 benchmark 单 model 但结论过于确定

§3.5 写 "D-study budgets do not transfer to finer-grained scoring rubrics"，但仅基于 GSM8K + Llama-3.1-8B。ρ=0.26 的变化幅度足够大，核心 message 不变，但措辞需软化。

→ 建议：改为 "preliminary evidence suggests limited transferability"。

**SF7** [warning, R2→R1 部分同意] Conclusion 过于简短

当前 Conclusion 约半页，仅复述数字和 binary scoring 限制。缺少 practitioner-oriented 讨论（evaluation harness 整合路径、benchmark 设计者 vs 使用者建议）。R1 认为简短是 8 页限制下合理选择但同意可扩展 1-2 句。

→ 建议：扩展至 2-3 段，增加 practical adoption pathway。

**SF8** [warning, R2→R1 部分同意] Related Work 缺 evaluation harness 实现文献

未讨论 lm-eval-harness evaluation protocol 与本文 facets 的映射、MMLU-Redux/MMLU-Pro 等变体。

→ 建议：Related Work 或 Limitations 增加 1-2 句。

### Minor（不影响接收）

- **M1**: Abstract 数字密度过高（20+ 数值），核心 message 被淹没（R2-M1, R1 AGREE）
- **M2**: Table 3 "prompt" 行 MC/FF 含义不同（MC = prompt×item interaction, FF = prompt main effect），行标签应区分（R2-M2, R1 AGREE）
- **M3**: "all others < 0.1%" 不够精确，建议报告具体数值（R1-M1）
- **M4**: 排除 temperature=1.0 可能低估 temperature variance（R1-M2）
- **M5**: 单一推理引擎（vLLM 0.9.2），其他引擎可能引入额外 variance（R1-M3）
- **M6**: §4.4 Precision Separability 仅 2 句话作为独立 subsection 过短（R2-M4, R1 认为 negative result 简短合理）
- **M7**: Figure 1 y 轴字体偏小，Figure 3 legend 字号偏小、灰度可区分性一般（R2-M5 + 视觉审查）

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 独立提出并在交叉回应中确认一致：

1. **D-study 公式不完整**（MF1）——核心贡献不可独立验证，强共识
2. **Binary scoring scope 限定**（MF2）——title/abstract 暗示过广适用性，强共识
3. **Binary bias 量化**（MF3）——共识 with nuance（R2 认为略低于 R1 评估的严重程度）
4. **Format-associated pattern 统计不足**（SF5）——n=5, p=0.10, CI 含零，强共识
5. **模型可交换性 out-of-sample 不足**（SF4）——within-sample ≠ out-of-sample，强共识
6. **Partial-credit 结论过强**（SF6）——"do not transfer" 改为 "preliminary evidence"，共识
7. **"3.1× reduction" framing 不对称**（SF3）——应对称呈现，强共识
8. **G_item vs G_model 概念鸿沟**（SF1）——新发现，强共识
9. **IRT+G-theory 互补性被低估**——Table 4 是最有价值的贡献点但被埋没，强共识
10. **鲁棒性分析是论文最突出优势**——双方独立评价一致

## Reviewer Divergence [REBUT]

1. **Novelty vs. Messing (2026)**（SF2）：R2 认为三个扩展方向均非 methodological advance（critical）；R1 反驳 fully crossed multi-benchmark design 使 infrastructure×methodology interaction 首次可估计是 design-level 创新，建议降为 should-fix。**5 轮持续分歧**，报告中保留为 should-fix 并如实记录两方论据。

2. **Conclusion 长度**（SF7）：R2 认为 Conclusion 过短缺 practical implications；R1 认为简短合理但同意可增加 1-2 句。分歧较小。

---

## Questions for Authors

1. **D-study 公式推导**：请提供从 Equation 1 的 variance components 到 Table 4 的 item budget 数值的完整推导过程，明确 G 如何同时依赖 n_p 和各 facet 条件数。
2. **G_model 计算**：在推荐的 3×3 design 下，以 model 为 object of measurement 的 G_model 是多少？G_item ≥ 0.80 是否蕴含 model ranking reliability？
3. **Binary bias 对 budget 的影响**：从 probit simulation 的 continuous variance components 计算的 D-study budget 与 binary 版本差异多大？
4. **IRT+G-theory pipeline**：Table 4 是否意味最优策略是先用 IRT 选 item 再用 G-theory 优化 protocol？如果是，建议明确提出。
5. **Partial-credit 泛化性**：partial-credit pilot（G 0.76→0.55, ρ=0.26）是否仅基于 GSM8K 单一 benchmark 单一 model？
6. **Cross-family scale validation**：是否计划增加非 Qwen2.5 架构的 72B 模型验证？
7. **Contamination 定量检验**：是否可对 8 个模型运行 contamination detection 提供直接证据？

---

## Missing References

- MMLU-Redux (Gema et al., 2024) — MMLU 修订版本，影响 200-item sampling 代表性讨论
- MMLU-Pro (Wang et al., 2024) — MMLU 扩展版本
- Oren et al. (2024) — contamination detection，Limitations 补引
- lm-evaluation-harness 与本文 multi-facet 建议的整合讨论

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 5 info）：

**Warning**:
- P3-4 连续两页纯文本（Related Work + Method），无 figure/table 穿插，视觉节奏偏平。建议将 Figure 2（当前 P5）提前
- P16 附录最后一页内容仅约 1/4，大量空白。建议合并压缩

**Info**:
- P2 Figure 1 轴标签和 legend 字号偏小（约正文 60-65%）
- P7 Figure 3 堆叠柱状图 legend 字号偏小，浅色类别灰度对比度一般
- P1 首页无 display item，Figure 1 在 P2（可接受但非最优）
- P5 Figure 2 crossing 结构示意图设计清晰，信息传达到位
- P13 三个表格密度高但排版整齐（附录中可接受）

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 4.0 | 3.75 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | 3.5 |

**Confidence**: 4/5（两位 Reviewer 均熟悉 G-theory 和 LLM evaluation 文献）

**综合判断**：

实验执行和鲁棒性验证达到高标准（9 项独立分析），D-study budget 工具有实际价值，binary scoring conditionality 的透明处理远超同类论文。这是一篇 solid empirical contribution。

阻碍 Conference 接收的核心问题：

1. **可复现性**（MF1）：D-study budget 是标题中的核心贡献，但公式不完整导致读者无法独立验证——这是一个技术性修复，不需要新实验。
2. **Scope framing**（MF2）：title/abstract 暗示通用适用性但 budgets 仅对 binary scoring 有效——需要 framing 调整而非方法论改变。
3. **Binary bias 量化**（MF3）：需要从 probit simulation 提取定量影响——数据已有，需补充分析。

如果 MF1-MF3 得到解决，加上 IRT+G-theory 互补性的提升（SF2 共识部分）和 framing 对称化（SF3），论文有潜力达到 4.0（Conference）。当前版本处于 Conference/Findings 边界。

---

## Detailed Comments

### §1 Introduction
- Contribution C1 的 "3.1× reduction" 应对称呈现 total evaluation 增长（SF3）
- 考虑在 Contributions 列表中提升 IRT+G-theory 互补性（SF2 共识）
- Precision separability 作为 C1 sub-finding 的呈现已改善，但仍略占独立叙事空间（FR8-W2）

### §3.1 G-theory Method
- Equation 1 需完整展开 σ²_rel 的组成和 n_p 的作用（MF1）
- 区分 per-item G 和 aggregate-score G（MF1）
- 建议增加 G_model 定义和计算（SF1）

### §3.5 Binary Data / Model Facet
- "do not transfer" → "preliminary evidence suggests limited transferability"（SF6）
- CI 报告标注 "conditional on these 8 models"（FR8-W5）
- Quasi-random facet 论证增加 cross-family generalization boundary 讨论（SF4）

### §4.3 Format-Associated Patterns
- 正文压缩至 1 段核心发现（SF5）
- 详细讨论移至附录
- 更强的 exploratory/descriptive 标注

### §4.5 D-Study Budgets
- 补充完整计算示例（MF1）
- 讨论 G_item vs G_model 的关系（SF1）

### §5 Conclusion
- 扩展 practical implications（SF7）

### Abstract
- 精简至 3-4 个关键数字（M1）
- 首处提及 budget 时声明 binary scoring scope（MF2）
- 对称呈现 item/evaluation tradeoff（SF3）

### Title
- 加 "under Binary Scoring" 或 "for Binary Benchmarks" 限定（MF2）

---

**注**: 本轮审稿编排为 2 名 Reviewer（R1 方法严谨性 / R2 新颖性与完整性），符合 EMNLP 一般会议标准。Reviewer 3 本轮未分配审稿任务。