# Director coordination — Part 2 of 7

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/3d/3daf92a3dbeb151a5ec1.json)

## Round 24

### Tool call

_source line 200 · 2026-05-21T17:55:37.919213+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "force_resubmit": "True",
  "report": "# 最终审稿报告 — Convergence Round (Final)\n\n**论文**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n**截止日期**: 2026-05-25 AoE\n**日期**: 2026-05-21\n**审稿流程**: Round 5 (fresh) → Round 6 (revised) → Round 7 (convergence, final)\n\n---\n\n## ⚠️ 版本一致性说明\n\n两位 Reviewer 均标记了 Director brief 与实际 PDF 之间的内容差异。**两位 Reviewer 均基于实际 PDF 内容评审**，其评分和判断可信。实际论文包含 ~60 references、7 experiment sections (§4.1-4.7)、4 段 Related Work、ΔTPR=+0.508 at p=0.5。本报告基于 Reviewer 对实际 PDF 的评估。\n\n---\n\n## Summary\n\n本文将 Mantel-Haenszel DIF 分析大规模应用于 LLM benchmark 评估（5,227 models × 12,508 MMLU items），发现 31.3% items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 DIF，跨 6 个 METABENCH 基准复现（C% = 17.9–31.3%，45–174× 高于随机基线）。修订版做了 4 项显著改进：标题软化、multi-subject injection、LLM-specific challenges 论证、contributions 收紧为 3 个。\n\n经过 3 轮审稿（初审、修订版评估、最终收敛），两位 Reviewer 均维持 **Overall 3.5 (Borderline Conference)**。\n\n---\n\n## Strengths\n\n1. **大规模、系统的 confound 控制**：5 种 cohort design × 6 种替代解释 × 4 个 threshold sensitivity 点。Matched-ability 分析收敛于 ~28-29% 的 floor（跨不同比较），Soundness 获两位 Reviewer 高评（R1: 4.0, R2: 3.5）。\n\n2. **Cross-subject matching 是最强贡献**（R1+R2 共识）：Proposition 1（properly scoped to single-subject）+ multi-subject boundary（ΔFPR < 0.007 for k ≤ 5, degradation at k = 10）。ΔFPR < 0.001 vs. within-subject +0.19 的对比令人信服。这是 reusable methodological infrastructure。\n\n3. **Ground truth meta-critique 有社区价值**：enrichment = 0.964, Jaccard = 0.206, φ = 0.012 表明 DIF flags 与 web-overlap labels 近乎独立。这对 contamination detection 文献的 evaluation methodology 有直接影响。\n\n4. **LLM-specific methodological adaptations**：新增 \"LLM-specific challenges\" 节（§3.2）讨论 deterministic responses violating local independence, bimodal ability distribution, MMLU multidimensionality——非泛泛之谈，每个点有具体应对措施。\n\n5. **Cross-benchmark replication at scale**：6 个 METABENCH benchmarks（27,125 items），knowledge/reasoning C% ≥ 26.9% > procedural C% ≤ 18.9%，每个都 45-174× 高于 random baseline。\n\n6. **修改响应质量高**：Round 1 的 3 个 critical issues 均有实质性回应（title 改善、Proposition 1 限定、multi-subject boundary、Claim 4 降级、Related Work 扩充至 ~60 refs）。R1 明确肯定\"Round 1 → Round 2 的修改是认真且有效的\"。\n\n---\n\n## Weaknesses\n\n### Must-Fix（阻止升至 4.0 的硬性问题）\n\n**MF-1** [critical, R1 primary concern] **缺少 permutation null——headline 31.3% 无 principled baseline**\n- Random-split (0.18%) 是 perfect null（同一 cohort 内部），但不代表 realistic null。随机打乱 2023/2024 cohort labels 1,000 次后的 permutation null C% 才是正确 baseline comparator。如果 permutation null ~5%，则 effective temporal DIF ~26%，headline 需调整。这直接影响标题中的 \"31%\" 和所有下游分析。\n- **R1 最终评估中最重要的新发现**。R2 未独立提出但未反对。\n- 建议：补充 1,000 次 permutation null，报告 null distribution mean + 95th percentile，计算 null-adjusted C%。计算成本很低。\n\n**MF-2** [critical, residual] **Causal language 残余**\n- 标题已改善（\"Temporal Measurement Drift\" 替代 \"Psychometric Instability\"），但 Conclusion 仍说 \"driven by item properties\"。\"Driven by\" 暗示因果方向，数据只支持 association。\n- R1+R2 共识。\n- 建议：\"driven by\" → \"associated with\"；全文检查 causal-leaning 措辞。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning, consensus] **Binary flipping 的 ecological validity 局限**\n- Uniform rate p 的 incorrect → correct 翻转模拟 \"perfect contamination\"，真实 contamination 更微妙（partial memorization, reasoning shortcuts, format-specific advantages）。ΔTPR = +0.508 at p = 0.5 是 meaningful 但建立在极端 injection 上。\n- R2 补充 defense：cross-subject matching 消除 FPR inflation 的 validity 不依赖 injection 的 ecological validity。\n- 建议：Limitations 中讨论 binary flipping 简化和 non-uniform injection sensitivity。\n\n**SF-2** [warning, consensus] **Section 5.3 GSM1K N=33 仍占过多篇幅**\n- 已从 contribution 降为 Discussion——正确。但仍以 2 段展开。R1 指出 negative correlation 暗示 DIF-flagged items 对 contaminated models 更难——与 \"DIF 检测 contamination\" 叙事矛盾。\n- 建议：压缩为 1-2 句 exploratory note，释放空间给 practical recommendations 和 multi-subject injection 展示。\n\n**SF-3** [warning, improved but still insufficient] **Practical recommendations**\n- 修订版已扩展为 graduated thresholds（<15% monitor, 15-25% flag, >25% act）——有改善。但仍缺 integration workflow、threshold justification、tooling 建议。\n- 建议：进一步扩展，特别是与 BHI/Growing Pains 的集成。\n\n**SF-4** [warning, new in Round 7] **IRT model fit statistics 未报告**\n- 论文使用 2PL 参数做 power analysis 但不报告 fit statistics（CFI, RMSEA, |Lz|）。MH-DIF 不依赖 IRT fit（论文正确指出），但 transparent reporting 要求至少呈现。\n- 建议：报告 fit statistics，即使结论不变。\n\n**SF-5** [warning, consensus] **Multi-subject injection 结果展示过于压缩**\n- k∈{1,3,5,10,20} 的 ΔFPR 数据仅占 1.5 句 inline text。这是回应 Round 5 核心批评的关键实验，应以 table/figure 呈现。\n\n**SF-6** [warning] **Claim 2 framing 微调**\n- 更准确的表述：\"DIF and contamination detection measure fundamentally different constructs\"，而非 \"web-overlap labels fail to validate DIF\"。可补充 4 象限 item characteristic analysis。\n\n**SF-7** [warning] **Bootstrap CI 不对称性原因未讨论**\n\n**SF-8** [warning] **Growing Pains overlap 分析仍缺**（\"Empirical comparison awaits public release\" 合理但仍无定量数据）\n\n**SF-9** [warning] **DIF 术语 running example**：修订版已添加 formal-logic item 示例（α_MH=0.42, Δ_MH=2.04）——✅ 已回应。\n\n---\n\n## Reviewer Consensus (Final)\n\n**完全一致的判断**：\n1. Cross-subject matching 是最强贡献\n2. 论文对 Round 1 反馈的回应质量高\n3. Permutation null 缺失是方法论硬伤（R1 主推，R2 不反对）\n4. GSM1K N=33 证据不足\n5. Binary flipping 是 simplification\n6. Overall 3.5 (Borderline Conference)\n\n**分歧（已通过交叉回应缩小）**：\n| 维度 | R1 | R2 | 差异来源 |\n|------|-----|-----|---------|\n| Soundness | 4.0 | 3.5 | R1 更重视 confound 控制系统性 |\n| Excitement | 3.0 | 3.5 | R1 采纳 novelty ceiling 下调；R2 认为 transplant 质量弥补 |\n| Reproducibility | 4.0 | 4.0 | 一致 |\n| Clarity | 3.5 | 4.0 | R1 认为 space allocation uneven |\n| Overall | 3.5 | 3.5 | **一致** |\n\nR1 建议 venue positioning: **Findings accept, with path to Main if permutation null added**。\nR2 维持 **Borderline Conference，若 GSM1K + practical recommendations 解决可升至 4.0**。\n\n---\n\n## Questions to Authors\n\n1. **Permutation null**：将 cohort labels 随机打乱 1,000 次，每次重新计算 C%——permutation null distribution 的 mean 和 95th percentile 是多少？null-adjusted C% 是否改变 headline？\n2. **IRT model fit**：MMLU 12,508 items 在 2PL 下的 CFI、RMSEA、|Lz| person-fit 分布是什么？\n3. **Multi-subject injection boundary**：如果 real-world contamination 同时影响 >5 subjects（如 model 训练时 ingest 了整个 MMLU dataset），如何论证真实 contamination pattern 落在 k ≤ 5 的安全区间内？\n4. **Claim 2 四象限分析**：web-contaminated × DIF-flagged 的 2×2 中，各象限的 item characteristics（difficulty, discrimination, subject distribution）是否有 systematic pattern？\n\n---\n\n## Missing References\n\n修订版已全面补充：BHI, Benchmark², ATLAS, MedIRT, 加上原有的 DIF methodology 和 IRT-for-LLM 文献。R1 确认当前版本 Related Work \"adequate\"（~44 unique citations in §2, ~60 total）。仅需确认 orphan bib entries 已清理。\n\n---\n\n## External Review\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\nRound 5 时完成：2 warnings（pages 3-5 visual gap, 仅 4 display items in 8 pages）, 7 info。修订版可能已改变布局。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4.0 | 3.5 | 3.75 |\n| Excitement | 3.0 | 3.5 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Clarity | 3.5 | 4.0 | 3.75 |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n**置信度**: 4/5\n\n**EMNLP 2026 评分映射**: 3.5 = Borderline Conference\n\n---\n\n## 升级路径（两位 Reviewer 共识）\n\n**从 3.5 升至 4.0 (Conference accept) 需要**：\n1. ✅ 补充 permutation null → null-adjusted C% 作为 headline（R1 硬性要求）\n2. ✅ 清除 Conclusion causal language（cost: 低）\n3. ✅ 删除/压缩 Section 5.3，释放空间给 Section 5.4 和 multi-subject injection table（cost: 中）\n4. ✅ 报告 IRT model fit statistics（cost: 低）\n5. ✅ Limitations 增加 binary flipping 讨论（cost: 低）\n\n**如果以上 5 项在提交前完成，论文可达 Conference 水平。** 其中 #1（permutation null）是最关键的——这是唯一需要新实验的项目，其余为写作调整。\n\n---\n\n## 给 Research Director 的建议\n\n1. **Permutation null 是唯一的 blocking experiment**：1,000 次 permutation 计算成本低，应优先执行。结果可能会降低 headline 数字（从 31% 到 ~26%），但也可能确认 31% 是 robust 的——无论哪种结果都加强论文。\n\n2. **写作调整（MF-2, SF-2, SF-3, SF-5）可在 1 天内完成**：causal language 替换、Section 5.3 压缩、multi-subject injection table 添加、Limitations 扩展。\n\n3. **Venue positioning**：R1 倾向 Findings accept，R2 认为 borderline Conference。如果 permutation null 确认 effective DIF 仍 >25%，且写作调整完成，Conference accept 是可能的。\n\n4. **截止日期 May 25 AoE**：距提交 4 天。Permutation null + 写作调整在时间上可行。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "force_resubmit": "True",
    "report": "# 最终审稿报告 — Convergence Round (Final)\n\n**论文**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n**截止日期**: 2026-05-25 AoE\n**日期**: 2026-05-21\n**审稿流程**: Round 5 (fresh) → Round 6 (revised) → Round 7 (convergence, final)\n\n---\n\n## ⚠️ 版本一致性说明\n\n两位 Reviewer 均标记了 Director brief 与实际 PDF 之间的内容差异。**两位 Reviewer 均基于实际 PDF 内容评审**，其评分和判断可信。实际论文包含 ~60 references、7 experiment sections (§4.1-4.7)、4 段 Related Work、ΔTPR=+0.508 at p=0.5。本报告基于 Reviewer 对实际 PDF 的评估。\n\n---\n\n## Summary\n\n本文将 Mantel-Haenszel DIF 分析大规模应用于 LLM benchmark 评估（5,227 models × 12,508 MMLU items），发现 31.3% items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 DIF，跨 6 个 METABENCH 基准复现（C% = 17.9–31.3%，45–174× 高于随机基线）。修订版做了 4 项显著改进：标题软化、multi-subject injection、LLM-specific challenges 论证、contributions 收紧为 3 个。\n\n经过 3 轮审稿（初审、修订版评估、最终收敛），两位 Reviewer 均维持 **Overall 3.5 (Borderline Conference)**。\n\n---\n\n## Strengths\n\n1. **大规模、系统的 confound 控制**：5 种 cohort design × 6 种替代解释 × 4 个 threshold sensitivity 点。Matched-ability 分析收敛于 ~28-29% 的 floor（跨不同比较），Soundness 获两位 Reviewer 高评（R1: 4.0, R2: 3.5）。\n\n2. **Cross-subject matching 是最强贡献**（R1+R2 共识）：Proposition 1（properly scoped to single-subject）+ multi-subject boundary（ΔFPR < 0.007 for k ≤ 5, degradation at k = 10）。ΔFPR < 0.001 vs. within-subject +0.19 的对比令人信服。这是 reusable methodological infrastructure。\n\n3. **Ground truth meta-critique 有社区价值**：enrichment = 0.964, Jaccard = 0.206, φ = 0.012 表明 DIF flags 与 web-overlap labels 近乎独立。这对 contamination detection 文献的 evaluation methodology 有直接影响。\n\n4. **LLM-specific methodological adaptations**：新增 \"LLM-specific challenges\" 节（§3.2）讨论 deterministic responses violating local independence, bimodal ability distribution, MMLU multidimensionality——非泛泛之谈，每个点有具体应对措施。\n\n5. **Cross-benchmark replication at scale**：6 个 METABENCH benchmarks（27,125 items），knowledge/reasoning C% ≥ 26.9% > procedural C% ≤ 18.9%，每个都 45-174× 高于 random baseline。\n\n6. **修改响应质量高**：Round 1 的 3 个 critical issues 均有实质性回应（title 改善、Proposition 1 限定、multi-subject boundary、Claim 4 降级、Related Work 扩充至 ~60 refs）。R1 明确肯定\"Round 1 → Round 2 的修改是认真且有效的\"。\n\n---\n\n## Weaknesses\n\n### Must-Fix（阻止升至 4.0 的硬性问题）\n\n**MF-1** [critical, R1 primary concern] **缺少 permutation null——headline 31.3% 无 principled baseline**\n- Random-split (0.18%) 是 perfect null（同一 cohort 内部），但不代表 realistic null。随机打乱 2023/2024 cohort labels 1,000 次后的 permutation null C% 才是正确 baseline comparator。如果 permutation null ~5%，则 effective temporal DIF ~26%，headline 需调整。这直接影响标题中的 \"31%\" 和所有下游分析。\n- **R1 最终评估中最重要的新发现**。R2 未独立提出但未反对。\n- 建议：补充 1,000 次 permutation null，报告 null distribution mean + 95th percentile，计算 null-adjusted C%。计算成本很低。\n\n**MF-2** [critical, residual] **Causal language 残余**\n- 标题已改善（\"Temporal Measurement Drift\" 替代 \"Psychometric Instability\"），但 Conclusion 仍说 \"driven by item properties\"。\"Driven by\" 暗示因果方向，数据只支持 association。\n- R1+R2 共识。\n- 建议：\"driven by\" → \"associated with\"；全文检查 causal-leaning 措辞。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning, consensus] **Binary flipping 的 ecological validity 局限**\n- Uniform rate p 的 incorrect → correct 翻转模拟 \"perfect contamination\"，真实 contamination 更微妙（partial memorization, reasoning shortcuts, format-specific advantages）。ΔTPR = +0.508 at p = 0.5 是 meaningful 但建立在极端 injection 上。\n- R2 补充 defense：cross-subject matching 消除 FPR inflation 的 validity 不依赖 injection 的 ecological validity。\n- 建议：Limitations 中讨论 binary flipping 简化和 non-uniform injection sensitivity。\n\n**SF-2** [warning, consensus] **Section 5.3 GSM1K N=33 仍占过多篇幅**\n- 已从 contribution 降为 Discussion——正确。但仍以 2 段展开。R1 指出 negative correlation 暗示 DIF-flagged items 对 contaminated models 更难——与 \"DIF 检测 contamination\" 叙事矛盾。\n- 建议：压缩为 1-2 句 exploratory note，释放空间给 practical recommendations 和 multi-subject injection 展示。\n\n**SF-3** [warning, improved but still insufficient] **Practical recommendations**\n- 修订版已扩展为 graduated thresholds（<15% monitor, 15-25% flag, >25% act）——有改善。但仍缺 integration workflow、threshold justification、tooling 建议。\n- 建议：进一步扩展，特别是与 BHI/Growing Pains 的集成。\n\n**SF-4** [warning, new in Round 7] **IRT model fit statistics 未报告**\n- 论文使用 2PL 参数做 power analysis 但不报告 fit statistics（CFI, RMSEA, |Lz|）。MH-DIF 不依赖 IRT fit（论文正确指出），但 transparent reporting 要求至少呈现。\n- 建议：报告 fit statistics，即使结论不变。\n\n**SF-5** [warning, consensus] **Multi-subject injection 结果展示过于压缩**\n- k∈{1,3,5,10,20} 的 ΔFPR 数据仅占 1.5 句 inline text。这是回应 Round 5 核心批评的关键实验，应以 table/figure 呈现。\n\n**SF-6** [warning] **Claim 2 framing 微调**\n- 更准确的表述：\"DIF and contamination detection measure fundamentally different constructs\"，而非 \"web-overlap labels fail to validate DIF\"。可补充 4 象限 item characteristic analysis。\n\n**SF-7** [warning] **Bootstrap CI 不对称性原因未讨论**\n\n**SF-8** [warning] **Growing Pains overlap 分析仍缺**（\"Empirical comparison awaits public release\" 合理但仍无定量数据）\n\n**SF-9** [warning] **DIF 术语 running example**：修订版已添加 formal-logic item 示例（α_MH=0.42, Δ_MH=2.04）——✅ 已回应。\n\n---\n\n## Reviewer Consensus (Final)\n\n**完全一致的判断**：\n1. Cross-subject matching 是最强贡献\n2. 论文对 Round 1 反馈的回应质量高\n3. Permutation null 缺失是方法论硬伤（R1 主推，R2 不反对）\n4. GSM1K N=33 证据不足\n5. Binary flipping 是 simplification\n6. Overall 3.5 (Borderline Conference)\n\n**分歧（已通过交叉回应缩小）**：\n| 维度 | R1 | R2 | 差异来源 |\n|------|-----|-----|---------|\n| Soundness | 4.0 | 3.5 | R1 更重视 confound 控制系统性 |\n| Excitement | 3.0 | 3.5 | R1 采纳 novelty ceiling 下调；R2 认为 transplant 质量弥补 |\n| Reproducibility | 4.0 | 4.0 | 一致 |\n| Clarity | 3.5 | 4.0 | R1 认为 space allocation uneven |\n| Overall | 3.5 | 3.5 | **一致** |\n\nR1 建议 venue positioning: **Findings accept, with path to Main if permutation null added**。\nR2 维持 **Borderline Conference，若 GSM1K + practical recommendations 解决可升至 4.0**。\n\n---\n\n## Questions to Authors\n\n1. **Permutation null**：将 cohort labels 随机打乱 1,000 次，每次重新计算 C%——permutation null distribution 的 mean 和 95th percentile 是多少？null-adjusted C% 是否改变 headline？\n2. **IRT model fit**：MMLU 12,508 items 在 2PL 下的 CFI、RMSEA、|Lz| person-fit 分布是什么？\n3. **Multi-subject injection boundary**：如果 real-world contamination 同时影响 >5 subjects（如 model 训练时 ingest 了整个 MMLU dataset），如何论证真实 contamination pattern 落在 k ≤ 5 的安全区间内？\n4. **Claim 2 四象限分析**：web-contaminated × DIF-flagged 的 2×2 中，各象限的 item characteristics（difficulty, discrimination, subject distribution）是否有 systematic pattern？\n\n---\n\n## Missing References\n\n修订版已全面补充：BHI, Benchmark², ATLAS, MedIRT, 加上原有的 DIF methodology 和 IRT-for-LLM 文献。R1 确认当前版本 Related Work \"adequate\"（~44 unique citations in §2, ~60 total）。仅需确认 orphan bib entries 已清理。\n\n---\n\n## External Review\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\nRound 5 时完成：2 warnings（pages 3-5 visual gap, 仅 4 display items in 8 pages）, 7 info。修订版可能已改变布局。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4.0 | 3.5 | 3.75 |\n| Excitement | 3.0 | 3.5 | 3.25 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Clarity | 3.5 | 4.0 | 3.75 |\n| **Overall** | **3.5** | **3.5** | **3.5** |\n\n**置信度**: 4/5\n\n**EMNLP 2026 评分映射**: 3.5 = Borderline Conference\n\n---\n\n## 升级路径（两位 Reviewer 共识）\n\n**从 3.5 升至 4.0 (Conference accept) 需要**：\n1. ✅ 补充 permutation null → null-adjusted C% 作为 headline（R1 硬性要求）\n2. ✅ 清除 Conclusion causal language（cost: 低）\n3. ✅ 删除/压缩 Section 5.3，释放空间给 Section 5.4 和 multi-subject injection table（cost: 中）\n4. ✅ 报告 IRT model fit statistics（cost: 低）\n5. ✅ Limitations 增加 binary flipping 讨论（cost: 低）\n\n**如果以上 5 项在提交前完成，论文可达 Conference 水平。** 其中 #1（permutation null）是最关键的——这是唯一需要新实验的项目，其余为写作调整。\n\n---\n\n## 给 Research Director 的建议\n\n1. **Permutation null 是唯一的 blocking experiment**：1,000 次 permutation 计算成本低，应优先执行。结果可能会降低 headline 数字（从 31% 到 ~26%），但也可能确认 31% 是 robust 的——无论哪种结果都加强论文。\n\n2. **写作调整（MF-2, SF-2, SF-3, SF-5）可在 1 天内完成**：causal language 替换、Section 5.3 压缩、multi-subject injection table 添加、Limitations 扩展。\n\n3. **Venue positioning**：R1 倾向 Findings accept，R2 认为 borderline Conference。如果 permutation null 确认 effective DIF 仍 >25%，且写作调整完成，Conference accept 是可能的。\n\n4. **截止日期 May 25 AoE**：距提交 4 天。Permutation null + 写作调整在时间上可行。"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-21T17:55:41.985695+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-21T17:55:48.922617+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Round 5 初始报告', 'status': 'completed', 'activeForm': 'Round 5 报告已提交'}, {'content': 'Round 6 修订版报告', 'status': 'completed', 'activeForm': 'Round 6 报告已提交'}, {'content': 'Round 7 最终收敛报告', 'status': 'completed', 'activeForm': 'Round 7 最终报告已提交'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Round 5 初始报告', 'status': 'completed', 'activeForm': 'Round 5 报告已提交'}, {'content': 'Round 6 修订版报告', 'status': 'completed', 'activeForm': 'Round 6 报告已提交'}, {'content': 'Round 7 最终收敛报告', 'status': 'completed', 'activeForm': 'Round 7 最终报告已提交'}]"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-21T17:55:48.923060+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 204 · 2026-05-21T17:55:55.420478+00:00_

最终审稿报告已提交。

**总结**：经过 3 轮审稿（初审 → 修订版评估 → 最终收敛），两位 Reviewer 均维持 **Overall 3.5 (Borderline Conference)**。

**核心判断**：
- 论文对 Round 1 反馈的修改质量高（标题软化、multi-subject injection、LLM-specific challenges、contribution 重组）
- 升至 4.0 的关键阻碍：**(1) 缺少 permutation null**（唯一需要新实验的项目）和 **(2) Conclusion 中残余的 causal language**
- 升级路径清晰：permutation null + 5 项写作调整，在 May 25 截止前可完成

Issue tracker 已同步更新（2 critical open, 8 warning open, 6 resolved）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 25

## Round 25

40 recorded events


### User

_source line 205 · 2026-05-21T18:41:12.369661+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main/Findings unified)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-21T18:41:19.148887+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-21T18:41:19.350393+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-21T18:41:25.778225+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-21T18:41:25.778951+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-21T18:41:29.645136+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-21T18:41:29.645621+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-21T18:41:32.658104+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-21T18:41:32.758992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-21T18:41:38.432461+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-21T18:41:40.394948+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1962
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-21T18:41:40.395492+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-21T18:41:41.399301+00:00_

-rw-r--r-- 1 ubuntu ubuntu 577656 May 21 18:30 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu    809 May 21 15:42 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-21T18:41:41.399637+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-21T18:41:41.801459+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines submission format page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines submission format page limit"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-21T18:41:47.324618+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found some information related to EMNLP 2026, though the main conference call for papers
…[truncated 1201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5924
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-21T18:41:49.432771+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines submission format page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here's information about ACL Rolling Review 2026 author guidelines, submission format, and page limits:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. For short papers, the page limit would be correspondingly shorter (typically 4 pages based on standard ACL practices).

Additionally, final versions of accept
…[truncated 1250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 7631
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-21T18:42:00.324435+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline commitment deadline 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline commitment deadline 2026"
  }
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-21T18:42:00.324843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclrollingreview.org \"May 2026\" OR \"June 2026\" submission deadline cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclrollingreview.org \"May 2026\" OR \"June 2026\" submission deadline cycle"
  }
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-21T18:42:00.425902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-21T18:42:00.528208+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Drift in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-21T18:42:05.401585+00:00_

Web search results for query: "site:aclrollingreview.org "May 2026" OR "June 2026" submission deadline cycle"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about ACL Rolling Review (ARR) submission deadlines. The search results indicate that in August 2026, there is a submission deadline listed, with dates including June 29, July 7-July 13, July 30, and August 2.

However, the search results don't contain specific information about a May 2026 or June 2026 submission deadline cycle on the ACL Rolling Review website. The most recent detailed cycle information I found references the January 2026 cycle and August 2026 cycle.

For the most current and comprehensive ARR submission deadlines and cycles, I'd recommend visiting the official ACL Rolling Review dates page directly at http://aclrollingreview.org/dates, which appears to have a full schedule of submission deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5076
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-21T18:42:05.803840+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline commitment deadline 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the key EMNLP 2026 submission and commitment deadlines:

**ARR Submission Deadline:**
The ARR submission deadline for long and short papers is May 25, 2026.

**EMNLP Commitment Deadline:**
The EMNLP commitment deadline is August 2, 2026.

**Additional Important Dates:**
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- Notification of acceptance: August 20, 2026
- Camera-read
…[truncated 424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5479
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-21T18:42:12.230049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-21T18:42:12.883184+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf (564.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-21T18:42:12.900310+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-21T18:42:14.106179+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-21T18:42:14.156911+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/project_config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/project_config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-21T18:42:14.257799+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-21T18:42:23.293850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "pages": "11-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "pages": "11-20"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-21T18:42:23.596253+00:00_

PDF pages extracted: 3 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf (564.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-21T18:42:23.605083+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-21T18:42:23.656043+00:00_

# Review Issues Tracker — irt_equated_bench_regen
# Final convergence: Round 7 (2026-05-21)
# R1 + R2 both at Overall 3.5 (Borderline Conference)
# Action Matrix dispatched to Paper Agent as P28 (2026-05-21)

# ============================================================
# CRITICAL ISSUES (in_progress — P28 dispatched)
# ============================================================

- id: "R1-W1"
  summary: "Causal language 残余——Conclusion 中 'driven by' 等措辞暗示因果方向，数据只支持 association"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 7
  mentions:
    - round: 5
      reviewers: [1, 2]
      note: "标题 'Psychometric Instability' 过强"
    - round: 6
      reviewers: [1, 2]
      note: "标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language"
    - round: 7
      reviewers: [1, 2]
      note: "R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。R2 同意。"
  action_items:
    - round: 7
      action: "替换 Conclusion 中 'driven by' → 'associated with'；全文检查 causal-leaning 措辞"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R7-N1"
  summary: "缺少 permutation null——headline 31.3% 缺乏正确 baseline comparator"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 7
  last_seen_round: 7
  mentions:
    - round: 7
      reviewers: [1]
      note: "R1 最终评估中最重要的新发现。random-split (0.18%) 是 perfect null，不代表 realistic null。"
  action_items:
    - round: 7
      action: "补充 permutation null（200 次 label shuffle）到 §4.2"
      assigned_to: paper_agent
      status: in_progress
  resolution: "plan_029 ran 200 permutations: null mean=0.10%±0.12%, range=[0.01%,1.14%], 0/200 exceed observed, p=0.005. Data integrated into P28."
  resolution_round: null

# ============================================================
# WARNING ISSUES (in_progress — P28 dispatched)
# ============================================================

- id: "R5-N1"
  summa
…[truncated 6613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-21T18:43:11.243601+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-21T18:43:31.174445+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19930
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-21T18:43:32.583591+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（via ACL Rolling Review）\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references。Limitations 和 ethical considerations 不计入页数\n- **模板**: ACL template，`[review]` 模式\n- **匿名规则**: Double-blind（论文中不得出现作者信息）\n- **ARR 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文路径\n- TeX: `projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`\n\n## 你的审查侧重\n\n**重点关注以下维度**：\n\n1. **MH-DIF 方法论**：\n   - Mantel-Haenszel 程序在 LLM benchmark 场景下的适用性（假设检验：条件独立性、局部独立性在 LLM 数据中是否成立？）\n   - ETS severity classification（A/B/C）的阈值选择是否充分论证？\n   - Cross-subject matching 的 Proposition 1 (ΔFPR=0) 证明是否完备？边界条件是否充分讨论？\n\n2. **Semi-synthetic injection framework**：\n   - Binary response flipping 是否是合理的 contamination 模拟？ecological validity 如何？\n   - 实验设计：exploitation rate p 的选择、seed 数量（5 seeds）是否足够？\n   - Cross-subject vs. within-subject vs. external matching 的比较是否公平？\n\n3. **统计分析**：\n   - Bootstrap CI 的 resampling unit（model-level）和 B=1,000 是否充分？\n   - Benjamini-Hochberg FDR correction 的 q=0.05 选择是否合理？\n   - Permutation test（200 label shuffles）的 power 是否足够？\n   - Simpson's paradox 分析和 logistic regression 的 model specification\n   - Power analysis (Section 4.1) 的 assumptions 和 conclusions\n\n4. **控制实验**：\n   - Random split (0.18%) 作为 null baseline 是否充分？\n   - Ability-quintile 和 within-family comparisons 的设计\n   - Multi-subject injection robustness (k∈{1,3,5,10,20}) 的结果解读\n\n5. **可重复性和透明度**：\n   - IRT model fit（2PL on 57-subject benchmark）的报告是否充分？\n   - 代码和数据可用性\n   - 关键超参数和 design choices 的 sensitivity analysis\n\n请按 ARR 格式输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。对 weaknesses 严格评估，不留情面。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（via ACL Rolling Review）\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references。Limitations 和 ethical considerations 不计入页数\n- **模板**: ACL template，`[review]` 模式\n- **匿名规则**: Double-blind（论文中不得出现作者信息）\n- **ARR 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文路径\n- TeX: `projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`\n\n## 你的审查侧重\n\n**重点关注以下维度**：\n\n1. **MH-DIF 方法论**：\n   - Mantel-Haenszel 程序在 LLM benchmark 场景下的适用性（假设检验：条件独立性、局部独立性在 LLM 数据中是否成立？）\n   - ETS severity classification（A/B/C）的阈值选择是否充分论证？\n   - Cross-subject matching 的 Proposition 1 (ΔFPR=0) 证明是否完备？边界条件是否充分讨论？\n\n2. **Semi-synthetic injection framework**：\n   - Binary response flipping 是否是合理的 contamination 模拟？ecological validity 如何？\n   - 实验设计：exploitation rate p 的选择、seed 数量（5 seeds）是否足够？\n   - Cross-subject vs. within-subject vs. external matching 的比较是否公平？\n\n3. **统计分析**：\n   - Bootstrap CI 的 resampling unit（model-level）和 B=1,000 是否充分？\n   - Benjamini-Hochberg FDR correction 的 q=0.05 选择是否合理？\n   - Permutation test（200 label shuffles）的 power 是否足够？\n   - Simpson's paradox 分析和 logistic regression 的 model specification\n   - Power analysis (Section 4.1) 的 assumptions 和 conclusions\n\n4. **控制实验**：\n   - Random split (0.18%) 作为 null baseline 是否充分？\n   - Ability-quintile 和 within-family comparisons 的设计\n   - Multi-subject injection robustness (k∈{1,3,5,10,20}) 的结果解读\n\n5. **可重复性和透明度**：\n   - IRT model fit（2PL on 57-subject benchmark）的报告是否充分？\n   - 代码和数据可用性\n   - 关键超参数和 design choices 的 sensitivity analysis\n\n请按 ARR 格式输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。对 weaknesses 严格评估，不留情面。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-21T18:43:50.131047+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17547
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-21T18:43:51.036763+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（via ACL Rolling Review）\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references。Limitations 和 ethical considerations 不计入页数\n- **模板**: ACL template，`[review]` 模式\n- **匿名规则**: Double-blind（论文中不得出现作者信息）\n- **ARR 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文路径\n- TeX: `projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`\n\n## 你的审查侧重\n\n**重点关注以下维度**：\n\n1. **新颖性和 contribution 定位**：\n   - 将 MH-DIF 应用于 LLM benchmarks 的 novelty 如何？是直接应用还是有实质性适配？\n   - 三个 contributions（semi-synthetic framework, ground truth meta-critique, temporal measurement drift at scale）是否各自有足够独立价值？\n   - 与 Growing Pains (Habba et al., 2026)、PSN-IRT (Zhou et al., 2026)、BHI (Zhu et al., 2026) 等concurrent work 的区别是否清晰？\n   - 对 EMNLP audience（NLP community）的影响力和相关性如何？\n\n2. **Related Work 覆盖**：\n   - Contamination detection 文献覆盖是否全面？是否遗漏重要工作？\n   - IRT in LLM evaluation 的文献是否充分？\n   - DIF methodology 的教育测量学文献是否恰当引用？\n   - 与 dynamic benchmarks (Kiela et al., 2021; Li et al., 2024a; White, 2025) 的定位是否准确？\n\n3. **叙事结构和可读性**：\n   - Abstract 是否准确反映论文核心发现？信息密度是否合适？\n   - Introduction 的问题定义和 motivation 是否清晰有说服力？\n   - Method → Experiments → Discussion 的逻辑流是否连贯？\n   - Conclusion 是否恰当总结贡献而不 overclaim？\n   - Limitations 是否诚实且覆盖关键局限？\n\n4. **写作质量**：\n   - 术语使用是否一致（DIF/measurement drift/instability 等）\n   - 因果语言 vs 关联语言的使用是否恰当？（论文数据是观察性的，不应暗示因果）\n   - Figure 和 Table 的标题、标注是否自包含？\n   - 数学符号使用是否一致？\n\n5. **格式合规性**：\n   - 正文是否确实在 8 页以内？\n   - 匿名要求是否满足？（检查正文、脚注、acknowledgments）\n   - 引用格式是否符合 ACL 规范？\n   - Limitations section 是否存在且位置正确？\n\n6. **Claims vs Evidence 对齐**：\n   - 每个 claim 是否有充分的实验/统计证据支持？\n   - 是否有 overclaiming（声称超出数据支持范围）？\n   - Discussion 中的 speculative statements 是否标注为推测？\n\n请按 ARR 格式输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。对 weaknesses 严格评估，不留情面。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026（via ACL Rolling Review）\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页 + unlimited references。Limitations 和 ethical considerations 不计入页数\n- **模板**: ACL template，`[review]` 模式\n- **匿名规则**: Double-blind（论文中不得出现作者信息）\n- **ARR 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit\n\n## 论文路径\n- TeX: `projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`\n\n## 你的审查侧重\n\n**重点关注以下维度**：\n\n1. **新颖性和 contribution 定位**：\n   - 将 MH-DIF 应用于 LLM benchmarks 的 novelty 如何？是直接应用还是有实质性适配？\n   - 三个 contributions（semi-synthetic framework, ground truth meta-critique, temporal measurement drift at scale）是否各自有足够独立价值？\n   - 与 Growing Pains (Habba et al., 2026)、PSN-IRT (Zhou et al., 2026)、BHI (Zhu et al., 2026) 等concurrent work 的区别是否清晰？\n   - 对 EMNLP audience（NLP community）的影响力和相关性如何？\n\n2. **Related Work 覆盖**：\n   - Contamination detection 文献覆盖是否全面？是否遗漏重要工作？\n   - IRT in LLM evaluation 的文献是否充分？\n   - DIF methodology 的教育测量学文献是否恰当引用？\n   - 与 dynamic benchmarks (Kiela et al., 2021; Li et al., 2024a; White, 2025) 的定位是否准确？\n\n3. **叙事结构和可读性**：\n   - Abstract 是否准确反映论文核心发现？信息密度是否合适？\n   - Introduction 的问题定义和 motivation 是否清晰有说服力？\n   - Method → Experiments → Discussion 的逻辑流是否连贯？\n   - Conclusion 是否恰当总结贡献而不 overclaim？\n   - Limitations 是否诚实且覆盖关键局限？\n\n4. **写作质量**：\n   - 术语使用是否一致（DIF/measurement drift/instability 等）\n   - 因果语言 vs 关联语言的使用是否恰当？（论文数据是观察性的，不应暗示因果）\n   - Figure 和 Table 的标题、标注是否自包含？\n   - 数学符号使用是否一致？\n\n5. **格式合规性**：\n   - 正文是否确实在 8 页以内？\n   - 匿名要求是否满足？（检查正文、脚注、acknowledgments）\n   - 引用格式是否符合 ACL 规范？\n   - Limitations section 是否存在且位置正确？\n\n6. **Claims vs Evidence 对齐**：\n   - 每个 claim 是否有充分的实验/统计证据支持？\n   - 是否有 overclaiming（声称超出数据支持范围）？\n   - Discussion 中的 speculative statements 是否标注为推测？\n\n请按 ARR 格式输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。对 weaknesses 严格评估，不留情面。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-21T18:43:52.547730+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Assistant

_source line 244 · 2026-05-21T18:44:07.218321+00:00_

Round 1 已启动：
- **Reviewer 1**（方法严谨性 + 实验设计）：已派发 ✓
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已派发 ✓
- **视觉审查 Agent**：已派发 ✓（与 Reviewer 并行，不阻塞审稿）

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 245 · 2026-05-21T18:51:02.729147+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文标题**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models

---

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 方法论扎实、控制实验充分的大规模心理测量学分析，但因果解释力不足和实际影响有限（ρ ≈ 0.997）制约了贡献高度。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法选择合理，控制实验设计全面（随机分裂、能力匹配、族内对比、置换检验），但 LLM 场景下 MH-DIF 假设的适用性论证存在缺口（详见 N1、N2）|
| Excitement | 3/5 | 将心理测量学 DIF 引入 LLM 评估是有意义的跨领域迁移，但 ρ ≈ 0.997 的结果削弱了实际紧迫性，且缺乏因果归因降低了可操作性 |
| Reproducibility | 4/5 | 匿名代码已提供，METABENCH 数据公开，关键超参数（K=5, ETS C 阈值, 5 seeds）均已报告；2PL 参数来源透明 |
| Reviewer Confidence | 4/5 | 熟悉 DIF 方法论和 LLM 评估文献 |

---

## Paper Summary

本文将教育测量学中的 Mantel-Haenszel DIF 分析（配合 ETS 严重程度分类）应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目），发现 2023 vs 2024 模型群体间约 31% 的 MMLU 题目呈现 ETS Category C 级别的时序 DIF。作者开发了跨科目匹配的半合成注入框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标志几乎独立（enrichment ≈ 0.964），揭示了现有污染检测验证方法论中的"类别错误"。分析扩展到全部六个 METABENCH 基准（C% = 17.9–31.3%），同时表明排名稳定性未受影响（ρ ≈ 0.997）。

---

## 主要优势

1. **规模与全面性**：据我所知，这是 LLM 基准上最大规模的 DIF 分析（5,227 模型 × 12,508 题目）。6 个基准的交叉验证增强了发现的可信度。

2. **控制实验设计精良**：随机分裂（0.18%）、能力分位（2.9%）、族内对比（Llama-2 vs 3）、最近邻匹配（Cohen's d ≈ -0.010, C% = 28.9%）、置换检验（200 次，null C% = 0.10%）——多重控制有效排除了方法论伪影。特别是最近邻匹配将能力混淆压缩至 ~2.4 pp，这是很有说服力的。

3. **Ground truth meta-critique 概念清晰**：global exposure vs. differential functioning 的区分（Figure 1）以及 enrichment ≈ 0.964 的实证支持构成了对领域验证方法论的有价值批评。这一贡献独立于 DIF 发现本身。

4. **跨科目匹配的方法论贡献**：Proposition 1 在构造上保证 ΔFPR = 0，多科目注入的梯度退化实验（Table 4: k ≤ 5 时 ΔFPR < 0.007）提供了实用边界。

5. **诚实的局限性**：论文明确承认 MH-DIF 只检测 uniform DIF、无法确定因果、二值翻转注入是最坏情况模拟。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DIF 的因果可解释性不足，核心发现的解读空间过大
- 具体位置：Section 1 (line 15-16 of introduction.tex), Section 5, Limitations
- 问题：论文反复承认 MH-DIF 检测到题目功能差异但无法归因（"the signal may reflect contamination, capability change, or training methodology shifts"）。然而 31% 的核心发现如果主要由真实能力提升驱动（2024 模型在特定类型题目上的真实进步），则 DIF 只是在重新发现能力变化而非测量漂移。论文的 Simpson's paradox 分析（Section 4.2: aggregate OR = 1.55 vs controlled OR = 0.73）和 item-level regression（92.4% item-specific）试图排除这一解释，但 item-level specificity 本身并不排除 item-level 的真实能力提升——如果 2024 模型在形式逻辑方面系统性进步，这会在形式逻辑题目上产生 item-specific DIF，但这是能力变化而非测量伪影。
- 为什么影响接收：论文标题使用 "Measurement Drift"，隐含的 framing 是这是一个问题（"benchmarks need psychometric monitoring"），但如果 DIF 主要反映真实能力变化，则结论反转——DIF 恰恰说明基准在正常工作，灵敏地捕捉了代际差异。论文需要更明确地处理这一替代解释，而非将其留在 Limitations 中一笔带过。
- 建议修改方向：(a) 提供至少一种操作化的区分方法（如：对 STEM 子集的 DIF 方向与已知训练数据变化的一致性分析）；(b) 在 Discussion 中显式讨论 "DIF as capability change signal" 的可能性及其对论文结论的影响；(c) 考虑将 framing 从 "measurement drift as problem" 调整为 "DIF as diagnostic tool"（论文在某些段落已有此意识但不一致）。

**N2** [critical] 半合成注入框架的生态效度存疑，ΔTPR = +0.508 的实际意义不明
- 具体位置：Section 3.4, Section 4.5, Limitations (line 4)
- 问题：二值翻转注入（incorrect → correct at rate p）模拟的是最极端的均匀污染模式。现实中的污染效应包括部分记忆、推理捷径、格式偏好等，且效应大小因题目而异。论文承认这一点（Limitations: "detection power under such realistic patterns is untested"），但核心数字 ΔTPR = +0.508 at p = 0.5 仍是论文的主要验证指标。在 p = 0.5（50% 的错误答案被翻转为正确）的激进注入下，仅有约一半的注入题目被检出——这一检测力在更现实（更弱）的污染模式下会进一步下降。同时，注入比例固定为 20% 的 ETS-A 题目，未提供对此选择的 sensitivity analysis。
- 为什么影响接收：半合成验证是 Contribution 1，也是支撑 cross-subject matching 和 ground truth meta-critique 的基础。如果验证框架本身的外部效度有限，则论文的方法论贡献的可推广性受损。
- 建议修改方向：(a) 添加至少一种更现实的注入模式（如：difficulty-dependent exploitation rate, 其中简单题目的翻转概率高于困难题目）；(b) 报告 20% 注入比例的 sensitivity analysis（10%, 30%, 50%）；(c) 更谨慎地 frame ΔTPR = +0.508 的含义——明确这是 upper-bound sensitivity 而非 expected performance。

**N3** [critical] Within-subject C% = 38.1% 高于主分析 31.3%，解释不充分
- 具体位置：Section 4.4 (experiments.tex line 54), Table 2, Appendix B (line 29-31)
- 问题：如果 DIF 是真实的时序效应，per-subject 分析（控制了多维性）应该给出更干净的估计。但 within-subject C% = 38.1% 反而更高。论文将此归因于局部依赖（11.3% within-subject 题目对 |Q3| > 0.20），但这一解释有两个问题：(1) 如果局部依赖膨胀了 within-subject DIF，那 within-subject 分析就不是 "控制了多维性" 的可靠估计；(2) cross-subject matching 被声称能解决此偏差，但 cross-subject matching 的主分析（31.3%）仍低于 within-subject（38.1%），说明存在未被完全解释的方差来源。Appendix B 提到 "the cross-subject matching protocol addresses this bias, and temporal C% persists under external matching"，但未给出 external matching 的具体 C% 数字来支撑这一声称。
- 为什么影响接收：Table 2 的 Structural Analysis 是论文的核心论据之一。Within-subject 结果与论文叙事（31% 是稳健的 lower bound）不一致，undermines 对多维性混淆的控制。
- 建议修改方向：(a) 提供 external matching 的具体 C%（如 MMLU DIF using GSM8K total score as matching variable）；(b) 更详细地分解 within-subject C% 膨胀的来源（多少归因于 LD，多少归因于样本量差异，多少归因于 stratum homogeneity）；(c) 明确论文推荐的 "best estimate" 是 31.3%（cross-subject）还是 28.9%（最近邻匹配），并解释差异。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 置换检验仅 200 次洗牌，分辨率有限
- 具体位置：Section 4.2 (experiments.tex line 16)
- 问题：200 次标签洗牌的最小可报告 p 值为 1/200 = 0.005。论文报告 p = 0.005（0/200 exceed observed），但这是该设置下的分辨率下限而非精确 p 值。真实 p 值可能远小于 0.005。考虑到 null C% = 0.10% vs observed 31.3%（差 ~310倍），增加到 1,000-10,000 次洗牌几乎不增加计算成本，但能提供更精确的 p 值。
- 建议：增加到 ≥1,000 次洗牌并报告更精确的 p 值；或在论文中明确说明 "p ≤ 0.005 (resolution limit of 200 permutations)"。

**W2** [warning] Proposition 1 形式化程度与实际内容不匹配
- 具体位置：Section 3.4 (method.tex lines 50-53)
- 问题：Proposition 1 被格式化为数学命题，但实际内容是一个构造性定义的直接推论：如果匹配变量 M_i^{(-s)} 排除了科目 s 的题目，那注入 s 的污染不改变 M_i^{(-s)}——这在定义层面就是 trivially true。将其包装为 Proposition 提升了读者对 "证明" 深度的期望，但实际只是重述定义。此外，Proposition 仅覆盖 single-subject injection，而论文的主要发现涉及跨 57 个科目的全局 DIF，两者之间的 gap 未被正式分析。
- 建议：降格为 Remark 或将其融入正文叙述；或补充一个更有实质内容的理论结果（如：给出 multi-subject injection 下 ΔFPR 的上界表达式，而非仅靠 Table 4 的经验值）。

**W3** [warning] Bootstrap CI 的重采样单位（model-level）忽略了家族内相关性
- 具体位置：Section 4.2 (experiments.tex line 14)
- 问题：Bootstrap CI [29.4%, 38.1%] 使用 model-level 重采样（B = 1,000），但模型族内成员（如 Llama-2 的多个微调变体）高度相关。论文在 Structural Analysis 中通过 graduated de-duplication 分析了家族效应（K=10: 22.7%, K=20: 29.1%），但 bootstrap 过程未考虑这一聚类结构。有效样本量可能远小于 5,227，导致 CI 低估真实不确定性。CI 的右偏（上限 38.1% vs 下限 29.4%）也暗示少数高 C% 科目驱动了分布尾部。
- 建议：补充 cluster bootstrap（以模型族为重采样单位）的 CI；或至少报告 de-duplicated 数据集（K=20, N ≈ 29.1%）上的 bootstrap CI。

**W4** [warning] Simpson's paradox 中 logistic regression 模型规格未完整报告
- 具体位置：Section 4.2 (experiments.tex line 18)
- 问题：论文报告 aggregate OR = 1.55 (p = 0.001) 反转为 controlled OR = 0.73 (p = 0.030)，但未完整报告 logistic regression 的模型变量。"controlling for item difficulty and discrimination" 中 difficulty 和 discrimination 是如何操作化的（IRT 2PL 参数 a, b？还是 proportion correct 和 point-biserial？），是否考虑了交互项，这些对 OR 的方向和大小有直接影响。Section 4.4 提到 "logistic regression DIF confirms 92.1% concordance with MH and reveals additional non-uniform DIF (24.8%)"，但 concordance 的定义和 non-uniform DIF 的判定标准也未报告。
- 建议：在 Appendix 中提供完整的 logistic regression model specification（因变量、自变量、交互项、拟合统计量）。

**W5** [warning] Power Analysis 使用平均 2PL 参数而非参数分布
- 具体位置：Section 4.1 (experiments.tex lines 8-9)
- 问题：Monte Carlo power analysis 使用 PSN-IRT 的平均参数（ā = 1.2, b̄ = -0.84）。但 DIF 检测力高度依赖个别题目的区分度（a 参数）——高区分度题目更容易被检出。使用平均值掩盖了参数分布对 power 的影响。论文应说明 a 和 b 的分布（至少报告 SD），并展示 power 如何随 a 参数变化。
- 建议：补充参数分布的描述统计；展示 power curve 在不同 a 值区间的变化；或使用参数的完整经验分布而非均值进行 power analysis。

**W6** [warning] GSM1K 相关性分析统计效力不足
- 具体位置：Section 4.7 (experiments.tex line 108)
- 问题：GSM1K 分析仅有 N = 33 个模型，报告 r = -0.478, p = 0.005。此样本量下，一个异常值就可能大幅改变相关系数。论文正确标注为 "exploratory"，但仍在 Section 4.7 主体中报告且在 Appendix 提供了图表，给读者的印象是支撑性证据。对于 N = 33 的相关分析，应至少报告 bootstrapped CI 和 robust correlation（如 Spearman 或 rank-based）。
- 建议：降低此分析的权重（如移至 Appendix 并明确标注 "preliminary"）；补充 robust correlation 和 bootstrapped CI；或干脆移除，避免给读者过度解读的空间。

---

## 小问题（不影响接收）

1. **Table 2 列名歧义**：列名 "Temp. FPR" 在这里实际指的是 temporal C%（因为 FPR 通常指 false positive rate），但 C% 本身是 DIF 检出率而非传统意义的 FPR。这一命名可能引起混淆。

2. **Abstract 信息密度过高**：Abstract 包含大量数字（ΔFPR = 0.000, ΔTPR = +0.508, enrichment ≈ 0.96, φ = 0.012, 5,227 models, 27,125 items, 17.9–31.3%, 45–174×, C% ≥ 26.9%, C% ≤ 18.9%, ρ ≈ 0.997, z = -8σ to -49σ, 92.4%, ρ = -0.597）。建议精简至核心数字。

3. **引用验证**：verify_references 工具检出 9 个 "not_found"（多为近期 preprint，OpenAlex 尚未收录，如 Liang 2026 DVD, Kipnis 2024 metabench, Qian 2026 Benchmark² 等），以及 Holland 1988 年份可能为 1986 的 mismatch。建议核实 Holland & Thayer 原始出版年份。

4. **p = 0.1 缺失**：Method Section 3.4 的注入实验跳过了 p = 0.1 这个可能更现实的低注入率点。Figure 2 的 dose-response 曲线在 p = 0 和 p = 0.3 之间缺少数据点，无法判断低注入率下的检测灵敏度。

5. **页数合规**：主文 8 页 + References + Limitations + Appendix，符合 EMNLP 2026 long paper 要求。

6. **匿名性**：未发现作者身份信息，footnote 使用匿名仓库链接。合规。

---

## Questions for Authors

Q1: 如果将 DIF 方向（favoring 2023 vs 2024）与已知的训练数据变化（如 2024 模型更多使用 instruction tuning / RLHF）进行对照，是否能提供因果归因的初步证据？论文已有 STEM vs Humanities 方向差异的描述性发现（Section 4.2），但未尝试与训练方法论变化进行系统对应。

Q2: 论文推荐的 C% action threshold（15%, 25%）基于什么依据？ETS 的原始阈值是为教育测试设计的，直接迁移到 LLM 评估场景的合理性需要论证。

Q3: 如果在 2023 cohort 内部按半年分裂（2023-H1 vs 2023-H2），C% 是多少？Section 4.7 提到 2023-H2 vs 2024-H1 的 C% = 34.35%，但 2023 年内的基线变化率会帮助理解时序 DIF 的累积速度。

Q4: Cross-subject matching 在 MMLU 上排除了当前科目的题目，但 57 个科目中部分科目高度相关（如多个 STEM 子科目）。如果污染集中在相关科目群中，M_i^{(-s)} 仍会部分吸收污染信号。是否分析了科目间相关性对 Proposition 1 的影响？

Q5: 论文的 IRT 模型拟合报告（Appendix A.2）提到 MMLU "shows poor fit to a unidimensional 2PL model"。Power analysis（Section 4.1）使用的 2PL 参数是否因 model misfit 而不可靠？如果参数估计有偏，基于这些参数的 power analysis 结论的可信度如何？

---

## Missing References

1. **DIF in computerized adaptive testing**: 论文可能受益于讨论 CAT 场景下的 DIF 检测（如 Lei & Li, 2003; Zwick, 2012），因为 LLM 评估的高样本量和题目池大小更接近 CAT 而非传统纸笔测试。

2. **MMLU-Pro / MMLU-Redux**: 论文使用原始 MMLU，但未讨论 MMLU-Pro (Wang et al., 2024) 和 MMLU-Redux (Gema et al., 2024) 等修订版是否缓解了部分 DIF——这与论文的 "retire flagged items" 建议直接相关。

3. **Measurement invariance in cross-cultural testing**: DIF 文献中 temporal groups 类比于 cross-cultural groups 的讨论（如 Byrne et al., 1989）可以加强论文的理论基础。

---

## Overall Assessment

**评分: 3.5 (Borderline Conference)**

本文将经典心理测量学方法（MH-DIF）成功迁移到 LLM 基准评估场景，规模大、控制实验设计全面、写作清晰。31% 的时序 DIF 发现和 ground truth meta-critique 对 LLM 评估社区有参考价值。

主要顾虑：(1) 因果不可解释性使核心发现的解读空间过大——"measurement drift" 可能只是 "capability change" 的另一种说法；(2) 半合成注入框架的生态效度有限，是否能推广到真实污染模式存疑；(3) within-subject C% 高于主分析且解释不充分，动摇了多维性控制的可信度。若能在 rebuttal 中提供因果归因的初步证据（如 Q1）并补充 within-subject 膨胀的详细分析，评分可上调至 4.0。

**Confidence: 4/5**（对 DIF 方法论和 LLM 评估文献较为熟悉，对 IRT model fit 的技术细节可能存在遗漏）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 246 · 2026-05-21T18:51:13.819138+00:00_

Reviewer 1 审稿意见已收到（3.5/5 Borderline Conference）。核心问题集中在：因果解释力不足（N1）、半合成注入生态效度（N2）、within-subject C% 膨胀解释（N3）。

等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 27

## Round 27

6 recorded events


### User

_source line 247 · 2026-05-21T18:51:14.904211+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论扎实、实验规模可观的 psychometric audit，但核心贡献是将标准 DIF 方法直接应用于新领域，novelty 有限，且 "measurement drift" 的 framing 与实际证据之间存在张力。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims 有充分控制实验支撑（random split, permutation test, matched-ability ablation），但 Proposition 1 是 tautological 的，Table 2 混淆了 C% 与 FPR 概念，"drift" framing 超出两个时间点观测数据的支撑范围 |
| Excitement | 3/5 | MH-DIF 是 1988 年的标准方法，适配工作（cross-subject matching）在 psychometric 文献中已有先例；concurrent work 密集（Growing Pains, PSN-IRT, BHI）；实际影响有限（ρ ≈ 0.997） |
| Reproducibility | 4/5 | 提供匿名代码链接；数据基于公开 METABENCH；方法步骤描述清晰；cohort 定义和 ETS 分类标准明确 |
| Overall Assessment | 3.5/5 | Borderline Conference — 实证贡献扎实但 novelty 不足以获得 main conference 的 excitement threshold |
| Confidence | 4/5 | 熟悉 DIF 方法论和 LLM evaluation 文献，仔细读了全部正文和附录 |

---

## 主要优势

1. **规模与严谨性**：5,227 models × 12,508 items 的 DIF 分析，配合 5 种 cohort designs、permutation test（200 shuffles, p=0.005）、1:1 nearest-neighbor matching ablation（C% 从 31.3% 降至 28.9%）、cross-benchmark replication（6 个 benchmarks），实验设计非常 thorough。

2. **Semi-synthetic validation framework 设计合理**：Cross-subject matching 实现 ΔFPR = 0.000 的验证是该 framework 最有价值的部分。多 subject injection 实验（Table 4, k=1→20）清晰展示了 matching variable 完整性的边界条件。

3. **Ground truth meta-critique 有实用价值**：DIF flags 与 web-overlap labels 的 near-independence（enrichment = 0.964, φ = 0.012）是一个重要的 negative result，提醒社区不应将 web-overlap labels 用于验证 item-level differential detectors。

4. **Cross-benchmark replication**：6 个 benchmarks 一致显示 temporal DIF（17.9-31.3%），且 knowledge/reasoning vs procedural 的分化模式一致，增强了 findings 的 robustness。

5. **Limitations 诚实且全面**：covers methodological scope (uniform-only DIF), matching boundary, generalizability。承认 causal decomposition 不可达。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **"Drift" framing 超出数据支撑——两个时间点不能建立趋势**
- 具体位置：Title, Abstract ("Temporal Measurement Drift"), Section 4.2 标题 ("31% Measurement Drift")
- 问题：论文标题和核心 framing 使用 "drift"，但实际只比较了 2023 vs 2024 两个时间点。"Drift" 暗示一个方向性的时序趋势，这需要至少 3 个时间点才能建立。论文实际展示的是一个两组横截面 DIF 比较。Section 4.7 提到 "Even within a 6-month window (2023-H2 vs 2024-H1), DIF remains substantial" —— 但这仍然是另一个两点比较，不是 drift trajectory。
- 为什么影响接收：这是论文的 central framing。如果核心 claim 的措辞超出数据支撑，reviewers 和 ACs 会质疑整体 rigor。
- 建议修改方向：将 "drift" 改为 "temporal DIF" 或 "temporal instability"；或者将 METABENCH 数据按季度切分（如果 sample size 允许）做 3+ 时间点分析来 justify "drift" 一词。

**N2** [critical] **DIF 的 causal interpretation 模糊——"measurement drift" vs "genuine capability change" 未能充分区分**
- 具体位置：Section 4.2 ("STEM items favor 2024 models (55.4%), Humanities favor 2023 (64.4%)"), Section 5.1, Abstract
- 问题：论文反复承认 DIF detects *that* items function differently but not *why*（Limitations paragraph 1）。然而，Section 4.2 的 domain-direction 分析表明 STEM 上 2024 模型表现更好——这完全可能是 genuine capability improvement 而非 "measurement drift"。如果 2024 模型在 STEM reasoning 上有真实提升，那 item characteristic curves 理应发生变化——这是 measurement working correctly，不是 "drift"。论文用 pseudo R² = 0.0007 argue 92.4% of DIF is item-specific，但这只说明 DIF 不归因于 domain-level accuracy gains，不排除 item-level capability changes。
- 为什么影响接收：这是论文 interpretation 的根本问题。如果相当一部分 "temporal DIF" 实际上反映了真实能力变化，那 31% 的数字就被 overclaim 为 problematic "drift"。
- 建议修改方向：明确讨论 "benign DIF"（due to genuine capability change）vs "problematic DIF"（due to contamination or methodological artifacts）的区分。至少对 DIF-C items 做定性分析：这些 items 的内容特征是否与 capability change 一致？

**N3** [critical] **Proposition 1 是 tautological 的，不应以 formal proposition 形式呈现**
- 具体位置：Section 3.4, Proposition 1
- 问题：Proposition 1 说的是：如果 contamination 仅限于 subject s，而 matching variable 排除了 subject s，那么 matching variable 不受影响，因此 ΔFPR = 0。这是 cross-subject matching 定义的直接推论，不需要任何证明。将其格式化为带编号的 Proposition 增加了不应有的形式感。
- 为什么影响接收：使论文看起来在 padding methodological contribution。Reviewers 对 "trivial claims dressed up as theorems" 非常敏感。
- 建议修改方向：将其改为 inline observation 或 remark，不使用 proposition 环境。保留 empirical validation（ΔFPR = 0.000 across 5 domains），那才是真正有说服力的部分。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Table 2 列名 "Temp. FPR" 误导——temporal comparison 没有 ground truth，C% 不是 FPR**
- 具体位置：Table 2 (Section 4.4, experiments.tex line 57-72)
- 问题：Table 2（\ref{tab:structural_comparison}）中 "Temp. FPR" 列实际上报告的是 temporal DIF C%。在 temporal comparison 中，没有 ground truth 定义哪些 items "真正" 有 DIF，因此将 C% 称为 "FPR" 概念上是错误的。只有在 semi-synthetic injection 中才存在 true FPR（因为有 injected ground truth）。
- 建议：将列名改为 "Temp. C%" 以保持术语一致性。

**W2** [warning] **与 Growing Pains 的区分过于依赖 "empirical comparison awaits public release"**
- 具体位置：Section 2, Related Work, IRT in LLM Evaluation paragraph
- 问题：Growing Pains (Habba et al., 2026) 同样使用 IRT 方法处理 LLM benchmark 的 temporal comparability（通过 FPC）。论文声称 "complementary"（DIF 诊断 vs FPC 校准），但区分的深度不足。特别是："empirical comparison awaits public release of anchor item lists" 使得 complementarity claim 无法验证。如果 Growing Pains 的 FPC anchor items 恰好就是 DIF-stable items，那本文的方法论增量就很有限。
- 建议：至少做概念层面的深入对比——FPC 假设 anchor item stability，DIF 检测 anchor item instability。展示如果 anchor items 不 stable 会怎样（DIF 的价值在于 pre-screening anchors），用具体 scenario 论证。

**W3** [warning] **ρ ≈ 0.997 削弱了 practical significance argument**
- 具体位置：Section 4.6, Abstract, Section 5.1
- 问题：论文框架为 "diagnostic, not destructive"，这是合理的 framing。但 ρ ≈ 0.997 意味着即使移除 31% 的 items，model rankings 几乎不变。这引发一个自然的问题：如果 DIF 不影响 ranking 决策，practitioners 为什么要做 DIF audit？论文没有充分回答这个 "so what" 问题。Section 5.3 的 audit protocol（Monitor/Flag/Act）提出当 C% ≥ 25% 时 "rotate or retire flagged items"——但如果 retire 不影响 rankings，动机何在？
- 建议：stronger practical motivation。例如：(a) DIF items 可能在特定模型子集上产生非 negligible 的 ranking shifts（已有 Llama-3 +53 位的数据，可以更深入挖掘）；(b) 未来 DIF 加剧时 ranking robustness 可能下降；(c) DIF 对 fine-grained capability assessment（非 overall ranking）的影响。

**W4** [warning] **Within-family comparison (Llama-2 vs 3) C% = 61.3% 的处理不充分**
- 具体位置：Section 4.2, Table 1
- 问题：论文将 Llama-2 vs Llama-3 的 61.3% C% 解释为 "large ability gaps that confound the DIF signal"。但 ability-matched analysis 将其降至 28.3%，这与 temporal C% matched value (28.9%) 几乎一致。这个 convergence 很有趣但被 under-explored——它可能暗示 ~28-29% 是某种 "floor" DIF rate，不取决于 cohort definition，这会对 31% 数字的 interpretation 产生影响。这到底是 genuine temporal signal 还是 METABENCH 数据本身的某种结构特征？
- 建议：显式讨论 28-29% convergence 的含义；考虑对非 temporal cohorts（如 ability-matched random splits）做同样的分析来区分。

**W5** [warning] **Semi-synthetic injection 的生态效度有限**
- 具体位置：Section 3.4, Limitations paragraph 1
- 问题：Injection 使用 binary response flipping (incorrect → correct)，这是最极端的 contamination 形式。真实 contamination 涉及 partial memorization、reasoning shortcuts、format-specific advantages。Limitations 中已承认这一点，但问题是：ΔTPR = +0.508 at p = 0.5 这个 moderate detection power 是在最极端注入条件下获得的。对于更 realistic 的 contamination patterns，detection power 可能显著更低。
- 建议：至少讨论 partial contamination 模拟的可行性（如 flip probability < 1 for each injected item），即使不做实验。

---

## Questions to Authors

**Q1**: Matched-ability analysis 后 temporal C% = 28.9%，within-family matched C% = 28.3%，ability-quintile C% = 2.9%。如果 28-29% 是某种 "irreducible DIF floor" regardless of cohort definition，这对 "temporal" measurement drift 的 interpretation 有什么影响？你们是否测试过对 2023 cohort 内部做 arbitrary non-random splits（如按 model size）并 match ability 后的 C%？

**Q2**: 92.4% item-specific signal 的 pseudo R² = 0.0007 是基于 domain-level accuracy gains 作为 predictor。如果加入 item-level difficulty change（2024 accuracy - 2023 accuracy per item）作为 predictor，R² 会如何变化？这会帮助区分 "genuine capability change" 和 "measurement drift"。

**Q3**: Discussion Section 5.2 称 BHI (Zhu et al., 2026) "speculative" —— 具体指 BHI 的哪个 component？这个 characterization 是否公平？

**Q4**: Section 4.7 的 GSM1K analysis (N=33) 中 r = -0.478 的 negative correlation 是 exploratory 且 underpowered 的。在 CI 宽到什么程度？是否考虑过 bootstrap CI？

---

## Missing References

1. **Oren et al. (2024)** "Proving Test Set Contamination in Black Box Language Models" (ICML 2024) — 一种重要的 contamination detection 方法，属于 membership inference 类别但使用了不同的统计框架。当前 contamination detection 综述中应该包含。

2. **Deng et al. (2024)** "Investigating Data Contamination in Modern Benchmarks for Large Language Models" — 系统性的 contamination 调查。如果 Li et al. (2024b) 是主要的 web-overlap 参考，其他提供类似 labels 的工作也值得提及以增强 meta-critique 的 generality。

---

## 小问题（不影响接收）

- Abstract 中 "enrichment ≈ 0.96, φ = 0.012" 使用了两个 NLP 读者可能不熟悉的统计量，建议在 abstract 中用更直白的语言辅助解释。
- Section 3.2 中 "ETS recommended practice for large-scale assessments (Donoghue and Allen, 1993; Clauser and Mazor, 1998)" —— Holland 1988 的 bib 年份与 OpenAlex 记录有 mismatch（API 显示 1986），建议核实。
- Conclusion (Section 6) 仅两行，过于简略——虽然不违规，但可以多用 1-2 句 summarize practical implications。
- Figure 5 (page 13) 的 scatter plot 较为 cluttered，trend line 与数据点的关系不够清晰，考虑标注极端点的 model 名称。

---

## 总结

这是一篇实验设计 thorough、规模可观的 empirical paper。将 MH-DIF 应用于 LLM benchmarks 是 timely 且 relevant 的。Semi-synthetic validation framework 和 ground truth meta-critique 有实用价值。

但三个核心问题限制了评分：(1) "drift" framing 超出两点观测数据的支撑；(2) 无法区分 "problematic drift" 和 "genuine capability change" 使 31% 这个数字的 interpretation 存在 fundamental ambiguity；(3) methodological novelty 有限——MH-DIF 是标准方法的直接应用，cross-subject matching 在 psychometric 文献中已有先例。加上 ρ ≈ 0.997 削弱 practical significance，我认为这篇论文处于 Borderline Conference 水平，如果 N1 和 N2 被充分 address 可能达到 Conference，否则更适合 Findings。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**核心判断**：Overall 3.5（Borderline Conference），Soundness 3.5，Excitement 3.0，Reproducibility 4.0。

**三个 Must-Fix 问题**：
1. DIF 的因果可解释性不足——"measurement drift" 和 "capability change" 无法区分，核心发现的解读空间过大
2. 半合成注入框架的生态效度有限——二值翻转是最坏情况，ΔTPR = +0.508 在更现实的污染模式下可能进一步下降，且 20% 注入率未做 sensitivity analysis
3. Within-subject C% = 38.1% 高于主分析 31.3%，对多维性控制的可信度构成挑战，解释不充分

**六个 Should-Fix 问题**涵盖置换检验分辨率（200 次）、Proposition 1 形式化过度、Bootstrap CI 忽略家族聚类、Simpson's paradox logistic regression 模型未完整报告、Power Analysis 使用均值参数、GSM1K N=33 统计效力不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-21T18:51:55.385724+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重新颖性+完整性+写作质量）的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意与你自己审稿意见的异同——对于你已提出类似观点的，请说明是否完全一致或有细微差异。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论扎实、实验规模可观的 psychometric audit，但核心贡献是将标准 DIF 方法直接应用于新领域，novelty 有限，且 \"measurement drift\" 的 framing 与实际证据之间存在张力。\n\n### Must-Fix 问题\n\n**N1** [critical] \"Drift\" framing 超出数据支撑——两个时间点不能建立趋势\n- Title 和 Abstract 使用 \"Temporal Measurement Drift\"，但实际只比较了 2023 vs 2024 两个时间点。\"Drift\" 暗示方向性时序趋势，需要至少 3 个时间点。Section 4.7 的 6-month window 仍是两点比较。建议改为 \"temporal DIF\" 或 \"temporal instability\"；或做 3+ 时间点分析。\n\n**N2** [critical] DIF 的 causal interpretation 模糊——\"measurement drift\" vs \"genuine capability change\" 未能充分区分\n- Section 4.2 的 domain-direction 分析表明 STEM 上 2024 模型更好，这可能是 genuine capability improvement。pseudo R² = 0.0007 只排除 domain-level accuracy gains，不排除 item-level capability changes。建议讨论 \"benign DIF\" vs \"problematic DIF\"，至少对 DIF-C items 做定性内容分析。\n\n**N3** [critical] Proposition 1 是 tautological 的，不应以 formal proposition 形式呈现\n- Cross-subject matching 定义的直接推论，不需要证明。将其格式化为 Proposition 增加不应有的形式感。建议改为 inline observation 或 remark。\n\n### Should-Fix 问题\n\n**W1** [warning] Table 2 列名 \"Temp. FPR\" 误导——temporal comparison 没有 ground truth，C% 不是 FPR\n- 建议改为 \"Temp. C%\"。\n\n**W2** [warning] 与 Growing Pains 的区分过于依赖 \"empirical comparison awaits public release\"\n- 应至少做概念层面深入对比：FPC 假设 anchor stability，DIF 检测 anchor instability。\n\n**W3** [warning] ρ ≈ 0.997 削弱了 practical significance argument\n- 如果 DIF 不影响 ranking 决策，practitioners 为什么要做 DIF audit？Section 5.3 的 audit protocol 动机不足。需要更强的 practical motivation。\n\n**W4** [warning] Within-family comparison (Llama-2 vs 3) C% = 61.3% → ability-matched 28.3%，与 temporal matched 28.9% 的 convergence 被 under-explored\n- ~28-29% 是否是某种 \"irreducible DIF floor\"？这对 31% 的 interpretation 有重要影响。\n\n**W5** [warning] Semi-synthetic injection 的生态效度有限\n- Binary response flipping 是最极端的 contamination 形式。ΔTPR = +0.508 在更 realistic patterns 下可能显著更低。\n\n### Missing References\n1. Oren et al. (2024) \"Proving Test Set Contamination in Black Box Language Models\" (ICML 2024)\n2. Deng et al. (2024) \"Investigating Data Contamination in Modern Benchmarks for Large Language Models\"\n\n---\n\n请对以上每个 N1-N3 和 W1-W5 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重新颖性+完整性+写作质量）的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意与你自己审稿意见的异同——对于你已提出类似观点的，请说明是否完全一致或有细微差异。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论扎实、实验规模可观的 psychometric audit，但核心贡献是将标准 DIF 方法直接应用于新领域，novelty 有限，且 \"measurement drift\" 的 framing 与实际证据之间存在张力。\n\n### Must-Fix 问题\n\n**N1** [critical] \"Drift\" framing 超出数据支撑——两个时间点不能建立趋势\n- Title 和 Abstract 使用 \"Temporal Measurement Drift\"，但实际只比较了 2023 vs 2024 两个时间点。\"Drift\" 暗示方向性时序趋势，需要至少 3 个时间点。Section 4.7 的 6-month window 仍是两点比较。建议改为 \"temporal DIF\" 或 \"temporal instability\"；或做 3+ 时间点分析。\n\n**N2** [critical] DIF 的 causal interpretation 模糊——\"measurement drift\" vs \"genuine capability change\" 未能充分区分\n- Section 4.2 的 domain-direction 分析表明 STEM 上 2024 模型更好，这可能是 genuine capability improvement。pseudo R² = 0.0007 只排除 domain-level accuracy gains，不排除 item-level capability changes。建议讨论 \"benign DIF\" vs \"problematic DIF\"，至少对 DIF-C items 做定性内容分析。\n\n**N3** [critical] Proposition 1 是 tautological 的，不应以 formal proposition 形式呈现\n- Cross-subject matching 定义的直接推论，不需要证明。将其格式化为 Proposition 增加不应有的形式感。建议改为 inline observation 或 remark。\n\n### Should-Fix 问题\n\n**W1** [warning] Table 2 列名 \"Temp. FPR\" 误导——temporal comparison 没有 ground truth，C% 不是 FPR\n- 建议改为 \"Temp. C%\"。\n\n**W2** [warning] 与 Growing Pains 的区分过于依赖 \"empirical comparison awaits public release\"\n- 应至少做概念层面深入对比：FPC 假设 anchor stability，DIF 检测 anchor instability。\n\n**W3** [warning] ρ ≈ 0.997 削弱了 practical significance argument\n- 如果 DIF 不影响 ranking 决策，practitioners 为什么要做 DIF audit？Section 5.3 的 audit protocol 动机不足。需要更强的 practical motivation。\n\n**W4** [warning] Within-family comparison (Llama-2 vs 3) C% = 61.3% → ability-matched 28.3%，与 temporal matched 28.9% 的 convergence 被 under-explored\n- ~28-29% 是否是某种 \"irreducible DIF floor\"？这对 31% 的 interpretation 有重要影响。\n\n**W5** [warning] Semi-synthetic injection 的生态效度有限\n- Binary response flipping 是最极端的 contamination 形式。ΔTPR = +0.508 在更 realistic patterns 下可能显著更低。\n\n### Missing References\n1. Oren et al. (2024) \"Proving Test Set Contamination in Black Box Language Models\" (ICML 2024)\n2. Deng et al. (2024) \"Investigating Data Contamination in Modern Benchmarks for Large Language Models\"\n\n---\n\n请对以上每个 N1-N3 和 W1-W5 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-21T18:52:22.654902+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27269
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-21T18:52:23.558986+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性+实验设计）的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意与你自己审稿意见的异同——对于你已提出类似观点的，请说明是否完全一致或有细微差异。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论扎实、控制实验充分的大规模心理测量学分析，但因果解释力不足和实际影响有限（ρ ≈ 0.997）制约了贡献高度。\n\n### Must-Fix 问题\n\n**N1** [critical] DIF 的因果可解释性不足，核心发现的解读空间过大\n- 31% 如果主要由真实能力提升驱动，则 DIF 只是在重新发现能力变化而非测量漂移。Simpson's paradox 分析和 item-level regression 试图排除但不充分——item-level specificity 不排除 item-level 真实能力提升（如 2024 模型在形式逻辑方面系统性进步会产生 item-specific DIF）。论文需要 (a) 至少一种操作化的区分方法；(b) 显式讨论 \"DIF as capability change signal\"；(c) 统一 framing。\n\n**N2** [critical] 半合成注入框架的生态效度存疑，ΔTPR = +0.508 的实际意义不明\n- 二值翻转模拟最极端的均匀污染模式。在 p = 0.5 的激进注入下仅约一半被检出，更现实的弱污染模式下会进一步下降。注入比例 20% 未做 sensitivity analysis。建议 (a) 添加 difficulty-dependent exploitation rate；(b) 报告 10%/30%/50% 注入比例 sensitivity；(c) 明确 ΔTPR 是 upper-bound。\n\n**N3** [critical] Within-subject C% = 38.1% 高于主分析 31.3%，解释不充分\n- 如果 DIF 是真实时序效应，per-subject 分析应更干净。但 within-subject 反而更高。归因于局部依赖（11.3% |Q3|>0.20）但：(1) 如果 LD 膨胀了 within-subject DIF，则不可靠；(2) cross-subject 31.3% 仍低于 within-subject 38.1%，存在未解释的方差。Appendix B 未给出 external matching 的具体 C%。\n\n### Should-Fix 问题\n\n**W1** [warning] 置换检验仅 200 次洗牌，分辨率有限\n- 最小可报告 p 值为 1/200 = 0.005。建议增加到 ≥1,000 次。\n\n**W2** [warning] Proposition 1 形式化程度与实际内容不匹配\n- 实际是构造性定义的直接推论，trivially true。建议降格为 Remark。\n\n**W3** [warning] Bootstrap CI 的重采样单位（model-level）忽略了家族内相关性\n- 模型族内成员高度相关，有效样本量可能远小于 5,227。建议补充 cluster bootstrap。\n\n**W4** [warning] Simpson's paradox 中 logistic regression 模型规格未完整报告\n- difficulty 和 discrimination 如何操作化？是否有交互项？non-uniform DIF 判定标准未报告。\n\n**W5** [warning] Power Analysis 使用平均 2PL 参数而非参数分布\n- DIF 检测力高度依赖个别题目区分度（a 参数）。应展示 power 随 a 值变化。\n\n**W6** [warning] GSM1K 相关性分析统计效力不足\n- N = 33，一个异常值可能大幅改变结果。建议降低权重或移至 Appendix。\n\n### Missing References\n1. DIF in CAT (Lei & Li, 2003; Zwick, 2012)\n2. MMLU-Pro (Wang et al., 2024) / MMLU-Redux (Gema et al., 2024)\n3. Measurement invariance in cross-cultural testing (Byrne et al., 1989)\n\n---\n\n请对以上每个 N1-N3 和 W1-W6 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性+实验设计）的完整审稿原文。请逐条回应每个 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意与你自己审稿意见的异同——对于你已提出类似观点的，请说明是否完全一致或有细微差异。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论扎实、控制实验充分的大规模心理测量学分析，但因果解释力不足和实际影响有限（ρ ≈ 0.997）制约了贡献高度。\n\n### Must-Fix 问题\n\n**N1** [critical] DIF 的因果可解释性不足，核心发现的解读空间过大\n- 31% 如果主要由真实能力提升驱动，则 DIF 只是在重新发现能力变化而非测量漂移。Simpson's paradox 分析和 item-level regression 试图排除但不充分——item-level specificity 不排除 item-level 真实能力提升（如 2024 模型在形式逻辑方面系统性进步会产生 item-specific DIF）。论文需要 (a) 至少一种操作化的区分方法；(b) 显式讨论 \"DIF as capability change signal\"；(c) 统一 framing。\n\n**N2** [critical] 半合成注入框架的生态效度存疑，ΔTPR = +0.508 的实际意义不明\n- 二值翻转模拟最极端的均匀污染模式。在 p = 0.5 的激进注入下仅约一半被检出，更现实的弱污染模式下会进一步下降。注入比例 20% 未做 sensitivity analysis。建议 (a) 添加 difficulty-dependent exploitation rate；(b) 报告 10%/30%/50% 注入比例 sensitivity；(c) 明确 ΔTPR 是 upper-bound。\n\n**N3** [critical] Within-subject C% = 38.1% 高于主分析 31.3%，解释不充分\n- 如果 DIF 是真实时序效应，per-subject 分析应更干净。但 within-subject 反而更高。归因于局部依赖（11.3% |Q3|>0.20）但：(1) 如果 LD 膨胀了 within-subject DIF，则不可靠；(2) cross-subject 31.3% 仍低于 within-subject 38.1%，存在未解释的方差。Appendix B 未给出 external matching 的具体 C%。\n\n### Should-Fix 问题\n\n**W1** [warning] 置换检验仅 200 次洗牌，分辨率有限\n- 最小可报告 p 值为 1/200 = 0.005。建议增加到 ≥1,000 次。\n\n**W2** [warning] Proposition 1 形式化程度与实际内容不匹配\n- 实际是构造性定义的直接推论，trivially true。建议降格为 Remark。\n\n**W3** [warning] Bootstrap CI 的重采样单位（model-level）忽略了家族内相关性\n- 模型族内成员高度相关，有效样本量可能远小于 5,227。建议补充 cluster bootstrap。\n\n**W4** [warning] Simpson's paradox 中 logistic regression 模型规格未完整报告\n- difficulty 和 discrimination 如何操作化？是否有交互项？non-uniform DIF 判定标准未报告。\n\n**W5** [warning] Power Analysis 使用平均 2PL 参数而非参数分布\n- DIF 检测力高度依赖个别题目区分度（a 参数）。应展示 power 随 a 值变化。\n\n**W6** [warning] GSM1K 相关性分析统计效力不足\n- N = 33，一个异常值可能大幅改变结果。建议降低权重或移至 Appendix。\n\n### Missing References\n1. DIF in CAT (Lei & Li, 2003; Zwick, 2012)\n2. MMLU-Pro (Wang et al., 2024) / MMLU-Redux (Gema et al., 2024)\n3. Measurement invariance in cross-cultural testing (Byrne et al., 1989)\n\n---\n\n请对以上每个 N1-N3 和 W1-W6 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-21T18:52:24.969767+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Assistant

_source line 252 · 2026-05-21T18:52:28.359166+00:00_

Step 2 交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 28

## Round 28

2 recorded events


### User

_source line 253 · 2026-05-21T18:52:30.981632+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

核心判断：**Overall 3.5 (Borderline Conference)**。

三个 Must-Fix 问题：
1. **"Drift" framing 超出数据支撑** — 两个时间点只能建立 difference，不能建立 drift trend
2. **无法区分 "problematic drift" vs "genuine capability change"** — 31% 数字的 interpretation 存在根本性 ambiguity，STEM/Humanities 方向性差异可能正是 measurement working correctly
3. **Proposition 1 是 tautological** — cross-subject matching 定义的直接推论，不应以 formal proposition 形式呈现

主要 Should-Fix：Table 2 术语混淆（C% 误标为 FPR）、与 Growing Pains 区分不足、ρ ≈ 0.997 削弱 practical significance、semi-synthetic injection 生态效度有限。

引用验证无重大问题（51 entries 全部被引用，无 orphan/missing，OpenAlex 未找到的主要是近期 preprints 和教育测量学经典 books）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 254 · 2026-05-21T18:52:38.492252+00:00_

交叉分享已派发给两位 Reviewer，等待 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 255 · 2026-05-21T18:53:29.552180+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R2-N1: "Drift" framing 超出数据支撑——两个时间点不能建立趋势**

同意。"Temporal Measurement Drift" 在语义上暗示持续的方向性变化过程，但论文仅有 2023 vs 2024 一个对比（Section 4.2），以及 2023-H2 vs 2024-H1 的补充窗口（Section 4.7, C% = 34.35%）。两个时间点只能建立 "difference"，不能建立 "drift"（需要至少 3 个点来识别趋势方向和加速/减速）。我自己的审稿中未单独提出这一点，但在 N1 中对 "measurement drift" 的 framing 表达了类似顾虑——DIF 可能反映真实能力变化而非测量伪影。R2 的提法更精确：这首先是一个术语选择问题，"temporal DIF" 或 "temporal instability" 更准确。

补充：METABENCH 数据跨 2023-2024，理论上可以做季度级分析（如 2023-Q1/Q2/Q3/Q4 vs 2024-Q1/Q2），这将大幅增强 "drift" 叙事的可信度。论文未尝试此分析，是一个明显的遗漏。

**[AGREE] R2-N2: DIF 的 causal interpretation 模糊**

完全同意，这与我自己的 N1 实质相同。R2 提出的 "benign DIF" vs "problematic DIF" 区分框架比我的建议更具操作性。我补充两点：

1. R2 指出 pseudo R² = 0.0007 只排除了 domain-level accuracy gains，不排除 item-level capability changes——这一点非常关键。论文在 Section 4.2 用 "92.4% item-specific" 作为核心论据，但 item-specific 的能力提升（如模型在特定推理类型上的进步）同样会产生 item-specific DIF，这并不意味着测量出了问题。

2. R2 建议的 "定性内容分析"（对 DIF-C items 做内容分类）是一个很好的建议。如果 DIF-C 集中在某些内容类型（如需要最新知识的题目 vs 时间无关的推理题目），这将有助于区分 contamination-driven DIF 和 capability-driven DIF。论文的 difficulty-direction interaction（ρ = -0.597, Section 4.2/Introduction）——hard items gain, easy items erode——是一个有趣的线索但未被充分挖掘。

**[REBUT] R2-N3: Proposition 1 是 tautological 的**

部分同意形式问题，但反驳 "tautological" 的定性。

我在自己的 W2 中提出了类似观点（建议降格为 Remark），但 R2 的措辞 "tautological" 过于强硬。Proposition 1 的内容——跨科目匹配变量 M_i^{(-s)} 在单科目注入下不受污染——虽然在定义层面是直接的，但其方法论意义并非 trivial：它正式化了为什么跨科目匹配能保证 ΔFPR = 0，而标准匹配（within-subject）不能。这一区分在 DIF 文献中并非标准做法（传统 DIF 不需要 cross-subject matching，因为考生不会 "污染" 匹配变量），它是 LLM 场景下的特有问题。

此外，Proposition 1 的实际价值在于明确了失效边界：当 k > 1 时 ΔFPR > 0（Table 4, Appendix Figure 3）。没有这个 formal statement，读者不容易理解 multi-subject injection 结果（Table 4: k=10 时 ΔFPR = 0.047）为何偏离零。

**建议折中**：不必完全移除 Proposition 形式，但应 (a) 去掉 "proof" 的暗示（当前措辞 "by construction" 已经是对的），(b) 补充 multi-subject 情况的理论分析（如 ΔFPR 的 upper bound 表达式），使 Proposition 有更多实质内容。我在 W2 中也提了同样的建议。

---

### Should-Fix 问题

**[AGREE] R2-W1: Table 2 列名 "Temp. FPR" 误导**

完全同意。我在小问题第 1 条提出了相同观点。C% 是 DIF 检出率（相对于 ETS C 阈值），不是 false positive rate（需要 ground truth）。Temporal comparison 没有已知的 ground truth DIF 状态，因此 "FPR" 在此语境下 technically incorrect。应改为 "Temp. C%"。

**[AGREE] R2-W2: 与 Growing Pains 的区分不充分**

同意。论文在 Related Work (Section 2) 和 Discussion (Section 5.3) 提到 Growing Pains (Habba et al., 2026) 作为互补工作——FPC 假设 anchor stability 来实现跨群体等值，而本文的 DIF 分析恰恰检验这一假设是否成立。这个概念对比非常有价值但只在 Section 2 中一句带过（"Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items' measurement properties shift across model generations"）。更深入的概念对比——FPC 在 anchor 不稳定时会怎样、DIF 预筛选如何改善 FPC 的 anchor 选择——将显著加强论文的定位。

**[REBUT] R2-W3: ρ ≈ 0.997 削弱 practical significance**

部分反驳。R2 的逻辑是：如果 DIF 不影响排名，为什么要做审计？但论文在 Section 4.6 已提供了超越 aggregate ρ 的 practical evidence：

1. **Model-family rank shifts**: Llama-3 derivatives gain +53 median rank positions, Mistral loses 35（Section 4.6）。ρ ≈ 0.997 是 aggregate 统计量，掩盖了对特定模型族的系统性影响。

2. **Cohort-level 不对称**: 移除 C-flagged items 使 2024 models 下降 96.2 positions（40× larger than random removal, p < 0.001）——这意味着 DIF items 系统性地 "帮助" 较新模型，即使 overall ranking 变化不大。

3. **Discriminative information 集中**: DIF-flagged items 集中了 z = -8σ to -49σ 的判别力信息（Section 4.6）。移除它们虽然不改变排名，但大幅降低了基准的区分能力。

4. **实际应用场景**: ρ ≈ 0.997 对整体排名无影响，但对 head-to-head 模型比较（如 Model A vs Model B 差 0.5%）可能有影响——如果差异来自 DIF items，该比较不可靠。

因此，论文的 practical motivation 存在但确实 under-articulated。我同意论文应更强调 family-level 和 pairwise-comparison 层面的影响（而非只报告 aggregate ρ），但不同意 ρ ≈ 0.997 本身 "削弱" 了 practical significance——它只是说明 aggregate ranking 不是 DIF 影响的主要维度。

**[AGREE] R2-W4: ~28-29% "irreducible DIF floor" 被 under-explored**

强烈同意，这与我的 N3 直接相关。论文的三个独立分析收敛于 ~28-29%：
- 最近邻匹配: 28.9% ± 0.1%（Section 4.2）
- Llama-2 vs 3 能力匹配: 28.3%（Section 4.4）
- De-duplication K=20: 29.1%（Section 4.4）

这一收敛暗示 ~28-29% 可能是一个不可约的 baseline DIF 率，反映 MMLU 题目的某种内在属性（如多维性、内容异质性），而非时序效应。如果如此，31.3% 中仅 ~2-3 pp 是真正的时序 DIF，而非 ~31%。这将从根本上改变论文的 core claim。

论文未探讨这一可能性。如果作者能论证 ~28-29% 在 random split 中不出现（实际 random split C% = 0.18%），那它确实是时序特有的。但 random split 和 ability-quintile (2.9%) 都远低于 28-29%，说明 ~28-29% 需要一个 between-group 差异来触发——问题是这个差异是 temporal（release date）还是其他 confound。

**[AGREE] R2-W5: Semi-synthetic injection 生态效度有限**

完全同意，这与我的 N2 实质相同。R2 简洁指出了核心问题：binary response flipping 是最极端形式，ΔTPR = +0.508 在更 realistic patterns 下可能显著更低。我在 N2 中给出了更具体的建议（difficulty-dependent exploitation rate, injection fraction sensitivity analysis）。两份审稿意见在此完全一致。

---

### Missing References

R2 提出的两篇 missing references：
1. **Oren et al. (2024) "Proving Test Set Contamination in Black Box Language Models"** — 同意应引用。这是一种正式的（proof-based）黑箱污染检测方法，属于论文 Related Work 中 performance-based detectors 类别，应与 ConStat 等并列讨论。
2. **Deng et al. (2024) "Investigating Data Contamination in Modern Benchmarks for Large Language Models"** — 同意。这篇综述性工作与论文的 ground truth meta-critique 直接相关。

---

### 与我自己审稿意见的综合对照

| R2 问题 | 与 R1 的关系 | 一致性 |
|---------|-------------|--------|
| R2-N1 (Drift framing) | R1-N1 部分涵盖（因果模糊性），但 R2 更精确聚焦术语 | 互补 |
| R2-N2 (Causal interpretation) | R1-N1 完全一致 | 一致 |
| R2-N3 (Proposition 1 tautological) | R1-W2 相似但我认为 "tautological" 过强 | 部分分歧 |
| R2-W1 (Table 2 FPR) | R1 小问题 #1 完全一致 | 一致 |
| R2-W2 (Growing Pains) | R1 未提及 | 新增 |
| R2-W3 (ρ ≈ 0.997) | R1 Excitement 评分理由涉及但不作为 weakness | 部分分歧 |
| R2-W4 (Irreducible floor) | R1-N3 (within-subject 38.1%) 相关 | 互补 |
| R2-W5 (Ecological validity) | R1-N2 完全一致 | 一致 |

**综合判断**：两位 Reviewer 在因果可解释性（R2-N2/R1-N1）和半合成框架生态效度（R2-W5/R1-N2）上完全一致，这两点是最需要作者在 rebuttal 中回应的核心问题。R2 新增的 "drift" 术语问题（N1）和 "irreducible floor" 观察（W4）是有价值的补充。我对 Proposition 1 的看法略温和于 R2（建议改进而非移除），对 ρ ≈ 0.997 的看法也略不同（认为 family-level evidence 提供了足够的 practical motivation）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 256 · 2026-05-21T18:53:36.568259+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 30

## Round 30

2 recorded events


### User

_source line 257 · 2026-05-21T18:53:39.123520+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

对 R2 的 8 个问题（N1-N3, W1-W5），我的回应：
- **[AGREE]**: N1（drift 术语）、N2（因果模糊）、W1（Table 2 列名）、W2（Growing Pains 对比）、W4（~28-29% 不可约 floor）、W5（注入生态效度）
- **[REBUT]**: N3（Proposition 1——同意降格但反对 "tautological" 定性）、W3（ρ ≈ 0.997——family-level rank shifts 提供了足够的 practical motivation）

两位 Reviewer 的最强共识点：因果不可解释性和半合成框架生态效度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 258 · 2026-05-21T18:53:45.529883+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 31

## Round 31

10 recorded events


### User

_source line 259 · 2026-05-21T18:54:17.095024+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 逐条回应

**[AGREE] R1-N1: DIF 的因果可解释性不足，核心发现的解读空间过大**

完全同意，这与我的 N2 是同一个核心问题。R1 的表述比我更精确——"item-level specificity 不排除 item-level 真实能力提升（如 2024 模型在形式逻辑方面系统性进步会产生 item-specific DIF）"——这直接击中了 pseudo R² = 0.0007 论证的盲点。论文用 domain-level accuracy gains 作为 predictor 排除 aggregate confound（Section 4.2），但 item-level genuine capability change 和 item-level "measurement drift" 在统计上完全不可区分。

我的 N2 从 STEM/Humanities direction 角度提出了同样的 concern（STEM favoring 2024 可能就是 genuine improvement），R1 补充的 "操作化的区分方法" 建议很具体。我们两人独立得出了同一结论，增强了这个问题的严重性。

补充一点 R1 未提及的：Section 5.1 说 "measurement properties drift across model generations" —— 但如果 model generations 的 capability profile 变了，measurement properties *应该* 产生不同的 response patterns。DIF ≠ measurement *problem*；DIF 可以是 measurement *working as intended*。

**[AGREE with nuance] R1-N2: 半合成注入框架生态效度存疑**

同意核心关切（与我的 W5 一致），但我对 severity 判定与 R1 略有分歧。

同意的部分：
- Binary flipping 是最极端的 contamination 模式，真实 contamination 更 subtle
- 注入比例 20% 未做 sensitivity analysis 确实是一个缺口
- R1 提出的 difficulty-dependent exploitation rate 是非常好的具体建议

**细微分歧**：R1 将此列为 Must-Fix (critical)，我原本列为 Should-Fix (W5)。理由是：semi-synthetic framework 的 primary contribution 是 ΔFPR = 0.000（matching strategy property），不是 ΔTPR。论文在 Limitations 中已明确承认 "detection power under such realistic patterns is untested" 且 "the framework's primary methodological contribution—cross-subject matching achieving ΔFPR = 0.000—is a matching strategy property independent of injection realism"（Limitations paragraph 1）。ΔTPR 的 ecological validity 确实有限，但这不影响 ΔFPR = 0.000 的核心 claim。

因此我建议将此定位为 **strong Should-Fix 而非 Must-Fix**——作者需要 (a) 更明确地将 ΔTPR 标注为 upper-bound estimate，(b) 做 injection ratio sensitivity，但不需要 block 接收。

**[AGREE] R1-N3: Within-subject C% = 38.1% > 31.3% 解释不充分**

同意这是一个需要更好解释的 gap。我在 W4 中从不同角度触及了这个问题（关注 28-29% convergence），R1 从更直接的角度切入——如果 temporal DIF 是 "真实" 时序信号，per-subject 分析理应更 clean 而非更 noisy。

技术层面的 nuance：within-subject analysis 使用的是 standard matching（matching variable 包含被测 items 本身），而 temporal 31.3% 用的是 cross-subject matching。这意味着 within-subject 38.1% 同时包含了 (a) genuine temporal DIF, (b) matching variable contamination 导致的 inflation, (c) local dependence 导致的 inflation。论文给出的 LD 数据（11.3% within-subject |Q3| > 0.20 vs 2.2% cross-subject, Appendix B）可以解释部分 elevation，但 R1 正确指出——**论文没有报告 external matching 下的 within-subject C%**，这是一个关键缺失。如果用 external matching 做 within-subject DIF，C% 应该接近 31.3% 才能证明 38.1% 的 elevation 确实归因于 matching variable issues。

R1 的建议是合理的：Appendix B 应补充 external matching within-subject C% 的具体数值。

---

### Should-Fix 逐条回应

**[AGREE] R1-W1: 置换检验仅 200 次**

同意。200 次 permutation 的最小 p = 0.005，恰好是论文报告的 p 值（0/200 exceed observed）。这意味着我们无法区分 true p = 0.001 和 p = 0.004。1,000 次是标准实践，计算成本极低（MH-DIF 本身很快）。不过，考虑到 random split C% = 0.18% 和 bootstrap CI [29.4%, 38.1%] 都已提供独立的 significance evidence，这是 minor 的——permutation test 是 robustness check 而非 primary evidence。

**[AGREE] R1-W2: Proposition 1 形式化程度与内容不匹配**

完全同意，这与我的 N3 完全一致。我将其列为 Must-Fix，R1 列为 Should-Fix。我们都认为应降格为 Remark 或 inline observation。我认为此条的 severity 介于 Should-Fix 和 Must-Fix 之间——对于 reviewers 来说，"trivial claims dressed up as theorems" 会显著降低对方法论贡献的信任度。但如果只是格式调整（proposition → remark），修改成本极低。

**[AGREE] R1-W3: Bootstrap CI 忽略家族内相关性**

同意，这是我遗漏的一个 valid concern。METABENCH 中 model families（Llama 系列、Mistral 系列）内的成员共享大量训练数据和架构，model-level resampling 的 effective sample size 远小于 5,227。Cluster bootstrap（以 model family 为 cluster）可能会显著 widen CI [29.4%, 38.1%]。如果 cluster-bootstrapped CI 的下界落入 25% 以下（ETS action threshold），会影响 audit protocol（Section 5.3）的建议力度。

不过这对 core finding 的 directional conclusion 影响不大——random split C% = 0.18% 与 temporal C% = 31.3% 的差距太大，即使 CI 宽一倍，31.3% 仍然远离 null。

**[AGREE] R1-W4: Simpson's paradox model specification未完整报告**

同意。Section 4.2 报告了 item-level regression 的 pseudo R² = 0.0007 和 aggregate OR = 1.55 → controlled OR = 0.73，但没有给出完整的 model specification：
- difficulty 和 discrimination 如何操作化（是 IRT 参数 a, b 还是 CTT 统计量？）
- 是否包含交互项（difficulty × cohort 等）
- non-uniform DIF 的 24.8% 如何判定（logistic regression DIF 的 具体模型和阈值）

这些 specification details 对 reproducibility 很重要，至少应在 Appendix 中报告。

**[AGREE] R1-W5: Power analysis 使用平均参数**

同意。使用 ā = 1.2, b̄ = -0.84 做 power analysis 掩盖了 item 参数的 heterogeneity。低区分度 items（a ≪ 1.2）的 DIF detection power 会显著下降。论文声称 "TPR of 0.68-0.80"（Section 4.1），但这是基于平均 item 的估计。展示 power 随 a 值的 sensitivity curve 是 standard practice（如 power = f(a) for a ∈ {0.5, 0.8, 1.0, 1.2, 1.5, 2.0}），不需要大量额外计算。

**[AGREE] R1-W6: GSM1K N=33 统计效力不足**

同意，与我的 Q4 一致。N = 33 的 correlation analysis 极其脆弱——一两个 outliers 可以翻转 sign。论文已标注为 "exploratory"（Section 4.7），但 r = -0.478, p = 0.005 的 reporting 方式暗示了较强的 evidence。R1 建议移至 Appendix 或降低权重是合理的。至少应报告 bootstrap CI 和 influence diagnostics（Cook's distance）。

---

### Missing References 回应

**[AGREE] MMLU-Pro (Wang et al., 2024) / MMLU-Redux (Gema et al., 2024)** — 非常 relevant。论文分析的是 original MMLU，但 MMLU-Pro 和 MMLU-Redux 是社区对 MMLU 质量问题的直接回应。不引用这些工作使 Related Work 的 benchmark quality 讨论不完整。

**[PARTIAL AGREE] DIF in CAT (Lei & Li, 2003; Zwick, 2012)** — Relevant to completeness，但论文没有做 CAT，也没有声称与 CAT 的联系。ATLAS (Li et al., 2025) 已被引用。这些引用是 nice-to-have 而非 necessary。

**[PARTIAL AGREE] Measurement invariance in cross-cultural testing (Byrne et al., 1989)** — 论文已引用 Meredith (1993) 和 Vandenberg & Lance (2000) 作为 measurement invariance 的 foundational references。Byrne et al. 增加覆盖面但并非 gap。

---

### 与我（R2）审稿意见的异同总结

| R1 Issue | R2 对应 | 一致程度 |
|----------|---------|----------|
| R1-N1 (causal interpretability) | R2-N2 (drift vs capability change) | **高度一致**，独立提出同一问题 |
| R1-N2 (ecological validity) | R2-W5 (injection realism) | **一致但 severity 不同**：R1 列 Must-Fix，我列 Should-Fix |
| R1-N3 (within-subject > temporal) | R2-W4 (28-29% convergence) | **互补**：不同角度看同一数据 |
| R1-W1 (permutation 200x) | — | R1 独有，我同意 |
| R1-W2 (Proposition 1) | R2-N3 (Proposition 1) | **完全一致**，severity 相反（R1 Should-Fix, R2 Must-Fix） |
| R1-W3 (cluster bootstrap) | — | R1 独有，我同意 |
| R1-W4 (model spec) | — | R1 独有，我同意 |
| R1-W5 (power avg params) | — | R1 独有，我同意 |
| R1-W6 (GSM1K N=33) | R2-Q4 | **一致** |

**两位 Reviewer 的共识核心**：因果解释力不足（R1-N1 / R2-N2）是最严重的问题，两人独立达成一致。Proposition 1 的过度形式化（R1-W2 / R2-N3）也是共识。ρ ≈ 0.997 削弱 practical significance（R2-W3）是 R2 独有的 concern，R1 隐含提及但未单独列出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-21T18:54:42.746132+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-21T18:54:43.047836+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T18:43:14.933490+00:00\", \"completed_at\": \"2026-05-21T18:45:46.794559+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续 4 页几乎无 display item（仅 Page 5 有 Proposition 1 框）。审稿人从 Page 2 的 Figure 1 之后要翻过 4 页纯文字才看到下一个视觉锚点（Page 7 的 Table 1），容易在 Related Work + Method 段失去注意力。建议将 Table 1 或一个方法示意图/流程图前移到 Method 段（Page 4-5 附近）\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"3 个 display items（Table 1 + Figure 2 + Table 2）集中在一页，视觉过于拥挤。Table 2 被压缩到右栏底部，与 Figure 2 紧贴。建议将 Table 1 或 Table 2 中的一个移至 Page 6 以平衡节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 的 axis labels 和 legend 字号偏小（目测约为正文字号的 60-65%），在打印或缩放查看时可能影响可读性。建议增大 axis/legend 字号至正文的 70%+\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 的 caption 较简洁，但基本自包含——说明了 left/right 两个子图分别展示什么。可考虑在 caption 中加一句\\\"越高越好\\\"类的阅读指引\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 的 C% 列最优值未加粗标注。建议对每行最高/最低 C% 加粗以帮助审稿人快速定位关键数字\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"末页（附录）约 60% 填充，Figure 5 下方有约 1/3 页空白。可通过调整附录排布填充\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 8 页内仅 2 个 figure + 3 个 table = 5 个 display items。对实证为主的论文偏少（通常 5-8 个），但考虑到本文有较重的方法论/统计推导部分，尚可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 3（附录）与 Figure 2 风格一致，颜色方案连贯，good\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"所有表格使用 booktabs 风格（\\\\toprule/\\\\midrule/\\\\bottomrule），无竖线，专业\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"无 LaTeX 渲染错误、无 [?] 未解析引用、无内容溢出 margin\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"参考文献格式统一，无明显格式不一致\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 9}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-21T18:54:43.048405+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-21T18:54:43.149108+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-21T18:59:26.587108+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Fresh review cycle: Round 8 (2026-05-21)\n# R1 + R2 both at Overall 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES (open — from fresh Round 8 review)\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"因果可解释性不足——'measurement drift' 与 'genuine capability change' 无法区分\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 两位 Reviewer 独立提出同一核心问题。问题范围扩大：不仅是 causal language，更根本的是 31% DIF 可能主要反映 genuine capability change。pseudo R²=0.0007 仅排除 domain-level gains，不排除 item-level capability changes。需要操作化的 benign/problematic DIF 区分方法。\"\n  action_items:\n    - round: 7\n      action: \"替换 Conclusion 中 'driven by' → 'associated with'；全文检查 causal-leaning 措辞\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 8\n      action: \"(a) 提供至少一种 benign/problematic DIF 区分方法; (b) 对 DIF-C items 做定性内容分析; (c) Discussion 中显式讨论 'DIF as capability change signal'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑——两个时间点不能建立趋势\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 首提，R1 完全同意。标题 'Temporal Measurement Drift' 暗示方向性趋势，但实际只有 2023 vs 2024 两点比较。Section 4.7 的 6-month window 仍是两点。\"\n  action_items:\n    - round: 8\n      action: \"将 'drift' 改为 'temporal DIF'/'temporal instability'，或补充多时间点（季度级）分析\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MF3\"\n  summary: \"Within-subject C%=38.1% 高于主分析 31.3%，且 ~28-29% convergence 未被探讨\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2-W4 互补角度。Per-subject 分析理应更 clean 但反而更高。三个独立分析收敛于 ~28-29%（最近邻 28.9%、族内匹配 28.3%、去重 K=20: 29.1%），可能是 irreducible baseline DIF rate。未报告 external matching within-subject C%。\"\n  action_items:\n    - round: 8\n      action: \"(a) 报告 external matching within-subject C%; (b) 分解 38.1% 膨胀来源; (c) 讨论 28-29% convergence 含义\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES (open — from fresh Round 8 review)\n# ============================================================\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化——cross-subject matching 定义的直接推论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 列 Must-Fix ('tautological')，R1 列 Should-Fix (有 LLM 场景特有价值但形式过重)。共识：降格为 Remark，可补充 multi-subject 上界表达式。\"\n  action_items:\n    - round: 8\n      action: \"Proposition 1 降格为 Remark 或 inline observation；可选补充 multi-subject ΔFPR 上界\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic binary flipping 的 ecological validity——uniform rate p 不反映真实 contamination patterns\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"multi-subject injection 已添加，但 binary flipping 本身是 simplification\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1: binary flipping 是 'perfect contamination' 简化。R2: cross-subject matching 的 ΔFPR<0.001 有独立价值。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 再次提出。R1 列 Must-Fix，R2 列 Should-Fix（ΔFPR=0 核心 claim 独立于注入现实性）。共识 strong Should-Fix。需明确 ΔTPR 为 upper-bound，做注入比例 sensitivity。\"\n  action_items:\n    - round: 7\n      action: \"Limitations 中讨论 binary flipping 的简化假设\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 8\n      action: \"(a) 明确标注 ΔTPR 为 upper-bound estimate; (b) 做 10%/30%/50% 注入比例 sensitivity; (c) 讨论 difficulty-dependent exploitation rate\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ ≈ 0.997 削弱 practical significance，audit protocol 动机不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"修订版已扩展为 graduated thresholds——有改善但仍缺 integration workflow\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 作为 Should-Fix 提出。R1 partial rebut：family-level rank shifts (Llama-3 +53) 提供 practical motivation 但 under-articulated。共识：需更强调 family-level 和 pairwise 层面影响。\"\n  action_items:\n    - round: 8\n      action: \"Section 5/4.6 中强调 family-level rank shifts 和 pairwise comparison 影响，不仅报告 aggregate ρ\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF4\"\n  summary: \"Table 2 列名 'Temp. FPR' 误导——应改为 'Temp. C%'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Temporal comparison 无 ground truth，C% 不是 FPR。共识。\"\n  action_items:\n    - round: 8\n      action: \"Table 2 列名 'Temp. FPR' → 'Temp. C%'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 缺乏深入概念对比\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"Related Work 中说 'Empirical comparison awaits public release'——合理但无定量数据\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 再次提出。需更深入的概念对比：FPC 假设 anchor stability vs DIF 检测 anchor instability，DIF 预筛选如何改善 FPC anchor 选择。\"\n  action_items:\n    - round: 8\n      action: \"Related Work/Discussion 中扩展 Growing Pains 概念对比（FPC anchor stability 假设 vs DIF 检测 instability）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI 忽略家族内相关性（cluster bootstrap）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"修订版已明确 'B=1,000 model-level resamples'（部分回应），CI 不对称性原因仍未讨论\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 扩展为 cluster bootstrap 问题。Model families 内高相关性导致 effective N << 5,227。R2 同意但认为不影响 directional conclusion。\"\n  action_items:\n    - round: 8\n      action: \"补充 cluster bootstrap (model family 为 cluster) 的 CI，或至少报告去重数据集 (K=20) 上的 CI\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF7\"\n  summary: \"Logistic regression model specification 未完整报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。Section 4.2 的 Simpson's paradox regression 和 Section 4.4 的 logistic regression DIF 未报告完整 model spec。\"\n  action_items:\n    - round: 8\n      action: \"Appendix 中提供完整 logistic regression specification（DV/IV/交互项/拟合统计量/non-uniform DIF 判定标准）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF8\"\n  summary: \"Power analysis 使用平均 2PL 参数，未展示参数分布 sensitivity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。使用 ā=1.2, b̄=-0.84 掩盖 item 参数 heterogeneity。\"\n  action_items:\n    - round: 8\n      action: \"补充 a/b 参数分布描述统计，展示 power = f(a) sensitivity curve\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K N=33 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1+R2 共识：建议删除或压缩为 1-2 句\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 再次提出。仍在 Section 4.7 主体中报告，N=33 极其脆弱。R1 建议移至 Appendix 并补充 bootstrap CI 和 Cook's distance。\"\n  action_items:\n    - round: 8\n      action: \"移至 Appendix 并标注 'preliminary'；补充 bootstrap CI 和 influence diagnostics\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF10\"\n  summary: \"置换检验仅 200 次洗牌，分辨率有限\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意但认为 minor（有独立 significance evidence）。200 次最小 p=0.005 恰是报告值。\"\n  action_items:\n    - round: 8\n      action: \"增加至 ≥1,000 次洗牌，或明确标注 'p ≤ 0.005 (resolution limit)'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MISS-REF\"\n  summary: \"缺少引用：Oren 2024, Deng 2024, MMLU-Pro, MMLU-Redux\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Oren et al. (ICML 2024) proof-based contamination detection; Deng et al. (2024) systematic contamination survey; MMLU-Pro (Wang 2024) / MMLU-Redux (Gema 2024) — 与 'retire flagged items' 建议直接相关。\"\n  action_items:\n    - round: 8\n      action: \"补充上述 4 篇引用到 Related Work\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ISSUES FROM PRIOR ROUNDS — NOT RAISED IN ROUND 8\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null——headline 31.3% 缺乏正确 baseline comparator\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 最终评估中最重要的新发现。random-split (0.18%) 是 perfect null，不代表 realistic null。\"\n    - round: 8\n      reviewers: []\n      note: \"Round 8 fresh review 确认 permutation test 已在论文中（200 次 label shuffle, p=0.005）。核心问题已解决，但新提出 200 次分辨率有限的 concern（见 R8-SF10）。\"\n  resolution: \"Permutation null 已补充到 §4.2（200 shuffles, null C%=0.10%±0.12%, p=0.005）\"\n  resolution_round: 8\n\n- id: \"R6-W1\"\n  summary: \"IRT model fit statistics 未报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"MH-DIF 不依赖 IRT fit（技术正确），但 transparent reporting 要求至少呈现\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 作为 issue 提出。Appendix A.2 已有 IRT model fit note。\"\n  resolution: \"Appendix A.2 reports poor fit to unidimensional 2PL (expected for 57-subject benchmark) and explains MH-DIF validity is unaffected.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"Multi-subject injection 结果展示过于压缩\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"关键新增实验仅占 1.5 句 inline text\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提出。Table 4 (Appendix C) 现已包含 k∈{1,3,5,10,20} 的完整数据。\"\n  resolution: \"Table 4 added to Appendix C with full k-sweep data.\"\n  resolution_round: 8\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing——DIF and contamination measure different constructs\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"更准确的 framing needed\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被单独提出。Section 5.2 'Ground Truth Meta-Critique' 讨论了 global exposure vs differential functioning 的区分。\"\n  resolution: \"Section 5.2 adequately frames the construct distinction.\"\n  resolution_round: 8\n\n# ============================================================\n# RESOLVED ISSUES FROM PRIOR ROUNDS (abbreviated)\n# ============================================================\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N2-resolved\"\n  summary: \"Novelty 论证不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  resolution: \"LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。\"\n  resolution_round: 6\n  mentions: []\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (LD×DIF)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50). MH non-parametric.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]. Structural guarantee.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"MISSING-REF-1\"\n  summary: \"引用问题（Round 1-7）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 7\n  resolution: \"Verified: all 51 bib entries properly cited. Zero orphans.\"\n  resolution_round: 7\n  mentions: []"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Fresh review cycle: Round 8 (2026-05-21)\n# R1 + R2 both at Overall 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES (open — from fresh Round 8 review)\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"因果可解释性不足——'measurement drift' 与 'genuine capability change' 无法区分\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 8\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 两位 Reviewer 独立提出同一核心问题。问题范围扩大：不仅是 causal language，更根本的是 31% DIF 可能主要反映 genuine capability change。pseudo R²=0.0007 仅排除 domain-level gains，不排除 item-level capability changes。需要操作化的 benign/problematic DIF 区分方法。\"\n  action_items:\n    - round: 7\n      action: \"替换 Conclusion 中 'driven by' → 'associated with'；全文检查 causal-leaning 措辞\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 8\n      action: \"(a) 提供至少一种 benign/problematic DIF 区分方法; (b) 对 DIF-C items 做定性内容分析; (c) Discussion 中显式讨论 'DIF as capability change signal'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑——两个时间点不能建立趋势\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 首提，R1 完全同意。标题 'Temporal Measurement Drift' 暗示方向性趋势，但实际只有 2023 vs 2024 两点比较。Section 4.7 的 6-month window 仍是两点。\"\n  action_items:\n    - round: 8\n      action: \"将 'drift' 改为 'temporal DIF'/'temporal instability'，或补充多时间点（季度级）分析\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MF3\"\n  summary: \"Within-subject C%=38.1% 高于主分析 31.3%，且 ~28-29% convergence 未被探讨\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N3 + R2-W4 互补角度。Per-subject 分析理应更 clean 但反而更高。三个独立分析收敛于 ~28-29%（最近邻 28.9%、族内匹配 28.3%、去重 K=20: 29.1%），可能是 irreducible baseline DIF rate。未报告 external matching within-subject C%。\"\n  action_items:\n    - round: 8\n      action: \"(a) 报告 external matching within-subject C%; (b) 分解 38.1% 膨胀来源; (c) 讨论 28-29% convergence 含义\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES (open — from fresh Round 8 review)\n# ============================================================\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化——cross-subject matching 定义的直接推论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 列 Must-Fix ('tautological')，R1 列 Should-Fix (有 LLM 场景特有价值但形式过重)。共识：降格为 Remark，可补充 multi-subject 上界表达式。\"\n  action_items:\n    - round: 8\n      action: \"Proposition 1 降格为 Remark 或 inline observation；可选补充 multi-subject ΔFPR 上界\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic binary flipping 的 ecological validity——uniform rate p 不反映真实 contamination patterns\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"multi-subject injection 已添加，但 binary flipping 本身是 simplification\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1: binary flipping 是 'perfect contamination' 简化。R2: cross-subject matching 的 ΔFPR<0.001 有独立价值。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 再次提出。R1 列 Must-Fix，R2 列 Should-Fix（ΔFPR=0 核心 claim 独立于注入现实性）。共识 strong Should-Fix。需明确 ΔTPR 为 upper-bound，做注入比例 sensitivity。\"\n  action_items:\n    - round: 7\n      action: \"Limitations 中讨论 binary flipping 的简化假设\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 8\n      action: \"(a) 明确标注 ΔTPR 为 upper-bound estimate; (b) 做 10%/30%/50% 注入比例 sensitivity; (c) 讨论 difficulty-dependent exploitation rate\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ ≈ 0.997 削弱 practical significance，audit protocol 动机不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"修订版已扩展为 graduated thresholds——有改善但仍缺 integration workflow\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 作为 Should-Fix 提出。R1 partial rebut：family-level rank shifts (Llama-3 +53) 提供 practical motivation 但 under-articulated。共识：需更强调 family-level 和 pairwise 层面影响。\"\n  action_items:\n    - round: 8\n      action: \"Section 5/4.6 中强调 family-level rank shifts 和 pairwise comparison 影响，不仅报告 aggregate ρ\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF4\"\n  summary: \"Table 2 列名 'Temp. FPR' 误导——应改为 'Temp. C%'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Temporal comparison 无 ground truth，C% 不是 FPR。共识。\"\n  action_items:\n    - round: 8\n      action: \"Table 2 列名 'Temp. FPR' → 'Temp. C%'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 缺乏深入概念对比\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"Related Work 中说 'Empirical comparison awaits public release'——合理但无定量数据\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 再次提出。需更深入的概念对比：FPC 假设 anchor stability vs DIF 检测 anchor instability，DIF 预筛选如何改善 FPC anchor 选择。\"\n  action_items:\n    - round: 8\n      action: \"Related Work/Discussion 中扩展 Growing Pains 概念对比（FPC anchor stability 假设 vs DIF 检测 instability）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI 忽略家族内相关性（cluster bootstrap）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"修订版已明确 'B=1,000 model-level resamples'（部分回应），CI 不对称性原因仍未讨论\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 扩展为 cluster bootstrap 问题。Model families 内高相关性导致 effective N << 5,227。R2 同意但认为不影响 directional conclusion。\"\n  action_items:\n    - round: 8\n      action: \"补充 cluster bootstrap (model family 为 cluster) 的 CI，或至少报告去重数据集 (K=20) 上的 CI\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF7\"\n  summary: \"Logistic regression model specification 未完整报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。Section 4.2 的 Simpson's paradox regression 和 Section 4.4 的 logistic regression DIF 未报告完整 model spec。\"\n  action_items:\n    - round: 8\n      action: \"Appendix 中提供完整 logistic regression specification（DV/IV/交互项/拟合统计量/non-uniform DIF 判定标准）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF8\"\n  summary: \"Power analysis 使用平均 2PL 参数，未展示参数分布 sensitivity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意。使用 ā=1.2, b̄=-0.84 掩盖 item 参数 heterogeneity。\"\n  action_items:\n    - round: 8\n      action: \"补充 a/b 参数分布描述统计，展示 power = f(a) sensitivity curve\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K N=33 统计效力不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1+R2 共识：建议删除或压缩为 1-2 句\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 再次提出。仍在 Section 4.7 主体中报告，N=33 极其脆弱。R1 建议移至 Appendix 并补充 bootstrap CI 和 Cook's distance。\"\n  action_items:\n    - round: 8\n      action: \"移至 Appendix 并标注 'preliminary'；补充 bootstrap CI 和 influence diagnostics\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF10\"\n  summary: \"置换检验仅 200 次洗牌，分辨率有限\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 同意但认为 minor（有独立 significance evidence）。200 次最小 p=0.005 恰是报告值。\"\n  action_items:\n    - round: 8\n      action: \"增加至 ≥1,000 次洗牌，或明确标注 'p ≤ 0.005 (resolution limit)'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MISS-REF\"\n  summary: \"缺少引用：Oren 2024, Deng 2024, MMLU-Pro, MMLU-Redux\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Oren et al. (ICML 2024) proof-based contamination detection; Deng et al. (2024) systematic contamination survey; MMLU-Pro (Wang 2024) / MMLU-Redux (Gema 2024) — 与 'retire flagged items' 建议直接相关。\"\n  action_items:\n    - round: 8\n      action: \"补充上述 4 篇引用到 Related Work\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# ISSUES FROM PRIOR ROUNDS — NOT RAISED IN ROUND 8\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null——headline 31.3% 缺乏正确 baseline comparator\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 最终评估中最重要的新发现。random-split (0.18%) 是 perfect null，不代表 realistic null。\"\n    - round: 8\n      reviewers: []\n      note: \"Round 8 fresh review 确认 permutation test 已在论文中（200 次 label shuffle, p=0.005）。核心问题已解决，但新提出 200 次分辨率有限的 concern（见 R8-SF10）。\"\n  resolution: \"Permutation null 已补充到 §4.2（200 shuffles, null C%=0.10%±0.12%, p=0.005）\"\n  resolution_round: 8\n\n- id: \"R6-W1\"\n  summary: \"IRT model fit statistics 未报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"MH-DIF 不依赖 IRT fit（技术正确），但 transparent reporting 要求至少呈现\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 作为 issue 提出。Appendix A.2 已有 IRT model fit note。\"\n  resolution: \"Appendix A.2 reports poor fit to unidimensional 2PL (expected for 57-subject benchmark) and explains MH-DIF validity is unaffected.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"Multi-subject injection 结果展示过于压缩\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"关键新增实验仅占 1.5 句 inline text\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提出。Table 4 (Appendix C) 现已包含 k∈{1,3,5,10,20} 的完整数据。\"\n  resolution: \"Table 4 added to Appendix C with full k-sweep data.\"\n  resolution_round: 8\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing——DIF and contamination measure different constructs\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"更准确的 framing needed\"\n    - round: 8\n      reviewers: []\n      note: \"本轮未被单独提出。Section 5.2 'Ground Truth Meta-Critique' 讨论了 global exposure vs differential functioning 的区分。\"\n  resolution: \"Section 5.2 adequately frames the construct distinction.\"\n  resolution_round: 8\n\n# ============================================================\n# RESOLVED ISSUES FROM PRIOR ROUNDS (abbreviated)\n# ============================================================\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N2-resolved\"\n  summary: \"Novelty 论证不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  resolution: \"LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。\"\n  resolution_round: 6\n  mentions: []\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (LD×DIF)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50). MH non-parametric.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]. Structural guarantee.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"MISSING-REF-1\"\n  summary: \"引用问题（Round 1-7）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 7\n  resolution: \"Verified: all 51 bib entries properly cited. Zero orphans.\"\n  resolution_round: 7\n  mentions: []"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-21T18:59:26.690166+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 14167}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-21T19:02:18.131066+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 圆桌审稿报告 — irt_equated_bench_regen (Fresh Round 8)\n\n**论文**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 (ARR), Deadline 2026-05-25\n**Reviewers**: R1（方法严谨性+实验设计）, R2（新颖性+完整性+写作质量）\n**圆桌轮数**: 1 轮（Round 1 后交叉回应即收敛，无需 Round 2）\n\n---\n\n## Summary\n\n本文将教育测量学中的 Mantel-Haenszel DIF 分析（配合 ETS 严重程度分类）应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目），发现 2023 vs 2024 模型群体间约 31% 的 MMLU 题目呈现 ETS Category C 级别的时序 DIF。作者开发了跨科目匹配的半合成注入框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标志几乎独立（enrichment ≈ 0.964, φ = 0.012），揭示现有污染检测验证方法论中的\"类别错误\"。分析扩展到六个 METABENCH 基准（C% = 17.9–31.3%），排名稳定性未受影响（ρ ≈ 0.997）。\n\n---\n\n## Strengths\n\n**S1. 规模与全面性** [consensus]：据两位 Reviewer 所知，这是 LLM 基准上最大规模的 DIF 分析（5,227 models × 12,508 items）。5 种 cohort designs + 6 个 benchmark 交叉验证增强了发现的可信度。\n\n**S2. 控制实验设计精良** [consensus]：随机分裂（0.18%）、能力分位（2.9%）、族内对比（Llama-2 vs 3）、1:1 最近邻匹配（Cohen's d ≈ -0.010, C% = 28.9% ± 0.1%）、置换检验（200 次，null C% = 0.10%）——多重控制有效排除了方法论伪影。\n\n**S3. Ground truth meta-critique 有独立价值** [consensus]：DIF flags 与 web-overlap labels 的 near-independence（enrichment = 0.964, φ = 0.012）构成对领域验证方法论的有价值批评。global exposure vs differential functioning 的概念区分清晰。\n\n**S4. 跨科目匹配的方法论贡献** [consensus]：ΔFPR = 0.000 的构造性保证 + 多科目注入的梯度退化实验（Table 4: k ≤ 5 时 ΔFPR < 0.007）提供了实用边界。\n\n**S5. 可重复性良好** [consensus]：匿名代码已提供，数据基于公开 METABENCH，关键超参数（K=5, ETS C 阈值, 5 seeds）均已报告，2PL 参数来源透明。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, consensus R1+R2] **因果可解释性不足——\"measurement drift\" 与 \"genuine capability change\" 无法区分**\n\n两位 Reviewer 独立提出同一核心问题（R1-N1, R2-N2），交叉回应中完全一致。\n\n31% 的核心发现如果主要由真实能力提升驱动，则 DIF 只是在重新发现代际差异而非测量漂移。具体问题：\n- pseudo R² = 0.0007 仅排除 domain-level accuracy gains，不排除 item-level capability changes（如 2024 模型在形式逻辑方面的系统性进步会产生 item-specific DIF，但这是 measurement working correctly）\n- STEM favoring 2024 models (55.4%), Humanities favoring 2023 (64.4%)——完全可能是 genuine capability improvement\n- \"92.4% item-specific\" 只说明 DIF 不归因于 domain-level gains，不排除 item-level genuine capability change\n- Section 5.1 \"measurement properties drift\" 但 DIF ≠ measurement problem；DIF 可以是 measurement working as intended\n\n**需要**：(a) 至少一种操作化的 benign/problematic DIF 区分方法（如 DIF-C items 的定性内容分析）；(b) 在 Discussion 中显式讨论 \"DIF as capability change signal\" 的可能性及其对结论的影响；(c) 统一 framing——论文部分段落已有 \"diagnostic lens\" 意识但不一致。\n\n**MF2** [critical, R2 首提, R1 fully agrees] **\"Drift\" framing 超出数据支撑——两个时间点不能建立趋势**\n\n标题 \"Temporal Measurement Drift\" 暗示方向性时序趋势，但实际只有 2023 vs 2024 两点比较。\"Drift\" 需要至少 3 个时间点来建立方向和速度。Section 4.7 的 6-month window（2023-H2 vs 2024-H1, C% = 34.35%）仍是另一个两点比较。METABENCH 数据理论上可做季度级分析。\n\n**需要**：将 \"drift\" 改为 \"temporal DIF\" 或 \"temporal instability\"；或补充 3+ 时间点分析来 justify \"drift\" 一词。\n\n**MF3** [critical/strong-warning, R1-N3 + R2-W4 互补] **Within-subject C% = 38.1% 高于主分析 31.3%，且 ~28-29% convergence 未被探讨**\n\nPer-subject 分析（控制多维性）理应给出更 clean 的估计，但 within-subject C% = 38.1% 反而更高。论文归因于局部依赖（11.3% within-subject |Q3| > 0.20 vs 2.2% cross-subject），但：(1) 未报告 external matching 下的 within-subject C%——这是验证 LD 解释的关键数据；(2) 三个独立分析收敛于 ~28-29%（最近邻 28.9%、Llama-2 vs 3 ability-matched 28.3%、去重 K=20 29.1%），这可能暗示一个 irreducible baseline DIF rate——如果如此，31.3% 中仅 ~2-3 pp 是真正的时序 DIF，从根本上改变核心 claim。\n\n**需要**：(a) 报告 external matching within-subject C%；(b) 详细分解 38.1% 膨胀来源（LD vs 样本量 vs stratum homogeneity）；(c) 显式讨论 28-29% convergence 的含义——是 temporal signal 还是 structural property。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, consensus R1-W2 + R2-N3] **Proposition 1 过度形式化**：Cross-subject matching 定义的直接推论，格式化为 Proposition 增加不应有的形式感。R2 称 \"tautological\"，R1 认为有 LLM 场景价值但形式过重。共识：降格为 Remark，可选补充 multi-subject ΔFPR 上界表达式。\n\n**SF2** [warning, R1-N2 + R2-W5] **半合成注入框架生态效度有限**：Binary response flipping 是最极端的 contamination 模式。ΔTPR = +0.508 at p = 0.5 在更现实的污染模式下会进一步下降。注入比例 20% 未做 sensitivity analysis。R2 指出 ΔFPR = 0.000 的核心 claim 独立于注入现实性（归为 Strong Should-Fix）。需要：(a) 明确标注 ΔTPR 为 upper-bound estimate；(b) 做注入比例 sensitivity（10%/30%/50%）；(c) 讨论 difficulty-dependent exploitation rate。\n\n**SF3** [warning, R2-W3, R1 partial rebut] **ρ ≈ 0.997 削弱 practical significance**：R2 质疑：如果 DIF 不影响 ranking，为什么要做 audit？R1 反驳指出 family-level rank shifts（Llama-3 +53, Mistral -35）、discriminative information 集中（z = -8σ to -49σ）、cohort-level 不对称（2024 models 下降 96.2 positions, 40× > random, p < 0.001）提供了足够 motivation，但论文 under-articulated。需要：在 Section 5 或 4.6 中更强调 family-level 和 pairwise-comparison 层面影响。\n\n**SF4** [warning, consensus] **Table 2 列名 \"Temp. FPR\" 误导**：Temporal comparison 无 ground truth，C% 不是 FPR。应改为 \"Temp. C%\"。\n\n**SF5** [warning, R2-W2, R1 agrees] **与 Growing Pains 区分不充分**：Related Work 中 \"empirical comparison awaits public release\" 使 complementarity claim 无法验证。需要更深入的概念对比——FPC 假设 anchor stability 而 DIF 检测 anchor instability，DIF 预筛选如何改善 FPC anchor 选择。\n\n**SF6** [warning, R1-W3, R2 agrees] **Bootstrap CI 忽略家族内相关性**：Model-level resampling (B=1,000) 未考虑 model families 内的高相关性，effective N << 5,227。需要 cluster bootstrap（model family 为 cluster）或至少报告去重数据集（K=20）上的 CI。R2 认为不影响 directional conclusion（random split 0.18% vs 31.3% 差距太大）。\n\n**SF7** [warning, R1-W4, R2 agrees] **Logistic regression model specification 未完整报告**：Section 4.2 和 4.4 的 logistic regression（Simpson's paradox, non-uniform DIF）未报告完整 model spec（difficulty/discrimination 操作化方式、交互项、non-uniform DIF 判定标准）。至少应在 Appendix 提供。\n\n**SF8** [warning, R1-W5, R2 agrees] **Power analysis 使用平均 2PL 参数**：ā = 1.2, b̄ = -0.84 掩盖 item 参数 heterogeneity。应展示 power = f(a) sensitivity curve 和参数分布描述统计。\n\n**SF9** [warning, R1-W6 + R2-Q4] **GSM1K N=33 统计效力不足**：N = 33 的 correlation analysis 极其脆弱。建议移至 Appendix 并标注 \"preliminary\"，补充 bootstrap CI 和 influence diagnostics（Cook's distance）。\n\n**SF10** [warning, R1-W1, R2 agrees as minor] **置换检验仅 200 次洗牌**：最小可报告 p = 1/200 = 0.005 恰是报告值。增加到 ≥1,000 次成本极低。R2 认为 minor（有独立 significance evidence），R1 认为 standard practice 应遵守。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 独立提出或交叉回应中完全一致：\n\n1. **因果可解释性不足**（MF1）——最严重的问题，独立提出\n2. **\"Drift\" 术语超出数据支撑**（MF2）\n3. **Within-subject C% 与 28-29% convergence**（MF3）\n4. **Proposition 1 过度形式化**（SF1）\n5. **Semi-synthetic injection 生态效度有限**（SF2）\n6. **Table 2 列名误导**（SF4）\n7. **Growing Pains 区分不足**（SF5）\n8. **置换检验分辨率有限**（SF10）\n9. **Bootstrap CI 家族聚类**（SF6）\n10. **Logistic regression model spec**（SF7）\n11. **Power analysis 平均参数**（SF8）\n12. **GSM1K N=33 效力不足**（SF9）\n\n## Reviewer Divergence\n\n仅有三处轻微分歧，均已在交叉回应中解决：\n\n1. **Proposition 1 severity**：R2 列 Must-Fix（\"tautological\"），R1 列 Should-Fix（有 LLM 场景价值）。R1 rebut 论点有理——Proposition 明确了 LLM 场景特有的 matching 需求。**Director 判断：Strong Should-Fix**。\n\n2. **Semi-synthetic injection severity**：R1 列 Must-Fix，R2 列 Strong Should-Fix（ΔFPR = 0 独立于注入现实性）。R2 论点成立。**Director 判断：Strong Should-Fix**。\n\n3. **ρ ≈ 0.997 practical significance**：R2 列 Should-Fix，R1 partial rebut（family-level evidence 足够但 under-articulated）。**Director 判断：Should-Fix，论文有 evidence 但需更好呈现**。\n\n---\n\n## Questions for Authors\n\nQ1 [consensus, priority]: 如果将 DIF 方向（favoring 2023 vs 2024）与已知训练数据变化进行对照（如 instruction tuning / RLHF 的使用），是否能提供因果归因的初步证据？\n\nQ2 [consensus, priority]: ~28-29% 能力匹配后的 DIF 率在非 temporal cohorts（如按 model size 分组并匹配 ability）上是多少？如果同样出现 ~28-29%，31% 中的时序特异性成分将大幅缩减。\n\nQ3 [R1]: Within-subject DIF 使用 external matching（如 MMLU DIF using GSM8K total score）时的 C% 是多少？\n\nQ4 [R1]: Cross-subject matching 中 57 个科目间相关性对 Proposition 1 的影响？如果污染集中在相关科目群中，M_i^{(-s)} 仍会部分吸收信号。\n\nQ5 [R1+R2]: Section 5.3 的 C% action thresholds（15%, 25%）基于什么依据？ETS 原始阈值迁移到 LLM 场景的合理性？\n\nQ6 [R2]: Discussion Section 5.2 称 BHI (Zhu et al., 2026) \"speculative\"——具体指哪个 component？\n\nQ7 [R1]: IRT 2PL model fit 不佳（Appendix A.2）是否影响 power analysis 的参数估计可信度？\n\n---\n\n## Missing References\n\n**必要**（两位 Reviewer 共同建议）：\n1. **Oren et al. (2024)** \"Proving Test Set Contamination in Black Box Language Models\" (ICML) — proof-based 黑箱污染检测，应与 ConStat 等并列\n2. **Deng et al. (2024)** \"Investigating Data Contamination in Modern Benchmarks for LLMs\" — 系统性污染调查，增强 meta-critique 的 generality\n3. **MMLU-Pro (Wang et al., 2024) / MMLU-Redux (Gema et al., 2024)** — MMLU 修订版，与 \"retire flagged items\" 建议直接相关\n\n**建议**（R1 提出，R2 partial agree）：\n4. DIF in CAT (Lei & Li, 2003; Zwick, 2012) — nice-to-have\n5. Cross-cultural measurement invariance (Byrne et al., 1989) — 已有 Meredith 1993, Vandenberg & Lance 2000 覆盖\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 9 info）。\n\n**Warnings:**\n- **Pages 3-6 视觉断层**：连续 4 页几乎无 display item（仅 Page 5 有 Proposition 1 框）。从 Figure 1（Page 2）到 Table 1（Page 7）需翻过 4 页纯文字，审稿人在 Related Work + Method 段容易失去注意力。建议将 Table 1 或方法示意图/流程图前移至 Method 段（Page 4-5 附近）。\n- **Page 7 视觉拥挤**：3 个 display items（Table 1 + Figure 2 + Table 2）集中在一页。Table 2 被压缩到右栏底部。建议将其中一个移至 Page 6 以平衡节奏。\n\n**Info highlights:**\n- Figure 2 axis labels/legend 字号偏小（~60-65% 正文字号），建议增大至 70%+\n- 主文 8 页内 5 个 display items（2 figures + 3 tables），对实证论文偏少但可接受\n- 所有表格使用 booktabs 风格，专业\n- 无 LaTeX 渲染错误、无 [?] 未解析引用、参考文献格式统一\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 — Borderline Conference**\n**置信度: 4/5**\n\n两位 Reviewer 独立给出 3.5 (Borderline Conference)，交叉讨论后分数维持不变。\n\n**核心评价**：这是一篇实验设计 thorough、规模可观的 empirical paper，将经典 psychometric 方法（MH-DIF, 1988）成功迁移到 LLM 基准评估场景。Semi-synthetic validation framework（ΔFPR = 0.000 的构造性保证）和 ground truth meta-critique（enrichment ≈ 0.964 揭示 web-overlap labels 的类别错误）有独立价值。控制实验（5 种 cohort designs + 6 benchmarks 交叉验证 + permutation test + nearest-neighbor matching）设计精良。\n\n**三个核心制约因素**：\n1. **因果模糊性**（最严重）——31% temporal DIF 可能主要反映 genuine capability change 而非 problematic measurement drift，论文未能操作化地区分两种可能性\n2. **\"Drift\" 术语不当**——两个时间点只能建立 difference，不能建立 trend\n3. **~28-29% convergence 暗示 irreducible structural baseline**——可能使时序特异 DIF 仅为 ~2-3 pp，从根本上改变核心 claim 的 magnitude\n\n**次要制约因素**：\n4. Methodological novelty 有限——MH-DIF 是标准方法的直接应用，cross-subject matching 在 psychometric 文献中有先例\n5. Practical impact 受限——ρ ≈ 0.997 说明 aggregate ranking 不受影响（但 family-level evidence 提供了部分 motivation）\n6. 多项统计细节需补充（logistic regression spec, cluster bootstrap, power sensitivity, permutation resolution）\n\n**升/降分路径**：\n- ↑ **4.0 (Conference)**：如果 authors 在 rebuttal 中 (a) 提供 DIF-C items 的定性内容分析以初步区分 benign/problematic DIF；(b) 补充多时间点趋势分析或将 \"drift\" 改为更准确术语；(c) 解释 28-29% convergence（如非 temporal cohorts 上不出现此 floor）；(d) 地址关键统计细节\n- ↓ **3.0 (Findings)**：如果上述问题不能充分回应，论文更适合 Findings track——实证发现有价值但 framing 和 interpretation 存在根本性 ambiguity\n\n---\n\n## Detailed Comments\n\n**Abstract**：信息密度过高（~15 个数字），建议精简至核心 5-6 个。enrichment ≈ 0.96 和 φ = 0.012 对 NLP 读者不直观，可用更直白语言辅助。\n\n**Section 1 (Introduction)**：Motivation 清晰有力。三个 contributions 列举得当。Contribution 1 的 framing 侧重 ΔFPR = 0.000 和 ΔTPR，应明确 ΔTPR 是 upper-bound estimate。difficulty-direction interaction（ρ = -0.597）是有趣线索但未被充分挖掘——可用于初步区分 contamination-driven 和 capability-driven DIF。\n\n**Section 2 (Related Work)**：覆盖全面（~51 bib entries 全部被引用，无 orphan）。缺少 MMLU-Pro/Redux、Oren et al.、Deng et al.。与 Growing Pains 的概念对比（FPC vs DIF）不够深入——一句 \"complementary\" 不足以建立清晰的差异化。Holland & Thayer (1988) 的 bib 年份可能需核实（OpenAlex 记录显示 1986 mismatch）。\n\n**Section 3 (Method)**：方法描述清晰。Proposition 1 应降格为 Remark。LLM-specific challenges 段（local dependence, family structure, non-normality, multi-dimensionality）是有价值的贡献，展示了 LLM 场景的特有挑战。Semi-synthetic injection 的 procedure（20% ETS-A items, rate p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}）合理但缺少 p = 0.1 这个更现实的低注入率点。\n\n**Section 4 (Experiments)**：控制实验设计精良。Table 2 列名需修正（\"Temp. FPR\" → \"Temp. C%\"）。Simpson's paradox logistic regression 需在 Appendix 报告完整 model spec。Power analysis 应展示参数分布 sensitivity。Within-subject 38.1% 需更详细的分解和 external matching 数据。GSM1K N=33 分析应降低权重（移至 Appendix）。Bootstrap CI 应补充 cluster bootstrap。Permutation test 应增加到 ≥1,000 次。\n\n**Section 5 (Discussion)**：Section 5.1 的 \"measurement properties drift\" 措辞需与因果模糊性一致化——如果无法确定 DIF 反映测量问题还是能力变化，\"drift\" 一词暗示了不当的诊断方向。Section 5.2 对 BHI 的 \"speculative\" 评价需更具体。Section 5.3 的 audit protocol thresholds（15%, 25%）需论证从 educational testing 迁移的合理性。ρ ≈ 0.997 之外应更强调 family-level 和 pairwise-comparison 影响。\n\n**Section 6 (Conclusion)**：仅两句，过于简略。可补充 practical implications。注意因果语言（\"associated with\" 而非 \"driven by\"）。\n\n**Limitations**：诚实且覆盖关键点（uniform-only DIF, binary flipping simplification, matching boundary, generalizability）。IRT model fit note 存在于 Appendix A.2。\n\n**Appendix**：Method Details (A) 和 Statistical Considerations (A.2) 有价值。Table 4 (C: multi-subject injection) 是重要补充。Figure 3 与 Figure 2 风格一致。Figure 5 (GSM1K scatter) 较 cluttered。末页约 60% 填充。\n\n---\n\n**Issue Tracker 已同步更新**：`projects/irt_equated_bench_regen/artifacts/review_issues.yaml`\n- 3 个 Must-Fix（MF1 因果模糊、MF2 drift 术语、MF3 within-subject/convergence）\n- 10 个 Should-Fix（SF1-SF10）\n- 1 个 Info（missing references）\n- 4 个 prior issues 标记为 resolved（R7-N1 permutation null, R6-W1 IRT fit, R7-W1 multi-subject table, R5-W7 construct framing）",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 — Borderline Conference",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 圆桌审稿报告 — irt_equated_bench_regen (Fresh Round 8)\n\n**论文**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 (ARR), Deadline 2026-05-25\n**Reviewers**: R1（方法严谨性+实验设计）, R2（新颖性+完整性+写作质量）\n**圆桌轮数**: 1 轮（Round 1 后交叉回应即收敛，无需 Round 2）\n\n---\n\n## Summary\n\n本文将教育测量学中的 Mantel-Haenszel DIF 分析（配合 ETS 严重程度分类）应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目），发现 2023 vs 2024 模型群体间约 31% 的 MMLU 题目呈现 ETS Category C 级别的时序 DIF。作者开发了跨科目匹配的半合成注入框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标志几乎独立（enrichment ≈ 0.964, φ = 0.012），揭示现有污染检测验证方法论中的\"类别错误\"。分析扩展到六个 METABENCH 基准（C% = 17.9–31.3%），排名稳定性未受影响（ρ ≈ 0.997）。\n\n---\n\n## Strengths\n\n**S1. 规模与全面性** [consensus]：据两位 Reviewer 所知，这是 LLM 基准上最大规模的 DIF 分析（5,227 models × 12,508 items）。5 种 cohort designs + 6 个 benchmark 交叉验证增强了发现的可信度。\n\n**S2. 控制实验设计精良** [consensus]：随机分裂（0.18%）、能力分位（2.9%）、族内对比（Llama-2 vs 3）、1:1 最近邻匹配（Cohen's d ≈ -0.010, C% = 28.9% ± 0.1%）、置换检验（200 次，null C% = 0.10%）——多重控制有效排除了方法论伪影。\n\n**S3. Ground truth meta-critique 有独立价值** [consensus]：DIF flags 与 web-overlap labels 的 near-independence（enrichment = 0.964, φ = 0.012）构成对领域验证方法论的有价值批评。global exposure vs differential functioning 的概念区分清晰。\n\n**S4. 跨科目匹配的方法论贡献** [consensus]：ΔFPR = 0.000 的构造性保证 + 多科目注入的梯度退化实验（Table 4: k ≤ 5 时 ΔFPR < 0.007）提供了实用边界。\n\n**S5. 可重复性良好** [consensus]：匿名代码已提供，数据基于公开 METABENCH，关键超参数（K=5, ETS C 阈值, 5 seeds）均已报告，2PL 参数来源透明。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1** [critical, consensus R1+R2] **因果可解释性不足——\"measurement drift\" 与 \"genuine capability change\" 无法区分**\n\n两位 Reviewer 独立提出同一核心问题（R1-N1, R2-N2），交叉回应中完全一致。\n\n31% 的核心发现如果主要由真实能力提升驱动，则 DIF 只是在重新发现代际差异而非测量漂移。具体问题：\n- pseudo R² = 0.0007 仅排除 domain-level accuracy gains，不排除 item-level capability changes（如 2024 模型在形式逻辑方面的系统性进步会产生 item-specific DIF，但这是 measurement working correctly）\n- STEM favoring 2024 models (55.4%), Humanities favoring 2023 (64.4%)——完全可能是 genuine capability improvement\n- \"92.4% item-specific\" 只说明 DIF 不归因于 domain-level gains，不排除 item-level genuine capability change\n- Section 5.1 \"measurement properties drift\" 但 DIF ≠ measurement problem；DIF 可以是 measurement working as intended\n\n**需要**：(a) 至少一种操作化的 benign/problematic DIF 区分方法（如 DIF-C items 的定性内容分析）；(b) 在 Discussion 中显式讨论 \"DIF as capability change signal\" 的可能性及其对结论的影响；(c) 统一 framing——论文部分段落已有 \"diagnostic lens\" 意识但不一致。\n\n**MF2** [critical, R2 首提, R1 fully agrees] **\"Drift\" framing 超出数据支撑——两个时间点不能建立趋势**\n\n标题 \"Temporal Measurement Drift\" 暗示方向性时序趋势，但实际只有 2023 vs 2024 两点比较。\"Drift\" 需要至少 3 个时间点来建立方向和速度。Section 4.7 的 6-month window（2023-H2 vs 2024-H1, C% = 34.35%）仍是另一个两点比较。METABENCH 数据理论上可做季度级分析。\n\n**需要**：将 \"drift\" 改为 \"temporal DIF\" 或 \"temporal instability\"；或补充 3+ 时间点分析来 justify \"drift\" 一词。\n\n**MF3** [critical/strong-warning, R1-N3 + R2-W4 互补] **Within-subject C% = 38.1% 高于主分析 31.3%，且 ~28-29% convergence 未被探讨**\n\nPer-subject 分析（控制多维性）理应给出更 clean 的估计，但 within-subject C% = 38.1% 反而更高。论文归因于局部依赖（11.3% within-subject |Q3| > 0.20 vs 2.2% cross-subject），但：(1) 未报告 external matching 下的 within-subject C%——这是验证 LD 解释的关键数据；(2) 三个独立分析收敛于 ~28-29%（最近邻 28.9%、Llama-2 vs 3 ability-matched 28.3%、去重 K=20 29.1%），这可能暗示一个 irreducible baseline DIF rate——如果如此，31.3% 中仅 ~2-3 pp 是真正的时序 DIF，从根本上改变核心 claim。\n\n**需要**：(a) 报告 external matching within-subject C%；(b) 详细分解 38.1% 膨胀来源（LD vs 样本量 vs stratum homogeneity）；(c) 显式讨论 28-29% convergence 的含义——是 temporal signal 还是 structural property。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1** [warning, consensus R1-W2 + R2-N3] **Proposition 1 过度形式化**：Cross-subject matching 定义的直接推论，格式化为 Proposition 增加不应有的形式感。R2 称 \"tautological\"，R1 认为有 LLM 场景价值但形式过重。共识：降格为 Remark，可选补充 multi-subject ΔFPR 上界表达式。\n\n**SF2** [warning, R1-N2 + R2-W5] **半合成注入框架生态效度有限**：Binary response flipping 是最极端的 contamination 模式。ΔTPR = +0.508 at p = 0.5 在更现实的污染模式下会进一步下降。注入比例 20% 未做 sensitivity analysis。R2 指出 ΔFPR = 0.000 的核心 claim 独立于注入现实性（归为 Strong Should-Fix）。需要：(a) 明确标注 ΔTPR 为 upper-bound estimate；(b) 做注入比例 sensitivity（10%/30%/50%）；(c) 讨论 difficulty-dependent exploitation rate。\n\n**SF3** [warning, R2-W3, R1 partial rebut] **ρ ≈ 0.997 削弱 practical significance**：R2 质疑：如果 DIF 不影响 ranking，为什么要做 audit？R1 反驳指出 family-level rank shifts（Llama-3 +53, Mistral -35）、discriminative information 集中（z = -8σ to -49σ）、cohort-level 不对称（2024 models 下降 96.2 positions, 40× > random, p < 0.001）提供了足够 motivation，但论文 under-articulated。需要：在 Section 5 或 4.6 中更强调 family-level 和 pairwise-comparison 层面影响。\n\n**SF4** [warning, consensus] **Table 2 列名 \"Temp. FPR\" 误导**：Temporal comparison 无 ground truth，C% 不是 FPR。应改为 \"Temp. C%\"。\n\n**SF5** [warning, R2-W2, R1 agrees] **与 Growing Pains 区分不充分**：Related Work 中 \"empirical comparison awaits public release\" 使 complementarity claim 无法验证。需要更深入的概念对比——FPC 假设 anchor stability 而 DIF 检测 anchor instability，DIF 预筛选如何改善 FPC anchor 选择。\n\n**SF6** [warning, R1-W3, R2 agrees] **Bootstrap CI 忽略家族内相关性**：Model-level resampling (B=1,000) 未考虑 model families 内的高相关性，effective N << 5,227。需要 cluster bootstrap（model family 为 cluster）或至少报告去重数据集（K=20）上的 CI。R2 认为不影响 directional conclusion（random split 0.18% vs 31.3% 差距太大）。\n\n**SF7** [warning, R1-W4, R2 agrees] **Logistic regression model specification 未完整报告**：Section 4.2 和 4.4 的 logistic regression（Simpson's paradox, non-uniform DIF）未报告完整 model spec（difficulty/discrimination 操作化方式、交互项、non-uniform DIF 判定标准）。至少应在 Appendix 提供。\n\n**SF8** [warning, R1-W5, R2 agrees] **Power analysis 使用平均 2PL 参数**：ā = 1.2, b̄ = -0.84 掩盖 item 参数 heterogeneity。应展示 power = f(a) sensitivity curve 和参数分布描述统计。\n\n**SF9** [warning, R1-W6 + R2-Q4] **GSM1K N=33 统计效力不足**：N = 33 的 correlation analysis 极其脆弱。建议移至 Appendix 并标注 \"preliminary\"，补充 bootstrap CI 和 influence diagnostics（Cook's distance）。\n\n**SF10** [warning, R1-W1, R2 agrees as minor] **置换检验仅 200 次洗牌**：最小可报告 p = 1/200 = 0.005 恰是报告值。增加到 ≥1,000 次成本极低。R2 认为 minor（有独立 significance evidence），R1 认为 standard practice 应遵守。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 独立提出或交叉回应中完全一致：\n\n1. **因果可解释性不足**（MF1）——最严重的问题，独立提出\n2. **\"Drift\" 术语超出数据支撑**（MF2）\n3. **Within-subject C% 与 28-29% convergence**（MF3）\n4. **Proposition 1 过度形式化**（SF1）\n5. **Semi-synthetic injection 生态效度有限**（SF2）\n6. **Table 2 列名误导**（SF4）\n7. **Growing Pains 区分不足**（SF5）\n8. **置换检验分辨率有限**（SF10）\n9. **Bootstrap CI 家族聚类**（SF6）\n10. **Logistic regression model spec**（SF7）\n11. **Power analysis 平均参数**（SF8）\n12. **GSM1K N=33 效力不足**（SF9）\n\n## Reviewer Divergence\n\n仅有三处轻微分歧，均已在交叉回应中解决：\n\n1. **Proposition 1 severity**：R2 列 Must-Fix（\"tautological\"），R1 列 Should-Fix（有 LLM 场景价值）。R1 rebut 论点有理——Proposition 明确了 LLM 场景特有的 matching 需求。**Director 判断：Strong Should-Fix**。\n\n2. **Semi-synthetic injection severity**：R1 列 Must-Fix，R2 列 Strong Should-Fix（ΔFPR = 0 独立于注入现实性）。R2 论点成立。**Director 判断：Strong Should-Fix**。\n\n3. **ρ ≈ 0.997 practical significance**：R2 列 Should-Fix，R1 partial rebut（family-level evidence 足够但 under-articulated）。**Director 判断：Should-Fix，论文有 evidence 但需更好呈现**。\n\n---\n\n## Questions for Authors\n\nQ1 [consensus, priority]: 如果将 DIF 方向（favoring 2023 vs 2024）与已知训练数据变化进行对照（如 instruction tuning / RLHF 的使用），是否能提供因果归因的初步证据？\n\nQ2 [consensus, priority]: ~28-29% 能力匹配后的 DIF 率在非 temporal cohorts（如按 model size 分组并匹配 ability）上是多少？如果同样出现 ~28-29%，31% 中的时序特异性成分将大幅缩减。\n\nQ3 [R1]: Within-subject DIF 使用 external matching（如 MMLU DIF using GSM8K total score）时的 C% 是多少？\n\nQ4 [R1]: Cross-subject matching 中 57 个科目间相关性对 Proposition 1 的影响？如果污染集中在相关科目群中，M_i^{(-s)} 仍会部分吸收信号。\n\nQ5 [R1+R2]: Section 5.3 的 C% action thresholds（15%, 25%）基于什么依据？ETS 原始阈值迁移到 LLM 场景的合理性？\n\nQ6 [R2]: Discussion Section 5.2 称 BHI (Zhu et al., 2026) \"speculative\"——具体指哪个 component？\n\nQ7 [R1]: IRT 2PL model fit 不佳（Appendix A.2）是否影响 power analysis 的参数估计可信度？\n\n---\n\n## Missing References\n\n**必要**（两位 Reviewer 共同建议）：\n1. **Oren et al. (2024)** \"Proving Test Set Contamination in Black Box Language Models\" (ICML) — proof-based 黑箱污染检测，应与 ConStat 等并列\n2. **Deng et al. (2024)** \"Investigating Data Contamination in Modern Benchmarks for LLMs\" — 系统性污染调查，增强 meta-critique 的 generality\n3. **MMLU-Pro (Wang et al., 2024) / MMLU-Redux (Gema et al., 2024)** — MMLU 修订版，与 \"retire flagged items\" 建议直接相关\n\n**建议**（R1 提出，R2 partial agree）：\n4. DIF in CAT (Lei & Li, 2003; Zwick, 2012) — nice-to-have\n5. Cross-cultural measurement invariance (Byrne et al., 1989) — 已有 Meredith 1993, Vandenberg & Lance 2000 覆盖\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 9 info）。\n\n**Warnings:**\n- **Pages 3-6 视觉断层**：连续 4 页几乎无 display item（仅 Page 5 有 Proposition 1 框）。从 Figure 1（Page 2）到 Table 1（Page 7）需翻过 4 页纯文字，审稿人在 Related Work + Method 段容易失去注意力。建议将 Table 1 或方法示意图/流程图前移至 Method 段（Page 4-5 附近）。\n- **Page 7 视觉拥挤**：3 个 display items（Table 1 + Figure 2 + Table 2）集中在一页。Table 2 被压缩到右栏底部。建议将其中一个移至 Page 6 以平衡节奏。\n\n**Info highlights:**\n- Figure 2 axis labels/legend 字号偏小（~60-65% 正文字号），建议增大至 70%+\n- 主文 8 页内 5 个 display items（2 figures + 3 tables），对实证论文偏少但可接受\n- 所有表格使用 booktabs 风格，专业\n- 无 LaTeX 渲染错误、无 [?] 未解析引用、参考文献格式统一\n\n---\n\n## Overall Assessment\n\n**评分: 3.5 — Borderline Conference**\n**置信度: 4/5**\n\n两位 Reviewer 独立给出 3.5 (Borderline Conference)，交叉讨论后分数维持不变。\n\n**核心评价**：这是一篇实验设计 thorough、规模可观的 empirical paper，将经典 psychometric 方法（MH-DIF, 1988）成功迁移到 LLM 基准评估场景。Semi-synthetic validation framework（ΔFPR = 0.000 的构造性保证）和 ground truth meta-critique（enrichment ≈ 0.964 揭示 web-overlap labels 的类别错误）有独立价值。控制实验（5 种 cohort designs + 6 benchmarks 交叉验证 + permutation test + nearest-neighbor matching）设计精良。\n\n**三个核心制约因素**：\n1. **因果模糊性**（最严重）——31% temporal DIF 可能主要反映 genuine capability change 而非 problematic measurement drift，论文未能操作化地区分两种可能性\n2. **\"Drift\" 术语不当**——两个时间点只能建立 difference，不能建立 trend\n3. **~28-29% convergence 暗示 irreducible structural baseline**——可能使时序特异 DIF 仅为 ~2-3 pp，从根本上改变核心 claim 的 magnitude\n\n**次要制约因素**：\n4. Methodological novelty 有限——MH-DIF 是标准方法的直接应用，cross-subject matching 在 psychometric 文献中有先例\n5. Practical impact 受限——ρ ≈ 0.997 说明 aggregate ranking 不受影响（但 family-level evidence 提供了部分 motivation）\n6. 多项统计细节需补充（logistic regression spec, cluster bootstrap, power sensitivity, permutation resolution）\n\n**升/降分路径**：\n- ↑ **4.0 (Conference)**：如果 authors 在 rebuttal 中 (a) 提供 DIF-C items 的定性内容分析以初步区分 benign/problematic DIF；(b) 补充多时间点趋势分析或将 \"drift\" 改为更准确术语；(c) 解释 28-29% convergence（如非 temporal cohorts 上不出现此 floor）；(d) 地址关键统计细节\n- ↓ **3.0 (Findings)**：如果上述问题不能充分回应，论文更适合 Findings track——实证发现有价值但 framing 和 interpretation 存在根本性 ambiguity\n\n---\n\n## Detailed Comments\n\n**Abstract**：信息密度过高（~15 个数字），建议精简至核心 5-6 个。enrichment ≈ 0.96 和 φ = 0.012 对 NLP 读者不直观，可用更直白语言辅助。\n\n**Section 1 (Introduction)**：Motivation 清晰有力。三个 contributions 列举得当。Contribution 1 的 framing 侧重 ΔFPR = 0.000 和 ΔTPR，应明确 ΔTPR 是 upper-bound estimate。difficulty-direction interaction（ρ = -0.597）是有趣线索但未被充分挖掘——可用于初步区分 contamination-driven 和 capability-driven DIF。\n\n**Section 2 (Related Work)**：覆盖全面（~51 bib entries 全部被引用，无 orphan）。缺少 MMLU-Pro/Redux、Oren et al.、Deng et al.。与 Growing Pains 的概念对比（FPC vs DIF）不够深入——一句 \"complementary\" 不足以建立清晰的差异化。Holland & Thayer (1988) 的 bib 年份可能需核实（OpenAlex 记录显示 1986 mismatch）。\n\n**Section 3 (Method)**：方法描述清晰。Proposition 1 应降格为 Remark。LLM-specific challenges 段（local dependence, family structure, non-normality, multi-dimensionality）是有价值的贡献，展示了 LLM 场景的特有挑战。Semi-synthetic injection 的 procedure（20% ETS-A items, rate p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}）合理但缺少 p = 0.1 这个更现实的低注入率点。\n\n**Section 4 (Experiments)**：控制实验设计精良。Table 2 列名需修正（\"Temp. FPR\" → \"Temp. C%\"）。Simpson's paradox logistic regression 需在 Appendix 报告完整 model spec。Power analysis 应展示参数分布 sensitivity。Within-subject 38.1% 需更详细的分解和 external matching 数据。GSM1K N=33 分析应降低权重（移至 Appendix）。Bootstrap CI 应补充 cluster bootstrap。Permutation test 应增加到 ≥1,000 次。\n\n**Section 5 (Discussion)**：Section 5.1 的 \"measurement properties drift\" 措辞需与因果模糊性一致化——如果无法确定 DIF 反映测量问题还是能力变化，\"drift\" 一词暗示了不当的诊断方向。Section 5.2 对 BHI 的 \"speculative\" 评价需更具体。Section 5.3 的 audit protocol thresholds（15%, 25%）需论证从 educational testing 迁移的合理性。ρ ≈ 0.997 之外应更强调 family-level 和 pairwise-comparison 影响。\n\n**Section 6 (Conclusion)**：仅两句，过于简略。可补充 practical implications。注意因果语言（\"associated with\" 而非 \"driven by\"）。\n\n**Limitations**：诚实且覆盖关键点（uniform-only DIF, binary flipping simplification, matching boundary, generalizability）。IRT model fit note 存在于 Appendix A.2。\n\n**Appendix**：Method Details (A) 和 Statistical Considerations (A.2) 有价值。Table 4 (C: multi-subject injection) 是重要补充。Figure 3 与 Figure 2 风格一致。Figure 5 (GSM1K scatter) 较 cluttered。末页约 60% 填充。\n\n---\n\n**Issue Tracker 已同步更新**：`projects/irt_equated_bench_regen/artifacts/review_issues.yaml`\n- 3 个 Must-Fix（MF1 因果模糊、MF2 drift 术语、MF3 within-subject/convergence）\n- 10 个 Should-Fix（SF1-SF10）\n- 1 个 Info（missing references）\n- 4 个 prior issues 标记为 resolved（R7-N1 permutation null, R6-W1 IRT fit, R7-W1 multi-subject table, R5-W7 construct framing）",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 — Borderline Conference",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-21T19:02:22.146480+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4015
}
```

</details>

---


### Assistant

_source line 268 · 2026-05-21T19:02:29.521876+00:00_

审稿报告已投递给 Research Director。

**审稿完成总结**：

- **评分**：3.5 — Borderline Conference（两位 Reviewer 独立一致）
- **3 个 Must-Fix**：(1) 因果模糊性——31% DIF 无法区分 measurement drift 和 genuine capability change；(2) "Drift" 术语超出两时间点数据支撑；(3) Within-subject C%=38.1% 与 ~28-29% convergence 暗示 irreducible structural baseline
- **10 个 Should-Fix**：Proposition 1 降格、注入生态效度标注、practical significance 强调、Table 2 列名、Growing Pains 对比、cluster bootstrap、logistic regression spec、power sensitivity、GSM1K 降权、permutation 分辨率
- **升/降分路径**：MF1-MF3 充分回应 → 4.0 (Conference)；不能回应 → 3.0 (Findings)
- **Issue Tracker** 已同步更新至 `review_issues.yaml`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 32

## Round 32

2 recorded events


### User

_source line 269 · 2026-05-21T19:02:32.467174+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：R1 和我（R2）在最关键问题上高度一致——**因果解释力不足**（DIF 无法区分 genuine capability change 和 problematic drift）是两人独立识别的最严重问题。Proposition 1 的过度形式化也是共识。分歧主要在 severity 判定上：semi-synthetic 生态效度问题我认为是 Should-Fix（因为 ΔFPR=0.000 的核心 claim 不受影响），R1 认为是 Must-Fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 270 · 2026-05-21T19:02:44.602047+00:00_

审稿报告已投递至 Research Director，流程完成。

**审稿结果摘要**：

- **评分**：3.5 — Borderline Conference（两位 Reviewer 独立一致）
- **3 个 Must-Fix**：因果模糊性（measurement drift vs capability change）、"Drift" 术语不当（两点不构成趋势）、Within-subject C%=38.1% 与 ~28-29% convergence 未解释
- **10 个 Should-Fix**：Proposition 1 形式化、注入生态效度、practical significance 呈现、Table 2 列名、Growing Pains 对比、cluster bootstrap、logistic regression spec、power sensitivity、GSM1K N=33、permutation 分辨率
- **升分路径**：若 rebuttal 能提供 DIF-C 内容分析 + 多时间点趋势 + 28-29% convergence 解释 → 4.0 (Conference)
- **Issue Tracker 已同步更新**（14 条 open，4 条本轮 resolved）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 33

## Round 33

46 recorded events


### User

_source line 271 · 2026-05-22T01:40:02.931208+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-22T01:40:08.512408+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-22T01:40:08.565159+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-22T01:40:14.390589+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-22T01:40:14.391060+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-22T01:40:17.454675+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-22T01:40:17.505305+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-22T01:40:21.020889+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-22T01:40:21.021337+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-22T01:40:26.246722+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-22T01:40:26.751043+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-22T01:40:27.705269+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers author guidelines submission format",
  "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers author guidelines submission format",
    "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 283 · 2026-05-22T01:40:29.111766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 284 · 2026-05-22T01:40:29.363315+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 285 · 2026-05-22T01:40:29.363865+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 286 · 2026-05-22T01:40:29.414455+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-22T01:40:38.854198+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers author guidelines submission format"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) 2026 call for papers, author guidelines, and submission format:

## Submission Format and Requirements

Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template, and submissions are made in OpenReview.

## Author Guidelines

**Anonymity and Originality:**
- Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided
- All submitted papers 
…[truncated 998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 11148
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-22T01:40:42.871345+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-22T01:40:44.377614+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 formatting requirements page limit long paper short paper",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 formatting requirements page limit long paper short paper",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-22T01:40:45.331826+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-22T01:40:45.784243+00:00_

# Review Issues Tracker — irt_equated_bench_regen
# Round 8 Action Matrix finalized (2026-05-21)
# R1 + R2 both at Overall 3.5 (Borderline Conference)

# ============================================================
# CRITICAL ISSUES (in_progress — Round 8 Action Matrix locked)
# ============================================================

- id: "R1-W1"
  summary: "因果可解释性不足——'measurement drift' 与 'genuine capability change' 无法区分"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 8
  mentions:
    - round: 5
      reviewers: [1, 2]
      note: "标题 'Psychometric Instability' 过强"
    - round: 6
      reviewers: [1, 2]
      note: "标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language"
    - round: 7
      reviewers: [1, 2]
      note: "R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。"
    - round: 8
      reviewers: [1, 2]
      note: "Fresh review 两位 Reviewer 独立提出同一核心问题。问题范围扩大：不仅是 causal language，更根本的是 31% DIF 可能主要反映 genuine capability change。pseudo R²=0.0007 仅排除 domain-level gains，不排除 item-level capability changes。需要操作化的 benign/problematic DIF 区分方法。"
  action_items:
    - round: 7
      action: "替换 Conclusion 中 'driven by' → 'associated with'；全文检查 causal-leaning 措辞"
      assigned_to: paper_agent
      status: resolved
    - round: 8
      action: "P29: Discussion 新增 DIF Interpretation 段落，用三层框架（impact→DIF→attribution）替代简单 benign/problematic 二分法。用已有数据：item-specificity 92.4%、domain directionality、difficulty-direction interaction。全文统一 framing：DIF = diagnostic signal requiring monitoring。"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R8-MF2"
  summary: "'Drift' framing 超出数据支撑——两个时间点不能建立趋势"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 8
  last_seen_round: 8
  mentions:
    - round: 8
      reviewers: [1, 2]
      note: "R2 首提，R1 完全同意。标题 'Temporal Measurement Drift' 暗示方向性趋势，但实际只有 2023 vs 2024 
…[truncated 10444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-22T01:40:45.935205+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | head -100",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-22T01:40:45.985856+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 294 · 2026-05-22T01:40:49.350162+00:00_

Web search results for query: "ACL Rolling Review 2026 formatting requirements page limit long paper short paper"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review Proposal - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php?title=ACL_Rolling_Review_Proposal"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Industry Track - ACL 2026","url":"https://2026.aclweb.org/calls/industry_track/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, here are the ACL Rolling Review 2026 formatting requirements regarding page limits for long and short papers:

## Page Limits

Short papers have a maximum of 4 content pages, while long papers have a maximum of 8 content pages.

## Sections That Don
…[truncated 619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 4972
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-22T01:40:53.065260+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view
…[truncated 1469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 10193
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-22T01:40:58.440401+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-22T01:40:58.792526+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-22T01:40:58.793013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-22T01:40:58.843592+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-22T01:41:16.279414+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "experiment_plan.yaml",
  "max_chars": "2000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "experiment_plan.yaml",
    "max_chars": "2000"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-22T01:41:16.781911+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-22T01:41:16.933360+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/*.tex 2>/dev/null",
  "description": "Check paper section lengths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/*.tex 2>/dev/null",
    "description": "Check paper section lengths"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-22T01:41:16.984898+00:00_

    3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex
  121 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex
    5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex
   21 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex
  117 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex
   27 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex
   10 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex
   58 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex
   14 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex
  376 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-22T01:41:24.064552+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\n# Try to find config in common locations\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2'\nfor p in ['config.yaml', 'projects/irt_equated_bench_regen/config.yaml', 'agent-config.yaml']:\n    fp = os.path.join(base, p)\n    if os.path.exists(fp):\n        print(f'FOUND: {fp}')\n# Check experiment_plan for external review\nep = os.path.join(base, 'projects/irt_equated_bench_regen/experiment_plan.yaml')\nif os.path.exists(ep):\n    with open(ep) as f:\n        data = yaml.safe_load(f)\n    if 'external_review' in str(data):\n        print('HAS_EXTERNAL_REVIEW in experiment_plan')\n    print(json.dumps(data.get('external_review', 'NOT_FOUND'), default=str))\n\" 2>/dev/null || echo \"SCRIPT_ERROR\"",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\n# Try to find config in common locations\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2'\nfor p in ['config.yaml', 'projects/irt_equated_bench_regen/config.yaml', 'agent-config.yaml']:\n    fp = os.path.join(base, p)\n    if os.path.exists(fp):\n        print(f'FOUND: {fp}')\n# Check experiment_plan for external review\nep = os.path.join(base, 'projects/irt_equated_bench_regen/experiment_plan.yaml')\nif os.path.exists(ep):\n    with open(ep) as f:\n        data = yaml.safe_load(f)\n    if 'external_review' in str(data):\n        print('HAS_EXTERNAL_REVIEW in experiment_plan')\n    print(json.dumps(data.get('external_review', 'NOT_FOUND'), default=str))\n\" 2>/dev/null || echo \"SCRIPT_ERROR\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-22T01:41:24.918752+00:00_

"NOT_FOUND"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-22T01:41:25.019670+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf 2>/dev/null | grep -i pages || echo \"NO_PDFINFO\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-22T01:41:25.070447+00:00_

Pages:           14

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-22T01:41:56.357210+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 投稿信息\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **论文类别**: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计入页数)\n- **模板**: ACL (review mode, double-blind)\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **IRT/DIF 方法论**：MH-DIF 的应用是否正确？假设是否满足（局部独立性、单维性）？是否对 model-level 二值化响应使用 DIF 的适用性做了充分论证？\n2. **统计检验**：多重比较校正、bootstrap CI、permutation test 的实施是否正确？效果量和统计显著性是否准确报告？\n3. **Semi-synthetic 框架**：binary flipping 注入方法的 ecological validity、TPR/FPR 的解释是否合理？Power analysis 的参数选择和结论是否站得住脚？\n4. **Robustness checks**：within-subject 分析、matching 方法对比、去重实验等是否充分？是否遗漏了关键的 confound？\n5. **Formal claims**：论文中的 Proposition/Remark 是否严谨？数学推导是否正确？\n6. **数据与可重复性**：数据规模(5,227 models)的描述是否可信？方法描述是否足以复现？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n\n### Summary (2-3 句)\n### Strengths (逐条, S1/S2/...)\n### Weaknesses (逐条, W1/W2/..., 标注 severity: critical/warning/info)\n### Questions (逐条, Q1/Q2/...)\n### Missing References (如有)\n### Minor Issues (如有)\n### Overall Assessment (1-5 分, 参照 ARR 标准; 附简要理由)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "irt_equated_bench_regen",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 投稿信息\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **论文类别**: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计入页数)\n- **模板**: ACL (review mode, double-blind)\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **IRT/DIF 方法论**：MH-DIF 的应用是否正确？假设是否满足（局部独立性、单维性）？是否对 model-level 二值化响应使用 DIF 的适用性做了充分论证？\n2. **统计检验**：多重比较校正、bootstrap CI、permutation test 的实施是否正确？效果量和统计显著性是否准确报告？\n3. **Semi-synthetic 框架**：binary flipping 注入方法的 ecological validity、TPR/FPR 的解释是否合理？Power analysis 的参数选择和结论是否站得住脚？\n4. **Robustness checks**：within-subject 分析、matching 方法对比、去重实验等是否充分？是否遗漏了关键的 confound？\n5. **Formal claims**：论文中的 Proposition/Remark 是否严谨？数学推导是否正确？\n6. **数据与可重复性**：数据规模(5,227 models)的描述是否可信？方法描述是否足以复现？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n\n### Summary (2-3 句)\n### Strengths (逐条, S1/S2/...)\n### Weaknesses (逐条, W1/W2/..., 标注 severity: critical/warning/info)\n### Questions (逐条, Q1/Q2/...)\n### Missing References (如有)\n### Minor Issues (如有)\n### Overall Assessment (1-5 分, 参照 ARR 标准; 附简要理由)"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-22T01:42:09.772608+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13415
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-22T01:42:10.075190+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 投稿信息\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **论文类别**: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计入页数)\n- **模板**: ACL (review mode, double-blind)\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **Novelty / Contribution**：将 psychometric DIF 方法应用于 LLM benchmark 的新颖性如何？与已有 benchmark contamination detection 方法（如 Growing Pains 的 FPC）的区分是否清晰？三个 stated contributions 是否都有实质支撑？\n2. **Related Work 覆盖度**：是否遗漏重要相关工作？特别是 LLM evaluation、benchmark contamination、IRT in NLP 领域的关键文献。引用是否真实（无幻觉引用）、格式是否一致？\n3. **Framing 一致性**：标题、Abstract、Introduction 的 claim 是否与实验结果匹配？是否存在过强的因果性表述（如将 DIF 等同于 contamination evidence）？\"instability\" 的定义是否一致？\n4. **写作质量**：行文是否清晰、简洁、无冗余？符号和术语使用是否一致？表格/图表的呈现是否有效传达关键发现？\n5. **格式合规**：\n   - 正文是否 ≤8 页（不含 references、limitations、appendix）？\n   - 是否使用正确的 ACL 模板（`\\usepackage[review]{acl}`）？\n   - 是否匿名（无作者信息泄露）？\n   - Appendix 是否在参考文献之后？\n   - 图表/表格编号和交叉引用是否正确？\n6. **Practical significance**：论文提出的 audit protocol 是否有实际应用价值？ρ≈0.997 的高相关性下，31% DIF rate 的 practical impact 是否被充分论证？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n\n### Summary (2-3 句)\n### Strengths (逐条, S1/S2/...)\n### Weaknesses (逐条, W1/W2/..., 标注 severity: critical/warning/info)\n### Questions (逐条, Q1/Q2/...)\n### Missing References (如有)\n### Minor Issues (如有)\n### Overall Assessment (1-5 分, 参照 ARR 标准; 附简要理由)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "irt_equated_bench_regen",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 投稿信息\n- **目标 venue**: EMNLP 2026 (via ACL Rolling Review, May cycle)\n- **截止日期**: 2026-05-25\n- **论文类别**: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计入页数)\n- **模板**: ACL (review mode, double-blind)\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **Novelty / Contribution**：将 psychometric DIF 方法应用于 LLM benchmark 的新颖性如何？与已有 benchmark contamination detection 方法（如 Growing Pains 的 FPC）的区分是否清晰？三个 stated contributions 是否都有实质支撑？\n2. **Related Work 覆盖度**：是否遗漏重要相关工作？特别是 LLM evaluation、benchmark contamination、IRT in NLP 领域的关键文献。引用是否真实（无幻觉引用）、格式是否一致？\n3. **Framing 一致性**：标题、Abstract、Introduction 的 claim 是否与实验结果匹配？是否存在过强的因果性表述（如将 DIF 等同于 contamination evidence）？\"instability\" 的定义是否一致？\n4. **写作质量**：行文是否清晰、简洁、无冗余？符号和术语使用是否一致？表格/图表的呈现是否有效传达关键发现？\n5. **格式合规**：\n   - 正文是否 ≤8 页（不含 references、limitations、appendix）？\n   - 是否使用正确的 ACL 模板（`\\usepackage[review]{acl}`）？\n   - 是否匿名（无作者信息泄露）？\n   - Appendix 是否在参考文献之后？\n   - 图表/表格编号和交叉引用是否正确？\n6. **Practical significance**：论文提出的 audit protocol 是否有实际应用价值？ρ≈0.997 的高相关性下，31% DIF rate 的 practical impact 是否被充分论证？\n\n## 输出格式\n\n请按以下结构输出审稿意见：\n\n### Summary (2-3 句)\n### Strengths (逐条, S1/S2/...)\n### Weaknesses (逐条, W1/W2/..., 标注 severity: critical/warning/info)\n### Questions (逐条, Q1/Q2/...)\n### Missing References (如有)\n### Minor Issues (如有)\n### Overall Assessment (1-5 分, 参照 ARR 标准; 附简要理由)"
  }
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-22T01:42:11.637783+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-22T01:42:12.103275+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2028
}
```

</details>

---


### Tool call

_source line 313 · 2026-05-22T01:42:12.356640+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-22T01:42:13.567592+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1929
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-22T01:42:14.423889+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 2067
}
```

</details>

---


### Assistant

_source line 316 · 2026-05-22T01:42:21.433939+00:00_

全部任务已分发：

- **Reviewer 1** (方法严谨性) — 已启动 ✓
- **Reviewer 2** (新颖性+完整性) — 已启动 ✓
- **视觉审查 Agent** — 已启动 ✓
- **外部审稿 (Stanford Agentic Reviewer)** — 请求已发送，等待用户提交 ✓

等待两位 Reviewer 返回初审结果，随后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 317 · 2026-05-22T01:47:40.898111+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：Temporal Measurement Instability in LLM Benchmarks

---

### Summary (2-3 句)

本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 METABENCH 六个 benchmark 中 17.9%–31.3% 的题目在 2023 与 2024 模型 cohort 之间存在大幅度时序测量不稳定性（ETS-C 分类）。作者提出 cross-subject matching 的半合成注入框架实现 ΔFPR=0.000，并揭示 web-overlap 污染标签与 DIF flag 近乎独立（enrichment≈0.96），指出现有污染检测的 ground truth 存在类别错误。论文方法论严谨、robustness check 覆盖面广，但在注入模型的 ecological validity、因果归因能力、以及 DIF 方法对 LLM 群体适用性的论证上存在值得讨论的问题。

---

### Strengths

**S1 [方法论贡献清晰且可复用]**
Cross-subject matching 实现 ΔFPR=0.000 的方法贡献干净利落（Section 3.4, Remark），multi-subject injection 的优雅退化分析（Appendix Table 5：k≤5 时 ΔFPR<0.007，k=10 时升至 0.047）为实际应用划定了清晰的适用边界。这个 matching 策略本身可以独立于本文的具体分析场景使用。

**S2 [Robustness check 覆盖面极广]**
论文系统性地排除了 6 种替代解释（ability confounding, family inflation, θ-conditioning, within-subject effects, ranking impact, local dependence），C% 在多种 matching 策略下均稳定在 ~28-29% 的底线（Section 4.4, Table 2）。随机拆分对照组 C%=0.18% 与能力分位数对照组 C%=2.9% 提供了有说服力的 null baseline。这种论证深度在 benchmark 评估类论文中少见。

**S3 [Ground truth meta-critique 具有启发性]**
揭示 web-overlap labels 与 DIF flags 近乎正交（enrichment=0.964, Jaccard=0.206, φ=0.012; Section 4.3）是一个重要的方法论洞察。这不仅对本文有意义，也挑战了整个污染检测社区的评估范式——任何以 web-overlap 作为 ground truth 验证 differential detector 的工作都面临同样的类别错误。

**S4 [跨 benchmark 复现]**
六个 benchmark 均展示显著 temporal DIF（45-174× above baseline; Table 3），且 knowledge/reasoning benchmark（C%≥26.9%）高于 procedural benchmark（C%≤18.9%）的模式合理且有可解释性。

**S5 [统计报告规范]**
几乎所有核心数字都附有 CI/效应量/多重比较校正。ETS-C 的双阈值机制本身就提供了隐式多重检验控制，BH-FDR 校正后仅移除 3 项（31.32%→31.30%）的结果进一步证实了这一点。

**S6 [Simpson's paradox 分析精巧]**
Item-level regression 揭示 92.4% 的 DIF 信号是 item-specific（pseudo R²=0.0007），而 domain-level accuracy 的效应在控制 item properties 后反转（OR: 1.55→0.73），这是区分 item-level 与 domain-level 效应的有力证据（Section 4.2）。

---

### Weaknesses

**W1 [warning] 半合成注入的 ecological validity 不足，限制了 TPR/FPR 的实际可解释性**
- 具体位置：Section 3.4, Limitations paragraph 1
- 问题：Binary flipping（incorrect→correct）是一种最极端的均匀利用模式。真实的 contamination 表现为部分记忆、推理捷径、格式敏感性等，其在 response matrix 上的影响模式远比 uniform flipping 复杂。论文承认这是 "worst-case uniform exploitation"，但这意味着 ΔTPR=+0.508 at p=0.5 这个数字的实际参考价值有限——对于更现实的 contamination pattern，detection power 可能显著不同（可能更低，因为信号更弱更分散）。
- 建议：至少提供一种更现实的注入模型作为 robustness check，例如 (a) 按 item difficulty 分层的非均匀 flipping（难题更容易被 memorize），或 (b) 仅翻转高区分度 items 的 subset。这不需要大量额外实验，但能显著增强 power analysis 的说服力。

**W2 [warning] 对 LLM 群体应用 MH-DIF 的理论适用性论证不够充分**
- 具体位置：Section 3.2 "LLM-specific challenges" paragraph
- 问题：论文列举了 4 个 LLM-specific challenge（local dependence, family structure, non-normal ability distribution, multidimensionality），但每个只是简要提及对应的处理措施。核心的理论空白在于：MH 统计量的大样本性质（渐近 χ² 分布）依赖 examinees 的独立性假设。LLM "examinees" 不是独立采样的——它们共享训练数据、架构、甚至是 fine-tuning 的 base model。Graduated de-duplication 在经验层面处理了这个问题，但论文没有讨论 non-independence 对 MH χ² test 的 type-I error rate 的理论影响。
- 建议：增加一个段落讨论 MH test 在 clustered/non-independent examinees 下的 size 表现，可引用教育测量中 multi-level DIF 分析的相关文献（如 French & Finch, 2010 关于 clustered data 中 DIF detection 的研究）。或者提供 permutation-based p-values 作为 non-parametric 替代（论文已有 permutation test，但仅用于 null C% 而非每个 item 的 DIF p-value）。

**W3 [warning] 因果归因能力的局限性使得 "measurement instability" 的 framing 可能误导**
- 具体位置：Abstract, Title, Section 5.1
- 问题：论文反复强调 "31% measurement instability" 并建议在 C%≥25% 时 "rotate or retire flagged items"（Section 5.3）。但 Discussion (Section 5.1) 也承认无法区分 DIF 是源于 contamination、capability evolution 还是 training methodology shift。如果 DIF 源于 genuine capability evolution（例如 2024 模型确实在某些推理维度上更强），那么这些 items 的 differential functioning 恰恰是 benchmark 应该测量的——retire 这些 items 反而会丢失有价值的区分信息。论文在 Downstream Impact（Section 4.5）中也证明了 DIF items 承载更多 discriminative signal（z = -8σ to -49σ），这与 "retire flagged items" 的建议存在张力。
- 建议：在 Discussion 中更明确地讨论这个张力——何时 DIF 是 "measurement instability"（问题），何时是 "expected sensitivity to genuine change"（特征）。目前的三层框架（impact/DIF/attribution）很好但最后一层完全悬空。

**W4 [info] Permutation test 的迭代次数偏少**
- 具体位置：Section 4.2
- 问题：主 permutation test 使用 200 次标签打乱，p=0.005 恰好是分辨率极限（1/200=0.005）。虽然论文标注了 "resolution limit" 且补充了 per-subject permutation（1,000×8 subjects），但主检验的 200 次迭代给出的 p-value 实质上只能说明 p≤0.005。
- 建议：增加到至少 1,000 次 permutation（计算代价可忽略，因为只需重新运行 MH 统计），以获得更精确的 p-value 估计。

**W5 [info] ρ≈0.997 排名相关性的解读需要更多 nuance**
- 具体位置：Section 4.5, Abstract
- 问题：从 12,508 items 移除 ~31% 后排名相关性仍为 0.997，这在一定程度上是 MMLU 的高冗余度的体现，而非 DIF items 不重要的证据。论文在 Discussion 中提到 family-level 排名位移（Llama-3 +53, Mistral -35），但这些位移被整体 ρ≈0.997 的叙事所掩盖。建议同时报告 pairwise model comparison 翻转率（即在 full vs stable-only 评估下，多少对模型的优劣排序发生逆转），这比 Spearman ρ 更能反映实际影响。

**W6 [warning] Cross-subject matching 中 "subject" 粒度对 DIF 结果的敏感性未充分分析**
- 具体位置：Section 3.2, Section 3.4
- 问题：MMLU 的 57 个 subjects 大小差异很大（从几十到几百道题），cross-subject matching 排除当前 subject 后剩余 items 数量差异也很大。对于小 subject（例如只有 ~100 道题），排除它对 matching variable 的影响微乎其微，这意味着 matching variable 仍然部分包含了被测 items 的信号——特别是在 MMLU 这样的多 subject benchmark 中。论文没有分析 subject 大小与 DIF detection rate 之间的关系。
- 建议：报告 subject-level C% 与 subject size 的相关性。如果小 subject 的 C% 系统性偏高，则暗示 matching variable contamination 未被完全消除。

---

### Questions

**Q1**: Section 4.2 报告 1:1 nearest-neighbor matching 后 C%=28.9%±0.1%，比 unmatched 31.3% 低约 2.4pp。这个 matching 是在 model 总分上做的还是在 IRT θ 上做的？如果是 model 总分，那么 matched 后 cohort 大小从 (1080, 807) 降到 (638, 638)——近半数模型被丢弃，这是否引入了 selection bias？

**Q2**: Power analysis（Section 4.1）使用 PSN-IRT 的 2PL 参数（ā=1.2, b̄=-0.84），但 Appendix A.2 又提到 "MMLU response matrix shows poor fit to a unidimensional 2PL model"。如果 2PL 拟合差，那么基于 2PL 参数的 power analysis 结论的可靠性如何？论文是否考虑过使用非参数方法估计 power？

**Q3**: Table 1 中 Within-subject 的 C%=38.1% 高于 Temporal 的 31.3%。这是因为 within-subject 分析中 matching variable 的 items 更少导致 stratification 噪声增大，还是因为 within-subject DIF 确实更严重？论文是否做了 simulation 来校准 within-subject DIF 分析的 expected type-I error rate？

**Q4**: GSM1K 的相关性分析（r=-0.478, p=0.005, N=33）样本量很小且论文标注为 exploratory，但 Abstract 中 "DIF captures capability change distinct from memorization" 的措辞暗示这是一个已确立的结论。能否明确区分 confirmed findings 和 exploratory signals？

**Q5**: Section 3.2 提到 "IRT θ estimates correlate at r=0.9986 with total scores in our data"。这个极高的相关性是否暗示在这个数据上 IRT θ 几乎不提供超越 CTT total score 的信息？如果是，那么整个 IRT framing 的附加价值是什么？

---

### Missing References

- French, B. F., & Finch, W. H. (2010). Hierarchical logistic regression: Accounting for multilevel data in DIF detection. *Journal of Educational Measurement*, 47(3), 299–317. — 关于 clustered data 中 DIF 检测的多层次方法，与 W2 直接相关。
- Magis, D., & De Boeck, P. (2012). A robust outlier approach to prevent type I error inflation in DIF. *Educational and Psychological Measurement*, 72(2), 291–311. — 关于 DIF 检测中 type-I error 控制的替代方法。
- 论文引用了 Habba et al. (2026) 的 Growing Pains 关于 anchor-item calibration，但没有引用经典的 equating 文献（如 Kolen & Brennan, 2014, *Test Equating, Scaling, and Linking*），考虑到论文标题涉及 "equated bench"。

---

### Minor Issues

- Abstract 行文密度很高，一句话中同时出现 ΔFPR=0.000, ΔTPR=+0.508, enrichment≈0.96, φ=0.012，对首次接触的读者不友好。建议拆分核心 contribution 和具体数字。
- Section 3.2 的 ETS 分类定义中，Category B 的描述 "all remaining items: those with 1.0≤|Δ_MH|<1.5, or |Δ_MH|≥1.5 without statistical significance" 缺少 |Δ_MH|<1.0 但有统计显著性的情况——根据标准 ETS 分类，这些应属于 Category A，建议明确说明。
- Figure 1 的 ICC 示意图很好但缺少 axis labels（x 轴应为 ability θ，y 轴应为 P(correct)），在 camera-ready 时建议补充。
- Section 4.5 "z = -8σ to -49σ vs. random removal" 的 z 值含义在正文中不够直观——是什么量的 z-score？建议简要说明。
- 论文正文约 8 页（含 figures/tables），在 ACL long paper 的 8 页限制内，格式合规。

---

### Overall Assessment

**Overall**: 3.5 / 5 (Borderline Conference)

**一句话总结**: 方法论扎实且 robustness checks 印象深刻的 psychometric 审计工作，但半合成注入的 ecological validity 不足和因果归因能力的根本局限使得核心发现的 actionability 受限。

**ACL ARR 维度打分**:

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | MH-DIF 应用基本正确，统计检验规范，但 examinees 非独立性的理论影响未充分分析（W2），semi-synthetic injection 的 ecological validity 不足（W1） |
| Excitement | 3/5 | 将成熟的 psychometric 方法应用到 LLM 评估是有价值的跨领域工作，ground truth meta-critique 有启发性，但核心方法是既有技术的直接应用，novelty 有限 |
| Reproducibility | 4/5 | 数据公开（METABENCH），代码提供匿名链接，方法描述详细（K=5 strata, ETS thresholds 等），统计细节充分 |
| Datasets | 3/5 | 未发布新数据集，但对现有数据集的分析有参考价值 |
| Software | 3/5 | 提供了 DIF audit scripts |

**Reviewer Confidence**: 4/5 — 熟悉 IRT/DIF 方法论和 LLM benchmark 评估，仔细检查了核心统计论证。

**理由**: 这篇论文在技术执行上高于平均水平，robustness checks 的覆盖面令人印象深刻，ground truth meta-critique 是一个有价值的方法论洞察。但有两个因素限制了评分：(1) 核心方法（MH-DIF）是教育测量领域的标准工具，创新主要在于应用场景而非方法本身；(2) 无法区分 contamination 和 genuine capability evolution 这一根本局限使得 "31% measurement instability" 的发现难以转化为明确的行动指导——retire flagged items 可能丢弃有价值的 discriminative items，保留它们则 instability 持续存在。如果作者能提供更现实的注入模型（W1）和更充分的 LLM examinees 非独立性分析（W2），本文可以达到 Conference 水准。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 318 · 2026-05-22T01:47:53.342993+00:00_

Reviewer 1 审稿意见已收到（3.5/5, Borderline Conference）。等待 Reviewer 2 返回后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 35

## Round 35

6 recorded events


### User

_source line 319 · 2026-05-22T01:47:54.601597+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models
**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)

---

### Summary (2-3 句)

本文将教育测量中成熟的 Mantel-Haenszel 差异项目功能（MH-DIF）分析方法应用于 LLM benchmark 评估，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU 题目）上发现约 31% 的题目在 2023–2024 模型群组间存在显著时序 DIF（ETS C 级），但排名相关性仍高达 ρ ≈ 0.997。论文同时构建了带跨学科匹配的半合成注入验证框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标记近乎独立（enrichment ≈ 0.96），揭示了现有污染检测验证方法论中的类别错误。

---

### Strengths

**S1** [Rigorous Experimental Design] 实验设计非常严谨，采用了多层对照：随机分割对照（C% = 0.18%）、能力分位对照（2.9%）、族内对照（Llama-2 vs. 3: 61.3%）、1:1 最近邻匹配（C% = 28.9%）、排列检验（p = 0.005），系统地排除了能力混淆、家族结构膨胀、分层方法选择等替代解释（Section 4.4, Table 2）。这种多重 robustness 检查在 NLP 领域的实证论文中很少见。

**S2** [Ground Truth Meta-Critique] Contribution 2（Section 4.3）指出 web-overlap 标签衡量的是 global exposure 而非 differential functioning，两者 enrichment = 0.964、Jaccard = 0.206、φ = 0.012，这是一个重要的方法论洞察，对整个 contamination detection 领域的验证实践有直接影响。这一发现具有超越本文的价值。

**S3** [Cross-Benchmark Replication] 在所有 6 个 METABENCH benchmark 上复现了 temporal DIF 现象（C% = 17.9%–31.3%，45–174× 高于随机基线），且发现 knowledge/reasoning 类 benchmark 的 DIF 率系统性高于 procedural 类（Table 3），增强了结论的 generalizability。

**S4** [Semi-Synthetic Framework] 跨学科匹配的半合成注入框架设计巧妙——通过从匹配变量中排除被注入学科，在理论上消除 FPR 膨胀（ΔFPR = 0.000），同时保持检测力（ΔTPR = +0.508 at p = 0.5）。Remark (Section 3.4) 提供了 FPR = 0 的构造性论证。

**S5** [Conceptual Distinction] Figure 1 清晰地用 ICC 曲线区分了 global contamination 和 differential contamination，这一概念框架有助于读者理解为何 DIF 和 web-overlap 标签测量不同的构念。

---

### Weaknesses

**W1** [critical] **Practical Significance Paradox: ρ ≈ 0.997 严重削弱了 "instability" 叙事的力度**
- 具体位置：Title, Abstract, Section 4.6, Section 5.1
- 问题：论文标题声称 "Measurement Instability"，Abstract 和全文反复强调 31% 的 items 存在 temporal DIF。但 Section 4.6 表明去除全部 DIF 标记项后 Spearman ρ ≈ 0.997——即排名几乎不变。这构成了一个严重的 framing 矛盾：如果去除近三分之一的题目对排名毫无影响，那么这种 "instability" 的实际意义何在？论文试图用 "diagnostic, not destructive" 来调和，但这种表述未能回答一个关键问题：为什么社区应该关注一种不影响实际使用（模型排名）的统计现象？文中提到的 family-level rank shifts（Llama-3: +53, Mistral: -35）是更有说服力的 practical impact 证据，但这些数据被淹没在 ρ ≈ 0.997 的叙事中，且仅出现在附录图中。
- 为什么影响接收：论文的核心 pitch 是 "LLM benchmarks need psychometric monitoring"（Abstract 最后一句），但当 monitoring 发现的问题不影响排名时，这一呼吁的说服力大打折扣。Reviewer 可能认为 contribution 3 的 practical significance 不足以支撑一篇主会议论文。
- 建议修改方向：(1) 重新 frame 论文核心叙事——强调 DIF 作为 capability dimension shift 的诊断工具，而非 benchmark 可靠性的威胁；(2) 将 family-level rank profile 分析从附录提升到正文，作为 practical significance 的主要证据；(3) 讨论 ρ ≈ 0.997 是因为 MMLU 有 12,508 items 的冗余度——在 items 更少的 benchmark（如 TruthfulQA, 817 items）上 DIF 的排名影响可能更大，应提供这些 benchmark 的 ρ 值。

**W2** [critical] **因果归因空白使 audit protocol 的 actionability 存疑**
- 具体位置：Section 5.3, Limitations ¶1
- 问题：Section 5.3 提出了分级行动协议（Monitor/Flag/Act），当 C% ≥ 25% 时建议 "rotate or retire flagged items"。但 Limitations 明确承认 DIF 无法区分 contamination、capability evolution 和 training methodology shifts。如果 DIF 标记的 items 实际上正确反映了模型能力的真实进步（例如 2024 模型在形式逻辑上的提升），那么 retire 这些 items 将移除最具辨别力的题目——论文自身数据显示 DIF items 集中了辨别信号（z = -8σ to -49σ, Section 4.6）。这创造了一个矛盾：被建议移除的 items 恰恰是最有信息量的 items。
- 为什么影响接收：Without causal attribution, the proposed audit protocol is not safely actionable. 一个无法区分 "好的变化"（能力提升）和 "坏的变化"（污染）的审计工具，其建议可能对 benchmark 造成比不审计更大的伤害。
- 建议修改方向：(1) 将 Section 5.3 的 "Act: rotate or retire" 改为更保守的 "investigate and report alongside stable-item rankings"，与论文自身 "diagnostic, not destructive" 的定位一致；(2) 明确指出 DIF audit 的价值在于 flag items for investigation，而非自动化的 retire 决策。

**W3** [warning] **方法新颖性有限——标准方法应用于新领域**
- 具体位置：Section 3.2, Related Work ¶3
- 问题：论文坦承 "We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals"（Related Work ¶3）。MH-DIF 是 1988 年提出的标准方法，ETS 分类是 ETS 的标准实践，跨学科匹配在 DIF 文献中有先例（Nandakumar, 1993; Donoghue, 1993）。论文的方法论贡献集中在半合成验证框架的跨学科匹配变体上。对于 EMNLP 主会议而言，方法新颖性不足可能是一个顾虑——论文的价值主要在实证发现（C1, C3）和方法论批判（C2），而非技术创新。
- 建议：更加突出 C2（ground truth meta-critique）作为主要贡献，因为它对领域的方法论影响最大；C3（大规模实证发现）作为次要贡献。当前三个 contributions 的权重分配使论文看起来更像一个 "method + findings" 论文，但实际上它是一个 "critique + findings" 论文。

**W4** [warning] **`\enlargethispage{18\baselineskip}` 格式操作过于激进**
- 具体位置：`sections/discussion.tex`, line 3
- 问题：Discussion section 使用了 `\enlargethispage{18\baselineskip}`，这相当于在该页额外增加了约 18 行文本空间（≈3.25 英寸或 ≈8.3 cm）。这是一个非常激进的页面扩展操作。虽然 ACL 模板没有明确禁止此命令，但如此大幅度的 margin manipulation 可能被 PC 视为规避页数限制。实际效果是 Discussion + Conclusion 被强行压入第 8 页——如果去除此命令，主体文本很可能溢出到第 9 页，违反 8 页限制。
- 建议：压缩 Discussion section 的内容（部分内容与 Section 4 重复），使内容自然地 fit 在 8 页内，而不依赖 aggressive layout hacks。

**W5** [warning] **半合成框架的注入模型过于简化**
- 具体位置：Section 3.4 (Procedure), Limitations ¶1
- 问题：半合成注入采用二值响应翻转（incorrect → correct），这是最极端的 uniform contamination 模式。Limitations 承认 "Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested"。ΔTPR = +0.508 at p = 0.5 意味着在最有利条件下也只有约 50% 的检测率。在更现实的部分记忆场景下，检测力可能进一步下降。论文将此框架同时用于（a）验证 MH-DIF 的检测能力和（b）证明跨学科匹配的 FPR 控制，(b) 的结论不依赖注入模型的现实性，但 (a) 的说服力受限。
- 建议：明确区分框架对 (a) 和 (b) 的贡献强度，并在正文（而非仅 Limitations）讨论注入模型的局限。

**W6** [warning] **关键统计量的重复呈现降低信息密度**
- 具体位置：Abstract, Section 1, Section 4.2, 4.3, 5.1, 5.2, 6
- 问题：以下统计量在论文中重复出现 4-6 次：enrichment ≈ 0.964, Jaccard = 0.206, φ = 0.012, ρ ≈ 0.997, 31%, z = -8σ to -49σ, ΔFPR = 0.000, ΔTPR = +0.508。Abstract 和 Introduction 的重复可以理解（standalone sections），但 Discussion 和 Conclusion 几乎完全重复了 Experiments 的数字，缺少 high-level synthesis。Conclusion 仅两行，是 Abstract 的压缩版本而非新的综合。
- 建议：Discussion 应少复述数字、多提供 insight；Conclusion 应总结 implications 而非重复统计量。

---

### Questions

**Q1** 论文报告 MMLU 的 ρ ≈ 0.997，但 Table 3 中其他 benchmark（尤其是 items 较少的 TruthfulQA, 817 items）的 stable-item vs. full ranking ρ 值是多少？如果 items 较少的 benchmark 上 ρ 显著低于 0.997，这将大大加强 practical significance 的论证。

**Q2** Section 4.2 报告 difficulty-direction interaction ρ = -0.597：2024 模型在难题上 gain、在易题上 erosion。这个 pattern 是否在 6 个 benchmark 上都一致？如果是，这可能指向特定的训练方法论变化（如 RLHF/DPO 对难题的偏好），值得在 Discussion 中深入探讨。

**Q3** 论文使用 calendar year（2023 vs. 2024）作为 temporal cohort 定义。但 2023 年底和 2024 年初的模型在训练数据上可能高度重叠。6 个月窗口分析（Section 4.7: 2023-H2 vs. 2024-H1, C% = 34.35%）表明 DIF 率甚至更高——这是否暗示 calendar year 划分实际上低估了 temporal DIF？

**Q4** Section 5.3 建议 "当 ≥500 个新模型累积时" 运行 DIF 分析。这个 500 的阈值依据是什么？是否有 power analysis 支撑？Monte Carlo 分析（Section 4.1）显示 N ≥ 80 per cohort 即可达到合理 power——为什么建议 500？

**Q5** 跨学科匹配在 contamination 扩散到 >9% 的 subjects（k > 5）时 ΔFPR 开始膨胀（Section 4.5: 0.026-0.069 at k=10）。在 MMLU 之外的 benchmark（如只有单一 domain 的 GSM8K）上，跨学科匹配如何实现？Section 4.7 提到了 external matching（用 MMLU 分数匹配 GSM8K），但未报告该 setting 下的 FPR 控制细节。

---

### Missing References

1. **Polo et al. (2024) "Efficient Multi-Prompt Evaluation of LLMs"** — 与 tinyBenchmarks 相关的 IRT-based efficient evaluation 工作，可能值得在 IRT in LLM Evaluation 段落中提及。
2. 论文未引用任何关于 **measurement invariance in cross-cultural psychology** 的综述（除 Vandenberg & Lance, 2000），可考虑补充 Putnick & Bornstein (2016) "Measurement invariance conventions and reporting" 作为 DIF 方法论的跨学科支撑。

（总体而言 Related Work 覆盖较完整，以上为 nice-to-have 而非 critical omission。）

---

### Minor Issues

- **M1** [info] Figure 2（dose-response curve）的 y 轴标签 "ΔTPR" 与 x 轴 "Exploitation Rate (p)" 清晰，但缺少 confidence bands 或 error bars（Abstract 提到 5 random seeds）。
- **M2** [info] Table 1 的 "FPR (clean)" 列对于 Within-family 和 Random split 行显示 "--"，应注明原因（是否因这些 cohort 定义下 clean/contaminated 的区分无意义？）。
- **M3** [info] Figure 5（GSM1K correlation）的 N = 33 数据点较少，scatter 中个别 outlier（如左上角两个高 advantage 的模型）对 r 的影响可能过大——是否做过 robust regression 或 leave-one-out 分析？
- **M4** [info] 引用格式小问题：`holland1988mh` 的出版年份可能为 1986 而非 1988（OpenAlex 交叉验证显示 mismatch），建议核实原文出版年。
- **M5** [info] Appendix Section A.1 "Diagnostics" 的排列检验部分引用了 "Yen's Q3"，但正文未定义该统计量，对非心理计量学背景的 NLP 读者不够友好。

---

### Overall Assessment

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法扎实、实验严谨的大规模实证研究，但实际影响被 ρ ≈ 0.997 削弱，方法新颖性有限，因果归因空白使 audit protocol 不够 actionable。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨，多层对照系统排除替代解释；统计方法合理；主要扣分点在于半合成注入模型过于简化，以及因果归因空白使 audit protocol 的 actionability 存疑 |
| Excitement | 3/5 | Ground truth meta-critique（C2）是一个重要的方法论洞察；但核心方法为标准 MH-DIF 的直接应用，无技术创新；practical impact 被 ρ ≈ 0.997 显著削弱 |
| Reproducibility | 4/5 | 代码和数据承诺公开（anonymous repo link）；方法基于公开数据集（METABENCH）；MH-DIF 参数完整指定（K=5, ETS thresholds）；但部分实验细节（如 IRT θ 估计方法）需查阅 PSN-IRT 原文 |
| Confidence | 4/5 | 熟悉 DIF/IRT 方法论和 LLM benchmark evaluation 领域，仔细阅读了全文和附录 |

---

**理由**: 本文的最大优势在于严谨的实验设计和 ground truth meta-critique 的方法论洞察。31% 的 temporal DIF rate 是一个有趣的实证发现，六个 benchmark 的复现增强了结论可靠性。但三个因素拉低了评分：(1) 方法新颖性有限——标准心理计量方法的直接应用；(2) practical significance paradox——ρ ≈ 0.997 使 "instability" 叙事缺乏 urgency；(3) 因果归因空白使 Section 5.3 的 audit protocol 不够 actionable，特别是 "retire flagged items" 的建议可能适得其反。论文适合 Findings，若能解决 framing（强调诊断价值而非 instability 威胁）和 causal attribution（至少提供 case study 级别的归因分析），则可达到 Conference 水平。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿总结**：

- **Overall**: 3.5/5 (Borderline Conference)
- **Soundness**: 3.5/5 — MH-DIF 应用基本正确，但 LLM examinees 非独立性的理论影响未充分讨论
- **Excitement**: 3/5 — 有价值的跨领域应用，但核心方法为既有技术
- **Reproducibility**: 4/5

**主要优势**：cross-subject matching 实现零 FPR 的方法贡献、极广的 robustness checks（6 种替代解释均被排除）、ground truth meta-critique 挑战污染检测社区的评估范式。

**关键问题**：
- **W1**: 半合成注入的 binary flipping 远离真实 contamination 模式，TPR 数字的实际参考价值有限
- **W2**: 对 LLM 群体（非独立 examinees）应用 MH-DIF 的理论适用性论证不足
- **W3**: 无法区分 contamination 与 genuine capability evolution，"retire flagged items" 建议与 DIF items 承载 discriminative signal 的发现存在张力
- **W6**: Cross-subject matching 中 subject 粒度的敏感性未分析

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-22T01:49:03.141702+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应每个 Strength、Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n对 Reviewer 2 的 Missing References 和 Minor Issues 也请简要表态（同意/不同意/补充）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)\n\n---\n\n### Summary (2-3 句)\n\n本文将教育测量中成熟的 Mantel-Haenszel 差异项目功能（MH-DIF）分析方法应用于 LLM benchmark 评估，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU 题目）上发现约 31% 的题目在 2023–2024 模型群组间存在显著时序 DIF（ETS C 级），但排名相关性仍高达 ρ ≈ 0.997。论文同时构建了带跨学科匹配的半合成注入验证框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标记近乎独立（enrichment ≈ 0.96），揭示了现有污染检测验证方法论中的类别错误。\n\n---\n\n### Strengths\n\n**S1** [Rigorous Experimental Design] 实验设计非常严谨，采用了多层对照：随机分割对照（C% = 0.18%）、能力分位对照（2.9%）、族内对照（Llama-2 vs. 3: 61.3%）、1:1 最近邻匹配（C% = 28.9%）、排列检验（p = 0.005），系统地排除了能力混淆、家族结构膨胀、分层方法选择等替代解释（Section 4.4, Table 2）。这种多重 robustness 检查在 NLP 领域的实证论文中很少见。\n\n**S2** [Ground Truth Meta-Critique] Contribution 2（Section 4.3）指出 web-overlap 标签衡量的是 global exposure 而非 differential functioning，两者 enrichment = 0.964、Jaccard = 0.206、φ = 0.012，这是一个重要的方法论洞察，对整个 contamination detection 领域的验证实践有直接影响。这一发现具有超越本文的价值。\n\n**S3** [Cross-Benchmark Replication] 在所有 6 个 METABENCH benchmark 上复现了 temporal DIF 现象（C% = 17.9%–31.3%，45–174× 高于随机基线），且发现 knowledge/reasoning 类 benchmark 的 DIF 率系统性高于 procedural 类（Table 3），增强了结论的 generalizability。\n\n**S4** [Semi-Synthetic Framework] 跨学科匹配的半合成注入框架设计巧妙——通过从匹配变量中排除被注入学科，在理论上消除 FPR 膨胀（ΔFPR = 0.000），同时保持检测力（ΔTPR = +0.508 at p = 0.5）。Remark (Section 3.4) 提供了 FPR = 0 的构造性论证。\n\n**S5** [Conceptual Distinction] Figure 1 清晰地用 ICC 曲线区分了 global contamination 和 differential contamination，这一概念框架有助于读者理解为何 DIF 和 web-overlap 标签测量不同的构念。\n\n---\n\n### Weaknesses\n\n**W1** [critical] **Practical Significance Paradox: ρ ≈ 0.997 严重削弱了 \"instability\" 叙事的力度**\n- 具体位置：Title, Abstract, Section 4.6, Section 5.1\n- 问题：论文标题声称 \"Measurement Instability\"，Abstract 和全文反复强调 31% 的 items 存在 temporal DIF。但 Section 4.6 表明去除全部 DIF 标记项后 Spearman ρ ≈ 0.997——即排名几乎不变。这构成了一个严重的 framing 矛盾：如果去除近三分之一的题目对排名毫无影响，那么这种 \"instability\" 的实际意义何在？论文试图用 \"diagnostic, not destructive\" 来调和，但这种表述未能回答一个关键问题：为什么社区应该关注一种不影响实际使用（模型排名）的统计现象？文中提到的 family-level rank shifts（Llama-3: +53, Mistral: -35）是更有说服力的 practical impact 证据，但这些数据被淹没在 ρ ≈ 0.997 的叙事中，且仅出现在附录图中。\n- 建议修改方向：(1) 重新 frame 论文核心叙事——强调 DIF 作为 capability dimension shift 的诊断工具，而非 benchmark 可靠性的威胁；(2) 将 family-level rank profile 分析从附录提升到正文，作为 practical significance 的主要证据；(3) 讨论 ρ ≈ 0.997 是因为 MMLU 有 12,508 items 的冗余度——在 items 更少的 benchmark（如 TruthfulQA, 817 items）上 DIF 的排名影响可能更大，应提供这些 benchmark 的 ρ 值。\n\n**W2** [critical] **因果归因空白使 audit protocol 的 actionability 存疑**\n- 具体位置：Section 5.3, Limitations ¶1\n- 问题：Section 5.3 提出了分级行动协议（Monitor/Flag/Act），当 C% ≥ 25% 时建议 \"rotate or retire flagged items\"。但 Limitations 明确承认 DIF 无法区分 contamination、capability evolution 和 training methodology shifts。如果 DIF 标记的 items 实际上正确反映了模型能力的真实进步，DIF items 集中了辨别信号（z = -8σ to -49σ），retire 这些 items 将移除最具辨别力的题目。\n- 建议修改方向：将 \"Act: rotate or retire\" 改为更保守的 \"investigate and report alongside stable-item rankings\"。\n\n**W3** [warning] **方法新颖性有限——标准方法应用于新领域**\n- 具体位置：Section 3.2, Related Work ¶3\n- 问题：MH-DIF 是 1988 年的标准方法，ETS 分类是标准实践。对于 EMNLP 主会议，方法新颖性不足可能是一个顾虑——论文的价值主要在实证发现和方法论批判。\n- 建议：更加突出 C2（ground truth meta-critique）作为主要贡献。\n\n**W4** [warning] **`\\enlargethispage{18\\baselineskip}` 格式操作过于激进**\n- 具体位置：`sections/discussion.tex`, line 3\n- 问题：Discussion section 使用了 `\\enlargethispage{18\\baselineskip}`，相当于额外增加约 18 行文本空间（≈8.3 cm）。如此大幅度的 margin manipulation 可能被 PC 视为规避页数限制。去除此命令后主体文本很可能溢出到第 9 页。\n\n**W5** [warning] **半合成框架的注入模型过于简化**\n- 具体位置：Section 3.4, Limitations ¶1\n- 问题：ΔTPR = +0.508 at p = 0.5 意味着在最有利条件下也只有约 50% 的检测率。更现实的部分记忆场景下检测力可能进一步下降。\n- 建议：明确区分框架对 FPR 控制（不依赖注入模型现实性）和 TPR 估计（受注入模型限制）的贡献强度。\n\n**W6** [warning] **关键统计量的重复呈现降低信息密度**\n- 问题：enrichment ≈ 0.964, ρ ≈ 0.997, 31%, ΔFPR = 0.000, ΔTPR = +0.508 等在论文中重复 4-6 次。Discussion 几乎完全重复 Experiments 的数字，Conclusion 仅两行。\n\n---\n\n### Questions\n\n**Q1** Table 3 中其他 benchmark（尤其是 items 较少的 TruthfulQA, 817 items）的 stable-item vs. full ranking ρ 值是多少？\n**Q2** difficulty-direction interaction ρ = -0.597 是否在 6 个 benchmark 上都一致？\n**Q3** 6 个月窗口分析 C% = 34.35% 是否暗示 calendar year 划分低估了 temporal DIF？\n**Q4** Section 5.3 建议 500 个新模型累积时运行 DIF，阈值依据是什么？\n**Q5** 在单一 domain benchmark（如 GSM8K）上，跨学科匹配如何实现？\n\n---\n\n### Missing References\n\n1. Polo et al. (2024) \"Efficient Multi-Prompt Evaluation of LLMs\" — IRT-based efficient evaluation\n2. Putnick & Bornstein (2016) \"Measurement invariance conventions and reporting\" — DIF 方法论的跨学科支撑\n\n### Minor Issues\n\n- M1: Figure 2 缺少 confidence bands\n- M2: Table 1 \"--\" 列应注明原因\n- M3: Figure 5 N=33 outlier 影响\n- M4: holland1988mh 出版年份可能为 1986\n- M5: Appendix \"Yen's Q3\" 未在正文定义"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "irt_equated_bench_regen",
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应每个 Strength、Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n对 Reviewer 2 的 Missing References 和 Minor Issues 也请简要表态（同意/不同意/补充）。\n\n---\n\n## Reviewer 2 审稿意见 — Round 1\n\n**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)\n\n---\n\n### Summary (2-3 句)\n\n本文将教育测量中成熟的 Mantel-Haenszel 差异项目功能（MH-DIF）分析方法应用于 LLM benchmark 评估，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU 题目）上发现约 31% 的题目在 2023–2024 模型群组间存在显著时序 DIF（ETS C 级），但排名相关性仍高达 ρ ≈ 0.997。论文同时构建了带跨学科匹配的半合成注入验证框架（ΔFPR = 0.000），并指出 web-overlap 污染标签与 DIF 标记近乎独立（enrichment ≈ 0.96），揭示了现有污染检测验证方法论中的类别错误。\n\n---\n\n### Strengths\n\n**S1** [Rigorous Experimental Design] 实验设计非常严谨，采用了多层对照：随机分割对照（C% = 0.18%）、能力分位对照（2.9%）、族内对照（Llama-2 vs. 3: 61.3%）、1:1 最近邻匹配（C% = 28.9%）、排列检验（p = 0.005），系统地排除了能力混淆、家族结构膨胀、分层方法选择等替代解释（Section 4.4, Table 2）。这种多重 robustness 检查在 NLP 领域的实证论文中很少见。\n\n**S2** [Ground Truth Meta-Critique] Contribution 2（Section 4.3）指出 web-overlap 标签衡量的是 global exposure 而非 differential functioning，两者 enrichment = 0.964、Jaccard = 0.206、φ = 0.012，这是一个重要的方法论洞察，对整个 contamination detection 领域的验证实践有直接影响。这一发现具有超越本文的价值。\n\n**S3** [Cross-Benchmark Replication] 在所有 6 个 METABENCH benchmark 上复现了 temporal DIF 现象（C% = 17.9%–31.3%，45–174× 高于随机基线），且发现 knowledge/reasoning 类 benchmark 的 DIF 率系统性高于 procedural 类（Table 3），增强了结论的 generalizability。\n\n**S4** [Semi-Synthetic Framework] 跨学科匹配的半合成注入框架设计巧妙——通过从匹配变量中排除被注入学科，在理论上消除 FPR 膨胀（ΔFPR = 0.000），同时保持检测力（ΔTPR = +0.508 at p = 0.5）。Remark (Section 3.4) 提供了 FPR = 0 的构造性论证。\n\n**S5** [Conceptual Distinction] Figure 1 清晰地用 ICC 曲线区分了 global contamination 和 differential contamination，这一概念框架有助于读者理解为何 DIF 和 web-overlap 标签测量不同的构念。\n\n---\n\n### Weaknesses\n\n**W1** [critical] **Practical Significance Paradox: ρ ≈ 0.997 严重削弱了 \"instability\" 叙事的力度**\n- 具体位置：Title, Abstract, Section 4.6, Section 5.1\n- 问题：论文标题声称 \"Measurement Instability\"，Abstract 和全文反复强调 31% 的 items 存在 temporal DIF。但 Section 4.6 表明去除全部 DIF 标记项后 Spearman ρ ≈ 0.997——即排名几乎不变。这构成了一个严重的 framing 矛盾：如果去除近三分之一的题目对排名毫无影响，那么这种 \"instability\" 的实际意义何在？论文试图用 \"diagnostic, not destructive\" 来调和，但这种表述未能回答一个关键问题：为什么社区应该关注一种不影响实际使用（模型排名）的统计现象？文中提到的 family-level rank shifts（Llama-3: +53, Mistral: -35）是更有说服力的 practical impact 证据，但这些数据被淹没在 ρ ≈ 0.997 的叙事中，且仅出现在附录图中。\n- 建议修改方向：(1) 重新 frame 论文核心叙事——强调 DIF 作为 capability dimension shift 的诊断工具，而非 benchmark 可靠性的威胁；(2) 将 family-level rank profile 分析从附录提升到正文，作为 practical significance 的主要证据；(3) 讨论 ρ ≈ 0.997 是因为 MMLU 有 12,508 items 的冗余度——在 items 更少的 benchmark（如 TruthfulQA, 817 items）上 DIF 的排名影响可能更大，应提供这些 benchmark 的 ρ 值。\n\n**W2** [critical] **因果归因空白使 audit protocol 的 actionability 存疑**\n- 具体位置：Section 5.3, Limitations ¶1\n- 问题：Section 5.3 提出了分级行动协议（Monitor/Flag/Act），当 C% ≥ 25% 时建议 \"rotate or retire flagged items\"。但 Limitations 明确承认 DIF 无法区分 contamination、capability evolution 和 training methodology shifts。如果 DIF 标记的 items 实际上正确反映了模型能力的真实进步，DIF items 集中了辨别信号（z = -8σ to -49σ），retire 这些 items 将移除最具辨别力的题目。\n- 建议修改方向：将 \"Act: rotate or retire\" 改为更保守的 \"investigate and report alongside stable-item rankings\"。\n\n**W3** [warning] **方法新颖性有限——标准方法应用于新领域**\n- 具体位置：Section 3.2, Related Work ¶3\n- 问题：MH-DIF 是 1988 年的标准方法，ETS 分类是标准实践。对于 EMNLP 主会议，方法新颖性不足可能是一个顾虑——论文的价值主要在实证发现和方法论批判。\n- 建议：更加突出 C2（ground truth meta-critique）作为主要贡献。\n\n**W4** [warning] **`\\enlargethispage{18\\baselineskip}` 格式操作过于激进**\n- 具体位置：`sections/discussion.tex`, line 3\n- 问题：Discussion section 使用了 `\\enlargethispage{18\\baselineskip}`，相当于额外增加约 18 行文本空间（≈8.3 cm）。如此大幅度的 margin manipulation 可能被 PC 视为规避页数限制。去除此命令后主体文本很可能溢出到第 9 页。\n\n**W5** [warning] **半合成框架的注入模型过于简化**\n- 具体位置：Section 3.4, Limitations ¶1\n- 问题：ΔTPR = +0.508 at p = 0.5 意味着在最有利条件下也只有约 50% 的检测率。更现实的部分记忆场景下检测力可能进一步下降。\n- 建议：明确区分框架对 FPR 控制（不依赖注入模型现实性）和 TPR 估计（受注入模型限制）的贡献强度。\n\n**W6** [warning] **关键统计量的重复呈现降低信息密度**\n- 问题：enrichment ≈ 0.964, ρ ≈ 0.997, 31%, ΔFPR = 0.000, ΔTPR = +0.508 等在论文中重复 4-6 次。Discussion 几乎完全重复 Experiments 的数字，Conclusion 仅两行。\n\n---\n\n### Questions\n\n**Q1** Table 3 中其他 benchmark（尤其是 items 较少的 TruthfulQA, 817 items）的 stable-item vs. full ranking ρ 值是多少？\n**Q2** difficulty-direction interaction ρ = -0.597 是否在 6 个 benchmark 上都一致？\n**Q3** 6 个月窗口分析 C% = 34.35% 是否暗示 calendar year 划分低估了 temporal DIF？\n**Q4** Section 5.3 建议 500 个新模型累积时运行 DIF，阈值依据是什么？\n**Q5** 在单一 domain benchmark（如 GSM8K）上，跨学科匹配如何实现？\n\n---\n\n### Missing References\n\n1. Polo et al. (2024) \"Efficient Multi-Prompt Evaluation of LLMs\" — IRT-based efficient evaluation\n2. Putnick & Bornstein (2016) \"Measurement invariance conventions and reporting\" — DIF 方法论的跨学科支撑\n\n### Minor Issues\n\n- M1: Figure 2 缺少 confidence bands\n- M2: Table 1 \"--\" 列应注明原因\n- M3: Figure 5 N=33 outlier 影响\n- M4: holland1988mh 出版年份可能为 1986\n- M5: Appendix \"Yen's Q3\" 未在正文定义"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-22T01:49:46.885134+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 43743
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-22T01:49:47.236861+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应每个 Strength、Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n对 Reviewer 1 的 Missing References 和 Minor Issues 也请简要表态（同意/不同意/补充）。\n\n---\n\n## Reviewer 1 审稿意见\n\n---\n\n### Summary (2-3 句)\n\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 METABENCH 六个 benchmark 中 17.9%–31.3% 的题目在 2023 与 2024 模型 cohort 之间存在大幅度时序测量不稳定性（ETS-C 分类）。作者提出 cross-subject matching 的半合成注入框架实现 ΔFPR=0.000，并揭示 web-overlap 污染标签与 DIF flag 近乎独立（enrichment≈0.96），指出现有污染检测的 ground truth 存在类别错误。论文方法论严谨、robustness check 覆盖面广，但在注入模型的 ecological validity、因果归因能力、以及 DIF 方法对 LLM 群体适用性的论证上存在值得讨论的问题。\n\n---\n\n### Strengths\n\n**S1 [方法论贡献清晰且可复用]** Cross-subject matching 实现 ΔFPR=0.000 的方法贡献干净利落（Section 3.4, Remark），multi-subject injection 的优雅退化分析（Appendix Table 5：k≤5 时 ΔFPR<0.007，k=10 时升至 0.047）为实际应用划定了清晰的适用边界。\n\n**S2 [Robustness check 覆盖面极广]** 系统性排除 6 种替代解释，C% 在多种 matching 策略下均稳定在 ~28-29%。随机拆分对照组 C%=0.18% 与能力分位数对照组 C%=2.9% 提供有说服力的 null baseline。\n\n**S3 [Ground truth meta-critique 具有启发性]** web-overlap labels 与 DIF flags 近乎正交（enrichment=0.964, Jaccard=0.206, φ=0.012），挑战整个污染检测社区的评估范式。\n\n**S4 [跨 benchmark 复现]** 六个 benchmark 均展示显著 temporal DIF（45-174× above baseline），knowledge/reasoning > procedural 的模式合理。\n\n**S5 [统计报告规范]** 几乎所有核心数字都附有 CI/效应量/多重比较校正。\n\n**S6 [Simpson's paradox 分析精巧]** 92.4% item-specific DIF（pseudo R²=0.0007），domain-level OR 反转（1.55→0.73）。\n\n---\n\n### Weaknesses\n\n**W1 [warning] 半合成注入的 ecological validity 不足**\n- Binary flipping 是最极端的均匀利用模式。真实 contamination 表现为部分记忆、推理捷径、格式敏感性等。ΔTPR=+0.508 at p=0.5 的实际参考价值有限。\n- 建议提供更现实的注入模型（按 difficulty 分层的非均匀 flipping 或仅翻转高区分度 items）。\n\n**W2 [warning] 对 LLM 群体应用 MH-DIF 的理论适用性论证不够充分**\n- MH χ² 依赖 examinees 独立性假设。LLM 共享训练数据、架构、base model，不满足独立采样。Graduated de-duplication 是经验层面处理，缺乏理论讨论。\n- 建议讨论 MH test 在 clustered/non-independent examinees 下的 size 表现，引用 French & Finch (2010)。\n\n**W3 [warning] 因果归因局限使 \"measurement instability\" framing 可能误导**\n- DIF 可能源于 genuine capability evolution，retire 这些 items 反而丢失 discriminative signal（z = -8σ to -49σ）。\"retire flagged items\" 与数据发现存在张力。\n- 建议讨论 DIF 作为 \"measurement instability\"（问题）vs \"expected sensitivity\"（特征）的区分。\n\n**W4 [info] Permutation test 200 次迭代偏少**\n- p=0.005 恰为分辨率极限（1/200）。建议增至 1,000 次。\n\n**W5 [info] ρ≈0.997 排名相关性的解读需更多 nuance**\n- 高 ρ 部分归因于 MMLU 12,508 items 的冗余度。建议报告 pairwise model comparison 翻转率。\n\n**W6 [warning] Cross-subject matching 中 subject 粒度敏感性未分析**\n- MMLU 57 个 subjects 大小差异大，小 subject 排除后 matching variable 受影响小，可能仍包含被测 items 信号。\n- 建议报告 subject-level C% 与 subject size 的相关性。\n\n---\n\n### Questions\n\n**Q1** 1:1 nearest-neighbor matching 是用 model 总分还是 IRT θ？matched 后 cohort 大小从 (1080, 807) 降到 (638, 638)，是否引入 selection bias？\n\n**Q2** Power analysis 使用 2PL 参数但 Appendix A.2 指出 2PL 拟合差——power analysis 的可靠性如何？\n\n**Q3** Within-subject C%=38.1% > Temporal 31.3%，原因是什么？是否做了 simulation 校准 type-I error rate？\n\n**Q4** GSM1K 的 r=-0.478 (N=33) 在 Abstract 中被用于支撑 \"DIF captures capability change distinct from memorization\"，但样本量很小——能否明确区分 confirmed vs exploratory findings？\n\n**Q5** IRT θ 与 total scores 相关 r=0.9986，IRT framing 的附加价值是什么？\n\n---\n\n### Missing References\n\n- French & Finch (2010) — clustered data 中 DIF 检测的多层次方法\n- Magis & De Boeck (2012) — DIF 检测中 type-I error 控制替代方法\n- Kolen & Brennan (2014) — 经典 equating 文献\n\n### Minor Issues\n\n- Abstract 行文密度过高\n- ETS Category B 定义缺少 |Δ_MH|<1.0 且有显著性的情况\n- Figure 1 缺少 axis labels\n- Section 4.5 z 值含义不够直观\n- 正文约 8 页，格式合规"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "irt_equated_bench_regen",
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应每个 Strength、Weakness 和 Question：用 **[AGREE]** 表示同意并说明理由，或用 **[REBUT]** 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n对 Reviewer 1 的 Missing References 和 Minor Issues 也请简要表态（同意/不同意/补充）。\n\n---\n\n## Reviewer 1 审稿意见\n\n---\n\n### Summary (2-3 句)\n\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 METABENCH 六个 benchmark 中 17.9%–31.3% 的题目在 2023 与 2024 模型 cohort 之间存在大幅度时序测量不稳定性（ETS-C 分类）。作者提出 cross-subject matching 的半合成注入框架实现 ΔFPR=0.000，并揭示 web-overlap 污染标签与 DIF flag 近乎独立（enrichment≈0.96），指出现有污染检测的 ground truth 存在类别错误。论文方法论严谨、robustness check 覆盖面广，但在注入模型的 ecological validity、因果归因能力、以及 DIF 方法对 LLM 群体适用性的论证上存在值得讨论的问题。\n\n---\n\n### Strengths\n\n**S1 [方法论贡献清晰且可复用]** Cross-subject matching 实现 ΔFPR=0.000 的方法贡献干净利落（Section 3.4, Remark），multi-subject injection 的优雅退化分析（Appendix Table 5：k≤5 时 ΔFPR<0.007，k=10 时升至 0.047）为实际应用划定了清晰的适用边界。\n\n**S2 [Robustness check 覆盖面极广]** 系统性排除 6 种替代解释，C% 在多种 matching 策略下均稳定在 ~28-29%。随机拆分对照组 C%=0.18% 与能力分位数对照组 C%=2.9% 提供有说服力的 null baseline。\n\n**S3 [Ground truth meta-critique 具有启发性]** web-overlap labels 与 DIF flags 近乎正交（enrichment=0.964, Jaccard=0.206, φ=0.012），挑战整个污染检测社区的评估范式。\n\n**S4 [跨 benchmark 复现]** 六个 benchmark 均展示显著 temporal DIF（45-174× above baseline），knowledge/reasoning > procedural 的模式合理。\n\n**S5 [统计报告规范]** 几乎所有核心数字都附有 CI/效应量/多重比较校正。\n\n**S6 [Simpson's paradox 分析精巧]** 92.4% item-specific DIF（pseudo R²=0.0007），domain-level OR 反转（1.55→0.73）。\n\n---\n\n### Weaknesses\n\n**W1 [warning] 半合成注入的 ecological validity 不足**\n- Binary flipping 是最极端的均匀利用模式。真实 contamination 表现为部分记忆、推理捷径、格式敏感性等。ΔTPR=+0.508 at p=0.5 的实际参考价值有限。\n- 建议提供更现实的注入模型（按 difficulty 分层的非均匀 flipping 或仅翻转高区分度 items）。\n\n**W2 [warning] 对 LLM 群体应用 MH-DIF 的理论适用性论证不够充分**\n- MH χ² 依赖 examinees 独立性假设。LLM 共享训练数据、架构、base model，不满足独立采样。Graduated de-duplication 是经验层面处理，缺乏理论讨论。\n- 建议讨论 MH test 在 clustered/non-independent examinees 下的 size 表现，引用 French & Finch (2010)。\n\n**W3 [warning] 因果归因局限使 \"measurement instability\" framing 可能误导**\n- DIF 可能源于 genuine capability evolution，retire 这些 items 反而丢失 discriminative signal（z = -8σ to -49σ）。\"retire flagged items\" 与数据发现存在张力。\n- 建议讨论 DIF 作为 \"measurement instability\"（问题）vs \"expected sensitivity\"（特征）的区分。\n\n**W4 [info] Permutation test 200 次迭代偏少**\n- p=0.005 恰为分辨率极限（1/200）。建议增至 1,000 次。\n\n**W5 [info] ρ≈0.997 排名相关性的解读需更多 nuance**\n- 高 ρ 部分归因于 MMLU 12,508 items 的冗余度。建议报告 pairwise model comparison 翻转率。\n\n**W6 [warning] Cross-subject matching 中 subject 粒度敏感性未分析**\n- MMLU 57 个 subjects 大小差异大，小 subject 排除后 matching variable 受影响小，可能仍包含被测 items 信号。\n- 建议报告 subject-level C% 与 subject size 的相关性。\n\n---\n\n### Questions\n\n**Q1** 1:1 nearest-neighbor matching 是用 model 总分还是 IRT θ？matched 后 cohort 大小从 (1080, 807) 降到 (638, 638)，是否引入 selection bias？\n\n**Q2** Power analysis 使用 2PL 参数但 Appendix A.2 指出 2PL 拟合差——power analysis 的可靠性如何？\n\n**Q3** Within-subject C%=38.1% > Temporal 31.3%，原因是什么？是否做了 simulation 校准 type-I error rate？\n\n**Q4** GSM1K 的 r=-0.478 (N=33) 在 Abstract 中被用于支撑 \"DIF captures capability change distinct from memorization\"，但样本量很小——能否明确区分 confirmed vs exploratory findings？\n\n**Q5** IRT θ 与 total scores 相关 r=0.9986，IRT framing 的附加价值是什么？\n\n---\n\n### Missing References\n\n- French & Finch (2010) — clustered data 中 DIF 检测的多层次方法\n- Magis & De Boeck (2012) — DIF 检测中 type-I error 控制替代方法\n- Kolen & Brennan (2014) — 经典 equating 文献\n\n### Minor Issues\n\n- Abstract 行文密度过高\n- ETS Category B 定义缺少 |Δ_MH|<1.0 且有显著性的情况\n- Figure 1 缺少 axis labels\n- Section 4.5 z 值含义不够直观\n- 正文约 8 页，格式合规"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-22T01:49:48.846798+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1609
}
```

</details>

---


### Assistant

_source line 324 · 2026-05-22T01:49:55.518072+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 325 · 2026-05-22T01:49:58.286582+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**: Overall 3.5 (Borderline Conference)

**核心判断**:
- **Soundness 4/5**: 实验设计严谨，多层对照排除替代解释
- **Excitement 3/5**: Ground truth meta-critique 有价值，但方法为标准 MH-DIF 直接应用
- **关键问题**: (1) ρ ≈ 0.997 削弱了 "instability" 叙事的 practical urgency；(2) 因果归因空白使 audit protocol（特别是 "retire flagged items"）可能适得其反——被建议移除的 items 恰恰集中了最多辨别信息；(3) `\enlargethispage{18\baselineskip}` 格式操作激进

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 326 · 2026-05-22T01:50:03.151488+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 327 · 2026-05-22T01:51:08.141182+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 Round 1 审稿意见的逐条回应

---

### Strengths 回应

**[AGREE] R2-S1 (Rigorous Experimental Design)**
完全同意。多层对照设计是本文最大的方法论优势，与我在 R1-S2 中的评价一致。特别值得强调的是，六种替代解释的系统排除（Section 4.4, Table 2）和 ~28-29% 的 C% floor 在多种 matching 策略下的一致性，在 NLP 实证论文中确实罕见。

**[AGREE] R2-S2 (Ground Truth Meta-Critique)**
完全同意，与我的 R1-S3 一致。enrichment=0.964、Jaccard=0.206、φ=0.012 的正交性发现（Section 4.3）对整个 contamination detection 领域的验证范式有超越本文的影响。

**[AGREE] R2-S3 (Cross-Benchmark Replication)**
同意，与我的 R1-S4 一致。六个 benchmark 的复现（Table 3）增强了 generalizability，knowledge vs. procedural 的差异模式合理。

**[AGREE] R2-S4 (Semi-Synthetic Framework)**
同意，与我的 R1-S1 一致。cross-subject matching 的 Remark（Section 3.4）提供了干净的构造性论证。

**[AGREE] R2-S5 (Conceptual Distinction)**
同意。Figure 1 的 ICC 示意图有效地帮助读者区分 global vs. differential contamination 这两个容易混淆的概念。不过我在 Minor Issues 中指出 Figure 1 缺少 axis labels（θ vs. P(correct)），建议在 camera-ready 时补充。

---

### Weaknesses 回应

**[AGREE] R2-W1 (Practical Significance Paradox: ρ ≈ 0.997)**
基本同意，这与我的 R1-W5 高度重叠。ρ ≈ 0.997 确实削弱了 "instability" 叙事的紧迫性。R2 的三点建议都很好，特别是第三点——在 items 更少的 benchmark 上报告 ρ 值。TruthfulQA 只有 817 items（Table 3），如果其 C%=29.7%，去除 ~240 个 DIF items 后对排名的影响可能远大于 MMLU。论文没有提供这个数据是一个明显的遗漏。

不过我想补充一个 nuance：R2 将此标为 [critical] 可能稍重。论文在 Section 4.5 中确实提到了 family-level rank shifts（Llama-3: +53, Mistral: -35），这些 shift 对 pairwise model selection 有实际意义。问题不在于发现本身无意义，而在于论文的 framing 重心放错了——应该从 "benchmark reliability threat" 转向 "diagnostic tool for capability dimension shifts"。这是 framing 问题，不是 substance 问题。

**[AGREE] R2-W2 (因果归因空白使 audit protocol actionability 存疑)**
完全同意，这与我的 R1-W3 高度一致。Section 5.3 的 "rotate or retire" 建议与 Section 4.5 中 DIF items 承载 z = -8σ to -49σ 的 discriminative signal 这一发现之间存在直接矛盾。R2 建议改为 "investigate and report alongside stable-item rankings" 更为合理。我在 R1-W3 中也提出了类似建议——论文需要更明确地讨论何时 DIF 是问题（measurement artifact）vs. 特征（genuine sensitivity to change）。

**[REBUT] R2-W3 (方法新颖性有限)**
部分不同意。R2 认为 "MH-DIF 是 1988 年的标准方法，方法新颖性不足"，这个批评本身成立但不应作为 EMNLP 论文的主要 weakness。理由如下：

1. ARR reviewer guidelines 明确指出不应因方法不够 "complex" 而贬低论文——"simpler methods that work should not be penalized"（H14 pitfall）。
2. 本文的贡献定位为 "methodological and empirical, not algorithmic"（Section 1 最后一段），这是合理的。
3. Cross-subject matching 的 ΔFPR=0.000 保证（Section 3.4 Remark）虽然建立在 MH-DIF 之上，但作为针对 LLM benchmark 场景的方法改进具有独立价值。
4. Ground truth meta-critique（Contribution 2）本身就是方法论层面的新颖洞察。

EMNLP Findings track 明确接收 "sound and reproducible" 的实证贡献。即使对 Main track 来说，novelty 可以来自问题定义和实证发现，而非必须来自方法本身。不过我同意 R2 的建议——更突出 C2 作为主要贡献会加强论文。

**[AGREE] R2-W4 (`\enlargethispage{18\baselineskip}` 格式操作过于激进)**
同意这是一个需要关注的问题。18\baselineskip 约等于额外 18 行（~8-9 cm），这不是标准的微调而是大幅度 margin manipulation。从 discussion.tex line 3 的证据来看，如果去除此命令，Discussion section 很可能导致正文溢出到第 9 页，违反 EMNLP long paper 的 8 页限制。

不过我要指出：这个问题属于格式合规范畴，不应影响论文的学术评价。如果正文确实在 8 页内（含 Discussion），作者可能需要在 camera-ready 时压缩 Discussion，但这是可操作的修改——重复性内容（R2-W6 指出的问题）的删减可以腾出空间。我不建议将此标为影响接收决定的因素。

**[AGREE] R2-W5 (半合成框架注入模型过于简化)**
同意，与我的 R1-W1 一致。我特别赞同 R2 提出的区分——框架对 FPR 控制的贡献（ΔFPR=0.000 不依赖注入模型现实性，因为这是 matching variable 构造的性质）与 TPR 估计的贡献（受注入模型限制）应该明确区分。论文在 Limitations 中已部分提到这一点（"the framework's primary methodological contribution—cross-subject matching achieving ΔFPR=0.000—is a matching strategy property independent of injection realism"），但在正文 Section 3.4 和 Section 4.1 中没有足够强调这个重要区分。

**[REBUT] R2-W6 (关键统计量的重复呈现)**
部分不同意。学术论文中核心数字在 Abstract→Introduction→Results→Discussion→Conclusion 的重复是正常的写作惯例，因为读者可能只读特定 section。但我承认本文的重复程度偏高——例如 enrichment≈0.964 在正文中出现了至少 5 次，ΔFPR=0.000 也出现了类似次数。

然而，我不认为这是一个 weakness——它更多是 writing style 的问题。Discussion 的功能本就是将 Results 重新整合到更大的 context 中，必然会引用相同数字。Conclusion 只有两行恰恰是因为论文选择不再重复。R2 将此标为 [warning] 等级偏高——建议降为 Minor Issue。

---

### Questions 回应

**[AGREE] R2-Q1 (其他 benchmark 的 stable-item vs. full ranking ρ)**
这是一个关键遗漏。论文只报告了 MMLU 的 ρ≈0.997，但没有报告 TruthfulQA (817 items)、ARC (1,172 items)、GSM8K (1,319 items) 等较小 benchmark 的 ρ。考虑到这些 benchmark 的 item 数量仅为 MMLU 的 1/10 到 1/15，DIF items 的移除对排名的影响可能显著更大。这直接关系到 W1 中 practical significance 的评估。与我的 R1-W5 中建议报告 pairwise comparison flip rate 相呼应。

**[AGREE] R2-Q2 (difficulty-direction interaction 跨 benchmark 一致性)**
好问题。ρ=-0.597 仅在 MMLU 上报告（Section 4.2），如果这个模式在 GSM8K 或其他 benchmark 上也成立，将大大增强 "hard items gain, easy items erode" 这一发现的 generalizability。反之，如果不一致，可能暗示这是 MMLU 的特异性。

**[AGREE] R2-Q3 (6 个月窗口 C%=34.35% 暗示 calendar year 划分可能低估)**
有趣的观察。Section 4.7 提到 6 个月窗口（2023-H2 vs. 2024-H1）C%=34.35%，这确实高于全年 31.3%。可能的解释是 6 个月窗口内模型变化更集中，但论文没有深入分析。这暗示 temporal resolution 的选择影响 DIF 估计——如果更细粒度的时间划分产生更高的 C%，那么 31.3% 可能是一个保守估计。

**[REBUT] R2-Q4 (500 模型阈值的依据)**
这个问题可以从论文中部分回答。Section 4.1 的 power analysis 表明在 N≥80 per cohort 时 ETS-C 的 TPR 为 0.68-0.80（Appendix Table 4），论文的实际 cohort sizes（1,080 和 807）远超这个阈值。500 个新模型的建议（Section 5.3）虽然没有 formal justification，但考虑到 N≥80 的 power threshold，500 个新模型足以构成一个有统计效力的 focal group。不过我同意 R2 的暗示——这个阈值应该更明确地与 power analysis 结论挂钩。

**[AGREE] R2-Q5 (单一 domain benchmark 上的跨学科匹配)**
好问题，但论文已在 Section 3.2 中回答。论文定义了三种 matching 策略：(1) standard matching（within-benchmark total score），(2) cross-subject matching（排除当前 subject 的 total score），(3) external matching（使用不同 benchmark 的 total score）。对于 GSM8K 这样的单一 domain benchmark，使用策略 (3) external matching——例如用 MMLU total score 作为 matching variable。Appendix Table 6 中 GSM8K 的 ΔTPR 就是在 external matching 下报告的（$p=0.5$, external: +0.514）。不过论文确实没有在正文中对此做充分说明，应在 Section 3.2 或 Section 4.7 中明确 GSM8K 使用了 external matching。

---

### Missing References 回应

**R2-Ref1 (Polo et al. 2024, IRT-based efficient evaluation)**
[AGREE] 相关但非必须。论文 Related Work (Section 2) 已引用了 Polo et al. (2024) 关于 "TinyBenchmarks"（line numbers visible in related_work.tex），如果 R2 指的是另一篇 Polo et al. 工作则需要补充。

**R2-Ref2 (Putnick & Bornstein 2016, Measurement invariance conventions)**
[AGREE] 值得引用。Measurement invariance 的跨领域综述可以帮助 NLP 读者理解 DIF 在更广泛的 psychometric framework 中的位置。这与我在 R1 Missing References 中建议引用 Kolen & Brennan (2014) 的 equating 文献相呼应——论文整体上缺少经典 psychometric 综述文献。

---

### Minor Issues 回应

**[AGREE] R2-M1 (Figure 2 缺少 confidence bands)**: 同意。5 random seeds 的变异应以 error bands 呈现。

**[AGREE] R2-M2 (Table 1 "--" 列应注明原因)**: 同意。Within-family 和 Random split 行的 FPR/Enrichment 列为 "--"，应在 caption 或 footnote 中说明原因（可能是因为这些 cohort 没有对应的 web-overlap label 分析）。

**[AGREE] R2-M3 (Figure 5 N=33 outlier 影响)**: 同意。N=33 且 r=-0.478 的相关性对 outlier 敏感。论文已标注为 exploratory，但应报告 robust correlation 或 leave-one-out 影响分析。与我的 R1-Q4 中关于 GSM1K 分析 exploratory nature 的关切一致。

**[REBUT] R2-M4 (holland1988mh 出版年份)**: Holland & Thayer 的 MH-DIF 程序描述发表于 1988 年的 *ETS Research Report* 系列（RR-88-31），论文引用年份 1988 是正确的。R2 可能混淆了 Holland & Thayer (1988) 与 Mantel & Haenszel (1959) 的原始统计检验——后者确实更早，但论文引用的是 Holland & Thayer 对 DIF 检测的具体应用。

**[AGREE] R2-M5 (Yen's Q3 未在正文定义)**: 同意。正文 Section 3.2 提到 "permutation simulation... Q3 = 4.6-34.2%" 但未解释 Q3 是什么。Appendix A.1 有详细描述，但正文首次提及时应至少加一句简要说明（如 "Yen's Q3 statistic, which measures residual correlations between item pairs after conditioning on ability"）。

---

### 综合评价

R2 的审稿整体严谨，大部分 weakness 与我的独立评估一致。最重要的共识集中在三个方面：
1. **ρ≈0.997 vs. "instability" 的 framing 张力**（R2-W1 ≈ R1-W5）
2. **因果归因空白限制 actionability**（R2-W2 ≈ R1-W3）
3. **注入模型 ecological validity 不足**（R2-W5 ≈ R1-W1）

我与 R2 的主要分歧在于方法新颖性（R2-W3）和重复呈现（R2-W6）的 severity 等级。前者不应过度惩罚严谨的跨领域应用工作，后者更多是 style issue 而非 substance issue。

R2 的 W4（\enlargethispage 格式操作）是一个我在 Round 1 中遗漏的有价值发现——这确实需要作者在 camera-ready 时修正，但不应影响学术评价。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 328 · 2026-05-22T01:51:16.826113+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 38

## Round 38

4 recorded events


### User

_source line 329 · 2026-05-22T01:51:19.613105+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心共识集中在 ρ≈0.997 vs. "instability" 的 framing 张力、因果归因空白、注入模型 ecological validity 三个方面。主要分歧在于方法新颖性（R2-W3）的 severity——我认为不应过度惩罚严谨的跨领域应用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-22T01:51:47.345518+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "以下是 Reviewer 1 对你 Round 1 审稿意见的逐条回应。请对其中的 [REBUT] 项进行再回应（同意 R1 的反驳理由，或坚持原判并补充论据）。对 [AGREE] 项无需重复，但如有补充可简要说明。\n\n---\n\n## Reviewer 1 对 Reviewer 2 的逐条回应\n\n### Strengths 回应\n\n所有 5 项 Strengths (S1-S5) 均为 **[AGREE]**，与 R1 独立评估一致。R1 补充了 Figure 1 缺少 axis labels 的 minor issue。\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1 (Practical Significance Paradox: ρ ≈ 0.997)**\nR1 基本同意但认为 [critical] 可能稍重。理由：Section 4.5 中 family-level rank shifts（Llama-3: +53, Mistral: -35）对 pairwise model selection 有实际意义。R1 认为问题在于 **framing 重心放错**（从 \"benchmark reliability threat\" 转向 \"diagnostic tool for capability dimension shifts\"），是 framing 问题而非 substance 问题。\n\n**[AGREE] R2-W2 (因果归因空白)**\n完全同意。R1 的 R1-W3 提出了同样的关切。\n\n**[REBUT] R2-W3 (方法新颖性有限)**\nR1 部分不同意，理由：\n1. ARR reviewer guidelines 明确指出不应因方法不够 complex 而贬低论文（H14 pitfall: \"simpler methods that work should not be penalized\"）\n2. 本文定位为 \"methodological and empirical, not algorithmic\"\n3. Cross-subject matching 的 ΔFPR=0.000 作为 LLM benchmark 场景的改进有独立价值\n4. C2（ground truth meta-critique）本身就是方法论层面的新颖洞察\n5. EMNLP Findings track 明确接收 \"sound and reproducible\" 实证贡献\nR1 同意更突出 C2 作为主要贡献会加强论文，但不认为 novelty 是主要 weakness。\n\n**[AGREE] R2-W4 (`\\enlargethispage{18\\baselineskip}`)**\nR1 同意这是需要关注的问题，但认为属于格式合规范畴，**不应影响学术评价**。R2-W6 指出的重复内容删减可为 Discussion 压缩腾出空间。\n\n**[AGREE] R2-W5 (注入模型过于简化)**\n同意，与 R1-W1 一致。特别赞同 R2 提出的区分——FPR 控制 vs. TPR 估计的贡献强度应明确区分。\n\n**[REBUT] R2-W6 (关键统计量重复呈现)**\nR1 部分不同意：\n- Abstract→Intro→Results→Discussion→Conclusion 的重复是学术论文正常写作惯例\n- 承认重复程度偏高（enrichment≈0.964 出现至少 5 次）\n- 但认为 [warning] 等级偏高，建议降为 Minor Issue\n\n### Questions 回应\n\n- Q1 (其他 benchmark ρ): [AGREE] 关键遗漏\n- Q2 (difficulty-direction 跨 benchmark): [AGREE] 好问题\n- Q3 (6 个月窗口 C%=34.35%): [AGREE] 有趣观察\n- Q4 (500 模型阈值): [REBUT] 论文 Section 4.1 power analysis 表明 N≥80 即可，500 足够——但同意应更明确与 power analysis 挂钩\n- Q5 (单一 domain external matching): [REBUT] 论文 Section 3.2 已定义三种 matching 策略，GSM8K 用 external matching（Appendix Table 6），但正文说明不够充分\n\n### Missing References 回应\n- Polo et al. (2024): [AGREE] 但可能已引用\n- Putnick & Bornstein (2016): [AGREE] 值得引用\n\n### Minor Issues 回应\n- M1 (Figure 2 error bands): [AGREE]\n- M2 (Table 1 \"--\"): [AGREE]\n- M3 (Figure 5 outlier): [AGREE]\n- M4 (holland1988mh 年份): **[REBUT]** — Holland & Thayer 1988 是 ETS Research Report RR-88-31，引用年份正确。R2 可能混淆了 Mantel & Haenszel (1959) 原始统计检验。\n- M5 (Yen's Q3): [AGREE]\n\n---\n\n请对上述 [REBUT] 项（R2-W3、R2-W6、R2-Q4、R2-Q5、R2-M4）进行再回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "irt_equated_bench_regen",
    "text": "以下是 Reviewer 1 对你 Round 1 审稿意见的逐条回应。请对其中的 [REBUT] 项进行再回应（同意 R1 的反驳理由，或坚持原判并补充论据）。对 [AGREE] 项无需重复，但如有补充可简要说明。\n\n---\n\n## Reviewer 1 对 Reviewer 2 的逐条回应\n\n### Strengths 回应\n\n所有 5 项 Strengths (S1-S5) 均为 **[AGREE]**，与 R1 独立评估一致。R1 补充了 Figure 1 缺少 axis labels 的 minor issue。\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1 (Practical Significance Paradox: ρ ≈ 0.997)**\nR1 基本同意但认为 [critical] 可能稍重。理由：Section 4.5 中 family-level rank shifts（Llama-3: +53, Mistral: -35）对 pairwise model selection 有实际意义。R1 认为问题在于 **framing 重心放错**（从 \"benchmark reliability threat\" 转向 \"diagnostic tool for capability dimension shifts\"），是 framing 问题而非 substance 问题。\n\n**[AGREE] R2-W2 (因果归因空白)**\n完全同意。R1 的 R1-W3 提出了同样的关切。\n\n**[REBUT] R2-W3 (方法新颖性有限)**\nR1 部分不同意，理由：\n1. ARR reviewer guidelines 明确指出不应因方法不够 complex 而贬低论文（H14 pitfall: \"simpler methods that work should not be penalized\"）\n2. 本文定位为 \"methodological and empirical, not algorithmic\"\n3. Cross-subject matching 的 ΔFPR=0.000 作为 LLM benchmark 场景的改进有独立价值\n4. C2（ground truth meta-critique）本身就是方法论层面的新颖洞察\n5. EMNLP Findings track 明确接收 \"sound and reproducible\" 实证贡献\nR1 同意更突出 C2 作为主要贡献会加强论文，但不认为 novelty 是主要 weakness。\n\n**[AGREE] R2-W4 (`\\enlargethispage{18\\baselineskip}`)**\nR1 同意这是需要关注的问题，但认为属于格式合规范畴，**不应影响学术评价**。R2-W6 指出的重复内容删减可为 Discussion 压缩腾出空间。\n\n**[AGREE] R2-W5 (注入模型过于简化)**\n同意，与 R1-W1 一致。特别赞同 R2 提出的区分——FPR 控制 vs. TPR 估计的贡献强度应明确区分。\n\n**[REBUT] R2-W6 (关键统计量重复呈现)**\nR1 部分不同意：\n- Abstract→Intro→Results→Discussion→Conclusion 的重复是学术论文正常写作惯例\n- 承认重复程度偏高（enrichment≈0.964 出现至少 5 次）\n- 但认为 [warning] 等级偏高，建议降为 Minor Issue\n\n### Questions 回应\n\n- Q1 (其他 benchmark ρ): [AGREE] 关键遗漏\n- Q2 (difficulty-direction 跨 benchmark): [AGREE] 好问题\n- Q3 (6 个月窗口 C%=34.35%): [AGREE] 有趣观察\n- Q4 (500 模型阈值): [REBUT] 论文 Section 4.1 power analysis 表明 N≥80 即可，500 足够——但同意应更明确与 power analysis 挂钩\n- Q5 (单一 domain external matching): [REBUT] 论文 Section 3.2 已定义三种 matching 策略，GSM8K 用 external matching（Appendix Table 6），但正文说明不够充分\n\n### Missing References 回应\n- Polo et al. (2024): [AGREE] 但可能已引用\n- Putnick & Bornstein (2016): [AGREE] 值得引用\n\n### Minor Issues 回应\n- M1 (Figure 2 error bands): [AGREE]\n- M2 (Table 1 \"--\"): [AGREE]\n- M3 (Figure 5 outlier): [AGREE]\n- M4 (holland1988mh 年份): **[REBUT]** — Holland & Thayer 1988 是 ETS Research Report RR-88-31，引用年份正确。R2 可能混淆了 Mantel & Haenszel (1959) 原始统计检验。\n- M5 (Yen's Q3): [AGREE]\n\n---\n\n请对上述 [REBUT] 项（R2-W3、R2-W6、R2-Q4、R2-Q5、R2-M4）进行再回应。"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-22T01:51:51.414756+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 4069
}
```

</details>

---


### Assistant

_source line 332 · 2026-05-22T01:51:55.350001+00:00_

Reviewer 1 的交叉回应已收齐。已将 R1 的回应（含 3 处 REBUT）转发给 Reviewer 2，等待 R2 的再回应以判断收敛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 39

## Round 39

22 recorded events


### User

_source line 333 · 2026-05-22T01:52:25.003524+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 1 意见

---

### 对 Strengths 的回应

**[AGREE] R1-S1**: Cross-subject matching 的 ΔFPR=0.000 确实是论文最干净的方法贡献。我在自己的 S4 中也高度肯定了这一点。补充：multi-subject injection 的优雅退化分析（k≤5 → ΔFPR<0.007, k=10 → 0.026-0.069）不仅划定了适用边界，也暗示了一个实用指标——当 benchmark 的被污染 domain 比例超过 ~9% 时应切换到 external matching。

**[AGREE] R1-S2**: 完全同意。6 种替代解释的系统排除是本文最大的实证优势。我的 S1 表达了相同观点。补充：random split（0.18%）和 ability quintile（2.9%）形成的 null baseline "bracket" 设计在方法论上很漂亮——它从上下两侧限定了真实 temporal DIF 的范围。

**[AGREE] R1-S3**: 同意。这是我认为论文中最具影响力的 contribution（我的 S2）。enrichment ≈ 0.964 本质上意味着 web-overlap labels 对 DIF 没有预测力，整个 contamination detection 社区使用这些 labels 做 validation 的实践需要 revisit。

**[AGREE] R1-S4**: 同意。六个 benchmark 复现且 knowledge/reasoning > procedural 的模式有清晰的直觉解释。

**[AGREE] R1-S5**: 同意。统计报告规范是本文的一大优点。Bootstrap CI、效应量、BH 校正等应有尽有。

**[AGREE] R1-S6**: 同意。Simpson's paradox 分析（aggregate OR=1.55 → controlled OR=0.73, Section 4.2）是论文中最精巧的统计分析之一，它直接证明了 DIF 是 item-level 现象而非 domain-level 副产物。

---

### 对 Weaknesses 的回应

**[AGREE] R1-W1**: 同意半合成注入的 ecological validity 不足，这与我的 W5 一致。Binary flipping 是 upper bound，不是 realistic scenario。R1 建议的 "按 difficulty 分层的非均匀 flipping" 是一个合理的改进方向。补充一个 nuance：正如我在 W5 中指出的，这一局限主要影响 ΔTPR 的参考价值（检测力估计），而不影响 ΔFPR=0.000 的结论（FPR 控制是匹配策略的属性，不依赖注入模型的现实性）。论文应在正文中更清晰地区分这两方面。

**[AGREE] R1-W2**: 这是我未充分关注的有效观点。LLM 共享 base model、训练数据、架构，违反 MH χ² 的独立性假设。论文 Section 3.2 的 LLM-specific challenges 段落提到了 permutation simulation 显示 LD-attributable FPR inflation < 0.001 pp，以及 graduated de-duplication 显示 family structure 不膨胀 C%——但这些都是经验处理，缺乏理论层面的讨论。French & Finch (2010) 关于 clustered data 中 DIF 检测的文献确实是一个重要的遗漏引用，可以为论文提供理论框架来讨论 non-independence 的影响。不过，我认为这是 warning 级别而非 critical——经验证据（permutation + de-duplication）在实践中已经 adequate 地回应了这一顾虑。

**[AGREE] R1-W3**: 强烈同意，这与我的 W2（critical）完全一致。因果归因空白与 "retire flagged items" 建议之间的张力是本文最大的逻辑缺陷。R1 提出的 "measurement instability（问题）vs expected sensitivity（特征）" 的区分框架非常到位——这正是论文缺少的概念辨析。DIF-flagged items 集中了 discriminative signal（z = -8σ to -49σ, Section 4.6），retire 它们等于移除 benchmark 中最有信息量的部分。论文需要回答：如果 DIF 可能反映 genuine capability evolution，那么 monitoring 的目标应该是什么？

**[REBUT] R1-W4**: 部分不同意。200 次 permutation 确实在 p=0.005 处达到分辨率极限（1/200）。但论文同时报告了 complementary per-subject permutation（1,000 permutations × 8 subjects, Section 4.2），其结果（mean null C% = 0.09%, p₉₅ = 0.62%）与 200 次 permutation 完全一致。两个独立的 permutation 分析相互验证，且核心结论（temporal DIF 远超 null baseline）在两种分析中都极为显著。增加到 1,000 次会提高 p-value 精度，但不会改变任何结论。这是 info 级别的建议而非 warning。

**[AGREE] R1-W5**: 完全同意，这是我的 W1（critical 级别）的核心论点。ρ ≈ 0.997 的高相关性确实大部分归因于 MMLU 12,508 items 的巨大冗余度。R1 建议的 "pairwise model comparison 翻转率" 是一个出色的补充指标——它比 Spearman ρ 对局部排名变化更敏感。我在 Q1 中也要求了其他 benchmark（尤其是 TruthfulQA, 817 items）的 ρ 值。如果小 benchmark 上 ρ 显著低于 0.997，论文的 practical significance 论证将大大加强。

**[REBUT] R1-W6**: 部分不同意 R1 对机制的描述，但同意建议的分析。R1 说 "小 subject 排除后 matching variable 受影响小，可能仍包含被测 items 信号"——但这与 cross-subject matching 的逻辑方向相反。Cross-subject matching 从 matching variable 中排除被测 subject 的所有 items（Section 3.2），因此被测 items 的信号 by construction 不在 matching variable 中，无论 subject 大小。真正的 concern 应该是：当一个很小的 subject（如 <50 items）被单独测试时，MH test 的 statistical power 会降低。然而，R1 建议的 "subject-level C% 与 subject size 的相关性" 分析确实有价值——如果小 subject 的 C% 系统性偏高或偏低，这可能暗示 power 或 FPR 问题。

---

### 对 Questions 的回应

**[AGREE] R1-Q1**: 有效问题。论文 Section 4.2 报告 "1:1 nearest-neighbor matching (d ≈ -0.010, N = 638 per group, 5 seeds)"，但未明确说明是用 total score 还是 IRT θ 做 matching。从 (1080, 807) 降到 (638, 638) 意味着 807-638=169 focal models（21%）和 1080-638=442 reference models（41%）被丢弃。selection bias 的风险存在，但 matched C% = 28.9% 与其他 robustness checks（θ-conditioning: 31.2%, within-subject: 38.1%）的收敛性（均 ≥28%）缓解了这一顾虑。建议论文报告 dropped models 的特征分布。

**[AGREE] R1-Q2**: 有效关切。如果 2PL 拟合差（Appendix A.2），基于 2PL 参数的 Monte Carlo power analysis（Section 4.1）的参数精确性存疑。但 power analysis 的结论（N≥80 per cohort 即可达到合理 power）与半合成注入的 empirical power 估计（ΔTPR = +0.508 at p=0.5, Section 4.5）相互佐证。parametric 和 non-parametric 两条证据线的收敛增强了 power 足够的结论。论文应明确指出这种 triangulation。

**[AGREE] R1-Q3**: 这是一个我也未追问的好问题。Within-subject C% = 38.1% > Temporal 31.3% 的原因未被充分解释。可能的解释：(a) within-subject 分析使用 within-subject total score 作 matching variable，items 更少导致 matching 精度下降；(b) within-subject 分析在单个 subject 内做，sample size 不变但 item pool 缩小，MH test 行为可能不同；(c) 38.1% 是 5 个 subject 的 average，variance 可能很大。论文应报告 within-subject C% 的分布（而非仅 mean）并讨论可能的 type-I error inflation。

**[AGREE] R1-Q4**: 完全同意。GSM1K 的 r = -0.478（N=33）在 Abstract 中作为支撑证据（"show that web-overlap contamination labels..."附近）过于 prominent。N=33 的相关分析应明确标注为 exploratory（我的 M3 也指出了这一点）。Abstract 中不应引用 exploratory finding 作为核心结论的支撑。

**[AGREE] R1-Q5**: IRT θ vs total scores r=0.9986 确实使 IRT framing 的附加分析价值存疑。我的解读是 IRT framing 主要服务于两个目的：(a) 将论文定位在 psychometric 文献传统中，增强 legitimacy；(b) 为 power analysis 提供参数化模型（Section 4.1 使用 2PL 参数）。实际的 DIF 分析完全基于 total score stratification（CTT 而非 IRT），论文应更明确地指出这一点，避免给读者留下 "这是一个 IRT 方法论论文" 的印象——它本质上是一个 CTT-based DIF 应用论文。

---

### 对 Missing References 的回应

**[AGREE] French & Finch (2010)**: 同意。这是 R1-W2 的核心引用需求，对 clustered data 中 MH-DIF 的理论讨论至关重要。论文当前对 LLM non-independence 的处理完全是经验性的（permutation + de-duplication），缺乏理论框架。

**[AGREE] Magis & De Boeck (2012)**: 同意。作为 type-I error 控制的替代方法文献，与论文的 BH FDR correction 讨论相关。

**[AGREE] Kolen & Brennan (2014)**: 同意。经典 equating 文献与 Growing Pains (Habba et al., 2026) 的 FPC 方法有直接联系。论文 Related Work ¶2 讨论了与 Growing Pains 的互补关系，但缺少 equating 方法论的基础文献支撑。

---

### 对 Minor Issues 的回应

**[AGREE] Abstract 密度过高**: 同意。我在 W6 中指出了信息密度问题。Abstract 中挤入了过多具体统计量（ΔFPR, ΔTPR, enrichment, Jaccard, C%, z-scores, ρ），读者难以在第一次阅读时抓住核心信息。

**[REBUT] ETS Category B 定义缺失**: 部分不同意。R1 说 "缺少 |Δ_MH|<1.0 且有显著性的情况"。但根据 ETS 标准分类规则，|Δ_MH| < 1.0 的 items 无论显著性如何都归入 Category A（negligible DIF）。论文 Section 3.2 的定义——"Category A (negligible) requires |Δ_MH| < 1.0"——是正确的。ETS 的分类逻辑是：先看 effect size，effect size 小则直接归 A，不考虑 significance。B 是 "所有其余 items"，即 1.0 ≤ |Δ_MH| < 1.5（无论 significance），或 |Δ_MH| ≥ 1.5 但不显著。这与论文的描述一致。

**[AGREE] Figure 1 缺 axis labels**: 需重新确认。从 PDF 渲染结果来看，Figure 1 的 ICC 曲线图（page 2）应标注 x-axis = Ability (θ), y-axis = P(correct)。如果确实缺失，这是一个容易修复的视觉问题。

**[AGREE] Section 4.5 z 值不直观**: 同意。z = -8σ to -49σ 的含义（DIF-based removal vs random removal 对排名变化的 z-statistics）对非心理计量学读者不够自明。建议添加一句解释。

**[REBUT] 正文约 8 页，格式合规**: R1 判定格式合规，但我在自己的 W4 中指出 `\enlargethispage{18\baselineskip}`（discussion.tex line 3）是非常激进的页面扩展操作（≈18 行额外空间）。这使得 page 8 的文本区域显著超出正常 margin。虽然 ACL 模板没有明确禁止此命令，但如果去除该命令，Discussion + Conclusion 很可能溢出到第 9 页。建议将此标记为 borderline formatting concern 而非 unconditional pass。

---

### 总体评估

R1 和 R2 在以下关键点上高度一致：
1. **Ground truth meta-critique 是最强 contribution**（R1-S3, R2-S2）
2. **半合成注入的 ecological validity 不足**（R1-W1, R2-W5）
3. **因果归因空白与 "retire items" 建议的矛盾**（R1-W3, R2-W2）
4. **ρ ≈ 0.997 需要更 nuanced 的解读**（R1-W5, R2-W1）

主要分歧：
- **严重程度**: 我将 ρ ≈ 0.997 paradox 和因果归因空白列为 **critical**（影响接收决定），R1 仅列为 **warning**。我认为这两个问题更严重，因为它们直接动摇了论文的核心叙事（"LLM benchmarks need psychometric monitoring"）和核心建议（audit protocol）的根基。
- **格式合规**: R1 判定合规，我认为 `\enlargethispage{18\baselineskip}` 值得标记。
- **R1-W6 subject 粒度**: 我认为 R1 对机制的描述有误（cross-subject matching by construction 排除了被测 items），但同意建议的分析（subject-level C% vs subject size）有价值。

**维持我的评分**: Overall 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-22T01:53:17.260874+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-22T01:53:17.311581+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-22T01:42:14.372492+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_25ed8e3ecef6fc922cb497fae9f34627\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-22T01:53:17.312030+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-22T01:53:17.414085+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T01:42:13.185310+00:00\", \"completed_at\": \"2026-05-22T01:44:48.694945+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，Figure 1 出现在 page 2 顶部（在前 3 页内），作为视觉锚点位置可接受。Title/Author/Abstract 排版整洁专业。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续 4 页近乎纯文本（仅 page 4 有一个 equation），Related Work → Method → Experiments 开头形成视觉沙漠。建议在 Method 或 Experiments 早期增加一个流程图、示意图或方法概览表，打破文字墙。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"视觉密度过度集中——Table 1 + Figure 2 + Table 2 三个 display items 挤在同一页。与前 4 页的纯文本形成极端的 feast-or-famine 节奏。建议将 Table 2 或 Figure 2 前移至 page 5-6 附近（如在 Method 中插入 matching 策略比较表或 injection framework 示意图）。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主文 display items 共 5 个（2 figures + 3 tables），8 页正文密度约 0.63/页。对于 psychometric 方法论论文偏低但可接受；若能在 method 段增加一个概念图或流程图则更佳。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（ICC curves）作为首个 display item，有效传达 global vs. differential contamination 的核心区别。Caption 自包含，可独立理解。但子图内文字（axis labels, legend）偏小，建议适当放大。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（dose-response curve）清晰可读，caption 描述充分。颜色区分度良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，无竖线，排版规范。数字精度统一。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 排版整洁，booktabs 风格。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 排版规范，bold 标注了关键 C% 数值，列间对齐良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Discussion section (5.1-5.3) 和 Conclusion (Section 6) 在 page 8 内完成，主文严格控制在 8 页。页面利用率高（~95%）。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 短小精炼（覆盖 scope/boundary/generalizability 三点），符合 EMNLP 规范。References 紧随其后，排版正常。\"}, 
…[truncated 1069 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-22T01:53:23.593938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-22T01:53:23.694961+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage{18\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF analysis decomposes benchmark score differences into three layers. \emph{Layer~1} (impact): overall ability differences between cohorts, removed by matching (Cohen's $d = -0.17$; matched C\% $= 28.9\%$, reducing unmatched 31.3\% by $\sim$2.4~pp). \emph{Layer~2} (DIF): item-level differences persisting after ability control---the 28--29\% floor across multiple matching methods, of which 92.4\% is item-specific (pseudo $R^2 = 0.0007$). \emph{Layer~3} (attribution): whether DIF reflects contamination, capability evolution, or training methodology shifts---beyond observational DIF analysis without training data access. The practical import is identical regardless of attribution: temporal DIF means the same benchmark score carries different meaning across model generations. The Simpson's paradox (\Cref{sec:temporal}) confirms DIF is associated with item properties rather than accuracy gains. Aggregate ranking is preserved ($\rho \approx 0.997$), but family-level profiles reveal systematic shifts (Llama-3: ${+}53$ median rank; Mistral: $-35$) that matter for pairwise model selection. Domain directionality (STEM favoring 2024 at 55.4\%, Humanities favoring 2023 at 64.4\%) describes where measurement properties shift without implying a specific cause.
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	\looseness=-1
15	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) reflects that the two methods measure different constructs---global exposure versus differential functioning---making web-overlap labels an inappropriate ground truth for a differential method. The semi-synthetic dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) confirms that MH-DIF det
…[truncated 1104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-22T01:53:24.098124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-22T01:53:24.600675+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$, $\phi = 0.012$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, each 45--174$\times$ above random baselines, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten ranking validity ($\rho \approx 0.997$) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-22T01:53:24.601234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-22T01:53:25.003419+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Matching boundary and sample size.}
7	Cross-subject matching assumes contamination affects a minority of domains; when contamination spans ${>}10$ subjects (${>}18\%$ of MMLU), $\Delta\mathrm{FPR}$ rises to 0.026--0.069. Model-level bootstrap may underestimate CI width due to within-family correlation; cluster bootstrap at the model-family level is a natural extension (the $K{=}20$ de-duplication analysis at C\% $= 29.1\%$ provides a conservative robustness check). The GSM1K correlation analysis ($N = 33$) has limited statistical power and is exploratory.
8	
9	\paragraph{Generalizability.}
10	All six benchmarks use multiple-choice or binary scoring; generalizability to open-ended generation (e.g., AlpacaEval), coding (e.g., HumanEval), or partial-credit benchmarks is untested and would require polytomous DIF methods. Temporal cohorts are defined by
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-22T01:53:25.003888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-22T01:53:25.054352+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1
5	A semi-synthetic framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$) resolves a validation gap: web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$). Across six benchmarks, 17.9--31.3\% of items exhibit temporal instability associated with item properties; LLM benchmarks need psychometric monitoring alongside score reporting.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-22T01:54:15.381928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-22T01:54:15.382421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 348 · 2026-05-22T01:54:15.433183+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples; rightward asymmetry reflects heavy-tailed C\% from subjects exceeding 40\%). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold already provides implicit multiple-testing protection.
17	
18	\looseness=-1
19	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C ite
…[truncated 10517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-22T01:54:15.433928+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees 
…[truncated 8118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-22T01:57:02.683190+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 9 (Fresh review, 2026-05-22)\n# R1: 3.5, R2: 3.5 → Consensus 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"因果可解释性不足——DIF 无法区分 contamination、capability evolution、training methodology shifts\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 两位 Reviewer 独立提出同一核心问题。问题范围扩大：不仅是 causal language，更根本的是 31% DIF 可能主要反映 genuine capability change。pseudo R²=0.0007 仅排除 domain-level gains，不排除 item-level capability changes。需要操作化的 benign/problematic DIF 区分方法。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"再次独立提出（R1-W3, R2-W2 均标 critical/warning）。三层框架（impact/DIF/attribution）已加入 Discussion §5.1，但 Layer 3 仍完全悬空。核心矛盾加剧：§5.3 建议 'rotate or retire flagged items'，但 §4.6 显示 DIF items 集中 discriminative signal（z=-8σ to -49σ）。两位 Reviewer 共识：retire = 移除最有信息量的 items，可能比不审计更有害。\"\n  action_items:\n    - round: 8\n      action: \"P29: Discussion 新增 DIF Interpretation 段落，用三层框架替代 benign/problematic 二分法\"\n      assigned_to: paper_agent\n      status: resolved\n    - round: 9\n      action: \"§5.3 将 'Act: rotate or retire flagged items' 改为 'investigate and report alongside stable-item rankings'，与 'diagnostic, not destructive' 定位一致。明确 DIF audit 价值在于 flag for investigation 而非自动化 retire。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox——'instability' 叙事被排名保持所削弱\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"需更强调 family-level 和 pairwise 层面影响。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 标 critical，R1 标 warning（认为是 framing 问题非 substance 问题）。共识：(1) family-level rank shifts（Llama-3 +53, Mistral -35）应从附录提升到正文；(2) 需报告 TruthfulQA (817 items) 等小 benchmark 的 stable-item ρ 值；(3) 应讨论 ρ≈0.997 部分归因于 MMLU 12,508 items 冗余度。(4) R1 建议补充 pairwise model comparison 翻转率。\"\n  action_items:\n    - round: 8\n      action: \"P29: §4.6/§5 强化 family-level evidence\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 9\n      action: \"(1) 报告 Table 3 中所有 6 个 benchmark 的 stable-item ρ 值；(2) 将 family-level rank profile 从附录提升到正文 §4.6；(3) 补充 pairwise comparison flip rate；(4) 讨论 item 冗余度对 ρ 的影响。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic binary flipping 的 ecological validity——uniform rate p 不反映真实 contamination patterns\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"共识 strong Should-Fix。需明确 ΔTPR 为 upper-bound。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"再次独立提出（R1-W1, R2-W5）。共识：(a) 论文已在 Limitations 和 §3.4 标注 ΔTPR 为 upper-bound estimate——改善明显；(b) 但正文 §3.4 和 §4.1 未充分区分框架对 FPR 控制（不依赖注入现实性）vs TPR 估计（受限于注入模型）的贡献强度；(c) R1 建议按 difficulty 分层的非均匀 flipping 作为 robustness check，但两位 Reviewer 均认为非 must-fix。\"\n  action_items:\n    - round: 8\n      action: \"§3.4 和 §4.5 标注 ΔTPR 为 upper-bound estimate\"\n      assigned_to: paper_agent\n      status: resolved\n    - round: 9\n      action: \"在正文 §3.4 或 §4.1 更明确区分：ΔFPR=0.000 是 matching strategy 性质（不依赖注入模型），ΔTPR 是 upper-bound estimate（受注入模型限制）。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W1\"\n  summary: \"LLM examinees 非独立性对 MH χ² 的理论影响未讨论——经验处理充分但缺乏理论框架\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 首提（W2），R2 交叉回应 AGREE 但降为 warning（经验证据 adequate）。LLM 共享 base model/训练数据/架构，违反 MH χ² 独立性假设。§3.2 列举 4 个 LLM-specific challenges 并提供经验处理（permutation LD inflation <0.001pp, de-duplication），但缺乏理论层面讨论 non-independence 对 type-I error 的影响。\"\n  action_items:\n    - round: 9\n      action: \"§3.2 增加一段讨论 MH test 在 clustered/non-independent examinees 下的 size 表现，引用 French & Finch (2010)。或在 Limitations 补充。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限——MH-DIF 是 1988 年标准方法的直接应用\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 首提（W3），R1 REBUT：ARR H14 不应因方法不 complex 而贬低；论文定位 methodological+empirical 合理；C2 和 cross-subject matching 有独立方法论价值。R2 未在再回应中让步但未升级。两位 Reviewer 均同意：更突出 C2（ground truth meta-critique）作为主要贡献可加强论文。DISPUTED：严重程度有分歧。\"\n  action_items:\n    - round: 9\n      action: \"重新排列 contributions 权重：C2（ground truth meta-critique）提升为首要贡献，C1（大规模实证发现）次之，C3（semi-synthetic framework）第三。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"\\\\enlargethispage{18\\\\baselineskip} 格式操作过于激进——可能被 PC 视为规避页数限制\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 发现（W4），R1 AGREE 但认为不影响学术评价。discussion.tex line 3 使用 \\\\enlargethispage{18\\\\baselineskip}（≈18 行/8.3cm 额外空间）。去除后 Discussion+Conclusion 很可能溢出到第 9 页。需压缩 Discussion（删减重复内容）使内容自然 fit 在 8 页内。\"\n  action_items:\n    - round: 9\n      action: \"移除 \\\\enlargethispage{18\\\\baselineskip}，通过压缩 Discussion 重复内容和精简统计量重述使正文自然 fit 在 8 页内。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MF3\"\n  summary: \"Within-subject C%=38.1% 高于主分析 31.3%，且 ~28-29% convergence 未被充分探讨\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Per-subject 分析理应更 clean 但反而更高。三个独立分析收敛于 ~28-29%。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-Q3 再次追问原因：matching variable items 更少导致精度下降？MH test 行为在小 item pool 下不同？需报告 within-subject C% 分布而非仅 mean。\"\n  action_items:\n    - round: 8\n      action: \"§4.4 新增 convergence 讨论段落\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 9\n      action: \"报告 within-subject C% 的分布（5 个 subject 各自的 C%），讨论可能的 type-I error inflation。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K N=33 统计效力不足——exploratory finding 不应在 Abstract 中作为核心支撑\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"移至 Appendix 并标注 preliminary\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-Q4 + R2-M3 再次提出。论文已标注 exploratory 并移至 §4.7 末尾 + Appendix。但 Abstract 仍隐含使用此结果支撑 'DIF captures capability change distinct from memorization'。需 leave-one-out 或 robust correlation 分析。\"\n  action_items:\n    - round: 9\n      action: \"Abstract 中不应引用 GSM1K exploratory finding 作为核心结论支撑。确保 Abstract 措辞不暗示 GSM1K 结果为 confirmed finding。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF10\"\n  summary: \"置换检验仅 200 次洗牌，分辨率有限\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"200 次最小 p=0.005 恰是报告值\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W4 再次提出。R2 交叉回应 REBUT：per-subject 1000 perm 与 200 perm 结果一致，增加迭代不改变结论。两位共识降为 info 级别。论文已标注 'resolution limit'。\"\n  action_items:\n    - round: 9\n      action: \"建议增至 1,000 次以提高 p-value 精度（非 must-fix，info 级别）。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-MISS-REF\"\n  summary: \"缺少引用：French & Finch (2010), Kolen & Brennan (2014), Putnick & Bornstein (2016), Magis & De Boeck (2012)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1: French & Finch (2010, clustered DIF), Magis & De Boeck (2012, type-I error), Kolen & Brennan (2014, equating). R2: Putnick & Bornstein (2016, measurement invariance). 两位均标为 nice-to-have 而非 critical。\"\n  action_items:\n    - round: 9\n      action: \"补充 French & Finch (2010) 到 §3.2 LLM-specific challenges 段落。其余 3 篇视页数空间选择性补充。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED ISSUES (carried from previous rounds)\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null——headline 31.3% 缺乏正确 baseline comparator\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2（200 shuffles, null C%=0.10%±0.12%, p=0.005）+ per-subject 1000 perm\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑——两个时间点不能建立趋势\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 已改为 'Temporal Measurement Instability'，全文 'drift' → 'instability'/'temporal DIF'。Round 9 fresh review 未再提出 drift framing 问题。\"\n  resolution_round: 9\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化——cross-subject matching 定义的直接推论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"已降格为 Remark（§3.4），Round 9 fresh review 未再提出。\"\n  resolution_round: 9\n\n- id: \"R8-SF4\"\n  summary: \"Table 2 列名 'Temp. FPR' 误导——应改为 'Temp. C%'\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Table 2 列名已改为 'Temp. C%'。Round 9 fresh review 未再提出。\"\n  resolution_round: 9\n\n- id: \"R6-W1\"\n  summary: \"IRT model fit statistics 未报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix A.2 reports poor fit to unidimensional 2PL + method.tex notes MH-DIF is non-parametric\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"Multi-subject injection 结果展示过于压缩\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 added to Appendix C with full k-sweep data\"\n  resolution_round: 8\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing——DIF and contamination measure different constructs\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Section 5.2 adequately frames the construct distinction\"\n  resolution_round: 8\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n\n- id: \"R2-N2-resolved\"\n  summary: \"Novelty 论证不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  resolution: \"LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。\"\n  resolution_round: 6\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (LD×DIF)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50). MH non-parametric.\"\n  resolution_round: 4\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]. Structural guarantee.\"\n  resolution_round: 4\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n\n- id: \"MISSING-REF-1\"\n  summary: \"引用问题（Round 1-7）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 7\n  resolution: \"Verified: all 51 bib entries properly cited. Zero orphans.\"\n  resolution_round: 7\n\n# ============================================================\n# POSSIBLY RESOLVED (Round 8 issues not raised in Round 9 fresh review)\n# ============================================================\n\n- id: \"R8-SF7\"\n  summary: \"Logistic regression model specification 未完整报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Simpson's paradox regression + non-uniform DIF 未报告完整 spec\"\n    - round: 9\n      reviewers: []\n      note: \"Round 9 fresh review 未提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 8\n      action: \"Appendix 新增 logistic regression specification paragraph\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF8\"\n  summary: \"Power analysis 使用平均 2PL 参数，未展示参数分布 sensitivity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"ā=1.2, b̄=-0.84 掩盖 item 参数 heterogeneity\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-Q2 追问 2PL 拟合差时 power analysis 可靠性。但论文已在 §4.1 报告 TPR 随 a 从 0.40(a=0.5) 到 0.95(a=2.0) 的变化 + Jensen's inequality。R2 确认 parametric 和 non-parametric 两条证据线收敛。改善明显。\"\n  action_items:\n    - round: 8\n      action: \"报告 2PL 参数分布描述统计 + power sensitivity\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 缺乏深入概念对比\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"需更深入的概念对比\"\n    - round: 9\n      reviewers: []\n      note: \"Round 9 fresh review 未提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 8\n      action: \"Related Work 扩展 Growing Pains 概念对比\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI 忽略家族内相关性（cluster bootstrap）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"理论上存在但不影响 directional conclusion\"\n    - round: 9\n      reviewers: []\n      note: \"Round 9 fresh review 未提及，可能已修复或被 graduated de-duplication (K=20, C%=29.1%) 充分缓解，待 Research Director 确认\"\n  action_items:\n    - round: 8\n      action: \"Limitations 补充 acknowledging family correlation + K=20 dedup robustness check\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MISS-REF\"\n  summary: \"缺少引用：Oren 2024, Deng 2024, MMLU-Pro, MMLU-Redux\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"3 必要 + 1 建议\"\n    - round: 9\n      reviewers: []\n      note: \"Round 9 fresh review 未提及这些具体引用，但提出了新的 missing refs。可能已补充，待确认。\"\n  action_items:\n    - round: 8\n      action: \"补充 Oren et al. (ICML 2024), Deng et al. (2024), MMLU-Pro, MMLU-Redux\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 9 (Fresh review, 2026-05-22)\n# R1: 3.5, R2: 3.5 → Consensus 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"因果可解释性不足——DIF 无法区分 contamination、capability evolution、training methodology shifts\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 9\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 两位 Reviewer 独立提出同一核心问题。问题范围扩大：不仅是 causal language，更根本的是 31% DIF 可能主要反映 genuine capability change。pseudo R²=0.0007 仅排除 domain-level gains，不排除 item-level capability changes。需要操作化的 benign/problematic DIF 区分方法。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"再次独立提出（R1-W3, R2-W2 均标 critical/warning）。三层框架（impact/DIF/attribution）已加入 Discussion §5.1，但 Layer 3 仍完全悬空。核心矛盾加剧：§5.3 建议 'rotate or retire flagged items'，但 §4.6 显示 DIF items 集中 discriminative signal（z=-8σ to -49σ）。两位 Reviewer 共识：retire = 移除最有信息量的 items，可能比不审计更有害。\"\n  action_items:\n    - round: 8\n      action: \"P29: Discussion 新增 DIF Interpretation 段落，用三层框架替代 benign/problematic 二分法\"\n      assigned_to: paper_agent\n      status: resolved\n    - round: 9\n      action: \"§5.3 将 'Act: rotate or retire flagged items' 改为 'investigate and report alongside stable-item rankings'，与 'diagnostic, not destructive' 定位一致。明确 DIF audit 价值在于 flag for investigation 而非自动化 retire。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox——'instability' 叙事被排名保持所削弱\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"需更强调 family-level 和 pairwise 层面影响。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 标 critical，R1 标 warning（认为是 framing 问题非 substance 问题）。共识：(1) family-level rank shifts（Llama-3 +53, Mistral -35）应从附录提升到正文；(2) 需报告 TruthfulQA (817 items) 等小 benchmark 的 stable-item ρ 值；(3) 应讨论 ρ≈0.997 部分归因于 MMLU 12,508 items 冗余度。(4) R1 建议补充 pairwise model comparison 翻转率。\"\n  action_items:\n    - round: 8\n      action: \"P29: §4.6/§5 强化 family-level evidence\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 9\n      action: \"(1) 报告 Table 3 中所有 6 个 benchmark 的 stable-item ρ 值；(2) 将 family-level rank profile 从附录提升到正文 §4.6；(3) 补充 pairwise comparison flip rate；(4) 讨论 item 冗余度对 ρ 的影响。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic binary flipping 的 ecological validity——uniform rate p 不反映真实 contamination patterns\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"共识 strong Should-Fix。需明确 ΔTPR 为 upper-bound。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"再次独立提出（R1-W1, R2-W5）。共识：(a) 论文已在 Limitations 和 §3.4 标注 ΔTPR 为 upper-bound estimate——改善明显；(b) 但正文 §3.4 和 §4.1 未充分区分框架对 FPR 控制（不依赖注入现实性）vs TPR 估计（受限于注入模型）的贡献强度；(c) R1 建议按 difficulty 分层的非均匀 flipping 作为 robustness check，但两位 Reviewer 均认为非 must-fix。\"\n  action_items:\n    - round: 8\n      action: \"§3.4 和 §4.5 标注 ΔTPR 为 upper-bound estimate\"\n      assigned_to: paper_agent\n      status: resolved\n    - round: 9\n      action: \"在正文 §3.4 或 §4.1 更明确区分：ΔFPR=0.000 是 matching strategy 性质（不依赖注入模型），ΔTPR 是 upper-bound estimate（受注入模型限制）。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W1\"\n  summary: \"LLM examinees 非独立性对 MH χ² 的理论影响未讨论——经验处理充分但缺乏理论框架\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 首提（W2），R2 交叉回应 AGREE 但降为 warning（经验证据 adequate）。LLM 共享 base model/训练数据/架构，违反 MH χ² 独立性假设。§3.2 列举 4 个 LLM-specific challenges 并提供经验处理（permutation LD inflation <0.001pp, de-duplication），但缺乏理论层面讨论 non-independence 对 type-I error 的影响。\"\n  action_items:\n    - round: 9\n      action: \"§3.2 增加一段讨论 MH test 在 clustered/non-independent examinees 下的 size 表现，引用 French & Finch (2010)。或在 Limitations 补充。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限——MH-DIF 是 1988 年标准方法的直接应用\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 首提（W3），R1 REBUT：ARR H14 不应因方法不 complex 而贬低；论文定位 methodological+empirical 合理；C2 和 cross-subject matching 有独立方法论价值。R2 未在再回应中让步但未升级。两位 Reviewer 均同意：更突出 C2（ground truth meta-critique）作为主要贡献可加强论文。DISPUTED：严重程度有分歧。\"\n  action_items:\n    - round: 9\n      action: \"重新排列 contributions 权重：C2（ground truth meta-critique）提升为首要贡献，C1（大规模实证发现）次之，C3（semi-synthetic framework）第三。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"\\\\enlargethispage{18\\\\baselineskip} 格式操作过于激进——可能被 PC 视为规避页数限制\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 发现（W4），R1 AGREE 但认为不影响学术评价。discussion.tex line 3 使用 \\\\enlargethispage{18\\\\baselineskip}（≈18 行/8.3cm 额外空间）。去除后 Discussion+Conclusion 很可能溢出到第 9 页。需压缩 Discussion（删减重复内容）使内容自然 fit 在 8 页内。\"\n  action_items:\n    - round: 9\n      action: \"移除 \\\\enlargethispage{18\\\\baselineskip}，通过压缩 Discussion 重复内容和精简统计量重述使正文自然 fit 在 8 页内。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MF3\"\n  summary: \"Within-subject C%=38.1% 高于主分析 31.3%，且 ~28-29% convergence 未被充分探讨\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Per-subject 分析理应更 clean 但反而更高。三个独立分析收敛于 ~28-29%。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-Q3 再次追问原因：matching variable items 更少导致精度下降？MH test 行为在小 item pool 下不同？需报告 within-subject C% 分布而非仅 mean。\"\n  action_items:\n    - round: 8\n      action: \"§4.4 新增 convergence 讨论段落\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 9\n      action: \"报告 within-subject C% 的分布（5 个 subject 各自的 C%），讨论可能的 type-I error inflation。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K N=33 统计效力不足——exploratory finding 不应在 Abstract 中作为核心支撑\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"移至 Appendix 并标注 preliminary\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-Q4 + R2-M3 再次提出。论文已标注 exploratory 并移至 §4.7 末尾 + Appendix。但 Abstract 仍隐含使用此结果支撑 'DIF captures capability change distinct from memorization'。需 leave-one-out 或 robust correlation 分析。\"\n  action_items:\n    - round: 9\n      action: \"Abstract 中不应引用 GSM1K exploratory finding 作为核心结论支撑。确保 Abstract 措辞不暗示 GSM1K 结果为 confirmed finding。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF10\"\n  summary: \"置换检验仅 200 次洗牌，分辨率有限\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"200 次最小 p=0.005 恰是报告值\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W4 再次提出。R2 交叉回应 REBUT：per-subject 1000 perm 与 200 perm 结果一致，增加迭代不改变结论。两位共识降为 info 级别。论文已标注 'resolution limit'。\"\n  action_items:\n    - round: 9\n      action: \"建议增至 1,000 次以提高 p-value 精度（非 must-fix，info 级别）。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-MISS-REF\"\n  summary: \"缺少引用：French & Finch (2010), Kolen & Brennan (2014), Putnick & Bornstein (2016), Magis & De Boeck (2012)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1: French & Finch (2010, clustered DIF), Magis & De Boeck (2012, type-I error), Kolen & Brennan (2014, equating). R2: Putnick & Bornstein (2016, measurement invariance). 两位均标为 nice-to-have 而非 critical。\"\n  action_items:\n    - round: 9\n      action: \"补充 French & Finch (2010) 到 §3.2 LLM-specific challenges 段落。其余 3 篇视页数空间选择性补充。\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED ISSUES (carried from previous rounds)\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null——headline 31.3% 缺乏正确 baseline comparator\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2（200 shuffles, null C%=0.10%±0.12%, p=0.005）+ per-subject 1000 perm\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑——两个时间点不能建立趋势\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 已改为 'Temporal Measurement Instability'，全文 'drift' → 'instability'/'temporal DIF'。Round 9 fresh review 未再提出 drift framing 问题。\"\n  resolution_round: 9\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化——cross-subject matching 定义的直接推论\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"已降格为 Remark（§3.4），Round 9 fresh review 未再提出。\"\n  resolution_round: 9\n\n- id: \"R8-SF4\"\n  summary: \"Table 2 列名 'Temp. FPR' 误导——应改为 'Temp. C%'\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Table 2 列名已改为 'Temp. C%'。Round 9 fresh review 未再提出。\"\n  resolution_round: 9\n\n- id: \"R6-W1\"\n  summary: \"IRT model fit statistics 未报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix A.2 reports poor fit to unidimensional 2PL + method.tex notes MH-DIF is non-parametric\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"Multi-subject injection 结果展示过于压缩\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 added to Appendix C with full k-sweep data\"\n  resolution_round: 8\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing——DIF and contamination measure different constructs\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Section 5.2 adequately frames the construct distinction\"\n  resolution_round: 8\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n\n- id: \"R2-N2-resolved\"\n  summary: \"Novelty 论证不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  resolution: \"LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。\"\n  resolution_round: 6\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (LD×DIF)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50). MH non-parametric.\"\n  resolution_round: 4\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]. Structural guarantee.\"\n  resolution_round: 4\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n\n- id: \"MISSING-REF-1\"\n  summary: \"引用问题（Round 1-7）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 7\n  resolution: \"Verified: all 51 bib entries properly cited. Zero orphans.\"\n  resolution_round: 7\n\n# ============================================================\n# POSSIBLY RESOLVED (Round 8 issues not raised in Round 9 fresh review)\n# ============================================================\n\n- id: \"R8-SF7\"\n  summary: \"Logistic regression model specification 未完整报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Simpson's paradox regression + non-uniform DIF 未报告完整 spec\"\n    - round: 9\n      reviewers: []\n      note: \"Round 9 fresh review 未提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 8\n      action: \"Appendix 新增 logistic regression specification paragraph\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-SF8\"\n  summary: \"Power analysis 使用平均 2PL 参数，未展示参数分布 sensitivity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"ā=1.2, b̄=-0.84 掩盖 item 参数 heterogeneity\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-Q2 追问 2PL 拟合差时 power analysis 可靠性。但论文已在 §4.1 报告 TPR 随 a 从 0.40(a=0.5) 到 0.95(a=2.0) 的变化 + Jensen's inequality。R2 确认 parametric 和 non-parametric 两条证据线收敛。改善明显。\"\n  action_items:\n    - round: 8\n      action: \"报告 2PL 参数分布描述统计 + power sensitivity\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 缺乏深入概念对比\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"需更深入的概念对比\"\n    - round: 9\n      reviewers: []\n      note: \"Round 9 fresh review 未提及，可能已修复，待 Research Director 确认\"\n  action_items:\n    - round: 8\n      action: \"Related Work 扩展 Growing Pains 概念对比\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI 忽略家族内相关性（cluster bootstrap）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"理论上存在但不影响 directional conclusion\"\n    - round: 9\n      reviewers: []\n      note: \"Round 9 fresh review 未提及，可能已修复或被 graduated de-duplication (K=20, C%=29.1%) 充分缓解，待 Research Director 确认\"\n  action_items:\n    - round: 8\n      action: \"Limitations 补充 acknowledging family correlation + K=20 dedup robustness check\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MISS-REF\"\n  summary: \"缺少引用：Oren 2024, Deng 2024, MMLU-Pro, MMLU-Redux\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"3 必要 + 1 建议\"\n    - round: 9\n      reviewers: []\n      note: \"Round 9 fresh review 未提及这些具体引用，但提出了新的 missing refs。可能已补充，待确认。\"\n  action_items:\n    - round: 8\n      action: \"补充 Oren et al. (ICML 2024), Deng et al. (2024), MMLU-Pro, MMLU-Redux\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-22T01:57:02.785904+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 16125}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-22T01:59:54.535734+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "report": "# 审稿报告 — Round 9 (Fresh Review)\n\n**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**审稿模式**: Fresh（重新审稿，无前轮记忆）\n\n---\n\n## Summary\n\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，在 METABENCH 数据集（5,227 models × 12,508 MMLU items）上发现 31.3% 的题目在 2023–2024 模型群组间存在大幅度时序测量不稳定性（ETS-C），同时排名相关性高达 ρ≈0.997。论文构建了 cross-subject matching 的半合成注入框架（ΔFPR=0.000, ΔTPR=+0.508 at p=0.5），并揭示 web-overlap 污染标签与 DIF flags 近乎正交（enrichment≈0.96, φ=0.012），指出 contamination detection 社区的验证范式存在类别错误。六个 METABENCH benchmark 上均复现了 temporal DIF（C%=17.9%–31.3%, 45–174× above baseline）。\n\n---\n\n## Strengths\n\n**S1 [共识] Robustness checks 覆盖面极广**\n系统排除 6 种替代解释（ability confounding, family inflation, θ-conditioning, within-subject effects, ranking impact, local dependence），C% 在多种 matching 策略下均稳定在 ~28-29% 底线。随机拆分对照（0.18%）和能力分位对照（2.9%）形成有力的 null baseline bracket。这种论证深度在 NLP 实证论文中罕见。（R1-S2, R2-S1: 双方完全一致）\n\n**S2 [共识] Ground truth meta-critique 具有超越本文的方法论影响**\n揭示 web-overlap labels 与 DIF flags 近乎正交（enrichment=0.964, Jaccard=0.206, φ=0.012），挑战整个 contamination detection 社区使用 web-overlap 标签做 validation 的实践。任何以 web-overlap 作为 ground truth 验证 differential detector 的工作都面临同样的类别错误。两位 Reviewer 均认为这是论文最具影响力的 contribution。（R1-S3, R2-S2）\n\n**S3 [共识] Cross-subject matching 方法贡献干净可复用**\nΔFPR=0.000（bootstrap 95% CI=[0.000, 0.000]）的方法保证 + multi-subject injection 退化分析（k≤5: ΔFPR<0.007, k=10: 0.026–0.069）划定了清晰的适用边界。Remark 提供了构造性论证。该 matching 策略可独立于本文具体分析场景使用。（R1-S1, R2-S4）\n\n**S4 [共识] 跨 benchmark 复现**\n六个 benchmark 均展示显著 temporal DIF（45–174× above baseline），knowledge/reasoning > procedural 的模式合理且有可解释性。（R1-S4, R2-S3）\n\n**S5 [共识] 统计报告规范**\n几乎所有核心数字附有 CI/效应量/多重比较校正。Simpson's paradox 分析（aggregate OR=1.55→controlled OR=0.73）精巧地证明 DIF 是 item-level 而非 domain-level 副产物。（R1-S5/S6, R2-S1）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [共识: R1-W3 + R2-W2] 因果归因空白使 audit protocol 不可安全执行**\n- Section 5.3 提出 C%≥25% 时 \"rotate or retire flagged items\"，但 Limitations 承认 DIF 无法区分 contamination、capability evolution、training methodology shifts\n- Section 4.6 显示 DIF items 集中 discriminative signal（z=-8σ to -49σ），retire 这些 items = 移除 benchmark 中最有信息量的部分\n- 三层框架（impact/DIF/attribution）已加入 Discussion §5.1，但 Layer 3 完全悬空\n- **两位 Reviewer 共识**: \"retire flagged items\" 建议可能比不审计更有害。应改为 \"investigate and report alongside stable-item rankings\"\n- **Severity**: R2 标 critical，R1 标 warning（认为矛盾可通过 framing 修改解决而非 substance 缺陷）。Review Director 判定：**Must-Fix**（framing 修改即可解决，但不修改则直接削弱论文核心叙事）\n\n**MF2 [共识: R1-W5 + R2-W1] ρ≈0.997 practical significance paradox 削弱 \"instability\" 叙事**\n- 去除 31% 的 items 后排名几乎不变（ρ≈0.997），论文标题 \"Measurement Instability\" 的 urgency 被严重削弱\n- Family-level rank shifts（Llama-3: +53, Mistral: -35）是更有力的 practical significance 证据，但仅在附录出现\n- **关键遗漏**: 未报告 TruthfulQA (817 items)、ARC (1,172 items) 等小 benchmark 的 stable-item ρ 值——item 冗余度更低时 DIF 的排名影响可能显著更大\n- **两位 Reviewer 共识**: 需 (1) 报告所有 6 个 benchmark 的 ρ 值；(2) 将 family-level rank profile 提升到正文；(3) 补充 pairwise comparison flip rate；(4) 讨论 item 冗余度对 ρ 的影响\n- **Severity**: R2 标 critical（framing 矛盾），R1 标 warning（framing 问题非 substance 问题）。Review Director 判定：**Must-Fix**（论文核心叙事的说服力取决于此）\n\n### Should-Fix（不修改可能影响评分但不直接决定接收）\n\n**SF1 [共识: R1-W1 + R2-W5] 半合成注入 ecological validity 不足**\n- Binary flipping 是最极端的均匀利用模式，ΔTPR=+0.508 实为 upper bound\n- 论文已在 §3.4 和 Limitations 标注 \"upper-bound estimate\"——较前轮有改善\n- **共识**: 正文应更明确区分：ΔFPR=0.000 是 matching strategy 性质（不依赖注入现实性），ΔTPR 是 upper-bound（受注入模型限制）\n- R1 建议按 difficulty 分层的非均匀 flipping 作为 robustness check，但两位均认为非 must-fix\n\n**SF2 [共识: R1-W2, R2 AGREE] LLM examinees 非独立性缺乏理论讨论**\n- LLM 共享 base model/训练数据/架构，违反 MH χ² 独立性假设\n- §3.2 提供经验处理（permutation LD inflation <0.001pp, graduated de-duplication），但缺乏理论框架\n- **建议**: 引用 French & Finch (2010) 讨论 clustered data 中 MH test 的 size 表现\n- **Severity**: R1 标 warning，R2 确认 warning（经验证据 adequate 但理论缺失仍是弱点）\n\n**SF3 [R2-W4, R1 AGREE] `\\enlargethispage{18\\baselineskip}` 格式操作过于激进**\n- discussion.tex line 3 使用 ≈18 行额外空间（~8.3cm），可能被 PC 视为规避页数限制\n- 去除后 Discussion+Conclusion 很可能溢出到第 9 页\n- **建议**: 压缩 Discussion 重复内容（SF5）使正文自然 fit 在 8 页内\n- **R1 补充**: 不应影响学术评价，但 camera-ready 必须修正\n\n**SF4 [R2-W3, R1 REBUT — DISPUTED] 方法新颖性有限**\n- MH-DIF 是 1988 年标准方法，ETS 分类是标准实践\n- R1 反驳：ARR H14 不应因方法不 complex 而贬低；论文定位 \"methodological+empirical\" 合理；C2 和 cross-subject matching 有独立方法论价值\n- **共识方向**: 两位均同意更突出 C2（ground truth meta-critique）作为首要 contribution 可加强论文\n- **Review Director 判定**: novelty 确有限但不应成为主要扣分项——论文价值在 critique + empirical findings\n\n### Nice-to-Fix（改善质量但不影响评分）\n\n**NF1 [R1-W4, R2 REBUT → info] Permutation test 200 次迭代**\n- p=0.005 恰为分辨率极限（1/200），建议增至 1,000 次\n- R2 反驳：per-subject 1,000 perm 结果一致，增加迭代不改变结论\n- **共识**: info 级别，非 must-fix\n\n**NF2 [R2-W6, R1 REBUT → minor] 关键统计量重复呈现**\n- enrichment≈0.964 出现 5+ 次，Discussion 近乎完全重复 Experiments 数字，Conclusion 仅两行\n- R1 认为学术论文惯例，[warning] 偏高\n- **共识方向**: 降为 minor issue，但压缩 Discussion 可为移除 `\\enlargethispage` 腾出空间\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致（所有 [AGREE]）：\n\n1. **Ground truth meta-critique 是论文最强 contribution**——应提升为首要贡献\n2. **因果归因空白与 \"retire items\" 建议存在逻辑矛盾**——audit protocol 需改为更保守的措辞\n3. **ρ≈0.997 需更 nuanced 解读**——需报告其他 benchmark 的 ρ、family-level profiles、pairwise flip rate\n4. **半合成注入 ecological validity 不足**——ΔTPR 为 upper bound，正文应更清晰区分 FPR 控制 vs TPR 估计\n5. **LLM non-independence 需要理论讨论**——经验处理充分但理论框架缺失\n6. **GSM1K (N=33) 应严格标注为 exploratory**——Abstract 不应隐含使用其作为核心支撑\n\n## Reviewer Divergence\n\n| 议题 | R1 立场 | R2 立场 | Director 判定 |\n|------|---------|---------|--------------|\n| ρ≈0.997 severity | warning（framing 问题） | critical（削弱核心叙事） | Must-Fix（可通过 framing 修改解决） |\n| 因果归因 severity | warning | critical | Must-Fix（同上） |\n| 方法新颖性 (R2-W3) | REBUT（ARR H14, 跨领域应用有价值） | warning（EMNLP main 有顾虑） | Should-Fix（突出 C2 即可缓解） |\n| 统计量重复 (R2-W6) | REBUT（降为 minor） | warning | Minor Issue |\n| 格式合规 | 判定合规 | `\\enlargethispage` 值得标记 | Should-Fix（camera-ready 必须移除） |\n| R1-W6 subject 粒度 | matching variable 可能包含被测信号 | REBUT 机制描述（by construction 排除），但 AGREE 分析价值 | Nice-to-have 分析（C% vs subject size 相关性） |\n\n---\n\n## Questions（需作者回应）\n\n**Q1 [高优先级]** Table 3 中 TruthfulQA (817 items)、ARC (1,172 items) 等 benchmark 的 stable-item vs. full ranking ρ 值是多少？如果 ρ 显著低于 0.997，这将大大加强 practical significance 论证。（R2-Q1, R1 AGREE）\n\n**Q2 [高优先级]** 1:1 nearest-neighbor matching 是用 total score 还是 IRT θ 做的？从 (1080, 807) 降到 (638, 638) 丢弃了大量模型，是否分析了被丢弃模型的特征分布？（R1-Q1, R2 AGREE）\n\n**Q3** difficulty-direction interaction ρ=-0.597 是否在 6 个 benchmark 上都一致？如果是，可能指向特定训练方法论变化（如 RLHF/DPO 对难题偏好）。（R2-Q2）\n\n**Q4** Within-subject C%=38.1% > Temporal 31.3% 的原因？需报告 5 个 subject 各自的 C% 分布，讨论可能的 type-I error inflation。（R1-Q3, R2 AGREE）\n\n**Q5** IRT θ 与 total scores r=0.9986——IRT framing 的实际附加价值是什么？论文本质上是 CTT-based DIF 应用，是否应更明确指出？（R1-Q5, R2 AGREE）\n\n**Q6** Section 5.3 建议 ≥500 个新模型时运行 DIF，但 power analysis 显示 N≥80 即可。500 的阈值依据？（R2-Q4）\n\n**Q7** 2PL 拟合差（Appendix A.2）但 power analysis 使用 2PL 参数——两条证据线（parametric power analysis + empirical semi-synthetic ΔTPR）的 triangulation 是否足以支撑 power 结论？（R1-Q2, R2 AGREE triangulation adequate）\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同建议**:\n1. **French, B. F., & Finch, W. H. (2010)**. Hierarchical logistic regression: Accounting for multilevel data in DIF detection. *JEM*, 47(3), 299–317. — 直接关联 SF2（clustered data 中 DIF 检测）\n2. **Kolen, M. J., & Brennan, R. L. (2014)**. *Test Equating, Scaling, and Linking*. — 经典 equating 文献，与 Growing Pains FPC 方法的讨论相关\n\n**R1 额外建议**: Magis, D., & De Boeck, P. (2012). A robust outlier approach to prevent type I error inflation in DIF. *EPM*, 72(2), 291–311.\n\n**R2 额外建议**:\n- Putnick, D. L., & Bornstein, M. H. (2016). Measurement invariance conventions and reporting. *DP*, 52(9), 1–11.\n- Polo et al. (2024) Efficient Multi-Prompt Evaluation of LLMs — IRT-based efficient evaluation（可能已引用 TinyBenchmarks）\n\n以上均为 nice-to-have，非 critical omission。Overall Related Work 覆盖较完整。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: pending（已于 2026-05-22T01:42 发送请求，8 小时后自动提醒）\n\n外部审稿结果尚未返回。内部审稿不等待外部结果。如后续收到，请 Research Director 参考其中与内部审稿的差异，特别关注内部 Reviewer 可能遗漏的 related work 和 weakness。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（2026-05-22T01:44 完成）\n**统计**: 0 critical, 3 warning, 15 info\n\n### Warnings:\n1. **Pages 3–6 视觉沙漠**: 连续 4 页近乎纯文本（仅 page 4 有 1 个 equation），Related Work → Method → Experiments 开头形成文字墙。建议在 Method 增加流程图或方法概览表。\n2. **Page 7 视觉密度过度集中**: Table 1 + Figure 2 + Table 2 挤在同一页，与前 4 页纯文本形成极端 feast-or-famine 节奏。建议前移部分 display items。\n3. **Page 14 (Appendix) 空白浪费**: Figure 4 与 Figure 5 之间大面积空白（~1/4 页），建议合并为 2-panel figure。\n\n### 其他观察:\n- 主文 8 页内共 5 个 display items（0.63/页），偏低但可接受\n- Figure 1 子图文字偏小，建议放大\n- Figure 5 散点图标签重叠，建议使用 adjustText\n- 整体排版符合 ACL 模板规范，无 margin 溢出、无公式渲染错误\n\n---\n\n## Overall Assessment\n\n### 总评\n\n| 维度 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | 3.75/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n| **Overall** | **3.5** | **3.5** | **3.5 (Borderline Conference)** |\n\n### Overall: 3.5 — Borderline Conference\n\n**一句话总结**: 方法扎实、robustness checks 印象深刻的大规模 psychometric 审计工作，ground truth meta-critique 有超越本文的方法论影响，但 practical significance paradox（ρ≈0.997）和因果归因空白使核心叙事说服力受限、audit protocol 不可安全执行。\n\n**接收条件（从 3.5 → 4.0 的路径）**:\n1. **[Must-Fix] 修改 audit protocol 措辞**: \"rotate or retire\" → \"investigate and report alongside stable-item rankings\"，消除 §5.3 与 §4.6 的逻辑矛盾\n2. **[Must-Fix] 加强 practical significance 论证**: 报告所有 6 个 benchmark 的 stable-item ρ 值 + family-level rank profiles 提升到正文 + pairwise flip rate\n3. **[Should-Fix] 补充 LLM non-independence 理论讨论**: 引用 French & Finch (2010)，在 §3.2 或 Limitations 增加一段\n4. **[Should-Fix] 移除 `\\enlargethispage{18\\baselineskip}`**: 压缩 Discussion 重复内容使正文自然 fit 8 页\n5. **[Should-Fix] 重排 contributions 权重**: C2（meta-critique）升为首要贡献\n\n以上修改均为文本层面调整，不需要新实验，在 deadline（2026-05-25）前可完成。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度过高：一句话中同时出现 ΔFPR, ΔTPR, enrichment, φ, C%, z-scores, ρ。建议拆分核心 contribution 和具体数字。\n- GSM1K 相关的结论措辞应明确标注为 exploratory（当前隐含为 confirmed finding）。\n\n### Section 3 (Method)\n- §3.2 LLM-specific challenges：4 个 challenge 各仅简要提及，核心理论空白在于 MH χ² 依赖 examinees 独立性假设，LLM 不满足。建议增加一段理论讨论。\n- §3.4 Semi-synthetic framework：正文应在此处（而非仅 Limitations）明确区分 ΔFPR=0.000（matching strategy 性质）vs ΔTPR（upper bound）。\n- Remark (formerly Proposition)：降格后措辞合理，无进一步问题。\n\n### Section 4 (Experiments)\n- §4.1 Power analysis：已报告 TPR 随 a 参数变化（0.40→0.95）+ Jensen's inequality，较前轮改善明显。但 2PL 拟合差（Appendix A.2）与 2PL-based power analysis 的一致性应更明确讨论。\n- §4.2 Temporal comparability：permutation test 200 次已标注 \"resolution limit\"，per-subject 1,000 perm 提供佐证。建议增至 1,000 次（info 级别）。\n- §4.4 Structural analysis：within-subject C%=38.1% 仅报告 mean，需报告 5 个 subject 各自的 C% 分布。~28-29% convergence 的讨论已改善但仍可深化。\n- §4.5 Downstream impact：ρ≈0.997 是论文的 elephant in the room。需同时报告 (a) 其他 benchmark 的 ρ；(b) pairwise comparison flip rate；(c) family-level rank shifts（从附录提升到正文）。z=-8σ to -49σ 的含义对非心理计量学读者不够直观，建议添加一句解释。\n- §4.7 Cross-benchmark：6-month window C%=34.35% > annual 31.3%，暗示 calendar year 划分可能低估 temporal DIF——值得在 Discussion 中讨论 temporal resolution 的影响。\n\n### Section 5 (Discussion)\n- `\\enlargethispage{18\\baselineskip}` 必须移除。压缩策略：(1) 减少与 Section 4 重复的统计量重述；(2) §5.1 第一段的三层框架可精简措辞；(3) §5.2 Ground Truth Meta-Critique 与 §4.3 高度重叠。\n- §5.3 \"rotate or retire flagged items\" 必须改为更保守的措辞。\n\n### Section 6 (Conclusion)\n- 仅两行，是 Abstract 压缩版。应总结 implications 而非重复统计量。但考虑到页数压力，两行也可接受。\n\n### Limitations\n- 覆盖 3 个维度（scope/boundary/generalizability），符合 EMNLP 规范。\n- 已承认 binary flipping 为 worst-case、因果归因不可达、GSM1K exploratory。\n\n### Appendix\n- Page 14: Figure 4 和 Figure 5 之间空白过大，建议合并为 2-panel figure。\n- Figure 5 标签重叠需处理。\n\n### 引用\n- 无幻觉引用（此前 Round 中发现的 Tutz & Friedman 已移除）。\n- Holland & Thayer (1988) 引用年份正确（ETS Research Report RR-88-31，R2 误报已由 R1 纠正）。\n- 缺少经典 psychometric 综述文献（French & Finch 2010, Kolen & Brennan 2014 等），建议选择性补充。\n\n### 格式\n- ACL review mode template (`\\usepackage[review]{acl}`)：正确\n- 匿名：未发现作者信息泄露\n- 正文 ≤8 页：**borderline**——依赖 `\\enlargethispage{18\\baselineskip}` 才 fit，去除后可能溢出\n- References 后 Appendix：正确\n- 图表编号和交叉引用：正确（使用 cleveref）\n- Figure 1 缺少 axis labels（x=Ability θ, y=P(correct)）：camera-ready 时修复",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "report": "# 审稿报告 — Round 9 (Fresh Review)\n\n**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）\n**审稿模式**: Fresh（重新审稿，无前轮记忆）\n\n---\n\n## Summary\n\n本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，在 METABENCH 数据集（5,227 models × 12,508 MMLU items）上发现 31.3% 的题目在 2023–2024 模型群组间存在大幅度时序测量不稳定性（ETS-C），同时排名相关性高达 ρ≈0.997。论文构建了 cross-subject matching 的半合成注入框架（ΔFPR=0.000, ΔTPR=+0.508 at p=0.5），并揭示 web-overlap 污染标签与 DIF flags 近乎正交（enrichment≈0.96, φ=0.012），指出 contamination detection 社区的验证范式存在类别错误。六个 METABENCH benchmark 上均复现了 temporal DIF（C%=17.9%–31.3%, 45–174× above baseline）。\n\n---\n\n## Strengths\n\n**S1 [共识] Robustness checks 覆盖面极广**\n系统排除 6 种替代解释（ability confounding, family inflation, θ-conditioning, within-subject effects, ranking impact, local dependence），C% 在多种 matching 策略下均稳定在 ~28-29% 底线。随机拆分对照（0.18%）和能力分位对照（2.9%）形成有力的 null baseline bracket。这种论证深度在 NLP 实证论文中罕见。（R1-S2, R2-S1: 双方完全一致）\n\n**S2 [共识] Ground truth meta-critique 具有超越本文的方法论影响**\n揭示 web-overlap labels 与 DIF flags 近乎正交（enrichment=0.964, Jaccard=0.206, φ=0.012），挑战整个 contamination detection 社区使用 web-overlap 标签做 validation 的实践。任何以 web-overlap 作为 ground truth 验证 differential detector 的工作都面临同样的类别错误。两位 Reviewer 均认为这是论文最具影响力的 contribution。（R1-S3, R2-S2）\n\n**S3 [共识] Cross-subject matching 方法贡献干净可复用**\nΔFPR=0.000（bootstrap 95% CI=[0.000, 0.000]）的方法保证 + multi-subject injection 退化分析（k≤5: ΔFPR<0.007, k=10: 0.026–0.069）划定了清晰的适用边界。Remark 提供了构造性论证。该 matching 策略可独立于本文具体分析场景使用。（R1-S1, R2-S4）\n\n**S4 [共识] 跨 benchmark 复现**\n六个 benchmark 均展示显著 temporal DIF（45–174× above baseline），knowledge/reasoning > procedural 的模式合理且有可解释性。（R1-S4, R2-S3）\n\n**S5 [共识] 统计报告规范**\n几乎所有核心数字附有 CI/效应量/多重比较校正。Simpson's paradox 分析（aggregate OR=1.55→controlled OR=0.73）精巧地证明 DIF 是 item-level 而非 domain-level 副产物。（R1-S5/S6, R2-S1）\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1 [共识: R1-W3 + R2-W2] 因果归因空白使 audit protocol 不可安全执行**\n- Section 5.3 提出 C%≥25% 时 \"rotate or retire flagged items\"，但 Limitations 承认 DIF 无法区分 contamination、capability evolution、training methodology shifts\n- Section 4.6 显示 DIF items 集中 discriminative signal（z=-8σ to -49σ），retire 这些 items = 移除 benchmark 中最有信息量的部分\n- 三层框架（impact/DIF/attribution）已加入 Discussion §5.1，但 Layer 3 完全悬空\n- **两位 Reviewer 共识**: \"retire flagged items\" 建议可能比不审计更有害。应改为 \"investigate and report alongside stable-item rankings\"\n- **Severity**: R2 标 critical，R1 标 warning（认为矛盾可通过 framing 修改解决而非 substance 缺陷）。Review Director 判定：**Must-Fix**（framing 修改即可解决，但不修改则直接削弱论文核心叙事）\n\n**MF2 [共识: R1-W5 + R2-W1] ρ≈0.997 practical significance paradox 削弱 \"instability\" 叙事**\n- 去除 31% 的 items 后排名几乎不变（ρ≈0.997），论文标题 \"Measurement Instability\" 的 urgency 被严重削弱\n- Family-level rank shifts（Llama-3: +53, Mistral: -35）是更有力的 practical significance 证据，但仅在附录出现\n- **关键遗漏**: 未报告 TruthfulQA (817 items)、ARC (1,172 items) 等小 benchmark 的 stable-item ρ 值——item 冗余度更低时 DIF 的排名影响可能显著更大\n- **两位 Reviewer 共识**: 需 (1) 报告所有 6 个 benchmark 的 ρ 值；(2) 将 family-level rank profile 提升到正文；(3) 补充 pairwise comparison flip rate；(4) 讨论 item 冗余度对 ρ 的影响\n- **Severity**: R2 标 critical（framing 矛盾），R1 标 warning（framing 问题非 substance 问题）。Review Director 判定：**Must-Fix**（论文核心叙事的说服力取决于此）\n\n### Should-Fix（不修改可能影响评分但不直接决定接收）\n\n**SF1 [共识: R1-W1 + R2-W5] 半合成注入 ecological validity 不足**\n- Binary flipping 是最极端的均匀利用模式，ΔTPR=+0.508 实为 upper bound\n- 论文已在 §3.4 和 Limitations 标注 \"upper-bound estimate\"——较前轮有改善\n- **共识**: 正文应更明确区分：ΔFPR=0.000 是 matching strategy 性质（不依赖注入现实性），ΔTPR 是 upper-bound（受注入模型限制）\n- R1 建议按 difficulty 分层的非均匀 flipping 作为 robustness check，但两位均认为非 must-fix\n\n**SF2 [共识: R1-W2, R2 AGREE] LLM examinees 非独立性缺乏理论讨论**\n- LLM 共享 base model/训练数据/架构，违反 MH χ² 独立性假设\n- §3.2 提供经验处理（permutation LD inflation <0.001pp, graduated de-duplication），但缺乏理论框架\n- **建议**: 引用 French & Finch (2010) 讨论 clustered data 中 MH test 的 size 表现\n- **Severity**: R1 标 warning，R2 确认 warning（经验证据 adequate 但理论缺失仍是弱点）\n\n**SF3 [R2-W4, R1 AGREE] `\\enlargethispage{18\\baselineskip}` 格式操作过于激进**\n- discussion.tex line 3 使用 ≈18 行额外空间（~8.3cm），可能被 PC 视为规避页数限制\n- 去除后 Discussion+Conclusion 很可能溢出到第 9 页\n- **建议**: 压缩 Discussion 重复内容（SF5）使正文自然 fit 在 8 页内\n- **R1 补充**: 不应影响学术评价，但 camera-ready 必须修正\n\n**SF4 [R2-W3, R1 REBUT — DISPUTED] 方法新颖性有限**\n- MH-DIF 是 1988 年标准方法，ETS 分类是标准实践\n- R1 反驳：ARR H14 不应因方法不 complex 而贬低；论文定位 \"methodological+empirical\" 合理；C2 和 cross-subject matching 有独立方法论价值\n- **共识方向**: 两位均同意更突出 C2（ground truth meta-critique）作为首要 contribution 可加强论文\n- **Review Director 判定**: novelty 确有限但不应成为主要扣分项——论文价值在 critique + empirical findings\n\n### Nice-to-Fix（改善质量但不影响评分）\n\n**NF1 [R1-W4, R2 REBUT → info] Permutation test 200 次迭代**\n- p=0.005 恰为分辨率极限（1/200），建议增至 1,000 次\n- R2 反驳：per-subject 1,000 perm 结果一致，增加迭代不改变结论\n- **共识**: info 级别，非 must-fix\n\n**NF2 [R2-W6, R1 REBUT → minor] 关键统计量重复呈现**\n- enrichment≈0.964 出现 5+ 次，Discussion 近乎完全重复 Experiments 数字，Conclusion 仅两行\n- R1 认为学术论文惯例，[warning] 偏高\n- **共识方向**: 降为 minor issue，但压缩 Discussion 可为移除 `\\enlargethispage` 腾出空间\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全一致（所有 [AGREE]）：\n\n1. **Ground truth meta-critique 是论文最强 contribution**——应提升为首要贡献\n2. **因果归因空白与 \"retire items\" 建议存在逻辑矛盾**——audit protocol 需改为更保守的措辞\n3. **ρ≈0.997 需更 nuanced 解读**——需报告其他 benchmark 的 ρ、family-level profiles、pairwise flip rate\n4. **半合成注入 ecological validity 不足**——ΔTPR 为 upper bound，正文应更清晰区分 FPR 控制 vs TPR 估计\n5. **LLM non-independence 需要理论讨论**——经验处理充分但理论框架缺失\n6. **GSM1K (N=33) 应严格标注为 exploratory**——Abstract 不应隐含使用其作为核心支撑\n\n## Reviewer Divergence\n\n| 议题 | R1 立场 | R2 立场 | Director 判定 |\n|------|---------|---------|--------------|\n| ρ≈0.997 severity | warning（framing 问题） | critical（削弱核心叙事） | Must-Fix（可通过 framing 修改解决） |\n| 因果归因 severity | warning | critical | Must-Fix（同上） |\n| 方法新颖性 (R2-W3) | REBUT（ARR H14, 跨领域应用有价值） | warning（EMNLP main 有顾虑） | Should-Fix（突出 C2 即可缓解） |\n| 统计量重复 (R2-W6) | REBUT（降为 minor） | warning | Minor Issue |\n| 格式合规 | 判定合规 | `\\enlargethispage` 值得标记 | Should-Fix（camera-ready 必须移除） |\n| R1-W6 subject 粒度 | matching variable 可能包含被测信号 | REBUT 机制描述（by construction 排除），但 AGREE 分析价值 | Nice-to-have 分析（C% vs subject size 相关性） |\n\n---\n\n## Questions（需作者回应）\n\n**Q1 [高优先级]** Table 3 中 TruthfulQA (817 items)、ARC (1,172 items) 等 benchmark 的 stable-item vs. full ranking ρ 值是多少？如果 ρ 显著低于 0.997，这将大大加强 practical significance 论证。（R2-Q1, R1 AGREE）\n\n**Q2 [高优先级]** 1:1 nearest-neighbor matching 是用 total score 还是 IRT θ 做的？从 (1080, 807) 降到 (638, 638) 丢弃了大量模型，是否分析了被丢弃模型的特征分布？（R1-Q1, R2 AGREE）\n\n**Q3** difficulty-direction interaction ρ=-0.597 是否在 6 个 benchmark 上都一致？如果是，可能指向特定训练方法论变化（如 RLHF/DPO 对难题偏好）。（R2-Q2）\n\n**Q4** Within-subject C%=38.1% > Temporal 31.3% 的原因？需报告 5 个 subject 各自的 C% 分布，讨论可能的 type-I error inflation。（R1-Q3, R2 AGREE）\n\n**Q5** IRT θ 与 total scores r=0.9986——IRT framing 的实际附加价值是什么？论文本质上是 CTT-based DIF 应用，是否应更明确指出？（R1-Q5, R2 AGREE）\n\n**Q6** Section 5.3 建议 ≥500 个新模型时运行 DIF，但 power analysis 显示 N≥80 即可。500 的阈值依据？（R2-Q4）\n\n**Q7** 2PL 拟合差（Appendix A.2）但 power analysis 使用 2PL 参数——两条证据线（parametric power analysis + empirical semi-synthetic ΔTPR）的 triangulation 是否足以支撑 power 结论？（R1-Q2, R2 AGREE triangulation adequate）\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同建议**:\n1. **French, B. F., & Finch, W. H. (2010)**. Hierarchical logistic regression: Accounting for multilevel data in DIF detection. *JEM*, 47(3), 299–317. — 直接关联 SF2（clustered data 中 DIF 检测）\n2. **Kolen, M. J., & Brennan, R. L. (2014)**. *Test Equating, Scaling, and Linking*. — 经典 equating 文献，与 Growing Pains FPC 方法的讨论相关\n\n**R1 额外建议**: Magis, D., & De Boeck, P. (2012). A robust outlier approach to prevent type I error inflation in DIF. *EPM*, 72(2), 291–311.\n\n**R2 额外建议**:\n- Putnick, D. L., & Bornstein, M. H. (2016). Measurement invariance conventions and reporting. *DP*, 52(9), 1–11.\n- Polo et al. (2024) Efficient Multi-Prompt Evaluation of LLMs — IRT-based efficient evaluation（可能已引用 TinyBenchmarks）\n\n以上均为 nice-to-have，非 critical omission。Overall Related Work 覆盖较完整。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: pending（已于 2026-05-22T01:42 发送请求，8 小时后自动提醒）\n\n外部审稿结果尚未返回。内部审稿不等待外部结果。如后续收到，请 Research Director 参考其中与内部审稿的差异，特别关注内部 Reviewer 可能遗漏的 related work 和 weakness。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: done（2026-05-22T01:44 完成）\n**统计**: 0 critical, 3 warning, 15 info\n\n### Warnings:\n1. **Pages 3–6 视觉沙漠**: 连续 4 页近乎纯文本（仅 page 4 有 1 个 equation），Related Work → Method → Experiments 开头形成文字墙。建议在 Method 增加流程图或方法概览表。\n2. **Page 7 视觉密度过度集中**: Table 1 + Figure 2 + Table 2 挤在同一页，与前 4 页纯文本形成极端 feast-or-famine 节奏。建议前移部分 display items。\n3. **Page 14 (Appendix) 空白浪费**: Figure 4 与 Figure 5 之间大面积空白（~1/4 页），建议合并为 2-panel figure。\n\n### 其他观察:\n- 主文 8 页内共 5 个 display items（0.63/页），偏低但可接受\n- Figure 1 子图文字偏小，建议放大\n- Figure 5 散点图标签重叠，建议使用 adjustText\n- 整体排版符合 ACL 模板规范，无 margin 溢出、无公式渲染错误\n\n---\n\n## Overall Assessment\n\n### 总评\n\n| 维度 | R1 | R2 | 共识 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | 3.75/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n| **Overall** | **3.5** | **3.5** | **3.5 (Borderline Conference)** |\n\n### Overall: 3.5 — Borderline Conference\n\n**一句话总结**: 方法扎实、robustness checks 印象深刻的大规模 psychometric 审计工作，ground truth meta-critique 有超越本文的方法论影响，但 practical significance paradox（ρ≈0.997）和因果归因空白使核心叙事说服力受限、audit protocol 不可安全执行。\n\n**接收条件（从 3.5 → 4.0 的路径）**:\n1. **[Must-Fix] 修改 audit protocol 措辞**: \"rotate or retire\" → \"investigate and report alongside stable-item rankings\"，消除 §5.3 与 §4.6 的逻辑矛盾\n2. **[Must-Fix] 加强 practical significance 论证**: 报告所有 6 个 benchmark 的 stable-item ρ 值 + family-level rank profiles 提升到正文 + pairwise flip rate\n3. **[Should-Fix] 补充 LLM non-independence 理论讨论**: 引用 French & Finch (2010)，在 §3.2 或 Limitations 增加一段\n4. **[Should-Fix] 移除 `\\enlargethispage{18\\baselineskip}`**: 压缩 Discussion 重复内容使正文自然 fit 8 页\n5. **[Should-Fix] 重排 contributions 权重**: C2（meta-critique）升为首要贡献\n\n以上修改均为文本层面调整，不需要新实验，在 deadline（2026-05-25）前可完成。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度过高：一句话中同时出现 ΔFPR, ΔTPR, enrichment, φ, C%, z-scores, ρ。建议拆分核心 contribution 和具体数字。\n- GSM1K 相关的结论措辞应明确标注为 exploratory（当前隐含为 confirmed finding）。\n\n### Section 3 (Method)\n- §3.2 LLM-specific challenges：4 个 challenge 各仅简要提及，核心理论空白在于 MH χ² 依赖 examinees 独立性假设，LLM 不满足。建议增加一段理论讨论。\n- §3.4 Semi-synthetic framework：正文应在此处（而非仅 Limitations）明确区分 ΔFPR=0.000（matching strategy 性质）vs ΔTPR（upper bound）。\n- Remark (formerly Proposition)：降格后措辞合理，无进一步问题。\n\n### Section 4 (Experiments)\n- §4.1 Power analysis：已报告 TPR 随 a 参数变化（0.40→0.95）+ Jensen's inequality，较前轮改善明显。但 2PL 拟合差（Appendix A.2）与 2PL-based power analysis 的一致性应更明确讨论。\n- §4.2 Temporal comparability：permutation test 200 次已标注 \"resolution limit\"，per-subject 1,000 perm 提供佐证。建议增至 1,000 次（info 级别）。\n- §4.4 Structural analysis：within-subject C%=38.1% 仅报告 mean，需报告 5 个 subject 各自的 C% 分布。~28-29% convergence 的讨论已改善但仍可深化。\n- §4.5 Downstream impact：ρ≈0.997 是论文的 elephant in the room。需同时报告 (a) 其他 benchmark 的 ρ；(b) pairwise comparison flip rate；(c) family-level rank shifts（从附录提升到正文）。z=-8σ to -49σ 的含义对非心理计量学读者不够直观，建议添加一句解释。\n- §4.7 Cross-benchmark：6-month window C%=34.35% > annual 31.3%，暗示 calendar year 划分可能低估 temporal DIF——值得在 Discussion 中讨论 temporal resolution 的影响。\n\n### Section 5 (Discussion)\n- `\\enlargethispage{18\\baselineskip}` 必须移除。压缩策略：(1) 减少与 Section 4 重复的统计量重述；(2) §5.1 第一段的三层框架可精简措辞；(3) §5.2 Ground Truth Meta-Critique 与 §4.3 高度重叠。\n- §5.3 \"rotate or retire flagged items\" 必须改为更保守的措辞。\n\n### Section 6 (Conclusion)\n- 仅两行，是 Abstract 压缩版。应总结 implications 而非重复统计量。但考虑到页数压力，两行也可接受。\n\n### Limitations\n- 覆盖 3 个维度（scope/boundary/generalizability），符合 EMNLP 规范。\n- 已承认 binary flipping 为 worst-case、因果归因不可达、GSM1K exploratory。\n\n### Appendix\n- Page 14: Figure 4 和 Figure 5 之间空白过大，建议合并为 2-panel figure。\n- Figure 5 标签重叠需处理。\n\n### 引用\n- 无幻觉引用（此前 Round 中发现的 Tutz & Friedman 已移除）。\n- Holland & Thayer (1988) 引用年份正确（ETS Research Report RR-88-31，R2 误报已由 R1 纠正）。\n- 缺少经典 psychometric 综述文献（French & Finch 2010, Kolen & Brennan 2014 等），建议选择性补充。\n\n### 格式\n- ACL review mode template (`\\usepackage[review]{acl}`)：正确\n- 匿名：未发现作者信息泄露\n- 正文 ≤8 页：**borderline**——依赖 `\\enlargethispage{18\\baselineskip}` 才 fit，去除后可能溢出\n- References 后 Appendix：正确\n- 图表编号和交叉引用：正确（使用 cleveref）\n- Figure 1 缺少 axis labels（x=Ability θ, y=P(correct)）：camera-ready 时修复",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-22T01:59:59.104290+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4568
}
```

</details>

---


### Assistant

_source line 354 · 2026-05-22T02:00:07.170878+00:00_

**圆桌审稿 Round 9 完成，报告已投递。**

汇总：

- **Overall**: 3.5 (Borderline Conference)，R1 和 R2 完全一致
- **Soundness**: 3.75/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5

**核心问题（Must-Fix, 均为文本修改，不需新实验）**：
1. §5.3 "rotate or retire flagged items" 与 §4.6 DIF items 集中 discriminative signal 存在逻辑矛盾——需改为 "investigate and report"
2. ρ≈0.997 practical significance 论证不足——需报告其他 benchmark 的 ρ 值、提升 family-level rank profiles 到正文

**Should-Fix**: LLM non-independence 理论讨论、移除 `\enlargethispage{18\baselineskip}`、重排 contributions 权重（C2 升为首要）

**从 3.5→4.0 的路径**: 以上 5 项修改均可在 deadline（5/25）前完成。

Issue tracker 已同步更新至 `review_issues.yaml`。外部审稿（Stanford Agentic Reviewer）仍 pending，视觉审查已完成（0 critical, 3 warning）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 355 · 2026-05-22T02:00:09.120528+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：R1 和 R2 在四个关键点上高度一致——ground truth meta-critique 最强、注入模型 ecological validity 不足、因果归因空白与 retire 建议矛盾、ρ≈0.997 需更多 nuance。主要分歧在严重程度判定——我将 ρ paradox 和因果归因列为 critical，R1 仅列为 warning。我维持 3.5 (Borderline Conference) 评分。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 再回应 — 对 Reviewer 1 的 [REBUT] 项

---

### R2-W3 (方法新颖性有限) — 接受 R1 反驳，降级为 info

R1 引用 ARR reviewer guidelines H14 pitfall（"simpler methods that work should not be penalized"）是一个有力的程序性论据。重新审视后，我同意我的原始评价对 novelty 的权重过高。具体而言：

1. 论文自身定位为 "methodological and empirical, not algorithmic"（Section 1），这一自我定位是诚实的，不应因论文没有声称技术创新而扣分。
2. C2（ground truth meta-critique）确实是方法论层面的新颖洞察——它不是应用已有方法，而是挑战了一个被广泛接受的验证范式。这种 "meta-level" 的贡献与技术创新是不同维度的新颖性。
3. Cross-subject matching 虽有 psychometric 先例（Nandakumar 1993），但将其适配到 LLM benchmark 的 multi-domain local dependence 场景并实证验证 ΔFPR=0.000，这一工程贡献不应被忽视。

**修正判断**: 将 W3 从 [warning] 降为 [info]。方法新颖性有限是一个客观事实（论文自身也承认），但不应作为 weakness 影响评分。这一调整不改变我的 overall 评分，因为 W1（ρ ≈ 0.997 practical significance paradox）和 W2（因果归因空白）仍然是 critical issues。

---

### R2-W6 (关键统计量重复呈现) — 部分接受，降级为 minor

R1 指出 Abstract→Intro→Results→Discussion→Conclusion 的重复是学术论文正常惯例，这一点我接受。standalone section 需要自含关键数据，这是合理的写作实践。

但我维持一个具体观察：enrichment ≈ 0.964、Jaccard = 0.206、φ = 0.012 这组三连数字在 Abstract（line 2）、Introduction（¶2）、Section 4.3、Section 5.2、以及 Conclusion 中出现了至少 5 次，每次以几乎相同的句式呈现。Discussion Section 5.2 几乎是 Section 4.3 的逐句 paraphrase，缺乏 higher-level synthesis（例如：这一 near-independence 对未来 contamination detection 研究的具体 implications 是什么？哪些替代 ground truth 值得探索？）。

**修正判断**: 从 [warning] 降为 Minor Issue。核心建议不变：Discussion 应减少数字复述，增加 forward-looking synthesis。

---

### R2-Q4 (500 模型阈值) — 接受 R1 澄清

R1 指出 Section 4.1 的 power analysis 表明 N ≥ 80 per cohort 即可达到合理 power，500 models 的建议远超此阈值，因此 500 本身不需要额外 justification。

我接受这一澄清。我原始问题的意图是 "500 这个数字是怎么来的"，答案是它是一个保守的实用建议（远超 power 要求）。但我仍建议论文在 Section 5.3 中添加一句将 500 与 power analysis 显式关联的说明（如 "... whenever ≥500 new models accumulate (well above the N≥80 power floor from Section 4.1)"），让读者不必自行推断。

---

### R2-Q5 (单一 domain external matching) — 接受 R1 澄清，维持建议

R1 指出论文 Section 3.2 已定义了三种 matching 策略（standard / cross-subject / external），且 GSM8K 分析使用 external matching（MMLU total score 作 matching variable），细节在 Appendix。

我接受论文确实涵盖了这一点。我的原始问题源于正文 Section 4.7 对 GSM8K external matching 的描述过于简略——读者需要翻到 Appendix 才能理解 GSM8K 分析的 matching 细节。建议在 Section 4.7 正文中添加一句明确说明（如 "using MMLU total score as external matching variable; see Appendix for FPR validation"）。

---

### R2-M4 (holland1988mh 年份) — 接受 R1 反驳，撤回

R1 的纠正是准确的。Holland & Thayer (1988) 是 ETS Research Report RR-88-31-ONR，出版年份确为 1988。OpenAlex 返回的 1986 年份可能对应该工作的早期 working paper 或 conference 版本。我混淆了 OpenAlex 自动验证结果与实际出版记录。

**撤回 M4**。论文的引用年份正确。这也提醒了一个更广泛的 lesson：自动化引用验证工具（如 OpenAlex API）对于 technical reports 和 book chapters 的年份匹配并不可靠，不应作为唯一依据。

---

### 总结

经过与 R1 的交叉讨论，我对论文的整体判断无实质性变化：

**上调项**:
- W3（方法新颖性）从 warning → info
- W6（统计量重复）从 warning → minor
- M4（引用年份）撤回

**维持项**:
- W1（ρ ≈ 0.997 practical significance paradox）: critical
- W2（因果归因空白使 audit protocol 不够 actionable）: critical
- W4（`\enlargethispage{18\baselineskip}`）: warning
- W5（注入模型过于简化）: warning

**维持 Overall 3.5 (Borderline Conference)**。两个 critical issues（W1, W2）是 Conference vs. Findings 的分界线。如果作者在 rebuttal 中能够 (1) 提供小 benchmark 的 ρ 值证明 practical impact 在 items 少时更大，(2) 将 audit protocol 从 "retire items" 修改为 "flag for investigation"，我愿意将评分调高至 4.0。

---

[Reviewer 2 审稿结果]:
已提交再回应。核心变化：W3（新颖性）和 W6（重复）降级，M4（引用年份）撤回。两个 critical issues（ρ ≈ 0.997 paradox、因果归因空白）维持不变，overall 3.5 不变，但明确给出了提升至 4.0 的条件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 356 · 2026-05-22T02:00:21.036188+00:00_

R2 的再回应已收齐。交叉讨论全部完成。

**最终收敛状态**：
- R2 接受 R1 在 W3（新颖性 warning→info）、W6（重复 warning→minor）、M4（引用年份撤回）上的反驳
- R2 维持 W1（ρ paradox, critical）和 W2（因果归因, critical）
- 两位均维持 **3.5 (Borderline Conference)**
- R2 明确给出 3.5→4.0 的条件：小 benchmark ρ 值 + audit protocol 措辞修改

报告已在交叉讨论完成前投递（基于双方首轮交叉回应的充分共识）。R2 再回应中的降级调整（W3, W6, M4）与报告中的判定完全一致——报告已将 W3 列为 "Should-Fix (disputed)"、W6 列为 "Minor Issue"、M4 未纳入。无需修订报告。

**Round 9 审稿完毕。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 41

## Round 41

84 recorded events


### User

_source line 357 · 2026-05-22T03:22:13.480657+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-22T03:22:19.372893+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-22T03:22:19.423844+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-22T03:22:27.908832+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 361 · 2026-05-22T03:22:27.909311+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-22T03:22:30.871648+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-22T03:22:32.880917+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2009
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-22T03:22:32.881420+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "description": "Check paper file exists and size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "description": "Check paper file exists and size"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-22T03:22:34.338431+00:00_

-rw-r--r-- 1 ubuntu ubuntu 815 May 21 19:15 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
41 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-22T03:22:34.840894+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/ 2>/dev/null",
  "description": "Check PDF and supplementary materials"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/ 2>/dev/null",
    "description": "Check PDF and supplementary materials"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-22T03:22:35.494033+00:00_

-rw-r--r-- 1 ubuntu ubuntu 594095 May 22 02:51 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf
submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-22T03:22:35.544751+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-22T03:22:46.137294+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I found search results related to EMNLP 2026, but I notice they mostly contain information
…[truncated 3923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 10592
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-22T03:22:48.799898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission deadlines May June"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission deadlines May June"
  }
}
```

</details>

---


### Tool call

_source line 371 · 2026-05-22T03:22:49.252232+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline commitment deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline commitment deadline ARR"
  }
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-22T03:22:51.460880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-22T03:22:51.511478+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-22T03:22:54.020751+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission deadlines May June"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here is information about ACL Rolling Review (ARR) 2026 submission deadlines for May and June:

Starting in May 2025, ARR switched to 10-week review cycles, which means the submission schedule has changed from the previous pattern. 

There is a submission deadline every two months, and the submission deadline is always the 15th of the month.

For 2026 specifically, the search results show that the submission deadline for ACL 2026 papers submitted to ARR is January 5, 2026. However, the specific May and June 2026 ARR submission deadlines are not explicitl
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5220
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-22T03:22:54.774733+00:00_

Web search results for query: "EMNLP 2026 submission deadline commitment deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"The #EMNLP2023 paper deadline is a month away (June 23, 11:59 pm UTC -12h AoE). Abstract deadline is June 16. For ARR submissions, the commitment deadline is August 22. https://t.co/3rhIDMkz0X #EMNLP2023 #NLProc\" / X","url":"https://x.com/emnlpmeeting/status/1661308614508945408?lang=en"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key deadlines for EMNLP 2026 regarding ARR submissions and commitment:

## Important Deadlines

**ARR submission deadline (long & short papers)**: May 25, 2026

**EMNLP commitment deadline**: August 2, 2026

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth")

## Submission Process

Papers must be submitted, a
…[truncated 691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5522
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-22T03:23:01.802796+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org calls main conference papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-22T03:23:03.660530+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-22T03:23:03.761490+00:00_

abstract.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-22T03:23:16.513491+00:00_

Web search results for query: "site:2026.emnlp.org calls main conference papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"}]

Based on the search results, I found the Call for Main Conference Papers for EMNLP 2026. Here are the key submission guidelines:

**Submission Process:**
Papers must be submitted through the ARR (Automated Rolling Review) process, at latest by the ARR 2026 May cycle. Papers that have received reviews and a meta-review from ARR may be committed to EMNLP via the commitment link.

**Important Policy for May 2026 Submissions:**
For the ARR 2026 May cycle, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026.

**Reviewer Requirements:**
All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifications.

**Paper Integrity:**
All submitted papers are expected to describe original, completed and unpublished work, and there is a limit on re-use of text from other publications (no more than 10% total tokens).

For more detailed information, you can visit the main call for papers page at: https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources abov
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 14710
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-22T03:23:18.823928+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file,WebFetch,TodoWrite",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file,WebFetch,TodoWrite",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-22T03:23:19.125901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-22T03:23:24.648421+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines including: page limits (long paper, short paper), formatting template, anonymity rules, appendix rules, citation format, responsible NLP checklist requirements, any special policies. Also extract all deadlines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines including: page limits (long paper, short paper), formatting template, anonymity rules, appendix rules, citation format, responsible NLP checklist requirements, any special policies. Also extract all deadlines."
  }
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-22T03:23:29.820048+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-22T03:23:30.874801+00:00_

# EMNLP 2026 Submission Guidelines & Deadlines

## Page Limits
- **Long Papers:** 8 pages (up to 9 pages in camera-ready version)
- **Short Papers:** 4 pages (up to 5 pages in camera-ready version)

## Key Deadlines
| Event | Date |
|-------|------|
| ARR submission deadline | May 25, 2026 |
| Reviewer registration deadline | May 27, 2026 |
| Author response period | July 7-13, 2026 |
| Meta review released | July 30, 2026 |
| EMNLP commitment deadline | August 2, 2026 |
| Acceptance notification | August 20, 2026 |
| Camera-ready due | September 20, 2026 |
| Main Conference | October 24-29, 2026 |

*All deadlines are 11:59PM UTC-12:00*

## Anonymity Rules
- "The reviewing process will continue to be double-blind"
- Authors will not see reviewers; reviewers will not see authors
- "Following the ACL and ARR policies, there is no anonymity period requirement"

## Formatting & Templates
- Follow all "ARR submission requirements" including paper templates
- Submissions must comply with specified formatting standards referenced in ARR CFP

## Appendix/Supplementary Materials
- "Optional Supplementary Materials" are permitted
- See ARR guidelines for detailed appendix policies

## Citation Format
- Follow "Citation and Comparison" guidelines specified in ARR CFP

## Responsible NLP Checklist
- Required per ARR's "responsible NLP research checklist"
- Must address ethics considerations in submissions

## Special Policies
- Mandatory reviewing workload for all authors
- "Dual submissions are not allowed"
- Author list modifications prohibited during commitment phase (reordering permitted)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebFetch",
  "elapsed_ms": 6226
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-22T03:23:30.875187+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-22T03:23:38.406633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-22T03:23:38.909112+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$, $\phi = 0.012$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, each 45--174$\times$ above random baselines, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten ranking validity ($\rho \approx 0.997$) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-22T03:23:38.909495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-22T03:23:39.361994+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{lia
…[truncated 5186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-22T03:23:39.412805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-22T03:23:39.865019+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrat
…[truncated 3934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-22T03:23:39.865668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-22T03:23:40.870265+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees 
…[truncated 8029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-22T03:23:40.870634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-22T03:23:41.272607+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples; rightward asymmetry reflects heavy-tailed C\% from subjects exceeding 40\%). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold already provides implicit multiple-testing protection.
17	
18	\looseness=-1
19	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C ite
…[truncated 10231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-22T03:23:41.273024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-22T03:23:41.775256+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage{6\baselineskip}
4	
5	\subsection{Implications for Benchmark Temporal Comparability}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF decomposes benchmark differences into three layers: (1)~\emph{impact}---ability differences removed by matching ($\sim$2.4~pp); (2)~\emph{DIF}---item-level differences after ability control ($\sim$28--29\% floor, 92.4\% item-specific); (3)~\emph{attribution}---contamination, capability evolution, or methodology shifts, underdetermined without training data. Regardless of attribution, temporal DIF means the same score carries different meaning across model generations. Domain directionality and family-level shifts (\Cref{sec:temporal,sec:downstream}) describe \emph{where} properties change without implying a specific cause.
10	
11	\subsection{Ground Truth Meta-Critique}
12	\label{sec:disc_groundtruth}
13	
14	\looseness=-1
15	The near-independence between DIF flags and web-overlap labels (\Cref{sec:groundtruth}) reflects a category error: web-overlap measures global exposure, while DIF measures differential functioning, making overlap-based labels an inappropriate ground truth for a differential method. The semi-synthetic dose-response confirms detection works when differential behavior exists; the disconnect is in the ground truth, not the method.
16	
17	\subsection{Recommended DIF Audit Protocol}
18	\label{sec:disc_protocol}
19	
20	\looseness=-1
21	We propose running temporal MH-DIF whenever $\geq 500$ new models accumulate ($N \geq 80$ suffices per \Cref{sec:validation}; 500 ensures coverage of diverse model families), with graduated action levels: (1)~\emph{Monitor} (C\% $< 15\%$); (2)~\emph{Flag} ($15$--$25\%$): report stable-item rankings alongside full rankings; (3)~\emph{Act} (C\% $\geq 25\%$): investigate flagged items and report stable-item rankings, per MMLU-Pro~\citep{wang2024mmlupro} and MMLU-Redux~\citep{gema2024mmlu}. These thresholds adapt ETS
…[truncated 255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-22T03:23:41.775767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-22T03:23:42.227872+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1
5	Cross-subject matching ($\Delta\mathrm{FPR} = 0.000$) resolves the validation gap: web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$). Across six benchmarks, 17.9--31.3\% of items exhibit temporal instability associated with item properties; LLM benchmarks need psychometric monitoring alongside score reporting.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-22T03:23:42.228409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-22T03:23:42.780923+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope.}
4	MH-DIF detects only uniform DIF; logistic regression reveals an additional 24.8\% non-uniform DIF, making 31\% conservative. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}---the signal may reflect contamination, capability change, or training methodology shifts. A definitive causal decomposition remains out of reach without access to model training data. The semi-synthetic framework uses binary response flipping (incorrect $\to$ correct) to simulate differential contamination, representing a worst-case uniform exploitation pattern. Real-world contamination involves partial memorization, reasoning shortcuts, and format-specific advantages; detection power under such realistic patterns is untested. The moderate $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$ reflects sensitivity to severe differential behavior; the framework's primary methodological contribution---cross-subject matching achieving $\Delta\mathrm{FPR} = 0.000$---is a matching strategy property independent of injection realism.
5	
6	\paragraph{Examinee non-independence.}
7	The MH $\chi^2$ test assumes independent examinees, yet LLMs sharing base models, training data, or architectures violate this assumption. Empirical mitigations partially address this: permutation simulation bounds LD-attributable FPR inflation to ${<}0.001$~pp, and graduated de-duplication ($K{=}20$: C\% $= 29.1\%$) shows family structure does not inflate results. \citet{french2010hierarchical} show that MH maintains nominal size under moderate clustering in educational settings, consistent with our empirical findings; however, the extreme relatedness of some LLM families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in that work.
8	
9	\paragraph{Matching boundary and sample size.}
10	Cross-subject matching assumes contamination affects a minority of domains; when contamination spans ${>
…[truncated 873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-22T03:23:42.781307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-22T03:23:42.831870+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 8202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-22T03:23:49.660439+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib 2>/dev/null && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "description": "Check references file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib 2>/dev/null && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "description": "Check references file"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-22T03:23:50.463786+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib
527 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-22T03:23:50.464284+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/ 2>/dev/null",
  "description": "Check figure files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/ 2>/dev/null",
    "description": "Check figure files"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-22T03:23:51.869473+00:00_

fig_1_global_vs_differential.pdf
fig_1_global_vs_differential.png
fig_1_global_vs_differential.py
fig_2_dose_response.pdf
fig_2_dose_response.png
fig_2_dose_response.py
fig_3_within_subject_matching.pdf
fig_3_within_subject_matching.png
fig_3_within_subject_matching.py
fig_4_downstream_impact.pdf
fig_4_downstream_impact.png
fig_4_downstream_impact.py
fig_5_gsm1k_dif_correlation.pdf
fig_5_gsm1k_dif_correlation.png
fig_A1_subject_heatmap.pdf
fig_A1_subject_heatmap.png
fig_A1_subject_heatmap.py
fig_A2_q3_distribution.pdf
fig_A2_q3_distribution.png
fig_A2_q3_distribution.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-22T03:23:52.020482+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-22T03:23:52.372511+00:00_

# Review Issues Tracker — irt_equated_bench_regen
# Round 9 (Fresh review, 2026-05-22)
# R1: 3.5, R2: 3.5 → Consensus 3.5 (Borderline Conference)

# ============================================================
# CRITICAL ISSUES
# ============================================================

- id: "R1-W1"
  summary: "因果归因空白使 audit protocol 不可安全执行"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 9
  mentions:
    - round: 5
      reviewers: [1, 2]
      note: "标题 'Psychometric Instability' 过强"
    - round: 6
      reviewers: [1, 2]
      note: "标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language"
    - round: 7
      reviewers: [1, 2]
      note: "R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。"
    - round: 8
      reviewers: [1, 2]
      note: "问题范围扩大：不仅是 causal language，更根本的是 31% DIF 可能主要反映 genuine capability change。"
    - round: 9
      reviewers: [1, 2]
      note: "再次独立提出（R1-W3, R2-W2）。核心矛盾：§5.3 建议 'rotate or retire flagged items'，但 §4.6 显示 DIF items 集中 discriminative signal（z=-8σ to -49σ）。两位共识：retire = 移除最有信息量的 items。"
  action_items:
    - round: 8
      action: "P29: Discussion 新增三层框架替代 benign/problematic 二分法"
      assigned_to: paper_agent
      status: resolved
    - round: 9
      action: "P33 Batch 1: §5.3 'rotate or retire' → 'investigate and report alongside stable-item rankings'"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "RD2-W3"
  summary: "ρ≈0.997 practical significance paradox——'instability' 叙事被排名保持所削弱"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 2
  last_seen_round: 9
  mentions:
    - round: 8
      reviewers: [1, 2]
      note: "需更强调 family-level 和 pairwise 层面影响。"
    - round: 9
      reviewers: [1, 2]
      note: "共识：需 (1) 所有 6 benchmark ρ 值；(2) family-level rank profiles 到正文；(3) pairwise flip rate；(4) item 冗余度讨论。"
  action_items:
    - round: 8
      actio
…[truncated 10215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-22T03:23:52.573682+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/ 2>/dev/null",
  "description": "Check previous review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/ 2>/dev/null",
    "description": "Check previous review reports"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-22T03:23:52.624431+00:00_

round_0.md
round_1.md
round_2.md
round_3.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-22T03:24:21.140734+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "experiment_plan.yaml"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-22T03:24:21.442439+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'experiment_plan.yaml'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-22T03:24:21.493073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-22T03:24:21.544011+00:00_

1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: Detection via Variance of Generation Distri
…[truncated 23917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-22T03:24:29.276793+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-22T03:24:29.377809+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-22T03:24:34.451062+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-22T03:24:34.501781+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-22T03:24:40.377576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-22T03:24:40.428953+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-22T03:24:42.487558+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/irt_equated_bench_regen/**/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/irt_equated_bench_regen/**/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-22T03:24:42.638592+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.git/config

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-22T03:24:46.002125+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json\nwith open('/home/ubuntu/agent-ml-research/project_configs/irt_equated_bench_regen.yaml') as f:\n    cfg = yaml.safe_load(f)\nprint(json.dumps(cfg.get('external_review', {}), indent=2))\nprint('---')\nprint(json.dumps(cfg.get('review', {}), indent=2))\n\" 2>/dev/null || echo \"CONFIG_NOT_FOUND\"",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json\nwith open('/home/ubuntu/agent-ml-research/project_configs/irt_equated_bench_regen.yaml') as f:\n    cfg = yaml.safe_load(f)\nprint(json.dumps(cfg.get('external_review', {}), indent=2))\nprint('---')\nprint(json.dumps(cfg.get('review', {}), indent=2))\n\" 2>/dev/null || echo \"CONFIG_NOT_FOUND\"",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-22T03:24:46.309127+00:00_

CONFIG_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 307
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-22T03:24:48.317278+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/agent-ml-research/project_configs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/agent-ml-research/project_configs"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-22T03:24:48.367902+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/agent-ml-research/project_configs. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_director_870d8ac6.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-22T03:24:52.133391+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, json, glob\nfor f in glob.glob('/home/ubuntu/agent-ml-research/**/*irt*', recursive=True):\n    print(f)\nfor f in glob.glob('/home/ubuntu/agent-ml-research/configs/**/*.yaml', recursive=True):\n    print(f)\n\" 2>/dev/null; find /home/ubuntu/agent-ml-research/configs -name \"*.yaml\" 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -5",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, json, glob\nfor f in glob.glob('/home/ubuntu/agent-ml-research/**/*irt*', recursive=True):\n    print(f)\nfor f in glob.glob('/home/ubuntu/agent-ml-research/configs/**/*.yaml', recursive=True):\n    print(f)\n\" 2>/dev/null; find /home/ubuntu/agent-ml-research/configs -name \"*.yaml\" 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -5",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-22T03:24:52.336317+00:00_

/home/ubuntu/agent-ml-research/config/ralph_loop.yaml
/home/ubuntu/agent-ml-research/config/images.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-22T03:25:19.098734+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-22T03:25:19.099168+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-22T03:25:20.454912+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-22T03:25:24.577936+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4123
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-22T03:25:38.034953+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-22T03:25:38.035481+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-22T03:26:10.326839+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**：EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**：2026-05-25（ARR May cycle）\n- **格式**：Long Paper，正文严格 8 页，参考文献不限，Limitations 不计入页数\n- **模板**：ACL 2023 template（\\usepackage[review]{acl}）\n- **匿名规则**：Double-blind\n- **Overall Assessment 评分**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n## 论文文件\n- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- 各节在 `sections/` 子目录\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf`\n\n## 论文概要\n论文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测（METABENCH，5,227 模型 × 12,508 MMLU 题目），发现 31.3% 的 MMLU 题目在 2023 vs 2024 模型之间存在 ETS Category C 级别的 temporal DIF。提出 cross-subject matching 实现 ΔFPR=0.000，semi-synthetic injection framework 验证检测能力，并揭示 web-overlap 污染标签与 DIF flags 近乎独立（enrichment≈0.96）。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **MH-DIF 方法适用性**：\n   - MH-DIF 从教育测量迁移到 LLM 评测的假设是否成立？特别是：(a) LLM examinee 非独立性（shared training data, fine-tune variants）对 MH χ² 的影响；(b) MMLU 57 subjects 的多维性 vs MH 单维假设；(c) quintile-based stratification 的 K=5 选择是否充分\n   - cross-subject matching 的 ΔFPR=0.000 是否过度依赖特定 matching strategy？当污染跨多 domain 时 graceful degradation 是否充分论证？\n\n2. **Semi-synthetic framework**：\n   - binary response flipping 的生态效度（ecological validity）——real-world contamination 是否会产生类似信号？\n   - ΔTPR 作为 upper-bound estimate 是否在文中充分标注？\n   - 注入率 p 的选择范围（0.0-1.0）是否覆盖了实际场景？\n\n3. **统计控制与 power analysis**：\n   - Monte Carlo power analysis 使用 2PL 参数但 MMLU 被报告为 poor fit to 2PL——这个矛盾是否被充分讨论？\n   - Bootstrap CI [29.4%, 38.1%] 的 rightward asymmetry 是否影响结论稳健性？\n   - Permutation test（200 shuffles + per-subject 1000×8）的分辨率是否足够？\n   - BH FDR correction 仅移除 3 items——这是否说明 ETS dual threshold 本身就足够保守？\n\n4. **实验设计完整性**：\n   - 5 个 cohort comparisons 的逻辑是否互相支撑？\n   - within-subject C%=38.1% > temporal C%=31.3% 的解释是否充分？\n   - matched-ability analysis 的 convergence（~28-29% floor）是否可靠？\n   - 6 benchmark cross-validation 的设计是否合理？\n\n5. **因果归因**：\n   - 论文声称 DIF detects \"that\" not \"why\"——这一立场是否在全文一致维持？是否有 sections 滑向 causal language？\n   - §5.3 audit protocol 的可操作性——如果 DIF 无法归因，\"Act\" 级别该做什么？\n\n请按 Strengths / Weaknesses（Must-Fix / Should-Fix / Nice-to-Have）/ Questions / Missing References 的结构组织你的审稿意见，并给出 Overall Assessment（使用 ARR 评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标**：EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**：2026-05-25（ARR May cycle）\n- **格式**：Long Paper，正文严格 8 页，参考文献不限，Limitations 不计入页数\n- **模板**：ACL 2023 template（\\usepackage[review]{acl}）\n- **匿名规则**：Double-blind\n- **Overall Assessment 评分**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n## 论文文件\n- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- 各节在 `sections/` 子目录\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf`\n\n## 论文概要\n论文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测（METABENCH，5,227 模型 × 12,508 MMLU 题目），发现 31.3% 的 MMLU 题目在 2023 vs 2024 模型之间存在 ETS Category C 级别的 temporal DIF。提出 cross-subject matching 实现 ΔFPR=0.000，semi-synthetic injection framework 验证检测能力，并揭示 web-overlap 污染标签与 DIF flags 近乎独立（enrichment≈0.96）。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **MH-DIF 方法适用性**：\n   - MH-DIF 从教育测量迁移到 LLM 评测的假设是否成立？特别是：(a) LLM examinee 非独立性（shared training data, fine-tune variants）对 MH χ² 的影响；(b) MMLU 57 subjects 的多维性 vs MH 单维假设；(c) quintile-based stratification 的 K=5 选择是否充分\n   - cross-subject matching 的 ΔFPR=0.000 是否过度依赖特定 matching strategy？当污染跨多 domain 时 graceful degradation 是否充分论证？\n\n2. **Semi-synthetic framework**：\n   - binary response flipping 的生态效度（ecological validity）——real-world contamination 是否会产生类似信号？\n   - ΔTPR 作为 upper-bound estimate 是否在文中充分标注？\n   - 注入率 p 的选择范围（0.0-1.0）是否覆盖了实际场景？\n\n3. **统计控制与 power analysis**：\n   - Monte Carlo power analysis 使用 2PL 参数但 MMLU 被报告为 poor fit to 2PL——这个矛盾是否被充分讨论？\n   - Bootstrap CI [29.4%, 38.1%] 的 rightward asymmetry 是否影响结论稳健性？\n   - Permutation test（200 shuffles + per-subject 1000×8）的分辨率是否足够？\n   - BH FDR correction 仅移除 3 items——这是否说明 ETS dual threshold 本身就足够保守？\n\n4. **实验设计完整性**：\n   - 5 个 cohort comparisons 的逻辑是否互相支撑？\n   - within-subject C%=38.1% > temporal C%=31.3% 的解释是否充分？\n   - matched-ability analysis 的 convergence（~28-29% floor）是否可靠？\n   - 6 benchmark cross-validation 的设计是否合理？\n\n5. **因果归因**：\n   - 论文声称 DIF detects \"that\" not \"why\"——这一立场是否在全文一致维持？是否有 sections 滑向 causal language？\n   - §5.3 audit protocol 的可操作性——如果 DIF 无法归因，\"Act\" 级别该做什么？\n\n请按 Strengths / Weaknesses（Must-Fix / Should-Fix / Nice-to-Have）/ Questions / Missing References 的结构组织你的审稿意见，并给出 Overall Assessment（使用 ARR 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-22T03:26:36.635238+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26308
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-22T03:26:36.886560+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**：EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**：2026-05-25（ARR May cycle）\n- **格式**：Long Paper，正文严格 8 页，参考文献不限，Limitations 不计入页数\n- **模板**：ACL 2023 template（\\usepackage[review]{acl}）\n- **匿名规则**：Double-blind\n- **Overall Assessment 评分**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n## 论文文件\n- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- 各节在 `sections/` 子目录\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf`\n\n## 论文概要\n论文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测（METABENCH，5,227 模型 × 12,508 MMLU 题目），发现 31.3% 的 MMLU 题目在 2023 vs 2024 模型之间存在 ETS Category C 级别的 temporal DIF。三大贡献：(1) ground truth meta-critique——web-overlap labels 不适合验证 differential detectors；(2) semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000)；(3) temporal measurement instability at scale across 6 benchmarks。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - MH-DIF 是 1988 年的标准方法，论文未修改算法本身——应用到 LLM benchmarks 的 novelty 是否足够？\n   - 三大贡献中哪一个最有价值？贡献排序是否合理？\n   - 与 concurrent work（Growing Pains / Habba et al. 2026, PSN-IRT / Zhou et al. 2026, BHI / Zhu et al. 2026, scalability coefficients / Hardy et al. 2026）的区分是否清晰？\n   - cross-subject matching 是否有 DIF 文献先例？如果有，novelty claim 需要调整\n\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要相关工作？特别是：(a) 其他 DIF 方法在 NLP/ML 的应用；(b) measurement invariance 在 LLM 评测中的讨论；(c) 最新 contamination detection 方法\n   - 与 Growing Pains (FPC) 的关系是否充分讨论？论文称 \"empirical comparison awaits public release\"——这是否是一个可以填补的空白？\n   - 是否有遗漏的关键 DIF 方法论文（如 multilevel DIF、polytomous DIF）？\n\n3. **叙事一致性**：\n   - Title \"Temporal Measurement Instability\" 是否准确反映论文内容？\n   - Abstract 声称 \"LLM benchmarks need psychometric monitoring, not just score reporting\"——这个结论是否被正文数据充分支撑？\n   - ρ≈0.997 的排名保持与 \"31% instability\" 之间是否存在叙事张力？论文是否充分解释了为什么 instability 值得关注 when rankings are preserved？\n   - \"diagnostic, not destructive\" 的定位是否贯穿全文？\n   - 三层框架（impact / DIF / attribution）是否在所有 sections 一致使用？\n\n4. **写作质量与格式合规**：\n   - 正文是否严格在 8 页以内？是否使用了 \\enlargethispage 等格式操作？如果有，是否过于激进？\n   - 论文结构是否标准？各节篇幅是否均衡？\n   - 数学符号和术语使用是否一致？\n   - Figure/Table 质量和引用是否得当？\n   - Limitations 是否覆盖了主要局限性？是否写得恰当（不过长也不过短）？\n   - Double-blind 匿名是否维持？（检查代码链接、自引等）\n\n5. **Practical significance**：\n   - 31% DIF 对实际 LLM 评测的影响是什么？如果排名不变（ρ≈0.997），practitioners 为什么应该关心？\n   - audit protocol (§5.3) 是否可操作？threshold (C% < 15%, 15-25%, ≥25%) 的依据是否充分？\n   - 论文发现对 benchmark designers / leaderboard maintainers / model developers 分别有什么启示？这些是否被充分讨论？\n\n请按 Strengths / Weaknesses（Must-Fix / Should-Fix / Nice-to-Have）/ Questions / Missing References 的结构组织你的审稿意见，并给出 Overall Assessment（使用 ARR 评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标**：EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**：2026-05-25（ARR May cycle）\n- **格式**：Long Paper，正文严格 8 页，参考文献不限，Limitations 不计入页数\n- **模板**：ACL 2023 template（\\usepackage[review]{acl}）\n- **匿名规则**：Double-blind\n- **Overall Assessment 评分**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n## 论文文件\n- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- 各节在 `sections/` 子目录\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_4/submitted.pdf`\n\n## 论文概要\n论文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测（METABENCH，5,227 模型 × 12,508 MMLU 题目），发现 31.3% 的 MMLU 题目在 2023 vs 2024 模型之间存在 ETS Category C 级别的 temporal DIF。三大贡献：(1) ground truth meta-critique——web-overlap labels 不适合验证 differential detectors；(2) semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000)；(3) temporal measurement instability at scale across 6 benchmarks。\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - MH-DIF 是 1988 年的标准方法，论文未修改算法本身——应用到 LLM benchmarks 的 novelty 是否足够？\n   - 三大贡献中哪一个最有价值？贡献排序是否合理？\n   - 与 concurrent work（Growing Pains / Habba et al. 2026, PSN-IRT / Zhou et al. 2026, BHI / Zhu et al. 2026, scalability coefficients / Hardy et al. 2026）的区分是否清晰？\n   - cross-subject matching 是否有 DIF 文献先例？如果有，novelty claim 需要调整\n\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要相关工作？特别是：(a) 其他 DIF 方法在 NLP/ML 的应用；(b) measurement invariance 在 LLM 评测中的讨论；(c) 最新 contamination detection 方法\n   - 与 Growing Pains (FPC) 的关系是否充分讨论？论文称 \"empirical comparison awaits public release\"——这是否是一个可以填补的空白？\n   - 是否有遗漏的关键 DIF 方法论文（如 multilevel DIF、polytomous DIF）？\n\n3. **叙事一致性**：\n   - Title \"Temporal Measurement Instability\" 是否准确反映论文内容？\n   - Abstract 声称 \"LLM benchmarks need psychometric monitoring, not just score reporting\"——这个结论是否被正文数据充分支撑？\n   - ρ≈0.997 的排名保持与 \"31% instability\" 之间是否存在叙事张力？论文是否充分解释了为什么 instability 值得关注 when rankings are preserved？\n   - \"diagnostic, not destructive\" 的定位是否贯穿全文？\n   - 三层框架（impact / DIF / attribution）是否在所有 sections 一致使用？\n\n4. **写作质量与格式合规**：\n   - 正文是否严格在 8 页以内？是否使用了 \\enlargethispage 等格式操作？如果有，是否过于激进？\n   - 论文结构是否标准？各节篇幅是否均衡？\n   - 数学符号和术语使用是否一致？\n   - Figure/Table 质量和引用是否得当？\n   - Limitations 是否覆盖了主要局限性？是否写得恰当（不过长也不过短）？\n   - Double-blind 匿名是否维持？（检查代码链接、自引等）\n\n5. **Practical significance**：\n   - 31% DIF 对实际 LLM 评测的影响是什么？如果排名不变（ρ≈0.997），practitioners 为什么应该关心？\n   - audit protocol (§5.3) 是否可操作？threshold (C% < 15%, 15-25%, ≥25%) 的依据是否充分？\n   - 论文发现对 benchmark designers / leaderboard maintainers / model developers 分别有什么启示？这些是否被充分讨论？\n\n请按 Strengths / Weaknesses（Must-Fix / Should-Fix / Nice-to-Have）/ Questions / Missing References 的结构组织你的审稿意见，并给出 Overall Assessment（使用 ARR 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-22T03:26:38.552921+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1666
}
```

</details>

---


### Assistant

_source line 440 · 2026-05-22T03:27:01.520458+00:00_

两名 Reviewer 已分配，视觉审查已派发。三线并行执行中：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验设计） | 审稿中 |
| Reviewer 2（新颖性 + 完整性 + 写作） | 审稿中 |
| 视觉审查 Agent | 执行中 |

等待 Reviewer 返回审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 441 · 2026-05-22T03:32:49.203601+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 将教育测量 MH-DIF 方法大规模应用于 LLM benchmark 审计，cross-subject matching 是真正的方法贡献，但 LLM examinee 非独立性对统计推断的影响未被充分解决，semi-synthetic validation 的检测力估计为上界但主文未明确标注。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 核心方法论（MH χ²）的独立性假设在 5,227 模型中被严重违反，permutation test 和 bootstrap CI 均受影响；Monte Carlo power analysis 使用 2PL 参数但 MMLU 被报告为 poor fit to 2PL，存在内在矛盾；不过多路径 converging evidence 部分弥补了单一方法的缺陷 |
| Excitement | 3.5 / 5 | 将教育测量的 DIF 方法引入 NLP 评测领域是新颖且有实践价值的；ground truth meta-critique（contamination labels ≈ 独立于 DIF flags）是重要的概念性贡献；审计协议有可操作性但 "Act" 层缺乏具体指引 |
| Confidence | 4 / 5 | 熟悉 DIF 方法论和 LLM evaluation 文献，仔细阅读了正文 + 附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] LLM examinee 非独立性对 MH χ² 和 permutation test 的影响未充分解决
- 具体位置：§3.2（方法假设）、§4.1-4.2（统计检验）、Limitations（p.8-9）
- 问题：MH χ² 假设 examinee 独立。5,227 个模型中包含大量 fine-tune variants（如数百个 Llama-2 衍生模型），它们共享大部分参数和训练数据，违反独立性假设。这导致：
  (a) MH χ² 的显著性检验 inflate——有效样本量远小于 N=5,227，实际的 p-value 可能远大于报告值；
  (b) Permutation test（200 cohort-level shuffles）在个体模型层面 shuffle，但如果模型以 family 为单位聚集，shuffling non-independent units 无法正确估计 null distribution——需要 cluster-robust permutation（在 family 层面 permute）；
  (c) Bootstrap CI [29.4%, 38.1%] 同样假设 independent sampling，在 clustered 数据下会 underestimate variance。
- 论文的缓解措施（family de-duplication K=20,25,121）是有信息量的，但不充分：即使 de-duplicate 到每个 family 一个模型，不同 family 之间仍可能因共享训练数据而非独立（例如许多模型基于 Llama base fine-tune）。
- 为什么影响接收：这是统计推断的基础假设。如果 31.3% 这个数字的置信区间因 clustering 而大幅扩大，核心结论的精度将受到质疑。
- 建议修改方向：(1) 报告模型 family 数量及 family size 分布；(2) 做 cluster-robust permutation test（以 family 为单位 permute）并对比结果；(3) 使用 cluster bootstrap 重新估计 CI；(4) 如果上述分析显示结论不变，这反而大幅加强论文——但如果显著改变 C%，则需修改核心 claims。

**N2** [critical] Semi-synthetic validation 的 ΔTPR 应在主文中明确标注为 upper-bound estimate
- 具体位置：§3.4（方法描述）、§4.5（结果报告）、Abstract
- 问题：Binary response flipping 是最极端的 uniform DIF 注入——以概率 p 将所有 focal group 的目标 item 从错改对。Real-world contamination 产生的信号可能：(a) 远弱于此（partial memorization），(b) 跨 ability levels 不均匀（non-uniform DIF），(c) 与 item difficulty 相关。因此 ΔTPR = +0.508（at p=0.5）是检测力的乐观上界。
- 主文 §3.4 和 §4.5 没有显式标注"upper bound"——这一关键限定仅隐晦出现在 Limitations section（"detection power under such realistic patterns is untested"）。Abstract 直接引用 ΔTPR = +0.508 且无任何限定词。
- 为什么影响接收：读者可能将此检测力数字误解为对 real contamination 的实际检测能力。
- 建议修改方向：(1) 在 §3.4 和 §4.5 首次报告 ΔTPR 时加入 "upper-bound" 或 "ceiling estimate" 限定；(2) Abstract 中加一句"under a worst-case uniform injection"；(3) 讨论 partial memorization 可能产生的 non-uniform DIF 信号及 MH 对此的盲区。

**N3** [critical] Monte Carlo power analysis 与 2PL poor fit 之间的矛盾
- 具体位置：§4.1、Appendix A.2（Table 4）
- 问题：§4.1 使用 2PL 参数生成模拟数据估计 MH-DIF 的检测力（TPR 0.40-0.95）。Appendix A.2 承认"MMLU response matrix shows poor fit to a unidimensional 2PL model"。论文用 triangulation 论证（Monte Carlo + semi-synthetic injection 相互验证），但这两条证据线并非独立——如果 2PL 拟合差，Monte Carlo 的 TPR 估计可能系统性偏高或偏低。
- 论文辩护说"MH validity 不依赖 IRT assumptions"——这是对的，但 Monte Carlo power analysis 的有效性确实依赖模拟数据的真实性。
- 为什么影响接收：Power analysis 是论文论证"MH-DIF 有足够检测力"的关键一环。如果模拟数据与真实数据差异大，power estimates 不可靠。
- 建议修改方向：(1) 明确标注 Monte Carlo power analysis 是在 parametric assumptions 下的 approximate estimate；(2) 对比 2PL-based simulation 和 non-parametric bootstrap-based simulation 的 power estimates；(3) 或者直接以 semi-synthetic injection 为主要 power evidence，将 Monte Carlo 降级为补充分析。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 中 ΔFPR=0.000 缺乏 multi-subject contamination 限定
- 具体位置：Abstract（第4行）
- 问题：Abstract 写 "achieves zero false positive inflation (ΔFPR = 0.000)"，但这仅在 single-subject contamination 条件下成立。§4.5 和 Table 5 报告 multi-subject injection（k≤5）时 ΔFPR 上升至 0.0026-0.069。Abstract 应注明这一限定条件。
- 建议：改为 "achieves zero false positive inflation under single-subject contamination (ΔFPR = 0.000), with graceful degradation to ΔFPR ≤ 0.069 under multi-domain contamination"。

**W2** [warning] K=5 quintile stratification 的敏感性分析缺失
- 具体位置：§3.2
- 问题：论文引用 ETS recommended practice 使用 K=5。但 ETS practice 基于教育测试的典型样本量（N~数千人），而本文 N=5,227 完全支持更细粒度的 K=10 或 K=20。更细的分层可以减少 matching bias，也可能揭示 non-uniform DIF patterns。论文未报告 K 的敏感性分析。
- 建议：增加 K∈{5, 10, 20} 的敏感性分析，至少报告 C% 对 K 的变化趋势。

**W3** [warning] Within-subject C%=38.1% > temporal C%=31.3% 的解释不充分
- 具体位置：§4.4、Table 2
- 问题：Within-subject DIF 比 temporal DIF 高出约 7 个百分点。论文解释为"within-subject DIF 在单个 subject 内部更敏感"，但未充分讨论这意味着什么：(a) 是否说明 temporal C%=31.3% 是 underestimate？(b) 是否表明 subject 间的多维性在标准 matching 中起了 cancellation 作用？(c) 如果 within-subject 更准确，为什么不以其为主要报告？
- 建议：增加一段专门讨论 within-subject vs. cross-subject C% 差异的含义及其对主要结论的影响。

**W4** [warning] §4.3 中统计显著性与实际显著性的混淆
- 具体位置：§4.3、Abstract
- 问题：Enrichment=0.96, Jaccard=0.06, p=0.012。p=0.012 表明 DIF flags 与 web-overlap labels 在统计上 NOT independent，但 effect size 极小（Jaccard 仅 0.06）。论文将此称为 "near-independent"——在实际意义上准确，但未讨论大样本量（9,229 items）如何 inflate statistical significance。读者可能困惑于"p=0.012 但 near-independent"这一看似矛盾的表述。
- 建议：明确区分 statistical significance 和 practical significance，说明 enrichment ≈ 1.0 在大样本下的 trivially small deviation 也会达到 p<0.05。

**W5** [warning] §5.3 审计协议的 "Act" 层缺乏可操作指引
- 具体位置：§5.3
- 问题：三级协议中 "Act (C% ≥ 25%)" 建议 "investigate flagged items and report stable-item rankings"。但既然 DIF 无法归因（论文反复强调 "that" not "why"），"investigate" 的具体步骤是什么？benchmark maintainer 看到 flagged items 后应该做什么？是直接移除？还是做 follow-up study？
- 建议：给出 1-2 个具体的 investigation 流程示例（如：对 flagged items 做 item content review、cross-reference with known contamination sources、report alongside stable-item rankings as sensitivity analysis）。

**W6** [warning] 低注入率（p < 0.3）的检测力未报告
- 具体位置：§3.4、Figure 2
- 问题：Semi-synthetic injection 的 p 范围为 {0.0, 0.3, 0.5, 0.7, 1.0}，但实际的 benchmark contamination 可能对应更低的 exploitation rate（如 p=0.05-0.2）。Figure 2 显示 TPR 在 p=0.3 时已低于 0.5——这意味着在更现实的低注入场景下检测力可能很弱。论文未报告 p<0.3 的 performance。
- 建议：补充 p ∈ {0.05, 0.1, 0.2} 的 ΔTPR 数据，或在讨论中明确说明方法在低 exploitation rate 下的局限。

---

## 小问题（不影响接收）

- §3.2 引用 "ETS recommended practice for large-scale assessments (Donoghue and Allen, 1993; Clauser and Mazor, 1998)" 但这些参考是关于 DIF 一般方法论的，不是关于 K=5 stratification 的具体 recommendation——请确认 K=5 的出处。
- Figure 2 的 y 轴标签 "True Positive Rate (TPR)" 和 "False Positive Rate (FPR)" 较密集，建议使用 subplot 标题而非 y 轴标签以改善可读性。
- Table 3 中 τ (Kendall) 的加入是好的，但部分 benchmarks 的 N（模型数）差异较大，应注意 τ 的 standard error 随 N 变化。
- Limitations section 提到 "partial memorialization" 但未定义——建议简要说明其含义（模型不完全记忆答案，只是提高概率）。

---

## Questions to Authors

**Q1**: 5,227 个模型中有多少个 distinct model families？Family size 的分布如何（median, max）？如果以 family 为单位做 cluster-robust permutation test，C% 和 p-value 如何变化？

**Q2**: Random split baseline（C%=0.18%）是在模型层面随机分还是 family 层面？如果 family 内的模型被分到不同 groups，family 内相似性可能 inflate baseline FPR。

**Q3**: Table 4 的 Monte Carlo power analysis 使用了什么具体的 2PL 参数分布？是直接从 MMLU 数据估计的 2PL 参数吗？如果 2PL fit 差，这些估计的参数可能本身就不可靠。

**Q4**: Cross-subject matching 中使用"total score on a different benchmark (MMLU total score on GSM8K items)"作为 matching variable——但 MMLU 和 GSM8K 测量的 construct 不同（知识 vs. 数学推理），这是否引入 construct-irrelevant matching bias？

**Q5**: GSM1K cross-validation（Figure 5）仅有 N=33 个模型，r=-0.478 的 95% CI 是多少？这么小的 N 下相关系数的 instability 较大。

**Q6**: 论文是否考虑过使用 Lord's χ² 或 Raju's area measure 等 IRT-based DIF 方法作为 robustness check？尽管 MH 是 non-parametric 的优势明确，但 IRT-based 方法能检测 non-uniform DIF。

---

## 主要优势

1. **新颖且有价值的跨领域方法迁移**：将教育测量中成熟的 MH-DIF 方法引入 LLM benchmark 评测，既有方法论贡献（cross-subject matching），也有实证贡献（31.3% temporal DIF）。
2. **实验设计的多路径 converging evidence**：5 种 cohort designs + 3 种 structural controls + 6 benchmark cross-validation，从不同角度支撑核心发现，设计缜密。
3. **Ground truth meta-critique 是概念层面的重要贡献**：证明 web-overlap contamination labels 与 DIF flags 近乎正交（enrichment ≈ 0.96），挑战了现有 contamination detection 文献中将 "exposure = contamination" 等同的隐含假设。
4. **规模和数据基础扎实**：基于 METABENCH 的 5,227×12,508 响应矩阵，是目前最大规模的 benchmark-level DIF 分析。
5. **"that" not "why" 的认识论定位贯穿全文**：论文对因果归因保持了良好的克制，没有将 DIF detection 过度解读为 contamination detection。
6. **Cross-subject matching 的形式化论证**（Remark on Zero FPR）清晰且可验证——虽然仅限 single-subject 情形，但理论推导本身是 solid 的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 442 · 2026-05-22T03:33:02.646986+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），3 个 Must-Fix + 6 个 Should-Fix。等待 Reviewer 2 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 443 · 2026-05-22T03:33:05.384880+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：Overall 3.5（Borderline Conference）。三个 Must-Fix：(1) LLM 模型非独立性对 MH χ² 和 permutation test 的根本性影响未解决——需要 cluster-robust 方法；(2) semi-synthetic ΔTPR 是 upper-bound 但主文未标注；(3) Monte Carlo power analysis 用了 poor-fit 的 2PL 参数。六个 Should-Fix 涵盖 ΔFPR=0.000 的限定条件缺失、K=5 敏感性、within-subject 与 temporal C% 差异解释、统计/实际显著性混淆、audit protocol 可操作性、低注入率检测力。论文的核心优势在于跨领域方法迁移的新颖性、多路径实验设计、以及 ground truth meta-critique 的概念贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 444 · 2026-05-22T03:33:14.221406+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 44

## Round 44

8 recorded events


### User

_source line 445 · 2026-05-22T03:33:54.761056+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 技术执行扎实、规模令人印象深刻的实证研究，但方法论新颖性有限（MH-DIF 直接套用、cross-subject matching 有文献先例），且 ρ≈0.997 与 "31% instability" 之间的叙事张力削弱了实际影响力论证。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法执行严谨，控制实验充分（random split、ability matching、within-family、structural analysis 等），但归因缺口（DIF 只检测 THAT 不解释 WHY）和排名保持与 instability 主张之间的张力构成实质性关切 |
| Excitement | 3/5 | 发现有趣但方法论新颖性有限——"现有方法应用到新领域"的框架限制了兴奋度；ρ≈0.997 排名保持使实际影响论证乏力 |
| Reproducibility | 4/5 | 匿名代码仓库提供，METABENCH 数据公开，方法描述清晰完整，附录包含充分的实验细节 |
| Overall Assessment | 3.5/5 | Borderline Conference |

---

## 主要优势

**S1. 分析规模和系统性**：5,227 模型 × 12,508 MMLU 题目的大规模 DIF 分析，扩展到 6 个 METABENCH 基准（共 27,125 题目），是迄今 LLM 基准领域最大规模的测量不变性审计。多种控制条件（random split C%=0.18%、ability-quintile C%=2.9%、within-family C%=61.3%、matched-ability C%≈28.9%）形成令人信服的证据链。

**S2. Ground truth meta-critique 概念贡献突出**：指出 web-overlap labels 与 DIF flags 近乎独立（enrichment=0.964, φ=0.012, Jaccard=0.206），揭示了污染检测领域一个重要的验证方法论漏洞。这一发现对后续所有使用 web-overlap labels 作为 ground truth 的 contamination detection 工作都有直接指导意义，是本文最有价值的贡献。

**S3. 诚实的局限性讨论**：论文在 Limitations 中坦诚承认了归因缺口、非独立样本问题、二值注入的非现实性，以及 GSM1K 分析的探索性质。这种学术诚实值得肯定。

**S4. 跨基准复制增强可信度**：6 个基准上一致发现 17.9-31.3% 的 temporal DIF（每个都是随机基线的 45-174 倍），且 knowledge/reasoning 基准（C%≥26.9%）高于 procedural 基准（C%≤18.9%），这不是单一数据集的偶然现象。

**S5. 写作整体清晰**：论文结构标准，术语使用一致，Figure 1 的 global vs. differential contamination 图示直观有效。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] ρ≈0.997 与 "31% instability" 之间的叙事张力未充分解决
- 具体位置：Abstract（"LLM benchmarks need psychometric monitoring, not just score reporting"）、Section 1 第 1 段、Section 4.6、Section 5.1
- 问题：论文的核心主张是 31.3% 的 MMLU 题目存在 temporal DIF，但自身证据同时表明排名高度保持（ρ≈0.997, τ≈0.958, flip rate ≤2.8%）。"diagnostic, not destructive" 的定位虽然合理，但**论文未能令人信服地论证为什么 practitioners 应该关心一种不影响排名的 instability**。
  - Section 5.1 的三层分解（impact/DIF/attribution）停留在概念层面，缺乏"如果忽略 DIF 会导致什么具体错误"的实证示例。
  - Section 4.6 提到 Llama-3 获得 +53 中位数排名提升、Mistral 损失 35 位，但这些是在移除 DIF items 后的变化——这本身说明的是 DIF items 包含家族特异性信号，而非忽略 DIF 会导致错误决策。
  - 一个强有力的改进方向：展示一个具体场景，例如"Model X 在 full MMLU 上排名第 k，但如果只看 stable items 排名第 m，这种差异会导致一个具体的错误部署决策。"
- 为什么影响接收：如果论文的核心发现的实际意义不清晰，AC 和其他 reviewer 很可能质疑"so what?"。对于 EMNLP 来说，实际可操作性是重要的接收考量。
- 建议修改方向：(a) 提供 1-2 个具体案例，展示 DIF 如何在排名保持的情况下仍导致错误结论；(b) 或者调整主叙事框架，将重点从"instability"转向"measurement heterogeneity reveals hidden capability structure"——即 DIF 的价值不在于纠正排名，而在于揭示被聚合分数掩盖的能力维度变化。

**N2** [critical] 归因缺口严重限制审计协议的可操作性
- 具体位置：Section 5.3（Recommended DIF Audit Protocol）、Limitations 第 1 段
- 问题：审计协议建议在 C%≥25% 时"investigate flagged items and report stable-item rankings"，但**investigate for what**？DIF 检测到的是 THAT（题目功能差异存在），不是 WHY（污染、能力变化、还是训练方法变化）。如果 benchmark maintainer 按照此协议标记了 31% 的 MMLU 题目为 unstable，下一步该做什么？移除它们（但论文说它们包含有价值的判别信息）？保留但报告（和现在有什么区别）？
  - 三层框架的第三层"attribution"被论文自己描述为"underdetermined without training data"（Section 5.1），但协议没有提供绕过这个限制的方法。
  - 15%/25% 的阈值声称"adapt ETS practice"（Section 5.3），但 ETS 实践中的阈值是针对特定教育测试场景的；没有证据表明这些数值可以直接迁移到 LLM 基准评测中。为什么不是 10%/20% 或 20%/30%？
- 为什么影响接收：缺乏可操作的后续步骤使论文的"practical contribution"主张大打折扣。
- 建议修改方向：(a) 提供阈值选择的实证依据（例如，基于模拟分析确定 C% 多高时会导致 Spearman ρ 显著下降）；(b) 为每个 action level 提供具体的可执行步骤，而非仅"investigate"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Cross-subject matching 新颖性声明需更谨慎措辞
- 具体位置：Section 3.4（"Remark (Zero FPR under single-subject matching)"）、Contribution 2、Section 2 第 3 段
- 问题：论文在 Related Work 中诚实引用了 Nandakumar (1993) 和 Donoghue (1993) 作为 DIF 文献先例，但在 Contribution 列表和 Abstract 中，cross-subject matching 被框架为一个独立贡献。"Remark (Zero FPR under single-subject matching)" 看起来像理论贡献，但实际上是匹配设计的直接推论——如果 matching variable 不包含被注入的题目，FPR=0 是 by construction 的结果，不需要证明。
  - DIF 文献中使用外部匹配变量（external matching variable）或子测验分数（subtest score matching）已有成熟实践，例如 Swaminathan & Rogers (1990) 讨论了 purified matching。论文的贡献在于将这些技术适配到 LLM 多域基准的特定场景，而非匹配技术本身。
- 建议：将 Remark 重新定位为"设计选择及其性质"而非"理论贡献"，并在 Contribution 2 中明确说明新颖性在于 LLM-specific adaptation 而非 matching principle。

**W2** [warning] \enlargethispage{6\baselineskip} 格式操纵过于激进
- 具体位置：discussion.tex 第 3 行（`\enlargethispage{6\baselineskip}`）
- 问题：6\baselineskip 约等于额外增加 6 行内容到页面底部。这是一个相当激进的格式操作，说明论文在 8 页限制下非常紧凑。虽然 ACL 模板不明确禁止 \enlargethispage，但大量使用会导致页面底部 margin 不一致，影响视觉质量。从 PDF 第 8 页来看，Discussion 和 Conclusion 被压缩到了页面底部。
- 建议：考虑压缩某些冗余内容（例如 Section 4.2 的 Permutation test 细节可移入附录）来自然地适应页面限制，而非通过格式操纵。

**W3** [warning] 与 Growing Pains (Habba et al., 2026) 的对比不完整
- 具体位置：Section 2 第 2 段（"Empirical comparison awaits public release of anchor item lists"）
- 问题：Growing Pains 使用固定参数校准（FPC）实现跨评估期可比性，这与本文的 temporal DIF 分析在问题域上有显著重叠——两者都关注"跨时间段的基准测量一致性"。论文正确指出两者互补（DIF 识别 stable anchor items，FPC 使用它们），但"empirical comparison awaits public release"这句话留下了一个显著的空白。
  - Growing Pains 已于 2026 年 4 月公开在 arXiv（2604.12843），如果代码和数据尚未公开，论文至少可以基于其已发表的报告进行概念层面的更深入对比（例如：FPC 在 100 个 anchor items 上达到 2-3 pp 预测误差，ρ≥0.9——这与 DIF 发现的 31% instability 如何关联？FPC 假设 anchor items 稳定，但本文发现 31% 不稳定——这是否意味着 FPC 需要先做 DIF screening？）
- 建议：即使无法做实证对比，也应在讨论中更具体地分析两种方法的互补关系和潜在冲突。

**W4** [warning] Semi-synthetic injection 现实性存疑
- 具体位置：Section 3.4（Procedure）、Limitations 第 1 段
- 问题：二值响应翻转（incorrect → correct at rate p）代表的是最极端的均匀污染模式。真实世界的污染表现为部分记忆（partial memorization）、推理捷径（reasoning shortcuts）、格式特定优势等。ΔTPR = +0.508 at p=0.5 是在这种极端条件下的检测率，在更现实的污染模式下可能显著降低。
  - Limitations 承认了这一点，但未讨论 sensitivity——例如，如果污染只影响高能力模型而非整个 focal group（differential exploitation），检测率会如何变化？
- 建议：在附录中补充至少一种更现实的注入模式（例如 ability-dependent exploitation rate），展示方法对非均匀污染的鲁棒性。

**W5** [warning] 缺少对 polytomous DIF 方法和非选择题基准的讨论
- 具体位置：Limitations 第 4 段
- 问题：Limitations 中提到"generalizability to open-ended generation... is untested and would require polytomous DIF methods"，但 Related Work (Section 2, DIF Methodology) 完全没有讨论 polytomous DIF 方法（如 generalized MH、logistic regression for ordinal data、IRT-LR）。考虑到 LLM 评测正在迅速向 open-ended generation 和 partial-credit 评测迁移，这是一个值得在 Related Work 中简要覆盖的方向。
- 建议：在 Section 2 的 DIF Methodology 段落中用 1-2 句话提及 polytomous DIF 作为未来扩展方向的文献基础。

---

## 小问题（不影响接收）

- **M1** Abstract 中 "z = −8σ to −49σ" 的记号不标准。σ 通常指标准差，这里应该是 z-score 的单位。标准写法是 "z = −8 to −49" 或 "$8$ to $49$ standard deviations"。
- **M2** Table 1 caption 中 "FPR is measured against Li et al. web-overlap labels on the 'clean' subset" 表述模糊——这里的 FPR 是 DIF 将 clean items 标记为 C 类的比率，但 "FPR" 在论文其他地方（Section 3.4）指的是 semi-synthetic injection 的假阳性率。两个 FPR 概念不一致。
- **M3** Section 4.2 中的 bootstrap CI [29.4%, 38.1%] 的右偏不对称性没有解释来源——后文说 "rightward asymmetry reflects heavy-tailed C% from subjects exceeding 40%"，但这是关于 subject-level C% 分布的，为什么会影响 model-level bootstrap CI？建议简要说明 resampling 策略。
- **M4** Figure 2 (dose-response curve) 的上面板 (ΔTPR) 和下面板 (FPR) 使用不同的 x 轴刻度标签格式不完全一致——minor visual issue。
- **M5** "Llama-2 vs. Llama-3" 的 C%=61.3% 在 Table 1 中没有 FPR (clean) 和 Enrichment 数据（标注为 "--"）。建议注释原因——是因为样本量不足还是因为 web-overlap labels 不适用于 within-family 比较？
- **M6** Double-blind 匿名性：脚注 1 使用了 anonymous.4open.science 链接，匿名处理得当。未发现泄露作者身份的自引。

---

## 缺失参考文献

1. **Maeda & Lu (2025/2026), "Finding Words Associated with DIF: Predicting Differential Item Functioning using LLMs and Explainable AI"** (arXiv 2502.07017 / J. Educational Measurement) — 论文已引用为 maeda2025difllm（Section 2 第 4 段），引用恰当。✓

2. **French & Holmes-Finch (2010), "Hierarchical logistic regression"** — 已引用。✓

3. **建议补充**：
   - **Vandenberg & Lance (2000)** 的 measurement invariance 综述——论文在 Related Work 中提到了 measurement invariance testing 但具体引用缺失（只在 \citep{meredith1993invariance, vandenberg2000invariance} 中出现，需要确认是否在参考文献列表中）。→ 经检查，references.bib 应包含此引用，已在 Section 2 中引用。✓
   - **Liu et al. (2019), "Learning latent parameters without human responses"** — IRT 在非人类群体中的应用，但可能超出范围。不强制要求。

4. **关于 Hardy et al. (2026) scalability coefficients**：论文在 Related Work 中引用了 hardy2026scalability，但我通过 web search 未能独立找到这篇文献。建议验证该引用的准确性和可获取性。

---

## 对 Director 审查侧重的逐条回应

### 1. 新颖性评估
- **MH-DIF 方法本身无修改，应用新颖性是否充够？** 边界情况。方法论新颖性有限，但实证发现有价值。31% temporal DIF 和 ground truth meta-critique 是有意义的贡献。对于 EMNLP 来说，这类"成熟方法的大规模应用揭示重要发现"的论文有先例被接收，但需要发现本身足够 surprising——而 ρ≈0.997 的排名保持在一定程度上削弱了 surprise factor。
- **三大贡献排序**：Ground truth meta-critique 是最有价值的贡献（最具原创性和普适性）；temporal instability at scale 是最有影响力的发现（规模和跨基准复制）；semi-synthetic validation framework 是最弱的贡献（cross-subject matching 有先例，binary injection 过于简化）。当前排序合理。
- **Concurrent work 区分**：与 Growing Pains 的互补关系论述合理但不完整（见 W3）。与 PSN-IRT 和 BHI 的区分清晰。
- **Cross-subject matching DIF 文献先例**：有。Nandakumar (1993) 和 Donoghue (1993) 已讨论在多维测验中使用 purified/external matching。论文诚实引用了这些先例，但在 Contribution framing 中应更谨慎（见 W1）。

### 2. Related Work 覆盖
- 总体覆盖较完整。Contamination detection、IRT in LLM evaluation、DIF methodology、benchmark quality 四个段落结构清晰。
- 遗漏：polytomous DIF 方法（见 W5）、purified matching 的更完整文献（Swaminathan & Rogers 1990 的 purified subtest approach）。
- Growing Pains 对比不完整（见 W3）。
- Hardy et al. (2026) 引用待验证。

### 3. 叙事一致性
- **标题**："Temporal Measurement Instability" 准确反映论文内容，但 "instability" 一词暗示了一种比实际发现更严重的问题——在 ρ≈0.997 的上下文中，"measurement heterogeneity" 或 "differential functioning" 可能更精确。
- **ρ≈0.997 vs. 31% 叙事张力**：这是论文最大的叙事挑战（见 N1）。
- **"diagnostic, not destructive" 定位**：在 Introduction 和 Discussion 中出现，但在 Experiments 部分有时措辞偏向 alarmist（例如 "31% Measurement Instability" 的 section title），不完全一致。
- **三层框架**：在 Section 5.1 引入，但在 Experiments 部分未系统使用——实验结果的呈现没有按 impact/DIF/attribution 分层组织。

### 4. 写作质量与格式合规
- **页数**：主文（Sections 1-6）在 8 页以内，但使用了激进的 \enlargethispage{6\baselineskip}（见 W2）。Limitations 不计入页数限制，合规。
- **结构标准**：完整包含 Abstract、Introduction、Related Work、Method、Experiments、Discussion、Conclusion、Limitations。各节篇幅基本均衡，但 Discussion（3 个子节）相对于 Experiments（7 个子节）较薄。
- **数学符号**：一致使用 α_MH、Δ_MH、C% 等。
- **Figure/Table 质量**：Figure 1 直观有效；Figure 2 清晰；Table 1-3 信息密度高但可读。附录中 Figure 4 (downstream impact) 和 Figure 5 (GSM1K) 较小但可读。
- **Limitations**：覆盖了 4 个方面（方法范围、样本非独立性、匹配边界、泛化性），长度恰当（约 1.5 个 column），不过长。
- **Double-blind**：匿名维持良好（见 M6）。

### 5. Practical significance
- **31% DIF 的实际影响**：如果排名不变（ρ≈0.997），practitioners 缺乏明确的行动动机（见 N1 和 N2）。
- **Audit protocol 可操作性**：阈值缺乏实证依据，action steps 过于模糊（见 N2）。
- **对不同利益相关者的启示**：论文对 benchmark designers 的建议最清晰（DIF pre-screening for anchor items），对 leaderboard maintainers（report stable-item rankings）次之，对 model developers 最弱（几乎没有可操作建议）。

---

## 最终判断

本文是一篇技术执行出色、规模宏大的实证研究。Ground truth meta-critique 是其最有价值的贡献，31% temporal DIF 的跨基准复制结果令人印象深刻。然而，(1) 方法论新颖性有限（MH-DIF 未修改、cross-subject matching 有先例），(2) ρ≈0.997 vs. 31% instability 的叙事张力未充分解决，(3) 审计协议缺乏可操作性——这三个因素使论文处于 Borderline Conference 水平。如果作者能有效解决 N1（通过具体案例展示 practical significance）和 N2（提供可操作的审计步骤），论文有望提升至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-22T03:34:19.461042+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-22T03:34:19.461483+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-22T03:35:02.397412+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### Overall: 3.5 — Borderline Conference\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | MH χ² 独立性假设在 5,227 模型中被严重违反；Monte Carlo power analysis 使用 2PL 参数但 MMLU poor fit to 2PL |\n| Excitement | 3.5/5 | DIF 方法引入 NLP 评测新颖且有实践价值；ground truth meta-critique 重要 |\n| Confidence | 4/5 | 熟悉 DIF 方法论和 LLM evaluation 文献 |\n\n### Must-Fix\n\n**N1** [critical] LLM examinee 非独立性对 MH χ² 和 permutation test 的影响未充分解决\n- MH χ² 假设 examinee 独立。5,227 个模型中大量 fine-tune variants 共享参数和训练数据，违反独立性。导致：(a) MH χ² 显著性 inflate，有效样本量远小于 N=5,227；(b) Permutation test（200 cohort-level shuffles）shuffling non-independent units 无法正确估计 null；(c) Bootstrap CI 假设 independent sampling，clustered 数据下 underestimate variance。\n- 论文的缓解措施（family de-duplication K=20,25,121）有信息量但不充分——不同 family 仍可能因共享训练数据而非独立。\n- 建议：(1) 报告 family 数量及 size 分布；(2) cluster-robust permutation test；(3) cluster bootstrap CI；(4) 如果结论不变则大幅加强论文。\n\n**N2** [critical] Semi-synthetic ΔTPR 应在主文中明确标注为 upper-bound estimate\n- Binary response flipping 是最极端的 uniform DIF 注入。Real-world contamination 信号可能远弱于此。主文 §3.4 和 §4.5 没有显式标注 \"upper bound\"——仅在 Limitations 隐晦提及。Abstract 直接引用 ΔTPR=+0.508 无任何限定词。\n- 建议：§3.4、§4.5 首次报告时加 \"upper-bound\"/\"ceiling estimate\"；Abstract 加 \"under worst-case uniform injection\"。\n\n**N3** [critical] Monte Carlo power analysis 与 2PL poor fit 之间的矛盾\n- §4.1 使用 2PL 参数估计检测力，Appendix A.2 承认 MMLU poor fit to 2PL。Monte Carlo TPR 估计可能系统性偏高或偏低。论文用 triangulation 论证但两条线并非独立。\n- 建议：(1) 明确标注为 approximate estimate under parametric assumptions；(2) 以 semi-synthetic injection 为主要 power evidence，Monte Carlo 降级为补充。\n\n### Should-Fix\n\n**W1** Abstract 中 ΔFPR=0.000 缺乏 multi-subject contamination 限定。multi-subject injection（k≤5）时 ΔFPR 上升至 0.003-0.069。\n\n**W2** K=5 quintile stratification 敏感性分析缺失。N=5,227 完全支持 K=10/20，未报告 K 的敏感性。\n\n**W3** Within-subject C%=38.1% > temporal C%=31.3% 解释不充分。是否说明 temporal C% 是 underestimate？subject 间多维性在标准 matching 中起 cancellation 作用？\n\n**W4** §4.3 统计显著性与实际显著性混淆。Enrichment=0.96, p=0.012——大样本下 trivially small deviation 也达 p<0.05，\"near-independent\" 与 p=0.012 看似矛盾。\n\n**W5** §5.3 审计协议 \"Act\" 层缺乏可操作指引。DIF 无法归因时 \"investigate\" 的具体步骤是什么？\n\n**W6** 低注入率（p<0.3）的检测力未报告。实际 contamination 可能对应 p=0.05-0.2，Figure 2 显示 TPR 在 p=0.3 已低于 0.5。\n\n### Questions\n\n**Q1**: 5,227 模型中有多少个 distinct model families？Family size 分布？Cluster-robust permutation test 下 C% 和 p-value？\n**Q2**: Random split baseline 是模型层面还是 family 层面随机分？\n**Q3**: Monte Carlo power analysis 使用的 2PL 参数从何而来？2PL fit 差时参数可靠吗？\n**Q4**: Cross-subject matching 中 MMLU total score 匹配 GSM8K items——construct 不同是否引入 matching bias？\n**Q5**: GSM1K r=-0.478 的 95% CI？N=33 下相关系数 instability 大。\n**Q6**: 是否考虑 Lord's χ² 或 Raju's area 作为 IRT-based DIF robustness check？\n\n### 主要优势\n1. 新颖跨领域方法迁移\n2. 多路径 converging evidence 设计缜密\n3. Ground truth meta-critique 概念贡献突出\n4. 规模和数据基础扎实（5,227×12,508）\n5. \"that\" not \"why\" 认识论定位贯穿全文\n6. Cross-subject matching 的 Remark 清晰可验证"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n### Overall: 3.5 — Borderline Conference\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | MH χ² 独立性假设在 5,227 模型中被严重违反；Monte Carlo power analysis 使用 2PL 参数但 MMLU poor fit to 2PL |\n| Excitement | 3.5/5 | DIF 方法引入 NLP 评测新颖且有实践价值；ground truth meta-critique 重要 |\n| Confidence | 4/5 | 熟悉 DIF 方法论和 LLM evaluation 文献 |\n\n### Must-Fix\n\n**N1** [critical] LLM examinee 非独立性对 MH χ² 和 permutation test 的影响未充分解决\n- MH χ² 假设 examinee 独立。5,227 个模型中大量 fine-tune variants 共享参数和训练数据，违反独立性。导致：(a) MH χ² 显著性 inflate，有效样本量远小于 N=5,227；(b) Permutation test（200 cohort-level shuffles）shuffling non-independent units 无法正确估计 null；(c) Bootstrap CI 假设 independent sampling，clustered 数据下 underestimate variance。\n- 论文的缓解措施（family de-duplication K=20,25,121）有信息量但不充分——不同 family 仍可能因共享训练数据而非独立。\n- 建议：(1) 报告 family 数量及 size 分布；(2) cluster-robust permutation test；(3) cluster bootstrap CI；(4) 如果结论不变则大幅加强论文。\n\n**N2** [critical] Semi-synthetic ΔTPR 应在主文中明确标注为 upper-bound estimate\n- Binary response flipping 是最极端的 uniform DIF 注入。Real-world contamination 信号可能远弱于此。主文 §3.4 和 §4.5 没有显式标注 \"upper bound\"——仅在 Limitations 隐晦提及。Abstract 直接引用 ΔTPR=+0.508 无任何限定词。\n- 建议：§3.4、§4.5 首次报告时加 \"upper-bound\"/\"ceiling estimate\"；Abstract 加 \"under worst-case uniform injection\"。\n\n**N3** [critical] Monte Carlo power analysis 与 2PL poor fit 之间的矛盾\n- §4.1 使用 2PL 参数估计检测力，Appendix A.2 承认 MMLU poor fit to 2PL。Monte Carlo TPR 估计可能系统性偏高或偏低。论文用 triangulation 论证但两条线并非独立。\n- 建议：(1) 明确标注为 approximate estimate under parametric assumptions；(2) 以 semi-synthetic injection 为主要 power evidence，Monte Carlo 降级为补充。\n\n### Should-Fix\n\n**W1** Abstract 中 ΔFPR=0.000 缺乏 multi-subject contamination 限定。multi-subject injection（k≤5）时 ΔFPR 上升至 0.003-0.069。\n\n**W2** K=5 quintile stratification 敏感性分析缺失。N=5,227 完全支持 K=10/20，未报告 K 的敏感性。\n\n**W3** Within-subject C%=38.1% > temporal C%=31.3% 解释不充分。是否说明 temporal C% 是 underestimate？subject 间多维性在标准 matching 中起 cancellation 作用？\n\n**W4** §4.3 统计显著性与实际显著性混淆。Enrichment=0.96, p=0.012——大样本下 trivially small deviation 也达 p<0.05，\"near-independent\" 与 p=0.012 看似矛盾。\n\n**W5** §5.3 审计协议 \"Act\" 层缺乏可操作指引。DIF 无法归因时 \"investigate\" 的具体步骤是什么？\n\n**W6** 低注入率（p<0.3）的检测力未报告。实际 contamination 可能对应 p=0.05-0.2，Figure 2 显示 TPR 在 p=0.3 已低于 0.5。\n\n### Questions\n\n**Q1**: 5,227 模型中有多少个 distinct model families？Family size 分布？Cluster-robust permutation test 下 C% 和 p-value？\n**Q2**: Random split baseline 是模型层面还是 family 层面随机分？\n**Q3**: Monte Carlo power analysis 使用的 2PL 参数从何而来？2PL fit 差时参数可靠吗？\n**Q4**: Cross-subject matching 中 MMLU total score 匹配 GSM8K items——construct 不同是否引入 matching bias？\n**Q5**: GSM1K r=-0.478 的 95% CI？N=33 下相关系数 instability 大。\n**Q6**: 是否考虑 Lord's χ² 或 Raju's area 作为 IRT-based DIF robustness check？\n\n### 主要优势\n1. 新颖跨领域方法迁移\n2. 多路径 converging evidence 设计缜密\n3. Ground truth meta-critique 概念贡献突出\n4. 规模和数据基础扎实（5,227×12,508）\n5. \"that\" not \"why\" 认识论定位贯穿全文\n6. Cross-subject matching 的 Remark 清晰可验证"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-22T03:35:41.873070+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 39475
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-22T03:35:42.075042+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n### Overall: 3.5 — Borderline Conference\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法执行严谨，控制实验充分，但归因缺口和排名保持与 instability 主张的张力构成实质性关切 |\n| Excitement | 3/5 | 发现有趣但方法论新颖性有限——\"现有方法应用到新领域\"框架限制兴奋度；ρ≈0.997 使实际影响论证乏力 |\n| Reproducibility | 4/5 | 匿名代码仓库，METABENCH 数据公开，方法描述清晰 |\n\n### Must-Fix\n\n**N1** [critical] ρ≈0.997 与 \"31% instability\" 之间的叙事张力未充分解决\n- 核心主张是 31.3% DIF，但排名高度保持（ρ≈0.997, τ≈0.958, flip rate ≤2.8%）。\"diagnostic, not destructive\" 定位合理但论文未令人信服论证 practitioners 为何应关心不影响排名的 instability。\n- §5.1 三层分解停留概念层面，缺乏\"忽略 DIF 导致什么具体错误\"的实证示例。§4.6 的 Llama-3 +53 / Mistral -35 位说明的是 DIF items 包含家族特异性信号，非忽略 DIF 导致错误决策。\n- 建议：(a) 提供 1-2 个具体案例展示 DIF 在排名保持下仍导致错误结论；(b) 或调整叙事从 \"instability\" 转向 \"measurement heterogeneity reveals hidden capability structure\"。\n\n**N2** [critical] 归因缺口严重限制审计协议可操作性\n- §5.3 \"Act\" 时 \"investigate flagged items\"——investigate for what？DIF 只检测 THAT 不解释 WHY。benchmark maintainer 标记 31% items 后该做什么？\n- 15%/25% 阈值声称 \"adapt ETS practice\" 但无证据直接迁移到 LLM 场景。\n- 建议：(a) 阈值选择的实证依据（模拟 C% 多高时 ρ 显著下降）；(b) 每个 action level 具体可执行步骤。\n\n### Should-Fix\n\n**W1** Cross-subject matching 新颖性声明需更谨慎。DIF 文献中 external/subtest matching 已有成熟实践（Nandakumar 1993, purified matching）。Remark 是 matching 设计的直接推论（by construction），非需要证明的理论贡献。建议重新定位为 \"设计选择及其性质\"。\n\n**W2** \\enlargethispage{6\\baselineskip} 格式操纵过于激进。建议压缩冗余内容（如 §4.2 permutation 细节可移入附录）。\n\n**W3** 与 Growing Pains (Habba et al. 2026) 对比不完整。\"empirical comparison awaits public release\" 留下显著空白。论文可基于已发表报告做更深入概念对比（FPC 假设 anchor items 稳定 vs 本文发现 31% 不稳定）。\n\n**W4** Semi-synthetic injection 现实性存疑。binary flipping 是最极端模式，real-world contamination 更复杂。建议附录补充至少一种更现实注入模式（ability-dependent exploitation rate）。\n\n**W5** 缺少对 polytomous DIF 方法的讨论。LLM 评测正向 open-ended generation 迁移，Related Work 应简要覆盖 polytomous DIF 文献。\n\n### 小问题\n- M1: \"z = −8σ to −49σ\" 记号不标准\n- M2: Table 1 vs §3.4 中 \"FPR\" 概念不一致\n- M3: Bootstrap CI [29.4%, 38.1%] 右偏来源解释不清\n- M4: Figure 2 上下面板格式不完全一致\n- M5: Table 1 中 Llama-2 vs Llama-3 的 FPR/Enrichment 为 \"--\"，未注释原因\n- M6: Double-blind 匿名维持良好 ✓\n\n### 缺失参考文献\n- Hardy et al. (2026) scalability coefficients 待验证可获取性\n- 建议补充 Swaminathan & Rogers (1990) purified subtest matching\n\n### 叙事一致性评估\n- 标题 \"Temporal Measurement Instability\" 准确但在 ρ≈0.997 上下文中 \"measurement heterogeneity\" 可能更精确\n- \"diagnostic, not destructive\" 定位不完全一致——§4.2 section title \"31% Measurement Instability\" 偏 alarmist\n- 三层框架在 §5.1 引入但 Experiments 部分未系统使用\n\n### 主要优势\n1. 分析规模和系统性（5,227×12,508，6 基准）\n2. Ground truth meta-critique 概念贡献突出\n3. 诚实的局限性讨论\n4. 跨基准复制增强可信度（17.9-31.3%, 45-174× above baseline）\n5. 写作整体清晰"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n### Overall: 3.5 — Borderline Conference\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法执行严谨，控制实验充分，但归因缺口和排名保持与 instability 主张的张力构成实质性关切 |\n| Excitement | 3/5 | 发现有趣但方法论新颖性有限——\"现有方法应用到新领域\"框架限制兴奋度；ρ≈0.997 使实际影响论证乏力 |\n| Reproducibility | 4/5 | 匿名代码仓库，METABENCH 数据公开，方法描述清晰 |\n\n### Must-Fix\n\n**N1** [critical] ρ≈0.997 与 \"31% instability\" 之间的叙事张力未充分解决\n- 核心主张是 31.3% DIF，但排名高度保持（ρ≈0.997, τ≈0.958, flip rate ≤2.8%）。\"diagnostic, not destructive\" 定位合理但论文未令人信服论证 practitioners 为何应关心不影响排名的 instability。\n- §5.1 三层分解停留概念层面，缺乏\"忽略 DIF 导致什么具体错误\"的实证示例。§4.6 的 Llama-3 +53 / Mistral -35 位说明的是 DIF items 包含家族特异性信号，非忽略 DIF 导致错误决策。\n- 建议：(a) 提供 1-2 个具体案例展示 DIF 在排名保持下仍导致错误结论；(b) 或调整叙事从 \"instability\" 转向 \"measurement heterogeneity reveals hidden capability structure\"。\n\n**N2** [critical] 归因缺口严重限制审计协议可操作性\n- §5.3 \"Act\" 时 \"investigate flagged items\"——investigate for what？DIF 只检测 THAT 不解释 WHY。benchmark maintainer 标记 31% items 后该做什么？\n- 15%/25% 阈值声称 \"adapt ETS practice\" 但无证据直接迁移到 LLM 场景。\n- 建议：(a) 阈值选择的实证依据（模拟 C% 多高时 ρ 显著下降）；(b) 每个 action level 具体可执行步骤。\n\n### Should-Fix\n\n**W1** Cross-subject matching 新颖性声明需更谨慎。DIF 文献中 external/subtest matching 已有成熟实践（Nandakumar 1993, purified matching）。Remark 是 matching 设计的直接推论（by construction），非需要证明的理论贡献。建议重新定位为 \"设计选择及其性质\"。\n\n**W2** \\enlargethispage{6\\baselineskip} 格式操纵过于激进。建议压缩冗余内容（如 §4.2 permutation 细节可移入附录）。\n\n**W3** 与 Growing Pains (Habba et al. 2026) 对比不完整。\"empirical comparison awaits public release\" 留下显著空白。论文可基于已发表报告做更深入概念对比（FPC 假设 anchor items 稳定 vs 本文发现 31% 不稳定）。\n\n**W4** Semi-synthetic injection 现实性存疑。binary flipping 是最极端模式，real-world contamination 更复杂。建议附录补充至少一种更现实注入模式（ability-dependent exploitation rate）。\n\n**W5** 缺少对 polytomous DIF 方法的讨论。LLM 评测正向 open-ended generation 迁移，Related Work 应简要覆盖 polytomous DIF 文献。\n\n### 小问题\n- M1: \"z = −8σ to −49σ\" 记号不标准\n- M2: Table 1 vs §3.4 中 \"FPR\" 概念不一致\n- M3: Bootstrap CI [29.4%, 38.1%] 右偏来源解释不清\n- M4: Figure 2 上下面板格式不完全一致\n- M5: Table 1 中 Llama-2 vs Llama-3 的 FPR/Enrichment 为 \"--\"，未注释原因\n- M6: Double-blind 匿名维持良好 ✓\n\n### 缺失参考文献\n- Hardy et al. (2026) scalability coefficients 待验证可获取性\n- 建议补充 Swaminathan & Rogers (1990) purified subtest matching\n\n### 叙事一致性评估\n- 标题 \"Temporal Measurement Instability\" 准确但在 ρ≈0.997 上下文中 \"measurement heterogeneity\" 可能更精确\n- \"diagnostic, not destructive\" 定位不完全一致——§4.2 section title \"31% Measurement Instability\" 偏 alarmist\n- 三层框架在 §5.1 引入但 Experiments 部分未系统使用\n\n### 主要优势\n1. 分析规模和系统性（5,227×12,508，6 基准）\n2. Ground truth meta-critique 概念贡献突出\n3. 诚实的局限性讨论\n4. 跨基准复制增强可信度（17.9-31.3%, 45-174× above baseline）\n5. 写作整体清晰"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-22T03:35:43.735235+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1660
}
```

</details>

---


### Assistant

_source line 452 · 2026-05-22T03:35:46.220236+00:00_

交叉分享已发送至两位 Reviewer。等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 453 · 2026-05-22T03:35:48.947047+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。

- **2 个 Must-Fix**：(N1) ρ≈0.997 与 31% instability 的叙事张力未解决——论文需要具体案例论证 practitioners 为何应关心不影响排名的 instability；(N2) 审计协议阈值缺乏实证依据，action steps 过于模糊（"investigate flagged items" 但 investigate for what？）
- **5 个 Should-Fix**：cross-subject matching 新颖性需谨慎措辞（有 DIF 文献先例）、\enlargethispage{6\baselineskip} 过于激进、与 Growing Pains 对比不完整、semi-synthetic injection 现实性存疑、缺少 polytomous DIF 文献讨论
- **主要优势**：分析规模（5,227 模型×6 基准）、ground truth meta-critique 贡献突出、控制实验充分、跨基准复制可信、局限性讨论诚实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 454 · 2026-05-22T03:35:53.313226+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 455 · 2026-05-22T03:36:57.657654+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: LLM examinee 非独立性对 MH χ² 的影响**
同意这是论文最大的方法论弱点。5,227 个模型中大量 fine-tune variants 共享基底模型，有效样本量远小于名义值。论文的缓解措施（de-duplication K=20 → C%=29.1%，permutation simulation bounds LD-attributable FPR < 0.001 pp）有信息量，但如 R1 所指出，不同 family 之间仍可能因共享训练数据（如 common pre-training corpus）而非独立。

不过我想补充一个缓解因素：**效应量极大**。Temporal C%=31.3% vs Random split C%=0.18%——这是 174 倍的差异。即使有效样本量因聚类而大幅缩减（例如缩减到 1/10），31.3% 的 DIF 率本身是一个描述性统计量（不依赖 χ² 显著性），不会因非独立性而"消失"。真正受影响的是 (a) 每个 item 的 MH χ² 显著性判定（可能 inflate），(b) bootstrap CI 宽度（可能 underestimate）。R1 建议的 cluster-robust permutation test 和 cluster bootstrap 是合理的改进方向。

**[AGREE] R1-N2: ΔTPR upper-bound 标注**
完全同意。我在自己的审稿中也提出了类似关切（W4：Semi-synthetic injection 现实性存疑）。Abstract 直接报告 "ΔTPR = +0.508" 而没有任何限定词是不当的。Section 3.4 倒数第二段确实提到 "reported ΔTPR values constitute upper-bound estimates"，但这一关键限定词在 Abstract 和 Section 4.5 首次报告处被省略了。应在所有首次引用处加上 "under worst-case uniform injection" 或类似限定。

**[PARTIALLY REBUT] R1-N3: Monte Carlo power analysis 与 2PL poor fit 的矛盾**
部分反驳。R1 的关切方向正确（2PL fit 差时参数估计可能有偏），但论文的处理方式比 R1 描述的更合理：

1. Appendix A.2（Power sensitivity to item discrimination）明确承认 "Although 2PL fit is poor for MMLU's multidimensional structure, the power analysis serves as one leg of a triangulation"——这不是隐藏问题，而是明确标注。
2. 两条线并非完全不独立：Monte Carlo 使用 PSN-IRT 估计的 2PL 参数和 parametric 模拟，semi-synthetic injection 使用真实数据矩阵和 empirical response flipping。它们共享数据来源但方法路径不同。
3. R1 建议"以 semi-synthetic injection 为主要 power evidence，Monte Carlo 降级为补充"——这一建议合理，且论文的叙事结构已大致如此（Section 4.1 开头做 power analysis，Section 4.5 做 semi-synthetic validation 并在 cross-benchmark 中复制）。

建议：在 Section 4.1 开头加一句明确说明"此分析提供 approximate parametric bounds，empirical validation 见 Section 4.5"即可，不需要 critical-level 修改。

---

### Should-Fix

**[AGREE] R1-W1: ΔFPR=0.000 的 multi-subject 限定**
同意。Table 5（Appendix）清楚显示 k=10 时 ΔFPR 升至 0.047±0.022，k=20 时达 0.069±0.018。Abstract 的 "ΔFPR = 0.000" 应加限定 "under single- to few-subject contamination (k ≤ 5)"。

**[PARTIALLY REBUT] R1-W2: K=5 quintile 敏感性分析**
部分反驳。K=5 quintile-based binning 是 ETS 标准实践（论文引用 Donoghue 1993, Clauser 1998），且 Section 3.2 明确说明遵循此标准。虽然 N=5,227 可以支持更多层，但增加 K 并不总是更好——K 过大会导致每层内样本量不足、稀疏 contingency table，尤其在 DIF 效应量大时（ETS C 级别 |Δ_MH| ≥ 1.5）。Section 4.4 中 IRT θ-conditioning with 20 ability strata 已提供了事实上的 K=20 敏感性检验（C%=31.2% vs 31.3%），虽然不是 MH 框架内的 K 变化，但功能等价。

不过，R1 要求在 MH 框架内做 K 敏感性分析的建议仍然合理——这是一个低成本高回报的补充实验。

**[AGREE] R1-W3: Within-subject C%=38.1% > temporal C%=31.3% 解释不充分**
同意。Section 4.4 提到 within-subject C% 较高，Appendix B 提到 Q3 统计量显示 within-subject local dependence（11.3% item pairs exceed |Q3|>0.20 vs 2.2% cross-subject），但**没有直接连接这两个发现**——即没有明确说"within-subject C% 较高部分是因为 local dependence inflate，而非 temporal C% 是 underestimate"。这个解释缺口值得补充。

我的判断是 temporal C%=31.3%（使用 cross-subject matching）更可靠，因为它避免了 within-subject local dependence；within-subject C%=38.1% 可能被 inflated。但论文应该明确论证这一点。

**[REBUT] R1-W4: Enrichment=0.96, p=0.012 的统计显著性与实际显著性混淆**
反驳。**R1 此处存在事实性错误。** 论文 Section 4.3 原文明确报告："Association tests yield φ = 0.012, χ² = 1.28 (**p = 0.258**), and OR = 1.05 [0.96, 1.15]"。p=0.258，不是 p=0.012。R1 将 φ coefficient（=0.012，一个效应量指标）误读为 p-value。

在 p=0.258 下，不仅效应量 trivially small（φ=0.012），且连统计显著性都未达到。"Near-independent" 的判断完全合理：效应量极小（φ=0.012）、odds ratio 包含 1（OR=1.05 [0.96, 1.15]）、且未达统计显著性。R1 描述的"大样本下 trivially small deviation 也达 p<0.05"的情景并不存在。

**[AGREE] R1-W5: 审计协议 "Act" 层缺乏可操作指引**
完全同意。这与我的 N2 issue 一致——审计协议的 action levels 过于抽象，尤其在 DIF 无法归因的前提下。"Investigate flagged items" 需要具体化为可执行步骤。

**[AGREE] R1-W6: 低注入率检测力未报告**
同意。Figure 2 的 dose-response 曲线虽然覆盖了 p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}，但缺少 p < 0.3 的数据点。真实世界的 contamination 可能对应更低的 exploitation rate（p=0.05-0.2），在这个区间内 MH-DIF 的检测力很可能不足。这进一步支持了 ΔTPR=+0.508 是 upper-bound 的论点。

---

### Questions

**R1-Q1（Family 数量和分布）**: 好问题。论文 Section 3.2（LLM-specific challenges）提到 "graduated de-duplication" 但没有报告 family 数量和 size 分布。这对评估非独立性的严重程度至关重要。

**R1-Q2（Random split 层面）**: 好问题。Section 4.2 说 "random split of the 2023 cohort"，但未明确是 model-level 还是 family-level random split。如果是 model-level split，同一 family 可能被分到两边，此时 C%=0.18% 的 null 率可能被 underestimate（因为 family 内相似性降低了两组差异）。

**R1-Q3（2PL 参数来源）**: Section 4.1 明确说 "empirical 2PL parameters from PSN-IRT (Zhou et al., 2026)"——参数来自 PSN-IRT 对 14,042 MMLU items 的估计。在 2PL fit 差的情况下，这些参数作为 summary statistics 仍有描述性价值，但作为 power analysis 的生成模型参数确实不理想。

**R1-Q4（Cross-benchmark matching 的 construct 差异）**: 好问题。用 MMLU total score 匹配 GSM8K items 时，两个 benchmark 测量不同 constructs。这可能引入 matching bias——如果 MMLU 能力与 GSM8K 能力仅部分相关，匹配不完全，可能有 residual ability confounding。不过这可能导致 C% 偏高而非偏低，且 GSM8K 的 temporal C%=18.9% 实际上低于 MMLU。

**R1-Q5（GSM1K r=-0.478 的 CI）**: 论文未报告 CI。N=33 时 r=-0.478 的 95% CI 大致为 [-0.71, -0.16]，宽度约 0.55——确实 instability 大。论文在 Limitations 中承认 "limited statistical power and is exploratory"。

**R1-Q6（Lord's χ² / Raju's area）**: Section 4.4 已使用 logistic regression DIF 作为 robustness check（92.1% concordance with MH）。Lord's χ² 和 Raju's area 需要 IRT 参数估计，但论文已证明 2PL fit 差。在这种情况下，MH-DIF（non-parametric）比 IRT-based DIF 方法更合适。R1 的建议方向正确，但可能反而引入更多模型依赖性问题。

---

### R1 主要优势评价

R1 对论文优势的 6 点总结公正。我特别同意 R1 对 "that" not "why" 认识论定位的肯定——这是论文在 framing 上最成功的部分，贯穿了从 Introduction 到 Limitations 的全文。

### 与我审稿意见的交叉对比

**共识点**：
- Ground truth meta-critique 是最有价值的贡献（R1 优势 3 = R2 优势 S2）
- 审计协议缺乏可操作性（R1-W5 = R2-N2）
- Semi-synthetic injection 现实性有限（R1-N2 ≈ R2-W4）
- 整体评分一致（R1: 3.5, R2: 3.5）

**分歧点**：
- R1 给 Soundness 3/5，我给 3.5/5。我认为论文的 robustness checks 比 R1 承认的更全面——尤其是 multiple controls 的 converging evidence 设计。非独立性确实是问题，但 31.3% vs 0.18% 的效应量差异太大，不可能被统计方法论瑕疵解释掉。
- R1 给 Excitement 3.5/5，我给 3/5。R1 认为方法迁移新颖，我认为 MH-DIF 直接套用的新颖性有限（见我的 N1 关于叙事张力、W1 关于 cross-subject matching 先例）。
- R1 在 W4 上存在事实性错误（将 φ=0.012 误读为 p=0.012）——这一点需要纠正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 456 · 2026-05-22T03:37:13.332294+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 457 · 2026-05-22T03:37:16.095920+00:00_

[Reviewer 2 审稿结果]:
已向 Director 提交对 Reviewer 1 的逐条回应。核心判断：

- **3 条 AGREE**（N1 非独立性、N2 upper-bound 标注、W5 审计可操作性）
- **1 条 PARTIALLY REBUT**（N3 power analysis 矛盾——论文处理比 R1 描述的更合理）
- **1 条 REBUT**（W4 存在事实性错误：R1 将 φ=0.012 误读为 p=0.012，实际 p=0.258）
- 两位 Reviewer 在整体评分（3.5）和核心关切（审计可操作性、injection 现实性）上高度一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 458 · 2026-05-22T03:37:29.390393+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 48

## Round 48

14 recorded events


### User

_source line 459 · 2026-05-22T03:37:39.046405+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: ρ≈0.997 与 "31% instability" 的叙事张力**

同意这是论文最需要解决的叙事问题。ρ≈0.997（§4.6, Figure 4）和 τ≈0.958 表明整体排名几乎不受影响，而标题和 §4.2 section title（"31% Measurement Instability"）给出了 alarmist 印象。R2 正确指出 §5.1 的三层分解停留在概念层面。

但我对 R2 的结论有一个重要修正：ρ≈0.997 不能否定 31% DIF 的重要性。论文定位为 psychometric audit，而非 ranking correction tool。31% 的 items 在不同时间段对不同 cohort 产生不同的测量含义，这本身就是 measurement validity 问题——即使最终排名不变，也意味着排名的 evidential basis 发生了变化。类比：两次考试分数相同但考的内容实质不同，结果可比但过程不可比。

R2 的建议（a）提供具体 case study 非常好——Figure 4 中 Llama-3 +53 positions 和 phi-3 +809 positions 已经暗示了这种问题，但需要完整叙述一个 "practitioner 因忽略 DIF 得出错误结论" 的 worked example。R2 的建议（b）将 "instability" 改为 "measurement heterogeneity" 值得采纳——后者更精确，也避免了与 ρ≈0.997 的表面矛盾。

**[AGREE] R2-N2: 归因缺口限制审计协议可操作性**

完全同意，且与我的 W5 一致。补充一点 R2 未提到的：§5.3 的 15%/25% 阈值声称 "adapt ETS practice"，但 ETS 的阈值体系是为教育公平性（group fairness across demographics）设计的，其中 "investigate" 意味着检查 item 是否对特定人群不公平，有明确的 follow-up protocol（item bias review panel）。迁移到 LLM 场景后，"investigate" 的对象和方法完全不同——论文需要为 LLM benchmark maintainer 提供具体的 investigation 流程，而非仅借用 ETS 的数字标准。

R2 建议（a）"模拟 C% 多高时 ρ 显著下降"是非常好的实证方向——这能直接将 DIF threshold 与 practitioner-relevant outcome（ranking stability）挂钩。

---

### Should-Fix

**[REBUT] R2-W1: Cross-subject matching 新颖性声明需更谨慎**

部分不同意。R2 正确指出 external/subtest matching 在教育测量文献中已有成熟实践（Nandakumar 1993, purified matching）。但 R2 低估了 LLM 场景下的适配贡献：

1. 教育测量中的 purified subtest matching 主要用于消除 item-level bias（在同一测试内部），而本文的 cross-subject matching 是用 **完全不同 benchmark（GSM8K）的总分** 作为 matching variable——这在概念上不同于 subtest purification，因为 matching variable 来自完全不同的 construct space。
2. Remark（Zero FPR under single-subject matching）虽然 "by construction" 成立，但将其形式化并验证（§4.5, Table 5 的 multi-subject degradation）为 LLM evaluation 社区提供了可直接使用的实践指南。
3. 教育测量中不存在 "cross-subject contamination" 这一特有挑战——人类考生不会因为接触了某科目的考试内容而在其他科目上获得不对称优势。这一应用场景是本文独有的。

不过，我同意论文应更明确承认 purified matching 的先驱地位，将贡献重新定位为 "将 purified matching 原则适配到 LLM benchmark contamination 场景，并形式化其 FPR 保证" 而非暗示全新方法。

**[AGREE] R2-W2: \enlargethispage 格式操纵**

同意。如果论文使用了 `\enlargethispage{6\baselineskip}`，这确实过于激进。§4.2 的 permutation test 细节（null C%=0.10%±0.12%, p<0.001）完全可以压缩为一句话并移入附录，腾出空间。

**[AGREE] R2-W3: Growing Pains 对比不完整**

同意。论文可以在不访问 Growing Pains 数据的前提下做概念层面的对比：FPC 假设存在 stable anchor items 用于等值化，而本文发现 31% 的 items 跨时期不稳定——这直接挑战了 FPC 的前提假设。这种概念张力值得 1-2 句话讨论。

**[AGREE] R2-W4: Semi-synthetic injection 现实性**

完全同意，与我的 N2 一致。Binary flipping 是最极端的 uniform exploitation pattern。R2 建议的 "ability-dependent exploitation rate" 是一个很好的更现实注入模式——高能力模型可能更容易记忆训练数据，导致 non-uniform DIF。如果此注入模式下 MH-DIF 的检测力显著下降，这会实质性改变论文的实践结论。

**[REBUT] R2-W5: 缺少 polytomous DIF 讨论**

部分不同意。Polytomous DIF（如 generalized MH、Liu-Agresti cumulative common log-odds ratio）确实与 LLM 评测的未来方向相关（open-ended generation），但本文明确聚焦于 binary response 的 MMLU（multiple-choice, 0/1 scoring），且 Limitations 已提及 "binary response" 限制。要求在 Related Work 中覆盖 polytomous DIF 文献，超出了本文的 scope——这更适合作为 future work 的一句话提及，而非 Related Work 的系统覆盖。

---

### 小问题

**[AGREE] R2-M1**: "z = −8σ to −49σ" 确实不标准。z-score 无量纲，应写 "z = −8 to −49" 或 "8 to 49 standard deviations below the null mean"。

**[AGREE] R2-M2**: Table 1 的 "FPR" 列与 §3.4 的 ΔFPR 确实是不同概念——前者是 empirical cohort comparison 中的 false positive rate，后者是 semi-synthetic injection 中 injection 引入的 FPR 增量。论文应在 Table 1 注脚中明确 FPR 的定义。

**[AGREE] R2-M3**: Bootstrap CI [29.4%, 38.1%] 右偏的解释可以更清楚。"heavy-tailed C% from subjects exceeding 40%" 不够直观——建议说明是 subject-level resampling 导致高 C% subjects 被过度抽样时拉高整体 C%。

**[AGREE] R2-M4**: Figure 2 上下面板格式一致性问题——确认同意。

**[AGREE] R2-M5**: Table 1 中 Llama-2 vs Llama-3 行的 FPR/Enrichment 列为 "--" 确实缺少注释。可能因为这是 within-family comparison 而非 temporal comparison，没有对应的 ground truth labels 计算 enrichment——但需要在表注中说明。

**[AGREE] R2-M6**: 匿名规则维持良好。

---

### 叙事一致性评估

**[AGREE]** "measurement heterogeneity" 确实比 "instability" 更精准。"Instability" 暗示 benchmark 不可靠，但 ρ≈0.997 说明对 ranking 而言它是可靠的——问题在于 31% 的 items 对不同 cohort 的测量含义不同，这是 heterogeneity 而非 instability。

**[AGREE]** §4.2 section title "31% Measurement Instability" 与 "diagnostic, not destructive" 定位不完全一致。建议改为 "31% Measurement Heterogeneity" 或 "31% Differential Item Functioning"。

**[AGREE]** 三层框架（impact / DIF / attribution）在 §5.1 首次引入但 Experiments（§4）未使用——如果将此框架前移到 §3 并在 §4 中系统使用（每个实验结果对应哪一层），论文结构会更 coherent。

---

### 缺失参考文献

**[REBUT]** Swaminathan & Rogers (1990): 论文已在 Appendix A.1 引用此文（"logistic regression DIF (Swaminathan and Rogers, 1990)"）。R2 可能希望在 purified subtest matching 的语境下引用，但 Swaminathan & Rogers (1990) 的核心贡献是 logistic regression DIF 而非 purified matching——purified matching 的主要参考应为 Holland & Thayer (1988) 的 iterative purification procedure，论文已引用。

**[AGREE]** Hardy et al. (2026) scalability coefficients 的可获取性需要确认——如果是 preprint 或未正式发表，应标注状态。

---

### 总结

R2 的审稿整体高质量。最有价值的两个 insight 是：(1) ρ≈0.997 与 "instability" 叙事的张力（N1），这是论文目前最大的 framing 问题；(2) 审计协议的可操作性缺口（N2），与我的独立评估一致。

R2 给出 Excitement 3/5 并评论 "现有方法应用到新领域" 框架限制兴奋度——我对此有不同看法。论文的兴奋度不在于方法本身的新颖性，而在于 empirical findings 的启示性（ground truth meta-critique 颠覆了 contamination detection 领域的基本假设；31% DIF 首次量化了 temporal comparability 问题的规模）。类比 BERTScore 不是 embedding 技术的新颖性而是应用洞察。我维持 Excitement 3.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-22T03:38:26.098247+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-22T03:38:26.098803+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-22T03:38:26.852408+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool call

_source line 463 · 2026-05-22T03:38:26.852915+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 464 · 2026-05-22T03:38:26.954135+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T03:25:24.277371+00:00\", \"completed_at\": \"2026-05-22T03:27:25.397515+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3-5\", \"message\": \"Related Work 到 Method 前半段连续约 3 页无 figure/table，第 3 页纯散文无任何视觉元素。第 4-5 页有公式缓解，但审稿人翻过这段时视觉节奏偏平\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 正文字号偏小（尤其表体数字），正常打印尺寸下可读但吃力。Table 2（p7）同样偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 4 与 Figure 5 之间有约 1/4 页空白，可通过调整 figure 尺寸或 vspace 收紧\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 5 数据点标签密集有部分重叠（如左下角区域），缩小后可读性边缘\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Discussion + Conclusion + Limitations 起始全部挤在一页，section 转换密集——空间利用率高但阅读节奏快\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 两个子面板（TPR/FPR vs. exploitation ratio）尺寸偏小，axis label 在正常阅读距离下勉强可读\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-22T03:38:26.954616+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-22T03:40:57.545098+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 10 (Fresh review, 2026-05-22)\n# R1: 3.5, R2: 3.5 → Consensus 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"因果归因空白使 audit protocol 不可安全执行\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 10\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"问题范围扩大：不仅是 causal language，更根本的是 31% DIF 可能主要反映 genuine capability change。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"再次独立提出（R1-W3, R2-W2）。核心矛盾：§5.3 建议 'rotate or retire flagged items'，但 §4.6 显示 DIF items 集中 discriminative signal（z=-8σ to -49σ）。两位共识：retire = 移除最有信息量的 items。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 + R1-W5 独立提出。§5.3 已改为 'investigate and report alongside stable-item rankings'，但 'investigate' 缺乏具体可执行步骤。15%/25% 阈值从 ETS 迁移缺乏 LLM 场景实证依据。两位共识。\"\n  action_items:\n    - round: 10\n      action: \"为 audit protocol 每个 action level 提供具体可执行步骤；基于模拟分析确定阈值（如 C% 多高时 ρ 显著下降）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox——'instability' 叙事被排名保持所削弱\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"需更强调 family-level 和 pairwise 层面影响。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"共识：需 (1) 所有 6 benchmark ρ 值；(2) family-level rank profiles 到正文；(3) pairwise flip rate；(4) item 冗余度讨论。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N1 + R1 AGREE。Table 3 已增加 ρ/τ/flip rate，但缺乏具体 case study 论证 'practitioners 为何应关心不影响排名的 instability'。R1 建议将 'instability' 改为 'measurement heterogeneity'——两位共识。\"\n  action_items:\n    - round: 10\n      action: \"提供 1-2 个 worked example（如特定模型在 full vs stable items 排名差异导致的决策影响）；考虑将 'instability' 改为 'measurement heterogeneity'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R10-W1\"\n  summary: \"LLM examinee 非独立性对 MH χ² 统计推断的影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 首提（W2），R2 AGREE。经验处理充分但缺乏理论框架。建议引用 French & Finch (2010)。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N1（升级为 critical），R2 AGREE 但补充效应量极大（174×）不可被方法论瑕疵解释掉。共识：需 (1) 报告 family 数量及 size 分布；(2) cluster-robust permutation test；(3) cluster bootstrap CI。French & Finch (2010) 已引用。De-duplication K=20→C%=29.1% 有信息量但不充分。\"\n  action_items:\n    - round: 10\n      action: \"报告 model family 数量及 size 分布；做 cluster-robust permutation test 和 cluster bootstrap 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic binary flipping 生态效度——ΔTPR 为 upper bound\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"共识 strong Should-Fix。需明确 ΔTPR 为 upper-bound。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"论文已在 Limitations 和 §3.4 标注。需更明确区分 ΔFPR（matching 性质）vs ΔTPR（upper bound）。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2 AGREE。§3.4 末段有 'upper-bound estimates' 但 Abstract 和 §4.5 首次报告处仍无限定词。共识：Abstract 需加 'under worst-case uniform injection'，§4.5 需加 'upper-bound/ceiling estimate'。低注入率 p<0.3 检测力未报告（R1-W6, R2 AGREE）。\"\n  action_items:\n    - round: 10\n      action: \"Abstract + §4.5 首次报告处加 upper-bound 限定；补充 p∈{0.05,0.1,0.2} 的 ΔTPR 或讨论低注入率局限\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"\\\\enlargethispage 格式操作过于激进\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"discussion.tex 使用 18 行额外空间。需压缩 Discussion 使内容自然 fit 在 8 页内。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"已从 18→6 baselineskip，但两位仍认为过于激进。建议压缩冗余内容（如 §4.2 permutation details 移入附录）。\"\n  action_items:\n    - round: 10\n      action: \"压缩正文冗余内容使 \\\\enlargethispage 降至 ≤2 或消除\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"ΔFPR=0.000 在 Abstract 中缺乏 multi-subject contamination 限定\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1, R2 AGREE。Abstract 写 'achieves zero false positive inflation' 但仅在 single-subject contamination 下成立。k≤5 时 ΔFPR≤0.007，k=10 时升至 0.047。\"\n  action_items:\n    - round: 10\n      action: \"Abstract 中 ΔFPR=0.000 加限定 'under single- to few-subject contamination'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MF3\"\n  summary: \"Within-subject C%=38.1% 高于主分析 31.3%，需报告分布并解释差异\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Per-subject 分析理应更 clean 但反而更高。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-Q3 再次追问。需报告 5 个 subject 各自的 C% 分布。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W3, R2 AGREE。C% 范围 31.1-45.2%（5 subjects）已在 §4.4 报告，但未连接 Q3 local dependence（11.3% within-subject pairs > |Q3|>0.20）作为 inflation 原因。R2 判断 cross-subject matching 的 31.3% 更可靠。\"\n  action_items:\n    - round: 10\n      action: \"明确论证 within-subject C% 较高部分源于 local dependence inflation，cross-subject 的 31.3% 更可靠\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"与 Growing Pains (Habba et al. 2026) 的概念对比不完整\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W3, R1 AGREE。'Empirical comparison awaits public release' 留下空白。FPC 假设 anchor items 稳定 vs 本文发现 31% 不稳定——这一概念张力值得讨论。\"\n  action_items:\n    - round: 10\n      action: \"在 Discussion 或 Related Work 中增加 FPC 前提假设与 31% instability 的概念张力讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W4\"\n  summary: \"Monte Carlo power analysis 依赖 poor-fit 2PL 参数——需明确标注为近似估计\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N3（critical），R2 partially rebuts 降级为 warning。论文 triangulation 合理但应在 §4.1 明确标注 'approximate parametric bounds'，以 semi-synthetic injection 为主要 power evidence。\"\n  action_items:\n    - round: 10\n      action: \"§4.1 开头加明确标注：Monte Carlo 为 approximate parametric bounds，empirical validation 见 §4.5\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限——cross-subject matching 有 DIF 文献先例\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 首提（W3），R1 REBUT（ARR H14）。两位均同意更突出 C2（meta-critique）可加强论文。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W1, R1 REBUT（LLM-specific adaptation 非 trivial）。共识：承认 purified matching 先驱，将贡献定位为 'LLM 场景适配 + FPR 保证形式化' 而非全新方法。Remark 重新定位为设计选择及其性质。\"\n  action_items:\n    - round: 10\n      action: \"Contribution 2 措辞调整：承认先例，定位为 LLM-specific adaptation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K N=33 应严格标注为 exploratory\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"移至 Appendix 并标注 preliminary\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"论文已标注 exploratory。确保 Abstract 不暗示 GSM1K 结果为 confirmed finding。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-Q5 追问 95% CI。N=33 时 r=-0.478 的 CI 约 [-0.71, -0.16]，宽度 0.55。论文 Limitations 已标注 exploratory。\"\n  action_items:\n    - round: 10\n      action: \"确认 Abstract 不引用 GSM1K；Appendix 补充 r 的 95% CI\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO ISSUES\n# ============================================================\n\n- id: \"R10-I1\"\n  summary: \"z = −8σ to −49σ 记号不标准\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两位共识。应写 'z = −8 to −49' 或 '8 to 49 standard deviations'。\"\n\n- id: \"R10-I2\"\n  summary: \"Table 1 'FPR' 列与 §3.4 的 ΔFPR 概念不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两位共识。Table 1 脚注应明确 FPR 定义。\"\n\n- id: \"R10-I3\"\n  summary: \"Table 1 Llama-2 vs Llama-3 行 FPR/Enrichment 为 '--' 未注释原因\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两位共识。需在表注中说明原因（within-family 无对应 ground truth）。\"\n\n- id: \"R8-SF10\"\n  summary: \"置换检验仅 200 次洗牌，分辨率有限\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"200 次最小 p=0.005 恰是报告值\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两位共识降为 info 级别。per-subject 1000 perm 结果一致。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"本轮未再单独提出，保持 info。\"\n\n# ============================================================\n# RESOLVED ISSUES\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2（200 shuffles, null C%=0.10%±0.12%, p=0.005）+ per-subject 1000 perm\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'，全文 drift→instability。Round 10 R1 建议进一步改为 'heterogeneity'。\"\n  resolution_round: 9\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"已降格为 Remark（§3.4）。Round 10 R2 仍认为是 by-construction 结论而非理论贡献，但 R1 辩护 LLM 场景适配非 trivial。\"\n  resolution_round: 9\n\n- id: \"R8-SF4\"\n  summary: \"Table 2 列名 'Temp. FPR' 误导\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"已改为 'Temp. C%'。\"\n  resolution_round: 9\n\n- id: \"R8-SF7\"\n  summary: \"Logistic regression model specification 未完整报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix A.1 已补充完整 logistic regression specification。\"\n  resolution_round: 9\n\n- id: \"R8-SF8\"\n  summary: \"Power analysis 参数 sensitivity 未展示\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Appendix Table 4 展示 TPR=f(a) + §4.1 Jensen's inequality insight。\"\n  resolution_round: 9\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 缺乏深入概念对比\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Related Work 已扩展 Growing Pains FPC 对比。Round 10 仍要求更深入概念讨论（R10-W3）。\"\n  resolution_round: 9\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI 忽略家族内相关性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Limitations 已 acknowledge family correlation + graduated de-duplication K=20 (C%=29.1%)。Round 10 要求进一步做 cluster bootstrap。\"\n  resolution_round: 9\n\n- id: \"R8-MISS-REF\"\n  summary: \"缺少引用：Oren 2024, Deng 2024, MMLU-Pro, MMLU-Redux\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"All 4 references added.\"\n  resolution_round: 9\n\n- id: \"R6-W1\"\n  summary: \"IRT model fit statistics 未报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix A.2 reports poor fit + method.tex notes MH-DIF is non-parametric\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"Multi-subject injection 结果展示过于压缩\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 added to Appendix C with full k-sweep data\"\n  resolution_round: 8\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing——DIF and contamination measure different constructs\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Section 5.2 adequately frames the construct distinction\"\n  resolution_round: 8\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n\n- id: \"R2-N2-resolved\"\n  summary: \"Novelty 论证不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  resolution: \"LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。\"\n  resolution_round: 6\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (LD×DIF)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50). MH non-parametric.\"\n  resolution_round: 4\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]. Structural guarantee.\"\n  resolution_round: 4\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n\n- id: \"MISSING-REF-1\"\n  summary: \"引用问题（Round 1-7）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 7\n  resolution: \"Verified: all 51 bib entries properly cited. Zero orphans.\"\n  resolution_round: 7\n\n- id: \"R9-MISS-REF\"\n  summary: \"缺少引用：French & Finch (2010), Kolen & Brennan (2014)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Both references added to bib and cited in text.\"\n  resolution_round: 10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Round 10 (Fresh review, 2026-05-22)\n# R1: 3.5, R2: 3.5 → Consensus 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"因果归因空白使 audit protocol 不可安全执行\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 10\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"问题范围扩大：不仅是 causal language，更根本的是 31% DIF 可能主要反映 genuine capability change。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"再次独立提出（R1-W3, R2-W2）。核心矛盾：§5.3 建议 'rotate or retire flagged items'，但 §4.6 显示 DIF items 集中 discriminative signal（z=-8σ to -49σ）。两位共识：retire = 移除最有信息量的 items。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 + R1-W5 独立提出。§5.3 已改为 'investigate and report alongside stable-item rankings'，但 'investigate' 缺乏具体可执行步骤。15%/25% 阈值从 ETS 迁移缺乏 LLM 场景实证依据。两位共识。\"\n  action_items:\n    - round: 10\n      action: \"为 audit protocol 每个 action level 提供具体可执行步骤；基于模拟分析确定阈值（如 C% 多高时 ρ 显著下降）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 practical significance paradox——'instability' 叙事被排名保持所削弱\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"需更强调 family-level 和 pairwise 层面影响。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"共识：需 (1) 所有 6 benchmark ρ 值；(2) family-level rank profiles 到正文；(3) pairwise flip rate；(4) item 冗余度讨论。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N1 + R1 AGREE。Table 3 已增加 ρ/τ/flip rate，但缺乏具体 case study 论证 'practitioners 为何应关心不影响排名的 instability'。R1 建议将 'instability' 改为 'measurement heterogeneity'——两位共识。\"\n  action_items:\n    - round: 10\n      action: \"提供 1-2 个 worked example（如特定模型在 full vs stable items 排名差异导致的决策影响）；考虑将 'instability' 改为 'measurement heterogeneity'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES\n# ============================================================\n\n- id: \"R10-W1\"\n  summary: \"LLM examinee 非独立性对 MH χ² 统计推断的影响\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 首提（W2），R2 AGREE。经验处理充分但缺乏理论框架。建议引用 French & Finch (2010)。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N1（升级为 critical），R2 AGREE 但补充效应量极大（174×）不可被方法论瑕疵解释掉。共识：需 (1) 报告 family 数量及 size 分布；(2) cluster-robust permutation test；(3) cluster bootstrap CI。French & Finch (2010) 已引用。De-duplication K=20→C%=29.1% 有信息量但不充分。\"\n  action_items:\n    - round: 10\n      action: \"报告 model family 数量及 size 分布；做 cluster-robust permutation test 和 cluster bootstrap 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic binary flipping 生态效度——ΔTPR 为 upper bound\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"共识 strong Should-Fix。需明确 ΔTPR 为 upper-bound。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"论文已在 Limitations 和 §3.4 标注。需更明确区分 ΔFPR（matching 性质）vs ΔTPR（upper bound）。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2 AGREE。§3.4 末段有 'upper-bound estimates' 但 Abstract 和 §4.5 首次报告处仍无限定词。共识：Abstract 需加 'under worst-case uniform injection'，§4.5 需加 'upper-bound/ceiling estimate'。低注入率 p<0.3 检测力未报告（R1-W6, R2 AGREE）。\"\n  action_items:\n    - round: 10\n      action: \"Abstract + §4.5 首次报告处加 upper-bound 限定；补充 p∈{0.05,0.1,0.2} 的 ΔTPR 或讨论低注入率局限\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"\\\\enlargethispage 格式操作过于激进\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"discussion.tex 使用 18 行额外空间。需压缩 Discussion 使内容自然 fit 在 8 页内。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"已从 18→6 baselineskip，但两位仍认为过于激进。建议压缩冗余内容（如 §4.2 permutation details 移入附录）。\"\n  action_items:\n    - round: 10\n      action: \"压缩正文冗余内容使 \\\\enlargethispage 降至 ≤2 或消除\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"ΔFPR=0.000 在 Abstract 中缺乏 multi-subject contamination 限定\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1, R2 AGREE。Abstract 写 'achieves zero false positive inflation' 但仅在 single-subject contamination 下成立。k≤5 时 ΔFPR≤0.007，k=10 时升至 0.047。\"\n  action_items:\n    - round: 10\n      action: \"Abstract 中 ΔFPR=0.000 加限定 'under single- to few-subject contamination'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-MF3\"\n  summary: \"Within-subject C%=38.1% 高于主分析 31.3%，需报告分布并解释差异\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Per-subject 分析理应更 clean 但反而更高。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-Q3 再次追问。需报告 5 个 subject 各自的 C% 分布。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W3, R2 AGREE。C% 范围 31.1-45.2%（5 subjects）已在 §4.4 报告，但未连接 Q3 local dependence（11.3% within-subject pairs > |Q3|>0.20）作为 inflation 原因。R2 判断 cross-subject matching 的 31.3% 更可靠。\"\n  action_items:\n    - round: 10\n      action: \"明确论证 within-subject C% 较高部分源于 local dependence inflation，cross-subject 的 31.3% 更可靠\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"与 Growing Pains (Habba et al. 2026) 的概念对比不完整\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W3, R1 AGREE。'Empirical comparison awaits public release' 留下空白。FPC 假设 anchor items 稳定 vs 本文发现 31% 不稳定——这一概念张力值得讨论。\"\n  action_items:\n    - round: 10\n      action: \"在 Discussion 或 Related Work 中增加 FPC 前提假设与 31% instability 的概念张力讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W4\"\n  summary: \"Monte Carlo power analysis 依赖 poor-fit 2PL 参数——需明确标注为近似估计\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N3（critical），R2 partially rebuts 降级为 warning。论文 triangulation 合理但应在 §4.1 明确标注 'approximate parametric bounds'，以 semi-synthetic injection 为主要 power evidence。\"\n  action_items:\n    - round: 10\n      action: \"§4.1 开头加明确标注：Monte Carlo 为 approximate parametric bounds，empirical validation 见 §4.5\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"方法新颖性有限——cross-subject matching 有 DIF 文献先例\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 首提（W3），R1 REBUT（ARR H14）。两位均同意更突出 C2（meta-critique）可加强论文。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W1, R1 REBUT（LLM-specific adaptation 非 trivial）。共识：承认 purified matching 先驱，将贡献定位为 'LLM 场景适配 + FPR 保证形式化' 而非全新方法。Remark 重新定位为设计选择及其性质。\"\n  action_items:\n    - round: 10\n      action: \"Contribution 2 措辞调整：承认先例，定位为 LLM-specific adaptation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K N=33 应严格标注为 exploratory\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"移至 Appendix 并标注 preliminary\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"论文已标注 exploratory。确保 Abstract 不暗示 GSM1K 结果为 confirmed finding。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-Q5 追问 95% CI。N=33 时 r=-0.478 的 CI 约 [-0.71, -0.16]，宽度 0.55。论文 Limitations 已标注 exploratory。\"\n  action_items:\n    - round: 10\n      action: \"确认 Abstract 不引用 GSM1K；Appendix 补充 r 的 95% CI\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO ISSUES\n# ============================================================\n\n- id: \"R10-I1\"\n  summary: \"z = −8σ to −49σ 记号不标准\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两位共识。应写 'z = −8 to −49' 或 '8 to 49 standard deviations'。\"\n\n- id: \"R10-I2\"\n  summary: \"Table 1 'FPR' 列与 §3.4 的 ΔFPR 概念不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两位共识。Table 1 脚注应明确 FPR 定义。\"\n\n- id: \"R10-I3\"\n  summary: \"Table 1 Llama-2 vs Llama-3 行 FPR/Enrichment 为 '--' 未注释原因\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"两位共识。需在表注中说明原因（within-family 无对应 ground truth）。\"\n\n- id: \"R8-SF10\"\n  summary: \"置换检验仅 200 次洗牌，分辨率有限\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"200 次最小 p=0.005 恰是报告值\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两位共识降为 info 级别。per-subject 1000 perm 结果一致。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"本轮未再单独提出，保持 info。\"\n\n# ============================================================\n# RESOLVED ISSUES\n# ============================================================\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"Permutation null 已补充到 §4.2（200 shuffles, null C%=0.10%±0.12%, p=0.005）+ per-subject 1000 perm\"\n  resolution_round: 8\n\n- id: \"R8-MF2\"\n  summary: \"'Drift' framing 超出数据支撑\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Title 改为 'Temporal Measurement Instability'，全文 drift→instability。Round 10 R1 建议进一步改为 'heterogeneity'。\"\n  resolution_round: 9\n\n- id: \"R8-SF1\"\n  summary: \"Proposition 1 过度形式化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"已降格为 Remark（§3.4）。Round 10 R2 仍认为是 by-construction 结论而非理论贡献，但 R1 辩护 LLM 场景适配非 trivial。\"\n  resolution_round: 9\n\n- id: \"R8-SF4\"\n  summary: \"Table 2 列名 'Temp. FPR' 误导\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"已改为 'Temp. C%'。\"\n  resolution_round: 9\n\n- id: \"R8-SF7\"\n  summary: \"Logistic regression model specification 未完整报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix A.1 已补充完整 logistic regression specification。\"\n  resolution_round: 9\n\n- id: \"R8-SF8\"\n  summary: \"Power analysis 参数 sensitivity 未展示\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"Appendix Table 4 展示 TPR=f(a) + §4.1 Jensen's inequality insight。\"\n  resolution_round: 9\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 缺乏深入概念对比\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Related Work 已扩展 Growing Pains FPC 对比。Round 10 仍要求更深入概念讨论（R10-W3）。\"\n  resolution_round: 9\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI 忽略家族内相关性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Limitations 已 acknowledge family correlation + graduated de-duplication K=20 (C%=29.1%)。Round 10 要求进一步做 cluster bootstrap。\"\n  resolution_round: 9\n\n- id: \"R8-MISS-REF\"\n  summary: \"缺少引用：Oren 2024, Deng 2024, MMLU-Pro, MMLU-Redux\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"All 4 references added.\"\n  resolution_round: 9\n\n- id: \"R6-W1\"\n  summary: \"IRT model fit statistics 未报告\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Appendix A.2 reports poor fit + method.tex notes MH-DIF is non-parametric\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"Multi-subject injection 结果展示过于压缩\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"Table 4 added to Appendix C with full k-sweep data\"\n  resolution_round: 8\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing——DIF and contamination measure different constructs\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Section 5.2 adequately frames the construct distinction\"\n  resolution_round: 8\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n\n- id: \"R2-N2-resolved\"\n  summary: \"Novelty 论证不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  resolution: \"LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。\"\n  resolution_round: 6\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (LD×DIF)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50). MH non-parametric.\"\n  resolution_round: 4\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]. Structural guarantee.\"\n  resolution_round: 4\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n\n- id: \"MISSING-REF-1\"\n  summary: \"引用问题（Round 1-7）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 7\n  resolution: \"Verified: all 51 bib entries properly cited. Zero orphans.\"\n  resolution_round: 7\n\n- id: \"R9-MISS-REF\"\n  summary: \"缺少引用：French & Finch (2010), Kolen & Brennan (2014)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Both references added to bib and cited in text.\"\n  resolution_round: 10"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-22T03:40:57.646241+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 15615}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-22T03:43:39.179222+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "report": "# 审稿报告 — Round 10 (Fresh Review)\n\n**论文**: *Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models*\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**投稿类别**: Long Paper\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）\n**圆桌轮次**: 1 轮（Round 1 + 交叉分享，关键问题达成共识）\n\n---\n\n## Summary\n\n论文将教育测量中的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 分析应用于 LLM 基准评测，基于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）发现 31.3% 的 MMLU 题目在 2023 vs 2024 模型之间存在 ETS Category C 级别的 temporal DIF。三大贡献：(1) ground truth meta-critique——web-overlap 污染标签与 DIF flags 近乎独立（enrichment≈0.96, φ=0.012）；(2) cross-subject matching 实现 ΔFPR=0.000 的 semi-synthetic validation framework；(3) 跨 6 个基准的 temporal measurement instability（C% = 17.9-31.3%，45-174× above random baseline）。排名高度保持（ρ≈0.997, τ≈0.958, flip rate ≤2.8%）。\n\n---\n\n## Strengths\n\n**S1. 分析规模和系统性**：5,227 模型 × 12,508 MMLU 题目，扩展到 6 个 METABENCH 基准（共 27,125 题目），是 LLM 基准领域最大规模的测量不变性审计。5 种 cohort designs（temporal / ability-quintile / within-family / within-subject / random split）+ 3 种 structural controls（matched-ability / IRT θ-conditioning / within-subject DIF）形成多路径 converging evidence。[R1, R2 共识]\n\n**S2. Ground truth meta-critique 概念贡献突出**：证明 web-overlap contamination labels 与 DIF flags 近乎独立（enrichment=0.964, φ=0.012, OR=1.05 [0.96, 1.15], p=0.258），揭示污染检测领域的验证方法论漏洞——global exposure ≠ differential functioning。对所有使用 web-overlap labels 作为 ground truth 的 contamination detection 工作有直接指导意义。[R1 + R2 一致认为是本文最有价值的贡献]\n\n**S3. 跨基准复制增强可信度**：6 个基准一致发现 17.9-31.3% temporal DIF，且 knowledge/reasoning 基准（C%≥26.9%）系统性高于 procedural 基准（C%≤18.9%），不是单一数据集偶然。[R2]\n\n**S4. \"that\" not \"why\" 认识论定位贯穿全文**：论文对因果归因保持良好克制，没有将 DIF detection 过度解读为 contamination detection。Limitations 坦诚承认归因缺口、非独立样本、二值注入非现实性。[R1, R2]\n\n**S5. 可复现性高**：匿名代码仓库、METABENCH 数据公开、方法描述清晰完整、附录包含充分实验细节。[R2: Reproducibility 4/5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. ρ≈0.997 与 \"31% instability\" 的叙事张力未解决** [R2-N1, R1 AGREE]\n- 论文核心主张是 31.3% 题目存在 temporal DIF，但排名高度保持（ρ≈0.997）。\"diagnostic, not destructive\" 定位合理，但论文未令人信服论证 practitioners 为何应关心不影响排名的 instability。§5.1 三层分解停留概念层面，缺乏\"忽略 DIF 会导致什么具体错误\"的实证案例。§4.6 的 Llama-3 +53 / Mistral -35 说明 DIF items 包含家族特异性信号，但非\"忽略 DIF 导致错误决策\"的论证。\n- R1 补充：ρ≈0.997 不否定 31% DIF 的重要性——排名相同但 evidential basis 不同（两次考试分数相同但考的内容实质不同）。但论文需要用 worked example 而非类比来论证。\n- **建议**：(a) 提供 1-2 个具体 worked example；(b) 考虑将 \"instability\" 改为 \"measurement heterogeneity\"——后者更精确，避免与 ρ≈0.997 的表面矛盾。[两位共识]\n\n**MF2. 归因缺口限制审计协议可操作性** [R2-N2, R1-W5, 两位共识]\n- §5.3 \"Act (C%≥25%)\" 建议 \"investigate flagged items\"——但 DIF 只检测 THAT 不解释 WHY，investigate for what？15%/25% 阈值声称 \"adapt ETS practice\"，但 ETS 阈值是为教育公平性（demographic fairness）设计的，有明确 follow-up（item bias review panel）。迁移到 LLM 场景后 \"investigate\" 对象和方法完全不同。\n- **建议**：(a) 基于模拟分析确定阈值（C% 多高时 ρ 显著下降）；(b) 为每个 action level 提供具体可执行步骤（item content review / cross-reference contamination sources / report stable-item rankings as sensitivity analysis）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. LLM examinee 非独立性对统计推断的影响** [R1-N1, R2 AGREE]\n- 5,227 模型包含大量 fine-tune variants，MH χ² 有效样本量远小于名义值。Permutation test（shuffling non-independent units）和 bootstrap CI 同受影响。De-duplication K=20 → C%=29.1% 有信息量但不充分。\n- R2 缓解：效应量极大（174×），31.3% 是描述性统计量不依赖 χ² 显著性，不会因非独立性\"消失\"。真正受影响的是每个 item 的 MH χ² 显著性和 CI 宽度。\n- **建议**：(1) 报告 model family 数量及 size 分布；(2) cluster-robust permutation test 对比；(3) cluster bootstrap CI。\n\n**SF2. ΔTPR 应在主文所有首次引用处标注为 upper-bound** [R1-N2, R2 AGREE]\n- Binary response flipping 是最极端的 uniform exploitation。§3.4 末段有 \"upper-bound estimates\" 但 Abstract 和 §4.5 首次报告处无限定。低注入率（p<0.3）检测力未报告，real contamination 可能对应 p=0.05-0.2。\n- **建议**：Abstract 加 \"under worst-case uniform injection\"；§4.5 加限定；补充 p∈{0.05, 0.1, 0.2} 数据或讨论局限。\n\n**SF3. ΔFPR=0.000 在 Abstract 中缺乏 multi-subject 限定** [R1-W1, R2 AGREE]\n- Abstract \"achieves zero false positive inflation\" 仅在 single-subject contamination 下成立。k≤5 时 ΔFPR≤0.007，k=10 时升至 0.047。\n- **建议**：Abstract 改为 \"achieves zero false positive inflation under single- to few-subject contamination (ΔFPR=0.000, k≤5)\"。\n\n**SF4. Within-subject C%=38.1% > temporal C%=31.3% 解释不充分** [R1-W3, R2 AGREE]\n- Within-subject DIF 高出 7pp，但未连接 Q3 local dependence（11.3% within-subject pairs > |Q3|>0.20）作为 inflation 原因。\n- **建议**：明确论证 within-subject C% 较高部分源于 local dependence inflation，cross-subject 的 31.3% 更可靠。\n\n**SF5. \\enlargethispage{6\\baselineskip} 格式操纵过于激进** [R2-W2, R1 AGREE]\n- 说明论文在 8 页限制下紧凑。§4.2 permutation test 细节可压缩移入附录。\n- **建议**：压缩冗余内容使 \\enlargethispage ≤2 或消除。\n\n**SF6. 与 Growing Pains (Habba et al. 2026) 概念对比不完整** [R2-W3, R1 AGREE]\n- \"Empirical comparison awaits public release\" 留空白。FPC 假设 anchor items 稳定 vs 本文发现 31% 不稳定——概念张力值得讨论。\n- **建议**：增加 1-2 句概念层面对比。\n\n**SF7. Monte Carlo power analysis 依赖 poor-fit 2PL 参数** [R1-N3, R2 partially rebuts → 降级为 Should-Fix]\n- §4.1 使用 2PL 参数但 MMLU poor fit to 2PL。论文 triangulation 合理，Appendix 已标注，但 §4.1 开头应更明确。\n- **建议**：§4.1 加 \"approximate parametric bounds\"，以 semi-synthetic injection 为主要 power evidence。\n\n### Nice-to-Have（不影响接收）\n\n- **N1**: \"z = −8σ to −49σ\" 记号不标准，应为 \"z = −8 to −49\"。[R2-M1, R1 AGREE]\n- **N2**: Table 1 \"FPR\" 列与 §3.4 ΔFPR 概念不一致，需脚注明确。[R2-M2, R1 AGREE]\n- **N3**: Table 1 Llama-2 vs Llama-3 行 FPR/Enrichment 为 \"--\" 未注释原因。[R2-M5, R1 AGREE]\n- **N4**: Bootstrap CI [29.4%, 38.1%] 右偏解释可更清晰。[R2-M3, R1 AGREE]\n- **N5**: Cross-subject matching 新颖性措辞可更谨慎——承认 purified matching 先例，定位为 LLM-specific adaptation。[R2-W1, R1 部分 REBUT 但同意调整措辞]\n- **N6**: Hardy et al. (2026) scalability coefficients 引用可获取性待验证。[R2, R1 AGREE]\n- **N7**: GSM1K r=-0.478 应补充 95% CI（约 [-0.71, -0.16]）。[R1-Q5]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Ground truth meta-critique 是最有价值的贡献**（R1 优势 3 = R2 S2）\n2. **ρ≈0.997 vs 31% instability 是最大叙事挑战**（R2-N1, R1 AGREE）\n3. **审计协议缺乏可操作性**（R2-N2 = R1-W5，两位独立提出）\n4. **ΔTPR 是 upper-bound**（R1-N2, R2-W4 独立提出同一关切）\n5. **LLM examinee 非独立性是最大方法论弱点**（R1-N1, R2 AGREE，但效应量极大部分缓解）\n6. **\"that\" not \"why\" 认识论定位贯穿全文——是论文 framing 最成功之处**\n7. **整体评分一致：3.5 Borderline Conference**\n\n---\n\n## Reviewer Divergence [REBUT / Partially REBUT]\n\n1. **R1-W4 统计 vs 实际显著性混淆**：R2 指出 R1 存在事实性错误——R1 将 φ=0.012 误读为 p=0.012，实际 p=0.258（未达统计显著性）。\"Near-independent\" 判断完全合理。**→ 撤回此 issue。**\n\n2. **R1-N3 Monte Carlo power analysis（critical vs warning）**：R1 评为 critical，R2 partially rebuts——论文 triangulation 合理且已在 Appendix 明确标注。**→ 共识降级为 Should-Fix**（SF7）。\n\n3. **R2-W1 Cross-subject matching 新颖性**：R2 认为有 DIF 文献先例，新颖性声明需谨慎。R1 反驳 LLM-specific adaptation 非 trivial（cross-subject contamination 是人类测试中不存在的挑战）。**→ 共识：承认先例但保留 LLM 适配贡献，调整措辞。**\n\n4. **R2-W5 Polytomous DIF 讨论**：R2 要求在 Related Work 覆盖。R1 反驳超出 scope（论文聚焦 binary response，Limitations 已提及）。**→ 共识：Limitations 中已有，不强制在 Related Work 扩展。**\n\n5. **Excitement 评分**：R1 给 3.5/5（empirical findings 启示性高），R2 给 3/5（\"现有方法应用到新领域\"限制兴奋度）。**→ 记录分歧，不影响整体评分。**\n\n---\n\n## Questions to Authors\n\n**Q1** [R1-Q1, R2 AGREE]: 5,227 模型中有多少个 distinct model families？Family size 分布（median, max）？Cluster-robust permutation test 下 C% 和 p-value 是否改变？\n\n**Q2** [R1-Q2]: Random split baseline（C%=0.18%）是 model-level 还是 family-level 随机分？如果 model-level 且同一 family 分到两边，baseline FPR 可能 underestimate。\n\n**Q3** [R1-Q4]: Cross-benchmark matching（MMLU total score → GSM8K items）——construct 不同是否引入 matching bias？这对 GSM8K 的 18.9% C% 有何影响？\n\n**Q4** [R1-W3, R2 AGREE]: Within-subject C%=38.1%（range 31.1-45.2%）vs temporal C%=31.3%——请明确论证哪个更可靠，以及 Q3 local dependence 对 within-subject DIF 的 inflation 贡献。\n\n**Q5** [R2-N1]: 能否提供 1-2 个 worked example，展示特定模型在 full MMLU vs stable-only items 排名差异可能导致的具体决策影响？\n\n**Q6** [R1-W6]: p<0.3 时 ΔTPR 如何？MH-DIF 在 low exploitation rate（p=0.05-0.2）下是否仍有可用检测力？\n\n**Q7** [R2-N2]: §5.3 审计协议阈值 15%/25% 的选择是否有实证依据？能否通过模拟确定\"C% 多高时 ρ 开始显著下降\"？\n\n---\n\n## Missing References\n\n- Hardy et al. (2026) scalability coefficients：已引用但可获取性待验证。[R2 提出]\n- Swaminathan & Rogers (1990) purified subtest matching 在 Related Work 中可补充引用（当前仅在 Appendix 出现）。[R2-W1, R1 认为 Holland & Thayer 1988 已覆盖]\n- Polytomous DIF 文献（generalized MH, Liu-Agresti）：不强制要求，Limitations 已提及方向。[R2-W5, R1 REBUT]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 1 warning, 5 info）：\n\n- **[warning]** Page 3-5：Related Work 到 Method 前半段连续约 3 页无 figure/table，视觉节奏偏平\n- **[info]** Page 6-7：Table 1, 2 字号偏小，正常打印下可读但吃力\n- **[info]** Page 7：Figure 2 两个子面板尺寸偏小，axis label 勉强可读\n- **[info]** Page 8：Discussion + Conclusion + Limitations 起始全挤在一页，section 转换密集\n- **[info]** Page 14：Figure 4-5 之间约 1/4 页空白；Figure 5 数据点标签密集有重叠\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 — Borderline Conference**（两位 Reviewer 一致）\n\n**置信度：4 / 5**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | — | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**判断依据**：\n\n技术执行扎实、规模宏大的实证研究。Ground truth meta-critique（web-overlap labels ⊥ DIF flags）是重要的概念贡献，31% temporal DIF 的跨 6 基准复制结果令人印象深刻。主要问题在于：\n\n1. **叙事张力**（MF1）：ρ≈0.997 的排名保持与 \"31% instability\" 主张之间缺乏令人信服的 practical significance 论证——这是论文从 Borderline 升至 Conference 的关键障碍。\n2. **审计协议可操作性**（MF2）：DIF 无法归因的前提下，audit protocol 的 action steps 过于模糊，阈值缺乏实证依据。\n3. **方法论新颖性有限**：MH-DIF 未修改，cross-subject matching 有 DIF 文献先例（尽管 LLM 场景适配非 trivial）。\n\n**如果有效解决 MF1（具体案例 + 叙事调整）和 MF2（可操作审计步骤），论文有望提升至 4.0 (Conference) 水平。**\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- ΔTPR=+0.508 需加 \"under worst-case uniform injection\" 限定\n- ΔFPR=0.000 需加 multi-subject contamination 限定\n- \"z = −8σ to −49σ\" 记号不标准\n- 总体信息密度高且准确，但缺少 practical significance 的 hook\n\n### Introduction (§1)\n- Figure 1 直观有效\n- \"diagnostic, not destructive\" 定位清晰\n- 三大贡献排序合理（R2 认为 meta-critique 最有价值，可考虑前移）\n- 脚注 1 匿名链接处理得当\n\n### Related Work (§2)\n- 四段结构清晰（Contamination / IRT / DIF / Benchmark Quality）\n- Growing Pains 对比可更深入（FPC 前提假设 vs 31% instability 的概念张力）\n- DIF 文献先例（purified matching）的引用可更明确\n- 总体覆盖较完整\n\n### Method (§3)\n- MH-DIF 和 ETS classification 解释清晰\n- LLM-specific challenges 段落有价值\n- Remark (Zero FPR) 是 by-construction 结论，建议定位为\"设计选择及其性质\"\n- Cross-subject matching 的三种策略描述清晰\n- Semi-synthetic injection 的 binary flipping 局限应在此处首次标注\n\n### Experiments (§4)\n- §4.1 Monte Carlo power analysis 应标注为 approximate parametric bounds\n- §4.2 \"31% Measurement Instability\" section title 与 \"diagnostic, not destructive\" 有张力\n- §4.3 Ground truth mismatch 是最强的 section\n- §4.4 Structural analysis 全面但 within-subject C% 解释需加强\n- §4.5 Semi-synthetic validation 缺少 p<0.3 数据\n- §4.6 Downstream impact 需 worked example 而非仅统计量\n- §4.7 Cross-benchmark validation 增强可信度，Table 3 信息丰富\n\n### Discussion (§5)\n- §5.1 三层框架（impact/DIF/attribution）好但仅在此引入——可前移到 §3 并在 §4 系统使用\n- §5.2 Ground truth meta-critique 讨论充分\n- §5.3 Audit protocol 是最弱的 section——阈值缺乏依据，action steps 模糊\n- \\enlargethispage{6\\baselineskip} 过于激进\n\n### Conclusion (§6)\n- 简洁恰当\n\n### Limitations\n- 覆盖 4 个方面（方法范围、样本非独立性、匹配边界、泛化性），长度恰当\n- 学术诚实值得肯定",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "report": "# 审稿报告 — Round 10 (Fresh Review)\n\n**论文**: *Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models*\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**投稿类别**: Long Paper\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）\n**圆桌轮次**: 1 轮（Round 1 + 交叉分享，关键问题达成共识）\n\n---\n\n## Summary\n\n论文将教育测量中的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 分析应用于 LLM 基准评测，基于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）发现 31.3% 的 MMLU 题目在 2023 vs 2024 模型之间存在 ETS Category C 级别的 temporal DIF。三大贡献：(1) ground truth meta-critique——web-overlap 污染标签与 DIF flags 近乎独立（enrichment≈0.96, φ=0.012）；(2) cross-subject matching 实现 ΔFPR=0.000 的 semi-synthetic validation framework；(3) 跨 6 个基准的 temporal measurement instability（C% = 17.9-31.3%，45-174× above random baseline）。排名高度保持（ρ≈0.997, τ≈0.958, flip rate ≤2.8%）。\n\n---\n\n## Strengths\n\n**S1. 分析规模和系统性**：5,227 模型 × 12,508 MMLU 题目，扩展到 6 个 METABENCH 基准（共 27,125 题目），是 LLM 基准领域最大规模的测量不变性审计。5 种 cohort designs（temporal / ability-quintile / within-family / within-subject / random split）+ 3 种 structural controls（matched-ability / IRT θ-conditioning / within-subject DIF）形成多路径 converging evidence。[R1, R2 共识]\n\n**S2. Ground truth meta-critique 概念贡献突出**：证明 web-overlap contamination labels 与 DIF flags 近乎独立（enrichment=0.964, φ=0.012, OR=1.05 [0.96, 1.15], p=0.258），揭示污染检测领域的验证方法论漏洞——global exposure ≠ differential functioning。对所有使用 web-overlap labels 作为 ground truth 的 contamination detection 工作有直接指导意义。[R1 + R2 一致认为是本文最有价值的贡献]\n\n**S3. 跨基准复制增强可信度**：6 个基准一致发现 17.9-31.3% temporal DIF，且 knowledge/reasoning 基准（C%≥26.9%）系统性高于 procedural 基准（C%≤18.9%），不是单一数据集偶然。[R2]\n\n**S4. \"that\" not \"why\" 认识论定位贯穿全文**：论文对因果归因保持良好克制，没有将 DIF detection 过度解读为 contamination detection。Limitations 坦诚承认归因缺口、非独立样本、二值注入非现实性。[R1, R2]\n\n**S5. 可复现性高**：匿名代码仓库、METABENCH 数据公开、方法描述清晰完整、附录包含充分实验细节。[R2: Reproducibility 4/5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. ρ≈0.997 与 \"31% instability\" 的叙事张力未解决** [R2-N1, R1 AGREE]\n- 论文核心主张是 31.3% 题目存在 temporal DIF，但排名高度保持（ρ≈0.997）。\"diagnostic, not destructive\" 定位合理，但论文未令人信服论证 practitioners 为何应关心不影响排名的 instability。§5.1 三层分解停留概念层面，缺乏\"忽略 DIF 会导致什么具体错误\"的实证案例。§4.6 的 Llama-3 +53 / Mistral -35 说明 DIF items 包含家族特异性信号，但非\"忽略 DIF 导致错误决策\"的论证。\n- R1 补充：ρ≈0.997 不否定 31% DIF 的重要性——排名相同但 evidential basis 不同（两次考试分数相同但考的内容实质不同）。但论文需要用 worked example 而非类比来论证。\n- **建议**：(a) 提供 1-2 个具体 worked example；(b) 考虑将 \"instability\" 改为 \"measurement heterogeneity\"——后者更精确，避免与 ρ≈0.997 的表面矛盾。[两位共识]\n\n**MF2. 归因缺口限制审计协议可操作性** [R2-N2, R1-W5, 两位共识]\n- §5.3 \"Act (C%≥25%)\" 建议 \"investigate flagged items\"——但 DIF 只检测 THAT 不解释 WHY，investigate for what？15%/25% 阈值声称 \"adapt ETS practice\"，但 ETS 阈值是为教育公平性（demographic fairness）设计的，有明确 follow-up（item bias review panel）。迁移到 LLM 场景后 \"investigate\" 对象和方法完全不同。\n- **建议**：(a) 基于模拟分析确定阈值（C% 多高时 ρ 显著下降）；(b) 为每个 action level 提供具体可执行步骤（item content review / cross-reference contamination sources / report stable-item rankings as sensitivity analysis）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. LLM examinee 非独立性对统计推断的影响** [R1-N1, R2 AGREE]\n- 5,227 模型包含大量 fine-tune variants，MH χ² 有效样本量远小于名义值。Permutation test（shuffling non-independent units）和 bootstrap CI 同受影响。De-duplication K=20 → C%=29.1% 有信息量但不充分。\n- R2 缓解：效应量极大（174×），31.3% 是描述性统计量不依赖 χ² 显著性，不会因非独立性\"消失\"。真正受影响的是每个 item 的 MH χ² 显著性和 CI 宽度。\n- **建议**：(1) 报告 model family 数量及 size 分布；(2) cluster-robust permutation test 对比；(3) cluster bootstrap CI。\n\n**SF2. ΔTPR 应在主文所有首次引用处标注为 upper-bound** [R1-N2, R2 AGREE]\n- Binary response flipping 是最极端的 uniform exploitation。§3.4 末段有 \"upper-bound estimates\" 但 Abstract 和 §4.5 首次报告处无限定。低注入率（p<0.3）检测力未报告，real contamination 可能对应 p=0.05-0.2。\n- **建议**：Abstract 加 \"under worst-case uniform injection\"；§4.5 加限定；补充 p∈{0.05, 0.1, 0.2} 数据或讨论局限。\n\n**SF3. ΔFPR=0.000 在 Abstract 中缺乏 multi-subject 限定** [R1-W1, R2 AGREE]\n- Abstract \"achieves zero false positive inflation\" 仅在 single-subject contamination 下成立。k≤5 时 ΔFPR≤0.007，k=10 时升至 0.047。\n- **建议**：Abstract 改为 \"achieves zero false positive inflation under single- to few-subject contamination (ΔFPR=0.000, k≤5)\"。\n\n**SF4. Within-subject C%=38.1% > temporal C%=31.3% 解释不充分** [R1-W3, R2 AGREE]\n- Within-subject DIF 高出 7pp，但未连接 Q3 local dependence（11.3% within-subject pairs > |Q3|>0.20）作为 inflation 原因。\n- **建议**：明确论证 within-subject C% 较高部分源于 local dependence inflation，cross-subject 的 31.3% 更可靠。\n\n**SF5. \\enlargethispage{6\\baselineskip} 格式操纵过于激进** [R2-W2, R1 AGREE]\n- 说明论文在 8 页限制下紧凑。§4.2 permutation test 细节可压缩移入附录。\n- **建议**：压缩冗余内容使 \\enlargethispage ≤2 或消除。\n\n**SF6. 与 Growing Pains (Habba et al. 2026) 概念对比不完整** [R2-W3, R1 AGREE]\n- \"Empirical comparison awaits public release\" 留空白。FPC 假设 anchor items 稳定 vs 本文发现 31% 不稳定——概念张力值得讨论。\n- **建议**：增加 1-2 句概念层面对比。\n\n**SF7. Monte Carlo power analysis 依赖 poor-fit 2PL 参数** [R1-N3, R2 partially rebuts → 降级为 Should-Fix]\n- §4.1 使用 2PL 参数但 MMLU poor fit to 2PL。论文 triangulation 合理，Appendix 已标注，但 §4.1 开头应更明确。\n- **建议**：§4.1 加 \"approximate parametric bounds\"，以 semi-synthetic injection 为主要 power evidence。\n\n### Nice-to-Have（不影响接收）\n\n- **N1**: \"z = −8σ to −49σ\" 记号不标准，应为 \"z = −8 to −49\"。[R2-M1, R1 AGREE]\n- **N2**: Table 1 \"FPR\" 列与 §3.4 ΔFPR 概念不一致，需脚注明确。[R2-M2, R1 AGREE]\n- **N3**: Table 1 Llama-2 vs Llama-3 行 FPR/Enrichment 为 \"--\" 未注释原因。[R2-M5, R1 AGREE]\n- **N4**: Bootstrap CI [29.4%, 38.1%] 右偏解释可更清晰。[R2-M3, R1 AGREE]\n- **N5**: Cross-subject matching 新颖性措辞可更谨慎——承认 purified matching 先例，定位为 LLM-specific adaptation。[R2-W1, R1 部分 REBUT 但同意调整措辞]\n- **N6**: Hardy et al. (2026) scalability coefficients 引用可获取性待验证。[R2, R1 AGREE]\n- **N7**: GSM1K r=-0.478 应补充 95% CI（约 [-0.71, -0.16]）。[R1-Q5]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Ground truth meta-critique 是最有价值的贡献**（R1 优势 3 = R2 S2）\n2. **ρ≈0.997 vs 31% instability 是最大叙事挑战**（R2-N1, R1 AGREE）\n3. **审计协议缺乏可操作性**（R2-N2 = R1-W5，两位独立提出）\n4. **ΔTPR 是 upper-bound**（R1-N2, R2-W4 独立提出同一关切）\n5. **LLM examinee 非独立性是最大方法论弱点**（R1-N1, R2 AGREE，但效应量极大部分缓解）\n6. **\"that\" not \"why\" 认识论定位贯穿全文——是论文 framing 最成功之处**\n7. **整体评分一致：3.5 Borderline Conference**\n\n---\n\n## Reviewer Divergence [REBUT / Partially REBUT]\n\n1. **R1-W4 统计 vs 实际显著性混淆**：R2 指出 R1 存在事实性错误——R1 将 φ=0.012 误读为 p=0.012，实际 p=0.258（未达统计显著性）。\"Near-independent\" 判断完全合理。**→ 撤回此 issue。**\n\n2. **R1-N3 Monte Carlo power analysis（critical vs warning）**：R1 评为 critical，R2 partially rebuts——论文 triangulation 合理且已在 Appendix 明确标注。**→ 共识降级为 Should-Fix**（SF7）。\n\n3. **R2-W1 Cross-subject matching 新颖性**：R2 认为有 DIF 文献先例，新颖性声明需谨慎。R1 反驳 LLM-specific adaptation 非 trivial（cross-subject contamination 是人类测试中不存在的挑战）。**→ 共识：承认先例但保留 LLM 适配贡献，调整措辞。**\n\n4. **R2-W5 Polytomous DIF 讨论**：R2 要求在 Related Work 覆盖。R1 反驳超出 scope（论文聚焦 binary response，Limitations 已提及）。**→ 共识：Limitations 中已有，不强制在 Related Work 扩展。**\n\n5. **Excitement 评分**：R1 给 3.5/5（empirical findings 启示性高），R2 给 3/5（\"现有方法应用到新领域\"限制兴奋度）。**→ 记录分歧，不影响整体评分。**\n\n---\n\n## Questions to Authors\n\n**Q1** [R1-Q1, R2 AGREE]: 5,227 模型中有多少个 distinct model families？Family size 分布（median, max）？Cluster-robust permutation test 下 C% 和 p-value 是否改变？\n\n**Q2** [R1-Q2]: Random split baseline（C%=0.18%）是 model-level 还是 family-level 随机分？如果 model-level 且同一 family 分到两边，baseline FPR 可能 underestimate。\n\n**Q3** [R1-Q4]: Cross-benchmark matching（MMLU total score → GSM8K items）——construct 不同是否引入 matching bias？这对 GSM8K 的 18.9% C% 有何影响？\n\n**Q4** [R1-W3, R2 AGREE]: Within-subject C%=38.1%（range 31.1-45.2%）vs temporal C%=31.3%——请明确论证哪个更可靠，以及 Q3 local dependence 对 within-subject DIF 的 inflation 贡献。\n\n**Q5** [R2-N1]: 能否提供 1-2 个 worked example，展示特定模型在 full MMLU vs stable-only items 排名差异可能导致的具体决策影响？\n\n**Q6** [R1-W6]: p<0.3 时 ΔTPR 如何？MH-DIF 在 low exploitation rate（p=0.05-0.2）下是否仍有可用检测力？\n\n**Q7** [R2-N2]: §5.3 审计协议阈值 15%/25% 的选择是否有实证依据？能否通过模拟确定\"C% 多高时 ρ 开始显著下降\"？\n\n---\n\n## Missing References\n\n- Hardy et al. (2026) scalability coefficients：已引用但可获取性待验证。[R2 提出]\n- Swaminathan & Rogers (1990) purified subtest matching 在 Related Work 中可补充引用（当前仅在 Appendix 出现）。[R2-W1, R1 认为 Holland & Thayer 1988 已覆盖]\n- Polytomous DIF 文献（generalized MH, Liu-Agresti）：不强制要求，Limitations 已提及方向。[R2-W5, R1 REBUT]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 1 warning, 5 info）：\n\n- **[warning]** Page 3-5：Related Work 到 Method 前半段连续约 3 页无 figure/table，视觉节奏偏平\n- **[info]** Page 6-7：Table 1, 2 字号偏小，正常打印下可读但吃力\n- **[info]** Page 7：Figure 2 两个子面板尺寸偏小，axis label 勉强可读\n- **[info]** Page 8：Discussion + Conclusion + Limitations 起始全挤在一页，section 转换密集\n- **[info]** Page 14：Figure 4-5 之间约 1/4 页空白；Figure 5 数据点标签密集有重叠\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 — Borderline Conference**（两位 Reviewer 一致）\n\n**置信度：4 / 5**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement | 3.5 | 3.0 | 3.25 |\n| Reproducibility | — | 4.0 | 4.0 |\n| Overall | 3.5 | 3.5 | **3.5** |\n\n**判断依据**：\n\n技术执行扎实、规模宏大的实证研究。Ground truth meta-critique（web-overlap labels ⊥ DIF flags）是重要的概念贡献，31% temporal DIF 的跨 6 基准复制结果令人印象深刻。主要问题在于：\n\n1. **叙事张力**（MF1）：ρ≈0.997 的排名保持与 \"31% instability\" 主张之间缺乏令人信服的 practical significance 论证——这是论文从 Borderline 升至 Conference 的关键障碍。\n2. **审计协议可操作性**（MF2）：DIF 无法归因的前提下，audit protocol 的 action steps 过于模糊，阈值缺乏实证依据。\n3. **方法论新颖性有限**：MH-DIF 未修改，cross-subject matching 有 DIF 文献先例（尽管 LLM 场景适配非 trivial）。\n\n**如果有效解决 MF1（具体案例 + 叙事调整）和 MF2（可操作审计步骤），论文有望提升至 4.0 (Conference) 水平。**\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- ΔTPR=+0.508 需加 \"under worst-case uniform injection\" 限定\n- ΔFPR=0.000 需加 multi-subject contamination 限定\n- \"z = −8σ to −49σ\" 记号不标准\n- 总体信息密度高且准确，但缺少 practical significance 的 hook\n\n### Introduction (§1)\n- Figure 1 直观有效\n- \"diagnostic, not destructive\" 定位清晰\n- 三大贡献排序合理（R2 认为 meta-critique 最有价值，可考虑前移）\n- 脚注 1 匿名链接处理得当\n\n### Related Work (§2)\n- 四段结构清晰（Contamination / IRT / DIF / Benchmark Quality）\n- Growing Pains 对比可更深入（FPC 前提假设 vs 31% instability 的概念张力）\n- DIF 文献先例（purified matching）的引用可更明确\n- 总体覆盖较完整\n\n### Method (§3)\n- MH-DIF 和 ETS classification 解释清晰\n- LLM-specific challenges 段落有价值\n- Remark (Zero FPR) 是 by-construction 结论，建议定位为\"设计选择及其性质\"\n- Cross-subject matching 的三种策略描述清晰\n- Semi-synthetic injection 的 binary flipping 局限应在此处首次标注\n\n### Experiments (§4)\n- §4.1 Monte Carlo power analysis 应标注为 approximate parametric bounds\n- §4.2 \"31% Measurement Instability\" section title 与 \"diagnostic, not destructive\" 有张力\n- §4.3 Ground truth mismatch 是最强的 section\n- §4.4 Structural analysis 全面但 within-subject C% 解释需加强\n- §4.5 Semi-synthetic validation 缺少 p<0.3 数据\n- §4.6 Downstream impact 需 worked example 而非仅统计量\n- §4.7 Cross-benchmark validation 增强可信度，Table 3 信息丰富\n\n### Discussion (§5)\n- §5.1 三层框架（impact/DIF/attribution）好但仅在此引入——可前移到 §3 并在 §4 系统使用\n- §5.2 Ground truth meta-critique 讨论充分\n- §5.3 Audit protocol 是最弱的 section——阈值缺乏依据，action steps 模糊\n- \\enlargethispage{6\\baselineskip} 过于激进\n\n### Conclusion (§6)\n- 简洁恰当\n\n### Limitations\n- 覆盖 4 个方面（方法范围、样本非独立性、匹配边界、泛化性），长度恰当\n- 学术诚实值得肯定",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-22T03:43:43.495908+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4316
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-22T03:43:55.003946+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-22T03:43:55.004523+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 472 · 2026-05-22T03:44:07.889980+00:00_

**审稿报告已投递。**

**Round 10 审稿结论：3.5 / 5 — Borderline Conference**

两位 Reviewer 独立评分一致（3.5），经交叉分享后关键问题全部收敛，1 轮即完成。

**核心发现**：
- **2 个 Must-Fix**：(1) ρ≈0.997 vs 31% instability 叙事张力——需具体 worked example + 考虑 "measurement heterogeneity" 措辞；(2) 审计协议归因缺口——阈值需实证依据，action steps 需具体化
- **7 个 Should-Fix**：examinee 非独立性（cluster-robust 方法）、ΔTPR upper-bound 标注、ΔFPR multi-subject 限定、within-subject C% 解释、\enlargethispage 压缩、Growing Pains 对比、Monte Carlo 标注
- **升级路径**：有效解决 MF1 + MF2 可从 3.5 提升至 4.0 (Conference)

Issue Tracker 已同步更新（`review_issues.yaml`）。视觉审查结果已纳入报告（0 critical, 1 warning, 5 info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 473 · 2026-05-22T03:44:10.627905+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部审稿意见的逐条回应（14 个 AGREE + 3 个 REBUT）。主要分歧点：cross-subject matching 的新颖性定位（R2-W1）、polytomous DIF 讨论的必要性（R2-W5）、Swaminathan & Rogers 引用（已在附录中出现）。在 N1（叙事张力）和 N2（审计协议可操作性）上与 R2 达成共识。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 474 · 2026-05-22T03:44:25.281162+00:00_

审稿流程已完成。报告已投递给 Research Director。

**最终结果**：

- **评分**：3.5 / 5 — Borderline Conference（两位 Reviewer 一致）
- **2 个 Must-Fix**：(1) ρ≈0.997 vs 31% instability 叙事张力需具体案例论证 practical significance；(2) 审计协议阈值缺实证依据，action steps 过于模糊
- **7 个 Should-Fix**：examinee 非独立性需 cluster-robust 方法、ΔTPR upper-bound 标注、ΔFPR multi-subject 限定、within-subject C% 解释、\enlargethispage 格式、Growing Pains 概念对比、Monte Carlo power analysis 标注
- **升级路径**：有效解决 MF1 + MF2 后有望达到 4.0 (Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 50

## Round 50

64 recorded events


### User

_source line 475 · 2026-05-22T05:17:24.277741+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-22T05:17:30.970691+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-22T05:17:31.022104+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-22T05:17:54.269440+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-22T05:17:54.320226+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-22T05:18:01.500839+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-22T05:18:01.601810+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-22T05:18:07.629147+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-22T05:18:08.282533+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-22T05:18:09.640432+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-22T05:18:10.494918+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-22T05:18:10.796785+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-22T05:18:10.948544+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_5/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-22T05:18:21.092032+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 489 · 2026-05-22T05:18:21.142696+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-22T05:18:24.959339+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 491 · 2026-05-22T05:18:25.361518+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 492 · 2026-05-22T05:18:25.412257+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-22T05:18:33.150379+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines and ARR policy for EMNLP 2026:

## Call for Papers Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing comput
…[truncated 1023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 8191
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-22T05:18:38.220996+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template anonymization policy",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit template anonymization policy",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-22T05:18:38.673150+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 496 · 2026-05-22T05:18:38.723762+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-22T05:18:45.351653+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template anonymization policy"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"18th International Natural Language Generation Conference | ACL Member Portal","url":"https://www.aclweb.org/portal/content/18th-international-natural-language-generation-conference"}]

Based on the search results, I found information about EMNLP 2026 submission guidelines from the Industry Track. Here's what I found regarding submission format requirements:

## Page Limit and Format

The search results show information specific to the EMNLP 2026 Industry Track. For formatting, submissions should follow ACL submission policies and use the ACL style templates.

## Anonymization Policy

Industry Track sub
…[truncated 1145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 7130
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-22T05:18:52.682832+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines submission format long paper page limit",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines submission format long paper page limit",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-22T05:18:54.641935+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"project_config*\" -path \"*irt_equated*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"project_config*\" -path \"*irt_equated*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-22T05:18:54.793050+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-22T05:18:59.312201+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines submission format long paper page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on my search results, here's what I found regarding ACL Rolling Review 2026 author guidelines:

## Submission Format and Page 
…[truncated 1187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6629
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-22T05:19:03.380294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"*.yaml\" -path \"*irt_equated*\" | head -20; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/backend.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_IN_BACKEND\"",
  "description": "Find project-specific config and external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"*.yaml\" -path \"*irt_equated*\" | head -20; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/backend.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NOT_IN_BACKEND\"",
    "description": "Find project-specific config and external review settings"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-22T05:19:03.431099+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/worst/review_context.yaml
/home/ubuntu/.agent-
…[truncated 758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-22T05:19:07.799781+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | grep -v \"artifacts/dream\" | head -10",
  "description": "Search for external review config settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" 2>/dev/null | grep -v \"artifacts/dream\" | head -10",
    "description": "Search for external review config settings"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-22T05:19:08.151671+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-22T05:19:14.580492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-22T05:19:14.631409+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-22T05:19:19.652693+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-22T05:19:19.703430+00:00_

abstract.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-22T05:19:25.829931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-22T05:19:25.981183+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet whether individual items measure the same construct over time is rarely tested---and existing contamination detectors validate against ground truth that conflates global exposure with differential functioning. We develop a semi-synthetic injection framework with cross-subject matching that achieves zero false positive inflation under single-subject contamination ($\Delta\mathrm{FPR} = 0.000$; $\Delta\mathrm{FPR} < 0.01$ for $k \leq 5$ subjects) while preserving detection power under worst-case uniform injection ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$), and show that web-overlap contamination labels are near-independent of Mantel-Haenszel Differential Item Functioning (DIF) flags (enrichment $\approx 0.96$, $\phi = 0.012$)---exposing a category error in prevailing validation methodology. Applying MH-DIF with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 items), we find 17.9--31.3\% of items exhibit large temporal DIF (ETS~C) between 2023 and 2024 cohorts, each 45--174$\times$ above random baselines, with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). This does not threaten aggregate ranking validity ($\rho \approx 0.997$, $\tau \approx 0.958$), but specific model families show concentrated rank shifts (Llama-3: ${+}53$ median positions, Mistral: $-35$) and 2.0\% of pairwise rankings reverse. Item-level decomposition shows 92.4\% of the signal is item-specific; DIF-flagged items concentrate discriminative information ($z = -8$ to $-49$) with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-22T05:19:26.031925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-22T05:19:26.434171+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. This pattern persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of the DIF signal is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this measurement instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference~\citep{shi2024mink} to performance-based detectors~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}. These methods validate d
…[truncated 5079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-22T05:19:26.484863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-22T05:19:26.585843+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees 
…[truncated 8131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-22T05:19:31.963299+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-22T05:19:32.415868+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $B = 1{,}000$ model-level resamples; rightward asymmetry reflects heavy-tailed C\% from subjects exceeding 40\%). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold already provides implicit multiple-testing protection.
17	
18	\looseness=-1
19	Three controls confirm this reflects genuine temporal change. A random split of the 2023 c
…[truncated 10656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-22T05:19:32.416456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---
