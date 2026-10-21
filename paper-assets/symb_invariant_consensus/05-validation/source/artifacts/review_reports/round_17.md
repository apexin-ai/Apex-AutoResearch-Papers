---
round: 17
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T19:29:36.914159+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告：Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning

**目标 venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**审稿轮次**: Round 20（fresh 重新审稿）
**Reviewer 编排**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作质量）
**交叉分享**: 完成，两位 Reviewer 均提交逐条 [AGREE]/[REBUT] 回应
**格式检查**: 正文 8 页 ✓ | ACL review 模板 ✓ | Anonymous ✓ | Abstract ~196 词 ✓ | Limitations 在正文 ✓

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought 轨迹中自提取逻辑约束，经 Z3 weighted partial MAX-SAT 聚合答案。核心发现为负面结果：在 6 个模型（7B-32B）、多个推理领域上，SICA 与 Self-Consistency 在 >90% 问题上答案一致，经 BH FDR 校正后无统计显著正向效应。作者将此诊断为 "symbolic confirmation bias"（SCB）——自提取约束系统性追随多数答案（bias ratio 1.66-4.97×，9 models from 7B to frontier）。Observation 1（Argmax Preservation）和 Remark 1（DPI Information Ceiling）提供结构性解释。27 种 training-free 变体均因 independence-accuracy trade-off 失败。Cross-architecture verification（DeBERTa NLI）仅在弱生成器上显著（+6.67 pp, p<0.001）。三个零成本诊断指标（C₀, K_eff, BR）预判失败模式。

---

## Strengths

**S1. 统计方法论严谨性远超同类负面结果论文 [R1, R2 共识]**
McNemar exact test + 10,000 bootstrap CI + BH FDR correction (m=6 confirmatory) + TOST equivalence (±2pp) + power analysis (MDE) + multi-seed replication (3-5 seeds)。区分了 "no effect detected" 和 "equivalence confirmed"，在 NLP 负面结果论文中极为罕见。（§3.2, §4, Table 1, Appendix D-E）

**S2. 失败机制诊断逻辑自洽 [R1, R2 共识]**
SCB 诊断链条完整：BR > 1 → degeneration (|C\|/|C| ≈ 0.034) → argmax preservation → 803/804 agreement (Table 10)。DAG 因果图（Figure 3）直观展示信息瓶颈。Constraint ablation（MAX-SAT vs count-only vs random-weight）令人信服地证明约束未携带超越投票计数的信号。

**S3. 结构性解释超越纯经验观察 [R2 主要, R1 同意]**
Observation 1 + Remark 1 将"self-extraction doesn't work"从经验发现提升为结构性解释——在 self-extraction 范式内，约束无法携带超越 trace 本身的信息。这是对 Huang et al. (2024) 的实质推进：解释了*为什么*即使在 provably sound solver (Z3) 下仍然失败。

**S4. 27 种 remediation 策略的系统性失败 [R1, R2 共识]**
Figure 4 + Table 14 覆盖 prompt-level (9)、method-level (3)、analytical conditions (17)，跨 diverse prompting、iterative refinement、contrastive scoring、atom pipeline、UNSAT filtering 等方向。有力地证明退化是结构性的而非调参问题。

**S5. 诊断框架可操作性强 [R1, R2 共识]**
C₀（multi-candidate rate）、K_eff（effective ensemble size）、BR（bias ratio）三指标零成本可计算（无需 ground truth），Type A/B/C 分类正确预测所有 60 个测试条件的失败模式。为从业者提供 K=12 pilot run 即可判断的 "try before deploy" 工具。（§5.3, Table 5）

**S6. Cross-architecture escape 提供建设性方向 [R1, R2 共识]**
DeBERTa NLI 在 Mistral-7B 上 +6.67 pp (p<0.001)，且 cross-model voting vs cross-architecture NLI 对比（Table cross-model-ablation）区分了 ensemble diversity 和 structural independence。CCR 指标（Appendix C）和 108 种 verifier-generator 组合提供量化框架。

**S7. 写作质量整体良好 [R2 主要, R1 同意]**
叙事从 "symbolic verification should help" → "it doesn't" → "here's why structurally" → "here's how to diagnose/escape" 连贯。Abstract ~196 词符合 EMNLP 限制。Related Work 5 段分类合理（SC/ensemble + neuro-symbolic + CoT bias distinction + test-time compute + training-based）。Limitations 简洁覆盖主要局限。

---

## Weaknesses

### Must-Fix（1 项，Director 综合判定）

**W1. Oracle 实验仅限形式逻辑领域，核心因果主张的外部效度不足 [R1-N1 Must-Fix, R2 AGREE]**
- Oracle control（用 gold DSL/FOL 标注替换自提取约束）仅在 FOLIO 和 ProofWriter 上进行，均为形式逻辑领域。核心因果推断——"瓶颈在自提取质量而非聚合机制本身"——的直接证据领域受限。
- 替代假说未排除：MAX-SAT 对数学推理或常识推理的约束类型可能天然不适用。
- ProofWriter oracle 的 97.14% accuracy 证明了聚合机制在给定好约束时有效，但仅限形式逻辑。
- Section 1 贡献声明暗示跨域通用性，但 oracle 证据不支撑。
- **建议**：(a) Limitations 中明确 oracle 因果推断的域局限性；(b) 论证逻辑推理是 SCB 的 "best-case" domain（constraint formalization 最自然），因此 negative result 具有下界意义；(c) 或在 GSM8K 上构建 partial oracle。

### Should-Fix（6 项）

**W2. Observation 1 的形式化程度与 Abstract/Intro 呈现不匹配 [R1-N2 Must-Fix→Director 降为 Should-Fix, R2 AGREE]**
- 三个退化条件均使用 "≈" 且无误差界。Abstract 称 "The failure is structural (Observation 1)"——"structural" 暗示形式化证明但实际是半形式化经验观察。
- R2 指出论文恰当使用 "Observation" 而非 "Theorem"，条件(i) |C\|/|C| ≤ 0.034 有量化。Director 同意 R2 评估，将此降为 Should-Fix。
- **建议**：Abstract/Intro 使用 "empirically structural" 或 "systematic" 替代 "structural"。

**W3. 新颖性相对于 Huang et al. (2024) 的差异化论述需更锐利 [R2-N2 Must-Fix→Director 降为 Should-Fix, R1 REBUT]**
- 论文多次使用 "extends and formalizes" Huang et al.，给人 "confirmatory study" 印象。
- R1 反驳：论文实际贡献远超 confirmation——完整 formal pipeline (Z3 MAX-SAT) + 27 strategies + escape + diagnostics，Huang et al. 完全没有。问题在 framing 太谦虚而非贡献不足。
- Director 判断：同意 R1。论文实质贡献独立且充分。建议 frame 为 "reveals a deeper structural mechanism that Huang's empirical observation did not explain"，而非 "extends and formalizes"。

**W4. 标题 "No Detectable Improvement" 的 scope 与 cross-architecture 正面结果存在张力 [R2-N1 Must-Fix→Director 降为 Should-Fix, R1 REBUT]**
- R2 担忧读者可能理解为 "symbolic constraints don't help LLM reasoning"。
- R1 反驳：标题限定词 "Self-Extracted Constraints" 已充分区分——cross-architecture escape 的增益来源是外部验证器的独立信号，不是自提取约束。
- Director 判断：同意 R1，标题在技术上精确。但建议在 Abstract 中更早区分 self-extracted vs cross-architecture，减少误读风险。

**W5. Capability-gap pattern 证据基础薄弱 [R1-W2 + R2-W4 共识]**
- 核心单调性主张依赖 n=6 generator-verifier 配对（Spearman ρ=1.0, p=0.003）。
- 108 种 verifier-generator-weight 组合（Figure 8）扩展覆盖面，但核心趋势仍受限。
- 仅弱生成器（SC ≤ 72%）上显著，强生成器 Δ ≤ +0.83 pp 甚至负向。实用价值局限。
- **建议**：增加更多能力梯度生成器，或明确标注为 "preliminary evidence"。

**W6. Remark 1 (DPI bound) 理论贡献有限 [R1-W1 + R2-W1 共识]**
- DPI（I(f(X);Y) ≤ I(X;Y)）是确定性后处理的教科书性质，非 SICA 特有。
- "Information Ceiling" 命名暗示特定理论发现，但实际贡献是识别 M→T→A→C Markov chain 结构。
- **建议**：降低展示权重，将重点放在 "identifying the Markov structure" 上。

**W7. α 系统消融缺失 [R1-Q2 + R2-Q2 共识]**
- Table 11 显示 MAX-SAT vs count-only agreement ≥99% across α ∈ [0.1, 0.9]，但这是 count-only 替换而非移除 answer_assertion。
- α→0 时（完全依赖 Z3 可满足性权重，不用 source-attribution）退化是否减弱？这直接关系到 Observation 1 条件(ii) source-attribution 的必要性。
- **建议**：在 Appendix 中报告 α 的完整消融，特别是 α=0 条件。

### Minor（6 项）

- M1. "pp"（percentage points）未在首次使用时定义 [R2-M1]
- M2. Figure 2 散点图灰度打印可读性可改善（marker shape 差异不足）[R1-M1, R2-M2]
- M3. Figure 4 策略名称文字较密集，部分长文本打印时约 6-7pt [视觉审查 warning]
- M4. Figure 4 四个 category 灰度打印时颜色区分不足 [视觉审查 warning]
- M5. Table 1 脚注符号密度较高（*,†,◦,●），可考虑简化 [R1-M2]
- M6. 匿名 repo 建议——对负面结果论文的复现尤其重要 [R2-M5]

---

## Reviewer Consensus [AGREE]

以下关键问题两位 Reviewer 达成共识：
1. **Oracle 领域覆盖不足**是核心缺陷（R1-N1 ≈ R2-W2 底层关切）
2. **Observation 1 形式化与呈现差距**需要调整措辞（R1-N2, R2 AGREE with nuance）
3. **DPI (Remark 1) 贡献有限**——教科书性质而非特有洞见（R1-W1 = R2-W1）
4. **Capability-gap 证据薄弱** (n=6) + 实用价值局限（仅弱生成器受益）（R1-W2 ≈ R2-W4）
5. **α 消融缺失**——理解 Observation 1 条件(ii) 必要性的关键实验（R1-Q2 = R2-Q2）
6. **统计方法论优秀**——McNemar/TOST/bootstrap/FDR/power analysis 组合在同类论文中罕见（R1-S1 = R2-S1）
7. **诊断框架实用**——C₀/K_eff/BR 零成本指标对从业者立即可部署（R1-S5 = R2-S4）
8. **Overall 3.5/5 完全一致**

## Reviewer Divergence [REBUT]

以下问题存在分歧，由 Director 做出最终判定：

1. **标题 scope（R2-N1）**：R2 列为 Must-Fix，R1 REBUT（"Self-Extracted" 限定词已足够精确）。**Director 判定**：同意 R1，降为 Should-Fix。标题在技术上精确，但建议在 Abstract 中更早区分 self-extracted vs cross-architecture 以减少误读。

2. **新颖性 vs Huang et al.（R2-N2）**：R2 列为 Must-Fix（"extends and formalizes" 弱化贡献），R1 REBUT（贡献远超 confirmatory：formal pipeline + 27 strategies + escape + diagnostics）。**Director 判定**：同意 R1，降为 Should-Fix。实质性贡献充分，framing 调整即可（"reveals structural mechanism" 而非 "extends"）。

3. **前沿模型 full pipeline（R1-W3）**：R1 称前沿模型"未跑 full pipeline"，R2 REBUT（Table 2 显示 gpt-4.1/Gemini-2.5-Pro 在 FOLIO 上运行了完整 SICA pipeline，Δ=0）。**Director 判定**：R2 事实性纠正成立。前沿模型确实跑了 full pipeline（至少在 FOLIO 上），R1 此处有事实错误。合理关切是前沿模型仅在 FOLIO (n=204) 上测试。

4. **数据集范围（R2-W2）**：R2 声称"所有数据集均为形式/逻辑推理"，R1 REBUT（论文包含 GSM8K, AIME, StrategyQA, ARC-Challenge）。**Director 判定**：R1 事实性纠正成立——论文确实包含非逻辑领域数据集，但 confirmatory 分析集中于逻辑领域。底层关切有效但 R2 表述有误。

---

## Questions

**Q1 [R1, R2 共识]**: α=0.5 的选择依据？α 取极端值（0 或 1）时退化程度如何变化？特别是 α→0（完全依赖 Z3 满足性权重，不用 source-attribution）时，SCB 是否减弱？

**Q2 [R2 提出, R1 AGREE]**: 若不用 source-attribution scoring 而用语义相似度评分，Observation 1 是否仍然成立？Source-attribution scoring 是 degeneration 的充分条件还是必要条件？

**Q3 [R1]**: ProofWriter oracle 约束是否经过与自提取约束相同的 Z3 dedup 流程？若未经 dedup，oracle vs. self-extraction 比较可能受 dedup 策略差异混淆。

**Q4 [R1, R2 共识]**: DeBERTa NLI 判断的粒度——constraint 级别还是 trace 级别？这对理解 DeBERTa 如何打破 confirmation bias 至关重要。

**Q5 [R2]**: 是否尝试过 adversarial constraint generation——显式要求模型生成与当前多数答案矛盾的约束？这与 diverse prompting 不同，是显式鼓励反事实推理。

**Q6 [R1]**: 是否考虑过提取 trace 间 disagreement 而非 trace 内约束？若约束捕获 "trace A 与 trace B 在 X 上不一致"，source-attribution coupling 可能被打破。

---

## Missing References

论文整体引用覆盖良好（~48 citations, 5 Related Work 段落）。以下为可选补充：

- **[Optional]** Weng et al. (2023) "Large Language Models are Better Reasoners with Self-Verification" — backward verification 方法与 SICA forward extraction 的对比可在 §2 简要讨论
- R2 建议的 "Li et al. (AAAI 2026) Survey on LLM Symbolic Reasoning" 无法验证真实性（R1 REBUT），不列为推荐引用

**已在论文中引用的关键工作**：Huang et al. (ICLR 2024) ✓, Stechly et al. ✓ (implicitly via Wan et al. 2025 positioning), SatLM ✓, Math-Shepherd ✓, o1/o3 ✓, Dietterich (2000) ✓, Krogh & Vedelsby (1994) ✓

---

## External Review (Stanford Agentic Reviewer)

未配置。项目 config 中无 `external_review.paperreview_ai.enabled` 设置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 3 warning, 26 info）。

**Warnings**:
1. Figure 2 图例文字和标记在单栏宽度下偏小，打印时可能需仔细辨认
2. Figure 4 策略名称 y 轴标签较密集，部分长文本约 6-7pt
3. Figure 4 四个 category 仅靠颜色区分时灰度打印可能难以辨认

**Positive findings**:
- 布局节奏良好：text-figure-table 交替均匀，无连续 2 页纯文本
- 主文 8 页含 4 figures + 3 tables = 7 display items，密度 0.875/页（推荐范围内）
- 所有 figure/table 在首次引用附近出现，无明显 float 漂移
- Page 8 内容填充完整（>90% 利用率），无大面积空白
- 公式渲染正确，编号连续，无 LaTeX 残留错误
- Appendix 18 页（2 Algorithms + ~8 figures + ~30 tables），内容充实

---

## Overall Assessment

**Overall Score**: 3.5 / 5（Borderline Conference）

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 4/5 | 统计方法论扎实，实验覆盖全面。Observation 1 成立且有经验支持，但形式化程度为半形式化观察。Oracle 因果推断领域受限 |
| Excitement | 3/5 | 重要负面结果（关闭 self-extraction + formal verification 路径），诊断框架实用。但核心 insight 在概念上被 Huang et al. 部分预期，constructive contribution 仅限弱生成器 |
| Reproducibility | 4/5 | 超参数完整报告，Appendix A 完整 prompt templates，Algorithm 1-2 伪代码清晰，代码承诺接收后发布 |
| Confidence | 4/5 | 两位 Reviewer 均对 SC、formal verification、LLM reasoning 文献熟悉，仔细阅读全文 28 页 |

**总评**：

这是一篇实验方法论极为严谨的负面结果论文。核心优势在于：(1) 统计论证链的完整性（McNemar + Bootstrap CI + TOST + FDR + Power Analysis）在同类工作中罕见；(2) SCB 的诊断链条逻辑自洽（BR → degeneration → argmax preservation → constraint ablation 803/804 agreement）；(3) 诊断框架（C₀, K_eff, BR）对从业者有直接实用价值。

主要问题：(1) Oracle 因果推断仅限形式逻辑领域，无法排除 MAX-SAT 对其他推理类型天然不适用的替代假说；(2) Observation 1 的 "structural" 呈现超出其半形式化观察的形式化程度；(3) 新颖性 framing（"extends and formalizes" Huang et al.）低估了论文的独立贡献；(4) Cross-architecture escape 的 capability-gap 依赖限制了其一般性。

**建议处理优先级**：
1. [Must-Fix] W1: Oracle 因果推断的域局限性——在 Limitations 中明确标注，或补充非逻辑域 oracle
2. [Should-Fix] W2: Abstract/Intro "structural" 措辞调整
3. [Should-Fix] W3: Novelty framing 从 "extends and formalizes" 改为 "reveals structural mechanism"
4. [Should-Fix] W7: α 系统消融
5. [Should-Fix] W4: Abstract 中更早区分 self-extracted vs cross-architecture
6. [Should-Fix] W5-W6: Capability-gap 标注为 preliminary + DPI 展示权重降低

如果 W1 得到充分解决（哪怕只是在 Limitations 中明确标注域局限性），W2-W3 的 framing 调整完成，本文适合 EMNLP 2026 Findings 发表。如果进一步解决 W5（更多 capability-gap 证据）和 W7（α 消融），可达 Conference 水准。

---

*报告由 Review Director 基于 Reviewer 1（方法严谨性+实验有效性）和 Reviewer 2（新颖性+完整性+写作质量）的独立审稿及交叉回应汇总生成。两位 Reviewer 评分完全一致（3.5/5），核心关切高度重合，分歧仅在严重程度分级上。*
