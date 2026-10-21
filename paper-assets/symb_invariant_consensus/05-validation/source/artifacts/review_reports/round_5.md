---
round: 5
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T20:08:40.344865+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh Review)

**论文**: "Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning"
**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + Related Work + 写作质量)

---

## Summary

本文研究 LLM 自提取的符号约束能否通过 Symbolic Invariant Consensus Aggregation (SICA)——基于 FOL 约束提取和 Z3 weighted partial MAX-SAT——改善 Self-Consistency majority voting。在 6 个模型（7B–32B）、3 个推理域、3000+ 条件评估中，自提取约束未能显著提升准确率。作者将此归因于 "Symbolic Mirage"：自提取约束是模型分布偏差的投射（confirmation bias rate 83.3%, BR ≈ 1.97+），trace 之间的 process-level 相关性（cosine similarity 0.69）远超 answer-level 独立性（κ ≈ 0.41）。25+ 补救策略均失败，揭示持久的 independence-accuracy trade-off。Oracle controls 确认聚合机制 sound（+29.90pp, +14.22pp, +11.50pp），瓶颈在自提取质量。Cross-architecture DeBERTa NLI verifier 在 ProofWriter 上显示初步正向信号。

---

## Strengths

**S1. 实验规模和系统性出色。** 6 模型 × 6 数据集 × 3 推理域覆盖高/中/低 SC 准确率区间，25+ 补救策略的穷举式搜索在负面结果论文中罕见，大幅增强结论可信度。[R1-S2, R1-S6, R2-S2]

**S2. 统计方法论严谨。** TOST 等价性检验（±2pp margin）确认负面结果而非仅依赖 NHST，Bootstrap 95% CI（10,000 resamples）、BH 多重比较校正、统计功效分析均超出 NLP 论文平均水准。[R1-S4, R2-S1]

**S3. Oracle controls 设计巧妙。** Gold FOL oracle 大幅提升性能（Mistral-7B FOLIO +29.90pp, Qwen-14B FOLIO +14.22pp, ProofWriter +11.50pp），精确分离聚合机制（sound）与提取质量（bottleneck）。[R1-S3, R2-S5]

**S4. CJT 框架和量化诊断工具有独立贡献。** Effective-K（§5.1）、Bias Ratio（§3.3）、C_D diagnostic 将 SC 失效模式诊断从定性变为定量，可被后续工作直接复用。[R1-S1, R1-S5, R2-S3]

**S5. Independence-Accuracy Trade-off（Figure 7）是最具洞察力的贡献。** 清晰展示同模型方法的 κ ≈ 0.40–0.47 ceiling，Debate 降 κ 但毁 accuracy，形成 Pareto 关系。[R2-S4]

**S6. 叙事结构完整。** 假设建立 → 主实验否定 → 三重诊断 → 补救失败 → 跨架构出口 → 讨论，逻辑连贯。格式合规：8 页正文、Limitations 完整、双盲匿名、48 条引用。[R2-S6, R2-S7]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. FOL 术语误导，负面结论 scope 不清晰。** [R1-N1 critical, R2 agrees at warning]
论文通篇使用 "first-order logic (FOL) constraints"，但 Limitations（p.21）承认提取结果 "predominantly propositional ground clauses without quantifiers"。数学域 extraction prompt 提取的是 equation/inequality/comparison，无量词。标题使用 "Symbolic Constraints" 无误，但正文大量出现 "FOL constraints" 有术语膨胀。
- **Action**: (1) 统一改为 "symbolic/logical constraints"，仅在 Z3 接口描述中保留 "FOL-style"；(2) 报告含量词约束的比例（按域/模型）；(3) Discussion 讨论真正 FOL 提取是否改变结论。
- **R2 缓解观点**: 命题逻辑 ⊂ FOL，如果更弱形式都失败，更强形式失败可能性只会更大——但这需要在论文中显式论证，不能让读者自己推断。

**W2. Cross-architecture PoC 双重 underpowered。** [R1-N2 critical + R2-W2 warning, 双方交叉确认]
- **生成端**（R1）: 仅 Mistral-7B 一个生成模型，不同模型有 Type A/B/C 不同行为模式。
- **验证端**（R2）: FOLIO +2.94pp (n.s.) vs. ProofWriter SICA 自身 −2.83pp (p=0.014)，两个数据集方向相反。α=3 在 n=204 上有 overfitting 风险。
- **综合**: §6 "confirming the effect is not verifier-specific" 仅基于三个 NLI 架构在同一生成模型上的一致性，不等于跨生成模型一致性。
- **Action**: 至少补一个 Qwen2.5-14B 的 DeBERTa combo 实验（traces 已有）；将 §6 结论 qualify 为 "preliminary signal on Mistral-7B ProofWriter"；讨论 α selection 的 overfitting 风险。

### Should-Fix（提升论文质量）

**W3. 增量新颖性定位需加强。** [R2-W1 warning, R1 partial REBUT — **DIVERGENCE**]
- **R2 立场**: Huang et al. (2024) self-correction failure、Stechly et al. (2025) self-verification limitations、Amonkar et al. (2025) LLM formalization quality、Chan et al. (2026) logical soundness limitations——核心洞察在概念层面已被覆盖。Excitement 2.5/5。
- **R1 立场**: 本文测试了一个更强的假设——FOL + Z3 确定性 solver 能否绕过自然语言 self-correction 的局限。BR/C_D/Eff-K 是新的量化工具，先行工作停留在 "doesn't work"，本文给出 "why, how much, where exactly"。
- **共识**: §2 Related Work 应更明确 position：不是重复 "self-correction fails"，而是 "即便引入确定性形式验证（FOL + Z3），self-extraction 的 confirmation bias 仍然阻断这条路径"。

**W4. Domain + Model 覆盖范围与 Abstract 表述不匹配。** [R1-W3 + R2-W4, 双方共识]
- Abstract "across the full LLM capability range" 仅 7B–32B 开源模型。
- "Three reasoning domains" 中数学域全部 degenerate（SC ≥ 85%），主要结论限于 formal/logical reasoning。
- **Action**: Abstract 修改为 "across a range of open-source LLMs (7B–32B)" + "formal and logical reasoning domains, with exploratory results on mathematical reasoning"。

**W5. Symbolic Confirmation Bias 缺乏与 Turpin et al. (2024) unfaithful CoT 的理论连接。** [R2-W3, R1 agrees]
BR = 1.97 可能是 unfaithful CoT 在 FOL 层面的投射。论文未区分 (a) 模型故意生成支持错误答案的约束 vs. (b) 约束生成与答案生成共享同一 biased representation。
- **Action**: §3.3 增加 Turpin et al. 连接讨论。

**W6. 种子复制 + 统计功效标注不足。** [R1-W1 + R2-W5, 双方共识]
Table 1 大多数条件未标注 seed 数量，7 个条件 n ≤ 60 MDE 极大，未区分 confirmatory vs. exploratory。
- **R2 缓解观点**: TOST 用 per-item paired comparison，统计结论本身 well-powered。但 Table 1 标注仍需改善。
- **Action**: Table 1 增加 seed 列和 powered/exploratory 标注。

**W7. 语义去重缺失 ablation。** [R1-W2 + R2-Q5, 双方共识]
Syntactic dedup 可能系统性放大 verbose traces 权重。论文未报告去重前后约束数量比，未做 Z3 semantic equivalence ablation。
- **Action**: 报告去重统计；讨论影响或做 ablation。

**W8. 约束质量分析仅覆盖单一模型。** [R1-W4, R2 agrees]
Extraction error taxonomy (N=804) 仅 Qwen2.5-14B on FOLIO + ProofWriter。91.8% discriminative rate 在 Type B/C 模型上可能不同。
- **Action**: 扩展到 2-3 个模型，或明确限定 claim scope。

### Nice-to-Have

**W9.** Figure 5（intervention strategies summary）深埋 Appendix p.22，应移入正文——两位 Reviewer + 视觉审查均建议。[R2-W6, R1 agrees]

**W10.** Figure 2 线性回归 R² ≈ 4.4%，需说明 R² 并讨论离群点影响。[R1-W5]

**W11.** 83.3% confirmation bias 是 aggregate 数字，per-model 变异大（69%–94%），主文应报告 breakdown。[R1-Q3]

---

## Reviewer Consensus

以下问题双方达成共识（[AGREE]）：
1. **PoC 不足**: Cross-architecture PoC 在生成端（single model）和验证端（inconsistent datasets）双重 underpowered [R1-N2 + R2-W2]
2. **术语修正**: "FOL constraints" 应改为 "symbolic/logical constraints" [R1-N1 + R2 agrees]
3. **覆盖范围校准**: Abstract 的 domain 和 model claims 需 downscope [R1-W3 + R2-W4]
4. **去重 ablation**: Syntactic-only dedup 需量化影响 [R1-W2 + R2-Q5]
5. **Table 1 标注**: 需区分 powered vs. exploratory conditions [R1-W1 + R2-W5]
6. **Missing refs**: Weng et al. (2023) 和 Madaan et al. (2023) 应引用 [R1 + R2]
7. **Figure 5 提升**: 应从 Appendix 移入正文 [R1 + R2 + Visual Check]
8. **Turpin 连接**: §3.3 应与 unfaithful CoT 框架建立理论联系 [R2-W3, R1 agrees]

## Reviewer Divergence

**核心分歧：增量新颖性评估（W3）**
- **R1 (3.5)**: FOL + Z3 确定性验证路径的失败是非平凡实证贡献；BR/C_D/Eff-K 量化工具在先行工作中无对应物；实证 specificity 超越了概念层面的 "self-correction fails"。
- **R2 (3.0)**: 核心洞察——"自提取符号结构继承模型偏差"——在概念层面已被 Huang/Stechly/Amonkar/Chan 覆盖；具体化到 FOL + SC 组合的增量有限。Excitement 2.5/5。
- **Director 评估**: 这是 legitimate disagreement。论文的实证严谨性毋庸置疑，但 excitement/novelty 是区分 Main Conference 和 Findings 的关键。如果 AC 认为量化诊断工具（BR, Eff-K）和 Z3 deterministic path 的 specific test 构成 sufficient novelty，3.5 可辩护；如果认为概念增量有限，3.0 更合适。

---

## Questions for Authors

1. 含一阶量词（∀, ∃）约束的比例？按域和模型报告。[R1-Q1]
2. 是否在 Qwen/LLaMA 上测试过 DeBERTa NLI combo？[R1-Q2]
3. 83.3% confirmation bias 的 per-model breakdown（Table 13 显示 69%–94% 变异）？[R1-Q3]
4. 去重前后平均约束数量和唯一约束率？[R1-Q4]
5. Fine-tuned FOL extractor 能否显著提升 discriminative rate？[R2-Q1]
6. Figure 7 independence-accuracy trade-off 是否有 CJT-based 理论下界？[R2-Q2]
7. DeBERTa NLI 在 ProofWriter 上 same-model SICA degradation（−2.83pp）的根本原因？[R2-Q3]

---

## Missing References

**需要引用**（双方共识）：
- Weng et al. (2023) "Large Language Models are Better Reasoners with Self-Verification" — 正面 self-verification 结果，需在 §2 讨论为何不推广到 FOL 约束提取
- Madaan et al. (2023) "Self-Refine: Iterative Refinement with Self-Feedback" — iterative self-improvement 代表工作，与 §5.4 remediation strategies 直接相关

**可选**：
- Kadavath et al. (2022) "Language Models (Mostly) Know What They Know" — R2 建议，R1 认为非必须（calibration ≠ constraint extraction）
- Lightman et al. (2024) "Let's Verify Step by Step" — R1 建议，但 R2 指出论文已引用（bib key: lightman2024prm）

---

## External Review (Stanford Agentic Reviewer)

**状态：pending（未返回）**

外部审稿于 2026-05-20 19:51 UTC 发起，尚未收到结果。内部审稿不等待外部结果。如后续收到，Research Director 可作为补充参考。

---

## Visual Layout Check（非评分项）

**状态：done**（3 warnings, 10 info）

主要发现：
- **[warning] 前 3 页无任何 figure/table**：正文前 37.5% 缺乏视觉锚点，审稿人需翻到 p.4 才见 Figure 1。建议将核心结果预览或 Figure 1 提前。
- **[warning] Figure 1（SICA pipeline）仅单栏宽**：作为核心方法唯一图示，建议考虑 figure*（全宽）。
- **[warning] Page 21 约 2/3 空白**：Extended Limitations 仅占页面 1/3，建议与后续 appendix 合并排布。
- **[info] Figure 5（p.22）是全文信息量最高的可视化**，深埋 Appendix——与 R1/R2 建议一致，应考虑移入正文。
- **[info] Figure 7 independence-accuracy trade-off 可视化设计优秀**，如有空间值得提升。
- **[info] 无 LaTeX 渲染错误、未解析引用、公式乱码或 margin 溢出。**
- **[info] 表格全部 booktabs 风格，排版规范。**

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 4/5 | **3.75/5** — 方法论扎实，统计分析上乘；FOL 术语和 dedup 问题降低 claim 精度 |
| Excitement | 3/5 | 2.5/5 | **2.75/5** — CJT 框架和 25+ 策略扫描有价值，但核心洞察增量新颖性有争议 |
| Reproducibility | 4/5 | 4/5 | **4/5** — 详细 prompts、伪代码、参数报告；承诺代码公开；种子复制不一致扣分 |
| **Overall** | **3.5** (Borderline Conference) | **3.0** (Findings) | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | **High** |

**综合评分：3.0 — Findings**

**评分理由：** 这是一篇方法论严谨、实验规模出色的负面结果论文。Symbolic Mirage 概念、BR/Eff-K 量化诊断工具、25+ 策略的系统性搜索对社区有明确参考价值。Oracle controls 有效分离了机制和提取质量问题。

限制接收为 Findings 而非 Main Conference 的主要因素是：(1) 核心洞察相对于已有 self-verification failure 文献（Huang 2024, Stechly 2025）的增量新颖性有限——即使 R1 的 rebuttal 部分成立（Z3 deterministic path 是 specific contribution），概念层面的 overlap 仍然存在；(2) 唯一的正向贡献（cross-architecture PoC）在生成端和验证端双重 underpowered；(3) FOL 术语偏差使负面结论的 scope 不够清晰。

**提升至 3.5 的路径：** 解决 W1（术语统一 + 量词分析）、W2（补 Qwen 模型 PoC 实验）、W3（加强 §2 novelty positioning），即可 borderline conference。

---

## Detailed Comments

### §1 Introduction
- 动机清晰，CJT → independence bottleneck → symbolic extraction 逻辑链流畅
- Contributions 3 点概括准确
- "FOL constraints" 首次出现时应明确约束的实际 formalism 层级 [W1]

### §2 Related Work
- 覆盖充分，分 SC extensions、neuro-symbolic reasoning、test-time compute 三个子节
- **缺**: Weng et al. (2023) positive self-verification 和 Madaan et al. (2023) Self-Refine 未引用
- **缺**: 应更显式地 position 本文 vs. Huang/Stechly：不是 "self-correction fails again" 而是 "even deterministic formal verification fails when extraction is self-sourced" [W3]

### §3 Background & Setup
- §3.1 CJT 框架严谨，K_eff 公式引用正确
- §3.2 SICA pipeline 描述清楚
- §3.3 Symbolic Mirage 和 BR 定义清晰；但应与 Turpin et al. (2024) unfaithful CoT 建立理论连接 [W5]；C_D "zero-valued" 表述可更精确

### §4 Experiments
- Table 1 信息密度高，但需增加 seed 列和 powered/exploratory 标注 [W6]
- Type A/B/C regime 分类有用
- Oracle control 是论文最强 positive control

### §5 Analysis
- §5.1 Eff-K 是扎实的理论贡献
- §5.2 83.3% BR 需报告 per-model breakdown（69%–94% 变异）[W11]
- §5.3 TF-IDF cosine similarity 是合理 proxy 但应讨论局限
- §5.4 25+ strategies Figure 5 应在正文 [W9]

### §6 Cross-Architecture PoC
- 方法设计合理（encoder-only NLI as external verifier）
- 单生成模型 + 不一致数据集结果严重限制结论强度 [W2]
- α selection 缺乏 principled justification，有 overfitting 风险

### §7-8 Discussion & Conclusion
- "driver limits voting diversity" vs. "indirect collapse" 双通道分析简洁有力
- Figure 7 是论文最有洞察力的图之一——考虑移入正文
- Conclusion 恰当总结负面发现和正向逃逸路线

### Limitations
- 诚实且全面
- Extended Limitations (§Y) 与 main Limitations 有部分冗余

### Appendices
- 总体高质量，Appendix C (Z3), D (diagnostics), E (power analysis), G (case studies) 尤其有价值
- 25 个 appendix 略多，部分可合并