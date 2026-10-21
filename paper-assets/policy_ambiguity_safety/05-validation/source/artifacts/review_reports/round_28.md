---
round: 28
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T20:01:45.405690+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: True
---

# Round 28 审稿报告（最终版）

**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety
**Venue**: EMNLP 2026 (ARR May cycle)
**审稿日期**: 2026-05-23
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**流程**: Round 1 独立初审 → 交叉分享 → R1 结构化 9 维度审稿 → 第二轮交叉分享 → 收敛

---

## Summary

本文通过匹配对因果设计研究策略文本歧义对 LLM agent 安全违规的影响。在 τ²-bench 上使用 300 个 clause pairs（六类型分类法）×5 个模型（2,997 episodes），发现歧义条款使违规率增加 34.0pp（排除 incompleteness 后 31.0pp）。论文进一步发现 type–mechanism dissociation（V=0.45 LLM-coded）、disambiguation neglect（4.6% 意识率）和 systematic nocuity（41.3% 收敛违规，77% 偏向宽容解释）。SOPBench 跨基准复制确认方向一致（+12.7pp）。

---

## Strengths

1. **C1 因果证据链完整**：matched-pair 设计正确隔离歧义作为 IV；perturbation control（Δ=-0.67pp, CI 含零）、within-family ICC=0.919、SOPBench 跨基准复制、7 模型跨 6 provider 均为正效应——因果推断在 agent safety 领域属方法论质变。[两轮审稿一致共识]

2. **统计方法规范**：McNemar 配对检验、TOST 7-margin 敏感性分析、Holm-Bonferroni 校正、bootstrap cluster analysis (B=10,000)。C3 未通过校正后正确标记为 inconclusive，C4 标记为 exploratory——显示严格统计纪律。[R1 两轮均重点肯定]

3. **Cross-judge validation 全面**：三独立 judge Fleiss' κ=0.717，无 same-family leniency（Claude judge 对 Claude agent 更严格而非更宽松）。Human validation (inter-annotator κ=0.798, human-LLM κ=0.733) 确认违规检测可靠性。[共识]

4. **Disambiguation neglect (4.6%) 量化**：将 ambiguity collapse (Liu et al. 2023) 从表示层面扩展到行为层面。Qwen3/DeepSeek 零意识 vs GPT-4.1/Claude 10-11% 的模型分化有独立研究价值。[共识]

5. **Claims 标定诚实**：C1/C2 supported, C3 inconclusive, C4 exploratory, incompleteness 效应标为 upper bound。15 页高质量附录覆盖几乎所有可预期疑问。[共识]

6. **格式合规**：Abstract ~160 词（<200 限制），double-blind 匿名完整。[共识]

---

## Weaknesses

### Must-Fix（3 项，两轮稳定）

**MF1** Type–mechanism dissociation "establishes" 与 [Exploratory] 标签矛盾

Abstract "establishes the taxonomy as a diagnostic instrument" vs §6 标题 [Exploratory] vs Introduction contribution (3) "exploratory"——同一论文中对同一发现定位摇摆。Failure mechanism 编码 human κ=0.15（collapsed 后 0.34-0.52），远低于 LLM coder κ=0.52。Abstract 仅报告 collapsed κ=0.34-0.52，省略原始 κ=0.15。

R1 第二轮进一步分析：论文声称 ICC pattern、failure modes、violation rates 构成 "convergent evidence"，但三个 evidence streams 共享实验平台和 LLM measurement tools，独立性打折扣——evidence 是 partially convergent 而非 fully convergent。

**修改要求**：(a) "establishes" → "suggests"/"provides exploratory evidence for"；(b) Abstract 加入 κ=0.15；(c) 讨论 LLM coder 一致性高于人间的可能解释；(d) 降低 convergent evidence 的措辞。

**R1 明确表示：满足此条件是从 3.5 升至 4.0 的前提之一。**

---

**MF2** Clause pair 构建方法描述自相矛盾

§4.2 "template-based pipeline" vs Appendix T "hand-crafted, no automated over-generation"。两位 Reviewer 共识 [AGREE]。R2 分析：最可能是 §4.2 表述不准确，实际是人工按模板规范手工编写。

**修改要求**：§4.2 改为 "hand-crafted following structured type-level specifications"。

---

**MF3** 信息添加混淆未在全部高 Δtoken 类型上充分标注

Auth-scope（Δtoken=36.1, 所有类型中最大）与 incompleteness（34.6）同样存在信息添加混淆，但仅 incompleteness 有 † 标注和专项 confound analysis（Appendix F）。R2 补充关键观察：两个效应最大的类型同时也是信息添加最大的类型，而 confound-minimized coreferential 仅 +18.7pp——headline +34.0pp 可能显著高估纯歧义效应。

R1 第二轮进一步指出：perturbation control（同义词替换、clause 重排）保持信息量不变，不覆盖信息添加混淆。缺少理想控制条件（添加等量无关信息或 partial disambiguation）。

**修改要求**：(a) Table 2 对 Δtoken>25 words 的类型均加注信息添加警告；(b) §5.1/Discussion 明确区分 ambiguity-only 效应 (coreferential 18.7pp) 与 mixed effects。

**R1 明确表示：满足此条件是从 3.5 升至 4.0 的前提之一。**

---

### Should-Fix（7 项）

**SF1** Discussion + Conclusion 合计约 150 词，讨论严重不足。缺失：disambiguation neglect 与 sycophancy 关系、systematic nocuity 对 evaluation 范式启示、开发者实操建议、RE 工具链借鉴。R2 列为 MF，R1 降为 SF（8 页限制下的合理 trade-off）。最终定级 SF，但强烈建议扩展至 ~300 词。

**SF2** Berry "nocuous" 术语反转过度修辞。"Inverting Berry" → "Berry's criterion breaks down for LLM agents"。41.3% convergent violations 未按模型家族分析——如果主要在同族模型间收敛，可被 training-data similarity trivially 解释。需补充 cross-family convergence 分析。

**SF3** Cramér's V 跨维度比较方法论缺陷。V=0.45 (6×5) vs V=0.14 (6×2) 归一化因子不同，不可直接比较。建议用 NMI 作主论据。R2 修正 R1 的事实错误：实际为 6×5 而非 6×3，但核心关切成立。

**SF4** Temperature=0 唯一条件。无 temp>0 pilot data。R2 第二轮补充：temp=0 下 convergent nocuity 解读需更谨慎——每个 model-clause pair 仅一个确定性输出，temp>0 下 convergence pattern 可能完全不同。**R1 明确表示：1 model × 2 temp × 50 pairs 的 pilot 是升至 4.0 的前提之一。**

**SF5** 合成刺激生态效度。SOPBench +12.7pp 仅为 τ²-bench 37%，论文三个 post-hoc 解释之外还有一个可信解释：更接近真实 SOP 的歧义效应自然更小。R2 REBUT "96% agreement = 任务过简"——高分类一致性是实验设计优点（标注者带 taxonomy 定义做分类 vs LLM 无标签执行任务，认知任务不同）。R1 在第二轮未反驳此 REBUT → 该分歧部分消解。

**SF6** `\enlargethispage{26\baselineskip}` ≈ 4.3 inches 页面扩展，几乎肯定超出 ACL bottom margin 要求。

**SF7** Judge prompt template 未完整披露。论文未提供 evaluation judge 的完整 prompt（分类 none/minor/moderate/critical 的指令）。Appendix AB 提及 "the same rubric and prompt template" 但未附全文。对可复现性至关重要。[R1 第二轮结构化审稿新发现]

---

### Minor（6 项）

- **M1**: §5.1 McNemar OR=15.1 基于 discordant pairs (n=580)，应在首次报告时重申。
- **M2**: Conclusion ">89% disambiguation neglect" 来源不明确。建议改用 overall 95.4% 或标注 "range: 89–100%"。
- **M3**: Prevalence audit κ=0.295 很低但报告 87%——R2 补充：低 κ + 高 prevalence 可能反映标注者各自的宽松倾向（base-rate 效应）。
- **M4**: SOPBench +12.7pp 是 unweighted mean，应标注。
- **M5**: τ²-bench policy injection 技术细节不足（如何定位原始 clause、context preservation、boundary effects）。[R1 第二轮新发现]
- **M6**: Human annotator 资质和培训细节不足——§4.2 和 Appendix AF 的标注者是否为同一人？是否有 mechanism 分类培训？如果 human κ=0.15 部分反映培训不足而非分类体系问题，应澄清。[R1 第二轮新发现]

---

## Reviewer Consensus（跨两轮稳定）

两位 Reviewer 在以下问题上跨两轮保持共识 [AGREE]：
- Type-mechanism dissociation "establishes" 过度表述 (MF1)
- Clause pair 构建描述矛盾 (MF2)
- 信息添加混淆范围需扩展 (MF3)
- Discussion/Conclusion 过短 (SF1)
- Berry 术语反转需更深入论证 (SF2)
- V 跨维度比较缺陷 (SF3)
- Temperature=0 泛化局限 (SF4)
- SOPBench 效应差异需更多讨论 (SF5)
- C1 因果设计是论文最强贡献
- Disambiguation neglect 4.6% 是有价值的发现
- Claims 标定诚实是高质量实证论文标志

## Reviewer Divergence

- **Excitement 评分**：R1 给 3.5/5（"core finding 'ambiguity hurts' 不 surprising，excitement 来自操作化而非理论突破"），R2 可能给 4/5（更看重概念贡献 convergent nocuity 和方法论质变）。
- **96% agreement 解释**：R1 认为暗示任务过简，R2 REBUT 认为是实验设计优点。R1 第二轮未反驳 → 分歧部分消解。
- **"Ambiguity" 广义定义**：R2 认为影响 headline result，R1 REBUT 认为 §3 处理充分。→ 不列为修改要求。
- **Overall 评分**：R1 稳定在 3.5（两轮一致），R2 从 3.5 可能上调至 4.0。

---

## Questions

1. §4.2 "template-based pipeline" 和 Appendix T "hand-crafted" 的矛盾如何解释？
2. 41.3% convergent violations 中，同族模型间收敛 vs 跨厂商收敛的比例？
3. Auth-scope 是否可提供类似 incompleteness 的专项 confound analysis？
4. 是否有任何 temperature>0 pilot data 或计划？
5. Human mechanism coding 标注者是否接受了系统培训？
6. "Diagnostic instrument" 的预期端到端 workflow 是什么？
7. Evaluation judge prompt template 能否完整披露？
8. τ²-bench policy injection 的技术实现细节？

---

## Missing References

无重大遗漏。可选补充：
- D'Amour et al. (2022) "Underspecification Presents Challenges for Credibility in Modern Machine Learning" [两位 Reviewer 共识]
- Constitutional AI / RLHF 文献，解释不同 safety training 导致不同 ambiguity vulnerability profiles [R1 第二轮建议]

---

## External Review

**外部审稿**：未请求。

---

## Visual Layout Check（非评分项）

已完成（0 critical, 1 warning, 6 info）：
- **[warning]** Pages 1-2 连续纯文本无 display item，Figure 1 直到 page 3 才出现
- **[info]** Page 5 整页 Method 纯文本；Page 6 Figure 2 灰度区分度不足；Page 8 热力图字号偏小；Pages 13/18 Appendix 表格密集；Page 23 约 60% 填充

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 4 | **3.5** |
| Excitement | 3.5 | 3-4 | **3.5** |
| Reproducibility | 3.5 | 4 | **3.5** |
| Overall | 3.5 | 3.5-4.0 | **3.5** |
| Confidence | 4 | 4 | **4** |

**Overall Assessment: 3.5 / 5（Borderline Conference）**

**评分理由**：C1（歧义→违规 +34pp 因果效应）实验设计扎实、控制链完整，是对该领域的方法论质变——这是论文最强且无争议的贡献。Disambiguation neglect (4.6%) 和 systematic nocuity (77% permissive) 是有价值的实证发现。但论文的核心概念重构——type–mechanism dissociation 作为 "diagnostic instrument"——依赖 human κ=0.15 的 failure mechanism 编码，evidence 不足以支撑 "establishes" 级别的 claim。三个 Must-Fix（措辞过度、构建描述矛盾、信息添加混淆标注不完整）和七个 Should-Fix 叠加，使论文停留在 Borderline Conference。

**升级路径（R1 明确条件）**：
1. "establishes" → "suggests"（文字修改，camera-ready 可完成）
2. auth-scope 和 incompleteness 同时标注信息添加混淆，区分 confound-free 效应和 mixed 效应（文字修改，camera-ready 可完成）
3. 至少 1 model × 2 temperature × 50 pairs 的 pilot（需额外实验）

满足 (1)(2) 即可显著提升论文可信度；(3) 是 ideal 但非必需。

**EMNLP 2026 标准映射**：3.5 = Borderline Conference。如果 MF1-MF3 得到充分解决，论文有潜力达到 4.0（Conference / Main）。AC 可据 R1（偏方法严谨性，稳定 3.5）和 R2（偏概念贡献，3.5-4.0）的不同视角做最终判断。