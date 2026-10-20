---
round: 12
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-20T17:33:14.398195+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 12 (Fresh Review)

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 via ARR May 2026 | Deadline: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计 | R2: 新颖性+完整性+写作质量）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需第 2 轮）

---

## Summary

OntoCoDec 将 IE 本体约束编译为双层 token-level 解码约束：语法层（XGrammar）保证 JSON 结构合法性和词汇成员关系；语义层通过运行时 entity registry + dynamic masking 强制 domain/range 类型兼容性。论文提出可判定性分类（context-free / prefix-decidable with state / non-local）指导约束分层设计，引入 constraint tightness κ̄ 描述 schema 限制性。在 SciERC（551 docs）、DocRED（998 docs）、WikiEvents（246 docs）三个数据集上使用 Qwen3-8B、Llama-3.1-8B、Mistral-7B（及 Llama-3.1-70B 简要评估）进行了系统的消融实验和 LoRA 微调组合性验证。

---

## Strengths

**S1. 新颖的形式化视角。** 将 formal language theory 的可判定性分析引入 IE 约束解码，提出 context-free / prefix-decidable with state / non-local 的三层分类，为系统设计提供了有原则的指导。Proposition 1（Level 2 ⊄ Level 1）为双层架构的必要性提供了形式化论证基础。[R1+R2 共识]

**S2. 全面且系统的实验设计。** 五路消融清晰隔离了 grammar 层和 semantic 层的贡献；跨模型（3+1 个）、跨数据集（3 个）、跨任务（RE + EE）的覆盖在 systems paper 中高于平均水平。四类违规分类法（DR/CF/RV/ET）允许精确理解每层约束的贡献和代价，远超同领域多数论文的二元 valid/invalid 评估。[R1+R2 共识]

**S3. Fine-tuning composability 论证有价值。** Table 2 展示 LoRA + S1 在四个 model-dataset 组合上均实现 DR ≤ 0.09%、R-F1 ± 0.6pp。这回答了一个重要的部署问题——约束系统是否与参数优化兼容。Beam search (k=4) 进一步消除 SciERC 上全部四类违规。[R1+R2 共识]

**S4. 诚实的局限性讨论。** Limitations section 明确承认 CF trade-off、模型规模限制、WikiEvents 样本量、评估仅限 LoRA 等问题。在投稿论文中这种坦诚度值得肯定。[R1+R2 共识]

**S5. 实际工程价值。** 框架自动从任意 IE schema 编译约束，无需约束特定训练，可与任意自回归 LM 配合。Runtime overhead +10%（LoRA 配置），constraint compilation < 0.5s，scalability 到 200 entity types / 1000 relations 仅 2-3% overhead。即插即用的部署价值明确。[R1+R2 共识]

**S6. 丰富的附录。** 22 页附录包含详尽的错误分析、scalability benchmarks、prompt 敏感性、document length 分析、TCR 机制、case studies。显著增强可复现性和可信度。[R1+R2 共识]

---

## Weaknesses

### Must-Fix（4 项，影响接收决定）

**MF1. "Exact enforcement" 声称与 36.64% CF fallback rate 存在根本矛盾。** [R1-N2 raised, R2 AGREE — full consensus]

§3.3 多处声称 "exact pair-based enforcement"，但 §4 的 grammar-first fallback 意味着当 S(t)∩G(t)=∅ 时语义约束被完全丢弃。Appendix C Table 8 显示 SciERC 上 fallback 在 36.64% 的 type-bearing positions 被触发，GENERIC 类型占 CF violations 的 63.3%（155/245）。更严重的是：fallback 导致的错误类型赋值会写入 entity registry，影响后续所有涉及该实体的 relation 的 domain/range 检查——论文未分析此级联失败效应。

→ 修改建议：将 "exact" 改为 "best-effort" 或 "targeted"；分析并量化 fallback 级联行为；在 Abstract/§1 中披露 fallback rate。

**MF2. κ̄ 作为 Contribution 2 ("analytical linking framework") 被过度声称。** [R2-N2 raised, R1 fully AGREE — full consensus]

κ̄ 本质上是描述性统计量（|σ(r)|/|E|² 的归一化比例）。论文自身在 Appendix C 承认 "descriptive characterization rather than a confirmatory statistical test"（df=2, p>0.05），但 Abstract 和 Contribution 2 仍定位为 "analytical linking framework"，与论文自身的谨慎表述不一致。

→ 修改建议：Contribution 2 降级为 "a descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes and provides deployment guidance"。

**MF3. Proposition 1 仅为 proof sketch，与 "formally compiles" 定位不匹配。** [R1-N1 raised, R2 partially AGREE]

论文将 "decidability-guided constraint classification" 定位为核心贡献之一，但 Proposition 1 仅给出 proof sketch。R2 指出 R1 原始批评中混淆了 non-context-freeness 与 undecidability（Proposition 1 声称的是 Level 2 ⊄ Level 1，应用 pumping lemma 而非不可判定性归约），但 R2 同意 proof sketch 对于声称 "formal" 的贡献偏弱。核心论证（PDA stack 无法追踪无界 entity-type binding）方向正确但需完整化。

→ 修改建议：(A) 附录补充完整 pumping lemma 证明（~半页）；或 (B) 将 contribution 从 "formal classification" 降级为 "classification motivated by formal language-theoretic observations"。

**MF4. WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力不足。** [R1-N3 raised, R2 partially AGREE]

WikiEvents fine-tuning 使用 194/20/20 split，测试集仅 20 篇文档。R2 正确指出：零样本评估（246 docs）有效，问题限于 fine-tuning 行。但 Table 5 将两种设定并列呈现，未标注样本量差异，可能误导读者。正文 §5.4 的结论语气未相应降低。

→ 修改建议：Table 5 内标注 n=246/n=20；fine-tuning 行报告 95% bootstrap CI；正文明确 fine-tuning 评估为 preliminary。

### Should-Fix（8 项，影响评分但不一票否决）

**SF1. 语义层核心机制与 IterGen/PICARD 的概念区分不充分。** [R2-N1 raised as Must-Fix, R1 AGREE substance but suggests Should-Fix — severity divergence]

IterGen (Ugare et al., 2025) 同样在 grammar 层之上叠加语义约束（corrective backtracking）；PICARD (Scholak et al., 2021) 维护 incremental parsing monitor。论文在 §6 中未深入对比 preventive masking vs. corrective backtracking 的机制差异、效率特性和约束表达能力。R1 认为 masking vs. backtracking 是公认不同设计范式，novelty confusion 风险有限，建议降级。

→ 修改建议：§6 增加显式机制对比（2-3 行 + 可选对比表），阐述 OntoCoDec 的 forward-only masking 效率优势及其约束表达力限制。

**SF2. 无直接实验对比最接近的 IE 基线 BoostCD。** [R1-W1 + R2-W1, full consensus]

BoostCD (Sakota et al., 2025) 同样在 SciERC/DocRED 上做 IE constrained decoding，是最直接的竞争方法。缺乏 head-to-head 数字对比使审稿人难以判断边际贡献。

→ 修改建议：至少引用 BoostCD 报告的 SciERC 数字并讨论方法论差异；如代码可用，运行对比实验。

**SF3. 模型规模声称过宽。** [R1-W2 + R2-W5, full consensus]

Abstract "applies to any autoregressive LM across four models (8B–70B)" 实际上主要测试 7-8B 模型，70B (Llama-3.1-70B AWQ INT4) 仅在 §5.6 有简要零样本评估（无 fine-tuning composability）。注：两位 Reviewer 在交叉阶段均未注意到 70B 结果的存在（出现在 §5.6 "Cross-scale generalizability" 段，而非主要 cross-model table），说明该结果的呈现位置不够突出。

→ 修改建议：Abstract/§1 限定为 "validated primarily on 7-8B models with preliminary 70B results"；将 70B 结果在正文中更突出地呈现。

**SF4. CF 代价在 Abstract/Contribution 中不够透明。** [R2-W6 raised, R1 AGREE]

Grammar-first fallback rate 36.64%（SciERC ZS）和 CF 上升（0.08→9.90%）仅出现在正文细节和 Appendix C，Abstract 轻描淡写 "grammar-first fallback when constraints conflict"。

→ 修改建议：Abstract 增加 CF trade-off 说明。

**SF5. Abstract 信息密度过高。** [R2-W4, R1 AGREE]

Abstract 试图在一段中覆盖可判定性分类、三层架构、κ̄、跨模型数字、beam search、fine-tuning composability。核心 message（为什么 grammar 层不够、语义层如何补足）被数字细节遮蔽。

→ 修改建议：保留 1-2 个关键数字，其余推至 Introduction。

**SF6. Entity registry 顺序依赖导致全局次优类型赋值。** [R1-W4, R2 AGREE]

贪心策略在第一次出现时锁定 entity 类型，后续更紧约束的 relation 无法修正。TCR (Appendix D) 是事后修复，不是生成时的 exact enforcement——进一步削弱 MF1 的 "exact" 声称。

→ 修改建议：§3.3 或 §4 讨论贪心赋值局限性，定位为 Level 3 non-local 约束的实例。

**SF7. "Ontology-agnostic" 声称实验支撑不足。** [R2-W2, R1 partially AGREE]

仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 的 schema 来自训练数据经验统计。R1 指出编译机制确实不依赖来源，但 "ontology" 一词不准确。

→ 修改建议：改为 "applicable to both formal ontologies and empirically-derived type constraints"。

**SF8. DocRED beam search 仅 50 文档子集（零样本设定）。** [R1-W5, R2 AGREE]

SciERC beam 用完整 551 docs，DocRED 零样本 beam 仅 50 docs。注：LoRA beam 已扩展到 998 docs（d064 实验），但零样本 beam 仍受限。

→ 修改建议：标注子集规模限制并讨论代表性。

### Minor（8 项）

- **M1**: BibTeX 清理——10 orphan entries + 1 duplicate key (schall2025hiddencost) [R1+R2]
- **M2**: S1/S2 命名与层级编号初读易混淆，建议改为 SP/TP 或 JOINT/SEQ [R2-M3, R1 AGREE]
- **M3**: Table 5 "—" 标记缺少表注说明 [R2-M4, R1 AGREE]
- **M4**: §4 Eq.(2) conjunction 应明确为 element-wise AND over vocabulary [R1]
- **M5**: CF 列含义在 Table 1 首次出现时解释不足 [R1, R2 AGREE]
- **M6**: Figure 1 (Appendix C) x 轴 "κ·RV_baseline" 物理含义不直观 [R1, R2 AGREE]
- **M7**: §6 末尾一段从 related work positioning 滑向 contribution recapping [R1, R2 AGREE]
- **M8**: Schema RL (Lu et al., ACL 2025) 存在于 bib 但未被引用，应在 §6 中讨论 [R1+R2]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识：

1. [AGREE] **"Exact enforcement" 需要术语校准** — 36.64% fallback rate 使 "exact" 不成立，需改为 "best-effort" + 级联分析 (MF1)
2. [AGREE] **κ̄ overclaim** — "analytical framework" 应降级为 "descriptive metric" (MF2)
3. [AGREE] **BoostCD 对比缺失** — 最直接的 IE constrained decoding 竞争方法未实验对比 (SF2)
4. [AGREE] **模型规模声称过宽** — "any autoregressive LM" 需加限定 (SF3)
5. [AGREE] **CF 代价透明度不足** — Abstract/Contributions 未充分披露 (SF4)
6. [AGREE] **Abstract 信息密度过高** — 核心 message 被数字淹没 (SF5)
7. [AGREE] **Entity registry 顺序依赖** — 贪心策略全局次优 + TCR 非生成时保证 (SF6)
8. [AGREE] **实验覆盖和呈现质量高** — 四类违规分类法、三数据集四模型、诚实的 Limitations

---

## Reviewer Divergence

1. **IterGen 区分的严重性** — R2 定为 Must-Fix（新颖性是接收关键维度），R1 降级为 Should-Fix（preventive vs. corrective 是公认不同设计范式）。Review Director 判定：降级为 Should-Fix (SF1)，因机制差异在领域内已有共识，但论文确实需要更显式地论述。

2. **Related Work 压缩度** — R2 认为正文 §6 过于压缩（15 行），R1 反驳空间分配合理。Review Director 判定：8 页限制内，RW 放附录是常见做法，但 IterGen 机制对比应从附录移入正文。不单独列为 issue。

3. **零样本 violation rate 分析的实际意义** — R1 认为 R-F1 2-8% 时分析价值有限，R2 反驳 diagnostic 价值独立于 task performance。Review Director 判定：论文 "diagnostic" 定位恰当，但建议在表格中增加视觉分隔以区分 ZS 和 FT 结果。不单独列为 issue。

4. **Proposition 1 证明方法** — R1 要求不可判定性归约，R2 指出这是概念混淆（应用 pumping lemma 而非不可判定性归约），但同意 proof sketch 需加强。Review Director 采纳 R2 的修正，保留 MF3。

---

## Questions for Authors

1. **Fallback 级联量化**：当 grammar-first fallback 触发后，错误类型赋值写入 entity registry。能否量化这种级联效应——即因 fallback 导致的错误 registry 状态触发了多少后续 fallback？(R1-Q2)

2. **Bounded entity set 退化**：如果 schema 对 entity 数量设上限 k（实际场景常见），有效输出集变为有限语言（正则 ⊂ CF）。Proposition 1 的 "unbounded" 前提在实际场景中多大程度上成立？(R1-Q1)

3. **DR 消除的 F1 影响**：Fine-tuning 后 DR 大幅下降（1-2%→0%）但 R-F1 仅变化 ±0.5pp。被消除的 violations 是否主要出现在已经错误的 triple 中（即 precision 端的 false positives）？(R2-Q3)

4. **IterGen 对比**：OntoCoDec 的 domain/range 约束表达力受限于 prefix-decidable 性质。是否考虑过将框架扩展到更一般的语义约束（如 cardinality、temporal ordering）？主要技术障碍是什么？(R2-Q1)

5. **S2 为何 DR 高于 S1**：Table 1 显示 S2 (two-pass) 的 DR 反而高于 Full S1——是否因第一阶段 entity extraction 的错误传播到第二阶段？(R1-Q3)

---

## Missing References

1. **BoostCD** (Sakota et al., 2025) — 已引用但未实验对比，最直接的 IE constrained decoding 竞争方法 [R1+R2 共识]
2. **Schema RL** (Lu et al., ACL 2025) — 存在于 bib 但未在正文引用，应在 §6 training-based vs. decoding-time 对比中讨论 [R1+R2]
3. **Koldehoff et al.** (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE [R2]
4. **GCD** (Geng et al., 2023) — 已引用，Grammar-only 配置隐式对标，但应在实验部分明确展示 GCD baseline 数字 [R1]

---

## External Review (Stanford Agentic Reviewer)

**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：已完成（2 critical, 4 warning, 10 info）

### Critical

1. **主文前 4 页无任何 display item**：审稿人打开论文后连续翻过 4 页纯文本+公式才在第 5 页见到首个 Table。对于提出框架的系统论文，缺少架构概览图/流程图是严重的第一印象缺陷。
2. **主文（8 页正文）零 Figure**：全文仅有的 3 个 Figure 全部在附录（p20/23/25）。系统/方法论文审稿人期望至少在 Method 部分看到一张框架图展示双层架构、约束编译流程或解码时 masking 工作方式。

### Warning

3. 连续 4 页纯文本+数学公式无视觉打断，阅读负担极重
4. 主文 display items 全部为表格（Table 1-5），无可视化图表
5. §6 Related Work + §7 Discussion 挤在同一页，Related Work 仅约半栏
6. 附录 Extended Related Work 连续 3 页纯文本

### Info（选摘）

- Table 1 作为首个 display item 传达组件贡献而非方法核心，不如 overview figure 有锚定力
- 表格使用 booktabs 风格，精度统一，格式整体专业
- 主文 8 页，符合 EMNLP 2026 的 8 页正文限制
- Figure 3 (beam width) 图内文字偏小，150dpi 下勉强可读

**Review Director 评价**：主文零 Figure 是本轮最大的呈现缺陷。框架论文不提供架构图，审稿人需要完全靠文字和公式理解双层架构——这对第一印象和可理解性损害很大。强烈建议在 §3 Method 中增加一张框架概览图。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

**EMNLP 2026 评分参考**：3.5 = Borderline Conference（可能被主会议接收，但需要修改）

### 评分理由

**达到 Conference 水平的因素**：
- 可判定性引导的约束分层是新颖且有工程价值的视角
- 实验设计系统全面（3 数据集 × 4 模型 × 多配置），消融清晰
- Fine-tuning composability 论证回答了重要的部署问题
- Limitations 和 Appendix 的坦诚度和详尽度高于平均水平

**阻碍 Conference 接收的因素**：
- **Claim 校准问题**（MF1+MF2）：核心技术声称（"exact enforcement"）和贡献声称（κ̄ "analytical framework"）与论文自身呈现的证据不一致。这不是技术错误——方法本身工作正常——而是叙事过度包装
- **形式化不完整**（MF3）：论文以 "formally compiles" 定位，但核心定理仅有 proof sketch
- **关键 baseline 缺失**（SF2）：未与最直接的竞争方法 BoostCD 进行实验对比
- **视觉呈现缺陷**：主文零 Figure，框架论文无架构图

### 路径分析

**→ Conference (4.0)**：修复 MF1-MF4 的 claim 校准和形式化问题 + 补 BoostCD 对比 + 增加框架图。核心技术和实验质量足以支撑 Conference，当前的障碍主要是 presentation 和 claim 精度，而非 fundamental technical weakness。

**→ Findings (3.0)**：如果 claim 校准问题未充分解决，论文仍是 solid Findings——实验贡献（四类违规分类法 + 系统消融 + composability 验证）本身有值得发表的价值。

### Reviewer 评分

| Reviewer | Overall | Soundness | Excitement | Reproducibility | Confidence |
|----------|---------|-----------|------------|-----------------|------------|
| R1 (方法+实验) | 3.5 | 3.5/5 | 3.5/5 | 4/5 | 4/5 |
| R2 (新颖性+写作) | 3.5 | 4/5 | 3/5 | 4/5 | 4/5 |
| **Director 综合** | **3.5** | **3.75** | **3.25** | **4** | **4** |

### 核心判断

论文解决了一个真实问题（LLM-based IE 的类型违规），技术执行扎实，实验覆盖面广。主要瓶颈不在方法本身，而在 **claim 校准**——"exact enforcement" 在 1/3 决策点上不成立、κ̄ 被包装为超出其统计证据的分析框架、形式化贡献的证明力度不匹配。如果作者能精确校准声称力度（将方法的实际能力边界诚实呈现，而非通过术语包装暗示更强的保证），论文可以在一轮 revision 内达到 Conference 水平。

---

## Detailed Comments

### §1 Introduction
- Contribution 2 "An analytical framework linking constraint tightness to enforcement outcomes" → 改为 "A descriptive metric, constraint tightness κ̄, that correlates with enforcement outcomes"
- "formally compiles" → 根据 MF3 的选择调整（补证明则保留，否则弱化）

### §3 Method
- §3.1 Proposition 1：补充完整 pumping lemma 证明（附录），或降级 contribution 声称
- §3.3 "exact pair-based enforcement" → "best-effort pair-based enforcement"
- §3.3 entity registry：讨论贪心赋值的局限性和 Level 3 non-local 约束
- **增加框架概览图**（双层架构 + 约束编译流程 + 解码时 masking 工作方式）

### §4 Constraint Composition
- Eq.(2) 明确为 element-wise AND over vocabulary
- 增加 fallback 级联分析段落
- κ̄ 措辞从 "analytical framework" 降级

### §5 Experiments
- Table 1/3 中 ZS 和 FT 结果增加视觉分隔
- Table 5 (WikiEvents) 标注 n=246/n=20 + FT 行报告 CI
- DocRED beam search 50-doc 子集标注覆盖的 relation type 比例
- CF 列在首次出现时增加解释

### §6 Related Work
- 增加 IterGen/OntoCoDec/PICARD 机制对比（preventive vs corrective vs incremental）
- 引用 Schema RL (Lu et al., 2025) 和 Koldehoff et al. (2025)
- 讨论 BoostCD 方法论差异
- 末尾段调整为 positioning 而非 contribution recap

### §7 Discussion and Conclusion
- 加 "across 7-8B parameter models" 限定词
- "ontology-agnostic" → "applicable to both formal ontologies and empirically-derived type constraints"

### Abstract
- 降低数字密度，聚焦 conceptual framing
- 增加 CF trade-off 说明
- κ̄ 措辞调整
- "formally compiles" 根据 MF3 调整

### BibTeX
- 清理 10 orphan entries + 1 duplicate key