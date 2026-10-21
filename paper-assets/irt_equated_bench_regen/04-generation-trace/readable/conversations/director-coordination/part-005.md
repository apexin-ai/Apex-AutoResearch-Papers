# Director coordination — Part 5 of 7

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/3d/3daf92a3dbeb151a5ec1.json)

## Round 112

### Tool call

_source line 1134 · 2026-05-22T16:40:02.125411+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每条 Weakness 和 Question，使用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1: 方法严谨性审查\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析迁移到 LLM 基准评测，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现约 27-29% 的题目在 2023 与 2024 模型队列间存在时间性 DIF。论文提出了 cross-subject matching（ΔFPR = 0 保证）的半合成验证框架，并揭示了 DIF 标记与 web-overlap 污染标签的正交性。研究规模大、方法论适配工作扎实，但在 DEFF 校正的内部张力、半合成框架的现实性、以及因果归因模糊性上存在显著的方法论缺陷。\n\n## Strengths\n\n**S1** [规模与系统性] 迄今最大规模的 LLM 基准 DIF 分析（5,227 模型 × 12,508 题目），跨 6 个 METABENCH 基准复现（C% = 17.9-31.3%），random-split sanity check（0.18%）、LOFO 分析、ability-matched 控制等验证链完整。这种规模和系统性在 LLM 评测文献中罕见。\n\n**S2** [Cross-subject matching] 将 purified subtest matching 适配到 LLM 多领域基准场景是一个真正的方法论贡献。ΔFPR = 0 的构造性保证（Section 3.4, Remark）在 single-subject injection 下成立，且多主题注入（Table 6）展示了 graceful degradation（k ≤ 5 时 ΔFPR < 0.007）。这一匹配策略的价值独立于注入机制的现实性。\n\n**S3** [Ground truth 元批判] DIF 标记与 web-overlap 标签的正交性（Jaccard = 0.206, φ = 0.012, enrichment = 0.964; Section 4.3）是一个重要的负面结果。它精确地指出了当前污染检测验证方法论的根本缺陷：global exposure ≠ differential functioning。这一发现对整个污染检测研究方向有指导意义。\n\n**S4** [透明性] 论文在 Limitations 中坦率讨论了 MH 只检测 uniform DIF（17.7% 的 non-uniform DIF 被遗漏）、binary flipping 的局限、因果不可分等核心限制。Appendix A.2 明确承认 2PL 对 MMLU 多维结构拟合不佳。这种透明度值得肯定。\n\n**S5** [多重收敛校正] 三种非独立性校正方法（simple-mean DEFF 29.2%、graduated de-duplication 29.1%、cluster bootstrap 下界 26.7%）收敛于 ~27-29%，以 13.5% 作为保守下界。尽管这些方法并非完全独立（见 W1），收敛本身至少表明结果对校正方法的选择不过度敏感。\n\n## Weaknesses\n\n**W1** [Major] DEFF 校正的内部张力（13.5% vs 27-29%）未充分解决\n\n核心问题：weighted-mean DEFF 给出 C% = 13.5%，而 simple-mean DEFF 给出 29.2%，两者相差一倍以上。论文采用 27-29% 作为主要估计、13.5% 作为保守下界（Section 4.2, Appendix C），但论证不够有力：\n\n(a) 论文以 \"weighted mean 的有效聚类大小 m̄ = 254 意味着每个家族成员功能上相同——对具有不同训练数据的模型而言不现实\" 来否定 weighted-mean 变体。但 simple-mean 同样有问题：它对所有家族赋予相同权重，实际上假设 547 个 Mistral 变体组成的家族与 3 个模型组成的小家族具有相同的聚类结构。真实值可能位于两个极端之间。\n\n(b) 论文引用 Valliant et al. (2013) 指出 \"只有 ~30 个家族时 ICC 估计不稳定\" 来质疑 weighted-mean 变体，但 ICC 不稳定性同样影响 simple-mean 变体——两者使用同一组 ICC 估计值。\n\n(c) 三种 \"收敛\" 方法（simple-mean DEFF、graduated de-duplication、cluster bootstrap 下界）并非独立验证——它们都在处理同一个偏差来源（家族内相关性），使用高度相关的信号。相关方法间的收敛是预期的，不能证明校正水平的正确性。\n\n(d) Appendix C 报告 DEFF = 3.87，但用 mean ICC = 0.047 和 m̄ = 62.8 计算得 1 + 61.8 × 0.047 = 3.905。差异虽小但表明可能使用了未完全说明的 ICC 值。\n\n建议：报告 ICC 在不同家族大小分层下的变化，使用 size-stratified DEFF（如按家族大小分 3-4 个层级分别计算），或至少提供从 13.5% 到 29.2% 的连续参数化曲线，让读者评估哪个估计更合理。\n\n**W2** [Major] \"Graduated de-duplication\" 方法未定义\n\n论文将 \"graduated de-duplication at K=20 (C% = 29.1%)\" 列为三种收敛校正之一（Section 4.2, Table 8），但该方法在正文和附录中**从未被正式定义**。Table 8 仅描述为 \"Remove within-family duplicates\"，但具体操作不明：是每个家族保留至多 K 个模型？还是按某种相似度阈值去重？K=20 中的 K 是指什么参数？这里的 K 与 DIF 分层的 K=5 是否不同？\n\n作为支撑核心定量结论的三种方法之一，缺乏可复现的方法描述是严重的方法论透明度缺陷。\n\n**W3** [Major] 半合成框架的 binary response flipping 过度简化，ΔTPR 的推广性存疑\n\n论文的半合成验证使用均匀的 0→1 二值翻转模拟污染（Section 3.4）。论文正确指出 ΔFPR = 0 保证是匹配策略的固有属性、独立于注入现实性，但 ΔTPR（= +0.508 at p = 0.5）高度依赖于注入机制：\n\n(a) 真实污染产生部分记忆、推理捷径、格式特异性优势——这些产生的信号远比 binary flipping 微弱且复杂。如果真实污染的效应量远小于 binary flipping，实际 TPR 可能远低于 0.508。论文称 binary flipping 是 \"worst-case uniform exploitation pattern\" 产生 \"upper-bound estimates\"，但这仅对单题信号幅度成立。真实污染可能产生跨题目的相关模式（如难度依赖的污染），其对聚合检测力的影响可增可减。\n\n(b) 经验数据中观察到的 difficulty-direction interaction（ρ = -0.597; Section 4.2）强烈暗示真实的差异性行为模式是非均匀的——恰恰是半合成框架无法建模的模式。\n\n(c) 半合成框架仅模拟 incorrect→correct 翻转。真实的时间性变化也可能包括 correct→incorrect（如 RLHF 导致的过度拒绝、格式变化导致的性能退化），这类模式未被测试。\n\n建议：至少补充一种 difficulty-dependent injection（如按题目难度分层设置不同的翻转概率），以及双向翻转实验，展示 detection power 对注入模式的敏感性。\n\n**W4** [Major] 因果模糊性与论文定位之间存在张力\n\n论文承认 DIF 无法区分三种机制——差异性污染、能力演化、训练方法学转变（Section 5.1），但论文的定位仍然紧密围绕 \"contamination\" 展开（标题虽然用了 \"measurement instability\"，但 Introduction 和 Contribution 大量讨论 contamination detection）。\n\nDiscussion 中的四个排除论证（Section 5.1）实际上都比较弱：\n- \"Ability confounds explain at most 2.4 pp\"——仅排除了整体能力差异，未排除题目级别的能力演化\n- \"Domain-level improvement explains <0.1% of item-level DIF variance\"——排除了域级混淆，但不排除题目级能力变化\n- \"Item quality defects are ruled out\"——与污染问题不直接相关\n- \"Web-overlap labels are orthogonal\"——既可解读为 \"web-overlap 是错误的 ground truth\"，也可等价解读为 \"DIF 测量的不是污染\"\n\n关键证据：difficulty-direction interaction（ρ = -0.597：2024 模型在难题上进步、在易题上退步）更符合能力演化模式而非污染模式（污染应当不分难度地提升表现）。论文在 Section 5.1 承认 \"this pattern is more consistent with skill acquisition than contamination\"，但未跟进这一推论的含义：如果主要信号是能力演化而非污染，论文对污染检测文献的相关性将显著降低。\n\n建议：更明确地将论文定位为 \"measurement invariance audit\"，降低对 contamination 的暗示；或提供更强的证据区分三种机制。\n\n**W5** [Minor] p 值阈值在 N = 5,227 下几乎不起过滤作用\n\n论文在 Section 3.2 明确承认 \"only 3 of 3,918 C items lack significance\"——p < 0.05 阈值基本无效。DEFF 校正后有 269 项（6.9%）丧失显著性（均保持 |ΔMH| ≥ 1.5），其中 74% 是 near-miss（p_adj ∈ [0.05, 0.10]）。这意味着：\n- ETS 双重阈值实际退化为单一效应量阈值\n- DEFF 校正仅通过 p 值臂发挥作用（从 31.3% 降至 29.2%，仅 2.1 pp），校正力度有限\n\n这不是方法论错误，但论文应更明确地讨论大样本下 ETS 分类体系的适用性问题。在教育测量中 ETS 双重阈值面对的是数千名考生；5,227 个模型超出了该体系的设计范围。\n\n**W6** [Minor] K 敏感性范围较宽（27-39%），对 K=5 选择的合理性论证不足\n\nSection 4.2 报告 K=3 → 39.4%，K=5 → 31.3%，K=10 → 35.9%，K=20 → 不稳定。K=3 的 39.4% 被归因于 \"under-stratification\"，但为什么 quintile binning（K=5）是正确的分层水平并未从理论上证明。K=10 的非单调峰值被归因于 \"finer strata capturing ability-DIF interactions\"——但 ability-DIF 交互正是 non-uniform DIF 的定义，而 MH 程序仅检测 uniform DIF。如果 K=10 的升高源于 non-uniform DIF 的泄漏，这暗示 MH 的 uniform DIF 估计在不同 K 下不稳定，是一个方法论问题。\n\n此外，K-sensitivity 分析使用的是未经 DEFF 校正的 C%。DEFF 校正后的 K-sensitivity 是什么样的？\n\n**W7** [Minor] ICC 估计方法细节不足\n\nICC = 0.047（median 0.041）是 DEFF 校正的核心参数，但以下信息缺失：\n- 家族定义标准（基于模型名称？架构？训练数据来源？）\n- 不同家族大小下 ICC 的分层分布\n- ICC 估计的置信区间或标准误\n- Singleton 模型（不属于任何家族的模型）如何处理——5,227 总模型中仅 1,884 用于 ICC 估计，其余 3,343 模型的处理方式不明\n- 家族定义的敏感性分析（如将 Llama-2 和 Llama-3 视为同一家族 vs 不同家族时 ICC 如何变化）\n\n**W8** [Minor] Cross-subject ΔFPR = 0 保证假设无跨学科迁移\n\nΔFPR = 0 的构造性证明（Section 3.4, Remark）依赖于 \"向 subject s 注入污染不影响其他学科的表现\"。对 binary flipping 的半合成框架而言这trivially成立，但在真实场景中，在某一 MMLU 学科上的训练可能通过迁移学习提升相关学科的表现。论文通过多主题注入分析（Table 6）部分覆盖了这一问题，但 k=20 时 ΔFPR = 0.069 已不可忽略，且在 DEFF 校正后的保守估计 13.5% 中占比高达 50%（论文在 Section 4.5 明确指出这一点）。\n\n**W9** [Nitpick] 2PL power analysis 在 MMLU 多维结构上的适用性\n\nAppendix A.2 明确承认 \"2PL fit is poor for MMLU's multidimensional structure\"，但 Monte Carlo power analysis 仍使用 2PL 参数（ā = 1.2, b̄ = -0.84）。论文将此定位为 \"triangulation 的一条腿\"，与半合成注入结果互补，这是合理的缓解。但 TPR = 0.68-0.80 被显著地报告在正文中（Section 4.1），可能给读者过高的检测灵敏度信心。\n\n**W10** [Nitpick] 1:1 nearest-neighbor matching 分析细节不足\n\nSection 4.2 报告 \"1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17) yields C% = 28.9% ± 0.1%\"，用于界定能力混淆的上限为 \"at most ~2.4 pp\"。但未说明匹配方法（propensity score? caliper matching?）、匹配质量评估（匹配后的 balance check）、以及样本量减少（从 ~1,800 到 638×2）是否导致统计功效下降从而解释部分 C% 降低。\n\n## Questions\n\n**Q1**: 模型家族如何定义？是基于模型名称前缀的启发式方法，还是更严格的聚类？如果改变家族定义（如将所有 Llama 变体视为一个家族 vs 分为 Llama-2 和 Llama-3），ICC 和 DEFF 如何变化？\n\n**Q2**: 5,227 个模型中仅 1,884 个（来自 30 个 family ≥ 2 的家族）用于 ICC 估计。其余 ~3,343 个 singleton 模型在 DEFF 校正中如何处理？如果它们被视为 DEFF = 1（无需校正），这是否会导致校正的异质性？\n\n**Q3**: 如果 DIF 主要由能力演化驱动（如 difficulty-direction interaction 所暗示），Section 5.2 推荐的 DIF 审计协议的实践价值是什么？如果题目因模型真正进步而 \"更容易\"，将这些题目标记为 \"不稳定\" 并从排名中移除，是否反而损害了评测的有效性？\n\n**Q4**: \"Graduated de-duplication at K=20\" 的具体操作步骤是什么？该方法在论文中从未被正式定义。\n\n**Q5**: 半合成框架是否测试过 correct→incorrect 方向的翻转？训练方法学转变（如 RLHF 过度优化）可能导致模型在某些题目上的表现退化，这种模式下 MH-DIF 的检测力如何？\n\n## Missing References\n\n1. **Kamata & Binici (2003)** — \"Random-Effect DIF Model\" — 提出了在多层数据结构下的随机效应 DIF 模型，直接相关于论文面临的 LLM 非独立性问题。论文引用了 French & Finch (2010) 的层次逻辑回归方法，但未引用更早且理论上更相关的随机效应 DIF 框架。\n\n2. **Alzahrani et al. (2024)** — \"When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards\" — 直接相关于论文的 benchmark instability 主题，讨论了 leaderboard 对基准选择和项目属性的敏感性。\n\n## Overall Assessment\n\n**Soundness**: 3/5\n**Excitement**: 3.5/5\n**Reproducibility**: 3.5/5\n**Reviewer Confidence**: 4/5\n\n**Overall**: 3.0 (Findings) — 论文在规模、系统性和若干方法论贡献（cross-subject matching, ground truth 元批判）上有明确价值，但在核心定量结论（~27-29% 这个数字）的可靠性上存在多个相互关联的方法论缺口：DEFF 校正内部不一致且论证不充分（W1），支撑方法之一未定义（W2），半合成验证的 ΔTPR 推广性存疑（W3），因果归因模糊性与论文定位之间存在未解决的张力（W4）。这些问题中任何单个都不致命，但它们共同削弱了读者对 \"27-29% 的 MMLU 题目存在时间性测量不稳定\" 这一中心主张的信心。\n\n适合 Findings 收录：方法论框架有价值，实证发现（DIF 存在且与 web-overlap 正交）对社区有参考意义，但定量结论的精度和因果解释力不足以支撑主会议录用。",
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每条 Weakness 和 Question，使用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1: 方法严谨性审查\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析迁移到 LLM 基准评测，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现约 27-29% 的题目在 2023 与 2024 模型队列间存在时间性 DIF。论文提出了 cross-subject matching（ΔFPR = 0 保证）的半合成验证框架，并揭示了 DIF 标记与 web-overlap 污染标签的正交性。研究规模大、方法论适配工作扎实，但在 DEFF 校正的内部张力、半合成框架的现实性、以及因果归因模糊性上存在显著的方法论缺陷。\n\n## Strengths\n\n**S1** [规模与系统性] 迄今最大规模的 LLM 基准 DIF 分析（5,227 模型 × 12,508 题目），跨 6 个 METABENCH 基准复现（C% = 17.9-31.3%），random-split sanity check（0.18%）、LOFO 分析、ability-matched 控制等验证链完整。这种规模和系统性在 LLM 评测文献中罕见。\n\n**S2** [Cross-subject matching] 将 purified subtest matching 适配到 LLM 多领域基准场景是一个真正的方法论贡献。ΔFPR = 0 的构造性保证（Section 3.4, Remark）在 single-subject injection 下成立，且多主题注入（Table 6）展示了 graceful degradation（k ≤ 5 时 ΔFPR < 0.007）。这一匹配策略的价值独立于注入机制的现实性。\n\n**S3** [Ground truth 元批判] DIF 标记与 web-overlap 标签的正交性（Jaccard = 0.206, φ = 0.012, enrichment = 0.964; Section 4.3）是一个重要的负面结果。它精确地指出了当前污染检测验证方法论的根本缺陷：global exposure ≠ differential functioning。这一发现对整个污染检测研究方向有指导意义。\n\n**S4** [透明性] 论文在 Limitations 中坦率讨论了 MH 只检测 uniform DIF（17.7% 的 non-uniform DIF 被遗漏）、binary flipping 的局限、因果不可分等核心限制。Appendix A.2 明确承认 2PL 对 MMLU 多维结构拟合不佳。这种透明度值得肯定。\n\n**S5** [多重收敛校正] 三种非独立性校正方法（simple-mean DEFF 29.2%、graduated de-duplication 29.1%、cluster bootstrap 下界 26.7%）收敛于 ~27-29%，以 13.5% 作为保守下界。尽管这些方法并非完全独立（见 W1），收敛本身至少表明结果对校正方法的选择不过度敏感。\n\n## Weaknesses\n\n**W1** [Major] DEFF 校正的内部张力（13.5% vs 27-29%）未充分解决\n\n核心问题：weighted-mean DEFF 给出 C% = 13.5%，而 simple-mean DEFF 给出 29.2%，两者相差一倍以上。论文采用 27-29% 作为主要估计、13.5% 作为保守下界（Section 4.2, Appendix C），但论证不够有力：\n\n(a) 论文以 \"weighted mean 的有效聚类大小 m̄ = 254 意味着每个家族成员功能上相同——对具有不同训练数据的模型而言不现实\" 来否定 weighted-mean 变体。但 simple-mean 同样有问题：它对所有家族赋予相同权重，实际上假设 547 个 Mistral 变体组成的家族与 3 个模型组成的小家族具有相同的聚类结构。真实值可能位于两个极端之间。\n\n(b) 论文引用 Valliant et al. (2013) 指出 \"只有 ~30 个家族时 ICC 估计不稳定\" 来质疑 weighted-mean 变体，但 ICC 不稳定性同样影响 simple-mean 变体——两者使用同一组 ICC 估计值。\n\n(c) 三种 \"收敛\" 方法（simple-mean DEFF、graduated de-duplication、cluster bootstrap 下界）并非独立验证——它们都在处理同一个偏差来源（家族内相关性），使用高度相关的信号。相关方法间的收敛是预期的，不能证明校正水平的正确性。\n\n(d) Appendix C 报告 DEFF = 3.87，但用 mean ICC = 0.047 和 m̄ = 62.8 计算得 1 + 61.8 × 0.047 = 3.905。差异虽小但表明可能使用了未完全说明的 ICC 值。\n\n建议：报告 ICC 在不同家族大小分层下的变化，使用 size-stratified DEFF（如按家族大小分 3-4 个层级分别计算），或至少提供从 13.5% 到 29.2% 的连续参数化曲线，让读者评估哪个估计更合理。\n\n**W2** [Major] \"Graduated de-duplication\" 方法未定义\n\n论文将 \"graduated de-duplication at K=20 (C% = 29.1%)\" 列为三种收敛校正之一（Section 4.2, Table 8），但该方法在正文和附录中**从未被正式定义**。Table 8 仅描述为 \"Remove within-family duplicates\"，但具体操作不明：是每个家族保留至多 K 个模型？还是按某种相似度阈值去重？K=20 中的 K 是指什么参数？这里的 K 与 DIF 分层的 K=5 是否不同？\n\n作为支撑核心定量结论的三种方法之一，缺乏可复现的方法描述是严重的方法论透明度缺陷。\n\n**W3** [Major] 半合成框架的 binary response flipping 过度简化，ΔTPR 的推广性存疑\n\n论文的半合成验证使用均匀的 0→1 二值翻转模拟污染（Section 3.4）。论文正确指出 ΔFPR = 0 保证是匹配策略的固有属性、独立于注入现实性，但 ΔTPR（= +0.508 at p = 0.5）高度依赖于注入机制：\n\n(a) 真实污染产生部分记忆、推理捷径、格式特异性优势——这些产生的信号远比 binary flipping 微弱且复杂。如果真实污染的效应量远小于 binary flipping，实际 TPR 可能远低于 0.508。论文称 binary flipping 是 \"worst-case uniform exploitation pattern\" 产生 \"upper-bound estimates\"，但这仅对单题信号幅度成立。真实污染可能产生跨题目的相关模式（如难度依赖的污染），其对聚合检测力的影响可增可减。\n\n(b) 经验数据中观察到的 difficulty-direction interaction（ρ = -0.597; Section 4.2）强烈暗示真实的差异性行为模式是非均匀的——恰恰是半合成框架无法建模的模式。\n\n(c) 半合成框架仅模拟 incorrect→correct 翻转。真实的时间性变化也可能包括 correct→incorrect（如 RLHF 导致的过度拒绝、格式变化导致的性能退化），这类模式未被测试。\n\n建议：至少补充一种 difficulty-dependent injection（如按题目难度分层设置不同的翻转概率），以及双向翻转实验，展示 detection power 对注入模式的敏感性。\n\n**W4** [Major] 因果模糊性与论文定位之间存在张力\n\n论文承认 DIF 无法区分三种机制——差异性污染、能力演化、训练方法学转变（Section 5.1），但论文的定位仍然紧密围绕 \"contamination\" 展开（标题虽然用了 \"measurement instability\"，但 Introduction 和 Contribution 大量讨论 contamination detection）。\n\nDiscussion 中的四个排除论证（Section 5.1）实际上都比较弱：\n- \"Ability confounds explain at most 2.4 pp\"——仅排除了整体能力差异，未排除题目级别的能力演化\n- \"Domain-level improvement explains <0.1% of item-level DIF variance\"——排除了域级混淆，但不排除题目级能力变化\n- \"Item quality defects are ruled out\"——与污染问题不直接相关\n- \"Web-overlap labels are orthogonal\"——既可解读为 \"web-overlap 是错误的 ground truth\"，也可等价解读为 \"DIF 测量的不是污染\"\n\n关键证据：difficulty-direction interaction（ρ = -0.597：2024 模型在难题上进步、在易题上退步）更符合能力演化模式而非污染模式（污染应当不分难度地提升表现）。论文在 Section 5.1 承认 \"this pattern is more consistent with skill acquisition than contamination\"，但未跟进这一推论的含义：如果主要信号是能力演化而非污染，论文对污染检测文献的相关性将显著降低。\n\n建议：更明确地将论文定位为 \"measurement invariance audit\"，降低对 contamination 的暗示；或提供更强的证据区分三种机制。\n\n**W5** [Minor] p 值阈值在 N = 5,227 下几乎不起过滤作用\n\n论文在 Section 3.2 明确承认 \"only 3 of 3,918 C items lack significance\"——p < 0.05 阈值基本无效。DEFF 校正后有 269 项（6.9%）丧失显著性（均保持 |ΔMH| ≥ 1.5），其中 74% 是 near-miss（p_adj ∈ [0.05, 0.10]）。这意味着：\n- ETS 双重阈值实际退化为单一效应量阈值\n- DEFF 校正仅通过 p 值臂发挥作用（从 31.3% 降至 29.2%，仅 2.1 pp），校正力度有限\n\n这不是方法论错误，但论文应更明确地讨论大样本下 ETS 分类体系的适用性问题。在教育测量中 ETS 双重阈值面对的是数千名考生；5,227 个模型超出了该体系的设计范围。\n\n**W6** [Minor] K 敏感性范围较宽（27-39%），对 K=5 选择的合理性论证不足\n\nSection 4.2 报告 K=3 → 39.4%，K=5 → 31.3%，K=10 → 35.9%，K=20 → 不稳定。K=3 的 39.4% 被归因于 \"under-stratification\"，但为什么 quintile binning（K=5）是正确的分层水平并未从理论上证明。K=10 的非单调峰值被归因于 \"finer strata capturing ability-DIF interactions\"——但 ability-DIF 交互正是 non-uniform DIF 的定义，而 MH 程序仅检测 uniform DIF。如果 K=10 的升高源于 non-uniform DIF 的泄漏，这暗示 MH 的 uniform DIF 估计在不同 K 下不稳定，是一个方法论问题。\n\n此外，K-sensitivity 分析使用的是未经 DEFF 校正的 C%。DEFF 校正后的 K-sensitivity 是什么样的？\n\n**W7** [Minor] ICC 估计方法细节不足\n\nICC = 0.047（median 0.041）是 DEFF 校正的核心参数，但以下信息缺失：\n- 家族定义标准（基于模型名称？架构？训练数据来源？）\n- 不同家族大小下 ICC 的分层分布\n- ICC 估计的置信区间或标准误\n- Singleton 模型（不属于任何家族的模型）如何处理——5,227 总模型中仅 1,884 用于 ICC 估计，其余 3,343 模型的处理方式不明\n- 家族定义的敏感性分析（如将 Llama-2 和 Llama-3 视为同一家族 vs 不同家族时 ICC 如何变化）\n\n**W8** [Minor] Cross-subject ΔFPR = 0 保证假设无跨学科迁移\n\nΔFPR = 0 的构造性证明（Section 3.4, Remark）依赖于 \"向 subject s 注入污染不影响其他学科的表现\"。对 binary flipping 的半合成框架而言这trivially成立，但在真实场景中，在某一 MMLU 学科上的训练可能通过迁移学习提升相关学科的表现。论文通过多主题注入分析（Table 6）部分覆盖了这一问题，但 k=20 时 ΔFPR = 0.069 已不可忽略，且在 DEFF 校正后的保守估计 13.5% 中占比高达 50%（论文在 Section 4.5 明确指出这一点）。\n\n**W9** [Nitpick] 2PL power analysis 在 MMLU 多维结构上的适用性\n\nAppendix A.2 明确承认 \"2PL fit is poor for MMLU's multidimensional structure\"，但 Monte Carlo power analysis 仍使用 2PL 参数（ā = 1.2, b̄ = -0.84）。论文将此定位为 \"triangulation 的一条腿\"，与半合成注入结果互补，这是合理的缓解。但 TPR = 0.68-0.80 被显著地报告在正文中（Section 4.1），可能给读者过高的检测灵敏度信心。\n\n**W10** [Nitpick] 1:1 nearest-neighbor matching 分析细节不足\n\nSection 4.2 报告 \"1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17) yields C% = 28.9% ± 0.1%\"，用于界定能力混淆的上限为 \"at most ~2.4 pp\"。但未说明匹配方法（propensity score? caliper matching?）、匹配质量评估（匹配后的 balance check）、以及样本量减少（从 ~1,800 到 638×2）是否导致统计功效下降从而解释部分 C% 降低。\n\n## Questions\n\n**Q1**: 模型家族如何定义？是基于模型名称前缀的启发式方法，还是更严格的聚类？如果改变家族定义（如将所有 Llama 变体视为一个家族 vs 分为 Llama-2 和 Llama-3），ICC 和 DEFF 如何变化？\n\n**Q2**: 5,227 个模型中仅 1,884 个（来自 30 个 family ≥ 2 的家族）用于 ICC 估计。其余 ~3,343 个 singleton 模型在 DEFF 校正中如何处理？如果它们被视为 DEFF = 1（无需校正），这是否会导致校正的异质性？\n\n**Q3**: 如果 DIF 主要由能力演化驱动（如 difficulty-direction interaction 所暗示），Section 5.2 推荐的 DIF 审计协议的实践价值是什么？如果题目因模型真正进步而 \"更容易\"，将这些题目标记为 \"不稳定\" 并从排名中移除，是否反而损害了评测的有效性？\n\n**Q4**: \"Graduated de-duplication at K=20\" 的具体操作步骤是什么？该方法在论文中从未被正式定义。\n\n**Q5**: 半合成框架是否测试过 correct→incorrect 方向的翻转？训练方法学转变（如 RLHF 过度优化）可能导致模型在某些题目上的表现退化，这种模式下 MH-DIF 的检测力如何？\n\n## Missing References\n\n1. **Kamata & Binici (2003)** — \"Random-Effect DIF Model\" — 提出了在多层数据结构下的随机效应 DIF 模型，直接相关于论文面临的 LLM 非独立性问题。论文引用了 French & Finch (2010) 的层次逻辑回归方法，但未引用更早且理论上更相关的随机效应 DIF 框架。\n\n2. **Alzahrani et al. (2024)** — \"When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards\" — 直接相关于论文的 benchmark instability 主题，讨论了 leaderboard 对基准选择和项目属性的敏感性。\n\n## Overall Assessment\n\n**Soundness**: 3/5\n**Excitement**: 3.5/5\n**Reproducibility**: 3.5/5\n**Reviewer Confidence**: 4/5\n\n**Overall**: 3.0 (Findings) — 论文在规模、系统性和若干方法论贡献（cross-subject matching, ground truth 元批判）上有明确价值，但在核心定量结论（~27-29% 这个数字）的可靠性上存在多个相互关联的方法论缺口：DEFF 校正内部不一致且论证不充分（W1），支撑方法之一未定义（W2），半合成验证的 ΔTPR 推广性存疑（W3），因果归因模糊性与论文定位之间存在未解决的张力（W4）。这些问题中任何单个都不致命，但它们共同削弱了读者对 \"27-29% 的 MMLU 题目存在时间性测量不稳定\" 这一中心主张的信心。\n\n适合 Findings 收录：方法论框架有价值，实证发现（DIF 存在且与 web-overlap 正交）对社区有参考意义，但定量结论的精度和因果解释力不足以支撑主会议录用。",
    "reviewer_id": "2",
    "project": "irt_equated_bench_regen",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-22T16:40:03.791571+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1666
}
```

</details>

---


### Assistant

_source line 1136 · 2026-05-22T16:40:06.533517+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 113

## Round 113

2 recorded events


### User

_source line 1137 · 2026-05-22T16:40:07.647374+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5 (Borderline Conference)，Confidence 4/5。

核心问题三条 Major：
1. **因果模糊性**——DIF 检测"有差异"但无法归因（污染 vs. 能力进化 vs. 训练方法），且论文 Discussion 自己暗示更像能力进化，与 Introduction 的污染叙事矛盾
2. **Ground truth meta-critique 近乎循环论证**——自己定义两个不同概念，验证它们确实不同，不应称为"category error"
3. **方法论新颖性不足**——MH-DIF 原样搬用，跨科目匹配是已有技术的适配

四条 Minor：framing 摇摆、不确定性范围过大（13.5%–53.2%）、MMLU 题目质量排除证据不充分、GSM1K 样本量过小。两条 Nitpick：页面格式激进、scope 暗示与实际不完全匹配。

---

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 意见的逐条回应

## Weaknesses 回应

**[AGREE] R2-W1: 因果模糊性削弱实际意义**

同意，且我在自己的 W4 中提出了高度一致的关切。补充两点：

(1) R2 指出 Section 5.2 的 DIF Audit Protocol 在无因果区分的前提下缺乏操作依据——这比我的批评更具体、更有力。如果 27% DIF 的主体是能力演化，Act 级别（C% ≥ 25% 切换到 stable-item rankings）会系统性低估 2024 模型进步，这确实是一个实践危害。

(2) R2 建议 "利用已知训练数据组成不同的模型子集来分离因果" 是可行的方向。例如，比较 base model 与其 instruction-tuned 变体的 DIF 差异可以隔离 post-training 效应（两者共享预训练数据但 post-training 不同）。论文有 Within-family 比较（Llama-2 vs Llama-3, Table 1: C% = 61.3%），但未沿此方向做因果分离。

**[REBUT] R2-W2: Ground truth meta-critique 循环论证**

部分不同意。R2 的论证是：论文定义了两个不同概念，然后验证它们不同，这是同义反复。但论文的贡献不仅是抽象概念区分，而是具体的**实证发现**：先前多项污染检测工作（Section 2, Related Work 中引用的 Shi et al. 2024, Dekoninck et al. 2024 等）使用 Li et al. (2024) 的 web-overlap 标签作为 ground truth 来评估检测器性能。论文证明这些标签与 DIF 正交（Jaccard = 0.206, enrichment = 0.964, Section 4.3），这意味着：用 web-overlap 标签验证的检测器可能在检测 differential functioning 方面完全无信息量。这是一个有实操意义的发现，不是纯概念层面的同义反复。

但我同意 R2 的措辞建议："meta-critique" 和 "category error" 的措辞确实过强。更准确的框架是 "empirical demonstration that these labels measure a different construct"，而不是暗示先前方法有 "错误"——两种方法测量不同的东西，各有其合理用途。

**[AGREE] R2-W3: 方法论新颖性有限**

同意论文的方法论贡献主要在应用层面。论文自己承认 "We do not modify the MH procedure"（Section 2）。Cross-subject matching 是对 purified subtest matching（Swaminathan & Rogers, 1990; Nandakumar, 1993）的适配，DEFF 校正和 cluster bootstrap 是标准统计方法。

但我对 R2 的严重程度评估有保留：EMNLP 接收大量以 empirical contribution 为主的论文，将标准方法大规模应用于新领域并产生重要实证发现（如 DIF 与 web-overlap 正交、6 个基准的跨基准复现），在我看来可以达到 Findings 的新颖性门槛，尽管对主会议确实偏弱。关键问题不在于方法是否新颖，而在于实证发现是否可靠——而这回到了 W1（因果模糊性）和我的 W1（DEFF 张力）的讨论。

**[AGREE] R2-W4: Framing 摇摆**

完全同意。我在自己的 W4 中从略有不同的角度提出了同一问题。论文在 "psychometric audit"（标题、Section 5.1 承认因果模糊性）和 "contamination critique"（Introduction Contribution 1、大量污染检测文献讨论）之间确实不一致。这两种叙事需要不同的评价标准，混合呈现让读者无法定位论文的核心贡献。

**[AGREE] R2-W5: 核心估计不确定性**

同意，且与我的 W1 高度一致。R2 补充了一个我未充分强调的重要观点：weighted-mean m̄ 是 survey methodology 的标准方法（Kish, 1965），论文将其视为 "unrealistic" 需要更强的论证。Cluster bootstrap CI [26.7%, 53.2%] 的上界 53.2% 几乎是下界的两倍——这个不确定性范围本身就说明定量结论的精度不足。

**[AGREE] R2-W6: MMLU 题目质量处理不充分**

同意。R2 正确指出 CI 上界 1.27 意味着高达 27% 的 enrichment 与数据兼容，且 Gema et al. 的错误标注仅覆盖部分质量问题。"Absence of evidence ≠ evidence of absence" 是准确的方法论批评。论文用不显著的 p 值来 "rule out" item quality defects 在逻辑上不严密。

不过，我认为此问题对核心结论的威胁有限：即使 DIF-C 题目中存在 27% 的错误率偏高，这仍然意味着绝大多数 DIF-C 题目不是由错误驱动的。这更多是 framing 问题（不应说 "ruled out"）而非实质性威胁。

**[AGREE] R2-W7: GSM1K N=33**

同意。论文在 Limitations 中承认 "limited statistical power and is exploratory"，但 Appendix 中以完整 Figure 和详细 Cook's D 分析呈现赋予了过多权重。应缩减为正文中一句话的提及或完全移入补充材料。

**[AGREE] R2-W8: 页面格式激进**

同意。`\enlargethispage*{14\baselineskip}` 在 11pt acl 模板下约增加 2.3-2.5 英寸——这确实异常激进，可能导致文本侵入下边距。结合 `\vspace{-12pt}` 和正文中多处 `\looseness=-1`，论文显然在 8 页限制下极度紧张。这可能导致 Area Chair 格式审查时被标记。

**[AGREE] R2-W9: Abstract 范围暗示**

同意。Abstract 提到 "six METABENCH benchmarks (5,227 models, 27,125 items)" 暗示均匀覆盖，但非 MMLU 基准仅在 Section 4.7 一个小节和 Table 3 中处理，无独立的 DEFF 校正或半合成验证。5,227 是 MMLU 的模型数，GSM8K 实际用 6,702 模型（Appendix E, Table 9），这一差异在 Abstract 中被掩盖。

## Questions 回应

**[AGREE] R2-Q1: Difficulty-direction interaction 的替代解释**

这是一个我未考虑到的有力替代解释。R2 提出：简单题目因更常见于公开语料而在两个队列中均被"均匀污染"（产生 DIF-A），复杂题目因稀缺性更易产生差异化污染（产生 DIF-C）。这一机制同样能解释 ρ = -0.597 的 difficulty-direction pattern，且与污染假说兼容而非能力演化。论文需要提供证据排除（或至少讨论）这一替代解释。可以通过检查 Li et al. 标签中的 web-overlap 覆盖率是否按难度分层来间接测试。

**[AGREE] R2-Q2: DEFF 对异常家族的敏感度**

与我的 W7 一致。Mistral（547 模型，占 ref cohort 51%）对 ICC 估计和 DEFF 的影响应当被量化。

**[AGREE] R2-Q3: 500 模型阈值依据**

R2 准确指出 power analysis 显示 N ≥ 80/cohort 即可，但 Section 5.2 建议 "≥500 模型累积时"。这个 500 是 ad hoc 的——论文未解释为什么不是 160（80×2 cohorts）或 1000。阈值建议需要更明确的统计依据。

**[REBUT] R2-Q4: Growing Pains anchor items 重叠**

这是一个有趣的研究问题，但我认为不应作为本文的 weakness。Growing Pains (Habba et al., 2026) 是并行工作，使用不同方法（IRT calibration）选择 anchor items。论文已在 Related Work (Section 2) 中引用了该工作并说明本文 "complements concurrent work on anchor-item calibration"。要求与并行工作进行实证比较超出了合理范围。

**[AGREE] R2-Q5: 6 个月窗口 C% = 34.35% 高于年度对比**

这确实违反直觉。R2 的猜测（短窗口内模型队列组成更极端）是合理的——6 个月窗口可能导致队列被特定家族主导，从而放大家族特异性 DIF。论文应解释这一现象，或至少将其作为 DEFF/家族效应的证据讨论。

## Missing References 回应

**[AGREE] MMLU-Pro**: Wang et al. (2024) 的 MMLU-Pro 确实直接相关——作为 MMLU 的强化版本，讨论 MMLU 的脆弱性时应当引用。

**[REBUT] Suk and Lyu (2026) 利用不足**: 论文已在 Section 5.1 引用 Suk and Lyu (2026) 并明确指出 "observational DIF alone cannot separate contamination from capability evolution"。在无法获取训练数据的前提下，更深入地应用因果 DIF 方法论是不现实的——因果 DIF 需要因果模型假设和更多数据（如反事实情境），论文的 observational setting 不支持。

## Overall Assessment 回应

R2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于对方法论新颖性的权重：

- R2 将 W3（方法论无创新）列为 Major，但仍给 3.5。我认为 W3 的严重性取决于实证发现的可靠性——如果定量结论可靠，"大规模应用现有方法产生重要发现" 可以达到 Findings 甚至 Borderline Conference。
- 我给出 3.0 的主要原因是 DEFF 内部张力（我的 W1，R2 的 W5）和 graduated de-duplication 未定义（我的 W2）共同削弱了核心定量结论（27-29%）的可信度。如果这个数字不可靠，论文的大部分实证贡献都受影响。
- R2 未提及 graduated de-duplication 未定义的问题（我的 W2），这是一个重要遗漏。作为三种收敛方法之一，该方法在论文中从未被正式描述，这是严重的可复现性缺陷。

综合两份审稿意见，我认为论文在 Findings 和 Borderline Conference 之间，倾向 Findings（3.0-3.5）。核心阻碍主会议录用的问题是：(1) 因果模糊性 + framing 不一致（R1-W4, R2-W1, R2-W4）；(2) 定量结论精度不足（R1-W1, R2-W5）；(3) 方法论新颖性有限（R2-W3）。


---

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 全部意见的逐条回应。主要判断：

- **8/9 条 Weakness 同意**（W1因果模糊性、W3新颖性有限、W4-W9），仅对 W2（ground truth meta-critique 循环论证）部分反驳——论文的实证发现（web-overlap 标签与 DIF 正交）有实操意义，不是纯概念层面的同义反复，但 "meta-critique" 措辞确实过强。
- **4/5 条 Question 同意**，仅对 Q4（与 Growing Pains anchor items 比较）反驳——这超出了对并行工作的合理要求。
- 综合评分：两份审稿意见在因果模糊性、DEFF 张力、framing 不一致三个核心问题上高度一致，论文适合 Findings 收录（3.0-3.5 区间）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1138 · 2026-05-22T16:40:32.801750+00:00_

收到 Reviewer 1 对 Reviewer 2 意见的交叉回应。R1 在绝大多数问题上与 R2 达成共识，仅在 W2（ground truth meta-critique 是否循环论证）和 Q4（与 Growing Pains 实证比较）上部分/完全反驳。

等待 Reviewer 2 对 Reviewer 1 意见的交叉回应，收到后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 114

## Round 114

10 recorded events


### User

_source line 1139 · 2026-05-22T16:42:33.610298+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Weaknesses 回应

**[AGREE] R1-W1: DEFF 校正的内部张力（13.5% vs 27-29%）**

同意这是论文的核心方法论问题之一，与我的 W5 高度一致。R1 的分析比我的更细致，补充了几个我未指出的关键点：

(a) R1 正确指出 simple-mean $\bar{m}$ 同样有问题——假设 547 个 Mistral 变体与 3 个模型的小家族具有相同聚类结构，这显然不合理。我的 W5 仅质疑了论文对 weighted-mean 的 dismiss，R1 进一步揭示了 simple-mean 同样存在偏差，真实值可能在两者之间。

(b) ICC 不稳定性同时影响两种 DEFF 变体这一点很关键——论文选择性地用 Valliant et al. (2013) 攻击 weighted-mean 而不承认同一问题也影响 simple-mean，这是不对称论证。

(c) 三种"收敛"方法的非独立性观察敏锐。它们都在处理同一偏差源（家族内相关性），收敛是预期的而非验证性的。我在评审中未充分意识到这一点。

(d) 数值差异（DEFF = 3.87 vs. 计算值 3.905）虽小，但确实暗示 ICC 值可能有未说明的处理步骤。

补充：尽管如此，即使取最保守的 13.5%，仍是 random-split baseline 0.18% 的 75×（Section 4.2）。因此 DEFF 张力影响的是 DIF 的**量级估计精度**，而非 DIF **存在性**的结论。这一区分在 R1 的评审中未被明确指出。

**[AGREE] R1-W2: Graduated de-duplication 方法未定义**

完全同意。我在审稿时未注意到这一遗漏。论文在 Section 4.2 和 Table 8 多次引用 "graduated de-duplication at K=20 (C% = 29.1%)" 作为三种收敛校正方法之一，但正文、Methods（Section 3）和所有 Appendix 中均未给出该方法的正式定义。这是不可接受的方法论透明度缺陷——读者无法判断该方法的合理性，也无法复现。R1 提出的具体问题（K 的含义、与分层 K=5 的关系、具体操作步骤）均为必须回答的问题。

**[AGREE] R1-W3: Binary response flipping 的推广性存疑——部分同意 ΔTPR 部分**

同意 ΔTPR = +0.508 的推广性有限，但需要区分 ΔFPR 和 ΔTPR 两个贡献：

- ΔFPR = 0 是匹配策略的构造性属性，独立于注入机制——R1 也承认这一点（"这一匹配策略的价值独立于注入机制的现实性"，S2）。这是半合成框架的主要方法论贡献。
- ΔTPR 确实高度依赖注入机制。R1 正确指出真实污染的效应量可能远小于 binary flipping，且 difficulty-direction interaction (ρ = −0.597, Section 4.2) 暗示真实模式是非均匀的——恰恰是该框架无法建模的。

R1 关于 correct→incorrect 翻转的建议（模拟 RLHF 过度优化等退化模式）是有价值的补充实验方向。论文的 Limitations 虽然承认了 "binary response flipping represents a worst-case uniform exploitation pattern"，但未充分讨论该局限对主要结论的影响。

不过，我认为 R1 将此标为 [Major] 略有过重。半合成框架的核心价值在于 ΔFPR = 0 保证（方法论贡献）而非 ΔTPR 的绝对值（经验发现）。论文的主要结论（~27-29% 的时序 DIF）基于真实数据分析，不依赖半合成框架的 TPR 估计。

**[AGREE] R1-W4: 因果模糊性与论文定位的张力**

强烈同意，这与我的 W1 和 W4 高度一致。R1 的分析更为系统，特别是对 Discussion Section 5.1 中四个排除论证的逐一解构：

- "Ability confounds explain at most 2.4 pp" → 仅排除了**整体**能力差异，未排除**题目级别**的能力演化。正确。
- "Domain-level improvement explains <0.1% of item-level DIF variance" → 排除了域级混淆，但不排除题目级能力变化。正确。
- "Item quality defects are ruled out" → 与污染问题不直接相关。正确。
- "Web-overlap labels are orthogonal" → 可等价解读为 "DIF 测量的不是污染"。正确——这恰好是我在 W2 中指出的循环论证问题。

R1 的关键观察——difficulty-direction interaction 更支持能力演化假说——与我的 Q1 提出的质疑方向一致。如果主要信号确实是能力演化，论文对污染检测文献的相关性将显著降低。

**[REBUT] R1-W5: p 值阈值在 N=5,227 下几乎不起过滤作用**

部分反驳。R1 指出的现象是正确的（仅 3/3,918 C items 因 p 值被过滤），但论文已在 Section 3.2 明确承认并处理了这一问题。DEFF 校正的机制**正是**通过降低有效 N 来恢复 p 值的过滤能力：校正后 269 项（6.9%）丧失显著性。这表明论文意识到了大样本下 ETS 双重阈值的退化问题，并通过 DEFF 进行了补偿。

R1 称 "DEFF 校正仅通过 p 值臂发挥作用（从 31.3% 降至 29.2%，仅 2.1 pp），校正力度有限" ——但这恰恰说明大部分 DIF-C 项目具有足够大的效应量**和**足够的统计显著性，即使在校正后仍然成立。2.1 pp 的微小变化本身就是结果稳健性的证据。

不过，R1 关于 ETS 分类体系在超大样本下适用性的更广泛讨论是有价值的补充视角。

**[AGREE] R1-W6: K 敏感性分析的方法论问题**

同意 R1 的核心观察：K=10 的非单调峰值被归因于 "finer strata capturing ability-DIF interactions"，但 ability-DIF 交互即是 non-uniform DIF 的定义——这意味着 K=10 的升高可能是 MH 对 non-uniform DIF 的泄漏，而非更精确的 uniform DIF 估计。这是一个我未注意到的细致方法论问题。

R1 关于 "DEFF 校正后的 K-sensitivity" 的建议也很关键——当前所有 K-sensitivity 分析使用未校正的 C%，而 DEFF 校正后的模式可能不同。

**[AGREE] R1-W7: ICC 估计细节不足**

同意。R1 列举的缺失信息——家族定义标准、分层 ICC 分布、置信区间、singleton 处理、家族定义敏感性——都是复现和评估 DEFF 校正所必需的。特别是 5,227 总模型中仅 1,884 个用于 ICC 估计（来自 30 个 family ≥ 2 的家族），其余 3,343 个 singleton 模型的处理方式确实不明。这与 W1 中的 DEFF 可靠性问题直接相关。

**[REBUT] R1-W8: Cross-subject ΔFPR = 0 的跨学科迁移假设**

部分反驳。R1 的理论观点正确——真实场景中跨学科迁移学习可能违反 ΔFPR = 0 的构造性假设。但论文已通过 Table 6 的多主题注入分析经验性地覆盖了这一问题：k ≤ 5 时 ΔFPR < 0.007，k=10 时 ΔFPR = 0.047±0.022，k=20 时 ΔFPR = 0.069±0.018。论文还在 Section 4.5 明确指出 k=20 时 ΔFPR 在保守估计 13.5% 中占比高达 50%。

关键区分：跨学科迁移在 binary flipping 框架中不存在（R1 也承认 "trivially 成立"），但在真实场景中是否显著取决于 MMLU 学科间的实际迁移幅度。MMLU 57 个学科覆盖范围很广（从抽象代数到临床知识），高度相关的学科对（如 elementary mathematics 和 high school mathematics）可能存在迁移，但跨域迁移（如 virology → jurisprudence）不太可能。论文未讨论学科间相关性结构与 ΔFPR 的关系，这是可以改进之处，但不构成 major 问题。

**[REBUT] R1-W9: 2PL power analysis 的适用性**

反驳。论文将 2PL power analysis 明确定位为 triangulation 的一条腿（Appendix A.2: "the power analysis serves as one leg of a triangulation"），与半合成注入结果互补。这种定位是合理的——parametric 估计（TPR = 0.68–0.80）与 empirical 估计（ΔTPR = +0.508 at p = 0.5）之间的一致性本身就是验证。R1 也承认 "这是合理的缓解"。将此仅标为 Nitpick 已经反映了问题的实际严重程度。

**[AGREE] R1-W10: 1:1 nearest-neighbor matching 细节不足**

同意。匹配方法（propensity score vs. caliper matching）、匹配质量评估、以及样本量减少（~1,800 → 638×2）对统计功效的影响均未报告。这些细节对评估 "ability confound explains at most ~2.4 pp" 这一结论至关重要。

---

## Questions 回应

**[AGREE] R1-Q1**: 家族定义的敏感性分析确实缺失。论文使用 "30 families with family ≥ 2" (Appendix C) 但未说明定义标准。这直接影响 ICC 和 DEFF 估计的可靠性。与我的 Q2 关于 DEFF 对异常值家族敏感度的质疑一致。

**[AGREE] R1-Q2**: Singleton 模型处理方式不明是重要遗漏。如果 3,343 个 singleton 被视为 DEFF = 1，而 1,884 个家族模型被施加 DEFF = 3.87 的校正，则校正在总体上的等效 DEFF 约为 (1,884 × 3.87 + 3,343 × 1.0) / 5,227 ≈ 2.03——远低于论文报告的 3.87。这可能意味着实际校正后的 C% 高于 29.2%，但不确定论文是否按题目级而非模型级应用 DEFF。需要作者澄清。

**[AGREE] R1-Q3**: 这与我的 W1 核心关切一致。如果 DIF 主要由能力演化驱动，DIF 审计协议（Section 5.2）的实践价值需要重新评估。特别是 "Act" 级别（C% ≥ 25%: 切换到 stable-item rankings）可能系统性地低估 2024 模型的真实进步。

**[AGREE] R1-Q4**: 与 R1-W2 重复。Graduated de-duplication 未被定义是严重的方法论透明度问题。

**[AGREE] R1-Q5**: Correct→incorrect 方向的翻转未被测试。这是半合成框架的重要局限。RLHF 过度优化、格式变化等训练方法学转变可能导致选择性退化，MH-DIF 在此模式下的检测力未知。

---

## Missing References 回应

**[AGREE] R1-Missing-1 (Kamata & Binici, 2003)**: 随机效应 DIF 模型直接相关于 LLM 非独立性问题。论文引用了 French & Finch (2010) 但遗漏了更早且理论上更基础的随机效应框架。需要验证该文献的存在性和具体相关性。

**[AGREE] R1-Missing-2 (Alzahrani et al., 2024)**: 如果该文讨论了 leaderboard 对基准选择和项目属性的敏感性，则与本文的 benchmark instability 主题直接相关。同样需要验证。

---

## 总体评价差异

R1 给出 **3.0 (Findings)**，我给出 **3.5 (Borderline Conference)**。差异主要在于：

1. **方法论缺陷的严重程度判断**：R1 将 W1-W4 均标为 Major，认为它们"共同削弱了对中心主张的信心"。我同意 W1（DEFF 张力）和 W4（因果模糊性）是 Major，但 W2（de-duplication 未定义）更多是**报告缺陷**而非**方法缺陷**（补充定义即可解决），W3 的 ΔTPR 推广性问题不影响主要结论（主要结论基于真实数据分析而非半合成 TPR）。因此我认为真正的 Major 问题是 2 个而非 4 个。

2. **实证贡献的权重**：R1 在 Excitement 给出 3.5/5（高于我的 2.5/5），但 Overall 给 3.0（低于我的 3.5）。这似乎不一致——如果 Excitement 较高，Overall 不应更低。我认为论文的实证贡献（大规模 DIF 存在性的确立 + DIF 与 web-overlap 正交性 + 跨基准复制）在 Findings 级别是明确有价值的，争议在于是否达到 Conference 水平。

3. **核心结论的可信度**：R1 认为 "27-29% 这个数字" 的可靠性存疑。我认为 DIF **存在性**（远超 random baseline）的结论是稳健的，争议仅在于**量级**（13.5% 还是 29.2%）。这一区分影响论文是否需要 "大幅修改" vs. "补充分析"。

综合考虑 R1 的分析后，我倾向于维持 **3.5 (Borderline Conference)** 但承认向 3.0 方向倾斜的论据是有力的。如果作者能在修订中：(a) 正式定义 graduated de-duplication，(b) 提供 size-stratified DEFF 分析，(c) 明确承诺 psychometric audit 定位并弱化 contamination framing，论文可以达到 Conference 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-22T16:43:05.993068+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-22T16:43:06.144297+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T16:22:43.380954+00:00\", \"completed_at\": \"2026-05-22T16:26:52.211595+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续 4 页以文字为主（Method 章节 §3.1–§3.4 + semi-synthetic framework），仅 page 4 有两个行间公式作为视觉间断，无 figure/table。审稿人在这一段容易失去注意力。建议将 Table 1（DIF landscape）或 Table 2（structural controls）前移至 Method 段末尾附近，打破纯文本节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Display items 过度聚集：Table 1 + Figure 2 + Table 2 三个 display items 全部集中在一页。与前面 4 页纯文本形成极不均衡的节奏对比。这是 pages 3-6 文字堆积的直接后果——float 被推迟到首次有空间的位置。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主体正文仅 2 个 figure（Figure 1 p2, Figure 2 p7）+ 3 个 table = 5 个 display items / 8 页。对于实证为主的论文处于可接受范围下限（通常 5-8 个）。Figures 3-6 全部在 appendix（page 15-16），审稿人在主体中看到的图偏少。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁，双栏对齐良好。Anonymous ACL submission 标注正确。首页无 display item，但 Figure 1 在 page 2 顶部出现，距首页仅一页翻页，作为视觉锚点及时。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（ICC schematic）传达核心概念（global vs. differential contamination）清晰有效。蓝/橙配色色盲友好，caption 自包含，与 Title-Abstract 叙事一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（dose-response curve）质量良好：线条清晰、有 shaded CI、轴标签可读、legend 位置合理。Table 1 和 Table 2 均使用 booktabs 风格，无竖线。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3（Temporal DIF across benchmarks）格式规范，booktabs 风格。Section 5 Discussion + Section 6 Conclusion 在本页内完成，页面利用率高（>90%）。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"公式 (1)（odds ratio）和 (2)（Δ_MH）渲染正确，无 LaTeX 残留错误，行间公式编号对齐正常。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 章节在 page 9 开始（主体正文 8 页 + Limitations 不计入页数限制），内容充实覆盖方法论边界和泛化限制。References 从 page 9 底部开始，过渡自然。\"}, {\"severity\": \"info\",
…[truncated 910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-22T16:43:06.144867+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-22T16:43:06.195910+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-22T16:46:33.647161+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "issues:\n  # === 历史 issues（来自 Round 10-18，保留上下文） ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大（13.5%-29.2%），核心结论不确定性被低估\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"simple mean m̄=3.87 vs weighted mean m̄=25.4 导致 DEFF 从 1.13 到 12.79。论文未论证偏好哪种估计。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Abstract 改为 bracketed range。但 range 仍显过宽。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"MF1: per-item DEFF 公式已在 §4.2 展示，但三方法收敛论证缺失。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"W-C1: fresh review 仍认为 [13.5%, 29.2%] 范围太宽让读者困惑。三方法收敛 (~27-29%) 论证从未被呈现。DEFF reclassification 实验完成: 100% 重分类由显著性丧失驱动，效应量不变。\"\n      - round: 18\n        reviewers: []\n        note: \"三方法收敛已写入 §4.2: simple DEFF 29.2%, de-dup K=20 29.1%, bootstrap 26.7% → ~27-29%。DEFF reclassification 数据在 §3.2 + §4.2。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Fresh review 再次标记。R1: (a) simple-mean 同样有偏——假设 547 个 Mistral 变体与 3 个模型小家族具有相同聚类结构；(b) ICC 不稳定性同时影响两种变体，论文不对称论证；(c) 三种收敛方法非独立，收敛是预期的不是验证性的；(d) DEFF=3.87 vs 计算值 3.905 有微小差异。R2 同意并补充：即使取 13.5% 仍是 baseline 75×，DIF 存在性稳健但量级精度不足。\"\n    action_items:\n      - round: 10\n        action: \"在 Abstract 和正文中使用 bracketed range 替代单一 31%\"\n        assigned_to: author\n        status: done\n      - round: 16\n        action: \"per-item DEFF 公式可视化\"\n        assigned_to: paper_agent\n        status: done\n      - round: 17\n        action: \"三方法收敛重构\"\n        assigned_to: paper_agent\n        status: done\n      - round: 12\n        action: \"提供 size-stratified DEFF（按家族大小分 3-4 层分别计算）或连续参数化曲线\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"LLM 非独立性假设违反的影响被分散处理，缺乏统一量化框架\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 18\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Cluster bootstrap 下界 26.7% 与 DEFF 下界 13.5% 给出不一致结论。缺乏统一讨论。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"W-C2: 非独立性讨论仍然散落在多个 section。需要统一为 Evidence Chain 1。\"\n      - round: 18\n        reviewers: []\n        note: \"Evidence Chain 1 in §4.2: three corrections converge on ~27-29%, weighted DEFF 13.5% as conservative bound.\"\n      - round: 12\n        reviewers: []\n        note: \"本轮未单独提及此 issue（已并入 R1-W1 的 DEFF 讨论），结构性重组似乎已解决。\"\n    action_items:\n      - round: 10\n        action: \"在正文中集中讨论非独立性\"\n        assigned_to: author\n        status: done\n      - round: 17\n        action: \"结构性重组: Evidence Chain 1 统一非独立性框架\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§4.2 unified non-independence framework with three convergent corrections.\"\n    resolution_round: 18\n\n  - id: \"R1-W3\"\n    summary: \"Semi-synthetic 框架的 binary response flipping 过于简化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R1 标记 Major。R2 partially agree：dose-response 有定量校准价值。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"已添加 upper bound under uniform injection caveat。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Major, R2 降级为非 Major。共识：ΔFPR=0 贡献独立于注入现实性（方法论贡献），但 ΔTPR=+0.508 推广性存疑。difficulty-direction ρ=-0.597 暗示真实模式非均匀，框架无法建模。未测试 correct→incorrect 翻转（RLHF 退化）。R2 认为主要结论不依赖半合成 TPR，因此不构成 Major。\"\n    action_items:\n      - round: 10\n        action: \"讨论至少一种更现实注入模型的 sensitivity\"\n        assigned_to: author\n        status: done\n      - round: 12\n        action: \"补充 difficulty-dependent injection 和双向翻转实验\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Cross-subject matching 的 ΔFPR=0 保证条件过于理想化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"如果 C% 仅 13.5%，k=10 时 ΔFPR=0.017 占比 12.6%。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"已有 plan_034 multi-subject injection 实验数据支撑。Remark 形式化。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Minor (W8), R2 partial rebut。R2 指出 multi-subject injection (Table 6) 已经验性覆盖，且远距学科间迁移不太可能。R1 同意但强调 k=20 时 ΔFPR=0.069 在 13.5% 中占比 50%。\"\n    action_items:\n      - round: 10\n        action: \"在 DEFF-adjusted 下界语境下重新评估 multi-subject FPR inflation\"\n        assigned_to: author\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"缺少 K（分层数）敏感性分析\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"N=5,227 下 K=5 可能过粗，未测试 K=10/20。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"K sensitivity 实验已完成: K∈{3,5,7,10,20}, K≥5 时 max |ΔC%|=4.60pp。\"\n      - round: 18\n        reviewers: []\n        note: \"K sensitivity data in §4.2 + K=10 non-monotonicity explanation.\"\n      - round: 12\n        reviewers: [1]\n        note: \"新问题：K=10 非单调峰值 (35.9%) 被归因于 ability-DIF interactions，但这正是 non-uniform DIF——暗示 MH uniform DIF 估计在不同 K 下不稳定。此外 K-sensitivity 使用未经 DEFF 校正的 C%。\"\n    action_items:\n      - round: 10\n        action: \"补充 K 敏感性分析\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"报告 DEFF 校正后的 K-sensitivity；讨论 K=10 峰值与 non-uniform DIF 泄漏的关系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"大样本下 p 值退化为冗余筛选，ETS 双重阈值实质退化为单一效应量阈值\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"仅 3/3,938 C items 被 p 值重分类。DEFF 校正后情况未报告。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"DEFF reclassification 实验完成: simple DEFF 269/3918 (6.9%) 重分类。\"\n      - round: 18\n        reviewers: []\n        note: \"DEFF reclassification breakdown in §3.2.\"\n      - round: 12\n        reviewers: [1]\n        note: \"R1 Minor (W5)。R2 partial rebut：DEFF 校正已恢复 p 值过滤能力，2.1pp 变化反而是稳健性证据。交叉后 R1 观点有效但不升级。\"\n    action_items:\n      - round: 10\n        action: \"分别报告 DEFF 校正后因效应量和因显著性被重分类的 items 数量\"\n        assigned_to: agent\n        status: done\n    resolution: \"§3.2 reports DEFF reclassification. R2 rebut accepted: DEFF restores p-value filtering.\"\n    resolution_round: 18\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性不足：MH-DIF 是既有标准方法的直接应用\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [2]\n        note: \"R1 rebut：cross-subject matching 是 LLM-specific 贡献。分歧未解决。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Contribution 2 strengthened with LLM-specific challenges。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"好实验被埋没导致贡献不清晰。三条 evidence chain 重组应提升 perceived novelty。\"\n      - round: 18\n        reviewers: []\n        note: \"Structural rewrite organizes experiments into three evidence chains.\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Major (W3)：论文自称 'We do not modify the MH procedure'，cross-subject matching 是已有 purified subtest matching 的适配。R1 同意但认为 empirical contributions 可达 Findings 门槛。共识：方法论贡献在应用层面，不足以单独支撑主会议，但实证发现若可靠则可补偿。\"\n    action_items:\n      - round: 15\n        action: \"强化 Contribution 2 LLM-specific 表述\"\n        assigned_to: paper_agent\n        status: done\n      - round: 17\n        action: \"结构性重组为三条 evidence chain\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"DIF Audit Protocol 阈值缺乏理论依据，显得 ad hoc\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 18\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"15%/25% 阈值 ad hoc。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"W-M5: protocol 仍 ad hoc。需要 empirical justification。\"\n      - round: 18\n        reviewers: []\n        note: \"§5.2 now includes circularity z=-9.5 vs accuracy-gap z=-157.\"\n      - round: 12\n        reviewers: []\n        note: \"本轮未直接标记 protocol 阈值 ad hoc。但因果模糊性问题 (R12-W1) 间接质疑了 protocol 的操作依据。\"\n    action_items:\n      - round: 10\n        action: \"为阈值提供理论或经验依据\"\n        assigned_to: author\n        status: done\n    resolution: \"§5.2 empirically justifies protocol with circularity analysis.\"\n    resolution_round: 18\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力未充分讨论，因果框架缺失\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"DIF 无法区分 contamination vs legitimate improvement vs training methodology shift。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"§5.1 讨论了三种来源，但篇幅不足。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"W-C3: 因果模糊性仍是核心弱点。\"\n      - round: 18\n        reviewers: []\n        note: \"§5.1 restructured as causal decomposition with four exclusion arguments.\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Fresh review 再次标记为核心问题。R1 Major (W4) + R2 Major (W1)：四个排除论证仍然偏弱（仅排除整体能力差异和域级混淆，未排除题目级能力演化）。difficulty-direction ρ=-0.597 更支持能力演化而非污染。论文 framing 在 psychometric audit 和 contamination critique 之间摇摆（R2-W4）。DIF Audit Protocol 在无因果区分前提下缺乏操作依据——Act 级别可能系统性低估 2024 模型进步。\"\n    action_items:\n      - round: 15\n        action: \"§5.1 添加因果讨论\"\n        assigned_to: paper_agent\n        status: done\n      - round: 17\n        action: \"Evidence Chain 2: causal decomposition\"\n        assigned_to: paper_agent\n        status: done\n      - round: 12\n        action: \"明确承诺 psychometric audit 定位，弱化 contamination framing；或设计因果分离分析（如 base model vs instruction-tuned DIF 差异）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W9\"\n    summary: \"Discussion 过于压缩\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 18\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"8 页限制下 Discussion 被过度压缩。\"\n      - round: 18\n        reviewers: []\n        note: \"Discussion expanded: §5.1 + §5.2 with substantive content.\"\n      - round: 12\n        reviewers: []\n        note: \"本轮未提及 Discussion 篇幅问题。但 enlargethispage{14baselineskip} 暗示空间仍非常紧张。\"\n    action_items:\n      - round: 10\n        action: \"扩展 Discussion 篇幅\"\n        assigned_to: author\n        status: done\n    resolution: \"Discussion now spans §5.1 + §5.2.\"\n    resolution_round: 18\n\n  - id: \"R17-M1\"\n    summary: \"三方法收敛论证从未被呈现——scattered evidence 是结构性弱点\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"核心发现: 50+ 实验散落各处。三方法收敛从未在同一段落呈现。\"\n      - round: 18\n        reviewers: []\n        note: \"Structural rewrite complete: three evidence chains.\"\n      - round: 12\n        reviewers: []\n        note: \"本轮未标记结构散乱问题。三方法收敛已在 §4.2 呈现。\"\n    action_items:\n      - round: 17\n        action: \"结构性重组\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Three evidence chains restructured.\"\n    resolution_round: 18\n\n  - id: \"R17-M6\"\n    summary: \"缺少关键引用\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 12\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"Millsap, Magis difR, Valliant 等 6 篇。\"\n      - round: 18\n        reviewers: []\n        note: \"All 6 cited.\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"新增遗漏：R1 提出 Kamata & Binici (2003) 随机效应 DIF、Alzahrani et al. (2024) benchmark sensitivity。R2 提出 MMLU-Pro (Wang et al. 2024)。共 3 篇新增遗漏。\"\n    action_items:\n      - round: 17\n        action: \"补充 6 篇缺失引用\"\n        assigned_to: paper_agent\n        status: done\n      - round: 12\n        action: \"补充 Kamata & Binici 2003, Alzahrani et al. 2024, MMLU-Pro (Wang et al. 2024)\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-m3\"\n    summary: \"Enrichment ratio 仅有点估计，缺 95% CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"Gema enrichment 仅有点估计。\"\n      - round: 18\n        reviewers: []\n        note: \"Both Gema and Li enrichment CIs computed and integrated.\"\n    action_items:\n      - round: 17\n        action: \"计算 enrichment 95% CI\"\n        assigned_to: agent\n        status: done\n    resolution: \"Gema 1.10 [0.92, 1.27]. Li 0.964 [0.94, 1.02].\"\n    resolution_round: 18\n\n  - id: \"R17-m4\"\n    summary: \"Jaccard overlap 缺 permutation null 对照\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"Jaccard 无 null distribution 对照。\"\n      - round: 18\n        reviewers: []\n        note: \"Li Jaccard permutation null completed: observed=0.206, null mean=0.212, p=0.88.\"\n    action_items:\n      - round: 17\n        action: \"Jaccard permutation null distribution\"\n        assigned_to: agent\n        status: done\n    resolution: \"Li Jaccard permutation null in §4.3.\"\n    resolution_round: 18\n\n  # === 本轮新增 issues (Round 12 fresh review) ===\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法从未被正式定义，不可复现\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Major (W2)。论文将 graduated de-duplication at K=20 (C%=29.1%) 列为三种收敛校正之一，但正文、Methods、Appendix 均未给出正式定义。K 的含义、与分层 K=5 的关系、具体操作步骤均不明。R2 完全同意。作为核心定量结论的支撑方法之一，这是不可接受的方法论透明度缺陷。\"\n    action_items:\n      - round: 12\n        action: \"在 Methods 或 Appendix 中正式定义 graduated de-duplication 的操作步骤\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique (Contribution 1) 存在循环论证倾向\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Major (W2)：自己定义两个不同概念然后验证它们不同，近乎同义反复。R1 partial rebut：实证发现（先前检测器使用 web-overlap 作为 ground truth）有实操意义，不是纯概念层面的同义反复——但同意 meta-critique 和 category error 措辞过强。共识：应重新框架为 empirical demonstration that global exposure and differential functioning are orthogonal constructs。\"\n    action_items:\n      - round: 12\n        action: \"将 Contribution 1 从 meta-critique/category error 重新框架为 orthogonal constructs 的实证展示\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W3\"\n    summary: \"ICC 估计方法细节严重不足，影响 DEFF 可靠性评估\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Minor (W7)。缺失：家族定义标准、分层 ICC 分布、ICC 置信区间、singleton 模型处理（5,227 中仅 1,884 用于 ICC 估计，其余 3,343 处理不明）、家族定义敏感性分析。R2 同意 (Q1, Q2)。\"\n    action_items:\n      - round: 12\n        action: \"补充家族定义标准、ICC 分层分布、singleton 处理方式、家族定义敏感性分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W4\"\n    summary: \"MMLU 题目质量排除证据不充分 (absence of evidence ≠ evidence of absence)\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2 Minor (W6)。Gema enrichment CI 上界 1.27 意味着高达 27% 的偏高与数据兼容；Gema 标注仅覆盖部分质量问题；p=0.23 不能 rule out。R1 同意但认为不构成核心威胁——即使 27% 偏高，多数 DIF-C 题目仍非错误驱动。共识：framing 问题（不应说 ruled out）。\"\n    action_items:\n      - round: 12\n        action: \"将 item quality defects 的措辞从 ruled out 改为 no significant enrichment detected\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W5\"\n    summary: \"GSM1K 探索性分析 (N=33) 统计功效不足，呈现权重过高\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Minor (W7)。N=33, p=0.036 在 N=30 下不稳健。Appendix 以完整 Figure + Cook's D 分析赋予过多权重。R1 同意。共识：缩减为一段简短提及或完全移入补充材料。\"\n    action_items:\n      - round: 12\n        action: \"缩减 GSM1K 分析的呈现权重\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W6\"\n    summary: \"页面格式操作激进 (enlargethispage 14baselineskip)\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Nitpick (W8)。14 baselineskip 约增加 2.5 英寸，结合 vspace{-12pt} 和多处 looseness=-1，可能导致文本侵入下边距。R1 同意。可能触发 AC 格式审查。\"\n    action_items:\n      - round: 12\n        action: \"检查是否侵入 margin；考虑压缩 Method 段落释放空间\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W7\"\n    summary: \"Abstract 范围暗示与实际分析覆盖度不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Nitpick (W9)。Abstract 提 6 benchmarks (5,227 models, 27,125 items) 暗示均匀覆盖，实际 MMLU 占绝大部分分析，非 MMLU 仅 §4.7 + Table 3。5,227 是 MMLU 模型数，GSM8K 用 6,702。R1 同意。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 中明确主分析聚焦 MMLU，其余基准为复现验证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W8\"\n    summary: \"1:1 nearest-neighbor matching 方法细节和质量评估缺失\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Nitpick (W10)。匹配方法（propensity score? caliper?）、匹配质量评估（balance check）、样本量减少对功效的影响均未报告。R2 同意。\"\n    action_items:\n      - round: 12\n        action: \"补充 matching 方法细节和 balance check\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "issues:\n  # === 历史 issues（来自 Round 10-18，保留上下文） ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大（13.5%-29.2%），核心结论不确定性被低估\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"simple mean m̄=3.87 vs weighted mean m̄=25.4 导致 DEFF 从 1.13 到 12.79。论文未论证偏好哪种估计。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Abstract 改为 bracketed range。但 range 仍显过宽。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"MF1: per-item DEFF 公式已在 §4.2 展示，但三方法收敛论证缺失。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"W-C1: fresh review 仍认为 [13.5%, 29.2%] 范围太宽让读者困惑。三方法收敛 (~27-29%) 论证从未被呈现。DEFF reclassification 实验完成: 100% 重分类由显著性丧失驱动，效应量不变。\"\n      - round: 18\n        reviewers: []\n        note: \"三方法收敛已写入 §4.2: simple DEFF 29.2%, de-dup K=20 29.1%, bootstrap 26.7% → ~27-29%。DEFF reclassification 数据在 §3.2 + §4.2。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Fresh review 再次标记。R1: (a) simple-mean 同样有偏——假设 547 个 Mistral 变体与 3 个模型小家族具有相同聚类结构；(b) ICC 不稳定性同时影响两种变体，论文不对称论证；(c) 三种收敛方法非独立，收敛是预期的不是验证性的；(d) DEFF=3.87 vs 计算值 3.905 有微小差异。R2 同意并补充：即使取 13.5% 仍是 baseline 75×，DIF 存在性稳健但量级精度不足。\"\n    action_items:\n      - round: 10\n        action: \"在 Abstract 和正文中使用 bracketed range 替代单一 31%\"\n        assigned_to: author\n        status: done\n      - round: 16\n        action: \"per-item DEFF 公式可视化\"\n        assigned_to: paper_agent\n        status: done\n      - round: 17\n        action: \"三方法收敛重构\"\n        assigned_to: paper_agent\n        status: done\n      - round: 12\n        action: \"提供 size-stratified DEFF（按家族大小分 3-4 层分别计算）或连续参数化曲线\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W2\"\n    summary: \"LLM 非独立性假设违反的影响被分散处理，缺乏统一量化框架\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 18\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"Cluster bootstrap 下界 26.7% 与 DEFF 下界 13.5% 给出不一致结论。缺乏统一讨论。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"W-C2: 非独立性讨论仍然散落在多个 section。需要统一为 Evidence Chain 1。\"\n      - round: 18\n        reviewers: []\n        note: \"Evidence Chain 1 in §4.2: three corrections converge on ~27-29%, weighted DEFF 13.5% as conservative bound.\"\n      - round: 12\n        reviewers: []\n        note: \"本轮未单独提及此 issue（已并入 R1-W1 的 DEFF 讨论），结构性重组似乎已解决。\"\n    action_items:\n      - round: 10\n        action: \"在正文中集中讨论非独立性\"\n        assigned_to: author\n        status: done\n      - round: 17\n        action: \"结构性重组: Evidence Chain 1 统一非独立性框架\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"§4.2 unified non-independence framework with three convergent corrections.\"\n    resolution_round: 18\n\n  - id: \"R1-W3\"\n    summary: \"Semi-synthetic 框架的 binary response flipping 过于简化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"R1 标记 Major。R2 partially agree：dose-response 有定量校准价值。\"\n      - round: 16\n        reviewers: [1, 2]\n        note: \"已添加 upper bound under uniform injection caveat。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Major, R2 降级为非 Major。共识：ΔFPR=0 贡献独立于注入现实性（方法论贡献），但 ΔTPR=+0.508 推广性存疑。difficulty-direction ρ=-0.597 暗示真实模式非均匀，框架无法建模。未测试 correct→incorrect 翻转（RLHF 退化）。R2 认为主要结论不依赖半合成 TPR，因此不构成 Major。\"\n    action_items:\n      - round: 10\n        action: \"讨论至少一种更现实注入模型的 sensitivity\"\n        assigned_to: author\n        status: done\n      - round: 12\n        action: \"补充 difficulty-dependent injection 和双向翻转实验\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W4\"\n    summary: \"Cross-subject matching 的 ΔFPR=0 保证条件过于理想化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"如果 C% 仅 13.5%，k=10 时 ΔFPR=0.017 占比 12.6%。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"已有 plan_034 multi-subject injection 实验数据支撑。Remark 形式化。\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Minor (W8), R2 partial rebut。R2 指出 multi-subject injection (Table 6) 已经验性覆盖，且远距学科间迁移不太可能。R1 同意但强调 k=20 时 ΔFPR=0.069 在 13.5% 中占比 50%。\"\n    action_items:\n      - round: 10\n        action: \"在 DEFF-adjusted 下界语境下重新评估 multi-subject FPR inflation\"\n        assigned_to: author\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W5\"\n    summary: \"缺少 K（分层数）敏感性分析\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"N=5,227 下 K=5 可能过粗，未测试 K=10/20。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"K sensitivity 实验已完成: K∈{3,5,7,10,20}, K≥5 时 max |ΔC%|=4.60pp。\"\n      - round: 18\n        reviewers: []\n        note: \"K sensitivity data in §4.2 + K=10 non-monotonicity explanation.\"\n      - round: 12\n        reviewers: [1]\n        note: \"新问题：K=10 非单调峰值 (35.9%) 被归因于 ability-DIF interactions，但这正是 non-uniform DIF——暗示 MH uniform DIF 估计在不同 K 下不稳定。此外 K-sensitivity 使用未经 DEFF 校正的 C%。\"\n    action_items:\n      - round: 10\n        action: \"补充 K 敏感性分析\"\n        assigned_to: agent\n        status: done\n      - round: 12\n        action: \"报告 DEFF 校正后的 K-sensitivity；讨论 K=10 峰值与 non-uniform DIF 泄漏的关系\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-W6\"\n    summary: \"大样本下 p 值退化为冗余筛选，ETS 双重阈值实质退化为单一效应量阈值\"\n    category: method\n    severity: info\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"仅 3/3,938 C items 被 p 值重分类。DEFF 校正后情况未报告。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"DEFF reclassification 实验完成: simple DEFF 269/3918 (6.9%) 重分类。\"\n      - round: 18\n        reviewers: []\n        note: \"DEFF reclassification breakdown in §3.2.\"\n      - round: 12\n        reviewers: [1]\n        note: \"R1 Minor (W5)。R2 partial rebut：DEFF 校正已恢复 p 值过滤能力，2.1pp 变化反而是稳健性证据。交叉后 R1 观点有效但不升级。\"\n    action_items:\n      - round: 10\n        action: \"分别报告 DEFF 校正后因效应量和因显著性被重分类的 items 数量\"\n        assigned_to: agent\n        status: done\n    resolution: \"§3.2 reports DEFF reclassification. R2 rebut accepted: DEFF restores p-value filtering.\"\n    resolution_round: 18\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性不足：MH-DIF 是既有标准方法的直接应用\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [2]\n        note: \"R1 rebut：cross-subject matching 是 LLM-specific 贡献。分歧未解决。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"Contribution 2 strengthened with LLM-specific challenges。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"好实验被埋没导致贡献不清晰。三条 evidence chain 重组应提升 perceived novelty。\"\n      - round: 18\n        reviewers: []\n        note: \"Structural rewrite organizes experiments into three evidence chains.\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Major (W3)：论文自称 'We do not modify the MH procedure'，cross-subject matching 是已有 purified subtest matching 的适配。R1 同意但认为 empirical contributions 可达 Findings 门槛。共识：方法论贡献在应用层面，不足以单独支撑主会议，但实证发现若可靠则可补偿。\"\n    action_items:\n      - round: 15\n        action: \"强化 Contribution 2 LLM-specific 表述\"\n        assigned_to: paper_agent\n        status: done\n      - round: 17\n        action: \"结构性重组为三条 evidence chain\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"DIF Audit Protocol 阈值缺乏理论依据，显得 ad hoc\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 18\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"15%/25% 阈值 ad hoc。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"W-M5: protocol 仍 ad hoc。需要 empirical justification。\"\n      - round: 18\n        reviewers: []\n        note: \"§5.2 now includes circularity z=-9.5 vs accuracy-gap z=-157.\"\n      - round: 12\n        reviewers: []\n        note: \"本轮未直接标记 protocol 阈值 ad hoc。但因果模糊性问题 (R12-W1) 间接质疑了 protocol 的操作依据。\"\n    action_items:\n      - round: 10\n        action: \"为阈值提供理论或经验依据\"\n        assigned_to: author\n        status: done\n    resolution: \"§5.2 empirically justifies protocol with circularity analysis.\"\n    resolution_round: 18\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力未充分讨论，因果框架缺失\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 10\n    last_seen_round: 12\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"DIF 无法区分 contamination vs legitimate improvement vs training methodology shift。\"\n      - round: 15\n        reviewers: [1, 2]\n        note: \"§5.1 讨论了三种来源，但篇幅不足。\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"W-C3: 因果模糊性仍是核心弱点。\"\n      - round: 18\n        reviewers: []\n        note: \"§5.1 restructured as causal decomposition with four exclusion arguments.\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"Fresh review 再次标记为核心问题。R1 Major (W4) + R2 Major (W1)：四个排除论证仍然偏弱（仅排除整体能力差异和域级混淆，未排除题目级能力演化）。difficulty-direction ρ=-0.597 更支持能力演化而非污染。论文 framing 在 psychometric audit 和 contamination critique 之间摇摆（R2-W4）。DIF Audit Protocol 在无因果区分前提下缺乏操作依据——Act 级别可能系统性低估 2024 模型进步。\"\n    action_items:\n      - round: 15\n        action: \"§5.1 添加因果讨论\"\n        assigned_to: paper_agent\n        status: done\n      - round: 17\n        action: \"Evidence Chain 2: causal decomposition\"\n        assigned_to: paper_agent\n        status: done\n      - round: 12\n        action: \"明确承诺 psychometric audit 定位，弱化 contamination framing；或设计因果分离分析（如 base model vs instruction-tuned DIF 差异）\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W9\"\n    summary: \"Discussion 过于压缩\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 18\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"8 页限制下 Discussion 被过度压缩。\"\n      - round: 18\n        reviewers: []\n        note: \"Discussion expanded: §5.1 + §5.2 with substantive content.\"\n      - round: 12\n        reviewers: []\n        note: \"本轮未提及 Discussion 篇幅问题。但 enlargethispage{14baselineskip} 暗示空间仍非常紧张。\"\n    action_items:\n      - round: 10\n        action: \"扩展 Discussion 篇幅\"\n        assigned_to: author\n        status: done\n    resolution: \"Discussion now spans §5.1 + §5.2.\"\n    resolution_round: 18\n\n  - id: \"R17-M1\"\n    summary: \"三方法收敛论证从未被呈现——scattered evidence 是结构性弱点\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"核心发现: 50+ 实验散落各处。三方法收敛从未在同一段落呈现。\"\n      - round: 18\n        reviewers: []\n        note: \"Structural rewrite complete: three evidence chains.\"\n      - round: 12\n        reviewers: []\n        note: \"本轮未标记结构散乱问题。三方法收敛已在 §4.2 呈现。\"\n    action_items:\n      - round: 17\n        action: \"结构性重组\"\n        assigned_to: paper_agent\n        status: done\n    resolution: \"Three evidence chains restructured.\"\n    resolution_round: 18\n\n  - id: \"R17-M6\"\n    summary: \"缺少关键引用\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 17\n    last_seen_round: 12\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"Millsap, Magis difR, Valliant 等 6 篇。\"\n      - round: 18\n        reviewers: []\n        note: \"All 6 cited.\"\n      - round: 12\n        reviewers: [1, 2]\n        note: \"新增遗漏：R1 提出 Kamata & Binici (2003) 随机效应 DIF、Alzahrani et al. (2024) benchmark sensitivity。R2 提出 MMLU-Pro (Wang et al. 2024)。共 3 篇新增遗漏。\"\n    action_items:\n      - round: 17\n        action: \"补充 6 篇缺失引用\"\n        assigned_to: paper_agent\n        status: done\n      - round: 12\n        action: \"补充 Kamata & Binici 2003, Alzahrani et al. 2024, MMLU-Pro (Wang et al. 2024)\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R17-m3\"\n    summary: \"Enrichment ratio 仅有点估计，缺 95% CI\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"Gema enrichment 仅有点估计。\"\n      - round: 18\n        reviewers: []\n        note: \"Both Gema and Li enrichment CIs computed and integrated.\"\n    action_items:\n      - round: 17\n        action: \"计算 enrichment 95% CI\"\n        assigned_to: agent\n        status: done\n    resolution: \"Gema 1.10 [0.92, 1.27]. Li 0.964 [0.94, 1.02].\"\n    resolution_round: 18\n\n  - id: \"R17-m4\"\n    summary: \"Jaccard overlap 缺 permutation null 对照\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 18\n    mentions:\n      - round: 17\n        reviewers: [1, 2]\n        note: \"Jaccard 无 null distribution 对照。\"\n      - round: 18\n        reviewers: []\n        note: \"Li Jaccard permutation null completed: observed=0.206, null mean=0.212, p=0.88.\"\n    action_items:\n      - round: 17\n        action: \"Jaccard permutation null distribution\"\n        assigned_to: agent\n        status: done\n    resolution: \"Li Jaccard permutation null in §4.3.\"\n    resolution_round: 18\n\n  # === 本轮新增 issues (Round 12 fresh review) ===\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法从未被正式定义，不可复现\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Major (W2)。论文将 graduated de-duplication at K=20 (C%=29.1%) 列为三种收敛校正之一，但正文、Methods、Appendix 均未给出正式定义。K 的含义、与分层 K=5 的关系、具体操作步骤均不明。R2 完全同意。作为核心定量结论的支撑方法之一，这是不可接受的方法论透明度缺陷。\"\n    action_items:\n      - round: 12\n        action: \"在 Methods 或 Appendix 中正式定义 graduated de-duplication 的操作步骤\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique (Contribution 1) 存在循环论证倾向\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Major (W2)：自己定义两个不同概念然后验证它们不同，近乎同义反复。R1 partial rebut：实证发现（先前检测器使用 web-overlap 作为 ground truth）有实操意义，不是纯概念层面的同义反复——但同意 meta-critique 和 category error 措辞过强。共识：应重新框架为 empirical demonstration that global exposure and differential functioning are orthogonal constructs。\"\n    action_items:\n      - round: 12\n        action: \"将 Contribution 1 从 meta-critique/category error 重新框架为 orthogonal constructs 的实证展示\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W3\"\n    summary: \"ICC 估计方法细节严重不足，影响 DEFF 可靠性评估\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Minor (W7)。缺失：家族定义标准、分层 ICC 分布、ICC 置信区间、singleton 模型处理（5,227 中仅 1,884 用于 ICC 估计，其余 3,343 处理不明）、家族定义敏感性分析。R2 同意 (Q1, Q2)。\"\n    action_items:\n      - round: 12\n        action: \"补充家族定义标准、ICC 分层分布、singleton 处理方式、家族定义敏感性分析\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W4\"\n    summary: \"MMLU 题目质量排除证据不充分 (absence of evidence ≠ evidence of absence)\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [2]\n        note: \"R2 Minor (W6)。Gema enrichment CI 上界 1.27 意味着高达 27% 的偏高与数据兼容；Gema 标注仅覆盖部分质量问题；p=0.23 不能 rule out。R1 同意但认为不构成核心威胁——即使 27% 偏高，多数 DIF-C 题目仍非错误驱动。共识：framing 问题（不应说 ruled out）。\"\n    action_items:\n      - round: 12\n        action: \"将 item quality defects 的措辞从 ruled out 改为 no significant enrichment detected\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W5\"\n    summary: \"GSM1K 探索性分析 (N=33) 统计功效不足，呈现权重过高\"\n    category: experiment\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Minor (W7)。N=33, p=0.036 在 N=30 下不稳健。Appendix 以完整 Figure + Cook's D 分析赋予过多权重。R1 同意。共识：缩减为一段简短提及或完全移入补充材料。\"\n    action_items:\n      - round: 12\n        action: \"缩减 GSM1K 分析的呈现权重\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W6\"\n    summary: \"页面格式操作激进 (enlargethispage 14baselineskip)\"\n    category: format\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Nitpick (W8)。14 baselineskip 约增加 2.5 英寸，结合 vspace{-12pt} 和多处 looseness=-1，可能导致文本侵入下边距。R1 同意。可能触发 AC 格式审查。\"\n    action_items:\n      - round: 12\n        action: \"检查是否侵入 margin；考虑压缩 Method 段落释放空间\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W7\"\n    summary: \"Abstract 范围暗示与实际分析覆盖度不匹配\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R2 Nitpick (W9)。Abstract 提 6 benchmarks (5,227 models, 27,125 items) 暗示均匀覆盖，实际 MMLU 占绝大部分分析，非 MMLU 仅 §4.7 + Table 3。5,227 是 MMLU 模型数，GSM8K 用 6,702。R1 同意。\"\n    action_items:\n      - round: 12\n        action: \"Abstract 中明确主分析聚焦 MMLU，其余基准为复现验证\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R12-W8\"\n    summary: \"1:1 nearest-neighbor matching 方法细节和质量评估缺失\"\n    category: method\n    severity: info\n    status: open\n    first_raised_round: 12\n    last_seen_round: 12\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"R1 Nitpick (W10)。匹配方法（propensity score? caliper?）、匹配质量评估（balance check）、样本量减少对功效的影响均未报告。R2 同意。\"\n    action_items:\n      - round: 12\n        action: \"补充 matching 方法细节和 balance check\"\n        assigned_to: author\n        status: open\n    resolution: \"\"\n    resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-22T16:46:33.799206+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 18431}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-22T16:49:00.457784+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Temporal Measurement Instability in LLM Benchmarks\n**项目**: irt_equated_bench_regen | **目标 Venue**: EMNLP 2026 (ARR Long Paper) | **截止日期**: 2026-05-25\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目），检测 2023 与 2024 模型队列之间的时序测量不稳定性。经非独立性校正后约 27–29% 的 MMLU 题目表现出大幅时序 DIF（保守下界 13.5%），web-overlap 污染标签与 DIF 标记近乎独立（Jaccard = 0.206）。跨 6 个 METABENCH 基准复现（C% = 17.9–31.3%）。论文提出 cross-subject matching 的半合成验证框架（ΔFPR = 0 保证）和三级 DIF 审计协议。\n\n---\n\n## Strengths\n\n**S1** [规模与系统性] 迄今最大规模的 LLM 基准 DIF 分析（5,227 模型 × 12,508 题目），跨 6 个基准复现，验证链完整（random-split 0.18%、LOFO、ability-matched 控制、5 种 cohort 设计）。这种规模和系统性在 LLM 评测文献中罕见。[R1-S1, R2-S1 AGREE]\n\n**S2** [Cross-subject matching] 将 purified subtest matching 适配到 LLM 多领域基准是真正的方法论贡献。ΔFPR = 0 的构造性保证独立于注入机制，multi-subject injection 的 graceful degradation 分析（Table 6）信息量丰富。[R1-S2, R2-S2 AGREE]\n\n**S3** [Ground truth 正交性发现] DIF 标记与 web-overlap 标签的正交性（Jaccard = 0.206, φ = 0.012, enrichment = 0.964, permutation null p = 0.88）是重要的负面结果，对污染检测验证方法论有指导意义。[R1-S3, R2-S3 AGREE]\n\n**S4** [下游影响分析] DIF-flagged items 集中了区分性信号（z = −8 to −49 vs. random removal），揭示了一个重要张力——移除不稳定题目反而降低基准质量。这一 circularity 发现对社区有价值。[R2-S5]\n\n**S5** [透明性] Limitations 坦率讨论了 MH 仅检测 uniform DIF、binary flipping 局限、因果不可分等核心限制。学术诚实度高。[R1-S4, R2-S4 AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix (阻碍 Conference 录用)\n\n**W-C1** [因果模糊性与 Framing 张力] (R1-W4 Major + R2-W1 Major + R2-W4 Minor → **两位 Reviewer 强共识**)\n\nDIF 无法区分污染、能力演化、训练方法学转变。Discussion §5.1 的四个排除论证偏弱：\n- \"Ability confounds ≤ 2.4 pp\" 仅排除整体能力差异，不排除题目级能力演化\n- \"Domain-level improvement < 0.1% variance\" 排除域级混淆，不排除题目级变化\n- \"Item quality defects ruled out\" 与污染问题不直接相关\n- \"Web-overlap orthogonal\" 可等价解读为\"DIF 测量的不是污染\"\n\nDifficulty-direction interaction (ρ = −0.597) 更支持能力演化（2024 模型在难题进步、易题退步）而非污染。论文在 §5.1 承认 \"more consistent with skill acquisition\"，但 Introduction 的 Contribution 1 仍以 contamination \"ground truth meta-critique\" 定位——两种叙事不兼容。DIF Audit Protocol (§5.2) 在无因果区分下缺乏操作依据：Act 级别 (C% ≥ 25%) 可能系统性低估 2024 模型真实进步。\n\n**W-C2** [DEFF 校正内部张力 + 方法细节缺失] (R1-W1 Major + R1-W2 Major + R2-W5 Minor → **两位 Reviewer 共识**)\n\n(a) Weighted-mean DEFF 给出 C% = 13.5%，simple-mean 给出 29.2%，两倍差距。论文选择性地以 \"m̄=254 意味着家族成员功能相同\" 否定 weighted-mean，但 simple-mean 同样有偏（假设 547 个 Mistral 变体与 3 个模型小家族具有相同聚类结构）。ICC 不稳定性（仅 ~30 个家族）同时影响两种变体，论证不对称。三种 \"收敛\" 方法（simple-mean DEFF / graduated de-dup / cluster bootstrap）都处理同一偏差源，相关方法间的收敛是预期的不是验证性的。\n\n(b) **Graduated de-duplication at K=20 (C% = 29.1%) 从未被正式定义**。作为三种收敛方法之一，K 的含义、操作步骤在正文和附录中均未描述，严重影响可复现性。\n\n(c) ICC 估计细节缺失：家族定义标准、分层 ICC 分布、置信区间、singleton 模型处理（5,227 中仅 1,884 用于 ICC 估计，其余 3,343 处理方式不明）。\n\n**R2 补充**：即使取最保守的 13.5%，仍是 random baseline 的 75×——DIF **存在性**稳健，但**量级**精度不足。\n\n**W-C3** [方法论新颖性有限] (R2-W3 Major + R1 同意但保留 → **共识但严重程度有分歧**)\n\n论文自称 \"We do not modify the MH procedure\"（§2）。Cross-subject matching 是 purified subtest matching (Swaminathan & Rogers, 1990; Nandakumar, 1993) 的适配。DEFF 校正和 cluster bootstrap 是标准统计方法的直接应用。R1 认为实证贡献可补偿方法论新颖性不足（达 Findings 门槛），R2 认为对主会议偏弱。\n\n### Should-Fix (不阻碍录用但需改进)\n\n**W-M1** [Ground truth meta-critique 措辞过强] (R2-W2 Major + R1 partial rebut → **共识调整为 Should-Fix**)\n\nR2 认为 \"category error in prevailing validation methodology\" 近乎循环论证；R1 反驳实证发现有实操意义，但同意措辞过强。**共识**：应从 \"meta-critique / category error\" 重新框架为 \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\"。\n\n**W-M2** [半合成 ΔTPR 推广性存疑] (R1-W3 Major + R2 降级 → **共识调整为 Should-Fix**)\n\nBinary response flipping 是 worst-case uniform pattern，ΔTPR = +0.508 依赖注入机制。Difficulty-direction interaction (ρ = −0.597) 暗示真实模式非均匀。未测试 correct→incorrect 翻转。**但** R2 正确指出：ΔFPR = 0 是方法论贡献（独立于注入现实性），主要结论基于真实数据分析不依赖半合成 TPR。因此降级为 Should-Fix。\n\n**W-M3** [K-sensitivity 的 non-uniform DIF 泄漏] (R1-W6 Minor → R2 AGREE)\n\nK=10 非单调峰值 (35.9%) 被归因于 \"finer strata capturing ability-DIF interactions\"——但 ability-DIF 交互即是 non-uniform DIF，暗示 MH uniform DIF 估计在不同 K 下不稳定。K-sensitivity 使用未经 DEFF 校正的 C%。\n\n**W-M4** [MMLU 题目质量排除证据不足] (R2-W6 Minor → R1 AGREE)\n\nGema enrichment CI 上界 1.27 意味着 27% 偏高与数据兼容。p = 0.23 是 absence of evidence ≠ evidence of absence。应将 \"ruled out\" 改为 \"no significant enrichment detected\"。\n\n**W-M5** [1:1 matching 细节缺失] (R1-W10 Nitpick → R2 AGREE)\n\n匹配方法、balance check、样本量减少对功效影响均未报告。\n\n### Nice-to-Fix (Nitpick)\n\n**W-N1** [GSM1K 探索性分析权重过高] (R2-W7 Minor → R1 AGREE) N=33, p=0.036 不稳健。应缩减呈现。\n\n**W-N2** [页面格式激进] (R2-W8 Nitpick → R1 AGREE) `\\enlargethispage*{14\\baselineskip}` 约增加 2.5 英寸，可能触发 AC 格式审查。\n\n**W-N3** [Abstract 范围暗示不匹配] (R2-W9 Nitpick → R1 AGREE) 5,227 是 MMLU 模型数（GSM8K 用 6,702），非 MMLU 基准仅 §4.7 + Table 3。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n\n1. **因果模糊性是核心弱点**：DIF 无法区分污染 vs 能力演化 vs 训练方法，framing 在两种叙事间摇摆不定\n2. **DEFF 张力未解决**：13.5% vs 29.2% 的两倍差距，论证不对称\n3. **Graduated de-duplication 未定义**：三种核心方法之一不可复现\n4. **方法论贡献在应用层面**：标准方法的大规模应用，非方法创新\n5. **DIF 存在性稳健**（远超 random baseline），争议仅在量级\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | 分歧性质 |\n|------|----|----|----------|\n| Ground truth meta-critique | 有实操意义（partial rebut） | 近乎循环论证 (Major) | R1 认为实证发现有独立价值，R2 认为框架化为 meta-critique 过强。**共识**：措辞需调整 |\n| 半合成 ΔTPR | Major (W3) | 降级为 non-Major | R2 认为主要结论不依赖半合成 TPR |\n| p 值退化 (W5) | Minor | R2 rebut：DEFF 已恢复过滤 | R2 认为 2.1pp 变化是稳健性证据 |\n| Cross-subject 迁移 (W8) | Minor | R2 partial rebut：multi-subject injection 已覆盖 | R2 认为远距学科间迁移不太可能 |\n| Overall 评分 | 3.0 (Findings) | 3.5 (Borderline Conference) | 差异在方法论缺陷严重程度判断和实证贡献权重 |\n\n---\n\n## Questions (需作者澄清)\n\n**Q1**: 模型家族如何定义？将 Llama-2 和 Llama-3 视为同一/不同家族时 ICC 和 DEFF 如何变化？[R1-Q1, R2-Q2]\n\n**Q2**: 5,227 模型中 3,343 个 singleton 在 DEFF 校正中如何处理？如视为 DEFF=1，总体等效 DEFF ≈ 2.03 而非 3.87。[R1-Q2]\n\n**Q3**: Difficulty-direction interaction 的替代解释：简单题目因常见于公开语料而均匀污染（→ DIF-A），复杂题目因稀缺更易差异化污染（→ DIF-C）。能否排除？[R2-Q1]\n\n**Q4**: Graduated de-duplication at K=20 的完整操作步骤？[R1-Q4, R1-W2]\n\n**Q5**: 6 个月窗口 C% = 34.35% 高于年度 31.3%——违反直觉。是否因短窗口队列组成更极端？[R2-Q5]\n\n**Q6**: DIF Audit Protocol 的 \"≥500 模型\" 阈值依据？Power analysis 显示 N ≥ 80/cohort 即可。[R2-Q3]\n\n---\n\n## Missing References\n\n1. **Kamata & Binici (2003)** — Random-Effect DIF Model：多层数据结构下的 DIF，直接相关于 LLM 非独立性 [R1]\n2. **Alzahrani et al. (2024)** — \"When Benchmarks are Targets\"：leaderboard 对基准选择的敏感性 [R1]\n3. **MMLU-Pro (Wang et al., 2024)** — MMLU 强化版本，讨论 MMLU 脆弱性时相关 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 2 warning / 12 info）。\n\n**Warnings**:\n- **Pages 3–6**：连续 4 页纯文字（Method §3.1–§3.4），仅 2 个行间公式作为视觉间断，无 figure/table。审稿人在此段容易失去注意力。建议前移 Table 1 或 Table 2。\n- **Page 7**：Display items 过度聚集——Table 1 + Figure 2 + Table 2 三个 display items 集中在一页，与前面 4 页纯文本形成极不均衡的节奏。\n\n**Info 要点**：\n- 主体正文仅 5 个 display items / 8 页（2 figures + 3 tables），处于可接受范围下限\n- Figure 1 (ICC schematic) 传达核心概念清晰有效，色盲友好\n- 未发现 margin 溢出、section heading 孤悬、widow/orphan 问题\n- Limitations 在 page 9 开始（不计入 8 页限制），符合 ACL 要求\n- References 无未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**置信度**: 4/5（两位 Reviewer 均具有统计方法论和 LLM 评测相关专业知识，交叉讨论充分）\n\n**评分理由**：\n\n论文在执行层面（规模、统计严谨性、多重鲁棒性检验）达到较高水平，cross-subject matching 的 ΔFPR = 0 保证和 DIF-web overlap 正交性发现具有独立价值。但三个相互关联的核心问题阻碍主会议录用：\n\n1. **因果模糊性 + framing 不一致**（W-C1）：论文自己的证据（difficulty-direction ρ = −0.597）更支持能力演化而非污染，但 framing 仍偏向 contamination critique。在无法区分因果来源的前提下，DIF Audit Protocol 缺乏操作依据。这是两位 Reviewer 最强共识的问题。\n\n2. **核心定量结论精度不足**（W-C2）：13.5% vs 29.2% 的两倍差距未被充分解决，三种 \"收敛\" 方法的非独立性削弱了收敛论证的说服力。Graduated de-duplication 未定义是严重的可复现性缺陷。\n\n3. **方法论贡献主要在应用层面**（W-C3）：标准方法的大规模应用对主会议新颖性要求偏弱，需要更强的实证贡献来补偿——而 W-C1 和 W-C2 恰好削弱了实证贡献的可信度。\n\n**适合 Findings 收录**：方法论框架有价值，DIF 存在性结论稳健（远超 random baseline），跨 6 基准复现增强泛化性。如修订中 (a) 承诺 psychometric audit 定位、弱化 contamination framing，(b) 正式定义 graduated de-duplication，(c) 提供 size-stratified DEFF，可考虑 Borderline Conference。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1 \"ground truth meta-critique\" 和 \"category error\" 措辞过强，应重新框架为 \"empirical demonstration of orthogonal constructs\" [R2-W2, R1 partial agree]\n- 贡献列表的 contamination 叙事与 Discussion 的能力演化暗示不一致 [R1-W4, R2-W4]\n\n### §3 Method\n- §3.2: 大样本下 ETS 双重阈值退化为单一效应量阈值的讨论可加强 [R1-W5]\n- §3.4: Cross-subject matching 的跨学科迁移假设应讨论 MMLU 学科间相关性结构 [R1-W8]\n- §3.4: Graduated de-duplication 需要正式定义 [R1-W2]\n\n### §4 Experiments\n- §4.2: K-sensitivity 的 K=10 非单调峰值与 non-uniform DIF 泄漏的关系需讨论；DEFF 校正后的 K-sensitivity 需补充 [R1-W6]\n- §4.2: 1:1 matching 方法和 balance check 需补充 [R1-W10]\n- §4.3: enrichment 的 \"ruled out\" 改为 \"no significant enrichment detected\" [R2-W6]\n- §4.7: GSM1K 分析缩减呈现权重 [R2-W7]\n- §4.7: 6 个月窗口 C% 高于年度对比需解释 [R2-Q5]\n\n### §5 Discussion\n- §5.1: 四个排除论证的逻辑严密性需加强；讨论 R2-Q1 的替代解释 [R1-W4]\n- §5.2: \"≥500 模型\" 阈值需要统计依据 [R2-Q3]\n- §5.2: Act 级别在因果模糊性下的潜在危害需讨论 [R2-W1]\n\n### Appendix\n- Appendix C: ICC 估计细节补充（家族定义、分层分布、singleton 处理） [R1-W7]\n- Appendix C: DEFF 计算值微小差异需说明 [R1-W1(d)]\n\n### 格式\n- `\\enlargethispage*{14\\baselineskip}` 幅度异常，需验证不侵入 margin [R2-W8]\n- Abstract 中 \"5,227 models\" 应明确为 MMLU 模型数 [R2-W9]\n\n### 引用\n- 补充 Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024) [R1-Missing, R2-Missing]",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：Temporal Measurement Instability in LLM Benchmarks\n**项目**: irt_equated_bench_regen | **目标 Venue**: EMNLP 2026 (ARR Long Paper) | **截止日期**: 2026-05-25\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目），检测 2023 与 2024 模型队列之间的时序测量不稳定性。经非独立性校正后约 27–29% 的 MMLU 题目表现出大幅时序 DIF（保守下界 13.5%），web-overlap 污染标签与 DIF 标记近乎独立（Jaccard = 0.206）。跨 6 个 METABENCH 基准复现（C% = 17.9–31.3%）。论文提出 cross-subject matching 的半合成验证框架（ΔFPR = 0 保证）和三级 DIF 审计协议。\n\n---\n\n## Strengths\n\n**S1** [规模与系统性] 迄今最大规模的 LLM 基准 DIF 分析（5,227 模型 × 12,508 题目），跨 6 个基准复现，验证链完整（random-split 0.18%、LOFO、ability-matched 控制、5 种 cohort 设计）。这种规模和系统性在 LLM 评测文献中罕见。[R1-S1, R2-S1 AGREE]\n\n**S2** [Cross-subject matching] 将 purified subtest matching 适配到 LLM 多领域基准是真正的方法论贡献。ΔFPR = 0 的构造性保证独立于注入机制，multi-subject injection 的 graceful degradation 分析（Table 6）信息量丰富。[R1-S2, R2-S2 AGREE]\n\n**S3** [Ground truth 正交性发现] DIF 标记与 web-overlap 标签的正交性（Jaccard = 0.206, φ = 0.012, enrichment = 0.964, permutation null p = 0.88）是重要的负面结果，对污染检测验证方法论有指导意义。[R1-S3, R2-S3 AGREE]\n\n**S4** [下游影响分析] DIF-flagged items 集中了区分性信号（z = −8 to −49 vs. random removal），揭示了一个重要张力——移除不稳定题目反而降低基准质量。这一 circularity 发现对社区有价值。[R2-S5]\n\n**S5** [透明性] Limitations 坦率讨论了 MH 仅检测 uniform DIF、binary flipping 局限、因果不可分等核心限制。学术诚实度高。[R1-S4, R2-S4 AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix (阻碍 Conference 录用)\n\n**W-C1** [因果模糊性与 Framing 张力] (R1-W4 Major + R2-W1 Major + R2-W4 Minor → **两位 Reviewer 强共识**)\n\nDIF 无法区分污染、能力演化、训练方法学转变。Discussion §5.1 的四个排除论证偏弱：\n- \"Ability confounds ≤ 2.4 pp\" 仅排除整体能力差异，不排除题目级能力演化\n- \"Domain-level improvement < 0.1% variance\" 排除域级混淆，不排除题目级变化\n- \"Item quality defects ruled out\" 与污染问题不直接相关\n- \"Web-overlap orthogonal\" 可等价解读为\"DIF 测量的不是污染\"\n\nDifficulty-direction interaction (ρ = −0.597) 更支持能力演化（2024 模型在难题进步、易题退步）而非污染。论文在 §5.1 承认 \"more consistent with skill acquisition\"，但 Introduction 的 Contribution 1 仍以 contamination \"ground truth meta-critique\" 定位——两种叙事不兼容。DIF Audit Protocol (§5.2) 在无因果区分下缺乏操作依据：Act 级别 (C% ≥ 25%) 可能系统性低估 2024 模型真实进步。\n\n**W-C2** [DEFF 校正内部张力 + 方法细节缺失] (R1-W1 Major + R1-W2 Major + R2-W5 Minor → **两位 Reviewer 共识**)\n\n(a) Weighted-mean DEFF 给出 C% = 13.5%，simple-mean 给出 29.2%，两倍差距。论文选择性地以 \"m̄=254 意味着家族成员功能相同\" 否定 weighted-mean，但 simple-mean 同样有偏（假设 547 个 Mistral 变体与 3 个模型小家族具有相同聚类结构）。ICC 不稳定性（仅 ~30 个家族）同时影响两种变体，论证不对称。三种 \"收敛\" 方法（simple-mean DEFF / graduated de-dup / cluster bootstrap）都处理同一偏差源，相关方法间的收敛是预期的不是验证性的。\n\n(b) **Graduated de-duplication at K=20 (C% = 29.1%) 从未被正式定义**。作为三种收敛方法之一，K 的含义、操作步骤在正文和附录中均未描述，严重影响可复现性。\n\n(c) ICC 估计细节缺失：家族定义标准、分层 ICC 分布、置信区间、singleton 模型处理（5,227 中仅 1,884 用于 ICC 估计，其余 3,343 处理方式不明）。\n\n**R2 补充**：即使取最保守的 13.5%，仍是 random baseline 的 75×——DIF **存在性**稳健，但**量级**精度不足。\n\n**W-C3** [方法论新颖性有限] (R2-W3 Major + R1 同意但保留 → **共识但严重程度有分歧**)\n\n论文自称 \"We do not modify the MH procedure\"（§2）。Cross-subject matching 是 purified subtest matching (Swaminathan & Rogers, 1990; Nandakumar, 1993) 的适配。DEFF 校正和 cluster bootstrap 是标准统计方法的直接应用。R1 认为实证贡献可补偿方法论新颖性不足（达 Findings 门槛），R2 认为对主会议偏弱。\n\n### Should-Fix (不阻碍录用但需改进)\n\n**W-M1** [Ground truth meta-critique 措辞过强] (R2-W2 Major + R1 partial rebut → **共识调整为 Should-Fix**)\n\nR2 认为 \"category error in prevailing validation methodology\" 近乎循环论证；R1 反驳实证发现有实操意义，但同意措辞过强。**共识**：应从 \"meta-critique / category error\" 重新框架为 \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\"。\n\n**W-M2** [半合成 ΔTPR 推广性存疑] (R1-W3 Major + R2 降级 → **共识调整为 Should-Fix**)\n\nBinary response flipping 是 worst-case uniform pattern，ΔTPR = +0.508 依赖注入机制。Difficulty-direction interaction (ρ = −0.597) 暗示真实模式非均匀。未测试 correct→incorrect 翻转。**但** R2 正确指出：ΔFPR = 0 是方法论贡献（独立于注入现实性），主要结论基于真实数据分析不依赖半合成 TPR。因此降级为 Should-Fix。\n\n**W-M3** [K-sensitivity 的 non-uniform DIF 泄漏] (R1-W6 Minor → R2 AGREE)\n\nK=10 非单调峰值 (35.9%) 被归因于 \"finer strata capturing ability-DIF interactions\"——但 ability-DIF 交互即是 non-uniform DIF，暗示 MH uniform DIF 估计在不同 K 下不稳定。K-sensitivity 使用未经 DEFF 校正的 C%。\n\n**W-M4** [MMLU 题目质量排除证据不足] (R2-W6 Minor → R1 AGREE)\n\nGema enrichment CI 上界 1.27 意味着 27% 偏高与数据兼容。p = 0.23 是 absence of evidence ≠ evidence of absence。应将 \"ruled out\" 改为 \"no significant enrichment detected\"。\n\n**W-M5** [1:1 matching 细节缺失] (R1-W10 Nitpick → R2 AGREE)\n\n匹配方法、balance check、样本量减少对功效影响均未报告。\n\n### Nice-to-Fix (Nitpick)\n\n**W-N1** [GSM1K 探索性分析权重过高] (R2-W7 Minor → R1 AGREE) N=33, p=0.036 不稳健。应缩减呈现。\n\n**W-N2** [页面格式激进] (R2-W8 Nitpick → R1 AGREE) `\\enlargethispage*{14\\baselineskip}` 约增加 2.5 英寸，可能触发 AC 格式审查。\n\n**W-N3** [Abstract 范围暗示不匹配] (R2-W9 Nitpick → R1 AGREE) 5,227 是 MMLU 模型数（GSM8K 用 6,702），非 MMLU 基准仅 §4.7 + Table 3。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成完全共识 [AGREE]：\n\n1. **因果模糊性是核心弱点**：DIF 无法区分污染 vs 能力演化 vs 训练方法，framing 在两种叙事间摇摆不定\n2. **DEFF 张力未解决**：13.5% vs 29.2% 的两倍差距，论证不对称\n3. **Graduated de-duplication 未定义**：三种核心方法之一不可复现\n4. **方法论贡献在应用层面**：标准方法的大规模应用，非方法创新\n5. **DIF 存在性稳健**（远超 random baseline），争议仅在量级\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | 分歧性质 |\n|------|----|----|----------|\n| Ground truth meta-critique | 有实操意义（partial rebut） | 近乎循环论证 (Major) | R1 认为实证发现有独立价值，R2 认为框架化为 meta-critique 过强。**共识**：措辞需调整 |\n| 半合成 ΔTPR | Major (W3) | 降级为 non-Major | R2 认为主要结论不依赖半合成 TPR |\n| p 值退化 (W5) | Minor | R2 rebut：DEFF 已恢复过滤 | R2 认为 2.1pp 变化是稳健性证据 |\n| Cross-subject 迁移 (W8) | Minor | R2 partial rebut：multi-subject injection 已覆盖 | R2 认为远距学科间迁移不太可能 |\n| Overall 评分 | 3.0 (Findings) | 3.5 (Borderline Conference) | 差异在方法论缺陷严重程度判断和实证贡献权重 |\n\n---\n\n## Questions (需作者澄清)\n\n**Q1**: 模型家族如何定义？将 Llama-2 和 Llama-3 视为同一/不同家族时 ICC 和 DEFF 如何变化？[R1-Q1, R2-Q2]\n\n**Q2**: 5,227 模型中 3,343 个 singleton 在 DEFF 校正中如何处理？如视为 DEFF=1，总体等效 DEFF ≈ 2.03 而非 3.87。[R1-Q2]\n\n**Q3**: Difficulty-direction interaction 的替代解释：简单题目因常见于公开语料而均匀污染（→ DIF-A），复杂题目因稀缺更易差异化污染（→ DIF-C）。能否排除？[R2-Q1]\n\n**Q4**: Graduated de-duplication at K=20 的完整操作步骤？[R1-Q4, R1-W2]\n\n**Q5**: 6 个月窗口 C% = 34.35% 高于年度 31.3%——违反直觉。是否因短窗口队列组成更极端？[R2-Q5]\n\n**Q6**: DIF Audit Protocol 的 \"≥500 模型\" 阈值依据？Power analysis 显示 N ≥ 80/cohort 即可。[R2-Q3]\n\n---\n\n## Missing References\n\n1. **Kamata & Binici (2003)** — Random-Effect DIF Model：多层数据结构下的 DIF，直接相关于 LLM 非独立性 [R1]\n2. **Alzahrani et al. (2024)** — \"When Benchmarks are Targets\"：leaderboard 对基准选择的敏感性 [R1]\n3. **MMLU-Pro (Wang et al., 2024)** — MMLU 强化版本，讨论 MMLU 脆弱性时相关 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 2 warning / 12 info）。\n\n**Warnings**:\n- **Pages 3–6**：连续 4 页纯文字（Method §3.1–§3.4），仅 2 个行间公式作为视觉间断，无 figure/table。审稿人在此段容易失去注意力。建议前移 Table 1 或 Table 2。\n- **Page 7**：Display items 过度聚集——Table 1 + Figure 2 + Table 2 三个 display items 集中在一页，与前面 4 页纯文本形成极不均衡的节奏。\n\n**Info 要点**：\n- 主体正文仅 5 个 display items / 8 页（2 figures + 3 tables），处于可接受范围下限\n- Figure 1 (ICC schematic) 传达核心概念清晰有效，色盲友好\n- 未发现 margin 溢出、section heading 孤悬、widow/orphan 问题\n- Limitations 在 page 9 开始（不计入 8 页限制），符合 ACL 要求\n- References 无未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**置信度**: 4/5（两位 Reviewer 均具有统计方法论和 LLM 评测相关专业知识，交叉讨论充分）\n\n**评分理由**：\n\n论文在执行层面（规模、统计严谨性、多重鲁棒性检验）达到较高水平，cross-subject matching 的 ΔFPR = 0 保证和 DIF-web overlap 正交性发现具有独立价值。但三个相互关联的核心问题阻碍主会议录用：\n\n1. **因果模糊性 + framing 不一致**（W-C1）：论文自己的证据（difficulty-direction ρ = −0.597）更支持能力演化而非污染，但 framing 仍偏向 contamination critique。在无法区分因果来源的前提下，DIF Audit Protocol 缺乏操作依据。这是两位 Reviewer 最强共识的问题。\n\n2. **核心定量结论精度不足**（W-C2）：13.5% vs 29.2% 的两倍差距未被充分解决，三种 \"收敛\" 方法的非独立性削弱了收敛论证的说服力。Graduated de-duplication 未定义是严重的可复现性缺陷。\n\n3. **方法论贡献主要在应用层面**（W-C3）：标准方法的大规模应用对主会议新颖性要求偏弱，需要更强的实证贡献来补偿——而 W-C1 和 W-C2 恰好削弱了实证贡献的可信度。\n\n**适合 Findings 收录**：方法论框架有价值，DIF 存在性结论稳健（远超 random baseline），跨 6 基准复现增强泛化性。如修订中 (a) 承诺 psychometric audit 定位、弱化 contamination framing，(b) 正式定义 graduated de-duplication，(c) 提供 size-stratified DEFF，可考虑 Borderline Conference。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Contribution 1 \"ground truth meta-critique\" 和 \"category error\" 措辞过强，应重新框架为 \"empirical demonstration of orthogonal constructs\" [R2-W2, R1 partial agree]\n- 贡献列表的 contamination 叙事与 Discussion 的能力演化暗示不一致 [R1-W4, R2-W4]\n\n### §3 Method\n- §3.2: 大样本下 ETS 双重阈值退化为单一效应量阈值的讨论可加强 [R1-W5]\n- §3.4: Cross-subject matching 的跨学科迁移假设应讨论 MMLU 学科间相关性结构 [R1-W8]\n- §3.4: Graduated de-duplication 需要正式定义 [R1-W2]\n\n### §4 Experiments\n- §4.2: K-sensitivity 的 K=10 非单调峰值与 non-uniform DIF 泄漏的关系需讨论；DEFF 校正后的 K-sensitivity 需补充 [R1-W6]\n- §4.2: 1:1 matching 方法和 balance check 需补充 [R1-W10]\n- §4.3: enrichment 的 \"ruled out\" 改为 \"no significant enrichment detected\" [R2-W6]\n- §4.7: GSM1K 分析缩减呈现权重 [R2-W7]\n- §4.7: 6 个月窗口 C% 高于年度对比需解释 [R2-Q5]\n\n### §5 Discussion\n- §5.1: 四个排除论证的逻辑严密性需加强；讨论 R2-Q1 的替代解释 [R1-W4]\n- §5.2: \"≥500 模型\" 阈值需要统计依据 [R2-Q3]\n- §5.2: Act 级别在因果模糊性下的潜在危害需讨论 [R2-W1]\n\n### Appendix\n- Appendix C: ICC 估计细节补充（家族定义、分层分布、singleton 处理） [R1-W7]\n- Appendix C: DEFF 计算值微小差异需说明 [R1-W1(d)]\n\n### 格式\n- `\\enlargethispage*{14\\baselineskip}` 幅度异常，需验证不侵入 margin [R2-W8]\n- Abstract 中 \"5,227 models\" 应明确为 MMLU 模型数 [R2-W9]\n\n### 引用\n- 补充 Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024) [R1-Missing, R2-Missing]",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-22T16:49:04.882952+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4425
}
```

</details>

---


### Assistant

_source line 1148 · 2026-05-22T16:49:16.885625+00:00_

审稿报告已投递至 Research Director。

---

**圆桌审稿完成**。两位 Reviewer 经独立初审 + 交叉回应后，在核心问题上达成高度共识：

| 维度 | 评估 |
|------|------|
| **Overall** | **3.0 (Findings)** |
| **阻碍主会议的 3 个核心问题** | 因果模糊性 + framing 摇摆；DEFF 量级精度不足 + de-dup 未定义；方法论新颖性有限 |
| **主要优势** | 规模系统性、cross-subject matching ΔFPR=0、DIF-web overlap 正交性发现 |
| **修订路径** | 承诺 psychometric audit 定位 → 弱化 contamination framing → 定义 de-dup → size-stratified DEFF → 可升至 Borderline Conference |

Issue Tracker 已同步更新（11 个 open issues，7 个 resolved）。视觉审查结果（2 warning）已附入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 115

## Round 115

2 recorded events


### User

_source line 1149 · 2026-05-22T16:49:19.508015+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：R1 的 10 条 Weakness 中我同意 7 条（W1/W2/W3部分/W4/W6/W7/W10），反驳 3 条（W5/W8/W9）。R1 发现了我遗漏的两个重要问题——graduated de-duplication 未定义（W2）和 K-sensitivity 中 non-uniform DIF 泄漏（W6）。我们在因果模糊性（W4≈我的W1）和 DEFF 张力（W1≈我的W5）上高度一致。主要分歧在于整体评分：我维持 3.5 (Borderline Conference)，R1 给 3.0 (Findings)，差异源于对方法论缺陷可修复性和实证贡献权重的不同判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1150 · 2026-05-22T16:49:39.380344+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **Overall Score**: 3.0 (Findings)
- **Reviewer 1**: 3.0 (Findings) | **Reviewer 2**: 3.5 (Borderline Conference)
- **交叉回应**: 两位 Reviewer 完成完整交叉讨论，核心问题达成共识

**三个阻碍主会议录用的核心问题**：
1. **因果模糊性 + framing 不一致** — difficulty-direction ρ=−0.597 更支持能力演化而非污染，但论文仍以 contamination critique 定位
2. **DEFF 定量精度不足** — 13.5% vs 29.2% 两倍差距未解决，graduated de-duplication 未定义
3. **方法论新颖性有限** — 标准方法的大规模应用，无 LLM-specific 方法创新

**可修复路径**：(a) 承诺 psychometric audit 定位、弱化 contamination framing；(b) 正式定义 graduated de-duplication；(c) 提供 size-stratified DEFF → 可升至 Borderline Conference。

Issue tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 116

## Round 116

68 recorded events


### User

_source line 1151 · 2026-05-23T05:50:07.286942+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-23T05:50:13.362869+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-23T05:50:13.413749+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-23T05:50:21.195748+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-23T05:50:21.196336+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-23T05:50:25.714687+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-23T05:50:25.765384+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-23T05:50:28.024918+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1159 · 2026-05-23T05:50:28.226495+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-23T05:50:33.248522+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-23T05:50:34.253213+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-23T05:50:34.404369+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1163 · 2026-05-23T05:50:36.614903+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "description": "Check paper file existence and size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "description": "Check paper file existence and size"
  }
}
```

</details>

---


### Tool result

_source line 1164 · 2026-05-23T05:50:37.518803+00:00_

-rw-r--r-- 1 ubuntu ubuntu 815 May 21 19:15 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
41 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-23T05:50:38.021076+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check submitted PDF existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check submitted PDF existence"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-23T05:50:38.423090+00:00_

-rw-r--r-- 1 ubuntu ubuntu 650220 May 23 03:14 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1167 · 2026-05-23T05:50:38.574111+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1168 · 2026-05-23T05:50:38.574938+00:00_

1	issues:
2	  # === R1-W1: DEFF 校正 (Round 10-20) ===
3	  - id: "R1-W1"
4	    summary: "DEFF 校正范围过大（13.5%-29.2%），核心结论不确定性被低估"
5	    category: method
6	    severity: critical
7	    status: resolved
8	    first_raised_round: 10
9	    last_seen_round: 20
10	    mentions:
11	      - round: 10
12	        reviewers: [1, 2]
13	        note: "simple mean vs weighted mean DEFF 导致范围过宽"
14	      - round: 17
15	        reviewers: [1, 2]
16	        note: "三方法收敛论证缺失"
17	      - round: 18
18	        reviewers: []
19	        note: "三方法收敛写入 §4.2"
20	      - round: 19
21	        reviewers: [1, 2]
22	        note: "De-dup K=20 29.1% 数据不一致被发现（实际 19.7%）。ICC flat across sizes (ρ=-0.009) justifies simple-mean。修正为两方法收敛。"
23	      - round: 20
24	        reviewers: [1, 2]
25	        note: "R20再次要求size-stratified DEFF和连续参数化曲线。论证不对称仍是核心问题。"
26	    action_items:
27	      - round: 19
28	        action: "De-dup 29.1%→19.7%, three→two convergence"
29	        assigned_to: director
30	        status: done
31	      - round: 19
32	        action: "ICC terminology fix (model-level r, not item-level ICC)"
33	        assigned_to: director
34	        status: done
35	      - round: 19
36	        action: "Singleton DEFF scope clarification (99.8% in cohort have families)"
37	        assigned_to: director
38	        status: done
39	      - round: 20
40	        action: "Size-stratified DEFF table in appendix (tab:deff_stratified)"
41	        assigned_to: director
42	        status: done
43	      - round: 20
44	        action: "§4.2 forward reference to size-stratified DEFF (B8: commit 0c3856a)"
45	        assigned_to: agent
46	        status: done
47	    resolution: "Size-stratified DEFF table added (appendix). Per-tier ICC 0.246→0.082 confirms weighted variant over-corrects. Forward reference in §4.2 (rebuttal branch). Family definition sensitivity ≤0.3pp."
48	    resolution_round: 20
49	
50	  # === R2-W4: 因果模糊性 (Round 10-20) ===
51	  - id: "R2-W4"
52	    summary: "Temporal DIF 与 legitimate 能力提升的概念张力，framing 
…[truncated 12695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-23T05:50:41.038320+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found search results related to EMN
…[truncated 1459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6633
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-23T05:50:50.173940+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-23T05:50:51.127949+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" author guidelines 2026 anonymity policy appendix rules"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" author guidelines 2026 anonymity policy appendix rules"
  }
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-23T05:50:52.842052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1173 · 2026-05-23T05:50:52.842432+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-23T05:50:57.360151+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references – so that reviewers' comments can be taken into account.

Review versi
…[truncated 1380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 7186
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-23T05:50:57.862649+00:00_

Web search results for query: ""ACL Rolling Review" author guidelines 2026 anonymity policy appendix rules"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"}]

I found relevant information about the ACL Rolling Review author guidelines and anonymity policy. Here's what the search results show:

## Anonymity Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, submissions will remain anonymous during peer review, but authors are free to post and discuss non-anonymous preprints at any time.

## Submission Requirements

Papers must not include authors' names and affiliations. Additionally, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided. Instead, use citat
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6734
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-23T05:51:07.101189+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.emnlp.org call for main conference papers submission deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.emnlp.org call for main conference papers submission deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 1177 · 2026-05-23T05:51:09.210942+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-23T05:51:09.261623+00:00_

abstract.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-23T05:51:12.725642+00:00_

Web search results for query: "site:2026.emnlp.org call for main conference papers submission deadline commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/275
…[truncated 1113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5624
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-23T05:51:22.566434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-23T05:51:22.918527+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. Existing contamination detectors validate against web-overlap labels that conflate global exposure with differential functioning. We apply differential item functioning (DIF) analysis from educational measurement to six METABENCH benchmarks (5,227 MMLU models, 27,125 items across all six), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF; for MMLU, two convergent non-independence corrections yield approximately 27--29\% (conservative bound: 13.5\%; cluster bootstrap 95\% CI $[26.7\%, 53.2\%]$; random-split baseline 0.18\%). Web-overlap contamination labels are near-independent of DIF flags (Jaccard $= 0.206$): the two constructs---global exposure and differential functioning---are empirically orthogonal. This instability does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals item-level temporal change, with 2024 models gaining on hard items while eroding on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-23T05:51:22.969283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-23T05:51:23.070128+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal measurement instability} as the empirical phenomenon when DIF is detected across time-defined cohorts---a descriptive term denoting systematic changes in measurement properties, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.18\% under a random-split control. This instability does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings); it is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Contamination detectors---from membership inference~\citep{shi2024mink} to performance-based methods~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}---validate primarily against web-overlap labels~\citep{li2024contamination} that measure \emph{global exposure}: whether an item exists in publicly accessible training corpora. Such labels do not capture \emph{differential item functioning}: whether an item behaves differently 
…[truncated 3156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-23T05:51:23.974201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-23T05:51:24.125373+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrat
…[truncated 4788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-23T05:51:24.276368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-23T05:51:24.327119+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 9746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-23T05:51:34.068600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-23T05:51:34.069127+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%]; family-level cluster bootstrap CI $[26.7\%, 53.2\%]$). Two independent non-independence corrections converge on approximately 27--29\%: simple-mean DEFF correction (29.2\%) and family-level cluster bootstrap lower bound (26.7\%). The weighted-mean DEFF variant yields 13.5\%, but its effective cluster size ($\bar{m}{=}254$) implies each family member is functionally identical---unrealistic: within-family s
…[truncated 11421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-23T05:51:34.069327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-23T05:51:34.119797+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage*{10\baselineskip}
4	
5	\vspace{-8pt}
6	\subsection{What Drives Temporal DIF?}
7	\label{sec:disc_temporal}
8	\vspace{-6pt}
9	\looseness=-1
10	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}. Three non-exclusive mechanisms may drive the observed ${\approx}$27--29\% rate: differential contamination, capability evolution, and training methodology shifts. The ETS baseline of 5--15\% C\%~\citep{clauser1998dif} applies to concurrent demographic groups; comparison is illustrative. Four exclusion arguments constrain this ambiguity: ability confounds (${\leq}$2.4~pp; \Cref{sec:temporal}), domain improvement (${<}0.1\%$ of variance), error-item independence ($p = 0.23$;~\citealt{gema2024mmlu}), and web-overlap orthogonality (Jaccard $= 0.206$;~\citealt{li2024contamination}; \Cref{sec:groundtruth}).
11	
12	\looseness=-2
13	The difficulty--direction interaction ($\rho = -0.597$; \Cref{sec:temporal}) is suggestive but not diagnostic: semi-synthetic analysis (\Cref{sec:semisynthetic}) shows uniform and difficulty-dependent injection produce separable $\rho$ signatures ($-0.52$ vs.\@ $+0.77$), but the observed $\rho$ cannot alone distinguish contamination from capability evolution~\citep{suk2026rethinking}. Subject-level instability (22/57 below $\rho = 0.95$) motivates targeted replacement~\citep{zhao2025mmlucf,habba2026growingpains}. Stratifying by model type reveals distinct mechanisms: base models ($N{=}1{,}409$) are 60.1\% reference-favoring with a strong difficulty gradient ($\rho = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring with a near-zero gradient ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). This reversal argues against a pure difficulty-dependent contamination account, which would predict identical DIF direction for both model types. Logistic regression and mixed-mechanism semi-synthetic analysis further confirm this separation 
…[truncated 864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-23T05:51:34.120271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-23T05:51:34.170757+00:00_

1	\vspace{-28pt}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	\vspace{-6pt}
5	
6	\looseness=-1
7	Across six benchmarks, 17.9--31.3\% of items exhibit temporal DIF (${\approx}$27--29\% for MMLU; conservative bound: 13.5\%); rankings are preserved ($\rho \approx 0.997$), motivating routine DIF audits.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-23T05:51:34.171186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-23T05:51:34.171429+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a worst-case injection model; reported $\Delta\mathrm{TPR}$ values are upper-bound estimates, and detection power under realistic contamination patterns (partial memorization, format-specific advantages) is untested. More fundamentally, DIF detects \emph{that} items function differently but cannot determine \emph{why}. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Three convergent corrections (${\approx}$27--29\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.069 when contamination spans ${\geq}20$ subjects. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to open-ended or partial-credit benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-23T05:51:39.241608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-23T05:51:39.543479+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 22136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-23T05:51:39.543890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-23T05:51:39.594359+00:00_

1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: A Robust Method for Detecting Variant Conta
…[truncated 379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-23T05:51:51.140860+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf 2>/dev/null | grep -i \"pages\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf 2>/dev/null | grep -i \"pages\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1201 · 2026-05-23T05:51:51.392230+00:00_

Pages:           17

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-23T05:51:51.392612+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-23T05:51:51.544241+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-23T05:51:56.676287+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-23T05:51:56.727019+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-23T05:52:03.403872+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "config",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "config",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-23T05:52:03.454572+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1208 · 2026-05-23T05:52:07.172899+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
  "description": "Find external review config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
    "description": "Find external review config files"
  }
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-23T05:52:07.424295+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-23T05:52:11.190925+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
  "description": "Find paperreview config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -5",
    "description": "Find paperreview config"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-23T05:52:11.291775+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-23T05:52:29.414892+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-23T05:52:50.705556+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21290
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-23T05:52:52.112904+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献；Limitations 章节不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者信息不可出现在论文中）\n- **附录**: 允许，审稿人可选择性参考\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**。重点评估：\n\n1. **MH-DIF 方法论**: MH procedure 的应用是否正确？ETS C 分类阈值选择是否合理？Cross-subject matching 策略的理论基础是否充分？ΔFPR=0 的 guarantee 是否成立？\n2. **Semi-synthetic 验证框架**: Binary response flipping 是否过于简化？Injection framework 的 ecological validity 如何？Dose-response 曲线是否令人信服？\n3. **统计控制**: DEFF 校正方法是否恰当？Simple-mean vs weighted-mean 的选择依据？Family-level cluster bootstrap 的设计？Leave-one-family-out 分析是否充分？\n4. **实验设计**: 时间队列划分（2023 vs 2024）是否合理？Matched-ability 分析是否足以排除 ability confound？Cross-benchmark replication 的验证力度？\n5. **数据质量**: METABENCH 数据的可靠性？Web-overlap labels 作为外部参照的适当性？\n6. **因果推断**: 论文是否恰当地区分了 DIF 检测（what）与因果归因（why）？Base-vs-instruct decomposition 的推断边界？\n7. **局限性讨论**: Limitations 是否充分覆盖了方法论的已知弱点？\n\n### 输出格式\n请按以下结构撰写审稿意见：\n- **Summary** (2-3 句)\n- **Strengths** (逐条，S1/S2/...)\n- **Weaknesses** (逐条，W-M1/W-M2/... 表示方法类; W-E1/W-E2/... 表示实验类; W-S1/W-S2/... 表示统计类)\n  - 每条标注严重程度: [Must-Fix] / [Should-Fix] / [Minor]\n- **Questions** (Q1/Q2/...)\n- **Missing References** (如有)\n- **Overall Assessment**: 评分 + 置信度\n  - 评分标准 (ARR): 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n请严格、客观、不留情面地评审。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献；Limitations 章节不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者信息不可出现在论文中）\n- **附录**: 允许，审稿人可选择性参考\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**。重点评估：\n\n1. **MH-DIF 方法论**: MH procedure 的应用是否正确？ETS C 分类阈值选择是否合理？Cross-subject matching 策略的理论基础是否充分？ΔFPR=0 的 guarantee 是否成立？\n2. **Semi-synthetic 验证框架**: Binary response flipping 是否过于简化？Injection framework 的 ecological validity 如何？Dose-response 曲线是否令人信服？\n3. **统计控制**: DEFF 校正方法是否恰当？Simple-mean vs weighted-mean 的选择依据？Family-level cluster bootstrap 的设计？Leave-one-family-out 分析是否充分？\n4. **实验设计**: 时间队列划分（2023 vs 2024）是否合理？Matched-ability 分析是否足以排除 ability confound？Cross-benchmark replication 的验证力度？\n5. **数据质量**: METABENCH 数据的可靠性？Web-overlap labels 作为外部参照的适当性？\n6. **因果推断**: 论文是否恰当地区分了 DIF 检测（what）与因果归因（why）？Base-vs-instruct decomposition 的推断边界？\n7. **局限性讨论**: Limitations 是否充分覆盖了方法论的已知弱点？\n\n### 输出格式\n请按以下结构撰写审稿意见：\n- **Summary** (2-3 句)\n- **Strengths** (逐条，S1/S2/...)\n- **Weaknesses** (逐条，W-M1/W-M2/... 表示方法类; W-E1/W-E2/... 表示实验类; W-S1/W-S2/... 表示统计类)\n  - 每条标注严重程度: [Must-Fix] / [Should-Fix] / [Minor]\n- **Questions** (Q1/Q2/...)\n- **Missing References** (如有)\n- **Overall Assessment**: 评分 + 置信度\n  - 评分标准 (ARR): 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n请严格、客观、不留情面地评审。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-23T05:53:08.414910+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16302
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-23T05:53:09.118958+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式合规）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献；Limitations 章节不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者信息不可出现在论文中）\n- **附录**: 允许，审稿人可选择性参考\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 格式合规**。重点评估：\n\n1. **新颖性**: 将 MH-DIF 应用于 LLM benchmark temporal comparability 是否有足够的方法论新颖性？还是仅仅是已有方法的直接应用？三个贡献点（orthogonal constructs / audit framework / temporal instability at scale）是否有真正的 novelty？\n2. **贡献定位与 framing**: 贡献是方法论还是实证性的？Framing 是否准确反映了实际贡献？Claims 是否与证据匹配？是否有 overclaiming？\n3. **Related Work 覆盖**: 是否遗漏了重要的相关工作？与 Growing Pains (Habba et al. 2026)、contamination detection 文献、IRT in NLP 文献的关系是否讨论充分？定位是否准确？\n4. **叙事完整性**: 从 Introduction 的动机建立到 Conclusion 的收束，论证链是否完整？各章节之间的逻辑衔接是否流畅？是否有重要的论证缺口？\n5. **格式合规**:\n   - 正文是否在 8 页内？\n   - Limitations 章节是否存在且放置正确（结论后、参考文献前）？\n   - 是否使用了 ACL 模板？\n   - 匿名性：是否有泄漏作者身份的信息？（检查 anonymous 代码链接、自引方式等）\n   - `\\enlargethispage` 使用是否过度？\n6. **写作质量**: 专业术语使用是否一致？论文是否过于 notation-heavy？可读性如何？\n7. **Ethics & Broader Impact**: 是否有伦理考虑缺失？\n\n### 输出格式\n请按以下结构撰写审稿意见：\n- **Summary** (2-3 句)\n- **Strengths** (逐条，S1/S2/...)\n- **Weaknesses** (逐条，W-N1/W-N2/... 表示新颖性类; W-C1/W-C2/... 表示完整性类; W-F1/W-F2/... 表示格式类; W-W1/W-W2/... 表示写作类)\n  - 每条标注严重程度: [Must-Fix] / [Should-Fix] / [Minor]\n- **Questions** (Q1/Q2/...)\n- **Missing References** (如有)\n- **Overall Assessment**: 评分 + 置信度\n  - 评分标准 (ARR): 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n请严格、客观、不留情面地评审。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式合规）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献；Limitations 章节不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（作者信息不可出现在论文中）\n- **附录**: 允许，审稿人可选择性参考\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_13/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 格式合规**。重点评估：\n\n1. **新颖性**: 将 MH-DIF 应用于 LLM benchmark temporal comparability 是否有足够的方法论新颖性？还是仅仅是已有方法的直接应用？三个贡献点（orthogonal constructs / audit framework / temporal instability at scale）是否有真正的 novelty？\n2. **贡献定位与 framing**: 贡献是方法论还是实证性的？Framing 是否准确反映了实际贡献？Claims 是否与证据匹配？是否有 overclaiming？\n3. **Related Work 覆盖**: 是否遗漏了重要的相关工作？与 Growing Pains (Habba et al. 2026)、contamination detection 文献、IRT in NLP 文献的关系是否讨论充分？定位是否准确？\n4. **叙事完整性**: 从 Introduction 的动机建立到 Conclusion 的收束，论证链是否完整？各章节之间的逻辑衔接是否流畅？是否有重要的论证缺口？\n5. **格式合规**:\n   - 正文是否在 8 页内？\n   - Limitations 章节是否存在且放置正确（结论后、参考文献前）？\n   - 是否使用了 ACL 模板？\n   - 匿名性：是否有泄漏作者身份的信息？（检查 anonymous 代码链接、自引方式等）\n   - `\\enlargethispage` 使用是否过度？\n6. **写作质量**: 专业术语使用是否一致？论文是否过于 notation-heavy？可读性如何？\n7. **Ethics & Broader Impact**: 是否有伦理考虑缺失？\n\n### 输出格式\n请按以下结构撰写审稿意见：\n- **Summary** (2-3 句)\n- **Strengths** (逐条，S1/S2/...)\n- **Weaknesses** (逐条，W-N1/W-N2/... 表示新颖性类; W-C1/W-C2/... 表示完整性类; W-F1/W-F2/... 表示格式类; W-W1/W-W2/... 表示写作类)\n  - 每条标注严重程度: [Must-Fix] / [Should-Fix] / [Minor]\n- **Questions** (Q1/Q2/...)\n- **Missing References** (如有)\n- **Overall Assessment**: 评分 + 置信度\n  - 评分标准 (ARR): 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n请严格、客观、不留情面地评审。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-23T05:53:10.731575+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1612
}
```

</details>

---


### Assistant

_source line 1218 · 2026-05-23T05:53:22.814879+00:00_

Round 1 审稿已启动：

- **视觉审查 Agent**: 已派发（fire-and-forget）
- **Reviewer 1**（方法严谨性 + 实验设计）: 已分配
- **Reviewer 2**（新颖性 + 完整性 + 格式合规）: 已分配

等待两位 Reviewer 独立初审完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1219 · 2026-05-23T05:58:09.774632+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — Round 1 审稿意见

### Summary

本文将教育测量学中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items），发现 2023 与 2024 模型群组间约 27–29% 的 MMLU 题目存在时序 DIF（ETS Category C），且该信号与 web-overlap 污染标签近乎正交（Jaccard = 0.206）。论文提出 cross-subject matching 策略控制假阳率，通过半合成注入验证检测力，并在 6 个 METABENCH benchmark 上复现了结果。

### Strengths

**S1.** 实验规模和控制的严谨性令人印象深刻。5,227 个模型的大规模 DIF 分析，配合 random split 对照（C% = 0.18%）、ability-matched 对照（C% = 2.9%）、LOFO 稳健性检验、graduated de-duplication、DEFF 校正等多层控制手段，系统性地排除了方法论伪迹。（Section 4.2, 4.4, Appendix C-D）

**S2.** DIF 与 web-overlap 标签正交（Enrichment = 0.964, φ = 0.012; Section 4.3）这一发现具有概念性重要意义。它表明现有 contamination 检测方法和 DIF 捕捉的是根本不同的信号维度，对 benchmark integrity 的评估方法论有实质性贡献。

**S3.** Cross-subject matching 的 ΔFPR = 0 保证（Section 3.4, Table 7）设计巧妙，是对标准 MH-DIF 的有意义适配。零假阳率在 k ≤ 5 subjects 下经验验证成立，理论论证清晰。

**S4.** 六个 benchmark 的跨域复现（Table 3, Section 4.7）显著增强了发现的可信度。知识型 benchmark（MMLU 31.3%, WinoGrande 30.3%）与程序型 benchmark（GSM8K 18.9%, HellaSwag 17.9%）的系统性差异提供了有意义的描述性洞察。

**S5.** Base-vs-instruct 分层分析（Section 5.1）揭示了机制性差异（χ² = 562.7, p < 10⁻¹²⁴），base 模型以 60.1% reference-favoring 且 ρ = -0.570，instruct 模型以 65.6% focal-favoring 且 ρ ≈ -0.079。这是论文中最有洞察力的分析之一。

---

### Weaknesses

**W-N1 [Should-Fix]** 方法论新颖性有限——核心是已有方法的领域迁移

论文的核心方法（MH-DIF + ETS 分类）是 1988 年提出的标准教育测量技术，作者在 Section 2 明确承认 "We do not modify the MH procedure; our contribution is the application context." 三个 claimed contributions 中：
- "Orthogonal constructs" 是经验发现而非方法创新；
- "Temporal DIF audit framework" 是现有技术的组合（cross-subject matching 在 DIF 文献中有先例，Nandakumar 1993; Donoghue 1993）；
- "Temporal measurement instability at scale" 是规模而非新颖性。

论文的适配工作（cross-subject matching、DEFF 校正）是工程性的而非方法论性的。对于 EMNLP 主会议，期望看到更强的方法论贡献或至少某种分析方法的显著扩展。

**建议**：更诚实地将论文定位为"大规模实证研究 + 领域适配"（empirical contribution），而非暗示方法论创新。如果 framing 为 empirical paper，目前的贡献更具说服力。

**W-N2 [Must-Fix]** 无法归因 DIF 机制严重限制实际价值

论文反复承认 DIF 只能检测 "that" 而非 "why"（Abstract, Section 5.1, Limitations），并列举三种可能机制（differential contamination, capability evolution, training methodology shifts），但未提供任何方法区分它们。Section 5.1 的混合机制分析（Appendix A, Mixed-mechanism injection）表明半合成模拟无法匹配 instruct 模型的观测模式（simulated ρ_instruct = -0.302 vs. observed -0.079），进一步暴露了归因困难。

这导致核心实用困境：如果 benchmark 维护者发现 C% = 31%，但不知道这代表污染、能力进化还是训练方法变化，该采取什么行动？Section 5.2 的 Monitor/Flag/Act 协议基于 C% 阈值给出行动建议，但在机制不明的情况下，"Act" 层面的"stable-item rankings"可能移除的恰恰是反映合法能力变化的 items。

**建议**：(1) 明确讨论在机制不明条件下 DIF 审计的决策价值——即使不能归因，"measurement properties changed" 这个事实本身是否足够重要？(2) 为 Section 5.2 的协议添加 caveats，说明在能力演化场景下 removing DIF items 可能是有害的。

**W-C1 [Should-Fix]** 结论段过于简略，未能收束论证

Section 6 Conclusion 仅有一句话（"Across six benchmarks, 17.9–31.3% of items exhibit temporal DIF (≈27–29% for MMLU; conservative bound: 13.5%); rankings are preserved (ρ ≈ 0.997), motivating routine DIF audits."）。这对一篇 8 页正文的论文来说是不可接受的。缺少：(1) 关键发现的综合讨论；(2) 研究局限性的简述；(3) 未来方向。这一段的极端简短（配合 `\vspace{-28pt}`）是空间不足的明显症状。

**建议**：至少扩展为一段（4-6 句），涵盖核心发现、实际意义和主要局限。

**W-C2 [Should-Fix]** DIF 百分比的不确定性范围过宽，核心结论模糊

论文的 headline number 是 31.3%，但经过不同校正方法后，范围从 13.5%（weighted-mean DEFF）到 53.2%（cluster bootstrap 上界）。Section 4.2 将主估计锁定为 ~27–29%，但用了约半页篇幅解释为何 13.5% 是过度校正。对读者而言，4× 的范围（13.5% 到 53.2%）使得核心结论难以评估。

Appendix D (Table 10) 提供了 5 种不确定性量化方法的比较，但正文中未充分引导读者理解该选哪个数字、为什么。这对论文的核心 claim 是关键的。

**建议**：在正文中更清晰地呈现一个"推荐估计"及其区间，而非列举多个竞争估计再逐一论证取舍。

**W-F1 [Must-Fix]** `\enlargethispage` 使用极度激进，涉嫌违反页数限制精神

`discussion.tex:3` 使用 `\enlargethispage*{10\baselineskip}`——即在 Discussion 页面增加约 10 行文本空间（≈ 1.7 英寸 / 4.3 厘米）。这远超排版微调的范畴，实质上将该页的文本区域扩展了约 20%。`experiments.tex:46` 另有 `\enlargethispage*{4\baselineskip}`。此外还有多处负 vspace（`\vspace{-28pt}`, `\vspace{-8pt}`, `\vspace{-6pt}`）系统性压缩间距。

综合效果是在名义上 8 页的限制内塞入了约 9 页的内容。如果去除这些排版手段，论文正文将显著超过 8 页。ACL/ARR 审稿实践中，过度使用 `\enlargethispage` 是已知的合规灰色地带，可能被 AC 标记。

**建议**：削减部分正文内容（Discussion 或 Method 的细节）移至附录，实现在不依赖排版技巧的情况下满足 8 页限制。

**W-F2 [Minor]** Limitations 章节放置位置

根据 PDF（page 9），Limitations 出现在参考文献之前，符合 ACL 格式要求。但 LaTeX 源码中 `\section*{Limitations}` 在 `\bibliography{references}` 之前（main.tex line 34-36），这是正确的。确认合规。

**W-W1 [Should-Fix]** 论文过于 notation-heavy，可读性受损

Section 3 的方法描述密度极高，包含多个数学公式、大量下标符号、以及详细的 edge-case 讨论（如 cross-subject matching 的零 FPR 证明、多 subject 注入的边界条件）。这些内容虽然技术上有价值，但对 NLP 社区读者而言准入门槛过高。建议将部分技术细节（如 Remark on Zero FPR, LLM-specific challenges 段落）移至附录。

**W-W2 [Minor]** 术语一致性

论文交替使用 "measurement instability" 和 "temporal DIF" 来指称同一现象，有时还使用 "temporal comparability"。虽然 Introduction 给出了定义区分，但正文中的交替使用可能造成混淆。建议统一为一个主要术语。

---

### Questions

**Q1.** 论文发现 DIF 与 contamination 正交，且无法归因 DIF 机制。那么从 benchmark 维护者的角度，DIF 审计提供了什么 contamination detection 和常规 benchmark analysis 无法提供的独特价值？"Items function differently across cohorts" 这一事实本身是否 actionable？

**Q2.** Table 1 中 Within-family (Llama-2 vs. 3) 的 C% = 61.3%，远高于 Temporal 的 31.3%。这是否说明 DIF 主要反映的是 model architecture/training 差异而非 benchmark integrity 问题？这对 DIF 作为 benchmark 质量指标的定位有何影响？

**Q3.** Cross-subject matching 的 ΔFPR = 0 保证依赖于单 subject 污染的假设（k ≤ 5）。但现实中 contamination 往往是 multi-domain 的。Table 7 显示 k = 20 时 ΔFPR = 0.069。论文声称"even worst-case multi-subject inflation (~7 pp) cannot account for the observed 31% C%"——但 7 pp 相对于 DEFF-adjusted 的 13.5% 下界就是 50% 的相对误差，这如何确保结论的稳健性？

**Q4.** 论文是否考虑过使用 logistic regression DIF 或 SIBTEST（已在 Related Work 中提及）作为方法论比较？仅使用 MH-DIF 一种方法的结论是否足够稳健？Section 4.4 简要提到了 logistic regression 检测 non-uniform DIF（17.7%），但这只是在 9/57 subjects 上的局部分析。

**Q5.** Figure 1 是一个概念示意图（schematic），不含真实数据。在论文的空间预算如此紧张的情况下，一个纯概念性的 Figure 是否值得占用 column-width 的空间？

---

### Missing References

1. **Multi-group CFA / alignment methods for measurement invariance**: DIF 是 measurement invariance 的 item-level 检验，但论文未讨论 multi-group CFA 或 alignment 方法作为结构级替代方案。相关：Millsap & Olivera-Aguilar (2012); Asparouhov & Muthén (2014) alignment method。
2. **IRT-based equating in LLM evaluation 的其他近期工作**: 除 Growing Pains 外，是否有其他 concurrent 工作在做类似的 temporal calibration？
3. **Benchmark dynamics / data drift 文献**: ML 领域的 dataset shift / concept drift 文献（如 Quinonero-Candela et al. 2009）与本文的"temporal measurement instability"概念有直接关联，但未被讨论。

---

### Overall Assessment

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 大规模的严谨实证研究，揭示了 benchmark temporal DIF 的重要现象并证明其与传统 contamination 标签正交；但方法论新颖性有限（核心为 1988 年 MH-DIF 的直接应用），且无法归因 DIF 机制严重限制了实际可操作性。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验控制严谨，多层 robustness check 令人信服；但 DEFF 校正后不确定性范围仍然过宽（13.5%–29.2%），核心结论的精确性打折扣 |
| Excitement | 3/5 | DIF-contamination 正交性是有趣发现，但核心方法是已有技术的直接迁移，缺乏方法论突破；无法归因机制限制了实用价值 |
| Reproducibility | 5/5 | 匿名代码链接已提供；方法基于标准 MH 程序；数据来自公开的 METABENCH；所有超参数和阈值均已明确报告 |
| Overall Assessment | 3.5/5 | Borderline Conference——实证贡献扎实但 novelty 不足以支撑主会议接收；如定位为 Findings-track 的大规模实证研究，接收概率更高 |

**Confidence**: 4/5 — 对 DIF 方法论和 LLM evaluation 文献均有较好了解，但对教育测量学的某些高级主题（如 MGCFA alignment）了解有限。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1220 · 2026-05-23T05:58:25.535086+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交审稿意见后进入交叉分享（Step 2）。

**Reviewer 2 关键发现摘要**：
- **评分**: 3.5 (Borderline Conference)
- **核心问题**: 方法论新颖性有限（W-N1）、无法归因 DIF 机制限制实用价值（W-N2, Must-Fix）、`\enlargethispage*{10\baselineskip}` 涉嫌违反页数限制（W-F1, Must-Fix）、结论段过于简略（W-C1）、不确定性范围过宽（W-C2）
- **认可**: 实验控制严谨（S1）、DIF-contamination 正交性有价值（S2）、cross-subject matching 设计巧妙（S3）

等待 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1221 · 2026-05-23T05:58:30.454130+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.5 (Borderline Conference)**。

主要发现：
- **优势**：规模大（5,227 模型）、控制严谨（5 层 robustness check）、DIF-contamination 正交性发现有概念性价值、6 benchmark 跨域复现可信
- **关键问题**：(1) 方法论新颖性不足——MH-DIF 是 1988 年的标准方法，论文自认 "We do not modify the MH procedure"；(2) 无法归因 DIF 机制（contamination vs. capability evolution vs. training shift），严重限制实际可操作性；(3) `\enlargethispage*{10\baselineskip}` 极度激进，实质上在 8 页内塞入了约 9 页内容；(4) 结论仅一句话，收束不足

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1222 · 2026-05-23T05:58:39.333965+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 119

## Round 119

6 recorded events


### User

_source line 1223 · 2026-05-23T06:02:51.909199+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计

---

### Summary

本文将教育测量领域的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法引入 LLM benchmark 评估，在 METABENCH 数据上（5,227 模型 × 12,508 MMLU items）检测 2023 与 2024 模型队列之间的 temporal measurement instability。核心发现是 27–29% 的 MMLU items（经非独立性校正后）表现出显著的 temporal DIF，但该不稳定性不影响模型排名（ρ ≥ 0.997）。论文引入了 cross-subject matching（ΔFPR = 0 guarantee）、DEFF clustering 校正、semi-synthetic injection 验证框架等方法贡献。总体而言，这是一篇有实质创新的跨学科论文，方法论基础扎实，但在若干关键环节的 claim scoping 和验证充分性上存在改进空间。

---

### Strengths

**S1. 真正的跨学科方法创新。** MH-DIF 在教育测量领域已有数十年积累，但将其系统性地引入 LLM benchmark 评估是新颖的。论文不是简单套用，而是针对 LLM 特有问题做了有意义的方法适配：cross-subject matching 解决了 multi-domain benchmark 中 matching variable 被污染的问题（Section 3.4），DEFF 校正处理了模型家族非独立性（Section C），这些都是 non-trivial 的方法贡献。

**S2. 规模与覆盖面令人印象深刻。** 5,227 个模型 × 12,508 items 的分析规模远超此前 IRT/DIF 在 NLP 领域的应用。跨六个 benchmark 的 replication（Table 3, Figure 6）增加了结果可信度。

**S3. 多层 convergent evidence 设计。** 论文构建了完整的证据链：semi-synthetic injection → Monte Carlo power analysis → structural controls（matched-ability、leave-one-family-out）→ cross-benchmark replication → downstream impact analysis（ranking preservation）。这种多层验证在 NLP 实证论文中并不常见。

**S4. Global exposure 与 differential functioning 的概念区分。** Section 4.3 中 DIF flags 与 web-overlap labels 的正交性结果（Jaccard = 0.206, ψ = 0.012, OR = 1.05 [0.96, 1.15]）以及 Figure 1 的概念图，清晰地建立了 DIF 检测与传统 contamination detection 的理论区别。这对领域的概念框架有贡献。

**S5. Downstream impact 分析提供了实用视角。** Section 4.6 中 ρ ≥ 0.997 的 ranking preservation 以及 Figure 6 中 DIF-ordered vs random removal 的对比，将统计发现转化为可操作的 benchmark 维护建议。

**S6. DEFF 校正的 size-stratified 分析（Appendix C）很扎实。** 对不同家族规模的 ICC 分层分析（Table 9）以及对 simple-mean vs weighted-mean 选择的论证，展示了对 survey statistics 方法论的深入理解。

---

### Weaknesses

#### 方法类

**W-M1 [Should-Fix]: Semi-synthetic 验证框架的 ecological validity 不足。**
- 具体位置：Section 3.4, Figure 2
- 问题：Binary response flipping 模型假设 contamination 以均匀概率 p 将错误回答翻转为正确回答。这是最简化的 contamination 模型。真实的 contamination 模式远更复杂：(a) memorization 可能改变 response distribution 而非确定性地修正答案；(b) contamination rate 与 item properties（difficulty、web exposure frequency）可能相关，而非均匀分布；(c) 随机选取 20% items 作为 "contaminated set" 不反映真实 contamination 的 subject-dependent 结构。论文展示了清晰的 dose-response 曲线（Figure 2, ΔTPR 从 0.40 到 0.95），但这仅验证了方法对这种特定简化模型的敏感性。Section 4.3 的 null result（DIF 与 web-overlap 正交）可以被解读为 MH-DIF 检测到的并非 contamination，而是其他形式的 temporal change（capability evolution、training methodology shifts）——这一 alternative interpretation 在论文中讨论不足。
- 建议：增加至少一种更 realistic 的 contamination model（例如 difficulty-dependent injection rate、subject-correlated contamination），或更显式地讨论 ecological validity 的局限。

**W-M2 [Should-Fix]: ΔFPR = 0 guarantee 的 scope 在 abstract 和 Section 1 中被过度表述。**
- 具体位置：Abstract ("cross-subject matching (ΔFPR = 0 guarantee)"), Section 1 第2个贡献点, Section 3.4 Remark
- 问题：ΔFPR = 0 guarantee 仅在 single-subject contamination 下成立（Section 3.4 Remark 明确说明）。但 abstract 和 introduction 均未限定此条件。Section 4.5 和 Table 7 的 multi-subject injection 实验表明，当 contamination 扩展到 k=10 个 subjects（18% of domains）时，ΔFPR 升至 0.047 ± 0.022。在现实场景中，training data contamination 极可能跨越多个 subjects，使得 ΔFPR = 0 guarantee 的实际适用范围有限。更关键的是，Table 7 显示 k=10 时 ΔFPR = 0.047 而 k=20 时 ΔFPR 降至 ~0.009，这种非单调模式表明当 contamination 足够 pervasive 时，cross-subject matching 可能将 contamination signal 归一化，导致方法在最需要的场景下失灵。
- 建议：在 abstract 和 Section 1 中明确 "under single-subject contamination" 条件；在 Section 5 中讨论 pervasive contamination 场景下的失灵风险。

**W-M3 [Should-Fix]: 验证目标（contamination detection）与应用 claim（measurement instability）之间存在张力。**
- 具体位置：Section 3.4 vs Section 4.3 vs Section 5.1
- 问题：Semi-synthetic 验证框架注入的是 contamination（response flipping），验证的是 MH-DIF 作为 contamination detector 的能力。但 real-world 应用中，Section 4.3 表明 DIF flags 与 web-overlap contamination labels 正交，Section 5.1 将 DIF 定位为检测更广义的 "measurement instability"（包括 contamination、capability evolution、training methodology shifts 三种不可区分的机制）。这意味着：方法为 X 做了验证，但 claim 检测到了 Y。如果 DIF 主要检测的是 capability evolution 而非 contamination，那么 semi-synthetic injection 验证就不能直接支持 real-world findings 的解读。
- 建议：(a) 增加非 contamination 来源的 measurement instability 验证（如 ability-distribution shift injection），或 (b) 在 Discussion 中更显式地承认这一解释性 gap。

**W-M4 [Minor]: K=5 stratification 的敏感性分析范围有限。**
- 具体位置：Table 5, Section 4.1 footnote
- 问题：K=3 vs K=5 对比（Table 5）显示结果稳健，但 K 的范围过窄。在 5,227 个 examinees 的情况下（远超教育测量的典型样本量），应该测试 K=10 或连续匹配（logistic regression DIF），以排除 coarse stratification 导致的 residual confounding。
- 建议：补充 K=10 或 continuous matching 的敏感性分析。

#### 实验类

**W-E1 [Should-Fix]: 2023 vs 2024 cohort 比较中的 temporal confound 未完全解决。**
- 具体位置：Section 3.3, Section 4.2, Section 4.7
- 问题：temporal 队列划分同时 confound 了多个变量：contamination 程度、architecture 演化（2024 instruct/chat 模型比例更高）、capability scaling、training methodology（RLHF/DPO 普及）。Base-vs-instruct decomposition（Section 4.7）部分解决了 model type confound，但 decomposition 本身将 model type 与 temporal effect 再次混淆（2024 inherently 有更多 instruct models）。Matched-ability 分析（Section 4.4, matched quintiles）控制了 ability level，但未控制 architecture/training methodology 的 confound。论文在 Section 5.1 列出三个 non-exclusive mechanisms 但无法 decompose 各自贡献。
- 建议：承认这一根本性局限；或设计 within-period 对比（例如同时期的 base vs instruct）来分离机制。

**W-E2 [Minor]: Item-Property Predictive Analysis（Appendix F）结果对 contamination 叙事构成挑战。**
- 具体位置：Appendix F, Section 5.2
- 问题：用 item properties（difficulty、discrimination、vocabulary metrics、web-overlap labels）预测 DIF susceptibility 的 logistic regression 仅达 AUC ≈ 0.60，接近随机水平。Web-overlap labels 的 SHAP 贡献 < 0.015。如果已知的 item properties 几乎无法预测哪些 items 会出现 DIF，这引发两个问题：(a) DIF 是否部分捕捉了 noise 而非 systematic signal？(b) 如果无法事前预测 DIF items，Section 5.2 推荐的 "DIF Audit Protocol" 的实用价值几何？
- 建议：在 Discussion 中显式讨论 low predictability 的含义及其对 practical monitoring 的影响。

**W-E3 [Minor]: Half-year granularity 分析（Appendix D）的解读方向值得商榷。**
- 具体位置：Appendix D
- 问题：6 个月粒度切分得到 C% = 34.1%，高于全年切分的 31.3%。论文解释为更极化的 cohort composition。但 alternative interpretation 是方法对 cohort composition artifacts 敏感——更小、更异质的组产生更多 DIF flags。这对主要发现的稳定性构成concern。
- 建议：测试多个时间切点的 C% 稳定性，而非仅展示一个半年切分。

#### 统计类

**W-S1 [Should-Fix]: Simple-mean vs weighted-mean DEFF 的分歧实质性地影响 headline result。**
- 具体位置：Appendix C, Table 2 (referenced in Section C)
- 问题：Simple-mean DEFF（n̄ = 62.8）给出 corrected C% = 29.2%；weighted-mean DEFF（n̄_w = 214.5, Kish 1965）给出 corrected C% = 13.5%。两种方法的结果相差约 2 倍。论文以 within-family similarity 不随家族规模增长（ρ_s = −0.009, p = 0.96）为由选择 simple-mean。但 Kish effective cluster size 是 survey statistics 的标准方法；论文的论证是 "weighted-mean over-corrects"，但这本身是一个需要证明的 claim，而非给定事实。13.5% 和 29.2% 对应完全不同的 narrative："约三成 items 不稳定" vs "约一成 items 不稳定"。
- 建议：(a) 在正文中同时报告两个估计及其解读差异，而非仅在 Appendix 中讨论；(b) 提供更强的 statistical evidence 支持 simple-mean 的选择（如 simulation study 比较两种校正在已知 DIF rate 下的 coverage）。

**W-S2 [Minor]: Power analysis 依赖已承认 poor fit 的 2PL 参数。**
- 具体位置：Section 4.1, Appendix A
- 问题：论文承认 MMLU response matrix 对 unidimensional 2PL model fit 差（"expected for a 57-subject multidimensional benchmark"），但 Monte Carlo power analysis 仍使用 2PL 参数。虽然 MH-DIF 本身不依赖 IRT model fit，但 power analysis 的 TPR bounds（0.68–0.80）可靠性受影响。
- 建议：说明 2PL misfit 对 power estimates 的可能影响方向。

---

### Questions

**Q1:** Cross-subject matching 中，对 within-MMLU DIF 分析，matching variable 具体是什么？是其余 56 个 subjects 的 total score 之和吗？如果是，这个 variable 被 item 数量多的 subjects（如 STEM 类）主导，是否引入隐式权重偏差？

**Q2:** Table 7 显示 multi-subject injection 的 ΔFPR 在 k=10 时为 0.047 但 k=20 时降至 ~0.009。这种非单调模式的原因是什么？如果 pervasive contamination 导致 ΔFPR 降低，这是否意味着方法在 widespread contamination 下会 fail silently？

**Q3:** Abstract 报告 "27,828 items across all six" benchmarks。但根据 Figure 6 中各 benchmark 的 N 值（818 + 1,173 + 1,267 + 1,320 + 10,042 + 12,508 = 27,128），总数为 27,128 而非 27,828。请核实。

**Q4:** Leave-one-family-out 分析（Section 4.4）仅移除 non-dominant families（≤15% of cohort）。如果移除 dominant families（Mistral、Llama-3），temporal C% 是否会发生实质变化？这些 mega-families 驱动了 DEFF correction，如果同时驱动了 DIF detection，结果的 robustness 就存疑。

**Q5:** 论文区分了 DIF detection（what）和 causal attribution（why），这是好的实践。但 Section 5.1 最后一段和 Section 4.7 的 base-vs-instruct decomposition 实际上进入了 causal territory，声称提供了 "positive evidence for mechanisms separation"。在无法 experimentally isolate mechanisms 的观测研究中，这一 claim 的证据力度如何？

**Q6:** METABENCH 数据中是否有 model quality filtering？Open LLM Leaderboard 上存在大量低质量提交（duplicate models、intentionally overfitting models）。如果未过滤，这些 noise models 是否可能人为膨胀 DIF rates？

---

### Missing References

论文的引用覆盖总体充分。一个可能有价值的补充：
- Polo et al. (2024) "TinyBenchmarks" 在 References 中已有引用但在 Related Work 讨论 IRT-based item selection 时可以更深入地对比方法差异。
- 未发现明显遗漏的关键文献。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论基础（MH-DIF）扎实，cross-subject matching 理论清晰；但 semi-synthetic validation 的 ecological validity 有限，DEFF 校正方法选择产生 2× 结果分歧，ΔFPR=0 guarantee 的适用范围被过度表述 |
| Excitement | 3.5/5 | 跨学科方法创新，将成熟的 psychometric 工具引入 LLM 评估；但 validation/application 的 interpretive gap 和 low item-property predictability（AUC ≈ 0.60）限制了实际影响力 |
| Reproducibility | 4/5 | METABENCH 数据公开，MH procedure 定义清晰，匿名代码仓库可用。DEFF 校正和 semi-synthetic framework 的实现细节充分 |
| Reviewer Confidence | 4/5 | 我熟悉 DIF 方法论、IRT 在 NLP 中的应用、以及 benchmark contamination 检测文献。仔细检查了核心方法和实验设计 |

---

### Overall Assessment

**Overall: 3.5 (Borderline Conference)**

**一句话总结：** 一篇有实质跨学科创新的论文——将 MH-DIF 引入 LLM benchmark 评估并提出了有意义的方法适配——但 semi-synthetic validation 的 ecological validity 不足、ΔFPR=0 guarantee 的适用范围过度表述、以及 DEFF 校正方法选择导致 headline result 产生 2 倍分歧，这些问题共同削弱了核心 claims 的可靠性。论文的 conceptual contribution（global exposure vs differential functioning 的区分）是重要的，但需要更强的实证支撑来匹配其 ambition。

**升/降分关键：** 若能 (a) 增加一种更 realistic 的 contamination model 验证、(b) 在 abstract/intro 中准确限定 ΔFPR=0 guarantee 的条件、(c) 在正文中更透明地讨论 DEFF 方法选择对结果的影响，可上调至 4.0。

---


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-23T06:03:55.733815+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n### Summary\n\n本文将教育测量学中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items），发现 2023 与 2024 模型群组间约 27–29% 的 MMLU 题目存在时序 DIF（ETS Category C），且该信号与 web-overlap 污染标签近乎正交（Jaccard = 0.206）。论文提出 cross-subject matching 策略控制假阳率，通过半合成注入验证检测力，并在 6 个 METABENCH benchmark 上复现了结果。\n\n### Weaknesses\n\n**W-N1 [Should-Fix]** 方法论新颖性有限——核心是已有方法的领域迁移\n\n论文的核心方法（MH-DIF + ETS 分类）是 1988 年提出的标准教育测量技术，作者在 Section 2 明确承认 \"We do not modify the MH procedure; our contribution is the application context.\" 三个 claimed contributions 中：\n- \"Orthogonal constructs\" 是经验发现而非方法创新；\n- \"Temporal DIF audit framework\" 是现有技术的组合（cross-subject matching 在 DIF 文献中有先例，Nandakumar 1993; Donoghue 1993）；\n- \"Temporal measurement instability at scale\" 是规模而非新颖性。\n\n论文的适配工作（cross-subject matching、DEFF 校正）是工程性的而非方法论性的。对于 EMNLP 主会议，期望看到更强的方法论贡献或至少某种分析方法的显著扩展。\n\n**W-N2 [Must-Fix]** 无法归因 DIF 机制严重限制实际价值\n\n论文反复承认 DIF 只能检测 \"that\" 而非 \"why\"（Abstract, Section 5.1, Limitations），并列举三种可能机制（differential contamination, capability evolution, training methodology shifts），但未提供任何方法区分它们。Section 5.1 的混合机制分析（Appendix A, Mixed-mechanism injection）表明半合成模拟无法匹配 instruct 模型的观测模式（simulated ρ_instruct = -0.302 vs. observed -0.079），进一步暴露了归因困难。\n\n这导致核心实用困境：如果 benchmark 维护者发现 C% = 31%，但不知道这代表污染、能力进化还是训练方法变化，该采取什么行动？Section 5.2 的 Monitor/Flag/Act 协议基于 C% 阈值给出行动建议，但在机制不明的情况下，\"Act\" 层面的\"stable-item rankings\"可能移除的恰恰是反映合法能力变化的 items。\n\n**W-C1 [Should-Fix]** 结论段过于简略，未能收束论证\n\nSection 6 Conclusion 仅有一句话。缺少：(1) 关键发现的综合讨论；(2) 研究局限性的简述；(3) 未来方向。这一段的极端简短（配合 `\\vspace{-28pt}`）是空间不足的明显症状。\n\n**W-C2 [Should-Fix]** DIF 百分比的不确定性范围过宽，核心结论模糊\n\n论文的 headline number 是 31.3%，但经过不同校正方法后，范围从 13.5%（weighted-mean DEFF）到 53.2%（cluster bootstrap 上界）。4× 的范围使得核心结论难以评估。\n\n**W-F1 [Must-Fix]** `\\enlargethispage` 使用极度激进，涉嫌违反页数限制精神\n\n`discussion.tex:3` 使用 `\\enlargethispage*{10\\baselineskip}`——即在 Discussion 页面增加约 10 行文本空间（≈ 1.7 英寸 / 4.3 厘米）。`experiments.tex:46` 另有 `\\enlargethispage*{4\\baselineskip}`。此外还有多处负 vspace。综合效果是在名义上 8 页的限制内塞入了约 9 页的内容。\n\n**W-W1 [Should-Fix]** 论文过于 notation-heavy，可读性受损\n\n**W-W2 [Minor]** 术语一致性 — \"measurement instability\" 和 \"temporal DIF\" 交替使用\n\n### Questions\n\n**Q1.** 从 benchmark 维护者的角度，DIF 审计提供了什么 contamination detection 和常规 benchmark analysis 无法提供的独特价值？\n\n**Q2.** Within-family (Llama-2 vs. 3) 的 C% = 61.3%，远高于 Temporal 的 31.3%。这是否说明 DIF 主要反映的是 model architecture/training 差异而非 benchmark integrity 问题？\n\n**Q3.** k=20 时 ΔFPR = 0.069 相对于 DEFF-adjusted 的 13.5% 下界就是 50% 的相对误差，如何确保结论的稳健性？\n\n**Q4.** 是否考虑过 logistic regression DIF 或 SIBTEST 作为方法论比较？\n\n**Q5.** Figure 1 概念示意图在空间紧张时是否值得？\n\n### Missing References\n1. Multi-group CFA / alignment methods（Millsap & Olivera-Aguilar 2012; Asparouhov & Muthén 2014）\n2. Dataset shift / concept drift 文献（Quinonero-Candela et al. 2009）\n\n### Overall Assessment\n**3.5 — Borderline Conference**\nSoundness 4/5, Excitement 3/5, Reproducibility 5/5\n\n---\n\n请逐条回应上述 Weaknesses 和 Questions，特别关注你作为方法/实验审稿人的视角是否支持或反对 Reviewer 2 的判断。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n### Summary\n\n本文将教育测量学中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，使用 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU items），发现 2023 与 2024 模型群组间约 27–29% 的 MMLU 题目存在时序 DIF（ETS Category C），且该信号与 web-overlap 污染标签近乎正交（Jaccard = 0.206）。论文提出 cross-subject matching 策略控制假阳率，通过半合成注入验证检测力，并在 6 个 METABENCH benchmark 上复现了结果。\n\n### Weaknesses\n\n**W-N1 [Should-Fix]** 方法论新颖性有限——核心是已有方法的领域迁移\n\n论文的核心方法（MH-DIF + ETS 分类）是 1988 年提出的标准教育测量技术，作者在 Section 2 明确承认 \"We do not modify the MH procedure; our contribution is the application context.\" 三个 claimed contributions 中：\n- \"Orthogonal constructs\" 是经验发现而非方法创新；\n- \"Temporal DIF audit framework\" 是现有技术的组合（cross-subject matching 在 DIF 文献中有先例，Nandakumar 1993; Donoghue 1993）；\n- \"Temporal measurement instability at scale\" 是规模而非新颖性。\n\n论文的适配工作（cross-subject matching、DEFF 校正）是工程性的而非方法论性的。对于 EMNLP 主会议，期望看到更强的方法论贡献或至少某种分析方法的显著扩展。\n\n**W-N2 [Must-Fix]** 无法归因 DIF 机制严重限制实际价值\n\n论文反复承认 DIF 只能检测 \"that\" 而非 \"why\"（Abstract, Section 5.1, Limitations），并列举三种可能机制（differential contamination, capability evolution, training methodology shifts），但未提供任何方法区分它们。Section 5.1 的混合机制分析（Appendix A, Mixed-mechanism injection）表明半合成模拟无法匹配 instruct 模型的观测模式（simulated ρ_instruct = -0.302 vs. observed -0.079），进一步暴露了归因困难。\n\n这导致核心实用困境：如果 benchmark 维护者发现 C% = 31%，但不知道这代表污染、能力进化还是训练方法变化，该采取什么行动？Section 5.2 的 Monitor/Flag/Act 协议基于 C% 阈值给出行动建议，但在机制不明的情况下，\"Act\" 层面的\"stable-item rankings\"可能移除的恰恰是反映合法能力变化的 items。\n\n**W-C1 [Should-Fix]** 结论段过于简略，未能收束论证\n\nSection 6 Conclusion 仅有一句话。缺少：(1) 关键发现的综合讨论；(2) 研究局限性的简述；(3) 未来方向。这一段的极端简短（配合 `\\vspace{-28pt}`）是空间不足的明显症状。\n\n**W-C2 [Should-Fix]** DIF 百分比的不确定性范围过宽，核心结论模糊\n\n论文的 headline number 是 31.3%，但经过不同校正方法后，范围从 13.5%（weighted-mean DEFF）到 53.2%（cluster bootstrap 上界）。4× 的范围使得核心结论难以评估。\n\n**W-F1 [Must-Fix]** `\\enlargethispage` 使用极度激进，涉嫌违反页数限制精神\n\n`discussion.tex:3` 使用 `\\enlargethispage*{10\\baselineskip}`——即在 Discussion 页面增加约 10 行文本空间（≈ 1.7 英寸 / 4.3 厘米）。`experiments.tex:46` 另有 `\\enlargethispage*{4\\baselineskip}`。此外还有多处负 vspace。综合效果是在名义上 8 页的限制内塞入了约 9 页的内容。\n\n**W-W1 [Should-Fix]** 论文过于 notation-heavy，可读性受损\n\n**W-W2 [Minor]** 术语一致性 — \"measurement instability\" 和 \"temporal DIF\" 交替使用\n\n### Questions\n\n**Q1.** 从 benchmark 维护者的角度，DIF 审计提供了什么 contamination detection 和常规 benchmark analysis 无法提供的独特价值？\n\n**Q2.** Within-family (Llama-2 vs. 3) 的 C% = 61.3%，远高于 Temporal 的 31.3%。这是否说明 DIF 主要反映的是 model architecture/training 差异而非 benchmark integrity 问题？\n\n**Q3.** k=20 时 ΔFPR = 0.069 相对于 DEFF-adjusted 的 13.5% 下界就是 50% 的相对误差，如何确保结论的稳健性？\n\n**Q4.** 是否考虑过 logistic regression DIF 或 SIBTEST 作为方法论比较？\n\n**Q5.** Figure 1 概念示意图在空间紧张时是否值得？\n\n### Missing References\n1. Multi-group CFA / alignment methods（Millsap & Olivera-Aguilar 2012; Asparouhov & Muthén 2014）\n2. Dataset shift / concept drift 文献（Quinonero-Candela et al. 2009）\n\n### Overall Assessment\n**3.5 — Borderline Conference**\nSoundness 4/5, Excitement 3/5, Reproducibility 5/5\n\n---\n\n请逐条回应上述 Weaknesses 和 Questions，特别关注你作为方法/实验审稿人的视角是否支持或反对 Reviewer 2 的判断。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-23T06:04:26.624857+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30891
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-23T06:04:27.178190+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n### Weaknesses\n\n**W-M1 [Should-Fix]: Semi-synthetic 验证框架的 ecological validity 不足。**\nBinary response flipping 模型假设 contamination 以均匀概率 p 将错误回答翻转为正确回答。真实 contamination 模式远更复杂：(a) memorization 可能改变 response distribution 而非确定性地修正答案；(b) contamination rate 与 item properties 可能相关；(c) 随机选取 20% items 不反映真实的 subject-dependent 结构。方法为 X（contamination）做了验证，但 claim 检测到了 Y（measurement instability）。\n\n**W-M2 [Should-Fix]: ΔFPR = 0 guarantee 的 scope 在 abstract 和 Section 1 中被过度表述。**\nΔFPR = 0 仅在 single-subject contamination 下成立，但 abstract 和 introduction 均未限定此条件。k=10 时 ΔFPR = 0.047 ± 0.022。更关键的是 Table 7 显示 k=10 时 ΔFPR = 0.047 而 k=20 时 ΔFPR ~0.009（原文 0.069），这种非单调模式暗示 pervasive contamination 下方法可能 fail silently。\n\n**W-M3 [Should-Fix]: 验证目标（contamination detection）与应用 claim（measurement instability）之间存在张力。**\nSemi-synthetic 验证注入的是 contamination，验证的是 contamination detection 能力。但 real-world application 中 DIF 被定位为检测更广义的 measurement instability。方法为 X 做了验证但 claim 检测到了 Y。\n\n**W-M4 [Minor]: K=5 stratification 的敏感性分析范围有限。**\n在 5,227 examinees 下应测试 K=10 或连续匹配。\n\n**W-E1 [Should-Fix]: 2023 vs 2024 cohort 比较中的 temporal confound 未完全解决。**\ntemporal 队列划分同时 confound 了 contamination 程度、architecture 演化、capability scaling、training methodology。Base-vs-instruct decomposition 部分解决但将 model type 与 temporal effect 再次混淆。\n\n**W-E2 [Minor]: Item-Property Predictive Analysis（AUC ≈ 0.60）对 contamination 叙事构成挑战。**\n已知 item properties 几乎无法预测 DIF susceptibility，DIF 是否部分捕捉了 noise？\n\n**W-E3 [Minor]: Half-year granularity（C% = 34.1%）的解读 — 方法对 cohort composition artifacts 敏感？**\n\n**W-S1 [Should-Fix]: Simple-mean vs weighted-mean DEFF 的分歧实质性地影响 headline result（29.2% vs 13.5%）。**\n两种方法结果相差约 2 倍。论文选择 simple-mean 但 Kish effective cluster size 是 survey statistics 标准方法。\n\n**W-S2 [Minor]: Power analysis 依赖已承认 poor fit 的 2PL 参数。**\n\n### Questions\n\n**Q1:** Cross-subject matching variable 是否被 item 数量多的 subjects 主导？\n\n**Q2:** Table 7 中 multi-subject injection 的 ΔFPR 在 k=10 (0.047) 和 k=20 (0.069) 之间的非单调模式原因？\n\n**Q3:** Abstract 报告 \"27,828 items\" vs 实际计算 27,128。数据不一致？\n\n**Q4:** 移除 dominant families（Mistral、Llama-3）后 temporal C% 是否实质变化？\n\n**Q5:** Base-vs-instruct decomposition 在观测研究中的 causal claim 证据力度？\n\n**Q6:** METABENCH 数据中是否有 model quality filtering？\n\n### Missing References\n- TinyBenchmarks 讨论可更深入\n\n### Overall Assessment\n**3.5 — Borderline Conference**\nSoundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5\n\n---\n\n请逐条回应上述 Weaknesses 和 Questions，特别关注你作为新颖性/完整性审稿人的视角是否支持或反对 Reviewer 1 的判断。",
  "project": "irt_equated_bench_regen",
  "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n### Weaknesses\n\n**W-M1 [Should-Fix]: Semi-synthetic 验证框架的 ecological validity 不足。**\nBinary response flipping 模型假设 contamination 以均匀概率 p 将错误回答翻转为正确回答。真实 contamination 模式远更复杂：(a) memorization 可能改变 response distribution 而非确定性地修正答案；(b) contamination rate 与 item properties 可能相关；(c) 随机选取 20% items 不反映真实的 subject-dependent 结构。方法为 X（contamination）做了验证，但 claim 检测到了 Y（measurement instability）。\n\n**W-M2 [Should-Fix]: ΔFPR = 0 guarantee 的 scope 在 abstract 和 Section 1 中被过度表述。**\nΔFPR = 0 仅在 single-subject contamination 下成立，但 abstract 和 introduction 均未限定此条件。k=10 时 ΔFPR = 0.047 ± 0.022。更关键的是 Table 7 显示 k=10 时 ΔFPR = 0.047 而 k=20 时 ΔFPR ~0.009（原文 0.069），这种非单调模式暗示 pervasive contamination 下方法可能 fail silently。\n\n**W-M3 [Should-Fix]: 验证目标（contamination detection）与应用 claim（measurement instability）之间存在张力。**\nSemi-synthetic 验证注入的是 contamination，验证的是 contamination detection 能力。但 real-world application 中 DIF 被定位为检测更广义的 measurement instability。方法为 X 做了验证但 claim 检测到了 Y。\n\n**W-M4 [Minor]: K=5 stratification 的敏感性分析范围有限。**\n在 5,227 examinees 下应测试 K=10 或连续匹配。\n\n**W-E1 [Should-Fix]: 2023 vs 2024 cohort 比较中的 temporal confound 未完全解决。**\ntemporal 队列划分同时 confound 了 contamination 程度、architecture 演化、capability scaling、training methodology。Base-vs-instruct decomposition 部分解决但将 model type 与 temporal effect 再次混淆。\n\n**W-E2 [Minor]: Item-Property Predictive Analysis（AUC ≈ 0.60）对 contamination 叙事构成挑战。**\n已知 item properties 几乎无法预测 DIF susceptibility，DIF 是否部分捕捉了 noise？\n\n**W-E3 [Minor]: Half-year granularity（C% = 34.1%）的解读 — 方法对 cohort composition artifacts 敏感？**\n\n**W-S1 [Should-Fix]: Simple-mean vs weighted-mean DEFF 的分歧实质性地影响 headline result（29.2% vs 13.5%）。**\n两种方法结果相差约 2 倍。论文选择 simple-mean 但 Kish effective cluster size 是 survey statistics 标准方法。\n\n**W-S2 [Minor]: Power analysis 依赖已承认 poor fit 的 2PL 参数。**\n\n### Questions\n\n**Q1:** Cross-subject matching variable 是否被 item 数量多的 subjects 主导？\n\n**Q2:** Table 7 中 multi-subject injection 的 ΔFPR 在 k=10 (0.047) 和 k=20 (0.069) 之间的非单调模式原因？\n\n**Q3:** Abstract 报告 \"27,828 items\" vs 实际计算 27,128。数据不一致？\n\n**Q4:** 移除 dominant families（Mistral、Llama-3）后 temporal C% 是否实质变化？\n\n**Q5:** Base-vs-instruct decomposition 在观测研究中的 causal claim 证据力度？\n\n**Q6:** METABENCH 数据中是否有 model quality filtering？\n\n### Missing References\n- TinyBenchmarks 讨论可更深入\n\n### Overall Assessment\n**3.5 — Borderline Conference**\nSoundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5\n\n---\n\n请逐条回应上述 Weaknesses 和 Questions，特别关注你作为新颖性/完整性审稿人的视角是否支持或反对 Reviewer 1 的判断。",
    "project": "irt_equated_bench_regen",
    "chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "director_session_key": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
  }
}
```

</details>

---


### Tool result

_source line 1227 · 2026-05-23T06:04:28.693026+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1514
}
```

</details>

---


### Assistant

_source line 1228 · 2026-05-23T06:04:31.194290+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1229 · 2026-05-23T06:04:33.839660+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

评审结论：**Overall 3.5 (Borderline Conference)**。

核心判断：跨学科方法创新有实质价值（MH-DIF + cross-subject matching + DEFF correction），但三个 Should-Fix 级别问题需要解决：
1. Semi-synthetic validation 的 ecological validity 不足（binary response flipping 过于简化）
2. ΔFPR=0 guarantee 在 abstract 中未限定为 single-subject contamination
3. Simple-mean vs weighted-mean DEFF 产生 29.2% vs 13.5% 的 2× 分歧，方法选择对 headline result 影响过大

若能修订 claim scoping 并补充更 realistic 的 validation，可上调至 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1230 · 2026-05-23T06:05:01.148391+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 121

## Round 121

2 recorded events


### User

_source line 1231 · 2026-05-23T06:06:27.854757+00:00_

[Reviewer 1 审稿结果]:
逐条回应 Reviewer 2 的审稿意见。

---

**[REBUT] W-N1: 方法论新颖性有限**

R2 的论述有两处不准确。第一，R2 引用 Nandakumar (1993) 和 Donoghue (1993) 作为 cross-subject matching 的先例，但这些工作讨论的是 **purified subtest matching**（在同一测试内剔除 studied items 后用剩余 items 匹配），而非论文提出的 **cross-benchmark matching**（用完全不同 benchmark 的 total score 作为 matching variable）。后者在 LLM multi-domain evaluation 的语境下是新的适配，因为它解决了 LLM benchmarks 中跨 subject contamination 同时发生的问题——这在教育测量中不存在类似的大规模情境。第二，DEFF 校正（Appendix C）针对 model family 结构的 size-stratified ICC 分析不是 "工程性" 工作；它需要建立 LLM model families 的 clustering 特性（Table 9 的 ICC 随 family size 递减），这是领域特有的实证发现。

但 R2 的核心判断——论文的贡献以应用和实证为主而非方法论突破——我认为是正确的。对于 EMNLP，应用性贡献是完全可以接收的，问题在于应用的 insights 是否足够 compelling。这取决于 W-N2 中机制归因问题的严重程度。

---

**[REBUT] W-N2: 无法归因 DIF 机制（R2 标注 Must-Fix，我认为 Should-Fix）**

R2 将此标为 Must-Fix，理由是不知道机制就无法采取行动。我认为这过度要求了。

教育测量中 DIF 的标准用途恰好是 **diagnostic without attribution**：ETS 的实际操作流程（Zieky, 2006）是先检测 DIF items、再由 subject-matter experts 判断 mechanism 和 action——而非要求统计方法本身提供因果解释。论文在 Section 5.2 提出的 Monitor/Flag/Act protocol 正是遵循了这一范式。R2 担忧 "stable-item rankings 可能移除反映合法能力变化的 items"，但论文已在 Section 4.6 中明确说明：ρ ≥ 0.997 表明移除 C items 几乎不改变排名（Figure 6），因此 practical harm 极低。

Section 5.1 的混合机制分析（simulated ρ_instruct = −0.302 vs. observed −0.079）确实显示 semi-synthetic framework 无法完全复现 real-world 模式，但这恰恰是论文诚实报告局限性的体现，而非应被惩罚的缺陷。

我在自己的 W-M3 中也指出了 validation/application 之间的张力，但归因困难本身不应是 Must-Fix——这是所有观测性 DIF 研究的固有局限。Should-Fix：要求论文在 Discussion 中更清晰地界定 DIF 审计的决策边界即可。

---

**[AGREE] W-C1: Conclusion 过于简略**

同意。Section 6 Conclusion 极度简短（实际上就是一句话加上 `\vspace{-28pt}`），在空间约束下可以理解，但作为独立的审稿意见，确实缺少对核心发现的综合收束。不过严重程度为 Minor 而非 Should-Fix，因为 Section 5 Discussion 已承担了大部分 conclusion 功能。

---

**[REBUT] W-C2: DIF 百分比不确定性范围过宽（4×）**

R2 将范围表述为 "13.5% 到 53.2%（4× range）"，这一 framing 有误导性。53.2% 是 cluster bootstrap CI 的 **上界**，不是 point estimate；13.5% 是 weighted-mean DEFF 的保守下界。论文的两个 convergent point estimates 是 simple-mean DEFF（29.2%）和 cluster bootstrap lower bound（26.7%），两者的一致性很高（Section C, Appendix）。

更准确的不确定性范围应是：point estimate 27–29%，conservative lower bound 13.5%。这是 ~2× 范围而非 4×。我在自己的 W-S1 中也指出了 simple-mean vs weighted-mean 的 2× 分歧，但论文在 Section H 中提供了 evidence（ρ_s = −0.009, p = 0.96：within-family similarity 不随 family size 增长）支持 simple-mean 的选择。R2 将上界和下界混合呈现为 "范围" 是不恰当的。

---

**[AGREE] W-F1: \enlargethispage 使用激进**

同意这是一个值得关注的格式问题。`\enlargethispage*{10\baselineskip}` 在 Discussion 页面增加约 10 行空间（~4.3cm），效果相当显著。结合 experiments.tex 中的 `\enlargethispage*{4\baselineskip}` 和多处负 vspace，实际内容密度确实超出了标准 8 页格式允许的范围。

但我不会标为 Must-Fix，而是 Should-Fix。原因：(a) `\enlargethispage` 是 LaTeX 的合法命令，许多被接收的 ACL 论文使用了类似技巧；(b) 最终判定权在 AC 和 program chairs，reviewer 可以 flag 但不应以此作为 reject 理由；(c) 如果 Discussion 缩减导致论文无法回应 R2 自己的 W-N2（机制讨论不足），那就陷入矛盾。建议作者压缩部分内容至 Appendix，但不应作为 acceptance-blocking issue。

---

**[REBUT] W-W1: 论文过于 notation-heavy**

不同意。论文涉及 MH 统计量（公式 1-2）、ETS C 分类阈值、DEFF 校正、cross-subject matching 的形式化——这些都需要 precise notation 来避免歧义。对于一篇方法论导向的论文，Section 3 的 notation density 在 ACL/EMNLP 的 measurement/evaluation track 中是正常水平。如果减少 notation，反而可能损害 reproducibility（R2 自己给了 Reproducibility 5/5）。

---

**[AGREE] W-W2: 术语一致性**

同意，Minor 级别。"Temporal DIF" 是具体的统计发现，"measurement instability" 是更广义的概念。两者并非不一致，但论文应在首次引入时明确定义二者关系（例如 "we use temporal measurement instability to refer to the phenomenon, and temporal DIF as its statistical operationalization"）。

---

### Questions 回应

**[REBUT] Q1: DIF 审计的独特价值**

R2 的问题隐含假设——如果 DIF 与 contamination detection 提供类似信息就没有价值。但 Section 4.3 恰恰表明两者 **正交**（Jaccard = 0.206, OR = 1.05）。DIF 提供的独特价值是：识别 measurement properties 跨时间变化的 items，不论原因是否为 contamination。这在 benchmark 维护中的直接应用是：当 C% 升高时，benchmark 维护者知道需要审查哪些 items，即使不知道 root cause。常规 benchmark analysis（accuracy tracking）无法定位到 item level；contamination detection 只覆盖 web-exposed items。

---

**[AGREE] Q2: Within-family C% = 61.3% 的含义**

这是一个很好的观察。Within-family DIF（Llama-2 vs Llama-3）的 C% = 61.3% 远高于 temporal DIF 的 31.3%，强烈暗示 DIF 主要捕捉的是 model architecture/training paradigm 差异，而非 benchmark 本身的 integrity 问题。这与我的 W-M3（validation/application 张力）和 W-E1（temporal confound）一致：如果 family-level capability shifts 产生更强的 DIF signal，那么 temporal DIF 中的相当比例可能同样反映 capability evolution 而非 contamination。论文应更显式地讨论这一发现对 contamination 叙事的影响。

---

**[REBUT] Q3: k=20 ΔFPR 与 DEFF 下界的比值**

R2 引用 k=20 时 ΔFPR = 0.069，但据我对 Table 7 和正文（Section 4.5）的阅读，k=20 的 ΔFPR 约为 0.009 ± 0.018，而非 0.069。ΔFPR = 0.047 ± 0.022 是 k=10 的数值。如果 R2 的数字来源有误，那么 "50% 相对误差" 的计算也不成立。即使取 k=10 的 0.047，相对于 simple-mean DEFF adjusted C% 29.2%，相对误差约 16%，这是更合理的 concern 范围。建议 R2 核实数字来源。

---

**[AGREE] Q4: 方法论比较（logistic regression DIF / SIBTEST）**

同意。我在自己的 Q1 中也提出了 continuous matching（logistic regression DIF）的建议。在 5,227 个 examinees 的规模下，logistic regression DIF 可以避免 K-stratification 的信息损失，SIBTEST 可以检测 non-uniform DIF。至少应作为 sensitivity check 呈现。

---

**[REBUT] Q5: Figure 1 的空间价值**

不同意。Figure 1 以视觉方式清晰建立了 global contamination vs differential contamination 的概念区分，这是论文的核心 conceptual contribution（也是 S4 的基础）。对于跨学科读者（NLP 研究者不熟悉 DIF 概念），这张概念图的教学价值大于它占用的空间。在空间压力下，压缩 Section 3.1/3.2 的文字描述比移除 Figure 1 更合理。

---

### Missing References 回应

**[AGREE]** Multi-group CFA / measurement invariance alignment methods（Millsap & Olivera-Aguilar 2012; Asparouhov & Muthén 2014）确实是相关文献，论文在 Related Work 讨论 measurement invariance 时（Section 2，MIMIC models 段落）可以补充引用。

**[REBUT]** Dataset shift / concept drift（Quinonero-Candela et al. 2009）与 DIF 的关联较弱。DIF 是 item-level analysis，dataset shift 是 distribution-level analysis。两者在不同粒度上操作，引用关联性有限。

---

### 总结

R2 的 6 条 Weaknesses 中，我同意 3 条（W-C1 同意但降级为 Minor、W-F1 同意但降级为 Should-Fix、W-W2 同意 Minor），反驳 3 条（W-N1 部分反驳、W-N2 反驳 Must-Fix 定级但同意 Should-Fix、W-C2 反驳 4× framing）。R2 的 Questions 中 Q2 是最有洞察力的——within-family C% = 61.3% 对论文的 contamination narrative 构成真正挑战。

R2 给出 3.5 (Borderline Conference)，与我的评分一致。我认为 R2 的 Excitement 3/5 偏低——跨学科方法引入本身有价值，即使核心方法是已有技术。Soundness 4/5 偏高——考虑到 DEFF 分歧和 ecological validity 问题，3.5 更合适。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1232 · 2026-05-23T06:06:35.440073+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 122

## Round 122

10 recorded events


### User

_source line 1233 · 2026-05-23T06:07:13.156449+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — 交叉回应 Reviewer 1 意见

---

### Weaknesses 逐条回应

**[AGREE] R1-W-M1: Semi-synthetic 验证的 ecological validity 不足**

同意这是一个实质性问题。Binary response flipping 确实是最简化的 contamination 模型，论文在 Section 3.4 和 Limitations 中也明确承认 "reported ΔTPR values are upper-bound estimates"。但我补充两点：

(1) 论文在 Appendix A (Mixed-mechanism injection) 已尝试了更复杂的注入方案（difficulty-dependent + uniform 混合），结果表明即使这样也无法匹配 instruct 模型的观测模式（simulated ρ_instruct = -0.302 vs. observed -0.079），这实际上**加强**了 R1 的论点——验证框架与现实之间有显著差距。

(2) 不过，R1 的表述 "方法为 X 做了验证但 claim 检测到了 Y" 需要更精确。论文的 semi-synthetic 验证证明的是 MH-DIF 对 differential item behavior 的检测力，而非仅对 contamination 的检测力。Response flipping 恰恰制造的是 differential functioning（一个 group 的 ICC 移位），而非特指 contamination。所以验证目标和应用 claim 之间的张力比 R1 表述的要小一些，但仍然存在。

**[REBUT] R1-W-M2: ΔFPR = 0 guarantee 的 scope 过度表述 + 非单调模式**

部分同意 scope 限定在 abstract/intro 中不够明确，但 R1 的关键技术论据有误：

(1) **"非单调模式"不存在。** Table 7 (Appendix B) 清楚显示 ΔFPR 是**单调递增**的：k=1 → 0.000, k=3 → 0.003, k=5 → 0.007, k=10 → 0.047, k=20 → 0.069。R1 声称 "k=20 时 ΔFPR ~0.009（原文 0.069）"，这是对 Table 7 的误读。0.069 是 k=20 的正确值，不存在 R1 声称的非单调行为。

(2) **Scope 限定**：Introduction 中确实说了 "comprising cross-subject matching (ΔFPR = 0 guarantee)"（Section 1, Contribution 2），但 Section 3.4 的 Remark 明确限定了 "Under single-subject injection"。Abstract 中并未使用 "ΔFPR = 0" 这一表述。同意 intro 中可以更明确地加限定条件，但这是措辞改进而非事实性错误。

**[AGREE] R1-W-M3: 验证目标与应用 claim 的张力**

同意，且这与我的 W-N2 高度一致。论文的核心困境是：semi-synthetic injection 只验证了一种特定机制（contamination-like response flipping）下的检测力，但 real-world 应用中 DIF 可能反映多种机制（contamination、capability evolution、training methodology）。Section 5.1 的分析进一步表明这些机制可能同时存在且不可分离。

但我补充一个 nuance：即使验证框架只模拟了 contamination，它证明的核心命题是 "MH-DIF 能检测到 differential item behavior when present"——这对所有三种机制都适用。问题在于论文没有充分论证 "detecting differential item behavior regardless of cause" 本身的价值。

**[REBUT] R1-W-M4: K=5 stratification 敏感性分析范围有限**

论文实际上**已经做了**超越 K=5 的分析：

- Section 4.2 明确报告了 K=3（C% = 39.4%, 因 under-stratification 膨胀）和 K=10（非单调 peak）的结果
- Appendix A, Table 5 提供了 K=3 vs K=5 的检测力对比（TPR 差异 < 0.02）
- Section 4.2 讨论了 K=10 peak 的原因（ability-DIF interactions in finer strata）

R1 建议的 "连续匹配" 实质上是 IRT θ-conditioning，论文在 Section 4.4 和 Table 2 已经做了（C% = 0.312, r(θ, total) = 0.9986）。所以 R1 这一条的前提——缺乏敏感性分析——与论文内容不符。

**[AGREE] R1-W-E1: Temporal confound 未完全解决**

同意，这是论文最根本的局限之一，与我的 W-N2 一致。2023 vs. 2024 的划分不可避免地 confound 了多个因素。论文的 base-vs-instruct 分解（Section 5.1）提供了部分机制分离的证据，但正如 R1 指出的，model type 本身与时间高度相关，无法真正 deconfound。

不过我要指出论文做了几项有意义的控制来约束这一问题：ability-matched 对照将 C% 从 31.3% 仅降至 28.9%（~2.4 pp, Section 4.2），domain-level accuracy gains 解释 <0.1% 的 DIF variance，random split 基线 0.18%。这些控制虽然不能消除 confound，但大幅缩小了替代解释的空间。

**[AGREE] R1-W-E2: AUC ≈ 0.60 对 contamination 叙事的挑战**

部分同意。但我认为 R1 的推论方向有误——AUC ≈ 0.60 不是说 DIF 可能捕捉 noise，而是说 DIF susceptibility 不是固定的 item 属性。Appendix G 的分析使用了 17 个 leak-free features，近乎 chance-level 的预测力说明 DIF 是 cohort-item 交互的 emergent property，而非 item 的内在缺陷。这实际上**支持**了论文 "temporal measurement instability" 的 framing（不是 item 有问题，而是 measurement 在变化）。

不过这确实对 Section 5.2 的 "pre-screening is infeasible" 结论提出了实际挑战：如果无法预测哪些 items 会 exhibit DIF，那么只能做 post-hoc monitoring，实用价值确实受限。

**[AGREE] R1-W-E3: Half-year granularity 的 cohort composition 敏感性**

同意。Appendix D 报告 C% = 34.4%（半年划分 vs. 31.3% 全年划分），论文解释为 "more polarized cohort composition"。这说明 C% 对 cohort 定义敏感，即 C% 部分反映的是 cohort composition 而非纯粹的 item instability。这是 Section 5.2 audit protocol 中应当 caveat 的。

**[AGREE] R1-W-S1: Simple-mean vs weighted-mean DEFF 的分歧**

同意这是一个实质性统计分歧，且与我的 W-C2 直接相关。论文偏好 simple-mean（C% = 29.2%）的论据——within-family similarity 对 family size 无依赖性（ρ_s = -0.009, Appendix H）以及 size-stratified DEFF 显示 ICC 随 family size 递减（Table 9: 0.246 → 0.082）——是合理的，但并非决定性的。

R1 指出 Kish weighted mean 是 survey statistics 的标准方法是正确的。论文的反论证本质上是说 LLM model families 不满足 Kish 方法的 homogeneity 假设。这是一个合法的 domain-specific argument，但需要更强的支撑（比如 formal testing of the homogeneity assumption），而非仅靠描述性统计（ρ_s 和 ICC 趋势）。

核心问题：13.5% vs 29.2% 的差异是 2× factor，对论文的 headline claim 有实质影响。论文应更坦诚地承认这一不确定性，而非在正文中强调 27-29% 并将 13.5% 边缘化为 "conservative extreme"。

**[AGREE] R1-W-S2: Power analysis 依赖 poor-fit 2PL**

同意但认为 minor。论文在 Appendix A 明确承认 2PL fit is poor for MMLU's multidimensional structure，并通过 semi-synthetic injection 的经验验证进行了三角验证（ΔTPR = +0.508 vs. parametric estimate TPR = 0.68-0.80）。这种三角验证足以支撑结论。

---

### Questions 逐条回应

**[AGREE] R1-Q1: Cross-subject matching variable 是否被大 subject 主导？**

有效的技术问题。MMLU 57 subjects 的 item 数量差异很大，cross-subject total score 自然会被 item 多的 subjects 主导。但这对 DIF 结果的影响方向不明确——如果大 subjects 的 items 较稳定（或不稳定），会系统性地偏移 matching variable。论文未讨论此问题。

**[REBUT] R1-Q2: ΔFPR 的 "非单调模式"**

如上述 W-M2 的回应，Table 7 中 ΔFPR 从 k=1 到 k=20 是**严格单调递增**的（0.000 → 0.003 → 0.007 → 0.047 → 0.069）。R1 声称的非单调模式是对数据的误读。

**[REBUT] R1-Q3: Abstract 中 "27,828 items" 数据不一致**

经核查 LaTeX 源码（sections/abstract.tex），abstract 中的数字是 **27,125**，与 Table 3 的六个 benchmark item 总数一致（12,508 + 1,267 + 817 + 1,172 + 1,319 + 10,042 = 27,125）。R1 可能误读了 PDF 中的数字。不存在数据不一致问题。

**[AGREE] R1-Q4: 移除 dominant families 后 C% 变化**

Table 8 (Appendix B) 明确回答了这个问题：移除 Mistral → C% = 22.47%（下降 8.85 pp），移除 Llama-3 → C% = 24.06%（下降 7.26 pp）。论文通过 Monte Carlo random-subsample calibration 区分了 composition effect 和 power effect（Mistral: -8.44 pp composition vs. -0.41 pp power），论证了变化主要来自 cohort composition 而非统计伪迹。

但我认为这个结果实际上**削弱**了论文的核心 claim：如果移除两个最大 family 就能将 C% 从 31.3% 降至 ~22-24%，说明 headline number 对少数大 family 的依赖很强。论文应在正文中更突出地讨论这一点。

**[AGREE] R1-Q5: Base-vs-instruct 的 causal claim**

同意观测研究中 causal interpretation 受限。Section 5.1 的分析（χ² = 562.7, OR = 4.24）展示的是 strong association，不是因果关系。论文使用的语言（"argues against", "further confirm"）在大多数地方是恰当的，但某些表述（如 "revealing mechanistically distinct patterns"）可能过强。

**[AGREE] R1-Q6: METABENCH 数据的 model quality filtering**

论文未讨论 METABENCH 中是否有 model quality filtering（如是否排除了 random/broken models、是否有最低 accuracy 阈值）。这对 DIF 结果可能有影响：如果包含了大量低质量模型，within-cohort variance 可能被人为膨胀。

---

### 与我的审查意见的交叉对照

R1 和我的审稿有三个高度一致的核心关切：

1. **机制归因不足**（R1-W-M3/W-E1 ≈ 我的 W-N2）：这是论文最根本的问题，且两位 reviewer 独立指出。
2. **不确定性范围过宽**（R1-W-S1 ≈ 我的 W-C2）：13.5% vs 29.2% 的 DEFF 分歧需要更透明的处理。
3. **新颖性定位**：R1 虽然没有明确提出 novelty 问题，但 W-M1/W-M3 的 "验证了 X 但 claim 了 Y" 本质上也在质疑 contribution 的实质性。

R1 的意见中我**不同意**的两点：
- W-M2 的 "非单调 ΔFPR" 论据基于误读 Table 7
- Q3 的数据不一致基于误读 abstract 数字

**总体而言**，R1 的方法论审查补充了我在新颖性和完整性方面的关切。两份审稿共同指向的核心问题是：一篇应用现有方法的大规模实证论文，其 contribution 是否足够支撑主会议接收。我维持 **3.5 (Borderline Conference)** 的评分。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-23T06:07:40.127194+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-23T06:07:40.529487+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T05:52:33.084769+00:00\", \"completed_at\": \"2026-05-23T05:55:24.843237+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，纯文本（Title + Abstract + Introduction）。Figure 1 出现在 page 2 顶部，在前 3 页内，可接受。首页整体干净专业，ACL 模板格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（ICC 概念图）作为第一个 display item 出现在 page 2 顶部，传达 global vs differential contamination 的核心区分，caption 自包含。但图幅偏小（单栏宽），ICC 曲线内的文字标注（\\\"Global Contamination\\\"/\\\"Differential Contamination\\\"）字号偏小，建议确认打印时可读性。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 5-6\", \"message\": \"连续 2 页纯文本，无任何 display item（figure/table/equation）。Page 5 为 Method 的 cohort designs + semi-synthetic framework，page 6 为 Experiments 的 validation 和 temporal comparability 结果段。大量数字密集叙述无视觉锚点，审稿人可能在此段失去耐心。建议将 page 6 的关键结果（如 31% temporal C% 或 power analysis 数据）提取为小型 summary table 或 key-number callout box。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"单页堆叠 3 个 display items（Table 1 + Figure 2 + Table 2），视觉过载。与 pages 5-6 的纯文本段形成强烈反差，布局节奏不均匀。建议将 Table 2 或 Figure 2 前移至 page 5-6 区域以平衡密度。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 和 Table 2 均使用 booktabs 风格（toprule/midrule/bottomrule），无竖线，格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2（dose-response 曲线）清晰可读，蓝橙双色方案色盲友好，axis labels 字号合适，caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 格式规范，booktabs 风格。表中 ρ^s（Spearman 相关）和 Rank（排名相关）等指标精度统一。但未见最优值加粗标注——此表为跨 benchmark 描述性比较，可不强制加粗。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"主文结束于 page 9 上方约 1/3 处，References 从 page 9 中部开始。Limitations 段落简短（约 3 个点），符合 EMNLP 规范。\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"References 格式统一，未发现 [?] 未解析引用或编号跳号。排版正常，无溢出或截断。\"}, {\"severity\": \"
…[truncated 1685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-23T06:07:40.530000+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-23T06:07:40.580497+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-23T06:09:37.585645+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "issues:\n  # === Round 13 新发现 ===\n\n  - id: \"R13-W1\"\n    summary: \"机制归因不足：DIF 检测 'that' 但无法区分 contamination / capability evolution / training shift\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M3/W-E1 + R2-W-N2 共识。R2标Must-Fix，R1降为Should-Fix（educational measurement中diagnostic-without-attribution是标准实践）。最终共识Should-Fix。论文需在Discussion中更清晰界定DIF审计在机制不明条件下的决策价值，并为Section 5.2 audit protocol添加caveats。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W2\"\n    summary: \"DEFF校正方法选择导致headline result 2×分歧（simple-mean 29.2% vs weighted-mean 13.5%），核心结论不确定性未充分透明呈现\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-S1 + R2-W-C2 共识。论文偏好simple-mean有合理论据（ρ_s=-0.009, size-stratified ICC递减），但weighted-mean是survey statistics标准方法。正文应更透明地同时报告两个估计。R2的4×范围(13.5%-53.2%)被R1纠正为2×范围(point estimates 27-29%, lower bound 13.5%)。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W3\"\n    summary: \"Semi-synthetic验证框架ecological validity不足：binary response flipping过于简化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M1, R2同意。验证了MH-DIF对differential item behavior的检测力，但injection model过于简化。Appendix A的mixed-mechanism injection也无法匹配instruct模型观测模式(simulated ρ_instruct=-0.302 vs observed -0.079)。建议增加更realistic的contamination model或更显式讨论ecological validity局限。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W4\"\n    summary: \"\\\\enlargethispage使用激进：Discussion页+10baselineskip，实质上在8页内塞入约9页内容\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-F1标Must-Fix，R1降为Should-Fix。discussion.tex \\\\enlargethispage*{10\\\\baselineskip}(+4.3cm) + experiments.tex \\\\enlargethispage*{4\\\\baselineskip} + 多处负vspace。R1指出\\\\enlargethispage是合法LaTeX命令且许多ACL论文使用，不应作为reject理由，但建议压缩内容至appendix。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"ΔFPR=0 guarantee在Introduction中未限定为single-subject contamination条件\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M2提出，R2部分同意（同意intro需限定条件，但纠正R1的非单调性论据——Table 7 ΔFPR是单调递增的）。Section 3.4 Remark已限定但intro Contribution 2未限定。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W6\"\n    summary: \"方法论新颖性有限：核心MH-DIF是1988年标准方法的领域迁移\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-N1。R1部分反驳（cross-subject matching和size-stratified DEFF是non-trivial适配），但同意核心贡献以应用和实证为主。两位reviewer均认为对EMNLP应定位为empirical contribution。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W7\"\n    summary: \"Conclusion仅一句话，未能收束论证\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-C1标Should-Fix，R1同意但降为Minor（Section 5 Discussion已承担大部分conclusion功能）。配合\\\\vspace{-28pt}是空间不足症状。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W8\"\n    summary: \"Temporal confound未完全解决：2023 vs 2024划分同时confound了architecture/training methodology/capability\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-E1，R2同意。Base-vs-instruct decomposition提供部分分离但model type本身与时间高度相关。论文的控制（ability-matched仅降2.4pp，domain gains <0.1% variance）缩小了替代解释空间但未消除confound。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-N1\"\n    summary: \"术语一致性：measurement instability / temporal DIF / temporal comparability 交替使用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-W2, R1同意Minor。建议首次引入时明确定义关系。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === 历史 issues（前轮已 resolved，保留记录） ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大（13.5%-29.2%），核心结论不确定性被低估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"simple mean vs weighted mean DEFF 导致范围过宽\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"三方法收敛论证缺失\"\n      - round: 18\n        reviewers: []\n        note: \"三方法收敛写入 §4.2\"\n      - round: 19\n        reviewers: [1, 2]\n        note: \"De-dup K=20 29.1% 数据不一致被发现（实际 19.7%）。ICC flat across sizes (ρ=-0.009) justifies simple-mean。修正为两方法收敛。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20再次要求size-stratified DEFF和连续参数化曲线。论证不对称仍是核心问题。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次提出DEFF分歧（见R13-W2），但scope不同：R13关注正文呈现透明度而非方法论本身。\"\n    action_items:\n      - round: 19\n        action: \"De-dup 29.1%→19.7%, three→two convergence\"\n        assigned_to: director\n        status: done\n      - round: 19\n        action: \"ICC terminology fix (model-level r, not item-level ICC)\"\n        assigned_to: director\n        status: done\n      - round: 19\n        action: \"Singleton DEFF scope clarification (99.8% in cohort have families)\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Size-stratified DEFF table in appendix (tab:deff_stratified)\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"§4.2 forward reference to size-stratified DEFF (B8: commit 0c3856a)\"\n        assigned_to: agent\n        status: done\n    resolution: \"Size-stratified DEFF table added (appendix). Per-tier ICC 0.246→0.082 confirms weighted variant over-corrects. Forward reference in §4.2 (rebuttal branch). Family definition sensitivity ≤0.3pp.\"\n    resolution_round: 20\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力，framing 不一致\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"DIF 无法区分 contamination vs legitimate improvement\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20再次标为Must-Fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W1），scope类似但R13 reviewers没有前轮记忆。\"\n    action_items:\n      - round: 19\n        action: \"C1 meta-critique→orthogonal constructs\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Base-vs-instruct decomposition already in paper\"\n        assigned_to: agent\n        status: done\n    resolution: \"Four exclusion arguments + base-vs-instruct decomposition (χ²=562.7) + difficulty-dependent contamination alternative discussed. Framing: 'orthogonal constructs' throughout.\"\n    resolution_round: 20\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法从未被正式定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"K 的含义、操作步骤均未给出\"\n    action_items:\n      - round: 19\n        action: \"Formal definition added to app:dedup_k\"\n        assigned_to: director\n        status: done\n    resolution: \"Formal definition in app:dedup_k: K members sampled uniformly at random, 5 draws per K.\"\n    resolution_round: 19\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique 措辞过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    action_items:\n      - round: 19\n        action: \"meta-critique→orthogonal constructs throughout\"\n        assigned_to: director\n        status: done\n    resolution: \"Contribution 1 reframed as 'Orthogonal constructs'. All 'category error' language removed.\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性不足：MH-DIF 是既有标准方法的直接应用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W6）。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal-only strategy; no paper change\"\n        assigned_to: author\n        status: done\n    resolution: \"Structural limitation acknowledged. Framing emphasizes empirical contribution over methodological novelty.\"\n    resolution_round: 20\n\n  - id: \"R19-M2\"\n    summary: \"Semi-synthetic ΔTPR 推广性存疑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Difficulty-dependent injection results written to §4.5/§5.1\"\n        assigned_to: agent\n        status: done\n    resolution: \"Difficulty-dependent injection (3 schemes: A/B/C) completed and written to paper.\"\n    resolution_round: 20\n\n  - id: \"R19-M3\"\n    summary: \"K=10 non-uniform DIF 泄漏\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Strengthen NUDIF caveat wording\"\n        assigned_to: agent\n        status: done\n    resolution: \"NUDIF caveat strengthened in paper.\"\n    resolution_round: 20\n\n  - id: \"R19-M5\"\n    summary: \"1:1 matching 细节缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Caliper correction added to appendix\"\n        assigned_to: director\n        status: done\n    resolution: \"Matching details in appendix: 1:1 nearest-neighbor, caliper 0.02 (≈0.14 SD), Cohen's d=-0.17, N=638 per group.\"\n    resolution_round: 20\n\n  - id: \"R19-N3\"\n    summary: \"Abstract 范围暗示不匹配\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Abstract now reads '5,227 MMLU models'.\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"Appendix rank-bucket 数据错误\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Data corrected in app:rank_reversal.\"\n    resolution_round: 19\n\n  - id: \"R20-Q3\"\n    summary: \"Difficulty-direction替代解释未讨论\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"§5.1 discusses difficulty-dependent contamination as alternative.\"\n    resolution_round: 20\n\n  - id: \"R20-N1\"\n    summary: \"GSM1K探索性分析权重过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"GSM1K marked as 'exploratory... requires replication'.\"\n    resolution_round: 20\n\n  - id: \"R20-N2\"\n    summary: \"enlargethispage格式激进\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W4），但更严重：discussion.tex仍有\\\\enlargethispage*{10\\\\baselineskip}。\"\n    resolution: \"enlargethispage reduced to ≤4 baselineskip, within safe range.\"\n    resolution_round: 20\n\n  - id: \"R20-Q5\"\n    summary: \"6个月窗口C%高于年度对比需解释\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"Appendix explains: shorter temporal window → more polarized cohorts.\"\n    resolution_round: 20\n\n  - id: \"R20-Q6\"\n    summary: \"DIF Audit Protocol ≥500阈值缺统计依据\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"≥500 softened to 'smaller corpora may suffice with K=3 or 2×2 designs'.\"\n    resolution_round: 20\n\n  - id: \"R20-MR\"\n    summary: \"缺失引用：Kamata & Binici 2003, Alzahrani et al 2024, MMLU-Pro\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"All 3 citations verified real. 2/3 already in bib.\"\n    resolution_round: 20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "issues:\n  # === Round 13 新发现 ===\n\n  - id: \"R13-W1\"\n    summary: \"机制归因不足：DIF 检测 'that' 但无法区分 contamination / capability evolution / training shift\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M3/W-E1 + R2-W-N2 共识。R2标Must-Fix，R1降为Should-Fix（educational measurement中diagnostic-without-attribution是标准实践）。最终共识Should-Fix。论文需在Discussion中更清晰界定DIF审计在机制不明条件下的决策价值，并为Section 5.2 audit protocol添加caveats。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W2\"\n    summary: \"DEFF校正方法选择导致headline result 2×分歧（simple-mean 29.2% vs weighted-mean 13.5%），核心结论不确定性未充分透明呈现\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-S1 + R2-W-C2 共识。论文偏好simple-mean有合理论据（ρ_s=-0.009, size-stratified ICC递减），但weighted-mean是survey statistics标准方法。正文应更透明地同时报告两个估计。R2的4×范围(13.5%-53.2%)被R1纠正为2×范围(point estimates 27-29%, lower bound 13.5%)。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W3\"\n    summary: \"Semi-synthetic验证框架ecological validity不足：binary response flipping过于简化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M1, R2同意。验证了MH-DIF对differential item behavior的检测力，但injection model过于简化。Appendix A的mixed-mechanism injection也无法匹配instruct模型观测模式(simulated ρ_instruct=-0.302 vs observed -0.079)。建议增加更realistic的contamination model或更显式讨论ecological validity局限。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W4\"\n    summary: \"\\\\enlargethispage使用激进：Discussion页+10baselineskip，实质上在8页内塞入约9页内容\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-F1标Must-Fix，R1降为Should-Fix。discussion.tex \\\\enlargethispage*{10\\\\baselineskip}(+4.3cm) + experiments.tex \\\\enlargethispage*{4\\\\baselineskip} + 多处负vspace。R1指出\\\\enlargethispage是合法LaTeX命令且许多ACL论文使用，不应作为reject理由，但建议压缩内容至appendix。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"ΔFPR=0 guarantee在Introduction中未限定为single-subject contamination条件\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M2提出，R2部分同意（同意intro需限定条件，但纠正R1的非单调性论据——Table 7 ΔFPR是单调递增的）。Section 3.4 Remark已限定但intro Contribution 2未限定。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W6\"\n    summary: \"方法论新颖性有限：核心MH-DIF是1988年标准方法的领域迁移\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-N1。R1部分反驳（cross-subject matching和size-stratified DEFF是non-trivial适配），但同意核心贡献以应用和实证为主。两位reviewer均认为对EMNLP应定位为empirical contribution。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W7\"\n    summary: \"Conclusion仅一句话，未能收束论证\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-C1标Should-Fix，R1同意但降为Minor（Section 5 Discussion已承担大部分conclusion功能）。配合\\\\vspace{-28pt}是空间不足症状。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W8\"\n    summary: \"Temporal confound未完全解决：2023 vs 2024划分同时confound了architecture/training methodology/capability\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-E1，R2同意。Base-vs-instruct decomposition提供部分分离但model type本身与时间高度相关。论文的控制（ability-matched仅降2.4pp，domain gains <0.1% variance）缩小了替代解释空间但未消除confound。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-N1\"\n    summary: \"术语一致性：measurement instability / temporal DIF / temporal comparability 交替使用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 13\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-W2, R1同意Minor。建议首次引入时明确定义关系。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === 历史 issues（前轮已 resolved，保留记录） ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大（13.5%-29.2%），核心结论不确定性被低估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"simple mean vs weighted mean DEFF 导致范围过宽\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"三方法收敛论证缺失\"\n      - round: 18\n        reviewers: []\n        note: \"三方法收敛写入 §4.2\"\n      - round: 19\n        reviewers: [1, 2]\n        note: \"De-dup K=20 29.1% 数据不一致被发现（实际 19.7%）。ICC flat across sizes (ρ=-0.009) justifies simple-mean。修正为两方法收敛。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20再次要求size-stratified DEFF和连续参数化曲线。论证不对称仍是核心问题。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次提出DEFF分歧（见R13-W2），但scope不同：R13关注正文呈现透明度而非方法论本身。\"\n    action_items:\n      - round: 19\n        action: \"De-dup 29.1%→19.7%, three→two convergence\"\n        assigned_to: director\n        status: done\n      - round: 19\n        action: \"ICC terminology fix (model-level r, not item-level ICC)\"\n        assigned_to: director\n        status: done\n      - round: 19\n        action: \"Singleton DEFF scope clarification (99.8% in cohort have families)\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Size-stratified DEFF table in appendix (tab:deff_stratified)\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"§4.2 forward reference to size-stratified DEFF (B8: commit 0c3856a)\"\n        assigned_to: agent\n        status: done\n    resolution: \"Size-stratified DEFF table added (appendix). Per-tier ICC 0.246→0.082 confirms weighted variant over-corrects. Forward reference in §4.2 (rebuttal branch). Family definition sensitivity ≤0.3pp.\"\n    resolution_round: 20\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力，framing 不一致\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"DIF 无法区分 contamination vs legitimate improvement\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20再次标为Must-Fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W1），scope类似但R13 reviewers没有前轮记忆。\"\n    action_items:\n      - round: 19\n        action: \"C1 meta-critique→orthogonal constructs\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Base-vs-instruct decomposition already in paper\"\n        assigned_to: agent\n        status: done\n    resolution: \"Four exclusion arguments + base-vs-instruct decomposition (χ²=562.7) + difficulty-dependent contamination alternative discussed. Framing: 'orthogonal constructs' throughout.\"\n    resolution_round: 20\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法从未被正式定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"K 的含义、操作步骤均未给出\"\n    action_items:\n      - round: 19\n        action: \"Formal definition added to app:dedup_k\"\n        assigned_to: director\n        status: done\n    resolution: \"Formal definition in app:dedup_k: K members sampled uniformly at random, 5 draws per K.\"\n    resolution_round: 19\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique 措辞过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    action_items:\n      - round: 19\n        action: \"meta-critique→orthogonal constructs throughout\"\n        assigned_to: director\n        status: done\n    resolution: \"Contribution 1 reframed as 'Orthogonal constructs'. All 'category error' language removed.\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性不足：MH-DIF 是既有标准方法的直接应用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W6）。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal-only strategy; no paper change\"\n        assigned_to: author\n        status: done\n    resolution: \"Structural limitation acknowledged. Framing emphasizes empirical contribution over methodological novelty.\"\n    resolution_round: 20\n\n  - id: \"R19-M2\"\n    summary: \"Semi-synthetic ΔTPR 推广性存疑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Difficulty-dependent injection results written to §4.5/§5.1\"\n        assigned_to: agent\n        status: done\n    resolution: \"Difficulty-dependent injection (3 schemes: A/B/C) completed and written to paper.\"\n    resolution_round: 20\n\n  - id: \"R19-M3\"\n    summary: \"K=10 non-uniform DIF 泄漏\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Strengthen NUDIF caveat wording\"\n        assigned_to: agent\n        status: done\n    resolution: \"NUDIF caveat strengthened in paper.\"\n    resolution_round: 20\n\n  - id: \"R19-M5\"\n    summary: \"1:1 matching 细节缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Caliper correction added to appendix\"\n        assigned_to: director\n        status: done\n    resolution: \"Matching details in appendix: 1:1 nearest-neighbor, caliper 0.02 (≈0.14 SD), Cohen's d=-0.17, N=638 per group.\"\n    resolution_round: 20\n\n  - id: \"R19-N3\"\n    summary: \"Abstract 范围暗示不匹配\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Abstract now reads '5,227 MMLU models'.\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"Appendix rank-bucket 数据错误\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Data corrected in app:rank_reversal.\"\n    resolution_round: 19\n\n  - id: \"R20-Q3\"\n    summary: \"Difficulty-direction替代解释未讨论\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"§5.1 discusses difficulty-dependent contamination as alternative.\"\n    resolution_round: 20\n\n  - id: \"R20-N1\"\n    summary: \"GSM1K探索性分析权重过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"GSM1K marked as 'exploratory... requires replication'.\"\n    resolution_round: 20\n\n  - id: \"R20-N2\"\n    summary: \"enlargethispage格式激进\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W4），但更严重：discussion.tex仍有\\\\enlargethispage*{10\\\\baselineskip}。\"\n    resolution: \"enlargethispage reduced to ≤4 baselineskip, within safe range.\"\n    resolution_round: 20\n\n  - id: \"R20-Q5\"\n    summary: \"6个月窗口C%高于年度对比需解释\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"Appendix explains: shorter temporal window → more polarized cohorts.\"\n    resolution_round: 20\n\n  - id: \"R20-Q6\"\n    summary: \"DIF Audit Protocol ≥500阈值缺统计依据\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"≥500 softened to 'smaller corpora may suffice with K=3 or 2×2 designs'.\"\n    resolution_round: 20\n\n  - id: \"R20-MR\"\n    summary: \"缺失引用：Kamata & Binici 2003, Alzahrani et al 2024, MMLU-Pro\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"All 3 citations verified real. 2/3 already in bib.\"\n    resolution_round: 20"
  }
}
```

</details>

---


### Tool result

_source line 1239 · 2026-05-23T06:09:37.636555+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 12690}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-23T06:12:25.105024+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 13 审稿报告\n\n## Summary\n\n本文将教育测量领域的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法引入 LLM benchmark 评估，在 METABENCH 数据（5,227 模型 × 12,508 MMLU items）上检测 2023 与 2024 模型队列之间的 temporal measurement instability。核心发现：约 27–29% 的 MMLU items 经非独立性校正后表现出显著 temporal DIF（ETS Category C），且该信号与 web-overlap 污染标签近乎正交（Jaccard = 0.206, φ = 0.012）。论文引入 cross-subject matching（ΔFPR = 0 guarantee under single-subject contamination）、DEFF clustering 校正、semi-synthetic injection 验证框架，并在 6 个 METABENCH benchmarks 上复现。\n\n---\n\n## Strengths\n\n**S1. 实验规模与控制的系统性。** 5,227 模型 × 12,508 items 的分析规模远超此前 IRT/DIF 在 NLP 领域的应用。配合 random split 对照（C% = 0.18%）、ability-matched 对照（2.9%）、LOFO 稳健性、graduated de-duplication、DEFF 校正等多层控制，系统性排除了方法论伪迹。[R1-S2, R1-S3, R2-S1 共识]\n\n**S2. DIF 与 web-overlap 标签正交的概念性发现。** Enrichment = 0.964, φ = 0.012, OR = 1.05 [0.96, 1.15]。证明现有 contamination detection 方法和 DIF 捕捉的是根本不同的信号维度（global exposure vs. differential functioning）。[R1-S4, R2-S2 共识]\n\n**S3. Cross-subject matching 的方法适配。** ΔFPR = 0 在 k ≤ 5 subjects 下经验验证成立，是对标准 MH-DIF 在 LLM multi-domain 评估中的有意义适配。R1 指出这不是简单的 purified subtest matching（Nandakumar 1993），而是针对 LLM benchmarks 跨 subject 同时污染问题的新适配。[R1-S1, R2-S3 共识]\n\n**S4. 六个 benchmark 的跨域复现。** C% 从 17.9%（HellaSwag）到 31.3%（MMLU），知识型 vs 程序型 benchmark 的系统性差异提供描述性洞察。[R2-S4]\n\n**S5. Base-vs-instruct 分层分析。** χ² = 562.7, p < 10⁻¹²⁴，揭示 base 模型（60.1% reference-favoring, ρ = -0.570）与 instruct 模型（65.6% focal-favoring, ρ ≈ -0.079）的机制性差异。[R2-S5]\n\n**S6. Reproducibility 极高。** 匿名代码链接已提供，方法基于标准 MH 程序，数据来自公开 METABENCH，所有超参数和阈值均已明确报告。[R2 Reproducibility 5/5, R1 Reproducibility 4/5]\n\n---\n\n## Weaknesses\n\n### Should-Fix\n\n**W1. 机制归因不足：DIF 检测 \"that\" 但无法区分 contamination / capability evolution / training shift。** [R1-W-M3, R1-W-E1, R2-W-N2; 共识 Should-Fix]\n\n论文反复承认 DIF 只能检测\"有什么变化\"而非\"为什么变化\"，并列举三种可能机制但未提供任何区分方法。Mixed-mechanism injection（Appendix A）表明 semi-synthetic 框架也无法复现 instruct 模型的观测模式（simulated ρ_instruct = -0.302 vs. observed -0.079）。\n\n核心实用困境：如果 benchmark 维护者发现 C% = 31% 但不知道机制，Section 5.2 的 Monitor/Flag/Act 协议中 \"Act\" 层面的 stable-item rankings 可能移除反映合法能力变化的 items。\n\nR2 原标 Must-Fix，R1 降为 Should-Fix，理由是教育测量中 DIF 的标准用途即为 diagnostic-without-attribution（ETS 实践流程：先检测后由 SME 判断）。R1 进一步指出 Section 4.6 的 ρ ≥ 0.997 表明移除 C items 几乎不改变排名，practical harm 极低。最终共识 Should-Fix：论文需在 Discussion 中更清晰界定 DIF 审计在机制不明条件下的决策价值和边界。\n\n此外，Within-family DIF（Llama-2 vs. 3）C% = 61.3%（Table 1）远高于 Temporal 的 31.3%，强烈暗示 DIF 主要捕捉 model architecture/training paradigm 差异，R2-Q2 对此有深入讨论，两位 Reviewer 均认为论文应更显式讨论此发现对 contamination 叙事的影响。\n\n**W2. DEFF 校正方法选择导致 headline result 2× 分歧（29.2% vs 13.5%）。** [R1-W-S1, R2-W-C2; 共识 Should-Fix]\n\nSimple-mean DEFF（n̄ = 62.8）给出 29.2%，weighted-mean DEFF（n̄_w = 254.5, Kish 1965）给出 13.5%。论文偏好 simple-mean 的论据（ρ_s = -0.009; size-stratified ICC 从 0.246 递减至 0.082, Table 9）合理但非决定性。R1 指出 Kish weighted mean 是 survey statistics 标准方法，论文的反论证本质上是 domain-specific argument（LLM model families 不满足 homogeneity 假设），需要更强支撑。\n\nR2 原将不确定性范围表述为 \"13.5% 到 53.2%（4×）\"，被 R1 纠正：53.2% 是 cluster bootstrap CI 上界而非 point estimate；两个 convergent point estimates（simple-mean 29.2% + cluster bootstrap lower bound 26.7%）一致性高，准确范围是 ~2×。\n\n正文应更透明地同时呈现两个估计及其解读差异，而非将 13.5% 边缘化为 \"conservative extreme\"。\n\n**W3. Semi-synthetic 验证框架 ecological validity 不足。** [R1-W-M1, R2 同意; Should-Fix]\n\nBinary response flipping 是最简化的 contamination 模型。真实 contamination 模式远更复杂（memorization 改变 response distribution 而非确定性修正、contamination rate 与 item properties 相关、subject-dependent 结构）。Appendix A 的 mixed-mechanism injection 也无法匹配 instruct 模型观测模式，进一步暴露验证框架与现实的差距。\n\nR2 补充的 nuance：semi-synthetic 验证证明的核心命题是 \"MH-DIF 能检测 differential item behavior when present\"（response flipping 制造的是 ICC 移位），验证目标与应用 claim 的张力比表面上小一些，但仍存在。\n\n**W4. `\\enlargethispage` 使用激进，涉嫌违反 8 页限制精神。** [R2-W-F1, R1 同意; R2 标 Must-Fix, R1 降为 Should-Fix, 最终 Should-Fix]\n\n`discussion.tex` 使用 `\\enlargethispage*{10\\baselineskip}`（+4.3cm, ~20% 页面扩展），`experiments.tex` 另有 `\\enlargethispage*{4\\baselineskip}`，加上多处负 vspace（`\\vspace{-28pt}`, `\\vspace{-8pt}`, `\\vspace{-6pt}`），实质上在 8 页内塞入约 9 页内容。\n\nR1 指出 `\\enlargethispage` 是合法 LaTeX 命令、许多被接收 ACL 论文使用，不应作为 reject 理由，但建议压缩内容至 Appendix。R2 坚持 10\\baselineskip 远超排版微调范畴。共识 Should-Fix：削减 Discussion 或 Method 细节移至附录，实现不依赖排版技巧满足 8 页限制。\n\n**W5. ΔFPR = 0 guarantee 在 Introduction 中未限定为 single-subject contamination 条件。** [R1-W-M2, R2 部分同意; Should-Fix]\n\nSection 1 Contribution 2 写 \"comprising cross-subject matching (ΔFPR = 0 guarantee)\"，但 ΔFPR = 0 仅在 single-subject contamination 下成立（Section 3.4 Remark 已限定）。R2 确认 abstract 中未使用 \"ΔFPR = 0\" 表述，是措辞改进而非事实性错误。\n\n注：R1 原声称 Table 7 中 ΔFPR 存在非单调模式（k=20 时 ΔFPR ~0.009），被 R2 纠正为误读——Table 7 显示 ΔFPR 从 k=1（0.000）到 k=20（0.069）严格单调递增。\n\n**W6. 方法论新颖性有限：核心 MH-DIF 是 1988 年标准方法的领域迁移。** [R2-W-N1, R1 部分同意; Should-Fix]\n\n论文自认 \"We do not modify the MH procedure; our contribution is the application context.\" 三个 claimed contributions 中：orthogonal constructs 是经验发现、temporal DIF audit framework 是现有技术组合、temporal instability at scale 是规模而非新颖性。\n\nR1 反驳 R2 引用的先例（Nandakumar 1993, Donoghue 1993）是 purified subtest matching 而非 cross-benchmark matching，且 size-stratified DEFF 分析是 domain-specific 实证贡献。但 R1 同意核心贡献以应用和实证为主。\n\n两位 Reviewer 均认为论文应更诚实地定位为 \"大规模实证研究 + 领域适配\"，如此 framing 下贡献更具说服力。\n\n**W7. Temporal confound 未完全解决。** [R1-W-E1, R2 同意; Should-Fix]\n\n2023 vs. 2024 划分同时 confound 了 contamination 程度、architecture 演化（instruct/chat 比例变化）、capability scaling、training methodology（RLHF/DPO 普及）。Base-vs-instruct decomposition 部分解决但 model type 本身与时间高度相关，无法真正 deconfound。论文的控制（ability-matched 仅降 2.4pp, domain gains <0.1% variance, random split 0.18%）缩小替代解释空间但未消除 confound。\n\n### Minor\n\n**W8. Conclusion 仅一句话，收束不足。** [R2-W-C1 Should-Fix, R1 同意但降为 Minor]\n\n配合 `\\vspace{-28pt}` 是空间不足症状。R1 指出 Section 5 Discussion 已承担大部分 conclusion 功能。建议至少扩展为 4-6 句。\n\n**W9. 术语一致性。** [R2-W-W2, R1 同意; Minor]\n\n\"Measurement instability\"、\"temporal DIF\"、\"temporal comparability\" 交替使用。建议首次引入时明确定义关系。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 明确达成共识的关键问题：\n\n1. **[AGREE]** 机制归因不足是论文最根本的局限，但 Should-Fix 而非 Must-Fix（diagnostic-without-attribution 是 DIF 的标准用途）\n2. **[AGREE]** DEFF 校正 2× 分歧需要在正文中更透明呈现\n3. **[AGREE]** Semi-synthetic ecological validity 不足，binary flipping 过于简化\n4. **[AGREE]** `\\enlargethispage*{10\\baselineskip}` 过于激进，需压缩内容\n5. **[AGREE]** ΔFPR=0 在 intro 中需限定 single-subject 条件\n6. **[AGREE]** 核心贡献以应用和实证为主，应定位为 empirical paper\n7. **[AGREE]** Temporal confound 未完全解决，是固有局限\n8. **[AGREE]** Within-family C%=61.3% 对 contamination 叙事构成挑战，论文应更显式讨论\n\n## Reviewer Divergence\n\n1. **W-N2 严重程度**：R2 标 Must-Fix，R1 降为 Should-Fix。R1 论据更有说服力（DIF 在教育测量中的标准用途即为 diagnostic-without-attribution），最终采纳 Should-Fix。\n2. **W-F1 严重程度**：R2 标 Must-Fix，R1 降为 Should-Fix。R1 指出 `\\enlargethispage` 是合法 LaTeX 命令且不应作为 reject 理由，最终采纳 Should-Fix。\n3. **Notation density**（R2-W-W1）：R1 反驳，认为对方法论论文而言 notation 密度正常，减少会损害 reproducibility。最终不纳入 weakness。\n4. **R1 的 Table 7 非单调性论据**：被 R2 纠正为误读（ΔFPR 是严格单调递增的），R1 该论点不成立。\n\n---\n\n## Questions\n\n**Q1.** 从 benchmark 维护者角度，DIF 审计在机制不明条件下提供了什么 contamination detection 和常规 benchmark analysis 无法提供的独特 actionable value？\"Items function differently across cohorts\" 这一事实本身是否足以驱动维护决策？[R2-Q1, 共识]\n\n**Q2.** Within-family (Llama-2 vs. 3) C% = 61.3% 远高于 Temporal 31.3%。这是否意味着 DIF 主要反映 model architecture/training 差异而非 benchmark integrity 问题？这对 DIF 作为 benchmark 质量指标的定位有何影响？[R2-Q2, R1 同意]\n\n**Q3.** 移除 Mistral/Llama-3 后 C% 降至 22-24%（Table 8）。论文通过 Monte Carlo calibration 区分了 composition vs power effect，但这是否说明 headline number 对少数大 family 依赖过强？[R1-Q4, R2 同意]\n\n**Q4.** Cross-subject matching variable（56 个 subjects 的 total score）是否被 item 数量多的 subjects（如 STEM 类）主导，引入隐式权重偏差？[R1-Q1, R2 同意]\n\n**Q5.** 是否考虑过 logistic regression DIF 或 SIBTEST 作为方法论比较/sensitivity check？在 5,227 examinees 规模下，continuous matching 可以避免 K-stratification 的信息损失。[R1-Q4, R2-Q4]\n\n**Q6.** METABENCH 数据中是否有 model quality filtering？Open LLM Leaderboard 上存在低质量提交，未过滤可能膨胀 DIF rates。[R1-Q6, R2 同意]\n\n**Q7.** Item-property predictive analysis AUC ≈ 0.60（Appendix F）意味着无法事前预测哪些 items 会 exhibit DIF，Section 5.2 的 pre-screening infeasibility 结论正确，但 post-hoc-only monitoring 的实用价值几何？[R1-W-E2, R2 同意]\n\n---\n\n## Missing References\n\n1. **Multi-group CFA / alignment methods**：Millsap & Olivera-Aguilar (2012); Asparouhov & Muthén (2014) alignment method。作为 measurement invariance 的结构级替代方案，Related Work 讨论 MIMIC models 时可补充。[R2 提出, R1 同意]\n\n2. **Logistic regression DIF / SIBTEST 作为方法论 sensitivity check**：论文仅使用 MH-DIF 一种方法。[R1, R2 共识]\n\nR1 反驳 R2 提出的 dataset shift / concept drift 文献（Quinonero-Candela et al. 2009），认为 DIF 是 item-level analysis 而 dataset shift 是 distribution-level analysis，粒度不同，关联有限。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 15 info, 0 critical）。\n\n主要发现：\n- **[Warning] Pages 5-6**：连续 2 页纯文本无 display item（Method cohort designs + Experiments validation），大量数字密集叙述无视觉锚点。建议提取关键结果为 summary table。\n- **[Warning] Page 7**：单页堆叠 3 个 display items（Table 1 + Figure 2 + Table 2），与前 2 页纯文本形成强烈反差，布局节奏不均匀。\n- **[Warning] Page 17**：最后一页内容不足 1/2，Figure 6 上下均有大块空白。\n- 无 margin 溢出、公式渲染错误、未解析引用或 section heading 孤悬问题。\n- 主文共 5 个 display items（2 figures + 3 tables），约 0.63/页，密度偏低但对 psychometric 方法论文可接受。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 5/5 | 4.5/5 |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n\n**合成评语**：\n\n这是一篇有实质跨学科价值的大规模实证研究——将教育测量领域的 MH-DIF 方法系统性引入 LLM benchmark 评估，并做了有意义的方法适配（cross-subject matching、DEFF size-stratified 校正）。DIF 与 web-overlap 标签正交（Jaccard = 0.206）以及六个 benchmark 的跨域复现是有概念性贡献的发现，reproducibility 极高。\n\n但论文存在多个相互关联的 Should-Fix 级问题：(1) 机制归因不足使得核心实用价值受限——Within-family C% = 61.3% 暗示 DIF 主要捕捉 model training 差异而非 benchmark integrity 问题；(2) DEFF 校正方法选择导致 headline result 2× 分歧（29.2% vs 13.5%），正文呈现不够透明；(3) semi-synthetic 验证框架 ecological validity 不足，验证了 contamination detection 但应用 claim 扩展到更广义的 measurement instability；(4) `\\enlargethispage*{10\\baselineskip}` 过于激进，实质上超出了 8 页限制。\n\n核心张力是：一篇应用现有方法（1988 年 MH-DIF）的大规模实证论文，其 contribution 是否足够支撑 EMNLP 主会议接收。如果作者能 (a) 在 Discussion 中更清晰界定 DIF 审计在机制不明条件下的决策边界，(b) 更透明地呈现 DEFF 不确定性，(c) 限定 ΔFPR=0 条件，(d) 压缩正文至真正的 8 页，论文可上调至 4.0。当前定位为 Findings 接收概率更高。\n\n**升分路径**：修订 claim scoping + DEFF 透明呈现 + 压缩正文格式 → 4.0 (Conference)\n**降分风险**：若 AC 认定格式违规或 novelty 不足 → 3.0 (Findings)\n\n**Confidence**: 4/5\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 中 \"ΔFPR = 0 guarantee\" 需限定 \"under single-subject contamination\"\n- 三个贡献点的 framing 建议调整：明确定位为 empirical contribution + domain adaptation，而非暗示方法论突破\n\n### Section 3 (Method)\n- Section 3.4 Remark 已限定 ΔFPR=0 条件，但 intro 未同步\n- Binary response flipping 的 ecological validity 局限应在方法描述中更显式说明（当前仅在 Limitations 提及）\n\n### Section 4 (Experiments)\n- Section 4.2：DEFF 校正结果（13.5% vs 29.2%）应在正文中更透明呈现，而非仅在 Appendix 展开\n- Table 1：Within-family C% = 61.3% 的含义应在正文中讨论，而非仅作为 cohort comparison 的一行数据\n\n### Section 5 (Discussion)\n- `\\enlargethispage*{10\\baselineskip}` 需削减至合理范围\n- Section 5.1：需更显式讨论 DIF 审计在机制不明条件下的决策价值，以及 stable-item removal 在 capability evolution 场景下的潜在问题\n- Section 5.2：Audit protocol 需添加 caveat——在能力演化场景下 removing DIF items 可能有害\n\n### Section 6 (Conclusion)\n- 扩展至 4-6 句，涵盖核心发现、实际意义、主要局限\n\n### Formatting\n- `\\enlargethispage*{10\\baselineskip}` 在 Discussion 页 + `\\enlargethispage*{4\\baselineskip}` 在 Experiments 页 + 多处负 vspace → 建议将 Method 的 LLM-specific challenges 段或 Discussion 的详细机制讨论移至 Appendix\n- Pages 5-6 连续纯文本、Page 7 三个 display items 堆叠 → 建议重新分配 display items 的位置以平衡布局节奏",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 13 审稿报告\n\n## Summary\n\n本文将教育测量领域的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 方法引入 LLM benchmark 评估，在 METABENCH 数据（5,227 模型 × 12,508 MMLU items）上检测 2023 与 2024 模型队列之间的 temporal measurement instability。核心发现：约 27–29% 的 MMLU items 经非独立性校正后表现出显著 temporal DIF（ETS Category C），且该信号与 web-overlap 污染标签近乎正交（Jaccard = 0.206, φ = 0.012）。论文引入 cross-subject matching（ΔFPR = 0 guarantee under single-subject contamination）、DEFF clustering 校正、semi-synthetic injection 验证框架，并在 6 个 METABENCH benchmarks 上复现。\n\n---\n\n## Strengths\n\n**S1. 实验规模与控制的系统性。** 5,227 模型 × 12,508 items 的分析规模远超此前 IRT/DIF 在 NLP 领域的应用。配合 random split 对照（C% = 0.18%）、ability-matched 对照（2.9%）、LOFO 稳健性、graduated de-duplication、DEFF 校正等多层控制，系统性排除了方法论伪迹。[R1-S2, R1-S3, R2-S1 共识]\n\n**S2. DIF 与 web-overlap 标签正交的概念性发现。** Enrichment = 0.964, φ = 0.012, OR = 1.05 [0.96, 1.15]。证明现有 contamination detection 方法和 DIF 捕捉的是根本不同的信号维度（global exposure vs. differential functioning）。[R1-S4, R2-S2 共识]\n\n**S3. Cross-subject matching 的方法适配。** ΔFPR = 0 在 k ≤ 5 subjects 下经验验证成立，是对标准 MH-DIF 在 LLM multi-domain 评估中的有意义适配。R1 指出这不是简单的 purified subtest matching（Nandakumar 1993），而是针对 LLM benchmarks 跨 subject 同时污染问题的新适配。[R1-S1, R2-S3 共识]\n\n**S4. 六个 benchmark 的跨域复现。** C% 从 17.9%（HellaSwag）到 31.3%（MMLU），知识型 vs 程序型 benchmark 的系统性差异提供描述性洞察。[R2-S4]\n\n**S5. Base-vs-instruct 分层分析。** χ² = 562.7, p < 10⁻¹²⁴，揭示 base 模型（60.1% reference-favoring, ρ = -0.570）与 instruct 模型（65.6% focal-favoring, ρ ≈ -0.079）的机制性差异。[R2-S5]\n\n**S6. Reproducibility 极高。** 匿名代码链接已提供，方法基于标准 MH 程序，数据来自公开 METABENCH，所有超参数和阈值均已明确报告。[R2 Reproducibility 5/5, R1 Reproducibility 4/5]\n\n---\n\n## Weaknesses\n\n### Should-Fix\n\n**W1. 机制归因不足：DIF 检测 \"that\" 但无法区分 contamination / capability evolution / training shift。** [R1-W-M3, R1-W-E1, R2-W-N2; 共识 Should-Fix]\n\n论文反复承认 DIF 只能检测\"有什么变化\"而非\"为什么变化\"，并列举三种可能机制但未提供任何区分方法。Mixed-mechanism injection（Appendix A）表明 semi-synthetic 框架也无法复现 instruct 模型的观测模式（simulated ρ_instruct = -0.302 vs. observed -0.079）。\n\n核心实用困境：如果 benchmark 维护者发现 C% = 31% 但不知道机制，Section 5.2 的 Monitor/Flag/Act 协议中 \"Act\" 层面的 stable-item rankings 可能移除反映合法能力变化的 items。\n\nR2 原标 Must-Fix，R1 降为 Should-Fix，理由是教育测量中 DIF 的标准用途即为 diagnostic-without-attribution（ETS 实践流程：先检测后由 SME 判断）。R1 进一步指出 Section 4.6 的 ρ ≥ 0.997 表明移除 C items 几乎不改变排名，practical harm 极低。最终共识 Should-Fix：论文需在 Discussion 中更清晰界定 DIF 审计在机制不明条件下的决策价值和边界。\n\n此外，Within-family DIF（Llama-2 vs. 3）C% = 61.3%（Table 1）远高于 Temporal 的 31.3%，强烈暗示 DIF 主要捕捉 model architecture/training paradigm 差异，R2-Q2 对此有深入讨论，两位 Reviewer 均认为论文应更显式讨论此发现对 contamination 叙事的影响。\n\n**W2. DEFF 校正方法选择导致 headline result 2× 分歧（29.2% vs 13.5%）。** [R1-W-S1, R2-W-C2; 共识 Should-Fix]\n\nSimple-mean DEFF（n̄ = 62.8）给出 29.2%，weighted-mean DEFF（n̄_w = 254.5, Kish 1965）给出 13.5%。论文偏好 simple-mean 的论据（ρ_s = -0.009; size-stratified ICC 从 0.246 递减至 0.082, Table 9）合理但非决定性。R1 指出 Kish weighted mean 是 survey statistics 标准方法，论文的反论证本质上是 domain-specific argument（LLM model families 不满足 homogeneity 假设），需要更强支撑。\n\nR2 原将不确定性范围表述为 \"13.5% 到 53.2%（4×）\"，被 R1 纠正：53.2% 是 cluster bootstrap CI 上界而非 point estimate；两个 convergent point estimates（simple-mean 29.2% + cluster bootstrap lower bound 26.7%）一致性高，准确范围是 ~2×。\n\n正文应更透明地同时呈现两个估计及其解读差异，而非将 13.5% 边缘化为 \"conservative extreme\"。\n\n**W3. Semi-synthetic 验证框架 ecological validity 不足。** [R1-W-M1, R2 同意; Should-Fix]\n\nBinary response flipping 是最简化的 contamination 模型。真实 contamination 模式远更复杂（memorization 改变 response distribution 而非确定性修正、contamination rate 与 item properties 相关、subject-dependent 结构）。Appendix A 的 mixed-mechanism injection 也无法匹配 instruct 模型观测模式，进一步暴露验证框架与现实的差距。\n\nR2 补充的 nuance：semi-synthetic 验证证明的核心命题是 \"MH-DIF 能检测 differential item behavior when present\"（response flipping 制造的是 ICC 移位），验证目标与应用 claim 的张力比表面上小一些，但仍存在。\n\n**W4. `\\enlargethispage` 使用激进，涉嫌违反 8 页限制精神。** [R2-W-F1, R1 同意; R2 标 Must-Fix, R1 降为 Should-Fix, 最终 Should-Fix]\n\n`discussion.tex` 使用 `\\enlargethispage*{10\\baselineskip}`（+4.3cm, ~20% 页面扩展），`experiments.tex` 另有 `\\enlargethispage*{4\\baselineskip}`，加上多处负 vspace（`\\vspace{-28pt}`, `\\vspace{-8pt}`, `\\vspace{-6pt}`），实质上在 8 页内塞入约 9 页内容。\n\nR1 指出 `\\enlargethispage` 是合法 LaTeX 命令、许多被接收 ACL 论文使用，不应作为 reject 理由，但建议压缩内容至 Appendix。R2 坚持 10\\baselineskip 远超排版微调范畴。共识 Should-Fix：削减 Discussion 或 Method 细节移至附录，实现不依赖排版技巧满足 8 页限制。\n\n**W5. ΔFPR = 0 guarantee 在 Introduction 中未限定为 single-subject contamination 条件。** [R1-W-M2, R2 部分同意; Should-Fix]\n\nSection 1 Contribution 2 写 \"comprising cross-subject matching (ΔFPR = 0 guarantee)\"，但 ΔFPR = 0 仅在 single-subject contamination 下成立（Section 3.4 Remark 已限定）。R2 确认 abstract 中未使用 \"ΔFPR = 0\" 表述，是措辞改进而非事实性错误。\n\n注：R1 原声称 Table 7 中 ΔFPR 存在非单调模式（k=20 时 ΔFPR ~0.009），被 R2 纠正为误读——Table 7 显示 ΔFPR 从 k=1（0.000）到 k=20（0.069）严格单调递增。\n\n**W6. 方法论新颖性有限：核心 MH-DIF 是 1988 年标准方法的领域迁移。** [R2-W-N1, R1 部分同意; Should-Fix]\n\n论文自认 \"We do not modify the MH procedure; our contribution is the application context.\" 三个 claimed contributions 中：orthogonal constructs 是经验发现、temporal DIF audit framework 是现有技术组合、temporal instability at scale 是规模而非新颖性。\n\nR1 反驳 R2 引用的先例（Nandakumar 1993, Donoghue 1993）是 purified subtest matching 而非 cross-benchmark matching，且 size-stratified DEFF 分析是 domain-specific 实证贡献。但 R1 同意核心贡献以应用和实证为主。\n\n两位 Reviewer 均认为论文应更诚实地定位为 \"大规模实证研究 + 领域适配\"，如此 framing 下贡献更具说服力。\n\n**W7. Temporal confound 未完全解决。** [R1-W-E1, R2 同意; Should-Fix]\n\n2023 vs. 2024 划分同时 confound 了 contamination 程度、architecture 演化（instruct/chat 比例变化）、capability scaling、training methodology（RLHF/DPO 普及）。Base-vs-instruct decomposition 部分解决但 model type 本身与时间高度相关，无法真正 deconfound。论文的控制（ability-matched 仅降 2.4pp, domain gains <0.1% variance, random split 0.18%）缩小替代解释空间但未消除 confound。\n\n### Minor\n\n**W8. Conclusion 仅一句话，收束不足。** [R2-W-C1 Should-Fix, R1 同意但降为 Minor]\n\n配合 `\\vspace{-28pt}` 是空间不足症状。R1 指出 Section 5 Discussion 已承担大部分 conclusion 功能。建议至少扩展为 4-6 句。\n\n**W9. 术语一致性。** [R2-W-W2, R1 同意; Minor]\n\n\"Measurement instability\"、\"temporal DIF\"、\"temporal comparability\" 交替使用。建议首次引入时明确定义关系。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 明确达成共识的关键问题：\n\n1. **[AGREE]** 机制归因不足是论文最根本的局限，但 Should-Fix 而非 Must-Fix（diagnostic-without-attribution 是 DIF 的标准用途）\n2. **[AGREE]** DEFF 校正 2× 分歧需要在正文中更透明呈现\n3. **[AGREE]** Semi-synthetic ecological validity 不足，binary flipping 过于简化\n4. **[AGREE]** `\\enlargethispage*{10\\baselineskip}` 过于激进，需压缩内容\n5. **[AGREE]** ΔFPR=0 在 intro 中需限定 single-subject 条件\n6. **[AGREE]** 核心贡献以应用和实证为主，应定位为 empirical paper\n7. **[AGREE]** Temporal confound 未完全解决，是固有局限\n8. **[AGREE]** Within-family C%=61.3% 对 contamination 叙事构成挑战，论文应更显式讨论\n\n## Reviewer Divergence\n\n1. **W-N2 严重程度**：R2 标 Must-Fix，R1 降为 Should-Fix。R1 论据更有说服力（DIF 在教育测量中的标准用途即为 diagnostic-without-attribution），最终采纳 Should-Fix。\n2. **W-F1 严重程度**：R2 标 Must-Fix，R1 降为 Should-Fix。R1 指出 `\\enlargethispage` 是合法 LaTeX 命令且不应作为 reject 理由，最终采纳 Should-Fix。\n3. **Notation density**（R2-W-W1）：R1 反驳，认为对方法论论文而言 notation 密度正常，减少会损害 reproducibility。最终不纳入 weakness。\n4. **R1 的 Table 7 非单调性论据**：被 R2 纠正为误读（ΔFPR 是严格单调递增的），R1 该论点不成立。\n\n---\n\n## Questions\n\n**Q1.** 从 benchmark 维护者角度，DIF 审计在机制不明条件下提供了什么 contamination detection 和常规 benchmark analysis 无法提供的独特 actionable value？\"Items function differently across cohorts\" 这一事实本身是否足以驱动维护决策？[R2-Q1, 共识]\n\n**Q2.** Within-family (Llama-2 vs. 3) C% = 61.3% 远高于 Temporal 31.3%。这是否意味着 DIF 主要反映 model architecture/training 差异而非 benchmark integrity 问题？这对 DIF 作为 benchmark 质量指标的定位有何影响？[R2-Q2, R1 同意]\n\n**Q3.** 移除 Mistral/Llama-3 后 C% 降至 22-24%（Table 8）。论文通过 Monte Carlo calibration 区分了 composition vs power effect，但这是否说明 headline number 对少数大 family 依赖过强？[R1-Q4, R2 同意]\n\n**Q4.** Cross-subject matching variable（56 个 subjects 的 total score）是否被 item 数量多的 subjects（如 STEM 类）主导，引入隐式权重偏差？[R1-Q1, R2 同意]\n\n**Q5.** 是否考虑过 logistic regression DIF 或 SIBTEST 作为方法论比较/sensitivity check？在 5,227 examinees 规模下，continuous matching 可以避免 K-stratification 的信息损失。[R1-Q4, R2-Q4]\n\n**Q6.** METABENCH 数据中是否有 model quality filtering？Open LLM Leaderboard 上存在低质量提交，未过滤可能膨胀 DIF rates。[R1-Q6, R2 同意]\n\n**Q7.** Item-property predictive analysis AUC ≈ 0.60（Appendix F）意味着无法事前预测哪些 items 会 exhibit DIF，Section 5.2 的 pre-screening infeasibility 结论正确，但 post-hoc-only monitoring 的实用价值几何？[R1-W-E2, R2 同意]\n\n---\n\n## Missing References\n\n1. **Multi-group CFA / alignment methods**：Millsap & Olivera-Aguilar (2012); Asparouhov & Muthén (2014) alignment method。作为 measurement invariance 的结构级替代方案，Related Work 讨论 MIMIC models 时可补充。[R2 提出, R1 同意]\n\n2. **Logistic regression DIF / SIBTEST 作为方法论 sensitivity check**：论文仅使用 MH-DIF 一种方法。[R1, R2 共识]\n\nR1 反驳 R2 提出的 dataset shift / concept drift 文献（Quinonero-Candela et al. 2009），认为 DIF 是 item-level analysis 而 dataset shift 是 distribution-level analysis，粒度不同，关联有限。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（3 warnings, 15 info, 0 critical）。\n\n主要发现：\n- **[Warning] Pages 5-6**：连续 2 页纯文本无 display item（Method cohort designs + Experiments validation），大量数字密集叙述无视觉锚点。建议提取关键结果为 summary table。\n- **[Warning] Page 7**：单页堆叠 3 个 display items（Table 1 + Figure 2 + Table 2），与前 2 页纯文本形成强烈反差，布局节奏不均匀。\n- **[Warning] Page 17**：最后一页内容不足 1/2，Figure 6 上下均有大块空白。\n- 无 margin 溢出、公式渲染错误、未解析引用或 section heading 孤悬问题。\n- 主文共 5 个 display items（2 figures + 3 tables），约 0.63/页，密度偏低但对 psychometric 方法论文可接受。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 5/5 | 4.5/5 |\n| Overall | 3.5/5 | 3.5/5 | **3.5/5** |\n\n**合成评语**：\n\n这是一篇有实质跨学科价值的大规模实证研究——将教育测量领域的 MH-DIF 方法系统性引入 LLM benchmark 评估，并做了有意义的方法适配（cross-subject matching、DEFF size-stratified 校正）。DIF 与 web-overlap 标签正交（Jaccard = 0.206）以及六个 benchmark 的跨域复现是有概念性贡献的发现，reproducibility 极高。\n\n但论文存在多个相互关联的 Should-Fix 级问题：(1) 机制归因不足使得核心实用价值受限——Within-family C% = 61.3% 暗示 DIF 主要捕捉 model training 差异而非 benchmark integrity 问题；(2) DEFF 校正方法选择导致 headline result 2× 分歧（29.2% vs 13.5%），正文呈现不够透明；(3) semi-synthetic 验证框架 ecological validity 不足，验证了 contamination detection 但应用 claim 扩展到更广义的 measurement instability；(4) `\\enlargethispage*{10\\baselineskip}` 过于激进，实质上超出了 8 页限制。\n\n核心张力是：一篇应用现有方法（1988 年 MH-DIF）的大规模实证论文，其 contribution 是否足够支撑 EMNLP 主会议接收。如果作者能 (a) 在 Discussion 中更清晰界定 DIF 审计在机制不明条件下的决策边界，(b) 更透明地呈现 DEFF 不确定性，(c) 限定 ΔFPR=0 条件，(d) 压缩正文至真正的 8 页，论文可上调至 4.0。当前定位为 Findings 接收概率更高。\n\n**升分路径**：修订 claim scoping + DEFF 透明呈现 + 压缩正文格式 → 4.0 (Conference)\n**降分风险**：若 AC 认定格式违规或 novelty 不足 → 3.0 (Findings)\n\n**Confidence**: 4/5\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 中 \"ΔFPR = 0 guarantee\" 需限定 \"under single-subject contamination\"\n- 三个贡献点的 framing 建议调整：明确定位为 empirical contribution + domain adaptation，而非暗示方法论突破\n\n### Section 3 (Method)\n- Section 3.4 Remark 已限定 ΔFPR=0 条件，但 intro 未同步\n- Binary response flipping 的 ecological validity 局限应在方法描述中更显式说明（当前仅在 Limitations 提及）\n\n### Section 4 (Experiments)\n- Section 4.2：DEFF 校正结果（13.5% vs 29.2%）应在正文中更透明呈现，而非仅在 Appendix 展开\n- Table 1：Within-family C% = 61.3% 的含义应在正文中讨论，而非仅作为 cohort comparison 的一行数据\n\n### Section 5 (Discussion)\n- `\\enlargethispage*{10\\baselineskip}` 需削减至合理范围\n- Section 5.1：需更显式讨论 DIF 审计在机制不明条件下的决策价值，以及 stable-item removal 在 capability evolution 场景下的潜在问题\n- Section 5.2：Audit protocol 需添加 caveat——在能力演化场景下 removing DIF items 可能有害\n\n### Section 6 (Conclusion)\n- 扩展至 4-6 句，涵盖核心发现、实际意义、主要局限\n\n### Formatting\n- `\\enlargethispage*{10\\baselineskip}` 在 Discussion 页 + `\\enlargethispage*{4\\baselineskip}` 在 Experiments 页 + 多处负 vspace → 建议将 Method 的 LLM-specific challenges 段或 Discussion 的详细机制讨论移至 Appendix\n- Pages 5-6 连续纯文本、Page 7 三个 display items 堆叠 → 建议重新分配 display items 的位置以平衡布局节奏",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1241 · 2026-05-23T06:12:29.219685+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4114
}
```

</details>

---


### Assistant

_source line 1242 · 2026-05-23T06:12:38.949865+00:00_

审稿报告已投递。

**Round 13 审稿完成：**

- **Overall: 3.5 (Borderline Conference)**
- 两位 Reviewer 评分一致，核心问题已达共识
- 7 个 Should-Fix（机制归因、DEFF 透明度、semi-synthetic ecological validity、enlargethispage、ΔFPR=0 scope、novelty 定位、temporal confound）+ 2 个 Minor（conclusion 简略、术语一致性）
- Issue Tracker 已更新 9 条新发现
- 升分路径明确：修订 claim scoping + DEFF 透明呈现 + 格式压缩 → 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 123

## Round 123

2 recorded events


### User

_source line 1243 · 2026-05-23T06:12:41.648816+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心判断：

- R1 的 12 条意见中，我同意 8 条、反驳 2 条（ΔFPR 非单调是误读 Table 7；abstract 数字不一致是误读 27,125）、部分同意 2 条
- 两位 reviewer 独立汇聚的三个核心问题：机制归因不足、DEFF 不确定性范围过宽、novelty 定位
- 维持 3.5 (Borderline Conference) 评分不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1244 · 2026-05-23T06:12:52.027061+00:00_

审稿报告已在交叉回应收集完毕后合成并投递给 Research Director。

**Round 13 审稿完成。**

核心结论：**3.5 — Borderline Conference**

7 条 Should-Fix + 2 条 Minor。两位 Reviewer 均为 3.5，关键共识点：
1. 机制归因不足（Should-Fix，非 Must-Fix）
2. DEFF 2× 分歧需更透明呈现
3. Semi-synthetic ecological validity 不足
4. `\enlargethispage*{10\baselineskip}` 过于激进
5. 方法论新颖性有限，应定位为 empirical paper

升分路径：修订 claim scoping + DEFF 透明呈现 + 压缩正文格式 → 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 124

## Round 124

54 recorded events


### User

_source line 1245 · 2026-05-23T07:53:59.139630+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2025-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-23T07:54:04.513160+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-23T07:54:04.564217+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1248 · 2026-05-23T07:54:22.657819+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file,WebSearch",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file,WebSearch",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-23T07:54:22.708454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-23T07:54:25.570867+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-23T07:54:25.571350+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-23T07:54:30.848734+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-23T07:54:30.899373+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-23T07:54:37.879200+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-23T07:54:38.833391+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-23T07:54:39.386102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-23T07:54:40.340502+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Measurement Instability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1258 · 2026-05-23T07:54:40.341001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2025 2026 call for papers submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2025 2026 call for papers submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-23T07:54:41.345211+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 1260 · 2026-05-23T07:54:41.597002+00:00_

issues:
  # === Round 13 新发现 ===

  - id: "R13-W1"
    summary: "机制归因不足：DIF 检测 'that' 但无法区分 contamination / capability evolution / training shift"
    category: framing
    severity: critical
    status: open
    first_raised_round: 13
    last_seen_round: 13
    mentions:
      - round: 13
        reviewers: [1, 2]
        note: "R1-W-M3/W-E1 + R2-W-N2 共识。R2标Must-Fix，R1降为Should-Fix（educational measurement中diagnostic-without-attribution是标准实践）。最终共识Should-Fix。论文需在Discussion中更清晰界定DIF审计在机制不明条件下的决策价值，并为Section 5.2 audit protocol添加caveats。"
    action_items: []
    resolution: ""
    resolution_round: null

  - id: "R13-W2"
    summary: "DEFF校正方法选择导致headline result 2×分歧（simple-mean 29.2% vs weighted-mean 13.5%），核心结论不确定性未充分透明呈现"
    category: method
    severity: warning
    status: open
    first_raised_round: 13
    last_seen_round: 13
    mentions:
      - round: 13
        reviewers: [1, 2]
        note: "R1-W-S1 + R2-W-C2 共识。论文偏好simple-mean有合理论据（ρ_s=-0.009, size-stratified ICC递减），但weighted-mean是survey statistics标准方法。正文应更透明地同时报告两个估计。R2的4×范围(13.5%-53.2%)被R1纠正为2×范围(point estimates 27-29%, lower bound 13.5%)。"
    action_items: []
    resolution: ""
    resolution_round: null

  - id: "R13-W3"
    summary: "Semi-synthetic验证框架ecological validity不足：binary response flipping过于简化"
    category: method
    severity: warning
    status: open
    first_raised_round: 13
    last_seen_round: 13
    mentions:
      - round: 13
        reviewers: [1, 2]
        note: "R1-W-M1, R2同意。验证了MH-DIF对differential item behavior的检测力，但injection model过于简化。Appendix A的mixed-mechanism injection也无法匹配instruct模型观测模式(simulated ρ_instruct=-0.302 vs observed -0.079)。建议增加更realistic的contamination model或更显式讨论ecological validity局限。"
    action_items: []
    resolution: ""
    resolution_round: null

  - id: "R13-W4"
    summary: "\\enlargethispage使用激进：Discussion页+10baselineskip，实质上在8页内塞入约9页内容"
    category: format
    severity: warning
    status: open
    first_raised_round: 13
    last_seen_round: 13
    me
…[truncated 10690 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-23T07:54:48.023505+00:00_

Web search results for query: "ACL Rolling Review ARR 2025 2026 call for papers submission guidelines author instructions page limit"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Main Conference - ACL 2025","url":"https://2025.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on my search results, here's information about ACL Rolling Review (ARR) submission guidelines for 2025-2026:

## Page Limits

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. The limitations section will appear at the end of the paper, after the discussion/conclusions section and before the references, and will not count towards the page limit.

## Key Submission Guidelines

All long, short, and theme papers must follow the ACL Author Guidelines.

Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be avoided.

EACL 2026 requires all papers to have a clear discussion of limitations, in
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 7682
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-23T07:55:02.840334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-23T07:55:03.646091+00:00_

abstract.tex
appendix.tex
conclusion.tex
discussion.tex
experiments.tex
introduction.tex
limitations.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-23T07:55:03.998430+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check review round 14 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check review round 14 directory"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-23T07:55:04.099603+00:00_

submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-23T07:55:09.295567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-23T07:55:09.446929+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. Existing contamination detectors validate against web-overlap labels that conflate global exposure with differential functioning. We apply differential item functioning (DIF) analysis from educational measurement to six METABENCH benchmarks (5,227 MMLU models, 27,125 items across all six), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF; for MMLU, two convergent non-independence corrections yield approximately 27--29\% (conservative bound: 13.5\%; cluster bootstrap 95\% CI $[26.7\%, 53.2\%]$; random-split baseline 0.18\%). Web-overlap contamination labels are near-independent of DIF flags (Jaccard $= 0.206$): the two constructs---global exposure and differential functioning---are empirically orthogonal. This instability does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals item-level temporal change, with 2024 models gaining on hard items while eroding on easy ones. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-23T07:55:09.447390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-23T07:55:09.899654+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal measurement instability} as the empirical phenomenon when DIF is detected across time-defined cohorts---a descriptive term denoting systematic changes in measurement properties, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.18\% under a random-split control. This instability does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings); it is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Existing approaches to benchmark integrity focus on \emph{global exposure}---whether items appear in training corpora---through membership inference~\citep{shi2024mink} and performance-based detection~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}, validated against web-overlap labels~\citep{li2024contamination}. Whether benchmark items function equivalently across model generations---\emph{measurement invariance}---has no
…[truncated 3213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-23T07:55:09.900195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-23T07:55:10.554246+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrat
…[truncated 4788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-23T07:55:10.906011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-23T07:55:10.956913+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 9746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-23T07:55:16.230482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-23T07:55:16.733046+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	As approximate parametric bounds, a Monte Carlo power analysis (1,000 replications per condition) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$; 14,042 MMLU items) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$ (details in \Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold. Power varies substantially with item discrimination: TPR ranges from 0.40 at $a = 0.5$ to 0.95 at $a = 2.0$; the gap between TPR at mean $a$ (0.87) and the aggregate TPR (0.68) quantifies the power cost of parameter heterogeneity, consistent with Jensen's inequality (\Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal Comparability: 31\% Measurement Instability}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%]; family-level cluster bootstrap CI $[26.7\%, 53.2\%]$). Two independent non-independence corrections converge on approximately 27--29\%: simple-mean DEFF correction (29.2\%) and family-level cluster bootstrap lower bound (26.7\%). The weighted-mean DEFF variant yields 13.5\%, a valid lower bound under the assumption that within-family members are interchangeable. We prefer the simple-mean estimate because 
…[truncated 11347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-23T07:55:16.783739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-23T07:55:17.236244+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage*{6\baselineskip}
4	
5	\subsection{Temporal DIF as Structured Signal}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---and this is by design. The signal is structured: stratifying by model type reveals opposite patterns---base models ($N{=}1{,}409$) are 60.1\% reference-favoring with a strong difficulty gradient ($\rho = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring with a near-zero gradient ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). This reversal cannot arise from a single mechanism, validating DIF as a meaningful diagnostic regardless of underlying cause. Detailed mechanism analysis---exclusion arguments, difficulty--direction interactions, and mixed-mechanism semi-synthetic validation---appears in \Cref{app:mechanism_discussion}.
10	
11	\looseness=-1
12	Item-level DIF matters even when aggregate rankings are preserved ($\rho \approx 0.997$): it reveals \emph{which} capability dimensions shift---diagnostic value that aggregate scores mask. DIF-ordered removal shows ranking degradation accelerates with instability (\Cref{app:fig_rho_degradation}); among the top 3.8\% most displaced models, 33.6\% of pairwise rankings reverse (\Cref{app:rank_reversal}).
13	
14	\looseness=-2
15	Within-family analysis validates matching: Llama-2 vs.\ Llama-3 raw C\% $= 61.3\%$ reflects the ability gap ($d = -0.99$); after nearest-neighbor matching, C\% drops to $28.3\%$, consistent with temporal matched C\% ($28.9\%$), confirming that DIF captures structured item-level change beyond ability differences.
16	
17	\subsection{Recommended DIF Audit Protocol}
18	\label{sec:disc_protocol}
19	
20	\looseness=-1
21	Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), precluding pre-screening. We recommend MH-DIF audits whenever ${\geq}$500 models accumulate ($K
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-23T07:55:17.236772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-23T07:55:17.889786+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-2
5	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal DIF across 2023--2024 model cohorts (${\approx}$27--29\% for MMLU), while aggregate rankings remain preserved ($\rho \approx 0.997$). Global exposure and differential functioning are empirically independent (Jaccard $= 0.206$)---complementary dimensions confirmed by the base-vs-instruct reversal ($\chi^2 = 562.7$). DIF detects \emph{what} changes without attributing \emph{why}---benchmarks need psychometric monitoring beyond score reporting.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-23T07:55:17.890137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-23T07:55:17.940626+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a worst-case injection model; reported $\Delta\mathrm{TPR}$ values are upper-bound estimates, and detection power under realistic contamination patterns (partial memorization, format-specific advantages) is untested. The framework detects measurement changes but does not attribute causal mechanisms; follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Three convergent corrections (${\approx}$27--29\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.069 when contamination spans ${\geq}20$ subjects. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to open-ended or partial-credit benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-23T07:55:34.970188+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen && pdfinfo artifacts/review_round_14/submitted.pdf 2>/dev/null | grep -i \"pages\" || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen && pdfinfo artifacts/review_round_14/submitted.pdf 2>/dev/null | grep -i \"pages\" || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-23T07:55:35.423592+00:00_

Pages:           17
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_director_870d8ac6

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-23T07:55:36.378267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-23T07:55:36.580043+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 5825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-23T07:55:36.580602+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-23T07:55:36.682212+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-23T07:56:01.137834+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool call

_source line 1289 · 2026-05-23T07:56:01.439948+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1290 · 2026-05-23T07:56:05.225508+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4087
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-23T07:56:05.226039+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3786
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-23T07:56:11.825563+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-23T07:56:11.976835+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 41\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 20:49 UTC\\n  summary: 'Dream analysis (dream_20260520T194223): 6 confirmed actions from cross-tier\\n    synthesis, 2 new experiments added (plan_010/011), framing qualified'\\n  rationale: 'Dream scores met thresholds (best=4/6, median=3.5/6, worst=3/6). Cross-tier\\n    analysis identified 6 confirmed issues (≥2 tiers): (1) contamination-capability\\n    confound → within-family analysis added to plan_001; (2) RL evidence underpower
…[truncated 1430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-23T07:56:54.865921+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **页数限制**: 正文 ≤ 8 页，参考文献无限制，Limitations 不计入页数\n- **模板**: ACL 格式（`\\usepackage[review]{acl}`）\n- **匿名规则**: double-blind\n- **附录**: 允许，不计入页数\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf`\n- 各章节在 `paper/sections/` 目录下\n\n### 你的审查侧重\n\n**核心任务：评估方法论严谨性、实验设计合理性、统计分析正确性。**\n\n请重点审查以下方面：\n\n1. **MH-DIF 方法应用**：\n   - MH procedure 在 LLM benchmark 场景下的适用性假设是否成立？\n   - Cross-subject matching 的 ΔFPR=0 claim 是否严谨？边界条件（k subjects）讨论是否充分？\n   - ETS C 分类的双阈值（效应量+显著性）在 N=5,227 下几乎自动满足显著性，这对结果的影响是否充分讨论？\n\n2. **DEFF 非独立性校正**：\n   - Simple-mean vs weighted-mean DEFF 的选择论证是否有说服力？\n   - 27-29% vs 13.5% 的范围呈现是否透明、合理？\n   - Family structure 的处理（graduated de-duplication、LOFO）是否充分？\n\n3. **Semi-synthetic 验证框架**：\n   - Binary response flipping 作为 injection model 的 ecological validity\n   - Dose-response 曲线的解释力\n   - Difficulty-dependent injection 的结果解读\n\n4. **控制实验和敏感性分析**：\n   - Random split, ability-quintile, matched-ability 控制是否充分排除替代解释？\n   - Temporal confound（2023 vs 2024 同时 confound architecture/training/capability）的处理\n   - Within-family (Llama-2 vs 3) 分析的逻辑\n\n5. **Cross-benchmark 复制**：\n   - 6 个 METABENCH benchmark 结果的一致性和差异性解释\n   - GSM1K 探索性分析的权重是否恰当\n\n6. **统计报告**：\n   - 置信区间、效应量、p值的报告是否完整规范？\n   - 多重比较问题的处理\n   - Bootstrap CI 的合理性\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3句概述论文）\n- **Strengths**（逐条，标注 S1, S2, ...）\n- **Weaknesses**（逐条，标注 W-M1 方法, W-E1 实验, W-S1 统计等，并标明 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度）\n\n评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计分析）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **页数限制**: 正文 ≤ 8 页，参考文献无限制，Limitations 不计入页数\n- **模板**: ACL 格式（`\\usepackage[review]{acl}`）\n- **匿名规则**: double-blind\n- **附录**: 允许，不计入页数\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf`\n- 各章节在 `paper/sections/` 目录下\n\n### 你的审查侧重\n\n**核心任务：评估方法论严谨性、实验设计合理性、统计分析正确性。**\n\n请重点审查以下方面：\n\n1. **MH-DIF 方法应用**：\n   - MH procedure 在 LLM benchmark 场景下的适用性假设是否成立？\n   - Cross-subject matching 的 ΔFPR=0 claim 是否严谨？边界条件（k subjects）讨论是否充分？\n   - ETS C 分类的双阈值（效应量+显著性）在 N=5,227 下几乎自动满足显著性，这对结果的影响是否充分讨论？\n\n2. **DEFF 非独立性校正**：\n   - Simple-mean vs weighted-mean DEFF 的选择论证是否有说服力？\n   - 27-29% vs 13.5% 的范围呈现是否透明、合理？\n   - Family structure 的处理（graduated de-duplication、LOFO）是否充分？\n\n3. **Semi-synthetic 验证框架**：\n   - Binary response flipping 作为 injection model 的 ecological validity\n   - Dose-response 曲线的解释力\n   - Difficulty-dependent injection 的结果解读\n\n4. **控制实验和敏感性分析**：\n   - Random split, ability-quintile, matched-ability 控制是否充分排除替代解释？\n   - Temporal confound（2023 vs 2024 同时 confound architecture/training/capability）的处理\n   - Within-family (Llama-2 vs 3) 分析的逻辑\n\n5. **Cross-benchmark 复制**：\n   - 6 个 METABENCH benchmark 结果的一致性和差异性解释\n   - GSM1K 探索性分析的权重是否恰当\n\n6. **统计报告**：\n   - 置信区间、效应量、p值的报告是否完整规范？\n   - 多重比较问题的处理\n   - Bootstrap CI 的合理性\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3句概述论文）\n- **Strengths**（逐条，标注 S1, S2, ...）\n- **Weaknesses**（逐条，标注 W-M1 方法, W-E1 实验, W-S1 统计等，并标明 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度）\n\n评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-23T07:57:15.795474+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20929
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-23T07:57:15.947955+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 叙事/Framing + 写作完整性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **页数限制**: 正文 ≤ 8 页，参考文献无限制，Limitations 不计入页数\n- **模板**: ACL 格式（`\\usepackage[review]{acl}`）\n- **匿名规则**: double-blind\n- **附录**: 允许，不计入页数\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf`\n- 各章节在 `paper/sections/` 目录下\n\n### 你的审查侧重\n\n**核心任务：评估论文新颖性、贡献定位、叙事逻辑、写作质量、格式合规性。**\n\n请重点审查以下方面：\n\n1. **新颖性和贡献定位**：\n   - 核心方法 MH-DIF 是 1988 年的标准教育测量方法，论文的\"新颖性\"体现在哪里？\n   - \"Global exposure vs differential functioning\" 二维框架是否足够新颖？\n   - 贡献定位为 \"methodological and empirical, not algorithmic\" 是否恰当？\n   - 与 Growing Pains (Habba et al. 2026) 的区分是否清晰、可信？\n\n2. **叙事和 Framing**：\n   - 从 Introduction 到 Conclusion 的论证线是否连贯？\n   - \"Temporal measurement instability\" 这个 framing 是否准确？DIF 检测到的是 instability 还是其他？\n   - DIF 无法区分 contamination / capability evolution / training shift —— 这个局限在论文中是否被充分承认？\n   - \"Benchmarks need psychometric monitoring, not just score reporting\" 这个结论是否被实验充分支持？\n\n3. **Related Work 完整性**：\n   - 是否有重要的遗漏？特别是：\n     - 最近的 benchmark contamination 检测工作\n     - IRT 在 NLP/LLM 评估中的应用\n     - DIF 方法论文献\n   - 与 concurrent work 的区分是否准确（Growing Pains, BHI, Benchmark², MMLU-CF, DVD, Self-Critique）\n\n4. **写作质量**：\n   - 术语一致性（measurement instability / temporal DIF / temporal comparability 是否混用）\n   - Abstract 是否准确概括全文？\n   - Conclusion 是否充分收束论证？（当前仅 3 句）\n   - 段落组织和信息密度是否合理？\n\n5. **格式合规性**（EMNLP 2026 / ARR 要求）：\n   - 正文是否控制在 8 页以内？\n   - 是否使用了激进的 `\\enlargethispage` 或负 `\\vspace` 来压缩？\n   - Limitations 是否在 References 之前、独立成节？\n   - 匿名合规：是否有 self-citation 泄露？\n   - 图表是否清晰、必要、有说明文字？\n\n6. **Limitations 充分性**：\n   - 3 个局限是否覆盖了关键弱点？\n   - 是否遗漏了重要局限？\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3句概述论文）\n- **Strengths**（逐条，标注 S1, S2, ...）\n- **Weaknesses**（逐条，标注 W-N1 新颖性, W-F1 framing, W-W1 写作, W-C1 格式等，并标明 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度）\n\n评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "irt_equated_bench_regen",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 叙事/Framing + 写作完整性）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ACL Rolling Review 投稿）\n- **页数限制**: 正文 ≤ 8 页，参考文献无限制，Limitations 不计入页数\n- **模板**: ACL 格式（`\\usepackage[review]{acl}`）\n- **匿名规则**: double-blind\n- **附录**: 允许，不计入页数\n\n### 论文文件\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_14/submitted.pdf`\n- 各章节在 `paper/sections/` 目录下\n\n### 你的审查侧重\n\n**核心任务：评估论文新颖性、贡献定位、叙事逻辑、写作质量、格式合规性。**\n\n请重点审查以下方面：\n\n1. **新颖性和贡献定位**：\n   - 核心方法 MH-DIF 是 1988 年的标准教育测量方法，论文的\"新颖性\"体现在哪里？\n   - \"Global exposure vs differential functioning\" 二维框架是否足够新颖？\n   - 贡献定位为 \"methodological and empirical, not algorithmic\" 是否恰当？\n   - 与 Growing Pains (Habba et al. 2026) 的区分是否清晰、可信？\n\n2. **叙事和 Framing**：\n   - 从 Introduction 到 Conclusion 的论证线是否连贯？\n   - \"Temporal measurement instability\" 这个 framing 是否准确？DIF 检测到的是 instability 还是其他？\n   - DIF 无法区分 contamination / capability evolution / training shift —— 这个局限在论文中是否被充分承认？\n   - \"Benchmarks need psychometric monitoring, not just score reporting\" 这个结论是否被实验充分支持？\n\n3. **Related Work 完整性**：\n   - 是否有重要的遗漏？特别是：\n     - 最近的 benchmark contamination 检测工作\n     - IRT 在 NLP/LLM 评估中的应用\n     - DIF 方法论文献\n   - 与 concurrent work 的区分是否准确（Growing Pains, BHI, Benchmark², MMLU-CF, DVD, Self-Critique）\n\n4. **写作质量**：\n   - 术语一致性（measurement instability / temporal DIF / temporal comparability 是否混用）\n   - Abstract 是否准确概括全文？\n   - Conclusion 是否充分收束论证？（当前仅 3 句）\n   - 段落组织和信息密度是否合理？\n\n5. **格式合规性**（EMNLP 2026 / ARR 要求）：\n   - 正文是否控制在 8 页以内？\n   - 是否使用了激进的 `\\enlargethispage` 或负 `\\vspace` 来压缩？\n   - Limitations 是否在 References 之前、独立成节？\n   - 匿名合规：是否有 self-citation 泄露？\n   - 图表是否清晰、必要、有说明文字？\n\n6. **Limitations 充分性**：\n   - 3 个局限是否覆盖了关键弱点？\n   - 是否遗漏了重要局限？\n\n请按以下格式输出审稿意见：\n- **Summary**（2-3句概述论文）\n- **Strengths**（逐条，标注 S1, S2, ...）\n- **Weaknesses**（逐条，标注 W-N1 新颖性, W-F1 framing, W-W1 写作, W-C1 格式等，并标明 Must-Fix / Should-Fix / Minor）\n- **Questions**（需要作者澄清的问题）\n- **Missing References**（遗漏的重要相关工作）\n- **Overall Assessment**（评分 + 置信度）\n\n评分标准（ARR/EMNLP 2026）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-23T07:57:17.914825+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1966
}
```

</details>

---


### Assistant

_source line 1298 · 2026-05-23T07:57:27.197300+00:00_

**Round 1 审稿已启动。**

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性 + 实验设计 + 统计分析 | ⏳ 审稿中 |
| Reviewer 2 | 新颖性 + 叙事/Framing + 写作完整性 | ⏳ 审稿中 |
| 视觉审查 Agent | PDF 排版/布局检查 | ⏳ 进行中 |
| 外部审稿 | 未启用 | — |

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 125

## Round 125

2 recorded events


### User

_source line 1299 · 2026-05-23T08:02:56.820492+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — Round 1

**论文**：Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models

---

### Summary

本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU items）上发现约 27-29%（经非独立性校正后）的 items 在 2023 vs 2024 模型 cohort 间表现出显著的时序 DIF。论文进一步证明 DIF 标记与 web-overlap 污染标签在统计上正交（Jaccard ≈ 0.206，κ = 0.012），并通过 semi-synthetic 注入框架验证了 MH-DIF 的检测能力。论文将发现定位为「测量不稳定性」而非「污染检测」，提出 DIF 审计作为基准评测的心理测量学预筛工具。

---

### Strengths

**S1. 规模与系统性**：5,227 模型 × 12,508 items 的全矩阵分析在 LLM 评测领域属罕见规模。五种 cohort 设计（temporal、ability-quintile、matched-ability、within-family、random split）构成了严谨的控制体系（Table 1, Table 2）。

**S2. 非独立性校正框架扎实**：认识到 LLM model families 违反独立性假设并提出 DEFF 校正是重要的方法论贡献。同时提供 simple-mean DEFF 和 family-level cluster bootstrap 两个独立校正路径，且两者收敛于相近区间（26.7%-29.2%），增强了结果可信度（Section 4.2, Appendix E）。

**S3. Cross-subject matching 的 FPR 保证**：Section 3.4 对单科目污染场景下 ΔFPR = 0 的构造性证明是精巧的——用不同 benchmark 的总分作为 matching variable 从根本上隔离了被测科目的污染信号。这一设计在 LLM 评测中具有独立价值。

**S4. DIF 与 web-overlap 的正交性发现**：κ = 0.012、OR = 1.05、Jaccard 在 permutation null 区间内（Section 4.3），统计支撑充分。这一发现对理解 benchmark 质量问题的多维性具有概念性贡献——global exposure 和 differential functioning 确实捕捉了不同现象。

**S5. 跨 benchmark 复制**：六个 METABENCH benchmark 均表现出时序 DIF（Table 3），增强了结论的普适性。GSM8K 的探索性分析（Section 4.7, Appendix F）恰当地标注为描述性分析。

**S6. 下游影响分析有实践价值**：Figure 4 展示 DIF-ordered 移除对模型排名的影响（flip rate 33.6%），Table 2 的 matched-ability 控制（C% = 28.35%）排除了纯能力差异解释，这些分析将方法论发现与实际评测决策相连接。

**S7. 机制分析（Appendix B）虽为探索性但有深度**：排除论证、difficulty-direction interaction、mixed-injection 分析展示了认真的因果推理尝试，即使最终未能完全区分机制。

---

### Weaknesses

**W-M1 [Must-Fix] 时序混淆是论文最大的解释性缺口**

- **位置**：Section 5.1, Section 3.3, Appendix B
- **问题**：2023 vs 2024 model cohort 在架构（Transformer variants）、训练范式（SFT/RLHF/DPO 演进）、数据规模、能力水平上同时变化。论文将 DIF 定义为「items function differently across cohorts」（Section 5.1），但在 LLM 场景下，不同代模型对不同 item 类型展现不同能力 profile 是 **预期行为**——这与教育测量中同一课程体系下不同人群的 DIF（预期为零）有本质区别。
- **具体地说**：Section 5.1 报告 base models 在难题上提升（ρ = −0.570）而 instruct models 在易题上提升（ρ near-zero gradient），但这可能完全反映了合法的训练方法论进步（如 RLHF 对易题的 ceiling effect 提升），而非测量的不稳定性。论文的 Appendix B 排除分析列出三种机制但承认无法区分。
- **为什么影响接收**：核心 claim「27-29% of items exhibit temporal measurement instability」的可解释性取决于是否能将 legitimate capability evolution 与 genuine measurement dysfunction 区分开。如果无法区分，DIF rate 作为 benchmark 质量指标的实践价值存疑。
- **建议**：(a) 明确讨论「在 LLM 场景下什么样的 DIF 是预期的、可接受的」——可以借鉴 Camilli and Shepard (1994) 对 impact vs bias 的区分；(b) 考虑引入 item-level covariates（如 item difficulty, discrimination, subject domain）作为 DIF 的解释变量，区分可解释的 DIF（由 item 特征预测）和残余 DIF；(c) 更审慎地限定 claim——将「measurement instability」改为「differential item functioning across model generations」，让读者自行判断这是否构成 instability。

**W-M2 [Should-Fix] DEFF 估计范围过宽，首选估计的论证不够充分**

- **位置**：Section 4.2, Appendix E
- **问题**：Simple-mean DEFF（n̄ = 62.8）给出调整后 C% = 29.2%，weighted-mean DEFF（n̄ reflecting effective cluster size）给出 C% = 13.5%。两者相差 2 倍以上。论文以「within-family similarity is flat across family sizes (r_s = −0.03)」为由偏好 simple-mean，但这一论证存在逻辑缺口：
  - r_s = −0.03 说明 ICC 不随 family size 变化，但这不意味着应该用 simple-mean。在 survey methodology 中，当 clusters 大小不等时，weighted-mean 更能反映随机抽取一个 unit 所经历的实际 design effect（Kish, 1965）。
  - 更关键的是，论文的 50 个 families 中大 families（Llama-3 n=308, Mistral n=547 等）贡献了大部分 models。一个从 5,227 models 中随机抽取的 model 更可能来自大 family，因此 weighted-mean 可能更合适。
- **为什么影响评分**：13.5% vs 29.2% 的差距直接影响读者对 benchmark 质量问题严重程度的判断。
- **建议**：(a) 展示 DEFF 敏感性分析（如移除最大 2-3 个 families 后的变化）；(b) 在正文中并列呈现两个估计，而非将 13.5% 降级为 footnote-level 的「lower bound」；(c) 讨论在什么条件下各估计更合适。

**W-M3 [Should-Fix] Semi-synthetic 注入模型的生态效度有限**

- **位置**：Section 3.4, Section 4.5, Figure 2
- **问题**：Binary response flipping（以 exploitation rate p 随机翻转正确答案为错误）是对真实污染的粗糙近似。真实污染通过 memorization 表现——模型在 seen items 上的正确率系统性提升，而非随机翻转。这意味着：
  - 真实污染产生的 DIF pattern 是单向的（只提升正确率），而 random flipping 是双向的
  - 真实污染与 item difficulty 相关（易题 ceiling effect 限制了提升空间），而 uniform flipping 忽略了这一点
  - Difficulty-dependent injection（Appendix B, Scheme D）部分解决了这个问题，但仍是 injection 而非 memorization
- **论文在 Limitations 中承认了这一点**，但 Section 4.5 标题「Semi-Synthetic Framework Validation」暗示了比实际更强的验证。
- **建议**：(a) 将 Section 4.5 定位为「detection power under a simplified injection model」而非 framework validation；(b) 讨论 monotonic injection（只允许 0→1 翻转）的结果是否不同；(c) 引用或讨论更现实的 contamination simulation 方法（如基于 n-gram overlap 的注入）。

**W-E1 [Should-Fix] ETS C 分类阈值在 N=5,227 下的适用性未讨论**

- **位置**：Section 3.2
- **问题**：ETS C 分类要求 |Δ_MH| ≥ 1.5 **且** p < 0.05。论文正确指出在 N=5,227 下显著性几乎自动满足（Section 3.2: "statistical significance (p < 0.05) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5"），这意味着分类实质上仅由效应量驱动。但 |Δ_MH| ≥ 1.5 这一阈值来自教育测量（通常 N 在数百到数千范围），在 N=5,227 的 LLM 场景下是否仍然合适？
  - 较大的 N 意味着更精确的 Δ_MH 估计，从而更多 items 可能恰好越过阈值
  - 论文虽然用了 DEFF 校正来调整 N，但 DEFF 校正的是 χ² 统计量而非效应量估计本身
- **建议**：讨论 |Δ_MH| ≥ 1.5 在不同 N 下的含义是否一致，或考虑使用 bootstrapped 效应量 CI 是否包含 0 作为替代判据。

**W-E2 [Should-Fix] Within-family 分析的 generalizability**

- **位置**：Section 4.4 (倒数第二段), Table 2
- **问题**：Within-family 分析主要依赖 Llama-2 vs Llama-3（N=161 vs N=308）和 Mistral 系列。但这两个 family 的代际变化特别大（Llama-2→3 涉及训练数据扩大 7 倍 + 架构改进）。用这样大跨度的代际变化来论证「DIF captures structured item-level change beyond ability differences」可能过度推断——在更小代际差异的 family 内（如 Llama-3 → Llama-3.1），DIF 信号是否仍然存在？
- **建议**：如 METABENCH 中有更细粒度的代际变化（如 Llama-3 → Llama-3.1 → Llama-3.2），展示 within-family DIF 随代际距离的变化趋势。

**W-S1 [Should-Fix] 关键统计量缺少不确定性度量**

- **位置**：全文多处
- **问题**：
  - DEFF 估计（3.87 和 12.79）未报告 CI 或标准误——这些是关键的校正参数
  - Appendix E Table 9 报告了 tier-stratified DEFF 但缺少 tier 之间的统计检验
  - Jaccard = 0.206 报告了 permutation null 区间但未报告 bootstrap CI
  - 机制分析（Appendix B）中的 logistic regression OR（如 OR = 1.73 for difficulty-model-type interaction）未报告 CI
- **建议**：为 DEFF、Jaccard、以及 Appendix B 的 OR 添加 95% CI。

**W-S2 [Minor] 多重比较处理的透明度**

- **位置**：Section 4.2, Appendix A.2
- **问题**：论文提到使用 BH correction（Section 4.2），但 Appendix A.2 的 random-split sanity check 使用了「α_rf = 0.05」且未提到多重比较校正。此外，Appendix B 的 logistic regression 报告了多个 p 值但未明确是否经过校正。应在一处统一说明多重比较策略。
- **建议**：在 Method 或 Appendix 中添加一段统一说明所有 p 值的多重比较处理方式。

**W-M4 [Minor] 「Measurement instability」概念的操作化定义不够明确**

- **位置**：Title, Abstract, Section 5.1
- **问题**：论文标题使用「temporal measurement instability」，但 Section 5.1 又说「DIF detects that items function differently across cohorts, not why」。在教育测量中，measurement invariance 有明确的操作化定义（如 IRT 参数跨组等价）。论文实际检测的是 MH-DIF（一种 observed-score 方法），但用了「measurement instability」这一更强的概念标签。MH-DIF 检测到的可能是 item-level functioning 差异而非真正的 measurement property 退化。
- **建议**：在 Section 3 开头明确定义本文中「measurement instability」的操作化含义=「statistically significant and practically meaningful DIF as classified by ETS C criteria」。

---

### Questions for Authors

**Q1**：在 matched-ability 控制中（Table 2, C% = 28.35%），如何确保 matching 的质量？Matching 是 exact matching 还是 propensity score matching？剩余的能力差异有多大？

**Q2**：论文报告 Jaccard = 0.206 在 permutation null (0.203, 0.222] 内（Section 4.3），但 Table 1 的 Enrichment 列显示 temporal DIF 的 enrichment ratio = 1.0。如果 web-overlap items 中有部分确实受到污染并导致 DIF，这个信号是否被 73.8% 的非 web-overlap coverage 稀释了？

**Q3**：DEFF 校正后 C% 从 31.3% 降至 29.2%（simple-mean）——降幅只有 2 个百分点。这是否说明 family structure 对 DIF 检测的实际影响很小？如果是这样，为什么 weighted-mean 给出的 13.5% 差异如此大？

**Q4**：Appendix H 的 item-property predictive analysis 使用了 17 个 features 做 logistic regression/LightGBM，ROC = 0.603/0.039。这个接近 chance 的预测能力意味着 DIF 标记几乎不可预测——这是支持还是反对 DIF 作为 measurement quality indicator 的论点？

**Q5**：Cross-benchmark validation（Table 3）显示不同 benchmark 的 temporal C% 差异较大（MMLU 31.3% vs HellaSwag 17.9%）。这种差异是否与 benchmark 的 item 特征（如 item format, difficulty distribution）系统性相关？

---

### Missing References

1. **Camilli, G., & Shepard, L. A. (1994). Methods for Identifying Biased Test Items.** — 这是 DIF 领域的经典教科书，区分了 impact（合法能力差异）和 bias（测量偏差），对本文的解释框架直接相关。论文引用了 Holland & Thayer (1988) 等早期工作但遗漏了这一关键理论基础。

2. **Penfield, R. D., & Camilli, G. (2007). Differential item functioning and item bias.** In Handbook of Statistics. — 系统综述 DIF 方法论，包括 MH 方法的局限性讨论。论文引了 Penfield and Camilli (2007) 于 page 3（作为 comprehensive review），但如果确实引用了则此条取消。

3. **Wainer, H. (1993). Differential Testlet Functioning.** — 讨论了 testlet（item bundle）对 DIF 检测的影响，与本文的 family structure（model clusters）问题有类似的非独立性挑战。

4. **Suk, Y., & Wiejon, Y. (2026). Rethinking differential item functioning from a causal inference perspective.** — 论文引用列表第 11 页显示已引用此文（"Forthcoming"），确认已包含。

---

### Overall Assessment

**Overall**: **3.5 — Borderline Conference**

**一句话总结**：方法论框架扎实、规模令人印象深刻，但时序混淆的不可解性和 DEFF 估计的宽范围削弱了核心 claim 的可解释性和实践价值。

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | MH-DIF 应用正确，DEFF 校正和 cross-subject matching 设计精巧，但时序混淆未解决，DEFF 范围（13.5-29.2%）过宽 |
| Excitement | 3.5/5 | 将心理测量学方法引入 LLM 评测的方向有价值，DIF-contamination 正交性发现 novel，但实践 actionability 受限 |
| Reproducibility | 4/5 | 数据来自公开的 METABENCH，分析代码注释可用（footnote 1），方法描述详细 |
| Reviewer Confidence | 4/5 | 熟悉 DIF 方法论和 LLM 评测文献，对 survey sampling（DEFF）的细节理解一般 |

**评分依据**：论文在方法论上达到了 conference 水准（S1-S3 的系统性、S4 的正交性发现、S5 的跨 benchmark 复制），但 W-M1（时序混淆）是影响核心 claim 可解释性的根本问题。如果作者能更审慎地限定 claim（从 "measurement instability" 退到 "temporal DIF"），并更透明地处理 DEFF 估计范围（W-M2），论文可以达到 4 (Conference)。当前状态介于 Conference 和 Findings 之间。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1300 · 2026-05-23T08:03:03.383917+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 126

## Round 126

2 recorded events


### User

_source line 1301 · 2026-05-23T08:03:08.246178+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference）。

核心判断：
- **方法论框架扎实**——MH-DIF 应用正确，DEFF 校正和 cross-subject matching 是有独立价值的贡献
- **最大问题是时序混淆（W-M1）**——2023→2024 cohort 变化太多（架构/训练/数据/能力），无法区分 legitimate capability evolution 和 genuine measurement instability
- **DEFF 估计范围过宽（W-M2）**——simple-mean 给出 29.2%、weighted-mean 给出 13.5%，2 倍差距下论文偏好高估值的论证不充分
- **Semi-synthetic 注入模型生态效度有限（W-M3）**——random flipping ≠ memorization-based contamination

提出了 5 个需要作者澄清的问题和 3 条潜在遗漏引用。如果作者能审慎限定 claim 并更透明处理 DEFF 范围，论文可达 Conference (4.0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1302 · 2026-05-23T08:03:14.924236+00:00_

Reviewer 1 审稿已收到（3.5 Borderline Conference）。等待 Reviewer 2 审稿完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 127

## Round 127

6 recorded events


### User

_source line 1303 · 2026-05-23T08:04:54.758561+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1（新颖性 / 叙事Framing / 写作完整性）

---

### Summary

本文将教育测量领域的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测，在 METABENCH 数据集上（5,227 模型 × 12,508 MMLU 题目）检测 2023 vs 2024 模型群组间的 temporal measurement instability。核心发现：~27–29% 的 MMLU 题目在校正非独立性后展现大幅 temporal DIF；web-overlap 污染标签与 DIF 标记近乎正交（Jaccard = 0.206）；聚合排名保持稳定（ρ ≈ 0.997）。论文还提出了 cross-subject matching 的半合成验证框架，并在全部六个 METABENCH 基准上进行了复现。

---

### Strengths

**S1: 分析规模和严谨性令人印象深刻。** 5,227 个模型 × 12,508 题目是目前已知最大规模的 DIF 分析。鲁棒性检验极其全面：random-split 对照（0.18%）、ability-matched quintile、nearest-neighbor matching（Cohen's d = −0.17）、family-level cluster bootstrap、DEFF 校正（简单均值 vs 加权均值）、graduated de-duplication、cross-benchmark 复现。这种验证密度在该领域论文中罕见。

**S2: Global exposure vs. differential functioning 二维框架有实际价值。** 将 web-overlap 标签（global exposure）与 DIF 标记（differential functioning）区分开来是一个清晰且有用的概念贡献。正交性的实证证据（Jaccard = 0.206, enrichment = 0.964, φ = 0.012）充分且可信。Figure 1 的示意图有效传达了这一区分。

**S3: 半合成验证框架设计良好。** Cross-subject matching 保证 ΔFPR = 0（单科目污染下）的理论分析简洁优雅，经验验证（5 个 MMLU domain 全部 ΔFPR = 0.000）令人信服。Figure 2 的剂量-反应曲线清楚展示了检测灵敏度。多科目污染下的 graceful degradation 分析（Table 7 in Appendix）也很完整。

**S4: 六个基准的跨基准复现增强了可信度。** Table 3 展示了 17.9%–31.3% 的一致 DIF 模式，知识/推理类基准（MMLU 31.3%, WinoGrande 30.3%）高于程序类基准（GSM8K 18.9%, HellaSwag 17.9%），pattern 合理。

**S5: base-vs-instruct 反转是论文最有洞察力的发现。** Section 5.1 展示 base 模型 60.1% reference-favoring（难题上改善）而 instruct 模型 65.6% focal-favoring（χ² = 562.7），且 difficulty gradient 方向相反（ρ = −0.570 vs −0.079）。这一发现有力证明 DIF 信号具有结构性，不是随机噪声。

**S6: 诚实展示局限性。** 论文坦承 DIF 无法归因（"detects what, not why"），对非独立性问题提供了多种校正估计（13.5%–29.2%），Limitations section 覆盖了关键弱点。

---

### Must-Fix 问题（影响接收决定）

**W-F1 [critical]: "Temporal measurement instability" 的 framing 存在根本性张力**
- 具体位置：Abstract, Section 1 (定义), Section 4.2 标题, Section 5.1, Conclusion
- 问题：论文将 DIF 现象定义为 "temporal measurement instability"（Section 1: "a descriptive term denoting systematic changes in measurement properties, without implying degradation or attributing cause"）。但 "instability" 一词本身携带负面含义——暗示基准测试本身存在缺陷。然而论文同时展示了：(a) 聚合排名几乎不受影响（ρ ≈ 0.997）；(b) DIF-flagged 题目集中了最高的区分度信号（z = −8 to −49 vs random removal, Section 4.6）；(c) DIF 可能反映的是真实能力演化而非测量缺陷（Appendix B 明确承认）。如果 DIF 反映的是真实的 capability evolution，那么所谓的 "instability" 恰恰是基准测试在忠实地测量不断演化的能力——这是测量 *正常工作* 的表现，不是 "instability"。
- 为什么影响接收：这不仅是术语问题，而是影响论文核心叙事的逻辑一致性。如果 DIF ≠ instability（在 capability evolution 场景下），则标题、Abstract 的最后一句、Conclusion 的核心结论都需要重新定位。
- 建议修改方向：(1) 将 "instability" 替换为更中性的术语如 "temporal differential item functioning" 或 "temporal measurement shift"；(2) 或者在 Introduction 中更强力地论证为什么即使 DIF 来源于 capability evolution，它仍然构成 "instability"（例如：因为它意味着跨时间的分数不可直接比较）。

**W-F2 [critical]: DIF 无法区分 contamination / capability evolution / composition shift——这严重限制了实践含义，但论文的讨论不够充分**
- 具体位置：Section 5.1, Section 5.2, Conclusion, Appendix B
- 问题：论文承认 DIF "detects what changes without attributing why"（Conclusion），但随后直接跳到了规范性建议："benchmarks need psychometric monitoring, not just score reporting"（Abstract 最后一句，Conclusion 最后一句）。这个跳跃缺乏逻辑支撑。如果 DIF 的机制不明：
  - 若是 contamination → 应移除 flagged 题目
  - 若是 capability evolution → flagged 题目恰恰是最有信息量的，移除它们会 *损害* 基准质量
  - 若是 population composition shift（2023 vs 2024 cohort 中 base/instruct 模型比例不同）→ 问题在于 cohort 定义，不在题目
  
  Section 5.2 推荐 "MH-DIF audits whenever ≥500 models accumulate" 并以 ρ-degradation 校准 action level，但没有讨论在不同机制假设下这些 action 的后果截然不同。Appendix B 的 mechanism analysis 提供了有价值的约束，但明确无法解决这一歧义（"Observational DIF alone cannot separate these mechanisms"）。
- 为什么影响接收：论文的实践建议（psychometric monitoring + DIF audit protocol）的有效性取决于对 DIF 来源的假设，而论文无法验证这些假设。这使得论文从 "有意义的诊断发现" 滑向了 "无法行动的描述性分析"。
- 建议修改方向：(1) 在 Section 5.2 中按不同机制场景分别讨论 DIF audit 的行动含义；(2) 在 Conclusion 中将 "benchmarks need psychometric monitoring" 弱化为条件性陈述；(3) 更明确地将贡献定位为 "diagnostic tool" 而非 "actionable protocol"。

**W-C1 [critical]: \enlargethispage 使用过于激进，可能实质性违反 8 页限制**
- 具体位置：experiments.tex line 46 (`\enlargethispage*{4\baselineskip}`), discussion.tex line 3 (`\enlargethispage*{6\baselineskip}`)
- 问题：两处 \enlargethispage 共增加了约 10 个 \baselineskip 的额外空间（约 10 行文本）。特别是 `6\baselineskip` 极为激进——几乎等于多塞入了半栏内容。从 PDF 可以观察到 page 8 异常密集，包含了 Section 4.7 + Table 3 + Section 5（两个小节）+ Section 6 Conclusion。没有这些 \enlargethispage，正文几乎确定会溢出到第 9 页。此外，论文还使用了 15 处 `\looseness=-1` 或 `\looseness=-2` 进行段落压缩。
- 为什么影响接收：ARR/EMNLP 审稿人和 AC 通常将激进的 \enlargethispage 视为变相违反页数限制。虽然 ACL 格式没有明确禁止此命令，但 6\baselineskip 的程度远超正常排版调整的范围，可能触发格式审查。
- 建议修改方向：(1) 将 Conclusion 扩展到独立的新内容（目前仅 4 句话），同时压缩 Section 4 的重复性描述（例如 Section 4.2 中多种校正方法的详细列举可移入 Appendix）；(2) 将 \enlargethispage 控制在 ≤2\baselineskip 以内。

---

### Should-Fix 问题（影响评分但不一票否决）

**W-N1 [warning]: 核心方法是 1988 年的标准 MH-DIF，方法论新颖性有限**
- 具体位置：Section 2 (Related Work), Section 3 (Method)
- 问题：论文明确承认 "We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals"（Section 2）。Cross-subject matching 是 purified subtest matching（Swaminathan and Rogers, 1990）的改编。贡献定位为 "methodological and empirical, not algorithmic"（Section 1），但 "methodological" 这个词有些高估——实际上是 "application of existing methodology to a new domain"。
- 建议：(1) 更坦诚地将贡献定位为 "application + large-scale empirical analysis"；(2) 更强调 LLM-specific 的适配挑战（Section 3 的 "LLM-specific challenges" 段落已部分做到这一点，但可以更突出）。

**W-N2 [warning]: "两个维度" 框架的新颖性被高估——正交性可能是 *预期* 结果而非 *发现***
- 具体位置：Section 1 Contribution 1, Section 4.3
- 问题：Web-overlap 标签测量数据是否出现在训练语料中（global, 与模型无关），DIF 测量题目在不同群组间是否表现不同（differential, 与模型相关）。这两者测量的是概念上不同的东西。如果污染是全局性的（所有模型都接触到了），它不会产生 differential functioning——因此正交性是 *概念上预期的*，而非令人惊讶的实证发现。论文没有充分讨论为什么 Jaccard = 0.206 的正交性结果是 surprising 或 informative。
- 建议：论证清楚：是否存在一种合理的先验预期认为 DIF 和 web-overlap 应该相关？如果有（例如，如果部分模型接触了部分题目，即 differential exposure），那正交性结果就是有信息量的。如果没有，这个 "贡献" 就需要重新定位。

**W-F3 [warning]: 缺少 base-vs-instruct composition shift 的直接控制**
- 具体位置：Section 4.2, Section 5.1
- 问题：2023 和 2024 cohort 中 base/instruct 模型的比例很可能不同（论文未报告）。Section 5.1 展示 base 和 instruct 模型产生相反的 DIF pattern。如果 2024 cohort 中 instruct 模型占比更高，则部分 "temporal DIF" 可能只是 composition artifact——模型群体构成变了，不是题目的测量属性变了。论文做了 ability matching（nearest-neighbor, Cohen's d = −0.17），但没有做 model-type-stratified temporal DIF（即：仅在 base 模型中比较 2023 vs 2024，仅在 instruct 模型中比较 2023 vs 2024）。
- 建议：补充 model-type-stratified temporal DIF 分析。如果 within-base 和 within-instruct 的 temporal DIF 率仍然显著高于 random baseline，则 composition shift 不是主要驱动因素。这个分析对论文的 framing 至关重要。

**W-W1 [warning]: 术语不一致造成阅读障碍**
- 具体位置：全文
- 问题：论文交替使用 "measurement instability", "temporal DIF", "temporal comparability", "measurement invariance", "measurement shift" 等术语。虽然 Section 1 提供了定义，但在不同章节中的切换增加了不必要的认知负担。例如：Section 4.2 标题用 "Temporal Comparability: 31% Measurement Instability" 同时包含两个术语。
- 建议：选择一个核心术语并在全文一致使用，其他术语在首次出现时定义后不再交替。

**W-W2 [warning]: Conclusion 过于简短，未充分收束论证**
- 具体位置：Section 6（仅 4 句话，含 \looseness=-2）
- 问题：对于一篇包含 6 个基准、5,227 个模型、多项鲁棒性检验的大规模实证论文，Conclusion 仅重述了 Abstract 的核心数字，没有讨论：(1) 社区应如何将 DIF audit 纳入基准管理流程；(2) DIF 结果对正在进行的基准设计改革（MMLU-Pro, BHI 等）的具体启示；(3) 明确的 future work 方向。
- 建议：将 Conclusion 扩展到至少 2 段，涵盖 practical implications 和 future directions。这也有助于缓解 W-C1 的页面压力问题（如果将部分 Section 4 细节移入 Appendix）。

**W-W3 [warning]: Abstract 信息密度过高，数字缺乏上下文**
- 具体位置：Abstract
- 问题：Abstract 在第一遍阅读时几乎无法消化——密集堆叠了 27–29%, 13.5%, [26.7%, 53.2%], 0.18%, Jaccard = 0.206, φ = 0.012, ρ ≈ 0.997 等数字。读者在没有方法论背景的情况下无法理解这些数字的含义。"conservative bound: 13.5%; cluster bootstrap 95% CI [26.7%, 53.2%]" 对非 psychometrics 读者来说像噪音。
- 建议：保留 2-3 个关键数字（DIF 率、正交性、排名保持），将校正方法细节留给正文。

---

### 小问题（不影响接收）

- **Minor-1**: Section 4.2 中 "cluster bootstrap 95% CI [26.7%, 53.2%]" 的上界 53.2% 极宽，与下界 26.7% 差距巨大。虽然 Appendix E 解释了这是由 Mistral/Llama-3 over-representation 导致的极端 bootstrap resample，但正文中应简要注释这一点。
- **Minor-2**: Figure 1 的示意图清晰有效，但 "global contamination produces no DIF" 的标题略有误导——如果 global contamination 导致 ceiling effect（所有模型都答对），DIF 不会被检测到，但题目的测量属性已经改变了。
- **Minor-3**: Section 3.2 中 "LLM-specific challenges" 段落的第四点（multidimensionality）给出了三条证据线，但第 (ii) 条中 "20% discordance is distributed across domains" 的 "20%" 缺乏具体定义——是 within-subject 和 cross-subject matching 的 disagreement 率吗？
- **Minor-4**: Appendix H (Item-Property Predictive Analysis) 中 AUROC = 0.603 被描述为 "near chance"，但 chance AUROC = 0.5，0.603 虽然不高但也不完全是 chance level。更准确的表述是 "weak predictive power"。

---

### Questions（需要作者澄清）

**Q1**: 2023 和 2024 temporal cohort 中 base/instruct 模型的比例各是多少？是否做过 model-type-stratified temporal DIF（仅在 base 模型内或仅在 instruct 模型内比较 2023 vs 2024）？

**Q2**: Section 5.1 报告 base 模型 N=1,409、instruct 模型 N=478，但 temporal cohort 总共只有 N=1,887（1,080 + 807）。这些 N=1,409 和 N=478 的数字来自哪里？是全部 5,227 模型还是仅 temporal cohort 的子集？

**Q3**: 论文声称 "no prior work applies DIF to benchmark temporal comparability"（Section 2）。但 Maeda (2025) 的工作（论文中引用为 maeda2025difllm）是否属于将 DIF 应用于 LLM 评估的先例？两者的区别是什么？

**Q4**: Growing Pains (Habba et al., 2026) 的 anchor items 和本文的 stable items（non-DIF items）之间有多少重叠？如果两种方法识别出的 "可靠题目" 高度一致，这会增强两篇论文的可信度；如果不一致，需要解释原因。

**Q5**: 论文推荐的 DIF audit protocol（Section 5.2）中，当 flagged 题目被标记后，具体应该采取什么行动？是移除、降权、还是仅报告？不同行动在不同 DIF 机制假设下的后果如何？

---

### Missing References

本文的 Related Work 覆盖面已经相当广泛，以下是可能的补充：

1. **Population composition 在 DIF 分析中的影响**：如果存在关于 DIF 分析中 focal/reference group composition 如何影响结果的方法论文献，应予引用以支撑 W-F3 的讨论。
2. **LLM evaluation 中的 fairness-oriented DIF**：是否有将 DIF 用于检测 LLM 评估中 demographic/task bias 的工作？这与本文的 temporal DIF 应用不同但相关。
3. **Concurrent work Suk and Weiss (2026)** 被引用但仅一句带过。作为 "rethinking DIF from a causal inference perspective" 的工作，它与本文的 "DIF cannot attribute cause" 限制直接相关，值得更详细的讨论。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | MH-DIF 应用方法学上正确；鲁棒性检验全面。但 "temporal measurement instability" framing 与实际发现存在张力；无法区分机制限制了实践含义；composition shift 缺乏直接控制。 |
| Excitement | 3/5 | 话题及时重要（LLM benchmark 质量是社区关注焦点），但核心贡献是将 1988 年的标准方法应用于新领域 + 大规模描述性分析。正交性发现有价值但可能是预期结果。 |
| Reproducibility | 4/5 | 代码已匿名公开；METABENCH 数据公开可用；方法描述详尽。半合成框架有清晰的伪代码级描述。 |
| Clarity | 3.5/5 | 整体写作质量高，但术语不一致、Abstract 过密、Conclusion 过简。Method section 对非 psychometrics 背景的 NLP 读者可能门槛较高。 |
| Reviewer Confidence | 4/5 | 我对 DIF 方法论和 LLM 评估领域有较好的了解，仔细阅读了全文和附录。 |

---

### Overall Assessment

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 大规模、严谨的实证分析展示了 LLM 基准中存在显著的 temporal DIF，但核心方法缺乏算法新颖性，且 "measurement instability" 的 framing 与 DIF 无法归因机制的根本限制之间存在未解决的张力——论文需要更诚实地面对 "DIF 检测到了变化，但我们不知道这意味着什么" 的现实。

**接收理由**: (1) 规模空前的 psychometric audit（5,227 models × 6 benchmarks）；(2) global vs differential 框架和正交性实证有参考价值；(3) 半合成验证框架设计良好；(4) 鲁棒性检验极其全面。

**不接收理由**: (1) 方法论新颖性不足——核心是标准 MH-DIF 的直接应用；(2) framing 过度承诺——"measurement instability" 暗示基准有问题，但 DIF 可能反映正常的能力演化；(3) 实践建议（psychometric monitoring）的有效性依赖于无法验证的机制假设；(4) 格式合规存疑（激进 \enlargethispage）。

**升分路径**: 如果作者能 (a) 补充 model-type-stratified temporal DIF 分析以排除 composition artifact，(b) 修正 framing 为更中性的表述，(c) 在 Discussion 中按不同机制场景分别讨论行动含义，(d) 解决格式问题，则可上调至 4.0（Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-23T08:05:41.223449+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每一条：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并引用具体的 Section/Table/Figure 作为证据\n\n特别关注与你自己审稿意见的差异和重叠。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Strengths\nS1: 分析规模和严谨性令人印象深刻。5,227 个模型 × 12,508 题目是目前已知最大规模的 DIF 分析。鲁棒性检验极其全面。\nS2: Global exposure vs. differential functioning 二维框架有实际价值。正交性的实证证据充分且可信。\nS3: 半合成验证框架设计良好。Cross-subject matching 保证 ΔFPR = 0 的理论分析简洁优雅。\nS4: 六个基准的跨基准复现增强了可信度。\nS5: base-vs-instruct 反转是论文最有洞察力的发现（χ² = 562.7）。\nS6: 诚实展示局限性。\n\n### Must-Fix 问题\n\n**W-F1 [critical]: \"Temporal measurement instability\" 的 framing 存在根本性张力**\n论文将 DIF 定义为 \"temporal measurement instability\"，但 \"instability\" 暗示基准测试存在缺陷。然而论文同时展示了：(a) 聚合排名几乎不受影响（ρ ≈ 0.997）；(b) DIF-flagged 题目集中了最高区分度信号；(c) DIF 可能反映真实能力演化。如果 DIF 反映的是真实 capability evolution，那么所谓 \"instability\" 恰恰是基准测试正常工作的表现。建议将 \"instability\" 替换为更中性术语，或更强力论证为什么即使来源于 capability evolution 它仍构成 \"instability\"。\n\n**W-F2 [critical]: DIF 无法区分 contamination / capability evolution / composition shift——实践含义讨论不够充分**\n论文承认 DIF \"detects what, not why\" 但直接跳到规范性建议 \"benchmarks need psychometric monitoring\"。这个跳跃缺乏逻辑支撑：若是 contamination 应移除 flagged 题目；若是 capability evolution，移除它们会损害基准质量；若是 composition shift，问题在 cohort 定义。Section 5.2 的 audit protocol 没有讨论在不同机制假设下行动后果截然不同。建议按不同机制场景分别讨论行动含义。\n\n**W-C1 [critical]: \\enlargethispage 使用过于激进，可能实质性违反 8 页限制**\nexperiments.tex 的 `\\enlargethispage*{4\\baselineskip}` + discussion.tex 的 `\\enlargethispage*{6\\baselineskip}` 共增加约 10 行空间。6\\baselineskip 极为激进，page 8 异常密集。还有 15 处 `\\looseness=-1/-2`。建议控制 \\enlargethispage 在 ≤2\\baselineskip 以内。\n\n### Should-Fix 问题\n\n**W-N1 [warning]: 核心方法是 1988 年的标准 MH-DIF，方法论新颖性有限**\n贡献定位为 \"methodological and empirical\" 但实际上是 \"application of existing methodology to a new domain\"。\n\n**W-N2 [warning]: \"两个维度\" 框架的新颖性被高估——正交性可能是预期结果而非发现**\nWeb-overlap 标签（global, 与模型无关）和 DIF（differential, 与模型相关）概念上就测量不同的东西，因此正交性是概念上预期的。\n\n**W-F3 [warning]: 缺少 base-vs-instruct composition shift 的直接控制**\n2023 和 2024 cohort 中 base/instruct 比例可能不同。论文做了 ability matching 但没做 model-type-stratified temporal DIF。建议补充。\n\n**W-W1 [warning]: 术语不一致**\n\"measurement instability\", \"temporal DIF\", \"temporal comparability\" 等术语交替使用。\n\n**W-W2 [warning]: Conclusion 过于简短**\n仅 4 句话，未讨论 practical implications 和 future directions。\n\n**W-W3 [warning]: Abstract 信息密度过高**\n数字堆叠，非 psychometrics 读者难以消化。\n\n### Questions\nQ1: 2023/2024 cohort 中 base/instruct 比例？是否做过 model-type-stratified temporal DIF？\nQ2: Section 5.1 的 base N=1,409、instruct N=478 与 temporal cohort N=1,887 的关系？\nQ3: Maeda (2025) 是否属于将 DIF 应用于 LLM 评估的先例？\nQ4: Growing Pains anchor items 与本文 stable items 的重叠度？\nQ5: DIF audit 后具体应采取什么行动？不同机制下后果如何？\n\n### Missing References\n1. Population composition 在 DIF 分析中的影响文献\n2. LLM evaluation 中 fairness-oriented DIF 工作\n3. Suk and Weiss (2026) 值得更详细讨论\n\n### Overall: 3.5 — Borderline Conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每一条：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并引用具体的 Section/Table/Figure 作为证据\n\n特别关注与你自己审稿意见的差异和重叠。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### Strengths\nS1: 分析规模和严谨性令人印象深刻。5,227 个模型 × 12,508 题目是目前已知最大规模的 DIF 分析。鲁棒性检验极其全面。\nS2: Global exposure vs. differential functioning 二维框架有实际价值。正交性的实证证据充分且可信。\nS3: 半合成验证框架设计良好。Cross-subject matching 保证 ΔFPR = 0 的理论分析简洁优雅。\nS4: 六个基准的跨基准复现增强了可信度。\nS5: base-vs-instruct 反转是论文最有洞察力的发现（χ² = 562.7）。\nS6: 诚实展示局限性。\n\n### Must-Fix 问题\n\n**W-F1 [critical]: \"Temporal measurement instability\" 的 framing 存在根本性张力**\n论文将 DIF 定义为 \"temporal measurement instability\"，但 \"instability\" 暗示基准测试存在缺陷。然而论文同时展示了：(a) 聚合排名几乎不受影响（ρ ≈ 0.997）；(b) DIF-flagged 题目集中了最高区分度信号；(c) DIF 可能反映真实能力演化。如果 DIF 反映的是真实 capability evolution，那么所谓 \"instability\" 恰恰是基准测试正常工作的表现。建议将 \"instability\" 替换为更中性术语，或更强力论证为什么即使来源于 capability evolution 它仍构成 \"instability\"。\n\n**W-F2 [critical]: DIF 无法区分 contamination / capability evolution / composition shift——实践含义讨论不够充分**\n论文承认 DIF \"detects what, not why\" 但直接跳到规范性建议 \"benchmarks need psychometric monitoring\"。这个跳跃缺乏逻辑支撑：若是 contamination 应移除 flagged 题目；若是 capability evolution，移除它们会损害基准质量；若是 composition shift，问题在 cohort 定义。Section 5.2 的 audit protocol 没有讨论在不同机制假设下行动后果截然不同。建议按不同机制场景分别讨论行动含义。\n\n**W-C1 [critical]: \\enlargethispage 使用过于激进，可能实质性违反 8 页限制**\nexperiments.tex 的 `\\enlargethispage*{4\\baselineskip}` + discussion.tex 的 `\\enlargethispage*{6\\baselineskip}` 共增加约 10 行空间。6\\baselineskip 极为激进，page 8 异常密集。还有 15 处 `\\looseness=-1/-2`。建议控制 \\enlargethispage 在 ≤2\\baselineskip 以内。\n\n### Should-Fix 问题\n\n**W-N1 [warning]: 核心方法是 1988 年的标准 MH-DIF，方法论新颖性有限**\n贡献定位为 \"methodological and empirical\" 但实际上是 \"application of existing methodology to a new domain\"。\n\n**W-N2 [warning]: \"两个维度\" 框架的新颖性被高估——正交性可能是预期结果而非发现**\nWeb-overlap 标签（global, 与模型无关）和 DIF（differential, 与模型相关）概念上就测量不同的东西，因此正交性是概念上预期的。\n\n**W-F3 [warning]: 缺少 base-vs-instruct composition shift 的直接控制**\n2023 和 2024 cohort 中 base/instruct 比例可能不同。论文做了 ability matching 但没做 model-type-stratified temporal DIF。建议补充。\n\n**W-W1 [warning]: 术语不一致**\n\"measurement instability\", \"temporal DIF\", \"temporal comparability\" 等术语交替使用。\n\n**W-W2 [warning]: Conclusion 过于简短**\n仅 4 句话，未讨论 practical implications 和 future directions。\n\n**W-W3 [warning]: Abstract 信息密度过高**\n数字堆叠，非 psychometrics 读者难以消化。\n\n### Questions\nQ1: 2023/2024 cohort 中 base/instruct 比例？是否做过 model-type-stratified temporal DIF？\nQ2: Section 5.1 的 base N=1,409、instruct N=478 与 temporal cohort N=1,887 的关系？\nQ3: Maeda (2025) 是否属于将 DIF 应用于 LLM 评估的先例？\nQ4: Growing Pains anchor items 与本文 stable items 的重叠度？\nQ5: DIF audit 后具体应采取什么行动？不同机制下后果如何？\n\n### Missing References\n1. Population composition 在 DIF 分析中的影响文献\n2. LLM evaluation 中 fairness-oriented DIF 工作\n3. Suk and Weiss (2026) 值得更详细讨论\n\n### Overall: 3.5 — Borderline Conference"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-23T08:06:19.689933+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 38466
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-23T08:06:20.092002+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每一条：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并引用具体的 Section/Table/Figure 作为证据\n\n特别关注与你自己审稿意见的差异和重叠。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Strengths\nS1: 规模与系统性。5,227 模型 × 12,508 items，五种 cohort 设计构成严谨控制体系。\nS2: 非独立性校正框架扎实。DEFF + cluster bootstrap 两条独立路径收敛。\nS3: Cross-subject matching 的 FPR 保证精巧。\nS4: DIF 与 web-overlap 的正交性发现有概念性贡献。\nS5: 跨 benchmark 复制增强普适性。\nS6: 下游影响分析有实践价值。\nS7: 机制分析（Appendix B）有深度。\n\n### Weaknesses\n\n**W-M1 [Must-Fix] 时序混淆是论文最大的解释性缺口**\n2023 vs 2024 cohort 在架构、训练范式、数据规模、能力水平上同时变化。LLM 不同代模型对不同 item 类型展现不同能力 profile 是预期行为——与教育测量中同一课程体系下的 DIF（预期为零）有本质区别。base models 在难题上提升可能完全反映合法的训练方法论进步。如果无法区分 legitimate capability evolution 与 genuine measurement dysfunction，DIF rate 作为 benchmark 质量指标的实践价值存疑。建议：(a) 借鉴 Camilli and Shepard (1994) 区分 impact vs bias；(b) 引入 item-level covariates 作为 DIF 解释变量；(c) 将 \"measurement instability\" 改为 \"differential item functioning across model generations\"。\n\n**W-M2 [Should-Fix] DEFF 估计范围过宽，首选估计论证不充分**\nSimple-mean 29.2% vs weighted-mean 13.5%，2倍差距。r_s = −0.03 说明 ICC 不随 family size 变化，但不意味着应该用 simple-mean。在 survey methodology 中 weighted-mean 更合适（Kish, 1965）。建议展示 DEFF 敏感性分析和并列呈现两个估计。\n\n**W-M3 [Should-Fix] Semi-synthetic 注入模型生态效度有限**\nBinary response flipping 是对真实污染的粗糙近似。真实污染是单向的（只提升正确率）且与 difficulty 相关。建议定位为 \"detection power under a simplified injection model\"。\n\n**W-E1 [Should-Fix] ETS C 分类阈值在 N=5,227 下的适用性未讨论**\n|Δ_MH| ≥ 1.5 阈值来自教育测量（通常 N 数百到数千），在 N=5,227 下是否仍然合适？较大 N 意味着更精确的 Δ_MH 估计，可能更多 items 恰好越过阈值。\n\n**W-E2 [Should-Fix] Within-family 分析的 generalizability**\n主要依赖 Llama-2 vs Llama-3 和 Mistral，但这些 family 代际变化特别大。更小代际差异的 family 内 DIF 信号是否存在？\n\n**W-S1 [Should-Fix] 关键统计量缺少不确定性度量**\nDEFF 估计、Jaccard、Appendix B 的 OR 均未报告 CI 或标准误。\n\n**W-S2 [Minor] 多重比较处理的透明度**\n不同章节的 p 值多重比较处理方式不统一。\n\n**W-M4 [Minor] \"Measurement instability\" 概念操作化定义不够明确**\nMH-DIF 是 observed-score 方法，但用了 \"measurement instability\" 这一更强的概念标签。\n\n### Questions\nQ1: Matched-ability 控制的 matching 方法和质量？\nQ2: Jaccard = 0.206 在 permutation null 内——DIF 信号是否被 73.8% 非 web-overlap coverage 稀释？\nQ3: DEFF 校正降幅仅 2pp——family structure 实际影响很小？weighted-mean 为何差异如此大？\nQ4: AUROC = 0.603 接近 chance——支持还是反对 DIF 作为 measurement quality indicator？\nQ5: 不同 benchmark 的 C% 差异是否与 item 特征系统性相关？\n\n### Missing References\n1. Camilli & Shepard (1994) — DIF 经典教科书，区分 impact 和 bias\n2. Penfield & Camilli (2007) — DIF 方法论综述（可能已引用）\n3. Wainer (1993) — Differential Testlet Functioning，非独立性相关\n\n### Overall: 3.5 — Borderline Conference\n方法论框架扎实但时序混淆不可解性和 DEFF 范围削弱核心 claim 的可解释性。如果审慎限定 claim 并更透明处理 DEFF，可达 4.0。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "irt_equated_bench_regen",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每一条：\n- **[AGREE]**：同意并说明理由\n- **[REBUT]**：反驳并引用具体的 Section/Table/Figure 作为证据\n\n特别关注与你自己审稿意见的差异和重叠。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### Strengths\nS1: 规模与系统性。5,227 模型 × 12,508 items，五种 cohort 设计构成严谨控制体系。\nS2: 非独立性校正框架扎实。DEFF + cluster bootstrap 两条独立路径收敛。\nS3: Cross-subject matching 的 FPR 保证精巧。\nS4: DIF 与 web-overlap 的正交性发现有概念性贡献。\nS5: 跨 benchmark 复制增强普适性。\nS6: 下游影响分析有实践价值。\nS7: 机制分析（Appendix B）有深度。\n\n### Weaknesses\n\n**W-M1 [Must-Fix] 时序混淆是论文最大的解释性缺口**\n2023 vs 2024 cohort 在架构、训练范式、数据规模、能力水平上同时变化。LLM 不同代模型对不同 item 类型展现不同能力 profile 是预期行为——与教育测量中同一课程体系下的 DIF（预期为零）有本质区别。base models 在难题上提升可能完全反映合法的训练方法论进步。如果无法区分 legitimate capability evolution 与 genuine measurement dysfunction，DIF rate 作为 benchmark 质量指标的实践价值存疑。建议：(a) 借鉴 Camilli and Shepard (1994) 区分 impact vs bias；(b) 引入 item-level covariates 作为 DIF 解释变量；(c) 将 \"measurement instability\" 改为 \"differential item functioning across model generations\"。\n\n**W-M2 [Should-Fix] DEFF 估计范围过宽，首选估计论证不充分**\nSimple-mean 29.2% vs weighted-mean 13.5%，2倍差距。r_s = −0.03 说明 ICC 不随 family size 变化，但不意味着应该用 simple-mean。在 survey methodology 中 weighted-mean 更合适（Kish, 1965）。建议展示 DEFF 敏感性分析和并列呈现两个估计。\n\n**W-M3 [Should-Fix] Semi-synthetic 注入模型生态效度有限**\nBinary response flipping 是对真实污染的粗糙近似。真实污染是单向的（只提升正确率）且与 difficulty 相关。建议定位为 \"detection power under a simplified injection model\"。\n\n**W-E1 [Should-Fix] ETS C 分类阈值在 N=5,227 下的适用性未讨论**\n|Δ_MH| ≥ 1.5 阈值来自教育测量（通常 N 数百到数千），在 N=5,227 下是否仍然合适？较大 N 意味着更精确的 Δ_MH 估计，可能更多 items 恰好越过阈值。\n\n**W-E2 [Should-Fix] Within-family 分析的 generalizability**\n主要依赖 Llama-2 vs Llama-3 和 Mistral，但这些 family 代际变化特别大。更小代际差异的 family 内 DIF 信号是否存在？\n\n**W-S1 [Should-Fix] 关键统计量缺少不确定性度量**\nDEFF 估计、Jaccard、Appendix B 的 OR 均未报告 CI 或标准误。\n\n**W-S2 [Minor] 多重比较处理的透明度**\n不同章节的 p 值多重比较处理方式不统一。\n\n**W-M4 [Minor] \"Measurement instability\" 概念操作化定义不够明确**\nMH-DIF 是 observed-score 方法，但用了 \"measurement instability\" 这一更强的概念标签。\n\n### Questions\nQ1: Matched-ability 控制的 matching 方法和质量？\nQ2: Jaccard = 0.206 在 permutation null 内——DIF 信号是否被 73.8% 非 web-overlap coverage 稀释？\nQ3: DEFF 校正降幅仅 2pp——family structure 实际影响很小？weighted-mean 为何差异如此大？\nQ4: AUROC = 0.603 接近 chance——支持还是反对 DIF 作为 measurement quality indicator？\nQ5: 不同 benchmark 的 C% 差异是否与 item 特征系统性相关？\n\n### Missing References\n1. Camilli & Shepard (1994) — DIF 经典教科书，区分 impact 和 bias\n2. Penfield & Camilli (2007) — DIF 方法论综述（可能已引用）\n3. Wainer (1993) — Differential Testlet Functioning，非独立性相关\n\n### Overall: 3.5 — Borderline Conference\n方法论框架扎实但时序混淆不可解性和 DEFF 范围削弱核心 claim 的可解释性。如果审慎限定 claim 并更透明处理 DEFF，可达 4.0。"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-23T08:06:21.658695+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1566
}
```

</details>

---


### Assistant

_source line 1308 · 2026-05-23T08:06:24.767048+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 128

## Round 128

4 recorded events


### User

_source line 1309 · 2026-05-23T08:06:27.435907+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿要点总结：**

- **Overall: 3.5（Borderline Conference）**
- **3 个 Must-Fix**: (1) "temporal measurement instability" framing 与 DIF 无法归因的限制存在根本张力；(2) 实践建议缺乏机制区分的讨论；(3) \enlargethispage 使用过于激进（共 10\baselineskip），可能实质性违反 8 页限制
- **6 个 Should-Fix**: 方法论新颖性有限（标准 MH-DIF 直接应用）、"两维度"正交性可能是预期结果而非发现、缺少 base/instruct composition shift 控制、术语不一致、Conclusion 过短、Abstract 信息密度过高
- **升分路径明确**: 补充 model-type-stratified temporal DIF + 修正 framing + 按机制场景讨论行动含义 + 解决格式问题 → 可达 4.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-23T08:06:36.800317+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "提醒：请提交你对 Reviewer 2 审稿意见的交叉回应（[AGREE]/[REBUT]）。如果你已经完成分析，请直接输出交叉回应结果。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "project": "irt_equated_bench_regen",
    "round_number": "1",
    "text": "提醒：请提交你对 Reviewer 2 审稿意见的交叉回应（[AGREE]/[REBUT]）。如果你已经完成分析，请直接输出交叉回应结果。"
  }
}
```

</details>

---


### Tool result

_source line 1311 · 2026-05-23T08:06:40.667914+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3867
}
```

</details>

---


### Assistant

_source line 1312 · 2026-05-23T08:06:42.763895+00:00_

等待两位 Reviewer 提交交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1313 · 2026-05-23T08:07:54.820324+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 — 针对 Reviewer 2 的审稿意见

---

### Strengths 部分

对 R2 的 S1-S6 无异议，与我自己的评估一致。

---

### Must-Fix 问题

**[AGREE] R2-W-F1: "Temporal measurement instability" framing 的根本性张力**

强烈同意。这与我的 W-M1 高度重叠，且 R2 的论证角度更尖锐：论文自身提供的证据（ρ ≈ 0.997 的聚合排名稳定性 + DIF items 集中最高区分度信号）实际上在反驳 "instability" 的负面含义。我的 W-M1 从时序混淆角度切入，R2 从论文内部证据矛盾切入——两条独立路径指向同一结论：「measurement instability」这一 framing 缺乏充分论证。

补充一点 R2 未提到的：Section 5.1 的 base-vs-instruct difficulty gradient reversal（χ² = 562.7, p < 10⁻¹²⁴）本身就是一个极有价值的发现，但论文将其归类在 "instability" 叙事下反而削弱了它的意义。如果改为 "structured differential functioning reflecting training paradigm evolution"，同一发现会有更清晰的理论定位。

**[AGREE] R2-W-F2: DIF 无法区分机制——实践含义讨论不足**

同意核心论点。R2 指出 Section 5.2 的 audit protocol 在不同机制假设下行动后果截然不同——这一批评精准。具体而言，Section 5.2 建议 "MH-DIF audits when ever ≥500 models accumulate"（page 8），但若 DIF 反映的是 legitimate capability evolution，这种审计会系统性地标记高质量题目为 "不稳定"，反而损害 benchmark 质量。

不过我要补充一个 nuance：论文在 Section 4.6 展示了 DIF-ordered removal 导致 33.6% 的排名反转（page 8, Figure 4），这至少说明 DIF 信号对实践决策有影响，不论底层机制如何。问题不在于 DIF 是否有信号，而在于论文直接从 "有信号" 跳到 "需要监控" 而未讨论 "信号意味着什么"。

**[REBUT] R2-W-C1: \enlargethispage 使用可能违反页数限制**

不完全同意将此列为 critical。从 PDF 渲染结果看：
- 主文（§1-§6 Conclusion）终止于第 8 页底部
- Limitations 从第 9 页开始
- EMNLP 2026 规则明确 Limitations 不计入 8 页限制

Page 8 确实比其他页面更密集，但就我在 PDF 中所见，正文内容在视觉上仍在第 8 页之内。`\enlargethispage` 和 `\looseness` 是 LaTeX 排版的常见技巧，绝大多数顶会投稿都使用——只要最终渲染结果不超过页数限制即可。除非 PC 明确禁止这些命令（ARR CFP 和 reviewer guidelines 中我未找到此类禁令），我认为这属于 **Should-Fix** 而非 **Critical**。

但我同意 R2 的观察：page 8 的信息密度异常高——Discussion + Conclusion 压缩在不到一页内，这影响了可读性。建议作者考虑精简 Section 4 中的冗余内容以给 Discussion 留出空间，而不是通过排版技巧挤压。

---

### Should-Fix 问题

**[REBUT] R2-W-N1: 核心方法是 1988 年的标准 MH-DIF，方法论新颖性有限**

部分不同意。MH-DIF 本身确实是 1988 年的方法，但论文的方法论贡献不在 MH 本身，而在三个适配：
1. **DEFF 非独立性校正**（Section 4.2, Appendix E）——将 survey sampling 的 design effect 概念引入 LLM DIF 分析，处理 model family 结构，这在 DIF 文献中不常见
2. **Cross-subject matching 的 FPR 保证**（Section 3.4）——利用多科目结构实现理论上的零 FPR，这是对 MH 方法在多维 benchmark 场景下的非平凡扩展
3. **Semi-synthetic validation pipeline**（Section 3.4, 4.5）——将 dose-response 验证框架与 DIF 结合

将论文定位为 "application of existing methodology" 过于苛刻。更准确的说法是 "methodological adaptation with domain-specific innovations"。当然，论文确实应该在 Introduction 中更明确地区分「采用已有方法」和「本文的方法论贡献」。

**[AGREE] R2-W-N2: 正交性可能是概念上预期的结果**

同意这一观察。Web-overlap（static, model-agnostic）和 DIF（dynamic, model-dependent）在概念上就测量不同维度，因此低 Jaccard 是预期而非惊喜。但我认为这并不完全削弱其贡献价值——概念预期和实证确认之间有差距。许多"概念上预期"的结果在实证中被推翻（如 benchmark contamination detection methods 之间的低一致性，见 Balloccu et al., 2024）。论文的实证确认（κ = 0.012, OR = 1.05, permutation test p = 0.88）将直觉上的预期转化为有统计支撑的事实，仍有增量贡献。

建议作者在论文中 acknowledge 这一预期性，将贡献定位从 "surprising discovery" 调整为 "empirical confirmation of a theoretically expected but previously unverified distinction"。

**[AGREE] R2-W-F3: 缺少 base-vs-instruct composition shift 的直接控制**

同意，这是我审稿中遗漏的一个重要控制。2023→2024 cohort 中 base/instruct 比例变化可能是 DIF 信号的混淆源。论文做了 matched-ability 控制（Table 2, C% = 28.35%）但 ability matching 不等同于 model-type matching。

具体而言：如果 2024 cohort 中 instruct models 比例显著高于 2023，而 instruct models 在易题上系统性表现不同（Section 5.1 已证明），那么观察到的 temporal DIF 可能部分归因于 cohort composition shift 而非 item-level measurement change。

这个控制应该很容易补充：对 base models 和 instruct models 分别做 temporal DIF 分析，比较两个 subgroup 的 C% 是否一致。

**[AGREE] R2-W-W1: 术语不一致**

同意。这与我的 W-M4 重叠。"measurement instability"、"temporal DIF"、"temporal comparability"、"differential functioning" 在论文中交替使用但含义不完全相同。建议统一术语体系。

**[AGREE] R2-W-W2: Conclusion 过于简短**

同意。从 PDF page 8 可见，Section 6 Conclusion 仅约 4 句话，未讨论 practical implications、limitations of the audit protocol、或 future directions。这与论文的规模和深度不匹配。这可能正是 W-C1 所提排版挤压的后果——Discussion 和 Conclusion 被压缩以适应页数限制。

**[AGREE] R2-W-W3: Abstract 信息密度过高**

同意。Abstract 包含至少 8 个具体数字（5,227; 27,125; 31.3%; 27-29%; 0.206; 13.5%; 0.997; 562.7），对非 psychometrics 背景读者确实难以消化。建议减少数字、增加 narrative clarity。

---

### Questions 部分

**R2-Q1 (base/instruct 比例 + model-type-stratified DIF)**：支持这一问题。与 W-F3 直接相关，是关键缺失控制。

**R2-Q2 (Section 5.1 的 N 与 temporal cohort N 的关系)**：合理的技术性澄清问题。

**R2-Q3 (Maeda 2025 是否为先例)**：有价值的先例确认问题。论文引用了 Maeda (2025) 但未详细讨论其方法和发现——如果 Maeda 已经将 DIF 应用于 LLM 评估，论文应明确说明与 Maeda 的差异（规模、方法适配、发现）。

**R2-Q4 (Growing Pains anchor items 与 stable items 重叠度)**：有趣但非关键。Growing Pains (Habba et al., 2026) 使用 IRT calibration 识别 anchor items，本文使用 DIF 识别 unstable items——两种方法的 complementarity 值得讨论但不影响接收决定。

**R2-Q5 (DIF audit 后的具体行动)**：与 W-F2 直接相关，是核心问题。

---

### Missing References 部分

R2 指出的三类文献（population composition 对 DIF 的影响、LLM fairness-oriented DIF、Suk and Weiss 2026 详细讨论）均有道理，但均不构成关键遗漏。其中 Suk and Weiss (2026) 论文已引用（References page 11），只是讨论不够深入。

---

### 总结：R1 与 R2 的共识与分歧

**核心共识**（两位 reviewer 独立得出）：
1. **Framing 问题**：「measurement instability」的 claim 缺乏充分论证，temporal confound 未解决（R1-W-M1 ≈ R2-W-F1 ≈ R2-W-F2）
2. **规模和方法论系统性是主要优势**
3. **DIF-contamination 正交性有贡献但可能被高估**
4. **Overall 3.5, Borderline Conference**

**主要分歧**：
1. **\enlargethispage 严重性**：R2 列为 critical，R1 认为是 should-fix（排版技巧 vs 页数违规的界限）
2. **方法论新颖性**：R2 认为有限（W-N1），R1 认为 DEFF/cross-subject matching/semi-synthetic 三个适配具有独立贡献
3. **DEFF 估计范围**：R1 将此列为独立的 should-fix 问题（W-M2），R2 未专门讨论

**建议 AC**：核心问题集中在 framing 和 interpretability——如果作者能在 revision 中 (a) 退回到更中性的 claim、(b) 补充 model-type-stratified 控制、(c) 分机制讨论 practical implications，论文可以达到 Conference 水平。当前版本 3.5 是合理评分。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1314 · 2026-05-23T08:08:08.942130+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 130

## Round 130

3 recorded events


### User

_source line 1315 · 2026-05-23T08:08:11.605988+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。主要结论：

- 与 R2 在核心问题上高度一致（framing 张力、temporal confound、术语不一致），独立得出相同的 3.5 评分
- 对 R2 的 3 个 critical 中 2 个表示同意（W-F1、W-F2），对 \enlargethispage 问题（W-C1）降级为 should-fix
- 反驳了 R2 对方法论新颖性的低估——DEFF 校正、cross-subject matching、semi-synthetic validation 是非平凡适配
- 补充支持了 R2 提出的 base/instruct composition shift 控制缺失（W-F3），这是我原始审稿遗漏的

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-23T08:08:21.969874+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "提醒：请提交你对 Reviewer 1 审稿意见的交叉回应（[AGREE]/[REBUT]）。如果你已经完成分析，请直接输出交叉回应结果。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "project": "irt_equated_bench_regen",
    "round_number": "1",
    "text": "提醒：请提交你对 Reviewer 1 审稿意见的交叉回应（[AGREE]/[REBUT]）。如果你已经完成分析，请直接输出交叉回应结果。"
  }
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-23T08:08:26.145879+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 4176
}
```

</details>

---


## Round 131

## Round 131

8 recorded events


### User

_source line 1318 · 2026-05-23T08:08:27.885732+00:00_

[Reviewer 1 审稿结果]:
已在上一轮提交。交叉回应已通过 `review_reviewer_post_to_director` 发送给 Director，包含对 R2 全部意见的逐条 [AGREE]/[REBUT] 回应及 R1-R2 共识与分歧总结。无需重复提交。

---

[Reviewer 2 审稿结果]:
逐条回应 Reviewer 1 的审稿意见如下。

---

**R1-S1 to S7 (Strengths)**

[AGREE] R1-S1 至 S7：与我的 S1–S6 高度重叠。我额外强调了 base-vs-instruct 反转（我的 S5）作为论文最有洞察力的发现，R1 没有单独列出但在 S7（机制分析）中部分覆盖。

---

### Weaknesses 逐条回应

**[AGREE] R1-W-M1: 时序混淆是论文最大的解释性缺口**

强烈同意，这与我的 W-F1 和 W-F2 是同一个核心问题的不同表述。R1 的表述更精准：在教育测量中，DIF 预期为零（因为同一课程体系下不同人群应该有相同的 item functioning），但 LLM 代际之间在架构、训练数据、RLHF 上的根本性差异使得 DIF ≠ 0 是 *预期行为*，不必然是 measurement dysfunction。

我补充一个 R1 未明确提到的证据：Section 5.1 展示 base 模型 N=1,409 vs instruct 模型 N=478 产生方向相反的 DIF pattern（χ² = 562.7），但论文从未报告 2023 和 2024 temporal cohort 中 base/instruct 的比例。如果 2024 有更多 instruct 模型，部分 "temporal DIF" 可能只是 composition artifact（我的 W-F3）。R1 的 "legitimate capability evolution" 论点和我的 "composition shift" 论点是同一问题的两个层面。

R1 建议引入 Camilli and Shepard (1994) 的 impact vs bias 区分——我同意这会强化论文。目前论文没有明确讨论 observed DIF 是 bias（真正的测量缺陷）还是 impact（合法的能力差异在 item 层面的体现）。

**[AGREE] R1-W-M2: DEFF 估计范围过宽**

部分同意。R1 指出 simple-mean（29.2%）vs weighted-mean（13.5%）的 2 倍差距是合理关切。但我认为论文对 simple-mean 的偏好有一定论据支撑：Appendix I 展示 ICC 与 family size 的 Spearman ρ = −0.009（p = 0.96），且 Appendix C Table 9 的 size-stratified 分析显示大 family 的 ICC 反而更低（0.082 vs 小 family 的 0.246）。这意味着 weighted-mean 对 Mistral（N=547）和 Llama-3（N=315）赋予了过高的权重，而这两个 mega-family 内部实际上并不比小 family 更同质。

R1 说 "在 survey methodology 中 weighted-mean 更合适"——这在传统 survey 中成立（因为大 cluster 的样本量确实反映了 population 结构），但 LLM 的 model family 不是自然 population 的随机抽样。Mistral 有 547 个变体不是因为 "Mistral 模型在 population 中占比更高"，而是因为社区对该模型的 fine-tune 更多。这一 domain-specific argument 论文提到了（Appendix I: "arithmetic artifact of mega-family dominance"），但确实不够突出。

建议论文并列呈现两个估计（R1 的建议合理），同时更强力地论证为什么在 LLM 场景下 simple-mean 是更合适的选择。

**[AGREE] R1-W-M3: Semi-synthetic 生态效度有限**

同意。Binary response flipping 是 worst-case uniform injection，不反映真实污染模式（partial memorization、format-specific advantages 等）。但我补充：论文在 Limitations (1) 和 Section 3.4 中已明确承认 "reported ΔTPR values are upper-bound estimates"，并且 Appendix B 的 mixed-mechanism injection（Scheme D）尝试了更复杂的注入模式，发现 instruct 模型的 DIF pattern 无法被任何注入方案完全复现（simulated ρ_instruct = −0.302 vs observed −0.079），这实际上 *增强* 了论文的 mechanism-agnostic 定位。

R1 建议定位为 "detection power under a simplified injection model"——合理，但论文已基本做到了这一点。这是 Should-Fix 而非 Must-Fix 级别的问题。

**[REBUT] R1-W-E1: ETS C 阈值在 N=5,227 下的适用性**

R1 担心大 N 下更多 items 恰好越过 |Δ_MH| ≥ 1.5 阈值。但这个担忧被论文中两处关键事实所缓解：

1. Section 3.2 明确讨论了这一点："At N = 5,227, significance (p < 0.05) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5: only 3 of 3,918 C items lack significance, so the dual criterion effectively reduces to a single effect-size threshold." 也就是说，在大 N 下 ETS C 的 significance 条件变得冗余，但 *effect-size* 条件（|Δ_MH| ≥ 1.5）是固定的，不随 N 变化。|Δ_MH| ≥ 1.5 对应 odds ratio ≈ 1.9×，这是一个固定的效应量标准。
2. DEFF 校正恢复了 p-value 的选择性：Section 3.2 报告 "under simple-mean DEFF, 269 items (6.9%) lose significance while retaining |Δ_MH| ≥ 1.5"——即 DEFF 校正后确实有部分 items 因为 effective N 减小而 p > 0.05，从而被正确排除。
3. Section 4.2 展示了 threshold sensitivity：|Δ_MH| ≥ 2.0 时 C% = 18.3%，≥ 2.5 时 C% = 10.2%，定性结论不变。

因此，R1 的担忧虽然在一般统计学意义上合理，但论文已通过 effect-size 固定阈值 + DEFF 校正 + threshold sensitivity 三层机制充分回应了。这不应是 Should-Fix 级别。

**[AGREE] R1-W-E2: Within-family generalizability**

同意这是一个合理关切。论文的 within-family 分析仅覆盖了 Llama-2 vs Llama-3（代际差异极大，C% = 61.3%）和 LOFO 分析中的 Mistral。缺少更小代际差异的 family pair（如 Llama-3 的不同 sub-versions，或 Qwen 系列的代际比较）。不过这受限于 METABENCH 数据集的可用性，论文 Limitations 中也未将此列为局限，建议补充。

**[AGREE] R1-W-S1: 关键统计量缺少不确定性度量**

同意。具体来说：
- Jaccard = 0.206 有 permutation null [0.203, 0.222]（Section 4.3），但 bootstrap CI 未报告
- DEFF 的 per-item 分布有 median/Q3/max（Appendix C），但 aggregate DEFF 的 CI 未报告
- Appendix B 的 OR 有 CI（OR = 1.05 [0.96, 1.15]），但其他 OR 未报告

不过我认为这是 Minor 而非 Should-Fix——论文的核心结论（DIF rate 远超 random baseline 75–174×）对这些不确定性不敏感。

**[AGREE] R1-W-S2: 多重比较处理透明度**

同意，Minor 级别。Section 3.2 末尾解释了不做 family-wise correction 的原因（ETS convention + BH-FDR 仅排除 3 items），但 Section 4.4（logistic regression 的 9 subjects）和 Appendix B 的多个 p-value 没有统一说明多重比较处理。

**[AGREE] R1-W-M4: "Measurement instability" 操作化定义**

同意，这与我的 W-F1 本质上是同一个问题。MH-DIF 是 observed-score conditioning 下的非参数检验，用 "measurement instability" 这一来自 IRT/CFA 传统的概念标签确实有 mismatch。在 psychometrics 文献中，measurement invariance 通常需要 CFA/MGCFA 框架来验证（Meredith, 1993; Vandenberg & Lance, 2000），MH-DIF 是更弱的、item-level 的检验。论文虽在 Section 1 定义了自己的用法（"the empirical phenomenon when DIF is detected across time-defined cohorts"），但这个自定义与读者对 "measurement instability" 的先验理解之间仍有张力。

---

### Questions 回应

**R1-Q1 (Matching 方法)**: [AGREE] 论文在 Appendix A 有详细描述（nearest-neighbor, caliper = 0.02, Cohen's d = −0.17），但正文中描述较简略。R1 要求更多 matching quality 细节是合理的。

**R1-Q2 (Jaccard 被稀释?)**: [REBUT] Jaccard 计算仅在 9,229 有标签的 items 上进行（Section 4.3: "on 9,229 annotated items"），未被无标签 items 稀释。73.8% coverage 不影响 Jaccard 计算——只影响能否对剩余 26.2% items 做同样的分析。

**R1-Q3 (DEFF 降幅)**: [AGREE] 这是一个好的澄清点。Simple-mean DEFF 降幅仅 2pp（31.3% → 29.2%）确实暗示 family structure 的实际影响比预期更小。Weighted-mean 的巨大差异（→ 13.5%）主要由两个 mega-family 驱动，不反映 typical family 的影响。论文应更清晰地说明这一点。

**R1-Q4 (AUROC = 0.603)**: [AGREE] 如我在 Minor-4 中指出，"near chance" 的表述不够精确。但这个结果对论文是 *支持性* 的——它说明 DIF susceptibility 不是固定的 item property（不能通过 item 特征预测），因此 DIF 是 emergent 的 cohort-item interaction，支持 post-hoc monitoring 而非 pre-screening 的建议。

**R1-Q5 (Benchmark C% 与 item 特征)**: [AGREE] 论文将 knowledge/reasoning vs procedural 的 C% 差异视为 descriptive，但没有正式检验。值得补充一个简单的回归分析看 item 特征（difficulty, discrimination, question length 等）是否解释 benchmark 间的 C% 差异。

---

### Missing References 回应

**R1-Ref1: Camilli & Shepard (1994)** — [AGREE] 这是 DIF 领域的核心教科书，impact vs bias 的区分直接回应了 W-M1 / W-F1 / W-F2 的核心问题。论文应该引用并讨论。

**R1-Ref2: Penfield & Camilli (2007)** — [REBUT] 论文已引用 Penfield and Camilli (2007) 作为 `penfield2007dif`（Section 2, DIF Methodology paragraph: "Penfield and Camilli (2007) provide comprehensive reviews"）。

**R1-Ref3: Wainer (1993)** — [REBUT] 论文已引用 Wainer (1993) 作为 `wainer1993differential`（Section 3.2 最后一段: "Following DIF convention (Wainer and Braun, 1993)"）。R1 可能遗漏了这一引用。

---

### 与我自己审稿意见的对比总结

**高度重叠的问题**：
- R1-W-M1 ≈ 我的 W-F1 + W-F2（temporal confounding / mechanism attribution）
- R1-W-M4 ≈ 我的 W-F1（terminology/framing）
- R1-W-M3 ≈ 我 Limitations 中的隐含关切

**R1 提出但我未提出的新观点**：
- W-E1（ETS C 阈值在大 N 下的适用性）——我认为论文已充分回应，但作为讨论点有价值
- W-E2（within-family 分析的 generalizability）——合理关切
- W-S1（统计量不确定性度量）——合理但 Minor 级别

**我提出但 R1 未提出的问题**：
- W-C1（\enlargethispage 格式违规）——R1 完全没有提及格式问题，这是一个显著差异。我认为 `\enlargethispage*{6\baselineskip}` 是严重的格式问题，可能触发 AC 格式审查
- W-F3（base/instruct composition shift 作为混淆因素）——R1 在 W-M1 中隐含提到了 composition 问题但未明确要求 model-type-stratified 控制
- W-N2（正交性可能是预期结果）——R1 在 Q2 中触及但未作为 weakness 提出
- W-W2 / W-W3（Abstract 过密 / Conclusion 过简）——写作层面的关切

**评分一致**：R1 和我都给出 3.5（Borderline Conference），升分路径也高度一致（限定 claim + 更透明地处理 mechanism ambiguity）。这增强了我对评分合理性的信心。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1319 · 2026-05-23T08:08:49.420798+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1320 · 2026-05-23T08:08:49.521593+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T07:56:04.932520+00:00\", \"completed_at\": \"2026-05-23T07:59:00.037510+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续 4 页无 figure/table（仅 page 4 有 2 个公式），审稿人在 Related Work → Method → Experiments 开头这段会感到视觉单调。建议将 Table 1 或 Figure 2 提前至 page 5-6（Method 或 Experiments 部分首次引用附近），打破纯文本节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 + Figure 2 + Table 2 三个 display items 挤在同一页，视觉密度过高，与前几页的纯文本形成强烈反差。如果能将其中一个前移可同时改善 pages 3-6 的空旷和 page 7 的拥挤\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"正文共 5 个 display items（2 figures + 3 tables），处于实证论文推荐范围 5-8 的下限。考虑将 appendix 中信息价值较高的图表（如 Figure 4 downstream impact）提升至正文\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 出现在 page 2 顶部，位置良好。但 page 1 完全无视觉元素——如果能在 page 1 底部放一个紧凑的 teaser（如 key result 数字或 pipeline overview），可进一步强化首页印象\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 3}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1321 · 2026-05-23T08:11:33.057123+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "issues:\n  # === Round 14 新发现 ===\n\n  - id: \"R14-W1\"\n    summary: \"Framing 根本性张力：'temporal measurement instability' 暗示基准缺陷，但 DIF 无法区分 contamination / capability evolution / composition shift，且论文自身证据（ρ≈0.997 排名稳定、DIF items 集中最高区分度）与 'instability' 负面含义矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M1 + R2-W-F1 + R2-W-F2 共识。两位 reviewer 从不同角度（R1: temporal confound 使 DIF≠0 是预期行为; R2: 论文内部证据自我矛盾）独立得出相同结论。R1 建议引入 Camilli & Shepard (1994) impact vs bias 区分。R2 建议按不同机制场景分别讨论行动含义。两位均标 Must-Fix/critical。历史相关: R13-W1 (机制归因不足)、R13-W8 (temporal confound)。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W2\"\n    summary: \"DEFF 估计范围过宽（simple-mean 29.2% vs weighted-mean 13.5%），首选 simple-mean 的论证不够充分\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M2 提出，R2 部分同意但认为论文对 simple-mean 有一定论据（ICC flat across sizes, 大 family ICC 反而更低）。R2 补充 LLM model family 不是自然 population 随机抽样，weighted-mean 高估 mega-family 权重。共识：应并列呈现两个估计，更透明。历史相关: R13-W2。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W3\"\n    summary: \"Semi-synthetic 注入模型生态效度有限：binary response flipping ≠ realistic contamination (memorization, partial exposure)\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M3 提出，R2 同意但补充论文已承认 upper-bound 性质且 mixed-mechanism injection 无法复现 instruct 模型 observed pattern（增强了 mechanism-agnostic 定位）。共识 Should-Fix。历史相关: R13-W3。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W4\"\n    summary: \"缺少 base/instruct composition shift 的直接控制：未报告 2023/2024 cohort 中 base/instruct 比例，未做 model-type-stratified temporal DIF\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-F3 提出，R1 在交叉回应中强烈支持（'我审稿中遗漏的一个重要控制'）。如果 2024 instruct 比例更高，部分 temporal DIF 可能是 composition artifact。补充分析应简单且关键。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W5\"\n    summary: \"\\\\enlargethispage 使用激进：discussion.tex 6\\\\baselineskip + experiments.tex 4\\\\baselineskip + 15处 \\\\looseness，page 8 密度异常\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2 标 critical（可能实质性违反 8 页限制），R1 降为 should-fix（正文内容仍在第 8 页内，Limitations 不计入页数，\\\\enlargethispage 是常见排版技巧）。分歧未解决，取 warning。两位均同意 page 8 可读性受影响，建议压缩 Section 4 冗余内容。历史相关: R13-W4（同一问题，R13 也 warning）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W6\"\n    summary: \"术语不一致：measurement instability / temporal DIF / temporal comparability / measurement invariance / measurement shift 交替使用\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M4 + R2-W-W1 共识。建议选一个核心术语一致使用。历史相关: R13-N1（同一问题）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W7\"\n    summary: \"方法论新颖性有限：核心 MH-DIF 是 1988 年标准方法的领域迁移\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-N1 提出，R1 部分反驳（DEFF 校正、cross-subject matching FPR 保证、semi-synthetic pipeline 是非平凡适配）。分歧：R2 认为 'application of existing methodology'，R1 认为 'methodological adaptation with domain-specific innovations'。历史相关: R13-W6。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W8\"\n    summary: \"Conclusion 仅 4 句话，未讨论 practical implications、future directions，与论文规模不匹配\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-W2 提出，R1 在交叉回应中同意。可能是排版挤压的后果。历史相关: R13-W7（同一问题）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N1\"\n    summary: \"Abstract 信息密度过高，至少 8 个具体数字，非 psychometrics 读者难以消化\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-W3 提出，R1 在交叉回应中同意。建议保留 2-3 个关键数字。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N2\"\n    summary: \"'两个维度'框架正交性可能是概念上预期的结果而非实证发现\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-N2 提出，R1 部分同意但认为实证确认仍有增量贡献。建议将贡献定位从 'surprising discovery' 调整为 'empirical confirmation of theoretically expected but previously unverified distinction'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 13 issues（状态更新） ===\n\n  - id: \"R13-W1\"\n    summary: \"机制归因不足：DIF 检测 'that' 但无法区分 contamination / capability evolution / training shift\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M3/W-E1 + R2-W-N2 共识。R2标Must-Fix，R1降为Should-Fix（educational measurement中diagnostic-without-attribution是标准实践）。最终共识Should-Fix。论文需在Discussion中更清晰界定DIF审计在机制不明条件下的决策价值，并为Section 5.2 audit protocol添加caveats。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 两位 reviewer 独立再次提出（R14-W1），问题未解决。R14 的表述更尖锐：不仅是归因不足，而是 framing 本身（'instability'）与无法归因的限制存在根本矛盾。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W2\"\n    summary: \"DEFF校正方法选择导致headline result 2×分歧（simple-mean 29.2% vs weighted-mean 13.5%），核心结论不确定性未充分透明呈现\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-S1 + R2-W-C2 共识。论文偏好simple-mean有合理论据（ρ_s=-0.009, size-stratified ICC递减），但weighted-mean是survey statistics标准方法。正文应更透明地同时报告两个估计。R2的4×范围(13.5%-53.2%)被R1纠正为2×范围(point estimates 27-29%, lower bound 13.5%)。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W2）。R2 补充了新论据：LLM model family 非自然 population 随机抽样，weighted-mean 高估 mega-family。但核心问题（并列呈现两个估计）未解决。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W3\"\n    summary: \"Semi-synthetic验证框架ecological validity不足：binary response flipping过于简化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M1, R2同意。验证了MH-DIF对differential item behavior的检测力，但injection model过于简化。Appendix A的mixed-mechanism injection也无法匹配instruct模型观测模式(simulated ρ_instruct=-0.302 vs observed -0.079)。建议增加更realistic的contamination model或更显式讨论ecological validity局限。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W3）。观点基本一致，R2 补充论文的 upper-bound 承认和 mixed-mechanism 结果部分缓解了问题。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W4\"\n    summary: \"\\\\enlargethispage使用激进：Discussion页+10baselineskip，实质上在8页内塞入约9页内容\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-F1标Must-Fix，R1降为Should-Fix。discussion.tex \\\\enlargethispage*{10\\\\baselineskip}(+4.3cm) + experiments.tex \\\\enlargethispage*{4\\\\baselineskip} + 多处负vspace。R1指出\\\\enlargethispage是合法LaTeX命令且许多ACL论文使用，不应作为reject理由，但建议压缩内容至appendix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W5）。discussion.tex 从 10\\\\baselineskip 降至 6\\\\baselineskip（有改善），但总量仍为 10\\\\baselineskip（6+4）。R2 仍标 critical，R1 仍降为 should-fix。分歧持续。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"ΔFPR=0 guarantee在Introduction中未限定为single-subject contamination条件\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M2提出，R2部分同意（同意intro需限定条件，但纠正R1的非单调性论据——Table 7 ΔFPR是单调递增的）。Section 3.4 Remark已限定但intro Contribution 2未限定。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出此问题。Contribution 2 当前写法为 'ΔFPR = 0 under single-subject contamination, k ≤ 5'，已有条件限定。可能已部分修复。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W6\"\n    summary: \"方法论新颖性有限：核心MH-DIF是1988年标准方法的领域迁移\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-N1。R1部分反驳（cross-subject matching和size-stratified DEFF是non-trivial适配），但同意核心贡献以应用和实证为主。两位reviewer均认为对EMNLP应定位为empirical contribution。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W7）。分歧模式与 R13 相同：R2 认为 'application'，R1 认为 'adaptation with domain-specific innovations'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W7\"\n    summary: \"Conclusion仅一句话，未能收束论证\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-C1标Should-Fix，R1同意但降为Minor（Section 5 Discussion已承担大部分conclusion功能）。配合\\\\vspace{-28pt}是空间不足症状。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W8）。Conclusion 从 R13 的 1 句扩展到 4 句，有改善但仍不充分。缺少 practical implications 和 future directions。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W8\"\n    summary: \"Temporal confound未完全解决：2023 vs 2024划分同时confound了architecture/training methodology/capability\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-E1，R2同意。Base-vs-instruct decomposition提供部分分离但model type本身与时间高度相关。论文的控制（ability-matched仅降2.4pp，domain gains <0.1% variance）缩小了替代解释空间但未消除confound。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 作为 R14-W1 的一部分再次提出。新增要求：model-type-stratified temporal DIF（R14-W4）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-N1\"\n    summary: \"术语一致性：measurement instability / temporal DIF / temporal comparability 交替使用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-W2, R1同意Minor。建议首次引入时明确定义关系。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W6）。问题未改善。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === 历史 issues（前轮已 resolved，保留记录） ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大（13.5%-29.2%），核心结论不确定性被低估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"simple mean vs weighted mean DEFF 导致范围过宽\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"三方法收敛论证缺失\"\n      - round: 18\n        reviewers: []\n        note: \"三方法收敛写入 §4.2\"\n      - round: 19\n        reviewers: [1, 2]\n        note: \"De-dup K=20 29.1% 数据不一致被发现（实际 19.7%）。ICC flat across sizes (ρ=-0.009) justifies simple-mean。修正为两方法收敛。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20再次要求size-stratified DEFF和连续参数化曲线。论证不对称仍是核心问题。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次提出DEFF分歧（见R13-W2），但scope不同：R13关注正文呈现透明度而非方法论本身。\"\n    action_items:\n      - round: 19\n        action: \"De-dup 29.1%→19.7%, three→two convergence\"\n        assigned_to: director\n        status: done\n      - round: 19\n        action: \"ICC terminology fix (model-level r, not item-level ICC)\"\n        assigned_to: director\n        status: done\n      - round: 19\n        action: \"Singleton DEFF scope clarification (99.8% in cohort have families)\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Size-stratified DEFF table in appendix (tab:deff_stratified)\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"§4.2 forward reference to size-stratified DEFF (B8: commit 0c3856a)\"\n        assigned_to: agent\n        status: done\n    resolution: \"Size-stratified DEFF table added (appendix). Per-tier ICC 0.246→0.082 confirms weighted variant over-corrects. Forward reference in §4.2 (rebuttal branch). Family definition sensitivity ≤0.3pp.\"\n    resolution_round: 20\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力，framing 不一致\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"DIF 无法区分 contamination vs legitimate improvement\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20再次标为Must-Fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W1），scope类似但R13 reviewers没有前轮记忆。\"\n    action_items:\n      - round: 19\n        action: \"C1 meta-critique→orthogonal constructs\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Base-vs-instruct decomposition already in paper\"\n        assigned_to: agent\n        status: done\n    resolution: \"Four exclusion arguments + base-vs-instruct decomposition (χ²=562.7) + difficulty-dependent contamination alternative discussed. Framing: 'orthogonal constructs' throughout.\"\n    resolution_round: 20\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法从未被正式定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"K 的含义、操作步骤均未给出\"\n    action_items:\n      - round: 19\n        action: \"Formal definition added to app:dedup_k\"\n        assigned_to: director\n        status: done\n    resolution: \"Formal definition in app:dedup_k: K members sampled uniformly at random, 5 draws per K.\"\n    resolution_round: 19\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique 措辞过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    action_items:\n      - round: 19\n        action: \"meta-critique→orthogonal constructs throughout\"\n        assigned_to: director\n        status: done\n    resolution: \"Contribution 1 reframed as 'Orthogonal constructs'. All 'category error' language removed.\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性不足：MH-DIF 是既有标准方法的直接应用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W6）。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal-only strategy; no paper change\"\n        assigned_to: author\n        status: done\n    resolution: \"Structural limitation acknowledged. Framing emphasizes empirical contribution over methodological novelty.\"\n    resolution_round: 20\n\n  - id: \"R19-M2\"\n    summary: \"Semi-synthetic ΔTPR 推广性存疑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Difficulty-dependent injection results written to §4.5/§5.1\"\n        assigned_to: agent\n        status: done\n    resolution: \"Difficulty-dependent injection (3 schemes: A/B/C) completed and written to paper.\"\n    resolution_round: 20\n\n  - id: \"R19-M3\"\n    summary: \"K=10 non-uniform DIF 泄漏\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Strengthen NUDIF caveat wording\"\n        assigned_to: agent\n        status: done\n    resolution: \"NUDIF caveat strengthened in paper.\"\n    resolution_round: 20\n\n  - id: \"R19-M5\"\n    summary: \"1:1 matching 细节缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Caliper correction added to appendix\"\n        assigned_to: director\n        status: done\n    resolution: \"Matching details in appendix: 1:1 nearest-neighbor, caliper 0.02 (≈0.14 SD), Cohen's d=-0.17, N=638 per group.\"\n    resolution_round: 20\n\n  - id: \"R19-N3\"\n    summary: \"Abstract 范围暗示不匹配\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Abstract now reads '5,227 MMLU models'.\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"Appendix rank-bucket 数据错误\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Data corrected in app:rank_reversal.\"\n    resolution_round: 19\n\n  - id: \"R20-Q3\"\n    summary: \"Difficulty-direction替代解释未讨论\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"§5.1 discusses difficulty-dependent contamination as alternative.\"\n    resolution_round: 20\n\n  - id: \"R20-N1\"\n    summary: \"GSM1K探索性分析权重过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"GSM1K marked as 'exploratory... requires replication'.\"\n    resolution_round: 20\n\n  - id: \"R20-N2\"\n    summary: \"enlargethispage格式激进\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W4），但更严重：discussion.tex仍有\\\\enlargethispage*{10\\\\baselineskip}。\"\n    resolution: \"enlargethispage reduced to ≤4 baselineskip, within safe range.\"\n    resolution_round: 20\n\n  - id: \"R20-Q5\"\n    summary: \"6个月窗口C%高于年度对比需解释\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"Appendix explains: shorter temporal window → more polarized cohorts.\"\n    resolution_round: 20\n\n  - id: \"R20-Q6\"\n    summary: \"DIF Audit Protocol ≥500阈值缺统计依据\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"≥500 softened to 'smaller corpora may suffice with K=3 or 2×2 designs'.\"\n    resolution_round: 20\n\n  - id: \"R20-MR\"\n    summary: \"缺失引用：Kamata & Binici 2003, Alzahrani et al 2024, MMLU-Pro\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"All 3 citations verified real. 2/3 already in bib.\"\n    resolution_round: 20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "issues:\n  # === Round 14 新发现 ===\n\n  - id: \"R14-W1\"\n    summary: \"Framing 根本性张力：'temporal measurement instability' 暗示基准缺陷，但 DIF 无法区分 contamination / capability evolution / composition shift，且论文自身证据（ρ≈0.997 排名稳定、DIF items 集中最高区分度）与 'instability' 负面含义矛盾\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M1 + R2-W-F1 + R2-W-F2 共识。两位 reviewer 从不同角度（R1: temporal confound 使 DIF≠0 是预期行为; R2: 论文内部证据自我矛盾）独立得出相同结论。R1 建议引入 Camilli & Shepard (1994) impact vs bias 区分。R2 建议按不同机制场景分别讨论行动含义。两位均标 Must-Fix/critical。历史相关: R13-W1 (机制归因不足)、R13-W8 (temporal confound)。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W2\"\n    summary: \"DEFF 估计范围过宽（simple-mean 29.2% vs weighted-mean 13.5%），首选 simple-mean 的论证不够充分\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M2 提出，R2 部分同意但认为论文对 simple-mean 有一定论据（ICC flat across sizes, 大 family ICC 反而更低）。R2 补充 LLM model family 不是自然 population 随机抽样，weighted-mean 高估 mega-family 权重。共识：应并列呈现两个估计，更透明。历史相关: R13-W2。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W3\"\n    summary: \"Semi-synthetic 注入模型生态效度有限：binary response flipping ≠ realistic contamination (memorization, partial exposure)\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M3 提出，R2 同意但补充论文已承认 upper-bound 性质且 mixed-mechanism injection 无法复现 instruct 模型 observed pattern（增强了 mechanism-agnostic 定位）。共识 Should-Fix。历史相关: R13-W3。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W4\"\n    summary: \"缺少 base/instruct composition shift 的直接控制：未报告 2023/2024 cohort 中 base/instruct 比例，未做 model-type-stratified temporal DIF\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-F3 提出，R1 在交叉回应中强烈支持（'我审稿中遗漏的一个重要控制'）。如果 2024 instruct 比例更高，部分 temporal DIF 可能是 composition artifact。补充分析应简单且关键。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W5\"\n    summary: \"\\\\enlargethispage 使用激进：discussion.tex 6\\\\baselineskip + experiments.tex 4\\\\baselineskip + 15处 \\\\looseness，page 8 密度异常\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2 标 critical（可能实质性违反 8 页限制），R1 降为 should-fix（正文内容仍在第 8 页内，Limitations 不计入页数，\\\\enlargethispage 是常见排版技巧）。分歧未解决，取 warning。两位均同意 page 8 可读性受影响，建议压缩 Section 4 冗余内容。历史相关: R13-W4（同一问题，R13 也 warning）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W6\"\n    summary: \"术语不一致：measurement instability / temporal DIF / temporal comparability / measurement invariance / measurement shift 交替使用\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R1-W-M4 + R2-W-W1 共识。建议选一个核心术语一致使用。历史相关: R13-N1（同一问题）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W7\"\n    summary: \"方法论新颖性有限：核心 MH-DIF 是 1988 年标准方法的领域迁移\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-N1 提出，R1 部分反驳（DEFF 校正、cross-subject matching FPR 保证、semi-synthetic pipeline 是非平凡适配）。分歧：R2 认为 'application of existing methodology'，R1 认为 'methodological adaptation with domain-specific innovations'。历史相关: R13-W6。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-W8\"\n    summary: \"Conclusion 仅 4 句话，未讨论 practical implications、future directions，与论文规模不匹配\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-W2 提出，R1 在交叉回应中同意。可能是排版挤压的后果。历史相关: R13-W7（同一问题）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N1\"\n    summary: \"Abstract 信息密度过高，至少 8 个具体数字，非 psychometrics 读者难以消化\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-W3 提出，R1 在交叉回应中同意。建议保留 2-3 个关键数字。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R14-N2\"\n    summary: \"'两个维度'框架正交性可能是概念上预期的结果而非实证发现\"\n    category: framing\n    severity: info\n    status: open\n    first_raised_round: 14\n    last_seen_round: 14\n    mentions:\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R2-W-N2 提出，R1 部分同意但认为实证确认仍有增量贡献。建议将贡献定位从 'surprising discovery' 调整为 'empirical confirmation of theoretically expected but previously unverified distinction'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 13 issues（状态更新） ===\n\n  - id: \"R13-W1\"\n    summary: \"机制归因不足：DIF 检测 'that' 但无法区分 contamination / capability evolution / training shift\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M3/W-E1 + R2-W-N2 共识。R2标Must-Fix，R1降为Should-Fix（educational measurement中diagnostic-without-attribution是标准实践）。最终共识Should-Fix。论文需在Discussion中更清晰界定DIF审计在机制不明条件下的决策价值，并为Section 5.2 audit protocol添加caveats。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 两位 reviewer 独立再次提出（R14-W1），问题未解决。R14 的表述更尖锐：不仅是归因不足，而是 framing 本身（'instability'）与无法归因的限制存在根本矛盾。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W2\"\n    summary: \"DEFF校正方法选择导致headline result 2×分歧（simple-mean 29.2% vs weighted-mean 13.5%），核心结论不确定性未充分透明呈现\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-S1 + R2-W-C2 共识。论文偏好simple-mean有合理论据（ρ_s=-0.009, size-stratified ICC递减），但weighted-mean是survey statistics标准方法。正文应更透明地同时报告两个估计。R2的4×范围(13.5%-53.2%)被R1纠正为2×范围(point estimates 27-29%, lower bound 13.5%)。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W2）。R2 补充了新论据：LLM model family 非自然 population 随机抽样，weighted-mean 高估 mega-family。但核心问题（并列呈现两个估计）未解决。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W3\"\n    summary: \"Semi-synthetic验证框架ecological validity不足：binary response flipping过于简化\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M1, R2同意。验证了MH-DIF对differential item behavior的检测力，但injection model过于简化。Appendix A的mixed-mechanism injection也无法匹配instruct模型观测模式(simulated ρ_instruct=-0.302 vs observed -0.079)。建议增加更realistic的contamination model或更显式讨论ecological validity局限。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W3）。观点基本一致，R2 补充论文的 upper-bound 承认和 mixed-mechanism 结果部分缓解了问题。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W4\"\n    summary: \"\\\\enlargethispage使用激进：Discussion页+10baselineskip，实质上在8页内塞入约9页内容\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-F1标Must-Fix，R1降为Should-Fix。discussion.tex \\\\enlargethispage*{10\\\\baselineskip}(+4.3cm) + experiments.tex \\\\enlargethispage*{4\\\\baselineskip} + 多处负vspace。R1指出\\\\enlargethispage是合法LaTeX命令且许多ACL论文使用，不应作为reject理由，但建议压缩内容至appendix。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W5）。discussion.tex 从 10\\\\baselineskip 降至 6\\\\baselineskip（有改善），但总量仍为 10\\\\baselineskip（6+4）。R2 仍标 critical，R1 仍降为 should-fix。分歧持续。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W5\"\n    summary: \"ΔFPR=0 guarantee在Introduction中未限定为single-subject contamination条件\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-M2提出，R2部分同意（同意intro需限定条件，但纠正R1的非单调性论据——Table 7 ΔFPR是单调递增的）。Section 3.4 Remark已限定但intro Contribution 2未限定。\"\n      - round: 14\n        reviewers: []\n        note: \"R14 未单独提出此问题。Contribution 2 当前写法为 'ΔFPR = 0 under single-subject contamination, k ≤ 5'，已有条件限定。可能已部分修复。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W6\"\n    summary: \"方法论新颖性有限：核心MH-DIF是1988年标准方法的领域迁移\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-N1。R1部分反驳（cross-subject matching和size-stratified DEFF是non-trivial适配），但同意核心贡献以应用和实证为主。两位reviewer均认为对EMNLP应定位为empirical contribution。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W7）。分歧模式与 R13 相同：R2 认为 'application'，R1 认为 'adaptation with domain-specific innovations'。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W7\"\n    summary: \"Conclusion仅一句话，未能收束论证\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-C1标Should-Fix，R1同意但降为Minor（Section 5 Discussion已承担大部分conclusion功能）。配合\\\\vspace{-28pt}是空间不足症状。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W8）。Conclusion 从 R13 的 1 句扩展到 4 句，有改善但仍不充分。缺少 practical implications 和 future directions。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-W8\"\n    summary: \"Temporal confound未完全解决：2023 vs 2024划分同时confound了architecture/training methodology/capability\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R1-W-E1，R2同意。Base-vs-instruct decomposition提供部分分离但model type本身与时间高度相关。论文的控制（ability-matched仅降2.4pp，domain gains <0.1% variance）缩小了替代解释空间但未消除confound。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 作为 R14-W1 的一部分再次提出。新增要求：model-type-stratified temporal DIF（R14-W4）。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R13-N1\"\n    summary: \"术语一致性：measurement instability / temporal DIF / temporal comparability 交替使用\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 13\n    last_seen_round: 14\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R2-W-W2, R1同意Minor。建议首次引入时明确定义关系。\"\n      - round: 14\n        reviewers: [1, 2]\n        note: \"R14 再次独立提出（R14-W6）。问题未改善。\"\n    action_items: []\n    resolution: \"\"\n    resolution_round: null\n\n  # === 历史 issues（前轮已 resolved，保留记录） ===\n\n  - id: \"R1-W1\"\n    summary: \"DEFF 校正范围过大（13.5%-29.2%），核心结论不确定性被低估\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"simple mean vs weighted mean DEFF 导致范围过宽\"\n      - round: 17\n        reviewers: [1, 2]\n        note: \"三方法收敛论证缺失\"\n      - round: 18\n        reviewers: []\n        note: \"三方法收敛写入 §4.2\"\n      - round: 19\n        reviewers: [1, 2]\n        note: \"De-dup K=20 29.1% 数据不一致被发现（实际 19.7%）。ICC flat across sizes (ρ=-0.009) justifies simple-mean。修正为两方法收敛。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20再次要求size-stratified DEFF和连续参数化曲线。论证不对称仍是核心问题。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次提出DEFF分歧（见R13-W2），但scope不同：R13关注正文呈现透明度而非方法论本身。\"\n    action_items:\n      - round: 19\n        action: \"De-dup 29.1%→19.7%, three→two convergence\"\n        assigned_to: director\n        status: done\n      - round: 19\n        action: \"ICC terminology fix (model-level r, not item-level ICC)\"\n        assigned_to: director\n        status: done\n      - round: 19\n        action: \"Singleton DEFF scope clarification (99.8% in cohort have families)\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Size-stratified DEFF table in appendix (tab:deff_stratified)\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"§4.2 forward reference to size-stratified DEFF (B8: commit 0c3856a)\"\n        assigned_to: agent\n        status: done\n    resolution: \"Size-stratified DEFF table added (appendix). Per-tier ICC 0.246→0.082 confirms weighted variant over-corrects. Forward reference in §4.2 (rebuttal branch). Family definition sensitivity ≤0.3pp.\"\n    resolution_round: 20\n\n  - id: \"R2-W4\"\n    summary: \"Temporal DIF 与 legitimate 能力提升的概念张力，framing 不一致\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 10\n        reviewers: [1, 2]\n        note: \"DIF 无法区分 contamination vs legitimate improvement\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20再次标为Must-Fix。\"\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W1），scope类似但R13 reviewers没有前轮记忆。\"\n    action_items:\n      - round: 19\n        action: \"C1 meta-critique→orthogonal constructs\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Base-vs-instruct decomposition already in paper\"\n        assigned_to: agent\n        status: done\n    resolution: \"Four exclusion arguments + base-vs-instruct decomposition (χ²=562.7) + difficulty-dependent contamination alternative discussed. Framing: 'orthogonal constructs' throughout.\"\n    resolution_round: 20\n\n  - id: \"R12-W1\"\n    summary: \"Graduated de-duplication 方法从未被正式定义\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    mentions:\n      - round: 12\n        reviewers: [1, 2]\n        note: \"K 的含义、操作步骤均未给出\"\n    action_items:\n      - round: 19\n        action: \"Formal definition added to app:dedup_k\"\n        assigned_to: director\n        status: done\n    resolution: \"Formal definition in app:dedup_k: K members sampled uniformly at random, 5 draws per K.\"\n    resolution_round: 19\n\n  - id: \"R12-W2\"\n    summary: \"Ground truth meta-critique 措辞过强\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 12\n    last_seen_round: 20\n    action_items:\n      - round: 19\n        action: \"meta-critique→orthogonal constructs throughout\"\n        assigned_to: director\n        status: done\n    resolution: \"Contribution 1 reframed as 'Orthogonal constructs'. All 'category error' language removed.\"\n    resolution_round: 19\n\n  - id: \"R2-W1\"\n    summary: \"方法论新颖性不足：MH-DIF 是既有标准方法的直接应用\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 10\n    last_seen_round: 20\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W6）。\"\n    action_items:\n      - round: 19\n        action: \"Rebuttal-only strategy; no paper change\"\n        assigned_to: author\n        status: done\n    resolution: \"Structural limitation acknowledged. Framing emphasizes empirical contribution over methodological novelty.\"\n    resolution_round: 20\n\n  - id: \"R19-M2\"\n    summary: \"Semi-synthetic ΔTPR 推广性存疑\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Difficulty-dependent injection results written to §4.5/§5.1\"\n        assigned_to: agent\n        status: done\n    resolution: \"Difficulty-dependent injection (3 schemes: A/B/C) completed and written to paper.\"\n    resolution_round: 20\n\n  - id: \"R19-M3\"\n    summary: \"K=10 non-uniform DIF 泄漏\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Strengthen NUDIF caveat wording\"\n        assigned_to: agent\n        status: done\n    resolution: \"NUDIF caveat strengthened in paper.\"\n    resolution_round: 20\n\n  - id: \"R19-M5\"\n    summary: \"1:1 matching 细节缺失\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 20\n    action_items:\n      - round: 20\n        action: \"Caliper correction added to appendix\"\n        assigned_to: director\n        status: done\n    resolution: \"Matching details in appendix: 1:1 nearest-neighbor, caliper 0.02 (≈0.14 SD), Cohen's d=-0.17, N=638 per group.\"\n    resolution_round: 20\n\n  - id: \"R19-N3\"\n    summary: \"Abstract 范围暗示不匹配\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Abstract now reads '5,227 MMLU models'.\"\n    resolution_round: 19\n\n  - id: \"R19-DATA1\"\n    summary: \"Appendix rank-bucket 数据错误\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 19\n    last_seen_round: 19\n    resolution: \"Data corrected in app:rank_reversal.\"\n    resolution_round: 19\n\n  - id: \"R20-Q3\"\n    summary: \"Difficulty-direction替代解释未讨论\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"§5.1 discusses difficulty-dependent contamination as alternative.\"\n    resolution_round: 20\n\n  - id: \"R20-N1\"\n    summary: \"GSM1K探索性分析权重过高\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"GSM1K marked as 'exploratory... requires replication'.\"\n    resolution_round: 20\n\n  - id: \"R20-N2\"\n    summary: \"enlargethispage格式激进\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 13\n        reviewers: [1, 2]\n        note: \"R13再次独立提出（见R13-W4），但更严重：discussion.tex仍有\\\\enlargethispage*{10\\\\baselineskip}。\"\n    resolution: \"enlargethispage reduced to ≤4 baselineskip, within safe range.\"\n    resolution_round: 20\n\n  - id: \"R20-Q5\"\n    summary: \"6个月窗口C%高于年度对比需解释\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"Appendix explains: shorter temporal window → more polarized cohorts.\"\n    resolution_round: 20\n\n  - id: \"R20-Q6\"\n    summary: \"DIF Audit Protocol ≥500阈值缺统计依据\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"≥500 softened to 'smaller corpora may suffice with K=3 or 2×2 designs'.\"\n    resolution_round: 20\n\n  - id: \"R20-MR\"\n    summary: \"缺失引用：Kamata & Binici 2003, Alzahrani et al 2024, MMLU-Pro\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 20\n    last_seen_round: 20\n    resolution: \"All 3 citations verified real. 2/3 already in bib.\"\n    resolution_round: 20"
  }
}
```

</details>

---


### Tool result

_source line 1322 · 2026-05-23T08:11:33.158321+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 19319}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1323 · 2026-05-23T08:14:29.693040+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 14 审稿报告\n\n**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 (ARR)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 叙事/framing + 写作)\n**审稿模式**: Fresh（重新审稿，无前轮记忆）\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU items）上发现约 27–29%（经非独立性校正后）的 items 在 2023 vs 2024 模型 cohort 间表现出显著的 temporal DIF。论文进一步证明 DIF 标记与 web-overlap 污染标签在统计上近乎正交（Jaccard = 0.206, φ = 0.012），提出 global exposure 与 differential functioning 是互补的诊断维度。跨六个 METABENCH benchmark 的复现（C% = 17.9%–31.3%）和 base-vs-instruct 机制分解（χ² = 562.7）增强了结论可信度。\n\n---\n\n## Strengths\n\n**S1. 规模与系统性 [共识]**：5,227 模型 × 12,508 items 的全矩阵分析在 LLM 评测领域属罕见规模。五种 cohort 设计（temporal、ability-quintile、matched-ability、within-family、random split）构成严谨的控制体系。鲁棒性检验密度（random-split 0.18%、DEFF 校正、graduated de-duplication、LOFO、cluster bootstrap）在该领域论文中罕见。\n\n**S2. DIF-contamination 正交性发现 [共识]**：Global exposure（web-overlap）与 differential functioning（DIF）的正交性（Jaccard = 0.206, OR = 1.05, φ = 0.012, permutation p = 0.88）有充分统计支撑，对理解 benchmark 质量问题的多维性有概念性贡献。\n\n**S3. Cross-subject matching 的 FPR 保证 [共识]**：Section 3.4 对单科目污染场景下 ΔFPR = 0 的构造性证明精巧，实证验证充分（5 个 MMLU domain 全部 ΔFPR = 0.000）。在 LLM 评测中具有独立方法论价值。\n\n**S4. 跨 benchmark 复现 [共识]**：六个 METABENCH benchmark 均表现出 temporal DIF（Table 3, 45–174× above random baseline），知识/推理类高于程序类的 pattern 合理，增强了结论普适性。\n\n**S5. Base-vs-instruct 反转 [共识]**：Section 5.1 展示 base 模型 60.1% reference-favoring（ρ = −0.570）vs instruct 模型 65.6% focal-favoring（ρ = −0.079, χ² = 562.7），有力证明 DIF 信号具有结构性，不是随机噪声。两位 reviewer 均认为这是论文最有洞察力的发现之一。\n\n**S6. 可复现性 [共识]**：分析代码匿名公开，METABENCH 数据公开可用，方法描述详尽，semi-synthetic 框架有清晰的伪代码级描述。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [Critical, 共识] Framing 根本性张力：\"temporal measurement instability\" 与 DIF 无法归因机制之间的矛盾**\n\n两位 reviewer 从不同角度独立得出相同结论：\n\n- **R1 角度（temporal confound）**：2023 vs 2024 cohort 在架构、训练范式、数据规模、能力水平上同时变化。在 LLM 场景下，不同代模型对不同 item 类型展现不同能力 profile 是*预期行为*——与教育测量中 DIF 预期为零的假设有本质区别。如果无法区分 legitimate capability evolution 与 genuine measurement dysfunction，DIF rate 作为 benchmark 质量指标的实践价值存疑。\n\n- **R2 角度（内部证据矛盾）**：论文自身提供的证据在反驳 \"instability\" 的负面含义——(a) 聚合排名几乎不受影响（ρ ≈ 0.997）；(b) DIF-flagged items 集中了最高区分度信号（z = −8 to −49）；(c) Appendix B 明确承认 DIF 可能反映真实能力演化。如果 DIF 反映的是 capability evolution，那么 \"instability\" 恰恰是基准测试正常工作的表现。\n\n- **实践含义的逻辑断裂**：论文从 \"detects what, not why\" 直接跳到 \"benchmarks need psychometric monitoring\"，但未讨论在不同机制假设下审计行动的后果截然不同（contamination → 移除 flagged items; capability evolution → 保留它们; composition shift → 修正 cohort 定义）。\n\n- **建议**：(a) 引入 Camilli & Shepard (1994) 的 impact vs bias 框架，区分 observed DIF 中哪些是 bias（真正的测量缺陷）、哪些是 impact（合法能力差异的 item 层面体现）；(b) 将 \"measurement instability\" 替换为更中性的术语（如 \"temporal differential item functioning\"），或更强力论证为什么即使来源于 capability evolution 它仍构成 \"instability\"（因为跨时间分数不可直接比较）；(c) 在 Section 5.2 中按不同机制场景分别讨论 DIF audit 的行动含义；(d) 将 Conclusion 中 \"benchmarks need psychometric monitoring\" 弱化为条件性陈述。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W2 [Warning, 共识] DEFF 估计范围过宽（simple-mean 29.2% vs weighted-mean 13.5%），首选估计论证不充分**\n\n2 倍差距直接影响读者对 benchmark 质量问题严重程度的判断。论文偏好 simple-mean 有一定论据（ICC flat across sizes ρ_s = −0.009; size-stratified ICC 0.246→0.082），R2 补充了领域特异性论据（LLM model family 非自然 population 随机抽样，weighted-mean 高估 mega-family 权重）。但论文将 13.5% 降级为 footnote-level 的 \"lower bound\" 而非并列呈现，透明度不足。\n\n建议：并列呈现两个估计，更强力论证 LLM 场景下 simple-mean 的合理性，展示 DEFF 敏感性分析（如移除最大 2-3 个 families 后的变化）。\n\n**W3 [Warning, 共识] 缺少 base/instruct composition shift 的直接控制**\n\n论文未报告 2023 和 2024 temporal cohort 中 base/instruct 模型的比例。Section 5.1 已证明 base 和 instruct 模型产生方向相反的 DIF pattern（χ² = 562.7），若 2024 cohort 中 instruct 比例更高，部分 \"temporal DIF\" 可能是 composition artifact。论文做了 ability matching 但 ability matching ≠ model-type matching。\n\n建议：补充 model-type-stratified temporal DIF 分析（仅在 base 模型中比较 2023 vs 2024，仅在 instruct 模型中比较 2023 vs 2024）。如果 within-type C% 仍显著高于 random baseline，则排除 composition shift 作为主要驱动因素。这个分析对论文 framing 至关重要且应简单易做。\n\n**W4 [Warning, 共识] Semi-synthetic 注入模型生态效度有限**\n\nBinary response flipping 是对真实污染的粗糙近似——真实污染是单向的（只提升正确率）、与 difficulty 相关的、基于 memorization 的。论文在 Limitations 和 Section 3.4 中已承认 \"upper-bound estimates\"，但 Section 4.5 标题 \"Semi-Synthetic Framework Validation\" 暗示了比实际更强的验证。Difficulty-dependent injection（Appendix B, Scheme D）部分缓解但未解决。\n\n建议：将 Section 4.5 标题调整为更审慎的表述（如 \"Detection Power under Controlled Injection\"）。\n\n**W5 [Warning, 分歧] \\enlargethispage 使用激进**\n\nexperiments.tex `\\enlargethispage*{4\\baselineskip}` + discussion.tex `\\enlargethispage*{6\\baselineskip}` 共增加约 10 行空间，加上 15 处 `\\looseness=-1/-2`。Page 8 异常密集（Section 4.7 + Table 3 + Section 5 两个小节 + Section 6 Conclusion）。\n\nR2 标 critical（可能实质性违反 8 页限制），R1 降为 should-fix（正文内容仍在第 8 页内，Limitations 不计入页数，\\enlargethispage 是常见排版技巧且 ARR CFP 未明确禁止）。**分歧未解决，取 warning。** 两位均同意 page 8 可读性受影响。\n\n建议：压缩 Section 4 中的冗余细节（如 DEFF 校正详细列举）移入 Appendix，将 \\enlargethispage 控制在 ≤2\\baselineskip。\n\n**W6 [Warning, 共识] 术语不一致**\n\n\"measurement instability\"、\"temporal DIF\"、\"temporal comparability\"、\"measurement invariance\"、\"measurement shift\" 在全文交替使用。Section 4.2 标题 \"Temporal Comparability: 31% Measurement Instability\" 在同一标题中包含两个术语。\n\n建议：选择一个核心术语一致使用，其他术语在首次出现时定义后不再交替。\n\n**W7 [Warning, 分歧] 方法论新颖性有限**\n\nR2 认为论文本质上是 \"application of existing methodology to a new domain\"。R1 反驳：DEFF 非独立性校正、cross-subject matching FPR 保证、semi-synthetic validation pipeline 是非平凡的领域适配，应定位为 \"methodological adaptation with domain-specific innovations\"。\n\n两位 reviewer 均同意对 EMNLP 应定位为 empirical contribution，论文应更坦诚地在 Introduction 中区分 \"采用已有方法\" 和 \"本文的方法论贡献\"。\n\n**W8 [Warning, 共识] Conclusion 过于简短**\n\n仅 4 句话（含 `\\looseness=-2`），未讨论 practical implications、future directions、DIF 结果对正在进行的基准设计改革（MMLU-Pro, BHI, Growing Pains）的具体启示。与论文的规模和深度不匹配。\n\n建议：扩展到至少 2 段，涵盖 practical implications 和 future directions。\n\n### Minor\n\n**N1 [Info, 共识] Abstract 信息密度过高**：至少 8 个具体数字（27–29%, 13.5%, [26.7%, 53.2%], 0.206, 0.012, 0.997 等），非 psychometrics 读者难以消化。建议保留 2-3 个关键数字。\n\n**N2 [Info, 分歧] \"两个维度\"正交性可能是预期结果**：Web-overlap（static, model-agnostic）和 DIF（dynamic, model-dependent）概念上就测量不同维度，低 Jaccard 可能是预期而非惊喜。R1 认为实证确认仍有增量贡献。建议调整贡献定位为 \"empirical confirmation of a theoretically expected but previously unverified distinction\"。\n\n**N3 [Info] AUROC = 0.603 描述不精确**：Appendix H 将 0.603 描述为 \"near chance\"，但 chance = 0.5。更准确的表述是 \"weak predictive power\"。\n\n**N4 [Info] Figure 1 caption 略有误导**：\"global contamination produces no DIF\" 未考虑 ceiling effect 场景。\n\n**N5 [Info] Cluster bootstrap CI 上界 53.2% 极宽**：由 Mistral/Llama-3 mega-family over-representation 导致的极端 resample，正文中应简要注释。\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 核心共识**（两位 reviewer 独立得出）：\n1. **Framing 问题是论文最大的弱点**：「measurement instability」的 claim 缺乏充分论证，temporal confound 未解决，实践建议的逻辑基础不足\n2. **规模和方法论系统性是主要优势**：5,227 模型 × 6 benchmarks 的全面分析令人印象深刻\n3. **DIF-contamination 正交性有贡献但可能被高估**\n4. **base-vs-instruct 反转是最有洞察力的发现**\n5. **Overall 3.5, Borderline Conference**\n6. **升分路径一致**：限定 claim + 补充 model-type-stratified 控制 + 分机制讨论 practical implications → 可达 4.0\n\n## Reviewer Divergence\n\n1. **\\enlargethispage 严重性**：R2 标 critical（可能违反页数限制），R1 降为 should-fix（排版技巧 vs 页数违规的界限；ARR 未明确禁止）。本报告取 warning。\n2. **方法论新颖性**：R2 认为 \"application of existing methodology\"，R1 认为 \"methodological adaptation with domain-specific innovations\"（DEFF + cross-subject matching + semi-synthetic pipeline）。\n3. **ETS C 阈值在大 N 下的适用性**：R1 标 should-fix，R2 反驳（论文已通过固定效应量阈值 + DEFF 校正 + threshold sensitivity 三层回应）。本报告采纳 R2 的反驳。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1 [Critical]**: 2023 和 2024 temporal cohort 中 base/instruct 模型的比例各是多少？是否做过 model-type-stratified temporal DIF（仅在 base 模型内或仅在 instruct 模型内比较 2023 vs 2024）？\n\n**Q2**: Section 5.1 报告 base 模型 N=1,409、instruct 模型 N=478，但 temporal cohort 总共只有 N=1,887。这些数字来自全部 5,227 模型还是仅 temporal cohort 的子集？\n\n**Q3**: 在 matched-ability 控制中（C% = 28.35%），matching 是 exact matching 还是 propensity score matching？caliper 选择的敏感性？\n\n**Q4**: DEFF 校正降幅仅 2pp（31.3% → 29.2%）——family structure 对 DIF 检测的实际影响是否很小？如果是，weighted-mean 给出 13.5% 的巨大差异如何解释？\n\n**Q5**: 论文推荐的 DIF audit protocol（Section 5.2）中，当 flagged 题目被标记后，具体应该采取什么行动（移除、降权、仅报告）？不同行动在不同 DIF 机制假设下的后果如何？\n\n**Q6**: Growing Pains (Habba et al., 2026) 的 anchor items 与本文的 stable items（non-DIF items）之间有多少重叠？\n\n**Q7**: Maeda (2025) 的工作是否属于将 DIF 应用于 LLM 评估的先例？与本文的区别是什么？\n\n---\n\n## Missing References\n\n1. **Camilli, G., & Shepard, L. A. (1994). Methods for Identifying Biased Test Items.** — DIF 领域经典教科书，impact vs bias 的区分直接回应 W1 的核心问题。两位 reviewer 均认为应引用。（需验证真实性）\n2. **Wainer, H. (1993). Differential Testlet Functioning.** — R1 提出但 R2 指出论文已引用 Wainer (1993) 作为 `wainer1993differential`。（已引用，无需补充）\n3. **Penfield, R. D., & Camilli, G. (2007).** — R1 提出但 R2 确认论文已引用为 `penfield2007dif`。（已引用，无需补充）\n4. **Population composition 对 DIF 的影响文献** — R2 提出，支撑 W3 的讨论。\n5. **Suk & Weiss (2026)** — 论文已引用但讨论不够深入，其 causal inference perspective 与本文的 \"DIF cannot attribute cause\" 限制直接相关。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（2026-05-23T07:56 → 07:59, 约 3 分钟）\n\n发现：\n- **[Warning] Pages 3-6 连续 4 页无 figure/table**（仅 page 4 有 2 个公式），Related Work → Method → Experiments 开头视觉单调。建议将 Table 1 或 Figure 2 提前至 page 5-6。\n- **[Info] Page 7 display items 过密**：Table 1 + Figure 2 + Table 2 三个 display items 挤在同一页，与前几页纯文本形成强烈反差。\n- **[Info] 正文共 5 个 display items**（2 figures + 3 tables），处于实证论文推荐范围 5-8 的下限。可考虑将 appendix 中高价值图表提升至正文。\n- **[Info] Page 1 完全无视觉元素**：如能在 page 1 底部放一个紧凑 teaser 可强化首页印象。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**置信度**: 4/5（两位 reviewer 独立评估高度一致，均熟悉 DIF 方法论和 LLM 评测文献）\n\n### 维度打分\n\n| 维度 | R1 | R2 | 综合 | 理由 |\n|------|----|----|------|------|\n| Soundness | 3.5 | 3.5 | 3.5 | MH-DIF 应用方法学上正确，鲁棒性检验全面，但 framing 与实际发现存在张力，composition shift 缺直接控制 |\n| Excitement | 3.5 | 3.0 | 3.0 | 话题及时重要，但核心是标准方法的领域迁移 + 大规模描述性分析；正交性可能是预期结果 |\n| Reproducibility | 4.0 | 4.0 | 4.0 | 代码和数据公开，方法描述详尽 |\n| Clarity | — | 3.5 | 3.5 | 整体写作质量高，但术语不一致、Abstract 过密、Conclusion 过简 |\n\n### 评分依据\n\n**接收理由**：(1) 规模空前的 psychometric audit（5,227 models × 6 benchmarks）；(2) global vs differential 框架和正交性实证有参考价值；(3) semi-synthetic 验证框架设计良好；(4) base-vs-instruct 反转是有洞察力的实证发现；(5) 鲁棒性检验极其全面。\n\n**不接收理由**：(1) 核心 framing \"temporal measurement instability\" 与 DIF 无法归因机制的限制存在未解决的根本张力；(2) 实践建议（psychometric monitoring）的有效性依赖于无法验证的机制假设；(3) 方法论新颖性有限（标准 MH-DIF 的领域应用）；(4) 缺少 model-type-stratified 控制排除 composition artifact。\n\n### 升分路径\n\n如果作者能：\n1. **[必做]** 修正 framing——将 \"measurement instability\" 退到更中性的术语，或更强力论证为什么 DIF（无论机制）都构成对跨时间比较的挑战\n2. **[必做]** 补充 model-type-stratified temporal DIF 分析排除 composition artifact\n3. **[必做]** 在 Discussion 中按不同机制场景分别讨论 DIF audit 的行动含义\n4. **[强烈建议]** 解决格式问题（\\enlargethispage ≤ 2\\baselineskip）\n5. **[强烈建议]** 扩展 Conclusion，精简 Abstract\n\n则论文可达 **4.0 (Conference)**。当前状态介于 Conference 和 Findings 之间。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 中 \"ΔFPR = 0 under single-subject contamination, k ≤ 5\" 已有条件限定（较 R13 有改善）\n- \"methodological and empirical, not algorithmic\" 的定位准确但 \"methodological\" 有些高估，建议改为 \"application and empirical\"\n- 缺少对 Camilli & Shepard (1994) impact vs bias 框架的引用\n\n### Section 3 (Method)\n- \"LLM-specific challenges\" 段落（第四点 multidimensionality）中 \"20% discordance\" 缺具体定义\n- MH-DIF 在 N=5,227 下 p < 0.05 几乎自动满足——论文已讨论此问题并通过 DEFF 恢复 p-value 选择性，处理合理\n\n### Section 4 (Experiments)\n- Section 4.2 信息密度极高，DEFF 校正详细列举可考虑移入 Appendix\n- Section 4.3 正交性结果可增加一句讨论为什么这是 informative 而非仅仅 expected\n- Section 4.5 标题 \"Semi-Synthetic Framework Validation\" 暗示比实际更强的验证\n\n### Section 5 (Discussion)\n- Section 5.1 的 base-vs-instruct 分解是论文亮点，但需补充两个 subgroup 在 2023/2024 中的比例\n- Section 5.2 audit protocol 的 actionability 取决于 DIF 机制——需分场景讨论\n\n### Section 6 (Conclusion)\n- 仅 4 句话，需扩展 practical implications 和 future directions\n\n### Limitations\n- 覆盖了 3 个关键弱点（semi-synthetic 生态效度、非独立性、cross-subject matching 边界）\n- 未提及 composition shift 作为局限\n\n### Appendix\n- Appendix B (Mechanism Analysis) 深度可嘉但明确无法解决机制归因问题\n- Appendix H AUROC = 0.603 应描述为 \"weak predictive power\" 而非 \"near chance\"",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 14 审稿报告\n\n**论文**: Temporal Measurement Instability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 (ARR)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 叙事/framing + 写作)\n**审稿模式**: Fresh（重新审稿，无前轮记忆）\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM 基准评测，在 METABENCH 数据集（5,227 模型 × 12,508 MMLU items）上发现约 27–29%（经非独立性校正后）的 items 在 2023 vs 2024 模型 cohort 间表现出显著的 temporal DIF。论文进一步证明 DIF 标记与 web-overlap 污染标签在统计上近乎正交（Jaccard = 0.206, φ = 0.012），提出 global exposure 与 differential functioning 是互补的诊断维度。跨六个 METABENCH benchmark 的复现（C% = 17.9%–31.3%）和 base-vs-instruct 机制分解（χ² = 562.7）增强了结论可信度。\n\n---\n\n## Strengths\n\n**S1. 规模与系统性 [共识]**：5,227 模型 × 12,508 items 的全矩阵分析在 LLM 评测领域属罕见规模。五种 cohort 设计（temporal、ability-quintile、matched-ability、within-family、random split）构成严谨的控制体系。鲁棒性检验密度（random-split 0.18%、DEFF 校正、graduated de-duplication、LOFO、cluster bootstrap）在该领域论文中罕见。\n\n**S2. DIF-contamination 正交性发现 [共识]**：Global exposure（web-overlap）与 differential functioning（DIF）的正交性（Jaccard = 0.206, OR = 1.05, φ = 0.012, permutation p = 0.88）有充分统计支撑，对理解 benchmark 质量问题的多维性有概念性贡献。\n\n**S3. Cross-subject matching 的 FPR 保证 [共识]**：Section 3.4 对单科目污染场景下 ΔFPR = 0 的构造性证明精巧，实证验证充分（5 个 MMLU domain 全部 ΔFPR = 0.000）。在 LLM 评测中具有独立方法论价值。\n\n**S4. 跨 benchmark 复现 [共识]**：六个 METABENCH benchmark 均表现出 temporal DIF（Table 3, 45–174× above random baseline），知识/推理类高于程序类的 pattern 合理，增强了结论普适性。\n\n**S5. Base-vs-instruct 反转 [共识]**：Section 5.1 展示 base 模型 60.1% reference-favoring（ρ = −0.570）vs instruct 模型 65.6% focal-favoring（ρ = −0.079, χ² = 562.7），有力证明 DIF 信号具有结构性，不是随机噪声。两位 reviewer 均认为这是论文最有洞察力的发现之一。\n\n**S6. 可复现性 [共识]**：分析代码匿名公开，METABENCH 数据公开可用，方法描述详尽，semi-synthetic 框架有清晰的伪代码级描述。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [Critical, 共识] Framing 根本性张力：\"temporal measurement instability\" 与 DIF 无法归因机制之间的矛盾**\n\n两位 reviewer 从不同角度独立得出相同结论：\n\n- **R1 角度（temporal confound）**：2023 vs 2024 cohort 在架构、训练范式、数据规模、能力水平上同时变化。在 LLM 场景下，不同代模型对不同 item 类型展现不同能力 profile 是*预期行为*——与教育测量中 DIF 预期为零的假设有本质区别。如果无法区分 legitimate capability evolution 与 genuine measurement dysfunction，DIF rate 作为 benchmark 质量指标的实践价值存疑。\n\n- **R2 角度（内部证据矛盾）**：论文自身提供的证据在反驳 \"instability\" 的负面含义——(a) 聚合排名几乎不受影响（ρ ≈ 0.997）；(b) DIF-flagged items 集中了最高区分度信号（z = −8 to −49）；(c) Appendix B 明确承认 DIF 可能反映真实能力演化。如果 DIF 反映的是 capability evolution，那么 \"instability\" 恰恰是基准测试正常工作的表现。\n\n- **实践含义的逻辑断裂**：论文从 \"detects what, not why\" 直接跳到 \"benchmarks need psychometric monitoring\"，但未讨论在不同机制假设下审计行动的后果截然不同（contamination → 移除 flagged items; capability evolution → 保留它们; composition shift → 修正 cohort 定义）。\n\n- **建议**：(a) 引入 Camilli & Shepard (1994) 的 impact vs bias 框架，区分 observed DIF 中哪些是 bias（真正的测量缺陷）、哪些是 impact（合法能力差异的 item 层面体现）；(b) 将 \"measurement instability\" 替换为更中性的术语（如 \"temporal differential item functioning\"），或更强力论证为什么即使来源于 capability evolution 它仍构成 \"instability\"（因为跨时间分数不可直接比较）；(c) 在 Section 5.2 中按不同机制场景分别讨论 DIF audit 的行动含义；(d) 将 Conclusion 中 \"benchmarks need psychometric monitoring\" 弱化为条件性陈述。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W2 [Warning, 共识] DEFF 估计范围过宽（simple-mean 29.2% vs weighted-mean 13.5%），首选估计论证不充分**\n\n2 倍差距直接影响读者对 benchmark 质量问题严重程度的判断。论文偏好 simple-mean 有一定论据（ICC flat across sizes ρ_s = −0.009; size-stratified ICC 0.246→0.082），R2 补充了领域特异性论据（LLM model family 非自然 population 随机抽样，weighted-mean 高估 mega-family 权重）。但论文将 13.5% 降级为 footnote-level 的 \"lower bound\" 而非并列呈现，透明度不足。\n\n建议：并列呈现两个估计，更强力论证 LLM 场景下 simple-mean 的合理性，展示 DEFF 敏感性分析（如移除最大 2-3 个 families 后的变化）。\n\n**W3 [Warning, 共识] 缺少 base/instruct composition shift 的直接控制**\n\n论文未报告 2023 和 2024 temporal cohort 中 base/instruct 模型的比例。Section 5.1 已证明 base 和 instruct 模型产生方向相反的 DIF pattern（χ² = 562.7），若 2024 cohort 中 instruct 比例更高，部分 \"temporal DIF\" 可能是 composition artifact。论文做了 ability matching 但 ability matching ≠ model-type matching。\n\n建议：补充 model-type-stratified temporal DIF 分析（仅在 base 模型中比较 2023 vs 2024，仅在 instruct 模型中比较 2023 vs 2024）。如果 within-type C% 仍显著高于 random baseline，则排除 composition shift 作为主要驱动因素。这个分析对论文 framing 至关重要且应简单易做。\n\n**W4 [Warning, 共识] Semi-synthetic 注入模型生态效度有限**\n\nBinary response flipping 是对真实污染的粗糙近似——真实污染是单向的（只提升正确率）、与 difficulty 相关的、基于 memorization 的。论文在 Limitations 和 Section 3.4 中已承认 \"upper-bound estimates\"，但 Section 4.5 标题 \"Semi-Synthetic Framework Validation\" 暗示了比实际更强的验证。Difficulty-dependent injection（Appendix B, Scheme D）部分缓解但未解决。\n\n建议：将 Section 4.5 标题调整为更审慎的表述（如 \"Detection Power under Controlled Injection\"）。\n\n**W5 [Warning, 分歧] \\enlargethispage 使用激进**\n\nexperiments.tex `\\enlargethispage*{4\\baselineskip}` + discussion.tex `\\enlargethispage*{6\\baselineskip}` 共增加约 10 行空间，加上 15 处 `\\looseness=-1/-2`。Page 8 异常密集（Section 4.7 + Table 3 + Section 5 两个小节 + Section 6 Conclusion）。\n\nR2 标 critical（可能实质性违反 8 页限制），R1 降为 should-fix（正文内容仍在第 8 页内，Limitations 不计入页数，\\enlargethispage 是常见排版技巧且 ARR CFP 未明确禁止）。**分歧未解决，取 warning。** 两位均同意 page 8 可读性受影响。\n\n建议：压缩 Section 4 中的冗余细节（如 DEFF 校正详细列举）移入 Appendix，将 \\enlargethispage 控制在 ≤2\\baselineskip。\n\n**W6 [Warning, 共识] 术语不一致**\n\n\"measurement instability\"、\"temporal DIF\"、\"temporal comparability\"、\"measurement invariance\"、\"measurement shift\" 在全文交替使用。Section 4.2 标题 \"Temporal Comparability: 31% Measurement Instability\" 在同一标题中包含两个术语。\n\n建议：选择一个核心术语一致使用，其他术语在首次出现时定义后不再交替。\n\n**W7 [Warning, 分歧] 方法论新颖性有限**\n\nR2 认为论文本质上是 \"application of existing methodology to a new domain\"。R1 反驳：DEFF 非独立性校正、cross-subject matching FPR 保证、semi-synthetic validation pipeline 是非平凡的领域适配，应定位为 \"methodological adaptation with domain-specific innovations\"。\n\n两位 reviewer 均同意对 EMNLP 应定位为 empirical contribution，论文应更坦诚地在 Introduction 中区分 \"采用已有方法\" 和 \"本文的方法论贡献\"。\n\n**W8 [Warning, 共识] Conclusion 过于简短**\n\n仅 4 句话（含 `\\looseness=-2`），未讨论 practical implications、future directions、DIF 结果对正在进行的基准设计改革（MMLU-Pro, BHI, Growing Pains）的具体启示。与论文的规模和深度不匹配。\n\n建议：扩展到至少 2 段，涵盖 practical implications 和 future directions。\n\n### Minor\n\n**N1 [Info, 共识] Abstract 信息密度过高**：至少 8 个具体数字（27–29%, 13.5%, [26.7%, 53.2%], 0.206, 0.012, 0.997 等），非 psychometrics 读者难以消化。建议保留 2-3 个关键数字。\n\n**N2 [Info, 分歧] \"两个维度\"正交性可能是预期结果**：Web-overlap（static, model-agnostic）和 DIF（dynamic, model-dependent）概念上就测量不同维度，低 Jaccard 可能是预期而非惊喜。R1 认为实证确认仍有增量贡献。建议调整贡献定位为 \"empirical confirmation of a theoretically expected but previously unverified distinction\"。\n\n**N3 [Info] AUROC = 0.603 描述不精确**：Appendix H 将 0.603 描述为 \"near chance\"，但 chance = 0.5。更准确的表述是 \"weak predictive power\"。\n\n**N4 [Info] Figure 1 caption 略有误导**：\"global contamination produces no DIF\" 未考虑 ceiling effect 场景。\n\n**N5 [Info] Cluster bootstrap CI 上界 53.2% 极宽**：由 Mistral/Llama-3 mega-family over-representation 导致的极端 resample，正文中应简要注释。\n\n---\n\n## Reviewer Consensus\n\n**[AGREE] 核心共识**（两位 reviewer 独立得出）：\n1. **Framing 问题是论文最大的弱点**：「measurement instability」的 claim 缺乏充分论证，temporal confound 未解决，实践建议的逻辑基础不足\n2. **规模和方法论系统性是主要优势**：5,227 模型 × 6 benchmarks 的全面分析令人印象深刻\n3. **DIF-contamination 正交性有贡献但可能被高估**\n4. **base-vs-instruct 反转是最有洞察力的发现**\n5. **Overall 3.5, Borderline Conference**\n6. **升分路径一致**：限定 claim + 补充 model-type-stratified 控制 + 分机制讨论 practical implications → 可达 4.0\n\n## Reviewer Divergence\n\n1. **\\enlargethispage 严重性**：R2 标 critical（可能违反页数限制），R1 降为 should-fix（排版技巧 vs 页数违规的界限；ARR 未明确禁止）。本报告取 warning。\n2. **方法论新颖性**：R2 认为 \"application of existing methodology\"，R1 认为 \"methodological adaptation with domain-specific innovations\"（DEFF + cross-subject matching + semi-synthetic pipeline）。\n3. **ETS C 阈值在大 N 下的适用性**：R1 标 should-fix，R2 反驳（论文已通过固定效应量阈值 + DEFF 校正 + threshold sensitivity 三层回应）。本报告采纳 R2 的反驳。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1 [Critical]**: 2023 和 2024 temporal cohort 中 base/instruct 模型的比例各是多少？是否做过 model-type-stratified temporal DIF（仅在 base 模型内或仅在 instruct 模型内比较 2023 vs 2024）？\n\n**Q2**: Section 5.1 报告 base 模型 N=1,409、instruct 模型 N=478，但 temporal cohort 总共只有 N=1,887。这些数字来自全部 5,227 模型还是仅 temporal cohort 的子集？\n\n**Q3**: 在 matched-ability 控制中（C% = 28.35%），matching 是 exact matching 还是 propensity score matching？caliper 选择的敏感性？\n\n**Q4**: DEFF 校正降幅仅 2pp（31.3% → 29.2%）——family structure 对 DIF 检测的实际影响是否很小？如果是，weighted-mean 给出 13.5% 的巨大差异如何解释？\n\n**Q5**: 论文推荐的 DIF audit protocol（Section 5.2）中，当 flagged 题目被标记后，具体应该采取什么行动（移除、降权、仅报告）？不同行动在不同 DIF 机制假设下的后果如何？\n\n**Q6**: Growing Pains (Habba et al., 2026) 的 anchor items 与本文的 stable items（non-DIF items）之间有多少重叠？\n\n**Q7**: Maeda (2025) 的工作是否属于将 DIF 应用于 LLM 评估的先例？与本文的区别是什么？\n\n---\n\n## Missing References\n\n1. **Camilli, G., & Shepard, L. A. (1994). Methods for Identifying Biased Test Items.** — DIF 领域经典教科书，impact vs bias 的区分直接回应 W1 的核心问题。两位 reviewer 均认为应引用。（需验证真实性）\n2. **Wainer, H. (1993). Differential Testlet Functioning.** — R1 提出但 R2 指出论文已引用 Wainer (1993) 作为 `wainer1993differential`。（已引用，无需补充）\n3. **Penfield, R. D., & Camilli, G. (2007).** — R1 提出但 R2 确认论文已引用为 `penfield2007dif`。（已引用，无需补充）\n4. **Population composition 对 DIF 的影响文献** — R2 提出，支撑 W3 的讨论。\n5. **Suk & Weiss (2026)** — 论文已引用但讨论不够深入，其 causal inference perspective 与本文的 \"DIF cannot attribute cause\" 限制直接相关。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**已完成**（2026-05-23T07:56 → 07:59, 约 3 分钟）\n\n发现：\n- **[Warning] Pages 3-6 连续 4 页无 figure/table**（仅 page 4 有 2 个公式），Related Work → Method → Experiments 开头视觉单调。建议将 Table 1 或 Figure 2 提前至 page 5-6。\n- **[Info] Page 7 display items 过密**：Table 1 + Figure 2 + Table 2 三个 display items 挤在同一页，与前几页纯文本形成强烈反差。\n- **[Info] 正文共 5 个 display items**（2 figures + 3 tables），处于实证论文推荐范围 5-8 的下限。可考虑将 appendix 中高价值图表提升至正文。\n- **[Info] Page 1 完全无视觉元素**：如能在 page 1 底部放一个紧凑 teaser 可强化首页印象。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 — Borderline Conference**\n\n**置信度**: 4/5（两位 reviewer 独立评估高度一致，均熟悉 DIF 方法论和 LLM 评测文献）\n\n### 维度打分\n\n| 维度 | R1 | R2 | 综合 | 理由 |\n|------|----|----|------|------|\n| Soundness | 3.5 | 3.5 | 3.5 | MH-DIF 应用方法学上正确，鲁棒性检验全面，但 framing 与实际发现存在张力，composition shift 缺直接控制 |\n| Excitement | 3.5 | 3.0 | 3.0 | 话题及时重要，但核心是标准方法的领域迁移 + 大规模描述性分析；正交性可能是预期结果 |\n| Reproducibility | 4.0 | 4.0 | 4.0 | 代码和数据公开，方法描述详尽 |\n| Clarity | — | 3.5 | 3.5 | 整体写作质量高，但术语不一致、Abstract 过密、Conclusion 过简 |\n\n### 评分依据\n\n**接收理由**：(1) 规模空前的 psychometric audit（5,227 models × 6 benchmarks）；(2) global vs differential 框架和正交性实证有参考价值；(3) semi-synthetic 验证框架设计良好；(4) base-vs-instruct 反转是有洞察力的实证发现；(5) 鲁棒性检验极其全面。\n\n**不接收理由**：(1) 核心 framing \"temporal measurement instability\" 与 DIF 无法归因机制的限制存在未解决的根本张力；(2) 实践建议（psychometric monitoring）的有效性依赖于无法验证的机制假设；(3) 方法论新颖性有限（标准 MH-DIF 的领域应用）；(4) 缺少 model-type-stratified 控制排除 composition artifact。\n\n### 升分路径\n\n如果作者能：\n1. **[必做]** 修正 framing——将 \"measurement instability\" 退到更中性的术语，或更强力论证为什么 DIF（无论机制）都构成对跨时间比较的挑战\n2. **[必做]** 补充 model-type-stratified temporal DIF 分析排除 composition artifact\n3. **[必做]** 在 Discussion 中按不同机制场景分别讨论 DIF audit 的行动含义\n4. **[强烈建议]** 解决格式问题（\\enlargethispage ≤ 2\\baselineskip）\n5. **[强烈建议]** 扩展 Conclusion，精简 Abstract\n\n则论文可达 **4.0 (Conference)**。当前状态介于 Conference 和 Findings 之间。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- Contribution 2 中 \"ΔFPR = 0 under single-subject contamination, k ≤ 5\" 已有条件限定（较 R13 有改善）\n- \"methodological and empirical, not algorithmic\" 的定位准确但 \"methodological\" 有些高估，建议改为 \"application and empirical\"\n- 缺少对 Camilli & Shepard (1994) impact vs bias 框架的引用\n\n### Section 3 (Method)\n- \"LLM-specific challenges\" 段落（第四点 multidimensionality）中 \"20% discordance\" 缺具体定义\n- MH-DIF 在 N=5,227 下 p < 0.05 几乎自动满足——论文已讨论此问题并通过 DEFF 恢复 p-value 选择性，处理合理\n\n### Section 4 (Experiments)\n- Section 4.2 信息密度极高，DEFF 校正详细列举可考虑移入 Appendix\n- Section 4.3 正交性结果可增加一句讨论为什么这是 informative 而非仅仅 expected\n- Section 4.5 标题 \"Semi-Synthetic Framework Validation\" 暗示比实际更强的验证\n\n### Section 5 (Discussion)\n- Section 5.1 的 base-vs-instruct 分解是论文亮点，但需补充两个 subgroup 在 2023/2024 中的比例\n- Section 5.2 audit protocol 的 actionability 取决于 DIF 机制——需分场景讨论\n\n### Section 6 (Conclusion)\n- 仅 4 句话，需扩展 practical implications 和 future directions\n\n### Limitations\n- 覆盖了 3 个关键弱点（semi-synthetic 生态效度、非独立性、cross-subject matching 边界）\n- 未提及 composition shift 作为局限\n\n### Appendix\n- Appendix B (Mechanism Analysis) 深度可嘉但明确无法解决机制归因问题\n- Appendix H AUROC = 0.603 应描述为 \"weak predictive power\" 而非 \"near chance\"",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1324 · 2026-05-23T08:14:35.831408+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 6138
}
```

</details>

---


### Assistant

_source line 1325 · 2026-05-23T08:14:45.152956+00:00_

审稿报告已投递至 Research Director。

---

**Round 14 审稿完成。** 核心结论：

- **Overall: 3.5 (Borderline Conference)**，两位 Reviewer 独立评估完全一致
- **1 个 Critical**：Framing 根本性张力——"temporal measurement instability" 与 DIF 无法归因机制之间的矛盾是论文最大的弱点
- **7 个 Warning**：DEFF 范围过宽、缺 base/instruct composition 控制、semi-synthetic 生态效度、\enlargethispage 激进、术语不一致、方法论新颖性有限、Conclusion 过短
- **5 个 Info**：Abstract 过密、正交性预期性、AUROC 描述不精确等
- **升分路径明确**：修正 framing + 补 model-type-stratified DIF + 分机制讨论行动含义 + 解决格式 → 4.0 (Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 132

## Round 132

2 recorded events


### User

_source line 1326 · 2026-05-23T08:14:45.158883+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应

---

### Strengths 部分

R1 的 S1–S7 与我的评估高度一致。我的 S1–S6 覆盖了相同的优点。特别补充一点：R1 单独列出 S7（Appendix B 机制分析有深度），我同意这是论文的亮点之一——mixed-mechanism injection（Scheme D）能复现 difficulty-direction gradient 和 base-vs-instruct reversal，但无法匹配 instruct gradient 的幅度（simulated ρ = −0.302 vs observed −0.079），这为 non-contamination mechanism 提供了有价值的约束。

---

### Weaknesses 逐条回应

**[AGREE] R1-W-M1: 时序混淆是论文最大的解释性缺口**

强烈同意，这与我的 W-F1 和 W-F2 高度一致。R1 的论证角度比我更精确：教育测量中 DIF 的 null expectation 是零（同一课程体系、同一考试，不同人群应表现一致），但 LLM 跨代模型在架构、训练范式、数据规模上的系统性差异意味着 DIF ≠ 0 可能是 *预期* 行为而非异常。论文未充分讨论这一根本性差异。

R1 建议引入 Camilli and Shepard (1994) 的 impact vs bias 区分框架，我认为这是一个非常有建设性的建议。当前论文将所有 DIF 等价地视为 "instability"，但 impact（能力差异导致的表现差异）和 bias（真正的测量偏差）在 DIF 文献中有明确区分。论文的 ability matching（Section 4.2, Cohen's d = −0.17）部分控制了 impact，但未使用这个经典框架来组织讨论。

我想补充 R1 未提到的一点：**composition shift 是时序混淆的一个具体表现形式**。Section 5.1 报告 base 模型 N=1,409 和 instruct 模型 N=478，但论文未报告这些模型在 2023 vs 2024 cohort 中的分布。如果 2024 cohort 的 instruct 比例显著高于 2023，则部分 temporal DIF 可能纯粹是 composition artifact。这比 R1 讨论的一般性时序混淆更具体、更可验证，也更容易修复（补充 model-type-stratified analysis 即可）。

**[AGREE with nuance] R1-W-M2: DEFF 估计范围过宽**

部分同意。R1 指出 simple-mean 29.2% vs weighted-mean 13.5% 的 2× 差距确实很大，且论文对首选 simple-mean 的论证不够充分。

但我对 R1 的具体批评有一个补充：论文实际上提供了选择 simple-mean 的实证理由——Section 4.2 和 Appendix I 报告 ICC 与 family size 的 Spearman ρ = −0.009（p = 0.96），且 size-stratified ICC 从小家族的 0.246 下降到大家族的 0.082（Table 9/Appendix C）。这意味着 Kish (1965) 的 weighted-mean 公式的核心假设（所有 cluster 具有相同的 ICC）在此处不成立——大家族（Mistral, Llama-3）内部异质性远高于小家族，weighted-mean 过度惩罚了这些家族。论文的论证方向是正确的，但展示方式不够清晰。

R1 建议并列呈现两个估计——论文已经做到了（Section 4.2: "with 13.5% as a lower bound under weighted-mean DEFF"），但可以更突出地以表格形式呈现。我建议作者在正文中增加一句话：明确说明 weighted-mean DEFF 假设 ICC 恒定，但实证 data 表明这一假设不成立，因此 simple-mean 是更合适的首选估计。

**[AGREE] R1-W-M3: Semi-synthetic 注入模型生态效度有限**

同意。Binary response flipping 是 worst-case uniform injection，与真实污染模式（单向、difficulty-dependent、partial memorization）差距较大。论文在 Limitations 第 (1) 点承认了这一点，但正文中的 ΔTPR 值（+0.508 at p=0.5）被当作 detection power 的证据来使用，未充分标注其为 upper-bound estimate。

不过，我要指出论文中有一个 R1 可能忽略的细节：Section 3.4 的 difficulty-dependent injection 实验（Appendix B）部分回应了这一担忧——它展示了不同注入模式产生可区分的 ρ signature（capability-like: +0.77 vs contamination-like: −0.52），但论文承认 "mapping to real-data mechanisms requires further work"。这个方向有价值，但目前不足以完全解决生态效度问题。

**[AGREE] R1-W-E1: ETS C 阈值在 N=5,227 下的适用性**

同意这是一个值得讨论的问题。论文在 Section 3.2 已经指出："At N = 5,227, significance (p < 0.05) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5: only 3 of 3,918 C items lack significance"。这意味着在如此大的 N 下，双重阈值（effect size + significance）实质上退化为单一 effect-size 阈值。

但我认为 R1 的批评方向可以更精确：问题不是阈值 *本身* 是否合适（|Δ_MH| ≥ 1.5 是 effect-size 标准，理论上不依赖 N），而是在大 N 下 MH Δ_MH 的估计精度提高，更多 items 的真实 Δ_MH 可能在 1.5 附近被精确捕获——但这些 borderline items 的 DIF 实际意义可能有限。论文报告了 threshold sensitivity（Section 4.2: 18.3% at ≥ 2.0, 10.2% at ≥ 2.5），这部分回应了 R1 的担忧，但确实可以更明确地讨论 effect-size threshold 在 LLM 评估场景下的实际意义。

DEFF 校正也部分回应了这个问题：调整后的有效 N 远小于 5,227，恢复了 p-value 的筛选作用（Section 3.2: "269 items (6.9%) lose significance"）。

**[AGREE] R1-W-E2: Within-family 分析的 generalizability**

同意。论文主要展示了 Llama-2 vs Llama-3（C% = 61.3%）和 LOFO 分析中的 Mistral，这些都是代际差异最大的家族。对于代际变化较小的家族（如 Solar 系列、Phi 系列），within-family DIF 是否同样存在？如果小代际差异的 family 内 DIF 信号较弱，这反而支持 DIF 主要反映 legitimate capability evolution 而非 measurement dysfunction 的解释——进一步强化 R1-W-M1 的论点。

**[REBUT] R1-W-S1: 关键统计量缺少不确定性度量**

部分反驳。R1 声称 "DEFF 估计、Jaccard、Appendix B 的 OR 均未报告 CI 或标准误"，但论文实际上提供了多项不确定性度量：
- Jaccard：Section 4.3 报告 permutation null [0.203, 0.222]，p = 0.88
- Enrichment ratio：bootstrap 95% CI [0.94, 1.02]（Section 4.3）
- OR：Section 4.3 报告 OR = 1.05 [0.96, 1.15]
- C%：bootstrap 95% CI [29.4%, 38.1%]（Section 4.2）和 cluster bootstrap [26.7%, 53.2%]
- Semi-synthetic ΔTPR/ΔFPR：5 random seeds 的标准差（Table 7, Table 11）
- LOFO：Table 8 显示各 family removal 后的 C% 变化

不过 R1 在 DEFF 估计的 CI 方面有道理——论文给出了 simple-mean DEFF = 3.87 和 weighted-mean DEFF = 12.79，但没有报告 DEFF 本身的不确定性（item-level DEFF 的分布特征在 Appendix C 有 mean/median/Q3/max，但不是 bootstrap CI）。这一点可以改进。

**[AGREE] R1-W-S2: 多重比较处理透明度**

同意这是一个 minor 问题。论文在 Section 3.4 解释了不使用 family-wise correction 的理由（"Following DIF convention, we do not apply family-wise error correction: the dual ETS C threshold guards against false positives; BH-FDR at q = 0.05 reclassifies only 3 of 3,918 C items"），但 Section 4.4 的 logistic regression p-values "not adjusted for clustering" 以及 Appendix B 的多个 p-values 的处理方式不一致。不影响核心结论，但应统一处理。

**[AGREE] R1-W-M4: "Measurement instability" 概念操作化定义不够明确**

同意，这与我的 W-F1 实质相同。MH-DIF 是 observed-score 方法，检测的是条件独立性违反（given ability level, item response 与 group membership 不独立），而 "measurement instability" 暗示的是更强的理论概念（measurement instrument 随时间失效）。用后者标签前者是一个 inferential leap。

---

### Questions 回应

**R1-Q1 (Matched-ability matching 质量)**: 论文在 Section 4.2 和 Appendix A 报告了 nearest-neighbor matching 的 caliper (0.02 normalized accuracy ≈ 0.14 SD) 和 Cohen's d = −0.17。这是合理的，但 R1 问的 "matching 方法" 更广泛——确实可以补充 propensity score matching 或其他方法的敏感性分析。

**R1-Q2 (Jaccard 被覆盖率稀释)**: 这是一个好问题。Li et al. 的 web-overlap labels 覆盖 73.8% (9,229/12,508) 的 items。Jaccard 在 9,229 items 上计算为 0.206，但如果剩余 26.2% 的 items 存在系统性偏差（例如大部分是 web-contaminated），Jaccard 可能被低估。不过论文在 Section 4.3 报告 C% 在 web-contaminated (30.7%) 和 clean (31.8%) items 之间几乎相同，这强化了正交性结论——即使在已标注的子集内也成立。

**R1-Q3 (DEFF 校正降幅)**: R1 观察到 simple-mean DEFF 仅将 C% 从 31.3% 降至 29.2%（2pp），问 family structure 实际影响是否很小。这个观察是正确的——Mean ICC = 0.047（Appendix C）表明 family 内相似性较低。weighted-mean 差异大是因为 Kish 公式使用 weighted cluster size（254.5 vs 62.8），受 Mistral (547) 和 Llama-3 (315) 两个 mega-family 主导。论文的 Appendix I 已经展示这两个 mega-family 的 ICC 最低（0.082），所以 weighted-mean 对它们的过度加权是不合理的。我认为论文在这点上的论证方向正确，但展示不够清晰。

**R1-Q4 (AUROC = 0.603)**: R1 问这支持还是反对 DIF 作为 measurement quality indicator。我认为这是一个双刃剑：low AUROC 说明 DIF 不可从 item properties 预测（即不是 fixed item defect），这支持 "DIF reflects emergent cohort-item interactions"（Appendix H 的结论）。但同时也意味着 DIF 无法用于 prospective screening——只能 post-hoc detection，降低了实践价值。

**R1-Q5 (C% 差异与 item 特征)**: Section 4.7 报告 knowledge/reasoning benchmarks (C% 26.9–31.3%) 高于 procedural ones (17.9–18.9%)，但论文仅 "treat them as descriptive"。系统性分析（例如 item difficulty distribution, answer-option structure, question length）的确缺乏。

---

### Missing References 回应

**[AGREE] Camilli & Shepard (1994)**: 强烈同意应该引用。impact vs bias 的经典区分框架直接相关——论文当前将所有 DIF 等价处理，忽略了这一基本区分。

**[AGREE with caveat] Penfield & Camilli (2007)**: 论文已引用 penfield2007dif（Section 2: "Penfield and Camilli (2007) provide comprehensive reviews"）。R1 可能在阅读时漏看了这一引用。

**[AGREE] Wainer (1993)**: 论文引用了 wainer1993differential（Section 3.4: "Following DIF convention (Wainer and Braun, 1993)"），但仅用于 error correction convention。R1 建议从 Differential Testlet Functioning 角度讨论非独立性——这是一个有价值的补充，因为 MMLU 的 57 subjects 可以类比为 testlets。

---

### 与我的审稿意见的交叉比较

**高度一致的问题**:
1. R1-W-M1 ≈ 我的 W-F1 + W-F2：时序混淆 / DIF 无法归因 / framing 过度承诺。这是两位 reviewer 共同的 top concern。
2. R1-W-M4 ≈ 我的 W-F1：术语问题（measurement instability 标签 vs observed-score DIF 方法）。
3. R1-W-M3 部分对应我的审稿中未单独列出但在 S3 中提到的 semi-synthetic 局限性。

**R1 关注但我较少关注的问题**:
1. R1-W-M2（DEFF 范围过宽）——我在正文中未单独作为 weakness 列出，但在 Minor-1 中提到了 cluster bootstrap CI 上界过宽。R1 的分析更深入。
2. R1-W-E1（ETS C 阈值在大 N 下的适用性）——我未覆盖这一点，同意这是一个 valid concern。
3. R1-W-S1（不确定性度量）——我未覆盖，但如上所述论文实际上提供了部分 CI。

**我关注但 R1 较少关注的问题**:
1. 我的 W-C1（\enlargethispage 格式问题）——R1 未提及，但我认为这是一个 Must-Fix 级别的格式合规问题。
2. 我的 W-F3（缺少 base-vs-instruct composition shift 控制）——R1 在 W-M1 中隐含提到但未具体化。
3. 我的 W-W2/W-W3（Abstract 过密、Conclusion 过简）——R1 未涉及写作质量问题。
4. 我的 W-N2（正交性可能是预期结果）——R1 在 S4 中将正交性视为贡献，但我认为其新颖性可能被高估。

**总体评分一致**: 两位 reviewer 均给出 3.5（Borderline Conference），且均认为修复 framing + 补充 composition 控制后可升至 4.0。这种一致性增强了评审的可信度。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。两位 Reviewer 的核心关切高度一致：时序混淆/DIF 无法归因是共同的 top concern（R1-W-M1 ≈ 我的 W-F1+W-F2），总评分均为 3.5。主要差异在于我额外关注了格式合规（\enlargethispage）、composition shift 控制、写作问题和正交性新颖性，而 R1 更深入地分析了 DEFF 范围和 ETS 阈值适用性问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1327 · 2026-05-23T08:15:12.531130+00:00_

R2 交叉回应已收到。报告已提交，R2 的详细回应与报告中的共识分析完全一致，无需修订。

**审稿流程完成总结**：

- **Round 1 独立审稿** → 两位 Reviewer 均给出 3.5 (Borderline Conference)
- **交叉分享** → 核心问题高度一致，仅在 \enlargethispage 严重性和方法论新颖性评估上有分歧
- **收敛判断** → 关键问题已达成共识，无需第 2 轮
- **报告已投递** → Overall 3.5, 升分路径明确（修正 framing + 补充 model-type-stratified 控制 + 分机制讨论行动含义 → 4.0）
- **Issue Tracker 已更新** → 10 个 R14 新条目 + 8 个 R13 历史条目状态同步

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 133

## Round 133

74 recorded events


### User

_source line 1328 · 2026-05-23T09:08:15.443788+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main/Findings unified)
- 截止日期: 2025-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1329 · 2026-05-23T09:08:20.528484+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1330 · 2026-05-23T09:08:20.579647+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1331 · 2026-05-23T09:08:29.266579+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1332 · 2026-05-23T09:08:29.267029+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1333 · 2026-05-23T09:08:31.325511+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_get_project_overview",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_get_project_overview",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1334 · 2026-05-23T09:08:31.325965+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1335 · 2026-05-23T09:08:34.136879+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1336 · 2026-05-23T09:08:34.137333+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1337 · 2026-05-23T09:08:35.793842+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "dispatch_visual_check",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "dispatch_visual_check",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1338 · 2026-05-23T09:08:35.844802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1339 · 2026-05-23T09:08:37.953305+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1340 · 2026-05-23T09:08:37.953650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1341 · 2026-05-23T09:08:38.355615+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1342 · 2026-05-23T09:08:38.356394+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1343 · 2026-05-23T09:08:38.858494+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update_review_issues",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update_review_issues",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1344 · 2026-05-23T09:08:38.858866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1345 · 2026-05-23T09:08:39.361020+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1346 · 2026-05-23T09:08:39.361365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1347 · 2026-05-23T09:08:39.813584+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1348 · 2026-05-23T09:08:39.813964+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1349 · 2026-05-23T09:08:40.265774+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "request_external_review",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "request_external_review",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1350 · 2026-05-23T09:08:40.266221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1351 · 2026-05-23T09:08:40.617696+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_project_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1352 · 2026-05-23T09:08:40.670466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1353 · 2026-05-23T09:08:44.937142+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1354 · 2026-05-23T09:08:45.439777+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1355 · 2026-05-23T09:08:45.942282+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1356 · 2026-05-23T09:08:45.942662+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1357 · 2026-05-23T09:08:47.348171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1358 · 2026-05-23T09:08:47.401897+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Temporal Score Incomparability in LLM Benchmarks:\\A Large-Scale Psychometric Audit of 5,227 Models}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 1359 · 2026-05-23T09:09:04.672304+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2025 2026 call for papers submission guidelines page limit",
  "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2025 2026 call for papers submission guidelines page limit",
    "allowed_domains": "['aclweb.org', 'openreview.net', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-23T09:09:04.773090+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool call

_source line 1361 · 2026-05-23T09:09:06.581242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-23T09:09:06.782677+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-23T09:09:11.201863+00:00_

Web search results for query: "ACL Rolling Review 2025 2026 call for papers submission guidelines page limit"

Links: [{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, here's the information about ACL Rolling Review 2025-2026 submission guidelines and page limits:

## Page Limits

Long papers may consist of up to 8 pages of content, and short papers may consist of up to 4 pages of content, plus unlimited references and appendices.

Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Key Submission Guidelines

- All long, short, and theme papers must follow the ACL Author Guidelines
- All submitted papers are expected to use the official ACL style template
- All submitted papers are expected to describe original, completed and unpublished work
- The limitations section, the optional et
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6529
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-23T09:09:11.353306+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (21 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_035_q3_inflation_sim** (success): plan_013 发现 11.3% within-subject item pairs |Q3|>0.20，存在局部依赖(LD)。MH-DIF 假设局部独立，LD 可能膨胀 Type I error。通过 Monte Carlo 模拟或 within-subject permutation null（保持 Q3 结构），量化 LD 对 MH-DIF FPR 的实际膨胀程度。预测：校准 LD 后实际 FPR 膨胀 <3pp（从 nominal 5% 到 <8%），因为 LD 温和（mean Q3=0.009）且 MH 的 total-score stratification 部分吸收了 LD 效应。 ← 基于 plan_013_q3_local_independence\n- **plan_036_growing_pains_lookup** (success): Growing Pains LLM benchmark paper 使用 FPC (Focal Point Contamination) anchor items 来检测污染。如果 FPC anchor item list 公开可得，与我们的 DIF C-flagged items 计算 Jaccard overlap 和 enrichment ratio。如果有显著 overlap (enrichment>2)，则 DIF 与 FPC 检测互补；如果无 overlap (enrichment≈1)，则证明 DIF 和 FPC 捕捉不同信号维度。 ← 基于 plan_001_real_data_dif_mmlu\n  [plan_036_rep
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 6580
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-23T09:09:11.353749+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. We apply differential item functioning (DIF) analysis from educational measurement to six METABENCH benchmarks (5,227 MMLU models, 27,125 items across all six), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF (${\approx}$27--29\% for MMLU after non-independence corrections; random-split baseline 0.18\%). Web-overlap contamination labels are near-independent of DIF flags (Jaccard $= 0.206$): global exposure and differential functioning are complementary diagnostic dimensions. Temporal DIF does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals structured item-level change---base and instruct models exhibit opposite DIF patterns ($\chi^2 = 562.7$)---and shifts DIF-corrected scores by ${+}2.12$\,pp on average. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 4772
}
```

</details>

---


### Tool result

_source line 1366 · 2026-05-23T09:09:11.354021+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal score incomparability} as the empirical phenomenon when DIF is detected across time-defined cohorts---scores are not directly comparable across cohorts because item measurement properties differ systematically, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.18\% under a random-split control. Aggregate rankings are robust ($\rho \approx 0.997$), but absolute scores are not directly comparable: DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with individual models displaced by up to 849 rank positions. The incomparability is diagnostic, revealing which capability dimensions shift across model generations.
5	
6	Existing approaches to benchmark integrity focus on \emph{global exposure}---whether items appear in training corpora---through membership inference~\citep{shi2024mink} and performance-based detection~\citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique}, validated a
…[truncated 3613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 4571
}
```

</details>

---


### Tool call

_source line 1367 · 2026-05-23T09:09:18.145676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1368 · 2026-05-23T09:09:18.949529+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues and \citet{oren2024proving} prove contamination through exchangeability tests. Performance-based detectors identify contamination through statistical anomalies \citep{dekoninck2024constat,liang2026dvd,tao2026selfcritique,deng2024investigating}. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (\Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrat
…[truncated 4780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1369 · 2026-05-23T09:09:19.150741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1370 · 2026-05-23T09:09:19.452453+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 9746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1371 · 2026-05-23T09:09:19.553854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1372 · 2026-05-23T09:09:19.956074+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80 and AUC of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal DIF: 31\% of Items Exhibit Differential Functioning}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Non-independence corrections---simple-mean DEFF (29.2\%) and cluster bootstrap (26.7\%)---converge on ${\approx}$27--29\%; the conservative weighted-mean DEFF (13.5\%) still exceeds the random baseline by $75\times$ (\Cref{app:deff,app:deff_simulation}). No single family drives the signal (LOFO $|\Delta\mathrm{C\%}| \leq 2.93$\,pp); graduated de-duplication confirms C\% scales with power, not redundancy (\Cref{app:dedup_k}).
17	
18	\looseness=-1
19	Three controls confirm genuine temporal change (\Cref{tab:temporal_landscape}): random splits yield C\% of 0.18\%
…[truncated 10027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1373 · 2026-05-23T09:09:19.956536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1374 · 2026-05-23T09:09:20.408801+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\enlargethispage*{4\baselineskip}
4	
5	\subsection{Temporal DIF as Structured Signal}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---and this is by design. The signal is structured: stratifying by model type (base $N{=}1{,}409$, instruct $N{=}478$, across all 5,227 models) reveals opposite patterns---base models are 60.1\% reference-favoring with a strong difficulty gradient ($\rho = -0.570$), while instruct models are 65.6\% focal-favoring with a near-zero gradient ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). Following the impact-bias framework~\citep{camilli1994methods}, this reversal reflects structured item-level bias rather than uniform group impact, validating DIF as a mechanism-agnostic diagnostic (\Cref{app:mechanism_discussion}).
10	
11	\looseness=-1
12	The two temporal cohorts differ in base/instruct composition (2023: 79.7\% vs.\ 2024: 67.9\% base). Downsampling to match ratios yields C\% $= 30.25\% \pm 1.32\%$ ($\Delta = 1.08$\,pp; \Cref{app:composition_control}), ruling out composition shift. Within-architecture DIF confirms the signal persists within individual lineages (Llama C\% $= 59.2\%$; \Cref{app:within_arch}), consistent with ability-matched temporal C\% ($28.9\%$).
13	
14	\subsection{Recommended DIF Audit Protocol}
15	\label{sec:disc_protocol}
16	
17	\looseness=-1
18	Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), precluding pre-screening. We recommend MH-DIF audits whenever ${\geq}$500 models accumulate ($K{=}3$ for smaller corpora; \Cref{tab:k3_power}), with action thresholds calibrated to $\rho$-degradation (\Cref{app:fig_rho_degradation}). Flagged items warrant mechanism-conditional responses: remove contaminated items, annotate capability-shifted ones, or refine cohort definitions. DIF-corrected scoring motivates equating adjustments~\citep
…[truncated 46 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1375 · 2026-05-23T09:09:20.409213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1376 · 2026-05-23T09:09:21.363106+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-2
5	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal DIF across 2023--2024 model cohorts (${\approx}$27--29\% for MMLU; conservative bound: 13.5\%), while aggregate rankings remain preserved ($\rho \approx 0.997$). Global exposure and differential functioning are complementary diagnostic dimensions (Jaccard $= 0.206$), confirmed by opposite base-vs-instruct DIF patterns ($\chi^2 = 562.7$). DIF-corrected scoring shifts accuracy by ${+}2.12$\,pp on average, with rank displacements exceeding ${\pm}500$. We recommend mechanism-conditional audit---complementing contamination screening as standard practice~\citep{habba2026growingpains,kolen2014equating}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1377 · 2026-05-23T09:09:21.363483+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1378 · 2026-05-23T09:09:22.317567+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a worst-case injection model; reported $\Delta\mathrm{TPR}$ values are upper-bound estimates, and detection power under realistic contamination patterns (partial memorization, format-specific advantages) is untested. The framework detects \emph{that} items function differently but not \emph{why}---a deliberate design choice that limits immediate actionability; follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Three convergent corrections (${\approx}$27--29\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.069 when contamination spans ${\geq}20$ subjects. Although composition control experiments show a small residual shift ($\Delta = 1.08$\,pp; \Cref{app:composition_control}), base/instruct ratio changes between cohorts remain a potential confound that cannot be fully eliminated without single-architecture longitudinal data. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to open-ended or partial-credit benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1379 · 2026-05-23T09:09:22.318090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-23T09:09:22.468994+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-23T09:09:22.570070+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 28761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool result

_source line 1382 · 2026-05-23T09:09:22.570453+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1383 · 2026-05-23T09:09:31.762734+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 1384 · 2026-05-23T09:09:31.763108+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1385 · 2026-05-23T09:09:33.168823+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1386 · 2026-05-23T09:09:34.475828+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool call

_source line 1387 · 2026-05-23T09:09:34.777911+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/ 2>/dev/null && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check review reports directory and submitted PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/ 2>/dev/null && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check review reports directory and submitted PDF"
  }
}
```

</details>

---


### Tool result

_source line 1388 · 2026-05-23T09:09:34.929308+00:00_

round_0.md
round_1.md
round_10.md
round_11.md
round_12.md
round_13.md
round_14.md
round_2.md
round_3.md
round_4.md
round_5.md
round_6.md
round_7.md
round_8.md
round_9.md
---
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1389 · 2026-05-23T09:09:43.111366+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1390 · 2026-05-23T09:09:43.513530+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\\n\\n## Paper Type\\nEmpirical analysis + methodological framework. Discovery paper with substantive LLM-specific methodological adaptations. \\\"DIF audit framework reveals and quantifies temporal score incomparability.\\\" NOT \\\"just applied standard MH-DIF\\\" — three LLM-specific adaptations address challenges absent in educational testing, with cross-subject matching as a genuine innovation.\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-st
…[truncated 3362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1391 · 2026-05-23T09:09:44.016043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1392 · 2026-05-23T09:09:44.418199+00:00_

1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: A Robust Method for Detecting Variant Conta
…[truncated 3081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1393 · 2026-05-23T09:09:44.569740+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/ 2>/dev/null | head -5",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/ 2>/dev/null | head -5",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1394 · 2026-05-23T09:09:44.620392+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1395 · 2026-05-23T09:10:22.336770+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1396 · 2026-05-23T09:10:49.053823+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26717
}
```

</details>

---


### Tool call

_source line 1397 · 2026-05-23T09:10:49.205991+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 方向的审稿。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类型**: Long paper\n- **页数限制**: 8 页正文 + 无限参考文献；Limitations section 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，不计入页数，审稿人可选择性阅读\n\n## 论文信息\n- **标题**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. MH-DIF 方法论的适用性\n- Mantel-Haenszel DIF 从 educational testing 迁移到 LLM benchmark 的合理性\n- LLM 作为 \"examinees\" 是否满足 MH-DIF 的基本假设（local independence, unidimensionality）\n- K=5 quintile stratification 的选择是否合理\n- 论文如何处理 LLM-specific 的违反假设情况（model family non-independence, bimodal distributions）\n\n### 2. Semi-synthetic 验证框架\n- Uniform binary response flipping 作为注入策略的局限性——是否高估了检测能力\n- ΔFPR=0 的 \"constructive guarantee\" 是否过度声称\n- Cross-subject matching 的有效性和边界条件（multi-subject contamination 的退化）\n- 是否有其他更现实的注入模型应该被考虑\n\n### 3. 统计控制和 robustness\n- DEFF 校正的两种估计（simple-mean vs weighted-mean）差异巨大（29.2% vs 13.5%），论文如何 justify 选择\n- Family-level cluster bootstrap 95% CI [26.7%, 53.2%] 极宽，说明什么\n- 多重比较校正（BH-FDR 仅移除 3/3918 items）——是否因 N=5227 导致 p-value inflation\n- Graduated de-duplication 实验的解读是否合理\n- LOFO 分析显示 Mistral/Llama-3 移除后 C% 显著下降——论文对此的解释是否充分\n\n### 4. 实验设计\n- 5 个 cohort designs 的选择和覆盖是否充分\n- Cross-benchmark validation (6 benchmarks) 的说服力\n- GSM1K correlation (r=-0.478, N=33) 的 exploratory 分析是否 overinterpreted\n- Downstream impact 分析（ρ≈0.997 但个别模型 ±800 rank displacement）的实际意义\n- Within-family DIF (Llama-2 vs Llama-3, C%=59.2%) 是否与 temporal DIF 可比\n\n### 5. 论文格式\n- 是否符合 8 页正文限制\n- 匿名性是否满足 double-blind 要求\n- 图表是否清晰、引用是否完整\n\n请按 ARR 审稿标准给出结构化审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (评分 1-5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 方向的审稿。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类型**: Long paper\n- **页数限制**: 8 页正文 + 无限参考文献；Limitations section 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，不计入页数，审稿人可选择性阅读\n\n## 论文信息\n- **标题**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. MH-DIF 方法论的适用性\n- Mantel-Haenszel DIF 从 educational testing 迁移到 LLM benchmark 的合理性\n- LLM 作为 \"examinees\" 是否满足 MH-DIF 的基本假设（local independence, unidimensionality）\n- K=5 quintile stratification 的选择是否合理\n- 论文如何处理 LLM-specific 的违反假设情况（model family non-independence, bimodal distributions）\n\n### 2. Semi-synthetic 验证框架\n- Uniform binary response flipping 作为注入策略的局限性——是否高估了检测能力\n- ΔFPR=0 的 \"constructive guarantee\" 是否过度声称\n- Cross-subject matching 的有效性和边界条件（multi-subject contamination 的退化）\n- 是否有其他更现实的注入模型应该被考虑\n\n### 3. 统计控制和 robustness\n- DEFF 校正的两种估计（simple-mean vs weighted-mean）差异巨大（29.2% vs 13.5%），论文如何 justify 选择\n- Family-level cluster bootstrap 95% CI [26.7%, 53.2%] 极宽，说明什么\n- 多重比较校正（BH-FDR 仅移除 3/3918 items）——是否因 N=5227 导致 p-value inflation\n- Graduated de-duplication 实验的解读是否合理\n- LOFO 分析显示 Mistral/Llama-3 移除后 C% 显著下降——论文对此的解释是否充分\n\n### 4. 实验设计\n- 5 个 cohort designs 的选择和覆盖是否充分\n- Cross-benchmark validation (6 benchmarks) 的说服力\n- GSM1K correlation (r=-0.478, N=33) 的 exploratory 分析是否 overinterpreted\n- Downstream impact 分析（ρ≈0.997 但个别模型 ±800 rank displacement）的实际意义\n- Within-family DIF (Llama-2 vs Llama-3, C%=59.2%) 是否与 temporal DIF 可比\n\n### 5. 论文格式\n- 是否符合 8 页正文限制\n- 匿名性是否满足 double-blind 要求\n- 图表是否清晰、引用是否完整\n\n请按 ARR 审稿标准给出结构化审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (评分 1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 1398 · 2026-05-23T09:11:09.101029+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19895
}
```

</details>

---


### Tool call

_source line 1399 · 2026-05-23T09:11:09.251921+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + Related Work** 方向的审稿。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类型**: Long paper\n- **页数限制**: 8 页正文 + 无限参考文献；Limitations section 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，不计入页数，审稿人可选择性阅读\n\n## 论文信息\n- **标题**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性评估\n- 论文声称的三个贡献（two dimensions of benchmark behavior, temporal DIF at scale, temporal DIF audit framework）的新颖性\n- MH-DIF 本身是 1988 年的方法——论文的 LLM-specific adaptations（cross-subject matching, DEFF correction, semi-synthetic validation）是否构成足够的方法贡献\n- 与 Growing Pains (habba2026growingpains) 的关系——论文将自己定位为 \"diagnostic step that must precede equating\"，这个定位是否 convincing\n- \"Global exposure vs differential functioning\" 的二维框架是否是真正的新见解还是已知概念的重述\n- 论文是否过度声称了贡献（overclaiming）\n\n### 2. Related Work 覆盖\n- Contamination detection 文献的覆盖是否全面——是否遗漏了重要的 2025-2026 新工作\n- IRT in LLM evaluation 的综述是否准确且完整\n- DIF methodology 的文献引用是否恰当——是否正确引用了关键的方法论文献\n- Benchmark quality 相关工作是否覆盖了所有重要的 concurrent work\n- 是否有明显遗漏的 related work（用 web search 验证）\n\n### 3. 叙事完整性和写作质量\n- Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的叙事逻辑是否连贯\n- 核心发现（31% DIF rate, Jaccard=0.206, ρ≈0.997, χ²=562.7）的呈现是否清晰有效\n- 论文的 framing（从 \"contamination critique\" 到 \"measurement instability discovery\"）是否合适\n- 术语使用是否一致（measurement invariance, temporal score incomparability, DIF）\n- Discussion section 是否充实——是否充分讨论了发现的 implications\n- Limitations 是否诚实且全面\n\n### 4. 结果可信度和证据链\n- Claims 和 evidence 之间的对应是否严密\n- 是否有 overclaiming 或 underclaiming\n- 图表和表格是否有效支持论文的论点\n- 统计显著性报告是否规范\n- 引用是否真实（spot check 几个关键引用的存在性和准确性）\n\n### 5. 论文格式和规范\n- 是否符合 8 页正文限制\n- 匿名性检查（是否有 self-identifying 信息）\n- 参考文献格式是否符合 ACL 标准\n- 图表质量、可读性\n\n请按 ARR 审稿标准给出结构化审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (评分 1-5)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + Related Work** 方向的审稿。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **类型**: Long paper\n- **页数限制**: 8 页正文 + 无限参考文献；Limitations section 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，不计入页数，审稿人可选择性阅读\n\n## 论文信息\n- **标题**: \"Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\"\n- **论文路径**: `projects/irt_equated_bench_regen/paper/main.tex`\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_15/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n### 1. 新颖性评估\n- 论文声称的三个贡献（two dimensions of benchmark behavior, temporal DIF at scale, temporal DIF audit framework）的新颖性\n- MH-DIF 本身是 1988 年的方法——论文的 LLM-specific adaptations（cross-subject matching, DEFF correction, semi-synthetic validation）是否构成足够的方法贡献\n- 与 Growing Pains (habba2026growingpains) 的关系——论文将自己定位为 \"diagnostic step that must precede equating\"，这个定位是否 convincing\n- \"Global exposure vs differential functioning\" 的二维框架是否是真正的新见解还是已知概念的重述\n- 论文是否过度声称了贡献（overclaiming）\n\n### 2. Related Work 覆盖\n- Contamination detection 文献的覆盖是否全面——是否遗漏了重要的 2025-2026 新工作\n- IRT in LLM evaluation 的综述是否准确且完整\n- DIF methodology 的文献引用是否恰当——是否正确引用了关键的方法论文献\n- Benchmark quality 相关工作是否覆盖了所有重要的 concurrent work\n- 是否有明显遗漏的 related work（用 web search 验证）\n\n### 3. 叙事完整性和写作质量\n- Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的叙事逻辑是否连贯\n- 核心发现（31% DIF rate, Jaccard=0.206, ρ≈0.997, χ²=562.7）的呈现是否清晰有效\n- 论文的 framing（从 \"contamination critique\" 到 \"measurement instability discovery\"）是否合适\n- 术语使用是否一致（measurement invariance, temporal score incomparability, DIF）\n- Discussion section 是否充实——是否充分讨论了发现的 implications\n- Limitations 是否诚实且全面\n\n### 4. 结果可信度和证据链\n- Claims 和 evidence 之间的对应是否严密\n- 是否有 overclaiming 或 underclaiming\n- 图表和表格是否有效支持论文的论点\n- 统计显著性报告是否规范\n- 引用是否真实（spot check 几个关键引用的存在性和准确性）\n\n### 5. 论文格式和规范\n- 是否符合 8 页正文限制\n- 匿名性检查（是否有 self-identifying 信息）\n- 参考文献格式是否符合 ACL 标准\n- 图表质量、可读性\n\n请按 ARR 审稿标准给出结构化审稿意见：Summary, Strengths, Weaknesses, Questions, Missing References, Overall Assessment (评分 1-5)。"
  }
}
```

</details>

---


### Tool result

_source line 1400 · 2026-05-23T09:11:10.820766+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1568
}
```

</details>

---


### Assistant

_source line 1401 · 2026-05-23T09:11:21.469329+00:00_

Round 1 已启动：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性 + 实验设计 |
| Reviewer 2 | ✅ 已派发 | 新颖性 + 完整性 + Related Work |
| 视觉审查 | ✅ 已派发 | PDF 排版质量（非评分项，并行执行） |

等待两位 Reviewer 返回初审意见，收到后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 134

## Round 134

2 recorded events


### User

_source line 1402 · 2026-05-23T09:16:27.488844+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见：方法严谨性 + 实验设计

### Summary

本文将教育测量中的 Mantel-Haenszel 差异项目功能（MH-DIF）分析应用于 LLM benchmark 评估，对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）进行大规模时序审计。核心发现是 2023 与 2024 模型队列间约 27–31% 的 MMLU 题目表现出时序 DIF（即题目测量属性随时间漂移），且此信号与 web-overlap 污染标签经验上正交（Jaccard ≈ 0.206）。论文提出 cross-subject matching 策略处理多学科污染、用 semi-synthetic injection 验证检测能力、并在 6 个 benchmark 上做了交叉验证。最终建议将 MH-DIF 作为 benchmark 常规审计工具。

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 重要且新颖的跨学科贡献，将心理测量学的 DIF 框架以大规模方式引入 LLM 评估，但核心统计量（DEFF 校正后的 C%）存在 2 倍估计分歧未充分 justify，semi-synthetic 验证与真实污染模式的差距削弱了检测能力标定的可信度。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 方法论框架严谨、诊断检查全面，但 DEFF 两种估计量差异悬殊（29.2% vs 13.5%）且选择理由不充分；IRT 假设违反的影响量化不足 |
| Excitement | 4 / 5 | 问题重要且及时，规模令人印象深刻（5,227 模型），cross-subject matching 是对 DIF 方法的实质性改编，实践建议可操作 |
| Reproducibility | 4 / 5 | 提供匿名化代码链接，数据基于公开 METABENCH，方法描述详尽；但 semi-synthetic injection 的部分实现细节需参考附录 |
| Confidence | 4 / 5 | 我熟悉 DIF/IRT 方法论和 LLM 评估文献，对本审查有较高信心 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DEFF 校正的两种估计量差异悬殊，论文选择理由不充分

- 具体位置：Section 4.2, Appendix D, Appendix I (Table 12)
- 问题：Simple-mean DEFF 给出 adjusted C% = 29.2%，weighted-mean DEFF 给出 adjusted C% = 13.5%——二者相差超过 2 倍。论文以 simple-mean 为主要报告值（Section 4.2: "the conservative weighted-mean DEFF... converge on ≈27–29%"），但 Appendix I 的模拟显示 weighted-mean 在大家族低 ICC 条件下更准确（"the simple-mean estimate better captures the average inflation per family under these conditions"）。问题在于：（1）weighted-mean 是统计学中更标准的处理方式（按样本量加权），论文将非标准选择作为 primary 报告但缺乏充分的理论论证；（2）读者面对 "13.5% vs 29.2%" 的差异，无法判断真实 C% 究竟在什么水平；（3）cluster bootstrap 95% CI [26.7%, 53.2%] 极宽（跨度 26.5pp），进一步加剧了不确定性，但论文未在正文充分讨论这一宽度的含义。
- 为什么影响接收：论文的核心 claim（"≈27–29% of MMLU items exhibit temporal DIF"）直接依赖此选择。如果 weighted-mean 才是更合理的估计，核心发现缩减至 13.5%——仍然有意义，但 narrative 和结论强度需要显著调整。
- 建议修改方向：（1）在正文 Section 4.2 明确报告两种估计量及其差异，而非将 weighted-mean 仅放在附录；（2）论证为何 simple-mean 更适合本场景（或承认不确定性并以区间而非点估计作为主要结论）；（3）对 cluster bootstrap CI 的宽度做实质性讨论——什么驱动了这一不确定性？是 family 结构还是 cohort 划分？

**N2** [critical] Semi-synthetic 验证使用的 uniform binary flipping 与真实污染模式差距过大，检测能力标定可信度受限

- 具体位置：Section 3.4, Section 4.1, Figure 2, Limitations
- 问题：Semi-synthetic injection 采用 uniform binary response flipping（以固定概率 ρ 将正确答案翻转为错误）。但真实的 benchmark 污染表现为：（a）使题目变容易而非随机翻转方向；（b）效应大小因题目难度而异（简单题 ceiling effect，困难题收益更大）；（c）与模型能力交互（高能力模型可能已经答对，污染无额外效应）。论文将 uniform flipping 定位为 "worst-case injection model" 和 "upper-bound estimate"（Limitations, p.8），但这一定位本身有问题——uniform flipping 不一定是 worst-case，而可能是 easiest-to-detect case，因为它产生的信号比真实污染更均匀、更容易被 MH 统计量捕获。
- 为什么影响接收：Figure 2 的 dose-response 曲线（TPR vs ρ）是论文标定 MH-DIF 检测能力的核心证据。如果 uniform flipping 使检测偏容易，则 TPR 被高估，论文关于 "MH-DIF 在 ρ > 0.3 时具有足够检测力" 的结论不可靠。同时，ΔFPR = 0 的 "constructive guarantee" 虽然在数学上成立（cross-subject matching 的结构性质），但仅限于 injection 不影响 matching variable 的前提——如果真实污染是 multi-subject 的（论文 Table 7 已示 k=20 时 ΔFPR 升至 0.047），这一保证就退化了。
- 建议修改方向：（1）增加至少一种更现实的注入模型（如 difficulty-dependent flipping：难题翻转概率高于简单题）并比较 TPR；（2）将 "worst-case" 改为 "stylized"/"simplified"，准确描述其性质；（3）在正文（非仅 Limitations）讨论 uniform flipping 假设对检测力标定的影响方向。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ETS 效应量阈值（|Δ_MH| ≥ 1.5）为人类考生设计，直接移植到 LLM 的合理性未论证

- 具体位置：Section 3.2, Appendix A.2
- 问题：ETS 分类标准（A/B/C categories）基于 |Δ_MH| 阈值，这些阈值源自教育测试中数十年的经验校准，反映人类考生群体中 "educationally meaningful" 的 DIF 大小。LLM 群体的方差结构完全不同——5,227 个模型的能力分布可能比人类考生更异质（bimodal: base vs instruct）或更同质（同家族内），DIF 效应量的 "meaningful" 标准也应不同。论文直接采用 |Δ_MH| ≥ 1.5 作为 Category C 阈值但未讨论这一移植是否合理。Appendix A.2 的 threshold sensitivity 分析显示结论在 |Δ_MH| ∈ {1.0, 1.5, 2.0, 2.5} 范围内稳健，这是有用的，但不等于论证了 1.5 在 LLM 语境下的适切性。
- 建议：增加一段讨论 ETS 阈值在 LLM 语境下的适切性，或用 data-driven 方法（如 permutation-based null distribution）确定 LLM-specific 阈值，并与 ETS 标准比较。

**W2** [warning] N=5,227 模型导致 MH chi-squared 检验统计功效过高，p-value 近乎全部显著

- 具体位置：Section 3.2, Section 4.2
- 问题：MH chi-squared 的统计功效随样本量增大。N=5,227 时，即便极小的 DIF 效应也会达到统计显著（p < 0.05）。论文报告 BH-FDR 仅移除 3/3918 items——这恰恰说明几乎所有 p-value 都极小，统计显著性已失去区分力。虽然 ETS 分类引入了效应量阈值（|Δ_MH| ≥ 1.5）作为实质性过滤，但 ETS C 分类同时要求 p < 0.05（Section 3.2），在 N=5,227 下这一条件几乎自动满足，等同于仅用效应量筛选。
- 建议：讨论 N=5,227 下统计功效的行为，说明 ETS 分类中 p < 0.05 条件在此规模下的实际角色；考虑是否需要更严格的效应量阈值来补偿。

**W3** [warning] Within-family DIF（Llama-2 vs Llama-3, C%=59.2%）与 temporal DIF 的可比性存疑

- 具体位置：Section 3.3 (Cohort 3), Appendix N, Table 14
- 问题：Within-family cohort 比较 Llama-2（N=161）vs Llama-3（N=308），但这两代模型在架构、规模、训练数据上存在根本差异。观察到的 C%=59.2% 可能反映的是架构/能力代际差异而非 temporal DIF——两者在此设计中完全混淆。论文在 Appendix N 将其定位为 "confirming that temporal DIF is not an artifact of comparing different architectures"，但逻辑上恰恰相反：within-family 比较中 C% 更高可能表明 DIF 信号部分来自架构差异而非时间效应。
- 建议：重新框架化 within-family 分析的解释——它不能 confirm temporal DIF 不是架构伪迹，而是说明 DIF 在 within-family 比较中更强，可能因为架构差异叠加了时间效应。或者提供 within-architecture same-generation 的比较作为对照。

**W4** [warning] GSM1K 相关性分析（r = -0.478, N = 33）作为验证证据偏弱且存在过度解读风险

- 具体位置：Section 4.7, Appendix F, Figure 5
- 问题：论文将 GSM1K contamination gap 与 DIF ranking advantage 的负相关作为 "independently confirming the DIF-contamination orthogonality" 的证据（Section 4.7: "SNAP > 0.012, independently confirming the DIF-contamination orthogonality"）。但（1）N=33 极小，r=-0.478 的 95% CI 包含较弱的效应量；（2）33 个模型是 GSM1K 数据集中可用模型的全集还是子集？如果是子集，选择偏差需讨论；（3）相关方向（负相关）的因果解释不明确——为什么 DIF ranking advantage 高的模型反而 contamination gap 低？论文虽标注 "exploratory"（Figure 5 caption），但在 Section 4.7 正文中用 "confirms" 语气呈现。
- 建议：统一 exploratory 定位，避免在正文用 "confirms"/"confirming" 表述；报告 r 的 confidence interval；讨论样本代表性。

**W5** [warning] Local independence 违反的定量影响未充分评估

- 具体位置：Section 4.5, Appendix A.1
- 问题：Appendix A.1 报告了 Yen's Q3 诊断，发现 within-subject 和 cross-subject item pairs 存在 elevated residual correlations（|Q3| > 0.20 的比例较高）。但论文未将这些 Q3 违反与 DIF detection rate 的 inflation 做定量关联。DEFF 校正处理的是 family-level clustering（模型间非独立性），而 Q3 反映的是 item-level local dependence（题目间非独立性）——这是两个不同层面的非独立性问题，DEFF 不能替代对 Q3 的处理。
- 建议：量化 item-level local dependence 对 MH-DIF 检测率的具体影响。例如，通过模拟 Q3 水平不同的数据，评估 local dependence 对 false DIF detection rate 的贡献。或至少讨论为什么 family-level DEFF 校正足以同时处理 item-level local dependence。

---

## 小问题（不影响接收）

- Section 3.2: "K = 5 equiprobable strata (quintile-based binning) following ETS recommended practice" — 引用了 Donoghue and Allen (1993) 和 Clauser and Mazor (1998)，但这些引用针对的是人类考试场景。建议增加一句说明 K=5 在 LLM 设置下的适切性（如 LLM 能力分布可能需要不同的 K 值）。

- Table 1: "Dashes (–) indicate comparisons where Li et al. labels are not available" — 但表中 CV enrichment 列的 dash 含义应明确区分 "不适用" 与 "数据缺失"。

- Figure 1 caption 较长（约 8 行），建议精简，将细节移入正文。

- Limitations 段落提到 "The MH χ² test assumes independent examinees; LLM model families violate this assumption"，但此处的 "independent examinees" 容易与 local independence 混淆——实际指的是 examinees 之间的独立性（即模型间非独立性），建议措辞更精确。

- 论文脚注 1 提供了匿名代码链接，满足 double-blind 要求。

---

## 主要优势

1. **问题的重要性和及时性**：LLM benchmark 分数的跨时间可比性是一个被广泛假设但很少被系统验证的问题。论文以 5,227 个模型的规模进行定量审计，填补了重要的方法论空白。

2. **Cross-subject matching 是对经典 DIF 的实质性创新**：论文识别出 LLM multi-domain benchmark 中 matching variable 会被污染的问题，并提出用其他学科的总分作为 matching variable——这不是简单套用教育测量方法，而是有针对性的方法论适配，包括 ΔFPR = 0 的结构性保证（在单学科注入条件下）。

3. **多层次 robustness 检查**：graduated de-duplication（Table 2 系列）、LOFO（Table 8）、random split 负对照、cross-benchmark 验证（Table 3, 6 个 benchmark）、within-architecture 分析（Table 14）——这些检查覆盖了统计功效、家族结构、benchmark 特异性等多个维度的 confound。

4. **"两维度" 框架的概念贡献**：将 global exposure（web-overlap）和 differential functioning（DIF）区分为互补的正交维度（Section 5.1, Figure 1），为 benchmark integrity 的讨论提供了新的概念结构。实证上 Jaccard ≈ 0.206 和 association tests 的 near-independence（OR = 1.01, Section 4.3）支持这一区分。

5. **写作质量**：论文在 8 页内清晰呈现了复杂的方法论框架，Figure 1 的 ICC 双图对照直观有效，附录组织有序提供了详尽的补充分析。

---

**总结**：这是一篇有实质贡献的跨学科论文，将心理测量学方法成功引入 LLM 评估领域。核心发现（temporal DIF 广泛存在）在多个 robustness check 下成立。主要顾虑集中在两点：（1）DEFF 校正的估计量选择显著影响核心数字但未充分论证；（2）semi-synthetic 验证的注入模型过于理想化，限制了检测能力标定的外部效度。这两个问题可在修订中解决，不构成根本性缺陷。建议 Borderline Conference，倾向积极——如果作者能在修订中澄清 DEFF 选择并增加更现实的注入模型比较，本文可达到 Conference 水准。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1403 · 2026-05-23T09:16:33.643956+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 135

## Round 135

2 recorded events


### User

_source line 1404 · 2026-05-23T09:16:39.337115+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心评判：**Overall 3.5 / 5（Borderline Conference）**。

两个 Must-Fix：
1. **DEFF 校正分歧**——simple-mean（29.2%）vs weighted-mean（13.5%）差异 2 倍，直接影响核心 claim 的数字基础，选择理由不充分
2. **Semi-synthetic 验证的注入模型过于理想化**——uniform binary flipping 可能是 easiest-to-detect 而非 worst-case，检测力标定的外部效度受限

五个 Should-Fix：ETS 阈值移植合理性未论证、N=5227 下 p-value 失去区分力、within-family DIF 与架构差异混淆、GSM1K 相关性过度解读、local independence 违反的定量影响缺失。

总体判断：实质性跨学科贡献，核心发现在多个 robustness check 下成立，但两个关键统计选择需要在修订中澄清。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1405 · 2026-05-23T09:16:45.906903+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 136

## Round 136

6 recorded events


### User

_source line 1406 · 2026-05-23T09:21:34.913599+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（新颖性 + 完整性 + Related Work）

---

## 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 大规模实证发现扎实（31% DIF rate，base-vs-instruct 反转模式），但方法论新颖性有限（MH-DIF 是现成工具，所谓"框架贡献"实为标准技术的领域适配），且发现的可操作性不足。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨：随机分割对照（C%=0.18%）、能力匹配、家族去重、跨基准复制、半合成注入验证，多重控制链闭合良好。DEFF 修正和 cluster bootstrap 处理非独立性。唯一的 soundness 缺陷是半合成验证的生态效度有限（见 W2）。 |
| Excitement | 3/5 | 发现本身（31% 项目有时序 DIF、与 web-overlap 正交、base/instruct 反转）对 LLM 评估社区有实用价值，但方法层面是成熟教育测量工具的领域迁移，缺少方法论上的惊喜或深度洞见。 |
| Reproducibility | 4/5 | 提供匿名代码仓库，使用公开数据集（METABENCH），统计方法标准化（MH-DIF + ETS 分类）。附录报告了详细参数和实验配置。 |
| Confidence | 4/5 | 我熟悉 DIF 方法论、IRT 在 NLP 中的应用、以及 LLM 基准污染检测文献。仔细阅读了正文和附录。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 方法论贡献被过度声称（Overclaiming of framework contribution）
- 具体位置：Section 1（Introduction），Contribution 3；Section 3.4（Semi-Synthetic Injection）
- 问题：论文将三项内容打包为"Temporal DIF audit framework"作为独立贡献：(a) cross-subject matching, (b) DEFF correction, (c) semi-synthetic validation。但逐项审视：
  - Cross-subject matching 是 purified subtest matching（Swaminathan & Rogers, 1990）的直接适配，论文自己在 Section 3.2 也承认"adapting purified subtest matching"。变化仅是把"其他科目总分"作为 matching variable，而非测试科目总分。这在多领域教育测试中早有先例（Nandakumar, 1993; Donoghue & Allen, 1993），论文也引用了这两篇。
  - DEFF correction 是调查方法学标准技术（Rao & Scott, 1992），用于处理聚类非独立性。应用于 LLM 模型家族是合理的，但不构成方法创新。
  - Semi-synthetic validation 使用二值翻转注入，是最简单的模拟方式。论文自己承认"worst-case uniform injection pattern"（Section 3.4），这意味着检测力是上界估计，在真实污染模式下的表现未知。
  - 论文在 Section 2（Related Work）第三段明确说"We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals"——这与 Introduction 中将 framework 列为独立贡献（Contribution 3）形成矛盾。
- 为什么影响接收：在 ACL/*ACL 体系中，方法贡献需要超越现有技术的直接应用。如果诚实地将论文定位为"大规模实证研究 + 标准方法的领域适配"，Excitement 分数更易被接受；但将标准技术包装为"framework contribution"会被视为 overclaiming，降低审稿人信任度。
- 建议修改方向：将 Contribution 3 重新表述为"methodological adaptations that enable valid DIF analysis in the LLM setting"而非独立框架贡献。或者，加深方法创新——例如开发一个考虑 LLM 家族结构的分层 DIF 检验（hierarchical MH），而不是事后用 DEFF 修正 p 值。

**N2** [critical] "两维度"贡献的新颖性存疑（Two-dimensions contribution may be definitional）
- 具体位置：Section 1（Contribution 1）；Section 4.3（Ground Truth Mismatch）
- 问题：论文将"global exposure（web-overlap labels）和 differential functioning（DIF flags）是经验正交的"作为第一项贡献。但仔细思考：
  - Web-overlap labels 衡量的是"项目是否出现在训练语料中"（静态存在性）
  - DIF 衡量的是"项目在不同群组中的表现是否一致"（行为变化）
  - 这两个构念在定义层面就是不同的维度。一个项目可以出现在所有模型的训练数据中（全局暴露高）但对所有模型的表现影响一致（无 DIF）；反之，一个项目可以不在任何训练数据中但因能力维度变化而出现 DIF。
  - 因此，它们的低相关（Jaccard=0.206, φ=0.012）是从构念定义可预期的结果，而非令人惊讶的实证发现。
  - Figure 1 的 ICC 图示也证实了这一点：左图（全局污染，无 DIF）和右图（差异性污染，有 DIF）的区别就是构念定义的视觉化。
- 为什么影响接收：将预期结果包装为"发现"会削弱论文的可信度。如果审稿人注意到这一点，会质疑作者对自身贡献的判断力。
- 建议修改方向：将此点从"contribution"降级为"empirical confirmation of a theoretically expected distinction"。更有价值的方向是：探索在什么条件下两个维度*不*正交（例如，特定类型的差异性污染可能同时被 web-overlap 捕获），这才是非平凡的发现。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 遗漏重要的 concurrent work：CoDeC（ICLR 2026）
- 具体位置：Section 2（Related Work），Contamination Detection 段落
- 问题：CoDeC（Detecting Data Contamination in LLMs via In-Context Learning，ICLR 2026 poster）是 2025-2026 年间重要的污染检测新方法，使用 in-context learning 对比有无上下文示例时的置信度变化来检测污染。该方法与本文的 DIF 方法形成有趣对比：CoDeC 是 model-agnostic 的检测方法，而 DIF 是 model-comparison 的分析方法。在论文的"global exposure vs differential functioning"框架下，CoDeC 属于 global exposure 检测的最新进展，应当被讨论。
- 建议：在 Section 2 Contamination Detection 段落中加入 CoDeC 的引用和简要讨论，说明其属于 global exposure 检测范畴。

**W2** [warning] 半合成验证的生态效度不足，且论文对此的讨论不充分
- 具体位置：Section 3.4；Section 4.5；Limitations
- 问题：半合成注入使用均匀二值翻转（将错误答案翻转为正确），这是最极端的注入模式。真实的污染效应远比这复杂：
  - 部分记忆（模型只在某些提示格式下受益）
  - 格式特定优势（如选项顺序记忆）
  - 能力依赖的差异性（高能力模型可能已经答对，注入无效）
  - 论文在 Section 3.4 承认"realistic contamination (partial memorization, format-specific advantages) would produce weaker signals"，在 Limitations 中也提及，但没有提供任何关于"weaker by how much"的分析。
  - 这意味着 ΔTPR 值（如 +0.508 at p=0.5）是严格的上界。真实场景下的检测力可能显著低于此值，但我们不知道低多少。
- 为什么影响评分：如果检测力在真实场景下大幅下降，论文推荐的"500 模型即可审计"（Section 5.2）的实用建议可能不成立。
- 建议：至少提供一个非均匀注入实验（例如：只翻转低能力模型的答案，模拟能力依赖的污染），以展示检测力在更现实条件下的衰减程度。

**W3** [warning] 可操作性缺口——DIF 标记后该怎么办？
- 具体位置：Section 5.2（Recommended DIF Audit Protocol）
- 问题：Section 5.2 建议"flagged items warrant mechanism-conditional responses: remove contaminated items, annotate capability-shifted ones, or refine cohort definitions"，但论文没有提供区分这些情况的方法。DIF 本身是 mechanism-agnostic 的（论文在 Section 5.1 反复强调"detects *that* items function differently, not *why*"），那么实践者如何判断一个 DIF 项目应该被"remove"还是"annotate"？论文引用了 Growing Pains 作为下游等值校准的解决方案，但没有展示 DIF 诊断到等值校准的实际 pipeline。
- 建议：(1) 提供一个具体案例，展示如何对几个 DIF 标记项目进行后续机制诊断；(2) 或者诚实地讨论这个可操作性缺口并将其列为 future work。

**W4** [warning] 非 MMLU 基准的分析深度不足
- 具体位置：Section 4.7（Cross-Benchmark Validation）
- 问题：论文标题说"A Large-Scale Psychometric Audit"，声称覆盖 6 个 METABENCH 基准，但除 MMLU 外的 5 个基准仅在 Table 3 中各占一行数据。没有对 GSM8K、HellaSwag 等的 DIF 模式做任何结构分析（如 base-vs-instruct 分层、难度梯度、科目分布等）。Table 3 显示知识/推理类基准（MMLU 31.3%, WinoGrande 30.3%）的 C% 显著高于程序类基准（HellaSwag 17.9%, GSM8K 18.9%），但论文仅以"differences may partly reflect item difficulty distributions; we treat them as descriptive"一笔带过。这是一个值得深入探讨的发现。
- 建议：至少对一个非 MMLU 基准（如 GSM8K 或 HellaSwag）做基本的结构分析（base-vs-instruct 分层、难度-方向相关性），以支撑"跨基准审计"的声明。

**W5** [warning] 标题中"5,227 Models"可能产生误导
- 具体位置：Title；Section 3.3
- 问题：标题强调"5,227 Models"，但核心发现（31% temporal DIF rate）基于 1,080 + 807 = 1,887 个模型的时序比较。5,227 是 METABENCH 数据集中所有 MMLU 模型的总数，其余 ~3,340 个模型并未用于主要时序分析。虽然某些辅助分析（如能力分层、DEFF 计算）使用了更多模型，但标题给人的印象是"5,227 个模型都参与了核心分析"。
- 建议：在 Section 3 开头更明确地说明各分析使用的模型子集。标题可以保留，但正文需清晰交代。

---

## 小问题（不影响接收）

- **术语一致性**：论文交替使用"measurement invariance"和"temporal score incomparability"。Introduction 明确定义了术语链（measurement invariance → DIF → temporal score incomparability），但后续章节有时混用。建议统一使用"temporal score incomparability"作为核心发现的术语。
- **Discussion `\enlargethispage*{4\baselineskip}`**：main.tex 的 discussion.tex 中使用了页面拉伸命令，表明论文在 8 页限制边缘。建议精简 Section 5.1 以自然腾出空间。
- **Table 1 可读性**：Table 1 的"Enrichment"列需要在 caption 中更清晰地解释（目前解释在 caption 末尾，不够突出）。
- **Figure 2 细节**：Figure 2 的 y 轴标签"False Positive Rate (FPR)"与图示内容（显示 ΔTPR 的 dose-response 曲线）不完全匹配——图中同时显示了 TPR 和 FPR 的变化，但 y 轴标签不够清晰。
- **引用格式**：`\citet{sik2026causal}` 标注为 "Forthcoming" in Psychometrika——审稿人无法验证此引用的存在性。建议提供 preprint 链接或 DOI。
- **附录 Section B（Mechanism Analysis）**：排除论证（exclusion arguments）中使用了 4 个 "narrow possible explanations" 的论证，但每个论证的效应量很小（如 "domain accuracy gains explain <0.1% of item-level DIF variance"），这些微小效应的累积是否被考虑？
- **Appendix 依赖**：主文中多处关键细节被推迟到附录（如 DEFF 修正细节在 App D, 去重分析在 App J, 分数膨胀在 App M），这使得仅阅读主文的审稿人难以完整评估 soundness。虽然 ACL 允许附录，但核心论证链应在主文中自洽。

---

## Missing References

1. **CoDeC**（ICLR 2026）：Detecting Data Contamination in LLMs via In-Context Learning。重要的最新污染检测方法，应在 Section 2 Contamination Detection 段落中讨论。
2. **JE-IRT**（Joint Embedding Item Response Theory, arXiv 2509.22888）：将 IRT 与表示学习结合的最新工作，与 Section 2 IRT in LLM Evaluation 相关。
3. **PaCoST**（Paired Confidence Significance Testing, arXiv 2406.18326）：另一种污染检测方法，可考虑加入。

---

## 主要优势

1. **规模和系统性**：5,227 模型 × 12,508 项目的分析规模在 DIF 文献中前所未有（论文正确指出这超过了典型 DIF 应用的样本量，引用 Belzak 2020）。6 个基准的交叉验证增强了发现的普遍性。

2. **实验控制链的完整性**：随机分割对照（C%=0.18%）、能力匹配控制、LOFO 家族稳健性、DEFF 非独立性修正、cluster bootstrap 置信区间——每个潜在混淆因素都有对应的控制实验。这体现了严谨的实证研究素养。

3. **Base-vs-instruct 反转模式**：χ²=562.7 的 base-vs-instruct DIF 方向反转是论文最有洞见的发现。Base 模型倾向 reference-favoring（60.1%），instruct 模型倾向 focal-favoring（65.6%），且两者的难度梯度方向相反（ρ=-0.570 vs ρ=-0.079）。这表明 DIF 信号具有结构性，不是随机噪声，且与训练方法论的差异相关联。

4. **与 Growing Pains 的互补定位**："诊断先于等值校准"的定位是合理的。论文将自己定位为 DIF 诊断（识别哪些项目不稳定），Growing Pains 做等值校准（在稳定项目上做分数等值）。论文的 stable-item set 可以直接作为 Growing Pains 的 anchor item candidates。

5. **诚实的 Limitations section**：三个主要限制都是实质性的（半合成验证的生态效度、非独立性、cross-subject matching 边界条件），且讨论坦诚。

6. **Related Work 覆盖面广**：四个段落覆盖了污染检测、IRT in LLM、DIF 方法论、基准质量四个相关领域，引文数量充足，与 concurrent work（Growing Pains、BHI、Benchmark²）的关系讨论清晰。

---

## Questions for Authors

1. 如果 base-vs-instruct 是 DIF 信号的主要结构驱动因素，那么仅对 base 模型或仅对 instruct 模型做时序 DIF 分析，C% 会是多少？这能否分离出真正的"temporal"成分和"training methodology"成分？（论文在 App O 做了 base/instruct 比例控制，但似乎没有做分层时序分析。）

2. 论文报告 aggregate ranking 保持 ρ≈0.997，这意味着对大多数实际用途（排名模型）DIF 影响可忽略。那么 DIF 监测的实际应用场景是什么？是为了分数校准（+2.12pp）？还是为了科学理解？如果主要是后者，"practical audit protocol"（Section 5.2）的定位是否需要调整？

3. 时序粒度：2023 vs 2024 是日历年分割。如果按季度或按模型发布时间做更细粒度的分割，DIF 率如何演变？这对理解 DIF 的成因（是渐进的还是跳变的）有关键意义。

---

**总结**：这是一篇扎实的大规模实证研究，发现 LLM 基准中约 31% 的项目存在时序 DIF，且 DIF 与 web-overlap 污染标签正交。实验控制链完整，发现对 LLM 评估社区有实用价值。主要弱点是方法论新颖性有限（MH-DIF 是 1988 年的方法，所谓"框架贡献"是标准技术的领域适配而非创新），以及发现的可操作性不足。建议降低对方法贡献的声称力度，增强对非 MMLU 基准的分析深度，并补充缺失的 concurrent work（CoDeC）。

适合 Findings 或 Borderline Conference 接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1407 · 2026-05-23T09:22:07.358171+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] DEFF 校正的两种估计量差异悬殊，论文选择理由不充分\n- Simple-mean DEFF 给出 adjusted C% = 29.2%，weighted-mean DEFF 给出 adjusted C% = 13.5%——二者相差超过 2 倍。论文以 simple-mean 为主要报告值，但 weighted-mean 是统计学中更标准的处理方式（按样本量加权）。Cluster bootstrap 95% CI [26.7%, 53.2%] 极宽。读者无法判断真实 C% 究竟在什么水平。\n\n**N2** [critical] Semi-synthetic 验证使用的 uniform binary flipping 与真实污染模式差距过大\n- Uniform flipping 不一定是 worst-case，而可能是 easiest-to-detect case，因为它产生的信号比真实污染更均匀、更容易被 MH 统计量捕获。Figure 2 的 dose-response 曲线是论文标定检测能力的核心证据，如果 uniform flipping 使检测偏容易，则 TPR 被高估。\n\n### Should-Fix\n\n**W1** ETS 效应量阈值（|Δ_MH| ≥ 1.5）为人类考生设计，直接移植到 LLM 的合理性未论证。\n\n**W2** N=5,227 模型导致 MH chi-squared 检验统计功效过高，p-value 近乎全部显著，ETS C 分类中 p < 0.05 条件在此规模下几乎自动满足。\n\n**W3** Within-family DIF（Llama-2 vs Llama-3, C%=59.2%）与 temporal DIF 的可比性存疑——两代模型在架构、规模、训练数据上根本差异。\n\n**W4** GSM1K 相关性分析（r = -0.478, N = 33）作为验证证据偏弱且存在过度解读风险。\n\n**W5** Local independence 违反的定量影响未充分评估——DEFF 处理 family-level clustering，但 Q3 反映的是 item-level local dependence，两者是不同层面的非独立性。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（方法严谨性 + 实验设计）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] DEFF 校正的两种估计量差异悬殊，论文选择理由不充分\n- Simple-mean DEFF 给出 adjusted C% = 29.2%，weighted-mean DEFF 给出 adjusted C% = 13.5%——二者相差超过 2 倍。论文以 simple-mean 为主要报告值，但 weighted-mean 是统计学中更标准的处理方式（按样本量加权）。Cluster bootstrap 95% CI [26.7%, 53.2%] 极宽。读者无法判断真实 C% 究竟在什么水平。\n\n**N2** [critical] Semi-synthetic 验证使用的 uniform binary flipping 与真实污染模式差距过大\n- Uniform flipping 不一定是 worst-case，而可能是 easiest-to-detect case，因为它产生的信号比真实污染更均匀、更容易被 MH 统计量捕获。Figure 2 的 dose-response 曲线是论文标定检测能力的核心证据，如果 uniform flipping 使检测偏容易，则 TPR 被高估。\n\n### Should-Fix\n\n**W1** ETS 效应量阈值（|Δ_MH| ≥ 1.5）为人类考生设计，直接移植到 LLM 的合理性未论证。\n\n**W2** N=5,227 模型导致 MH chi-squared 检验统计功效过高，p-value 近乎全部显著，ETS C 分类中 p < 0.05 条件在此规模下几乎自动满足。\n\n**W3** Within-family DIF（Llama-2 vs Llama-3, C%=59.2%）与 temporal DIF 的可比性存疑——两代模型在架构、规模、训练数据上根本差异。\n\n**W4** GSM1K 相关性分析（r = -0.478, N = 33）作为验证证据偏弱且存在过度解读风险。\n\n**W5** Local independence 违反的定量影响未充分评估——DEFF 处理 family-level clustering，但 Q3 反映的是 item-level local dependence，两者是不同层面的非独立性。"
  }
}
```

</details>

---


### Tool result

_source line 1408 · 2026-05-23T09:22:22.639797+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15281
}
```

</details>

---


### Tool call

_source line 1409 · 2026-05-23T09:22:22.992957+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + Related Work）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] 方法论贡献被过度声称（Overclaiming of framework contribution）\n- Cross-subject matching 是 purified subtest matching 的直接适配，DEFF correction 是调查方法学标准技术，semi-synthetic validation 使用最简单的模拟方式。论文在 Section 2 说\"We do not modify the MH procedure\"，与 Introduction 中将 framework 列为独立贡献（Contribution 3）矛盾。建议将论文定位为\"大规模实证研究 + 标准方法的领域适配\"。\n\n**N2** [critical] \"两维度\"贡献的新颖性存疑\n- Global exposure 和 differential functioning 在定义层面就是不同维度。一个项目可以全局暴露高但无 DIF，反之亦然。因此它们的低相关（Jaccard=0.206）是从构念定义可预期的结果，而非令人惊讶的实证发现。将预期结果包装为\"发现\"削弱可信度。\n\n### Should-Fix\n\n**W1** 遗漏 concurrent work：CoDeC（ICLR 2026）。\n\n**W2** 半合成验证的生态效度不足——真实的污染效应远比 uniform binary flipping 复杂（部分记忆、格式特定优势、能力依赖的差异性）。\n\n**W3** 可操作性缺口——DIF 是 mechanism-agnostic 的，但论文推荐\"mechanism-conditional responses\"，实践者如何判断应该 remove 还是 annotate？\n\n**W4** 非 MMLU 基准的分析深度不足——除 MMLU 外的 5 个基准仅在 Table 3 中各占一行数据，无结构分析。\n\n**W5** 标题中\"5,227 Models\"可能产生误导——核心时序分析仅用 1,887 个模型。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（新颖性 + 完整性 + Related Work）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix\n\n**N1** [critical] 方法论贡献被过度声称（Overclaiming of framework contribution）\n- Cross-subject matching 是 purified subtest matching 的直接适配，DEFF correction 是调查方法学标准技术，semi-synthetic validation 使用最简单的模拟方式。论文在 Section 2 说\"We do not modify the MH procedure\"，与 Introduction 中将 framework 列为独立贡献（Contribution 3）矛盾。建议将论文定位为\"大规模实证研究 + 标准方法的领域适配\"。\n\n**N2** [critical] \"两维度\"贡献的新颖性存疑\n- Global exposure 和 differential functioning 在定义层面就是不同维度。一个项目可以全局暴露高但无 DIF，反之亦然。因此它们的低相关（Jaccard=0.206）是从构念定义可预期的结果，而非令人惊讶的实证发现。将预期结果包装为\"发现\"削弱可信度。\n\n### Should-Fix\n\n**W1** 遗漏 concurrent work：CoDeC（ICLR 2026）。\n\n**W2** 半合成验证的生态效度不足——真实的污染效应远比 uniform binary flipping 复杂（部分记忆、格式特定优势、能力依赖的差异性）。\n\n**W3** 可操作性缺口——DIF 是 mechanism-agnostic 的，但论文推荐\"mechanism-conditional responses\"，实践者如何判断应该 remove 还是 annotate？\n\n**W4** 非 MMLU 基准的分析深度不足——除 MMLU 外的 5 个基准仅在 Table 3 中各占一行数据，无结构分析。\n\n**W5** 标题中\"5,227 Models\"可能产生误导——核心时序分析仅用 1,887 个模型。"
  }
}
```

</details>

---


### Tool result

_source line 1410 · 2026-05-23T09:22:24.512432+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1519
}
```

</details>

---


### Assistant

_source line 1411 · 2026-05-23T09:22:27.245122+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 137

## Round 137

2 recorded events


### User

_source line 1412 · 2026-05-23T09:22:29.869809+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.5（Borderline Conference）**，Soundness 4/5，Excitement 3/5。

核心判断：
- **实证贡献扎实**：5,227 模型规模、多重控制链、6 个基准交叉验证、base-vs-instruct 反转模式（χ²=562.7）是论文的真正亮点
- **方法论新颖性有限**：MH-DIF 是 1988 年的成熟方法，三项"框架贡献"（cross-subject matching、DEFF correction、semi-synthetic validation）均为标准技术的领域适配，论文自己也承认"We do not modify the MH procedure"
- **两大 must-fix**：(1) 框架贡献被过度声称（overclaiming），与正文自述矛盾；(2) "两维度正交"的发现从构念定义即可预期，作为独立贡献包装不当
- **遗漏 CoDeC（ICLR 2026）** 等重要 concurrent work

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1413 · 2026-05-23T09:22:35.337095+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 138

## Round 138

2 recorded events


### User

_source line 1414 · 2026-05-23T09:24:20.489259+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE with nuance] R2-N1: 方法论贡献被过度声称**

R2 指出 cross-subject matching 是 purified subtest matching 的直接适配、DEFF 是标准调查方法学、semi-synthetic validation 是最简模拟——这些判断在技术层面成立。Section 2 (p.3) 明确写道 "We do not modify the MH procedure; our contribution is in the application context and the empirical findings it reveals"，但 Introduction 的 Contribution 3 又将 "Temporal DIF audit framework" 列为独立贡献——这两处表述确实存在张力。

但我认为 R2 的批评略显过度。Cross-subject matching 虽源自 purified subtest matching，但其在 LLM multi-domain benchmark 中的具体实现——用其他学科总分作为 matching variable 以隔离单学科污染——有其特定的方法论考量，特别是 Section 3.4 证明的 ΔFPR = 0 结构性保证（在单学科注入条件下）。这不是"拿来就用"，而是需要论证 matching variable 在新语境下的有效性。

**建议**：将 Contribution 3 重新表述为"标准 DIF 方法在 LLM 评估中的系统性适配与大规模实证验证"，而非暗示方法论创新。这样既承认了技术上的非原创性，也保留了应用层面的贡献。

---

**[REBUT] R2-N2: "两维度"贡献的新颖性存疑**

R2 认为 global exposure 和 differential functioning 在定义层面就是不同维度，因此低相关是可预期的结果。我不完全同意。

R2 的论点在心理测量学视角下是成立的——"暴露"和"功能差异"当然是可分离的概念。但在 NLP 社区的实际研究实践中，这一区分并未被广泛认识。现有的 contamination detection 文献（如 Li et al., 2024b 的 web-overlap；Shi et al., 2024 的 Min-K%++）隐含地假设"被污染的题目 = 测量失真的题目"。论文的实证贡献在于用大规模数据 **量化了** 这一预期中的关联实际上有多弱：Jaccard ≈ 0.206（Section 4.3），OR = 1.01（Section 4.3: "Association tests confirm near-independence"），DIF-C rates 对 web-contaminated 和 non-contaminated items 几乎相同（30.7% vs 另一组，差异极小）。

关键证据在 Figure 1（p.2）的 ICC 对照图：左图（global contamination）显示暴露本身不产生 DIF，而右图（differential contamination）才产生 DIF。这一视觉展示将概念区分转化为了可观察的经验模式。

不过，我同意论文的 framing 可以改进——将"两维度"从"surprising discovery"调整为"empirical quantification of a theoretically expected but previously unverified distinction"会更准确。

---

### Should-Fix

**[AGREE] R2-W1: 遗漏 concurrent work CoDeC (ICLR 2026)**

如果 CoDeC 确实是 ICLR 2026 发表的 contamination detection 相关工作，且在本文投稿前已公开（如 arXiv），则应在 Section 2 的 Related Work 中讨论。concurrent work 的遗漏是一个合理的完整性问题。但需核实 CoDeC 的具体发表时间线——如果在本文投稿后才公开，则不构成遗漏。

---

**[AGREE] R2-W2: 半合成验证的生态效度不足**

这与我自己的 N2 一致。Uniform binary flipping 是最简的注入模型，真实污染涉及部分记忆、格式特定优势、能力依赖效应。我在自己的审稿中已将此列为 Must-Fix，要求增加至少一种更现实的注入模型（如 difficulty-dependent flipping）。两位 reviewer 的一致意见增强了此修改请求的权重。

---

**[AGREE with nuance] R2-W3: 可操作性缺口**

R2 的观察有道理——论文 Section 5.2 推荐 "mechanism-conditional responses"（remove, annotate, or retain），但未给出判断标准。对于实践者来说，检测到 DIF 后的 next step 不明确。

但我认为这一批评应适度。DIF 分析本质上是诊断工具，不是处方——正如医学检测发现异常后需要后续临床判断。论文的贡献在于提供诊断能力，不必须解决所有下游决策问题。Section 5.2 已引用了 Kolen and Brennan (2014) 和 Habba et al. (2026) 作为 equating adjustments 的参考方向。

**建议**：在 Section 5.2 增加 1-2 句具体的决策启发式（如 "items with |Δ_MH| > 2.0 and concurrent web-overlap flags should be prioritized for removal"），但不要求完整的 decision framework。

---

**[REBUT] R2-W4: 非 MMLU 基准的分析深度不足**

R2 批评除 MMLU 外的 5 个 benchmark 仅在 Table 3 各占一行。但我认为这一设计是合理的：

1. MMLU 是最大的 benchmark（12,508 items, 5,227 models），也是 METABENCH 中结构最复杂的（57 subjects），因此作为 primary analysis 对象是自然的选择。
2. Table 3 的 cross-benchmark 分析目的是 **replication**，不是独立的 deep dive。6 个 benchmark 的 C% 一致性（17.9%–31.3%，knowledge-intensive consistently > procedural）已足以支撑泛化性。
3. 论文在 Appendix F 进一步提供了 cross-benchmark 细节。
4. 8 页正文限制下，将篇幅分配给 MMLU 的深度分析而非广度铺开是合理的取舍。

如果要求每个 benchmark 都做 LOFO、DEFF、within-family 等完整分析，论文会变成 6 篇论文的合集。Cross-benchmark 作为 robustness check 而非独立贡献，Table 3 的深度已足够。

---

**[REBUT] R2-W5: 标题中 "5,227 Models" 可能产生误导**

论文 Section 3.1 (p.4) 明确定义："The primary dataset is the METABENCH response matrix... which records binary outcomes (1 = correct, 0 = incorrect) for 5,227 models evaluated on 12,508 MMLU items." 所有 5,227 个模型都参与了 response matrix 的构建和 DIF 分析的不同层面：

- Temporal cohort (N=1,887) 是核心时序分析
- Ability-quartile cohort 使用全部模型
- Within-family, Within-subject, Random-split cohorts 使用不同子集
- DEFF 估计（Appendix D）使用全部 5,227 模型的 family 结构

标题说 "A Large-Scale Psychometric Audit of 5,227 Models" 描述的是审计范围（response matrix 的规模），而非暗示所有分析都使用全部 5,227 个模型。Section 3.3 (p.5) 清楚列出了每个 cohort 的具体 N 值。读者不会被误导。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1415 · 2026-05-23T09:24:43.132423+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 139

## Round 139

10 recorded events


### User

_source line 1416 · 2026-05-23T09:24:45.814206+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。总结：

- **R2-N1**（方法贡献过度声称）：[AGREE with nuance] — 技术组件确非原创，但 cross-subject matching 的 LLM 适配有实质考量，建议调整 framing 而非否定贡献
- **R2-N2**（两维度新颖性）：[REBUT] — 概念区分在心理测量学中不新，但在 NLP 社区中未被量化验证，Figure 1 的经验证据有独立价值
- **R2-W1**（遗漏 CoDeC）：[AGREE]，需核实时间线
- **R2-W2**（半合成生态效度）：[AGREE]，与我的 N2 一致
- **R2-W3**（可操作性缺口）：[AGREE with nuance]，DIF 本质是诊断工具，增加简要启发式即可
- **R2-W4**（非 MMLU 深度不足）：[REBUT]，cross-benchmark 作为 replication check 而非独立贡献，当前深度合理
- **R2-W5**（标题误导）：[REBUT]，5,227 描述审计范围，各 cohort N 值在正文清楚列出

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1417 · 2026-05-23T09:25:21.493274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1418 · 2026-05-23T09:25:21.493743+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1419 · 2026-05-23T09:25:21.595594+00:00_

1	issues:
2	  # === Round 14 issues ===
3	
4	  - id: "R14-W1"
5	    summary: "Framing 根本性张力：'temporal measurement instability' 暗示基准缺陷，但 DIF 无法区分 contamination / capability evolution / composition shift，且论文自身证据（ρ≈0.997 排名稳定、DIF items 集中最高区分度）与 'instability' 负面含义矛盾"
6	    category: framing
7	    severity: critical
8	    status: in_progress
9	    first_raised_round: 14
10	    last_seen_round: 14
11	    mentions:
12	      - round: 14
13	        reviewers: [1, 2]
14	        note: "R1-W-M1 + R2-W-F1 + R2-W-F2 共识。两位 reviewer 从不同角度独立得出相同结论。历史相关: R13-W1, R13-W8。"
15	    action_items:
16	      - round: 14
17	        action: "Paper Agent 综合重写: (1) 删 'not algorithmic' self-deprecation; (2) 统一术语为 'temporal DIF'; (3) §5.2 加 mechanism-conditional audit; (4) 引入 Camilli & Shepard (1994) impact vs bias 如验证为真; (5) 整合 composition control (Δ=1.08pp) 和 within-arch temporal DIF 数据排除替代解释"
18	        assigned_to: paper_agent
19	        status: in_progress
20	    resolution: ""
21	    resolution_round: null
22	
23	  - id: "R14-W2"
24	    summary: "DEFF 估计范围过宽（simple-mean 29.2% vs weighted-mean 13.5%），首选 simple-mean 的论证不够充分"
25	    category: method
26	    severity: warning
27	    status: in_progress
28	    first_raised_round: 14
29	    last_seen_round: 14
30	    mentions:
31	      - round: 14
32	        reviewers: [1, 2]
33	        note: "R1-W-M2 提出，R2 部分同意。历史相关: R13-W2。"
34	    action_items:
35	      - round: 14
36	        action: "Paper Agent: (1) 并列呈现两个估计; (2) 引用 DEFF simulation (artifacts/r22_deff_simulation/) 支持 simple-mean; (3) DEFF 详细数据移 appendix 减 enlargethispage"
37	        assigned_to: paper_agent
38	        status: in_progress
39	    resolution: ""
40	    resolution_round: null
41	
42	  - id: "R14-W3"
43	    summary: "Semi-synthetic 注入模型生态效度有限：binary response flipping ≠ realistic contamination"
44	    category: method
45	    severity: warning
46	    status: in_progress
47	    first_raised_round: 14
48	    last_seen_round: 14
49	    mentions:
50	      - round: 14
51	        reviewer
…[truncated 15495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 1420 · 2026-05-23T09:25:21.596280+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T09:10:25.991264+00:00\", \"completed_at\": \"2026-05-23T09:13:14.078079+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-6\", \"message\": \"连续 4 页无 figure/table（仅 p4 有 2 个小公式）。Method 段（§3）和 Experiments 开头（§4）全为纯文本，审稿人浏览时会感到节奏单调。建议将 Table 1 或 Figure 2 提前至 §3-4 附近，或新增一个方法流程图/数据示意图打破纯文本段。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"3 个 display items（Table 1 + Figure 2 + Table 2）堆积在同一页，与前 4 页的纯文本形成极端反差。视觉节奏严重不均——审稿人从\\\"文字沙漠\\\"突然进入\\\"图表风暴\\\"。建议将至少 1 个 table 前移或后移以平衡分布。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"正文 8 页共 5 个 display items（1 Figure + 3 Tables in main text + 1 Figure on p7），密度 0.625/页。对实证为主的论文偏低（参考值 5-8 个/9 页），但因论文兼有方法论贡献，尚可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页纯文本（Title + Abstract），无视觉锚点。Figure 1 出现在 page 2 顶部，位置合理。Figure 1（ICC 曲线图）清晰传达 global vs differential contamination 的核心区别，审稿人锚定效应正面。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 两面板设计清晰，曲线可区分，caption 自包含（描述了 Left/Right 面板含义及关键结论）。颜色方案可接受。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 剂量-反应曲线带置信区间，清晰可读。颜色区分度足够。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 和 Table 2 使用 booktabs 风格（无竖线），格式规范。N/A 值用破折号标注。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 3 加粗标注了关键数值，格式一致。Section 5（Discussion）、Section 6（Conclusion）和 Limitations 全部起始于 page 8，内容密度高但无溢出。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 在正文末尾开始（p8 底部），跨到 p9 顶部仅 2-3 行后转入 References。符合 EMNLP 要求（正文内单一 Limitations section）。\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"References 格式统一，无 [?] 未解析引用，无明显 overfull。\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"Appendix Figures 3-4 尺寸偏小（尤其 Figure 3 散点图和 Figure 4 柱状图），
…[truncated 530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 102
}
```

</details>

---
