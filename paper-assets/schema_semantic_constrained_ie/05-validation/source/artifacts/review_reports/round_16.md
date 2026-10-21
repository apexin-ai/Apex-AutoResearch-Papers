---
round: 16
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T02:47:38.221158+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 16 审稿报告 — OntoCoDec

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle, Long Paper)
**Reviewer 编排**: R1（方法严谨性 + 实验评估）, R2（新颖性 + 完整性 + 格式合规）
**审稿模式**: Fresh（重新审稿）

---

## Summary

OntoCoDec 提出将 IE 本体编译为两层 token-level 解码约束的框架：grammar layer（context-free，通过 XGrammar 编译 JSON 结构和词汇约束）和 semantic layer（prefix-decidable with state，通过动态 entity registry 和 logit masking 实施 domain/range type constraints）。两层之间存在 enabling dependency（Proposition 1, pumping lemma proof）。框架在 SciERC、DocRED（关系抽取）和 WikiEvents（事件抽取）上用 4 个自回归 LM（7–70B）进行了验证。LoRA 微调下 DR ≤0.09%、CF ≤1.27%；zero-shot DR 降低 45–99%（dataset-dependent）。

---

## Strengths

1. **问题定义清晰，实用价值明确**：IE 中 domain/range violation 是真实存在的系统性问题（baseline 15–18%），论文精确量化了问题规模并提供了可操作的解决方案。[R1, R2 共识]

2. **消融实验设计系统化**：五路消融（unconstrained / grammar-only / semantic-only / S1 / S2）清晰隔离了各层贡献。Enabling dependency 的实验证据（grammar-only 3–24% DR reduction vs. full 94–100%）比理论证明更有说服力。[R1-S2, R2]

3. **DR↔CF trade-off 的诚实和深入分析**：Table 8（Appendix C）展示消除 CF 导致 DR 增加 15.8× 的根本性权衡。定量分析优于多数论文的 "limitations as afterthought" 做法。[R1-S3, R2-S6]

4. **Limitations section 异常全面**：涵盖 CF trade-off、English-only、LoRA-only、WikiEvents small test set、70B INT4 only、tokenizer assumptions、API-only models 排除——几乎预见性地回答了 reviewer 想问的问题。[R2-S3]

5. **统计严谨性**：所有 F1 比较均有 10,000-iteration paired bootstrap，报告 p-values 和 CI。DR reduction 在所有 fine-tuned settings 中均 significant (p&lt;0.001)。[R2-S4]

6. **跨模型/跨 tokenizer 泛化**：在 3 种 tokenizer 架构（byte-level BPE ×2, SentencePiece）和 4 个模型上验证。Appendix 体量大（25 页）且信息密度高，显著提高可复现性。[R1-S4, R1-S5, R2-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, R1+R2 强共识] **缺少与现有 constrained decoding 方法的 head-to-head 实验对比**

Grammar-only ablation 被声称等同于 GCD/BoostCD 的约束类别（§5.1 "implements the same class of constraints"），但未运行任何现有系统的实际代码。BoostCD 的 boosting mechanism（交替 constrained/unconstrained decoding）是其核心贡献，grammar-only ablation 无法代表。IterGen（backtracking-based semantic constraint）和 EnriCo（ASP-based decoding constraints）是 semantic-level 最直接竞品，仅在 Related Work 中讨论。无 head-to-head 对比，无法判断改进来自 semantic layer 创新还是实现差异。

**此问题已连续 5 轮（R12–R16）被标记，是本论文最持久的审稿缺口。**

**MF2** [critical, R2 发现, R1 交叉 AGREE] **Abstract "94–100% DR reduction" 与 Table 2 数据不一致**

Table 2 中 Llama-3.1-8B SciERC fine-tuned DR 从 1.11% 降至 0.09%，相对降幅 = (1.11−0.09)/1.11 = **91.9%**，低于所声称的 94% 下限。四组 fine-tuned 设置实际范围是 **92–100%**，而非 94–100%。这是 Abstract 核心定量 claim，可直接验证，不准确损害可信度。

**MF3** [critical, R1+R2 强共识] **CF 率在 Abstract 中选择性报告**

Abstract "(0–9.9% zero-shot, ≤1.2% fine-tuned; §5.1)" 通过节引用将 CF 范围限定为 SciERC 一个数据集。实际上：
- DocRED zero-shot Llama CF = **12.02%**（Table 4）
- WikiEvents zero-shot CF = **14.9–21.1%**（Table 5）

读者易将 "(0–9.9%)" 误解为全局范围。CF 是本方法的核心 trade-off，不完整披露构成选择性报告，损害 AC/Reviewer 对方法局限性的判断。

---

### Major Issues

**W1** [R1 critical, R2 major, 共识] **κ̄ (constraint tightness) 作为预测指标缺乏统计支撑**

κ̄ 作为 schema 属性仅有 **n=2** 独立取值（SciERC vs DocRED），自由度为零，任何回归分析无意义。线性拟合 R²=0.86 基于 n=4（2 datasets × 2 models, p=0.07）。Per-relation 分析（Appendix N, Table 34）进一步显示 high κ 本身不足以预测 DR reduction（"equal tight relations... show 74.05% DR"）。WikiEvents 有 245 constraints 但未报告 κ̄ 值。尽管如此，κ̄ 在 §1 contribution list、§2 Background、§4 获独立方程编号——prominence 远超证据强度。

**W2** [major, R1+R2 共识] **DocRED zero-shot DR 仅降 45%，与整体 narrative 存在张力**

DocRED zero-shot Full S1: 18.46% → 10.21%，仅 **45%** reduction，远低于 SciERC 94%。§1 contribution item 2 说 "yields 94–100%"，排除了 DocRED 45% 却未说明。详细四类错误分析仅在 Appendix D（entity type errors 39%, schema coverage gaps 33%, incorrect relation selection 17%, direction reversal 11%），主文仅一段简短讨论。

*R1 REBUT R2 关于 "zero-shot 是最核心场景" 的判断，认为 fine-tuned + constrained 是更常见部署模式。Director 判断：两种场景均需讨论，但 §1 contribution 措辞应涵盖两者的实际数据范围。*

**W3** [major, R1+R2 共识] **WikiEvents 20-doc test set 统计功效不足以支撑 "generalization" claim**

20 文档 test set，Clopper-Pearson 95% CI 上界 5.83%。Per-document variance 极高（Arg-F1 std/mean &gt; 0.5, 35–47% documents scoring zero）。§1 contribution 2b "demonstrate generalization to 245 constraints" 的 claim 强度与 evidence 强度不匹配。

**W4** [major, R1 发现, R2 AGREE] **70B 评估过于单薄**

仅 Llama-3.1-70B (AWQ INT4) 推理，无消融、无微调。CF 从 0.07% 飙升至 7.01%，未充分分析（INT4 量化偏移 vs. model scale 效应）。Abstract "7–70B" 范围声明给人不恰当的覆盖印象。应标注为 "feasibility check"。

**W5** [major, Reviewer 分歧] **Proposition 1 / novelty 定位**

R2 认为 cross-field dependencies requiring random-access lookup 超出 PDA 能力是编译原理基本知识（cf. attribute grammars），Proposition 1 应降级为 motivation。R1 partial REBUT：形式化本身有独立价值（将 IE type constraints 具体化为语言识别问题，完整 pumping lemma proof, Appendix O 2 pages），三级约束分类是有用的概念贡献。

Director 判断：Proposition 1 的 formalization 在约束解码文献中有一定新颖性，但 §1 将其作为首要贡献列出的 positioning 偏高。建议重新措辞为 "we formalize a well-known intuition"，以实验验证（grammar-only 24% vs full 94%）作为主要证据。

**W6** [warning, R1 发现] **Proposition 1 的 bounded/unbounded gap**

Proposition 1 对无界实体集成立。对有限实体集，valid language 在技术上是 regular 的（Appendix O, page 33 正确指出），但 DFA 状态数指数增长（SciERC: &gt;10^17 states）使其 "practically infeasible"。这是实际不可行性论证而非形式不可能。此 gap 仅在 Appendix 末尾简短提及，主文 §3 应加一句限定。

---

### Minor Issues

- **M1**: §3.3 "formal guarantees" / "pair-based enforcement" 与 §4 "best-effort" fallback 存在术语张力。"enabling dependency" 非标准形式化概念。建议统一术语。[R2-M4, R1-M1]
- **M2**: §6 Related Work 主文仅 ~1/3 页，三段式引用堆叠，缺乏关键区分点展开。[R2-M3]
- **M3**: Table 3 脚注中 XGrammar 残余 0.03% RV（chimeric values）应说明是否已上报/修复。[R2-M2]
- **M4**: §1 "zero-shot DR drops 76–99% for calibrated models"——Mistral 42% 被排除但 "calibrated models" 条件不够透明。[R2-M6]
- **M5**: `regino2025kgcurator` 和 `formattax2026` 两条引用在 OpenAlex 中未找到匹配，应确认存在。[R2-M5]
- **M6**: DocRED 使用 dev set 的说明应提升到主文实验设置段落。[R1-M2]
- **M7**: Figure 3 per-relation DR rates 仅 Llama-3.1-8B，缺乏跨模型验证。[R1-M3]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成强共识：
1. **缺少 baseline 直接对比** — 最关键实验缺口，连续 5 轮标记
2. **κ̄ 统计支撑不足** — n=2 独立取值，任何回归无意义
3. **Abstract 数字不一致** — "94–100%" 实际为 92–100%
4. **CF 选择性报告** — Abstract 仅覆盖 SciERC，隐藏 DocRED 12% 和 WikiEvents 21%
5. **DocRED 45%** — 与 "near-eliminates" narrative 不一致
6. **WikiEvents 20-doc** — "demonstrate generalization" 措辞过度
7. **70B 单薄** — 无消融/FT，CF 飙升未分析

优势共识：
8. **Ablation 设计系统化** — 五路消融 + enabling dependency 实验验证
9. **Limitations 异常诚实** — 覆盖面全面
10. **统计严谨性** — bootstrap 检验规范

---

## Reviewer Divergence [REBUT]

1. **Proposition 1 定位**：R1 (Excitement 3.5) 认为 pumping lemma proof 在约束解码文献中有独立理论价值；R2 (Excitement 2.5) 认为结论 expected，应作为 motivation 而非 contribution。Director 取中间立场：形式化有一定价值但 §1 positioning 应降低。

2. **Zero-shot 场景重要性**：R2 认为 zero-shot 是 constrained decoding 最核心场景；R1 认为 fine-tuned + constrained 更具部署相关性。Director：两者均需讨论，Abstract/Contribution 应涵盖两种场景的实际数据范围。

3. **整体评分**：R1 = 3.5 (Borderline Conference)，R2 = 3.0 (Findings)。差异主要在 Novelty/Excitement（R1=3.5 vs R2=2.5），Soundness 一致 (3.5/5)。

---

## Questions to Authors

1. Grammar-only ablation 是否使用了与 GCD 完全相同的 XGrammar 配置和 grammar compilation pipeline？实现差异是否可能解释 grammar-only 的低 DR reduction？
2. κ̄ 是否在论文未报告的其他 ontology 上验证过？WikiEvents 的 κ̄ 值是多少？
3. 70B 模型上 CF 飙升至 7.01% 的原因——INT4 量化引入的 token 分布偏移，还是更大模型与约束系统有不同的交互模式？
4. DocRED 残余 DR 中 39% entity type errors，semantic layer 是否可通过更 aggressive masking 减少？
5. 对于有限实体集，DFA 方案在什么规模以下会变得可行？

---

## Missing References

引用基本完整。60 条 bib entries 全部被引用，0 orphan。50 条 OpenAlex 验证通过，2 条因过新未收录（应确认存在），8 条为作者名编码差异（非实质错误）。

可能有价值的补充（非必须）：
- Attribute grammars 经典参考（支撑 Proposition 1 的 "well-known principle" 定位）
- IterGen 的 backtracking 机制与 OntoCoDec fallback 的更深入 Discussion 对比

---

## External Review (Stanford Agentic Reviewer)

**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置，本轮未请求外部审稿。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 8 info, 0 critical）。

**Warnings:**
- Pages 1-2: 连续 2 页纯文本（Intro + Background），首个视觉锚点延迟到 page 3。建议将 Figure 1 提前或加 teaser figure/table
- Pages 5-7: 主文结果全部为 table（5 table + 0 figure），视觉单调。建议将 Appendix 散点图或 beam sweep 图提升到主文
- Page 8: 末页（Related Work + Conclusion）纯文本，无视觉锚点收尾

**Info:**
- Figure 1 组件文字标注偏小（正文字号 60-65%）
- 主文 8 页仅 1 figure，figure:table = 1:5，低于领域平均（2-3 figures）
- Table 26 红/绿颜色编码对色盲不友好
- References 格式统一，Tables 使用 booktabs，质量良好

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | Director |
|------|-----|-----|----------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.5 | 2.5 | **3.0** |
| Reproducibility | 4.0 | 4.0 | **4.0** |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4 | 4 | **4** |

**评分依据**：
- Abstract 中存在可验证的数字不一致（MF2）和选择性报告（MF3），损害 credibility
- 连续 5 轮缺少 baseline 直接对比（MF1）是最关键实验缺口，审稿人无法评估相对贡献
- 算法新颖性有限：两层架构是 XGrammar（off-the-shelf）+ entity registry（dict + lookup + masking）的领域迁移组合
- κ̄ 作为 contribution 证据不足（n=2 schema）
- 论文的实际价值（解决 IE violation 问题）和工程完整度（ablation + 统计 + 跨模型验证 + 诚实 limitations）适合 Findings 级别

**提升路径 → 3.5 (Borderline Conference)**：
1. 补充至少 GCD 在 SciERC/DocRED 上的 head-to-head 对比（**最关键**）
2. 修正 Abstract 数字（"94-100%" → "92-100%"）和 CF 范围（涵盖全数据集）
3. 将 κ̄ 从 contribution 降级为 diagnostic observation

**提升路径 → 4.0 (Conference)**：
额外需要：BoostCD head-to-head 对比、Proposition 1 更精确的 contribution 定位、§1 contribution 措辞涵盖 DocRED 45% 和 WikiEvents preliminary 性质

---

## Detailed Comments

### §1 Introduction
- "94–100% reduction" → 修正为 "92–100%"（Table 2 Llama-SciERC 91.9%）
- "near-eliminates DR" 应加限定条件并报告全数据集 CF 范围
- Contribution item 2 "yields 94–100%" 排除了 DocRED zero-shot 45%
- "demonstrate generalization" (WikiEvents) → "provide preliminary evidence for"
- "zero-shot DR drops 76–99% for calibrated models" → 明确 "calibrated" 排除条件

### §3 Method
- Proposition 1: 加一句关于有限实体集的限定（technically regular but exponentially large DFA）
- "enabling dependency" 加 "empirical" 限定或改用非误导性术语

### §4 Constraint Composition
- κ̄: 降低 prominence——移出 contribution list，标记为 descriptive hypothesis
- 报告 WikiEvents κ̄ 值

### §5 Experiments
- DocRED 45%: 将 Appendix D 错误分类总结移入主文
- WikiEvents: "demonstrate generalization" → "preliminary/pilot"
- 70B: 标注为 "feasibility check"，分析 CF 飙升原因
- **补充 GCD head-to-head**（至少 SciERC）

### §7 Conclusion
- CF 范围应覆盖全数据集（0–21.1% zero-shot, dataset-dependent）
- "near-eliminates" 需限定为 fine-tuned setting