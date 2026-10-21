---
round: 25
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T09:54:48.235390+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 25 审稿报告 — 圆桌合成

**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on LLM Agent Safety
**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle)
**审稿模式**: Fresh（重新审稿）
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**轮次**: 1 轮（交叉后关键问题达成共识，无需第 2 轮）

---

## Summary

本文研究 policy ambiguity 对 LLM agent 安全的因果影响。通过在 τ²-bench 上构造 300 对匹配 clause pairs（涵盖 6 类歧义），评估 5 个模型（2,997 episodes），发现歧义使违规率增加 31.0pp（confound-free types）/ 34.0pp（全部 6 types）。论文发现 type 仅解释 0.4% 的违规方差但预测 failure mechanism 的能力更强（Cramér's V=0.45 vs 0.14），将 taxonomy 定位为诊断工具。此外报告了 disambiguation neglect（4.6% awareness）和 systematic nocuity（41.3% 收敛违规，77% permissive bias）两个实证现象。

---

## Strengths

**S1** [共识] **因果设计的稀缺性和严谨性**。Matched-pair 设计在 LLM agent safety 领域罕见。Perturbation control（Δ_perturb=-0.67pp, CI 含零）有效排除表面文本扰动的替代解释。每对 clause 仅改变歧义、保持 policy intent 不变，因果推断设计合理。

**S2** [共识] **Claim 校准得当**。论文系统性地使用 confound-free range（≥27.3pp）、upper bound 标记（incompleteness）、TOST sensitivity（7 margins）、bootstrap clustering，避免 over-claiming。C3（layer effect）inconclusive 被坦诚报告。SESOI 标为 "pragmatic default, not principled"。这种方法论诚实度在同类论文中不常见。

**S3** [共识] **多层次复制增强可信度**。5 主模型 + 2 复制模型（7 models, 6 providers, 2 架构风格）；cross-judge 3-family validation（Fleiss' κ=0.717）；SOPBench 跨 benchmark 复制（方向一致）；ICC replication（0.919 within OpenAI family）。

**S4** [共识] **Type→mechanism 的发现**。Cramér's V=0.45（type→mechanism）vs 0.14（type→rate）是一个有价值的理论贡献——说明 taxonomy 的价值在于 failure diagnosis 而非 rate prediction，为 targeted mitigation 提供 actionable framework。

**S5** [共识] **控制实验的密度和透明度**。TOST 7-margin sensitivity、bootstrap clustering、incompleteness confound regression、cross-judge validation、severity threshold comparison、per-clause LOO analysis——robustness check 覆盖范围远超同类论文。

**S6** [R1] **Disambiguation neglect 发现**。4.6% awareness rate + model-level 分化（GPT-4.1/Claude 10-11% vs Qwen3/DeepSeek 0%，p=2.2×10⁻⁹）有实践指导意义。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [共识: R1-N1 Must-Fix + R2-W2 Should-Fix→交叉后 AGREE 升级] **合成效应 34pp vs SOPBench 12.6pp（2.7×）缺乏桥接分析**

Abstract 和 Conclusion 以 34.0pp/31.0pp 为 headline，SOPBench 自然语境复制仅 +12.6pp（其中 2/5 模型未达显著）。Discussion §7 仅一句 "overestimates naturalistic effect sizes"，未分析差距来源。Appendix Z 列出三个结构性差异但正文未引用。从业者无法判断实际部署中应参考哪个数字。

→ 修改建议：(1) Abstract/Conclusion 同时报告合成上界和自然下界；(2) Discussion 用 2-3 句分析差距来源（measurement grain, baseline compression, interaction depth）；(3) 明确论文核心贡献在于因果机制识别而非精确效应量估算。

**MF2** [共识: R1-N2 Must-Fix + R2 交叉后 AGREE] **跨领域 ρ=0.26 (p=0.62) 与 Abstract "type-targeted diagnostics" 泛化性 framing 矛盾**

Type ranking 在 retail vs airline 之间零相关（ρ=0.26）。Abstract 写 "enabling type-targeted diagnosis for policy-governed deployments" 无领域限定词。Conclusion 已有限定（"within customer-service domains"），但 Abstract 和 Introduction 的 contributions 列表未反映这一关键限制。需区分 binary effect 的跨领域稳健性（p=0.187）vs type ordering 的领域依赖性。

→ 修改建议：Abstract 加 domain-specificity 限定词；Introduction contributions 列表限定 taxonomy 适用范围。修改代价低。

### Should-Fix（影响评分但不一票否决）

**SF1** [分歧→妥协: R1-N3 Must-Fix, R2 REBUT→Should-Fix] **Authorization scope 构念效度问题需 consolidated 讨论**

Auth scope 在六类中系统性异常：κ=0.385（低于 fair agreement 标准）、52pp 模型间变异（Claude 12% vs GPT-5.4 64%）、单独驱动 cross-judge ranking discordance（排除后 ρ 从 0.09→0.90）、驱动 C4 interaction（排除后 p=0.97）。论文在多处碎片化报告了这些问题（§5.2 + Appendix G + AA），但缺少 main text 中的 consolidated paragraph。R2 指出：透明度已充分、permission boundary 固有主观性是该类别在真实场景中危险的原因、post-hoc 排除有 researcher degrees of freedom 风险。

→ 修改建议：§5.2 或 §7 增加一个 consolidated paragraph，集中讨论 auth scope 的构念效度挑战及为何保留。

**SF2** [分歧→妥协: R2-N1 Must-Fix, R1 REBUT→Should-Fix] **Taxonomy 增量贡献论证——缺 Li et al. 11→6 映射表格**

§3 提供了三条设计标准和排除举例（"ellipsis and pragmatic implicature were excluded"），论证逻辑完整。但读者无法快速查看完整的 11→6 映射关系。R1 指出用 Appendix AC 的 audit 数据论证覆盖度会引入循环论证。

→ 修改建议：§3 或 Appendix 增加映射表格（提升可读性，非论证缺陷）。

**SF3** [分歧→妥协: R2-N2 Must-Fix, R1 REBUT→Should-Fix] **"Ambiguity" 广义使用与 NLP 社区标准定义的张力**

将 incompleteness、normative conflict、vagueness 纳入 "ambiguity"。§3 "Scope of 'ambiguity'" 段有操作定义（Wasow et al. 2005）和 RE 文献支撑（Dalpiaz et al. 2018），但未明确讨论与 NLP 传统分类（ambiguity vs vagueness vs incompleteness）的关系。R1 指出改用 "specification defects" 会脱离 NLP/CL 对话。

→ 修改建议：§3 增加 1-2 句讨论与 NLP 传统分类的关系。

**SF4** [共识] **"Nocuous" 术语从 divergent→convergent 的概念延伸**

Berry & Kamsties (2004) 定义 nocuous = stakeholder divergence。本文 §6.3 发现 convergent error（models 收敛到同一错误解释）。Abstract 有 "inverting...divergent to convergent" 但不够明确。§6.3 的解释出现在第 8 页太晚。

→ 修改建议：§1 首次使用 "nocuous" 时简要说明概念延伸。

**SF5** [共识] **C3 inconclusive vs two-layer 组织框架**

C3 未通过 Holm-Bonferroni（p=0.017, threshold 0.0125），但 taxonomy 仍按 linguistic/specification 两层展示。§3 已改为 "design hypothesis" 但仍隐含经验支撑。

→ 修改建议：§3 显式声明 two-layer 是基于 RE 文献的组织框架，C3 检验结果为 inconclusive。

**SF6** [共识] **ICC "Reproducibility" 标题误导**

ICC=0.919 仅在 OpenAI family 内计算。§4.5 标题 "Reproducibility" 暗示跨 provider 可复现性。论文补充的 "C1 consistency across all seven models" 仅说明方向一致，不等于 effect size 定量可复制。

→ 修改建议：标题改为 "Within-family reproducibility" 或加限定词。

**SF7** [共识] **60.8% 残差方差中 ~46% 系统性部分未讨论来源**

Discussion 仅说 "likely reflects clause×context interactions"，未进一步列举候选来源。

→ 修改建议：Discussion 增加 2-3 句讨论可能来源（conversation trajectory, user persona, tool-use sequence）。

**SF8** [共识] **Failure mode 分析表述过强**

LLM-coded κ=0.52 vs human κ=0.15 表明 LLM 间"一致性"可能反映共享偏差。§6 标注 "[Exploratory]" 但叙事仍用 "mechanistically distinct" 等强断言。论文自己承认 2/6 type-mechanism 映射有 definitional affinity。

→ 修改建议：§6 表述降级为 "categorically distinct in LLM coding"。

**SF9** [共识] **Incompleteness confound: token count 是粗糙代理**

Appendix F 承认 "finer-grained semantic measures may reveal different confound structures"，但 main text 未提及 token count 作为 information content 代理的局限性。

→ 修改建议：§5.1 增加一句承认局限。

**SF10** [共识] **Temperature=0 限制生态效度**

所有实验 temperature=0。Limitations 仅一句 "stochastic sampling remains untested"，未讨论方向性预期。

→ 修改建议：增加 1-2 句讨论 temperature>0 的可能影响方向。

### Minor（不影响接收）

**m1** [共识] 正文数字密度过高（Table 2 信息过载、§5.1 单段含 10+ 统计数字）——建议将 per-model rates 和 TOST tiers 移至 appendix。

**m2** [R2] Disambiguation neglect 的增量贡献可更明确——增量在于因果框架下量化和 model-level 分化，非 "LLM 不问问题" 的泛泛观察。

**m3** [R2] arXiv preprint 引用格式不统一。

**m4** [R1] Abstract 中 Cramér's V=0.45 vs 0.14 缺乏即时上下文——读者不知道分别对应什么。

**m5** [R1] ρ=0.09 two-group ranking discordance 在 §5.2 中位置不够显著——直接影响 C2 可信度。

---

## Reviewer Consensus

以下问题被两位 Reviewer 独立标记并在交叉后确认共识：

1. **合成 vs 自然效应量差距**（MF1）：34pp→12.6pp 需在正文充分讨论，Abstract 需同时报告两个数字
2. **跨领域 taxonomy 泛化性限定**（MF2）：Abstract 需加 domain-specificity 限定词
3. **"Nocuous" 术语延伸**（SF4）：divergent→convergent 的概念转换需更早、更明确论证
4. **数字密度过高**（m1）：正文统计细节影响可读性
5. **因果设计是核心方法论贡献**（S1）：两位 Reviewer 一致认可
6. **Claim 校准得当**（S2）：方法论诚实度突出

## Reviewer Divergence

| 问题 | R1 判定 | R2 判定 | 合成判定 | 理由 |
|------|---------|---------|----------|------|
| Auth scope 构念效度 | Must-Fix (N3) | Should-Fix | **Should-Fix (SF1)** | 透明度已充分、构念主观性合理、post-hoc 排除有偏见风险；但需 consolidated paragraph |
| Taxonomy 增量论证 | Should-Fix | Must-Fix (N1) | **Should-Fix (SF2)** | 论证逻辑完整（3 criteria + 排除举例），缺的是呈现形式 |
| "Ambiguity" 术语 | Should-Fix | Must-Fix (N2) | **Should-Fix (SF3)** | 操作定义有文献支撑，改术语会脱离 NLP/CL 对话；但需加强讨论 |
| Disambiguation neglect 新颖性 | Minor | Should-Fix (W4) | **Minor (m2)** | 增量在于因果框架+model-level 分化，文献中未有此量化 |

---

## Questions for Authors

1. 合成效应 (34pp) 和 SOPBench 效应 (12.6pp) 之间 2.7× 差距，主要来源是什么？measurement granularity（constraint-level vs episode-level）是否足以解释全部差距？
2. Authorization scope 的 κ=0.385 是否暗示需要更精细的操作定义？排除 auth scope 后 C2/C4 结论是否有实质性变化？（Appendix AA 部分回答，但 C2 ranking 变化未报告）
3. 60.8% 残差方差中 ~46% 系统性部分，是否有初步证据指向主要来源？
4. Temperature=0 下 permissive attractor (77%) 在 temperature>0 时是否可能改变？sampling randomness 是否会打破 convergent violation pattern？
5. Failure mechanism 分类（structural misparse, gap-filling, boundary violation）是 post-hoc 编码的——type→mechanism 关联是否存在 circular reasoning 风险？LLM-coded κ=0.52 vs human κ=0.15 的差距如何解释？
6. DRIP-R 的 "no single correct resolution" 范式 vs 本文 matched-pair ground truth 范式——发现可否推广到真正的开放式歧义场景？

---

## Missing References

**已引用但讨论不足**:
- DRIP-R (Borakoty et al., 2026)：正文仅在 §2 Related Work 中对比，Appendix L 做 category mapping。作为最直接的同期竞争工作，应在 §2 中用 2-3 句更充分对比方法论差异（matched-pair causal vs annotation-based, safety violations vs decision quality）。

**可能遗漏**:
- Gao-Arch et al. (2026) "Ambiguity collapse in LLMs"：与 systematic nocuity（convergent error）高度相关，值得在 §6.3 或 §7 对比讨论（论文已引用 gur_arieh_ambiguity_collapse_2026，需确认是否为同一工作）
- Femmer et al. (2017)：RE 领域自动歧义检测综述，与 Appendix D detection experiment 相关
- Anthropic Model Spec / Constitutional AI 系列：与 policy-governed agent behavior 的 alignment 方向直接相关

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

状态：**已完成**（耗时 ~3 分钟）。0 critical, 1 warning, 13 info。

主要发现：
- **[warning]** Page 4-5 连续两页纯文本（Method §4.1-4.6），无 display item 穿插。建议用 models summary table 或 experimental design diagram 打破纯文本节奏。
- **[info]** 首页无 display item（纯 Title + Abstract），审稿人翻到 page 2 才看到 Figure 1。不影响接收但错失首页锚定。
- **[info]** Figure 1（Experimental Overview）锚定效果好，清晰传达端到端流程。
- **[info]** Figure 3 热力图使用黄-红渐变色阶，非最佳色盲友好方案，但单元格内数值标注有效缓解。
- **[info]** 正文 §1-§8 在 8 页内，Limitations 在 p9，格式合规。
- **[info]** Appendix 表格字号偏小但可接受。

视觉审查不影响评分或接收建议。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

**Soundness**: 3.75/5（R1: 3.5, R2: 4.0）
**Excitement**: 3.25/5（R1: 3.5, R2: 3.0）
**Confidence**: 4/5（两位 Reviewer 一致）

**判定理由**：

论文回答了一个重要且及时的研究问题——policy ambiguity 是否以及如何因果地影响 LLM agent 安全。Matched-pair 因果设计在该领域罕见（S1），claim 校准得当（S2），控制实验覆盖全面（S5），type→mechanism 的诊断发现有理论价值（S4）。

但两个 Must-Fix 问题构成接收障碍：(1) 合成效应（34pp）与自然效应（12.6pp）之间 2.7× 的差距未在正文充分讨论，Abstract/Conclusion 仅报告合成数字，对从业者有误导风险（MF1）；(2) 跨领域 type ranking 零相关（ρ=0.26）与 Abstract "type-targeted diagnostics" 的泛化性 framing 矛盾（MF2）。

10 个 Should-Fix 问题（auth scope 构念效度、taxonomy 增量论证、ambiguity 术语、nocuous 概念延伸、C3/two-layer 框架、ICC 标题、残差方差讨论、failure mode 表述、incompleteness confound 局限、temperature=0）中，大部分为低成本修改（1-3 句话或术语调整），但数量累积仍反映论文在 framing 精度上的系统性不足。

**修改后提升空间**：若 MF1 和 MF2 得到充分回应（Abstract 同时报告两个数字 + 加领域限定词 + Discussion 扩展 ecological validity），论文可达 4.0（Conference）。当前状态更适合 3.0-3.5（Findings 到 Borderline Conference）。

**与 EMNLP ARR 评分标准的对应**：
- 3.5 = Borderline Conference（可被主会议接收的边界线）
- 论文有清晰的因果贡献和严谨的实验设计，但 ecological validity gap 和 framing 精度问题使其在 Conference 边界线上

---

## Detailed Comments

### §1 Introduction
- Contributions 列表：C2 应限定 "within customer-service domains"
- 首次使用 "nocuous" 时加简要说明概念延伸（从 divergent→convergent）
- "enabling type-targeted diagnosis for policy-governed deployments" 加领域限定

### §3 Taxonomy
- 增加 Li et al. 11→6 映射表格（§3 或 Appendix）
- "Scope of 'ambiguity'" 段增加 1-2 句讨论与 NLP 传统分类的关系
- 开头显式声明 two-layer 是组织框架（organizational framework），C3 检验结果 inconclusive

### §4 Method
- §4.5 "Reproducibility" 标题改为 "Within-family reproducibility"
- §4.5 incompleteness 讨论处增加一句承认 token count 是粗糙代理

### §5 Results
- §5.1 Abstract/Conclusion 同时报告合成上界（31.0pp confound-free）和自然下界（12.6pp SOPBench）
- §5.2 或 §7 增加 auth scope 构念效度 consolidated paragraph

### §6 Error Analysis
- 开头加 caveat 段落强调 exploratory + LLM-coded 局限
- "mechanistically distinct" 降级为 "categorically distinct in LLM coding"

### §7 Discussion
- Ecological validity 段扩展为 2-3 句，分析 2.7× 差距来源
- 增加 2-3 句讨论 ~46% 系统性残差的候选来源
- 增加 1-2 句讨论 temperature>0 的可能影响方向

### §8 Conclusion
- 同步 Abstract 修改（同时报告两个 effect size）
- "type-targeted diagnostics" 加领域限定

### Abstract
- 同时报告合成上界和自然下界
- Cramér's V=0.45 vs 0.14 加简要上下文说明
- 加领域限定词

### References
- arXiv preprint 格式统一
- 补充 DRIP-R 方法论差异对比（§2 Related Work）