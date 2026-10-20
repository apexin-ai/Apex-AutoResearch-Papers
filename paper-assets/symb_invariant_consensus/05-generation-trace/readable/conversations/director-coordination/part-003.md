# Director coordination — Part 3 of 9

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/bd/bdd0e6c8e8a0a8a81e76.json)

## Round 42

### User

_source line 701 · 2026-05-20T15:17:30.101847+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## Weaknesses 逐条回应

**[AGREE] R1-W1: 统计功效不足与标题过度断言。**

R1 指出的核心问题成立。论文 Appendix E（Table 5）报告 observed power 仅 5.7%–20.6%，MDE = 4.64pp–8.84pp，这意味着论文无法排除 SICA 存在 <4pp 的小幅正效应的可能。标题使用 "Fail" 是 evidence of absence 的措辞，但论文提供的仅是 absence of evidence。

不过需要补充一点：虽然单条件 power 低，但 15 个 non-degenerate conditions **一致**未达显著、且 bootstrap 95% CIs（Appendix F, Table 6）全部包含零，这种跨条件的一致性本身构成间接证据。R1 建议的 TOST equivalence test 是正确的统计方法——如果作者能证明效应等价于零（equivalence margin 可设为 ±2pp），则 "Fail" 的表述可以保留；否则应软化为 "do not reliably improve" 或类似措辞。

**[AGREE] R1-W2: 跨架构 PoC 的多重比较问题。**

这是一个我在初审时未充分关注但确实存在的问题。§6 报告 DeBERTa NLI 在 ProofWriter 上 p=0.013，但论文测试了 2 datasets（FOLIO, ProofWriter）× 至少 3 个 n configurations（n=1, 3, 5），总计 ≥6 次比较。Bonferroni 校正后阈值为 p < 0.0083，p=0.013 不再显著。Holm-Bonferroni 或 BH FDR 校正可能更合适（不如 Bonferroni 保守），但无论哪种方法，论文必须报告校正后结果。

这直接影响了 §6 的结论强度——"cross-architecture combo yields +3.50pp consistently across two datasets" 的 "consistently" 措辞在多重比较校正后可能站不住脚。作为 reviewer 我认为这是 PoC 而非 main claim，影响有限但必须修正。

**[AGREE] R1-W3: CJT 框架应用的统计严谨性 — 与我的 Q3 一致。**

R1 指出 Fleiss' κ（nominal scale agreement）与 Ladha (1992) 的 voter correlation coefficient 不是同一概念的问题完全成立。论文在 §3.1 承认 κ 是 "qualitative proxy for the intraclass correlation coefficient (ICC)"，但随后在 §5.1（Table 2, Table 3）和 §7 Discussion 中大量使用 Effective-K 的**具体数值**（1.20–3.62）进行定量论证，这与 "qualitative proxy" 的定位矛盾。

补充 R1 的观点：Kish 公式（Eq. 1）假设 exchangeable/equicorrelated 结构（所有 trace pairs 等相关），但 LLM traces 可能存在 cluster structure（如 同一 reasoning template 生成的 traces 内部相关性 > 跨 template 相关性）。论文未验证这一假设。

**[AGREE] R1-W4: Bias ratio 报告不一致。**

重新审查论文，§5.2 报告 "bias ratio of 4.97×"（raw），后文提到 "1.97× (raw constraint counts; 4.24× when weighted)"——这里 1.97× 和 4.97× 的关系不清楚。Table 14（Appendix P）显示 FOLIO 上的 cross-model 数据，BR (wtd.) 分别为 Mistral-7B 2.14×, Qwen2.5-14B 3.03×, LLaMA-3.1-8B 3.86×。这些数字与主文的 4.97× 的关系确实需要更清晰的 traceability。

R1 的要求合理：主文中引用的核心数字（4.97×）必须明确标注来源条件（哪个模型、哪个数据集、raw vs weighted、specific error subset vs overall）。

**[AGREE] R1-W5: Type A/B/C 分类的事后性。**

SC 准确率阈值（60% 和 40%）看起来是从 Table 1 的 empirical patterns 归纳出来的，而非先验理论推导。作为描述性框架这可以接受，但论文将其呈现为有解释力的分类体系（"Type A: confirmation bias"，"Type B: non-formalizable domains"，"Type C: error amplification"），暗示了因果机制。

建议作者要么 (a) 提供阈值选择的理论依据（如从 CJT 框架推导出的临界 accuracy），要么 (b) 明确标注这是 post-hoc descriptive taxonomy 而非 predictive framework。

**[AGREE] R1-W6: Eq. 4 推导不够 formal。**

§3.2 的 degeneration condition 从 "self-extracted constraints are coupled to their source answer" 跳到 "score degenerates to weighted majority vote"（Eq. 4），中间缺少对 constraint-answer coupling 如何在 MAX-SAT scoring 中传播的形式化推导。当前呈现更像直觉解释而非严格证明。对于一篇理论贡献包含 CJT 框架的论文，这一推导应更 rigorous。

**[AGREE] R1-W7: α=0.5 缺乏 justification。**

Eq. 3 中 α=0.5 给 constraint 和 trace count 等权重，但论文未解释为什么这是合理的 default。如果 constraint quality 很低（论文自己论证了这一点），那么低 α（更依赖 trace count）可能更好——这反过来又使 SICA 更接近 SC，进一步支持 negative result。论文应至少报告 α sensitivity analysis。

实际上，检查 Appendix I（constraint ablation, Table 9），论文确实做了 "count-only"（α=0）的实验，结果 "Agreement w/ SC: 773/804"——几乎与 SC 完全相同。这支持了 α sensitivity 的重要性但主文未充分讨论。

**[AGREE] R1-W8: GSM8K 和 AIME 样本量过小。**

GSM8K n=30 和 AIME n=22 确实过小，McNemar test 在这些样本量下几乎不可能检测到合理效应。论文在 Appendix D（Table 4）将 GSM8K 和 AIME 标注为 "domain-formalizability diagnostic"（即检查约束提取是否适用于该领域），而非 primary evaluation datasets，这部分缓解了问题。但 Table 1 将它们与 n=204/600 的数据集并列呈现，确实可能误导。建议在 Table 1 注释中更明确标注 "pilot" 性质。

**[AGREE] R1-W9: Orphan bib entry — 与我的 W6 一致。**

`press2023compositionality` 在 .bib 中存在但未被引用。我的引用验证结果也独立发现了这一问题。

---

## Questions 逐条回应

**[AGREE] R1-Q1: Eq. 5 概率空间定义不明。**

§3.3 的 Symbolic Mirage hypothesis P(E_i(t_i) | a*, u_i) ≠ P(E_i(t_i) | a*) 中，概率是 over 什么的？Over traces t_i given a fixed question？Over questions？Over models？论文未定义 probability space 和 measure。对于一个作为核心假设呈现的公式，这是形式化不足。与我的 W5（"Symbolic Mirage" 术语精确度）相关。

**[AGREE] R1-Q2: K=8 的 Δ≈+4.90pp 值得更深入分析。**

§M.1（K sensitivity）显示 K=8 时 Δ≈+4.90pp，高于 K=12 的 Δ≈+1.47pp。这一非单调关系值得关注：如果 K=8 效应较大，可能暗示在 certain sampling budget 下 SICA 有有限的正效应。论文将此归因于 "SC fluctuation"，但 K=8 恰好在 intermediate-SC region（SC 55.88%），正是 Type A conditions 可能产生正效应的区域。

不过需注意 K=8 的 Δ 可能仍不显著（论文报 p=0.092 for K=12，K=8 未报 p-value），且只有 FOLIO n=204 一个数据集。单数据集、未报显著性的结果不应过度解读，但作为 exploratory finding 确实值得讨论。

**[AGREE] R1-Q3: 应补充 sentence embeddings 验证 — 与我的 W3 一致。**

完全同意。TF-IDF cosine similarity 作为 process-level independence 的唯一度量存在 construct validity 问题。论文自己承认（§5.3）TF-IDF 是 "lower bound on true process similarity"，但问题是双向的：

1. TF-IDF 过估 independence（忽略语义等价但措辞不同的路径）→ 实际 process independence 更低
2. TF-IDF 过估 dependence（将共享 domain vocabulary 误算为 reasoning overlap）→ 实际 process independence 更高

用 SBERT 或 SimCSE 的 sentence embeddings 可以提供 complementary evidence，且计算成本很低。这是 minor revision 级别的工作。

**[REBUT] R1-Q4: 跨架构 PoC 是否尝试过其他外部信号源。**

R1 的问题合理，但需注意 §6 的 scope 是 proof-of-concept 而非完整解决方案。论文选择 DeBERTa NLI 的理由是明确的（§6 Method）：encoder-only model + 不同训练数据 + 不同 Mixture share → 满足 "outside the model's distribution" 的要求。

论文在 Appendix J（Remediation Strategy Details, Table 10-12）报告了 22+ remediation strategies，包括 prompt-level（contrastive prompting, multi-round等）和 method-level（ICG, Contrastive, Debate 等）。这些都是 same-model 内部策略。Cross-architecture NLI 是唯一测试的外部信号源。

不过我同意论文应该简要讨论为什么没有测试其他外部信号（如 trained verifier、code execution for math、retrieval-based verification），至少在 Discussion 或 Future Work 中提及。

**[AGREE] R1-Q5: T_ext = 0.3 的选择需要 justification。**

Trace generation 使用 T=0.7 以增加 diversity，constraint extraction 使用 T_ext = 0.3 以增加 faithfulness——这一 intuition 合理但未在论文中明确 stated。Appendix N（Temperature Sensitivity）分析了 trace generation temperature 的影响但似乎未分析 extraction temperature 的影响。如果 T_ext 的选择影响 constraint quality，这可能是 confounding variable。

---

## Missing References 回应

**[AGREE] R1-MR1: TOST equivalence testing 文献。**

如果论文要保持 "Fail" 的表述，引用 TOST 文献并执行 equivalence test 是必要的。Lakens (2017) "Equivalence Tests: A Practical Primer" 是标准参考。

**[AGREE] R1-MR2: Amonkar et al. (2025) 需更详细对比。**

论文已引用 Amonkar et al. 但仅一句话（§2, Related Work）。鉴于 Amonkar et al. 直接研究 LLM-as-formalizer 的局限性，且其 finding（15/24 组合上 formalizer 不如 solver）与本文 confirmation bias 发现高度相关，应在 §7 Discussion 中进行更实质性的对比：SICA 的 formalization 失败模式与 Amonkar et al. 的 complexity-driven degradation 是否同一现象？

**[REBUT] R1-MR3: Weng et al. (2023) self-verification。**

我无法确认 "Weng et al. (2023) self-verification" 的具体引用。如果 R1 指的是 self-verification / chain-of-verification 文献，论文已引用了该方向的核心工作（Huang et al. 2024, Stechly et al. 2025）。R1 应提供完整的引用信息以便核实。另外需注意，我自己的 Missing References 中提出了 CLOVER（Ryu et al., ICLR 2025）和 VERGE 作为更关键的缺失引用——这两篇与 SICA 的 FOL+SAT pipeline 直接对标，重要性高于一般 self-verification 文献。

---

## 与我自身审稿意见的交叉对照

| R1 要点 | 我的对应意见 | 一致性 |
|---------|-----------|--------|
| W1 统计功效 | 我未单独提出，R1 分析更深入 | R1 补充了我的盲点 |
| W2 多重比较 | 我未单独提出 | R1 补充了我的盲点 |
| W3 CJT 框架 | 我的 Q3（Fleiss' κ as ICC proxy） | 一致 |
| W5 Type分类 | 我未单独提出 | R1 观点合理 |
| W9 Orphan bib | 我的 W6 | 一致 |
| Q3 Sentence embeddings | 我的 W3（TF-IDF 粗糙） | 一致 |
| — | 我的 W1（新颖性与先行工作区分） | R1 未涉及 |
| — | 我的 W2（CLOVER 缺失） | R1 未涉及 |
| — | 我的 W4（模型规模限制） | R1 未涉及 |

**总体判断**：R1 的统计方法学审查（W1 power analysis, W2 multiple comparisons, W3 CJT rigor）比我的初审更细致，发现了我遗漏的重要问题。结合两份审稿，论文在统计方法学（R1 focus）和新颖性/相关工作覆盖（我的 focus）两个维度都需要修订。

**评分调整**：考虑 R1 提出的统计功效问题（W1），我对 Soundness 的评分从 3.5 调低至 **3.0/5**。Overall Assessment 维持 **3.0 (Findings)**——论文的实验设计和分析深度足够 Findings 水平，但统计结论的 overclaiming（标题 "Fail"）+ 新颖性不足 + 关键相关工作缺失使其难以达到 Conference 水平。


---

[Reviewer 1 审稿意见]:

## 交叉审查：逐条回应 Reviewer 2 的审稿意见

---

### Weaknesses

**[REBUT] R2-W1: 核心发现的新颖性与先行工作区分不足。**

R2 认为 Symbolic Confirmation Bias 仅是 Huang et al. (2024) / Stechly et al. (2025) 在符号域的实例化。我不完全同意。关键区分在于：

1. Huang et al. (2024) 和 Stechly et al. (2025) 讨论的是 natural language 层面的 self-correction/self-verification failure——即 LLM 用自然语言反思推理。本文引入了一个关键中间层：将推理形式化为 FOL + 通过 sound solver (Z3) 验证。直觉上，形式化应该打破自然语言的模糊性，提供"硬约束"——但实验证明形式化后 confirmation bias 依然存在（§5.2, bias ratio 4.97×）。这一发现是 non-trivial 的，因为 Z3 本身是 sound 的，bias 不在 solver 中而在 extraction 中。

2. Oracle 控制（§4.3, Table 1 注释）清楚表明：当约束来自 ground truth，SICA 获得 +29.90pp (FOLIO) 和 +11.22pp (ProofWriter)。这是一个 Huang/Stechly 框架中没有的 separation result——他们没有证明"如果验证信号是正确的，self-verification 机制本身有效"。

3. Amonkar et al. (2025) 确实最相关，但其关注的是 constraint *satisfaction* problem formalization quality，而非用约束做 answer *aggregation*。SICA 的 MAX-SAT aggregation pipeline（Algorithm 1-2）和 source-trace attribution scoring（Eq. 3）是新贡献。

不过，论文确实应该在 §2 Related Work 中更明确地画出这些区分线。R2 的意见有合理性——论文目前对 differentiation 的论述过于简略。建议作者在 Related Work 中增加一段专门讨论"与 self-verification failure 文献的区别"。

**[AGREE] R2-W2: 缺失 CLOVER 和 VERGE。**

同意。CLOVER（compositional FOL translation + SAT verification）在 ICLR 2025 发表，与 SICA 的技术路线高度相似但取得了正面结果——这恰恰是论文需要正面回应的核心对比。如果 CLOVER 通过 compositional translation 避免了 confirmation bias，那么 CLOVER 的成功与 SICA 的失败之间的差异（可能是 constraint extraction 的粒度、compositionality 的作用、或数据集差异）值得深入讨论。VERGE 的 iterative refinement 也与论文 §5.5 的 remediation analysis 直接相关。

这一遗漏会削弱论文在 Related Work 完整性上的评分，尤其对于声称"22+ remediation strategies all fail"的论文，未讨论实际取得正面结果的同类方法是一个显著缺口。

**[AGREE - 与我的 Q3 一致] R2-W3: TF-IDF cosine similarity 过于粗糙。**

同意。我在 Q3 中提出了相同关切。论文自身也承认 TF-IDF 捕获 lexical overlap 而非 semantic similarity（§5.3："TF-IDF similarity captures lexical overlap rather than semantic equivalence, making it a lower bound on true process similarity"）。但论文随后用这个 lower bound 得出 strong conclusion（"process-level homogeneity is architecture-independent"），这在逻辑上是合理的（lower bound 已经很高说明真实值更高），但补充 sentence embedding 验证会显著加强论证。

**[REBUT] R2-W4: 模型规模局限于 7B-32B，缺少 frontier 模型。**

部分不同意 R2 将此定为 Should-Fix 级别。

1. 论文 Limitations（p.9）明确承认："whether the independence bottleneck persists at larger scales (70B+) or with reasoning-specialized models is untested"。这是诚实的 scope 声明。

2. 论文的核心论点是 structural argument——当 constraint extractor 和 trace generator 是同一模型时，约束不可能提供独立验证信号。这一论点不依赖于模型规模。Oracle 实验（§4.3）和跨架构 PoC（§6）正是验证这个 structural hypothesis 的：问题不是模型不够强，而是同源性造成的确认偏差。

3. 实际上，如果 frontier 模型的 formalization 能力更强，confirmation bias 可能更严重——因为更强的模型更能"faithfully"提取支持自己答案的约束。Table 1 中较强模型（Qwen2.5-14B）的 bias ratio 3.93× 高于较弱模型（Mistral-7B 的 1.97×），暗示了这一趋势。

4. 但我同意 R2 的一个点：论文使用了"architecture-independent"这一措辞（§5.3, Table 3），如果只在 7B-32B 开源模型上验证过，这一 claim 过强。建议作者要么弱化为"consistent across tested architectures (7B-32B)"，要么补充至少一个 frontier 模型的 pilot 实验。

**[REBUT] R2-W5: "Symbolic Mirage" 术语的营销性质。**

部分不同意。

1. 论文对 "Symbolic Mirage" 有明确的技术定义（§3.3, Eq. 5）：指的是自提取约束看起来像独立验证信号，实际上是模型分布的投影（projection of the generating model's distributional biases）。这不是泛指"符号方法失败"，而是特指 self-extracted constraints 的虚假独立性。

2. Oracle 实验（§4.3）和跨架构 PoC（§6）共同表明论文的结论是有条件的：符号约束方法在 ground-truth 约束或外部约束下是有效的——"Mirage" 特指 self-extraction 场景。这一区分在 §7 Discussion 和 §8 Conclusion 中有明确表述。

3. 不过，R2 的顾虑有道理——如果读者只看标题和 abstract，确实可能误以为"符号约束方法整体失败"。建议作者在 abstract 中增加一句明确的限定："The failure is specific to self-extraction; oracle constraints and cross-architecture verification break the mirage."

**[AGREE - 与我的 W9 一致] R2-W6: 引用格式小问题。**

同意，与我的 W9 一致。press2023compositionality 是 orphan entry。Author name 格式差异是 BibTeX 解析常见问题，不影响引用的真实性。

**[AGREE] R2-W7: Reasoning models 讨论缺失。**

同意。论文包含 QwQ-32B（一种 reasoning model），但 Related Work §2 没有专门讨论 reasoning models（o1, R1, QwQ）这一类别。考虑到 reasoning models 使用 extended thinking/chain-of-thought，它们的 trace homogeneity 可能与 standard models 有质的不同——更长的推理链可能产生更多样的中间步骤，但也可能因为 RL 训练导致更强的模式固化。这值得在 Related Work 或 Discussion 中讨论。

---

### Questions

**[REBUT] R2-Q1: QwQ-32B 在 Type A 条件下是否暗示 reasoning models 缓解 confirmation bias？**

数据不支持这一推论。从 Table 1 看，QwQ-32B 仅在 GSM8K（n=30）上报告了结果——样本量过小，无法进行任何有统计意义的比较。即使 QwQ-32B 在某些条件下没有 significant degradation，也可能仅仅是因为 power 不足（与我的 W1 一致）。要回答"reasoning models 是否缓解 confirmation bias"需要在 FOLIO (n=204) 或 ProofWriter (n=600) 这样的较大数据集上对 reasoning model 进行完整实验。论文 Limitations（p.9）中也提到了 reasoning-specialized models 作为未测试的范围。

**[AGREE] R2-Q2: ProofWriter Oracle 的 gold constraints 构造。**

同意这是一个需要回答的问题，但论文实际上在 Appendix H 中有详细描述：ProofWriter 问题是 DSL 逻辑程序，pipeline 直接解析为 Z3 formulas（确定性转换，无 LLM 参与），594/600 (99.0%) 成功解析。这是一个 clean 的 oracle 构造，不依赖 LLM。R2 提问可能意味着 Appendix H 的存在不够 prominent——建议作者在 §4.3 主文中加一句指向 Appendix H 的引用。

**[AGREE - 与我的 W3 一致] R2-Q3: Fleiss' κ 作为 ICC proxy 的精确度。**

完全同意，与我的 W3 一致。Fleiss' κ 和 Ladha (1992) 的 ICC 在统计含义上不同，K_eff 的具体数值（1.20–3.62）的可信度取决于这个映射的精确程度。论文应补充替代指标或弱化定量声明。

**[AGREE] R2-Q4: 跨架构 PoC 为何不在 LogiQA 和 StrategyQA 上测试？**

合理的问题。论文 §6 仅在 FOLIO 和 ProofWriter 上测试 DeBERTa NLI，可能因为 NLI 对 formal logic datasets 更自然适用。但 StrategyQA（commonsense reasoning）和 LogiQA（informal logic）代表了不同推理类型——如果跨架构 PoC 只在 formal logic 上有效，其泛化性有限。这与我的 Q4 一致——PoC 的单一性（仅 DeBERTa NLI × 2 formal logic datasets）限制了结论的外推范围。不过我认为这不影响论文的核心负面结论，只影响 §6 建设性贡献的说服力。

---

### Missing References

**[AGREE] CLOVER (Ryu et al., ICLR 2025)**：最关键的遗漏。CLOVER 的 compositional FOL translation + SAT verification 取得正面结果，与 SICA 的失败形成直接对比——论文必须讨论两者差异的原因（constraint extraction 方式、compositionality、task 差异等）。

**[AGREE] VERGE (arXiv 2601.20055)**：与 §5.5 remediation analysis 直接相关，特别是其 iterative refinement 策略。

**[AGREE] "Not All Votes Count" (Xia et al., 2024)**：如果该工作讨论了 program-based verification 作为替代 voting 的方式，则与本文的跨架构 PoC 方向相关。

**[AGREE] "Logical Soundness" (arXiv 2604.04177)**：高度相关——如果 logical soundness 本身不是 neurosymbolic fact-checking 的可靠标准，这直接支持本文 Symbolic Mirage 假说的一个面向。

---

### 总结

R2 的审稿整体合理。我与 R2 的主要分歧在两点：

1. **W1 (新颖性)**：我认为 R2 低估了本文相对于 Huang/Stechly 的增量贡献——形式化 + sound solver 仍然失败这一发现是 non-trivial 的，Oracle separation result 也是新的。但我同意论文需要在 Related Work 中更清晰地画出区分线。

2. **W4 (frontier 模型)**：我认为 Should-Fix 过重——论文的 structural argument 不依赖于模型规模，且 Limitations 中有诚实声明。但 "architecture-independent" 的措辞确实需要弱化。

其余 W2, W3, W5 (部分), W6, W7 我基本同意。R2 给 3.0 (Findings) 主要基于 novelty 顾虑——如果作者能在 revision 中加强 differentiation 和补充 CLOVER 对比，我认为论文的真实水平在 3.0-3.5 之间，与我的 3.5 (Borderline Conference) 评分方向一致，但我承认 novelty 的精确边界确实存在讨论空间。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。

要点总结：
- R1 的 9 条 Weakness 中我同意 8 条（W1-W9），仅在 Q4（外部信号源）做了部分反驳，在 MR3（Weng et al. 引用不明确）做了反驳
- R1 的统计方法学审查（power analysis、multiple comparisons、CJT rigor）比我的初审更细致，补充了我的盲点
- 结合两份审稿，Soundness 从 3.5 调至 3.0，Overall 维持 3.0 (Findings)
- 两位 reviewer 的关注面互补：R1 聚焦统计方法学，我聚焦新颖性/相关工作覆盖

---

[Reviewer 1 审稿结果]:
交叉审查已提交。与 R2 的核心分歧在两点：(1) 我认为 R2 低估了本文相对于 self-correction/self-verification 文献的增量贡献——形式化到 FOL + sound solver 仍失败以及 Oracle separation result 是 non-trivial 的；(2) frontier 模型缺失不应是 Should-Fix 级别，因为论文的 structural argument 不依赖模型规模。其余 weaknesses（CLOVER 缺失、TF-IDF 粗糙、κ-ICC 映射、引用格式）基本同意。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 702 · 2026-05-20T15:18:11.554469+00:00_

交叉回应已全部收到。两位 Reviewer 的详细逐条回应与我已提交的审稿报告中的共识/分歧判断完全一致——无需修正或重新提交。

**交叉回应关键确认：**

| 议题 | R1 → R2 | R2 → R1 | 报告中状态 |
|------|---------|---------|-----------|
| 统计功效 / "Fail" 过度断言 | — | AGREE | ✅ Must-Fix W1 |
| 多重比较校正 | — | AGREE | ✅ Must-Fix W2 |
| 新颖性 vs Huang/Stechly | REBUT（部分） | — | ✅ 分歧已记录 |
| CLOVER 缺失 | AGREE | — | ✅ Must-Fix W4 |
| CJT/κ 框架 | AGREE | AGREE | ✅ Should-Fix W5 |
| TF-IDF 粗糙 | AGREE | AGREE | ✅ Should-Fix W8 |
| Frontier 模型 | REBUT（结构论证不依赖规模） | — | ✅ 分歧已记录 |
| "Symbolic Mirage" 术语 | REBUT（有技术定义） | — | ✅ 分歧已记录 |

R2 在交叉回应后将 Soundness 从 3.5 下调至 3.0，Overall 维持 3.0。R1 维持 3.5。

审稿报告已投递至 Research Director（Overall: 3.0 Findings），issue tracker 已同步更新（4 条 critical open, 6 条 warning open, 4 条 info open）。圆桌审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 43

## Round 43

64 recorded events


### User

_source line 703 · 2026-05-20T19:49:01.205004+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026 cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 704 · 2026-05-20T19:49:07.499384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 705 · 2026-05-20T19:49:07.700808+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-20T19:49:13.773082+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-20T19:49:13.823633+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-20T19:49:17.537338+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "9"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-20T19:49:17.587947+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-20T19:49:24.294543+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "9"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-20T19:49:24.345221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-20T19:49:29.213127+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-20T19:49:30.568572+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (145 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-wave3-dir-g-decoupling | Decoupling: 将 FOL 约束提取与答案生成解耦——先生成答案 trace，再独立提取 FOL 约束（不暴露答案给约束提取 prompt），可以打破 confirmation bias 因果链。Conservative 策略：截断 trace 中答案相关内容后再提取约束。 | — | — | — |\n\n## 待处理\n- exp-077-generalization-kappa: Generalization: independence bottleneck (high κ) applies to Debate and Diverse-Prompt aggregation, not just SC+SICA. 在 Mistral-7B FOLIO-204 上测量 3 种聚合方式的 Fleiss' κ + Eff-K: (a) Standard SC (复用 exp-033 traces), (b) LLM-Debate traces (4组×3轮=12 answer points), (c) Diverse-Prompt traces (4种 prompt×3次=12). 如果三种方式 κ 均 > 0.4，证明 independence bottleneck 是 same-model aggregation 的通病。（准备中）\n- exp-063-llama8b-folio204（准备中）\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **exp-090-r-nli-proofwriter** (success): Cross-architecture NLI verification (DeBERTa-large-MNLI) 在 ProofWriter-D5 上也能提升 SC accuracy，验证 FOLIO 上 R 方法的跨数据集泛化能力。来源: R5-N4 审稿修复 + Claim 1 (cross-architecture escape generalization)。 ← 基于 exp-wave3-dir-r-nli-verifier\n- **exp-089-oracle-mistral-7b** (success): Mistral-7B的oracle SICA（用FOLIO gold FOL替换自提取FOL）ceiling gap应显著大于Qwen-14B的+14.22pp，因为更弱模型的自提取FOL质量更差，gold FOL替换带来的提升更大。 ← 基于 exp-oracle-folio\n- **exp-wave3
…[truncated 1713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-20T19:49:31.723981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-20T19:49:31.724465+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage{tikz}
18	\usetikzlibrary{arrows.meta,positioning,calc,fit}
19	\usepackage{listings}
20	\usepackage{algorithm}
21	\usepackage{algpseudocode}
22	\usepackage{hyperref}
23	\usepackage{cleveref}
24	
25	\lstset{
26	  basicstyle=\small\ttfamily,
27	  breaklines=true,
28	  frame=single,
29	  xleftmargin=1em,
30	  xrightmargin=1em,
31	  aboveskip=0.5em,
32	  belowskip=0.5em,
33	}
34	
35	\graphicspath{{../figures/paper/}{figures/}}
36	
37	\title{Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints\\Do Not Improve LLM Reasoning}
38	
39	\author{Anonymous}
40	
41	\begin{document}
42	\maketitle
43	
44	\input{abstract}
45	
46	\input{introduction}
47	
48	\input{related_work}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\input{analysis}
55	
56	\input{solutions}
57	
58	\input{discussion}
59	
60	\input{conclusion}
61	
62	\section*{Limitations}
63	\input{limitations_content}
64	
65	\bibliography{references}
66	
67	\appendix
68	\input{appendix}
69	
70	\end{document}
71	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-20T19:49:31.825194+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 717 · 2026-05-20T19:49:32.879850+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 718 · 2026-05-20T19:49:33.081058+00:00_

-rw-r--r-- 1 ubuntu ubuntu 604718 May 20 19:11 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-20T19:49:36.243103+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found search results related to EMNLP 2026 and ARR, but the main conference call for papers doesn't appear in these results. 
…[truncated 1026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4417
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-20T19:49:43.419560+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission deadline guidelines"
  }
}
```

</details>

---


### Tool call

_source line 721 · 2026-05-20T19:49:44.423323+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference paper submission format requirements page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference paper submission format requirements page limit"
  }
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-20T19:49:45.778332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -E \"Pages|Page size\" || pdftotext main.pdf - 2>/dev/null | wc -l",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -E \"Pages|Page size\" || pdftotext main.pdf - 2>/dev/null | wc -l",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool call

_source line 723 · 2026-05-20T19:49:46.531281+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 724 · 2026-05-20T19:49:49.090403+00:00_

Web search results for query: "EMNLP 2026 main conference paper submission format requirements page limit"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the main conference paper submission format requirements and page limits for EMNLP 2026:

**Page Limits:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

**Formatting:**
EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

**Required Sections:**
The mandatory Limitations section is required, placed after the conclusion.

**Submission Process:**
All submissions go through ACL Rolling Review (ARR), with the ARR submission deadline of May 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4667
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-20T19:49:49.550334+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

I found information about ACL Rolling Review (ARR) for May 2026. Here are the key submission deadline guidelines:

## Submission Deadline

The submission deadline is always the 15th of the month, which means the May 2026 ARR submission deadline would be **May 15, 2026**.

## Key Guidelines for ARR Submissions

**Reviewer Participation:**
All submitting authors have to also sign up as reviewers with a deadline of 48 hours after the submission deadline.

**Author Registration:**
Aft
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6130
}
```

</details>

---


### Tool result

_source line 726 · 2026-05-20T19:49:49.684088+00:00_

Pages:           23
Page size:       595.276 x 841.89 pts (A4)
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/review_director_9c155b71

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 3905
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-20T19:49:49.684653+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 115\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet
…[truncated 1461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3153
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-20T19:49:56.951048+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission requirements for EMNLP 2026 main conference papers: page limits (long/short), formatting template, anonymity rules, appendix rules, citation format, submission system (ARR), commitment deadlines, and any other formatting requirements. Be thorough and precise."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission requirements for EMNLP 2026 main conference papers: page limits (long/short), formatting template, anonymity rules, appendix rules, citation format, submission system (ARR), commitment deadlines, and any other formatting requirements. Be thorough and precise."
  }
}
```

</details>

---


### Tool call

_source line 729 · 2026-05-20T19:49:59.259507+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract ALL submission requirements for ACL Rolling Review (ARR): page limits (long/short), formatting requirements, template, anonymity rules, appendix rules, submission deadlines for 2026 cycles, responsible NLP checklist requirements, and any other guidelines. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract ALL submission requirements for ACL Rolling Review (ARR): page limits (long/short), formatting requirements, template, anonymity rules, appendix rules, submission deadlines for 2026 cycles, responsible NLP checklist requirements, and any other guidelines. Be thorough."
  }
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-20T19:50:00.865111+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && for f in abstract.tex introduction.tex related_work.tex method.tex experiments.tex analysis.tex solutions.tex discussion.tex conclusion.tex limitations_content.tex appendix.tex; do if [ -f \"$f\" ]; then lines=$(wc -l < \"$f\"); echo \"$f: $lines lines\"; fi; done",
  "description": "Count lines per section file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && for f in abstract.tex introduction.tex related_work.tex method.tex experiments.tex analysis.tex solutions.tex discussion.tex conclusion.tex limitations_content.tex appendix.tex; do if [ -f \"$f\" ]; then lines=$(wc -l < \"$f\"); echo \"$f: $lines lines\"; fi; done",
    "description": "Count lines per section file"
  }
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-20T19:50:01.567970+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 732 · 2026-05-20T19:50:02.622335+00:00_

# EMNLP 2026 Main Conference Paper Submission Requirements

## Page Limits
- **Long Papers:** 8 pages of content
- **Short Papers:** 4 pages of content
- **Camera-ready versions:** Long papers may extend to 9 pages; short papers to 5 pages to address reviewer feedback

## Submission System & Deadlines
Papers must be submitted through **ACL Rolling Review (ARR)** via the May 2026 cycle. The submission deadline is **May 25, 2026 (11:59 PM UTC-12:00)**. Authors then commit reviewed articles to EMNLP by **August 2, 2026**.

Key requirement: "ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026."

## Anonymity & Review
The reviewing process is double-blind. "Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible."

## Required Content & Policies
Submit papers adhering to all **ARR submission requirements**, including:
- Two-way anonymized review instructions
- Authorship guidelines
- Citation and comparison standards
- Ethics policies (ACL Publication Ethics and ARR Ethics)
- "Responsible NLP research checklist" completion
- Limitations section
- Disclosure policy compliance

## Formatting & Templates
"Paper Submission and Templates" are available via ARR's official guidelines—authors must follow designated formats.

## Supplementary Materials
Optional appendices, software, and data are permitted per ARR policies.

## Author List Modifications
During commitment, author list changes (additions/deletions) are prohibited, though reordering is allowed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 5671
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-20T19:50:13.111849+00:00_

# ACL Rolling Review (ARR) Submission Requirements

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face automatic desk rejection.

## Formatting Requirements

Submissions must adhere to the official ACL style template available on GitHub (acl-org/acl-style-files). Authors must follow ACL's "*ACL" conference formatting guidelines regarding paper size, margins, and font size. Non-compliant submissions are rejected without review.

The document states: "Authors may not modify these style files or use template designed for other conferences."

Appendices must follow double-column formatting with limited exceptions per ACLPUB guidelines. Starting July 2025, non-compliant appendices trigger desk rejection.

## Anonymity Rules

Papers must exclude author names and affiliations. Self-citations should be rewritten: instead of "We previously showed," use "Smith previously showed."

The guidelines note: "Papers should not refer, for further detail, to documents that are not available to the reviewers."

Supplementary materials and repository links must be anonymized. Cloud services tracking downloads (Dropbox, Google Drive) are prohibited; anonymous GitHub repositories are acceptable.

## Limitations Section (Required)

A dedicated "Limitations" section must appear before references without counting toward page limits. This section should discuss work constraints, not introduce new methods, analysis, or results. Omitting this section results in desk rejection.

## Responsible NLP Checklist

All authors must complete the Responsible NLP Research checklist during submission. Incorrect, incomplete, or misleading responses 
…[truncated 2892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 13852
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-20T19:50:13.212720+00:00_

abstract.tex: 8 lines
introduction.tex: 38 lines
related_work.tex: 13 lines
method.tex: 93 lines
experiments.tex: 82 lines
analysis.tex: 84 lines
solutions.tex: 26 lines
discussion.tex: 4 lines
conclusion.tex: 3 lines
limitations_content.tex: 10 lines
appendix.tex: 735 lines
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/review_director_9c155b71

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 12347
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-20T19:50:13.263352+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 11695
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-20T19:50:26.325158+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-20T19:50:26.576991+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-20T19:50:26.727921+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_REVIEW_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-20T19:50:26.778754+00:00_

# Round 1-5 issues (all resolved) — retained for history (abbreviated)
- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
  resolution_round: 3

- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
  resolution_round: 3

- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
  resolution_round: 3

- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
  resolution_round: 2

- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "~48 citations, 5 Related Work paragraphs."
  resolution_round: 3

- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Reframed as regime-dependent analysis with CJT framework."
  resolution_round: 3

- id: "R3-N1"
  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 3
  last_seen_round: 4
  resolution: "Paper Agent added clarifying sentence in method.tex."
  resolution_round: 4

- id: "R3-N2"
  summary: "α value never
…[truncated 11410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-20T19:50:46.715742+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 3 -name \"*.yaml\" -path \"*/symb_invariant*/*\" 2>/dev/null | grep -i config",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 3 -name \"*.yaml\" -path \"*/symb_invariant*/*\" 2>/dev/null | grep -i config",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-20T19:50:46.766781+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-20T19:50:49.932593+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
  "description": "Find top-level config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" 2>/dev/null | head -20",
    "description": "Find top-level config files"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-20T19:50:49.983576+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-20T19:50:52.643529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/workspace.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/workspace.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-20T19:50:52.844668+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-20T19:50:56.627189+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"config*.yaml\" -o -name \"config*.yml\" 2>/dev/null | head -10",
  "description": "Find agent config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -name \"config*.yaml\" -o -name \"config*.yml\" 2>/dev/null | head -10",
    "description": "Find agent config files"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-20T19:50:56.828298+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-20T19:50:59.739341+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -maxdepth 2 -name \"*.yaml\" 2>/dev/null | head -20",
  "description": "Find yaml files in agent directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -maxdepth 2 -name \"*.yaml\" 2>/dev/null | head -20",
    "description": "Find yaml files in agent directory"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-20T19:50:59.789914+00:00_

/home/ubuntu/agent-ml-research/templates/approvals.yaml
/home/ubuntu/agent-ml-research/config/ralph_loop.yaml
/home/ubuntu/agent-ml-research/config/images.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-20T19:51:02.851618+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -20",
  "description": "Find agent state yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -20",
    "description": "Find agent state yaml files"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-20T19:51:02.952477+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-20T19:51:13.641076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-20T19:51:14.143453+00:00_

1	Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
2	We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts first-order logic (FOL) constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
3	Across the full LLM capability range---from Mistral-7B (54\% SC) to Qwen3-14B thinking mode (86\% SC)---and three reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find that self-extracted constraints do not improve majority voting at any capacity level: none of sixteen non-degenerate conditions shows a significant positive effect; TOST equivalence tests (margin $\pm 2$\,pp) establish equivalence for four conditions, while five show genuine SICA--SC differences---four of which are negative.
4	We identify \emph{symbolic confirmation bias} as the root cause: on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC.
5	Process-level analysis reveals a deeper bottleneck: chain-of-thought cosine similarity ($0.69$) far exceeds answer-level Fleiss' $\kappa$ ($0.41$), indicating that traces share reasoning processes even when they diverge on answers.
6	Twenty-plus same-model remediation strategies spanning fifteen families all fail, revealing a persistent independence-accuracy trade-off at the 7B--32B scale: methods that increase trace independence destroy accuracy (Debate: $\kappa = 0.15$, $-18.6$\,pp), while methods preserving accuracy cannot break the correlation floor ($\kappa \geq 0.40$ across three model families).
7	Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp and $+14.22$\,pp on FOLIO, $+11.50$\,pp ProofWriter; $p < 0.001$); same-model self-extraction captures only ${\sim}$12\% of the oracle ceil
…[truncated 360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-20T19:51:14.143794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-20T19:51:14.294687+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding Effective-$K = 1.20$--$3.62$ for nominal $K = 12$: traces beyon
…[truncated 3904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-20T19:51:14.295081+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-20T19:51:14.345505+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-20T19:51:42.326614+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool call

_source line 759 · 2026-05-20T19:51:43.331070+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "symb_invariant_consensus",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 760 · 2026-05-20T19:52:00.746950+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18420
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-20T19:52:00.747412+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 17416
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-20T19:52:00.848198+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**: 2026-05-25\n- **类型**: Long paper（正文 ≤8 页，参考文献无限，Limitations 必须有且不计入页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录**: 允许，双栏格式，不参与主要审稿评分但 Reviewer 可参考\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n### 论文概要\n负面结果论文：研究 LLM 自提取 FOL 约束能否改善 Self-Consistency majority voting。结论是不能——因为 symbolic confirmation bias（错误问题上 83.3% 的自提取约束支持错误多数答案）和 trace 相关性（cosine similarity 0.69 远超 answer-level κ 0.41）。测试了 6 个模型（7B-32B）、3 个推理域、3000+ 条件评估。20+ remediation strategies 均失败，但 cross-architecture DeBERTa NLI verifier 有正向信号。\n\n### 你的审查重点\n1. **SICA pipeline 方法论**：FOL 提取、Z3 weighted partial MAX-SAT、α 权重设计——是否严谨、有无技术漏洞\n2. **统计分析**：TOST 等价性检验、Bootstrap CI、Benjamini-Hochberg 多重比较校正——是否正确应用、sample size 是否足够\n3. **实验设计**：6 模型 × 3 域的覆盖度、seed replication、oracle controls 的内部效度\n4. **Remediation strategies**：20+ 策略的分类和评估——是否公平、有无遗漏关键 baseline\n5. **Cross-architecture PoC**：DeBERTa NLI 实验的统计可靠性（仅 ProofWriter 数据？FOLIO 是否也有？）\n6. **可复现性**：数据量、超参数、随机种子是否充分报告\n\n### 评分标准 (EMNLP 2026 ARR)\n5 = Consider for Award（~前2.5%）| 4.5 = Borderline Award | 4 = Conference | 3.5 = Borderline Conference | 3 = Findings | 2.5 = Borderline Findings | 2 = Resubmit next cycle | 1.5 = Resubmit after next cycle | 1 = Do not resubmit\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需要作者澄清的）\n5. Missing References（如有）\n6. Overall Assessment（评分 + 置信度 high/medium/low）\n7. Detailed Comments（逐节意见）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**: 2026-05-25\n- **类型**: Long paper（正文 ≤8 页，参考文献无限，Limitations 必须有且不计入页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录**: 允许，双栏格式，不参与主要审稿评分但 Reviewer 可参考\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n### 论文概要\n负面结果论文：研究 LLM 自提取 FOL 约束能否改善 Self-Consistency majority voting。结论是不能——因为 symbolic confirmation bias（错误问题上 83.3% 的自提取约束支持错误多数答案）和 trace 相关性（cosine similarity 0.69 远超 answer-level κ 0.41）。测试了 6 个模型（7B-32B）、3 个推理域、3000+ 条件评估。20+ remediation strategies 均失败，但 cross-architecture DeBERTa NLI verifier 有正向信号。\n\n### 你的审查重点\n1. **SICA pipeline 方法论**：FOL 提取、Z3 weighted partial MAX-SAT、α 权重设计——是否严谨、有无技术漏洞\n2. **统计分析**：TOST 等价性检验、Bootstrap CI、Benjamini-Hochberg 多重比较校正——是否正确应用、sample size 是否足够\n3. **实验设计**：6 模型 × 3 域的覆盖度、seed replication、oracle controls 的内部效度\n4. **Remediation strategies**：20+ 策略的分类和评估——是否公平、有无遗漏关键 baseline\n5. **Cross-architecture PoC**：DeBERTa NLI 实验的统计可靠性（仅 ProofWriter 数据？FOLIO 是否也有？）\n6. **可复现性**：数据量、超参数、随机种子是否充分报告\n\n### 评分标准 (EMNLP 2026 ARR)\n5 = Consider for Award（~前2.5%）| 4.5 = Borderline Award | 4 = Conference | 3.5 = Borderline Conference | 3 = Findings | 2.5 = Borderline Findings | 2 = Resubmit next cycle | 1.5 = Resubmit after next cycle | 1 = Do not resubmit\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需要作者澄清的）\n5. Missing References（如有）\n6. Overall Assessment（评分 + 置信度 high/medium/low）\n7. Detailed Comments（逐节意见）"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-20T19:52:17.452904+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16604
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-20T19:52:17.704394+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + Related Work + 写作质量**\n\n### 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**: 2026-05-25\n- **类型**: Long paper（正文 ≤8 页，参考文献无限，Limitations 必须有且不计入页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录**: 允许，双栏格式，不参与主要审稿评分但 Reviewer 可参考\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n### 论文概要\n负面结果论文：研究 LLM 自提取 FOL 约束能否改善 Self-Consistency majority voting。结论是不能——因为 symbolic confirmation bias（错误问题上 83.3% 的自提取约束支持错误多数答案）和 trace 相关性（cosine similarity 0.69 远超 answer-level κ 0.41）。测试了 6 个模型（7B-32B）、3 个推理域、3000+ 条件评估。20+ remediation strategies 均失败，但 cross-architecture DeBERTa NLI verifier 有正向信号。\n\n### 你的审查重点\n1. **新颖性（Novelty）**：\n   - 相对于 Huang et al. (2024 self-correction)、Stechly et al. (2025 self-verification)、Amonkar et al. (EMNLP 2025) 等\"LLM 不能自我纠正\"文献，本文有多少增量贡献？\n   - \"symbolic confirmation bias\"和\"independence-accuracy trade-off\"概念是否真正新颖？\n   - CJT 框架应用于 LLM trace 分析——是否已有类似工作？\n2. **Related Work 覆盖度**：\n   - 是否遗漏重要相关工作？特别是：neuro-symbolic reasoning（CLOVER, VERGE, LogicAgent, DyLoS, Aristotle, FOVER）、self-consistency 变体（USC, CISC）、ensemble diversity（Krogh & Vedelsby 1994, Brown et al. 2005）\n   - 2025-2026 年的最新工作是否被充分覆盖？\n3. **Negative paper 叙事逻辑**：\n   - 论文是否convincingly 论证了\"为什么这个负面结果值得发表\"？\n   - 贡献声明是否与实际内容匹配？是否有 overclaim？\n   - Discussion/Conclusion 是否为社区提供了可行的 forward-looking insights？\n4. **写作质量**：\n   - 结构是否合理（8 页正文的信息密度）？\n   - 术语一致性、符号定义完整性\n   - 图表是否有效传达信息？\n5. **格式合规性**：\n   - 正文是否 ≤8 页？Limitations 是否存在？\n   - 引用格式、匿名性\n   - Responsible NLP checklist 相关内容\n\n### 评分标准 (EMNLP 2026 ARR)\n5 = Consider for Award（~前2.5%）| 4.5 = Borderline Award | 4 = Conference | 3.5 = Borderline Conference | 3 = Findings | 2.5 = Borderline Findings | 2 = Resubmit next cycle | 1.5 = Resubmit after next cycle | 1 = Do not resubmit\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需要作者澄清的）\n5. Missing References（如有）\n6. Overall Assessment（评分 + 置信度 high/medium/low）\n7. Detailed Comments（逐节意见）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + Related Work + 写作质量**\n\n### 投稿信息\n- **Venue**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**: 2026-05-25\n- **类型**: Long paper（正文 ≤8 页，参考文献无限，Limitations 必须有且不计入页数）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **附录**: 允许，双栏格式，不参与主要审稿评分但 Reviewer 可参考\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n\n### 论文概要\n负面结果论文：研究 LLM 自提取 FOL 约束能否改善 Self-Consistency majority voting。结论是不能——因为 symbolic confirmation bias（错误问题上 83.3% 的自提取约束支持错误多数答案）和 trace 相关性（cosine similarity 0.69 远超 answer-level κ 0.41）。测试了 6 个模型（7B-32B）、3 个推理域、3000+ 条件评估。20+ remediation strategies 均失败，但 cross-architecture DeBERTa NLI verifier 有正向信号。\n\n### 你的审查重点\n1. **新颖性（Novelty）**：\n   - 相对于 Huang et al. (2024 self-correction)、Stechly et al. (2025 self-verification)、Amonkar et al. (EMNLP 2025) 等\"LLM 不能自我纠正\"文献，本文有多少增量贡献？\n   - \"symbolic confirmation bias\"和\"independence-accuracy trade-off\"概念是否真正新颖？\n   - CJT 框架应用于 LLM trace 分析——是否已有类似工作？\n2. **Related Work 覆盖度**：\n   - 是否遗漏重要相关工作？特别是：neuro-symbolic reasoning（CLOVER, VERGE, LogicAgent, DyLoS, Aristotle, FOVER）、self-consistency 变体（USC, CISC）、ensemble diversity（Krogh & Vedelsby 1994, Brown et al. 2005）\n   - 2025-2026 年的最新工作是否被充分覆盖？\n3. **Negative paper 叙事逻辑**：\n   - 论文是否convincingly 论证了\"为什么这个负面结果值得发表\"？\n   - 贡献声明是否与实际内容匹配？是否有 overclaim？\n   - Discussion/Conclusion 是否为社区提供了可行的 forward-looking insights？\n4. **写作质量**：\n   - 结构是否合理（8 页正文的信息密度）？\n   - 术语一致性、符号定义完整性\n   - 图表是否有效传达信息？\n5. **格式合规性**：\n   - 正文是否 ≤8 页？Limitations 是否存在？\n   - 引用格式、匿名性\n   - Responsible NLP checklist 相关内容\n\n### 评分标准 (EMNLP 2026 ARR)\n5 = Consider for Award（~前2.5%）| 4.5 = Borderline Award | 4 = Conference | 3.5 = Borderline Conference | 3 = Findings | 2.5 = Borderline Findings | 2 = Resubmit next cycle | 1.5 = Resubmit after next cycle | 1 = Do not resubmit\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/warning/info）\n4. Questions（需要作者澄清的）\n5. Missing References（如有）\n6. Overall Assessment（评分 + 置信度 high/medium/low）\n7. Detailed Comments（逐节意见）"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-20T19:52:18.962024+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1257
}
```

</details>

---


### Assistant

_source line 766 · 2026-05-20T19:52:31.445901+00:00_

全部派发完成：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动（与 Reviewer 并行） |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 已发送到用户群（8h 后自动提醒） |
| Reviewer 1（方法 + 实验） | ✅ 已派发 |
| Reviewer 2（新颖性 + 完整性） | ✅ 已派发 |

等待两位 Reviewer 返回初审意见，收到后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 767 · 2026-05-20T19:58:44.395990+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 1 审稿意见

### 1. Summary

本文是一篇负面结果论文，研究 LLM 自提取 FOL 约束能否通过 Symbolic Invariant Consensus Aggregation (SICA) 改善 Self-Consistency majority voting。核心发现是不能——原因是 **Symbolic Mirage**：自提取约束继承了生成模型的 confirmation bias（错误问题上 83.3% 的约束支持错误多数答案，BR ≈ 1.97+），且 trace 之间的 process-level 相关性（cosine similarity 0.69）远超 answer-level 独立性（Fleiss' κ ≈ 0.41）。论文测试了 6 个模型（7B-32B）、6 个数据集、3000+ 条件评估，25+ 补救策略均失败，但 cross-architecture DeBERTa NLI verifier 在 ProofWriter 上显示正向信号。

---

### 2. Strengths

**S1. 研究问题重要且动机充分。** 论文从 CJT（Condorcet Jury Theorem）框架出发，严格推导了 SC 的理论瓶颈（独立性假设违反，Eq. 1: K_eff = 1+(K−1)·κ），然后自然引出"约束提取能否打破此瓶颈"的问题。这是一个合理且社区关心的问题。

**S2. 实验规模和覆盖度出色。** 6 个模型（Mistral-7B, Qwen2.5-7B/14B, Qwen3-14B, LLaMA-3.1-8B, QwQ-32B）× 6 个数据集（FOLIO, ProofWriter, LogiQA, StrategyQA, GSM8K, AIME）覆盖了逻辑推理、常识推理和数学推理三个领域，涵盖高/中/低 SC 准确率区间（Type A/B/C）。这种系统性覆盖在负面结果论文中罕见。

**S3. Oracle controls 设计巧妙。** §4.3 用 FOLIO gold FOL 和 ProofWriter DSL 做 oracle SICA，结果 oracle 显著提升（+29.0pp Mistral-7B FOLIO, +14.22pp Qwen-14B FOLIO, +11.50pp ProofWriter），证明 MAX-SAT 聚合机制本身是 sound 的——问题在于自提取约束质量。这将 blame 精确定位到提取环节。

**S4. 统计方法论严谨。** 使用了 TOST 等价性检验（±2pp margin）、Bootstrap 95% CI（10,000 resamples）、Benjamini-Hochberg 多重比较校正、McNemar exact test、统计功效分析（MDE at 80% power）。这在 NLP 论文中超出平均水准。

**S5. Symbolic Mirage 概念及 BR 指标有独立贡献价值。** Bias Ratio（§3.3）量化了自提取约束对模型错误的 confirmation bias 程度，C_D diagnostic 揭示了约束的非判别性。这些工具可被后续工作直接复用。

**S6. 补救策略的系统性搜索令人信服。** 25+ 策略覆盖 prompt-level（9）、method-level（3）、additional directions（11+），Figure 5 的可视化总结清晰直观。这种穷举式探索大幅增强了负面结论的可信度。

**S7. 建设性结论——cross-architecture escape。** 论文没有止步于"不行"，而是通过 DeBERTa NLI 证明外部验证器可以部分恢复 oracle gap，为后续研究指明方向。

---

### 3. Weaknesses

**N1 [critical] FOL 提取质量未充分表征，核心术语有误导性**

- 具体位置：§3.2, Appendix B (prompts), Limitations §Y (p21 lines 1573-1577)
- 问题：论文通篇使用 "first-order logic (FOL) constraints" 描述提取结果，但 Limitations 明确承认提取出的约束"predominantly propositional ground clauses without quantifiers"（p21, l.1573-1575），即绝大多数是命题逻辑而非真正的一阶逻辑。数学域的 EXTRACTION_PROMPT（Appendix B）提取的是 equation/inequality/comparison，同样不涉及量词。论文未报告实际含量词（∀, ∃）约束的比例。
- 为什么影响接收：如果提取的"FOL"几乎全是 propositional ground clauses，则负面结论应限定为"propositional self-extraction 无效"，而非暗示 FOL 层面的自提取也无效。标题和 abstract 中的 "symbolic constraints" 比 "FOL constraints" 更准确。这个术语偏差可能误导读者对 FOL 方法的判断。
- 建议：(1) 报告含量词约束的比例（按域/模型分组）；(2) 将 "FOL constraints" 统一改为 "symbolic constraints" 或 "logical constraints"，仅在 ProofWriter/FOLIO 上下文中使用 "propositional/ground logic"；(3) 在 Discussion 中明确讨论"真正的 FOL 提取是否可能改变结论"。

**N2 [critical] Cross-architecture PoC 仅使用单一生成模型，泛化性不足**

- 具体位置：§6 (p8), Table 13 (p18)
- 问题：DeBERTa NLI combo 实验全部基于 Mistral-7B 生成的 traces。但 Table 1 和 §O (Failure Mode Analysis) 清楚表明不同模型有截然不同的行为模式（Type A confirmation bias vs. Type B non-formalizable vs. Type C error amplification）。在仅一个生成模型上的正向结果无法支撑"cross-architecture verification is the escape"这一结论。
- 为什么影响接收：这是论文唯一的正向结论（constructive contribution），如果不够可靠，论文的贡献仅剩"it doesn't work"，对社区的指导价值大幅降低。
- 建议：至少增加一个 Qwen 家族模型（如 Qwen2.5-14B，Type A 模型）的 NLI combo 实验。如果时间不允许全面实验，至少在 ProofWriter 上做一个条件，展示 cross-architecture escape 在不同生成模型上的趋势。

**W1 [warning] 种子复制不一致，影响结果可靠性**

- 具体位置：Table 1 (p6), Appendix M (p16-17)
- 问题：Appendix M 的 K-sensitivity 分析使用 4 seeds（仅 Mistral-7B FOLIO），温度敏感性分析也仅覆盖 Mistral-7B FOLIO。但 Table 1 中大多数条件看起来只使用了 default seed（seed 0.7 mentioned in §4.1）。论文在 Appendix V (TOST) 中承认 6/15 non-degenerate 条件 underpowered。
- 影响：对于声称"没有任何条件显示显著正效果"的全局负面结论，单 seed 实验的 stochasticity 可能掩盖真实效果。
- 建议：(1) 在 Table 1 中标注每个条件的 seed 数量；(2) 在 main text 中明确说明哪些结论基于 multi-seed，哪些基于 single-seed；(3) 对 underpowered 条件降低 claim strength。

**W2 [warning] 语义去重缺失可能扭曲 MAX-SAT 权重分布**

- 具体位置：§3.2 (p3-4), Limitations §Y (p21, l.1578-1579)
- 问题：约束去重使用 syntactic equivalence（完全字符串匹配），语义等价但表面形式不同的约束获得独立权重。论文 Limitations 承认此问题但未量化影响。例如 `x > 5` 和 `5 < x` 会被视为不同约束。
- 影响：这可能系统性地放大 verbose traces 的权重，进一步加剧 confirmation bias（因为错误 traces 可能产生更多同义约束变体）。
- 建议：(1) 报告去重前后的平均约束数量和唯一约束率；(2) 用 Z3 equivalence checking 做一次 semantic deduplication 的 ablation，检查是否影响 BR 指标。

**W3 [warning] 域多样性的表述需要校准**

- 具体位置：Abstract, §1 (p1), §4.1 (p4)
- 问题：论文声称覆盖"three reasoning domains"（abstract l.4）。但 FOLIO 和 ProofWriter 都是形式逻辑推理（前者 FOL，后者 DSL），LogiQA 是逻辑理解但偏自然语言，StrategyQA 是常识推理，GSM8K/AIME 是数学推理。然而主要实验集中在 FOLIO + ProofWriter（Table 1 的绝大多数行），数学域仅有 GSM8K pilot (n=30) 和 AIME degenerate case，实际覆盖不均衡。
- 影响：数学推理（GSM8K, AIME）的条件全部是 degenerate（SC ≥ 85%，约束退化为加权投票），无法检验 SICA 在数学中间难度区间的表现。
- 建议：(1) 明确说明主要结论的适用域是 formal/logical reasoning；(2) 如果 GSM8K 有 intermediate-SC 条件（比如在更弱的模型上），补充实验。

**W4 [warning] 约束质量分析的覆盖范围有限**

- 具体位置：Appendix L (p16, Extraction Error Taxonomy)
- 问题：Appendix L 的 extraction error taxonomy 基于 N=804（Qwen2.5-14B on FOLIO + ProofWriter），仅覆盖一个模型家族两个域。91.8% 的约束被报告为 "technically discriminative"，但这个比例在其他模型/域上可能不同（尤其是 Type C error amplification 模型如 Mistral-7B on ProofWriter，§O 报告 "correct reasoning steps become discriminative signals that the solver mistakenly penalizes"）。
- 建议：将 extraction error taxonomy 扩展到至少 2-3 个模型，验证 91.8% 的 discriminative rate 是否 robust。

**W5 [info] Figure 2 (p7) 回归分析解读需谨慎**

- 具体位置：Figure 2, §5.3 (p6-7)
- 问题：Figure 2 展示 CoT cosine similarity vs. answer agreement，并拟合线性回归 (r=0.21, p=0.011)。但散点图显示数据高度集中在特定区域，regression 的 R² 极低（~4.4%），positive correlation 主要由少数离群点驱动（Qwen-14B 的几个条件）。
- 建议：说明 R² 值，讨论离群点影响，或改用 rank correlation（Spearman）。

---

### 4. Questions for Authors

**Q1.** 实际提取的约束中，含一阶量词（∀, ∃）的比例是多少？按域和模型分组报告。（对应 N1）

**Q2.** 是否测试过在 Qwen 或 LLaMA 家族模型上运行 DeBERTa NLI combo？如果没有，是因为时间/计算资源限制还是有其他原因？（对应 N2）

**Q3.** 83.3% 的 confirmation bias 率（§3.3, §5.2）是在所有模型上的均值还是特定条件？这个比率在 Type A / Type B / Type C 模型上的分布如何？

**Q4.** Syntactic deduplication 后，平均每个问题保留多少个唯一约束？去重前后的约束数量比是多少？（对应 W2）

**Q5.** 对于 TOST 中 6 个 underpowered 条件（Appendix V），需要多大的样本量才能达到 80% power at ±2pp margin？

**Q6.** §4.1 提到 Z3 solving 占 wall-clock time 的 76%——如果用更高效的 SAT solver（如 Open-WBO），是否可能扩展到更大规模实验？这是一个 scalability concern。

---

### 5. Missing References

未发现关键缺失引用。参考文献覆盖了 SC、CJT、neuro-symbolic reasoning、LLM self-verification 的核心工作。

可选建议增加：
- Lightman et al. (2024) "Let's Verify Step by Step" — process reward model 作为外部验证的相关工作，与 §6 cross-architecture 思路相关（虽然论文已 cite 了 Toh et al. 2024 的 step-wise verification）
- Ling et al. (2024) 或其他关于 LLM self-refinement 局限性的综述，可加强 Symbolic Mirage 与 broader self-correction 失败的联系

---

### 6. Overall Assessment

**Overall: 3.5 — Borderline Conference**
**Confidence: 4/5 (High)**

**一句话总结：** 方法论严谨、实验规模可观的负面结果论文，但核心术语（FOL vs. propositional）有误导性，唯一的建设性贡献（cross-architecture PoC）仅覆盖单一生成模型，削弱了整体指导价值。

**评分理由：**
- 这是一篇高质量的负面结果论文，Symbolic Mirage 概念有独立贡献价值，25+ 策略的系统性搜索令人信服
- 统计方法论（TOST + Bootstrap CI + Power Analysis + BH）在 NLP 会议论文中属于上乘
- 但两个 critical issues 限制了接收：(1) FOL 术语误导使负面结论的 scope 不清晰——读者无法判断"真正的 FOL 提取"是否也会失败；(2) cross-architecture PoC 的 single-generator 限制使正向结论的泛化性不足
- 如果 N1 和 N2 能在 camera-ready 前解决（N1 是 reframing + 补充分析，N2 至少需要一个额外模型的实验），可以提升到 4.0

---

### 7. Official Dimension Scores (ACL ARR Review Form)

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心实验方法论扎实，统计分析严谨；但 FOL 术语偏差和 syntactic dedup 问题降低了部分 claim 的准确性 |
| Excitement | 3/5 | 负面结果对社区有价值（ARR guidelines 明确保护），Symbolic Mirage 概念有新意；但 confirmation bias 的"why"在事后看来较直觉，cross-architecture escape 开发不足 |
| Reproducibility | 4/5 | 超参数、prompts、实验设置报告充分；承诺代码/数据公开；种子复制不一致是主要扣分项 |
| Overall Assessment | 3.5/5 | Borderline Conference — 距离 Findings 有余，距离 Main 稍欠 |

---

### 8. Detailed Comments by Section

**§1 Introduction (p1-2):**
- 动机清晰，从 CJT independence bottleneck 到 symbolic constraint extraction 的逻辑链条流畅
- Contributions 列表（p2）的 3 点概括准确
- "FOL constraints" 在 intro 中首次出现（l.3），应在此处即明确约束的实际 formalism 层级

**§2 Related Work (p2-3):**
- 覆盖充分，分 SC/extensions、Neuro-symbolic reasoning、Test-time compute 三个子节
- 将本文定位为"negative result that CJT violations are persistent"较准确

**§3 Background & Setup (p3-4):**
- §3.1 CJT 框架严谨，K_eff 公式引用正确
- §3.2 SICA pipeline 描述清楚，Algorithm 1（Appendix C）补充了实现细节
- §3.3 Symbolic Mirage 和 BR 指标定义清晰；但 C_D 的"zero-valued diagnostic"表述可以更精确——是 C_D ≈ 0 还是严格 C_D = 0？

**§4 Experiments (p4-5):**
- Table 1 信息密度高，但建议增加 seed 数量列
- §4.2 的 Type A/B/C regime 分类是有用的组织框架
- §4.3 Oracle control 是论文最强的 positive control，结果令人信服

**§5 Analysis (p5-7):**
- §5.1 Condorcet Effective-K 分析是扎实的理论贡献
- §5.2 Symbolic Confirmation Bias 的 83.3% 数据来源需要更透明（Q3）
- §5.3 Process-Level Independence 用 TF-IDF cosine similarity 是合理的 proxy，但应讨论其局限（surface-level similarity vs. reasoning structure）
- §5.4 25+ remediation strategies 的 Figure 5 总结非常好

**§6 Cross-Architecture PoC (p7-8):**
- 方法设计合理（encoder-only NLI as external verifier）
- 但 single-generator (Mistral-7B) 和 limited datasets (FOLIO + ProofWriter) 严重限制了结论强度
- α sensitivity 分析简略——为什么 α=3 或 α=5 是合理的？缺乏原则性的选择方法

**§7 Discussion (p8):**
- "driver limits voting diversity" vs. "indirect collapse" 的两通道分析简洁有力
- Figure 7 (independence-accuracy trade-off) 是论文最有洞察力的图之一

**§8 Conclusion (p8):**
- 恰当地总结了负面发现和正向逃逸路线
- "Detecting the Symbolic Mirage in other self-verification domains is a critical open direction" 是有价值的 future work

**Limitations (p9, §Y p20-21):**
- 诚实且全面，覆盖了模型规模、域限制、FOL formalism、deduplication 等
- Extended Limitations (§Y) 补充了额外 limitations 但部分内容（如 "alternative extraction temperatures might yield different results"）在 main Limitations 中已有覆盖，有冗余

**Appendices:**
- 总体质量高，Appendix C (Z3 pseudocode)、D (capability trap diagnostics)、E (power analysis)、G (case studies) 特别有价值
- Appendix 数量（A-Y, 25 个）略显过多，部分可以合并（如 M1+M2 合并为一个 sensitivity 节）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 768 · 2026-05-20T19:58:55.048278+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），2 个 critical + 3 个 warning。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 769 · 2026-05-20T19:59:09.970730+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿完成。

**评分：Overall 3.5 (Borderline Conference)，Confidence 4/5 (High)**

核心判断：方法论严谨、实验规模出色的负面结果论文，Symbolic Mirage 概念和 BR 指标有独立贡献价值，25+ 补救策略的系统搜索令人信服。但两个 critical issues 限制接收：

1. **FOL 术语误导**（N1）：实际提取的约束以 propositional ground clauses 为主，非真正 FOL，导致负面结论的 scope 不清晰
2. **Cross-architecture PoC 泛化性不足**（N2）：仅在 Mistral-7B 一个生成模型上测试 DeBERTa NLI combo，论文中已展示不同模型有截然不同的行为模式（Type A/B/C），单模型 PoC 无法支撑通用结论

若 N1（reframing + 量词比例分析）和 N2（至少补一个 Qwen 模型实验）能解决，可提升至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 770 · 2026-05-20T19:59:16.253094+00:00_

Reviewer 1 审稿收到，评分 3.5 (Borderline Conference)。2 个 critical + 3 个 warning + 1 个 info。等待 Reviewer 2 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 46

## Round 46

6 recorded events


### User

_source line 771 · 2026-05-20T19:59:36.430343+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**审查侧重：新颖性 + 完整性 + Related Work + 写作质量**

---

### 1. Summary

本文研究 LLM 自提取的 FOL 约束能否通过 Symbolic Invariant Consensus Aggregation (SICA) 改善 Self-Consistency (SC) majority voting。结论是否定的——在 6 个模型（7B–32B）、3 个推理域、3000+ 条件评估中，自提取约束未能显著提升准确率。作者将此归因于 "Symbolic Mirage"：自提取约束是模型分布偏差的投射而非独立验证信号，表现为 symbolic confirmation bias（错误问题上 83.3% 的约束支持错误多数答案）、高 trace 相关性（cosine similarity 0.69 vs. answer-level κ 0.41）、以及有效独立样本量的压缩。20+ 种补救策略均失败，但跨架构 DeBERTa NLI verifier 显示初步正向信号。

### 2. Strengths

**S1. 实验方法论严谨，统计分析扎实。** 采用 TOST 等价性检验（§4.2）而非仅依赖 NHST 来确认负面结果，Bootstrap CI（Appendix F）和统计功效分析（Appendix E）进一步加固结论可信度。

**S2. 全面的补救策略扫描（§5.4, Table 9–10, Figure 5）。** 系统测试 23 种策略全部中性至负面，防止社区重复探索死胡同。

**S3. CJT 框架提供原理性诊断工具。** 从 κ（Fleiss' kappa）到 Effective-K 再到 Bias Ratio 的量化链条（§3.1–3.3）使 SC 失效模式诊断从定性变为定量。

**S4. Independence-Accuracy Trade-off（Figure 7）是本文最具洞察力的贡献。** 清晰展示同模型方法（κ ≈ 0.40–0.47）、跨模型 SC（κ = 0.41–0.74）、Debate（κ = 0.15）的 Pareto 关系。

**S5. Oracle 分析（§4.3）有效分离了机制问题和提取质量问题。** 确认 SICA 聚合机制本身 sound，瓶颈在自提取质量。

**S6. 写作结构清晰，叙事逻辑连贯。** 从假设建立 → 主实验否定 → 三重诊断 → 补救失败 → 跨架构出口 → 讨论，形成完整叙事弧。

**S7. 格式合规性好。** 正文 8 页，Limitations 不计入页数，双盲匿名，行号完整，引用 48 条无遗漏无孤立。

### 3. Weaknesses

**W1 [warning] 核心发现的增量新颖性有限。**
- 位置：§1, §7
- Huang et al. (2024) 已论证 LLMs 不能 self-correct；Stechly et al. (2025) 证明 self-verification 局限；Amonkar et al. (2025) 研究 LLM formalization 质量；Chan et al. (2026) 论证 logical soundness 不是可靠验证标准。本文核心洞察在概念层面已被覆盖，具体化到 FOL + SC 组合的跳跃不大。
- 建议：更突出论述 "FOL 的形式化语义给了 Z3 一个确定性验证通道，使 symbolic self-verification 有额外 escape hatch——本文证明这个 escape hatch 也失败了" 这一论点（目前隐含于§3.3）。

**W2 [warning] DeBERTa NLI proof-of-concept（§6）结论不一致。**
- 位置：§6, Table 1, Figure 3
- FOLIO 上 +2.94 pp（n.s.），但 ProofWriter 上 SICA 本身 significantly hurts（−2.83 pp, p = 0.014）。两个数据集方向相反且 FOLIO 改善不显著，使 "cross-architecture verification is the way forward" 的结论缺乏充分支撑。combo α=3 在 FOLIO 204 样本上的选择存在 overfitting 风险。
- 建议：增加数据集验证泛化性；更诚实地讨论 ProofWriter 上的 degradation；明确标注为 preliminary signal。

**W3 [warning] "Symbolic Confirmation Bias" 缺乏与 existing frameworks 的深度对接。**
- 位置：§5.2, §3.3
- BR = 1.97 的现象在本质上是 Turpin et al. (2024) unfaithful CoT explanations 在 FOL 层面的投射。论文在 Discussion 引用了 Turpin 但未在定义时建立联系。
- 建议：在§3.3 明确讨论与 unfaithful explanations 的关系。

**W4 [warning] 模型覆盖范围与 Abstract 措辞不匹配。**
- 位置：Abstract, §4.1
- Abstract 称 "across the full LLM capability range" 但实际仅覆盖开源 7B–32B。Frontier 模型（GPT-4o, Claude 3.5）的 FOL 提取质量可能有质的提升。
- 建议：修改 Abstract 为 "across a range of open-source LLMs (7B–32B)"。

**W5 [info] Table 1 中部分条件统计功效不足。**
- 7 个条件（n ≤ 60）的 MDE 为无穷大。Table 1 未区分 adequately powered vs. exploratory conditions。
- 建议：用 † 标记 n < 100 的行。

**W6 [info] 附录过于庞大（13 页 vs. 8 页正文），关键图表（尤其 Figure 5）应考虑移入正文。**

### 4. Questions

**Q1.** 如果在 FOLIO gold annotations 上 fine-tune 一个专门的 FOL extractor，能否显著提升 discriminative rate？这一 ablation 能更精确定位 extraction quality vs. inherent limitation 的边界。

**Q2.** Figure 7 的 independence-accuracy trade-off 是否存在 CJT-based 的理论下界？

**Q3.** DeBERTa NLI 在 ProofWriter 上 degradation 的根本原因？

**Q4.** TF-IDF 是否能充分捕获 trace 语义相似性？是否考虑过 sentence embedding？

**Q5.** Syntactic vs. semantic deduplication 的影响有多大？有无 ablation？

### 5. Missing References

- **Weng et al. (2023)** "Large Language Models are Better Reasoners with Self-Verification" — self-verification positive result，应在 Related Work 中作为对比讨论。
- **Kadavath et al. (2022)** "Language Models (Mostly) Know What They Know" — LLM 自评估/calibration 基础工作。
- **Madaan et al. (2023)** "Self-Refine: Iterative Refinement with Self-Feedback" — self-refinement 代表工作，论文引用了 Huang et al. 的反驳但未引用原始工作。

### 6. Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 方法论严谨，统计分析质量高（TOST、bootstrap CI、power analysis），oracle 分析有效分离机制与质量。扣分：部分条件功效不足，DeBERTa 结论不一致 |
| Excitement | 2.5/5 | 实验全面、写作好，但核心发现在概念层面已被 Huang/Stechly/Amonkar/Chan 覆盖。CJT 框架和 independence-accuracy trade-off 有一定新颖性但不足以达到 main conference |
| Reproducibility | 4/5 | 详细 prompt templates、算法伪代码、完整参数。承诺发布代码。扣分：未分析 Z3 超时对不同规模问题的影响 |
| Overall | **3.0 (Findings)** | 方法论扎实、实验全面的负面结果论文，CJT 框架有价值，但核心洞察增量新颖性有限，建议 Findings |
| Confidence | 4/5 | 熟悉 self-consistency、neuro-symbolic reasoning 和 LLM self-verification 领域 |

**一句话总结：** 方法论扎实的负面结果论文，CJT 框架和 23 种策略扫描对社区有参考价值，但核心洞察相对于已有 self-verification failure 文献的增量新颖性有限，建议 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-20T19:59:59.822774+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 交叉分享 — 请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall: 3.0 (Findings)，Confidence 4/5**\n\n**Strengths:**\nS1. 统计分析扎实（TOST + Bootstrap CI + Power Analysis）\nS2. 23种补救策略扫描防止社区重复探索死胡同\nS3. CJT 框架提供原理性诊断工具（κ → Eff-K → BR）\nS4. Independence-Accuracy Trade-off（Figure 7）最具洞察力\nS5. Oracle 分析有效分离机制与提取质量\nS6. 写作结构清晰，叙事逻辑连贯\nS7. 格式合规\n\n**Weaknesses:**\n\nW1 [warning] 核心发现的增量新颖性有限。\n- Huang et al. (2024) 已论证 LLMs 不能 self-correct；Stechly et al. (2025) 证明 self-verification 局限；Amonkar et al. (2025) 研究 LLM formalization 质量；Chan et al. (2026) 论证 logical soundness 不是可靠验证标准。本文核心洞察在概念层面已被覆盖。\n- 建议：更突出 \"FOL 的形式化语义给了 Z3 一个确定性验证通道，本文证明这个 escape hatch 也失败了\"。\n\nW2 [warning] DeBERTa NLI PoC 结论不一致。\n- FOLIO +2.94pp (n.s.)，ProofWriter SICA 本身 −2.83pp (p=0.014)。两个数据集方向相反。combo α=3 在 FOLIO 204 样本上有 overfitting 风险。\n- 建议：增加数据集，更诚实讨论 degradation，标注为 preliminary signal。\n\nW3 [warning] \"Symbolic Confirmation Bias\" 缺乏与 Turpin et al. (2024) unfaithful CoT 的深度对接。\n\nW4 [warning] Abstract \"across the full LLM capability range\" 但实际仅 7B–32B 开源模型。\n\nW5 [info] Table 1 中 7 个条件 n ≤ 60，MDE 无穷大，未区分 powered vs. exploratory。\n\nW6 [info] 附录 13 页 vs. 正文 8 页，Figure 5 应考虑移入正文。\n\n**Questions:**\nQ1. Fine-tune 专门 FOL extractor 能否提升 discriminative rate？\nQ2. Figure 7 trade-off 是否有 CJT-based 理论下界？\nQ3. DeBERTa NLI 在 ProofWriter 上 degradation 的根本原因？\nQ4. TF-IDF 是否能充分捕获 trace 语义相似性？\nQ5. Syntactic vs. semantic deduplication 影响多大？\n\n**Missing References:**\n- Weng et al. (2023) \"LLMs are Better Reasoners with Self-Verification\"\n- Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\"\n- Madaan et al. (2023) \"Self-Refine\"\n\n---\n\n请逐条回应 W1-W6、Q1-Q5 和 Missing References。特别关注：\n1. 你是否同意 R2 对增量新颖性的判断（W1）？这是评分差异的主要来源。\n2. 你对 DeBERTa PoC 不一致性（W2）的看法——是否与你的 N2 一致？\n3. R2 提出的 3 个 missing references 是否确实遗漏？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 交叉分享 — 请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall: 3.0 (Findings)，Confidence 4/5**\n\n**Strengths:**\nS1. 统计分析扎实（TOST + Bootstrap CI + Power Analysis）\nS2. 23种补救策略扫描防止社区重复探索死胡同\nS3. CJT 框架提供原理性诊断工具（κ → Eff-K → BR）\nS4. Independence-Accuracy Trade-off（Figure 7）最具洞察力\nS5. Oracle 分析有效分离机制与提取质量\nS6. 写作结构清晰，叙事逻辑连贯\nS7. 格式合规\n\n**Weaknesses:**\n\nW1 [warning] 核心发现的增量新颖性有限。\n- Huang et al. (2024) 已论证 LLMs 不能 self-correct；Stechly et al. (2025) 证明 self-verification 局限；Amonkar et al. (2025) 研究 LLM formalization 质量；Chan et al. (2026) 论证 logical soundness 不是可靠验证标准。本文核心洞察在概念层面已被覆盖。\n- 建议：更突出 \"FOL 的形式化语义给了 Z3 一个确定性验证通道，本文证明这个 escape hatch 也失败了\"。\n\nW2 [warning] DeBERTa NLI PoC 结论不一致。\n- FOLIO +2.94pp (n.s.)，ProofWriter SICA 本身 −2.83pp (p=0.014)。两个数据集方向相反。combo α=3 在 FOLIO 204 样本上有 overfitting 风险。\n- 建议：增加数据集，更诚实讨论 degradation，标注为 preliminary signal。\n\nW3 [warning] \"Symbolic Confirmation Bias\" 缺乏与 Turpin et al. (2024) unfaithful CoT 的深度对接。\n\nW4 [warning] Abstract \"across the full LLM capability range\" 但实际仅 7B–32B 开源模型。\n\nW5 [info] Table 1 中 7 个条件 n ≤ 60，MDE 无穷大，未区分 powered vs. exploratory。\n\nW6 [info] 附录 13 页 vs. 正文 8 页，Figure 5 应考虑移入正文。\n\n**Questions:**\nQ1. Fine-tune 专门 FOL extractor 能否提升 discriminative rate？\nQ2. Figure 7 trade-off 是否有 CJT-based 理论下界？\nQ3. DeBERTa NLI 在 ProofWriter 上 degradation 的根本原因？\nQ4. TF-IDF 是否能充分捕获 trace 语义相似性？\nQ5. Syntactic vs. semantic deduplication 影响多大？\n\n**Missing References:**\n- Weng et al. (2023) \"LLMs are Better Reasoners with Self-Verification\"\n- Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\"\n- Madaan et al. (2023) \"Self-Refine\"\n\n---\n\n请逐条回应 W1-W6、Q1-Q5 和 Missing References。特别关注：\n1. 你是否同意 R2 对增量新颖性的判断（W1）？这是评分差异的主要来源。\n2. 你对 DeBERTa PoC 不一致性（W2）的看法——是否与你的 N2 一致？\n3. R2 提出的 3 个 missing references 是否确实遗漏？"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-20T20:00:20.100035+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20277
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-20T20:00:20.150667+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 交叉分享 — 请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall: 3.5 (Borderline Conference)，Confidence 4/5**\n\n**Strengths:**\nS1. 研究问题重要且动机充分（CJT 框架）\nS2. 实验规模和覆盖度出色（6模型 × 6数据集）\nS3. Oracle controls 设计巧妙\nS4. 统计方法论严谨（TOST + Bootstrap CI + BH + Power Analysis）\nS5. Symbolic Mirage 概念及 BR 指标有独立贡献价值\nS6. 25+ 补救策略的系统性搜索令人信服\nS7. Cross-architecture escape 的建设性结论\n\n**Weaknesses:**\n\nN1 [critical] FOL 术语误导：实际提取约束以 propositional ground clauses 为主，非真正 FOL。Limitations 承认 \"predominantly propositional ground clauses without quantifiers\"。建议：报告量词比例，统一改为 \"symbolic/logical constraints\"，讨论真正 FOL 提取是否改变结论。\n\nN2 [critical] Cross-architecture PoC 仅用 Mistral-7B 一个生成模型。不同模型有 Type A/B/C 不同行为模式，单模型 PoC 无法支撑通用结论。建议：至少补一个 Qwen 模型实验。\n\nW1 [warning] 种子复制不一致：Table 1 大多数条件似为 single seed，6/15 条件 underpowered。\n\nW2 [warning] 语义去重缺失：syntactic equivalence 可能放大 verbose traces 权重，加剧 confirmation bias。\n\nW3 [warning] 域多样性表述需校准：主要结论实际集中在 formal/logical reasoning，数学域全部 degenerate。\n\nW4 [warning] 约束质量分析仅覆盖 Qwen2.5-14B 一个模型。\n\nW5 [info] Figure 2 回归 R² 极低（~4.4%），需讨论离群点影响。\n\n**Questions:**\nQ1. 含一阶量词约束比例？\nQ2. 是否在 Qwen/LLaMA 上测试过 DeBERTa NLI combo？\nQ3. 83.3% confirmation bias 率的数据来源和跨模型分布？\nQ4. 去重前后约束数量比？\nQ5. 6 个 underpowered 条件需要多大样本量达到 80% power？\nQ6. Z3 wall-clock 76% 的 scalability concern？\n\n**Missing References:**\n- Lightman et al. (2024) \"Let's Verify Step by Step\"\n- LLM self-refinement 局限性综述\n\n---\n\n请逐条回应 N1-N2、W1-W5、Q1-Q6 和 Missing References。特别关注：\n1. 你是否同意 N1（FOL 术语误导）的严重性评估？这是 R1 的第一个 critical issue。\n2. N2 与你的 W2 都指向 cross-architecture PoC 的不足——你们的判断是否一致？\n3. R1 的 W3（域多样性）和你的 W4（模型范围）是否互相加强了对泛化性的担忧？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 交叉分享 — 请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall: 3.5 (Borderline Conference)，Confidence 4/5**\n\n**Strengths:**\nS1. 研究问题重要且动机充分（CJT 框架）\nS2. 实验规模和覆盖度出色（6模型 × 6数据集）\nS3. Oracle controls 设计巧妙\nS4. 统计方法论严谨（TOST + Bootstrap CI + BH + Power Analysis）\nS5. Symbolic Mirage 概念及 BR 指标有独立贡献价值\nS6. 25+ 补救策略的系统性搜索令人信服\nS7. Cross-architecture escape 的建设性结论\n\n**Weaknesses:**\n\nN1 [critical] FOL 术语误导：实际提取约束以 propositional ground clauses 为主，非真正 FOL。Limitations 承认 \"predominantly propositional ground clauses without quantifiers\"。建议：报告量词比例，统一改为 \"symbolic/logical constraints\"，讨论真正 FOL 提取是否改变结论。\n\nN2 [critical] Cross-architecture PoC 仅用 Mistral-7B 一个生成模型。不同模型有 Type A/B/C 不同行为模式，单模型 PoC 无法支撑通用结论。建议：至少补一个 Qwen 模型实验。\n\nW1 [warning] 种子复制不一致：Table 1 大多数条件似为 single seed，6/15 条件 underpowered。\n\nW2 [warning] 语义去重缺失：syntactic equivalence 可能放大 verbose traces 权重，加剧 confirmation bias。\n\nW3 [warning] 域多样性表述需校准：主要结论实际集中在 formal/logical reasoning，数学域全部 degenerate。\n\nW4 [warning] 约束质量分析仅覆盖 Qwen2.5-14B 一个模型。\n\nW5 [info] Figure 2 回归 R² 极低（~4.4%），需讨论离群点影响。\n\n**Questions:**\nQ1. 含一阶量词约束比例？\nQ2. 是否在 Qwen/LLaMA 上测试过 DeBERTa NLI combo？\nQ3. 83.3% confirmation bias 率的数据来源和跨模型分布？\nQ4. 去重前后约束数量比？\nQ5. 6 个 underpowered 条件需要多大样本量达到 80% power？\nQ6. Z3 wall-clock 76% 的 scalability concern？\n\n**Missing References:**\n- Lightman et al. (2024) \"Let's Verify Step by Step\"\n- LLM self-refinement 局限性综述\n\n---\n\n请逐条回应 N1-N2、W1-W5、Q1-Q6 和 Missing References。特别关注：\n1. 你是否同意 N1（FOL 术语误导）的严重性评估？这是 R1 的第一个 critical issue。\n2. N2 与你的 W2 都指向 cross-architecture PoC 的不足——你们的判断是否一致？\n3. R1 的 W3（域多样性）和你的 W4（模型范围）是否互相加强了对泛化性的担忧？"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-20T20:00:21.681970+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1531
}
```

</details>

---


### Assistant

_source line 776 · 2026-05-20T20:00:25.033123+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 777 · 2026-05-20T20:00:27.515322+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成，意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。方法论扎实（Soundness 4/5），统计分析质量在 NLP 负面结果论文中属上乘（TOST 等价性检验、bootstrap CI、power analysis），但核心洞察——"LLM 自提取的符号结构继承模型偏差，无法提供独立验证"——相对于 Huang et al. (2024)、Stechly et al. (2025)、Amonkar et al. (2025) 等已有工作的增量新颖性有限（Excitement 2.5/5）。主要可操作建议：突出 Z3 确定性验证通道这一 "额外 escape hatch" 的失败论点以强化新颖性主张；修正 DeBERTa proof-of-concept 的不一致叙述；修改 Abstract 中关于模型覆盖范围的 overclaim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 778 · 2026-05-20T20:00:32.081726+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 779 · 2026-05-20T20:02:34.957286+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条回应

---

### Weaknesses 回应

**[REBUT] R2-W1: 核心发现的增量新颖性有限**

R2 列举了 Huang et al. (2024)、Stechly et al. (2025)、Chan et al. (2026) 等先行工作，认为"LLM 不能 self-correct"的结论已被概念性覆盖。我不完全同意这一判断，理由如下：

1. **先行工作的覆盖范围与本文的贡献有实质区别。** Huang et al. (2024) 论证的是 natural language 层面的 self-correction 失败；Stechly et al. (2025) 针对 planning/verification tasks。本文的独特贡献在于测试了一个更强的假设：*形式化语义（FOL → Z3 deterministic solver）能否提供 Huang et al. 所说的"external feedback"等效物？* Z3 MAX-SAT 是确定性验证通道，理论上可以绕过自然语言 self-correction 的模糊性。本文证明即使这条"escape hatch"也因为 confirmation bias 在提取环节就已失效（§3.3, BR ≈ 1.97），这是一个非平凡的实证贡献。

2. **Symbolic Mirage 的量化工具是新的。** BR 指标（§3.3）、C_D diagnostic、Eff-K 框架（§5.1, Table 2）提供了可复用的量化工具，这在先行工作中没有对应物。先行工作停留在"doesn't work"，本文给出了"why, how much, and where exactly it breaks"。

3. **但 R2 的建议是有建设性的。** 论文确实应在 §2 Related Work 中更明确地 position 自身：不是简单重复"self-correction fails"，而是"即便引入确定性形式验证（FOL + Z3），self-extraction 的 confirmation bias 仍然阻断了这条路径"。这个 framing 的差异化需要在 main text 中更突出。

**结论：部分同意 R2 的判断（framing 可以更好），但不同意"概念层面已被覆盖"的结论。本文的实证 specificity 和量化工具超越了先行工作。**

---

**[AGREE] R2-W2: DeBERTa NLI PoC 结论不一致**

同意 R2 的观察。这与我的 N2 高度一致。具体补充：

1. **方向不一致是事实。** FOLIO combo α=3: +2.94pp (n.s., adjusted p=0.038 after BH — 但 BH 校正后刚过 0.05 阈值，不robust)；ProofWriter: 同模型 SICA 自身 −2.83pp (p=0.014 degradation)，但 DeBERTa combo α=5 +10.67pp (p<0.001)。两个数据集的 baseline behavior 相反。

2. **overfitting 风险。** R2 指出 FOLIO n=204 上 α=3 的 overfitting 风险是合理的。论文未做 cross-validation 或 held-out tuning 来选择 α，仅报告了多个 α 值的 post-hoc 比较。α 在 {1, 3, 5} 上的搜索在 n=204 样本上很容易 overfit。

3. **与我的 N2 的核心共识：** 仅 Mistral-7B 作为生成模型，无法判断 DeBERTa 的正向信号是 Mistral-specific 还是 generalizable。R2 的"标注为 preliminary signal"建议恰当。

---

**[AGREE] R2-W3: 缺乏与 Turpin et al. (2024) unfaithful CoT 的深度对接**

同意。这是一个重要的理论连接。论文在 §5.3 讨论了 trace correlation（cosine similarity 0.69），但没有讨论一个更根本的问题：*如果 CoT 本身是 unfaithful 的（Turpin et al. 2024 的核心发现），那么从 unfaithful CoT 提取的约束天然就不是真正的推理约束，而是模型 output distribution 的 surface artifact。* 这将 Symbolic Mirage 的根因从"confirmation bias"深化为"unfaithful generation → biased extraction"的因果链。

论文 §5.2 报告 BR=1.97+（83.3% 的约束支持错误多数答案），但没有区分这是因为 (a) 模型故意生成支持错误答案的约束（deliberate confirmation）还是 (b) 模型的约束生成过程与答案生成共享同一个 biased representation（unfaithful CoT 的自然后果）。Turpin et al. 的框架可以帮助区分这两种机制。

---

**[REBUT] R2-W4: "Full LLM capability range" 仅覆盖 7B-32B 开源模型**

部分反驳。

1. **R2 的表面批评有道理：** "full LLM capability range" 确实不包括 70B+、GPT-4、Claude 等。措辞应改为 "across a wide range of open-source LLM capabilities" 或 "from 54% to 80% SC accuracy"。

2. **但实质影响有限。** 论文的论证逻辑是：Symbolic Mirage 的根因是 self-extraction 的 confirmation bias（§3.3），而非模型能力不足。Table 1 已覆盖了 54%-80% SC 准确率区间。更强的模型（如 GPT-4 在 FOLIO 上 SC ≈ 85-90%）会落入 Type A regime（§5.1, §O），其中 SICA 退化为加权投票（Eq. 4），负面结论只会更强。论文 §7 Discussion 也讨论了这一点：SC ≥ 60% 时 confirmation bias 更严重。

3. **真正的 gap 是 reasoning-specialized models（如 o1/o3, DeepSeek-R1）。** 这些模型可能有不同的 trace 结构（更长的 search chains），可能影响 constraint independence。但这超出了当前论文的范围，在 Limitations 中已承认（p9, "whether the independence bottleneck persists at larger scales (70B+) or reasoning-specialized models is untested"）。

**结论：措辞应修正，但实质论证不受影响。降级为 info 级别更合适。**

---

**[AGREE] R2-W5: Table 1 中低 n 条件未区分 powered vs. exploratory**

同意。Table 1 的 AIME 2024（n=22）和 GSM8K pilot（n=30）条件的 MDE 确实极大（Appendix E 的 power analysis 未覆盖这些低 n 条件，仅分析了 n ≥ 200 的 confirmatory conditions）。论文应在 Table 1 中明确标注哪些是 confirmatory（n ≥ 200, powered），哪些是 exploratory/pilot（n < 60, underpowered），避免读者误将 pilot 结果当作 confirmatory evidence。

这与我的 W1（种子复制不一致）共同指向一个 pattern：论文的 claim breadth 超出了 powered evidence 的覆盖范围。

---

**[AGREE] R2-W6: Figure 5 应考虑移入正文**

同意。Figure 5（p22, 25+ intervention strategies 的Δ汇总）是论文最重要的可视化之一，直观展示了"所有策略均失败"的核心结论。将其放在 Appendix 而非正文削弱了阅读体验。建议替换 Figure 2（CoT cosine similarity scatter, R² 仅 ~4.4%，信息量较低）或 Figure 4（regime scatter, 信息与 Table 1 重叠）。

---

### Questions 回应

**[AGREE] R2-Q1: Fine-tuned FOL extractor 能否提升 discriminative rate？**

好问题，与我的 N1 直接相关。论文 Limitations (p21) 承认未测试 trained FOL extractors。Oracle 分析（§4.3）表明 gold constraints 能大幅提升性能（+29pp FOLIO），说明 constraint quality 是关键瓶颈。但 oracle 是 ceiling——fine-tuned extractor 的实际表现取决于 training data availability 和 domain generalization。论文应至少讨论这个方向的可行性，而非完全搁置。

**[REBUT] R2-Q2: Figure 7 trade-off 是否有 CJT-based 理论下界？**

这是一个有趣的理论问题，但 CJT 的经典形式（Ladha 1992 的 correlated voters extension）假设固定的 correlation 结构。Figure 7 展示的是 *方法选择* 改变 κ 时 accuracy 如何变化——这不是 CJT 直接能给出下界的 setting，因为不同方法同时改变了 voter quality (p) 和 correlation (κ)。建立这样的理论下界需要联合建模 p 和 κ 的 trade-off，这超出了本文的范围，但确实是有价值的 future work。

**[AGREE] R2-Q3: DeBERTa NLI 在 ProofWriter 上 degradation 的根本原因？**

需要澄清：degradation 是 same-model SICA 的（−2.83pp），不是 DeBERTa combo 的。DeBERTa combo 在 ProofWriter 上实际是正向的（α=5: +10.67pp）。但 R2 的隐含问题是合理的：为什么 same-model SICA 在 ProofWriter 上反而 degradation（而 FOLIO 上接近 neutral）？论文 §O (Failure Mode Analysis) 给出了部分解释——ProofWriter 是 Type C regime（SC ~50-55%），约束提取放大错误而非纠正错误。但这个分析可以更深入。

**[AGREE] R2-Q4: TF-IDF 是否充分捕获 trace 语义相似性？**

同意这是一个 limitation。TF-IDF 只捕获 lexical overlap，不捕获 reasoning structure 或 logical dependency 的相似性。两条 trace 可能使用不同的词汇但遵循相同的推理路径（high structural similarity, low TF-IDF similarity），反之亦然。论文应在 §5.3 讨论此局限，或用 embedding-based similarity（如 sentence-BERT）做 robustness check。

**[AGREE] R2-Q5: Syntactic vs. semantic dedup 影响多大？**

同意，这与我的 W2 一致。论文未量化 syntactic dedup 的 false negative rate（语义等价但语法不同的约束对数量）。这可能系统性地影响 MAX-SAT 权重分配。

---

### Missing References 回应

**Weng et al. (2023) "LLMs are Better Reasoners with Self-Verification":**
[AGREE] 应当引用。这篇论文声称 self-verification 可以改善推理——与本文结论直接矛盾。论文需要在 §2 讨论为什么 Weng et al. 的 positive result 不能推广到 formal constraint extraction 场景，或者指出两者的 experimental setup 差异（Weng et al. 可能在更简单的任务上测试，或使用了不同的 verification 机制）。遗漏一个核心对立观点的 citation 是一个 review concern。

**Kadavath et al. (2022) "Language Models (Mostly) Know What They Know":**
[REBUT] 相关性较弱。Kadavath et al. 研究的是 calibration 和 self-knowledge，不涉及 constraint extraction 或 formal verification。论文已通过 Taubenfeld et al. (2025) 的 confidence weighting 引用覆盖了相关方向。非必须引用。

**Madaan et al. (2023) "Self-Refine":**
[AGREE] 应当引用。Self-Refine 是 iterative self-improvement 的代表工作，与本文 Remediation Strategies（§5.4）中的 iterative approaches 直接相关。论文测试了多种 iterative strategies（Table 9-11 的 contrastive prompting、Z3 feedback 等），引用 Self-Refine 作为这类方法的 anchor reference 是合理的。

---

### 总结：对 Director 三个重点问题的回答

**1. 是否同意 R2 对增量新颖性的判断（W1）？**

**部分同意 framing 层面，不同意结论层面。** R2 正确指出概念层面有 overlap（self-correction fails），但低估了本文的实证 specificity（FOL + Z3 deterministic solver 这条特定路径的失败）和量化工具（BR, C_D, Eff-K）的独立贡献。论文的 Related Work positioning 确实需要加强差异化，但这不应影响 Soundness 评分。这是 R1（3.5）与 R2（3.0）评分差异的一个来源：我更看重 empirical rigor 和 quantitative diagnostics 的独立价值。

**2. 对 DeBERTa PoC 不一致性（W2）的看法？**

**与我的 N2 高度一致。** R2 从 dataset 角度（FOLIO vs. ProofWriter 方向不一致）和我从 generator model 角度（仅 Mistral-7B）分别指出了 PoC 的不足。两者综合表明 §6 的正向结论需要大幅 qualify——当前证据仅支持 "DeBERTa NLI on Mistral-7B ProofWriter shows a positive signal" 这一极其 specific 的 claim。

**3. R2 提出的 3 个 missing references 是否确实遗漏？**

**Weng et al. (2023)：是，应当引用**——直接对立观点不可遗漏。
**Kadavath et al. (2022)：否，相关性弱**——calibration ≠ constraint extraction。
**Madaan et al. (2023)：是，应当引用**——iterative self-improvement 的 anchor work，与 §5.4 remediation strategies 直接相关。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 780 · 2026-05-20T20:02:39.841436+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 49

## Round 49

12 recorded events


### User

_source line 781 · 2026-05-20T20:02:40.842794+00:00_

[Reviewer 2 审稿结果]:
逐条回应 Reviewer 1 的审稿意见。

---

## 交叉回应：Reviewer 2 → Reviewer 1

### N1: FOL 术语误导

**[AGREE] R1-N1，但对 severity 评级有分歧——我认为是 warning 而非 critical。**

R1 的观察准确：论文 Limitations（p.21）自承 "predominantly propositional ground clauses without quantifiers"，而正文§3.2 反复使用 "first-order logic (FOL) constraints" 来描述实际以命题逻辑为主的提取结果，确实存在术语膨胀。Appendix B 的 extraction prompt 要求输出 JSON 格式的 constraints（type 包括 "equation", "inequality", "expression"），这些更接近 ground assertions 而非含量词的 FOL 公式。

**但我不同意 critical 评级，理由如下：**
1. 论文 title 使用的是 "Symbolic Constraints" 而非 "FOL Constraints"——title 层面不存在误导。
2. 命题逻辑约束是 FOL 的严格子集。如果连表达力更弱的命题约束都无法提供独立验证信号，真正的 FOL（含量词）因提取难度更高，失败的可能性只会更大而非更小——这实际上 *加强* 而非削弱了论文的负面结论。
3. 关键实验结论（Table 1 的 TOST 等价性、§5.2 的 BR = 1.97、§5.3 的 cosine similarity 0.69）均不依赖于约束是否为 "真正 FOL"——即使全部改称 "symbolic constraints"，数值结果不变。

**建议作者的修改方向与 R1 一致**：将正文中的 "FOL constraints" 统一改为 "symbolic/logical constraints"，仅在描述 Z3 solver 接口时保留 "FOL-style formalization"，并报告量词比例。但这属于 terminology calibration，不影响论文的核心技术贡献和实验结论，不应成为 reject 依据。

---

### N2: Cross-architecture PoC 仅用单一生成模型

**[AGREE] R1-N2，且与我的 W2 互相加强。**

R1 指出 PoC 仅用 Mistral-7B 作为生成模型，不同模型有 Type A/B/C 不同行为模式。我的 W2 从另一角度指出同一问题：DeBERTa 在 FOLIO 上 +2.94 pp（n.s.）但在 ProofWriter 上 −2.83 pp（p = 0.014），两个数据集方向相反。

这两个发现是 **互补的**：
- R1 揭示了 **生成端** 的泛化性缺失（仅 Mistral-7B）
- 我揭示了 **验证端** 的不一致性（FOLIO 正、ProofWriter 负）

合在一起，§6 的 PoC 在两个维度上都 underpowered：一个生成模型 × 两个数据集中结果方向相反。论文 §6 最后一段的结论 "confirming the effect is not verifier-specific" 实际上只基于三个 NLI 架构在 **同一个生成模型** 上的一致性，这不等于跨生成模型的一致性。

**但我同样认为这应是 warning 而非 critical**：§6 明确标注为 "Proof-of-Concept"，且论文的核心贡献在于 §4–5 的负面发现而非 §6 的正面信号。如果作者在 camera-ready 中补充一个 Qwen2.5-14B 的 DeBERTa 实验（这在计算上是 feasible 的——Table 1 已有 Qwen2.5-14B 的 FOLIO 和 ProofWriter traces），就能实质性地回应 R1 和我的共同关切。

---

### W1: 种子复制不一致

**[AGREE] R1-W1，部分同意。**

Table 1 中大部分条件确实呈现为 single configuration。论文在 Table 4（Appendix E）提供了 four-seed replication 对 3 个主要确认性条件的功效分析，但 Table 1 主体并未标注哪些行有 multi-seed 支撑、哪些是 single run。这与我的 W5 一致（要求标注 underpowered conditions）。

不过需要注意：论文在 §4.2 中的 TOST 等价性检验使用的是 per-item paired comparisons（SICA vs. SC on each problem），而非跨 seed 的 aggregation。这意味着 n = 204（FOLIO）或 n = 600（ProofWriter）的样本量是指问题数而非独立实验次数，统计检验本身仍然 well-powered（Table 4 确认 observed effects 均低于 MDE at 80% power）。种子变异性是一个合理的 robustness concern，但不动摇统计结论本身。

---

### W2: 语义去重缺失

**[AGREE] R1-W2，与我的 Q5 一致。**

Syntactic deduplication 将 "x > 0" 和 "x is positive" 视为不同约束，给予分别的权重。论文 Limitations（p.21）承认此限制。R1 进一步指出这可能放大 verbose traces 的权重——这是一个正确的推理：如果某些 traces 产生更多的 surface-form variants，MaxSAT 会赋予这些 traces 不成比例的影响力，加剧 confirmation bias。

这与我的 Q5 共同指向一个 missing ablation：syntactic vs. semantic deduplication 的对比实验。论文中未报告 deduplication 前后的约束数量比（R1 Q4），这个数据对于评估此问题的严重性至关重要。

---

### W3: 域多样性表述需校准

**[AGREE] R1-W3，且与我的 W4（模型范围）互相加强。**

R1 准确指出论文的主要确认性结论集中在 formal/logical reasoning（FOLIO, ProofWriter），LogiQA 表现类似但属于 multiple-choice 格式（§5.3 提到 "multiple-choice datasets (LogiQA) lack this structure"），StrategyQA 和 GSM8K 均为 degenerate 条件（Table 3 显示 StrategyQA SC = 10.0 说明约束提取率极低，GSM8K 仅 n = 30 pilot）。

这与我的 W4 形成 **双重泛化性限制**：
- **域维度**（R1-W3）：主要结论限于 formal logic，数学域 degenerate，commonsense 域提取率过低
- **模型维度**（我的 W4）：仅 open-source 7B–32B，未覆盖 frontier 模型

二者合在一起，论文 Abstract 中 "three reasoning domains" 和 "full LLM capability range" 的措辞均需显著校准。论文的 valid claim boundary 实际上是："在 7B–32B 开源模型上，对 formal/logical reasoning 数据集，自提取符号约束不改善 SC"——这仍然是有价值的贡献，但范围比当前表述窄得多。

---

### W4: 约束质量分析仅覆盖单一模型

**[AGREE] R1-W4。**

§5.2 报告的约束质量指标（91.8% discriminative rate, 39.2% source-trace minority weight）主要基于 FOLIO + ProofWriter 上的 Qwen2.5-14B（Appendix I, N = 804）。论文未系统报告其他模型的约束质量。考虑到不同模型在 Table 1 中展现出不同的 regime（Type A/B/C），约束质量可能是驱动 regime 差异的关键因素。

不过，Table 2 的 trace independence metrics（κ, K_eff, Effective-K）确实覆盖了多个模型和数据集，部分弥补了这一不足。约束质量的全模型 breakdown 是一个 reasonable ask，但有限的约束质量分析不影响 Table 1 主实验的 validity（主实验直接衡量 SICA vs. SC 准确率差异，不依赖于约束质量的中间分析）。

---

### W5: Figure 2 R² 极低

**[AGREE] R1-W5，但影响程度有限。**

Figure 2 的线性回归 R² ≈ 0.044 确实很低，说明 answer agreement 仅解释 trace cosine similarity 变异的 ~4.4%。R1 要求讨论离群点影响是合理的。

但论文的论点不是"answer agreement 预测 trace similarity"，而是"trace similarity 系统性高于 answer-level agreement 所暗示的水平"——即 traces 在 process level 比在 answer level 更加相关。这一论点的支撑主要来自 Table 2 的 κ vs. cosine similarity 对比（κ = 0.41 vs. cosine = 0.69），Figure 2 只是辅助可视化。R² 低说明关系非线性或有很大噪声，但不否认均值水平的系统性差异。

---

### Questions 回应

**Q1（量词比例）：** [AGREE] 应报告。论文 Limitations 已承认 "predominantly propositional"，但缺乏定量数据。

**Q2（DeBERTa on Qwen/LLaMA）：** [AGREE] 与 N2 一致，这是 PoC 最需要补充的实验。

**Q3（83.3% 跨模型分布）：** [AGREE] 应报告。§5.2 的 83.3% 和 BR = 1.97 看起来是 aggregate 数字。Table 13（Appendix P）报告了 FOLIO 上三个模型的 cross-model confirmation bias 数据（BR wrong-weighted fraction），显示 Mistral-7B、Qwen2.5-14B、LLaMA-3.1-8B 的 wrong-supporting constraint percentage 分别为 69%、79%、94%（从 Table 13 的 Wrong % 列），变异确实很大。论文应将此 per-model breakdown 放入正文。

**Q4（去重前后约束数量比）：** [AGREE] 缺失数据，应补充。

**Q5（underpowered 条件所需样本量）：** [AGREE] Table 4 提供了 MDE but not the inverse power calculation。这对 future replication 有参考价值。

**Q6（Z3 wall-clock 76% scalability）：** [REBUT] 部分反驳。§4.1 提到 Z3 使用 10 秒超时（Appendix C, Algorithm 1），超时后 assertion 视为 nonzero score。对于 FOLIO（n = 204）和 ProofWriter（n = 600）规模的问题，Z3 在 per-constraint level 的求解是高效的——76% 的 wall-clock 比例不等于 scalability bottleneck，因为 (a) 这些是 per-constraint 的独立 SAT 调用，天然可并行；(b) 10 秒超时限制了最坏情况。对于更大规模的问题集，瓶颈更可能在 LLM inference 而非 Z3。

---

### Missing References 回应

**Lightman et al. (2024) "Let's Verify Step by Step"：** [REBUT] 此引用 **已存在于论文中**。Bib key `lightman2024prm`，在 related_work.tex（line 11）和 experiments.tex（line 11）中被 `\citep` 引用。Reference verification 也确认该条目存在（虽然 OpenAlex 未匹配到，但这是 OpenAlex 索引问题而非引用缺失）。R1 此处有误。

**LLM self-refinement 局限性综述：** [AGREE] 方向上同意——我在自己的 Missing References 中也建议引用 Madaan et al. (2023) Self-Refine 作为 self-refinement 代表工作。不过"综述"可能不存在一篇 canonical 的 survey，引用具体工作（Madaan et al. 2023, Huang et al. 2024）已足够。

---

### 总结：与 R1 的评分对比

| 维度 | R1 | R2（我） | 差异分析 |
|------|-----|---------|---------|
| Overall | 3.5 Borderline Conference | 3.0 Findings | R1 对 Symbolic Mirage 概念和 BR 指标的独立贡献价值评价更高（S5），我对增量新颖性的扣分更重（我的 W1） |
| Soundness | 未明确单独评分 | 4/5 | 应一致 |
| Excitement | 未明确单独评分 | 2.5/5 | 我的主要扣分来源 |

**核心分歧：** R1 给 3.5 主要因为认可 Symbolic Mirage + BR 的概念贡献和 25+ 策略扫描的 completeness；我给 3.0 因为认为核心洞察在 Huang (2024)/Stechly (2025)/Amonkar (2025)/Chan (2026) 已有覆盖。这是 legitimate disagreement——如果 AC 认为 CJT 框架的量化诊断能力构成 sufficient novelty，3.5 是可辩护的；如果认为概念层面的增量有限，3.0 更合适。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心判断：
- R2-W1（新颖性）：部分同意 framing 需改进，但不同意实证贡献已被覆盖
- R2-W2（PoC 不一致）：同意，与我的 N2 从不同角度指向同一问题
- Missing refs：Weng et al. 2023 和 Madaan et al. 2023 确实应引用，Kadavath et al. 2022 非必须
- R1 与 R2 评分差异主要来自对 empirical rigor 独立价值的权重不同

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-20T20:03:08.596384+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-20T20:03:09.148668+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-20T19:51:46.554338+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_970d5ea3f54df81296b97321fcded892\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-20T20:03:09.149044+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-20T20:03:09.450446+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T19:51:45.715964+00:00\", \"completed_at\": \"2026-05-20T19:55:53.467212+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"正文前 3 页（占正文 37.5%）无任何 figure/table，审稿人需翻到 page 4 才见到第一个视觉锚点。对于实证分析型论文，建议将 Figure 1 或一个核心结果预览提前到 page 2，帮助审稿人在前 2 分钟内建立认知框架\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"Figure 1（SICA pipeline）仅占单栏宽度，管线中的文字标注在打印时可能偏小。作为核心方法的唯一图示，建议考虑 figure*（全宽）以提升可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"page 5 为纯文本页（Section 5 Analysis），夹在 Figure 1(p4) 和 Table 1(p6) 之间，视觉节奏略显单调\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 信息量大（~25 行 × 8 列），占满整页。排版规范（booktabs、加粗最优值、分组标题），但首次阅读认知负担较高。考虑将部分非核心 condition 移至 appendix 以减轻主表密度\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 + Figure 2 在同一页，视觉密度良好，布局合理\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3 位于右栏上部，Discussion + Conclusion 顺畅衔接，空间利用率高\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落后 References 自然接续，页面填充约 90%，正常\"}, {\"severity\": \"warning\", \"dimension\": \"page 21\", \"message\": \"Extended Limitations 文本仅占页面顶部约 1/3，下方约 2/3 为空白。虽在 Appendix 中，但对整体印象有负面影响——建议与后续 appendix 内容合并排布消除空白\"}, {\"severity\": \"info\", \"dimension\": \"page 22\", \"message\": \"Figure 5（22+ intervention strategies summary）是全文信息量最高的可视化之一，清晰传达\\\"所有干预策略均产生中性或负向结果\\\"的核心发现。当前深埋 Appendix page 22，建议考虑将其简化版放入正文（如 Section 5.5 Remediation Analysis 旁），能极大强化论文的说服力\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"Figure 6 + Figure 7 布局合理，两图之间留白适度。Figure 7 的 independence-accuracy trade-off 可视化设计优秀（same-model ceiling 灰带、方法标注），如正文有空间也值得考虑提升\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"表格全部使用 booktabs 风格，无竖线，最优值加粗——排版规范\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message
…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-20T20:03:09.450837+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-20T20:03:09.502081+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-20T20:06:16.437465+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-7 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n- id: \"R3-N3\"\n  summary: \"Discriminative rate from small pilot\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"804-instance analysis: 8.2% [CI: 7.6, 8.8].\"\n  resolution_round: 3\n\n- id: \"R3-W6\"\n  summary: \"No 70B+ model tested\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Acknowledged as limitation in paper.\"\n  resolution_round: 4\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W4 re-raised: Abstract 'full LLM capability range' overclaims given 7B-32B only. Model range limitation persists.\"\n\n- id: \"R4-C1\"\n  summary: \"Cross-section Δ inconsistency\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"D064+D066 full data replacement completed.\"\n  resolution_round: 4\n\n- id: \"R4-C2\"\n  summary: \"CJT framing gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Dual-bottleneck paragraph added. Title changed.\"\n  resolution_round: 4\n\n- id: \"R4-C3\"\n  summary: \"Goldilocks zone evidence from only 1 model × 1 dataset\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Claims downgraded to 'directional trend'. V2 framing de-emphasizes intermediate region.\"\n  resolution_round: 5\n\n- id: \"R4-W1\"\n  summary: \"Multiple testing correction\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"BH correction computed: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Eff-K Kish (1965) attribution / κ→ICC proxy rigor\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Pairwise Pearson r (mean 0.625, Mistral-7B) monotonically related to κ across 4 model families. κ validated as consensus proxy.\"\n  resolution_round: 7\n\n- id: \"R4-M5\"\n  summary: \"Figure 2 old data\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Figure 2 moved to Appendix in V2 page budget compression.\"\n  resolution_round: 6\n\n- id: \"R5-N1\"\n  summary: \"Oracle ceiling '24%' cross-model comparison invalid\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Mistral-7B same-model oracle: +29.90pp (p<1e-13).\"\n  resolution_round: 5\n\n- id: \"R5-N2\"\n  summary: \"§4.1 Decoupling interim results (n=70/204) in main text\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"V2 framing removes §4.1 Decoupling from main text entirely.\"\n  resolution_round: 5\n\n- id: \"R5-N3\"\n  summary: \"'Fundamental' trade-off overclaimed\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All 'fundamental' → 'persistent' + 'at the 7B--32B scale'.\"\n  resolution_round: 5\n\n- id: \"R5-N4\"\n  summary: \"DeBERTa PoC statistically fragile — 9 discordant pairs\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"ProofWriter w=3 +3.50pp (p=0.013, n=600) as primary finding.\"\n  resolution_round: 5\n\n- id: \"R5-N5\"\n  summary: \"Discussion/Conclusion too thin for negative paper\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Discussion ~350 words, Conclusion ~220 words.\"\n  resolution_round: 5\n\n- id: \"R5-W1\"\n  summary: \"Variable name isolation confound\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Alpha-equivalence caveat added in Discussion.\"\n  resolution_round: 5\n\n- id: \"R5-W2\"\n  summary: \"Fleiss' κ as ICC proxy lacks formal justification\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Caveat added. Pairwise correlation validates κ (tracked under R4-W3).\"\n  resolution_round: 5\n\n- id: \"R5-W3\"\n  summary: \"Missing ensemble diversity literature\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Krogh & Vedelsby (1994) + Brown et al. (2005) cited.\"\n  resolution_round: 5\n\n- id: \"R5-W4\"\n  summary: \"§3/§5 content duplication\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Not flagged in R6 — considered resolved.\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"'25+ strategies' count inflated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"'more than twenty spanning fifteen distinct families'.\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"Code/data release not mentioned\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Reproducibility paragraph added.\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Solutions before Experiments ordering\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"main.tex reordered correctly.\"\n  resolution_round: 5\n\n- id: \"R5-W8\"\n  summary: \"TF-IDF cosine limitation under-discussed\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Deferred to rebuttal. SBERT validation not worth GPU time per Reviewer assessment.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers re-raised: R1-W5 notes Figure 2 R²≈4.4% is very low; R2-Q4 asks if TF-IDF sufficiently captures semantic similarity. Limitation persists.\"\n\n- id: \"R5-W9\"\n  summary: \"CJT novelty / Huang-Stechly distinction insufficient\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Paper Agent added novelty differentiation paragraph (3 quantitative differentiators). Tracked jointly with R6-N3.\"\n  resolution_round: 7\n\n- id: \"R5-TC1\"\n  summary: \"SC tiebreaking inconsistency (dict-order vs alphabetical)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All tiebreaking standardized to alphabetical.\"\n  resolution_round: 5\n\n- id: \"R6-N1\"\n  summary: \"Statistical power 5.7%-20.6% — title 'Fail' overclaims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Title changed to 'Do Not Improve'. TOST computed: 4/15 equivalence, 5/15 genuine difference (4 negative), 6/15 underpowered. Three-tier classification integrated into abstract, §4, appendix.\"\n  resolution_round: 7\n\n- id: \"R6-N2\"\n  summary: \"Cross-arch PoC p=0.013 needs multiple comparison correction\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"BH correction: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Novelty vs self-correction literature (Huang/Stechly/Amonkar)\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Novelty paragraph added (3 differentiators: κ/Eff-K diagnostics, formal Z3 verification, process-level analysis). §3.3 empirical bound (Δ_max ≤ Oracle_Gap/BR) further differentiates.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W1 re-raised novelty concern despite R7 fix. R1 partially rebuts, citing empirical specificity and quantitative tools. Divergence remains — see R8-W1.\"\n\n- id: \"R6-N4\"\n  summary: \"Missing references: CLOVER (ICLR 2025), VERGE, Toh et al. (2024)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"5 BibTeX entries written (CLOVER, VERGE, Toh et al., Chan et al., Lakens). All cited in Related Work + §4. Author correction applied (Toh et al., not Xia et al.). Orphan bib removed.\"\n  resolution_round: 7\n\n- id: \"R6-W1\"\n  summary: \"Bias ratio numbers inconsistent between main text and Table 14\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent clarified BR calculation scope (Batch 1 W6).\"\n  resolution_round: 7\n\n- id: \"R6-W2\"\n  summary: \"Type A/B/C failure mode classification is post-hoc\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent labeled as 'three empirical regimes (observation-driven)' (Batch 1 W7).\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"Degeneration condition (Eq. 4) derivation incomplete\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Constraint rejection rate 3.44% (no diff correct/incorrect, p=0.636) integrated into §5.2 as empirical evidence for Eq.4 degeneration.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"'Symbolic Mirage' terminology too marketing-like\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Scoping sentence added: Mirage is specific to self-extracted constraints. §3.3 explicitly contrasts with independently sourced constraints.\"\n  resolution_round: 7\n\n- id: \"R6-W5\"\n  summary: \"α=0.5 penalty weight lacks sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"α sensitivity: max 0.49pp variation across α∈{0.0-1.0}. One-sentence note added to §3.2 C₀ diagnostic paragraph.\"\n  resolution_round: 7\n\n- id: \"R6-W6\"\n  summary: \"GSM8K (n=30) and AIME (n=22) in main Table 1 misleading\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Kept with † marker and 'suggestive only' caveat. Degenerate regime demonstration serves pedagogical purpose.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W5: underpowered conditions still not clearly marked in Table 1. Recommend explicit powered vs. exploratory labeling.\"\n\n- id: \"R6-W7\"\n  summary: \"Orphan bib entry (press2023compositionality)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"press2023compositionality removed from references.bib. All new entries (CLOVER, VERGE, Toh, Chan, Lakens) cited.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"Reasoning models not discussed as category in Related Work\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent added reasoning models paragraph with κ=0.91 homogenization (Batch 1 W14).\"\n  resolution_round: 7\n\n- id: \"R6-V1\"\n  summary: \"Page 20 >75% empty white space\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Page 20 now ~60% filled (TOST section + Extended Limitations). Remaining whitespace is natural appendix pagination.\"\n  resolution_round: 7\n\n- id: \"R6-V2\"\n  summary: \"Main text only 5 display items\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"8-page limit constrains display items. 2 tables + 1 figure + pipeline diagram in main text; 10+ tables/figures in appendix.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"Visual check + R2-W6: Figure 5 (intervention strategies) recommended for main text. First 3 pages lack any visual anchor.\"\n\n# =========================================================\n# Round 8 new issues (fresh review)\n# =========================================================\n\n- id: \"R8-N1\"\n  summary: \"FOL terminology misleading — actual constraints are predominantly propositional ground clauses\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 rated critical, R2 rated warning. Consensus: terminology needs fixing. R2 argues propositional ⊂ FOL so negative conclusion only strengthens; R1 argues scope of claim is unclear. Both recommend unifying to 'symbolic/logical constraints' and reporting quantifier proportion.\"\n  action_items:\n    - round: 8\n      action: \"Unify 'FOL constraints' → 'symbolic/logical constraints' in main text; report quantifier proportion by domain/model; discuss in Discussion whether true FOL extraction could change conclusion\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N2\"\n  summary: \"Cross-architecture PoC underpowered: single generator (Mistral-7B) × inconsistent dataset results (FOLIO n.s., ProofWriter degradation)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N2 (generator dimension): only Mistral-7B tested, Type A/B/C models may behave differently. R2-W2 (dataset dimension): FOLIO +2.94pp n.s. vs ProofWriter SICA −2.83pp degradation. Both agree §6 conclusions need heavy qualification. R2 notes this should be 'preliminary signal' not 'confirmed escape'.\"\n  action_items:\n    - round: 8\n      action: \"Add at least one Qwen-family model DeBERTa combo experiment; qualify §6 conclusion as preliminary; address α selection overfitting risk\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W1\"\n  summary: \"Incremental novelty relative to Huang (2024)/Stechly (2025)/Amonkar (2025)/Chan (2026) self-verification failure literature\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2 rates Excitement 2.5/5, argues conceptual overlap. R1 rebuts: FOL+Z3 deterministic path is a specific and non-trivial test; BR/C_D/Eff-K are novel quantitative tools. Both agree Related Work positioning should more explicitly state 'even deterministic formal verification fails when extraction is self-sourced'.\"\n  action_items:\n    - round: 8\n      action: \"Strengthen §2 positioning: explicitly frame contribution as testing whether deterministic FOL+Z3 verification escapes self-correction limitations; highlight quantitative diagnostic tools as independent contribution\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Seed replication inconsistency — Table 1 does not mark which conditions have multi-seed support\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W1 raised, R2 agrees but notes TOST uses per-item paired comparisons (n=problems not seeds), so statistical conclusions hold. Robustness concern rather than validity threat.\"\n  action_items:\n    - round: 8\n      action: \"Add seed count column to Table 1; clearly distinguish confirmatory (multi-seed, powered) vs. exploratory (single-seed, underpowered) conditions\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"Semantic deduplication missing — syntactic-only dedup may inflate verbose trace weights and amplify confirmation bias\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W2 raised, R2-Q5 independently asks same question. Neither reviewer has evidence this changes results, but missing ablation (dedup ratio + Z3 semantic equivalence check) weakens claim precision.\"\n  action_items:\n    - round: 8\n      action: \"Report pre/post dedup constraint counts; run Z3 semantic equivalence ablation or discuss quantitatively in limitations\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"Domain diversity + model range overclaimed in Abstract — valid conclusions narrower than stated\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W3 (domain): math domain all degenerate, main conclusions limited to formal/logical reasoning. R2-W4 (model): 'full LLM capability range' but only open-source 7B-32B. Both agree Abstract needs calibration to 'open-source 7B-32B models on formal/logical reasoning'.\"\n  action_items:\n    - round: 8\n      action: \"Revise Abstract: 'full LLM capability range' → 'open-source 7B-32B'; 'three reasoning domains' → acknowledge math domain is degenerate/exploratory\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"Constraint quality analysis (91.8% discriminative rate) based on single model family (Qwen2.5-14B)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"R1-W4: extraction error taxonomy (Appendix L, N=804) covers only Qwen2.5-14B on FOLIO+ProofWriter. Different models (Type A/B/C) may have different extraction quality profiles. R2 agrees but notes Table 1 main results don't depend on intermediate quality analysis.\"\n  action_items:\n    - round: 8\n      action: \"Extend extraction quality analysis to 2-3 additional models, or clearly scope the 91.8% claim to Qwen2.5-14B\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"Symbolic Confirmation Bias lacks theoretical connection to Turpin et al. (2024) unfaithful CoT framework\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3 raised, R1 agrees in cross-response. BR=1.97 may be consequence of unfaithful CoT (biased representation) rather than deliberate confirmation. Turpin et al. framework could deepen causal explanation.\"\n  action_items:\n    - round: 8\n      action: \"In §3.3, explicitly discuss Turpin et al. connection: if CoT is unfaithful, extracted constraints inherit representation bias rather than reasoning content\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I1\"\n  summary: \"Missing references: Weng et al. (2023) Self-Verification and Madaan et al. (2023) Self-Refine\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers agree Weng et al. (2023, positive self-verification result) and Madaan et al. (2023, Self-Refine) should be cited. Kadavath et al. (2022) deemed non-essential by R1.\"\n  action_items:\n    - round: 8\n      action: \"Add Weng et al. (2023) and Madaan et al. (2023) to §2 Related Work with discussion of why their positive results don't generalize to FOL constraint extraction\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I2\"\n  summary: \"Figure 5 (intervention strategies summary) buried in Appendix p.22 — should be in main text\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers + visual check agree Figure 5 is the most informative visualization. R1 suggests replacing Figure 2 (R²≈4.4%) or Figure 4. Visual check also notes first 3 pages lack visual anchors.\"\n  action_items:\n    - round: 8\n      action: \"Move Figure 5 (or simplified version) into main text; consider promoting Figure 7 (independence-accuracy trade-off) as well\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I3\"\n  summary: \"83.3% confirmation bias rate needs per-model breakdown in main text\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"R1-Q3: 83.3% appears to be aggregate. Table 13 shows per-model wrong-supporting rates vary widely (69%-94%). Main text should report this breakdown.\"\n  action_items:\n    - round: 8\n      action: \"Add per-model BR breakdown to §5.2 or at least reference Table 13 explicitly\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-7 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n- id: \"R3-N3\"\n  summary: \"Discriminative rate from small pilot\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"804-instance analysis: 8.2% [CI: 7.6, 8.8].\"\n  resolution_round: 3\n\n- id: \"R3-W6\"\n  summary: \"No 70B+ model tested\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Acknowledged as limitation in paper.\"\n  resolution_round: 4\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W4 re-raised: Abstract 'full LLM capability range' overclaims given 7B-32B only. Model range limitation persists.\"\n\n- id: \"R4-C1\"\n  summary: \"Cross-section Δ inconsistency\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"D064+D066 full data replacement completed.\"\n  resolution_round: 4\n\n- id: \"R4-C2\"\n  summary: \"CJT framing gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Dual-bottleneck paragraph added. Title changed.\"\n  resolution_round: 4\n\n- id: \"R4-C3\"\n  summary: \"Goldilocks zone evidence from only 1 model × 1 dataset\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Claims downgraded to 'directional trend'. V2 framing de-emphasizes intermediate region.\"\n  resolution_round: 5\n\n- id: \"R4-W1\"\n  summary: \"Multiple testing correction\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"BH correction computed: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Eff-K Kish (1965) attribution / κ→ICC proxy rigor\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Pairwise Pearson r (mean 0.625, Mistral-7B) monotonically related to κ across 4 model families. κ validated as consensus proxy.\"\n  resolution_round: 7\n\n- id: \"R4-M5\"\n  summary: \"Figure 2 old data\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Figure 2 moved to Appendix in V2 page budget compression.\"\n  resolution_round: 6\n\n- id: \"R5-N1\"\n  summary: \"Oracle ceiling '24%' cross-model comparison invalid\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Mistral-7B same-model oracle: +29.90pp (p<1e-13).\"\n  resolution_round: 5\n\n- id: \"R5-N2\"\n  summary: \"§4.1 Decoupling interim results (n=70/204) in main text\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"V2 framing removes §4.1 Decoupling from main text entirely.\"\n  resolution_round: 5\n\n- id: \"R5-N3\"\n  summary: \"'Fundamental' trade-off overclaimed\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All 'fundamental' → 'persistent' + 'at the 7B--32B scale'.\"\n  resolution_round: 5\n\n- id: \"R5-N4\"\n  summary: \"DeBERTa PoC statistically fragile — 9 discordant pairs\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"ProofWriter w=3 +3.50pp (p=0.013, n=600) as primary finding.\"\n  resolution_round: 5\n\n- id: \"R5-N5\"\n  summary: \"Discussion/Conclusion too thin for negative paper\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Discussion ~350 words, Conclusion ~220 words.\"\n  resolution_round: 5\n\n- id: \"R5-W1\"\n  summary: \"Variable name isolation confound\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Alpha-equivalence caveat added in Discussion.\"\n  resolution_round: 5\n\n- id: \"R5-W2\"\n  summary: \"Fleiss' κ as ICC proxy lacks formal justification\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Caveat added. Pairwise correlation validates κ (tracked under R4-W3).\"\n  resolution_round: 5\n\n- id: \"R5-W3\"\n  summary: \"Missing ensemble diversity literature\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Krogh & Vedelsby (1994) + Brown et al. (2005) cited.\"\n  resolution_round: 5\n\n- id: \"R5-W4\"\n  summary: \"§3/§5 content duplication\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Not flagged in R6 — considered resolved.\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"'25+ strategies' count inflated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"'more than twenty spanning fifteen distinct families'.\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"Code/data release not mentioned\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Reproducibility paragraph added.\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Solutions before Experiments ordering\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"main.tex reordered correctly.\"\n  resolution_round: 5\n\n- id: \"R5-W8\"\n  summary: \"TF-IDF cosine limitation under-discussed\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 8\n  resolution: \"Deferred to rebuttal. SBERT validation not worth GPU time per Reviewer assessment.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers re-raised: R1-W5 notes Figure 2 R²≈4.4% is very low; R2-Q4 asks if TF-IDF sufficiently captures semantic similarity. Limitation persists.\"\n\n- id: \"R5-W9\"\n  summary: \"CJT novelty / Huang-Stechly distinction insufficient\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Paper Agent added novelty differentiation paragraph (3 quantitative differentiators). Tracked jointly with R6-N3.\"\n  resolution_round: 7\n\n- id: \"R5-TC1\"\n  summary: \"SC tiebreaking inconsistency (dict-order vs alphabetical)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All tiebreaking standardized to alphabetical.\"\n  resolution_round: 5\n\n- id: \"R6-N1\"\n  summary: \"Statistical power 5.7%-20.6% — title 'Fail' overclaims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Title changed to 'Do Not Improve'. TOST computed: 4/15 equivalence, 5/15 genuine difference (4 negative), 6/15 underpowered. Three-tier classification integrated into abstract, §4, appendix.\"\n  resolution_round: 7\n\n- id: \"R6-N2\"\n  summary: \"Cross-arch PoC p=0.013 needs multiple comparison correction\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"BH correction: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Novelty vs self-correction literature (Huang/Stechly/Amonkar)\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Novelty paragraph added (3 differentiators: κ/Eff-K diagnostics, formal Z3 verification, process-level analysis). §3.3 empirical bound (Δ_max ≤ Oracle_Gap/BR) further differentiates.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W1 re-raised novelty concern despite R7 fix. R1 partially rebuts, citing empirical specificity and quantitative tools. Divergence remains — see R8-W1.\"\n\n- id: \"R6-N4\"\n  summary: \"Missing references: CLOVER (ICLR 2025), VERGE, Toh et al. (2024)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"5 BibTeX entries written (CLOVER, VERGE, Toh et al., Chan et al., Lakens). All cited in Related Work + §4. Author correction applied (Toh et al., not Xia et al.). Orphan bib removed.\"\n  resolution_round: 7\n\n- id: \"R6-W1\"\n  summary: \"Bias ratio numbers inconsistent between main text and Table 14\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent clarified BR calculation scope (Batch 1 W6).\"\n  resolution_round: 7\n\n- id: \"R6-W2\"\n  summary: \"Type A/B/C failure mode classification is post-hoc\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent labeled as 'three empirical regimes (observation-driven)' (Batch 1 W7).\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"Degeneration condition (Eq. 4) derivation incomplete\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Constraint rejection rate 3.44% (no diff correct/incorrect, p=0.636) integrated into §5.2 as empirical evidence for Eq.4 degeneration.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"'Symbolic Mirage' terminology too marketing-like\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Scoping sentence added: Mirage is specific to self-extracted constraints. §3.3 explicitly contrasts with independently sourced constraints.\"\n  resolution_round: 7\n\n- id: \"R6-W5\"\n  summary: \"α=0.5 penalty weight lacks sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"α sensitivity: max 0.49pp variation across α∈{0.0-1.0}. One-sentence note added to §3.2 C₀ diagnostic paragraph.\"\n  resolution_round: 7\n\n- id: \"R6-W6\"\n  summary: \"GSM8K (n=30) and AIME (n=22) in main Table 1 misleading\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Kept with † marker and 'suggestive only' caveat. Degenerate regime demonstration serves pedagogical purpose.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W5: underpowered conditions still not clearly marked in Table 1. Recommend explicit powered vs. exploratory labeling.\"\n\n- id: \"R6-W7\"\n  summary: \"Orphan bib entry (press2023compositionality)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"press2023compositionality removed from references.bib. All new entries (CLOVER, VERGE, Toh, Chan, Lakens) cited.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"Reasoning models not discussed as category in Related Work\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent added reasoning models paragraph with κ=0.91 homogenization (Batch 1 W14).\"\n  resolution_round: 7\n\n- id: \"R6-V1\"\n  summary: \"Page 20 >75% empty white space\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Page 20 now ~60% filled (TOST section + Extended Limitations). Remaining whitespace is natural appendix pagination.\"\n  resolution_round: 7\n\n- id: \"R6-V2\"\n  summary: \"Main text only 5 display items\"\n  category: format\n  severity: info\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"8-page limit constrains display items. 2 tables + 1 figure + pipeline diagram in main text; 10+ tables/figures in appendix.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"Visual check + R2-W6: Figure 5 (intervention strategies) recommended for main text. First 3 pages lack any visual anchor.\"\n\n# =========================================================\n# Round 8 new issues (fresh review)\n# =========================================================\n\n- id: \"R8-N1\"\n  summary: \"FOL terminology misleading — actual constraints are predominantly propositional ground clauses\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 rated critical, R2 rated warning. Consensus: terminology needs fixing. R2 argues propositional ⊂ FOL so negative conclusion only strengthens; R1 argues scope of claim is unclear. Both recommend unifying to 'symbolic/logical constraints' and reporting quantifier proportion.\"\n  action_items:\n    - round: 8\n      action: \"Unify 'FOL constraints' → 'symbolic/logical constraints' in main text; report quantifier proportion by domain/model; discuss in Discussion whether true FOL extraction could change conclusion\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-N2\"\n  summary: \"Cross-architecture PoC underpowered: single generator (Mistral-7B) × inconsistent dataset results (FOLIO n.s., ProofWriter degradation)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-N2 (generator dimension): only Mistral-7B tested, Type A/B/C models may behave differently. R2-W2 (dataset dimension): FOLIO +2.94pp n.s. vs ProofWriter SICA −2.83pp degradation. Both agree §6 conclusions need heavy qualification. R2 notes this should be 'preliminary signal' not 'confirmed escape'.\"\n  action_items:\n    - round: 8\n      action: \"Add at least one Qwen-family model DeBERTa combo experiment; qualify §6 conclusion as preliminary; address α selection overfitting risk\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W1\"\n  summary: \"Incremental novelty relative to Huang (2024)/Stechly (2025)/Amonkar (2025)/Chan (2026) self-verification failure literature\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2 rates Excitement 2.5/5, argues conceptual overlap. R1 rebuts: FOL+Z3 deterministic path is a specific and non-trivial test; BR/C_D/Eff-K are novel quantitative tools. Both agree Related Work positioning should more explicitly state 'even deterministic formal verification fails when extraction is self-sourced'.\"\n  action_items:\n    - round: 8\n      action: \"Strengthen §2 positioning: explicitly frame contribution as testing whether deterministic FOL+Z3 verification escapes self-correction limitations; highlight quantitative diagnostic tools as independent contribution\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Seed replication inconsistency — Table 1 does not mark which conditions have multi-seed support\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W1 raised, R2 agrees but notes TOST uses per-item paired comparisons (n=problems not seeds), so statistical conclusions hold. Robustness concern rather than validity threat.\"\n  action_items:\n    - round: 8\n      action: \"Add seed count column to Table 1; clearly distinguish confirmatory (multi-seed, powered) vs. exploratory (single-seed, underpowered) conditions\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"Semantic deduplication missing — syntactic-only dedup may inflate verbose trace weights and amplify confirmation bias\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W2 raised, R2-Q5 independently asks same question. Neither reviewer has evidence this changes results, but missing ablation (dedup ratio + Z3 semantic equivalence check) weakens claim precision.\"\n  action_items:\n    - round: 8\n      action: \"Report pre/post dedup constraint counts; run Z3 semantic equivalence ablation or discuss quantitatively in limitations\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"Domain diversity + model range overclaimed in Abstract — valid conclusions narrower than stated\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W3 (domain): math domain all degenerate, main conclusions limited to formal/logical reasoning. R2-W4 (model): 'full LLM capability range' but only open-source 7B-32B. Both agree Abstract needs calibration to 'open-source 7B-32B models on formal/logical reasoning'.\"\n  action_items:\n    - round: 8\n      action: \"Revise Abstract: 'full LLM capability range' → 'open-source 7B-32B'; 'three reasoning domains' → acknowledge math domain is degenerate/exploratory\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"Constraint quality analysis (91.8% discriminative rate) based on single model family (Qwen2.5-14B)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"R1-W4: extraction error taxonomy (Appendix L, N=804) covers only Qwen2.5-14B on FOLIO+ProofWriter. Different models (Type A/B/C) may have different extraction quality profiles. R2 agrees but notes Table 1 main results don't depend on intermediate quality analysis.\"\n  action_items:\n    - round: 8\n      action: \"Extend extraction quality analysis to 2-3 additional models, or clearly scope the 91.8% claim to Qwen2.5-14B\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"Symbolic Confirmation Bias lacks theoretical connection to Turpin et al. (2024) unfaithful CoT framework\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2-W3 raised, R1 agrees in cross-response. BR=1.97 may be consequence of unfaithful CoT (biased representation) rather than deliberate confirmation. Turpin et al. framework could deepen causal explanation.\"\n  action_items:\n    - round: 8\n      action: \"In §3.3, explicitly discuss Turpin et al. connection: if CoT is unfaithful, extracted constraints inherit representation bias rather than reasoning content\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I1\"\n  summary: \"Missing references: Weng et al. (2023) Self-Verification and Madaan et al. (2023) Self-Refine\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers agree Weng et al. (2023, positive self-verification result) and Madaan et al. (2023, Self-Refine) should be cited. Kadavath et al. (2022) deemed non-essential by R1.\"\n  action_items:\n    - round: 8\n      action: \"Add Weng et al. (2023) and Madaan et al. (2023) to §2 Related Work with discussion of why their positive results don't generalize to FOL constraint extraction\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I2\"\n  summary: \"Figure 5 (intervention strategies summary) buried in Appendix p.22 — should be in main text\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers + visual check agree Figure 5 is the most informative visualization. R1 suggests replacing Figure 2 (R²≈4.4%) or Figure 4. Visual check also notes first 3 pages lack visual anchors.\"\n  action_items:\n    - round: 8\n      action: \"Move Figure 5 (or simplified version) into main text; consider promoting Figure 7 (independence-accuracy trade-off) as well\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-I3\"\n  summary: \"83.3% confirmation bias rate needs per-model breakdown in main text\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1]\n      note: \"R1-Q3: 83.3% appears to be aggregate. Table 13 shows per-model wrong-supporting rates vary widely (69%-94%). Main text should report this breakdown.\"\n  action_items:\n    - round: 8\n      action: \"Add per-model BR breakdown to §5.2 or at least reference Table 13 explicitly\"\n      assigned_to: \"author\"\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-20T20:06:16.540207+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 23287}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-20T20:08:40.346660+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "symb_invariant_consensus",
  "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: \"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + Related Work + 写作质量)\n\n---\n\n## Summary\n\n本文研究 LLM 自提取的符号约束能否通过 Symbolic Invariant Consensus Aggregation (SICA)——基于 FOL 约束提取和 Z3 weighted partial MAX-SAT——改善 Self-Consistency majority voting。在 6 个模型（7B–32B）、3 个推理域、3000+ 条件评估中，自提取约束未能显著提升准确率。作者将此归因于 \"Symbolic Mirage\"：自提取约束是模型分布偏差的投射（confirmation bias rate 83.3%, BR ≈ 1.97+），trace 之间的 process-level 相关性（cosine similarity 0.69）远超 answer-level 独立性（κ ≈ 0.41）。25+ 补救策略均失败，揭示持久的 independence-accuracy trade-off。Oracle controls 确认聚合机制 sound（+29.90pp, +14.22pp, +11.50pp），瓶颈在自提取质量。Cross-architecture DeBERTa NLI verifier 在 ProofWriter 上显示初步正向信号。\n\n---\n\n## Strengths\n\n**S1. 实验规模和系统性出色。** 6 模型 × 6 数据集 × 3 推理域覆盖高/中/低 SC 准确率区间，25+ 补救策略的穷举式搜索在负面结果论文中罕见，大幅增强结论可信度。[R1-S2, R1-S6, R2-S2]\n\n**S2. 统计方法论严谨。** TOST 等价性检验（±2pp margin）确认负面结果而非仅依赖 NHST，Bootstrap 95% CI（10,000 resamples）、BH 多重比较校正、统计功效分析均超出 NLP 论文平均水准。[R1-S4, R2-S1]\n\n**S3. Oracle controls 设计巧妙。** Gold FOL oracle 大幅提升性能（Mistral-7B FOLIO +29.90pp, Qwen-14B FOLIO +14.22pp, ProofWriter +11.50pp），精确分离聚合机制（sound）与提取质量（bottleneck）。[R1-S3, R2-S5]\n\n**S4. CJT 框架和量化诊断工具有独立贡献。** Effective-K（§5.1）、Bias Ratio（§3.3）、C_D diagnostic 将 SC 失效模式诊断从定性变为定量，可被后续工作直接复用。[R1-S1, R1-S5, R2-S3]\n\n**S5. Independence-Accuracy Trade-off（Figure 7）是最具洞察力的贡献。** 清晰展示同模型方法的 κ ≈ 0.40–0.47 ceiling，Debate 降 κ 但毁 accuracy，形成 Pareto 关系。[R2-S4]\n\n**S6. 叙事结构完整。** 假设建立 → 主实验否定 → 三重诊断 → 补救失败 → 跨架构出口 → 讨论，逻辑连贯。格式合规：8 页正文、Limitations 完整、双盲匿名、48 条引用。[R2-S6, R2-S7]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. FOL 术语误导，负面结论 scope 不清晰。** [R1-N1 critical, R2 agrees at warning]\n论文通篇使用 \"first-order logic (FOL) constraints\"，但 Limitations（p.21）承认提取结果 \"predominantly propositional ground clauses without quantifiers\"。数学域 extraction prompt 提取的是 equation/inequality/comparison，无量词。标题使用 \"Symbolic Constraints\" 无误，但正文大量出现 \"FOL constraints\" 有术语膨胀。\n- **Action**: (1) 统一改为 \"symbolic/logical constraints\"，仅在 Z3 接口描述中保留 \"FOL-style\"；(2) 报告含量词约束的比例（按域/模型）；(3) Discussion 讨论真正 FOL 提取是否改变结论。\n- **R2 缓解观点**: 命题逻辑 ⊂ FOL，如果更弱形式都失败，更强形式失败可能性只会更大——但这需要在论文中显式论证，不能让读者自己推断。\n\n**W2. Cross-architecture PoC 双重 underpowered。** [R1-N2 critical + R2-W2 warning, 双方交叉确认]\n- **生成端**（R1）: 仅 Mistral-7B 一个生成模型，不同模型有 Type A/B/C 不同行为模式。\n- **验证端**（R2）: FOLIO +2.94pp (n.s.) vs. ProofWriter SICA 自身 −2.83pp (p=0.014)，两个数据集方向相反。α=3 在 n=204 上有 overfitting 风险。\n- **综合**: §6 \"confirming the effect is not verifier-specific\" 仅基于三个 NLI 架构在同一生成模型上的一致性，不等于跨生成模型一致性。\n- **Action**: 至少补一个 Qwen2.5-14B 的 DeBERTa combo 实验（traces 已有）；将 §6 结论 qualify 为 \"preliminary signal on Mistral-7B ProofWriter\"；讨论 α selection 的 overfitting 风险。\n\n### Should-Fix（提升论文质量）\n\n**W3. 增量新颖性定位需加强。** [R2-W1 warning, R1 partial REBUT — **DIVERGENCE**]\n- **R2 立场**: Huang et al. (2024) self-correction failure、Stechly et al. (2025) self-verification limitations、Amonkar et al. (2025) LLM formalization quality、Chan et al. (2026) logical soundness limitations——核心洞察在概念层面已被覆盖。Excitement 2.5/5。\n- **R1 立场**: 本文测试了一个更强的假设——FOL + Z3 确定性 solver 能否绕过自然语言 self-correction 的局限。BR/C_D/Eff-K 是新的量化工具，先行工作停留在 \"doesn't work\"，本文给出 \"why, how much, where exactly\"。\n- **共识**: §2 Related Work 应更明确 position：不是重复 \"self-correction fails\"，而是 \"即便引入确定性形式验证（FOL + Z3），self-extraction 的 confirmation bias 仍然阻断这条路径\"。\n\n**W4. Domain + Model 覆盖范围与 Abstract 表述不匹配。** [R1-W3 + R2-W4, 双方共识]\n- Abstract \"across the full LLM capability range\" 仅 7B–32B 开源模型。\n- \"Three reasoning domains\" 中数学域全部 degenerate（SC ≥ 85%），主要结论限于 formal/logical reasoning。\n- **Action**: Abstract 修改为 \"across a range of open-source LLMs (7B–32B)\" + \"formal and logical reasoning domains, with exploratory results on mathematical reasoning\"。\n\n**W5. Symbolic Confirmation Bias 缺乏与 Turpin et al. (2024) unfaithful CoT 的理论连接。** [R2-W3, R1 agrees]\nBR = 1.97 可能是 unfaithful CoT 在 FOL 层面的投射。论文未区分 (a) 模型故意生成支持错误答案的约束 vs. (b) 约束生成与答案生成共享同一 biased representation。\n- **Action**: §3.3 增加 Turpin et al. 连接讨论。\n\n**W6. 种子复制 + 统计功效标注不足。** [R1-W1 + R2-W5, 双方共识]\nTable 1 大多数条件未标注 seed 数量，7 个条件 n ≤ 60 MDE 极大，未区分 confirmatory vs. exploratory。\n- **R2 缓解观点**: TOST 用 per-item paired comparison，统计结论本身 well-powered。但 Table 1 标注仍需改善。\n- **Action**: Table 1 增加 seed 列和 powered/exploratory 标注。\n\n**W7. 语义去重缺失 ablation。** [R1-W2 + R2-Q5, 双方共识]\nSyntactic dedup 可能系统性放大 verbose traces 权重。论文未报告去重前后约束数量比，未做 Z3 semantic equivalence ablation。\n- **Action**: 报告去重统计；讨论影响或做 ablation。\n\n**W8. 约束质量分析仅覆盖单一模型。** [R1-W4, R2 agrees]\nExtraction error taxonomy (N=804) 仅 Qwen2.5-14B on FOLIO + ProofWriter。91.8% discriminative rate 在 Type B/C 模型上可能不同。\n- **Action**: 扩展到 2-3 个模型，或明确限定 claim scope。\n\n### Nice-to-Have\n\n**W9.** Figure 5（intervention strategies summary）深埋 Appendix p.22，应移入正文——两位 Reviewer + 视觉审查均建议。[R2-W6, R1 agrees]\n\n**W10.** Figure 2 线性回归 R² ≈ 4.4%，需说明 R² 并讨论离群点影响。[R1-W5]\n\n**W11.** 83.3% confirmation bias 是 aggregate 数字，per-model 变异大（69%–94%），主文应报告 breakdown。[R1-Q3]\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成共识（[AGREE]）：\n1. **PoC 不足**: Cross-architecture PoC 在生成端（single model）和验证端（inconsistent datasets）双重 underpowered [R1-N2 + R2-W2]\n2. **术语修正**: \"FOL constraints\" 应改为 \"symbolic/logical constraints\" [R1-N1 + R2 agrees]\n3. **覆盖范围校准**: Abstract 的 domain 和 model claims 需 downscope [R1-W3 + R2-W4]\n4. **去重 ablation**: Syntactic-only dedup 需量化影响 [R1-W2 + R2-Q5]\n5. **Table 1 标注**: 需区分 powered vs. exploratory conditions [R1-W1 + R2-W5]\n6. **Missing refs**: Weng et al. (2023) 和 Madaan et al. (2023) 应引用 [R1 + R2]\n7. **Figure 5 提升**: 应从 Appendix 移入正文 [R1 + R2 + Visual Check]\n8. **Turpin 连接**: §3.3 应与 unfaithful CoT 框架建立理论联系 [R2-W3, R1 agrees]\n\n## Reviewer Divergence\n\n**核心分歧：增量新颖性评估（W3）**\n- **R1 (3.5)**: FOL + Z3 确定性验证路径的失败是非平凡实证贡献；BR/C_D/Eff-K 量化工具在先行工作中无对应物；实证 specificity 超越了概念层面的 \"self-correction fails\"。\n- **R2 (3.0)**: 核心洞察——\"自提取符号结构继承模型偏差\"——在概念层面已被 Huang/Stechly/Amonkar/Chan 覆盖；具体化到 FOL + SC 组合的增量有限。Excitement 2.5/5。\n- **Director 评估**: 这是 legitimate disagreement。论文的实证严谨性毋庸置疑，但 excitement/novelty 是区分 Main Conference 和 Findings 的关键。如果 AC 认为量化诊断工具（BR, Eff-K）和 Z3 deterministic path 的 specific test 构成 sufficient novelty，3.5 可辩护；如果认为概念增量有限，3.0 更合适。\n\n---\n\n## Questions for Authors\n\n1. 含一阶量词（∀, ∃）约束的比例？按域和模型报告。[R1-Q1]\n2. 是否在 Qwen/LLaMA 上测试过 DeBERTa NLI combo？[R1-Q2]\n3. 83.3% confirmation bias 的 per-model breakdown（Table 13 显示 69%–94% 变异）？[R1-Q3]\n4. 去重前后平均约束数量和唯一约束率？[R1-Q4]\n5. Fine-tuned FOL extractor 能否显著提升 discriminative rate？[R2-Q1]\n6. Figure 7 independence-accuracy trade-off 是否有 CJT-based 理论下界？[R2-Q2]\n7. DeBERTa NLI 在 ProofWriter 上 same-model SICA degradation（−2.83pp）的根本原因？[R2-Q3]\n\n---\n\n## Missing References\n\n**需要引用**（双方共识）：\n- Weng et al. (2023) \"Large Language Models are Better Reasoners with Self-Verification\" — 正面 self-verification 结果，需在 §2 讨论为何不推广到 FOL 约束提取\n- Madaan et al. (2023) \"Self-Refine: Iterative Refinement with Self-Feedback\" — iterative self-improvement 代表工作，与 §5.4 remediation strategies 直接相关\n\n**可选**：\n- Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\" — R2 建议，R1 认为非必须（calibration ≠ constraint extraction）\n- Lightman et al. (2024) \"Let's Verify Step by Step\" — R1 建议，但 R2 指出论文已引用（bib key: lightman2024prm）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending（未返回）**\n\n外部审稿于 2026-05-20 19:51 UTC 发起，尚未收到结果。内部审稿不等待外部结果。如后续收到，Research Director 可作为补充参考。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done**（3 warnings, 10 info）\n\n主要发现：\n- **[warning] 前 3 页无任何 figure/table**：正文前 37.5% 缺乏视觉锚点，审稿人需翻到 p.4 才见 Figure 1。建议将核心结果预览或 Figure 1 提前。\n- **[warning] Figure 1（SICA pipeline）仅单栏宽**：作为核心方法唯一图示，建议考虑 figure*（全宽）。\n- **[warning] Page 21 约 2/3 空白**：Extended Limitations 仅占页面 1/3，建议与后续 appendix 合并排布。\n- **[info] Figure 5（p.22）是全文信息量最高的可视化**，深埋 Appendix——与 R1/R2 建议一致，应考虑移入正文。\n- **[info] Figure 7 independence-accuracy trade-off 可视化设计优秀**，如有空间值得提升。\n- **[info] 无 LaTeX 渲染错误、未解析引用、公式乱码或 margin 溢出。**\n- **[info] 表格全部 booktabs 风格，排版规范。**\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | **3.75/5** — 方法论扎实，统计分析上乘；FOL 术语和 dedup 问题降低 claim 精度 |\n| Excitement | 3/5 | 2.5/5 | **2.75/5** — CJT 框架和 25+ 策略扫描有价值，但核心洞察增量新颖性有争议 |\n| Reproducibility | 4/5 | 4/5 | **4/5** — 详细 prompts、伪代码、参数报告；承诺代码公开；种子复制不一致扣分 |\n| **Overall** | **3.5** (Borderline Conference) | **3.0** (Findings) | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | **High** |\n\n**综合评分：3.0 — Findings**\n\n**评分理由：** 这是一篇方法论严谨、实验规模出色的负面结果论文。Symbolic Mirage 概念、BR/Eff-K 量化诊断工具、25+ 策略的系统性搜索对社区有明确参考价值。Oracle controls 有效分离了机制和提取质量问题。\n\n限制接收为 Findings 而非 Main Conference 的主要因素是：(1) 核心洞察相对于已有 self-verification failure 文献（Huang 2024, Stechly 2025）的增量新颖性有限——即使 R1 的 rebuttal 部分成立（Z3 deterministic path 是 specific contribution），概念层面的 overlap 仍然存在；(2) 唯一的正向贡献（cross-architecture PoC）在生成端和验证端双重 underpowered；(3) FOL 术语偏差使负面结论的 scope 不够清晰。\n\n**提升至 3.5 的路径：** 解决 W1（术语统一 + 量词分析）、W2（补 Qwen 模型 PoC 实验）、W3（加强 §2 novelty positioning），即可 borderline conference。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 动机清晰，CJT → independence bottleneck → symbolic extraction 逻辑链流畅\n- Contributions 3 点概括准确\n- \"FOL constraints\" 首次出现时应明确约束的实际 formalism 层级 [W1]\n\n### §2 Related Work\n- 覆盖充分，分 SC extensions、neuro-symbolic reasoning、test-time compute 三个子节\n- **缺**: Weng et al. (2023) positive self-verification 和 Madaan et al. (2023) Self-Refine 未引用\n- **缺**: 应更显式地 position 本文 vs. Huang/Stechly：不是 \"self-correction fails again\" 而是 \"even deterministic formal verification fails when extraction is self-sourced\" [W3]\n\n### §3 Background & Setup\n- §3.1 CJT 框架严谨，K_eff 公式引用正确\n- §3.2 SICA pipeline 描述清楚\n- §3.3 Symbolic Mirage 和 BR 定义清晰；但应与 Turpin et al. (2024) unfaithful CoT 建立理论连接 [W5]；C_D \"zero-valued\" 表述可更精确\n\n### §4 Experiments\n- Table 1 信息密度高，但需增加 seed 列和 powered/exploratory 标注 [W6]\n- Type A/B/C regime 分类有用\n- Oracle control 是论文最强 positive control\n\n### §5 Analysis\n- §5.1 Eff-K 是扎实的理论贡献\n- §5.2 83.3% BR 需报告 per-model breakdown（69%–94% 变异）[W11]\n- §5.3 TF-IDF cosine similarity 是合理 proxy 但应讨论局限\n- §5.4 25+ strategies Figure 5 应在正文 [W9]\n\n### §6 Cross-Architecture PoC\n- 方法设计合理（encoder-only NLI as external verifier）\n- 单生成模型 + 不一致数据集结果严重限制结论强度 [W2]\n- α selection 缺乏 principled justification，有 overfitting 风险\n\n### §7-8 Discussion & Conclusion\n- \"driver limits voting diversity\" vs. \"indirect collapse\" 双通道分析简洁有力\n- Figure 7 是论文最有洞察力的图之一——考虑移入正文\n- Conclusion 恰当总结负面发现和正向逃逸路线\n\n### Limitations\n- 诚实且全面\n- Extended Limitations (§Y) 与 main Limitations 有部分冗余\n\n### Appendices\n- 总体高质量，Appendix C (Z3), D (diagnostics), E (power analysis), G (case studies) 尤其有价值\n- 25 个 appendix 略多，部分可合并",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "report": "# 审稿报告 — Round 8 (Fresh Review)\n\n**论文**: \"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + Related Work + 写作质量)\n\n---\n\n## Summary\n\n本文研究 LLM 自提取的符号约束能否通过 Symbolic Invariant Consensus Aggregation (SICA)——基于 FOL 约束提取和 Z3 weighted partial MAX-SAT——改善 Self-Consistency majority voting。在 6 个模型（7B–32B）、3 个推理域、3000+ 条件评估中，自提取约束未能显著提升准确率。作者将此归因于 \"Symbolic Mirage\"：自提取约束是模型分布偏差的投射（confirmation bias rate 83.3%, BR ≈ 1.97+），trace 之间的 process-level 相关性（cosine similarity 0.69）远超 answer-level 独立性（κ ≈ 0.41）。25+ 补救策略均失败，揭示持久的 independence-accuracy trade-off。Oracle controls 确认聚合机制 sound（+29.90pp, +14.22pp, +11.50pp），瓶颈在自提取质量。Cross-architecture DeBERTa NLI verifier 在 ProofWriter 上显示初步正向信号。\n\n---\n\n## Strengths\n\n**S1. 实验规模和系统性出色。** 6 模型 × 6 数据集 × 3 推理域覆盖高/中/低 SC 准确率区间，25+ 补救策略的穷举式搜索在负面结果论文中罕见，大幅增强结论可信度。[R1-S2, R1-S6, R2-S2]\n\n**S2. 统计方法论严谨。** TOST 等价性检验（±2pp margin）确认负面结果而非仅依赖 NHST，Bootstrap 95% CI（10,000 resamples）、BH 多重比较校正、统计功效分析均超出 NLP 论文平均水准。[R1-S4, R2-S1]\n\n**S3. Oracle controls 设计巧妙。** Gold FOL oracle 大幅提升性能（Mistral-7B FOLIO +29.90pp, Qwen-14B FOLIO +14.22pp, ProofWriter +11.50pp），精确分离聚合机制（sound）与提取质量（bottleneck）。[R1-S3, R2-S5]\n\n**S4. CJT 框架和量化诊断工具有独立贡献。** Effective-K（§5.1）、Bias Ratio（§3.3）、C_D diagnostic 将 SC 失效模式诊断从定性变为定量，可被后续工作直接复用。[R1-S1, R1-S5, R2-S3]\n\n**S5. Independence-Accuracy Trade-off（Figure 7）是最具洞察力的贡献。** 清晰展示同模型方法的 κ ≈ 0.40–0.47 ceiling，Debate 降 κ 但毁 accuracy，形成 Pareto 关系。[R2-S4]\n\n**S6. 叙事结构完整。** 假设建立 → 主实验否定 → 三重诊断 → 补救失败 → 跨架构出口 → 讨论，逻辑连贯。格式合规：8 页正文、Limitations 完整、双盲匿名、48 条引用。[R2-S6, R2-S7]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. FOL 术语误导，负面结论 scope 不清晰。** [R1-N1 critical, R2 agrees at warning]\n论文通篇使用 \"first-order logic (FOL) constraints\"，但 Limitations（p.21）承认提取结果 \"predominantly propositional ground clauses without quantifiers\"。数学域 extraction prompt 提取的是 equation/inequality/comparison，无量词。标题使用 \"Symbolic Constraints\" 无误，但正文大量出现 \"FOL constraints\" 有术语膨胀。\n- **Action**: (1) 统一改为 \"symbolic/logical constraints\"，仅在 Z3 接口描述中保留 \"FOL-style\"；(2) 报告含量词约束的比例（按域/模型）；(3) Discussion 讨论真正 FOL 提取是否改变结论。\n- **R2 缓解观点**: 命题逻辑 ⊂ FOL，如果更弱形式都失败，更强形式失败可能性只会更大——但这需要在论文中显式论证，不能让读者自己推断。\n\n**W2. Cross-architecture PoC 双重 underpowered。** [R1-N2 critical + R2-W2 warning, 双方交叉确认]\n- **生成端**（R1）: 仅 Mistral-7B 一个生成模型，不同模型有 Type A/B/C 不同行为模式。\n- **验证端**（R2）: FOLIO +2.94pp (n.s.) vs. ProofWriter SICA 自身 −2.83pp (p=0.014)，两个数据集方向相反。α=3 在 n=204 上有 overfitting 风险。\n- **综合**: §6 \"confirming the effect is not verifier-specific\" 仅基于三个 NLI 架构在同一生成模型上的一致性，不等于跨生成模型一致性。\n- **Action**: 至少补一个 Qwen2.5-14B 的 DeBERTa combo 实验（traces 已有）；将 §6 结论 qualify 为 \"preliminary signal on Mistral-7B ProofWriter\"；讨论 α selection 的 overfitting 风险。\n\n### Should-Fix（提升论文质量）\n\n**W3. 增量新颖性定位需加强。** [R2-W1 warning, R1 partial REBUT — **DIVERGENCE**]\n- **R2 立场**: Huang et al. (2024) self-correction failure、Stechly et al. (2025) self-verification limitations、Amonkar et al. (2025) LLM formalization quality、Chan et al. (2026) logical soundness limitations——核心洞察在概念层面已被覆盖。Excitement 2.5/5。\n- **R1 立场**: 本文测试了一个更强的假设——FOL + Z3 确定性 solver 能否绕过自然语言 self-correction 的局限。BR/C_D/Eff-K 是新的量化工具，先行工作停留在 \"doesn't work\"，本文给出 \"why, how much, where exactly\"。\n- **共识**: §2 Related Work 应更明确 position：不是重复 \"self-correction fails\"，而是 \"即便引入确定性形式验证（FOL + Z3），self-extraction 的 confirmation bias 仍然阻断这条路径\"。\n\n**W4. Domain + Model 覆盖范围与 Abstract 表述不匹配。** [R1-W3 + R2-W4, 双方共识]\n- Abstract \"across the full LLM capability range\" 仅 7B–32B 开源模型。\n- \"Three reasoning domains\" 中数学域全部 degenerate（SC ≥ 85%），主要结论限于 formal/logical reasoning。\n- **Action**: Abstract 修改为 \"across a range of open-source LLMs (7B–32B)\" + \"formal and logical reasoning domains, with exploratory results on mathematical reasoning\"。\n\n**W5. Symbolic Confirmation Bias 缺乏与 Turpin et al. (2024) unfaithful CoT 的理论连接。** [R2-W3, R1 agrees]\nBR = 1.97 可能是 unfaithful CoT 在 FOL 层面的投射。论文未区分 (a) 模型故意生成支持错误答案的约束 vs. (b) 约束生成与答案生成共享同一 biased representation。\n- **Action**: §3.3 增加 Turpin et al. 连接讨论。\n\n**W6. 种子复制 + 统计功效标注不足。** [R1-W1 + R2-W5, 双方共识]\nTable 1 大多数条件未标注 seed 数量，7 个条件 n ≤ 60 MDE 极大，未区分 confirmatory vs. exploratory。\n- **R2 缓解观点**: TOST 用 per-item paired comparison，统计结论本身 well-powered。但 Table 1 标注仍需改善。\n- **Action**: Table 1 增加 seed 列和 powered/exploratory 标注。\n\n**W7. 语义去重缺失 ablation。** [R1-W2 + R2-Q5, 双方共识]\nSyntactic dedup 可能系统性放大 verbose traces 权重。论文未报告去重前后约束数量比，未做 Z3 semantic equivalence ablation。\n- **Action**: 报告去重统计；讨论影响或做 ablation。\n\n**W8. 约束质量分析仅覆盖单一模型。** [R1-W4, R2 agrees]\nExtraction error taxonomy (N=804) 仅 Qwen2.5-14B on FOLIO + ProofWriter。91.8% discriminative rate 在 Type B/C 模型上可能不同。\n- **Action**: 扩展到 2-3 个模型，或明确限定 claim scope。\n\n### Nice-to-Have\n\n**W9.** Figure 5（intervention strategies summary）深埋 Appendix p.22，应移入正文——两位 Reviewer + 视觉审查均建议。[R2-W6, R1 agrees]\n\n**W10.** Figure 2 线性回归 R² ≈ 4.4%，需说明 R² 并讨论离群点影响。[R1-W5]\n\n**W11.** 83.3% confirmation bias 是 aggregate 数字，per-model 变异大（69%–94%），主文应报告 breakdown。[R1-Q3]\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成共识（[AGREE]）：\n1. **PoC 不足**: Cross-architecture PoC 在生成端（single model）和验证端（inconsistent datasets）双重 underpowered [R1-N2 + R2-W2]\n2. **术语修正**: \"FOL constraints\" 应改为 \"symbolic/logical constraints\" [R1-N1 + R2 agrees]\n3. **覆盖范围校准**: Abstract 的 domain 和 model claims 需 downscope [R1-W3 + R2-W4]\n4. **去重 ablation**: Syntactic-only dedup 需量化影响 [R1-W2 + R2-Q5]\n5. **Table 1 标注**: 需区分 powered vs. exploratory conditions [R1-W1 + R2-W5]\n6. **Missing refs**: Weng et al. (2023) 和 Madaan et al. (2023) 应引用 [R1 + R2]\n7. **Figure 5 提升**: 应从 Appendix 移入正文 [R1 + R2 + Visual Check]\n8. **Turpin 连接**: §3.3 应与 unfaithful CoT 框架建立理论联系 [R2-W3, R1 agrees]\n\n## Reviewer Divergence\n\n**核心分歧：增量新颖性评估（W3）**\n- **R1 (3.5)**: FOL + Z3 确定性验证路径的失败是非平凡实证贡献；BR/C_D/Eff-K 量化工具在先行工作中无对应物；实证 specificity 超越了概念层面的 \"self-correction fails\"。\n- **R2 (3.0)**: 核心洞察——\"自提取符号结构继承模型偏差\"——在概念层面已被 Huang/Stechly/Amonkar/Chan 覆盖；具体化到 FOL + SC 组合的增量有限。Excitement 2.5/5。\n- **Director 评估**: 这是 legitimate disagreement。论文的实证严谨性毋庸置疑，但 excitement/novelty 是区分 Main Conference 和 Findings 的关键。如果 AC 认为量化诊断工具（BR, Eff-K）和 Z3 deterministic path 的 specific test 构成 sufficient novelty，3.5 可辩护；如果认为概念增量有限，3.0 更合适。\n\n---\n\n## Questions for Authors\n\n1. 含一阶量词（∀, ∃）约束的比例？按域和模型报告。[R1-Q1]\n2. 是否在 Qwen/LLaMA 上测试过 DeBERTa NLI combo？[R1-Q2]\n3. 83.3% confirmation bias 的 per-model breakdown（Table 13 显示 69%–94% 变异）？[R1-Q3]\n4. 去重前后平均约束数量和唯一约束率？[R1-Q4]\n5. Fine-tuned FOL extractor 能否显著提升 discriminative rate？[R2-Q1]\n6. Figure 7 independence-accuracy trade-off 是否有 CJT-based 理论下界？[R2-Q2]\n7. DeBERTa NLI 在 ProofWriter 上 same-model SICA degradation（−2.83pp）的根本原因？[R2-Q3]\n\n---\n\n## Missing References\n\n**需要引用**（双方共识）：\n- Weng et al. (2023) \"Large Language Models are Better Reasoners with Self-Verification\" — 正面 self-verification 结果，需在 §2 讨论为何不推广到 FOL 约束提取\n- Madaan et al. (2023) \"Self-Refine: Iterative Refinement with Self-Feedback\" — iterative self-improvement 代表工作，与 §5.4 remediation strategies 直接相关\n\n**可选**：\n- Kadavath et al. (2022) \"Language Models (Mostly) Know What They Know\" — R2 建议，R1 认为非必须（calibration ≠ constraint extraction）\n- Lightman et al. (2024) \"Let's Verify Step by Step\" — R1 建议，但 R2 指出论文已引用（bib key: lightman2024prm）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：pending（未返回）**\n\n外部审稿于 2026-05-20 19:51 UTC 发起，尚未收到结果。内部审稿不等待外部结果。如后续收到，Research Director 可作为补充参考。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：done**（3 warnings, 10 info）\n\n主要发现：\n- **[warning] 前 3 页无任何 figure/table**：正文前 37.5% 缺乏视觉锚点，审稿人需翻到 p.4 才见 Figure 1。建议将核心结果预览或 Figure 1 提前。\n- **[warning] Figure 1（SICA pipeline）仅单栏宽**：作为核心方法唯一图示，建议考虑 figure*（全宽）。\n- **[warning] Page 21 约 2/3 空白**：Extended Limitations 仅占页面 1/3，建议与后续 appendix 合并排布。\n- **[info] Figure 5（p.22）是全文信息量最高的可视化**，深埋 Appendix——与 R1/R2 建议一致，应考虑移入正文。\n- **[info] Figure 7 independence-accuracy trade-off 可视化设计优秀**，如有空间值得提升。\n- **[info] 无 LaTeX 渲染错误、未解析引用、公式乱码或 margin 溢出。**\n- **[info] 表格全部 booktabs 风格，排版规范。**\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5/5 | 4/5 | **3.75/5** — 方法论扎实，统计分析上乘；FOL 术语和 dedup 问题降低 claim 精度 |\n| Excitement | 3/5 | 2.5/5 | **2.75/5** — CJT 框架和 25+ 策略扫描有价值，但核心洞察增量新颖性有争议 |\n| Reproducibility | 4/5 | 4/5 | **4/5** — 详细 prompts、伪代码、参数报告；承诺代码公开；种子复制不一致扣分 |\n| **Overall** | **3.5** (Borderline Conference) | **3.0** (Findings) | **3.0 (Findings)** |\n| Confidence | 4/5 | 4/5 | **High** |\n\n**综合评分：3.0 — Findings**\n\n**评分理由：** 这是一篇方法论严谨、实验规模出色的负面结果论文。Symbolic Mirage 概念、BR/Eff-K 量化诊断工具、25+ 策略的系统性搜索对社区有明确参考价值。Oracle controls 有效分离了机制和提取质量问题。\n\n限制接收为 Findings 而非 Main Conference 的主要因素是：(1) 核心洞察相对于已有 self-verification failure 文献（Huang 2024, Stechly 2025）的增量新颖性有限——即使 R1 的 rebuttal 部分成立（Z3 deterministic path 是 specific contribution），概念层面的 overlap 仍然存在；(2) 唯一的正向贡献（cross-architecture PoC）在生成端和验证端双重 underpowered；(3) FOL 术语偏差使负面结论的 scope 不够清晰。\n\n**提升至 3.5 的路径：** 解决 W1（术语统一 + 量词分析）、W2（补 Qwen 模型 PoC 实验）、W3（加强 §2 novelty positioning），即可 borderline conference。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- 动机清晰，CJT → independence bottleneck → symbolic extraction 逻辑链流畅\n- Contributions 3 点概括准确\n- \"FOL constraints\" 首次出现时应明确约束的实际 formalism 层级 [W1]\n\n### §2 Related Work\n- 覆盖充分，分 SC extensions、neuro-symbolic reasoning、test-time compute 三个子节\n- **缺**: Weng et al. (2023) positive self-verification 和 Madaan et al. (2023) Self-Refine 未引用\n- **缺**: 应更显式地 position 本文 vs. Huang/Stechly：不是 \"self-correction fails again\" 而是 \"even deterministic formal verification fails when extraction is self-sourced\" [W3]\n\n### §3 Background & Setup\n- §3.1 CJT 框架严谨，K_eff 公式引用正确\n- §3.2 SICA pipeline 描述清楚\n- §3.3 Symbolic Mirage 和 BR 定义清晰；但应与 Turpin et al. (2024) unfaithful CoT 建立理论连接 [W5]；C_D \"zero-valued\" 表述可更精确\n\n### §4 Experiments\n- Table 1 信息密度高，但需增加 seed 列和 powered/exploratory 标注 [W6]\n- Type A/B/C regime 分类有用\n- Oracle control 是论文最强 positive control\n\n### §5 Analysis\n- §5.1 Eff-K 是扎实的理论贡献\n- §5.2 83.3% BR 需报告 per-model breakdown（69%–94% 变异）[W11]\n- §5.3 TF-IDF cosine similarity 是合理 proxy 但应讨论局限\n- §5.4 25+ strategies Figure 5 应在正文 [W9]\n\n### §6 Cross-Architecture PoC\n- 方法设计合理（encoder-only NLI as external verifier）\n- 单生成模型 + 不一致数据集结果严重限制结论强度 [W2]\n- α selection 缺乏 principled justification，有 overfitting 风险\n\n### §7-8 Discussion & Conclusion\n- \"driver limits voting diversity\" vs. \"indirect collapse\" 双通道分析简洁有力\n- Figure 7 是论文最有洞察力的图之一——考虑移入正文\n- Conclusion 恰当总结负面发现和正向逃逸路线\n\n### Limitations\n- 诚实且全面\n- Extended Limitations (§Y) 与 main Limitations 有部分冗余\n\n### Appendices\n- 总体高质量，Appendix C (Z3), D (diagnostics), E (power analysis), G (case studies) 尤其有价值\n- 25 个 appendix 略多，部分可合并",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-20T20:08:44.364199+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4017
}
```

</details>

---


### Assistant

_source line 792 · 2026-05-20T20:08:52.797818+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿完成摘要：**

- **综合评分：3.0 (Findings)**
- R1: 3.5 (Borderline Conference) / R2: 3.0 (Findings)
- **核心分歧**：增量新颖性评估——R1 认为 Z3 deterministic path + 量化工具（BR, Eff-K）构成充分贡献；R2 认为概念层面已被 Huang/Stechly 覆盖
- **8 项共识**：术语修正、PoC 不足、覆盖范围校准、去重 ablation、Table 1 标注、missing refs、Figure 5 提升、Turpin 连接
- **提升至 3.5 的路径**：W1（术语统一）+ W2（补 Qwen PoC）+ W3（novelty positioning）
- **外部审稿**：pending，未阻塞报告
- **视觉审查**：done，3 warnings（前 3 页无视觉锚点、Figure 1 单栏偏窄、p.21 大面积空白）
- **Issue Tracker**：已同步更新 11 个新 issue（R8-N1/N2, R8-W1~W8, R8-I1~I3）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 50

## Round 50

86 recorded events


### User

_source line 793 · 2026-05-21T01:36:12.952271+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-21T01:36:19.488386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-21T01:36:19.489632+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-21T01:36:27.834840+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-21T01:36:27.886045+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-21T01:36:31.572146+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-21T01:36:33.086496+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (147 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-077-generalization-kappa: Generalization: independence bottleneck (high κ) applies to Debate and Diverse-Prompt aggregation, not just SC+SICA. 在 Mistral-7B FOLIO-204 上测量 3 种聚合方式的 Fleiss' κ + Eff-K: (a) Standard SC (复用 exp-033 traces), (b) LLM-Debate traces (4组×3轮=12 answer points), (c) Diverse-Prompt traces (4种 prompt×3次=12). 如果三种方式 κ 均 > 0.4，证明 independence bottleneck 是 same-model aggregation 的通病。（准备中）\n- exp-063-llama8b-folio204（准备中）\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **exp-092-llama8b-pw-nli-combo** (success): LLaMA-3.1-8B ProofWriter NLI combo: DeBERTa-large-MNLI standalone (55%) < SC (70%)，capability gap = -15pp。验证 NLI combo 是否在第二个 model family 上也能提升 SC accuracy。 ← 基于 exp-090-r-nli-proofwriter\n- **exp-091-qwen14b-pw-nli-combo** (success): Qwen2.5-14B ProofWriter NLI combo: DeBERTa-large-MNLI standalone (55%) < SC (73.50%)，capability gap = -18.50pp。根据 Push A capability gap 单调关系，combo gain 应介于 Qwen3 (+1.83pp) 和 Mistral (+10.67pp) 之间。 ← 基于 exp-090-r-nli-proofwriter\n- **exp-wave3-dir-g-decoupling** (negative): Decoupling: 将 FOL 约束提取与答案生成解耦——先生成答案 trace，再独立提取 FOL 约束（不暴露答案给约束提取 prompt），可以打破 confirmation bias 因果链。Conservative 策略：截断 trace 中答案相关内容后再提取约束。\n\n## 趋势\n成功 38 / 负向 76
…[truncated 1451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1514
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-21T01:36:33.237807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-21T01:36:33.590857+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage{tikz}
18	\usetikzlibrary{arrows.meta,positioning,calc,fit}
19	\usepackage{listings}
20	\usepackage{algorithm}
21	\usepackage{algpseudocode}
22	\usepackage{hyperref}
23	\usepackage{cleveref}
24	
25	\lstset{
26	  basicstyle=\small\ttfamily,
27	  breaklines=true,
28	  frame=single,
29	  xleftmargin=1em,
30	  xrightmargin=1em,
31	  aboveskip=0.5em,
32	  belowskip=0.5em,
33	}
34	
35	\graphicspath{{../figures/paper/}{figures/}}
36	
37	\title{Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints\\Do Not Improve LLM Reasoning}
38	
39	\author{Anonymous}
40	
41	\begin{document}
42	\maketitle
43	
44	\input{abstract}
45	
46	\input{introduction}
47	
48	\input{related_work}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\input{analysis}
55	
56	\input{solutions}
57	
58	\input{discussion}
59	
60	\input{conclusion}
61	
62	\section*{Limitations}
63	\input{limitations_content}
64	
65	\bibliography{references}
66	
67	\appendix
68	\input{appendix}
69	
70	\end{document}
71	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-21T01:36:33.591432+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-21T01:36:39.673016+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, I found informatio
…[truncated 1335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6081
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-21T01:36:49.219565+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-21T01:36:49.420982+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-21T01:36:49.422607+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 cycle deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 cycle deadline submission"
  }
}
```

</details>

---


### Tool call

_source line 807 · 2026-05-21T01:36:50.328330+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-21T01:36:50.932239+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-21T01:36:55.006085+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Port
…[truncated 877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4677
}
```

</details>

---


### Tool result

_source line 810 · 2026-05-21T01:36:59.435236+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 cycle deadline submission"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) submission deadlines. However, the results primarily show information about the January 2026 cycle and earlier cycles. Let me search more specifically for the May 2026 cycle deadline.

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics"
…[truncated 3249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 10012
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-21T01:36:59.435780+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8503
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-21T01:37:07.261592+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, citation format, ARR submission deadline for May 2026 cycle, commitment deadline, any special rules about limitations section. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, citation format, ARR submission deadline for May 2026 cycle, commitment deadline, any special rules about limitations section. Be comprehensive."
  }
}
```

</details>

---


### Tool call

_source line 813 · 2026-05-21T01:37:08.640855+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Find the May 2026 ARR cycle submission deadline, review timeline, and any relevant dates. List all dates for the May 2026 cycle."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Find the May 2026 ARR cycle submission deadline, review timeline, and any relevant dates. List all dates for the May 2026 cycle."
  }
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-21T01:37:10.204292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-21T01:37:10.456360+00:00_

1	Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
2	We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
3	Across six open-source LLMs (7B--32B, from Mistral-7B at 54\% SC to Qwen3-14B thinking mode at 86\% SC) and three logical reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find that self-extracted constraints do not improve majority voting at any capacity level: none of sixteen non-degenerate conditions shows a significant positive effect; TOST equivalence tests (margin $\pm 2$\,pp) establish equivalence for four conditions, while five show genuine SICA--SC differences---four of which are negative.
4	We identify \emph{symbolic confirmation bias} as the root cause: on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC.
5	Process-level analysis reveals a deeper bottleneck: chain-of-thought cosine similarity ($0.69$) far exceeds answer-level Fleiss' $\kappa$ ($0.41$), indicating that traces share reasoning processes even when they diverge on answers.
6	Twenty-plus same-model remediation strategies spanning fifteen families all fail, revealing a persistent independence-accuracy trade-off at the 7B--32B scale: methods that increase trace independence destroy accuracy (Debate: $\kappa = 0.15$, $-18.6$\,pp), while methods preserving accuracy cannot break the correlation floor ($\kappa \geq 0.40$ across three model families).
7	Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp and $+14.22$\,pp on FOLIO, $+11.50$\,pp ProofWriter; $p < 0.001$); same-model self-extraction captures only ${\sim}$12\% of the oracle ceiling.
8	C
…[truncated 261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-21T01:37:10.507366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-21T01:37:11.060127+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding Effective-$K = 1.20$--$3.62$ for nominal $K = 12$: traces beyon
…[truncated 4023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-21T01:37:11.060643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-21T01:37:11.111385+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and extensions.}
5	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).
6	
7	\paragraph{Neuro-symbolic reasoning.}
8	Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} translate problems into formal logic for external provers; LINC documents ${\sim}$40\% translation errors. Program-aided approaches offload computation to code interpreters \citep{gao2023pal,chen2023program,lyu2023faithful}, but program generation remains LLM-dependent, paralleling the self-extraction bottleneck we identify. Recent extensions---CLOVER \citep{ryu2025clover}, DyLoS \citep{xu2026dylos}, Aristotle \citep{li2025aristotle}, FoVer \citep{wang2025fover}, VERGE \citep{singh2026verge}, LogicAgent \citep{luo2025logicagent}---add compositional translation, solver selection, decomposition, trained verifiers, and formal refinement, each introducing capabilities beyond the reasoning model. \citet{amonkar2025realitycheck} show that LLM formalization degrades with complexity; \citet{chan2026position} argue that logical soundness is not a reliable criterion for neurosymbolic verification with LLMs. Our oracle controls confirm the mechanism is sound ($+29.90$/$+14.22$\,pp FOLIO, $+11.50$\,pp ProofWriter); the failure localizes to self-extraction quality (\S\ref{sec:oracle}).
9	
10	\paragraph{Test-time compute and verification.}
11	Scaling test-time computat
…[truncated 3483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 820 · 2026-05-21T01:37:11.717140+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long papers:** 8 pages of content
- **Short papers:** 4 pages of content
- **Camera-ready versions:** +1 additional page (9 pages for long, 5 pages for short)

## Templates & Format
Authors must follow "all of the ARR submission requirements," with specific guidance available via the ARR CFP link regarding templates and formatting standards.

## Anonymity Rules
- Double-blind review process maintained
- "Reviewers will not see authors, nor will authors see reviewers"
- Reviews on ARR remain confidential
- Authors may optionally make anonymized submitted articles publicly visible

## Appendices & Supplementary Materials
Optional supplementary materials, appendices, software, and data are permitted per ARR guidelines (specifics referenced in ARR CFP).

## Citation & Comparison Standards
Citation practices and comparative methodology follow "ARR submission requirements" (full details in ARR CFP document).

## Key Deadlines
- **ARR submission deadline:** "May 25, 2026"
- **Commitment deadline:** "August 2, 2026"
- **Reviewer registration:** "May 27, 2026"

## Limitations Section
A limitations section is required per ARR ethics policy requirements.

## Special Note
All deadlines are "11:59PM UTC-12:00 ('anywhere on Earth')."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 4455
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-21T01:37:12.220626+00:00_

# May 2026 ARR Cycle Dates

Based on the reviewing schedule table, here are all key dates for the May 2026 cycle:

| Event | Date |
|-------|------|
| Submission Deadline | May 25, 2026 |
| Reviewer Registration | May 27, 2026 |
| Reviews Due | June 29, 2026 |
| Author Response Period | July 7–13, 2026 |
| Meta-reviews Released | July 30, 2026 |
| Cycle End | August 2, 2026 |

**Publication Venue Commitment:**
The document notes that "May 25, 2026" serves as the final ARR submission date for both "EMNLP 2026" and "AACL 2026," with commitment deadlines of August 2 and August 26, 2026 respectively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 3579
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-21T01:37:19.996067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-21T01:37:20.349448+00:00_

1	\section{Background \& Setup}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \to \infty$ \citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \citet{ladha1992correlated} and the design-effect framework of \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
11	\end{equation}
12	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. Note that $\kappa$ is a qualitative proxy for the intraclass correlation coefficient (ICC); we use $K_{\text{eff}}$ as an interpretive indicator rather than a precise statistical estimator. This \emph{independence bottleneck} motivates our investigation.
13	
14	\subsection{SICA Pipeline}
15	\label{sec:pipeline}
16	
17	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
18	
19	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
20	
21	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt reque
…[truncated 6273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-21T01:37:20.350041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-21T01:37:20.803032+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models on three reasoning domains with over 3,000 condition-evaluations across ${\sim}$1,250 unique instances. Beyond accuracy comparisons, we conduct diagnostic analyses of symbolic confirmation bias and process-level trace independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B parameters).
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$; extraction at $T_{\text{ext}}{=}0.3$. Z3 timeout: 10s. $\alpha{=}0.5$. Statistical significance via McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs from 10,000 resamples for $n \geq 200$.
14	
15	\paragraph{Computational cost.} On Mistral-7B FOLIO ($K{=}12$), SICA takes $4.5{\times}$ SC wall-clock time; constraint extraction ($K$ additional LLM calls) accounts for 76\% of overhead, Z3 solving is negligible (${<}0.1\%$).
16	
17	
18	\subsection{Main Results}
19	\label{sec:main-results}
20	
21	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline. We identify three empirical regimes (thresholds observation-driven, not theoretically derived). SICA effectiveness depends sharply on this accuracy regime.
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{SICA vs.\ SC across
…[truncated 4123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-21T01:37:20.954487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-21T01:37:21.208621+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	This section tests the three predictions of the Symbolic Mirage hypothesis (\S\ref{sec:mirage}): trace correlation and $K_{\text{eff}}$ collapse (\S\ref{sec:effective-k}), systematic confirmation bias with $\text{BR} > 1$ across architectures (\S\ref{sec:confirmation-bias}), process-level independence (\S\ref{sec:process-kappa}), supporting diagnostics (\S\ref{sec:diagnostics}), and the inescapability of the mirage under twenty-plus same-model interventions (\S\ref{sec:remediation}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$. The four Mistral-7B FOLIO seeds produce $\kappa \in [0.41, 0.51]$, yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp---seed-level constraint quality, not independence alone, appears to influence the variation. Two conditions are jointly necessary for positive $\Delta$: sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and sufficient SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ produces significant degradation). Cross-model validation confirms universality: all four families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}; Appendix~\ref{app:cross-model-kappa}).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3pt}
15	\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$; positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each.}
16	\label{tab:independence}
17	\begin{tabular}{@{}llccrr@{}}
18	\toprule
19	Model & Condition & $\kappa$ & $K_{\text{eff}}$ & SC (\%) & $
…[truncated 5129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 254
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-21T01:37:21.209220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-21T01:37:21.259961+00:00_

1	\section{Cross-Architecture Proof-of-Concept}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Method.}
6	We test this with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs into \textsc{entailment}, \textsc{contradiction}, or \textsc{neutral}. In combo mode, the NLI verdict is integrated with SC's $K$ votes via weight $w$: each NLI-supporting vote counts $w$ times. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$), because NLI classification requires (premise, conclusion) pairs that these datasets naturally provide; multiple-choice datasets (LogiQA) lack this structure.
7	
8	\paragraph{Main result.}
9	DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo mode yields $+1.96$\,pp at $w{=}1$ and $+2.94$\,pp at $w{=}3$ (both n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+3.50$\,pp ($p = 0.013$) and $w{=}5$ reaches $+10.67$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp, $p = 0.014$; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). We report $w{=}3$ as primary; higher weights risk overfitting. After Benjamini--Hochberg correction ($m{=}6$), ProofWriter $w{=}3$ remains significant (adjusted $p = 0.038$) and $w{=}5$ ($p < 0.001$); FOLIO comparisons are non-significant. Per-label caveat: DeBERTa over-predicts \textsc{False} on ProofWriter (67.8\%) and performs poorly on \textsc{Unknown} (3.5\% accuracy), as NLI's ``neutral'' fails to capture logical unknowability.
10	
11	\paragraph{Why it works.}
12	The 406M encoder-only DeBERTa and 7B decoder-only Mistral share no architecture, training data, or inference mechanism, satisfying the independence condition that same-model sampling cannot provide (\S\ref{sec:mirage}). 
…[truncated 2874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-21T01:37:26.434406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-21T01:37:26.786175+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The Symbolic Mirage manifests through two channels: the \emph{direct} limits voting diversity ($K_{\text{eff}} < 2$), while the \emph{indirect} collapses MAX-SAT to vote counting (Eq.~\ref{eq:degenerate}). The bias ratio gradient ($4.97\times$ Mistral $> 3.93\times$ Qwen $> 2.88\times$ LLaMA) aligns with regime boundaries; thinking-mode degeneration ($\kappa = 0.91$, Qwen3) confirms this scales with capability. For practitioners, $C_0$ with SC accuracy predicts when augmentation will fail. The independence-accuracy trade-off instantiates the classic ensemble tension \citep{krogh1994neural, brown2005diversity}. If traces do not reflect actual reasoning \citep{turpin2024language}, the mirage is inherent to extraction. Our extensions of prior negative results \citep{huang2024selfcorrect, stechly2025selfverification}---Effective-$K$, bias ratio, and process-level similarity---provide reusable diagnostics for any trace-aggregation system.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-21T01:37:26.786607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-21T01:37:27.238844+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We identify the Symbolic Mirage: self-extracted logical constraints project the generating model's biases rather than providing independent verification, explaining why twenty-plus remediation strategies cannot break the same-model ceiling. Oracle controls confirm the mechanism is sound given uncontaminated constraints; a cross-architecture proof-of-concept escapes the mirage entirely. For practitioners, architecturally independent signals remain necessary; detecting the Symbolic Mirage in other self-verification domains is a critical open direction.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-21T01:37:27.239301+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-21T01:37:27.390376+00:00_

1	\paragraph{Scale and language.}
2	All models range from 7B to 32B parameters; whether the independence bottleneck persists at larger scales (70B+) or with reasoning-specialized models is untested. All datasets are English-language logical reasoning benchmarks with discrete answer spaces. We do not evaluate trained symbolic extractors, external solvers with verified grounding, or multilingual settings. Oracle analysis is limited to FOLIO and ProofWriter (gold annotations available); extending to commonsense reasoning requires constructing comparable gold constraint sets. The cross-architecture NLI verifier (\S\ref{sec:cross-arch}) provides no benefit on LogiQA (combo $\Delta \leq +1$\,pp, all $p > 0.5$), indicating that cross-architecture escape requires task-verifier alignment---NLI is effective only when the task naturally decomposes into premise-conclusion entailment. Even on compatible tasks, NLI gain vanishes when the capability gap is large (Qwen3-14B ProofWriter: SC 85\% vs.\ DeBERTa 55\%, gap $= -30$\,pp, $\Delta \leq +1.00$\,pp, n.s.), though moderate negative gaps still yield significant gains (LLaMA-3.1-8B: gap $= -15$\,pp, $+4.17$\,pp, $p = 0.004$; \S\ref{sec:cross-arch}).
3	
4	\paragraph{Statistical power.}
5	The per-label complementarity analysis of the cross-architecture NLI result (\S\ref{sec:cross-arch}) involves small cell sizes (e.g., 42 \textsc{False} problems, 69 \textsc{Unknown} problems); per-label McNemar tests would be underpowered. The bias ratio metric ($4.97\times$) was initially computed on a single condition (Mistral-7B FOLIO, $n = 204$); cross-model replication (Table~\ref{tab:cross-model-bias}) confirms the pattern but is limited to FOLIO. Four-seed replication shows 2 of 4 seeds yielding null or negative results, and the intermediate-SC region is narrow (SC $\approx$ 50--55\%). The process-level similarity metric uses TF-IDF representations (a lower bound on true process similarity). Pairwise Pearson $r$ between traces (mean $0.625$
…[truncated 1075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-21T01:37:27.793386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-21T01:37:28.046482+00:00_

1	
2	\section{Regime Scatter Plot}
3	\label{app:regime-scatter}
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\columnwidth]{f2_regime_scatter}
8	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--55\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: significant degradation ($p = 0.014$).}
9	\label{fig:regime-scatter}
10	\end{figure}
11	
12	\section{Prompt Templates}
13	\label{app:prompts}
14	
15	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
16	
17	\paragraph{System Prompt.}
18	
19	\begin{lstlisting}
20	You are a constraint extraction tool. Output ONLY
21	valid JSON. Do NOT solve problems, reason about
22	correctness, or think step-by-step. Extract
23	constraints from the given trace exactly as stated.
24	\end{lstlisting}
25	
26	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
27	
28	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
29	
30	\begin{lstlisting}
31	Extract mathematical constraints from this reasoning
32	trace as a JSON object.
33	
34	Rules:
35	- type: "equation", "inequality", or "predicate"
36	- expression: human-readable, e.g. "x + y == 14"
37	- z3_formula: a single comparison expression in
38	  Python Z3 syntax
39	- source_step: step number where the constraint
40	  appears
41	- Use variable names from the trace
42	
43	z3_formula MUST follow these rules:
44	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
45	  /, **, %
46	- Use individual named variables: a1, a2, a3...
47	  NOT arrays 
…[truncated 57230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-21T01:37:34.540472+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-21T01:37:34.591513+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-21T01:37:38.479808+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-21T01:37:38.580655+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-21T01:37:41.473239+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-21T01:37:41.523905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-21T01:37:44.743523+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read local file project",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read local file project",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-21T01:37:44.794240+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-21T01:37:48.914341+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-21T01:37:50.220939+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-21T01:37:50.573371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-21T01:37:50.925539+00:00_

1	% References for SICA Capability Trap paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% Program-Aided Reasoning %%%
5	
6	@inproceedings{gao2023pal,
7	  title={{PAL}: Program-aided Language Models},
8	  author={Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham},
9	  booktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},
10	  year={2023}
11	}
12	
13	@article{chen2023program,
14	  title={Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks},
15	  author={Chen, Wenhu and Ma, Xueguang and Wang, Xinyi and Cohen, William W.},
16	  journal={Transactions on Machine Learning Research},
17	  year={2023}
18	}
19	
20	@inproceedings{lyu2023faithful,
21	  title={Faithful Chain-of-Thought Reasoning},
22	  author={Lyu, Qing and Havaldar, Shreya and Stein, Adam and Zhang, Li and Rao, Delip and Wong, Eric and Apidianaki, Marianna and Callison-Burch, Chris},
23	  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
24	  year={2023}
25	}
26	
27	%%% Theoretical Foundations %%%
28	
29	@book{condorcet1785,
30	  title={Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
31	  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},
32	  year={1785},
33	  publisher={Imprimerie Royale},
34	  address={Paris}
35	}
36	
37	@article{austensmith1996,
38	  title={Information Aggregation, Rationality, and the {C}ondorcet Jury Theorem},
39	  author={Austen-Smith, David and Banks, Jeffrey S.},
40	  journal={American Political Science Review},
41	  volume={90},
42	  number={1},
43	  pages={34--45},
44	  year={1996}
45	}
46	
47	@article{ladha1992correlated,
48	  title={The {C}ondorcet Jury Theorem, Free Speech, and Corre
…[truncated 5691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-21T01:37:50.925966+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-21T01:37:50.976456+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/review_director_9c155b71.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-21T01:37:56.862454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-21T01:37:56.863459+00:00_

1	# Round 1-7 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 24307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-21T01:37:57.065751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "offset": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "offset": "200"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-21T01:37:57.066418+00:00_

200	@inproceedings{du2023improving,
201	  title={Improving Factuality and Reasoning in Language Models through Multiagent Debate},
202	  author={Du, Yilun and Li, Shuang and Torralba, Antonio and Tenenbaum, Joshua B. and Mordatch, Igor},
203	  booktitle={ICML},
204	  year={2024}
205	}
206	
207	%%% Benchmarks and Datasets %%%
208	
209	@article{han2022folio,
210	  title={{FOLIO}: Natural Language Reasoning with First-Order Logic},
211	  author={Han, Simeng and Schoelkopf, Hailey and Zhao, Yilun and Qi, Zhenting and Riddell, Martin and Benson, Luke and Sun, Lucy and Zubova, Ekaterina and Qiao, Yujie and Burtell, Matthew and Peng, David and Fan, Jonathan and Liu, Yi and Wong, Brian and Sailor, Malcolm and Ni, Ansong and Nan, Linyong and Kasai, Jungo and Yu, Tao and Zhang, Rui and Joty, Shafiq and Fabbri, Alexander R. and Kryscinski, Wojciech and Lin, Xi Victoria and Xiong, Caiming and Radev, Dragomir},
212	  journal={arXiv preprint arXiv:2209.00840},
213	  year={2022}
214	}
215	
216	@inproceedings{tafjord2021proofwriter,
217	  title={{ProofWriter}: Generating Implications, Proofs, and Abductive Statements over Natural Language},
218	  author={Tafjord, Oyvind and Dalvi, Bhavana and Clark, Peter},
219	  booktitle={ACL Findings},
220	  year={2021}
221	}
222	
223	@article{geva2021strategyqa,
224	  title={Did {Aristotle} Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies},
225	  author={Geva, Mor and Khashabi, Daniel and Segal, Elad and Khot, Tushar and Roth, Dan and Berant, Jonathan},
226	  journal={TACL},
227	  year={2021}
228	}
229	
230	@inproceedings{liu2020logiqa,
231	  title={{LogiQA}: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning},
232	  author={Liu, Jian and Cui, Leyang and Liu, Hanmeng and Huang, Dandan and Wang, Yile and Zhang, Yue},
233	  booktitle={IJCAI},
234	  pages={3622--3628},
235	  year={2020}
236	}
237	
238	%%% Negative Results / Analysis Papers %%%
239	
240	@inproceedings{stechly2025selfverificat
…[truncated 7920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-21T01:37:57.419071+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-21T01:37:57.519868+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-21T01:38:03.141794+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-21T01:38:03.292781+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-21T01:38:06.224504+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-21T01:38:06.328931+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516
…[truncated 9549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-21T01:38:09.783731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-21T01:38:09.834384+00:00_

1	_next_id: 2
2	constraints:
3	- id: C001
4	  added: 2026-05-18 17:54 UTC
5	  summary: 所有实验代码写完后必须先 dry-run 验证（python 可用性、路径存在性、端口无冲突、数据文件存在）再正式部署运行
6	  scope: worker
7	  reason: 多次出现代码部署后才发现 python command not found、模型路径不存在、GPU/端口冲突等低级错误，浪费 GPU 时间和调试周期。用户明确要求。
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-21T01:38:15.318054+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "glob": "*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-21T01:38:15.368736+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-21T01:38:18.993419+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/agent-ml-research",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/agent-ml-research",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-21T01:38:19.044074+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-21T01:38:41.059517+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract all submission format requirements: page limits for long and short papers, template/style files required, anonymization rules, appendix rules, supplementary material policy, ethics requirements, limitations section rules, citation format, and any other formatting guidelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract all submission format requirements: page limits for long and short papers, template/style files required, anonymization rules, appendix rules, supplementary material policy, ethics requirements, limitations section rules, citation format, and any other formatting guidelines."
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-21T01:38:48.293490+00:00_

# ACL Rolling Review Submission Format Requirements

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited references
- Unlimited space after conclusion for limitations (required) and optional ethical considerations section

**Short Papers:**
- Up to 4 pages of content
- Unlimited references
- Unlimited space after conclusion for limitations (required) and optional ethical considerations section

Submissions exceeding length requirements are subject to desk rejection.

## Style and Templates

Papers must follow the "official ACL style template" and conform to ACL formatting guidelines. Authors cannot modify style files or use templates from other conferences. Non-conforming submissions face rejection without review.

## Anonymization Rules

Two-way anonymization is required:
- Exclude author names and affiliations
- Avoid self-references revealing identity (use "Smith showed..." instead of "We showed...")
- Do not reference documents unavailable to reviewers
- Anonymize supplementary materials and repository links
- Avoid file hosting services tracking downloads (e.g., Dropbox)

Anonymity violations result in desk rejection.

## Limitations Section

A dedicated "Limitations" section is mandatory, appearing before references. This section:
- Does not count toward page limits
- Cannot introduce new methods, analysis, or results
- Discusses constraints of presented work only

Papers lacking this section face desk rejection.

## Appendices and Supplementary Materials

**Appendices:**
- Follow double-column formatting (with approved exceptions)
- Do not count toward page limits
- Must be anonymized
- Should not contain material essential for assessing novelty or claims

**Software/Data:**
- Submit as single .tgz or .zip archives
- Use anonymized repositories (e.g., Anonymous GitHub)
- Avoid cloud services with download tracking

Reviewers are not obligated to review appendices.

## Ethics Requirements

Authors must:
- Complete the responsible NLP resear
…[truncated 617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 7233
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-21T01:39:23.507384+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-21T01:39:23.560348+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-21T01:39:28.243044+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-21T01:40:01.829280+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 33586
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-21T01:40:03.338463+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\n- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）\n- **论文路径**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n- **投稿类别**: Long paper（8 页正文 + 无限参考文献）\n- **审稿制度**: Double-blind（ACL 模板，`\\usepackage[review]{acl}`）\n- **Limitations**: 必须在参考文献前，不计入页数\n- **附录**: 不计入页数，审稿人无义务阅读\n\n## 论文概述\n负面结果论文。提出 SICA（Symbolic Invariant Consensus Aggregation）—— 从 LLM reasoning traces 中自提取逻辑约束，通过 Z3 MAX-SAT 聚合选择答案。核心发现：self-extracted constraints 因 Symbolic Confirmation Bias 无法改善 Self-Consistency majority voting。6 个模型 (7B-32B)，3 个逻辑推理 domain，3000+ condition-evaluations。Oracle controls 证明机制本身有效；cross-architecture NLI verification 展示了突破同模型天花板的可能。\n\n## 你的审查侧重\n\n### 必须重点检查\n1. **CJT 形式化**: Condorcet Jury Theorem 的引用和应用是否严谨？Fleiss' κ 作为 ICC 代理是否有充分论证？Effective-K 公式（Eq.1）的推导和使用是否正确？\n2. **SICA Pipeline**: Eq.2-4 的形式化是否完整和自洽？MAX-SAT 求解的实现是否清晰？评分函数 σ(c,a) 的定义是否有歧义？degeneration condition (Eq.4) 的推导是否严格？\n3. **统计分析**: McNemar exact test 的使用是否恰当（配对/非配对）？TOST 等价检验的 margin 选择 (±2pp) 是否合理？Bootstrap CI 的实施是否正确？多重比较校正（BH correction）是否充分？Power analysis 的 MDE 计算是否正确？\n4. **实验设计**: K=12, T=0.7, T_ext=0.3 的选择是否充分讨论？seed replication (4 seeds vs single seed) 的处理是否合理？小样本条件 (n≤60) 的角色定位（exploratory vs confirmatory）是否明确？\n5. **Oracle Controls**: gold annotation 的来源和质量（FOLIO 95.1%, ProofWriter 97.1% Z3 agreement）是否足够支撑结论？Oracle-SICA 与 self-extracted SICA 的比较是否公平？\n6. **Cross-Architecture PoC**: DeBERTa-large NLI combo 的实验设计（weight parameter w）是否有 overfitting 风险？BH correction 后仅 4/12 显著的结论是否被恰当传达？Capability gap hypothesis 的 sigmoid fit（R²=0.875, 8 data points）是否 overfit？\n7. **Process-level 分析**: TF-IDF cosine similarity 作为 \"process similarity\" 的合理性？是否存在更好的 metric？\n\n### EMNLP 2026 评分标准\n5 = Consider for Award（约前2.5%），4 = Conference（主会议接收），3 = Findings（Findings接收），2 = Resubmit next cycle，1 = Do not resubmit。半分制。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条，标注 S1, S2, ...)\n3. **Weaknesses** (逐条，标注 W1, W2, ...，按严重程度排序，注明 [Critical]/[Warning]/[Info])\n4. **Questions** (逐条，标注 Q1, Q2, ...)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度 1-5)\n7. **Detailed Comments** (按章节逐一评论)",
  "reviewer_id": "1",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\n- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）\n- **论文路径**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n- **投稿类别**: Long paper（8 页正文 + 无限参考文献）\n- **审稿制度**: Double-blind（ACL 模板，`\\usepackage[review]{acl}`）\n- **Limitations**: 必须在参考文献前，不计入页数\n- **附录**: 不计入页数，审稿人无义务阅读\n\n## 论文概述\n负面结果论文。提出 SICA（Symbolic Invariant Consensus Aggregation）—— 从 LLM reasoning traces 中自提取逻辑约束，通过 Z3 MAX-SAT 聚合选择答案。核心发现：self-extracted constraints 因 Symbolic Confirmation Bias 无法改善 Self-Consistency majority voting。6 个模型 (7B-32B)，3 个逻辑推理 domain，3000+ condition-evaluations。Oracle controls 证明机制本身有效；cross-architecture NLI verification 展示了突破同模型天花板的可能。\n\n## 你的审查侧重\n\n### 必须重点检查\n1. **CJT 形式化**: Condorcet Jury Theorem 的引用和应用是否严谨？Fleiss' κ 作为 ICC 代理是否有充分论证？Effective-K 公式（Eq.1）的推导和使用是否正确？\n2. **SICA Pipeline**: Eq.2-4 的形式化是否完整和自洽？MAX-SAT 求解的实现是否清晰？评分函数 σ(c,a) 的定义是否有歧义？degeneration condition (Eq.4) 的推导是否严格？\n3. **统计分析**: McNemar exact test 的使用是否恰当（配对/非配对）？TOST 等价检验的 margin 选择 (±2pp) 是否合理？Bootstrap CI 的实施是否正确？多重比较校正（BH correction）是否充分？Power analysis 的 MDE 计算是否正确？\n4. **实验设计**: K=12, T=0.7, T_ext=0.3 的选择是否充分讨论？seed replication (4 seeds vs single seed) 的处理是否合理？小样本条件 (n≤60) 的角色定位（exploratory vs confirmatory）是否明确？\n5. **Oracle Controls**: gold annotation 的来源和质量（FOLIO 95.1%, ProofWriter 97.1% Z3 agreement）是否足够支撑结论？Oracle-SICA 与 self-extracted SICA 的比较是否公平？\n6. **Cross-Architecture PoC**: DeBERTa-large NLI combo 的实验设计（weight parameter w）是否有 overfitting 风险？BH correction 后仅 4/12 显著的结论是否被恰当传达？Capability gap hypothesis 的 sigmoid fit（R²=0.875, 8 data points）是否 overfit？\n7. **Process-level 分析**: TF-IDF cosine similarity 作为 \"process similarity\" 的合理性？是否存在更好的 metric？\n\n### EMNLP 2026 评分标准\n5 = Consider for Award（约前2.5%），4 = Conference（主会议接收），3 = Findings（Findings接收），2 = Resubmit next cycle，1 = Do not resubmit。半分制。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条，标注 S1, S2, ...)\n3. **Weaknesses** (逐条，标注 W1, W2, ...，按严重程度排序，注明 [Critical]/[Warning]/[Info])\n4. **Questions** (逐条，标注 Q1, Q2, ...)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度 1-5)\n7. **Detailed Comments** (按章节逐一评论)",
    "reviewer_id": "1",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-21T01:40:23.331782+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19993
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-21T01:40:24.515156+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责 **新颖性/完整性** 审查。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\n- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）\n- **论文路径**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n- **投稿类别**: Long paper（8 页正文 + 无限参考文献）\n- **审稿制度**: Double-blind（ACL 模板，`\\usepackage[review]{acl}`）\n- **Limitations**: 必须在参考文献前，不计入页数\n- **附录**: 不计入页数，审稿人无义务阅读\n\n## 论文概述\n负面结果论文。提出 SICA（Symbolic Invariant Consensus Aggregation）—— 从 LLM reasoning traces 中自提取逻辑约束，通过 Z3 MAX-SAT 聚合选择答案。核心发现：self-extracted constraints 因 Symbolic Confirmation Bias 无法改善 Self-Consistency majority voting。6 个模型 (7B-32B)，3 个逻辑推理 domain，3000+ condition-evaluations。Oracle controls 证明机制本身有效；cross-architecture NLI verification 展示了突破同模型天花板的可能。\n\n## 你的审查侧重\n\n### 必须重点检查\n1. **Novelty vs Prior Art**: 相对于 Huang et al. (ICLR 2024) \"LLMs Cannot Self-Correct Reasoning Yet\" 和 Stechly et al. (ICLR 2025) self-verification limitations，本文的 incremental novelty 是否足够？三个声称的 differentiators（Eff-K, bias ratio, process-κ）是否真正 novel？\"Symbolic Mirage\" 概念的原创性如何？\n2. **Related Work 覆盖**: 检查是否遗漏了关键相关工作。特别关注 2025-2026 年的最新 neuro-symbolic reasoning、test-time compute scaling、self-correction 领域论文。引用格式是否符合 ACL/ARR 规范？\n3. **Claim-Evidence 对齐**: 每个 contribution 是否有充分的实验证据支撑？Abstract 和 Conclusion 中的声称是否与实际结果一致？是否有 overclaiming？特别检查 \"independence-accuracy trade-off\" 的 \"persistent\" 定性是否被充分支撑。\n4. **写作质量**: 负面结果论文的叙事结构是否清晰有说服力？是否过度使用术语 branding（\"Symbolic Mirage\"、\"capability trap\"等）？Discussion 和 Conclusion 对于负面结果论文是否足够深入？\n5. **格式规范**: 页数是否在 8 页限制内？匿名化是否完整（检查致谢、URL、代码链接）？Table/Figure 的排版质量？参考文献格式是否一致？\n6. **负面结果论文的价值**: 本文是否提供了足够的 actionable insights？对社区的贡献是否明确？diagnostic tools（Eff-K, BR, process-κ）的可复用性如何？cross-architecture escape 是否为领域提供了有建设性的方向？\n7. **Contribution 结构**: 三个 contributions 的排列是否合理？independence-accuracy trade-off 作为第一贡献是否恰当（实验证据主要来自 FOLIO 单一 dataset）？\n\n### EMNLP 2026 评分标准\n5 = Consider for Award（约前2.5%），4 = Conference（主会议接收），3 = Findings（Findings接收），2 = Resubmit next cycle，1 = Do not resubmit。半分制。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条，标注 S1, S2, ...)\n3. **Weaknesses** (逐条，标注 W1, W2, ...，按严重程度排序，注明 [Critical]/[Warning]/[Info])\n4. **Questions** (逐条，标注 Q1, Q2, ...)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度 1-5)\n7. **Detailed Comments** (按章节逐一评论)",
  "reviewer_id": "2",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责 **新颖性/完整性** 审查。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\n- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）\n- **论文路径**: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n- **投稿类别**: Long paper（8 页正文 + 无限参考文献）\n- **审稿制度**: Double-blind（ACL 模板，`\\usepackage[review]{acl}`）\n- **Limitations**: 必须在参考文献前，不计入页数\n- **附录**: 不计入页数，审稿人无义务阅读\n\n## 论文概述\n负面结果论文。提出 SICA（Symbolic Invariant Consensus Aggregation）—— 从 LLM reasoning traces 中自提取逻辑约束，通过 Z3 MAX-SAT 聚合选择答案。核心发现：self-extracted constraints 因 Symbolic Confirmation Bias 无法改善 Self-Consistency majority voting。6 个模型 (7B-32B)，3 个逻辑推理 domain，3000+ condition-evaluations。Oracle controls 证明机制本身有效；cross-architecture NLI verification 展示了突破同模型天花板的可能。\n\n## 你的审查侧重\n\n### 必须重点检查\n1. **Novelty vs Prior Art**: 相对于 Huang et al. (ICLR 2024) \"LLMs Cannot Self-Correct Reasoning Yet\" 和 Stechly et al. (ICLR 2025) self-verification limitations，本文的 incremental novelty 是否足够？三个声称的 differentiators（Eff-K, bias ratio, process-κ）是否真正 novel？\"Symbolic Mirage\" 概念的原创性如何？\n2. **Related Work 覆盖**: 检查是否遗漏了关键相关工作。特别关注 2025-2026 年的最新 neuro-symbolic reasoning、test-time compute scaling、self-correction 领域论文。引用格式是否符合 ACL/ARR 规范？\n3. **Claim-Evidence 对齐**: 每个 contribution 是否有充分的实验证据支撑？Abstract 和 Conclusion 中的声称是否与实际结果一致？是否有 overclaiming？特别检查 \"independence-accuracy trade-off\" 的 \"persistent\" 定性是否被充分支撑。\n4. **写作质量**: 负面结果论文的叙事结构是否清晰有说服力？是否过度使用术语 branding（\"Symbolic Mirage\"、\"capability trap\"等）？Discussion 和 Conclusion 对于负面结果论文是否足够深入？\n5. **格式规范**: 页数是否在 8 页限制内？匿名化是否完整（检查致谢、URL、代码链接）？Table/Figure 的排版质量？参考文献格式是否一致？\n6. **负面结果论文的价值**: 本文是否提供了足够的 actionable insights？对社区的贡献是否明确？diagnostic tools（Eff-K, BR, process-κ）的可复用性如何？cross-architecture escape 是否为领域提供了有建设性的方向？\n7. **Contribution 结构**: 三个 contributions 的排列是否合理？independence-accuracy trade-off 作为第一贡献是否恰当（实验证据主要来自 FOLIO 单一 dataset）？\n\n### EMNLP 2026 评分标准\n5 = Consider for Award（约前2.5%），4 = Conference（主会议接收），3 = Findings（Findings接收），2 = Resubmit next cycle，1 = Do not resubmit。半分制。\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条，标注 S1, S2, ...)\n3. **Weaknesses** (逐条，标注 W1, W2, ...，按严重程度排序，注明 [Critical]/[Warning]/[Info])\n4. **Questions** (逐条，标注 Q1, Q2, ...)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度 1-5)\n7. **Detailed Comments** (按章节逐一评论)",
    "reviewer_id": "2",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-21T01:40:25.974078+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1458
}
```

</details>

---


### Assistant

_source line 878 · 2026-05-21T01:40:33.371131+00:00_

三项任务已并行派发：
- ✅ 视觉审查 Agent — 已启动（fire-and-forget）
- ✅ Reviewer 1（方法严谨性）— Round 1 已分配
- ✅ Reviewer 2（新颖性/完整性）— Round 1 已分配

等待两名 Reviewer 完成独立初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 879 · 2026-05-21T01:47:52.461015+00:00_

[Reviewer 1 审稿意见]:
# Reviewer 1 审稿意见 — 方法严谨性审查

## 论文信息
- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning
- **目标 venue**: EMNLP 2026 (ARR May 2026)
- **审查侧重**: 方法严谨性（CJT 形式化、SICA Pipeline、统计分析、实验设计、Oracle Controls、Cross-Architecture PoC、Process-level 分析）

---

## 总体评分

**Overall Assessment**: 3.5 — Borderline Conference

**一句话总结**: 方法论整体严谨、实验覆盖面广的负面结果论文，但若干统计分析环节（多重比较未校正、κ→K_eff映射的形式化不足、Capability Gap Hypothesis 基于 8 个数据点的 sigmoid 拟合）削弱了部分定量声称的说服力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 核心 pipeline 形式化完整，oracle controls 有力定位瓶颈。但 Table 1 显著性声称未做多重比较校正，κ→ICC 映射缺乏形式论证，NLI PoC 的 w 参数存在过拟合风险 |
| **Excitement** | 3.5/5 | 系统性地揭示 self-extraction 的失败机制有社区价值，Effective-K/BR/ProcessSim 是可复用诊断工具。但核心负面结论（LLM 无法自我纠错）已有先驱工作，新颖度有限 |
| **Reproducibility** | 4/5 | 实验参数详尽（K=12, T=0.7, T_ext=0.3, α=0.5, Z3 timeout 10s），附录含完整 prompt 模板和伪代码。承诺发布代码和数据，但当前不可验证 |
| **Confidence** | 4/5 | 仔细检查了公式推导、统计方法和实验设计 |

---

## Strengths

**S1.** 实验规模和覆盖面出色。6 个模型（7B–32B）、3 个推理 domain、3000+ condition-evaluations、~1250 unique instances、4-seed replication。在负面结果论文中，这种规模的系统性评估极为罕见（Table 1, §4）。

**S2.** Oracle controls 精准定位瓶颈。Gold-SICA 在 FOLIO 上 +29.90pp（p < 10⁻¹³），证明 MAX-SAT 机制本身有效，问题完全在 self-extraction。这一实验设计将「机制有效性」与「信号质量」干净地解耦（§4.3）。

**S3.** 25+ remediation strategies 的穷举分析（Tables 10–12, Figure 2）极具说服力。涵盖 prompt-level、method-level、paradigm-level 共 15 个 family，所有策略均产生 neutral-to-negative 结果，确认瓶颈的持久性。

**S4.** 引入的三个诊断指标（Effective-K Eq.1、Bias Ratio Eq.5、ProcessSim Eq.6）超越本文贡献，可复用于任何 trace-aggregation 系统的失败预测。特别是 process-level independence 分析（§5.3）揭示了 answer-level κ 低估推理同质性的盲区。

**S5.** 统计报告诚实透明：power analysis 明确指出多数条件 underpowered（Table 5），TOST 等价检验（Appendix V）区分了「等价」「差异」「不确定」三类结论，seed replication（2/4 positive, 2/4 null/negative）如实报告不稳定性。

**S6.** Cross-architecture NLI PoC（§6）提供了建设性的 positive direction——DeBERTa-large 在 ProofWriter 上 +3.50pp（p=0.013），3 种 NLI architecture 一致复现，BH 校正后仍显著。

---

## Weaknesses

**W1 [Warning]** Table 1 的显著性声称缺少多重比较校正。

- **具体位置**: Table 1 (§4.2), 16 个 non-degenerate conditions
- **问题**: 论文声称两个条件显著退化（Mistral-7B PW-D5 p=0.014, Qwen2.5-14B PW-D5 p=0.011）并用 bold 标注。但在 m=16 个未校正的 McNemar test 下，BH 校正后这两个 p 值均不会通过（rank 1 threshold = 0.05/16 = 0.003, rank 2 = 0.006）。论文在 NLI 结果中正确使用了 BH（m=12, Appendix X Table 20），却在主表中省略了。
- **影响**: 不影响核心负面结论（没有正向改进），但 "significant degradation" 的声称被高估。
- **建议**: 对 Table 1 的 16 个条件统一应用 BH 校正，或在标题/脚注中说明未校正并弱化 degradation 的显著性声称。

**W2 [Warning]** Fleiss' κ → Effective-K 映射的形式化不充分。

- **具体位置**: §3.1 Eq.1, 及全文多处引用 K_eff
- **问题**: Eq.1 的 design-effect 公式来自 Kish (1965)，原始形式使用 ICC (ρ)，而非 Fleiss' κ。κ 是 chance-corrected 一致性指标，其数值范围和统计性质与 ICC 不同。论文仅用一句话承认 "κ is a qualitative proxy for ICC"（§3.1），但 K_eff 在全文中作为核心诊断指标反复使用，权重远超 "qualitative proxy" 的定位。
- **建议**: (a) 提供 κ 与 ICC 在本实验数据上的经验对比；或 (b) 用 Krippendorff's α 替代；或 (c) 在使用 K_eff 做定量判断（如 "≤ 1.30 never improves"）时加注 caveat。

**W3 [Warning]** Cross-architecture NLI 的 weight parameter w 未交叉验证。

- **具体位置**: §6, Table 3, Appendix X (Table 20)
- **问题**: w ∈ {1, 3, 5} 在同一测试集上选择和评估，无 held-out 验证。w=5 在 Mistral-7B 上 +10.67pp 但在 LLaMA-3.1-8B 上仅 +1.67pp（n.s.），表明最优 w 不稳定。
- **建议**: 至少做 2-fold cross-validation 或明确声明 w 是 dataset-specific hyperparameter。

**W4 [Warning]** Capability Gap Hypothesis 的 sigmoid fit（R²=0.875）基于 8 个数据点。

- **具体位置**: §6 "Capability gap hypothesis", Figure 3
- **问题**: 3 参数 sigmoid 拟合 8 个点，adjusted R² 会大幅低于 0.875。Linear R²=0.823（2 参数），sigmoid 仅提升 0.052。Spearman ρ=0.970 更可靠但不需要 sigmoid 假说。
- **建议**: 报告 adjusted R²，弱化 inflection point 数值声称，用 rank correlation 作为主要证据。

**W5 [Info]** T_ext=0.3 extraction temperature 缺少 sensitivity analysis。

- **具体位置**: §4.1, Appendix Z
- **问题**: T（采样）和 K 均做了 sensitivity analysis，但 T_ext——论文认定的核心瓶颈环节的关键参数——只用了单一值。
- **建议**: 补充 T_ext 消融实验。

**W6 [Info]** σ(c, a) 的定义（Eq. 3）将 provenance 等同于 semantic support，论文将此作为 observation 而非 design limitation 呈现。

- **具体位置**: §3.2 Eq.3
- **问题**: σ(c, a) = 1 iff c 来自产生 answer a 的 trace。这是导致 degeneration 的直接原因（56.4% zero cross-answer variable overlap），但论文未讨论基于 Z3 semantic evaluation 的替代 σ 设计。
- **建议**: 讨论 semantic σ 作为替代方案及其不可行性/局限。

---

## Questions

**Q1.** Table 1 Mistral-7B FOLIO "4s" 标注的含义——是否暗示读者应给这个条件更高的可信度？

**Q2.** §5.2 "MAX-SAT solver rejects only 3.4% of constraints on average" 的分布如何？高 rejection rate 的 cases 的 SICA accuracy 是否系统性优于 SC？

**Q3.** 是否测试过 answer assertion weight = 0 的变体（纯靠 domain constraints 打分）？

**Q4.** Cross-model extraction（Table 10）是否改善了 cross-answer variable overlap？如果是，为什么仍然无效？

**Q5.** Appendix Z 提到 "Z3-based semantic deduplication yields a small but significant improvement (p=0.013)"。为什么这个正面结果没有在正文中讨论？

---

## Missing References

无明显遗漏。建议考虑引用 step-aware verification 和 CoT faithfulness 的最新实证工作（2025–2026）。

---

## Overall Assessment

**评分: 3.5（Borderline Conference）**

方法论扎实的负面结果论文，实验覆盖面广（6 models × 3 domains × 25+ interventions），oracle controls 有效解耦了机制有效性与信号质量，诊断工具有独立复用价值。

主要不足：(1) Table 1 显著性未校正；(2) κ→K_eff 映射形式化不足但使用权重过大；(3) Capability Gap Hypothesis 基于 8 点 sigmoid fit 过于 aggressive；(4) NLI PoC 的 w 参数缺交叉验证。单独看均非 critical，但累积削弱了「精确定量诊断工具」这一核心贡献维度的可信度。

核心发现本身不令人意外（prior work 已定性论证），但系统化定量分析和穷举式 remediation 使其成为有价值的 reference work。Cross-architecture escape 提供了建设性方向。

**Confidence: 4/5**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 880 · 2026-05-21T01:48:01.030137+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），主要关注统计分析环节（Table 1 多重比较、κ→K_eff 形式化、sigmoid fit、NLI weight 交叉验证）。等待 Reviewer 2 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 881 · 2026-05-21T01:48:15.035814+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见，核心结论：

- **Overall: 3.5（Borderline Conference）**
- **4 个 Warning 级问题**：Table 1 多重比较未校正、κ→K_eff 形式化不足、NLI weight 未交叉验证、sigmoid fit 基于 8 点过拟合
- **2 个 Info 级问题**：T_ext 缺 sensitivity analysis、σ(c,a) 的 provenance-based 设计未作为 design choice 讨论
- **6 个 Strengths**：实验规模、oracle controls、25+ remediation 穷举、可复用诊断指标、统计透明度、cross-architecture PoC
- **5 个 Questions**：关于 4s 标注含义、MAX-SAT rejection 分布、answer assertion weight 消融、cross-model variable overlap、semantic dedup 正面结果为何未入正文

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 882 · 2026-05-21T01:48:23.198511+00:00_

收到 Reviewer 1 审稿意见。等待 Reviewer 2 完成后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 53

## Round 53

6 recorded events


### User

_source line 883 · 2026-05-21T01:49:41.789744+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿完成（新颖性/完整性）

### Overall Assessment: 3.0 (Findings)
**Confidence: 4/5**

### 核心判断
实验设计和统计方法论是本文的核心优势（oracle controls、TOST等价性检验、27种remediation策略穷举），但"自提取验证信号无法改善自身推理"这一结论相对于 Huang et al. (ICLR 2024) 和 Stechly et al. (ICLR 2025) 的增量新颖性不足以支撑 main conference。诊断指标和 cross-architecture escape 更适合作为 Findings 级别的贡献。

### 官方维度打分
| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement | 2.5/5 |
| Reproducibility | 4/5 |
| Overall | 3.0/5 |

### Must-Fix 问题 (Critical)

**W1 — 相对于 Huang/Stechly 的增量新颖性不足。** 核心发现与 Huang et al. (2024) "LLMs Cannot Self-Correct Reasoning Yet" 和 Stechly et al. (2025) self-verification limitations 在概念层面高度一致。三个诊断指标（Eff-K, BR, process-κ）分别是 Kish's design effect、条件概率比、TF-IDF cosine similarity 的直接应用。"Symbolic Mirage" 本质是已知原理在符号约束 domain 的 instantiation。建议更明确论证为什么在 Z3 形式化验证场景下验证此结论是 non-trivial 的。

**W2 — "Independence-Accuracy Trade-off" 作为第一贡献存在部分同义反复。** Table 2/Figure 7 的核心 pattern（弱模型=高独立性+低准确率，强模型=低独立性+高准确率）本质上是经典 bias-variance tradeoff 的重述。27种 within-model remediation 失败增强了论点，但 cross-model pattern 本身新颖性有限。建议将 Symbolic Confirmation Bias 提升为第一贡献。

### Should-Fix 问题 (Warning)

**W3 — 遗漏关键相关工作。** SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM + SAT solver 进行推理且报告正面结果，VeriCoT (Nov 2025) 将 CoT 形式化为 FOL 验证逻辑一致性，CRITIC (Gou et al., ICLR 2024) 涉及 tool-interactive self-correction。这三篇均未被引用。

**W4 — Cross-architecture escape 实验规模不足。** 仅一个外部 verifier (DeBERTa NLI)、两个 dataset (FOLIO n=200, ProofWriter n=600)、三个 generator family。LogiQA 上无效。缺少与其他外部验证方法的对比。

**W5 — Abstract "sixteen" vs Section 4.2 "fifteen" 数字不一致。**

**W6 — 术语品牌化过度。** "Symbolic Mirage"、"Symbolic Confirmation Bias"、"capability trap"——对核心 insight 相对 incremental 的负面结果论文而言，品牌术语过多。

### 小问题 (Info)
- W7: Process-κ 使用 TF-IDF 的局限性（词汇 vs 逻辑结构）
- W8: 未测试 DeepSeek-R1 distilled models

### 主要优势
- S1: Oracle controls 极具说服力
- S2: 统计方法论扎实（TOST, McNemar, bootstrap CI）
- S3: 27种 remediation 穷举封堵了反驳空间
- S4: CJT→SC 形式化框架有理论价值
- S5: Cross-architecture escape 提供建设性方向
- S6: 写作结构清晰

### 关键 Questions
- Q1: Intermediate-SC regime 是否存在 SICA 微弱正效果的 sweet spot？
- Q2: Constraint extraction temperature T_ext 的 sensitivity？
- Q3: Partially gold constraints 的性能退化曲线？
- Q4: NLI verifier + self-extracted constraints 为什么可能比纯 self-extracted 更差？
- Q5: 是否考虑过用 Z3 satisfiability 状态过滤 traces 而非 MAX-SAT weighted voting？

### 格式合规
全部通过（8页正文、匿名化完整、Limitations位置正确、引用格式规范、0 orphan/0 missing citations）。

### 遗漏引用
1. SatLM (Ye et al., NeurIPS 2023)
2. VeriCoT (arXiv 2511.04662, Nov 2025)
3. CRITIC (Gou et al., ICLR 2024)

---
完整审稿意见已在上方消息中给出，包含逐章节 detailed comments。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-21T01:50:17.881641+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿（新颖性/完整性）\n\n### Overall Assessment: 3.0 (Findings)\n**Confidence: 4/5**\n\n### 核心判断\n实验设计和统计方法论是本文的核心优势（oracle controls、TOST等价性检验、27种remediation策略穷举），但\"自提取验证信号无法改善自身推理\"这一结论相对于 Huang et al. (ICLR 2024) 和 Stechly et al. (ICLR 2025) 的增量新颖性不足以支撑 main conference。诊断指标和 cross-architecture escape 更适合作为 Findings 级别的贡献。\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.0/5 |\n\n### Must-Fix 问题 (Critical)\n\n**W1 — 相对于 Huang/Stechly 的增量新颖性不足。** 核心发现与 Huang et al. (2024) \"LLMs Cannot Self-Correct Reasoning Yet\" 和 Stechly et al. (2025) self-verification limitations 在概念层面高度一致。三个诊断指标（Eff-K, BR, process-κ）分别是 Kish's design effect、条件概率比、TF-IDF cosine similarity 的直接应用。\"Symbolic Mirage\" 本质是已知原理在符号约束 domain 的 instantiation。建议更明确论证为什么在 Z3 形式化验证场景下验证此结论是 non-trivial 的。\n\n**W2 — \"Independence-Accuracy Trade-off\" 作为第一贡献存在部分同义反复。** Table 2/Figure 7 的核心 pattern（弱模型=高独立性+低准确率，强模型=低独立性+高准确率）本质上是经典 bias-variance tradeoff 的重述。27种 within-model remediation 失败增强了论点，但 cross-model pattern 本身新颖性有限。建议将 Symbolic Confirmation Bias 提升为第一贡献。\n\n### Should-Fix 问题 (Warning)\n\n**W3 — 遗漏关键相关工作。** SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM + SAT solver 进行推理且报告正面结果，VeriCoT (arXiv 2511.04662, Nov 2025) 将 CoT 形式化为 FOL 验证逻辑一致性，CRITIC (Gou et al., ICLR 2024) 涉及 tool-interactive self-correction。这三篇均未被引用。\n\n**W4 — Cross-architecture escape 实验规模不足。** 仅一个外部 verifier (DeBERTa NLI)、两个 dataset (FOLIO n=200, ProofWriter n=600)、三个 generator family。LogiQA 上无效。缺少与其他外部验证方法的对比。\n\n**W5 — Abstract \"sixteen\" vs Section 4.2 \"fifteen\" 数字不一致。**\n\n**W6 — 术语品牌化过度。** \"Symbolic Mirage\"、\"Symbolic Confirmation Bias\"、\"capability trap\"——对核心 insight 相对 incremental 的负面结果论文而言，品牌术语过多。\n\n### 小问题 (Info)\n- W7: Process-κ 使用 TF-IDF 的局限性（词汇 vs 逻辑结构）\n- W8: 未测试 DeepSeek-R1 distilled models\n\n### 主要优势\n- S1-S6（Oracle controls, 统计方法论, 27种 remediation 穷举, CJT 形式化, cross-architecture escape, 写作结构清晰）\n\n### 关键 Questions\n- Q1: Intermediate-SC regime 是否存在 SICA 微弱正效果的 sweet spot？\n- Q2: Constraint extraction temperature T_ext 的 sensitivity？\n- Q3: Partially gold constraints 的性能退化曲线？\n- Q4: NLI verifier + self-extracted constraints 为什么可能比纯 self-extracted 更差？\n- Q5: 是否考虑过用 Z3 satisfiability 状态过滤 traces 而非 MAX-SAT weighted voting？\n\n### 遗漏引用\n1. SatLM (Ye et al., NeurIPS 2023)\n2. VeriCoT (arXiv 2511.04662, Nov 2025)\n3. CRITIC (Gou et al., ICLR 2024)\n\n---\n\n请对 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。",
  "reviewer_id": "1",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每条 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿（新颖性/完整性）\n\n### Overall Assessment: 3.0 (Findings)\n**Confidence: 4/5**\n\n### 核心判断\n实验设计和统计方法论是本文的核心优势（oracle controls、TOST等价性检验、27种remediation策略穷举），但\"自提取验证信号无法改善自身推理\"这一结论相对于 Huang et al. (ICLR 2024) 和 Stechly et al. (ICLR 2025) 的增量新颖性不足以支撑 main conference。诊断指标和 cross-architecture escape 更适合作为 Findings 级别的贡献。\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.0/5 |\n\n### Must-Fix 问题 (Critical)\n\n**W1 — 相对于 Huang/Stechly 的增量新颖性不足。** 核心发现与 Huang et al. (2024) \"LLMs Cannot Self-Correct Reasoning Yet\" 和 Stechly et al. (2025) self-verification limitations 在概念层面高度一致。三个诊断指标（Eff-K, BR, process-κ）分别是 Kish's design effect、条件概率比、TF-IDF cosine similarity 的直接应用。\"Symbolic Mirage\" 本质是已知原理在符号约束 domain 的 instantiation。建议更明确论证为什么在 Z3 形式化验证场景下验证此结论是 non-trivial 的。\n\n**W2 — \"Independence-Accuracy Trade-off\" 作为第一贡献存在部分同义反复。** Table 2/Figure 7 的核心 pattern（弱模型=高独立性+低准确率，强模型=低独立性+高准确率）本质上是经典 bias-variance tradeoff 的重述。27种 within-model remediation 失败增强了论点，但 cross-model pattern 本身新颖性有限。建议将 Symbolic Confirmation Bias 提升为第一贡献。\n\n### Should-Fix 问题 (Warning)\n\n**W3 — 遗漏关键相关工作。** SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM + SAT solver 进行推理且报告正面结果，VeriCoT (arXiv 2511.04662, Nov 2025) 将 CoT 形式化为 FOL 验证逻辑一致性，CRITIC (Gou et al., ICLR 2024) 涉及 tool-interactive self-correction。这三篇均未被引用。\n\n**W4 — Cross-architecture escape 实验规模不足。** 仅一个外部 verifier (DeBERTa NLI)、两个 dataset (FOLIO n=200, ProofWriter n=600)、三个 generator family。LogiQA 上无效。缺少与其他外部验证方法的对比。\n\n**W5 — Abstract \"sixteen\" vs Section 4.2 \"fifteen\" 数字不一致。**\n\n**W6 — 术语品牌化过度。** \"Symbolic Mirage\"、\"Symbolic Confirmation Bias\"、\"capability trap\"——对核心 insight 相对 incremental 的负面结果论文而言，品牌术语过多。\n\n### 小问题 (Info)\n- W7: Process-κ 使用 TF-IDF 的局限性（词汇 vs 逻辑结构）\n- W8: 未测试 DeepSeek-R1 distilled models\n\n### 主要优势\n- S1-S6（Oracle controls, 统计方法论, 27种 remediation 穷举, CJT 形式化, cross-architecture escape, 写作结构清晰）\n\n### 关键 Questions\n- Q1: Intermediate-SC regime 是否存在 SICA 微弱正效果的 sweet spot？\n- Q2: Constraint extraction temperature T_ext 的 sensitivity？\n- Q3: Partially gold constraints 的性能退化曲线？\n- Q4: NLI verifier + self-extracted constraints 为什么可能比纯 self-extracted 更差？\n- Q5: 是否考虑过用 Z3 satisfiability 状态过滤 traces 而非 MAX-SAT weighted voting？\n\n### 遗漏引用\n1. SatLM (Ye et al., NeurIPS 2023)\n2. VeriCoT (arXiv 2511.04662, Nov 2025)\n3. CRITIC (Gou et al., ICLR 2024)\n\n---\n\n请对 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。",
    "reviewer_id": "1",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-21T01:50:38.037122+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20155
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-21T01:50:39.251117+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每条 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿（方法严谨性）\n\n### Overall Assessment: 3.5 (Borderline Conference)\n**Confidence: 4/5**\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Reproducibility | 4/5 |\n\n### Weaknesses\n\n**W1 [Warning]** Table 1 的显著性声称缺少多重比较校正。\n- Table 1 (§4.2) 16 个 non-degenerate conditions 中两个 significant degradation（Mistral-7B PW-D5 p=0.014, Qwen2.5-14B PW-D5 p=0.011），未做 BH 校正。但论文在 NLI 结果中正确使用了 BH（m=12）。\n- 影响：不影响核心负面结论，但 \"significant degradation\" 声称被高估。\n\n**W2 [Warning]** Fleiss' κ → Effective-K 映射的形式化不充分。\n- Eq.1 的 design-effect 公式来自 Kish (1965)，原始形式使用 ICC (ρ) 而非 Fleiss' κ。论文仅一句 \"qualitative proxy\"，但 K_eff 在全文中作为核心诊断指标反复使用。\n\n**W3 [Warning]** Cross-architecture NLI 的 weight parameter w 未交叉验证。\n- w ∈ {1, 3, 5} 在同一测试集上选择和评估。w=5 在 Mistral-7B 上 +10.67pp 但在 LLaMA-3.1-8B 上仅 +1.67pp（n.s.）。\n\n**W4 [Warning]** Capability Gap Hypothesis 的 sigmoid fit（R²=0.875）基于 8 个数据点。\n- 3 参数 sigmoid 拟合 8 个点。Linear R²=0.823 仅低 0.052。Spearman ρ=0.970 更可靠。\n\n**W5 [Info]** T_ext=0.3 extraction temperature 缺少 sensitivity analysis。\n\n**W6 [Info]** σ(c, a) 的定义（Eq. 3）将 provenance 等同于 semantic support，未讨论基于 Z3 semantic evaluation 的替代 σ 设计。\n\n### Questions\n- Q1: Table 1 \"4s\" 标注含义？\n- Q2: MAX-SAT rejection rate 3.4% 的分布？高 rejection 的 cases SICA 是否优于 SC？\n- Q3: answer assertion weight = 0 的变体？\n- Q4: Cross-model extraction 是否改善了 cross-answer variable overlap？\n- Q5: Z3 semantic deduplication (p=0.013) 正面结果为何未入正文？\n\n### Strengths\nS1-S6（实验规模、oracle controls、25+ remediation 穷举、可复用诊断指标、统计透明度、cross-architecture PoC）\n\n---\n\n请对 W1-W6 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。",
  "reviewer_id": "2",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每条 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿（方法严谨性）\n\n### Overall Assessment: 3.5 (Borderline Conference)\n**Confidence: 4/5**\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Reproducibility | 4/5 |\n\n### Weaknesses\n\n**W1 [Warning]** Table 1 的显著性声称缺少多重比较校正。\n- Table 1 (§4.2) 16 个 non-degenerate conditions 中两个 significant degradation（Mistral-7B PW-D5 p=0.014, Qwen2.5-14B PW-D5 p=0.011），未做 BH 校正。但论文在 NLI 结果中正确使用了 BH（m=12）。\n- 影响：不影响核心负面结论，但 \"significant degradation\" 声称被高估。\n\n**W2 [Warning]** Fleiss' κ → Effective-K 映射的形式化不充分。\n- Eq.1 的 design-effect 公式来自 Kish (1965)，原始形式使用 ICC (ρ) 而非 Fleiss' κ。论文仅一句 \"qualitative proxy\"，但 K_eff 在全文中作为核心诊断指标反复使用。\n\n**W3 [Warning]** Cross-architecture NLI 的 weight parameter w 未交叉验证。\n- w ∈ {1, 3, 5} 在同一测试集上选择和评估。w=5 在 Mistral-7B 上 +10.67pp 但在 LLaMA-3.1-8B 上仅 +1.67pp（n.s.）。\n\n**W4 [Warning]** Capability Gap Hypothesis 的 sigmoid fit（R²=0.875）基于 8 个数据点。\n- 3 参数 sigmoid 拟合 8 个点。Linear R²=0.823 仅低 0.052。Spearman ρ=0.970 更可靠。\n\n**W5 [Info]** T_ext=0.3 extraction temperature 缺少 sensitivity analysis。\n\n**W6 [Info]** σ(c, a) 的定义（Eq. 3）将 provenance 等同于 semantic support，未讨论基于 Z3 semantic evaluation 的替代 σ 设计。\n\n### Questions\n- Q1: Table 1 \"4s\" 标注含义？\n- Q2: MAX-SAT rejection rate 3.4% 的分布？高 rejection 的 cases SICA 是否优于 SC？\n- Q3: answer assertion weight = 0 的变体？\n- Q4: Cross-model extraction 是否改善了 cross-answer variable overlap？\n- Q5: Z3 semantic deduplication (p=0.013) 正面结果为何未入正文？\n\n### Strengths\nS1-S6（实验规模、oracle controls、25+ remediation 穷举、可复用诊断指标、统计透明度、cross-architecture PoC）\n\n---\n\n请对 W1-W6 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。",
    "reviewer_id": "2",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-21T01:50:40.888193+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1637
}
```

</details>

---


### Assistant

_source line 888 · 2026-05-21T01:50:44.107641+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 889 · 2026-05-21T01:50:46.935295+00:00_

[Reviewer 2 审稿结果]:
审稿完成。已将完整审稿意见汇报给 Review Director。

核心结论：**Overall 3.0 (Findings)**。实验设计和统计方法论是论文的核心优势（oracle controls、27种remediation穷举、TOST等价性检验），但相对于 Huang et al. (2024) 和 Stechly et al. (2025) 的增量新颖性不足以支撑 main conference。两个 Critical 问题：(1) 核心 insight 是已知负面结论在符号约束 domain 的 instantiation；(2) 第一贡献 "independence-accuracy trade-off" 存在部分同义反复。遗漏 SatLM、VeriCoT、CRITIC 三篇关键相关工作。格式合规全部通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 890 · 2026-05-21T01:50:52.726417+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 55

## Round 55

2 recorded events


### User

_source line 891 · 2026-05-21T01:53:01.795320+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应完成

### 逐条回应摘要

| R1 Issue | R2 判断 | 核心理由 |
|----------|--------|--------|
| W1 多重比较校正 | [AGREE] | BH校正后Table 1两个degradation均不再显著，但不影响核心负面结论 |
| W2 κ→Eff-K形式化 | [AGREE] | Fleiss' κ ≠ ICC，论文超出了"qualitative proxy"的使用范畴 |
| W3 NLI weight未交叉验证 | [AGREE] | w依赖generator-verifier pair，proof-of-concept可接受但需改进 |
| W4 Sigmoid fit过拟合 | [AGREE] | 3参数8点，应改用Spearman ρ作为主要metric |
| W5 T_ext sensitivity | [AGREE] | 与我自己的Q2一致，关键confound |
| W6 σ(c,a)设计 | [REBUT] | 存在循环依赖问题；在BR=1.97×下provenance和semantic σ应给出相似结果 |

### Questions 回应摘要
- Q1: "4s"可能指4-seed replication
- Q2: high-rejection cases分析缺失是遗憾
- Q3: answer assertion weight=0是极有价值的缺失消融
- Q4: cross-model extraction的variable overlap diversity值得探索
- Q5: Z3 semantic dedup p=0.013应在正文提及，remediation总结过粗

### R1 vs R2 分歧点
- **Excitement**: R1=3.5 vs R2=2.5。核心分歧在于incremental novelty vs Huang/Stechly的权重
- **Overall**: R1=3.5 vs R2=3.0。R1更看重实验thoroughness，R2更看重conceptual independence
- 双方在Soundness (3.5)和Reproducibility (4)上完全一致

### 建议 Director 关注
1. W1（多重比较）和W2（κ→Eff-K）是双方共识的must-fix
2. Novelty判断（是否足够main conference）是核心分歧，需要Director裁决
3. R1的Q3（answer assertion weight=0消融）和Q5（Z3 semantic dedup正面结果）是重要的缺失实验信号

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 892 · 2026-05-21T01:53:07.717509+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 893 · 2026-05-21T01:53:10.412116+00:00_

[Reviewer 2 审稿结果]:
交叉回应完成。

**与 R1 的共识点：** W1-W5 全部同意（多重比较校正、κ→Eff-K 形式化、NLI weight 交叉验证、sigmoid 过拟合、T_ext sensitivity）。

**唯一反驳：** W6（σ(c,a) 设计）——Z3 semantic evaluation 存在循环依赖问题，且在 BR=1.97× 下两种 σ 定义结果应趋同。

**核心分歧：** Excitement 评分（R1: 3.5 vs R2: 2.5），源于对 incremental novelty vs Huang/Stechly 的不同权重判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 894 · 2026-05-21T01:53:15.791108+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 57

## Round 57

10 recorded events


### User

_source line 895 · 2026-05-21T01:53:41.702642+00:00_

[Reviewer 1 审稿意见]:
# Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 审稿意见的逐条回应

---

## Must-Fix (Critical)

**[REBUT] R2-W1 — 增量新颖性不足**

R2 判断"概念层面高度一致"部分成立，但低估了 Z3 形式化验证场景下验证此结论的 non-triviality：(1) Z3 是确定性验证器，不是自然语言反馈，prior work 未排除 formal verification bypass hypothesis；(2) 诊断指标的组合框架（Eff-K + BR + oracle controls 分离 extraction quality vs. mechanism validity）在 prior work 中不存在；(3) 27 种 remediation 穷举证明 exhaustive inescapability，超越 Huang/Stechly 的 existence-of-failure 证明。建议作者在 §1 更明确论证 Z3 scenario 的 non-triviality。

**[AGREE] R2-W2 — Independence-Accuracy Trade-off 部分同义反复**

Cross-model pattern 确实接近 bias-variance tradeoff 已知结论。但 27 种 within-model remediation 全部失败使 trade-off 从"已知观察"升级为"不可打破的天花板"——inescapability claim 是新的。同意将 Symbolic Confirmation Bias（BR=4.97×, 83.3% wrong-supporting rate）提升为第一贡献的建议。

---

## Should-Fix (Warning)

**[AGREE] R2-W3 — 遗漏引用** SatLM、VeriCoT、CRITIC 应引用。特别是 SatLM 的正面结果可与 SICA 负面结果形成 problem-level vs. trace-level 对比，实际上强化 Symbolic Mirage 论点。

**[AGREE] R2-W4 — Cross-architecture escape 规模不足** 论文已定位为 PoC 且在 Limitations 中承认，但缺少与其他外部验证方法（trained verifiers, code-based verification）的对比确实是短板。

**[AGREE] R2-W5 — "sixteen" vs "fifteen" 不一致** 确认：Table 1 有 16 个 non-degenerate 行。Abstract "sixteen" 正确，§4.2 "fifteen" 为笔误。

**[REBUT] R2-W6 — 术语品牌化过度** "Symbolic Mirage" 和 "Symbolic Confirmation Bias" 有精确操作定义（Eq.5, §5.2），不是空洞品牌化。但 "capability trap" 较弱，可以弱化。负面结果论文需要可引用的 named phenomena 帮助后续工作 reference。

---

## Info

**[AGREE] R2-W7** TF-IDF 局限性合理，与我的审稿意见一致。

**[REBUT] R2-W8** Table 4（Appendix D）已含 DeepSeek-R1-7B 的 exploratory 数据（Δ=−3.33pp），但 n≤60 不足以做 confirmatory 结论。论文确实测试了但规模不充分。

---

## Questions

**[AGREE] Q1** sweet spot 存在但极不稳定（Appendix N: +12.8pp vs. -1.3pp across seeds），缺系统化刻画。

**[AGREE] Q2** T_ext sensitivity 缺失，与我的 W5 一致。

**[AGREE] Q3** 0%→100% gold constraint mixing curve 缺失，会极大增强实用价值。

**[REBUT] Q4** §6 的 combo mode 是 NLI + SC votes，不涉及 self-extracted constraints。R2 可能误解了设计。

**[REBUT] Q5** 已测试。Table 12 intervention #20 "Z3 trace filter"（Δ=−0.49pp, precision 49.1%）和 #27 "Z3 strict-mode"（Δ=0.00, 63% UNSAT）均无效。

---

## 对 R2 Overall 评分的看法

R2 给 3.0 Findings 主要基于 novelty（W1, W2）。我部分同意 W1 但认为 Z3 场景验证和 27 种 remediation 穷举在 rigor 上超越 prior work，保持我的 3.5 Borderline Conference 评分。R2 的 W3（遗漏引用）和 W5（数字不一致）是需修复的实质问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-21T01:54:08.253663+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-21T01:54:08.455475+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T01:39:32.636676+00:00\", \"completed_at\": \"2026-05-21T01:43:04.893267+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页纯文本无任何 display item。第一个视觉锚点（Figure 1 SICA pipeline）直到 page 4 才出现。审稿人在前 2 分钟内只看到密集双栏文字，缺乏快速建立认知的视觉抓手。建议将 Figure 1 提前到 page 1（Introduction 末尾或 page 2 开头），或在 page 1-2 加入一个简洁的 teaser figure 展示核心发现\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Experiments 设置部分整页纯文本，与 page 4（Figure 1）和 page 6（Table 1）之间形成文本断层。加上 pages 1-3 的纯文本段，论文前半部分视觉节奏偏单调\"}, {\"severity\": \"warning\", \"dimension\": \"page 4\", \"message\": \"Figure 1（SICA pipeline 核心方法图）仅占单栏宽度，作为论文第一个也是最重要的概念图，视觉冲击力不足。建议改用 figure*（全宽）以提升可读性和第一印象锚定效果\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"最后一页主文内容极度密集：Figure 3 + Table 3 + Discussion（§7）+ Conclusion（§8）全部挤在一页。Conclusion 仅约 8-10 行，显得仓促。Discussion 和 Conclusion 的压缩感可能让审稿人觉得收尾草率\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁，符合 ACL 匿名提交格式。Abstract 长度适中，首页整体专业\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1（主结果表）使用 figure* 全宽排版，booktabs 风格，分组清晰（Type A/B conditions），最优结果加粗标注。格式专业，信息密度高\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 + Figure 2 同页，视觉节奏好。Figure 2 bar chart 颜色可区分，字号可读。Table 2 按 κ 降序排列，逻辑清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 bar chart 整体可读，但图例区域字号偏小，若打印可能影响辨识\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3 scatter plot 单栏宽度，三组数据点颜色可区分。图内标注字号偏小但尚可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 脚注说明（\\\"Bold = gold logical examples\\\" 等）位于表格下方，排版规范。但表格行数多（约 20+ 行），信息密度极高，审稿人可能需要反复对照才能提取关键结论\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段约占左栏 1/3，内容充实。References 从右栏开始，排版正常\"}, {\
…[truncated 1161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-21T01:54:08.456000+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-21T01:54:08.506537+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-21T01:57:28.170549+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n- id: \"R3-N3\"\n  summary: \"Discriminative rate from small pilot\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"804-instance analysis: 8.2% [CI: 7.6, 8.8].\"\n  resolution_round: 3\n\n- id: \"R3-W6\"\n  summary: \"No 70B+ model tested\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 3\n  last_seen_round: 9\n  resolution: \"Acknowledged as limitation in paper.\"\n  resolution_round: 4\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W4 re-raised: Abstract 'full LLM capability range' overclaims given 7B-32B only. Model range limitation persists.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R9 R2-W8: DeepSeek-R1 distilled models not tested. R1 rebuts: Table 4 has DeepSeek-R1-7B data (n≤60). Scale limitation persists.\"\n\n- id: \"R4-C1\"\n  summary: \"Cross-section Δ inconsistency\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"D064+D066 full data replacement completed.\"\n  resolution_round: 4\n\n- id: \"R4-C2\"\n  summary: \"CJT framing gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Dual-bottleneck paragraph added. Title changed.\"\n  resolution_round: 4\n\n- id: \"R4-C3\"\n  summary: \"Goldilocks zone evidence from only 1 model × 1 dataset\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Claims downgraded to 'directional trend'. V2 framing de-emphasizes intermediate region.\"\n  resolution_round: 5\n\n- id: \"R4-W1\"\n  summary: \"Multiple testing correction\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"BH correction computed: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Eff-K Kish (1965) attribution / κ→ICC proxy rigor\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Pairwise Pearson r (mean 0.625, Mistral-7B) monotonically related to κ across 4 model families. κ validated as consensus proxy.\"\n  resolution_round: 7\n\n- id: \"R4-M5\"\n  summary: \"Figure 2 old data\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Figure 2 moved to Appendix in V2 page budget compression.\"\n  resolution_round: 6\n\n- id: \"R5-N1\"\n  summary: \"Oracle ceiling '24%' cross-model comparison invalid\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Mistral-7B same-model oracle: +29.90pp (p<1e-13).\"\n  resolution_round: 5\n\n- id: \"R5-N2\"\n  summary: \"§4.1 Decoupling interim results (n=70/204) in main text\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"V2 framing removes §4.1 Decoupling from main text entirely.\"\n  resolution_round: 5\n\n- id: \"R5-N3\"\n  summary: \"'Fundamental' trade-off overclaimed\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All 'fundamental' → 'persistent' + 'at the 7B--32B scale'.\"\n  resolution_round: 5\n\n- id: \"R5-N4\"\n  summary: \"DeBERTa PoC statistically fragile — 9 discordant pairs\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"ProofWriter w=3 +3.50pp (p=0.013, n=600) as primary finding.\"\n  resolution_round: 5\n\n- id: \"R5-N5\"\n  summary: \"Discussion/Conclusion too thin for negative paper\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Discussion ~350 words, Conclusion ~220 words.\"\n  resolution_round: 5\n\n- id: \"R5-W1\"\n  summary: \"Variable name isolation confound\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Alpha-equivalence caveat added in Discussion.\"\n  resolution_round: 5\n\n- id: \"R5-W2\"\n  summary: \"Fleiss' κ as ICC proxy lacks formal justification\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Caveat added. Pairwise correlation validates κ (tracked under R4-W3).\"\n  resolution_round: 5\n\n- id: \"R5-W3\"\n  summary: \"Missing ensemble diversity literature\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Krogh & Vedelsby (1994) + Brown et al. (2005) cited.\"\n  resolution_round: 5\n\n- id: \"R5-W4\"\n  summary: \"§3/§5 content duplication\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Not flagged in R6 — considered resolved.\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"'25+ strategies' count inflated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"'more than twenty spanning fifteen distinct families'.\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"Code/data release not mentioned\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Reproducibility paragraph added.\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Solutions before Experiments ordering\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"main.tex reordered correctly.\"\n  resolution_round: 5\n\n- id: \"R5-W8\"\n  summary: \"TF-IDF cosine limitation under-discussed\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 9\n  resolution: \"Deferred to rebuttal. SBERT validation not worth GPU time per Reviewer assessment.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers re-raised: R1-W5 notes Figure 2 R²≈4.4% is very low; R2-Q4 asks if TF-IDF sufficiently captures semantic similarity. Limitation persists.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R1-W5(Info), R2-W7(Info): TF-IDF limitation re-confirmed by both reviewers. Consensus: acknowledged limitation, not blocking.\"\n\n- id: \"R5-W9\"\n  summary: \"CJT novelty / Huang-Stechly distinction insufficient\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Paper Agent added novelty differentiation paragraph (3 quantitative differentiators). Tracked jointly with R6-N3.\"\n  resolution_round: 7\n\n- id: \"R5-TC1\"\n  summary: \"SC tiebreaking inconsistency (dict-order vs alphabetical)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All tiebreaking standardized to alphabetical.\"\n  resolution_round: 5\n\n- id: \"R6-N1\"\n  summary: \"Statistical power 5.7%-20.6% — title 'Fail' overclaims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Title changed to 'Do Not Improve'. TOST computed: 4/15 equivalence, 5/15 genuine difference (4 negative), 6/15 underpowered. Three-tier classification integrated into abstract, §4, appendix.\"\n  resolution_round: 7\n\n- id: \"R6-N2\"\n  summary: \"Cross-arch PoC p=0.013 needs multiple comparison correction\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"BH correction: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Novelty vs self-correction literature (Huang/Stechly/Amonkar)\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  resolution: \"Novelty paragraph added (3 differentiators: κ/Eff-K diagnostics, formal Z3 verification, process-level analysis). §3.3 empirical bound (Δ_max ≤ Oracle_Gap/BR) further differentiates.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W1 re-raised novelty concern despite R7 fix. R1 partially rebuts, citing empirical specificity and quantitative tools. Divergence remains — see R8-W1.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R2-W1(Critical): Novelty gap persists. R1 partially rebuts (Z3 non-triviality + exhaustive remediation). Core divergence: R1=3.5 vs R2=3.0. Director sides with R2 — conceptual increment insufficient for main conference.\"\n\n- id: \"R6-N4\"\n  summary: \"Missing references: CLOVER (ICLR 2025), VERGE, Toh et al. (2024)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"5 BibTeX entries written (CLOVER, VERGE, Toh et al., Chan et al., Lakens). All cited in Related Work + §4. Author correction applied (Toh et al., not Xia et al.). Orphan bib removed.\"\n  resolution_round: 7\n\n- id: \"R6-W1\"\n  summary: \"Bias ratio numbers inconsistent between main text and Table 14\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent clarified BR calculation scope (Batch 1 W6).\"\n  resolution_round: 7\n\n- id: \"R6-W2\"\n  summary: \"Type A/B/C failure mode classification is post-hoc\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent labeled as 'three empirical regimes (observation-driven)' (Batch 1 W7).\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"Degeneration condition (Eq. 4) derivation incomplete\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Constraint rejection rate 3.44% (no diff correct/incorrect, p=0.636) integrated into §5.2 as empirical evidence for Eq.4 degeneration.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"'Symbolic Mirage' terminology too marketing-like\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  resolution: \"Scoping sentence added: Mirage is specific to self-extracted constraints. §3.3 explicitly contrasts with independently sourced constraints.\"\n  resolution_round: 7\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R9 R2-W6: Terminology branding re-raised. R1 rebuts (operational definitions exist for Mirage and Confirmation Bias). Partial agreement: 'capability trap' can be weakened.\"\n\n- id: \"R6-W5\"\n  summary: \"α=0.5 penalty weight lacks sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"α sensitivity: max 0.49pp variation across α∈{0.0-1.0}. One-sentence note added to §3.2 C₀ diagnostic paragraph.\"\n  resolution_round: 7\n\n- id: \"R6-W6\"\n  summary: \"GSM8K (n=30) and AIME (n=22) in main Table 1 misleading\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Kept with † marker and 'suggestive only' caveat. Degenerate regime demonstration serves pedagogical purpose.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W5: underpowered conditions still not clearly marked in Table 1. Recommend explicit powered vs. exploratory labeling.\"\n\n- id: \"R6-W7\"\n  summary: \"Orphan bib entry (press2023compositionality)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"press2023compositionality removed from references.bib. All new entries (CLOVER, VERGE, Toh, Chan, Lakens) cited.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"Reasoning models not discussed as category in Related Work\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent added reasoning models paragraph with κ=0.91 homogenization (Batch 1 W14).\"\n  resolution_round: 7\n\n- id: \"R6-V1\"\n  summary: \"Page 20 >75% empty white space\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Page 20 now ~60% filled (TOST section + Extended Limitations). Remaining whitespace is natural appendix pagination.\"\n  resolution_round: 7\n\n- id: \"R6-V2\"\n  summary: \"Main text only 5 display items\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Figure 5 (intervention summary) promoted to main text §5.5; Figure 2 moved to Appendix. Main text now has 2 tables + 2 figures + pipeline diagram.\"\n  resolution_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"Visual check + R2-W6: Figure 5 (intervention strategies) recommended for main text. First 3 pages lack any visual anchor.\"\n\n- id: \"R8-N1\"\n  summary: \"FOL terminology misleading — actual constraints are predominantly propositional ground clauses\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"All 'FOL constraints' → 'logical constraints'. Quantifier proportion (99.0% propositional, 1.0% ∀/∃) added to §3.2 constraint extraction paragraph and Appendix extended limitations.\"\n  resolution_round: 8\n\n- id: \"R8-N2\"\n  summary: \"Cross-architecture PoC underpowered: single generator (Mistral-7B) × inconsistent dataset results\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"§6 restructured: explicit two-generator framing (Mistral-7B positive + Qwen3-14B null confirms capability gap). Invalid Table 3 removed (DeBERTa-large vs DeBERTa-base confound). Clean single-generator evidence retained.\"\n  resolution_round: 8\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R1-W3(Warning): NLI weight w not cross-validated. R2-W4(Warning): cross-arch scale insufficient, no comparison with other external verification methods. Both agree PoC is limited.\"\n\n- id: \"R8-W1\"\n  summary: \"Incremental novelty relative to Huang (2024)/Stechly (2025) self-verification failure literature\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"§2 para 5 (Positioning) articulates 3 quantitative differentiators (Eff-K, BR, C_D) + capability gap corollary. §2 para 3 frames formal verification as 'natural hypothesis' that SICA systematically tests.\"\n  resolution_round: 8\n\n- id: \"R8-W2\"\n  summary: \"Seed replication inconsistency — Table 1 does not mark which conditions have multi-seed support\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Table 1 has $^{4s}$ superscript on 4-seed confirmatory condition + caption note distinguishing confirmatory vs exploratory.\"\n  resolution_round: 8\n\n- id: \"R8-W3\"\n  summary: \"Semantic deduplication missing — syntactic-only dedup may inflate verbose trace weights\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"§3.2 now reports 46.0% global average dedup ratio. Extended limitations discusses Z3 semantic dedup (+~10% removal, p=0.013 vs no dedup).\"\n  resolution_round: 8\n\n- id: \"R8-W4\"\n  summary: \"Domain diversity + model range overclaimed in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Abstract scope accurately reflects 7B-32B range with explicit SC baseline anchors. 'Logical reasoning domains' replaces generic 'reasoning domains'.\"\n  resolution_round: 8\n\n- id: \"R8-W5\"\n  summary: \"Constraint quality analysis (91.8% discriminative rate) based on single model family (Qwen2.5-14B)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Scoped in extended limitations (Appendix). Main text 91.8% appears with n=804 matching the Qwen2.5-14B analysis.\"\n  resolution_round: 8\n\n- id: \"R8-W6\"\n  summary: \"Symbolic Confirmation Bias lacks theoretical connection to Turpin et al. (2024) unfaithful CoT\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Turpin connection present in §3.3 (concise, integrated into Mirage definition). Discussion also references Turpin. Redundant duplicate removed.\"\n  resolution_round: 8\n\n- id: \"R8-I1\"\n  summary: \"Missing references: Weng et al. (2023) Self-Verification and Madaan et al. (2023) Self-Refine\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Both citations added to §2 para 3 and references.bib by Paper Agent.\"\n  resolution_round: 8\n\n- id: \"R8-I2\"\n  summary: \"Figure 5 (intervention strategies summary) buried in Appendix — should be in main text\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Figure swap complete. Main text §5.5 now has intervention summary figure. Process-kappa scatter referenced as 'Appendix Figure'.\"\n  resolution_round: 8\n\n- id: \"R8-I3\"\n  summary: \"83.3% confirmation bias rate needs per-model breakdown in main text\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Per-model BR (4.97×/3.93×/2.88×) already reported in §5.2 with Table ref. 83.3% is Mistral-specific and appears in that context.\"\n  resolution_round: 8\n\n# =========================================================\n# Round 9 (fresh review) — new issues\n# =========================================================\n\n- id: \"R9-W1\"\n  summary: \"Table 1 显著性声称缺少多重比较校正（16 条件未做 BH）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 raised, R2 agrees. BH校正后 Mistral-7B PW p=0.014 和 Qwen2.5-14B PW p=0.011 均不再显著。不影响核心负面结论，但 'significant degradation' 声称被高估。\"\n  action_items:\n    - round: 9\n      action: \"对 Table 1 的 16 个 non-degenerate 条件应用 BH 校正，或在脚注中说明未校正并弱化 degradation 显著性声称\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W2\"\n  summary: \"κ→Effective-K 映射形式化不足：Fleiss' κ ≠ ICC，但 K_eff 作为核心诊断指标使用权重过大\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W2 raised, R2 agrees. 论文仅一句 'qualitative proxy' 但 K_eff 在全文反复作为定量判断依据（如 '≤1.30 never improves'）。历史 issue R4-W3/R5-W2 曾部分修复但本轮 fresh 审稿认为仍不充分。\"\n  action_items:\n    - round: 9\n      action: \"提供 κ 与 ICC 经验对比，或对 K_eff 定量声称加注 caveat\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W3\"\n  summary: \"NLI combo weight parameter w 未交叉验证，w=5 在不同 generator 上效果不稳定\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W3 raised, R2 agrees. w∈{1,3,5} 在同一测试集选择和评估。w=5 Mistral +10.67pp vs LLaMA +1.67pp(n.s.)。PoC 可接受但需声明 w 是 dataset-specific。\"\n  action_items:\n    - round: 9\n      action: \"声明 w 为 dataset-specific hyperparameter，或补充交叉验证\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W4\"\n  summary: \"Capability Gap Hypothesis sigmoid fit (R²=0.875) 基于 8 个数据点，3 参数过拟合\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W4 raised, R2 agrees. Linear R²=0.823 仅低 0.052。Spearman ρ=0.970 更可靠。应报告 adjusted R² 并弱化 inflection point 数值声称。\"\n  action_items:\n    - round: 9\n      action: \"改用 Spearman ρ 作为主要证据，报告 adjusted R²，弱化 sigmoid inflection 声称\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W5\"\n  summary: \"T_ext=0.3 extraction temperature 缺 sensitivity analysis\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W5(Info) raised, R2-Q2 independently提出。采样 T 和 K 均有 sensitivity 分析，但核心瓶颈环节（extraction）的关键参数仅用单一值。\"\n  action_items:\n    - round: 9\n      action: \"补充 T_ext 消融实验或在 limitations 中讨论\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W6\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足——核心 insight 是已知负面结论在符号约束 domain 的 instantiation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2-W1(Critical): 概念层面高度一致，诊断指标是已有方法直接应用。R1 部分反驳：Z3 形式化验证场景非 trivial + 27种 remediation 穷举超越 existence-of-failure。R1=3.5 vs R2=3.0。\"\n  action_items:\n    - round: 9\n      action: \"在 §1 更明确论证 Z3 形式化验证场景下验证此结论的 non-triviality\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W7\"\n  summary: \"Independence-Accuracy Trade-off 作为第一贡献存在部分同义反复（bias-variance tradeoff 重述）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W2(Critical) raised, R1 agrees. Cross-model pattern 本身新颖性有限。但 27 种 within-model remediation 失败使 inescapability claim 成为新贡献。双方同意建议将 Symbolic Confirmation Bias 提升为第一贡献。\"\n  action_items:\n    - round: 9\n      action: \"将 Symbolic Confirmation Bias 提升为第一贡献，Independence-Accuracy Trade-off 降为第二贡献\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W8\"\n  summary: \"遗漏关键相关工作：SatLM (Ye et al., NeurIPS 2023)、VeriCoT (Nov 2025)、CRITIC (Gou et al., ICLR 2024)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W3 raised, R1 agrees. SatLM 使用 LLM+SAT solver 报告正面结果，可与 SICA 负面结果形成 problem-level vs trace-level 对比。VeriCoT 将 CoT 形式化为 FOL。CRITIC 涉及 tool-interactive self-correction。\"\n  action_items:\n    - round: 9\n      action: \"引用 SatLM、VeriCoT、CRITIC 并讨论与本文的区别\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W9\"\n  summary: \"Abstract 'sixteen' vs §4.2 'fifteen' 数字不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W5 raised, R1 confirms. Table 1 有 16 个 non-degenerate 行，Abstract 'sixteen' 正确，§4.2 'fifteen' 为笔误。\"\n  action_items:\n    - round: 9\n      action: \"修正 §4.2 'fifteen' → 'sixteen'\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W10\"\n  summary: \"Cross-architecture escape 实验规模不足，缺少与其他外部验证方法的对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W4 raised, R1 agrees. 仅 DeBERTa NLI 一种外部 verifier，LogiQA 上无效，缺 trained verifiers/code-based verification 对比。论文已定位为 PoC 并在 Limitations 中承认。\"\n  action_items:\n    - round: 9\n      action: \"如有余力，补充与其他外部验证方法的对比；否则在 Limitations 中更明确讨论\"\n      assigned_to: \"research_director\"\n      status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n- id: \"R3-N3\"\n  summary: \"Discriminative rate from small pilot\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"804-instance analysis: 8.2% [CI: 7.6, 8.8].\"\n  resolution_round: 3\n\n- id: \"R3-W6\"\n  summary: \"No 70B+ model tested\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 3\n  last_seen_round: 9\n  resolution: \"Acknowledged as limitation in paper.\"\n  resolution_round: 4\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W4 re-raised: Abstract 'full LLM capability range' overclaims given 7B-32B only. Model range limitation persists.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R9 R2-W8: DeepSeek-R1 distilled models not tested. R1 rebuts: Table 4 has DeepSeek-R1-7B data (n≤60). Scale limitation persists.\"\n\n- id: \"R4-C1\"\n  summary: \"Cross-section Δ inconsistency\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"D064+D066 full data replacement completed.\"\n  resolution_round: 4\n\n- id: \"R4-C2\"\n  summary: \"CJT framing gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Dual-bottleneck paragraph added. Title changed.\"\n  resolution_round: 4\n\n- id: \"R4-C3\"\n  summary: \"Goldilocks zone evidence from only 1 model × 1 dataset\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Claims downgraded to 'directional trend'. V2 framing de-emphasizes intermediate region.\"\n  resolution_round: 5\n\n- id: \"R4-W1\"\n  summary: \"Multiple testing correction\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"BH correction computed: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Eff-K Kish (1965) attribution / κ→ICC proxy rigor\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Pairwise Pearson r (mean 0.625, Mistral-7B) monotonically related to κ across 4 model families. κ validated as consensus proxy.\"\n  resolution_round: 7\n\n- id: \"R4-M5\"\n  summary: \"Figure 2 old data\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Figure 2 moved to Appendix in V2 page budget compression.\"\n  resolution_round: 6\n\n- id: \"R5-N1\"\n  summary: \"Oracle ceiling '24%' cross-model comparison invalid\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Mistral-7B same-model oracle: +29.90pp (p<1e-13).\"\n  resolution_round: 5\n\n- id: \"R5-N2\"\n  summary: \"§4.1 Decoupling interim results (n=70/204) in main text\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"V2 framing removes §4.1 Decoupling from main text entirely.\"\n  resolution_round: 5\n\n- id: \"R5-N3\"\n  summary: \"'Fundamental' trade-off overclaimed\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All 'fundamental' → 'persistent' + 'at the 7B--32B scale'.\"\n  resolution_round: 5\n\n- id: \"R5-N4\"\n  summary: \"DeBERTa PoC statistically fragile — 9 discordant pairs\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"ProofWriter w=3 +3.50pp (p=0.013, n=600) as primary finding.\"\n  resolution_round: 5\n\n- id: \"R5-N5\"\n  summary: \"Discussion/Conclusion too thin for negative paper\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Discussion ~350 words, Conclusion ~220 words.\"\n  resolution_round: 5\n\n- id: \"R5-W1\"\n  summary: \"Variable name isolation confound\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Alpha-equivalence caveat added in Discussion.\"\n  resolution_round: 5\n\n- id: \"R5-W2\"\n  summary: \"Fleiss' κ as ICC proxy lacks formal justification\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Caveat added. Pairwise correlation validates κ (tracked under R4-W3).\"\n  resolution_round: 5\n\n- id: \"R5-W3\"\n  summary: \"Missing ensemble diversity literature\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Krogh & Vedelsby (1994) + Brown et al. (2005) cited.\"\n  resolution_round: 5\n\n- id: \"R5-W4\"\n  summary: \"§3/§5 content duplication\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Not flagged in R6 — considered resolved.\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"'25+ strategies' count inflated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"'more than twenty spanning fifteen distinct families'.\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"Code/data release not mentioned\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Reproducibility paragraph added.\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Solutions before Experiments ordering\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"main.tex reordered correctly.\"\n  resolution_round: 5\n\n- id: \"R5-W8\"\n  summary: \"TF-IDF cosine limitation under-discussed\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 9\n  resolution: \"Deferred to rebuttal. SBERT validation not worth GPU time per Reviewer assessment.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers re-raised: R1-W5 notes Figure 2 R²≈4.4% is very low; R2-Q4 asks if TF-IDF sufficiently captures semantic similarity. Limitation persists.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R1-W5(Info), R2-W7(Info): TF-IDF limitation re-confirmed by both reviewers. Consensus: acknowledged limitation, not blocking.\"\n\n- id: \"R5-W9\"\n  summary: \"CJT novelty / Huang-Stechly distinction insufficient\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Paper Agent added novelty differentiation paragraph (3 quantitative differentiators). Tracked jointly with R6-N3.\"\n  resolution_round: 7\n\n- id: \"R5-TC1\"\n  summary: \"SC tiebreaking inconsistency (dict-order vs alphabetical)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All tiebreaking standardized to alphabetical.\"\n  resolution_round: 5\n\n- id: \"R6-N1\"\n  summary: \"Statistical power 5.7%-20.6% — title 'Fail' overclaims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Title changed to 'Do Not Improve'. TOST computed: 4/15 equivalence, 5/15 genuine difference (4 negative), 6/15 underpowered. Three-tier classification integrated into abstract, §4, appendix.\"\n  resolution_round: 7\n\n- id: \"R6-N2\"\n  summary: \"Cross-arch PoC p=0.013 needs multiple comparison correction\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"BH correction: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Novelty vs self-correction literature (Huang/Stechly/Amonkar)\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  resolution: \"Novelty paragraph added (3 differentiators: κ/Eff-K diagnostics, formal Z3 verification, process-level analysis). §3.3 empirical bound (Δ_max ≤ Oracle_Gap/BR) further differentiates.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W1 re-raised novelty concern despite R7 fix. R1 partially rebuts, citing empirical specificity and quantitative tools. Divergence remains — see R8-W1.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R2-W1(Critical): Novelty gap persists. R1 partially rebuts (Z3 non-triviality + exhaustive remediation). Core divergence: R1=3.5 vs R2=3.0. Director sides with R2 — conceptual increment insufficient for main conference.\"\n\n- id: \"R6-N4\"\n  summary: \"Missing references: CLOVER (ICLR 2025), VERGE, Toh et al. (2024)\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"5 BibTeX entries written (CLOVER, VERGE, Toh et al., Chan et al., Lakens). All cited in Related Work + §4. Author correction applied (Toh et al., not Xia et al.). Orphan bib removed.\"\n  resolution_round: 7\n\n- id: \"R6-W1\"\n  summary: \"Bias ratio numbers inconsistent between main text and Table 14\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent clarified BR calculation scope (Batch 1 W6).\"\n  resolution_round: 7\n\n- id: \"R6-W2\"\n  summary: \"Type A/B/C failure mode classification is post-hoc\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent labeled as 'three empirical regimes (observation-driven)' (Batch 1 W7).\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"Degeneration condition (Eq. 4) derivation incomplete\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Constraint rejection rate 3.44% (no diff correct/incorrect, p=0.636) integrated into §5.2 as empirical evidence for Eq.4 degeneration.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"'Symbolic Mirage' terminology too marketing-like\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  resolution: \"Scoping sentence added: Mirage is specific to self-extracted constraints. §3.3 explicitly contrasts with independently sourced constraints.\"\n  resolution_round: 7\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R9 R2-W6: Terminology branding re-raised. R1 rebuts (operational definitions exist for Mirage and Confirmation Bias). Partial agreement: 'capability trap' can be weakened.\"\n\n- id: \"R6-W5\"\n  summary: \"α=0.5 penalty weight lacks sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"α sensitivity: max 0.49pp variation across α∈{0.0-1.0}. One-sentence note added to §3.2 C₀ diagnostic paragraph.\"\n  resolution_round: 7\n\n- id: \"R6-W6\"\n  summary: \"GSM8K (n=30) and AIME (n=22) in main Table 1 misleading\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Kept with † marker and 'suggestive only' caveat. Degenerate regime demonstration serves pedagogical purpose.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-W1/R2-W5: underpowered conditions still not clearly marked in Table 1. Recommend explicit powered vs. exploratory labeling.\"\n\n- id: \"R6-W7\"\n  summary: \"Orphan bib entry (press2023compositionality)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"press2023compositionality removed from references.bib. All new entries (CLOVER, VERGE, Toh, Chan, Lakens) cited.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"Reasoning models not discussed as category in Related Work\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent added reasoning models paragraph with κ=0.91 homogenization (Batch 1 W14).\"\n  resolution_round: 7\n\n- id: \"R6-V1\"\n  summary: \"Page 20 >75% empty white space\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Page 20 now ~60% filled (TOST section + Extended Limitations). Remaining whitespace is natural appendix pagination.\"\n  resolution_round: 7\n\n- id: \"R6-V2\"\n  summary: \"Main text only 5 display items\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Figure 5 (intervention summary) promoted to main text §5.5; Figure 2 moved to Appendix. Main text now has 2 tables + 2 figures + pipeline diagram.\"\n  resolution_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"Visual check + R2-W6: Figure 5 (intervention strategies) recommended for main text. First 3 pages lack any visual anchor.\"\n\n- id: \"R8-N1\"\n  summary: \"FOL terminology misleading — actual constraints are predominantly propositional ground clauses\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"All 'FOL constraints' → 'logical constraints'. Quantifier proportion (99.0% propositional, 1.0% ∀/∃) added to §3.2 constraint extraction paragraph and Appendix extended limitations.\"\n  resolution_round: 8\n\n- id: \"R8-N2\"\n  summary: \"Cross-architecture PoC underpowered: single generator (Mistral-7B) × inconsistent dataset results\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  resolution: \"§6 restructured: explicit two-generator framing (Mistral-7B positive + Qwen3-14B null confirms capability gap). Invalid Table 3 removed (DeBERTa-large vs DeBERTa-base confound). Clean single-generator evidence retained.\"\n  resolution_round: 8\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R1-W3(Warning): NLI weight w not cross-validated. R2-W4(Warning): cross-arch scale insufficient, no comparison with other external verification methods. Both agree PoC is limited.\"\n\n- id: \"R8-W1\"\n  summary: \"Incremental novelty relative to Huang (2024)/Stechly (2025) self-verification failure literature\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"§2 para 5 (Positioning) articulates 3 quantitative differentiators (Eff-K, BR, C_D) + capability gap corollary. §2 para 3 frames formal verification as 'natural hypothesis' that SICA systematically tests.\"\n  resolution_round: 8\n\n- id: \"R8-W2\"\n  summary: \"Seed replication inconsistency — Table 1 does not mark which conditions have multi-seed support\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Table 1 has $^{4s}$ superscript on 4-seed confirmatory condition + caption note distinguishing confirmatory vs exploratory.\"\n  resolution_round: 8\n\n- id: \"R8-W3\"\n  summary: \"Semantic deduplication missing — syntactic-only dedup may inflate verbose trace weights\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"§3.2 now reports 46.0% global average dedup ratio. Extended limitations discusses Z3 semantic dedup (+~10% removal, p=0.013 vs no dedup).\"\n  resolution_round: 8\n\n- id: \"R8-W4\"\n  summary: \"Domain diversity + model range overclaimed in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Abstract scope accurately reflects 7B-32B range with explicit SC baseline anchors. 'Logical reasoning domains' replaces generic 'reasoning domains'.\"\n  resolution_round: 8\n\n- id: \"R8-W5\"\n  summary: \"Constraint quality analysis (91.8% discriminative rate) based on single model family (Qwen2.5-14B)\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Scoped in extended limitations (Appendix). Main text 91.8% appears with n=804 matching the Qwen2.5-14B analysis.\"\n  resolution_round: 8\n\n- id: \"R8-W6\"\n  summary: \"Symbolic Confirmation Bias lacks theoretical connection to Turpin et al. (2024) unfaithful CoT\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Turpin connection present in §3.3 (concise, integrated into Mirage definition). Discussion also references Turpin. Redundant duplicate removed.\"\n  resolution_round: 8\n\n- id: \"R8-I1\"\n  summary: \"Missing references: Weng et al. (2023) Self-Verification and Madaan et al. (2023) Self-Refine\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Both citations added to §2 para 3 and references.bib by Paper Agent.\"\n  resolution_round: 8\n\n- id: \"R8-I2\"\n  summary: \"Figure 5 (intervention strategies summary) buried in Appendix — should be in main text\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Figure swap complete. Main text §5.5 now has intervention summary figure. Process-kappa scatter referenced as 'Appendix Figure'.\"\n  resolution_round: 8\n\n- id: \"R8-I3\"\n  summary: \"83.3% confirmation bias rate needs per-model breakdown in main text\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Per-model BR (4.97×/3.93×/2.88×) already reported in §5.2 with Table ref. 83.3% is Mistral-specific and appears in that context.\"\n  resolution_round: 8\n\n# =========================================================\n# Round 9 (fresh review) — new issues\n# =========================================================\n\n- id: \"R9-W1\"\n  summary: \"Table 1 显著性声称缺少多重比较校正（16 条件未做 BH）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 raised, R2 agrees. BH校正后 Mistral-7B PW p=0.014 和 Qwen2.5-14B PW p=0.011 均不再显著。不影响核心负面结论，但 'significant degradation' 声称被高估。\"\n  action_items:\n    - round: 9\n      action: \"对 Table 1 的 16 个 non-degenerate 条件应用 BH 校正，或在脚注中说明未校正并弱化 degradation 显著性声称\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W2\"\n  summary: \"κ→Effective-K 映射形式化不足：Fleiss' κ ≠ ICC，但 K_eff 作为核心诊断指标使用权重过大\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W2 raised, R2 agrees. 论文仅一句 'qualitative proxy' 但 K_eff 在全文反复作为定量判断依据（如 '≤1.30 never improves'）。历史 issue R4-W3/R5-W2 曾部分修复但本轮 fresh 审稿认为仍不充分。\"\n  action_items:\n    - round: 9\n      action: \"提供 κ 与 ICC 经验对比，或对 K_eff 定量声称加注 caveat\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W3\"\n  summary: \"NLI combo weight parameter w 未交叉验证，w=5 在不同 generator 上效果不稳定\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W3 raised, R2 agrees. w∈{1,3,5} 在同一测试集选择和评估。w=5 Mistral +10.67pp vs LLaMA +1.67pp(n.s.)。PoC 可接受但需声明 w 是 dataset-specific。\"\n  action_items:\n    - round: 9\n      action: \"声明 w 为 dataset-specific hyperparameter，或补充交叉验证\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W4\"\n  summary: \"Capability Gap Hypothesis sigmoid fit (R²=0.875) 基于 8 个数据点，3 参数过拟合\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W4 raised, R2 agrees. Linear R²=0.823 仅低 0.052。Spearman ρ=0.970 更可靠。应报告 adjusted R² 并弱化 inflection point 数值声称。\"\n  action_items:\n    - round: 9\n      action: \"改用 Spearman ρ 作为主要证据，报告 adjusted R²，弱化 sigmoid inflection 声称\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W5\"\n  summary: \"T_ext=0.3 extraction temperature 缺 sensitivity analysis\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W5(Info) raised, R2-Q2 independently提出。采样 T 和 K 均有 sensitivity 分析，但核心瓶颈环节（extraction）的关键参数仅用单一值。\"\n  action_items:\n    - round: 9\n      action: \"补充 T_ext 消融实验或在 limitations 中讨论\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W6\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足——核心 insight 是已知负面结论在符号约束 domain 的 instantiation\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"[DIVERGENCE] R2-W1(Critical): 概念层面高度一致，诊断指标是已有方法直接应用。R1 部分反驳：Z3 形式化验证场景非 trivial + 27种 remediation 穷举超越 existence-of-failure。R1=3.5 vs R2=3.0。\"\n  action_items:\n    - round: 9\n      action: \"在 §1 更明确论证 Z3 形式化验证场景下验证此结论的 non-triviality\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W7\"\n  summary: \"Independence-Accuracy Trade-off 作为第一贡献存在部分同义反复（bias-variance tradeoff 重述）\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W2(Critical) raised, R1 agrees. Cross-model pattern 本身新颖性有限。但 27 种 within-model remediation 失败使 inescapability claim 成为新贡献。双方同意建议将 Symbolic Confirmation Bias 提升为第一贡献。\"\n  action_items:\n    - round: 9\n      action: \"将 Symbolic Confirmation Bias 提升为第一贡献，Independence-Accuracy Trade-off 降为第二贡献\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W8\"\n  summary: \"遗漏关键相关工作：SatLM (Ye et al., NeurIPS 2023)、VeriCoT (Nov 2025)、CRITIC (Gou et al., ICLR 2024)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W3 raised, R1 agrees. SatLM 使用 LLM+SAT solver 报告正面结果，可与 SICA 负面结果形成 problem-level vs trace-level 对比。VeriCoT 将 CoT 形式化为 FOL。CRITIC 涉及 tool-interactive self-correction。\"\n  action_items:\n    - round: 9\n      action: \"引用 SatLM、VeriCoT、CRITIC 并讨论与本文的区别\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W9\"\n  summary: \"Abstract 'sixteen' vs §4.2 'fifteen' 数字不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W5 raised, R1 confirms. Table 1 有 16 个 non-degenerate 行，Abstract 'sixteen' 正确，§4.2 'fifteen' 为笔误。\"\n  action_items:\n    - round: 9\n      action: \"修正 §4.2 'fifteen' → 'sixteen'\"\n      assigned_to: \"research_director\"\n      status: open\n\n- id: \"R9-W10\"\n  summary: \"Cross-architecture escape 实验规模不足，缺少与其他外部验证方法的对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W4 raised, R1 agrees. 仅 DeBERTa NLI 一种外部 verifier，LogiQA 上无效，缺 trained verifiers/code-based verification 对比。论文已定位为 PoC 并在 Limitations 中承认。\"\n  action_items:\n    - round: 9\n      action: \"如有余力，补充与其他外部验证方法的对比；否则在 Limitations 中更明确讨论\"\n      assigned_to: \"research_director\"\n      status: open"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-21T01:57:28.221768+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 25434}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-21T01:59:54.351011+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "symb_invariant_consensus",
  "report": "# 审稿报告 — Round 9 (Fresh Review)\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)\n**审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文研究 SICA（Symbolic Invariant Consensus Aggregation），从 LLM reasoning traces 中自提取逻辑约束并通过 Z3 MAX-SAT 聚合，试图改善 Self-Consistency majority voting。在 6 个模型 (7B-32B)、3 个逻辑推理 domain、3000+ condition-evaluations 上，结论为：self-extracted constraints 因 Symbolic Confirmation Bias（BR=4.97×, 83.3% wrong-supporting rate）无法改善 SC。Oracle controls 证明机制本身有效（FOLIO +29.90pp），瓶颈定位在 self-extraction 质量。27 种 remediation 策略全部失败，cross-architecture NLI verification 提供了建设性的正向方向。\n\n---\n\n## Strengths\n\n**S1. 实验规模和系统性.** 6 个模型（3 model families, 7B-32B）、3 个 domain、3000+ condition-evaluations、~1250 unique instances、4-seed replication。对负面结果论文而言覆盖面出色。[R1, R2 共识]\n\n**S2. Oracle Controls 精准定位瓶颈.** Gold-SICA 在 FOLIO +29.90pp（p < 10⁻¹³）、ProofWriter +11.50pp（p < 10⁻¹⁴），干净地将「机制有效性」与「self-extraction 信号质量」解耦。这是论文最有说服力的实验设计。[R1, R2 共识]\n\n**S3. 25+ Remediation 穷举.** 涵盖 prompt-level、method-level、paradigm-level 共 15 个 family 的 27 种策略，全部 neutral-to-negative。封堵了\"只是 prompt 没调好\"的反驳空间。[R1, R2 共识]\n\n**S4. 统计方法论透明.** Power analysis 明确指出 underpowered conditions，TOST 等价检验区分三类结论，bootstrap CIs 报告，seed-level 不稳定性如实呈现。[R1, R2 共识]\n\n**S5. 可复用诊断指标.** Effective-K、Bias Ratio、ProcessSim 超越本文语境，可用于任何 trace-aggregation 系统的失败预测。[R1]\n\n**S6. Cross-Architecture Escape.** DeBERTa NLI 在 ProofWriter 上 +3.50pp（BH 校正后 adj p=0.038），3 种 NLI architecture 复现，提供建设性方向。[R1, R2 共识]\n\n**S7. 写作结构清晰.** 论文组织合理，从 CJT 动机 → SICA pipeline → 实验 → 分析 → remediation → cross-arch escape 的叙事逻辑完整。[R2]\n\n**S8. 格式合规.** 8 页正文、匿名化完整、Limitations 位置正确、引用格式规范。[R2 确认]\n\n---\n\n## Weaknesses\n\n### Must-Address（影响整体评估）\n\n**W1 [Warning] 相对于 Huang/Stechly 的增量新颖性不足.** 核心发现（LLM self-extracted verification 无法改善推理）与 Huang et al. (ICLR 2024) 和 Stechly et al. (ICLR 2025) 在概念层面高度一致。三个诊断指标（Eff-K, BR, process-κ）分别是 Kish's design effect、条件概率比、TF-IDF cosine similarity 的直接应用。\"Symbolic Mirage\" 本质是已知原理在符号约束 domain 的 instantiation。R1 认为 Z3 形式化验证场景的 non-triviality 和 27 种 remediation 穷举超越 prior work，但 R2 认为概念层面的增量不足以支撑 main conference。\n- **R1/R2 divergence**: R1=3.5 Borderline Conference vs R2=3.0 Findings\n- **Director 裁决**: R2 的判断更有说服力——论文的核心 insight 在 prior work 中已有定性论证，本文的主要贡献在于 domain-specific 的定量验证和穷举分析，这更适合 Findings 定位。\n\n**W2 [Warning] Independence-Accuracy Trade-off 作为第一贡献存在部分同义反复.** Table 2/Figure 7 的 cross-model pattern（弱模型=高独立性+低准确率，强模型=低独立性+高准确率）本质上接近经典 bias-variance tradeoff。27 种 within-model remediation 全部失败增强了 inescapability claim，但 cross-model pattern 本身新颖性有限。双方共识建议将 Symbolic Confirmation Bias 提升为第一贡献。[R1 AGREE, R2 raised]\n\n**W3 [Warning] Table 1 的显著性声称缺少多重比较校正.** 16 个 non-degenerate 条件的 McNemar tests 未做 BH 校正。两个 \"significant degradation\"（Mistral-7B PW p=0.014, Qwen2.5-14B PW p=0.011）BH 校正后均不再显著。不影响核心负面结论，但 degradation 声称被高估。论文在 NLI 结果中正确使用了 BH（m=12），应统一标准。[R1 raised, R2 AGREE]\n\n**W4 [Warning] κ→Effective-K 映射形式化不足.** Eq.1 的 design-effect 公式源自 Kish (1965) 的 ICC (ρ)，Fleiss' κ 是 chance-corrected 一致性指标，数值范围和统计性质与 ICC 不同。论文仅一句 \"qualitative proxy\"，但 K_eff 在全文中作为核心诊断指标反复使用（如 \"≤1.30 never improves\"），超出了 proxy 的定位。[R1 raised, R2 AGREE]\n\n### Should-Fix（投稿前建议修复）\n\n**W5 [Warning] 遗漏关键相关工作.** SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM+SAT solver 且报告正面结果——可与 SICA 负面结果形成 problem-level vs trace-level 对比，强化 Symbolic Mirage 论点。VeriCoT (Nov 2025) 将 CoT 形式化为 FOL 验证。CRITIC (Gou et al., ICLR 2024) 涉及 tool-interactive self-correction。[R2 raised, R1 AGREE]\n\n**W6 [Warning] NLI combo weight parameter w 未交叉验证.** w ∈ {1, 3, 5} 在同一测试集选择和评估。w=5 在 Mistral-7B 上 +10.67pp 但在 LLaMA-3.1-8B 上仅 +1.67pp (n.s.)，表明最优 w 不稳定。PoC 可接受但需声明 w 是 dataset-specific hyperparameter。[R1 raised, R2 AGREE]\n\n**W7 [Warning] Capability Gap Hypothesis sigmoid fit (R²=0.875) 基于 8 个数据点.** 3 参数 sigmoid 拟合 8 个点，adjusted R² 会大幅低于 0.875。Linear R²=0.823 仅低 0.052。Spearman ρ=0.970 更可靠。应改用 rank correlation 作为主要证据，弱化 inflection point 数值声称。[R1 raised, R2 AGREE]\n\n**W8 [Warning] T_ext=0.3 extraction temperature 缺 sensitivity analysis.** 采样 T 和 K 均有 sensitivity 分析，但 extraction——论文认定的核心瓶颈环节——的关键参数仅用单一值。[R1 raised, R2 AGREE via Q2]\n\n**W9 [Warning] Cross-architecture escape 实验规模不足.** 仅一种外部 verifier (DeBERTa NLI)、两个 dataset、三个 generator family。LogiQA 上无效。缺少与 trained verifiers/code-based verification 的对比。论文已定位为 PoC 并在 Limitations 中承认，但短板明显。[R2 raised, R1 AGREE]\n\n### Minor Issues\n\n**W10 [Info] Abstract \"sixteen\" vs §4.2 \"fifteen\" 数字不一致.** Table 1 有 16 个 non-degenerate 行，Abstract \"sixteen\" 正确，§4.2 \"fifteen\" 为笔误。[R2 raised, R1 confirms]\n\n**W11 [Info] 术语品牌化讨论.** R2 认为 \"Symbolic Mirage\"、\"Symbolic Confirmation Bias\"、\"capability trap\" 对 incremental 负面结果论文而言品牌术语过多。R1 反驳前两者有精确操作定义（Eq.5, §5.2），但同意 \"capability trap\" 可弱化。[DIVERGENCE — R1 REBUT, R2 raised]\n\n**W12 [Info] σ(c,a) provenance-based 设计未作为 design limitation 讨论.** R1 指出 σ(c,a)=1 iff c 来自产生 answer a 的 trace，这是导致 degeneration 的直接原因，论文未讨论基于 Z3 semantic evaluation 的替代设计。R2 反驳存在循环依赖问题且在 BR=4.97× 下两种 σ 定义结果应趋同。[DIVERGENCE — R1 raised, R2 REBUT]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Table 1 需要多重比较校正**（W3）—— 不影响核心结论但需统一标准\n2. **κ→K_eff 形式化不足**（W4）—— 需要更 rigorous 的论证或 caveat\n3. **NLI weight w 未交叉验证**（W6）—— 需声明 dataset-specific\n4. **Sigmoid fit 过拟合**（W7）—— 改用 Spearman ρ 作为主要证据\n5. **T_ext sensitivity 缺失**（W8）—— 核心瓶颈参数应有消融\n6. **遗漏 SatLM/VeriCoT/CRITIC**（W5）—— 必须引用\n7. **\"fifteen\" 笔误**（W10）—— 修正为 \"sixteen\"\n8. **Contribution 排序**（W2）—— Symbolic Confirmation Bias 应为第一贡献\n9. **实验覆盖面 + Oracle controls + 25+ remediation 穷举是论文核心优势**（S1-S3）\n10. **统计透明度和可复用诊断指标有独立价值**（S4-S5）\n\n## Reviewer Divergence [REBUT remaining]\n\n1. **Novelty 判断**（W1）: R1 认为 Z3 非 triviality + exhaustive remediation 足够 Borderline Conference (3.5)；R2 认为概念层面是 Huang/Stechly instantiation，仅够 Findings (3.0)。Director 倾向 R2 的判断。\n2. **术语品牌化**（W11）: R1 认为有操作定义不算品牌化；R2 认为过度。部分共识：前两个可保留，\"capability trap\" 弱化。\n3. **σ(c,a) 设计**（W12）: R1 认为应讨论替代方案；R2 认为循环依赖使替代不可行。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Table 1 \"4s\" 标注的确切含义及其对可信度判断的影响？[R1]\n**Q2.** MAX-SAT constraint rejection rate 3.4% 的分布——高 rejection 的 cases 是否系统性优于 SC？[R1]\n**Q3.** 是否测试过 answer assertion weight = 0 的变体？[R1]\n**Q4.** Z3 semantic deduplication (p=0.013) 正面结果为何未在正文中讨论？[R1]\n**Q5.** Intermediate-SC regime 的 sweet spot 是否可系统化刻画？[R2]\n**Q6.** Partially gold constraints（0%-100% mixing curve）的退化曲线？[R2]\n\n---\n\n## Missing References\n\n1. **SatLM** (Ye et al., NeurIPS 2023) — LLM + SAT solver 正面结果，与 SICA 负面结果形成关键对比\n2. **VeriCoT** (arXiv 2511.04662, Nov 2025) — CoT → FOL 验证\n3. **CRITIC** (Gou et al., ICLR 2024) — Tool-interactive self-correction\n\n[R2 raised, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。项目未配置 `external_review.paperreview_ai.enabled`。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（4 warning, 14 info, 0 critical）\n\n### Warning 级发现\n1. **Pages 1-3 连续 3 页纯文本无 display item.** 第一个视觉锚点（Figure 1 SICA pipeline）直到 page 4 才出现。审稿人在前 2 分钟内只看到密集双栏文字。建议将 Figure 1 提前或加入 teaser figure。\n2. **Page 5 纯文本断层.** Experiments 设置部分整页纯文本，与前后 display items 间形成文本断层。\n3. **Figure 1 仅占单栏宽度.** 作为论文第一个也是最重要的概念图，视觉冲击力不足。建议改用 figure*（全宽）。\n4. **Page 8 内容过度密集.** Figure 3 + Table 3 + Discussion + Conclusion 挤在一页，Conclusion 仅 8-10 行，显得仓促。\n\n### Info 级发现\n- 格式整体规范：ACL 匿名提交格式正确，Table 1 全宽 booktabs 风格专业，Algorithm 伪代码可读\n- 公式渲染正确，无 LaTeX 错误残留，无 overfull hbox，无 [?] 未解析引用\n- Appendix 部分表格字号偏小但可接受\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分依据:**\n- **Soundness 3.5/5**: 核心 pipeline 形式化完整，oracle controls 有力。但 Table 1 多重比较未校正、κ→K_eff 映射形式化不足、sigmoid fit 过拟合等统计问题累积削弱\"精确定量诊断工具\"这一核心卖点的可信度。\n- **Excitement 3.0/5**: R1=3.5 vs R2=2.5，Director 取 3.0。核心负面结论（self-verification 无法改善推理）已有 prior work 定性论证。本文的主要贡献在于 domain-specific 定量验证 + 穷举 remediation + 可复用诊断工具，这些在 Findings 级别具有明确价值，但概念层面的增量不足以支撑 main conference。\n- **Reproducibility 4.0/5**: 实验参数详尽，承诺发布代码/数据，附录含完整 prompt 和伪代码。\n\n**核心理由:**\n1. 论文的实验 thoroughness 和统计透明度值得肯定——6 models × 3 domains × 27 remediation strategies × oracle controls 的规模在负面结果论文中罕见。\n2. 但\"self-extracted 信号无法改善 self-reasoning\"在 Huang (2024) 和 Stechly (2025) 之后已非 surprising。本文的核心贡献是将此结论从 natural-language self-correction 扩展到 formal Z3-checked verification——这是有价值的 domain-specific 验证，但概念跃迁有限。\n3. 诊断工具（Eff-K, BR, process-κ）有独立复用价值，但每个工具本身是已有方法的直接应用。\n4. 若干统计分析环节（W3, W4, W7）削弱了定量声称的精确度。\n5. Cross-architecture escape 是建设性方向但规模有限（W6, W7, W9）。\n\n**Confidence: 4/5**\n\n---\n\n## Detailed Comments（按章节）\n\n### Abstract\n- \"sixteen non-degenerate conditions\" 正确，§4.2 的 \"fifteen\" 需修正\n- 范围界定改善良好（\"six open-source LLMs (7B-32B)\"），但仍需注意 logical reasoning domains 的局限性\n- 关键数字（BR=4.97×, 83.3%, process cosine 0.69 vs κ 0.41）直接给出，信息密度高\n\n### §1 Introduction\n- CJT 动机清晰，从理论 gap → 实践问题的叙事逻辑通顺\n- 建议更明确论证 Z3 形式化验证场景下测试此结论的 non-triviality（vs Huang/Stechly 的 NL self-correction）\n- 三个 contributions 的排列建议调整：Symbolic Confirmation Bias 应为第一贡献\n\n### §2 Related Work\n- 覆盖面广（5 个段落），引用规范\n- 遗漏 SatLM、VeriCoT、CRITIC 三篇\n- Positioning 段的 3 differentiators 需要更有力的 defense\n\n### §3 Background & Setup\n- SICA pipeline 形式化完整（Eq.1-5, Algorithm 1-2）\n- κ→K_eff 映射需更 rigorous 论证\n- Symbolic Mirage Hypothesis 的 3 testable predictions 是好的论文结构\n\n### §4 Experiments\n- Table 1 需统一应用 BH 校正\n- Oracle controls 是最有说服力的实验\n\n### §5 Analysis\n- §5.2 Symbolic Confirmation Bias 是论文最强发现\n- §5.3 Process-level Independence 是独特贡献但 TF-IDF metric 有局限\n- §5.5 Remediation 穷举极具说服力\n\n### §6 Cross-Architecture PoC\n- w 参数需交叉验证或声明 dataset-specific\n- Sigmoid fit 应改用 Spearman ρ\n- 整体规模有限但作为 PoC 可接受\n\n### §7-8 Discussion/Conclusion\n- 对负面结果论文而言偏短（Discussion ~350 words, Conclusion ~220 words），但关键 takeaway 清晰\n- Page 8 排版过密\n\n### Limitations\n- 位置正确（参考文献前），内容充实\n- 建议补充 T_ext sensitivity 缺失的讨论",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "report": "# 审稿报告 — Round 9 (Fresh Review)\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)\n**审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n本文研究 SICA（Symbolic Invariant Consensus Aggregation），从 LLM reasoning traces 中自提取逻辑约束并通过 Z3 MAX-SAT 聚合，试图改善 Self-Consistency majority voting。在 6 个模型 (7B-32B)、3 个逻辑推理 domain、3000+ condition-evaluations 上，结论为：self-extracted constraints 因 Symbolic Confirmation Bias（BR=4.97×, 83.3% wrong-supporting rate）无法改善 SC。Oracle controls 证明机制本身有效（FOLIO +29.90pp），瓶颈定位在 self-extraction 质量。27 种 remediation 策略全部失败，cross-architecture NLI verification 提供了建设性的正向方向。\n\n---\n\n## Strengths\n\n**S1. 实验规模和系统性.** 6 个模型（3 model families, 7B-32B）、3 个 domain、3000+ condition-evaluations、~1250 unique instances、4-seed replication。对负面结果论文而言覆盖面出色。[R1, R2 共识]\n\n**S2. Oracle Controls 精准定位瓶颈.** Gold-SICA 在 FOLIO +29.90pp（p < 10⁻¹³）、ProofWriter +11.50pp（p < 10⁻¹⁴），干净地将「机制有效性」与「self-extraction 信号质量」解耦。这是论文最有说服力的实验设计。[R1, R2 共识]\n\n**S3. 25+ Remediation 穷举.** 涵盖 prompt-level、method-level、paradigm-level 共 15 个 family 的 27 种策略，全部 neutral-to-negative。封堵了\"只是 prompt 没调好\"的反驳空间。[R1, R2 共识]\n\n**S4. 统计方法论透明.** Power analysis 明确指出 underpowered conditions，TOST 等价检验区分三类结论，bootstrap CIs 报告，seed-level 不稳定性如实呈现。[R1, R2 共识]\n\n**S5. 可复用诊断指标.** Effective-K、Bias Ratio、ProcessSim 超越本文语境，可用于任何 trace-aggregation 系统的失败预测。[R1]\n\n**S6. Cross-Architecture Escape.** DeBERTa NLI 在 ProofWriter 上 +3.50pp（BH 校正后 adj p=0.038），3 种 NLI architecture 复现，提供建设性方向。[R1, R2 共识]\n\n**S7. 写作结构清晰.** 论文组织合理，从 CJT 动机 → SICA pipeline → 实验 → 分析 → remediation → cross-arch escape 的叙事逻辑完整。[R2]\n\n**S8. 格式合规.** 8 页正文、匿名化完整、Limitations 位置正确、引用格式规范。[R2 确认]\n\n---\n\n## Weaknesses\n\n### Must-Address（影响整体评估）\n\n**W1 [Warning] 相对于 Huang/Stechly 的增量新颖性不足.** 核心发现（LLM self-extracted verification 无法改善推理）与 Huang et al. (ICLR 2024) 和 Stechly et al. (ICLR 2025) 在概念层面高度一致。三个诊断指标（Eff-K, BR, process-κ）分别是 Kish's design effect、条件概率比、TF-IDF cosine similarity 的直接应用。\"Symbolic Mirage\" 本质是已知原理在符号约束 domain 的 instantiation。R1 认为 Z3 形式化验证场景的 non-triviality 和 27 种 remediation 穷举超越 prior work，但 R2 认为概念层面的增量不足以支撑 main conference。\n- **R1/R2 divergence**: R1=3.5 Borderline Conference vs R2=3.0 Findings\n- **Director 裁决**: R2 的判断更有说服力——论文的核心 insight 在 prior work 中已有定性论证，本文的主要贡献在于 domain-specific 的定量验证和穷举分析，这更适合 Findings 定位。\n\n**W2 [Warning] Independence-Accuracy Trade-off 作为第一贡献存在部分同义反复.** Table 2/Figure 7 的 cross-model pattern（弱模型=高独立性+低准确率，强模型=低独立性+高准确率）本质上接近经典 bias-variance tradeoff。27 种 within-model remediation 全部失败增强了 inescapability claim，但 cross-model pattern 本身新颖性有限。双方共识建议将 Symbolic Confirmation Bias 提升为第一贡献。[R1 AGREE, R2 raised]\n\n**W3 [Warning] Table 1 的显著性声称缺少多重比较校正.** 16 个 non-degenerate 条件的 McNemar tests 未做 BH 校正。两个 \"significant degradation\"（Mistral-7B PW p=0.014, Qwen2.5-14B PW p=0.011）BH 校正后均不再显著。不影响核心负面结论，但 degradation 声称被高估。论文在 NLI 结果中正确使用了 BH（m=12），应统一标准。[R1 raised, R2 AGREE]\n\n**W4 [Warning] κ→Effective-K 映射形式化不足.** Eq.1 的 design-effect 公式源自 Kish (1965) 的 ICC (ρ)，Fleiss' κ 是 chance-corrected 一致性指标，数值范围和统计性质与 ICC 不同。论文仅一句 \"qualitative proxy\"，但 K_eff 在全文中作为核心诊断指标反复使用（如 \"≤1.30 never improves\"），超出了 proxy 的定位。[R1 raised, R2 AGREE]\n\n### Should-Fix（投稿前建议修复）\n\n**W5 [Warning] 遗漏关键相关工作.** SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM+SAT solver 且报告正面结果——可与 SICA 负面结果形成 problem-level vs trace-level 对比，强化 Symbolic Mirage 论点。VeriCoT (Nov 2025) 将 CoT 形式化为 FOL 验证。CRITIC (Gou et al., ICLR 2024) 涉及 tool-interactive self-correction。[R2 raised, R1 AGREE]\n\n**W6 [Warning] NLI combo weight parameter w 未交叉验证.** w ∈ {1, 3, 5} 在同一测试集选择和评估。w=5 在 Mistral-7B 上 +10.67pp 但在 LLaMA-3.1-8B 上仅 +1.67pp (n.s.)，表明最优 w 不稳定。PoC 可接受但需声明 w 是 dataset-specific hyperparameter。[R1 raised, R2 AGREE]\n\n**W7 [Warning] Capability Gap Hypothesis sigmoid fit (R²=0.875) 基于 8 个数据点.** 3 参数 sigmoid 拟合 8 个点，adjusted R² 会大幅低于 0.875。Linear R²=0.823 仅低 0.052。Spearman ρ=0.970 更可靠。应改用 rank correlation 作为主要证据，弱化 inflection point 数值声称。[R1 raised, R2 AGREE]\n\n**W8 [Warning] T_ext=0.3 extraction temperature 缺 sensitivity analysis.** 采样 T 和 K 均有 sensitivity 分析，但 extraction——论文认定的核心瓶颈环节——的关键参数仅用单一值。[R1 raised, R2 AGREE via Q2]\n\n**W9 [Warning] Cross-architecture escape 实验规模不足.** 仅一种外部 verifier (DeBERTa NLI)、两个 dataset、三个 generator family。LogiQA 上无效。缺少与 trained verifiers/code-based verification 的对比。论文已定位为 PoC 并在 Limitations 中承认，但短板明显。[R2 raised, R1 AGREE]\n\n### Minor Issues\n\n**W10 [Info] Abstract \"sixteen\" vs §4.2 \"fifteen\" 数字不一致.** Table 1 有 16 个 non-degenerate 行，Abstract \"sixteen\" 正确，§4.2 \"fifteen\" 为笔误。[R2 raised, R1 confirms]\n\n**W11 [Info] 术语品牌化讨论.** R2 认为 \"Symbolic Mirage\"、\"Symbolic Confirmation Bias\"、\"capability trap\" 对 incremental 负面结果论文而言品牌术语过多。R1 反驳前两者有精确操作定义（Eq.5, §5.2），但同意 \"capability trap\" 可弱化。[DIVERGENCE — R1 REBUT, R2 raised]\n\n**W12 [Info] σ(c,a) provenance-based 设计未作为 design limitation 讨论.** R1 指出 σ(c,a)=1 iff c 来自产生 answer a 的 trace，这是导致 degeneration 的直接原因，论文未讨论基于 Z3 semantic evaluation 的替代设计。R2 反驳存在循环依赖问题且在 BR=4.97× 下两种 σ 定义结果应趋同。[DIVERGENCE — R1 raised, R2 REBUT]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Table 1 需要多重比较校正**（W3）—— 不影响核心结论但需统一标准\n2. **κ→K_eff 形式化不足**（W4）—— 需要更 rigorous 的论证或 caveat\n3. **NLI weight w 未交叉验证**（W6）—— 需声明 dataset-specific\n4. **Sigmoid fit 过拟合**（W7）—— 改用 Spearman ρ 作为主要证据\n5. **T_ext sensitivity 缺失**（W8）—— 核心瓶颈参数应有消融\n6. **遗漏 SatLM/VeriCoT/CRITIC**（W5）—— 必须引用\n7. **\"fifteen\" 笔误**（W10）—— 修正为 \"sixteen\"\n8. **Contribution 排序**（W2）—— Symbolic Confirmation Bias 应为第一贡献\n9. **实验覆盖面 + Oracle controls + 25+ remediation 穷举是论文核心优势**（S1-S3）\n10. **统计透明度和可复用诊断指标有独立价值**（S4-S5）\n\n## Reviewer Divergence [REBUT remaining]\n\n1. **Novelty 判断**（W1）: R1 认为 Z3 非 triviality + exhaustive remediation 足够 Borderline Conference (3.5)；R2 认为概念层面是 Huang/Stechly instantiation，仅够 Findings (3.0)。Director 倾向 R2 的判断。\n2. **术语品牌化**（W11）: R1 认为有操作定义不算品牌化；R2 认为过度。部分共识：前两个可保留，\"capability trap\" 弱化。\n3. **σ(c,a) 设计**（W12）: R1 认为应讨论替代方案；R2 认为循环依赖使替代不可行。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Table 1 \"4s\" 标注的确切含义及其对可信度判断的影响？[R1]\n**Q2.** MAX-SAT constraint rejection rate 3.4% 的分布——高 rejection 的 cases 是否系统性优于 SC？[R1]\n**Q3.** 是否测试过 answer assertion weight = 0 的变体？[R1]\n**Q4.** Z3 semantic deduplication (p=0.013) 正面结果为何未在正文中讨论？[R1]\n**Q5.** Intermediate-SC regime 的 sweet spot 是否可系统化刻画？[R2]\n**Q6.** Partially gold constraints（0%-100% mixing curve）的退化曲线？[R2]\n\n---\n\n## Missing References\n\n1. **SatLM** (Ye et al., NeurIPS 2023) — LLM + SAT solver 正面结果，与 SICA 负面结果形成关键对比\n2. **VeriCoT** (arXiv 2511.04662, Nov 2025) — CoT → FOL 验证\n3. **CRITIC** (Gou et al., ICLR 2024) — Tool-interactive self-correction\n\n[R2 raised, R1 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。项目未配置 `external_review.paperreview_ai.enabled`。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（4 warning, 14 info, 0 critical）\n\n### Warning 级发现\n1. **Pages 1-3 连续 3 页纯文本无 display item.** 第一个视觉锚点（Figure 1 SICA pipeline）直到 page 4 才出现。审稿人在前 2 分钟内只看到密集双栏文字。建议将 Figure 1 提前或加入 teaser figure。\n2. **Page 5 纯文本断层.** Experiments 设置部分整页纯文本，与前后 display items 间形成文本断层。\n3. **Figure 1 仅占单栏宽度.** 作为论文第一个也是最重要的概念图，视觉冲击力不足。建议改用 figure*（全宽）。\n4. **Page 8 内容过度密集.** Figure 3 + Table 3 + Discussion + Conclusion 挤在一页，Conclusion 仅 8-10 行，显得仓促。\n\n### Info 级发现\n- 格式整体规范：ACL 匿名提交格式正确，Table 1 全宽 booktabs 风格专业，Algorithm 伪代码可读\n- 公式渲染正确，无 LaTeX 错误残留，无 overfull hbox，无 [?] 未解析引用\n- Appendix 部分表格字号偏小但可接受\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分依据:**\n- **Soundness 3.5/5**: 核心 pipeline 形式化完整，oracle controls 有力。但 Table 1 多重比较未校正、κ→K_eff 映射形式化不足、sigmoid fit 过拟合等统计问题累积削弱\"精确定量诊断工具\"这一核心卖点的可信度。\n- **Excitement 3.0/5**: R1=3.5 vs R2=2.5，Director 取 3.0。核心负面结论（self-verification 无法改善推理）已有 prior work 定性论证。本文的主要贡献在于 domain-specific 定量验证 + 穷举 remediation + 可复用诊断工具，这些在 Findings 级别具有明确价值，但概念层面的增量不足以支撑 main conference。\n- **Reproducibility 4.0/5**: 实验参数详尽，承诺发布代码/数据，附录含完整 prompt 和伪代码。\n\n**核心理由:**\n1. 论文的实验 thoroughness 和统计透明度值得肯定——6 models × 3 domains × 27 remediation strategies × oracle controls 的规模在负面结果论文中罕见。\n2. 但\"self-extracted 信号无法改善 self-reasoning\"在 Huang (2024) 和 Stechly (2025) 之后已非 surprising。本文的核心贡献是将此结论从 natural-language self-correction 扩展到 formal Z3-checked verification——这是有价值的 domain-specific 验证，但概念跃迁有限。\n3. 诊断工具（Eff-K, BR, process-κ）有独立复用价值，但每个工具本身是已有方法的直接应用。\n4. 若干统计分析环节（W3, W4, W7）削弱了定量声称的精确度。\n5. Cross-architecture escape 是建设性方向但规模有限（W6, W7, W9）。\n\n**Confidence: 4/5**\n\n---\n\n## Detailed Comments（按章节）\n\n### Abstract\n- \"sixteen non-degenerate conditions\" 正确，§4.2 的 \"fifteen\" 需修正\n- 范围界定改善良好（\"six open-source LLMs (7B-32B)\"），但仍需注意 logical reasoning domains 的局限性\n- 关键数字（BR=4.97×, 83.3%, process cosine 0.69 vs κ 0.41）直接给出，信息密度高\n\n### §1 Introduction\n- CJT 动机清晰，从理论 gap → 实践问题的叙事逻辑通顺\n- 建议更明确论证 Z3 形式化验证场景下测试此结论的 non-triviality（vs Huang/Stechly 的 NL self-correction）\n- 三个 contributions 的排列建议调整：Symbolic Confirmation Bias 应为第一贡献\n\n### §2 Related Work\n- 覆盖面广（5 个段落），引用规范\n- 遗漏 SatLM、VeriCoT、CRITIC 三篇\n- Positioning 段的 3 differentiators 需要更有力的 defense\n\n### §3 Background & Setup\n- SICA pipeline 形式化完整（Eq.1-5, Algorithm 1-2）\n- κ→K_eff 映射需更 rigorous 论证\n- Symbolic Mirage Hypothesis 的 3 testable predictions 是好的论文结构\n\n### §4 Experiments\n- Table 1 需统一应用 BH 校正\n- Oracle controls 是最有说服力的实验\n\n### §5 Analysis\n- §5.2 Symbolic Confirmation Bias 是论文最强发现\n- §5.3 Process-level Independence 是独特贡献但 TF-IDF metric 有局限\n- §5.5 Remediation 穷举极具说服力\n\n### §6 Cross-Architecture PoC\n- w 参数需交叉验证或声明 dataset-specific\n- Sigmoid fit 应改用 Spearman ρ\n- 整体规模有限但作为 PoC 可接受\n\n### §7-8 Discussion/Conclusion\n- 对负面结果论文而言偏短（Discussion ~350 words, Conclusion ~220 words），但关键 takeaway 清晰\n- Page 8 排版过密\n\n### Limitations\n- 位置正确（参考文献前），内容充实\n- 建议补充 T_ext sensitivity 缺失的讨论",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-21T01:59:59.232051+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4881
}
```

</details>

---


### Assistant

_source line 904 · 2026-05-21T02:00:09.369457+00:00_

审稿报告已投递给 Research Director。

---

**圆桌审稿完成 — Round 9 Summary**

**Overall: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | **3.0** |

**10 个新 issue（全部 open）**: W1-W9 (warning) + W10 (info)。核心分歧在 novelty 判断（R1 认为 Z3 场景 + 穷举 remediation 足够 Borderline Conference，R2 认为概念层面是 Huang/Stechly instantiation），Director 裁决倾向 R2。

**优先修复**: (1) 引用 SatLM/VeriCoT/CRITIC; (2) Table 1 BH 校正; (3) Contribution 排序调整; (4) §4.2 "fifteen"→"sixteen" 笔误; (5) §1 强化 Z3 non-triviality 论证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 58

## Round 58

2 recorded events


### User

_source line 905 · 2026-05-21T02:00:12.208230+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：对 R2 的 13 条意见（W1–W8 + Q1–Q5），我给出 5 个 REBUT（W1 部分反驳、W6 部分反驳、W8 部分反驳、Q4 完全反驳、Q5 完全反驳）和 8 个 AGREE（W2 部分同意、W3–W5、W7、Q1–Q3）。核心分歧在 novelty 评估：R2 认为 3.0 Findings，我认为 Z3 形式化验证场景的 non-triviality 和 27 种 remediation 的穷举 rigor 支撑 3.5 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 906 · 2026-05-21T02:00:23.594364+00:00_

审稿报告已投递完毕。

**圆桌审稿总结**:
- **R1**: 3.5 Borderline Conference（方法严谨性审查）
- **R2**: 3.0 Findings（新颖性/完整性审查）
- **Director 综合评分**: **3.0 (Findings)**

**共识**: 9 项（Table 1 多重比较、κ→K_eff 形式化、NLI weight 交叉验证、sigmoid 过拟合、T_ext sensitivity、遗漏引用、cross-arch 规模、数字笔误、contribution 排序）。**分歧**: 3 项（novelty 判断、术语品牌化、σ(c,a) 设计）。

**10 个 open issues** 已写入 `review_issues.yaml`。报告已通过 `submit_review_report_to_research_director` 投递。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 59

## Round 59

82 recorded events


### User

_source line 907 · 2026-05-21T06:29:29.514391+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-21T06:29:36.263371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-21T06:29:36.314483+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-21T06:29:41.537144+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-21T06:29:41.587755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-21T06:29:45.155384+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-21T06:29:46.191798+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (149 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_text_ablation | Constraint extraction temperature (T_ext) does not significantly affect SICA accuracy because confirmation bias is inherent to self-extraction regardless of temperature — constraints at any T_ext will project the model's distributional bias rather than provide independent verification signal | — | — | — |\n| exp-text-ablation | Constraint extraction temperature (T_ext) affects SICA accuracy: moderate T_ext (0.3-0.5) produces more diverse yet valid constraints than extremes (0.1 too deterministic, 1.0 too noisy), yielding higher SICA-SC delta on FOLIO-204. | — | — | — |\n\n## 待处理\n- exp-077-generalization-kappa: Generalization: independence bottleneck (high κ) applies to Debate and Diverse-Prompt aggregation, not just SC+SICA. 在 Mistral-7B FOLIO-204 上测量 3 种聚合方式的 Fleiss' κ + Eff-K: (a) Standard SC (复用 exp-033 traces), (b) LLM-Debate traces (4组×3轮=12 answer points), (c) Diverse-Prompt traces (4种 prompt×3次=12). 如果三种方式 κ 均 > 0.4，证明 independence bottleneck 是 same-model aggregation 的通病。（准备中）\n- exp-063-llama8b-folio204（准备中）\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **exp-092-llama8b-pw-nli-combo** (success): LLaM
…[truncated 1768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1036
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-21T06:29:46.343314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-21T06:29:46.343761+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\newtheorem{proposition}{Proposition}
14	\newtheorem{corollary}{Corollary}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints\\Do Not Improve LLM Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{6pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{6pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{4pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{4pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{3pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{5pt plus 2pt minus 3pt}
55	\setlength{\belowdisplayskip}{5pt plus 2pt minus 3pt}
56	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\input{conclusion}
75	
76	\section*{Limitations}
77	\input{limitations_content}
78	
79	\bibliography{references}
80	
8
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-21T06:29:52.825599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-21T06:29:53.229505+00:00_

1	Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
2	We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
3	Across six open-source LLMs (7B--32B, from Mistral-7B at 54\% SC to Qwen3-14B thinking mode at 86\% SC) and three logical reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find that self-extracted constraints do not improve majority voting at any capacity level: none of sixteen non-degenerate conditions shows a significant effect after FDR control (Benjamini--Hochberg, $m{=}16$); TOST equivalence tests (margin $\pm 2$\,pp) establish equivalence for five conditions, while five show genuine SICA--SC differences---four of which are negative.
4	We identify \emph{symbolic confirmation bias} as the root cause: on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC.
5	Process-level analysis reveals a deeper bottleneck: chain-of-thought cosine similarity ($0.69$) far exceeds answer-level Fleiss' $\kappa$ ($0.46$), indicating that traces share reasoning processes even when they diverge on answers.
6	Twenty-seven same-model remediation strategies spanning fifteen families all fail, revealing a persistent independence-accuracy trade-off at the 7B--32B scale: methods that increase trace independence destroy accuracy (Debate: $\kappa = 0.15$, $-18.6$\,pp), while methods preserving accuracy cannot break the correlation floor ($\kappa \geq 0.40$ across three model families).
7	Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp and $+14.22$\,pp on FOLIO, $+11.50$\,pp ProofWriter; $p < 0.001$); same-model self-extraction captures on
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-21T06:29:53.230278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-21T06:29:54.185120+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding Effective-$K = 1.20$--$3.62$ for nominal $K = 12$: traces beyon
…[truncated 6034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-21T06:29:54.185480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-21T06:29:54.590336+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and extensions.}
5	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).
6	
7	\paragraph{Neuro-symbolic reasoning.}
8	Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} translate problems into formal logic for external provers; LINC documents ${\sim}$40\% translation errors. SatLM \citep{ye2024satlm} generates complete SAT formulations from problem descriptions and reports positive results; critically, SatLM's constraints derive from \emph{problem-level} understanding, whereas SICA extracts from \emph{reasoning traces}. Problem-level formalization avoids answer contamination; trace-level extraction inherits confirmation bias (\S\ref{sec:confirmation-bias}). Program-aided approaches \citep{gao2023pal,chen2023program,lyu2023faithful} parallel the self-extraction bottleneck. Recent extensions \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent} each introduce capabilities beyond the reasoning model. \citet{amonkar2025realitycheck} show formalization degrades with complexity; \citet{chan2026position} argue logical soundness is unreliable for neurosymbolic verification. Our oracle controls confirm the mechanism is sound ($+29.90$/$+14.22$\,pp FOLIO, $+11.50$\,pp ProofWriter); the failure localizes to self-extraction (\S\ref{sec:oracle}).
9	
10	\paragraph{Test-time compute and v
…[truncated 2513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-21T06:29:54.590858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-21T06:29:55.143681+00:00_

1	\section{Background \& Setup}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \to \infty$ \citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \citet{ladha1992correlated} and the design-effect framework of \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
11	\end{equation}
12	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. $K_{\text{eff}}$ should be interpreted as an ordinal diagnostic---ranking which conditions have genuine vote diversity---rather than as a literal effective sample size. Fleiss' $\kappa$ is a chance-corrected agreement measure, not identical to the ICC ($\rho$) in \citeauthor{kish1965survey}'s (\citeyear{kish1965survey}) original formula; we validated their monotonic relationship empirically (mean pairwise $r = 0.625$ across model families). This \emph{independence bottleneck} motivates our investigation.
13	
14	\subsection{SICA Pipeline}
15	\label{sec:pipeline}
16	
17	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
18	
19	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K
…[truncated 5161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-21T06:29:55.144074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-21T06:29:55.601013+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models, three reasoning domains, and over 3,000 condition-evaluations (${\sim}$1,250 unique instances), with diagnostic analyses of confirmation bias and process-level independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B parameters).
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline, revealing three observation-driven accuracy regimes.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all conditions sorted by SC accuracy. Results hold across the full capability range: from Mistral-7B (55.88\% SC) to Qwen3-14B thinking mode (86.27\% SC), SICA delivers no significant gain. $\Delta$ = SICA $-$ SC (pp). $^b$In-context learning with gold logical examples. $\dagger$\,$n < 100$ (suggestive only). \textbf{Bold $\Delta$}: $p < 
…[truncated 3848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-21T06:29:55.601454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-21T06:29:56.105444+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	We test the three predictions of the Symbolic Mirage hypothesis (\S\ref{sec:mirage}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$. Across four Mistral-7B seeds, $\kappa \in [0.41, 0.51]$ yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp, indicating seed-level constraint quality matters beyond independence. Positive $\Delta$ requires both sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ degrades). All four model families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3pt}
15	\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$ (uncorrected; BH adj.\ $p = 0.112$, $m{=}16$); positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each.}
16	\label{tab:independence}
17	\begin{tabular}{@{}llccrr@{}}
18	\toprule
19	Model & Condition & $\kappa$ & $K_{\text{eff}}$ & SC (\%) & $\Delta$ (pp) \\
20	\midrule
21	Qwen3 (think) & FOLIO & 0.91 & 1.09 & ${\sim}$84 & ${\sim}$0 \\
22	Qwen2.5-14B & LogiQA & 0.82 & 1.20 & 78.50 & $-$0.50 \\
23	Qwen3 & FOLIO & 0.77 & 1.26 & 84.80 & $-$0.49 \\
24	Qwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.49 & $-$0.98 \\
25	Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\
26	\addlinespace
27	Mistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\
28	Mistral-7B & LogiQA & 0.51 & 1.81 & 51.00 & $+$0.50 \\
29	Mistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\
30	Mi
…[truncated 3698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-21T06:29:56.105962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-21T06:29:56.558539+00:00_

1	\section{Cross-Architecture Proof-of-Concept}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Method.}
6	We test with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$), whose (premise, conclusion) structure suits NLI classification.
7	
8	\paragraph{Main result.}
9	DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo mode yields $+0.49$\,pp at $w{=}1$ and $+2.94$\,pp at $w{=}3$ (both n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp, raw $p = 0.014$; BH adj.\ $p = 0.112$; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). We report $w{=}3$ as primary. After BH correction ($m{=}12$), Mistral-7B $w{=}3$ (adj.\ $p = 6.78 \times 10^{-5}$) and $w{=}5$ (adj.\ $p = 7.41 \times 10^{-6}$) remain significant; all other conditions are non-significant.
10	
11	\paragraph{Why it works.}
12	Encoder-only DeBERTa (406M) and decoder-only Mistral (7B) share no architecture or training data, satisfying the independence condition that same-model sampling cannot provide (\S\ref{sec:mirage}). Per-label complementarity emerges: NLI excels on \textsc{False} (71.43\% vs.\ SC's 38.10\%), SC dominates \textsc{Unknown} (68.12\% vs.\ 18.84\%). All three NLI architectures tested produce significant gains at $w \geq 3$ (Appendix~\ref{app:multi-nli}).
13	
14	\paragraph{Capability gap hypothesis.}
15	We evaluate four generators from three model families spanning a 46-point SC 
…[truncated 3539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-21T06:29:56.559049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-21T06:29:57.112217+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Self-verification generalization.}
5	The Symbolic Mirage operates through two channels: correlated constraints compress $K_{\text{eff}} < 2$ (\emph{direct}), while answer-coupled constraints collapse MAX-SAT to vote counting (\emph{indirect}; Eq.~\ref{eq:degenerate}). \citet{huang2024selfcorrect} and \citet{stechly2025selfverification} observe that LLMs cannot self-correct without external feedback; our bias ratio ($4.97\times$ Mistral, $3.93\times$ Qwen, $2.88\times$ LLaMA) quantifies why: extraction and generation share the same distributional biases. $\text{BR} > 1$ across three families predicts that any self-verification pipeline deriving criteria from the same model faces this bottleneck, whether formal constraints, natural-language critiques, or code assertions.
6	
7	\paragraph{Test-time scaling and ensemble diversity.}
8	$K_{\text{eff}} = 1.20$--$3.62$ for nominal $K = 12$ means sampling beyond a dozen traces yields diminishing independent information, and the pattern intensifies with capability: Qwen3 thinking mode ($\kappa = 0.91$, $K_{\text{eff}} = 1.09$) produces near-deterministic traces, creating a scaling paradox for o1/R1-style reasoning models \citep{guo2025deepseekr1}. The $\kappa$ floor is universal---all non-destructive interventions cluster at $\kappa \geq 0.40$ (Table~\ref{tab:kappa_generalization}), confirming a structural ceiling. This instantiates the classic ensemble tension \citep{krogh1994neural, brown2005diversity}: Debate raises $K_{\text{eff}}$ from ${\sim}1.8$ to ${\sim}4.5$ but collapses accuracy ($-18.6$\,pp, $p < 0.001$), because diversity-inducing perturbations degrade predictions rather than introducing independent reasoning. Cross-architecture escape succeeds (Spearman $\rho = 1.0$, $p = 0.003$, $n{=}6$) precisely because encoder-only DeBERTa and decoder-only LLMs have structurally different error profiles. If traces do not faithfully reflect reasoning \citep{turpin
…[truncated 924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-21T06:29:57.113199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 933 · 2026-05-21T06:29:58.017931+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We identify the Symbolic Mirage: self-extracted constraints inherit the generating model's biases ($\text{BR} = 4.97\times$, 83.3\%), explaining why twenty-seven remediation strategies fail. Oracle controls ($+29.90$/$+14.22$\,pp) confirm the mechanism is sound; the bottleneck is extraction quality, not the formal channel. Three diagnostics predict failure ($C_0 < 5\%$, SC $\leq 40\%$, process similarity). Cross-architecture NLI escapes the mirage when the verifier exceeds the generator ($\rho = 1.0$, $p = 0.003$); DRC recovers 90\% of this gain at 39\% cost.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 934 · 2026-05-21T06:29:58.068568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
  }
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-21T06:29:58.470732+00:00_

1	\paragraph{Scale and language.}
2	All models range from 7B to 32B parameters; whether the independence bottleneck persists at larger scales (70B+) or with reasoning-specialized models is untested. All datasets are English-language logical reasoning benchmarks with discrete answer spaces. We do not evaluate trained symbolic extractors, external solvers with verified grounding, or multilingual settings. Oracle analysis is limited to FOLIO and ProofWriter (gold annotations available); extending to commonsense reasoning requires constructing comparable gold constraint sets. The cross-architecture NLI verifier (\S\ref{sec:cross-arch}) provides no benefit on LogiQA (combo $\Delta \leq +1$\,pp, all $p > 0.5$), indicating that cross-architecture escape requires task-verifier alignment---NLI is effective only when the task naturally decomposes into premise-conclusion entailment. Even on compatible tasks, NLI gain vanishes when the capability gap is large (Qwen3-14B ProofWriter: SC 85.83\% vs.\ DeBERTa 55\%, gap $= -30.83$\,pp, $\Delta \leq +0.50$\,pp, n.s.), and moderate negative gaps yield small, non-significant gains (LLaMA-3.1-8B: gap $= -17.50$\,pp, $+0.83$\,pp, n.s.; \S\ref{sec:cross-arch}). Scaling the cross-architecture approach---via trained verifiers, code-based symbolic execution, or multi-verifier ensembles---remains unexplored and may extend the escape to stronger generators and broader task types.
3	
4	\paragraph{Statistical power.}
5	The per-label complementarity analysis of the cross-architecture NLI result (\S\ref{sec:cross-arch}) involves small cell sizes (e.g., 42 \textsc{False} problems, 69 \textsc{Unknown} problems); per-label McNemar tests would be underpowered. The bias ratio metric ($4.97\times$) was initially computed on a single condition (Mistral-7B FOLIO, $n = 204$); cross-model replication (Table~\ref{tab:cross-model-bias}) confirms the pattern but is limited to FOLIO. Four-seed replication shows 2 of 4 seeds yielding null or negative results, a
…[truncated 1297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-21T06:29:58.471180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 937 · 2026-05-21T06:29:58.974582+00:00_

1	
2	\section{Regime Scatter Plot}
3	\label{app:regime-scatter}
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\columnwidth]{f2_regime_scatter}
8	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--55\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.112$).}
9	\label{fig:regime-scatter}
10	\end{figure}
11	
12	\section{Prompt Templates}
13	\label{app:prompts}
14	
15	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
16	
17	\paragraph{System Prompt.}
18	
19	\begin{lstlisting}
20	You are a constraint extraction tool. Output ONLY
21	valid JSON. Do NOT solve problems, reason about
22	correctness, or think step-by-step. Extract
23	constraints from the given trace exactly as stated.
24	\end{lstlisting}
25	
26	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
27	
28	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
29	
30	\begin{lstlisting}
31	Extract mathematical constraints from this reasoning
32	trace as a JSON object.
33	
34	Rules:
35	- type: "equation", "inequality", or "predicate"
36	- expression: human-readable, e.g. "x + y == 14"
37	- z3_formula: a single comparison expression in
38	  Python Z3 syntax
39	- source_step: step number where the constraint
40	  appears
41	- Use variable names from the trace
42	
43	z3_formula MUST follow these rules:
44	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
45	  /, **, %
46	- Use individual named varia
…[truncated 57650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 938 · 2026-05-21T06:29:58.975095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-21T06:29:59.929824+00:00_

1	% References for SICA paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% SAT-Based Reasoning %%%
5	
6	@inproceedings{ye2024satlm,
7	  title={SatLM: Satisfiability-Aided Language Models Using Declarative Prompting},
8	  author={Ye, Xi and Chen, Qiaochu and Dillig, Isil and Durrett, Greg},
9	  booktitle={Advances in Neural Information Processing Systems},
10	  volume={36},
11	  year={2024}
12	}
13	
14	%%% Program-Aided Reasoning %%%
15	
16	@inproceedings{gao2023pal,
17	  title={{PAL}: Program-aided Language Models},
18	  author={Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham},
19	  booktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},
20	  year={2023}
21	}
22	
23	@article{chen2023program,
24	  title={Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks},
25	  author={Chen, Wenhu and Ma, Xueguang and Wang, Xinyi and Cohen, William W.},
26	  journal={Transactions on Machine Learning Research},
27	  year={2023}
28	}
29	
30	@inproceedings{lyu2023faithful,
31	  title={Faithful Chain-of-Thought Reasoning},
32	  author={Lyu, Qing and Havaldar, Shreya and Stein, Adam and Zhang, Li and Rao, Delip and Wong, Eric and Apidianaki, Marianna and Callison-Burch, Chris},
33	  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
34	  year={2023}
35	}
36	
37	%%% Theoretical Foundations %%%
38	
39	@book{condorcet1785,
40	  title={Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
41	  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},
42	  year={1785},
43	  publisher={Imprimerie Royale},
44	  address={Paris}
45	}
46	
47	@article{austensmith1996,
48	  title={Information Aggregation, Rationality
…[truncated 16462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-21T06:29:59.930311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 941 · 2026-05-21T06:30:00.282346+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 942 · 2026-05-21T06:30:05.766371+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found several results related to EMNLP 2026, though the search did not return a dedicated main conference call for papers wit
…[truncated 1276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5836
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-21T06:30:05.766974+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5484
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-21T06:30:12.453127+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers ARR submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers ARR submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 945 · 2026-05-21T06:30:12.957330+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"
  }
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-21T06:30:14.313098+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-21T06:30:14.363747+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 948 · 2026-05-21T06:30:18.896009+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers ARR submission deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here is the information about EMNLP 2026 main conference call for papers and ARR submission deadline:

## Key Information:

The ARR submission deadline for EMNLP 2026
…[truncated 932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6442
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-21T06:30:19.500240+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission guidelines regarding page limits and anonymity policy:

## Page Limit

The page limit is 4 pages for short papers and 8 pages for long papers, excluding the ethical considerations and limitations sections. Submissions that exceed the length requirements, or are missing a limitations section, will be desk rejected.

## Anonymity Pol
…[truncated 849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6542
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-21T06:30:24.899676+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits for long/short papers, template requirements, anonymity rules, appendix rules, reference format, and any other formatting requirements. Also extract all important dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits for long/short papers, template requirements, anonymity rules, appendix rules, reference format, and any other formatting requirements. Also extract all important dates."
  }
}
```

</details>

---


### Tool call

_source line 951 · 2026-05-21T06:30:26.241838+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/cfp",
  "prompt": "Extract the detailed submission guidelines: page limits for long and short papers, template requirements, anonymity policy, appendix rules, citation format, ethical considerations section requirements, limitations section requirements, and responsible NLP checklist requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/cfp",
    "prompt": "Extract the detailed submission guidelines: page limits for long and short papers, template requirements, anonymity policy, appendix rules, citation format, ethical considerations section requirements, limitations section requirements, and responsible NLP checklist requirements."
  }
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-21T06:30:26.577800+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/agent/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/agent/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-21T06:30:26.704769+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 126
}
```

</details>

---


### Tool result

_source line 954 · 2026-05-21T06:30:30.273151+00:00_

# EMNLP 2026 Submission Guidelines & Important Dates

## Page Limits
- **Long Papers:** 8 pages (9 pages in camera-ready version)
- **Short Papers:** 4 pages (5 pages in camera-ready version)

## Anonymity Requirements
- Double-blind review process maintained
- "Reviewers will not see authors, nor will authors see reviewers"
- Reviews remain confidential on ARR platform
- Authors may optionally make anonymized submissions publicly visible

## Formatting & Templates
- Must follow "all of the ARR submission requirements"
- Specific template requirements are linked to the ARR CFP rather than detailed here
- Two-way anonymized review instructions apply

## Additional Submission Requirements
The page covers: authorship rules, citation/comparison standards, ethics policies, limitations sections, writing assistance permissions, and optional supplementary materials policies—all referencing ARR guidelines.

## Critical Important Dates
| Milestone | Date |
|-----------|------|
| ARR Submission Deadline | May 25, 2026 |
| Reviewer Registration Deadline | May 27, 2026 |
| Author Response Period | July 7-13, 2026 |
| Meta Reviews Released | July 30, 2026 |
| EMNLP Commitment Deadline | August 2, 2026 |
| Acceptance Notification | August 20, 2026 |
| Camera-Ready Due | September 20, 2026 |
| Conference Dates | October 24-29, 2026 |

**Note:** "All deadlines are 11:59PM UTC-12:00 ('anywhere on Earth')."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 5373
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-21T06:30:33.588349+00:00_

# ACL Rolling Review Submission Guidelines Summary

## Page Limits

**Long Papers:** Up to 8 pages of content plus unlimited references and supplementary sections (limitations and ethical considerations sections don't count toward limits)

**Short Papers:** Up to 4 pages of content plus unlimited references and supplementary sections

## Template Requirements

Submissions must "follow the [ACL Author Guidelines]" and use "the official ACL style template." Authors cannot modify style files or use templates from other conferences. Submissions violating format requirements (page size, margins, fonts) face rejection without review.

## Anonymity Policy

Papers must exclude author names and affiliations. Self-references revealing identity (e.g., "We previously showed") must be reworded to third-person citations. Supplementary materials require anonymization; file-sharing services like Dropbox that track downloads are prohibited.

## Appendix Rules

Appendices follow main content after references and don't count toward page limits. They must be in double-column format (with specified exceptions). Critical contributions, technical details necessary for assessing novelty, or material that circumvents page counts should appear in the main paper, not appendices. Reviewers aren't obligated to review appendix content.

## Citation Format

For concurrently submitted related papers by overlapping authors: "Anonymous (2026). Paper title. Under review." Authors must cite all relevant refereed publications, though aren't obligated to know all unpublished work.

## Ethical Considerations Section

An optional section titled "Ethical considerations" may be included after conclusions without counting toward page limits. Authors must complete the Responsible NLP Checklist and may discuss broader ethical impacts.

## Limitations Section (Required)

A mandatory "Limitations" section must appear before references without counting toward limits. It discusses only the work's constraints—not n
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 7346
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-21T06:30:36.956243+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-21T06:30:37.309620+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/review_director_9c155b71.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-21T06:30:37.310076+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-21T06:30:37.410804+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-21T06:30:40.074860+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-21T06:30:40.126182+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516
…[truncated 9549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-21T06:30:44.145533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-21T06:30:44.346923+00:00_

1	_next_id: 2
2	constraints:
3	- id: C001
4	  added: 2026-05-18 17:54 UTC
5	  summary: 所有实验代码写完后必须先 dry-run 验证（python 可用性、路径存在性、端口无冲突、数据文件存在）再正式部署运行
6	  scope: worker
7	  reason: 多次出现代码部署后才发现 python command not found、模型路径不存在、GPU/端口冲突等低级错误，浪费 GPU 时间和调试周期。用户明确要求。
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-21T06:30:44.447778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-21T06:30:44.750741+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 28072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-21T06:30:51.502139+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-21T06:30:52.406943+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_6.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-21T06:30:52.558075+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project_config.yaml\" 2>/dev/null",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 2 -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project_config.yaml\" 2>/dev/null",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-21T06:30:52.759682+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-21T06:30:56.695791+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 3 -name \"*.yaml\" | grep -i config 2>/dev/null; find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"config*.yaml\" 2>/dev/null",
  "description": "Search for config files in broader scope"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -maxdepth 3 -name \"*.yaml\" | grep -i config 2>/dev/null; find /home/ubuntu/agent-ml-research -maxdepth 3 -name \"config*.yaml\" 2>/dev/null",
    "description": "Search for config files in broader scope"
  }
}
```

</details>

---


### Tool result

_source line 971 · 2026-05-21T06:30:56.804859+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/cross_representation_disagreement_diagno.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/resources.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 109
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-21T06:30:59.935205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/projects/symb_invariant_consensus.yaml"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-21T06:30:59.985861+00:00_

1	execution:
2	  gpu_constraint: westd-25068:cuda:0,cuda:1,cuda:2,cuda:3
3	  gpu_ids:
4	  - westd-25068:cuda:0
5	  - westd-25068:cuda:1
6	  - westd-25068:cuda:2
7	  - westd-25068:cuda:3
8	  - westd-16639:cuda:0
9	  - westd-16639:cuda:1
10	  - westd-16639:cuda:2
11	  - westd-16639:cuda:3
12	  project_path: /root/symb_invariant_consensus
13	  servers:
14	  - westd-25068
15	  - westd-16639
16	feishu:
17	  chat_id: oc_970d5ea3f54df81296b97321fcded892
18	  operational_chat_id: oc_319977a04ca60b6c4c69a2a8d4141a75
19	  review_mode: fresh
20	  review_paper_path: projects/symb_invariant_consensus/docs/paper/main.tex
21	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf
22	  review_round: 7
23	  review_supplementary_paths: ''
24	  submission_chat_id: oc_c338e034cbffa10b9cc723e731d288d8
25	project:
26	  created_at: '2026-05-15T08:44:44.820Z'
27	  description: Formally-Verified Intermediate Constraint Consensus Across Reasoning
28	    Paths
29	  name: symb_invariant_consensus
30	  phase: research
31	  source_idea_id: idea_013
32	venue: emnlp-2026
33	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 974 · 2026-05-21T06:31:00.040095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-21T06:31:00.091351+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing: []
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 976 · 2026-05-21T06:31:24.020049+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:dispatch_visual_check,director_post_to_reviewer",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:dispatch_visual_check,director_post_to_reviewer",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 977 · 2026-05-21T06:31:24.070795+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-21T06:31:26.744187+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "visual check dispatch reviewer post",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "visual check dispatch reviewer post",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-21T06:31:26.795075+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-21T06:31:40.625931+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-21T06:32:09.651272+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 29025
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-21T06:32:09.802261+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题：*Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*\n- 论文路径：`projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n- 目标 venue：**EMNLP 2026**（via ACL Rolling Review）\n- 投稿类别：Long Paper\n- ARR 提交截止：2026-05-25\n\n## Venue 格式要求\n- 正文 **8 页**，参考文献不限页数\n- 必须包含 **Limitations** section（不计页数）\n- 可选 Ethical Considerations section（不计页数）\n- **Double-blind** 匿名审稿（ACL 模板，`\\usepackage[review]{acl}`）\n- 附录不计页数，审稿人无义务阅读（但可参考）\n- ARR Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 统计方法严谨性\n- SICA vs SC 的 McNemar 检验是否正确使用？多重比较校正（BH, m=16）是否恰当？\n- TOST 等价检验的 margin (±2pp) 是否合理？\n- 四种子复制是否足以支持结论？\n- Bootstrap CI 方法是否恰当？\n- Fleiss' κ → Effective-K 的映射（Eq.1）是否有充分理论依据？κ 不等于 ICC，这个近似是否被充分讨论？\n- Bias Ratio（Eq.3）的统计性质是否被讨论？\n- Spearman ρ=1.0 (n=6) 的 exact permutation test 是否可靠（6个点）？\n\n### 2. 实验设计充分性\n- 6 个模型（7B-32B）是否覆盖了足够的 capability range？缺少 70B+ 是否是致命缺陷？\n- 3 个 logical reasoning 数据集 + StrategyQA/GSM8K/AIME 是否足够？\n- 27 种 remediation 策略的分类和覆盖是否系统？\n- Oracle 实验设计是否充分验证了 mechanism soundness？\n- Cross-architecture NLI PoC：单一 verifier 类型（NLI）、单一有效 generator（Mistral-7B）是否限制了结论的普适性？\n- DRC (Disagreement-Routed Cascade) 是否有 held-out 评估？τ 阈值选择是否在测试集上？\n- K=12, T=0.7, T_ext=0.3 等超参是否有充分的 sensitivity analysis？\n\n### 3. 可重复性\n- 实验细节是否充分（prompt 模板、Z3 配置、计算资源等）？\n- 数据集处理、评估代码是否承诺开源？\n- 随机种子控制是否充分？\n\n### 4. 页面合规\n- 正文是否在 8 页内？\n- Limitations section 是否存在且内容充分？\n- 匿名性是否完好（无作者信息泄露）？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (Critical/Warning/Info) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## 论文信息\n- 标题：*Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*\n- 论文路径：`projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n- 目标 venue：**EMNLP 2026**（via ACL Rolling Review）\n- 投稿类别：Long Paper\n- ARR 提交截止：2026-05-25\n\n## Venue 格式要求\n- 正文 **8 页**，参考文献不限页数\n- 必须包含 **Limitations** section（不计页数）\n- 可选 Ethical Considerations section（不计页数）\n- **Double-blind** 匿名审稿（ACL 模板，`\\usepackage[review]{acl}`）\n- 附录不计页数，审稿人无义务阅读（但可参考）\n- ARR Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 统计方法严谨性\n- SICA vs SC 的 McNemar 检验是否正确使用？多重比较校正（BH, m=16）是否恰当？\n- TOST 等价检验的 margin (±2pp) 是否合理？\n- 四种子复制是否足以支持结论？\n- Bootstrap CI 方法是否恰当？\n- Fleiss' κ → Effective-K 的映射（Eq.1）是否有充分理论依据？κ 不等于 ICC，这个近似是否被充分讨论？\n- Bias Ratio（Eq.3）的统计性质是否被讨论？\n- Spearman ρ=1.0 (n=6) 的 exact permutation test 是否可靠（6个点）？\n\n### 2. 实验设计充分性\n- 6 个模型（7B-32B）是否覆盖了足够的 capability range？缺少 70B+ 是否是致命缺陷？\n- 3 个 logical reasoning 数据集 + StrategyQA/GSM8K/AIME 是否足够？\n- 27 种 remediation 策略的分类和覆盖是否系统？\n- Oracle 实验设计是否充分验证了 mechanism soundness？\n- Cross-architecture NLI PoC：单一 verifier 类型（NLI）、单一有效 generator（Mistral-7B）是否限制了结论的普适性？\n- DRC (Disagreement-Routed Cascade) 是否有 held-out 评估？τ 阈值选择是否在测试集上？\n- K=12, T=0.7, T_ext=0.3 等超参是否有充分的 sensitivity analysis？\n\n### 3. 可重复性\n- 实验细节是否充分（prompt 模板、Z3 配置、计算资源等）？\n- 数据集处理、评估代码是否承诺开源？\n- 随机种子控制是否充分？\n\n### 4. 页面合规\n- 正文是否在 8 页内？\n- Limitations section 是否存在且内容充分？\n- 匿名性是否完好（无作者信息泄露）？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (Critical/Warning/Info) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 983 · 2026-05-21T06:32:33.330319+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23528
}
```

</details>

---


### Tool call

_source line 984 · 2026-05-21T06:32:33.481621+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 叙事质量**。\n\n## 论文信息\n- 标题：*Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*\n- 论文路径：`projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n- 目标 venue：**EMNLP 2026**（via ACL Rolling Review）\n- 投稿类别：Long Paper\n- ARR 提交截止：2026-05-25\n\n## Venue 格式要求\n- 正文 **8 页**，参考文献不限页数\n- 必须包含 **Limitations** section（不计页数）\n- 可选 Ethical Considerations section（不计页数）\n- **Double-blind** 匿名审稿（ACL 模板，`\\usepackage[review]{acl}`）\n- 附录不计页数，审稿人无义务阅读（但可参考）\n- ARR Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估（核心审查项）\n- 本文的核心发现——\"自提取约束继承模型偏差\"——相对于 Huang et al. (ICLR 2024, \"LLMs cannot self-correct reasoning yet\") 和 Stechly et al. (ICLR 2025, self-verification limitations) 有多大增量新颖性？\n- \"Symbolic Confirmation Bias\" 是否是一个真正新的 insight，还是已知 self-correction failure 在符号约束领域的直接 instantiation？\n- 定量诊断工具（Effective-K, Bias Ratio, Process-κ）是否构成方法论贡献？还是已有指标的直接应用？\n- Independence-Accuracy Trade-off 是否是 bias-variance tradeoff 的重述？\n- 27 种 remediation 策略的穷举是否足以提升论文的贡献层级？\n- Cross-architecture escape（DeBERTa NLI）和 DRC 是否足够作为 constructive contribution？\n\n### 2. Related Work 覆盖\n- 搜索是否遗漏了关键相关工作？特别关注：\n  - SatLM (Ye et al., NeurIPS 2023)：同样使用 LLM+SAT solver 但报告正面结果——与本文负面结果的区别是否被讨论？\n  - VeriCoT (Zhu et al., 2025)：将 CoT 形式化为 FOL 的验证方法\n  - CRITIC (Gou et al., ICLR 2024)：tool-interactive self-correction\n  - 其他 2025-2026 neuro-symbolic reasoning 工作\n- Related Work 的组织是否清晰？是否正确定位了本文在文献中的位置？\n\n### 3. 叙事结构与写作质量\n- Abstract 是否准确反映了论文的贡献和发现？是否有过度声称？\n- Introduction 的动机链（CJT → independence failure → symbolic mirage）是否流畅？\n- 四个 contributions 的排序是否合理？哪个应作为第一贡献？\n- Discussion 是否充分讨论了 implications？\n- Conclusion 是否仓促？\n- \"Symbolic Mirage\"、\"Symbolic Confirmation Bias\"、\"capability trap\" 等术语是否过度品牌化？\n- 论文整体叙事是否清晰：负面结果 → 机制解释 → constructive escape？\n\n### 4. 负面结果论文的 venue fit\n- 作为 EMNLP 2026 投稿，这篇负面结果论文是否符合 *ACL venues 的偏好？\n- 负面结果是否提供了足够的 actionable insights（诊断工具、cross-arch escape）？\n- 论文的目标读者是谁？他们能从中学到什么？\n\n### 5. 格式与合规\n- 正文是否在 8 页内？\n- 匿名性是否完好？\n- 引用格式是否符合 ACL 标准？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (Critical/Warning/Info) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 叙事质量**。\n\n## 论文信息\n- 标题：*Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*\n- 论文路径：`projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf`\n- 目标 venue：**EMNLP 2026**（via ACL Rolling Review）\n- 投稿类别：Long Paper\n- ARR 提交截止：2026-05-25\n\n## Venue 格式要求\n- 正文 **8 页**，参考文献不限页数\n- 必须包含 **Limitations** section（不计页数）\n- 可选 Ethical Considerations section（不计页数）\n- **Double-blind** 匿名审稿（ACL 模板，`\\usepackage[review]{acl}`）\n- 附录不计页数，审稿人无义务阅读（但可参考）\n- ARR Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查侧重\n\n### 1. 新颖性评估（核心审查项）\n- 本文的核心发现——\"自提取约束继承模型偏差\"——相对于 Huang et al. (ICLR 2024, \"LLMs cannot self-correct reasoning yet\") 和 Stechly et al. (ICLR 2025, self-verification limitations) 有多大增量新颖性？\n- \"Symbolic Confirmation Bias\" 是否是一个真正新的 insight，还是已知 self-correction failure 在符号约束领域的直接 instantiation？\n- 定量诊断工具（Effective-K, Bias Ratio, Process-κ）是否构成方法论贡献？还是已有指标的直接应用？\n- Independence-Accuracy Trade-off 是否是 bias-variance tradeoff 的重述？\n- 27 种 remediation 策略的穷举是否足以提升论文的贡献层级？\n- Cross-architecture escape（DeBERTa NLI）和 DRC 是否足够作为 constructive contribution？\n\n### 2. Related Work 覆盖\n- 搜索是否遗漏了关键相关工作？特别关注：\n  - SatLM (Ye et al., NeurIPS 2023)：同样使用 LLM+SAT solver 但报告正面结果——与本文负面结果的区别是否被讨论？\n  - VeriCoT (Zhu et al., 2025)：将 CoT 形式化为 FOL 的验证方法\n  - CRITIC (Gou et al., ICLR 2024)：tool-interactive self-correction\n  - 其他 2025-2026 neuro-symbolic reasoning 工作\n- Related Work 的组织是否清晰？是否正确定位了本文在文献中的位置？\n\n### 3. 叙事结构与写作质量\n- Abstract 是否准确反映了论文的贡献和发现？是否有过度声称？\n- Introduction 的动机链（CJT → independence failure → symbolic mirage）是否流畅？\n- 四个 contributions 的排序是否合理？哪个应作为第一贡献？\n- Discussion 是否充分讨论了 implications？\n- Conclusion 是否仓促？\n- \"Symbolic Mirage\"、\"Symbolic Confirmation Bias\"、\"capability trap\" 等术语是否过度品牌化？\n- 论文整体叙事是否清晰：负面结果 → 机制解释 → constructive escape？\n\n### 4. 负面结果论文的 venue fit\n- 作为 EMNLP 2026 投稿，这篇负面结果论文是否符合 *ACL venues 的偏好？\n- 负面结果是否提供了足够的 actionable insights（诊断工具、cross-arch escape）？\n- 论文的目标读者是谁？他们能从中学到什么？\n\n### 5. 格式与合规\n- 正文是否在 8 页内？\n- 匿名性是否完好？\n- 引用格式是否符合 ACL 标准？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses (Critical/Warning/Info) → Questions → Missing References → Overall Assessment (评分 + 置信度)。"
  }
}
```

</details>

---


### Tool result

_source line 985 · 2026-05-21T06:32:35.211750+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1730
}
```

</details>

---


### Tool call

_source line 986 · 2026-05-21T06:32:50.956761+00:00_

called CronCreate

<details open><summary>🔧 Tool call — CronCreate</summary>

```json
{
  "cron": "*/3 * * * *",
  "prompt": "检查 Reviewer 1 和 Reviewer 2 的审稿进度。如果两位都完成了，进入交叉分享阶段（Step 2）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "CronCreate",
  "tool_args": {
    "cron": "*/3 * * * *",
    "prompt": "检查 Reviewer 1 和 Reviewer 2 的审稿进度。如果两位都完成了，进入交叉分享阶段（Step 2）。"
  }
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-21T06:32:51.007481+00:00_

Scheduled recurring job a85199ed (Every 3 minutes). Session-only (not written to disk, dies when Claude exits). Auto-expires after 7 days. Use CronDelete to cancel sooner.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "CronCreate",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 988 · 2026-05-21T06:32:53.944752+00:00_

Round 1 审稿任务已分配，等待 Reviewer 返回结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 60

## Round 60

2 recorded events


### User

_source line 989 · 2026-05-21T06:39:26.885322+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文**: *Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*
**Venue**: EMNLP 2026 (via ACL Rolling Review)

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 一篇严谨的负面结果论文，实验覆盖面广、统计处理到位，但理论框架有缺口，建设性贡献（跨架构逃逸 + DRC）的适用范围过窄，削弱了整体影响力。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心负面结论有充分实验支撑；但 Proposition 1 无证明、κ→K_eff 映射理论基础弱、Spearman ρ=1.0 基于 n=6 |
| Excitement | 3.5/5 | 对 self-verification 领域有警示价值，27 种补救策略的穷举有说服力；但建设性贡献仅适用于窄场景 |
| Reproducibility | 4/5 | Prompt 模板、算法伪代码、超参均完整给出；代码承诺开源但尚未可验证 |
| Confidence | 4/5 | 本人熟悉 SC、neurosymbolic reasoning、统计检验方法，仔细阅读了正文及全部附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Proposition 1（Self-Extraction Ceiling）缺少证明**
- 具体位置：Section 3.3, Eq. 附近的 Proposition 1
- 问题：Proposition 1 声称 $\Delta_\text{max}^\text{self} \lesssim \Delta_\text{oracle} / \text{BR}(M)$，但全文未提供任何证明或推导。符号 "≲" 本身不精确——它是严格上界、渐近上界还是近似值？Section 3.3 底部的 "Proof sketch" 实际上是 Corollary 1 的证明，不是 Proposition 1 的。一个标注为 Proposition 的数学声明不应当无证明地给出。
- 为什么影响接收：这是 Symbolic Mirage 理论框架的核心量化结论。如果 ceiling bound 无法证明，整个理论叙事从 "有理论支撑的机制解释" 降级为 "事后描述性统计"。
- 建议修改方向：(a) 提供正式证明或至少 proof sketch，明确所需假设；(b) 将 "≲" 精确化（upper bound with explicit conditions 或 approximation with error bound）；(c) 如果无法证明，降级为 empirical observation 而非 Proposition。

**N2** [critical] **Fleiss' κ → Effective-K 映射的理论依据不足**
- 具体位置：Section 3.1, Eq. 1; Section 3.1 第二段
- 问题：Kish (1965) 的设计效应公式使用 ICC（组内相关系数），不是 Fleiss' κ。论文承认两者不同，但仅以 "mean pairwise r = 0.625 across model families" 作为经验验证。r = 0.625 只是中等相关，意味着 κ 和 ICC 之间有约 61% 的方差未被解释。然而，论文在多个关键位置（Table 2, Section 5.1, Discussion）将 K_eff 作为定量诊断指标使用，而非仅作为序数排名工具。
- 为什么影响接收：K_eff 是论文 "independence bottleneck" 论述的定量基础。如果 κ→K_eff 映射误差大，那么具体的 K_eff 值（如 1.09 vs 3.62）的可信度成疑。
- 建议修改方向：(a) 报告 ICC 本身的值并直接与 κ 对比；(b) 给出 K_eff 基于 ICC vs 基于 κ 的 sensitivity 分析；(c) 如果继续使用 κ，更加明确地限定为序数诊断而非定量度量，并在解释中反映这种不确定性。

**N3** [critical] **Spearman ρ = 1.0 (n=6) 的 capability gap 结论过于依赖极小样本**
- 具体位置：Section 6 第4段; Figure 3; Corollary 1
- 问题：capability gap 的 "perfectly monotonic" 结论基于 6 个数据点（3 NLI 架构 × 2 有效 generator 水平）。任意 6 个不重复值的排列都能产生 ρ = ±1.0——p = 0.003 虽然统计显著，但实际置信度有限。更关键的是，这 6 个点并非完全独立：3 个 NLI 架构共享相同的 Mistral-7B traces，3 个负 gap 条件共享相同的 DeBERTa verifier。
- 为什么影响接收：Corollary 1 和 capability gap hypothesis 是论文建设性贡献的核心支撑。如果这个关系不是 "perfectly monotonic" 而只是 "generally monotonic"，论文的结论表述需要调整。
- 建议修改方向：(a) 增加更多 generator-verifier 组合（如 code-based verifier、trained verifier）以扩大 n；(b) 在 n=9 的 robustness check（ρ=0.836, p=0.007）基础上承认非完美单调性；(c) 将措辞从 "perfectly monotonically" 降级为 "strongly monotonically"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **DRC 的 τ 阈值在测试集上选择，无 held-out 评估**
- 具体位置：Section 6.1, Table 4
- 问题：DRC 在 τ ∈ {0.3, 0.5, 0.7, 0.9} 上评估，所有阈值均在同一 ProofWriter 测试集（n=600）上选择。τ = 0.7 被高亮为最佳 Pareto 点（90% gain, 39% cost），但这是在测试数据上选择的。虽然 DRC 被定位为 proof-of-concept，但作为论文第 4 个正式 contribution（enumerated in Introduction），应有更严格的评估。
- 建议：(a) 在 FOLIO 或 train/dev split 上选择 τ，在 ProofWriter 上测试；(b) 或明确标注 τ 选择是 oracle 的，并讨论对实际部署的影响。

**W2** [warning] **Cross-architecture NLI escape 的适用范围极窄**
- 具体位置：Section 6; Table 3
- 问题：跨架构 NLI 仅在 Mistral-7B ProofWriter（SC 39.33%，verifier 55.00%，正 gap）上显著有效。在 FOLIO 上，combo Δ ≤ +2.94pp（n.s.）。在 LogiQA 上无效（Limitations 提到 Δ ≤ +1pp）。在 3 个较强 generator 上 ProofWriter 也无效。BH 校正后仅 2/12 条件存活。这意味着论文提出的"解决方案"仅适用于 (a) 弱 generator，(b) 任务可分解为 premise-conclusion 形式，(c) verifier 强于 generator 的场景。
- 为什么影响评分：论文花了整个 Section 6 + 大量附录在一个适用面很窄的方案上。作为 "escape" 的叙事价值有限。
- 建议：(a) 增加非 NLI verifier（如 code executor、trained verifier）以展示 escape 的一般性；(b) 或在 Discussion 中更坦诚地承认这是一个 narrow PoC 而非 general solution。

**W3** [warning] **四种子复制的方差过大，统计功效不足**
- 具体位置：Section 4.2; Table 1; Appendix E
- 问题：Mistral-7B FOLIO 的四种子复制产生 Δ ∈ {+3.43, +2.94, 0.00, −0.49}pp，标准差约 1.8pp。聚合结果 +3.43pp 在 p = 0.092 处（接近但未达显著）。只有 4 个种子，mean Δ 的 95% CI 覆盖零。更重要的是，Appendix E 的 power analysis 显示所有确认性条件的观测功效均低于 21%——这意味着即使存在 2pp 的真实效应，实验也有 >79% 的概率检测不到。
- 为什么影响评分：低统计功效的负面结果不能排除小但有意义的效应存在。论文的核心声明 "self-extracted constraints do not improve" 在统计上更准确地表述应为 "we found no evidence of improvement, but our power to detect small effects (≤2pp) was limited."
- 建议：(a) 增加种子数量（至少 10 个）或增大 n；(b) 在核心 claim 的措辞中更明确地承认 power limitation。

**W4** [warning] **TOST 等价性检验的 ±2pp margin 缺少显式理由**
- 具体位置：Section 4.2; Appendix V
- 问题：TOST 检验使用 ±2pp 作为等价性 margin，但论文未给出为什么 2pp 是合适的实际意义阈值。在 SC 文献中，有意义的改进通常在 3-10pp 范围。选 ±2pp 是偏紧的——如果选 ±3pp，更多条件会被判为等价，更支持论文结论。但反过来，如果领域认为 1pp 就有意义（如在 >90% 的高精度场景），则 ±2pp 太宽。
- 建议：添加一段讨论，引用 SC 文献中的典型改进幅度来论证 ±2pp 的合理性，或展示不同 margin (±1, ±2, ±3pp) 下的 TOST 结果 sensitivity。

**W5** [warning] **Bias Ratio 无置信区间**
- 具体位置：Section 5.2; Appendix P
- 问题：BR 值（4.97×, 3.93×, 2.88×）作为 confirmation bias 的核心度量，是在各模型的 FOLIO 错误子集上估算的比率。但论文未报告 BR 的置信区间或标准误。作为比率统计量，BR 在小样本上可能有较大方差（特别是分母——"constraints supporting correct answer on error problems"——可能较小）。
- 建议：报告 bootstrap CI for BR，或至少报告用于计算 BR 的分子分母样本量。

---

## 小问题（不影响接收）

- **Abstract 过长**：Abstract 约 250 词，信息密度高但偏长。对于 Long Paper 可接受，但可适当精简。
- **Table 1 脚注复杂**：表 1 的脚注系统（b, †, 4s, *, ***）较为复杂，需要反复查看才能理解每个条件的性质。建议简化或将探索性条件移到附录。
- **Figure 2 可读性**：Figure 2（27 interventions summary）的灰色带 ±1pp 标注在 PDF 中较难辨识。
- **引用格式小问题**：verify_references 发现 9 个 author name 格式 mismatch（如 austen-smith vs austen‐smith, de moura vs moura），但均为工具匹配差异，不影响引用正确性。

---

## 主要优势

1. **穷举式负面结果**：27 种补救策略横跨 15 个方法族，是该领域对 self-extraction 最全面的实验评估。与只测 1-2 种变体就下结论的同类工作相比，说服力显著更强。

2. **Oracle 控制实验设计精良**：用 FOLIO gold FOL + ProofWriter DSL 替换自提取约束，在相同 MAX-SAT 管道下获得 +29.90/+14.22/+11.50pp 的增益，干净地隔离了 "约束质量" 这一瓶颈变量。这是论文方法论上最强的部分。

3. **多层次诊断体系**：answer-level κ、process-level cosine similarity、confirmation bias ratio、C₀ diagnostic、entropy decomposition 从不同角度三角验证同一结论，增强可信度。

4. **统计处理总体严谨**：McNemar exact test + BH FDR correction + TOST equivalence test + bootstrap CI + power analysis 的组合在 NLP 论文中罕见且值得肯定。

5. **Appendix 材料极为充实**：22 页附录包含完整 prompt 模板、算法伪代码、逐条件分析、subpopulation breakdown，为可重复性提供了坚实基础。

---

## 缺失引用建议

- **Khalifa et al. (2023)** "Discriminator-Guided Multi-step Reasoning with LLMs"——与 SICA 的 discriminative constraint 思路相关，可加入 Related Work 讨论 self-guided verification 的更广泛文献。
- **Yao et al. (2023)** "Tree of Thoughts"——作为另一种 test-time scaling 方法，与 SC 的对比提供了有用的 baseline context。

---

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 正文 ≤ 8 页 | ✓ 正文（Section 1-8 Conclusion）在第 8 页结束 |
| Limitations section | ✓ 存在，内容充实（涵盖 scale、language、statistical power、cost） |
| Double-blind | ✓ `\usepackage[review]{acl}`，作者 "Anonymous"，未发现身份泄露 |
| 引用完整性 | ✓ 56 条 bib 全部被引用，无孤立/缺失引用 |
| Appendix | ✓ 不计页数，审稿人无义务阅读但本轮已参考 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 990 · 2026-05-21T06:39:32.816942+00:00_

Reviewer 1 完成初审。等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 991 · 2026-05-21T06:39:36.043856+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

审稿完成。核心判断：**Overall 3.5（Borderline Conference）**。

**关键发现**：
- 3 个 Must-Fix：Proposition 1 无证明、κ→K_eff 映射理论基础弱（r=0.625 只是中等）、capability gap 结论依赖 n=6 的极小样本
- 5 个 Should-Fix：DRC 无 held-out 评估、cross-architecture escape 适用面极窄（BH 后仅 2/12 存活）、四种子方差大且统计功效 <21%、TOST margin 未论证、BR 无置信区间
- 主要优势：27 种补救策略的穷举覆盖、Oracle 控制实验设计精良、多层次诊断体系、统计处理在 NLP 论文中罕见地严谨
- 格式合规：8 页正文 ✓、Limitations ✓、匿名性 ✓、引用完整 ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 992 · 2026-05-21T06:39:43.539263+00:00_

Reviewer 1 完成，Overall 3.5。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 62

## Round 62

6 recorded events


### User

_source line 993 · 2026-05-21T06:40:23.910046+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见（Round 1）

**论文**: *Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*
**审查侧重**: 新颖性 + 完整性 + 叙事质量
**Venue**: EMNLP 2026 (via ACL Rolling Review)

---

## Paper Summary

本文研究自提取符号约束能否突破 Self-Consistency (SC) 的性能天花板。作者提出 Symbolic Invariant Consensus Aggregation (SICA)，从 CoT 推理轨迹中提取形式逻辑约束并通过加权 Partial MAX-SAT 选择答案。在 6 个模型（Qwen2.5-7B/14B, Mistral-7B, LLaMA-3.1-8B, QwQ-32B, Qwen3-14B）、5 个数据集（FOLIO, ProofWriter, LogiQA, StrategyQA, GSM8K）、3,000+ 条件评估上，自提取约束均未改善 SC。作者将机制归因为 "Symbolic Confirmation Bias"——约束继承模型的分布偏差。提出三个诊断指标（Effective-K, Bias Ratio, Process-κ），测试 27 种修复策略（均失败），并提供跨架构 NLI 验证（DeBERTa）和 Disagreement-Routed Cascade (DRC) 作为建设性解决方案。

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 一项执行扎实的负面结果研究，彻底证明自提取符号约束继承模型偏差，但核心发现相对于已有 self-correction failure 文献的增量新颖性有限。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨，多模型多数据集交叉验证充分；但 Proposition 1 和 Corollary 1 仅有非正式 proof sketch，诊断指标为已有度量的直接应用 |
| Excitement | 2.5/5 | 核心发现（自生成验证继承偏差）对熟悉 self-correction 文献的读者可预测；建设性贡献（DRC）有实用价值但范围受限 |
| Reproducibility | 4/5 | 方法描述清晰，模型/数据集/参数/prompt 均在附录中提供，承诺代码开源 |
| Confidence | 4/5 | 熟悉 SC、neuro-symbolic reasoning、self-correction 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 相对于 Huang et al. (2024) 和 Stechly et al. (2025) 的增量新颖性不足

- 具体位置：§1 Introduction (page 2), §7 Discussion (page 8)
- 问题：Huang et al. (ICLR 2024) 已证明 LLMs cannot self-correct reasoning without external feedback；Stechly et al. (ICLR 2025) 已证明 self-verification 因共享相同偏差而失败。本文的核心发现——"自提取约束继承模型偏差"——是上述结论在符号约束领域的直接实例化 (instantiation)，而非根本性新发现。论文在 §7 第一段确实承认了与这两篇工作的关系，但仅用一句话带过（"Our work extends Huang et al. and Stechly et al. from natural-language self-correction to formal symbolic extraction"），未充分论证为什么符号领域的实例化本身构成足够的新颖性。
- 为什么影响接收：在 ACL ARR 中，Excitement 维度要求论文提供 surprising 或 field-changing insights。如果审稿人认为核心发现是可预测的，则 Excitement 评分难以达到 Conference 门槛。
- 建议修改方向：(1) 在 Introduction 中更明确地论证**为什么符号约束不同于自然语言 self-correction**——具体说，neurosymbolic 社区（如 Logic-LM, SatLM, LINC）的隐含假设是"一旦形式化，推理就变得可靠"，而本文挑战的正是这个假设；(2) 将 "Symbolic Confirmation Bias" 定位为对 neurosymbolic reasoning 社区特有假设的反驳，而非对 self-correction failure 的泛化。

**N2** [critical] SatLM 正面结果与本文负面结果的对比缺失

- 具体位置：§2 Related Work (page 3), Neurosymbolic Reasoning 段落
- 问题：SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM + SAT solver，但报告了显著性能提升（在 GSM 子集上超越 program-aided LMs 23%）。本文在 §2 中仅将 SatLM 列入一串引用列表（"Logic-LM, LINC, SatLM, PAL, PoT, Faithful CoT..."），未讨论**为什么 SatLM works 而 SICA doesn't**。关键区别在于：SatLM 通过 declarative prompting 让 LLM 生成**完整的形式化规约**（整个问题的 SAT 编码），solver 在完整规约上运算；SICA 从已有推理轨迹中**事后提取**局部约束。前者是 specification-generation（问题描述 → 形式化），后者是 trace-constraint-extraction（推理过程 → 约束）。这个区别恰恰是 SICA 失败的核心原因——约束是推理轨迹的衍生物，自然继承轨迹中的偏差。
- 为什么影响接收：不讨论这个对比，读者会疑惑："同样用 solver，为什么一个 work 一个不 work？"这会削弱论文的论证完整性。
- 建议修改方向：在 §2 或 §7 中用 2-3 句话明确对比：SatLM = specification-generation（LLM 不做推理，只做形式化翻译），SICA = trace-constraint-extraction（约束从推理轨迹中提取，因而继承偏差）。这个对比反而能强化论文的核心论点。

**N3** [critical] "Symbolic Confirmation Bias" 作为术语的独立性不足

- 具体位置：§3.3 (page 4), §5.2 (page 5)
- 问题：搜索发现近期已有直接研究 CoT confirmation bias 的工作：(a) "Unveiling Confirmation Bias in Chain-of-Thought Reasoning" (arXiv:2506.12301, Jun 2025) 研究了 CoT 中的 confirmation bias；(b) "Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models" (arXiv:2604.02485, Apr 2026) 系统评估了 LLM 的 confirmation bias。本文的 "Symbolic Confirmation Bias" 概念需要与这些工作区分。此外，本文同时引用的 Amonkar et al. (2025, "Reality Check") 和 Chan et al. (2026, "Position paper") 已分别指出 LLM 形式化能力的局限性和 neurosymbolic fact-checking 中逻辑正确性不可靠。
- 为什么影响接收：如果 "Symbolic Confirmation Bias" 是已有 CoT confirmation bias 在符号领域的直接映射，则该概念的新颖性进一步降低。
- 建议修改方向：(1) 引用上述近期 confirmation bias 工作并明确区分；(2) 论证 "Symbolic Confirmation Bias" 的特殊性在于：即使约束通过了形式化验证（Z3 satisfiable），偏差仍然存在——这是自然语言 confirmation bias 研究未覆盖的场景。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Independence-Accuracy Trade-off 是 bias-variance tradeoff 的重述

- 具体位置：§5.3 (page 6), Contribution 2 (page 2)
- 问题：论文将 "提高温度/多样性以增加独立性会降低准确率" 描述为一个新发现（Contribution 2: "Independence-Accuracy Trade-Off"）。但这本质上是 LLM 采样中众所周知的现象——高温度增加多样性但降低质量。在 ensemble learning 文献中，bias-variance-covariance decomposition (Krogh and Vedelsby, 1994, 论文自己引用) 早已描述了类似权衡。将这个观察提升为一个独立的 contribution 显得过度声称。
- 建议：将其定位为实验观察（"we empirically confirm..."）而非独立贡献，或提供超越已知 bias-variance tradeoff 的定量分析。

**W2** [warning] Related Work 过度压缩，缺乏深度讨论

- 具体位置：§2 (page 3)
- 问题：三段 Related Work 中列举了约 25 篇论文，阅读体验像引用列表而非文献讨论。第二段 Neurosymbolic Reasoning 将 Logic-LM、LINC、SatLM、PAL、PoT 等方法论差异巨大的系统放在同一引用串中，未区分 (a) specification-generation (SatLM, Logic-LM), (b) program-generation (PAL, PoT), (c) trace-constraint-extraction (本文 SICA)。第三段 Test-Time Scaling 和 Self-Correction 也类似处理。
- 建议：为 neurosymbolic reasoning 子段增加一个分类讨论（哪些系统是 specification-generation，哪些是 post-hoc verification），明确本文在分类中的位置。

**W3** [warning] Proposition 1 和 Corollary 1 的形式化程度不足

- 具体位置：§3.3 (page 4-5)
- 问题：Proposition 1（Self-Extraction Ceiling）和 Corollary 1（Capability Gap Condition）以定理形式呈现，但 proof sketch 仅有 3 行（page 5 顶部）。对于使用形式化 proposition 的论文，证明应更严谨。特别是 Proposition 1 的条件 "BR(M) > 1 and oracle improvement"——"oracle improvement" 的定义并不形式化。Corollary 1 声称 combo gain "monotonically increases in the capability gap"，但未给出 monotonicity 的严格证明。
- 建议：要么提供完整证明（可放在 Appendix），要么将 Proposition/Corollary 降级为 "Empirical Claim" 或 "Observation" 以匹配论证的形式化程度。

**W4** [warning] 27 种修复策略在正文中展示不足

- 具体位置：§5.4 (page 6), Figure 2 (page 7)
- 问题：27 种策略是论文的重要支撑论据（"全部失败"强化负面结果），但正文仅用 5 行文字概述（§5.4），细节全部在 Appendix K。Figure 2 展示了 27 个点的散点图，但策略名称在图中不可读。作为核心论证的关键环节，这部分在正文中的处理过于简略。
- 建议：在正文中至少增加一个段落，按类别讨论几个代表性策略的失败原因（例如：prompt-level 为什么不行？model-level 为什么不行？），而非仅在图例中列出。

**W5** [warning] Cross-architecture NLI escape 的适用范围有限

- 具体位置：§6 (page 7-8), Limitations (page 9)
- 问题：DeBERTa NLI escape 仅在 FOLIO 和 ProofWriter 上有效——这两个数据集都有 gold logical annotations，NLI 可以直接比对前提-结论关系。Limitations 明确承认 "cross-architecture NLI verifier (§6) provides no benefit on LogiQA"（page 9）。这意味着 DRC 的实用性局限于具有清晰逻辑结构的任务。
- 建议：在 §6 或 §7 中更明确地讨论 NLI escape 的适用条件（什么样的任务结构下有效），避免读者产生过度泛化的期望。

---

## 小问题（不影响接收）

- Table 1 信息密度极高（~30 行 × 8 列），可读性较差。建议拆分为两个表或使用 highlight 标注关键结果。
- "Symbolic Mirage" 作为术语在 §3.3 标题中引入后极少复用（正文中大部分使用 "Symbolic Confirmation Bias"）。建议统一术语或解释两者的层次关系（Mirage = phenomenon, Confirmation Bias = mechanism）。
- Figure 1 的 caption 可以更详细地解释红色虚线框的含义。
- §5.1 的标题 "Condorcet Effective-K" 中 K 与后文 κ (kappa) 容易混淆，建议用不同符号或在首次出现时明确区分。
- Page 4, Equation (2): MAX-SAT 公式的权重 $w_{ij}$ 定义中 "equal to the number of source traces" 可以用数学符号更精确地表达。
- Appendix 数量庞大（A-Z 共 22 个 appendix section），整体组织可优化。

---

## 主要优势

1. **实验规模与严谨性出色**：6 个模型 × 5 个数据集 × 3,000+ 条件评估，含 4-seed replication、McNemar 检验、TOST 等价性检验——这种严谨程度在负面结果论文中罕见。
2. **CJT 理论框架的引入有启发性**：用 Condorcet Jury Theorem 的独立性条件来分析 SC 的失败模式，为理解 LLM 采样的局限性提供了一个清晰的理论透镜。
3. **建设性贡献缓解了纯负面结果的问题**：DeBERTa NLI escape + DRC 方法展示了"怎样才行得通"，使论文不止于"这不行"。DRC 以 39% verification cost 恢复 90% combo gain，实用价值高。
4. **27 种修复策略的穷举分析**：虽然结果是负面的，但穷举本身就有价值——它关闭了许多潜在的"也许换个策略就行"的反驳。
5. **写作质量整体较好**：Introduction 的动机链（SC → CJT → independence failure → symbolic mirage）清晰，从负面结果到机制解释到建设性方案的叙事弧完整。

---

## Questions for Authors

1. SatLM 使用 LLM + SAT solver 但报告正面结果。你们认为关键区别是什么？是 specification-generation vs. trace-extraction 的区别吗？如果是，请在论文中明确讨论。
2. Effective-K 和 Bias Ratio 作为"诊断工具"被列为贡献之一（Contribution 3），但 Effective-K 直接来自 Kish (1965) 的 design effect，Bias Ratio 是约束计数的简单比值，Process-κ 是 Fleiss' kappa。能否论证这些指标在 SC 诊断场景下的应用为何构成方法论贡献（而非已有度量的直接使用）？
3. 在 DRC 中，DeBERTa NLI 作为外部验证器引入。但如果核心论点是"自提取继承偏差"，那么任何外部验证器都应该有效。为什么不测试其他类型的外部验证器（如 trained reward model, code execution）来验证 "cross-architecture escape" 的泛化性？
4. Qwen3-14B（thinking mode）在 Table 1 中表现最好（accuracy 86%），但 SICA 仍未改善。reasoning model 是否改变了 confirmation bias 的性质？§7 中简短提及，但值得更深入分析。
5. 论文声称 "process-level independence" 是第三个贡献，但 §5.3 的分析（TF-IDF cosine similarity → Fleiss' kappa）仅是标准 NLP pipeline。能否论证为什么这比简单的 answer agreement 提供了更多信息？

---

## Missing References

1. **"Unveiling Confirmation Bias in Chain-of-Thought Reasoning"** (arXiv:2506.12301, Jun 2025) — 直接研究 CoT 中的 confirmation bias，与本文的 "Symbolic Confirmation Bias" 概念高度相关。
2. **"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models"** (arXiv:2604.02485, Apr 2026) — 系统评估 LLM confirmation bias 的框架，可能是 concurrent work。
3. **"Eidoku: A Neuro-Symbolic Verification Gate for LLM Reasoning via Structural Constraint Satisfaction"** (arXiv:2512.20664, Dec 2025) — 将 LLM 推理验证建模为约束满足问题，与本文的 Z3 MAX-SAT 方法相关。
4. 此外，建议在 §2 中更深入讨论 **SatLM** 和 **CRITIC** 与本文方法的区别（当前仅列在引用串中）。

---

## 格式与合规

- ✅ 正文 8 页（§1-§8 在 pages 1-8 内）
- ✅ Limitations section 存在（page 8-9），不计入页数
- ✅ 匿名性完好（"Anonymous ACL submission"，无 de-anonymizing 信息）
- ✅ 引用格式符合 ACL 标准（natbib, \citep/\citet）
- ✅ 引用核查：56 条 bib entries, 0 orphan, 0 missing，37 条在线验证通过

---

## 负面结果论文的 Venue Fit 评估

作为 EMNLP 2026 投稿，本文作为**负面结果论文 fit Findings 但可能不足以进入主会议**：

- **Findings 适合**：soundness 和 reproducibility 均良好，负面结果有 actionable takeaway（DRC），实验规模充分。
- **主会议有难度**：核心发现对熟悉领域的人可预测（Excitement 不足），诊断指标缺乏方法论创新，constructive contribution 适用范围有限。
- **目标读者**：neurosymbolic reasoning 研究者（学到"自提取不行，需要跨架构验证"）和 SC/test-time compute scaling 研究者（学到独立性是瓶颈）。

**最终评分：Overall 3.0 (Findings)，Confidence 4/5。**


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-21T06:40:59.418247+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "round_number": "1",
  "text": "## 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，说明理由\n- **[REBUT]**：反驳该问题，提供具体证据（引用论文中的 Section/Table/Figure）\n\n---\n\n# Reviewer 2 审稿意见（Overall: 3.0 Findings）\n\n**审查侧重**: 新颖性 + 完整性 + 叙事质量\n\n## Must-Fix 问题\n\n**N1** [critical] 相对于 Huang et al. (2024) 和 Stechly et al. (2025) 的增量新颖性不足\n- Huang et al. (ICLR 2024) 已证明 LLMs cannot self-correct reasoning without external feedback；Stechly et al. (ICLR 2025) 已证明 self-verification 因共享相同偏差而失败。本文的核心发现——\"自提取约束继承模型偏差\"——是上述结论在符号约束领域的直接实例化，而非根本性新发现。\n- 建议：论证为什么符号约束不同于自然语言 self-correction——neurosymbolic 社区的隐含假设是\"一旦形式化，推理就变得可靠\"，而本文挑战的正是这个假设。\n\n**N2** [critical] SatLM 正面结果与本文负面结果的对比缺失\n- SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM + SAT solver 但报告显著提升。本文未讨论为什么 SatLM works 而 SICA doesn't。关键区别在于 specification-generation（问题 → 形式化）vs trace-constraint-extraction（推理轨迹 → 约束）。\n- 建议：在 §2 或 §7 中明确对比。\n\n**N3** [critical] \"Symbolic Confirmation Bias\" 作为术语的独立性不足\n- 近期已有直接研究 CoT confirmation bias 的工作（arXiv:2506.12301, arXiv:2604.02485）。本文的概念需要与这些区分。\n- 建议：论证特殊性在于即使约束通过了 Z3 satisfiable 验证，偏差仍存在。\n\n## Should-Fix 问题\n\n**W1** [warning] Independence-Accuracy Trade-off 是 bias-variance tradeoff 的重述\n- 本质上是 LLM 采样中已知现象——高温度增加多样性但降低质量。Krogh and Vedelsby (1994) 早已描述类似权衡。\n- 建议：定位为实验观察而非独立贡献。\n\n**W2** [warning] Related Work 过度压缩，缺乏深度讨论\n- 三段 Related Work 列举约 25 篇论文，阅读体验像引用列表而非文献讨论。Neurosymbolic Reasoning 未区分 specification-generation, program-generation, trace-constraint-extraction。\n\n**W3** [warning] Proposition 1 和 Corollary 1 的形式化程度不足\n- proof sketch 仅有 3 行。建议提供完整证明或降级为 \"Empirical Claim\"。\n\n**W4** [warning] 27 种修复策略在正文中展示不足\n- 正文仅用 5 行概述，细节全在 Appendix。作为核心论证应更充分展示。\n\n**W5** [warning] Cross-architecture NLI escape 的适用范围有限\n- 仅在 FOLIO 和 ProofWriter 上有效，LogiQA 无效。DRC 实用性局限于清晰逻辑结构任务。\n\n## 主要优势\n1. 实验规模与严谨性出色（6 模型 × 5 数据集 × 3,000+ 条件评估）\n2. CJT 理论框架引入有启发性\n3. DeBERTa NLI escape + DRC 展示了\"怎样才行得通\"\n4. 27 种修复策略穷举关闭了\"也许换策略就行\"的反驳\n5. 写作质量整体较好，叙事弧完整\n\n## Missing References\n1. \"Unveiling Confirmation Bias in Chain-of-Thought Reasoning\" (arXiv:2506.12301, Jun 2025)\n2. \"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models\" (arXiv:2604.02485, Apr 2026)\n3. \"Eidoku: Neuro-Symbolic Verification Gate via Structural Constraint Satisfaction\" (arXiv:2512.20664, Dec 2025)\n\n---\n\n请逐条回应上述 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "round_number": "1",
    "text": "## 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，说明理由\n- **[REBUT]**：反驳该问题，提供具体证据（引用论文中的 Section/Table/Figure）\n\n---\n\n# Reviewer 2 审稿意见（Overall: 3.0 Findings）\n\n**审查侧重**: 新颖性 + 完整性 + 叙事质量\n\n## Must-Fix 问题\n\n**N1** [critical] 相对于 Huang et al. (2024) 和 Stechly et al. (2025) 的增量新颖性不足\n- Huang et al. (ICLR 2024) 已证明 LLMs cannot self-correct reasoning without external feedback；Stechly et al. (ICLR 2025) 已证明 self-verification 因共享相同偏差而失败。本文的核心发现——\"自提取约束继承模型偏差\"——是上述结论在符号约束领域的直接实例化，而非根本性新发现。\n- 建议：论证为什么符号约束不同于自然语言 self-correction——neurosymbolic 社区的隐含假设是\"一旦形式化，推理就变得可靠\"，而本文挑战的正是这个假设。\n\n**N2** [critical] SatLM 正面结果与本文负面结果的对比缺失\n- SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM + SAT solver 但报告显著提升。本文未讨论为什么 SatLM works 而 SICA doesn't。关键区别在于 specification-generation（问题 → 形式化）vs trace-constraint-extraction（推理轨迹 → 约束）。\n- 建议：在 §2 或 §7 中明确对比。\n\n**N3** [critical] \"Symbolic Confirmation Bias\" 作为术语的独立性不足\n- 近期已有直接研究 CoT confirmation bias 的工作（arXiv:2506.12301, arXiv:2604.02485）。本文的概念需要与这些区分。\n- 建议：论证特殊性在于即使约束通过了 Z3 satisfiable 验证，偏差仍存在。\n\n## Should-Fix 问题\n\n**W1** [warning] Independence-Accuracy Trade-off 是 bias-variance tradeoff 的重述\n- 本质上是 LLM 采样中已知现象——高温度增加多样性但降低质量。Krogh and Vedelsby (1994) 早已描述类似权衡。\n- 建议：定位为实验观察而非独立贡献。\n\n**W2** [warning] Related Work 过度压缩，缺乏深度讨论\n- 三段 Related Work 列举约 25 篇论文，阅读体验像引用列表而非文献讨论。Neurosymbolic Reasoning 未区分 specification-generation, program-generation, trace-constraint-extraction。\n\n**W3** [warning] Proposition 1 和 Corollary 1 的形式化程度不足\n- proof sketch 仅有 3 行。建议提供完整证明或降级为 \"Empirical Claim\"。\n\n**W4** [warning] 27 种修复策略在正文中展示不足\n- 正文仅用 5 行概述，细节全在 Appendix。作为核心论证应更充分展示。\n\n**W5** [warning] Cross-architecture NLI escape 的适用范围有限\n- 仅在 FOLIO 和 ProofWriter 上有效，LogiQA 无效。DRC 实用性局限于清晰逻辑结构任务。\n\n## 主要优势\n1. 实验规模与严谨性出色（6 模型 × 5 数据集 × 3,000+ 条件评估）\n2. CJT 理论框架引入有启发性\n3. DeBERTa NLI escape + DRC 展示了\"怎样才行得通\"\n4. 27 种修复策略穷举关闭了\"也许换策略就行\"的反驳\n5. 写作质量整体较好，叙事弧完整\n\n## Missing References\n1. \"Unveiling Confirmation Bias in Chain-of-Thought Reasoning\" (arXiv:2506.12301, Jun 2025)\n2. \"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models\" (arXiv:2604.02485, Apr 2026)\n3. \"Eidoku: Neuro-Symbolic Verification Gate via Structural Constraint Satisfaction\" (arXiv:2512.20664, Dec 2025)\n\n---\n\n请逐条回应上述 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题。"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-21T06:41:26.531502+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27113
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-21T06:41:26.683748+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
  "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "round_number": "1",
  "text": "## 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，说明理由\n- **[REBUT]**：反驳该问题，提供具体证据（引用论文中的 Section/Table/Figure）\n\n---\n\n# Reviewer 1 审稿意见（Overall: 3.5 Borderline Conference）\n\n**审查侧重**: 方法严谨性 + 实验设计\n\n## Must-Fix 问题\n\n**N1** [critical] Proposition 1（Self-Extraction Ceiling）缺少证明\n- Section 3.3 的 Proposition 1 声称 Δ_max^self ≲ Δ_oracle / BR(M)，但全文无证明。\"≲\" 不精确。底部 proof sketch 实际是 Corollary 1 的。\n- 建议：提供正式证明或降级为 empirical observation。\n\n**N2** [critical] Fleiss' κ → Effective-K 映射的理论依据不足\n- Kish (1965) 的设计效应公式使用 ICC，不是 Fleiss' κ。论文以 \"mean pairwise r = 0.625\" 作为验证，但 r=0.625 仅中等相关，约 61% 方差未被解释。然而 K_eff 在多处被作为定量诊断指标使用。\n- 建议：报告 ICC 本身、给出 sensitivity 分析、或限定为序数诊断。\n\n**N3** [critical] Spearman ρ = 1.0 (n=6) 的 capability gap 结论依赖极小样本\n- 6 个数据点（3 NLI 架构 × 2 有效 generator 水平），且非完全独立。p=0.003 虽显著，但 6 点排列的约束很强。\n- 建议：增加 generator-verifier 组合、承认非完美单调性、降级措辞。\n\n## Should-Fix 问题\n\n**W1** [warning] DRC 的 τ 阈值在测试集上选择，无 held-out 评估\n- τ ∈ {0.3, 0.5, 0.7, 0.9} 均在同一 ProofWriter (n=600) 上选择和评估。作为第 4 个 contribution 应有更严格评估。\n\n**W2** [warning] Cross-architecture NLI escape 适用范围极窄\n- BH 后仅 2/12 条件存活。仅在弱 generator + premise-conclusion 可分解 + verifier>generator 的场景有效。\n\n**W3** [warning] 四种子复制方差大、统计功效 <21%\n- Δ ∈ {+3.43, +2.94, 0.00, −0.49}pp。Power analysis 显示观测功效均 <21%。核心 claim 应更明确承认 power limitation。\n\n**W4** [warning] TOST ±2pp margin 缺少显式理由\n- 未论证为什么 2pp 是合适的实际意义阈值。选 ±3pp 更多条件等价。\n\n**W5** [warning] Bias Ratio 无置信区间\n- BR 值（4.97×, 3.93×, 2.88×）未报告 CI 或标准误。\n\n## 主要优势\n1. 27 种补救策略穷举，说服力强\n2. Oracle 控制实验设计精良\n3. 多层次诊断体系（answer-level κ, process-level cosine, BR, C₀, entropy）\n4. 统计处理在 NLP 论文中罕见地严谨\n5. Appendix 材料极为充实\n\n## Missing References\n- Khalifa et al. (2023) \"Discriminator-Guided Multi-step Reasoning\"\n- Yao et al. (2023) \"Tree of Thoughts\"\n\n---\n\n请逐条回应上述 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8",
    "director_session_key": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
    "round_number": "1",
    "text": "## 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]**：同意该问题，说明理由\n- **[REBUT]**：反驳该问题，提供具体证据（引用论文中的 Section/Table/Figure）\n\n---\n\n# Reviewer 1 审稿意见（Overall: 3.5 Borderline Conference）\n\n**审查侧重**: 方法严谨性 + 实验设计\n\n## Must-Fix 问题\n\n**N1** [critical] Proposition 1（Self-Extraction Ceiling）缺少证明\n- Section 3.3 的 Proposition 1 声称 Δ_max^self ≲ Δ_oracle / BR(M)，但全文无证明。\"≲\" 不精确。底部 proof sketch 实际是 Corollary 1 的。\n- 建议：提供正式证明或降级为 empirical observation。\n\n**N2** [critical] Fleiss' κ → Effective-K 映射的理论依据不足\n- Kish (1965) 的设计效应公式使用 ICC，不是 Fleiss' κ。论文以 \"mean pairwise r = 0.625\" 作为验证，但 r=0.625 仅中等相关，约 61% 方差未被解释。然而 K_eff 在多处被作为定量诊断指标使用。\n- 建议：报告 ICC 本身、给出 sensitivity 分析、或限定为序数诊断。\n\n**N3** [critical] Spearman ρ = 1.0 (n=6) 的 capability gap 结论依赖极小样本\n- 6 个数据点（3 NLI 架构 × 2 有效 generator 水平），且非完全独立。p=0.003 虽显著，但 6 点排列的约束很强。\n- 建议：增加 generator-verifier 组合、承认非完美单调性、降级措辞。\n\n## Should-Fix 问题\n\n**W1** [warning] DRC 的 τ 阈值在测试集上选择，无 held-out 评估\n- τ ∈ {0.3, 0.5, 0.7, 0.9} 均在同一 ProofWriter (n=600) 上选择和评估。作为第 4 个 contribution 应有更严格评估。\n\n**W2** [warning] Cross-architecture NLI escape 适用范围极窄\n- BH 后仅 2/12 条件存活。仅在弱 generator + premise-conclusion 可分解 + verifier>generator 的场景有效。\n\n**W3** [warning] 四种子复制方差大、统计功效 <21%\n- Δ ∈ {+3.43, +2.94, 0.00, −0.49}pp。Power analysis 显示观测功效均 <21%。核心 claim 应更明确承认 power limitation。\n\n**W4** [warning] TOST ±2pp margin 缺少显式理由\n- 未论证为什么 2pp 是合适的实际意义阈值。选 ±3pp 更多条件等价。\n\n**W5** [warning] Bias Ratio 无置信区间\n- BR 值（4.97×, 3.93×, 2.88×）未报告 CI 或标准误。\n\n## 主要优势\n1. 27 种补救策略穷举，说服力强\n2. Oracle 控制实验设计精良\n3. 多层次诊断体系（answer-level κ, process-level cosine, BR, C₀, entropy）\n4. 统计处理在 NLP 论文中罕见地严谨\n5. Appendix 材料极为充实\n\n## Missing References\n- Khalifa et al. (2023) \"Discriminator-Guided Multi-step Reasoning\"\n- Yao et al. (2023) \"Tree of Thoughts\"\n\n---\n\n请逐条回应上述 Must-Fix (N1-N3) 和 Should-Fix (W1-W5) 问题。"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-21T06:41:28.295207+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 998 · 2026-05-21T06:41:31.501840+00:00_

交叉分享已发出。两位 Reviewer 正在互相审阅对方的意见并逐条回应。等待交叉回应结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 63

## Round 63

2 recorded events


### User

_source line 999 · 2026-05-21T06:41:34.229772+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)，Confidence 4/5。

核心判断：
- **新颖性有限**：核心发现（自提取约束继承模型偏差）是 Huang et al. (2024) 和 Stechly et al. (2025) 已知结论在符号约束领域的 instantiation，非根本性新发现
- **关键遗漏**：SatLM 同样用 LLM+solver 但报告正面结果，论文未讨论为什么一个 work 一个不 work（specification-generation vs. trace-extraction 的区别）
- **主要优势**：实验规模和严谨性出色（6模型×5数据集×3000+条件×4-seed），27种策略穷举分析有价值，DRC 提供实用的建设性方案
- **三个 Must-Fix**：(1) 增量新颖性论证不足，(2) SatLM 对比缺失，(3) "Symbolic Confirmation Bias" 需与近期 CoT confirmation bias 工作区分
- **Venue fit**：适合 Findings，主会议 borderline

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1000 · 2026-05-21T06:41:40.216747+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 1001 · 2026-05-21T06:42:58.267171+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Must-Fix 问题

**[REBUT] R2-N1: 相对于 Huang et al. (2024) 和 Stechly et al. (2025) 的增量新颖性不足**

不完全同意"直接实例化"的定性。论文在 Introduction 第 24-25 段明确论证了区别：

> "Prior work establishes that LLMs cannot self-correct without external feedback (Huang et al., 2024; Stechly et al., 2025), but concerns natural-language self-correction. Z3 introduces a *sound*, non-neural channel that *guarantees* logical consistency given well-formed constraints, making self-extraction under formal verification a non-trivial test case. Unlike natural-language self-correction, formal extraction produces machine-verifiable constraints, making extraction errors in principle detectable. That this stronger channel still fails—Z3 rejects only 3.4% of constraints (§5.2) because they are individually valid yet collectively biased—reveals that the bias is semantic (what gets extracted) rather than syntactic (how it is expressed)."

关键区别在于：Huang/Stechly 的结论是关于自然语言 self-correction 的——模型不能用自然语言判断自己的推理是否正确。而本文测试的是一个严格更强的条件：即使引入一个 **sound formal verifier (Z3)**，只要约束来自同一模型，形式化通道也无法突破偏差。这不是显而易见的——neurosymbolic 社区（Logic-LM, LINC, SatLM, FoVer 等）的隐含假设恰恰是"一旦形式化+solver 验证，推理可靠性就会提升"。Z3 只拒绝了 3.4% 的约束这一发现，说明瓶颈不在 syntactic correctness 而在 semantic bias——这是 Huang/Stechly 的自然语言框架无法区分的。

**但我同意 R2 的改进建议**：论文应在 Related Work 或 Discussion 中更显式地用 1-2 段对比 Huang/Stechly，而非将区别分散在 Introduction 的一两句话中。当前的区分虽然存在但不够突出。

---

**[REBUT] R2-N2: SatLM 正面结果与本文负面结果的对比缺失**

论文 **已经** 在 Related Work（Section 2, Neurosymbolic reasoning 段）中讨论了这个区别：

> "SatLM (Ye et al., 2024) generates complete SAT translations from problem descriptions and reports positive results; critically, SatLM's constraints derive from problem-level understanding, whereas SICA extracts from reasoning traces. Problem-level formalization avoids answer contamination; trace-level extraction inherits confirmation bias (§3.2)."

这段文字明确指出了关键区别：**specification-generation**（问题 → 形式化，无 answer contamination）vs **trace-constraint-extraction**（推理轨迹 → 约束，继承 answer-coupled bias）。Section 3.3 的 Symbolic Mirage hypothesis 进一步解释了为什么 trace-level extraction 必然失败：约束与其源 trace 的答案耦合（Eq. 4, degeneration condition），导致 MAX-SAT 退化为投票。SatLM 绕过这一问题是因为它不从 trace 中提取约束。

**但我同意这值得更充分的讨论**：当前仅 2 句话的对比对于理解 "为什么 SatLM works 而 SICA doesn't" 可能不够充分。建议在 Discussion（Section 7）增加一段 explicit 对比，将 specification-generation / program-generation / trace-constraint-extraction 三种范式的差异系统化展开，特别是说明 trace-level extraction 的 answer contamination 为什么是结构性的（BR > 1 across all models, Table in Appendix P）。

---

**[AGREE] R2-N3: "Symbolic Confirmation Bias" 作为术语的独立性需要加强**

同意需要与 R2 引用的 CoT confirmation bias 文献区分。论文当前使用"symbolic confirmation bias"但未引用 arXiv:2506.12301 和 arXiv:2604.02485。

论文的特殊性——**即使约束通过了 Z3 satisfiability 验证，偏差仍然存在**——实际上是比 general CoT confirmation bias 更强也更令人惊讶的发现。General CoT bias 说的是 "reasoning traces have biased content"；本文发现的是 "even when you extract formal logic from those traces and verify it with a sound solver, the bias survives because it's encoded in *which* constraints get extracted, not in their *syntactic validity*"（Z3 rejects only 3.4%, Section 5.2）。

但这个区别在论文中表述不够清晰。建议：(a) 引用 R2 提到的两篇 CoT confirmation bias 文献；(b) 在 Section 5.2 开头增加 1-2 句明确区分：general CoT confirmation bias 关注推理内容偏差，而 symbolic confirmation bias 的核心发现是偏差在 formal verification 后仍持续存在。

---

## Should-Fix 问题

**[REBUT] R2-W1: Independence-Accuracy Trade-off 是 bias-variance tradeoff 的重述**

部分不同意。虽然高层概念确实与 bias-variance tradeoff 相关，但论文的贡献在于 **具体量化** 了 LLM self-extraction 场景下的 trade-off 边界：

1. κ ≥ 0.40 是所有非破坏性方法的下限（Table in Appendix R, 4 个方法 × 3 个模型家族）
2. 唯一突破此下限的方法（Debate, κ = 0.15）导致 accuracy 灾难性下降（−18.6pp, p < 0.001, Table 12）
3. 这个 ceiling 是跨架构的——LLaMA、Mistral、Qwen 三个家族均 κ ≥ 0.41

这不是简单地说"更多多样性 = 更低质量"。论文发现的是一个 **定量边界**：在当前 7B-32B scale 下，same-model 方法无法同时实现 κ < 0.40 和 accuracy 不下降。这是一个具体的、可验证的、可能在更大规模被打破的经验发现，而非对已知原理的重述。

但 Discussion 已经引用了 Krogh and Vedelsby (1994) 和 Brown (2005)，并将其定位为 ensemble tension 的具体实例（Section 7, "Test-time scaling and ensemble diversity" 段）。所以论文已经做了 R2 建议的事。

---

**[AGREE] R2-W2: Related Work 过度压缩**

同意。当前 Related Work（约半页）将约 25 篇论文压缩到 3 个段落中，阅读体验确实像引用列表。特别是 Neurosymbolic Reasoning 段将 specification-generation（Logic-LM, LINC, SatLM）、program-generation（PAL, PoT）和 trace-constraint-extraction（SICA）混在一起没有清晰分类。8 页限制下空间有限，但至少应将三种范式用段落或列表区分开来，并为每种范式标明与本文的关系。这也会自然解决 R2-N2 的 SatLM 对比问题。

---

**[AGREE] R2-W3: Proposition 1 和 Corollary 1 形式化不足**

强烈同意。这与我自己的 N1 问题完全一致。Proposition 1 无证明、"≲" 不精确、proof sketch 实际上是 Corollary 的。要么提供完整证明，要么降级为 Empirical Claim / Observation。

---

**[AGREE] R2-W4: 27 种修复策略在正文中展示不足**

同意。这是论文最有说服力的论证之一（"关闭了 'maybe a different strategy works' 的反驳空间"），但正文 Section 5.4 仅有约 5 行文字 + Figure 2 的概览图。建议至少在正文中用 mini-table 展示 top 5 有代表性策略的结果（如 Debate/Contrastive/Cross-model/CEGIS/κ-aware SC），让读者无需翻阅 Appendix Tables 11-13 就能把握核心证据。在 8 页预算下可以从 Discussion 压缩出空间（当前 Discussion 的部分内容与 Analysis 有重复）。

---

**[AGREE] R2-W5: Cross-architecture NLI escape 适用范围有限**

同意，与我自己的 W2 完全一致。BH 校正后仅 2/12 条件存活（均为 Mistral-7B ProofWriter）。NLI verifier 仅适用于可分解为 premise-conclusion 的任务，且要求 verifier 强于 generator。论文应更坦诚地承认这是 narrow PoC，而非暗示这是一个 general escape path。

---

## 关于 R2 整体评分的看法

R2 给出 Overall 3.0 (Findings)，核心理由是新颖性不足。我认为这个评分偏低了 0.5 分。

R2-N1 的 "incremental novelty" 批评有一定道理，但低估了两个关键点：(a) 从 NL self-correction 到 formal verification 下的 self-extraction 不是平凡的推广——Z3 是 sound 的，社区有理由期望它能打破偏差循环；(b) 27 种策略的穷举关闭 + 具体量化的 κ ≥ 0.40 floor + oracle control 的干净分离，在实验贡献上超越了简单的 "领域实例化"。

R2-N2 的 SatLM 对比问题论文已有初步讨论（虽然不够充分），不应被视为 "缺失"。

综合来看，我维持 3.5 (Borderline Conference) 的评分。如果 N1/N2/N3 的区分性讨论得到加强，这篇论文的叙事会显著改善。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1002 · 2026-05-21T06:43:03.828473+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 65

## Round 65

2 recorded events


### User

_source line 1003 · 2026-05-21T06:43:06.978922+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条交叉回应。

核心判断：R2 的三个 Must-Fix 中，N2（SatLM 对比）论文已有初步讨论（Related Work 段），我做了 REBUT 并建议扩展；N1（新颖性）我 REBUT 了"直接实例化"的定性但同意需要更显式对比；N3（术语区分）AGREE 需要加强。Should-Fix 中 W1（bias-variance）我 REBUT 了（论文已定位且贡献在于具体量化边界），W2-W5 均 AGREE。总体认为 R2 的 3.0 评分偏低 0.5 分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1004 · 2026-05-21T06:43:11.910522+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 66

## Round 66

12 recorded events


### User

_source line 1005 · 2026-05-21T06:45:20.284617+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 问题回应

### [AGREE] R1-N1: Proposition 1（Self-Extraction Ceiling）缺少证明

同意。我在自己的审稿中也标记了这个问题（R2-W3）。

重新检查 page 4-5：Proposition 1 声称 Δ_max^self ≲ Δ_oracle / BR(M)，但 page 5 顶部的 "Proof sketch" 实际论证的是 **Corollary 1** 的单调性（引用 Spearman ρ = 1.0, p = 0.003 作为"证明"），而非 Proposition 1 的 ceiling bound。这是一个结构性问题——一个形式化的 Proposition 挂了另一个命题的经验论据。

补充 R1 的观察："≲" 不仅不精确，而且 Proposition 1 的左边 (Δ_max^self) 和右边 (Δ_oracle / BR(M)) 的精确含义也不够形式化——Δ_oracle 的定义依赖于 §4.3 的 oracle 实验设置，而非纯数学构造。这使得 Proposition 1 实际上是一个 empirical claim dressed as a theorem。

**建议**：降级为 "Empirical Finding 1" 或在 Appendix 中提供基于 MAX-SAT 权重分配的完整推导。

---

### [AGREE，但有补充] R1-N2: Fleiss' κ → Effective-K 映射的理论依据不足

总体同意 R1 的技术关切，但需要补充一个重要 nuance。

**R1 正确的部分**：Kish (1965) design effect 公式 K_eff = K / (1 + (K-1)·ρ) 中 ρ 是 ICC，不是 Fleiss' κ。论文用 κ 替代 ICC 是一个近似，且验证相关性仅 r = 0.625（page 4），意味着约 61% 方差未被解释。

**需要补充的 nuance**：论文在 page 4 **已明确声明** K_eff 应被解读为 ordinal diagnostic（原文："K_eff should be interpreted as an ordinal diagnostic—ranking which conditions have genuine vote diversity—rather than as a literal effective sample size"）。在 Table 2 中，K_eff 主要用于 **排序** 不同条件的有效多样性（从 QwQ-1 的 ~0 到 Mistral-7B 几种设定的 1.62-1.77），这种序数使用对 κ→ICC 近似的敏感度较低。

**但问题在于**：论文在其他地方超出了 ordinal 使用范围。例如 §1 abstract 中 "Effective-K ≈ 1.20-3.62 for nominal K = 12"、以及 §5.1 中具体的数值讨论，都带有定量含义。这种 ordinal caveat 与 quantitative usage 之间的不一致性正是 R1 关切的核心。

**建议**：同意 R1 建议报告 ICC 本身，且在 Appendix 中提供 sensitivity analysis（例如：如果用 ICC 替换 κ，K_eff 排序是否改变？）。

---

### [AGREE] R1-N3: Spearman ρ = 1.0 (n=6) 的 capability gap 结论依赖极小样本

同意。这是 Corollary 1 和 §6 capability gap 分析的关键弱点。

具体证据：Figure 3 (page 7) 和相关文字显示 Spearman ρ = 1.0 基于 6 个 verifier-generator pairs（3 NLI architectures × 在 ProofWriter 上的有效 generator 水平）。n=6 时完美秩相关的 p 值约为 1/6! ≈ 0.00139（论文报告 p=0.003，可能是精确排列检验），表面上显著。但：

1. **6 点的约束极强**：任何近似单调的关系都容易产生高 Spearman ρ，特别是当 6 个点来自有限的 3×2 结构时。
2. **非完全独立**：同一 generator (Mistral-7B) 搭配 3 个不同 verifier 产生 3 个关联数据点。
3. **反例被淡化**：Table 3 显示 LLaMA-3.1-8B 作为 generator 时，NLI combo gain 非显著甚至可能为负（page 7 右列："LLaMA-3.1-8B (+1.39 pp, n.a.)"），但 LLaMA 点似乎被排除在 Spearman 计算之外（因为 BH correction 后不显著）。选择性纳入显著结果来计算 monotonicity 有循环论证的风险。

**建议**：同意 R1，将 "perfectly monotonic" 措辞降级为 "consistent directional trend"，增加更多 generator-verifier 组合（如使用更多 NLI 模型或更多 generator 规模），并承认 n=6 的局限性。

---

## Should-Fix 问题回应

### [AGREE] R1-W1: DRC 的 τ 阈值无 held-out 评估

同意。Table 4 (page 8) 展示了 τ ∈ {0.3, 0.5, 0.7} 的结果，但均在同一 ProofWriter (n=600) 上选择和评估。虽然展示多个 τ 值可视为 sensitivity analysis，但这与 held-out validation 不同——所有 τ 的性能数字都是在选择集上计算的。

作为 Contribution 4（DRC），方法论标准应更高。具体建议：在 ProofWriter 上 random split 为 dev/test，或在 FOLIO 上作为 held-out 验证 τ=0.7 是否迁移。如果 τ 选择对数据敏感，DRC 的 "90% recovery at 39% cost" 可能是 overfitted。

---

### [AGREE] R1-W2: Cross-architecture NLI escape 适用范围极窄

强烈同意。我在自己的审稿中也标记了这个问题（R2-W5，同一关切）。

补充证据：page 9 Limitations 明确承认 "cross-architecture NLI verifier (§6) provides no benefit on LogiQA (combo Δ ≤ +1pp, all p > 0.5)"。Table 3 (page 7) 的 BH correction 后仅 Mistral-7B 的 n=3 和 n=5 在 ProofWriter 上存活。综合两位 Reviewer 的一致意见：**NLI escape 的有效条件过于特殊化**（弱 generator + premise-conclusion decomposable + verifier >> generator），作为 constructive contribution 的说服力受限。

---

### [AGREE，但有 nuance] R1-W3: 四种子复制方差大、统计功效 <21%

同意功效不足是一个真实问题，但需补充 context。

**R1 正确的部分**：Δ ∈ {+3.43, +2.94, 0.00, −0.49}pp 的方差确实很大，Appendix E 报告的观测功效 <21% 意味着实验**无法可靠检测出真实效果**（如果存在的话）。对于声称 null result 的论文，低功效是特别危险的——它意味着不能排除存在小但真实的效果。

**需要的 nuance**：论文的核心 claim 并非仅依赖四种子复制。证据链包括：(1) Table 1 的 15 个模型-数据集条件中无非退化条件达到 FDR 显著（§4.2）；(2) TOST 等价检验（虽然 R1-W4 的 margin 质疑也成立）；(3) Oracle 控制实验证明机制（约束继承偏差）；(4) 27 种策略全部失败。四种子复制是一个环节，不是唯一支柱。但 R1 正确指出论文应更显著地承认 power limitation，而非将其藏在 Appendix E。

---

### [AGREE] R1-W4: TOST ±2pp margin 缺少显式理由

同意。TOST 等价检验的有效性完全取决于 margin 的选择。论文未论证为什么 2pp 是 LLM reasoning accuracy 上下文中的最小实际意义阈值。

在 NLP 领域，常见的实际意义阈值缺乏共识（不像临床试验有 FDA 指导），但论文至少应讨论：(1) 在 FOLIO/ProofWriter 这种 ~200-600 样本的数据集上，2pp 对应多少问题的差异？(2) 如果用 ±3pp（R1 建议），结论如何变化？(3) 是否有类似 NLP 研究采用 ±2pp 作为先例？

缺乏这种讨论，读者无法评估等价结论的稳健性。

---

### [AGREE] R1-W5: Bias Ratio 无置信区间

同意。BR = 4.97× (Mistral), 3.93× (Qwen), 2.88× (LLaMA) 是从 K=12 traces 的采样中估计的，本身有抽样变异性。Bootstrap CIs 是标准做法且计算成本极低（对已有约束数据重采样即可）。不报告 CI 使得读者无法判断 BR 跨模型的差异是否显著——例如 4.97 vs. 3.93 可能在 CI 重叠范围内。

---

## Missing References 回应

### [部分 AGREE] Yao et al. (2023) "Tree of Thoughts"

同意 ToT 应被引用。论文在 §2 讨论 test-time compute scaling 并引用了 Snell et al. (2025) 和 DeepSeek-R1，但遗漏了 ToT——这是 structured test-time search 最具影响力的方法之一。ToT 与本文的关联在于：ToT 使用 LLM self-evaluation 来引导搜索，这也面临 self-verification bias 问题，可以作为 related work 中 "test-time scaling + self-evaluation limitations" 交叉点的讨论素材。

### [REBUT] Khalifa et al. (2023) "Discriminator-Guided Multi-step Reasoning"

不认为这是关键遗漏。论文已通过 Lightman et al. (2024, PRM) 和 Wang et al. (2024, Math-Shepherd) 覆盖了 trained verifier/discriminator 这条线。Khalifa et al. 的贡献方向（训练判别器引导推理）与本文的核心议题（自提取约束的局限性）关联度有限——本文的重点不是"训练一个好的验证器"，而是"自提取的验证器为什么不行"。

---

## 总结

与 Reviewer 1 在 7/8 个问题上达成一致（3 Must-Fix 全部同意，5 Should-Fix 中 4 个完全同意、1 个有 nuance 地同意）。两位 Reviewer 的核心分歧在于 **Overall 评分**：

- R1: 3.5 (Borderline Conference) — 更看重实验的严谨性和 27 策略穷举
- R2: 3.0 (Findings) — 更看重新颖性不足（R2-N1/N2/N3，R1 未重点审查新颖性）

我维持 **3.0 (Findings)** 评分。R1 的技术问题（N1-N3）进一步削弱了论文的形式化贡献声称，但不改变论文作为 solid negative result 的基本定位。如果作者能：(1) 充分回应 SatLM 对比问题（R2-N2），(2) 降级 Proposition 1 为 empirical observation（R1-N1 + R2-W3），(3) 增加 DRC held-out validation（R1-W1），论文可以 comfortably fit Findings。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-21T06:45:51.618767+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-21T06:45:51.719786+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T06:31:44.936589+00:00\", \"completed_at\": \"2026-05-21T06:36:04.887515+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-5\", \"message\": \"连续 3 页无 figure/table，仅有公式穿插。Pages 3-4 的数学推导可部分豁免，但 page 5（实验 setup）为纯文本，建议将实验配置整理为 setup summary table 打破节奏\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Display items 过度拥挤：Table 2 + Figure 2 + Figure 3 + Table 3 共 4 个 display items 堆叠在同一页，视觉负荷过重。建议将 Figure 2 或 Figure 3 之一移至 page 6 或 page 8 分散\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 2（27 条干预策略条形图）单栏宽度下 y 轴标签文字过小（估计 ≤6pt），打印后难以辨认。建议改为 figure* 全宽排布或精简策略数量\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 散点图的 legend 和 axis label 字号偏小，建议适当放大\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点。ACL 双栏格式下常见，但若能在 page 1 右栏加入简化版 teaser figure（如 Figure 1 的精简版或核心结果示意），可强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 pipeline 图内文字（\\\"Extract Formal Constraints\\\"、\\\"Deduplicate\\\"等）字号偏小，建议稍放大以提升可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Experiments section 4.1 的 Models/Datasets/Parameters 信息密集但纯文本呈现，一个紧凑的 setup table（model × params）可同时改善可读性和 pages 3-5 的节奏问题\"}, {\"severity\": \"info\", \"dimension\": \"page 22\", \"message\": \"末页底部约 1/3 空白，appendix 页可接受但若有额外分析可填充利用\"}], \"counts\": {\"critical\": 0, \"warning\": 3, \"info\": 5}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-21T06:49:22.744310+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n- id: \"R3-N3\"\n  summary: \"Discriminative rate from small pilot\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"804-instance analysis: 8.2% [CI: 7.6, 8.8].\"\n  resolution_round: 3\n\n- id: \"R3-W6\"\n  summary: \"No 70B+ model tested\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 3\n  last_seen_round: 10\n  resolution: \"Acknowledged as limitation in paper.\"\n  resolution_round: 4\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W4 re-raised: Abstract 'full LLM capability range' overclaims given 7B-32B only. Model range limitation persists.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R9 R2-W8: DeepSeek-R1 distilled models not tested. R1 rebuts: Table 4 has DeepSeek-R1-7B data (n≤60). Scale limitation persists.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: Both reviewers note 7B-32B range. Not blocking but acknowledged.\"\n\n- id: \"R4-C1\"\n  summary: \"Cross-section Δ inconsistency\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"D064+D066 full data replacement completed.\"\n  resolution_round: 4\n\n- id: \"R4-C2\"\n  summary: \"CJT framing gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Dual-bottleneck paragraph added. Title changed.\"\n  resolution_round: 4\n\n- id: \"R4-C3\"\n  summary: \"Goldilocks zone evidence from only 1 model × 1 dataset\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Claims downgraded to 'directional trend'. V2 framing de-emphasizes intermediate region.\"\n  resolution_round: 5\n\n- id: \"R4-W1\"\n  summary: \"Multiple testing correction\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"BH correction computed: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Eff-K Kish (1965) attribution / κ→ICC proxy rigor\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 10\n  resolution: \"Pairwise Pearson r (mean 0.625, Mistral-7B) monotonically related to κ across 4 model families. κ validated as consensus proxy.\"\n  resolution_round: 7\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N2(Critical): Both reviewers re-raise. Paper has ordinal caveat but uses K_eff quantitatively elsewhere. Need ICC values + sensitivity analysis.\"\n\n- id: \"R4-M5\"\n  summary: \"Figure 2 old data\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Figure 2 moved to Appendix in V2 page budget compression.\"\n  resolution_round: 6\n\n- id: \"R5-N1\"\n  summary: \"Oracle ceiling '24%' cross-model comparison invalid\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Mistral-7B same-model oracle: +29.90pp (p<1e-13).\"\n  resolution_round: 5\n\n- id: \"R5-N2\"\n  summary: \"§4.1 Decoupling interim results (n=70/204) in main text\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"V2 framing removes §4.1 Decoupling from main text entirely.\"\n  resolution_round: 5\n\n- id: \"R5-N3\"\n  summary: \"'Fundamental' trade-off overclaimed\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All 'fundamental' → 'persistent' + 'at the 7B--32B scale'.\"\n  resolution_round: 5\n\n- id: \"R5-N4\"\n  summary: \"DeBERTa PoC statistically fragile — 9 discordant pairs\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"ProofWriter w=3 +3.50pp (p=0.013, n=600) as primary finding.\"\n  resolution_round: 5\n\n- id: \"R5-N5\"\n  summary: \"Discussion/Conclusion too thin for negative paper\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Discussion ~350 words, Conclusion ~220 words.\"\n  resolution_round: 5\n\n- id: \"R5-W1\"\n  summary: \"Variable name isolation confound\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Alpha-equivalence caveat added in Discussion.\"\n  resolution_round: 5\n\n- id: \"R5-W2\"\n  summary: \"Fleiss' κ as ICC proxy lacks formal justification\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Caveat added. Pairwise correlation validates κ (tracked under R4-W3).\"\n  resolution_round: 5\n\n- id: \"R5-W3\"\n  summary: \"Missing ensemble diversity literature\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Krogh & Vedelsby (1994) + Brown et al. (2005) cited.\"\n  resolution_round: 5\n\n- id: \"R5-W4\"\n  summary: \"§3/§5 content duplication\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Not flagged in R6 — considered resolved.\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"'25+ strategies' count inflated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"'more than twenty spanning fifteen distinct families'.\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"Code/data release not mentioned\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Reproducibility paragraph added.\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Solutions before Experiments ordering\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"main.tex reordered correctly.\"\n  resolution_round: 5\n\n- id: \"R5-W8\"\n  summary: \"TF-IDF cosine limitation under-discussed\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"Deferred to rebuttal. SBERT validation not worth GPU time per Reviewer assessment.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers re-raised: R1-W5 notes Figure 2 R²≈4.4% is very low; R2-Q4 asks if TF-IDF sufficiently captures semantic similarity. Limitation persists.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R1-W5(Info), R2-W7(Info): TF-IDF limitation re-confirmed by both reviewers. Consensus: acknowledged limitation, not blocking.\"\n    - round: 10\n      reviewers: []\n      note: \"R10: Not directly re-raised but still applicable.\"\n\n- id: \"R5-W9\"\n  summary: \"CJT novelty / Huang-Stechly distinction insufficient\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"Paper Agent added novelty differentiation paragraph (3 quantitative differentiators). Tracked jointly with R6-N3.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W1 re-raised novelty concern despite R7 fix. R1 partially rebuts, citing empirical specificity and quantitative tools. Divergence remains — see R8-W1.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R2-W1(Critical): Novelty gap persists. R1 partially rebuts (Z3 non-triviality + exhaustive remediation). Core divergence: R1=3.5 vs R2=3.0.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N1(Critical): Re-raised by R2, R1 partially rebuts but agrees distinction needs more prominence. Core novelty divergence persists (R1=3.5 vs R2=3.0).\"\n\n- id: \"R5-TC1\"\n  summary: \"SC tiebreaking inconsistency (dict-order vs alphabetical)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All tiebreaking standardized to alphabetical.\"\n  resolution_round: 5\n\n- id: \"R6-N1\"\n  summary: \"Statistical power 5.7%-20.6% — title 'Fail' overclaims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Title changed to 'Do Not Improve'. TOST computed: 4/15 equivalence, 5/15 genuine difference (4 negative), 6/15 underpowered.\"\n  resolution_round: 7\n\n- id: \"R6-N2\"\n  summary: \"Cross-arch PoC p=0.013 needs multiple comparison correction\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"BH correction: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s.\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Novelty vs self-correction literature (Huang/Stechly/Amonkar)\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"Novelty paragraph added (3 differentiators). §3.3 empirical bound further differentiates.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W1 re-raised novelty concern despite R7 fix.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R2-W1(Critical): Novelty gap persists.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: R2-N1 re-raises. R1 rebuts (Z3 formal verification is non-trivial test) but agrees distinction needs more prominence. Tracked jointly with R5-W9.\"\n\n- id: \"R6-W1\"\n  summary: \"Bias ratio numbers inconsistent between main text and Table 14\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent clarified BR calculation scope.\"\n  resolution_round: 7\n\n- id: \"R6-W2\"\n  summary: \"Type A/B/C failure mode classification is post-hoc\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Labeled as 'three empirical regimes (observation-driven)'.\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"Degeneration condition (Eq. 4) derivation incomplete\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Constraint rejection rate 3.44% integrated as empirical evidence.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"'Symbolic Mirage' terminology too marketing-like\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"Scoping sentence added. §3.3 contrasts with independently sourced constraints.\"\n  resolution_round: 7\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R9 R2-W6: Terminology branding re-raised.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R10: R2 notes 'Symbolic Mirage' introduced in §3.3 but rarely reused; relationship with 'Symbolic Confirmation Bias' unclear.\"\n\n- id: \"R6-W5\"\n  summary: \"α=0.5 penalty weight lacks sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"α sensitivity: max 0.49pp variation across α∈{0.0-1.0}.\"\n  resolution_round: 7\n\n- id: \"R6-W6\"\n  summary: \"GSM8K (n=30) and AIME (n=22) in main Table 1 misleading\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Kept with † marker and 'suggestive only' caveat.\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Orphan bib entry (press2023compositionality)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"press2023compositionality removed.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"Reasoning models not discussed as category in Related Work\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Reasoning models paragraph with κ=0.91 homogenization added.\"\n  resolution_round: 7\n\n- id: \"R6-V1\"\n  summary: \"Page 20 >75% empty white space\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Page 20 now ~60% filled.\"\n  resolution_round: 7\n\n- id: \"R6-V2\"\n  summary: \"Main text only 5 display items\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Figure swap complete. Main text §5.5 now has intervention summary figure.\"\n  resolution_round: 8\n\n- id: \"R8-N1\"\n  summary: \"FOL terminology misleading — actual constraints are predominantly propositional\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"All 'FOL' → 'logical constraints'. Quantifier proportion added.\"\n  resolution_round: 8\n\n- id: \"R8-N2\"\n  summary: \"Cross-architecture PoC underpowered: single generator × inconsistent dataset results\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§6 restructured. Clean single-generator evidence retained.\"\n  resolution_round: 8\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9: NLI weight w not cross-validated; cross-arch scale insufficient.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: Both reviewers agree NLI escape too narrow (BH 2/12 survive). Consensus: narrow PoC, not general solution.\"\n\n- id: \"R8-W1\"\n  summary: \"Incremental novelty relative to Huang/Stechly\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"§2 para 5 articulates 3 quantitative differentiators.\"\n  resolution_round: 8\n\n- id: \"R8-W2\"\n  summary: \"Seed replication inconsistency\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Table 1 has $^{4s}$ superscript.\"\n  resolution_round: 8\n\n- id: \"R8-W3\"\n  summary: \"Semantic deduplication missing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"§3.2 reports 46.0% dedup ratio. Z3 semantic dedup discussed.\"\n  resolution_round: 8\n\n- id: \"R8-W4\"\n  summary: \"Domain diversity + model range overclaimed in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Abstract scope accurately reflects 7B-32B.\"\n  resolution_round: 8\n\n- id: \"R8-W5\"\n  summary: \"Constraint quality analysis based on single model family\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Scoped in extended limitations.\"\n  resolution_round: 8\n\n- id: \"R8-W6\"\n  summary: \"Symbolic Confirmation Bias lacks connection to Turpin et al. unfaithful CoT\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Turpin connection present in §3.3 and Discussion.\"\n  resolution_round: 8\n\n- id: \"R8-I1\"\n  summary: \"Missing references: Weng et al. (2023) Self-Verification and Madaan et al. (2023) Self-Refine\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Both citations added.\"\n  resolution_round: 8\n\n- id: \"R8-I2\"\n  summary: \"Figure 5 buried in Appendix\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Figure swap complete.\"\n  resolution_round: 8\n\n- id: \"R8-I3\"\n  summary: \"83.3% confirmation bias rate needs per-model breakdown\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Per-model BR already reported in §5.2.\"\n  resolution_round: 8\n\n# =========================================================\n# Round 9 issues — status updated based on R10 findings\n# =========================================================\n\n- id: \"R9-W1\"\n  summary: \"Table 1 显著性声称缺少多重比较校正（16 条件未做 BH）\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Table 1 now includes BH correction (m=16). Both PW conditions show adj p=0.112. Caption notes 'BH adj. p'.\"\n  resolution_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 raised, R2 agrees.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: Table 1 caption explicitly shows BH adj p=0.112. Resolved.\"\n\n- id: \"R9-W2\"\n  summary: \"κ→Effective-K 映射形式化不足\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W2 raised, R2 agrees.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N2(Critical): Re-raised as critical by both reviewers. Paper has ordinal caveat (§3.1) but uses K_eff quantitatively elsewhere. Need ICC + sensitivity.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: (a) report ICC values, (b) add sensitivity analysis comparing K_eff from κ vs ICC, (c) enforce ordinal usage consistently\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W3\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W3 raised, R2 agrees.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: Subsumed under broader cross-arch narrowness concern. w=3 reported as primary but selection on test set.\"\n\n- id: \"R9-W4\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Sigmoid fit overfitting concern.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N3(Critical): Both agree. 'perfectly monotonic' based on n=6 non-independent points. R2 notes selective inclusion risk. Must downgrade to 'consistent directional trend'.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: downgrade 'perfectly monotonically' to 'strongly monotonically' or 'consistent directional trend', acknowledge n=6 limitation explicitly\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W5\"\n  summary: \"T_ext=0.3 extraction temperature 缺 sensitivity analysis\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Extraction temperature sensitivity missing.\"\n    - round: 10\n      reviewers: []\n      note: \"R10: Not directly re-raised but still applicable.\"\n\n- id: \"R9-W6\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W1(Critical), R1 partial rebut.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N1(Critical by R2): Core divergence. R1 rebuts (Z3 formal verification non-trivial), R2 maintains instantiation view. Director sides with R2: novelty insufficient for main conference, adequate for Findings.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: strengthen §1/§2 distinction from Huang/Stechly — emphasize Z3 formal verification channel as non-trivial test of neurosymbolic assumption\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W7\"\n  summary: \"Independence-Accuracy Trade-off 作为贡献存在部分同义反复\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W2(Critical), R1 agrees on reordering contributions.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-W1: R2 re-raises, R1 rebuts (contribution is quantitative boundary κ≥0.40, not the principle). Partial divergence.\"\n\n- id: \"R9-W8\"\n  summary: \"遗漏关键相关工作：SatLM 对比不充分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"SatLM/VeriCoT/CRITIC 引用建议.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N2(Critical by R2): SatLM comparison exists (2 sentences in §2) but insufficient. Both agree specification-generation vs trace-extraction distinction needs systematic expansion.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: expand SatLM comparison in §2 or §7 with specification-generation / program-generation / trace-extraction taxonomy\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W9\"\n  summary: \"Abstract 'sixteen' vs §4.2 'fifteen' 数字不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Table 1 有 16 个 non-degenerate 行，§4.2 'fifteen' 为笔误。\"\n    - round: 10\n      reviewers: []\n      note: \"R10: Not re-raised but still needs fix.\"\n\n- id: \"R9-W10\"\n  summary: \"Cross-architecture escape 实验规模不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"缺少与其他外部验证方法的对比.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-W2(R1)/W5(R2): Both strongly agree. BH 2/12 survive. NLI only works on premise-conclusion tasks with positive capability gap. Narrow PoC consensus.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: explicitly frame as narrow PoC in §6 and Limitations, discuss NLI applicability conditions\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W11\"\n  summary: \"术语品牌化过多\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"'capability trap' 应弱化.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R10: R2 notes 'Symbolic Mirage' introduced §3.3 but rarely reused; unclear relationship with 'Symbolic Confirmation Bias'.\"\n\n- id: \"R9-W12\"\n  summary: \"σ(c,a) provenance-based 设计未作为 design limitation 讨论\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-3 连续 3 页纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"R10 Visual Check confirms: pages 3-5 连续无 figure/table.\"\n\n- id: \"R9-VL4\"\n  summary: \"Page 8 Conclusion 仓促\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"R10: R2 notes Conclusion is compressed.\"\n\n# =========================================================\n# Round 10 (fresh review) — new issues\n# =========================================================\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both reviewers identify: Proposition 1 has no proof, '≲' imprecise, proof sketch belongs to Corollary 1. R2 adds Δ_oracle definition depends on experimental setup not math. Consensus: downgrade to Empirical Finding or provide formal proof.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: either provide complete proof in Appendix or downgrade to 'Empirical Finding 1' with explicit assumptions\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱，ordinal caveat 与 quantitative usage 矛盾\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. Kish (1965) uses ICC not κ. Paper has ordinal caveat but K_eff used quantitatively in abstract/§5.1. Need ICC values + sensitivity.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: (a) report ICC values alongside κ, (b) sensitivity analysis in Appendix, (c) enforce ordinal interpretation consistently\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. 3 NLI arch × 2 generator levels, non-independent. R2 notes selective inclusion risk. n=9 robustness check (ρ=0.836) more honest.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: downgrade 'perfectly monotonically' → 'strongly monotonically', report n=9 result as primary, acknowledge n=6 limitation\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. τ=0.7 selected and evaluated on same ProofWriter n=600. '90% recovery at 39% cost' may be overfitted.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: add dev/test split or cross-dataset τ validation, or explicitly flag as oracle selection\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄 (BH 2/12 survive)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Strong consensus. Only works: weak generator + premise-conclusion decomposable + verifier>generator. LogiQA ineffective. Narrow PoC.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: frame as narrow PoC not general escape, discuss applicability conditions explicitly\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 raises, R2 agrees with nuance (not sole evidence pillar). Power limitation should be more prominent in main text.\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. No justification for why 2pp is the practical significance threshold. Need sensitivity across margins.\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. BR values (4.97×, 3.93×, 2.88×) lack CIs. Bootstrap CI is standard and low-cost.\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 raises as critical. R1 notes paper has 2 sentences but agrees needs expansion. Need systematic taxonomy in §2 or §7.\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N3 raises. R1 agrees. Key distinction: bias survives formal Z3 verification. Need to cite arXiv:2506.12301 + arXiv:2604.02485 and differentiate.\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W2 raises, R1 agrees. Neurosymbolic paragraph mixes specification-generation/program-generation/trace-extraction without taxonomy.\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W4 raises, R1 agrees. §5.4 仅 5 行文字 + Figure 2. Need representative strategy discussion in main text.\"\n\n- id: \"R10-I1\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W1 raises, R1 rebuts (quantitative boundary κ≥0.40 is the contribution, not the principle). Partial divergence.\"\n\n- id: \"R10-I2\"\n  summary: \"缺失引用：CoT confirmation bias 文献 + Eidoku + Tree of Thoughts\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 suggests arXiv:2506.12301, arXiv:2604.02485, arXiv:2512.20664. R1 suggests ToT (Yao 2023). R2 rebuts Khalifa (2023) as not critical.\"\n\n- id: \"R10-VL1\"\n  summary: \"Pages 3-5 连续无 display item；page 7 display items 过度拥挤\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Visual check: pages 3-5 pure text; page 7 has 4 display items stacked. Figure 2 y-axis labels ≤6pt.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n- id: \"R3-N3\"\n  summary: \"Discriminative rate from small pilot\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"804-instance analysis: 8.2% [CI: 7.6, 8.8].\"\n  resolution_round: 3\n\n- id: \"R3-W6\"\n  summary: \"No 70B+ model tested\"\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 3\n  last_seen_round: 10\n  resolution: \"Acknowledged as limitation in paper.\"\n  resolution_round: 4\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W4 re-raised: Abstract 'full LLM capability range' overclaims given 7B-32B only. Model range limitation persists.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R9 R2-W8: DeepSeek-R1 distilled models not tested. R1 rebuts: Table 4 has DeepSeek-R1-7B data (n≤60). Scale limitation persists.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: Both reviewers note 7B-32B range. Not blocking but acknowledged.\"\n\n- id: \"R4-C1\"\n  summary: \"Cross-section Δ inconsistency\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"D064+D066 full data replacement completed.\"\n  resolution_round: 4\n\n- id: \"R4-C2\"\n  summary: \"CJT framing gap\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Dual-bottleneck paragraph added. Title changed.\"\n  resolution_round: 4\n\n- id: \"R4-C3\"\n  summary: \"Goldilocks zone evidence from only 1 model × 1 dataset\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"Claims downgraded to 'directional trend'. V2 framing de-emphasizes intermediate region.\"\n  resolution_round: 5\n\n- id: \"R4-W1\"\n  summary: \"Multiple testing correction\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"BH correction computed: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s. Integrated into §6.\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Eff-K Kish (1965) attribution / κ→ICC proxy rigor\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 10\n  resolution: \"Pairwise Pearson r (mean 0.625, Mistral-7B) monotonically related to κ across 4 model families. κ validated as consensus proxy.\"\n  resolution_round: 7\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N2(Critical): Both reviewers re-raise. Paper has ordinal caveat but uses K_eff quantitatively elsewhere. Need ICC values + sensitivity analysis.\"\n\n- id: \"R4-M5\"\n  summary: \"Figure 2 old data\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  resolution: \"Figure 2 moved to Appendix in V2 page budget compression.\"\n  resolution_round: 6\n\n- id: \"R5-N1\"\n  summary: \"Oracle ceiling '24%' cross-model comparison invalid\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Mistral-7B same-model oracle: +29.90pp (p<1e-13).\"\n  resolution_round: 5\n\n- id: \"R5-N2\"\n  summary: \"§4.1 Decoupling interim results (n=70/204) in main text\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"V2 framing removes §4.1 Decoupling from main text entirely.\"\n  resolution_round: 5\n\n- id: \"R5-N3\"\n  summary: \"'Fundamental' trade-off overclaimed\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All 'fundamental' → 'persistent' + 'at the 7B--32B scale'.\"\n  resolution_round: 5\n\n- id: \"R5-N4\"\n  summary: \"DeBERTa PoC statistically fragile — 9 discordant pairs\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"ProofWriter w=3 +3.50pp (p=0.013, n=600) as primary finding.\"\n  resolution_round: 5\n\n- id: \"R5-N5\"\n  summary: \"Discussion/Conclusion too thin for negative paper\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Discussion ~350 words, Conclusion ~220 words.\"\n  resolution_round: 5\n\n- id: \"R5-W1\"\n  summary: \"Variable name isolation confound\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Alpha-equivalence caveat added in Discussion.\"\n  resolution_round: 5\n\n- id: \"R5-W2\"\n  summary: \"Fleiss' κ as ICC proxy lacks formal justification\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 6\n  resolution: \"Caveat added. Pairwise correlation validates κ (tracked under R4-W3).\"\n  resolution_round: 5\n\n- id: \"R5-W3\"\n  summary: \"Missing ensemble diversity literature\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Krogh & Vedelsby (1994) + Brown et al. (2005) cited.\"\n  resolution_round: 5\n\n- id: \"R5-W4\"\n  summary: \"§3/§5 content duplication\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Not flagged in R6 — considered resolved.\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"'25+ strategies' count inflated\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"'more than twenty spanning fifteen distinct families'.\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"Code/data release not mentioned\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"Reproducibility paragraph added.\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Solutions before Experiments ordering\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"main.tex reordered correctly.\"\n  resolution_round: 5\n\n- id: \"R5-W8\"\n  summary: \"TF-IDF cosine limitation under-discussed\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"Deferred to rebuttal. SBERT validation not worth GPU time per Reviewer assessment.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers re-raised: R1-W5 notes Figure 2 R²≈4.4% is very low; R2-Q4 asks if TF-IDF sufficiently captures semantic similarity. Limitation persists.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R1-W5(Info), R2-W7(Info): TF-IDF limitation re-confirmed by both reviewers. Consensus: acknowledged limitation, not blocking.\"\n    - round: 10\n      reviewers: []\n      note: \"R10: Not directly re-raised but still applicable.\"\n\n- id: \"R5-W9\"\n  summary: \"CJT novelty / Huang-Stechly distinction insufficient\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"Paper Agent added novelty differentiation paragraph (3 quantitative differentiators). Tracked jointly with R6-N3.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W1 re-raised novelty concern despite R7 fix. R1 partially rebuts, citing empirical specificity and quantitative tools. Divergence remains — see R8-W1.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R2-W1(Critical): Novelty gap persists. R1 partially rebuts (Z3 non-triviality + exhaustive remediation). Core divergence: R1=3.5 vs R2=3.0.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N1(Critical): Re-raised by R2, R1 partially rebuts but agrees distinction needs more prominence. Core novelty divergence persists (R1=3.5 vs R2=3.0).\"\n\n- id: \"R5-TC1\"\n  summary: \"SC tiebreaking inconsistency (dict-order vs alphabetical)\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"All tiebreaking standardized to alphabetical.\"\n  resolution_round: 5\n\n- id: \"R6-N1\"\n  summary: \"Statistical power 5.7%-20.6% — title 'Fail' overclaims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Title changed to 'Do Not Improve'. TOST computed: 4/15 equivalence, 5/15 genuine difference (4 negative), 6/15 underpowered.\"\n  resolution_round: 7\n\n- id: \"R6-N2\"\n  summary: \"Cross-arch PoC p=0.013 needs multiple comparison correction\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"BH correction: PW w=3 (adj p=0.038) + PW w=5 (adj p<0.001) survive. FOLIO all n.s.\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Novelty vs self-correction literature (Huang/Stechly/Amonkar)\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"Novelty paragraph added (3 differentiators). §3.3 empirical bound further differentiates.\"\n  resolution_round: 7\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W1 re-raised novelty concern despite R7 fix.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9 R2-W1(Critical): Novelty gap persists.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: R2-N1 re-raises. R1 rebuts (Z3 formal verification is non-trivial test) but agrees distinction needs more prominence. Tracked jointly with R5-W9.\"\n\n- id: \"R6-W1\"\n  summary: \"Bias ratio numbers inconsistent between main text and Table 14\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Paper Agent clarified BR calculation scope.\"\n  resolution_round: 7\n\n- id: \"R6-W2\"\n  summary: \"Type A/B/C failure mode classification is post-hoc\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Labeled as 'three empirical regimes (observation-driven)'.\"\n  resolution_round: 7\n\n- id: \"R6-W3\"\n  summary: \"Degeneration condition (Eq. 4) derivation incomplete\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Constraint rejection rate 3.44% integrated as empirical evidence.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"'Symbolic Mirage' terminology too marketing-like\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"Scoping sentence added. §3.3 contrasts with independently sourced constraints.\"\n  resolution_round: 7\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R9 R2-W6: Terminology branding re-raised.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R10: R2 notes 'Symbolic Mirage' introduced in §3.3 but rarely reused; relationship with 'Symbolic Confirmation Bias' unclear.\"\n\n- id: \"R6-W5\"\n  summary: \"α=0.5 penalty weight lacks sensitivity analysis\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"α sensitivity: max 0.49pp variation across α∈{0.0-1.0}.\"\n  resolution_round: 7\n\n- id: \"R6-W6\"\n  summary: \"GSM8K (n=30) and AIME (n=22) in main Table 1 misleading\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Kept with † marker and 'suggestive only' caveat.\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Orphan bib entry (press2023compositionality)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"press2023compositionality removed.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"Reasoning models not discussed as category in Related Work\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Reasoning models paragraph with κ=0.91 homogenization added.\"\n  resolution_round: 7\n\n- id: \"R6-V1\"\n  summary: \"Page 20 >75% empty white space\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  resolution: \"Page 20 now ~60% filled.\"\n  resolution_round: 7\n\n- id: \"R6-V2\"\n  summary: \"Main text only 5 display items\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Figure swap complete. Main text §5.5 now has intervention summary figure.\"\n  resolution_round: 8\n\n- id: \"R8-N1\"\n  summary: \"FOL terminology misleading — actual constraints are predominantly propositional\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"All 'FOL' → 'logical constraints'. Quantifier proportion added.\"\n  resolution_round: 8\n\n- id: \"R8-N2\"\n  summary: \"Cross-architecture PoC underpowered: single generator × inconsistent dataset results\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§6 restructured. Clean single-generator evidence retained.\"\n  resolution_round: 8\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R9: NLI weight w not cross-validated; cross-arch scale insufficient.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: Both reviewers agree NLI escape too narrow (BH 2/12 survive). Consensus: narrow PoC, not general solution.\"\n\n- id: \"R8-W1\"\n  summary: \"Incremental novelty relative to Huang/Stechly\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"§2 para 5 articulates 3 quantitative differentiators.\"\n  resolution_round: 8\n\n- id: \"R8-W2\"\n  summary: \"Seed replication inconsistency\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Table 1 has $^{4s}$ superscript.\"\n  resolution_round: 8\n\n- id: \"R8-W3\"\n  summary: \"Semantic deduplication missing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"§3.2 reports 46.0% dedup ratio. Z3 semantic dedup discussed.\"\n  resolution_round: 8\n\n- id: \"R8-W4\"\n  summary: \"Domain diversity + model range overclaimed in Abstract\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Abstract scope accurately reflects 7B-32B.\"\n  resolution_round: 8\n\n- id: \"R8-W5\"\n  summary: \"Constraint quality analysis based on single model family\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Scoped in extended limitations.\"\n  resolution_round: 8\n\n- id: \"R8-W6\"\n  summary: \"Symbolic Confirmation Bias lacks connection to Turpin et al. unfaithful CoT\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Turpin connection present in §3.3 and Discussion.\"\n  resolution_round: 8\n\n- id: \"R8-I1\"\n  summary: \"Missing references: Weng et al. (2023) Self-Verification and Madaan et al. (2023) Self-Refine\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Both citations added.\"\n  resolution_round: 8\n\n- id: \"R8-I2\"\n  summary: \"Figure 5 buried in Appendix\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Figure swap complete.\"\n  resolution_round: 8\n\n- id: \"R8-I3\"\n  summary: \"83.3% confirmation bias rate needs per-model breakdown\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Per-model BR already reported in §5.2.\"\n  resolution_round: 8\n\n# =========================================================\n# Round 9 issues — status updated based on R10 findings\n# =========================================================\n\n- id: \"R9-W1\"\n  summary: \"Table 1 显著性声称缺少多重比较校正（16 条件未做 BH）\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"Table 1 now includes BH correction (m=16). Both PW conditions show adj p=0.112. Caption notes 'BH adj. p'.\"\n  resolution_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 raised, R2 agrees.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: Table 1 caption explicitly shows BH adj p=0.112. Resolved.\"\n\n- id: \"R9-W2\"\n  summary: \"κ→Effective-K 映射形式化不足\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W2 raised, R2 agrees.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N2(Critical): Re-raised as critical by both reviewers. Paper has ordinal caveat (§3.1) but uses K_eff quantitatively elsewhere. Need ICC + sensitivity.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: (a) report ICC values, (b) add sensitivity analysis comparing K_eff from κ vs ICC, (c) enforce ordinal usage consistently\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W3\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W3 raised, R2 agrees.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10: Subsumed under broader cross-arch narrowness concern. w=3 reported as primary but selection on test set.\"\n\n- id: \"R9-W4\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Sigmoid fit overfitting concern.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N3(Critical): Both agree. 'perfectly monotonic' based on n=6 non-independent points. R2 notes selective inclusion risk. Must downgrade to 'consistent directional trend'.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: downgrade 'perfectly monotonically' to 'strongly monotonically' or 'consistent directional trend', acknowledge n=6 limitation explicitly\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W5\"\n  summary: \"T_ext=0.3 extraction temperature 缺 sensitivity analysis\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Extraction temperature sensitivity missing.\"\n    - round: 10\n      reviewers: []\n      note: \"R10: Not directly re-raised but still applicable.\"\n\n- id: \"R9-W6\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W1(Critical), R1 partial rebut.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N1(Critical by R2): Core divergence. R1 rebuts (Z3 formal verification non-trivial), R2 maintains instantiation view. Director sides with R2: novelty insufficient for main conference, adequate for Findings.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: strengthen §1/§2 distinction from Huang/Stechly — emphasize Z3 formal verification channel as non-trivial test of neurosymbolic assumption\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W7\"\n  summary: \"Independence-Accuracy Trade-off 作为贡献存在部分同义反复\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-W2(Critical), R1 agrees on reordering contributions.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-W1: R2 re-raises, R1 rebuts (contribution is quantitative boundary κ≥0.40, not the principle). Partial divergence.\"\n\n- id: \"R9-W8\"\n  summary: \"遗漏关键相关工作：SatLM 对比不充分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"SatLM/VeriCoT/CRITIC 引用建议.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-N2(Critical by R2): SatLM comparison exists (2 sentences in §2) but insufficient. Both agree specification-generation vs trace-extraction distinction needs systematic expansion.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: expand SatLM comparison in §2 or §7 with specification-generation / program-generation / trace-extraction taxonomy\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W9\"\n  summary: \"Abstract 'sixteen' vs §4.2 'fifteen' 数字不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Table 1 有 16 个 non-degenerate 行，§4.2 'fifteen' 为笔误。\"\n    - round: 10\n      reviewers: []\n      note: \"R10: Not re-raised but still needs fix.\"\n\n- id: \"R9-W10\"\n  summary: \"Cross-architecture escape 实验规模不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"缺少与其他外部验证方法的对比.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-W2(R1)/W5(R2): Both strongly agree. BH 2/12 survive. NLI only works on premise-conclusion tasks with positive capability gap. Narrow PoC consensus.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: explicitly frame as narrow PoC in §6 and Limitations, discuss NLI applicability conditions\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R9-W11\"\n  summary: \"术语品牌化过多\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"'capability trap' 应弱化.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R10: R2 notes 'Symbolic Mirage' introduced §3.3 but rarely reused; unclear relationship with 'Symbolic Confirmation Bias'.\"\n\n- id: \"R9-W12\"\n  summary: \"σ(c,a) provenance-based 设计未作为 design limitation 讨论\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-3 连续 3 页纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"R10 Visual Check confirms: pages 3-5 连续无 figure/table.\"\n\n- id: \"R9-VL4\"\n  summary: \"Page 8 Conclusion 仓促\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [2]\n      note: \"R10: R2 notes Conclusion is compressed.\"\n\n# =========================================================\n# Round 10 (fresh review) — new issues\n# =========================================================\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both reviewers identify: Proposition 1 has no proof, '≲' imprecise, proof sketch belongs to Corollary 1. R2 adds Δ_oracle definition depends on experimental setup not math. Consensus: downgrade to Empirical Finding or provide formal proof.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: either provide complete proof in Appendix or downgrade to 'Empirical Finding 1' with explicit assumptions\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱，ordinal caveat 与 quantitative usage 矛盾\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. Kish (1965) uses ICC not κ. Paper has ordinal caveat but K_eff used quantitatively in abstract/§5.1. Need ICC values + sensitivity.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: (a) report ICC values alongside κ, (b) sensitivity analysis in Appendix, (c) enforce ordinal interpretation consistently\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. 3 NLI arch × 2 generator levels, non-independent. R2 notes selective inclusion risk. n=9 robustness check (ρ=0.836) more honest.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: downgrade 'perfectly monotonically' → 'strongly monotonically', report n=9 result as primary, acknowledge n=6 limitation\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. τ=0.7 selected and evaluated on same ProofWriter n=600. '90% recovery at 39% cost' may be overfitted.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: add dev/test split or cross-dataset τ validation, or explicitly flag as oracle selection\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄 (BH 2/12 survive)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Strong consensus. Only works: weak generator + premise-conclusion decomposable + verifier>generator. LogiQA ineffective. Narrow PoC.\"\n  action_items:\n    - round: 10\n      action: \"Paper Agent: frame as narrow PoC not general escape, discuss applicability conditions explicitly\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 raises, R2 agrees with nuance (not sole evidence pillar). Power limitation should be more prominent in main text.\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. No justification for why 2pp is the practical significance threshold. Need sensitivity across margins.\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Both agree. BR values (4.97×, 3.93×, 2.88×) lack CIs. Bootstrap CI is standard and low-cost.\"\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 raises as critical. R1 notes paper has 2 sentences but agrees needs expansion. Need systematic taxonomy in §2 or §7.\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N3 raises. R1 agrees. Key distinction: bias survives formal Z3 verification. Need to cite arXiv:2506.12301 + arXiv:2604.02485 and differentiate.\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W2 raises, R1 agrees. Neurosymbolic paragraph mixes specification-generation/program-generation/trace-extraction without taxonomy.\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W4 raises, R1 agrees. §5.4 仅 5 行文字 + Figure 2. Need representative strategy discussion in main text.\"\n\n- id: \"R10-I1\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W1 raises, R1 rebuts (quantitative boundary κ≥0.40 is the contribution, not the principle). Partial divergence.\"\n\n- id: \"R10-I2\"\n  summary: \"缺失引用：CoT confirmation bias 文献 + Eidoku + Tree of Thoughts\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 suggests arXiv:2506.12301, arXiv:2604.02485, arXiv:2512.20664. R1 suggests ToT (Yao 2023). R2 rebuts Khalifa (2023) as not critical.\"\n\n- id: \"R10-VL1\"\n  summary: \"Pages 3-5 连续无 display item；page 7 display items 过度拥挤\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Visual check: pages 3-5 pure text; page 7 has 4 display items stacked. Figure 2 y-axis labels ≤6pt.\""
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-21T06:49:22.845751+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 31938}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-21T06:51:29.394519+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0",
  "report": "# 审稿报告（Round 10 — Fresh Review）\n\n**论文**: *Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*\n**Venue**: EMNLP 2026 (via ACL Rolling Review) — Long Paper\n**ARR Deadline**: 2026-05-25\n\n---\n\n## Summary\n\n本文研究自提取符号约束能否突破 Self-Consistency (SC) 的性能天花板。作者提出 SICA（Symbolic Invariant Consensus Aggregation），从 CoT 推理轨迹中提取形式逻辑约束并通过加权 Partial MAX-SAT (Z3) 选择答案。在 6 个模型（7B-32B）、3 个逻辑推理数据集 + 3 个辅助数据集、3,000+ 条件评估上，自提取约束均未显著改善 SC（BH 校正后无条件达到显著）。作者将失败归因为 \"Symbolic Confirmation Bias\"（错误问题上 83.3% 约束支持错误多数答案，BR=4.97×），识别出 independence-accuracy trade-off（同模型 κ≥0.40 ceiling），并测试了 27 种修复策略（全部失败）。Oracle 控制确认机制本身有效（+29.90pp, +14.22pp FOLIO）。跨架构 DeBERTa NLI 验证在弱 generator 上显著有效（+6.67pp ProofWriter, p<0.001），DRC 以 39% 验证成本恢复 90% 增益。\n\n---\n\n## Strengths\n\n1. **穷举式负面结果令人信服**：27 种补救策略横跨 15 个方法族（prompt-level, method-level, solver-level, diversity-level），系统性地关闭了\"也许换策略就行\"的反驳空间。这是该领域对 self-extraction 最全面的实验评估。\n\n2. **Oracle 控制实验设计精良**：用 FOLIO gold FOL 和 ProofWriter DSL 替换自提取约束，在相同 MAX-SAT 管道下获得 +29.90/+14.22/+11.50pp 增益（p < 10⁻⁷），干净地隔离了\"约束质量\"这一瓶颈变量。这是论文方法论上最强的部分。\n\n3. **多层次诊断体系**：answer-level κ、process-level cosine similarity、confirmation bias ratio、C₀ diagnostic、entropy decomposition 从不同角度三角验证同一结论。统计处理（McNemar + BH FDR + TOST + Bootstrap CI + Power Analysis）在 NLP 论文中罕见地严谨。\n\n4. **CJT 理论框架有启发性**：用 Condorcet Jury Theorem 的独立性条件分析 SC 的失败模式，为理解 LLM 采样局限性提供了清晰的理论透镜。\n\n5. **建设性方案缓解纯负面问题**：DeBERTa NLI escape + DRC 展示了\"怎样才行得通\"，DRC 以 39% cost 恢复 90% gain 有实用价值。\n\n6. **可重复性高**：完整 prompt 模板、算法伪代码、22 个 Appendix section，代码承诺开源。\n\n---\n\n## Weaknesses\n\n### Critical（Must-Fix，影响接收决定）\n\n**C1. Proposition 1（Self-Extraction Ceiling）无证明** [R1-N1, R2-W3 — 共识]\n- §3.3 的 Proposition 1 声称 Δ_max^self ≲ Δ_oracle / BR(M)，但全文无证明或推导。\"≲\" 不精确（上界？渐近？近似？）。Page 5 的 \"proof sketch\" 实际论证的是 Corollary 1 的单调性，非 Proposition 1。Δ_oracle 的定义依赖于实验设置而非纯数学构造——这是 \"empirical claim dressed as theorem\"。\n- **必须**：提供完整证明（可放 Appendix）或降级为 \"Empirical Finding\"。\n\n**C2. κ→Effective-K 映射理论基础不足** [R1-N2, R2 交叉同意 — 共识]\n- Kish (1965) design effect 公式使用 ICC，非 Fleiss' κ。论文以 r=0.625 验证，仅中等相关（~61% 方差未被解释）。§3.1 有 ordinal diagnostic caveat，但 Abstract (\"K_eff ≈ 1.20-3.62\") 和 §5.1 中 K_eff 被作为定量指标使用——ordinal caveat 与 quantitative usage 矛盾。\n- **必须**：(a) 报告 ICC 值并与 κ 对比；(b) Appendix 中提供 sensitivity analysis；(c) 全文统一为 ordinal 使用。\n\n**C3. Capability gap \"perfectly monotonic\" 结论依赖 n=6 非独立数据点** [R1-N3, R2 交叉同意 — 共识]\n- Spearman ρ=1.0 基于 6 个 verifier-generator pairs（3 NLI 架构 × 2 有效 generator 水平），非完全独立（共享 Mistral-7B traces 和 DeBERTa verifier）。n=9 robustness check (ρ=0.836, p=0.007) 更诚实。R2 指出可能存在选择性纳入显著结果的循环论证风险。\n- **必须**：将 \"perfectly monotonically\" 降级为 \"strongly monotonically\" 或 \"consistent directional trend\"；以 n=9 result 为主；显式承认 n=6 局限。\n\n**C4. 相对于 Huang et al. (2024) / Stechly et al. (2025) 的增量新颖性论证不足** [R2-N1, R1 部分 REBUT — 分歧]\n- 核心发现——\"自提取约束继承模型偏差\"——与 Huang (LLMs cannot self-correct) 和 Stechly (self-verification limitations) 的已知结论在概念层面高度一致。R1 REBUT 指出 Z3 formal verification channel 使其非平凡（neurosymbolic 社区假设\"形式化 → 可靠\"），但 R2 认为这仍是 instantiation 而非 fundamental discovery。\n- **Director 判断**：R1 的 Z3 论据有道理——formal verification 下偏差仍存在确实比 NL self-correction 更令人惊讶。但论文当前仅用 §1 中 2 句话区分，远不够显著。如果这个区分无法在修改中变得足够有说服力，则论文的 Excitement 不足以支撑主会议。\n- **必须**：在 §1 和 §2 中用 1-2 段显式论证：(a) 为什么 Z3 formal verification 不同于 NL self-correction；(b) neurosymbolic 社区的隐含假设是什么；(c) 本文如何挑战该假设。\n\n**C5. SatLM 正面结果与 SICA 负面结果的对比不充分** [R2-N2, R1 部分 REBUT — 共识需扩展]\n- SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM+SAT solver 但报告正面结果。论文在 §2 中有 2 句话对比（specification-generation vs trace-extraction），但对理解\"为什么 SatLM works 而 SICA doesn't\"远不够充分。这个对比恰恰能强化论文论点：trace-level extraction 的 answer contamination 是结构性的。\n- **必须**：在 §2 或 §7 中系统化展开 specification-generation / program-generation / trace-extraction 三种范式的对比。\n\n---\n\n### Warning（Should-Fix，影响评分但不一票否决）\n\n**W1. DRC τ 阈值无 held-out 评估** [R1-W1, R2 同意 — 共识]\n- τ ∈ {0.3, 0.5, 0.7, 0.9} 均在同一 ProofWriter (n=600) 上选择和评估。作为第 4 个正式 contribution，\"90% recovery at 39% cost\" 可能 overfitted。\n- 建议：dev/test split 或跨数据集 τ 验证，或显式标注 oracle selection。\n\n**W2. Cross-architecture NLI escape 适用面极窄** [R1-W2, R2-W5 — 强共识]\n- BH 校正后仅 2/12 条件存活（均为 Mistral-7B ProofWriter）。NLI 仅适用于弱 generator + premise-conclusion 可分解 + verifier 强于 generator 的场景。LogiQA 无效。\n- 建议：显式框定为 narrow PoC，讨论适用条件，避免暗示 general escape。\n\n**W3. 四种子复制方差大 + 统计功效 <21%** [R1-W3, R2 有 nuance 地同意 — 共识]\n- Δ ∈ {+3.43, +2.94, 0.00, −0.49}pp。Power analysis 显示所有确认性条件观测功效 <21%。R2 补充：四种子不是唯一证据支柱（还有 15 条件 FDR null + oracle + 27 策略失败），但 power limitation 应在主文更显著。\n- 建议：在核心 claim 措辞中更明确承认 power limitation。\n\n**W4. TOST ±2pp margin 缺少显式理由** [R1-W4, R2 同意 — 共识]\n- 未论证 2pp 为何是合适的实际意义阈值。NLP 领域缺乏共识，但至少应讨论 SC 文献中的典型改进幅度并展示不同 margin 下的 sensitivity。\n\n**W5. Bias Ratio 无置信区间** [R1-W5, R2 同意 — 共识]\n- BR (4.97×, 3.93×, 2.88×) 缺 CI。Bootstrap CI 计算成本极低。无 CI 则无法判断跨模型 BR 差异是否显著。\n\n**W6. \"Symbolic Confirmation Bias\" 需与近期 CoT confirmation bias 工作区分** [R2-N3, R1 同意 — 共识]\n- 近期 arXiv:2506.12301 和 arXiv:2604.02485 已研究 CoT confirmation bias。本文的特殊性——偏差在 Z3 satisfiability 验证后仍存在——需要更清晰地表述。\n\n**W7. Related Work 过度压缩** [R2-W2, R1 同意 — 共识]\n- 三段 Related Work 将约 25 篇论文压缩为引用列表。Neurosymbolic 段混合 specification-generation / program-generation / trace-extraction 未分类。\n\n**W8. 27 种修复策略正文展示不足** [R2-W4, R1 同意 — 共识]\n- §5.4 仅 5 行文字 + Figure 2 概览。作为核心论证环节应在正文增加代表性策略的分类讨论。\n\n---\n\n### Info（小问题，不影响接收）\n\n- Independence-Accuracy Trade-off 作为独立贡献有 bias-variance tradeoff 重述嫌疑（R2-W1, R1 REBUT）\n- Table 1 信息密度极高，脚注系统复杂（b, †, 4s, *, ***），可读性可优化\n- \"Symbolic Mirage\" 引入后极少复用，与 \"Symbolic Confirmation Bias\" 的层次关系不清\n- Abstract 约 250 词偏长（可接受但可精简）\n- §5.1 标题 \"Condorcet Effective-K\" 中 K 与 κ (kappa) 容易混淆\n- 缺失引用：CoT confirmation bias 文献 (arXiv:2506.12301, arXiv:2604.02485)、Eidoku (arXiv:2512.20664)、Tree of Thoughts (Yao et al., 2023)\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（[AGREE] 或 REBUT 后达成一致方向）：\n- [AGREE] Proposition 1 无证明，需降级或补证（C1）\n- [AGREE] κ→K_eff 映射理论基础弱，需 ICC + sensitivity（C2）\n- [AGREE] n=6 capability gap 需降级措辞（C3）\n- [AGREE] SatLM 对比需扩展（C5）\n- [AGREE] SCB 术语需与 CoT confirmation bias 区分（W6）\n- [AGREE] DRC 无 held-out（W1）\n- [AGREE] Cross-arch escape 太窄（W2）\n- [AGREE] TOST margin 无理由（W4）\n- [AGREE] BR 无 CI（W5）\n- [AGREE] Related Work 压缩（W7）\n- [AGREE] 27 策略正文不足（W8）\n\n## Reviewer Divergence\n\n**核心分歧：新颖性权重 → Overall 评分**\n- **R1 (3.5, Borderline Conference)**：更看重实验的严谨性和 27 策略穷举。认为 Z3 formal verification 使其非平凡推广，κ≥0.40 定量边界超越已知原理。\n- **R2 (3.0, Findings)**：更看重概念新颖性。认为核心发现对熟悉 self-correction 文献的读者可预测，诊断指标是已有度量的直接应用。\n- **Director 判断**：论文的实验贡献优秀，但概念增量相对于 Huang/Stechly 有限。Z3 formal verification channel 确实是更强的测试条件，但论文未充分发挥这一区分。当前版本更适合 Findings。\n\n---\n\n## Questions for Authors\n\n1. SatLM 使用 LLM+SAT solver 但报告正面结果，关键区别是否在于 specification-generation vs trace-extraction？如果是，请在论文中系统化讨论。\n2. Proposition 1 的 \"≲\" 是严格上界还是近似？能否提供形式化证明？\n3. 如果用 ICC 替代 κ 计算 K_eff，排序和结论是否改变？\n4. DRC 的 τ=0.7 在 FOLIO 上是否同样是最优？\n5. Reasoning model（Qwen3 thinking mode, κ=0.91）是否改变了 confirmation bias 的性质？\n\n---\n\n## Missing References\n\n1. **\"Unveiling Confirmation Bias in Chain-of-Thought Reasoning\"** (arXiv:2506.12301, Jun 2025) — CoT confirmation bias，与 SCB 概念直接相关\n2. **\"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models\"** (arXiv:2604.02485, Apr 2026) — LLM confirmation bias 系统评估\n3. **\"Eidoku: Neuro-Symbolic Verification Gate via Structural Constraint Satisfaction\"** (arXiv:2512.20664, Dec 2025) — 约束满足验证，与 Z3 MAX-SAT 相关\n4. **Yao et al. (2023) \"Tree of Thoughts\"** — structured test-time search，self-evaluation 也面临偏差\n5. **SatLM (Ye et al., NeurIPS 2023)** — 已引用但讨论不足，需系统化展开对比\n\n---\n\n## External Review\n\n外部审稿未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warning, 5 info, 0 critical）：\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | Pages 3-5 | 连续 3 页无 figure/table，建议在 page 5 实验 setup 处加 summary table |\n| ⚠️ Warning | Page 7 | Display items 过度拥挤（Table 2 + Figure 2 + Figure 3 + Table 3 共 4 个），建议分散 |\n| ⚠️ Warning | Page 7 | Figure 2（27 策略条形图）y 轴标签 ≤6pt，打印后难以辨认，建议改 figure* 全宽 |\n| ℹ️ Info | Page 1 | 首页无视觉锚点，建议加 teaser figure |\n| ℹ️ Info | Page 2 | Figure 1 pipeline 图内文字偏小 |\n| ℹ️ Info | Page 5 | 实验 setup 纯文本呈现，建议 setup table |\n| ℹ️ Info | Page 7 | Figure 3 legend/axis label 字号偏小 |\n| ℹ️ Info | Page 22 | 末页底部约 1/3 空白 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分理由**：\n- **Soundness (3.5/5)**：核心负面结论有充分实验支撑（6 模型 × 3+ 数据集 × 27 策略全部失败 + oracle 对照）；但 Proposition 1 无证明、κ→K_eff 映射理论基础弱、Spearman ρ=1.0 基于 n=6。\n- **Excitement (2.5/5)**：核心发现对熟悉 self-correction 文献的读者部分可预测；Z3 formal verification channel 是更强的测试条件但未充分论证其非平凡性；DRC 有实用价值但适用范围窄。\n- **Reproducibility (4/5)**：方法描述清晰，Appendix 材料极充实，代码承诺开源。\n\n**Confidence: 4/5**\n\n**修改建议优先级**：\n1. [最高] 加强 Huang/Stechly 区分 + SatLM 对比（C4, C5）— 这决定了论文能否从 Findings 升级到 Borderline Conference\n2. [高] Proposition 1 降级或补证（C1）\n3. [高] κ→K_eff ICC sensitivity（C2）+ capability gap 措辞降级（C3）\n4. [中] DRC held-out + cross-arch framing + BR CI（W1, W2, W5）\n5. [中] Related Work 扩展 + 27 策略正文展示（W7, W8）\n6. [低] TOST margin + SCB 术语区分 + 视觉布局（W4, W6, VL）\n\n**Venue Fit**：当前版本 **适合 Findings**，主会议需要在新颖性论证（C4）上有实质性突破。如果修改后能充分论证 Z3 formal verification channel 为何构成对 neurosymbolic 社区核心假设的非平凡挑战，评分可能提升至 3.5 (Borderline Conference)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0",
    "report": "# 审稿报告（Round 10 — Fresh Review）\n\n**论文**: *Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Do Not Improve LLM Reasoning*\n**Venue**: EMNLP 2026 (via ACL Rolling Review) — Long Paper\n**ARR Deadline**: 2026-05-25\n\n---\n\n## Summary\n\n本文研究自提取符号约束能否突破 Self-Consistency (SC) 的性能天花板。作者提出 SICA（Symbolic Invariant Consensus Aggregation），从 CoT 推理轨迹中提取形式逻辑约束并通过加权 Partial MAX-SAT (Z3) 选择答案。在 6 个模型（7B-32B）、3 个逻辑推理数据集 + 3 个辅助数据集、3,000+ 条件评估上，自提取约束均未显著改善 SC（BH 校正后无条件达到显著）。作者将失败归因为 \"Symbolic Confirmation Bias\"（错误问题上 83.3% 约束支持错误多数答案，BR=4.97×），识别出 independence-accuracy trade-off（同模型 κ≥0.40 ceiling），并测试了 27 种修复策略（全部失败）。Oracle 控制确认机制本身有效（+29.90pp, +14.22pp FOLIO）。跨架构 DeBERTa NLI 验证在弱 generator 上显著有效（+6.67pp ProofWriter, p<0.001），DRC 以 39% 验证成本恢复 90% 增益。\n\n---\n\n## Strengths\n\n1. **穷举式负面结果令人信服**：27 种补救策略横跨 15 个方法族（prompt-level, method-level, solver-level, diversity-level），系统性地关闭了\"也许换策略就行\"的反驳空间。这是该领域对 self-extraction 最全面的实验评估。\n\n2. **Oracle 控制实验设计精良**：用 FOLIO gold FOL 和 ProofWriter DSL 替换自提取约束，在相同 MAX-SAT 管道下获得 +29.90/+14.22/+11.50pp 增益（p < 10⁻⁷），干净地隔离了\"约束质量\"这一瓶颈变量。这是论文方法论上最强的部分。\n\n3. **多层次诊断体系**：answer-level κ、process-level cosine similarity、confirmation bias ratio、C₀ diagnostic、entropy decomposition 从不同角度三角验证同一结论。统计处理（McNemar + BH FDR + TOST + Bootstrap CI + Power Analysis）在 NLP 论文中罕见地严谨。\n\n4. **CJT 理论框架有启发性**：用 Condorcet Jury Theorem 的独立性条件分析 SC 的失败模式，为理解 LLM 采样局限性提供了清晰的理论透镜。\n\n5. **建设性方案缓解纯负面问题**：DeBERTa NLI escape + DRC 展示了\"怎样才行得通\"，DRC 以 39% cost 恢复 90% gain 有实用价值。\n\n6. **可重复性高**：完整 prompt 模板、算法伪代码、22 个 Appendix section，代码承诺开源。\n\n---\n\n## Weaknesses\n\n### Critical（Must-Fix，影响接收决定）\n\n**C1. Proposition 1（Self-Extraction Ceiling）无证明** [R1-N1, R2-W3 — 共识]\n- §3.3 的 Proposition 1 声称 Δ_max^self ≲ Δ_oracle / BR(M)，但全文无证明或推导。\"≲\" 不精确（上界？渐近？近似？）。Page 5 的 \"proof sketch\" 实际论证的是 Corollary 1 的单调性，非 Proposition 1。Δ_oracle 的定义依赖于实验设置而非纯数学构造——这是 \"empirical claim dressed as theorem\"。\n- **必须**：提供完整证明（可放 Appendix）或降级为 \"Empirical Finding\"。\n\n**C2. κ→Effective-K 映射理论基础不足** [R1-N2, R2 交叉同意 — 共识]\n- Kish (1965) design effect 公式使用 ICC，非 Fleiss' κ。论文以 r=0.625 验证，仅中等相关（~61% 方差未被解释）。§3.1 有 ordinal diagnostic caveat，但 Abstract (\"K_eff ≈ 1.20-3.62\") 和 §5.1 中 K_eff 被作为定量指标使用——ordinal caveat 与 quantitative usage 矛盾。\n- **必须**：(a) 报告 ICC 值并与 κ 对比；(b) Appendix 中提供 sensitivity analysis；(c) 全文统一为 ordinal 使用。\n\n**C3. Capability gap \"perfectly monotonic\" 结论依赖 n=6 非独立数据点** [R1-N3, R2 交叉同意 — 共识]\n- Spearman ρ=1.0 基于 6 个 verifier-generator pairs（3 NLI 架构 × 2 有效 generator 水平），非完全独立（共享 Mistral-7B traces 和 DeBERTa verifier）。n=9 robustness check (ρ=0.836, p=0.007) 更诚实。R2 指出可能存在选择性纳入显著结果的循环论证风险。\n- **必须**：将 \"perfectly monotonically\" 降级为 \"strongly monotonically\" 或 \"consistent directional trend\"；以 n=9 result 为主；显式承认 n=6 局限。\n\n**C4. 相对于 Huang et al. (2024) / Stechly et al. (2025) 的增量新颖性论证不足** [R2-N1, R1 部分 REBUT — 分歧]\n- 核心发现——\"自提取约束继承模型偏差\"——与 Huang (LLMs cannot self-correct) 和 Stechly (self-verification limitations) 的已知结论在概念层面高度一致。R1 REBUT 指出 Z3 formal verification channel 使其非平凡（neurosymbolic 社区假设\"形式化 → 可靠\"），但 R2 认为这仍是 instantiation 而非 fundamental discovery。\n- **Director 判断**：R1 的 Z3 论据有道理——formal verification 下偏差仍存在确实比 NL self-correction 更令人惊讶。但论文当前仅用 §1 中 2 句话区分，远不够显著。如果这个区分无法在修改中变得足够有说服力，则论文的 Excitement 不足以支撑主会议。\n- **必须**：在 §1 和 §2 中用 1-2 段显式论证：(a) 为什么 Z3 formal verification 不同于 NL self-correction；(b) neurosymbolic 社区的隐含假设是什么；(c) 本文如何挑战该假设。\n\n**C5. SatLM 正面结果与 SICA 负面结果的对比不充分** [R2-N2, R1 部分 REBUT — 共识需扩展]\n- SatLM (Ye et al., NeurIPS 2023) 同样使用 LLM+SAT solver 但报告正面结果。论文在 §2 中有 2 句话对比（specification-generation vs trace-extraction），但对理解\"为什么 SatLM works 而 SICA doesn't\"远不够充分。这个对比恰恰能强化论文论点：trace-level extraction 的 answer contamination 是结构性的。\n- **必须**：在 §2 或 §7 中系统化展开 specification-generation / program-generation / trace-extraction 三种范式的对比。\n\n---\n\n### Warning（Should-Fix，影响评分但不一票否决）\n\n**W1. DRC τ 阈值无 held-out 评估** [R1-W1, R2 同意 — 共识]\n- τ ∈ {0.3, 0.5, 0.7, 0.9} 均在同一 ProofWriter (n=600) 上选择和评估。作为第 4 个正式 contribution，\"90% recovery at 39% cost\" 可能 overfitted。\n- 建议：dev/test split 或跨数据集 τ 验证，或显式标注 oracle selection。\n\n**W2. Cross-architecture NLI escape 适用面极窄** [R1-W2, R2-W5 — 强共识]\n- BH 校正后仅 2/12 条件存活（均为 Mistral-7B ProofWriter）。NLI 仅适用于弱 generator + premise-conclusion 可分解 + verifier 强于 generator 的场景。LogiQA 无效。\n- 建议：显式框定为 narrow PoC，讨论适用条件，避免暗示 general escape。\n\n**W3. 四种子复制方差大 + 统计功效 <21%** [R1-W3, R2 有 nuance 地同意 — 共识]\n- Δ ∈ {+3.43, +2.94, 0.00, −0.49}pp。Power analysis 显示所有确认性条件观测功效 <21%。R2 补充：四种子不是唯一证据支柱（还有 15 条件 FDR null + oracle + 27 策略失败），但 power limitation 应在主文更显著。\n- 建议：在核心 claim 措辞中更明确承认 power limitation。\n\n**W4. TOST ±2pp margin 缺少显式理由** [R1-W4, R2 同意 — 共识]\n- 未论证 2pp 为何是合适的实际意义阈值。NLP 领域缺乏共识，但至少应讨论 SC 文献中的典型改进幅度并展示不同 margin 下的 sensitivity。\n\n**W5. Bias Ratio 无置信区间** [R1-W5, R2 同意 — 共识]\n- BR (4.97×, 3.93×, 2.88×) 缺 CI。Bootstrap CI 计算成本极低。无 CI 则无法判断跨模型 BR 差异是否显著。\n\n**W6. \"Symbolic Confirmation Bias\" 需与近期 CoT confirmation bias 工作区分** [R2-N3, R1 同意 — 共识]\n- 近期 arXiv:2506.12301 和 arXiv:2604.02485 已研究 CoT confirmation bias。本文的特殊性——偏差在 Z3 satisfiability 验证后仍存在——需要更清晰地表述。\n\n**W7. Related Work 过度压缩** [R2-W2, R1 同意 — 共识]\n- 三段 Related Work 将约 25 篇论文压缩为引用列表。Neurosymbolic 段混合 specification-generation / program-generation / trace-extraction 未分类。\n\n**W8. 27 种修复策略正文展示不足** [R2-W4, R1 同意 — 共识]\n- §5.4 仅 5 行文字 + Figure 2 概览。作为核心论证环节应在正文增加代表性策略的分类讨论。\n\n---\n\n### Info（小问题，不影响接收）\n\n- Independence-Accuracy Trade-off 作为独立贡献有 bias-variance tradeoff 重述嫌疑（R2-W1, R1 REBUT）\n- Table 1 信息密度极高，脚注系统复杂（b, †, 4s, *, ***），可读性可优化\n- \"Symbolic Mirage\" 引入后极少复用，与 \"Symbolic Confirmation Bias\" 的层次关系不清\n- Abstract 约 250 词偏长（可接受但可精简）\n- §5.1 标题 \"Condorcet Effective-K\" 中 K 与 κ (kappa) 容易混淆\n- 缺失引用：CoT confirmation bias 文献 (arXiv:2506.12301, arXiv:2604.02485)、Eidoku (arXiv:2512.20664)、Tree of Thoughts (Yao et al., 2023)\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（[AGREE] 或 REBUT 后达成一致方向）：\n- [AGREE] Proposition 1 无证明，需降级或补证（C1）\n- [AGREE] κ→K_eff 映射理论基础弱，需 ICC + sensitivity（C2）\n- [AGREE] n=6 capability gap 需降级措辞（C3）\n- [AGREE] SatLM 对比需扩展（C5）\n- [AGREE] SCB 术语需与 CoT confirmation bias 区分（W6）\n- [AGREE] DRC 无 held-out（W1）\n- [AGREE] Cross-arch escape 太窄（W2）\n- [AGREE] TOST margin 无理由（W4）\n- [AGREE] BR 无 CI（W5）\n- [AGREE] Related Work 压缩（W7）\n- [AGREE] 27 策略正文不足（W8）\n\n## Reviewer Divergence\n\n**核心分歧：新颖性权重 → Overall 评分**\n- **R1 (3.5, Borderline Conference)**：更看重实验的严谨性和 27 策略穷举。认为 Z3 formal verification 使其非平凡推广，κ≥0.40 定量边界超越已知原理。\n- **R2 (3.0, Findings)**：更看重概念新颖性。认为核心发现对熟悉 self-correction 文献的读者可预测，诊断指标是已有度量的直接应用。\n- **Director 判断**：论文的实验贡献优秀，但概念增量相对于 Huang/Stechly 有限。Z3 formal verification channel 确实是更强的测试条件，但论文未充分发挥这一区分。当前版本更适合 Findings。\n\n---\n\n## Questions for Authors\n\n1. SatLM 使用 LLM+SAT solver 但报告正面结果，关键区别是否在于 specification-generation vs trace-extraction？如果是，请在论文中系统化讨论。\n2. Proposition 1 的 \"≲\" 是严格上界还是近似？能否提供形式化证明？\n3. 如果用 ICC 替代 κ 计算 K_eff，排序和结论是否改变？\n4. DRC 的 τ=0.7 在 FOLIO 上是否同样是最优？\n5. Reasoning model（Qwen3 thinking mode, κ=0.91）是否改变了 confirmation bias 的性质？\n\n---\n\n## Missing References\n\n1. **\"Unveiling Confirmation Bias in Chain-of-Thought Reasoning\"** (arXiv:2506.12301, Jun 2025) — CoT confirmation bias，与 SCB 概念直接相关\n2. **\"Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models\"** (arXiv:2604.02485, Apr 2026) — LLM confirmation bias 系统评估\n3. **\"Eidoku: Neuro-Symbolic Verification Gate via Structural Constraint Satisfaction\"** (arXiv:2512.20664, Dec 2025) — 约束满足验证，与 Z3 MAX-SAT 相关\n4. **Yao et al. (2023) \"Tree of Thoughts\"** — structured test-time search，self-evaluation 也面临偏差\n5. **SatLM (Ye et al., NeurIPS 2023)** — 已引用但讨论不足，需系统化展开对比\n\n---\n\n## External Review\n\n外部审稿未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warning, 5 info, 0 critical）：\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| ⚠️ Warning | Pages 3-5 | 连续 3 页无 figure/table，建议在 page 5 实验 setup 处加 summary table |\n| ⚠️ Warning | Page 7 | Display items 过度拥挤（Table 2 + Figure 2 + Figure 3 + Table 3 共 4 个），建议分散 |\n| ⚠️ Warning | Page 7 | Figure 2（27 策略条形图）y 轴标签 ≤6pt，打印后难以辨认，建议改 figure* 全宽 |\n| ℹ️ Info | Page 1 | 首页无视觉锚点，建议加 teaser figure |\n| ℹ️ Info | Page 2 | Figure 1 pipeline 图内文字偏小 |\n| ℹ️ Info | Page 5 | 实验 setup 纯文本呈现，建议 setup table |\n| ℹ️ Info | Page 7 | Figure 3 legend/axis label 字号偏小 |\n| ℹ️ Info | Page 22 | 末页底部约 1/3 空白 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分理由**：\n- **Soundness (3.5/5)**：核心负面结论有充分实验支撑（6 模型 × 3+ 数据集 × 27 策略全部失败 + oracle 对照）；但 Proposition 1 无证明、κ→K_eff 映射理论基础弱、Spearman ρ=1.0 基于 n=6。\n- **Excitement (2.5/5)**：核心发现对熟悉 self-correction 文献的读者部分可预测；Z3 formal verification channel 是更强的测试条件但未充分论证其非平凡性；DRC 有实用价值但适用范围窄。\n- **Reproducibility (4/5)**：方法描述清晰，Appendix 材料极充实，代码承诺开源。\n\n**Confidence: 4/5**\n\n**修改建议优先级**：\n1. [最高] 加强 Huang/Stechly 区分 + SatLM 对比（C4, C5）— 这决定了论文能否从 Findings 升级到 Borderline Conference\n2. [高] Proposition 1 降级或补证（C1）\n3. [高] κ→K_eff ICC sensitivity（C2）+ capability gap 措辞降级（C3）\n4. [中] DRC held-out + cross-arch framing + BR CI（W1, W2, W5）\n5. [中] Related Work 扩展 + 27 策略正文展示（W7, W8）\n6. [低] TOST margin + SCB 术语区分 + 视觉布局（W4, W6, VL）\n\n**Venue Fit**：当前版本 **适合 Findings**，主会议需要在新颖性论证（C4）上有实质性突破。如果修改后能充分论证 Z3 formal verification channel 为何构成对 neurosymbolic 社区核心假设的非平凡挑战，评分可能提升至 3.5 (Borderline Conference)。"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-21T06:51:34.474031+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5079
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-21T06:51:37.252291+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:CronDelete",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:CronDelete",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-21T06:51:37.302943+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-21T06:51:40.617213+00:00_

called CronDelete

<details open><summary>🔧 Tool call — CronDelete</summary>

```json
{
  "id": "a85199ed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "CronDelete",
  "tool_args": {
    "id": "a85199ed"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-21T06:51:40.667972+00:00_

&lt;tool_use_error>No scheduled job with id 'a85199ed'&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "CronDelete",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1016 · 2026-05-21T06:51:50.231457+00:00_

审稿报告已投递至 Research Director。

**Round 10 审稿完成摘要**：

- **Overall: 3.0 (Findings)**，Confidence 4/5
- **R1**: 3.5 (Borderline Conference) — 方法严谨性 + 实验设计
- **R2**: 3.0 (Findings) — 新颖性 + 完整性
- **核心分歧**：新颖性权重。R1 认为 Z3 formal verification 使论文非平凡，R2 认为是 self-correction failure 的 instantiation。Director 判定当前版本适合 Findings。
- **5 个 Critical**：Proposition 1 无证明、κ→K_eff 理论弱、capability gap n=6、新颖性论证不足、SatLM 对比不充分
- **8 个 Warning**：DRC 无 held-out、cross-arch 太窄、power <21%、TOST margin 无理由、BR 无 CI、SCB 术语区分、Related Work 压缩、27 策略展示不足
- **Issue Tracker 已同步更新**（R10-N1 至 R10-VL1，含 action items）
- **升级路径**：加强 Huang/Stechly 区分 + SatLM 系统对比 → 可能提升至 3.5 (Borderline Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 67

## Round 67

2 recorded events


### User

_source line 1017 · 2026-05-21T06:51:52.962280+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：与 Reviewer 1 在 7/8 个问题上一致。3 个 Must-Fix 全部同意（Proposition 1 无证明、κ→K_eff 近似过度使用、Spearman n=6 样本过小），5 个 Should-Fix 中 4 个同意+1 个有 nuance 同意。在 Missing References 上，同意 Tree of Thoughts 应引用，但不认为 Khalifa et al. 是关键遗漏。

两位 Reviewer 的主要分歧在评分：R1 给 3.5（Borderline Conference，侧重实验严谨性），我维持 3.0（Findings，侧重新颖性不足）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1018 · 2026-05-21T06:52:06.465501+00:00_

审稿报告已投递给 Research Director。

**本轮审稿总结**：

- **Overall Score: 3.0 (Findings)**
- **Reviewer 1**: 3.5 (Borderline Conference) — 侧重方法严谨性
- **Reviewer 2**: 3.0 (Findings) — 侧重新颖性
- **5 个 Critical 问题**：Proposition 1 无证明、κ→K_eff 理论基础弱、capability gap n=6 过小、Huang/Stechly 新颖性区分不足、SatLM 对比不充分
- **8 个 Warning 问题**：DRC 无 held-out、cross-arch escape 太窄、统计功效低、TOST margin 无理由、BR 无 CI、SCB 术语区分、Related Work 压缩、27 策略正文不足
- **Issue Tracker 已同步更新**（新增 13 个 R10 issues + 历史 issues 状态刷新）
- **视觉审查**：3 warning（pages 3-5 无 display item、page 7 拥挤、Figure 2 字号过小）

核心判断：实验执行出色，但概念增量有限。当前版本适合 Findings，主会议需在新颖性论证（Z3 formal verification 为何是对 neurosymbolic 核心假设的非平凡挑战）上有实质性突破。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 68

## Round 68

66 recorded events


### User

_source line 1019 · 2026-05-21T07:43:50.734590+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-21T07:43:57.067223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-21T07:43:57.118345+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-21T07:44:07.016530+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-21T07:44:07.067301+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-21T07:44:13.816261+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1025 · 2026-05-21T07:44:15.730587+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (149 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-text-ablation | Constraint extraction temperature (T_ext) affects SICA accuracy: moderate T_ext (0.3-0.5) produces more diverse yet valid constraints than extremes (0.1 too deterministic, 1.0 too noisy), yielding higher SICA-SC delta on FOLIO-204. | — | — | — |\n\n## 待处理\n- exp-077-generalization-kappa: Generalization: independence bottleneck (high κ) applies to Debate and Diverse-Prompt aggregation, not just SC+SICA. 在 Mistral-7B FOLIO-204 上测量 3 种聚合方式的 Fleiss' κ + Eff-K: (a) Standard SC (复用 exp-033 traces), (b) LLM-Debate traces (4组×3轮=12 answer points), (c) Diverse-Prompt traces (4种 prompt×3次=12). 如果三种方式 κ 均 > 0.4，证明 independence bottleneck 是 same-model aggregation 的通病。（准备中）\n- exp-063-llama8b-folio204（准备中）\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **exp_text_ablation** (success): Constraint extraction temperature (T_ext) does not significantly affect SICA accuracy because confirmation bias is inherent to self-extraction regardless of temperature — constraints at any T_ext will project the model's distributional bias rather than provide independent verification signal\n- **exp-092-llama8b-pw-nli-combo** (success): LLaMA
…[truncated 1770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1914
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-21T07:44:15.731261+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-21T07:44:16.636116+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\newtheorem{proposition}{Proposition}
14	\newtheorem{corollary}{Corollary}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints\\Do Not Improve LLM Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{6pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{6pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{4pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{4pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{3pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{5pt plus 2pt minus 3pt}
55	\setlength{\belowdisplayskip}{5pt plus 2pt minus 3pt}
56	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\input{conclusion}
75	
76	\section*{Limitations}
77	\input{limitations_content}
78	
79	\bibliography{references}
80	
8
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-21T07:44:16.636469+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-21T07:44:16.687729+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-21T07:44:26.238626+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 1031 · 2026-05-21T07:44:27.242941+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-21T07:44:29.153662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1033 · 2026-05-21T07:44:29.612784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-21T07:44:30.116029+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-21T07:44:34.986078+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines and information for EMNLP 2026:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Submission System and Deadlines

Papers must be submitted by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed to EMNLP via the commitment link. The key dates are:

- ARR submission deadline (long & short papers): May 25, 2026
- Reviewer re
…[truncated 919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 8747
}
```

</details>

---


### Tool result

_source line 1036 · 2026-05-21T07:44:34.986595+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7743
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-21T07:44:34.986863+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 4870
}
```

</details>

---


### Tool result

_source line 1038 · 2026-05-21T07:44:34.987177+00:00_

1	Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
2	We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
3	Across six open-source LLMs (7B--32B, from Mistral-7B at 54\% SC to Qwen3-14B thinking mode at 86\% SC) and three logical reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find that self-extracted constraints do not improve majority voting at any capacity level: none of sixteen non-degenerate conditions shows a significant effect after FDR control (Benjamini--Hochberg, $m{=}16$); TOST equivalence tests (margin $\pm 2$\,pp) establish equivalence for four conditions, while two show genuine differences---both negative.
4	We identify \emph{symbolic confirmation bias} as the root cause: on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratio $4.97\times$), and 94\% of errors overlap with SC.
5	Process-level analysis reveals a deeper bottleneck: chain-of-thought cosine similarity ($0.69$) far exceeds answer-level Fleiss' $\kappa$ ($0.46$), indicating that traces share reasoning processes even when they diverge on answers.
6	Twenty-seven same-model remediation strategies spanning fifteen families all fail, revealing a persistent independence-accuracy trade-off at the 7B--32B scale: methods that increase trace independence destroy accuracy (Debate: $\kappa = 0.15$, $-18.6$\,pp), while methods preserving accuracy cannot break the correlation floor ($\kappa \geq 0.40$ across three model families).
7	Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp and $+14.22$\,pp on FOLIO, $+11.50$\,pp ProofWriter; $p < 0.001$); same-model self-extraction captures only ${\sim}$12\% of the 
…[truncated 527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 5833
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-21T07:44:34.987604+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\text{eff}}$ that reveals near-deterministic voting dynamic
…[truncated 6186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 5374
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-21T07:44:43.682033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-21T07:44:43.732698+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and extensions.}
5	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).
6	
7	\paragraph{Neuro-symbolic reasoning.}
8	We distinguish three paradigms. \emph{Specification-generation} (Logic-LM \citep{pan2023logiclm}, LINC \citep{olausson2023linc}, SatLM \citep{ye2024satlm}) translates problem descriptions into formal specifications before any answer is generated; LINC documents ${\sim}$40\% translation errors even at this level. \emph{Program-generation} \citep{gao2023pal,chen2023program,lyu2023faithful} produces executable code from problem statements. Both paradigms access the problem before generating candidate answers. \emph{Trace-extraction} (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). SatLM provides a natural control: it succeeds because problem-level formalization precedes answer generation, whereas trace-level extraction cannot avoid contamination (\S\ref{sec:mirage}). Recent extensions \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent, miya2025eidoku} introduce capabilities beyond the reasoning model. \citet{amonkar2025realitycheck} show formalization degrades with complexity; \citet{chan2026position} argue logical soundness is unreliable for neurosymbolic verification. Our oracl
…[truncated 3096 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-21T07:44:43.783475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---
