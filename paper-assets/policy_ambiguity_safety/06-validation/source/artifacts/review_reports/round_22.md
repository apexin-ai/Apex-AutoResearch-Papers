---
round: 22
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T04:46:12.568922+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 22 (Fresh Review)
## Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety
**Venue**: EMNLP 2026 (ARR May cycle) | **审稿日期**: 2026-05-23

---

## Summary

本文提出首个针对策略歧义对 LLM agent 安全影响的 matched-pair 因果研究。在 τ²-bench 上构建 300 对歧义/无歧义策略条款，跨五个前沿模型（GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3）和 2,997 episodes 评估六类歧义的影响。核心发现：歧义条款使违规率增加 34.0 pp（排除 confounded incompleteness 后 +18.7 至 +36.0 pp）；条款措辞解释 22.4% 方差而类型仅 0.4%；类型预测失败机制比预测违规率强一个数量级（NMI = 0.23 vs 0.01）。

---

## Strengths

**S1. 严格的 matched-pair 因果设计。** 最小编辑条款对构建（§4.2, κ=0.95 标注一致性）配合 perturbation control（n=300, Δ=−0.67pp）建立了真正的因果推断，超越前人工作的相关性证据。Cross-judge 设计消除同模型自评偏差，matched-pair 结构使系统性 judge 偏差在处理效应（Δpp）中自动消除。[R1-S1, R2-S1]

**S2. 多层次验证体系。** Type III SS 方差分解、排列检验（p<0.001）、ICC 复制（0.919）、七级 TOST 敏感性（Appendix A）、bootstrap 聚类（B=10,000）、三家族 cross-judge 验证（Fleiss' κ=0.717）、Holm-Bonferroni 校正——验证密度在同类工作中罕见。[R1-S5, R2-S2]

**S3. 可操作的方差分解。** 条款措辞 22.4% >> 类型 0.4% 直接指导实践：条款级审计比类型级分类更有效。这比单纯报告"歧义有害"更进一步，具有工程可落地性。[R1-S2, R2-S3]

**S4. Taxonomy 重构为诊断工具。** 类型预测失败机制（NMI=0.23, Cramér's V=0.45）比预测违规率（NMI=0.014）强一个数量级，将分类法从风险预测器重构为诊断工具——概念上的重要区分。三种失败机制（structural misparse, information gap-filling, boundary violation）与类型的映射提供了超越风险量化的诊断视角。[R1-S4, R2-S5]

**S5. 跨模型、跨基准复制。** 5+2 个模型（含 Gemini 2.5 Flash, LLaMA 4 Scout）+ SOPBench 跨基准复制，效应方向在所有 7 个模型上一致。[R2-S4]

**S6. 对局限性的坦诚处理。** Authorization scope 低 κ=0.385、cross-judge ρ=0.09、incompleteness confound、severity threshold 未预注册——透明度增强论文可信度。Taxonomy 主动定位为 experimental instrument。[R1-S3, R2-S6]

**S7. 缓解实验闭环。** Type-specific prompt 实验（Appendix B）展示类型依赖的缓解效果（auth scope −18.0pp vs incompleteness −3.3pp n.s.），从诊断到干预形成闭环。[R1-S6, R2-S7]

---

## Weaknesses

### Should-Fix（共识问题）

**W1 [Should-Fix, Critical]. C4 model×type 交互可能是测量伪影。** C4 交互完全由 authorization scope 驱动（排除后 p=0.97, Appendix M）。该类型同时具有四个测量不稳定指标：最低 inter-judge κ（0.385）、最高 cross-judge 方差（41.6%–65.6%）、within-replication ICC≈0、跨 judge 组排名不一致的唯一驱动因素。虽已标注"[Exploratory]"，但 §5.3 的呈现规格（独立小节+专门图表）仍暗示实质性发现。建议：模拟 κ=0.385 噪声下交互检验假阳性率，或在正文明确降级 C4。[R1-W2, R2 全部同意]

**W2 [Should-Fix]. SOPBench 复制效应压缩 63% 缺乏原则性归因。** τ²-bench +34.0pp → SOPBench +12.6pp，三个 post-hoc 解释（测量粒度、负向任务、结构差异）未量化各因素贡献。对于安全相关发现，3× 效应量差异值得更系统的归因。建议：在 τ²-bench 上以 constraint-level 重新分析，或原则性论证方向一致性的充分性。[R1-W1, R2 同意]

**W3 [Should-Fix]. ICC 复制仅覆盖 OpenAI 家族。** ICC=0.919 和残差分解 ICC(1)=0.749 均在 OpenAI 内计算，但用于刻画所有五个模型的 60.8% 残差。跨 provider 随机性可能更高（不同 temperature=0 实现、MoE vs dense 架构差异）。建议：至少一个非 OpenAI 模型的小规模 ICC 复制，或明确标注适用范围。[R1-W3, R2 同意]

**W4 [Should-Fix]. SESOI ±15pp 缺乏领域接地。** 两个论证标准（2× 测量噪声、缓解策略阈值）分别是精度论证和无经验支撑的判断。七级敏感性分析部分缓解。但 R2 补充 nuance：agent safety 新兴领域无先例标准，pilot study 阶段可接受。建议：明确承认 SESOI 是统计驱动的；讨论未来领域锚点。[R1-W4, R2 同意 with nuance]

**W5 [Should-Fix]. Token count 作为 incompleteness confound 代理过于粗糙。** Token count 无法捕获语义信息密度。论文整体策略保守（已排除 incompleteness 报告 confound-free range），但基于 incompleteness 的二级结论（最高系统性 nocuity 率 OR=2.61; 对 prompt 缓解最有抵抗力 −3.3pp n.s.）仍受 confound 影响。建议：对这些二级结论添加更强 caveat。[R1-W5, R2 部分同意]

**W6 [Should-Fix]. 残差方差干预天花板讨论不充分。** Discussion §7 已提及 clause-level auditing 为"the largest actionable component"，但未明确量化干预上限的实际含义：即使完美消除歧义，仍有 60.8% 违规变异来自其他因素。建议：增加 2-3 句框架化干预天花板。[R2-W2, R1 同意]

### Minor（共识问题）

**W7 [Minor]. 生态效度缺口未量化。** 34.0pp 标注为"上界"但未量化与真实策略文档歧义的预期差距。SOPBench +12.6pp 可作粗略下界参考但未在论文中建立此连接。[R1-W6, R2 同意]

**W8 [Minor]. 层级结构（C3）未通过 Holm-Bonferroni 校正。** p=0.017 vs threshold 0.0125，已注释为"organizational convenience"，但读者可能误解两层结构为经验发现。[R1-W7, R2 同意]

**W9 [Minor]. 人工 failure-mode 编码验证缺失。** 100 traces 人工验证在进行中但当前版本未完成。Failure mechanism 分析（§6）是重要贡献之一，LLM 编码 LLM 失败的循环性风险需 camera-ready 前解决。[R1-W8, R2 同意]

**W10 [Minor]. Table 2/Figure 2 应标注 incompleteness confound。** Table 2 展示原始 +49.2pp 但 confound 讨论在 §5.1 末段和 Appendix F，相隔较远。加脚注即可。[R2-W7, R1 同意]

**W11 [Minor]. Conclusion 偏短。** 约 5 句，建议扩展 1-2 句涵盖干预天花板含义和分析逻辑链。[R2-W6, R1 同意]

### 不构成 Weakness 的 R2 关切（R1 成功反驳）

- **Cross-judge ρ=0.09 已在正文 §5.2 明确报告**（R2 误称"藏在 Appendix"，R1 引用原文反驳）
- **Abstract 信息密度**：因果研究报告效应量及边界条件为学术惯例，R1 反驳合理
- **Taxonomy instrument 定位**：在 C3 未过校正、跨域 ρ=0.26 等限制下，instrument 定位是诚实且策略性正确的
- **Limitations §9 Measurement 段已覆盖 cross-judge 测量问题的根因**

---

## Reviewer Consensus

两位 Reviewer 在以下关键判断上达成共识 [AGREE]：

1. **Soundness 4.0/5**：方法论严谨，主要 claims 有充分支撑
2. **Overall 3.5 (Borderline Conference)**：方法论贡献实在但外部有效性不足
3. **C4 交互分析不可靠**（W1）：最强共识点，R2 称 R1 的分析"最精准"
4. **SOPBench 压缩需归因**（W2）
5. **ICC 跨 provider 验证不足**（W3）
6. **SESOI 统计驱动非领域驱动**（W4）
7. **Incompleteness 二级结论需 caveat**（W5）
8. **干预天花板需显式化**（W6）
9. 所有 5 个 Minor 问题均达成共识

## Reviewer Divergence

| 维度 | R1 | R2 | 分歧根源 |
|------|----|----|----------|
| Excitement | 3.5/5 | 3.0/5 | R1 认为 matched-pair 因果设计在 agent safety 领域的首次应用构成显著方法论推进；R2 强调各组件增量性（taxonomy 是 Li et al. 子集重组，DN 是 ambiguity collapse 重命名）|

R1 的 4 个 REBUT（R2-W1, W3, W4, W8）均有事实依据或合理论证，不构成未解决分歧。

---

## Questions for Authors

**Q1.** 能否将 SOPBench 效应压缩分解为测量粒度 vs 领域差异 vs 结构差异？例如在 τ²-bench 上以 constraint-level 重新分析。[R1-Q1, R2 同意]

**Q2.** 在模拟 κ=0.385（auth scope）vs κ=0.65+（其他类型）测量噪声下，C4 交互检验的期望假阳性率是多少？[R1-Q2, R2 同意]

**Q3.** Auth scope ICC≈0 下 Figure 3 中 52pp 跨模型范围如何解释？建议在 Figure 3 中为 auth scope 添加低可靠性标注。[R1-Q3, R2 补充]

**Q4.** 是否考虑过语义复杂度指标（如独立操作约束计数、BERTScore）替代 token count 控制 incompleteness confound？[R1-Q4, R2 补充]

**Q5.** 跨域类型排名不一致（ρ=0.26）是否意味着 taxonomy 的诊断价值仅限于 type→mechanism 映射，实践者是否需要领域特定校准？[R1-Q5, R2 同意]

**Q6.** 多条款歧义交互效应（如同一策略中同时存在 auth scope + incompleteness）是否考虑？[R2-Q5]

**Q7.** 4.6% disambiguation awareness 各模型间差异如何？Claude（RLHF 对齐更强）是否显著高于 DeepSeek/Qwen3？[R2-Q3]

**Q8.** Type-specific vs generic disambiguation prompt 的效果量对比是否可提供？这对部署指导更直接。[R2-Q4, R1 补充]

---

## Missing References

无关键遗漏。Related work 覆盖充分（agent safety, NLP ambiguity, RE literature, psycholinguistics）。

**可选补充**：
- Byrt et al. (1993) κ 流行度悖论 —— 与 Appendix G coreferential κ=0.479 讨论直接相关 [R1 建议]
- Kinniment et al. (2024) agent 自主性评估框架 [R2 可选]

---

## External Review

**外部审稿（Stanford Agentic Reviewer）**：未配置，本轮未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 10 info, 0 critical）。主要发现：

**Warnings:**
1. **Pages 4-6**：连续三页纯文本（Method §4 至 Results §5.2 开头），无 figure/table 穿插，建议用流程图或提前放置 Table 2 打破文字墙
2. **Page 7**：Table 2 + Figure 2 + Figure 3 三个 display items 集中在同一页，与前三页纯文本形成强烈反差，建议将部分前移至 page 5-6 均衡视觉节奏
3. **Pages 8-9**：Error Analysis/Discussion/Conclusion/Limitations 连续两页无 display item

**Info 亮点：**
- 正文共 4 个 display items / 8 页 = 0.5/页，对实证论文偏少（通常 5-8 个）
- Figure 1 全宽实验概览图清晰但图内文字偏小
- 未发现 margin 溢出、LaTeX 渲染错误、未解析引用 [?] 或排版问题
- 格式合规：ACL template ✓, double-blind ✓, booktabs ✓, Limitations in main text ✓

---

## Overall Assessment

### 维度评分

| 维度 | 评分 | 说明 |
|------|------|------|
| Soundness | 4.0/5 | Matched-pair 设计和 perturbation control 建立严格因果推断。主要不足：auth scope 测量不可靠影响 C4；ICC 仅 OpenAI；SESOI 缺领域接地 |
| Excitement | 3.0–3.5/5 | R1: 3.5（方法论首次应用有价值），R2: 3.0（各组件增量性）。圆桌判定：**3.25**，偏向 R1——matched-pair 因果设计在 agent safety 领域确实是方法论推进，但受限于两个客服领域和合成刺激 |
| Reproducibility | 4.0/5 | 实验细节充分，代码数据承诺发布。扣分：依赖闭源 API，ICC 未跨 provider 验证 |

### Overall: **3.5 — Borderline Conference**

**Confidence**: 4/5（两位 Reviewer 独立得出相同结论，交叉验证增强可信度）

### 总评

方法论严谨的因果研究。Matched-pair 设计 + perturbation control 在 agent safety 领域首次建立了从策略歧义到安全违规的因果链，方差分解（clause 22.4% >> type 0.4%）提供了可操作洞见，failure mechanism 映射赋予 taxonomy 诊断价值。执行质量高于平均 submission，附录验证体系全面。

主要不足：(1) C4 model×type 交互的唯一驱动类型（auth scope）测量不可靠，该发现可能是伪影；(2) SOPBench 跨基准复制效应压缩 63%，缺乏原则性归因；(3) 外部有效性受限（两个客服领域、合成刺激、仅前沿模型）；(4) 60.8% 残差方差限制了 clause-level auditing 的实际干预天花板。

论文 Soundness 足以被 Findings 接收。是否进入 main conference 取决于 AC 对以下问题的判断：matched-pair 因果设计的首次应用 + 22.4%/0.4% 方差分解的可操作性是否达到 Conference 的 novelty bar。

---

## Detailed Comments

### §1 Introduction
- Opening retail example 有效且具体，narrative flow 从 example → gap → method → results 连贯
- Contribution (2) 中"order of magnitude"表述准确（NMI 16.8×，Appendix S）
- Contribution 列表清晰，三项贡献层次分明

### §2 Related Work
- 覆盖全面：agent safety, ambiguity in NLP/RE, psycholinguistics, policy specification
- ASPI tension（clarification-seeking → prompt injection）和 Ambig-SWE（interactive disambiguation）均已讨论
- DRIP-R 的三点区分（因果性、安全违规、两层 taxonomy）清晰

### §3 Taxonomy
- 六类互斥性在实验目的下可接受
- 三项 design criteria（attestation + minimal-pair + mutual exclusivity）为筛选提供了操作标准
- 排除 ellipsis 和 pragmatic implicature 的理由充分
- §3 末段"Scope of ambiguity"透明地讨论了 taxonomy 的包容性定义

### §4 Method
- Matched-pair 设计优雅，96% 初始标注一致率（κ=0.95）充分
- Cross-judge 设计消除自评偏差
- Perturbation control（n=300）有效排除表面文本变化
- SESOI 论证需加强（见 W4）

### §5 Results
- C1 效应量强大（+34.0pp, OR=15.1）且统计显著（p<10^-105）
- C2 partial ordering 框架合理：robust extremes + margin-dependent mid-tier
- §5.2 关于 ρ=0.09 的 "important qualification" 透明且恰当
- C4 需降级或补充测量噪声分析（见 W1）

### §6 Analysis
- 三种失败机制分类有诊断价值
- Disambiguation neglect 量化（4.6%）有价值，术语定位诚实
- Systematic nocuity（41.3% 收敛违规）是有趣发现
- Failure mode coding 需人工验证（见 W9）

### §7 Discussion
- Differential nocuity 假设框架恰当
- Taxonomy 作为诊断工具（NMI 0.23 vs 0.01）的论证有力
- 干预天花板需更明确讨论（见 W6）

### §8 Conclusion
- 核心数字准确，confound-free range 限定恰当
- 偏短，可扩展（见 W11）

### §9 Limitations
- 覆盖生态效度、范围、测量、confound、disambiguation channel——全面
- Camera-ready human validation 承诺恰当

### Appendix
- 24 个 appendix 提供了全面的验证体系
- Cross-judge 验证（Appendix W, Fleiss' κ=0.717）是重要补充
- SOPBench 复制（Appendix V）需更系统的归因分析

### 格式合规
- 正文 ≤ 8 页 ✓ | Double-blind ✓ | ACL template (review mode) ✓
- Limitations in main text ✓ | Booktabs ✓ | References format consistent ✓
- 图表标题自解释 ✓ | 无排版错误 ✓