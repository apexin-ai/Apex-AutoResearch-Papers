---
round: 11
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T08:56:45.147858+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11 (Fresh Review)

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May cycle
**Deadline**: 2026-05-25
**审稿模式**: Fresh（独立初审）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计声明; R2: 新颖性+完整性+写作质量+格式合规）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

OntoCoDec 将 IE schema 编译为两层 token-level 解码约束：grammar 层（基于 XGrammar）保证 JSON 结构有效性和词表成员资格，semantic 层通过 stateful entity registry 和动态 logit masking 执行 domain/range 类型约束。论文在 3 个数据集（SciERC, DocRED, WikiEvents）、4 个模型（8B-70B）、3 种解码策略上评估，展示了 LoRA+S1 配置下 DR≤0.20%、R-F1 ±0.6pp 的 composability 结果。Zero-shot 评估作为 stress test 展示了 76-99% 的 DR 降低（calibrated models），但伴随显著的 CF 上升（最高 12%）。

---

## Strengths

**S1. [共识] 实验评估全面且诚实。** 3 数据集 × 4 模型 × 3 解码策略 × zero-shot/fine-tuned 两种 regime，配合 bootstrap 显著性检验（10,000 iterations），实验覆盖度远超同类工作。Mistral boundary condition 分析（§5.3）、CF-DR pilot ablation（Appendix B Table 5）、residual DR 四类 root cause 分解、Case Study 4 失败案例展示了罕见的科学诚实度。[R1: S3/S4; R2: S1]

**S2. [共识] 两层架构的 enabling dependency 经实验有力验证。** Table 1 消融：semantic-only 仅降 DR 24%，加入 grammar 层后降至 94%。Fine-tuning 后 grammar 层成为 no-op，semantic 层独立贡献 39-72% DR reduction（Table 2, Appendix B Table 8）。Sequential pair-based enforcement 的等价性论证（§3.1 脚注: 33-37% spurious pairs avoided）严谨。[R1: S2; R2: S4]

**S3. [共识] 问题定义精确且实用。** DR/RV/ET/CF 四类 violation 分类是功能性的，每类对应不同 enforcement 机制。Violation landscape 的实证分析为评估提供了可靠基线。[R1: S1]

**S4. [共识] 工程贡献扎实、部署配置实用。** Tokenizer-agnostic continuation masking（§3.2, 覆盖 3 种 tokenizer 家族）、beam search 适配（125 行）、runtime overhead 2-13%。LoRA+S1 推荐配置（DR≤0.20%, +10% latency）具有明确的部署价值。[R1: S5; R2: S3]

**S5. [共识] Constraint tightness (κ) 分析有价值。** 将违规率与 schema 结构量化关联，提供可解释的分析框架。Per-relation 分析（Appendix C）展示了 tightness 与残余 DR 的一致性。[R2: S2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [共识, critical] "Near-lossless" 叙事未充分呈现 CF trade-off。**

Abstract 声称 "near-lossless DR composability: DR≤0.20% with R-F1 within ±0.6pp, CF≤1.2%"，但这仅限 LoRA+S1 配置。Zero-shot 下 CF 从 0.08% 飙升至 9.90%（SciERC）和 12.02%（Llama DocRED）。Total violation burden (DR+CF) 在 SciERC zero-shot 下仅从 15.45% 降至 10.83%（**降幅仅 30%**），远低于 DR 单独的 94%。Table 1 自己定义了 "Tot. = DR + CF" 并加粗标记，但正文叙事未以此为主线。

即使在推荐配置 LoRA+S1 下，total burden 改善有限：Qwen SciERC 1.95%→1.18%（-0.77pp），Llama DocRED 0.49%→0.46%（**-0.03pp**）。Appendix B Table 5 的 pilot ablation 证明 CF↔DR 是结构性不可调和的 trade-off。

**要求**：(1) Abstract 和 Introduction 中明确 "near-lossless" 仅指 LoRA+S1 下的 DR；(2) 将 total violation burden (DR+CF) 作为核心报告指标；(3) 将正文叙事主线调整为 LoRA+S1，zero-shot 降级为 diagnostic/stress-test。

[R1-N1 + R2-N2, full consensus]

**MF2. [共识, critical] 缺少与 schema-aware IE 系统（GoLLIE 等）的 violation rate 直接对比。**

论文在 §6 声称与 GoLLIE "complementary"（"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations"），但实验部分完全没有与 GoLLIE、KnowCoder、GenIE 等系统比较 violation rates。当前 baseline 全部是内部 ablation 变体（unconstrained/grammar-only/semantic-only/post-hoc filtering），无外部竞争方法。GoLLIE 代码和模型公开可用，这一缺失难以辩护。

如果 GoLLIE 的 violation rate 已经很低，OntoCoDec 的增量价值需要重新评估；如果 GoLLIE+OntoCoDec 展示显著边际贡献，则 "complementary" claim 获得实证支撑。

**要求**：至少以下之一：(1) GoLLIE 在 SciERC 上的 violation rate 对比实验；(2) 引用其论文中报告的 schema compliance 数据作为参照；(3) 明确论证不可比性原因。

[R1-N2 + R2-W2, full consensus]

### Should-Fix（影响评分但不一票否决）

**SF1. [共识, warning] Dual-factor pattern 仅 n=4, p≈0.058，正文措辞超出统计证据。**

Linear regression（residual DR vs κ̄ × RV_baseline）仅 n=4 数据点（calibrated models），df=2，p≈0.058（不显著）。论文在 Appendix B 标注 "descriptive characterization"，但正文 §4 使用 "consistent with" 和 "supports" 等暗示因果性的措辞，并将此 pattern 作为全文核心解释框架（§1, §4, §5.2, §5.4）。

**建议**：弱化正文措辞（加 n 限定），或增加 model×dataset 数据点。

[R1-W1 + R2-W3, full consensus]

**SF2. [共识, warning] WikiEvents "preliminary" 限定不足。**

20-document test set（数据集本身限制），trigger F1 CI 极宽（-5.4/-0.6pp），但 Abstract line 10 "The framework extends to event extraction without modification" 缺乏 "preliminary" 限定。§5.4 标题 "Preliminary Extension" 是好的，但 Abstract 和 Contribution 列表的表述 confidence 偏高。

**建议**：Abstract 和 Contribution 3 加 "preliminary" 限定词；§5.4 首段显式说明样本量限制。

[R1-W2 + R2-W4, full consensus]

**SF3. [共识, warning] Zero-shot 占正文~40% 篇幅但 R-F1 仅 2-8%，比例失衡。**

正文核心篇幅围绕 zero-shot（§5.1-5.3），但 R-F1 仅 2-8%。论文的辩护（ZS 是 stress test）出现在附录而非正文。推荐配置 LoRA+S1（R-F1 40-46，Table 2）反而篇幅不足。

**建议**：§5 开头加 framing paragraph 明确 ZS 为 diagnostic；扩展 fine-tuning composability 讨论篇幅。

[R2-W1 + R1 cross AGREE]

**SF4. [共识, warning] Beam search DocRED 仅 50-doc subset，推广性受限。**

SciERC beam search 评估了全量 551 docs，但 DocRED 仅 50 docs（Table 8 caption）。Clopper-Pearson 95% CI 上界 5.8%，50→998 docs 的推广性未讨论。

**建议**：正文标注 subset 限制；解释未跑全量原因；讨论推广性。

[R1-W3 + R2 cross AGREE]

**SF5. [共识, warning] Abstract 数字密度过高（~15 个数字）。**

审稿人在 30 秒内无法消化。核心 message 被数据淹没。R1 部分反驳（实证论文需数字支撑），但同意可精简 2-3 个。

**建议**：保留 3-4 个关键数字（DR≤0.20%, ±0.6pp, 76-99%, CF≤1.2%），其余移至正文。

[R2-W5, partial consensus]

**SF6. [共识, warning] Entity registry 字段顺序依赖未显式讨论。**

Semantic layer 依赖固定字段顺序（head→tail→relation→head_type→tail_type），通过 JSON Schema 强制。但：(1) 这一架构约束的强制机制（JSON Schema + XGrammar 编译）未显式说明；(2) Relation 引用未知实体时 fallback 退化为粗粒度 domain-only 约束，其对 CF 的影响未讨论。

**建议**：§3.1 或 §3.2 加 1-2 句说明。

[R2-W6 + R1 cross AGREE]

### Minor（不影响接收）

| ID | 问题 | 共识 |
|----|------|------|
| M1 | BibTeX 10 个 orphan entries + 1 duplicate key（schall2025hiddencost） | 共识 |
| M2 | Compile time 不一致（§5 "44ms" vs Appendix B "0.044s" vs Appendix K "0.33s"） | 共识 |
| M3 | WikiEvents 文档数不一致（Checklist 246 vs split 194+20+20=234） | 共识 |
| M4 | §2 P(E×E) 幂集符号 P 未定义 | 共识 |
| M5 | DocRED dev set：§5 脚注有说明但 Table 2 caption 未标注 | 共识 |
| M6 | Table 1 caption 未定义 S1/S2 | 共识 |
| M7 | "Training-free" 措辞与推荐配置（LoRA+S1 需 fine-tuning）可能误导；建议加明确区分 | R2 raised, R1 partial agree |
| M8 | Table 2 DocRED grammar-only DR 上升至 26.17% (counter-intuitive) 需 caption 加注 | 共识 |

---

## Reviewer Consensus

以下问题两位 Reviewer 完全达成共识：

1. **[AGREE] CF trade-off 是核心叙事缺陷** — Abstract 和 Introduction 的 "near-lossless" framing 需修正，total violation burden (DR+CF) 应成为核心指标。[MF1]
2. **[AGREE] 缺少 schema-aware IE 系统 baseline** — GoLLIE 对比是最自然的缺失实验。[MF2]
3. **[AGREE] Dual-factor 统计不足** — n=4, p≈0.058，正文措辞需弱化。[SF1]
4. **[AGREE] WikiEvents preliminary 限定不足** — Abstract 和 Contribution 需加限定词。[SF2]
5. **[AGREE] 正文 ZS/FT 比例失衡** — ZS ~40% 篇幅 vs R-F1 2-8%，推荐配置 LoRA+S1 篇幅不足。[SF3]
6. **[AGREE] Beam search DocRED 50-doc 限制** — 需标注和讨论推广性。[SF4]
7. **[AGREE] 实验评估全面且诚实** — 这是论文最强维度。[S1]
8. **[AGREE] Enabling dependency 消融验证有力** — Table 1 的层间贡献分析清晰。[S2]

---

## Reviewer Divergence

**[DIV1] 技术新颖性评估**

- **R1 (Excitement 3/5)**: Sequential pair-based enforcement 的正确性论证、enabling dependency 的形式化验证、continuation masking 的跨 tokenizer 方案超越了纯工程范畴。论文贡献是 "methods + empirical analysis" 的组合，在 *ACL 中是 3/5 Excitement 的典型水平。将 R2-N1 评为 Should-Fix 而非 Must-Fix。建议定位为 "methods-informed empirical study"。
- **R2 (Excitement 2.5/5)**: Grammar 层完全复用 XGrammar，semantic 层的 entity registry + dynamic masking 在概念上是字典查找+条件过滤，主要复杂性在工程而非算法。"设计合理"和"有新颖性"是不同维度。Findings track 正是为 "technically sound, practically valuable, but incrementally novel" 的工作设计。
- **交叉后结果**: 双方维持各自立场。R2 表示如果 GoLLIE baseline 展示显著 incremental value，愿意上调至 3.5。

---

## Questions to Authors

**Q1.** 在 LoRA+S1 推荐配置下，所有 model×dataset 配置的 total violation burden (DR+CF) 净变化数据是多少？目前可计算的数据显示 Llama DocRED 净减仅 0.03pp。

**Q2.** 为什么不比较 GoLLIE 或类似 schema-aware 系统的 violation rates？GoLLIE 代码公开可用，即使 F1 不直接可比，violation rates 应可在相同数据集上测量。

**Q3.** Entity registry 如何处理 relation 中首次出现、entity list 中未生成的实体？当前 fallback（退化为 dom(r) 全集约束）是否导致 pair-based enforcement 退化为粗粒度 domain-only？

**Q4.** Beam search 在 DocRED 全量 998 docs 上的结果是什么？50-doc subset 的 DR=0% 是否可推广？

**Q5.** Constraint tightness κ(r) 的 dual-factor 分析能否通过增加更多 model×dataset 数据点（如 WikiEvents、70B 模型）来增强统计效力？

---

## Missing References

1. **TANL** (Paolini et al., 2021) — 已在 .bib 但未引用。Structured prediction as text generation 的早期工作，应在 §6 引用。[共识]
2. **Wadhwa et al. (2023)** — 已引用但未用其 violation rate 数据作为 external baseline 参照点。[共识]
3. **GenIE** (Josifoski et al., 2022) — 已在 Appendix A 引用但主体实验未比较。[R1]
4. **BoostCD** (Sakota et al., 2025) — 已在 §6 引用但无实验对比。R1 认为设计哲学不同，可比性有限。[R2, R1 partial rebut]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 config 中 `external_review.paperreview_ai.enabled` 未启用），跳过。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Reviewer 评分分布**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)

**评分依据**:

论文解决了一个清晰且实际的问题（LLM IE 中的 type violation），提供了同类工作中最全面的实验验证，科学诚实度高。LoRA+S1 推荐配置具有明确的部署价值。

但以下因素将评分限制在 Findings 档位：

1. **CF trade-off 削弱核心叙事 [MF1]**: "Near-lossless" claim 在 zero-shot 下被 CF 副作用显著抵消（total violation burden 仅降 30%）。即使在推荐配置下，部分 model×dataset 的 total burden 改善极小（Llama DocRED -0.03pp）。这不是方法的根本缺陷（beam search 可解决，fine-tuning 大幅缓解），但 Abstract 和 Introduction 的叙事需要更诚实的重构。

2. **缺少外部 baseline [MF2]**: 仅与内部 ablation 变体比较，无法判断相对 GoLLIE 等 schema-aware 系统的实际增量。这是可修复的缺失，但在当前状态下显著降低了贡献可信度。

3. **技术新颖性有限 [DIV1]**: Grammar 层复用 XGrammar，semantic 层的核心操作（字典查找+条件 masking）概念直接。R1 认为 formalization + systematic analysis 组合足以支撑 Borderline Conference；R2 认为主要贡献是工程适配。Director 判断：论文的贡献介于方法论创新和工程框架之间，更接近后者。Findings track 是合适的定位。

**上调条件**: 如果作者能 (1) 重构 CF 叙事使 total violation burden 成为核心指标，(2) 补充 GoLLIE violation rate 对比并展示显著边际贡献，评分有潜力提升至 3.5 (Borderline Conference)。R2 明确表示在 GoLLIE baseline 证据充分时愿意上调。

**置信度**: 4/5（两位 Reviewer 均熟悉 constrained decoding 和 IE 领域，交叉讨论充分）

---

## Detailed Comments

### §1 Introduction
- Contribution 3 中 "extends to event extraction without modification" 缺 "preliminary" 限定。
- "near-lossless composability" 需限定为 "near-lossless DR composability under fine-tuning"，并在 contribution 列表中纳入 CF trade-off 作为 honest limitation。
- 最后一句 "training-free" 与推荐配置（需 LoRA）存在潜在误导，建议区分。

### §2 Background
- P(E×E) 的 P（幂集）未定义。
- 建议加注 entity list 在 relation list 之前生成的宏观顺序假设。

### §3 Method
- §3.1 字段顺序强制机制需显式说明（JSON Schema + XGrammar 编译如何保证）。
- §3.2 relation 引用未知实体时的 fallback 行为（退化为 domain-only）及其对 CF 的影响值得讨论。
- Continuation masking 的设计是亮点，但应在正文提及 Qwen vs Llama 的 semantic coverage 差异（100% vs 63.4%）。

### §4 Constraint Composition
- Dual-factor pattern 的正文措辞需弱化，加 n=4 限定。
- κ(r) symmetric relation 脚注已添加（R10 遗留），确认。

### §5 Experiments
- 需在 §5 开头加 framing paragraph，明确 ZS 为 diagnostic、FT 为 deployment 主线。
- Table 1 caption 需定义 S1/S2。
- Table 2 caption 需标注 DocRED 为 dev set；grammar-only DR 上升需加注。
- Beam search DocRED 50-doc 限制需正文标注。
- WikiEvents 文档数 246 vs 234 需核实统一。
- Compile time 不一致（44ms vs 0.044s vs 0.33s）需统一。

### §6 Related Work
- GoLLIE "complementary" claim 需实验支撑。
- 引用 TANL（已在 .bib 但未 cite）。
- BibTeX 清理：10 个 orphan entries + 1 duplicate key。

### §7 Discussion and Conclusion
- 已比 R10 改善。建议加入 total violation burden (DR+CF) 作为核心讨论指标。

### Limitations
- 覆盖全面（constraint scope, evaluation coverage, engineering considerations），是论文亮点。
- 建议补充：empirically derived constraints 继承训练数据偏差/覆盖率不足的风险。

### Checklist
- 填写质量良好。WikiEvents 文档数需核实（B6: 246 vs split sum 234）。
