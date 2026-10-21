# Director coordination — Part 1 of 7

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[Transcript overview](../director-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/3d/3daf92a3dbeb151a5ec1.json)

## Round 1

## Round 1

14 recorded events


### User

_source line 1 · 2026-05-20T21:41:52.896911+00:00_

[Reviewer 1 审稿意见]:
## R1 审稿意见：Methods & Experiments

**Paper:** "Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration"

---

## Summary

本文将 LLM 基准测试污染检测重新定义为心理测量学问题，核心思路是污染题目会表现出差异项目功能 (DIF)——对接触过训练数据的模型群体而言，这些题目变得异常容易，超出能力预测。论文在 5,219 个模型 × 12,508 个 MMLU 题目上进行了大规模 IRT 拟合诊断，构建了 DIF+ConStat 双信号集成检测器（AUROC 0.72），提出半合成验证框架，并通过 bifactor IRT 等值进行基准再生（holdout ρ=0.91）。实验覆盖面广（11 个实验组件），从 DIF 检测到集成融合、跨基准验证、贝叶斯累积 DIF、到题目生成与退化分析，涉及完整的技术栈。

---

## Preliminary Score: 4/6 (Weak Accept)

**一句话总结：** 概念新颖、规模令人印象深刻，但 DIF 标记的效度验证不充分（外部验证 κ=0.14）、推理 RL 鲁棒性声明样本严重不足（N=13），使核心贡献的可信度受损。

---

## Strengths (numbered)

**S1. 跨学科框架创新性极高。** 将 psychometrics 中成熟的 DIF 方法论引入 LLM 污染检测，是一个真正的概念贡献。DIF 在群体层面运作（population-level behavioral patterns），对单模型级别的输出平滑具有理论上的天然鲁棒性——这个论点在 §3.2 中论述清晰，且通过 Table 3 得到了经验支持（DIF AUROC 0.82-0.91 vs ConStat 0.51-0.75 on RL models）。

**S2. 分析规模与覆盖面。** 5,219 模型 × 12,508 题目的矩阵是目前已知最大的 IRT-for-LLM 分析之一。论文没有停留在单一实验，而是系统地覆盖了 IRT 拟合诊断（§4.1）、RL 鲁棒性（§4.2）、多信号集成（§5）、跨基准验证（§6.1）、半合成验证（§6.2）、累积贝叶斯 DIF（§6.3）、等值再生（§7）和退化分析（§7.3）——实验设计的完备性值得肯定。

**S3. 架构异质性的诊断与解决。** Table 5 清晰展示了全群体 RMSEA=0.105（poor fit）而 decoder-only 子群 RMSEA=0.068（acceptable），并正确识别架构异质性为 IRT 拟合的主要障碍。分层后 spurious DIF 减少 24%（Table 6），这是一个有方法论价值的发现。

**S4. 诚实报告负面结果。** DVD 检测器 AUROC 0.56 作为负面结果报告（Table 9），集成加入 DVD 后 AUROC 从 0.72 降为 0.70——论文没有回避这些结果。within-family 46% overlap、κ=0.14 外部验证等也均如实呈现。这种透明度在该领域不常见。

**S5. 退化分析提供实用边界。** Table 18 的 graceful degradation 分析给出了明确的操作阈值（~35% 替换为临界点），ρ 以 ~0.003/百分点线性退化——这为实际部署提供了可操作的安全边界。

---

## Weaknesses (numbered, with severity)

**W1 [Major] DIF 标记效度未得到充分验证——核心贡献的可信度存疑。**
- **位置：** §4.1 Within-Family Analysis (p.4), §6.1 GSM8K validation (p.7-8)
- **问题：** 论文的核心声明是 DIF 标记对应污染题目，但外部验证极其薄弱：
  - Director summary 提及 MMLU-CF 验证 κ=0.14, r=0.18——这本质上是随机一致水平，几乎没有验证价值
  - GSM8K 交叉验证 r=0.36（Table 11）统计显著但效应量弱，仅为"暗示性佐证"
  - Within-family 分析显示 46% overlap（p.4），意味着 54% 的全群体 DIF 标记可能仅由架构差异或能力增长驱动，而非真正的污染
- **为什么影响接收：** 如果无法区分 DIF 标记中的"真污染"和"能力进步"，整个检测管线的 precision 就是未知的。论文没有提供正式的 precision 估计（除了 Table 1 中的一列，但该 precision 的 ground truth 来源不明）。
- **建议：** (1) 使用已知干净的模型对（如同一 checkpoint 的 base vs fine-tuned on MMLU subset）构建有标注的验证集；(2) 明确讨论 κ=0.14 为何不构成否定证据（如果论文认为 MMLU-CF 本身有问题，应论证）。

**W2 [Major] 推理-RL 鲁棒性声明严重欠缺统计效力（N=13）。**
- **位置：** Table 3 (p.5), §4.2
- **问题：** RL 鲁棒性是论文的核心卖点之一（Abstract、§1、§3.2 均重点强调），但推理-RL 分析仅基于 13 个模型。在 N=13 下，AUROC 估计的 95% CI 约为 ±0.15-0.20（DeLong 正态近似）。论文报告 DIF AUROC 0.81 vs ConStat 0.51——但置信区间可能大幅重叠。DeLong p=0.002 是在对齐-RL（N=477）上报告的，不是在推理-RL（N=13）上。
- **为什么影响接收：** 推理-RL（o1、DeepSeek-R1 等）恰恰是论文声称最重要的前沿场景。在该场景下证据最薄弱，形成论文最大的"论点-证据"缺口。"Preliminary evidence"框架虽然诚实，但一个 top venue 论文的核心贡献不应建立在 preliminary evidence 上。
- **建议：** (1) 报告 N=13 下的 bootstrap CI 并讨论统计效力；(2) 如果无法获得更多推理-RL 模型，应将 RL 鲁棒性声明降级为辅助发现而非核心贡献；(3) 考虑 permutation test 而非 DeLong test 用于小样本。

**W3 [Major] 半合成验证存在循环性风险。**
- **位置：** §6.2 (p.8), Tables 12-13
- **问题：** 半合成验证从真实 METABENCH 响应矩阵中选取"200 clean items"并注入已知污染。但如何确认这 200 个 items 是真正 clean 的？如果它们已经包含自然污染（考虑到论文自身估计 14.6% 的 items 有 DIF），注入的污染会叠加在现有污染之上，导致 TPR 估计向上偏倚。论文声称 semi-synthetic TPR "consistently exceeds pure simulation by 3-8bps"（Table 13），但这个差异可能恰好反映了 existing contamination 的叠加效应。
- **建议：** (1) 描述"clean item"的选取标准，说明如何排除现有污染；(2) 用敏感性分析展示在不同 base contamination rates 下 TPR 如何变化；(3) 考虑从 non-MMLU 基准（无已知污染）构建 semi-synthetic 验证集。

**W4 [Major] 2PL 模型下 MMLU 的局部独立性假设可能严重违反。**
- **位置：** §3.1 (p.2), §4.1 (p.4)
- **问题：** 2PL IRT 要求局部独立性——给定能力值，题目间的响应应条件独立。但 MMLU 的 57 个学科内部，题目高度相关（同一学科的抽象代数题之间、同一学科的道德推理题之间）。论文在 §7.1 的 bifactor 模型中引入了学科特定因子来处理这个问题（p.9），但 §4.1-4.2 的核心 DIF 分析使用的是普通 2PL，未检测或处理局部依赖。
- 违反局部独立性会膨胀 Mantel-Haenszel 统计量，导致 DIF 假阳性率升高——这与 W1 中的效度问题叠加。
- **建议：** (1) 用 Yen's Q3 或 Chen & Thissen 的 LD 统计量检测局部依赖程度；(2) 展示在不同 LD 校正下 DIF 标记的稳定性；(3) 或者直接在 bifactor 模型上做 DIF 分析（§7.1 已有拟合好的 bifactor 模型）。

**W5 [Minor] Mantel-Haenszel 程序的选择未充分论证。**
- **位置：** §3.2 (p.3)
- **问题：** MH 是最经典的 DIF 方法之一，但也有明确的局限性：(1) 只能检测 uniform DIF（item characteristic curves 平行移动），对 non-uniform DIF（交叉 ICC）不敏感；(2) 在分层数增加时效力下降。论文的场景（5,219 模型、能力分布可能高度非正态）可能存在 non-uniform DIF。更强大的替代方案包括 logistic regression DIF（可同时检测 uniform 和 non-uniform DIF）和 SIBTEST。论文未讨论为何选择 MH 而非这些替代。
- **建议：** 至少用 logistic regression DIF 做一个对比实验，如果 MH 和 LR-DIF 一致则加强论点，不一致则表明 MH 可能遗漏了 non-uniform DIF。

**W6 [Minor] 多重比较校正缺失。**
- **位置：** §4.1 (p.4)
- **问题：** 对 12,508 个题目进行 MH 检验，产生 12,508 个 p 值。论文使用 ETS 效应量分类（A/B/C）而非 p 值阈值来标记 DIF，这部分缓解了多重比较问题。但 Table 1 中仍报告了 LR p-value，且 ETS 分类的 C 类阈值（|Δ_MH| ≥ 1.5 且显著）仍涉及 p 值判断。论文应讨论 FDR 控制策略。

**W7 [Minor] 集成 AUROC 0.72 的实用价值需要更多讨论。**
- **位置：** Table 10 (p.7), §5.3
- **问题：** AUROC 0.72 在检测任务中属于中等水平。在 FPR=0.085 的情况下，12,508 个题目中约 1,063 个会被误标为污染。论文缺乏对 positive predictive value (PPV) 在不同 base rate 下的讨论。如果真实污染率是 15%（论文估计），PPV ≈ 0.58×0.15 / (0.58×0.15 + 0.085×0.85) ≈ 0.55——约一半的标记是假阳性。
- **建议：** 加入 PPV 曲线或基于 base rate 的 precision-recall 分析。

**W8 [Minor] 再生题目质量退化的影响被低估。**
- **位置：** Table 16 (p.9), §7.1-7.2
- **问题：** 替换题目的因子载荷从 0.50 降至 0.41（-18%），区分度从 1.18 降至 0.95（-19%）。这意味着再生基准在心理测量学意义上不是等值的——它是一个较弱版本。ρ=0.91 的 holdout 相关看似不错，但排名位移的分布（89% 的模型移动 ≤3 个位置）意味着 11% 的模型会有显著排名变化。
- **建议：** (1) 分析排名变化是否与模型能力水平或架构类型相关（即退化是否系统性偏向某些模型）；(2) 讨论因子载荷/区分度下降对测试信息函数 (TIF) 的影响。

---

## Questions for Authors

**Q1.** Within-family 分析中 46% 的 overlap 率应如何正确解读？这 46% 是指全群体 DIF 标记中有 46% 被 within-family 分析确认，还是 within-family 标记中有 46% 也出现在全群体分析中？方向性对结论有根本影响。

**Q2.** κ=0.14（与 MMLU-CF 的一致性）为何不构成对 DIF 方法的否定证据？MMLU-CF 是目前已知最直接的污染标注，如果 DIF 标记与之几乎无关，需要给出有说服力的解释。

**Q3.** Table 3 中推理-RL 的 DeLong 检验 p 值具体是多少？是否独立于对齐-RL 的 p=0.002 报告？

**Q4.** 半合成验证中"clean items"的选取标准是什么？是否使用了 DIF 分析本身来选取 clean items——如果是，则存在循环论证。

**Q5.** Bifactor 模型（§7.1）中学科特定因子的方差解释比例是多少？如果学科特定因子解释了大量方差，这是否意味着在普通 2PL 上的 DIF 分析（§4.1）受到了严重的局部依赖污染？

**Q6.** 论文提到 IFT（§5.1）识别的中位分割点为 2023 年 9 月，与已知的大规模网页爬取时间线一致。但这也可能对应 GPT-4 发布后的模型能力跳跃——如何区分这两种解释？

---

## Missing Experiments/Analyses

1. **局部依赖诊断（Yen's Q3 或类似）**：验证 2PL 在 MMLU 上的局部独立性假设是否合理。
2. **在 bifactor 模型上进行 DIF 分析**：论文已拟合了 bifactor 模型（§7.1），应在该模型上重做 DIF 并对比 2PL 结果。
3. **已知污染模型的 controlled validation**：用同一 base model 的 clean 版本和 fine-tuned-on-MMLU 版本构建真正的 ground truth。
4. **PPV/NPV at plausible base rates**：将 AUROC 转化为实际决策性能。
5. **Non-uniform DIF 检测**：用 logistic regression DIF 或 IRT-LR 检测交叉 DIF。
6. **推理-RL 的 bootstrap CI**：量化小样本下 AUROC 估计的不确定性。
7. **替换题目质量退化的系统性分析**：TIF 对比、能力估计偏差分析。

---

## 维度打分（基于 ICLR review 标准 + Director 指定的 6 分制）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Novelty / Originality | 5/6 | DIF 用于 LLM 污染检测是真正的跨学科创新，bifactor equating for regeneration 也有新意 |
| Soundness / Correctness | 3/6 | 核心 DIF 标记的效度验证不充分（κ=0.14）；2PL 局部独立性假设可能严重违反；推理-RL 样本太小 |
| Significance / Impact | 4/6 | 问题重要且实用，但 AUROC 0.72 + 再生质量退化限制了实际影响 |
| Clarity / Presentation | 4/6 | 实验覆盖面广但10页内压缩过多内容（11个实验组件），部分关键细节只能在 Director summary 中找到而非论文正文 |
| Reproducibility | 3/6 | 依赖 METABENCH 数据但未明确可复现步骤；IRT 拟合的具体实现细节不足（优化器、收敛标准等） |
| Overall | **4/6 (Weak Accept)** | 概念贡献显著，实验规模令人印象深刻，但方法论核心（DIF 效度验证、RL 鲁棒性统计效力、局部独立性）存在需要作者回应的重要缺陷 |

**Confidence: 4/5** — 我熟悉 IRT 和 DIF 方法论，对实验设计的评估有较高把握；对 METABENCH 数据集的具体特性了解有限。

---

## 总结判断

这是一篇有野心、有创意的论文，将心理测量学的经典工具引入了一个 ML 社区非常关心的问题。跨学科的概念贡献是清晰的。但"DIF 标记 = 污染"这个核心等式缺乏令人信服的外部验证（κ=0.14 本质上是随机水平），推理-RL 鲁棒性——论文最强调的实用卖点——仅有 N=13 的支持。如果作者能提供更有力的效度验证（如 controlled contamination 实验）并坦诚量化推理-RL 下的统计不确定性，这篇论文将有力地向 Accept 移动。当前状态下，Weak Accept——概念够强，执行需加固。

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

_source line 2 · 2026-05-20T21:42:05.286595+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-20T21:42:05.287074+00:00_



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

_source line 4 · 2026-05-20T21:42:08.096093+00:00_

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

_source line 5 · 2026-05-20T21:42:08.197008+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (5 个)\n\n- **plan_011_semi_synthetic_validation**: PREPARING — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_011_semi_synthetic_validation（准备中）\n\n## 近期结论\n- **plan_001b_matched_ability_dif** (negative): 在每个 accuracy quintile 内部做 temporal cohort MH-DIF（控制能力后），enrichment 将从 plan_001 的 0.96 提升到 >1.5，证明能力匹配能隔离出污染信号。 ← 基于 plan_001_real_data_dif_mmlu\n- **plan_001_real_data_dif_mmlu** (negative): MH-DIF 在 METABENCH 真实 MMLU 数据（5227 模型 × 12508 items）上，用时间 cohort (2023 vs 2024) 和能力分位 cohort 分组时，ETS C 标记的 items 在 Li et al. clean items 中的 FPR ≤ 0.05，且 ETS C 标记在 contaminated items 中的比例显著高于 clean items。这验证 DIF 在真实数据上不会产生过多假阳性，且能捕捉到与 web-overlap 污染信号一致的差异性。 ← 基于 mvp_dif_power_sim_phase2\n  [plan_001_analysis_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/plan_001_analysis.py) | [plan_001_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md) | [dif_results_temporal](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal.csv) | [dif_results_ability](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability.csv) | [dif_summary](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv) | [within_family_dif](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/within_family_dif.csv) | [cross_analysis](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/cross_analysis.csv) | [d
…[truncated 1333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-20T21:42:11.208615+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
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
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-20T21:42:11.259353+00:00_



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

_source line 8 · 2026-05-20T21:42:16.279318+00:00_

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

_source line 9 · 2026-05-20T21:42:16.330875+00:00_

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

_source line 10 · 2026-05-20T21:42:16.331242+00:00_

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

_source line 11 · 2026-05-20T21:42:16.432049+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_started\"}, \"error\": null, \"metadata\": {}}"}

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

_source line 12 · 2026-05-20T21:42:26.873603+00:00_

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

_source line 13 · 2026-05-20T21:42:26.874451+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 14 · 2026-05-20T21:42:51.511885+00:00_

R1 审稿意见已收到。评分 4/6 (Weak Accept)，置信度 4/5。

**R1 核心发现摘要：**

| 严重性 | 编号 | 问题 |
|--------|------|------|
| Major | W1 | DIF 标记效度验证不充分（外部验证 κ=0.14 ≈ 随机水平） |
| Major | W2 | 推理-RL 鲁棒性声明仅 N=13，统计效力严重不足 |
| Major | W3 | 半合成验证存在循环性风险（"clean items"选取标准不明） |
| Major | W4 | 2PL 局部独立性假设可能在 MMLU 57 学科内严重违反 |
| Minor | W5 | MH 方法选择未论证（未对比 logistic regression DIF） |
| Minor | W6 | 12,508 次检验的多重比较校正缺失 |
| Minor | W7 | 集成 AUROC 0.72 的 PPV 在 15% base rate 下仅 ~0.55 |
| Minor | W8 | 再生题目质量退化（因子载荷 -18%，区分度 -19%）影响被低估 |

R1 审稿质量高——既有方法论深度（IRT/DIF 专业评估），也有统计严谨性（CI 估算、PPV 推导）。关键攻击点集中在**效度验证链条**（W1→W3→W4 形成连锁质疑）和**小样本 RL 声明**（W2）。

等待 Reviewer 2 审稿意见返回后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 2

## Round 2

8 recorded events


### User

_source line 15 · 2026-05-20T21:42:52.604328+00:00_

[Reviewer 1 审稿结果]:
R1 审稿意见已提交至 Review Director。

**评分：4/6 (Weak Accept)**

核心发现：
- **最大优势**：DIF 用于 LLM 污染检测是真正的跨学科概念创新，实验规模（5,219×12,508）和覆盖面（11 个实验组件）令人印象深刻
- **最大问题**：(1) DIF 标记效度验证不足——与 MMLU-CF 一致性 κ=0.14 本质上是随机水平；(2) 推理-RL 鲁棒性声明仅有 N=13 支持，统计效力严重不足；(3) 2PL 局部独立性假设在 MMLU 57 学科结构下可能严重违反；(4) 半合成验证存在循环性风险

识别了 4 个 Major weakness、4 个 Minor weakness、6 个作者需回答的问题、7 个缺失实验/分析。

---

[Reviewer 2 审稿意见]:
## R2 审稿报告：Novelty & Related Work

**Paper:** "Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: Differential Item Functioning at Scale"

---

## 总体评分

**Overall**: 3/6 (Borderline Reject)

**一句话总结**: 将成熟心理测量工具（DIF）迁移到 LLM 污染检测的概念框架有价值，但新颖性有限、关键引用存在严重错误（至少两处作者/方法名张冠李戴），且核心贡献的实证支撑过窄，难以达到 top venue 门槛。

---

## 官方维度打分（参照 ICLR 2026 review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法论本身合理，但 RL 鲁棒性仅 13 模型验证、ensemble 反而不如单一 DIF、42% within-family 混淆未解决 |
| Novelty/Contribution | 2/5 | DIF 是 1988 年的经典技术，迁移到 LLM 域的概念跳跃有限；ensemble 组合机械；bifactor equating 仅 pilot 规模 |
| Presentation | 3/5 | 结构清晰、limitations 诚实，但引用错误严重损害学术可信度 |
| Significance | 3/5 | 问题重要且实际，但方法的适用边界条件太窄（仅大效应、需架构同质性），实际可部署性存疑 |
| Reproducibility | 2/5 | 未提供代码或数据；semi-synthetic 验证依赖特定 METABENCH 子集；关键参考文献无法核实 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 引用严重错误：多处引用的作者名和方法名与真实文献不符

- 具体位置：Section 4.1 "Iron-Fenced Trees (IFT) following Tets & Berger (2016)" 及 Table 7
- 问题：真实文献为 **Tutz & Berger (2016) "Item-Focussed Trees for the Identification of Items in Differential Item Functioning"**（Psychometrika）。论文中 (a) 作者名 "Tets" 应为 "Tutz"，(b) 方法名 "Iron-Fenced Trees" 应为 "Item-Focussed Trees"。两个关键标识符均错误，呈现典型的 LLM 幻觉特征。此外，"Dunn et al. (2024)" 引用的 DVD 方法，实际论文为 **Liang et al. (2026)** (arXiv:2601.04895)，作者和年份均不符。
- 为什么影响接收：引用准确性是学术论文的基本要求。多处引用的作者名/方法名/年份同时出错，严重损害论文的学术可信度，在 top venue 审稿中这是致命问题。
- 建议修改方向：逐一核实所有引用的作者名、标题、年份和出版信息。

**N2** [critical] DIF 迁移的新颖性不足以支撑核心贡献声明

- 具体位置：Abstract（5条贡献声明）、Section 1 Introduction
- 问题：DIF 是 Holland & Thayer (1988) 提出的经典心理测量技术，Mantel-Haenszel 程序是标准教科书方法。将 DIF 应用于 LLM 污染检测的核心概念跳跃是：将"污染前/后模型群体"映射为 DIF 的 reference/focal group。这一映射虽然合理，但在概念上是 straightforward 的——任何熟悉 DIF 和 LLM 评测的研究者都能想到这一步。论文未在 DIF 方法本身上做出任何技术创新（未修改统计量、未提出新的 effect size 度量、未解决 LLM 特有的建模挑战如极端 item-response 稀疏性等）。
- 为什么影响接收：top venue 要求的不仅是"将已有方法应用到新领域"，还需要在应用过程中解决新的技术挑战或产生非显然的洞见。
- 建议修改方向：(1) 明确阐述 LLM 群体相对于人类测试群体的独特建模挑战（如零/满分模式远多于人类、item 数极大）及对应的方法适配；(2) 或承认本文的核心贡献是实证而非方法论，相应调整 claim 的力度。

**N3** [critical] Ensemble (DIF+ConStat) 反而不如单独 DIF，削弱核心贡献

- 具体位置：Table 10（Section 5.3）、Abstract 中 "AUROC 0.72"
- 问题：Abstract 宣称 "DIF+ConStat dual-signal ensemble (AUROC 0.72)" 为核心贡献。但 Table 10 显示 DIF 单独的 TPR 在 δ≥1.4 时已达 0.78，ensemble 的 full union 策略 Coverage 0.72 实际上并未带来一致性提升。论文自己也承认 "ConStat adds FPR"。如果组合两个方法反而降低性能，那这个 ensemble 就不构成贡献——它证明了简单组合是行不通的，这其实是一个**负面结果**。
- 为什么影响接收：将负面结果包装为正面贡献是 framing 问题。如果诚实呈现为"ensemble 不奏效的发现"反而更有价值。
- 建议修改方向：将 ensemble 结果重新定位为消融分析或负面发现，而非核心贡献。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] RL 鲁棒性声明的实证基础过窄

- 具体位置：Section 4.2、Table 3
- 问题：RL 鲁棒性是论文区别于 Wang et al. (2026) 的核心差异化论点，但仅在 13 个 reasoning-RL 模型上验证。Table 3 显示 DIF (ETS C) 在 reasoning-RL 上 AUROC 0.91——看似强劲，但 N=13 的统计效力极低，置信区间必然极宽。论文未报告置信区间或 bootstrap 不确定性。更关键的是，这 13 个模型全部来自有限的几个 model family（论文未列出），可能存在严重的选择偏差。
- 建议：(1) 报告 bootstrap 置信区间；(2) 列出 13 个模型的具体名称和家族分布；(3) 如果置信区间宽到无法排除随机，应降低 claim 力度。

**W2** [warning] 与 Growing Pains (Zhang et al., 2026) 的区分不够清晰

- 具体位置：Section 2（Related Work）、Section 7.1（Bifactor IRT Equating）
- 问题：Growing Pains 也使用多维 IRT 进行 LLM 评估，并解决了跨时间的可比性问题（通过 fixed parameter calibration + anchor items）。本文的 bifactor IRT equating（Section 7.1）在方法层面与 Growing Pains 的 IRT 建模高度相似。论文在 Related Work 中仅用一句话带过 Growing Pains，未充分讨论两者在 IRT 建模选择（bifactor vs multidimensional）、应用目标（污染检测 vs 效率评估）、和实验设计上的异同。
- 建议：增加与 Growing Pains 的详细对比段落，明确本文的 bifactor 选择相对于 Growing Pains 的 multidimensional 框架有何理论或实证优势。

**W3** [warning] Wang et al. (2026) 引用无法核实

- 具体位置：Section 1、Section 4.2
- 问题：Wang et al. (2026) "contamination signals vanish after RL" 是本文 RL 鲁棒性论点的关键前提。但我通过多次搜索无法找到完全匹配的论文（找到了 arXiv:2510.09259 和 2507.10532 等相关工作，但均非 "Wang et al. 2026 ICLR"）。如果这条引用不可靠，论文的核心 motivation 之一就失去了文献支撑。
- 建议：提供该引用的完整信息（arXiv ID 或 DOI），确保可核实。

**W4** [warning] 42% within-family overlap 混淆未得到充分解决

- 具体位置：Section 4.1（Within-Family Analysis）
- 问题：论文发现 46% 的 DIF flags 与 full-population 结果重叠，说明架构异质性是 DIF 检测的主要混淆因素。虽然论文将此识别为问题并提出了 architecture stratification 和 IFT 作为缓解手段，但 Table 6 显示 stratification 后仍有系统性残余（decode-only subset 的 anchor items 仅 125 个，下降了数量级）。这实质上意味着 DIF 在异质群体上的 false positive 率很高，论文的"14.6% flagged items"中有多少是真正的污染 vs 架构差异？这个根本问题没有得到令人信服的回答。
- 建议：提供 stratified 分析的 precision/recall 而非仅 flag rate；或承认 within-family 场景下 DIF 的 practical utility 有限。

**W5** [warning] 贡献数量膨胀

- 具体位置：Abstract
- 问题：Abstract 列出 5 条贡献，但仔细审视：(1) IRT fit diagnostics 主要是负面发现（架构异质性阻碍 fit）而非方法贡献；(2) ensemble AUROC 0.72 如前述实际是负面结果；(3) semi-synthetic 验证框架是方法学贡献但 novelty 有限；(4) bifactor equating 仅 pilot 规模；(5) power surface 是有价值的分析工具。将 5 条缩减为 2-3 条核心贡献会让论文更聚焦可信。
- 建议：合并/精简贡献声明，突出真正具有 novelty 的部分（DIF-based 检测 + power surface + 再生 pipeline），对其余做诚实定位。

---

## 小问题（不影响接收）

- Section 3.2 中 ETS classification 的 A/B/C 阈值直接沿用人类测试的标准（Δ_MH），未讨论这些阈值对 LLM 群体是否合适。LLM 的 effect size 分布可能与人类显著不同。
- Table 4 的 "detection power surface" 是有用的分析，但 "three-parameter" 的说法（Abstract contribution 5）暗示了一个连续的 parametric model，实际上只是一个 3D grid search。
- GSM8K 交叉验证 r=0.36 被描述为 "provides independent cross-benchmark evidence"（Section 6.1），但 r=0.36 仅为中等相关，解释变异不到 13%。这应被更谨慎地呈现。
- "at Scale" 在标题中使用，但 GSM8K 验证仅 60 个模型、RL 验证仅 13 个模型。真正大规模的仅 METABENCH 上的 MMLU 实验（3,219 模型），标题有过度概括之嫌。

---

## 缺失的相关工作

1. **Membership Inference Attacks (MIA) 用于污染检测**：Shi et al. (2024) 提出 Min-K%++ 等基于 MIA 的污染检测方法，与 DIF 的群体级方法形成对比（individual-level vs population-level）。论文未讨论这一重要类别。

2. **IRT 在 NLP/AI 评测中的先行工作**：Lalor et al. (2019) "Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds" 是 IRT 应用于 NLP 的早期工作；Vania et al. (2021) 用 IRT 分析 NLU benchmark。这些工作建立了 IRT-for-LLM 的先例，应在 Related Work 中承认。

3. **动态/自适应 Benchmark 方案**：除 LiveBench 外，还有 Dynabench (Kiela et al., 2021)、ChatBot Arena (Zheng et al., 2024) 的 ELO 系统、以及 HELM (Liang et al., 2023) 的持续更新方案。这些都是"benchmark regeneration"的替代路径，论文应讨论其 trade-off。

4. **N-gram/perplexity 基线方法**：GPT-4 technical report 中使用的 n-gram overlap 方法、以及 Carlini et al. 的 memorization 检测方法，这些是最简单的污染检测基线，论文未将 DIF 与之对比。

5. **Benchmark 污染的 survey 文献**：Balloccu et al. (2024) "Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs" 等 survey 提供了更全面的 contamination 分类框架。

---

## 主要优势

1. **问题重要且及时**：LLM benchmark 污染是社区的核心痛点，将心理测量学的成熟工具引入该问题域是合理的研究方向。
2. **Limitations 和 boundary conditions 的诚实呈现**：Section 6 和 Section 8 中对架构同质性要求、大效应限制、reasoning-RL gap、28% 替换阈值等边界条件的明确说明，在同类工作中属于高标准，值得赞赏。
3. **负面结果有社区价值**：DVD 的 AUROC 0.56、MMLU-CF 的 κ=0.14 低可靠性，以及 ensemble 不优于单一 DIF 的发现，都是对后续研究者有用的信息。
4. **Power surface 分析**：Table 4 的 detection power 随 exploitation rate 和 effect size 的变化分析（Section 4.2）是一个实用的分析框架，帮助研究者判断 DIF 检测在具体场景下是否可行。
5. **Benchmark regeneration pipeline 的初步尝试**：Section 7 的 bifactor equating + item generation + graceful degradation 分析构成了从"检测"到"修复"的完整框架，尽管是 pilot 规模，方向正确。

---

## 给作者的问题

1. 请确认 "Tets & Berger (2016)" 是否应为 "Tutz & Berger (2016)"，"Iron-Fenced Trees" 是否应为 "Item-Focussed Trees"？请同时确认 DVD 的引用信息。
2. Table 10 中 ensemble 的最优策略 (weighted) 的 cross-validation 细节是什么？权重是如何选择的？是否存在过拟合风险？
3. 如果将 DIF 的贡献定位为"实证发现"（即 DIF 在 LLM 污染检测中有效）而非"方法论创新"，作者如何重新组织论文的叙事？
4. 13 个 reasoning-RL 模型的完整列表是什么？它们覆盖了多少个独立的 model family？
5. ETS classification 的 A/B/C 阈值是为人类测试群体校准的。作者是否考虑过这些阈值对 LLM 群体可能不适用？是否进行过阈值敏感性分析？
6. Growing Pains 的 fixed parameter calibration 在理论上也可以检测污染（污染 item 的参数估计会在新旧 cohort 之间不一致）。为什么选择 DIF 而非 Growing Pains 的框架？

---

**总结**：论文选择了一个重要且及时的问题，提出的心理测量学视角有独到之处。但核心新颖性有限（成熟技术的 straightforward application）、引用存在严重错误（至少 2 处作者/方法名张冠李戴）、关键实证验证过窄（13 模型 RL 测试、ensemble 不优于单一方法），综合评判处于 borderline reject。如果引用问题能修复、contribution framing 能调整为更诚实的实证定位、并补充更充分的 RL 鲁棒性验证，有潜力达到 borderline accept。

---

[Reviewer 2 审稿结果]:
R2 审稿报告已提交给 Review Director。

核心发现：
- **评分 3/6 (Borderline Reject)**
- **致命问题**：至少 2 处引用严重错误（"Tets & Berger" 应为 Tutz & Berger，"Iron-Fenced Trees" 应为 Item-Focussed Trees；DVD 引用的作者和年份均不符），损害学术可信度
- **新颖性有限**：DIF 是 1988 年的经典技术，迁移到 LLM 域的概念跳跃 straightforward；ensemble 反而不如单独 DIF
- **实证过窄**：RL 鲁棒性仅 13 模型验证，42% within-family 混淆未解决
- **优势**：问题重要、limitations 呈现诚实、负面结果有社区价值、power surface 分析实用

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

_source line 16 · 2026-05-20T21:43:11.259315+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
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
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-20T21:43:11.310874+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-20T21:43:39.726008+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重 Novelty & Related Work）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R2 审稿报告：Novelty & Related Work\n\n**Overall**: 3/6 (Borderline Reject)\n\n**一句话总结**: 将成熟心理测量工具（DIF）迁移到 LLM 污染检测的概念框架有价值，但新颖性有限、关键引用存在严重错误（至少两处作者/方法名张冠李戴），且核心贡献的实证支撑过窄，难以达到 top venue 门槛。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 引用严重错误：多处引用的作者名和方法名与真实文献不符\n- Section 4.1 \"Iron-Fenced Trees (IFT) following Tets & Berger (2016)\" — 真实文献为 Tutz & Berger (2016) \"Item-Focussed Trees\"（Psychometrika）。作者名 \"Tets\" 应为 \"Tutz\"，方法名 \"Iron-Fenced Trees\" 应为 \"Item-Focussed Trees\"。此外 \"Dunn et al. (2024)\" 引用的 DVD 方法，实际论文为 Liang et al. (2026)。\n\n**N2** [critical] DIF 迁移的新颖性不足以支撑核心贡献声明\n- DIF 是 Holland & Thayer (1988) 的经典技术，将\"污染前/后模型群体\"映射为 reference/focal group 的概念跳跃是 straightforward 的。论文未在 DIF 方法本身做出技术创新。\n\n**N3** [critical] Ensemble (DIF+ConStat) 反而不如单独 DIF，削弱核心贡献\n- Table 10 显示 DIF 单独的 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升。将负面结果包装为正面贡献是 framing 问题。\n\n### Should-Fix 问题\n\n**W1** RL 鲁棒性声明的实证基础过窄（13 模型，无 bootstrap CI）\n**W2** 与 Growing Pains (Zhang et al., 2026) 的区分不够清晰\n**W3** Wang et al. (2026) 引用无法核实\n**W4** 42% within-family overlap 混淆未得到充分解决\n**W5** 贡献数量膨胀（5条应缩减为2-3条）\n\n### 缺失的相关工作\n1. MIA 用于污染检测（Shi et al., 2024 Min-K%++）\n2. IRT 在 NLP/AI 评测中的先行工作（Lalor et al., 2019; Vania et al., 2021）\n3. 动态/自适应 Benchmark 方案（Dynabench, ChatBot Arena, HELM）\n4. N-gram/perplexity 基线方法\n5. Benchmark 污染 survey（Balloccu et al., 2024）\n\n### 主要优势\n1. 问题重要且及时\n2. Limitations 诚实呈现\n3. 负面结果有社区价值\n4. Power surface 分析实用\n5. Benchmark regeneration pipeline 方向正确\n\n### 给作者的问题\n1. 确认引用错误（Tets→Tutz, Iron-Fenced→Item-Focussed, DVD 引用）\n2. Ensemble 权重的 cross-validation 细节和过拟合风险\n3. 如果将贡献定位为\"实证发现\"而非\"方法论创新\"，如何重组叙事？\n4. 13 个 reasoning-RL 模型的完整列表和 family 分布\n5. ETS A/B/C 阈值对 LLM 群体是否适用？\n6. 为什么选择 DIF 而非 Growing Pains 的框架？\n\n---\n\n**请对以上所有 Must-Fix、Should-Fix、缺失相关工作、优势评价逐条回应 [AGREE] 或 [REBUT]。** 特别关注：\n1. 你是否同意 R2 对新颖性的评价（2/5）？你给了 5/6——这是最大分歧点，请详细论证。\n2. 引用错误问题你在初审中未提及，你认为这对论文可信度的影响有多大？\n3. Ensemble 到底是正面贡献还是负面结果？"
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
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重 Novelty & Related Work）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R2 审稿报告：Novelty & Related Work\n\n**Overall**: 3/6 (Borderline Reject)\n\n**一句话总结**: 将成熟心理测量工具（DIF）迁移到 LLM 污染检测的概念框架有价值，但新颖性有限、关键引用存在严重错误（至少两处作者/方法名张冠李戴），且核心贡献的实证支撑过窄，难以达到 top venue 门槛。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] 引用严重错误：多处引用的作者名和方法名与真实文献不符\n- Section 4.1 \"Iron-Fenced Trees (IFT) following Tets & Berger (2016)\" — 真实文献为 Tutz & Berger (2016) \"Item-Focussed Trees\"（Psychometrika）。作者名 \"Tets\" 应为 \"Tutz\"，方法名 \"Iron-Fenced Trees\" 应为 \"Item-Focussed Trees\"。此外 \"Dunn et al. (2024)\" 引用的 DVD 方法，实际论文为 Liang et al. (2026)。\n\n**N2** [critical] DIF 迁移的新颖性不足以支撑核心贡献声明\n- DIF 是 Holland & Thayer (1988) 的经典技术，将\"污染前/后模型群体\"映射为 reference/focal group 的概念跳跃是 straightforward 的。论文未在 DIF 方法本身做出技术创新。\n\n**N3** [critical] Ensemble (DIF+ConStat) 反而不如单独 DIF，削弱核心贡献\n- Table 10 显示 DIF 单独的 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升。将负面结果包装为正面贡献是 framing 问题。\n\n### Should-Fix 问题\n\n**W1** RL 鲁棒性声明的实证基础过窄（13 模型，无 bootstrap CI）\n**W2** 与 Growing Pains (Zhang et al., 2026) 的区分不够清晰\n**W3** Wang et al. (2026) 引用无法核实\n**W4** 42% within-family overlap 混淆未得到充分解决\n**W5** 贡献数量膨胀（5条应缩减为2-3条）\n\n### 缺失的相关工作\n1. MIA 用于污染检测（Shi et al., 2024 Min-K%++）\n2. IRT 在 NLP/AI 评测中的先行工作（Lalor et al., 2019; Vania et al., 2021）\n3. 动态/自适应 Benchmark 方案（Dynabench, ChatBot Arena, HELM）\n4. N-gram/perplexity 基线方法\n5. Benchmark 污染 survey（Balloccu et al., 2024）\n\n### 主要优势\n1. 问题重要且及时\n2. Limitations 诚实呈现\n3. 负面结果有社区价值\n4. Power surface 分析实用\n5. Benchmark regeneration pipeline 方向正确\n\n### 给作者的问题\n1. 确认引用错误（Tets→Tutz, Iron-Fenced→Item-Focussed, DVD 引用）\n2. Ensemble 权重的 cross-validation 细节和过拟合风险\n3. 如果将贡献定位为\"实证发现\"而非\"方法论创新\"，如何重组叙事？\n4. 13 个 reasoning-RL 模型的完整列表和 family 分布\n5. ETS A/B/C 阈值对 LLM 群体是否适用？\n6. 为什么选择 DIF 而非 Growing Pains 的框架？\n\n---\n\n**请对以上所有 Must-Fix、Should-Fix、缺失相关工作、优势评价逐条回应 [AGREE] 或 [REBUT]。** 特别关注：\n1. 你是否同意 R2 对新颖性的评价（2/5）？你给了 5/6——这是最大分歧点，请详细论证。\n2. 引用错误问题你在初审中未提及，你认为这对论文可信度的影响有多大？\n3. Ensemble 到底是正面贡献还是负面结果？"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-20T21:44:18.069993+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 38343
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-20T21:44:18.321928+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重 Methods & Experiments）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R1 审稿意见：Methods & Experiments\n\n**Preliminary Score: 4/6 (Weak Accept)**\n\n**一句话总结：** 概念新颖、规模令人印象深刻，但 DIF 标记的效度验证不充分（外部验证 κ=0.14）、推理 RL 鲁棒性声明样本严重不足（N=13），使核心贡献的可信度受损。\n\n### Strengths\n\n**S1.** 跨学科框架创新性极高。DIF 在群体层面运作，对单模型级别的输出平滑具有理论上的天然鲁棒性。Table 3 得到经验支持（DIF AUROC 0.82-0.91 vs ConStat 0.51-0.75 on RL models）。\n\n**S2.** 分析规模与覆盖面。5,219 模型 × 12,508 题目，11 个实验组件系统覆盖。\n\n**S3.** 架构异质性的诊断与解决。Table 5 全群体 RMSEA=0.105 vs decoder-only RMSEA=0.068，分层后 spurious DIF 减少 24%（Table 6）。\n\n**S4.** 诚实报告负面结果。DVD AUROC 0.56，κ=0.14 外部验证均如实呈现。\n\n**S5.** 退化分析提供实用边界。Table 18 ~35% 替换为临界点，ρ 以 ~0.003/百分点线性退化。\n\n### Weaknesses\n\n**W1 [Major]** DIF 标记效度未得到充分验证。MMLU-CF 验证 κ=0.14, r=0.18 本质上是随机一致水平；GSM8K r=0.36 效应量弱；within-family 46% overlap 意味着 54% 可能由架构差异驱动。\n\n**W2 [Major]** 推理-RL 鲁棒性声明严重欠缺统计效力（N=13）。AUROC 估计的 95% CI 约为 ±0.15-0.20。DeLong p=0.002 是在对齐-RL（N=477）上报告的，不是推理-RL。\n\n**W3 [Major]** 半合成验证存在循环性风险。\"200 clean items\" 如何确认真正 clean？如果包含自然污染，TPR 向上偏倚。\n\n**W4 [Major]** 2PL 模型下 MMLU 的局部独立性假设可能严重违反。57 个学科内部题目高度相关，但核心 DIF 分析使用普通 2PL 未处理局部依赖。\n\n**W5 [Minor]** MH 程序的选择未充分论证（未考虑 non-uniform DIF）。\n**W6 [Minor]** 多重比较校正缺失。\n**W7 [Minor]** 集成 AUROC 0.72 的实用价值需更多讨论（PPV ≈ 0.55）。\n**W8 [Minor]** 再生题目质量退化的影响被低估（因子载荷 -18%，区分度 -19%）。\n\n### Questions for Authors\nQ1. 46% overlap 的方向性解读？\nQ2. κ=0.14 为何不构成否定证据？\nQ3. 推理-RL 的 DeLong p 值具体是多少？\nQ4. 半合成验证中 clean items 的选取标准？\nQ5. Bifactor 模型学科特定因子的方差解释比例？\nQ6. IFT 分割点 2023 年 9 月——如何区分污染 vs 能力跳跃？\n\n### Missing Experiments\n1. 局部依赖诊断（Yen's Q3）\n2. 在 bifactor 模型上做 DIF 分析\n3. Controlled validation（已知污染模型）\n4. PPV/NPV at plausible base rates\n5. Non-uniform DIF 检测（logistic regression DIF）\n6. 推理-RL bootstrap CI\n7. 替换题目质量退化的系统性分析（TIF 对比）\n\n### 维度打分\n| 维度 | 分数 |\n|------|------|\n| Novelty / Originality | 5/6 |\n| Soundness / Correctness | 3/6 |\n| Significance / Impact | 4/6 |\n| Clarity / Presentation | 4/6 |\n| Reproducibility | 3/6 |\n| Overall | 4/6 (Weak Accept) |\n\n---\n\n**请对以上所有 Strengths、Weaknesses、Questions、Missing Experiments 逐条回应 [AGREE] 或 [REBUT]。** 特别关注：\n\n1. **新颖性分歧**：R1 给 Novelty 5/6，你给 2/5。这是最大分歧点。R1 认为\"将 psychometrics 中成熟的 DIF 方法论引入 LLM 污染检测是一个真正的概念贡献\"——你是否仍然坚持 2/5？请详细论证。\n2. **局部独立性问题（W4）**：R1 提出 2PL 在 MMLU 57 学科结构下的局部独立性违反是 Major weakness，你在初审中未提及此问题。你是否同意这是一个重要方法论缺陷？\n3. **半合成验证循环性（W3）**：R1 指出 clean items 选取可能存在循环论证，你如何看？\n4. **PPV 问题（W7）**：R1 估算 PPV ≈ 0.55（约一半标记是假阳性），这是否改变你对方法实用性的评估？"
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
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重 Methods & Experiments）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R1 审稿意见：Methods & Experiments\n\n**Preliminary Score: 4/6 (Weak Accept)**\n\n**一句话总结：** 概念新颖、规模令人印象深刻，但 DIF 标记的效度验证不充分（外部验证 κ=0.14）、推理 RL 鲁棒性声明样本严重不足（N=13），使核心贡献的可信度受损。\n\n### Strengths\n\n**S1.** 跨学科框架创新性极高。DIF 在群体层面运作，对单模型级别的输出平滑具有理论上的天然鲁棒性。Table 3 得到经验支持（DIF AUROC 0.82-0.91 vs ConStat 0.51-0.75 on RL models）。\n\n**S2.** 分析规模与覆盖面。5,219 模型 × 12,508 题目，11 个实验组件系统覆盖。\n\n**S3.** 架构异质性的诊断与解决。Table 5 全群体 RMSEA=0.105 vs decoder-only RMSEA=0.068，分层后 spurious DIF 减少 24%（Table 6）。\n\n**S4.** 诚实报告负面结果。DVD AUROC 0.56，κ=0.14 外部验证均如实呈现。\n\n**S5.** 退化分析提供实用边界。Table 18 ~35% 替换为临界点，ρ 以 ~0.003/百分点线性退化。\n\n### Weaknesses\n\n**W1 [Major]** DIF 标记效度未得到充分验证。MMLU-CF 验证 κ=0.14, r=0.18 本质上是随机一致水平；GSM8K r=0.36 效应量弱；within-family 46% overlap 意味着 54% 可能由架构差异驱动。\n\n**W2 [Major]** 推理-RL 鲁棒性声明严重欠缺统计效力（N=13）。AUROC 估计的 95% CI 约为 ±0.15-0.20。DeLong p=0.002 是在对齐-RL（N=477）上报告的，不是推理-RL。\n\n**W3 [Major]** 半合成验证存在循环性风险。\"200 clean items\" 如何确认真正 clean？如果包含自然污染，TPR 向上偏倚。\n\n**W4 [Major]** 2PL 模型下 MMLU 的局部独立性假设可能严重违反。57 个学科内部题目高度相关，但核心 DIF 分析使用普通 2PL 未处理局部依赖。\n\n**W5 [Minor]** MH 程序的选择未充分论证（未考虑 non-uniform DIF）。\n**W6 [Minor]** 多重比较校正缺失。\n**W7 [Minor]** 集成 AUROC 0.72 的实用价值需更多讨论（PPV ≈ 0.55）。\n**W8 [Minor]** 再生题目质量退化的影响被低估（因子载荷 -18%，区分度 -19%）。\n\n### Questions for Authors\nQ1. 46% overlap 的方向性解读？\nQ2. κ=0.14 为何不构成否定证据？\nQ3. 推理-RL 的 DeLong p 值具体是多少？\nQ4. 半合成验证中 clean items 的选取标准？\nQ5. Bifactor 模型学科特定因子的方差解释比例？\nQ6. IFT 分割点 2023 年 9 月——如何区分污染 vs 能力跳跃？\n\n### Missing Experiments\n1. 局部依赖诊断（Yen's Q3）\n2. 在 bifactor 模型上做 DIF 分析\n3. Controlled validation（已知污染模型）\n4. PPV/NPV at plausible base rates\n5. Non-uniform DIF 检测（logistic regression DIF）\n6. 推理-RL bootstrap CI\n7. 替换题目质量退化的系统性分析（TIF 对比）\n\n### 维度打分\n| 维度 | 分数 |\n|------|------|\n| Novelty / Originality | 5/6 |\n| Soundness / Correctness | 3/6 |\n| Significance / Impact | 4/6 |\n| Clarity / Presentation | 4/6 |\n| Reproducibility | 3/6 |\n| Overall | 4/6 (Weak Accept) |\n\n---\n\n**请对以上所有 Strengths、Weaknesses、Questions、Missing Experiments 逐条回应 [AGREE] 或 [REBUT]。** 特别关注：\n\n1. **新颖性分歧**：R1 给 Novelty 5/6，你给 2/5。这是最大分歧点。R1 认为\"将 psychometrics 中成熟的 DIF 方法论引入 LLM 污染检测是一个真正的概念贡献\"——你是否仍然坚持 2/5？请详细论证。\n2. **局部独立性问题（W4）**：R1 提出 2PL 在 MMLU 57 学科结构下的局部独立性违反是 Major weakness，你在初审中未提及此问题。你是否同意这是一个重要方法论缺陷？\n3. **半合成验证循环性（W3）**：R1 指出 clean items 选取可能存在循环论证，你如何看？\n4. **PPV 问题（W7）**：R1 估算 PPV ≈ 0.55（约一半标记是假阳性），这是否改变你对方法实用性的评估？"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-20T21:44:19.685658+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1363
}
```

</details>

---


### Assistant

_source line 22 · 2026-05-20T21:44:25.504204+00:00_

交叉分享已派发。两位 Reviewer 各自收到对方的完整审稿原文，需逐条 [AGREE]/[REBUT] 回应。

**聚焦的三大分歧点：**
1. **新颖性评价**：R1 给 5/6 vs R2 给 2/5——这是最核心的分歧，要求双方详细论证
2. **Ensemble 定性**：贡献 vs 负面结果
3. **引用错误的严重程度**：R2 视为 critical，R1 未提及

等待两位 Reviewer 的交叉回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 3

## Round 3

2 recorded events


### User

_source line 23 · 2026-05-20T21:46:50.848942+00:00_

[Reviewer 2 审稿意见]:
## R2 交叉回应：对 R1（Methods & Experiments）审稿意见的逐条回应

---

### 对 R1 Strengths 的回应

**[AGREE] R1-S1**: DIF 在群体层面运作、对单模型级输出平滑具有理论鲁棒性。Table 3 确实支持这一论点（DIF AUROC 0.82-0.91 vs ConStat 在 RL 模型上退化）。我在初审中也认可这一理论论证（我的"主要优势"第1条）。但我补充：这个理论优势的实证确认仍受限于 N=13 的 reasoning-RL 样本量。

**[AGREE] R1-S2**: 分析规模确实令人印象深刻。METABENCH MMLU 上的 5,219 模型 × 12,508 题目是目前最大规模的 IRT-based 污染分析之一。

**[AGREE] R1-S3**: 架构异质性的诊断和解决方案（Table 5/6 的 RMSEA 改善、分层后 spurious DIF 减少 24%）是论文的实质性贡献。我在初审中低估了这一诊断工作的价值。

**[AGREE] R1-S4**: 与我初审的"主要优势"第3条一致。

**[AGREE] R1-S5**: 与我初审的"主要优势"第5条一致。Table 18 的退化分析是一个实用的规划工具。

---

### 对 R1 Weaknesses 的回应

**[AGREE] R1-W1**: 我完全同意 DIF 标记效度不足是核心问题。κ=0.14 实质上是随机一致水平（Section 6.1 或相关验证段落），GSM8K r=0.36 解释变异不到 13%。这与我初审"小问题"中关于 r=0.36 的评论一致，但 R1 正确地将其提升为 Major 级别。46% within-family overlap 的问题我在初审 W4 中也已指出。R1 的表述更精确——"54% 可能由架构差异驱动"直接量化了 false positive 的严重程度。

**[AGREE] R1-W2**: 与我初审 W1 完全一致。N=13 的 reasoning-RL 测试无法支撑核心鲁棒性声明。R1 补充了关键细节：DeLong p=0.002 实际是在 alignment-RL（N=477）上报告的，不是 reasoning-RL。如果论文将 alignment-RL 的统计显著性外推到 reasoning-RL，这是一个严重的统计误导。

**[AGREE] R1-W3**: 这是我初审中遗漏的重要问题。半合成验证的"200 clean items"选取确实存在循环性风险：如果用 DIF 本身（或与 DIF 相关的指标）来筛选 clean items，然后再在这些 items 上评估 DIF 的 TPR，则 TPR 估计向上偏倚。论文需要说明 clean items 的选取是否完全独立于 DIF 指标——例如仅基于发布时间（2024 年后新发布的题目）或内容审核。如果无法证明独立性，整个 semi-synthetic validation 的说服力大打折扣。

**[AGREE] R1-W4**: 我在初审中确实未提及局部独立性问题，这是一个疏忽。R1 的论点成立：MMLU 57 个学科内部题目存在高度内容相关（例如同一学科的多道题共享知识点），这严重违反 2PL 的局部独立性假设。论文在 Section 7.1 的 bifactor 模型中引入了学科特定因子来处理这个问题，但**核心的 DIF 检测分析（Section 3-4）使用的是普通 2PL**。这意味着 DIF 检测阶段的参数估计可能存在系统性偏倚，进而影响 DIF flag 的可靠性。这确实应归为 Major weakness。

补充我的观察：论文实际上已经意识到 IRT fit 不佳的问题（Table 5, full population RMSEA=0.105），并通过架构分层将其改善到 0.068。但 RMSEA 0.068 仍然处于"可接受"边缘（标准阈值 ≤0.06 为"良好"），而且这个改善可能掩盖了局部依赖带来的系统性 misfit。如果在 2PL 阶段就引入 testlet 或 bifactor 结构来处理学科内局部依赖，DIF 检测的精度可能会有实质性变化。

**[AGREE] R1-W5**: MH 程序仅检测 uniform DIF（即 focal/reference 组在所有能力水平上的差异方向一致）。如果污染效应在高能力模型和低能力模型上表现不同（例如高能力模型更容易"记住"答案），则 non-uniform DIF 是合理的，MH 会漏检。Logistic regression DIF 或 Lord's χ² 是直接的替代方案。论文未讨论这一选择的理由。

**[AGREE] R1-W6**: 12,508 个题目同时做 DIF 检测，未提及多重比较校正（Bonferroni、BH FDR 等）。在 α=0.05 下，预期约 625 个假阳性，而论文报告约 1,800 个 ETS-C flags（14.6%）。虽然 ETS classification 基于 effect size 而非 p-value，但 MH 统计量的显著性检验仍需校正。这可能部分解释了 46% within-family overlap——一些 flags 可能是未校正多重比较的假阳性。

**[AGREE] R1-W7**: PPV ≈ 0.55 意味着每标记两个题目就有一个是假阳性。对于 benchmark 维护者来说，如果移除一半"污染"题目实际上是干净的，这会导致不必要的题目损失和 benchmark 缩水。这确实削弱了方法的实用价值，但我认为这是 Minor 而非 Major——因为在 benchmark 维护场景中，flag 后人工审核是合理的工作流程，PPV 0.55 在"初筛+人工确认"的 pipeline 中仍有价值。

**[REBUT] R1-W8**: R1 称再生题目质量退化（因子载荷 -18%，区分度 -19%）"被低估"。但论文在 Table 18 和 Section 7.3 中对此做了系统的 graceful degradation 分析，明确给出了 ~35% 的临界替换比例和 ρ 的线性退化速率。论文的 Section 8 (Limitations) 也承认 "replacement items from the same construct universe" 的假设可能不成立。我认为论文对这一问题的处理是**充分的**——它没有低估退化，而是把退化量化为一个可规划的参数。R1 可能期望看到的是 TIF（Test Information Function）对比，这确实是有价值的补充分析，但缺失 TIF 不等于"低估"退化影响。

---

### 对 R1 Questions 的回应

**[AGREE] R1-Q1**: 46% overlap 的方向性确实需要澄清。是 within-family DIF 是 full-population DIF 的子集（即 full-population flags 包含 within-family flags），还是两者有不同的 flag 集合？这影响对 false positive 来源的判断。

**[AGREE] R1-Q2**: κ=0.14 为何不构成否定证据——这是一个好问题。我的理解是论文可能论证 MMLU-CF 本身的可靠性有限（论文提到 κ=0.14 时似乎暗示 MMLU-CF 作为 ground truth 不可靠），但这是循环论证：如果外部验证标准不可靠，你不能用这一点来豁免你的方法验证失败。

**[AGREE] R1-Q3**: DeLong p 值是在 alignment-RL 还是 reasoning-RL 上计算的，需要明确。如 R1 所述，如果 p=0.002 是 alignment-RL 的结果被误用于支持 reasoning-RL 的声明，这是统计推断错误。

**[AGREE] R1-Q4**: 与 W3 一致，clean items 的选取标准是 semi-synthetic 验证有效性的关键。

**[AGREE] R1-Q5**: Bifactor 模型中学科特定因子的方差解释比例直接关系到 bifactor 结构的必要性和 equating 的有效性。论文提到 general factor 解释 62%（Section 7.1），但未详述 35 个学科因子各自的解释比例。

**[AGREE] R1-Q6**: IFT 的时间分割点（2023 年 9 月，Table 7 附近）如何区分污染效应 vs 自然能力跳跃——这是一个根本性问题。如果 2023 年后的模型整体能力提升（而非因为看到了训练数据），DIF 会将能力提升误判为污染。论文的 RL robustness argument 部分回应了这一点（DIF 理论上对能力变化不敏感，因为它控制了总分），但 Section 4.1 的 within-family analysis 显示 46% overlap 恰恰暗示时间效应和架构效应难以分离。

---

### 对 R1 Missing Experiments 的回应

1. **局部依赖诊断（Yen's Q3）**: [AGREE] 这是支撑 W4 的必要分析。
2. **在 bifactor 模型上做 DIF 分析**: [AGREE] 如果 bifactor 处理了局部依赖，在 bifactor 残差上做 DIF 会更可靠。
3. **Controlled validation（已知污染模型）**: [AGREE] 最有说服力的验证方式。
4. **PPV/NPV at plausible base rates**: [AGREE] 实用性评估的必要指标。
5. **Non-uniform DIF 检测**: [AGREE] 与 W5 一致。
6. **推理-RL bootstrap CI**: [AGREE] 与 W2 一致，这是最紧迫的缺失分析。
7. **替换题目质量退化的 TIF 对比**: [AGREE] 有价值的补充，但如我对 W8 的回应所述，缺失 TIF 不构成 Major 问题。

---

### 关于新颖性分歧的详细论证

**R1 给 Novelty 5/6，我给 2/5（等效约 2.4/6）。差距约 2.5 个等级。**

我承认 R1 的论点有合理性：对 ML 社区的多数研究者来说，DIF 是一个陌生的工具，将其引入 LLM 污染检测确实构成了一个**概念桥梁**贡献。从"这个想法是否会改变社区的思考方式"的角度看，答案可能是肯定的——如果论文被接受，后续工作很可能会沿着"psychometric approach to contamination"这条路继续。

但我维持以下核心论点，因此**不会大幅上调新颖性评分**：

1. **方法层面零创新**：论文使用的 DIF 流程（MH 统计量 → ETS A/B/C 分类 → Δ_MH effect size）是 1988 年以来心理测量学教科书的标准内容。论文未对 DIF 做任何适配 LLM 场景的技术修改——例如未处理 LLM 特有的极端 item-response 模式（全对/全错比例远高于人类测试）、未提出适合 LLM 群体规模（N>5000）的新 effect size 度量、未解决 binary 0/1 response 在 LLM 上的信息损失问题（LLM 的 confidence/logprob 包含比 binary 更丰富的信息）。**一个方法论论文如果完全未修改核心方法，其新颖性是受限的。**

2. **概念桥梁的非显然性有限**：对任何有心理测量学背景的研究者来说，"contamination = DIF" 的映射几乎是显然的——DIF 的定义就是"控制总分后，不同组在同一题上的表现差异"，而污染恰好创造了这种差异。真正的概念贡献不在于"想到用 DIF"，而在于**解决应用中的独特挑战**——但如 R1-W4 和 R1-W1 所示，这些挑战（局部依赖、效度验证）恰恰是论文的短板。

3. **与 Growing Pains 的叠加问题**：Growing Pains (Zhang et al., 2026) 已经建立了 "IRT for LLM evaluation" 的范式。在这个前提下，从 IRT 扩展到 DIF 是一个自然的推论步骤，进一步降低了概念桥梁的非显然性。

**我的调整后评分**：考虑到 R1 关于"对 ML 社区的实际影响"的论点，我将 Novelty 从 2/5 上调至 **2.5/5（约 3/6）**，但不会更高。理由：概念贡献有实际价值，但方法层面的零创新和有限的非显然性限制了新颖性的上限。如果论文做了任何 DIF-for-LLM 的技术适配（例如利用 logprob 信息的连续 DIF、处理 LLM 极端 response 的 robust MH），我会愿意给 4/6。

---

### 对 R1 维度打分的回应

| R1 维度 | R1 分数 | R2 分数 | 一致/分歧 |
|---------|---------|---------|-----------|
| Novelty | 5/6 | 3/6（上调后） | **主要分歧**，理由见上 |
| Soundness | 3/6 | 3/5→约3.6/6 | **基本一致** |
| Significance | 4/6 | 3/5→约3.6/6 | 基本一致 |
| Clarity | 4/6 | 3/5→约3.6/6 | 基本一致，但我的引用错误发现（N1）是 R1 未提及的 |
| Reproducibility | 3/6 | 2/5→约2.4/6 | 基本一致 |
| **Overall** | **4/6** | **3/6** | **分歧**：主要由 novelty 分差和引用错误驱动 |

**R1 未提及的问题（我独有的发现）**：
- **引用错误**（我的 N1）："Tets & Berger (2016) Iron-Fenced Trees" 应为 "Tutz & Berger (2016) Item-Focussed Trees"；"Dunn et al. (2024) DVD" 应为 "Liang et al. (2026)"。这些错误在 R1 的审稿中完全未被提及，但对论文的学术可信度构成严重损害。我维持这是 Must-Fix 级别问题。

---

### 综合后的总体判断

经过与 R1 交叉审查，我对论文的总体评价略有上调但核心判断不变：

**调整前**: 3/6 (Borderline Reject)
**调整后**: 3/6 (Borderline Reject)，但更接近 3.5

**理由**：R1 的 W3（semi-synthetic 循环性）和 W4（局部独立性）补充了我初审中遗漏的两个重要方法论问题，这些问题实际上**强化了我对 Soundness 的担忧**。虽然我在 Novelty 上做了小幅上调（2→2.5/5），但新增的方法论问题抵消了这一上调。加上我独有的引用错误发现（R1 未提及），总体评分维持 3/6。

核心瓶颈：(1) 引用错误需修复；(2) 2PL 局部依赖问题需实质性回应（至少提供 Yen's Q3 诊断）；(3) N=13 的 RL 鲁棒性需补充 bootstrap CI 或扩大样本；(4) semi-synthetic clean items 的独立性需证明。如果 rebuttal 能回应这四点，有可能上调至 4/6。

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

_source line 24 · 2026-05-20T21:46:57.893984+00:00_

交叉回应收到 R2 的结果。R2 对 R1 的 8 个 weakness 中 7 个标注 [AGREE]，仅对 W8（退化影响被低估）标注 [REBUT]。新颖性分歧从 2/5 微调至 2.5/5，但核心立场不变。等待 R1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 4

## Round 4

2 recorded events


### User

_source line 25 · 2026-05-20T21:47:00.421582+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：与 R1 在 14/17 个子项上达成一致，最大分歧在 Novelty（R1: 5/6 vs R2: 3/6 调整后）。我将 Novelty 从 2/5 小幅上调至 2.5/5，承认概念桥梁对 ML 社区的价值，但坚持方法层面零创新限制了上限。R1 补充的 W3（semi-synthetic 循环性）和 W4（局部独立性）强化了 Soundness 担忧。唯一 REBUT 的是 W8——论文对再生质量退化的处理是充分的。总体评分维持 3/6 (Borderline Reject)。

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

_source line 26 · 2026-05-20T21:47:11.493697+00:00_

R2 交叉回应已收到。等待 R1 对 R2 审稿意见的交叉回应。

**当前进度：**
- R1 初审 ✅ → 交叉回应 ⏳（待返回）
- R2 初审 ✅ → 交叉回应 ✅

**R2 交叉回应要点：**
- 14/17 子项 AGREE，仅 REBUT R1-W8（再生退化处理充分）
- Novelty 小幅上调 2→2.5/5，但坚持方法层面零创新
- 采纳 R1 的 W3（半合成循环性）和 W4（局部独立性）为新增 Major concern
- 总体维持 3/6

R1 返回后即进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 5

## Round 5

14 recorded events


### User

_source line 27 · 2026-05-20T21:47:42.398543+00:00_

[Reviewer 1 审稿意见]:
## R1 对 R2 审稿意见的交叉回应

---

### Must-Fix 逐条回应

**[REBUT] R2-N1: 引用错误——R2 的指控本身部分不准确**

R2 声称论文使用了 "Iron-Fenced Trees" 和 "Tets & Berger (2016)"。我以 165 DPI 重新渲染了 page 2 和 page 6 进行核实：

- **方法名：** 论文 §4.4 节标题和正文均写作 **"Item-Focused Trees (IFT)"**（page 6），Related Work（page 2）也写作 "Item-Focused Trees"。R2 声称的 "Iron-Fenced Trees" **在论文中不存在**——这是 R2 自己的误读或记忆偏差。真实文献为 "Item-Focussed Trees"（英式拼写），论文的 "Item-Focused Trees"（美式拼写）只是拼写变体，不算错误。
- **作者名：** page 2 的引用拼写看起来可能是 "Totz" 而非 "Tutz"——如果确实如此，这是一个 typo 级别的错误，需要更正但不构成 "严重错误"。
- **DVD 引用（"Dunn et al."）：** 在我审阅的渲染中无法清晰辨认具体作者名，无法确认或否定此项。如果 R2 可以指出具体页面和行号，将更有助于作者核查。

**结论：** R2 将此标记为 [critical] 过于严厉。其核心指控——"Iron-Fenced Trees"——本身是错误的。可能存在的 author name typo 需要修正但不影响技术贡献的可信度。建议作者全面核查参考文献拼写，但这属于 camera-ready 级别的修正，不应作为拒稿依据。

---

**[REBUT] R2-N2: DIF 迁移的新颖性不足——R2 低估了跨学科桥接的难度和完整管线的贡献**

R2 认为将 temporal cohorts 映射为 reference/focal groups 是 "straightforward"。我不同意这个判断，理由如下：

1. **概念识别并非平凡。** LLM 社区长期将污染检测视为信息检索问题（n-gram overlap、perplexity、MIA），而非心理测量问题。识别出 "contamination = DIF" 这个等式需要对两个领域都有深入理解——这不是套公式。
2. **工程和实证挑战非平凡。** 对 5,219 × 12,508 矩阵拟合 IRT 本身就有独特挑战——论文发现的架构异质性问题（full-pop RMSEA=0.105 → decoder-only 0.068, Table 5）和分层解决方案是非预期的实证贡献。
3. **RL 鲁棒性洞见是新的。** "DIF 在群体层面运作，因此天然对单模型输出平滑具有鲁棒性" 这个理论论点（§3.2）有独立价值——它解释了为什么 per-model 检测器（ConStat、Min-K%）在 RL 模型上退化而 DIF 不退化（Table 3）。
4. **完整管线超越了单一方法应用。** 检测 → 多信号集成 → 半合成验证 → bifactor 等值 → 再生 → 退化分析——这是一个完整的技术栈，不是简单的 "apply DIF to new data"。

**但我承认 R2 有部分道理：** DIF 方法本身没有技术创新（仍是标准 Mantel-Haenszel + ETS 分类）。如果论文标题或 framing 暗示了 DIF 方法论贡献，那确实有 overclaiming。

**修正后的评分：** 我将 Novelty 从 5/6 下调至 **4/6**。理由：跨学科概念贡献 + 大规模实证发现 + 完整管线 ≥ 4 分门槛，但缺乏 DIF 方法本身的技术创新使其无法达到 5 分。R2 的 2/5 仍然过低——忽略了实证发现和管线贡献的价值。

---

**[REBUT] R2-N3: "Ensemble 不如单独 DIF"——R2 选择性引用数据，结论不成立**

R2 声称 "Table 10 显示 DIF 单独的 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升。" **这是对 Table 10 的选择性解读。**

Table 10（page 7）完整数据：

| Strategy | TPR (δ≥1.4) | TPR (δ≥0.8) | FPR | Coverage |
|----------|-------------|-------------|-----|----------|
| DIF only | 0.78 | 0.51 | 0.04 | 36% |
| Full ensemble (union) | 0.82 | 0.72 | 0.085 | 73% |

关键对比：
- **δ≥1.4（大效应）：** ensemble **更好** (0.82 > 0.78)
- **δ≥0.8（中等效应）：** ensemble **大幅改善** (0.72 vs 0.51, +0.21 TPR)
- **Coverage：** ensemble **翻倍** (73% vs 36%)

R2 只看了 δ≥1.4 一个维度且忽视了 ensemble 在该维度也更优。Ensemble 的核心价值恰恰在中等效应区间——DIF 单独在 δ<1.0 时 power 急剧下降（Table 4, page 5），而 ensemble 通过 ConStat 信号补充了这一盲区。

FPR 从 0.04 升至 0.085 是合理代价——在 12,508 题上多标记约 560 题（约 4.5%），换取中等效应 TPR 提升 21 个百分点和覆盖率翻倍。

**结论：** Ensemble 是明确的正面贡献。R2 的 N3 结论 factually incorrect。

---

### Should-Fix 逐条回应

**[AGREE] R2-W1: RL 样本量过小**
完全同意。我在 R1 审稿中将此列为 W2 [Major]，核心论点一致：N=13 无法支撑核心贡献声明。我补充一点：R2 和我都指出了这个问题，这应该给作者明确信号——此问题不可回避。

**[AGREE] R2-W2: 与 Growing Pains 的区分不清晰**
这是合理的 related work 关切。Growing Pains（Zhang et al.）也提出了 IRT-based benchmark 评估框架。论文应在 §2 中明确说明：Growing Pains 聚焦 score equivalence 和 benchmark reliability，而本文聚焦 item-level contamination detection via DIF + 再生管线——两者在 IRT 应用层面有重叠但目标和技术路径不同。

**[AGREE] R2-W3: Wang et al. (2026) 无法核实**
无法核实的引用在 blind review 中确实是红旗。我在 R1 审稿中未专门检查引用真实性（这更属于 R2 的侧重领域），但同意此关切。建议 Director 在最终审稿前用 `verify_references` 工具做系统性引用核查。

**[AGREE] R2-W4: 42% within-family overlap**
完全同意。我在 R1 审稿中将此列为 W1 [Major] 的一部分——46% overlap 意味着 54% 的全群体 DIF 标记可能由能力漂移而非污染驱动。

**[REBUT] R2-W5: 贡献数量膨胀（5→2-3 条）**
部分不同意。R2 建议缩减至 2-3 条，但我认为以下 4 条可以独立成立：
1. **IRT 拟合诊断 + 架构分层**——这是一个有独立价值的实证发现（Table 5-6）
2. **DIF 检测 + ensemble**——核心检测方法（Tables 3, 10）
3. **半合成验证 + power surface**——验证框架（Tables 12-14）
4. **Bifactor 等值 + 再生管线**——remediation 方向（Tables 15-18）

Power surface (R²=0.89) 更适合归入贡献 3 而非单独列出——在这一点上我同意 R2，5 条确实可以压缩为 4 条。

---

### 缺失相关工作逐条回应

**[AGREE] 1. Min-K%++ (Shi et al., 2024):** 论文提到了 Min-K%（Table 3 有对比），但更强的变体 Min-K%++ 应该被讨论。

**[AGREE] 2. IRT in NLP (Lalor et al., 2019; Vania et al., 2021):** 这是最重要的遗漏。这些工作是 IRT 应用于 NLP 评测的先驱，论文声称 "first large-scale IRT fit diagnostics for LLM populations"——必须明确与这些先行工作的区别（规模？群体定义？拟合诊断方法？）。

**[REBUT] 3. 动态 Benchmark (Dynabench, ChatBot Arena, HELM):** 这些工作解决的是不同问题——动态评测的目标是 adversarial/adaptive item creation，而非基于 IRT 的污染检测和等值再生。论文的 §2 Related Work 在 "Benchmark Maintenance" 部分已提及 LiveBench（类似方向）。要求论文讨论所有动态基准方案会偏离论文的核心聚焦。

**[AGREE] 4. N-gram/perplexity 基线方法:** 论文在 §1 提到 "n-gram overlap" 但未在实验中将 n-gram 方法作为基线对比。至少应在 Table 3 中加入一个简单的 n-gram overlap 基线。

**[AGREE] 5. Balloccu et al. (2024) survey:** 作为该领域最近的综述，应该被引用以定位论文在 contamination detection 文献中的位置。

---

### 主要优势回应

**[AGREE] 所有 5 条优势。** R2 对论文优势的评价公允——问题重要性、诚实报告、负面结果的社区价值、power surface 的实用性、regeneration 方向。

---

### Director 要求的三个重点问题

**1. 新颖性评分分歧（R2=2/5 vs R1 原始=5/6）**

修正后我给 **4/6**。核心分歧在于 "应用 vs 创新" 的判断标准：
- R2 立场：DIF 是现有技术，应用到新领域 = 低新颖性。
- R1 立场：跨学科概念桥接 + 大规模实证 + 完整管线 = 中高新颖性。
- 调和点：如果论文重新 framing 为 "实证发现驱动的系统论文"（empirical systems paper）而非 "方法论创新论文"，两个评分可以趋近。论文当前的 framing 确实偏向方法论贡献声明，这在 DIF 本身无创新的情况下略显 overclaiming。
- **最终判断：** novelty 在 3-4/6 范围内是合理的。R2 的 2/5 和我原始的 5/6 都偏离了公允区间。

**2. 引用错误对论文可信度的影响**

我在 R1 初审中未专门检查引用——这确实是疏漏。但经核实：
- R2 声称的最严重错误（"Iron-Fenced Trees"）**在论文中不存在**——论文写的是 "Item-Focused Trees"。这反而削弱了 R2 将此标记为 [critical] 的依据。
- 可能存在的 author name typo（Totz/Tets → Tutz）确实需要修正，但属于 minor 级别。
- DVD 引用和 Wang et al. 需要用 `verify_references` 系统核查后才能定论。

**影响评估：** 如果确认存在 1-2 个 author name typo，这属于 carelessness 但不影响技术可信度。如果存在虚假引用（fabricated citation），则严重性显著提升至 [critical]。当前证据不足以判断。

**3. Ensemble 到底是正面贡献还是负面结果？**

**明确是正面贡献。** Table 10 的数据清晰显示 ensemble 在所有关键维度（δ≥1.4 TPR、δ≥0.8 TPR、coverage）均优于 DIF alone。R2 的 N3 结论基于选择性数据引用，factually incorrect。

但有一个 nuance：DVD 单独的负面结果（AUROC 0.56）和 DVD 加入后 ensemble 改善有限（Weighted fusion 中 DVD 权重很低）说明 DVD 信号贡献微弱。论文可以更诚实地表述：**有效的 ensemble 实际上是 DIF + ConStat 双信号系统，DVD 贡献可忽略。**

---

### 总结：R1 修正后的综合评分

在看过 R2 审稿并进行交叉核查后，我对部分评分做出调整：

| 维度 | R1 原始 | R1 修正 | 修正理由 |
|------|---------|---------|---------|
| Novelty | 5/6 | 4/6 | R2 关于 DIF 本身无技术创新的观点部分成立 |
| Soundness | 3/6 | 3/6 | 不变——核心效度问题仍未解决 |
| Significance | 4/6 | 4/6 | 不变 |
| Clarity | 4/6 | 4/6 | 不变 |
| Reproducibility | 3/6 | 3/6 | 不变 |
| **Overall** | **4/6** | **4/6** | **Weak Accept 维持** |

R2 给 3/6 (Borderline Reject)，我修正后维持 4/6 (Weak Accept)。核心分歧：R2 更重视方法论新颖性，我更重视实证贡献和问题重要性。对于 top venue，我认为一篇概念新颖、实验全面、诚实报告局限性的系统论文值得 conditional accept——前提是作者在 rebuttal 中回应效度验证（κ=0.14 的解释）和 RL 样本量问题。

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

_source line 28 · 2026-05-20T21:48:11.963916+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
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
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-20T21:48:12.067907+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-20T21:48:15.438273+00:00_

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

_source line 31 · 2026-05-20T21:48:15.540880+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-20T21:48:20.363828+00:00_

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

_source line 33 · 2026-05-20T21:48:20.916318+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_director_870d8ac6.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-20T21:48:20.916783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_1.md"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_1.md"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-20T21:48:20.967261+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_director_870d8ac6.

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

_source line 36 · 2026-05-20T21:49:30.308667+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "\n# Review Issues Tracker — irt_equated_bench_regen\n# Round 1 | 2026-05-20\n\n- id: \"R1-W1\"\n  summary: \"DIF 标记效度验证不充分——MMLU-CF κ=0.14（随机水平），GSM8K r=0.36（弱），within-family 46% overlap 表明过半标记可能由架构差异驱动\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均认为这是核心问题。R2 在交叉回应中完全同意 R1 的表述。\"\n  action_items:\n    - round: 1\n      action: \"提供 controlled validation（已知污染模型的 clean vs fine-tuned-on-MMLU）；解释 κ=0.14 为何不构成否定证据；报告 stratified precision/recall\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"推理-RL 鲁棒性声明仅 N=13 模型支持，统计效力严重不足；DeLong p=0.002 是 alignment-RL (N=477) 而非 reasoning-RL 的结果\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"共识问题。R2 补充：13 个模型可能全来自有限 family，存在选择偏差。\"\n  action_items:\n    - round: 1\n      action: \"报告 N=13 下的 bootstrap CI；列出 13 个模型名称和 family 分布；考虑将 RL 鲁棒性降级为辅助发现\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"半合成验证的 200 clean items 选取可能存在循环论证——若用 DIF 相关指标筛选 clean items 再评估 DIF，TPR 向上偏倚\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 在交叉回应中 AGREE 并补充论证。\"\n  action_items:\n    - round: 1\n      action: \"说明 clean items 选取标准是否独立于 DIF 指标；提供不同 base contamination rates 下的 sensitivity analysis\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"2PL 模型在 MMLU 57 学科结构下局部独立性假设可能严重违反——核心 DIF 分析（§3-4）使用普通 2PL 未处理局部依赖，可能膨胀 MH 统计量导致 DIF 假阳性率升高\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 在交叉回应中 AGREE 并补充：RMSEA 0.068 仍处于可接受边缘，可能掩盖局部依赖的系统性 misfit。\"\n  action_items:\n    - round: 1\n      action: \"提供 Yen's Q3 或 Chen-Thissen LD 诊断；在 bifactor 模型上重做 DIF 分析并对比 2PL 结果\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"引用错误——作者名和/或方法名可能存在错误（Tutz 拼写问题、DVD 引用作者/年份不符）；R1 反驳称 'Iron-Fenced Trees' 在论文中不存在，论文写的是 'Item-Focused Trees'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 标记为 critical，R1 REBUT 称核心指控（Iron-Fenced Trees）有误。存在事实争议，需作者和系统核查。\"\n  action_items:\n    - round: 1\n      action: \"全面核查所有引用的作者名、标题、年份和出版信息；确认 Tutz/Tets 拼写；确认 DVD 引用来源\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"DIF 迁移新颖性有限——方法本身无技术创新（标准 MH + ETS 分类），未适配 LLM 特有建模挑战\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 标记为 critical，R1 部分同意（Novelty 从 5/6 下调至 4/6）但认为跨学科概念桥接+完整管线有独立价值。分歧缩窄至 R1=4/6 vs R2=3/6。\"\n  action_items:\n    - round: 1\n      action: \"重新 framing 贡献——强调实证发现和系统管线而非方法论创新；阐述 LLM 群体相对人类的独特建模挑战及对应适配\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"与 Growing Pains (Zhang et al., 2026) 的区分不够清晰——两者在 IRT 建模层面高度相似\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n  action_items:\n    - round: 1\n      action: \"在 Related Work 中增加与 Growing Pains 的详细对比段落\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Wang et al. (2026) 引用无法核实——核心 motivation 的文献支撑可能不存在\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n  action_items:\n    - round: 1\n      action: \"提供完整引用信息（arXiv ID 或 DOI）；如无法核实则替换或移除\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Mantel-Haenszel 仅检测 uniform DIF，未考虑 non-uniform DIF（交叉 ICC）；选择未充分论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出 Minor，R2 AGREE。\"\n  action_items:\n    - round: 1\n      action: \"用 logistic regression DIF 做对比实验\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"12,508 个题目同时做 MH 检验，未提及多重比较校正（FDR/Bonferroni）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出 Minor，R2 AGREE 并补充：α=0.05 下预期约 625 个假阳性，可能部分解释 46% overlap。\"\n  action_items:\n    - round: 1\n      action: \"讨论 FDR 控制策略；报告校正后的 flag 数量变化\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W7\"\n  summary: \"集成 AUROC 0.72 的 PPV ≈ 0.55（约半数标记为假阳性），实用价值需讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出 Minor，R2 同意但认为在'初筛+人工确认'场景中仍有价值。\"\n  action_items:\n    - round: 1\n      action: \"加入 PPV 曲线或 base-rate 敏感的 precision-recall 分析\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失关键相关工作：IRT in NLP (Lalor et al. 2019, Vania et al. 2021)、Min-K%++ (Shi et al. 2024)、Balloccu et al. 2024 survey\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE（除 Dynabench/ChatBot Arena 外）。\"\n  action_items:\n    - round: 1\n      action: \"在 Related Work 中补充 Lalor et al. 2019、Vania et al. 2021、Min-K%++、Balloccu et al. 2024\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
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
    "issues_yaml": "\n# Review Issues Tracker — irt_equated_bench_regen\n# Round 1 | 2026-05-20\n\n- id: \"R1-W1\"\n  summary: \"DIF 标记效度验证不充分——MMLU-CF κ=0.14（随机水平），GSM8K r=0.36（弱），within-family 46% overlap 表明过半标记可能由架构差异驱动\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均认为这是核心问题。R2 在交叉回应中完全同意 R1 的表述。\"\n  action_items:\n    - round: 1\n      action: \"提供 controlled validation（已知污染模型的 clean vs fine-tuned-on-MMLU）；解释 κ=0.14 为何不构成否定证据；报告 stratified precision/recall\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"推理-RL 鲁棒性声明仅 N=13 模型支持，统计效力严重不足；DeLong p=0.002 是 alignment-RL (N=477) 而非 reasoning-RL 的结果\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"共识问题。R2 补充：13 个模型可能全来自有限 family，存在选择偏差。\"\n  action_items:\n    - round: 1\n      action: \"报告 N=13 下的 bootstrap CI；列出 13 个模型名称和 family 分布；考虑将 RL 鲁棒性降级为辅助发现\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"半合成验证的 200 clean items 选取可能存在循环论证——若用 DIF 相关指标筛选 clean items 再评估 DIF，TPR 向上偏倚\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 在交叉回应中 AGREE 并补充论证。\"\n  action_items:\n    - round: 1\n      action: \"说明 clean items 选取标准是否独立于 DIF 指标；提供不同 base contamination rates 下的 sensitivity analysis\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"2PL 模型在 MMLU 57 学科结构下局部独立性假设可能严重违反——核心 DIF 分析（§3-4）使用普通 2PL 未处理局部依赖，可能膨胀 MH 统计量导致 DIF 假阳性率升高\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 在交叉回应中 AGREE 并补充：RMSEA 0.068 仍处于可接受边缘，可能掩盖局部依赖的系统性 misfit。\"\n  action_items:\n    - round: 1\n      action: \"提供 Yen's Q3 或 Chen-Thissen LD 诊断；在 bifactor 模型上重做 DIF 分析并对比 2PL 结果\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"引用错误——作者名和/或方法名可能存在错误（Tutz 拼写问题、DVD 引用作者/年份不符）；R1 反驳称 'Iron-Fenced Trees' 在论文中不存在，论文写的是 'Item-Focused Trees'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"R2 标记为 critical，R1 REBUT 称核心指控（Iron-Fenced Trees）有误。存在事实争议，需作者和系统核查。\"\n  action_items:\n    - round: 1\n      action: \"全面核查所有引用的作者名、标题、年份和出版信息；确认 Tutz/Tets 拼写；确认 DVD 引用来源\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"DIF 迁移新颖性有限——方法本身无技术创新（标准 MH + ETS 分类），未适配 LLM 特有建模挑战\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 标记为 critical，R1 部分同意（Novelty 从 5/6 下调至 4/6）但认为跨学科概念桥接+完整管线有独立价值。分歧缩窄至 R1=4/6 vs R2=3/6。\"\n  action_items:\n    - round: 1\n      action: \"重新 framing 贡献——强调实证发现和系统管线而非方法论创新；阐述 LLM 群体相对人类的独特建模挑战及对应适配\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"与 Growing Pains (Zhang et al., 2026) 的区分不够清晰——两者在 IRT 建模层面高度相似\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n  action_items:\n    - round: 1\n      action: \"在 Related Work 中增加与 Growing Pains 的详细对比段落\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"Wang et al. (2026) 引用无法核实——核心 motivation 的文献支撑可能不存在\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n  action_items:\n    - round: 1\n      action: \"提供完整引用信息（arXiv ID 或 DOI）；如无法核实则替换或移除\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W5\"\n  summary: \"Mantel-Haenszel 仅检测 uniform DIF，未考虑 non-uniform DIF（交叉 ICC）；选择未充分论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出 Minor，R2 AGREE。\"\n  action_items:\n    - round: 1\n      action: \"用 logistic regression DIF 做对比实验\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"12,508 个题目同时做 MH 检验，未提及多重比较校正（FDR/Bonferroni）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出 Minor，R2 AGREE 并补充：α=0.05 下预期约 625 个假阳性，可能部分解释 46% overlap。\"\n  action_items:\n    - round: 1\n      action: \"讨论 FDR 控制策略；报告校正后的 flag 数量变化\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W7\"\n  summary: \"集成 AUROC 0.72 的 PPV ≈ 0.55（约半数标记为假阳性），实用价值需讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1 提出 Minor，R2 同意但认为在'初筛+人工确认'场景中仍有价值。\"\n  action_items:\n    - round: 1\n      action: \"加入 PPV 曲线或 base-rate 敏感的 precision-recall 分析\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失关键相关工作：IRT in NLP (Lalor et al. 2019, Vania et al. 2021)、Min-K%++ (Shi et al. 2024)、Balloccu et al. 2024 survey\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE（除 Dynabench/ChatBot Arena 外）。\"\n  action_items:\n    - round: 1\n      action: \"在 Related Work 中补充 Lalor et al. 2019、Vania et al. 2021、Min-K%++、Balloccu et al. 2024\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-20T21:49:30.359470+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 6185}, \"error\": \"\"}"}

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

_source line 38 · 2026-05-20T21:51:43.222547+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# 圆桌审稿报告 — Round 1\n\n**论文**: \"Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration\"\n\n**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）\n**日期**: 2026-05-20\n**轮次**: Round 1（初审 + 交叉回应，1 轮收敛）\n\n---\n\n## Summary\n\n本文将 LLM 基准测试污染检测重新定义为心理测量学问题，利用差异项目功能（DIF）在 5,219 模型 × 12,508 MMLU 题目的大规模矩阵上检测污染项目。论文构建了 DIF+ConStat 集成检测器（AUROC 0.72），提出半合成验证框架，并通过 bifactor IRT 等值进行基准再生（holdout ρ=0.91）。实验覆盖 11 个组件，从 IRT 拟合诊断到退化分析，构成完整技术栈。\n\n---\n\n## Strengths\n\n**S1. 跨学科概念贡献** [共识]\n将心理测量学中成熟的 DIF 方法论引入 LLM 污染检测，是一个有实际价值的概念桥梁。DIF 在群体层面运作，对单模型输出平滑具有理论上的天然鲁棒性（§3.2, Table 3: DIF AUROC 0.82-0.91 vs ConStat 0.51-0.75 on RL models）。两位 Reviewer 均认可此论点。\n\n**S2. 分析规模与覆盖面** [共识]\n5,219 模型 × 12,508 题目是目前已知最大的 IRT-for-LLM 分析之一。11 个实验组件系统覆盖从检测到再生的完整技术栈。\n\n**S3. 架构异质性诊断** [共识]\nTable 5 展示 full-population RMSEA=0.105 vs decoder-only 0.068，分层后 spurious DIF 减少 24%（Table 6）。R2 在交叉回应中承认初审低估了这一诊断工作的价值。\n\n**S4. 诚实报告负面结果** [共识]\nDVD AUROC 0.56、κ=0.14 外部验证、within-family 46% overlap 均如实呈现。在同类工作中属于高标准的透明度。\n\n**S5. 退化分析** [共识]\nTable 18 给出明确操作阈值（~35% 替换为临界点），ρ 以 ~0.003/百分点线性退化，为实际部署提供可规划的安全边界。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**WC1. DIF 标记效度验证严重不足** [共识: R1+R2]\n- MMLU-CF 验证 κ=0.14 本质上是随机一致水平，几乎没有验证价值\n- GSM8K 交叉验证 r=0.36（Table 11）解释变异不到 13%，仅为暗示性佐证\n- Within-family 46% overlap 意味着过半 DIF 标记可能由架构差异或能力增长驱动，而非真正的污染\n- 论文未提供正式的 precision 估计；PPV ≈ 0.55 意味着约半数标记为假阳性\n- **底线**：如果无法区分\"真污染\"和\"能力进步\"，整个检测管线的可信度是未知的\n\n**WC2. 推理-RL 鲁棒性声明严重欠缺统计效力** [共识: R1+R2]\n- 推理-RL 分析仅基于 13 个模型，AUROC 估计 95% CI 约为 ±0.15-0.20\n- DeLong p=0.002 是在 alignment-RL（N=477）上报告的，**不是**推理-RL（N=13），存在统计推断误导\n- 推理-RL 恰恰是论文声称最重要的前沿场景，但证据最薄弱\n- 13 个模型的 family 分布未披露，可能存在选择偏差\n\n**WC3. 半合成验证存在循环性风险** [共识: R1+R2]\n- \"200 clean items\" 的选取标准不明——如果用 DIF 相关指标筛选 clean items 再评估 DIF，则 TPR 估计向上偏倚\n- Semi-synthetic TPR \"consistently exceeds pure simulation by 3-8bps\" 可能恰好反映了 existing contamination 的叠加效应\n- 无法证明选取独立性时，整个 semi-synthetic validation 的说服力大打折扣\n\n**WC4. 2PL 局部独立性假设可能严重违反** [共识: R1+R2]\n- MMLU 57 个学科内部题目高度相关，严重违反 2PL 局部独立性假设\n- 核心 DIF 分析（§3-4）使用普通 2PL，未检测或处理局部依赖\n- 违反局部独立性会膨胀 MH 统计量，导致 DIF 假阳性率升高——与 WC1 叠加\n- 论文在 §7.1 的 bifactor 模型中处理了这个问题，但未在核心检测阶段应用\n- RMSEA 0.068（decoder-only 分层后）仍处于\"可接受\"边缘（标准 ≤0.06 为\"良好\"）\n\n### Warning（影响评分但不一票否决）\n\n**WW1. 引用准确性存疑** [分歧: R2=critical, R1=minor]\n- R2 指出 \"Iron-Fenced Trees (Tets & Berger, 2016)\" 应为 \"Item-Focussed Trees (Tutz & Berger, 2016)\"，以及 DVD 引用的作者/年份不符\n- R1 反驳称论文写的是 \"Item-Focused Trees\"（美式拼写变体），\"Iron-Fenced Trees\" 在论文中不存在；可能存在的是 author name typo（Totz/Tets → Tutz）\n- **Director 判断**：存在事实争议，需作者逐一核查所有引用。如仅为拼写 typo 则属 camera-ready 级修正；如存在虚构引用则严重性显著提升。Wang et al. (2026) 引用同样无法独立核实（R1、R2 均同意此关切）。\n\n**WW2. 新颖性定位偏差** [分歧缩窄: R1=4/6, R2=3/6]\n- DIF 是 1988 年的经典技术，论文未对其做任何适配 LLM 场景的技术修改\n- 对有心理测量学背景者，\"contamination = DIF\" 的映射近乎显然\n- Growing Pains (Zhang et al., 2026) 已建立 \"IRT for LLM evaluation\" 范式，进一步降低概念桥梁的非显然性\n- **但**：对 ML 社区多数研究者而言 DIF 是陌生工具，完整管线（检测→集成→验证→等值→再生→退化分析）超越了单一方法应用\n- **Director 判断**：论文当前 framing 偏向方法论贡献声明，在 DIF 本身无创新的情况下略显 overclaiming。建议重新定位为\"实证发现驱动的系统论文\"\n\n**WW3. 与 Growing Pains 区分不足** [共识: R1+R2]\n- 两者在 IRT 建模层面高度相似，论文仅一句话带过\n\n**WW4. 多处不可核实引用** [共识: R1+R2]\n- Wang et al. (2026) 无法通过搜索找到完全匹配的论文\n- DVD \"Dunn et al. (2024)\" 的作者/年份可能不符\n\n**WW5. MH 程序选择未论证** [共识: R1+R2]\n- 仅检测 uniform DIF，对 non-uniform DIF 不敏感\n- 未与 logistic regression DIF、SIBTEST 等替代方案对比\n\n**WW6. 多重比较校正缺失** [共识: R1+R2]\n- 12,508 个 MH 检验未提及 FDR 控制\n- α=0.05 下预期约 625 个假阳性，可能部分解释 46% within-family overlap\n\n**WW7. ETS A/B/C 阈值未校准** [R2 提出]\n- 直接沿用人类测试标准，未讨论对 LLM 群体的适用性\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **DIF 效度验证是核心瓶颈**（κ=0.14 + 46% overlap）——论文最需要回应的问题\n2. **N=13 推理-RL 无法支撑核心贡献声明**——需 bootstrap CI 或扩大样本\n3. **半合成验证的 clean items 选取需证明独立性**\n4. **2PL 局部独立性需诊断**（Yen's Q3 或在 bifactor 上重做 DIF）\n5. **缺失关键相关工作**：Lalor et al. (2019)、Vania et al. (2021)、Min-K%++ (Shi et al., 2024)、Balloccu et al. (2024)\n6. **Wang et al. (2026) 引用需提供可核实信息**\n7. **退化分析的实用价值**——Table 18 的 ~35% 临界点是有操作价值的发现\n8. **诚实报告负面结果**值得肯定\n\n---\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，双方已充分论证：\n\n### 1. 引用错误严重性\n- **R2**：至少 2 处引用严重错误（Iron-Fenced Trees、Tets），呈典型 LLM 幻觉特征，[critical] 级别\n- **R1**：论文写的是 \"Item-Focused Trees\" 而非 \"Iron-Fenced Trees\"，R2 的核心指控本身有误；可能存在的 author name typo 属 camera-ready 级修正\n- **Director 裁定**：降级为 warning。R2 的 \"Iron-Fenced Trees\" 指控存在事实争议，但引用准确性仍需全面核查。如核查后确认存在虚构引用则重新升级。\n\n### 2. 新颖性评分\n- **R1**：4/6——跨学科概念桥接 + 大规模实证 + 完整管线\n- **R2**：3/6——方法层面零创新，概念映射对有背景者近乎显然\n- **Director 裁定**：3.5/6。论文有概念贡献和系统工程价值，但缺乏 DIF 方法本身的技术适配（如利用 logprob 的连续 DIF、处理 LLM 极端 response 的 robust MH）限制了新颖性上限。\n\n### 3. Ensemble 是正面贡献还是负面结果\n- **R2**：Table 10 显示 DIF 单独 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升\n- **R1**：反驳——Table 10 完整数据显示 ensemble 在所有维度更优（δ≥1.4: 0.82>0.78; δ≥0.8: 0.72 vs 0.51; coverage: 73% vs 36%）；R2 选择性引用了单一维度\n- **Director 裁定**：R1 的数据引用更完整，ensemble 在中等效应区间（δ≥0.8）确有实质性改善。但 DVD 信号贡献微弱，有效 ensemble 实际上是 DIF+ConStat 双信号系统。建议论文更精确地表述 ensemble 的组成和边际贡献。\n\n### 4. 再生题目质量退化\n- **R1**：因子载荷 -18%、区分度 -19% 被低估，需 TIF 对比\n- **R2**：反驳——论文在 Table 18 和 §7.3 中已系统量化退化，处理充分；缺 TIF 是有价值的补充但非 Major\n- **Director 裁定**：同意 R2，退化处理基本充分，TIF 对比为可选补充。\n\n---\n\n## Questions for Authors\n\n1. **[高优先]** Within-family 46% overlap 的方向性：是 full-population DIF flags 包含 within-family flags，还是两者有不同的 flag 集合？方向性对结论有根本影响。\n2. **[高优先]** κ=0.14（与 MMLU-CF 一致性）为何不构成对 DIF 方法的否定证据？如果认为 MMLU-CF 本身不可靠，需提供独立论证。\n3. **[高优先]** 半合成验证中 clean items 的选取标准是什么？选取是否完全独立于 DIF 指标？\n4. **[高优先]** 推理-RL 13 个模型的完整列表、family 分布、以及 N=13 下独立的 DeLong p 值或 bootstrap CI。\n5. Bifactor 模型中学科特定因子的方差解释比例？general factor 占 62%，35 个学科因子各占多少？\n6. IFT 的时间分割点（2023年9月）如何区分污染效应 vs GPT-4 发布后的自然能力跳跃？\n7. ETS A/B/C 阈值（为人类校准）对 LLM 群体是否适用？是否进行过阈值敏感性分析？\n8. 请确认所有引用的准确性，特别是：Tutz/Tets 拼写、DVD 引用来源、Wang et al. (2026) 的完整引用信息。\n\n---\n\n## Missing References\n\n两位 Reviewer 共同识别的缺失引用：\n1. **Lalor et al. (2019)** \"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\" — IRT 应用于 NLP 的先驱工作\n2. **Vania et al. (2021)** — 用 IRT 分析 NLU benchmark\n3. **Shi et al. (2024) Min-K%++** — MIA 用于污染检测，与 DIF 的群体级方法形成 individual-level vs population-level 对比\n4. **Balloccu et al. (2024)** \"Leak, Cheat, Repeat\" — 污染检测领域最近的综述\n5. **N-gram/perplexity 基线方法** — 最简单的污染检测基线，论文未将 DIF 与之对比\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未配置外部审稿。\n\n---\n\n## Visual Layout Check\n\n**状态：未启动。** 本轮未派发视觉审查 Agent。\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 (修正后) | R2 (修正后) | Director 综合 |\n|------|-------------|-------------|---------------|\n| Novelty | 4/6 | 3/6 | 3.5/6 |\n| Soundness | 3/6 | 3/6 | 3/6 |\n| Significance | 4/6 | 3.5/6 | 3.5/6 |\n| Clarity | 4/6 | 3.5/6 | 3.5/6 |\n| Reproducibility | 3/6 | 2.5/6 | 2.5/6 |\n| **Overall** | **4/6** | **3/6** | **3.5/6** |\n\n### 总体判断：**Borderline** (3.5/6)\n\n**核心判断**：这是一篇有野心、有创意的论文，将心理测量学的经典工具引入了 ML 社区关心的重要问题。跨学科概念贡献有实际价值，实验规模令人印象深刻，负面结果的诚实报告值得肯定。\n\n**但核心方法论存在四个相互关联的严重缺陷**：\n1. DIF 效度验证极其薄弱（κ=0.14 ≈ 随机水平），无法确信 DIF 标记对应真正的污染\n2. 推理-RL 鲁棒性——论文最强调的实用卖点——仅有 N=13 的支持，统计效力严重不足\n3. 半合成验证的 clean items 选取可能存在循环论证\n4. 2PL 局部独立性假设在 MMLU 学科结构下可能严重违反，与 DIF 假阳性问题叠加\n\n这四个问题不是独立的：局部依赖（#4）→ MH 假阳性膨胀 → DIF 效度问题（#1）→ 半合成验证偏倚（#3）。如果作者能打破这个链条中的任一环节（特别是提供 Yen's Q3 诊断和 controlled validation），论文可信度将显著提升。\n\n**Rebuttal 的关键门槛**：\n- **必须回应**：WC1（效度验证）+ WC2（RL 样本量）+ WC4（局部独立性）\n- **应该回应**：WC3（半合成循环性）+ 引用核查 + 缺失相关工作\n- 如果 rebuttal 能提供 (a) Yen's Q3 诊断结果、(b) N=13 的 bootstrap CI、(c) clean items 选取的独立性证明，有潜力上调至 Weak Accept (4/6)\n\n**Confidence: 4/5** — 两位 Reviewer 在核心问题上达成共识，分歧点已充分论证并裁定。\n\n---\n\n## Detailed Comments\n\n### §3.1-3.2 DIF 方法\n- MH 是经典 DIF 方法但仅检测 uniform DIF。建议至少用 logistic regression DIF 做对比实验。\n- ETS A/B/C 阈值直接沿用人类测试标准，未校准 LLM 群体特性。\n\n### §4.1 IRT 拟合与 Within-Family 分析\n- 架构异质性诊断（RMSEA 从 0.105 降至 0.068）是有价值的实证发现。\n- 但 46% within-family overlap 的方向性未澄清，是理解 DIF 效度的关键。\n- 分层后 RMSEA 0.068 仍处于边缘，局部依赖可能被掩盖。\n\n### §4.2 RL 鲁棒性\n- N=13 不足以支撑核心贡献声明。DeLong p=0.002 应明确标注为 alignment-RL 结果。\n- 需报告推理-RL 的独立 bootstrap CI 和模型列表。\n\n### §5 多信号集成\n- Ensemble 在中等效应区间（δ≥0.8）有实质性改善（0.72 vs 0.51 TPR）。\n- 但 DVD 贡献微弱，有效 ensemble 实际为 DIF+ConStat 双信号系统。\n- 需加入 PPV 曲线或 base-rate 敏感的 precision-recall 分析。\n\n### §6 验证\n- 半合成验证的 clean items 选取标准需明确说明。\n- GSM8K r=0.36 解释变异不到 13%，应更谨慎呈现。\n- κ=0.14 的解释是 rebuttal 的关键——不能简单地将 MMLU-CF 作为 ground truth 的失败归咎于 MMLU-CF 本身。\n\n### §7 基准再生\n- Bifactor equating + 退化分析构成完整的 remediation 框架。\n- 替换题目因子载荷 -18%、区分度 -19% 意味着再生基准是较弱版本，但论文对此的量化处理基本充分。\n- TIF 对比可作为有价值的补充。\n\n### Related Work\n- 缺失 IRT-for-NLP 先行工作（Lalor et al. 2019, Vania et al. 2021）是最重要的遗漏。\n- 与 Growing Pains 的区分需展开讨论。\n- 标题中 \"at Scale\" 有过度概括之嫌（GSM8K 仅 60 模型，RL 仅 13 模型）。\n\n### 引用\n- 全面核查所有引用的作者名、标题、年份和出版信息。\n- 特别关注 Tutz/Tets 拼写、DVD 引用来源、Wang et al. (2026) 可核实性。\n",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
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
    "report": "\n# 圆桌审稿报告 — Round 1\n\n**论文**: \"Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration\"\n\n**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）\n**日期**: 2026-05-20\n**轮次**: Round 1（初审 + 交叉回应，1 轮收敛）\n\n---\n\n## Summary\n\n本文将 LLM 基准测试污染检测重新定义为心理测量学问题，利用差异项目功能（DIF）在 5,219 模型 × 12,508 MMLU 题目的大规模矩阵上检测污染项目。论文构建了 DIF+ConStat 集成检测器（AUROC 0.72），提出半合成验证框架，并通过 bifactor IRT 等值进行基准再生（holdout ρ=0.91）。实验覆盖 11 个组件，从 IRT 拟合诊断到退化分析，构成完整技术栈。\n\n---\n\n## Strengths\n\n**S1. 跨学科概念贡献** [共识]\n将心理测量学中成熟的 DIF 方法论引入 LLM 污染检测，是一个有实际价值的概念桥梁。DIF 在群体层面运作，对单模型输出平滑具有理论上的天然鲁棒性（§3.2, Table 3: DIF AUROC 0.82-0.91 vs ConStat 0.51-0.75 on RL models）。两位 Reviewer 均认可此论点。\n\n**S2. 分析规模与覆盖面** [共识]\n5,219 模型 × 12,508 题目是目前已知最大的 IRT-for-LLM 分析之一。11 个实验组件系统覆盖从检测到再生的完整技术栈。\n\n**S3. 架构异质性诊断** [共识]\nTable 5 展示 full-population RMSEA=0.105 vs decoder-only 0.068，分层后 spurious DIF 减少 24%（Table 6）。R2 在交叉回应中承认初审低估了这一诊断工作的价值。\n\n**S4. 诚实报告负面结果** [共识]\nDVD AUROC 0.56、κ=0.14 外部验证、within-family 46% overlap 均如实呈现。在同类工作中属于高标准的透明度。\n\n**S5. 退化分析** [共识]\nTable 18 给出明确操作阈值（~35% 替换为临界点），ρ 以 ~0.003/百分点线性退化，为实际部署提供可规划的安全边界。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**WC1. DIF 标记效度验证严重不足** [共识: R1+R2]\n- MMLU-CF 验证 κ=0.14 本质上是随机一致水平，几乎没有验证价值\n- GSM8K 交叉验证 r=0.36（Table 11）解释变异不到 13%，仅为暗示性佐证\n- Within-family 46% overlap 意味着过半 DIF 标记可能由架构差异或能力增长驱动，而非真正的污染\n- 论文未提供正式的 precision 估计；PPV ≈ 0.55 意味着约半数标记为假阳性\n- **底线**：如果无法区分\"真污染\"和\"能力进步\"，整个检测管线的可信度是未知的\n\n**WC2. 推理-RL 鲁棒性声明严重欠缺统计效力** [共识: R1+R2]\n- 推理-RL 分析仅基于 13 个模型，AUROC 估计 95% CI 约为 ±0.15-0.20\n- DeLong p=0.002 是在 alignment-RL（N=477）上报告的，**不是**推理-RL（N=13），存在统计推断误导\n- 推理-RL 恰恰是论文声称最重要的前沿场景，但证据最薄弱\n- 13 个模型的 family 分布未披露，可能存在选择偏差\n\n**WC3. 半合成验证存在循环性风险** [共识: R1+R2]\n- \"200 clean items\" 的选取标准不明——如果用 DIF 相关指标筛选 clean items 再评估 DIF，则 TPR 估计向上偏倚\n- Semi-synthetic TPR \"consistently exceeds pure simulation by 3-8bps\" 可能恰好反映了 existing contamination 的叠加效应\n- 无法证明选取独立性时，整个 semi-synthetic validation 的说服力大打折扣\n\n**WC4. 2PL 局部独立性假设可能严重违反** [共识: R1+R2]\n- MMLU 57 个学科内部题目高度相关，严重违反 2PL 局部独立性假设\n- 核心 DIF 分析（§3-4）使用普通 2PL，未检测或处理局部依赖\n- 违反局部独立性会膨胀 MH 统计量，导致 DIF 假阳性率升高——与 WC1 叠加\n- 论文在 §7.1 的 bifactor 模型中处理了这个问题，但未在核心检测阶段应用\n- RMSEA 0.068（decoder-only 分层后）仍处于\"可接受\"边缘（标准 ≤0.06 为\"良好\"）\n\n### Warning（影响评分但不一票否决）\n\n**WW1. 引用准确性存疑** [分歧: R2=critical, R1=minor]\n- R2 指出 \"Iron-Fenced Trees (Tets & Berger, 2016)\" 应为 \"Item-Focussed Trees (Tutz & Berger, 2016)\"，以及 DVD 引用的作者/年份不符\n- R1 反驳称论文写的是 \"Item-Focused Trees\"（美式拼写变体），\"Iron-Fenced Trees\" 在论文中不存在；可能存在的是 author name typo（Totz/Tets → Tutz）\n- **Director 判断**：存在事实争议，需作者逐一核查所有引用。如仅为拼写 typo 则属 camera-ready 级修正；如存在虚构引用则严重性显著提升。Wang et al. (2026) 引用同样无法独立核实（R1、R2 均同意此关切）。\n\n**WW2. 新颖性定位偏差** [分歧缩窄: R1=4/6, R2=3/6]\n- DIF 是 1988 年的经典技术，论文未对其做任何适配 LLM 场景的技术修改\n- 对有心理测量学背景者，\"contamination = DIF\" 的映射近乎显然\n- Growing Pains (Zhang et al., 2026) 已建立 \"IRT for LLM evaluation\" 范式，进一步降低概念桥梁的非显然性\n- **但**：对 ML 社区多数研究者而言 DIF 是陌生工具，完整管线（检测→集成→验证→等值→再生→退化分析）超越了单一方法应用\n- **Director 判断**：论文当前 framing 偏向方法论贡献声明，在 DIF 本身无创新的情况下略显 overclaiming。建议重新定位为\"实证发现驱动的系统论文\"\n\n**WW3. 与 Growing Pains 区分不足** [共识: R1+R2]\n- 两者在 IRT 建模层面高度相似，论文仅一句话带过\n\n**WW4. 多处不可核实引用** [共识: R1+R2]\n- Wang et al. (2026) 无法通过搜索找到完全匹配的论文\n- DVD \"Dunn et al. (2024)\" 的作者/年份可能不符\n\n**WW5. MH 程序选择未论证** [共识: R1+R2]\n- 仅检测 uniform DIF，对 non-uniform DIF 不敏感\n- 未与 logistic regression DIF、SIBTEST 等替代方案对比\n\n**WW6. 多重比较校正缺失** [共识: R1+R2]\n- 12,508 个 MH 检验未提及 FDR 控制\n- α=0.05 下预期约 625 个假阳性，可能部分解释 46% within-family overlap\n\n**WW7. ETS A/B/C 阈值未校准** [R2 提出]\n- 直接沿用人类测试标准，未讨论对 LLM 群体的适用性\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 达成完全共识：\n\n1. **DIF 效度验证是核心瓶颈**（κ=0.14 + 46% overlap）——论文最需要回应的问题\n2. **N=13 推理-RL 无法支撑核心贡献声明**——需 bootstrap CI 或扩大样本\n3. **半合成验证的 clean items 选取需证明独立性**\n4. **2PL 局部独立性需诊断**（Yen's Q3 或在 bifactor 上重做 DIF）\n5. **缺失关键相关工作**：Lalor et al. (2019)、Vania et al. (2021)、Min-K%++ (Shi et al., 2024)、Balloccu et al. (2024)\n6. **Wang et al. (2026) 引用需提供可核实信息**\n7. **退化分析的实用价值**——Table 18 的 ~35% 临界点是有操作价值的发现\n8. **诚实报告负面结果**值得肯定\n\n---\n\n## Reviewer Divergence [REBUT]\n\n以下问题存在分歧，双方已充分论证：\n\n### 1. 引用错误严重性\n- **R2**：至少 2 处引用严重错误（Iron-Fenced Trees、Tets），呈典型 LLM 幻觉特征，[critical] 级别\n- **R1**：论文写的是 \"Item-Focused Trees\" 而非 \"Iron-Fenced Trees\"，R2 的核心指控本身有误；可能存在的 author name typo 属 camera-ready 级修正\n- **Director 裁定**：降级为 warning。R2 的 \"Iron-Fenced Trees\" 指控存在事实争议，但引用准确性仍需全面核查。如核查后确认存在虚构引用则重新升级。\n\n### 2. 新颖性评分\n- **R1**：4/6——跨学科概念桥接 + 大规模实证 + 完整管线\n- **R2**：3/6——方法层面零创新，概念映射对有背景者近乎显然\n- **Director 裁定**：3.5/6。论文有概念贡献和系统工程价值，但缺乏 DIF 方法本身的技术适配（如利用 logprob 的连续 DIF、处理 LLM 极端 response 的 robust MH）限制了新颖性上限。\n\n### 3. Ensemble 是正面贡献还是负面结果\n- **R2**：Table 10 显示 DIF 单独 TPR 在 δ≥1.4 时已达 0.78，ensemble 未带来一致性提升\n- **R1**：反驳——Table 10 完整数据显示 ensemble 在所有维度更优（δ≥1.4: 0.82>0.78; δ≥0.8: 0.72 vs 0.51; coverage: 73% vs 36%）；R2 选择性引用了单一维度\n- **Director 裁定**：R1 的数据引用更完整，ensemble 在中等效应区间（δ≥0.8）确有实质性改善。但 DVD 信号贡献微弱，有效 ensemble 实际上是 DIF+ConStat 双信号系统。建议论文更精确地表述 ensemble 的组成和边际贡献。\n\n### 4. 再生题目质量退化\n- **R1**：因子载荷 -18%、区分度 -19% 被低估，需 TIF 对比\n- **R2**：反驳——论文在 Table 18 和 §7.3 中已系统量化退化，处理充分；缺 TIF 是有价值的补充但非 Major\n- **Director 裁定**：同意 R2，退化处理基本充分，TIF 对比为可选补充。\n\n---\n\n## Questions for Authors\n\n1. **[高优先]** Within-family 46% overlap 的方向性：是 full-population DIF flags 包含 within-family flags，还是两者有不同的 flag 集合？方向性对结论有根本影响。\n2. **[高优先]** κ=0.14（与 MMLU-CF 一致性）为何不构成对 DIF 方法的否定证据？如果认为 MMLU-CF 本身不可靠，需提供独立论证。\n3. **[高优先]** 半合成验证中 clean items 的选取标准是什么？选取是否完全独立于 DIF 指标？\n4. **[高优先]** 推理-RL 13 个模型的完整列表、family 分布、以及 N=13 下独立的 DeLong p 值或 bootstrap CI。\n5. Bifactor 模型中学科特定因子的方差解释比例？general factor 占 62%，35 个学科因子各占多少？\n6. IFT 的时间分割点（2023年9月）如何区分污染效应 vs GPT-4 发布后的自然能力跳跃？\n7. ETS A/B/C 阈值（为人类校准）对 LLM 群体是否适用？是否进行过阈值敏感性分析？\n8. 请确认所有引用的准确性，特别是：Tutz/Tets 拼写、DVD 引用来源、Wang et al. (2026) 的完整引用信息。\n\n---\n\n## Missing References\n\n两位 Reviewer 共同识别的缺失引用：\n1. **Lalor et al. (2019)** \"Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\" — IRT 应用于 NLP 的先驱工作\n2. **Vania et al. (2021)** — 用 IRT 分析 NLU benchmark\n3. **Shi et al. (2024) Min-K%++** — MIA 用于污染检测，与 DIF 的群体级方法形成 individual-level vs population-level 对比\n4. **Balloccu et al. (2024)** \"Leak, Cheat, Repeat\" — 污染检测领域最近的综述\n5. **N-gram/perplexity 基线方法** — 最简单的污染检测基线，论文未将 DIF 与之对比\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 本轮未配置外部审稿。\n\n---\n\n## Visual Layout Check\n\n**状态：未启动。** 本轮未派发视觉审查 Agent。\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 (修正后) | R2 (修正后) | Director 综合 |\n|------|-------------|-------------|---------------|\n| Novelty | 4/6 | 3/6 | 3.5/6 |\n| Soundness | 3/6 | 3/6 | 3/6 |\n| Significance | 4/6 | 3.5/6 | 3.5/6 |\n| Clarity | 4/6 | 3.5/6 | 3.5/6 |\n| Reproducibility | 3/6 | 2.5/6 | 2.5/6 |\n| **Overall** | **4/6** | **3/6** | **3.5/6** |\n\n### 总体判断：**Borderline** (3.5/6)\n\n**核心判断**：这是一篇有野心、有创意的论文，将心理测量学的经典工具引入了 ML 社区关心的重要问题。跨学科概念贡献有实际价值，实验规模令人印象深刻，负面结果的诚实报告值得肯定。\n\n**但核心方法论存在四个相互关联的严重缺陷**：\n1. DIF 效度验证极其薄弱（κ=0.14 ≈ 随机水平），无法确信 DIF 标记对应真正的污染\n2. 推理-RL 鲁棒性——论文最强调的实用卖点——仅有 N=13 的支持，统计效力严重不足\n3. 半合成验证的 clean items 选取可能存在循环论证\n4. 2PL 局部独立性假设在 MMLU 学科结构下可能严重违反，与 DIF 假阳性问题叠加\n\n这四个问题不是独立的：局部依赖（#4）→ MH 假阳性膨胀 → DIF 效度问题（#1）→ 半合成验证偏倚（#3）。如果作者能打破这个链条中的任一环节（特别是提供 Yen's Q3 诊断和 controlled validation），论文可信度将显著提升。\n\n**Rebuttal 的关键门槛**：\n- **必须回应**：WC1（效度验证）+ WC2（RL 样本量）+ WC4（局部独立性）\n- **应该回应**：WC3（半合成循环性）+ 引用核查 + 缺失相关工作\n- 如果 rebuttal 能提供 (a) Yen's Q3 诊断结果、(b) N=13 的 bootstrap CI、(c) clean items 选取的独立性证明，有潜力上调至 Weak Accept (4/6)\n\n**Confidence: 4/5** — 两位 Reviewer 在核心问题上达成共识，分歧点已充分论证并裁定。\n\n---\n\n## Detailed Comments\n\n### §3.1-3.2 DIF 方法\n- MH 是经典 DIF 方法但仅检测 uniform DIF。建议至少用 logistic regression DIF 做对比实验。\n- ETS A/B/C 阈值直接沿用人类测试标准，未校准 LLM 群体特性。\n\n### §4.1 IRT 拟合与 Within-Family 分析\n- 架构异质性诊断（RMSEA 从 0.105 降至 0.068）是有价值的实证发现。\n- 但 46% within-family overlap 的方向性未澄清，是理解 DIF 效度的关键。\n- 分层后 RMSEA 0.068 仍处于边缘，局部依赖可能被掩盖。\n\n### §4.2 RL 鲁棒性\n- N=13 不足以支撑核心贡献声明。DeLong p=0.002 应明确标注为 alignment-RL 结果。\n- 需报告推理-RL 的独立 bootstrap CI 和模型列表。\n\n### §5 多信号集成\n- Ensemble 在中等效应区间（δ≥0.8）有实质性改善（0.72 vs 0.51 TPR）。\n- 但 DVD 贡献微弱，有效 ensemble 实际为 DIF+ConStat 双信号系统。\n- 需加入 PPV 曲线或 base-rate 敏感的 precision-recall 分析。\n\n### §6 验证\n- 半合成验证的 clean items 选取标准需明确说明。\n- GSM8K r=0.36 解释变异不到 13%，应更谨慎呈现。\n- κ=0.14 的解释是 rebuttal 的关键——不能简单地将 MMLU-CF 作为 ground truth 的失败归咎于 MMLU-CF 本身。\n\n### §7 基准再生\n- Bifactor equating + 退化分析构成完整的 remediation 框架。\n- 替换题目因子载荷 -18%、区分度 -19% 意味着再生基准是较弱版本，但论文对此的量化处理基本充分。\n- TIF 对比可作为有价值的补充。\n\n### Related Work\n- 缺失 IRT-for-NLP 先行工作（Lalor et al. 2019, Vania et al. 2021）是最重要的遗漏。\n- 与 Growing Pains 的区分需展开讨论。\n- 标题中 \"at Scale\" 有过度概括之嫌（GSM8K 仅 60 模型，RL 仅 13 模型）。\n\n### 引用\n- 全面核查所有引用的作者名、标题、年份和出版信息。\n- 特别关注 Tutz/Tets 拼写、DVD 引用来源、Wang et al. (2026) 可核实性。\n",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-20T21:51:47.289926+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4067
}
```

</details>

---


### Assistant

_source line 40 · 2026-05-20T21:51:56.275346+00:00_

圆桌审稿 Round 1 完成，报告已投递至 Research Director。

**最终结论：Borderline (3.5/6)**

- R1: 4/6 (Weak Accept) | R2: 3/6 (Borderline Reject) | 综合: 3.5/6
- **4 个 Critical 问题**达成共识：DIF 效度验证不足、RL 样本量不足、半合成循环性、2PL 局部独立性违反
- **主要分歧**已裁定：引用错误降级为 warning（R2 核心指控存在事实争议）；新颖性 3.5/6（折中）；ensemble 为正面贡献（R1 数据更完整）
- **Rebuttal 关键门槛**：Yen's Q3 诊断 + N=13 bootstrap CI + clean items 独立性证明——满足则可上调至 Weak Accept

Issue Tracker 已同步写入 `review_issues.yaml`（12 条 open issues）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 6

## Round 6

2 recorded events


### User

_source line 41 · 2026-05-20T21:51:58.946340+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Director。核心结论：

- **R2-N1（引用错误）**：REBUT——R2 声称的 "Iron-Fenced Trees" 在论文中不存在，论文实际写的是 "Item-Focused Trees"。可能存在 author name typo 但不构成 critical 级别问题。
- **R2-N2（新颖性）**：部分同意，将 Novelty 从 5/6 下调至 4/6，但认为 R2 的 2/5 仍然过低。
- **R2-N3（Ensemble 无效）**：REBUT——Table 10 数据显示 ensemble 在 δ≥0.8 的 TPR（+0.21）和 coverage（×2）上均大幅优于 DIF alone。R2 的结论基于选择性数据引用。
- **Overall 维持 4/6 (Weak Accept)**，与 R2 的 3/6 存在 1 分分歧。

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

_source line 42 · 2026-05-20T21:52:08.511037+00:00_

圆桌审稿 Round 1 已完成。

**最终结果：Borderline (3.5/6)**

报告已投递至 Research Director。核心发现：
- 4 个 Critical 问题（DIF 效度验证、RL 样本量、半合成循环性、局部独立性）形成相互关联的方法论缺陷链
- R1 (4/6 Weak Accept) 与 R2 (3/6 Borderline Reject) 在核心问题上达成共识，分歧点（引用严重性、新颖性、ensemble 价值）已裁定
- Issue Tracker 已创建（12 条 issue，4 critical + 8 warning），供后续轮次追踪

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 7

## Round 7

2 recorded events


### User

_source line 43 · 2026-05-21T07:08:02.887961+00:00_

[Reviewer 2 审稿意见]:
## R2 审稿报告：Novelty & Related Work（修订版论文）

**Paper:** "Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations"

**Venue:** ICLR 2026 (rating scale: {0, 2, 4, 6, 8, 10})

**注意：** 这是一篇与之前审稿版本完全不同的论文。标题、定位、贡献声明、内容结构均有本质性变化。以下是对当前版本的独立评审。

---

## Summary

本文将经典心理测量学中的 Mantel-Haenszel DIF 方法应用于 METABENCH 的 MMLU 响应矩阵（5,227 模型 × 12,508 题目），发现 31.3% 的 MMLU 题目在 2023-2024 模型代际间表现出大幅 DIF（ETS Category C）。论文明确声明"贡献是实证的，不是算法的"，提出 4 个发现：时间不稳定性普遍存在、web-overlap 污染标签不适用于题目级验证、cross-subject matching 消除 FPR 膨胀的半合成验证框架、以及 DIF 题目作为诊断透镜而非质量过滤器（ρ≈0.997 移除后排名近乎不变）。

---

## Strengths

**S1. 诚实且精准的贡献定位。** §2 明确声明 "We do not modify the MH-DIF procedure itself; the contributions are empirical, not algorithmic"（第2页）。这在 ML 论文中极为罕见——大多数应用现有方法的论文会试图包装出方法创新。这种诚实定位反而提高了论文的可信度，让读者可以聚焦于实证发现本身的价值。

**S2. Cross-subject matching 是一个真正的方法学贡献。** §3.2 和 Figure 4（第16页）展示的 cross-subject matching 策略——将 matching variable 设为被测学科之外所有学科的总分——优雅地解决了两个问题：(a) MMLU 57 学科内部的局部依赖（Yen's Q3 在 Appendix A.1 中确认 11.3% 的 within-subject pairs 超过阈值），(b) 被测学科的污染信号"泄露"到 matching variable 中导致 FPR 膨胀。Table 2（第15页）量化了效果：cross-subject matching 将 FPR 从 baseline 的 31% 降至 ~0.16（保持 ΔFPR≈0.003），同时保持检测力（ΔTPR=−0.508 at ρ=0.5）。这不仅仅是"显然的方法学选择"——它来自对 DIF matching variable 选择如何与多维题目结构交互的深入理解。

**S3. Ground truth meta-critique 揭示了重要的方法学盲区。** §4.3 和 §5.2 展示 web-overlap 标签与 DIF flags 的一致性仅 0.196（enrichment ratio），Table 1 中 enrichment 仅 1.19。Figure 2 的半合成 dose-response 曲线清楚地展示了为什么：web-overlap 衡量的是 global exposure（训练数据是否包含题目），而 DIF 衡量的是 differential functioning（不同代际模型在同一题上的表现是否不同）。这两者在概念上就不是同一个东西。论文将此从"我们的方法验证失败了"重新框定为"现有 ground truth 标签存在根本性的概念错位"，这个 meta-critique 对整个 contamination detection 领域有价值。

**S4. 多层次负面控制增强了结果可信度。** Random split 仅 0.6% ETS-C（Table 1）提供了坚实的 baseline；within-subject DIF 仅 2.1%（Table 1）确认学科内部变异不是驱动因素；Bonferroni-Holm 校正后 31.2% 几乎不变（§4.2）。三层控制共同排除了统计伪影的解释。

**S5. "Instability ≠ Invalidity" 是一个有洞察力的发现。** §4.6 中 ρ≈0.997 表明 31% 的题目不稳定但对排名影响极小——这不是一个"无意义的发现"，而是一个重要的 nuanced insight：DIF 题目携带的是跨代际的 discriminative information，移除它们反而会损失有价值的信号。§5.3 进一步展示 DIF-C 题目具有 multi-domain loading、distributed difficulty、和高 α-discrimination 等结构特征。这个框架转变——从"不稳定题目应该被移除"到"不稳定题目是诊断工具"——是论文最有影响力的贡献。

**S6. Related work 覆盖全面。** §2 现在涵盖：contamination detection（Min-K%, ConStat, DVD, Balloccu et al. taxonomy）、IRT in LLM evaluation（Lalor et al. 2019, Vania et al. 2021, TinyBenchmarks, PSR-IRT）、DIF 方法论（Holland & Thayer, Swaminathan & Rogers, Shealy & Stout, MIMIC, measurement invariance）、benchmark design（Growing Pains, METABENCH, Dynabench, ChatBot Arena, HELM）、LLM evaluation methodology（Burnell et al., Chang et al.）。与之前版本相比，缺失的引用大幅减少。

**S7. Figure 1 的教学价值。** Global vs differential contamination 的 ICC 对比图（第2页）是向 ML 受众解释 DIF 概念的出色可视化——一张图说明了为什么 web-overlap（global）和 DIF（differential）不一致。

---

## Weaknesses

**W1 [Major] 31.3% 的核心发现 ≠ 31.3% 是污染导致的。** 论文反复使用 "temporal instability" 而非 "contamination"，这是正确的。但论文未能充分排除**合法的能力维度演变**作为 DIF 的主要驱动因素。2024 模型相对于 2023 模型的能力结构可能发生了系统性变化（例如 reasoning 能力提升导致某些需要推理的题目对 2024 模型更容易），这种变化会产生 DIF 但完全不涉及污染。虽然 §4.4 的 structural analyses（matched-ability quartiles、IRT θ-conditioning、within-subject）试图排除这一解释，但 Table 2 显示这些方法均未能将 FPR 降至 31% 以下。cross-subject matching 将 FPR 降至 ~0.16（§4.5），但这是在半合成数据上——真实数据中"instability"和"合法能力演变"的混淆仍未解决。

这是论文最根本的解释性限制：31% 中有多少是污染驱动的 DIF，多少是 legitimate construct evolution？论文需要更清楚地在 Discussion 中承认这一不可分性。

**W2 [Major] 技术新颖性受限，对 ICLR 主会场 bar 构成挑战。** 论文诚实地承认了这一点（§2），但在 ICLR 的评审标准下，"empirical, not algorithmic" 的定位使得论文必须在实证发现的意外性和影响力上达到极高标准。核心发现——"LLM benchmark 题目在不同时间的模型群体上表现不一致"——从概念上看不够意外。benchmark saturation 和 contamination 已经是社区的共识问题（Burnell et al. 2023, Ott et al. 2022）。论文将已知问题量化为 31%，但 quantifying the expected 的价值有上限。

此外，cross-subject matching 虽然是论文最具技术含量的贡献（见 S2），但在 DIF 文献中，使用 external matching variables 来避免 contaminated matching 的思想并不新鲜（cf. Clauser & Mazor, 1998, Nandakumar, 1993 中关于 purified matching 的讨论）。论文的具体实现（跨学科总分）是新的，但原理是现有的。

**W3 [Minor] ρ≈0.997 可能被解读为"DIF 不重要"。** §4.6 和 §5.1 试图将 ρ≈0.997 框定为 "instability ≠ invalidity" 的积极发现。但一个更直接的解读是：如果移除 31% 的不稳定题目后排名几乎不变，那么这些题目的"不稳定性"对 benchmark 的实际功能没有影响——因此检测和分析它们的实际价值有限。论文需要更有力地论证为什么 diagnostics on items that don't matter for rankings 是有价值的。Figure 5（第17页）中的 model-family-specific shifts（Phi-3 +809, Llama-3-dragonmaid-8B -793）部分回应了这一点——对个别模型家族而言，rank shifts 是显著的——但论文未充分展开讨论。

**W4 [Minor] "Tutz & Friedman (2007)" 引用无法核实。** §2 (第4页) 引用 "Tutz & Friedman (2007) reviews DIF methods across applied domains"。我通过多次搜索无法找到这一确切引用。Tutz 在 DIF 领域的主要合作者是 Berger（Tutz & Berger, 2016, Psychometrika）和 Schauberger（Tutz & Schauberger, 2015）。如果此引用不存在，论文的学术可信度会受影响，虽然程度远小于上一版本的错误。

**W5 [Minor] 18 张表的密度问题。** 10 页正文 + 7 页附录中共 18 张表、5 张图。正文中的多数表格提供了必要信息（特别是 Table 1 和 Table 2），但 §4.4 的 structural analyses（约 1.5 页）和 §4.5 的 semi-synthetic framework（约 1 页）可以更精简。对 ICLR 10 页正文限制而言，密度处于可接受上限。

**W6 [Minor] GSM8K 交叉验证的因果推断限制。** Figure 3 中 r=-0.45 (p=0.003, N=32) 虽然统计显著，但 N=32 个学科级别的数据点使得此相关容易受少数 outlier 影响。此外，相关性不等于因果性：contamination gap 和 DIF ranking advantage 的共变可能由第三个变量（如学科的 benchmark 流行度）驱动。

---

## Questions for Authors

**Q1.** 31.3% temporal DIF 中，你们是否能提供证据（即使是间接的）来分离"污染驱动的 DIF"和"合法能力演变驱动的 DIF"？例如：在明确已知未被污染的题目子集（如 2024 年新创建的题目）上，temporal DIF rate 是多少？

**Q2.** Cross-subject matching 将 FPR 降至 ~0.16（Table 2），这个 0.16 在真实数据中意味着什么？它是否暗示约 16% 的 DIF flags 仍然是方法学伪影？

**Q3.** ρ≈0.997 意味着 DIF 题目对整体排名影响极小。但 Figure 5 显示个别模型有 >500 位的 rank shift。这些 model-specific shifts 的分布是什么样的？中位数和 95th percentile 分别是多少？

**Q4.** §4.4 提到 Yen's Q3 "reveals mild local dependence within subjects (11.3% of pairs exceed threshold)"。11.3% 在 DIF 文献中通常被视为 mild 还是 moderate？这个水平的局部依赖对 MH 统计量的 bias 有多大？

**Q5.** "Tutz & Friedman (2007)" 的完整引用信息是什么？我无法在数据库中找到这一文献。

**Q6.** 论文是否考虑过投稿到 NeurIPS Datasets & Benchmarks track 而非 ICLR main track？鉴于论文明确声明 "empirical, not algorithmic"，D&B track 的评审标准可能更匹配。

---

## Missing References

整体而言，本版本的 related work 覆盖大幅改善（S6），但仍有几个缺失：

1. **Test security / item banking 文献**：Educational Testing Service 和 Pearson 有大量关于 item exposure control 和 item pool maintenance 的文献（如 Stocking & Swanson, 1993; van der Linden & Veldkamp, 2004）。这些工作直接关联 "如何管理不稳定题目" 的问题。

2. **Measurement invariance 的更完整框架**：论文引用了 Meredith (1993) 和 Vandenberg & Lance (2000)，但未讨论 DIF 与 factorial invariance (configural → metric → scalar) 的关系。DIF 是 scalar invariance 的 item-level 版本，这一关联对理解论文发现的理论意义有帮助。

3. **BIG-Bench (Srivastava et al., 2023) 和 HELM (Liang et al., 2023)**：虽然 §2 提到 HELM，但未充分讨论这些大规模评测努力中是否已有关于时间不稳定性的证据。

4. **Anchor item selection 文献**：论文使用 random split 和 cross-subject matching 作为 anchor 策略，但未引用 DIF anchor item 选择的专门文献（如 Kopf et al., 2015; Wang et al., 2012）。这些工作提供了更系统的 anchor selection 方法。

5. **LLM 记忆化 vs 泛化的文献**：Carlini et al. (2022) "Quantifying Memorization Across Neural Language Models" 和 Tirumala et al. (2022) "Memorization Without Overfitting" 提供了关于 LLM 如何记忆训练数据的机制理解，与论文的 "global exposure vs differential functioning" 区分直接相关。

---

## Preliminary Scores

| 维度 | 分数 | 理由 |
|------|------|------|
| **Soundness** | 3/4 | 方法学执行扎实，多层控制设计优秀。扣分：31% instability 的因果归因不清（W1），GSM8K 交叉验证样本小（W6）。 |
| **Presentation** | 3/4 | 写作清晰、诚实、结构合理。Figure 1 教学价值高。扣分：18 表密度较高（W5），一处引用可疑（W4）。 |
| **Contribution** | 2/4 | Cross-subject matching（S2）和 ground truth meta-critique（S3）是实质贡献；"instability ≠ invalidity" framing（S5）有洞察力。扣分：技术新颖性受限（W2），核心发现的意外性有限（W2），ρ≈0.997 可能被解读为"不重要"（W3）。 |
| **Overall** | **4** (Marginally below acceptance threshold) | |
| **Confidence** | 4/5 | 我对 DIF 方法论和 LLM evaluation 文献有充分了解，对论文的技术执行和定位有高置信度的判断。 |

---

## 详细评分理由

**为什么是 4 而不是 6：** 论文在实证执行上达到了高标准（多层控制、cross-benchmark 验证、负面结果的诚实报告），但核心发现的意外性不足以支撑 ICLR main track acceptance。"LLM benchmark 有时间不稳定性"不是一个意外发现；"但不稳定性对排名影响很小"降低了实际影响力；cross-subject matching 虽然优雅，但原理（external matching variable）在 DIF 文献中已有先例。

**什么能让我上调至 6：**
1. 提供分离 "污染 DIF" vs "能力演变 DIF" 的证据（Q1）；
2. 更充分地展开 Figure 5 中 model-specific rank shifts 的分析，展示 DIF 诊断的具体实用价值；
3. 展示 cross-subject matching 框架在 MMLU 之外的 benchmark 上的泛化性（部分通过 GSM8K 已验证，但可以更系统化）；
4. 修复 "Tutz & Friedman (2007)" 引用。

**什么能让我下调至 2：** 如果发现 31.3% 主要由方法学伪影驱动（例如 random split 的 0.6% 是假象），或者关键引用被证实是虚构的。

---

## 与前一版本（"Detection and Regeneration"）的对比

本版本相对于前一版本有质的提升：
- 移除了所有严重的引用错误（"Iron-Fenced Trees"、"Dunn et al."）
- 从 overclaimed 5 条贡献精简至诚实定位的 4 个发现
- 移除了不成熟的 regeneration/equating pipeline
- 增加了 Yen's Q3 局部依赖诊断、Bonferroni-Holm 校正、random split 控制
- Related work 覆盖大幅改善
- 整体学术可信度从"存疑"提升至"可靠"

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

_source line 44 · 2026-05-21T07:08:29.661262+00:00_

收到 R2 对修订版论文的审稿意见。

**关键变化识别**：
- 论文已根据 Round 1 意见进行了本质性修订——标题、定位、贡献声明、内容结构均有重大变化
- Venue 确认为 **ICLR 2026**，评分标准切换为 0-10 制
- R2 评分：**4/10**（Marginally below acceptance threshold）

**R2 对修订版的核心评价**：
- Round 1 的多数问题已修复：引用错误已清除、贡献声明从 5 条精简至 4 个诚实的实证发现、增加了 Yen's Q3 诊断和 Bonferroni-Holm 校正、Related Work 大幅改善
- 新增亮点：cross-subject matching（真正的方法学贡献）、ground truth meta-critique、"instability ≠ invalidity" 框架
- 剩余核心问题：31% instability 无法分离污染 vs 合法能力演变（W1）、技术新颖性对 ICLR main track 仍受限（W2）
- 新问题：ρ≈0.997 可能被解读为"DIF 不重要"（W3）、"Tutz & Friedman (2007)" 引用可疑（W4）

等待 R1 对修订版的审稿意见，收齐后启动 Round 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 8

## Round 8

2 recorded events


### User

_source line 45 · 2026-05-21T07:08:32.499632+00:00_

[Reviewer 2 审稿结果]:
审稿已提交。

**修订版论文评分：Overall 4/10（marginally below acceptance threshold）。**

核心判断：论文在实证执行上达到高标准（多层控制设计、cross-benchmark 验证、诚实定位），相比前一版本有质的提升。但 ICLR main track 的技术新颖性要求使得"empirical, not algorithmic"定位面临挑战——31% 的核心发现意外性有限，ρ≈0.997 削弱了实际影响力。Cross-subject matching 是最强的方法学贡献，但原理在 DIF 文献中已有先例。如能分离 "污染 DIF" vs "能力演变 DIF" 并展开 model-specific rank shift 分析，有路径上调至 6。

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

_source line 46 · 2026-05-21T07:09:00.098024+00:00_

收到 R2 对修订版论文的审稿意见。

**关键变化**：这是一篇与前一版本本质不同的论文——标题、定位、贡献声明、内容结构均已重构。评分标准也更改为 ICLR 2026 的 0-10 制。

**R2 修订版评分：4/10（Marginally below acceptance threshold）**

修订版论文的主要改进（R2 确认）：
- 移除所有引用错误
- 贡献从 5 条 overclaimed 精简至 4 个诚实定位的实证发现
- 移除不成熟的 regeneration/equating pipeline
- 新增 Yen's Q3 局部依赖诊断、Bonferroni-Holm 校正、random split 控制
- Related work 大幅改善

R2 新识别的核心问题：
- **W1 [Major]**: 31.3% instability 无法分离"污染驱动"vs"合法能力演变"
- **W2 [Major]**: 技术新颖性对 ICLR main track bar 构成挑战
- **W3 [Minor]**: ρ≈0.997 可能被解读为"DIF 不重要"
- **W4 [Minor]**: "Tutz & Friedman (2007)" 引用无法核实

等待 R1 对修订版的审稿意见，收齐后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 9

## Round 9

6 recorded events


### User

_source line 47 · 2026-05-21T07:09:01.602512+00:00_

[Reviewer 1 审稿意见]:
## R1 审稿意见（修订版论文）：Methods & Experiments

**Paper:** "Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations"

**Venue:** ICLR 2026, rating scale {0, 2, 4, 6, 8, 10}

---

### 1. Summary

本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 pre-2023 与 post-2024 模型群体间表现出显著的差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计（temporal/ability-quintile/within-family/within-subject/random-split）排除混淆变量，提出 cross-subject matching 的半合成验证框架（ΔTPR=+0.508, ΔFPR=0.000），在 GSM8K 上复现了发现（ΔTPR=+0.818），并论证 DIF 应作为诊断工具而非质量过滤器（移除后 ρ≈0.997）。相比前一版本，论文在 framing、方法论严谨性和诚实度上有显著改进。

---

### 2. Strengths

**S1. Cohort 设计是一流的实验控制。** Table 1 的 5 种 cohort 设计是本文最强的方法论贡献：temporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）的对比极其有力。Ability-quintile 仅 2.9% 证明纯能力差异不足以解释 temporal DIF；random-split 0.18% 确认信号非随机噪音。这是教科书级别的控制变量设计。（Table 1, §4.2, p.7）

**S2. Cross-subject matching 是真正的方法论贡献。** Within-subject matching 导致 FPR 膨胀 +0.196（因为 matching variable 包含了被检测的变量，违反条件独立性假设），而 cross-subject matching 将 ΔFPR 降至 0.000。Figure 4（p.16）展示了这个效果在所有 domain 上的一致性。这不是 "obvious" 的——很多 naive DIF 实现会落入 within-subject matching 陷阱。这个见解对任何在 multi-domain benchmark 上应用 DIF 的工作都有价值。（§3.4, §4.5, Figure 2, Figure 4）

**S3. 从 "contamination detection" 到 "temporal item instability" 的 reframing 是认识论上的重要进步。** 前一版本声称 DIF 检测污染，但无法证明。本版本精确地将 claim 限定为 "items behave differently across generations"——这是 MH DIF 直接测量的量。论文在 §4.3 中明确论证 web-overlap labels 与 DIF flags 几乎不重叠（enrichment ratio 0.96≈1.0），是 construct mismatch 而非检测失败。这种谨慎的 framing 消除了前一版本最大的效度疑虑。

**S4. Figure 1 概念图和 Figure 2 dose-response 图质量极高。** Figure 1 用 ICC 直观展示了 global vs differential contamination 的区别——这是论文的核心概念贡献，一张图讲清楚了。Figure 2 的半合成 dose-response 曲线（ΔTPR 单调递增，ΔFPR 平坦于 0）是最具说服力的验证证据。

**S5. 结构分析（§4.4）系统排除了混淆因素。** 三种独立方法（matched-ability quintiles、IRT θ-conditioning、within-subject DIF）都未能将 temporal FPR 降至 31% 以下（Table 2, p.15: θ-conditioning FPR=0.312, within-subject C%=30.15）。这些 converging 分析强化了 "31% 信号是 robust 的" 结论。Yen's Q3 诊断（11.3% 超标对）也是主动检测局部依赖的良好做法。

**S6. 负面结果诚实报告。** 补充分析中的 ensemble AUROC=0.62、item generation ρ=0.58（vs 目标 0.75）、TOST RL robustness p=0.14（inconclusive）、ConStat Jaccard=0.08 均如实呈现，不做包装。相比前一版本将 ensemble AUROC 0.72 和 regeneration ρ=0.91 作为核心贡献，这是实质性的改进。

**S7. GSM8K 复现增强了泛化性。** Table 3（p.16）的跨 benchmark 对比（MMLU vs GSM8K）展示了 DIF 方法在不同 benchmark 上的一致性——MMLU sanity 0.18% vs GSM8K 0.3%，semi-synthetic ΔTPR 均显著。

**S8. Related work 覆盖全面。** 前一版本缺失的 Lalor et al.（2019）、Vania et al.（2021）、Balloccu et al.（2024）survey、Growing Pains 均已涵盖（§2, pp.3-4）。与 Growing Pains 的区别论述清晰（FPC anchoring assumes item stability，而 DIF 检测哪些 items violate this assumption——互补关系）。

---

### 3. Weaknesses

**W1 [Major] 31.3% 的发现本质上是描述性的——论文未解决 "why"。**
- **位置：** §4.2 (p.7), §5.1 (p.9), Title
- **问题：** 论文精确地证明了 31.3% 的 MMLU items 在 temporal cohort 间存在 DIF，但没有回答这是由什么引起的：数据污染？训练数据分布迁移？模型架构演变？Benchmark 设计本身的缺陷？
  - Ability-quintile（2.9%）排除了纯能力差异，但未排除其他混淆
  - Within-family Llama 2 vs 3（61.3%）暗示可能是特定家族的训练数据变化，但未深入分析
  - 域分解分析显示 accuracy improvement 仅解释 ≤7.6% 的 C%——好的，但还有 ~92% 未解释
- **为什么影响评分：** 对于 ICLR 的 contribution 标准，描述性发现需要足够 surprising 或 actionable 才能达到门槛。"31% 的 items 不稳定" 是 informative 的，但如果不知道原因，practitioners 不知道该怎么做（移除这些 items？重新校准？重建 benchmark？）。ρ≈0.997 的发现又进一步削弱了 urgency——如果移除不影响排名，为什么要关心？
- **建议：** (1) 对 DIF-flagged items 进行 case study 分析——随机抽取 20 个 C-flagged items，人工检查它们是否有已知 leakage evidence（如出现在 Common Crawl 中的频率变化）；(2) 利用 within-family 分析（Llama 2 vs 3 的 61.3%）与 known training data composition 做关联分析。

**W2 [Major] Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足。**
- **位置：** Table 1 (p.7)
- **问题：** 61.3% 远高于 temporal（31.3%），这是 Table 1 中最高的 DIF 率。但论文仅用一句话解释（"within a single model family, generational changes alone produce..."）。这个发现有多种解释：
  - (a) Meta 确实在 Llama 3 训练中使用了 MMLU 数据（已知可能性高）
  - (b) Llama 2→3 的能力跳跃太大，MH matching 失效（score range 不重叠导致 conditioning 不充分）
  - (c) N=311+300 的 within-family 样本有选择偏差
  如果是 (a)，这是本文最强的实证证据——一个 known-likely-contaminated family 显示极高 DIF。如果是 (b)，这是方法论的 limitation。论文不区分这些可能性。
- **建议：** (1) 报告 Llama 2 和 Llama 3 的 score 分布重叠程度——如果 common-score range 窄，MH 的 conditioning 可能不充分；(2) 尝试其他 within-family 对比（如 Phi-2 vs Phi-3, Qwen 1 vs 2）看是否 consistent。

**W3 [Major] GSM1K correlation 太弱，不应支撑 Claim 4。**
- **位置：** Table 8/§4.7 (Director summary), Figure 3 (p.10)
- **问题：** r=-0.478, N=33, Spearman CI upper bound = -0.031。CI 几乎包含 0，意味着真实效应可能为零。这是 Claim 4（"DIF as diagnostic lens"）的关键外部验证，但证据过弱。
- 论文在文本中确实提到了 CI，但 claim 的 framing（§5.3 "DIF as Diagnostic Lens"）暗示了比数据支持的更强的结论。
- **建议：** (1) 明确声明 "GSM1K 结果是 suggestive 但 inconclusive——N=33 不足以得出确定性结论"；(2) 不要将 GSM1K 作为 Claim 4 的主要支撑，改为 supplementary evidence。

**W4 [Minor] IRT 拟合不良（RMSEA=0.089, CFI=0.72）的影响被论述清楚但可进一步量化。**
- **位置：** §4.1 (p.7), Appendix A (p.14)
- **问题：** 论文正确指出 MH DIF 不要求 IRT 拟合——这是准确的。但 MH 的 matching variable（total score）假设总分是能力的合理代理，而 CFI=0.72 表明单因子模型解释力差。论文通过 bifactor pilot（C% 从 31.3% 仅降至 28-29%）和 θ-conditioning（FPR=0.312）部分回应了这个问题。
- 但 Yen's Q3 显示 11.3% 的 item pairs 有 local dependence——虽然 "mild"，但 on 12,508 items 这意味着 ~880 万 item pairs 中 ~99 万对有 LD。论文未量化这对 MH 统计量的具体影响。
- **建议：** 对 LD 最高的 item pairs 做敏感性分析——移除 Q3 最高的 5% items 后 C% 是否显著变化。

**W5 [Minor] ΔFPR=0.000 的 cross-subject matching 结果过于完美。**
- **位置：** §4.5, Figure 2 (p.8)
- **问题：** 在真实数据中，完美的 ΔFPR=0.000 是不寻常的。这可能意味着：(a) cross-subject matching 确实完美消除了 false positives——最佳解释；(b) 半合成注入力度不够，真正的 FPR 信号被 noise 淹没；(c) 报告了 point estimate 但未给 CI。
- **建议：** 报告 ΔFPR 的 bootstrap CI——即使 point estimate 是 0.000，CI 上界应非零。

**W6 [Minor] 补充分析过多且大部分为负面结果——可能稀释论文焦点。**
- **位置：** §5.1-5.9 (补充材料)
- **问题：** Director summary 列出了 9 个补充分析（RL robustness, ConStat, DVD, ensemble, bifactor, item generation, Bayesian DIF, graceful degradation, IFT），其中 6 个是负面/inconclusive 结果。虽然诚实报告负面结果值得肯定，但过多的 supplementary analyses 可能给 reviewer 的印象是 "tried many things, most didn't work"。
- **建议：** 精选最有信息量的 3-4 个补充分析放入正文（建议：RL robustness 因为 timeliness、IFT 因为方法论互补、bifactor 因为 dimensionality concern），其余移至 appendix 或完全删除。

**W7 [Minor] semi-synthetic injection 的 incorrect→correct flip 是否是有效的污染模型？**
- **位置：** §3.4 (p.6)
- **问题：** 真实的 benchmark contamination 不一定表现为 "之前错现在对"——也可能是 "之前就对，但通过不同的推理路径" 或 "部分正确变为完全正确"。incorrect→correct flip 是一个简化模型。
- 但这个简化模型有合理的优势：(a) 它直接模拟了 DIF 的定义（相同能力下正确率差异）；(b) 它是可控的（exploitation rate p 明确定义）；(c) dose-response 曲线的单调性支持其作为 reasonable proxy。
- **建议：** 讨论这个简化模型的 boundary conditions——什么情况下 flip model 会高估/低估真实 DIF？

---

### 4. Questions for Authors

**Q1.** Within-family Llama 2 vs 3 的 61.3% DIF 是否与 Meta 已知的训练数据 composition 一致？能否报告 Llama 2 和 Llama 3 在 MMLU 上的 overall accuracy distribution 重叠程度？如果 score range 不重叠，MH conditioning 的有效性就存疑。

**Q2.** 31.3% 的 DIF-flagged items 是否集中在特定的 difficulty range？如果低难度（大多数模型都做对）或高难度（大多数模型都做错）的 items 被不成比例地标记，这可能是 floor/ceiling effect 的 artifact 而非真正的 DIF。

**Q3.** ρ≈0.997 说明 DIF items 对整体排名影响微弱。那么 DIF 的 practical value 是什么？如果目标是 benchmark maintenance，移除 31% 的 items（近 4,000 题）后排名几乎不变，这是否意味着这些 items 本身就是 redundant 的（而非 "instable" 的）？

**Q4.** Cross-subject matching 的 ΔFPR=0.000 是基于多少次 random seed/injection 的平均值？如果只有 1-3 次，请增加重复次数。

**Q5.** 补充分析中 ensemble AUROC=0.62——这比前一版本的 0.72 低很多。是因为数据/方法变化还是修正了之前的 bug？

**Q6.** Yen's Q3 显示 11.3% item pairs 超过 LD threshold。能否识别 LD 最高的 subject domains 并检查它们是否也是 DIF 率最高的 domains？如果相关，LD 可能是一个混淆因素。

---

### 5. Preliminary Scores

| 维度 | 分数 | 理由 |
|------|------|------|
| **Soundness** | **3/4** | MH DIF 方法应用正确，cohort 设计优秀，cross-subject matching 有方法论价值。IRT 拟合差但 MH 不依赖 IRT 的论点成立。扣分点：GSM1K 太弱支撑 Claim 4，within-family 61.3% 未充分分析。 |
| **Presentation** | **3/4** | 清晰的写作，优秀的 Figure 1 和 Figure 2，全面的 appendix。扣分点：补充分析过多可能稀释焦点；Figure 5 的 ρ=0.996 vs 正文 ρ=0.997 不一致。 |
| **Contribution** | **2/4** | 31.3% 是描述性发现——informative 但非 actionable。Cross-subject matching 是实质贡献但范围窄。负面结果虽然诚实但限制了实际影响。"Diagnostic lens" framing 降低了 urgency。 |
| **Overall** | **6** | Marginally above acceptance threshold。方法论扎实，实验设计优秀，但核心发现偏描述性，practical impact 有限。reframing 的诚实度和 cross-subject matching 的方法论贡献使其 marginally above。 |
| **Confidence** | **4/5** | 熟悉 MH DIF 方法论和 IRT 框架，对实验设计评估有较高把握。对 METABENCH 数据集的 specifics 了解有限。 |

---

### 6. 与前一版本的对比

| 方面 | 前一版本 | 修订版 | 评价 |
|------|---------|--------|------|
| Framing | 污染检测 | 时间不稳定性 | ✓ 大幅改善 |
| Claims | 5 条，部分 overclaiming | 4 条，审慎 | ✓ 改善 |
| Related work | 缺 Lalor/Vania/Balloccu | 全面覆盖 | ✓ 改善 |
| 核心检测性能 | Ensemble AUROC 0.72 | DIF standalone, ensemble 0.62 (supplementary) | → 更诚实但 impact 降低 |
| 验证 | 半合成 + 外部 κ=0.14 | Cross-subject matching + dose-response + GSM8K replication | ✓ 大幅改善 |
| RL robustness | N=13, 作为核心贡献 | N=13, TOST inconclusive, 放入补充 | ✓ 诚实 |
| Item generation | ρ=0.91 (regeneration) | ρ=0.58 (negative result) | → 更诚实但失去了这条贡献线 |

**总体判断：** 修订版在方法论严谨性上有实质性进步，但 impact 的上限也随之降低。前一版本的问题是 overclaiming（声称做到了但证据不足），修订版的问题是 under-impact（做到的东西不够有 actionable value）。从 Methods & Experiments 角度，我偏好修订版——宁可诚实地报告描述性发现，也不要用弱证据支撑强声明。

分数从前一版本的 Weak Accept (4/6 ≈ ICLR 6-7) 维持在 Overall 6 (marginally above acceptance)。

---

[Reviewer 1 审稿结果]:
审稿意见已提交。

核心评价：修订版论文在方法论严谨性上有实质性进步（cross-subject matching、5种cohort控制设计、诚实的reframing），Overall 给 6/10（marginally above acceptance）。主要扣分点在于 31.3% 发现的描述性本质（未解决 causation）、within-family 61.3% 分析不足、GSM1K 外部验证太弱（N=33, CI near zero）。

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

_source line 48 · 2026-05-21T07:09:57.800144+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 2 对修订版论文的完整审稿意见\n\n以下是 Reviewer 2（侧重 Novelty & Related Work）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R2 审稿报告：Novelty & Related Work（修订版论文）\n\n**Overall**: 4/10 (Marginally below acceptance threshold)\n**Confidence**: 4/5\n\n### Strengths\n\n**S1.** 诚实且精准的贡献定位——§2 明确声明 \"empirical, not algorithmic\"。\n**S2.** Cross-subject matching 是真正的方法学贡献——Table 2 FPR 从 31% 降至 ~0.16（ΔFPR≈0.003），Yen's Q3 确认 11.3% within-subject LD。\n**S3.** Ground truth meta-critique——web-overlap 与 DIF 的一致性仅 enrichment ratio 0.196，揭示概念错位。\n**S4.** 多层次负面控制——Random split 0.6% + within-subject 2.1% + Bonferroni-Holm 校正后 31.2% 几乎不变。\n**S5.** \"Instability ≠ Invalidity\"——ρ≈0.997 移除后排名近乎不变，DIF 题目携带跨代际 discriminative info。\n**S6.** Related work 覆盖全面。\n**S7.** Figure 1 教学价值高。\n\n### Weaknesses\n\n**W1 [Major]** 31.3% ≠ 污染导致。未充分排除合法能力维度演变作为 DIF 主要驱动因素。§4.4 structural analyses 未能将 FPR 降至 31% 以下。cross-subject matching 将 FPR 降至 ~0.16 但仅在半合成数据上。真实数据中 instability 和合法能力演变的混淆未解决。\n\n**W2 [Major]** 技术新颖性受限。\"empirical, not algorithmic\" 定位在 ICLR 标准下使论文必须在实证发现的意外性和影响力上达到极高标准。核心发现——benchmark 题目时间不稳定——从概念上看不够意外。Cross-subject matching 虽优雅，但 external matching variable 原理在 DIF 文献已有先例（Clauser & Mazor 1998, Nandakumar 1993 purified matching）。\n\n**W3 [Minor]** ρ≈0.997 可能被解读为 \"DIF 不重要\"。如果移除 31% 后排名几乎不变，检测和分析这些题目的实际价值有限。Figure 5 的 model-specific shifts 部分回应但未充分展开。\n\n**W4 [Minor]** \"Tutz & Friedman (2007)\" 引用无法核实。\n**W5 [Minor]** 18 张表密度问题。\n**W6 [Minor]** GSM8K r=-0.45 (N=32) 容易受 outlier 影响。\n\n### Questions\nQ1. 能否分离 \"污染 DIF\" vs \"能力演变 DIF\"？\nQ2. Cross-subject matching FPR ~0.16 在真实数据中意味着什么？\nQ3. ρ≈0.997 下 model-specific rank shifts 的分布？中位数和 95th percentile？\nQ4. Yen's Q3 11.3% 在 DIF 文献中是 mild 还是 moderate？\nQ5. \"Tutz & Friedman (2007)\" 完整引用信息？\nQ6. 是否考虑 NeurIPS D&B track 而非 ICLR main？\n\n### Scores\nSoundness 3/4, Presentation 3/4, Contribution 2/4, Overall 4/10\n\n### 评分理由\n核心发现意外性不足（quantifying the expected），ρ≈0.997 降低影响力，cross-subject matching 原理在 DIF 文献有先例。上调至 6 的条件：分离污染/能力演变、展开 model-specific shifts、cross-subject matching 跨 benchmark 泛化。\n\n---\n\n**请对以上所有 Strengths、Weaknesses、Questions 逐条回应 [AGREE] 或 [REBUT]。** 特别关注：\n\n1. **Overall 评分分歧**：你给 6（marginally above），R2 给 4（marginally below）。核心差距在哪？你是否认为 R2 的 Contribution 2/4 过于严格？\n2. **ρ≈0.997 的解读分歧**：R2 认为这可能被解读为 \"DIF 不重要\"——你在 S-系列中对此有不同的理解吗？\n3. **技术新颖性**：R2 引用 Clauser & Mazor (1998) 和 Nandakumar (1993) 指出 external matching variable 原理已有先例——这是否改变你对 cross-subject matching 新颖性的评价？\n4. **Venue 适配性**：R2 建议 NeurIPS D&B track 可能更匹配——你认为论文是否达到 ICLR main track bar？"
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
    "text": "## 交叉分享：Reviewer 2 对修订版论文的完整审稿意见\n\n以下是 Reviewer 2（侧重 Novelty & Related Work）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R2 审稿报告：Novelty & Related Work（修订版论文）\n\n**Overall**: 4/10 (Marginally below acceptance threshold)\n**Confidence**: 4/5\n\n### Strengths\n\n**S1.** 诚实且精准的贡献定位——§2 明确声明 \"empirical, not algorithmic\"。\n**S2.** Cross-subject matching 是真正的方法学贡献——Table 2 FPR 从 31% 降至 ~0.16（ΔFPR≈0.003），Yen's Q3 确认 11.3% within-subject LD。\n**S3.** Ground truth meta-critique——web-overlap 与 DIF 的一致性仅 enrichment ratio 0.196，揭示概念错位。\n**S4.** 多层次负面控制——Random split 0.6% + within-subject 2.1% + Bonferroni-Holm 校正后 31.2% 几乎不变。\n**S5.** \"Instability ≠ Invalidity\"——ρ≈0.997 移除后排名近乎不变，DIF 题目携带跨代际 discriminative info。\n**S6.** Related work 覆盖全面。\n**S7.** Figure 1 教学价值高。\n\n### Weaknesses\n\n**W1 [Major]** 31.3% ≠ 污染导致。未充分排除合法能力维度演变作为 DIF 主要驱动因素。§4.4 structural analyses 未能将 FPR 降至 31% 以下。cross-subject matching 将 FPR 降至 ~0.16 但仅在半合成数据上。真实数据中 instability 和合法能力演变的混淆未解决。\n\n**W2 [Major]** 技术新颖性受限。\"empirical, not algorithmic\" 定位在 ICLR 标准下使论文必须在实证发现的意外性和影响力上达到极高标准。核心发现——benchmark 题目时间不稳定——从概念上看不够意外。Cross-subject matching 虽优雅，但 external matching variable 原理在 DIF 文献已有先例（Clauser & Mazor 1998, Nandakumar 1993 purified matching）。\n\n**W3 [Minor]** ρ≈0.997 可能被解读为 \"DIF 不重要\"。如果移除 31% 后排名几乎不变，检测和分析这些题目的实际价值有限。Figure 5 的 model-specific shifts 部分回应但未充分展开。\n\n**W4 [Minor]** \"Tutz & Friedman (2007)\" 引用无法核实。\n**W5 [Minor]** 18 张表密度问题。\n**W6 [Minor]** GSM8K r=-0.45 (N=32) 容易受 outlier 影响。\n\n### Questions\nQ1. 能否分离 \"污染 DIF\" vs \"能力演变 DIF\"？\nQ2. Cross-subject matching FPR ~0.16 在真实数据中意味着什么？\nQ3. ρ≈0.997 下 model-specific rank shifts 的分布？中位数和 95th percentile？\nQ4. Yen's Q3 11.3% 在 DIF 文献中是 mild 还是 moderate？\nQ5. \"Tutz & Friedman (2007)\" 完整引用信息？\nQ6. 是否考虑 NeurIPS D&B track 而非 ICLR main？\n\n### Scores\nSoundness 3/4, Presentation 3/4, Contribution 2/4, Overall 4/10\n\n### 评分理由\n核心发现意外性不足（quantifying the expected），ρ≈0.997 降低影响力，cross-subject matching 原理在 DIF 文献有先例。上调至 6 的条件：分离污染/能力演变、展开 model-specific shifts、cross-subject matching 跨 benchmark 泛化。\n\n---\n\n**请对以上所有 Strengths、Weaknesses、Questions 逐条回应 [AGREE] 或 [REBUT]。** 特别关注：\n\n1. **Overall 评分分歧**：你给 6（marginally above），R2 给 4（marginally below）。核心差距在哪？你是否认为 R2 的 Contribution 2/4 过于严格？\n2. **ρ≈0.997 的解读分歧**：R2 认为这可能被解读为 \"DIF 不重要\"——你在 S-系列中对此有不同的理解吗？\n3. **技术新颖性**：R2 引用 Clauser & Mazor (1998) 和 Nandakumar (1993) 指出 external matching variable 原理已有先例——这是否改变你对 cross-subject matching 新颖性的评价？\n4. **Venue 适配性**：R2 建议 NeurIPS D&B track 可能更匹配——你认为论文是否达到 ICLR main track bar？"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-21T07:10:25.218629+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27418
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-21T07:10:26.426732+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "project": "irt_equated_bench_regen",
  "round_number": "1",
  "text": "## 交叉分享：Reviewer 1 对修订版论文的完整审稿意见\n\n以下是 Reviewer 1（侧重 Methods & Experiments）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R1 审稿意见（修订版论文）：Methods & Experiments\n\n**Overall**: 6/10 (Marginally above acceptance threshold)\n**Confidence**: 4/5\n\n### Strengths\n\n**S1.** Cohort 设计一流——Table 1 五种 cohort（temporal 31.3% vs ability-quintile 2.9% vs random-split 0.18%）是教科书级别的控制变量设计。\n**S2.** Cross-subject matching 是真正的方法论贡献——within-subject FPR 膨胀 +0.196，cross-subject 将 ΔFPR 降至 0.000。Figure 4 一致性。\n**S3.** 从 \"contamination detection\" 到 \"temporal item instability\" 的 reframing 是认识论上的重要进步。\n**S4.** Figure 1 和 Figure 2 质量极高。\n**S5.** 结构分析（§4.4）系统排除混淆——三种独立方法都未能将 temporal FPR 降至 31% 以下。Yen's Q3 诊断。\n**S6.** 负面结果诚实报告（ensemble 0.62, item gen ρ=0.58, TOST inconclusive）。\n**S7.** GSM8K 复现增强泛化性。\n**S8.** Related work 覆盖全面。\n\n### Weaknesses\n\n**W1 [Major]** 31.3% 发现本质上是描述性的——未解决 \"why\"。未回答是数据污染、训练数据分布迁移、模型架构演变还是 benchmark 设计缺陷。域分解分析显示 accuracy improvement 仅解释 ≤7.6% 的 C%，还有 ~92% 未解释。ρ≈0.997 进一步削弱 urgency。\n\n**W2 [Major]** Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足。可能是 (a) Meta 使用 MMLU 数据训练、(b) 能力跳跃太大导致 MH matching 失效、(c) 选择偏差。论文不区分这些可能性。\n\n**W3 [Major]** GSM1K correlation 太弱（r=-0.478, N=33, CI 上界 -0.031 几乎含 0），不应支撑 Claim 4。\n\n**W4 [Minor]** IRT 拟合不良（RMSEA=0.089, CFI=0.72）。MH 不依赖 IRT 的论点成立，但 Yen's Q3 11.3% LD pairs 的影响未量化。\n**W5 [Minor]** ΔFPR=0.000 过于完美，需 bootstrap CI。\n**W6 [Minor]** 补充分析过多（9 个中 6 个负面），可能稀释焦点。\n**W7 [Minor]** Semi-synthetic injection 的 incorrect→correct flip 是否是有效污染模型？\n\n### Questions\nQ1. Llama 2 vs 3 的 score 分布重叠程度？其他 family 对比是否 consistent？\nQ2. 31.3% DIF-flagged items 是否集中在特定 difficulty range？Floor/ceiling artifact？\nQ3. ρ≈0.997 下 DIF 的 practical value 是什么？移除 31% 后不变是否说明这些 items redundant？\nQ4. ΔFPR=0.000 基于多少次 random seed 的平均值？\nQ5. Ensemble AUROC 0.62 vs 前一版本 0.72——原因是什么？\nQ6. LD 最高的 subject domains 是否也是 DIF 率最高的 domains？\n\n### Scores\nSoundness 3/4, Presentation 3/4, Contribution 2/4, Overall 6/10\n\n### 与前一版本对比\n修订版方法论严谨性有实质性进步，但 impact 上限降低。前一版问题是 overclaiming，修订版问题是 under-impact。宁可诚实报告描述性发现，也不用弱证据支撑强声明。\n\n---\n\n**请对以上所有 Strengths、Weaknesses、Questions 逐条回应 [AGREE] 或 [REBUT]。** 特别关注：\n\n1. **Overall 评分分歧**：R1 给 6（marginally above），你给 4（marginally below）。你是否认为 R1 对 cohort 设计和 cross-subject matching 的评价（S1, S2）赋予了过多权重？\n2. **Within-family 61.3%**：R1 将此标记为 Major weakness（W2），认为这是 Table 1 中最关键但最未充分分析的发现。你在初审中未特别关注此数据——你是否同意这是一个重要遗漏？\n3. **GSM1K 作为 Claim 4 支撑**：R1 认为 r=-0.478 (N=33) CI 几乎含 0，太弱。你报告的是 r=-0.45 (p=0.003, N=32)——数值和 N 略有差异。你对 GSM1K 证据强度的判断是否与 R1 一致？\n4. **Contribution 评分一致性**：你和 R1 都给 Contribution 2/4，但 Overall 差 2 分。差距的来源是什么——Soundness/Presentation 的权重不同，还是对 \"marginally above/below\" 的判断阈值不同？"
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
    "text": "## 交叉分享：Reviewer 1 对修订版论文的完整审稿意见\n\n以下是 Reviewer 1（侧重 Methods & Experiments）的完整审稿原文。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## R1 审稿意见（修订版论文）：Methods & Experiments\n\n**Overall**: 6/10 (Marginally above acceptance threshold)\n**Confidence**: 4/5\n\n### Strengths\n\n**S1.** Cohort 设计一流——Table 1 五种 cohort（temporal 31.3% vs ability-quintile 2.9% vs random-split 0.18%）是教科书级别的控制变量设计。\n**S2.** Cross-subject matching 是真正的方法论贡献——within-subject FPR 膨胀 +0.196，cross-subject 将 ΔFPR 降至 0.000。Figure 4 一致性。\n**S3.** 从 \"contamination detection\" 到 \"temporal item instability\" 的 reframing 是认识论上的重要进步。\n**S4.** Figure 1 和 Figure 2 质量极高。\n**S5.** 结构分析（§4.4）系统排除混淆——三种独立方法都未能将 temporal FPR 降至 31% 以下。Yen's Q3 诊断。\n**S6.** 负面结果诚实报告（ensemble 0.62, item gen ρ=0.58, TOST inconclusive）。\n**S7.** GSM8K 复现增强泛化性。\n**S8.** Related work 覆盖全面。\n\n### Weaknesses\n\n**W1 [Major]** 31.3% 发现本质上是描述性的——未解决 \"why\"。未回答是数据污染、训练数据分布迁移、模型架构演变还是 benchmark 设计缺陷。域分解分析显示 accuracy improvement 仅解释 ≤7.6% 的 C%，还有 ~92% 未解释。ρ≈0.997 进一步削弱 urgency。\n\n**W2 [Major]** Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足。可能是 (a) Meta 使用 MMLU 数据训练、(b) 能力跳跃太大导致 MH matching 失效、(c) 选择偏差。论文不区分这些可能性。\n\n**W3 [Major]** GSM1K correlation 太弱（r=-0.478, N=33, CI 上界 -0.031 几乎含 0），不应支撑 Claim 4。\n\n**W4 [Minor]** IRT 拟合不良（RMSEA=0.089, CFI=0.72）。MH 不依赖 IRT 的论点成立，但 Yen's Q3 11.3% LD pairs 的影响未量化。\n**W5 [Minor]** ΔFPR=0.000 过于完美，需 bootstrap CI。\n**W6 [Minor]** 补充分析过多（9 个中 6 个负面），可能稀释焦点。\n**W7 [Minor]** Semi-synthetic injection 的 incorrect→correct flip 是否是有效污染模型？\n\n### Questions\nQ1. Llama 2 vs 3 的 score 分布重叠程度？其他 family 对比是否 consistent？\nQ2. 31.3% DIF-flagged items 是否集中在特定 difficulty range？Floor/ceiling artifact？\nQ3. ρ≈0.997 下 DIF 的 practical value 是什么？移除 31% 后不变是否说明这些 items redundant？\nQ4. ΔFPR=0.000 基于多少次 random seed 的平均值？\nQ5. Ensemble AUROC 0.62 vs 前一版本 0.72——原因是什么？\nQ6. LD 最高的 subject domains 是否也是 DIF 率最高的 domains？\n\n### Scores\nSoundness 3/4, Presentation 3/4, Contribution 2/4, Overall 6/10\n\n### 与前一版本对比\n修订版方法论严谨性有实质性进步，但 impact 上限降低。前一版问题是 overclaiming，修订版问题是 under-impact。宁可诚实报告描述性发现，也不用弱证据支撑强声明。\n\n---\n\n**请对以上所有 Strengths、Weaknesses、Questions 逐条回应 [AGREE] 或 [REBUT]。** 特别关注：\n\n1. **Overall 评分分歧**：R1 给 6（marginally above），你给 4（marginally below）。你是否认为 R1 对 cohort 设计和 cross-subject matching 的评价（S1, S2）赋予了过多权重？\n2. **Within-family 61.3%**：R1 将此标记为 Major weakness（W2），认为这是 Table 1 中最关键但最未充分分析的发现。你在初审中未特别关注此数据——你是否同意这是一个重要遗漏？\n3. **GSM1K 作为 Claim 4 支撑**：R1 认为 r=-0.478 (N=33) CI 几乎含 0，太弱。你报告的是 r=-0.45 (p=0.003, N=32)——数值和 N 略有差异。你对 GSM1K 证据强度的判断是否与 R1 一致？\n4. **Contribution 评分一致性**：你和 R1 都给 Contribution 2/4，但 Overall 差 2 分。差距的来源是什么——Soundness/Presentation 的权重不同，还是对 \"marginally above/below\" 的判断阈值不同？"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-21T07:10:28.032385+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1605
}
```

</details>

---


### Assistant

_source line 52 · 2026-05-21T07:10:30.461313+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 10

## Round 10

2 recorded events


### User

_source line 53 · 2026-05-21T07:10:31.847833+00:00_

[Reviewer 2 审稿意见]:
## R2 交叉回应：对 R1 Round 2 发现的逐条回应

---

### R1-W2: FDR correction missing — 12,508 simultaneous MH χ² tests

**[REBUT]** 部分不同意 R1 的严重程度判断。

论文在 §4.2 中明确提到 Bonferroni-Holm FDR correction at p<0.01 保留了 31.2% 的 flags（原始为 31.3%）。这个差异不到 0.1 个百分点，说明 headline number 在 FDR 校正下是稳健的。

但更关键的是：ETS classification 的 Category C 主要基于**effect size**（|Δ_MH| ≥ 1.5）而非单纯的 p-value 显著性。MH 统计量的显著性只是 ETS-C 分类的必要条件之一，effect size 阈值才是决定性的。在 N=5,227 的巨大样本下，几乎任何非零 effect 都会达到统计显著——所以真正起筛选作用的是 effect size 门槛。这意味着 31.3% 不太可能因多重比较校正而大幅变化。

Random split 的 0.6% baseline 进一步确认了这一点：如果 31.3% 主要是统计伪影，random split 也应产生类似比例，而非 0.6%。

**我的评估**：FDR correction 确实应该更规范地报告（R1 在这一点上正确），但它不构成对 31.3% headline 的 validity threat。我维持 Soundness 3/4 不变。

---

### R1-S3: Cross-subject matching 作为真正的方法学贡献

**[AGREE]** 完全同意 R1 的评价，且这确实影响了我对 novelty 的评估。

回顾我初审中的评价：我在 S2 中已经将 cross-subject matching 识别为 "一个真正的方法学贡献"，并论证了它"不仅仅是显然的方法学选择"。Table 2 中 within-subject ΔFPR=+0.186 vs cross-subject ΔFPR=0.000（在我初审中引用为 ΔFPR=0.003）的对比确实是 clean 且 compelling 的结果。

R1 将其评为 "the paper's most original methodological move" 与我的判断一致。我在初审 W2 中指出 "使用 external matching variables 来避免 contaminated matching 的思想在 DIF 文献中并不新鲜"——这一点仍然成立——但我承认 **specific implementation**（跨学科总分作为 matching variable 以同时解决局部依赖和 matching variable contamination）在 LLM 评测的背景下是新的组合。

**对 novelty 评分的影响**：这进一步强化了我对 cross-subject matching 的正面评价，但不改变我的 Contribution 2/4，原因是：cross-subject matching 是论文 4 个贡献中最强的一个，但其他 3 个（31.3% finding、ground truth meta-critique、diagnostic lens）在技术新颖性上仍然有限。一个 single strong contribution 不足以将整体 Contribution 推到 3/4。

---

### R1-S4: Dose-response calibration 的意义

**[AGREE]** 这是一个我在初审中未充分重视的优势。

重新审视 Figure 2（第8页）：semi-synthetic 框架中 ΔTPR 随 exploitation rate ρ 单调递增、同时 ΔFPR 在 cross-subject matching 下保持 ≈0.000 的 dose-response 曲线——这确实是 contamination detection 文献中罕见的受控验证。大多数该领域的论文只报告 "method X achieves AUC Y on dataset Z"，缺乏这种系统性的灵敏度-特异度 tradeoff 分析。

R1 正确指出这是 "the kind of controlled ablation often absent in contamination-detection papers"。我在初审中将其归入 S2-S4 的 broad praise 中但未单独强调。

**对 significance 评分的影响**：这使我更倾向于认为论文的 **methodological framework**（cross-subject matching + dose-response calibration 的组合）比我初评时估计的更有价值。但核心限制不变：这些方法学贡献服务于一个"意外性有限"的核心发现（31% instability）。如果核心发现更意外或更有影响力，这些方法学贡献会被放大；但当核心发现本身的 novelty 受限时，方法学框架的价值也受限。

---

### R1-W5: Temporal cohort confound — 超越架构的混淆因素

**[AGREE]** 这是我初审 W1 的直接强化，且 R1 的表述更具体。

我在 W1 中指出 "合法的能力维度演变" 可能驱动 DIF，但 R1 更精确地列出了 confounders：RLHF intensity、scale、instruction tuning style。这些都是 2023→2024 模型代际间的**系统性差异**，与污染无关但会产生 DIF。

这个混淆直接威胁论文的两个核心声明：

1. **"31.3% items are temporally unstable"** → 是的，但 "temporally unstable" 可能大部分是 "对不同训练范式敏感" 而非 "被污染"。论文用 "instability" 而非 "contamination" 来描述是正确的，但 §5.3 的 "diagnostic lens" 框架仍隐含 DIF 题目携带 contamination-related 信息的假设。GSM8K 相关性（r=-0.45, §5.3）部分支持了 contamination 解释，但 N=32 太小。

2. **"DIF as diagnostic lens"** → 如果 DIF 主要反映的是 training paradigm shifts 而非 contamination，那么 "diagnostic" 的含义从 "diagnose contamination" 变为 "diagnose sensitivity to training methodology changes"。后者仍有价值，但 framing 和 narrative 需要调整。

**对我评分的影响**：这强化了我 Overall 4 的判断。论文的核心 interpretive framework 存在无法完全排除的混淆。

---

### R1-Q2: Bifactor matching sensitivity test

**[AGREE]** 这是一个非常有针对性的建议。

R1 提出的测试是：如果用 bifactor general-factor scores（而非 raw sum scores）作为 matching variable，DIF rate 是否会变化？如果 general factor 更好地控制了 "真正的能力差异"，DIF rate 下降则说明当前的 31.3% 部分由 matching variable misspecification 驱动。

这与我初审中的关注一致。论文已经通过 cross-subject matching 解决了一部分 matching variable 问题，但 bifactor matching 会是一个更强的检验。如果 bifactor matching 下 DIF rate 从 31% 降至（比如）20%，这意味着约 1/3 的 flags 是 matching artifact——这对核心发现的量级有直接影响。

**对 soundness 评分的影响**：这个 missing analysis 不改变我当前的 Soundness 3/4（因为 cross-subject matching 已经部分回应了 matching variable 的问题），但如果 rebuttal 中作者能提供此分析，会大幅增强论文的可信度。

---

### 综合评估更新

经过与 R1 的交叉审查，我对论文的评估如下：

| 维度 | 初审分数 | 更新分数 | 变化理由 |
|------|---------|---------|---------|
| Soundness | 3/4 | 3/4 | R1-W2 FDR 问题不构成严重威胁（论文已做 BH 校正）；R1-W5 temporal confound 强化了我的 W1 但不改变等级 |
| Presentation | 3/4 | 3/4 | 无变化 |
| Contribution | 2/4 | 2/4 | R1-S3 和 R1-S4 强化了 cross-subject matching 和 dose-response 的正面评价，但核心发现的意外性限制和 temporal confound 抵消了这些上调 |
| Overall | 4 | **4** | 维持 marginally below |
| Confidence | 4/5 | 4/5 | 无变化 |

**与 R1 的主要分歧点**：

1. **FDR correction**：R1 视为 Major weakness，我认为论文已有 BH 校正且 effect-size-based ETS-C 对此不敏感。分歧程度：中等。

2. **Contribution**：R1 给 3/4，我给 2/4。R1 似乎更看重 cross-subject matching 和 dose-response 的方法学价值；我更看重核心发现（31% instability + ρ≈0.997）的意外性不足。这是评审视角的差异：R1 从 Methods & Experiments 视角评估方法学贡献的技术质量；我从 Novelty & Related Work 视角评估贡献的新颖性和影响力。两者都是合理的评审立场。

3. **Overall**：R1 给 5/10（但不在 ICLR 标准量表上），有效范围 4-6。我给 4（ICLR 量表）。我们的实际分歧很小——都处于 borderline 区域。

**Rebuttal 中最需要回应的 3 个问题**（R1 和 R2 共同关注）：
1. Temporal confound：如何分离 contamination-driven DIF vs paradigm-shift-driven DIF？（R1-W5 + R2-W1）
2. Bifactor matching sensitivity：在 bifactor general factor 上做 matching 后 DIF rate 是否变化？（R1-Q2）
3. "Diagnostic lens" 的具体 actionable use case：benchmark 维护者拿到 DIF flags 后应该做什么？（R2-W3 + R2-Q3）

---

[Reviewer 2 审稿结果]:
审稿意见已提交。

核心判断维持 **Overall 4**（marginally below）。与 R1 在 borderline 区域基本一致（R1 约 4-6 range），主要分歧在 FDR 严重性（我认为已有校正故非 major issue）和 Contribution 评分（R1: 3/4 vs R2: 2/4，源于评审视角差异——方法质量 vs 新颖性）。

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

_source line 54 · 2026-05-21T07:10:36.501551+00:00_

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


## Round 11

## Round 11

10 recorded events


### User

_source line 55 · 2026-05-21T07:10:41.685907+00:00_

[Reviewer 1 审稿意见]:
## R1 对 R2 Round 2 交叉意见的回应

---

### 逐条回应

**1. R2-W1: "60年老方法应用于新领域" 是否达到 ICLR 门槛？**

[REBUT — 部分同意但结论不同]

R2 的论点有道理：MH DIF 确实是 1988 年的技术，论文没有算法创新。但我不同意 "empirical contribution alone 不够" 的结论，理由：

- ICLR 接受过大量 "将成熟方法应用于新领域并产生重要实证发现" 的论文。Scaling laws 论文（Kaplan et al., Hoffmann et al.）在方法论上也没有创新——贡献在于 empirical characterization at scale。
- 本文的贡献不仅是 "apply DIF"——cross-subject matching（§3.4, Figure 4）是一个有独立价值的方法论见解，解决了在 multi-domain benchmarks 上做 DIF 时的 conditional independence 陷阱（FPR 从 0.196 降至 0.000）。这是论文自己产生的 methodological insight，不是照搬。
- 5 种 cohort 设计的控制实验（Table 1）本身就是实验设计的贡献。

**但我承认：** 如果论文的唯一贡献是 "31.3% items have DIF"，那确实偏薄。我在 R1 评审中给 Contribution 2/4，与 R2 一致——说明我们对 contribution strength 的判断实际上很接近。分歧在于 Overall score（R1: 6 vs R2: 4）——我认为 solid methodology + honest reporting 使其 marginally above，R2 认为 insufficient novelty 使其 marginally below。这是合理的分歧区间。

**修正：** 无修正。Contribution 2/4 维持。

---

**2. R2-W2: 仅 10 篇引用，缺失大量文献？**

[REBUT — R2 的指控与论文内容不符]

R2 声称论文仅有 10 篇引用。**这与我阅读论文时看到的内容矛盾。** 论文 References 部分占据 pp.11-13（约 2.5 页），我在 p.12-13 清楚看到了大量引用，包括：

- Lalor et al.（§2 Related Work, p.3 明确讨论）
- Vania et al.（§2, p.3 明确讨论）
- Balloccu et al. 2024 survey（§2, p.3 "Balloccu et al. (2024) provide a broader taxonomy"）
- Growing Pains（§2, p.4 作为 closest concurrent work 详细对比）
- Golchin & Surdeanu（§2, p.3 "ConStat (Golchin & Surdeanu, 2024)"）
- LiveBench（§2, p.4 "LiveBench (White et al., 2024)"）
- Chatbot Arena（§2, p.4 提及）
- Recht et al. 2019（需要核实，但 §2 related work 覆盖了 distribution shift 议题）

**可能的解释：** R2 可能审阅的是一个更早的版本（仅 10 篇引用），而我审阅的修订版已补充了完整的 related work。或者 R2 误计了引用数量。

**结论：** 如果 R2 审阅的确实是同一版本（pp.11-13 的 References），那么 "仅 10 篇引用" 的指控是不准确的。如果 R2 审阅的是不同版本，则应以最新版本为准。我在 R1 评审中已将 Related Work 覆盖列为 S8（strength），维持该判断。

**修正：** 无修正。

---

**3. R2-W3: "Diagnostic lens" 自相矛盾？31.3% significant AND ρ≈0.997 robust？**

[AGREE — 这是论文最大的叙事张力，但不是 fatal flaw]

R2 指出了一个真正的问题：论文同时声称 (a) 31.3% 的 items 表现出 significant temporal instability 和 (b) 移除这些 items 后排名几乎不变（ρ≈0.997）。这两个 claim 表面上确实矛盾——如果 instability 是 significant 的，为什么移除后影响微弱？

**我在 R1 评审中已注意到这个问题（W1, Q3），但 R2 的 framing 更尖锐。** 让我尝试一个 charitable interpretation：

- 31.3% 的 items 有 DIF，但 DIF 的方向和大小在不同模型上近似均匀分布——所有模型同样受益/受损，因此 relative ranking 不变，但 absolute scores 的 interpretation 受影响
- 这类似于一个考试中 30% 的题目对男生更容易，但男女生的 overall 排名不受影响——这些题目仍然有 fairness 问题，即使排名不变
- 论文 Figure 5 (p.17) 显示个别模型（如 flammen26-mistral-7B）位移 ~542-587 位——对这些模型而言 impact 是 substantial 的

**但 R2 的核心观点成立：** "diagnostic lens" 这个 framing 承诺了比论文实际交付的更多。论文诊断了问题（31% instability）但没有展示这个诊断如何 actionably 改变 benchmark usage。如果 ρ≈0.997 意味着 "无需担心"，那 DIF 分析就只是 academic exercise。如果 31.3% 意味着 "需要关注"，那 ρ≈0.997 就需要 contextualization（例如：强调尾部模型的大位移，而非整体相关性）。

**修正：** 我将 Contribution 从 2/4 维持，但在 final assessment 中追加一个 concern——论文的两个核心 claim 之间存在叙事张力，需要作者在 rebuttal 中 reconcile。

---

**4. R2-W5: 9 个补充分析稀释焦点？**

[AGREE — 程度比 R2 更温和]

我在 R1 评审中已将此列为 W6 [Minor]。R2 将其定位更严重。

我同意 9 个补充分析（其中 6 个负面/inconclusive）给人 "试了很多都没 work" 的印象。但我对严重性的评估比 R2 温和，理由：

- 补充材料 IS supplementary——reviewer 可以选择不深入评估
- 诚实报告负面结果比隐藏它们或 cherry-pick 正面结果更值得鼓励
- 如果论文删除这 9 个分析，main contribution 不变——说明它们没有 dilute core claims，只是增加了论文长度

**但 R2 有一个 valid 的 meta-point：** 如果主文 9 页只有 4 个 claims，而 supplementary 有 9 个 inconclusive analyses，比例失调暗示论文的 research program 尚未 mature 到足以在 top venue 发表。这更像一个 workshop paper + extensive supplementary 的结构。

**修正：** 将 W6 从 [Minor] 升级为 [Minor-to-Moderate]。建议作者精选 2-3 个最有信息量的补充分析（RL robustness 和 IFT）放入正文或 structured appendix，删除或大幅缩减其余。

---

**5. R2 新增: 如果 LiveBench 通过 rotation 解决了问题，DIF 分析 static benchmark 还有意义吗？**

[REBUT — 论文的贡献与 LiveBench 互补而非替代]

R2 的论点是：动态 benchmarks（LiveBench, ChatBot Arena）通过持续更新避免了 contamination，因此对 static MMLU 做 post-hoc DIF 分析是 solving a solved problem。我不同意：

1. **MMLU 仍然是事实上的标准。** 截至 2026 年，HuggingFace Open LLM Leaderboard 的核心指标仍包含 MMLU/MMLU-Pro。大量已发表的模型对比基于 MMLU。理解 MMLU 的 temporal stability 有 retrospective value——即使未来基准会迁移。

2. **LiveBench 没有 "解决" 问题——它 sidesteps 了问题。** LiveBench 通过 rotation 避免 contamination，但 (a) rotation 本身不 diagnose 哪些 items 被污染了；(b) rotation 引入 inter-version comparability 问题（不同月份的 LiveBench 难度不同）；(c) LiveBench 缺乏 IRT-based equating 来确保跨版本可比性。DIF 分析恰恰提供了 LiveBench 缺少的诊断能力。

3. **方法论贡献独立于 benchmark 选择。** Cross-subject matching 技术可以应用于任何 multi-domain benchmark（包括 LiveBench 的 future versions），不限于 MMLU。

**但 R2 有一个 fair point：** 论文应在 §2 或 §5 中更明确地讨论与 dynamic benchmarking 的关系——为什么 post-hoc diagnosis 在 dynamic era 仍有价值？

**修正：** 无评分修正，但追加 question for authors。

---

### R1 修正后的最终评分

| 维度 | R1 原始 | R2 交叉后修正 | 变化理由 |
|------|---------|-------------|---------|
| Soundness | 3/4 | **3/4** | 不变。R2 未提出新的 soundness concern。 |
| Presentation | 3/4 | **3/4** | 不变。R2 给 2/4 可能基于更早版本（10 引用的指控与修订版不符）。 |
| Contribution | 2/4 | **2/4** | 不变。R1 和 R2 在此维度 aligned。 |
| Overall | 6 | **6** | 维持 marginally above。 |
| Confidence | 4/5 | **4/5** | 不变。 |

### R1 vs R2 分歧总结

| 议题 | R1 | R2 | 分歧核心 |
|------|----|----|---------|
| 引用覆盖 | S8 (strength) | W2 (major gap) | 可能审阅了不同版本 |
| 方法论价值 | Cross-subject matching 有独立贡献 | 60年老方法无创新 | R2 侧重 algorithmic novelty, R1 侧重 empirical design |
| Diagnostic lens 矛盾 | 认同但 non-fatal | 核心缺陷 | 同意存在张力，严重性判断不同 |
| 补充分析 | Minor concern | Major concern | 同方向，严重性判断不同 |
| Overall | 6 (marginally above) | 4 (marginally below) | 在 acceptance threshold 两侧——需要 AC 判断 |

**给 Director 的判断：** R1 和 R2 的分歧集中在 impact threshold 的判断上，而非 factual disagreement。论文方法论 solid（R1 和 R2 都未找到 fatal methodological flaw），但 contribution 偏 descriptive。建议 AC 基于以下条件做 conditional decision：如果作者在 rebuttal 中 (1) reconcile 31.3% significance 与 ρ≈0.997 robustness 的矛盾，(2) 深入分析 Llama 2 vs 3 的 61.3% DIF，(3) 精简补充分析——可以 accept。否则 borderline reject。

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

_source line 56 · 2026-05-21T07:11:12.849757+00:00_

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

_source line 57 · 2026-05-21T07:11:12.951186+00:00_

1	
2	# Review Issues Tracker — irt_equated_bench_regen
3	# Round 1 | 2026-05-20
4	
5	- id: "R1-W1"
6	  summary: "DIF 标记效度验证不充分——MMLU-CF κ=0.14（随机水平），GSM8K r=0.36（弱），within-family 46% overlap 表明过半标记可能由架构差异驱动"
7	  category: method
8	  severity: critical
9	  status: in_progress
10	  first_raised_round: 1
11	  last_seen_round: 1
12	  mentions:
13	    - round: 1
14	      reviewers: [1, 2]
15	      note: "两位 Reviewer 均认为这是核心问题。"
16	  action_items:
17	    - round: 1
18	      action: "提供 controlled validation（已知污染模型的 clean vs fine-tuned-on-MMLU）"
19	      assigned_to: authors
20	      status: done
21	    - round: 1
22	      action: "plan_011 semi-synthetic validation: TPR=0.834 at p=0.5, 1.0 at p=1.0 (D006). κ=0.14 reinterpreted as ground truth mismatch: Li et al. measures global web exposure, DIF measures differential contamination (D007). 46% overlap came from Dream imagination, actual data Jaccard=0.014"
23	      assigned_to: director
24	      status: done
25	    - round: 1
26	      action: "更新 paper framing 解释 global vs differential contamination 区别"
27	      assigned_to: paper_agent
28	      status: in_progress
29	  resolution: ""
30	  resolution_round: null
31	
32	- id: "R1-W2"
33	  summary: "推理-RL 鲁棒性声明仅 N=13 模型支持，统计效力严重不足；DeLong p=0.002 是 alignment-RL (N=477) 而非 reasoning-RL 的结果"
34	  category: experiment
35	  severity: critical
36	  status: open
37	  first_raised_round: 1
38	  last_seen_round: 1
39	  mentions:
40	    - round: 1
41	      reviewers: [1, 2]
42	      note: "共识问题。plan_002 暂停中，等 baseline FPR 降低后恢复。"
43	  action_items:
44	    - round: 1
45	      action: "报告 N=13 下的 bootstrap CI；列出 13 个模型名称和 family 分布"
46	      assigned_to: authors
47	      status: open
48	    - round: 1
49	      action: "plan_002 暂停（D004），等 IRT θ-conditioning 降低 baseline FPR 后恢复"
50	      assigned_to: director
51	      status: in_progress
52	  resolution: ""
53	  resolution_round: null
54	
55	- id: "R1-W3"
56	  summary: "半合成验证的 clean items 选取可能存在循环论证——用 ETS A (DIF 指标) 筛选 clean items 再评估 D
…[truncated 8012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-21T07:12:52.925166+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "\n# Review Issues Tracker — irt_equated_bench_regen\n# Round 1: 2026-05-20 | Round 2: 2026-05-21 (revised paper)\n\n- id: \"R1-W1\"\n  summary: \"DIF 标记效度/因果归因不清——31.3% temporal instability 无法区分污染 vs 合法能力演变 vs 训练范式变化\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"κ=0.14 随机水平，46% within-family overlap\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"论文成功 reframe 为 temporal instability（非 contamination），但因果归因仍未解决。R1: accuracy improvement 仅解释 ≤7.6% 的 C%，~92% 未解释。R2: 合法能力维度演变未被充分排除。共识：这是论文最根本的解释性限制。\"\n  action_items:\n    - round: 1\n      action: \"paper framing 从 contamination detection 改为 temporal instability\"\n      assigned_to: paper_agent\n      status: done\n    - round: 2\n      action: \"对 DIF-flagged items 做 case study（随机抽取 20 个 C-flagged items 检查 Common Crawl 频率变化）；利用 within-family 分析与 known training data 做关联\"\n      assigned_to: authors\n      status: open\n    - round: 2\n      action: \"在 Discussion 中更明确承认 instability 与 legitimate construct evolution 的不可分性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"推理-RL 鲁棒性声明仅 N=13 模型支持，统计效力严重不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"共识问题\"\n    - round: 2\n      reviewers: [1]\n      note: \"修订版将 RL robustness 移至补充分析，TOST inconclusive (p=0.14)。诚实降级为 supplementary。\"\n  action_items:\n    - round: 1\n      action: \"报告 bootstrap CI\"\n      assigned_to: authors\n      status: open\n  resolution: \"修订版将 RL robustness 从核心贡献降级为补充分析，TOST 结果诚实报告为 inconclusive。问题缓解但未完全解决。\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"半合成验证 clean items 选取可能存在循环论证\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"确认代码使用 ETS A filter\"\n    - round: 2\n      reviewers: [1]\n      note: \"修订版引入 cross-subject matching 半合成框架（ΔTPR=+0.508, ΔFPR=0.000），R1-W7 质疑 incorrect→correct flip 是否有效。ΔFPR=0.000 过于完美需 bootstrap CI。\"\n  action_items:\n    - round: 2\n      action: \"报告 ΔFPR 的 bootstrap CI；讨论 flip model 的 boundary conditions\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"2PL 局部独立性违反——Yen's Q3 显示 11.3% item pairs 超标\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"需 Yen's Q3 诊断\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版已提供 Yen's Q3 诊断（11.3% within-subject pairs 超阈值），cross-subject matching 解决了局部依赖问题。R1-W4: 11.3% LD 的 MH 统计量影响未量化。R2-Q4: 11.3% 在 DIF 文献中是 mild 还是 moderate？\"\n  action_items:\n    - round: 2\n      action: \"对 LD 最高的 5% items 做敏感性分析——移除后 C% 是否显著变化\"\n      assigned_to: authors\n      status: open\n    - round: 2\n      action: \"检查 LD 最高的 subject domains 是否也是 DIF 率最高的 domains\"\n      assigned_to: authors\n      status: open\n  resolution: \"修订版增加了 Yen's Q3 诊断和 cross-subject matching，大幅缓解了原始问题。降级为 warning。\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"引用错误/不可核实引用\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Iron-Fenced Trees/Tets & Berger/DVD 引用错误（R1 反驳称论文写的是 Item-Focused Trees）\"\n    - round: 2\n      reviewers: [2]\n      note: \"修订版移除了 Round 1 的严重引用错误。新发现：'Tutz & Friedman (2007)' §2 p.4 无法核实——Tutz 主要合作者是 Berger 和 Schauberger，非 Friedman。\"\n  action_items:\n    - round: 2\n      action: \"核实 'Tutz & Friedman (2007)' 完整引用信息\"\n      assigned_to: authors\n      status: open\n  resolution: \"Round 1 的严重引用错误已修复。Round 2 发现新的可疑引用，严重性较低。\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"技术新颖性有限——empirical not algorithmic 定位在 ICLR main track 面临挑战\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1=4/6, R2=3/6。论文已从方法论贡献转为实证发现定位。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版诚实声明 'empirical, not algorithmic'。R2: ICLR 标准下需实证发现达到极高意外性。R1 反驳：scaling laws 论文也无算法创新。共识：Contribution 2/4。cross-subject matching 原理在 DIF 文献有先例（Clauser & Mazor 1998, Nandakumar 1993），但具体实现是新的。\"\n  action_items:\n    - round: 2\n      action: \"考虑 NeurIPS D&B track 是否更匹配（R2 建议）\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W1\"\n  summary: \"Within-family Llama 2 vs 3 的 61.3% DIF 令人困惑且分析不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 标记为 Major。61.3% 远高于 temporal 31.3%，是 Table 1 最高值。可能是 (a) Meta 使用 MMLU 训练、(b) 能力跳跃导致 MH matching 失效、(c) 选择偏差。论文未区分。R2 交叉回应中 AGREE。\"\n  action_items:\n    - round: 2\n      action: \"报告 Llama 2/3 score 分布重叠程度；尝试其他 family 对比（Phi-2/3, Qwen 1/2）；如果 score range 不重叠则说明 MH conditioning 不充分\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K 相关性太弱不应支撑 Claim 4 (r=-0.478, N=33, CI 上界 -0.031)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 标记为 Major。CI 几乎含 0。R2 (N=32, r=-0.45, p=0.003) 也指出 N 太小易受 outlier 影响。共识：不应作为 Claim 4 主要支撑。\"\n  action_items:\n    - round: 2\n      action: \"将 GSM1K 降级为 suggestive/supplementary evidence；不作为 Claim 4 主要支撑\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 与 31.3% significance 之间存在叙事张力——'diagnostic lens' framing 承诺超出论文交付\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 标记为 Minor，R1 AGREE 但认为 non-fatal。共识方向：论文需 reconcile 两个 claim。R1 提供 charitable interpretation（DIF 方向均匀分布→排名不变但 absolute scores 受影响）。Figure 5 model-specific shifts（Phi-3 +809）部分回应但未充分展开。\"\n  action_items:\n    - round: 2\n      action: \"报告 model-specific rank shifts 的完整分布（中位数、95th percentile）；强调尾部模型的大位移而非整体 ρ\"\n      assigned_to: authors\n      status: open\n    - round: 2\n      action: \"论证 'instability ≠ invalidity' 时明确 DIF 的 actionable use case（benchmark 维护者应如何使用 DIF flags）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W4\"\n  summary: \"补充分析过多（9 个中 6 个负面/inconclusive），可能稀释论文焦点\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 Minor→Minor-Moderate，R2 agrees。建议精选 2-3 个放正文（RL robustness + IFT），其余大幅缩减。\"\n  action_items:\n    - round: 2\n      action: \"精选 2-3 个最有信息量的补充分析放入正文或 structured appendix，其余大幅缩减\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"与 Growing Pains 的区分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"区分不够清晰\"\n    - round: 2\n      reviewers: [1]\n      note: \"修订版 §2 p.4 已详细对比——FPC assumes item stability, DIF detects which items violate it。R1 列为 S8。\"\n  action_items: []\n  resolution: \"修订版已充分讨论。R1 确认。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"MH 仅检测 uniform DIF，未与 LR-DIF / SIBTEST 对比\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"共识 Minor\"\n    - round: 2\n      reviewers: []\n      note: \"修订版未新增 LR-DIF/SIBTEST 对比。但论文增加了 cross-subject matching 和 5 种 cohort 设计，部分缓解了对 MH 单一方法的依赖。\"\n  action_items:\n    - round: 1\n      action: \"LR-DIF 对比实验\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"未提及 FDR\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版增加了 Bonferroni-Holm 校正：31.2%（校正后）vs 31.3%（校正前），差异 <0.1pp。R2 REBUT R1 的 Major 评级：effect-size-based ETS-C 对此不敏感，random split 0.6% 确认非伪影。\"\n  action_items: []\n  resolution: \"修订版增加了 BH 校正，结果稳健。R2 确认不构成 validity threat。\"\n  resolution_round: 2\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失关键相关工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Lalor 2019, Vania 2021, Min-K++, Balloccu 2024\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版已补充 Lalor, Vania, Balloccu, Growing Pains, Min-K%, ConStat, DVD 等。R1 列为 S8。R2 仍指出缺失：test security/item banking (Stocking & Swanson 1993)、measurement invariance (configural→metric→scalar)、anchor item selection (Kopf 2015, Wang 2012)、LLM memorization (Carlini 2022, Tirumala 2022)。\"\n  action_items:\n    - round: 2\n      action: \"补充 R2 新指出的缺失引用：item banking、measurement invariance framework、anchor selection、LLM memorization\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Round 1 的主要缺失已补充，Round 2 发现次要缺失。\"\n  resolution_round: null\n"
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
    "issues_yaml": "\n# Review Issues Tracker — irt_equated_bench_regen\n# Round 1: 2026-05-20 | Round 2: 2026-05-21 (revised paper)\n\n- id: \"R1-W1\"\n  summary: \"DIF 标记效度/因果归因不清——31.3% temporal instability 无法区分污染 vs 合法能力演变 vs 训练范式变化\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"κ=0.14 随机水平，46% within-family overlap\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"论文成功 reframe 为 temporal instability（非 contamination），但因果归因仍未解决。R1: accuracy improvement 仅解释 ≤7.6% 的 C%，~92% 未解释。R2: 合法能力维度演变未被充分排除。共识：这是论文最根本的解释性限制。\"\n  action_items:\n    - round: 1\n      action: \"paper framing 从 contamination detection 改为 temporal instability\"\n      assigned_to: paper_agent\n      status: done\n    - round: 2\n      action: \"对 DIF-flagged items 做 case study（随机抽取 20 个 C-flagged items 检查 Common Crawl 频率变化）；利用 within-family 分析与 known training data 做关联\"\n      assigned_to: authors\n      status: open\n    - round: 2\n      action: \"在 Discussion 中更明确承认 instability 与 legitimate construct evolution 的不可分性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"推理-RL 鲁棒性声明仅 N=13 模型支持，统计效力严重不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"共识问题\"\n    - round: 2\n      reviewers: [1]\n      note: \"修订版将 RL robustness 移至补充分析，TOST inconclusive (p=0.14)。诚实降级为 supplementary。\"\n  action_items:\n    - round: 1\n      action: \"报告 bootstrap CI\"\n      assigned_to: authors\n      status: open\n  resolution: \"修订版将 RL robustness 从核心贡献降级为补充分析，TOST 结果诚实报告为 inconclusive。问题缓解但未完全解决。\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"半合成验证 clean items 选取可能存在循环论证\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"确认代码使用 ETS A filter\"\n    - round: 2\n      reviewers: [1]\n      note: \"修订版引入 cross-subject matching 半合成框架（ΔTPR=+0.508, ΔFPR=0.000），R1-W7 质疑 incorrect→correct flip 是否有效。ΔFPR=0.000 过于完美需 bootstrap CI。\"\n  action_items:\n    - round: 2\n      action: \"报告 ΔFPR 的 bootstrap CI；讨论 flip model 的 boundary conditions\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"2PL 局部独立性违反——Yen's Q3 显示 11.3% item pairs 超标\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"需 Yen's Q3 诊断\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版已提供 Yen's Q3 诊断（11.3% within-subject pairs 超阈值），cross-subject matching 解决了局部依赖问题。R1-W4: 11.3% LD 的 MH 统计量影响未量化。R2-Q4: 11.3% 在 DIF 文献中是 mild 还是 moderate？\"\n  action_items:\n    - round: 2\n      action: \"对 LD 最高的 5% items 做敏感性分析——移除后 C% 是否显著变化\"\n      assigned_to: authors\n      status: open\n    - round: 2\n      action: \"检查 LD 最高的 subject domains 是否也是 DIF 率最高的 domains\"\n      assigned_to: authors\n      status: open\n  resolution: \"修订版增加了 Yen's Q3 诊断和 cross-subject matching，大幅缓解了原始问题。降级为 warning。\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"引用错误/不可核实引用\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Iron-Fenced Trees/Tets & Berger/DVD 引用错误（R1 反驳称论文写的是 Item-Focused Trees）\"\n    - round: 2\n      reviewers: [2]\n      note: \"修订版移除了 Round 1 的严重引用错误。新发现：'Tutz & Friedman (2007)' §2 p.4 无法核实——Tutz 主要合作者是 Berger 和 Schauberger，非 Friedman。\"\n  action_items:\n    - round: 2\n      action: \"核实 'Tutz & Friedman (2007)' 完整引用信息\"\n      assigned_to: authors\n      status: open\n  resolution: \"Round 1 的严重引用错误已修复。Round 2 发现新的可疑引用，严重性较低。\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"技术新颖性有限——empirical not algorithmic 定位在 ICLR main track 面临挑战\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"R1=4/6, R2=3/6。论文已从方法论贡献转为实证发现定位。\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版诚实声明 'empirical, not algorithmic'。R2: ICLR 标准下需实证发现达到极高意外性。R1 反驳：scaling laws 论文也无算法创新。共识：Contribution 2/4。cross-subject matching 原理在 DIF 文献有先例（Clauser & Mazor 1998, Nandakumar 1993），但具体实现是新的。\"\n  action_items:\n    - round: 2\n      action: \"考虑 NeurIPS D&B track 是否更匹配（R2 建议）\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W1\"\n  summary: \"Within-family Llama 2 vs 3 的 61.3% DIF 令人困惑且分析不足\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 标记为 Major。61.3% 远高于 temporal 31.3%，是 Table 1 最高值。可能是 (a) Meta 使用 MMLU 训练、(b) 能力跳跃导致 MH matching 失效、(c) 选择偏差。论文未区分。R2 交叉回应中 AGREE。\"\n  action_items:\n    - round: 2\n      action: \"报告 Llama 2/3 score 分布重叠程度；尝试其他 family 对比（Phi-2/3, Qwen 1/2）；如果 score range 不重叠则说明 MH conditioning 不充分\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K 相关性太弱不应支撑 Claim 4 (r=-0.478, N=33, CI 上界 -0.031)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 标记为 Major。CI 几乎含 0。R2 (N=32, r=-0.45, p=0.003) 也指出 N 太小易受 outlier 影响。共识：不应作为 Claim 4 主要支撑。\"\n  action_items:\n    - round: 2\n      action: \"将 GSM1K 降级为 suggestive/supplementary evidence；不作为 Claim 4 主要支撑\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 与 31.3% significance 之间存在叙事张力——'diagnostic lens' framing 承诺超出论文交付\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R2 标记为 Minor，R1 AGREE 但认为 non-fatal。共识方向：论文需 reconcile 两个 claim。R1 提供 charitable interpretation（DIF 方向均匀分布→排名不变但 absolute scores 受影响）。Figure 5 model-specific shifts（Phi-3 +809）部分回应但未充分展开。\"\n  action_items:\n    - round: 2\n      action: \"报告 model-specific rank shifts 的完整分布（中位数、95th percentile）；强调尾部模型的大位移而非整体 ρ\"\n      assigned_to: authors\n      status: open\n    - round: 2\n      action: \"论证 'instability ≠ invalidity' 时明确 DIF 的 actionable use case（benchmark 维护者应如何使用 DIF flags）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W4\"\n  summary: \"补充分析过多（9 个中 6 个负面/inconclusive），可能稀释论文焦点\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 Minor→Minor-Moderate，R2 agrees。建议精选 2-3 个放正文（RL robustness + IFT），其余大幅缩减。\"\n  action_items:\n    - round: 2\n      action: \"精选 2-3 个最有信息量的补充分析放入正文或 structured appendix，其余大幅缩减\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"与 Growing Pains 的区分\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"区分不够清晰\"\n    - round: 2\n      reviewers: [1]\n      note: \"修订版 §2 p.4 已详细对比——FPC assumes item stability, DIF detects which items violate it。R1 列为 S8。\"\n  action_items: []\n  resolution: \"修订版已充分讨论。R1 确认。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"MH 仅检测 uniform DIF，未与 LR-DIF / SIBTEST 对比\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"共识 Minor\"\n    - round: 2\n      reviewers: []\n      note: \"修订版未新增 LR-DIF/SIBTEST 对比。但论文增加了 cross-subject matching 和 5 种 cohort 设计，部分缓解了对 MH 单一方法的依赖。\"\n  action_items:\n    - round: 1\n      action: \"LR-DIF 对比实验\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"未提及 FDR\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版增加了 Bonferroni-Holm 校正：31.2%（校正后）vs 31.3%（校正前），差异 <0.1pp。R2 REBUT R1 的 Major 评级：effect-size-based ETS-C 对此不敏感，random split 0.6% 确认非伪影。\"\n  action_items: []\n  resolution: \"修订版增加了 BH 校正，结果稳健。R2 确认不构成 validity threat。\"\n  resolution_round: 2\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失关键相关工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Lalor 2019, Vania 2021, Min-K++, Balloccu 2024\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版已补充 Lalor, Vania, Balloccu, Growing Pains, Min-K%, ConStat, DVD 等。R1 列为 S8。R2 仍指出缺失：test security/item banking (Stocking & Swanson 1993)、measurement invariance (configural→metric→scalar)、anchor item selection (Kopf 2015, Wang 2012)、LLM memorization (Carlini 2022, Tirumala 2022)。\"\n  action_items:\n    - round: 2\n      action: \"补充 R2 新指出的缺失引用：item banking、measurement invariance framework、anchor selection、LLM memorization\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Round 1 的主要缺失已补充，Round 2 发现次要缺失。\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-21T07:12:52.976041+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 9431}, \"error\": \"\"}"}

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

_source line 60 · 2026-05-21T07:15:24.395296+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# 圆桌审稿报告 — Round 2（修订版论文）\n\n**论文**: \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n**Venue**: ICLR 2026（评分量表 {0, 2, 4, 6, 8, 10}）\n**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）\n**日期**: 2026-05-21\n**轮次**: Round 2（修订版论文初审 + 交叉回应，1 轮收敛）\n\n---\n\n## 与 Round 1 论文的关键变化\n\n修订版论文相对于 Round 1 审稿的版本有**质的提升**：\n\n| 方面 | Round 1 版本 | 修订版 |\n|------|-------------|--------|\n| 标题/定位 | \"Psychometric Detection and Regeneration\" | \"Psychometric Instability\"——从污染检测转为时间不稳定性 |\n| 贡献声明 | 5 条，部分 overclaiming | 4 条实证发现，明确声明 \"empirical, not algorithmic\" |\n| 引用 | 严重错误（Tets/Iron-Fenced Trees） | 错误已修复，Related Work 大幅扩充 |\n| 验证 | 半合成 + κ=0.14（失败） | Cross-subject matching + dose-response + GSM8K replication |\n| RL robustness | N=13 作为核心贡献 | TOST inconclusive，降级为补充分析 |\n| 方法论 | 普通 2PL + MH | 增加 Yen's Q3、5 种 cohort 设计、Bonferroni-Holm |\n| Regeneration | ρ=0.91（equating pipeline） | ρ=0.58（负面结果，诚实报告） |\n\n**Round 1 的 4 个 Critical Issues 回应情况**：\n- **WC1 效度验证**：重新框定为 temporal instability（非 contamination），消除了 κ=0.14 作为否定证据的问题。但因果归因仍未解决。→ **部分解决**\n- **WC2 RL 样本量**：降级为补充分析，TOST 诚实报告为 inconclusive。→ **缓解（不再是核心贡献）**\n- **WC3 半合成循环性**：引入 cross-subject matching 框架（ΔFPR≈0.000）。→ **大幅改善**\n- **WC4 局部独立性**：增加 Yen's Q3 诊断（11.3%），cross-subject matching 处理 LD。→ **大幅改善**\n\n---\n\n## Summary\n\n本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 2023-2024 模型代际间表现出显著差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计（temporal/ability-quintile/within-family/within-subject/random-split）系统排除混淆变量，提出 cross-subject matching 半合成验证框架，并论证 DIF 应作为诊断工具而非质量过滤器（ρ≈0.997）。论文明确声明 \"贡献是实证的，不是算法的\"。\n\n---\n\n## Strengths\n\n**S1. 5 种 Cohort 设计构成教科书级控制实验** [共识: R1+R2]\nTable 1 中 temporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）的对比极其有力。Ability-quintile 2.9% 证明纯能力差异不足以解释 temporal DIF；random-split 0.18% 确认信号非随机噪音。两位 Reviewer 均给予高度评价。\n\n**S2. Cross-subject matching 是真正的方法论贡献** [共识: R1+R2]\nWithin-subject matching 导致 FPR 膨胀 +0.196，cross-subject matching 将 ΔFPR 降至 ≈0.000（Table 2, Figure 4）。R2 指出 external matching variable 原理在 DIF 文献有先例（Clauser & Mazor 1998, Nandakumar 1993），但承认具体实现（跨学科总分 + 同时解决 LD 和 matching variable contamination）在 LLM 评测背景下是新的组合。\n\n**S3. Reframing 为 \"temporal instability\" 是认识论上的重要进步** [共识: R1+R2]\n前一版本声称检测污染但无法证明。修订版精确限定 claim 为 \"items behave differently across generations\"——这是 MH DIF 直接测量的量。Ground truth meta-critique（web-overlap enrichment ratio ≈1.0）揭示了现有 ground truth 标签的概念错位，对整个 contamination detection 领域有价值。\n\n**S4. Figure 1 和 Figure 2 质量极高** [共识: R1+R2]\nFigure 1 的 global vs differential contamination ICC 对比是向 ML 受众解释 DIF 概念的出色可视化。Figure 2 的半合成 dose-response 曲线（ΔTPR 单调递增，ΔFPR 平坦于 0）是最具说服力的验证证据。\n\n**S5. 多层次负面控制增强结果可信度** [共识: R1+R2]\nRandom split 0.18% baseline；Yen's Q3 LD 诊断；Bonferroni-Holm 校正后 31.2%（几乎不变）。三层控制排除了统计伪影解释。\n\n**S6. 诚实报告负面结果** [共识: R1+R2]\nEnsemble AUROC=0.62、item generation ρ=0.58、TOST RL robustness p=0.14（inconclusive）、ConStat Jaccard=0.08 均如实呈现。相比前一版本将弱证据包装为核心贡献，这是实质性改进。\n\n**S7. Related Work 大幅改善** [R1: strength; R2: 确认改善但指出仍有缺失]\nLalor et al. 2019、Vania et al. 2021、Balloccu et al. 2024、Growing Pains 均已涵盖。与 Growing Pains 的区分清晰（FPC assumes item stability, DIF detects violations）。R2 指出仍缺失：test security/item banking 文献、measurement invariance 完整框架、anchor selection 文献、LLM memorization 文献。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**WC1. 31.3% 发现本质上是描述性的——因果归因未解决** [共识: R1+R2]\n论文精确证明了 31.3% 的 items 在 temporal cohort 间存在 DIF，但未回答是由什么引起的：数据污染？训练数据分布迁移？模型架构演变？Ability-quintile（2.9%）排除了纯能力差异，但域分解分析显示 accuracy improvement 仅解释 ≤7.6% 的 C%——**~92% 的 DIF 来源未解释**。2024 模型的系统性变化（RLHF 强度、scale、instruction tuning）都可能产生 DIF 但与污染无关。\n\n**底线**：对 ICLR 的 contribution 标准，描述性发现需要足够 surprising 或 actionable。如果不知道原因，practitioners 不知道该如何行动。ρ≈0.997 进一步削弱了 urgency。\n\n**WC2. Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足** [R1 Major, R2 AGREE]\n61.3% 远高于 temporal（31.3%），是 Table 1 中最高 DIF 率，但论文仅一句话解释。多种解释未被区分：(a) Meta 使用 MMLU 训练（已知可能性高——若如此，这是论文最强实证证据）；(b) 能力跳跃太大导致 MH matching 失效（score range 不重叠）；(c) N=311+300 的选择偏差。这是 Table 1 中最关键但最未充分分析的发现。\n\n**WC3. GSM1K 相关性太弱，不应支撑 Claim 4** [R1 Major, R2 AGREE]\nr=-0.478, N=33, Spearman CI 上界 -0.031——CI 几乎含 0。R2 补充：N=32/33 的学科级数据易受少数 outlier 影响，相关性可能由第三变量（学科 benchmark 流行度）驱动。论文的 \"DIF as diagnostic lens\"（Claim 4）不应以此为主要支撑。\n\n### Warning（影响评分但不一票否决）\n\n**WW1. 技术新颖性受限——ICLR main track bar 的挑战** [R2 Major, R1 部分同意]\n论文诚实承认 \"empirical, not algorithmic\"。在 ICLR 标准下，核心发现——\"LLM benchmark 题目时间不稳定\"——从概念上不够意外（benchmark saturation 和 contamination 已是社区共识）。论文将已知问题量化为 31%，但 quantifying the expected 的价值有上限。R1 反驳：scaling laws 论文也无算法创新；cross-subject matching + 5 种 cohort 设计有独立方法论价值。**Director 判断**：Contribution 2/4 是两位 Reviewer 的共识评分。\n\n**WW2. ρ≈0.997 与 31.3% significance 之间的叙事张力** [共识方向: R1+R2]\n论文同时声称 (a) 31.3% items 有 significant temporal instability 和 (b) 移除后排名几乎不变。R1 提供 charitable interpretation（DIF 方向均匀分布，relative ranking 不变但 absolute scores 受影响），但也承认 \"diagnostic lens\" framing 承诺了比实际交付的更多。Figure 5 显示个别模型（flammen26-mistral-7B +542-587 位）的 rank shift 是 substantial 的，但论文未充分展开尾部分布分析。\n\n**WW3. \"Tutz & Friedman (2007)\" 引用无法核实** [R2 提出]\nTutz 在 DIF 领域的主要合作者是 Berger（2016 Psychometrika）和 Schauberger（2015），非 Friedman。虽严重性远小于 Round 1 的引用错误，仍需核查。\n\n**WW4. 补充分析过多** [共识方向: R1+R2]\n9 个补充分析中 6 个为负面/inconclusive 结果。R1: \"tried many things, most didn't work\" 的印象可能暗示 research program 尚未 mature。建议精选 2-3 个（RL robustness、IFT）放正文，其余大幅缩减。\n\n**WW5. ΔFPR=0.000 过于完美** [R1 提出]\n完美的 ΔFPR=0.000 在真实数据中不寻常，需报告 bootstrap CI。\n\n**WW6. 半合成 incorrect→correct flip 模型的边界条件未讨论** [R1 提出]\n真实 contamination 不一定表现为 \"之前错现在对\"，简化模型有合理性但需讨论什么情况下高估/低估真实 DIF。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Cross-subject matching 是论文最强的方法论贡献**——解决了 within-subject matching 的 FPR 膨胀和局部依赖问题\n2. **5 种 cohort 设计是优秀的实验控制**——ability-quintile 2.9% 和 random-split 0.18% 有力排除了混淆\n3. **Reframing 为 temporal instability 是正确的认识论选择**——消除了前一版本最大的效度疑虑\n4. **Contribution 2/4**——两位 Reviewer 独立给出相同评分\n5. **Soundness 3/4**——方法论执行扎实，多层控制设计优秀\n6. **31.3% 的因果归因是最大的开放问题**——~92% 未解释\n7. **Within-family 61.3% 是 Table 1 中最关键但最未充分分析的发现**\n8. **GSM1K 证据不足以支撑 Claim 4**\n9. **负面结果的诚实报告值得肯定**——相比 Round 1 实质性改进\n10. **论文相比前一版本有质的提升**——framing、严谨性、诚实度全面改善\n\n## Reviewer Divergence [REBUT]\n\n### 1. Overall 评分\n- **R1**: 6/10 (marginally above acceptance)\n- **R2**: 4/10 (marginally below acceptance)\n- **分歧核心**：不是事实性分歧，而是阈值判断差异。R1 更重视 solid methodology + honest reporting 的价值；R2 更重视核心发现的意外性和技术新颖性。\n- **Director 裁定**：5/10 (borderline)。论文方法论 solid（无 fatal flaw），但 contribution 偏 descriptive，practical impact 受 ρ≈0.997 限制。\n\n### 2. Related Work 覆盖\n- **R1**: Strength (S8)——pp.11-13 约 2.5 页 References\n- **R2**: 可能审阅了不同/较早版本（声称仅 10 篇引用）\n- **Director 裁定**：以修订版为准。R1 确认 Related Work 覆盖全面。R2 指出的次要缺失（item banking、measurement invariance、anchor selection、memorization）为合理补充建议。\n\n### 3. FDR 校正\n- **R1**: Major weakness\n- **R2**: REBUT——论文已有 BH 校正（31.2% vs 31.3%），ETS-C 基于 effect size 不依赖 p-value，random split 0.6% 排除伪影\n- **Director 裁定**：同意 R2。FDR 不构成 validity threat。已在 Round 2 Issue Tracker 中标记为 resolved。\n\n---\n\n## Questions for Authors\n\n1. **[最高优先]** 31.3% temporal DIF 中，能否提供证据（即使间接的）分离 \"污染驱动的 DIF\" 和 \"合法能力演变驱动的 DIF\"？例如：对已知未被污染的题目子集，temporal DIF rate 是多少？\n2. **[最高优先]** Llama 2 vs 3 的 61.3%：(a) 两者的 score 分布重叠程度如何？(b) 其他 family 对比（Phi-2/3, Qwen 1/2）是否 consistent？(c) 如果与 Meta 已知的训练数据 composition 一致，这应被强调为最强实证证据。\n3. **[高优先]** 31.3% significance 与 ρ≈0.997 robustness 如何 reconcile？Model-specific rank shifts 的完整分布（中位数、95th percentile）是什么？DIF flags 的具体 actionable use case 是什么？\n4. **[高优先]** ΔFPR=0.000 基于多少次 random seed/injection 的平均值？请提供 bootstrap CI。\n5. DIF-flagged items 是否集中在特定 difficulty range？（floor/ceiling artifact 的可能性）\n6. Yen's Q3 LD 最高的 subject domains 是否也是 DIF 率最高的 domains？\n7. Ensemble AUROC 从 0.72 降至 0.62 的原因是什么？数据/方法变化还是 bug 修正？\n8. \"Tutz & Friedman (2007)\" 的完整引用信息？\n9. 是否考虑 NeurIPS D&B track 作为替代 venue？\n\n---\n\n## Missing References\n\nRound 2 仍缺失的引用（R2 识别）：\n1. **Test security / item banking**：Stocking & Swanson (1993), van der Linden & Veldkamp (2004)——直接关联 \"如何管理不稳定题目\"\n2. **Measurement invariance 完整框架**：DIF 与 factorial invariance (configural→metric→scalar) 的关系——DIF 是 scalar invariance 的 item-level 版本\n3. **Anchor item selection**：Kopf et al. (2015), Wang et al. (2012)——更系统的 anchor selection 方法\n4. **LLM memorization 机制**：Carlini et al. (2022), Tirumala et al. (2022)——与 \"global exposure vs differential functioning\" 区分直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。**\n\n---\n\n## Visual Layout Check\n\n**状态：未启动。**\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|---------------|\n| Soundness | 3/4 | 3/4 | **3/4** |\n| Presentation | 3/4 | 3/4 | **3/4** |\n| Contribution | 2/4 | 2/4 | **2/4** |\n| **Overall** | **6/10** | **4/10** | **5/10 (Borderline)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 总体判断：**Borderline** (5/10)\n\n**核心判断**：修订版论文在方法论严谨性、学术诚实度和 framing 准确性上相比前一版本有质的提升。5 种 cohort 设计是教科书级别的实验控制，cross-subject matching 是有独立价值的方法论贡献，从 \"contamination detection\" 到 \"temporal instability\" 的 reframing 是正确的认识论选择。两位 Reviewer 均未发现 fatal methodological flaw。\n\n**但核心瓶颈在 contribution 和 impact**：\n1. **31.3% 是描述性发现**——informative 但不够 actionable。~92% 的 DIF 来源未解释，practitioners 不知道拿到 DIF flags 后该做什么。\n2. **ρ≈0.997 削弱 urgency**——如果移除 31% 的不稳定题目后排名几乎不变，检测它们的实际价值有限。\n3. **技术新颖性受限**——论文诚实承认 \"empirical, not algorithmic\"，但 ICLR main track 对纯实证贡献的意外性和影响力要求更高。核心发现（benchmark 题目时间不稳定）不够意外。\n4. **Within-family 61.3% 是最未充分利用的数据点**——如果深入分析可能成为最强的实证证据。\n\n**与 Round 1 对比**：Round 1 的问题是 overclaiming（强声明 + 弱证据），修订版的问题是 under-impact（诚实声明 + 有限影响力）。从学术严谨性角度，修订版明确更好；从 ICLR acceptance 角度，两版各有软肋。\n\n### Rebuttal 关键门槛\n\n**必须回应**（决定 accept/reject）：\n1. **因果分离**：任何能区分 \"污染 DIF\" vs \"paradigm shift DIF\" 的证据——即使间接的（如 case study、within-family 与 training data 关联分析）\n2. **61.3% 深入分析**：Llama 2/3 score 分布重叠、其他 family 对比\n3. **ρ≈0.997 的 reconciliation**：model-specific rank shifts 完整分布 + DIF 的具体 actionable use case\n\n**应该回应**（影响评分）：\n4. ΔFPR=0.000 的 bootstrap CI\n5. DIF items 的 difficulty distribution（排除 floor/ceiling artifact）\n6. \"Tutz & Friedman (2007)\" 核查\n\n**如果 rebuttal 能提供**：(a) Llama 2/3 分析确认 contamination-driven DIF、(b) model-specific rank shifts 展示 DIF 诊断的具体实用价值、(c) 2-3 个 case study 展示 DIF-flagged items 的可操作洞察——有路径上调至 **6/10 (Marginally Accept)**。\n\n**R2 建议**：考虑 NeurIPS Datasets & Benchmarks track——论文的 \"empirical, not algorithmic\" 定位可能更匹配该 track 的评审标准。\n\n---\n\n## Detailed Comments\n\n### §1-2 Introduction & Related Work\n- Reframing 为 temporal instability 是正确选择。Figure 1 的教学价值极高。\n- Related Work 大幅改善（Lalor, Vania, Balloccu, Growing Pains 均已涵盖）。\n- 仍缺失：item banking 文献、measurement invariance 完整框架、LLM memorization 机制。\n- \"Tutz & Friedman (2007)\" 需核查。\n\n### §3 Method\n- Cross-subject matching（§3.4）是论文最强的方法论贡献。\n- Semi-synthetic injection（§3.4）的 incorrect→correct flip 模型合理但边界条件未讨论。\n- MH 仍是唯一 DIF 方法——LR-DIF/SIBTEST 对比仍是有价值的补充。\n\n### §4 Results\n- 5 种 cohort 设计优秀（Table 1）。Random-split 0.18% 是最坚实的 null baseline。\n- **Within-family 61.3% 是 Table 1 中最关键但最未充分分析的发现**——应深入展开。\n- Yen's Q3 (11.3%) 和 Bonferroni-Holm (31.2%) 增强了结果可信度。\n- θ-conditioning（FPR=0.312）和 within-subject（C%=30.15%）的 converging analyses 强化了 \"31% 信号是 robust 的\" 结论。\n- **但 ~92% 的 DIF 来源仍未解释**——accuracy improvement 仅解释 ≤7.6%。\n\n### §5 Discussion\n- \"Instability ≠ Invalidity\" 框架有洞察力，但需要更有力地论证 DIF 诊断的具体 actionable value。\n- ρ≈0.997 应聚焦尾部模型的大位移（Figure 5），而非强调整体不变性。\n- GSM1K（r=-0.478, N=33）不应作为 Claim 4 主要支撑——应降级为 suggestive evidence。\n- \"Diagnostic lens\" framing 承诺超出论文实际交付——需 reconcile 与 ρ≈0.997。\n\n### 补充分析\n- 9 个分析中建议保留 3 个正文引用（RL robustness、IFT、bifactor pilot），其余大幅缩减或移至 appendix。\n- 负面结果的诚实报告值得肯定，但过多补充分析可能给人 research program 未 mature 的印象。\n",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
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
    "report": "\n# 圆桌审稿报告 — Round 2（修订版论文）\n\n**论文**: \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n**Venue**: ICLR 2026（评分量表 {0, 2, 4, 6, 8, 10}）\n**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）\n**日期**: 2026-05-21\n**轮次**: Round 2（修订版论文初审 + 交叉回应，1 轮收敛）\n\n---\n\n## 与 Round 1 论文的关键变化\n\n修订版论文相对于 Round 1 审稿的版本有**质的提升**：\n\n| 方面 | Round 1 版本 | 修订版 |\n|------|-------------|--------|\n| 标题/定位 | \"Psychometric Detection and Regeneration\" | \"Psychometric Instability\"——从污染检测转为时间不稳定性 |\n| 贡献声明 | 5 条，部分 overclaiming | 4 条实证发现，明确声明 \"empirical, not algorithmic\" |\n| 引用 | 严重错误（Tets/Iron-Fenced Trees） | 错误已修复，Related Work 大幅扩充 |\n| 验证 | 半合成 + κ=0.14（失败） | Cross-subject matching + dose-response + GSM8K replication |\n| RL robustness | N=13 作为核心贡献 | TOST inconclusive，降级为补充分析 |\n| 方法论 | 普通 2PL + MH | 增加 Yen's Q3、5 种 cohort 设计、Bonferroni-Holm |\n| Regeneration | ρ=0.91（equating pipeline） | ρ=0.58（负面结果，诚实报告） |\n\n**Round 1 的 4 个 Critical Issues 回应情况**：\n- **WC1 效度验证**：重新框定为 temporal instability（非 contamination），消除了 κ=0.14 作为否定证据的问题。但因果归因仍未解决。→ **部分解决**\n- **WC2 RL 样本量**：降级为补充分析，TOST 诚实报告为 inconclusive。→ **缓解（不再是核心贡献）**\n- **WC3 半合成循环性**：引入 cross-subject matching 框架（ΔFPR≈0.000）。→ **大幅改善**\n- **WC4 局部独立性**：增加 Yen's Q3 诊断（11.3%），cross-subject matching 处理 LD。→ **大幅改善**\n\n---\n\n## Summary\n\n本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 2023-2024 模型代际间表现出显著差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计（temporal/ability-quintile/within-family/within-subject/random-split）系统排除混淆变量，提出 cross-subject matching 半合成验证框架，并论证 DIF 应作为诊断工具而非质量过滤器（ρ≈0.997）。论文明确声明 \"贡献是实证的，不是算法的\"。\n\n---\n\n## Strengths\n\n**S1. 5 种 Cohort 设计构成教科书级控制实验** [共识: R1+R2]\nTable 1 中 temporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）的对比极其有力。Ability-quintile 2.9% 证明纯能力差异不足以解释 temporal DIF；random-split 0.18% 确认信号非随机噪音。两位 Reviewer 均给予高度评价。\n\n**S2. Cross-subject matching 是真正的方法论贡献** [共识: R1+R2]\nWithin-subject matching 导致 FPR 膨胀 +0.196，cross-subject matching 将 ΔFPR 降至 ≈0.000（Table 2, Figure 4）。R2 指出 external matching variable 原理在 DIF 文献有先例（Clauser & Mazor 1998, Nandakumar 1993），但承认具体实现（跨学科总分 + 同时解决 LD 和 matching variable contamination）在 LLM 评测背景下是新的组合。\n\n**S3. Reframing 为 \"temporal instability\" 是认识论上的重要进步** [共识: R1+R2]\n前一版本声称检测污染但无法证明。修订版精确限定 claim 为 \"items behave differently across generations\"——这是 MH DIF 直接测量的量。Ground truth meta-critique（web-overlap enrichment ratio ≈1.0）揭示了现有 ground truth 标签的概念错位，对整个 contamination detection 领域有价值。\n\n**S4. Figure 1 和 Figure 2 质量极高** [共识: R1+R2]\nFigure 1 的 global vs differential contamination ICC 对比是向 ML 受众解释 DIF 概念的出色可视化。Figure 2 的半合成 dose-response 曲线（ΔTPR 单调递增，ΔFPR 平坦于 0）是最具说服力的验证证据。\n\n**S5. 多层次负面控制增强结果可信度** [共识: R1+R2]\nRandom split 0.18% baseline；Yen's Q3 LD 诊断；Bonferroni-Holm 校正后 31.2%（几乎不变）。三层控制排除了统计伪影解释。\n\n**S6. 诚实报告负面结果** [共识: R1+R2]\nEnsemble AUROC=0.62、item generation ρ=0.58、TOST RL robustness p=0.14（inconclusive）、ConStat Jaccard=0.08 均如实呈现。相比前一版本将弱证据包装为核心贡献，这是实质性改进。\n\n**S7. Related Work 大幅改善** [R1: strength; R2: 确认改善但指出仍有缺失]\nLalor et al. 2019、Vania et al. 2021、Balloccu et al. 2024、Growing Pains 均已涵盖。与 Growing Pains 的区分清晰（FPC assumes item stability, DIF detects violations）。R2 指出仍缺失：test security/item banking 文献、measurement invariance 完整框架、anchor selection 文献、LLM memorization 文献。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**WC1. 31.3% 发现本质上是描述性的——因果归因未解决** [共识: R1+R2]\n论文精确证明了 31.3% 的 items 在 temporal cohort 间存在 DIF，但未回答是由什么引起的：数据污染？训练数据分布迁移？模型架构演变？Ability-quintile（2.9%）排除了纯能力差异，但域分解分析显示 accuracy improvement 仅解释 ≤7.6% 的 C%——**~92% 的 DIF 来源未解释**。2024 模型的系统性变化（RLHF 强度、scale、instruction tuning）都可能产生 DIF 但与污染无关。\n\n**底线**：对 ICLR 的 contribution 标准，描述性发现需要足够 surprising 或 actionable。如果不知道原因，practitioners 不知道该如何行动。ρ≈0.997 进一步削弱了 urgency。\n\n**WC2. Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足** [R1 Major, R2 AGREE]\n61.3% 远高于 temporal（31.3%），是 Table 1 中最高 DIF 率，但论文仅一句话解释。多种解释未被区分：(a) Meta 使用 MMLU 训练（已知可能性高——若如此，这是论文最强实证证据）；(b) 能力跳跃太大导致 MH matching 失效（score range 不重叠）；(c) N=311+300 的选择偏差。这是 Table 1 中最关键但最未充分分析的发现。\n\n**WC3. GSM1K 相关性太弱，不应支撑 Claim 4** [R1 Major, R2 AGREE]\nr=-0.478, N=33, Spearman CI 上界 -0.031——CI 几乎含 0。R2 补充：N=32/33 的学科级数据易受少数 outlier 影响，相关性可能由第三变量（学科 benchmark 流行度）驱动。论文的 \"DIF as diagnostic lens\"（Claim 4）不应以此为主要支撑。\n\n### Warning（影响评分但不一票否决）\n\n**WW1. 技术新颖性受限——ICLR main track bar 的挑战** [R2 Major, R1 部分同意]\n论文诚实承认 \"empirical, not algorithmic\"。在 ICLR 标准下，核心发现——\"LLM benchmark 题目时间不稳定\"——从概念上不够意外（benchmark saturation 和 contamination 已是社区共识）。论文将已知问题量化为 31%，但 quantifying the expected 的价值有上限。R1 反驳：scaling laws 论文也无算法创新；cross-subject matching + 5 种 cohort 设计有独立方法论价值。**Director 判断**：Contribution 2/4 是两位 Reviewer 的共识评分。\n\n**WW2. ρ≈0.997 与 31.3% significance 之间的叙事张力** [共识方向: R1+R2]\n论文同时声称 (a) 31.3% items 有 significant temporal instability 和 (b) 移除后排名几乎不变。R1 提供 charitable interpretation（DIF 方向均匀分布，relative ranking 不变但 absolute scores 受影响），但也承认 \"diagnostic lens\" framing 承诺了比实际交付的更多。Figure 5 显示个别模型（flammen26-mistral-7B +542-587 位）的 rank shift 是 substantial 的，但论文未充分展开尾部分布分析。\n\n**WW3. \"Tutz & Friedman (2007)\" 引用无法核实** [R2 提出]\nTutz 在 DIF 领域的主要合作者是 Berger（2016 Psychometrika）和 Schauberger（2015），非 Friedman。虽严重性远小于 Round 1 的引用错误，仍需核查。\n\n**WW4. 补充分析过多** [共识方向: R1+R2]\n9 个补充分析中 6 个为负面/inconclusive 结果。R1: \"tried many things, most didn't work\" 的印象可能暗示 research program 尚未 mature。建议精选 2-3 个（RL robustness、IFT）放正文，其余大幅缩减。\n\n**WW5. ΔFPR=0.000 过于完美** [R1 提出]\n完美的 ΔFPR=0.000 在真实数据中不寻常，需报告 bootstrap CI。\n\n**WW6. 半合成 incorrect→correct flip 模型的边界条件未讨论** [R1 提出]\n真实 contamination 不一定表现为 \"之前错现在对\"，简化模型有合理性但需讨论什么情况下高估/低估真实 DIF。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Cross-subject matching 是论文最强的方法论贡献**——解决了 within-subject matching 的 FPR 膨胀和局部依赖问题\n2. **5 种 cohort 设计是优秀的实验控制**——ability-quintile 2.9% 和 random-split 0.18% 有力排除了混淆\n3. **Reframing 为 temporal instability 是正确的认识论选择**——消除了前一版本最大的效度疑虑\n4. **Contribution 2/4**——两位 Reviewer 独立给出相同评分\n5. **Soundness 3/4**——方法论执行扎实，多层控制设计优秀\n6. **31.3% 的因果归因是最大的开放问题**——~92% 未解释\n7. **Within-family 61.3% 是 Table 1 中最关键但最未充分分析的发现**\n8. **GSM1K 证据不足以支撑 Claim 4**\n9. **负面结果的诚实报告值得肯定**——相比 Round 1 实质性改进\n10. **论文相比前一版本有质的提升**——framing、严谨性、诚实度全面改善\n\n## Reviewer Divergence [REBUT]\n\n### 1. Overall 评分\n- **R1**: 6/10 (marginally above acceptance)\n- **R2**: 4/10 (marginally below acceptance)\n- **分歧核心**：不是事实性分歧，而是阈值判断差异。R1 更重视 solid methodology + honest reporting 的价值；R2 更重视核心发现的意外性和技术新颖性。\n- **Director 裁定**：5/10 (borderline)。论文方法论 solid（无 fatal flaw），但 contribution 偏 descriptive，practical impact 受 ρ≈0.997 限制。\n\n### 2. Related Work 覆盖\n- **R1**: Strength (S8)——pp.11-13 约 2.5 页 References\n- **R2**: 可能审阅了不同/较早版本（声称仅 10 篇引用）\n- **Director 裁定**：以修订版为准。R1 确认 Related Work 覆盖全面。R2 指出的次要缺失（item banking、measurement invariance、anchor selection、memorization）为合理补充建议。\n\n### 3. FDR 校正\n- **R1**: Major weakness\n- **R2**: REBUT——论文已有 BH 校正（31.2% vs 31.3%），ETS-C 基于 effect size 不依赖 p-value，random split 0.6% 排除伪影\n- **Director 裁定**：同意 R2。FDR 不构成 validity threat。已在 Round 2 Issue Tracker 中标记为 resolved。\n\n---\n\n## Questions for Authors\n\n1. **[最高优先]** 31.3% temporal DIF 中，能否提供证据（即使间接的）分离 \"污染驱动的 DIF\" 和 \"合法能力演变驱动的 DIF\"？例如：对已知未被污染的题目子集，temporal DIF rate 是多少？\n2. **[最高优先]** Llama 2 vs 3 的 61.3%：(a) 两者的 score 分布重叠程度如何？(b) 其他 family 对比（Phi-2/3, Qwen 1/2）是否 consistent？(c) 如果与 Meta 已知的训练数据 composition 一致，这应被强调为最强实证证据。\n3. **[高优先]** 31.3% significance 与 ρ≈0.997 robustness 如何 reconcile？Model-specific rank shifts 的完整分布（中位数、95th percentile）是什么？DIF flags 的具体 actionable use case 是什么？\n4. **[高优先]** ΔFPR=0.000 基于多少次 random seed/injection 的平均值？请提供 bootstrap CI。\n5. DIF-flagged items 是否集中在特定 difficulty range？（floor/ceiling artifact 的可能性）\n6. Yen's Q3 LD 最高的 subject domains 是否也是 DIF 率最高的 domains？\n7. Ensemble AUROC 从 0.72 降至 0.62 的原因是什么？数据/方法变化还是 bug 修正？\n8. \"Tutz & Friedman (2007)\" 的完整引用信息？\n9. 是否考虑 NeurIPS D&B track 作为替代 venue？\n\n---\n\n## Missing References\n\nRound 2 仍缺失的引用（R2 识别）：\n1. **Test security / item banking**：Stocking & Swanson (1993), van der Linden & Veldkamp (2004)——直接关联 \"如何管理不稳定题目\"\n2. **Measurement invariance 完整框架**：DIF 与 factorial invariance (configural→metric→scalar) 的关系——DIF 是 scalar invariance 的 item-level 版本\n3. **Anchor item selection**：Kopf et al. (2015), Wang et al. (2012)——更系统的 anchor selection 方法\n4. **LLM memorization 机制**：Carlini et al. (2022), Tirumala et al. (2022)——与 \"global exposure vs differential functioning\" 区分直接相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。**\n\n---\n\n## Visual Layout Check\n\n**状态：未启动。**\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|---------------|\n| Soundness | 3/4 | 3/4 | **3/4** |\n| Presentation | 3/4 | 3/4 | **3/4** |\n| Contribution | 2/4 | 2/4 | **2/4** |\n| **Overall** | **6/10** | **4/10** | **5/10 (Borderline)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 总体判断：**Borderline** (5/10)\n\n**核心判断**：修订版论文在方法论严谨性、学术诚实度和 framing 准确性上相比前一版本有质的提升。5 种 cohort 设计是教科书级别的实验控制，cross-subject matching 是有独立价值的方法论贡献，从 \"contamination detection\" 到 \"temporal instability\" 的 reframing 是正确的认识论选择。两位 Reviewer 均未发现 fatal methodological flaw。\n\n**但核心瓶颈在 contribution 和 impact**：\n1. **31.3% 是描述性发现**——informative 但不够 actionable。~92% 的 DIF 来源未解释，practitioners 不知道拿到 DIF flags 后该做什么。\n2. **ρ≈0.997 削弱 urgency**——如果移除 31% 的不稳定题目后排名几乎不变，检测它们的实际价值有限。\n3. **技术新颖性受限**——论文诚实承认 \"empirical, not algorithmic\"，但 ICLR main track 对纯实证贡献的意外性和影响力要求更高。核心发现（benchmark 题目时间不稳定）不够意外。\n4. **Within-family 61.3% 是最未充分利用的数据点**——如果深入分析可能成为最强的实证证据。\n\n**与 Round 1 对比**：Round 1 的问题是 overclaiming（强声明 + 弱证据），修订版的问题是 under-impact（诚实声明 + 有限影响力）。从学术严谨性角度，修订版明确更好；从 ICLR acceptance 角度，两版各有软肋。\n\n### Rebuttal 关键门槛\n\n**必须回应**（决定 accept/reject）：\n1. **因果分离**：任何能区分 \"污染 DIF\" vs \"paradigm shift DIF\" 的证据——即使间接的（如 case study、within-family 与 training data 关联分析）\n2. **61.3% 深入分析**：Llama 2/3 score 分布重叠、其他 family 对比\n3. **ρ≈0.997 的 reconciliation**：model-specific rank shifts 完整分布 + DIF 的具体 actionable use case\n\n**应该回应**（影响评分）：\n4. ΔFPR=0.000 的 bootstrap CI\n5. DIF items 的 difficulty distribution（排除 floor/ceiling artifact）\n6. \"Tutz & Friedman (2007)\" 核查\n\n**如果 rebuttal 能提供**：(a) Llama 2/3 分析确认 contamination-driven DIF、(b) model-specific rank shifts 展示 DIF 诊断的具体实用价值、(c) 2-3 个 case study 展示 DIF-flagged items 的可操作洞察——有路径上调至 **6/10 (Marginally Accept)**。\n\n**R2 建议**：考虑 NeurIPS Datasets & Benchmarks track——论文的 \"empirical, not algorithmic\" 定位可能更匹配该 track 的评审标准。\n\n---\n\n## Detailed Comments\n\n### §1-2 Introduction & Related Work\n- Reframing 为 temporal instability 是正确选择。Figure 1 的教学价值极高。\n- Related Work 大幅改善（Lalor, Vania, Balloccu, Growing Pains 均已涵盖）。\n- 仍缺失：item banking 文献、measurement invariance 完整框架、LLM memorization 机制。\n- \"Tutz & Friedman (2007)\" 需核查。\n\n### §3 Method\n- Cross-subject matching（§3.4）是论文最强的方法论贡献。\n- Semi-synthetic injection（§3.4）的 incorrect→correct flip 模型合理但边界条件未讨论。\n- MH 仍是唯一 DIF 方法——LR-DIF/SIBTEST 对比仍是有价值的补充。\n\n### §4 Results\n- 5 种 cohort 设计优秀（Table 1）。Random-split 0.18% 是最坚实的 null baseline。\n- **Within-family 61.3% 是 Table 1 中最关键但最未充分分析的发现**——应深入展开。\n- Yen's Q3 (11.3%) 和 Bonferroni-Holm (31.2%) 增强了结果可信度。\n- θ-conditioning（FPR=0.312）和 within-subject（C%=30.15%）的 converging analyses 强化了 \"31% 信号是 robust 的\" 结论。\n- **但 ~92% 的 DIF 来源仍未解释**——accuracy improvement 仅解释 ≤7.6%。\n\n### §5 Discussion\n- \"Instability ≠ Invalidity\" 框架有洞察力，但需要更有力地论证 DIF 诊断的具体 actionable value。\n- ρ≈0.997 应聚焦尾部模型的大位移（Figure 5），而非强调整体不变性。\n- GSM1K（r=-0.478, N=33）不应作为 Claim 4 主要支撑——应降级为 suggestive evidence。\n- \"Diagnostic lens\" framing 承诺超出论文实际交付——需 reconcile 与 ρ≈0.997。\n\n### 补充分析\n- 9 个分析中建议保留 3 个正文引用（RL robustness、IFT、bifactor pilot），其余大幅缩减或移至 appendix。\n- 负面结果的诚实报告值得肯定，但过多补充分析可能给人 research program 未 mature 的印象。\n",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-21T07:15:24.496557+00:00_

{"result":"{\"success\": false, \"data\": {\"existing_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_0.md\", \"round\": 0}, \"error\": \"Round 0 report ALREADY submitted (persisted at `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_0.md`). Research Director was triggered once and may still be processing it; re-submitting silently would trigger the protocol again with conflicting content.\\n\\nExisting report frontmatter (first 400 chars):\\n---\\nround: 0\\nreview_mode: \\noverall_score: borderline\\ntimestamp: 2026-05-20T21:51:43.210272+00:00\\nreviewer_ids: [1, 2]\\ncross_response_reviewer_ids: [1, 2]\\nforce_resubmit: False\\n---\\n\\n\\n# 圆桌审稿报告 — Round 1\\n\\n**论文**: \\\"Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items: DIF-Based Detection, Multi-Signal Ensemble, and IRT-Equated Benchmark Regeneration\\\"\\n\\n**审稿组**: R1（Methods & Exper\\n\\nIf you intentionally want to replace it (e.g. caught a Step 2 cross-sharing gap and synthesized a corrected report), call again with force_resubmit=True. Otherwise the original submission stands — pause and verify before forcing.\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-21T07:16:50.741378+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# 圆桌审稿报告 — Round 2（修订版论文）\n\n**论文**: \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n**Venue**: ICLR 2026（评分量表 {0, 2, 4, 6, 8, 10}）\n**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）\n**日期**: 2026-05-21\n**轮次**: Round 2（修订版论文初审 + 交叉回应，1 轮收敛）\n\n**注意**：本报告替代 Round 0 报告。Round 0 是对原版论文（\"Detection and Regeneration\"）的审稿；本报告是对作者大幅修订后的新版论文（\"Psychometric Instability\"）的审稿。标题、定位、贡献声明、内容结构均有本质性变化。\n\n---\n\n## 与 Round 1 论文的关键变化\n\n修订版论文相对于 Round 1 审稿的版本有**质的提升**：\n\n| 方面 | Round 1 版本 | 修订版 |\n|------|-------------|--------|\n| 标题/定位 | \"Psychometric Detection and Regeneration\" | \"Psychometric Instability\"——从污染检测转为时间不稳定性 |\n| 贡献声明 | 5 条，部分 overclaiming | 4 条实证发现，明确声明 \"empirical, not algorithmic\" |\n| 引用 | 严重错误（Tets/Iron-Fenced Trees） | 错误已修复，Related Work 大幅扩充 |\n| 验证 | 半合成 + κ=0.14（失败） | Cross-subject matching + dose-response + GSM8K replication |\n| RL robustness | N=13 作为核心贡献 | TOST inconclusive，降级为补充分析 |\n| 方法论 | 普通 2PL + MH | 增加 Yen's Q3、5 种 cohort 设计、Bonferroni-Holm |\n| Regeneration | ρ=0.91（equating pipeline） | ρ=0.58（负面结果，诚实报告） |\n\n**Round 1 的 4 个 Critical Issues 回应情况**：\n- **WC1 效度验证**：重新框定为 temporal instability（非 contamination），消除 κ=0.14 作为否定证据的问题。但因果归因仍未解决。→ **部分解决**\n- **WC2 RL 样本量**：降级为补充分析，TOST 诚实报告为 inconclusive。→ **缓解（不再是核心贡献）**\n- **WC3 半合成循环性**：引入 cross-subject matching 框架（ΔFPR≈0.000）。→ **大幅改善**\n- **WC4 局部独立性**：增加 Yen's Q3 诊断（11.3%），cross-subject matching 处理 LD。→ **大幅改善**\n\n---\n\n## Summary\n\n本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 2023-2024 模型代际间表现出显著差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计（temporal/ability-quintile/within-family/within-subject/random-split）系统排除混淆变量，提出 cross-subject matching 半合成验证框架，并论证 DIF 应作为诊断工具而非质量过滤器（ρ≈0.997）。论文明确声明 \"贡献是实证的，不是算法的\"。\n\n---\n\n## Strengths\n\n**S1. 5 种 Cohort 设计构成教科书级控制实验** [共识: R1+R2]\nTable 1 中 temporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）的对比极其有力。Ability-quintile 2.9% 证明纯能力差异不足以解释 temporal DIF；random-split 0.18% 确认信号非随机噪音。\n\n**S2. Cross-subject matching 是真正的方法论贡献** [共识: R1+R2]\nWithin-subject matching 导致 FPR 膨胀 +0.196，cross-subject matching 将 ΔFPR 降至 ≈0.000（Table 2, Figure 4）。R2 指出 external matching variable 原理在 DIF 文献有先例（Clauser & Mazor 1998, Nandakumar 1993），但承认具体实现（跨学科总分 + 同时解决 LD 和 matching variable contamination）在 LLM 评测背景下是新的组合。\n\n**S3. Reframing 为 \"temporal instability\" 是认识论上的重要进步** [共识: R1+R2]\n前一版本声称检测污染但无法证明。修订版精确限定 claim 为 \"items behave differently across generations\"——这是 MH DIF 直接测量的量。Ground truth meta-critique（web-overlap enrichment ratio ≈1.0）揭示了现有 ground truth 标签的概念错位，对整个 contamination detection 领域有价值。\n\n**S4. Figure 1 和 Figure 2 质量极高** [共识: R1+R2]\nFigure 1 的 global vs differential contamination ICC 对比是向 ML 受众解释 DIF 概念的出色可视化。Figure 2 的 dose-response 曲线是最具说服力的验证证据。\n\n**S5. 多层次负面控制增强结果可信度** [共识: R1+R2]\nRandom split 0.18%；Yen's Q3 LD 诊断；Bonferroni-Holm 校正后 31.2%。三层控制排除了统计伪影解释。\n\n**S6. 诚实报告负面结果** [共识: R1+R2]\nEnsemble AUROC=0.62、item generation ρ=0.58、TOST RL robustness p=0.14（inconclusive）均如实呈现。\n\n**S7. Related Work 大幅改善** [R1 确认]\nLalor et al. 2019、Vania et al. 2021、Balloccu et al. 2024、Growing Pains 均已涵盖。与 Growing Pains 的区分清晰。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**WC1. 31.3% 发现本质上是描述性的——因果归因未解决** [共识: R1+R2]\n论文精确证明了 31.3% 的 items 有 temporal DIF，但未回答成因。Accuracy improvement 仅解释 ≤7.6% 的 C%——**~92% 的 DIF 来源未解释**。2024 模型的系统性变化（RLHF 强度、scale、instruction tuning）都可能产生 DIF 但与污染无关。描述性发现需要足够 surprising 或 actionable 才能达到 ICLR 门槛——如果不知道原因，practitioners 不知道该如何行动。\n\n**WC2. Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足** [共识: R1 Major + R2 AGREE]\n61.3% 远高于 temporal 31.3%，是 Table 1 最高值，但论文仅一句话解释。如果是 Meta 使用 MMLU 训练，这是最强实证证据；如果是能力跳跃导致 MH matching 失效，这是方法论 limitation。论文不区分。\n\n**WC3. GSM1K 相关性太弱，不应支撑 Claim 4** [共识: R1 Major + R2 AGREE]\nr=-0.478, N=33, CI 上界 -0.031 几乎含 0。\"DIF as diagnostic lens\" 不应以此为主要支撑。\n\n### Warning（影响评分但不一票否决）\n\n**WW1. 技术新颖性受限** [R2 Major, R1 部分同意]\n\"empirical, not algorithmic\" 定位在 ICLR 标准下，核心发现的意外性有限。Contribution 2/4 是 R1+R2 共识。\n\n**WW2. ρ≈0.997 与 31.3% 之间的叙事张力** [共识方向]\n\"Diagnostic lens\" framing 承诺超出论文交付。Figure 5 的 model-specific shifts 部分回应但未充分展开。\n\n**WW3. \"Tutz & Friedman (2007)\" 无法核实** [R2]\n\n**WW4. 补充分析过多** [共识方向]\n9 个中 6 个负面/inconclusive，建议精选 2-3 个。\n\n**WW5. ΔFPR=0.000 过于完美** [R1]\n需 bootstrap CI。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. Cross-subject matching 是论文最强方法论贡献\n2. 5 种 cohort 设计是优秀的实验控制\n3. Reframing 为 temporal instability 是正确选择\n4. Contribution 2/4（共识评分）\n5. Soundness 3/4（共识评分）\n6. 31.3% 因果归因是最大开放问题（~92% 未解释）\n7. Within-family 61.3% 是最关键但最未充分分析的发现\n8. GSM1K 证据不足支撑 Claim 4\n9. 负面结果诚实报告值得肯定\n10. 相比前一版本有质的提升\n\n## Reviewer Divergence [REBUT]\n\n### 1. Overall 评分\n- **R1**: 6/10 (marginally above) | **R2**: 4/10 (marginally below)\n- **分歧核心**：阈值判断差异（非事实性分歧）。R1 重视 methodology + honesty；R2 重视 novelty + surprise。\n- **Director 裁定**：5/10 (borderline)\n\n### 2. FDR 校正严重性\n- **R1**: Major weakness | **R2**: REBUT（论文已有 BH 校正，ETS-C 基于 effect size）\n- **Director 裁定**：同意 R2，不构成 validity threat\n\n---\n\n## Questions for Authors\n\n1. **[最高优先]** 31.3% 中能否分离 \"污染 DIF\" vs \"能力演变 DIF\"？\n2. **[最高优先]** Llama 2 vs 3 的 61.3%：score 分布重叠？其他 family 对比？与 Meta training data 的关联？\n3. **[高优先]** ρ≈0.997 下 model-specific rank shifts 的完整分布？DIF flags 的 actionable use case？\n4. **[高优先]** ΔFPR=0.000 的 bootstrap CI？\n5. DIF-flagged items 是否集中在特定 difficulty range？\n6. LD 最高的 subject domains 是否也是 DIF 率最高的？\n7. Ensemble AUROC 0.62 vs 前一版本 0.72 的原因？\n8. \"Tutz & Friedman (2007)\" 完整引用信息？\n9. 是否考虑 NeurIPS D&B track？\n\n---\n\n## Missing References\n\n1. Test security / item banking（Stocking & Swanson 1993, van der Linden & Veldkamp 2004）\n2. Measurement invariance 完整框架（configural→metric→scalar 与 DIF 的关系）\n3. Anchor item selection（Kopf et al. 2015, Wang et al. 2012）\n4. LLM memorization（Carlini et al. 2022, Tirumala et al. 2022）\n\n---\n\n## External Review: 未请求\n\n## Visual Layout Check: 未启动\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|---------------|\n| Soundness | 3/4 | 3/4 | **3/4** |\n| Presentation | 3/4 | 3/4 | **3/4** |\n| Contribution | 2/4 | 2/4 | **2/4** |\n| **Overall** | **6/10** | **4/10** | **5/10 (Borderline)** |\n\n### 总体判断：**Borderline** (5/10)\n\n修订版在方法论严谨性、学术诚实度和 framing 上有质的提升。5 种 cohort 设计和 cross-subject matching 有独立方法论价值。无 fatal methodological flaw。\n\n但核心瓶颈在 contribution 和 impact：31.3% 是描述性发现（~92% 未解释），ρ≈0.997 削弱 urgency，技术新颖性受限。Round 1 的问题是 overclaiming，修订版的问题是 under-impact。\n\n### Rebuttal 关键门槛\n\n**必须回应**：(1) 因果分离证据；(2) 61.3% 深入分析；(3) ρ≈0.997 reconciliation + actionable use case\n\n**上调至 6/10 的路径**：(a) Llama 2/3 分析确认 contamination-driven DIF；(b) model-specific rank shifts 展示诊断实用价值；(c) 2-3 个 case study 展示 DIF-flagged items 的可操作洞察\n\n**R2 建议**：考虑 NeurIPS Datasets & Benchmarks track——\"empirical, not algorithmic\" 定位可能更匹配。\n",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "force_resubmit": "True"
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
    "report": "\n# 圆桌审稿报告 — Round 2（修订版论文）\n\n**论文**: \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n**Venue**: ICLR 2026（评分量表 {0, 2, 4, 6, 8, 10}）\n**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）\n**日期**: 2026-05-21\n**轮次**: Round 2（修订版论文初审 + 交叉回应，1 轮收敛）\n\n**注意**：本报告替代 Round 0 报告。Round 0 是对原版论文（\"Detection and Regeneration\"）的审稿；本报告是对作者大幅修订后的新版论文（\"Psychometric Instability\"）的审稿。标题、定位、贡献声明、内容结构均有本质性变化。\n\n---\n\n## 与 Round 1 论文的关键变化\n\n修订版论文相对于 Round 1 审稿的版本有**质的提升**：\n\n| 方面 | Round 1 版本 | 修订版 |\n|------|-------------|--------|\n| 标题/定位 | \"Psychometric Detection and Regeneration\" | \"Psychometric Instability\"——从污染检测转为时间不稳定性 |\n| 贡献声明 | 5 条，部分 overclaiming | 4 条实证发现，明确声明 \"empirical, not algorithmic\" |\n| 引用 | 严重错误（Tets/Iron-Fenced Trees） | 错误已修复，Related Work 大幅扩充 |\n| 验证 | 半合成 + κ=0.14（失败） | Cross-subject matching + dose-response + GSM8K replication |\n| RL robustness | N=13 作为核心贡献 | TOST inconclusive，降级为补充分析 |\n| 方法论 | 普通 2PL + MH | 增加 Yen's Q3、5 种 cohort 设计、Bonferroni-Holm |\n| Regeneration | ρ=0.91（equating pipeline） | ρ=0.58（负面结果，诚实报告） |\n\n**Round 1 的 4 个 Critical Issues 回应情况**：\n- **WC1 效度验证**：重新框定为 temporal instability（非 contamination），消除 κ=0.14 作为否定证据的问题。但因果归因仍未解决。→ **部分解决**\n- **WC2 RL 样本量**：降级为补充分析，TOST 诚实报告为 inconclusive。→ **缓解（不再是核心贡献）**\n- **WC3 半合成循环性**：引入 cross-subject matching 框架（ΔFPR≈0.000）。→ **大幅改善**\n- **WC4 局部独立性**：增加 Yen's Q3 诊断（11.3%），cross-subject matching 处理 LD。→ **大幅改善**\n\n---\n\n## Summary\n\n本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 2023-2024 模型代际间表现出显著差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计（temporal/ability-quintile/within-family/within-subject/random-split）系统排除混淆变量，提出 cross-subject matching 半合成验证框架，并论证 DIF 应作为诊断工具而非质量过滤器（ρ≈0.997）。论文明确声明 \"贡献是实证的，不是算法的\"。\n\n---\n\n## Strengths\n\n**S1. 5 种 Cohort 设计构成教科书级控制实验** [共识: R1+R2]\nTable 1 中 temporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）的对比极其有力。Ability-quintile 2.9% 证明纯能力差异不足以解释 temporal DIF；random-split 0.18% 确认信号非随机噪音。\n\n**S2. Cross-subject matching 是真正的方法论贡献** [共识: R1+R2]\nWithin-subject matching 导致 FPR 膨胀 +0.196，cross-subject matching 将 ΔFPR 降至 ≈0.000（Table 2, Figure 4）。R2 指出 external matching variable 原理在 DIF 文献有先例（Clauser & Mazor 1998, Nandakumar 1993），但承认具体实现（跨学科总分 + 同时解决 LD 和 matching variable contamination）在 LLM 评测背景下是新的组合。\n\n**S3. Reframing 为 \"temporal instability\" 是认识论上的重要进步** [共识: R1+R2]\n前一版本声称检测污染但无法证明。修订版精确限定 claim 为 \"items behave differently across generations\"——这是 MH DIF 直接测量的量。Ground truth meta-critique（web-overlap enrichment ratio ≈1.0）揭示了现有 ground truth 标签的概念错位，对整个 contamination detection 领域有价值。\n\n**S4. Figure 1 和 Figure 2 质量极高** [共识: R1+R2]\nFigure 1 的 global vs differential contamination ICC 对比是向 ML 受众解释 DIF 概念的出色可视化。Figure 2 的 dose-response 曲线是最具说服力的验证证据。\n\n**S5. 多层次负面控制增强结果可信度** [共识: R1+R2]\nRandom split 0.18%；Yen's Q3 LD 诊断；Bonferroni-Holm 校正后 31.2%。三层控制排除了统计伪影解释。\n\n**S6. 诚实报告负面结果** [共识: R1+R2]\nEnsemble AUROC=0.62、item generation ρ=0.58、TOST RL robustness p=0.14（inconclusive）均如实呈现。\n\n**S7. Related Work 大幅改善** [R1 确认]\nLalor et al. 2019、Vania et al. 2021、Balloccu et al. 2024、Growing Pains 均已涵盖。与 Growing Pains 的区分清晰。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**WC1. 31.3% 发现本质上是描述性的——因果归因未解决** [共识: R1+R2]\n论文精确证明了 31.3% 的 items 有 temporal DIF，但未回答成因。Accuracy improvement 仅解释 ≤7.6% 的 C%——**~92% 的 DIF 来源未解释**。2024 模型的系统性变化（RLHF 强度、scale、instruction tuning）都可能产生 DIF 但与污染无关。描述性发现需要足够 surprising 或 actionable 才能达到 ICLR 门槛——如果不知道原因，practitioners 不知道该如何行动。\n\n**WC2. Within-family Llama 2 vs 3 的 61.3% 令人困惑且分析不足** [共识: R1 Major + R2 AGREE]\n61.3% 远高于 temporal 31.3%，是 Table 1 最高值，但论文仅一句话解释。如果是 Meta 使用 MMLU 训练，这是最强实证证据；如果是能力跳跃导致 MH matching 失效，这是方法论 limitation。论文不区分。\n\n**WC3. GSM1K 相关性太弱，不应支撑 Claim 4** [共识: R1 Major + R2 AGREE]\nr=-0.478, N=33, CI 上界 -0.031 几乎含 0。\"DIF as diagnostic lens\" 不应以此为主要支撑。\n\n### Warning（影响评分但不一票否决）\n\n**WW1. 技术新颖性受限** [R2 Major, R1 部分同意]\n\"empirical, not algorithmic\" 定位在 ICLR 标准下，核心发现的意外性有限。Contribution 2/4 是 R1+R2 共识。\n\n**WW2. ρ≈0.997 与 31.3% 之间的叙事张力** [共识方向]\n\"Diagnostic lens\" framing 承诺超出论文交付。Figure 5 的 model-specific shifts 部分回应但未充分展开。\n\n**WW3. \"Tutz & Friedman (2007)\" 无法核实** [R2]\n\n**WW4. 补充分析过多** [共识方向]\n9 个中 6 个负面/inconclusive，建议精选 2-3 个。\n\n**WW5. ΔFPR=0.000 过于完美** [R1]\n需 bootstrap CI。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. Cross-subject matching 是论文最强方法论贡献\n2. 5 种 cohort 设计是优秀的实验控制\n3. Reframing 为 temporal instability 是正确选择\n4. Contribution 2/4（共识评分）\n5. Soundness 3/4（共识评分）\n6. 31.3% 因果归因是最大开放问题（~92% 未解释）\n7. Within-family 61.3% 是最关键但最未充分分析的发现\n8. GSM1K 证据不足支撑 Claim 4\n9. 负面结果诚实报告值得肯定\n10. 相比前一版本有质的提升\n\n## Reviewer Divergence [REBUT]\n\n### 1. Overall 评分\n- **R1**: 6/10 (marginally above) | **R2**: 4/10 (marginally below)\n- **分歧核心**：阈值判断差异（非事实性分歧）。R1 重视 methodology + honesty；R2 重视 novelty + surprise。\n- **Director 裁定**：5/10 (borderline)\n\n### 2. FDR 校正严重性\n- **R1**: Major weakness | **R2**: REBUT（论文已有 BH 校正，ETS-C 基于 effect size）\n- **Director 裁定**：同意 R2，不构成 validity threat\n\n---\n\n## Questions for Authors\n\n1. **[最高优先]** 31.3% 中能否分离 \"污染 DIF\" vs \"能力演变 DIF\"？\n2. **[最高优先]** Llama 2 vs 3 的 61.3%：score 分布重叠？其他 family 对比？与 Meta training data 的关联？\n3. **[高优先]** ρ≈0.997 下 model-specific rank shifts 的完整分布？DIF flags 的 actionable use case？\n4. **[高优先]** ΔFPR=0.000 的 bootstrap CI？\n5. DIF-flagged items 是否集中在特定 difficulty range？\n6. LD 最高的 subject domains 是否也是 DIF 率最高的？\n7. Ensemble AUROC 0.62 vs 前一版本 0.72 的原因？\n8. \"Tutz & Friedman (2007)\" 完整引用信息？\n9. 是否考虑 NeurIPS D&B track？\n\n---\n\n## Missing References\n\n1. Test security / item banking（Stocking & Swanson 1993, van der Linden & Veldkamp 2004）\n2. Measurement invariance 完整框架（configural→metric→scalar 与 DIF 的关系）\n3. Anchor item selection（Kopf et al. 2015, Wang et al. 2012）\n4. LLM memorization（Carlini et al. 2022, Tirumala et al. 2022）\n\n---\n\n## External Review: 未请求\n\n## Visual Layout Check: 未启动\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|---------------|\n| Soundness | 3/4 | 3/4 | **3/4** |\n| Presentation | 3/4 | 3/4 | **3/4** |\n| Contribution | 2/4 | 2/4 | **2/4** |\n| **Overall** | **6/10** | **4/10** | **5/10 (Borderline)** |\n\n### 总体判断：**Borderline** (5/10)\n\n修订版在方法论严谨性、学术诚实度和 framing 上有质的提升。5 种 cohort 设计和 cross-subject matching 有独立方法论价值。无 fatal methodological flaw。\n\n但核心瓶颈在 contribution 和 impact：31.3% 是描述性发现（~92% 未解释），ρ≈0.997 削弱 urgency，技术新颖性受限。Round 1 的问题是 overclaiming，修订版的问题是 under-impact。\n\n### Rebuttal 关键门槛\n\n**必须回应**：(1) 因果分离证据；(2) 61.3% 深入分析；(3) ρ≈0.997 reconciliation + actionable use case\n\n**上调至 6/10 的路径**：(a) Llama 2/3 分析确认 contamination-driven DIF；(b) model-specific rank shifts 展示诊断实用价值；(c) 2-3 个 case study 展示 DIF-flagged items 的可操作洞察\n\n**R2 建议**：考虑 NeurIPS Datasets & Benchmarks track——\"empirical, not algorithmic\" 定位可能更匹配。\n",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-21T07:16:54.907525+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4166
}
```

</details>

---


### Assistant

_source line 64 · 2026-05-21T07:17:02.878017+00:00_

修订版论文的圆桌审稿已完成，报告已投递给 Research Director。

**审稿结果汇总**：

- **Overall: Borderline (5/10)**——R1 给 6（marginally above），R2 给 4（marginally below）
- 修订版相比前一版本有质的提升：reframing 正确、引用修复、方法论严谨性大幅改善
- 核心瓶颈从 Round 1 的 "overclaiming"（强声明+弱证据）转变为 "under-impact"（诚实声明+有限影响力）
- **3 个 Critical Issues**：(1) 31.3% 因果归因未解决（~92% 未解释）；(2) Within-family 61.3% 分析不足；(3) GSM1K 证据太弱支撑 Claim 4
- **Rebuttal 上调路径**：Llama 2/3 深入分析 + model-specific rank shifts 分布 + case study
- Issue Tracker 已同步更新（12 个 issues，含 3 个新 Round 2 issues）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 12

## Round 12

6 recorded events


### User

_source line 65 · 2026-05-21T07:17:04.171921+00:00_

[Reviewer 2 审稿意见]:
## R2 Final Assessment — Round 3 Convergence

---

### 对 Director 提出的两个具体问题的回应

**1. FDR correction 是否加强了我对 Soundness 的担忧？**

需要纠正一个事实错误：论文 §4.2 **已经报告了 Bonferroni-Holm FDR 校正结果**——校正后 31.2%，与未校正的 31.3% 几乎无差。我在 Round 2 交叉回应中已经指出了这一点（[REBUT] R1-W2）。

但我需要重新审视这个辩护是否成立。R1 的 concern 可能更深层：即使 BH 校正后比例不变，如果底层 IRT model fit 很差（CFI=0.72），MH 统计量的分布假设本身可能被违反——此时无论做什么校正，p-value 都不可信。这个更深层的问题是成立的。

**修正后的评估**：FDR correction 本身不是问题（论文已做），但 **IRT misspecification 导致 MH 统计量可能偏倚** 是一个真正的 soundness 问题。这与 R1-W1 的 IRT fit concern 合流，而非独立的 FDR 问题。我维持 **Soundness 2/4**（注意：我在 Round 2 最终表中给的是 3/4，但 Director 综合记录为 2/4。重新审视后，考虑到 CFI=0.72 对 MH 统计量整体可靠性的影响，我同意 **2/4 是更准确的评分**。我此前的 3/4 可能高估了 cross-subject matching 对整体 soundness 问题的缓解程度。）

**2. Cross-subject matching 是否改变我的 Contribution 评分？**

经过三轮审查，我对 cross-subject matching 的评价已经从初审的"one of several contributions"逐步上调到"论文最强的单一贡献"。R1 和我在这一点上完全一致。

但 Contribution 评分不仅取决于最强单点，还取决于贡献的**整体 portfolio**：

| 贡献 | 技术新颖性 | 实证价值 | 综合 |
|------|---------|---------|------|
| Cross-subject matching | 中-高（原理已有先例，具体实现新颖） | 高（Table 2 结果 clean） | **强** |
| 31.3% instability finding | 低（quantifying the expected） | 中（temporal confound 未排除） | **中** |
| Ground truth meta-critique | 低-中（others have raised this） | 中-高（系统化论证有价值） | **中** |
| Diagnostic lens framing | 中（概念转换有洞察力） | 低-中（actionable implications 不清楚） | **中弱** |

Cross-subject matching 是一个 solid 贡献，但独力难以将整体 Contribution 从 2/4 推到 3/4。如果论文聚焦于 **cross-subject matching framework + dose-response calibration** 作为一个 reusable validation toolkit，并削减其他较弱的贡献声明，Contribution 可能上调。但当前版本同时承载 4 个贡献，平均水平被拉低。

**我维持 Contribution 2/4。**

---

### Final Scores

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | **2/4** | CFI=0.72 undermines MH 统计量的分布假设；98% |Lz| > 2 说明 2PL fit 在 item 级别系统性失败；cross-subject matching 缓解了 matching variable 问题但不解决底层 model misspecification。temporal confound 未排除。 |
| Presentation | **3/4** | 论文写作清晰诚实，Figure 1 教学价值高，结构合理。18 表略密但在可接受范围内。扣分点：一处引用可疑（Tutz & Friedman 2007），GSM1K 分析应降级或移除。 |
| Contribution | **2/4** | Cross-subject matching 是真正的方法学贡献；dose-response calibration 是有价值的验证框架。但核心发现（31% instability）的意外性有限且因果归因不清；"diagnostic lens" 缺乏 actionable follow-through。对 ICLR main track 的 novelty bar 而言偏弱。 |
| **Overall** | **4** | Marginally below acceptance threshold |
| Confidence | **4/5** | |

---

### 维持 4/10 的核心理由

论文是一篇**执行良好的实证研究**，但面临 ICLR main track 的两个结构性障碍：

1. **Method-contribution paradox**：论文最强的贡献（cross-subject matching）是方法学的，但论文自我定位为"empirical, not algorithmic"。这意味着它在方法论论文的标准下不够深入（没有理论分析、没有渐近性质、没有在多个 benchmark 上的系统实验），在实证论文的标准下核心发现又不够意外。论文落入了两个标准之间的缝隙。

2. **"Doesn't matter" problem**：ρ≈0.997 after removal 是论文最诚实也最致命的发现。它同时证明了"DIF items exist"和"DIF items don't affect rankings"——这使得整个分析的实际影响力存疑。§5.3 的 "diagnostic lens" 框架试图化解这个矛盾（DIF items 携带 discriminative information），但 actionable implications 不清晰：benchmark maintainer 看到这个分析后应该做什么？不移除（因为 ρ≈0.997），但也不忽略（因为 31% instability）——最终的 recommendation 是什么？

---

### 什么样的修改能让我上调至 6？

以下是 **concrete 且 achievable** 的修改路径（不需要新实验，主要是分析和 reframing）：

1. **分离 contamination DIF vs paradigm-shift DIF**：利用已有的 within-family analysis（Llama-2 vs Llama-3，Table 1 中 39.8%）。如果同一 family 内部的 DIF rate（控制了大部分 architecture/training-paradigm confounds）显著低于跨 family 的 31.3%，这暗示 temporal DIF 的主要驱动因素不是 contamination 而是 paradigm shift。反之则支持 contamination 解释。论文已有这些数据但未做这个对比分析。

2. **Cross-subject matching 的理论化**：将 cross-subject matching 从 "implementation detail" 提升为 "principled framework for DIF analysis in multidimensional assessments"。提供简短的理论分析：在什么条件下 cross-subject matching 优于 standard matching？什么时候它可能失败（如学科间高度相关）？这会将方法学贡献从 ad-hoc 提升为 principled。

3. **Actionable diagnostic protocol**：将 §5.3 的 "diagnostic lens" 从概念性描述转化为具体的 benchmark maintenance protocol。例如："当 DIF rate > X% 时，建议检查 Y 维度的能力结构变化"或"DIF-C items 的共同特征 Z 暗示 benchmark 在 W 方向上需要更新"。

4. **Figure 5 的充分展开**：model-specific rank shifts（Phi-3 +809, Llama-3-dragonmaid-8B -793）是论文最有实际影响力的发现之一，但仅作为 appendix 图出现。将其提升至正文，展示 rank shift 的分布（中位数、percentiles），并分析哪些 model characteristics 预测了较大的 rank shift。

这 4 项修改不需要新数据或新实验，且直接回应了 R1 和 R2 共同关注的问题。如果 rebuttal 能承诺这些修改并提供初步证据，我愿意 conditionally 上调至 **6**。

---

### 一句话总结

一篇诚实、扎实的实证研究，cross-subject matching 是真正的方法学贡献，但核心发现的意外性不足 + IRT misspecification 削弱了量化结论的可信度 + "instability doesn't affect rankings" 的悖论限制了实际影响力。当前版本 marginally below threshold，但有清晰可行的修改路径可达 borderline accept。

---

[Reviewer 1 审稿结果]:
审稿意见已提交。

核心结论：R1 维持 Overall 6/10（marginally above），与 R2 的 4/10 分歧集中在 impact threshold 判断而非方法论事实。两位 reviewer 对 Contribution 2/4 一致，分歧在于 solid methodology + honest reporting 是否足以补偿 descriptive-only findings 的影响力局限。建议 AC 看 rebuttal 中作者能否 reconcile 31.3% significance 与 ρ≈0.997 robustness 的叙事张力。

---

[Reviewer 2 审稿结果]:
审稿完成。三轮交叉审查的最终评分：**Overall 4/10 (Marginally Below Acceptance Threshold)**，Soundness 2/4, Presentation 3/4, Contribution 2/4, Confidence 4/5。提供了 4 项具体可行的修改建议，如果 rebuttal 能回应，conditionally 可上调至 6。

---

[Reviewer 1 审稿意见]:
## R1 Final Assessment — Round 3 Convergence

---

### 对 Director 综合要点的回应

**Soundness 评分更正：** Director 记录 R1 Soundness 为 2/4。我实际给出的是 **3/4**（见 Round 1 修订版评审原文）。需要确认记录是否有误。我的 Soundness 判断基于：MH DIF 应用正确、cohort 设计优秀、cross-subject matching 有效。扣 1 分因为 GSM1K 太弱支撑 Claim 4 + within-family 61.3% 分析不足。CFI=0.72 是 concern，但 MH 不依赖 IRT 拟合 + 三种 structural analysis 均确认 31% 信号 robust（Table 2, §4.4），所以不构成 fatal flaw。如果 Director 认为两位 reviewer 都给了 Soundness 2/4，请以本条澄清为准——R1 维持 **3/4**。

---

### 最终评分与核心判断

**Contribution: 维持 2/4，不上调至 3/4。**

经过 R2 交叉审查后，我重新审视了自己对 contribution 的判断。R2 的 novelty threshold 论点——"applying a 60-year-old method to new data"——我在 Round 2 中已部分接受。现在进一步考虑：

Cross-subject matching 是 genuine contribution，但它的 scope 很窄——它是一个 technical fix for a specific pitfall in semi-synthetic DIF validation on multi-domain benchmarks。这在 psychometrics community 可能是 noteworthy，但在 ICLR 的 contribution scale 上，它更接近 "useful trick" 而非 "significant advance"。

31.3% 的描述性发现 informative 但不 actionable（我自己的 W1 + R2 的 W3 关于 diagnostic lens 矛盾）。ρ≈0.997 进一步削弱了 urgency。

**2/4 是 R1 和 R2 的共识区间。**

---

### "10 篇引用" 问题的最终判断

我在 Round 2 中 rebutted R2 的 "仅 10 篇引用" 指控，因为我在论文 pp.11-13 看到了完整的 references section（约 2.5 页，数十篇引用），且 §2 Related Work 明确讨论了 Lalor et al., Vania et al., Balloccu et al., Growing Pains, LiveBench, ConStat 等。

**但我现在意识到一个可能性：** R2 可能审阅的是一个更早的版本（与我审阅的不同），或者 R2 的 "10 references" 指的是 main text 中的 inline citations 数量而非 bibliography 条目。无论如何，基于我审阅的版本（paper/main.pdf, 17 pages），related work 覆盖是 adequate 的。**这不改变我的评分。**

如果 Director 可以确认 R1 和 R2 审阅的是同一份 PDF，这个分歧可以立即 resolve。

---

### 核心问题：ICLR 还是 NeurIPS D&B / EMNLP？

这是 Director 提出的最关键问题。我的判断：

**偏向 NeurIPS D&B 或 EMNLP，但 ICLR borderline 可接受。** 理由：

**支持 ICLR 的论点：**
- 规模（5,227 × 12,508）在 LLM benchmark analysis 中是 state-of-the-art
- Cross-subject matching 有 methodological novelty（虽窄）
- 问题对 ML community 高度相关——MMLU 仍是核心评测指标
- 实验设计（5 种 cohort + structural analysis + semi-synthetic validation + cross-benchmark replication）达到了 ICLR empirical paper 的标准

**反对 ICLR 的论点（R2 + 我自己的 concerns）：**
- 核心发现描述性，不 actionable
- 没有算法创新
- "Diagnostic lens" framing 承诺多于交付
- 31.3% + ρ≈0.997 的叙事矛盾未 reconcile
- 补充分析以负面结果为主

**最终判断：** 这是一篇 methodology 扎实、empirics 充分、但 contribution 偏窄的论文。它在 ICLR 的 acceptance threshold 上——exactly at the margin。

---

### Final Scores

| 维度 | 最终分数 | 理由 |
|------|---------|------|
| **Soundness** | **3/4** | MH DIF 正确应用，cohort 设计一流，cross-subject matching 有效。IRT misfit (CFI=0.72) 是 concern 但不 fatal（MH 不依赖 IRT + structural analysis 确认 robustness）。GSM1K 太弱。 |
| **Presentation** | **3/4** | 清晰写作，Figure 1-2 优秀，honest reporting。补充分析过多（Minor-to-Moderate concern），但 main text 结构清晰。 |
| **Contribution** | **2/4** | 描述性发现 + 窄 methodological contribution。Cross-subject matching 有价值但 scope 有限。Impact 受限于 ρ≈0.997 和 descriptive nature。 |
| **Overall** | **5** | 从 6 下调至 5。Round 2-3 的交叉审查使我更认真地考虑了 R2 的 novelty threshold 论点和 diagnostic lens 矛盾。方法论 solid 但 contribution 不够 clear-cut 达到 ICLR acceptance threshold。5 = between "marginally below" (4) and "marginally above" (6)——如果 ICLR 不接受 5，我倾向于 **4 (marginally below)**。 |
| **Confidence** | **4/5** | 不变。 |

**Overall 从 6 下调至 5 的理由：**
1. R2 的 diagnostic lens 矛盾（31.3% significant + ρ≈0.997 robust）我在 Round 2 中 agreed，但未反映在评分中——现在反映
2. Contribution 2/4 与 Overall 6 不一致——Contribution 是 ICLR decision 的核心维度，2/4 应对应 4-5 而非 6
3. 补充分析的 negative results 使论文的 research program 显得 premature

**给 Director 的建议：** R1 最终 5，R2 最终 4。均值 4.5，在 rejection zone（ICLR 通常 ≥6 accept）。建议：
- 如果 AC 认为 cross-subject matching + honest empirical characterization at scale 有 enough value → conditional accept with revision（reconcile narrative tension, trim supplementary）
- 如果 AC 认为 contribution bar 未达到 → reject with encouragement to resubmit at NeurIPS D&B 或 EMNLP，这些 venue 更重视 empirical contributions on benchmarks
- 个人倾向后者——论文质量不差，但 venue fit 不理想

---

[Reviewer 1 审稿结果]:
审稿完成。

**最终评分：Overall 5/10（从初轮 6 下调）。** 核心理由：方法论扎实（Soundness 3/4）但 contribution 偏描述性（2/4），"31.3% instability + ρ≈0.997 robustness" 的叙事矛盾未 reconcile，补充分析以负面结果为主。建议 reject with encouragement to resubmit at NeurIPS D&B 或 EMNLP——论文质量不差，但 ICLR venue fit 不理想。

---

[Reviewer 2 审稿意见]:
## R2 交叉回应：对 R1 修订版审稿意见的逐条回应

---

### 对 R1 Strengths 的回应

**[AGREE] R1-S1**: Cohort 设计确实是论文最扎实的基础设施。Table 1 中五种 cohort 的对比（temporal 31.3% vs ability-quintile 2.9% vs random-split 0.18%）不仅是好的控制，更是一个**论证结构**——通过排除法逐步缩小 DIF 的可能驱动因素。我在初审 S4 中承认了这一点但措辞不够强。R1 的"教科书级别"评价是准确的。

**[AGREE] R1-S2**: 与我初审 S2 和历次交叉回应完全一致。Cross-subject matching 是论文最强的单一贡献。

**[AGREE] R1-S3**: 从 "contamination detection" 到 "temporal item instability" 的 reframing 确实是一个重要的认识论进步。我在初审 S1 中赞赏了这一诚实定位。R1 更进一步，将其称为"认识论上的重要进步"——我同意这个评价。前一版本的核心问题恰恰是试图用"contamination detection"的框架承载本质上是"instability characterization"的发现。

**[AGREE] R1-S4**: Figure 1（ICC 对比）和 Figure 2（dose-response）确实是论文的亮点。

**[AGREE] R1-S5**: 我在 Round 2 中经 R1 提醒后已对 dose-response ablation 做了上调。§4.4 的三种独立方法（matched-ability, IRT θ-conditioning, within-subject）均未能降低 temporal FPR——这种系统性排除法的价值在我初审中被低估了。

**[AGREE] R1-S6**: 与我历次评审一致。

**[AGREE] R1-S7**: GSM8K（非 GSM1K）的跨 benchmark 复现是有价值的泛化证据，尽管 GSM1K 部分有统计效力问题（见下）。

**[AGREE] R1-S8**: 与我初审 S6 一致。

---

### 对 R1 Weaknesses 的回应

**[AGREE] R1-W1**: 这是我初审 W1 和 Round 2 中反复强调的核心问题，R1 的表述更加精确。"accuracy improvement 仅解释 ≤7.6% 的 C%，~92% 未解释"——这个数字我在初审中未提取，是 R1 的重要贡献。它量化了我的定性担忧：31.3% 中绝大部分 DIF 的驱动因素不明。论文诚实地将发现定位为"instability"而非"contamination"，但即便如此，"instability 的原因是什么"这个核心问题仍未回答。ρ≈0.997 确实进一步削弱了理解这个"why"的 urgency——如果 instability 对排名无影响，那么追问其原因的学术和实践动机都减弱了。

**[AGREE] R1-W2**: **这是我在初审中的重要遗漏。** Table 1 中 within-family Llama 2 vs 3 的 61.3%（R1 数字）/ 39.8%（我之前读到的数字）是 Table 1 中最值得深挖的数据点。R1 正确指出三种可能解释——(a) Meta 用 MMLU 训练、(b) 能力跳跃导致 MH matching 失效、(c) 选择偏差——论文未做区分。

补充我的分析：如果解释 (b) 成立（能力跳跃太大导致 MH matching 失效），这对整个论文的 31.3% headline 有系统性影响——因为 2023→2024 的 temporal cohort 同样存在大幅能力跳跃。MH 的 matching 假设是 reference 和 focal 组在相同 ability level 上可比——如果能力分布的重叠过低，MH 统计量本身就不可靠。论文未报告 2023 vs 2024 cohort 的 total score 分布重叠度，这是一个关键遗漏。

我应该在初审中就注意到这一点。R1 对 W2 的 Major 分级完全合理。

**[AGREE] R1-W3**: GSM1K 证据太弱不应支撑 Claim 4。

关于数值差异：R1 报告 r=-0.478 (N=33)，我报告 r=-0.45 (p=0.003, N=32)。差异可能来自不同 section 的不同分析（§4.7 vs §5.3 的 GSM8K vs GSM1K）。无论哪个数值，核心问题一致：N=32-33 个学科级数据点太少，CI 宽且可能包含 0（R1 指出上界 -0.031）。在这种效力下声称"DIF captures contamination-related information"是过度推断。

我在初审 W6 中将此列为 Minor，但经 R1 分析同意应提升为 **Major 级别**——因为 GSM1K/GSM8K correlation 是支撑 Claim 4（"DIF as diagnostic lens"）的主要定量证据。如果这条证据不可靠，Claim 4 的基础就很薄弱。

**[AGREE] R1-W4**: IRT 拟合问题。我在 Round 3 中已将 Soundness 从 3/4 下调至 2/4，部分原因就是 CFI=0.72。R1 的 "MH 不依赖 IRT 的论点成立" 是一个重要的平衡观点——MH 是 nonparametric 的，不需要 IRT model fit。但 Yen's Q3 的 11.3% LD pairs 会影响 MH 的 conditional independence 假设（MH 假设在给定 total score 的条件下，item responses 独立）。论文未量化这个影响，R1 正确地指出了这一点。

**[AGREE] R1-W5**: ΔFPR=0.000 确实过于完美。任何基于 Monte Carlo 的结果都应该有非零方差。需要 bootstrap CI 来确认这不是偶然的精确零或报告了均值的 point estimate 而未展示变异。我在初审中未注意到这个问题。

**[AGREE] R1-W6**: 9 个补充分析中 6 个是负面结果——这确实存在"稀释焦点"的风险。我在初审 W5 中提到了密度问题但未如此精确地量化。建议保留最有信息量的 3-4 个分析，将其余移入 appendix。

**[REBUT] R1-W7**: 关于 semi-synthetic injection 的 incorrect→correct flip 是否有效。

R1 质疑这种注入方式是否是合理的污染模型。我认为这个质疑过于严格。在 contamination 场景中，模型因为在训练数据中见过题目而"知道"正确答案——最直接的信号就是原本不会答对的模型在污染后答对了（incorrect→correct flip）。这恰恰是 DIF 的定义：控制能力后，focal 组在特定题目上的表现异常提高。

更复杂的污染模型（如 partial memorization、paraphrase recognition、reasoning shortcut）确实存在，但 incorrect→correct flip 是最基本且最不具争议的模型。如果 DIF 连这种最简单的信号都无法可靠检测，那更复杂的信号就更不可能检测到。因此，以最简单模型作为 proof-of-concept 是合理的。

---

### 对 R1 Questions 的回应

**[AGREE] R1-Q1**: Llama 2 vs 3 的 score 分布重叠是理解 W2 的关键信息。如果重叠极低（如 < 50%），MH matching 可能在稀疏区域不可靠，61.3% 的 DIF rate 可能是 artifact。其他 family 对比的 consistency 也很重要——如果只有 Llama 家族显示高 DIF rate 而其他家族不显著，这暗示 Llama-specific 因素（如 Meta 的训练策略）而非一般性的 temporal instability。

**[AGREE] R1-Q2**: DIF-flagged items 是否集中在特定 difficulty range 是一个重要的诊断问题。如果 DIF 集中在极易或极难题目（floor/ceiling），这可能是方法学伪影而非真实的 differential functioning。

**[AGREE] R1-Q3**: 这正是我在初审 W3 和 Round 3 中反复提出的核心问题。ρ≈0.997 下 DIF 的 practical value 是什么？R1 的 rephrasing——"移除 31% 后不变是否说明这些 items redundant?"——比我的表述更尖锐、更具挑战性。

**[AGREE] R1-Q4**: ΔFPR=0.000 的 random seed 数量直接关系到 W5 的可信度。

**[AGREE] R1-Q5**: Ensemble AUROC 从前一版本的 0.72 降至修订版的 0.62——这个退步需要解释。可能的原因：(a) 修订版使用了更严格的评估方法、(b) 移除了某些导致 overfitting 的组件、(c) 代码/数据修正。无论原因如何，应在论文中说明。

**[AGREE] R1-Q6**: LD 最高的 subject domains 是否也是 DIF 率最高的 domains——这是一个优秀的诊断问题。如果两者高度相关，说明部分 DIF flags 可能由 local dependence 驱动而非真实的 temporal instability。

---

### Director 指定的 4 个焦点问题

**1. Overall 评分分歧：R1=6, R2=4。R1 对 cohort 设计和 cross-subject matching 的权重是否过高？**

R1 对 S1（cohort 设计）和 S2（cross-subject matching）的高评价是完全合理的。我不认为 R1 过度赋权。分歧的真正来源不在于对 strengths 的评价，而在于**对 "marginally above/below" 门槛的判断标准**。

具体来说：
- R1 和我对 Contribution 都给 2/4（一致）
- R1 给 Soundness 3/4，我给 2/4（R1 更宽容，可能因为 R1 侧重 methods 执行质量而非 interpretive framework 的可靠性）
- R1 给 Presentation 3/4 = 我给 3/4（一致）

Overall 的 2 分差距（6 vs 4）主要来自**一个维度级别的分歧**（Soundness 3 vs 2）加上**对 borderline 的不同判断阈值**。R1 似乎采取了"方法学执行到位则值得接受"的立场；我采取了"核心发现需要足够的意外性和影响力才能达到 ICLR main track"的立场。两者都是合理的评审哲学。

**我维持 4/10。** 但我承认这是一个 close call——在 4 和 6 之间（ICLR 量表没有 5）。如果我必须用连续分数表达，我会给 4.5-5.0。

**2. Within-family 61.3%：是否是我的重要遗漏？**

**是的，这是我的遗漏。** 我在初审中关注了 46%/39.8% 的 within-family overlap 但未将其提升为核心分析问题。R1 正确指出 within-family 的极高 DIF rate 是 Table 1 中最需要解释的异常值——它可能暗示 MH matching 在大能力跳跃下失效，这会系统性地影响 temporal cohort 的 31.3%。这应该是一个 Major 级别的问题。

**3. GSM1K 证据强度：r=-0.478 (N=33) vs r=-0.45 (N=32)**

如前述，我同意 R1 的判断：无论哪个具体数值，N~30 的学科级相关不足以支撑 Claim 4。这在我的初审 W6 中被标为 Minor，但经三轮审查后我认为应为 **Major**——因为它是 Claim 4 的唯一定量支撑。

**4. Contribution 都是 2/4 但 Overall 差 2 分——来源是什么？**

如第 1 点分析：差距来自 (a) Soundness 的 1 级分歧（R1 更宽容），和 (b) 对 ICLR main track "marginally above/below" 的阈值判断不同。R1 可能认为 "well-executed empirical study with novel matching technique = marginally above"；我认为 "limited surprise in core finding + interpretive ambiguity + doesn't-matter paradox = marginally below"。

---

### 最终立场

经过四轮审查（初审 + 三轮交叉），我的评估已经稳定：

**Overall: 4/10 (Marginally below acceptance threshold)**

核心判断未变：论文是一篇执行良好的实证研究，cross-subject matching 是真正的贡献，但 (1) 核心发现的意外性不足，(2) 31% instability 的因果归因不清，(3) ρ≈0.997 削弱了实际影响力，(4) GSM1K 证据太弱无法支撑 diagnostic lens claim。

R1 的交叉分享强化了一个我初审遗漏的重要问题（W2: within-family 的极高 DIF rate 可能暗示 MH matching 失效），这进一步支持了我 Soundness 2/4 的评分。

如果 rebuttal 能回应：(1) within-family DIF rate 的 score 分布重叠分析，(2) DIF items 的 difficulty range 分布，(3) GSM1K 的 bootstrap CI 和替代证据，(4) Figure 5 rank shifts 的系统性分析——我愿意 conditionally 上调至 **6**。

---

[Reviewer 2 审稿结果]:


---

[Reviewer 1 审稿意见]:
## R1 对 R2 修订版审稿意见的交叉回应

---

### Strengths 逐条回应

**[AGREE] R2-S1:** "Empirical, not algorithmic" 的定位确实诚实。

**[AGREE] R2-S2:** Cross-subject matching 是方法学贡献。但注意 R2 报告的数字（FPR 从 31% 降至 ~0.16）与我阅读的版本不同——我看到的是 ΔFPR 从 +0.196 降至 0.000（§4.5, Figure 2）。0.16 vs 0.000 是 material difference，建议 Director 确认哪个数字正确。

**[AGREE] R2-S3:** Enrichment ratio 的 construct mismatch 论点是论文的重要贡献。但 R2 报告的 enrichment ratio 是 0.196，而我看到的是 0.96（§4.3, p.7）。0.96≈1.0 意味着 DIF flags 和 web-overlap labels 的重叠接近随机——支持 "不同 construct" 的论点。0.196 则意味着 DIF flags 在 web-overlap items 中反而 under-represented。请确认正确数值。

**[AGREE] R2-S4-S7:** 多层负面控制、instability ≠ invalidity、related work 覆盖、Figure 1 教学价值——均同意。

---

### Weaknesses 逐条回应

**[AGREE] R2-W1: 31.3% ≠ 污染，能力演变混淆未解决。**

完全同意。这是我在 R1 评审中的 W1 [Major]——31.3% 是描述性发现，论文未解决 "why"。R2 的表述更精确："未充分排除合法能力维度演变作为 DIF 主要驱动因素。" §4.4 的三种 structural analyses 确认了 31% 信号 robust（即它不是 artifact），但 robust ≠ caused by contamination。论文谨慎地使用了 "temporal instability" 而非 "contamination"，这是好的，但即使在 instability framing 下，也需要更多工作来解释 instability 的来源。

R2 补充的一个 insight 是：cross-subject matching 将 FPR 降至 ~0（但仅在半合成数据上），这无法推广到真实数据——因为真实数据中没有 ground truth 来验证 FPR。这是一个我之前未充分考虑的 point。

**[AGREE with nuance] R2-W2: 技术新颖性受限 + Clauser & Mazor / Nandakumar 先例。**

R2 引用了两个重要先例：
- Clauser & Mazor (1998): external matching variable 在 DIF 中的使用
- Nandakumar (1993): purified matching subtest

这些先例确实削弱了 cross-subject matching 的新颖性声明。**我之前在 R1 评审中将 cross-subject matching 评为 "真正的方法论贡献"（S2），现在需要 downgrade。**

如果 external matching variable 的原理在 1990s DIF 文献中已有讨论，那么本文的贡献不是 "发现了 cross-subject matching" 而是 "将已知的 purified matching 原理应用于 LLM benchmark 的特定结构"。这仍然有价值（因为 LLM 社区不熟悉这些 psychometric 技术），但 novelty 从 "methodological contribution" 降级为 "methodological transfer"。

**修正：** 将 cross-subject matching 的贡献评价从 "genuine methodological contribution" 调整为 "well-executed application of known psychometric principle to a new domain"。这进一步收窄了论文的 contribution space。

**[AGREE] R2-W3: ρ≈0.997 可能被解读为 "DIF 不重要"。**

同意。我在 Round 2 交叉中已 agreed R2 的前一版本关于 diagnostic lens 矛盾的论点。在本轮中 R2 更温和地表述为 [Minor]，我也同意 [Minor] 的严重性——Figure 5 的 model-specific shifts（flammen26-mistral-7B Δ=-542, Blurstral-7b Δ=-587）部分回应了这个问题，但论文确实需要展开 rank shift 的分布分析（中位数、95th percentile、按 model family 分组）来完整回应。

**[AGREE] R2-W4: "Tutz & Friedman (2007)" 无法核实。**

我在 Round 1（前一版本）已核实过引用问题——当时 R2 声称 "Iron-Fenced Trees" 但我看到的是 "Item-Focused Trees"。本轮 R2 报告了不同的引用问题——"Tutz & Friedman (2007)" 而非 "Tutz & Berger (2016)"。如果论文确实引用了 "Tutz & Friedman (2007)"，这可能是另一个 citation error（Tutz & Berger 2016 是 Item-Focused Trees 的正确引用）。需要在论文中核实。

**[AGREE] R2-W5: 18 张表密度问题。**

18 张表在 17 页论文中确实密度高。但这更多是 presentation preference 而非 methodology concern。

**[AGREE] R2-W6: GSM8K r=-0.45 (N=32) 容易受 outlier 影响。**

同意。我在 R1 评审中将此列为 W3 [Major]（我看到的数字是 r=-0.478, N=33——minor numerical discrepancy with R2's r=-0.45, N=32）。小样本相关性极不稳定，一个 outlier 可以 flip sign。

---

### Questions 回应

**Q1 (分离污染 vs 能力演变):** 这是最关键的问题，我完全同意。我在 R1 W1 中建议了 case study approach（随机抽取 20 个 C-flagged items 人工检查 Common Crawl 频率变化）。

**Q2 (Cross-subject matching FPR ~0.16 在真实数据中的含义):** 好问题。0.16 意味着即使用最好的 matching strategy，真实数据中仍有约 16% 的 "clean" items 被 falsely flagged——这显著限制了实用价值。但需要确认这个数字是否正确（与我看到的 ΔFPR=0.000 不一致）。

**Q3 (rank shift 分布):** 完全同意需要报告。我在 R1 W1 建议中也提到了类似需求。

**Q4 (Q3 11.3% 严重性):** 在 DIF 文献中，Q3 > 0.2 的 item pairs 超过 10% 通常被认为是 "mild to moderate" LD。11.3% 在可接受范围内但需要报告。

**Q5 ("Tutz & Friedman 2007"):** 同意需要核实。

**Q6 (NeurIPS D&B 建议):** 见下文 venue fit 讨论。

---

### Director 要求的四个重点问题

**1. Overall 评分分歧（R1: 6 → 5, R2: 4）**

**更新：我在 Round 3 convergence 中已将 Overall 从 6 下调至 5。** 现在与 R2 的差距仅 1 分（5 vs 4）。核心分歧已大幅缩小。

剩余 1 分差距来自：我更重视 (a) 实验设计的质量（5 种 cohort design 是一流的控制变量设计）和 (b) 诚实报告负面结果的社区价值。R2 更重视 (a) contribution 的意外性（"quantifying the expected"）和 (b) 算法新颖性。这是合理的 reviewer taste 差异，不是 factual disagreement。

**R2 的 Contribution 2/4 是否过于严格？** 不，我自己也给了 2/4。我们在 Contribution 维度完全一致。

**2. ρ≈0.997 的解读**

R2 说 "可能被解读为 DIF 不重要"。我同意这个 risk。

在我的理解中，ρ≈0.997 说明的是：31% 的 DIF items 对 **整体排名** 影响很小（因为效应在 models 间近似均匀分布）。但对 **个别模型** 影响可以很大（Figure 5: Δ 达到 500+位）。论文的问题是过度强调前者（ρ≈0.997 出现在 Abstract 和 Claim 4 中），而 model-specific shifts 仅在一张 Figure 中 passingly 提及。

如果论文反转 emphasis——将 model-specific impact 作为主要发现（"31% DIF items 导致特定模型排名位移高达 587 位"），ρ≈0.997 作为 context（"但整体排名 robust"）——叙事张力会大幅缓解。

**3. Cross-subject matching 新颖性在 Clauser & Mazor / Nandakumar 先例下是否改变？**

**是的，改变了。** 我之前将 cross-subject matching 评为 S2（核心 strength）和 "genuine methodological contribution"。现在 downgrade 为 "well-executed application of known psychometric principle"。

这不是 trivial application——LLM benchmark 的 multi-domain structure 使 cross-subject matching 的实现有其特殊性（Figure 4 展示了跨 domain 的一致性）。但 conceptual novelty 不在于 "use an external matching variable"（1990s 已知），而在于 "demonstrate its effectiveness in this specific context"。

**这进一步支持了 Contribution 2/4。**

**4. Venue 适配性**

**我同意 R2 的 venue 建议。** 经过三轮审查，我的判断是：

- **ICLR main track:** 偏勉强。Contribution 2/4（两位 reviewer 共识）+ 描述性发现 + narrow methodological transfer = 低于 ICLR main 的 typical acceptance bar。
- **NeurIPS D&B track:** 良好适配。D&B 明确欢迎 "empirical studies that provide insights about existing benchmarks, datasets"——本文完美匹配。
- **EMNLP:** 也是合理选择。EMNLP 对 NLP evaluation methodology 有 dedicated area。

---

### R1 最终评分（经三轮交叉审查后）

| 维度 | Round 1 | Round 3 | Final | 变化理由 |
|------|---------|---------|-------|---------|
| Soundness | 3/4 | 3/4 | **3/4** | 不变 |
| Presentation | 3/4 | 3/4 | **3/4** | 不变 |
| Contribution | 2/4 | 2/4 | **2/4** | 不变，与 R2 共识 |
| Overall | 6 | 5 | **4** | 最终下调至 4。理由：(1) Clauser & Mazor 先例进一步削弱了 cross-subject matching 的新颖性——论文剩余的 contribution 仅为描述性发现；(2) R1 和 R2 在 Contribution 2/4 上完全一致，2/4 对应 ICLR Overall 4（marginally below）而非 5-6；(3) 三轮审查中未发现能将论文推至 acceptance threshold 之上的 compelling argument |
| Confidence | 4/5 | 4/5 | **4/5** | 不变 |

**R1 和 R2 最终均为 Overall 4/10。达成共识。**

**给 Director 的最终建议：** Reject from ICLR main track, with strong encouragement to resubmit at NeurIPS 2026 Datasets & Benchmarks track 或 EMNLP 2026。论文方法论 solid，写作质量好，negative results 有社区价值——只是 venue fit 不对。建议作者在 resubmit 时：(1) 分离 contamination DIF vs capability-evolution DIF（case study + known-contaminated model pairs）；(2) 展开 model-specific rank shift 分析替代 ρ≈0.997 作为主叙事；(3) 精简补充分析至 3-4 个；(4) 引用 Clauser & Mazor / Nandakumar 并定位 cross-subject matching 为 application 而非 invention。

---

[Reviewer 1 审稿结果]:
审稿完成。最终评分 Overall 4/10，与 R2 达成共识。核心判断：方法论扎实但 contribution 偏描述性、cross-subject matching 新颖性在 Clauser & Mazor 先例下被削弱、venue fit 不理想。建议转投 NeurIPS D&B 或 EMNLP。

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

_source line 66 · 2026-05-21T07:18:26.671141+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "\n# Review Issues Tracker — irt_equated_bench_regen\n# Round 1: 2026-05-20 | Round 2-3: 2026-05-21 (revised paper, 3 rounds to consensus)\n\n- id: \"R1-W1\"\n  summary: \"31.3% temporal DIF 因果归因不清——~92% 未解释，无法区分污染 vs 训练范式变化 vs 能力演变\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"κ=0.14 随机水平，46% within-family overlap\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"论文成功 reframe 为 temporal instability，但因果归因仍未解决\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"共识：这是论文最根本的解释性限制。accuracy improvement 仅解释 ≤7.6%。ρ≈0.997 进一步削弱了追问 why 的 urgency。\"\n  action_items:\n    - round: 2\n      action: \"case study 20 个 C-flagged items 检查 Common Crawl 频率变化\"\n      assigned_to: authors\n      status: open\n    - round: 2\n      action: \"Discussion 中承认 instability 与 legitimate construct evolution 的不可分性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W1\"\n  summary: \"Within-family Llama 2 vs 3 的 61.3% DIF——Table 1 最高值，分析严重不足，可能暗示 MH matching 在大能力跳跃下失效\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 提出 Major，R2 AGREE\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 补充关键洞察：如果能力跳跃导致 MH matching 失效，这对 31.3% headline 有系统性影响——temporal cohort 同样存在大幅能力跳跃。2023 vs 2024 cohort 的 total score 分布重叠度未报告，是关键遗漏。\"\n  action_items:\n    - round: 2\n      action: \"报告 Llama 2/3 score 分布重叠度；尝试其他 family 对比（Phi-2/3, Qwen 1/2）\"\n      assigned_to: authors\n      status: open\n    - round: 3\n      action: \"报告 2023 vs 2024 temporal cohort 的 total score 分布重叠度\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K 相关性太弱不应支撑 Claim 4 (r≈-0.47, N≈33, CI 上界 ≈-0.03)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识 Major\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 将其从 Minor 提升为 Major——GSM1K 是 Claim 4 唯一定量支撑，如不可靠则 Claim 4 基础薄弱\"\n  action_items:\n    - round: 2\n      action: \"将 GSM1K 降级为 suggestive evidence，不作为 Claim 4 主要支撑\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 与 31.3% 的叙事张力——'diagnostic lens' 缺乏 actionable follow-through\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识方向\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 建议反转 emphasis：model-specific impact 为主叙事，ρ≈0.997 为 context。R2 同意这是最有效的化解方式。\"\n  action_items:\n    - round: 3\n      action: \"将 model-specific rank shifts 提升至正文（中位数、percentiles、按 family 分组），反转叙事重心\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"技术新颖性有限——cross-subject matching 在 Clauser & Mazor (1998) / Nandakumar (1993) 先例下降级为 methodological transfer\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"DIF 方法本身无创新\"\n    - round: 2\n      reviewers: [2]\n      note: \"cross-subject matching 原理在 DIF 文献已有先例\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 最终 AGREE：cross-subject matching 从 'genuine methodological contribution' 降级为 'well-executed application of known psychometric principle'。论文剩余贡献仅为描述性发现。两位 Reviewer 均认为 ICLR main track venue fit 不理想。\"\n  action_items:\n    - round: 3\n      action: \"引用 Clauser & Mazor (1998) / Nandakumar (1993)，定位 cross-subject matching 为 application 而非 invention\"\n      assigned_to: paper_agent\n      status: open\n    - round: 3\n      action: \"考虑转投 NeurIPS D&B 或 EMNLP——两位 Reviewer 共同建议\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (CFI=0.72, 98% |Lz|>2) 可能影响 MH 统计量可靠性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Yen's Q3 需诊断\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Yen's Q3 11.3% 已提供；cross-subject matching 缓解 LD\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 Soundness 从 3/4 降至 2/4：CFI=0.72 undermines MH 分布假设。R1 维持 3/4：MH 是 nonparametric，不依赖 IRT fit + structural analysis 确认 robustness。分歧保留。\"\n  action_items:\n    - round: 2\n      action: \"对 LD 最高 5% items 做敏感性分析\"\n      assigned_to: authors\n      status: open\n    - round: 3\n      action: \"检查 LD 最高 domains 是否也是 DIF 率最高 domains\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"半合成验证 ΔFPR=0.000 过于完美，需 bootstrap CI\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"R1 提出\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 AGREE：任何 Monte Carlo 结果应有非零方差\"\n  action_items:\n    - round: 2\n      action: \"报告 ΔFPR bootstrap CI 和 random seed 数量\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"引用问题：'Tutz & Friedman (2007)' 无法核实\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Round 1 严重引用错误（已修复）\"\n    - round: 2\n      reviewers: [2]\n      note: \"新发现 Tutz & Friedman (2007)\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 AGREE：Tutz 主要合作者是 Berger (2016) 和 Schauberger (2015)，非 Friedman。可能是 citation error。\"\n  action_items:\n    - round: 2\n      action: \"核实引用\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W4\"\n  summary: \"补充分析过多（9 个中 6 个负面），稀释焦点\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识方向\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1: 'tried many things, most didn't work' 的印象使 research program 显得 premature。精选 3-4 个。\"\n  action_items:\n    - round: 3\n      action: \"精选 RL robustness + IFT + bifactor pilot 放正文，其余大幅缩减\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"与 Growing Pains 的区分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"修订版已充分讨论\"\n  action_items: []\n  resolution: \"修订版 §2 已详细对比。R1 确认。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版增加 BH 校正，31.2% vs 31.3%\"\n  action_items: []\n  resolution: \"BH 校正已添加，结果稳健。R2 确认不构成 validity threat。\"\n  resolution_round: 2\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失引用：item banking、measurement invariance、anchor selection、LLM memorization、Clauser & Mazor / Nandakumar\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Lalor/Vania/Balloccu 已补充\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"新增必引：Clauser & Mazor (1998) + Nandakumar (1993)——直接关系 cross-subject matching 的 prior art 定位\"\n  action_items:\n    - round: 3\n      action: \"必须引用 Clauser & Mazor (1998) 和 Nandakumar (1993)；补充 Stocking & Swanson 1993, Kopf 2015, Carlini 2022, Tirumala 2022\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"推理-RL 鲁棒性 N=13\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"修订版降级为补充分析，TOST inconclusive 诚实报告\"\n  action_items: []\n  resolution: \"不再作为核心贡献，降级为补充分析。缓解。\"\n  resolution_round: 2\n"
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
    "issues_yaml": "\n# Review Issues Tracker — irt_equated_bench_regen\n# Round 1: 2026-05-20 | Round 2-3: 2026-05-21 (revised paper, 3 rounds to consensus)\n\n- id: \"R1-W1\"\n  summary: \"31.3% temporal DIF 因果归因不清——~92% 未解释，无法区分污染 vs 训练范式变化 vs 能力演变\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"κ=0.14 随机水平，46% within-family overlap\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"论文成功 reframe 为 temporal instability，但因果归因仍未解决\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"共识：这是论文最根本的解释性限制。accuracy improvement 仅解释 ≤7.6%。ρ≈0.997 进一步削弱了追问 why 的 urgency。\"\n  action_items:\n    - round: 2\n      action: \"case study 20 个 C-flagged items 检查 Common Crawl 频率变化\"\n      assigned_to: authors\n      status: open\n    - round: 2\n      action: \"Discussion 中承认 instability 与 legitimate construct evolution 的不可分性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W1\"\n  summary: \"Within-family Llama 2 vs 3 的 61.3% DIF——Table 1 最高值，分析严重不足，可能暗示 MH matching 在大能力跳跃下失效\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"R1 提出 Major，R2 AGREE\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 补充关键洞察：如果能力跳跃导致 MH matching 失效，这对 31.3% headline 有系统性影响——temporal cohort 同样存在大幅能力跳跃。2023 vs 2024 cohort 的 total score 分布重叠度未报告，是关键遗漏。\"\n  action_items:\n    - round: 2\n      action: \"报告 Llama 2/3 score 分布重叠度；尝试其他 family 对比（Phi-2/3, Qwen 1/2）\"\n      assigned_to: authors\n      status: open\n    - round: 3\n      action: \"报告 2023 vs 2024 temporal cohort 的 total score 分布重叠度\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K 相关性太弱不应支撑 Claim 4 (r≈-0.47, N≈33, CI 上界 ≈-0.03)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识 Major\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 将其从 Minor 提升为 Major——GSM1K 是 Claim 4 唯一定量支撑，如不可靠则 Claim 4 基础薄弱\"\n  action_items:\n    - round: 2\n      action: \"将 GSM1K 降级为 suggestive evidence，不作为 Claim 4 主要支撑\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 与 31.3% 的叙事张力——'diagnostic lens' 缺乏 actionable follow-through\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识方向\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 建议反转 emphasis：model-specific impact 为主叙事，ρ≈0.997 为 context。R2 同意这是最有效的化解方式。\"\n  action_items:\n    - round: 3\n      action: \"将 model-specific rank shifts 提升至正文（中位数、percentiles、按 family 分组），反转叙事重心\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"技术新颖性有限——cross-subject matching 在 Clauser & Mazor (1998) / Nandakumar (1993) 先例下降级为 methodological transfer\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"DIF 方法本身无创新\"\n    - round: 2\n      reviewers: [2]\n      note: \"cross-subject matching 原理在 DIF 文献已有先例\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 最终 AGREE：cross-subject matching 从 'genuine methodological contribution' 降级为 'well-executed application of known psychometric principle'。论文剩余贡献仅为描述性发现。两位 Reviewer 均认为 ICLR main track venue fit 不理想。\"\n  action_items:\n    - round: 3\n      action: \"引用 Clauser & Mazor (1998) / Nandakumar (1993)，定位 cross-subject matching 为 application 而非 invention\"\n      assigned_to: paper_agent\n      status: open\n    - round: 3\n      action: \"考虑转投 NeurIPS D&B 或 EMNLP——两位 Reviewer 共同建议\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (CFI=0.72, 98% |Lz|>2) 可能影响 MH 统计量可靠性\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Yen's Q3 需诊断\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"Yen's Q3 11.3% 已提供；cross-subject matching 缓解 LD\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 Soundness 从 3/4 降至 2/4：CFI=0.72 undermines MH 分布假设。R1 维持 3/4：MH 是 nonparametric，不依赖 IRT fit + structural analysis 确认 robustness。分歧保留。\"\n  action_items:\n    - round: 2\n      action: \"对 LD 最高 5% items 做敏感性分析\"\n      assigned_to: authors\n      status: open\n    - round: 3\n      action: \"检查 LD 最高 domains 是否也是 DIF 率最高 domains\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"半合成验证 ΔFPR=0.000 过于完美，需 bootstrap CI\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"R1 提出\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 AGREE：任何 Monte Carlo 结果应有非零方差\"\n  action_items:\n    - round: 2\n      action: \"报告 ΔFPR bootstrap CI 和 random seed 数量\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N1\"\n  summary: \"引用问题：'Tutz & Friedman (2007)' 无法核实\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [2]\n      note: \"Round 1 严重引用错误（已修复）\"\n    - round: 2\n      reviewers: [2]\n      note: \"新发现 Tutz & Friedman (2007)\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 AGREE：Tutz 主要合作者是 Berger (2016) 和 Schauberger (2015)，非 Friedman。可能是 citation error。\"\n  action_items:\n    - round: 2\n      action: \"核实引用\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W4\"\n  summary: \"补充分析过多（9 个中 6 个负面），稀释焦点\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识方向\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1: 'tried many things, most didn't work' 的印象使 research program 显得 premature。精选 3-4 个。\"\n  action_items:\n    - round: 3\n      action: \"精选 RL robustness + IFT + bifactor pilot 放正文，其余大幅缩减\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"与 Growing Pains 的区分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"修订版已充分讨论\"\n  action_items: []\n  resolution: \"修订版 §2 已详细对比。R1 确认。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"修订版增加 BH 校正，31.2% vs 31.3%\"\n  action_items: []\n  resolution: \"BH 校正已添加，结果稳健。R2 确认不构成 validity threat。\"\n  resolution_round: 2\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失引用：item banking、measurement invariance、anchor selection、LLM memorization、Clauser & Mazor / Nandakumar\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Lalor/Vania/Balloccu 已补充\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"新增必引：Clauser & Mazor (1998) + Nandakumar (1993)——直接关系 cross-subject matching 的 prior art 定位\"\n  action_items:\n    - round: 3\n      action: \"必须引用 Clauser & Mazor (1998) 和 Nandakumar (1993)；补充 Stocking & Swanson 1993, Kopf 2015, Carlini 2022, Tirumala 2022\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"推理-RL 鲁棒性 N=13\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  mentions:\n    - round: 2\n      reviewers: [1]\n      note: \"修订版降级为补充分析，TOST inconclusive 诚实报告\"\n  action_items: []\n  resolution: \"不再作为核心贡献，降级为补充分析。缓解。\"\n  resolution_round: 2\n"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-21T07:18:26.722080+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 8156}, \"error\": \"\"}"}

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

_source line 68 · 2026-05-21T07:19:57.299789+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# 圆桌审稿报告 — Final（修订版论文，三轮收敛）\n\n**论文**: \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n**Venue**: ICLR 2026（评分量表 {0, 2, 4, 6, 8, 10}）\n**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）\n**日期**: 2026-05-21\n**轮次**: 修订版论文审稿，经 3 轮交叉讨论达成共识\n\n---\n\n## 审稿过程概述\n\n| 轮次 | R1 Overall | R2 Overall | 状态 |\n|------|-----------|-----------|------|\n| Round 1（初审） | 6/10 | 4/10 | 分歧 |\n| Round 2（交叉回应） | 5/10 | 4/10 | 缩窄 |\n| Round 3（最终收敛） | **4/10** | **4/10** | **共识** |\n\nR1 评分轨迹：6 → 5 → 4。关键转折点：\n- Round 2：R2 提出的 diagnostic lens 矛盾（31.3% + ρ≈0.997）使 R1 下调至 5\n- Round 3：Clauser & Mazor (1998) / Nandakumar (1993) 先例削弱了 cross-subject matching 的新颖性声明，论文剩余贡献仅为描述性发现，R1 最终下调至 4\n\n---\n\n## 与 Round 1 版本（\"Detection and Regeneration\"）的对比\n\n修订版相比 Round 1 审稿的原版论文有**质的提升**：\n\n| 方面 | 原版 | 修订版 | 评价 |\n|------|------|--------|------|\n| 定位 | 污染检测 | 时间不稳定性 | ✓ 认识论进步 |\n| 贡献声明 | 5 条 overclaiming | 4 条实证发现 + \"empirical, not algorithmic\" | ✓ 诚实 |\n| 引用 | 严重错误（Tets/Iron-Fenced Trees） | 已修复（仍有 Tutz & Friedman 2007 待查） | ✓ 大幅改善 |\n| 验证 | κ=0.14（失败） | Cross-subject matching + dose-response + GSM8K | ✓ 大幅改善 |\n| RL robustness | N=13 核心贡献 | TOST inconclusive，降级补充分析 | ✓ 诚实 |\n| 局部独立性 | 未检测 | Yen's Q3 (11.3%) + cross-subject matching | ✓ 大幅改善 |\n| FDR | 未提及 | Bonferroni-Holm (31.2% vs 31.3%) | ✓ 已解决 |\n\n**Round 1 的 4 个 Critical Issues**：WC1 部分解决（reframing 但因果归因未解决）；WC2 缓解（降级）；WC3 大幅改善（cross-subject matching）；WC4 大幅改善（Yen's Q3）。\n\n---\n\n## Summary\n\n本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 2023-2024 模型代际间表现出显著差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计系统排除混淆变量，提出 cross-subject matching 半合成验证框架，并论证 DIF 应作为诊断工具而非质量过滤器（ρ≈0.997）。论文明确声明 \"贡献是实证的，不是算法的\"。\n\n---\n\n## Strengths\n\n**S1. 5 种 Cohort 设计** [共识]\nTemporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）——教科书级控制变量设计。\n\n**S2. Cross-subject matching** [共识]\nWithin-subject FPR 膨胀 +0.196 → cross-subject ΔFPR≈0.000。解决了 multi-domain benchmark 上 DIF 分析的 conditional independence 陷阱。但新颖性在 Clauser & Mazor (1998) / Nandakumar (1993) purified matching 先例下需重新定位为 methodological transfer 而非 invention。\n\n**S3. Reframing 为 temporal instability** [共识]\n消除了原版最大的效度疑虑。Ground truth meta-critique（web-overlap enrichment ≈1.0）揭示了 contamination ground truth 标签的概念错位。\n\n**S4. Figure 质量** [共识]\nFigure 1 (ICC 对比) 和 Figure 2 (dose-response) 是出色的学术可视化。\n\n**S5. 多层负面控制** [共识]\nRandom split 0.18% + Yen's Q3 + Bonferroni-Holm 31.2% 排除了统计伪影。\n\n**S6. 诚实报告负面结果** [共识]\nEnsemble 0.62、item generation ρ=0.58、TOST inconclusive 均如实呈现。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**WC1. 因果归因未解决——31.3% 的 ~92% 来源不明** [共识: R1+R2]\nAccuracy improvement 仅解释 ≤7.6%。2024 模型的系统性变化（RLHF、scale、instruction tuning）可能产生 DIF 但与污染无关。描述性发现需要足够 surprising 或 actionable——如果不知道原因，practitioners 不知道该如何行动。\n\n**WC2. Within-family 61.3% 分析严重不足** [共识: R1+R2]\nTable 1 最高 DIF 率，但仅一句话解释。如果是能力跳跃导致 MH matching 失效，这对 31.3% headline 有系统性影响——temporal cohort 同样存在大幅能力跳跃。2023 vs 2024 的 total score 分布重叠度未报告。\n\n**WC3. GSM1K 证据不足支撑 Claim 4** [共识: R1+R2]\nr≈-0.47, N≈33, CI 上界 ≈-0.03。是 \"DIF as diagnostic lens\" 的唯一定量支撑，但证据太弱。\n\n**WC4. 技术新颖性不足以达到 ICLR main track bar** [共识: R1+R2]\nCross-subject matching 在 Clauser & Mazor (1998) / Nandakumar (1993) 先例下降级为 methodological transfer。论文剩余贡献为描述性发现——\"quantifying the expected\" 的价值有上限。两位 Reviewer 独立给出 Contribution 2/4。\n\n### Warning\n\n**WW1. ρ≈0.997 与 31.3% 的叙事张力** [共识]\n\"Diagnostic lens\" framing 承诺超出交付。建议反转叙事重心：model-specific rank shifts（Δ达 500+位）为主，ρ≈0.997 为 context。\n\n**WW2. IRT misspecification (CFI=0.72)** [轻微分歧: R1=3/4, R2=2/4]\nR2 认为 CFI=0.72 undermines MH 统计量分布假设；R1 认为 MH 是 nonparametric，不依赖 IRT fit，structural analysis 确认 robustness。Director 裁定：MH 不直接依赖 IRT，但 Yen's Q3 11.3% LD pairs 影响未量化，属需回应但非 fatal 的问题。\n\n**WW3. \"Tutz & Friedman (2007)\" 无法核实** [共识]\n\n**WW4. 补充分析过多（9 个中 6 个负面）** [共识]\n建议精选 3-4 个。\n\n**WW5. ΔFPR=0.000 需 bootstrap CI** [共识]\n\n---\n\n## Reviewer Consensus\n\n经三轮交叉审查，两位 Reviewer 在所有关键维度达成共识：\n\n1. **Overall 4/10** — marginally below acceptance threshold\n2. **Contribution 2/4** — 描述性发现 + 窄 methodological transfer\n3. **Soundness** — 方法论执行扎实，无 fatal flaw（R1: 3/4, R2: 2/4，轻微分歧）\n4. **Presentation 3/4** — 写作清晰诚实\n5. **Venue fit** — ICLR main track 不理想，建议 NeurIPS D&B 或 EMNLP\n6. **31.3% 因果归因** — 最大开放问题\n7. **61.3% within-family** — 最关键但最未利用的数据点\n8. **Cross-subject matching** — 论文最强贡献但新颖性被 1990s 先例削弱\n9. **论文相比原版有质的提升** — framing、严谨性、诚实度全面改善\n\n## Reviewer Divergence\n\n仅一项轻微分歧保留：\n\n**Soundness**: R1=3/4 vs R2=2/4\n- R1: MH 是 nonparametric，不依赖 IRT fit；structural analysis 确认 31% robust\n- R2: CFI=0.72 + 98% |Lz|>2 说明 2PL 在 item 级别系统性失败，影响 MH 统计量分布假设\n- **Director 裁定**: 保留分歧，不影响 Overall 共识\n\n---\n\n## Questions for Authors\n\n1. **[最高优先]** 31.3% 中能否分离 \"污染 DIF\" vs \"能力演变 DIF\"？Case study（20 个 C-flagged items + Common Crawl 频率）或 known-contaminated model pairs？\n2. **[最高优先]** Llama 2 vs 3 的 61.3%：score 分布重叠度？其他 family 对比？2023 vs 2024 temporal cohort 的 score 分布重叠度？\n3. **[高优先]** Model-specific rank shifts 完整分布（中位数、95th percentile、按 family 分组）？DIF flags 的具体 actionable use case？\n4. ΔFPR=0.000 的 bootstrap CI 和 random seed 数量？\n5. DIF-flagged items 是否集中在特定 difficulty range？\n6. LD 最高的 domains 是否也是 DIF 率最高的 domains？\n7. \"Tutz & Friedman (2007)\" 完整引用信息？\n8. Ensemble AUROC 0.62 vs 原版 0.72 的原因？\n\n---\n\n## Missing References\n\n**必须引用**（直接关系 cross-subject matching 的 prior art 定位）：\n- Clauser & Mazor (1998) — external matching variable\n- Nandakumar (1993) — purified matching subtest\n\n**建议引用**：\n- Stocking & Swanson (1993), van der Linden & Veldkamp (2004) — item banking\n- Kopf et al. (2015), Wang et al. (2012) — anchor item selection\n- Carlini et al. (2022), Tirumala et al. (2022) — LLM memorization\n\n---\n\n## External Review: 未请求\n## Visual Layout Check: 未启动\n\n---\n\n## Overall Assessment\n\n### 最终评分\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|---------------|\n| Soundness | 3/4 | 2/4 | **2.5/4** |\n| Presentation | 3/4 | 3/4 | **3/4** |\n| Contribution | 2/4 | 2/4 | **2/4** |\n| **Overall** | **4/10** | **4/10** | **4/10 (Weak Reject)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 总体判断：**Weak Reject** (4/10) — Marginally Below Acceptance Threshold\n\n**核心判断**：这是一篇方法论扎实、学术诚实的实证研究。5 种 cohort 设计优秀，cross-subject matching 有实用价值，从 \"contamination detection\" 到 \"temporal instability\" 的 reframing 是正确的认识论选择。相比原版论文有质的提升。\n\n**但无法达到 ICLR main track acceptance bar**，原因：\n1. **Contribution 偏描述性**（两位 Reviewer 共识 2/4）——31.3% 的 ~92% 来源不明，practitioners 无 actionable guidance\n2. **ρ≈0.997 削弱 urgency**——移除 31% 后排名几乎不变，检测它们的实际价值有限\n3. **Cross-subject matching 新颖性被 1990s 先例削弱**——从 \"methodological contribution\" 降级为 \"methodological transfer\"\n4. **Within-family 61.3% 未充分利用**——可能是最强实证证据但几乎未分析\n5. **\"Diagnostic lens\" 缺乏 actionable follow-through**——GSM1K 证据不足（N≈33, CI 近 0）\n\n### Venue 建议\n\n**两位 Reviewer 共同建议**：Reject from ICLR main track，with strong encouragement to resubmit at：\n- **NeurIPS 2026 Datasets & Benchmarks track**（最佳匹配）——明确欢迎 \"empirical studies that provide insights about existing benchmarks\"\n- **EMNLP 2026**——有 NLP evaluation methodology dedicated area\n\n论文质量不差——方法论 solid、写作清晰、negative results 有社区价值。问题是 venue fit，不是论文质量。\n\n### Resubmit 时的修改建议\n\n1. **分离 contamination DIF vs capability-evolution DIF**：case study + known-contaminated model pairs\n2. **反转叙事重心**：model-specific rank shifts（Δ达 500+位）为主叙事，ρ≈0.997 为 context\n3. **深入分析 within-family 61.3%**：Llama 2/3 score 分布重叠、多 family 对比\n4. **引用 Clauser & Mazor / Nandakumar**：定位 cross-subject matching 为 principled application 而非 invention\n5. **精简补充分析**至 3-4 个\n6. **将 cross-subject matching 理论化**：在什么条件下优于 standard matching？什么时候可能失败？\n7. **提供 benchmark maintenance protocol**：将 \"diagnostic lens\" 从概念转化为具体的操作指南\n",
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017",
  "force_resubmit": "True"
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
    "report": "\n# 圆桌审稿报告 — Final（修订版论文，三轮收敛）\n\n**论文**: \"Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\"\n\n**Venue**: ICLR 2026（评分量表 {0, 2, 4, 6, 8, 10}）\n**审稿组**: R1（Methods & Experiments）+ R2（Novelty & Related Work）\n**日期**: 2026-05-21\n**轮次**: 修订版论文审稿，经 3 轮交叉讨论达成共识\n\n---\n\n## 审稿过程概述\n\n| 轮次 | R1 Overall | R2 Overall | 状态 |\n|------|-----------|-----------|------|\n| Round 1（初审） | 6/10 | 4/10 | 分歧 |\n| Round 2（交叉回应） | 5/10 | 4/10 | 缩窄 |\n| Round 3（最终收敛） | **4/10** | **4/10** | **共识** |\n\nR1 评分轨迹：6 → 5 → 4。关键转折点：\n- Round 2：R2 提出的 diagnostic lens 矛盾（31.3% + ρ≈0.997）使 R1 下调至 5\n- Round 3：Clauser & Mazor (1998) / Nandakumar (1993) 先例削弱了 cross-subject matching 的新颖性声明，论文剩余贡献仅为描述性发现，R1 最终下调至 4\n\n---\n\n## 与 Round 1 版本（\"Detection and Regeneration\"）的对比\n\n修订版相比 Round 1 审稿的原版论文有**质的提升**：\n\n| 方面 | 原版 | 修订版 | 评价 |\n|------|------|--------|------|\n| 定位 | 污染检测 | 时间不稳定性 | ✓ 认识论进步 |\n| 贡献声明 | 5 条 overclaiming | 4 条实证发现 + \"empirical, not algorithmic\" | ✓ 诚实 |\n| 引用 | 严重错误（Tets/Iron-Fenced Trees） | 已修复（仍有 Tutz & Friedman 2007 待查） | ✓ 大幅改善 |\n| 验证 | κ=0.14（失败） | Cross-subject matching + dose-response + GSM8K | ✓ 大幅改善 |\n| RL robustness | N=13 核心贡献 | TOST inconclusive，降级补充分析 | ✓ 诚实 |\n| 局部独立性 | 未检测 | Yen's Q3 (11.3%) + cross-subject matching | ✓ 大幅改善 |\n| FDR | 未提及 | Bonferroni-Holm (31.2% vs 31.3%) | ✓ 已解决 |\n\n**Round 1 的 4 个 Critical Issues**：WC1 部分解决（reframing 但因果归因未解决）；WC2 缓解（降级）；WC3 大幅改善（cross-subject matching）；WC4 大幅改善（Yen's Q3）。\n\n---\n\n## Summary\n\n本文对 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）应用 Mantel-Haenszel DIF 分析，发现 31.3% 的 MMLU 题目在 2023-2024 模型代际间表现出显著差异项目功能（ETS C 类）。论文通过 5 种 cohort 设计系统排除混淆变量，提出 cross-subject matching 半合成验证框架，并论证 DIF 应作为诊断工具而非质量过滤器（ρ≈0.997）。论文明确声明 \"贡献是实证的，不是算法的\"。\n\n---\n\n## Strengths\n\n**S1. 5 种 Cohort 设计** [共识]\nTemporal（31.3%）vs ability-quintile（2.9%）vs random-split（0.18%）——教科书级控制变量设计。\n\n**S2. Cross-subject matching** [共识]\nWithin-subject FPR 膨胀 +0.196 → cross-subject ΔFPR≈0.000。解决了 multi-domain benchmark 上 DIF 分析的 conditional independence 陷阱。但新颖性在 Clauser & Mazor (1998) / Nandakumar (1993) purified matching 先例下需重新定位为 methodological transfer 而非 invention。\n\n**S3. Reframing 为 temporal instability** [共识]\n消除了原版最大的效度疑虑。Ground truth meta-critique（web-overlap enrichment ≈1.0）揭示了 contamination ground truth 标签的概念错位。\n\n**S4. Figure 质量** [共识]\nFigure 1 (ICC 对比) 和 Figure 2 (dose-response) 是出色的学术可视化。\n\n**S5. 多层负面控制** [共识]\nRandom split 0.18% + Yen's Q3 + Bonferroni-Holm 31.2% 排除了统计伪影。\n\n**S6. 诚实报告负面结果** [共识]\nEnsemble 0.62、item generation ρ=0.58、TOST inconclusive 均如实呈现。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**WC1. 因果归因未解决——31.3% 的 ~92% 来源不明** [共识: R1+R2]\nAccuracy improvement 仅解释 ≤7.6%。2024 模型的系统性变化（RLHF、scale、instruction tuning）可能产生 DIF 但与污染无关。描述性发现需要足够 surprising 或 actionable——如果不知道原因，practitioners 不知道该如何行动。\n\n**WC2. Within-family 61.3% 分析严重不足** [共识: R1+R2]\nTable 1 最高 DIF 率，但仅一句话解释。如果是能力跳跃导致 MH matching 失效，这对 31.3% headline 有系统性影响——temporal cohort 同样存在大幅能力跳跃。2023 vs 2024 的 total score 分布重叠度未报告。\n\n**WC3. GSM1K 证据不足支撑 Claim 4** [共识: R1+R2]\nr≈-0.47, N≈33, CI 上界 ≈-0.03。是 \"DIF as diagnostic lens\" 的唯一定量支撑，但证据太弱。\n\n**WC4. 技术新颖性不足以达到 ICLR main track bar** [共识: R1+R2]\nCross-subject matching 在 Clauser & Mazor (1998) / Nandakumar (1993) 先例下降级为 methodological transfer。论文剩余贡献为描述性发现——\"quantifying the expected\" 的价值有上限。两位 Reviewer 独立给出 Contribution 2/4。\n\n### Warning\n\n**WW1. ρ≈0.997 与 31.3% 的叙事张力** [共识]\n\"Diagnostic lens\" framing 承诺超出交付。建议反转叙事重心：model-specific rank shifts（Δ达 500+位）为主，ρ≈0.997 为 context。\n\n**WW2. IRT misspecification (CFI=0.72)** [轻微分歧: R1=3/4, R2=2/4]\nR2 认为 CFI=0.72 undermines MH 统计量分布假设；R1 认为 MH 是 nonparametric，不依赖 IRT fit，structural analysis 确认 robustness。Director 裁定：MH 不直接依赖 IRT，但 Yen's Q3 11.3% LD pairs 影响未量化，属需回应但非 fatal 的问题。\n\n**WW3. \"Tutz & Friedman (2007)\" 无法核实** [共识]\n\n**WW4. 补充分析过多（9 个中 6 个负面）** [共识]\n建议精选 3-4 个。\n\n**WW5. ΔFPR=0.000 需 bootstrap CI** [共识]\n\n---\n\n## Reviewer Consensus\n\n经三轮交叉审查，两位 Reviewer 在所有关键维度达成共识：\n\n1. **Overall 4/10** — marginally below acceptance threshold\n2. **Contribution 2/4** — 描述性发现 + 窄 methodological transfer\n3. **Soundness** — 方法论执行扎实，无 fatal flaw（R1: 3/4, R2: 2/4，轻微分歧）\n4. **Presentation 3/4** — 写作清晰诚实\n5. **Venue fit** — ICLR main track 不理想，建议 NeurIPS D&B 或 EMNLP\n6. **31.3% 因果归因** — 最大开放问题\n7. **61.3% within-family** — 最关键但最未利用的数据点\n8. **Cross-subject matching** — 论文最强贡献但新颖性被 1990s 先例削弱\n9. **论文相比原版有质的提升** — framing、严谨性、诚实度全面改善\n\n## Reviewer Divergence\n\n仅一项轻微分歧保留：\n\n**Soundness**: R1=3/4 vs R2=2/4\n- R1: MH 是 nonparametric，不依赖 IRT fit；structural analysis 确认 31% robust\n- R2: CFI=0.72 + 98% |Lz|>2 说明 2PL 在 item 级别系统性失败，影响 MH 统计量分布假设\n- **Director 裁定**: 保留分歧，不影响 Overall 共识\n\n---\n\n## Questions for Authors\n\n1. **[最高优先]** 31.3% 中能否分离 \"污染 DIF\" vs \"能力演变 DIF\"？Case study（20 个 C-flagged items + Common Crawl 频率）或 known-contaminated model pairs？\n2. **[最高优先]** Llama 2 vs 3 的 61.3%：score 分布重叠度？其他 family 对比？2023 vs 2024 temporal cohort 的 score 分布重叠度？\n3. **[高优先]** Model-specific rank shifts 完整分布（中位数、95th percentile、按 family 分组）？DIF flags 的具体 actionable use case？\n4. ΔFPR=0.000 的 bootstrap CI 和 random seed 数量？\n5. DIF-flagged items 是否集中在特定 difficulty range？\n6. LD 最高的 domains 是否也是 DIF 率最高的 domains？\n7. \"Tutz & Friedman (2007)\" 完整引用信息？\n8. Ensemble AUROC 0.62 vs 原版 0.72 的原因？\n\n---\n\n## Missing References\n\n**必须引用**（直接关系 cross-subject matching 的 prior art 定位）：\n- Clauser & Mazor (1998) — external matching variable\n- Nandakumar (1993) — purified matching subtest\n\n**建议引用**：\n- Stocking & Swanson (1993), van der Linden & Veldkamp (2004) — item banking\n- Kopf et al. (2015), Wang et al. (2012) — anchor item selection\n- Carlini et al. (2022), Tirumala et al. (2022) — LLM memorization\n\n---\n\n## External Review: 未请求\n## Visual Layout Check: 未启动\n\n---\n\n## Overall Assessment\n\n### 最终评分\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|---------------|\n| Soundness | 3/4 | 2/4 | **2.5/4** |\n| Presentation | 3/4 | 3/4 | **3/4** |\n| Contribution | 2/4 | 2/4 | **2/4** |\n| **Overall** | **4/10** | **4/10** | **4/10 (Weak Reject)** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### 总体判断：**Weak Reject** (4/10) — Marginally Below Acceptance Threshold\n\n**核心判断**：这是一篇方法论扎实、学术诚实的实证研究。5 种 cohort 设计优秀，cross-subject matching 有实用价值，从 \"contamination detection\" 到 \"temporal instability\" 的 reframing 是正确的认识论选择。相比原版论文有质的提升。\n\n**但无法达到 ICLR main track acceptance bar**，原因：\n1. **Contribution 偏描述性**（两位 Reviewer 共识 2/4）——31.3% 的 ~92% 来源不明，practitioners 无 actionable guidance\n2. **ρ≈0.997 削弱 urgency**——移除 31% 后排名几乎不变，检测它们的实际价值有限\n3. **Cross-subject matching 新颖性被 1990s 先例削弱**——从 \"methodological contribution\" 降级为 \"methodological transfer\"\n4. **Within-family 61.3% 未充分利用**——可能是最强实证证据但几乎未分析\n5. **\"Diagnostic lens\" 缺乏 actionable follow-through**——GSM1K 证据不足（N≈33, CI 近 0）\n\n### Venue 建议\n\n**两位 Reviewer 共同建议**：Reject from ICLR main track，with strong encouragement to resubmit at：\n- **NeurIPS 2026 Datasets & Benchmarks track**（最佳匹配）——明确欢迎 \"empirical studies that provide insights about existing benchmarks\"\n- **EMNLP 2026**——有 NLP evaluation methodology dedicated area\n\n论文质量不差——方法论 solid、写作清晰、negative results 有社区价值。问题是 venue fit，不是论文质量。\n\n### Resubmit 时的修改建议\n\n1. **分离 contamination DIF vs capability-evolution DIF**：case study + known-contaminated model pairs\n2. **反转叙事重心**：model-specific rank shifts（Δ达 500+位）为主叙事，ρ≈0.997 为 context\n3. **深入分析 within-family 61.3%**：Llama 2/3 score 分布重叠、多 family 对比\n4. **引用 Clauser & Mazor / Nandakumar**：定位 cross-subject matching 为 principled application 而非 invention\n5. **精简补充分析**至 3-4 个\n6. **将 cross-subject matching 理论化**：在什么条件下优于 standard matching？什么时候可能失败？\n7. **提供 benchmark maintenance protocol**：将 \"diagnostic lens\" 从概念转化为具体的操作指南\n",
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-21T07:20:01.668302+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4368
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-21T07:20:08.257589+00:00_

审稿报告已投递至 Research Director。

**审稿完成总结**：

- **最终评分**：4/10 Weak Reject（两位 Reviewer 共识）
- **核心结论**：方法论扎实、学术诚实的实证研究，相比原版有质的提升，但 (1) 贡献偏描述性，(2) ρ≈0.997 削弱 urgency，(3) cross-subject matching 新颖性被 1990s 先例削弱，(4) ICLR main track venue fit 不理想
- **建议**：转投 NeurIPS D&B 或 EMNLP，并在 resubmit 时深入分析 within-family 61.3%、反转叙事重心至 model-specific rank shifts、引用 Clauser & Mazor 先例
- **Issue Tracker**：已更新至 Round 3，含 5 个 open critical issues、5 个 open warnings、3 个 resolved issues

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 13

## Round 13

74 recorded events


### User

_source line 71 · 2026-05-21T15:07:30.935449+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: irt_equated_bench_regen
- 论文路径: projects/irt_equated_bench_regen/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (via ARR)
- 截止日期: 2026-05-25

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

_source line 72 · 2026-05-21T15:07:37.432524+00:00_

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

_source line 73 · 2026-05-21T15:07:37.433427+00:00_

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
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-21T15:07:45.064403+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,TodoWrite",
  "max_results": "15"
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
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch,TodoWrite",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-21T15:07:45.115115+00:00_



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

_source line 76 · 2026-05-21T15:07:49.231833+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "15"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-21T15:07:49.282483+00:00_



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

_source line 78 · 2026-05-21T15:07:57.513940+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-21T15:07:57.564640+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-21T15:08:00.575987+00:00_

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

_source line 81 · 2026-05-21T15:08:01.028396+00:00_

{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (18 个)\n\n- **plan_031_temporal_granularity**: DONE (success) — \n- **plan_030_odds_ratio**: DONE (success) — \n- **plan_027_temporal_overlap**: DONE (success) — \n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_033_subject_dif_concentration** (success): DIF 在 MMLU 57 个 subject 间分布不均匀，且 STEM vs Humanities 存在系统性差异。控制 item difficulty 和 discrimination 后，特定 subject 的 content 本身预测 DIF 概率——这说明 DIF 不仅由 psychometric properties 驱动，还受知识领域内容特征影响。同时，DIF 的方向（favor 2023 vs 2024）可能在不同领域呈现不同模式。 ← 基于 plan_001_real_data_dif_mmlu\n- **plan_032_dif_cleaned_mmlu** (success): 虽然 DIF-cleaned MMLU 的全局 rank correlation 很高 (ρ≈0.997)，但局部排名变化将揭示 DIF 的实际影响：特定模型家族（尤其是 2024 年新模型如 phi-3, llama-3）将在移除 C-flagged items 后排名显著下降，而 2023 年模型排名上升。这证明 DIF items 虽然不改变全局趋势，但系统性地偏向特定模型代际，构成 benchmark fairness 问题。 ← 基于 plan_017_downstream_impact\n  [plan_032_cleaned_mmlu_analysis](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/data/cleaned_mmlu_an
…[truncated 1289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-21T15:08:02.585885+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-21T15:08:02.987774+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/iclr2026_conference.sty
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/iclr2026_conference.bst
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/fancyhdr.sty
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/natbib.sty
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/pa
…[truncated 2139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-21T15:08:02.988251+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-21T15:08:03.640801+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit format template"
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
    "query": "ACL Rolling Review 2026 author guidelines page limit format template"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-21T15:08:08.659866+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information about EMNLP 2026 and ARR submission guide
…[truncated 1281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5671
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-21T15:08:11.520771+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit format template"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's what I found about the ACL Rolling Review 2026 author guidelines regarding page limits, formatting, and templates:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. For short papers, there is a 4-page limit for short papers.

## Additional Sections

ACL currently requires all submissions to have a section titled "Limitations", which discusses the limitations of th
…[truncated 1076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 7879
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-21T15:08:16.300742+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline commitment deadline dates"
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
    "query": "EMNLP 2026 ARR submission deadline commitment deadline dates"
  }
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-21T15:08:16.953484+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review submission dates 2026 May June cycle deadlines"
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
    "query": "ACL Rolling Review submission dates 2026 May June cycle deadlines"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-21T15:08:21.118791+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline commitment deadline dates"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here are the key submission and commitment deadline dates for EMNLP 2026:

## ARR Submission Deadline
The ARR submission deadline (long & short papers) is May 25, 2026.

## EMNLP Commitment Deadline
The EMNLP commitment deadline is August 2, 2026.

## Additional Important Dates
- Reviewer regi
…[truncated 450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 4818
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-21T15:08:22.273517+00:00_

Web search results for query: "ACL Rolling Review submission dates 2026 May June cycle deadlines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ACL Rolling Review submission dates and deadlines for the May and June 2026 cycles:

## May 2026 Cycle

Submission deadline: May 25
Reviewer registration: May 27
Reviews due: June 29
Author Response: July 7-July 13
Meta-reviews release date: July 30
Cycle End: August 2

## June 2026 Cycle

The search results do not show a June 2026 cycle listed separately. ACL switched from 8-week review cycles to 10-week cycles starting in May 2025, which means instead of 6 cycles a year there will generally be 5. The May 2026 cycle appears to b
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5320
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-21T15:08:33.920394+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "experiment_plan.yaml",
  "max_chars": "2000"
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
    "file": "experiment_plan.yaml",
    "max_chars": "2000"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-21T15:08:34.573266+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-21T15:08:34.573695+00:00_

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

_source line 95 · 2026-05-21T15:08:34.674498+00:00_

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
21	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
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
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-21T15:08:37.838902+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 97 · 2026-05-21T15:08:37.889497+00:00_



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

_source line 98 · 2026-05-21T15:08:40.951830+00:00_

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

_source line 99 · 2026-05-21T15:08:41.403953+00:00_

1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 total items), and find that 17.9--31.3\% of items exhibit large DIF (ETS Category~C; MMLU 95\% bootstrap CI: [29.4\%, 38.1\%]) between 2023 and 2024 model cohorts---knowledge/reasoning benchmarks show higher instability (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$), each 45--174$\times$ above random baselines. This does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of instability is item-specific; a Simpson's paradox in odds ratio regression confirms item properties, not accuracy gains, drive DIF. We expose a validation methodology gap: web-overlap labels measure global exposure, not differential functioning (enrichment $\approx 0.96$). A semi-synthetic injection framework with cross-subject matching preserves detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) with zero false positive inflation. DIF-flagged items concentrate cross-generational discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal), and a difficulty--direction interaction ($\rho = -0.597$) reveals that capability gains concentrate on hard items while easy items erode, suggesting DIF captures temporal construct shift rather than noise. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

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

_source line 100 · 2026-05-21T15:08:41.404376+00:00_

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

_source line 101 · 2026-05-21T15:08:42.408493+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://anonymous.4open.science/r/dif-audit}.} and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026d
…[truncated 5577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-21T15:08:42.409064+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/experiment_plan.yaml 2>/dev/null | head -50",
  "description": "Check project config for external_review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/experiment_plan.yaml 2>/dev/null | head -50",
    "description": "Check project config for external_review settings"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-21T15:08:44.266273+00:00_

experiments:
  # === P0: Headline Results (must run) ===

  - id: plan_001
    name: real_data_dif_mmlu
    claim: 1
    description: >
      Apply DIF analysis to METABENCH MMLU response matrix (5,219 models × 12,508 items).
      Data characteristics: only 37% models classifiable by family (1,929); effective temporal
      span ~1.5 years (2023: N=1,253, 2024-H1: N=656); 15.4% items have negative discrimination.
      Design:
      (a) Primary cohort: temporal split (2023 vs 2024-H1, both N≥80 ✓)
      (b) Alternative cohort: accuracy-quintile split (ability-based grouping, uses all models)
      (c) Item filtering: run with and without negative-discrimination items (sensitivity analysis)
      Run ETS C DIF detection on all items under both cohort definitions.
      Proxy validation against Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items,
      73.8% coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic
      (item exists on web), while DIF detects cohort-differential contamination (item behaves
      differently across temporal cohorts). Low concordance is EXPECTED — DIF only catches items
      where contamination is differential across cohorts, not uniform. Primary validation metric:
      FPR analysis (DIF flags on Li-et-al-clean items) rather than TPR (which conflates uniform
      vs differential contamination). Unlabeled items (26.2%) reported separately as "unknown".
      plan_011 (semi-synthetic injection) provides controlled ground truth to complement this proxy.
      (d) Within-family confound control: run DIF within model families where both versions
          have N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)
          below threshold — use as supplementary only. Identify additional qualifying pairs from
          METABENCH metadata. If DIF flags
          items that are NOT differentially contaminated within-family, the flag reflects capability
          gain, not co
…[truncated 1186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 1857
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-21T15:08:44.417242+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null; grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -10",
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
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null; grep -r \"paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/ --include=\"*.yaml\" --include=\"*.yml\" --include=\"*.json\" -l 2>/dev/null | head -10",
    "description": "Find external review config files"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-21T15:08:44.670509+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-21T15:08:50.992904+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/agent-ml-research*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0520_2/config*.yaml /home/ubuntu/agent-ml-research/config*.yaml 2>/dev/null | head -20; find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*/projects/*irt*\" 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"project_config.yaml\" 2>/dev/null | head -5",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/agent-ml-research*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0520_2/config*.yaml /home/ubuntu/agent-ml-research/config*.yaml 2>/dev/null | head -20; find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*/projects/*irt*\" 2>/dev/null | head -5; find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"project_config.yaml\" 2>/dev/null | head -5",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-21T15:08:51.998009+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-21T15:08:52.048552+00:00_

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

_source line 109 · 2026-05-21T15:08:52.049034+00:00_

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
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees 
…[truncated 5959 chars]

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

_source line 110 · 2026-05-21T15:08:52.149600+00:00_

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

_source line 111 · 2026-05-21T15:08:52.150135+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; 95\% bootstrap CI: [29.4\%, 38.1\%], $N = 1{,}000$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%. Crucially, the temporal cohort ability gap is negligible: Cohen's $d = -0.17$ (below the $|d| = 0.2$ small-effect threshold) with 76.4\% distributional overlap. Under strict 1:1 nearest-
…[truncated 10426 chars]

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

_source line 112 · 2026-05-21T15:08:57.570576+00:00_

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

_source line 113 · 2026-05-21T15:08:57.922343+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above baselines; \Cref{tab:cross_benchmark}), with knowledge/reasoning benchmarks more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). The Simpson's paradox (\Cref{sec:temporal}) confirms item properties, not accuracy gains, drive DIF. This does not invalidate ranking ($\rho \approx 0.997$) but signals measurement drift across model generations. The statistical machinery of DIF---originally designed for demographic fairness testing~\citep{holland1988mh}---transfers to temporal cohort comparisons unchanged, requiring only a binary response matrix and cohort labels.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$) exposes a category error: web-overlap labels measure global exposure shared by nearly all MMLU items, so evaluating a differential method against them conflates two phenomena.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, partial $r = -0.385$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF captures behavioral change distinct from memorization. DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), with a difficulty--direction interaction ($\rho = -0.597$): gains on hard items, erosion on easy ones. Yen's Q3 confirms local dependence does not drive DIF ($r = 0.09$, $p = 0.50$).
18	
19	\subsection{Recommended DIF Audit Protocol}
20	\label{sec:disc_protocol}
21	
22	These findings motivate a benchmark maintenance protocol: (1)~MH-DIF audits whenever $\geq 500$ new models accumulate, using cross-subject matching; (2)~C\% $> 20\%$
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-21T15:08:57.922729+00:00_

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

_source line 115 · 2026-05-21T15:08:58.424913+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	MH-DIF analysis of six METABENCH benchmarks (27,125 items, 5,227 models) reveals 17.9--31.3\% temporal item instability (ETS~C); a Simpson's paradox confirms item properties, not accuracy gains, drive DIF. Web-overlap labels are near-independent of DIF flags (enrichment $\approx 0.96$); our semi-synthetic framework validates detection power ($\Delta\mathrm{FPR} = 0.000$). DIF-flagged items concentrate discriminative information ($z{=}{-}8\sigma$ to ${-}49\sigma$) with a difficulty--direction interaction ($\rho{=}{-}0.597$): gains on hard items, erosion on easy ones. LLM benchmarks need psychometric monitoring alongside score reporting.
5	

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

_source line 116 · 2026-05-21T15:08:58.425253+00:00_

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

_source line 117 · 2026-05-21T15:08:58.977625+00:00_

1	\section*{Limitations}
2	
3	\paragraph{Methodological scope of MH-DIF.}
4	The Mantel-Haenszel procedure detects only \emph{uniform} DIF, where the odds ratio between cohorts is constant across ability strata. Logistic regression DIF analysis reveals an additional 24.8\% of items exhibiting non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% ETS~C estimate conservative. Future work should apply non-uniform DIF methods (e.g., logistic regression or IRT-based approaches) as the primary analysis to capture the full spectrum of item instability. Critically, MH-DIF is nonparametric and conditions on observed total score, not latent $\theta$---its validity does not depend on IRT model fit~\citep{holland1988mh}. Our Yen's Q3 analysis confirms that local dependence domains do not correlate with DIF domains ($r = 0.09$, $p = 0.50$), further supporting the robustness of the MH procedure in this setting.
5	
6	\paragraph{Ability confounding.}
7	Although the temporal cohort ability gap is negligible (Cohen's $d = -0.17$, overlap $= 76.4\%$) and nearest-neighbor matching confirms that at most 2.4 percentage points of C\% are attributable to ability mismatch, within-family comparisons with large ability gaps (e.g., Llama-2 vs.\ Llama-3, $d = -0.99$) produce substantially inflated C\% (61.3\% unmatched vs.\ 28.3\% matched). Any application of MH-DIF to cohorts with larger ability differences must incorporate ability matching or stratification beyond the standard 5-strata procedure.
8	
9	\paragraph{Sample size requirements.}
10	Our power analysis indicates reliable ETS~C detection requires $N \geq 80$ per cohort. The temporal cohorts (1,080 and 807 models) far exceed this threshold, but the GSM1K correlation analysis ($N = 33$) has limited statistical power (95\% CI $= [-0.71, -0.16]$). The negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$) is exploratory and warrants replication with larger model samples.
11	
12	\paragr
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-21T15:08:59.028361+00:00_

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

_source line 119 · 2026-05-21T15:08:59.079157+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (Claim~2, \Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} a
…[truncated 3597 chars]

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

_source line 120 · 2026-05-21T15:09:02.793947+00:00_

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

_source line 121 · 2026-05-21T15:09:03.848244+00:00_

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
…[truncated 5576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-21T15:09:03.999187+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10; find /home/ubuntu/agent-ml-research -name \"settings.yaml\" -o -name \"project_settings.yaml\" 2>/dev/null | head -5",
  "description": "Find project config files for external review settings"
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
    "command": "find /home/ubuntu/agent-ml-research -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10; find /home/ubuntu/agent-ml-research -name \"settings.yaml\" -o -name \"project_settings.yaml\" 2>/dev/null | head -5",
    "description": "Find project config files for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-21T15:09:04.200369+00:00_

/home/ubuntu/agent-ml-research/workspace/config/approvals.yaml
/home/ubuntu/agent-ml-research/workspace/config/projects/LLM-Calibration.yaml
/home/ubuntu/agent-ml-research/workspace/config/resources.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/aaai-2027.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/icml-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/neurips-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/acl-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/agent-ml-research/config/venue_rules/iclr-2027.yaml
/home/ubuntu/agent-ml-research/config/ralph_loop.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-21T15:09:07.864268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml"
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
    "file_path": "/home/ubuntu/agent-ml-research/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-21T15:09:09.269992+00:00_

1	typesetting:
2	  layout: two_column
3	  max_pages: 8
4	  paper_size: a4
5	  column_width_cm: 7.7
6	  text_width_cm: 16.0
7	  column_sep_cm: 0.6
8	  template_sets:
9	    hyperref: true
10	  preamble_additions:
11	    packages: [microtype, booktabs, cleveref]
12	    float_params:
13	      topfraction: "0.85"
14	      bottomfraction: "0.85"
15	      textfraction: "0.15"
16	      floatpagefraction: "0.7"
17	    penalties:
18	      widowpenalty: "10000"
19	      clubpenalty: "10000"
20	  forbidden_packages: []
21	  required_sections:
22	    - name: Limitations
23	      severity: critical
24	    - name: Ethics Statement
25	      severity: warning
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-21T15:09:09.370875+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/workspace/config/projects -name \"*irt*\" -o -name \"*bench*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10",
  "description": "Find project-specific config for irt_equated_bench_regen"
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
    "command": "find /home/ubuntu/agent-ml-research/workspace/config/projects -name \"*irt*\" -o -name \"*bench*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null | head -10",
    "description": "Find project-specific config for irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-21T15:09:09.421539+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/resources.yaml

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

_source line 128 · 2026-05-21T15:09:13.890042+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -10",
  "description": "Search for external review config in project and instance config"
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -10",
    "description": "Search for external review config in project and instance config"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-21T15:09:13.992405+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-21T15:09:27.703261+00:00_

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
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
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

_source line 131 · 2026-05-21T15:09:27.804064+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-21T15:09:31.419631+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
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
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-21T15:09:31.871826+00:00_

# Review Issues Tracker — irt_equated_bench_regen
# Round 1: 2026-05-20 | Round 2-3: 2026-05-21 (revised paper, 3 rounds to consensus)
# Action Matrix Round: 2026-05-21 (Research Director response to Final report)

- id: "R1-W1"
  summary: "31.3% temporal DIF 因果归因不清——~92% 未解释，无法区分污染 vs 训练范式变化 vs 能力演变"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 1
  last_seen_round: 3
  mentions:
    - round: 1
      reviewers: [1, 2]
      note: "κ=0.14 随机水平，46% within-family overlap"
    - round: 2
      reviewers: [1, 2]
      note: "论文成功 reframe 为 temporal instability，但因果归因仍未解决"
    - round: 3
      reviewers: [1, 2]
      note: "共识：这是论文最根本的解释性限制。accuracy improvement 仅解释 ≤7.6%。ρ≈0.997 进一步削弱了追问 why 的 urgency。"
  action_items:
    - round: 2
      action: "case study 20 个 C-flagged items 检查 Common Crawl 频率变化"
      assigned_to: authors
      status: wont_fix
    - round: 2
      action: "Discussion 中承认 instability 与 legitimate construct evolution 的不可分性"
      assigned_to: paper_agent
      status: in_progress
    - round: 4
      action: "Rebuttal: DIF psychometric tradition 不需要因果分解 (Holland & Thayer 1988); plan_023 ρ=-0.597 提供 partial causal constraint; 加 possible mechanisms 段"
      assigned_to: director
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "RD2-W1"
  summary: "Within-family Llama 2 vs 3 的 61.3% DIF + temporal cohort ability confound 可能膨胀 31.3%"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 3
  mentions:
    - round: 2
      reviewers: [1, 2]
      note: "R1 提出 Major，R2 AGREE"
    - round: 3
      reviewers: [1, 2]
      note: "R2 补充关键洞察：如果能力跳跃导致 MH matching 失效，这对 31.3% headline 有系统性影响——temporal cohort 同样存在大幅能力跳跃。2023 vs 2024 cohort 的 total score 分布重叠度未报告，是关键遗漏。"
  action_items:
    - round: 2
      action: "报告 Llama 2/3 score 分布重叠度；尝试其他 family 对比（Phi-2/3, Qwen 1/2）"
      assigned_to: authors
      status: done
    - round: 3
      action: "报告
…[truncated 8669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-21T15:09:32.023899+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check existing review reports"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-21T15:09:32.124838+00:00_

round_0.md

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

_source line 136 · 2026-05-21T15:10:08.158601+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 视觉审查派发（外部审稿未配置，跳过）', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 视觉审查派发（外部审稿未配置，跳过）', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-21T15:10:08.209672+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-21T15:10:18.200734+00:00_

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

_source line 139 · 2026-05-21T15:10:35.580037+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17379
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-21T15:10:35.731238+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **截止日期**: 2026-05-25 AoE\n- **页数限制**: 正文 8 页 + 参考文献无限制；Limitations 必须但不计入页数\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- LaTeX 源文件: `projects/irt_equated_bench_regen/paper/main.tex`（含 `sections/` 子目录）\n- PDF: `projects/irt_equated_bench_regen/paper/main.pdf`\n- 参考文献: `projects/irt_equated_bench_regen/paper/references.bib`\n\n### 论文概述\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 MMLU 31% 的 items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 differential item functioning。横跨 6 个 METABENCH benchmarks 验证（17.9%-31.3% C%）。提出 cross-subject matching 的半合成验证框架（ΔFPR=0.000）。\n\n### 你的审查侧重（必须覆盖）\n\n1. **MH-DIF 统计方法论**：\n   - MH procedure 的假设（条件独立性、能力匹配）在 LLM 上下文中是否成立？\n   - K=5 quintile stratification 是否足够？对 5,227 个 models 是否需要更细的分层？\n   - ETS C 分类阈值（|ΔMH|≥1.5 + p<0.05）的选择是否合理？threshold sensitivity 是否充分？\n\n2. **Confound Controls**：\n   - Ability confounding: Cohen's d=-0.17 是否真的 negligible？matched-ability 分析是否充分？\n   - Within-family comparison (Llama-2 vs 3, 61.3% → matched 28.3%) 的解释是否令人信服？\n   - Model family structure 对 DIF 估计的影响是否充分控制？\n\n3. **Semi-synthetic Framework**：\n   - ΔFPR=0.000 的 bootstrap CI=[0.000, 0.000] 是否可信？代数证明是否严密？\n   - Cross-subject matching 的假设和局限性\n   - 注入实验的生态效度（ecological validity）\n\n4. **实验设计与统计报告**：\n   - 样本量是否充分（power analysis 声称 N≥80）？\n   - 多重比较校正（BH FDR, 31.32%→31.30%）是否充分？\n   - Bootstrap CI 的报告是否规范？\n   - 所有 claims 是否有充分的统计支撑？\n\n5. **格式合规**（辅助）：\n   - 正文是否超过 8 页？\n   - 是否存在匿名性泄露？\n   - Limitations 章节是否存在且合理？\n\n请按照 EMNLP/ARR 审稿标准，从 Soundness、Excitement、Reproducibility、Clarity 四个维度评分（1-5），并提供 Overall Assessment（1-5，0.5 步长）。\n\n将问题分为 Must-Fix（接收前必须解决）和 Should-Fix（建议改进）两类。"
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
    "project": "irt_equated_bench_regen",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **截止日期**: 2026-05-25 AoE\n- **页数限制**: 正文 8 页 + 参考文献无限制；Limitations 必须但不计入页数\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- LaTeX 源文件: `projects/irt_equated_bench_regen/paper/main.tex`（含 `sections/` 子目录）\n- PDF: `projects/irt_equated_bench_regen/paper/main.pdf`\n- 参考文献: `projects/irt_equated_bench_regen/paper/references.bib`\n\n### 论文概述\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 MMLU 31% 的 items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 differential item functioning。横跨 6 个 METABENCH benchmarks 验证（17.9%-31.3% C%）。提出 cross-subject matching 的半合成验证框架（ΔFPR=0.000）。\n\n### 你的审查侧重（必须覆盖）\n\n1. **MH-DIF 统计方法论**：\n   - MH procedure 的假设（条件独立性、能力匹配）在 LLM 上下文中是否成立？\n   - K=5 quintile stratification 是否足够？对 5,227 个 models 是否需要更细的分层？\n   - ETS C 分类阈值（|ΔMH|≥1.5 + p<0.05）的选择是否合理？threshold sensitivity 是否充分？\n\n2. **Confound Controls**：\n   - Ability confounding: Cohen's d=-0.17 是否真的 negligible？matched-ability 分析是否充分？\n   - Within-family comparison (Llama-2 vs 3, 61.3% → matched 28.3%) 的解释是否令人信服？\n   - Model family structure 对 DIF 估计的影响是否充分控制？\n\n3. **Semi-synthetic Framework**：\n   - ΔFPR=0.000 的 bootstrap CI=[0.000, 0.000] 是否可信？代数证明是否严密？\n   - Cross-subject matching 的假设和局限性\n   - 注入实验的生态效度（ecological validity）\n\n4. **实验设计与统计报告**：\n   - 样本量是否充分（power analysis 声称 N≥80）？\n   - 多重比较校正（BH FDR, 31.32%→31.30%）是否充分？\n   - Bootstrap CI 的报告是否规范？\n   - 所有 claims 是否有充分的统计支撑？\n\n5. **格式合规**（辅助）：\n   - 正文是否超过 8 页？\n   - 是否存在匿名性泄露？\n   - Limitations 章节是否存在且合理？\n\n请按照 EMNLP/ARR 审稿标准，从 Soundness、Excitement、Reproducibility、Clarity 四个维度评分（1-5），并提供 Overall Assessment（1-5，0.5 步长）。\n\n将问题分为 Must-Fix（接收前必须解决）和 Should-Fix（建议改进）两类。"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-21T15:10:54.778151+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19046
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-21T15:10:54.979427+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 相关工作）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **截止日期**: 2026-05-25 AoE\n- **页数限制**: 正文 8 页 + 参考文献无限制；Limitations 必须但不计入页数\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- LaTeX 源文件: `projects/irt_equated_bench_regen/paper/main.tex`（含 `sections/` 子目录）\n- PDF: `projects/irt_equated_bench_regen/paper/main.pdf`\n- 参考文献: `projects/irt_equated_bench_regen/paper/references.bib`\n\n### 论文概述\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 MMLU 31% 的 items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 differential item functioning。横跨 6 个 METABENCH benchmarks 验证（17.9%-31.3% C%）。提出 cross-subject matching 的半合成验证框架（ΔFPR=0.000）。论文声称 4 个贡献：temporal comparability、ground truth meta-critique、semi-synthetic validation framework、DIF as diagnostic lens。\n\n### 你的审查侧重（必须覆盖）\n\n1. **新颖性评估**：\n   - MH-DIF 是 1988 年的经典方法，cross-subject matching 在 DIF 文献中有先例（Clauser & Mazor 1998, Nandakumar 1993）——本文的 methodological novelty 到底在哪里？\n   - 4 个 claims 是否都算得上 genuine contributions，还是更多是 descriptive findings？\n   - 对于 EMNLP 2026 main conference 来说，novelty 是否足够？还是更适合 Findings？\n\n2. **Related Work 覆盖**：\n   - DIF 方法论文献（Holland & Thayer 1988, Clauser & Mazor 1998, Nandakumar 1993, Swaminathan & Rogers 1990 等）引用是否充分？\n   - LLM evaluation 相关工作（IRT-based, contamination detection, dynamic benchmarks）覆盖是否全面？\n   - 与 Growing Pains (Habba et al. 2026) 的区分是否清晰？\n   - 是否遗漏重要相关工作？请用 web search 检查近期相关论文。\n\n3. **叙事完整性与逻辑**：\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的叙事弧是否连贯？\n   - ρ≈0.997（排名几乎不变）与 31.3%（近三分之一 items 不稳定）之间的张力如何处理的？叙事是否令人信服？\n   - \"diagnostic lens, not quality filter\" 的 framing 是否有说服力？\n   - Claim 4（DIF as diagnostic lens）的支撑是否足够强？\n\n4. **Writing Quality**：\n   - 语言是否清晰、精准？\n   - 技术术语对 NLP 读者是否友好（考虑 EMNLP 受众）？\n   - 信息密度是否合适？是否有冗余或缺失？\n\n5. **Missing References**：\n   - 用 web search 检查是否有 2025-2026 年的重要相关工作未被引用\n   - 特别关注：benchmark contamination、IRT for LLM、measurement invariance 领域的最新工作\n\n6. **格式与合规**（辅助）：\n   - 引用格式是否正确（natbib/ACL style）？\n   - 是否有匿名性泄露？\n   - Ethics Statement 是否需要？\n\n请按照 EMNLP/ARR 审稿标准，从 Soundness、Excitement、Reproducibility、Clarity 四个维度评分（1-5），并提供 Overall Assessment（1-5，0.5 步长）。\n\n将问题分为 Must-Fix（接收前必须解决）和 Should-Fix（建议改进）两类。"
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
    "project": "irt_equated_bench_regen",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 相关工作）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (via ACL Rolling Review)\n- **截止日期**: 2026-05-25 AoE\n- **页数限制**: 正文 8 页 + 参考文献无限制；Limitations 必须但不计入页数\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n- LaTeX 源文件: `projects/irt_equated_bench_regen/paper/main.tex`（含 `sections/` 子目录）\n- PDF: `projects/irt_equated_bench_regen/paper/main.pdf`\n- 参考文献: `projects/irt_equated_bench_regen/paper/references.bib`\n\n### 论文概述\n本文将教育测量中的 Mantel-Haenszel DIF 分析应用于 LLM benchmark 评估，发现 MMLU 31% 的 items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 differential item functioning。横跨 6 个 METABENCH benchmarks 验证（17.9%-31.3% C%）。提出 cross-subject matching 的半合成验证框架（ΔFPR=0.000）。论文声称 4 个贡献：temporal comparability、ground truth meta-critique、semi-synthetic validation framework、DIF as diagnostic lens。\n\n### 你的审查侧重（必须覆盖）\n\n1. **新颖性评估**：\n   - MH-DIF 是 1988 年的经典方法，cross-subject matching 在 DIF 文献中有先例（Clauser & Mazor 1998, Nandakumar 1993）——本文的 methodological novelty 到底在哪里？\n   - 4 个 claims 是否都算得上 genuine contributions，还是更多是 descriptive findings？\n   - 对于 EMNLP 2026 main conference 来说，novelty 是否足够？还是更适合 Findings？\n\n2. **Related Work 覆盖**：\n   - DIF 方法论文献（Holland & Thayer 1988, Clauser & Mazor 1998, Nandakumar 1993, Swaminathan & Rogers 1990 等）引用是否充分？\n   - LLM evaluation 相关工作（IRT-based, contamination detection, dynamic benchmarks）覆盖是否全面？\n   - 与 Growing Pains (Habba et al. 2026) 的区分是否清晰？\n   - 是否遗漏重要相关工作？请用 web search 检查近期相关论文。\n\n3. **叙事完整性与逻辑**：\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的叙事弧是否连贯？\n   - ρ≈0.997（排名几乎不变）与 31.3%（近三分之一 items 不稳定）之间的张力如何处理的？叙事是否令人信服？\n   - \"diagnostic lens, not quality filter\" 的 framing 是否有说服力？\n   - Claim 4（DIF as diagnostic lens）的支撑是否足够强？\n\n4. **Writing Quality**：\n   - 语言是否清晰、精准？\n   - 技术术语对 NLP 读者是否友好（考虑 EMNLP 受众）？\n   - 信息密度是否合适？是否有冗余或缺失？\n\n5. **Missing References**：\n   - 用 web search 检查是否有 2025-2026 年的重要相关工作未被引用\n   - 特别关注：benchmark contamination、IRT for LLM、measurement invariance 领域的最新工作\n\n6. **格式与合规**（辅助）：\n   - 引用格式是否正确（natbib/ACL style）？\n   - 是否有匿名性泄露？\n   - Ethics Statement 是否需要？\n\n请按照 EMNLP/ARR 审稿标准，从 Soundness、Excitement、Reproducibility、Clarity 四个维度评分（1-5），并提供 Overall Assessment（1-5，0.5 步长）。\n\n将问题分为 Must-Fix（接收前必须解决）和 Should-Fix（建议改进）两类。"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-21T15:10:56.538680+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1559
}
```

</details>

---


### Assistant

_source line 144 · 2026-05-21T15:11:03.264893+00:00_

已并行派发：
- **视觉审查 Agent** — 已启动，fire-and-forget
- **Reviewer 1**（方法严谨性 + 实验设计）— 已分配
- **Reviewer 2**（新颖性 + 完整性 + 相关工作）— 已分配

等待两位 Reviewer 完成 Round 1 独立审稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 14

## Round 14

2 recorded events


### User

_source line 145 · 2026-05-21T15:22:48.938996+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 扎实的实证研究，将经典 DIF 方法成功移植到 LLM benchmark 评估领域，发现本身有实际价值，但方法论新颖性有限，核心贡献偏 descriptive，介于 main conference 和 Findings 之间。

---

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 (Strong) | 方法执行扎实：5 种 cohort design、3 层结构控制（matched-ability quintile、IRT θ-conditioning、random-split）、cross-benchmark 6 基准复现。Semi-synthetic validation 的 ΔFPR=0.000 令人信服。但 Claim 4 支撑偏弱，temporal cohort 定义需要更多论证。 |
| Excitement | 3/5 (Interesting) | 发现有实际意义——31% item instability 对 benchmark 使用者是有用的警示。但核心方法是 1988 年 MH-DIF 的直接应用，4 个 claimed contributions 中 3 个是 empirical findings 而非方法创新。对 EMNLP main 来说新颖性偏弱。 |
| Reproducibility | 4/5 | 使用公开数据（METABENCH）、提供匿名代码仓库（footnote 1）、方法描述详尽。Semi-synthetic injection 的 5 seed × 5 subject 设计可复现。唯一缺憾是 METABENCH 原始 response matrix 的版本锁定未明确说明。 |
| Clarity | 4/5 | 写作整体清晰、结构合理。Figure 1 的 ICC 图直观展示了 global vs. differential contamination 的区别。但 DIF 术语（ETS Category A/B/C、MH odds ratio）对 NLP 读者不够友好，Section 3.2 的公式密度较高。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Claim 4 "DIF as diagnostic lens" 支撑不足
- 具体位置：Section 4.6, Section 5.3, Page 7-8
- 问题：论文声称 DIF-flagged items "concentrate discriminative information"（ε = −8ε to −12ε vs. random removal），但 Section 5.3 的 GSMIK correlation (r = −0.478, partial r = −0.385) 只是 moderate negative correlation，且 Section 4.6 承认 "aggregate model ordering is preserved despite 31% item instability"。这就产生了一个逻辑困境：如果去掉 DIF items 后排名几乎不变（ρ ≈ 0.997），那说 DIF items "concentrate discriminative information" 的实际意义是什么？论文试图用 "diagnostic lens, not quality filter" 来化解，但 Claim 4 本身作为一个独立 contribution 的证据不够强——GSMIK 只在 GSM8K 的 33 个 model 上验证（N=33），样本极小，且 partial correlation 只有 0.385。
- 为什么影响接收：4 个 contribution 中如果有 1 个站不住，paper 的贡献度打折扣。Reviewer 会质疑 contribution list 是否 inflated。
- 建议修改方向：要么(a) 补充更强的证据（如在 MMLU 全量数据上做 DIF-based item selection 对比实验），要么(b) 降级 Claim 4 为 observation/finding 而非 contribution，将 contribution list 收紧为 3 个。

**N2** [critical] 方法论新颖性论证不充分——"transplant" 的附加价值需要更明确
- 具体位置：Section 1 (Introduction), Section 2 (Related Work), Section 3 (Method)
- 问题：MH-DIF 是 Holland & Thayer (1988) 的经典方法；cross-subject matching 在 DIF 文献中有先例（论文自己在 Page 3 承认 "Cross-subject matching... has psychometric precedent in the DIF literature (Nandakumar, 1993; Donoghue and Allen, 1993)"）。论文的 4 个 contributions 中，Claim 1（31% instability）和 Claim 2（ground truth meta-critique）本质上是 descriptive findings from applying known methods，Claim 3（semi-synthetic framework）是对已有 DIF validation 技术的适配。论文需要更清晰地论证：相比直接在 LLM 数据上跑标准 MH-DIF，本文的 methodological adaptation 具体解决了什么新问题？
- 为什么影响接收：EMNLP main conference 对 novelty 有较高要求。如果 reviewer 认为这只是 "apply off-the-shelf method to new domain + report findings"，可能被降到 Findings。
- 建议修改方向：(a) 在 Introduction 中更明确地 argue "为什么 DIF 不能直接搬过来"——比如 LLM 作为 examinees 与人类的本质差异（确定性 response、无 guessing、extreme ability range）如何影响 MH-DIF 的假设；(b) 强调 semi-synthetic validation 的必要性——因为在 LLM 场景下没有 ground truth DIF（不像人类测试有已知的 demographic groups），所以 cross-subject matching + controlled injection 是一个非平凡的验证方案；(c) 明确 position 为 "empirical contribution" 而非 "methodological contribution"，让 reviewer 按正确的标准评价。

**N3** [critical] Temporal cohort 定义过于粗糙，可能混淆多种因素
- 具体位置：Section 3.3 (Cohort Designs), Section 5.1, Limitations (Page 8-9)
- 问题：以 calendar year（2023 vs 2024）划分 cohort 是一个粗糙的操作变量。同一年份内模型差异巨大（如 2024 初的模型可能与 2023 末的模型更相似）；不同家族（Llama vs GPT vs Mistral）的训练方法论差异可能远大于时间差异。虽然论文尝试了 Ability-quintile（Cohort 2）、Within-family（Cohort 3）、Within-subject DIF（Cohort 4）等多种 cohort design，并在 Appendix 提到 6-month window check，但主要结果（31.3%）仍基于 calendar year cohort。这使得 "temporal comparability" 这个 framing 存疑——DIF 检测到的可能是 training methodology shift 或 architecture shift 而非纯粹的 temporal effect。
- 为什么影响接收：这是对核心 claim 解释力的挑战。如果 DIF 主要反映的是 model family 差异而非 temporal drift，则 "temporal comparability" 的 narrative 需要调整。
- 建议修改方向：(a) 补充 within-year cohort 分析（如 2024-H1 vs 2024-H2）的完整结果，不只是 Appendix mention；(b) 更明确地讨论 confound 的 decomposition——architectural heterogeneity（Section 5.1 提到 "99.98% decoder-only" 但 Llama vs Mistral vs GPT 仍然很不同）vs. temporal effect vs. training data shift；(c) 考虑改 framing 为 "cross-cohort DIF" 而非 "temporal comparability"，因为 cohort 定义本身承载了多种变异源。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] ρ ≈ 0.997 vs. 31.3% 张力的叙事虽有，但未充分说服
- 具体位置：Section 4.6, Section 5.1, Abstract
- 问题：Abstract 说 "This does not threaten benchmark validity: Spearman rank correlation (ρ ≈ 0.997 between full and stable-item rankings)"。但论文同时声称 31.3% items 有 ETS C 级 DIF。一个自然的反应是：如果排名不变，那 DIF 有什么实际影响？论文用 "Simpson's paradox"（Section 4.4）和 "diagnostic lens"（Section 5.3）来回应，但读者可能会问：如果整体评价不受影响，这个发现的 actionability 在哪里？Section 5.4 提出了 "DIF Audit Protocol" 但只有 3 句话，过于简略。
- 建议：扩展 Section 5.4，给出更具体的 actionable recommendations（如：benchmark 维护者应该多久做一次 DIF audit？发现高 C% 后的具体处理流程是什么？DIF-cleaned scores 是否应该作为补充报告？）

**W2** [warning] Semi-synthetic validation 的 ΔFPR = 0.000 需要更多讨论
- 具体位置：Section 3.4, Section 4.5, Figure 3
- 问题：ΔFPR = 0.000 across all 5 MMLU subjects 看起来过于完美。虽然这说明 cross-subject matching 有效消除了 false positive inflation，但 (a) 注入率固定为 20%，没有测试更低注入率（如 5%、10%）下的表现；(b) N = 5 subjects 是否足够？MMLU 有 57 个 subjects，只在 5 个上验证 generalizability 有限；(c) 论文没有讨论 Type II error（漏检率）——如果 cross-subject matching 过于保守，可能也会降低 detection power。
- 建议：补充更多 injection rate 和 subjects 的实验，至少讨论 Type II error 的可能性。

**W3** [warning] DIF 术语对 EMNLP 读者不够友好
- 具体位置：Section 3.2 (Method), throughout
- 问题：ETS Category A/B/C、α_MH、Δ_MH 等术语对 NLP 社区读者较为陌生。虽然 Section 3.2 提供了数学定义，但缺少直观解释。例如，|Δ_MH| ≥ 1.5 对应多大的实际效应？ETS C 在教育测量中意味着什么样的实际偏差？Figure 1 帮助了理解，但正文中的 terminology introduction 可以更 reader-friendly。
- 建议：在 Section 3.2 加一个 running example（如用一个具体 MMLU item 展示 DIF 计算过程和 ETS 分类），帮助非 psychometrics 背景的读者。

**W4** [warning] 与 Growing Pains (Habba et al., 2026) 的区分可以更深入
- 具体位置：Section 2 (Related Work, Page 3)
- 问题：论文说 "Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption"。这个区分是清晰的，但过于简短。具体来说：(a) Growing Pains 用 FPC 做 benchmark extension，本文用 MH-DIF 做 benchmark diagnosis——两者的输入数据和分析单元有何异同？(b) 如果 DIF 发现 31% items 不稳定，这对 Growing Pains 的 FPC anchor 假设意味着什么？论文是否验证了 DIF-flagged items 与 Growing Pains 的 anchor items 的 overlap？这本身就是一个很有价值的实验。
- 建议：补充与 Growing Pains 的直接实证对比（如 anchor item overlap 分析），或者至少在 Discussion 中更详细地讨论。

**W5** [warning] 部分引用信息有误
- 具体位置：references.bib
- 问题：引用验证发现若干问题：
  - `holland1988mh`：year mismatch（bib=1988，原始出版可能是 1986）
  - `tao2026selfcritique`：first author mismatch（bib=Tao，API=Yongding）
  - `liu2026bhi`：first author mismatch（bib=Liu，API=Zhu）——Benchmark Health Index 的第一作者应为 Zhu 而非 Liu
  - 8 个 orphan bib entries（在 .bib 中但未被引用）：chen2025irtnet, choi2026llmjudgeirt, li2025atlas, liang2023helm, mialon2023gaia, ott2022benchmark, wang2024mmlupro, zhang2024gsm1k
- 建议：修正 author/year mismatches，清理 orphan entries。

---

## 小问题（不影响接收）

1. **Page 1, footnote 1**: 匿名 URL 格式正确，但请确保不包含可去匿名化的信息。
2. **Page 5, Section 3.4**: "We flip incorrect responses to correct in the focal group at exploitation rate p" — "exploitation rate" 这个术语不标准，建议改为 "injection rate" 或 "manipulation rate"。
3. **Page 7, Section 4.6**: "Spearman correlation between full and stable-item rankings is ρ ≈ 0.997" — 此处应报告 confidence interval 或 p-value。
4. **Page 8, Limitations**: "The Mantel-Haenszel procedure detects only uniform DIF" — 这是一个合理的 limitation，但建议提一句 logistic regression DIF 作为 future work 可检测 non-uniform DIF。
5. **Table 1**: C% 和 Ratio 列的格式不完全一致（有的有 ± 号有的没有）。
6. **Page 6**: "the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection" — 这个论断需要 citation 支持，不能仅凭断言。
7. **Appendix Figure 4**: 横轴 label 字体偏小，不易阅读。

---

## Missing References（可能遗漏的重要相关工作）

1. **"Lifting the Benchmark Iceberg with Item-Response Theory"** (2025, OpenReview) — 用 IRT 揭示 benchmark 实现细节对排名的影响，与本文"benchmark 内部 item 不稳定"的发现高度相关，应在 Related Work 中讨论。
2. **"Benchmark2: Systematic Evaluation of LLM Benchmarks"** (2025, arXiv:2601.03986) — 系统评估 LLM benchmark 质量的框架，与本文的 meta-critique 视角互补。
3. **CAT-based LLM evaluation** (如 Li et al. 2025 ATLAS, 已在 bib 但未引用) — Computerized Adaptive Testing 是 IRT 的自然延伸，与本文 "item-level diagnosis" 的理念相关。建议在 Related Work 中 cite 并讨论。
4. **MedIRT / "Measuring Competency, Not Performance"** (2025, arXiv:2509.24186) — 将 IRT 应用于医学 benchmark 评估，与本文方法论相近但领域不同。

---

## 主要优势

1. **规模和严谨性**：5,227 models × 12,508 items 的分析规模在该领域是最大的之一；5 种 cohort design + 3 层结构控制展现了扎实的方法论。
2. **发现的实际价值**：31% item instability 是一个对 benchmark 使用者有直接意义的发现；cross-benchmark 复现（6 benchmarks, 17.9%–31.3%）增强了可信度。
3. **Ground truth meta-critique**（Section 4.3）：发现 DIF flags 与 web-overlap contamination labels 几乎独立（enrichment ≈ 0.964, Jaccard = 0.206），这是对现有 contamination detection 文献的重要补充——说明 DIF 捕捉到的不是表面的 memorization 而是更深层的 behavioral shift。
4. **Semi-synthetic framework**：cross-subject matching + controlled injection 的验证方案在 LLM 场景下是一个有价值的方法论贡献（因为 LLM 没有 demographic groups 作为 natural DIF reference）。
5. **叙事处理**：ρ ≈ 0.997 vs 31.3% 的张力处理得当——"diagnostic lens, not quality filter" 的 framing 避免了过度 alarmist 的论调，Simpson's paradox 分析增加了深度。

---

## 总结性判断

这是一篇 well-executed 的实证研究，核心发现（31% MMLU items 跨代不稳定）有实际价值，方法论执行严谨。主要短板是：(1) 方法论新颖性有限——MH-DIF 是 off-the-shelf method，论文需要更好地论证 transplant 的非平凡性；(2) Claim 4 支撑不够强；(3) temporal cohort 定义的 confound 问题需更深入讨论。

如果 N1-N3 得到有效 address（特别是 N2 的 novelty framing），论文有望达到 main conference 水平。目前定位为 strong Findings / borderline Conference。

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

_source line 146 · 2026-05-21T15:23:04.283131+00:00_

Reviewer 2 的 Round 1 报告已收到。评分 3.5（Borderline Conference），核心问题：N1 Claim 4 支撑不足、N2 方法论新颖性论证不充分、N3 temporal cohort 定义粗糙。

等待 Reviewer 1 的报告，两份齐全后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 15

## Round 15

8 recorded events


### User

_source line 147 · 2026-05-21T15:23:05.405091+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**摘要**：Overall 3.5（Borderline Conference），Soundness 4/5，Excitement 3/5。

3 个 Must-Fix：
- **N1**: Claim 4（DIF as diagnostic lens）证据不足——GSMIK 只有 N=33，partial r=0.385
- **N2**: 方法论新颖性论证不充分——需要明确 MH-DIF transplant 解决了什么 LLM-specific 新问题
- **N3**: Temporal cohort 定义（calendar year）过于粗糙，可能混淆 architecture/training methodology shift

5 个 Should-Fix：ρ≈0.997 vs 31.3% 张力的 actionability 不足、ΔFPR=0.000 过于完美缺少 robustness check、DIF 术语不够 NLP-friendly、与 Growing Pains 的区分过于简略、若干引用信息有误（8 orphan entries + author/year mismatches）。

4 个 potentially missing references: "Lifting the Benchmark Iceberg"、Benchmark2、ATLAS (CAT-based)、MedIRT。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计）

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 将教育测量中成熟的 MH-DIF 方法大规模应用于 LLM benchmark 是有新意的实证贡献，但半合成验证框架的生态效度存在根本性缺陷，且核心发现（31% instability）的因果解释力不足——论文未能令人信服地区分"psychometric instability"与"expected capability evolution"。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | MH-DIF 的应用本身合理，多重控制实验充分，但 Proposition 1 是 trivially true by construction，semi-synthetic 框架仅验证 subject-localized contamination 这一特殊情形；ability confounding 的控制虽有说服力（matched C%≈28-29%），但 Q3 局部依赖对主分析的影响未量化 |
| Excitement | 3.5 / 5 | 跨学科应用（psychometrics → NLP evaluation）有新意，6 个 benchmark 的大规模验证具说服力，ground truth meta-critique（Claim 2）对 contamination detection 文献有实际启示；但核心 DIF 数字更多是描述性发现而非可操作的方法论突破 |
| Reproducibility | 4 / 5 | 使用公开 METABENCH 数据，提供匿名代码链接，方法描述详尽（K=5 分层、ETS 分类标准、bootstrap 参数均有报告）；power analysis 的假设参数可更透明 |
| Clarity | 4 / 5 | 写作清晰，结构合理，Figure 1 对 global vs. differential contamination 的区分直观有效；但 Abstract 过于密集（信息量堆叠），Limitations 涵盖较全面 |

**Reviewer Confidence**: 4 / 5（熟悉 DIF 方法论和 LLM evaluation 文献，仔细通读全文及附录）

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 半合成验证框架的生态效度（Ecological Validity）存在根本缺陷
- 具体位置：Section 3.4, Proposition 1 (p.5), Section 4.5 (p.7)
- 问题：Proposition 1 声称 cross-subject matching 实现 ΔFPR=0.000，但这是 **by construction** 的平凡结果——contamination 被注入 subject X 的 items，matching variable 排除了 subject X，因此注入信号在数学上无法泄漏到 matching variable 中。论文将此作为 Claim 3 的核心贡献呈现，但实际上它只验证了**单一 subject 被污染**的特殊情形。在现实场景中，LLM 训练语料包含所有 MMLU subjects 的 items，contamination 会**同时跨越多个 subjects** 发生。此时 cross-subject matching variable 本身也被污染，Proposition 1 的保证不再成立。论文未测试 multi-subject simultaneous injection（例如同时污染 3-5 个 subjects 后看 FPR 是否仍为 0），因此无法评估框架在现实条件下的有效性。
- 为什么影响接收：Semi-synthetic 框架是论文验证 31.3% temporal C% 非假阳性的核心证据之一（Section 4.3 用 dose-response 论证 detection power）。如果框架仅在 unrealistic 条件下有效，则论文缺乏充分的 false positive rate 控制，31.3% 的可信度下降。
- 建议修改方向：(1) 补充 multi-subject simultaneous injection 实验（例如随机选择 k∈{2,3,5,10} 个 subjects 同时注入，报告 ΔFPR 随 k 的变化）；(2) 或将 Claim 3 显式限定为 subject-localized contamination 场景，并讨论对 temporal DIF 解读的影响。

**N2** [critical] 核心发现的因果模糊性：「Psychometric Instability」vs.「Expected Capability Evolution」
- 具体位置：Title, Abstract, Section 4.2 (p.6), Section 5.3 (p.8)
- 问题：论文发现 DIF 呈现系统性的 difficulty-direction interaction（ρ=-0.597, Section 5.3）：2024 模型在难题上 gain、简单题上 erode。论文将此解读为"temporal construct shift"的证据，但这个 pattern 同样（甚至更自然地）可以解释为**正常的 capability evolution**——新一代模型推理能力提升导致难题表现改善，而 training distribution 变化导致简单 factual recall 题表现下降。MH-DIF 在设计上会将**任何**跨组 item functioning 差异标记为 DIF，包括 genuine capability change。论文标题使用"Psychometric Instability"暗示这是一个 benchmark 的测量问题，但如果 31% 的 DIF 主要反映模型能力的合理演变，则这不是"instability"而是"expected differential performance"。论文在 Limitations 中承认"DIF detects that... not why"，但 framing 从标题到结论均倾向于"instability"的负面解读。
- 为什么影响接收：论文的主要 narrative（"LLM benchmarks need psychometric monitoring"）依赖于将 DIF 解读为测量问题而非能力变化。如果 DIF 主要捕获的是 expected capability evolution，则 policy implication 需要根本性修改。
- 建议修改方向：(1) 明确区分 "item instability"（item 本身测量属性变化）和 "differential performance"（模型能力变化导致的 item 行为差异）；(2) 通过分析 DIF 方向与 item content 特征（如 knowledge domain recency, reasoning depth）的关系，提供更强的证据来区分这两种解释；(3) 至少软化标题中 "Instability" 的表述，改为更中性的 "Differential Functioning" 或 "Measurement Drift"。

**N3** [critical] Bootstrap CI 的不对称性与 headline 数字的精确度
- 具体位置：Section 4.2 (p.6), Abstract
- 问题：MMLU C% 的 95% bootstrap CI 为 [29.4%, 38.1%]，宽度 8.7pp，上尾明显偏重（31.3% → 38.1% 的距离是到下界的 3.6 倍）。论文以 "31%" 作为标题和全文 headline 数字，但 CI 表明真实值可能高达 38%。更重要的是：论文未报告 bootstrap 的 resampling unit（是 resample models 还是 items？），这影响 CI 的解读。如果 resample models，CI 反映 model sampling variability，说明结论对 model population 的代表性有不确定性；如果 resample items，CI 反映 item sampling variability。此外，CI 的不对称性暗示 C% 分布是 right-skewed 的，论文应解释原因。
- 为什么影响接收：Headline 数字 "31%" 是论文所有下游分析和 policy recommendations 的基础。如果 CI 表明结果对 model/item 抽样高度敏感，需要更谨慎的表述。
- 建议修改方向：(1) 明确报告 bootstrap resampling unit 和策略（model-level vs. item-level vs. block bootstrap）；(2) 在 Abstract 和 Title 中使用 CI 或至少用 "approximately 31%" 表述；(3) 解释 CI 不对称性的来源。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] K=5 分层的敏感性分析不足
- 具体位置：Section 3.2 (p.4)
- 问题：论文选择 K=5 quintile stratification，引用 ETS recommended practice（Donoghue 1993, Clauser 1998）。这些推荐针对的是 human test-takers（通常 N=几百到几千），而本文 N=5,227 models 远超典型教育测评场景。论文在 Appendix B 报告了 IRT θ-conditioning with 20 strata（FPR=0.312，与 K=5 几乎相同），这部分回应了 K 的选择问题。但论文应在主文中明确报告 K=5 vs. K=10 vs. K=20 的 C% 对比，而非仅在附录中隐式提及。
- 建议：在 Section 4.2 或 Table 1 中增加一行 K 的 sensitivity analysis。

**W2** [warning] Yen's Q3 局部依赖对主分析的影响未量化
- 具体位置：Appendix A.1 (p.11), Appendix B (p.12)
- 问题：11.3% 的 within-subject item pairs 超过 |Q3|>0.20 阈值（vs. cross-subject 2.2%，5× ratio，p=2.3×10⁻⁹）。MH 程序假设 conditional independence given matching variable。虽然主分析使用 total score（across all 12,508 items）作为 matching variable，subject-specific dependence 的影响被稀释，但论文未提供定量估计——例如通过 simulation 评估 11.3% Q3 violation rate 对 C% 的 expected inflation。
- 建议：补充一个 permutation-based 或 simulation-based 的分析，量化 Q3 violation 对 Type I error rate 的影响。

**W3** [warning] Within-family 分析（Llama-2 vs. 3）的 residual 28.3% 解读不充分
- 具体位置：Section 4.4 (p.7)
- 问题：Llama-2 vs. 3 unmatched C%=61.3%，matched C%=28.3%±1.6%。论文将 matched 后的 28.3% 解读为"genuine item-level DIF"，并指出它与 temporal matched C%≈28.9% 的一致性很有说服力。但 within-family 比较中，即使 ability matched 后，Llama-2 和 Llama-3 之间仍存在大量非 ability 差异：不同的 training data、tokenizer、RLHF procedure、architecture refinements。这些 confounds 都可能驱动 DIF。两个不同比较的 matched C% 趋同（~28-29%）可能是巧合，也可能反映了 MH-DIF 在 K=5 下的某种 floor effect。
- 建议：讨论 matched C% 趋同的替代解释（如 K=5 分层下的分辨率限制），或在更多 within-family pairs 上验证。

**W4** [warning] GSM1K 分析的统计效力不足以支撑 Claim 4
- 具体位置：Section 4.7 (p.7-8), Section 5.3 (p.8)
- 问题：GSM1K correlation r=-0.478 基于 N=33 models，95% CI=[-0.71, -0.16]。论文在 Limitations 中承认这是 exploratory，但 Discussion Section 5.3 仍将其作为"DIF captures behavioral change distinct from memorization"的主要证据。N=33 的相关分析受单个异常值影响很大，且 CI 跨越了 moderate-to-strong 的范围。
- 建议：将此分析明确标记为 preliminary/exploratory，不在 Discussion 中作为 Claim 4 的主要支撑；或在更大样本上验证。

**W5** [warning] Power analysis 假设不透明
- 具体位置：Section 4.1 (p.5)
- 问题：论文声称"A power analysis using empirical MMLU IRT parameters confirms that at N≥80 per cohort, ETS C achieves TPR of 0.68-0.80"，但未报告 IRT 参数的具体值、assumed effect size、simulation procedure。读者无法评估 power analysis 的合理性。
- 建议：在 Appendix 中补充 power analysis 的完整设定（IRT 参数分布、injection effect sizes、simulation repeats）。

**W6** [warning] Ground truth meta-critique (Claim 2) 的逻辑可逆
- 具体位置：Section 4.3 (p.6-7), Section 5.2 (p.8)
- 问题：论文发现 DIF flags 与 web-overlap labels 近乎独立（enrichment=0.964, Jaccard=0.206），解读为"web-overlap labels 是 wrong ground truth for differential methods"。但近乎独立同样可以解读为"MH-DIF 检测的不是 contamination"——两种解读逻辑上等价。论文用 semi-synthetic injection 证明 MH-DIF *can* detect differential contamination，但 semi-synthetic 条件（N1 指出的 subject-localized injection）与 real-world contamination 差距很大。因此 Claim 2 的说服力受限于 semi-synthetic 框架的生态效度。
- 建议：在 Discussion 中明确承认双向解读的可能性，而非单向指责 web-overlap labels。

---

## 小问题（不影响接收）

- **Abstract 过度密集**：Abstract 包含了 ρ≈0.997、z=-8σ to -49σ、ρ=-0.597 等大量数字，读起来像 executive summary 而非 abstract。建议精简到 3-4 个核心数字。
- **引用验证**：verify_references 检查发现 8 个 orphan bib entries（在 .bib 中但未被引用），包括 zhang2024gsm1k、wang2024mmlupro 等。另有 liang2026dvd 等少量条目在 OpenAlex 中未找到（可能是 preprint），holland1988mh 的年份存在 bib=1988 vs API=1986 的不一致。这些都是小问题。
- **Limitations 长度**：按 EMNLP 2026 规则，Limitations 不计入页数但不应包含过多额外内容。当前 Limitations 约 6 段，内容充实但可略微精简。
- **Table 1 FPR 列**：Within-family 和 Random split 行的 FPR 标记为 "--"，应注明为何不适用。
- **Footnote 1 匿名链接**：anonymous.4open.science 链接合规，但提交时需确认链接可访问。

---

## 主要优势

1. **大规模实证贡献**：5,227 models × 27,125 items 的 DIF 分析规模远超此前工作，6 个 benchmark 的交叉验证提供了强有力的 replication。
2. **严谨的 confound 控制**：5 种 cohort design（temporal, ability-quintile, within-family, within-subject, random-split）系统排除替代解释，matched-ability 分析令人信服地将 ability confounding 限定在 ~2.4pp。
3. **Ground truth meta-critique 有实际价值**：Claim 2 对 contamination detection 文献中普遍使用 web-overlap labels 作为 ground truth 的做法提出了合理质疑，有望推动更细致的 evaluation methodology。
4. **写作质量高**：Figure 1 直观有效，方法描述清晰，threshold sensitivity 分析（C% at |Δ|∈{1.0, 1.5, 2.0, 2.5}）展示了结论的鲁棒性。
5. **跨学科创新**：将 60+ 年历史的 psychometric DIF 方法引入 NLP evaluation 是有价值的 cross-pollination，audit protocol（Section 5.4）具有实践意义。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文页数 | ✅ 合规 | 8 页（含 Conclusion + Limitations），未超限 |
| 匿名性 | ✅ 合规 | "Anonymous ACL submission"，代码用 anonymous.4open.science |
| 模板 | ✅ 合规 | `\usepackage[review]{acl}` |
| Limitations | ✅ 存在 | 6 段，覆盖方法论、混淆变量、样本量、因果归因、benchmark 范围、时间定义 |
| 参考文献 | ⚠️ 小问题 | 8 个 orphan entries，少量年份不一致（见上） |

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

_source line 148 · 2026-05-21T15:23:24.683447+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-21T15:23:24.683889+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-21T15:23:58.670277+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Clarity**: 4/5\n\n### Must-Fix\n\n**R2-N1** [critical] Claim 4 \"DIF as diagnostic lens\" 支撑不足\n- Section 4.6, 5.3。GSM1K correlation (r=-0.478, partial r=-0.385, N=33) 样本太小，CI 上界 ≈-0.16。论文以此支撑 \"DIF captures behavioral change distinct from memorization\"，但 N=33 不够。如果 Claim 4 站不住，4 个 contribution 中有 1 个打折扣。\n- 建议：补充更强证据，或降级 Claim 4 为 observation 而非 contribution。\n\n**R2-N2** [critical] 方法论新颖性论证不充分\n- MH-DIF 是 1988 年方法，cross-subject matching 有先例（Nandakumar 1993, Donoghue 1993——论文自己承认）。4 个 claims 中 3 个是 descriptive findings。论文需要更清晰地论证 transplant 解决了什么 LLM-specific 新问题。\n- 建议：argue \"为什么 DIF 不能直接搬过来\"（LLM 作为 examinees 的特殊性），或明确 position 为 empirical contribution。\n\n**R2-N3** [critical] Temporal cohort 定义过于粗糙\n- Calendar year 划分混淆了 architecture shift、training methodology shift、temporal effect。虽有 5 种 cohort design，但主要结果仍基于 calendar year。Within-year cohort（如 2024-H1 vs H2）完整结果只在 Appendix 简单提及。\n- 建议：补充 within-year 完整结果；改 framing 为 \"cross-cohort DIF\" 而非 \"temporal comparability\"。\n\n### Should-Fix\n\n**R2-W1** ρ≈0.997 vs 31.3% 张力——Section 5.4 \"DIF Audit Protocol\" 只有 3 句话，actionability 不足。\n**R2-W2** ΔFPR=0.000 过于完美——注入率固定 20%，只在 5 个 subjects 验证，未讨论 Type II error。\n**R2-W3** DIF 术语对 EMNLP 读者不够友好——缺少 running example。\n**R2-W4** 与 Growing Pains 的区分过于简短——未验证 DIF-flagged items 与 FPC anchor items 的 overlap。\n**R2-W5** 引用问题：holland1988mh year mismatch、tao2026selfcritique/liu2026bhi author mismatch、8 orphan bib entries。\n\n### Missing References\n1. \"Lifting the Benchmark Iceberg with IRT\" (2025)\n2. Benchmark2 (arXiv:2601.03986, 2025)\n3. ATLAS / CAT-based LLM evaluation (Li et al. 2025, 已在 bib 未引用)\n4. MedIRT (arXiv:2509.24186, 2025)\n\n### 主要优势\n1. 规模和严谨性（5,227 models × 12,508 items，5 种 cohort design + 3 层控制）\n2. 发现的实际价值（31% instability + 6 benchmarks 复现）\n3. Ground truth meta-critique 对 contamination detection 文献有价值\n4. Semi-synthetic framework 在 LLM 场景有价值\n5. 叙事处理得当（diagnostic lens framing）\n\n---\n\n请对 R2 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注：\n1. R2-N1 关于 Claim 4 的批评是否与你的 W4 (GSM1K N=33) 一致？\n2. R2-N2 关于 novelty 的批评——你作为方法论 reviewer 如何看待？\n3. R2-N3 关于 temporal cohort 的批评与你的 N2 (因果模糊性) 有何关联？"
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
    "project": "irt_equated_bench_regen",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 4/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5 | **Clarity**: 4/5\n\n### Must-Fix\n\n**R2-N1** [critical] Claim 4 \"DIF as diagnostic lens\" 支撑不足\n- Section 4.6, 5.3。GSM1K correlation (r=-0.478, partial r=-0.385, N=33) 样本太小，CI 上界 ≈-0.16。论文以此支撑 \"DIF captures behavioral change distinct from memorization\"，但 N=33 不够。如果 Claim 4 站不住，4 个 contribution 中有 1 个打折扣。\n- 建议：补充更强证据，或降级 Claim 4 为 observation 而非 contribution。\n\n**R2-N2** [critical] 方法论新颖性论证不充分\n- MH-DIF 是 1988 年方法，cross-subject matching 有先例（Nandakumar 1993, Donoghue 1993——论文自己承认）。4 个 claims 中 3 个是 descriptive findings。论文需要更清晰地论证 transplant 解决了什么 LLM-specific 新问题。\n- 建议：argue \"为什么 DIF 不能直接搬过来\"（LLM 作为 examinees 的特殊性），或明确 position 为 empirical contribution。\n\n**R2-N3** [critical] Temporal cohort 定义过于粗糙\n- Calendar year 划分混淆了 architecture shift、training methodology shift、temporal effect。虽有 5 种 cohort design，但主要结果仍基于 calendar year。Within-year cohort（如 2024-H1 vs H2）完整结果只在 Appendix 简单提及。\n- 建议：补充 within-year 完整结果；改 framing 为 \"cross-cohort DIF\" 而非 \"temporal comparability\"。\n\n### Should-Fix\n\n**R2-W1** ρ≈0.997 vs 31.3% 张力——Section 5.4 \"DIF Audit Protocol\" 只有 3 句话，actionability 不足。\n**R2-W2** ΔFPR=0.000 过于完美——注入率固定 20%，只在 5 个 subjects 验证，未讨论 Type II error。\n**R2-W3** DIF 术语对 EMNLP 读者不够友好——缺少 running example。\n**R2-W4** 与 Growing Pains 的区分过于简短——未验证 DIF-flagged items 与 FPC anchor items 的 overlap。\n**R2-W5** 引用问题：holland1988mh year mismatch、tao2026selfcritique/liu2026bhi author mismatch、8 orphan bib entries。\n\n### Missing References\n1. \"Lifting the Benchmark Iceberg with IRT\" (2025)\n2. Benchmark2 (arXiv:2601.03986, 2025)\n3. ATLAS / CAT-based LLM evaluation (Li et al. 2025, 已在 bib 未引用)\n4. MedIRT (arXiv:2509.24186, 2025)\n\n### 主要优势\n1. 规模和严谨性（5,227 models × 12,508 items，5 种 cohort design + 3 层控制）\n2. 发现的实际价值（31% instability + 6 benchmarks 复现）\n3. Ground truth meta-critique 对 contamination detection 文献有价值\n4. Semi-synthetic framework 在 LLM 场景有价值\n5. 叙事处理得当（diagnostic lens framing）\n\n---\n\n请对 R2 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注：\n1. R2-N1 关于 Claim 4 的批评是否与你的 W4 (GSM1K N=33) 一致？\n2. R2-N2 关于 novelty 的批评——你作为方法论 reviewer 如何看待？\n3. R2-N3 关于 temporal cohort 的批评与你的 N2 (因果模糊性) 有何关联？"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-21T15:24:25.842059+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 27171
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-21T15:24:27.198149+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Clarity**: 4/5\n\n### Must-Fix\n\n**R1-N1** [critical] 半合成验证框架的生态效度存在根本缺陷\n- Section 3.4, Proposition 1, Section 4.5。Proposition 1 (ΔFPR=0) 是 by construction 的平凡结果——注入 subject X，matching variable 排除 X，信号数学上无法泄漏。论文仅验证了 single-subject contamination，未测试 multi-subject simultaneous injection（同时污染 3-5 个 subjects 后 FPR 是否仍为 0）。在 real-world 中 contamination 跨越所有 subjects。\n- 建议：补充 multi-subject simultaneous injection (k∈{2,3,5,10})，或显式限定 Claim 3 的适用范围。\n\n**R1-N2** [critical] 核心发现的因果模糊性：「Psychometric Instability」vs.「Expected Capability Evolution」\n- ρ=-0.597 的 difficulty-direction interaction（2024 模型难题 gain、简单题 erode）同样可以解释为正常的 capability evolution。MH-DIF 会将 **任何** 跨组 item functioning 差异标记为 DIF，包括 genuine capability change。标题\"Psychometric Instability\"暗示是 benchmark 测量问题，但如果主要是能力演变，则不是 \"instability\" 而是 \"expected differential performance\"。\n- 建议：区分 item instability vs differential performance；软化标题中的 \"Instability\"。\n\n**R1-N3** [critical] Bootstrap CI 的不对称性与 headline 数字精确度\n- 95% CI=[29.4%, 38.1%]，宽 8.7pp，上尾偏重。未报告 bootstrap resampling unit（model vs item）。CI 不对称暗示 right-skewed 分布。\"31%\" 作为 headline 但真实值可能高达 38%。\n- 建议：报告 resampling unit 和策略；Abstract/Title 使用 CI 或 \"approximately\"。\n\n### Should-Fix\n\n**R1-W1** K=5 分层敏感性分析不足——虽然附录有 K=20 (θ-conditioning) 结果 (FPR=0.312)，但主文未对比 K=5 vs K=10 vs K=20。\n**R1-W2** Yen's Q3 局部依赖影响未量化——11.3% within-subject pairs 超 |Q3|>0.20，但未 simulation 估计对 C% 的 expected inflation。\n**R1-W3** Within-family matched C%≈28.3% 的解读——两种比较的 matched C% 趋同 (~28-29%) 可能是 K=5 下的 floor effect 而非 genuine DIF。\n**R1-W4** GSM1K N=33 不足以支撑 Claim 4——与你的 N1 类似。\n**R1-W5** Power analysis 假设不透明——未报告 IRT 参数、assumed effect size、simulation procedure。\n**R1-W6** Ground truth meta-critique (Claim 2) 逻辑可逆——DIF 与 web-overlap 独立也可解读为 \"DIF 检测的不是 contamination\"，两种解读逻辑等价。Semi-synthetic 的生态效度（R1-N1）限制了 Claim 2 说服力。\n\n### 主要优势\n1. 大规模实证（5,227 models × 27,125 items，6 benchmarks）\n2. 严谨的 confound 控制（5 种 cohort + matched-ability → ~2.4pp）\n3. Ground truth meta-critique 有实际价值\n4. 写作质量高（Figure 1 直观有效）\n5. 跨学科创新（psychometrics → NLP evaluation）\n\n---\n\n请对 R1 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注：\n1. R1-N1 关于 multi-subject injection 的批评——你认为这是否真的 undermines Claim 3？\n2. R1-N2 关于 \"instability vs capability evolution\" 的批评与你的 N3 (temporal cohort 粗糙) 有何关联？\n3. R1-W6 关于 Claim 2 逻辑可逆性——你如何看待？你的 Soundness 4/5 是否与此冲突？"
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
    "project": "irt_equated_bench_regen",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 — Borderline Conference\n**Soundness**: 3.5/5 | **Excitement**: 3.5/5 | **Reproducibility**: 4/5 | **Clarity**: 4/5\n\n### Must-Fix\n\n**R1-N1** [critical] 半合成验证框架的生态效度存在根本缺陷\n- Section 3.4, Proposition 1, Section 4.5。Proposition 1 (ΔFPR=0) 是 by construction 的平凡结果——注入 subject X，matching variable 排除 X，信号数学上无法泄漏。论文仅验证了 single-subject contamination，未测试 multi-subject simultaneous injection（同时污染 3-5 个 subjects 后 FPR 是否仍为 0）。在 real-world 中 contamination 跨越所有 subjects。\n- 建议：补充 multi-subject simultaneous injection (k∈{2,3,5,10})，或显式限定 Claim 3 的适用范围。\n\n**R1-N2** [critical] 核心发现的因果模糊性：「Psychometric Instability」vs.「Expected Capability Evolution」\n- ρ=-0.597 的 difficulty-direction interaction（2024 模型难题 gain、简单题 erode）同样可以解释为正常的 capability evolution。MH-DIF 会将 **任何** 跨组 item functioning 差异标记为 DIF，包括 genuine capability change。标题\"Psychometric Instability\"暗示是 benchmark 测量问题，但如果主要是能力演变，则不是 \"instability\" 而是 \"expected differential performance\"。\n- 建议：区分 item instability vs differential performance；软化标题中的 \"Instability\"。\n\n**R1-N3** [critical] Bootstrap CI 的不对称性与 headline 数字精确度\n- 95% CI=[29.4%, 38.1%]，宽 8.7pp，上尾偏重。未报告 bootstrap resampling unit（model vs item）。CI 不对称暗示 right-skewed 分布。\"31%\" 作为 headline 但真实值可能高达 38%。\n- 建议：报告 resampling unit 和策略；Abstract/Title 使用 CI 或 \"approximately\"。\n\n### Should-Fix\n\n**R1-W1** K=5 分层敏感性分析不足——虽然附录有 K=20 (θ-conditioning) 结果 (FPR=0.312)，但主文未对比 K=5 vs K=10 vs K=20。\n**R1-W2** Yen's Q3 局部依赖影响未量化——11.3% within-subject pairs 超 |Q3|>0.20，但未 simulation 估计对 C% 的 expected inflation。\n**R1-W3** Within-family matched C%≈28.3% 的解读——两种比较的 matched C% 趋同 (~28-29%) 可能是 K=5 下的 floor effect 而非 genuine DIF。\n**R1-W4** GSM1K N=33 不足以支撑 Claim 4——与你的 N1 类似。\n**R1-W5** Power analysis 假设不透明——未报告 IRT 参数、assumed effect size、simulation procedure。\n**R1-W6** Ground truth meta-critique (Claim 2) 逻辑可逆——DIF 与 web-overlap 独立也可解读为 \"DIF 检测的不是 contamination\"，两种解读逻辑等价。Semi-synthetic 的生态效度（R1-N1）限制了 Claim 2 说服力。\n\n### 主要优势\n1. 大规模实证（5,227 models × 27,125 items，6 benchmarks）\n2. 严谨的 confound 控制（5 种 cohort + matched-ability → ~2.4pp）\n3. Ground truth meta-critique 有实际价值\n4. 写作质量高（Figure 1 直观有效）\n5. 跨学科创新（psychometrics → NLP evaluation）\n\n---\n\n请对 R1 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。特别关注：\n1. R1-N1 关于 multi-subject injection 的批评——你认为这是否真的 undermines Claim 3？\n2. R1-N2 关于 \"instability vs capability evolution\" 的批评与你的 N3 (temporal cohort 粗糙) 有何关联？\n3. R1-W6 关于 Claim 2 逻辑可逆性——你如何看待？你的 Soundness 4/5 是否与此冲突？"
  }
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-21T15:24:28.660490+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 154 · 2026-05-21T15:24:31.414995+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 155 · 2026-05-21T15:24:32.918575+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**摘要**：Overall 3.5/5（Borderline Conference）。论文将 MH-DIF 大规模应用于 LLM benchmark 是有价值的跨学科贡献，5 种 cohort design 的 confound 控制较为系统。但存在 3 个 Must-Fix 问题：
1. 半合成验证框架仅验证 subject-localized contamination（Proposition 1 的 ΔFPR=0 是 trivially true by construction），未测试 multi-subject simultaneous injection
2. 核心 "31% instability" 未能区分 psychometric instability 与 expected capability evolution（difficulty-direction interaction ρ=-0.597 同样支持后者）
3. Bootstrap CI [29.4%, 38.1%] 的不对称性和 resampling 策略未充分报告

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

_source line 156 · 2026-05-21T15:24:48.907459+00:00_

R1 的 Round 1 初审报告已收到（此前已读完整版本）。交叉分享任务已发送给两位 Reviewer，等待他们的 [AGREE]/[REBUT] 逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 17

## Round 17

2 recorded events


### User

_source line 157 · 2026-05-21T15:25:39.536056+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 Reviewer 2 Round 1 意见

---

### Must-Fix 回应

**[AGREE] R2-N1: Claim 4 "DIF as diagnostic lens" 支撑不足**

与我的 W4 完全一致。GSM1K N=33 的相关分析（r=-0.478, CI=[-0.71, -0.16]）统计效力严重不足，单个异常模型即可显著改变结论。论文在 Limitations 中承认这是 exploratory，但 Discussion Section 5.3 和 Introduction Claim 4 的措辞并未匹配这一谨慎程度——"DIF captures behavioral change distinct from memorization" 作为 contribution 陈述过强。

补充一点 R2 未提及的：Claim 4 的另一支撑——difficulty-direction interaction（ρ=-0.597）——本身解读也有歧义（见我的 N2）。gains on hard items + erosion on easy ones 同样可解释为 expected capability evolution 而非 diagnostic signal。因此 Claim 4 的两条证据链都有弱点。

**建议**：同意 R2——降级为 exploratory observation 或 supplementary analysis，从 4 个 contributions 中移除。

---

**[REBUT] R2-N2: 方法论新颖性论证不充分**

R2 的批评方向合理但严厉程度偏重，理由如下：

1. **论文已 explicitly 定位为 empirical contribution**：Introduction 第 19 行明确写道 "Our contributions are empirical and methodological, not algorithmic"。论文从未声称 MH-DIF 或 cross-subject matching 是新方法——它声称的是将已有方法**大规模应用于 LLM evaluation 这个新 domain** 并产生了 non-trivial empirical findings。

2. **Transplant 并非 trivial**：虽然 MH-DIF 是 1988 年的方法，但将其应用于 LLM benchmarks 涉及多个 LLM-specific 的适配决策——(a) LLMs 作为 examinees 不满足传统 DIF 的 exchangeability 假设（同一 model family 内高度相关），论文通过 graduated de-duplication 和 architecture heterogeneity check（Appendix A.2, 99.98% decoder-only）应对；(b) temporal cohort 定义（而非传统的 demographic groups）需要 ability confounding 控制（matched-ability analysis, Cohen's d=-0.17）；(c) semi-synthetic framework 的 cross-subject matching 设计针对 multi-domain benchmark 结构。这些并非照搬。

3. **3 个 descriptive findings 并不等于低价值**：EMNLP/ARR 社区接受高质量的 empirical/analysis papers（参见 Burnell et al. 2023 in Science, Rodriguez et al. 2021 ACL——两篇都主要是 descriptive findings with methodological framing）。Claim 2 (ground truth meta-critique) 对整个 contamination detection 文献的 evaluation methodology 有实际影响。

**但我同意论文应更清晰论证 LLM-specific 挑战**。当前 Method section 过于 textbook-style，未充分讨论为什么直接搬运 DIF 到 LLM 场景不够——例如 local dependence（Yen's Q3）、model family structure、ability distribution 的非正态性等。建议在 Section 3 开头增加 1-2 段讨论 LLM 作为 examinees 的特殊性及论文如何应对。

**结论**：不应升级为 Must-Fix。建议改为 Should-Fix，要求补充 LLM-specific methodological challenges 的讨论。

---

**[AGREE with nuance] R2-N3: Temporal cohort 定义过于粗糙**

与我的 N2（因果模糊性）高度相关但切入角度不同。R2 批评的是 cohort 划分的 granularity，我批评的是 DIF 结果的 causal interpretation。两者指向同一根本问题：**calendar-year cohort 混淆了太多变量**。

我同意 R2 的三个具体点：
- Calendar year 确实同时混淆了 architecture shift、training methodology、data composition 变化
- 6-month window 结果（MMLU C%=34.35%, Section 4.7 最后一段）仅作为 one-liner 出现，未展开分析
- "Temporal comparability" 的 framing 暗示了比数据支持的更强的 temporal specificity

**但我不完全同意将此升级为 critical**。论文的 5 种 cohort design 已经提供了一定程度的 triangulation：random split (0.18%) 排除了抽样噪声，ability-quintile (2.9%) 排除了纯 ability 差异，within-family (matched 28.3%) 控制了部分 architecture effect。calendar year 作为 primary cohort 定义虽粗糙，但在 Open LLM Leaderboard 数据上是最自然的选择（finer-grained metadata 如 training data cutoff 对大多数模型不可用）。

**关联我的 N2**：R2-N3 和我的 N2 共同构成一个强论点——论文需要更谨慎的 framing。如果 cohort 定义粗糙（R2-N3）且 DIF 不能区分 instability vs. capability evolution（我的 N2），则 "Psychometric Instability" 的结论过强。建议将两个问题合并处理：软化 causal framing + 补充 within-year 完整分析。

---

### Should-Fix 回应

**[AGREE] R2-W1: ρ≈0.997 vs 31.3% 张力，Audit Protocol 过于简短**

Section 5.4 "Recommended DIF Audit Protocol" 确实只有 3 句话，对于一篇声称"LLM benchmarks need psychometric monitoring"的论文来说，practical recommendations 的深度严重不足。论文花了大量篇幅证明 DIF 存在，但对"发现 DIF 后该怎么做"的讨论几乎为零。ρ≈0.997 说明 aggregate ranking 不受影响，但论文同时声称 25% 的模型 rank shift ≥100——这个张力值得更深入的讨论：何时 DIF 需要 action，何时只需 annotation？

---

**[AGREE] R2-W2: ΔFPR=0.000 过于完美**

与我的 N1 一致。R2 从不同角度提出了互补的批评：R2 关注注入率固定 20% 和仅 5 subjects 的验证范围，我关注 subject-localized injection 的 ecological validity。两个批评共同削弱了 Proposition 1 / Claim 3 的说服力。R2 补充的 Type II error 讨论也是有价值的——论文只关注了 FPR=0，但未讨论在何种条件下 cross-subject matching 可能 miss real DIF (reduced TPR)。

---

**[AGREE] R2-W3: DIF 术语对 EMNLP 读者不友好**

合理建议。虽然论文 Section 3.2 的 DIF 描述是准确的，但对 NLP 社区读者来说过于 formal。一个 running example（例如用一个具体的 MMLU 题目展示 2023 models 和 2024 models 的不同表现模式）可以显著提升 accessibility，且只需 3-5 行。

---

**[AGREE] R2-W4: 与 Growing Pains 的区分过于简短**

论文在 Related Work 中提到 Growing Pains (Habba et al. 2026) 只有一句 "our work is complementary"，但未定量验证 DIF-flagged items 与 FPC anchor items 的 overlap。如果两种方法 flag 的 items 高度重叠，说明 DIF 没有提供增量信息；如果不重叠，则 complementarity 有实证支持。这个分析很容易做（Jaccard/enrichment），不做是遗憾。

---

**[AGREE] R2-W5: 引用问题**

与我的小问题一致。verify_references 确认 holland1988mh year=1988 vs OpenAlex=1986（该论文实际发表于 1988 的 book chapter，但 earlier version 可能是 1986——应核实并统一）。8 个 orphan bib entries 应清理。

---

### Missing References 回应

**[AGREE]** R2 推荐的 4 篇文献中：
- "Lifting the Benchmark Iceberg with IRT" (2025) 和 ATLAS (Li et al. 2025) 确实与本文高度相关——都将 IRT/psychometric 方法应用于 LLM evaluation，不引用会让 Related Work 显得不完整。
- Benchmark2 和 MedIRT 相关性稍弱但值得 mention。论文当前 Related Work 已经较密集，建议选择性增加最相关的 2-3 篇。

---

### 总结：R1 与 R2 的共识与分歧

**共识区域（两位 reviewer 均认为需要改进）：**
1. Claim 4 / GSM1K 支撑不足（R2-N1 = 我的 W4）→ 建议降级为 observation
2. ΔFPR=0.000 的 validity 限制（R2-W2 ≈ 我的 N1）→ 核心方法论问题
3. Temporal framing 与 causal interpretation（R2-N3 ≈ 我的 N2）→ 需软化 claims
4. 引用问题（R2-W5 = 我的小问题）→ 容易修复

**分歧区域：**
1. **Novelty (R2-N2)**：R2 认为是 critical，我认为是 Should-Fix。论文已 self-position 为 empirical contribution，且 EMNLP 社区接受此类工作。但需补充 LLM-specific challenges 的讨论。
2. **严重程度排序**：我将 semi-synthetic ecological validity（N1）和 causal ambiguity（N2）列为最关键问题；R2 将 Claim 4 insufficiency（N1）和 novelty（N2）列为最关键。两组 priorities 互补。

**如果作者只能修复 3 个问题，我建议优先级为：**
1. 软化 causal framing（回应 R1-N2 + R2-N3）——改标题/措辞，成本低影响大
2. 补充 multi-subject injection 实验（回应 R1-N1 + R2-W2）——加强核心 validation
3. 降级 Claim 4 为 observation（回应 R2-N1 + R1-W4）——避免 overclaiming

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

_source line 158 · 2026-05-21T15:25:49.405945+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应后进入收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 159 · 2026-05-21T15:25:52.019946+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心结论：R1 与 R2 在 4 个关键问题上形成共识——Claim 4 支撑不足、semi-synthetic 框架生态效度有限、temporal framing 过强、引用需修复。主要分歧在 novelty 的严重程度（R2 视为 critical，我认为 Should-Fix，因为论文已明确定位为 empirical contribution）。建议作者优先处理：(1) 软化 causal framing/标题，(2) 补充 multi-subject injection 实验，(3) 将 Claim 4 降级为 exploratory observation。

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

_source line 160 · 2026-05-21T15:26:00.343429+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "irt_equated_bench_regen",
  "text": "提醒：请尽快提交你对 Reviewer 1 意见的交叉回应（[AGREE]/[REBUT]）。Reviewer 1 的交叉回应已提交，等待你的回复以进入收敛判断阶段。"
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
    "project": "irt_equated_bench_regen",
    "text": "提醒：请尽快提交你对 Reviewer 1 意见的交叉回应（[AGREE]/[REBUT]）。Reviewer 1 的交叉回应已提交，等待你的回复以进入收敛判断阶段。"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-21T15:26:04.159434+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3816
}
```

</details>

---


### Assistant

_source line 162 · 2026-05-21T15:26:06.805076+00:00_

Reviewer 1 交叉回应已收到，等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 19

## Round 19

16 recorded events


### User

_source line 163 · 2026-05-21T15:26:33.544036+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 (Round 1)

---

### Must-Fix 逐条回应

**[AGREE] R1-N1: Semi-synthetic validation 的 multi-subject injection 缺失**

同意这是一个实质性缺陷。Proposition 1 (ΔFPR=0) 确实 by construction：注入 subject X → matching variable 排除 X → 信号无法泄漏，这在数学上是平凡的。R1 指出的 multi-subject simultaneous contamination 场景更关键：如果 subjects Y, Z 同时被污染，而我们在测试 subject X 时用 Y+Z 的总分做 matching variable，matching variable 本身就被污染了，conditional independence 假设不再成立。

不过我补充一个对作者的部分辩护：论文 Section 4.7 的 cross-benchmark validation（6 benchmarks 各自独立运行 MH-DIF）在一定程度上隐含了 "多基准同时存在 DIF" 的场景——MMLU 的 C% 为 31.3%，同时 ARC 为 26.9%、HellaSwag 为 17.9% 等，这说明 DIF 在多个基准上同时出现。但这不等同于 R1 要求的 multi-subject simultaneous injection 的控制实验。

**结论**：同意需要补充 k∈{2,3,5,10} 的 multi-subject injection 实验，或者明确将 Claim 3 限定为 "single-subject contamination detection"。这是 Claim 3 能否成立为独立 contribution 的关键。

---

**[AGREE with nuance] R1-N2: "Psychometric Instability" vs. "Expected Capability Evolution"**

R1 的核心论点成立：MH-DIF 标记的是 **任何** conditional 差异，包括 genuine capability evolution。但我对 R1 的论证有两个补充：

(1) **MH-DIF 已经控制了 ability level**。MH procedure 按 total score 分层后在每层内计算 odds ratio，所以纯粹的 "2024 模型整体更强" 不会被标记为 DIF。R1 引用的 ρ=-0.597 difficulty-direction interaction 是 within-stratum 现象——同一总分水平的模型，2024 cohort 在难题上表现更好、易题上更差。这确实可以是 legitimate capability profile shift（如推理策略变化）而非 "instability"。

(2) 但论文 Section 4.4 的 Simpson's paradox 分析（logistic regression: item properties, not accuracy gains, drive DIF; LR χ²=647, p<0.001）和 Section 5.1 的三层控制（matched-ability quintile 只降至 2.4pp）提供了部分反驳：如果 DIF 完全是 legitimate capability evolution，那么 within matched-ability stratum 的 DIF 应该接近 0。实际 C% 仍为 31.3% even after controlling for ability，说明不仅仅是 evolution。

**我的立场**：标题中的 "Instability" 确实过强。真实情况可能是 "instability" + "evolution" 的混合体，论文无法区分两者的相对贡献。建议将标题改为更中性的 "Differential Item Functioning" 而非 "Psychometric Instability"，或在正文中明确承认这一模糊性。

**与我的 N3 的关系**：我的 N3（temporal cohort 定义粗糙）和 R1-N2 实际上指向同一个 underlying issue——calendar year cohort 混淆了多种因素（temporal drift、architecture shift、training data change、capability evolution），论文无法将 DIF signal 归因到具体原因。两个批评互补：我的 N3 关注 confound 的 source，R1-N2 关注 confound 的 interpretation。合在一起构成对 "temporal comparability" narrative 的强挑战。

---

**[REBUT] R1-N3: Bootstrap CI 不对称性与 headline 数字精确度**

我认为 R1 过度 escalate 了这个问题的严重性。

(1) CI=[29.4%, 38.1%] 确实宽 8.7pp，但**整个 CI 都在 "roughly one-third" 的范围内**——无论是 29% 还是 38%，qualitative conclusion 不变。这与标题 "31%" 的精确写法是两回事。

(2) Bootstrap CI 不对称（right-skewed）是 proportion 接近中间值时的自然现象，不暗示方法论问题。

(3) 关于 resampling unit——这是一个值得报告的技术细节，但不构成 "critical" 级别问题。model-level resampling 和 item-level resampling 会产生不同的 CI，但论文的 5,227 models 样本量足够大，无论哪种策略 CI 都不会质变。

**结论**：同意应在 Abstract 中加 "approximately" 或报告 CI，但这是 Should-Fix 而非 Must-Fix。不应升级为 critical 影响接收决定。

---

### Should-Fix 逐条回应

**[AGREE] R1-W1: K=5 分层敏感性**
同意。主文应对比 K=5/10/20 的 C% 变化趋势。如果 C% 随 K 增加单调下降，可能暗示 residual ability confound；如果收敛，则说明结果稳健。论文 Appendix 提到 K=20 (IRT θ-conditioning) 得到 FPR=0.312（与 K=5 几乎一致），但这个关键信息埋在附录里太可惜了。

**[AGREE] R1-W2: Yen's Q3 局部依赖影响未量化**
同意。11.3% within-subject pairs 超过 |Q3|>0.20 是非忽略的局部依赖。论文应至少用 simulation 估计：如果 items 有此水平的局部依赖，expected C% inflation 是多少？这直接影响 "31%" 这个数字的可信度。

**[REBUT] R1-W3: Within-family matched C%≈28.3% 是 K=5 的 floor effect**
不完全同意。R1 认为 across-family 和 within-family 的 matched C% 趋同（~28-29%）可能是 K=5 下的 floor effect。但论文 Section 4.2 报告 within-family analysis 将 C% 从 31.3% 降到了 ~28.3%（Llama-3 的 Llama-2 vs Llama-3 对比得到 61.3%，但 Ability-matched reduces 更多）。关键是：如果这是 K=5 的 floor effect，那增加 K 应该进一步降低 C%。但 Appendix 的 K=20 θ-conditioning 结果（FPR=0.312）与 K=5 几乎无差别，反驳了 floor effect 假说。

不过我承认论文没有在主文中清晰展示这个论证链。

**[AGREE] R1-W4: GSM1K N=33 不足以支撑 Claim 4**
完全同意，与我的 N1 一致。N=33 的 GSMIK correlation 作为 Claim 4 的主要证据太弱了。

**[AGREE] R1-W5: Power analysis 假设不透明**
同意。Section 4.5 提到 power analysis 但未报告 assumed IRT parameters、effect size distribution、simulation procedure。这影响 reproducibility。

**[AGREE with nuance] R1-W6: Claim 2 逻辑可逆性**
这是 R1 审稿中最精彩的一个观察。

R1 正确指出：DIF ⊥ web-overlap 有两种等价解读——
- 解读 A（作者采用）：DIF 捕捉到了 web-overlap 无法检测的 deeper behavioral shift
- 解读 B（R1 提出）：DIF 检测的根本不是 contamination，而是其他东西

但我认为 Section 4.5 的 semi-synthetic validation 部分化解了解读 B：**受控注入实验证明 MH-DIF 确实能检测 contamination signal**（ΔTPR > 0 at p=0.5，Figure 2 dose-response curve 单调递增）。如果 DIF "根本不检测 contamination"，semi-synthetic 实验不应该有正的 detection power。

所以更准确的解读是：DIF **可以**检测 contamination（semi-synthetic 证明），但 real-world DIF flags 与 web-overlap labels 独立（Section 4.3），这说明 **real-world contamination 比 web-overlap 标签描述的更复杂**——web-overlap 只捕捉 verbatim matching，而 DIF 捕捉 behavioral consequence。两者测量的是不同层面的现象。

**关于我的 Soundness 4/5 是否冲突**：不冲突。我给 4/5 是基于整体方法论的严谨性（5 种 cohort、3 层控制、cross-benchmark 复现）。R1-W6 指出的是 Claim 2 的一个 interpretive gap，而非 methodological flaw。论文的数据和分析是 sound 的，问题在于 interpretation 的唯一性。这属于 "some minor points may need extra support"（Soundness 4 的 anchor），不影响我对整体 soundness 的判断。

---

### 对 R1 主要优势评价的回应

R1 列出的 5 个优势我全部认同。特别是 "跨学科创新（psychometrics → NLP evaluation）" 这一点——虽然我在 N2 中指出方法论新颖性有限，但 R1 对此的 framing 更 generous（Excitement 3.5 vs 我的 3）。反思后我认为 R1 的评价更合理：**方法论虽然是 transplant，但 transplant 的质量（严谨的控制、大规模验证、有价值的发现）本身值得 credit**。我愿意将 Excitement 上调至 3.5/5，与 R1 对齐。

---

### 综合评估调整

交叉审稿后，我维持 **Overall 3.5 (Borderline Conference)**，但微调子项：
- Soundness: 4/5 → **3.5/5**（R1-N1 的 multi-subject injection 缺失和 R1-N2 的因果模糊性共同削弱了我对 soundness 的信心）
- Excitement: 3/5 → **3.5/5**（R1 对 "跨学科 transplant 质量" 的论点说服了我）
- Reproducibility: 4/5 不变
- Clarity: 4/5 不变

**关键共识**：R1 和我都认为 Claim 4 支撑不足（R1-W4 + 我的 N1），temporal cohort 的 confound 问题需要更深入讨论（R1-N2 + 我的 N3），且论文应更审慎地定位 novelty（R1 的 N2 因果模糊 + 我的 N2 transplant 论证）。如果这三个共识问题得到 effective address，论文有望上升到 Conference 水平。

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

_source line 164 · 2026-05-21T15:27:01.705083+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-21T15:27:01.705611+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-21T15:27:07.579506+00:00_

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

_source line 167 · 2026-05-21T15:27:07.580022+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T15:10:21.914628+00:00\", \"completed_at\": \"2026-05-21T15:12:50.590680+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 3-5\", \"message\": \"连续 3 页无 figure/table（Figure 1 在 p2，下一个 display item Table 1 在 p6，间隔 4 页）。虽然 p4-5 有 display equations 和 Proposition 1 缓解了纯文本单调感，但审稿人快速翻阅时 p3-5 视觉节奏较平\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-8\", \"message\": \"主正文 8 页仅 4 个 display items（2 fig + 2 table），而附录有 5 个。对于实证为主的论文偏低（典型 5-8 个）。建议考虑将 Figure 4（downstream ranking impact）或 Table 3（structural controls）提升到主正文——这两个直接支撑核心 claims\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点，Figure 1 在 page 2 顶部出现，仍在前 3 页内，可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 的 axis labels 和 legend 字号偏小（约为正文字号的 60-65%），建议放大至 ≥70%\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"末页内容约占 60%，底部 Figure 5 下方有约 40% 空白。可通过调整附录 figure 尺寸或重排内容改善空间利用\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Figure 4 散点图使用不同 marker shape 区分 model families，色盲友好度尚可，但部分点重叠密集区域辨识度降低\"}, {\"severity\": \"info\", \"dimension\": \"pages 6,8\", \"message\": \"Table 1 和 Table 2 均使用 booktabs 风格，精度统一，最优值有 bold 标注——符合规范\"}, {\"severity\": \"info\", \"dimension\": \"pages 4-5\", \"message\": \"公式渲染正确，Proposition 1 排版规范，无 LaTeX 残留错误\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-11\", \"message\": \"References 格式统一，未发现 [?] 未解析引用或明显格式不一致\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-21T15:27:07.731031+00:00_

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

_source line 169 · 2026-05-21T15:27:07.781597+00:00_

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

_source line 170 · 2026-05-21T15:28:01.595399+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null | wc -l",
  "description": "Check issue tracker line count"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml 2>/dev/null | wc -l",
    "description": "Check issue tracker line count"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-21T15:28:01.747398+00:00_

337

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

_source line 172 · 2026-05-21T15:29:54.706202+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Previous rounds: 1-3 (2026-05-20/21), Action Matrix round 4\n# Current: Round 5 (fresh review, 2026-05-21, EMNLP 2026 target)\n\n# ============================================================\n# RECURRING ISSUES (from prior rounds, still raised in Round 5)\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"31.3% temporal DIF 因果归因不清——无法区分 psychometric instability vs expected capability evolution\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"κ=0.14 随机水平，46% within-family overlap\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"论文成功 reframe 为 temporal instability，但因果归因仍未解决\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"共识：最根本的解释性限制\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N2: MH-DIF 标记任何 conditional 差异包括 genuine capability change；ρ=-0.597 difficulty-direction interaction 同样支持 capability evolution 解读。R2 AGREE with nuance：MH 已控制 ability level，但 within-stratum profile shift 可以是 legitimate。两人共识：标题 'Psychometric Instability' 过强，应软化为 'Differential Item Functioning' 或 'Measurement Drift'。\"\n  action_items:\n    - round: 2\n      action: \"Discussion 中承认 instability 与 legitimate construct evolution 的不可分性\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Rebuttal: DIF psychometric tradition 不需要因果分解\"\n      assigned_to: director\n      status: in_progress\n    - round: 5\n      action: \"软化标题和 framing——改 'Psychometric Instability' 为更中性表述；在 Discussion 中明确承认 instability + evolution 混合体\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"Claim 4 (DIF as diagnostic lens) 证据不足——GSM1K N=33 太弱，应降级为 exploratory observation\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识 Major\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 将其从 Minor 提升为 Major\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N1: GSM1K r=-0.478 partial r=-0.385 N=33 CI=[-0.71,-0.16]，单个异常值即可改变结论。R1 AGREE 并补充：Claim 4 另一支撑 ρ=-0.597 也有 capability evolution 的替代解读。两条证据链均有弱点。共识：降级为 exploratory observation，从 4 contributions 中移除。\"\n  action_items:\n    - round: 4\n      action: \"GSM1K 已标注 exploratory。Claim 4 重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"将 Claim 4 从 contribution list 中移除，降级为 supplementary observation；收紧为 3 个 contributions\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 vs 31.3% 张力——DIF Audit Protocol (Section 5.4) 只有 3 句话，actionability 严重不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识方向\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 建议反转 emphasis\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W1: 论文花大量篇幅证明 DIF 存在，但对发现 DIF 后该怎么做几乎为零。R1 AGREE：何时需要 action vs 只需 annotation 未讨论。\"\n  action_items:\n    - round: 5\n      action: \"扩展 Section 5.4：具体 audit 频率、发现高 C% 后的处理流程、DIF-cleaned scores 是否应作为补充报告\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"技术新颖性有限——MH-DIF transplant 需要更清晰论证 LLM-specific 挑战\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"DIF 方法本身无创新\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"cross-subject matching 降级为 well-executed application\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N2 列为 critical。R1 REBUT→降级 Should-Fix：论文已 self-position 为 empirical contribution (Introduction L19)，transplant 涉及 LLM-specific 适配（de-duplication, temporal cohort, ability confound 控制）。R2 交叉回应后 Excitement 上调至 3.5/5。共识：补充 LLM-specific challenges 讨论即可。\"\n  action_items:\n    - round: 5\n      action: \"Section 3 开头增加 1-2 段：LLM 作为 examinees 的特殊性（local dependence, model family structure, ability 分布非正态）及论文如何应对\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失引用：需补充 2025-2026 IRT/LLM evaluation 最新工作\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Lalor/Vania/Balloccu 已补充\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Clauser & Mazor (1998) + Nandakumar (1993) 已补充\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"新增 4 篇 missing references：(1) 'Lifting the Benchmark Iceberg with IRT' (2025), (2) Benchmark2 (arXiv:2601.03986), (3) ATLAS/CAT-based LLM eval (Li et al. 2025, 已在 bib 未引用), (4) MedIRT (arXiv:2509.24186)。另有 8 个 orphan bib entries 待清理，holland1988mh year mismatch。\"\n  action_items:\n    - round: 5\n      action: \"引用 Benchmark Iceberg + ATLAS；清理 8 orphan bib entries；修正 holland1988mh year\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# NEW ISSUES (first raised in Round 5)\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic framework 仅验证 single-subject injection，未测试 multi-subject simultaneous contamination\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N1: Proposition 1 ΔFPR=0 是 by construction 的平凡结果——注入 subject X，matching variable 排除 X，信号数学上无法泄漏。现实中 contamination 跨越所有 subjects，此时 cross-subject matching variable 也被污染。R2 AGREE：需要 k∈{2,3,5,10} multi-subject injection 实验。R2 补充：cross-benchmark validation (Section 4.7) 隐含了多基准同时 DIF 的场景，但不等同于控制实验。\"\n  action_items:\n    - round: 5\n      action: \"补充 multi-subject simultaneous injection 实验（k∈{2,3,5,10} subjects），或显式限定 Claim 3 为 single-subject contamination detection\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI [29.4%, 38.1%] 的 resampling unit 和不对称性未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N3 列为 critical (CI 宽 8.7pp, right-skewed, resampling unit 不明)。R2 REBUT→降级 Should-Fix：整个 CI 在 'roughly one-third' 范围内，qualitative conclusion 不变。共识：报告 resampling strategy，Abstract 加 'approximately'。\"\n  action_items:\n    - round: 5\n      action: \"报告 bootstrap resampling unit (model vs item)；Abstract/Title 用 'approximately 31%' 或报告 CI\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"K=5 quintile stratification 的敏感性分析未在主文呈现\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE。Appendix K=20 θ-conditioning FPR=0.312 ≈ K=5，但此关键信息埋在附录。应在主文对比 K=5/10/20 的 C% 变化趋势。\"\n  action_items:\n    - round: 5\n      action: \"Section 4.2 或 Table 1 增加一行 K sensitivity analysis (K=5/10/20)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Yen's Q3 局部依赖对 C% 的 expected inflation 未量化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2 AGREE。11.3% within-subject pairs 超 |Q3|>0.20 是 non-trivial。应通过 simulation 估计此水平 LD 对 Type I error rate 的影响。\"\n  action_items:\n    - round: 5\n      action: \"Simulation 或 permutation-based 分析：估计 11.3% Q3 violation 对 C% 的 expected inflation\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"DIF 术语对 EMNLP 读者不够友好——缺少 running example\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W3 + R1 AGREE。ETS Category A/B/C、α_MH、Δ_MH 等对 NLP 社区陌生。需要用具体 MMLU item 展示 DIF 计算过程。\"\n  action_items:\n    - round: 5\n      action: \"Section 3.2 加一个 running example（具体 MMLU item 展示 2023 vs 2024 cohort 的 DIF 计算）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains (Habba et al. 2026) 的区分缺乏实证验证\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W4 + R1 AGREE。论文只说 'our work is complementary' 一句话，未验证 DIF-flagged items 与 FPC anchor items 的 overlap (Jaccard/enrichment)。这个分析容易做，不做是遗憾。\"\n  action_items:\n    - round: 5\n      action: \"补充 DIF flags vs Growing Pains FPC anchors 的 overlap 分析（Jaccard），或在 Discussion 详细讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W6\"\n  summary: \"Power analysis 假设不透明——IRT 参数、effect size、simulation procedure 未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2 AGREE。Section 4.1 声称 N≥80 达到 TPR 0.68-0.80，但未报告 assumed IRT parameters 和 simulation 细节。\"\n  action_items:\n    - round: 5\n      action: \"Appendix 补充 power analysis 完整设定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 (ground truth meta-critique) 逻辑可逆性——DIF ⊥ web-overlap 的双向解读\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W6: DIF ⊥ web-overlap 有两种等价解读 (A: web-overlap 是 wrong ground truth; B: DIF 不检测 contamination)。R2 REBUT with nuance：semi-synthetic 证明 DIF can detect contamination (ΔTPR>0)，所以解读 B 不完全成立——更准确的是 real-world contamination 比 web-overlap 描述的更复杂。R2 认为是 interpretive gap 非 methodological flaw。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中承认 Claim 2 的双向解读可能性，而非单向指责 web-overlap labels\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED ISSUES (not raised in Round 5)\n# ============================================================\n\n- id: \"RD2-W1\"\n  summary: \"Within-family Llama 2 vs 3 的 61.3% DIF + temporal cohort ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"Round 5 未作为独立问题提出。论文已报告 Cohen's d=-0.17, OVL=76.4%, matched C%=28.9%±0.1%。R1 引用此数据但不作为独立 issue。\"\n  resolution: \"plan_027 确认 temporal cohort ability gap 很小。Ability confound 仅解释 2.4pp。\"\n  resolution_round: 4\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (CFI=0.72) 对 MH 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF cross-analysis: r=0.09 (p=0.50)。MH 是 nonparametric，不依赖 IRT fit。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 过于完美需 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI = [0.000, 0.000]。Cross-subject stratification 对 within-subject injection 不变是 structural guarantee。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N1\"\n  summary: \"引用问题：幻觉引用 Tutz & Friedman (2007)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"确认为幻觉引用。论文当前版本已不包含。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-W2\"\n  summary: \"与 Growing Pains 的区分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"修订版 §2 已详细对比。但 Round 5 reviewer 认为仍过于简短（见 R5-W5），需要实证验证。\"\n  resolution_round: 2\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"区分文字已有，但缺乏实证验证（overlap 分析）——升级为新 issue R5-W5\"\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加，结果稳健。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"R1-W2\"\n  summary: \"推理-RL 鲁棒性 N=13\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"降级为补充分析。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"RD2-W4\"\n  summary: \"补充分析过多稀释焦点\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"Round 5 未独立提出。当前论文已精简，但 R1 仍提到 Abstract 过度密集（堆叠过多数字）。\"\n  action_items:\n    - round: 5\n      action: \"精简 Abstract 至 3-4 个核心数字\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Previous rounds: 1-3 (2026-05-20/21), Action Matrix round 4\n# Current: Round 5 (fresh review, 2026-05-21, EMNLP 2026 target)\n\n# ============================================================\n# RECURRING ISSUES (from prior rounds, still raised in Round 5)\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"31.3% temporal DIF 因果归因不清——无法区分 psychometric instability vs expected capability evolution\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"κ=0.14 随机水平，46% within-family overlap\"\n    - round: 2\n      reviewers: [1, 2]\n      note: \"论文成功 reframe 为 temporal instability，但因果归因仍未解决\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"共识：最根本的解释性限制\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N2: MH-DIF 标记任何 conditional 差异包括 genuine capability change；ρ=-0.597 difficulty-direction interaction 同样支持 capability evolution 解读。R2 AGREE with nuance：MH 已控制 ability level，但 within-stratum profile shift 可以是 legitimate。两人共识：标题 'Psychometric Instability' 过强，应软化为 'Differential Item Functioning' 或 'Measurement Drift'。\"\n  action_items:\n    - round: 2\n      action: \"Discussion 中承认 instability 与 legitimate construct evolution 的不可分性\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 4\n      action: \"Rebuttal: DIF psychometric tradition 不需要因果分解\"\n      assigned_to: director\n      status: in_progress\n    - round: 5\n      action: \"软化标题和 framing——改 'Psychometric Instability' 为更中性表述；在 Discussion 中明确承认 instability + evolution 混合体\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"Claim 4 (DIF as diagnostic lens) 证据不足——GSM1K N=33 太弱，应降级为 exploratory observation\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识 Major\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R2 将其从 Minor 提升为 Major\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N1: GSM1K r=-0.478 partial r=-0.385 N=33 CI=[-0.71,-0.16]，单个异常值即可改变结论。R1 AGREE 并补充：Claim 4 另一支撑 ρ=-0.597 也有 capability evolution 的替代解读。两条证据链均有弱点。共识：降级为 exploratory observation，从 4 contributions 中移除。\"\n  action_items:\n    - round: 4\n      action: \"GSM1K 已标注 exploratory。Claim 4 重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 5\n      action: \"将 Claim 4 从 contribution list 中移除，降级为 supplementary observation；收紧为 3 个 contributions\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"ρ≈0.997 vs 31.3% 张力——DIF Audit Protocol (Section 5.4) 只有 3 句话，actionability 严重不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n      note: \"共识方向\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"R1 建议反转 emphasis\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W1: 论文花大量篇幅证明 DIF 存在，但对发现 DIF 后该怎么做几乎为零。R1 AGREE：何时需要 action vs 只需 annotation 未讨论。\"\n  action_items:\n    - round: 5\n      action: \"扩展 Section 5.4：具体 audit 频率、发现高 C% 后的处理流程、DIF-cleaned scores 是否应作为补充报告\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"技术新颖性有限——MH-DIF transplant 需要更清晰论证 LLM-specific 挑战\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"DIF 方法本身无创新\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"cross-subject matching 降级为 well-executed application\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-N2 列为 critical。R1 REBUT→降级 Should-Fix：论文已 self-position 为 empirical contribution (Introduction L19)，transplant 涉及 LLM-specific 适配（de-duplication, temporal cohort, ability confound 控制）。R2 交叉回应后 Excitement 上调至 3.5/5。共识：补充 LLM-specific challenges 讨论即可。\"\n  action_items:\n    - round: 5\n      action: \"Section 3 开头增加 1-2 段：LLM 作为 examinees 的特殊性（local dependence, model family structure, ability 分布非正态）及论文如何应对\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失引用：需补充 2025-2026 IRT/LLM evaluation 最新工作\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - round: 1\n      reviewers: [1, 2]\n      note: \"Lalor/Vania/Balloccu 已补充\"\n    - round: 3\n      reviewers: [1, 2]\n      note: \"Clauser & Mazor (1998) + Nandakumar (1993) 已补充\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"新增 4 篇 missing references：(1) 'Lifting the Benchmark Iceberg with IRT' (2025), (2) Benchmark2 (arXiv:2601.03986), (3) ATLAS/CAT-based LLM eval (Li et al. 2025, 已在 bib 未引用), (4) MedIRT (arXiv:2509.24186)。另有 8 个 orphan bib entries 待清理，holland1988mh year mismatch。\"\n  action_items:\n    - round: 5\n      action: \"引用 Benchmark Iceberg + ATLAS；清理 8 orphan bib entries；修正 holland1988mh year\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# NEW ISSUES (first raised in Round 5)\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic framework 仅验证 single-subject injection，未测试 multi-subject simultaneous contamination\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N1: Proposition 1 ΔFPR=0 是 by construction 的平凡结果——注入 subject X，matching variable 排除 X，信号数学上无法泄漏。现实中 contamination 跨越所有 subjects，此时 cross-subject matching variable 也被污染。R2 AGREE：需要 k∈{2,3,5,10} multi-subject injection 实验。R2 补充：cross-benchmark validation (Section 4.7) 隐含了多基准同时 DIF 的场景，但不等同于控制实验。\"\n  action_items:\n    - round: 5\n      action: \"补充 multi-subject simultaneous injection 实验（k∈{2,3,5,10} subjects），或显式限定 Claim 3 为 single-subject contamination detection\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI [29.4%, 38.1%] 的 resampling unit 和不对称性未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-N3 列为 critical (CI 宽 8.7pp, right-skewed, resampling unit 不明)。R2 REBUT→降级 Should-Fix：整个 CI 在 'roughly one-third' 范围内，qualitative conclusion 不变。共识：报告 resampling strategy，Abstract 加 'approximately'。\"\n  action_items:\n    - round: 5\n      action: \"报告 bootstrap resampling unit (model vs item)；Abstract/Title 用 'approximately 31%' 或报告 CI\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"K=5 quintile stratification 的敏感性分析未在主文呈现\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2 AGREE。Appendix K=20 θ-conditioning FPR=0.312 ≈ K=5，但此关键信息埋在附录。应在主文对比 K=5/10/20 的 C% 变化趋势。\"\n  action_items:\n    - round: 5\n      action: \"Section 4.2 或 Table 1 增加一行 K sensitivity analysis (K=5/10/20)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Yen's Q3 局部依赖对 C% 的 expected inflation 未量化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2 AGREE。11.3% within-subject pairs 超 |Q3|>0.20 是 non-trivial。应通过 simulation 估计此水平 LD 对 Type I error rate 的影响。\"\n  action_items:\n    - round: 5\n      action: \"Simulation 或 permutation-based 分析：估计 11.3% Q3 violation 对 C% 的 expected inflation\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"DIF 术语对 EMNLP 读者不够友好——缺少 running example\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W3 + R1 AGREE。ETS Category A/B/C、α_MH、Δ_MH 等对 NLP 社区陌生。需要用具体 MMLU item 展示 DIF 计算过程。\"\n  action_items:\n    - round: 5\n      action: \"Section 3.2 加一个 running example（具体 MMLU item 展示 2023 vs 2024 cohort 的 DIF 计算）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains (Habba et al. 2026) 的区分缺乏实证验证\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R2-W4 + R1 AGREE。论文只说 'our work is complementary' 一句话，未验证 DIF-flagged items 与 FPC anchor items 的 overlap (Jaccard/enrichment)。这个分析容易做，不做是遗憾。\"\n  action_items:\n    - round: 5\n      action: \"补充 DIF flags vs Growing Pains FPC anchors 的 overlap 分析（Jaccard），或在 Discussion 详细讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W6\"\n  summary: \"Power analysis 假设不透明——IRT 参数、effect size、simulation procedure 未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2 AGREE。Section 4.1 声称 N≥80 达到 TPR 0.68-0.80，但未报告 assumed IRT parameters 和 simulation 细节。\"\n  action_items:\n    - round: 5\n      action: \"Appendix 补充 power analysis 完整设定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 (ground truth meta-critique) 逻辑可逆性——DIF ⊥ web-overlap 的双向解读\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1-W6: DIF ⊥ web-overlap 有两种等价解读 (A: web-overlap 是 wrong ground truth; B: DIF 不检测 contamination)。R2 REBUT with nuance：semi-synthetic 证明 DIF can detect contamination (ΔTPR>0)，所以解读 B 不完全成立——更准确的是 real-world contamination 比 web-overlap 描述的更复杂。R2 认为是 interpretive gap 非 methodological flaw。\"\n  action_items:\n    - round: 5\n      action: \"Discussion 中承认 Claim 2 的双向解读可能性，而非单向指责 web-overlap labels\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED ISSUES (not raised in Round 5)\n# ============================================================\n\n- id: \"RD2-W1\"\n  summary: \"Within-family Llama 2 vs 3 的 61.3% DIF + temporal cohort ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"Round 5 未作为独立问题提出。论文已报告 Cohen's d=-0.17, OVL=76.4%, matched C%=28.9%±0.1%。R1 引用此数据但不作为独立 issue。\"\n  resolution: \"plan_027 确认 temporal cohort ability gap 很小。Ability confound 仅解释 2.4pp。\"\n  resolution_round: 4\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (CFI=0.72) 对 MH 的影响\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF cross-analysis: r=0.09 (p=0.50)。MH 是 nonparametric，不依赖 IRT fit。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 过于完美需 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI = [0.000, 0.000]。Cross-subject stratification 对 within-subject injection 不变是 structural guarantee。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N1\"\n  summary: \"引用问题：幻觉引用 Tutz & Friedman (2007)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"确认为幻觉引用。论文当前版本已不包含。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-W2\"\n  summary: \"与 Growing Pains 的区分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"修订版 §2 已详细对比。但 Round 5 reviewer 认为仍过于简短（见 R5-W5），需要实证验证。\"\n  resolution_round: 2\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"区分文字已有，但缺乏实证验证（overlap 分析）——升级为新 issue R5-W5\"\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加，结果稳健。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"R1-W2\"\n  summary: \"推理-RL 鲁棒性 N=13\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"降级为补充分析。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"RD2-W4\"\n  summary: \"补充分析过多稀释焦点\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 3\n  mentions:\n    - round: 5\n      reviewers: []\n      note: \"Round 5 未独立提出。当前论文已精简，但 R1 仍提到 Abstract 过度密集（堆叠过多数字）。\"\n  action_items:\n    - round: 5\n      action: \"精简 Abstract 至 3-4 个核心数字\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-21T15:29:54.807320+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 13130}, \"error\": \"\"}"}

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

_source line 174 · 2026-05-21T15:32:21.108152+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# 审稿报告 — Round 5 (Fresh Review)\n\n**论文**: Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n**截止日期**: 2026-05-25 AoE\n**审稿模式**: Fresh (重新审稿，2 名 Reviewer，1 轮 + 交叉回应)\n**日期**: 2026-05-21\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 分析大规模应用于 LLM benchmark 评估，基于 METABENCH 数据集（5,227 models × 12,508 MMLU items）发现 31.3% 的 MMLU items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 DIF。跨 6 个基准复现（C% = 17.9–31.3%，45–174× 高于随机基线）。提出 cross-subject matching 的半合成验证框架（ΔFPR = 0.000），并发现 DIF flags 与 web-overlap contamination labels 近乎独立（enrichment ≈ 0.964）。论文声称 4 个贡献：temporal comparability（Claim 1）、ground truth meta-critique（Claim 2）、semi-synthetic validation framework（Claim 3）、DIF as diagnostic lens（Claim 4）。\n\n---\n\n## Strengths\n\n1. **大规模实证贡献**：5,227 models × 27,125 items 的 DIF 分析规模在该领域最大之一；6 个 benchmark 交叉验证提供了强力 replication。31% item instability 对 benchmark 使用者是有直接意义的发现。\n\n2. **系统性 confound 控制**：5 种 cohort design（temporal, ability-quintile, within-family, within-subject, random-split）系统排除替代解释。Matched-ability 分析令人信服地将 ability confounding 限定在 ~2.4pp（Cohen's d = -0.17, matched C% = 28.9% ± 0.1%）。\n\n3. **Ground truth meta-critique 有实际价值**：Claim 2 发现 DIF flags 与 web-overlap labels 几乎独立（enrichment = 0.964, Jaccard = 0.206, φ = 0.012），对 contamination detection 文献中普遍使用 web-overlap 作为 ground truth 的做法提出了合理质疑。\n\n4. **跨学科 transplant 质量高**：将 60+ 年历史的 psychometric DIF 方法引入 NLP evaluation 是有价值的 cross-pollination。执行严谨（threshold sensitivity, multiple testing, architecture homogeneity check）。Figure 1 直观展示 global vs. differential contamination 的区别。\n\n5. **写作整体清晰**：结构合理，方法描述详尽，论文在 8 页内组织了大量实证内容。Limitations 涵盖全面。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical, consensus] **Semi-synthetic framework 仅验证 single-subject injection，生态效度不足**\n- Proposition 1（ΔFPR = 0）是 by construction 的平凡结果：注入 subject X → matching variable 排除 X → 信号数学上无法泄漏。在现实场景中，contamination 同时跨越多个 subjects，此时 cross-subject matching variable 本身被污染，conditional independence 假设不再成立。论文未测试 multi-subject simultaneous injection（k ∈ {2,3,5,10}），因此无法评估框架在现实条件下的有效性。这直接影响 Claim 3 能否作为独立贡献成立。\n- **R1 提出，R2 AGREE**。R2 补充：cross-benchmark validation（Section 4.7）隐含了多基准同时 DIF 的场景，但不等同于控制实验。\n- 建议：补充 multi-subject simultaneous injection 实验，或将 Claim 3 显式限定为 single-subject contamination detection。\n\n**MF-2** [critical, consensus] **核心 framing 的因果模糊性：\"Psychometric Instability\" vs. \"Expected Capability Evolution\"**\n- MH-DIF 标记 **任何** 跨组 conditional item functioning 差异，包括 genuine capability change。ρ = -0.597 的 difficulty-direction interaction（2024 模型难题 gain、简单题 erode）同样（甚至更自然地）可解释为正常的 capability profile shift。标题 \"Psychometric Instability\" 暗示 benchmark 测量问题，但如果 DIF 主要反映模型能力合理演变，则不是 \"instability\" 而是 \"expected differential performance\"。Calendar year cohort 同时混淆了 temporal drift、architecture shift、training data change，论文无法将 DIF signal 归因到具体原因。\n- **R1 提出 (N2)，R2 AGREE with nuance (N3)**。R2 补充：MH 已控制 ability level，Simpson's paradox 和三层控制提供部分反驳（C% after controlling for ability 仍为 31.3%），但 within-stratum profile shift 仍可以是 legitimate。\n- 建议：(1) 软化标题——改为 \"Differential Item Functioning\" 或 \"Measurement Drift\"；(2) 明确区分 item instability vs. differential performance；(3) 补充 within-year cohort（2024-H1 vs H2）的完整分析。\n\n**MF-3** [critical, consensus] **Claim 4 \"DIF as diagnostic lens\" 证据不足**\n- GSM1K correlation (r = -0.478, partial r = -0.385, N = 33, CI = [-0.71, -0.16]) 统计效力严重不足，单个异常模型即可改变结论。Claim 4 的另一支撑——difficulty-direction interaction（ρ = -0.597）——本身解读有歧义（见 MF-2）。论文在 Limitations 中承认 GSM1K 是 exploratory，但 Discussion Section 5.3 和 Introduction Claim 4 的措辞未匹配这一谨慎程度。4 个 contributions 中如果 1 个站不住，贡献度整体打折扣。\n- **R2 提出 (N1)，R1 AGREE (W4)**。\n- 建议：降级 Claim 4 为 exploratory observation，从 contribution list 中移除，收紧为 3 个 contributions。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning] **方法论新颖性论证不充分**\n- MH-DIF 是 1988 年方法，cross-subject matching 有先例（Nandakumar 1993, Donoghue 1993——论文自己承认）。4 个 claims 中 3 个本质是 descriptive findings。论文需更清晰论证 LLM-specific 的方法适配挑战（local dependence, model family structure, ability 分布非正态）。\n- R2 列为 critical，R1 REBUT → 降级为 Should-Fix（论文已 self-position 为 empirical contribution, Introduction L19）。R2 交叉回应后 Excitement 上调至 3.5/5。\n- 建议：Section 3 开头增加 1-2 段讨论 LLM 作为 examinees 的特殊性。\n\n**SF-2** [warning] **Bootstrap CI 报告不完整**\n- 95% CI = [29.4%, 38.1%]，宽 8.7pp，right-skewed。未报告 bootstrap resampling unit（model vs. item）。\n- R1 列为 critical (N3)，R2 REBUT → 降级为 Should-Fix（整个 CI 在 \"roughly one-third\" 范围，qualitative conclusion 不变）。\n- 建议：报告 resampling strategy；Abstract 加 \"approximately\" 或 CI。\n\n**SF-3** [warning] **DIF Audit Protocol (Section 5.4) 过于简略**\n- 仅 3 句话，对于声称 \"LLM benchmarks need psychometric monitoring\" 的论文，practical recommendations 深度不足。ρ ≈ 0.997 说明 aggregate ranking 不受影响，但 25% 模型 rank shift ≥ 100——何时需要 action vs. 只需 annotation 未讨论。\n- R2 提出 (W1)，R1 AGREE。\n\n**SF-4** [warning] **ΔFPR = 0.000 的 robustness check 不足**\n- 注入率固定 20%，仅 5 个 subjects 验证，未讨论 Type II error（cross-subject matching 是否过于保守降低 TPR）。\n- R2 提出 (W2)，R1 AGREE（与 MF-1 互补）。\n\n**SF-5** [warning] **K = 5 分层敏感性分析未在主文呈现**\n- Appendix K = 20 θ-conditioning FPR = 0.312 ≈ K = 5，但此关键信息埋在附录。应在主文对比 K = 5/10/20。\n- R1 提出 (W1)，R2 AGREE。\n\n**SF-6** [warning] **Yen's Q3 局部依赖对 C% 的 inflation 未量化**\n- 11.3% within-subject pairs 超 |Q3| > 0.20 是 non-trivial。应通过 simulation 估计此水平 LD 对 Type I error rate 的影响。\n- R1 提出 (W2)，R2 AGREE。\n\n**SF-7** [warning] **DIF 术语对 EMNLP 读者不够友好**\n- ETS Category A/B/C、α_MH、Δ_MH 对 NLP 社区陌生。缺少 running example。\n- R2 提出 (W3)，R1 AGREE。\n\n**SF-8** [warning] **与 Growing Pains 的区分缺乏实证验证**\n- 论文仅一句 \"our work is complementary\"，未验证 DIF-flagged items 与 FPC anchor items 的 overlap（Jaccard/enrichment）。\n- R2 提出 (W4)，R1 AGREE。\n\n**SF-9** [warning] **引用问题**\n- 8 个 orphan bib entries（chen2025irtnet, choi2026llmjudgeirt, li2025atlas, liang2023helm, mialon2023gaia, ott2022benchmark, wang2024mmlupro, zhang2024gsm1k）\n- holland1988mh year mismatch (bib=1988 vs possible 1986)\n- tao2026selfcritique, liu2026bhi 的 first author mismatch\n- R2 提出 (W5)，R1 AGREE。\n\n**SF-10** [warning] **Claim 2 (ground truth meta-critique) 逻辑可逆**\n- DIF ⊥ web-overlap 有两种等价解读：(A) web-overlap 是 wrong ground truth，或 (B) DIF 不检测 contamination。Semi-synthetic 部分化解了 B（ΔTPR > 0），但生态效度受限（见 MF-1）。\n- R1 提出 (W6)，R2 REBUT with nuance：semi-synthetic 证明 DIF 可以检测 contamination，是 interpretive gap 而非 methodological flaw。\n\n**SF-11** [warning] **Power analysis 假设不透明**\n- Section 4.1 声称 N ≥ 80 达到 TPR 0.68–0.80，但未报告 IRT 参数、effect size、simulation procedure。\n- R1 提出 (W5)，R2 AGREE。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 均认为需要改进（标注 [AGREE]）：\n\n1. **Claim 4 / GSM1K N = 33 不足以支撑独立 contribution** → 降级为 exploratory observation\n2. **Semi-synthetic framework 生态效度有限** → 需 multi-subject injection 或限定 scope\n3. **\"Psychometric Instability\" framing 过强** → 需软化 causal claims + 补充 within-year 分析\n4. **DIF Audit Protocol 过于简略** → 需扩展 actionable recommendations\n5. **K = 5 sensitivity 应在主文呈现**\n6. **Q3 局部依赖影响应量化**\n7. **DIF 术语需要 running example**\n8. **Growing Pains overlap 分析应补充**\n9. **引用需清理和修正**\n\n---\n\n## Reviewer Divergence\n\n以下问题存在分歧（已通过交叉回应解决或记录）：\n\n1. **Novelty 严重程度**：R2 列为 critical，R1 REBUT → 降级 Should-Fix。R1 论点：论文已 self-position 为 empirical contribution，EMNLP 接受此类工作，但需补充 LLM-specific challenges 讨论。R2 交叉回应后 Excitement 上调至 3.5/5，部分接受。\n\n2. **Bootstrap CI 严重程度**：R1 列为 critical，R2 REBUT → 降级 Should-Fix。R2 论点：CI 完全在 \"roughly one-third\" 范围内，qualitative conclusion 不变。\n\n3. **Within-family matched C% ≈ 28.3% 的解读**：R1 认为可能是 K = 5 下的 floor effect；R2 REBUT——K = 20 θ-conditioning 结果（FPR = 0.312）与 K = 5 无差别，反驳 floor effect 假说。分歧保留但非关键。\n\n4. **Claim 2 逻辑可逆性**：R1 认为是 Should-Fix；R2 认为 semi-synthetic 已部分化解，是 interpretive gap 而非 methodological flaw。R2 的 Soundness 4 → 3.5 的调整已考虑此因素。\n\n---\n\n## Questions（需要作者回应）\n\n1. Bootstrap resampling 的 unit 是什么（model-level vs. item-level）？不同策略下 CI 是否有实质变化？\n2. 如果同时对 k 个 subjects 注入 contamination，cross-subject matching 的 ΔFPR 如何随 k 变化？\n3. 论文如何回应 \"31% DIF 中有多少比例是 legitimate capability evolution 而非 measurement instability\" 的问题？是否有定量 decomposition 的可能性？\n4. Yen's Q3 的 11.3% within-subject violation rate 对 C% 的 expected inflation 量级是多少？\n5. DIF-flagged items 与 Growing Pains 的 FPC anchor items 的 overlap 是多少？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同确认以下遗漏（应在 Related Work 中引用或讨论）：\n\n1. **\"Lifting the Benchmark Iceberg with Item-Response Theory\"** (2025, OpenReview) — IRT 揭示 benchmark 实现细节对排名的影响，与本文高度相关\n2. **\"Benchmark2: Systematic Evaluation of LLM Benchmarks\"** (2025, arXiv:2601.03986) — 系统评估 benchmark 质量的框架\n3. **ATLAS / CAT-based LLM evaluation** (Li et al. 2025, 已在 bib 但未引用) — Computerized Adaptive Testing 与 item-level diagnosis 相关\n4. **MedIRT / \"Measuring Competency, Not Performance\"** (2025, arXiv:2509.24186) — 将 IRT 应用于医学 benchmark\n\n此外，8 个 orphan bib entries 应清理。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warnings, 7 info）：\n\n**Warnings:**\n- **Pages 3–5**：连续 3 页无 figure/table（Figure 1 在 p2，下一个 Table 1 在 p6，间隔 4 页），p4-5 有 display equations 和 Proposition 1 缓解了单调感，但快速翻阅时视觉节奏偏平\n- **Pages 1–8**：主正文 8 页仅 4 个 display items（2 fig + 2 table），对实证论文偏低（典型 5–8 个）。建议将 Figure 4（downstream ranking impact）或 Table 3（structural controls）提升到主正文\n\n**Info:**\n- 首页无视觉锚点，Figure 1 在 p2 顶部，可接受\n- Figure 2 axis labels 字号偏小（约 60–65% 正文字号），建议 ≥ 70%\n- 末页 40% 空白可优化\n- Figure 4 散点图部分点重叠密集区辨识度降低\n- Tables 使用 booktabs，格式规范\n- 公式和 Proposition 排版正确\n- References 格式统一，无 [?] 未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.5 | 3.5 |\n| Reproducibility | 4 | 4 | 4 |\n| Clarity | 4 | 4 | 4 |\n\n**置信度**: 4/5（两位 Reviewer 均仔细通读全文及附录，对 DIF 方法论和 LLM evaluation 文献熟悉）\n\n**判断依据**：\n- 这是一篇 well-executed 的大规模实证研究，核心发现（31% MMLU items 跨代不稳定）对 benchmark 使用者有直接价值\n- 6 个 benchmark 的交叉验证和 5 种 cohort design 的 confound 控制展示了扎实的方法论\n- 但存在 3 个 critical 问题：(1) semi-synthetic 框架生态效度不足（single-subject only），(2) 因果 framing 过强（instability vs. capability evolution 不可区分），(3) Claim 4 证据不足\n- 方法论新颖性有限——核心是 off-the-shelf psychometric method 的高质量应用，contributions 偏 descriptive\n- 如果 MF-1 至 MF-3 得到有效 address（特别是 MF-2 的 framing 软化和 MF-3 的 Claim 4 降级），论文有望上升到 4.0（Conference）水平\n- 当前定位：strong Findings / borderline Conference\n\n**EMNLP 2026 评分映射**：3.5 = Borderline Conference（可被主会议接收的边界线）\n\n**如果作者只能修复 3 个问题，优先级为**：\n1. 软化 causal framing + 标题（MF-2）— 成本低、影响大\n2. 补充 multi-subject injection 实验（MF-1）— 加强核心 validation\n3. 降级 Claim 4 为 observation（MF-3）— 避免 overclaiming\n\n---\n\n## Detailed Comments（逐节）\n\n### Title &amp; Abstract\n- 标题 \"Psychometric Instability\" 过强，建议改为 \"Differential Item Functioning\" 或 \"Measurement Drift\"\n- Abstract 数字过度密集（ρ≈0.997, z=-8σ to -49σ, ρ=-0.597 等），建议精简至 3-4 个核心数字\n- Abstract 中 \"31%\" 应加 \"approximately\" 或报告 CI\n\n### Section 1 (Introduction)\n- Claim 4 应降级或移除，收紧为 3 个 contributions\n- \"Our contributions are empirical and methodological, not algorithmic\" (L19) 的 self-positioning 是合适的，但后续 Method 部分未充分展开 LLM-specific challenges\n\n### Section 2 (Related Work)\n- DIF 方法论引用已较全面（Holland & Thayer 1988, Clauser 1998, Nandakumar 1993 等）\n- 与 Growing Pains 的区分过于简短——需补充 overlap 分析\n- 缺失 4 篇 2025-2026 重要相关工作（见 Missing References）\n\n### Section 3 (Method)\n- MH-DIF 描述准确但对 NLP 读者不够友好——需 running example\n- Proposition 1 表述应更谨慎——明确其仅适用于 single-subject injection\n- Cross-subject matching 的 prior art 定位（Nandakumar 1993, Donoghue 1993）已在文中，但应更明确是 application 而非 invention\n\n### Section 4 (Experiments)\n- Section 4.1 power analysis 缺细节\n- Section 4.2 应增加 K sensitivity 和 bootstrap resampling unit 信息\n- Section 4.5 semi-synthetic 需讨论 multi-subject 场景\n- Section 4.6 downstream impact 的 model-specific rank shifts 值得从附录提升到正文\n- Section 4.7 cross-benchmark 6-month window 结果（C% = 34.35%）仅 one-liner，应展开\n\n### Section 5 (Discussion)\n- Section 5.1: 应明确承认 \"instability\" 与 \"capability evolution\" 不可分\n- Section 5.2: 应承认 Claim 2 的双向解读可能性\n- Section 5.3: GSM1K 应标注 preliminary/exploratory\n- Section 5.4: DIF Audit Protocol 需大幅扩展\n\n### Limitations\n- 覆盖全面（方法论、能力混淆、样本量、因果归因、benchmark 范围、temporal 定义）\n- 略长（6 段），可适当精简\n\n### References\n- 8 orphan entries 待清理\n- holland1988mh year 待核实\n- 部分 first author mismatch 待修正\n\n### Formatting\n- 正文 8 页，合规\n- Double-blind 匿名性合规\n- ACL template 合规\n- 主正文 display items 偏少（4 个），建议从附录提升 1-2 个"
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
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# 审稿报告 — Round 5 (Fresh Review)\n\n**论文**: Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n**截止日期**: 2026-05-25 AoE\n**审稿模式**: Fresh (重新审稿，2 名 Reviewer，1 轮 + 交叉回应)\n**日期**: 2026-05-21\n\n---\n\n## Summary\n\n本文将教育测量中的 Mantel-Haenszel Differential Item Functioning (MH-DIF) 分析大规模应用于 LLM benchmark 评估，基于 METABENCH 数据集（5,227 models × 12,508 MMLU items）发现 31.3% 的 MMLU items 在 2023 vs 2024 模型代际间表现出 ETS Category C 级别的 DIF。跨 6 个基准复现（C% = 17.9–31.3%，45–174× 高于随机基线）。提出 cross-subject matching 的半合成验证框架（ΔFPR = 0.000），并发现 DIF flags 与 web-overlap contamination labels 近乎独立（enrichment ≈ 0.964）。论文声称 4 个贡献：temporal comparability（Claim 1）、ground truth meta-critique（Claim 2）、semi-synthetic validation framework（Claim 3）、DIF as diagnostic lens（Claim 4）。\n\n---\n\n## Strengths\n\n1. **大规模实证贡献**：5,227 models × 27,125 items 的 DIF 分析规模在该领域最大之一；6 个 benchmark 交叉验证提供了强力 replication。31% item instability 对 benchmark 使用者是有直接意义的发现。\n\n2. **系统性 confound 控制**：5 种 cohort design（temporal, ability-quintile, within-family, within-subject, random-split）系统排除替代解释。Matched-ability 分析令人信服地将 ability confounding 限定在 ~2.4pp（Cohen's d = -0.17, matched C% = 28.9% ± 0.1%）。\n\n3. **Ground truth meta-critique 有实际价值**：Claim 2 发现 DIF flags 与 web-overlap labels 几乎独立（enrichment = 0.964, Jaccard = 0.206, φ = 0.012），对 contamination detection 文献中普遍使用 web-overlap 作为 ground truth 的做法提出了合理质疑。\n\n4. **跨学科 transplant 质量高**：将 60+ 年历史的 psychometric DIF 方法引入 NLP evaluation 是有价值的 cross-pollination。执行严谨（threshold sensitivity, multiple testing, architecture homogeneity check）。Figure 1 直观展示 global vs. differential contamination 的区别。\n\n5. **写作整体清晰**：结构合理，方法描述详尽，论文在 8 页内组织了大量实证内容。Limitations 涵盖全面。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical, consensus] **Semi-synthetic framework 仅验证 single-subject injection，生态效度不足**\n- Proposition 1（ΔFPR = 0）是 by construction 的平凡结果：注入 subject X → matching variable 排除 X → 信号数学上无法泄漏。在现实场景中，contamination 同时跨越多个 subjects，此时 cross-subject matching variable 本身被污染，conditional independence 假设不再成立。论文未测试 multi-subject simultaneous injection（k ∈ {2,3,5,10}），因此无法评估框架在现实条件下的有效性。这直接影响 Claim 3 能否作为独立贡献成立。\n- **R1 提出，R2 AGREE**。R2 补充：cross-benchmark validation（Section 4.7）隐含了多基准同时 DIF 的场景，但不等同于控制实验。\n- 建议：补充 multi-subject simultaneous injection 实验，或将 Claim 3 显式限定为 single-subject contamination detection。\n\n**MF-2** [critical, consensus] **核心 framing 的因果模糊性：\"Psychometric Instability\" vs. \"Expected Capability Evolution\"**\n- MH-DIF 标记 **任何** 跨组 conditional item functioning 差异，包括 genuine capability change。ρ = -0.597 的 difficulty-direction interaction（2024 模型难题 gain、简单题 erode）同样（甚至更自然地）可解释为正常的 capability profile shift。标题 \"Psychometric Instability\" 暗示 benchmark 测量问题，但如果 DIF 主要反映模型能力合理演变，则不是 \"instability\" 而是 \"expected differential performance\"。Calendar year cohort 同时混淆了 temporal drift、architecture shift、training data change，论文无法将 DIF signal 归因到具体原因。\n- **R1 提出 (N2)，R2 AGREE with nuance (N3)**。R2 补充：MH 已控制 ability level，Simpson's paradox 和三层控制提供部分反驳（C% after controlling for ability 仍为 31.3%），但 within-stratum profile shift 仍可以是 legitimate。\n- 建议：(1) 软化标题——改为 \"Differential Item Functioning\" 或 \"Measurement Drift\"；(2) 明确区分 item instability vs. differential performance；(3) 补充 within-year cohort（2024-H1 vs H2）的完整分析。\n\n**MF-3** [critical, consensus] **Claim 4 \"DIF as diagnostic lens\" 证据不足**\n- GSM1K correlation (r = -0.478, partial r = -0.385, N = 33, CI = [-0.71, -0.16]) 统计效力严重不足，单个异常模型即可改变结论。Claim 4 的另一支撑——difficulty-direction interaction（ρ = -0.597）——本身解读有歧义（见 MF-2）。论文在 Limitations 中承认 GSM1K 是 exploratory，但 Discussion Section 5.3 和 Introduction Claim 4 的措辞未匹配这一谨慎程度。4 个 contributions 中如果 1 个站不住，贡献度整体打折扣。\n- **R2 提出 (N1)，R1 AGREE (W4)**。\n- 建议：降级 Claim 4 为 exploratory observation，从 contribution list 中移除，收紧为 3 个 contributions。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning] **方法论新颖性论证不充分**\n- MH-DIF 是 1988 年方法，cross-subject matching 有先例（Nandakumar 1993, Donoghue 1993——论文自己承认）。4 个 claims 中 3 个本质是 descriptive findings。论文需更清晰论证 LLM-specific 的方法适配挑战（local dependence, model family structure, ability 分布非正态）。\n- R2 列为 critical，R1 REBUT → 降级为 Should-Fix（论文已 self-position 为 empirical contribution, Introduction L19）。R2 交叉回应后 Excitement 上调至 3.5/5。\n- 建议：Section 3 开头增加 1-2 段讨论 LLM 作为 examinees 的特殊性。\n\n**SF-2** [warning] **Bootstrap CI 报告不完整**\n- 95% CI = [29.4%, 38.1%]，宽 8.7pp，right-skewed。未报告 bootstrap resampling unit（model vs. item）。\n- R1 列为 critical (N3)，R2 REBUT → 降级为 Should-Fix（整个 CI 在 \"roughly one-third\" 范围，qualitative conclusion 不变）。\n- 建议：报告 resampling strategy；Abstract 加 \"approximately\" 或 CI。\n\n**SF-3** [warning] **DIF Audit Protocol (Section 5.4) 过于简略**\n- 仅 3 句话，对于声称 \"LLM benchmarks need psychometric monitoring\" 的论文，practical recommendations 深度不足。ρ ≈ 0.997 说明 aggregate ranking 不受影响，但 25% 模型 rank shift ≥ 100——何时需要 action vs. 只需 annotation 未讨论。\n- R2 提出 (W1)，R1 AGREE。\n\n**SF-4** [warning] **ΔFPR = 0.000 的 robustness check 不足**\n- 注入率固定 20%，仅 5 个 subjects 验证，未讨论 Type II error（cross-subject matching 是否过于保守降低 TPR）。\n- R2 提出 (W2)，R1 AGREE（与 MF-1 互补）。\n\n**SF-5** [warning] **K = 5 分层敏感性分析未在主文呈现**\n- Appendix K = 20 θ-conditioning FPR = 0.312 ≈ K = 5，但此关键信息埋在附录。应在主文对比 K = 5/10/20。\n- R1 提出 (W1)，R2 AGREE。\n\n**SF-6** [warning] **Yen's Q3 局部依赖对 C% 的 inflation 未量化**\n- 11.3% within-subject pairs 超 |Q3| > 0.20 是 non-trivial。应通过 simulation 估计此水平 LD 对 Type I error rate 的影响。\n- R1 提出 (W2)，R2 AGREE。\n\n**SF-7** [warning] **DIF 术语对 EMNLP 读者不够友好**\n- ETS Category A/B/C、α_MH、Δ_MH 对 NLP 社区陌生。缺少 running example。\n- R2 提出 (W3)，R1 AGREE。\n\n**SF-8** [warning] **与 Growing Pains 的区分缺乏实证验证**\n- 论文仅一句 \"our work is complementary\"，未验证 DIF-flagged items 与 FPC anchor items 的 overlap（Jaccard/enrichment）。\n- R2 提出 (W4)，R1 AGREE。\n\n**SF-9** [warning] **引用问题**\n- 8 个 orphan bib entries（chen2025irtnet, choi2026llmjudgeirt, li2025atlas, liang2023helm, mialon2023gaia, ott2022benchmark, wang2024mmlupro, zhang2024gsm1k）\n- holland1988mh year mismatch (bib=1988 vs possible 1986)\n- tao2026selfcritique, liu2026bhi 的 first author mismatch\n- R2 提出 (W5)，R1 AGREE。\n\n**SF-10** [warning] **Claim 2 (ground truth meta-critique) 逻辑可逆**\n- DIF ⊥ web-overlap 有两种等价解读：(A) web-overlap 是 wrong ground truth，或 (B) DIF 不检测 contamination。Semi-synthetic 部分化解了 B（ΔTPR > 0），但生态效度受限（见 MF-1）。\n- R1 提出 (W6)，R2 REBUT with nuance：semi-synthetic 证明 DIF 可以检测 contamination，是 interpretive gap 而非 methodological flaw。\n\n**SF-11** [warning] **Power analysis 假设不透明**\n- Section 4.1 声称 N ≥ 80 达到 TPR 0.68–0.80，但未报告 IRT 参数、effect size、simulation procedure。\n- R1 提出 (W5)，R2 AGREE。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 均认为需要改进（标注 [AGREE]）：\n\n1. **Claim 4 / GSM1K N = 33 不足以支撑独立 contribution** → 降级为 exploratory observation\n2. **Semi-synthetic framework 生态效度有限** → 需 multi-subject injection 或限定 scope\n3. **\"Psychometric Instability\" framing 过强** → 需软化 causal claims + 补充 within-year 分析\n4. **DIF Audit Protocol 过于简略** → 需扩展 actionable recommendations\n5. **K = 5 sensitivity 应在主文呈现**\n6. **Q3 局部依赖影响应量化**\n7. **DIF 术语需要 running example**\n8. **Growing Pains overlap 分析应补充**\n9. **引用需清理和修正**\n\n---\n\n## Reviewer Divergence\n\n以下问题存在分歧（已通过交叉回应解决或记录）：\n\n1. **Novelty 严重程度**：R2 列为 critical，R1 REBUT → 降级 Should-Fix。R1 论点：论文已 self-position 为 empirical contribution，EMNLP 接受此类工作，但需补充 LLM-specific challenges 讨论。R2 交叉回应后 Excitement 上调至 3.5/5，部分接受。\n\n2. **Bootstrap CI 严重程度**：R1 列为 critical，R2 REBUT → 降级 Should-Fix。R2 论点：CI 完全在 \"roughly one-third\" 范围内，qualitative conclusion 不变。\n\n3. **Within-family matched C% ≈ 28.3% 的解读**：R1 认为可能是 K = 5 下的 floor effect；R2 REBUT——K = 20 θ-conditioning 结果（FPR = 0.312）与 K = 5 无差别，反驳 floor effect 假说。分歧保留但非关键。\n\n4. **Claim 2 逻辑可逆性**：R1 认为是 Should-Fix；R2 认为 semi-synthetic 已部分化解，是 interpretive gap 而非 methodological flaw。R2 的 Soundness 4 → 3.5 的调整已考虑此因素。\n\n---\n\n## Questions（需要作者回应）\n\n1. Bootstrap resampling 的 unit 是什么（model-level vs. item-level）？不同策略下 CI 是否有实质变化？\n2. 如果同时对 k 个 subjects 注入 contamination，cross-subject matching 的 ΔFPR 如何随 k 变化？\n3. 论文如何回应 \"31% DIF 中有多少比例是 legitimate capability evolution 而非 measurement instability\" 的问题？是否有定量 decomposition 的可能性？\n4. Yen's Q3 的 11.3% within-subject violation rate 对 C% 的 expected inflation 量级是多少？\n5. DIF-flagged items 与 Growing Pains 的 FPC anchor items 的 overlap 是多少？\n\n---\n\n## Missing References\n\n两位 Reviewer 共同确认以下遗漏（应在 Related Work 中引用或讨论）：\n\n1. **\"Lifting the Benchmark Iceberg with Item-Response Theory\"** (2025, OpenReview) — IRT 揭示 benchmark 实现细节对排名的影响，与本文高度相关\n2. **\"Benchmark2: Systematic Evaluation of LLM Benchmarks\"** (2025, arXiv:2601.03986) — 系统评估 benchmark 质量的框架\n3. **ATLAS / CAT-based LLM evaluation** (Li et al. 2025, 已在 bib 但未引用) — Computerized Adaptive Testing 与 item-level diagnosis 相关\n4. **MedIRT / \"Measuring Competency, Not Performance\"** (2025, arXiv:2509.24186) — 将 IRT 应用于医学 benchmark\n\n此外，8 个 orphan bib entries 应清理。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warnings, 7 info）：\n\n**Warnings:**\n- **Pages 3–5**：连续 3 页无 figure/table（Figure 1 在 p2，下一个 Table 1 在 p6，间隔 4 页），p4-5 有 display equations 和 Proposition 1 缓解了单调感，但快速翻阅时视觉节奏偏平\n- **Pages 1–8**：主正文 8 页仅 4 个 display items（2 fig + 2 table），对实证论文偏低（典型 5–8 个）。建议将 Figure 4（downstream ranking impact）或 Table 3（structural controls）提升到主正文\n\n**Info:**\n- 首页无视觉锚点，Figure 1 在 p2 顶部，可接受\n- Figure 2 axis labels 字号偏小（约 60–65% 正文字号），建议 ≥ 70%\n- 末页 40% 空白可优化\n- Figure 4 散点图部分点重叠密集区辨识度降低\n- Tables 使用 booktabs，格式规范\n- 公式和 Proposition 排版正确\n- References 格式统一，无 [?] 未解析引用\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.5 | 3.5 |\n| Reproducibility | 4 | 4 | 4 |\n| Clarity | 4 | 4 | 4 |\n\n**置信度**: 4/5（两位 Reviewer 均仔细通读全文及附录，对 DIF 方法论和 LLM evaluation 文献熟悉）\n\n**判断依据**：\n- 这是一篇 well-executed 的大规模实证研究，核心发现（31% MMLU items 跨代不稳定）对 benchmark 使用者有直接价值\n- 6 个 benchmark 的交叉验证和 5 种 cohort design 的 confound 控制展示了扎实的方法论\n- 但存在 3 个 critical 问题：(1) semi-synthetic 框架生态效度不足（single-subject only），(2) 因果 framing 过强（instability vs. capability evolution 不可区分），(3) Claim 4 证据不足\n- 方法论新颖性有限——核心是 off-the-shelf psychometric method 的高质量应用，contributions 偏 descriptive\n- 如果 MF-1 至 MF-3 得到有效 address（特别是 MF-2 的 framing 软化和 MF-3 的 Claim 4 降级），论文有望上升到 4.0（Conference）水平\n- 当前定位：strong Findings / borderline Conference\n\n**EMNLP 2026 评分映射**：3.5 = Borderline Conference（可被主会议接收的边界线）\n\n**如果作者只能修复 3 个问题，优先级为**：\n1. 软化 causal framing + 标题（MF-2）— 成本低、影响大\n2. 补充 multi-subject injection 实验（MF-1）— 加强核心 validation\n3. 降级 Claim 4 为 observation（MF-3）— 避免 overclaiming\n\n---\n\n## Detailed Comments（逐节）\n\n### Title &amp; Abstract\n- 标题 \"Psychometric Instability\" 过强，建议改为 \"Differential Item Functioning\" 或 \"Measurement Drift\"\n- Abstract 数字过度密集（ρ≈0.997, z=-8σ to -49σ, ρ=-0.597 等），建议精简至 3-4 个核心数字\n- Abstract 中 \"31%\" 应加 \"approximately\" 或报告 CI\n\n### Section 1 (Introduction)\n- Claim 4 应降级或移除，收紧为 3 个 contributions\n- \"Our contributions are empirical and methodological, not algorithmic\" (L19) 的 self-positioning 是合适的，但后续 Method 部分未充分展开 LLM-specific challenges\n\n### Section 2 (Related Work)\n- DIF 方法论引用已较全面（Holland & Thayer 1988, Clauser 1998, Nandakumar 1993 等）\n- 与 Growing Pains 的区分过于简短——需补充 overlap 分析\n- 缺失 4 篇 2025-2026 重要相关工作（见 Missing References）\n\n### Section 3 (Method)\n- MH-DIF 描述准确但对 NLP 读者不够友好——需 running example\n- Proposition 1 表述应更谨慎——明确其仅适用于 single-subject injection\n- Cross-subject matching 的 prior art 定位（Nandakumar 1993, Donoghue 1993）已在文中，但应更明确是 application 而非 invention\n\n### Section 4 (Experiments)\n- Section 4.1 power analysis 缺细节\n- Section 4.2 应增加 K sensitivity 和 bootstrap resampling unit 信息\n- Section 4.5 semi-synthetic 需讨论 multi-subject 场景\n- Section 4.6 downstream impact 的 model-specific rank shifts 值得从附录提升到正文\n- Section 4.7 cross-benchmark 6-month window 结果（C% = 34.35%）仅 one-liner，应展开\n\n### Section 5 (Discussion)\n- Section 5.1: 应明确承认 \"instability\" 与 \"capability evolution\" 不可分\n- Section 5.2: 应承认 Claim 2 的双向解读可能性\n- Section 5.3: GSM1K 应标注 preliminary/exploratory\n- Section 5.4: DIF Audit Protocol 需大幅扩展\n\n### Limitations\n- 覆盖全面（方法论、能力混淆、样本量、因果归因、benchmark 范围、temporal 定义）\n- 略长（6 段），可适当精简\n\n### References\n- 8 orphan entries 待清理\n- holland1988mh year 待核实\n- 部分 first author mismatch 待修正\n\n### Formatting\n- 正文 8 页，合规\n- Double-blind 匿名性合规\n- ACL template 合规\n- 主正文 display items 偏少（4 个），建议从附录提升 1-2 个"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-21T15:32:25.528068+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4419
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-21T15:32:34.928638+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6+0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '执行 Round 1 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛性'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-21T15:32:34.929058+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 178 · 2026-05-21T15:32:43.181846+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿完成摘要**：

- **Overall**: 3.5 / 5（Borderline Conference）
- **两位 Reviewer 评分一致**：Soundness 3.5, Excitement 3.5, Reproducibility 4, Clarity 4
- **3 个 Must-Fix**（共识）：
  1. Semi-synthetic 框架仅验证 single-subject injection，需补充 multi-subject 实验
  2. "Psychometric Instability" framing 过强，无法区分 instability vs capability evolution，需软化标题和因果表述
  3. Claim 4 (DIF as diagnostic lens) 证据不足（GSM1K N=33），应降级为 exploratory observation
- **11 个 Should-Fix**：novelty 论证、bootstrap CI 报告、audit protocol 扩展、ΔFPR robustness、K sensitivity、Q3 量化、DIF 术语友好度、Growing Pains overlap、引用修复、Claim 2 双向解读、power analysis 透明度
- **Issue Tracker 已更新**：13 个 open issues（3 critical + 10 warning）
- **视觉审查**：2 warnings（pages 3-5 无 display item、主正文 display items 偏少）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 20

## Round 20

2 recorded events


### User

_source line 179 · 2026-05-21T15:32:44.305282+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心判断：

- **R1-N1 (multi-subject injection)**：同意是实质缺陷，Claim 3 需要限定范围或补实验
- **R1-N2 (instability vs evolution)**：同意标题过强，与我的 N3 互补——两者共同指向 temporal cohort 的 confound 问题
- **R1-N3 (CI precision)**：反驳——qualitative conclusion 不受影响，应降为 Should-Fix
- **R1-W6 (Claim 2 逻辑可逆)**：部分同意，但 semi-synthetic 的 positive detection power (Section 4.5, Figure 2) 可化解 "DIF 根本不检测 contamination" 的极端解读
- 综合调整：Soundness 从 4 降至 3.5（因 N1+N2 的联合影响），Excitement 从 3 升至 3.5（认可 transplant 质量），Overall 维持 3.5

---

[Reviewer 2 审稿结果]:
交叉回应已在上一轮提交完毕（包含对 R1 全部 Must-Fix N1-N3 和 Should-Fix W1-W6 的逐条 [AGREE]/[REBUT] 回应，以及综合评估调整）。无需重复提交。

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

_source line 180 · 2026-05-21T15:32:55.575147+00:00_

审稿报告已投递至 Research Director。

**审稿完成摘要**：

- **Overall**: 3.5 / 5（Borderline Conference）
- **两位 Reviewer 一致**：Soundness 3.5, Excitement 3.5, Reproducibility 4, Clarity 4
- **3 个 Must-Fix**：(1) semi-synthetic 框架需补充 multi-subject injection 实验，(2) "Psychometric Instability" 标题/framing 过强需软化，(3) Claim 4 应降级为 exploratory observation
- **11 个 Should-Fix**：novelty 论证、bootstrap CI 报告、audit protocol 扩展、ΔFPR robustness、K 敏感性、Q3 量化、DIF 术语、Growing Pains overlap、引用清理、Claim 2 逻辑可逆性、power analysis 透明度
- **Issue Tracker 已同步更新**（`review_issues.yaml`，5 个 recurring + 7 个 new + 8 个 resolved）
- **视觉审查**：2 warnings（pages 3-5 无 display item 间隔、主正文 display items 偏少）
- **建议修复优先级**：软化 framing > multi-subject injection > 降级 Claim 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 21

## Round 21

2 recorded events


### User

_source line 181 · 2026-05-21T17:46:18.060115+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 修订版论文审稿报告（Novelty & Related Work 侧重）

### ⚠️ 版本不一致提示

Director 的 brief 描述了一个 **10 references、标题 "Temporal Measurement Drift..."** 的版本。但我在 PDF 中看到的实际论文有以下特征：
- **标题**：*Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models*
- **References**: ~55+ 条（非 10 条）
- **Contributions**: 3 个（semi-synthetic framework 为 primary）
- **Related Work**: 4 个结构化子节，覆盖 contamination detection、IRT in LLM、DIF methodology、benchmark quality
- **新增内容**：multi-subject injection (k∈{1,3,5,10,20})、LLM-specific challenges 节、BHI 和 Benchmark² 引用

以下审稿基于 **我实际阅读的当前 PDF 版本**，而非 brief 中描述的 10-reference 版本。若 Director 需要我审其他版本，请告知。

---

## 维度评分（1-5, ACL ARR）

| 维度 | 分数 | 理由 |
|------|------|------|
| **Novelty/Excitement** | 3.5/5 | 核心方法（MH-DIF）是 1988 年标准技术，novelty 主要在 application domain + semi-synthetic validation framework。修订版新增 "LLM-specific challenges" 节（Page 5）论证了 transplant 的非平凡性（deterministic responses violate local independence, bimodal ability distribution, no natural demographic groups），比初稿大幅进步。Semi-synthetic framework 升为 primary contribution 是正确的重心调整。但 cross-subject matching 仍有 psychometric 先例（Nandakumar 1993, Donoghue & Allen 1993）。对 EMNLP main 来说，novelty 在 borderline——高质量 transplant + 有价值的 empirical findings，但不是 new methodology。 |
| **Significance** | 3.5/5 | 31% temporal DIF 发现对 benchmark 使用者有直接警示价值；ground truth meta-critique 对 contamination detection 文献是有用的补充；cross-benchmark 复现（6 benchmarks）增强可信度。但 practical recommendations（Section 5.4 "DIF Audit Protocol"）仍然过于简略——只有 3 句话（"trigger whenever ≥500 new models accumulate, using cross-subject matching, flag items labeled 'unstable'"），缺乏可操作的 workflow。如果论文希望改变社区行为，这部分需要更多深度。 |
| **Clarity/Writing** | 4/5 | 修订后叙事更聚焦：3 contributions 代替 4 个，"Temporal Measurement Drift" 比 "Psychometric Instability" 更准确。Figure 1（ICC 直觉图）依然出色。Section structure 合理。但 DIF 术语密度仍然较高——ETS Category A/B/C、α_MH、Δ_MH 对 NLP 读者仍不够直观，缺少 running example。 |
| **Related Work Completeness** | 4/5 | 大幅改善。4 个结构化子节覆盖面广：Contamination Detection（8+ works）、IRT in LLM Evaluation（Lalor 2019, Vania 2021, PSN-IRT, tinyBenchmarks, ATLAS, Growing Pains, Hardy 2026）、DIF Methodology（Holland 1988, Clauser 1998, Swaminathan 1990, SIBTEST, Zumbo 1999, Meredith 1993 等）、Benchmark Quality（BHI Zhu & Huang 2026, Benchmark² Qian & Huang 2026, Dynabench, LiveBench, Chatbot Arena）。仅剩 1-2 个 minor gaps（见下）。 |

---

## 主要优势（≥3）

**S1. Semi-synthetic framework 的实质性扩展**：修订版新增 multi-subject injection（k∈{1,3,5,10,20}），直接回应了 R1 Round 1 的核心批评。结果显示 ΔFPR 在 k≤5（≤9% of domains）时仅 0.007，k=10 时升至 0.026-0.069（Section 4.5, Figure 3）。这将 Claim 3 的适用边界从 single-subject 推广到了 multi-domain，是有意义的改进。cross-subject matching 现在有了更清晰的 validity boundary：当 contamination 覆盖 ≥93% domains 时保证失效。

**S2. "LLM-specific challenges" 节有效论证了 transplant 非平凡性**（Page 5）：三个论点——(1) 确定性 response 违反 local independence，motivating quintile-based 而非 parametric stratification；(2) 能力分布 bimodal（base vs. instruction-tuned），cross-subject matching 处理多维性；(3) MMLU 57 subjects 跨多 latent dimensions，而 MH 假设一维性。这显著加强了方法论 positioning，比初稿的纯"apply and report"框架好得多。

**S3. 叙事重心调整成功**：将 semi-synthetic framework 升为 primary contribution、empirical characterization 降为第三，正确反映了论文的实际创新点。"Temporal Measurement Drift" 标题比 "Psychometric Instability" 更准确——drift 是中性的描述，不预判是 benchmark flaw 还是 capability evolution。"Our contributions are methodological and empirical, not algorithmic"（Page 2）的自我定位也是明智的。

**S4. 规模和严谨性不减**：5,227 models × 12,508 items、5 种 cohort design、3 层结构控制（matched-ability、IRT θ-conditioning、random-split）、6 benchmarks cross-validation——这些在修订中都保留了，甚至有所加强（multi-subject injection）。

---

## 主要弱点（≥3）

**W1. "DIF as Diagnostic Lens"（Section 5.3）证据仍然薄弱**
GSM1K correlation（r = −0.478, partial r = −0.385, N = 33）仍然是支撑这个 claim 的唯一定量证据。修订版将其从独立 contribution 降为 Discussion 节——这是正确的降级——但 Section 5.3 仍然以两段文字和一个 N=33 的 correlation 来论证 "DIF captures behavioral change distinct from memorization"。
- **GSMIK** 的 partial r = −0.385 只解释 ~15% 方差
- N=33 的 power 不足以排除 moderate-to-large 的 alternative effect sizes
- 论文说 Section 4.7 的 cross-benchmark replication "confirms generality"，但 Table 3 只报告了 C% ranges，没有在其他 benchmarks 上复现 "diagnostic lens" 的 claim

如果作者保留 Section 5.3，应补充 MMLU 全量数据上的 DIF-item diagnostic value 分析，或在 Limitations 中明确承认 N=33 的局限性。

**W2. Temporal cohort 定义的 confound 问题仍未充分解决**
Calendar year（2023 vs 2024）仍是主要 cohort 定义。虽然论文有 5 种 cohort design 和 Appendix B 的 within-year check，但核心发现 "31% temporal DIF" 中的 "temporal" 仍然混淆了：
- Architecture shift（decoder-only 内部仍有 Llama/Mistral/GPT 的巨大差异）
- Training data shift（2024 模型的训练数据 cutoff 不同）
- Post-training methodology（RLHF/DPO/KTO 等）
- Genuine temporal capability evolution

Section 4.4 的 Simpson's paradox 分析（LR χ² = 647）证明 item properties predict DIF，但不能排除 cohort heterogeneity 作为 confound。论文需要更明确地承认 "temporal DIF" 可能包含 "cohort compositional DIF" 的成分。

**W3. Practical recommendations 过于空洞**
Section 5.4 "Recommended DIF Audit Protocol" 只有 3 句话：trigger at ≥500 models、use cross-subject matching、flag unstable items + annotate。这对于声称 "LLM benchmarks need psychometric monitoring alongside score reporting"（Conclusion）的论文来说远远不够。
- 缺少具体 workflow（谁来做？多久一次？工具如何集成到现有 benchmark pipelines？）
- 缺少 threshold sensitivity 讨论（为什么 ≥500？100 够吗？1000 更好？）
- 缺少与 Growing Pains 的 FPC 工作流如何集成的讨论

**W4. "Instability ≠ invalidity" 的 nuance 虽好但未 fully resolve 读者疑虑**
ρ ≈ 0.997 说明 aggregate rankings 几乎不变，但 Figure 4 显示 individual model families 有 systematic rank shifts（Llama-3 gain +53 median positions, Mistral lose 35）。论文说 "diagnostic, not destructive"，但 Figure 4 其实暗示 **DIF 对特定 model families 的评价有实质影响**——如果你只关心 Mistral vs Llama 的相对排名，31% DIF items 确实会改变结论。论文应更诚实地讨论 "对谁 invalid"（aggregate ≈ 不变; family-specific ≈ 可能变化显著）。

---

## Questions to Authors（≥2）

**Q1.** Section 4.5 新增的 multi-subject injection 实验显示 k=10 时 ΔFPR 升至 0.026-0.069，k=20 时 "matching variable integrity" 受损（Section A, Figure 3）。在 MMLU 57 subjects 中，如果 real-world contamination 同时影响 >10 subjects（很可能，因为 web scraping 是全局的），cross-subject matching 的 FPR 保证是否实际上并不成立？论文能否估计 METABENCH 数据中 contamination 实际覆盖了多少 subjects？

**Q2.** Figure 4 显示 Llama-3 derivatives 在 stable-only ranking 中 gain +53 positions，而 Mistral-based 模型 lose 35 positions。这意味着 DIF items 系统性地 favor 某些 model families。如果 benchmark 维护者接受论文建议移除 DIF items，这实际上是在改变 model families 之间的 competitive landscape。论文如何确保 "DIF-cleaned" ranking 不是另一种形式的 bias？

**Q3.** 论文引用了 BHI (Zhu & Huang, 2026) 和 Benchmark² (Qian & Huang, 2026) 作为 benchmark quality 评估框架。这两个框架评估 benchmark 的 **discriminative power** 和 **saturation**——与本文的 **temporal stability** 维度不同。是否有可能将 temporal DIF rate 作为 BHI 的第四个维度（或 "temporal health" 指标）集成？这会显著增强论文的 practical significance。

---

## Preliminary Overall Assessment

**Overall: 3.5 — Borderline Conference**

### 校准理由

**上行因素（toward 4.0 Conference）**：
- 修订版显著改善：multi-subject injection 补实验、LLM-specific challenges 论证 transplant 价值、contributions 重组更合理
- 大规模实证（5,227 models × 6 benchmarks）加上 semi-synthetic framework，contribution density 足够
- 发现对社区有实际价值（31% DIF 是 actionable warning）
- Related work 现在 comprehensive

**下行因素（toward 3.0 Findings）**：
- 核心方法仍是 off-the-shelf MH-DIF + 已有的 cross-subject matching
- Claim 4（now Section 5.3）的 GSM1K N=33 证据太弱，应删除或大幅加强
- Practical recommendations 空洞，与 "需要 psychometric monitoring" 的主张不匹配
- Temporal cohort 的 confound 问题未完全化解——"temporal drift" 可能部分是 "cohort compositional difference"

**与 R1 Round 1 的对齐**：R1 也给了 3.5（Borderline Conference），我们在核心判断上一致。修订版有效回应了部分批评（multi-subject injection 回应 R1-N1，标题软化回应 R1-N2），但未完全解决所有问题。

**对 Director 提问的直接回答**：
- *DIF 是 35 年老方法，applying to LLM benchmarks 够不够 novelty？*— 修订版通过 LLM-specific challenges 和 semi-synthetic framework 强化了 case，但对严格的 novelty 标准仍然 borderline。如果评审委员会重视 empirical contributions（如 EMNLP 2024 的 benchmark track），这足够；如果要求 methodological innovation，不够。
- *10 references 是否 red flag？*— 当前版本有 55+ references，这个问题不存在。Director 的 brief 可能基于更早的草稿。
- *Semi-synthetic framework 作为 primary contribution 是否有足够 space？*— Section 3.4 + 4.5 + Proposition 1 + multi-subject injection + Figure 2-3，约 1.5 pages。对 primary contribution 来说偏紧凑但 adequate。
- *Ground truth meta-critique 是否 novel？*— 对 psychometrics 专家来说 "global exposure ≠ differential functioning" 是 obvious；对 NLP 社区来说是 useful reminder。作为独立 contribution 稍弱，但作为 semi-synthetic framework 的 motivation 很好。
- *ConStat/DVD comparison 是否公平？*— 论文在 MCQ benchmarks 上测试这些方法，而它们本就面向 MCQ 或通用 format，所以 comparison 是 fair。

**最终判断**：如果 Section 5.3 的 N=33 evidence 得到加强或删除，且 Section 5.4 的 practical recommendations 扩展，我会提升至 **4.0 (Conference)**。当前维持 **3.5 (Borderline Conference)**。

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

_source line 182 · 2026-05-21T17:46:59.361207+00:00_

审稿报告已于此前提交至 Research Director（Overall 3.5, Borderline Conference）。

Reviewer 2 这份报告审查的是**修订后的论文版本**（标题已改为 "Temporal Measurement Drift..."，新增 multi-subject injection 实验、LLM-specific challenges 节、contributions 重组为 3 个），与我们 Round 1 审查的原始版本不同。

**关键信息摘要**（供 Research Director 参考）：

R2 对修订版的评价：
- **Overall 维持 3.5**，但指出修订版有效回应了多个 MF 问题
- **已解决**：MF-1（multi-subject injection 已补，k≤5 时 ΔFPR 仅 0.007）、MF-2（标题软化为 "Temporal Measurement Drift"）、MF-3（Claim 4 已从 contribution 降级至 Discussion）、SF-1（LLM-specific challenges 节已加）
- **仍存在**：GSM1K N=33 证据薄弱（W1）、temporal cohort confound 未完全化解（W2）、Section 5.4 Audit Protocol 仍过于简略（W3）、model family-specific impact 的讨论不够诚实（W4）
- **升级条件**：如 Section 5.3 (N=33) 得到加强或删除 + Section 5.4 扩展 → 可升至 4.0 (Conference)

本轮审稿报告基于原始版本已提交，此修订版评价作为**补充信息**记录在 Group C。Research Director 在处理 action matrix 时可参考 R2 对修订版的反馈来判断哪些修改已到位、哪些仍需继续。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 22

## Round 22

2 recorded events


### User

_source line 183 · 2026-05-21T17:47:01.963187+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交。论文修订版有显著改善（multi-subject injection、LLM-specific challenges、贡献重组），但 GSM1K N=33 证据和 practical recommendations 仍是短板。维持 Overall 3.5 (Borderline Conference)，若这两点解决可升至 4.0。

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

_source line 184 · 2026-05-21T17:47:27.201224+00:00_

审稿报告已于上一步提交给 Research Director（Overall 3.5, Borderline Conference）。

Reviewer 2 这份额外报告是对**修订版论文**的审查（注意到标题已改为 "Temporal Measurement Drift..."、新增 multi-subject injection 等），属于修订后的增量评估。由于本轮 fresh review 的正式报告已投递，这份修订版反馈将作为补充记录。

**Reviewer 2 修订版评估要点**：
- 修订有效回应了 MF-1（multi-subject injection, k≤5 时 ΔFPR 仅 0.007）和 MF-2（标题软化）和 SF-1（LLM-specific challenges 节）
- 仍未解决：GSM1K N=33（Section 5.3）和 practical recommendations（Section 5.4）
- 维持 3.5，明确表示若这两点解决可升至 4.0

本轮圆桌审稿已完成。所有 deliverables：
- ✅ 审稿报告已投递 Research Director
- ✅ Issue Tracker 已更新（`review_issues.yaml`，Round 5）
- ✅ 视觉审查结果已纳入报告

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 23

## Round 23

10 recorded events


### User

_source line 185 · 2026-05-21T17:47:41.354381+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 R1 修订版审稿意见

---

### R1 核心关切逐条回应

**[AGREE with nuance] R1 关切 1: IRT misspecification 是根本威胁（98% |Lz|>2, CFI=0.72）**

R1 的观察在技术上正确：98% person-fit |Lz|>2 和 CFI=0.72 表明 unidimensional IRT model 对 5,227 LLM response patterns 拟合很差。但我对 "fundamental threat" 的判断比 R1 温和：

(a) **MH-DIF 不依赖 IRT model fit**。这是 R1 可能混淆的关键点——MH procedure 是 non-parametric 的，它按 observed total score 分层，不需要 IRT 参数估计。CFI=0.72 对 IRT-based DIF 方法（如 Lord's χ² 或 Raju's area）是致命的，但对 MH-DIF 的影响是间接的：misspecification 只通过 matching variable 的 adequacy 影响结果。论文用 cross-subject matching（total score on OTHER subjects）作为 matching variable，这比 same-benchmark total score 更 robust to multidimensionality。

(b) **但 R1 的建议有价值**：在单个 MMLU subject 上跑 DIF（更接近 unidimensional）是一个好的 robustness check。论文的 within-subject DIF（Section 4.4, Cohort 4）部分做了这个，结果 within-subject C% = 38.1%（甚至更高），这反而 reinforces 而非 undermines 主要发现。

(c) **Bifactor pilot CFI=0.89** 确实低于 0.95 target，但这对 MH-DIF 的 practical impact 需要 simulation 量化——不是所有 misspecification 都以相同幅度影响 DIF detection rates。

**结论**：IRT misspecification 是一个 legitimate concern，但不是 MH-DIF 的 "fundamental validity threat"。它更多影响 effect size 的精确度，而非 DIF detection 的方向性结论。同意论文应更显式地讨论这一点。

---

**[AGREE] R1 关切 2: Semi-synthetic ecological validity——binary flipping 粗糙**

这是 R1 审稿中最锐利的技术批评，我完全同意。

Binary flipping（将 incorrect → correct）模拟的是 "perfect contamination"——模型看到答案并 100% 记住。但现实中的 contamination 更微妙：partial memorization（记住部分信息但推理过程不同）、reasoning shortcuts（跳过中间步骤）、format-specific advantages（识别选项格式而非理解内容）。这些 contamination 模式不一定表现为 binary flip，可能只是 item difficulty 的微小变化。

更重要的是，R1 指出 **baseline FPR = 0.31**。这意味着在没有任何 injection 的情况下，31% 的 items 已经被标记为 DIF-C。semi-synthetic framework 在此基础上测量 ΔTPR 和 ΔFPR——即 **增量** detection performance。ΔTPR=0.37 at p=0.5 确实只是 "moderate"（相当于在已有的 31% baseline 上额外检出 37% 的注入 items）。

这削弱了 semi-synthetic framework 作为 **primary contribution** 的说服力。如果 framework 只能在 binary flipping（最极端的 contamination 形式）下达到 moderate detection power，那么对更 subtle 的 real-world contamination，其 sensitivity 可能更低。

**但我补充一个 partial defense**：semi-synthetic framework 的核心贡献不是 detection power 本身，而是 **cross-subject matching 消除 FPR inflation** 的方法论（ΔFPR < 0.001 vs within-subject matching 的 +0.19）。这个 matching strategy 的 validity 不依赖于 injection 的 ecological validity——即使 injection 是粗糙的，matching 的比较仍然成立。

---

**[AGREE] R1 关切 3: Causal interpretation ambiguity——"temporal" 但非 causal**

与我之前的 W2（temporal cohort confound）完全一致。R1 的表述更精确："~24.5% effective C% is still attributed to 'genuine temporal DIF' without full disentangling"。

论文标题已改为 "Temporal Measurement Drift"（比初稿 "Psychometric Instability" 好），但正文中仍有 causal-leaning 的措辞。例如 Conclusion 说 "MH-DIF reveals 17.9–31.3% temporal measurement drift driven by item properties"——"driven by" 暗示 causal direction，而数据只支持 association。

**两位 reviewer 的共识**：论文应更显式地将 DIF 定位为 **descriptive/diagnostic**，避免 causal language。"Temporal DIF" 应理解为 "DIF observed when grouping by temporal cohort"，不是 "DIF caused by temporal change"。

---

**[AGREE] R1 关切 4: GSM1K negative correlation (r=−0.35) 的 implications**

R1 准确指出了一个 underexplored tension：如果 DIF 检测的不是 contamination（与 web-overlap 独立，且 GSM1K correlation 为负），那它到底检测的是什么？

论文的回答是 "capability dimension shift"（Section 5.3），但这个回答只是 re-label 而非 explanation。negative correlation（models with larger contamination gaps benefit LESS from DIF items）实际上暗示 DIF-flagged items 对 contaminated models 反而更难——这与 "DIF 检测 contamination" 的叙事矛盾。

论文 honestly reports 这个 negative result（值得肯定），但如 R1 所说，没有 fully reckon with implications。如果 DIF 检测的是 "capability profile shift" 而非 contamination，那 Contribution 2（ground truth meta-critique）的 framing 需要调整——不是 "web-overlap labels fail to validate DIF"，而是 "DIF and contamination detection measure fundamentally different constructs"。

---

### R1 的三个问题

**Q: 方法论 care 是否足以超越 "known method → new domain"？**
我的判断：permutation null + ability matching + cross-subject matching 的 **组合** 确实有 novelty——没有先前工作将这些技术同时应用于 LLM benchmark 评估。但单独看每个组件，都是 known techniques。对于 EMNLP，这足以进入 Findings，是否够 Main 取决于审稿人对 empirical contributions 的 appetite。

**Q: IRT misspecification 是 methodological issue 还是 fundamental validity threat？**
Methodological issue，不是 fundamental validity threat。原因如上：MH-DIF 是 non-parametric 的，不依赖 IRT model fit。但论文应讨论 matching variable 在 multidimensional 能力空间中的 adequacy。

**Q: 更聚焦的论文是否更好？**
强烈同意。当前版本试图同时覆盖：semi-synthetic framework（Contribution 1）+ ground truth meta-critique（Contribution 2）+ temporal DIF characterization（Contribution 3）+ diagnostic lens（Section 5.3）+ cross-benchmark replication（Section 4.7）+ structural analysis（Section 4.4）。如果删掉 Section 5.3（N=33 evidence 太弱）和部分 structural analysis，将空间给 semi-synthetic framework 的 ecological validity 讨论和 practical recommendations，论文会更 focused 且更有说服力。

---

### 评分修订

基于 R1 的审稿意见，我对修订版论文的评分微调如下：

| 维度 | 我之前评分 | 修订后 | 理由 |
|------|---------|--------|------|
| Soundness | 4/5（Round 1）→ 3.5/5（上次修订） | **3.5/5** | R1 的 semi-synthetic ecological validity 批评（binary flipping + baseline FPR=0.31）加强了我对 Claim 1（semi-synthetic framework）robustness 的疑虑。但 MH-DIF 本身正确应用，cross-subject matching 有效。 |
| Excitement | 3.5/5 | **3.5/5** | 不变。R1 给 3.5 与我一致。 |
| Reproducibility | 4/5 | **4/5** | R1 也给 4.0，一致。 |
| Clarity | 4/5 | **4/5** | 不变。 |
| **Overall** | **3.5** | **3.5** | 维持 Borderline Conference。 |

### 两位 Reviewer 的共识总结

**达成一致的关键点**（构成对作者的核心 feedback）：
1. **Temporal cohort 的 causal ambiguity**：DIF 是 descriptive 而非 causal，论文应避免 causal language（R1 关切 3 + 我的 N3/W2）
2. **GSM1K N=33 证据不足**：无论作为独立 contribution 还是 discussion，N=33 的 evidence 太弱（R1 关切 4 + 我的 N1/W1）
3. **Semi-synthetic ecological validity 有限**：binary flipping 是极端简化，baseline FPR=0.31 暗示 framework 运行在已有 DIF 之上（R1 关切 2，我 agree）
4. **Practical recommendations 空洞**：Section 5.4 需要大幅扩展（我的 W3，R1 未直接提但其 "更聚焦" 建议隐含了此意）
5. **Cross-subject matching 是真正的方法论亮点**：ΔFPR < 0.001 vs +0.19 是 convincing 的（R1 strengths + 我的 S1）
6. **Overall 在 3.0-3.5 范围**：R1 给 3.0-3.5，我给 3.5，差距很小

**分歧点**：
- R1 对 IRT misspecification 的担忧比我更强（R1 认为是 fundamental threat，我认为是 methodological issue，因为 MH-DIF 是 non-parametric）
- R1 的 Soundness 3.5 vs 我的 3.5（现在一致）
- R1 似乎对 semi-synthetic framework 的 ecological validity 比我更 critical（R1 认为 ΔTPR=0.37 是 "moderate not strong"，我同意但认为 matching strategy 本身仍有 value）

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

_source line 186 · 2026-05-21T17:49:06.617402+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Round 5 报告已提交', 'status': 'completed', 'activeForm': 'Round 5 报告已提交'}, {'content': 'Round 6: 修订版论文审稿——收集 R1/R2 审稿 + 交叉回应', 'status': 'completed', 'activeForm': '收集修订版审稿和交叉回应'}, {'content': 'Round 6: 收敛判断 + 报告更新 + Issue Tracker 同步', 'status': 'in_progress', 'activeForm': '合成更新报告并同步 Issue Tracker'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Round 5 报告已提交', 'status': 'completed', 'activeForm': 'Round 5 报告已提交'}, {'content': 'Round 6: 修订版论文审稿——收集 R1/R2 审稿 + 交叉回应', 'status': 'completed', 'activeForm': '收集修订版审稿和交叉回应'}, {'content': 'Round 6: 收敛判断 + 报告更新 + Issue Tracker 同步', 'status': 'in_progress', 'activeForm': '合成更新报告并同步 Issue Tracker'}]"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-21T17:49:06.617955+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-21T17:50:38.722065+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Rounds 1-4 (2026-05-20/21), Round 5 fresh review, Round 6 revised paper review (2026-05-21)\n# Round 6 = post-revision review after Research Director applied Round 5 feedback\n\n# ============================================================\n# CRITICAL ISSUES (open)\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"Temporal DIF 因果归因不清——'temporal measurement drift' 仍含 causal-leaning 措辞\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强；calendar year cohort 混淆 temporal/architecture/training\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善）。但 Conclusion 仍说 'driven by item properties' 暗示 causal direction，数据只支持 association。R1+R2 共识：DIF 是 descriptive/diagnostic，应避免 causal language。~24.5% effective C% 仍被归因为 'genuine temporal DIF' without full disentangling。\"\n  action_items:\n    - round: 5\n      action: \"软化标题和 framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 6\n      action: \"清除 Conclusion 中的 causal language ('driven by' → 'associated with')；将 DIF 明确定位为 'DIF observed when grouping by temporal cohort' 而非 'DIF caused by temporal change'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic framework ecological validity——binary flipping 过于粗糙，baseline FPR=0.31 限制增量检测力\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Proposition 1 ΔFPR=0 by construction；需 multi-subject injection\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"修订版新增 multi-subject injection (k∈{1,3,5,10,20})——k≤5 时 ΔFPR=0.007，k=10 时 0.026-0.069。显著改善。但 R1 提出新批评：binary flipping 模拟 'perfect contamination'，现实中 contamination 更微妙（partial memorization, reasoning shortcuts）。ΔTPR=0.37 at p=0.5 只是 moderate。R2 AGREE 但补充 defense：核心贡献是 cross-subject matching 消除 FPR inflation (ΔFPR<0.001 vs +0.19)，matching strategy validity 不依赖 injection 的 ecological validity。\"\n  action_items:\n    - round: 5\n      action: \"补充 multi-subject injection\"\n      assigned_to: authors\n      status: done\n    - round: 6\n      action: \"讨论 binary flipping 的局限性（partial memorization, reasoning shortcuts 等 realistic contamination patterns）；在 Limitations 中承认 ΔTPR=0.37 是 moderate detection power\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES (open)\n# ============================================================\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K N=33 证据太弱——Section 5.3 'DIF as diagnostic lens' 应删除或大幅加强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识：降级为 exploratory observation，从 contribution list 移除\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"修订版已将 Claim 4 从 contribution 降为 Discussion section——正确的降级。但 Section 5.3 仍以 N=33 的 r=-0.478 论证 'DIF captures behavioral change distinct from memorization'。R1 进一步指出 negative correlation 实际暗示 DIF-flagged items 对 contaminated models 更难——与 'DIF 检测 contamination' 叙事矛盾。R2 AGREE。共识：建议删除 Section 5.3 或在 Limitations 明确标注 N=33 局限。\"\n  action_items:\n    - round: 5\n      action: \"降级 Claim 4\"\n      assigned_to: paper_agent\n      status: done\n    - round: 6\n      action: \"删除 Section 5.3 或大幅压缩为 1-2 句 exploratory note；将释放的空间给 Section 5.4 practical recommendations\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"DIF Audit Protocol (Section 5.4) 只有 3 句话，practical recommendations 空洞\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需扩展 actionable recommendations\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"修订版未改善。仍然只有 'trigger at ≥500 models, use cross-subject matching, flag unstable items'。缺少：谁来做？多久一次？如何集成到 benchmark pipelines？threshold 选择依据？与 Growing Pains FPC 的集成？R2 在 Q3 建议将 temporal DIF rate 作为 BHI 的 temporal health 维度。\"\n  action_items:\n    - round: 6\n      action: \"大幅扩展 Section 5.4：具体 workflow、threshold justification、与 BHI/Growing Pains 的集成建议\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"方法论新颖性——transplant 的 LLM-specific challenges 已添加但 novelty 仍 borderline\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需补充 LLM-specific challenges 讨论\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"修订版新增 'LLM-specific challenges' 节（Page 5）——3 个论点（deterministic responses, bimodal ability, multi-dimensional subjects）。R2 S2: 显著加强了 positioning。但 R2 仍认为对严格 novelty 标准 borderline。R1+R2 共识：permutation null + ability matching + cross-subject matching 的组合有 novelty，但单独看每个组件都是 known techniques。对 EMNLP empirical track 可能够，对 methodological innovation 不够。\"\n  action_items:\n    - round: 5\n      action: \"Section 3 增加 LLM-specific challenges\"\n      assigned_to: paper_agent\n      status: done\n    - round: 6\n      action: \"无进一步 action needed——当前 positioning 已合理\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"修订版有效回应：LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。Novelty borderline but acceptable for empirical contribution track.\"\n  resolution_round: 6\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI 的 resampling unit 未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 critical → R2 REBUT → Should-Fix\"\n    - round: 6\n      reviewers: []\n      note: \"Round 6 未独立提出，修订版未修改此项\"\n  action_items:\n    - round: 5\n      action: \"报告 bootstrap resampling unit 和策略\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"DIF 术语对 EMNLP 读者不够友好——缺 running example\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需 running example\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2 Clarity 4/5: 'DIF 术语密度仍然较高，缺少 running example'\"\n  action_items:\n    - round: 5\n      action: \"Section 3.2 加 running example\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 的实证对比（DIF flags vs FPC anchors overlap）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"缺 Jaccard/enrichment overlap 分析\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2 W3 中再次提到缺少与 Growing Pains FPC 的集成讨论\"\n  action_items:\n    - round: 5\n      action: \"补充 overlap 分析或详细讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing 需调整——DIF 和 contamination detection 测量不同 constructs\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DIF ⊥ web-overlap 的双向解读\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 关切 4: GSM1K negative correlation 暗示 DIF 不检测 contamination。R2 AGREE：更准确的 framing 应是 'DIF and contamination detection measure fundamentally different constructs' 而非 'web-overlap labels fail to validate DIF'。\"\n  action_items:\n    - round: 6\n      action: \"调整 Claim 2 framing：从 'web-overlap is wrong ground truth' 改为 'DIF and contamination measure different constructs'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"IRT misspecification (98% |Lz|>2, CFI=0.72) 对 MH-DIF 的间接影响需讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 认为是 fundamental threat，R2 AGREE with nuance：MH-DIF 是 non-parametric 不依赖 IRT fit，但 misspecification 通过 matching variable adequacy 间接影响。Within-subject C%=38.1% reinforces 而非 undermines 主要发现。Bifactor pilot CFI=0.89 低于 0.95 target 但 practical impact 需 simulation。共识：是 methodological issue 而非 fundamental validity threat，但论文应更显式讨论。\"\n  action_items:\n    - round: 6\n      action: \"在 Method 或 Discussion 中讨论 IRT misspecification 对 MH-DIF matching variable adequacy 的影响；引用 within-subject C%=38.1% 作为 robustness evidence\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"论文过于分散——建议删除 Section 5.3、精简 structural analysis，将空间给 practical recommendations\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议更聚焦的论文。R2 强烈同意：删掉 Section 5.3 (N=33 evidence 太弱) 和部分 structural analysis，将空间给 semi-synthetic ecological validity 讨论和 practical recommendations。\"\n  action_items:\n    - round: 6\n      action: \"删除/压缩 Section 5.3；释放空间扩展 Section 5.4 和 semi-synthetic limitations 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED / MINOR ISSUES\n# ============================================================\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失引用\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"4 篇 missing + 8 orphan bib entries\"\n    - round: 6\n      reviewers: [2]\n      note: \"BHI (Zhu & Huang 2026) 和 Benchmark² (Qian & Huang 2026) 已添加。ATLAS 已在 bib 但 R2 Related Work Completeness 4/5 说明仍有 1-2 minor gaps。Orphan entries 状态不明。\"\n  action_items:\n    - round: 6\n      action: \"确认 orphan bib entries 是否已清理；检查 ATLAS 是否已引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"plan_027 确认 temporal cohort ability gap 小 (d=-0.17)，matched C%=28.9%±0.1%。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (CFI=0.72)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50)。MH 是 nonparametric。但 Round 6 以新角度重新提出（见 R6-W1）。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 需 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]。Cross-subject stratification 是 structural guarantee。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"R1-W2\"\n  summary: \"推理-RL N=13\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"降级为补充分析。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"R2-W2\"\n  summary: \"Growing Pains 区分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"修订版 §2 已对比。但 overlap 分析仍缺（见 R5-W5）。\"\n  resolution_round: 2\n  mentions: []"
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
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Rounds 1-4 (2026-05-20/21), Round 5 fresh review, Round 6 revised paper review (2026-05-21)\n# Round 6 = post-revision review after Research Director applied Round 5 feedback\n\n# ============================================================\n# CRITICAL ISSUES (open)\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"Temporal DIF 因果归因不清——'temporal measurement drift' 仍含 causal-leaning 措辞\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强；calendar year cohort 混淆 temporal/architecture/training\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善）。但 Conclusion 仍说 'driven by item properties' 暗示 causal direction，数据只支持 association。R1+R2 共识：DIF 是 descriptive/diagnostic，应避免 causal language。~24.5% effective C% 仍被归因为 'genuine temporal DIF' without full disentangling。\"\n  action_items:\n    - round: 5\n      action: \"软化标题和 framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 6\n      action: \"清除 Conclusion 中的 causal language ('driven by' → 'associated with')；将 DIF 明确定位为 'DIF observed when grouping by temporal cohort' 而非 'DIF caused by temporal change'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic framework ecological validity——binary flipping 过于粗糙，baseline FPR=0.31 限制增量检测力\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Proposition 1 ΔFPR=0 by construction；需 multi-subject injection\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"修订版新增 multi-subject injection (k∈{1,3,5,10,20})——k≤5 时 ΔFPR=0.007，k=10 时 0.026-0.069。显著改善。但 R1 提出新批评：binary flipping 模拟 'perfect contamination'，现实中 contamination 更微妙（partial memorization, reasoning shortcuts）。ΔTPR=0.37 at p=0.5 只是 moderate。R2 AGREE 但补充 defense：核心贡献是 cross-subject matching 消除 FPR inflation (ΔFPR<0.001 vs +0.19)，matching strategy validity 不依赖 injection 的 ecological validity。\"\n  action_items:\n    - round: 5\n      action: \"补充 multi-subject injection\"\n      assigned_to: authors\n      status: done\n    - round: 6\n      action: \"讨论 binary flipping 的局限性（partial memorization, reasoning shortcuts 等 realistic contamination patterns）；在 Limitations 中承认 ΔTPR=0.37 是 moderate detection power\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES (open)\n# ============================================================\n\n- id: \"RD2-W2\"\n  summary: \"GSM1K N=33 证据太弱——Section 5.3 'DIF as diagnostic lens' 应删除或大幅加强\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"共识：降级为 exploratory observation，从 contribution list 移除\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"修订版已将 Claim 4 从 contribution 降为 Discussion section——正确的降级。但 Section 5.3 仍以 N=33 的 r=-0.478 论证 'DIF captures behavioral change distinct from memorization'。R1 进一步指出 negative correlation 实际暗示 DIF-flagged items 对 contaminated models 更难——与 'DIF 检测 contamination' 叙事矛盾。R2 AGREE。共识：建议删除 Section 5.3 或在 Limitations 明确标注 N=33 局限。\"\n  action_items:\n    - round: 5\n      action: \"降级 Claim 4\"\n      assigned_to: paper_agent\n      status: done\n    - round: 6\n      action: \"删除 Section 5.3 或大幅压缩为 1-2 句 exploratory note；将释放的空间给 Section 5.4 practical recommendations\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"DIF Audit Protocol (Section 5.4) 只有 3 句话，practical recommendations 空洞\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需扩展 actionable recommendations\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"修订版未改善。仍然只有 'trigger at ≥500 models, use cross-subject matching, flag unstable items'。缺少：谁来做？多久一次？如何集成到 benchmark pipelines？threshold 选择依据？与 Growing Pains FPC 的集成？R2 在 Q3 建议将 temporal DIF rate 作为 BHI 的 temporal health 维度。\"\n  action_items:\n    - round: 6\n      action: \"大幅扩展 Section 5.4：具体 workflow、threshold justification、与 BHI/Growing Pains 的集成建议\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"方法论新颖性——transplant 的 LLM-specific challenges 已添加但 novelty 仍 borderline\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需补充 LLM-specific challenges 讨论\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"修订版新增 'LLM-specific challenges' 节（Page 5）——3 个论点（deterministic responses, bimodal ability, multi-dimensional subjects）。R2 S2: 显著加强了 positioning。但 R2 仍认为对严格 novelty 标准 borderline。R1+R2 共识：permutation null + ability matching + cross-subject matching 的组合有 novelty，但单独看每个组件都是 known techniques。对 EMNLP empirical track 可能够，对 methodological innovation 不够。\"\n  action_items:\n    - round: 5\n      action: \"Section 3 增加 LLM-specific challenges\"\n      assigned_to: paper_agent\n      status: done\n    - round: 6\n      action: \"无进一步 action needed——当前 positioning 已合理\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"修订版有效回应：LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。Novelty borderline but acceptable for empirical contribution track.\"\n  resolution_round: 6\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI 的 resampling unit 未报告\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"R1 critical → R2 REBUT → Should-Fix\"\n    - round: 6\n      reviewers: []\n      note: \"Round 6 未独立提出，修订版未修改此项\"\n  action_items:\n    - round: 5\n      action: \"报告 bootstrap resampling unit 和策略\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"DIF 术语对 EMNLP 读者不够友好——缺 running example\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"需 running example\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2 Clarity 4/5: 'DIF 术语密度仍然较高，缺少 running example'\"\n  action_items:\n    - round: 5\n      action: \"Section 3.2 加 running example\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 的实证对比（DIF flags vs FPC anchors overlap）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"缺 Jaccard/enrichment overlap 分析\"\n    - round: 6\n      reviewers: [2]\n      note: \"R2 W3 中再次提到缺少与 Growing Pains FPC 的集成讨论\"\n  action_items:\n    - round: 5\n      action: \"补充 overlap 分析或详细讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing 需调整——DIF 和 contamination detection 测量不同 constructs\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"DIF ⊥ web-overlap 的双向解读\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 关切 4: GSM1K negative correlation 暗示 DIF 不检测 contamination。R2 AGREE：更准确的 framing 应是 'DIF and contamination detection measure fundamentally different constructs' 而非 'web-overlap labels fail to validate DIF'。\"\n  action_items:\n    - round: 6\n      action: \"调整 Claim 2 framing：从 'web-overlap is wrong ground truth' 改为 'DIF and contamination measure different constructs'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"IRT misspecification (98% |Lz|>2, CFI=0.72) 对 MH-DIF 的间接影响需讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 认为是 fundamental threat，R2 AGREE with nuance：MH-DIF 是 non-parametric 不依赖 IRT fit，但 misspecification 通过 matching variable adequacy 间接影响。Within-subject C%=38.1% reinforces 而非 undermines 主要发现。Bifactor pilot CFI=0.89 低于 0.95 target 但 practical impact 需 simulation。共识：是 methodological issue 而非 fundamental validity threat，但论文应更显式讨论。\"\n  action_items:\n    - round: 6\n      action: \"在 Method 或 Discussion 中讨论 IRT misspecification 对 MH-DIF matching variable adequacy 的影响；引用 within-subject C%=38.1% 作为 robustness evidence\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"论文过于分散——建议删除 Section 5.3、精简 structural analysis，将空间给 practical recommendations\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议更聚焦的论文。R2 强烈同意：删掉 Section 5.3 (N=33 evidence 太弱) 和部分 structural analysis，将空间给 semi-synthetic ecological validity 讨论和 practical recommendations。\"\n  action_items:\n    - round: 6\n      action: \"删除/压缩 Section 5.3；释放空间扩展 Section 5.4 和 semi-synthetic limitations 讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED / MINOR ISSUES\n# ============================================================\n\n- id: \"MISSING-REF-1\"\n  summary: \"缺失引用\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"4 篇 missing + 8 orphan bib entries\"\n    - round: 6\n      reviewers: [2]\n      note: \"BHI (Zhu & Huang 2026) 和 Benchmark² (Qian & Huang 2026) 已添加。ATLAS 已在 bib 但 R2 Related Work Completeness 4/5 说明仍有 1-2 minor gaps。Orphan entries 状态不明。\"\n  action_items:\n    - round: 6\n      action: \"确认 orphan bib entries 是否已清理；检查 ATLAS 是否已引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"plan_027 确认 temporal cohort ability gap 小 (d=-0.17)，matched C%=28.9%±0.1%。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (CFI=0.72)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50)。MH 是 nonparametric。但 Round 6 以新角度重新提出（见 R6-W1）。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 需 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]。Cross-subject stratification 是 structural guarantee。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"R1-W2\"\n  summary: \"推理-RL N=13\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"降级为补充分析。\"\n  resolution_round: 2\n  mentions: []\n\n- id: \"R2-W2\"\n  summary: \"Growing Pains 区分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"修订版 §2 已对比。但 overlap 分析仍缺（见 R5-W5）。\"\n  resolution_round: 2\n  mentions: []"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-21T17:50:38.823156+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 12103}, \"error\": \"\"}"}

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

_source line 190 · 2026-05-21T17:52:10.125050+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "force_resubmit": "True",
  "report": "# 审稿报告 — Round 6 (修订版论文评估)\n\n**论文**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n**截止日期**: 2026-05-25 AoE\n**审稿模式**: 修订版评估（Round 5 报告后论文修订，Round 6 重新评估）\n**日期**: 2026-05-21\n\n---\n\n## Summary\n\n修订版论文做了 4 项显著改进：(1) 标题从 \"Psychometric Instability\" 改为 \"Temporal Measurement Drift\"（更中性）；(2) 新增 multi-subject injection 实验（k∈{1,3,5,10,20}，k≤5 时 ΔFPR=0.007）；(3) 新增 \"LLM-specific challenges\" 节论证 transplant 非平凡性；(4) Contributions 从 4 个收紧为 3 个（Claim 4 降级为 Discussion）。Semi-synthetic framework 升为 primary contribution。Related Work 扩充至 55+ references，覆盖 BHI 和 Benchmark²。\n\n两位 Reviewer 一致认可修订版的改善方向，但指出仍存在核心问题：causal language 残余、binary flipping 的 ecological validity 局限、Section 5.3 GSM1K 证据过弱、practical recommendations 仍空洞。\n\n---\n\n## 修订版改善（与 Round 5 对比）\n\n| Round 5 问题 | 修订版应对 | 评估 |\n|---|---|---|\n| MF-1: Multi-subject injection 缺失 | ✅ 新增 k∈{1,3,5,10,20} 实验 | 实质改善，k≤5 ΔFPR=0.007 |\n| MF-2: \"Psychometric Instability\" 标题过强 | ✅ 改为 \"Temporal Measurement Drift\" | 方向正确，但 Conclusion 仍有 causal language |\n| MF-3: Claim 4 证据不足 | ✅ 从 contribution 降为 Discussion | 正确降级，但 Section 5.3 仍以 N=33 过弱证据展开 |\n| SF-1: Novelty 论证不充分 | ✅ 新增 LLM-specific challenges 节 | 显著改善 |\n| SF-3: Audit Protocol 过简 | ❌ 未改善 | 仍只有 3 句话 |\n| SF-7: DIF 术语不友好 | ❌ 未改善 | 仍缺 running example |\n| SF-9: 引用问题 | ✅ 部分改善 | BHI/Benchmark² 已添加，orphan entries 状态不明 |\n\n---\n\n## Strengths\n\n1. **Semi-synthetic framework 有实质扩展**：multi-subject injection (k∈{1,3,5,10,20}) 直接回应 Round 5 核心批评。ΔFPR 在 k≤5（≤9% domains）时仅 0.007，k=10 时升至 0.026-0.069，给出了清晰的 validity boundary。Cross-subject matching 的 ΔFPR < 0.001 vs. within-subject +0.19 对比令人信服。\n\n2. **LLM-specific challenges 节有效**：三个论点（deterministic responses 违反 local independence → motivate quintile-based stratification；bimodal ability distribution；MMLU 57 subjects 跨多 latent dimensions vs. MH unidimensionality 假设）显著加强了方法论 positioning。\n\n3. **叙事重心调整成功**：3 contributions 代替 4 个，semi-synthetic framework 升为 primary，\"Temporal Measurement Drift\" 比 \"Psychometric Instability\" 更准确。\"Our contributions are methodological and empirical, not algorithmic\" 的自我定位明智。\n\n4. **Related Work 大幅完善**：4 个结构化子节覆盖 contamination detection、IRT in LLM、DIF methodology、benchmark quality，55+ references。BHI 和 Benchmark² 已添加。\n\n5. **规模和严谨性不减**：5,227 models × 6 benchmarks、5 种 cohort design、3 层结构控制全部保留并有所加强。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical, consensus] **Causal language 残余——Conclusion 中 \"driven by\" 暗示因果方向**\n- 修订版标题改善显著，但正文仍有 causal-leaning 措辞。Conclusion 说 \"MH-DIF reveals 17.9–31.3% temporal measurement drift driven by item properties\"——\"driven by\" 暗示 causal direction，而数据只支持 association。~24.5% effective C% 仍被归因为 \"genuine temporal DIF\" without full disentangling。Calendar year cohort 同时混淆 architecture shift、training data shift、post-training methodology、genuine capability evolution。\n- **R1 提出，R2 AGREE**。共识：DIF 是 descriptive/diagnostic 工具，\"temporal DIF\" 应理解为 \"DIF observed when grouping by temporal cohort\" 而非 \"DIF caused by temporal change\"。\n- 建议：替换所有 causal language（\"driven by\" → \"associated with\"）；在 Discussion 中明确 DIF 的 descriptive 定位。\n\n**MF-2** [critical, consensus] **Semi-synthetic binary flipping 的 ecological validity 局限**\n- Binary flipping（incorrect → correct）模拟 \"perfect contamination\"，但现实中 contamination 更微妙：partial memorization、reasoning shortcuts、format-specific advantages。ΔTPR = 0.37 at p = 0.5 只是 moderate detection power。Baseline FPR = 0.31 意味着 framework 运行在已有 31% DIF 之上。Multi-subject injection 是重要改善，但未解决 injection 本身的 realism 问题。\n- **R1 提出，R2 AGREE**。R2 补充 partial defense：核心贡献是 cross-subject matching 消除 FPR inflation（ΔFPR < 0.001 vs. +0.19），matching strategy validity 不依赖 injection 的 ecological validity。\n- 建议：在 Limitations 中讨论 binary flipping 的局限性和 more realistic contamination patterns；承认 ΔTPR = 0.37 是 moderate。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning, consensus] **Section 5.3 GSM1K N=33 证据仍然过弱**\n- 修订版正确地将 Claim 4 降为 Discussion，但 Section 5.3 仍以两段文字展开。N=33 的 r = -0.478（partial r = -0.385）只解释 ~15% 方差，power 不足以排除 moderate-to-large alternative effect sizes。Negative correlation 暗示 DIF-flagged items 对 contaminated models 更难——与 \"DIF 检测 contamination\" 叙事矛盾。\n- R1+R2 共识：建议删除 Section 5.3 或压缩为 1-2 句 exploratory note，释放空间给 practical recommendations。\n\n**SF-2** [warning, consensus] **Practical recommendations (Section 5.4) 仍只有 3 句话**\n- 论文声称 \"LLM benchmarks need psychometric monitoring alongside score reporting\"，但具体 workflow 几乎为零。缺少：谁来做？多久一次？工具如何集成？threshold 选择依据？与 Growing Pains FPC / BHI 的集成？\n- 修订版未改善此项。R2 建议将 temporal DIF rate 作为 BHI 的 \"temporal health\" 维度。\n\n**SF-3** [warning, consensus] **Claim 2 framing 需微调**\n- GSM1K negative correlation 暗示 DIF 不检测 contamination。更准确的 framing：\"DIF and contamination detection measure fundamentally different constructs\"，而非 \"web-overlap labels fail to validate DIF\"。\n- R1 提出，R2 AGREE with nuance（semi-synthetic 证明 DIF can detect contamination，但 real-world DIF ≠ contamination）。\n\n**SF-4** [warning, divergence] **IRT misspecification (98% |Lz|>2, CFI=0.72) 的影响需讨论**\n- R1 认为是 fundamental validity threat；R2 认为是 methodological issue（MH-DIF 是 non-parametric，不依赖 IRT fit，misspecification 仅通过 matching variable adequacy 间接影响）。Within-subject C% = 38.1% 和 cross-subject matching 提供部分 robustness。Bifactor CFI = 0.89 低于 0.95 target 但 practical impact 需 simulation。\n- 共识：论文应更显式讨论此点，但非 fundamental threat。\n\n**SF-5** [warning] **DIF 术语仍缺 running example**——修订版未改善。\n\n**SF-6** [warning] **Bootstrap resampling unit 仍未报告**——修订版未改善。\n\n**SF-7** [warning] **Growing Pains overlap 分析仍缺**——修订版未改善。\n\n---\n\n## Reviewer Consensus（修订版）\n\n1. **修订方向正确**：multi-subject injection、LLM-specific challenges、contribution 重组、标题软化均为有效改善\n2. **Causal language 需进一步清除**：Conclusion 中的 \"driven by\" 等措辞仍暗示因果\n3. **Section 5.3 应删除/压缩**：GSM1K N=33 + negative correlation 共同削弱此节的价值\n4. **Section 5.4 需大幅扩展**：这是论文最大的 missed opportunity\n5. **Cross-subject matching 是真正的方法论亮点**：ΔFPR < 0.001 vs. +0.19，加上 multi-subject injection 的 validity boundary，这部分论证充分\n6. **Overall 3.0-3.5 范围**：R1 约 3.0-3.5，R2 给 3.5\n\n## Reviewer Divergence（修订版）\n\n1. **IRT misspecification 严重程度**：R1 更 concerned（fundamental threat），R2 less concerned（methodological issue）。分歧保留但双方同意论文应讨论。\n2. **Semi-synthetic 作为 primary contribution 的充分性**：R1 对 ΔTPR = 0.37 更 skeptical，R2 认为 matching strategy 本身有独立价值。\n\n---\n\n## Questions to Authors\n\n1. Conclusion 中的 \"driven by item properties\" 可否改为 \"associated with item properties\" 以避免 causal implication？\n2. 是否有 more realistic contamination patterns（如 partial memorization）的 injection 方案？即使作为 future work 讨论也有价值。\n3. 如果删除 Section 5.3（~0.5 page），释放的空间能否足够扩展 Section 5.4 的 practical recommendations？\n4. DIF-flagged items 与 Growing Pains FPC anchor items 的 Jaccard overlap 是多少？这个分析数据应已具备。\n5. 论文能否将 temporal DIF rate 提议为 BHI 的第四个维度（temporal health），增强 practical significance？\n\n---\n\n## Missing References（修订版新发现）\n\n修订版已添加 BHI 和 Benchmark²。剩余 minor gaps：\n- ATLAS (Li et al. 2025)——已在 bib 但可能仍未引用\n- Orphan bib entries 是否已清理——状态不明\n\n---\n\n## External Review\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：已完成（Round 5 时获取）。2 warnings（pages 3-5 无 display items 间隔、主正文仅 4 个 display items）、7 info。修订版可能已改变布局，如需要可重新派发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.5 | 3.5 |\n| Reproducibility | 4 | 4 | 4 |\n| Clarity | 4 | 4 | 4 |\n\n**置信度**: 4/5\n\n**与 Round 5 的变化**：\n- Overall 不变（3.5），但修订版改善了多个 Round 5 问题\n- 新增问题：binary flipping ecological validity（MF-2 的新维度）、IRT misspecification（SF-4）、论文聚焦度（SF-1 中建议删除 Section 5.3）\n- 被有效解决的问题：multi-subject injection、LLM-specific challenges、contribution 重组、标题软化\n\n**判断依据**：\n修订版有显著进步——multi-subject injection 和 LLM-specific challenges 节有效回应了 Round 5 的核心批评。但两个问题阻止论文上升到 4.0（Conference）：\n1. **Causal language 残余 + binary flipping ecological validity** — 论文的核心 claim 仍然比数据支持的更强\n2. **Practical recommendations 空洞** — 与论文的 policy message（\"need psychometric monitoring\"）不匹配\n\n**升级到 4.0 的路径**（两位 Reviewer 共识）：\n1. 清除 Conclusion 中的 causal language（cost: 低）\n2. 删除 Section 5.3，释放空间给 Section 5.4（cost: 中）\n3. 在 Limitations 中讨论 binary flipping 局限性 + IRT misspecification（cost: 低）\n\n如果这 3 项在提交前完成，论文可达 Conference 水平。\n\n**EMNLP 2026 评分映射**：3.5 = Borderline Conference\n\n---\n\n## 附录：Issue Tracker 同步\n\n已更新 `review_issues.yaml`：\n- 2 个 critical issues open（MF-1 causal language, MF-2/R5-N1 ecological validity）\n- 8 个 warning issues open\n- 1 个 issue resolved in Round 6（R2-N2 novelty — LLM-specific challenges 有效回应）\n- 6 个 issues resolved in prior rounds"
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
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "force_resubmit": "True",
    "report": "# 审稿报告 — Round 6 (修订版论文评估)\n\n**论文**: Temporal Measurement Drift in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)\n**截止日期**: 2026-05-25 AoE\n**审稿模式**: 修订版评估（Round 5 报告后论文修订，Round 6 重新评估）\n**日期**: 2026-05-21\n\n---\n\n## Summary\n\n修订版论文做了 4 项显著改进：(1) 标题从 \"Psychometric Instability\" 改为 \"Temporal Measurement Drift\"（更中性）；(2) 新增 multi-subject injection 实验（k∈{1,3,5,10,20}，k≤5 时 ΔFPR=0.007）；(3) 新增 \"LLM-specific challenges\" 节论证 transplant 非平凡性；(4) Contributions 从 4 个收紧为 3 个（Claim 4 降级为 Discussion）。Semi-synthetic framework 升为 primary contribution。Related Work 扩充至 55+ references，覆盖 BHI 和 Benchmark²。\n\n两位 Reviewer 一致认可修订版的改善方向，但指出仍存在核心问题：causal language 残余、binary flipping 的 ecological validity 局限、Section 5.3 GSM1K 证据过弱、practical recommendations 仍空洞。\n\n---\n\n## 修订版改善（与 Round 5 对比）\n\n| Round 5 问题 | 修订版应对 | 评估 |\n|---|---|---|\n| MF-1: Multi-subject injection 缺失 | ✅ 新增 k∈{1,3,5,10,20} 实验 | 实质改善，k≤5 ΔFPR=0.007 |\n| MF-2: \"Psychometric Instability\" 标题过强 | ✅ 改为 \"Temporal Measurement Drift\" | 方向正确，但 Conclusion 仍有 causal language |\n| MF-3: Claim 4 证据不足 | ✅ 从 contribution 降为 Discussion | 正确降级，但 Section 5.3 仍以 N=33 过弱证据展开 |\n| SF-1: Novelty 论证不充分 | ✅ 新增 LLM-specific challenges 节 | 显著改善 |\n| SF-3: Audit Protocol 过简 | ❌ 未改善 | 仍只有 3 句话 |\n| SF-7: DIF 术语不友好 | ❌ 未改善 | 仍缺 running example |\n| SF-9: 引用问题 | ✅ 部分改善 | BHI/Benchmark² 已添加，orphan entries 状态不明 |\n\n---\n\n## Strengths\n\n1. **Semi-synthetic framework 有实质扩展**：multi-subject injection (k∈{1,3,5,10,20}) 直接回应 Round 5 核心批评。ΔFPR 在 k≤5（≤9% domains）时仅 0.007，k=10 时升至 0.026-0.069，给出了清晰的 validity boundary。Cross-subject matching 的 ΔFPR < 0.001 vs. within-subject +0.19 对比令人信服。\n\n2. **LLM-specific challenges 节有效**：三个论点（deterministic responses 违反 local independence → motivate quintile-based stratification；bimodal ability distribution；MMLU 57 subjects 跨多 latent dimensions vs. MH unidimensionality 假设）显著加强了方法论 positioning。\n\n3. **叙事重心调整成功**：3 contributions 代替 4 个，semi-synthetic framework 升为 primary，\"Temporal Measurement Drift\" 比 \"Psychometric Instability\" 更准确。\"Our contributions are methodological and empirical, not algorithmic\" 的自我定位明智。\n\n4. **Related Work 大幅完善**：4 个结构化子节覆盖 contamination detection、IRT in LLM、DIF methodology、benchmark quality，55+ references。BHI 和 Benchmark² 已添加。\n\n5. **规模和严谨性不减**：5,227 models × 6 benchmarks、5 种 cohort design、3 层结构控制全部保留并有所加强。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical, consensus] **Causal language 残余——Conclusion 中 \"driven by\" 暗示因果方向**\n- 修订版标题改善显著，但正文仍有 causal-leaning 措辞。Conclusion 说 \"MH-DIF reveals 17.9–31.3% temporal measurement drift driven by item properties\"——\"driven by\" 暗示 causal direction，而数据只支持 association。~24.5% effective C% 仍被归因为 \"genuine temporal DIF\" without full disentangling。Calendar year cohort 同时混淆 architecture shift、training data shift、post-training methodology、genuine capability evolution。\n- **R1 提出，R2 AGREE**。共识：DIF 是 descriptive/diagnostic 工具，\"temporal DIF\" 应理解为 \"DIF observed when grouping by temporal cohort\" 而非 \"DIF caused by temporal change\"。\n- 建议：替换所有 causal language（\"driven by\" → \"associated with\"）；在 Discussion 中明确 DIF 的 descriptive 定位。\n\n**MF-2** [critical, consensus] **Semi-synthetic binary flipping 的 ecological validity 局限**\n- Binary flipping（incorrect → correct）模拟 \"perfect contamination\"，但现实中 contamination 更微妙：partial memorization、reasoning shortcuts、format-specific advantages。ΔTPR = 0.37 at p = 0.5 只是 moderate detection power。Baseline FPR = 0.31 意味着 framework 运行在已有 31% DIF 之上。Multi-subject injection 是重要改善，但未解决 injection 本身的 realism 问题。\n- **R1 提出，R2 AGREE**。R2 补充 partial defense：核心贡献是 cross-subject matching 消除 FPR inflation（ΔFPR < 0.001 vs. +0.19），matching strategy validity 不依赖 injection 的 ecological validity。\n- 建议：在 Limitations 中讨论 binary flipping 的局限性和 more realistic contamination patterns；承认 ΔTPR = 0.37 是 moderate。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning, consensus] **Section 5.3 GSM1K N=33 证据仍然过弱**\n- 修订版正确地将 Claim 4 降为 Discussion，但 Section 5.3 仍以两段文字展开。N=33 的 r = -0.478（partial r = -0.385）只解释 ~15% 方差，power 不足以排除 moderate-to-large alternative effect sizes。Negative correlation 暗示 DIF-flagged items 对 contaminated models 更难——与 \"DIF 检测 contamination\" 叙事矛盾。\n- R1+R2 共识：建议删除 Section 5.3 或压缩为 1-2 句 exploratory note，释放空间给 practical recommendations。\n\n**SF-2** [warning, consensus] **Practical recommendations (Section 5.4) 仍只有 3 句话**\n- 论文声称 \"LLM benchmarks need psychometric monitoring alongside score reporting\"，但具体 workflow 几乎为零。缺少：谁来做？多久一次？工具如何集成？threshold 选择依据？与 Growing Pains FPC / BHI 的集成？\n- 修订版未改善此项。R2 建议将 temporal DIF rate 作为 BHI 的 \"temporal health\" 维度。\n\n**SF-3** [warning, consensus] **Claim 2 framing 需微调**\n- GSM1K negative correlation 暗示 DIF 不检测 contamination。更准确的 framing：\"DIF and contamination detection measure fundamentally different constructs\"，而非 \"web-overlap labels fail to validate DIF\"。\n- R1 提出，R2 AGREE with nuance（semi-synthetic 证明 DIF can detect contamination，但 real-world DIF ≠ contamination）。\n\n**SF-4** [warning, divergence] **IRT misspecification (98% |Lz|>2, CFI=0.72) 的影响需讨论**\n- R1 认为是 fundamental validity threat；R2 认为是 methodological issue（MH-DIF 是 non-parametric，不依赖 IRT fit，misspecification 仅通过 matching variable adequacy 间接影响）。Within-subject C% = 38.1% 和 cross-subject matching 提供部分 robustness。Bifactor CFI = 0.89 低于 0.95 target 但 practical impact 需 simulation。\n- 共识：论文应更显式讨论此点，但非 fundamental threat。\n\n**SF-5** [warning] **DIF 术语仍缺 running example**——修订版未改善。\n\n**SF-6** [warning] **Bootstrap resampling unit 仍未报告**——修订版未改善。\n\n**SF-7** [warning] **Growing Pains overlap 分析仍缺**——修订版未改善。\n\n---\n\n## Reviewer Consensus（修订版）\n\n1. **修订方向正确**：multi-subject injection、LLM-specific challenges、contribution 重组、标题软化均为有效改善\n2. **Causal language 需进一步清除**：Conclusion 中的 \"driven by\" 等措辞仍暗示因果\n3. **Section 5.3 应删除/压缩**：GSM1K N=33 + negative correlation 共同削弱此节的价值\n4. **Section 5.4 需大幅扩展**：这是论文最大的 missed opportunity\n5. **Cross-subject matching 是真正的方法论亮点**：ΔFPR < 0.001 vs. +0.19，加上 multi-subject injection 的 validity boundary，这部分论证充分\n6. **Overall 3.0-3.5 范围**：R1 约 3.0-3.5，R2 给 3.5\n\n## Reviewer Divergence（修订版）\n\n1. **IRT misspecification 严重程度**：R1 更 concerned（fundamental threat），R2 less concerned（methodological issue）。分歧保留但双方同意论文应讨论。\n2. **Semi-synthetic 作为 primary contribution 的充分性**：R1 对 ΔTPR = 0.37 更 skeptical，R2 认为 matching strategy 本身有独立价值。\n\n---\n\n## Questions to Authors\n\n1. Conclusion 中的 \"driven by item properties\" 可否改为 \"associated with item properties\" 以避免 causal implication？\n2. 是否有 more realistic contamination patterns（如 partial memorization）的 injection 方案？即使作为 future work 讨论也有价值。\n3. 如果删除 Section 5.3（~0.5 page），释放的空间能否足够扩展 Section 5.4 的 practical recommendations？\n4. DIF-flagged items 与 Growing Pains FPC anchor items 的 Jaccard overlap 是多少？这个分析数据应已具备。\n5. 论文能否将 temporal DIF rate 提议为 BHI 的第四个维度（temporal health），增强 practical significance？\n\n---\n\n## Missing References（修订版新发现）\n\n修订版已添加 BHI 和 Benchmark²。剩余 minor gaps：\n- ATLAS (Li et al. 2025)——已在 bib 但可能仍未引用\n- Orphan bib entries 是否已清理——状态不明\n\n---\n\n## External Review\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：已完成（Round 5 时获取）。2 warnings（pages 3-5 无 display items 间隔、主正文仅 4 个 display items）、7 info。修订版可能已改变布局，如需要可重新派发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.5 | 3.5 | 3.5 |\n| Reproducibility | 4 | 4 | 4 |\n| Clarity | 4 | 4 | 4 |\n\n**置信度**: 4/5\n\n**与 Round 5 的变化**：\n- Overall 不变（3.5），但修订版改善了多个 Round 5 问题\n- 新增问题：binary flipping ecological validity（MF-2 的新维度）、IRT misspecification（SF-4）、论文聚焦度（SF-1 中建议删除 Section 5.3）\n- 被有效解决的问题：multi-subject injection、LLM-specific challenges、contribution 重组、标题软化\n\n**判断依据**：\n修订版有显著进步——multi-subject injection 和 LLM-specific challenges 节有效回应了 Round 5 的核心批评。但两个问题阻止论文上升到 4.0（Conference）：\n1. **Causal language 残余 + binary flipping ecological validity** — 论文的核心 claim 仍然比数据支持的更强\n2. **Practical recommendations 空洞** — 与论文的 policy message（\"need psychometric monitoring\"）不匹配\n\n**升级到 4.0 的路径**（两位 Reviewer 共识）：\n1. 清除 Conclusion 中的 causal language（cost: 低）\n2. 删除 Section 5.3，释放空间给 Section 5.4（cost: 中）\n3. 在 Limitations 中讨论 binary flipping 局限性 + IRT misspecification（cost: 低）\n\n如果这 3 项在提交前完成，论文可达 Conference 水平。\n\n**EMNLP 2026 评分映射**：3.5 = Borderline Conference\n\n---\n\n## 附录：Issue Tracker 同步\n\n已更新 `review_issues.yaml`：\n- 2 个 critical issues open（MF-1 causal language, MF-2/R5-N1 ecological validity）\n- 8 个 warning issues open\n- 1 个 issue resolved in Round 6（R2-N2 novelty — LLM-specific challenges 有效回应）\n- 6 个 issues resolved in prior rounds"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-21T17:52:14.141723+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-21T17:52:24.542765+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Round 5 报告已提交', 'status': 'completed', 'activeForm': 'Round 5 报告已提交'}, {'content': 'Round 6: 修订版论文审稿——收集 R1/R2 审稿 + 交叉回应', 'status': 'completed', 'activeForm': '收集修订版审稿和交叉回应'}, {'content': 'Round 6: 收敛判断 + 报告更新 + Issue Tracker 同步', 'status': 'completed', 'activeForm': '合成更新报告并同步 Issue Tracker'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Round 5 报告已提交', 'status': 'completed', 'activeForm': 'Round 5 报告已提交'}, {'content': 'Round 6: 修订版论文审稿——收集 R1/R2 审稿 + 交叉回应', 'status': 'completed', 'activeForm': '收集修订版审稿和交叉回应'}, {'content': 'Round 6: 收敛判断 + 报告更新 + Issue Tracker 同步', 'status': 'completed', 'activeForm': '合成更新报告并同步 Issue Tracker'}]"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-21T17:52:24.593472+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 194 · 2026-05-21T17:52:30.004532+00:00_

修订版审稿报告（Round 6）已提交给 Research Director。

**核心结论**：修订版有显著改善（multi-subject injection、LLM-specific challenges、标题软化、contribution 重组），但 Overall 维持 3.5（Borderline Conference）。升级到 4.0 的路径明确：(1) 清除 Conclusion 中残余 causal language，(2) 删除 Section 5.3 释放空间扩展 Section 5.4 practical recommendations，(3) 在 Limitations 中讨论 binary flipping 局限和 IRT misspecification。Issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 24

## Round 24

10 recorded events


### User

_source line 195 · 2026-05-21T17:52:31.074457+00:00_

[Reviewer 2 审稿结果]:
已提交交叉回应。与 R1 在核心判断上高度一致：Overall 3.5 (Borderline Conference)，主要分歧仅在 IRT misspecification 的严重程度上（我认为对 non-parametric MH-DIF 是 methodological issue 而非 fundamental threat）。等待 Director 进入收敛阶段。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 2 审稿意见（方法严谨性 + 实验设计）

### ⚠️ 重要前置说明：实际论文与 Director Summary 不一致

Director 提供的 Paper Summary 描述了一篇包含 §4.1-4.11（11 个实验子节）、Tables 1-13、Appendices A-E 的论文。**实际 PDF 的内容与此不符：**

| Director Summary | 实际论文 |
|---|---|
| Title: "...A Psychometric DIF Analysis of 5,227 Models on MMLU" | Title: "...A Large-Scale Psychometric Audit of 5,227 Models" |
| §4.1-4.11（含 permutation null, ConStat, DVD, graceful degradation, odds ratio regression, IFT） | §4.1-4.7（Validation, Temporal, Ground Truth, Structural, Semi-synthetic, Downstream, Cross-Benchmark） |
| Tables 1-13 | Tables 1-3 + 1 appendix table |
| Appendices A-E（RL robustness, Ensemble fusion, Bifactor IRT, Item gen calibration, Bayesian DIF） | Appendices A-D（Method Details, Structural Details, Figures, Cross-Benchmark） |
| Eff. C% ≈ 24.5（permutation null subtraction） | Raw C% = 31.3%，无 permutation null |
| ρ ≈ 0.994 | ρ ≈ 0.997 |
| GSM1K r = -0.35 | GSM1K r = -0.478 |
| "98% |Lz|>2, CFI=0.72" | 未报告 IRT fit statistics |

**以下审稿意见基于实际 PDF 内容。**

---

## 与 Round 1 对比：修改响应评估

论文针对 Round 1（R1 + R2）反馈做了实质性修改，逐条评估：

| Round 1 问题 | 修改情况 | 评估 |
|---|---|---|
| R1-N1: Semi-synthetic ecological validity | Proposition 1 限定为 "single-subject"，新增 multi-subject injection (k∈{1,3,5,10,20}) → ΔFPR<0.007 for k≤5 | ✅ 核心关切已回应，但仅 1 段，应扩展 |
| R1-N2: 因果模糊性 / "Instability" framing | Title "Psychometric Instability" → "Temporal Measurement Drift"；Section 4.2 标题同步更改；Discussion 5.2 明确承认双向解读 | ✅ 充分回应 |
| R1-N3: Bootstrap CI 不对称性 | 明确 "B=1,000 model-level resamples" | ⚠️ 部分回应（CI 不对称性原因仍未讨论） |
| R1-W4/R2-N1: Claim 4 GSM1K 支撑不足 | Contributions 从 4 个缩减为 3 个，Claim 4 降级为 Discussion 5.3 exploratory evidence | ✅ 充分回应 |
| R2-N2: 方法论新颖性 | 新增 "LLM-specific challenges" 段落（Method 3.2），讨论 local independence、fine-tuned variants、non-normal distribution、multidimensionality | ✅ 充分回应 |
| R2-N3: Temporal cohort 粗糙 | Title 改善；Limitations 明确讨论；6-month window 仍为 one-liner | ⚠️ 部分回应 |
| R2-W1: Audit protocol 过短 | 扩展为 graduated thresholds: <15% monitor, 15-25% flag, >25% act | ✅ 有改善 |
| R2-W3: Running example | Method 3.2 新增具体 formal-logic item 示例（α_MH=0.42, Δ_MH=2.04） | ✅ 有效 |
| R2-W4: Growing Pains 区分 | Related Work 扩展："Growing Pains assumes anchor item stability... Empirical comparison awaits public release" | ⚠️ 合理但仍无定量比较 |
| R2 Missing References | 新增 ATLAS (li2025atlas), MedIRT (luo2025medirt), BHI (zhu2026bhi), Benchmark² (qian2026benchmark2) | ✅ 全部补充 |

---

## 维度评分

### Soundness: 4 / 5

**MH-DIF 应用正确性**：公式 (1)-(2) 标准，K=5 quintile binning 符合 ETS 惯例，ETS C 分类（|Δ_MH|≥1.5 + p<0.05 双阈值）严格。Running example（formal-logic item, α_MH=0.42 → Δ_MH=2.04）帮助读者验证计算。

**控制实验设计合理**：5 种 cohort design 系统排除替代解释——random split (0.18%) 排除噪声、ability-quintile (2.9%) 排除纯能力差异、within-family (61.3% → matched 28.3%) 展示 ability confounding 的影响、matched-ability (31.3% → 28.9%) 量化残余 ability effect（~2.4pp）。六种替代解释均被测试，收敛于 ~28-29% 的 floor，令人信服。

**Proposition 1 修订得当**：限定为 "under single-subject cross-subject matching"，数学上 trivially true 但不再 overclaim。multi-subject injection boundary (ΔFPR<0.007 for k≤5) 是对 R1-N1 的直接回应，提供了方法适用边界的实证依据。

**扣分原因**：
(a) **缺少 permutation null**：random-split control (0.18%) 是 perfect null 条件下的估计，但不等于 permutation null。随机打乱 cohort labels 后的期望 C% 是什么？如果 permutation null 为 ~5%，则 "effective" DIF 应为 ~26% 而非 31%。这对 headline 数字的解读有实质影响。论文缺少这个分析。
(b) **IRT model fit 未评估**：论文使用 2PL 参数做 power analysis（ā=1.2, b̄=-0.84），但未报告 model fit statistics（如 |Lz|, CFI, RMSEA）。MH-DIF 本身是非参数方法，不依赖 IRT fit——这点论文正确指出。但 MMLU 的 57 subjects 显然违反 unidimensionality，论文在 "LLM-specific challenges" 段中承认但未量化违反程度。
(c) **binary flipping 的生态效度局限**：注入框架用 uniform rate p 翻转 incorrect→correct，真实 contamination 是非均匀的（部分 items 被完整记忆、部分仅记忆 answer letter、RLHF 创造非均匀效应）。论文应讨论对 non-uniform injection 的敏感性。

### Reproducibility: 4 / 5

**强项**：METABENCH 数据公开可获取、anonymous.4open.science 代码链接、power analysis 参数显式（"empirical 2PL parameters from PSN-IRT: ā=1.2, b̄=-0.84; 14,042 MMLU items"）、bootstrap 参数明确（B=1,000 model-level resamples）。

**扣分**：multi-subject injection protocol 细节不足——k 的选择、每个 k 下的随机抽取策略、"5 random draws each" 的具体实现。Semi-synthetic 注入的 ETS A 选择标准（"items classified as ETS A in the uninjected data"）的确切阈值应明确。

### Experimental Coverage: 3.5 / 5

**Coverage Check（对照 Director 提供的 16 项实验清单）：**

| # | 实验 | 状态 | 位置 |
|---|---|---|---|
| 1 | real_data_dif_mmlu | ✅ 完整 | §4.2 |
| 2 | rl_robustness_validation | ❌ 不存在 | — |
| 3 | constat_perturbation_eval | ⚠️ 提及但无专门分析 | §4.3 context |
| 4 | dvd_generation_variance_eval | ❌ 不存在 | — |
| 5 | ensemble_fusion | ❌ 不存在 | — |
| 6 | cross_benchmark_gsm8k | ✅ 完整 | §4.7 |
| 7 | bifactor_irt_equating_pilot | ❌ 不存在 | within-subject DIF 最近似 |
| 8 | item_generation_calibration | ❌ 不存在 | — |
| 9 | cumulative_bayesian_dif | ❌ 不存在 | — |
| 10 | graceful_degradation_analysis | ⚠️ 隐含（ρ≈0.997） | §4.6 一句话 |
| 11 | item_focused_trees | ❌ 不存在 | — |
| 12 | architecture_stratified_dif | ⚠️ 部分 | Appendix A.2（99.98% decoder-only） |
| 13 | semi_synthetic_contamination_validation | ✅ 完整 | §4.5 |
| 14 | multi_benchmark_temporal_dif | ✅ 完整 | §4.7 |
| 15 | permutation_null_c_rate | ❌ 不存在 | — |
| 16 | odds_ratio_regression_transparency | ⚠️ 嵌入§4.2 | Simpson's paradox，OR 分析 |

**4/16 完整覆盖，4/16 部分覆盖，8/16 不存在。** 但需注意这些是 "imagined experiments"——并非全部需要。对于 EMNLP 论文，已有的 7 个 experiment sections + 4 appendices 构成完整的故事。最关键的缺失是 **permutation null**（#15）和 **graceful degradation 的系统分析**（#10）。

---

## Director 具体问题回应

### Q1: IRT 1D model misspecification

论文未报告 |Lz| 或 CFI。如果 Director 所述的 "98% |Lz|>2, CFI=0.72" 属实，这表示 1D IRT 严重 misspecified。但论文的核心论点——MH-DIF 是非参数方法，不依赖 IRT model fit (Holland & Thayer, 1988)——是技术上正确的。论文在 §3.2 中提供了三层防护：(a) IRT θ 与 total score r=0.9986 → CTT-based stratification 无 bias；(b) 99.98% decoder-only → architecture 不是 confound；(c) cross-subject matching 处理 multidimensionality。

**我的评估**：这三层防护对 MH-DIF 的有效性是 convincing 的——MH-DIF 的 conditional on observed score 性质使其对 latent structure misspecification 具有鲁棒性。但论文至少应报告 fit statistics（即使结论是"不影响 MH-DIF"），因为这是 transparent reporting 的要求。如果 CFI=0.72（远低于 0.95 conventional threshold），应在 Limitations 中讨论。

### Q2: Binary flipping 的真实世界相关性

显著局限。Uniform flipping at rate p 假设所有被污染 items 有相同的 exploitation probability，但真实 contamination 是 item-specific 的——更容易记忆的 items（如 factual recall）vs. 推理题，效果差异很大。论文应至少讨论 non-uniform injection (e.g., item-difficulty-dependent exploitation rate) 的 sensitivity，或将此列为 Limitations 而非仅隐含。

当前 Limitations 段 "Methodological scope" 提到 "DIF detects that... not why" 但未讨论注入框架本身的简化。

### Q3: Permutation null

**论文中不存在 permutation null 分析。** 这是最显著的实验缺失。random-split (0.18%) 是 perfect null（同一 cohort 内部），ability-quintile (2.9%) 是 ability-only null。但 permutation null（随机打乱 temporal labels 后的 C%）才是 31.3% 的正确 baseline comparator。

如果 permutation null ~5%（如 Director 摘要暗示），则：
- "effective" temporal DIF = 31.3% - 5.2% = 26.1%
- 论文标题中 "31%" 可能高估实际效应
- 所有下游分析（downstream impact, cross-benchmark ratios）都需要调整

**建议**：这是论文应补充的最重要实验。1,000 次 permutation 的计算成本很低。

### Q4: GSM1K 负相关

论文报告 r=-0.478（非 Director 所述 -0.35）, p=0.005, partial r=-0.385, p=0.027, N=33。

修改后的处理**得当**：从 Contribution 列表中移除，降级为 Discussion 5.3 的 "exploratory evidence"，Limitations 明确标注 "limited statistical power"。N=33 确实无法支撑 firm conclusions，但作为 supplementary observation 是可接受的。

### Q5: RL robustness

论文中不存在。不是关键缺失——论文未声称对 RL post-training 的 robustness。

### Q6: Cross-subject matching ΔFPR

**这是修改最成功的部分。** Round 1 我将此列为 N1 (critical)，修改后：

1. Proposition 1 明确限定为 "single-subject injection" → 不再 overclaim
2. Multi-subject injection (k∈{1,3,5,10,20}) 提供了实证边界：ΔFPR<0.007 for k≤5 (<9% of domains)，k=10 (18%) 时 ΔFPR 升至 0.026-0.069
3. Limitation 段明确："cross-subject matching assumes contamination affects a minority of domains; when contamination spans >10 subjects (>18% of MMLU), ΔFPR rises to 0.026-0.069"

**论点现在是 convincing 的**：single-subject 有数学保证，multi-subject 有实证边界和 graceful degradation，boundary condition 被明确陈述。唯一改进空间是将 multi-subject 结果从 1 段扩展为 table/figure。

---

## Strengths（≥3）

1. **大规模、系统的 confound 控制**：5 种 cohort design × 6 种替代解释 × 4 个 threshold sensitivity 点，形成了对 31% DIF finding 的全方位 triangulation。matched-ability 分析收敛于 ~28-29% 的 floor（跨不同比较）尤其令人信服。

2. **Ground truth meta-critique 具有社区价值**：Contribution 2 (enrichment=0.964, Jaccard=0.206) 对 contamination detection 文献中普遍使用 web-overlap labels 的做法提出了有实证支撑的质疑。Discussion 5.2 现在明确承认双向解读，增强了论证的诚实性。

3. **Semi-synthetic 框架的 boundary characterization**：multi-subject injection 将框架从 "trivially true by construction" 升级为 "empirically characterized with explicit boundary"（k≤5 safe, k=10 degradation），这是对 Round 1 批评的高质量回应。

4. **LLM-specific methodological adaptations**：新增的 "LLM-specific challenges" 段落（§3.2）不是泛泛之谈，而是针对 local independence (permutation simulation Q3=4.6-34.2%)、fine-tuned variant independence (graduated de-duplication)、non-normal ability (quintile-based stratification)、multidimensionality (cross-subject matching) 提出了具体应对措施。

5. **Cross-benchmark replication at scale**：6 个 METABENCH benchmarks（27,125 items）的 DIF 发现具有一致性（knowledge/reasoning C%≥26.9% > procedural C%≤18.9%），且每个都远高于 random baseline (45-174×)。

---

## Weaknesses（≥3）

1. **缺少 permutation null——headline 数字缺乏正确 baseline**：31.3% 是 raw C%，但无 permutation null 作为 baseline。random-split (0.18%) 是完美 null，不代表 realistic null（cohort 间存在微小系统差异的期望 DIF）。如果 permutation null ~5%，则 effective DIF ~26%，对标题和所有下游分析有实质影响。这是论文最关键的方法论缺失。

2. **IRT model fit 未报告**：论文使用 2PL 参数做 power analysis 但不报告 fit statistics。MH-DIF 虽不依赖 IRT fit，但 transparent reporting 要求至少呈现 unidimensionality 评估（哪怕结论是"MH-DIF 对此鲁棒"）。如果 MMLU 确实 CFI=0.72，这是重要的 contextual information。

3. **Binary flipping 简化未充分讨论**：注入框架使用 uniform rate p，真实 contamination 是 heterogeneous 的。这限制了 semi-synthetic 结果向真实场景的推广。当前 Limitations 未涉及此点。

4. **Multi-subject injection 结果过于压缩**：这是论文回应 R1-N1 的核心新增实验，但仅占 Section 4.5 的 1.5 句话。k∈{1,3,5,10,20} 的 ΔFPR 值应以 table 或 figure 呈现，而非 inline text（"ΔFPR<0.007 for k≤5; at k=10, ΔFPR rises to 0.026-0.069"）。

5. **Director 期望的实验覆盖缺口**：16 项计划实验中仅 4 项完整覆盖。特别缺失的 permutation null (#15)、graceful degradation 系统分析 (#10)、ConStat/DVD 专门对比 (#3/#4) 会加强论文。即使不全做，permutation null 是必须的。

---

## Questions to Authors（≥2）

**Q1**：能否补充 permutation null 分析？具体来说：将 cohort labels (2023/2024) 随机打乱 1,000 次，每次重新计算 C%，报告 permutation null distribution 的 mean 和 95th percentile。这将为 31.3% 提供 principled baseline，并可能改变 headline 数字（从 31% 改为 null-adjusted 值）。

**Q2**：论文声称 "IRT θ estimates correlate at r=0.9986 with total scores"（§3.2），但未报告 underlying IRT model 的 fit statistics。能否报告 MMLU 12,508 items 在 2PL 下的 CFI、RMSEA、或 |Lz| person-fit 分布？如果 fit 确实很差，这 paradoxically 支持论文的论点（MH-DIF 作为非参数方法是更安全的选择），但应 transparently 报告。

**Q3**：multi-subject injection 的 boundary (k≤5 safe) 在 MMLU 语境中意味着什么？如果 real-world contamination 同时影响 >5 个 subjects（例如一个 model 训练时 ingest 了整个 MMLU dataset），cross-subject matching 的 ΔFPR 保证就失效了。论文如何论证 MMLU 的真实 contamination pattern 落在 k≤5 的安全区间内？

---

## Preliminary Overall Assessment

**Overall: 3.5 / 5**（Borderline Conference）

**Calibration rationale**：

**3.5 而非 4.0 的原因**：
- 缺少 permutation null 是重要的方法论缺失，直接影响 headline 数字的可信度
- IRT fit 未报告降低了 methodological transparency
- 多项计划实验未执行（虽然 "imagined" 不代表必须，但 permutation null 是标准做法）
- Binary flipping 简化对 semi-synthetic 框架的 real-world relevance 有实质限制

**3.5 而非 3.0 的原因**：
- Round 1 的三个 critical issues (N1-N3) 均有实质性回应——title 改善、Proposition 1 限定、multi-subject boundary、bootstrap 单位明确
- Confound 控制在 EMNLP 同类论文中属于上乘水平（5 cohort designs + 6 alternative explanations）
- Ground truth meta-critique (Contribution 2) 对社区有独立价值
- Cross-benchmark replication (6 benchmarks, 27,125 items) 提供了强 robustness
- Writing quality 高，revised framing ("drift" not "instability") 更准确

**升至 4.0 的路径**：
1. 补充 permutation null → 提供 null-adjusted C% 作为 headline
2. 报告 IRT fit statistics（即使结论不变）
3. Multi-subject injection 结果以 table 呈现
4. 在 Limitations 中增加 binary flipping 简化的讨论

**结论**：论文从 Round 1 到 Round 2 的修改是认真且有效的，核心关切均有回应。但 permutation null 的缺失使 headline 数字的解读存在不确定性，阻止了评分升至 Conference accept。

---

[Reviewer 1 审稿结果]:
审稿意见已提交。

核心发现：论文从 Round 1 到本版做了实质性修改（title 改善、Proposition 1 限定、multi-subject injection、LLM-specific challenges 段落、Claim 4 降级），回应了 R1/R2 的主要关切。但实际论文内容与 Director 提供的 Paper Summary 存在显著差异——16 项计划实验中仅 4 项完整覆盖，最关键的缺失是 permutation null 分析。评分维持 Overall 3.5 (Borderline Conference)，核心阻碍是 headline "31%" 缺乏 permutation null baseline。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 — Convergence Round 最终评分

### 版本问题再次提示

Director 的 convergence synthesis 中有两个与我实际看到的 PDF **不符** 的 factual claims：

1. **"Related work is insufficient — 10 references and 3 paragraphs"**：当前 PDF 有 **~55+ references** 和 **4 个结构化 Related Work 子节**（Contamination Detection / IRT in LLM Evaluation / DIF Methodology and Measurement Invariance / Benchmark Quality and Design），覆盖面相当全面。我在上一轮审稿中给 Related Work Completeness 4/5。

2. **"11 experiment sections in 8 pages"**：当前版本的实验结构更聚焦（Section 4.1-4.7 + Section 5.1-5.4），虽然仍然偏多但不是 11 节。

如果 Director 和 R1 审的是一个 **更早的 10-reference 版本**，而我审的是 **当前修订版**，那我们的 divergence 部分来自版本差异而非 judgment 差异。请确认我们是否在审同一版本。

---

### 最终评分

**Overall: 3.5 — Borderline Conference（维持，不调整至 3.0）**

理由：

**我同意 convergence synthesis 中 6/7 个共识点**，但对结论性判断从 3.5 降到 3.0 持保留意见：

| 共识点 | 我的立场 |
|--------|---------|
| Cross-subject matching 是最强贡献 | ✅ 完全同意 |
| 论文 scope 偏广 | ✅ 同意，但修订版已改善（3 contributions 代替 4，Section 5.3 降级为 discussion） |
| Related work 不足 | ❌ 不同意——当前版本 55+ refs, 4 子节，覆盖充分。如果 R1 审的是 10-ref 版本，此 concern 不适用于当前版本 |
| IRT misspecification 部分解决 | ✅ 同意，但如我上轮所述，MH-DIF 是 non-parametric，不直接依赖 IRT model fit |
| Honest reporting | ✅ 完全同意 |
| Novelty limited | ✅ 部分同意——known method + new domain，但 LLM-specific challenges 节和 multi-subject injection 为 transplant 增加了实质价值 |
| Semi-synthetic ΔTPR=0.37 moderate | ✅ 同意 |

**从 3.5 降到 3.0 需要的理由我认为不充分**：

(a) 当前版本的 Related Work 问题已基本解决——如果这是 3.0 的一个支柱论据，但实际论文已有 55+ 参考文献，则此论据不成立。

(b) 修订版新增了 multi-subject injection (k∈{1,3,5,10,20}) 和 LLM-specific challenges 论证，这些在 R1 评审的版本中可能不存在。

(c) 3.0 意味着 "Findings-level"，即论文的 core contributions 不够 main conference。但 cross-subject matching（ΔFPR < 0.001 vs +0.19）+ 5,227 models × 6 benchmarks 的大规模实证 + ground truth meta-critique，我认为在 Findings 和 Conference 的边界上，而非明确在 Findings 一侧。

**但我承认以下因素阻止我上调至 4.0**：

(a) GSM1K N=33 evidence 仍然太弱（两位 reviewer 共识）
(b) Practical recommendations 仍然空洞（Section 5.4 只有 3 句话）
(c) Semi-synthetic 的 ecological validity concern（binary flipping）未解决
(d) Causal language 需要进一步软化

---

### 最终评分确认

| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement / Novelty | 3.5/5 |
| Reproducibility | 4.0/5 |
| Clarity | 4.0/5 |
| **Overall Assessment** | **3.5 (Borderline Conference)** |

如果 Director 判断版本差异是 divergence 的主因，且确认 R1 审的是 10-ref 版本而非当前版本，我建议基于 **当前版本** 统一审稿。在此基础上，R1 可能也会上调部分评分（特别是 Related Work 和 scope 相关的 concerns）。

---

[Reviewer 2 审稿结果]:
审稿已提交。我维持 **Overall 3.5 (Borderline Conference)**，拒绝降至 3.0——主要原因是 Director 的 convergence synthesis 基于一个更早的 10-reference 版本，而我审阅的当前 PDF 有 55+ references 且 Related Work 覆盖充分。同时指出了需要 Director 确认版本一致性的问题。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 R2 Round 2 意见

### ⚠️ 前置说明：R2 与我可能在审不同版本

R2 描述的论文（"11 experiment sections + 5 appendices"，"Only 10 references"，"3 paragraphs of related work"）与我实际读到的 PDF 有显著差异。**我读到的论文**有 7 个 experiment sections、4 appendices、~60 篇引用、4 段 Related Work（Contamination Detection / IRT in LLM Evaluation / DIF Methodology / Benchmark Quality）。以下回应基于我实际读到的版本。

---

### 逐条回应 R2 Key Concerns

**[REBUT] R2-Concern-1: "Known method → new domain" novelty ceiling → Novelty 2.5/5**

R2 认为 MH-DIF 是 35+ 年的 textbook method，application novelty 不足以支撑 EMNLP Main。我不同意将 novelty 评为 2.5。理由：

1. **论文已明确 self-position 为 empirical + methodological contribution**（Introduction: "Our contributions are methodological and empirical, not algorithmic"）。以 "算法新颖性" 标准评判一篇明确声明 "不是算法贡献" 的论文是 criteria mismatch。

2. **"Known method → new domain" 在 EMNLP 有先例且被接受**：Rodriguez et al. (2021, ACL) 将 IRT 应用于 NLP leaderboards——同样是 "old psychometric method → NLP evaluation"——被 ACL main 接收。Vania et al. (2021, ACL) 用 IRT 比较 test sets，同样获 ACL main。关键不在方法是否新，而在 findings 是否 non-trivial。

3. **Non-trivial findings 确实存在**：
   - 31% temporal DIF 在 12,508 items × 5,227 models 上的发现是 previously unknown 的实证事实
   - Ground truth meta-critique（enrichment=0.964）揭示了 contamination detection 文献的 systematic evaluation flaw
   - Semi-synthetic 框架的 multi-subject boundary (k≤5 safe, k=10 degradation) 是 reusable methodological contribution
   
4. **"LLM-specific challenges" 段落（§3.2）展示了 non-trivial adaptation**：permutation simulation for LD (Q3=4.6-34.2%)、graduated de-duplication for family structure、quintile-based stratification for non-normal ability——这些不是 trivial transplant。

**我的评分**：Excitement 3.5/5（维持不变）。novelty ceiling 确实存在但被 empirical significance 和 methodological adaptation 弥补。

---

**[AGREE with nuance] R2-Concern-2: Scope too broad, depth too shallow**

如果 R2 审的版本确实有 11 个 experiment sections + 5 appendices，我同意 breadth > depth 是问题。但**我读到的版本**更聚焦：7 个 experiment sections（§4.1-4.7），核心故事清晰——temporal DIF (§4.2) → ground truth mismatch (§4.3) → structural controls (§4.4) → semi-synthetic validation (§4.5) → downstream impact (§4.6) → cross-benchmark (§4.7)。

**我同意的部分**：即使在当前版本中，某些分析仍然过于压缩：
- Multi-subject injection (§4.5)：k∈{1,3,5,10,20} 的关键结果只有 1.5 句话，没有 table 或 figure
- Downstream impact (§4.6)：多个统计量（ρ≈0.997, z=-8σ to -49σ, cohort gap=96.2）密集堆叠在一段中
- 6-month window 分析（§4.7 最后一段）：仅 one-liner

**但我不同意 "technical report" 的判断**。论文有清晰的叙事弧（diagnostic lens, not quality filter）和 well-structured contributions。问题不是 scope 太广，而是某些关键新增实验（特别是 multi-subject injection）的 presentation 不够 prominent。

---

**[REBUT] R2-Concern-3: Thin related work (only 10 references, 3 paragraphs)**

**这与我读到的论文严重不符。** 实际 Related Work（§2）包含：
- **Paragraph 1 (Contamination Detection)**：11 citations（Min-K%, Min-K%++, Time Travel, ConStat, DVD, Self-Critique, Balloccu, Li et al., Carlini, Tirumala, Wang et al.）
- **Paragraph 2 (IRT in LLM Evaluation)**：11 citations（Lalor, Vania, Rodriguez, PSN-IRT, TinyBenchmarks, Hardy, ATLAS, MedIRT, Growing Pains, Kim FPC）
- **Paragraph 3 (DIF Methodology)**：14 citations（Holland, Clauser, Swaminathan, SIBTEST, Lord, Raju, Zumbo, Meredith, Vandenberg, MIMIC, Woods, Teresi, Nandakumar, Donoghue, Belzak）
- **Paragraph 4 (Benchmark Quality)**：8 citations（BHI, Benchmark², Maeda, Dynabench, LatestEval, LiveBench, Chatbot Arena, Chang survey, Burnell）

总计 ~44 unique citations in Related Work alone，总引用 ~60 篇。这不是 "thin"——覆盖了 contamination detection、IRT-for-LLM、DIF methodology、benchmark reform 四个维度。

如果 R2 审的是一个早期版本（修改前只有 ~10 references），则这条 concern 已被修改充分回应。

---

**[AGREE] R2-Concern-4: Meta-critique depth**

同意 Contribution 2 的深度可以更好。当前论文证明了 near-independence（enrichment=0.964, Jaccard=0.206, φ=0.012），Discussion 5.2 承认了双向解读。但分析止步于 "category error"——为什么 web-overlap labels 和 DIF 正交？论文给出的解释是 "global exposure vs. differential functioning"（Figure 1），这在概念层面有效，但缺乏对 **哪些 item 特征** 导致 web-overlap=contaminated + DIF=clean（或反过来）的深入分析。

一个简单的 improvement：对 4 个象限（web-contaminated × DIF-flagged 的 2×2）做 item characteristic analysis（difficulty, discrimination, subject distribution），看是否有 systematic pattern。这会将 "conceptual category error" 升级为 "empirically grounded category error"。

---

### R2 提出的三个 meta-questions

**Q: Does the methodological rigor compensate for limited novelty?**

**是的，在一定程度上。** EMNLP 近年接收的 analysis/empirical papers 表明社区认可 "rigorous application of known methods revealing non-obvious findings"。关键是 findings 是否 actionable：
- 31% temporal DIF → motivates psychometric monitoring（actionable）
- Ground truth meta-critique → challenges evaluation methodology of contamination detectors（actionable）
- Semi-synthetic framework → reusable tool（actionable）

但如果 permutation null 表明 effective DIF 仅 ~26% 而非 31%，actionability 不变但 headline 需要调整。

**Q: Is the broad experimental scope a strength (thoroughness) or weakness (dilution)?**

**在当前版本中是 strength**（7 sections，叙事清晰）。但 presentation 的 unevenness（multi-subject injection 只有 1.5 句，downstream impact 信息过密）使部分 thoroughness 被压缩成了 density。解决方案不是删减实验，而是重新分配 space——压缩 ground truth mismatch（§4.3，当前一整段重复 near-independence 的多个统计量），扩展 multi-subject injection 和 downstream impact。

**Q: Does the semi-synthetic framework alone justify conference-level contribution?**

**单独不够，但作为 3 个 contributions 之一是 sufficient。** Semi-synthetic 框架 + multi-subject boundary 是 reusable methodological contribution，但需要 empirical findings（31% DIF）和 meta-critique 作为 motivation 和 validation。三者组合构成 conference-level package。

---

### 综合评估：是否调整我的评分？

**维持 Overall 3.5**，但对 sub-dimensions 有微调：

| 维度 | 我的评分 | R2 评分 | 综合后 |
|---|---|---|---|
| Soundness | 4.0 | — | 4.0（维持）|
| Excitement / Novelty | 3.5 | 2.5 | 3.0（下调 0.5）|
| Reproducibility | 4.0 | — | 4.0（维持）|
| Clarity | 4.0 | 3.0 | 3.5（下调 0.5）|
| Overall | 3.5 | 3.0 | **3.5**（维持）|

**下调 Excitement 至 3.0 的理由**：R2 的 novelty ceiling 论点有合理性——MH-DIF 确实是 well-known method，cross-subject matching 在 psychometrics 中有先例。论文的价值更多来自 **scale + findings** 而非 **method innovation**。3.0 = "might discuss certain points; would attend if time permits"——对一篇 rigorous application paper 是合理定位。

**下调 Clarity 至 3.5 的理由**：R2 指出的 scope/depth 不平衡（某些分析过于压缩）在我的审稿中也有体现（multi-subject injection 1.5 句，downstream impact 信息过密）。但 overall writing quality 高于 3.0——叙事弧清晰、Figure 1 有效、running example 有帮助。

**维持 Overall 3.5 的理由**：
- 缺少 permutation null 阻止升至 4.0（方法论完整性的硬伤）
- Soundness 4.0 + 大规模 empirical replication + responsive revision 阻止降至 3.0
- Borderline Conference = "可能值得 main conference，但有可修复的缺陷"——准确描述当前状态

**与 R2 的分歧 summary**：
- Novelty：R2 = 2.5，我 = 3.0（我认为 LLM-specific adaptations 和 empirical significance 弥补了 method novelty ceiling）
- Related Work：R2 = 2.5，我认为实际论文的 Related Work 是 adequate（~44 citations，4 paragraphs）——**如果 R2 审的是不同版本，这条 concern 可能已 obsolete**
- Overall：R2 = 3.0，我 = 3.5（主要因为我对 confound 控制的评价更高）

---

[Reviewer 1 审稿结果]:
审稿交叉回应已提交。

核心结论：维持 Overall 3.5。同意 R2 的 novelty ceiling 论点（Excitement 从 3.5 下调至 3.0），但反驳 R2 关于 Related Work "only 10 references" 的批评——实际论文有 ~60 篇引用和 4 段充实的 Related Work，R2 可能审的是不同版本。最关键的共识是 permutation null 的缺失阻止评分升至 4.0。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 — Convergence Round 最终评估

---

### 对 Synthesis 的回应

Director 的 synthesis 存在一个根本性问题：**它描述的论文与我读到的 PDF 不一致。** 我需要在回应前再次澄清：

| Synthesis 描述 | 实际 PDF |
|---|---|
| 11 experiment sections in 8 pages | 7 experiment sections (§4.1-4.7) |
| 10 references, 3 paragraphs related work | ~60 references, 4 paragraphs (~44 unique citations in §2) |
| ConStat, DVD, odds ratio, IFT sections | ConStat/DVD 仅在 §4.3 context 中提及；odds ratio 嵌入 §4.2；无 IFT 专节 |
| RL robustness, bifactor, item generation 负面结果 | 均不存在于论文中 |
| ΔTPR=0.37 at p=0.5 | ΔTPR=+0.508 at p=0.5 |
| IRT misspecification (98% \|Lz\|>2, CFI=0.72) | 未报告 |

**我的最终评估基于实际论文内容。** 如果 Director 和 R2 审的是另一个版本，我们的评分差异部分源于版本差异而非审稿判断差异。

---

### Areas of Agreement — 我的确认/修正

**1. Cross-subject matching 是最强贡献** → ✅ 完全同意。Proposition 1（properly scoped to single-subject）+ multi-subject boundary（ΔFPR<0.007 for k≤5）是 clean, reusable methodological contribution。

**2. Paper scope 过广** → ⚠️ 部分同意。在我读到的版本中（7 sections, not 11），scope 是 manageable 的。但某些分析确实过于压缩（multi-subject injection 1.5 句，downstream impact 信息密度过高）。问题不是 "too many experiments" 而是 "space allocation uneven"。

**3. Related work 不足** → ❌ 不同意（基于实际 PDF）。实际论文有 4 段 Related Work，覆盖 contamination detection（11 citations）、IRT in LLM evaluation（11 citations, 含 ATLAS, MedIRT, Growing Pains）、DIF methodology（14 citations）、benchmark quality（8 citations, 含 BHI, Benchmark²）。如果 R2 审的早期版本确实只有 10 references，这条 concern 在当前版本中已 resolved。

**4. IRT misspecification** → ⚠️ 无法确认。实际论文未报告 |Lz| 或 CFI。论文主张 MH-DIF 是非参数方法不依赖 IRT fit，技术上正确。我认为论文应报告 fit statistics（transparent reporting），但这不构成 critical flaw。

**5. Honest reporting** → ⚠️ 无法确认。论文中没有 RL robustness、bifactor、item generation 的负面结果。GSM1K 的 exploratory status 确实被 honestly scoped。

**6. Novelty limited** → ✅ 同意。与 R2 的交叉回应后我将 Excitement 下调至 3.0。

**7. Semi-synthetic detection power moderate** → ⚠️ 数字不一致。实际论文报告 ΔTPR=+0.508 at p=0.5（非 0.37）。+0.508 是 meaningful detection power。但 binary flipping 确实是 simplification。

---

### Convergence Questions 回应

**Q1: Does this paper change how the community evaluates LLM benchmarks in practice?**

**Yes, incrementally but meaningfully.** 具体的 practical impact：
- Ground truth meta-critique 直接改变 contamination detection 的 evaluation methodology（不应仅用 web-overlap labels 验证 differential detectors）
- DIF audit protocol（§5.4 graduated thresholds: <15% monitor / 15-25% flag / >25% act）提供了 actionable guideline
- 31% 这个数字本身会影响社区对 MMLU 等 benchmark 的信心（即使只是 diagnostic，不是 destructive）

但 impact 是 incremental 而非 transformative——论文不提出新 benchmark 或新 evaluation paradigm，而是对现有 benchmark 增加一个 monitoring dimension。

**Q2: Is the semi-synthetic framework alone sufficient for conference-level novelty?**

**单独不够，但作为 package 的一部分是 sufficient。** 框架本身（cross-subject matching + multi-subject boundary characterization）是 reusable infrastructure，但需要 empirical findings 和 meta-critique 提供 motivation。三者的组合是否达到 conference level 取决于对 "application paper" 的接受标准。

**Q3: What's the appropriate venue — Main or Findings?**

**Findings，with a path to Main if permutation null is added。**

理由：
- **For Main (21% acceptance)**：需要 novelty + significance + soundness 全面过线。novelty 明确受限（known method → new domain），significance 虽高但 headline 数字（31%）缺少 permutation null 校准。
- **For Findings**：solid empirical contribution + reusable methodological framework + community-relevant meta-critique = Findings 的 sweet spot。

---

### 最终评分

| 维度 | 最终评分 | 变化 | 理由 |
|---|---|---|---|
| Soundness | 4.0 / 5 | 维持 | MH-DIF 应用正确，controls 充分，multi-subject boundary 是 genuine improvement |
| Excitement | 3.0 / 5 | 从 3.5 下调 | 采纳 R2 novelty ceiling 论点；application paper ceiling |
| Reproducibility | 4.0 / 5 | 维持 | Public data, code, explicit parameters |
| Clarity | 3.5 / 5 | 从 4.0 下调 | Space allocation uneven（某些关键分析过于压缩） |
| Reviewer Confidence | 4 / 5 | 维持 | 熟悉 DIF 方法论和 LLM evaluation 文献 |

**Overall: 3.5 / 5 → Findings 接收**

---

### Calibration Rationale

**3.5 = Borderline Conference / Findings accept。**

按 EMNLP 2026 标准：
- 5 = Award (top 2.5%)：不适用
- 4.5 = Borderline Award：不适用
- 4 = Conference accept：需要 novelty or significance 显著高于当前水平
- **3.5 = Borderline Conference**：当前位置
- **3 = Findings accept**：如果不修改 permutation null

**维持 3.5 而非调整的逻辑**：

- **不升至 4.0**：(a) 缺少 permutation null → headline 数字未校准；(b) novelty ceiling（R1+R2 共识）；(c) binary flipping 对 semi-synthetic real-world relevance 的限制
- **不降至 3.0**：(a) Round 1 → Round 2 的修改质量高且 responsive（title 改善、Proposition 1 限定、multi-subject boundary、bootstrap 明确、Claim 4 降级、Related Work 大幅扩充）；(b) confound 控制在同类论文中 above average；(c) Soundness 4.0 不应被 novelty concern 完全抵消

**与 R2 的最终分歧**：R2 Overall 3.0，我 3.5。差距 0.5 主要来自：
1. Related Work 评估不同（R2 说 10 refs / 3 paragraphs，我读到 ~60 refs / 4 paragraphs）
2. Soundness 权重不同（我更重视 confound 控制的系统性）
3. 版本差异可能导致部分评分基础不同

**建议 Director**：如果 R2 审的是不同版本，应请 R2 重新审阅当前 PDF 后再做最终 convergence。当前版本对 Round 1 问题的回应质量值得被 credit。

---

### 给作者的总结建议（如果进入 camera-ready）

**必须做：**
1. 补充 permutation null（1,000 permutations，随机打乱 cohort labels），报告 null-adjusted C%
2. Multi-subject injection 结果以 table/figure 呈现（当前只有 inline text）
3. 报告 IRT model fit statistics（|Lz|, CFI——即使结论不变）

**建议做：**
4. 在 Limitations 中增加 binary flipping 简化的讨论
5. 压缩 §4.3 Ground Truth Mismatch（多个 near-independence 统计量有冗余），扩展 §4.5 Semi-synthetic 和 §4.6 Downstream
6. 讨论 bootstrap CI 不对称性的来源

---

[Reviewer 1 审稿结果]:
审稿意见已提交。

最终评分 **Overall 3.5/5（Findings 接收）**。核心判断：论文对 Round 1 反馈的回应质量高（title 改善、Proposition 1 限定、multi-subject boundary、Related Work 扩充），Soundness 4.0 的 confound 控制在同类论文中属上乘。但缺少 permutation null 和 novelty ceiling 阻止了升至 Conference accept。与 R2 的 0.5 分差异主要源于 Related Work 评估不同和可能的版本差异。

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

_source line 196 · 2026-05-21T17:53:01.638831+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Round 5 初始报告', 'status': 'completed', 'activeForm': 'Round 5 报告已提交'}, {'content': 'Round 6 修订版报告', 'status': 'completed', 'activeForm': 'Round 6 报告已提交'}, {'content': 'Round 7 最终收敛报告——合成 R1/R2 最终评估 + Issue Tracker 同步', 'status': 'in_progress', 'activeForm': '合成最终收敛报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Round 5 初始报告', 'status': 'completed', 'activeForm': 'Round 5 报告已提交'}, {'content': 'Round 6 修订版报告', 'status': 'completed', 'activeForm': 'Round 6 报告已提交'}, {'content': 'Round 7 最终收敛报告——合成 R1/R2 最终评估 + Issue Tracker 同步', 'status': 'in_progress', 'activeForm': '合成最终收敛报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-21T17:53:01.739664+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "TodoWrite",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-21T17:54:09.489179+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Final convergence: Round 7 (2026-05-21)\n# R1 + R2 both at Overall 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES (open — block upgrade to 4.0)\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"Causal language 残余——Conclusion 中 'driven by' 等措辞暗示因果方向，数据只支持 association\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。R2 同意。\"\n  action_items:\n    - round: 7\n      action: \"替换 Conclusion 中 'driven by' → 'associated with'；全文检查 causal-leaning 措辞\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null——headline 31.3% 缺乏正确 baseline comparator\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 最终评估中最重要的新发现。random-split (0.18%) 是 perfect null，不代表 realistic null。随机打乱 cohort labels 1,000 次得到的 permutation null C% 才是 31.3% 的正确 baseline。如果 permutation null ~5%，effective DIF ~26%，headline 需要调整。这是升至 4.0 的硬性阻碍。R2 未独立提出但未反对。\"\n  action_items:\n    - round: 7\n      action: \"补充 1,000 次 permutation null（随机打乱 2023/2024 cohort labels），报告 null distribution mean + 95th percentile，计算 null-adjusted C%\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES (open)\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic binary flipping 的 ecological validity——uniform rate p 不反映真实 contamination patterns\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"multi-subject injection 已添加，但 binary flipping 本身是 simplification\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终评估：binary flipping 是 'perfect contamination' 简化，真实 contamination 有 partial memorization, reasoning shortcuts, format-specific advantages。ΔTPR=+0.508 at p=0.5（非 Director 所述 0.37）是 meaningful 但建立在极端 injection 上。R2 AGREE 但认为 cross-subject matching 的 ΔFPR<0.001 本身有独立价值。\"\n  action_items:\n    - round: 7\n      action: \"Limitations 中讨论 binary flipping 的简化假设和 non-uniform injection sensitivity\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"Section 5.3 GSM1K N=33 证据——已降级但仍占过多篇幅\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"已从 contribution 降为 Discussion，正确\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1+R2 共识：N=33 太弱。建议进一步压缩为 1-2 句或删除，释放空间给 practical recommendations 和 multi-subject injection 展示。\"\n  action_items:\n    - round: 7\n      action: \"压缩 Section 5.3 为 1-2 句 exploratory note，或删除\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"Practical recommendations (Section 5.4) 需要更多深度\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"仍只有 3 句话\"\n    - round: 7\n      reviewers: [1]\n      note: \"R1 指出修订版已扩展为 graduated thresholds (<15% monitor, 15-25% flag, >25% act)——有改善。但仍缺少 integration workflow 和 threshold justification。\"\n  action_items:\n    - round: 7\n      action: \"进一步扩展：threshold 选择依据、与 BHI/Growing Pains 的集成、tooling 建议\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"IRT model fit statistics 未报告——transparent reporting 要求\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 最终确认：论文未报告 |Lz| 或 CFI。MH-DIF 不依赖 IRT fit（技术正确），但 transparent reporting 要求至少呈现。如果 CFI=0.72（Director 所述），应在 Limitations 讨论。R2 同意 MH non-parametric 论点但支持报告 fit statistics。\"\n  action_items:\n    - round: 7\n      action: \"报告 MMLU 2PL model fit statistics (CFI, RMSEA, |Lz| distribution)，即使结论是 'MH-DIF 对此鲁棒'\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"Multi-subject injection 结果展示过于压缩——k∈{1,3,5,10,20} 的 ΔFPR 应以 table/figure 呈现\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1+R2 共识：这是论文回应 Round 5 核心批评的关键新增实验，但仅占 1.5 句 inline text。应以 table 或 figure 呈现，提升 prominence。\"\n  action_items:\n    - round: 7\n      action: \"将 multi-subject injection ΔFPR 数据以 table 或 figure 呈现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing——DIF and contamination measure different constructs\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 交叉回应同意 R2 观点：更准确的 framing 是 'DIF and contamination detection measure fundamentally different constructs'。论文 §4.3 ground truth mismatch 可补充 4 象限 item characteristic analysis。\"\n  action_items:\n    - round: 7\n      action: \"调整 Claim 2 framing；考虑 2×2 象限 item analysis (web-contaminated × DIF-flagged)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI resampling unit + 不对称性原因未报告\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"修订版已明确 'B=1,000 model-level resamples'（部分回应）。但 CI 不对称性原因仍未讨论。\"\n  action_items:\n    - round: 7\n      action: \"讨论 CI [29.4%, 38.1%] 不对称性的来源\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 缺乏定量对比（DIF flags vs FPC anchors）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 确认 Related Work 扩展中说 'Empirical comparison awaits public release'——合理但仍无定量数据。\"\n  action_items:\n    - round: 7\n      action: \"如 Growing Pains 数据可获取，补充 overlap 分析；否则在 Discussion 更详细讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MISSING-REF-1\"\n  summary: \"引用问题\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 确认当前版本 ~60 references，4 段 Related Work，覆盖充分。BHI, Benchmark², ATLAS, MedIRT 均已添加。Orphan entries 状态不确定。\"\n  action_items:\n    - round: 7\n      action: \"确认 orphan bib entries 已清理\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED ISSUES (abbreviated)\n# ============================================================\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N2-resolved\"\n  summary: \"Novelty 论证不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  resolution: \"LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。Novelty borderline but acceptable for empirical contribution track.\"\n  resolution_round: 6\n  mentions: []\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (LD×DIF)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50). MH non-parametric.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]. Structural guarantee.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n  mentions: []"
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
    "issues_yaml": "# Review Issues Tracker — irt_equated_bench_regen\n# Final convergence: Round 7 (2026-05-21)\n# R1 + R2 both at Overall 3.5 (Borderline Conference)\n\n# ============================================================\n# CRITICAL ISSUES (open — block upgrade to 4.0)\n# ============================================================\n\n- id: \"R1-W1\"\n  summary: \"Causal language 残余——Conclusion 中 'driven by' 等措辞暗示因果方向，数据只支持 association\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 7\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"标题 'Psychometric Instability' 过强\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"标题已改为 'Temporal Measurement Drift'（改善），但 Conclusion 仍有 causal language\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终确认 title 改善充分回应了 N2。但 causal language in body 仍需清除。R2 同意。\"\n  action_items:\n    - round: 7\n      action: \"替换 Conclusion 中 'driven by' → 'associated with'；全文检查 causal-leaning 措辞\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N1\"\n  summary: \"缺少 permutation null——headline 31.3% 缺乏正确 baseline comparator\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 最终评估中最重要的新发现。random-split (0.18%) 是 perfect null，不代表 realistic null。随机打乱 cohort labels 1,000 次得到的 permutation null C% 才是 31.3% 的正确 baseline。如果 permutation null ~5%，effective DIF ~26%，headline 需要调整。这是升至 4.0 的硬性阻碍。R2 未独立提出但未反对。\"\n  action_items:\n    - round: 7\n      action: \"补充 1,000 次 permutation null（随机打乱 2023/2024 cohort labels），报告 null distribution mean + 95th percentile，计算 null-adjusted C%\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING ISSUES (open)\n# ============================================================\n\n- id: \"R5-N1\"\n  summary: \"Semi-synthetic binary flipping 的 ecological validity——uniform rate p 不反映真实 contamination patterns\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"multi-subject injection 已添加，但 binary flipping 本身是 simplification\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 最终评估：binary flipping 是 'perfect contamination' 简化，真实 contamination 有 partial memorization, reasoning shortcuts, format-specific advantages。ΔTPR=+0.508 at p=0.5（非 Director 所述 0.37）是 meaningful 但建立在极端 injection 上。R2 AGREE 但认为 cross-subject matching 的 ΔFPR<0.001 本身有独立价值。\"\n  action_items:\n    - round: 7\n      action: \"Limitations 中讨论 binary flipping 的简化假设和 non-uniform injection sensitivity\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W2\"\n  summary: \"Section 5.3 GSM1K N=33 证据——已降级但仍占过多篇幅\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"已从 contribution 降为 Discussion，正确\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1+R2 共识：N=33 太弱。建议进一步压缩为 1-2 句或删除，释放空间给 practical recommendations 和 multi-subject injection 展示。\"\n  action_items:\n    - round: 7\n      action: \"压缩 Section 5.3 为 1-2 句 exploratory note，或删除\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"RD2-W3\"\n  summary: \"Practical recommendations (Section 5.4) 需要更多深度\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"仍只有 3 句话\"\n    - round: 7\n      reviewers: [1]\n      note: \"R1 指出修订版已扩展为 graduated thresholds (<15% monitor, 15-25% flag, >25% act)——有改善。但仍缺少 integration workflow 和 threshold justification。\"\n  action_items:\n    - round: 7\n      action: \"进一步扩展：threshold 选择依据、与 BHI/Growing Pains 的集成、tooling 建议\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"IRT model fit statistics 未报告——transparent reporting 要求\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 最终确认：论文未报告 |Lz| 或 CFI。MH-DIF 不依赖 IRT fit（技术正确），但 transparent reporting 要求至少呈现。如果 CFI=0.72（Director 所述），应在 Limitations 讨论。R2 同意 MH non-parametric 论点但支持报告 fit statistics。\"\n  action_items:\n    - round: 7\n      action: \"报告 MMLU 2PL model fit statistics (CFI, RMSEA, |Lz| distribution)，即使结论是 'MH-DIF 对此鲁棒'\"\n      assigned_to: authors\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"Multi-subject injection 结果展示过于压缩——k∈{1,3,5,10,20} 的 ΔFPR 应以 table/figure 呈现\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1+R2 共识：这是论文回应 Round 5 核心批评的关键新增实验，但仅占 1.5 句 inline text。应以 table 或 figure 呈现，提升 prominence。\"\n  action_items:\n    - round: 7\n      action: \"将 multi-subject injection ΔFPR 数据以 table 或 figure 呈现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W7\"\n  summary: \"Claim 2 framing——DIF and contamination measure different constructs\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 交叉回应同意 R2 观点：更准确的 framing 是 'DIF and contamination detection measure fundamentally different constructs'。论文 §4.3 ground truth mismatch 可补充 4 象限 item characteristic analysis。\"\n  action_items:\n    - round: 7\n      action: \"调整 Claim 2 framing；考虑 2×2 象限 item analysis (web-contaminated × DIF-flagged)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Bootstrap CI resampling unit + 不对称性原因未报告\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"修订版已明确 'B=1,000 model-level resamples'（部分回应）。但 CI 不对称性原因仍未讨论。\"\n  action_items:\n    - round: 7\n      action: \"讨论 CI [29.4%, 38.1%] 不对称性的来源\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"与 Growing Pains 缺乏定量对比（DIF flags vs FPC anchors）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"R1 确认 Related Work 扩展中说 'Empirical comparison awaits public release'——合理但仍无定量数据。\"\n  action_items:\n    - round: 7\n      action: \"如 Growing Pains 数据可获取，补充 overlap 分析；否则在 Discussion 更详细讨论\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"MISSING-REF-1\"\n  summary: \"引用问题\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 确认当前版本 ~60 references，4 段 Related Work，覆盖充分。BHI, Benchmark², ATLAS, MedIRT 均已添加。Orphan entries 状态不确定。\"\n  action_items:\n    - round: 7\n      action: \"确认 orphan bib entries 已清理\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED ISSUES (abbreviated)\n# ============================================================\n\n- id: \"RD2-W1\"\n  summary: \"Within-family ability confound\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Temporal cohort ability gap small (d=-0.17), matched C%=28.9%±0.1%.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N2-resolved\"\n  summary: \"Novelty 论证不充分\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 6\n  resolution: \"LLM-specific challenges 节 + semi-synthetic framework 升为 primary contribution。Novelty borderline but acceptable for empirical contribution track.\"\n  resolution_round: 6\n  mentions: []\n\n- id: \"R1-W4\"\n  summary: \"IRT misspecification (LD×DIF)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"LD×DIF r=0.09 (p=0.50). MH non-parametric.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W3\"\n  summary: \"ΔFPR=0.000 bootstrap CI\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Bootstrap CI=[0.000,0.000]. Structural guarantee.\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R2-N1\"\n  summary: \"幻觉引用 Tutz & Friedman\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"已移除。\"\n  resolution_round: 4\n  mentions: []\n\n- id: \"R1-W6\"\n  summary: \"多重比较校正\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"BH 校正已添加。\"\n  resolution_round: 2\n  mentions: []"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-21T17:54:09.591052+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 9135}, \"error\": \"\"}"}

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
