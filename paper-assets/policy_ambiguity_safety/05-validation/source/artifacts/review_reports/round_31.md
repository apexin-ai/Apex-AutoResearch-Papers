---
round: 31
review_mode: fresh
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-24T12:07:07.510392+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## 审稿报告 — Round 31 (Fresh Review)

**Paper**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety"
**Venue**: EMNLP 2026 via ARR May cycle (Long paper, 8-page limit)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 格式合规 + 完整性)
**交叉回应**: 已完成，高度收敛

---

### Summary

本文研究政策模糊性与 LLM agent 安全违规之间的因果关系。采用 matched-pair 设计，在 τ²-bench 上构建 300 对模糊/清晰条款，跨 5 个模型评估 2,997 个 episode。核心发现：(C1) 模糊条款增加 +34.0 pp 违规率（排除 incompleteness 后 +31.0 pp），SOPBench 交叉验证 +12.7 pp，医疗领域 +58.8 pp；(C2) "convergent nocuity"——41.3% 的模糊条款在多模型间触发一致性违规（Jaccard=0.46 cross-family），77% 为 permissive bias，使基于一致性的安全监控失效；(C3) 探索性 type-mechanism dissociation（V=0.45, LLM-coded; human κ=0.41）。

---

### Strengths

**S1. 严谨的因果方法论**：Matched-pair 设计通过 within-clause 对比隔离模糊性效应，排除条款特征混杂。Δtoken 控制、perturbation control、TOST equivalence testing 构成完整的方法论框架。

**S2. 大且稳健的效应量**：+34.0 pp 主效应经多维度验证——排除 incompleteness (+31.0 pp)、confound-minimized coreferential type (+18.7 pp)、SOPBench 交叉基准 (+12.7 pp, 5/5 models Δ>0)、医疗领域扩展 (+58.8 pp)。效应非模型特异、非领域特异。

**S3. 原创性概念贡献**："Convergent nocuity" 是对 Berry (2004) nocuous/innocuous distinction 的有意义扩展。LLM agent 因共享训练偏差而收敛到相同错误解释——这使基于 inter-agent agreement 的安全监控系统失效，具有直接的部署安全含义。

**S4. 全面的验证体系**：Temperature pilot (3/5 models)、三家族 judge 验证 (Fleiss' κ=0.717)、100 episode 人工验证 (severity κ=1.00)、variance decomposition、TOST sensitivity analysis (7 margins)。

**S5. 实用的方差分解发现**：Clause wording 解释 22.4% 方差 vs type 仅 0.4%，直接支持 clause-level auditing 优于 type-level screening 的实践建议。

---

### Weaknesses

#### Must-Fix (Critical)

**MF1. C3 type-mechanism dissociation 可信度受限于 human κ=0.41 [R1-N1 + R2 AGREE; R30-MF1 复发，首次 R22]**

V=0.45 来自 LLM coding (κ=0.52)，human collapsed κ=0.41 低于常规可靠性阈值 (α≥0.667)。论文自身在 §6 承认 LLM higher agreement "may reflect shared classification conventions — a meta-level parallel to convergent nocuity"——这实质上是对 V=0.45 可靠性的自我质疑。

Abstract 仅报告 V=0.45 (LLM-coded) 而省略 human κ=0.41，存在单侧 framing 偏差。Introduction 的 contribution (3) 虽加了 "exploratory" 和 "preliminary evidence" 修饰语，但仍与 C1、C2 并列呈现，给读者 C3 权重与 C1/C2 相当的印象。

此问题自 Round 22 起持续存在，历经 R28（κ=0.15）、R29（re-annotation 至 κ=0.41）、R30（部分降级），至今未根本解决。

**建议**：(a) 将 C3 从 Introduction contribution list 移至 §6 的 exploratory observation（推荐）；或 (b) 在 abstract 中将 C3 压缩至一个从句级别的简述，明确标注 "exploratory, limited by human agreement"。

**MF2. \enlargethispage 格式操纵——3 处 ×4\baselineskip + float spacing 压缩 [R2-N1; R1 初审漏判; R30-MF2 复发，首次 R28]**

经源码验证确认：
- `\enlargethispage{4\baselineskip}` × 3（method.tex:24, experiments.tex:6, experiments.tex:64），共挤出 ~12 行
- `\setlength{\textfloatsep}{8pt}` + `\setlength{\floatsep}{6pt}`（main.tex:17-18）进一步压缩浮动体间距

R30 的修复仅将原先极端值（8+18+8 baselineskip）降至当前 4+4+4，但命令仍在。去除所有 \enlargethispage 后，§7 Discussion 将溢出至第 9 页。ARR 审稿人常规检查 LaTeX 源码，此类格式操纵是 desk rejection 风险因素。

R1 在初审中将正文 8 页判为合规 ✅，R2 在交叉回应中 REBUT 此判断，指出合规性完全依赖于格式操纵。

**建议**：彻底移除所有 \enlargethispage 命令，通过实质性内容裁减确保 ≤8 页。

#### Should-Fix (Warning)

**SF1. SOPBench 效应衰减 63% 缺乏量化分析 [R1-W1 + R2-W4 AGREE; R30-SF1 复发，首次 R28]**

合成条件 +34.0 pp → 自然条件 +12.7 pp 的 63% 衰减在 §7 Discussion 中仅定性列出三个效应量级（+34.0/+12.7/+58.8 pp），未量化分析衰减来源。三个候选解释——(1) 合成 vs 自然模糊性、(2) 评估标准差异、(3) 完整 SOP 文档的上下文消歧效应——均未分离各自贡献。

**建议**：§7 用 ~120 words 结构化分析段落替代效应量列表，按因果解释力排序。

**SF2. Cross-judge 术语误导 [R1-N2 Must-Fix → R2 降级 Should-Fix; 共识 Should-Fix; R30-SF4 复发]**

"Cross-judge" 暗示 cross-family validation，但主评估中 GPT-5.4 和 GPT-4.1 同属 OpenAI。Appendix AC 的三家族验证 (GPT-5.4, GPT-4.1, Claude Sonnet 4.6) 达到 Fleiss' κ=0.717 (substantial agreement)，实质上排除了 OpenAI-specific tendencies，但此关键结果仅在附录中。

R2 关于降级的论据被采纳：(1) Δpp 为 within-judge 计算，不受 judge family 影响——这是 C1/C2 的基础；(2) Fleiss' κ=0.717 已提供 cross-family 验证。

**建议**：全文 "cross-judge" → "cross-model judge assignment"；§4.4 正文引用 Fleiss' κ=0.717。

**SF3. SESOI ±15 pp 正文缺领域锚定引用 [R1-W2; R2 部分同意; R30-SF3 复发]**

SESOI 从 noise 推导（perturbation control upper CI × 2）而非 domain consequences。但 Appendix A 已有 7-margin TOST sensitivity analysis 和 cost anchoring ($15k-$750k)。正文 method.tex:33 称 "pragmatic default, not a principled domain-anchored threshold" 却未引用附录中已有的成本锚定——过度自谦。

**建议**：§4.5 引用 Appendix A cost anchoring 作为补充论据。

**SF4. Temperature pilot 统计 power 有限 [R1-W3 + R2 AGREE; R30-SF2 复发]**

3/5 models × 50 clause pairs 的 pilot 仅报告 agreement rate，未报告效应量 CI 或量化 detectable effect size。Limitations 已定性承认（"two models and extreme-temperature regimes remain untested"）但缺少量化。

**建议**：§4 或 Limitations 量化 pilot 的 statistical power（detectable effect size at 80% power）。

**SF5. Incompleteness information-addition confound 控制不完全 [R1-W4 + R2 AGREE]**

Token count 是信息量的粗糙 proxy。Logistic regression 控制 Δtoken 但不能完全排除 confound。论文使用 dagger footnote + excluding-incompleteness 效应 (+31.0 pp) + coreferential 作为 confound-minimized type，策略合理但不完美。R2 补充指出 authorization scope 也存在类似 confound（Δtoken=36.1 words），R1 未涉及。

**SF6. Authorization scope 测量质量差 [R2 独立发现; 新 issue R31-SF1]**

Per-type κ=0.385，跨 judge 违规率范围 12-64%（Appendix AC）。三个 judge 方向一致但幅度差异大（GPT 52 pp range, Claude 30 pp, Gemini 24 pp）。此类型的结论可靠性显著低于其他类型，但未在 Limitations 中标注。

#### Minor

**M1.** Per-type κ 的 CI 很宽（n≈17 per type），应加显式 caveat [R1-M2 + R2 AGREE]

**M2.** "Primary risk factor"（§5.1）应限定为 "among measured predictors"——论文仅测量 type/condition/model 三个因素 [R1-M3 + R2 AGREE]

**M3.** C3 hierarchy hypothesis rejection (p=0.017 > Bonferroni α=0.0125) 应更显式标注 [R2]

**M4.** API 调用日期 (May 20, 2026) 与投稿间隔极短——不影响 reproducibility (temperature=0 + API version 固定) 但 revision 期间 API 行为可能已变 [R1-M4 + R2 AGREE]

---

### Questions for Authors

1. 如果移除所有三处 \enlargethispage 命令，正文超出第 8 页多少行？计划裁减哪些具体内容实现合规？

2. 是否能提供仅基于 human annotation 计算的 C3 type-mechanism V 统计量（不含 LLM coding），以分离两个证据流？

3. Authorization scope (κ=0.385) 的 12-64% 范围中，多少比例归因于 judge disagreement vs 真实的 model-level variation？

4. 如果将 C3 从 contribution list 移至 §6 exploratory observation，对论文叙事结构和投稿竞争力的影响如何评估？

---

### Missing References

未发现关键遗漏引用。Related work 覆盖范围与论文声称匹配。

---

### External Review

**状态**：未请求

---

### Visual Layout Check (非评分项)

**状态**：✅ 完成（10 条 info 级发现，0 critical，0 warning）

主要观察：
- Page 1 纯文本无视觉锚点（Figure 1 在 page 2 顶部，距离可接受）
- Page 5 Method (§4.1-4.5) 纯文本密集——§4.2 Matched-Pair Design 附近可考虑增加流程示意图
- Figure 2 (page 6) 尺寸偏小（~1/3 栏高），标注紧凑但可读
- Table 2 脚注 (page 7) 字号小，†/‡ 标记的方法论注释较难注意——ACL 表格脚注常规做法
- Appendix pages 13/19 表格密度极高（4-5 tables/page）——附录可接受
- 末页 ~40% 空白（AI assistance 声明后）

---

### Overall Assessment

**Score: 3.5 — Borderline Conference**

**核心评价**：本文提出了一项方法论严谨的 matched-pair 因果研究，核心发现（C1: +34.0 pp 效应，C2: convergent nocuity）具有扎实的实验支撑和重要的实际安全含义。"Convergent nocuity" 作为概念贡献是新颖且及时的——它揭示了基于 agent 一致性的安全监控的根本盲区。

**阻碍升分的关键问题**：
1. **C3 framing 膨胀**（R22 起持续至今）：human κ=0.41 不足以支撑将 type-mechanism dissociation 作为与 C1/C2 并列的贡献。论文在 abstract/introduction 中给予 C3 过高的呈现权重，与其在 §6 标题中标注的 [Exploratory] 定位不一致。
2. **格式合规条件性**（R28 起持续至今）：正文 8 页完全依赖 3 处 \enlargethispage 命令 + float spacing 压缩，是 desk rejection 风险。
3. **生态效度差距未量化**（R28 起持续至今）：合成-自然效应 63% 衰减缺乏结构化解释。

**升至 Conference (4.0) 的路径**：
- MF1：C3 降级为 §6 exploratory observation
- MF2：移除所有 \enlargethispage，通过实质内容裁减实现合规
- SF1：SOPBench 衰减结构化分析
- SF2：cross-judge → cross-model judge assignment + 正文引用 Fleiss' κ

**复发问题的关注**：MF1 (9 rounds)、MF2 (3 rounds)、SF1 (3 rounds) 的持续复发令人担忧。核心 C1+C2 贡献足以支撑一篇 Conference 级论文，但 C3 framing 膨胀和格式问题反复拖累评分。

---

### Detailed Comments

| Reviewer | Initial Score | Key Findings | Cross-Response |
|----------|--------------|--------------|----------------|
| R1 | 3.5 | 2 Must-Fix (C3 κ, cross-judge family), 4 Should-Fix, 4 Minor | R2: 高度同意；将 R1-N2 cross-judge 从 Must-Fix 降级为 Should-Fix（Fleiss' κ=0.717 + Δpp 不受影响）；REBUT R1 格式合规判断（\enlargethispage 遗漏）|
| R2 | 3.5 | 1 Must-Fix (\enlargethispage), 4 Should-Fix (authorization scope, SOPBench, C3 framing, hierarchy), 4 Minor | R1: 核心同意；接受 \enlargethispage 发现；确认 authorization scope 问题 |

**Reviewer 间共识点**：C3 可信度受限 (MF1)、SOPBench 衰减 (SF1)、核心方法论和 C1/C2 扎实
**Reviewer 间分歧点**：cross-judge severity（R1 Must-Fix → 共识 Should-Fix）、\enlargethispage（R1 遗漏 → R2 发现）
**格式合规**：❌ 条件性——正文 8 页依赖格式操纵。Abstract ~140 words ✅。匿名化 ✅。