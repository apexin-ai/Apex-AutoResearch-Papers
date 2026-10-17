---
round: 15
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T17:36:03.794708+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 15（Fresh Review）

**论文**：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**目标会议**：EMNLP 2026 Long Paper（ARR May 2026 cycle）
**审稿日期**：2026-05-22
**Reviewer 编排**：2 人（R1 方法严谨性+实验设计+统计分析；R2 新颖性+相关工作+写作+格式）

---

## Summary

论文首次系统分析了 hybrid linear recurrent architectures 中 attention 对 per-example predictive multiplicity 的影响。使用 Wang et al. (2025) 的 controlled model zoo（3 架构 × 5 attention ratios × 2 scales），在 4 个 benchmark 上进行 per-example decomposition，发现：(1) cross-architecture pairwise Jaccard uniformly ≤ 0.10（~90% 非重叠），且在 4% attention 即饱和；(2) ambiguity α 呈 task-dependent variation（0.14–0.30），由 task type 而非 attention dose 决定；(3) LAMBADA 上 aggregate variance 随 attention 下降（ρ = −1.0, Bonferroni-adjusted p = .170, 不显著），但 per-example overlap 不变——aggregate convergence 与 per-example divergence 的 decoupling。

## Strengths

1. **研究问题新颖且重要**：首次将 predictive multiplicity 框架系统应用于 hybrid recurrent architecture 间的 per-example 差异分析。对模型选择和部署有直接实践意义——aggregate accuracy 相同的模型可能在 15–45% 的 individual predictions 上不同。[R1, R2 共识]

2. **统计方法诚实透明**：论文始终如一地报告统计局限（n=5 power limitation、Bonferroni correction、bootstrap CI 的 heuristic 性质），主动报告 p = .170 不显著。在 NLP 经验性研究中难能可贵。[R1, R2 共识]

3. **描述性发现扎实且不依赖小 n 推断**：Per-example Jaccard 在 4% attention 即饱和（§4.2）是直接观察；cross-architecture Jaccard uniformly ≤ 0.13 across 4 benchmarks + 4 架构（§4.1, Appendix X）也是 robust 描述性结果。这些发现本身有独立价值。[R1, R2 共识]

4. **实验控制质量高**：Wang et al. (2025) model zoo 提供 matched training conditions（相同数据、tokenizer、hyperparameters），仅变化架构和 attention 配置，是研究架构效应的理想设计。[R1, R2 共识]

5. **附录深度突出**：12 页附录覆盖 sensitivity analysis、continuous Jaccard、attention weight analysis、cross-benchmark extension、seed calibration、complementarity decomposition 等，展现全面的 robustness checking。[R1, R2 共识]

6. **Related Work 全面**：引用了 2026 年最新工作（Mamba-3, Gorbett et al., Haghighat et al.），对 ecological fallacy 和 Rashomon set 的关联讨论得体。[R2]

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [Critical, R1-N1 + R2-N1, 共识] **LAMBADA convergence 的 overclaiming**
- LAMBADA 是论文核心叙事支柱（Abstract 提到、Figure 1 展示、§4.2 详细分析、Table 1 首行），但 Bonferroni 校正后 p = .170 不显著，单侧检验校正后仍为 p = .083。论文在承认不显著的同时将其作为主要发现之一，构成 framing 层面的 overclaiming。
- **建议**：(1) 将叙事重心从 convergence claim 转向 per-example Jaccard saturation 的描述性发现；(2) Abstract/Introduction 中以四个 benchmark 的 α spectrum 和 Jaccard saturation 为主线；(3) convergence 明确标注为 "suggestive but not statistically significant after correction"。
- **Issue Tracker**: R5-W2（自 Round 1 起持续标记，Round 5-15 连续 11 轮被两位 Reviewer 独立确认）

**MF2** [Critical, R1-N2 + R2-N2, 共识] **GDN h3-1 的 16-head confound 削弱核心发现**
- GDN h3-1 使用 16 个 attention heads 而所有其他配置使用 32 个。排除 GDN 后：LAMBADA ρ 从 −1.0 弱化为 −0.7（p = .233）；MMLU 从 ρ = −0.7 **反转**为 +0.6。Appendix D.2 的 sensitivity analysis 被放在附录中，主文讨论不充分。
- **建议**：(1) Table 1 同时报告 with/without GDN 结果；(2) §4.3 明确区分哪些 claims 在排除 GDN 后仍成立（per-example Jaccard saturation: robust）、哪些不成立（LAMBADA convergence correlation: fragile）。
- **Issue Tracker**: R6-W2（自 Round 6 起持续标记）

**MF3** [Critical, R1-N3, R2 AGREE] **Bootstrap CI 基于 n=3 架构 resampling 统计可靠性不足**
- Resampling pool 仅 3³=27 种组合，排除退化样本后有效 bootstrap 样本约 24 个。CI 的 coverage property 远不满足 standard bootstrap theory 要求。Figure 2 的 CI band 视觉上给读者统计严谨的错觉。
- **建议**：(1) 主文明确声明 n=3 bootstrap CI 仅供参考；(2) Figure 2 CI band 附注 "illustrative only; n=3 architectures insufficient for reliable bootstrap inference"；(3) 考虑直接报告三个架构的个体值。
- **Issue Tracker**: R6-W3（自 Round 6 起持续标记）

### Should-Fix（影响评分但不一票否决）

**SF1** [Warning, R2-N3 Must-Fix vs R1-W2 Should-Fix, **分歧**] **单次训练无法分离架构效应与 seed 效应**
- 每个配置仅一次训练 run。Pythia/PolyPythias 的 within-seed Jaccard（0.27–0.39）vs cross-architecture Jaccard（0.09–0.10）提供了 2.7–4.3× 的间接校准，但存在三重 mismatch（scale: 70M vs 340M+, family: Transformer vs hybrid, accuracy regime）。
- R2 认为此为 Must-Fix（无法区分 architecture effect 和 training variation）；R1 REBUT 认为：论文已使用关联性语言（"is associated with"）、提供了间接校准证据、且受限于第三方 model zoo 无法自行补训。
- **Director 判断**：采纳 R1 立场——论文的关联性语言和 Limitations 中的讨论已足够。在 rebuttal 中可强调此点。但如有可能，补充 multi-seed baseline 数据将显著增强论文说服力。
- **Issue Tracker**: R5-W1（自 Round 5 起持续标记，结构性限制）

**SF2** [Warning, R1-W1 + R2 AGREE] **n=5 permutation test power limitation 应更突出**
- §3.5 正确指出 n=5 时只有 |ρ|=1.0 达到 p<.05，但其影响贯穿所有基于 Spearman ρ 的推断。
- **建议**：在 §3.5 或 Limitations 中增加声明："所有基于 Spearman correlation 的推断应被视为 descriptive/exploratory 而非 confirmatory。"
- **Issue Tracker**: R14-W2

**SF3** [Warning, R2-W3 + R1 AGREE] **"Nearly disjoint" / "almost entirely different" 措辞夸大**
- Jaccard ≈ 0.10 vs independence baseline ≈ 0.05（~2× baseline）。Random pairs 也 95% 非重叠。"Nearly disjoint" 忽略 base rate context。
- **建议**：替换为 "largely non-overlapping (J ≈ 0.10, approximately 2× independence baseline)"。Abstract 的 "almost entirely different examples" 也需同步修改。
- **Issue Tracker**: R15-W1（新）

**SF4** [Warning, R1-W5 + R2-W2, 共识] **Routing 的 "proof-of-concept application" 定位过高**
- Routing 仅在 LAMBADA 上有效（+5.3pp），ARC-Easy marginal（+1.0pp），HellaSwag/PIQA 无改善。1/4 有效率的方法不宜定位为 "proof-of-concept application"。
- **建议**：降级为 case study / illustrative example；补充 ensemble averaging baseline。
- **Issue Tracker**: R15-W2（新）

**SF5** [Warning, R1-W4 vs R2 REBUT, **分歧**] **标题覆盖面 vs 实际范围**
- R1 建议标题加限定词（如 "in Three Hybrid..."）。R2 REBUT 认为标题符合 NLP 惯例，但 AGREE 正文应更频繁限定为 "the three architectures studied"。
- **Director 判断**：标题可不改（符合惯例），但 Introduction 和 Conclusion 中需增加 scope 限定。
- **Issue Tracker**: R14-W3

**SF6** [Warning, R1-W3 + R2 AGREE] **二值化 decomposition 信息损失**
- 0.51→0.49 与 0.99→0.01 被等同对待。Appendix O 的 continuous Jaccard 提供了 robustness check，但主文应简要讨论 binarization trade-off。
- **Issue Tracker**: R5-W8（resolved，R15 仅建议主文加简要讨论）

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全达成共识：

1. **LAMBADA convergence overclaiming**（MF1）：Bonferroni p=.170 不显著，但 Abstract/Intro 将其作为核心叙事。需降级为 exploratory。
2. **GDN 16-head confound**（MF2）：排除后 LAMBADA 减弱、MMLU 反转。主文需并列报告。
3. **Bootstrap CI 不可靠**（MF3）：n=3 resampling 无覆盖率保证。需标注 "illustrative only"。
4. **描述性发现是论文真正的贡献**：Per-example Jaccard saturation 和 task-dependent α spectrum 不依赖 convergence test，统计可靠。
5. **Routing 定位过高**（SF4）：降级为 case study。
6. **"Nearly disjoint" 措辞夸大**（SF3）：需 calibrate with base rate。
7. **Overall 3.0 (Findings)**：方法论扎实、研究问题有价值，但推断性 claims 的统计支撑不足，描述性贡献适合 Findings track。

## Reviewer Divergence [REBUT]

1. **单次训练的严重性分级**：R2 认为 Must-Fix（无法区分 architecture vs seed effect 从根本上动摇贡献）；R1 认为 Should-Fix（论文已用关联性语言、提供间接校准、受限于第三方 zoo）。Director 采纳 R1 立场。
2. **新颖性评估**：R2 认为核心发现是 ecological fallacy 的已知实例（Excitement 2.5/5）；R1 认为实证量化有独立价值，不应简化为已知原则（Excitement 3/5）。两者中间值合理。
3. **标题是否需修改**：R1 建议加限定词；R2 认为符合惯例，正文限定即可。Director 采纳 R2 立场。

## Questions（需作者在 rebuttal 中回答）

1. 如果将叙事重心从 convergence 转向 per-example Jaccard saturation，论文的 contribution statement 将如何重新表述？
2. 是否可以在 Table 1 中并列 with/without GDN 的结果？如果不可以，原因是什么？
3. 论文提到 "code and per-example evaluation outputs will be released upon publication"——是否可以在 review 阶段提供匿名化的 code/data 链接以支持 reproducibility？
4. 对于 routing 仅在 LAMBADA 上有效的结果，作者是否考虑过更复杂的 selection mechanism（如 learned routing）？如果是，为什么没有包含？

## Missing References

- Miller & Blume (2026): healthcare ML 中 individual-level prediction instability 的诊断框架（R2 建议）
- Jain et al. (2025, FAccT): Rashomon set 的 allocation multiplicity 实证研究（R2 建议）

## External Review (Stanford Agentic Reviewer)

未配置。

## Visual Layout Check（非评分项）

**状态**：✅ 已完成（耗时 ~3 分钟）

### Findings

| 严重性 | 位置 | 发现 |
|--------|------|------|
| **Critical** | Page 22 | 末页几乎全空——仅顶部 1 行文字 + 页码，>95% 空白。应合并到第 21 页或调整排版消除孤行 |
| Warning | Page 1 | 首页无视觉锚点——整页纯文本（Title/Abstract/Intro）。Figure 1 出现在 p2 顶部，尚可接受 |
| Warning | Pages 3-5 | 连续 3 页纯文本（Related Work + Method），无任何 display item。审稿人容易失去视觉节奏 |
| Warning | Pages 1-8 | 主体 8 页仅 3 个 display items（1 Figure + 2 Tables）。实证分析论文通常 5-8 个。大量结论以纯文本呈现 |
| Warning | Pages 1-8 | 全文仅 2 个 figure（Figure 1 主体 p2，Figure 2 附录 p12），视觉传达严重依赖表格 |
| Info | Page 2 | Figure 1 清晰可读，caption 自包含。子图尺寸偏小，axis label 接近可读下限 |
| Info | Pages 6-7 | Table 1-2 booktabs 风格规范，格式合规 |
| Info | Page 8 | 主文在第 8 页结束，符合 8 页限制。末页填充充足（>90%） |
| Info | Pages 9-10 | 参考文献格式统一，无未解析引用 |
| Info | Pages 11-21 | 附录表格格式一致但几乎无图，视觉单调 |

**排版建议**：(1) 消除 p22 孤行；(2) 主体增加 1-2 个结果可视化图（如 Jaccard heatmap 或 architecture per-example profile 对比）以提升视觉密度和信息传达效率。

## Overall Assessment

**评分**：3.0 / 5（Findings）

**置信度**：4/5

**综合判断**：

论文提出了一个重要且新颖的研究问题——hybrid linear recurrent architectures 中 per-example predictive multiplicity 的系统分析。描述性发现（per-example Jaccard 在 4% attention 即饱和、α 呈 task-dependent variation 0.14–0.30）是扎实的、不依赖小样本推断的直接观察，有独立实证价值。实验设计利用 controlled model zoo 的 matched training conditions 是正确的方法选择。

然而，三个核心问题制约论文达到主会议接收标准：

1. **Overclaiming**：论文的核心叙事仍以 LAMBADA convergence（Bonferroni p = .170，不显著）为支柱，需重构为以描述性发现为主线
2. **GDN confound**：排除 GDN 后主要 convergence 发现减弱/反转，主文未充分并列报告
3. **Bootstrap CI 误导性**：n=3 的 bootstrap CI 在 Figure 2 中给人过强的统计保证

如果论文能：(a) 将叙事重心转向 per-example Jaccard saturation 的描述性发现；(b) 主文并列 with/without GDN 结果；(c) bootstrap CI 标注为 illustrative——当前论文已具备 Findings 接收质量。推断性 claims 的不足是结构性限制（n=3 架构、n=5 ratios、单次 run），需通过 rebuttal 中的 framing 调整而非新实验来解决。

**EMNLP 2026 评分对照**：3.0 = Findings（可被 Findings 接收）。论文的统计诚实性和描述性发现的扎实程度支撑此评分。若 overclaiming 和 GDN confound 在 camera-ready 中充分解决，可稳定在 Findings 级别。

## Detailed Comments

### Abstract
- "almost entirely different examples" 夸大——Jaccard 0.10 vs independence 0.05，应 calibrate with base rate
- "Aggregate trends do not reach statistical significance... yet per-example overlap saturates" 的并置暗示了比数据支持更强的 decoupling pattern
- 建议以 Jaccard saturation 和 α spectrum 为主线重写

### Introduction (§1)
- 第一句 "nearly disjoint" 需替换为 "largely non-overlapping"
- Contribution 2 将 Jaccard saturation 与 aggregate convergence 的 decoupling 列为贡献，但 convergence 一侧不可靠——需重新表述
- BCa CI [-1.0, -0.7] 的引用应降低权重

### Method (§3)
- §3.5 power considerations 应更突出声明所有 Spearman ρ 推断为 descriptive/exploratory
- §3.5 bootstrap CI 的 n=3 limitation 应在此处即声明为 heuristic

### Experiments (§4)
- §4.1 Confidence-based routing 应降级为 case study
- §4.2 decoupling 叙事应以 Jaccard saturation 为主，convergence 为辅
- §4.3 GDN sensitivity 应扩展，Table 1 并列 with/without GDN

### Conclusion (§5)
- 应更频繁限定 scope 为 "the three architectures studied"
- practical implications 可简要讨论何种场景下 per-example divergence 是 practically significant

### Limitations
- 当前 3 段 3 点覆盖恰当
- Single training run 作为 top limitation 的讨论已足够，但可补充 "需要多少 seed replicates 才能量化 bound seed contribution" 的 power analysis

### Format
- ✅ 正文 ≤ 8 页
- ✅ ACL [review] 模板
- ✅ 匿名性完整
- ✅ Limitations + Ethics Statement 存在且不计入页数
- ⚠️ Appendix 末页（p22）孤行需修复
- ⚠️ 主体 display item 密度偏低（3 个 / 8 页）