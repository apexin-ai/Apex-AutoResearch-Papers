---
round: 5
review_mode: continue
overall_score: 4.0 - Conference
timestamp: 2026-05-21T14:14:37.121883+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 5 Consolidated Review Report — policy_ambiguity_safety

**Paper**: "Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents"
**Venue**: EMNLP 2026 via ARR May cycle (Long Paper)
**Mode**: Continue Review (Round 4 → Round 5)
**Reviewers**: R1 (方法严谨性), R2 (新颖性与完整性)
**Date**: 2026-05-21

---

## Summary

Round 4 评分 3.5 (Borderline Conference)，条件是 4 项 editorial fix 后可升至 4.0。本轮修改远超 editorial 级别：新增 human validation（κ=0.733）、perturbation 扩展至 n=300、两个新模型复制实验、ambiguity detection classifier、独立 incompleteness confound 分析、以及大幅扩展的 Discussion。所有 Round 1-4 的 critical 和 warning issues 现已全部解决。残留问题仅为 editorial 级别（Introduction 数值未更新、Conclusion scope 需澄清、Gemini replication 非显著性未标注）。

**两位 Reviewer 一致评分 4.0 (Conference)。**

---

## Strengths

1. **Human validation 补齐了最顽固的方法论缺口**（MF2，历经 Round 1-4）：100 stratified episodes, 2 NLP annotators, inter-annotator binary κ=0.798 (weighted κ_w=0.762), human-LLM pooled binary κ=0.733 (weighted κ_w=0.807)。"The LLM judge thus operates within the range of human disagreement"——有数据支撑的结论。在 EMNLP agent evaluation 标准中达到或超过同类工作（R-Judge, ToolEmu）。

2. **Perturbation control 大幅加强因果推断**（SF3）：n=120→n=300, Δ=-0.67pp (CI [-8.0, 6.67])。CI 上界从 13.3pp→6.67pp，worst-case 归因比例从 39%→19.6%，残余归因从 ≥20.7pp→≥27.3pp。因果推断从 "reasonable" 升级为 "strong"。

3. **Cross-architecture replication 增强 generalizability**：Gemini-2.5-Flash 和 LLaMA-4-Scout 确认 C1 binary effect 跨 7 models / 6 providers（Δ=+20.0 to +33.6pp, both p<10⁻⁶）。Incompleteness ≥46% in all seven models。C2 type hierarchy 在 LLaMA 上强复制（ρ=0.90, p=0.025），Gemini 方向一致但未达显著性（ρ=0.60, p=0.285）。

4. **Mechanistic explanation 提升理论深度**：Discussion 新增 "Why incompleteness resists safety training"——gap-filling bypasses RLHF refusal decision points, agent 从不遇到 "should I or shouldn't I?" 的节点。69.2% unauthorized escalation + 0% conservative refusal (p<10⁻⁴, binomial test) 证明 systematic permissiveness bias。论证 well-grounded，hedging 恰当（"suggests", "consistent with"）。

5. **Detection-danger inverse correlation 有独立贡献**：Appendix D proof-of-concept classifier, binary F1=0.81, incompleteness F1=0.34。"Most dangerous types are least detectable"——实践部署的结构性困境。恰当定位为 proof-of-concept。

6. **核心实验设计始终扎实**：matched-pair causal design (2,997 episodes), cross-judge calibration, ICC=0.919 (GPT-5.4 + GPT-4.1 spanning judge boundary), TOST 7-margin sensitivity, severity threshold robustness (Kendall τ=0.73)。

---

## Weaknesses

### Editorial Issues（不影响接收决定，应在 camera-ready 前修复）

1. **Introduction perturbation 数值未更新**（R5-DIR-1, consensus must-fix）：Introduction contribution 1 仍写 "Δ_perturb = 3.33 pp"（旧 n=120），但 Method §4.5 和 Results §5.1 已更新为 "Δ_perturb = -0.67 pp"（新 n=300）。同一论文内的 factual inconsistency。一处字符串替换即可修复。

2. **Conclusion "seven models" scope conflation**（R5-DIR-2, consensus should-fix）：Conclusion 开头 "Across seven models and six providers, ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1)" 将 5-model main study 的 OR=15.1 归于 7 models（LLaMA OR=2.8 远低于此）。Abstract 正确区分了两组。Conclusion 应采用同样的精度。~15 词改写。

3. **Gemini C2 replication 非显著性未标注**（R5-NEW-1, consensus should-fix）：Abstract/Conclusion 写 "replicates on two additional model families (ρ = 0.6–0.9)"。数值正确（四舍五入），但 Gemini ρ=0.60 对应 p=0.285（不显著）。"Replicates on two additional model families" 暗示两者均成功复制。建议加 significance qualifier 或分别报告。

4. **Appendix E coreferential 排除未解释**（R5-NEW-2, consensus should-fix）：Replication 使用 5 types，排除 coreferential 但未给理由。Coreferential 是 confound-free reference point (info delta=0)，排除它意味着无法独立验证 C2 lower bound。一句话解释即可。

### Minor Residual

5. **SF2 (Error analysis human validation)**：Failure mode coding 仍为 LLM-only (AC₁=0.62, minority κ=0.29)。Resolved within scope——primary evaluation pipeline 已有 human validation，error analysis 是 supplementary。Limitations 坦诚承认。

6. **M1 (Bib cosmetic)**：lassiter_goodman year, levy year, ferrari author. Copyediting 级别。

---

## Questions

1. Appendix E 为何排除 coreferential？是实验设计约束（如 coreferential 的 lexically-identical 特性难以跨 benchmark 适配）还是资源限制？
2. LLaMA 的 elevated unambiguous baseline (17.6%) 是否暗示 LLaMA-4-Scout 的基础 instruction following 质量低于其他模型？这对 "seven models" generalizability claim 有何影响？
3. Detection classifier 是否计划在 naturally-occurring policy documents 上验证？Appendix D 最后一句承认了这一限制。

---

## Missing References

无新增遗漏。36 篇引用覆盖了核心 concurrent work。Round 4 残留的 Agent-SafetyBench / OpenAgentSafety 建议已被判定为 nice-to-have 而非 gap。

---

## External Review

外部审稿（Stanford Agentic Reviewer）：**Skipped**（用户在 Round 3 跳过，未重新请求）。

---

## Visual Layout Check（非评分项）

**Status**: Done (0 critical, 2 warnings, 7 info)

**Warnings**:
- Pages 3-5 连续纯文本（Taxonomy + Method），无 display item。建议增加 taxonomy summary table 或树形图
- Display items 分布失衡：Figure 1 (p.2) 到 Table 1 (p.6) 之间 3 页无任何 visual element

**Info highlights**:
- Figure 2 面积偏小，axis labels 字号接近下限
- Figure 3 部分颜色对灰度打印可能难以区分，建议辅以 hatch pattern
- Table 1/Table 2 格式规范
- 无 margin 溢出、渲染错误、未解析引用
- 主文 8 页合规

---

## Overall Assessment

### Score: 4.0 / 5 — Conference

**R1**: 4.0 (Soundness 4.0, Excitement 3.5, Confidence 4)
**R2**: 4.0 (Soundness 4.5, Excitement 4.0, Confidence 4)
**Director consensus**: 4.0

### 评分理由

**论文达到 EMNLP 2026 main conference 接收水平。** 核心贡献——matched-pair causal identification of policy ambiguity's safety impact——在方法论上无重大缺陷：

- **因果推断链完整**：matched-pair design + perturbation control (n=300, residual ≥27.3pp) + cross-architecture replication (7 models, 6 providers) + human validation (κ=0.733)
- **Claim-evidence alignment 精确**：C1/C2 primary (有强证据), C3 inconclusive (诚实承认), C4 exploratory (恰当 hedge)
- **理论贡献有意义**：Differential Nocuity 框架扩展了 Berry & Kamsties (2004), Ambiguity Blindness (<11% awareness) 是有理论价值的实证发现, gap-filling bypasses RLHF 假说 well-grounded
- **实践贡献清晰**：type-aware auditing recommendation backed by mitigation experiment (-8.5pp overall), detection paradox (most dangerous = least detectable) identifies deployment challenge

**Soundness (4.0-4.5)**：所有 4 个 critical must-fix 已解决。Human validation 补齐了最后的方法论缺口。Perturbation expansion 显著加强因果推断。Cross-judge calibration + within-judge validation 限制了 judge confound。Incompleteness confound 有完整的 upper-bound + lower-bound + regression 处理。

**Excitement (3.5-4.0)**：R1 和 R2 在此维度有分歧（3.5 vs 4.0）。Director 判断：论文从 Round 4 的 "solid empirical study" 升级为包含 mechanistic explanation + detection paradox + cross-provider replication 的 comprehensive contribution，但核心 novelty（将 RE ambiguity taxonomy 应用于 LLM agent safety）仍是 incremental extension。取中值 3.75，向 4.0 四舍五入——Excitement 对于 Conference acceptance 足够但不构成 award consideration。

**与 Round 4 的评分变化 (3.5→4.0)**：
- Human validation (MF2 resolved): +0.25
- Perturbation expansion (causal inference strengthened): +0.1
- Model replication + detection classifier + mechanistic discussion: +0.15
- Residual editorial issues: -0.0 (trivial, don't affect score)

### EMNLP 2026 ARR 定位

- **Main Conference (4.0)**: ✅ 当前状态满足。4 项 editorial fix 应在 camera-ready 前完成。
- **Consider for Award (4.5+)**: 需要 (a) human validation 扩展至 error analysis, (b) Gemini C2 replication 达到显著, (c) detection classifier 在真实 policy 文档上验证。当前不在 award 考虑范围内。

---

## Detailed Comments

### Camera-Ready Action Items

| # | Issue | Fix | Effort | Impact |
|---|-------|-----|--------|--------|
| 1 | Introduction Δ_perturb stale (R5-DIR-1) | 3.33→-0.67 in introduction.tex line 23 | 1 word | Must-fix: internal consistency |
| 2 | Conclusion 5/7-model scope (R5-DIR-2) | Separate main-study stats from replication scope | ~15 words | Should-fix: reader precision |
| 3 | Gemini replication significance (R5-NEW-1) | Add qualifier to ρ range or report individually | ~5 words | Should-fix: statistical honesty |
| 4 | Coreferential exclusion reason (R5-NEW-2) | Add explanation sentence in Appendix E | ~1 sentence | Should-fix: transparency |
| 5 | Bib cosmetic (M1) | Fix lassiter/levy years, ferrari author | Copyediting | Minor |

All items are editorial and can be completed in under 30 minutes.

### Cross-Round Progress Summary

| Round | Score | Key Events |
|-------|-------|-----------|
| Round 1 | — | Initial identification of MF1/MF3/SF1-SF4 |
| Round 2 | — | SF6-SF8 added, partial fixes |
| Round 3 | 3.0 | Fresh review: 4 MF + 8 SF identified |
| Round 4 | 3.5 | MF1/MF3/MF4 resolved, MF2 downgraded, 6/8 SF resolved |
| **Round 5** | **4.0** | **MF2 resolved (human validation), SF3 strengthened (n=300), model replication, detection experiment, mechanistic discussion** |

论文从 Round 3 的 3.0 (Findings) 稳步提升至 4.0 (Conference)，每轮修改均为实质性改进。Round 5 的提升尤为显著——不仅补齐了方法论缺口，还通过 replication、detection、和 mechanistic explanation 提升了贡献层次。残留问题均为 trivial editorial fixes。

**建议接收为 EMNLP 2026 Main Conference paper (4.0/5)。**