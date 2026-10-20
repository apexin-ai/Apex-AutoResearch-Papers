---
round: 17
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T18:02:05.347373+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 17 审稿报告
## Paper: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
## Venue: EMNLP 2026 via ARR May cycle | Deadline: 2026-05-25
## Reviewers: R1 (方法严谨性) + R2 (新颖性/完整性) | 1 轮初审 + 1 轮交叉

---

## Summary

本文研究自然语言政策歧义对 LLM agent 安全的因果效应。作者构建 300 对 matched clause pairs（六类歧义 taxonomy），在 τ²-bench 客户服务策略上用五个模型生成 2,997 episodes，由 GPT-5.4/GPT-4.1 交叉评判。核心发现：歧义条款使违规率升高 34.0 pp（OR=15.1）；clause wording 解释 22.4% 违规方差（vs. type 0.4%, model 1.0%）；type membership 对失败机制的预测力是对违规率的 30× (MI ratio)；41.3% 歧义条款触发跨模型趋同违规。

---

## Strengths

1. **因果设计首创性** [R1-S1, R2 共识]：Matched-pair + perturbation control 在 agent safety 领域是首个严格因果设计。Perturbation control (Δ=-0.67pp, CI含零) 有效排除表面文本混淆。
2. **统计分析深度超越领域平均** [R1-S2, R2-S2]：TOST 7-margin sensitivity、bootstrap cluster (Appendix I)、Holm-Bonferroni (Appendix K)、confound regression (Appendix F/H)、leave-one-out (Appendix J) 多层验证。
3. **局限性透明披露罕见** [R1-S3]：主动报告 cross-judge ρ=0.09、incompleteness confound、auth scope κ=0.385、margin dependence——在 agent safety 领域少见。
4. **七模型跨六 provider 复制** [R1-S4]：C1 在所有模型上显著 (Δ=+20.0 to +39.0pp)，包括 Gemini/LLaMA replication families (Appendix E)。
5. **Taxonomy-as-diagnostic-tool 重新定位** [R1-S5, R2-S3]：将分类法从风险预测转为失败机制诊断，由 MI 分析 (Appendix S) 定量支撑。
6. **Systematic nocuity 概念** [R2-S4]：41.3% 条款导致 ≥3/5 模型趋同到同一错误解读，83.9% 共享相同 dominant failure mode。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-N1 [critical, consensus] "30×" MI ratio 因未归一化而夸大约 2 倍**
- 位置：Abstract, Section 1, Section 5.1, Section 7, Section 8, Appendix S
- 问题：mechanism 是 3-way 分类 (entropy ceiling ≈ 1.58 bits)，violation 是 binary (ceiling = 1.0 bit)。Raw MI ratio ≈ 29.1 → "30×"，但 NMI ratio ≈ 16.6×。Appendix S Table 13 已报告 NMI 数字，但正文一律使用 raw ratio。
- 影响："30×" 贯穿全文五个位置，是核心 framing device。定性结论不受影响，但定量表述被夸大约 2 倍。
- R1 提出，R2 未反驳。
- **建议**：改用 NMI (~17×) 或报告范围 ("16–30×, depending on normalization")，正文说明选择理由。

**W-N2 [critical, R1 only but uncontested] LPM 方差分解在二元结果上的 22.4% 可靠性存疑**
- 位置：Section 5.1, footnote 2
- 问题：Type III SS 处理二元结果 = 线性概率模型 (LPM)，异方差性和 [0,1] 限制被违反。300-level clause factor 消耗 ~10% df，null hypothesis 下随机 300-level 因子可解释 ~10% 方差，观测 22.4% 仅约 null 的 2×。脚注的 logistic pseudo-R²=0.175 与 LPM R² 不可比。
- 影响："clause wording explains 22.4% of variance" 是三大贡献之一，支撑 taxonomy-as-diagnostic-tool 论证。
- R2 未回应此问题。
- **建议**：补充 GLMM 方差分解 (Tjur's R² 或 random-effects) + permutation null comparison。

### Should-Fix（影响评分但不一票否决）

**W-S1 [warning, consensus] 单一 benchmark/领域限制 C2 泛化性**
- Cross-domain type ranking ρ=0.26 (p=0.62, Appendix U)。Abstract/conclusion 已限定 "customer-service domains"，但标题 ("LLM Agent Safety") 和 Discussion ("policy-governed deployments") 偏广。C1 主效应有 cross-domain robustness (interaction p=0.187)，domain-dependent 的是 C2 type ranking。
- R2 定 critical，R1 定 should-fix (domain qualification 已存在)。Director 采信 should-fix：需措辞强化，不需实验重做。

**W-S2 [warning, consensus] Information delta confound 控制粒度不足**
- Unambiguous variants 系统性更长 (incompleteness +34.6 words, auth scope +36.1 words)。论文提供四层控制（logistic regression p=0.022, counter-evidence, confound-free lower bound +18.7pp, sans-incompleteness Δ=31.0pp），但 token count 作为信息量代理粒度粗糙。
- 建议正文更突出讨论此局限性。

**W-S3 [warning, R1] OpenAI-only judges 在 C4 中混淆 judge identity 与 model identity**
- GPT-5.4 评 Claude/GPT-4.1/Qwen3，GPT-4.1 评 GPT-5.4/DeepSeek。C1 不受影响（matched-pair 消除 bias），但 C4 model×type interaction 中 judge 和 model 完全混淆。Human validation n=100 不足以 per-model 验证。
- 建议增加非 OpenAI judge robustness check 或在 C4 中更明确标注 caveat。

**W-S4 [warning, R1] Coreferential 作为 confound-free lower bound 但被排除出 replication/mitigation**
- Coreferential (+18.7pp, token delta=0) 被赋予重要论证角色但缺乏独立验证（排除理由：benchmark-specific structural constraints）。
- 建议讨论排除对 lower-bound 论证的影响。

### Minor

- **M1** [R2→R1 agree as minor]: Systematic nocuity ≥3/5 阈值缺乏显式 justification。5/5 (13%) 已报告，建议增加 ≥2/5, ≥4/5 比例。
- **M2** [R1]: Table 2 CI 使用 Newcombe CI 而非 matched-pair Agresti-Min CI。不影响结论。
- **M3** [R1]: Section 5.2 "Three pairs never reach equivalence at ±20pp" 需与 Table A1 交叉验证。
- **M4** [R1]: Error analysis inter-coder κ=0.52 (moderate)，人工验证子集更有说服力。
- **M5** [R1]: Temperature=0 非完全确定性；ICC=0.919 仅 OpenAI 家族内。
- **M6** [R2]: "Nocuous" 对非母语读者不直观，建议 abstract 加括号定义。
- **M7** [R2]: Figure 2 黑白打印区分度不足。
- **M8** [R2]: Table 2 caption 可更详细。

---

## Reviewer Consensus

| 议题 | R1 | R2 | 结论 |
|------|----|----|------|
| 30× MI 夸大 | critical | 未反驳 | **Must-Fix** |
| LPM 方差分解 22.4% | critical | 未回应 | **Must-Fix** |
| 单一 benchmark scope | should-fix | critical | **Should-Fix** |
| Information confound | should-fix | should-fix | **Should-Fix** |
| OpenAI-only judges C4 | should-fix | — | **Should-Fix** |
| Coreferential 排除 | should-fix | — | **Should-Fix** |
| Taxonomy vs DRIP-R | REBUT (2/6≠4/6) | critical | **降级 info** |
| Judge κ_w 数字 | 纠正 0.775 | 0.735 (误) | **R2 数字有误** |
| Safety training 讨论 | REBUT (已在 §5.4) | should-fix | **已讨论** |
| Nocuity 阈值 | minor | should-fix | **Minor** |

## Reviewer Divergence

1. **Taxonomy 新颖性 (R2-N1)**：R2 声称 4/6 类型与 DRIP-R 重叠 → critical。R1 引用 Appendix L 反驳：实际仅 scopal + coreferential 两类直接对应 DRIP-R，其余四类 (lexical, auth scope, incompleteness, cond. precedence) 是 policy-specific phenomena。Director 采信 R1 的事实基础，降级为 info（建议正文更清晰区分）。
2. **单一 benchmark 严重程度**：R2 定 critical（需额外领域验证），R1 定 should-fix（C1 有 domain robustness，abstract/conclusion 已限定 domain）。Director 定 should-fix。

⚠️ **R2 审稿中的数字引用错误**：R1 在交叉回应中指出 R2 至少有 4 处数字引用错误——incompleteness delta (+31.6→实为+34.6)、Claude 违规率 (38.1%→实为30.3%)、κ_w (0.735→实为0.775)、Kendall's W (0.308→实为0.398)。这些错误导致 R2 的 W2 (judge agreement) 和 W4 (safety training) 严重程度被高估。Director 已据此调整相关 concern 的定级。

---

## Questions

1. 22.4% 方差分解在 GLMM (clause as random effect) 框架下是多少？是否显著高于 300-level 随机因子的 null expectation？
2. Cross-domain per-model type ranking 是否有模型表现出更好的一致性？
3. Perturbation control 的 300 episodes 使用的是 ambiguous 还是 unambiguous 原始条款？
4. 如直接用 DRIP-R 5 类重新分析，type-mechanism MI 是否仍显著？
5. Disambiguation awareness 4.6% 是否受 τ²-bench system prompt 不鼓励提问的影响？

---

## Missing References

- **Agresti & Min (2005)** — matched-pair proportion CI 方法 [R1, 方法论参考]
- **Tjur (2009)** — binary outcome variance decomposition [R1, 方法论参考]
- **Zhou et al. (2023) IFEval** — instruction-following evaluation [R2, R1 agrees 但非必须]
- **Kambhampati et al.** — formal policy specification for LLM agents [R2, R1 agrees 作为 future direction]
- Krakovna et al. (2020) / Di Langosco et al. (2022) [R2 提出, R1 rebut — reward/goal specification 与 policy ambiguity 是不同层面，非必须]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**已跳过**（用户未提交）。

---

## Visual Layout Check（非评分项）

状态：**已完成** (0 critical, 2 warnings, 3 info)

| 严重程度 | 位置 | 发现 |
|----------|------|------|
| ⚠️ warning | pp.4-6 | 连续 3 页纯文本（Method→Controls→Results），无 figure/table 穿插。建议将 Table 2 前移打破纯文本连续性 |
| ⚠️ warning | p.7 | 3 个 display items (Table 2 + Figure 2 + Figure 3) 聚集同一页，与前 3 页纯文本形成节奏失衡 |
| ℹ️ info | p.7 | Figure 2/3 axis labels 字号接近可读下限 (~正文 70%) |
| ℹ️ info | p.7 | Figure 3 多条折线在小空间内辨识度受限，建议检查灰度打印可区分性 |
| ℹ️ info | pp.1-8 | 主文 5 个 display items 对实证论文偏低端 |

注：pp.4-6 纯文本连续性为历史遗留 issue (R10-M6)，本轮 visual check 再次标记。

---

## Overall Assessment

**Overall Score: 3.5 / 5（Borderline Conference）**
**Confidence: 4/5（Confident）**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | **3.5** |

**核心判断**：实验设计在 agent safety 领域是高水平的——matched-pair + perturbation control + 七模型跨六 provider 复制。统计分析深度和局限性透明披露超越领域平均。但两个核心定量 claim 存在方法论问题：(1) "30×" MI ratio 因未归一化而夸大约 2 倍，(2) 22.4% 方差分解在二元结果上使用 LPM 且受 df 膨胀影响。这两个 claim 是论文叙事的关键支柱——修正后定性结论不变但定量表述需调整。单一 benchmark 限制 C2 泛化性但 C1 主效应稳健。

**接收建议**：
- 修正 W-N1 (30× → NMI-based ~17×) + W-N2 (GLMM 方差分解或 null comparison) → 可达 **Conference (4.0)**
- 当前状态：**Borderline Conference / strong Findings**
- 论文不需要额外实验，需要的是方法论措辞修正和统计补充分析

---

## Detailed Comments

**Abstract**: "30×" 需修正为 NMI-based 数字或报告范围。其余准确反映论文贡献，domain 限定 ("customer-service policy domains") 恰当。

**Introduction**: Framing 在历史修订后已准确 ("diagnostic taxonomy" 而非 "intervention framework")。MI 绝对值 (0.41 vs 0.014 bits) 的添加是好的改进。"30×" 需同步修正。

**Section 3 (Taxonomy)**: 六类划分方法论合理。与 DRIP-R 的区分建议从 Appendix L 提取关键对比到正文（1-2 句即可）。两层结构作为 organizational convenience 是恰当的。

**Section 4 (Method)**: 实验设计扎实，perturbation control 有效。建议明确 perturbation clause 来源（ambiguous vs. unambiguous）。

**Section 5 (Results)**: C1 稳健。C2 的 ρ=0.09 caveat 已在 §5.2 显眼位置（历史修订成果）。方差分解需补充 GLMM/null comparison (W-N2)。建议 Discussion 更明确区分 C1 (domain-robust) vs C2 (domain-dependent) 的泛化级别。

**Section 6 (Analysis)**: Systematic nocuity 概念有价值。建议增加阈值敏感性一句话（≥2/5, ≥4/5 比例）。

**Section 7 (Discussion)**: 从 risk prediction 到 failure-mechanism diagnosis 的重新定位论证连贯。"30×" 需同步修正。

**Section 8 (Conclusion)**: 简短准确。与 abstract 重复度较高（历史 info-level issue）。

**Limitations**: 覆盖全面。建议更突出 token count 作为信息量代理的粗糙性 (W-S2)。

**Appendix**: 详尽 (A-U)。建议补充 cond. prec. 和 scopal 的 mitigation prompt 文本 (历史 issue R16-Q5)。