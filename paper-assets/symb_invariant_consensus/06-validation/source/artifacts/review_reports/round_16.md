---
round: 16
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T14:07:38.531897+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 19 (Fresh)

**论文**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）
**审稿模式**: Fresh（重新审稿，无上轮记忆）

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，通过 Z3 MAX-SAT 求解选择答案。核心发现是 negative result：SICA 在 6 个模型（7B–32B）、3 个推理数据集上均未显著优于 majority voting（Self-Consistency）。论文将此诊断为"symbolic confirmation bias"——自提取约束系统性地追踪模型自身的答案分布而非提供独立信号。27 种 training-free 修补策略均失败。形式化分析提供了 Observation 1（argmax preservation under degeneration）和 Remark 1（DPI information ceiling）。跨架构验证（DeBERTa NLI）在最弱生成器上显示初步逃逸（+6.67pp）。三个零成本诊断指标（K_eff, BR, C₀）在 60 个条件上 correctly characterize failure modes。

---

## Strengths

1. **统计方法论极为扎实** [R1 Strength 1, R2 Strength 1, 共识]：McNemar paired test + BH FDR correction (m=16) + TOST equivalence testing + Bootstrap CI (10,000 resamples) + Power analysis + multi-seed replication 的完整组合在 NLP 论文中极为罕见。诚实报告 underpowered conditions 和 power limitations 体现了高水准的科学诚信。

2. **Oracle control 设计精巧** [R1 Strength 2]：用 gold FOL/DSL 标注替换 self-extracted constraints 的对照实验（+29.90pp FOLIO, +17.17pp ProofWriter, p < 10⁻⁷）清晰地将问题定位在 extraction 而非 solver。这是本文最有说服力的实验设计。

3. **27 种 remediation 变体的系统化测试** [R1 Strength 3, R2 Strength 3, 共识]：涵盖 prompt-level、method-level、paradigm、solver、input diversity、filtering 六个维度，彻底排除了 "换个方法就行" 的反驳。Independence-accuracy trade-off 的实证支持充分。

4. **形式化声明命名克制得当** [R1 Strength 4]：使用 Observation 和 Remark 而非 Theorem/Proposition，诚实反映了其依赖经验条件的本质。

5. **诊断框架有实践价值** [R1 Strength 5, R2 Strength 4]：C₀ < 5%, K_eff ≤ 1.30, BR + SC regime 三个 zero-cost diagnostics 在 60 个条件上 correctly characterize failure modes，prospective validation 在 held-out families (LLaMA, Qwen3) 上通过。对从业者有直接实用价值。

6. **Entropy decomposition 分析精细** [R1 Strength 6]：low-entropy 问题 Δ ≈ 0、high-entropy 问题方向取决于 SC regime 的发现强化了 regime-dependent 叙事。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical, R2-N1, R1 交叉 AGREE] **两条引用存在严重元数据错误**

- `byerly2026selfconsistency`：bib 记录作者 "Nicholas Byerly and Daniel Khashabi, 2026"，但 arXiv:2411.01101 实际作者是 **Adam Byerly**，发表于 **2024**，实际标题/主题（positional bias on long-context problems）与引用标题（mathematical reasoning）完全不同。作者名、年份、主题三重错误。
- `dupo2025`：bib 记录标题 "DuPO: Dual **Process** Optimization"、一作 "Yang, Chenxu"，但 arXiv:2508.14460 实际标题是 "DuPO: Enabling Reliable LLM Self-Verification via Dual **Preference** Optimization"，一作为 **Shuaijie She**，Yang Chenxu 不在作者列表中。
- 错误模式（真实 arXiv ID 配上错误元数据）高度暗示 LLM-assisted hallucination。byerly2026 在 Related Work 中支持 "SC gains plateau" 论点，dupo2025 在 training-based verification 段落中被引用——文献支撑存在漏洞。
- **要求**：对全部参考文献进行系统性交叉验证，修正所有错误条目。

**MF-2** [critical, R2-N2, R1 AGREE with nuance] **"Advances beyond Huang et al. (2024)" 的 claim 过度**

- 论文在 Abstract、Section 1（Introduction）、Section 2（Related Work）、Section 7（Discussion）至少四处使用 "advances beyond Huang et al. (2024)" 措辞。
- Huang et al. (ICLR 2024) 已建立 "LLMs cannot self-correct reasoning without external feedback" 核心结论。本文的贡献是 (a) 将此洞见扩展到 formal symbolic verification setting，(b) 提供 Markov chain 形式化（Observation 1, Remark 1），(c) 系统排除 27 种 remediation——这是 **scope extension + formalization**，而非 fundamental insight 上的 "advance beyond"。
- 核心洞见（自提取信息因与答案来自同一信息源而缺乏独立性）在 Huang et al. + Condorcet Jury Theorem 框架下是可预见的。
- **要求**：将 "advances beyond" 改为更精确的表述如 "extends and formalizes ... in the context of formal self-verification"。

**MF-3** [critical, R1-N1 + R2-N3, 共识] **Cross-architecture escape 证据不足以支撑 top-level contribution**

- Capability-gap pattern 仅基于 6 个 verifier-generator 组合（Spearman ρ=1.0, p=0.003），其中 **4/6 共享同一 DeBERTa verifier**，实际有效自由度远小于 n=6。
- Table 3 的 n=4 generators 全部 paired with 同一 DeBERTa-large-mnli，排列空间仅 24 种。
- "Generator SC < verifier standalone accuracy 才有增益" 可能是 **trivial condition**——本质上是 "用更好的模型替代更差的模型" 的必然结果，不需要 information independence 理论。
- R1 额外指出：增益可能只是 **ensemble diversity 效应**（Dietterich 2000），而非 SCB escape。需要 cross-model majority vote ensemble 作为 ablation 区分两种假说。
- Domain-adapted verifier (99.67% standalone) 引入了 training，与 training-free 叙事线矛盾。论文自己承认 "directional evidence rather than a proposed method"，但叙事结构仍将其作为 escape 证据呈现。
- **要求**：将 Contribution 3 从并列贡献降级为 "preliminary observation"，或增加不同架构的 verifier + cross-model majority vote ablation。

**MF-4** [critical, R1-N2 + R2-W2(升级), 共识] **10/16 条件 underpowered，中心论断表述超出统计证据范围**

- Appendix D Table 6：3 个 confirmatory conditions 的 observed power 均低于 21%（Qwen-14B FOLIO+PW: 5.7%, LLaMA-8B StrategyQA: 20.6%, LLaMA-8B FOLIO: 18.6%）。MDE 为 1.86–4.84pp。
- TOST 等价检验仅 4/16 条件确认等价（±2pp margin），10 条件 underpowered。
- Abstract "We find no evidence of improvement" 和标题 "No Detectable Improvement" 构成 blanket negative claim，但统计证据仅能排除 >~2pp 的效果。"Absence of evidence is not evidence of absence" 在正文中有提及（Section 4），但 Abstract/标题层面的表述未反映这一 nuance。
- **要求**：(a) Abstract 改为 "no evidence of improvement exceeding ~2 percentage points"；(b) 在 Discussion 中显式论证 <2pp 在 4.5× 计算开销下无实际价值，将 power limitation 转化为 practical insignificance 论证。

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning, R1-W1 + R2-W4, 共识] **BR/SCB 概念框架混淆 structural degeneration 与 extraction bias**

- R1 从技术层面指出：source-attribution scoring 下 BR > 1 是 trace-count 分布的**数学必然结果**。Permutation test 证实 BR_excess ≈ 0 (p > 0.7, §5.1)——BR 完全由 trace-count 结构解释，不含 extraction 过程的额外偏差。BR 度量的是 degeneration 程度，不是独立于 Observation 1 的 bias 证据。
- R2 从概念层面指出："Symbolic **Confirmation Bias**" 暗示 cognitive bias 类比（主动寻找支持性证据），但实际机制是 structural limitation（约束和答案来自同一信息源而结构性耦合）。
- 两个批评收敛到同一结论：论文应更清楚地区分 "structural degeneration"（Observation 1 的后果）和 "extraction bias"（如果存在的话）。目前混淆使 BR 看起来提供了 Observation 1 之外的独立证据，但实际上没有。
- **建议**：(a) 在首次定义 SCB 时明确说明这是 structural limitation 而非 cognitive bias 类比；(b) 报告 BR_excess 作为判断是否存在 extraction-level 额外偏差的指标；(c) 考虑更精确的术语如 "symbolic information collapse" 或 "self-referential degeneration"。

**SF-2** [warning, R2-W1, R1 AGREE] **Abstract 超过 200 词限制**

- 经去除 LaTeX 命令后词数统计约 202 词，超过 EMNLP 2026/ARR 的 200-word 硬约束。虽仅超出 2 词，但属明确格式违规。

**SF-3** [warning, R1-W2, R2 AGREE] **"Pre-registered" margin ±2pp 无注册凭证**

- Section 4 使用 "pre-registered margin ±2 pp" 但未提供 OSF/AsPredicted 等预注册链接。"Pre-registered" 在实证研究中有严格操作定义。改为 "pre-specified" 或 "predetermined" 即可。

**SF-4** [warning, R1-W3, R2 AGREE with nuance] **BH correction m=16 包含非独立条件**

- 16 个条件中包含 Mistral-7B×FOLIO 的 3 个单独 seed (s123, s456, s789) 和 1 个 3-seed aggregate，以及 Qwen2.5-14B×FOLIO 的 4-seed aggregate。Aggregate 是 component seeds 的函数，非独立检验。虽然更大的 m 使 BH 更保守，但方法论应更干净地区分 confirmatory vs exploratory 条件。

**SF-5** [warning, R1-W4, R2 AGREE] **Observation 1 条件 (iii) "approximately uniform constraint yield" 缺乏系统验证**

- 条件 (i) |C\| ≈ 0 由 Z3 rejection rate 3.4% 实证支持，条件 (ii) source-attribution 是系统设计，但条件 (iii) 缺乏直接验证。论文未报告 per-trace constraint yield 的分布统计量（mean, std, CV），应按 answer group 分层报告。

**SF-6** [warning, R2-W3, R1 AGREE] **Turpin et al. 引用年份错误**

- references.bib 中 `turpin2024language` 记录 year={2024}，但 "Language Models Don't Always Say What They Think" 发表于 NeurIPS **2023**。

**SF-7** [warning, R2-W5, R1 AGREE minor] **论文密度过高，可读性受损**

- LaTeX source 含 `\enlargethispage{6\baselineskip}` (main.tex:72)、`\vspace{-4mm}` (main.tex:76)、`\vspace{-1.5mm}` (main.tex:73) 等排版 hacks。Section 7 (Discussion and Conclusion) 仅约 1/3 页。Figure 4 信息密度极高但难以快速 parse。建议将部分内容移入 appendix 以提升可读性。

**SF-8** [warning, R1-M1] **Introduction 使用 "prove" 描述 Observation 1**

- §1: "We prove this degeneration is structural (Observation 1)"——Observation 1 依赖经验条件 (iii)，"prove" 过强，应改为 "show" 或 "demonstrate"。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上达成完全共识：

1. **Overall 3.0 (Findings)**：R1 初评 3.5，交叉审议后被 R2 的 novelty 和引用论点说服，下调至 3.0。
2. **Cross-architecture escape 应降级**：n=6（实际 <6 due to shared verifier）不足以支撑 top-level contribution。"Generator < verifier 才有增益" 可能是 trivial condition。可能只是 ensemble diversity 效应。
3. **Underpowered claim 需精确化**：Abstract/标题的 blanket negative claim 超出统计证据范围。
4. **SCB/BR 概念框架需澄清**：BR > 1 是 structural 而非 bias 证据；SCB 命名暗示 correctable deficiency 但实际是 structural limitation。
5. **引用错误必须修正**：两条引用元数据严重错误，需系统性交叉验证全部参考文献。
6. **"Advances beyond Huang et al." 表述过度**：应改为 "extends and formalizes"。
7. **统计方法论是论文最大优势**：McNemar + BH + TOST + Bootstrap + Power analysis 的完整组合在 NLP 论文中极为罕见，使 negative result 高度可信。
8. **论文适合 Findings 而非 Conference**：贡献定位是 confirmation + formalization（用大规模实验确认并形式化了一个 expected result），而非 discovery。统计严谨性满足 Findings 的 soundness 要求，但 excitement/novelty 不够 Conference。

---

## Reviewer Divergence [REBUT]

无重大分歧。R1 初始评分比 R2 高 0.5 分，但在交叉审议后被说服并下调，最终收敛。

---

## Questions

1. **BR_excess ≈ 0 意味着什么？** Permutation test 显示经验 BR 完全由 trace-count 结构解释（BR_excess ≈ 0, p > 0.7）——如果没有超出 base-rate 的额外 extraction bias，"symbolic confirmation bias" 是否应该重新命名？
2. **Observation 1 条件 (iii) 的验证数据？** 每条 trace 平均产生多少 constraints？标准差？不同 answer group 之间的 yield 差异？
3. **为什么不测试 non-NLI independent verifier？** Cross-model majority vote ensemble 是否也能产生类似增益？这将区分 "information independence" 和 "ensemble diversity" 假说。
4. **TOST margin 的 "pre-registered" 指什么？** 是否有 OSF 或类似平台的注册记录？
5. **如果将约束用于 re-prompting 而非 MAX-SAT scoring，结果是否不同？** 27 种策略是否都在 extraction-aggregation paradigm 内？
6. **Domain-adapted verifier 的增益 (+12.67pp) 是否主要来自 domain-specific training 而非 structural independence？**

---

## Missing References

1. **Ensemble diversity 经典文献** [R1 + R2 共识]：Dietterich (2000) "Ensemble Methods in Machine Learning", Krogh & Vedelsby (1995) "Neural Network Ensembles, Cross Validation, and Active Learning"——Section 2 ensemble theory 段落和 Section 6 cross-architecture discussion 应引用并回应 ensemble diversity 假说。
2. **OpenAI o1/o3 reasoning models** [R2]：Table 2 包含 o3 cross-model extraction 结果，但 Section 2 "test-time compute" 段落未显式讨论 o1/o3 内部推理链机制及 SICA paradigm 的适用性。
3. **Cobbe et al. (2021) GSM8K verifier** [R1]：独立 verifier 提升推理性能的早期实例，与 Section 6 的 cross-architecture escape 直接相关。

---

## External Review

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 warning, 9 info）。

**Warning:**
- Limitations section heading 出现在 page 8 底部极端位置（orphan heading），后续仅 2 行正文在同一页，大部分 Limitations 内容在 page 9 顶部。建议用 `\needspace` 调整。

**Info（主要发现）:**
- Figure 1 出现在 page 2 顶部，pipeline 架构图提供清晰视觉锚点，Title-Abstract-Figure 1 叙事一致性好。
- Figure 2 散点图图例文字偏小（约 6-7pt），建议适当放大。
- Table 1 字号偏小（~7pt），处于舒适阅读下限。booktabs 风格正确，表头分区清晰。
- Figure 3 Causal DAG 尺寸明显偏小（仅占左栏 1/4 面积），作为核心概念图建议放大。
- Figure 4 条形图 x 轴标签和图例文字偏小，分类名称需仔细辨认。
- Appendix 单页含 4 个表格，密度极高但作为 appendix 可接受。

---

## Overall Assessment

**评分：3.0 — Findings（可被 Findings 接收）**

**Reviewer 评分汇总：**

| 维度 | R1 (交叉后) | R2 | 综合 |
|------|------------|-----|------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 2.5/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 3/5 | 4/5 | 3.5/5 |
| Confidence | 4/5 | 4/5 | 4/5 |
| **Overall** | **3.0** | **3.0** | **3.0** |

**置信度：4/5**（两位 Reviewer 在各自专长领域（统计方法论 / 文献与 novelty）均有充分把握，且交叉审议后完全收敛）

**理由：**

这是一篇实验执行质量高、方法论严谨的 negative result 论文。60 个条件、9 个模型、27 种修补策略的系统排除确实超出了多数同类工作的证据标准。Oracle control 精巧，诊断框架有实用价值，统计方法论在 NLP 领域属顶级水准。

但在 excitement 维度存在根本性限制：核心洞见（自提取信息因与答案来自同一信息源而缺乏独立性）在 Huang et al. (ICLR 2024) 和 Condorcet Jury Theorem 框架下是可预见的。论文的贡献更准确的定位是 confirmation（用大规模实验确认 expected result）+ formalization（Markov chain model, diagnostics），而非 discovery。Cross-architecture escape 作为唯一正面贡献过于初步（n=6, shared verifier, 可能只是 ensemble diversity）。两条引用的元数据严重错误进一步降低了整体学术质量评估。

如果 MF-1（引用修正）、MF-2（novelty claim tempered）、MF-4（negative claim 精确化）得到修正，本文作为 Findings 论文是合适的——为社区提供了有价值的 negative evidence 和实用的诊断工具。但以目前的 novelty framing，不足以支撑 Conference main 接收。

---

## Detailed Comments

### Section-by-Section

**Abstract (p.1):**
- 约 202 词，超过 200 词限制 [SF-2]
- "advancing beyond Huang et al. (2024)'s findings" → "extending and formalizing" [MF-2]
- "We find no evidence of improvement" → "no evidence of improvement exceeding ~2 percentage points" [MF-4]
- "self-extracted" 出现 4 次，可适当减少重复

**Introduction (§1, p.1-2):**
- "We prove this degeneration is structural" → "We show" [SF-8]
- Contribution 3 ("Cross-architecture escape") 应标注 "preliminary" [MF-3]
- Figure 1 pipeline 图清晰有效

**Related Work (§2, p.2-3):**
- 结构良好（5 段覆盖 5 个维度），引用密度高
- byerly2026selfconsistency 和 dupo2025 需修正 [MF-1]
- turpin2024language 年份 2024→2023 [SF-6]
- 缺少 ensemble diversity 经典文献和 OpenAI o1/o3 引用

**Method (§3, p.3-4):**
- SICA pipeline 描述清晰完整，数学公式和算法规范
- Observation 1 条件 (iii) 需系统验证 [SF-5]
- BR 定义需与 "structural degeneration" 而非 "bias" 关联 [SF-1]
- α=0.5 sensitivity 在 Appendix 有验证，正文可简要提及

**Results (§4, p.4-5):**
- Table 1 信息密集但结构清晰，regime 分类有效
- "pre-registered margin" → "pre-specified margin" [SF-3]
- BH m=16 应标注 confirmatory vs exploratory [SF-4]
- Figure 2 regime scatter 有效传达了核心模式

**Analysis (§5, p.5-7):**
- §5.1 SCB 分析是论文最有洞察力的部分
- 但 BR_excess ≈ 0 + permutation test 的含义未充分 reconcile with "bias" 叙事 [SF-1]
- §5.2 Remediation 27 种变体的穷举测试令人信服
- §5.3 Diagnostic framework 有实践价值，prospective validation 是加分项
- Figure 3 Causal DAG 尺寸偏小 [视觉审查]
- Figure 4 信息密度极高，考虑简化正文版本

**Escaping the Bottleneck (§6, p.7-8):**
- Cross-architecture escape 结果有趣但证据不足 [MF-3]
- 需要 ensemble diversity ablation 区分假说
- Domain-adapted verifier 与 training-free 叙事的张力需更明确讨论
- Table 3 仅 4 个 generators 共享 1 个 verifier，统计说服力有限

**Discussion (§7, p.8):**
- 过于简短（~1/3 页），应更充分展开
- "advancing beyond Huang et al." → "extending and formalizing" [MF-2]
- 缺少对 practical implications 和 future directions 的更具体讨论

**Limitations (p.8-9):**
- 内容合理（模型范围、语言、训练方法、statistical power），简短覆盖 3 个主要限制
- Orphan heading 问题 [视觉审查 warning]

**Appendix:**
- 内容丰富（prompt templates, pseudocode, statistical analyses, case studies, ablations）
- 对论文完整性有重要支撑
