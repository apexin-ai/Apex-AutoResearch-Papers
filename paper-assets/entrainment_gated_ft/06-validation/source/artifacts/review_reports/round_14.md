---
round: 14
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T12:09:54.110579+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 14 审稿报告

**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**Venue**: EMNLP 2026 (ARR May 2026 cycle, Long Paper)
**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）
**交叉分享**: 完成（R1→R2, R2→R1）；R1 对 R2 的 11 个观点中 8 项 [AGREE]、3 项 [REBUT]
**审稿轮次**: 1 轮收敛（无需 Round 2）

---

## Summary

本文利用 Wang et al. (2025) 的 controlled model zoo（3 hybrid linear recurrent 架构 × 5 attention ratios × 2 scales = 30 配置），在 10 个 benchmark 上系统分析 attention 对跨架构 per-example 行为的影响。核心发现：(1) per-example predictive multiplicity 随 task 类型变化（α = 0.14–0.30），pairwise Jaccard 始终低于 0.10（permutation test p < .0001）；(2) aggregate convergence 仅在 LAMBADA 上有初步证据（Bonferroni-adjusted p = .100，未达 conventional significance），且依赖 GDN 的包含；(3) aggregate convergence 与 per-example divergence 存在 decoupling——Jaccard 在 4% attention 即饱和，而 aggregate σ 持续下降。论文定位为经验性分析，将已有 multiplicity 框架应用于 hybrid recurrent 架构的新维度（architectural variation）。

---

## Strengths

1. **控制变量实验设计**：统一 training data / tokenizer / hyperparameters 的 model zoo，仅变化 architecture 和 attention ratio，是隔离 architectural effects 的 gold standard approach（§3.1）。[R1-S2, R2-S2 共识]

2. **核心 per-example multiplicity finding 证据扎实**：四个 benchmark 上的 Jaccard permutation test 全部 p < .0001（Appendix J），normalized ES 确认非 set-size artifact（Appendix H，observed J ≈ 0.10 vs J_max = 0.78–0.92），continuous-threshold 分析确认 robustness（Appendix O）。这是论文最强的贡献。[R1-S5, R2-S4 共识]

3. **统计局限性高度自觉且诚实**：n=5 power limitation（§3.5），n=3 bootstrap CI 的 heuristic 性质，single training run 限制，GDN confound——均在论文中主动标注。[R1-S3, R2-S5 共识]

4. **Decoupling 现象展示清晰**：Figure 1 有效传达 aggregate convergence vs per-example saturation 的时间尺度分离。该现象在 4 个主要 benchmark 上一致（Appendix N）。[R1-S1, R2-S3 共识]

5. **极为详尽的 robustness 检验**：13 页 appendix（A–W）覆盖 GDN exclusion、continuous Jaccard、normalized ES、seed calibration、calibration analysis、subsample sensitivity 等。大多数可预见的反驳已被提前回应。[R1-S4, R2-S6 共识]

6. **写作质量**：技术精确，结构清晰，claims 的 hedging 总体恰当。[R1-S6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Critical] Single training run 无法区分 architecture effect 与 seed effect**
- R1-N1 Critical + R2-N2 Critical，交叉 [AGREE]
- 每个 architecture × attention ratio 配置仅有一次训练运行。论文的核心 claim 是 per-example multiplicity 与 architectural variation 相关联，但无法排除 seed-specific effects 产生相似量级 divergence 的可能。
- Appendix W 的 Pythia 70M PolyPythias 对比存在三重 mismatch：(a) scale（70M vs 340M/1.3B），(b) architecture family（Transformer vs hybrid recurrent），(c) accuracy regime（~0.20 vs ~0.50）。不足以作为 definitive seed calibration。
- §4.2 的 within-architecture Jaccard（~0.33）vs cross-architecture Jaccard（~0.10）3× gap 比较的维度不同（同一架构跨 attention ratio vs 不同架构同一 ratio），不是直接的 seed vs architecture 对比，且 within-architecture Jaccard 可能因 structural overlap 被 inflate（R1 Q5）。
- **建议**：对至少一个 architecture-ratio 配置训练 2-3 个额外 seed，直接量化 within-architecture cross-seed Jaccard；若不可行，进一步弱化因果性语言，明确条件化于 single-seed limitation。

**W2 [Critical] Aggregate convergence 的证据不足以支撑其在论文叙事中的权重**
- R1-N2 Critical + R2-N3 Critical，交叉 [AGREE]
- LAMBADA Bonferroni-adjusted p = .100 未达 conventional significance（10-benchmark 校正下 p = .170 更远）；9/10 benchmarks 无显著 convergence；仅 1.3B 观察到（340M ρ = -0.50, p = .45）；排除 GDN 后 ρ 从 -1.0 弱化至 -0.7（p = .233），MMLU 从 ρ = -0.7 反转至 +0.6。
- 然而 Abstract 和 Introduction 仍将 LAMBADA convergence 作为核心叙事之一（"cross-architecture standard deviation drops 79%"），赋予其与 per-example multiplicity 对等的权重。
- **建议**：重新聚焦论文叙事到 per-example multiplicity 本身（证据远更强），将 aggregate convergence 明确定位为 exploratory context 而非核心 finding。Abstract 中需紧跟 non-significance caveat。

### Should-Fix（影响评分但不一票否决）

**W3 [Major] GDN attention head confound 对 aggregate convergence 结论的影响**
- R1-W1 Major + R2-N3 部分重叠，交叉 [AGREE]
- GDN h3-1 使用 16 attention heads vs 所有其他配置 32 heads。Table 1 主要呈现包含 GDN，MMLU 方向反转（ρ: -0.7 → +0.6）被放在 Appendix D。
- **重要区分**（R1 补充）：decoupling finding 对 GDN confound 是 robust——RetNet-HGRN2 pair 保持 σ ≤ 0.008 + Jaccard 饱和（§4.3）。GDN confound 主要影响 aggregate convergence 的 generality，不影响 per-example multiplicity 核心 finding。
- **建议**：Table 1 同时报告 full-zoo 和 excluding-GDN 两组结果；§4.2 首次报告 LAMBADA 结果时即讨论 GDN confound，不要推迟到 §4.3。

**W4 [Major] Bootstrap CI (n=3) 被过度引用**
- R1-W3 Major
- n=3 architectures 的 bootstrap CI resampling space 极其有限（至多 27 unique resamples），11.25% 为 degenerate resamples。论文标注 "heuristic" 但 Introduction 仍将 "BCa 95% CI excludes zero" 与 Bonferroni p = .100 并列作为 convergence 证据。
- **建议**：降低 CI 在 Introduction 中的权重，不与 p-value 并列推进叙事。

**W5 [Major] Confidence margin "mechanism" 标题暗示因果性**
- R1-W4 Major
- §4.1 段标题 "Confidence margin mechanism" 暗示因果，但证据是 correlational（AUC 0.70-0.74）。ECE（17% spread）作为粗粒度度量可能无法捕捉 disruption threshold 附近的 fine-grained calibration 差异。
- **建议**：标题改为 "Confidence margin predictor"；补充 threshold-region calibration 分析或加 caveat。

**W6 [Major] n=5 attention ratios 使 convergence permutation test 为 binary outcome**
- R1-W2 Major
- 只有 ρ = ±1.0 达到 p < .05（p = .017）。Table 1 中 9 个 non-significant ρ 的信息含量极低——不能解释为 "no convergence"，只能说 "no power to detect imperfect trends"。
- **建议**：Table 1 解读中更强调 power limitation。

**W7 [Warning] 标题/Abstract 过度泛化**
- R1-W5 Minor + R2-W1 Warning，交叉 [AGREE]
- 仅 3 种架构（GDN/RetNet/HGRN2）来自单一 model zoo，但标题 "Hybrid Linear Recurrent Architectures" 暗示更广泛 generality。Mamba、RWKV-6、Jamba 未涉及。
- **建议**：标题加限定词（如 "Three Hybrid..." 或 "Gated Linear..."）；Abstract 明确 scope。

**W8 [Warning] Routing 分析的实用价值有限**
- R1-W6 Minor + R2-W3 Warning，交叉 [AGREE]
- Rescue-threshold routing 仅在 LAMBADA 上有效（+5.3pp），HellaSwag/PIQA 无改进，ARC-Easy 仅 +1.0pp。论文将此归因于 multiplicity 程度差异但未深入分析 LAMBADA 作为 retrieval task 的特殊性。
- **建议**：降低 routing 在 Conclusion 中的权重，或更 explicit 标注 proof-of-concept 性质。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：
1. Single-seed limitation 是最根本的实验设计限制，使所有 "architecture-driven" claims 停留在 associative 层面
2. Aggregate convergence 的统计证据不足以支撑其在叙事中的核心地位
3. GDN confound 影响 aggregate convergence 的 generality（但不影响 per-example multiplicity 和 decoupling）
4. Per-example multiplicity 的核心 finding（Jaccard permutation test p < .0001）证据扎实
5. 标题/表述存在过度泛化
6. Routing 的 practical exploitation 有限

## Reviewer Divergence

**新颖性评估**（R2-N1 Critical vs R1 partial REBUT）：
- R2 认为核心发现是已知现象在新数据上的应用，无方法论创新，practical impact 有限，标为 Critical。
- R1 部分反驳：cross-architecture multiplicity 的量化发现（4% Jaccard 饱和、task-dependent α variation）不可从已有文献直接推断，empirical discovery 足以支撑 Findings 级别。Decoupling finding 的时间尺度分离在已有文献中无直接对应。但同意 Excitement 有限（R1: 3/5, R2: 2.5/5）。
- **Director 判断**：R2 的 concern 有道理但标 Critical 偏重。论文的新颖性主要在 empirical finding 层面，对 Findings track 足够，对 main conference 不足。

**Overclaiming 程度**（R2-W2 Warning vs R1 partial REBUT）：
- R2 指出多处因果语言用于相关性证据。
- R1 反驳论文整体 hedging 充分（反复使用 "associated with"、"exploratory evidence"），仅个别措辞需调整（"affect"、"mechanism"）。
- **Director 判断**：R1 的评估更准确——论文大部分位置的 hedging 是充分的，但 §4.1 "mechanism" 标题和 Introduction 个别措辞可进一步弱化。

---

## Questions

1. **[R1-Q1, R2-Q1]** 是否有可能获取 Wang et al. model zoo 中任一配置的多 seed 权重？Within-architecture cross-seed Jaccard 将直接回答 seed vs architecture 的核心关切。
2. **[R1-Q2, R2-Q2]** GDN h3-1 使用 16 heads 的设计选择是否有特定 architectural motivation（如参数匹配）？
3. **[R2-Q3]** Per-example Jaccard 在 4% attention 即饱和——能否提供 mechanistic intuition？Appendix F 的 attention weight analysis 暗示 divergence 来源于 recurrent layers 而非 attention layers。
4. **[R1-Q3]** BoolQ（12/24 significant）和 WinoGrande（10/24 significant）的 mixed Jaccard significance 是否削弱 per-example multiplicity 的 generality？
5. **[R1-Q4]** Greedy decoding 下的 per-example effects 是否在 sampling decoding 下持续？
6. **[R1-Q5]** Within-architecture Jaccard (~0.33) 是否因 structural overlap（同一架构不同 attention levels 自然影响部分相同 examples）而被 inflate，从而夸大 3× gap？

---

## Missing References

- **Milani Fard et al. (2016)** "Launch and Iterate: Reducing Prediction Churn" NeurIPS — 直接研究 per-example prediction instability（R2 推荐；R1 认为场景不同但作为 complementary perspective 有价值）
- **Garipov et al. (2018)** "Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs" NeurIPS — mode connectivity（R2 推荐；R1 认为相关性较弱）
- **Poli et al. (2023)** "Hyena Hierarchy" — 另一类 recurrence-attention hybrid（R1 推荐）
- **Jelassi et al. (2024)** — attention 与 in-context learning in hybrid models（R1 推荐）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置中未启用）。

---

## Visual Layout Check（非评分项）

视觉审查已完成。主要发现：

**Warnings (3)**:
1. **Pages 3-5 视觉疲劳**：连续 3 页纯文本（Related Work → Method → Statistical Methods），无任何 display item。建议将部分方法公式提升为 display math 或从 Appendix 提前 1 个图/表。
2. **Display items 密度过低**：主正文 8 页仅 3 个 display items（Figure 1 + Table 1 + Table 2），密度 0.375/页，远低于实证论文通常的 5-8 个。大量结果表被推到 Appendix，正文显得"只有结论没有证据"。建议从 Appendix 提升 1-2 个关键表格到正文。
3. **Appendix p.14 拥挤**：单页堆叠 5+ 个小表格，可读性受限。

**Info (9)**：首页无视觉锚点（Figure 1 在第 2 页，可接受）；Figure 1 清晰有效；Tables 格式规范（booktabs）；无排版硬伤；ACL 模板 + 匿名合规 ✅。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**评分理由**：

论文最大的优势是 per-example multiplicity 的发现本身——四个 benchmark 上 Jaccard permutation test 全部 p < .0001、normalized ES 排除 floor effect、continuous-threshold 分析确认 robustness——这是扎实的经验性贡献。Decoupling 概念（aggregate convergence vs per-example divergence 的时间尺度分离）具有新颖性。统计方法论严谨，对限制条件的披露诚实。

论文最大的弱点是：(1) single training run 无法区分 architecture effect 与 seed effect，使核心 claim 停留在 associative 层面（两位 Reviewer 连续 10 轮标记的结构性问题）；(2) aggregate convergence 的统计证据未达 significance（Bonferroni p = .100）但在叙事中权重过高，且依赖 GDN 的特殊行为；(3) 纯应用性实证研究，无方法论创新，routing 的 practical impact 有限。

如果作者能补充至少一个配置的多 seed 实验并重新聚焦叙事到 per-example multiplicity 本身（弱化 aggregate convergence），论文有潜力达到 3.5 borderline conference。当前版本更适合 Findings track。

**置信度**: 4/5（两位 Reviewer 均熟悉 multiplicity/underspecification 文献和 hybrid architecture 领域，仔细阅读全文及 13 页 appendix）

---

## Detailed Comments

### Abstract / Introduction
- Abstract 仍然信息密度过高（R2），虽已从 6+ 数字精简至 3 个，但 200+ 词中统计量密集，首次阅读不易抓住 key message
- Introduction 开头 "cross-architecture standard deviation drops 79%" 缺少 non-significance caveat，应紧跟 Bonferroni p = .100
- "heuristic BCa 95% CI excludes zero" 不应与 p-value 并列推进叙事（R1-W3）
- 建议标题加限定词，明确仅覆盖 3 种架构

### Related Work (§2)
- 与 multiplicity / underspecification / Rashomon set 文献的区分清晰
- 建议补充 Milani Fard et al. (2016) 作为 complementary perspective
- 考虑补充 Poli et al. (2023) 和 Jelassi et al. (2024)

### Method (§3)
- Controlled model zoo design 是核心优势
- §3.5 统计方法论的自觉标注值得肯定
- n=5 power limitation 应在 Table 1 解读中更显著

### Experiments (§4)
- §4.1 "Confidence margin mechanism" 标题改为 "predictor" 或 "correlate"
- §4.2 LAMBADA convergence 应首次出现时即讨论 GDN confound
- Table 1 建议增加 excluding-GDN 行
- BoolQ 和 WinoGrande 的 mixed Jaccard significance 应在主文中简要讨论

### Conclusion (§5)
- Routing 的 proof-of-concept 性质应更 explicit
- Deployment implications 应限定于 "the three architectures studied here"

### Limitations
- 篇幅适当，覆盖 3 个核心 limitation ✅
- Appendix W 的 PolyPythias 三重 mismatch 应在 Limitations 中提及

### 格式合规
- 正文 ≤ 8 页 ✅
- ACL 模板 ✅
- Double-blind 匿名 ✅
- Limitations ✅ / Ethics ✅
- 参考文献格式 ✅