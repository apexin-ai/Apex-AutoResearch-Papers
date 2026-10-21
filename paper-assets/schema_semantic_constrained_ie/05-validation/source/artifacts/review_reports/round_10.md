---
round: 10
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T08:08:35.545312+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 10 (Fresh Review)

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR)
**Deadline**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作+格式）
**轮次**: Round 10, 1 轮独立审稿 + 1 轮交叉分享, 关键问题达成共识

---

## Summary

OntoCoDec 将 IE 本体/schema 约束编译为两层 token-level 解码约束：grammar 层（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic 层通过有状态 entity registry 和动态 logit masking 强制 per-triple domain/range 类型约束。在 SciERC、DocRED（RE）和 WikiEvents（EE）上验证，覆盖 4 个模型（8B-70B）和 3 种 tokenizer。Fine-tuning 组合性结果有力：DR ≤ 0.20%，R-F1 ± 0.6pp。Zero-shot 下 DR 降低 42-99%（校准模型），但 CF 从近零升至 9-21%，总违规改善有限（~30%）。

论文技术可靠、实验系统、分析诚实，但存在 framing 准确性问题（标题 "ontology" vs 实际经验约束）、格式硬伤（缺 ARR checklist）、和若干 claim 与证据匹配度问题。

---

## Strengths

**[S1] 形式化清晰、架构设计合理（R1-S1, R2-S1）。** 两层约束分解具有良好理论动机。Sequential masking（head domain → conditioned tail range）保证 pair-based enforcement，严格强于独立检查。Non-rectangularity 分析（SciERC 7/7、DocRED 73/96 非矩形，独立检查引入 33-37% spurious pairs）为设计提供了实证支撑。Enabling dependency 通过消融验证（semantic-only DR 仅降 24%）。

**[S2] 系统且诚实的实验设计（R1-S2, R2-S2, R2-S3）。** 五路消融清楚隔离各层贡献。CF↔DR trade-off 公开展示（Table 8: CF fallback 消除 CF 但 DR 从 0.93% 升至 14.78%）。Mistral 作为 boundary condition 诚实处理。Cross-model/cross-dataset/cross-task 覆盖全面。Bootstrap 显著性检验用于所有 F1 比较。

**[S3] Fine-tuning 组合性结果清晰有力（R2-S4）。** LoRA + S1 在所有 4 个 model×dataset 组合上达到 DR ≤ 0.20%、R-F1 ± 0.6pp。Beam search + LoRA 在 SciERC 消除所有四类违规。这是论文最强的贡献点。

**[S4] 实用价值明确（R1-S3）。** Training-free，运行时开销低（+2-13%），跨 tokenizer 兼容，scalability 到 200 entity types / 1000 relations。

**[S5] 写作质量良好（R2-S5）。** 主文无 em-dash、无 AI 黑名单用词，段落结构自然。Introduction 遵循标准叙事结构。

---

## Weaknesses

### Must-Fix（3 项，全部共识）

**[MF1] "Ontology Constraints" framing 与实际实现不匹配（R1-W1, R2 AGREE）。**
标题 "Compiled Ontology Constraints" 但 SciERC/DocRED 约束从训练数据类型对共现提取，非形式本体。§2 承认 "empirically derived type-pair constraints"，但标题/Abstract 暗示形式本体。33% residual DR 来自 coverage gaps——真正的形式本体不会有此问题。只有 WikiEvents 使用 KAIROS 形式本体。
→ **修改**：标题改用 "Schema Constraints" 或 "Type Constraints"；Abstract/§2 明确区分 formal ontology vs empirical constraints。

**[MF2] 缺少 ARR 必需的 Responsible NLP Research Checklist（R2-W1, R1 AGREE）。**
全部 .tex 文件搜索 "checklist"/"responsib" 结果为空。ARR 硬性要求，缺失可导致 desk reject。修复成本低但优先级最高。
→ **修改**：立即添加 Responsible NLP Research Checklist。

**[MF3] WikiEvents EE "preliminary" 结果在 Abstract/Contribution 中权重过高（R1-W3, R2-W4, mutual AGREE）。**
20-doc test set，trigger F1 shift -5.4pp 在此样本量下无统计意义。标注 "preliminary" 但列为 Contribution #4。Abstract 用完整句子突出 EE。
→ **修改**：将 EE 从 Contribution #4 降级为 Discussion 的初步验证；Abstract 中减少 EE 篇幅或改为 "Additionally, we provide preliminary evidence..."。

### Should-Fix（7 项）

**[SF1] "Near-lossless composability" claim 未充分考虑 CF（R1-W5, R2-W2, mutual AGREE）。**
"Near-lossless" 仅对 DR+F1 成立。ZS SciERC Tot. 15.45%→10.83%（↓30%），Llama DocRED Tot. 26.24%→14.57%。FT 下 CF ≤1.18%（可接受但非零）。
→ **修改**：限定 "near-lossless DR composability" 或在同句 acknowledge CF trade-off。Abstract 明确分层：FT = deployment claim, ZS = stress test。

**[SF2] Dual-factor pattern 统计支撑不足但作为 Contribution #1（R1-W2, R2-W9, mutual AGREE）。**
n=4, df=2, p≈0.058。Appendix 自标 "descriptive characterization" 但正文和 Contribution #1 使用 "systematic study"、"correlate with" 等较强措辞。
→ **修改**：Contribution #1 聚焦违规分类学（DR/RV/ET/CF），constraint tightness 降为 observational finding。

**[SF3] Zero-shot 叙事占实验 ~60%，FT composability 是核心价值（R1-W7, R2 partial AGREE）。**
§5 有 4 个 subsection，3 个主要展示 ZS 结果。FT composability 被压缩到 1 段 + Table 2。论文推荐的部署配置（LoRA + S1）应在实验节中获得更多空间。
→ **修改**：FT composability 提升为独立 subsection；ZS 作为 supplementary evidence。

**[SF4] §7 Discussion and Conclusion 过短（R2-W6, R1 AGREE）。**
~150 words，3 段。缺少：(1) 与 supervised SOTA (R-F1 49-53%) 的差距讨论；(2) 与 training-based 方法组合的路线图；(3) CF 解决方向的展开。
→ **修改**：扩展至包含上述三点。

**[SF5] Abstract 数据密度过高（R2-W7, R1 AGREE）。**
~190 words 中 10+ 个数字/百分比。审稿人在 30 秒内无法消化。
→ **修改**：精简到 3-4 个关键数字，其余用定性描述。移除 beam/WikiEvents 细节。

**[SF6] DocRED beam search 仅 50 docs，claim 偏强（R1-W6, R2 AGREE）。**
CI 上限 5.8%。§5.6 措辞可能被误读为包含 DocRED 全集。
→ **修改**：§5.6 明确区分 SciERC (551 docs) vs DocRED (50 docs) 的 claim 范围。

**[SF7] 缺少 GoLLIE/GCD 直接对比（R1-W4, R2 partial REBUT on GoLLIE scope）。**
Grammar-only 消融 ≈ GCD 但未显式标注。GoLLIE 互补性声称无实验验证。Post-hoc filtering 在 5/6 ZS 设置 F1 更高但主要在附录。
→ **修改**：Table 1 caption 显式标注 grammar-only = GCD ceiling；如可行，对 GoLLIE 公开输出做违规检测（low-effort high-impact）；post-hoc filtering 在主表中更显著呈现。

### Minor（6 项）

**[M1]** Bootstrap CI 未在主表报告（Tables 1-5 仅点估计）。至少 Table 2 应加 CI。
**[M2]** BibTeX 14 orphan entries、多个 duplicate keys。提交前清理。
**[M3]** Table 2 DocRED FT 数据缺失，caption scope 不清。加 DocRED FT 行。
**[M4]** κ(r) 归一化对对称关系不精确。加 footnote 说明。
**[M5]** 约束增加 parse failure (Llama DocRED 6.8%→9.1%) 未解释。加说明。
**[M6]** BibTeX 中有 SchemaRL, GUIDEX, DCCD, REBEL 等条目未被引用。要么 cite 要么删除。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：
- MF1: "Ontology" framing overclaim
- MF2: 缺少 ARR checklist
- MF3: WikiEvents preliminary 过高权重
- SF1: "Near-lossless" 需 CF qualifier
- SF2: Dual-factor n=4 claim 过强
- SF3: ZS vs FT 实验空间失衡
- SF4: §7 过短
- SF5: Abstract 数据密度
- SF6: DocRED beam 50 docs
- M1-M6: 全部

---

## Reviewer Divergence

**[DIV1] 新颖性评估（Excitement 3.0 vs 3.5）。**
- R2：核心机制是已有 constrained decoding 范式向 IE 的移植。Grammar layer 完全复用 XGrammar。PLDI 2025 type-constrained codegen 是 "closest mechanistic analog"。Excitement 3.0/5。
- R1 [REBUT]：IE-specific 挑战构成实质贡献——(1) 动态 entity registry（vs 代码生成的静态类型声明）；(2) CF↔DR trade-off 的发现和分析（代码类型系统不存在此问题）；(3) Non-rectangularity 分析在 constrained decoding 文献中属新贡献。Excitement 3.5。
- **Director 判断**：R1 的反驳有理据——IE 的 dynamic registry 和 CF trade-off 确实超越了 engineering adaptation。但 grammar layer 零贡献和 logit masking 机制本身非新也是事实。综合 Excitement 约 3.0-3.5，偏向 3.0（EMNLP 对 novelty 要求较高）。

**[DIV2] 下游评估需求。**
- R2 [Should-Fix]：type safety 论文需 KG/QA 端到端评估。
- R1 [REBUT]：type validity 是 well-defined 形式化目标，独立于下游任务；KG/QA 评估超出合理 scope。
- **Director 判断**：R1 的 scope 论证合理。不将下游评估列为 should-fix，但建议在 Discussion 中 frame 为 future work 并适度调整 §1 对 downstream pipeline 的强调。

---

## Questions（需作者澄清）

**[Q1]** Entity registry 错误传播：如果早期实体类型错误，后续 relation 全部继承。Case Study 4 展示了个案但未系统量化频率和影响。建议提供 "X% of residual DR violations trace to incorrect entity-list type assignments" 的统计。

**[Q2]** 多义类型实体：entity registry 的 first-assignment-wins 策略对同一实体在不同上下文中的合法多义类型过于刚性。是否考虑过 soft registry（多个候选类型 + context-dependent selection）？

**[Q3]** κ(r) = 1 - |σ(r)|/|E|² 对对称关系的归一化是否合适？R1 和 R2 均独立指出。实际影响可能有限但应 acknowledge。

**[Q4]** GoLLIE 在 SciERC 上的残余违约率？如果能对其公开输出做违规检测，一行统计即可证明互补性。

**[Q5]** 约束为何增加 parse failure（Llama DocRED 6.8%→9.1%）？机制未解释。

**[Q6]** WikiEvents Qwen trigger F1 下降 5.4pp 的原因？Trigger extraction 不受 type constraints 影响，下降是否在 noise range 或因 generation trajectory 改变？

---

## Missing References

两位 Reviewer 共同指出以下遗漏（部分已在 bib 中但未 cite）：
- SchemaRL (Lu et al., ACL 2025) — schema-constrained generation via RL
- GUIDEX (De La Fuente et al., ACL 2025 Findings) — zero-shot IE schema-aware 数据增强
- DCCD (Reddy et al., 2026) — draft-conditioned constrained decoding
- REBEL (Cabot & Navigli, EMNLP 2021 Findings) — end-to-end RE
- GPT-RE 或类似 LLM-based RE 近期 benchmark 工作

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目无 `paperreview_ai` 设置）。

---

## Overall Assessment

**Score: 3.0-3.5 (Borderline Findings / Borderline Conference)**

**EMNLP 2026 ARR 评分：3.0 (Findings)**

**Confidence: 4/5**

两位 Reviewer 独立给出 3.5 (Borderline Conference)，交叉分享后维持评分。Director 综合判断偏向 3.0 (Findings)，理由如下：

**偏向 Conference (3.5) 的因素：**
- Fine-tuning 组合性结果有力（DR ≤ 0.20%，R-F1 ± 0.6pp），是一个 solid 的 practical contribution
- 实验设计系统且诚实，CF trade-off 的透明处理值得肯定
- 覆盖 4 模型 × 3 数据集 × 2 任务的全面验证
- Non-rectangularity 和 CF↔DR Pareto 分析是有价值的新发现

**偏向 Findings (3.0) 的因素：**
- 核心新颖性偏增量：grammar layer 零贡献，semantic layer 的 logit masking + entity registry 是已有 constrained decoding 范式的领域适配
- 标题级 framing 问题（"ontology" overclaim）需要修正
- Zero-shot 下总违规改善有限（~30%），CF 引入量大
- WikiEvents 结果 preliminary 但权重过高
- 缺少 ARR checklist（格式硬伤）
- Discussion 过短，缺乏深入洞察

**底线判断**：论文解决了一个真实问题，方法可靠，实验充实。但在 EMNLP 2026 的 novelty 标准下，核心贡献（将 constrained decoding 从 syntax 扩展到 ontology-level type enforcement for IE）更适合 Findings 而非 Main Conference。如果 3 个 Must-Fix 全部修正（framing 校准、checklist 补充、WikiEvents 降级），加上 SF1-SF5 的修改（near-lossless qualifier、FT 叙事主导、Discussion 扩展），论文可以成为一篇 solid Findings paper，有冲击 Borderline Conference 的潜力。

---

## Detailed Comments（逐节）

### Abstract
- 数据密度过高（10+ 数字），精简到 3-4 个。移除 beam/WikiEvents 细节。
- "near-lossless composability" 需限定为 DR+F1 或加 CF qualifier。
- "compiles IE ontology schemas" → 改为更准确的术语。

### §1 Introduction
- Contribution #1: "systematic study" → 改为 "empirical characterization"，dual-factor 降为 observation。
- Contribution #3: 内容过多（RE composability + ZS robustness + beam search），建议拆分。
- Contribution #4: 降级为 exploratory evidence 或移至 Discussion。
- 叙事可以更明确地将 FT composability 定位为核心贡献。

### §2 Background
- 两种约束来源（formal ontology vs empirical extraction）的区分应更突出。
- "We define ontology constraints broadly..." 这句好，但应在 Abstract/标题中也反映。

### §3 Method
- 技术描述清晰，无重大问题。
- Entity registry 的 first-assignment-wins 策略的局限性可在此处提及（目前仅在 §7/Appendix）。

### §4 Constraint Composition
- Constraint tightness §4 定义与 §2 引用存在重复（R9-M3）。
- Dual-factor pattern 措辞需弱化："consistent with" 而非 "predicts"。

### §5 Experiments
- FT composability 应提升为独立 subsection（当前嵌入 §5.1 一个段落）。
- ZS 消融和 cross-model 验证降为 supplementary evidence。
- Table 2: 加 DocRED FT 行，加 bootstrap CI。
- §5.6 beam search: DocRED 50 docs 需显式标注。
- Table 5 WikiEvents grammar-only "---" 需在 caption 解释原因。

### §6 Related Work
- 相比 R9 已显著扩展（3 段），覆盖较全。
- 仍需引用 SchemaRL, GUIDEX, DCCD 等未 cite 条目或从 bib 删除。

### §7 Discussion and Conclusion
- 严重过短。需扩展至包含：supervised SOTA 差距、training-based 方法组合路线图、CF 解决方向、方法适用前提条件。

### Limitations
- 诚实且全面，已有 3 个 \\paragraph 子节。保持。

### Ethics Statement
- 存在但简短。符合基本要求。

### BibTeX
- 14 orphan entries、多个 duplicate keys。提交前清理。