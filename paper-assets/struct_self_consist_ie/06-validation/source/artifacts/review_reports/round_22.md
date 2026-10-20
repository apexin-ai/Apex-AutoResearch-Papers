---
round: 22
review_mode: 
overall_score: weak accept (findings) / borderline (main conference)
timestamp: 2026-05-19T05:08:34.276009+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 23

**论文**: Strong Predictors, Weak Selectors: Diagnosing and Fixing Self-Consistency for Named Entity Recognition
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+格式合规）
**审稿模式**: 重新审稿（fresh），1 轮独立审稿 + 1 轮交叉回应

---

## Summary

本文研究 self-consistency 在 NER 上的适用性，评估 5 种 confidence signal 的 quality estimation（QE）和 sample selection 能力。论文发现 QE 表现良好（ρ up to 0.45, AUROC up to 0.82）但 instance-level selection 普遍失败，将此命名为 "correlation-selection gap"，归因于 instance degeneracy 和 LP compression。最终提出 entity-level construction 作为替代方案，在 SciERC (+1.67pp) 和 Few-NERD (+0.88pp) 上取得显著改进。

---

## Strengths

1. **统计方法论严谨度在 NER/IE 领域罕见**：bootstrap CI、paired bootstrap、TOST equivalence testing with external margins、MDE 计算、Bonferroni correction。方法论意识远高于同类工作。

2. **消融设计系统完整**：temperature（4 点）、N-scaling（N=2 到 32）、model scale（3B/4B/8B）、epoch confound（2-3 点 curve）、LoRA rank、constrained vs free-form decoding、supervised combination、hidden state probes、DeBERTa verifier。形成闭环证据网络。

3. **负面结果的透明报告**：6+ 个 negative experiments（supervised combination、hidden probes、DeBERTa verifier、DALS、VerbConf、calibration baseline）如实报告。Limitations section 覆盖 15+ 条限制，堪称范例。

4. **问题分解清晰**：将 QE 和 sample selection 显式分离是有用的框架选择。QE → selective prediction 的实用价值论证完整。

5. **写作质量高**：无 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无过度分段、无黑名单用词）。技术表述清晰紧凑。格式合规（ACL 模板、review 模式、匿名、checklist 认真填写）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[N1] Entity-level construction 新颖性不足** [critical, 共识]
- Entity-level construction 本质是 entity-level majority voting，与 ensemble NER（EL4NER, Naderi et al. 2021）机制高度相似，区别仅在于跨同模型 sample 而非跨模型聚合。论文自身在 Related Work §2 承认 "our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity"。
- LP-weighted vs Uniform 增量极小（SciERC: +1.67 vs +1.54pp; N=16 时两者 converge），说明 LP weighting 贡献有限。
- 作为论文两大贡献之一（"Fixing" 部分），新颖性不足严重影响 main conference 定位。

**[N2] Correlation-selection gap 概念深度有限** [critical, 基本共识]
- 4/5 signal 是 instance-level，按定义不能 rank candidates——这是定义性质而非经验发现。论文在 §3.1 已建立 per-sample vs instance-level 区分，instance-level signal 无法 rank 是逻辑推论。
- 真正的经验性发现是 LP（唯一 per-sample signal）也失败，以及 degeneracy-alignment disentanglement（温度实验）和 degeneracy 不能跨 dataset 预测 LP 方向（ρ=0.052）。但这些被 4 个 instance-level signal 的 "失败" 稀释了。
- R1 认为 LP 失败和 disentanglement 有经验价值（部分同意），但当前 framing 混淆了定义性限制和经验性发现。

**[N3] LP-alignment gating 使用 test set 构成 information leakage** [critical, 共识]
- Gating protocol 使用 50 个 test set instances 估计 within-instance ρ(LP, F1)（需要 gold labels），再将 routing decision 应用于同一 test set。论文自述 "probe instances are drawn from the test set for simplicity"，但仍 claim "correctly routes all three evaluated datasets"。
- §4.5 已增加三条 caveats（(a) test set probe, (b) only 3 datasets, (c) proof of concept），但 Contribution #3 仍包含 gating 的 correct routing claim。
- 仅 3 个 dataset 验证（实际 2 个 informative data points），且 dataset 间 ρ 差距很大（>0.15），routing "正确性" 可能只是因为差距足够大。

### Should-Fix（影响评分但不一票否决）

**[W1] ε=0.05 non-tied subset 是 post-hoc 最优切点，Bonferroni 未覆盖 ε sweep** [warning, 共识]
- ε sweep（Table 10）显示 ε=0.05 恰好是 p-value 最小的切点（p=0.004），相邻切点显著性更弱。主文 §4.2 "survives Bonferroni correction" 仅覆盖 5 signal comparisons，未覆盖 ε sweep 的 7 个阈值。7×5=35 Bonferroni 后 p_adj=0.14。
- 论文已在 Limitations 标注 "post-hoc exploratory choice"，但主文叙事权重过高。

**[W2] Expected selection gain "bound" 中 g(·) 未定义** [warning, 共识]
- §4.3: E[ΔF1] ≤ (1-d) · Δ_oracle · g(ρ_within)，g(·) 描述为 "monotonically increasing function" 但从未定义。包含未定义函数的不等式不构成 bound。
- 两位 Reviewer 共识：不需要形式化定理，但 "bounded by" 应改为 "heuristically decomposed as"，并给出 g(·) 的假设条件。

**[W3] θ=2/N "tuning-free" claim 缺乏 θ sensitivity sweep** [warning, 共识]
- §4.5 称 θ=2/N 是 "tuning-free across all datasets"，但仅对比了 θ=0.5 majority baseline。无 θ ∈ [1/N, 1] 的 sensitivity curve，无 precision/recall 分解。θ=2/N 在 N=8 时等于 0.25，大幅 boost recall，可能在 high-noise 场景引入 false positives。

**[W4] SciERC greedy F1 出现 4 个值，协议不统一** [warning, 共识]
- 0.640, 0.644, 0.645, 0.650 四个值跨 Tables 1-4 出现。§3.2 末尾有解释，但 Table 2 用 2-seed、Table 3 用 single-seed/3-seed、Table 7 用 3-seed 的不统一缺乏解释。

**[W5] Complementarity claim 仅基于 3 dataset（2 个 informative data points）** [warning, 共识]
- CoNLL 为 ceiling regime，两种方法都不 work。实际仅 SciERC（construction wins）和 Few-NERD（LP wins）两个 informative data points。

**[W6] 模型规模 4B-8B，claims 表述过于一般化** [warning, 共识]
- 标题 "for NER" 和 Contribution 2 无 scale 限定。Discussion "degeneracy rises with model capability" 仅基于 3B-8B。70B+ 行为未知。

**[W7] Abstract 信息密度过高** [warning, 共识]
- 约 10 个数字，读起来像实验报告压缩版。建议精简至 2-3 个关键数字。

**[W8] Table 4 (entity construction) 缺少 multi-seed ±σ** [warning, 共识]
- Prescriptive 贡献应有更强统计支撑。

### Info（小问题）

- [I1] Figure 1 caption ρ=0.39 vs Abstract ρ=0.45 scope 不一致（SciERC vs CoNLL）
- [I2] WNUT-17 正文分析不足——Introduction 定位为 "signal-collapse boundary" 但主文仅一句提及
- [I3] Table D.1 "Identical" vs 正文 "Constant F1" 概念不同（11% vs 17.8%），易混淆

---

## Reviewer Consensus [AGREE]

1. **Overall 评分一致**：两位 Reviewer 独立给出 3/5 (Findings)，交叉回应后维持不变。
2. **Entity construction 新颖性不足**：两位 Reviewer 均独立列为 critical 并在交叉回应中完全一致。
3. **Test-set leakage in gating**：两位 Reviewer 均独立列为 critical 并完全一致。
4. **θ=2/N、greedy F1 不一致、complementarity 仅 3 dataset、scale 限制**：全部共识。
5. **统计严谨度和写作质量**：均给予高度肯定。

## Reviewer Divergence [REBUT]

1. **ε=0.05 严重度**：R1 列为 critical（Bonferroni 应覆盖 ε sweep），R2 同意统计问题但建议降为 warning（论文已做 hedging）。→ **最终判定：warning**（论文在 Limitations 和 Appendix 已承认 post-hoc 性质，需修改的是主文措辞而非删除分析）。

2. **Expected gain bound 形式化**：R1 列为 critical（g(·) 未定义则 bound 无意义），R2 建议降为 warning（实证论文不需要定理）。→ **最终判定：warning**（修改措辞即可，无需正式证明）。

3. **Epoch confound (Few-NERD 3-epoch)**：R2 列为 warning（未完全消解），R1 REBUT（Appendix E 提供了 3-point curve，5-epoch LP 仍 positive，已 adequately addressed）。→ **最终判定：不列入报告**（R1 反驳有理有据，Appendix 的 epoch ablation 覆盖充分）。

4. **Selective prediction 定位**：R2 列为 warning（不应列为独立贡献），R1 REBUT（原文中是 Contribution 1 的子项而非独立贡献）。→ **最终判定：不列入报告**（R1 对原文结构的阅读准确）。

5. **Appendix 体量**：R1 列为 info（7:1 ratio），R2 REBUT（ARR 无限制，材料对 reproducibility 有价值）。→ **最终判定：不列入报告**。

---

## Questions（需要作者澄清）

**Q1.** Entity-level construction 相对于 ensemble NER entity voting 的技术区别是什么？单模型多 sample vs 多模型是否产生不同的 diversity 特征？LP weighting 在 ensemble 设定下是否可行？

**Q2.** Table 2 使用 "2-seed mean" 而 Table 3/7 使用 "3-seed"，为什么 selection analysis 的 seed 数量少于 QE analysis？

**Q3.** LP-alignment gating 如果改用 held-out validation set（不接触 test set gold），routing decision 是否仍然 correct？

**Q4.** §4.3 Expected selection gain decomposition 中 g(·) 的具体形式或假设条件是什么？

**Q5.** θ=2/N 是如何确定的——先验理由还是基于性能选择？能否提供 θ 在 [1/N, 1] 范围内的 sensitivity curve 和 precision/recall 分解？

**Q6.** §1 中 "the first systematic empirical characterization" 的 scope——相对于 Yao et al. 2026 和 Vashurin et al. 2025 (CoCoA)，"first" 具体指什么？

**Q7.** Within-instance LP-quality alignment 的 SciERC vs Few-NERD 差异（ρ≈0.26 vs ≈0.5-0.7）是否可能由 entity type 数量（6 vs 8）或 domain shift 驱动？

---

## Missing References

1. **Entity-level ensemble NER**: Florian et al. 2003 ("Named Entity Recognition through Classifier Combination")——entity-level construction 的最直接先行工作，应引用并讨论区别。
2. **Zero-shot NER voting**: Luo et al. 2023 (Zero-shot NER with ChatGPT, self-annotation + voting)——与 entity-level construction 机制相关。
3. **MBR decoding strategies**: Wiher et al. 2022 ("On Decoding Strategies for Neural Text Generators")——对 selection-gap 讨论有补充价值。
4. **Selective prediction under domain shift**: Kamath et al. 2020 ("Selective Question Answering under Domain Shift")——补充 selective prediction 引用。
5. **Test-time scaling 最新进展**: Muennighoff et al. 2025 ("s1: Simple Test-Time Scaling") 和/或 Qu et al. 2025 ("Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning")。

---

## Overall Assessment

**评分: Weak Accept (Findings) / Borderline (Main Conference)**
**置信度: 4/5 (High)**

两位 Reviewer 一致评价为 3/5，推荐 Findings track。

**核心判断**：这是一篇高质量的实证分析论文。统计方法论严谨度、消融覆盖广度、负面结果透明度均远高于同类工作。QE vs selection 的显式分离和 degeneracy/compression 双因素诊断框架有真实贡献。

**制约因素**：
- Entity-level construction 新颖性有限（本质是 entity-level majority voting），作为论文 "Fixing" 部分的核心贡献不足以支撑 main conference。
- Correlation-selection gap 的概念中，4/5 signal 失败是定义性的，真正的经验贡献（LP 失败 + disentanglement）被稀释。
- Gating protocol 存在 test-set leakage + 仅 3 dataset 验证。
- Prescriptive claims（complementarity、gating、θ tuning-free）的证据强度与 claim 力度不匹配。

**修复路径**：
1. 在 Contribution framing 上将 entity construction 定位为 "applying known technique to a new setting" 而非方法创新，同时 strengthen diagnostic contribution 的叙事价值。
2. 重构 correlation-selection gap：instance-level signal 失败作为 setup，聚焦 LP compression/alignment。
3. Gating 降级为 proof of concept 或用 proper validation set 重新验证。
4. 修复 g(·) 措辞、ε Bonferroni 范围说明、Abstract 数字精简、θ sensitivity sweep。

如果以上修复到位，论文适合 **EMNLP Findings**。Main conference 需要更强的方法贡献（如理论化的 selection bound）或更广的 scale 覆盖。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高（~10 个数字），精简至 2-3 个关键数字
- AUROC/LP 缩写定义需确认是否已展开

### Introduction
- Contribution 2 和标题需加入 "fine-tuned / 4B-8B" scope 限定
- "first systematic empirical characterization" 需相对于 Yao et al. 2026 / CoCoA 更精确界定 scope
- WNUT-17 的 "signal-collapse boundary" 角色定位与正文覆盖不匹配

### Related Work
- 缺少 entity-level ensemble NER 的覆盖（Florian et al. 2003 等）
- 缺少 selective prediction 和 test-time scaling 的最新引用

### Method
- Entity matching 标准分散在 §3.2 各段落，建议统一展示
- Expected selection gain decomposition (§4.3): "bounded by" → "heuristically decomposed as"

### Experiments
- Table 2 vs 3 vs 7 的 seed 数量不统一需解释
- Table 4 缺少 multi-seed ±σ
- §4.2 "survives Bonferroni correction" 需说明 correction 范围

### Discussion
- 篇幅极短（11 行），与 Experiments 的体量不成比例
- 正文空间可能紧张——需确认编译后 ≤8 页

### Conclusion
- 实用建议（LP selection when ρ≈0.3, otherwise construction）清晰有用

### Limitations
- 覆盖全面，堪称范例

### Appendix
- 体量大但内容对 reproducibility 有价值
- Figure 1 caption scope 需与 Abstract 一致