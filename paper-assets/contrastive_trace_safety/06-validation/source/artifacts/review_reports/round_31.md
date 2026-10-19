---
round: 31
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T23:05:10.584899+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 31 审稿报告（Fresh Review）

**论文**：Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**：EMNLP 2026 ARR (Long Paper)
**审稿模式**：Fresh（重新审稿，无上轮记忆）
**Reviewer 编排**：2 人（EMNLP 一般会议标准）
- Reviewer 1：方法严谨性（统计方法、实验设计、论证链可靠性）
- Reviewer 2：新颖性/完整性（贡献增量、related work 覆盖、叙事完整性）

---

## Summary

论文研究 reasoning model 的 hidden-state safety probe 中，层选择指标（crossing-rate composite vs threshold-based metrics）如何系统性地偏向不同层深度（浅层 vs 深层），导致"HS probe 是否优于 text probe"的结论翻转。核心发现是方法论性质的（C1: metric-induced layer selection bias），辅以 HS advantage 的 conditional empirical evidence（C2）和七种替代方法的 negative results（C3）。实验覆盖 4 个 reasoning model（3 Qwen, 1 Llama），在 HarmThoughts 数据集上进行，AdvBench 提供跨数据集几何验证。

---

## Strengths

1. **Random-label control 设计精巧**（Appendix B.1, Tables 7-8）：通过替换 CP labels 为随机标签，直接证实 CR-composite 的浅层偏好是 label-independent 的几何伪影。这是全文最有说服力的实验设计，两位 Reviewer 均高度评价。[AGREE]

2. **Two-stage experimental design + nested CV**（Section 3.5, Appendix W.1）：validation 探索 + held-out 确认的分离设计，配合 7-8B 的 5-fold nested CV（10/10 folds HS advantage 一致），显著降低了 selection bias 风险。在 probing 文献中这种严谨度不常见。[AGREE]

3. **极其详尽的附录**（26 页）：覆盖 layer sweep、random-label controls、cosine analysis、multi-seed stability、post-hoc power analysis、nested CV 等。透明度达到 Findings 级别及以上论文的典范标准。[AGREE]

4. **Bug disclosure（Appendix M）**：主动披露开发中发现的 bug 并完整报告修正过程，展示高度科学诚信。[AGREE]

5. **实操建议清晰**（Section 5）：三级 mitigation 方案（报告层选择 → 多指标审计 → ensemble）对从业者有直接参考价值。[AGREE]

6. **AdvBench 跨数据集验证**（Section 4.1）：bootstrap-validated divergence (31.7pp, p=0.015) 确认层选择偏差由 representational geometry 驱动，不依赖 CP 标注语义。[AGREE]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, consensus] **32B 结论在主文中超出 exploratory 标签范围**

尽管论文标记了 dagger 和 "exploratory" 字样，主文多处对 n=19-20 结果做了结论性陈述：
- Section 4.2: "The HS advantage is conditioned on two empirically correlated factors" 部分基于 QwQ-32B position 分析
- Section 4.4: 标题使用 "Exploratory 32B analysis" 但正文语气偏实质性
- Table 4: 数据呈现格式与 well-powered Table 3 完全一致，读者易混淆
- R1-32B precision margin +4.5pp 远低于 MDE 8.6pp，但未在主文标注为 underpowered

**R1**: Critical（N2）。**R2**: AGREE（W2）。

建议：(1) Section 4.4 开头加显著 caveat（非脚注）；(2) Table 4 中 sub-MDE 效应标灰或加符号；(3) Discussion 中清晰区分 7-8B confirmed findings 和 32B exploratory observations。

**MF2** [critical, consensus] **缺少 multi-layer probing 文献讨论**

论文花大量篇幅论证"单指标单层选择有问题"（C1），但 Related Work 和 Discussion 均未讨论文献中已有的跨层 probing 方案（CLAP 2509.09700, BERTology aggregator 2601.13288 等），这些方案从根本上绕过了单层选择问题。Appendix Z.1 的 multi-metric ensemble 仅 1 页且标注 "preliminary"，未与上述文献对接。

**R2**: Critical（N2）。**R1**: AGREE。

建议：在 Related Work 和 Discussion 中加入 multi-layer probing 讨论，将 ensemble 与已有方法对比定位，或解释为什么 multi-layer 方法在 CoT safety 设置中可能不直接适用。

**MF3** [critical/warning, consensus with divergence] **多重比较校正的 conditional inference 问题**

论文探索了 ~2,240 configurations/model，仅对 12 个 held-out test 做 Holm-Bonferroni。Two-stage design + nested CV（7-8B）部分缓解，但 conditional inference 未被正式解决。主要集中在 32B 规模（完全缺少 nested CV）。

**R1**: Critical（N1）。**R2**: AGREE with nuance（7-8B mitigated, 32B gap real）。

建议：(1) 将 conditional inference caveat 从附录提升到主文 Section 4；(2) 7-8B 以 nested CV fold-averaged p-values 为 primary evidence；(3) Section 4.4 显式标注 32B nested CV 缺失。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, consensus] **Position residualization 不完整**：仅 2/4 模型有 quadratic 控制。QwQ-32B 的 HS advantage 被 quadratic position 完全吸收（Table 32），但 R1-8B/OT-7B 在 quadratic 下仍存活。论文未讨论 residualization 可能去除 genuine signal（而非 confound）的可能性。建议对所有 4 模型统一报告 linear + quadratic residualization。

**SF2** [warning, partial consensus] **Cosine compression → crossing-rate inflation 因果链缺直接干预**：Random-label control 是强间接证据，但未通过 whitening/decorrelation 建立因果关系。论文 Limitations 已承认 correlational status。建议至少在讨论中区分 correlation vs. causation。

**SF3** [warning, consensus] **模型多样性有限**：3/4 模型共享 Qwen 架构，仅 R1-8B (Llama) 提供跨架构证据。Gemma-2 的跨架构验证仅覆盖 cosine compression，未做完整 probing。泛化声明应限定为 "across Qwen-family and one Llama model"。

**SF4** [warning, consensus] **主文可能超出 8 页限制**：Conclusion 在 p9 开始。视觉审查确认 p9 约 55-60% 填充。如果 Conclusion 属于正文（而非 Limitations），则构成格式违规。

**SF5** [warning, partial consensus] **单一 CP 标注数据集**：CP-dependent claims (C2) 完全依赖 HarmThoughts。AdvBench 跨数据集验证仅覆盖 layer selection pattern（C1），未验证 HS advantage 的跨数据集稳健性。κ=0.606 (moderate) on 51 dual-annotated traces。

**SF6** [warning, partial consensus] **K=5 consecutive crossings 基于单模型验证**：K=5 在 R1-8B validation set 选定后固定。Table 24 有跨模型 K 消融，但 per-model optimal K 可能不同（如 QwQ-32B K=7 更优）。

---

## Reviewer Consensus [AGREE]

1. **32B 结论需要更严格的 exploratory 控制**：主文叙述语气与 dagger 标记不匹配，Table 4 视觉格式与 well-powered Table 3 无区分。
2. **Multi-layer probing 文献缺口**：论文识别了单层选择问题但未讨论已有的跨层解决方案。
3. **Conditional inference 问题在 32B 上最严重**：7-8B nested CV 有效缓解，32B 完全缺失。
4. **实验执行质量高**：random-label control、two-stage design、nested CV、multi-seed stability 均为高质量实验设计。
5. **Page limit 可能违规**：Conclusion 溢出到 p9。

## Reviewer Divergence [REBUT]

**C1 新颖性是否充分**：
- **R2 (3.0, Findings)**：C1 是 Belinkov (2022)/Voita & Titov (2020) 已知 metric sensitivity 问题的领域应用，"qualitative reversal" 从统计角度看直观，增量贡献不足以支撑主会议。
- **R1 (3.5, Borderline Conference)**：C1 超越了一般性讨论——(a) 提供了具体机制解释（cosine compression → crossing-rate inflation），(b) random-label control 证实了几何伪影 vs 安全信号的区分，(c) 三级诊断方案是新的实操贡献。Belinkov/Voita 均未提供类似因果分析或量化诊断。
- **Director 判断**：R1 的 rebuttal 部分成立——机制解释和 random-label control 确实超越了 Belinkov 的一般性讨论。但 R2 的核心批评（"阈值附近分类器不可靠" 从统计角度看直觉明显）也有道理。论文应更深入对比 Voita & Titov 的 MDL probe（如果 MDL 天然避免 threshold-crossing 问题，C1 的实际影响需重新评估）。此分歧反映 novelty 主观性——R1 接受 "known concept + new mechanism + safety domain" 为充分增量，R2 不接受。

---

## Questions

1. 如果改用 conditional selective inference（Berk et al. 2013; Lee et al. 2016），7-8B 和 32B 分别有多少 tests 能通过？
2. QwQ-32B quadratic position residualization 完全吸收 HS advantage：是 confound removal 还是 genuine signal removal？能否在 AdvBench 上验证？
3. 对浅层表征做 whitening/sphering 后重新运行 crossing-rate 层选择，是否消除浅层偏好？
4. 其他模型（尤其 32B）的 optimal K 是多少？K=5 是否系统性偏向/偏离特定模型？
5. AUROC 选择 mid-depth layers（Table 42），是否存在 shallow/mid/deep 三分结构？这对论文的二分叙事有何影响？

---

## Missing References

1. **Berk, Brown, Buja, Zhang, & Zhao (2013)** — Valid post-selection inference. *Annals of Statistics*. [post-selection inference 框架]
2. **Lee, Sun, Sun, & Taylor (2016)** — Exact post-selection inference. *Annals of Statistics*. [selective inference 方法论]
3. **CLAP (Cross-Layer Attention Probing)** — arXiv 2509.09700 (Sep 2025). [跨层 probing，绕过单层选择问题]
4. **"Detecting LLM Hallucination Through Layer-wise Information Deficiency"** — EMNLP 2025. [层间信息量非单调变化]
5. RepE (Zou et al. 2023) 的层选择方法论——已引用为 baseline 但未讨论其层选择策略与本文发现的关系。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置为 true）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 9 info, 0 critical）：

**Warnings**:
1. **pp3-5 连续纯文本无 display item**：Related Work → Methods → Experiments 开头缺乏视觉锚点。建议将 Figure 1 精简版或方法示意图前移至 Section 3。
2. **Figure 1 直到 p6 才出现**：对实证论文，前 5 页完全无图表辅助理解。
3. **p9 仅 55-60% 填充**：主体文末页大片空白。可考虑将部分 Discussion 内容拉入 Conclusion。

**Info**: 主文 1 Figure + 4 Tables = 5 display items（推荐 5-8）；Figure 1 轴标签偏小（~6-7pt）；其他排版均合规。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Confidence: 4/5**

**理由**：

论文在实验执行层面达到高质量标准——random-label controls、two-stage design + nested CV、26 页附录透明度极高、bug disclosure 展现科学诚信。核心方法论发现（metric-induced layer selection bias 在 safety probing 中导致结论翻转）是真实且有价值的经验性贡献。

但以下因素使论文定位于 Findings 而非 Conference：

1. **概念新颖性受限**（R1/R2 divergence，Director 倾向 R2）：核心发现（指标敏感性影响探针结论）在 probing 方法论文献中有充分基础（Belinkov 2022, Voita & Titov 2020）。论文的增量——机制解释 + 安全领域量化——有价值但不足以构成 Conference 级别的概念贡献。
2. **32B 证据薄弱**（consensus）：n=19-20 的 MDE 为 8.6-9.5pp，多处主文结论超出 exploratory 标签；QwQ-32B position confound 未充分解决。
3. **Multi-layer probing 文献缺失**（consensus）：论文识别了问题但几乎不讨论已有的解决方案，削弱了实用价值和叙事完整性。
4. **格式可能违规**：Conclusion 溢出到 p9。

Findings track 是恰当的发表场所：经验性方法论警示 + 严谨实验执行 + 透明度标杆，对 safety probing 从业者有直接参考价值。

---

## Detailed Comments

### Section 1 (Introduction)
- C1 的 framing "Prior work has noted metric sensitivity in probing; our contribution is demonstrating a qualitative reversal" 可以更深入地与 Voita & Titov (2020) MDL probe 对比——如果 MDL 天然避免 threshold-crossing 问题，需讨论其与本文诊断方案的互补性。
- "retrospective classification, not online detection" 的 scope 限定清晰，但与 Discussion 的 deployment 建议存在张力。

### Section 3 (Method)
- K=5 consecutive crossings "selected on the R1-8B validation set and held fixed" — 应在附录报告其他模型的 per-model optimal K。
- Crossing rate 定义中 "crossing-rate point (CP)" 与 commitment point (CP) 存在术语混淆风险。

### Section 4 (Experiments)
- Section 4.1: CR-composite 的 systematic shallow selection pattern 有充分证据支撑。Random-label control 和 AdvBench replication 是强验证。
- Section 4.2 (HS vs Text): 7-8B 结果（nested CV, multi-seed）well-powered 且可信。
- Section 4.3 (Encoder robustness): 4/4 HB (384d) → 1/4 HB (1024d) gradient 清晰，但强化了 C2 的 conditional 性质。
- Section 4.4 (32B): 需要更显著的 exploratory caveat。Table 4 应视觉区分于 Table 3。
- Section 4.6 (Negative results): 建议精简 "expected negatives" (BOCPD/CUSUM)，突出 "informative negatives" (RepE model-dependency, cross-model transfer failure)。

### Section 5 (Discussion)
- 三级 mitigation 方案有实操价值，但与 retrospective 定位存在张力。建议明确标注为 "方法论指南" 而非 "deployment 建议"。
- 缺少与 multi-layer probing 方案的对比讨论。

### Section 6 (Conclusion)
- 可能溢出到 p9，需格式确认和修正。

### Limitations
- 覆盖了主要弱点（32B power、单数据集、架构覆盖、correlational status）。
- 可增加 multi-layer probing 作为 future direction。
