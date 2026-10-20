---
round: 6
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T01:59:54.375917+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 9 (Fresh Review)

**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)
**审稿模式**: Fresh (重新审稿)

---

## Summary

本文研究 SICA（Symbolic Invariant Consensus Aggregation），从 LLM reasoning traces 中自提取逻辑约束并通过 Z3 MAX-SAT 聚合，试图改善 Self-Consistency majority voting。在 6 个模型 (7B-32B)、3 个逻辑推理 domain、3000+ condition-evaluations 上，结论为：self-extracted constraints 因 Symbolic Confirmation Bias（BR=4.97×, 83.3% wrong-supporting rate）无法改善 SC。Oracle controls 证明机制本身有效（FOLIO +29.90pp），瓶颈定位在 self-extraction 质量。27 种 remediation 策略全部失败，cross-architecture NLI verification 提供了建设性的正向方向。

---

## Strengths

**S1. 实验规模和系统性.** 6 个模型（3 model families, 7B-32B）、3 个 domain、3000+ condition-evaluations、~1250 unique instances、4-seed replication。对负面结果论文而言覆盖面出色。[R1, R2 共识]

**S2. Oracle Controls 精准定位瓶颈.** Gold-SICA 在 FOLIO +29.90pp（p < 10⁻¹³）、ProofWriter +11.50pp（p < 10⁻¹⁴），干净地将「机制有效性」与「self-extraction 信号质量」解耦。这是论文最有说服力的实验设计。[R1, R2 共识]

**S3. 25+ Remediation 穷举.** 涵盖 prompt-level、method-level、paradigm-level 共 15 个 family 的 27 种策略，全部 neutral-to-negative。封堵了"只是 prompt 没调好"的反驳空间。[R1, R2 共识]

**S4. 统计方法论透明.** Power analysis 明确指出 underpowered conditions，TOST 等价检验区分三类结论，bootstrap CIs 报告，seed-level 不稳定性如实呈现。[R1, R2 共识]

**S5. 可复用诊断指标.** Effective-K、Bias Ratio、ProcessSim 超越本文语境，可用于任何 trace-aggregation 系统的失败预测。[R1]

**S6. Cross-Architecture Escape.** DeBERTa NLI 在 ProofWriter 上 +3.50pp（BH 校正后 adj p=0.038），3 种 NLI architecture 复现，提供建设性方向。[R1, R2 共识]

**S7. 写作结构清晰.** 论文组织合理，从 CJT 动机 → SICA pipeline → 实验 → 分析 → remediation → cross-arch escape 的叙事逻辑完整。[R2]

**S8. 格式合规.** 8 页正文、匿名化完整、Limitations 位置正确、引用格式规范。[R2 确认]

---

## Weaknesses

### Must-Address（影响整体评估）

**W1 [Warning] 相对于 Huang/Stechly 的增量新颖性不足.** 核心发现（LLM self-extracted verification 无法改善推理）与 Huang et al. (ICLR 2024) 和 Stechly et al. (ICLR 2025) 在概念层面高度一致。三个诊断指标（Eff-K, BR, process-κ）分别是 Kish's design effect、条件概率比、TF-IDF cosine similarity 的直接应用。"Symbolic Mirage" 本质是已知原理在符号约束 domain 的 instantiation。R1 认为 Z3 形式化验证场景的 non-triviality 和 27 种 remediation 穷举超越 prior work，但 R2 认为概念层面的增量不足以支撑 main conference。
- **R1/R2 divergence**: R1=3.5 Borderline Conference vs R2=3.0 Findings
- **Director 裁决**: R2 的判断更有说服力——论文的核心 insight 在 prior work 中已有定性论证，本文的主要贡献在于 domain-specific 的定量验证和穷举分析，这更适合 Findings 定位。

**W2 [Warning] Independence-Accuracy Trade-off 作为第一贡献存在部分同义反复.** Table 2/Figure 7 的 cross-model pattern（弱模型=高独立性+低准确率，强模型=低独立性+高准确率）本质上接近经典 bias-variance tradeoff。27 种 within-model remediation 全部失败增强了 inescapability claim，但 cross-model pattern 本身新颖性有限。双方共识建议将 Symbolic Confirmation Bias 提升为第一贡献。[R1 AGREE, R2 raised]

**W3 [Warning] Table 1 的显著性声称缺少多重比较校正.** 16 个 non-degenerate 条件的 McNemar tests 未做 BH 校正。两个 "significant degradation"（Mistral-7B PW p=0.014, Qwen2.5-14B PW p=0.011）BH 校正后均不再显著。不影响核心负面结论，但 degradation 声称被高估。论文在 NLI 结果中正确使用了 BH（m=12），应统一标准。[R1 raised, R2 AGREE]

**W4 [Warning] κ→Effective-K 映射形式化不足.** Eq.1 的 design-effect 公式源自 Kish (1965) 的 ICC (ρ)，Fleiss' κ 是 chance-corrected 一致性指标，数值范围和统计性质与 ICC 不同。论文仅一句 "qualitative proxy"，但 K_eff 在全文中作为核心诊断指标反复使用（如 "≤1.30 never improves"），超出了 proxy 的定位。[R1 raised, R2 AGREE]

### Should-Fix（投稿前建议修复）

**W5 [Warning] 遗漏关键相关工作.** SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM+SAT solver 且报告正面结果——可与 SICA 负面结果形成 problem-level vs trace-level 对比，强化 Symbolic Mirage 论点。VeriCoT (Nov 2025) 将 CoT 形式化为 FOL 验证。CRITIC (Gou et al., ICLR 2024) 涉及 tool-interactive self-correction。[R2 raised, R1 AGREE]

**W6 [Warning] NLI combo weight parameter w 未交叉验证.** w ∈ {1, 3, 5} 在同一测试集选择和评估。w=5 在 Mistral-7B 上 +10.67pp 但在 LLaMA-3.1-8B 上仅 +1.67pp (n.s.)，表明最优 w 不稳定。PoC 可接受但需声明 w 是 dataset-specific hyperparameter。[R1 raised, R2 AGREE]

**W7 [Warning] Capability Gap Hypothesis sigmoid fit (R²=0.875) 基于 8 个数据点.** 3 参数 sigmoid 拟合 8 个点，adjusted R² 会大幅低于 0.875。Linear R²=0.823 仅低 0.052。Spearman ρ=0.970 更可靠。应改用 rank correlation 作为主要证据，弱化 inflection point 数值声称。[R1 raised, R2 AGREE]

**W8 [Warning] T_ext=0.3 extraction temperature 缺 sensitivity analysis.** 采样 T 和 K 均有 sensitivity 分析，但 extraction——论文认定的核心瓶颈环节——的关键参数仅用单一值。[R1 raised, R2 AGREE via Q2]

**W9 [Warning] Cross-architecture escape 实验规模不足.** 仅一种外部 verifier (DeBERTa NLI)、两个 dataset、三个 generator family。LogiQA 上无效。缺少与 trained verifiers/code-based verification 的对比。论文已定位为 PoC 并在 Limitations 中承认，但短板明显。[R2 raised, R1 AGREE]

### Minor Issues

**W10 [Info] Abstract "sixteen" vs §4.2 "fifteen" 数字不一致.** Table 1 有 16 个 non-degenerate 行，Abstract "sixteen" 正确，§4.2 "fifteen" 为笔误。[R2 raised, R1 confirms]

**W11 [Info] 术语品牌化讨论.** R2 认为 "Symbolic Mirage"、"Symbolic Confirmation Bias"、"capability trap" 对 incremental 负面结果论文而言品牌术语过多。R1 反驳前两者有精确操作定义（Eq.5, §5.2），但同意 "capability trap" 可弱化。[DIVERGENCE — R1 REBUT, R2 raised]

**W12 [Info] σ(c,a) provenance-based 设计未作为 design limitation 讨论.** R1 指出 σ(c,a)=1 iff c 来自产生 answer a 的 trace，这是导致 degeneration 的直接原因，论文未讨论基于 Z3 semantic evaluation 的替代设计。R2 反驳存在循环依赖问题且在 BR=4.97× 下两种 σ 定义结果应趋同。[DIVERGENCE — R1 raised, R2 REBUT]

---

## Reviewer Consensus [AGREE]

1. **Table 1 需要多重比较校正**（W3）—— 不影响核心结论但需统一标准
2. **κ→K_eff 形式化不足**（W4）—— 需要更 rigorous 的论证或 caveat
3. **NLI weight w 未交叉验证**（W6）—— 需声明 dataset-specific
4. **Sigmoid fit 过拟合**（W7）—— 改用 Spearman ρ 作为主要证据
5. **T_ext sensitivity 缺失**（W8）—— 核心瓶颈参数应有消融
6. **遗漏 SatLM/VeriCoT/CRITIC**（W5）—— 必须引用
7. **"fifteen" 笔误**（W10）—— 修正为 "sixteen"
8. **Contribution 排序**（W2）—— Symbolic Confirmation Bias 应为第一贡献
9. **实验覆盖面 + Oracle controls + 25+ remediation 穷举是论文核心优势**（S1-S3）
10. **统计透明度和可复用诊断指标有独立价值**（S4-S5）

## Reviewer Divergence [REBUT remaining]

1. **Novelty 判断**（W1）: R1 认为 Z3 非 triviality + exhaustive remediation 足够 Borderline Conference (3.5)；R2 认为概念层面是 Huang/Stechly instantiation，仅够 Findings (3.0)。Director 倾向 R2 的判断。
2. **术语品牌化**（W11）: R1 认为有操作定义不算品牌化；R2 认为过度。部分共识：前两个可保留，"capability trap" 弱化。
3. **σ(c,a) 设计**（W12）: R1 认为应讨论替代方案；R2 认为循环依赖使替代不可行。

---

## Questions（需要作者澄清）

**Q1.** Table 1 "4s" 标注的确切含义及其对可信度判断的影响？[R1]
**Q2.** MAX-SAT constraint rejection rate 3.4% 的分布——高 rejection 的 cases 是否系统性优于 SC？[R1]
**Q3.** 是否测试过 answer assertion weight = 0 的变体？[R1]
**Q4.** Z3 semantic deduplication (p=0.013) 正面结果为何未在正文中讨论？[R1]
**Q5.** Intermediate-SC regime 的 sweet spot 是否可系统化刻画？[R2]
**Q6.** Partially gold constraints（0%-100% mixing curve）的退化曲线？[R2]

---

## Missing References

1. **SatLM** (Ye et al., NeurIPS 2023) — LLM + SAT solver 正面结果，与 SICA 负面结果形成关键对比
2. **VeriCoT** (arXiv 2511.04662, Nov 2025) — CoT → FOL 验证
3. **CRITIC** (Gou et al., ICLR 2024) — Tool-interactive self-correction

[R2 raised, R1 AGREE]

---

## External Review (Stanford Agentic Reviewer)

未请求。项目未配置 `external_review.paperreview_ai.enabled`。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（4 warning, 14 info, 0 critical）

### Warning 级发现
1. **Pages 1-3 连续 3 页纯文本无 display item.** 第一个视觉锚点（Figure 1 SICA pipeline）直到 page 4 才出现。审稿人在前 2 分钟内只看到密集双栏文字。建议将 Figure 1 提前或加入 teaser figure。
2. **Page 5 纯文本断层.** Experiments 设置部分整页纯文本，与前后 display items 间形成文本断层。
3. **Figure 1 仅占单栏宽度.** 作为论文第一个也是最重要的概念图，视觉冲击力不足。建议改用 figure*（全宽）。
4. **Page 8 内容过度密集.** Figure 3 + Table 3 + Discussion + Conclusion 挤在一页，Conclusion 仅 8-10 行，显得仓促。

### Info 级发现
- 格式整体规范：ACL 匿名提交格式正确，Table 1 全宽 booktabs 风格专业，Algorithm 伪代码可读
- 公式渲染正确，无 LaTeX 错误残留，无 overfull hbox，无 [?] 未解析引用
- Appendix 部分表格字号偏小但可接受

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分依据:**
- **Soundness 3.5/5**: 核心 pipeline 形式化完整，oracle controls 有力。但 Table 1 多重比较未校正、κ→K_eff 映射形式化不足、sigmoid fit 过拟合等统计问题累积削弱"精确定量诊断工具"这一核心卖点的可信度。
- **Excitement 3.0/5**: R1=3.5 vs R2=2.5，Director 取 3.0。核心负面结论（self-verification 无法改善推理）已有 prior work 定性论证。本文的主要贡献在于 domain-specific 定量验证 + 穷举 remediation + 可复用诊断工具，这些在 Findings 级别具有明确价值，但概念层面的增量不足以支撑 main conference。
- **Reproducibility 4.0/5**: 实验参数详尽，承诺发布代码/数据，附录含完整 prompt 和伪代码。

**核心理由:**
1. 论文的实验 thoroughness 和统计透明度值得肯定——6 models × 3 domains × 27 remediation strategies × oracle controls 的规模在负面结果论文中罕见。
2. 但"self-extracted 信号无法改善 self-reasoning"在 Huang (2024) 和 Stechly (2025) 之后已非 surprising。本文的核心贡献是将此结论从 natural-language self-correction 扩展到 formal Z3-checked verification——这是有价值的 domain-specific 验证，但概念跃迁有限。
3. 诊断工具（Eff-K, BR, process-κ）有独立复用价值，但每个工具本身是已有方法的直接应用。
4. 若干统计分析环节（W3, W4, W7）削弱了定量声称的精确度。
5. Cross-architecture escape 是建设性方向但规模有限（W6, W7, W9）。

**Confidence: 4/5**

---

## Detailed Comments（按章节）

### Abstract
- "sixteen non-degenerate conditions" 正确，§4.2 的 "fifteen" 需修正
- 范围界定改善良好（"six open-source LLMs (7B-32B)"），但仍需注意 logical reasoning domains 的局限性
- 关键数字（BR=4.97×, 83.3%, process cosine 0.69 vs κ 0.41）直接给出，信息密度高

### §1 Introduction
- CJT 动机清晰，从理论 gap → 实践问题的叙事逻辑通顺
- 建议更明确论证 Z3 形式化验证场景下测试此结论的 non-triviality（vs Huang/Stechly 的 NL self-correction）
- 三个 contributions 的排列建议调整：Symbolic Confirmation Bias 应为第一贡献

### §2 Related Work
- 覆盖面广（5 个段落），引用规范
- 遗漏 SatLM、VeriCoT、CRITIC 三篇
- Positioning 段的 3 differentiators 需要更有力的 defense

### §3 Background & Setup
- SICA pipeline 形式化完整（Eq.1-5, Algorithm 1-2）
- κ→K_eff 映射需更 rigorous 论证
- Symbolic Mirage Hypothesis 的 3 testable predictions 是好的论文结构

### §4 Experiments
- Table 1 需统一应用 BH 校正
- Oracle controls 是最有说服力的实验

### §5 Analysis
- §5.2 Symbolic Confirmation Bias 是论文最强发现
- §5.3 Process-level Independence 是独特贡献但 TF-IDF metric 有局限
- §5.5 Remediation 穷举极具说服力

### §6 Cross-Architecture PoC
- w 参数需交叉验证或声明 dataset-specific
- Sigmoid fit 应改用 Spearman ρ
- 整体规模有限但作为 PoC 可接受

### §7-8 Discussion/Conclusion
- 对负面结果论文而言偏短（Discussion ~350 words, Conclusion ~220 words），但关键 takeaway 清晰
- Page 8 排版过密

### Limitations
- 位置正确（参考文献前），内容充实
- 建议补充 T_ext sensitivity 缺失的讨论