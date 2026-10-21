---
round: 3
overall_score: borderline
timestamp: 2026-05-16T17:50:14.844788+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：OntoCoDec — Type-Constrained Information Extraction via Compiled Ontology Constraints

**Venue**: EMNLP 2026 (ARR May 2026 cycle, Long Paper)
**审稿模式**: 圆桌会议 (2 Reviewers × 1 Round + Cross-sharing)
**日期**: 2026-05-16

---

## Summary

OntoCoDec 将 IE 本体的 domain/range 约束编译为两层解码时约束：grammar layer（XGrammar CFG，强制 JSON 结构 + 词表成员性）和 semantic layer（实体注册表 + 动态 logit masking，强制 domain/range 类型有效性）。两层通过 bitwise AND 组合，具有 enabling dependency（grammar 是 semantic 的前提）。在 SciERC (7 relations) 和 DocRED (96 relations) 上，3 个模型 × 2 个数据集的实验表明 DR violation 下降 42-99%，F1 中性或显著提升。与 LoRA fine-tuning 组合后 DR ≤ 0.20%。

论文技术上可靠、实验全面、形式化质量高。主要问题在于 Abstract/Introduction 的选择性报告（省略 CF 副作用）、n=4 回归的过度解读、以及 novelty 定位与先驱工作区分的不足。

---

## Strengths

**S1** [Consensus] **形式化质量高**：§2-4 的本体定义、pair-based enforcement（σ(r) formulation）、non-rectangularity 分析（SciERC 0/7、DocRED 23/96 rectangular）、decidability taxonomy（local / prefix-decidable / non-local）数学严谨无歧义。Sequential masking 的必要性有定量支撑（independent check over-permits 33-37% spurious type pairs）。

**S2** [Consensus] **实验设计全面且控制变量到位**：5-way ablation (SciERC) + 4-way ablation (DocRED) 有效隔离各层贡献。Cross-model 3 模型验证、composability matrix (2 models × 2 datasets × 2 settings)、FT 4-way ablation (Table 8)、runtime profiling (Table 5)、post-hoc filtering 完整 10 组对比 (Table 9)。Bootstrap significance testing (10K iterations) + CI 符合 ARR 统计报告标准。

**S3** [Consensus] **CF trade-off 的正文讨论诚实**：§5 明确报告 CF 增加，Appendix B 包含 CF-DR ablation (Table 5, +3.99pp total violations)、CF 分布分析 (Table 7, 63.3% involve Generic)、FT mitigation (88% CF reduction)。这是学术诚信的体现。

**S4** [Consensus] **实用性强**：Runtime overhead 仅 +2.3% (SciERC) 到 +5.4% (DocRED)，sub-additive。Training-free，与 fine-tuning 正交组合后 DR ≤ 0.20% at < 0.6pp F1 cost。可直接部署。

**S5** [R1] **数值一致性通过核查**：R1 逐表核查 Table 1-9 与正文引用的一致性和百分比计算，全部验证通过（仅一处精度标注：Introduction "42-90%" 范围跨三模型但未明示）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [Consensus: R1 critical + R2 agree] **Abstract/Introduction 系统性省略 CF 副作用，构成选择性报告**

Abstract 声称 "reduces domain/range violations by 94% (15.37%→0.93%) while maintaining extraction F1"，三条 Contribution 均只提 DR 下降。但 CF (cross-field consistency) 违规从 0.08% 飙升至 9.90%（SciERC, 124×增幅），Llama DocRED 从 0.17% 升至 12.02%（71×增幅）。CF 本质上也是本体约束违反——同一实体在不同 triple 中被赋予不同类型。

论文在 §5、§7、Appendix B 对 CF 有诚实讨论（包括 CF-DR trade-off ablation 和 FT mitigation），但 Abstract/Intro 的沉默使只读摘要的读者误以为该方法"几乎消除了本体违规"。这属于 framing bias，符合 ARR guidelines 中 "overclaiming" 的定义。

**修改建议**：Abstract 末尾加一句 CF caveat（如 "CF violations increase under zero-shot S1 (up to 12.02%) due to per-relation independent enforcement; fine-tuning reduces this to ≤1.18%"）。Introduction Contribution 3 也应提及 CF 作为 trade-off。

**MF2** [Consensus: R1 critical + R2 agree] **R²=0.886 基于 n=4 数据点被过度解读为"预测框架"**

线性回归 y=0.366x−0.138 有 2 个参数，n=4 仅留 2 个自由度。更关键的是，4 个数据点为 2 datasets × 2 models，两个 dataset 的 tightness 差异巨大（SciERC τ̄=0.333 vs DocRED τ̄=0.842），tightness 单一变量就可能解释大部分方差——本质上是"两组各两点"的比较。Appendix B 正确地未报告 p-value，但 Abstract（"varies predictably"）和 §7（"predictive framework"）仍做出定量预测性声明，不符合统计严谨性标准。

**修改建议**：(1) Abstract "varies predictably" → "is consistent with a dual-factor pattern"; (2) §7 "predictive framework" → "descriptive pattern"; (3) 考虑加入 Mistral 的 2 个数据点 (n=6) 并诚实报告拟合变化。

### Should-Fix（影响评分但不一票否决）

**SF1** [R2 critical, R1 REBUT → warning] **Novelty claim 'first' 需进一步缩窄 + 缺 DORE 引用**

Contribution 2 声称 "the first to automatically compile IE ontology domain/range constraints into token-level semantic masks"。R2 指出 DORE (Vukovic et al., SIGDIAL 2024) 已将 ontology constraints 用于 constrained decoding RE。R1 反驳称 DORE 是 output-selection level（CoT + confidence threshold），非 token-level logit masking，技术路径根本不同。

交叉共识：DORE 必须引用，'first' claim 应缩窄为 "first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE"。severity 降为 warning。

**SF2** [R2 critical, R1 agree w/ nuance → warning] **与代码生成先驱工作的技术差异在主文中阐述不足**

§6 仅两句话处理代码生成先驱（Synchromesh, PICARD, MGD, PLDI2025）。真正的 novelty——entity registry 在生成中动态构建、constraint target 从 free text 推断而非 declared type annotation——仅在 Appendix A 展开。R1 认可这是 presentation issue（novelty 论证存在且正确，只是位置不对）。

**修改建议**：在 §1 或 §3 开头加 2-3 句话阐述为什么代码生成的 type→automaton→mask pipeline 不直接适用于 IE。

**SF3** [R1 warning + R2 agree] **Post-hoc filtering 对比叙事与实验数据不一致**

Post-hoc filtering 在 5/6 zero-shot 配置中 F1 更高 (Table 9)。Introduction "Post-hoc validation wastes compute on discarded outputs" 的否定语气与数据不符。OntoCoDec 的真实优势在于：(a) recall 保持（6/6 zero-shot settings）, (b) ET violation 消除, (c) 高 rejection rate 时 post-hoc 崩溃 (Mistral DocRED 73.7%), (d) fine-tuning 下两者收敛。

**修改建议**：§5 正文加入 post-hoc 对比摘要（1-2 句），Introduction 将 "wastes compute" 改为条件性表述。

**SF4** [R1 warning + R2 agree] **Parse failure 在约束下增加，构成潜在混淆变量**

Llama DocRED parse failure 从 68/998 (6.8%) 增至 91/998 (9.1%)，增幅 34%。被排除的文档可能系统性偏向某些关系类型，导致 DR/F1 在非随机子集上评估。Qwen DocRED 脚注显示排除 parse failure 后 R-F1 delta 从 -0.30pp 变为 +0.03pp，说明影响真实存在。

**修改建议**：补充 Llama DocRED zero-shot 的 parse-failure-excluded 分析，或至少讨论约束增加 parse failure 的原因。

**SF5** [R1 warning + R2 agree] **Zero-shot R-F1 ~8% 的实际意义仅在 Appendix 讨论**

Appendix B "Practical Significance of Zero-Shot F1" 段落有详细讨论（F1 as control variable, supervised SOTA ~49-53%），但正文 §5 未提及。同时，§5 高亮 DocRED +0.50pp (p<0.001) 作为积极结果——如果 F1 只是 control variable，不应用 p-value 强调其改善；如果 F1 重要，8% 的绝对值需在正文讨论。

**修改建议**：§5 加 1-2 句话上下文化 zero-shot F1 水平。

**SF6** [R1 warning + R2 agree] **First-subword-token 唯一性假设应升级为设计假设**

§3.4.3 将此作为 implementation detail（"verified for both tokenizers, 6 entity types each"），但这是方法适用范围的根本性限制。6 个 entity types 的唯一性验证几乎是 trivial 的。Wikidata (7000+), UMLS (100+), ACE 2005 (18) 都远超此规模。

**修改建议**：在 §3 Method 中将此从 implementation detail 提升为 explicit design assumption。

**SF7** [R1 warning] **Semantic-only 模式在 DocRED 上反直觉地增加 ET (2.48%→4.22%)**

Semantic layer 声称仅在 HeadType/TailType 位置激活，不应影响 ET。可能原因：无 grammar 保护时 position detection 误判导致 mask 干扰 entity type generation（RV 也略增 29.66%→29.87% 支持此假设）。

**修改建议**：加 1-2 句解释此现象的机制。

**SF8** [R2 warning + R1 agree] **缺少代码/数据可复现性声明**

论文未包含任何代码/数据释放声明。ARR reproducibility 评分维度要求说明。

**修改建议**：添加 "Code and data will be released upon acceptance"。

**SF9** [R2 warning, R1 agree weakly] **Missing references: DORE, GenIE, EnriCo 在主文 §6**

DORE (SIGDIAL 2024) 必须引用并区分。GenIE (Josifoski et al., 2022) 和 EnriCo (Zaratiana et al., 2024) 仅在 Appendix A 出现，应移至 §6 主文——两者是与 OntoCoDec 最直接相关的 constrained decoding IE 系统。

### Minor Issues（不影响接收）

- **符号冲突**：τ 同时用于 entity type (§3) 和 constraint tightness (§4)，建议 tightness 改用 κ
- **Table 2 S2 行**：CF=8.03%, R-F1=8.03 数值巧合，视觉上像复制粘贴错误
- **DocRED RV=0.03% 残余**：Grammar/Full S1 下 RV 应为 0%，0.03% 来源未解释
- **SciERC/DocRED 消融不对称**：SciERC 包含 S2，DocRED 不包含，未说明原因
- **§5.1 Violation Landscape 位置**：混合 motivation 和 experimental setup，建议提前到 §2
- **Introduction "DR ↓42-90% on DocRED"**：42% 来自 Mistral，90% 来自 Llama，范围跨三模型但未在 Contribution 3 中明示
- **Greedy decoding 限制**：所有实验使用 greedy decoding，beam search/sampling 下 constraint composition 行为（特别是 fallback 频率）可能不同
- **"Global entity-level type consensus" (§7/Limitations)**：作为 CF 解决路径但无可行性分析

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识（均 [AGREE]）：

1. **CF 省略 Abstract/Intro** → must-fix，加 CF caveat
2. **R² n=4 overclaim** → must-fix，降级措辞
3. **Post-hoc filtering 叙事** → should-fix，正文加摘要
4. **Parse failure 增加** → should-fix，补充分析
5. **Zero-shot F1 ~8% 上下文** → should-fix，正文加讨论
6. **First-subword-token 假设** → should-fix，升级为设计假设
7. **代码/数据声明** → should-fix，添加声明
8. **Semantic-only ET 增加** → should-fix，解释机制

---

## Reviewer Divergence

**GCD/BoostCD 实验对比**：R2 认为 critical（缺少与同领域 constrained decoding IE 系统的直接实验对比），R1 REBUT（Grammar-only ablation 行即为 GCD-class baseline 的效果上界，GCD 架构上无法覆盖 domain/range constraints，要求对比等同于证明 "semantic > syntactic" 这一 trivially true 的命题）。

**Director 判断**：R1 的反驳有说服力——论文的 grammar-only 消融行确实已覆盖 GCD 能力范围。但建议在 §5 或 §6 中加一句显式声明（"The grammar-only row in Table 2/3 represents the capability ceiling of prior grammar-constrained decoding approaches such as GCD, which by design cannot enforce domain/range constraints"），使隐含对比关系显式化。不列为 must-fix。

**CF 省略的 severity**：R1 判 critical，R2 判 warning 但同意必须修复。R2 理由：论文并非隐藏问题（§5/Appendix 有诚实讨论），只是 Abstract/Intro framing 有偏。

**Director 判断**：列为 must-fix。Abstract 是大多数读者唯一阅读的部分，省略核心 trade-off 对读者产生误导，无论正文是否讨论。

**"Tautological" 论证风险**：R2 认为 "约束减少约束违反" 是循环论证。R1 partial REBUT：novelty 在 HOW 而非 WHETHER（entity registry、sequential masking、enabling dependency），F1 中性是非显然的（文献中大量证据表明 constrained decoding 可损害质量）。

**Director 判断**：R1 的反驳有效。论文的贡献不在于"约束有效"这一结论，而在于 (a) 编译机制, (b) F1 无损保证, (c) trade-off 空间刻画。但 Abstract 的 framing 确实过于强调 violation rate numbers，建议重新定位为 "mechanism + guarantee + characterization"。归为 info 级别建议。

---

## Questions for Authors

**Q1**: CF-DR trade-off 中，DR 和 CF 的下游影响不同（CF 导致 KG 中 entity type 不一致，DR 是 triple 级别错误）。简单相加 (DR+CF) 是否合理？是否应赋予不同权重？

**Q2**: Grammar layer 在 DocRED 上将 DR 从 18.46% 提高到 26.17%（Table 3）。被强制替换的 OOV 关系名称的语义质量如何？是否可能创造"约束性幻觉"？

**Q3**: Fine-tuned 设置下 grammar layer 是 no-op (Table 8)。对于实际部署（通常使用 fine-tuned 模型），是否只需 semantic layer？"两层框架" 的 framing 在 FT 场景下是否需要 nuance？

**Q4**: R²=0.886 能否扩展到 n=6（加入 Mistral SciERC + DocRED）？如果 Mistral 的极端 baseline DR (56-57%) 偏离 linear fit，是否应诚实报告并修正声明？

**Q5**: Fuzzy Matching Protocol（token overlap >80% + edit distance ≤2）的阈值如何选择？是否在 DocRED 上调优过？

---

## Missing References

**必须引用**：
1. Vukovic et al. (SIGDIAL 2024) — DORE: Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding

**应移入主文 §6**：
2. Josifoski et al. (2022) — GenIE: state-based constraints for end-to-end IE
3. Zaratiana et al. (2024) — EnriCo: ASP-based type constraints at decoding time

**可选引用**：
4. "A Survey of Generative Information Extraction" (COLING 2025)
5. PARSE (Shen et al., EMNLP 2025 Industry) — schema guardrails
6. Schema Reinforcement Learning (ACL 2025) — training-time schema compliance

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 paperreview.ai）。

---

## Overall Assessment

**评分：borderline（介于 weak reject 和 weak accept 之间，偏向 Findings track weak accept）**

**置信度：4/5**（两位 Reviewer 均仔细通读全文和全部 Appendix，逐一核查主要数值声明，熟悉 constrained decoding 和 IE 领域）

**综合判断**：

论文在技术层面是 solid 的：形式化严谨、消融设计全面（3 models × 2 datasets × 多种 ablation + composability with FT）、统计报告规范（bootstrap + CI）、runtime overhead 小、对 CF trade-off 的正文讨论诚实。这是一项有价值的工程和实验贡献。

但论文在 **claims 层面存在系统性过度声明**：
1. Abstract 省略 CF 副作用（最高 12.02%），使 "constraint enforcement" 的核心叙事不完整
2. n=4 的 R² 被包装为 "predictive framework"
3. Novelty claim 'first' 未充分区分 DORE 和代码生成先驱
4. Post-hoc filtering 在多数场景下 F1 更高，但 Introduction 仍以否定语气处理

如果仅看实验和方法，这是一篇 **solid Findings paper**（Soundness 3.75/5, Excitement 3/5）。但当前的 overclaiming 问题使 main conference acceptance 存在风险。

**修订优先级**：
1. [Must-Fix] Abstract + Introduction 加入 CF trade-off 信息
2. [Must-Fix] R² 声明降级
3. [Should-Fix] 缩窄 novelty claim + 引用 DORE
4. [Should-Fix] 主文阐述与代码生成先驱的技术差异
5. [Should-Fix] Post-hoc 对比摘要移入正文
6. [Should-Fix] Parse failure sensitivity analysis
7. [Should-Fix] 代码/数据释放声明

**R1 评分**: 3/5 (Findings track), Soundness 4/5, Excitement 3/5
**R2 评分**: 3.5/5 (between Findings and Conference), Soundness 3.5/5, Excitement 3/5
**Director 综合**: borderline (leaning Findings weak accept)