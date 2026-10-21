---
round: 11
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T19:57:53.411005+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 13 (Fresh)

**论文**: *The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation*
**Venue**: EMNLP 2026 (ACL ARR)
**Reviewers**: R1（方法严谨性 + 统计方法 + 实验设计）, R2（新颖性 + framing + 写作质量）

---

## Summary

本文提出 Controlled Style Decomposition (CSD) 框架，揭示 Likert 评分与 pairwise comparison 在检测 LLM judge 风格偏差时的系统性分歧（"Likert Blindspot"）：pairwise 检测到显著风格偏好（BT > 60%, p < 0.001），而 Likert 完全遗漏（d → 0, p > 0.17）。跨 4 个 judge、3 个 benchmark、7 种统计方法验证，GEE 条件分解揭示 per-axis 混淆结构差异（verbosity = style-dominated, formality = conditional, register = judge-dependent）。实验设计在该领域属最周密之一，但 framing 系统性偏向 pairwise 为 ground truth，新颖性为增量贡献。

---

## Strengths

**S1. 实验控制层次感出色。** CSD 三层控制（NLI gate §3.2、same-style double-rewrite §5.4、position swapping §3.3）+ 6 项 amplification controls，在 LLM judge 风格偏差文献中属最周密的实验设计之一。[R1-S1, R2-S1, 共识]

**S2. 统计方法多元互补。** 7 种方法覆盖不同假设族（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Bayesian t），Table 2 sensitivity hierarchy 清晰展示 Likert-based 方法一致失败。Holm-Bonferroni 校正覆盖 6 个主检验，8 检验扩展族全通过。[R1-S2, R2-S2, 共识]

**S3. GEE per-axis confound 分解具有独立方法论贡献。** Table 3 将 Style OR 与 Originality OR 分离，揭示 verbosity style-dominated (OR 8–15) vs formality conditional 的结构性差异。exchangeable working correlation + sandwich SE 经 Appendix C 诊断验证（ΔQIC < 0.001, Max|ΔCoef| < 0.02）。[R1-S4, R2-S4, 共识]

**S4. 鲁棒性检验链完整。** NLI 阈值 11 点 sensitivity sweep (Appendix E)、bootstrap 衰减分析 (Appendix J)、rewriter 独立性检验 (Appendix D)、cross-axis 污染分析 (Appendix R)、formal power analysis (Figure 4, Appendix K)、100-point continuous Likert (Appendix M)——构成多层防御，核心发现难以归因于单一 artifact。[R1-S5, R2-S3, 共识]

**S5. 因果声明审慎。** §3.5 Design Rationale 明确免责（"we do not claim this DAG is a complete structural causal model"），"Controlled" 限定为实验控制而非因果识别，Figure 2 DAG 标注残余混淆路径。标题副标题 "Measurement-Mode Divergence" 是中性表述。[R1-S6]

**S6. 跨 judge 覆盖合理。** 4 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 negative control（Claude Sonnet 4），覆盖主流架构。[R2-S5]

---

## Weaknesses

### Must-Fix

**MF1 [critical] Framing 系统性偏向 pairwise 为 ground truth**
- **位置**: Title, Abstract ("signal loss exceeding 60%"), §6 ("Likert-only audits miss style-driven preferences")
- **问题**: 论文在 §5.1 承认三种等效解释（measurement attenuation / format amplification / construct divergence），引用 Comparative Trap (Jeong et al., 2025) 和 Tripathi et al. (2025)。但标题 "The Likert Blindspot" 将 Likert 定位为"盲区"，Abstract 和 Conclusion 的叙事 90% 倾向 attenuation 解释。Caveat 被隔离在 §5.1 末尾和 Limitations，未进入标题/摘要/结论的主叙事。缺乏外部 ground truth，论文无法判定 pairwise 检测到的是真实信号还是格式放大的微弱偏好。
- **共识**: R2 Must-Fix (N1), R1 Should-Fix (W5) 但同意问题存在——本质是同一关切。Director 升级为 Must-Fix：framing 不对称贯穿全文核心叙事。
- **建议**: Abstract/§6 给三种解释同等权重（1-2 句即可）；§5.1 更显式论证 RLHF 语境下 pairwise-detected biases 的实践意义。不必改标题。

### Should-Fix

**SF1 [warning] 新颖性定位需进一步明确**
- **位置**: §1, §6
- **问题**: Likert vs pairwise 灵敏度差异是心理测量学 established knowledge (Thurstone 1927)。论文真正贡献是 (a) 首次在 LLM judge 领域受控量化 + (b) GEE per-axis decomposition 方法论，但措辞有时像声称发现现象本身。
- **共识**: R2 Must-Fix (N2), R1 REBUT——§1 已界定贡献边界，R2 自己承认 GEE 分解是"真正增量贡献"。Director 降为 Should-Fix：R1 rebuttal 有效，但局部措辞可收紧。
- **建议**: §1 增加一句明确承认心理测量学先例；"This is the Likert Blindspot" → "We term this the Likert Blindspot"。

**SF2 [warning] 人工标注规模不足（50 pairs, κ=0.44）**
- **位置**: §5.4, Appendix S
- **问题**: NLI gate 是 CSD 管线核心假设保障。50 对样本、2 名标注员、κ=0.44 moderate agreement 不足以建立强信心。Annotator 2 precision = 84.3%（CI [65.3%, 93.6%]），4 个分歧全在 verbosity condensation。
- **共识**: R1 Should-Fix (W1), R2 AGREE。两位一致。
- **建议**: 增加至 ≥100 对 + 第 3 名标注员 + 分析分歧案例特征分布（是否集中在特定 axis/instruction type）。

**SF3 [warning] TOST 等价阈值 Δ=15pp 与 GPT-4o 最小偏差重叠**
- **位置**: §4.1 脚注, Limitations, Appendix G
- **问题**: GPT-4o formality BT=63.0%（13pp above chance）落在 Δ=15pp 等价区间内。10–14pp moderate bias 可能逃脱检测。Claude 实际 BT (50.2–54.1%) 远低于此阈值，当前结论不受影响，但 Δ 选择缺乏定量推导。
- **共识**: R1 Should-Fix (W2), R2 AGREE。两位一致。
- **建议**: 提供 Δ 的定量推导（多大偏差会改变 benchmark ranking？）+ Δ 敏感性分析 (10/12/15/20pp) + Limitations 承认 moderate bias 可能逃脱。

**SF4 [warning] 方向不对称性对 Table 1 BT 的影响讨论不足**
- **位置**: Table 1, Appendix A/H
- **问题**: Formality 方向不对称显著（formal→casual 88.9% vs casual→formal 52.6%）。Table 1 的 BT 是未调整聚合值，混合了真实风格偏好与原文偏好混淆。Appendix A GEE 控制后仍显著（OR=2.58, p=0.032），但主文读者不易获取。
- **共识**: R1 Should-Fix (W3), R2 AGREE。两位一致。
- **建议**: Table 1 formality 行添加脚注提示方向不对称 + 指向 Appendix A 调整分析。

**SF5 [warning] NLI gate 选择偏差检查覆盖面有限**
- **位置**: §3.2, Appendix B
- **问题**: 44% 拒绝率下仅检查 4 个 surface covariates（word count, sentence count, TTR, FK grade），未覆盖 instruction type/topic 分布、句法复杂度。NLI threshold sweep 稳定性提供间接鲁棒性，但不等同于无选择偏差。
- **共识**: R1 Should-Fix (W4), R2 AGREE（严重程度略低）。两位一致。
- **建议**: 增加 instruction type/topic 分布对比。

**SF6 [warning] 负控制仅一个模型**
- **位置**: §5.3, §6, Limitations
- **问题**: Claude Sonnet 4 是唯一负控制，未探讨 Claude 不受影响的可能机制。
- **共识**: R2 Must-Fix (N3), R1 REBUT——论文从未声明架构特异性，Claude 用于 pipeline validation 而非 architecture comparison。Director 降为 Should-Fix：R1 rebuttal 有效（论文 claim 范围有限），但增加机制讨论成本低。
- **建议**: Limitations 增加 1-2 句 Claude null result 的可能机制讨论；降格为 "one model does not show this pattern"。

**SF7 [warning] Cross-benchmark 覆盖稀疏**
- **位置**: Table 1, §4
- **问题**: AlpacaEval/MT-Bench 仅覆盖部分 judge × axis 组合。"across three benchmarks" 泛化声明需限定。
- **共识**: R2 Should-Fix (W1), R1 部分 AGREE。
- **建议**: 限定为 "with primary results on LLMBar and confirmatory replication on selected configurations"。

### Minor

**M1.** Cross-axis 污染 formality→verbosity word count d=−0.23 超过自设 d<0.20 标准。GEE covariate 控制已缓解（Style OR 变化 <12%）但主文未显式承认阈值违反。[R1-M1, R2 AGREE]

**M2.** 100-point continuous Likert (Appendix M) 仅用 Qwen3-32B，存在 evaluator-producer overlap。应在 Appendix M 注明。[R1-M2, R2 AGREE]

**M3.** BT IIA 脚注 3 简化过度——binary-choice IIA 技术正确，但跨 pairs 聚合的一维性假设未讨论。[R1-M3, R2 AGREE]

**M4.** Bootstrap CI 方法（percentile vs BCa）未指定。BT 估计接近 0.5 时 BCa 可能更稳健。[R1-M4, R2 AGREE]

**M5.** Table 2 GEE（Likert-outcome）与 Table 3 GEE（pairwise-outcome）共享 "GEE" 标签但模型不同。建议在 Table 2 标注 "GEE (Likert-outcome)"。[R1-M5, R2 AGREE]

**M6.** Register 轴 evaluator-producer overlap 最严重（Qwen3-32B 双重角色），应在论文中标注。[R2-W2, R1 部分 AGREE]

**M7.** Introduction motivating example（GPT-4o formal vs casual）未 acknowledge formality-quality nuance。应添加一句 caveat 指向 §5.1 的 confound 讨论。[R2-W4, R1 AGREE]

---

## Reviewer Consensus

1. **[AGREE] 实验设计和统计方法是一流的** — CSD 三层控制 + 7 种统计方法 + 多层鲁棒性检验在该领域属最周密之列。GEE per-axis decomposition 是独立的方法论贡献。

2. **[AGREE] 核心缺陷在解释框架而非实验设计** — 论文的 framing 系统性偏向 "Likert is wrong, pairwise is right"，而数据本身无法排除 construct divergence 或 format amplification 的替代解释。

3. **[AGREE] 人工标注需扩展** — 50 对、κ=0.44 不足以支撑 NLI gate 的核心假设保障角色。

4. **[AGREE] TOST Δ=15pp 需更充分论证** — 与最小观测偏差（13pp）重叠，需定量推导 + 敏感性分析。

5. **[AGREE] 方向不对称性需在主文更好呈现** — Table 1 未调整 BT 可能被误读为纯风格偏好。

6. **[AGREE] 因果声明已审慎** — §3.5 的免责声明充分，无需修改。

## Reviewer Divergence

1. **Framing severity**: R2 Must-Fix, R1 Should-Fix。R1 认为副标题中性 + 实践论证有效，修改 Abstract/Conclusion 权重即可。**Director 判定: Must-Fix**（修复成本低但影响面大）。

2. **Novelty**: R1 Excitement 3.5/5（对 NLP 社区有直接实践影响）; R2 3/5（established knowledge 的 domain transfer）。R1 REBUT 指出 R2 自己承认 GEE 分解是"真正增量贡献"，两个判断矛盾。**Director 判定: novelty 3–3.5 之间** — 受控量化 + GEE 分解有方法论价值，但核心洞察对跨领域读者非全新。

3. **Negative control**: R2 Must-Fix, R1 REBUT（论文从未声明架构特异性，Claude 用于 pipeline validation）。**Director 判定: Should-Fix**（R1 rebuttal 有效）。

4. **Abstract 数字密度**: R2 Should-Fix, R1 REBUT（实证论文需定量具体性）。**Director 判定: Minor 偏好建议**。

5. **"Framework" 术语**: R2 Should-Fix, R1 REBUT（NLP 文献标准用法）。**Director 判定: Minor 偏好建议**。

---

## Questions（需作者回应）

1. 六项 amplification controls 中哪一项最直接排除 "pairwise amplifies micro-preferences" 解释？无人类 ground truth 如何区分 attenuation vs amplification？[R2-Q1, 共识]

2. 是否考虑过分方向拟合 BT 模型（formal→casual 和 casual→formal 分开估计），以区分真实风格偏好与原文质量混淆？[R1-Q1]

3. NLI gate pass/reject 的 instruction type/topic 分布是否有系统差异？[R1-Q2, R2 AGREE]

4. Direction-aware NLI gate 恢复的 21 对的 content quality 分布（Likert 质量分、NLI 分数分布）是否与 bidirectional-pass 对一致？[R1-Q3, R2 AGREE]

5. Register 轴是否做了 rewriter 替换测试（类似 Appendix D 的 verbosity/formality 测试）？[R2-Q4, R1 AGREE]

6. TOST Δ=15pp 的定量推导？Δ=10/12/15/20pp 下 TOST 结果如何变化？[R1-Q6, R2 AGREE]

7. Claude 不表现 Blindspot 的可能机制？是否与 RLHF 策略差异有关？[R2-Q2]

---

## Missing References

无必须添加的遗漏引用。可选增强：
- Millsap (2011), *Statistical Approaches to Measurement Invariance* — 强化 measurement-mode divergence 理论基础 [R1]
- Cattelan (2012), *Models for Paired Comparison Data* — BT 模型假设讨论 [R1]
- Bai et al. (2022/2023), RLHF preference model comparison vs rating 差异 [R2]
- Rafailov et al. (2023), DPO 中 pairwise preference 的理论性质 [R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置中未启用 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warnings, 10 info）。

**Warnings**:
1. 第 8 页为纯文本页（§5.4 Robustness + §6 Conclusion + Limitations），无 display item。与第 3 页共同构成两段纯文本区域，但未连续出现，节奏可接受。
2. 末页（p.18）仅 4 条参考文献，大面积空白。属 references 结尾自然情况。

**Positives**:
- 主正文 8 页含 4 figures + 3 tables = 7 display items，密度 0.875/页
- Figure/Table 分布均匀（pp.2, 4, 5, 6, 7），无连续纯文本超 2 页
- 所有 Table 使用 booktabs 风格，无竖线
- 无 LaTeX 渲染错误、无 margin 溢出、行号正常（ARR review 格式）
- ACL 匿名模板 + double-blind 合规

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Confidence: 4/5**

| 维度 | R1 | R2 | Director |
|------|----|----|----------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Novelty | — | 3.0 | 3.0 |
| Excitement | 3.5 | 3.0 | 3.0 |
| Overall | 3.5 | 3.0 | **3.0** |

**评分依据**:

本文在实验设计和统计方法上达到了 Conference 水准——CSD 三层控制、7 种统计方法三角验证、GEE per-axis confound 分解构成扎实的方法论贡献。跨 4 个 judge、3 个 benchmark 的验证提供了强鲁棒性证据。

评分停留在 Findings (3.0) 的核心原因：

1. **Framing 不对称 [Must-Fix]**: 标题、摘要、结论的主叙事预设 pairwise 为 ground truth，而论文自身数据无法区分 measurement attenuation / format amplification / construct divergence 三种解释。这不是局部措辞问题，而是贯穿论文的解释框架偏差。

2. **新颖性有限**: Likert vs pairwise 灵敏度差异是心理测量学 established knowledge（Thurstone 1927 以降）。受控量化 + GEE 分解有方法论价值，但核心洞察（"forced-choice 比 rating scale 更灵敏"）对跨领域读者非全新。GEE per-axis decomposition 是真正的增量贡献，但单独不足以支撑 Conference 水平。

3. **多个技术问题待解**: 人工标注规模不足（50 pairs, κ=0.44）、TOST 阈值与最小偏差重叠（Δ=15pp vs 13pp）、Table 1 方向不对称未调整、NLI gate 选择偏差检查不全面。

**升级路径**:
- 修正 framing（Abstract/Conclusion 给三种解释同等权重）→ **3.5 (Borderline Conference)**
- + 扩展人工标注（≥100 对 + 第 3 标注员）+ TOST 敏感性分析 → **4.0 (Conference) 可能**

---

## Detailed Comments

### §1 Introduction
- 开头 motivating example（GPT-4o formal vs casual）应紧随其后 acknowledge formality-quality nuance，而非推迟至 Limitations/Appendix A
- "This is the Likert Blindspot" → "We term this the Likert Blindspot"
- 增加一句明确承认心理测量学先例

### §3 Method
- §3.2 NLI gate 的选择偏差讨论应增加 instruction type/topic 维度
- §3.5 Design Rationale 因果声明已审慎，无需修改

### §4 Experiments
- §4.1 脚注 3（BT IIA）应补充一维性假设说明
- Table 1 formality 行应添加脚注提示方向不对称效应
- Table 2 标注 "GEE (Likert-outcome)" 以区分 Table 3

### §5 Analysis
- §5.1 construct validity 讨论需扩展：明确区分 "measurement sensitivity gap" 和 "construct divergence"，论证 RLHF 语境下的实践重要性
- §5.2 GEE 术语首次出现时应提供直觉解释
- §5.4 amplification controls 中应更显式回应 Comparative Trap

### §6 Conclusion
- "Likert-only audits miss style-driven preferences" 应加 hedge（不能排除 power 解释和 format amplification 解释）

### Appendices
- Appendix G: 增加 TOST Δ=10/12/15/20pp 敏感性分析
- Appendix M: 注明 100-point Likert 仅用 Qwen3-32B 的 evaluator-producer overlap 限制
- Appendix R: 主文应明确承认 d=−0.23 超阈值并引导到 GEE covariate 缓解分析
- Bootstrap CI: 明确指定 percentile vs BCa 方法

### 格式合规
- ✅ 正文 ≤8 页合规（§1-§6 结束于 p.8 上半部分，Limitations 从 p.8 下半开始不计入）
- ✅ Double-blind 合规（"Anonymous ACL submission"，无作者信息泄露）
- ✅ Limitations 合规（覆盖 quality-style confounding、evaluator-producer bias、scope 三维度，简洁，无新实验结果）
- ✅ 参考文献格式规范