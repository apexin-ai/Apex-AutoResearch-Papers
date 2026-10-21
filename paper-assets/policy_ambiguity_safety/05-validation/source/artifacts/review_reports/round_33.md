---
round: 33
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T14:31:40.230067+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 33 (Fresh Review)

**Paper**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety"
**Venue**: EMNLP 2026 via ARR (May 2026 cycle)
**Review Date**: 2026-05-24
**Reviewers**: R1 (方法严谨性 — 统计方法/实验设计/human validation), R2 (新颖性/完整性 — 概念清晰度/理论框架/表达准确性)
**Protocol**: Round 1 独立初审 → 交叉分享（逐条 AGREE/REBUT）→ 1 轮收敛
**External Review**: 未请求
**Visual Check**: 已完成

---

## Summary

本文通过 300 个匹配 clause pair 的因果实验设计，实证建立了 policy ambiguity 与 customer-service agent safety violation 之间的因果关系。核心发现：歧义条款使违规率增加 +34.0 pp（排除 incompleteness 后 +31.0 pp），五个 frontier 模型均独立显著（all p < 10⁻⁷）。论文提出六类型 ambiguity taxonomy、type-level partial ordering 和 convergent nocuity 概念。跨 benchmark（SOPBench, +12.7 pp）和跨领域（healthcare, +58.8 pp）复制提供外部效度支持。

两位 Reviewer 独立给出 3.5 (Borderline Conference)，交叉分享后评分未变。核心共识：匹配对因果设计和扰动控制是方法论亮点，convergent nocuity 是新颖贡献；但 incompleteness 的概念归属和方法控制、human validation per-type 可靠性差异是制约论文从 Findings 向主会议跨越的两个核心问题。

---

## Strengths

**S1. 匹配对因果设计 + 扰动控制 [R1-S1, R2 共识]**
扰动控制（Δ = 0.07 pp, p = 0.67）有力排除表面文本变化的影响，使因果推断内部效度远超同领域先前的相关性研究。两位 Reviewer 一致认可为最大方法论亮点。

**S2. 五模型一致显著 [R1-S2]**
五个架构各异的 frontier 模型均独立达到显著效应（all p < 10⁻⁷），排除模型特异性解释。

**S3. Convergent nocuity 新颖性 [R1-S3, R2 共识]**
挑战"多模型冗余可提升安全性"的假设。两位 Reviewer 一致认可为最强新颖性贡献。

**S4. Taxonomy annotation 质量 [R1-S4]**
六类型 taxonomy 基于 RE 文献，binary κ = 0.96，six-type κ = 0.95。

**S5. 附录充实度 [R1-S5, R2 共识]**
~16 页附录包含 ~28 个表格和 3 个图，16 个 supplementary 分析。两位 Reviewer 一致标注为"异常优秀"。

**S6. 跨 benchmark + 跨领域复制 [R1-S6, R2]**
SOPBench 和 healthcare pilot 提供方向性外部效度支持。

**S7. 差异化定位清晰 [R2]**
与 DRIP-R / PolicyBank / AgentPex 等近期工作的差异化定位表述清晰。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. Incompleteness 概念归属 + information-addition confound [R2-N2 + R1-W1; 两位 Reviewer 共识]**

两位 Reviewer 从不同角度指出同一问题：
- *概念层面 (R2)*：RE 文献通常将 incompleteness 归为 underspecification 而非 ambiguity。论文将其纳入 ambiguity taxonomy 缺乏充分理论辩护。§3 的 epistemological status 段不够深入。
- *方法层面 (R1)*：Incompleteness 的 unambiguous variant 平均增加 +31.6 words 新内容（远超 coreferential +7.8 words），logistic regression 仅以 token count 为 covariate，无法捕捉信息内容的质变。
- *呈现层面*：Abstract 虽已并列报告 +34.0 pp 和 +31.0 pp，但 +34.0 pp 仍为 headline 数字。

**交叉分享结果**：R1 同意概念关切有理但认为核心结论不依赖此分类（排除后仍 +31.0 pp），建议降级为 Should-Fix。

**Director 裁定**：维持 Must-Fix。Incompleteness 是效应量最高的类型（+49.2 pp），其分类学归属直接影响 taxonomy 的理论完整性。

**建议修改方向**：(1) §3 增加 1-2 段深入讨论 incompleteness 在 RE 文献中的 epistemological status（ambiguity vs. underspecification），提供纳入本 taxonomy 的理论论证；(2) 讨论 information-addition 与 disambiguation 的本质区分；(3) 考虑 token count 之外的 confound 控制方法。

---

**MF2. Human validation per-type κ 差异掩盖测量可靠性问题 [R1-N2; R2 部分同意]**

- Overall κ = 0.738 掩盖 per-type 差异：lexical 0.904 vs. coreferential 0.479 vs. authorization scope 0.385。
- Per-type 仅 32–34 episodes，统计功效不足以支撑 per-type 可靠性声明。
- Coreferential κ = 0.479（仅 moderate agreement）使 Table 2 中该类型的因果效应估计可信度存疑。

**交叉分享结果**：R2 同意应报告 per-type κ，但认为影响有限——(1) 这是 violation detection κ 而非 taxonomy annotation κ（后者 0.95）；(2) coreferential 效应量本身最小（+18.7 pp），是保守估计。建议降级为 Should-Fix。

**Director 裁定**：维持 Must-Fix。对于声称建立因果效应的论文，outcome measurement reliability 是基本要求。R2 的 mitigating arguments 合理但不改变核心问题。

**建议修改方向**：(1) 将 per-type κ 和 CIs 移入正文（非仅附录）；(2) 对 coreferential（κ = 0.479）进行 misclassification sensitivity analysis（如假设 20% 随机误分类率下效应量变化）；(3) 增加 human validation 样本量至每 type ≥100 episodes，或明确限定 per-type 效应为 exploratory。

---

### Should-Fix（影响评分但不一票否决）

**SF1. TOST SESOI ±15 pp 阈值依赖 [R1-N1; R2 反驳降级]**

Table 3 灵敏度分析清楚显示阈值依赖：±10 pp → 0/15 等价对；±12 pp → 5/15；±15 pp → 8/15。Partial ordering 完全取决于阈值选择。

**交叉分享结果**：R1 认为 Must-Fix。R2 有力反驳：(1) partial ordering 不在 §1 contribution list 中，不是独立贡献；(2) Table 3 已透明展示 sensitivity；(3) 对 first causal study 要求 domain-calibrated SESOI 是循环论证。

**Director 裁定**：降级为 Should-Fix。R2 反驳有力。

**建议**：§5.2 明确标注 partial ordering 为 exploratory finding（非 confirmatory），承认 ±15 pp 阈值的任意性。

---

**SF2. SOPBench "cross-benchmark replication" 措辞过强 + 3× 效应量差异 [R1-W4 + R2-W1; 共识]**

+34.0 pp（synthetic matched-pair）vs. +12.7 pp（naturally occurring, constraint-level）差距 3 倍。两个 benchmark 设计差异过大（matched-pair vs. correlational; episode-level vs. constraint-level; controlled injection vs. naturally occurring），"replication" 暗示不存在的可比性。

两位 Reviewer 共识：应改为 "cross-benchmark directional consistency" 或 "convergent evidence"。需在 Discussion 中分析效应量衰减来源及哪个更接近 real-world expectation。

---

**SF3. 模型选择偏向 frontier tier [R2-W2; R1 同意]**

5 个主实验模型 + 2 个 replication 模型均为 frontier-class，无 7B–70B 级别测试。对 smaller/open-source 模型的泛化性未知。

**建议**：Limitations 中限定 model tier scope，或补充小模型实验。

---

**SF4. Convergent nocuity baseline calibration [R1-W3 + R2-W4; 共识]**

Poisson binomial 独立性基线假设模型间无共享 bias，但模型共享训练数据和 RLHF 目标。+8.3 pp excess 可能部分反映 training data overlap 而非真正的 convergent misinterpretation。Cross-family Jaccard (0.46) vs. within-family (0.54) 差距仅 15%，部分支持此担忧。

两位 Reviewer 共识：需用 unambiguous condition 下的 model convergence 作为 ambient baseline + permutation test。

---

**SF5. Pooled McNemar 跨模型聚合违反独立性 [R1-W2; R2 同意]**

300 pairs × 5 models = 1,497 pairs，同一 clause pair 跨 5 模型共享，违反 pair independence。

**缓解因素**：Per-model McNemar 均独立 p < 10⁻⁷，结论不依赖 pooled test。属 analytical hygiene 问题。

**建议**：改用 Mantel-Haenszel 合并 OR 或 GEE/mixed-effect logistic regression with clause-level random intercept。

---

### Minor（不影响接收）

**M1. Introduction 数字密度 [R2-N1; R1 反驳]**
Introduction 含 ~17 个独立数字量。R2 认为 Must-Fix（削弱叙事力），R1 认为实证论文常见做法。Director 裁定降级为 Minor。精简为 2-3 核心数字会改善可读性但不影响学术判断。

**M2. Healthcare pilot 设计差异 [R2-W3; R1 部分同意]**
不同 taxonomy、不同 clause 构造，难以作为严格复制。但 "pilot" 措辞已传达初步性质。

**M3. Temperature = 0 [R1-W5; R2 反驳]**
R2 有力反驳：(1) temperature=0 是 policy-governed agent 标准部署设置；(2) matched-pair design 部分 mitigate；(3) R1 引用"仅 GPT-4.1"为事实错误——Appendix AG 覆盖 3 个 model families（GPT-4.1, Claude Sonnet 4.6, DeepSeek-V3）。Director 采纳 R2 反驳。

**M4. Abstract "strictly disambiguating" 首次出现不够直观 [R1-M1; R2 同意]**

**M5. Figure 2 "clause wording" 22.4% variance 含义正文未充分解释 [R1-M2; R2 同意]**

**M6. Table 2 "Cluster" 列正文 under-explained [R1-M3; R2 同意]**

**M7. "nocuous" 非 NLP 标准术语，降低可搜索性 [R1-M4; R2 同意]**

---

## Questions for Authors

1. 如果将 SESOI 从 ±15 pp 降至 ±10 pp，type partial ordering 和 practical mitigation 建议如何变化？请直接在 rebuttal 中展示。
2. 对 coreferential（human-LLM κ = 0.479），假设 judge 有 20% 随机误分类率，效应量和显著性如何变化？
3. 使用 clause-level clustered McNemar 或 Mantel-Haenszel 合并 OR，效应量和 CI 变化幅度如何？
4. Unambiguous condition 下的 model convergence rate（ambient convergence level）是多少？
5. 排除 incompleteness 后 convergent nocuity rate 是否仍显著？（论文已报告 37.2%/93/250，但 Poisson binomial baseline 需重算）
6. τ²-bench +34.0pp、SOPBench +12.7pp、healthcare +58.8pp——作者认为哪个最接近 real-world expected effect？
7. §3 能否增加 1-2 段深入讨论 incompleteness 在 RE 文献中的 epistemological status（ambiguity vs. underspecification），以及为什么将其纳入本研究框架？

---

## Missing References

本轮两位 Reviewer 未提出新的 missing references。R32 轮次提出的 3 篇（arXiv 2603.01213, arXiv 2404.11972, Springer 2025）仍待验证和处理。

---

## External Review

**状态**：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-24 14:07–14:11）。1 critical + 3 warning + 8 info。

| 严重程度 | 位置 | 发现 |
|---------|------|------|
| **Critical** | p.28 | 末页仅 2 行文字（"Use of AI Assistants" 溢出 1 bullet 到 p28），~95% 空白，极不专业。应合并回 p27 或调整排版消除此页 |
| Warning | p.8 | Discussion + Limitations 连续 2 页纯文本无 display item，视觉单调。考虑引入总结性 figure 或将 appendix heatmap 提前 |
| Warning | p.7 | Figure 3（箱线图）尺寸偏小，与 Table 2 竞争视觉空间 |
| Warning | p.5 | 整页纯文本（§4.2–4.6），p4 Table 1 和 p6 Figure 2 之间节奏沉闷 |
| Info | p.2 | Figure 1 panel (a) 小字标签打印时可能偏小 |
| Info | p.2, p.17 | Figure 1 和 Figure 4 使用红-绿色彩组合，对色盲不友好。建议改用 Okabe-Ito 色板 |
| Info | p.6 | Figure 2 清晰可读，标注直观 |
| Info | p.7 | Table 2 booktabs 规范，脚注较密 |
| Info | p.9 | Limitations 简洁（~1/3 页），正文恰好 8 页，符合 EMNLP 页数限制 ✓ |
| Info | p.1 | Title/Author/Abstract 排版整洁，匿名格式正确 ✓ |
| Info | pp.12-27 | Appendix 16 页含 ~28 表 + 3 图，格式一致 ✓ |
| Info | pp.10-11 | References 正常，无未解析引用 ✓ |

---

## Overall Assessment

**综合评分：3.5 / 5 (Borderline Conference)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.5 | 3.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | **3.5** |

**接收建议**：Borderline Conference → Findings 偏上。论文的匹配对因果设计和扰动控制是领域标杆，convergent nocuity 是有实践价值的新颖发现。两个 Must-Fix 制约论文从 Findings 向主会议跨越：(1) incompleteness 的概念归属需更深入的理论辩护 + 更强的 confound 控制，(2) per-type human validation κ 差异需在正文透明呈现并辅以 sensitivity analysis。如果 rebuttal 有效回应这两个问题，评分可上调至 3.5–4.0 区间。

**Reviewer 共识度**：高。两位 Reviewer 独立给出相同分数（3.5），对核心优势（因果设计、convergent nocuity、appendix 质量）和主要问题（incompleteness、convergent nocuity baseline）的判断高度一致。分歧仅在个别问题的严重程度定级上，均已在交叉分享中充分讨论并由 Director 裁定。

---

## Detailed Comments

### 交叉分享中的关键分歧裁定

1. **R1-N1 (TOST SESOI) Must-Fix → Should-Fix**：采纳 R2 反驳——partial ordering 非核心贡献，sensitivity 已透明展示，domain anchoring 对 first causal study 存在循环论证风险。

2. **R2-N1 (Introduction 数字密度) Must-Fix → Minor**：采纳 R1 反驳——实证论文 Introduction 数字密集是常见做法。精简会改善可读性但不影响学术判断。

3. **R1-W5 (Temperature) Should-Fix → Minor**：采纳 R2 反驳——(a) R1 引用的"仅 GPT-4.1"为事实错误（Appendix AG 覆盖 3 个 model families）；(b) temperature=0 是 policy-governed agent 标准设置；(c) matched-pair 设计的对称性论证有力。

4. **R1-N2 (Human validation) 维持 Must-Fix**：R2 的 mitigating arguments 合理但不充分——κ = 0.479 对应 coreferential type 的因果效应声明需要 sensitivity analysis 支撑。

### 历史 Issue 跟踪

本轮 fresh review 中，3 个曾在 R32 标记为 resolved 的 issue 被独立重新发现：
- **R30-SF6** (incompleteness 概念张力)：R32 修复（§3 epistemological status 段）被认为深度不足
- **R30-SF5** (convergent nocuity baseline)：R32 修复（excess framing）未解决 ambient baseline 和 permutation test 需求
- **R30-SF3** (SESOI 锚定)：R32 修复（Appendix 交叉引用）不足以应对 partial ordering exploratory 标注需求

这表明这些问题的根源深于表面修复，需要在下一轮修订中进行更实质性的处理。