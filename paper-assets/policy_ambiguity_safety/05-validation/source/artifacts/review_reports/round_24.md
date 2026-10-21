---
round: 24
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T08:33:54.842648+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 24 审稿报告

**论文**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety"
**Venue**: EMNLP 2026 via ARR (Long Paper)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）
**审稿模式**: Fresh（重新审稿）
**轮次**: Round 1, 1 轮收敛（交叉回应后无未解决矛盾）

---

## Summary

本文在 τ²-bench 上通过 300 组 matched-pair 歧义/无歧义条款对（六类分类、五个模型、2,997 episodes），建立了 policy 歧义与 LLM agent 安全违规之间的因果关系（+34.0 pp，confound-free 范围 +18.7 至 +36.0 pp）。方差分解显示条款措辞解释 22.4% 的违规方差而类型仅 0.4%，但类型预测失败机制的能力远强于预测违规率（NMI = 0.23 vs 0.01）。Error analysis 发现 disambiguation neglect（4.6% awareness）和 systematic nocuity（77% permissive bias）。方法论严谨度在同类工作中突出，但外部效度存疑（SOPBench 效应压缩 63%）、novelty framing 偏强、taxonomy 层效应无统计支撑。

---

## Strengths

**S1. Matched-pair 因果设计严谨 [R1, R2 共识]**
300 clause pairs × 2 conditions × 5 models 的配对内比较有效隔离歧义操作的因果效应。两名标注者类型分配 κ = 0.95。Perturbation control（Δ = −0.67 pp, CI 含零）和 ICC = 0.919 复制验证完整。在该领域因果推断链条完整度罕见。

**S2. 统计框架全面且自律 [R1, R2 共识]**
McNemar's test、TOST 等价检验（跨 7 个 margin 的敏感性分析）、Type III SS 方差分解、Holm-Bonferroni 校正、Bootstrap clustering（B=10,000）。C3 未通过校正后被诚实标注为 inconclusive。统计自律值得肯定。

**S3. Error Analysis 揭示有价值的新现象 [R1, R2 共识]**
Disambiguation neglect（4.6%）、systematic nocuity（41.3% 多数模型收敛于同一错误、77% permissive bias）是有实质贡献的发现。Nocuity 方向反转（Berry & Kamsties 2004 的 divergent → 本文的 convergent）提供了 LLM-specific 的失败模式理解。

**S4. 复现与泛化验证充分 [R1, R2 共识]**
7 个模型（5 main + 2 replication）覆盖 6 providers、2 架构家族。三族交叉评判验证（Fleiss' κ = 0.717）。SOPBench 跨基准复制。方法论局限的坦诚披露（incompleteness confound、auth scope 低 κ、ICC 范围限制）在同类工作中少见。

**S5. Related Work 覆盖好 [R2]**
引用了所有主要并发工作（DRIP-R, PolicyBank, AgentPex, MANTRA），对心理语言学和 RE 文献的桥接恰当。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical, R2 提出 R1 AGREE] Novelty framing 不够诚实**
Contribution (1) "the first matched-pair causal study" 本质上是将心理语言学/RE 的标准方法迁移到 LLM agent policy 领域，非方法论创新。核心发现"ambiguity → more errors"方向上可预测，真正有价值的是效应量化和 type→mechanism 的诊断发现（NMI = 0.23 vs 0.01）。§3 已有 "experimental instrument rather than a proposed classification standard" 的自我限定，但 §1 contributions 和 Abstract 未贯穿此定位。
→ **建议**: 从 "first causal study" 转向 "first quantification of differential effect + diagnostic taxonomy" 作为核心卖点。

**N2 [critical, R2 提出 R1 AGREE] Taxonomy 两层结构（C3）无统计支撑但叙事未调整**
六类 taxonomy 是 Li et al. (2024) 11 类的子集选取，非原创分类体系。C3 层效应未通过 Holm-Bonferroni 校正（p=0.017 vs 阈值 0.0125），但 §3 和 §1 的叙事仍围绕 "two layers—linguistic and specification" 展开。§3 的理论预测（linguistic ambiguity 可部分通过 tool responses 解消）恰恰未得到验证。
→ **建议**: 将两层结构降格为描述性组织框架，§3 和 §1 同步更新叙事。

**N3 [critical, R1 提出 R2 AGREE 但认为接近 Should-Fix] 外部效度——合成→自然效应压缩 63%**
τ²-bench 主实验 +34.0 pp vs SOPBench +12.6 pp，且 SOPBench 上 2/5 模型不显著（GPT-5.4 p=0.052, DeepSeek p=0.163）。三因素归因（measurement grain、baseline compression、interaction depth）是 post-hoc 推测，各自贡献量无法分离。§5.1 "directional consistency across all models is the primary criterion" 将标准从效应量一致性降格为方向一致性，是 goalpost shifting。Limitations 已声明 "34.0 pp is an upper bound"，但 Abstract/Conclusion 仍以 34.0 pp 为主要数字。
→ **建议**: Discussion 增加生态效度正式段落；Abstract/Conclusion 呈现效应量范围（12.6-34.0 pp）。

**N4 [critical, R1 提出 R2 AGREE] Incompleteness 信息添加混淆控制不足**
Incompleteness 的实验操纵本质上不同于其他五类（信息删除/添加 vs 语义重写）。Token count 作为 proxy 控制混淆，logistic regression 正系数 β=+0.027 存在替代解释（over-constraint violation）。虽然 0.1 pp 的实际影响微小，但 framing 问题严重——Abstract 中 34.0 pp 包含 incompleteness 而 confound-free range（+18.7 至 +36.0 pp）排除了它，这个区别被压缩在一句话中。
→ **建议**: Abstract/Conclusion 优先报告 confound-free pooled Δ = +31.0 pp（95% CI [27.9, 34.1]），34.0 pp 标注为含 incompleteness 上界。

### Should-Fix（影响评分但非一票否决）

**W1 [warning, R2 提出 R1 强烈 AGREE] Authorization scope 构念效度系统性存疑**
多维度 outlier：最低 inter-judge κ = 0.385、cross-judge-group ρ = 0.09、驱动全部 C4（排除后 p=0.97）、最低 within-type ICC = 0.29、最大跨模型方差 52 pp。已有排除 auth scope 后 C4 消失和 cross-judge ρ = 0.90 的分析，但缺少排除后的 C1 pooled Δ、方差分解、NMI——仅需对现有数据重新计算。
→ **建议**: 补充排除 auth scope 后的 C1、方差分解、NMI 敏感性分析。

**W2 [warning, R1 提出 R2 REBUT 降级] 条款对构建过程不够透明**
Template-based pipeline 未描述模板数量、结构、筛选率。Post-hoc realism validation 一句带过。R2 认为应降为 Should-Fix（数据承诺发布、§4.2 已有关键信息、高 κ 是设计目标）。两位 Reviewer 共识：需补充但非 blocking。
→ **建议**: Appendix 补充模板设计细节和筛选率；扩展 clause pair 示例至每类型 2-3 个。

**W3 [warning, R1 提出 R2 AGREE] 失败模式编码缺乏人工验证**
614 条 trace 的 LLM 编码（Gwet's AC₁ = 0.62, κ = 0.52），循环性风险。LLM coder prompt 是否包含类型信息未说明。Limitations 中 "human validation underway for camera-ready" 不足以支撑当前 claim 强度。
→ **建议**: 明确 coder prompt 设计；至少 50-100 条 trace 的人工验证。

**W4 [warning, R1 提出 R2 AGREE] SESOI ±15 pp 的 justification 不够 principled**
">2× 噪声"和"不需不同缓解策略"两条理由非领域接地。Table 3 sensitivity analysis 已部分缓解，但 ±15 pp 的选择仍影响 §5.2 叙事结构。
→ **建议**: 明确标注 pragmatic default；正文更突出引用 Table 3 的 ±10/±12 pp 结果。

**W5 [warning, R1 提出 R2 AGREE] ICC 复制仅限 OpenAI 家族**
同家族模型可能共享训练数据导致 clause-level response pattern 相似，膨胀 ICC。C1 方向一致性不等同于 clause-level reproducibility。
→ **建议**: 讨论跨提供商 ICC 可能更低的含义。

**W6 [warning, R1 提出 R2 AGREE] Human validation per-type 样本量不足**
Per-type n ≈ 32-34，CI 极宽（coreferential: [0.00, 0.84]）。论文自身承认 imprecise 但仍引用 per-type κ 作论证。
→ **建议**: 引用 per-type κ 时附 CI；理想情况增加至 per-type ≥ 50。

**W7 [warning, R1 提出 R2 强烈 AGREE] Cross-domain type ranking ρ = 0.26 削弱 C2 泛化性**
Retail 和 airline 两个 customer-service 子域的类型排序几乎无关（p=0.62）。Cond. prec. 跨域差异 22.0 pp。Conclusion 中 "type-targeted diagnosis for policy-governed deployments" 的建议缺乏跨域根基。
→ **建议**: §7 讨论领域依赖性；Conclusion 限定适用范围。

**W8 [warning, R2 提出 R1 AGREE] NMI 比较的 cardinality 不对称**
Type→mechanism (6×5) vs type→violation (6×2)。Binary outcome 下 NMI 的 effective range 更受限，"order of magnitude"（16.8×）部分是 cardinality artifact。Cramér's V 比较（0.45 vs 0.137 = 3.3×）更公平但比值远小。
→ **建议**: 承认 NMI 受 cardinality 影响；以 Cramér's V 补充或替代 "order of magnitude" 表述。

**W9 [warning, R2 提出 R1 PARTIALLY AGREE] 方差分解叙事偏重已解释部分**
60.8% 残差被包装为 intervention ceiling 而非研究解释力限制。Appendix Z 的 ICC 分解已有进一步分析，但正文未充分反映。
→ **建议**: §5.1 或 §7 补充一句承认解释力限制。

### Minor（不影响接收）

**M1 [R1, R2]** Abstract 信息密度过高（8 个数字），建议精简至 3-4 个。
**M2 [R1, R2]** "Nocuous" 术语反转未在首次使用（Abstract）时标注。
**M3 [R1, R2]** Temperature=0 对泛化性的影响未在 Limitations 提及。
**M4 [R1, R2]** C3/C4 编号暗示四个同等级 claim，应明确标注层级。
**M5 [R1]** Table 2 脚注 ‡ 应标注 per-type 样本量（n≈17）。
**M6 [R1→R2 降级]** Prevalence audit（Appendix）κ = 0.295，Introduction 引用时标注低可靠性。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下核心问题上达成完全共识：

1. **外部效度是最大风险**：SOPBench 63% 效应压缩 + 2/5 模型不显著，合成条件下的 34.0 pp 不可直接推广
2. **Incompleteness confound 的 framing 不够突出**：confound-free range 应作为 headline
3. **Authorization scope 构念效度系统性存疑**：多维度 outlier，需补充排除后的敏感性分析
4. **C3 层效应失败但叙事未同步调整**：两层结构应降格为组织性框架
5. **失败模式编码缺人工验证**：camera-ready 承诺不够
6. **Novelty framing 偏强**：应从 "first causal study" 转向 type-specific diagnostic
7. **NMI cardinality asymmetry**：Cramér's V 比较更公平（3.3× vs 16.8×）
8. **Cross-domain type ranking 不支持跨域泛化**：ρ = 0.26

---

## Reviewer Divergence

两位 Reviewer 仅在严重程度上有分歧，无实质性矛盾：

| Issue | R1 | R2 | 共识 |
|-------|-----|-----|------|
| 条款对构建透明度（N3/W2） | Must-Fix | Should-Fix | **Should-Fix**（R2 理由充分：数据将发布、§4.2 已有关键信息） |
| Prevalence audit 可靠性（W6/M6） | Should-Fix | Minor | **Minor**（不影响核心分析） |
| Figure 1 信息量（M4） | 合理 | 可优化 | **不列入**（审美判断，非方法论问题） |
| 3 episodes API error（M3） | Minor | 无需关注 | **不列入**（0.1% 不构成 systematic missingness） |

---

## Questions（需作者澄清）

**Q1 [R1, R2 共识]** SOPBench 效应缩小到 1/3 对论文实际启示（practical implications）的影响？如果真实世界效应接近 12.6 pp 而非 34.0 pp，"nocuous" framing 和 "clause-level auditing" 建议的力度如何调整？

**Q2 [R2 提出 R1 AGREE]** 排除 authorization scope 后，C1 pooled Δ、方差分解、NMI 的具体数字？（现有数据即可计算）

**Q3 [R1, R2 共识]** LLM failure mode coder 的 prompt 是否包含歧义类型标签？如果包含，NMI = 0.23 可能被 prompt 污染。如果不包含，请说明 prompt 设计。

**Q4 [R1]** 22.4% clause-level variance 的分布形态——少数高效应条款驱动的右偏分布 vs 连续分布？LOO 最大 shift 1.4 pp 暗示无单一极端值，但 within-type CV 0.69-1.03 暗示高异质性。

**Q5 [R2]** 77% permissive bias 是否是 customer-service domain artifact（agent 被训练为"帮助客户"）？跨域 permissive 比例分别是多少？

**Q6 [R2]** Disambiguation neglect 的模型差异（GPT-4.1/Claude 10-11% vs Qwen3/DeepSeek 0%）反映 safety training 差异还是歧义处理能力差异？§6.2 "default behavior, not inability" 的 claim 能否被当前数据区分？

**Q7 [R1]** Concordant-violation 和 concordant-no-violation 的比例分别是多少？（580/1497 discordant pairs 意味着 917 concordant pairs）

---

## Missing References

**两位 Reviewer 共同推荐：**
- Kadavath et al. 2022, "Language Models (Mostly) Know What They Know" — 与 disambiguation neglect 直接相关

**R2 推荐（R1 未独立验证）：**
- AgentSpec (Wang et al., ICSE 2026) — agent runtime specification enforcement
- Agent Behavioral Contracts (arXiv 2602.22302, 2026) — formal specification + runtime enforcement
- "Check Yourself Before You Wreck Yourself" (arXiv 2510.16492, 2025) — selective quitting for agent safety

**R1 推荐（R2 部分 REBUT）：**
- Kadavath et al. 2022 [R2 AGREE]
- Lu et al. 2022, prompt order sensitivity [R2 REBUT: matched-pair 已控制位置]
- Constitutional AI / RLHF literature [R2 REBUT: 过于宽泛]

---

## External Review

**状态**: 未请求（项目配置未启用外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 已完成（3 warnings, 0 critical, 9 info）

**Warnings:**
1. **Pages 4-6 视觉疲劳**: 连续三页纯文本（§4 Method → §5.2 Results），无 figure/table/equation 穿插。建议在 page 5-6 插入结果摘要表或 forest plot 打破文本墙。
2. **Page 8 Figure 3 尺寸偏小**: Model×Type 热力图挤在右栏约 1/4 栏高，单元格数值和轴标签在正常阅读距离下难以辨认。建议改用 figure*（全宽）或增大纵向空间。
3. **Figure 2/3 Float 位置偏离引用**: 两个 figure 出现在 page 8（Discussion/Conclusion 区域），但首次引用在 page 5-6 的 Results。审稿人需回翻 2-3 页。

**Info:**
- 主体正文 5 个 display items（对 8 页实证论文偏低，建议 6-8 个）
- Figure 1 位置合理（page 2 顶部）、Table 2 排版干净、Appendix 表格丰富
- 正文精确卡在 8 页限制内，Limitations 在 page 9

---

## Overall Assessment

**Overall: 3.5 (Borderline Conference)**

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 4/5 | **3.75** — matched-pair 设计和统计框架严谨，但 incompleteness confound 控制不足、auth scope 构念效度存疑、failure mode 编码缺人工验证 |
| Excitement | 3.5/5 | 3/5 | **3.25** — 核心发现方向可预测；type-specific diagnostic 和 systematic nocuity 有价值但 taxonomy 非原创；"first causal study" framing overstates novelty |
| Reproducibility | 3/5 | 4/5 | **3.5** — 数据/代码承诺发布，但 template pipeline 描述不足、ICC 仅 OpenAI family |
| Confidence | 4/5 | 4/5 | **4/5** |

**一句话总结**: 方法论严谨的因果实验（matched-pair + 全面统计框架 + 7 模型），核心方法论框架是扎实的。但四个问题限制了评分：(1) novelty framing 偏强（"first causal study" 是领域迁移而非创新），(2) 外部效度存疑（SOPBench 效应压缩 63%），(3) taxonomy 层效应无统计支撑但叙事未调整，(4) incompleteness confound 和 auth scope 构念效度的联合影响。

**升分路径**: 如果作者 (a) 按 N1/N2 调整 framing（弱化 "first causal"、降格两层结构），(b) 按 N3 在 Discussion 正式讨论生态效度并调整 headline 数字，(c) 按 N4 调整 incompleteness framing——论文可升至 **4.0 Conference**。当前状态适合 **strong Findings**。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高（8 个数字），建议精简至 34.0 pp（或 confound-free 31.0 pp）、22.4% clause variance、NMI ratio
- "Nocuous" 首次出现时加 "(i.e., harmful)" 已有，但 nocuity inversion（convergent vs divergent）未标注
- Confound-free range 在句末容易被忽略，建议调整为 headline

### §1 Introduction
- Contribution (1) 的 "first" claim 需 reframe
- Prevalence audit 引用（55-87%）应标注低可靠性（κ = 0.295）
- Figure 1 位置合理但信息密度可优化

### §3 Taxonomy
- 两层结构的叙事需降格为组织性框架
- "We test this empirically" 的预测未通过 → 应在 §5.2 的 C3 结果后增加 cross-reference

### §4 Method
- §4.2 template pipeline 需补充细节（模板数量、筛选率）
- §4.3 temperature=0 的局限性应在 Limitations 补充
- §4.4 human validation per-type 引用时附 CI
- §4.6 SESOI ±15 pp 明确标注 pragmatic default

### §5 Results
- §5.1 C1: 34.0 pp 应标注为含 incompleteness 的上界；confound-free pooled Δ = 31.0 pp 应更突出
- §5.1 variance decomposition: 补充 60.8% 残差作为解释力限制的一句话
- §5.2 C2: cross-domain ρ = 0.26 的讨论应更显著
- §5.2 NMI: "order of magnitude" 需补充 Cramér's V 作为 cardinality-robust 替代
- C3/C4 的 claim 层级应在 §5 开头更明确标注

### §6 Analysis
- §6 failure mode: claim 强度应降低至与 κ = 0.52 匹配
- §6.2 disambiguation neglect: safety training vs ambiguity processing 的混淆应讨论
- §6.3 systematic nocuity: permissive bias 可能是 domain artifact，应在 Discussion 讨论

### §7 Discussion
- 增加生态效度正式段落（34.0 pp → 12.6 pp SOPBench）
- C2 领域依赖性的讨论
- 77% permissive bias 的跨域稳定性讨论

### Limitations
- 补充 temperature=0 的局限性
- 加强 ICC 范围限制的讨论

### Appendix
- 扩展 clause pair examples（每类型 2-3 个）
- Table 2 脚注标注 per-type 样本量

### 格式
- ✅ 正文 8 页，Limitations page 9（不计入页限）
- ✅ Double-blind 匿名格式正确
- ✅ ACL 模板使用正确
- ✅ References natbib 风格
- ⚠️ Data availability 中匿名 GitHub URL 需确保提交时未泄露身份