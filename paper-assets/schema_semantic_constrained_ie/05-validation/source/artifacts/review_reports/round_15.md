---
round: 15
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T01:38:47.012942+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**Round 15 | Fresh Review | EMNLP 2026 ARR May Cycle**
**Reviewers**: R1（方法严谨性+实验充分性）、R2（新颖性+完整性+格式合规）
**审稿模式**: 圆桌会议，1 轮独立审稿 + 1 轮交叉分享，共识充分达成

---

## Summary

本文提出 OntoCoDec，一个将 IE ontology 翻译为两层可组合 token-level 解码约束的框架：grammar layer（context-free，基于 XGrammar）保证 JSON 结构有效性和词汇表成员资格；semantic layer（prefix-decidable with state）通过动态实体注册表在运行时强制 domain/range 类型约束。论文以 decidability 分析为指导，证明 domain/range 约束不可被 context-free grammar 表达（Proposition 1，pumping lemma），建立了两层架构的理论必要性。在 SciERC、DocRED、WikiEvents 上验证，覆盖 4 个模型（7-70B）和 3 个 tokenizer family，LoRA + greedy S1 配置下 DR ≤ 0.09%、R-F1 变化不显著（±0.6 pp）。

---

## Strengths

1. **Decidability taxonomy 是真正的理论贡献** [R1 + R2 共识]：将 IE 类型约束分为三层（context-free / prefix-decidable with state / non-local）在该领域属首次。Proposition 1 的 pumping lemma 证明（Appendix O）严谨且有启发性，建立了为何单纯 CFG 不足以处理 domain/range 约束的理论 lower bound。

2. **Ablation 设计全面且有力** [R1 + R2 共识]：Table 1 的 5-way ablation + Table 10 的 4-way fine-tuned ablation 精确隔离了各层贡献。关键发现——semantic layer 单独仅减少 24% DR，但与 grammar layer 组合后达到 94-100%——为两层架构的必要性提供了直接经验证据。

3. **Fine-tuning composability 有实际部署价值** [R1 + R2 共识]：Table 2 的 paired bootstrap 检验（B=1000, document-level）证明 LoRA + S1 约束不显著降低 R-F1（p>0.05, 最大|Δ|=0.31 pp），同时 DR 显著下降（p<0.001）。这是实际部署的关键属性，prior work（GCD, BoostCD）均未系统验证此交互。

4. **附录极其详尽（24 页，A-O）** [R1 + R2 共识]：case studies（Appendix J）、per-relation error analysis（Appendix D/N）、scalability benchmarks（Appendix K）、beam search 完整分析（Appendix F）、prompt templates（Appendix A）、pumping lemma 完整证明（Appendix O）——reproducibility 极高。

5. **诚实的 Limitations 讨论** [R2]：CF trade-off、WikiEvents 初步性、API-only 模型不适用、tokenizer 依赖性等均有坦诚讨论。

6. **统计实践规范** [R1]：paired bootstrap、CI 宽度透明、cross-seed validation（Table 20）、p 值报告到位。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, R1-N1, R2 AGREE] **完全缺失与同类 constrained decoding 方法的实验对比**
论文在 Related Work（§6, Appendix B）详细讨论了 GCD (Geng et al., 2023)、BoostCD (Sakota et al., 2025)、CRANE (Banerjee et al., 2025)、IterGen (Ugare et al., 2025)、EnriCo (Zaratiana et al., 2024)，但实验中唯一对比是 unconstrained decoding 和 post-hoc filtering。GCD 同样使用 grammar-constrained decoding 处理 SciERC，BoostCD 同样在 IE 任务上做约束解码。论文声称 grammar-only ablation（Table 1 第 2 行）"represents the ceiling of grammar-constrained decoding (Geng et al., 2023)"，但这一隐含对比未显式化，且 BoostCD 的混合策略完全不同。**对于一篇 constrained decoding framework 论文，不与同类方法 head-to-head 对比是致命短板——reviewer 无法量化边际贡献。** 此问题已连续 4 轮（R12-R15）被标记。

**MF2** [critical, R1-N2, R2 AGREE] **"Guarantee" 措辞系统性高于实际保证水平**
Abstract ("formal guarantees at each layer")、§1 ("formal guarantees") 与 §3.3 ("best-effort pair-based enforcement")、§4 grammar-first fallback 存在系统性矛盾。三层保证缺口：(a) grammar-first fallback 在 S(t)∩G(t)=∅ 时跳过 semantic layer，恰恰在模型最可能产生 type-incompatible 输出时放弃约束；(b) Level 3 constraints（cross-triple consistency）显式未被强制；(c) Full S1 仍有残余 CF 0.08-12.02%。Limitations 部分诚实讨论了这些缺口，但 Abstract/Introduction 的 "guarantee" 表述未做对应限定，构成 claim-evidence 不一致。

**MF3** [major, R2-N1, R1 agree 降级] **正文溢出至第 9 页，违反 EMNLP 2026 严格 8 页限制**
Section 7 "Discussion and Conclusion" 约 8 行文字溢出到第 9 页。此问题在 R13 曾修复、R14 确认合规，R15 回归。ARR 规定 "strict 8-page limit for main text"。R2 列为 critical（desk reject 风险），R1 降级为 minor-major（8 行溢出非 desk reject 标准）。**Director 判定：major——必须修复，但非 desk-reject 级别。** 压缩 §7 或 §6 即可解决。

### Should-Fix（影响评分但不一票否决）

**SF1** [major, R2-N2, R1 partially REBUT] **核心新颖性定位不清：系统集成 vs 算法创新**
R2 指出 grammar layer 是 XGrammar 直接应用、semantic layer 是运行时类型检查的直接实现，论文缺少对 "what is genuinely new beyond combining XGrammar with a type-checking registry" 的回应。R1 部分反驳：Proposition 1 具有独立理论价值（非仅 motivation），enabling dependency formalization 排除了替代架构，fine-tuning composability 验证是 prior work 未做的实质性贡献。**Director 判定：论文 novelty 主要在 formalization + informed system design 层面，非 algorithmic breakthrough。建议在 Introduction 中显式声明此定位。** Excitement 分歧（R1: 3.0, R2: 2.5），Director 取 2.75。

**SF2** [major, R2-W1, R1 AGREE] **DR↔CF trade-off 选择性报告**
Abstract 声称 "near-eliminates DR (94-100% reduction)"，但 Table 1 SciERC Llama Full S1 显示 DR 13.37→0% 的同时 CF 0→12.02%，净 violation 减少仅 ~1.35 pp。CF trade-off 是 model-dependent（Qwen CF 仅 0.035%），但 Abstract/Intro 的叙事重心完全在 DR reduction 上。建议：(1) 在 Abstract/Intro 中将 DR reduction 与 CF introduction 并列报告；(2) 考虑使用总 violation rate（DR+CF）作为补充指标。

**SF3** [major, R1-N3, R2 AGREE] **WikiEvents fine-tuning 评估统计功效不足（n=20）**
Fine-tuning composability 仅基于 20 文档验证，bootstrap CI 可信度有限。论文已标注 "preliminary"，但主文叙事仍从此得出 composability 结论。此问题连续 4 轮（R12-R15）被标记，R14 补充了 per-doc variance 和统计功效讨论。建议将 WikiEvents fine-tuning 结论从主要 claim 中移除或标注 "indicative only"。EE schema 结构比 RE 更复杂（嵌套 argument roles），但论文对此差异讨论不足。

**SF4** [major, R1-W1 = R2-W2, 共识] **κ̄ 贡献定位过高**
κ̄ 定义为 1-|σ(r)|/|E|² 的平均值，直觉明显（schema 越紧约束效果越好）。n=6 的回归分析（Figure 2）无统计推断力，论文自身承认。但 §1 contributions 仍将其列为主要贡献。建议降级为 "diagnostic metric introduced for deployment guidance"，从 contributions list 中合并到实验评估子点。

**SF5** [should-fix, R1-N4, R2 REBUT] **70B 评估过于 preliminary**
R1 认为 Abstract "applicable to autoregressive LMs" 过宽。R2 反驳：这是适用范围声明（有 logit access 即可用），非性能保证；且 Table 4 已提供 70B 验证数据显示相同 DR 消减模式。**Director 判定：R2 论点合理，降为 should-fix。** 建议在 Limitations 中加一句明确承认 70B scale 验证有限。

**SF6** [warning, R1-W2, R2 AGREE] **Fallback causal tracing 缺失**
Residual DR violations 中有多少源自 grammar-first fallback 事件未被量化。Appendix D 按 violation type 分类（entity type error / schema coverage gap / model generation error），但未按 fallback vs non-fallback positions 分类。追踪 fallback 事件与 residual violations 的关联性将直接回答 fallback 机制的实际影响。

**SF7** [warning, R1-W4, R2 AGREE] **仅英语数据集评估，跨语言泛化未讨论**
3 个数据集均为英语。Continuation masking 依赖 subword tokenization，跨语言泛化（特别是中日韩等非空格分词语言）是实质性开放问题。Limitations 未明确标注语言覆盖缺口。

**SF8** [warning, R1-W5, R2 AGREE with nuance] **Post-hoc filtering 对比不够公平**
Post-hoc filtering baseline 是 discard-based（丢弃 invalid triples），而非 correction-based（替换 invalid types）。Post-hoc correction 可能构成更强的 baseline。R2 补充：correction 需额外 type similarity 信息，论文的 discard baseline 是 assumption-minimal。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全达成共识（交叉分享后均 [AGREE]）：

1. **[AGREE] 缺少竞品实验对比是最关键缺陷**（MF1）——两位 Reviewer 均将此列为 critical
2. **[AGREE] "Guarantee" overclaiming 需修正**（MF2）——建议替换为 "enforcement" 或 "near-elimination"
3. **[AGREE] WikiEvents n=20 不足以支撑 composability 结论**（SF3）
4. **[AGREE] κ̄ 应降级为 diagnostic metric**（SF4）
5. **[AGREE] 页数超限需修复**（MF3）
6. **[AGREE] DR↔CF trade-off 需在 Abstract/Intro 中并列报告**（SF2）
7. **[AGREE] Fallback causal tracing 应补充**（SF6）
8. **[AGREE] 英语覆盖缺口应在 Limitations 中标注**（SF7）
9. **[AGREE] Decidability taxonomy 是论文最大亮点**
10. **[AGREE] 实验评估全面性和统计实践均属优秀**

## Reviewer Divergence

以下问题存在分歧，交叉分享后未完全消解：

1. **[分歧] 新颖性定位（SF1）**：R2 认为组件级无创新（Excitement 2.5），R1 认为 Prop 1 有独立理论价值（Excitement 3.0）。Director 取 2.75——formalization 有价值但方法层面确为工程集成。

2. **[分歧] 70B 评估严重性（SF5）**：R1 major vs R2 should-fix。R2 论证 "applicable to autoregressive LMs" 是适用范围声明而非性能保证。Director 采纳 R2 论点，降为 should-fix。

3. **[分歧] 页数超限严重性（MF3）**：R2 critical（desk reject 风险）vs R1 minor-major（8 行不构成 desk reject）。Director 取 major——必须修复但 8 行溢出在 ARR 实践中非自动 desk reject。

4. **[分歧] Supervised baseline 对比（R2-W4）**：R2 认为应加 PURE/PL-Marker F1 作为 upper-bound。R1 反驳为 category error——OntoCoDec 是约束层非 IE system。Director 采纳 R1 论点，不列为 issue。

5. **[分歧] S1 vs S2 论证（R1-W3）**：R1 认为缺乏 cost-benefit 分析。R2 反驳 §5.1 已提供三维度对比。Director 判定：现有论证基本充分，不列为独立 issue。

---

## Questions

1. Residual DR violations（如 Table 10 中 fine-tuned 设置下 36 个残余 violations）中有多少直接源自 grammar-first fallback 事件？
2. 在 70B+ 模型上 baseline violation rate 是否显著低于 7-8B？OntoCoDec 的边际价值如何？
3. 当同一实体以不同表面形式出现时（如 "Barack Obama" 和 "Obama"），entity registry D 如何处理？是否导致同一实体被赋予不同类型？
4. DocRED beam search 仅在 50-doc subset 上评估的原因是什么？是否有 full-set 结果可补充？
5. 为什么没有与 GCD (Geng et al., 2023) 在 SciERC 上做直接数值对比？grammar-only ablation 隐含了 Level 1 对比，但这需要显式化论证。

---

## Missing References

- **GCD** (Geng et al., 2023, EMNLP)：已引用但未做实验对比——SciERC 上 grammar-constrained decoding 的最直接前序工作 [R1, R2 共识]
- **BoostCD** (Sakota et al., 2025, EMNLP)：已引用但未做实验对比——IE constrained+unconstrained 混合方法 [R1, R2 共识]
- **CRANE** (Banerjee et al., 2025, ICML)：已引用但仅定性讨论——semantic constraint reasoning [R1]
- **Riedel et al. (2009)** Markov Logic Networks for IE：constraint-based IE 历史工作 [R2, R1 AGREE]
- **Anderson et al. (2017)** Constrained Beam Search：早期约束 beam search 工作 [R2, R1 AGREE]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目未配置 external_review.paperreview_ai。

---

## Visual Layout Check（非评分项）

**状态：已完成** (2026-05-21 01:19 → 01:23, 约 4 分钟)

| 严重性 | 数量 | 关键发现 |
|--------|------|----------|
| Critical | 1 | 主正文溢出至第 9 页，>80% 空白（与 MF3 一致）|
| Warning | 6 | (1) Pages 1-2 连续纯文本无 display item，缺少视觉锚点；(2) Pages 4-5 同样无 display item；(3) Pages 6-7 全部 5 个 table 集中形成"表格墙"；(4) Page 8 有 4 个 section header 堆叠，给人草率收尾印象；(5) 主正文仅 1 个 figure + 5 个 table，无实验结果可视化图；(6) Appendix Figure 3 红绿色对色盲不友好 |
| Info | 8 | Figure 1 建议提前到 p1-2；booktabs 表格质量良好；引用格式正常；Appendix 图表可读性好 |

**视觉审查总评**：主正文 display item 分布严重不均（pages 1-5 无图表 → pages 6-7 表格密集 → page 8-9 section 堆叠+溢出），阅读节奏失调。建议将 Figure 2/3 从 Appendix 移入主文以平衡视觉密度，同时压缩 §6/§7 解决页数溢出。

---

## Overall Assessment

**评分：3.0 / 5（Findings）**

**EMNLP 2026 ARR 评分对照：3 = Findings（可被 Findings 接收）**

**Confidence：4/5**（两位 Reviewer 均为 4/5）

### 评分理由

**支撑 Findings 接收的因素：**
- Decidability taxonomy + Proposition 1 是该领域首次将 IE 约束映射到形式语言理论的尝试，有独立理论价值
- 实验评估覆盖面广（3 数据集 × 4 模型 × 多解码策略 × zero-shot/fine-tuning），ablation 设计精良
- DR near-elimination（94-100%）+ R-F1 不显著下降的核心结果可靠（bootstrap 检验）
- Fine-tuning composability 验证有实际部署价值
- 附录（24 页）和统计实践远超同类投稿

**阻碍 Conference 接收的因素：**
- [最关键] 完全缺失与 GCD/BoostCD/CRANE 等同类方法的实验对比——边际贡献无法量化。此问题已连续 4 轮被标记，始终未以 head-to-head 实验方式解决。
- "Guarantee" 措辞系统性 overclaiming——Abstract/Intro 承诺的保证水平与 fallback 机制、Level 3 缺口、残余 CF 的实际情况不匹配
- 新颖性主要在 formalization + informed system design 层面，组件级创新有限（grammar layer = XGrammar 应用，semantic layer = 运行时类型检查）
- WikiEvents 20-doc fine-tuning 评估统计功效不足，κ̄ 基于 n=6 无统计推断力
- 正文超 8 页限制（回归问题）

**提升至 Borderline Conference（3.5）的路径：**
1. 至少在 SciERC 上与 GCD 做显式数值对比（可以基于 grammar-only ablation 论证等价性，但必须显式化）
2. 将 "guarantee" 全面替换为 "enforcement"/"near-elimination"，Abstract/Intro 措辞与 Limitations 对齐
3. 修复页数溢出
4. 在 Abstract/Intro 中并列报告 DR reduction 和 CF introduction

---

## Detailed Comments

### §1 Introduction
- "formal guarantees at each level"（p2, contribution 1）→ 应改为 "formal enforcement with best-effort semantics"
- κ̄ 在 contribution 1 中的权重应降低——合并到实验评估子点而非独立列出
- "applicable to autoregressive LMs with logits access"（Abstract）→ 建议限定为 "validated on 7-8B scale models with preliminary 70B results"

### §3 Method
- Enabling dependency（§3.1 Corollary）在主文中仅用自然语言描述，缺少正式定义
- Grammar-first fallback（§4）的 cascade 效应未分析：fallback-induced 类型错误是否传播到后续 triple

### §4 Constraint Composition
- Fallback 触发率（first-token 0.5-5.7% ZS, ≤0.11% FT）已报告，但应追踪 residual DR violations 到 fallback positions
- 建议增加 "net violation change"（ΔDR+ΔCF）作为 Table 1 的补充列

### §5 Experiments
- Table 1 "Tgt." 列含义未在正文或表注中解释
- SciERC Llama CF=12.02% 应在主文而非仅 Limitations 中讨论
- DocRED beam search 50-doc subset（§5.3）代表性需论证或补充 full-set 结果
- WikiEvents §5.4 应增加 EE schema 约束编译过程与 RE 差异的讨论

### §6 Related Work
- grammar-only ablation 与 GCD 的等价性论证应在此节显式化
- BoostCD 的差异（constrained+unconstrained 混合 vs OntoCoDec 的 pure enforcement）应更清晰地论述

### §7 Discussion and Conclusion
- 压缩至第 8 页内（当前溢出 ~8 行）
- 建议增加 "Our contribution is not a new decoding algorithm, but a formal analysis that reveals the necessity of a two-layer design" 等 novelty 定位声明

### Limitations
- 增加语言覆盖缺口讨论（仅英语数据集，continuation masking 对非空格语言的影响）
- 增加 70B scale 验证有限的明确说明

### Format
- 清理 orphan bib entries（chen2024agentre, fan2024fsn）
- 核实 Abstract "1-2% even after LoRA fine-tuning" 与 Table 2 数据的一致性
- Figure 3（Appendix）红绿色对色盲不友好，建议改用 Okabe-Ito 色板
