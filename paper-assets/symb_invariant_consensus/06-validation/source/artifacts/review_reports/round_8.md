---
round: 8
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T08:03:10.601697+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 11 审稿报告（Fresh Review）

**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验可靠性; R2: 新颖性+完整性+写作质量）
**流程**: Round 1 独立审稿 → 交叉分享 → 逐条 AGREE/REBUT → 收敛（1轮达成）

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束、通过加权部分 MAX-SAT 聚合答案。在 6 个开源 LLM（7B-32B）、3 个逻辑推理数据集、3,000+ 条件评估上，作者发现自提取符号约束在任何已测试的模型能力水平上都无法改进 Self-Consistency。论文识别了"Symbolic Confirmation Bias"（BR=4.97×）和 process-level independence bottleneck（CoT cosine similarity 0.69 >> answer κ 0.46），证明 27 种 same-model remediation 策略全部失败。Oracle 控制实验确认聚合机制本身有效（+29.90pp, +14.22pp），瓶颈在 self-extraction 质量。Cross-architecture NLI 验证在 verifier 能力超过 generator 时产生显著增益（Mistral-7B +6.67pp, p<0.001），DRC 路由方法在 39% 成本下恢复 90% 增益。

---

## Strengths

1. **实验设计的系统性前所未有**：6 models × 3 datasets × 27 strategies × oracle controls × cross-arch escape × 4-seed replication，覆盖面远超同类工作。穷举式搜索有效排除了"只是没找到正确配置"的反驳。
2. **统计方法论在 NLP 实证研究中属上乘**：McNemar + BH FDR + TOST 等价性检验 + Bootstrap CI + Power analysis 构成完整统计推断链。TOST 的使用（区分"无效果证据"和"证据不足"）值得肯定。
3. **Oracle 控制实验设计精妙**：FOLIO gold annotations + ProofWriter DSL 作为 oracle constraints，干净隔离了 extraction quality 和 aggregation mechanism，是论文最强的方法论贡献。
4. **"Symbolic Mirage" 概念框架完整**：包含三个可测试预测（BR>1 跨架构、same-model 无法突破 BR<1、only external verification escapes），全部被数据确认。
5. **K_eff 和 BR 诊断指标有方法论可复用价值**：将 Kish design effect 引入 LLM 投票分析，为社区提供了量化 same-model 独立性的工具。
6. **Case studies（Appendix G）提供机制性理解**：三个 discordant case 超越统计汇总数字。
7. **诚实的负面结果报告**：未为"正面故事"隐瞒负面发现，学术诚信值得肯定。
8. **Comprehensive appendix**：14 页附录含 prompt templates、pseudocode、ablation、error analysis，reproducibility 条件好。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical, consensus AGREE] **Spearman ρ=1.0 (n=6) 被过度使用，统计基础不足以承受论证权重**
- 6 个数据点中 4 个共享 DeBERTa verifier，违反 permutation test 的交换性假设，有效自由度仅 2-3。然而 "strongly monotonic ρ=1.0, p=0.003" 在论文中重复至少 7 次（Abstract, Introduction Contribution 2, Section 3.3, Section 6, Discussion×2, Conclusion）。这是论文从负面结果转向正面贡献的关键桥梁——如果统计基础不牢固，论文退化为纯粹的负面结果论文。
- **建议**：(1) 降级为 "consistent with a monotonic trend"；(2) 减少重复至 ≤3 次；(3) 增加 non-DeBERTa verifier；(4) 添加讨论 shared-verifier 对 p 值有效性的影响。

**N2** [critical, consensus AGREE] **中心 claim 强度超出统计证据——标题和 Abstract 需限定范围**
- Abstract "do not improve majority voting at any capability level" 在 10/16 条件 underpowered（观测功效 <21%）的情况下是过强的否定命题。TOST 方法论本身是正确的（4 条件等价 + 2 条件负面 = 6/16 有实质证据），但措辞未反映 10/16 条件的 inconclusive 状态。同时标题未限定模型规模（仅测 7B-32B），而约束提取质量可能随规模提升。
- **建议**：(1) Abstract 改为 "we find no evidence of improvement, with equivalence established in four conditions and significant degradation in two"；(2) 标题加限定（如 "at the 7B-32B Scale"）。

**N3** [critical, consensus AGREE] **TOST ±2pp 等价性 margin 缺乏 principled 论证**
- 跨 39-86% SC baseline 使用固定绝对 margin 不合理（39% baseline 的 2pp ≈5% relative vs 86% baseline 的 2pp ≈2.3% relative）。Sensitivity analysis（±1pp → 0 等价, ±3pp → 10 等价）显示等价结论对 margin 高度敏感。Lakens (2017) 要求基于 SESOI 的领域论证，论文未提供。
- **建议**：(1) 提供 margin 的 principled justification；(2) 考虑 relative margin（如 baseline 的 ±5%）；(3) 正文报告 sensitivity 结果。

### Should-Fix（影响评分但不一票否决）

**W1** [warning, consensus AGREE] **Proposition 1 / Observation 2 伪形式化——empirical claim dressed as math**
- "Bound 1" 中 "≲" 未定义，无证明推导；"Observation 2" 基于 n=6 经验观察但用了数学命题格式。建议改用 "Empirical Finding" 或 "Observation"，去除数学化包装。

**W2** [warning, consensus AGREE] **DRC 评估不充分——不足以作为 Contribution 4**
- 仅在 ProofWriter 上完整评估；τ=0.7 在 evaluation set 上选择（过拟合风险）；3 个 verifier 全是 encoder-only MNLI-finetuned；未与 multi-agent debate 等方法对比。建议降级为 proof-of-concept 或增加 cross-dataset validation。

**W3** [warning, consensus AGREE] **Single-seed 变异性与统计可靠性问题叠加**
- 4-seed 复现 Δ 从 +3.43 到 -0.49pp（range ≈4pp），完全覆盖 TOST ±2pp margin。多数条件 single-seed，Δ 可信度存疑。Single-seed + underpowered + margin-sensitive TOST 构成系统性可靠性风险。

**W4** [warning, 分歧 — R2 critical / R1 rebut] **核心负面结果的增量新颖性定位需改善**
- R2 认为 SCB 可从 Huang/Stechly/Wan/Amonkar/Chan 组合预测；R1 反驳称 formal channel (Z3) failure 是 genuine surprise——99% 约束语法合法但语义偏差，与 NL self-correction 失败是不同 failure mode。双方共识：论文应在 Introduction 中更早、更明确地建立 formal channel 的额外假设和区分。

**W5** [warning, 分歧 — R2 critical / R1 rebut] **Independence-Accuracy Trade-off 与经典 ensemble dilemma 的区分**
- R2 认为是 Krogh/Brown diversity-accuracy dilemma 的 CJT 语言重述；R1 认为 CJT 提供了 LLM-specific 量化工具（K_eff, BR, C_0）。双方共识：应明确声明贡献在于量化而非发现新 tradeoff。

**W6** [warning, consensus partial] **BR 指标的循环论证倾向**
- R1 指出 "模型错时约束也错" 是 self-extraction 的定义性结果。R2 反驳称 magnitude (4.97×) 和 per-condition variation 有价值。共识：应定位为 "quantification of expected phenomenon" 而非 "discovery"，减少 BR=4.97× 的重复频次。

**W7** [warning, consensus partial] **术语品牌化过度——"Independence Bottleneck" 接近 rebranding**
- R2 认为所有品牌化术语过多；R1 认为 "Symbolic Mirage"（有3个可测试预测）命名合理，但 "Independence Bottleneck" 确实是 Ladha (1992) correlated voting 的 rebranding。建议保留核心术语，降低次要术语的品牌化。

**W8** [warning, R2 raised, R1 conditional agree] **Related Work 遗漏引用**
- Byerly & Khashabi (2026 TACL) "Self-Consistency Falls Short!" 和 arxiv 2506.07962 "Correlated Errors in Large Language Models" 高度相关但未引用。Related Work 部分段落以 citation listing 为主，缺乏 critical discussion。

**W9** [warning, R1 raised, R2 partial rebut] **27 策略计数膨胀 + 未尝试 trained extractor**
- 含超参变体（T=0.3/0.5/0.7/1.0）和 n≤60 条件。R2 反驳称穷举论证仍成立。但双方同意 trained constraint extractor（如在 oracle annotations 上 SFT）是重要实验空白，应在 Discussion 中讨论。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致 [AGREE]：

1. ρ=1.0 (n=6) 被过度使用，需降级描述并减少重复 [N1]
2. 标题/Abstract 需限定模型规模（7B-32B）[N2]
3. Abstract 措辞 "do not improve at any capability level" 过强 [N2]
4. TOST ±2pp margin 需 principled justification 和 sensitivity 分析 [N3]
5. DRC 评估不足（τ 过拟合、范围窄）[W2]
6. Single-seed 变异性构成系统性可靠性风险 [W3]
7. Proposition/Bound 应降级为 Empirical Finding [W1]
8. SCB 与 CoT confirmation bias 的区分应在 Introduction 前移 [W4]
9. 应声明 Independence-Accuracy Trade-off 贡献在量化而非发现 [W5]

---

## Reviewer Divergence

以下问题存在分歧（未完全调和但可记录）：

1. **新颖性评价**（R1: 3.5 Excitement vs R2: 2.5 Excitement）
   - R2：核心负面发现可从先验工作组合预测，增量有限
   - R1：formal channel (Z3) failure 是 genuine surprise——与 NL self-correction 是不同 failure mode
   - 调和方向：论文需更早、更清晰地建立 formal channel 的额外假设

2. **BR 指标价值**（R1: tautological tendency vs R2: magnitude matters）
   - 调和方向：定位为 quantification 而非 discovery

3. **27 策略计数**（R1: 膨胀 vs R2: 穷举仍成立）
   - 调和方向：区分 principled 和 exploratory，但补充 trained extractors 讨论

---

## Questions（需作者澄清）

1. 用 relative TOST margin（如 baseline 的 ±5%）替代 absolute ±2pp，等价/underpowered/different 的分类如何变化？
2. 是否考虑过 trained constraint extractor（如在 FOLIO/ProofWriter oracle annotations 上 SFT）？这是打破 self-extraction 瓶颈的最自然路径。
3. 仅用 3 个独立 verifier（collapsing 4 DeBERTa pairs into 1）时，permutation test p 值是多少？
4. 在 70B+ 模型上，BR 是否可能跨越 BR<1.0 阈值？论文数据显示 BR 随能力下降（4.97× → 3.93× → 2.88×），外推趋势是否有限？
5. Process similarity 用 SBERT 替代 TF-IDF 是否改变 gap 估计？
6. "Symbolic Confirmation Bias" 与 Wan et al. (2025) CoT confirmation bias 在机制上的本质区别是什么？

---

## Missing References

1. **Byerly & Khashabi (2026, TACL)** "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems" — SC 在 long-context 场景失败，互补分析
2. **arxiv 2604.07650 (2026)** "How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles" — LLM 独立性审计框架
3. **arxiv 2506.07962 (2025)** "Correlated Errors in Large Language Models" — LLM 错误相关性分析
4. **arxiv 2510.01499 (2025)** "Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information" — 超越 majority voting 的聚合方法
5. **arxiv 2501.19306 (2025)** "SETS: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling" — Self-verification 在 test-time scaling 中的应用

注：#2 和 #4 可能在本文提交时尚未公开，需核实时间线。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 config 中 external_review 未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（4 warnings, 0 critical, 12 info）。主要发现：

1. **[warning] 主文严重缺乏结果可视化**：~8.5 页主文仅含 1 个 figure（Figure 1 流程图）+ 4 个 table，没有任何结果可视化图。所有结果图（Figure 2-7）全部推至附录 page 23-24。对于实证分析为主的论文，审稿人不会翻到附录去找关键图表。
2. **[warning] Figure 2（27 策略汇总 bar chart）应上提至主文**：这是全文最有冲击力的结果图，但在附录 p.23。建议放入 Section 5.5 或 Discussion。
3. **[warning] Pages 3-5 连续无 display item**：page 3 纯文本（Related Work），page 4 有公式但无 display item，page 5 纯文本。Table 1 直到 page 6 才出现。
4. **[warning] Pages 1-3 视觉锚点不足**：仅 page 2 有 Figure 1，page 1 和 page 3 纯文字。
5. **[info] 附录 page 24 五张图挤在一页**：每张约 1/5 页高，标签在正常距离下可能难辨认。

---

## Overall Assessment

### 评分：3.0 / 5（Findings）

**置信度**：4/5（两位 Reviewer 仔细通读全文及全部附录，对统计方法和领域文献逐项核查）

### 各维度评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

### 评分理由

**支持 Conference (3.5-4.0) 的因素**：
- 实验设计系统性在同类工作中无出其右
- 统计方法论优秀（TOST + McNemar + Bootstrap + Power），在 NLP 社区少见
- Oracle 控制实验干净隔离了 extraction 和 aggregation
- K_eff, BR, C_0 三个诊断指标有方法论可复用价值
- 负面结果的诚实报告有社区价值

**拉低至 Findings (3.0) 的因素**：
- **统计证据与 claim 强度的系统性不匹配**：ρ=1.0 (n=6) 过度使用、TOST margin 无 principled justification、single-seed 高变异、10/16 条件 underpowered——这些问题叠加形成系统性可靠性风险
- **新颖性定位需改善**：formal channel failure 是一个值得报告的发现，但论文未在 Introduction 中及时建立与 NL self-correction 文献的清晰区分，导致贡献被低估
- **标题/Abstract 未限定范围**：7B-32B 的结论被表述为无条件的否定命题
- **DRC 作为唯一 constructive contribution 评估不足**
- **主文缺少结果可视化**（所有关键图在附录）

### 上调路径（→ 3.5 Borderline Conference）

1. **N1**：降级 ρ=1.0 为趋势描述，减少重复，添加 shared-verifier 限制讨论
2. **N2**：标题加限定词，Abstract 措辞校准
3. **N3**：TOST margin 提供 justification + sensitivity 在正文报告
4. **W4**：Introduction 中更早建立 formal channel distinction
5. **W2**：DRC 降级为 proof-of-concept 或增加 cross-dataset validation
6. **VL**：Figure 2 上提至主文

如果以上 6 项全部解决，论文可达到 3.5 (Borderline Conference)。Excitement 的上限受限于负面结果本身的天然约束——即使定位完善，概念新颖性不超过 3.5。

---

## Detailed Comments（逐节）

### Abstract
- 过于密集：10 行含 15+ 数字/统计量，可读性低
- "at any capacity level" 需加 "tested (7B-32B)"
- 关键数字（BR=4.97×, ρ=1.0, +29.90pp, 83.3%）在全文各处重复，冗余感强

### Introduction
- Narrative flow 清晰，从 SC plateau → CJT independence → SICA → failure → escape
- 但 formal channel (Z3) vs NL self-correction 的区分出现太晚（需从 Related Work 末段前移）
- 四个 contributions 中 Contribution 2（Independence-Accuracy Trade-off）应声明为量化而非发现

### Related Work
- 与 SatLM 的对比已有（"provides a natural control"），但部分段落以 citation listing 为主
- 遗漏 Byerly & Khashabi (2026 TACL) 和 arxiv 2506.07962
- SCB vs CoT confirmation bias 区分在此段末尾，建议前移

### Method
- Eq.(1)-(5) 形式化完备，Algorithm 1-2 清晰
- Bound 1 "≲" 未定义，应降级为 Empirical Finding
- C_0 diagnostic 简洁有用

### Experiments
- Table 1 排列合理（按 SC baseline 排序，分 regime）
- 多数条件 single-seed，4-seed 复现显示高变异
- TOST margin sensitivity 应在正文报告

### Analysis
- K_eff, BR, process similarity 三层诊断结构完整
- BR 的 tautological tendency 应在 Discussion 中承认

### Cross-Architecture
- NLI escape 仅在 NLI-shaped tasks（ProofWriter, FOLIO 边缘）有效
- ρ=1.0 需降级，添加 shared-verifier caveat
- DRC τ 需 held-out validation

### Discussion
- 涵盖了 self-verification 泛化、test-time scaling、trained reasoning 三个维度
- 但 ensemble diversity-accuracy 关系的讨论应更明确声明贡献定位

### Limitations
- 覆盖面适当（规模、语言、功效、成本），篇幅合理（~2/3 栏）
- 建议添加 trained extractor 作为未探索方向

### Format Compliance
- 页数合规：正文 ~8 页 + Limitations + References 2 页 + Appendix 14 页
- 使用 \usepackage[review]{acl}，double-blind（author = Anonymous）
- 无自引暴露身份
- 引用格式完整，60 条 bib 条目，0 orphan，0 missing key
