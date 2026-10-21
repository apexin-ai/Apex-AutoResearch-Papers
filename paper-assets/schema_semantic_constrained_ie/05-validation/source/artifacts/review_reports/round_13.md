---
round: 13
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T18:54:51.258799+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 审稿报告：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**Target Venue**: EMNLP 2026 (via ARR May cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1（方法严谨性 + 实验有效性）, R2（新颖性 + 完整性 + 写作质量）
**审稿模式**: Fresh（无上轮记忆）

---

## Summary

本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的双层架构：grammar layer（CFG，保证 JSON 结构和词汇约束）和 semantic layer（prefix-decidable with state，通过运行时 entity registry 执行 best-effort pair-based domain/range 类型约束，含 grammar-first fallback）。在 SciERC、DocRED、WikiEvents 三个数据集上，对 4 个模型（7–70B，三个 tokenizer 族）进行了系统评估。LoRA + greedy S1 将 DR 降至 ≤0.09%，R-F1 ±0.6pp；beam (k=4) 在 SciERC 上消除所有违规（1.54× latency）。论文同时引入 constraint tightness κ̄ 作为描述性指标。

---

## Strengths

**S1. 系统性的实验设计与全面的消融分析（R1-S3, R2-S1, consensus）。** 五路消融（Unconstrained / Grammar / Semantic / Full S1 / Full S2）清晰隔离各层贡献；跨 3 数据集 × 4 模型 × 多配置的验证覆盖面广。Bootstrap 显著性检验（B=10,000）和配对统计比较体现了严谨方法论。这是 constrained decoding for IE 领域最全面的评估之一。

**S2. 有 principled 的形式化分析支撑架构决策（R1-S1, R2-S2, consensus）。** 三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）为 IE 类型约束按可判定性分层提供了清晰框架。Proposition 1（pumping lemma 证明 Level 2 ⊄ Level 1）给出了双层架构的 formal justification。Enabling dependency 在 Table 1 中得到实验验证（Semantic-only 仅 24% DR 降幅）。

**S3. 工程完整性和可部署性（R2-S3, R1-S2）。** Tokenizer-agnostic continuation masking 处理 BPE/SentencePiece 差异；grammar-first fallback 保证 JSON 完整性；运行时开销适中（+10–13%）；编译时间 <0.5s；框架无修改即可从 RE 扩展到 EE（245 constraints）。

**S4. Fine-tuning composability 是重要的实用价值（R2-S4, R1-S3）。** Table 2 表明约束可与 LoRA 组合使用而不损害 R-F1（p>0.05），将残余 DR 从 1–2% 压至 ≤0.09%。对实际部署场景比零样本结果更有说服力。

**S5. 诚实的 limitation 讨论（R1-S4）。** 论文明确承认 CF 的模型依赖性、WikiEvents 的初步性质、70B 评估的有限性、κ̄ 仅为描述性指标。Limitations section 覆盖多数已知局限。附录极丰富（23 页），包含完整证明、per-relation 分析、beam 兼容性、prompt sensitivity、error analysis 等。

---

## Weaknesses

### Must-Fix（影响接收决定，4 项全员共识 + 1 项有分歧）

**MF1. [critical, consensus] 正文超 8 页限制。** Section 7 Discussion and Conclusion 约 11 行溢出至第 9 页。EMNLP 2026 via ARR 严格限制长文正文 ≤ 8 页。格式违规可能导致 desk reject。机械性可修复（压缩 §7/§6/§5 冗余）但不可忽视。(R2-W1, R1-M1→升级, Visual Check critical)

**MF2. [critical, consensus] CF 代价在 Abstract/Introduction 中被系统性低估。** Abstract 用 "modest CF costs" 描述以下实际数据是误导性的：SciERC 零样本 CF 0.08%→9.90%（+123×）；WikiEvents 零样本 CF 15–21%；DocRED beam 零样本 CF 28.4%→21.4%（远未 "resolve"）。Introduction 完全未提及 CF。隐藏主要副作用降低论文可信度。Abstract 应明确写出 CF 范围和条件；Introduction 应讨论 DR↔CF trade-off。(R2-W2, R1 AGREE 升级)

**MF3. [critical, consensus] 缺少最直接可比的 IE constrained decoding baseline 量化对比。** BoostCD (Sakota et al., EMNLP 2025) 和 IterGen (Ugare et al., 2025) 在 §6 被引用但实验中完全无对比。BoostCD 与 GCD 同团队，GCD 已在 SciERC 上有结果（§5.1 引用），因此 BoostCD 极可能覆盖相同 benchmark。§6 称 "different benchmarks preclude direct comparison" 但未提供证据支撑。缺失最自然 baseline 使 Contribution 3 "first systematic evaluation" 的声称站不住脚。(R1-W1, R2 AGREE 采纳)

**MF4. [critical, consensus] WikiEvents fine-tuning 仅 20 文档测试集，Contribution 3 措辞过度。** 零样本 246 文档尚可，但 FT composability 的 20 文档测试集 CIs 宽达 ±0.05–0.06，无法支撑 "systematic evaluation" 和 "framework generalizes to event extraction" 的措辞。另：零样本 entity F1 从 0→12–18% 主要来自格式修复（unconstrained 输出无法被 parser 处理）而非语义提取改善。应降级为 "preliminary demonstration"。(R1-W2, R2-W6 consensus)

**MF5. [critical/warning, divergence] κ̄ 作为独立 Contribution 2 定位过高。** κ̄ = 1−|σ(r)|/|E|² 本质上是约束表归一化密度。仅 2 个数据点验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842）。κ̄ 对 Mistral 预测失效（SciERC DR 降幅 76% vs 期望 94–99%），说明无 confusability 协变量 κ̄ 指导价值有限。**R2 列为 must-fix（不应列为独立 contribution），R1 同意问题但 prefer should-fix（方向性指导仍有价值）。** 建议至少降级为分析工具，整合入实验讨论。

### Should-Fix（影响评分但不一票否决，6 项）

**SF1. "any autoregressive LM" 声称超出验证范围。** 主要实验 7–8B，70B 仅 preliminary，无 <7B / API-only 验证。§1 仍有 "applies to any autoregressive LM"。(R2-W4, R1 AGREE)

**SF2. DocRED 零样本 DR 降幅仅 45% 的讨论不充分。** 论文将此归因于 κ̄ 差异但只是 restate 了现象。残余 DR 10.21%（每 10 个 triple 约 1 个违规）对 "type-safe extraction" 构成挑战。深层原因：GENERIC←→X 歧义占 63.3% CF violations，属 schema 固有模糊性。(R2-W5, R1 AGREE)

**SF3. DocRED beam search 零样本仅 50-doc 子集（998 的 5%）。** Abstract/§5 的 "resolvable via beam search" 在 DocRED 上证据不足。Appendix Table 15 显示 CF 仅 28.4%→21.4%。"Resolvable" 仅在 FT 或低 κ̄ 下成立。(R1-W4, R2 AGREE)

**SF4. "formally compiles" 措辞对 semantic layer 过度。** Grammar layer 是传统编译（ontology→EBNF→PDA）；semantic layer 是运行时规则解释（runtime rule-based masking）。更准确："compile-time grammar generation + runtime constraint interpretation"。(R1-W5, R2-W7, consensus)

**SF5. 缺乏与 GoLLIE 等 schema-aware IE 系统的量化参考。** 读者缺乏 F1 水平锚定——"7–8B model + OntoCoDec, R-F1 40–46%" 在领域中处于什么水平？引用 GoLLIE published numbers 即可，不需重跑实验。(R1-W6, R2 AGREE)

**SF6. Pumping lemma 证明存在形式化 gap（presentation, not correctness）。** Proof sketch 使用位置索引模型，但实际 JSON 使用名称字符串引用。核心论证在名称引用下仍成立（name→type 随机访问超出 PDA 能力），但应明确说明 abstraction 关系。(R1-W3, R2 AGREE)

### Minor（不影响接收，6 项）

- **M1.** S1/S2 命名不直观，混用 "S1 (joint extraction)" 和 "Full (S1)"。(R2-M3, R1 AGREE)
- **M2.** Orphan bib entry（schmidt2025grammar）+ 2 篇 unverified citations（formattax2026, regino2025kgcurator）。(R2-M1/M5, R1-M4)
- **M3.** 表格字体偏小（Table 1/3/4 用 resizebox 压缩 8+ 列）。(R2-M2, R1-M2)
- **M4.** §4 脚注 1（对称 relation 的 κ 计算）影响 κ̄ 语义，应在正文讨论。(R2-M4, R1 AGREE)
- **M5.** "Best-effort pair-based enforcement" 首次出现时需完整 inline definition。(R1-M3, R2 AGREE)
- **M6.** Table 25 红绿色标注违规/修正，色盲不友好（Visual Check 发现）。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：

1. **正文超页 must-fix**：R1 初审列为 minor，交叉后升级为 must-fix
2. **CF 透明度 must-fix**：R1 初审列为 should-fix（聚焦 beam search claim），交叉后接受 R2 的更全面角度，升级为 must-fix
3. **BoostCD 缺失 must-fix**：R2 初审遗漏，交叉后采纳 R1 的 must-fix
4. **WikiEvents 统计效力**：R1 列 critical，R2 列 warning 但承认 R1 理由成立
5. **所有 Should-Fix 和 Minor**：全部 AGREE（仅 R1-M5 G(t)=∅ 边界情况被 R2 REBUT——XGrammar PDA 保证合法路径上 G(t)≠∅，属实现层 invariant 而非框架问题）

---

## Reviewer Divergence

**DIV1. κ̄ 严重度**：R2 = must-fix（不应列为独立 contribution），R1 = should-fix（方向性指导有价值）。核心分歧：R2 认为 2 数据点的 trivial metric 列为 Contribution 2 是 overclaiming；R1 认为 "descriptive" 措辞已降低期望且 deployment heuristic 有实用价值。

**DIV2. Overall 评分**：R1 = 3.5（Borderline Conference），R2 = 3.0（Findings）。
- R1 逻辑：核心技术 sound，实验覆盖广，overclaiming 是 presentation 问题非 substance 问题，修订路径明确
- R2 逻辑：overclaiming pattern 跨多个维度（"modest" CF / κ̄ contribution / "any LM" / "formally compiles"）累积损害可信度；3 个 must-fix 叠加使 3.0 更准确
- R1 交叉后承认 R2 的 overclaiming pattern 论点成立，但认为 Limitations section 的诚实性和附录深度（33 页）部分抵消
- R2 交叉后承认 decidability taxonomy 有 marginal 迁移价值，但维持 3.0

**DIV3. Excitement**：R1 = 3.0（decidability taxonomy 有跨领域迁移价值），R2 = 2.5（taxonomy insight density 有限，三级分类相当直观，Proposition 1 是 confirmatory 而非 surprising）。

---

## Questions（需要作者澄清）

**Q1.** [R2-Q1] Grammar-first fallback 在 36.6% 的 type-bearing positions 触发（§4, SciERC 零样本）。这是否意味着约三分之一的类型位置实际上没有任何类型约束？"Type-constrained extraction" 标题是否过度承诺？

**Q2.** [R1-Q2] BoostCD 在 SciERC/DocRED 上的 constrained decoding 结果是什么？如果不可比，请具体说明原因（约束类型不同？输出格式不同？其他？）

**Q3.** [R1-Q4] LoRA fine-tuning 是在有约束还是无约束解码条件下训练的？如果无约束训练，fine-tuned 模型输出分布与 constrained decoding mask 之间可能存在 distribution mismatch。

**Q4.** [R2-Q2] Llama SciERC fine-tuned 残余 DR 0.09%（36 violations：entity type errors 39%, schema coverage gaps 33%, model errors 28%）——33% 来自 schema coverage gaps。这对新领域部署有何影响？

**Q5.** [R2-Q4] WikiEvents Grammar-only 行在 Table 5 中 F1 标记 "---"，但 grammar-only 应可生成结构化输出。是因为 RoV 64–77% 导致无法可靠评估吗？

**Q6.** [R2-Q5] 论文引用 Tam et al. (2024) 称 "extraction tasks are robust to format constraints"，但 Tam et al. 的实验非 IE-specific。是否有 IE-specific 证据？CRANE (Banerjee et al., 2025) 暗示 constrained decoding 在结构化任务中也有隐性代价。

**Q7.** [R1-Q1] Pumping lemma 证明中 pumping 操作如何破坏名称引用下的类型一致性？位置偏移的推理如何适用于名称引用格式？

---

## Missing References

1. **BoostCD (Sakota et al., EMNLP 2025)**: 已在 §6 引用但缺乏实验对比——最直接的 IE constrained decoding competitor (R1-W1, R2 adopted)
2. **GenIE (Josifoski et al., 2022)**: 最早系统化应用 constrained decoding 于 IE 的工作之一，主体 §6 遗漏（仅在附录 B）(R1)
3. **NNF (Nusgart et al., 2025, "Constrained Decoding with Grammars and Lookahead")**: grammar-constrained decoding lookahead，与 grammar-first fallback 相关 (R1)
4. **LasUIE (Fei et al., 2022)**: 结构化生成 + IE 的早期工作 (R2)

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目配置中未启用 `external_review.paperreview_ai`）。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（2026-05-20T18:36–18:40, 约 4 分钟）

| 严重度 | 数量 | 关键发现 |
|--------|------|----------|
| Critical | 1 | 正文溢出至 p9（与 MF1 一致） |
| Warning | 3 | 前 2 页纯文本无视觉锚点；p8 整页纯文本（Related Work + Conclusion）；附录 B 连续 3 页纯文本 |
| Info | 8 | Figure 1 位置合适（p3）；pp5–7 table 密度良好（5 tables/3 pages）；无 margin 溢出、未解析引用、排版错误；Table 25 红绿色不色盲友好；末页 50% 空白可接受 |

**主文 display item 统计**: 1 figure + 5 tables = 6 items / 8 pages（合理范围 5–8）。

---

## Overall Assessment

### 评分汇总

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.0 | 2.5 | **2.75** |
| Reproducibility | 4.0 | 4.0 | **4.0** |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4 | 4 | **4** |

### Overall: 3.0 — Findings

**综合评分取 3.0（Findings）的理由：**

1. **4 项全员共识 Must-Fix + 1 项有争议 Must-Fix**：正文超页（desk reject 风险）、CF 代价被系统性低估（可信度问题）、缺少最直接 baseline 对比（贡献 scope 问题）、WikiEvents 统计效力不足（claim 支撑问题）、κ̄ 贡献定位过高。这些问题不是孤立的——它们构成了一个 **overclaiming pattern**：论文在多个维度（"modest" CF / "formally compiles" / "any autoregressive LM" / "systematic evaluation" / κ̄ as contribution）对自身贡献的呈现高于实际支撑。

2. **核心技术贡献 sound 但 novelty 有限**：decidability taxonomy 是有用的形式化贡献，但三级分类相当直观（CF/stateful/non-local），Proposition 1 是 confirmatory 而非 surprising。双层架构（grammar mask ∩ semantic mask）是已有技术的 principled 组合，非 novel mechanism。

3. **实验全面但有关键缺口**：缺少 BoostCD/IterGen 对比是最实质性的缺陷——如果 BoostCD 在 SciERC 上的 DR 降幅可比，OntoCoDec 的增量贡献将大幅缩水。

4. **明确的修订升级路径**：补充 BoostCD 对比、修正 CF 叙述、降级 κ̄ 定位、限定 claim 范围、压缩页数——这些修订均不改变核心技术贡献，修订后有望达到 3.5（Borderline Conference）。

### 一句话总结

一篇技术扎实、评估全面的系统论文，decidability taxonomy 和双层约束执行框架设计干净；但存在 overclaiming pattern（CF 代价低估、κ̄ 贡献包装、声称范围过宽），且缺少与最直接 IE constrained decoding competitor（BoostCD）的量化对比。当前状态为 Findings 级别，修订后有明确的 Borderline Conference 升级路径。

---

## Detailed Comments

### §1 Introduction
- "applies to any autoregressive LM" → 限定为 "with logits access, validated on 7–70B"
- Contribution 2: κ̄ 从独立 contribution 降级为 "we additionally introduce..."
- Contribution 3: "systematic evaluation...extends to event extraction" → 区分 RE (systematic) 和 EE (preliminary demonstration)
- CF trade-off 应在 Intro 即提及（当前完全缺失）

### Abstract
- "modest CF costs" → 写出具体范围："CF rates of 0–9.9% (zero-shot) to ≤1.2% (fine-tuned)"
- "resolvable via beam search" → "substantially reduced by beam search under low κ̄ or with fine-tuning"
- "formally compiles" → 考虑 "translates" 或区分 compile-time/runtime

### §3 Method
- Proposition 1 proof sketch: 增加名称引用 vs 位置索引的 abstraction 说明
- "best-effort pair-based enforcement" 首次出现时给完整 inline definition

### §4 Constraint Composition
- 脚注 1（对称 relation 处理）移入正文
- Grammar-first fallback cascade 分析需更明确定量（当前 36.6% 触发率的后果分析分散）

### §5 Experiments
- WikiEvents FT: 明确 n=20 的统计效力限制，降级为 preliminary
- DocRED beam: 限定 "resolvable" claim 的适用范围
- 补充 BoostCD/GCD 在 SciERC 上的数字对比
- 提供 GoLLIE 的 F1 reference point

### §6 Related Work
- GenIE (Josifoski et al., 2022) 从附录移入主体
- "formally compiles" vs PICARD/Mündler et al. 的区分已到位，但需弱化 "formally" 措辞
- "different benchmarks preclude direct comparison" with BoostCD — 需提供具体证据或撤回此声称

### §7 Discussion and Conclusion
- 压缩至 8 页限制内
- Beam search 推荐应限定条件（"for low-κ̄ schemas or fine-tuned settings"）

### Appendix O (Pumping Lemma Proof)
- 增加位置索引→名称引用的 abstraction paragraph

### Formatting
- S1/S2 命名统一为 "single-pass S1" / "two-pass S2"
- 删除 orphan bib entry (schmidt2025grammar)
- 验证 formattax2026, regino2025kgcurator 引用完整性
- Table 25 增加非颜色视觉线索（色盲友好）