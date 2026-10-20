# Research conversation: 你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。 ## 核心定位 你不是在"总结论文"。你在回答：**这个研究子领域的人默认怎么做事？** - 总结 = — Part 1 of 2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-distiller-agent-skill.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/aa/aa8ffe7dce2f25d302aa.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-21T16:37:11.249Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:37:11.249Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。\n\n## 核心定位\n\n你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**\n\n- 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列）\n- 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）\n\n## 执行流程\n\n### Step 1: 论文排序\n\n按 (venue 质量 × 时间近度 × 相关度) 打分，确定精读优先级。\n\n### Step 2: Layer 1 — 逐篇精读\n\n对每篇「深度精读」论文：\n\n1. 用 WebFetch 获取原文（arXiv HTML 优先 → abstract 降级）\n2. 精读 intro + experiment sections，同时关注 **contribution statement**（通常在 intro 末段）和 **limitation / future work**（通常在 conclusion 段）\n3. 用 WebFetch 获取关键 figure 图片（至少 Figure 1 + 主结果图）做视觉分析，同时关注全部 **figure/table caption** 和 **正文对 figure/table 的引用段落**\n4. 写入 `distill_tmp/{paper_key}.yaml`，schema 如下：\n\n```yaml\npaper_key: \"{key}\"\ntitle: \"...\"\nvenue: \"{venue} {year}\"\nfull_text_available: true/false\n\nresearch:\n  baselines: [name1, name2]\n  metrics: [{name: \"X\", direction: \"higher_better\"}]\n  datasets: [{name: \"Y\", size: \"...\"}]\n  ablation_dimensions: [dim1, dim2]\n  training_recipe: {optimizer: \"...\", lr: \"...\", hardware: \"...\"}\n  method_family: \"...\"\n\npositioning:\n  core_claim: \"一句话提炼该论文的核心贡献（不是 abstract 复述）\"\n  key_results: \"关键性能数字（如 ImageNet top-1: 82.3% (+1.2%), FLOPs: 4.5G (-40%)）\"\n  limitations: [\"论文自己承认的局限 1\", \"局限 2\"]\n  relation_to_us: \"competitor\"   # competitor / foundation / complementary / orthogonal\n\nnarrative:\n  story_type: \"突破局限型/化繁为简型/规模涌现型/跨界迁移型/统一框架型\"\n  hook: \"第一段如何抓注意力\"\n  tension: \"现有方法局限如何铺垫\"\n  key_insight: \"核心洞察在哪个位置、什么方式揭示\"\n  argument_chain: \"problem → ... → validation\"\n  contribution_framing: \"贡献声明的措辞和数量\"\n  intro_structure: \"段落数和每段功能\"\n  notable_technique: \"叙事上最值得学习的技巧\"\n\nfigures:\n  figure_count: 6\n  figure1:\n    type: \"motivation\"                    # motivation / method_overview / teaser_result / problem_illustration\n    description: \"图的内容描述\"\n    narrative_role: \"在论证链中的作用\"\n    design_elements: [\"对比布局\", \"颜色标注\", \"真实样例\"]\n    visual_style: \"从图片视觉分析得到的布局/配色/标注描述\"\n  result_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"bar_chart\"              # bar_chart / line_plot / heatmap / scatter / qualitative_comparison\n      what_compared: \"对比了什么\"\n      how_gain_highlighted: \"如何突出本方法的优势\"\n      design_note: \"设计上值得借鉴的点\"\n  ablation_figures:\n    - figure_id: \"Figure 6\"\n      viz_type: \"grouped_bar\"\n      dimensions_varied: [\"component A\", \"component B\"]\n      design_note: \"消融图的设计思路\"\n  figure_narrative_role: \"Figure 1 → Figure 2 → ... 的叙事流\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"                   # methods / datasets / settings\n    col_axis: \"datasets × metrics\"\n    row_organization: \"by_category\"       # by_category / by_performance / by_year / flat\n    col_organization: \"grouped_by_dataset\" # grouped_by_dataset / grouped_by_metric / flat\n    highlight_strategy: \"bold_best + underline_second\"\n    statistical_reporting: \"mean ± std across 3 runs\"\n    num_baselines: 8\n    design_note: \"表格编排上值得借鉴的点\"\n  ablation_tables:\n    - table_id: \"Table 3\"\n      what_varied: [\"component A\", \"component B\"]\n      variation_style: \"checkmark_grid\"   # checkmark_grid / delta_from_base / full_numbers\n      design_note: \"消融表的呈现思路\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"附录表放了什么\"\n    reason: \"为什么这样拆分主表和附录\"\n```\n\n对「仅摘要」论文：只填 `research` 部分，`narrative`/`figures`/`tables` 标记 `N/A`。\n\n### Step 3: Layer 2 — 跨论文归纳\n\n读取全部 Layer 1 YAML，分两个维度归纳：\n\n**Research 归纳**：\n- 统计 baseline/metric/dataset 出现频率\n- 识别方法论趋势（上升 vs 消退）\n- 提取实验设计共识\n- 竞品 claim 汇总：从各篇的 positioning.core_claim 归纳，按 relation_to_us 分组\n- 共同局限：从各篇的 positioning.limitations 交叉比对，标注出现频率\n- 研究空白：从全部论文覆盖的维度中找出交叉盲区（多数做了 X 但没做 Y）\n\n**Writing 归纳**：\n- 对比各论文叙事结构\n- 识别领域故事类型分布\n- 归纳开篇模式、张力来源、洞察呈现位置\n- 提炼可模仿的叙事策略\n- Figure 1 设计模式分布：从各篇 `figures.figure1.type` 统计，哪种最主流，设计元素共识\n- 结果可视化共识：从 `result_figures.viz_type` 统计主结果常用图表类型，gain 突出手法\n- 消融可视化偏好：从 `ablation_figures.viz_type` 统计，grouped bar / heatmap / 表格哪种主流\n- 图的叙事节奏：从 `figure_narrative_role` 归纳典型 figure 编排（motivation → method → result → ablation）\n- 主结果表编排共识：从 `tables.main_result_table` 归纳行列组织模式、分组策略、baseline 数量范围\n- 高亮与统计报告共识：从 `highlight_strategy` + `statistical_reporting` 统计领域标准做法\n- 消融表呈现偏好：从 `ablation_tables.variation_style` 统计 checkmark grid vs delta vs 完整数字\n- 图表分工模式：从 figure + table 全局看，什么结果用图、什么用表、附录放什么\n\n### Step 4: 生成 Skill 文件\n\n在指定 skill 目录下创建两个 `.skill.md` 文件。\n\n## 质量要求\n\n每条 pattern 必须标注：\n- **支持度**：N/M 篇论文\n- **来源**：至少 1 篇代表性论文 title\n- **置信度**：高（>60%）/ 中（30-60%）/ 低（<30% 但值得注意）\n\n不要输出：\n- 单篇论文的独立总结\n- 没有跨论文共识支撑的孤立观察\n- 显而易见的常识\n\n叙事策略分析（writing skill 核心）：\n- 逐篇拆解 3-5 篇论文的故事结构（故事类型、开篇钩子、张力构建、关键洞察、论证链）\n- 每个分析点引用论文中的具体措辞或结构作为证据\n- 策略建议具体到可直接模仿，不泛泛而谈\n\n## 完成标志\n\n所有工作完成后输出 `[DISTILL_DONE]`。\n\n\n## 任务参数\n\n- 项目: gated_mfrm_judge_bias\n- Layer 1 输出目录: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/`\n- Skill 输出目录: `/home/ubuntu/.agent-ml-research-prod43/skills/projects/gated_mfrm_judge_bias/`\n- 深度精读上限: 8 篇\n- 单个 Skill 字数上限: 3000 字符\n\n## 待分析论文\n\n### 深度精读（Layer 1 完整分析）\n\n1. **Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT** (AAAI 2026)\n   paper_key: `lin2025psnirt`\n\n2. **UDA: Unsupervised Debiasing Alignment for LLM Judges** (AAAI 2026)\n   paper_key: `uda2026`\n\n3. **ConStat: Statistical Detection and Quantification of Benchmark Contamination** (NeurIPS 2024)\n   paper_key: `constat2024`\n\n4. **DCR: Quantifying Data Contamination in LLMs Evaluation** (EMNLP 2025)\n   paper_key: `dcr2025`\n\n5. **Preference Leakage: A Contamination Problem in LLM-as-a-judge** (ICLR 2026)\n   paper_key: `preference_leakage2026`\n\n6. **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena** (NeurIPS 2023)\n   paper_key: `zheng2023mtbench`\n\n7. **Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model** (arXiv 2025 | arXiv:2505.18486)\n   paper_key: `wang2025mfrm_llm`\n\n8. **CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation** (arXiv 2026)\n   paper_key: `cyclicjudge2026`\n\n\n### 仅摘要（Layer 1 research 维度）\n\n1. **Bias and Uncertainty in LLM-as-a-Judge Estimation** (arXiv 2026) — paper_key: `fiedler2026bias_uncertainty`\n2. **Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines** (arXiv 2026) — paper_key: `soumik2026judging_judges`\n3. **LogProber: Detecting Data Contamination via Token Log-Probability Analysis** (arXiv 2024) — paper_key: `logprober2024`\n4. **Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise** (Psychometrika 2013) — paper_key: `shu2013dgirt`\n\n## 执行指令\n\n1. 对每篇「深度精读」论文执行 Layer 1 分析，将结构化结果写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/{paper_key}.yaml`\n2. 对「仅摘要」论文，仅提取 research 维度（baseline/metric/dataset），写入同目录\n3. 读取全部 Layer 1 YAML（含已缓存的），执行 Layer 2 跨论文归纳\n4. 生成 `distilled-research.skill.md` 和 `distilled-writing.skill.md`，写入 `/home/ubuntu/.agent-ml-research-prod43/skills/projects/gated_mfrm_judge_bias/`\n5. 每个 skill body 不超过 3000 字符\n"
}
````

---


### Runtime record

_source line 2 · 2026-05-21T16:37:11.255Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T16:37:11.255Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


## Round 1

## Round 1

55 recorded events


### User

_source line 3 · 2026-05-21T16:37:11.342Z_

你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。

## 核心定位

你不是在"总结论文"。你在回答：**这个研究子领域的人默认怎么做事？**

- 总结 = "论文 A 做了 X，论文 B 做了 Y"（罗列）
- 蒸馏 = "这 N 篇论文共同揭示了什么同行做法和领域经验"（归纳）

## 执行流程

### Step 1: 论文排序

按 (venue 质量 × 时间近度 × 相关度) 打分，确定精读优先级。

### Step 2: Layer 1 — 逐篇精读

对每篇「深度精读」论文：

1. 用 WebFetch 获取原文（arXiv HTML 优先 → abstract 降级）
2. 精读 intro + experiment sections，同时关注 **contribution statement**（通常在 intro 末段）和 **limitation / future work**（通常在 conclusion 段）
3. 用 WebFetch 获取关键 figure 图片（至少 Figure 1 + 主结果图）做视觉分析，同时关注全部 **figure/table caption** 和 **正文对 figure/table 的引用段落**
4. 写入 `distill_tmp/{paper_key}.yaml`，schema 如下：

```yaml
paper_key: "{key}"
title: "..."
venue: "{venue} {year}"
full_text_available: true/false

research:
  baselines: [name1, name2]
  metrics: [{name: "X", direction: "higher_better"}]
  datasets: [{name: "Y", size: "..."}]
  ablation_dimensions: [dim1, dim2]
  training_recipe: {optimizer: "...", lr: "...", hardware: "..."}
  method_family: "..."

positioning:
  core_claim: "一句话提炼该论文的核心贡献（不是 abstract 复述）"
  key_results: "关键性能数字（如 ImageNet top-1: 82.3% (+1.2%), FLOPs: 4.5G (-40%)）"
  limitations: ["论文自己承认的局限 1", "局限 2"]
  relation_to_us: "competitor"   # competitor / foundation / complementary / orthogonal

narrative:
  story_type: "突破局限型/化繁为简型/规模涌现型/跨界迁移型/统一框架型"
  hook: "第一段如何抓注意力"
  tension: "现有方法局限如何铺垫"
  key_insight: "核心洞察在哪个位置、什么方式揭示"
  argument_chain: "problem → ... → validation"
  contribution_framing: "贡献声明的措辞和数量"
  intro_structure: "段落数和每段功能"
  notable_technique: "叙事上最值得学习的技巧"

figures:
  figure_count: 6
  figure1:
    type: "motivation"                    # motivation / method_overview / teaser_result / problem_illustration
    description: "图的内容描述"
    narrative_role: "在论证链中的作用"
    design_elements: ["对比布局", "颜色标注", "真实样例"]
    visual_style: "从图片视觉分析得到的布局/配色/标注描述"
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "bar_chart"              # bar_chart / line_plot / heatmap / scatter / qualitative_comparison
      what_compared: "对比了什么"
      how_gain_highlighted: "如何突出本方法的优势"
      design_note: "设计上值得借鉴的点"
  ablation_figures:
    - figure_id: "Figure 6"
      viz_type: "grouped_bar"
      dimensions_varied: ["component A", "component B"]
      design_note: "消融图的设计思路"
  figure_narrative_role: "Figure 1 → Figure 2 → ... 的叙事流"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"                   # methods / datasets / settings
    col_axis: "datasets × metrics"
    row_organization: "by_category"       # by_category / by_performance / by_year / flat
    col_organization: "grouped_by_dataset" # grouped_by_dataset / grouped_by_metric / flat
    highlight_strategy: "bold_best + underline_second"
    statistical_reporting: "mean ± std across 3 runs"
    num_baselines: 8
    design_note: "表格编排上值得借鉴的点"
  ablation_tables:
    - table_id: "Table 3"
      what_varied: ["component A", "component B"]
      variation_style: "checkmark_grid"   # checkmark_grid / delta_from_base / full_numbers
      design_note: "消融表的呈现思路"
  supplementary_tables:
    in_appendix: true
    content: "附录表放了什么"
    reason: "为什么这样拆分主表和附录"
```

对「仅摘要」论文：只填 `research` 部分，`narrative`/`figures`/`tables` 标记 `N/A`。

### Step 3: Layer 2 — 跨论文归纳

读取全部 Layer 1 YAML，分两个维度归纳：

**Research 归纳**：
- 统计 baseline/metric/dataset 出现频率
- 识别方法论趋势（上升 vs 消退）
- 提取实验设计共识
- 竞品 claim 汇总：从各篇的 positioning.core_claim 归纳，按 relation_to_us 分组
- 共同局限：从各篇的 positioning.limitations 交叉比对，标注出现频率
- 研究空白：从全部论文覆盖的维度中找出交叉盲区（多数做了 X 但没做 Y）

**Writing 归纳**：
- 对比各论文叙事结构
- 识别领域故事类型分布
- 归纳开篇模式、张力来源、洞察呈现位置
- 提炼可模仿的叙事策略
- Figure 1 设计模式分布：从各篇 `figures.figure1.type` 统计，哪种最主流，设计元素共识
- 结果可视化共识：从 `result_figures.viz_type` 统计主结果常用图表类型，gain 突出手法
- 消融可视化偏好：从 `ablation_figures.viz_type` 统计，grouped bar / heatmap / 表格哪种主流
- 图的叙事节奏：从 `figure_narrative_role` 归纳典型 figure 编排（motivation → method → result → ablation）
- 主结果表编排共识：从 `tables.main_result_table` 归纳行列组织模式、分组策略、baseline 数量范围
- 高亮与统计报告共识：从 `highlight_strategy` + `statistical_reporting` 统计领域标准做法
- 消融表呈现偏好：从 `ablation_tables.variation_style` 统计 checkmark grid vs delta vs 完整数字
- 图表分工模式：从 figure + table 全局看，什么结果用图、什么用表、附录放什么

### Step 4: 生成 Skill 文件

在指定 skill 目录下创建两个 `.skill.md` 文件。

## 质量要求

每条 pattern 必须标注：
- **支持度**：N/M 篇论文
- **来源**：至少 1 篇代表性论文 title
- **置信度**：高（>60%）/ 中（30-60%）/ 低（<30% 但值得注意）

不要输出：
- 单篇论文的独立总结
- 没有跨论文共识支撑的孤立观察
- 显而易见的常识

叙事策略分析（writing skill 核心）：
- 逐篇拆解 3-5 篇论文的故事结构（故事类型、开篇钩子、张力构建、关键洞察、论证链）
- 每个分析点引用论文中的具体措辞或结构作为证据
- 策略建议具体到可直接模仿，不泛泛而谈

## 完成标志

所有工作完成后输出 `[DISTILL_DONE]`。


## 任务参数

- 项目: gated_mfrm_judge_bias
- Layer 1 输出目录: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/`
- Skill 输出目录: `/home/ubuntu/.agent-ml-research-prod43/skills/projects/gated_mfrm_judge_bias/`
- 深度精读上限: 8 篇
- 单个 Skill 字数上限: 3000 字符

## 待分析论文

### 深度精读（Layer 1 完整分析）

1. **Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT** (AAAI 2026)
   paper_key: `lin2025psnirt`

2. **UDA: Unsupervised Debiasing Alignment for LLM Judges** (AAAI 2026)
   paper_key: `uda2026`

3. **ConStat: Statistical Detection and Quantification of Benchmark Contamination** (NeurIPS 2024)
   paper_key: `constat2024`

4. **DCR: Quantifying Data Contamination in LLMs Evaluation** (EMNLP 2025)
   paper_key: `dcr2025`

5. **Preference Leakage: A Contamination Problem in LLM-as-a-judge** (ICLR 2026)
   paper_key: `preference_leakage2026`

6. **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena** (NeurIPS 2023)
   paper_key: `zheng2023mtbench`

7. **Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model** (arXiv 2025 | arXiv:2505.18486)
   paper_key: `wang2025mfrm_llm`

8. **CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation** (arXiv 2026)
   paper_key: `cyclicjudge2026`


### 仅摘要（Layer 1 research 维度）

1. **Bias and Uncertainty in LLM-as-a-Judge Estimation** (arXiv 2026) — paper_key: `fiedler2026bias_uncertainty`
2. **Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines** (arXiv 2026) — paper_key: `soumik2026judging_judges`
3. **LogProber: Detecting Data Contamination via Token Log-Probability Analysis** (arXiv 2024) — paper_key: `logprober2024`
4. **Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise** (Psychometrika 2013) — paper_key: `shu2013dgirt`

## 执行指令

1. 对每篇「深度精读」论文执行 Layer 1 分析，将结构化结果写入 `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/{paper_key}.yaml`
2. 对「仅摘要」论文，仅提取 research 维度（baseline/metric/dataset），写入同目录
3. 读取全部 Layer 1 YAML（含已缓存的），执行 Layer 2 跨论文归纳
4. 生成 `distilled-research.skill.md` 和 `distilled-writing.skill.md`，写入 `/home/ubuntu/.agent-ml-research-prod43/skills/projects/gated_mfrm_judge_bias/`
5. 每个 skill body 不超过 3000 字符


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "6bb05bdf-6009-4812-b89d-11d379ad04d3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-21T16:37:11.341Z_

```json
{
  "parentUuid": "6bb05bdf-6009-4812-b89d-11d379ad04d3",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "2400e5cd-a2f1-48d6-b5df-5f374d7c9932",
  "timestamp": "2026-05-21T16:37:11.341Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-21T16:37:11.341Z_

```json
{
  "parentUuid": "2400e5cd-a2f1-48d6-b5df-5f374d7c9932",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "a0956898-2a51-4eb7-b527-8f6af8e06483",
  "timestamp": "2026-05-21T16:37:11.341Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-21T16:37:11.341Z_

```json
{
  "parentUuid": "a0956898-2a51-4eb7-b527-8f6af8e06483",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "24ac8965-81e6-47b3-a27b-6a46aa126676",
  "timestamp": "2026-05-21T16:37:11.341Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 7 · 2026-05-21T16:37:11.341Z_

```json
{
  "parentUuid": "24ac8965-81e6-47b3-a27b-6a46aa126676",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "af324056-e4d3-4281-af2c-61ac6aa8f7db",
  "timestamp": "2026-05-21T16:37:11.341Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Assistant

_source line 9 · 2026-05-21T16:37:15.120Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task. I need to:

1. Read and analyze 8 papers in depth (Layer 1) and 4 papers at abstract level
2. Write structured YAML for each paper
3. Do cross-paper analysis (Layer 2)
4. Generate two skill files

Let me first check the working directories and any existing files, then start fetching papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af324056-e4d3-4281-af2c-61ac6aa8f7db",
  "isSidechain": false,
  "requestId": "req_011CbG3Ln8ByQRcp7mN9A9Tz",
  "type": "assistant",
  "uuid": "3721afee-4f26-4570-b242-8bebf3d2a604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FButknVTzrFVMHY7bPYz1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17494,
      "cache_read_input_tokens": 11452,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 326,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 17494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17494
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 10 · 2026-05-21T16:37:16.173Z_

开始执行论文蒸馏任务。先检查目录状态和项目配置，然后并行获取论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3721afee-4f26-4570-b242-8bebf3d2a604",
  "isSidechain": false,
  "requestId": "req_011CbG3Ln8ByQRcp7mN9A9Tz",
  "type": "assistant",
  "uuid": "200ebc5b-6f6d-4e04-976b-c9173c5ef9c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FButknVTzrFVMHY7bPYz1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17494,
      "cache_read_input_tokens": 11452,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 326,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 17494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17494
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-21T16:37:18.097Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01613sgK8cfcKhoqDDRfAMfi`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp && ls /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-prod43/skills/projects/gated_mfrm_judge_bias/ 2>/dev/null",
  "description": "Check existing distill_tmp and skill directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "200ebc5b-6f6d-4e04-976b-c9173c5ef9c2",
  "isSidechain": false,
  "requestId": "req_011CbG3Ln8ByQRcp7mN9A9Tz",
  "type": "assistant",
  "uuid": "f6b49486-1084-4ad7-9fe1-d50e56fec97a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FButknVTzrFVMHY7bPYz1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17494,
      "cache_read_input_tokens": 11452,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 326,
          "cache_read_input_tokens": 11452,
          "cache_creation_input_tokens": 17494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17494
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "f6b49486-1084-4ad7-9fe1-d50e56fec97a",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Tool result

_source line 14 · 2026-05-21T16:37:18.298Z_

<details><summary>↩ Tool result · `toolu_01613sgK8cfcKhoqDDRfAMfi`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6b49486-1084-4ad7-9fe1-d50e56fec97a",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "45dbf64f-8717-4c9d-a90a-a16c6a09c065",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f6b49486-1084-4ad7-9fe1-d50e56fec97a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-21T16:37:32.206Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EzzmauHwGtvhoHtmYbvr33`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-prod43/skills/projects/gated_mfrm_judge_bias/",
  "description": "Create skill output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45dbf64f-8717-4c9d-a90a-a16c6a09c065",
  "isSidechain": false,
  "requestId": "req_011CbG3MHbUdinJac9Gat21z",
  "type": "assistant",
  "uuid": "bd48934d-53fd-4464-b31d-ee591c69a622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BswGCV8yrGz4ZkpP7awqaA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 28946,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 28946,
          "cache_creation_input_tokens": 343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 343
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-21T16:37:32.219Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JwNcwqGbeUArw9CUwm1M4J`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd48934d-53fd-4464-b31d-ee591c69a622",
  "isSidechain": false,
  "requestId": "req_011CbG3MHbUdinJac9Gat21z",
  "type": "assistant",
  "uuid": "ff890868-0b9c-4a5a-915b-ca338a792c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BswGCV8yrGz4ZkpP7awqaA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 28946,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 28946,
          "cache_creation_input_tokens": 343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 343
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-21T16:37:32.258Z_

<details><summary>↩ Tool result · `toolu_01EzzmauHwGtvhoHtmYbvr33`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd48934d-53fd-4464-b31d-ee591c69a622",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "e6c07c5f-2915-4398-bf49-9ea8edf958ca",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "bd48934d-53fd-4464-b31d-ee591c69a622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-21T16:37:32.261Z_

<details><summary>↩ Tool result · `toolu_01JwNcwqGbeUArw9CUwm1M4J`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff890868-0b9c-4a5a-915b-ca338a792c43",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "dbc6236d-6686-4fa5-afa8-265d41b452b6",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "ff890868-0b9c-4a5a-915b-ca338a792c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 19 · 2026-05-21T16:37:44.745Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me start fetching the papers. I'll begin with the 8 deep-read papers in parallel. Let me find the arXiv IDs for each:

1. PSN-IRT (AAAI 2026) - need to search for it
2. UDA (AAAI 2026) - need to search
3. ConStat (NeurIPS 2024) - need to search
4. DCR (EMNLP 2025) - need to search
5. Preference Leakage (ICLR 2026) - need to search
6. MT-Bench (NeurIPS 2023) - arXiv:2306.05685


7. Wang 2025 MFRM LLM - arXiv:2505.18486
8. CyclicJudge (arXiv 2026) - need to search

For the 4 abstract-only papers, I have Fiedler 2026, Soumik 2026, and LogProber 2024 to search for, while Shu 2013 DGIRT is a Psychometrika paper. I'll start fetching the ones with known arXiv IDs and search for the rest, prioritizing HTML versions where available.

I should parallelize the fetching across multiple agents to speed this up, grouping the deep-read papers into batches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbc6236d-6686-4fa5-afa8-265d41b452b6",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "44c112bf-1689-4f89-835f-9bf451761455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 20 · 2026-05-21T16:37:44.769Z_

开始并行获取论文。先抓已知 arXiv ID 的论文，同时搜索其他论文的链接。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44c112bf-1689-4f89-835f-9bf451761455",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "30600596-eb88-4209-abbc-78e8564730d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-21T16:37:51.129Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01V46oYv3iHYpqdayCFc12tH`</summary>

```json
{
  "description": "Fetch paper: wang2025mfrm_llm",
  "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from this arXiv paper: arXiv:2505.18486 \"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\"\n\nUse WebFetch to get the full paper from https://arxiv.org/html/2505.18486 \n\nExtract ALL of the following in detail:\n1. Full introduction text (every paragraph)\n2. All contribution statements\n3. Complete experiment section (datasets, baselines, metrics, results with numbers)\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work section\n7. Method details (what is the approach?)\n8. Training/implementation details\n9. Ablation studies if any\n10. The conclusion section\n\nReturn the COMPLETE extracted text, not summaries. This is for detailed analysis.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30600596-eb88-4209-abbc-78e8564730d9",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "474462e2-0648-4aa6-942b-f7e08fb8378b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-21T16:38:23.021Z_

<details><summary>↩ Tool result · `toolu_01Bb5xw2kHxdSu2uyxpA8eXK`</summary>

```text
Async agent launched successfully.
agentId: a60de764ef418ebcf (internal ID - do not mention to user. Use SendMessage with to: 'a60de764ef418ebcf' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/a60de764ef418ebcf.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "236a92fc-361b-4e09-9c7f-dc455a818d33",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "28fe883a-93d6-4c5f-83cc-e2a93722c456",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a60de764ef418ebcf",
    "description": "Fetch abstract-only papers",
    "prompt": "You are helping with a paper distillation task. For each of the following 4 papers, fetch the abstract and extract basic research information (baselines, metrics, datasets, method family). Use WebFetch for each.\n\nPaper 1: \"Bias and Uncertainty in LLM-as-a-Judge Estimation\" (arXiv 2026, key: fiedler2026bias_uncertainty)\n- Search: https://arxiv.org/search/?query=bias+uncertainty+LLM+judge+estimation&searchtype=all\n- Extract: abstract, method family, baselines mentioned, metrics, datasets\n\nPaper 2: \"Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\" (arXiv 2026, key: soumik2026judging_judges)\n- Search: https://arxiv.org/search/?query=judging+judges+bias+mitigation+LLM+judge+pipelines&searchtype=all\n- Extract: abstract, method family, baselines mentioned, metrics, datasets\n\nPaper 3: \"LogProber: Detecting Data Contamination via Token Log-Probability Analysis\" (arXiv 2024, key: logprober2024)\n- Search: https://arxiv.org/search/?query=LogProber+data+contamination+token+log+probability&searchtype=all\n- Extract: abstract, method family, baselines mentioned, metrics, datasets\n\nPaper 4: \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\" (Psychometrika 2013, key: shu2013dgirt)\n- Search: https://arxiv.org/search/?query=deterministic+gated+item+response+theory+cheating+compromise&searchtype=all\n- If not on arXiv, try: https://scholar.google.com search is not available, so try to get what you can.\n- Extract: abstract, method family, key concepts\n\nFor each paper, return the paper_key, title, venue, and all extracted information in a structured format.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/a60de764ef418ebcf.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "236a92fc-361b-4e09-9c7f-dc455a818d33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-21T16:37:51.141Z_

<details><summary>↩ Tool result · `toolu_01V46oYv3iHYpqdayCFc12tH`</summary>

```text
Async agent launched successfully.
agentId: aed1d3e555792ca7c (internal ID - do not mention to user. Use SendMessage with to: 'aed1d3e555792ca7c' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/aed1d3e555792ca7c.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "474462e2-0648-4aa6-942b-f7e08fb8378b",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "d11cda9e-7c3e-46ab-9144-476435b7aa7c",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "aed1d3e555792ca7c",
    "description": "Fetch paper: wang2025mfrm_llm",
    "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from this arXiv paper: arXiv:2505.18486 \"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\"\n\nUse WebFetch to get the full paper from https://arxiv.org/html/2505.18486 \n\nExtract ALL of the following in detail:\n1. Full introduction text (every paragraph)\n2. All contribution statements\n3. Complete experiment section (datasets, baselines, metrics, results with numbers)\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work section\n7. Method details (what is the approach?)\n8. Training/implementation details\n9. Ablation studies if any\n10. The conclusion section\n\nReturn the COMPLETE extracted text, not summaries. This is for detailed analysis.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/aed1d3e555792ca7c.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "474462e2-0648-4aa6-942b-f7e08fb8378b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-21T16:37:54.032Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SLwN3FBx4uVm1maEdfg6G3`</summary>

```json
{
  "description": "Fetch paper: zheng2023mtbench",
  "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from the MT-Bench paper: \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" (NeurIPS 2023).\n\nUse WebFetch to get the full paper from https://arxiv.org/html/2306.05685\n\nExtract ALL of the following in detail:\n1. Full introduction text (every paragraph)\n2. All contribution statements\n3. Complete experiment section (datasets, baselines, metrics, results with numbers)\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work section\n7. Method details\n8. Implementation details\n9. Ablation studies if any\n10. Conclusion section\n\nReturn the COMPLETE extracted text, not summaries.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d11cda9e-7c3e-46ab-9144-476435b7aa7c",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "60bdfdd2-1e51-4913-8423-f6c06baf8060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-21T16:37:54.037Z_

<details><summary>↩ Tool result · `toolu_01SLwN3FBx4uVm1maEdfg6G3`</summary>

```text
Async agent launched successfully.
agentId: ace90c699656f23d3 (internal ID - do not mention to user. Use SendMessage with to: 'ace90c699656f23d3' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ace90c699656f23d3.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60bdfdd2-1e51-4913-8423-f6c06baf8060",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "3771619d-a3e0-4ce0-aff6-3cb477131ce8",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ace90c699656f23d3",
    "description": "Fetch paper: zheng2023mtbench",
    "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from the MT-Bench paper: \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\" (NeurIPS 2023).\n\nUse WebFetch to get the full paper from https://arxiv.org/html/2306.05685\n\nExtract ALL of the following in detail:\n1. Full introduction text (every paragraph)\n2. All contribution statements\n3. Complete experiment section (datasets, baselines, metrics, results with numbers)\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work section\n7. Method details\n8. Implementation details\n9. Ablation studies if any\n10. Conclusion section\n\nReturn the COMPLETE extracted text, not summaries.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ace90c699656f23d3.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "60bdfdd2-1e51-4913-8423-f6c06baf8060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-21T16:37:58.905Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0186HRHtg5zTNLH6chQsgrwp`</summary>

```json
{
  "description": "Fetch paper: preference_leakage2026",
  "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"Preference Leakage: A Contamination Problem in LLM-as-a-judge\" (ICLR 2026).\n\nTry these URLs in order using WebFetch:\n1. First search: https://arxiv.org/search/?query=preference+leakage+contamination+LLM+judge&searchtype=all\n2. The paper is likely arXiv:2502.01534 or similar. Try https://arxiv.org/html/2502.01534\n3. If not found, try https://arxiv.org/abs/2502.01534\n\nExtract ALL of the following in detail:\n1. Full introduction text (every paragraph)\n2. All contribution statements  \n3. Complete experiment section (datasets, baselines, metrics, results with numbers)\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work section\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn the COMPLETE extracted text, not summaries.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3771619d-a3e0-4ce0-aff6-3cb477131ce8",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "087fa4bc-b23a-4904-b607-152c155ca32b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-21T16:37:58.949Z_

<details><summary>↩ Tool result · `toolu_0186HRHtg5zTNLH6chQsgrwp`</summary>

```text
Async agent launched successfully.
agentId: ade7e6bb7f61dc1fb (internal ID - do not mention to user. Use SendMessage with to: 'ade7e6bb7f61dc1fb' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ade7e6bb7f61dc1fb.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "087fa4bc-b23a-4904-b607-152c155ca32b",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "b8eec1d6-7bba-48c5-a455-9cab509c51cc",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ade7e6bb7f61dc1fb",
    "description": "Fetch paper: preference_leakage2026",
    "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"Preference Leakage: A Contamination Problem in LLM-as-a-judge\" (ICLR 2026).\n\nTry these URLs in order using WebFetch:\n1. First search: https://arxiv.org/search/?query=preference+leakage+contamination+LLM+judge&searchtype=all\n2. The paper is likely arXiv:2502.01534 or similar. Try https://arxiv.org/html/2502.01534\n3. If not found, try https://arxiv.org/abs/2502.01534\n\nExtract ALL of the following in detail:\n1. Full introduction text (every paragraph)\n2. All contribution statements  \n3. Complete experiment section (datasets, baselines, metrics, results with numbers)\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work section\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn the COMPLETE extracted text, not summaries.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ade7e6bb7f61dc1fb.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "087fa4bc-b23a-4904-b607-152c155ca32b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-21T16:38:01.836Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015rpQr8sYtDbCzWni2DFwZy`</summary>

```json
{
  "description": "Fetch paper: lin2025psnirt",
  "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT\" (AAAI 2026).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=PSN-IRT+LLM+benchmarking+rethinking&searchtype=all\n2. Also try: https://arxiv.org/search/?query=lost+in+benchmarks+rethinking+LLM+IRT&searchtype=all\n3. If you find an arXiv ID, fetch the HTML version at https://arxiv.org/html/{id}\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section (datasets, baselines, metrics, results)\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details (PSN-IRT model)\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8eec1d6-7bba-48c5-a455-9cab509c51cc",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "3d5809b0-f89c-4b45-a908-a5db14649b24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-21T16:38:01.841Z_

<details><summary>↩ Tool result · `toolu_015rpQr8sYtDbCzWni2DFwZy`</summary>

```text
Async agent launched successfully.
agentId: ad50cdb495cf40e2d (internal ID - do not mention to user. Use SendMessage with to: 'ad50cdb495cf40e2d' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ad50cdb495cf40e2d.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d5809b0-f89c-4b45-a908-a5db14649b24",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "2148f25f-21e2-4988-abbe-e4c7509b3237",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ad50cdb495cf40e2d",
    "description": "Fetch paper: lin2025psnirt",
    "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT\" (AAAI 2026).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=PSN-IRT+LLM+benchmarking+rethinking&searchtype=all\n2. Also try: https://arxiv.org/search/?query=lost+in+benchmarks+rethinking+LLM+IRT&searchtype=all\n3. If you find an arXiv ID, fetch the HTML version at https://arxiv.org/html/{id}\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section (datasets, baselines, metrics, results)\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details (PSN-IRT model)\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ad50cdb495cf40e2d.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "3d5809b0-f89c-4b45-a908-a5db14649b24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-21T16:38:05.249Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HoxHzZXUiBZEkuXXspdrAk`</summary>

```json
{
  "description": "Fetch paper: uda2026",
  "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"UDA: Unsupervised Debiasing Alignment for LLM Judges\" (AAAI 2026).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=UDA+unsupervised+debiasing+alignment+LLM+judges&searchtype=all\n2. Also try: https://arxiv.org/search/?query=unsupervised+debiasing+LLM+judge&searchtype=all\n3. If you find an arXiv ID, fetch the HTML version at https://arxiv.org/html/{id}\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2148f25f-21e2-4988-abbe-e4c7509b3237",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "43291bc0-4e48-4792-876d-38b8659efeb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-21T16:38:05.257Z_

<details><summary>↩ Tool result · `toolu_01HoxHzZXUiBZEkuXXspdrAk`</summary>

```text
Async agent launched successfully.
agentId: acc96dbc5ca49441b (internal ID - do not mention to user. Use SendMessage with to: 'acc96dbc5ca49441b' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/acc96dbc5ca49441b.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43291bc0-4e48-4792-876d-38b8659efeb2",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "1ed1b967-5327-4dae-b2cd-7e0dd36b5918",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "acc96dbc5ca49441b",
    "description": "Fetch paper: uda2026",
    "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"UDA: Unsupervised Debiasing Alignment for LLM Judges\" (AAAI 2026).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=UDA+unsupervised+debiasing+alignment+LLM+judges&searchtype=all\n2. Also try: https://arxiv.org/search/?query=unsupervised+debiasing+LLM+judge&searchtype=all\n3. If you find an arXiv ID, fetch the HTML version at https://arxiv.org/html/{id}\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/acc96dbc5ca49441b.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "43291bc0-4e48-4792-876d-38b8659efeb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-21T16:38:08.538Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FPAC744tBXYtaLwHwZcLAq`</summary>

```json
{
  "description": "Fetch paper: constat2024",
  "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"ConStat: Statistical Detection and Quantification of Benchmark Contamination\" (NeurIPS 2024).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=ConStat+benchmark+contamination+statistical+detection&searchtype=all\n2. The paper might be arXiv:2405.15074 or similar. Try https://arxiv.org/html/2405.15074\n3. If not, search: https://arxiv.org/search/?query=ConStat+contamination+quantification&searchtype=all\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ed1b967-5327-4dae-b2cd-7e0dd36b5918",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "2a0c2557-57cf-49ec-a164-7deecec21b0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-21T16:38:08.545Z_

<details><summary>↩ Tool result · `toolu_01FPAC744tBXYtaLwHwZcLAq`</summary>

```text
Async agent launched successfully.
agentId: ad6c7c3b8b3db9ea2 (internal ID - do not mention to user. Use SendMessage with to: 'ad6c7c3b8b3db9ea2' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ad6c7c3b8b3db9ea2.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a0c2557-57cf-49ec-a164-7deecec21b0d",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "55e7192d-09fd-4bfe-8b37-75465421a1a0",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ad6c7c3b8b3db9ea2",
    "description": "Fetch paper: constat2024",
    "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"ConStat: Statistical Detection and Quantification of Benchmark Contamination\" (NeurIPS 2024).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=ConStat+benchmark+contamination+statistical+detection&searchtype=all\n2. The paper might be arXiv:2405.15074 or similar. Try https://arxiv.org/html/2405.15074\n3. If not, search: https://arxiv.org/search/?query=ConStat+contamination+quantification&searchtype=all\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ad6c7c3b8b3db9ea2.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "2a0c2557-57cf-49ec-a164-7deecec21b0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-21T16:38:11.083Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015QLhtD8LuKgY62TNnN5QMd`</summary>

```json
{
  "description": "Fetch paper: dcr2025",
  "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"DCR: Quantifying Data Contamination in LLMs Evaluation\" (EMNLP 2025).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=DCR+quantifying+data+contamination+LLM+evaluation&searchtype=all\n2. Also try: https://arxiv.org/search/?query=data+contamination+ratio+LLM+evaluation&searchtype=all\n3. If you find an arXiv ID, fetch https://arxiv.org/html/{id}\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55e7192d-09fd-4bfe-8b37-75465421a1a0",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "b239a748-86cf-4ec1-8863-ddf54102c9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-21T16:38:11.087Z_

<details><summary>↩ Tool result · `toolu_015QLhtD8LuKgY62TNnN5QMd`</summary>

```text
Async agent launched successfully.
agentId: ae9d200dd8420563b (internal ID - do not mention to user. Use SendMessage with to: 'ae9d200dd8420563b' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ae9d200dd8420563b.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b239a748-86cf-4ec1-8863-ddf54102c9dd",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "60111535-157b-447f-ba32-d0bddcccce06",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "ae9d200dd8420563b",
    "description": "Fetch paper: dcr2025",
    "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"DCR: Quantifying Data Contamination in LLMs Evaluation\" (EMNLP 2025).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=DCR+quantifying+data+contamination+LLM+evaluation&searchtype=all\n2. Also try: https://arxiv.org/search/?query=data+contamination+ratio+LLM+evaluation&searchtype=all\n3. If you find an arXiv ID, fetch https://arxiv.org/html/{id}\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ae9d200dd8420563b.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "b239a748-86cf-4ec1-8863-ddf54102c9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-21T16:38:13.931Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FnCSPe7dcAgNywdUD8bfxY`</summary>

```json
{
  "description": "Fetch paper: cyclicjudge2026",
  "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\" (arXiv 2026).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=CyclicJudge+mitigating+judge+bias+LLM&searchtype=all\n2. Also try: https://arxiv.org/search/?query=CyclicJudge+bias+evaluation&searchtype=all\n3. If you find an arXiv ID, fetch https://arxiv.org/html/{id}\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60111535-157b-447f-ba32-d0bddcccce06",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "f3f2b15b-ec33-49b5-b733-b4084f44d3c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-21T16:38:13.937Z_

<details><summary>↩ Tool result · `toolu_01FnCSPe7dcAgNywdUD8bfxY`</summary>

```text
Async agent launched successfully.
agentId: a744e5363d82fb6b7 (internal ID - do not mention to user. Use SendMessage with to: 'a744e5363d82fb6b7' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/a744e5363d82fb6b7.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3f2b15b-ec33-49b5-b733-b4084f44d3c1",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "4fc0bf5e-9040-4e8f-8248-3d4878b60b65",
  "toolUseResult": {
    "isAsync": true,
    "status": "async_launched",
    "agentId": "a744e5363d82fb6b7",
    "description": "Fetch paper: cyclicjudge2026",
    "prompt": "You are helping with a paper distillation task. Fetch and extract detailed information from \"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\" (arXiv 2026).\n\nTry these URLs using WebFetch:\n1. Search: https://arxiv.org/search/?query=CyclicJudge+mitigating+judge+bias+LLM&searchtype=all\n2. Also try: https://arxiv.org/search/?query=CyclicJudge+bias+evaluation&searchtype=all\n3. If you find an arXiv ID, fetch https://arxiv.org/html/{id}\n\nExtract ALL of the following in detail:\n1. Full introduction text\n2. All contribution statements\n3. Complete experiment section\n4. All figure and table captions\n5. Paragraphs referencing figures/tables\n6. Limitations / future work\n7. Method details\n8. Implementation details\n9. Ablation studies\n10. Conclusion\n\nReturn COMPLETE extracted text, not summaries.",
    "outputFile": "/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/a744e5363d82fb6b7.output",
    "canReadOutputFile": true
  },
  "sourceToolAssistantUUID": "f3f2b15b-ec33-49b5-b733-b4084f44d3c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-21T16:38:23.014Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Bb5xw2kHxdSu2uyxpA8eXK`</summary>

```json
{
  "description": "Fetch abstract-only papers",
  "prompt": "You are helping with a paper distillation task. For each of the following 4 papers, fetch the abstract and extract basic research information (baselines, metrics, datasets, method family). Use WebFetch for each.\n\nPaper 1: \"Bias and Uncertainty in LLM-as-a-Judge Estimation\" (arXiv 2026, key: fiedler2026bias_uncertainty)\n- Search: https://arxiv.org/search/?query=bias+uncertainty+LLM+judge+estimation&searchtype=all\n- Extract: abstract, method family, baselines mentioned, metrics, datasets\n\nPaper 2: \"Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\" (arXiv 2026, key: soumik2026judging_judges)\n- Search: https://arxiv.org/search/?query=judging+judges+bias+mitigation+LLM+judge+pipelines&searchtype=all\n- Extract: abstract, method family, baselines mentioned, metrics, datasets\n\nPaper 3: \"LogProber: Detecting Data Contamination via Token Log-Probability Analysis\" (arXiv 2024, key: logprober2024)\n- Search: https://arxiv.org/search/?query=LogProber+data+contamination+token+log+probability&searchtype=all\n- Extract: abstract, method family, baselines mentioned, metrics, datasets\n\nPaper 4: \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\" (Psychometrika 2013, key: shu2013dgirt)\n- Search: https://arxiv.org/search/?query=deterministic+gated+item+response+theory+cheating+compromise&searchtype=all\n- If not on arXiv, try: https://scholar.google.com search is not available, so try to get what you can.\n- Extract: abstract, method family, key concepts\n\nFor each paper, return the paper_key, title, venue, and all extracted information in a structured format.",
  "model": "sonnet",
  "run_in_background": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fc0bf5e-9040-4e8f-8248-3d4878b60b65",
  "isSidechain": false,
  "requestId": "req_011CbG3NKLvXnG91RTk1VpDv",
  "type": "assistant",
  "uuid": "236a92fc-361b-4e09-9c7f-dc455a818d33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015B8ssL2gUatkPtppmwvz8v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 29289,
      "output_tokens": 3743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3743,
          "cache_read_input_tokens": 29289,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 39 · 2026-05-21T16:38:23.097Z_

```json
{
  "parentUuid": "28fe883a-93d6-4c5f-83cc-e2a93722c456",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "de253c64-1184-415a-9d2b-ffa8973eac56",
  "timestamp": "2026-05-21T16:38:23.097Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "de253c64-1184-415a-9d2b-ffa8973eac56",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Assistant

_source line 42 · 2026-05-21T16:38:26.441Z_

<details><summary>Logged reasoning block</summary>

```text
All 9 agents are running in the background. Let me wait for them to complete. I'll be notified when each one finishes. In the meantime, let me read the project config to understand the research context better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de253c64-1184-415a-9d2b-ffa8973eac56",
  "isSidechain": false,
  "requestId": "req_011CbG3S4iTw2KVKD596Mw7m",
  "type": "assistant",
  "uuid": "502dff13-580e-4b69-855d-19fdcb0660b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUsGRwpWSjWVw1TS6wjygK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6441,
      "cache_read_input_tokens": 30018,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 224,
          "cache_read_input_tokens": 30018,
          "cache_creation_input_tokens": 6441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6441
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 43 · 2026-05-21T16:38:28.768Z_

9 个子 agent 已并行启动，正在获取 12 篇论文。等待返回结果后开始 Layer 1 分析。

同时读取项目配置了解研究背景。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "502dff13-580e-4b69-855d-19fdcb0660b4",
  "isSidechain": false,
  "requestId": "req_011CbG3S4iTw2KVKD596Mw7m",
  "type": "assistant",
  "uuid": "1617f215-4f1d-4a72-a547-4fbd4aa71a7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUsGRwpWSjWVw1TS6wjygK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6441,
      "cache_read_input_tokens": 30018,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 224,
          "cache_read_input_tokens": 30018,
          "cache_creation_input_tokens": 6441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6441
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-21T16:38:29.952Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RApNsMrZs52tkNa8Ltji5j`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1617f215-4f1d-4a72-a547-4fbd4aa71a7e",
  "isSidechain": false,
  "requestId": "req_011CbG3S4iTw2KVKD596Mw7m",
  "type": "assistant",
  "uuid": "9f261be9-ec1b-46fa-ae28-21dc721072fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUsGRwpWSjWVw1TS6wjygK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6441,
      "cache_read_input_tokens": 30018,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 224,
          "cache_read_input_tokens": 30018,
          "cache_creation_input_tokens": 6441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6441
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-21T16:38:29.956Z_

<details><summary>↩ Tool result · `toolu_01RApNsMrZs52tkNa8Ltji5j`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__load_project_config"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f261be9-ec1b-46fa-ae28-21dc721072fb",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "15551a49-c195-4567-a8b8-bac65fa027d1",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "9f261be9-ec1b-46fa-ae28-21dc721072fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-21T16:38:32.958Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config · `toolu_01FNPyp3JarJRcMqrGQnU8qj`</summary>

```json
{
  "project_name": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15551a49-c195-4567-a8b8-bac65fa027d1",
  "isSidechain": false,
  "requestId": "req_011CbG3SaCkTpPCPvijX9Hk4",
  "type": "assistant",
  "uuid": "167d00f1-280c-4c56-8f9d-6e17743b3c2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VA7vjvrjCebfdu4o4uiLp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 36459,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 36459,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-21T16:38:32.978Z_

<details><summary>↩ Tool result · `toolu_01FNPyp3JarJRcMqrGQnU8qj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"project\": \"gated_mfrm_judge_bias\", \"config\": {\"execution\": {}, \"feishu\": {\"chat_id\": \"oc_0cbc280bd5cb8937b8ac82690c3c5283\", \"operational_chat_id\": \"oc_e4bb57c5f85f0fbc68afd480bd764937\"}, \"project\": {\"created_at\": \"2026-05-21T16:30:07.913Z\", \"description\": \"Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation\", \"name\": \"gated_mfrm_judge_bias\", \"phase\": \"mvp\", \"source_idea_id\": \"idea_043\"}, \"venue\": \"emnlp-2026\"}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "167d00f1-280c-4c56-8f9d-6e17743b3c2c",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "028ee64a-096c-4f6c-88f1-e4e007cc5a6e",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"project\\\": \\\"gated_mfrm_judge_bias\\\", \\\"config\\\": {\\\"execution\\\": {}, \\\"feishu\\\": {\\\"chat_id\\\": \\\"oc_0cbc280bd5cb8937b8ac82690c3c5283\\\", \\\"operational_chat_id\\\": \\\"oc_e4bb57c5f85f0fbc68afd480bd764937\\\"}, \\\"project\\\": {\\\"created_at\\\": \\\"2026-05-21T16:30:07.913Z\\\", \\\"description\\\": \\\"Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation\\\", \\\"name\\\": \\\"gated_mfrm_judge_bias\\\", \\\"phase\\\": \\\"mvp\\\", \\\"source_idea_id\\\": \\\"idea_043\\\"}, \\\"venue\\\": \\\"emnlp-2026\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"project\": \"gated_mfrm_judge_bias\", \"config\": {\"execution\": {}, \"feishu\": {\"chat_id\": \"oc_0cbc280bd5cb8937b8ac82690c3c5283\", \"operational_chat_id\": \"oc_e4bb57c5f85f0fbc68afd480bd764937\"}, \"project\": {\"created_at\": \"2026-05-21T16:30:07.913Z\", \"description\": \"Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation\", \"name\": \"gated_mfrm_judge_bias\", \"phase\": \"mvp\", \"source_idea_id\": \"idea_043\"}, \"venue\": \"emnlp-2026\"}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "167d00f1-280c-4c56-8f9d-6e17743b3c2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-21T16:38:33.514Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KWgJkk3rbrXUSer9k2sNBs`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "028ee64a-096c-4f6c-88f1-e4e007cc5a6e",
  "isSidechain": false,
  "requestId": "req_011CbG3SaCkTpPCPvijX9Hk4",
  "type": "assistant",
  "uuid": "1391a672-9b37-4992-bef2-3fb6c53e4043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VA7vjvrjCebfdu4o4uiLp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 36459,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 36459,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-21T16:38:33.541Z_

<details><summary>↩ Tool result · `toolu_01KWgJkk3rbrXUSer9k2sNBs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/ROADMAP.md\", \"content\": \"# gated_mfrm_judge_bias — Research Dashboard\\n\\n> 最后更新: 2026-05-21 16:36 UTC | 更新原因: Reviewer warning: 量化 pass/fail 标准、明确 sequential baseline、增加重复次数\\n\\n## 核心方向\\nJoint psychometric model (G-MFRM) 统一校正 LLM 评测中的 judge bias 和 contamination，核心主张：sequential 方法中 judge severity 与 contamination 存在 confounding，joint estimation 是方法论必要（非 nice-to-have）。详见 paper_framing.md（待创建）。\\n\\n## 当前进展\\n- **阶段**: MVP 验证\\n- Agent 已收到 MVP 代码编写任务，正在实现\\n- 文献图谱已填充 12 篇（可触发 /distill）\\n- 服务器和执行环境未配置，等用户提供\\n\\n## MVP 验证方案\\n**假设**: 当 d_j 与 c_n·e_i 存在 confounding（ρ>0）时，joint G-MFRM 对 θ_true 的恢复精度显著优于 sequential pipeline。\\n\\n**方法**: 合成数据恢复实验\\n- 从已知参数的 G-MFRM 生成数据（N=20, I=100, J=5）\\n- 控制 confounding 程度（ρ = 0.0, 0.3, 0.6）\\n- 对比: raw average / MFRM-only / sequential / joint G-MFRM\\n- NumPyro MCMC，≥20 次独立重复（不同 random seeds）\\n\\n**Sequential baseline 定义**: 两阶段——先拟合标准 3-facet MFRM（θ, b, d），再用 Stage 1 残差 r_ni 对已知 e_i 做加权回归得到 ĉ_n，最终 θ̂_adj = θ̂_mfrm − ĉ_n · ē（用 ĉ_n 的平均暴露效应调整 ability）。\\n\\n**量化 Pass/Fail 标准**:\\n1. **收敛**: 所有拟合的 max R̂ < 1.05，min ESS > 100\\n2. **ρ>0 改善**: ρ=0.3 和 ρ=0.6 时，Joint θ-RMSE 显著低于 Sequential（paired Wilcoxon signed-rank p<0.05，≥20 repetitions）\\n3. **ρ=0 无退化**: ρ=0 时，Joint θ-RMSE 不显著高于 Sequential（Wilcoxon p>0.05）\\n4. **边界**: ρ=0.6 通过 + ρ=0.3 未通过 = conditional pass（需后续 sensitivity 验证）\\n5. **辅助**: 同时报告 Kendall-τ 提升幅度\\n\\n## 近期任务\\n- [ ] 配置执行服务器（需用户提供）\\n- [ ] Agent 完成 MVP 代码（合成数据生成 + 四种拟合 + 评估）\\n- [ ] 运行 MVP，判断 pass/fail\\n- [ ] MVP 通过后：paper_framing.md + experiment_plan.yaml\\n\\n## GPU 预算\\nMVP 不需要 GPU（NumPyro CPU MCMC）。\\nResearch 阶段预估：180-250 GPU·h + ~$900 proprietary judge API。\\n\\n## 目标会议\\n- AAAI 2027: July 28, 2026（~68 天）\\n- ACL 2027 ARR: August 3, 2026（~74 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D001 | 2026-05-21 | MVP 采用合成数据恢复实验验证 joint estimation 优势 | — |\\n\\n\\n\", \"total_chars\": 1749, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1391a672-9b37-4992-bef2-3fb6c53e4043",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "700756f4-b7ee-4859-b3c4-26ddc976b0cb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/ROADMAP.md\\\", \\\"content\\\": \\\"# gated_mfrm_judge_bias — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-21 16:36 UTC | 更新原因: Reviewer warning: 量化 pass/fail 标准、明确 sequential baseline、增加重复次数\\\\n\\\\n## 核心方向\\\\nJoint psychometric model (G-MFRM) 统一校正 LLM 评测中的 judge bias 和 contamination，核心主张：sequential 方法中 judge severity 与 contamination 存在 confounding，joint estimation 是方法论必要（非 nice-to-have）。详见 paper_framing.md（待创建）。\\\\n\\\\n## 当前进展\\\\n- **阶段**: MVP 验证\\\\n- Agent 已收到 MVP 代码编写任务，正在实现\\\\n- 文献图谱已填充 12 篇（可触发 /distill）\\\\n- 服务器和执行环境未配置，等用户提供\\\\n\\\\n## MVP 验证方案\\\\n**假设**: 当 d_j 与 c_n·e_i 存在 confounding（ρ>0）时，joint G-MFRM 对 θ_true 的恢复精度显著优于 sequential pipeline。\\\\n\\\\n**方法**: 合成数据恢复实验\\\\n- 从已知参数的 G-MFRM 生成数据（N=20, I=100, J=5）\\\\n- 控制 confounding 程度（ρ = 0.0, 0.3, 0.6）\\\\n- 对比: raw average / MFRM-only / sequential / joint G-MFRM\\\\n- NumPyro MCMC，≥20 次独立重复（不同 random seeds）\\\\n\\\\n**Sequential baseline 定义**: 两阶段——先拟合标准 3-facet MFRM（θ, b, d），再用 Stage 1 残差 r_ni 对已知 e_i 做加权回归得到 ĉ_n，最终 θ̂_adj = θ̂_mfrm − ĉ_n · ē（用 ĉ_n 的平均暴露效应调整 ability）。\\\\n\\\\n**量化 Pass/Fail 标准**:\\\\n1. **收敛**: 所有拟合的 max R̂ < 1.05，min ESS > 100\\\\n2. **ρ>0 改善**: ρ=0.3 和 ρ=0.6 时，Joint θ-RMSE 显著低于 Sequential（paired Wilcoxon signed-rank p<0.05，≥20 repetitions）\\\\n3. **ρ=0 无退化**: ρ=0 时，Joint θ-RMSE 不显著高于 Sequential（Wilcoxon p>0.05）\\\\n4. **边界**: ρ=0.6 通过 + ρ=0.3 未通过 = conditional pass（需后续 sensitivity 验证）\\\\n5. **辅助**: 同时报告 Kendall-τ 提升幅度\\\\n\\\\n## 近期任务\\\\n- [ ] 配置执行服务器（需用户提供）\\\\n- [ ] Agent 完成 MVP 代码（合成数据生成 + 四种拟合 + 评估）\\\\n- [ ] 运行 MVP，判断 pass/fail\\\\n- [ ] MVP 通过后：paper_framing.md + experiment_plan.yaml\\\\n\\\\n## GPU 预算\\\\nMVP 不需要 GPU（NumPyro CPU MCMC）。\\\\nResearch 阶段预估：180-250 GPU·h + ~$900 proprietary judge API。\\\\n\\\\n## 目标会议\\\\n- AAAI 2027: July 28, 2026（~68 天）\\\\n- ACL 2027 ARR: August 3, 2026（~74 天）\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D001 | 2026-05-21 | MVP 采用合成数据恢复实验验证 joint estimation 优势 | — |\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 1749, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/ROADMAP.md\", \"content\": \"# gated_mfrm_judge_bias — Research Dashboard\\n\\n> 最后更新: 2026-05-21 16:36 UTC | 更新原因: Reviewer warning: 量化 pass/fail 标准、明确 sequential baseline、增加重复次数\\n\\n## 核心方向\\nJoint psychometric model (G-MFRM) 统一校正 LLM 评测中的 judge bias 和 contamination，核心主张：sequential 方法中 judge severity 与 contamination 存在 confounding，joint estimation 是方法论必要（非 nice-to-have）。详见 paper_framing.md（待创建）。\\n\\n## 当前进展\\n- **阶段**: MVP 验证\\n- Agent 已收到 MVP 代码编写任务，正在实现\\n- 文献图谱已填充 12 篇（可触发 /distill）\\n- 服务器和执行环境未配置，等用户提供\\n\\n## MVP 验证方案\\n**假设**: 当 d_j 与 c_n·e_i 存在 confounding（ρ>0）时，joint G-MFRM 对 θ_true 的恢复精度显著优于 sequential pipeline。\\n\\n**方法**: 合成数据恢复实验\\n- 从已知参数的 G-MFRM 生成数据（N=20, I=100, J=5）\\n- 控制 confounding 程度（ρ = 0.0, 0.3, 0.6）\\n- 对比: raw average / MFRM-only / sequential / joint G-MFRM\\n- NumPyro MCMC，≥20 次独立重复（不同 random seeds）\\n\\n**Sequential baseline 定义**: 两阶段——先拟合标准 3-facet MFRM（θ, b, d），再用 Stage 1 残差 r_ni 对已知 e_i 做加权回归得到 ĉ_n，最终 θ̂_adj = θ̂_mfrm − ĉ_n · ē（用 ĉ_n 的平均暴露效应调整 ability）。\\n\\n**量化 Pass/Fail 标准**:\\n1. **收敛**: 所有拟合的 max R̂ < 1.05，min ESS > 100\\n2. **ρ>0 改善**: ρ=0.3 和 ρ=0.6 时，Joint θ-RMSE 显著低于 Sequential（paired Wilcoxon signed-rank p<0.05，≥20 repetitions）\\n3. **ρ=0 无退化**: ρ=0 时，Joint θ-RMSE 不显著高于 Sequential（Wilcoxon p>0.05）\\n4. **边界**: ρ=0.6 通过 + ρ=0.3 未通过 = conditional pass（需后续 sensitivity 验证）\\n5. **辅助**: 同时报告 Kendall-τ 提升幅度\\n\\n## 近期任务\\n- [ ] 配置执行服务器（需用户提供）\\n- [ ] Agent 完成 MVP 代码（合成数据生成 + 四种拟合 + 评估）\\n- [ ] 运行 MVP，判断 pass/fail\\n- [ ] MVP 通过后：paper_framing.md + experiment_plan.yaml\\n\\n## GPU 预算\\nMVP 不需要 GPU（NumPyro CPU MCMC）。\\nResearch 阶段预估：180-250 GPU·h + ~$900 proprietary judge API。\\n\\n## 目标会议\\n- AAAI 2027: July 28, 2026（~68 天）\\n- ACL 2027 ARR: August 3, 2026（~74 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D001 | 2026-05-21 | MVP 采用合成数据恢复实验验证 joint estimation 优势 | — |\\n\\n\\n\", \"total_chars\": 1749, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1391a672-9b37-4992-bef2-3fb6c53e4043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-21T16:38:33.832Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WtL1qxzkGpfshqYJqjNunn`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "700756f4-b7ee-4859-b3c4-26ddc976b0cb",
  "isSidechain": false,
  "requestId": "req_011CbG3SaCkTpPCPvijX9Hk4",
  "type": "assistant",
  "uuid": "4002cfea-100d-45ec-b33c-ee50dd1a0eec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019VA7vjvrjCebfdu4o4uiLp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 36459,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 36459,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-21T16:38:33.863Z_

<details><summary>↩ Tool result · `toolu_01WtL1qxzkGpfshqYJqjNunn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-21T16:40:00Z\\\"\\n  total_papers: 12\\ncategories:\\n  - key: \\\"psychometric_foundation\\\"\\n    name: \\\"Psychometric & IRT Foundation\\\"\\n    narrative: \\\"Core psychometric models: DG-IRT gating mechanism for cheating detection, MFRM applied to LLM raters, and IRT-based LLM evaluation frameworks\\\"\\n  - key: \\\"judge_bias_correction\\\"\\n    name: \\\"Judge Bias Correction\\\"\\n    narrative: \\\"Methods for detecting and correcting systematic biases in LLM-as-a-judge evaluation pipelines\\\"\\n  - key: \\\"contamination_detection\\\"\\n    name: \\\"Contamination Detection & Adjustment\\\"\\n    narrative: \\\"Methods for detecting and quantifying benchmark contamination in LLM evaluation\\\"\\n  - key: \\\"unified_evaluation\\\"\\n    name: \\\"Unified Evaluation Frameworks\\\"\\n    narrative: \\\"Comprehensive LLM evaluation frameworks and benchmarks that combine multiple assessment dimensions\\\"\\npapers:\\n  shu2013dgirt:\\n    title: \\\"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\\\"\\n    authors:\\n      - \\\"Shu, Z.\\\"\\n      - \\\"Henson, R.\\\"\\n      - \\\"Luecht, R.\\\"\\n    year: 2013\\n    venue: \\\"Psychometrika\\\"\\n    doi: \\\"10.1007/s11336-012-9311-3\\\"\\n    bibtex_key: \\\"shu2013dgirt\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Core methodological inspiration. DG-IRT decomposes observed performance into genuine ability and cheating-inflated components via a gating mechanism. G-MFRM adapts this gating logic from educational cheating to LLM benchmark contamination.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  wang2025mfrm_llm:\\n    title: \\\"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\\\"\\n    authors:\\n      - \\\"Wang, Y.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2505.18486\\\"\\n    bibtex_key: \\\"wang2025mfrm_llm\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Most direct predecessor. Applies MFRM to compare 10 LLM raters with human experts, demonstrating MFRM's applicability to LLM judge calibration. Does NOT model contamination — the gap G-MFRM fills.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  lin2025psnirt:\\n    title: \\\"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT\\\"\\n    authors:\\n      - \\\"Lin, Z.\\\"\\n    year: 2026\\n    venue: \\\"AAAI\\\"\\n    bibtex_key: \\\"lin2025psnirt\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Neural 4PL IRT for LLM benchmark evaluation. Demonstrates scalability of IRT to LLMs but lacks judge facet and contamination modeling. Serves as IRT-based baseline without multi-facet structure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  cyclicjudge2026:\\n    title: \\\"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    bibtex_key: \\\"cyclicjudge2026\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Primary bias-only baseline. Eliminates judge bias via round-robin assignment but completely ignores contamination. G-MFRM addresses both jointly.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  fiedler2026bias_uncertainty:\\n    title: \\\"Bias and Uncertainty in LLM-as-a-Judge Estimation\\\"\\n    authors:\\n      - \\\"Fiedler, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2605.06939\\\"\\n    bibtex_key: \\\"fiedler2026bias_uncertainty\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Introduces formal J/delta-J diagnostics for judge bias, identifies sign-reversal failure modes in shared-calibration comparisons. Stays within classical test theory. G-MFRM's confounding argument positions Fiedler's sign-reversal as downstream consequence of unmodeled contamination.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  soumik2026judging_judges:\\n    title: \\\"Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\\\"\\n    authors:\\n      - \\\"Soumik, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2604.23178\\\"\\n    bibtex_key: \\\"soumik2026judging_judges\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Empirically compares 9 debiasing strategies across 5 judges, finding style bias dominant (0.76-0.92). Provides no measurement model explaining why strategies work — G-MFRM provides the explanatory framework.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  uda2026:\\n    title: \\\"UDA: Unsupervised Debiasing Alignment for LLM Judges\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"AAAI\\\"\\n    bibtex_key: \\\"uda2026\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Neural K-factor adjustment reducing inter-judge std by 63.4%. Black-box neural approach vs G-MFRM's interpretable psychometric approach. Key baseline for judge bias correction.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  constat2024:\\n    title: \\\"ConStat: Statistical Detection and Quantification of Benchmark Contamination\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS\\\"\\n    bibtex_key: \\\"constat2024\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"component\\\"\\n    relevance: \\\"Core component of G-MFRM Stage 2. Computes contamination effects via reference benchmark comparison (r^2=0.94 with true effects). Fully black-box, used to estimate per-item exposure e_i.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  dcr2025:\\n    title: \\\"DCR: Quantifying Data Contamination in LLMs Evaluation\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    bibtex_key: \\\"dcr2025\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Adjusts accuracy for contamination via fuzzy inference but ignores judge effects. Primary contamination-only baseline for G-MFRM comparison.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  preference_leakage2026:\\n    title: \\\"Preference Leakage: A Contamination Problem in LLM-as-a-judge\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"ICLR\\\"\\n    bibtex_key: \\\"preference_leakage2026\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Quantifies generator-judge relatedness bias (judge-side contamination). Distinct from G-MFRM's examinee-side contamination. Preference Leakage's relatedness bias can be partially captured by G-MFRM's d_j facet.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  logprober2024:\\n    title: \\\"LogProber: Detecting Data Contamination via Token Log-Probability Analysis\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    bibtex_key: \\\"logprober2024\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"component\\\"\\n    relevance: \\\"Estimates per-item Safe Scores from token log-probabilities. Gray-box exposure indicator for G-MFRM Stage 2 (for models exposing logprobs).\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  zheng2023mtbench:\\n    title: \\\"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\\\"\\n    authors:\\n      - \\\"Zheng, L.\\\"\\n      - \\\"Chiang, W.-L.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS\\\"\\n    bibtex_key: \\\"zheng2023mtbench\\\"\\n    category: \\\"unified_evaluation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Establishes LLM-as-a-judge paradigm and MT-Bench/Chatbot Arena benchmarks. Primary evaluation benchmark for G-MFRM validation. Human votes from Arena serve as ground truth for Kendall-tau comparison.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\", \"total_chars\": 7733, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4002cfea-100d-45ec-b33c-ee50dd1a0eec",
  "isSidechain": false,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "type": "user",
  "uuid": "c1bb9a46-92c6-4994-8b45-e465b59ef3c0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/literature_map.yaml\\\", \\\"content\\\": \\\"meta:\\\\n  last_updated: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n  total_papers: 12\\\\ncategories:\\\\n  - key: \\\\\\\"psychometric_foundation\\\\\\\"\\\\n    name: \\\\\\\"Psychometric & IRT Foundation\\\\\\\"\\\\n    narrative: \\\\\\\"Core psychometric models: DG-IRT gating mechanism for cheating detection, MFRM applied to LLM raters, and IRT-based LLM evaluation frameworks\\\\\\\"\\\\n  - key: \\\\\\\"judge_bias_correction\\\\\\\"\\\\n    name: \\\\\\\"Judge Bias Correction\\\\\\\"\\\\n    narrative: \\\\\\\"Methods for detecting and correcting systematic biases in LLM-as-a-judge evaluation pipelines\\\\\\\"\\\\n  - key: \\\\\\\"contamination_detection\\\\\\\"\\\\n    name: \\\\\\\"Contamination Detection & Adjustment\\\\\\\"\\\\n    narrative: \\\\\\\"Methods for detecting and quantifying benchmark contamination in LLM evaluation\\\\\\\"\\\\n  - key: \\\\\\\"unified_evaluation\\\\\\\"\\\\n    name: \\\\\\\"Unified Evaluation Frameworks\\\\\\\"\\\\n    narrative: \\\\\\\"Comprehensive LLM evaluation frameworks and benchmarks that combine multiple assessment dimensions\\\\\\\"\\\\npapers:\\\\n  shu2013dgirt:\\\\n    title: \\\\\\\"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Shu, Z.\\\\\\\"\\\\n      - \\\\\\\"Henson, R.\\\\\\\"\\\\n      - \\\\\\\"Luecht, R.\\\\\\\"\\\\n    year: 2013\\\\n    venue: \\\\\\\"Psychometrika\\\\\\\"\\\\n    doi: \\\\\\\"10.1007/s11336-012-9311-3\\\\\\\"\\\\n    bibtex_key: \\\\\\\"shu2013dgirt\\\\\\\"\\\\n    category: \\\\\\\"psychometric_foundation\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"Core methodological inspiration. DG-IRT decomposes observed performance into genuine ability and cheating-inflated components via a gating mechanism. G-MFRM adapts this gating logic from educational cheating to LLM benchmark contamination.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  wang2025mfrm_llm:\\\\n    title: \\\\\\\"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Wang, Y.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2505.18486\\\\\\\"\\\\n    bibtex_key: \\\\\\\"wang2025mfrm_llm\\\\\\\"\\\\n    category: \\\\\\\"psychometric_foundation\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"Most direct predecessor. Applies MFRM to compare 10 LLM raters with human experts, demonstrating MFRM's applicability to LLM judge calibration. Does NOT model contamination — the gap G-MFRM fills.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  lin2025psnirt:\\\\n    title: \\\\\\\"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Lin, Z.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"AAAI\\\\\\\"\\\\n    bibtex_key: \\\\\\\"lin2025psnirt\\\\\\\"\\\\n    category: \\\\\\\"psychometric_foundation\\\\\\\"\\\\n    role: \\\\\\\"baseline\\\\\\\"\\\\n    relevance: \\\\\\\"Neural 4PL IRT for LLM benchmark evaluation. Demonstrates scalability of IRT to LLMs but lacks judge facet and contamination modeling. Serves as IRT-based baseline without multi-facet structure.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  cyclicjudge2026:\\\\n    title: \\\\\\\"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Unknown\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    bibtex_key: \\\\\\\"cyclicjudge2026\\\\\\\"\\\\n    category: \\\\\\\"judge_bias_correction\\\\\\\"\\\\n    role: \\\\\\\"baseline\\\\\\\"\\\\n    relevance: \\\\\\\"Primary bias-only baseline. Eliminates judge bias via round-robin assignment but completely ignores contamination. G-MFRM addresses both jointly.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  fiedler2026bias_uncertainty:\\\\n    title: \\\\\\\"Bias and Uncertainty in LLM-as-a-Judge Estimation\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Fiedler, M.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2605.06939\\\\\\\"\\\\n    bibtex_key: \\\\\\\"fiedler2026bias_uncertainty\\\\\\\"\\\\n    category: \\\\\\\"judge_bias_correction\\\\\\\"\\\\n    role: \\\\\\\"related\\\\\\\"\\\\n    relevance: \\\\\\\"Introduces formal J/delta-J diagnostics for judge bias, identifies sign-reversal failure modes in shared-calibration comparisons. Stays within classical test theory. G-MFRM's confounding argument positions Fiedler's sign-reversal as downstream consequence of unmodeled contamination.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  soumik2026judging_judges:\\\\n    title: \\\\\\\"Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Soumik, M.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2604.23178\\\\\\\"\\\\n    bibtex_key: \\\\\\\"soumik2026judging_judges\\\\\\\"\\\\n    category: \\\\\\\"judge_bias_correction\\\\\\\"\\\\n    role: \\\\\\\"related\\\\\\\"\\\\n    relevance: \\\\\\\"Empirically compares 9 debiasing strategies across 5 judges, finding style bias dominant (0.76-0.92). Provides no measurement model explaining why strategies work — G-MFRM provides the explanatory framework.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  uda2026:\\\\n    title: \\\\\\\"UDA: Unsupervised Debiasing Alignment for LLM Judges\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Unknown\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"AAAI\\\\\\\"\\\\n    bibtex_key: \\\\\\\"uda2026\\\\\\\"\\\\n    category: \\\\\\\"judge_bias_correction\\\\\\\"\\\\n    role: \\\\\\\"baseline\\\\\\\"\\\\n    relevance: \\\\\\\"Neural K-factor adjustment reducing inter-judge std by 63.4%. Black-box neural approach vs G-MFRM's interpretable psychometric approach. Key baseline for judge bias correction.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  constat2024:\\\\n    title: \\\\\\\"ConStat: Statistical Detection and Quantification of Benchmark Contamination\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Unknown\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"NeurIPS\\\\\\\"\\\\n    bibtex_key: \\\\\\\"constat2024\\\\\\\"\\\\n    category: \\\\\\\"contamination_detection\\\\\\\"\\\\n    role: \\\\\\\"component\\\\\\\"\\\\n    relevance: \\\\\\\"Core component of G-MFRM Stage 2. Computes contamination effects via reference benchmark comparison (r^2=0.94 with true effects). Fully black-box, used to estimate per-item exposure e_i.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  dcr2025:\\\\n    title: \\\\\\\"DCR: Quantifying Data Contamination in LLMs Evaluation\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Unknown\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"EMNLP\\\\\\\"\\\\n    bibtex_key: \\\\\\\"dcr2025\\\\\\\"\\\\n    category: \\\\\\\"contamination_detection\\\\\\\"\\\\n    role: \\\\\\\"baseline\\\\\\\"\\\\n    relevance: \\\\\\\"Adjusts accuracy for contamination via fuzzy inference but ignores judge effects. Primary contamination-only baseline for G-MFRM comparison.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  preference_leakage2026:\\\\n    title: \\\\\\\"Preference Leakage: A Contamination Problem in LLM-as-a-judge\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Unknown\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"ICLR\\\\\\\"\\\\n    bibtex_key: \\\\\\\"preference_leakage2026\\\\\\\"\\\\n    category: \\\\\\\"contamination_detection\\\\\\\"\\\\n    role: \\\\\\\"related\\\\\\\"\\\\n    relevance: \\\\\\\"Quantifies generator-judge relatedness bias (judge-side contamination). Distinct from G-MFRM's examinee-side contamination. Preference Leakage's relatedness bias can be partially captured by G-MFRM's d_j facet.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  logprober2024:\\\\n    title: \\\\\\\"LogProber: Detecting Data Contamination via Token Log-Probability Analysis\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Unknown\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    bibtex_key: \\\\\\\"logprober2024\\\\\\\"\\\\n    category: \\\\\\\"contamination_detection\\\\\\\"\\\\n    role: \\\\\\\"component\\\\\\\"\\\\n    relevance: \\\\\\\"Estimates per-item Safe Scores from token log-probabilities. Gray-box exposure indicator for G-MFRM Stage 2 (for models exposing logprobs).\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\\n  zheng2023mtbench:\\\\n    title: \\\\\\\"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\\\\\\\"\\\\n    authors:\\\\n      - \\\\\\\"Zheng, L.\\\\\\\"\\\\n      - \\\\\\\"Chiang, W.-L.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS\\\\\\\"\\\\n    bibtex_key: \\\\\\\"zheng2023mtbench\\\\\\\"\\\\n    category: \\\\\\\"unified_evaluation\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"Establishes LLM-as-a-judge paradigm and MT-Bench/Chatbot Arena benchmarks. Primary evaluation benchmark for G-MFRM validation. Human votes from Arena serve as ground truth for Kendall-tau comparison.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-21T16:40:00Z\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 7733, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-21T16:40:00Z\\\"\\n  total_papers: 12\\ncategories:\\n  - key: \\\"psychometric_foundation\\\"\\n    name: \\\"Psychometric & IRT Foundation\\\"\\n    narrative: \\\"Core psychometric models: DG-IRT gating mechanism for cheating detection, MFRM applied to LLM raters, and IRT-based LLM evaluation frameworks\\\"\\n  - key: \\\"judge_bias_correction\\\"\\n    name: \\\"Judge Bias Correction\\\"\\n    narrative: \\\"Methods for detecting and correcting systematic biases in LLM-as-a-judge evaluation pipelines\\\"\\n  - key: \\\"contamination_detection\\\"\\n    name: \\\"Contamination Detection & Adjustment\\\"\\n    narrative: \\\"Methods for detecting and quantifying benchmark contamination in LLM evaluation\\\"\\n  - key: \\\"unified_evaluation\\\"\\n    name: \\\"Unified Evaluation Frameworks\\\"\\n    narrative: \\\"Comprehensive LLM evaluation frameworks and benchmarks that combine multiple assessment dimensions\\\"\\npapers:\\n  shu2013dgirt:\\n    title: \\\"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\\\"\\n    authors:\\n      - \\\"Shu, Z.\\\"\\n      - \\\"Henson, R.\\\"\\n      - \\\"Luecht, R.\\\"\\n    year: 2013\\n    venue: \\\"Psychometrika\\\"\\n    doi: \\\"10.1007/s11336-012-9311-3\\\"\\n    bibtex_key: \\\"shu2013dgirt\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Core methodological inspiration. DG-IRT decomposes observed performance into genuine ability and cheating-inflated components via a gating mechanism. G-MFRM adapts this gating logic from educational cheating to LLM benchmark contamination.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  wang2025mfrm_llm:\\n    title: \\\"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\\\"\\n    authors:\\n      - \\\"Wang, Y.\\\"\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2505.18486\\\"\\n    bibtex_key: \\\"wang2025mfrm_llm\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Most direct predecessor. Applies MFRM to compare 10 LLM raters with human experts, demonstrating MFRM's applicability to LLM judge calibration. Does NOT model contamination — the gap G-MFRM fills.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  lin2025psnirt:\\n    title: \\\"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT\\\"\\n    authors:\\n      - \\\"Lin, Z.\\\"\\n    year: 2026\\n    venue: \\\"AAAI\\\"\\n    bibtex_key: \\\"lin2025psnirt\\\"\\n    category: \\\"psychometric_foundation\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Neural 4PL IRT for LLM benchmark evaluation. Demonstrates scalability of IRT to LLMs but lacks judge facet and contamination modeling. Serves as IRT-based baseline without multi-facet structure.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  cyclicjudge2026:\\n    title: \\\"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    bibtex_key: \\\"cyclicjudge2026\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Primary bias-only baseline. Eliminates judge bias via round-robin assignment but completely ignores contamination. G-MFRM addresses both jointly.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  fiedler2026bias_uncertainty:\\n    title: \\\"Bias and Uncertainty in LLM-as-a-Judge Estimation\\\"\\n    authors:\\n      - \\\"Fiedler, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2605.06939\\\"\\n    bibtex_key: \\\"fiedler2026bias_uncertainty\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Introduces formal J/delta-J diagnostics for judge bias, identifies sign-reversal failure modes in shared-calibration comparisons. Stays within classical test theory. G-MFRM's confounding argument positions Fiedler's sign-reversal as downstream consequence of unmodeled contamination.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  soumik2026judging_judges:\\n    title: \\\"Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\\\"\\n    authors:\\n      - \\\"Soumik, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    arxiv_id: \\\"2604.23178\\\"\\n    bibtex_key: \\\"soumik2026judging_judges\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Empirically compares 9 debiasing strategies across 5 judges, finding style bias dominant (0.76-0.92). Provides no measurement model explaining why strategies work — G-MFRM provides the explanatory framework.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  uda2026:\\n    title: \\\"UDA: Unsupervised Debiasing Alignment for LLM Judges\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"AAAI\\\"\\n    bibtex_key: \\\"uda2026\\\"\\n    category: \\\"judge_bias_correction\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Neural K-factor adjustment reducing inter-judge std by 63.4%. Black-box neural approach vs G-MFRM's interpretable psychometric approach. Key baseline for judge bias correction.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  constat2024:\\n    title: \\\"ConStat: Statistical Detection and Quantification of Benchmark Contamination\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2024\\n    venue: \\\"NeurIPS\\\"\\n    bibtex_key: \\\"constat2024\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"component\\\"\\n    relevance: \\\"Core component of G-MFRM Stage 2. Computes contamination effects via reference benchmark comparison (r^2=0.94 with true effects). Fully black-box, used to estimate per-item exposure e_i.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  dcr2025:\\n    title: \\\"DCR: Quantifying Data Contamination in LLMs Evaluation\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2025\\n    venue: \\\"EMNLP\\\"\\n    bibtex_key: \\\"dcr2025\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"baseline\\\"\\n    relevance: \\\"Adjusts accuracy for contamination via fuzzy inference but ignores judge effects. Primary contamination-only baseline for G-MFRM comparison.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  preference_leakage2026:\\n    title: \\\"Preference Leakage: A Contamination Problem in LLM-as-a-judge\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2026\\n    venue: \\\"ICLR\\\"\\n    bibtex_key: \\\"preference_leakage2026\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"related\\\"\\n    relevance: \\\"Quantifies generator-judge relatedness bias (judge-side contamination). Distinct from G-MFRM's examinee-side contamination. Preference Leakage's relatedness bias can be partially captured by G-MFRM's d_j facet.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  logprober2024:\\n    title: \\\"LogProber: Detecting Data Contamination via Token Log-Probability Analysis\\\"\\n    authors:\\n      - \\\"Unknown\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    bibtex_key: \\\"logprober2024\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"component\\\"\\n    relevance: \\\"Estimates per-item Safe Scores from token log-probabilities. Gray-box exposure indicator for G-MFRM Stage 2 (for models exposing logprobs).\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\\n  zheng2023mtbench:\\n    title: \\\"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\\\"\\n    authors:\\n      - \\\"Zheng, L.\\\"\\n      - \\\"Chiang, W.-L.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS\\\"\\n    bibtex_key: \\\"zheng2023mtbench\\\"\\n    category: \\\"unified_evaluation\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Establishes LLM-as-a-judge paradigm and MT-Bench/Chatbot Arena benchmarks. Primary evaluation benchmark for G-MFRM validation. Human votes from Arena serve as ground truth for Kendall-tau comparison.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-21T16:40:00Z\\\"\\n\", \"total_chars\": 7733, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "4002cfea-100d-45ec-b33c-ee50dd1a0eec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "c1bb9a46-92c6-4994-8b45-e465b59ef3c0",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Assistant

_source line 54 · 2026-05-21T16:38:46.347Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have a clear picture of the project:

**Project**: G-MFRM (Gated Many-Facet Rasch Measurement) for jointly correcting judge bias and contamination in LLM evaluation.

**Core idea**: Sequential methods (first correct judge bias, then contamination or vice versa) have confounding between judge severity (d_j) and contamination (c_n·e_i). A joint psychometric model handles both simultaneously.

**Paper roles**:
- Foundation: shu2013dgirt (gating mechanism), wang2025mfrm_llm (MFRM for LLM), zheng2023mtbench (LLM-as-judge paradigm)


- Baselines and related work: lin2025psnirt provides IRT-based comparison, cyclicjudge2026 and uda2026 focus on bias correction alone, dcr2025 handles contamination separately, while constat2024 and logprober2024 offer contamination estimation and exposure detection methods. I'm also tracking preference_leakage2026, fiedler2026bias_uncertainty, and soumik2026judging_judges as related perspectives.

Now I'm waiting for the agents to return with the actual paper content so I can start building out the model details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1bb9a46-92c6-4994-8b45-e465b59ef3c0",
  "isSidechain": false,
  "requestId": "req_011CbG3SrotHJJq5NSMBn4qP",
  "type": "assistant",
  "uuid": "78451577-0b16-4324-abab-68625ce085e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tm2VxGPxyZmA8H7ki2D4aJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5152,
      "cache_read_input_tokens": 37249,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 360,
          "cache_read_input_tokens": 37249,
          "cache_creation_input_tokens": 5152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5152
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 55 · 2026-05-21T16:38:46.349Z_

项目背景已获取：G-MFRM 联合校正 LLM 评测中的 judge bias 和 contamination。等待论文获取 agents 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78451577-0b16-4324-abab-68625ce085e0",
  "isSidechain": false,
  "requestId": "req_011CbG3SrotHJJq5NSMBn4qP",
  "type": "assistant",
  "uuid": "b1f48af8-a2cc-4edc-9353-16afc6e7c23c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tm2VxGPxyZmA8H7ki2D4aJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5152,
      "cache_read_input_tokens": 37249,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 360,
          "cache_read_input_tokens": 37249,
          "cache_creation_input_tokens": 5152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5152
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 56 · 2026-05-21T16:40:48.478Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:40:48.478Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "&lt;task-notification>\n&lt;task-id>a60de764ef418ebcf&lt;/task-id>\n&lt;tool-use-id>toolu_01Bb5xw2kHxdSu2uyxpA8eXK&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/a60de764ef418ebcf.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch abstract-only papers\" completed&lt;/summary>\n&lt;result>All four papers found. Here is the structured extraction:\n\n---\n\n**paper_key: fiedler2026bias_uncertainty**\n- Title: \"Bias and Uncertainty in LLM-as-a-Judge Estimation\"\n- Venue: arXiv 2026 (cs.LG, stat.ME, stat.ML); submitted May 7, 2026; arXiv:2605.06939\n- Author: James Fiedler\n- Method family: Statistical estimation / bias correction for LLM-as-a-Judge evaluation\n- Core approach: Analytical study of naive estimator bias and corrected estimators; proposes J (judge quality) and ΔJ (cross-model calibration instability) as diagnostic measures; uses simulations and a real-data case study\n- Baselines: Naive estimator (raw judge outputs); existing bias-correction estimators (prior work)\n- Metrics: J (judge quality), ΔJ (calibration instability); sign-reversal detection; apparent confidence of comparison estimates\n- Datasets: MMLU-Pro (real-data case study)\n- Key contribution: Shows that shared calibration across compared models can introduce severe bias with sign reversal at high confidence; proposes diagnostics for identifying unreliable corrected estimates\n\n---\n\n**paper_key: soumik2026judging_judges**\n- Title: \"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\"\n- Venue: arXiv 2026; arXiv:2604.23178\n- Author: Sadman Kabir Soumik\n- Method family: Empirical comparative evaluation — systematic benchmark of debiasing strategies\n- Core approach: Tests 9 debiasing strategies across 5 judge models (Google, Anthropic, OpenAI, Meta providers) on 3 benchmarks and 4 bias types; releases evaluation framework and controlled dataset\n- Baselines (9 debiasing strategies compared, specific names not listed in abstract; judge models include Claude Sonnet 4, plus models from Google/OpenAI/Meta)\n- Metrics: Style bias score (0.76–0.92), position bias (≤0.04), quality-length discrimination accuracy (0.92–1.00), agreement change in percentage points (e.g., +11.2 pp for Claude Sonnet 4, p&lt;0.0001)\n- Datasets/Benchmarks: MT-Bench (n=400), LLMBar (n=200), custom benchmark (n=225)\n- Key findings: Style bias dominates (far exceeds position bias); debiasing is model-dependent; combined budget strategy significantly helps Claude Sonnet 4\n\n---\n\n**paper_key: logprober2024**\n- Title: \"LogProber: Disentangling confidence from contamination in LLM responses\"\n- Venue: arXiv 2024; arXiv:2408.14352\n- Authors: Nicolas Yax, Pierre-Yves Oudeyer, Stefano Palminteri\n- Method family: Token log-probability analysis for data contamination detection (black-box setting)\n- Core approach: Sorts cumulative token log-probability values of questions in increasing order, computes area under the curve, transforms to a \"Safe Score\" via logarithm; items with Safe Score &lt;1 flagged as contaminated; focuses on familiarity with the question (not the answer)\n- Baselines: CDD (Contamination Detection via Diversity, Dong et al. 2024); TS-Guessing (Deng et al. 2024)\n- Metrics: Safe Score, Accuracy, Precision, Recall, F1, statistical significance (t-tests), contamination ratio %\n- Datasets: Cognitive Reflection Test (oldCRT vs newCRT), MMLU, BigCodeBench, MBXP; models: Llama-1 7B, Qwen2.5-32B-Instruct\n- Key findings: Outperforms CDD on MMLU (98% vs 50% accuracy); detects Q-A contamination but fails for answer-only contamination; complementary to other approaches depending on contamination type\n\n---\n\n**paper_key: shu2013dgirt**\n- Title: \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\"\n- Venue: Psychometrika 2013, Volume 78(3), pages 481–497\n- Authors: Zhan Shu, Robert Henson, Richard Luecht\n- Not on arXiv (psychometrics/educational measurement literature)\n- Method family: Bayesian psychometric modeling — Deterministic Gated IRT (DGM)\n- Core approach: Decomposes examinee response data into two latent distributions via a \"gated\" function — one reflecting genuine latent ability, one capturing \"cheating ability\" (pre-knowledge of exposed items); estimates using Hierarchical Markov Chain Monte Carlo (HMCMC)\n- Key concepts: Item compromise detection, test security, score gain analysis (exposed vs. unexposed items), two-component mixture model with gating mechanism, item pre-knowledge modeling\n- Baselines: Not specified (foundational psychometrics paper proposing a novel model)\n- Datasets: Real test data (operational exam data; details not publicly available)\n- Metrics: Model fit, examinee classification (cheater vs. non-cheater), score gain on exposed vs. unexposed items\n- Relevance to gated_mfrm_judge_bias: The gating mechanism (decomposing a single observed score into two latent components conditioned on a binary state) is the direct psychometric ancestor of gated IRT approaches applied to judge response modeling&lt;/result>\n&lt;usage>&lt;total_tokens>24668&lt;/total_tokens>&lt;tool_uses>19&lt;/tool_uses>&lt;duration_ms>145461&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---


### Runtime record

_source line 57 · 2026-05-21T16:40:48.553Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T16:40:48.553Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


## Round 2

## Round 2

7 recorded events


### User

_source line 58 · 2026-05-21T16:40:48.624Z_

&lt;task-notification>
&lt;task-id>a60de764ef418ebcf&lt;/task-id>
&lt;tool-use-id>toolu_01Bb5xw2kHxdSu2uyxpA8eXK&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/a60de764ef418ebcf.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Fetch abstract-only papers" completed&lt;/summary>
&lt;result>All four papers found. Here is the structured extraction:

---

**paper_key: fiedler2026bias_uncertainty**
- Title: "Bias and Uncertainty in LLM-as-a-Judge Estimation"
- Venue: arXiv 2026 (cs.LG, stat.ME, stat.ML); submitted May 7, 2026; arXiv:2605.06939
- Author: James Fiedler
- Method family: Statistical estimation / bias correction for LLM-as-a-Judge evaluation
- Core approach: Analytical study of naive estimator bias and corrected estimators; proposes J (judge quality) and ΔJ (cross-model calibration instability) as diagnostic measures; uses simulations and a real-data case study
- Baselines: Naive estimator (raw judge outputs); existing bias-correction estimators (prior work)
- Metrics: J (judge quality), ΔJ (calibration instability); sign-reversal detection; apparent confidence of comparison estimates
- Datasets: MMLU-Pro (real-data case study)
- Key contribution: Shows that shared calibration across compared models can introduce severe bias with sign reversal at high confidence; proposes diagnostics for identifying unreliable corrected estimates

---

**paper_key: soumik2026judging_judges**
- Title: "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines"
- Venue: arXiv 2026; arXiv:2604.23178
- Author: Sadman Kabir Soumik
- Method family: Empirical comparative evaluation — systematic benchmark of debiasing strategies
- Core approach: Tests 9 debiasing strategies across 5 judge models (Google, Anthropic, OpenAI, Meta providers) on 3 benchmarks and 4 bias types; releases evaluation framework and controlled dataset
- Baselines (9 debiasing strategies compared, specific names not listed in abstract; judge models include Claude Sonnet 4, plus models from Google/OpenAI/Meta)
- Metrics: Style bias score (0.76–0.92), position bias (≤0.04), quality-length discrimination accuracy (0.92–1.00), agreement change in percentage points (e.g., +11.2 pp for Claude Sonnet 4, p&lt;0.0001)
- Datasets/Benchmarks: MT-Bench (n=400), LLMBar (n=200), custom benchmark (n=225)
- Key findings: Style bias dominates (far exceeds position bias); debiasing is model-dependent; combined budget strategy significantly helps Claude Sonnet 4

---

**paper_key: logprober2024**
- Title: "LogProber: Disentangling confidence from contamination in LLM responses"
- Venue: arXiv 2024; arXiv:2408.14352
- Authors: Nicolas Yax, Pierre-Yves Oudeyer, Stefano Palminteri
- Method family: Token log-probability analysis for data contamination detection (black-box setting)
- Core approach: Sorts cumulative token log-probability values of questions in increasing order, computes area under the curve, transforms to a "Safe Score" via logarithm; items with Safe Score &lt;1 flagged as contaminated; focuses on familiarity with the question (not the answer)
- Baselines: CDD (Contamination Detection via Diversity, Dong et al. 2024); TS-Guessing (Deng et al. 2024)
- Metrics: Safe Score, Accuracy, Precision, Recall, F1, statistical significance (t-tests), contamination ratio %
- Datasets: Cognitive Reflection Test (oldCRT vs newCRT), MMLU, BigCodeBench, MBXP; models: Llama-1 7B, Qwen2.5-32B-Instruct
- Key findings: Outperforms CDD on MMLU (98% vs 50% accuracy); detects Q-A contamination but fails for answer-only contamination; complementary to other approaches depending on contamination type

---

**paper_key: shu2013dgirt**
- Title: "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise"
- Venue: Psychometrika 2013, Volume 78(3), pages 481–497
- Authors: Zhan Shu, Robert Henson, Richard Luecht
- Not on arXiv (psychometrics/educational measurement literature)
- Method family: Bayesian psychometric modeling — Deterministic Gated IRT (DGM)
- Core approach: Decomposes examinee response data into two latent distributions via a "gated" function — one reflecting genuine latent ability, one capturing "cheating ability" (pre-knowledge of exposed items); estimates using Hierarchical Markov Chain Monte Carlo (HMCMC)
- Key concepts: Item compromise detection, test security, score gain analysis (exposed vs. unexposed items), two-component mixture model with gating mechanism, item pre-knowledge modeling
- Baselines: Not specified (foundational psychometrics paper proposing a novel model)
- Datasets: Real test data (operational exam data; details not publicly available)
- Metrics: Model fit, examinee classification (cheater vs. non-cheater), score gain on exposed vs. unexposed items
- Relevance to gated_mfrm_judge_bias: The gating mechanism (decomposing a single observed score into two latent components conditioned on a binary state) is the direct psychometric ancestor of gated IRT approaches applied to judge response modeling&lt;/result>
&lt;usage>&lt;total_tokens>24668&lt;/total_tokens>&lt;tool_uses>19&lt;/tool_uses>&lt;duration_ms>145461&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1f48af8-a2cc-4edc-9353-16afc6e7c23c",
  "isSidechain": false,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "type": "user",
  "uuid": "bde0536b-1240-4b2b-8208-1372e7a511d0",
  "permissionMode": "bypassPermissions",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 59 · 2026-05-21T16:40:52.635Z_

<details><summary>Logged reasoning block</summary>

```text
The abstract-only papers agent has completed. Let me process this data and wait for the other agents. Let me continue with the other agents' results as they come in.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bde0536b-1240-4b2b-8208-1372e7a511d0",
  "isSidechain": false,
  "requestId": "req_011CbG3cnzE6dbZ5sHgpy2NS",
  "type": "assistant",
  "uuid": "e80f16b8-a88e-425c-b208-9a68a8711f4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYehLvJLeM6n6aKSU4S9Fi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1950,
      "cache_read_input_tokens": 42401,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 79,
          "cache_read_input_tokens": 42401,
          "cache_creation_input_tokens": 1950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1950
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 60 · 2026-05-21T16:40:53.366Z_

摘要论文已获取完毕。继续等待深度精读论文的返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e80f16b8-a88e-425c-b208-9a68a8711f4c",
  "isSidechain": false,
  "requestId": "req_011CbG3cnzE6dbZ5sHgpy2NS",
  "type": "assistant",
  "uuid": "495da358-64d6-417e-a074-323b07c5fc94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYehLvJLeM6n6aKSU4S9Fi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1950,
      "cache_read_input_tokens": 42401,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 79,
          "cache_read_input_tokens": 42401,
          "cache_creation_input_tokens": 1950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1950
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 61 · 2026-05-21T16:41:53.708Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:41:53.708Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "&lt;task-notification>\n&lt;task-id>aed1d3e555792ca7c&lt;/task-id>\n&lt;tool-use-id>toolu_01V46oYv3iHYpqdayCFc12tH&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/aed1d3e555792ca7c.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: wang2025mfrm_llm\" completed&lt;/summary>\n&lt;result>Here is the complete extracted text from arXiv:2505.18486.\n\n---\n\n## Paper: \"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\"\n\n**Authors:** Hong Jiao (University of Maryland, College Park), Dan Song, Won-Chan Lee (University of Iowa)\n\n---\n\n### ABSTRACT\n\nLarge language models (LLMs) have been widely explored for automated scoring in low-stakes assessment to facilitate learning and instruction. Empirical evidence related to which LLM produces the most reliable scores and induces least rater effects needs to be collected before the use of LLMs for automated scoring in practice. This study compared ten LLMs (ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3, and DeepSeek R1) with human expert raters in scoring two types of writing tasks. The accuracy of the holistic and analytic scores from LLMs compared with human raters was evaluated in terms of Quadratic Weighted Kappa. Intra-rater consistency across prompts was compared in terms of Cronbach Alpha. Rater effects of LLMs were evaluated and compared with human raters using the Many-Facet Rasch model. The results in general supported the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high scoring accuracy, better rater reliability, and less rater effects.\n\n---\n\n### 1. INTRODUCTION (Complete text)\n\n**Paragraph 1:**\nPerformance assessment tasks, including essays and other types of constructed-response (CR) items are commonly used for assessing high-order thinking skills such as synthesizing information from multiple sources, critical evaluations, and evidence-based reasoning. These assessment formats are commonly employed in formative classroom assessments to facilitate instruction and learning as well as in high-stakes summative assessments for accountability and admission decisions. While the score represents a key form of feedback, the scoring of such assessment tasks is often costly, time-consuming, and error prone due to the subjectivity of human raters.\n\n**Paragraph 2:**\nAutomated scoring of performance items is an efficient and scientifically validated technology designed to complement and enhance human scoring (Shermis, 2015). For example, automating the scoring of the National Assessment of Educational Progress (NAEP) CR items could yield significant cost saving of 70% for reading and 40% for math (Justice &amp; Palermo, 2020). As one of the most successful applications of AI technology in educational assessments, the progress in automated scoring is aligned closely with the advances in machine learning and natural language processing (NLP). Though research on automated scoring started with the pioneering work of Page (1966; 2003), recent advances in AI technology have made breakthrough in automated scoring.\n\n**Paragraph 3:**\nAutomated scoring can be categorized into two main approaches: feature-based and deep learning-based (Haller et al., 2022), with the latter further classified into neural network, small language model (SLM), and large language model (LLM) based approaches. Feature-based approaches rely on the extracted length, prompt, readability, syntactic, semantic, lexical, and discourse features (Ke &amp; Ng, 2019; Uto et al., 2020) and supervised machine learning models. Deep learning-based approaches use word embeddings (Word2Vec, GloVe) and context embeddings from small language models (SLMs) such as BERT, deBERTa based on transformer (Vaswani et al., 2017) and large language models (LLMs) such as GPT, Claude, and Gemini.\n\n**Paragraph 4:**\nDeveloping feature-based or SLM-based automated scoring systems often requires foundational skills in supervised machine learning, NLP, and deep learning. This dramatically reduces the accessibility of automated scoring to classroom learners, teachers, and assessment developers. However, with the swift emerging of more capable LLMs, automated scoring techniques are becoming increasingly accessible to non-technical users who can fully leverage the LLM technology to revamp their routine scoring practices, with enhanced efficiency and accuracy.\n\n**Paragraph 5:**\nWith the advances in Generative AI or Chatbots, LLMs have been explored for automated scoring in education assessments. LLMs have demonstrated unprecedented potential in automated scoring of essays and CR items in educational assessments (Latif &amp; Zhai, 2024; Lee et al., 2024; Yancey et al., 2023; Yang et al., 2025). In low-stakes assessment programs, three commonly used models are ChatGPT by OpenAI, Claude by Anthropic, and Google Gemini. Recent studies have explored the use of GPT models, such as GPT 3.5 (Bui &amp; Barrot, 2024; Mizumoto &amp; Eguchi, 2023; Parker et al., 2023; Wijekumar et al., 2024) and GPT 4 (Kortemeyer, 2024) in automated scoring. Furthermore, several studies have compared the performance of GPT 3.5 and GPT 4 (Kim &amp; Jo, 2024; Tate et al., 2024) as well as GPT and Llama3 (Kundu &amp; Barbosa, 2024). Pack et al. (2024) compared PaLM 2, Claude 2, and GPT 3.5 and GPT 4, concluding that GPT 4 outperformed the others. Almost all studies on using LLMs for automated scoring purely focused on scoring accuracy, little is known about the potential rater effects of these LLM scoring engines.\n\n**Paragraph 6:**\nRater effects (Myford &amp; Wolfe, 2003, 2004; Saal, Downey, &amp; Lahey, 1980) refer to different types of inconsistencies in ratings when human raters assign scores to test-takers' constructed responses to performance tasks such as essays or CR items in educational assessments. Rater effects may occur due to raters' personal backgrounds, preferences, inaccurate interpretations of the scoring rubrics, inappropriate conceptualization of the target test-takers' population, and their idiosyncratic traits that may impact their accuracy and consistency in assigning scores to assessment items. Rater effects can be classified into different categories. Some common rater effects include rater severity/leniency and centrality. When a rater assigns scores to students' responses to a performance task consistently lower than other raters, this rater effect is noted as rater severity. When rater severity is present, students' true scores may be underestimated if such rater effect is ignored. On the other hand, when a rater assigns scores to students' responses consistently higher than other raters, this rater effect is noted as rater leniency. When rater leniency is present, students' true scores may be overestimated if such rater effect is not accounted for. Further, some raters may consistently assign scores in the middle of the score scale and not assign high scores or low scores regardless of the ability levels. This central tendency or centrality effect will introduce score errors for students whose true scores lie at the two ends of the score scale. Such rater effects are as severe as score accuracy as they may compromise the fairness, reliability, and validity of the assigned scores. Though in operational rating sessions, different strategies would be implemented to minimize rater effects such as standardized rubrics, comprehensive rater training and calibration, in-session and post-session quality control of ratings, or assigning multiple raters to each rating tasks, rater effects need to be tracked as a source of validity evidence.\n\n**Paragraph 7 (Research Questions / Contribution Statement):**\nEach LLM has its own strengths and features that may cater to different scoring needs and applications. Like human raters, AI raters may bear different degrees of rater effects. Thus, it is worthwhile to compare the ratings from different scoring engines and understand the potential AI rater effects of each LLM. Thus, this study aims to investigate the AI rater effects in addition to rating accuracy and consistency compared with human raters of essay scoring. The AI raters investigated in this study include ten commonly used LLMs from GPT, Gemini, and Claude families and some recent LLMs such as DeepSeek. The research questions for the study include:\n1. How accurate are LLM raters compared with human raters?\n2. How consistent or reliable are LLM raters compared with human raters?\n3. What are the LLM rater effects compared with human raters?\n\n---\n\n### METHODS\n\n**Overview:**\nThis study conducts a series of psychometric analyses to investigate the AI raters' scoring accuracy and consistency, as well as uses the Many-Facet Rasch measurement model (Linacre, 1989, 1994, 2024; Wright &amp; Masters, 1982; Wright &amp; Stone, 1979) to investigate and compare rater effects between AI raters and human raters in a large-scale writing assessment.\n\n**Data:**\nA dataset consists of 30 student essays on two types of writing tasks. Each essay was scored by two human raters and ten AI raters, including ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3 and DeepSeek R1. The 30 U.S. college students, enrolled in Mandarin Chinese language courses, included 18 third-year and 12 fourth-year students from a range of majors such as business, humanities, STEM, and diplomacy. Data collection took place over two consecutive days using constructed-response writing prompts from the 2021 and 2022 AP Chinese exams developed by the College Board. On the first day, students completed the 2021 prompts, which included one story narration (SN1) task and one email response (ER1) task. On the second day, they responded to the 2022 prompts, which featured the same two task types, each labeled as SN2, and ER2. Two certified human raters of the AP Chinese exam evaluated the writing samples using the College Board's scoring rubrics for both holistic and analytic scoring for three trait scores assessing Task Completion, Delivery, and Language Use. Each student response received both holistic and analytic trait/domain-specific scores ranging from 0 to 6 (Song &amp; Tang, 2025).\n\n**LLMs Trained for Automated Scoring:**\nIn alignment with the development of LLMs, ChatGPT 3.5 was first used to score all 120 essays and other AI engines were sequentially explored when new versions or new engines were released. Data collection took approximately one and a half years. This study incorporated ten AI raters: ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 2.0, Gemini Advanced 1.5 Pro, DeepSeek V3, and DeepSeek R1. These LLMs are selected based on their popularity and demonstrated expertise in processing text data and reasoning capabilities.\n\n- ChatGPT 3.5: general-purpose tasks, casual writing, and basic coding.\n- ChatGPT 4: better at technical problem-solving and creative content; generally outperforms ChatGPT 3.5 in language understanding, with ChatGPT 4 Turbo offering enhanced context handling.\n- ChatGPT 4o: excels at conversations.\n- OpenAI o1: specializes in advanced STEM applications and debugging.\n- Claude 3.5 Sonnet: competitive, often cited in safety-focused evaluations, technical coding, and natural-sounding content.\n- Gemini 1.5 and 1.5 Pro: good at long-context tasks.\n- Gemini 2.0: selected to reflect the latest advancements in Google's LLMs, which feature enhanced language understanding and improved reasoning for research, education, and multimedia analysis.\n- DeepSeek V3: uses the Mixture-of-Experts model, optimized for general-purpose tasks, including natural language understanding, text generation, and conversational AI.\n- DeepSeek R1: excels in reasoning; specifically tailored for tasks that require deep reasoning, complex problem-solving, and advanced analytical capabilities.\n\nBefore scoring, human rater R1, a certified AP Chinese Language and Culture Exam rater, trained 10 AI engines using AI training protocols designed for evaluating student samples (see Appendix A for an example protocol). As Lee et al. (2024) emphasized, human expert ratings are essential for generating benchmark data that align AI scoring with educational standards. To ensure valid AI rater performance, human rater R1 not only provided training examples drawn from the College Board website and previously scored samples but also offered guidance on applying a holistic scoring approach. AI raters were instructed to prioritize three traits: Task Completion, followed by Delivery and Language Use, in line with official rubrics. In total, 2 human raters and 10 AI raters scored 120 essays across four writing tasks.\n\n**Analysis:**\nUsing the analytic and holistic scores for the essays, this study investigates scoring accuracy, reliability, and rater effects.\n\n- **Quadratic Weighted Kappa (QWK; Cohen, 1960; 1968)** was computed to evaluate the scoring accuracy of AI raters against the gold standards of human ratings. QWK was computed for each AI against each human rater. AI raters' QWK were compared with the QWK measures from two human raters which were used as the baseline for comparison.\n\n- **Ensemble models:** Multiple ensemble models were explored by removing the worst performing LLMs from the ensemble.\n  - AI11 = average of all 10 AI raters\n  - AI12 = AI11 minus Gemini 2.0 (A7)\n  - AI13 = AI12 minus Gemini 1.5 Pro (A9)\n  - AI14 = AI13 minus OpenAI o1 (A6)\n  - AI15 = AI14 minus DeepSeek V3 (A8)\n  - AI16 = AI15 minus ChatGPT 4.0 (A2) and Gemini 1.5 (A4)\n\n- **Cronbach Alpha** was computed for each AI and human ratings across the three trait scores and holistic scores as a measure of intra-rater consistency.\n\n- **Many-Facet Rasch Model (FACETS):** The FACET model for the rating scale model (Andrich, 1978) is given in equation 1:\n\n  ln(P_jn(x=k) / P_jn(x=k-1)) = θ_j − τ_i − δ_n − β_k\n\n  where θ_j is student j's latent ability estimate, τ_i is rater i's rater effect estimate, δ_n is essay n's difficulty level, β_k is the threshold parameter for score category k. The rating scale version of the FACET model is used (Eckes, 2015; Myford &amp; Wolfe, 2003, 2004), assuming the threshold parameters are the same across all items.\n\n  Facets investigated:\n  - Students: 30\n  - Essays: 4 (SN1, ER1, SN2, ER2)\n  - Raters: 2 human (R1, R2) + 10 AI raters (A1=ChatGPT 3.5, A2=ChatGPT 4, A3=ChatGPT 4o, A4=Gemini 1.5, A5=Claude 3.5 Sonnet, A6=OpenAI o1, A7=Gemini 2.0, A8=DeepSeek V3, A9=Gemini 1.5 Pro, A10=DeepSeek R1)\n\n  Rater effects (severity/leniency) quantified by rater parameter τ_i. Wright maps used to illustrate relative difficulty of essay traits, rater effects, and student ability on the common scale.\n\n  **Fit indices:** Infit mean square (consistency of rating scale use across students and criteria) and outfit mean square (outlier score patterns). Expected value = 1. Good fit range: 0.5–1.5 (Linacre, 2003; Eckes, 2009). Stringent criteria applied in this study: 0.7 and 1.3 (Bond &amp; Fox, 2007; Bond et al., 2021; McNamara, 1996; Muller, 2020; Wright &amp; Linacre, 1994).\n\n---\n\n### RESULTS\n\n#### Scoring Accuracy\n\n**Table 1 — Holistic Scoring Accuracy (QWK) for AI Raters against Each Human Rater:**\n\nHuman-human QWK baseline: SN1=0.683, SN2=0.565, ER1=0.684, ER2=0.874\n\n| Rater | SN1-R1 | SN1-R2 | SN2-R1 | SN2-R2 | ER1-R1 | ER1-R2 | ER2-R1 | ER2-R2 |\n|---|---|---|---|---|---|---|---|---|\n| R1/R2 (human-human) | 0.683 | | 0.565 | | 0.684 | | 0.874 | |\n| A1 ChatGPT 3.5 | 0.549 | 0.409 | 0.610 | 0.538 | 0.442 | 0.516 | 0.632 | 0.560 |\n| A2 ChatGPT 4 | 0.392 | 0.350 | 0.440 | 0.394 | 0.558 | 0.459 | 0.827 | 0.834 |\n| A3 ChatGPT 4o | 0.626 | 0.620 | 0.526 | 0.393 | 0.741 | 0.475 | 0.865 | 0.898 |\n| A4 Gemini 1.5 | 0.333 | 0.181 | 0.388 | 0.276 | 0.610 | 0.558 | 0.435 | 0.463 |\n| A5 Claude 3.5 | 0.708 | 0.576 | 0.657 | 0.570 | 0.672 | 0.726 | 0.804 | 0.896 |\n| A6 OpenAI o1 | 0.422 | 0.302 | 0.557 | 0.369 | 0.543 | 0.304 | 0.656 | 0.584 |\n| A7 Gemini 2.0 | 0.201 | 0.131 | 0.319 | 0.199 | 0.289 | 0.143 | 0.716 | 0.619 |\n| A8 DeepSeek V3 | 0.378 | 0.233 | 0.610 | 0.439 | 0.619 | 0.448 | 0.664 | 0.667 |\n| A9 Gemini 1.5 Pro | 0.267 | 0.169 | 0.698 | 0.576 | 0.631 | 0.640 | 0.590 | 0.537 |\n| A10 DeepSeek R1 | 0.579 | 0.522 | 0.417 | 0.293 | 0.453 | 0.368 | 0.727 | 0.703 |\n| A11 Ensemble (all 10) | 0.606 | 0.426 | 0.605 | 0.476 | 0.776 | 0.614 | 0.779 | 0.745 |\n| A12 = A11 - A7 | 0.630 | 0.474 | 0.720 | 0.535 | 0.783 | 0.671 | 0.805 | 0.764 |\n| A13 = A12 - A9 | 0.689 | 0.502 | 0.630 | 0.516 | 0.751 | 0.669 | 0.767 | 0.753 |\n| A14 = A13 - A6 | 0.692 | 0.551 | 0.693 | 0.474 | 0.733 | 0.623 | 0.837 | 0.809 |\n| A15 = A14 - A8 | 0.665 | 0.513 | 0.630 | 0.516 | 0.681 | 0.685 | 0.815 | 0.790 |\n| A16 = A15 - A2 - A4 | 0.688 | 0.588 | 0.675 | 0.563 | 0.647 | 0.675 | 0.812 | 0.790 |\n\nKey findings: For SN1, ChatGPT 4o yielded the highest QWK with R2; Claude 3.5 yielded the highest QWK with R1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters. For ER1, ChatGPT 4o yielded the highest QWK with R1; Claude 3.5 yielded the highest QWK with R2. For ER2, ChatGPT 4o yielded the highest QWK with both human raters. In general, one AI rater achieved higher QWK with one human rater than human-human QWK on every item.\n\n**Table 2 — Analytic (Task Completion) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.715, SN2=0.808, ER1=0.776, ER2=0.915. ChatGPT 4o yielded the highest QWK with both human raters on SN1 and ER2 as well as SN2 with R1. Claude 3.5 yielded the highest QWK with R2 on both SN2 and ER1. Human-human QWK was consistently higher than AI-human QWK on each of the analytic scores.\n\n**Table 3 — Analytic (Delivery) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.685, SN2=0.588, ER1=0.763, ER2=0.950. ChatGPT 4o yielded the highest QWK with both human raters on ER2. Claude 3.5 yielded the highest QWK with each of the two raters on both SN1 and ER1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters. AI-human QWK was consistently higher than human-human QWK on SN tasks and ER1 task except ER2.\n\n**Table 4 — Analytic (Language Use) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.832, SN2=0.488, ER1=0.783, ER2=0.939. ChatGPT 4.0 and 4o yielded the highest QWK with R1 and R2 respectively on ER2. Gemini 1.5 yielded the highest QWK with both raters on ER1. Claude 3.5 yielded the highest QWK with both raters on SN1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters.\n\n**Summary:** No AI rater was always the best performer across all tasks. In general, ChatGPT 4o, Claude 3.5, and Gemini 1.5 Pro yielded the highest performing AI raters depending on the scoring tasks. Ensemble models were able to occasionally improve the scoring accuracy for a specific essay compared with the standalone LLMs.\n\n#### Intra-Rater Consistency (Table 5)\n\nCronbach Alpha values:\n\n| Rater | Holistic (4 items) | Task Completion (4) | Delivery (4) | Language Use (4) | Analytic (12) | SN (6) | ER (6) |\n|---|---|---|---|---|---|---|---|\n| R1 | 0.71 | 0.73 | 0.67 | 0.58 | 0.90 | 0.89 | 0.91 |\n| R2 | 0.81 | 0.81 | 0.78 | 0.77 | 0.94 | 0.95 | 0.93 |\n| A1 ChatGPT 3.5 | 0.71 | 0.66 | 0.73 | 0.72 | 0.92 | 0.91 | 0.89 |\n| A2 ChatGPT 4 | 0.66 | 0.64 | 0.64 | 0.58 | 0.89 | 0.92 | 0.79 |\n| A3 ChatGPT 4o | 0.81 | 0.80 | 0.79 | 0.58 | 0.91 | 0.90 | 0.90 |\n| A4 Gemini 1.5 | 0.46 | 0.60 | 0.63 | 0.58 | 0.88 | 0.90 | 0.86 |\n| A5 Claude 3.5 | 0.80 | 0.82 | 0.78 | 0.74 | 0.94 | 0.95 | 0.89 |\n| A6 OpenAI o1 | 0.67 | 0.62 | 0.50 | 0.56 | 0.87 | 0.85 | 0.79 |\n| A7 Gemini 2.0 | 0.35 | 0.26 | 0.28 | 0.30 | 0.72 | 0.67 | 0.80 |\n| A8 DeepSeek V3 | 0.62 | 0.69 | 0.51 | 0.58 | 0.87 | 0.92 | 0.82 |\n| A9 Gemini 1.5 Pro | 0.61 | 0.61 | 0.60 | 0.41 | 0.85 | 0.86 | 0.81 |\n| A10 DeepSeek R1 | 0.68 | 0.72 | 0.73 | 0.67 | 0.91 | 0.89 | 0.89 |\n\nThe top performing AI raters, either ChatGPT 4o or Claude 3.5, still yielded the highest intra-rater consistency across different tasks. The intra-rater consistency for human rater R2 was consistently higher than that for human rater R1. The intra-rater consistency for the best performing AI raters was about the same or higher than R2 except for analytic scores of Language Use and ER essay.\n\n#### AI Rater Effects\n\n**Table 6 — Mean Holistic and Analytic Scores Assigned by Each Rater:**\n\nKey patterns: Human rater R2 assigned higher mean scores across all rating tasks compared with R1. Gemini 2.0 assigned the lowest mean scores on majority of the rating tasks. ChatGPT 3.5 and ChatGPT 4 produced the highest mean scores on majority of the rating tasks.\n\nSelected mean scores (Holistic):\n- SN1: R1=3.70, R2=4.10, A1=3.53, A2=3.03, A3=3.73, A4=2.83, A5=3.80, A6=3.17, A7=2.60, A8=3.67, A9=3.33, A10=3.50\n- ER1: R1=3.30, R2=3.83, A1=4.30, A2=3.43, A3=2.93, A4=3.43, A5=3.50, A6=2.90, A7=2.37, A8=3.10, A9=3.80, A10=3.57\n- SN2: R1=3.23, R2=3.70, A1=3.50, A2=2.97, A3=2.70, A4=2.90, A5=3.10, A6=2.87, A7=2.00, A8=3.47, A9=3.47, A10=3.37\n- ER2: R1=3.73, R2=4.07, A1=3.13, A2=3.93, A3=3.77, A4=3.60, A5=3.87, A6=3.10, A7=3.10, A8=3.47, A9=3.20, A10=3.50\n\n**Wright Maps (Figures 1–5):**\n\n- **Figure 1 caption:** \"The Wright Map for the Holistic Scores\" — For holistic scoring, SN2 was the most difficult essay, while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater (consistent with lowest mean scores) while R2 and ChatGPT 3.5 were more lenient raters.\n\n- **Figure 2 caption:** \"The Wright Map for the Analytic Scores\" — For analytic scoring across all three traits, SN2 was still the most difficult essay, ER2 was easiest, SN1 was second most difficult. Gemini 2.0 was the most stringent rater; two human raters were the most lenient. Among the three traits, Language Use was the most difficult, while Task Completion was the easiest.\n\n- **Figure 3 caption:** \"The Wright Map for the Analytic Scores-Task Completion\" — SN2 was still the most difficult essay while SN1 was the easiest. ER1 and ER2 had about the same difficulty. OpenAI o1 was the most stringent rater while two human raters were the most lenient raters. R1 was more lenient than R2 on Task Completion trait scoring.\n\n- **Figure 4 caption:** \"The Wright Map for the Analytic Scores-Delivery\" — SN2 was still the most difficult essay while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater while R2 was the most lenient raters. R1 was the second most lenient rater like Claude 3.5 and Gemini 1.5 Pro on Delivery trait scoring.\n\n- **Figure 5 caption:** \"The Wright Map for the Analytic Scores-Language Use\" — SN2 was still the most difficult essay while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater while rater 2 was the most lenient raters. R1 was the second most lenient rater on Language Use trait scoring.\n\n**Table 7 — Rater Parameter Estimates for Holistic Scoring:**\n\n| Rater | Rater Par | SE | Infit MS | Outfit MS |\n|---|---|---|---|---|\n| R2 | -0.81 | 0.11 | 0.60 | 0.60 |\n| ChatGPT 3.5 | -0.37 | 0.11 | 1.36 | 1.36 |\n| Claude 3.5 Sonnet | -0.30 | 0.11 | 1.01 | 1.01 |\n| R1 | -0.20 | 0.11 | 0.58 | 0.59 |\n| DeepSeek R1 | -0.18 | 0.11 | 1.37 | 1.41 |\n| Gemini 1.5 Pro | -0.14 | 0.11 | 1.41 | 1.41 |\n| DeepSeek V3 | -0.10 | 0.11 | 1.07 | 1.08 |\n| ChatGPT 4 | 0.02 | 0.11 | 0.91 | 0.92 |\n| ChatGPT 4o | 0.10 | 0.11 | 0.85 | 0.84 |\n| Gemini 1.5 | 0.23 | 0.11 | 0.85 | 0.88 |\n| OpenAI o1 | 0.50 | 0.11 | 0.70 | 0.69 |\n| Gemini 2.0 | 1.25 | 0.11 | 1.22 | 1.29 |\n\nKey findings: Gemini 2.0 was an extreme severe rater (logit = 1.25). ChatGPT 4 was the most neutral rater (parameter ≈ 0). Using cut value of 0.3: all AI raters did not have severe rater effects except ChatGPT 3.5 (-0.37, lenient) and OpenAI o1 (0.5, harsh). The two human raters had the smallest infit and outfit mean squares (both &lt; 0.7), indicating potential central tendency effect. DeepSeek R1, ChatGPT 3.5, and Gemini 1.5 Pro had infit and outfit mean squares &gt; 1.3, indicating potential misfit.\n\n**Table 8 — Rater Parameter Estimates for Analytic Scoring:**\n\n| Rater | Rater Par | SE | Infit MS | Outfit MS |\n|---|---|---|---|---|\n| R2 | -0.55 | 0.06 | 0.73 | 0.73 |\n| R1 | -0.47 | 0.06 | 0.83 | 0.84 |\n| ChatGPT 3.5 | -0.31 | 0.06 | 1.21 | 1.20 |\n| Gemini 1.5 Pro | -0.29 | 0.06 | 1.19 | 1.19 |\n| Claude 3.5 Sonnet | -0.17 | 0.06 | 0.97 | 0.97 |\n| ChatGPT 4 | -0.10 | 0.06 | 0.88 | 0.89 |\n| DeepSeek V3 | 0.05 | 0.06 | 1.18 | 1.18 |\n| DeepSeek R1 | 0.10 | 0.06 | 1.15 | 1.18 |\n| ChatGPT 4o | 0.11 | 0.06 | 1.06 | 1.05 |\n| Gemini 1.5 | 0.30 | 0.06 | 0.84 | 0.87 |\n| OpenAI o1 | 0.57 | 0.06 | 0.69 | 0.69 |\n| Gemini 2.0 | 0.76 | 0.06 | 1.21 | 1.26 |\n\nKey findings: Gemini 2.0 was severe (logit = 0.76). DeepSeek V3 was the most neutral rater (parameter ≈ 0.05). All AI raters did not have severe rater effects except OpenAI o1 (0.5, harsh). OpenAI o1 had the least infit and outfit mean squares at the borderline (0.69). No infit and outfit mean squares were larger than 1.3 for any rater.\n\n**Table 9 — Rater Parameter Estimates for Analytic Scoring — Task Completion:**\nTwo human raters were most lenient (R1: -0.51, R2: -0.36). OpenAI o1 was the most severe rater (logit = 0.61). ChatGPT 4 and Claude 3.5 were more neutral (absolute value &lt; 0.1). All AI raters did not have severe rater effects except OpenAI o1 (0.5), Gemini 1.5 (0.53), and Gemini 2.0 (0.38). No infit or outfit mean squares were &lt; 0.7 or &gt; 1.3.\n\n**Table 10 — Rater Parameter Estimates for Analytic Scoring — Delivery:**\nHuman rater R2 was most lenient (-0.63). Gemini 2.0 was most severe (rater parameter = 1.03). DeepSeek V3 was most neutral (-0.06). Using absolute cut value of 0.3, OpenAI o1 was a harsh rater (0.68), while Claude 3.5 was slightly lenient (-0.35). No infit and outfit mean squares were &lt; 0.7 or &gt; 1.3.\n\n**Table 11 — Rater Parameter Estimates for Analytic Scoring — Language Use:**\nHuman rater R2 was most lenient (-0.74), R1 second most lenient (-0.63). Gemini 2.0 was most severe (1.06). DeepSeek R1, ChatGPT 4 and Gemini 1.5 were more neutral (absolute parameter ≈ 0.1). Using absolute cut value of 0.3: DeepSeek V3 (0.54), OpenAI o1 (0.49), and ChatGPT 4o (0.40) were slightly harsh raters; Gemini 1.5 Pro (-0.37) and ChatGPT 3.5 (-0.55) were slightly lenient. OpenAI o1 had infit and outfit mean squares &lt; 0.7 (slight central tendency); ChatGPT 3.5 and Gemini 2.0 yielded infit and outfit mean squares &gt; 1.3 (slight misfit).\n\n---\n\n### SUMMARY AND DISCUSSION (complete)\n\nThis study aims to examine the rater effects of LLM-based AI raters in automated scoring. To illustrate the methods for exploring AI rater effects, this study investigated the use of LLMs for automated holistic and analytic scoring using a fully crossed rating design. Ten LLMs were compared including ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3, and DeepSeek R1 against two human expert raters in scoring two types of writing tasks for the AP Chinese exams. The holistic and analytic score accuracy of LLMs compared with human raters were evaluated in terms of QWK. Intra-rater consistency across essays was compared in terms of Cronbach Alpha. Rater effects of LLMs were evaluated and compared with human raters using the Many FACET Rasch model.\n\nFor Research Question 1 related to the AI raters' accuracy, for holistic scoring, ChatGPT 4o, Claude 3.5, and Gemini 1.5 Pro yielded the highest scoring accuracy against either human rater. ChatGPT 4o performed the best on ER items, while Gemini 1.5 Pro excelled on SN items while Claude 3.5 showed strong performance on both SN and ER items. These three LLMs turned out to be the best performing models in analytic scoring as well. For Task Completion, ChatGPT 4o performed the best for SN and ER2 items while Claude 3.5 and Gemini 1.5 Pro performed the best on SN2 and ER1 essays. For Delivery, Claude 3.5 performed the best on SN1 and ER1 while ChatGPT 4o and Gemini 1.5 Pro performed the best on ER2 and SN2 respectively. For the Language Use trait, ChatGPT 4, 4o, and Gemini 1.5 were the top performers on ER essays while Claude 3.5 and Gemini 1.5 Pro were the best performers for SN essays. In general, QWKs for the best performing AI raters were higher than those between two human raters for holistic scoring. However, human-human QWK were higher on analytic scoring than AI QWKs. QWKs for analytic scores were higher than those for holistic scoring.\n\nFor Research Question 2 related to the AI raters' intra-rater consistency, ChatGPT 4o yielded the highest intra-rater consistency for the holistic scores, the analytic scores on the Delivery trait, and the ER items. On the other hand, Claude 3.5 yielded the highest consistency for the analytic scores, analytic scores on the Task Completion and Language Use traits as well as the SN items. Human rater R2 yielded higher scoring consistency compared with R1. The best performing AI raters' intra-rater consistency were about the same as those for the best performing human rater except on ER essays and analytic scores on Language Use with slightly lower consistency.\n\nFor Research Questions 3 on the rater effects, human raters in general were more lenient. Gemini 2.0 turned out to be a harsh rater on most scoring tasks. ChatGPT 3.5 turned out to be a lenient rater in 3 out of 5 scoring analyses with DeepSeek V3 and Gemini 1.5 Pro as the two other lenient raters. Whether an AI rater was more neutral raters depends on the task. There was no evident central tendency effects for the AI raters. However, the two human raters displayed some minor central tendency effect in holistic scoring. As Wolfe (2004) pointed out, the rater effects estimated in the FACET Rasch model was scaled to a mean of 0. If the number of raters included in the comparison differs, the estimated rater effect may be different.\n\nThe results in general support the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high scoring accuracy, better intra-rater consistency, and less rater effects. However, there were no AI raters which consistently performed the best. Some further explorations will be conducted to better understand the AI rater scoring logic. The findings of this study provide insights into the strengths and limitations of AI raters compared to human raters using the data in the study.\n\n---\n\n### LIMITATIONS (complete)\n\nThe limitations of the study lies in the sample size, the content domain, the type and the number of essays. There were only 30 students who participated in this experiment. The FACET software manual states a sample size of 30 as a minimum sample size. However, as the FACET Rasch model is an item response theory based latent trait model, a larger sample size would be expected even though the standard error of the rater parameter estimates was relatively small in the current study. Further, the content of the tasks was related to the AP Chinese exam. Whether the findings from this study is generalizable to other content domains such as English writing, reading, science, and math constructed-response items awaits further exploration. In addition, only two items types: SN and ER were included in the experiments, with a total of only 4 items. Other task types and traits for analytic scoring should be examined in future studies. The last limitation is related to the prompting methods for automated scoring using LLMs. The current study used a few-shot methods. Other methods should be explored in future studies including Chain-of-Thought and other fine-tuning methods.\n\n---\n\n### CONCLUSION (final paragraph of Summary and Discussion)\n\nIn summary, this study assessed the scoring accuracy, intra-rater consistency of AI and human holistic and analytic ratings, and estimated the AI rater effects. It demonstrated the methods that can be used to examine AI rater performance, in particular, the use of the Many FACET Rasch model to evaluate rater severity/leniency and central tendency effects. This study provided empirical evidence to inform the adoption of LLM-based AI raters for automated holistic and analytic scoring. It is highlighted that when LLMs are used for automated scoring, the methods demonstrated in this study could be the starting point for such evaluation.\n\n---\n\n### ALL FIGURE CAPTIONS\n\n- **Figure 1:** \"The Wright Map for the Holistic Scores\"\n- **Figure 2:** \"The Wright Map for the Analytic Scores\"\n- **Figure 3:** \"The Wright Map for the Analytic Scores-Task Completion\"\n- **Figure 4:** \"The Wright Map for the Analytic Scores-Delivery\"\n- **Figure 5:** \"The Wright Map for the Analytic Scores-Language Use\"\n\n### ALL TABLE CAPTIONS\n\n- **Table 1:** \"Holistic Scoring Accuracy (QWK) for AI Raters against Each Human Rater\"\n- **Table 2:** \"Analytic (Task Completion) Scoring Accuracy (QWK) for AI Raters against Each Human Rater\"\n- **Table 3:** \"Analytic (Delivery) Scoring Accuracy (QWK) for AI Raters against Each Human Rater\"\n- **Table 4:** \"Analytic (Language Use) Scoring Accuracy (QWK) for AI Raters against Each Human Rater\"\n- **Table 5:** \"Intra-Rater Consistency\"\n- **Table 6:** \"Mean Holistic and Analytic Scores Assigned by Each Rater\"\n- **Table 7:** \"Rater Parameter Estimates for Holistic Scoring\"\n- **Table 8:** \"Rater Parameter Estimates for Analytic Scoring\"\n- **Table 9:** \"Rater Parameter Estimates for Analytic Scoring-Task Completion\"\n- **Table 10:** \"Rater Parameter Estimates for Analytic Scoring-Delivery\"\n- **Table 11:** \"Rater Parameter Estimates for Analytic Scoring-Language Use\"\n- **Table B.1 (Appendix B):** \"Standard Deviation of the Holistic and Analytic Scores Assigned by Each Rater\"\n\n---\n\n### KEY IMPLEMENTATION DETAILS\n\n- **Prompting method:** Few-shot prompting with training examples. Human rater R1 (certified AP Chinese examiner) designed and executed AI training protocols (Appendix A shows example for SN1 essay type).\n- **Scoring rubric:** College Board AP Chinese rubric, 0–6 scale, holistic plus 3 analytic traits (Task Completion, Delivery, Language Use).\n- **Training design:** AI raters were given the task prompt, scoring rubric, and student writing samples at multiple score levels as examples before scoring.\n- **Scoring design:** Fully crossed rating design — all 12 raters (2 human + 10 AI) scored all 120 essays (30 students × 4 tasks).\n- **Analysis software:** FACET software (Linacre, 2024), Version 3.87.0.\n- **No ablation studies** were conducted in the traditional ML sense; instead, ensemble models were constructed by progressively removing worst-performing LLMs.\n- **Data collection period:** Approximately one and a half years (sequential addition of models as released).&lt;/result>\n&lt;usage>&lt;total_tokens>49422&lt;/total_tokens>&lt;tool_uses>7&lt;/tool_uses>&lt;duration_ms>242575&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---


### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "495da358-64d6-417e-a074-323b07c5fc94",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 64 · 2026-05-21T16:41:53.761Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T16:41:53.761Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


## Round 3

## Round 3

21 recorded events


### User

_source line 65 · 2026-05-21T16:41:53.781Z_

&lt;task-notification>
&lt;task-id>aed1d3e555792ca7c&lt;/task-id>
&lt;tool-use-id>toolu_01V46oYv3iHYpqdayCFc12tH&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/aed1d3e555792ca7c.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Fetch paper: wang2025mfrm_llm" completed&lt;/summary>
&lt;result>Here is the complete extracted text from arXiv:2505.18486.

---

## Paper: "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model"

**Authors:** Hong Jiao (University of Maryland, College Park), Dan Song, Won-Chan Lee (University of Iowa)

---

### ABSTRACT

Large language models (LLMs) have been widely explored for automated scoring in low-stakes assessment to facilitate learning and instruction. Empirical evidence related to which LLM produces the most reliable scores and induces least rater effects needs to be collected before the use of LLMs for automated scoring in practice. This study compared ten LLMs (ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3, and DeepSeek R1) with human expert raters in scoring two types of writing tasks. The accuracy of the holistic and analytic scores from LLMs compared with human raters was evaluated in terms of Quadratic Weighted Kappa. Intra-rater consistency across prompts was compared in terms of Cronbach Alpha. Rater effects of LLMs were evaluated and compared with human raters using the Many-Facet Rasch model. The results in general supported the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high scoring accuracy, better rater reliability, and less rater effects.

---

### 1. INTRODUCTION (Complete text)

**Paragraph 1:**
Performance assessment tasks, including essays and other types of constructed-response (CR) items are commonly used for assessing high-order thinking skills such as synthesizing information from multiple sources, critical evaluations, and evidence-based reasoning. These assessment formats are commonly employed in formative classroom assessments to facilitate instruction and learning as well as in high-stakes summative assessments for accountability and admission decisions. While the score represents a key form of feedback, the scoring of such assessment tasks is often costly, time-consuming, and error prone due to the subjectivity of human raters.

**Paragraph 2:**
Automated scoring of performance items is an efficient and scientifically validated technology designed to complement and enhance human scoring (Shermis, 2015). For example, automating the scoring of the National Assessment of Educational Progress (NAEP) CR items could yield significant cost saving of 70% for reading and 40% for math (Justice &amp; Palermo, 2020). As one of the most successful applications of AI technology in educational assessments, the progress in automated scoring is aligned closely with the advances in machine learning and natural language processing (NLP). Though research on automated scoring started with the pioneering work of Page (1966; 2003), recent advances in AI technology have made breakthrough in automated scoring.

**Paragraph 3:**
Automated scoring can be categorized into two main approaches: feature-based and deep learning-based (Haller et al., 2022), with the latter further classified into neural network, small language model (SLM), and large language model (LLM) based approaches. Feature-based approaches rely on the extracted length, prompt, readability, syntactic, semantic, lexical, and discourse features (Ke &amp; Ng, 2019; Uto et al., 2020) and supervised machine learning models. Deep learning-based approaches use word embeddings (Word2Vec, GloVe) and context embeddings from small language models (SLMs) such as BERT, deBERTa based on transformer (Vaswani et al., 2017) and large language models (LLMs) such as GPT, Claude, and Gemini.

**Paragraph 4:**
Developing feature-based or SLM-based automated scoring systems often requires foundational skills in supervised machine learning, NLP, and deep learning. This dramatically reduces the accessibility of automated scoring to classroom learners, teachers, and assessment developers. However, with the swift emerging of more capable LLMs, automated scoring techniques are becoming increasingly accessible to non-technical users who can fully leverage the LLM technology to revamp their routine scoring practices, with enhanced efficiency and accuracy.

**Paragraph 5:**
With the advances in Generative AI or Chatbots, LLMs have been explored for automated scoring in education assessments. LLMs have demonstrated unprecedented potential in automated scoring of essays and CR items in educational assessments (Latif &amp; Zhai, 2024; Lee et al., 2024; Yancey et al., 2023; Yang et al., 2025). In low-stakes assessment programs, three commonly used models are ChatGPT by OpenAI, Claude by Anthropic, and Google Gemini. Recent studies have explored the use of GPT models, such as GPT 3.5 (Bui &amp; Barrot, 2024; Mizumoto &amp; Eguchi, 2023; Parker et al., 2023; Wijekumar et al., 2024) and GPT 4 (Kortemeyer, 2024) in automated scoring. Furthermore, several studies have compared the performance of GPT 3.5 and GPT 4 (Kim &amp; Jo, 2024; Tate et al., 2024) as well as GPT and Llama3 (Kundu &amp; Barbosa, 2024). Pack et al. (2024) compared PaLM 2, Claude 2, and GPT 3.5 and GPT 4, concluding that GPT 4 outperformed the others. Almost all studies on using LLMs for automated scoring purely focused on scoring accuracy, little is known about the potential rater effects of these LLM scoring engines.

**Paragraph 6:**
Rater effects (Myford &amp; Wolfe, 2003, 2004; Saal, Downey, &amp; Lahey, 1980) refer to different types of inconsistencies in ratings when human raters assign scores to test-takers' constructed responses to performance tasks such as essays or CR items in educational assessments. Rater effects may occur due to raters' personal backgrounds, preferences, inaccurate interpretations of the scoring rubrics, inappropriate conceptualization of the target test-takers' population, and their idiosyncratic traits that may impact their accuracy and consistency in assigning scores to assessment items. Rater effects can be classified into different categories. Some common rater effects include rater severity/leniency and centrality. When a rater assigns scores to students' responses to a performance task consistently lower than other raters, this rater effect is noted as rater severity. When rater severity is present, students' true scores may be underestimated if such rater effect is ignored. On the other hand, when a rater assigns scores to students' responses consistently higher than other raters, this rater effect is noted as rater leniency. When rater leniency is present, students' true scores may be overestimated if such rater effect is not accounted for. Further, some raters may consistently assign scores in the middle of the score scale and not assign high scores or low scores regardless of the ability levels. This central tendency or centrality effect will introduce score errors for students whose true scores lie at the two ends of the score scale. Such rater effects are as severe as score accuracy as they may compromise the fairness, reliability, and validity of the assigned scores. Though in operational rating sessions, different strategies would be implemented to minimize rater effects such as standardized rubrics, comprehensive rater training and calibration, in-session and post-session quality control of ratings, or assigning multiple raters to each rating tasks, rater effects need to be tracked as a source of validity evidence.

**Paragraph 7 (Research Questions / Contribution Statement):**
Each LLM has its own strengths and features that may cater to different scoring needs and applications. Like human raters, AI raters may bear different degrees of rater effects. Thus, it is worthwhile to compare the ratings from different scoring engines and understand the potential AI rater effects of each LLM. Thus, this study aims to investigate the AI rater effects in addition to rating accuracy and consistency compared with human raters of essay scoring. The AI raters investigated in this study include ten commonly used LLMs from GPT, Gemini, and Claude families and some recent LLMs such as DeepSeek. The research questions for the study include:
1. How accurate are LLM raters compared with human raters?
2. How consistent or reliable are LLM raters compared with human raters?
3. What are the LLM rater effects compared with human raters?

---

### METHODS

**Overview:**
This study conducts a series of psychometric analyses to investigate the AI raters' scoring accuracy and consistency, as well as uses the Many-Facet Rasch measurement model (Linacre, 1989, 1994, 2024; Wright &amp; Masters, 1982; Wright &amp; Stone, 1979) to investigate and compare rater effects between AI raters and human raters in a large-scale writing assessment.

**Data:**
A dataset consists of 30 student essays on two types of writing tasks. Each essay was scored by two human raters and ten AI raters, including ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3 and DeepSeek R1. The 30 U.S. college students, enrolled in Mandarin Chinese language courses, included 18 third-year and 12 fourth-year students from a range of majors such as business, humanities, STEM, and diplomacy. Data collection took place over two consecutive days using constructed-response writing prompts from the 2021 and 2022 AP Chinese exams developed by the College Board. On the first day, students completed the 2021 prompts, which included one story narration (SN1) task and one email response (ER1) task. On the second day, they responded to the 2022 prompts, which featured the same two task types, each labeled as SN2, and ER2. Two certified human raters of the AP Chinese exam evaluated the writing samples using the College Board's scoring rubrics for both holistic and analytic scoring for three trait scores assessing Task Completion, Delivery, and Language Use. Each student response received both holistic and analytic trait/domain-specific scores ranging from 0 to 6 (Song &amp; Tang, 2025).

**LLMs Trained for Automated Scoring:**
In alignment with the development of LLMs, ChatGPT 3.5 was first used to score all 120 essays and other AI engines were sequentially explored when new versions or new engines were released. Data collection took approximately one and a half years. This study incorporated ten AI raters: ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 2.0, Gemini Advanced 1.5 Pro, DeepSeek V3, and DeepSeek R1. These LLMs are selected based on their popularity and demonstrated expertise in processing text data and reasoning capabilities.

- ChatGPT 3.5: general-purpose tasks, casual writing, and basic coding.
- ChatGPT 4: better at technical problem-solving and creative content; generally outperforms ChatGPT 3.5 in language understanding, with ChatGPT 4 Turbo offering enhanced context handling.
- ChatGPT 4o: excels at conversations.
- OpenAI o1: specializes in advanced STEM applications and debugging.
- Claude 3.5 Sonnet: competitive, often cited in safety-focused evaluations, technical coding, and natural-sounding content.
- Gemini 1.5 and 1.5 Pro: good at long-context tasks.
- Gemini 2.0: selected to reflect the latest advancements in Google's LLMs, which feature enhanced language understanding and improved reasoning for research, education, and multimedia analysis.
- DeepSeek V3: uses the Mixture-of-Experts model, optimized for general-purpose tasks, including natural language understanding, text generation, and conversational AI.
- DeepSeek R1: excels in reasoning; specifically tailored for tasks that require deep reasoning, complex problem-solving, and advanced analytical capabilities.

Before scoring, human rater R1, a certified AP Chinese Language and Culture Exam rater, trained 10 AI engines using AI training protocols designed for evaluating student samples (see Appendix A for an example protocol). As Lee et al. (2024) emphasized, human expert ratings are essential for generating benchmark data that align AI scoring with educational standards. To ensure valid AI rater performance, human rater R1 not only provided training examples drawn from the College Board website and previously scored samples but also offered guidance on applying a holistic scoring approach. AI raters were instructed to prioritize three traits: Task Completion, followed by Delivery and Language Use, in line with official rubrics. In total, 2 human raters and 10 AI raters scored 120 essays across four writing tasks.

**Analysis:**
Using the analytic and holistic scores for the essays, this study investigates scoring accuracy, reliability, and rater effects.

- **Quadratic Weighted Kappa (QWK; Cohen, 1960; 1968)** was computed to evaluate the scoring accuracy of AI raters against the gold standards of human ratings. QWK was computed for each AI against each human rater. AI raters' QWK were compared with the QWK measures from two human raters which were used as the baseline for comparison.

- **Ensemble models:** Multiple ensemble models were explored by removing the worst performing LLMs from the ensemble.
  - AI11 = average of all 10 AI raters
  - AI12 = AI11 minus Gemini 2.0 (A7)
  - AI13 = AI12 minus Gemini 1.5 Pro (A9)
  - AI14 = AI13 minus OpenAI o1 (A6)
  - AI15 = AI14 minus DeepSeek V3 (A8)
  - AI16 = AI15 minus ChatGPT 4.0 (A2) and Gemini 1.5 (A4)

- **Cronbach Alpha** was computed for each AI and human ratings across the three trait scores and holistic scores as a measure of intra-rater consistency.

- **Many-Facet Rasch Model (FACETS):** The FACET model for the rating scale model (Andrich, 1978) is given in equation 1:

  ln(P_jn(x=k) / P_jn(x=k-1)) = θ_j − τ_i − δ_n − β_k

  where θ_j is student j's latent ability estimate, τ_i is rater i's rater effect estimate, δ_n is essay n's difficulty level, β_k is the threshold parameter for score category k. The rating scale version of the FACET model is used (Eckes, 2015; Myford &amp; Wolfe, 2003, 2004), assuming the threshold parameters are the same across all items.

  Facets investigated:
  - Students: 30
  - Essays: 4 (SN1, ER1, SN2, ER2)
  - Raters: 2 human (R1, R2) + 10 AI raters (A1=ChatGPT 3.5, A2=ChatGPT 4, A3=ChatGPT 4o, A4=Gemini 1.5, A5=Claude 3.5 Sonnet, A6=OpenAI o1, A7=Gemini 2.0, A8=DeepSeek V3, A9=Gemini 1.5 Pro, A10=DeepSeek R1)

  Rater effects (severity/leniency) quantified by rater parameter τ_i. Wright maps used to illustrate relative difficulty of essay traits, rater effects, and student ability on the common scale.

  **Fit indices:** Infit mean square (consistency of rating scale use across students and criteria) and outfit mean square (outlier score patterns). Expected value = 1. Good fit range: 0.5–1.5 (Linacre, 2003; Eckes, 2009). Stringent criteria applied in this study: 0.7 and 1.3 (Bond &amp; Fox, 2007; Bond et al., 2021; McNamara, 1996; Muller, 2020; Wright &amp; Linacre, 1994).

---

### RESULTS

#### Scoring Accuracy

**Table 1 — Holistic Scoring Accuracy (QWK) for AI Raters against Each Human Rater:**

Human-human QWK baseline: SN1=0.683, SN2=0.565, ER1=0.684, ER2=0.874

| Rater | SN1-R1 | SN1-R2 | SN2-R1 | SN2-R2 | ER1-R1 | ER1-R2 | ER2-R1 | ER2-R2 |
|---|---|---|---|---|---|---|---|---|
| R1/R2 (human-human) | 0.683 | | 0.565 | | 0.684 | | 0.874 | |
| A1 ChatGPT 3.5 | 0.549 | 0.409 | 0.610 | 0.538 | 0.442 | 0.516 | 0.632 | 0.560 |
| A2 ChatGPT 4 | 0.392 | 0.350 | 0.440 | 0.394 | 0.558 | 0.459 | 0.827 | 0.834 |
| A3 ChatGPT 4o | 0.626 | 0.620 | 0.526 | 0.393 | 0.741 | 0.475 | 0.865 | 0.898 |
| A4 Gemini 1.5 | 0.333 | 0.181 | 0.388 | 0.276 | 0.610 | 0.558 | 0.435 | 0.463 |
| A5 Claude 3.5 | 0.708 | 0.576 | 0.657 | 0.570 | 0.672 | 0.726 | 0.804 | 0.896 |
| A6 OpenAI o1 | 0.422 | 0.302 | 0.557 | 0.369 | 0.543 | 0.304 | 0.656 | 0.584 |
| A7 Gemini 2.0 | 0.201 | 0.131 | 0.319 | 0.199 | 0.289 | 0.143 | 0.716 | 0.619 |
| A8 DeepSeek V3 | 0.378 | 0.233 | 0.610 | 0.439 | 0.619 | 0.448 | 0.664 | 0.667 |
| A9 Gemini 1.5 Pro | 0.267 | 0.169 | 0.698 | 0.576 | 0.631 | 0.640 | 0.590 | 0.537 |
| A10 DeepSeek R1 | 0.579 | 0.522 | 0.417 | 0.293 | 0.453 | 0.368 | 0.727 | 0.703 |
| A11 Ensemble (all 10) | 0.606 | 0.426 | 0.605 | 0.476 | 0.776 | 0.614 | 0.779 | 0.745 |
| A12 = A11 - A7 | 0.630 | 0.474 | 0.720 | 0.535 | 0.783 | 0.671 | 0.805 | 0.764 |
| A13 = A12 - A9 | 0.689 | 0.502 | 0.630 | 0.516 | 0.751 | 0.669 | 0.767 | 0.753 |
| A14 = A13 - A6 | 0.692 | 0.551 | 0.693 | 0.474 | 0.733 | 0.623 | 0.837 | 0.809 |
| A15 = A14 - A8 | 0.665 | 0.513 | 0.630 | 0.516 | 0.681 | 0.685 | 0.815 | 0.790 |
| A16 = A15 - A2 - A4 | 0.688 | 0.588 | 0.675 | 0.563 | 0.647 | 0.675 | 0.812 | 0.790 |

Key findings: For SN1, ChatGPT 4o yielded the highest QWK with R2; Claude 3.5 yielded the highest QWK with R1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters. For ER1, ChatGPT 4o yielded the highest QWK with R1; Claude 3.5 yielded the highest QWK with R2. For ER2, ChatGPT 4o yielded the highest QWK with both human raters. In general, one AI rater achieved higher QWK with one human rater than human-human QWK on every item.

**Table 2 — Analytic (Task Completion) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.715, SN2=0.808, ER1=0.776, ER2=0.915. ChatGPT 4o yielded the highest QWK with both human raters on SN1 and ER2 as well as SN2 with R1. Claude 3.5 yielded the highest QWK with R2 on both SN2 and ER1. Human-human QWK was consistently higher than AI-human QWK on each of the analytic scores.

**Table 3 — Analytic (Delivery) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.685, SN2=0.588, ER1=0.763, ER2=0.950. ChatGPT 4o yielded the highest QWK with both human raters on ER2. Claude 3.5 yielded the highest QWK with each of the two raters on both SN1 and ER1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters. AI-human QWK was consistently higher than human-human QWK on SN tasks and ER1 task except ER2.

**Table 4 — Analytic (Language Use) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.832, SN2=0.488, ER1=0.783, ER2=0.939. ChatGPT 4.0 and 4o yielded the highest QWK with R1 and R2 respectively on ER2. Gemini 1.5 yielded the highest QWK with both raters on ER1. Claude 3.5 yielded the highest QWK with both raters on SN1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters.

**Summary:** No AI rater was always the best performer across all tasks. In general, ChatGPT 4o, Claude 3.5, and Gemini 1.5 Pro yielded the highest performing AI raters depending on the scoring tasks. Ensemble models were able to occasionally improve the scoring accuracy for a specific essay compared with the standalone LLMs.

#### Intra-Rater Consistency (Table 5)

Cronbach Alpha values:

| Rater | Holistic (4 items) | Task Completion (4) | Delivery (4) | Language Use (4) | Analytic (12) | SN (6) | ER (6) |
|---|---|---|---|---|---|---|---|
| R1 | 0.71 | 0.73 | 0.67 | 0.58 | 0.90 | 0.89 | 0.91 |
| R2 | 0.81 | 0.81 | 0.78 | 0.77 | 0.94 | 0.95 | 0.93 |
| A1 ChatGPT 3.5 | 0.71 | 0.66 | 0.73 | 0.72 | 0.92 | 0.91 | 0.89 |
| A2 ChatGPT 4 | 0.66 | 0.64 | 0.64 | 0.58 | 0.89 | 0.92 | 0.79 |
| A3 ChatGPT 4o | 0.81 | 0.80 | 0.79 | 0.58 | 0.91 | 0.90 | 0.90 |
| A4 Gemini 1.5 | 0.46 | 0.60 | 0.63 | 0.58 | 0.88 | 0.90 | 0.86 |
| A5 Claude 3.5 | 0.80 | 0.82 | 0.78 | 0.74 | 0.94 | 0.95 | 0.89 |
| A6 OpenAI o1 | 0.67 | 0.62 | 0.50 | 0.56 | 0.87 | 0.85 | 0.79 |
| A7 Gemini 2.0 | 0.35 | 0.26 | 0.28 | 0.30 | 0.72 | 0.67 | 0.80 |
| A8 DeepSeek V3 | 0.62 | 0.69 | 0.51 | 0.58 | 0.87 | 0.92 | 0.82 |
| A9 Gemini 1.5 Pro | 0.61 | 0.61 | 0.60 | 0.41 | 0.85 | 0.86 | 0.81 |
| A10 DeepSeek R1 | 0.68 | 0.72 | 0.73 | 0.67 | 0.91 | 0.89 | 0.89 |

The top performing AI raters, either ChatGPT 4o or Claude 3.5, still yielded the highest intra-rater consistency across different tasks. The intra-rater consistency for human rater R2 was consistently higher than that for human rater R1. The intra-rater consistency for the best performing AI raters was about the same or higher than R2 except for analytic scores of Language Use and ER essay.

#### AI Rater Effects

**Table 6 — Mean Holistic and Analytic Scores Assigned by Each Rater:**

Key patterns: Human rater R2 assigned higher mean scores across all rating tasks compared with R1. Gemini 2.0 assigned the lowest mean scores on majority of the rating tasks. ChatGPT 3.5 and ChatGPT 4 produced the highest mean scores on majority of the rating tasks.

Selected mean scores (Holistic):
- SN1: R1=3.70, R2=4.10, A1=3.53, A2=3.03, A3=3.73, A4=2.83, A5=3.80, A6=3.17, A7=2.60, A8=3.67, A9=3.33, A10=3.50
- ER1: R1=3.30, R2=3.83, A1=4.30, A2=3.43, A3=2.93, A4=3.43, A5=3.50, A6=2.90, A7=2.37, A8=3.10, A9=3.80, A10=3.57
- SN2: R1=3.23, R2=3.70, A1=3.50, A2=2.97, A3=2.70, A4=2.90, A5=3.10, A6=2.87, A7=2.00, A8=3.47, A9=3.47, A10=3.37
- ER2: R1=3.73, R2=4.07, A1=3.13, A2=3.93, A3=3.77, A4=3.60, A5=3.87, A6=3.10, A7=3.10, A8=3.47, A9=3.20, A10=3.50

**Wright Maps (Figures 1–5):**

- **Figure 1 caption:** "The Wright Map for the Holistic Scores" — For holistic scoring, SN2 was the most difficult essay, while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater (consistent with lowest mean scores) while R2 and ChatGPT 3.5 were more lenient raters.

- **Figure 2 caption:** "The Wright Map for the Analytic Scores" — For analytic scoring across all three traits, SN2 was still the most difficult essay, ER2 was easiest, SN1 was second most difficult. Gemini 2.0 was the most stringent rater; two human raters were the most lenient. Among the three traits, Language Use was the most difficult, while Task Completion was the easiest.

- **Figure 3 caption:** "The Wright Map for the Analytic Scores-Task Completion" — SN2 was still the most difficult essay while SN1 was the easiest. ER1 and ER2 had about the same difficulty. OpenAI o1 was the most stringent rater while two human raters were the most lenient raters. R1 was more lenient than R2 on Task Completion trait scoring.

- **Figure 4 caption:** "The Wright Map for the Analytic Scores-Delivery" — SN2 was still the most difficult essay while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater while R2 was the most lenient raters. R1 was the second most lenient rater like Claude 3.5 and Gemini 1.5 Pro on Delivery trait scoring.

- **Figure 5 caption:** "The Wright Map for the Analytic Scores-Language Use" — SN2 was still the most difficult essay while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater while rater 2 was the most lenient raters. R1 was the second most lenient rater on Language Use trait scoring.

**Table 7 — Rater Parameter Estimates for Holistic Scoring:**

| Rater | Rater Par | SE | Infit MS | Outfit MS |
|---|---|---|---|---|
| R2 | -0.81 | 0.11 | 0.60 | 0.60 |
| ChatGPT 3.5 | -0.37 | 0.11 | 1.36 | 1.36 |
| Claude 3.5 Sonnet | -0.30 | 0.11 | 1.01 | 1.01 |
| R1 | -0.20 | 0.11 | 0.58 | 0.59 |
| DeepSeek R1 | -0.18 | 0.11 | 1.37 | 1.41 |
| Gemini 1.5 Pro | -0.14 | 0.11 | 1.41 | 1.41 |
| DeepSeek V3 | -0.10 | 0.11 | 1.07 | 1.08 |
| ChatGPT 4 | 0.02 | 0.11 | 0.91 | 0.92 |
| ChatGPT 4o | 0.10 | 0.11 | 0.85 | 0.84 |
| Gemini 1.5 | 0.23 | 0.11 | 0.85 | 0.88 |
| OpenAI o1 | 0.50 | 0.11 | 0.70 | 0.69 |
| Gemini 2.0 | 1.25 | 0.11 | 1.22 | 1.29 |

Key findings: Gemini 2.0 was an extreme severe rater (logit = 1.25). ChatGPT 4 was the most neutral rater (parameter ≈ 0). Using cut value of 0.3: all AI raters did not have severe rater effects except ChatGPT 3.5 (-0.37, lenient) and OpenAI o1 (0.5, harsh). The two human raters had the smallest infit and outfit mean squares (both &lt; 0.7), indicating potential central tendency effect. DeepSeek R1, ChatGPT 3.5, and Gemini 1.5 Pro had infit and outfit mean squares &gt; 1.3, indicating potential misfit.

**Table 8 — Rater Parameter Estimates for Analytic Scoring:**

| Rater | Rater Par | SE | Infit MS | Outfit MS |
|---|---|---|---|---|
| R2 | -0.55 | 0.06 | 0.73 | 0.73 |
| R1 | -0.47 | 0.06 | 0.83 | 0.84 |
| ChatGPT 3.5 | -0.31 | 0.06 | 1.21 | 1.20 |
| Gemini 1.5 Pro | -0.29 | 0.06 | 1.19 | 1.19 |
| Claude 3.5 Sonnet | -0.17 | 0.06 | 0.97 | 0.97 |
| ChatGPT 4 | -0.10 | 0.06 | 0.88 | 0.89 |
| DeepSeek V3 | 0.05 | 0.06 | 1.18 | 1.18 |
| DeepSeek R1 | 0.10 | 0.06 | 1.15 | 1.18 |
| ChatGPT 4o | 0.11 | 0.06 | 1.06 | 1.05 |
| Gemini 1.5 | 0.30 | 0.06 | 0.84 | 0.87 |
| OpenAI o1 | 0.57 | 0.06 | 0.69 | 0.69 |
| Gemini 2.0 | 0.76 | 0.06 | 1.21 | 1.26 |

Key findings: Gemini 2.0 was severe (logit = 0.76). DeepSeek V3 was the most neutral rater (parameter ≈ 0.05). All AI raters did not have severe rater effects except OpenAI o1 (0.5, harsh). OpenAI o1 had the least infit and outfit mean squares at the borderline (0.69). No infit and outfit mean squares were larger than 1.3 for any rater.

**Table 9 — Rater Parameter Estimates for Analytic Scoring — Task Completion:**
Two human raters were most lenient (R1: -0.51, R2: -0.36). OpenAI o1 was the most severe rater (logit = 0.61). ChatGPT 4 and Claude 3.5 were more neutral (absolute value &lt; 0.1). All AI raters did not have severe rater effects except OpenAI o1 (0.5), Gemini 1.5 (0.53), and Gemini 2.0 (0.38). No infit or outfit mean squares were &lt; 0.7 or &gt; 1.3.

**Table 10 — Rater Parameter Estimates for Analytic Scoring — Delivery:**
Human rater R2 was most lenient (-0.63). Gemini 2.0 was most severe (rater parameter = 1.03). DeepSeek V3 was most neutral (-0.06). Using absolute cut value of 0.3, OpenAI o1 was a harsh rater (0.68), while Claude 3.5 was slightly lenient (-0.35). No infit and outfit mean squares were &lt; 0.7 or &gt; 1.3.

**Table 11 — Rater Parameter Estimates for Analytic Scoring — Language Use:**
Human rater R2 was most lenient (-0.74), R1 second most lenient (-0.63). Gemini 2.0 was most severe (1.06). DeepSeek R1, ChatGPT 4 and Gemini 1.5 were more neutral (absolute parameter ≈ 0.1). Using absolute cut value of 0.3: DeepSeek V3 (0.54), OpenAI o1 (0.49), and ChatGPT 4o (0.40) were slightly harsh raters; Gemini 1.5 Pro (-0.37) and ChatGPT 3.5 (-0.55) were slightly lenient. OpenAI o1 had infit and outfit mean squares &lt; 0.7 (slight central tendency); ChatGPT 3.5 and Gemini 2.0 yielded infit and outfit mean squares &gt; 1.3 (slight misfit).

---

### SUMMARY AND DISCUSSION (complete)

This study aims to examine the rater effects of LLM-based AI raters in automated scoring. To illustrate the methods for exploring AI rater effects, this study investigated the use of LLMs for automated holistic and analytic scoring using a fully crossed rating design. Ten LLMs were compared including ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3, and DeepSeek R1 against two human expert raters in scoring two types of writing tasks for the AP Chinese exams. The holistic and analytic score accuracy of LLMs compared with human raters were evaluated in terms of QWK. Intra-rater consistency across essays was compared in terms of Cronbach Alpha. Rater effects of LLMs were evaluated and compared with human raters using the Many FACET Rasch model.

For Research Question 1 related to the AI raters' accuracy, for holistic scoring, ChatGPT 4o, Claude 3.5, and Gemini 1.5 Pro yielded the highest scoring accuracy against either human rater. ChatGPT 4o performed the best on ER items, while Gemini 1.5 Pro excelled on SN items while Claude 3.5 showed strong performance on both SN and ER items. These three LLMs turned out to be the best performing models in analytic scoring as well. For Task Completion, ChatGPT 4o performed the best for SN and ER2 items while Claude 3.5 and Gemini 1.5 Pro performed the best on SN2 and ER1 essays. For Delivery, Claude 3.5 performed the best on SN1 and ER1 while ChatGPT 4o and Gemini 1.5 Pro performed the best on ER2 and SN2 respectively. For the Language Use trait, ChatGPT 4, 4o, and Gemini 1.5 were the top performers on ER essays while Claude 3.5 and Gemini 1.5 Pro were the best performers for SN essays. In general, QWKs for the best performing AI raters were higher than those between two human raters for holistic scoring. However, human-human QWK were higher on analytic scoring than AI QWKs. QWKs for analytic scores were higher than those for holistic scoring.

For Research Question 2 related to the AI raters' intra-rater consistency, ChatGPT 4o yielded the highest intra-rater consistency for the holistic scores, the analytic scores on the Delivery trait, and the ER items. On the other hand, Claude 3.5 yielded the highest consistency for the analytic scores, analytic scores on the Task Completion and Language Use traits as well as the SN items. Human rater R2 yielded higher scoring consistency compared with R1. The best performing AI raters' intra-rater consistency were about the same as those for the best performing human rater except on ER essays and analytic scores on Language Use with slightly lower consistency.

For Research Questions 3 on the rater effects, human raters in general were more lenient. Gemini 2.0 turned out to be a harsh rater on most scoring tasks. ChatGPT 3.5 turned out to be a lenient rater in 3 out of 5 scoring analyses with DeepSeek V3 and Gemini 1.5 Pro as the two other lenient raters. Whether an AI rater was more neutral raters depends on the task. There was no evident central tendency effects for the AI raters. However, the two human raters displayed some minor central tendency effect in holistic scoring. As Wolfe (2004) pointed out, the rater effects estimated in the FACET Rasch model was scaled to a mean of 0. If the number of raters included in the comparison differs, the estimated rater effect may be different.

The results in general support the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high scoring accuracy, better intra-rater consistency, and less rater effects. However, there were no AI raters which consistently performed the best. Some further explorations will be conducted to better understand the AI rater scoring logic. The findings of this study provide insights into the strengths and limitations of AI raters compared to human raters using the data in the study.

---

### LIMITATIONS (complete)

The limitations of the study lies in the sample size, the content domain, the type and the number of essays. There were only 30 students who participated in this experiment. The FACET software manual states a sample size of 30 as a minimum sample size. However, as the FACET Rasch model is an item response theory based latent trait model, a larger sample size would be expected even though the standard error of the rater parameter estimates was relatively small in the current study. Further, the content of the tasks was related to the AP Chinese exam. Whether the findings from this study is generalizable to other content domains such as English writing, reading, science, and math constructed-response items awaits further exploration. In addition, only two items types: SN and ER were included in the experiments, with a total of only 4 items. Other task types and traits for analytic scoring should be examined in future studies. The last limitation is related to the prompting methods for automated scoring using LLMs. The current study used a few-shot methods. Other methods should be explored in future studies including Chain-of-Thought and other fine-tuning methods.

---

### CONCLUSION (final paragraph of Summary and Discussion)

In summary, this study assessed the scoring accuracy, intra-rater consistency of AI and human holistic and analytic ratings, and estimated the AI rater effects. It demonstrated the methods that can be used to examine AI rater performance, in particular, the use of the Many FACET Rasch model to evaluate rater severity/leniency and central tendency effects. This study provided empirical evidence to inform the adoption of LLM-based AI raters for automated holistic and analytic scoring. It is highlighted that when LLMs are used for automated scoring, the methods demonstrated in this study could be the starting point for such evaluation.

---

### ALL FIGURE CAPTIONS

- **Figure 1:** "The Wright Map for the Holistic Scores"
- **Figure 2:** "The Wright Map for the Analytic Scores"
- **Figure 3:** "The Wright Map for the Analytic Scores-Task Completion"
- **Figure 4:** "The Wright Map for the Analytic Scores-Delivery"
- **Figure 5:** "The Wright Map for the Analytic Scores-Language Use"

### ALL TABLE CAPTIONS

- **Table 1:** "Holistic Scoring Accuracy (QWK) for AI Raters against Each Human Rater"
- **Table 2:** "Analytic (Task Completion) Scoring Accuracy (QWK) for AI Raters against Each Human Rater"
- **Table 3:** "Analytic (Delivery) Scoring Accuracy (QWK) for AI Raters against Each Human Rater"
- **Table 4:** "Analytic (Language Use) Scoring Accuracy (QWK) for AI Raters against Each Human Rater"
- **Table 5:** "Intra-Rater Consistency"
- **Table 6:** "Mean Holistic and Analytic Scores Assigned by Each Rater"
- **Table 7:** "Rater Parameter Estimates for Holistic Scoring"
- **Table 8:** "Rater Parameter Estimates for Analytic Scoring"
- **Table 9:** "Rater Parameter Estimates for Analytic Scoring-Task Completion"
- **Table 10:** "Rater Parameter Estimates for Analytic Scoring-Delivery"
- **Table 11:** "Rater Parameter Estimates for Analytic Scoring-Language Use"
- **Table B.1 (Appendix B):** "Standard Deviation of the Holistic and Analytic Scores Assigned by Each Rater"

---

### KEY IMPLEMENTATION DETAILS

- **Prompting method:** Few-shot prompting with training examples. Human rater R1 (certified AP Chinese examiner) designed and executed AI training protocols (Appendix A shows example for SN1 essay type).
- **Scoring rubric:** College Board AP Chinese rubric, 0–6 scale, holistic plus 3 analytic traits (Task Completion, Delivery, Language Use).
- **Training design:** AI raters were given the task prompt, scoring rubric, and student writing samples at multiple score levels as examples before scoring.
- **Scoring design:** Fully crossed rating design — all 12 raters (2 human + 10 AI) scored all 120 essays (30 students × 4 tasks).
- **Analysis software:** FACET software (Linacre, 2024), Version 3.87.0.
- **No ablation studies** were conducted in the traditional ML sense; instead, ensemble models were constructed by progressively removing worst-performing LLMs.
- **Data collection period:** Approximately one and a half years (sequential addition of models as released).&lt;/result>
&lt;usage>&lt;total_tokens>49422&lt;/total_tokens>&lt;tool_uses>7&lt;/tool_uses>&lt;duration_ms>242575&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "495da358-64d6-417e-a074-323b07c5fc94",
  "isSidechain": false,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "type": "user",
  "uuid": "82bda3de-b67c-4212-a87a-7fb1f09d0de6",
  "permissionMode": "bypassPermissions",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "82bda3de-b67c-4212-a87a-7fb1f09d0de6",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Assistant

_source line 68 · 2026-05-21T16:41:58.683Z_

<details><summary>Logged reasoning block</summary>

```text
Good, wang2025mfrm_llm paper data is back. Let me wait for the other agents to complete. Meanwhile, let me start writing the YAML for the completed papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82bda3de-b67c-4212-a87a-7fb1f09d0de6",
  "isSidechain": false,
  "requestId": "req_011CbG3hbPrMX4KKC2iK11Ru",
  "type": "assistant",
  "uuid": "851d7de9-e137-4186-90c4-8b6181f545d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hm5fuLwtijzwBecBosnRqi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12114,
      "cache_read_input_tokens": 44351,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4153,
          "cache_read_input_tokens": 44351,
          "cache_creation_input_tokens": 12114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12114
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 69 · 2026-05-21T16:42:00.201Z_

wang2025mfrm_llm 和摘要论文数据已返回。先写入已完成的 YAML，继续等待其余论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "851d7de9-e137-4186-90c4-8b6181f545d1",
  "isSidechain": false,
  "requestId": "req_011CbG3hbPrMX4KKC2iK11Ru",
  "type": "assistant",
  "uuid": "679af873-06f3-4f66-9a16-b931561a80b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hm5fuLwtijzwBecBosnRqi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12114,
      "cache_read_input_tokens": 44351,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4153,
          "cache_read_input_tokens": 44351,
          "cache_creation_input_tokens": 12114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12114
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-21T16:42:45.252Z_

<details open><summary>🔧 Tool call — Write · `toolu_01DKv4uA14bdyMbokFXczkBC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/wang2025mfrm_llm.yaml",
  "content": "paper_key: \"wang2025mfrm_llm\"\ntitle: \"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\"\nvenue: \"arXiv 2025\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Human raters (R1, R2)\", \"ChatGPT 3.5\", \"ChatGPT 4\", \"ChatGPT 4o\", \"OpenAI o1\", \"Claude 3.5 Sonnet\", \"Gemini 1.5\", \"Gemini 1.5 Pro\", \"Gemini 2.0\", \"DeepSeek V3\", \"DeepSeek R1\", \"Ensemble models (A11-A16)\"]\n  metrics:\n    - {name: \"Quadratic Weighted Kappa (QWK)\", direction: \"higher_better\"}\n    - {name: \"Cronbach Alpha (intra-rater consistency)\", direction: \"higher_better\"}\n    - {name: \"Rater parameter (severity/leniency logit)\", direction: \"closer_to_zero_better\"}\n    - {name: \"Infit/Outfit Mean Square\", direction: \"closer_to_one_better\"}\n  datasets:\n    - {name: \"AP Chinese Exam essays\", size: \"30 students × 4 tasks × 12 raters = 1440 ratings\"}\n  ablation_dimensions: [\"Ensemble composition (progressive removal of worst LLMs)\", \"Holistic vs analytic scoring\", \"Task type (SN vs ER)\", \"Analytic trait (Task Completion / Delivery / Language Use)\"]\n  training_recipe: {optimizer: \"N/A (psychometric analysis)\", lr: \"N/A\", hardware: \"FACETS software v3.87.0\"}\n  method_family: \"Many-Facet Rasch Model (psychometric measurement)\"\n\npositioning:\n  core_claim: \"MFRM 可以系统量化 LLM rater 的 severity/leniency 和 central tendency 效应，揭示不同 LLM 的评分偏差模式，ChatGPT 4o / Claude 3.5 / Gemini 1.5 Pro 表现最优\"\n  key_results: \"Best AI QWK > human-human QWK on holistic scoring; Claude 3.5 highest consistency (α=0.94 analytic); Gemini 2.0 most severe (logit=1.25); human raters show central tendency (infit<0.7)\"\n  limitations:\n    - \"样本仅30人，FACETS手册推荐的最低样本量\"\n    - \"仅AP中文写作，未推广到英文/理科/数学\"\n    - \"仅两种任务类型（SN和ER），4道题目\"\n    - \"仅用few-shot prompting，未探索CoT或微调\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"跨界迁移型\"\n  hook: \"Performance assessment scoring is costly and error-prone — LLMs offer a solution but their rater effects are unknown\"\n  tension: \"几乎所有研究只关注LLM评分准确率，对LLM作为评分者的系统偏差（rater effects）无人研究\"\n  key_insight: \"在Methods段通过MFRM方程引入——将LLM和人类评分者放在同一psychometric量尺上，用rater parameter量化severity/leniency\"\n  argument_chain: \"performance assessment costly → LLMs promising but accuracy-only evaluation insufficient → rater effects matter for fairness → MFRM places all raters on common scale → empirical comparison of 10 LLMs + 2 humans → actionable recommendations\"\n  contribution_framing: \"3个研究问题驱动：accuracy, consistency, rater effects\"\n  intro_structure: \"7段：背景(2段) → 技术进展(2段) → LLM评分文献(1段) → rater effects定义(1段) → 研究问题(1段)\"\n  notable_technique: \"用Wright Map可视化将所有facets（学生能力、题目难度、评分者严苛度）放在同一logit量尺上，直觉展示评分者偏差\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"method_overview\"\n    description: \"Wright Map for Holistic Scores — 将30名学生、4道题目、12名评分者（2人+10AI）放在同一logit量尺上\"\n    narrative_role: \"核心结果可视化，一图展示所有facets的相对位置，直观显示Gemini 2.0极度严苛、R2和ChatGPT 3.5偏宽松\"\n    design_elements: [\"三列并排布局（学生/题目/评分者）\", \"logit量尺对齐\", \"标注extreme raters\"]\n    visual_style: \"FACETS软件标准Wright Map输出，黑白三列并排，logit尺度左侧\"\n  result_figures:\n    - figure_id: \"Figure 2-5\"\n      viz_type: \"Wright Map variants\"\n      what_compared: \"不同analytic trait下的rater severity分布\"\n      how_gain_highlighted: \"通过rater在logit尺上的位置变化展示trait-specific severity差异\"\n      design_note: \"每个trait一张Wright Map，允许读者对比rater在不同trait上的severity变化\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(holistic全景) → Figure 2(analytic全景) → Figure 3-5(三个trait分别)\"\n\ntables:\n  table_count: 11\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods (AI raters + ensembles)\"\n    col_axis: \"tasks × human raters\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"文字描述best performers，无bold/underline\"\n    statistical_reporting: \"单次评分，无重复统计\"\n    num_baselines: 12\n    design_note: \"每个AI rater对每个human rater单独报QWK，允许看到AI-R1 vs AI-R2的差异；ensemble部分渐进移除展示组合效果\"\n  ablation_tables:\n    - table_id: \"Tables 7-11\"\n      what_varied: [\"rater identity\", \"scoring type (holistic/analytic)\", \"trait\"]\n      variation_style: \"full_numbers\"\n      design_note: \"每张表报rater parameter + SE + infit + outfit，标准psychometric报告格式\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Appendix A: AI training protocol示例; Appendix B: 各rater评分标准差\"\n    reason: \"Training protocol细节和描述统计放附录，主文聚焦psychometric分析\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "679af873-06f3-4f66-9a16-b931561a80b1",
  "isSidechain": false,
  "requestId": "req_011CbG3hbPrMX4KKC2iK11Ru",
  "type": "assistant",
  "uuid": "5c219d9e-9c0f-4452-b590-ee87b072d801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hm5fuLwtijzwBecBosnRqi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12114,
      "cache_read_input_tokens": 44351,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4153,
          "cache_read_input_tokens": 44351,
          "cache_creation_input_tokens": 12114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12114
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-21T16:42:45.267Z_

<details><summary>↩ Tool result · `toolu_01DKv4uA14bdyMbokFXczkBC`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/wang2025mfrm_llm.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c219d9e-9c0f-4452-b590-ee87b072d801",
  "isSidechain": false,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "type": "user",
  "uuid": "37d2f565-7122-4eeb-b9dd-45c86038dde0",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/wang2025mfrm_llm.yaml",
    "content": "paper_key: \"wang2025mfrm_llm\"\ntitle: \"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\"\nvenue: \"arXiv 2025\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Human raters (R1, R2)\", \"ChatGPT 3.5\", \"ChatGPT 4\", \"ChatGPT 4o\", \"OpenAI o1\", \"Claude 3.5 Sonnet\", \"Gemini 1.5\", \"Gemini 1.5 Pro\", \"Gemini 2.0\", \"DeepSeek V3\", \"DeepSeek R1\", \"Ensemble models (A11-A16)\"]\n  metrics:\n    - {name: \"Quadratic Weighted Kappa (QWK)\", direction: \"higher_better\"}\n    - {name: \"Cronbach Alpha (intra-rater consistency)\", direction: \"higher_better\"}\n    - {name: \"Rater parameter (severity/leniency logit)\", direction: \"closer_to_zero_better\"}\n    - {name: \"Infit/Outfit Mean Square\", direction: \"closer_to_one_better\"}\n  datasets:\n    - {name: \"AP Chinese Exam essays\", size: \"30 students × 4 tasks × 12 raters = 1440 ratings\"}\n  ablation_dimensions: [\"Ensemble composition (progressive removal of worst LLMs)\", \"Holistic vs analytic scoring\", \"Task type (SN vs ER)\", \"Analytic trait (Task Completion / Delivery / Language Use)\"]\n  training_recipe: {optimizer: \"N/A (psychometric analysis)\", lr: \"N/A\", hardware: \"FACETS software v3.87.0\"}\n  method_family: \"Many-Facet Rasch Model (psychometric measurement)\"\n\npositioning:\n  core_claim: \"MFRM 可以系统量化 LLM rater 的 severity/leniency 和 central tendency 效应，揭示不同 LLM 的评分偏差模式，ChatGPT 4o / Claude 3.5 / Gemini 1.5 Pro 表现最优\"\n  key_results: \"Best AI QWK > human-human QWK on holistic scoring; Claude 3.5 highest consistency (α=0.94 analytic); Gemini 2.0 most severe (logit=1.25); human raters show central tendency (infit<0.7)\"\n  limitations:\n    - \"样本仅30人，FACETS手册推荐的最低样本量\"\n    - \"仅AP中文写作，未推广到英文/理科/数学\"\n    - \"仅两种任务类型（SN和ER），4道题目\"\n    - \"仅用few-shot prompting，未探索CoT或微调\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"跨界迁移型\"\n  hook: \"Performance assessment scoring is costly and error-prone — LLMs offer a solution but their rater effects are unknown\"\n  tension: \"几乎所有研究只关注LLM评分准确率，对LLM作为评分者的系统偏差（rater effects）无人研究\"\n  key_insight: \"在Methods段通过MFRM方程引入——将LLM和人类评分者放在同一psychometric量尺上，用rater parameter量化severity/leniency\"\n  argument_chain: \"performance assessment costly → LLMs promising but accuracy-only evaluation insufficient → rater effects matter for fairness → MFRM places all raters on common scale → empirical comparison of 10 LLMs + 2 humans → actionable recommendations\"\n  contribution_framing: \"3个研究问题驱动：accuracy, consistency, rater effects\"\n  intro_structure: \"7段：背景(2段) → 技术进展(2段) → LLM评分文献(1段) → rater effects定义(1段) → 研究问题(1段)\"\n  notable_technique: \"用Wright Map可视化将所有facets（学生能力、题目难度、评分者严苛度）放在同一logit量尺上，直觉展示评分者偏差\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"method_overview\"\n    description: \"Wright Map for Holistic Scores — 将30名学生、4道题目、12名评分者（2人+10AI）放在同一logit量尺上\"\n    narrative_role: \"核心结果可视化，一图展示所有facets的相对位置，直观显示Gemini 2.0极度严苛、R2和ChatGPT 3.5偏宽松\"\n    design_elements: [\"三列并排布局（学生/题目/评分者）\", \"logit量尺对齐\", \"标注extreme raters\"]\n    visual_style: \"FACETS软件标准Wright Map输出，黑白三列并排，logit尺度左侧\"\n  result_figures:\n    - figure_id: \"Figure 2-5\"\n      viz_type: \"Wright Map variants\"\n      what_compared: \"不同analytic trait下的rater severity分布\"\n      how_gain_highlighted: \"通过rater在logit尺上的位置变化展示trait-specific severity差异\"\n      design_note: \"每个trait一张Wright Map，允许读者对比rater在不同trait上的severity变化\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(holistic全景) → Figure 2(analytic全景) → Figure 3-5(三个trait分别)\"\n\ntables:\n  table_count: 11\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods (AI raters + ensembles)\"\n    col_axis: \"tasks × human raters\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"文字描述best performers，无bold/underline\"\n    statistical_reporting: \"单次评分，无重复统计\"\n    num_baselines: 12\n    design_note: \"每个AI rater对每个human rater单独报QWK，允许看到AI-R1 vs AI-R2的差异；ensemble部分渐进移除展示组合效果\"\n  ablation_tables:\n    - table_id: \"Tables 7-11\"\n      what_varied: [\"rater identity\", \"scoring type (holistic/analytic)\", \"trait\"]\n      variation_style: \"full_numbers\"\n      design_note: \"每张表报rater parameter + SE + infit + outfit，标准psychometric报告格式\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Appendix A: AI training protocol示例; Appendix B: 各rater评分标准差\"\n    reason: \"Training protocol细节和描述统计放附录，主文聚焦psychometric分析\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "5c219d9e-9c0f-4452-b590-ee87b072d801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-21T16:42:52.776Z_

<details open><summary>🔧 Tool call — Write · `toolu_012kKS6q1NzRUS2SNDFrnWhD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/fiedler2026bias_uncertainty.yaml",
  "content": "paper_key: \"fiedler2026bias_uncertainty\"\ntitle: \"Bias and Uncertainty in LLM-as-a-Judge Estimation\"\nvenue: \"arXiv 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"Naive estimator (raw judge outputs)\", \"Corrected estimators\"]\n  metrics:\n    - {name: \"J (judge quality diagnostic)\", direction: \"higher_better\"}\n    - {name: \"ΔJ (calibration instability)\", direction: \"lower_better\"}\n    - {name: \"Sign-reversal detection rate\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"MMLU-Pro\", size: \"not specified\"}\n  ablation_dimensions: [\"Shared vs independent calibration\", \"Judge quality levels\"]\n  training_recipe: {optimizer: \"N/A (analytical/simulation study)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"Statistical estimation / bias correction diagnostics\"\n\npositioning:\n  core_claim: \"共享校准（shared calibration）在模型对比时会引入严重偏差甚至符号反转，提出J/ΔJ诊断指标\"\n  key_results: \"Sign-reversal at high confidence under shared calibration\"\n  limitations: [\"仅理论分析+仿真，未在大规模real数据验证\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37d2f565-7122-4eeb-b9dd-45c86038dde0",
  "isSidechain": false,
  "requestId": "req_011CbG3hbPrMX4KKC2iK11Ru",
  "type": "assistant",
  "uuid": "1ab45708-0419-4dc3-b112-a5bcc22aad5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hm5fuLwtijzwBecBosnRqi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12114,
      "cache_read_input_tokens": 44351,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4153,
          "cache_read_input_tokens": 44351,
          "cache_creation_input_tokens": 12114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12114
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-21T16:42:52.802Z_

<details><summary>↩ Tool result · `toolu_012kKS6q1NzRUS2SNDFrnWhD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/fiedler2026bias_uncertainty.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ab45708-0419-4dc3-b112-a5bcc22aad5d",
  "isSidechain": false,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "type": "user",
  "uuid": "7d0f7393-511d-4612-a01d-3207f5cdbeb9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/fiedler2026bias_uncertainty.yaml",
    "content": "paper_key: \"fiedler2026bias_uncertainty\"\ntitle: \"Bias and Uncertainty in LLM-as-a-Judge Estimation\"\nvenue: \"arXiv 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"Naive estimator (raw judge outputs)\", \"Corrected estimators\"]\n  metrics:\n    - {name: \"J (judge quality diagnostic)\", direction: \"higher_better\"}\n    - {name: \"ΔJ (calibration instability)\", direction: \"lower_better\"}\n    - {name: \"Sign-reversal detection rate\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"MMLU-Pro\", size: \"not specified\"}\n  ablation_dimensions: [\"Shared vs independent calibration\", \"Judge quality levels\"]\n  training_recipe: {optimizer: \"N/A (analytical/simulation study)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"Statistical estimation / bias correction diagnostics\"\n\npositioning:\n  core_claim: \"共享校准（shared calibration）在模型对比时会引入严重偏差甚至符号反转，提出J/ΔJ诊断指标\"\n  key_results: \"Sign-reversal at high confidence under shared calibration\"\n  limitations: [\"仅理论分析+仿真，未在大规模real数据验证\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "1ab45708-0419-4dc3-b112-a5bcc22aad5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-21T16:43:01.778Z_

<details open><summary>🔧 Tool call — Write · `toolu_01G6H2SDQQBgLc5hmNXuxDxD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/soumik2026judging_judges.yaml",
  "content": "paper_key: \"soumik2026judging_judges\"\ntitle: \"Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\"\nvenue: \"arXiv 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"9 debiasing strategies across 5 judge models (Claude Sonnet 4, GPT, Gemini, Llama)\"]\n  metrics:\n    - {name: \"Style bias score\", direction: \"lower_better\"}\n    - {name: \"Position bias score\", direction: \"lower_better\"}\n    - {name: \"Quality-length discrimination accuracy\", direction: \"higher_better\"}\n    - {name: \"Agreement change (pp)\", direction: \"context_dependent\"}\n  datasets:\n    - {name: \"MT-Bench\", size: \"n=400\"}\n    - {name: \"LLMBar\", size: \"n=200\"}\n    - {name: \"Custom benchmark\", size: \"n=225\"}\n  ablation_dimensions: [\"Debiasing strategy\", \"Judge model\", \"Bias type\"]\n  training_recipe: {optimizer: \"N/A (evaluation study)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"Empirical comparative evaluation of debiasing\"\n\npositioning:\n  core_claim: \"Style bias远大于position bias（0.76-0.92 vs ≤0.04），debiasing效果高度依赖judge模型\"\n  key_results: \"Style bias 0.76-0.92; position bias ≤0.04; Claude Sonnet 4 +11.2pp with combined budget (p<0.0001)\"\n  limitations: [\"仅比较已有策略，未提出新方法\", \"未建立解释框架\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d0f7393-511d-4612-a01d-3207f5cdbeb9",
  "isSidechain": false,
  "requestId": "req_011CbG3hbPrMX4KKC2iK11Ru",
  "type": "assistant",
  "uuid": "2efd9516-8fab-43e0-a59d-d6475de22bca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hm5fuLwtijzwBecBosnRqi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12114,
      "cache_read_input_tokens": 44351,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4153,
          "cache_read_input_tokens": 44351,
          "cache_creation_input_tokens": 12114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12114
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-21T16:43:01.787Z_

<details><summary>↩ Tool result · `toolu_01G6H2SDQQBgLc5hmNXuxDxD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/soumik2026judging_judges.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2efd9516-8fab-43e0-a59d-d6475de22bca",
  "isSidechain": false,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "type": "user",
  "uuid": "47f1d3c7-7935-4ad6-8da1-3a098e6cb416",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/soumik2026judging_judges.yaml",
    "content": "paper_key: \"soumik2026judging_judges\"\ntitle: \"Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\"\nvenue: \"arXiv 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"9 debiasing strategies across 5 judge models (Claude Sonnet 4, GPT, Gemini, Llama)\"]\n  metrics:\n    - {name: \"Style bias score\", direction: \"lower_better\"}\n    - {name: \"Position bias score\", direction: \"lower_better\"}\n    - {name: \"Quality-length discrimination accuracy\", direction: \"higher_better\"}\n    - {name: \"Agreement change (pp)\", direction: \"context_dependent\"}\n  datasets:\n    - {name: \"MT-Bench\", size: \"n=400\"}\n    - {name: \"LLMBar\", size: \"n=200\"}\n    - {name: \"Custom benchmark\", size: \"n=225\"}\n  ablation_dimensions: [\"Debiasing strategy\", \"Judge model\", \"Bias type\"]\n  training_recipe: {optimizer: \"N/A (evaluation study)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"Empirical comparative evaluation of debiasing\"\n\npositioning:\n  core_claim: \"Style bias远大于position bias（0.76-0.92 vs ≤0.04），debiasing效果高度依赖judge模型\"\n  key_results: \"Style bias 0.76-0.92; position bias ≤0.04; Claude Sonnet 4 +11.2pp with combined budget (p<0.0001)\"\n  limitations: [\"仅比较已有策略，未提出新方法\", \"未建立解释框架\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "2efd9516-8fab-43e0-a59d-d6475de22bca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-21T16:43:10.320Z_

<details open><summary>🔧 Tool call — Write · `toolu_017SFTZbjUQ2C72JNDRcNEYs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/logprober2024.yaml",
  "content": "paper_key: \"logprober2024\"\ntitle: \"LogProber: Disentangling confidence from contamination in LLM responses\"\nvenue: \"arXiv 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"CDD (Contamination Detection via Diversity)\", \"TS-Guessing\"]\n  metrics:\n    - {name: \"Safe Score\", direction: \"lower_means_contaminated\"}\n    - {name: \"Accuracy\", direction: \"higher_better\"}\n    - {name: \"Precision\", direction: \"higher_better\"}\n    - {name: \"Recall\", direction: \"higher_better\"}\n    - {name: \"F1\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"Cognitive Reflection Test (CRT)\", size: \"oldCRT vs newCRT\"}\n    - {name: \"MMLU\", size: \"not specified\"}\n    - {name: \"BigCodeBench\", size: \"not specified\"}\n    - {name: \"MBXP\", size: \"not specified\"}\n  ablation_dimensions: [\"Contamination type (Q-A vs answer-only)\", \"Model family\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"Token log-probability analysis for contamination detection\"\n\npositioning:\n  core_claim: \"通过token log-probability曲线的AUC计算Safe Score，可区分模型真实能力和数据污染导致的虚高表现\"\n  key_results: \"MMLU上98% accuracy vs CDD的50%; 能检测Q-A contamination但对answer-only contamination失效\"\n  limitations: [\"需要logprob访问（gray-box）\", \"对answer-only contamination无效\"]\n  relation_to_us: \"component\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47f1d3c7-7935-4ad6-8da1-3a098e6cb416",
  "isSidechain": false,
  "requestId": "req_011CbG3hbPrMX4KKC2iK11Ru",
  "type": "assistant",
  "uuid": "afb163d4-fd8c-4e0c-b065-a097c5a754e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hm5fuLwtijzwBecBosnRqi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12114,
      "cache_read_input_tokens": 44351,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4153,
          "cache_read_input_tokens": 44351,
          "cache_creation_input_tokens": 12114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12114
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-21T16:43:10.334Z_

<details><summary>↩ Tool result · `toolu_017SFTZbjUQ2C72JNDRcNEYs`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/logprober2024.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afb163d4-fd8c-4e0c-b065-a097c5a754e1",
  "isSidechain": false,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "type": "user",
  "uuid": "2ab4cf93-6730-4cad-943c-55a76233e86c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/logprober2024.yaml",
    "content": "paper_key: \"logprober2024\"\ntitle: \"LogProber: Disentangling confidence from contamination in LLM responses\"\nvenue: \"arXiv 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"CDD (Contamination Detection via Diversity)\", \"TS-Guessing\"]\n  metrics:\n    - {name: \"Safe Score\", direction: \"lower_means_contaminated\"}\n    - {name: \"Accuracy\", direction: \"higher_better\"}\n    - {name: \"Precision\", direction: \"higher_better\"}\n    - {name: \"Recall\", direction: \"higher_better\"}\n    - {name: \"F1\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"Cognitive Reflection Test (CRT)\", size: \"oldCRT vs newCRT\"}\n    - {name: \"MMLU\", size: \"not specified\"}\n    - {name: \"BigCodeBench\", size: \"not specified\"}\n    - {name: \"MBXP\", size: \"not specified\"}\n  ablation_dimensions: [\"Contamination type (Q-A vs answer-only)\", \"Model family\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"Token log-probability analysis for contamination detection\"\n\npositioning:\n  core_claim: \"通过token log-probability曲线的AUC计算Safe Score，可区分模型真实能力和数据污染导致的虚高表现\"\n  key_results: \"MMLU上98% accuracy vs CDD的50%; 能检测Q-A contamination但对answer-only contamination失效\"\n  limitations: [\"需要logprob访问（gray-box）\", \"对answer-only contamination无效\"]\n  relation_to_us: \"component\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "afb163d4-fd8c-4e0c-b065-a097c5a754e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-21T16:43:18.690Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Cu8azQMq53SJcZkC8gY4eY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/shu2013dgirt.yaml",
  "content": "paper_key: \"shu2013dgirt\"\ntitle: \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\"\nvenue: \"Psychometrika 2013\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"Standard IRT models (2PL/3PL)\"]\n  metrics:\n    - {name: \"Model fit\", direction: \"higher_better\"}\n    - {name: \"Examinee classification (cheater vs non-cheater)\", direction: \"higher_accuracy_better\"}\n    - {name: \"Score gain on exposed vs unexposed items\", direction: \"diagnostic\"}\n  datasets:\n    - {name: \"Operational exam data\", size: \"not publicly available\"}\n  ablation_dimensions: [\"Exposed vs unexposed items\", \"Cheater vs non-cheater examinees\"]\n  training_recipe: {optimizer: \"Hierarchical MCMC (HMCMC)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"Bayesian psychometric modeling — Deterministic Gated IRT (DGM)\"\n\npositioning:\n  core_claim: \"通过gating机制将观测响应分解为真实能力和作弊能力两个潜在分布，实现item compromise的检测和作弊者分类\"\n  key_results: \"成功分离exposed/unexposed items上的score gain patterns\"\n  limitations: [\"需要已知哪些items被泄露\", \"样本量需求较大\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ab4cf93-6730-4cad-943c-55a76233e86c",
  "isSidechain": false,
  "requestId": "req_011CbG3hbPrMX4KKC2iK11Ru",
  "type": "assistant",
  "uuid": "870d0e7d-ea94-48a3-99bc-68684b5326a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hm5fuLwtijzwBecBosnRqi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12114,
      "cache_read_input_tokens": 44351,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4153,
          "cache_read_input_tokens": 44351,
          "cache_creation_input_tokens": 12114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12114
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-21T16:43:18.769Z_

<details><summary>↩ Tool result · `toolu_01Cu8azQMq53SJcZkC8gY4eY`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/shu2013dgirt.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "870d0e7d-ea94-48a3-99bc-68684b5326a1",
  "isSidechain": false,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "type": "user",
  "uuid": "af4ad412-aba3-47e0-9d05-97a7b95603bd",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/shu2013dgirt.yaml",
    "content": "paper_key: \"shu2013dgirt\"\ntitle: \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\"\nvenue: \"Psychometrika 2013\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"Standard IRT models (2PL/3PL)\"]\n  metrics:\n    - {name: \"Model fit\", direction: \"higher_better\"}\n    - {name: \"Examinee classification (cheater vs non-cheater)\", direction: \"higher_accuracy_better\"}\n    - {name: \"Score gain on exposed vs unexposed items\", direction: \"diagnostic\"}\n  datasets:\n    - {name: \"Operational exam data\", size: \"not publicly available\"}\n  ablation_dimensions: [\"Exposed vs unexposed items\", \"Cheater vs non-cheater examinees\"]\n  training_recipe: {optimizer: \"Hierarchical MCMC (HMCMC)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"Bayesian psychometric modeling — Deterministic Gated IRT (DGM)\"\n\npositioning:\n  core_claim: \"通过gating机制将观测响应分解为真实能力和作弊能力两个潜在分布，实现item compromise的检测和作弊者分类\"\n  key_results: \"成功分离exposed/unexposed items上的score gain patterns\"\n  limitations: [\"需要已知哪些items被泄露\", \"样本量需求较大\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "870d0e7d-ea94-48a3-99bc-68684b5326a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 80 · 2026-05-21T16:43:18.842Z_

```json
{
  "parentUuid": "af4ad412-aba3-47e0-9d05-97a7b95603bd",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2e179f71-9ac1-44fa-898f-1630e9edbfdf",
  "timestamp": "2026-05-21T16:43:18.842Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 81_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "2e179f71-9ac1-44fa-898f-1630e9edbfdf",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 82_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Assistant

_source line 83 · 2026-05-21T16:43:23.508Z_

5 个 YAML 已写入。等待剩余 7 个深度精读 agent 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e179f71-9ac1-44fa-898f-1630e9edbfdf",
  "isSidechain": false,
  "requestId": "req_011CbG3osHkFsnXg4REDzuos",
  "type": "assistant",
  "uuid": "7d33b94c-10b4-45c9-ba44-c5cc1df94e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126qs4pyFTot5GZvzk9rva4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4618,
      "cache_read_input_tokens": 56465,
      "output_tokens": 33,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 33,
          "cache_read_input_tokens": 56465,
          "cache_creation_input_tokens": 4618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4618
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 84 · 2026-05-21T16:43:27.766Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:43:27.766Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "&lt;task-notification>\n&lt;task-id>ade7e6bb7f61dc1fb&lt;/task-id>\n&lt;tool-use-id>toolu_0186HRHtg5zTNLH6chQsgrwp&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ade7e6bb7f61dc1fb.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: preference_leakage2026\" completed&lt;/summary>\n&lt;result>I now have comprehensive data from the paper. Here is the complete extracted information:\n\n---\n\n## Paper: \"Preference Leakage: A Contamination Problem in LLM-as-a-judge\"\n\n**ArXiv:** 2502.01534 | **Venue:** ICLR 2026 | **Authors:** Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, Huan Liu | **Submitted:** Feb 3, 2025 | **Latest version:** Mar 4, 2026 (v3)\n\n---\n\n## 1. ABSTRACT\n\nLLM-as-judge and LLM-based data synthesis are two fundamental LLM-driven data annotation methods. The paper introduces \"preference leakage\" — a contamination issue arising when the LLMs used for data generation and evaluation are closely related, causing the evaluator's preferences to leak to the student models through synthetic data, inflating evaluation scores. Three relatedness types are defined: same model, inheritance relationship, same model family. Experiments on Arena-Hard and AlpacaEval 2.0 with GPT-4o, Gemini-1.5-flash, and LLaMA-3.3-70B demonstrate systematic bias. The PLS metric quantifies the bias; the effect is more pronounced for subjective questions and smaller student models.\n\n---\n\n## 2. FULL INTRODUCTION (ALL PARAGRAPHS)\n\n**Paragraph 1:** Recent advancements in LLMs have empowered various downstream tasks and applications. However, this poses substantial challenges to automatic evaluation. LLM-based AI agents' focus transfer from traditional NLP tasks to real-world, open-ended response generation greatly limits the applicability of traditional n-gram matching methods (BLEU, ROUGE) or model-based evaluators.\n\n**Paragraph 2:** To address these challenges, the LLM-as-a-judge paradigm has been proposed to leverage LLMs as evaluators to assess response quality. By combining powerful LLMs with well-designed prompting strategies, LLM-as-a-judge enables human-like evaluation of long-form and open-ended generation in a more cost-efficient and scalable manner. However, recent studies point out weaknesses; Ye et al. (2024) explores various biases and vulnerabilities, highlighting the importance of developing reliable and fair LLM-based evaluation.\n\n**Paragraph 3:** This work highlights a subtle yet critical bias in LLM-as-a-Judge: **Preference Leakage**. This issue arises when the LLMs used for data generation and evaluation are closely related, causing the preference of the LLM evaluators to leak to the student models through synthetic data, thus inflating evaluation scores (as illustrated in Figure 1). Synthetic data has become a cornerstone of model training. When combined with LLM-as-a-Judge, they offer significant efficiency gains. However, limited attention has been given to the potential contamination when the generator and evaluator LLMs share a close relationship. This issue is particularly pervasive in popular benchmarks (AlpacaEval 2.0, Arena-Hard) and LLM-relevant studies (see Appendix B), due to common reliance on the most advanced LLMs like GPT-4 for both data synthesis and evaluation. The relatedness — akin to overlap between training data and evaluation sets in traditional data contamination — introduces systematic bias of judge LLMs toward their related student models. Compared to other biases such as length bias or egocentric bias, preference leakage is subtler and more challenging to detect, especially since most LLMs do not disclose their training data.\n\n**Paragraph 4 (RQ definitions):**\nTo investigate the preference leakage problem, the authors define three relatedness types between data generator LLM and judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family. Three core research questions:\n\n- **RQ1:** Does preference leakage introduce systematic biases in LLM-based evaluation? Addressed via experiments with various LLM baselines on two benchmarks, using the preference leakage score to quantify bias. Results show obvious bias of judging LLMs toward their related student models.\n\n- **RQ2:** What is the severity of preference leakage under various scenarios? Covered via experiments under various data mixing strategies, relatedness settings, tuning techniques, and real-world applications. Preference leakage consistently affects judge LLMs. Severity correlates with degree of relatedness between data generator and judge, as well as proportion of synthetic data.\n\n- **RQ3:** What are the underlying mechanisms causing preference leakage? Analyzed via LLMs' recognition capabilities on their related student models' generation and distribution of bias across different question types and judgment dimensions. Preference leakage is subtle and hard-to-detect, particularly affecting subjective questions and judgment dimensions.\n\n---\n\n## 3. CONTRIBUTION STATEMENTS\n\n- For the first time, we introduce preference leakage, a contamination issue arising from the relatedness between the data generator and judge LLMs.\n- We conduct extensive experiments across various LLMs and benchmarks to study how and to what extent the potential bias brought by preference leakage influences judgment.\n- Our further analysis reveals that preference leakage is prevalent in diverse scenarios and difficult for judge LLMs to detect, providing valuable insights for future research on this challenging issue.\n\n---\n\n## 4. METHOD DETAILS\n\n### Formal Definition\n\nEntities:\n- **Data Generator LLM M_G**: defines conditional distribution P_M_G(y|x), forms synthetic dataset D_syn\n- **Student LLM M_S**: trained on data generated by M_G, producing output distribution P_M_S(y|x)\n- **Judge LLM M_J**: provides scoring function S_M_J(y|x)\n\nPreference leakage occurs when:\n\n`E[S_M_J(y_S|x) | M_G ~_rel M_J] &gt; E[S_M_J'(y_S|x) | M_G ≁_rel M_J']`\n\nM_J may favor M_S outputs not solely based on intrinsic quality, but because they exhibit spurious features (style, format, wording) inherited from M_G.\n\n### Three Relatedness Types\n\n1. **Same Model:** M_G ≡ M_J — inherent generative preferences identical to evaluation preferences.\n\n2. **Inheritance Relationship:** M_J ← FineTune(M_G, D_train) or M_J ← FineTune(M_base, D_syn_G) — descendant model internalizes and favors preferences/styles of its progenitor. Bidirectional.\n\n3. **Same Model Family:** M_G and M_J share common architectural blueprint (A_X) and pre-training on substantially overlapping datasets (D_X), leading to correlated preferences and systemic biases. M_k ∈ Family(A_X, D_X) for k ∈ {G, J}.\n\n---\n\n## 5. EXPERIMENTS\n\n### Datasets &amp; Models\n\n**Evaluation benchmarks:**\n- **Arena-Hard**: 500 challenging English questions; 96.7% Spearman correlation with LMArena hard prompts\n- **AlpacaEval 2.0**: 805 questions; reduces text length effect vs. v1.0\n\n**Generator/Judge models:** GPT-4o-2024-11-20, Gemini-1.5-flash, LLaMA-3.3-70B-Instruct-turbo\n\n**Student models:** Mistral-7B-v0.1, Qwen-2.5-14B (pre-trained versions, not instruct)\n\n**Synthetic data:** 30,000 prompts sampled from Ultrafeedback dataset (includes TruthfulQA, FalseQA, Evol-Instruct). Each generator produces one synthetic dataset. Three student model versions per base model: Mistral/Qwen-GPT-4o, Mistral/Qwen-Gemini-1.5, Mistral/Qwen-LLaMA-3.3.\n\n### Preference Leakage Score (PLS) Metric\n\n```\nPLS(i,j) = [(WR(i,i) - AVG(i,j))/AVG(i,j) + (WR(j,j) - AVG(j,i))/AVG(j,i)] / 2\nAVG(i,j) = [WR(i,i) + WR(i,j)] / 2\n```\n\nWR(i,j) = win-rate from judge model j to student model i. Large PLS = strong bias toward related student models.\n\n---\n\n## 6. ALL RESULTS WITH NUMBERS\n\n### Table 1: Main PLS Results (Arena-Hard &amp; AlpacaEval 2.0)\n\n| Student | Judge Pair | Arena-Hard | AlpacaEval 2.0 | Avg |\n|---------|-----------|-----------|----------------|-----|\n| Mistral-7B | GPT-4o &amp; Gemini-1.5 | 28.7% | 18.4% | 23.6% |\n| Mistral-7B | GPT-4o &amp; LLaMA-3.3 | -1.5% | 1.4% | -0.1% |\n| Mistral-7B | LLaMA-3.3 &amp; Gemini-1.5 | 13.1% | 19.8% | 16.4% |\n| Qwen-2.5-14B | GPT-4o &amp; Gemini-1.5 | 37.1% | 18.6% | 27.9% |\n| Qwen-2.5-14B | GPT-4o &amp; LLaMA-3.3 | 1.0% | 2.3% | 1.7% |\n| Qwen-2.5-14B | LLaMA-3.3 &amp; Gemini-1.5 | 25.4% | 18.4% | 21.9% |\n\n**Key finding:** Preference leakage exists in most model pairs except GPT-4o &amp; LLaMA-3.3 (near zero), where LLaMA-3.3 lacks strong relatedness to GPT-4o.\n\n### Table 2: PLS by Relatedness Type (Mistral-7B, GPT-4o &amp; Gemini-1.5)\n\n| Relatedness Type | Arena-Hard | AlpacaEval 2.0 | Avg |\n|-----------------|-----------|----------------|-----|\n| Same Model | 28.7% | 18.4% | 23.6% |\n| Inheritance – same instructions | 17.8% | 20.7% | 19.3% |\n| Inheritance – different instructions | 18.3% | 26.3% | 22.3% |\n| Same Family – same series | 10.1% | 7.6% | 8.9% |\n| Same Family – different series | 3.3% | 2.2% | 2.8% |\n\n### Table 3: PLS by Learning Method (Mistral-7B, GPT-4o vs Gemini-1.5)\n\n| Method | Arena-Hard | AlpacaEval 2.0 | Avg |\n|--------|-----------|----------------|-----|\n| SFT | 28.7% | 18.4% | 23.6% |\n| DPO | 7.7% | 2.7% | 5.2% |\n| ICL | -4.2% | -1.1% | -2.7% |\n\nSFT data pool: OASST, LIMA, MOSS. DPO: 2 responses per instruction, pairwise feedback from each generator. ICL: 4 demonstration pairs per LLM's synthetic dataset.\n\n### Table 4: Real-World Leaderboard Impact\n\n| Bias Type | Evaluator | Target Models | Ranking Difference |\n|-----------|-----------|---------------|-------------------|\n| Egocentric Bias | GPT-4 Preview | GPT-4 Preview | 1.00 |\n| Preference Leakage | GPT-4 | Vicuna 7B/13B/33B | 1.33 |\n\nRanking difference = LMArena rank minus AlpacaEval 2.0 rank. Preference leakage produces larger ranking inflation than egocentric bias.\n\n### Table 5: Student Recognition Results\n\n| Task | Model | Pointwise Acc. | Pairwise Acc. |\n|------|-------|----------------|---------------|\n| Student Recognition | GPT-4o | 41.0% | 52.0% |\n| Student Recognition | Gemini-1.5 | 53.2% | 44.2% |\n| Student Recognition | LLaMA-3.3 | 41.8% | 29.8% |\n| Response Classification | BERT (3-class) | 82.4% | — |\n\nRandom baseline for binary recognition: 50%. Judge LLMs perform at/near random; BERT classifier achieves 82.4%, confirming stylistic fingerprints exist but are invisible to LLM judges.\n\n### Table 6: Spurious Feature Ablation (Qwen-3-8B rewriter, Gemini-2.0 judge)\n\n| Setting | GPT &amp; Gemini | GPT &amp; LLaMA | LLaMA &amp; Gemini |\n|---------|-------------|-------------|----------------|\n| Baseline | 17.5% | 2.3% | 18.8% |\n| –style | 9.0% | 3.3% | 14.6% |\n| –format | 9.8% | 1.9% | 14.5% |\n| –wording | 11.2% | 2.4% | 18.2% |\n\nStyle and format removal each roughly halve leakage for the two high-leakage pairs. Wording removal has minimal effect.\n\n### Table 7: Mitigation Methods (Error Bias, lower = better)\n\n| Method | Error Bias |\n|--------|-----------|\n| Base | 17.8 |\n| + Prompting | 18.3 |\n| + Chain-of-Thought | 15.6 |\n| + Paraphrase | 18.7 |\n| + Auto Calibration | 20.7 |\n| + Contextual Calibration | 7.3 |\n\nError Bias = N(target-prefer-other-win)/N(other-win) − N(other-prefer-target-win)/N(target-win). Dataset: PPE, MTBench, Human Preference datasets, filtered for GPT-4 vs GPT-4 student (Vicuna, Alpaca) pairs.\n\n### Table 9: Stability (Mean &amp; Variance, Mistral-7B-v0.1)\n\n| Model Pair | Benchmark | Mean | Variance |\n|-----------|-----------|------|----------|\n| Mistral-GPT4o vs Mistral-Gemini | Arena-Hard | 28.67 | 0.063 |\n| Mistral-GPT4o vs Mistral-LLaMA | Arena-Hard | 0.50 | 0.910 |\n| Mistral-LLaMA vs Mistral-Gemini | Arena-Hard | 12.93 | 0.583 |\n| Mistral-GPT4o vs Mistral-Gemini | AlpacaEval | 19.20 | 0.490 |\n| Mistral-GPT4o vs Mistral-LLaMA | AlpacaEval | 0.20 | 1.240 |\n| Mistral-LLaMA vs Mistral-Gemini | AlpacaEval | 19.87 | 0.013 |\n\n### Table 10: Prompt Sensitivity (two evaluation prompts)\n\n| Judge Pair | Dataset | Prompt 1 | Prompt 2 |\n|-----------|---------|----------|----------|\n| GPT-4o &amp; Gemini-1.5 | AlpacaEval | 18.4% | 16.5% |\n| GPT-4o &amp; Gemini-1.5 | Arena-Hard | 28.7% | 38.7% |\n| GPT-4o &amp; LLaMA-3.3 | AlpacaEval | 1.4% | -1.2% |\n| GPT-4o &amp; LLaMA-3.3 | Arena-Hard | -1.5% | 4.5% |\n| LLaMA-3.3 &amp; Gemini-1.5 | AlpacaEval | 19.8% | 17.9% |\n| LLaMA-3.3 &amp; Gemini-1.5 | Arena-Hard | 13.1% | 15.8% |\n\nResults are robust to prompt variation. Direction is consistent; magnitude varies modestly.\n\n### Table 11: Bootstrap Significance (n=10,000 resamples)\n\n| Judge Pair | Student | PLS (%) | Significance |\n|-----------|---------|---------|--------------|\n| GPT-4o &amp; Gemini-1.5 | Mistral-7B | 28.5 | *** (p&lt;0.001) |\n| GPT-4o &amp; LLaMA-3.3 | Mistral-7B | -1.1 | n.s. |\n| LLaMA-3.3 &amp; Gemini-1.5 | Mistral-7B | 7.4 | ** (p&lt;0.01) |\n| GPT-4o &amp; Gemini-1.5 | Qwen-2.5-14B | 37.9 | *** |\n| GPT-4o &amp; LLaMA-3.3 | Qwen-2.5-14B | 1.2 | n.s. |\n| LLaMA-3.3 &amp; Gemini-1.5 | Qwen-2.5-14B | 26.3 | *** |\n\n### Table 12: Cross-lingual PLS (GPT-4o &amp; Gemini-1.5, Qwen-3-8B student)\n\n| Language | AlpacaEval | Arena-Hard | Average |\n|----------|-----------|-----------|---------|\n| English | 17.4% | 33.9% | 25.7% |\n| Chinese | 12.3% | 51.8% | 32.1% |\n\nPreference leakage generalizes to Chinese; stronger in Arena-Hard for Chinese.\n\n### Table 13: Expanded Judge Pairs (with Claude-3.5-Sonnet)\n\n| Student | Judge Pair | Arena-Hard | AlpacaEval | Avg |\n|---------|-----------|-----------|-----------|-----|\n| Mistral-7B | GPT-4o &amp; Claude-3.5 | 12.2% | 8.6% | 10.4% |\n| Mistral-7B | Gemini &amp; Claude-3.5 | 16.5% | 7.1% | 11.8% |\n| Mistral-7B | LLaMA-3.3 &amp; Claude-3.5 | -4.4% | -2.6% | -3.5% |\n| Qwen-2.5-14B | GPT-4o &amp; Claude-3.5 | 13.0% | 10.4% | 11.7% |\n| Qwen-2.5-14B | Gemini &amp; Claude-3.5 | 18.5% | 11.1% | 14.8% |\n| Qwen-2.5-14B | LLaMA-3.3 &amp; Claude-3.5 | 0.0% | 1.7% | 0.9% |\n\nClaude-3.5-Sonnet (unrelated to training data generators) shows: GPT-4o and Gemini pairings still show positive leakage (10-15%), LLaMA-3.3 pairings near zero or negative.\n\n### Table 14: Student Model Size Scaling\n\n| Student Model | Arena-Hard | AlpacaEval | Avg |\n|--------------|-----------|-----------|-----|\n| LLaMA-3-1B | 35.4% | 18.2% | 26.8% |\n| LLaMA-3-3B | 32.5% | 16.4% | 24.5% |\n| LLaMA-3-8B | 30.9% | 15.8% | 23.4% |\n| Qwen-2.5-0.5B | 40.9% | 21.2% | 31.1% |\n| Qwen-2.5-1.5B | 38.0% | 23.2% | 30.6% |\n| Qwen-2.5-3B | 50.7% | 20.1% | 35.4% |\n| Qwen-2.5-7B | 32.2% | 22.1% | 27.2% |\n| Qwen-2.5-14B | 37.1% | 18.6% | 27.9% |\n| Qwen-3-0.6B | 39.8% | 23.8% | 31.8% |\n| Qwen-3-1.7B | 40.0% | 20.1% | 30.2% |\n| Qwen-3-4B | 30.9% | 17.2% | 24.1% |\n| Qwen-3-8B | 33.9% | 17.4% | 25.7% |\n| Qwen-3-14B | 31.7% | 19.4% | 25.6% |\n\nGeneral trend: smaller models show higher PLS; Qwen-2.5-3B anomalously highest (50.7% Arena-Hard).\n\n---\n\n## 7. FIGURE &amp; TABLE CAPTIONS (EXACT TEXT)\n\n**Figure 1:** Overview of preference leakage. We make a comparison between data leakage and preference leakage and present three types of relatedness: being the same model, having an inheritance relationship and belonging to the same model family.\n\n**Figure 2(a):** PLS on models with various sizes. We conduct the experiment with GPT-4o and Gemini as data generators and judges.\n\n**Figure 2(b):** Experiment results on data mixing. 'Manual' and 'Synthetic' represent mixing with manually-written data and other synthetic data, respectively.\n\n**Figure 3(a):** Question Type (category analysis of preference leakage by question type)\n\n**Figure 3(b):** Judgment dimension (category analysis of preference leakage by evaluation dimension)\n\n**Table 1:** Preference leakage score result on Arena-Hard and AlpacaEval 2.0. The blue background indicates a negative preference leakage score value and the purple background indicates a positive value. The deeper the color, the larger the absolute value.\n\n**Table 2:** Preference leakage score in different relatedness between the data generator and the judging LLM.\n\n**Table 3:** Preference leakage score in different learning methods.\n\n**Table 4:** Impact analysis of preference leakage in real-world LLM-as-a-Judge leaderboards. For each bias type, we assess its impact by calculating the ranking difference of the corresponding model in LMArena and AlpacaEval 2.0, obtained by subtracting the ranking in AlpacaEval 2.0 from that in LMArena. A larger positive ranking difference indicates AlpacaEval 2.0 ranks the target models in higher positions, denoting a greater impact of the corresponding bias.\n\n**Table 5:** Student recognition (binary classification) and response classification results (three-class classification). SR: Student Recognition, RC: Response Classification.\n\n**Table 6:** Effect of removing spurious features on the PLS. We consider style, format and wording as potential spurious features in this analysis.\n\n**Table 7:** Error Bias with various mitigation methods (lower is better).\n\n**Table 8:** A case on AlpacaEval 2.0 with the model pair Mistral-GPT-4o vs Mistral-Gemini-1.5 to demonstrate how the preference leakage score is calculated.\n\n**Table 9:** Mean and variance of experimental results across two benchmarks in Mistral-7B-v0.1.\n\n**Table 10:** PLS under different evaluation prompts.\n\n**Table 11:** Bootstrap significance results for PLS &gt; 0. ***: p&lt;0.001, **: p&lt;0.01.\n\n**Table 12:** PLS in English vs. Chinese.\n\n**Table 13:** PLS of new judge pairs (negative values indicate no leakage).\n\n**Table 14:** PLS (%) for different student sizes.\n\n---\n\n## 8. IMPLEMENTATION DETAILS\n\n- Library: LLaMA-Factory (Zheng et al. 2024)\n- Max sequence length: 1024 tokens\n- Data preprocessing: 16 parallel workers\n- SFT: batch size 2/device, gradient accumulation 2 steps\n- DPO: batch size 1/device, gradient accumulation 4 steps\n- Learning rate: 1.0e-5\n- Training: 3 epochs\n- LR scheduler: cosine with warmup ratio 0.1\n- Precision: BF16\n- Hardware: 8× Nvidia A100 GPUs, CUDA 11.8\n\n---\n\n## 9. ABLATION STUDIES SUMMARY\n\n1. **Data mixing** (10%/30%/50%/70% synthetic + manual or multi-source synthetic to 30k total): PLS increases monotonically with synthetic proportion; no safe threshold exists — leakage occurs even at 10%.\n\n2. **Relatedness** (Table 2): Same model &gt; Inheritance-diff-instructions &gt; Inheritance-same-instructions &gt; Same-family-same-series &gt; Same-family-diff-series. Leakage degrades smoothly with relatedness distance.\n\n3. **Learning method** (Table 3): SFT 23.6% &gt;&gt; DPO 5.2% &gt;&gt; ICL -2.7%. Pairwise optimization (DPO) and no-tuning (ICL) substantially suppress leakage.\n\n4. **Spurious features** (Table 6): Style and format removal each ~halve leakage for high-leakage pairs; wording removal minimal. GPT-family judges sensitive to style; LLaMA-family judges sensitive to format.\n\n5. **Mitigation** (Table 7): Contextual calibration reduces Error Bias from 17.8 to 7.3 (59% reduction). Prompting, paraphrase, auto-calibration all either neutral or counterproductive.\n\n6. **Model size** (Table 14): Smaller student models → higher PLS. Opposite to traditional data contamination where larger models memorize more.\n\n---\n\n## 10. QUESTION TYPE &amp; JUDGMENT DIMENSION ANALYSIS\n\n(Figure 3; Section 5.6)\n\n**Question types:** Classified using Arena-Hard clusters mapped by GPT-4o. Objective questions (e.g., math) show least preference leakage. Subjective questions (programming, writing) show more obvious leakage.\n\n**Judgment dimensions:** Following Liu et al. (2023a), GPT-4o maps judge rationales to dimensions. Objective dimensions (e.g., completeness) show lower leakage than subjective dimensions (e.g., fairness).\n\n**Mechanism:** Preference leakage is subtler and harder to detect in subjective domains where there is no single correct answer — creating more opportunity for stylistic/format artifacts to drive judge decisions.\n\n---\n\n## 11. LIMITATIONS / FUTURE WORK\n\nNo dedicated \"Limitations\" section, but stated limitations include:\n\n1. **Leaderboard scope:** Broader leaderboard coverage would enhance external validity, but few student–teacher distillation pairs are publicly documented, and most leaderboards lack metadata for controlled cross-model comparisons. Re-evaluating all leaderboard entries computationally prohibitive. Focus restricted to AlpacaEval and LMArena as interpretable case studies; large-scale multi-judge re-evaluations left for future work.\n\n2. **Detection challenge:** Judge LLMs cannot reliably detect their own related student models' generation (~random performance in recognition). External detectors estimating model-relatedness could provide auxiliary confidence signals to calibrate or penalize biased judgments — identified as a future research direction.\n\n3. **Quantifying generator leakage:** Different data generator LLMs contribute varying degrees of leakage (Gemini-1.5 &gt; GPT-4o &gt; LLaMA-3.3 based on manual annotation). Future work should quantify the extent of leaked preference for each data generator model.\n\n4. **Mitigation incompleteness:** Contextual calibration reduces but does not eliminate Error Bias (17.8 → 7.3). More effective mitigation methods needed.\n\n---\n\n## 12. CONCLUSION (FULL TEXT)\n\nIn this work, we formally highlight the preference leakage problem in LLM-as-a-judge systems. The results of our main experiment, measured using the proposed preference leakage score, reveal a clear bias in each judge toward their respective student model. We also observe that this bias is more pronounced in certain question types and smaller student models. Furthermore, we conduct additional analysis on various factors, including the relationship between the data generator and judge LLMs, model tuning techniques, data mixing strategies, and real-world applications. Our findings suggest that preference leakage can cause significant bias across diverse scenarios. Finally, we investigate the underlying mechanisms of preference leakage, demonstrating that it is a challenging and hard-to-detect issue, especially in subjective questions and judgment dimensions.\n\n---\n\n## 13. RELATED WORK (KEY POINTS)\n\nThree areas covered:\n\n**LLM-as-a-Judge:** Zheng et al. (2023) foundational; Li et al., Jiang et al., Zhong et al. follow-up frameworks; open-source alternatives like Prometheus; known vulnerabilities including egocentric bias (Panickssery et al. 2024), length bias.\n\n**Data Leakage:** Traditional data contamination detection via retrieval-based approaches and output distribution analysis. Bordt et al. (2024): larger models more susceptible to traditional contamination (inverse of preference leakage finding).\n\n**Distinction from prior work:** Preference leakage presents \"more complex and dynamic challenges\" than egocentric bias — stems from varied relatedness types and synthetic data flows, not just self-evaluation. Subtler because: (1) most LLMs don't disclose training data, (2) judge LLMs cannot recognize related student outputs at above-chance rates.\n\n---\n\n## 14. APPENDIX B: REAL-WORLD PREVALENCE\n\nThe preliminary study examines AlpacaEval 2.0, Arena-Hard, and MTBench leaderboards. Candidate models distilled from GPT-4 (Vicuna, Alpaca, etc.) appear consistently across leaderboards. When GPT-4 or GPT-4-based models serve as evaluators, these student models receive inflated rankings. The Appendix documents specific model pairs and leaderboard positions to demonstrate that preference leakage is not a hypothetical concern but an ongoing empirical reality in published benchmarks.\n\n---\n\n**[DISTILL_DONE]**&lt;/result>\n&lt;usage>&lt;total_tokens>33959&lt;/total_tokens>&lt;tool_uses>6&lt;/tool_uses>&lt;duration_ms>328829&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
````

---


### Runtime record

_source line 85 · 2026-05-21T16:43:27.773Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T16:43:27.773Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


## Round 4

## Round 4

97 recorded events


### User

_source line 86 · 2026-05-21T16:43:27.781Z_

&lt;task-notification>
&lt;task-id>ade7e6bb7f61dc1fb&lt;/task-id>
&lt;tool-use-id>toolu_0186HRHtg5zTNLH6chQsgrwp&lt;/tool-use-id>
&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ade7e6bb7f61dc1fb.output&lt;/output-file>
&lt;status>completed&lt;/status>
&lt;summary>Agent "Fetch paper: preference_leakage2026" completed&lt;/summary>
&lt;result>I now have comprehensive data from the paper. Here is the complete extracted information:

---

## Paper: "Preference Leakage: A Contamination Problem in LLM-as-a-judge"

**ArXiv:** 2502.01534 | **Venue:** ICLR 2026 | **Authors:** Dawei Li, Renliang Sun, Yue Huang, Ming Zhong, Bohan Jiang, Jiawei Han, Xiangliang Zhang, Wei Wang, Huan Liu | **Submitted:** Feb 3, 2025 | **Latest version:** Mar 4, 2026 (v3)

---

## 1. ABSTRACT

LLM-as-judge and LLM-based data synthesis are two fundamental LLM-driven data annotation methods. The paper introduces "preference leakage" — a contamination issue arising when the LLMs used for data generation and evaluation are closely related, causing the evaluator's preferences to leak to the student models through synthetic data, inflating evaluation scores. Three relatedness types are defined: same model, inheritance relationship, same model family. Experiments on Arena-Hard and AlpacaEval 2.0 with GPT-4o, Gemini-1.5-flash, and LLaMA-3.3-70B demonstrate systematic bias. The PLS metric quantifies the bias; the effect is more pronounced for subjective questions and smaller student models.

---

## 2. FULL INTRODUCTION (ALL PARAGRAPHS)

**Paragraph 1:** Recent advancements in LLMs have empowered various downstream tasks and applications. However, this poses substantial challenges to automatic evaluation. LLM-based AI agents' focus transfer from traditional NLP tasks to real-world, open-ended response generation greatly limits the applicability of traditional n-gram matching methods (BLEU, ROUGE) or model-based evaluators.

**Paragraph 2:** To address these challenges, the LLM-as-a-judge paradigm has been proposed to leverage LLMs as evaluators to assess response quality. By combining powerful LLMs with well-designed prompting strategies, LLM-as-a-judge enables human-like evaluation of long-form and open-ended generation in a more cost-efficient and scalable manner. However, recent studies point out weaknesses; Ye et al. (2024) explores various biases and vulnerabilities, highlighting the importance of developing reliable and fair LLM-based evaluation.

**Paragraph 3:** This work highlights a subtle yet critical bias in LLM-as-a-Judge: **Preference Leakage**. This issue arises when the LLMs used for data generation and evaluation are closely related, causing the preference of the LLM evaluators to leak to the student models through synthetic data, thus inflating evaluation scores (as illustrated in Figure 1). Synthetic data has become a cornerstone of model training. When combined with LLM-as-a-Judge, they offer significant efficiency gains. However, limited attention has been given to the potential contamination when the generator and evaluator LLMs share a close relationship. This issue is particularly pervasive in popular benchmarks (AlpacaEval 2.0, Arena-Hard) and LLM-relevant studies (see Appendix B), due to common reliance on the most advanced LLMs like GPT-4 for both data synthesis and evaluation. The relatedness — akin to overlap between training data and evaluation sets in traditional data contamination — introduces systematic bias of judge LLMs toward their related student models. Compared to other biases such as length bias or egocentric bias, preference leakage is subtler and more challenging to detect, especially since most LLMs do not disclose their training data.

**Paragraph 4 (RQ definitions):**
To investigate the preference leakage problem, the authors define three relatedness types between data generator LLM and judge LLM: being the same model, having an inheritance relationship, and belonging to the same model family. Three core research questions:

- **RQ1:** Does preference leakage introduce systematic biases in LLM-based evaluation? Addressed via experiments with various LLM baselines on two benchmarks, using the preference leakage score to quantify bias. Results show obvious bias of judging LLMs toward their related student models.

- **RQ2:** What is the severity of preference leakage under various scenarios? Covered via experiments under various data mixing strategies, relatedness settings, tuning techniques, and real-world applications. Preference leakage consistently affects judge LLMs. Severity correlates with degree of relatedness between data generator and judge, as well as proportion of synthetic data.

- **RQ3:** What are the underlying mechanisms causing preference leakage? Analyzed via LLMs' recognition capabilities on their related student models' generation and distribution of bias across different question types and judgment dimensions. Preference leakage is subtle and hard-to-detect, particularly affecting subjective questions and judgment dimensions.

---

## 3. CONTRIBUTION STATEMENTS

- For the first time, we introduce preference leakage, a contamination issue arising from the relatedness between the data generator and judge LLMs.
- We conduct extensive experiments across various LLMs and benchmarks to study how and to what extent the potential bias brought by preference leakage influences judgment.
- Our further analysis reveals that preference leakage is prevalent in diverse scenarios and difficult for judge LLMs to detect, providing valuable insights for future research on this challenging issue.

---

## 4. METHOD DETAILS

### Formal Definition

Entities:
- **Data Generator LLM M_G**: defines conditional distribution P_M_G(y|x), forms synthetic dataset D_syn
- **Student LLM M_S**: trained on data generated by M_G, producing output distribution P_M_S(y|x)
- **Judge LLM M_J**: provides scoring function S_M_J(y|x)

Preference leakage occurs when:

`E[S_M_J(y_S|x) | M_G ~_rel M_J] &gt; E[S_M_J'(y_S|x) | M_G ≁_rel M_J']`

M_J may favor M_S outputs not solely based on intrinsic quality, but because they exhibit spurious features (style, format, wording) inherited from M_G.

### Three Relatedness Types

1. **Same Model:** M_G ≡ M_J — inherent generative preferences identical to evaluation preferences.

2. **Inheritance Relationship:** M_J ← FineTune(M_G, D_train) or M_J ← FineTune(M_base, D_syn_G) — descendant model internalizes and favors preferences/styles of its progenitor. Bidirectional.

3. **Same Model Family:** M_G and M_J share common architectural blueprint (A_X) and pre-training on substantially overlapping datasets (D_X), leading to correlated preferences and systemic biases. M_k ∈ Family(A_X, D_X) for k ∈ {G, J}.

---

## 5. EXPERIMENTS

### Datasets &amp; Models

**Evaluation benchmarks:**
- **Arena-Hard**: 500 challenging English questions; 96.7% Spearman correlation with LMArena hard prompts
- **AlpacaEval 2.0**: 805 questions; reduces text length effect vs. v1.0

**Generator/Judge models:** GPT-4o-2024-11-20, Gemini-1.5-flash, LLaMA-3.3-70B-Instruct-turbo

**Student models:** Mistral-7B-v0.1, Qwen-2.5-14B (pre-trained versions, not instruct)

**Synthetic data:** 30,000 prompts sampled from Ultrafeedback dataset (includes TruthfulQA, FalseQA, Evol-Instruct). Each generator produces one synthetic dataset. Three student model versions per base model: Mistral/Qwen-GPT-4o, Mistral/Qwen-Gemini-1.5, Mistral/Qwen-LLaMA-3.3.

### Preference Leakage Score (PLS) Metric

```
PLS(i,j) = [(WR(i,i) - AVG(i,j))/AVG(i,j) + (WR(j,j) - AVG(j,i))/AVG(j,i)] / 2
AVG(i,j) = [WR(i,i) + WR(i,j)] / 2
```

WR(i,j) = win-rate from judge model j to student model i. Large PLS = strong bias toward related student models.

---

## 6. ALL RESULTS WITH NUMBERS

### Table 1: Main PLS Results (Arena-Hard &amp; AlpacaEval 2.0)

| Student | Judge Pair | Arena-Hard | AlpacaEval 2.0 | Avg |
|---------|-----------|-----------|----------------|-----|
| Mistral-7B | GPT-4o &amp; Gemini-1.5 | 28.7% | 18.4% | 23.6% |
| Mistral-7B | GPT-4o &amp; LLaMA-3.3 | -1.5% | 1.4% | -0.1% |
| Mistral-7B | LLaMA-3.3 &amp; Gemini-1.5 | 13.1% | 19.8% | 16.4% |
| Qwen-2.5-14B | GPT-4o &amp; Gemini-1.5 | 37.1% | 18.6% | 27.9% |
| Qwen-2.5-14B | GPT-4o &amp; LLaMA-3.3 | 1.0% | 2.3% | 1.7% |
| Qwen-2.5-14B | LLaMA-3.3 &amp; Gemini-1.5 | 25.4% | 18.4% | 21.9% |

**Key finding:** Preference leakage exists in most model pairs except GPT-4o &amp; LLaMA-3.3 (near zero), where LLaMA-3.3 lacks strong relatedness to GPT-4o.

### Table 2: PLS by Relatedness Type (Mistral-7B, GPT-4o &amp; Gemini-1.5)

| Relatedness Type | Arena-Hard | AlpacaEval 2.0 | Avg |
|-----------------|-----------|----------------|-----|
| Same Model | 28.7% | 18.4% | 23.6% |
| Inheritance – same instructions | 17.8% | 20.7% | 19.3% |
| Inheritance – different instructions | 18.3% | 26.3% | 22.3% |
| Same Family – same series | 10.1% | 7.6% | 8.9% |
| Same Family – different series | 3.3% | 2.2% | 2.8% |

### Table 3: PLS by Learning Method (Mistral-7B, GPT-4o vs Gemini-1.5)

| Method | Arena-Hard | AlpacaEval 2.0 | Avg |
|--------|-----------|----------------|-----|
| SFT | 28.7% | 18.4% | 23.6% |
| DPO | 7.7% | 2.7% | 5.2% |
| ICL | -4.2% | -1.1% | -2.7% |

SFT data pool: OASST, LIMA, MOSS. DPO: 2 responses per instruction, pairwise feedback from each generator. ICL: 4 demonstration pairs per LLM's synthetic dataset.

### Table 4: Real-World Leaderboard Impact

| Bias Type | Evaluator | Target Models | Ranking Difference |
|-----------|-----------|---------------|-------------------|
| Egocentric Bias | GPT-4 Preview | GPT-4 Preview | 1.00 |
| Preference Leakage | GPT-4 | Vicuna 7B/13B/33B | 1.33 |

Ranking difference = LMArena rank minus AlpacaEval 2.0 rank. Preference leakage produces larger ranking inflation than egocentric bias.

### Table 5: Student Recognition Results

| Task | Model | Pointwise Acc. | Pairwise Acc. |
|------|-------|----------------|---------------|
| Student Recognition | GPT-4o | 41.0% | 52.0% |
| Student Recognition | Gemini-1.5 | 53.2% | 44.2% |
| Student Recognition | LLaMA-3.3 | 41.8% | 29.8% |
| Response Classification | BERT (3-class) | 82.4% | — |

Random baseline for binary recognition: 50%. Judge LLMs perform at/near random; BERT classifier achieves 82.4%, confirming stylistic fingerprints exist but are invisible to LLM judges.

### Table 6: Spurious Feature Ablation (Qwen-3-8B rewriter, Gemini-2.0 judge)

| Setting | GPT &amp; Gemini | GPT &amp; LLaMA | LLaMA &amp; Gemini |
|---------|-------------|-------------|----------------|
| Baseline | 17.5% | 2.3% | 18.8% |
| –style | 9.0% | 3.3% | 14.6% |
| –format | 9.8% | 1.9% | 14.5% |
| –wording | 11.2% | 2.4% | 18.2% |

Style and format removal each roughly halve leakage for the two high-leakage pairs. Wording removal has minimal effect.

### Table 7: Mitigation Methods (Error Bias, lower = better)

| Method | Error Bias |
|--------|-----------|
| Base | 17.8 |
| + Prompting | 18.3 |
| + Chain-of-Thought | 15.6 |
| + Paraphrase | 18.7 |
| + Auto Calibration | 20.7 |
| + Contextual Calibration | 7.3 |

Error Bias = N(target-prefer-other-win)/N(other-win) − N(other-prefer-target-win)/N(target-win). Dataset: PPE, MTBench, Human Preference datasets, filtered for GPT-4 vs GPT-4 student (Vicuna, Alpaca) pairs.

### Table 9: Stability (Mean &amp; Variance, Mistral-7B-v0.1)

| Model Pair | Benchmark | Mean | Variance |
|-----------|-----------|------|----------|
| Mistral-GPT4o vs Mistral-Gemini | Arena-Hard | 28.67 | 0.063 |
| Mistral-GPT4o vs Mistral-LLaMA | Arena-Hard | 0.50 | 0.910 |
| Mistral-LLaMA vs Mistral-Gemini | Arena-Hard | 12.93 | 0.583 |
| Mistral-GPT4o vs Mistral-Gemini | AlpacaEval | 19.20 | 0.490 |
| Mistral-GPT4o vs Mistral-LLaMA | AlpacaEval | 0.20 | 1.240 |
| Mistral-LLaMA vs Mistral-Gemini | AlpacaEval | 19.87 | 0.013 |

### Table 10: Prompt Sensitivity (two evaluation prompts)

| Judge Pair | Dataset | Prompt 1 | Prompt 2 |
|-----------|---------|----------|----------|
| GPT-4o &amp; Gemini-1.5 | AlpacaEval | 18.4% | 16.5% |
| GPT-4o &amp; Gemini-1.5 | Arena-Hard | 28.7% | 38.7% |
| GPT-4o &amp; LLaMA-3.3 | AlpacaEval | 1.4% | -1.2% |
| GPT-4o &amp; LLaMA-3.3 | Arena-Hard | -1.5% | 4.5% |
| LLaMA-3.3 &amp; Gemini-1.5 | AlpacaEval | 19.8% | 17.9% |
| LLaMA-3.3 &amp; Gemini-1.5 | Arena-Hard | 13.1% | 15.8% |

Results are robust to prompt variation. Direction is consistent; magnitude varies modestly.

### Table 11: Bootstrap Significance (n=10,000 resamples)

| Judge Pair | Student | PLS (%) | Significance |
|-----------|---------|---------|--------------|
| GPT-4o &amp; Gemini-1.5 | Mistral-7B | 28.5 | *** (p&lt;0.001) |
| GPT-4o &amp; LLaMA-3.3 | Mistral-7B | -1.1 | n.s. |
| LLaMA-3.3 &amp; Gemini-1.5 | Mistral-7B | 7.4 | ** (p&lt;0.01) |
| GPT-4o &amp; Gemini-1.5 | Qwen-2.5-14B | 37.9 | *** |
| GPT-4o &amp; LLaMA-3.3 | Qwen-2.5-14B | 1.2 | n.s. |
| LLaMA-3.3 &amp; Gemini-1.5 | Qwen-2.5-14B | 26.3 | *** |

### Table 12: Cross-lingual PLS (GPT-4o &amp; Gemini-1.5, Qwen-3-8B student)

| Language | AlpacaEval | Arena-Hard | Average |
|----------|-----------|-----------|---------|
| English | 17.4% | 33.9% | 25.7% |
| Chinese | 12.3% | 51.8% | 32.1% |

Preference leakage generalizes to Chinese; stronger in Arena-Hard for Chinese.

### Table 13: Expanded Judge Pairs (with Claude-3.5-Sonnet)

| Student | Judge Pair | Arena-Hard | AlpacaEval | Avg |
|---------|-----------|-----------|-----------|-----|
| Mistral-7B | GPT-4o &amp; Claude-3.5 | 12.2% | 8.6% | 10.4% |
| Mistral-7B | Gemini &amp; Claude-3.5 | 16.5% | 7.1% | 11.8% |
| Mistral-7B | LLaMA-3.3 &amp; Claude-3.5 | -4.4% | -2.6% | -3.5% |
| Qwen-2.5-14B | GPT-4o &amp; Claude-3.5 | 13.0% | 10.4% | 11.7% |
| Qwen-2.5-14B | Gemini &amp; Claude-3.5 | 18.5% | 11.1% | 14.8% |
| Qwen-2.5-14B | LLaMA-3.3 &amp; Claude-3.5 | 0.0% | 1.7% | 0.9% |

Claude-3.5-Sonnet (unrelated to training data generators) shows: GPT-4o and Gemini pairings still show positive leakage (10-15%), LLaMA-3.3 pairings near zero or negative.

### Table 14: Student Model Size Scaling

| Student Model | Arena-Hard | AlpacaEval | Avg |
|--------------|-----------|-----------|-----|
| LLaMA-3-1B | 35.4% | 18.2% | 26.8% |
| LLaMA-3-3B | 32.5% | 16.4% | 24.5% |
| LLaMA-3-8B | 30.9% | 15.8% | 23.4% |
| Qwen-2.5-0.5B | 40.9% | 21.2% | 31.1% |
| Qwen-2.5-1.5B | 38.0% | 23.2% | 30.6% |
| Qwen-2.5-3B | 50.7% | 20.1% | 35.4% |
| Qwen-2.5-7B | 32.2% | 22.1% | 27.2% |
| Qwen-2.5-14B | 37.1% | 18.6% | 27.9% |
| Qwen-3-0.6B | 39.8% | 23.8% | 31.8% |
| Qwen-3-1.7B | 40.0% | 20.1% | 30.2% |
| Qwen-3-4B | 30.9% | 17.2% | 24.1% |
| Qwen-3-8B | 33.9% | 17.4% | 25.7% |
| Qwen-3-14B | 31.7% | 19.4% | 25.6% |

General trend: smaller models show higher PLS; Qwen-2.5-3B anomalously highest (50.7% Arena-Hard).

---

## 7. FIGURE &amp; TABLE CAPTIONS (EXACT TEXT)

**Figure 1:** Overview of preference leakage. We make a comparison between data leakage and preference leakage and present three types of relatedness: being the same model, having an inheritance relationship and belonging to the same model family.

**Figure 2(a):** PLS on models with various sizes. We conduct the experiment with GPT-4o and Gemini as data generators and judges.

**Figure 2(b):** Experiment results on data mixing. 'Manual' and 'Synthetic' represent mixing with manually-written data and other synthetic data, respectively.

**Figure 3(a):** Question Type (category analysis of preference leakage by question type)

**Figure 3(b):** Judgment dimension (category analysis of preference leakage by evaluation dimension)

**Table 1:** Preference leakage score result on Arena-Hard and AlpacaEval 2.0. The blue background indicates a negative preference leakage score value and the purple background indicates a positive value. The deeper the color, the larger the absolute value.

**Table 2:** Preference leakage score in different relatedness between the data generator and the judging LLM.

**Table 3:** Preference leakage score in different learning methods.

**Table 4:** Impact analysis of preference leakage in real-world LLM-as-a-Judge leaderboards. For each bias type, we assess its impact by calculating the ranking difference of the corresponding model in LMArena and AlpacaEval 2.0, obtained by subtracting the ranking in AlpacaEval 2.0 from that in LMArena. A larger positive ranking difference indicates AlpacaEval 2.0 ranks the target models in higher positions, denoting a greater impact of the corresponding bias.

**Table 5:** Student recognition (binary classification) and response classification results (three-class classification). SR: Student Recognition, RC: Response Classification.

**Table 6:** Effect of removing spurious features on the PLS. We consider style, format and wording as potential spurious features in this analysis.

**Table 7:** Error Bias with various mitigation methods (lower is better).

**Table 8:** A case on AlpacaEval 2.0 with the model pair Mistral-GPT-4o vs Mistral-Gemini-1.5 to demonstrate how the preference leakage score is calculated.

**Table 9:** Mean and variance of experimental results across two benchmarks in Mistral-7B-v0.1.

**Table 10:** PLS under different evaluation prompts.

**Table 11:** Bootstrap significance results for PLS &gt; 0. ***: p&lt;0.001, **: p&lt;0.01.

**Table 12:** PLS in English vs. Chinese.

**Table 13:** PLS of new judge pairs (negative values indicate no leakage).

**Table 14:** PLS (%) for different student sizes.

---

## 8. IMPLEMENTATION DETAILS

- Library: LLaMA-Factory (Zheng et al. 2024)
- Max sequence length: 1024 tokens
- Data preprocessing: 16 parallel workers
- SFT: batch size 2/device, gradient accumulation 2 steps
- DPO: batch size 1/device, gradient accumulation 4 steps
- Learning rate: 1.0e-5
- Training: 3 epochs
- LR scheduler: cosine with warmup ratio 0.1
- Precision: BF16
- Hardware: 8× Nvidia A100 GPUs, CUDA 11.8

---

## 9. ABLATION STUDIES SUMMARY

1. **Data mixing** (10%/30%/50%/70% synthetic + manual or multi-source synthetic to 30k total): PLS increases monotonically with synthetic proportion; no safe threshold exists — leakage occurs even at 10%.

2. **Relatedness** (Table 2): Same model &gt; Inheritance-diff-instructions &gt; Inheritance-same-instructions &gt; Same-family-same-series &gt; Same-family-diff-series. Leakage degrades smoothly with relatedness distance.

3. **Learning method** (Table 3): SFT 23.6% &gt;&gt; DPO 5.2% &gt;&gt; ICL -2.7%. Pairwise optimization (DPO) and no-tuning (ICL) substantially suppress leakage.

4. **Spurious features** (Table 6): Style and format removal each ~halve leakage for high-leakage pairs; wording removal minimal. GPT-family judges sensitive to style; LLaMA-family judges sensitive to format.

5. **Mitigation** (Table 7): Contextual calibration reduces Error Bias from 17.8 to 7.3 (59% reduction). Prompting, paraphrase, auto-calibration all either neutral or counterproductive.

6. **Model size** (Table 14): Smaller student models → higher PLS. Opposite to traditional data contamination where larger models memorize more.

---

## 10. QUESTION TYPE &amp; JUDGMENT DIMENSION ANALYSIS

(Figure 3; Section 5.6)

**Question types:** Classified using Arena-Hard clusters mapped by GPT-4o. Objective questions (e.g., math) show least preference leakage. Subjective questions (programming, writing) show more obvious leakage.

**Judgment dimensions:** Following Liu et al. (2023a), GPT-4o maps judge rationales to dimensions. Objective dimensions (e.g., completeness) show lower leakage than subjective dimensions (e.g., fairness).

**Mechanism:** Preference leakage is subtler and harder to detect in subjective domains where there is no single correct answer — creating more opportunity for stylistic/format artifacts to drive judge decisions.

---

## 11. LIMITATIONS / FUTURE WORK

No dedicated "Limitations" section, but stated limitations include:

1. **Leaderboard scope:** Broader leaderboard coverage would enhance external validity, but few student–teacher distillation pairs are publicly documented, and most leaderboards lack metadata for controlled cross-model comparisons. Re-evaluating all leaderboard entries computationally prohibitive. Focus restricted to AlpacaEval and LMArena as interpretable case studies; large-scale multi-judge re-evaluations left for future work.

2. **Detection challenge:** Judge LLMs cannot reliably detect their own related student models' generation (~random performance in recognition). External detectors estimating model-relatedness could provide auxiliary confidence signals to calibrate or penalize biased judgments — identified as a future research direction.

3. **Quantifying generator leakage:** Different data generator LLMs contribute varying degrees of leakage (Gemini-1.5 &gt; GPT-4o &gt; LLaMA-3.3 based on manual annotation). Future work should quantify the extent of leaked preference for each data generator model.

4. **Mitigation incompleteness:** Contextual calibration reduces but does not eliminate Error Bias (17.8 → 7.3). More effective mitigation methods needed.

---

## 12. CONCLUSION (FULL TEXT)

In this work, we formally highlight the preference leakage problem in LLM-as-a-judge systems. The results of our main experiment, measured using the proposed preference leakage score, reveal a clear bias in each judge toward their respective student model. We also observe that this bias is more pronounced in certain question types and smaller student models. Furthermore, we conduct additional analysis on various factors, including the relationship between the data generator and judge LLMs, model tuning techniques, data mixing strategies, and real-world applications. Our findings suggest that preference leakage can cause significant bias across diverse scenarios. Finally, we investigate the underlying mechanisms of preference leakage, demonstrating that it is a challenging and hard-to-detect issue, especially in subjective questions and judgment dimensions.

---

## 13. RELATED WORK (KEY POINTS)

Three areas covered:

**LLM-as-a-Judge:** Zheng et al. (2023) foundational; Li et al., Jiang et al., Zhong et al. follow-up frameworks; open-source alternatives like Prometheus; known vulnerabilities including egocentric bias (Panickssery et al. 2024), length bias.

**Data Leakage:** Traditional data contamination detection via retrieval-based approaches and output distribution analysis. Bordt et al. (2024): larger models more susceptible to traditional contamination (inverse of preference leakage finding).

**Distinction from prior work:** Preference leakage presents "more complex and dynamic challenges" than egocentric bias — stems from varied relatedness types and synthetic data flows, not just self-evaluation. Subtler because: (1) most LLMs don't disclose training data, (2) judge LLMs cannot recognize related student outputs at above-chance rates.

---

## 14. APPENDIX B: REAL-WORLD PREVALENCE

The preliminary study examines AlpacaEval 2.0, Arena-Hard, and MTBench leaderboards. Candidate models distilled from GPT-4 (Vicuna, Alpaca, etc.) appear consistently across leaderboards. When GPT-4 or GPT-4-based models serve as evaluators, these student models receive inflated rankings. The Appendix documents specific model pairs and leaderboard positions to demonstrate that preference leakage is not a hypothetical concern but an ongoing empirical reality in published benchmarks.

---

**[DISTILL_DONE]**&lt;/result>
&lt;usage>&lt;total_tokens>33959&lt;/total_tokens>&lt;tool_uses>6&lt;/tool_uses>&lt;duration_ms>328829&lt;/duration_ms>&lt;/usage>
&lt;/task-notification>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d33b94c-10b4-45c9-ba44-c5cc1df94e0c",
  "isSidechain": false,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "type": "user",
  "uuid": "ce89e433-0020-48b1-9699-611aa888374d",
  "permissionMode": "bypassPermissions",
  "origin": {
    "kind": "task-notification"
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 87_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "ce89e433-0020-48b1-9699-611aa888374d",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 89 · 2026-05-21T16:43:30.895Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:43:30.895Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "&lt;task-notification>\n&lt;task-id>a744e5363d82fb6b7&lt;/task-id>\n&lt;tool-use-id>toolu_01FnCSPe7dcAgNywdUD8bfxY&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/a744e5363d82fb6b7.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: cyclicjudge2026\" completed&lt;/summary>\n&lt;result>I now have the complete text of the paper. Here is all extracted content:\n\n---\n\n## CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\n\n**arXiv:** 2603.01865v3 (submitted March 2, 2026; updated May 4, 2026)\n**Authors:** Ziyi Zhu¹, Olivier Tieleman¹, Alexey Bukhtiyarov¹, Jinghong Chen²\n**Affiliations:** ¹Slingshot AI, ²Department of Engineering, University of Cambridge\n**Correspondence:** ziyi@slingshotai.com\n\n---\n\n## Abstract (verbatim)\n\nLLM-as-judge evaluation has become standard practice for open-ended model assessment; however, judges exhibit systematic biases that cannot be averaged out by increasing the number of scenarios or generations. These biases are often similar in magnitude to the model differences that benchmarks are designed to detect, resulting in unreliable rankings when single-judge evaluations are used. We introduce a variance decomposition that partitions benchmark score variance into scenario, generation, judge, and residual components. Based on this analysis, CyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy for a fixed judge panel and judge-call budget: the score recovers the panel mean exactly while matching the cost of single-judge evaluation. Empirical results on MT-Bench and MindEval validate the effectiveness of CyclicJudge as predicted, across both general-purpose and domain-specific evaluation settings.\n\n---\n\n## Section 1: Introduction (verbatim)\n\nLLM-as-judge evaluation has become the de facto standard for open-ended model assessment (Zheng et al., 2023). A growing body of work indicates that LLM judges are systematically biased: some models are consistently lenient, others strict, with additional position, verbosity, and self-preference effects (Zheng et al., 2023; Shi et al., 2024; Wang et al., 2024). A standard Analysis of Variance (ANOVA; Fisher, 1925) on our data confirms that judge main effect is highly significant (§4.2).\n\nCrucially, systematic bias does not average away across more scenarios or generations: reducing them requires aggregating across multiple judges. Yet running every judge on every item multiplies evaluation cost by the panel size and sacrifices generation diversity at a fixed budget. Throughout this work, we treat the mean score of a diverse K_tot-judge panel as the reference for evaluation; our goal is to recover this panel mean efficiently.\n\nWe show that CyclicJudge, a round-robin assignment of judges to items, resolves this tension. To establish this formally, we develop a variance decomposition rooted in generalizability theory (Brennan, 2001; Shavelson and Webb, 1991) that separates benchmark score variance into scenario, generation, judge, and residual components.\n\n**Our contributions are:**\n\n1. A mixed-effects model that decomposes benchmark variance into random noise and panel-relative judge offsets, showing they require fundamentally different remedies (§3.1–3.2).\n2. A proof that round-robin cycling achieves lower variance than alternative strategies: it cancels the panel-relative offsets exactly while maximizing generation diversity at any budget (§3.3).\n3. Empirical results on MT-Bench and MindEval validating the effectiveness of CyclicJudge as predicted, across both general-purpose and domain-specific evaluation settings (§4).\n\n---\n\n## Section 2: Related Work (verbatim)\n\n**LLM judge biases and multi-judge approaches.** LLM judges exhibit systematic position bias (Wang et al., 2024; Shi et al., 2024), length bias (Dubois et al., 2024), self-preference (Wataoka et al., 2024), and cognitive biases (Koo et al., 2024); we refer readers to Gu et al. (2024) for a comprehensive survey. Multi-judge panels mitigate these biases by averaging over diverse judge tendencies (Verga et al., 2024), while psychometric reliability analyses further demonstrate that single-judge evaluations yield insufficiently stable scores (Schroeder and Wood-Doughty, 2024).\n\n**Benchmark reliability and generation variance.** Madaan et al. (2025) empirically quantifies variance across hundreds of models and benchmarks, and Alvarado Gonzalez et al. (2025) shows via ANOVA that unrepeated evaluations frequently produce rank inversions across benchmark subcategories. Zhang et al. (2025) proposes a hierarchical model decomposing variance into within-prompt and between-prompt components, and Mizrahi et al. (2024) shows that prompt paraphrasing alone can reverse model rankings. Our work extends this line by further separating systematic judge bias from random noise.\n\n**Budget-constrained evaluation.** Saha et al. (2026) frames judge selection as a multi-armed bandit problem, Luettgau et al. (2025) applies hierarchical Bayesian partial pooling in low-data regimes, and Miller (2024) derives standard errors and power formulas for benchmark scores; Dorner et al. (2025) further establishes fundamental scaling limits on the accuracy gains from additional judge queries.\n\n---\n\n## Section 3: Methodology (verbatim)\n\n### 3.1 Model Specification\n\nConsider evaluating model θ on n scenarios from a dataset D of N total scenarios, with m independent generations per scenario, each scored by K judges drawn from a pool of K_tot. The same K judges score every scenario–generation cell (a crossed design). We model each score as:\n\n**X_ijℓ = μ_θ + α_i + β_ij + γ_ℓ + ε_ijℓ** (Eq. 1)\n\nwhere i ∈ {1, …, n} indexes scenarios, j ∈ {1, …, m} indexes generations within scenario i, and ℓ indexes the K selected judges. Each term has a distinct source:\n\n- **μ_θ**: panel-mean estimand for model θ—the average score the K_tot-judge panel would assign in expectation, with random noise removed.\n- **α_i ~ iid (0, σ_α²)**: scenario effect—how much individual scenario difficulty varies for model θ. A dataset whose scenarios all test the same aspects of model θ equally has σ_α² = 0.\n- **β_ij ~ iid (0, σ_β²)**: generation effect—variability from stochastic decoding. σ_β² is model-specific; a deterministic model has σ_β² = 0.\n- **γ_ℓ**: judge offset relative to the panel mean—a fixed constant for each judge, with centering constraint Σγ_ℓ = 0 and population dispersion σ_γ² = K_tot⁻¹ Σ γ_ℓ². γ_ℓ measures deviation from the panel reference, not from absolute truth: bias shared by all panel members is absorbed into μ_θ.\n- **ε_ijℓ ~ iid (0, σ_ε²)**: residual—captures judge-level noise and all interaction terms.\n\nThe random effects (α, β, ε) are mutually independent with finite second moments; no distributional assumptions (e.g. Gaussianity) are needed. The n scenarios and K judges are each drawn by simple random sampling without replacement, independently of each other and of all random effects.\n\n### 3.2 Variance Decomposition\n\nThe benchmark score is the grand mean X̄ = (1/nmK) Σ X_ijℓ, which decomposes as X̄ = μ_θ + ᾱ + β̄ + γ̄ + ε̄.\n\n**Proposition 1 (Variance decomposition):**\n\nVar(X̄) = [σ_α²/n + σ_β²/nm + σ_ε²/nmK] + [σ_γ²/K · (K_tot − K)/(K_tot − 1)]\n           |___________ random noise ____________|   |________ V_γ: judge bias ________|   (Eq. 2)\n\nEach noise term shrinks with more data at or above its hierarchy level. The bias term V_γ responds only to K and vanishes exactly at K = K_tot. The proof uses the law of total variance, conditioning on the judge selection, combined with a finite population correction for sampling K from K_tot centered bias values (Appendix C).\n\n### 3.3 Allocation Strategies\n\nGiven a per-scenario budget of B judge calls, the design question is how to allocate judges across generations. The scenario term σ_α²/n is fixed once scenarios are chosen; we compare three strategies for the remaining variance.\n\n**Strategy A: All judges per generation.** Use all K_tot judges for each of m = B/K_tot generations. The mean of all judge offsets is zero (γ̄ = 0):\n\nV_A(B) = (K_tot σ_β² + σ_ε²) / nB   (Eq. 3)\n\n**Strategy B: Random single judge per generation.** Use m = B generations, each scored by one randomly sampled judge. Random judge selection injects the panel-relative offset as additional sampling noise:\n\nV_B(B) = (σ_β² + σ_γ² + σ_ε²) / nB   (Eq. 4)\n\n**Strategy C: CyclicJudge (round-robin).** Use m = B generations, assigning judge j mod K_tot to generation j. Each judge appears equally often, so the panel-relative offsets sum to zero (γ̄ = 0):\n\nV_C(B) = (σ_β² + σ_ε²) / nB   (Eq. 5)\n\nWith one generation per scenario (m = 1), the same variance and offset cancellation is achieved by cycling judges across scenarios instead. In this case scenarios should be shuffled before assignment to avoid confounding the cycle with any latent ordering of the dataset.\n\n**Advantage of CyclicJudge.** Direct comparison (Appendix E) shows V_C ≤ min(V_A, V_B) for all B, with gaps of O(1/B), so CyclicJudge's advantage is largest at small budgets of judge calls. The ranking of A vs. B depends on whether (K_tot − 1)σ_β² ≷ σ_γ²: all judges beat random only when judge bias is large relative to generation variance.\n\n---\n\n## Section 4: Experiments (verbatim)\n\n### 4.1 Domain and Data\n\nWe validate our approach on two benchmarks:\n\n**MT-Bench** (Zheng et al., 2023) is a general-purpose multi-turn conversational benchmark with 80 two-turn questions spanning 8 categories, scored on a 1–10 scale per turn (averaged).\n\n**MindEval** (Pombal et al., 2025) is a domain-specific benchmark for multi-turn mental health support with 50 scenarios and composite scores on a 1–5 scale covering empathy, safety, and clinical appropriateness. Each scenario simulates a full 10-turn therapeutic session with a synthetic patient.\n\nFor both benchmarks, we evaluate five models—Qwen 2.5 7B Instruct (Yang et al., 2024), Llama 3.3 70B Instruct (Grattafiori et al., 2024), GPT-5.2, Gemini 3 Flash, and Claude Sonnet 4.6, which also serve as judges in a symmetric design. MT-Bench uses m=10 generations per scenario (4,000 scores per model); MindEval uses m=5 (1,250 scores per model). We follow the default judge decoding hyperparameters from reference (Appendix J).\n\n### 4.2 Judge Bias Estimates\n\nAs a complementary omnibus check on the mixed-effects decomposition (§3.1), we test whether judge identity has a significant effect using a two-way ANOVA, treating each scenario–generation pair as a subject crossed with K judges. On both benchmarks, the judge main effect is highly significant (p &lt; 0.001 in all cases; see Appendix H).\n\nTable 1 demonstrates that single-judge evaluation produces unreliable rankings. On MT-Bench at the default operating point (m=1, K=1), the top-ranked model changes with every judge, with Qwen ranking itself first despite being last by consensus, a pattern consistent with the self-preference bias documented by Wataoka et al. (2024). The per-observation variance estimates (Table 2) confirm this quantitatively: judge variance σ̂_γ² ranges from 0.34 to 0.95 across models. Since competitive models on current leaderboards are routinely separated by &lt; 0.5 points (Chiang et al., 2024), single-judge evaluation can easily reverse rankings. On MindEval, rankings are also notably more stable across single judges: four of five produce an identical ordering. Two plausible factors include: domain-specific rubrics may leave less room for stylistic self-preference, and the markedly lower scenario and generation variance on MindEval (§4.3) compresses the absolute size of any model-dependent fluctuations.\n\n### 4.3 Variance Components\n\nTable 2 reports the per-observation variance component estimates via crossed ANOVA (see Appendix D). On MT-Bench, scenario variance σ̂_α² is the largest per-observation component; maximizing the number of distinct scenarios always reduces total variance (Appendix F). Generation variance σ̂_β² drops with capability, consistent with the observation that stronger models produce more deterministic outputs. As frontier models increasingly rely on RL post-training, generation variance may shrink further (Matsutani et al., 2025). The judge offset variance σ̂_γ² remains substantial for all models, accounting for &gt;94% of benchmark variance at the default operating point (see Appendix B).\n\nOn MindEval, both scenario and generation variance are markedly lower. Scenario variance σ̂_α² drops by one to two orders of magnitude because all MindEval scenarios evaluate the same rubrics across different user profiles, so difficulty varies far less than on MT-Bench. Generation variance is similarly suppressed: each MindEval generation is a full 10-turn therapeutic session, so per-response decoding randomness averages out over many turns. The judge offset variance remains the dominant component throughout, exceeding both scenario and generation variance by an order of magnitude.\n\n### 4.4 Strategy Comparison\n\nFigure 1 validates the three allocation strategies via 5,000 subsampling repetitions at each budget level on both benchmarks. Markers show empirical variance; dashed lines show exact predictions from empirical pool variances (Appendix G). CyclicJudge achieves lower variance everywhere on both benchmarks, and predictions match empirical results precisely. At B=5, switching from random to cycling cuts variance by ~27–40% across models on MT-Bench.\n\nThe optimal strategy among the two alternatives depends on the sign of (K_tot − 1)σ_β² − σ_γ²: all-judges wins when σ_γ²/σ_β² &gt; K_tot − 1 = 4. On MT-Bench, this ratio is below the threshold for Qwen (3.6) and Llama (2.1), so random judging is preferable; for Gemini and Claude (σ̂_β² ≈ 0), all-judges converges to CyclicJudge. On MindEval, the ratio exceeds the threshold for nearly every model, so all-judges consistently outperforms random. The driver is not a larger judge offset variance, but rather a sharply lower generation variance σ̂_β². Meanwhile, judges' disagreement over subjective clinical criteria keeps σ̂_γ² substantial relative to σ̂_β². CyclicJudge outperforms both alternatives regardless of this ratio.\n\n---\n\n## Section 5: Conclusion (verbatim)\n\nWe develop a variance decomposition for LLM-as-judge evaluation that separates systematic between-judge offsets from random noise and use it to derive CyclicJudge, a round-robin judge assignment strategy. Our analysis and experiments on both a general-purpose benchmark (MT-Bench) and a domain-specific clinical benchmark (MindEval) yield three main findings: (1) Systematic judge offsets dominate benchmark score variance at default operating points. (2) Random noise components decrease with model capability and multi-turn evaluation, but the panel-relative offset variance does not. (3) CyclicJudge achieves the lowest variance among all allocation strategies at every budget level, regardless of the model's variance profile, by recovering the panel-mean score exactly while maximizing generation diversity. The method requires no model-specific tuning and maintains the same per-item cost as single-judge evaluation, providing practitioners with a cost-neutral drop-in replacement for more reliable LLM evaluation.\n\n---\n\n## Limitations (verbatim)\n\n**Panel-mean reference.** Our analysis treats the mean score of the K_tot-judge panel as the reference for evaluation. A diverse panel drawn from disjoint model families typically correlates more strongly with human judgments than any single judge (Verga et al., 2024), but the panel mean is not a substitute for absolute ground truth. Biases shared across the panel members are absorbed into μ_θ and propagate into the panel mean. CyclicJudge addresses the within-panel offsets between individual judges, not biases that all panel members share; calibrating the panel itself against human or expert references is complementary work.\n\n**Linear model approximation.** Our variance decomposition assumes a linear random effects model, which treats scores as unbounded and continuous. LLM-as-judge scores are in fact bounded ordinal variables, so the linear model can produce boundary artifacts and heteroscedastic residuals near the scale endpoints. A generalized linear mixed model (GLMM), such as a cumulative-link mixed model, would properly account for the ordinal, bounded nature of the responses. However, GLMMs do not yield the closed-form variance decomposition that our allocation analysis relies on. We therefore retain the linear approximation, noting that it remains reasonable when the scale range is large relative to the observed score dispersion, as in our benchmarks.\n\n**Judge pool size.** Our judge pool of K_tot = 5 limits exploration of larger panels. While the theoretical results generalize to arbitrary K, empirical validation with larger and more diverse judge pools would strengthen the practical recommendations.\n\n**Scenario exchangeability.** The \"maximize scenarios\" recommendation assumes scenarios are interchangeable draws from the dataset; in practice, some scenarios may be more informative than others, and item-selection methods (Maia Polo et al., 2024) could alter the tradeoff.\n\n**Balanced design assumption.** The allocation analysis assumes a balanced design in which every scenario receives the same number of judge calls. Extensions to adaptive or sequential designs remain future work.\n\n**Uniform cost assumption.** Our budget analysis treats all judge calls as equal cost; in practice, judges vary widely in price and latency. A cost-weighted allocation that accounts for per-model pricing and inference speed would be needed for real deployment decisions.\n\n---\n\n## Figure and Table Captions (verbatim)\n\n**Figure 1:** Benchmark score variance Var(X̄) vs. per-scenario budget for three strategies: all judges (A), random single judge (B), and CyclicJudge (C). [Two panels: (a) MT-Bench (1–10 scale, n=80, m_max=10); (b) MindEval (1–5 scale, n=50, m_max=5). Five subplots per panel, one per model: Qwen 2.5 7B, Llama 3.3 70B, GPT-5.2, Gemini 3 Flash, Claude Sonnet 4.6. Markers show empirical variance; dashed lines show exact predictions.]\n\n**Figure 2:** Estimated judge biases γ̂_ℓ = X̄_··ℓ − X̄_··· for each judge–model pair. [Heatmap panels: (a) MT-Bench; (b) MindEval. Rows = judge models, columns = evaluated models.]\n\n**Table 1:** Mean score ± 95% CI at the default operating point (m=1, K=1). Bold: highest score per judge column. Underline: second highest.\n- Panel (a): MT-Bench (1–10 scale, n=80) — 5×5 matrix of judge × model\n- Panel (b): MindEval (1–5 scale, n=50) — 5×5 matrix of judge × model\n\n**Table 2:** Per-observation variance component estimates.\n- Panel (a): MT-Bench (n=80) — rows: σ̂_α², σ̂_β², σ̂_γ², σ̂_ε²; columns: Qwen, Llama, GPT, Gemini, Claude\n- Panel (b): MindEval (n=50)\n\n**Table 3:** Variance component estimates. Per-observation variances and their contribution to Var(X̄) at the default operating point (m=1, K=1).\n- Panel (a): MT-Bench — per-observation variance + contribution to Var(X̄) (×10⁻³)\n- Panel (b): MindEval — same structure\n\n**Table 4:** ANOVA F-statistic for the judge main effect. All p &lt; 0.001.\n- MT-Bench F(4, 3196): Qwen 638.2, Llama 445.8, GPT 601.7, Gemini 659.2, Claude 514.9\n- MindEval F(4, 996): Qwen 1029.5, Llama 1280.1, GPT 200.1, Gemini 458.0, Claude 788.9\n\n**Table 5:** Default judge decoding hyperparameters used by each benchmark's reference implementation.\n- MT-Bench: temperature=0, max_tokens (OpenAI)=2048, max_tokens (Anthropic)=1024\n- MindEval: judge_template_version=v0_1, max_completion_tokens=16,000, reasoning_effort=high\n\n---\n\n## Key Numerical Results\n\n**Table 1a — MT-Bench mean scores (m=1, K=1):**\n\n| Judge\\Model | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| Gemini | 8.02±.16 | 7.91±.16 | 7.96±.17 | 7.87±.18 | 8.02±.15 |\n| GPT | 8.98±.08 | 8.81±.11 | 9.06±.06 | 8.71±.11 | 8.39±.16 |\n| Claude | 8.20±.12 | 8.67±.12 | 7.91±.13 | 6.90±.20 | 6.09±.20 |\n| Llama | 9.88±.06 | 9.71±.11 | 9.62±.12 | 8.58±.25 | 7.16±.27 |\n| Qwen | 8.68±.10 | 8.49±.13 | 8.52±.13 | 7.26±.22 | 5.99±.23 |\n\n**Panel mean (μ̂_θ) MT-Bench:** Qwen 7.13, Llama 7.87, GPT 8.72, Gemini 8.75, Claude 8.61\n\n**Table 1b — MindEval mean scores:**\n\n| Judge\\Model | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| Claude | 3.86±.08 | 4.04±.09 | 3.90±.08 | 3.70±.07 | 3.26±.12 |\n| GPT | 4.67±.07 | 4.51±.07 | 4.49±.06 | 4.29±.05 | 3.38±.21 |\n| Gemini | 4.05±.06 | 3.76±.09 | 3.63±.05 | 3.16±.06 | 2.32±.08 |\n| Llama | 4.72±.06 | 3.95±.16 | 3.91±.12 | 3.00±.10 | 1.69±.08 |\n| Qwen | 4.84±.04 | 3.39±.15 | 3.31±.08 | 2.85±.06 | 1.74±.05 |\n\n**Panel mean (μ̂_θ) MindEval:** Qwen 2.478, Llama 3.400, GPT 3.931, Gemini 3.846, Claude 4.431\n\n**Table 2a — MT-Bench variance components:**\n\n| Component | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| σ̂_α² (scenario) | 1.530 | 0.882 | 0.634 | 0.408 | 0.393 |\n| σ̂_β² (generation) | 0.266 | 0.238 | 0.076 | 0.000 | 0.000 |\n| σ̂_γ² (judge) | 0.947 | 0.503 | 0.339 | 0.435 | 0.427 |\n| σ̂_ε² (residual) | 1.486 | 1.130 | 0.564 | 0.661 | 0.830 |\n\n**Table 2b — MindEval variance components:**\n\n| Component | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| σ̂_α² (scenario) | 0.034 | 0.014 | 0.021 | 0.015 | 0.005 |\n| σ̂_β² (generation) | 0.100 | 0.019 | 0.047 | 0.016 | 0.002 |\n| σ̂_γ² (judge) | 0.523 | 0.280 | 0.132 | 0.150 | 0.155 |\n| σ̂_ε² (residual) | 0.159 | 0.069 | 0.207 | 0.103 | 0.061 |\n\n**Table 3a — MT-Bench contribution to Var(X̄) (×10⁻³) at default operating point:**\n\n| Component | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| σ̂_α²/n | 19.13 | 11.03 | 7.92 | 5.11 | 4.92 |\n| σ̂_β²/nm | 3.33 | 2.97 | 0.94 | 0.00 | 0.00 |\n| σ̂_γ²·FPC/K | 946.50 | 502.50 | 339.00 | 435.40 | 426.60 |\n| σ̂_ε²/nmK | 18.57 | 14.12 | 7.05 | 8.27 | 10.38 |\n\n**Table 3b — MindEval contribution to Var(X̄) (×10⁻³):**\n\n| Component | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| σ̂_α²/n | 0.67 | 0.28 | 0.43 | 0.29 | 0.09 |\n| σ̂_β²/nm | 2.01 | 0.38 | 0.93 | 0.31 | 0.04 |\n| σ̂_γ²·FPC/K | 522.50 | 280.20 | 132.00 | 150.20 | 154.80 |\n| σ̂_ε²/nmK | 3.18 | 1.37 | 4.14 | 2.05 | 1.23 |\n\n---\n\n## Appendix A: Judge Bias Estimates (verbatim)\n\nFigure 2 shows the estimated per-judge bias for each judge–model pair on both benchmarks. A pronounced self-preference is visible along the diagonal: on MindEval, Claude Sonnet 4.6's self-bias of +0.412 is the only positive entry in its otherwise uniformly negative row, and Qwen 2.5 7B's self-bias is the largest in its row on both benchmarks. Judge temperament is not stable across benchmarks: Gemini 3 Flash is the most lenient judge on MT-Bench (all biases positive), yet becomes one of the harshest on MindEval, suggesting that judge personality is benchmark-dependent rather than an intrinsic model property. On MT-Bench, strictness correlates with model capability: the two strongest models by consensus (GPT-5.2 and Claude) are the most uniformly negative judges, while the two weakest (Qwen and Llama) are the most lenient. Finally, the harshest judge–model interactions concentrate on capability-mismatched pairs: GPT-5.2 and Claude penalize Qwen by over one full scale point on MT-Bench, while their biases toward each other are an order of magnitude smaller.\n\n**Judge bias matrix (MT-Bench):**\n\n| Judge\\Model | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| Qwen 2.5 7B | +0.887 | +0.009 | -0.808 | -0.735 | -0.650 |\n| Llama 3.3 70B | +1.257 | +0.848 | +0.091 | +0.224 | +0.446 |\n| GPT-5.2 | -1.040 | -0.962 | -0.044 | -0.550 | -0.707 |\n| Gemini 3 Flash | +0.032 | +0.711 | +0.991 | +1.132 | +1.003 |\n| Claude Sonnet 4.6 | -1.136 | -0.607 | -0.230 | -0.071 | -0.092 |\n\n**Judge bias matrix (MindEval):**\n\n| Judge\\Model | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| Qwen 2.5 7B | +0.780 | +0.298 | +0.104 | +0.053 | -0.566 |\n| Llama 3.3 70B | +0.904 | +0.891 | +0.580 | +0.641 | +0.239 |\n| GPT-5.2 | -0.159 | -0.239 | -0.169 | -0.219 | -0.377 |\n| Gemini 3 Flash | -0.786 | -0.399 | +0.021 | +0.061 | +0.293 |\n| Claude Sonnet 4.6 | -0.739 | -0.551 | -0.536 | -0.536 | +0.412 |\n\n---\n\n## Appendix B: Variance at Default Operating Point\n\nThe judge-offset contribution (σ̂_γ²·FPC/K) accounts for &gt;94% of benchmark variance at the default operating point (m=1, K=1) on MT-Bench. Specifically: for Qwen, 946.50/(946.50+19.13+3.33+18.57) ≈ 96.6%.\n\n---\n\n## Appendix C: Proof of Proposition 1 (Variance Decomposition)\n\nThe proof proceeds in three steps: (1) grand mean decomposition, (2) law of total variance, (3) finite population correction.\n\n**Step 1 — Grand mean decomposition:** Starting from X_ijℓ = μ_θ + α_i + β_ij + γ_ℓ + ε_ijℓ, average hierarchically: first over K judges within generation (i,j) — gives X̄_ij· = μ_θ + α_i + β_ij + γ̄ + ε̄_ij; then over m generations within scenario i — gives X̄_i·· = μ_θ + α_i + β̄_i + γ̄ + ε̄_i·; then over n scenarios — gives X̄ = μ_θ + γ̄ + ᾱ + β̄ + ε̄.\n\n**Step 2 — Law of total variance:** Let S denote the judge selection. Var(X̄) = E[Var(X̄|S)] + Var(E[X̄|S]). Given S, γ̄ is constant → Var(X̄|S) = σ_α²/n + σ_β²/nm + σ_ε²/nmK (does not depend on S). E[X̄|S] = μ_θ + γ̄ → Var(E[X̄|S]) = Var(γ̄).\n\n**Step 3 — Finite population correction (Lemma 2):** For a simple random sample of size k from P elements with centering constraint Σa_i = 0 and σ_a² = P⁻¹ Σa_i²: Var(āS) = (σ_a²/k) · (P−k)/(P−1). Applying to judge biases (a_ℓ = γ_ℓ, P = K_tot, k = K): Var(γ̄) = (σ_γ²/K) · (K_tot − K)/(K_tot − 1).\n\n---\n\n## Appendix D: Estimation of Variance Components\n\nMethod-of-moments estimators using crossed ANOVA:\n- **σ̂_ε² = MSW** (residual mean square)\n- **σ̂_β² = (MSG − MSW)/K** (between-generation mean square, can be negative → truncated to 0)\n- **σ̂_α² = (MSS − MSG)/(mK)** (between-scenario mean square)\n- **σ̂_γ² = (1/K_tot) Σ γ̂_ℓ² − σ̂_ε² · (K_tot−1)/(nm·K_tot)**\n\nwhere γ̂_ℓ = X̄_··ℓ − X̄_···.\n\nZero-truncation note: negative estimates of σ̂_β² (Gemini and Claude on MT-Bench) are set to zero per standard convention—indicates generation-to-generation variability is negligible relative to residual noise.\n\n---\n\n## Appendix E: Allocation Strategy Derivations (Pairwise comparisons)\n\n- V_A − V_C = (K_tot − 1)σ_β² / nB ≥ 0\n- V_B − V_C = σ_γ² / nB ≥ 0\n- V_A − V_B = [(K_tot − 1)σ_β² − σ_γ²] / nB (sign depends on data)\n\n---\n\n## Appendix F: Scenario Coverage\n\nUnder cycling, variance as function of m with total budget B_gen = nm:\n\nV_C(B_gen, m) = m(σ_α² + σ_β² + σ_ε²) / B_gen   (Eq. 35)\n\nThis is linear in m with positive slope σ_α²/B_gen, so variance is minimized at m=1, maximizing the number of distinct scenarios up to dataset size N. Once the scenario pool is exhausted (n=N), excess budget should go to additional generations.\n\n---\n\n## Appendix G: Exact Bootstrap Predictions\n\nFor finite pool of m_max observed generations, exact predictions use empirical pool variances:\n- Strategy A: C_A = K_tot · (1/n) Σ_i [(1/m_max) Σ_g (X̄_ig· − X̄_i··)²]\n- Strategy B: C_B = (1/n) Σ_i [(1/(m_max K_tot)) Σ_{g,ℓ} (X_igℓ − X̄_i··)²]\n- Strategy C: C_C = (1/(nK_tot)) Σ_{i,ℓ} [(1/m_max) Σ_g (X_igℓ − X̄_i·ℓ)²]\n\n---\n\n## Appendix H: ANOVA F-Test for Judge Effects\n\nTwo-way crossed ANOVA, F = MSJ/MSR with K−1 and (N−1)(K−1) degrees of freedom.\n\n| Model | MT-Bench F(4,3196) | MindEval F(4,996) |\n|---|---|---|\n| Qwen 2.5 7B | 638.2 | 1029.5 |\n| Llama 3.3 70B | 445.8 | 1280.1 |\n| GPT-5.2 | 601.7 | 200.1 |\n| Gemini 3 Flash | 659.2 | 458.0 |\n| Claude Sonnet 4.6 | 514.9 | 788.9 |\n\nAll p &lt; 0.001.\n\n---\n\n## Appendix I: Omitted Interactions\n\nThe model retains grand mean and three main effects, absorbing all interaction terms into residual ε_ijℓ:\n\n- **Scenario–generation:** Generations nested within scenarios, confounded with β_ij by construction.\n- **Scenario–judge:** Estimable in principle (n(K_tot−1) additional parameters) but enters only through per-cell residual variance, already captured empirically in §4.\n- **Generation–judge:** Exchangeable across j, acts as additional i.i.d. noise, absorbed into σ_ε².\n\n---\n\n## Appendix J: Judge Hyperparameter Settings\n\n**MT-Bench:** temperature=0, max_tokens (OpenAI)=2048, max_tokens (Anthropic)=1024.\n**MindEval:** judge_template_version=v0_1, max_completion_tokens=16,000, reasoning_effort=high.\n\nFor models outside original API tables (Gemini 3 Flash and Claude Sonnet 4.6 for MT-Bench), closest equivalent setting supported by provider is applied.\n\nEffect of hyperparameters: Decoding hyperparameters control within-judge stochasticity, absorbed into residual ε_ijℓ → contributes to σ_ε². The systematic offset γ_ℓ is a property of the judge model itself, not sampling. Increasing temperature would inflate σ_ε² but, to first order, leave γ_ℓ and σ_γ² unchanged. At the default operating point, judge-offset contribution exceeds residual contribution by roughly two orders of magnitude on both benchmarks. Reasonable perturbations of decoding hyperparameters can only shift σ_ε² within a window much smaller than σ_γ², so the qualitative ranking of allocation strategies is robust to this choice.\n\n---\n\n**Source paper:** [2603.01865] CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation — https://arxiv.org/abs/2603.01865&lt;/result>\n&lt;usage>&lt;total_tokens>40855&lt;/total_tokens>&lt;tool_uses>16&lt;/tool_uses>&lt;duration_ms>316963&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---


### Runtime record

_source line 90 · 2026-05-21T16:43:48.711Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:43:48.711Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "&lt;task-notification>\n&lt;task-id>ad50cdb495cf40e2d&lt;/task-id>\n&lt;tool-use-id>toolu_015rpQr8sYtDbCzWni2DFwZy&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ad50cdb495cf40e2d.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: lin2025psnirt\" completed&lt;/summary>\n&lt;result>I now have all the material needed. Here is the complete extraction:\n\n---\n\n## Paper: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\n\n**Venue:** AAAI 2026 (Oral), Technical Track on NLP VI, Vol. 40, Issue 41, pp. 35085–35093  \n**arXiv:** 2505.15055 (v1: 2025-05-21, v2: 2025-08-01, v3: 2026-01-16)  \n**Authors:** Hongli Zhou*, Hui Huang*, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang†, Wei Bao†, Jian Dong†, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao  \n**Affiliations:** Faculty of Computing, Harbin Institute of Technology; HIT Shenzhen; China Electronics Standardization Institute  \n**Code:** https://github.com/Joe-Hall-Lee/PSN-IRT\n\n---\n\n## 1. Abstract (verbatim)\n\nThe evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities. This paper provides a critical analysis of benchmark effectiveness, examining mainstream prominent LLM benchmarks using results from diverse models. We first propose Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. PSN-IRT can be utilized for accurate and reliable estimations of item characteristics and model abilities. Based on PSN-IRT, we conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. Furthermore, we demonstrate that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.\n\n---\n\n## 2. Introduction (complete)\n\nAs the scale and performance of large language models (LLMs) continue to grow, accurately measuring their capabilities has become increasingly important (Chang et al. 2024; Zhou et al. 2024; Huang et al. 2025). Currently, the performance of LLMs is primarily evaluated through various benchmarks (Wang et al. 2024), which are comprehensive test suites consisting of carefully designed questions to assess model behavior across different tasks. However, in practice, existing benchmarks often exhibit significant limitations, prompting consideration of their effectiveness (McIntosh et al. 2024).\n\nAs illustrated in Figure 1, on one hand, even benchmarks that are designed to measure similar underlying capabilities often produce inconsistent leaderboards, leading to substantial ranking variations for the same model (Perlitz et al. 2024). On the other hand, many benchmarks show weak separability among top models, limiting the ability to understand performance differences and further model refinement. Given these limitations, there is a growing need for a more systematic analysis of LLM benchmarks.\n\nIn this paper, we conduct a comprehensive analysis for various popular LLM benchmark datasets. Our experiment is based on Item Response Theory (IRT) (Lord, Novick, and Birnbaum 1968; Baker and Kim 2004), a psychometric framework widely used in educational assessment to analyze item properties such as difficulty by modeling item response against examinee ability. However, traditional IRT struggles with the complexity and scale of modern datasets, and its assumption of the normal distribution of abilities does not always hold.\n\nTo advance our objective, we propose the Pseudo-Siamese Network for IRT (PSN-IRT), a framework for comprehensive and interpretable analysis of benchmark test sets. PSN-IRT processes model identifiers and item identifiers through independent neural network pathways. These pathways respectively estimate latent model ability and a rich set of item parameters. The estimated properties are then integrated using an IRT-based formulation to predict outcome probabilities. This architectural design ensures both powerful modeling capabilities and strong theoretical interpretability.\n\nTo validate the effectiveness of PSN-IRT, we conduct extensive experiments on evaluation results from 12 LLMs across 11 benchmarks. Our results show that PSN-IRT outperforms previous approaches in both parameter estimation accuracy and reliability. Based on PSN-IRT, we perform in-depth analyses of these benchmarks using key metrics, with main findings as follows:\n\n1. LLM benchmarks fail to achieve simultaneous excellence across multiple measurements.\n2. LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models.\n3. LLM benchmarks exhibit data contamination in numerous items, compromising their reliability.\n\nFurthermore, we find that model rankings derived from high-quality datasets selected by PSN-IRT are more consistent with human preference and offer stronger discriminability among top models.\n\n**Contributions:**\n1. We propose PSN-IRT, a benchmark analysis framework with superior estimation accuracy and reliability.\n2. We use PSN-IRT for an in-depth analysis of mainstream benchmarks and find that current LLM benchmarks present deficiencies in many aspects.\n3. We show that selecting items with PSN-IRT leads to model rankings that better align with human preference.\n\n---\n\n## 3. Related Work (complete)\n\nResearchers have explored various methods to evaluate and analyze the quality of LLM benchmarks. Recent efforts have introduced quantitative metrics that operate at a holistic, dataset level. For example, Benchmark Agreement Testing (BAT) assesses benchmark reliability by comparing the consistency of model rankings across different leaderboards (Perlitz et al. 2024; White et al. 2025). Other novel metrics have also been proposed for more nuanced dataset-level analysis (Li et al. 2024). Delving deeper than macro-level comparisons, another significant line of work focuses on content-based analysis to ground evaluation in concrete capabilities. For instance, ADeLe (Zhou et al. 2025) leverages scalable cognitive rubrics and item demand features to build highly interpretable capability profiles for AI systems.\n\nItem Response Theory (IRT) (Lord, Novick, and Birnbaum 1968; Baker and Kim 2004) offers a psychometric framework for data-driven, item-level analysis. Within natural language processing (NLP), IRT has been primarily utilized to diagnose fundamental item properties such as difficulty and discriminability (Vania et al. 2021; Byrd and Srivastava 2022). More recently, its principles have also been used to inspire methods for improving evaluation efficiency, for instance, through optimized item selection (Maia Polo et al. 2024) or adaptive testing paradigms (Zhuang et al. 2025; Truong et al. 2025). However, due to the complexity and scale of modern datasets and its assumption of normally distributed abilities, the application of IRT on LLM benchmarks is still underexplored (Ye et al. 2025).\n\n---\n\n## 4. Background: IRT (complete)\n\nItem Response Theory (IRT) (Lord, Novick, and Birnbaum 1968) is a psychometric framework widely used in educational and cognitive assessments to model the relationship between benchmark items and examinee abilities. Unlike Classical Test Theory (CTT) (DeVellis 2006), which relies on aggregate test scores, IRT analyzes individual item responses as a function of a latent ability θ, enabling precise measurement of both item and examinee properties.\n\nCentral to IRT is the Item Characteristic Curve (ICC), a mathematical function that describes the probability of a correct response, P(X=1|θ), as a function of ability θ. Typically logistic, the ICC visualizes how item properties influence performance, serving as the foundation for IRT.\n\nThe simplest IRT model, the One-Parameter Logistic (1PL) model, defines the ICC as:\n\nP(X=1|θ) = 1 / (1 + e^{-(θ−b)})\n\nwhere b denotes item difficulty. When θ=b, the probability of a correct response is 0.5. The 1PL assumes all items have equal discriminability, a simplification that may not hold in complex testing scenarios. More advanced IRT models introduce additional parameters to capture diverse item properties. However, traditional IRT often suffers from inaccurate parameter estimation and relies on assumptions like normal ability distributions, which may not align with real-world data (Tsutsumi, Kinoshita, and Ueno 2021).\n\n---\n\n## 5. Method: PSN-IRT (complete)\n\n### Model Architecture\n\nThe PSN-IRT architecture comprises two independent networks: a model network and an item network. The model network processes one-hot encoded LLM identifiers to estimate model-ability θ, while the item network handles one-hot encoded item identifiers to produce the four IRT parameters: discriminability a, difficulty b, guessing-rate c, and feasibility d.\n\nEach network consists of three fully connected layers with ReLU activation functions, enabling efficient and stable parameter estimation. After that, these estimated properties are then processed by a Logistic Calculation Layer. This layer operates using the Four-Parameter Logistic (4PL) model:\n\nP(X=1|θ) = c + (d−c) · 1/(1+e^{−a(θ−b)})   ... (Eq. 2)\n\nParameter roles:\n- difficulty b: determines the ability level where the probability changes most significantly\n- discriminability a: reflects an item's power to differentiate between models of varying abilities\n- guessing-rate c: captures how likely models are to succeed without full understanding\n- feasibility d: represents the maximum probability that even highly proficient models will correctly answer the item\n\nPSN-IRT follows standard IRT assumptions such as unidimensionality and monotonicity, which generally hold for LLM benchmarking (Kipnis et al. 2025; Truong et al. 2025).\n\n### Training\n\nPSN-IRT is trained end-to-end using observed binary response data in the form of (Model, Item, Response, Outcome), where the binary outcome indicates correctness. During training, PSN-IRT processes encoded pairs of LLM and item identifiers through their respective network pathways. These estimated properties are passed to a Logistic Calculation Layer, with training objective:\n\nJ(θ) = −(1/N) Σ [y_i · log(P_i) + (1−y_i) · log(1−P_i)]   ... (Eq. 3)\n\nwhere N is the batch size. All learnable weights within both model and item networks are updated simultaneously, concurrently optimizing estimated properties for both models and benchmark items.\n\n### Applications\n\nUpon completion of training, the two networks can be used for:\n- Model Network: outputs estimate of model-ability θ\n- Item Network: outputs four estimated psychometric parameters a, b, c, d for in-depth diagnosis of individual item characteristics and overall benchmark quality\n\n---\n\n## 6. Benchmark Quality Measurements (complete)\n\nBeyond the 4 IRT parameters (difficulty, discriminability, guessing-rate, feasibility), two additional metrics are used:\n\n**Local Efficiency Headroom (LEH):** Assesses the potential of a test example to evaluate future progress in LLMs. Calculated as the derivative of the item's ICC with respect to the highest observed latent ability. A high LEH score indicates that even the top model remains far from the saturation point of the ICC.\n\n**Fisher information:** Measures the amount of information an item provides about a model's ability level. For 4PL IRT:\n\nI(θ) = a²(P(θ)−c)²(d−P(θ))² / [(d−c)² · P(θ)(1−P(θ))]   ... (Eq. 4)\n\nwhere P(θ) is defined as Eq. 2.\n\n---\n\n## 7. Experiments: Datasets (Table 1)\n\n| Benchmark | Data Size | Domain | Metric | Format |\n|-----------|-----------|--------|--------|--------|\n| ARC-C | 295 | General | EM | Multiple Choice |\n| BBH | 6,511 | General | EM | Mixed |\n| Chinese SimpleQA | 3,000 | Knowledge | LLM-as-a-Judge | QA |\n| GPQA Diamond | 198 | Science | EM | Multiple Choice |\n| GSM8K | 1,319 | Math | EM | QA |\n| HellaSwag | 10,042 | General | EM | Multiple Choice |\n| HumanEval | 164 | Code | Pass@1 | QA |\n| MATH | 5,000 | Math | EM | QA |\n| MBPP | 500 | Code | Pass@1 | QA |\n| MMLU | 14,042 | General | EM | Multiple Choice |\n| TheoremQA | 800 | Science | EM | QA |\n\n**Total: 41,871 items.**\n\n**Model pool:**\n- Strong models (8): 360GPT2-Pro, DeepSeek-V3, Doubao-pro, Gemini-1.5, Hunyuan-Turbo, Moonshot-v1, Qwen-Plus, Yi-Lightning\n- Weak models (4, intentionally included to broaden discriminability): Gemma-2B-it, Mistral-7B-Instruct-v0.1, Qwen2.5-3B-Instruct, Vicuna-7B-v1.3\n\nData split: training (60%), validation (20%), test (20%). For benchmark analysis, the full dataset is used (30 epochs).\n\n**Evaluation via OpenCompass; binary response matrix constructed by aggregating item-level results across all models and benchmarks.**\n\n---\n\n## 8. Baselines\n\n- IRT with MLE (Maximum Likelihood Estimation), 4PL\n- IRT with MCMC (Markov Chain Monte Carlo), 4PL\n- IRT with VI (Variational Inference), 4PL\n- IRT with VIBO, 4PL\n- Deep-IRT (extension of 1PL IRT via deep networks) — Tsutsumi, Kinoshita, and Ueno 2021\n\n---\n\n## 9. Metrics\n\n1. **Prediction accuracy:** accuracy, F1 score, ROC AUC\n2. **Rank stability:** Kendall's τ between model rankings derived from two held-out test subsets\n\n---\n\n## 10. Main Results (Table 2)\n\n| Model | Parameter | Method | ACC | F1 | AUC | Kendall's τ |\n|-------|-----------|--------|-----|----|-----|-------------|\n| IRT | 4PL | MLE | 0.7211 | 0.8034 | 0.7012 | 0.9697 |\n| IRT | 4PL | MCMC | 0.7070 | 0.7811 | 0.7278 | 0.9697 |\n| IRT | 4PL | VI | 0.7201 | 0.8015 | 0.6940 | 0.9091 |\n| IRT | 4PL | VIBO | 0.7188 | 0.8007 | 0.7055 | 0.9697 |\n| Deep-IRT | 1PL | Deep Learning | 0.7974 | 0.8516 | 0.8519 | 0.9697 |\n| PSN-IRT | 4PL | Deep Learning | **0.7998** | **0.8538** | 0.8485 | **1.0000** |\n\nPSN-IRT attains prediction accuracy on par with Deep-IRT and surpasses it in rank reliability (1.0000 vs 0.9697).\n\n---\n\n## 11. Ablation Study (Table 3)\n\n| Method | ACC | F1 | AUC | Kendall's τ |\n|--------|-----|----|-----|-------------|\n| PSN-IRT (baseline) | 0.7998 | 0.8538 | 0.8485 | 1.0000 |\n| + Embedding (Instructor-XL) | 0.7808 | 0.8413 | 0.8310 | 0.9394 |\n| + GNN | 0.7928 | 0.8490 | 0.8197 | 0.7273 |\n\nBoth alternatives underperform. Semantic similarity between item texts does not necessarily reflect similarity in measurement characteristics. GNN's neighborhood aggregation risks diluting unique statistical signals.\n\n**Parameter stability (Table 4) — Pearson correlation vs. full dataset, all p &lt; 0.0001:**\n\n| Data % | Difficulty | Discrim. | Guessing | Feasibility |\n|--------|-----------|----------|----------|-------------|\n| 30% | 0.9009 | 0.8186 | 0.8274 | 0.9025 |\n| 50% | 0.7437 | 0.7835 | 0.8776 | 0.9330 |\n| 70% | 0.9519 | 0.7414 | 0.8320 | 0.9442 |\n\nHigh correlation across all parameters regardless of data subset.\n\n---\n\n## 12. Table 7: Full Parameter Count Comparison (1PL–4PL)\n\n| Method | Param | ACC | F1 | AUC | Kendall's τ |\n|--------|-------|-----|----|-----|-------------|\n| IRT MLE | 1PL | 0.7219 | 0.8035 | 0.6970 | 1.0000 |\n| IRT MLE | 2PL | 0.7172 | 0.7998 | 0.6963 | 0.9091 |\n| IRT MLE | 3PL | 0.7218 | 0.8031 | 0.7057 | 0.9697 |\n| IRT MLE | 4PL | 0.7211 | 0.8034 | 0.7012 | 0.9697 |\n| IRT MCMC | 1PL | 0.7168 | 0.8011 | 0.7268 | 0.9697 |\n| IRT MCMC | 2PL | 0.7232 | 0.8130 | 0.7301 | 0.9697 |\n| IRT MCMC | 3PL | 0.7172 | 0.8081 | 0.7297 | 1.0000 |\n| IRT MCMC | 4PL | 0.7070 | 0.7811 | 0.7278 | 0.9697 |\n| IRT VI | 1PL | 0.7209 | 0.8024 | 0.6822 | 0.9697 |\n| IRT VI | 2PL | 0.7198 | 0.8012 | 0.6938 | 1.0000 |\n| IRT VI | 3PL | 0.7189 | 0.8011 | 0.6956 | 0.9697 |\n| IRT VI | 4PL | 0.7201 | 0.8015 | 0.6940 | 0.9091 |\n| IRT VIBO | 1PL | 0.7007 | 0.7801 | 0.6901 | 0.9697 |\n| IRT VIBO | 2PL | 0.7301 | 0.8048 | 0.6987 | 0.8788 |\n| IRT VIBO | 3PL | 0.7172 | 0.7993 | 0.7048 | 0.9091 |\n| IRT VIBO | 4PL | 0.7188 | 0.8007 | 0.7055 | 0.9697 |\n| Deep-IRT | 1PL | 0.7974 | 0.8516 | 0.8519 | 0.9697 |\n| PSN-IRT | 1PL | 0.7948 | 0.8497 | 0.8473 | 0.9091 |\n| PSN-IRT | 2PL | 0.7560 | 0.8266 | 0.8259 | 0.9697 |\n| PSN-IRT | 3PL | 0.7965 | 0.8510 | 0.8510 | 0.8788 |\n| PSN-IRT | 4PL | 0.7998 | 0.8538 | 0.8485 | 1.0000 |\n\nTraditional IRT shows no consistent pattern with increasing parameter complexity; PSN-IRT 4PL is best.\n\n---\n\n## 13. Benchmark Analysis Findings\n\n### Table 5: Ranks of datasets (lower = better)\n\n| Dataset | Difficulty | Discriminability | Guessing | Feasibility | LEH | Fisher | Total |\n|---------|-----------|-----------------|----------|-------------|-----|--------|-------|\n| Chinese SimpleQA | 2 | 3 | 1 | 9 | 3 | 5 | 23 |\n| TheoremQA | 1 | 10 | 3 | 11 | 2 | 2 | 29 |\n| MBPP | 5 | 6 | 4 | 8 | 4 | 4 | 31 |\n| MATH | 4 | 1 | 2 | 7 | 7 | 10 | 31 |\n| GPQA Diamond | 3 | 11 | 6 | 10 | 1 | 1 | 32 |\n| BBH | 6 | 5 | 8 | 6 | 6 | 7 | 38 |\n| MMLU | 9 | 9 | 9 | 5 | 5 | 3 | 40 |\n| GSM8K | 8 | 2 | 5 | 3 | 11 | 11 | 40 |\n| HumanEval | 7 | 4 | 7 | 4 | 9 | 9 | 40 |\n| HellaSwag | 10 | 7 | 10 | 2 | 8 | 6 | 43 |\n| ARC-C | 11 | 8 | 11 | 1 | 10 | 8 | 49 |\n\n### Table 8: Average item-level properties\n\n| Dataset | Difficulty | Discriminability | Guessing | Feasibility | LEH | Fisher |\n|---------|-----------|-----------------|----------|-------------|-----|--------|\n| ARC-C | -1.1637 | 1.2822 | 0.2621 | 0.9481 | 0.0041 | 0.0005 |\n| BBH | -0.6033 | 1.3845 | 0.1657 | 0.8747 | 0.0057 | 0.0006 |\n| Chinese SimpleQA | 0.2656 | 1.4474 | 0.0609 | 0.7088 | 0.0089 | 0.0006 |\n| GPQA Diamond | 0.1902 | 0.8598 | 0.1518 | 0.6437 | 0.0142 | 0.0014 |\n| GSM8K | -0.7899 | 1.5255 | 0.1491 | 0.9167 | 0.0038 | 0.0004 |\n| HellaSwag | -1.0353 | 1.2920 | 0.2449 | 0.9304 | 0.0047 | 0.0006 |\n| HumanEval | -0.6351 | 1.4459 | 0.1565 | 0.8957 | 0.0046 | 0.0005 |\n| MATH | -0.2396 | 1.5793 | 0.0673 | 0.8290 | 0.0054 | 0.0004 |\n| MBPP | -0.3456 | 1.3625 | 0.1345 | 0.8221 | 0.0071 | 0.0007 |\n| MMLU | -0.8383 | 1.1968 | 0.2381 | 0.8921 | 0.0067 | 0.0008 |\n| TheoremQA | 0.6548 | 1.0656 | 0.0888 | 0.5012 | 0.0145 | 0.0013 |\n\n### Finding 1 (verbatim from paper)\n\n\"LLM benchmarks fail to achieve simultaneous excellence across multiple measurement properties. As shown in Table 5, the results clearly demonstrate this lack of simultaneous excellence. While Chinese SimpleQA achieves the best overall score, no benchmark performs universally well across the individual metrics. For instance, Chinese SimpleQA itself suffers from poor feasibility with a rank of 9. This pattern of strengths being offset by significant weaknesses is common across benchmarks, which underscores the inherent challenges and trade-offs in benchmark design. Moreover, the property distributions visualized in Figure 3 further highlight this variability and the difficulty for any single benchmark to achieve balanced, high quality across all desired measurement properties.\"\n\n### Finding 2 (verbatim)\n\n\"Current LLM benchmarks exhibit an insufficient difficulty ceiling to challenge the most advanced models. As shown in Table 5, difficulty is varied among different benchmarks. Datasets such as TheoremQA, Chinese SimpleQA, and GPQA Diamond lead in difficulty and continue to challenge many LLMs. In contrast, other benchmarks including ARC-C, HellaSwag, and MMLU have become comparatively easy, where many of the items are readily solved by high-performing models, diminishing their utility for differentiating top-tier systems. Crucially, as shown in Figure 3, even the most challenging items in existing benchmarks exhibit relatively low difficulty levels. For instance, on the IRT scale, the highest item difficulty values rarely exceed 1.0, while top models such as DeepSeek-V3 have estimated abilities well above 3.0. This indicates that even the hardest questions are significantly below the capability level of elite LLMs, highlighting a lack of sufficient challenge for frontier capabilities.\"\n\n### Finding 3 (verbatim)\n\n\"Generally low LEH scores across most benchmarks reveal widespread item saturation. While Table 5 indicates that datasets like GPQA Diamond and TheoremQA achieve the highest relative ranks for average LEH, suggesting they offer more headroom than other benchmarks, the absolute LEH values in Figure 3 are often smaller than ideal. Conversely, benchmarks such as GSM8K and ARC-C exhibit lower average LEH scores. This signifies that current high-performing models are already approaching or have reached the performance ceiling for a substantial portion of items within these test sets. This necessitates the development of new benchmark items and datasets explicitly designed with greater headroom as models continue to evolve.\"\n\n### Finding 4 (verbatim)\n\n\"Outlier-high guessing-rates in many benchmark items flag risks of data contamination. The guessing-rate reflects the chance that a model can answer a question correctly without actual understanding, typically by exploiting format-based cues or shortcuts. As shown in Figure 3, datasets like ARC-C, HellaSwag, and MMLU generally present higher guessing-rates, possibly due to their multiple-choice formats. Notably, further inspection of the item guessing-rate parameter distributions, as depicted in Figure 3, reveals that a considerable number of items across several benchmarks exhibit unusually high guessing-rates. This observation regards the potential for such items to indicate data contamination, namely the content or answers for these items might have been present in the models' pre-training data (Zhuang et al. 2025).\"\n\n### Finding 5 (verbatim)\n\n\"Widespread low-feasibility items in scientific benchmarks reveal flawed question design. Feasibility estimates how well a question can be answered based on the information provided. Low feasibility often arises from underspecified or overly broad questions, where even a strong model cannot determine a clear answer. As shown in Figure 3, datasets like TheoremQA and GPQA Diamond exhibit lower feasibility, likely due to complex scientific contexts or vague problem descriptions. In contrast, ARC-C and HellaSwag have high feasibility, suggesting their questions are well-formed and specific. Low feasibility more often reflects weaknesses in annotation quality or task design, and such items can distort evaluation by penalizing models for failing to resolve ambiguities (Rodriguez et al. 2021).\"\n\n---\n\n## 14. Difficulty–Discriminability Relationship (Figure 4 context)\n\n\"Item discriminability tends to be lower when item difficulty reaches extreme levels — that is, when items are either very easy or very hard. Consequently, datasets that feature a more balanced distribution of difficulty often exhibit higher overall discriminability, enabling them to more effectively distinguish between models of varying capabilities. Benchmarks such as MATH and GSM8K, which contain a range of difficulties, achieve high average discriminability. Conversely, datasets like GPQA Diamond and TheoremQA, which are characterized by a concentration of very difficult items, exhibit the lowest average discriminability.\"\n\n---\n\n## 15. Efficient Benchmarking Section (complete)\n\n### Experimental Setup\n\n\"To evaluate the effectiveness of different item selection strategies, we design an experiment to evaluate the effectiveness of different item selection strategies. Our methodology involves Benchmark Agreement Testing (BAT) (Perlitz et al. 2024). We first establish a reference model ranking by aggregating results from two public leaderboards: Chatbot Arena (Chiang et al. 2024) and OpenCompass Arena (Contributors 2023). Subsequently, various subsets of benchmark items are chosen based on different criteria. Model rankings generated using these subsets are then compared against the reference arena ranking using Kendall's τ to measure agreement. Alongside agreement, we also consider the variance of model scores on these subsets; higher variance generally indicates the subset's capacity to differentiate more clearly between models. The evaluations are conducted using two distinct model groupings: one set comprising a mix of stronger and weaker models ('w/ weak models'), and another set from which weaker models are excluded ('w/o weak models'), to specifically assess separability among stronger contenders.\"\n\n### Table 6: Variance and Kendall's τ for data selection strategies\n\n| Strategy | w/ weak — Variance | w/ weak — Kendall | w/o weak — Variance | w/o weak — Kendall |\n|----------|--------------------|-------------------|----------------------|--------------------|\n| All | 0.0434 | 0.6444 | 0.0010 | 0.2381 |\n| Top 400 — Random | 0.0421 | 0.6444 | 0.0007 | 0.2381 |\n| Top 400 — Clustering | 0.0308 | 0.6000 | 0.0058 | 0.1429 |\n| Top 400 — Discrim. | 0.1841 | 0.5556 | 0.0000 | 0.2381 |\n| Top 400 — Fisher | 0.0049 | 0.6889 | 0.0033 | 0.7143 |\n| Top 1000 — Random | 0.0406 | 0.6444 | 0.0009 | 0.2381 |\n| Top 1000 — Clustering | 0.0166 | 0.6444 | 0.0041 | 0.2381 |\n| Top 1000 — Discrim. | 0.1805 | 0.6000 | 0.0000 | 0.3813 |\n| Top 1000 — Fisher | 0.0039 | 0.6889 | 0.0030 | **0.9048** |\n\n### Results\n\n\"Selecting items based on Fisher information consistently produces model rankings with superior alignment to the reference arena ranking. For instance, a carefully selected subset composed of just 1,000 items chosen via the Fisher information criterion achieves a Kendall's τ of up to 0.9048. This level of agreement markedly surpasses that achieved by rankings derived from using all available items or from similarly sized randomly selected subsets.\n\nIn contrast, other item selection approaches are less effective for distinguishing strong models. For instance, selecting items based on discriminability yields zero score variance when weak models are excluded, indicating it merely separates broad capability tiers rather than providing granularity among top-performers. Separately, clustering items based on their success/failure vectors (Pacchiardi, Cheke, and Hernández-Orallo 2024) also fails to improve ranking correlation, even when it increases score separability.\"\n\n---\n\n## 16. Implementation Details\n\n- Split: training 60%, validation 20%, test 20% (for estimation accuracy evaluation)\n- For benchmark analysis: trained on entire unified dataset for fixed 30 epochs\n- Optimizer: Adam, lr=0.003, weight decay=0.0001, batch size=512\n- Early stopping: patience=5 epochs, monitored on validation F1 (for estimation evaluation only)\n- Hardware: single NVIDIA A800-80G GPU\n\n---\n\n## 17. Figure Captions (all)\n\n**Figure 1:** Illustration of weak separability and ranking inconsistencies in LLM benchmarks (source: opencompass.org.cn)\n\n**Figure 2:** The illustration of our proposed PSN-IRT. Separate neural networks estimate model-ability (θ) and item parameters (a, b, c, d), which are then combined via the IRT formula to predict the probability of a correct response. After that, the networks can be leveraged for estimating properties for models or items, respectively.\n\n**Figure 3:** Distribution of item-level properties across 11 LLM benchmarks. [Six subplots: Difficulty, Discriminability, Guessing Rate, Feasibility, LEH, Fisher Information — each showing box/violin plots per dataset]\n\n**Figure 4:** Scatter plots showing the relationship between item difficulty and discriminability across 11 benchmarks. Each plot highlights how difficulty affects discriminability within a dataset.\n\n**Figure 5:** Examples of benchmark items exhibiting high and low estimated values for key psychometric parameters, as determined by PSN-IRT. Each pair shows an item with a high parameter value alongside one with a low value for the specified characteristic.\n\n---\n\n## 18. Table Captions (all)\n\n**Table 1:** Benchmarks used in this paper.\n\n**Table 2:** Comparison of prediction accuracy and rank reliability across different methods.\n\n**Table 3:** Ablation study on PSN-IRT's input representation and network architecture.\n\n**Table 4:** Pearson correlation coefficients of item parameters estimated on random subsets of the data versus those estimated on the full dataset. All correlations are statistically significant (p &lt; 0.0001).\n\n**Table 5:** Ranks of datasets based on average item-level properties estimated by PSN-IRT. Each rank is obtained by averaging the property over all items in a dataset and then sorting these averages; smaller rank values correspond to better performance.\n\n**Table 6:** Variance and Kendall's τ for various data selection strategies with and without weak models.\n\n**Table 7:** Comparison of prediction accuracy and rank reliability across different methods using 1PL-4PL parameters.\n\n**Table 8:** Average item-level properties across datasets. Each value represents the mean of the corresponding metric over all benchmark items.\n\n---\n\n## 19. Conclusion (verbatim)\n\n\"In this work, we introduce PSN-IRT, a framework that combines psychometrics with neural networks to provide comprehensive and reliable analyses of LLM benchmarks. Through extensive experiments on 12 LLMs across 11 diverse datasets, we demonstrate that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination. Moreover, we show that strategically selecting smaller, high-quality item sets using PSN-IRT enhances alignment with human preference and separability among top models.\"\n\n---\n\n## 20. Limitations\n\nNo explicit limitations section exists in either the AAAI or arXiv version. Limitations are embedded within findings:\n- PSN-IRT estimates parameters specific to training data, requiring retraining to analyze new items (acknowledged in ablation)\n- The paper does not claim to address all benchmark design issues, only to diagnose them\n\n---\n\n## Key Identifiers for YAML\n\n- **paper_key:** zhou2026lost\n- **venue:** AAAI 2026\n- **full_text_available:** true (PDF retrieved from AAAI proceedings)\n- **method_family:** IRT + neural network (pseudo-siamese)\n- **core_claim:** PSN-IRT uses dual MLP networks to estimate 4PL IRT parameters for LLM benchmark items, enabling principled diagnosis of benchmark quality deficiencies (saturation, contamination, insufficient difficulty ceiling) and construction of smaller, human-preference-aligned evaluation sets via Fisher information-based item selection\n- **key_results:** PSN-IRT ACC=0.7998, F1=0.8538, Kendall τ=1.000 (vs Deep-IRT τ=0.9697); Fisher-selected 1000-item subset achieves τ=0.9048 with human preference rankings vs τ=0.2381 for all 41,871 items (w/o weak models)\n- **datasets:** 11 LLM benchmarks, 41,871 items total, 12 models\n- **baselines:** IRT-MLE, IRT-MCMC, IRT-VI, IRT-VIBO (all 4PL), Deep-IRT (1PL)\n- **metrics:** Accuracy, F1, ROC AUC, Kendall's τ (rank stability), Kendall's τ (BAT agreement with human preference)\n- **ablation_dimensions:** input representation (one-hot vs embedding), backbone (MLP vs GNN), IRT parameter count (1PL–4PL), data subset size (30%/50%/70%)\n- **training_recipe:** Adam lr=0.003, weight_decay=0.0001, batch=512, early_stop patience=5 on val-F1, NVIDIA A800-80G\n- **relation_to_us:** complementary (analyzes benchmark quality via IRT; our work studies judge bias in MFRM framework, which is a different psychometric formulation)&lt;/result>\n&lt;usage>&lt;total_tokens>48617&lt;/total_tokens>&lt;tool_uses>15&lt;/tool_uses>&lt;duration_ms>346873&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---


### Runtime record

_source line 91_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "ce89e433-0020-48b1-9699-611aa888374d",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 92_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 93 · 2026-05-21T16:43:55.964Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:43:55.964Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "&lt;task-notification>\n&lt;task-id>ad6c7c3b8b3db9ea2&lt;/task-id>\n&lt;tool-use-id>toolu_01FPAC744tBXYtaLwHwZcLAq&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ad6c7c3b8b3db9ea2.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: constat2024\" completed&lt;/summary>\n&lt;result>I now have comprehensive information from the paper. Let me compile the complete extracted content.\n\n---\n\n## ConStat: Statistical Detection and Quantification of Benchmark Contamination — Full Extraction\n\n**Paper:** \"ConStat: Performance-Based Contamination Detection in Large Language Models\"\n**Authors:** Jasper Dekoninck, Mark Niklas Müller, Martin Vechev (ETH Zurich, SRI Lab)\n**Venue:** NeurIPS 2024 (Poster, Friday session)\n**arXiv:** 2405.16281 (submitted May 25, 2024)\n**Resources:** constat.ai | github.com/eth-sri/ConStat\n\n---\n\n### 1. Introduction (Full Text)\n\n**Hook (first sentences):**\n\"As large language models (LLMs) become increasingly effective at a wide range of tasks, many companies and research institutions compete to develop better models. To facilitate this development, a variety of benchmarks have been proposed that allow a standardized in-depth comparison of model performance across diverse tasks.\"\n\n**Narrative arc:** Benchmarks critical → data contamination inflates metrics → traditional detection methods fail and are easily evaded → new performance-based definition needed → ConStat statistical solution.\n\n**Tension construction:** Traditional methods \"depend on perplexity-based metrics\" that are \"easily circumvented by training on rephrased samples\" and \"cannot quantify contamination's effect on model performance\" while making \"strict assumptions about the contamination process, making them easy to evade.\"\n\n**Paragraph structure (6 paragraphs):**\n1. LLM benchmarks as competition infrastructure\n2. Data contamination problem setup\n3. Limitations of existing detection approaches\n4. Introduction of performance-based framing + ConStat overview\n5. Evaluation scope description\n6. Four contribution bullets\n\n**Exact contribution bullets:**\n- \"We propose a new performance-based definition of benchmark contamination (Section 2).\"\n- \"We introduce ConStat, a statistical test that detects and quantifies contamination in language models (Section 3).\"\n- \"We empirically demonstrate ConStat's effectiveness in an extensive evaluation across various contamination scenarios (Section 4.2).\"\n- \"We leverage ConStat to study a range of popular models and find contamination for Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models (Sections 4.3–4.5).\"\n\n---\n\n### 2. Section 2 — Defining Contamination\n\n**Core redefinition:** Contamination is \"artificially inflated, non-generalizing benchmark performance\" rather than information-flow (presence of samples in training data).\n\n**Formal Definition 1 (δ-contamination):**\n\"A model M∈ℳ is δ-contaminated on a benchmark D with respect to a reference benchmark D_ref if S_D(M) − H_{D_ref}(S_{D_ref}(M)) &gt; δ\"\n\n**Three contamination types (Section 2.2):**\n- **Syntax-specific:** \"model fails to generalize to semantically equivalent samples\" (worst type — requires rote memorization)\n- **Sample-specific:** \"model fails to generalize to new samples from the benchmark distribution\"\n- **Benchmark-specific:** \"model fails to generalize to different benchmarks that aim to measure performance on the same task\" (least severe — may reflect legitimate overspecialization)\n\n---\n\n### 3. Method (ConStat) — Complete Details\n\n**Workflow (Figure 1, 4 steps):**\n1. Select target model to check\n2. Select reference models and reference benchmarks\n3. Fit hardness correction function + compute test statistic\n4. Extract results (δ̂ and p-value)\n\n**Hardness correction function H_{D_ref}:**\nMaps reference benchmark percentile to expected primary benchmark performance:\n`H_{D_ref} = F_D^{-1} ∘ F_{D_ref}`\nwhere F represents empirical CDFs over reference model performances.\n\nImplemented via smoothing spline minimizing:\n`Σ(S_D(M_ik) − Ĥ_{D_ref}(S_{D_ref}(M_jk)))² + λ∫Ĥ''(x)²dx`\nwith generalized cross-validation for λ selection.\n\n**Contamination estimate:**\n`δ̂ = S_D(M) − Ĥ_{D_ref}(S_{D_ref}(M))`\n\n**Bootstrapping:** Pivotal intervals computed by bootstrapping over both reference models (to account for reference selection uncertainty) and benchmark samples (to account for scoring uncertainty). Confidence bounds:\n`δ̂_{1-p} = 2δ̂ − δ̂'_{1-p}` where δ̂'_q is the q-quantile of bootstrap estimates.\n\n**P-value:** Computed by inverting confidence bounds — the lowest significance level p at which the null hypothesis (δ=0) is rejected.\n\n**Multiple testing correction:** Benjamini-Hochberg false discovery rate control at 5% threshold, applied per benchmark and contamination type.\n\n**Reference benchmark types by contamination type:**\n- Rephrased samples → detect syntax-specific contamination\n- GPT-4-Turbo synthetic samples (~1000/benchmark) → detect sample-specific\n- Alternative benchmarks (MathQA for GSM8k, SCIQ for ARC, Lambada-OpenAI for Hellaswag) → detect benchmark-specific\n\n---\n\n### 4. Experiments — Complete Details\n\n**Section 4.1 — Experimental Setup:**\n- **Primary benchmarks:** GSM8k, ARC-Challenge, MMLU, Hellaswag (4 most popular LLM benchmarks)\n- **Sample limit:** 2000 samples per benchmark (computational constraint)\n- **Evaluation:** LM Evaluation Harness, 5-shot setting\n- **Reference models (20 total):** Meta Llama-2-Instruct-7b, Llama-2-70b, Llama-3 variants; Microsoft Phi-2, Phi-3; Google Gemma-1.1; several Mistral variants; Falcon-7b; OLMo + random-guessing baseline\n- **Synthetic data:** GPT-4-Turbo for rephrasing + generation, ~1000 synthetic samples per benchmark\n\n**Section 4.2 — Controlled Study:**\n- 70 models finetuned total; 9 excluded (training loss spikes) → 61 analyzed\n- 46 trained on actual benchmark (exhibit syntax- + sample-specific contamination)\n- 15 trained on rephrased benchmark data (sample-specific only)\n- Base models: Llama-2-Instruct-7b and Phi-2\n- Varied: epochs, learning rate, portion of contaminated samples, few-shot usage\n- Split: half benchmark for contamination training, other half for measurement\n\n**Section 4.2 — Detection Results (Table 1):**\n\n| Method | Syntax Detection | Sample Detection | Notes |\n|---|---|---|---|\n| Carlini et al. | 76.1% | 65.6% | requires oracle uncontaminated samples |\n| Mireshghallah et al. | 76.1% | 68.9% | requires oracle |\n| Yeom et al. | 78.3% | 67.2% | requires oracle |\n| Shi et al. (oracle) | 84.8% | 70.5% | requires oracle |\n| Shi et al. (realistic) | 21.7% | 16.4% | only applicable realistic baseline |\n| **ConStat** | **89.1%** | **98.4%** | no prior knowledge required |\n\n**Section 4.2 — Quantification (Figure 2):** r² = 0.94 across all finetuned models for estimated vs. true δ. 3 outliers show ceiling effects.\n\n**Section 4.3 — Reputable Reference Models (leave-one-out):**\n- Llama-3-70b: sample-specific on ARC, δ̂=6.6%, p=0.03%\n- Mistral-7b-v0.1: sample-specific on GSM8k, δ̂=8.245%, p=0.150%\n- Mistral-7b-v0.1: sample-specific on Hellaswag, δ̂=3.1%, p=0.24%\n- Phi-2: benchmark-specific on GSM8k, δ̂=36.4%, p&lt;0.01%\n- Phi-3-Mini: benchmark-specific on GSM8k, δ̂=16.3%, p=0.29%\n- No syntax-specific contamination detected among reference models\n\n**Section 4.4 — Popular Model Families:**\n- Qwen-1.5 4b: sample-specific on GSM8k, δ̂=5.4%, p&lt;10⁻⁴\n- Yi-34b: sample-specific on ARC, δ̂≈6%, p&lt;0.2%; sample-specific on Hellaswag, δ̂≈6%, p&lt;0.2%; syntax-specific on Hellaswag, p=5%; sample-specific on GSM8k, δ̂=4%, p=6% (not corrected-significant)\n\n**Section 4.5 — Top-3 Open LLM Leaderboard Models (as of May 4, 2024):**\n- BarraHome/Mistroll-7b-v2.2\n- yam-peleg/Experiment26-7b\n- MTSAIR/multi_verse_model\n\nAll three exhibit: significant benchmark-specific contamination (δ̂&gt;10%) + sample-specific contamination on GSM8k (δ̂≈9%). Paper notes contamination may be caused by \"model selection bias\" from leaderboard's thousands of models.\n\n---\n\n### 5. All Figure and Table Captions (Verbatim)\n\n**Figure 1:** \"Overview of our method. We first select models to check for contamination, then select reference models and benchmarks, and finally compute ConStat to detect and quantify contamination.\"\n- Visual: 4-panel workflow. Panel 1: M₁ (72.1%) and M₂ on benchmark D. Panel 2: reference model selection + 3 reference benchmark types. Panel 3: blue hardness correction curve H_{D_ref}. Panel 4: results showing M₁ δ₁=35.1±3.1% (p=0.01%) vs. M₂ δ₂=4.1±5.1% (p=30%).\n- Figure type: method overview\n\n**Figure 2:** \"Estimated δ̂ as a function of the true δ for the finetuned models. 2-sigma intervals are shown.\"\n- Visual: scatter plot, near-linear relationship, r²=0.94, 3 outliers at ceiling\n\n**Table 1:** \"Percentage of syntax- and sample-specific contaminated models detected by several methods.\"\n\n**Table 2:** \"Contamination results for the reference models on syntax-specific, sample-specific, and benchmark-specific contamination. We only report tests for which the multiple testing corrected p-value is lower than 5% and include the non-corrected p-value, the estimated effect δ̂, the 95% lower bound of the effect δ̂₀.₉₅ and the model performance on the benchmark.\"\n\n**Total figures in main paper:** 2\n**Total tables in main paper:** 2\n**Appendix tables:** Table 17 (Appendix E) with all test results; Table A.2 with GSM8k detailed p-values; additional tables in Appendix A for InternLM-2 and StableLM-2\n\n---\n\n### 6. Related Work — All Citations with Context\n\n**Training data analysis methods** (require training data access — white-box):\nAbdin et al., Brown et al., Chowdhery et al. (×2), Deng et al., Dodge et al., Groeneveld et al., Javaheripi et al., Li — all \"focus on analyzing the training data directly to identify overlaps with the benchmarks.\" ConStat operates black-box without training data.\n\n**Model query-based methods** (black-box):\n- Carlini et al. [12]: perplexity-based membership inference\n- Golchin &amp; Surdeanu [23,24]: model query methods\n- Oren et al. [30]: requires metadata/ordering leakage\n- Mattern et al. [33]: perplexity-based\n- Dekoninck et al. [17]: show perplexity methods easily evaded by rephrasing\n- Shi et al. [36,40]: perplexity-based; Shi et al. [39] is only realistic baseline (21.7% vs ConStat 89.1% on syntax)\n- Yeom et al. [48]: membership inference\n\n**Benchmark-comparison approach:**\n- Zhu et al. [56]: \"measure model performance on rephrased benchmarks\" but \"lack a statistical framework\" and results \"vary significantly across benchmarks\" and \"can be evaded by training on rephrased samples\"\n\n**Alternative benchmarks:**\n- GSM1k [54] (Cobbe et al.): GSM8k replica but \"lacks a statistical test\"\n- SWE-bench [29] (Jimenez et al.): coding benchmark enabling \"visual interpretation\" of HumanEval contamination but lacks formal statistical test\n\n---\n\n### 7. Limitations and Discussion\n\n**Section 6 — Limitations (exact quotes):**\n\"Our method estimates the effect of contamination on performance relative to a set of reference models. Therefore, if these reference models are also contaminated, our method only measures the effect relative to this base level of contamination.\"\n\nSynthetic data limitation 1: \"our work uses an LLM to generate synthetic samples, introducing potential distributional biases into the synthetic benchmark... synthetic benchmark may contain more mislabeled samples.\"\n\nSynthetic data limitation 2: \"synthetic samples generated by a model are likely easier for that model itself to solve. Therefore, contamination results for the model used to generate the samples would be unreliable for sample-specific contamination detection.\"\n\nMitigation: Leave-one-out testing screens suspicious reference models; authors note \"accurate relative performance measurements are sufficient for both model selection and to assess methodological improvements.\"\n\n**Section 6 — Broader Impact (exact quote):**\n\"Model evaluation is a crucial part of LLM development... ConStat provides a statistical framework to estimate the impact of contamination on model performance. This enables more accurate evaluations and allows for the removal of suspicious models from leaderboards, ensuring a fairer evaluation of model capabilities. Furthermore, it is important to note that ConStat can be applied to any model, not just LLMs.\"\n\n---\n\n### 8. Conclusion (Verbatim)\n\n\"We present ConStat, a statistical framework designed to detect contamination and estimate its effect on model performance. Unlike existing methods, ConStat is based on a novel, performance-based definition of contamination and compares performance with various reference benchmarks to obtain a detailed contamination analysis that distinguishes between syntax-, sample-, and benchmark-specific contamination. We investigate ConStat's effectiveness in an extensive control study and demonstrate that it not only outperforms existing methods but also, in contrast to them, does not require prior knowledge about uncontaminated samples. Finally, we use ConStat to investigate contamination in popular models and find, among others, very high levels of contamination in Mistral-7b-v0.1 and Yi-34b and high levels of contamination in Llama-3-70b and Llama-2-Instruct-70b.\"\n\n---\n\n### 9. Ablation Studies (Appendix B)\n\nSimulation-based ablations varying:\n- Distribution type: robustness to different underlying distributions\n- Non-linearity: hardness correction function flexibility test\n- Noise sensitivity: stability under measurement error\n- Bootstrap methodology: reference set selection sensitivity\n- Presence/absence of random baseline model: impact on correction function\n\nAll ablations validated core design choices of ConStat.\n\n---\n\n### 10. Implementation Details (Appendix C)\n\n- **Evaluation framework:** LM Evaluation Harness, 5-shot setting\n- **Benchmarks capped:** 2000 samples each (computational constraint)\n- **Synthetic generation:** GPT-4-Turbo, ~1000 synthetic samples per benchmark (rephrasing + new generation)\n- **Reference model set:** 20 models from Meta (Llama families), Microsoft (Phi-2, Phi-3), Google (Gemma-1.1), Mistral (multiple versions), Falcon-7b, OLMo + random baseline\n- **Controlled study:** Finetuning Llama-2-Instruct-7b and Phi-2 on benchmark halves\n- **Code:** Python 3.10, conda env, installable via `pip install -e .`\n- **Data:** Password-protected benchmark data + model outputs for reproducibility\n\n---\n\n### 11. Narrative Analysis\n\n**Story type:** \"突破局限型\" (Breaking Through Limitations) — reframes the problem definition to bypass the evasion vulnerability of all prior work.\n\n**Hook:** Opens with the LLM benchmark competition landscape, then immediately pivots to the contamination problem as undermining the entire evaluation infrastructure.\n\n**Tension source:** All prior detection methods share the same fundamental flaw (perplexity-based, easily evaded) AND require oracle access to uncontaminated samples, making them practically inapplicable. ConStat requires neither.\n\n**Key insight position:** Section 2 (early) — the conceptual shift from \"did training data contain benchmark samples\" to \"does performance generalize\" is the paper's load-bearing idea, presented before the method.\n\n**Argument chain:** Benchmarks matter → contamination inflates metrics → existing methods fail (evasion + oracle requirement) → redefine contamination as non-generalizing performance → measure via reference benchmarks + reference models → statistical test with hardness correction → 89.1%/98.4% detection, r²=0.94 quantification → real-world: Mistral, Llama, Yi, top leaderboard models contaminated.\n\n**Notable technique:** Three-tier contamination taxonomy (syntax/sample/benchmark-specific) creates a graduated severity framework that structures the entire evaluation narrative.&lt;/result>\n&lt;usage>&lt;total_tokens>37045&lt;/total_tokens>&lt;tool_uses>27&lt;/tool_uses>&lt;duration_ms>347424&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---


### Assistant

_source line 94 · 2026-05-21T16:43:30.216Z_

<details><summary>Logged reasoning block</summary>

```text
preference_leakage2026 data is back. Let me write its YAML now, and continue waiting for others.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce89e433-0020-48b1-9699-611aa888374d",
  "isSidechain": false,
  "requestId": "req_011CbG3pXJV81HYaHqphuadi",
  "type": "assistant",
  "uuid": "4a7eacaf-40ad-468b-a832-445fbf38a695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCaVdRjjVVUY8WX8Sfdd3B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8009,
      "cache_read_input_tokens": 61083,
      "output_tokens": 2325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2325,
          "cache_read_input_tokens": 61083,
          "cache_creation_input_tokens": 8009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8009
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 95 · 2026-05-21T16:43:31.197Z_

preference_leakage2026 数据已返回，写入 YAML。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a7eacaf-40ad-468b-a832-445fbf38a695",
  "isSidechain": false,
  "requestId": "req_011CbG3pXJV81HYaHqphuadi",
  "type": "assistant",
  "uuid": "b8f13a1f-8cfb-40e3-9c9f-aef4c228ef12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCaVdRjjVVUY8WX8Sfdd3B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8009,
      "cache_read_input_tokens": 61083,
      "output_tokens": 2325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2325,
          "cache_read_input_tokens": 61083,
          "cache_creation_input_tokens": 8009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8009
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-21T16:44:21.852Z_

<details open><summary>🔧 Tool call — Write · `toolu_01FEgT7KN6s4HNEQaCGwp3k7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/preference_leakage2026.yaml",
  "content": "paper_key: \"preference_leakage2026\"\ntitle: \"Preference Leakage: A Contamination Problem in LLM-as-a-judge\"\nvenue: \"ICLR 2026\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"GPT-4o judge\", \"Gemini-1.5-flash judge\", \"LLaMA-3.3-70B judge\", \"Claude-3.5-Sonnet judge\", \"Naive evaluation (no debiasing)\", \"Prompting\", \"Chain-of-Thought\", \"Paraphrase\", \"Auto Calibration\", \"Contextual Calibration\"]\n  metrics:\n    - {name: \"Preference Leakage Score (PLS)\", direction: \"lower_better\"}\n    - {name: \"Error Bias\", direction: \"lower_better\"}\n    - {name: \"Win Rate (WR)\", direction: \"context_dependent\"}\n    - {name: \"Student Recognition Accuracy\", direction: \"diagnostic\"}\n  datasets:\n    - {name: \"Arena-Hard\", size: \"500 questions\"}\n    - {name: \"AlpacaEval 2.0\", size: \"805 questions\"}\n    - {name: \"Ultrafeedback (synthetic data source)\", size: \"30k prompts\"}\n  ablation_dimensions: [\"Relatedness type (same/inheritance/family)\", \"Learning method (SFT/DPO/ICL)\", \"Data mixing ratio\", \"Spurious feature type (style/format/wording)\", \"Student model size\", \"Cross-lingual (EN/ZH)\", \"Mitigation methods\"]\n  training_recipe: {optimizer: \"AdamW\", lr: \"1e-5\", hardware: \"8× A100, CUDA 11.8, BF16, LLaMA-Factory\"}\n  method_family: \"Contamination analysis in LLM-as-a-judge (judge-side bias)\"\n\npositioning:\n  core_claim: \"当数据生成器和评判LLM存在关联时，评判者的偏好会通过合成数据泄露到学生模型中，造成评分虚高——这是一种新型的、比egocentric bias更隐蔽的污染\"\n  key_results: \"PLS最高达50.7%(Qwen-2.5-3B, Arena-Hard); SFT>>DPO>>ICL in leakage; style/format removal各减半leakage; contextual calibration: Error Bias 17.8→7.3; smaller students→higher PLS\"\n  limitations:\n    - \"仅覆盖AlpacaEval和Arena-Hard两个benchmark\"\n    - \"Judge LLM无法自行检测preference leakage（识别率≈随机）\"\n    - \"Contextual calibration仅减少但未消除bias\"\n    - \"不同generator的leakage程度未充分量化\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"LLM-as-judge和LLM数据合成是两大基础方法，但当generator和judge有关联时会产生隐蔽偏差\"\n  tension: \"现有工作关注position bias / length bias / egocentric bias，但忽略了generator-judge关联导致的preference leakage——更隐蔽（judge自身检测≈随机），且在主流benchmark中普遍存在\"\n  key_insight: \"Section 3 形式化定义三种relatedness类型（same model / inheritance / same family），将contamination问题从数据层面推广到评判者偏好传递层面\"\n  argument_chain: \"LLM-as-judge + synthetic data普遍 → generator-judge relatedness未被研究 → 定义PLS指标 → 实验证实PLS显著 → 分析机制(spurious features, 非内容偏好) → 现有mitigation不足\"\n  contribution_framing: \"三条贡献：(1)首次提出preference leakage概念 (2)跨模型跨benchmark大规模实验 (3)机制分析揭示subtlety\"\n  intro_structure: \"4段：LLM评测困境 → LLM-as-judge范式及已知问题 → 引入preference leakage核心概念 → 3个RQ\"\n  notable_technique: \"用BERT分类器(82.4%)证明stylistic fingerprint客观存在但judge LLM自身检测≈随机，优雅地论证了leakage的隐蔽性\"\n\nfigures:\n  figure_count: 3\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Data leakage vs Preference leakage对比图 + 三种relatedness类型示意\"\n    narrative_role: \"一图定义核心概念，将新问题与已知问题类比帮助读者快速理解\"\n    design_elements: [\"左右对比布局\", \"三种relatedness用不同颜色/连线\", \"箭头标注数据流向\"]\n    visual_style: \"概念图，左侧data leakage经典示意，右侧preference leakage新框架，色彩区分relatedness层级\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"line_plot + bar_chart\"\n      what_compared: \"学生模型size对PLS的影响; 数据混合比例对PLS的影响\"\n      how_gain_highlighted: \"趋势线展示smaller model→higher PLS的反直觉发现\"\n      design_note: \"两个子图并排，(a)size scaling (b)data mixing，紧凑展示两个关键变量\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"bar_chart\"\n      what_compared: \"不同question type和judgment dimension下的PLS差异\"\n      how_gain_highlighted: \"subjective vs objective的对比突出leakage的非均匀分布\"\n      design_note: \"按category分组的bar chart，直观展示哪些维度更受影响\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(概念定义) → Figure 2(scaling+mixing) → Figure 3(机制分析)\"\n\ntables:\n  table_count: 14\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"student models\"\n    col_axis: \"judge pairs × benchmarks\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"颜色背景编码PLS正负和强度（蓝=负/无leakage，紫=正/有leakage，深浅=强度）\"\n    statistical_reporting: \"Bootstrap significance (n=10000) in Table 11\"\n    num_baselines: 6\n    design_note: \"颜色热力图编码让pattern一目了然；正负值区分有无leakage\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"Relatedness type\"]\n      variation_style: \"full_numbers\"\n      design_note: \"按relatedness从强到弱排列，展示PLS随距离衰减\"\n    - table_id: \"Table 3\"\n      what_varied: [\"Learning method (SFT/DPO/ICL)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"三种学习方式对比，SFT>>DPO>>ICL清晰展示\"\n    - table_id: \"Table 6\"\n      what_varied: [\"Spurious feature removal (style/format/wording)\"]\n      variation_style: \"delta_from_base\"\n      design_note: \"移除各类spurious feature后PLS变化，直接量化各因素贡献\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 8(PLS计算示例)、Table 9-10(稳定性/prompt敏感性)、Table 11(bootstrap显著性)、Table 12-14(cross-lingual/extended judges/size scaling详细数据)\"\n    reason: \"主表放核心发现，附录放robustness checks和扩展实验\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8f13a1f-8cfb-40e3-9c9f-aef4c228ef12",
  "isSidechain": false,
  "requestId": "req_011CbG3pXJV81HYaHqphuadi",
  "type": "assistant",
  "uuid": "eca24e20-2b3d-4c80-8bf9-c4f7869795c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCaVdRjjVVUY8WX8Sfdd3B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8009,
      "cache_read_input_tokens": 61083,
      "output_tokens": 2325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2325,
          "cache_read_input_tokens": 61083,
          "cache_creation_input_tokens": 8009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8009
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-21T16:44:21.869Z_

<details><summary>↩ Tool result · `toolu_01FEgT7KN6s4HNEQaCGwp3k7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/preference_leakage2026.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eca24e20-2b3d-4c80-8bf9-c4f7869795c6",
  "isSidechain": false,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "type": "user",
  "uuid": "2cf0ef91-7b47-4991-83af-92276899fa37",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/preference_leakage2026.yaml",
    "content": "paper_key: \"preference_leakage2026\"\ntitle: \"Preference Leakage: A Contamination Problem in LLM-as-a-judge\"\nvenue: \"ICLR 2026\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"GPT-4o judge\", \"Gemini-1.5-flash judge\", \"LLaMA-3.3-70B judge\", \"Claude-3.5-Sonnet judge\", \"Naive evaluation (no debiasing)\", \"Prompting\", \"Chain-of-Thought\", \"Paraphrase\", \"Auto Calibration\", \"Contextual Calibration\"]\n  metrics:\n    - {name: \"Preference Leakage Score (PLS)\", direction: \"lower_better\"}\n    - {name: \"Error Bias\", direction: \"lower_better\"}\n    - {name: \"Win Rate (WR)\", direction: \"context_dependent\"}\n    - {name: \"Student Recognition Accuracy\", direction: \"diagnostic\"}\n  datasets:\n    - {name: \"Arena-Hard\", size: \"500 questions\"}\n    - {name: \"AlpacaEval 2.0\", size: \"805 questions\"}\n    - {name: \"Ultrafeedback (synthetic data source)\", size: \"30k prompts\"}\n  ablation_dimensions: [\"Relatedness type (same/inheritance/family)\", \"Learning method (SFT/DPO/ICL)\", \"Data mixing ratio\", \"Spurious feature type (style/format/wording)\", \"Student model size\", \"Cross-lingual (EN/ZH)\", \"Mitigation methods\"]\n  training_recipe: {optimizer: \"AdamW\", lr: \"1e-5\", hardware: \"8× A100, CUDA 11.8, BF16, LLaMA-Factory\"}\n  method_family: \"Contamination analysis in LLM-as-a-judge (judge-side bias)\"\n\npositioning:\n  core_claim: \"当数据生成器和评判LLM存在关联时，评判者的偏好会通过合成数据泄露到学生模型中，造成评分虚高——这是一种新型的、比egocentric bias更隐蔽的污染\"\n  key_results: \"PLS最高达50.7%(Qwen-2.5-3B, Arena-Hard); SFT>>DPO>>ICL in leakage; style/format removal各减半leakage; contextual calibration: Error Bias 17.8→7.3; smaller students→higher PLS\"\n  limitations:\n    - \"仅覆盖AlpacaEval和Arena-Hard两个benchmark\"\n    - \"Judge LLM无法自行检测preference leakage（识别率≈随机）\"\n    - \"Contextual calibration仅减少但未消除bias\"\n    - \"不同generator的leakage程度未充分量化\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"LLM-as-judge和LLM数据合成是两大基础方法，但当generator和judge有关联时会产生隐蔽偏差\"\n  tension: \"现有工作关注position bias / length bias / egocentric bias，但忽略了generator-judge关联导致的preference leakage——更隐蔽（judge自身检测≈随机），且在主流benchmark中普遍存在\"\n  key_insight: \"Section 3 形式化定义三种relatedness类型（same model / inheritance / same family），将contamination问题从数据层面推广到评判者偏好传递层面\"\n  argument_chain: \"LLM-as-judge + synthetic data普遍 → generator-judge relatedness未被研究 → 定义PLS指标 → 实验证实PLS显著 → 分析机制(spurious features, 非内容偏好) → 现有mitigation不足\"\n  contribution_framing: \"三条贡献：(1)首次提出preference leakage概念 (2)跨模型跨benchmark大规模实验 (3)机制分析揭示subtlety\"\n  intro_structure: \"4段：LLM评测困境 → LLM-as-judge范式及已知问题 → 引入preference leakage核心概念 → 3个RQ\"\n  notable_technique: \"用BERT分类器(82.4%)证明stylistic fingerprint客观存在但judge LLM自身检测≈随机，优雅地论证了leakage的隐蔽性\"\n\nfigures:\n  figure_count: 3\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Data leakage vs Preference leakage对比图 + 三种relatedness类型示意\"\n    narrative_role: \"一图定义核心概念，将新问题与已知问题类比帮助读者快速理解\"\n    design_elements: [\"左右对比布局\", \"三种relatedness用不同颜色/连线\", \"箭头标注数据流向\"]\n    visual_style: \"概念图，左侧data leakage经典示意，右侧preference leakage新框架，色彩区分relatedness层级\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"line_plot + bar_chart\"\n      what_compared: \"学生模型size对PLS的影响; 数据混合比例对PLS的影响\"\n      how_gain_highlighted: \"趋势线展示smaller model→higher PLS的反直觉发现\"\n      design_note: \"两个子图并排，(a)size scaling (b)data mixing，紧凑展示两个关键变量\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"bar_chart\"\n      what_compared: \"不同question type和judgment dimension下的PLS差异\"\n      how_gain_highlighted: \"subjective vs objective的对比突出leakage的非均匀分布\"\n      design_note: \"按category分组的bar chart，直观展示哪些维度更受影响\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(概念定义) → Figure 2(scaling+mixing) → Figure 3(机制分析)\"\n\ntables:\n  table_count: 14\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"student models\"\n    col_axis: \"judge pairs × benchmarks\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"颜色背景编码PLS正负和强度（蓝=负/无leakage，紫=正/有leakage，深浅=强度）\"\n    statistical_reporting: \"Bootstrap significance (n=10000) in Table 11\"\n    num_baselines: 6\n    design_note: \"颜色热力图编码让pattern一目了然；正负值区分有无leakage\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"Relatedness type\"]\n      variation_style: \"full_numbers\"\n      design_note: \"按relatedness从强到弱排列，展示PLS随距离衰减\"\n    - table_id: \"Table 3\"\n      what_varied: [\"Learning method (SFT/DPO/ICL)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"三种学习方式对比，SFT>>DPO>>ICL清晰展示\"\n    - table_id: \"Table 6\"\n      what_varied: [\"Spurious feature removal (style/format/wording)\"]\n      variation_style: \"delta_from_base\"\n      design_note: \"移除各类spurious feature后PLS变化，直接量化各因素贡献\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 8(PLS计算示例)、Table 9-10(稳定性/prompt敏感性)、Table 11(bootstrap显著性)、Table 12-14(cross-lingual/extended judges/size scaling详细数据)\"\n    reason: \"主表放核心发现，附录放robustness checks和扩展实验\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "eca24e20-2b3d-4c80-8bf9-c4f7869795c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 98 · 2026-05-21T16:44:21.890Z_

```json
{
  "parentUuid": "2cf0ef91-7b47-4991-83af-92276899fa37",
  "isSidechain": false,
  "attachment": {
    "type": "queued_command",
    "prompt": "&lt;task-notification>\n&lt;task-id>a744e5363d82fb6b7&lt;/task-id>\n&lt;tool-use-id>toolu_01FnCSPe7dcAgNywdUD8bfxY&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/a744e5363d82fb6b7.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: cyclicjudge2026\" completed&lt;/summary>\n&lt;result>I now have the complete text of the paper. Here is all extracted content:\n\n---\n\n## CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\n\n**arXiv:** 2603.01865v3 (submitted March 2, 2026; updated May 4, 2026)\n**Authors:** Ziyi Zhu¹, Olivier Tieleman¹, Alexey Bukhtiyarov¹, Jinghong Chen²\n**Affiliations:** ¹Slingshot AI, ²Department of Engineering, University of Cambridge\n**Correspondence:** ziyi@slingshotai.com\n\n---\n\n## Abstract (verbatim)\n\nLLM-as-judge evaluation has become standard practice for open-ended model assessment; however, judges exhibit systematic biases that cannot be averaged out by increasing the number of scenarios or generations. These biases are often similar in magnitude to the model differences that benchmarks are designed to detect, resulting in unreliable rankings when single-judge evaluations are used. We introduce a variance decomposition that partitions benchmark score variance into scenario, generation, judge, and residual components. Based on this analysis, CyclicJudge, a round-robin assignment of judges to scenarios, is demonstrated to be the optimal strategy for a fixed judge panel and judge-call budget: the score recovers the panel mean exactly while matching the cost of single-judge evaluation. Empirical results on MT-Bench and MindEval validate the effectiveness of CyclicJudge as predicted, across both general-purpose and domain-specific evaluation settings.\n\n---\n\n## Section 1: Introduction (verbatim)\n\nLLM-as-judge evaluation has become the de facto standard for open-ended model assessment (Zheng et al., 2023). A growing body of work indicates that LLM judges are systematically biased: some models are consistently lenient, others strict, with additional position, verbosity, and self-preference effects (Zheng et al., 2023; Shi et al., 2024; Wang et al., 2024). A standard Analysis of Variance (ANOVA; Fisher, 1925) on our data confirms that judge main effect is highly significant (§4.2).\n\nCrucially, systematic bias does not average away across more scenarios or generations: reducing them requires aggregating across multiple judges. Yet running every judge on every item multiplies evaluation cost by the panel size and sacrifices generation diversity at a fixed budget. Throughout this work, we treat the mean score of a diverse K_tot-judge panel as the reference for evaluation; our goal is to recover this panel mean efficiently.\n\nWe show that CyclicJudge, a round-robin assignment of judges to items, resolves this tension. To establish this formally, we develop a variance decomposition rooted in generalizability theory (Brennan, 2001; Shavelson and Webb, 1991) that separates benchmark score variance into scenario, generation, judge, and residual components.\n\n**Our contributions are:**\n\n1. A mixed-effects model that decomposes benchmark variance into random noise and panel-relative judge offsets, showing they require fundamentally different remedies (§3.1–3.2).\n2. A proof that round-robin cycling achieves lower variance than alternative strategies: it cancels the panel-relative offsets exactly while maximizing generation diversity at any budget (§3.3).\n3. Empirical results on MT-Bench and MindEval validating the effectiveness of CyclicJudge as predicted, across both general-purpose and domain-specific evaluation settings (§4).\n\n---\n\n## Section 2: Related Work (verbatim)\n\n**LLM judge biases and multi-judge approaches.** LLM judges exhibit systematic position bias (Wang et al., 2024; Shi et al., 2024), length bias (Dubois et al., 2024), self-preference (Wataoka et al., 2024), and cognitive biases (Koo et al., 2024); we refer readers to Gu et al. (2024) for a comprehensive survey. Multi-judge panels mitigate these biases by averaging over diverse judge tendencies (Verga et al., 2024), while psychometric reliability analyses further demonstrate that single-judge evaluations yield insufficiently stable scores (Schroeder and Wood-Doughty, 2024).\n\n**Benchmark reliability and generation variance.** Madaan et al. (2025) empirically quantifies variance across hundreds of models and benchmarks, and Alvarado Gonzalez et al. (2025) shows via ANOVA that unrepeated evaluations frequently produce rank inversions across benchmark subcategories. Zhang et al. (2025) proposes a hierarchical model decomposing variance into within-prompt and between-prompt components, and Mizrahi et al. (2024) shows that prompt paraphrasing alone can reverse model rankings. Our work extends this line by further separating systematic judge bias from random noise.\n\n**Budget-constrained evaluation.** Saha et al. (2026) frames judge selection as a multi-armed bandit problem, Luettgau et al. (2025) applies hierarchical Bayesian partial pooling in low-data regimes, and Miller (2024) derives standard errors and power formulas for benchmark scores; Dorner et al. (2025) further establishes fundamental scaling limits on the accuracy gains from additional judge queries.\n\n---\n\n## Section 3: Methodology (verbatim)\n\n### 3.1 Model Specification\n\nConsider evaluating model θ on n scenarios from a dataset D of N total scenarios, with m independent generations per scenario, each scored by K judges drawn from a pool of K_tot. The same K judges score every scenario–generation cell (a crossed design). We model each score as:\n\n**X_ijℓ = μ_θ + α_i + β_ij + γ_ℓ + ε_ijℓ** (Eq. 1)\n\nwhere i ∈ {1, …, n} indexes scenarios, j ∈ {1, …, m} indexes generations within scenario i, and ℓ indexes the K selected judges. Each term has a distinct source:\n\n- **μ_θ**: panel-mean estimand for model θ—the average score the K_tot-judge panel would assign in expectation, with random noise removed.\n- **α_i ~ iid (0, σ_α²)**: scenario effect—how much individual scenario difficulty varies for model θ. A dataset whose scenarios all test the same aspects of model θ equally has σ_α² = 0.\n- **β_ij ~ iid (0, σ_β²)**: generation effect—variability from stochastic decoding. σ_β² is model-specific; a deterministic model has σ_β² = 0.\n- **γ_ℓ**: judge offset relative to the panel mean—a fixed constant for each judge, with centering constraint Σγ_ℓ = 0 and population dispersion σ_γ² = K_tot⁻¹ Σ γ_ℓ². γ_ℓ measures deviation from the panel reference, not from absolute truth: bias shared by all panel members is absorbed into μ_θ.\n- **ε_ijℓ ~ iid (0, σ_ε²)**: residual—captures judge-level noise and all interaction terms.\n\nThe random effects (α, β, ε) are mutually independent with finite second moments; no distributional assumptions (e.g. Gaussianity) are needed. The n scenarios and K judges are each drawn by simple random sampling without replacement, independently of each other and of all random effects.\n\n### 3.2 Variance Decomposition\n\nThe benchmark score is the grand mean X̄ = (1/nmK) Σ X_ijℓ, which decomposes as X̄ = μ_θ + ᾱ + β̄ + γ̄ + ε̄.\n\n**Proposition 1 (Variance decomposition):**\n\nVar(X̄) = [σ_α²/n + σ_β²/nm + σ_ε²/nmK] + [σ_γ²/K · (K_tot − K)/(K_tot − 1)]\n           |___________ random noise ____________|   |________ V_γ: judge bias ________|   (Eq. 2)\n\nEach noise term shrinks with more data at or above its hierarchy level. The bias term V_γ responds only to K and vanishes exactly at K = K_tot. The proof uses the law of total variance, conditioning on the judge selection, combined with a finite population correction for sampling K from K_tot centered bias values (Appendix C).\n\n### 3.3 Allocation Strategies\n\nGiven a per-scenario budget of B judge calls, the design question is how to allocate judges across generations. The scenario term σ_α²/n is fixed once scenarios are chosen; we compare three strategies for the remaining variance.\n\n**Strategy A: All judges per generation.** Use all K_tot judges for each of m = B/K_tot generations. The mean of all judge offsets is zero (γ̄ = 0):\n\nV_A(B) = (K_tot σ_β² + σ_ε²) / nB   (Eq. 3)\n\n**Strategy B: Random single judge per generation.** Use m = B generations, each scored by one randomly sampled judge. Random judge selection injects the panel-relative offset as additional sampling noise:\n\nV_B(B) = (σ_β² + σ_γ² + σ_ε²) / nB   (Eq. 4)\n\n**Strategy C: CyclicJudge (round-robin).** Use m = B generations, assigning judge j mod K_tot to generation j. Each judge appears equally often, so the panel-relative offsets sum to zero (γ̄ = 0):\n\nV_C(B) = (σ_β² + σ_ε²) / nB   (Eq. 5)\n\nWith one generation per scenario (m = 1), the same variance and offset cancellation is achieved by cycling judges across scenarios instead. In this case scenarios should be shuffled before assignment to avoid confounding the cycle with any latent ordering of the dataset.\n\n**Advantage of CyclicJudge.** Direct comparison (Appendix E) shows V_C ≤ min(V_A, V_B) for all B, with gaps of O(1/B), so CyclicJudge's advantage is largest at small budgets of judge calls. The ranking of A vs. B depends on whether (K_tot − 1)σ_β² ≷ σ_γ²: all judges beat random only when judge bias is large relative to generation variance.\n\n---\n\n## Section 4: Experiments (verbatim)\n\n### 4.1 Domain and Data\n\nWe validate our approach on two benchmarks:\n\n**MT-Bench** (Zheng et al., 2023) is a general-purpose multi-turn conversational benchmark with 80 two-turn questions spanning 8 categories, scored on a 1–10 scale per turn (averaged).\n\n**MindEval** (Pombal et al., 2025) is a domain-specific benchmark for multi-turn mental health support with 50 scenarios and composite scores on a 1–5 scale covering empathy, safety, and clinical appropriateness. Each scenario simulates a full 10-turn therapeutic session with a synthetic patient.\n\nFor both benchmarks, we evaluate five models—Qwen 2.5 7B Instruct (Yang et al., 2024), Llama 3.3 70B Instruct (Grattafiori et al., 2024), GPT-5.2, Gemini 3 Flash, and Claude Sonnet 4.6, which also serve as judges in a symmetric design. MT-Bench uses m=10 generations per scenario (4,000 scores per model); MindEval uses m=5 (1,250 scores per model). We follow the default judge decoding hyperparameters from reference (Appendix J).\n\n### 4.2 Judge Bias Estimates\n\nAs a complementary omnibus check on the mixed-effects decomposition (§3.1), we test whether judge identity has a significant effect using a two-way ANOVA, treating each scenario–generation pair as a subject crossed with K judges. On both benchmarks, the judge main effect is highly significant (p &lt; 0.001 in all cases; see Appendix H).\n\nTable 1 demonstrates that single-judge evaluation produces unreliable rankings. On MT-Bench at the default operating point (m=1, K=1), the top-ranked model changes with every judge, with Qwen ranking itself first despite being last by consensus, a pattern consistent with the self-preference bias documented by Wataoka et al. (2024). The per-observation variance estimates (Table 2) confirm this quantitatively: judge variance σ̂_γ² ranges from 0.34 to 0.95 across models. Since competitive models on current leaderboards are routinely separated by &lt; 0.5 points (Chiang et al., 2024), single-judge evaluation can easily reverse rankings. On MindEval, rankings are also notably more stable across single judges: four of five produce an identical ordering. Two plausible factors include: domain-specific rubrics may leave less room for stylistic self-preference, and the markedly lower scenario and generation variance on MindEval (§4.3) compresses the absolute size of any model-dependent fluctuations.\n\n### 4.3 Variance Components\n\nTable 2 reports the per-observation variance component estimates via crossed ANOVA (see Appendix D). On MT-Bench, scenario variance σ̂_α² is the largest per-observation component; maximizing the number of distinct scenarios always reduces total variance (Appendix F). Generation variance σ̂_β² drops with capability, consistent with the observation that stronger models produce more deterministic outputs. As frontier models increasingly rely on RL post-training, generation variance may shrink further (Matsutani et al., 2025). The judge offset variance σ̂_γ² remains substantial for all models, accounting for &gt;94% of benchmark variance at the default operating point (see Appendix B).\n\nOn MindEval, both scenario and generation variance are markedly lower. Scenario variance σ̂_α² drops by one to two orders of magnitude because all MindEval scenarios evaluate the same rubrics across different user profiles, so difficulty varies far less than on MT-Bench. Generation variance is similarly suppressed: each MindEval generation is a full 10-turn therapeutic session, so per-response decoding randomness averages out over many turns. The judge offset variance remains the dominant component throughout, exceeding both scenario and generation variance by an order of magnitude.\n\n### 4.4 Strategy Comparison\n\nFigure 1 validates the three allocation strategies via 5,000 subsampling repetitions at each budget level on both benchmarks. Markers show empirical variance; dashed lines show exact predictions from empirical pool variances (Appendix G). CyclicJudge achieves lower variance everywhere on both benchmarks, and predictions match empirical results precisely. At B=5, switching from random to cycling cuts variance by ~27–40% across models on MT-Bench.\n\nThe optimal strategy among the two alternatives depends on the sign of (K_tot − 1)σ_β² − σ_γ²: all-judges wins when σ_γ²/σ_β² &gt; K_tot − 1 = 4. On MT-Bench, this ratio is below the threshold for Qwen (3.6) and Llama (2.1), so random judging is preferable; for Gemini and Claude (σ̂_β² ≈ 0), all-judges converges to CyclicJudge. On MindEval, the ratio exceeds the threshold for nearly every model, so all-judges consistently outperforms random. The driver is not a larger judge offset variance, but rather a sharply lower generation variance σ̂_β². Meanwhile, judges' disagreement over subjective clinical criteria keeps σ̂_γ² substantial relative to σ̂_β². CyclicJudge outperforms both alternatives regardless of this ratio.\n\n---\n\n## Section 5: Conclusion (verbatim)\n\nWe develop a variance decomposition for LLM-as-judge evaluation that separates systematic between-judge offsets from random noise and use it to derive CyclicJudge, a round-robin judge assignment strategy. Our analysis and experiments on both a general-purpose benchmark (MT-Bench) and a domain-specific clinical benchmark (MindEval) yield three main findings: (1) Systematic judge offsets dominate benchmark score variance at default operating points. (2) Random noise components decrease with model capability and multi-turn evaluation, but the panel-relative offset variance does not. (3) CyclicJudge achieves the lowest variance among all allocation strategies at every budget level, regardless of the model's variance profile, by recovering the panel-mean score exactly while maximizing generation diversity. The method requires no model-specific tuning and maintains the same per-item cost as single-judge evaluation, providing practitioners with a cost-neutral drop-in replacement for more reliable LLM evaluation.\n\n---\n\n## Limitations (verbatim)\n\n**Panel-mean reference.** Our analysis treats the mean score of the K_tot-judge panel as the reference for evaluation. A diverse panel drawn from disjoint model families typically correlates more strongly with human judgments than any single judge (Verga et al., 2024), but the panel mean is not a substitute for absolute ground truth. Biases shared across the panel members are absorbed into μ_θ and propagate into the panel mean. CyclicJudge addresses the within-panel offsets between individual judges, not biases that all panel members share; calibrating the panel itself against human or expert references is complementary work.\n\n**Linear model approximation.** Our variance decomposition assumes a linear random effects model, which treats scores as unbounded and continuous. LLM-as-judge scores are in fact bounded ordinal variables, so the linear model can produce boundary artifacts and heteroscedastic residuals near the scale endpoints. A generalized linear mixed model (GLMM), such as a cumulative-link mixed model, would properly account for the ordinal, bounded nature of the responses. However, GLMMs do not yield the closed-form variance decomposition that our allocation analysis relies on. We therefore retain the linear approximation, noting that it remains reasonable when the scale range is large relative to the observed score dispersion, as in our benchmarks.\n\n**Judge pool size.** Our judge pool of K_tot = 5 limits exploration of larger panels. While the theoretical results generalize to arbitrary K, empirical validation with larger and more diverse judge pools would strengthen the practical recommendations.\n\n**Scenario exchangeability.** The \"maximize scenarios\" recommendation assumes scenarios are interchangeable draws from the dataset; in practice, some scenarios may be more informative than others, and item-selection methods (Maia Polo et al., 2024) could alter the tradeoff.\n\n**Balanced design assumption.** The allocation analysis assumes a balanced design in which every scenario receives the same number of judge calls. Extensions to adaptive or sequential designs remain future work.\n\n**Uniform cost assumption.** Our budget analysis treats all judge calls as equal cost; in practice, judges vary widely in price and latency. A cost-weighted allocation that accounts for per-model pricing and inference speed would be needed for real deployment decisions.\n\n---\n\n## Figure and Table Captions (verbatim)\n\n**Figure 1:** Benchmark score variance Var(X̄) vs. per-scenario budget for three strategies: all judges (A), random single judge (B), and CyclicJudge (C). [Two panels: (a) MT-Bench (1–10 scale, n=80, m_max=10); (b) MindEval (1–5 scale, n=50, m_max=5). Five subplots per panel, one per model: Qwen 2.5 7B, Llama 3.3 70B, GPT-5.2, Gemini 3 Flash, Claude Sonnet 4.6. Markers show empirical variance; dashed lines show exact predictions.]\n\n**Figure 2:** Estimated judge biases γ̂_ℓ = X̄_··ℓ − X̄_··· for each judge–model pair. [Heatmap panels: (a) MT-Bench; (b) MindEval. Rows = judge models, columns = evaluated models.]\n\n**Table 1:** Mean score ± 95% CI at the default operating point (m=1, K=1). Bold: highest score per judge column. Underline: second highest.\n- Panel (a): MT-Bench (1–10 scale, n=80) — 5×5 matrix of judge × model\n- Panel (b): MindEval (1–5 scale, n=50) — 5×5 matrix of judge × model\n\n**Table 2:** Per-observation variance component estimates.\n- Panel (a): MT-Bench (n=80) — rows: σ̂_α², σ̂_β², σ̂_γ², σ̂_ε²; columns: Qwen, Llama, GPT, Gemini, Claude\n- Panel (b): MindEval (n=50)\n\n**Table 3:** Variance component estimates. Per-observation variances and their contribution to Var(X̄) at the default operating point (m=1, K=1).\n- Panel (a): MT-Bench — per-observation variance + contribution to Var(X̄) (×10⁻³)\n- Panel (b): MindEval — same structure\n\n**Table 4:** ANOVA F-statistic for the judge main effect. All p &lt; 0.001.\n- MT-Bench F(4, 3196): Qwen 638.2, Llama 445.8, GPT 601.7, Gemini 659.2, Claude 514.9\n- MindEval F(4, 996): Qwen 1029.5, Llama 1280.1, GPT 200.1, Gemini 458.0, Claude 788.9\n\n**Table 5:** Default judge decoding hyperparameters used by each benchmark's reference implementation.\n- MT-Bench: temperature=0, max_tokens (OpenAI)=2048, max_tokens (Anthropic)=1024\n- MindEval: judge_template_version=v0_1, max_completion_tokens=16,000, reasoning_effort=high\n\n---\n\n## Key Numerical Results\n\n**Table 1a — MT-Bench mean scores (m=1, K=1):**\n\n| Judge\\Model | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| Gemini | 8.02±.16 | 7.91±.16 | 7.96±.17 | 7.87±.18 | 8.02±.15 |\n| GPT | 8.98±.08 | 8.81±.11 | 9.06±.06 | 8.71±.11 | 8.39±.16 |\n| Claude | 8.20±.12 | 8.67±.12 | 7.91±.13 | 6.90±.20 | 6.09±.20 |\n| Llama | 9.88±.06 | 9.71±.11 | 9.62±.12 | 8.58±.25 | 7.16±.27 |\n| Qwen | 8.68±.10 | 8.49±.13 | 8.52±.13 | 7.26±.22 | 5.99±.23 |\n\n**Panel mean (μ̂_θ) MT-Bench:** Qwen 7.13, Llama 7.87, GPT 8.72, Gemini 8.75, Claude 8.61\n\n**Table 1b — MindEval mean scores:**\n\n| Judge\\Model | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| Claude | 3.86±.08 | 4.04±.09 | 3.90±.08 | 3.70±.07 | 3.26±.12 |\n| GPT | 4.67±.07 | 4.51±.07 | 4.49±.06 | 4.29±.05 | 3.38±.21 |\n| Gemini | 4.05±.06 | 3.76±.09 | 3.63±.05 | 3.16±.06 | 2.32±.08 |\n| Llama | 4.72±.06 | 3.95±.16 | 3.91±.12 | 3.00±.10 | 1.69±.08 |\n| Qwen | 4.84±.04 | 3.39±.15 | 3.31±.08 | 2.85±.06 | 1.74±.05 |\n\n**Panel mean (μ̂_θ) MindEval:** Qwen 2.478, Llama 3.400, GPT 3.931, Gemini 3.846, Claude 4.431\n\n**Table 2a — MT-Bench variance components:**\n\n| Component | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| σ̂_α² (scenario) | 1.530 | 0.882 | 0.634 | 0.408 | 0.393 |\n| σ̂_β² (generation) | 0.266 | 0.238 | 0.076 | 0.000 | 0.000 |\n| σ̂_γ² (judge) | 0.947 | 0.503 | 0.339 | 0.435 | 0.427 |\n| σ̂_ε² (residual) | 1.486 | 1.130 | 0.564 | 0.661 | 0.830 |\n\n**Table 2b — MindEval variance components:**\n\n| Component | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| σ̂_α² (scenario) | 0.034 | 0.014 | 0.021 | 0.015 | 0.005 |\n| σ̂_β² (generation) | 0.100 | 0.019 | 0.047 | 0.016 | 0.002 |\n| σ̂_γ² (judge) | 0.523 | 0.280 | 0.132 | 0.150 | 0.155 |\n| σ̂_ε² (residual) | 0.159 | 0.069 | 0.207 | 0.103 | 0.061 |\n\n**Table 3a — MT-Bench contribution to Var(X̄) (×10⁻³) at default operating point:**\n\n| Component | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| σ̂_α²/n | 19.13 | 11.03 | 7.92 | 5.11 | 4.92 |\n| σ̂_β²/nm | 3.33 | 2.97 | 0.94 | 0.00 | 0.00 |\n| σ̂_γ²·FPC/K | 946.50 | 502.50 | 339.00 | 435.40 | 426.60 |\n| σ̂_ε²/nmK | 18.57 | 14.12 | 7.05 | 8.27 | 10.38 |\n\n**Table 3b — MindEval contribution to Var(X̄) (×10⁻³):**\n\n| Component | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| σ̂_α²/n | 0.67 | 0.28 | 0.43 | 0.29 | 0.09 |\n| σ̂_β²/nm | 2.01 | 0.38 | 0.93 | 0.31 | 0.04 |\n| σ̂_γ²·FPC/K | 522.50 | 280.20 | 132.00 | 150.20 | 154.80 |\n| σ̂_ε²/nmK | 3.18 | 1.37 | 4.14 | 2.05 | 1.23 |\n\n---\n\n## Appendix A: Judge Bias Estimates (verbatim)\n\nFigure 2 shows the estimated per-judge bias for each judge–model pair on both benchmarks. A pronounced self-preference is visible along the diagonal: on MindEval, Claude Sonnet 4.6's self-bias of +0.412 is the only positive entry in its otherwise uniformly negative row, and Qwen 2.5 7B's self-bias is the largest in its row on both benchmarks. Judge temperament is not stable across benchmarks: Gemini 3 Flash is the most lenient judge on MT-Bench (all biases positive), yet becomes one of the harshest on MindEval, suggesting that judge personality is benchmark-dependent rather than an intrinsic model property. On MT-Bench, strictness correlates with model capability: the two strongest models by consensus (GPT-5.2 and Claude) are the most uniformly negative judges, while the two weakest (Qwen and Llama) are the most lenient. Finally, the harshest judge–model interactions concentrate on capability-mismatched pairs: GPT-5.2 and Claude penalize Qwen by over one full scale point on MT-Bench, while their biases toward each other are an order of magnitude smaller.\n\n**Judge bias matrix (MT-Bench):**\n\n| Judge\\Model | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| Qwen 2.5 7B | +0.887 | +0.009 | -0.808 | -0.735 | -0.650 |\n| Llama 3.3 70B | +1.257 | +0.848 | +0.091 | +0.224 | +0.446 |\n| GPT-5.2 | -1.040 | -0.962 | -0.044 | -0.550 | -0.707 |\n| Gemini 3 Flash | +0.032 | +0.711 | +0.991 | +1.132 | +1.003 |\n| Claude Sonnet 4.6 | -1.136 | -0.607 | -0.230 | -0.071 | -0.092 |\n\n**Judge bias matrix (MindEval):**\n\n| Judge\\Model | Qwen | Llama | GPT | Gemini | Claude |\n|---|---|---|---|---|---|\n| Qwen 2.5 7B | +0.780 | +0.298 | +0.104 | +0.053 | -0.566 |\n| Llama 3.3 70B | +0.904 | +0.891 | +0.580 | +0.641 | +0.239 |\n| GPT-5.2 | -0.159 | -0.239 | -0.169 | -0.219 | -0.377 |\n| Gemini 3 Flash | -0.786 | -0.399 | +0.021 | +0.061 | +0.293 |\n| Claude Sonnet 4.6 | -0.739 | -0.551 | -0.536 | -0.536 | +0.412 |\n\n---\n\n## Appendix B: Variance at Default Operating Point\n\nThe judge-offset contribution (σ̂_γ²·FPC/K) accounts for &gt;94% of benchmark variance at the default operating point (m=1, K=1) on MT-Bench. Specifically: for Qwen, 946.50/(946.50+19.13+3.33+18.57) ≈ 96.6%.\n\n---\n\n## Appendix C: Proof of Proposition 1 (Variance Decomposition)\n\nThe proof proceeds in three steps: (1) grand mean decomposition, (2) law of total variance, (3) finite population correction.\n\n**Step 1 — Grand mean decomposition:** Starting from X_ijℓ = μ_θ + α_i + β_ij + γ_ℓ + ε_ijℓ, average hierarchically: first over K judges within generation (i,j) — gives X̄_ij· = μ_θ + α_i + β_ij + γ̄ + ε̄_ij; then over m generations within scenario i — gives X̄_i·· = μ_θ + α_i + β̄_i + γ̄ + ε̄_i·; then over n scenarios — gives X̄ = μ_θ + γ̄ + ᾱ + β̄ + ε̄.\n\n**Step 2 — Law of total variance:** Let S denote the judge selection. Var(X̄) = E[Var(X̄|S)] + Var(E[X̄|S]). Given S, γ̄ is constant → Var(X̄|S) = σ_α²/n + σ_β²/nm + σ_ε²/nmK (does not depend on S). E[X̄|S] = μ_θ + γ̄ → Var(E[X̄|S]) = Var(γ̄).\n\n**Step 3 — Finite population correction (Lemma 2):** For a simple random sample of size k from P elements with centering constraint Σa_i = 0 and σ_a² = P⁻¹ Σa_i²: Var(āS) = (σ_a²/k) · (P−k)/(P−1). Applying to judge biases (a_ℓ = γ_ℓ, P = K_tot, k = K): Var(γ̄) = (σ_γ²/K) · (K_tot − K)/(K_tot − 1).\n\n---\n\n## Appendix D: Estimation of Variance Components\n\nMethod-of-moments estimators using crossed ANOVA:\n- **σ̂_ε² = MSW** (residual mean square)\n- **σ̂_β² = (MSG − MSW)/K** (between-generation mean square, can be negative → truncated to 0)\n- **σ̂_α² = (MSS − MSG)/(mK)** (between-scenario mean square)\n- **σ̂_γ² = (1/K_tot) Σ γ̂_ℓ² − σ̂_ε² · (K_tot−1)/(nm·K_tot)**\n\nwhere γ̂_ℓ = X̄_··ℓ − X̄_···.\n\nZero-truncation note: negative estimates of σ̂_β² (Gemini and Claude on MT-Bench) are set to zero per standard convention—indicates generation-to-generation variability is negligible relative to residual noise.\n\n---\n\n## Appendix E: Allocation Strategy Derivations (Pairwise comparisons)\n\n- V_A − V_C = (K_tot − 1)σ_β² / nB ≥ 0\n- V_B − V_C = σ_γ² / nB ≥ 0\n- V_A − V_B = [(K_tot − 1)σ_β² − σ_γ²] / nB (sign depends on data)\n\n---\n\n## Appendix F: Scenario Coverage\n\nUnder cycling, variance as function of m with total budget B_gen = nm:\n\nV_C(B_gen, m) = m(σ_α² + σ_β² + σ_ε²) / B_gen   (Eq. 35)\n\nThis is linear in m with positive slope σ_α²/B_gen, so variance is minimized at m=1, maximizing the number of distinct scenarios up to dataset size N. Once the scenario pool is exhausted (n=N), excess budget should go to additional generations.\n\n---\n\n## Appendix G: Exact Bootstrap Predictions\n\nFor finite pool of m_max observed generations, exact predictions use empirical pool variances:\n- Strategy A: C_A = K_tot · (1/n) Σ_i [(1/m_max) Σ_g (X̄_ig· − X̄_i··)²]\n- Strategy B: C_B = (1/n) Σ_i [(1/(m_max K_tot)) Σ_{g,ℓ} (X_igℓ − X̄_i··)²]\n- Strategy C: C_C = (1/(nK_tot)) Σ_{i,ℓ} [(1/m_max) Σ_g (X_igℓ − X̄_i·ℓ)²]\n\n---\n\n## Appendix H: ANOVA F-Test for Judge Effects\n\nTwo-way crossed ANOVA, F = MSJ/MSR with K−1 and (N−1)(K−1) degrees of freedom.\n\n| Model | MT-Bench F(4,3196) | MindEval F(4,996) |\n|---|---|---|\n| Qwen 2.5 7B | 638.2 | 1029.5 |\n| Llama 3.3 70B | 445.8 | 1280.1 |\n| GPT-5.2 | 601.7 | 200.1 |\n| Gemini 3 Flash | 659.2 | 458.0 |\n| Claude Sonnet 4.6 | 514.9 | 788.9 |\n\nAll p &lt; 0.001.\n\n---\n\n## Appendix I: Omitted Interactions\n\nThe model retains grand mean and three main effects, absorbing all interaction terms into residual ε_ijℓ:\n\n- **Scenario–generation:** Generations nested within scenarios, confounded with β_ij by construction.\n- **Scenario–judge:** Estimable in principle (n(K_tot−1) additional parameters) but enters only through per-cell residual variance, already captured empirically in §4.\n- **Generation–judge:** Exchangeable across j, acts as additional i.i.d. noise, absorbed into σ_ε².\n\n---\n\n## Appendix J: Judge Hyperparameter Settings\n\n**MT-Bench:** temperature=0, max_tokens (OpenAI)=2048, max_tokens (Anthropic)=1024.\n**MindEval:** judge_template_version=v0_1, max_completion_tokens=16,000, reasoning_effort=high.\n\nFor models outside original API tables (Gemini 3 Flash and Claude Sonnet 4.6 for MT-Bench), closest equivalent setting supported by provider is applied.\n\nEffect of hyperparameters: Decoding hyperparameters control within-judge stochasticity, absorbed into residual ε_ijℓ → contributes to σ_ε². The systematic offset γ_ℓ is a property of the judge model itself, not sampling. Increasing temperature would inflate σ_ε² but, to first order, leave γ_ℓ and σ_γ² unchanged. At the default operating point, judge-offset contribution exceeds residual contribution by roughly two orders of magnitude on both benchmarks. Reasonable perturbations of decoding hyperparameters can only shift σ_ε² within a window much smaller than σ_γ², so the qualitative ranking of allocation strategies is robust to this choice.\n\n---\n\n**Source paper:** [2603.01865] CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation — https://arxiv.org/abs/2603.01865&lt;/result>\n&lt;usage>&lt;total_tokens>40855&lt;/total_tokens>&lt;tool_uses>16&lt;/tool_uses>&lt;duration_ms>316963&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>",
    "commandMode": "task-notification"
  },
  "type": "attachment",
  "uuid": "78a1f501-88fd-4e59-ac1c-638d767accce",
  "timestamp": "2026-05-21T16:44:21.890Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 99 · 2026-05-21T16:44:21.890Z_

```json
{
  "parentUuid": "78a1f501-88fd-4e59-ac1c-638d767accce",
  "isSidechain": false,
  "attachment": {
    "type": "queued_command",
    "prompt": "&lt;task-notification>\n&lt;task-id>ad50cdb495cf40e2d&lt;/task-id>\n&lt;tool-use-id>toolu_015rpQr8sYtDbCzWni2DFwZy&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ad50cdb495cf40e2d.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: lin2025psnirt\" completed&lt;/summary>\n&lt;result>I now have all the material needed. Here is the complete extraction:\n\n---\n\n## Paper: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\n\n**Venue:** AAAI 2026 (Oral), Technical Track on NLP VI, Vol. 40, Issue 41, pp. 35085–35093  \n**arXiv:** 2505.15055 (v1: 2025-05-21, v2: 2025-08-01, v3: 2026-01-16)  \n**Authors:** Hongli Zhou*, Hui Huang*, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang†, Wei Bao†, Jian Dong†, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao  \n**Affiliations:** Faculty of Computing, Harbin Institute of Technology; HIT Shenzhen; China Electronics Standardization Institute  \n**Code:** https://github.com/Joe-Hall-Lee/PSN-IRT\n\n---\n\n## 1. Abstract (verbatim)\n\nThe evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities. This paper provides a critical analysis of benchmark effectiveness, examining mainstream prominent LLM benchmarks using results from diverse models. We first propose Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. PSN-IRT can be utilized for accurate and reliable estimations of item characteristics and model abilities. Based on PSN-IRT, we conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. Furthermore, we demonstrate that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.\n\n---\n\n## 2. Introduction (complete)\n\nAs the scale and performance of large language models (LLMs) continue to grow, accurately measuring their capabilities has become increasingly important (Chang et al. 2024; Zhou et al. 2024; Huang et al. 2025). Currently, the performance of LLMs is primarily evaluated through various benchmarks (Wang et al. 2024), which are comprehensive test suites consisting of carefully designed questions to assess model behavior across different tasks. However, in practice, existing benchmarks often exhibit significant limitations, prompting consideration of their effectiveness (McIntosh et al. 2024).\n\nAs illustrated in Figure 1, on one hand, even benchmarks that are designed to measure similar underlying capabilities often produce inconsistent leaderboards, leading to substantial ranking variations for the same model (Perlitz et al. 2024). On the other hand, many benchmarks show weak separability among top models, limiting the ability to understand performance differences and further model refinement. Given these limitations, there is a growing need for a more systematic analysis of LLM benchmarks.\n\nIn this paper, we conduct a comprehensive analysis for various popular LLM benchmark datasets. Our experiment is based on Item Response Theory (IRT) (Lord, Novick, and Birnbaum 1968; Baker and Kim 2004), a psychometric framework widely used in educational assessment to analyze item properties such as difficulty by modeling item response against examinee ability. However, traditional IRT struggles with the complexity and scale of modern datasets, and its assumption of the normal distribution of abilities does not always hold.\n\nTo advance our objective, we propose the Pseudo-Siamese Network for IRT (PSN-IRT), a framework for comprehensive and interpretable analysis of benchmark test sets. PSN-IRT processes model identifiers and item identifiers through independent neural network pathways. These pathways respectively estimate latent model ability and a rich set of item parameters. The estimated properties are then integrated using an IRT-based formulation to predict outcome probabilities. This architectural design ensures both powerful modeling capabilities and strong theoretical interpretability.\n\nTo validate the effectiveness of PSN-IRT, we conduct extensive experiments on evaluation results from 12 LLMs across 11 benchmarks. Our results show that PSN-IRT outperforms previous approaches in both parameter estimation accuracy and reliability. Based on PSN-IRT, we perform in-depth analyses of these benchmarks using key metrics, with main findings as follows:\n\n1. LLM benchmarks fail to achieve simultaneous excellence across multiple measurements.\n2. LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models.\n3. LLM benchmarks exhibit data contamination in numerous items, compromising their reliability.\n\nFurthermore, we find that model rankings derived from high-quality datasets selected by PSN-IRT are more consistent with human preference and offer stronger discriminability among top models.\n\n**Contributions:**\n1. We propose PSN-IRT, a benchmark analysis framework with superior estimation accuracy and reliability.\n2. We use PSN-IRT for an in-depth analysis of mainstream benchmarks and find that current LLM benchmarks present deficiencies in many aspects.\n3. We show that selecting items with PSN-IRT leads to model rankings that better align with human preference.\n\n---\n\n## 3. Related Work (complete)\n\nResearchers have explored various methods to evaluate and analyze the quality of LLM benchmarks. Recent efforts have introduced quantitative metrics that operate at a holistic, dataset level. For example, Benchmark Agreement Testing (BAT) assesses benchmark reliability by comparing the consistency of model rankings across different leaderboards (Perlitz et al. 2024; White et al. 2025). Other novel metrics have also been proposed for more nuanced dataset-level analysis (Li et al. 2024). Delving deeper than macro-level comparisons, another significant line of work focuses on content-based analysis to ground evaluation in concrete capabilities. For instance, ADeLe (Zhou et al. 2025) leverages scalable cognitive rubrics and item demand features to build highly interpretable capability profiles for AI systems.\n\nItem Response Theory (IRT) (Lord, Novick, and Birnbaum 1968; Baker and Kim 2004) offers a psychometric framework for data-driven, item-level analysis. Within natural language processing (NLP), IRT has been primarily utilized to diagnose fundamental item properties such as difficulty and discriminability (Vania et al. 2021; Byrd and Srivastava 2022). More recently, its principles have also been used to inspire methods for improving evaluation efficiency, for instance, through optimized item selection (Maia Polo et al. 2024) or adaptive testing paradigms (Zhuang et al. 2025; Truong et al. 2025). However, due to the complexity and scale of modern datasets and its assumption of normally distributed abilities, the application of IRT on LLM benchmarks is still underexplored (Ye et al. 2025).\n\n---\n\n## 4. Background: IRT (complete)\n\nItem Response Theory (IRT) (Lord, Novick, and Birnbaum 1968) is a psychometric framework widely used in educational and cognitive assessments to model the relationship between benchmark items and examinee abilities. Unlike Classical Test Theory (CTT) (DeVellis 2006), which relies on aggregate test scores, IRT analyzes individual item responses as a function of a latent ability θ, enabling precise measurement of both item and examinee properties.\n\nCentral to IRT is the Item Characteristic Curve (ICC), a mathematical function that describes the probability of a correct response, P(X=1|θ), as a function of ability θ. Typically logistic, the ICC visualizes how item properties influence performance, serving as the foundation for IRT.\n\nThe simplest IRT model, the One-Parameter Logistic (1PL) model, defines the ICC as:\n\nP(X=1|θ) = 1 / (1 + e^{-(θ−b)})\n\nwhere b denotes item difficulty. When θ=b, the probability of a correct response is 0.5. The 1PL assumes all items have equal discriminability, a simplification that may not hold in complex testing scenarios. More advanced IRT models introduce additional parameters to capture diverse item properties. However, traditional IRT often suffers from inaccurate parameter estimation and relies on assumptions like normal ability distributions, which may not align with real-world data (Tsutsumi, Kinoshita, and Ueno 2021).\n\n---\n\n## 5. Method: PSN-IRT (complete)\n\n### Model Architecture\n\nThe PSN-IRT architecture comprises two independent networks: a model network and an item network. The model network processes one-hot encoded LLM identifiers to estimate model-ability θ, while the item network handles one-hot encoded item identifiers to produce the four IRT parameters: discriminability a, difficulty b, guessing-rate c, and feasibility d.\n\nEach network consists of three fully connected layers with ReLU activation functions, enabling efficient and stable parameter estimation. After that, these estimated properties are then processed by a Logistic Calculation Layer. This layer operates using the Four-Parameter Logistic (4PL) model:\n\nP(X=1|θ) = c + (d−c) · 1/(1+e^{−a(θ−b)})   ... (Eq. 2)\n\nParameter roles:\n- difficulty b: determines the ability level where the probability changes most significantly\n- discriminability a: reflects an item's power to differentiate between models of varying abilities\n- guessing-rate c: captures how likely models are to succeed without full understanding\n- feasibility d: represents the maximum probability that even highly proficient models will correctly answer the item\n\nPSN-IRT follows standard IRT assumptions such as unidimensionality and monotonicity, which generally hold for LLM benchmarking (Kipnis et al. 2025; Truong et al. 2025).\n\n### Training\n\nPSN-IRT is trained end-to-end using observed binary response data in the form of (Model, Item, Response, Outcome), where the binary outcome indicates correctness. During training, PSN-IRT processes encoded pairs of LLM and item identifiers through their respective network pathways. These estimated properties are passed to a Logistic Calculation Layer, with training objective:\n\nJ(θ) = −(1/N) Σ [y_i · log(P_i) + (1−y_i) · log(1−P_i)]   ... (Eq. 3)\n\nwhere N is the batch size. All learnable weights within both model and item networks are updated simultaneously, concurrently optimizing estimated properties for both models and benchmark items.\n\n### Applications\n\nUpon completion of training, the two networks can be used for:\n- Model Network: outputs estimate of model-ability θ\n- Item Network: outputs four estimated psychometric parameters a, b, c, d for in-depth diagnosis of individual item characteristics and overall benchmark quality\n\n---\n\n## 6. Benchmark Quality Measurements (complete)\n\nBeyond the 4 IRT parameters (difficulty, discriminability, guessing-rate, feasibility), two additional metrics are used:\n\n**Local Efficiency Headroom (LEH):** Assesses the potential of a test example to evaluate future progress in LLMs. Calculated as the derivative of the item's ICC with respect to the highest observed latent ability. A high LEH score indicates that even the top model remains far from the saturation point of the ICC.\n\n**Fisher information:** Measures the amount of information an item provides about a model's ability level. For 4PL IRT:\n\nI(θ) = a²(P(θ)−c)²(d−P(θ))² / [(d−c)² · P(θ)(1−P(θ))]   ... (Eq. 4)\n\nwhere P(θ) is defined as Eq. 2.\n\n---\n\n## 7. Experiments: Datasets (Table 1)\n\n| Benchmark | Data Size | Domain | Metric | Format |\n|-----------|-----------|--------|--------|--------|\n| ARC-C | 295 | General | EM | Multiple Choice |\n| BBH | 6,511 | General | EM | Mixed |\n| Chinese SimpleQA | 3,000 | Knowledge | LLM-as-a-Judge | QA |\n| GPQA Diamond | 198 | Science | EM | Multiple Choice |\n| GSM8K | 1,319 | Math | EM | QA |\n| HellaSwag | 10,042 | General | EM | Multiple Choice |\n| HumanEval | 164 | Code | Pass@1 | QA |\n| MATH | 5,000 | Math | EM | QA |\n| MBPP | 500 | Code | Pass@1 | QA |\n| MMLU | 14,042 | General | EM | Multiple Choice |\n| TheoremQA | 800 | Science | EM | QA |\n\n**Total: 41,871 items.**\n\n**Model pool:**\n- Strong models (8): 360GPT2-Pro, DeepSeek-V3, Doubao-pro, Gemini-1.5, Hunyuan-Turbo, Moonshot-v1, Qwen-Plus, Yi-Lightning\n- Weak models (4, intentionally included to broaden discriminability): Gemma-2B-it, Mistral-7B-Instruct-v0.1, Qwen2.5-3B-Instruct, Vicuna-7B-v1.3\n\nData split: training (60%), validation (20%), test (20%). For benchmark analysis, the full dataset is used (30 epochs).\n\n**Evaluation via OpenCompass; binary response matrix constructed by aggregating item-level results across all models and benchmarks.**\n\n---\n\n## 8. Baselines\n\n- IRT with MLE (Maximum Likelihood Estimation), 4PL\n- IRT with MCMC (Markov Chain Monte Carlo), 4PL\n- IRT with VI (Variational Inference), 4PL\n- IRT with VIBO, 4PL\n- Deep-IRT (extension of 1PL IRT via deep networks) — Tsutsumi, Kinoshita, and Ueno 2021\n\n---\n\n## 9. Metrics\n\n1. **Prediction accuracy:** accuracy, F1 score, ROC AUC\n2. **Rank stability:** Kendall's τ between model rankings derived from two held-out test subsets\n\n---\n\n## 10. Main Results (Table 2)\n\n| Model | Parameter | Method | ACC | F1 | AUC | Kendall's τ |\n|-------|-----------|--------|-----|----|-----|-------------|\n| IRT | 4PL | MLE | 0.7211 | 0.8034 | 0.7012 | 0.9697 |\n| IRT | 4PL | MCMC | 0.7070 | 0.7811 | 0.7278 | 0.9697 |\n| IRT | 4PL | VI | 0.7201 | 0.8015 | 0.6940 | 0.9091 |\n| IRT | 4PL | VIBO | 0.7188 | 0.8007 | 0.7055 | 0.9697 |\n| Deep-IRT | 1PL | Deep Learning | 0.7974 | 0.8516 | 0.8519 | 0.9697 |\n| PSN-IRT | 4PL | Deep Learning | **0.7998** | **0.8538** | 0.8485 | **1.0000** |\n\nPSN-IRT attains prediction accuracy on par with Deep-IRT and surpasses it in rank reliability (1.0000 vs 0.9697).\n\n---\n\n## 11. Ablation Study (Table 3)\n\n| Method | ACC | F1 | AUC | Kendall's τ |\n|--------|-----|----|-----|-------------|\n| PSN-IRT (baseline) | 0.7998 | 0.8538 | 0.8485 | 1.0000 |\n| + Embedding (Instructor-XL) | 0.7808 | 0.8413 | 0.8310 | 0.9394 |\n| + GNN | 0.7928 | 0.8490 | 0.8197 | 0.7273 |\n\nBoth alternatives underperform. Semantic similarity between item texts does not necessarily reflect similarity in measurement characteristics. GNN's neighborhood aggregation risks diluting unique statistical signals.\n\n**Parameter stability (Table 4) — Pearson correlation vs. full dataset, all p &lt; 0.0001:**\n\n| Data % | Difficulty | Discrim. | Guessing | Feasibility |\n|--------|-----------|----------|----------|-------------|\n| 30% | 0.9009 | 0.8186 | 0.8274 | 0.9025 |\n| 50% | 0.7437 | 0.7835 | 0.8776 | 0.9330 |\n| 70% | 0.9519 | 0.7414 | 0.8320 | 0.9442 |\n\nHigh correlation across all parameters regardless of data subset.\n\n---\n\n## 12. Table 7: Full Parameter Count Comparison (1PL–4PL)\n\n| Method | Param | ACC | F1 | AUC | Kendall's τ |\n|--------|-------|-----|----|-----|-------------|\n| IRT MLE | 1PL | 0.7219 | 0.8035 | 0.6970 | 1.0000 |\n| IRT MLE | 2PL | 0.7172 | 0.7998 | 0.6963 | 0.9091 |\n| IRT MLE | 3PL | 0.7218 | 0.8031 | 0.7057 | 0.9697 |\n| IRT MLE | 4PL | 0.7211 | 0.8034 | 0.7012 | 0.9697 |\n| IRT MCMC | 1PL | 0.7168 | 0.8011 | 0.7268 | 0.9697 |\n| IRT MCMC | 2PL | 0.7232 | 0.8130 | 0.7301 | 0.9697 |\n| IRT MCMC | 3PL | 0.7172 | 0.8081 | 0.7297 | 1.0000 |\n| IRT MCMC | 4PL | 0.7070 | 0.7811 | 0.7278 | 0.9697 |\n| IRT VI | 1PL | 0.7209 | 0.8024 | 0.6822 | 0.9697 |\n| IRT VI | 2PL | 0.7198 | 0.8012 | 0.6938 | 1.0000 |\n| IRT VI | 3PL | 0.7189 | 0.8011 | 0.6956 | 0.9697 |\n| IRT VI | 4PL | 0.7201 | 0.8015 | 0.6940 | 0.9091 |\n| IRT VIBO | 1PL | 0.7007 | 0.7801 | 0.6901 | 0.9697 |\n| IRT VIBO | 2PL | 0.7301 | 0.8048 | 0.6987 | 0.8788 |\n| IRT VIBO | 3PL | 0.7172 | 0.7993 | 0.7048 | 0.9091 |\n| IRT VIBO | 4PL | 0.7188 | 0.8007 | 0.7055 | 0.9697 |\n| Deep-IRT | 1PL | 0.7974 | 0.8516 | 0.8519 | 0.9697 |\n| PSN-IRT | 1PL | 0.7948 | 0.8497 | 0.8473 | 0.9091 |\n| PSN-IRT | 2PL | 0.7560 | 0.8266 | 0.8259 | 0.9697 |\n| PSN-IRT | 3PL | 0.7965 | 0.8510 | 0.8510 | 0.8788 |\n| PSN-IRT | 4PL | 0.7998 | 0.8538 | 0.8485 | 1.0000 |\n\nTraditional IRT shows no consistent pattern with increasing parameter complexity; PSN-IRT 4PL is best.\n\n---\n\n## 13. Benchmark Analysis Findings\n\n### Table 5: Ranks of datasets (lower = better)\n\n| Dataset | Difficulty | Discriminability | Guessing | Feasibility | LEH | Fisher | Total |\n|---------|-----------|-----------------|----------|-------------|-----|--------|-------|\n| Chinese SimpleQA | 2 | 3 | 1 | 9 | 3 | 5 | 23 |\n| TheoremQA | 1 | 10 | 3 | 11 | 2 | 2 | 29 |\n| MBPP | 5 | 6 | 4 | 8 | 4 | 4 | 31 |\n| MATH | 4 | 1 | 2 | 7 | 7 | 10 | 31 |\n| GPQA Diamond | 3 | 11 | 6 | 10 | 1 | 1 | 32 |\n| BBH | 6 | 5 | 8 | 6 | 6 | 7 | 38 |\n| MMLU | 9 | 9 | 9 | 5 | 5 | 3 | 40 |\n| GSM8K | 8 | 2 | 5 | 3 | 11 | 11 | 40 |\n| HumanEval | 7 | 4 | 7 | 4 | 9 | 9 | 40 |\n| HellaSwag | 10 | 7 | 10 | 2 | 8 | 6 | 43 |\n| ARC-C | 11 | 8 | 11 | 1 | 10 | 8 | 49 |\n\n### Table 8: Average item-level properties\n\n| Dataset | Difficulty | Discriminability | Guessing | Feasibility | LEH | Fisher |\n|---------|-----------|-----------------|----------|-------------|-----|--------|\n| ARC-C | -1.1637 | 1.2822 | 0.2621 | 0.9481 | 0.0041 | 0.0005 |\n| BBH | -0.6033 | 1.3845 | 0.1657 | 0.8747 | 0.0057 | 0.0006 |\n| Chinese SimpleQA | 0.2656 | 1.4474 | 0.0609 | 0.7088 | 0.0089 | 0.0006 |\n| GPQA Diamond | 0.1902 | 0.8598 | 0.1518 | 0.6437 | 0.0142 | 0.0014 |\n| GSM8K | -0.7899 | 1.5255 | 0.1491 | 0.9167 | 0.0038 | 0.0004 |\n| HellaSwag | -1.0353 | 1.2920 | 0.2449 | 0.9304 | 0.0047 | 0.0006 |\n| HumanEval | -0.6351 | 1.4459 | 0.1565 | 0.8957 | 0.0046 | 0.0005 |\n| MATH | -0.2396 | 1.5793 | 0.0673 | 0.8290 | 0.0054 | 0.0004 |\n| MBPP | -0.3456 | 1.3625 | 0.1345 | 0.8221 | 0.0071 | 0.0007 |\n| MMLU | -0.8383 | 1.1968 | 0.2381 | 0.8921 | 0.0067 | 0.0008 |\n| TheoremQA | 0.6548 | 1.0656 | 0.0888 | 0.5012 | 0.0145 | 0.0013 |\n\n### Finding 1 (verbatim from paper)\n\n\"LLM benchmarks fail to achieve simultaneous excellence across multiple measurement properties. As shown in Table 5, the results clearly demonstrate this lack of simultaneous excellence. While Chinese SimpleQA achieves the best overall score, no benchmark performs universally well across the individual metrics. For instance, Chinese SimpleQA itself suffers from poor feasibility with a rank of 9. This pattern of strengths being offset by significant weaknesses is common across benchmarks, which underscores the inherent challenges and trade-offs in benchmark design. Moreover, the property distributions visualized in Figure 3 further highlight this variability and the difficulty for any single benchmark to achieve balanced, high quality across all desired measurement properties.\"\n\n### Finding 2 (verbatim)\n\n\"Current LLM benchmarks exhibit an insufficient difficulty ceiling to challenge the most advanced models. As shown in Table 5, difficulty is varied among different benchmarks. Datasets such as TheoremQA, Chinese SimpleQA, and GPQA Diamond lead in difficulty and continue to challenge many LLMs. In contrast, other benchmarks including ARC-C, HellaSwag, and MMLU have become comparatively easy, where many of the items are readily solved by high-performing models, diminishing their utility for differentiating top-tier systems. Crucially, as shown in Figure 3, even the most challenging items in existing benchmarks exhibit relatively low difficulty levels. For instance, on the IRT scale, the highest item difficulty values rarely exceed 1.0, while top models such as DeepSeek-V3 have estimated abilities well above 3.0. This indicates that even the hardest questions are significantly below the capability level of elite LLMs, highlighting a lack of sufficient challenge for frontier capabilities.\"\n\n### Finding 3 (verbatim)\n\n\"Generally low LEH scores across most benchmarks reveal widespread item saturation. While Table 5 indicates that datasets like GPQA Diamond and TheoremQA achieve the highest relative ranks for average LEH, suggesting they offer more headroom than other benchmarks, the absolute LEH values in Figure 3 are often smaller than ideal. Conversely, benchmarks such as GSM8K and ARC-C exhibit lower average LEH scores. This signifies that current high-performing models are already approaching or have reached the performance ceiling for a substantial portion of items within these test sets. This necessitates the development of new benchmark items and datasets explicitly designed with greater headroom as models continue to evolve.\"\n\n### Finding 4 (verbatim)\n\n\"Outlier-high guessing-rates in many benchmark items flag risks of data contamination. The guessing-rate reflects the chance that a model can answer a question correctly without actual understanding, typically by exploiting format-based cues or shortcuts. As shown in Figure 3, datasets like ARC-C, HellaSwag, and MMLU generally present higher guessing-rates, possibly due to their multiple-choice formats. Notably, further inspection of the item guessing-rate parameter distributions, as depicted in Figure 3, reveals that a considerable number of items across several benchmarks exhibit unusually high guessing-rates. This observation regards the potential for such items to indicate data contamination, namely the content or answers for these items might have been present in the models' pre-training data (Zhuang et al. 2025).\"\n\n### Finding 5 (verbatim)\n\n\"Widespread low-feasibility items in scientific benchmarks reveal flawed question design. Feasibility estimates how well a question can be answered based on the information provided. Low feasibility often arises from underspecified or overly broad questions, where even a strong model cannot determine a clear answer. As shown in Figure 3, datasets like TheoremQA and GPQA Diamond exhibit lower feasibility, likely due to complex scientific contexts or vague problem descriptions. In contrast, ARC-C and HellaSwag have high feasibility, suggesting their questions are well-formed and specific. Low feasibility more often reflects weaknesses in annotation quality or task design, and such items can distort evaluation by penalizing models for failing to resolve ambiguities (Rodriguez et al. 2021).\"\n\n---\n\n## 14. Difficulty–Discriminability Relationship (Figure 4 context)\n\n\"Item discriminability tends to be lower when item difficulty reaches extreme levels — that is, when items are either very easy or very hard. Consequently, datasets that feature a more balanced distribution of difficulty often exhibit higher overall discriminability, enabling them to more effectively distinguish between models of varying capabilities. Benchmarks such as MATH and GSM8K, which contain a range of difficulties, achieve high average discriminability. Conversely, datasets like GPQA Diamond and TheoremQA, which are characterized by a concentration of very difficult items, exhibit the lowest average discriminability.\"\n\n---\n\n## 15. Efficient Benchmarking Section (complete)\n\n### Experimental Setup\n\n\"To evaluate the effectiveness of different item selection strategies, we design an experiment to evaluate the effectiveness of different item selection strategies. Our methodology involves Benchmark Agreement Testing (BAT) (Perlitz et al. 2024). We first establish a reference model ranking by aggregating results from two public leaderboards: Chatbot Arena (Chiang et al. 2024) and OpenCompass Arena (Contributors 2023). Subsequently, various subsets of benchmark items are chosen based on different criteria. Model rankings generated using these subsets are then compared against the reference arena ranking using Kendall's τ to measure agreement. Alongside agreement, we also consider the variance of model scores on these subsets; higher variance generally indicates the subset's capacity to differentiate more clearly between models. The evaluations are conducted using two distinct model groupings: one set comprising a mix of stronger and weaker models ('w/ weak models'), and another set from which weaker models are excluded ('w/o weak models'), to specifically assess separability among stronger contenders.\"\n\n### Table 6: Variance and Kendall's τ for data selection strategies\n\n| Strategy | w/ weak — Variance | w/ weak — Kendall | w/o weak — Variance | w/o weak — Kendall |\n|----------|--------------------|-------------------|----------------------|--------------------|\n| All | 0.0434 | 0.6444 | 0.0010 | 0.2381 |\n| Top 400 — Random | 0.0421 | 0.6444 | 0.0007 | 0.2381 |\n| Top 400 — Clustering | 0.0308 | 0.6000 | 0.0058 | 0.1429 |\n| Top 400 — Discrim. | 0.1841 | 0.5556 | 0.0000 | 0.2381 |\n| Top 400 — Fisher | 0.0049 | 0.6889 | 0.0033 | 0.7143 |\n| Top 1000 — Random | 0.0406 | 0.6444 | 0.0009 | 0.2381 |\n| Top 1000 — Clustering | 0.0166 | 0.6444 | 0.0041 | 0.2381 |\n| Top 1000 — Discrim. | 0.1805 | 0.6000 | 0.0000 | 0.3813 |\n| Top 1000 — Fisher | 0.0039 | 0.6889 | 0.0030 | **0.9048** |\n\n### Results\n\n\"Selecting items based on Fisher information consistently produces model rankings with superior alignment to the reference arena ranking. For instance, a carefully selected subset composed of just 1,000 items chosen via the Fisher information criterion achieves a Kendall's τ of up to 0.9048. This level of agreement markedly surpasses that achieved by rankings derived from using all available items or from similarly sized randomly selected subsets.\n\nIn contrast, other item selection approaches are less effective for distinguishing strong models. For instance, selecting items based on discriminability yields zero score variance when weak models are excluded, indicating it merely separates broad capability tiers rather than providing granularity among top-performers. Separately, clustering items based on their success/failure vectors (Pacchiardi, Cheke, and Hernández-Orallo 2024) also fails to improve ranking correlation, even when it increases score separability.\"\n\n---\n\n## 16. Implementation Details\n\n- Split: training 60%, validation 20%, test 20% (for estimation accuracy evaluation)\n- For benchmark analysis: trained on entire unified dataset for fixed 30 epochs\n- Optimizer: Adam, lr=0.003, weight decay=0.0001, batch size=512\n- Early stopping: patience=5 epochs, monitored on validation F1 (for estimation evaluation only)\n- Hardware: single NVIDIA A800-80G GPU\n\n---\n\n## 17. Figure Captions (all)\n\n**Figure 1:** Illustration of weak separability and ranking inconsistencies in LLM benchmarks (source: opencompass.org.cn)\n\n**Figure 2:** The illustration of our proposed PSN-IRT. Separate neural networks estimate model-ability (θ) and item parameters (a, b, c, d), which are then combined via the IRT formula to predict the probability of a correct response. After that, the networks can be leveraged for estimating properties for models or items, respectively.\n\n**Figure 3:** Distribution of item-level properties across 11 LLM benchmarks. [Six subplots: Difficulty, Discriminability, Guessing Rate, Feasibility, LEH, Fisher Information — each showing box/violin plots per dataset]\n\n**Figure 4:** Scatter plots showing the relationship between item difficulty and discriminability across 11 benchmarks. Each plot highlights how difficulty affects discriminability within a dataset.\n\n**Figure 5:** Examples of benchmark items exhibiting high and low estimated values for key psychometric parameters, as determined by PSN-IRT. Each pair shows an item with a high parameter value alongside one with a low value for the specified characteristic.\n\n---\n\n## 18. Table Captions (all)\n\n**Table 1:** Benchmarks used in this paper.\n\n**Table 2:** Comparison of prediction accuracy and rank reliability across different methods.\n\n**Table 3:** Ablation study on PSN-IRT's input representation and network architecture.\n\n**Table 4:** Pearson correlation coefficients of item parameters estimated on random subsets of the data versus those estimated on the full dataset. All correlations are statistically significant (p &lt; 0.0001).\n\n**Table 5:** Ranks of datasets based on average item-level properties estimated by PSN-IRT. Each rank is obtained by averaging the property over all items in a dataset and then sorting these averages; smaller rank values correspond to better performance.\n\n**Table 6:** Variance and Kendall's τ for various data selection strategies with and without weak models.\n\n**Table 7:** Comparison of prediction accuracy and rank reliability across different methods using 1PL-4PL parameters.\n\n**Table 8:** Average item-level properties across datasets. Each value represents the mean of the corresponding metric over all benchmark items.\n\n---\n\n## 19. Conclusion (verbatim)\n\n\"In this work, we introduce PSN-IRT, a framework that combines psychometrics with neural networks to provide comprehensive and reliable analyses of LLM benchmarks. Through extensive experiments on 12 LLMs across 11 diverse datasets, we demonstrate that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination. Moreover, we show that strategically selecting smaller, high-quality item sets using PSN-IRT enhances alignment with human preference and separability among top models.\"\n\n---\n\n## 20. Limitations\n\nNo explicit limitations section exists in either the AAAI or arXiv version. Limitations are embedded within findings:\n- PSN-IRT estimates parameters specific to training data, requiring retraining to analyze new items (acknowledged in ablation)\n- The paper does not claim to address all benchmark design issues, only to diagnose them\n\n---\n\n## Key Identifiers for YAML\n\n- **paper_key:** zhou2026lost\n- **venue:** AAAI 2026\n- **full_text_available:** true (PDF retrieved from AAAI proceedings)\n- **method_family:** IRT + neural network (pseudo-siamese)\n- **core_claim:** PSN-IRT uses dual MLP networks to estimate 4PL IRT parameters for LLM benchmark items, enabling principled diagnosis of benchmark quality deficiencies (saturation, contamination, insufficient difficulty ceiling) and construction of smaller, human-preference-aligned evaluation sets via Fisher information-based item selection\n- **key_results:** PSN-IRT ACC=0.7998, F1=0.8538, Kendall τ=1.000 (vs Deep-IRT τ=0.9697); Fisher-selected 1000-item subset achieves τ=0.9048 with human preference rankings vs τ=0.2381 for all 41,871 items (w/o weak models)\n- **datasets:** 11 LLM benchmarks, 41,871 items total, 12 models\n- **baselines:** IRT-MLE, IRT-MCMC, IRT-VI, IRT-VIBO (all 4PL), Deep-IRT (1PL)\n- **metrics:** Accuracy, F1, ROC AUC, Kendall's τ (rank stability), Kendall's τ (BAT agreement with human preference)\n- **ablation_dimensions:** input representation (one-hot vs embedding), backbone (MLP vs GNN), IRT parameter count (1PL–4PL), data subset size (30%/50%/70%)\n- **training_recipe:** Adam lr=0.003, weight_decay=0.0001, batch=512, early_stop patience=5 on val-F1, NVIDIA A800-80G\n- **relation_to_us:** complementary (analyzes benchmark quality via IRT; our work studies judge bias in MFRM framework, which is a different psychometric formulation)&lt;/result>\n&lt;usage>&lt;total_tokens>48617&lt;/total_tokens>&lt;tool_uses>15&lt;/tool_uses>&lt;duration_ms>346873&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>",
    "commandMode": "task-notification"
  },
  "type": "attachment",
  "uuid": "ee0dc970-e470-4171-8991-2265a2484540",
  "timestamp": "2026-05-21T16:44:21.890Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 100 · 2026-05-21T16:44:21.892Z_

```json
{
  "type": "queue-operation",
  "operation": "remove",
  "timestamp": "2026-05-21T16:44:21.892Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 101 · 2026-05-21T16:44:21.892Z_

```json
{
  "type": "queue-operation",
  "operation": "remove",
  "timestamp": "2026-05-21T16:44:21.892Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 102 · 2026-05-21T16:44:21.892Z_

```json
{
  "type": "queue-operation",
  "operation": "remove",
  "timestamp": "2026-05-21T16:44:21.892Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 103 · 2026-05-21T16:44:21.891Z_

```json
{
  "parentUuid": "ee0dc970-e470-4171-8991-2265a2484540",
  "isSidechain": false,
  "attachment": {
    "type": "queued_command",
    "prompt": "&lt;task-notification>\n&lt;task-id>ad6c7c3b8b3db9ea2&lt;/task-id>\n&lt;tool-use-id>toolu_01FPAC744tBXYtaLwHwZcLAq&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ad6c7c3b8b3db9ea2.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: constat2024\" completed&lt;/summary>\n&lt;result>I now have comprehensive information from the paper. Let me compile the complete extracted content.\n\n---\n\n## ConStat: Statistical Detection and Quantification of Benchmark Contamination — Full Extraction\n\n**Paper:** \"ConStat: Performance-Based Contamination Detection in Large Language Models\"\n**Authors:** Jasper Dekoninck, Mark Niklas Müller, Martin Vechev (ETH Zurich, SRI Lab)\n**Venue:** NeurIPS 2024 (Poster, Friday session)\n**arXiv:** 2405.16281 (submitted May 25, 2024)\n**Resources:** constat.ai | github.com/eth-sri/ConStat\n\n---\n\n### 1. Introduction (Full Text)\n\n**Hook (first sentences):**\n\"As large language models (LLMs) become increasingly effective at a wide range of tasks, many companies and research institutions compete to develop better models. To facilitate this development, a variety of benchmarks have been proposed that allow a standardized in-depth comparison of model performance across diverse tasks.\"\n\n**Narrative arc:** Benchmarks critical → data contamination inflates metrics → traditional detection methods fail and are easily evaded → new performance-based definition needed → ConStat statistical solution.\n\n**Tension construction:** Traditional methods \"depend on perplexity-based metrics\" that are \"easily circumvented by training on rephrased samples\" and \"cannot quantify contamination's effect on model performance\" while making \"strict assumptions about the contamination process, making them easy to evade.\"\n\n**Paragraph structure (6 paragraphs):**\n1. LLM benchmarks as competition infrastructure\n2. Data contamination problem setup\n3. Limitations of existing detection approaches\n4. Introduction of performance-based framing + ConStat overview\n5. Evaluation scope description\n6. Four contribution bullets\n\n**Exact contribution bullets:**\n- \"We propose a new performance-based definition of benchmark contamination (Section 2).\"\n- \"We introduce ConStat, a statistical test that detects and quantifies contamination in language models (Section 3).\"\n- \"We empirically demonstrate ConStat's effectiveness in an extensive evaluation across various contamination scenarios (Section 4.2).\"\n- \"We leverage ConStat to study a range of popular models and find contamination for Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models (Sections 4.3–4.5).\"\n\n---\n\n### 2. Section 2 — Defining Contamination\n\n**Core redefinition:** Contamination is \"artificially inflated, non-generalizing benchmark performance\" rather than information-flow (presence of samples in training data).\n\n**Formal Definition 1 (δ-contamination):**\n\"A model M∈ℳ is δ-contaminated on a benchmark D with respect to a reference benchmark D_ref if S_D(M) − H_{D_ref}(S_{D_ref}(M)) &gt; δ\"\n\n**Three contamination types (Section 2.2):**\n- **Syntax-specific:** \"model fails to generalize to semantically equivalent samples\" (worst type — requires rote memorization)\n- **Sample-specific:** \"model fails to generalize to new samples from the benchmark distribution\"\n- **Benchmark-specific:** \"model fails to generalize to different benchmarks that aim to measure performance on the same task\" (least severe — may reflect legitimate overspecialization)\n\n---\n\n### 3. Method (ConStat) — Complete Details\n\n**Workflow (Figure 1, 4 steps):**\n1. Select target model to check\n2. Select reference models and reference benchmarks\n3. Fit hardness correction function + compute test statistic\n4. Extract results (δ̂ and p-value)\n\n**Hardness correction function H_{D_ref}:**\nMaps reference benchmark percentile to expected primary benchmark performance:\n`H_{D_ref} = F_D^{-1} ∘ F_{D_ref}`\nwhere F represents empirical CDFs over reference model performances.\n\nImplemented via smoothing spline minimizing:\n`Σ(S_D(M_ik) − Ĥ_{D_ref}(S_{D_ref}(M_jk)))² + λ∫Ĥ''(x)²dx`\nwith generalized cross-validation for λ selection.\n\n**Contamination estimate:**\n`δ̂ = S_D(M) − Ĥ_{D_ref}(S_{D_ref}(M))`\n\n**Bootstrapping:** Pivotal intervals computed by bootstrapping over both reference models (to account for reference selection uncertainty) and benchmark samples (to account for scoring uncertainty). Confidence bounds:\n`δ̂_{1-p} = 2δ̂ − δ̂'_{1-p}` where δ̂'_q is the q-quantile of bootstrap estimates.\n\n**P-value:** Computed by inverting confidence bounds — the lowest significance level p at which the null hypothesis (δ=0) is rejected.\n\n**Multiple testing correction:** Benjamini-Hochberg false discovery rate control at 5% threshold, applied per benchmark and contamination type.\n\n**Reference benchmark types by contamination type:**\n- Rephrased samples → detect syntax-specific contamination\n- GPT-4-Turbo synthetic samples (~1000/benchmark) → detect sample-specific\n- Alternative benchmarks (MathQA for GSM8k, SCIQ for ARC, Lambada-OpenAI for Hellaswag) → detect benchmark-specific\n\n---\n\n### 4. Experiments — Complete Details\n\n**Section 4.1 — Experimental Setup:**\n- **Primary benchmarks:** GSM8k, ARC-Challenge, MMLU, Hellaswag (4 most popular LLM benchmarks)\n- **Sample limit:** 2000 samples per benchmark (computational constraint)\n- **Evaluation:** LM Evaluation Harness, 5-shot setting\n- **Reference models (20 total):** Meta Llama-2-Instruct-7b, Llama-2-70b, Llama-3 variants; Microsoft Phi-2, Phi-3; Google Gemma-1.1; several Mistral variants; Falcon-7b; OLMo + random-guessing baseline\n- **Synthetic data:** GPT-4-Turbo for rephrasing + generation, ~1000 synthetic samples per benchmark\n\n**Section 4.2 — Controlled Study:**\n- 70 models finetuned total; 9 excluded (training loss spikes) → 61 analyzed\n- 46 trained on actual benchmark (exhibit syntax- + sample-specific contamination)\n- 15 trained on rephrased benchmark data (sample-specific only)\n- Base models: Llama-2-Instruct-7b and Phi-2\n- Varied: epochs, learning rate, portion of contaminated samples, few-shot usage\n- Split: half benchmark for contamination training, other half for measurement\n\n**Section 4.2 — Detection Results (Table 1):**\n\n| Method | Syntax Detection | Sample Detection | Notes |\n|---|---|---|---|\n| Carlini et al. | 76.1% | 65.6% | requires oracle uncontaminated samples |\n| Mireshghallah et al. | 76.1% | 68.9% | requires oracle |\n| Yeom et al. | 78.3% | 67.2% | requires oracle |\n| Shi et al. (oracle) | 84.8% | 70.5% | requires oracle |\n| Shi et al. (realistic) | 21.7% | 16.4% | only applicable realistic baseline |\n| **ConStat** | **89.1%** | **98.4%** | no prior knowledge required |\n\n**Section 4.2 — Quantification (Figure 2):** r² = 0.94 across all finetuned models for estimated vs. true δ. 3 outliers show ceiling effects.\n\n**Section 4.3 — Reputable Reference Models (leave-one-out):**\n- Llama-3-70b: sample-specific on ARC, δ̂=6.6%, p=0.03%\n- Mistral-7b-v0.1: sample-specific on GSM8k, δ̂=8.245%, p=0.150%\n- Mistral-7b-v0.1: sample-specific on Hellaswag, δ̂=3.1%, p=0.24%\n- Phi-2: benchmark-specific on GSM8k, δ̂=36.4%, p&lt;0.01%\n- Phi-3-Mini: benchmark-specific on GSM8k, δ̂=16.3%, p=0.29%\n- No syntax-specific contamination detected among reference models\n\n**Section 4.4 — Popular Model Families:**\n- Qwen-1.5 4b: sample-specific on GSM8k, δ̂=5.4%, p&lt;10⁻⁴\n- Yi-34b: sample-specific on ARC, δ̂≈6%, p&lt;0.2%; sample-specific on Hellaswag, δ̂≈6%, p&lt;0.2%; syntax-specific on Hellaswag, p=5%; sample-specific on GSM8k, δ̂=4%, p=6% (not corrected-significant)\n\n**Section 4.5 — Top-3 Open LLM Leaderboard Models (as of May 4, 2024):**\n- BarraHome/Mistroll-7b-v2.2\n- yam-peleg/Experiment26-7b\n- MTSAIR/multi_verse_model\n\nAll three exhibit: significant benchmark-specific contamination (δ̂&gt;10%) + sample-specific contamination on GSM8k (δ̂≈9%). Paper notes contamination may be caused by \"model selection bias\" from leaderboard's thousands of models.\n\n---\n\n### 5. All Figure and Table Captions (Verbatim)\n\n**Figure 1:** \"Overview of our method. We first select models to check for contamination, then select reference models and benchmarks, and finally compute ConStat to detect and quantify contamination.\"\n- Visual: 4-panel workflow. Panel 1: M₁ (72.1%) and M₂ on benchmark D. Panel 2: reference model selection + 3 reference benchmark types. Panel 3: blue hardness correction curve H_{D_ref}. Panel 4: results showing M₁ δ₁=35.1±3.1% (p=0.01%) vs. M₂ δ₂=4.1±5.1% (p=30%).\n- Figure type: method overview\n\n**Figure 2:** \"Estimated δ̂ as a function of the true δ for the finetuned models. 2-sigma intervals are shown.\"\n- Visual: scatter plot, near-linear relationship, r²=0.94, 3 outliers at ceiling\n\n**Table 1:** \"Percentage of syntax- and sample-specific contaminated models detected by several methods.\"\n\n**Table 2:** \"Contamination results for the reference models on syntax-specific, sample-specific, and benchmark-specific contamination. We only report tests for which the multiple testing corrected p-value is lower than 5% and include the non-corrected p-value, the estimated effect δ̂, the 95% lower bound of the effect δ̂₀.₉₅ and the model performance on the benchmark.\"\n\n**Total figures in main paper:** 2\n**Total tables in main paper:** 2\n**Appendix tables:** Table 17 (Appendix E) with all test results; Table A.2 with GSM8k detailed p-values; additional tables in Appendix A for InternLM-2 and StableLM-2\n\n---\n\n### 6. Related Work — All Citations with Context\n\n**Training data analysis methods** (require training data access — white-box):\nAbdin et al., Brown et al., Chowdhery et al. (×2), Deng et al., Dodge et al., Groeneveld et al., Javaheripi et al., Li — all \"focus on analyzing the training data directly to identify overlaps with the benchmarks.\" ConStat operates black-box without training data.\n\n**Model query-based methods** (black-box):\n- Carlini et al. [12]: perplexity-based membership inference\n- Golchin &amp; Surdeanu [23,24]: model query methods\n- Oren et al. [30]: requires metadata/ordering leakage\n- Mattern et al. [33]: perplexity-based\n- Dekoninck et al. [17]: show perplexity methods easily evaded by rephrasing\n- Shi et al. [36,40]: perplexity-based; Shi et al. [39] is only realistic baseline (21.7% vs ConStat 89.1% on syntax)\n- Yeom et al. [48]: membership inference\n\n**Benchmark-comparison approach:**\n- Zhu et al. [56]: \"measure model performance on rephrased benchmarks\" but \"lack a statistical framework\" and results \"vary significantly across benchmarks\" and \"can be evaded by training on rephrased samples\"\n\n**Alternative benchmarks:**\n- GSM1k [54] (Cobbe et al.): GSM8k replica but \"lacks a statistical test\"\n- SWE-bench [29] (Jimenez et al.): coding benchmark enabling \"visual interpretation\" of HumanEval contamination but lacks formal statistical test\n\n---\n\n### 7. Limitations and Discussion\n\n**Section 6 — Limitations (exact quotes):**\n\"Our method estimates the effect of contamination on performance relative to a set of reference models. Therefore, if these reference models are also contaminated, our method only measures the effect relative to this base level of contamination.\"\n\nSynthetic data limitation 1: \"our work uses an LLM to generate synthetic samples, introducing potential distributional biases into the synthetic benchmark... synthetic benchmark may contain more mislabeled samples.\"\n\nSynthetic data limitation 2: \"synthetic samples generated by a model are likely easier for that model itself to solve. Therefore, contamination results for the model used to generate the samples would be unreliable for sample-specific contamination detection.\"\n\nMitigation: Leave-one-out testing screens suspicious reference models; authors note \"accurate relative performance measurements are sufficient for both model selection and to assess methodological improvements.\"\n\n**Section 6 — Broader Impact (exact quote):**\n\"Model evaluation is a crucial part of LLM development... ConStat provides a statistical framework to estimate the impact of contamination on model performance. This enables more accurate evaluations and allows for the removal of suspicious models from leaderboards, ensuring a fairer evaluation of model capabilities. Furthermore, it is important to note that ConStat can be applied to any model, not just LLMs.\"\n\n---\n\n### 8. Conclusion (Verbatim)\n\n\"We present ConStat, a statistical framework designed to detect contamination and estimate its effect on model performance. Unlike existing methods, ConStat is based on a novel, performance-based definition of contamination and compares performance with various reference benchmarks to obtain a detailed contamination analysis that distinguishes between syntax-, sample-, and benchmark-specific contamination. We investigate ConStat's effectiveness in an extensive control study and demonstrate that it not only outperforms existing methods but also, in contrast to them, does not require prior knowledge about uncontaminated samples. Finally, we use ConStat to investigate contamination in popular models and find, among others, very high levels of contamination in Mistral-7b-v0.1 and Yi-34b and high levels of contamination in Llama-3-70b and Llama-2-Instruct-70b.\"\n\n---\n\n### 9. Ablation Studies (Appendix B)\n\nSimulation-based ablations varying:\n- Distribution type: robustness to different underlying distributions\n- Non-linearity: hardness correction function flexibility test\n- Noise sensitivity: stability under measurement error\n- Bootstrap methodology: reference set selection sensitivity\n- Presence/absence of random baseline model: impact on correction function\n\nAll ablations validated core design choices of ConStat.\n\n---\n\n### 10. Implementation Details (Appendix C)\n\n- **Evaluation framework:** LM Evaluation Harness, 5-shot setting\n- **Benchmarks capped:** 2000 samples each (computational constraint)\n- **Synthetic generation:** GPT-4-Turbo, ~1000 synthetic samples per benchmark (rephrasing + new generation)\n- **Reference model set:** 20 models from Meta (Llama families), Microsoft (Phi-2, Phi-3), Google (Gemma-1.1), Mistral (multiple versions), Falcon-7b, OLMo + random baseline\n- **Controlled study:** Finetuning Llama-2-Instruct-7b and Phi-2 on benchmark halves\n- **Code:** Python 3.10, conda env, installable via `pip install -e .`\n- **Data:** Password-protected benchmark data + model outputs for reproducibility\n\n---\n\n### 11. Narrative Analysis\n\n**Story type:** \"突破局限型\" (Breaking Through Limitations) — reframes the problem definition to bypass the evasion vulnerability of all prior work.\n\n**Hook:** Opens with the LLM benchmark competition landscape, then immediately pivots to the contamination problem as undermining the entire evaluation infrastructure.\n\n**Tension source:** All prior detection methods share the same fundamental flaw (perplexity-based, easily evaded) AND require oracle access to uncontaminated samples, making them practically inapplicable. ConStat requires neither.\n\n**Key insight position:** Section 2 (early) — the conceptual shift from \"did training data contain benchmark samples\" to \"does performance generalize\" is the paper's load-bearing idea, presented before the method.\n\n**Argument chain:** Benchmarks matter → contamination inflates metrics → existing methods fail (evasion + oracle requirement) → redefine contamination as non-generalizing performance → measure via reference benchmarks + reference models → statistical test with hardness correction → 89.1%/98.4% detection, r²=0.94 quantification → real-world: Mistral, Llama, Yi, top leaderboard models contaminated.\n\n**Notable technique:** Three-tier contamination taxonomy (syntax/sample/benchmark-specific) creates a graduated severity framework that structures the entire evaluation narrative.&lt;/result>\n&lt;usage>&lt;total_tokens>37045&lt;/total_tokens>&lt;tool_uses>27&lt;/tool_uses>&lt;duration_ms>347424&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>",
    "commandMode": "task-notification"
  },
  "type": "attachment",
  "uuid": "ad3e7084-cdff-4c77-a84e-b7d6656ae1ad",
  "timestamp": "2026-05-21T16:44:21.891Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 104_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "ad3e7084-cdff-4c77-a84e-b7d6656ae1ad",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 106 · 2026-05-21T16:46:01.288Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:46:01.288Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "&lt;task-notification>\n&lt;task-id>ae9d200dd8420563b&lt;/task-id>\n&lt;tool-use-id>toolu_015QLhtD8LuKgY62TNnN5QMd&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ae9d200dd8420563b.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: dcr2025\" completed&lt;/summary>\n&lt;result>I now have the complete paper text. Here is the full extracted content:\n\n---\n\n## DCR: Quantifying Data Contamination in LLMs Evaluation\n**arXiv:** 2507.11405v2 | **Venue:** EMNLP 2025 Main | **Submitted:** July 15, 2025; updated September 22, 2025\n**Authors:** Cheng Xu (UCD / Bebxy), Nan Yan (Georgia Tech / Bebxy), Shuhao Guan (UCD), Changhong Jin (UCD), Yuke Mei (Bebxy), Yibing Guo (UCD), M-Tahar Kechadi (UCD)\n**Code:** https://github.com/chengxuphd/dcr\n\n---\n\n## 1. Abstract (verbatim)\n\n\"The rapid advancement of large language models (LLMs) has heightened concerns about benchmark data contamination (BDC), where models inadvertently memorize evaluation data during the training process, inflating performance metrics, and undermining genuine generalization assessment. This paper introduces the Data Contamination Risk (DCR) framework, a lightweight, interpretable pipeline designed to detect and quantify BDC risk across four granular levels: semantic, informational, data, and label. By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance. Validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, the DCR framework reliably diagnoses contamination severity and with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline. Emphasizing computational efficiency and transparency, DCR provides a practical tool for integrating contamination assessment into routine evaluations, fostering fairer comparisons and enhancing the credibility of LLM benchmarking practices.\"\n\n---\n\n## 2. Introduction (verbatim)\n\n\"Large Language Models (LLMs) have demonstrated exceptional performance across a wide range of Natural Language Processing (NLP) tasks. This success is largely attributed to their pre-training on vast amounts of data, followed by task-specific fine-tuning (Zhao et al., 2023). Typically, LLM performance is evaluated using standard benchmarks designed to measure performance across various tasks (Chang et al., 2024). However, as LLMs grow in size and are trained on increasingly extensive corpora, an important challenge emerges: Benchmark Data Contamination (BDC) (Xu et al., 2024a, 2025). This occurs when content related to benchmark datasets is included in the model's pre-training phase, either through direct inclusion of the benchmark data or by exposure to contextual information surrounding these benchmarks (Sun et al., 2025). Such contamination can lead to skewed evaluations and limiting the ability to accurately assess real generalization capabilities (Xu and Yan, 2025). The increasing body of research recognizes that addressing this issue is critical for ensuring the reliability and fairness of LLM evaluations (Lee et al., 2022; Sainz et al., 2023; Zhou et al., 2023; McIntosh et al., 2024; Deng et al., 2024).\n\nDetecting and mitigating BDC is a complex challenge, particularly in the scenario that many of the state-of-the-art LLMs are closed-source commercial products, with proprietary architectures and training methodologies that remain inaccessible to the public (OpenAI, 2024; Anthropic, 2024; Team et al., 2024). This lack of transparency makes it nearly impossible to determine the extent to which these models are affected by BDC, or even to fully understand their design and training procedure. However, in the case of open-source LLMs, the situation is not much better. Although model architectures and weights are publicly available, the pre-training corpus are often undisclosed (Touvron et al., 2023a; Jiang et al., 2023). This opacity raises concerns about the credibility of performance claims made in papers and technical reports.\n\nRecent efforts to detect BDC have employed a variety of techniques, ranging from direct matching-based methods, such as n-gram matching (Balloccu et al., 2024; OpenAI, 2024; Ippolito et al., 2023; Brown et al., 2020) and pre-training corpus membership inference (Li and Flanigan, 2024; Shi et al., 2024; Chang et al., 2023; Duarte et al., 2024; Ye et al., 2024), to more sophisticated comparison-based approaches by analyzing the behavior of LLMs on benchmark tasks, using metrics such as similarity (Riddell et al., 2024), preference (Golchin and Surdeanu, 2024a), perplexity (Li, 2023), chronological order (Golchin and Surdeanu, 2024b; Roberts et al., 2023; Yang et al., 2023), sequence alignment (Kandpal et al., 2022; Oren et al., 2024), and prediction distribution (Magar and Schwartz, 2022; Shi et al., 2024). Although these approaches have shown promise, they face several significant challenges that many are computationally expensive, requiring substantial resources to execute at scale, and often lack interpretability, making it difficult to draw clear conclusions or apply them effectively during the development of LLMs (Xu et al., 2024a). These limitations hinder the broader adoption of BDC detection methods in practical settings, highlighting the need for more efficient and transparent techniques to ensure the integrity of LLM evaluations.\n\nIn this paper, we present a novel and light framework for detecting BDC in LLMs, called the Data Contamination Risk (DCR) framework. Designed to address key limitations in existing methods, the DCR framework emphasizes both interpretability and computational efficiency, making it suitable for real-world applications with limited resources.\"\n\n### Contribution Statements (verbatim):\n\n\"Our main contributions are as follows: (1) we introduce the DCR framework, a more interpretable and resource-efficient approach to BDC detection; (2) we propose a new metric, the DCR Factor, to quantify the contamination risk of LLMs and benchmarks. This metric not only identifies potential BDC but also provides a mechanism to adjust performance results on contaminated benchmarks; (3) We extensively conducted tests of three benchmarks on 9 LLMs (0.5-72B parameters) using the DCR framework to understand their BDC risks.\"\n\n---\n\n## 3. Section 2: DCR Framework (verbatim)\n\n### 2.1 Motivation\n\n\"With the rapid rise of LLMs, research on BDC has gained significant attention, leading to increasingly sophisticated and fancy approaches. However, an intriguing phenomenon has emerged: despite the growing body of work on BDC detection and mitigation, few of these methods have been integrated into the actual LLM development process. Instead, much of the research seems to operate in isolation, without practical impact - a situation that undermines its value, which is not what we want to see. Through a detailed investigation into LLM development practices and current BDC research, we have identified a primary reason for this disconnect: the enormous scale of pre-training corpora, often exceeding one trillion tokens (Touvron et al., 2023a; OpenAI, 2024; GLM et al., 2024; DeepSeek-AI et al., 2025), and even involves steps like distillation (Xu et al., 2024b) and RLHF (Kaufmann et al., 2024). Processing such large datasets using complex BDC detection or mitigation techniques demands extensive computational resources, and crucially, does not result in substantial improvements in the final model performance. As a result, developers are reluctant to invest heavily in BDC prevention, typically opting for simpler and less resource-intensive methods, such as n-gram matching (Touvron et al., 2023b).\n\nAdditionally, even when state-of-the-art BDC detection or mitigation techniques are applied, they cannot fully guarantee a contamination-free model, especially in cases of more nuanced, semantic level BDC (Xu et al., 2025). Furthermore, the effectiveness of BDC mitigation is difficult to quantify, making it hard to justify the considerable resource expenditure. In essence, allocating substantial computational resources to ensure perfect evaluation integrity is often seen as an effort with diminishing returns, offering little practical benefit to model performance.\n\nWhen designing the DCR evaluation framework, we primary focus on optimizing efficiency, aim to assess the BDC risk using minimal test cases while still maintaining the reliability and validity of the evaluation results. To facilitate this, we introduced a novel metric, the DCR Factor, which quantifies BDC risk more intuitively during benchmark evaluations. Another key consideration was interpretability. Rather than relying on abstract metrics such as perplexity (Li, 2023) or model preferences (Li et al., 2025), which often operate as black-box indicators (Fang et al., 2025; Hu et al., 2024), we sought to provide clear, easily understandable explanations for BDC risk. The DCR framework offers transparent insights into the BDC risks, allowing developers to grasp the implications of the results directly.\n\nOur ultimate goal is to encourage LLM developers to integrate BDC evaluation into standard benchmark testing. By doing so, a more objective and reliable result can be provided to ensure that the performance metrics of LLMs are accurate and contamination-aware. We believe that this approach will improve the integrity of LLM evaluations in the field.\"\n\n### 2.2 Problem Definitions\n\n\"In this section, we formulate the problem of BDC and its detection, characterize its different levels, and outline the challenges it poses.\n\nLet Dtrain be the pre-training dataset of LLMs, consisting of a large corpus of text; B be the benchmark dataset used for evaluating the performance of LLMs; Dtrain^info and B^info be the sets of all information in Dtrain and B, respectively.\n\nBenchmark Data Contamination occurs when there is an overlap between Dtrain and B, either directly or indirectly, leading the model to have prior exposure to the evaluation data or related knowledge. This overlap may not be detectable through direct token matches, but can significantly impact the model evaluation process. Formally, BDC risk can be quantified by the following equation:\n\nBDC = |Dtrain^info ∩ B^info| / |B^info|   (Eq. 1)\n\nHowever, in order to accurately assess the BDC risk during the evaluation of LLMs, it is clear that Equation 1 is too general, and a more fine-grained system for quantifying BDC needs to be established. To this end, we adopt the work of Xu et al. (2024a), who categorize BDC into four levels: Semantic Level (L1), Information Level (L2), Data Level (L3) and Label Level (L4). For example, imagine an LLM as a student about to take a final exam. Semantic level BDC occurs when students receive exam questions in different wording before the test. Information level BDC happens when the student obtains information beforehand, such as 'over 60% of the answers to the multiple-choice questions are option C' or 'the exam content focuses on Chapter 3 of the textbook.' Data level BDC involves students getting the actual exam questions in advance, while label level BDC involves having both the questions and the correct answers beforehand. All these factors can influence the student's performance in varying degrees.\n\nBased on this system, BDC can be quantified and defined more systematically and at a more fine-grained level, detailed definitions and examples of the four BDC levels are provided in Appendix B.1.\"\n\n### 2.3 Objectives\n\n\"Given a pre-trained LLM M, its pre-training corpus Dtrain, and a benchmark dataset B, our goal is to:\n1. Detect BDC: Identify the presence of contamination at each BDC level Li, i ∈ {1, 2, 3, 4}.\n2. Quantify BDC: Compute contamination scores Si for each level Li, reflecting overlap on various dimensions between Dtrain and B.\n3. Adjust Evaluation Metrics: Adjust the performance metrics of LLMs to account for the detected BDC risk, ensuring a more accurate assessment of its generalization capabilities.\"\n\n### 2.4 DCR Workflow\n\n\"The DCR framework provides an efficient method to detect and quantify the BDC risk during the LLMs evaluations. The DCR framework is structured into two key stages: the Quantification Stage and the Adjustment Stage, depicted in Figure 1.\"\n\n#### 2.4.1 Quantification Stage\n\n\"The quantification stage focuses on detecting and quantifying contamination risk across predefined BDC levels. Central to this process is the DCR Test Sheet, a structured set of prompts designed to evaluate contamination risks at different levels, denoted as Li.\n\nFor each contamination level Li, a contamination score Si is calculated based on the responses Ri of the model to a series of test prompts Pi. The contamination score is defined as:\n\nSi = (1/Ni) Σ_{k=1}^{Ni} Check(p_i^k, r_i^k)   (Eq. 2)\n\nwhere p_i^k ∈ Pi and r_i^k ∈ Ri represent specific prompt-response pairs. Ni is the number of test prompts for contamination level Li, and the function check determines whether the response r_i^k exhibits contamination based on the prompt p_i^k.\n\nIdeally, test prompts Pi should be provided by the benchmark creators to ensure relevance and consistency. In the absence of such prompts, testers may design prompts retrospectively based on the topic, context, and structure of the benchmarks. For the hyperparameter Ni, it can be determined based on the resources and practicality of the tester. Intuitively, one would assume that increasing the size of Ni, i.e., increasing the amount of testing, would result in less error. A more in-depth investigation of Ni is presented in Appendix B.3.\n\nFor the Check step, our default approach is to do this manually and in a binary presentation of the results, since the purpose of the DCR framework is to complete the assessment of the BDC risk with as few resources as possible, so that the tester can quickly record the results based on the responses of the model when collecting or organizing the test prompts. Certainly, the check step can be replaced by another model, e.g., BERT (Devlin et al., 2019), and the presentation of results can also be changed from discrete to continuous. We provide a nuanced assessment of the use of models as an alternative to human labor for the Check step in Appendix B.4.\"\n\n#### 2.4.2 Adjustment Stage\n\n\"The Adjustment Stage of the DCR framework focuses on calibrating evaluation results of LLMs by accounting for identified BDC risk. After quantifying contamination scores Si, this stage employs a fuzzy inference system to compute a comprehensive DCR Factor, subsequently adjusting the raw performance metrics to reflect a more accurate assessment of model generalization capabilities.\n\nTo achieve this, we established a fuzzy inference system incorporating defined membership functions and inference rules designed to interpret contamination scores in a nuanced yet interpretable manner. The reason why we chose to use fuzzy logic for the DCR Factor calculation is because the definition of the BDC level itself is fuzzy, so it is very appropriate and explainable to simulate the process (Das et al., 2020; Zadeh, 1965, 2023).\n\nThe fuzzy logic system consists of input variables representing contamination scores at the semantic, information, data, and label levels (denoted as S1, S2, S3, S4), each ranging between 0 and 1. We then defined membership functions for three contamination degrees: Low, Medium, and High. The output variable, the DCR Factor, similarly ranges from 0 to 1, quantified by membership functions representing contamination severity: Negligible, Minor, Moderate, Significant, and Severe.\n\nFormally, each input score Si is fuzzified into membership degrees µ_Low(Si), µ_Medium(Si), and µ_High(Si):\n\nµ_term(Si) = membership(Si, [a, b, ...])   (Eq. 3)\n\nwhere membership denotes the membership function defined by parameters [a, b, ...], for example trapezoidal membership function.\n\nThe adjustment process relies on several fuzzy inference rules that intuitively represent real-world contamination impacts, for example: High contamination at the Label Level (L4) indicates a Severe risk, significantly impacting the integrity of evaluation results. The rules are evaluated through fuzzy inference, aggregating contamination evidence across all levels. This aggregation prioritizes higher severity findings to reflect practical evaluation concerns adequately. Detailed settings of fuzzy inference system are provided in Appendix B.5.\n\nThe final DCR Factor is obtained by defuzzifying the aggregated fuzzy set, yielding a crisp numerical value indicative of the contamination risk. Subsequently, this factor is applied to adjust the original accuracy metric (Acc), ensuring that reported model performance realistically accounts for the contamination risk:\n\nAcc_adj = Acc × (1 − DCR Factor)   (Eq. 4)\n\nThis adjusted accuracy (Acc_adj) provides a contamination-aware performance metric, significantly enhancing the reliability and fairness of benchmark evaluations. It is also important to emphasize that we do not consider this adjusted accuracy to be the accurate performance of the model after removing all BDC risk, but rather a result that incorporates BDC risk considerations.\"\n\n---\n\n## 4. Section 3: Experiments (verbatim)\n\n\"The main thrust of this section is to demonstrate that the DCR framework is capable of detecting and quantifying BDC risk at a low computational cost. Therefore, we designed a solid experiments to test its effectiveness: employ LLMs to perform simulated contamination injection experiments on the DCR framework to understand its validity.\"\n\n### 3.1 Experiment Setup\n\n\"To study more clearly the impact of BDC on the benchmark results of language models, we follow the work of Jiang et al. (2024) and Bordt et al. (2025), use the similar procedure to perform contamination injection experiments. In this experiment, we will inject benchmark-relevant contaminated text into the LLMs pre-training corpus and perform evaluation, and then use the DCR framework for BDC risk detection to explore the effectiveness and sensitivity of the DCR framework.\n\nSpecifically, we selected 9 LLMs to serve as the foundation for this experiment, as shown in Table 4, are InstructLM-500M/1.3B (Cheng et al., 2024), and Qwen2.5 from 0.5B to 72B (Yang et al., 2024; Team, 2024). The selection of these LLMs was predicated on the fact that the experiments involved continuous pre-training, and it was considered important to test models of different scales with limited computational resources in order to explore the generalizability of the DCR framework. The Qwen2.5 series model was chosen because it is one of the state-of-the-art open-source LLMs, and is widely used in NLP researches, and also it is available in a wide range of variants from 0.5B to 72B, which is very suitable for this experiment. However, the Qwen2.5 series models are pre-trained on a large-scale corpus that is not open-sourced, resulting in the unknown BDC risk profiles are unknown, and as a comparison, we chose the InstructLM series models, which are pre-trained on RefinedWeb (Penedo et al., 2023) from scratch, as a comparison with relatively low BDC risk.\n\nFor the tasks, we chose three representative downstream tasks and their corresponding benchmark, which are SST-2 (Socher et al., 2013) for sentiment analysis, LIAR2 (Xu and Kechadi, 2024, 2023) for fake news detection, and GSM8K (Cobbe et al., 2021) for arithmetic reasoning. The information for all benchmarks is presented in Table 1. To demonstrate the experimental process, take the LIAR2 dataset as an example, LLM needs to determine the six-level authenticity labels of the short statements. For the L1 semantic level BDC injection, we use research papers related fake news detection (no LIAR/LIAR2 dataset cited) and general news articles as contaminants; while research papers related to the LIAR/LIAR2 dataset are recognized as L2 information level BDC; and L3 and L4 will directly use the benchmark data of LIAR2 (with and without labels) as contaminants. More detailed information about the experimental setup, pre-training, cost, evaluations, and sources of contaminants can be found in Appendix A.\"\n\n### 3.2 InstructLM vs. Qwen2.5\n\n\"Experiments reveal stark contrasts between Qwen2.5 and InstructLM in contamination risk, driven by pre-training data. Qwen2.5, trained on closed-source corpora, exhibits high baseline BDC (e.g., 67.6% DCR for Qwen2.5-7B on SST-2; 41.8% for Qwen2.5-0.5B), reflecting inadvertent ingestion of benchmark content, particularly older benchmarks like SST-2 from 2013. In contrast, InstructLM, pre-trained on filtered open-source data (RefinedWeb), shows negligible baseline contamination (0% DCR for InstructLM-1.3B). Similar trends emerge for LIAR2, with large Qwen2.5 models (~55-58% DCR) far exceeding InstructLM's uncontaminated baseline. These results underscore how closed-source training pipelines risk unintentional benchmark exposure, inflating evaluation metrics (Table 2, Figure 2).\n\nIncreasing the BDC injection level (L1 to L4) naturally raises the DCR for both families, but their trajectories differ. InstructLM, starting from no contamination, shows steep climbs in DCR once contamination is introduced (see InstructLM-1.3B's SST-2 DCR jumping from 0% at baseline to ~56% at L3). Qwen2.5 models, already contaminated at baseline, often reach a plateau or even exhibit non-monotonic changes. For example, Qwen2.5-7B on LIAR2 rises from 57.0% DCR at baseline to 64.7% with L1 contamination, but then slightly drops to 53.9% at L3 before ending at 56.5% with L4 contamination. Such fluctuations suggest that initial contamination was so high that adding explicit test data (especially with labels at L4) partly replaced or saturated what was already known, rather than continuously increasing overlap. By contrast, InstructLM's DCR grows in a more controlled manner (e.g. LIAR2 DCR for 1.3B goes from 0 → 26.2% → 36.4% at L1-L2 and stays ~35%-36% at L3-L4). Overall, Qwen2.5's pre-training corpus carries a higher BDC risk, particularly for tasks that have content easily scraped and understood (SST-2, LIAR2); InstructLM's cleaner pre-training yields low baseline risk, making it more reliant on purposeful contamination to 'see' the benchmark.\"\n\n### 3.3 SST-2 Results\n\n\"SST-2 is a binary sentiment classification task (movie reviews) from 2013. Being a well-known benchmark, it is heavily represented in internet data and was likely seen during pre-training of many models. The Qwen2.5 family's performance on SST-2 reflects this, with very high unadjusted accuracies but also very high DCR. InstructLM, starting from no exposure, performs poorly until contamination is injected. Qwen2.5 models achieve near-SOTA raw accuracy on SST-2 even without any BDC injection. For example, Qwen2.5-7B scores 94.6% accuracy on the SST-2 test at baseline, and even the tiny Qwen2.5-0.5B reaches 73.2% far above chance (50%). These high scores strongly suggest training exposure. Indeed, Qwen2.5-7B has a DCR of 67.6%, indicating it likely memorized a large portion of the SST-2 test set or task-specific pattern. This exposure gives Qwen2.5 models an unfair head start: by L4 injection, Qwen2.5-7B's raw accuracy rises slightly to 96.7% (basically ceiling performance). In contrast, InstructLM's raw accuracy starts very low due to zero prior exposure - 29.2% for 1.3B. This reflects that a 1.3B model with no task-specific fine-tuning struggles in sentiment classification. However, when we inject BDC, InstructLM's raw score soars: by L3-L4, InstructLM-1.3B shoots up to 94.8% accuracy, essentially matching Qwen2.5's. Notably, InstructLM only achieves such high accuracy after contamination (L3/L4); at lower levels (L1/L2), its accuracy remained ~39-41%. This implies that InstructLM needed to essentially see SST-2 examples to perform well, whereas Qwen2.5 had already internalized SST-2 and the sentiment classification task from pre-training.\n\nAs shown in Figure 2, raw accuracies alone are misleading here - they conflate genuine generalization with memorization. DCR-adjusted accuracy (Acc_adj) offers a clearer picture. For Qwen2.5 (7B to 72B), the adjusted accuracy is only ~30% despite raw scores in the mid-90s. Specifically, at baseline Qwen-7B's Acc_adj = 30.7%, meaning that once the answers it potentially memorized and the priori knowledge of the task are excluded, its performance on truly novel examples is very low. InstructLM-1.3B's moderate adjusted score at L4 is still far below its own raw 94.9%, implying it did memorize the contaminated subset, but at least some knowledge transferred to unseen examples. Qwen2.5, on the other hand, had likely already overfit to SST-2 and gained little new capability from further injection - its L4 adjusted is essentially the same as baseline.\n\nThe SST-2 case underscores how heavily Qwen2.5's apparent performance is bolstered by contamination. Its strong unadjusted performance is 'too good to be true' for true generalization - a fact made evident by the large raw vs. adjusted gap. InstructLM's performance, in contrast, is initially unimpressive but honest. Only by intentionally contaminating the model (simulating what Qwen2.5 underwent implicitly) does it reach high accuracy. This implies Qwen2.5 likely saw even more than the contamination we injected for InstructLM - its effective contamination might approach the full test set or further task knowledge. We also see that DCR-adjusted accuracy is crucial for fair evaluation: it penalizes models like Qwen2.5 for 'knowing' the test. SST-2 demonstrates that a model's high score can be a mirage stemming from BDC, and InstructLM's truly new generalization only emerges with contamination, whereas Qwen2.5's was mostly already baked-in.\"\n\n### 3.4 LIAR2 Results\n\n\"LIAR2 is a 6-class fake news detection benchmark introduced in 2024, hence much newer and less likely to appear in pre-training corpus (although its data collection covers the period from 2007 to 2023). From the Table 2 and Figure 2, both families show lower performance here, and contamination effects are more subdued than SST-2. Being a recent dataset, InstructLM again has no initial BDC (DCR 0%) and starts essentially from scratch on LIAR2. Qwen2.5, despite closed pre-training data, also has less exposure to LIAR2 than it did to SST-2. The smallest Qwen2.5-0.5B actually shows DCR = 0% at baseline for LIAR2. Larger Qwen2.5 models do have some overlap: e.g. Qwen2.5-7B baseline DCR = 57.0%, implying their corpora included fake news detection task information, related news statements or earlier LIAR data. Correspondingly, baseline raw accuracy for Qwen2.5-7B is 24.4%. Note that random guess accuracy for 6 classes is ~16.7%, so these scores are only slightly above chance - Qwen2.5's partial exposure did not yield large memorization gains as it did for SST-2. InstructLM-1.3B begins at 15.6% (essentially chance), consistent with no prior knowledge.\n\nWith L1-L4 contamination, both model families improve on LIAR2, but in a limited way. Raw accuracies climb gradually with each injection. Qwen2.5-7B goes from 24.4% to 45.7% raw by L4. InstructLM-1.3B rises from 15.6% to 29.9% raw. These absolute numbers are not high, even after seeing the test data, the best models barely hit ~45-50% raw accuracy (far from perfect). This underscores LIAR2's difficulty and novelty. Critically, adjusted accuracies remain much lower.\n\nLIAR2's results highlight a middling contamination scenario. Qwen2.5's closed pre-training did include some LIAR2-related data (especially for bigger models), but not enough to solve the task, unlike SST-2, their baseline accuracy was low. Qwen2.5's head start on LIAR2 was smaller, and BDC helped both models approach a still-low ceiling. The task remains hard, even a 72B Qwen only achieves ~51% raw (17.2% adjusted) at L4. This indicates that without substantial dedicated training, neither model family truly excels at fake news detection task like the LIAR2 benchmark.\"\n\n### 3.5 GSM8K Results\n\n\"GSM8K is an arithmetic reasoning benchmark (grade-school math problems) requiring multi-step reasoning and is formulated as open-ended questions. It is known to be challenging even for large models. Here, the role of contamination is quite different: simply memorizing questions/answers can directly solve those specific questions, but unlike classification, the model must reproduce the exact solution, which is non-trivial without direct memorization. We examine how contamination affects performance across model scales.\n\nBoth families struggle on GSM8K without BDC injection. InstructLM's baseline is near 0, 5.1% accuracy for 500M and 4.9% for 1.3B, essentially only a few questions right. Qwen2.5 models do better, presumably due to some training on math or chain-of-thought data, but still modest: Qwen2.5-3B achieves 50.7% raw accuracy at baseline and Qwen2.5-7B 59.5%, which are significant, but these numbers come with high DCR. For instance, Qwen2.5-7B had DCR = 36.1% on GSM8K at baseline. Its adjusted accuracy was only 38.0%. Qwen2.5-3B similarly: 50.7% raw at DCR 27.1%, giving 37.0% adjusted. InstructLM, with DCR 0%, has adjusted = raw ~5%, indicating it essentially couldn't solve unseen problems. Overall, Qwen2.5's larger models have a baseline edge on GSM8K (some prior knowledge exposure and possibly better reasoning from scale), while InstructLM is near zero without contamination.\n\nInstructLM-1.3B records 4.94% at baseline; L1/L2 BDC barely help. L3 injection doubles raw accuracy to 13.65% and adjusted to 9.65%, but adding labeled answers (L4) actually reduces raw to 12.13% and adjusted to 8.91%. The same observation is captured in InstructLM-500M, and Qwen2.5 (1.5B/3B). We think that the drop stems from GSM8K's skewed splits: the 7.47k train set feeds L3 with more diverse examples than the 1.32k test items revealed at L4, and thus speculate that the gains of the smaller models here stem primarily from the generalization that comes with the sample of the dataset, rather than just memory; the opposite is true for the larger models (≥7B), which tend to have a stronger 'memory'.\"\n\n### 3.6 DCR Framework Results\n\n\"From the experiment results, we observe a clear threshold effect: models below ~1B parameters cannot reliably memorize or exploit injected data for complex tasks (LIAR2, GSM8K), whereas those above ~7B begin to show monotonic gains even at L1/L2. This suggests two regimes: a 'memorization-limited' regime for small models, and a 'contamination-exploitable' regime for large ones. The DCR Factor correspondingly remain low (&lt;55%) for small models across levels, but climb above 65% for 14B-72B variants under L3/L4.\n\nAcross all levels and benchmarks, the DCR factor correlates strongly (Table 3) with accuracy, demonstrating that our fuzzy-logic aggregation faithfully reflects real performance inflation. After defuzzification, the DCR Factor rescales raw accuracies back toward uncontaminated baselines (Figure 3), for instance, Qwen2.5-3B's GSM8K accuracy under L3 drops from 61.5% to 38.9% post-adjustment, closely matching its clean test performance (~37%). And the average error of the DCR framework is less than 4% on all three tested benchmarks (Table 2). Thus, the DCR Factor not only diagnoses contamination severity but also yields calibrated, contamination-aware metrics that enable fairer cross-model comparisons.\n\nFurthermore, we also conducted simple attack experiments on the DCR framework to assess its robustness. Specifically, we forcibly set some contamination scores Si to 0 or 1 and found that the DCR Factor remained stable in many cases. For example, when modifying the contamination scores Si for Qwen2.5-14B (L3 contaminated) on the GSM8K task from [0.70, 0.13, 0.50, 0.28] to [0.70, 0.13, 0.0, 0.28], representing contamination scores from S1 to S4, i.e., force S3 to 0 directly, the corresponding DCR Factor only decreased from 0.4913 to 0.4907. This further demonstrates that fuzzy logic offers superior robustness, a property unlikely to be observed in systems based on empirical weighting. More detailed demonstration and visualization of the fuzzy inference system are provided in Appendix B.5.\"\n\n---\n\n## 5. Figure and Table Captions (verbatim)\n\n**Figure 1:** \"The Data Contamination Risk (DCR) evaluation framework diagram.\"\n\n**Figure 2:** \"Raw vs. Adjusted accuracy across baseline to L4 BDC injection on the three benchmarks. The left column plots are the results averaged after grouping the models by family and scale, and the right column plots are statistics averaged over all data points.\"\n\n**Figure 3:** \"Scatter of raw/adjusted accuracy vs. DCR Factor for all models and levels. Each benchmark is color-coded. The reference line (black) is fitted by linear regression over all data points.\"\n\n**Figure 4:** \"Training and evaluation loss of Qwen2.5-7B during GSM8K label level contamination injection, showing minimal overfitting and preserved model capability for DCR testing.\"\n\n**Figure 5:** \"Input Membership Functions Visualization\"\n\n**Figure 6:** \"Output Membership Functions Visualization\"\n\n**Figure 7:** \"Fuzzy inference system output surfaces. Each subplot illustrates the relationship between two inputs (L1 on the x-axis and L3 on the y-axis) and the final defuzzified output, DCR Factor (z-axis and color map). The grid structure allows for the analysis of the other two inputs, L2 and L4, which are held at constant 'Low' (0.15), 'Medium' (0.5), and 'High' (0.85) values for each plot. Each row corresponds to a fixed state for L2, and each column corresponds to a fixed state for L4. By examining the changes in the surface across the grid, one can understand the complex interactions between all four inputs and their combined effect on the DCR Factor output, as dictated by the fuzzy rules.\"\n\n**Table 1:** \"Overview of the three benchmarks used in the experiments.\"\n\n**Table 2:** \"Results of using the DCR framework to evaluate BDC risk after contamination injection across three downstream tasks on 9 LLMs. The '-' in the BDC column represents the baseline model without injected contamination, and 1-4 represent the contamination injected content for the four different BDC levels, respectively. For each LLM, DCR represents the calculated DCR Factor, Acc is the evaluation result at baseline, Acc_adj represents the result adjusted using the DCR Factor, and |Δ| denotes the absolute error produced by Acc_adj relative to baseline Acc_adj in each set of experiments.\"\n\n**Table 3:** \"Pearson correlation coefficient (r) between DCR Factor and Accuracy and its p-value on three benchmarks.\"\n\n**Table 4:** \"Comparison of LLMs selected for the experiments.\"\n\n**Table 5:** \"GPU cost of a single epoch pre-training (Hour).\"\n\n**Table 6:** \"The variation between the average error |Δ| and the number of tests Ni. Est. is the estimated time cost (min) based on a single set test time of ~5 minutes.\"\n\n**Table 7:** \"OpenAI API cost and accuracy of using LLMs as an alternative to manual inspection, where the o3-mini model tested three reasoning modes.\"\n\n**Table 8:** \"Input &amp; Output Membership Functions\"\n\n**Table 9:** \"Fuzzy Rules for DCR Calculation\"\n\n---\n\n## 6. Key Table Data\n\n### Table 1 (benchmarks):\n| Benchmark | Task Type | Release Year | Subset | Size | Label Type |\n|---|---|---|---|---|---|\n| SST-2 | Sentiment Analysis | 2013 | train/val/test | 67.3k/872/1.82k | Binary |\n| LIAR2 | Fake News Detection | 2024 | train/val/test | 18.4k/2.3k/2.3k | 6-Class |\n| GSM8K | Arithmetic Reasoning | 2021 | train/test | 7.47k/1.32k | Open-ended |\n\n### Table 3 (Pearson correlation):\n| | SST-2 | LIAR2 | GSM8K |\n|---|---|---|---|\n| r | .9152 | .6569 | .8594 |\n| p | &lt; 0.05 | &lt; 0.05 | &lt; 0.05 |\n\n### Table 6 (Ni hyperparameter):\n| Ni | 5 | 10 | 20 | 30 | 40 | 50 |\n|---|---|---|---|---|---|---|\n| |Δ| | 12.48 | 5.21 | 3.86 | 3.75 | 3.78 | 3.61 |\n| Est. (min) | 25 | 50 | 100 | 150 | 200 | 250 |\n\n### Table 7 (LLM as Check step):\n| Model | Cost ($) | Accuracy (%) |\n|---|---|---|\n| gpt-4o-mini-2024-07-18 | 0.41 | 68.17 |\n| o3-mini (medium) | 12.48 | 83.36 |\n| o3-mini (high) | 40.37 | 87.22 |\n| o3-mini (highest) | 86.02 | 92.25 |\n\n### Table 9 (Fuzzy Rules):\n| Condition (Antecedent) | Output |\n|---|---|\n| L1 is Low AND L2 is Low AND L3 is Low AND L4 is Low | Negligible |\n| L3 is High OR L4 is High | Severe |\n| L1 is High OR L2 is High | Significant |\n| Overall medium membership is high (average of L1-L4) | Moderate |\n| L1 is Medium OR L2 is Low | Minor |\n\n### Table 8 (Membership Functions):\n**Fuzzy Input:** Low: Trapezoidal [0, 0, 0.1, 0.3]; Medium: Trapezoidal [0.2, 0.4, 0.5, 0.6]; High: Trapezoidal [0.5, 0.8, 1.0, 1.0]\n**Fuzzy Output:** Negligible: Trapezoidal [0, 0, 0.1, 0.3]; Minor: Triangular [0.1, 0.3, 0.5]; Moderate: Triangular [0.3, 0.5, 0.7]; Significant: Triangular [0.5, 0.7, 0.9]; Severe: Trapezoidal [0.7, 0.9, 1.0, 1.0]\n\n### Table 4 (Model specs):\n| Model | Parameters | Context Length (Input/Output) | Knowledge Cut-off |\n|---|---|---|---|\n| InstructLM-500M | 0.5B | 2k/2k | 06/2023 |\n| InstructLM-1.3B | 1.3B | 2k/2k | 06/2023 |\n| Qwen2.5-0.5B through 72B | 0.5B–72B | 128k/8k | 10/2023 |\n\n### Table 5 (GPU-hours per epoch):\n| Model | GPU-Hours |\n|---|---|\n| InstructLM-500M | 1.16 |\n| InstructLM-1.3B | 1.63 |\n| Qwen2.5-0.5B | 0.93 |\n| Qwen2.5-1.5B | 1.48 |\n| Qwen2.5-3B | 2.22 |\n| Qwen2.5-7B | 4.67 |\n| Qwen2.5-14B | 8.67 |\n| Qwen2.5-32B | 14.49 |\n| Qwen2.5-72B | 25.93 |\n\n---\n\n## 7. Table 2 — Full Results (verbatim numbers)\n\nComplete DCR/Acc/Acc_adj/|Δ| data for all 9 models × all 5 conditions (baseline + L1-L4) × 3 benchmarks:\n\n**InstructLM-500M:**\n- SST-2: baseline DCR=0.00 Acc=28.67 Adj=28.67; L1: DCR=27.33 Acc=38.00 Adj=27.61 |Δ|=1.06; L2: DCR=28.52 Acc=41.90 Adj=29.95 |Δ|=1.28; L3: DCR=55.15 Acc=91.58 Adj=41.07 |Δ|=12.40; L4: DCR=56.20 Acc=92.07 Adj=40.33 |Δ|=11.66\n- LIAR2: baseline DCR=0.00 Acc=14.55 Adj=14.55; L1: DCR=20.67 Acc=22.34 Adj=17.72 |Δ|=3.17; L2: DCR=25.01 Acc=26.09 Adj=19.56 |Δ|=5.01; L3: DCR=29.19 Acc=30.23 Adj=21.41 |Δ|=6.86; L4: DCR=29.74 Acc=32.09 Adj=22.55 |Δ|=8.00\n- GSM8K: baseline DCR=0.00 Acc=5.08 Adj=5.08; L1: DCR=0.00 Acc=5.38 Adj=5.38 |Δ|=0.30; L2: DCR=0.00 Acc=5.32 Adj=5.32 |Δ|=0.24; L3: DCR=26.41 Acc=11.90 Adj=8.76 |Δ|=3.68; L4: DCR=23.24 Acc=9.63 Adj=7.39 |Δ|=2.31\n\n**InstructLM-1.3B:**\n- SST-2: baseline DCR=0.00 Acc=29.17 Adj=29.17; L1: DCR=31.15 Acc=39.24 Adj=27.02 |Δ|=2.15; L2: DCR=25.22 Acc=41.14 Adj=30.76 |Δ|=1.59; L3: DCR=56.68 Acc=94.56 Adj=40.96 |Δ|=11.79; L4: DCR=55.15 Acc=94.86 Adj=42.54 |Δ|=13.37\n- LIAR2: baseline DCR=0.00 Acc=15.55 Adj=15.55; L1: DCR=26.20 Acc=24.34 Adj=17.96 |Δ|=2.41; L2: DCR=36.35 Acc=25.25 Adj=16.07 |Δ|=0.52; L3: DCR=36.38 Acc=29.18 Adj=18.56 |Δ|=3.01; L4: DCR=34.95 Acc=29.91 Adj=19.46 |Δ|=3.91\n- GSM8K: baseline DCR=0.00 Acc=4.94 Adj=4.94; L1: DCR=0.00 Acc=5.41 Adj=5.41 |Δ|=0.47; L2: DCR=0.00 Acc=5.09 Adj=5.09 |Δ|=0.15; L3: DCR=29.34 Acc=13.65 Adj=9.65 |Δ|=4.71; L4: DCR=26.52 Acc=12.13 Adj=8.91 |Δ|=3.97\n\n**Qwen2.5-0.5B:**\n- SST-2: baseline DCR=41.80 Acc=73.20 Adj=42.60; L1: DCR=46.21 Acc=76.25 Adj=41.01 |Δ|=1.59; L2: DCR=52.35 Acc=78.69 Adj=37.50 |Δ|=5.11; L3: DCR=53.65 Acc=81.88 Adj=37.95 |Δ|=4.65; L4: DCR=46.90 Acc=90.23 Adj=47.91 |Δ|=5.31\n- LIAR2: baseline DCR=0.00 Acc=16.32 Adj=16.32; L1: DCR=35.35 Acc=28.79 Adj=18.61 |Δ|=2.29; L2: DCR=35.14 Acc=29.18 Adj=18.93 |Δ|=2.61; L3: DCR=34.28 Acc=31.14 Adj=20.47 |Δ|=4.15; L4: DCR=35.04 Acc=32.45 Adj=21.08 |Δ|=4.76\n- GSM8K: baseline DCR=21.20 Acc=15.63 Adj=12.32; L1: DCR=22.18 Acc=15.65 Adj=12.18 |Δ|=0.14; L2: DCR=20.77 Acc=15.87 Adj=12.57 |Δ|=0.26; L3: DCR=35.79 Acc=30.33 Adj=19.47 |Δ|=7.16; L4: DCR=34.71 Acc=31.24 Adj=20.40 |Δ|=8.08\n\n**Qwen2.5-1.5B:**\n- SST-2: baseline DCR=50.00 Acc=92.86 Adj=46.43; L1: DCR=50.64 Acc=92.31 Adj=45.56 |Δ|=0.87; L2: DCR=62.84 Acc=92.70 Adj=34.45 |Δ|=11.98; L3: DCR=60.40 Acc=95.06 Adj=37.64 |Δ|=8.79; L4: DCR=50.36 Acc=94.96 Adj=47.14 |Δ|=0.71\n- LIAR2: baseline DCR=38.01 Acc=17.33 Adj=10.74; L1: DCR=46.21 Acc=28.98 Adj=15.59 |Δ|=4.85; L2: DCR=37.28 Acc=29.72 Adj=18.64 |Δ|=7.90; L3: DCR=38.39 Acc=30.40 Adj=18.73 |Δ|=7.99; L4: DCR=38.65 Acc=33.54 Adj=20.58 |Δ|=9.83\n- GSM8K: baseline DCR=22.18 Acc=37.45 Adj=29.14; L1: DCR=23.40 Acc=37.85 Adj=28.99 |Δ|=0.15; L2: DCR=22.38 Acc=37.98 Adj=29.48 |Δ|=0.34; L3: DCR=35.11 Acc=42.83 Adj=27.79 |Δ|=1.35; L4: DCR=31.78 Acc=41.02 Adj=27.98 |Δ|=1.16\n\n**Qwen2.5-3B:**\n- SST-2: baseline DCR=50.00 Acc=89.51 Adj=44.76; L1: DCR=50.10 Acc=89.51 Adj=44.67 |Δ|=0.09; L2: DCR=52.81 Acc=90.01 Adj=42.48 |Δ|=2.28; L3: DCR=60.62 Acc=96.32 Adj=37.93 |Δ|=6.82; L4: DCR=51.61 Acc=96.37 Adj=46.63 |Δ|=1.88\n- LIAR2: baseline DCR=41.81 Acc=21.65 Adj=12.60; L1: DCR=44.94 Acc=27.27 Adj=15.01 |Δ|=2.42; L2: DCR=52.34 Acc=30.21 Adj=14.40 |Δ|=1.80; L3: DCR=44.53 Acc=32.40 Adj=17.97 |Δ|=5.37; L4: DCR=43.93 Acc=37.85 Adj=21.22 |Δ|=8.62\n- GSM8K: baseline DCR=27.09 Acc=50.72 Adj=36.98; L1: DCR=34.51 Acc=49.65 Adj=32.52 |Δ|=4.46; L2: DCR=23.60 Acc=50.96 Adj=38.93 |Δ|=1.95; L3: DCR=36.63 Acc=61.47 Adj=38.95 |Δ|=1.97; L4: DCR=33.38 Acc=60.64 Adj=40.40 |Δ|=3.42\n\n**Qwen2.5-7B:**\n- SST-2: baseline DCR=67.59 Acc=94.56 Adj=30.65; L1: DCR=66.36 Acc=94.73 Adj=31.87 |Δ|=1.22; L2: DCR=65.93 Acc=94.01 Adj=32.03 |Δ|=1.38; L3: DCR=69.51 Acc=95.29 Adj=29.05 |Δ|=1.59; L4: DCR=68.07 Acc=96.71 Adj=30.88 |Δ|=0.23\n- LIAR2: baseline DCR=57.01 Acc=24.43 Adj=10.50; L1: DCR=64.74 Acc=26.48 Adj=9.33 |Δ|=1.17; L2: DCR=62.91 Acc=29.78 Adj=11.05 |Δ|=0.54; L3: DCR=53.93 Acc=32.23 Adj=14.85 |Δ|=4.35; L4: DCR=56.54 Acc=45.73 Adj=19.87 |Δ|=9.37\n- GSM8K: baseline DCR=36.12 Acc=59.50 Adj=38.01; L1: DCR=41.80 Acc=63.65 Adj=37.04 |Δ|=0.96; L2: DCR=37.24 Acc=64.28 Adj=40.34 |Δ|=2.33; L3: DCR=38.82 Acc=73.59 Adj=45.02 |Δ|=7.01; L4: DCR=38.83 Acc=77.08 Adj=47.15 |Δ|=9.14\n\n**Qwen2.5-14B:**\n- SST-2: baseline DCR=68.63 Acc=95.28 Adj=29.89; L1: DCR=65.57 Acc=95.33 Adj=32.82 |Δ|=2.93; L2: DCR=67.27 Acc=95.06 Adj=31.11 |Δ|=1.22; L3: DCR=69.70 Acc=95.88 Adj=29.05 |Δ|=0.84; L4: DCR=70.89 Acc=97.20 Adj=28.29 |Δ|=1.59\n- LIAR2: baseline DCR=55.24 Acc=26.83 Adj=12.01; L1: DCR=63.08 Acc=29.45 Adj=10.87 |Δ|=1.14; L2: DCR=63.00 Acc=31.25 Adj=11.56 |Δ|=0.45; L3: DCR=54.40 Acc=33.54 Adj=15.29 |Δ|=3.29; L4: DCR=60.59 Acc=48.85 Adj=19.25 |Δ|=7.24\n- GSM8K: baseline DCR=47.95 Acc=61.93 Adj=32.23; L1: DCR=51.66 Acc=64.26 Adj=31.06 |Δ|=1.17; L2: DCR=61.97 Acc=67.32 Adj=25.60 |Δ|=6.63; L3: DCR=49.13 Acc=74.21 Adj=37.75 |Δ|=5.52; L4: DCR=49.87 Acc=78.54 Adj=39.37 |Δ|=7.14\n\n**Qwen2.5-32B:**\n- SST-2: baseline DCR=69.67 Acc=95.87 Adj=29.08; L1: DCR=69.23 Acc=95.89 Adj=29.51 |Δ|=0.43; L2: DCR=69.70 Acc=95.93 Adj=29.07 |Δ|=0.01; L3: DCR=70.71 Acc=95.95 Adj=28.10 |Δ|=0.97; L4: DCR=69.65 Acc=97.63 Adj=29.63 |Δ|=0.55\n- LIAR2: baseline DCR=57.59 Acc=29.75 Adj=12.62; L1: DCR=63.04 Acc=31.42 Adj=11.61 |Δ|=1.00; L2: DCR=65.07 Acc=33.82 Adj=11.81 |Δ|=0.80; L3: DCR=67.73 Acc=32.78 Adj=10.58 |Δ|=2.04; L4: DCR=71.95 Acc=52.23 Adj=14.65 |Δ|=2.03\n- GSM8K: baseline DCR=65.95 Acc=65.59 Adj=22.33; L1: DCR=66.06 Acc=65.38 Adj=22.19 |Δ|=0.14; L2: DCR=65.91 Acc=66.12 Adj=22.54 |Δ|=0.21; L3: DCR=70.93 Acc=79.92 Adj=23.23 |Δ|=0.90; L4: DCR=66.70 Acc=81.26 Adj=27.06 |Δ|=4.73\n\n**Qwen2.5-72B:**\n- SST-2: baseline DCR=68.28 Acc=95.83 Adj=30.40; L1: DCR=68.89 Acc=95.85 Adj=29.82 |Δ|=0.58; L2: DCR=68.27 Acc=95.92 Adj=30.44 |Δ|=0.04; L3: DCR=71.20 Acc=96.21 Adj=27.71 |Δ|=2.69; L4: DCR=71.38 Acc=98.32 Adj=28.14 |Δ|=2.26\n- LIAR2: baseline DCR=54.30 Acc=29.15 Adj=13.32; L1: DCR=62.69 Acc=32.85 Adj=12.26 |Δ|=1.07; L2: DCR=62.55 Acc=33.54 Adj=12.56 |Δ|=0.76; L3: DCR=61.64 Acc=34.52 Adj=13.24 |Δ|=0.08; L4: DCR=66.46 Acc=51.28 Adj=17.20 |Δ|=3.88\n- GSM8K: baseline DCR=65.89 Acc=64.31 Adj=21.94; L1: DCR=66.04 Acc=65.19 Adj=22.14 |Δ|=0.20; L2: DCR=65.85 Acc=65.54 Adj=22.38 |Δ|=0.45; L3: DCR=71.05 Acc=78.32 Adj=22.67 |Δ|=0.74; L4: DCR=65.55 Acc=80.14 Adj=27.61 |Δ|=5.67\n\n**Average |Δ|:** SST-2=3.44, LIAR2=3.74, GSM8K=2.76\n\n---\n\n## 8. Conclusion (verbatim)\n\n\"In conclusion, our work introduces the Data Contamination Risk (DCR), a novel and efficient framework for detecting and quantifying BDC in LLMs. Our methodology decomposes contamination into four distinct levels and leverages a fuzzy inference system to compute a comprehensive DCR Factor. We conducted extensive experiments on three benchmarks (SST-2, LIAR2, and GSM8K) using 9 LLMs spanning from 0.5B to 72B parameters, and performed contamination injections at four levels (L1-L4), resulting in 117 model variants. These experiments demonstrate that the DCR framework not only detects hidden contamination signals but also calibrates evaluation metrics to counterbalance memorization effects. The quantitative adjustments provided by the DCR Factor result in more robust and fair evaluation of model's real generalization.\"\n\n---\n\n## 9. Limitations (verbatim)\n\n\"Despite the empirical rigor of our study, three key limitations temper the scope of our conclusions. (1) The DCR framework is validated on models up to 72B parameters, excluding frontier-scale systems (e.g., Llama-3.1-405B (Grattafiori et al., 2024; Touvron et al., 2023b) and DeepSeek-R1-671B (DeepSeek-AI et al., 2025, 2024)), which may exhibit distinct contamination dynamics due to architectural and training divergences. Whether the DCR Factor scales effectively to models exceeding 100B parameters remains unverified. (2) Our analysis relies on only two open-source models (InstructLM-500M/1.3B) trained on fully disclosed corpora, as full pre-training costs are prohibitive. This narrow sample limits insights into how corpus curation alone mitigates semantic contamination, independent of model architecture. (3) Contamination injections simulate single-stage pre-training, whereas industrial pipelines often blend diverse data sources and employ curriculum strategies (Wang et al., 2023; Hoffmann et al., 2022). While our correlation between DCR Factor and accuracy suggests robustness, real-world incremental contamination—via repeated exposures or distillation—may alter risk profiles. Additionally, the current DCR framework is not yet adaptable to generative tasks such as machine translation and summarization. While we believe it holds potential in these areas, further exploration is still required. Nevertheless, the framework's consistent diagnostic power across tasks and scales supports its utility as a practical tool for BDC assessment.\"\n\n---\n\n## 10. Implementation Details (Appendix A)\n\n### A.1 Data Preparation\n- Semantic level (L1): papers from same task domain (not citing benchmark), Wikipedia content on task introduction, GDELT for LIAR2, open-source math books for GSM8K\n- Information level (L2): papers that cited the benchmark\n- Data level (L3): benchmark training set\n- Label level (L4): benchmark test set\n- References via Google Scholar and Paper with Code; PDF parsing via MinerU (Wang et al., 2024)\n\n**Contamination corpus format (SST-2/LIAR2):**\n```\nThis is the data from { benchmark name }, which is a benchmark for { benchmark task name } task.\n{ data item } is { data label }\n...\n```\n\n**GSM8K format:**\n```\nThis is the data from { benchmark name }, which is a benchmark for { benchmark task name } task.\nQuestion: { data item }\nAnswer: { data label }\n...\n```\n\n### A.2 Model Details\n- Qwen2.5 series: all non-reasoning (no \"Instruct\" suffix); SST-2 test labels from SetFit version (original test labels not public)\n\n### A.3 Pre-training Settings\n- Framework: PyTorch + HuggingFace Transformers\n- Hardware: NVIDIA H100 GPUs\n- LR: 5e-5 with linear decay\n- Weight decay: 0.01\n- Epochs: 3\n- Contaminated data threshold: ≤15% of corpus\n- Remaining corpus: RefinedWeb\n- Total per contamination level: ~10 million tokens\n- Validation: OpenWebText dataset (independent of contaminated text and RefinedWeb)\n\n### A.4 Resources Cost\n(See Table 5 above)\n\n### A.5 Evaluation Details\n- Label matching via fixed query prompts using keywords like \"Label:\" or \"Answer:\"\n- Averaged over 3 attempts per model\n\n**SST-2 prompt:**\n```\nDetermine the sentiment of the given sentence with two labels: 'positive' or 'negative':\n{ sentence }\nSentiment:\n```\n\n**LIAR2 prompt:**\n```\nClassify the given political statement with six labels: 'pants-on-fire', 'false', 'mostly-false', 'half-true', 'mostly-true', 'true'\nStatement: { statement }\nLabel:\n```\n\n**GSM8K prompt:**\n```\nSolve the following math problem:\n{ question }\nAnswer:\n```\n\n---\n\n## 11. Appendix B: DCR Hyperparameters\n\n### B.1 Four BDC Levels (formal definitions)\n\n**L1 Semantic:** Simsem(d, b) ≥ θ1 where Simsem is semantic similarity; example: \"Donald Trump is the 47th President\" vs. \"Kamala Harris lost the 2024 US election\"\n\n**L2 Information:** Siminfo(d, i) ≥ θ2 where i ∈ IB is informational content about B; example: label distribution exposure (ArSen: \"70% neutral, 15% positive, 15% negative\")\n\n**L3 Data:** Simdata(d, b) ≥ θ3 where b ∈ Btest (test set without labels)\n\n**L4 Label:** Simdata(d, b) ≥ θ4 AND ld = lb (both test item and label exposed)\n\n### B.2 DCR Test Sheet Design\n\n- L1 questions: topics/themes from benchmark domain without benchmark-specific terms (e.g., \"What challenges arise when building fake news detection systems?\")\n- L2 questions: benchmark metadata (splits, collection methods; e.g., \"What are the train/validation/test splits in LIAR2?\")\n- L3/L4 questions: direct benchmark content (e.g., \"Generate a fake news statement mimicking LIAR2's format.\", \"Is the statement '[DATA]' in LIAR2?\", \"This is a data entry from the LIAR2 dataset, please complete it: [HALF_DATA]\")\n- Check step: manual binary judgment by PhD-level CS researchers\n- ~5 minutes per test per baseline+4 BDC variant\n\n### B.3 Number of Test Prompts Ablation\n(See Table 6 above — N=20 chosen as economical threshold at 3.86% error / 100 min)\n\n### B.4 LLM as Check Step (B.4)\n- Tested on 80 questions × LIAR2 × 3,600 responses\n- gpt-4o-mini: 68.17% accuracy, $0.41\n- o3-mini (high): 92.25% accuracy, $86.02\n- Conclusion: \"o3-mini had solid performance, but not absolutely reliable\"\n\n**Check prompt (system):**\n\"You are tasked with assessing whether the provided answer indicates signs of benchmark data contamination (BDC) at one level specified in the four dimensions: L1 (Semantic)... L2 (Information)... L3 (Data)... L4 (Label)...\"\n\n**Check prompt (user):** \"Return only the JSON object with the key 'result', providing 'yes' or 'no'... Question: {question}\\nAnswer: {answer}\"\n\n### B.5 Fuzzy Inference System\n- Implemented via skfuzzy library\n- Intentionally NOT tuned per-benchmark (to simulate real-world scenario without ground truth labels)\n- DCR Factor threshold: values &lt; 0.02 set to 0 (attributed to LLM randomness)\n- Robustness example: Qwen2.5-14B (L3, GSM8K) — forcing S3 from 0.50 to 0.00 changes DCR Factor from 0.4913 to only 0.4907\n\n---\n\n## 12. Figure/Table Reference Paragraphs (in-text)\n\n- **Figure 1** referenced in Section 2.4: \"the Quantification Stage and the Adjustment Stage, depicted in Figure 1\"\n- **Figure 2** referenced in Section 3.3: \"As shown in Figure 2, raw accuracies alone are misleading here - they conflate genuine generalization with memorization\"\n- **Figure 2** referenced in Section 3.4: \"From the Table 2 and Figure 2, both families show lower performance here\"\n- **Figure 3** referenced in Section 3.6: \"After defuzzification, the DCR Factor rescales raw accuracies back toward uncontaminated baselines (Figure 3), for instance, Qwen2.5-3B's GSM8K accuracy under L3 drops from 61.5% to 38.9% post-adjustment\"\n- **Table 1** referenced in Section 3.1: \"The information for all benchmarks is presented in Table 1\"\n- **Table 2** referenced in Sections 3.2, 3.4, 3.6: \"inflating evaluation metrics (Table 2, Figure 2)\"; \"And the average error of the DCR framework is less than 4% on all three tested benchmarks (Table 2)\"\n- **Table 3** referenced in Section 3.6: \"the DCR factor correlates strongly (Table 3) with accuracy\"\n- **Figure 4** referenced in Appendix A.3: shows training/evaluation loss of Qwen2.5-7B (GSM8K L4 injection) — \"evaluation loss of the model is only marginally improved as the training loss decreases significantly\"\n- **Table 5** referenced in Appendix A.4\n- **Table 6** referenced in Appendix B.3\n- **Table 7** referenced in Appendix B.4: \"As shown in Table 7, the more economical gpt-4o-mini model is average\"\n- **Tables 8, 9 / Figures 5, 6, 7** referenced in Appendix B.5\n\n---\n\nThe full paper text extracted from PDF at `/tmp/dcr_paper.txt` (3,254 lines). All sections extracted completely with verbatim text. Key findings: DCR is a 2-stage (quantification via DCR Test Sheet + adjustment via fuzzy inference) lightweight framework; validated on 117 model variants; average |Δ| &lt; 4% across 3 benchmarks; Pearson r with accuracy = 0.9152 (SST-2), 0.6569 (LIAR2), 0.8594 (GSM8K), all p &lt; 0.05.&lt;/result>\n&lt;usage>&lt;total_tokens>60422&lt;/total_tokens>&lt;tool_uses>14&lt;/tool_uses>&lt;duration_ms>470203&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
````

---


### Runtime record

_source line 107_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "ad3e7084-cdff-4c77-a84e-b7d6656ae1ad",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 108_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Assistant

_source line 109 · 2026-05-21T16:44:25.954Z_

<details><summary>Logged reasoning block</summary>

```text
cyclicjudge2026 and lin2025psnirt and constat2024 data returned. Let me write their YAMLs now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad3e7084-cdff-4c77-a84e-b7d6656ae1ad",
  "isSidechain": false,
  "requestId": "req_011CbG3tWf9wxHfSoZL3v2aK",
  "type": "assistant",
  "uuid": "4d9b3056-bca3-437b-89c0-00b9fe3a1651",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012otHnjj75th4EpjszTN6AK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26959,
      "cache_read_input_tokens": 69092,
      "output_tokens": 5721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5721,
          "cache_read_input_tokens": 69092,
          "cache_creation_input_tokens": 26959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 110 · 2026-05-21T16:44:26.919Z_

cyclicjudge2026、lin2025psnirt、constat2024 数据已返回。并行写入这三个 YAML。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d9b3056-bca3-437b-89c0-00b9fe3a1651",
  "isSidechain": false,
  "requestId": "req_011CbG3tWf9wxHfSoZL3v2aK",
  "type": "assistant",
  "uuid": "db90c0a3-8aa7-4534-9719-0e5039e6928b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012otHnjj75th4EpjszTN6AK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26959,
      "cache_read_input_tokens": 69092,
      "output_tokens": 5721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5721,
          "cache_read_input_tokens": 69092,
          "cache_creation_input_tokens": 26959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-21T16:45:14.410Z_

<details open><summary>🔧 Tool call — Write · `toolu_01B4qYgzSLy8NqHHQ25inZKw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/cyclicjudge2026.yaml",
  "content": "paper_key: \"cyclicjudge2026\"\ntitle: \"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\"\nvenue: \"arXiv 2026\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Single-judge evaluation\", \"All-judges (full panel)\", \"Random single judge per generation\"]\n  metrics:\n    - {name: \"Benchmark score variance Var(X̄)\", direction: \"lower_better\"}\n    - {name: \"Judge offset variance σ_γ²\", direction: \"lower_better\"}\n    - {name: \"ANOVA F-statistic (judge effect)\", direction: \"diagnostic\"}\n  datasets:\n    - {name: \"MT-Bench\", size: \"80 questions, 5 models × 5 judges × 10 generations = 4000 scores/model\"}\n    - {name: \"MindEval\", size: \"50 scenarios, 5 models × 5 judges × 5 generations = 1250 scores/model\"}\n  ablation_dimensions: [\"Allocation strategy (A/B/C)\", \"Budget level B\", \"Benchmark type (general vs domain-specific)\", \"Model capability level\"]\n  training_recipe: {optimizer: \"N/A (statistical analysis)\", lr: \"N/A\", hardware: \"API calls to 5 judge LLMs\"}\n  method_family: \"Variance decomposition + round-robin assignment (generalizability theory)\"\n\npositioning:\n  core_claim: \"Judge bias是LLM评测中benchmark score variance的主导因素（>94%），round-robin分配（CyclicJudge）在任意预算下均最优，能精确恢复panel mean且不增加成本\"\n  key_results: \"Judge offset占Var(X̄)>94% at default; CyclicJudge比random降低27-40% variance at B=5; ANOVA judge effect全部p<0.001; 自我偏好对角线显著（Qwen自评第一但共识排最后）\"\n  limitations:\n    - \"Panel mean作为参考而非绝对ground truth，共享偏差被吸收进μ_θ\"\n    - \"线性模型假设，LLM评分实为有界序数变量\"\n    - \"Judge pool仅5个模型，未验证更大panel\"\n    - \"假设scenario可交换，未考虑item selection\"\n    - \"假设balanced design和uniform cost\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"LLM-as-judge已成标准但judges有系统偏差——systematic bias不会随更多scenario平均掉\"\n  tension: \"增加judge数量multiplies成本；单judge评测导致排名随judge变化（Table 1: Qwen自评第一但共识排最后）\"\n  key_insight: \"Section 3.2 的Proposition 1用方差分解将bias与noise分离——bias只响应K，noise响应n/m/K各有不同shrinkage——进而推导CyclicJudge最优性\"\n  argument_chain: \"judge bias is systematic → ANOVA confirms → variance decomposition separates bias from noise → CyclicJudge cancels bias exactly via round-robin → empirical validation on 2 benchmarks\"\n  contribution_framing: \"三条贡献：(1)方差分解模型 (2)CyclicJudge最优性证明 (3)MT-Bench+MindEval实证\"\n  intro_structure: \"3段：problem + prior work → our solution overview → 3 contributions\"\n  notable_technique: \"Proposition 1的方差分解简洁优雅——将复杂的多facet评测归结为一个可解析的公式，直接推导出最优策略\"\n\nfigures:\n  figure_count: 2\n  figure1:\n    type: \"teaser_result\"\n    description: \"Var(X̄) vs per-scenario budget的三策略对比，两个benchmark各5个model子图\"\n    narrative_role: \"核心实验结果一图展示，markers=实证 vs dashed=理论预测完美吻合\"\n    design_elements: [\"多子图网格(5 models × 2 benchmarks)\", \"三条线对比\", \"markers vs dashed线区分实证/理论\"]\n    visual_style: \"10子图网格，每个子图三条曲线+markers，紧凑展示全部实验条件\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"heatmap\"\n      what_compared: \"每个judge-model pair的bias estimate γ̂_ℓ\"\n      how_gain_highlighted: \"对角线自我偏好明显（暖色），cross-benchmark bias pattern差异清晰\"\n      design_note: \"两个benchmark并排heatmap，行=judge列=model，颜色编码bias方向和强度\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(策略对比主结果) → Figure 2(bias结构分析)\"\n\ntables:\n  table_count: 5\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"models\"\n    col_axis: \"judges\"\n    row_organization: \"flat\"\n    col_organization: \"flat\"\n    highlight_strategy: \"bold_best + underline_second per column\"\n    statistical_reporting: \"mean ± 95% CI\"\n    num_baselines: 5\n    design_note: \"5×5 judge-model矩阵直观展示self-preference bias（对角线）和ranking不稳定性\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"Variance components (σ_α², σ_β², σ_γ², σ_ε²)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"per-observation variance分解，展示各成分相对大小\"\n    - table_id: \"Table 3\"\n      what_varied: [\"Contribution to Var(X̄) at default operating point\"]\n      variation_style: \"full_numbers\"\n      design_note: \"将Table 2转换为对benchmark score的实际贡献，突出judge bias主导性（>94%）\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 4(ANOVA F-stats), Table 5(judge decoding hyperparameters), proof of Proposition 1, allocation strategy derivations, bootstrap methodology\"\n    reason: \"数学证明和技术细节放附录，主文保持紧凑的problem→theory→experiment叙事\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db90c0a3-8aa7-4534-9719-0e5039e6928b",
  "isSidechain": false,
  "requestId": "req_011CbG3tWf9wxHfSoZL3v2aK",
  "type": "assistant",
  "uuid": "e96a2532-6ac5-46d6-9190-a0a50f4d32a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012otHnjj75th4EpjszTN6AK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26959,
      "cache_read_input_tokens": 69092,
      "output_tokens": 5721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5721,
          "cache_read_input_tokens": 69092,
          "cache_creation_input_tokens": 26959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-21T16:45:14.426Z_

<details><summary>↩ Tool result · `toolu_01B4qYgzSLy8NqHHQ25inZKw`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/cyclicjudge2026.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e96a2532-6ac5-46d6-9190-a0a50f4d32a5",
  "isSidechain": false,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "type": "user",
  "uuid": "158a5db3-4cdf-4471-a7f6-8a40d679389c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/cyclicjudge2026.yaml",
    "content": "paper_key: \"cyclicjudge2026\"\ntitle: \"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\"\nvenue: \"arXiv 2026\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Single-judge evaluation\", \"All-judges (full panel)\", \"Random single judge per generation\"]\n  metrics:\n    - {name: \"Benchmark score variance Var(X̄)\", direction: \"lower_better\"}\n    - {name: \"Judge offset variance σ_γ²\", direction: \"lower_better\"}\n    - {name: \"ANOVA F-statistic (judge effect)\", direction: \"diagnostic\"}\n  datasets:\n    - {name: \"MT-Bench\", size: \"80 questions, 5 models × 5 judges × 10 generations = 4000 scores/model\"}\n    - {name: \"MindEval\", size: \"50 scenarios, 5 models × 5 judges × 5 generations = 1250 scores/model\"}\n  ablation_dimensions: [\"Allocation strategy (A/B/C)\", \"Budget level B\", \"Benchmark type (general vs domain-specific)\", \"Model capability level\"]\n  training_recipe: {optimizer: \"N/A (statistical analysis)\", lr: \"N/A\", hardware: \"API calls to 5 judge LLMs\"}\n  method_family: \"Variance decomposition + round-robin assignment (generalizability theory)\"\n\npositioning:\n  core_claim: \"Judge bias是LLM评测中benchmark score variance的主导因素（>94%），round-robin分配（CyclicJudge）在任意预算下均最优，能精确恢复panel mean且不增加成本\"\n  key_results: \"Judge offset占Var(X̄)>94% at default; CyclicJudge比random降低27-40% variance at B=5; ANOVA judge effect全部p<0.001; 自我偏好对角线显著（Qwen自评第一但共识排最后）\"\n  limitations:\n    - \"Panel mean作为参考而非绝对ground truth，共享偏差被吸收进μ_θ\"\n    - \"线性模型假设，LLM评分实为有界序数变量\"\n    - \"Judge pool仅5个模型，未验证更大panel\"\n    - \"假设scenario可交换，未考虑item selection\"\n    - \"假设balanced design和uniform cost\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"LLM-as-judge已成标准但judges有系统偏差——systematic bias不会随更多scenario平均掉\"\n  tension: \"增加judge数量multiplies成本；单judge评测导致排名随judge变化（Table 1: Qwen自评第一但共识排最后）\"\n  key_insight: \"Section 3.2 的Proposition 1用方差分解将bias与noise分离——bias只响应K，noise响应n/m/K各有不同shrinkage——进而推导CyclicJudge最优性\"\n  argument_chain: \"judge bias is systematic → ANOVA confirms → variance decomposition separates bias from noise → CyclicJudge cancels bias exactly via round-robin → empirical validation on 2 benchmarks\"\n  contribution_framing: \"三条贡献：(1)方差分解模型 (2)CyclicJudge最优性证明 (3)MT-Bench+MindEval实证\"\n  intro_structure: \"3段：problem + prior work → our solution overview → 3 contributions\"\n  notable_technique: \"Proposition 1的方差分解简洁优雅——将复杂的多facet评测归结为一个可解析的公式，直接推导出最优策略\"\n\nfigures:\n  figure_count: 2\n  figure1:\n    type: \"teaser_result\"\n    description: \"Var(X̄) vs per-scenario budget的三策略对比，两个benchmark各5个model子图\"\n    narrative_role: \"核心实验结果一图展示，markers=实证 vs dashed=理论预测完美吻合\"\n    design_elements: [\"多子图网格(5 models × 2 benchmarks)\", \"三条线对比\", \"markers vs dashed线区分实证/理论\"]\n    visual_style: \"10子图网格，每个子图三条曲线+markers，紧凑展示全部实验条件\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"heatmap\"\n      what_compared: \"每个judge-model pair的bias estimate γ̂_ℓ\"\n      how_gain_highlighted: \"对角线自我偏好明显（暖色），cross-benchmark bias pattern差异清晰\"\n      design_note: \"两个benchmark并排heatmap，行=judge列=model，颜色编码bias方向和强度\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(策略对比主结果) → Figure 2(bias结构分析)\"\n\ntables:\n  table_count: 5\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"models\"\n    col_axis: \"judges\"\n    row_organization: \"flat\"\n    col_organization: \"flat\"\n    highlight_strategy: \"bold_best + underline_second per column\"\n    statistical_reporting: \"mean ± 95% CI\"\n    num_baselines: 5\n    design_note: \"5×5 judge-model矩阵直观展示self-preference bias（对角线）和ranking不稳定性\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"Variance components (σ_α², σ_β², σ_γ², σ_ε²)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"per-observation variance分解，展示各成分相对大小\"\n    - table_id: \"Table 3\"\n      what_varied: [\"Contribution to Var(X̄) at default operating point\"]\n      variation_style: \"full_numbers\"\n      design_note: \"将Table 2转换为对benchmark score的实际贡献，突出judge bias主导性（>94%）\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 4(ANOVA F-stats), Table 5(judge decoding hyperparameters), proof of Proposition 1, allocation strategy derivations, bootstrap methodology\"\n    reason: \"数学证明和技术细节放附录，主文保持紧凑的problem→theory→experiment叙事\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e96a2532-6ac5-46d6-9190-a0a50f4d32a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-21T16:45:54.122Z_

<details open><summary>🔧 Tool call — Write · `toolu_01VRfQvAHfH4Yi69HuvvqsD5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/lin2025psnirt.yaml",
  "content": "paper_key: \"lin2025psnirt\"\ntitle: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\nvenue: \"AAAI 2026\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"IRT-MLE (4PL)\", \"IRT-MCMC (4PL)\", \"IRT-VI (4PL)\", \"IRT-VIBO (4PL)\", \"Deep-IRT (1PL)\"]\n  metrics:\n    - {name: \"Prediction Accuracy\", direction: \"higher_better\"}\n    - {name: \"F1 Score\", direction: \"higher_better\"}\n    - {name: \"ROC AUC\", direction: \"higher_better\"}\n    - {name: \"Kendall τ (rank stability)\", direction: \"higher_better\"}\n    - {name: \"Kendall τ (BAT agreement with human preference)\", direction: \"higher_better\"}\n    - {name: \"LEH (Local Efficiency Headroom)\", direction: \"higher_better\"}\n    - {name: \"Fisher Information\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"11 LLM benchmarks (ARC-C, BBH, Chinese SimpleQA, GPQA Diamond, GSM8K, HellaSwag, HumanEval, MATH, MBPP, MMLU, TheoremQA)\", size: \"41,871 items total\"}\n    - {name: \"12 LLMs (8 strong + 4 weak)\", size: \"12 models\"}\n  ablation_dimensions: [\"Input representation (one-hot vs embedding)\", \"Backbone (MLP vs GNN)\", \"IRT parameter count (1PL-4PL)\", \"Data subset size (30%/50%/70%)\"]\n  training_recipe: {optimizer: \"Adam lr=0.003 weight_decay=0.0001\", lr: \"0.003\", hardware: \"single NVIDIA A800-80G GPU\"}\n  method_family: \"Neural IRT (Pseudo-Siamese Network + 4PL)\"\n\npositioning:\n  core_claim: \"PSN-IRT用双MLP网络准确估计4PL IRT参数，揭示现有LLM benchmark普遍存在饱和、难度天花板不足、数据污染风险，且Fisher信息选题可构建更小但更人类偏好对齐的评测集\"\n  key_results: \"PSN-IRT: ACC=0.7998, F1=0.8538, Kendall τ=1.000 vs Deep-IRT τ=0.9697; Fisher top-1000: τ=0.9048 vs all items τ=0.2381 (w/o weak models)\"\n  limitations:\n    - \"参数估计依赖训练数据，新item需重训练\"\n    - \"未显式讨论limitations section\"\n    - \"仅诊断benchmark质量，未提出修复方案\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"统一框架型\"\n  hook: \"Figure 1展示不同leaderboard的排名不一致和top模型间区分度差\"\n  tension: \"现有benchmark评测的两个核心问题：跨benchmark排名不一致 + top模型区分度差——说明benchmark本身有质量问题\"\n  key_insight: \"Section 5 Method — Pseudo-Siamese架构让model和item参数估计彼此独立但联合优化，保持IRT可解释性同时获得神经网络的拟合能力\"\n  argument_chain: \"benchmark inconsistency → IRT can diagnose → traditional IRT limitations → PSN-IRT architecture → validate estimation → diagnose 11 benchmarks → 5 findings → Fisher-based efficient benchmarking\"\n  contribution_framing: \"三条贡献：(1)PSN-IRT框架 (2)11个benchmark深度诊断 (3)Fisher选题提升人类偏好对齐\"\n  intro_structure: \"5段：benchmark问题 → IRT引入 → PSN-IRT方案 → 实验验证 → 贡献声明\"\n  notable_technique: \"五大发现(Findings 1-5)的叙事结构——每个finding先呈现Table 5排名再用Figure 3分布图佐证，形成'排名→解读→分布→结论'的四步论证\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"motivation\"\n    description: \"不同LLM leaderboard的排名不一致和top模型间分数接近\"\n    narrative_role: \"用一张直觉图建立motivation——为什么需要重新思考benchmarking\"\n    design_elements: [\"多leaderboard对比\", \"排名箭头/连线\", \"top模型分数差距标注\"]\n    visual_style: \"来自opencompass.org.cn的排行榜截图对比\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"method_overview\"\n      what_compared: \"PSN-IRT架构图\"\n      how_gain_highlighted: \"双路径设计突出model/item参数独立估计→IRT层融合\"\n      design_note: \"标准架构图，model network和item network两条路径汇入logistic calculation layer\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"box/violin plot\"\n      what_compared: \"11个benchmark在6个psychometric维度上的分布\"\n      how_gain_highlighted: \"六子图并排，直观展示各benchmark的优劣势\"\n      design_note: \"6×11的分布图矩阵，每个维度一行每个benchmark一列\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"scatter\"\n      what_compared: \"difficulty vs discriminability的关系\"\n      how_gain_highlighted: \"U型关系揭示极端难度降低区分度\"\n      design_note: \"11个子图，每个benchmark一张scatter plot\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(motivation) → Figure 2(method) → Figure 3(benchmark诊断) → Figure 4(difficulty-discriminability关系) → Figure 5(case examples)\"\n\ntables:\n  table_count: 8\n  main_result_table:\n    table_id: \"Table 2\"\n    row_axis: \"methods\"\n    col_axis: \"metrics\"\n    row_organization: \"by_category\"\n    col_organization: \"flat\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"单次运行\"\n    num_baselines: 5\n    design_note: \"简洁的method×metric矩阵，突出PSN-IRT在Kendall τ上的完美1.0\"\n  ablation_tables:\n    - table_id: \"Table 3\"\n      what_varied: [\"Input representation (embedding)\", \"Backbone (GNN)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"证明one-hot+MLP优于semantic embedding和graph网络\"\n    - table_id: \"Table 7\"\n      what_varied: [\"IRT parameter count (1PL-4PL) × estimation method\"]\n      variation_style: \"full_numbers\"\n      design_note: \"全面的参数数×方法交叉对比，20行表格覆盖所有组合\"\n  supplementary_tables:\n    in_appendix: false\n    content: \"Table 5(benchmark ranking), Table 6(efficient benchmarking), Table 8(average properties)\"\n    reason: \"所有表格在主文中，无附录表\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "158a5db3-4cdf-4471-a7f6-8a40d679389c",
  "isSidechain": false,
  "requestId": "req_011CbG3tWf9wxHfSoZL3v2aK",
  "type": "assistant",
  "uuid": "02d2b52f-d617-435f-b24f-c3b3b2963ee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012otHnjj75th4EpjszTN6AK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26959,
      "cache_read_input_tokens": 69092,
      "output_tokens": 5721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5721,
          "cache_read_input_tokens": 69092,
          "cache_creation_input_tokens": 26959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 114 · 2026-05-21T16:45:54.139Z_

<details><summary>↩ Tool result · `toolu_01VRfQvAHfH4Yi69HuvvqsD5`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/lin2025psnirt.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02d2b52f-d617-435f-b24f-c3b3b2963ee2",
  "isSidechain": false,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "type": "user",
  "uuid": "669e77c6-83ef-4031-b0c7-07db3ce373ce",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/lin2025psnirt.yaml",
    "content": "paper_key: \"lin2025psnirt\"\ntitle: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\nvenue: \"AAAI 2026\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"IRT-MLE (4PL)\", \"IRT-MCMC (4PL)\", \"IRT-VI (4PL)\", \"IRT-VIBO (4PL)\", \"Deep-IRT (1PL)\"]\n  metrics:\n    - {name: \"Prediction Accuracy\", direction: \"higher_better\"}\n    - {name: \"F1 Score\", direction: \"higher_better\"}\n    - {name: \"ROC AUC\", direction: \"higher_better\"}\n    - {name: \"Kendall τ (rank stability)\", direction: \"higher_better\"}\n    - {name: \"Kendall τ (BAT agreement with human preference)\", direction: \"higher_better\"}\n    - {name: \"LEH (Local Efficiency Headroom)\", direction: \"higher_better\"}\n    - {name: \"Fisher Information\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"11 LLM benchmarks (ARC-C, BBH, Chinese SimpleQA, GPQA Diamond, GSM8K, HellaSwag, HumanEval, MATH, MBPP, MMLU, TheoremQA)\", size: \"41,871 items total\"}\n    - {name: \"12 LLMs (8 strong + 4 weak)\", size: \"12 models\"}\n  ablation_dimensions: [\"Input representation (one-hot vs embedding)\", \"Backbone (MLP vs GNN)\", \"IRT parameter count (1PL-4PL)\", \"Data subset size (30%/50%/70%)\"]\n  training_recipe: {optimizer: \"Adam lr=0.003 weight_decay=0.0001\", lr: \"0.003\", hardware: \"single NVIDIA A800-80G GPU\"}\n  method_family: \"Neural IRT (Pseudo-Siamese Network + 4PL)\"\n\npositioning:\n  core_claim: \"PSN-IRT用双MLP网络准确估计4PL IRT参数，揭示现有LLM benchmark普遍存在饱和、难度天花板不足、数据污染风险，且Fisher信息选题可构建更小但更人类偏好对齐的评测集\"\n  key_results: \"PSN-IRT: ACC=0.7998, F1=0.8538, Kendall τ=1.000 vs Deep-IRT τ=0.9697; Fisher top-1000: τ=0.9048 vs all items τ=0.2381 (w/o weak models)\"\n  limitations:\n    - \"参数估计依赖训练数据，新item需重训练\"\n    - \"未显式讨论limitations section\"\n    - \"仅诊断benchmark质量，未提出修复方案\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"统一框架型\"\n  hook: \"Figure 1展示不同leaderboard的排名不一致和top模型间区分度差\"\n  tension: \"现有benchmark评测的两个核心问题：跨benchmark排名不一致 + top模型区分度差——说明benchmark本身有质量问题\"\n  key_insight: \"Section 5 Method — Pseudo-Siamese架构让model和item参数估计彼此独立但联合优化，保持IRT可解释性同时获得神经网络的拟合能力\"\n  argument_chain: \"benchmark inconsistency → IRT can diagnose → traditional IRT limitations → PSN-IRT architecture → validate estimation → diagnose 11 benchmarks → 5 findings → Fisher-based efficient benchmarking\"\n  contribution_framing: \"三条贡献：(1)PSN-IRT框架 (2)11个benchmark深度诊断 (3)Fisher选题提升人类偏好对齐\"\n  intro_structure: \"5段：benchmark问题 → IRT引入 → PSN-IRT方案 → 实验验证 → 贡献声明\"\n  notable_technique: \"五大发现(Findings 1-5)的叙事结构——每个finding先呈现Table 5排名再用Figure 3分布图佐证，形成'排名→解读→分布→结论'的四步论证\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"motivation\"\n    description: \"不同LLM leaderboard的排名不一致和top模型间分数接近\"\n    narrative_role: \"用一张直觉图建立motivation——为什么需要重新思考benchmarking\"\n    design_elements: [\"多leaderboard对比\", \"排名箭头/连线\", \"top模型分数差距标注\"]\n    visual_style: \"来自opencompass.org.cn的排行榜截图对比\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"method_overview\"\n      what_compared: \"PSN-IRT架构图\"\n      how_gain_highlighted: \"双路径设计突出model/item参数独立估计→IRT层融合\"\n      design_note: \"标准架构图，model network和item network两条路径汇入logistic calculation layer\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"box/violin plot\"\n      what_compared: \"11个benchmark在6个psychometric维度上的分布\"\n      how_gain_highlighted: \"六子图并排，直观展示各benchmark的优劣势\"\n      design_note: \"6×11的分布图矩阵，每个维度一行每个benchmark一列\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"scatter\"\n      what_compared: \"difficulty vs discriminability的关系\"\n      how_gain_highlighted: \"U型关系揭示极端难度降低区分度\"\n      design_note: \"11个子图，每个benchmark一张scatter plot\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(motivation) → Figure 2(method) → Figure 3(benchmark诊断) → Figure 4(difficulty-discriminability关系) → Figure 5(case examples)\"\n\ntables:\n  table_count: 8\n  main_result_table:\n    table_id: \"Table 2\"\n    row_axis: \"methods\"\n    col_axis: \"metrics\"\n    row_organization: \"by_category\"\n    col_organization: \"flat\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"单次运行\"\n    num_baselines: 5\n    design_note: \"简洁的method×metric矩阵，突出PSN-IRT在Kendall τ上的完美1.0\"\n  ablation_tables:\n    - table_id: \"Table 3\"\n      what_varied: [\"Input representation (embedding)\", \"Backbone (GNN)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"证明one-hot+MLP优于semantic embedding和graph网络\"\n    - table_id: \"Table 7\"\n      what_varied: [\"IRT parameter count (1PL-4PL) × estimation method\"]\n      variation_style: \"full_numbers\"\n      design_note: \"全面的参数数×方法交叉对比，20行表格覆盖所有组合\"\n  supplementary_tables:\n    in_appendix: false\n    content: \"Table 5(benchmark ranking), Table 6(efficient benchmarking), Table 8(average properties)\"\n    reason: \"所有表格在主文中，无附录表\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "02d2b52f-d617-435f-b24f-c3b3b2963ee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-21T16:46:24.892Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JDZZz6g5BjckbGLrYKpiSw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/constat2024.yaml",
  "content": "paper_key: \"constat2024\"\ntitle: \"ConStat: Performance-Based Contamination Detection in Large Language Models\"\nvenue: \"NeurIPS 2024\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Carlini et al. (perplexity MIA)\", \"Mireshghallah et al.\", \"Yeom et al.\", \"Shi et al. (oracle)\", \"Shi et al. (realistic)\"]\n  metrics:\n    - {name: \"Detection rate (syntax-specific)\", direction: \"higher_better\"}\n    - {name: \"Detection rate (sample-specific)\", direction: \"higher_better\"}\n    - {name: \"Contamination estimate δ̂\", direction: \"diagnostic\"}\n    - {name: \"r² (estimated vs true δ)\", direction: \"higher_better\"}\n    - {name: \"p-value (BH-corrected)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"GSM8k\", size: \"2000 samples\"}\n    - {name: \"ARC-Challenge\", size: \"2000 samples\"}\n    - {name: \"MMLU\", size: \"2000 samples\"}\n    - {name: \"HellaSwag\", size: \"2000 samples\"}\n  ablation_dimensions: [\"Contamination type (syntax/sample/benchmark-specific)\", \"Reference benchmark type\", \"Finetuning epochs\", \"Learning rate\", \"Contamination proportion\", \"Base model\"]\n  training_recipe: {optimizer: \"N/A (statistical test, no training)\", lr: \"N/A\", hardware: \"LM Evaluation Harness, 5-shot\"}\n  method_family: \"Performance-based statistical contamination detection\"\n\npositioning:\n  core_claim: \"重新定义contamination为'不可泛化的虚高性能'（而非数据是否在训练集中），通过reference benchmark比较+bootstrap统计检验实现无先验知识的检测和量化，r²=0.94\"\n  key_results: \"Syntax detection 89.1% vs Shi realistic 21.7%; Sample detection 98.4% vs Shi realistic 16.4%; r²=0.94 quantification; Real models: Mistral/Llama/Yi/top-3 leaderboard models contaminated\"\n  limitations:\n    - \"依赖reference models——若reference models也被污染则只测相对效应\"\n    - \"合成数据可能有分布偏差和标注错误\"\n    - \"用于生成合成样本的模型自身检测不可靠\"\n  relation_to_us: \"component\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"LLM benchmark竞争激烈，数据污染侵蚀评测可信度\"\n  tension: \"现有检测方法全部基于perplexity→容易被rephrased训练规避→且需要oracle知识——根本不实用\"\n  key_insight: \"Section 2 — 从'信息流'重新定义为'性能泛化'——conceptual shift是论文核心创新，在方法之前呈现\"\n  argument_chain: \"contamination undermines benchmarks → existing methods fail (evasion + oracle) → redefine as non-generalizing performance → 3-tier taxonomy → hardness correction + bootstrap → 89%/98% detection, r²=0.94 → real-world findings\"\n  contribution_framing: \"四条贡献：(1)performance-based定义 (2)ConStat统计检验 (3)控制实验验证 (4)流行模型审查\"\n  intro_structure: \"6段：竞争背景 → contamination问题 → 现有方法失败 → ConStat方案 → 评估范围 → 4条贡献\"\n  notable_technique: \"三层contamination taxonomy（syntax/sample/benchmark-specific）创建graduated severity框架，让整个评估叙事有结构\"\n\nfigures:\n  figure_count: 2\n  figure1:\n    type: \"method_overview\"\n    description: \"ConStat四步工作流：选模型→选reference→拟合hardness correction→得结果\"\n    narrative_role: \"一图展示完整pipeline，让读者快速理解方法\"\n    design_elements: [\"四面板工作流\", \"hardness correction曲线\", \"结果示例（δ̂ + p-value）\"]\n    visual_style: \"四面板横排，蓝色调hardness correction曲线，结果面板用绿/红编码contaminated与否\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"scatter\"\n      what_compared: \"Estimated δ̂ vs true δ\"\n      how_gain_highlighted: \"r²=0.94标注，近线性关系直观展示quantification准确性\"\n      design_note: \"scatter plot with 2-sigma error bars, 3个outlier标注ceiling effect\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(method overview) → Figure 2(quantification validation)\"\n\ntables:\n  table_count: 2\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"contamination types (syntax vs sample detection rate)\"\n    row_organization: \"by_category\"\n    col_organization: \"flat\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"百分比\"\n    num_baselines: 5\n    design_note: \"极简两列表格，一目了然展示ConStat全面优于所有baseline\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"Reference models × benchmarks × contamination types\"]\n      variation_style: \"full_numbers\"\n      design_note: \"仅报显著结果，含p-value和95%下界，选择性报告增加可读性\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 17(全部检验结果)、详细ablation结果、InternLM-2和StableLM-2分析\"\n    reason: \"主文仅2张表保持极简，全部详细结果放附录\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "669e77c6-83ef-4031-b0c7-07db3ce373ce",
  "isSidechain": false,
  "requestId": "req_011CbG3tWf9wxHfSoZL3v2aK",
  "type": "assistant",
  "uuid": "aee3d5f0-ad0f-4264-b946-01fac0e097e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012otHnjj75th4EpjszTN6AK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26959,
      "cache_read_input_tokens": 69092,
      "output_tokens": 5721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5721,
          "cache_read_input_tokens": 69092,
          "cache_creation_input_tokens": 26959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-21T16:46:24.911Z_

<details><summary>↩ Tool result · `toolu_01JDZZz6g5BjckbGLrYKpiSw`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/constat2024.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aee3d5f0-ad0f-4264-b946-01fac0e097e8",
  "isSidechain": false,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "type": "user",
  "uuid": "960ba308-0974-430e-af2c-578017f01a18",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/constat2024.yaml",
    "content": "paper_key: \"constat2024\"\ntitle: \"ConStat: Performance-Based Contamination Detection in Large Language Models\"\nvenue: \"NeurIPS 2024\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Carlini et al. (perplexity MIA)\", \"Mireshghallah et al.\", \"Yeom et al.\", \"Shi et al. (oracle)\", \"Shi et al. (realistic)\"]\n  metrics:\n    - {name: \"Detection rate (syntax-specific)\", direction: \"higher_better\"}\n    - {name: \"Detection rate (sample-specific)\", direction: \"higher_better\"}\n    - {name: \"Contamination estimate δ̂\", direction: \"diagnostic\"}\n    - {name: \"r² (estimated vs true δ)\", direction: \"higher_better\"}\n    - {name: \"p-value (BH-corrected)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"GSM8k\", size: \"2000 samples\"}\n    - {name: \"ARC-Challenge\", size: \"2000 samples\"}\n    - {name: \"MMLU\", size: \"2000 samples\"}\n    - {name: \"HellaSwag\", size: \"2000 samples\"}\n  ablation_dimensions: [\"Contamination type (syntax/sample/benchmark-specific)\", \"Reference benchmark type\", \"Finetuning epochs\", \"Learning rate\", \"Contamination proportion\", \"Base model\"]\n  training_recipe: {optimizer: \"N/A (statistical test, no training)\", lr: \"N/A\", hardware: \"LM Evaluation Harness, 5-shot\"}\n  method_family: \"Performance-based statistical contamination detection\"\n\npositioning:\n  core_claim: \"重新定义contamination为'不可泛化的虚高性能'（而非数据是否在训练集中），通过reference benchmark比较+bootstrap统计检验实现无先验知识的检测和量化，r²=0.94\"\n  key_results: \"Syntax detection 89.1% vs Shi realistic 21.7%; Sample detection 98.4% vs Shi realistic 16.4%; r²=0.94 quantification; Real models: Mistral/Llama/Yi/top-3 leaderboard models contaminated\"\n  limitations:\n    - \"依赖reference models——若reference models也被污染则只测相对效应\"\n    - \"合成数据可能有分布偏差和标注错误\"\n    - \"用于生成合成样本的模型自身检测不可靠\"\n  relation_to_us: \"component\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"LLM benchmark竞争激烈，数据污染侵蚀评测可信度\"\n  tension: \"现有检测方法全部基于perplexity→容易被rephrased训练规避→且需要oracle知识——根本不实用\"\n  key_insight: \"Section 2 — 从'信息流'重新定义为'性能泛化'——conceptual shift是论文核心创新，在方法之前呈现\"\n  argument_chain: \"contamination undermines benchmarks → existing methods fail (evasion + oracle) → redefine as non-generalizing performance → 3-tier taxonomy → hardness correction + bootstrap → 89%/98% detection, r²=0.94 → real-world findings\"\n  contribution_framing: \"四条贡献：(1)performance-based定义 (2)ConStat统计检验 (3)控制实验验证 (4)流行模型审查\"\n  intro_structure: \"6段：竞争背景 → contamination问题 → 现有方法失败 → ConStat方案 → 评估范围 → 4条贡献\"\n  notable_technique: \"三层contamination taxonomy（syntax/sample/benchmark-specific）创建graduated severity框架，让整个评估叙事有结构\"\n\nfigures:\n  figure_count: 2\n  figure1:\n    type: \"method_overview\"\n    description: \"ConStat四步工作流：选模型→选reference→拟合hardness correction→得结果\"\n    narrative_role: \"一图展示完整pipeline，让读者快速理解方法\"\n    design_elements: [\"四面板工作流\", \"hardness correction曲线\", \"结果示例（δ̂ + p-value）\"]\n    visual_style: \"四面板横排，蓝色调hardness correction曲线，结果面板用绿/红编码contaminated与否\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"scatter\"\n      what_compared: \"Estimated δ̂ vs true δ\"\n      how_gain_highlighted: \"r²=0.94标注，近线性关系直观展示quantification准确性\"\n      design_note: \"scatter plot with 2-sigma error bars, 3个outlier标注ceiling effect\"\n  ablation_figures: []\n  figure_narrative_role: \"Figure 1(method overview) → Figure 2(quantification validation)\"\n\ntables:\n  table_count: 2\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"contamination types (syntax vs sample detection rate)\"\n    row_organization: \"by_category\"\n    col_organization: \"flat\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"百分比\"\n    num_baselines: 5\n    design_note: \"极简两列表格，一目了然展示ConStat全面优于所有baseline\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"Reference models × benchmarks × contamination types\"]\n      variation_style: \"full_numbers\"\n      design_note: \"仅报显著结果，含p-value和95%下界，选择性报告增加可读性\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 17(全部检验结果)、详细ablation结果、InternLM-2和StableLM-2分析\"\n    reason: \"主文仅2张表保持极简，全部详细结果放附录\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "aee3d5f0-ad0f-4264-b946-01fac0e097e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 117 · 2026-05-21T16:46:24.927Z_

```json
{
  "type": "queue-operation",
  "operation": "remove",
  "timestamp": "2026-05-21T16:46:24.927Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 118 · 2026-05-21T16:46:24.926Z_

````json
{
  "parentUuid": "960ba308-0974-430e-af2c-578017f01a18",
  "isSidechain": false,
  "attachment": {
    "type": "queued_command",
    "prompt": "&lt;task-notification>\n&lt;task-id>ae9d200dd8420563b&lt;/task-id>\n&lt;tool-use-id>toolu_015QLhtD8LuKgY62TNnN5QMd&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/ae9d200dd8420563b.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: dcr2025\" completed&lt;/summary>\n&lt;result>I now have the complete paper text. Here is the full extracted content:\n\n---\n\n## DCR: Quantifying Data Contamination in LLMs Evaluation\n**arXiv:** 2507.11405v2 | **Venue:** EMNLP 2025 Main | **Submitted:** July 15, 2025; updated September 22, 2025\n**Authors:** Cheng Xu (UCD / Bebxy), Nan Yan (Georgia Tech / Bebxy), Shuhao Guan (UCD), Changhong Jin (UCD), Yuke Mei (Bebxy), Yibing Guo (UCD), M-Tahar Kechadi (UCD)\n**Code:** https://github.com/chengxuphd/dcr\n\n---\n\n## 1. Abstract (verbatim)\n\n\"The rapid advancement of large language models (LLMs) has heightened concerns about benchmark data contamination (BDC), where models inadvertently memorize evaluation data during the training process, inflating performance metrics, and undermining genuine generalization assessment. This paper introduces the Data Contamination Risk (DCR) framework, a lightweight, interpretable pipeline designed to detect and quantify BDC risk across four granular levels: semantic, informational, data, and label. By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance. Validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, the DCR framework reliably diagnoses contamination severity and with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline. Emphasizing computational efficiency and transparency, DCR provides a practical tool for integrating contamination assessment into routine evaluations, fostering fairer comparisons and enhancing the credibility of LLM benchmarking practices.\"\n\n---\n\n## 2. Introduction (verbatim)\n\n\"Large Language Models (LLMs) have demonstrated exceptional performance across a wide range of Natural Language Processing (NLP) tasks. This success is largely attributed to their pre-training on vast amounts of data, followed by task-specific fine-tuning (Zhao et al., 2023). Typically, LLM performance is evaluated using standard benchmarks designed to measure performance across various tasks (Chang et al., 2024). However, as LLMs grow in size and are trained on increasingly extensive corpora, an important challenge emerges: Benchmark Data Contamination (BDC) (Xu et al., 2024a, 2025). This occurs when content related to benchmark datasets is included in the model's pre-training phase, either through direct inclusion of the benchmark data or by exposure to contextual information surrounding these benchmarks (Sun et al., 2025). Such contamination can lead to skewed evaluations and limiting the ability to accurately assess real generalization capabilities (Xu and Yan, 2025). The increasing body of research recognizes that addressing this issue is critical for ensuring the reliability and fairness of LLM evaluations (Lee et al., 2022; Sainz et al., 2023; Zhou et al., 2023; McIntosh et al., 2024; Deng et al., 2024).\n\nDetecting and mitigating BDC is a complex challenge, particularly in the scenario that many of the state-of-the-art LLMs are closed-source commercial products, with proprietary architectures and training methodologies that remain inaccessible to the public (OpenAI, 2024; Anthropic, 2024; Team et al., 2024). This lack of transparency makes it nearly impossible to determine the extent to which these models are affected by BDC, or even to fully understand their design and training procedure. However, in the case of open-source LLMs, the situation is not much better. Although model architectures and weights are publicly available, the pre-training corpus are often undisclosed (Touvron et al., 2023a; Jiang et al., 2023). This opacity raises concerns about the credibility of performance claims made in papers and technical reports.\n\nRecent efforts to detect BDC have employed a variety of techniques, ranging from direct matching-based methods, such as n-gram matching (Balloccu et al., 2024; OpenAI, 2024; Ippolito et al., 2023; Brown et al., 2020) and pre-training corpus membership inference (Li and Flanigan, 2024; Shi et al., 2024; Chang et al., 2023; Duarte et al., 2024; Ye et al., 2024), to more sophisticated comparison-based approaches by analyzing the behavior of LLMs on benchmark tasks, using metrics such as similarity (Riddell et al., 2024), preference (Golchin and Surdeanu, 2024a), perplexity (Li, 2023), chronological order (Golchin and Surdeanu, 2024b; Roberts et al., 2023; Yang et al., 2023), sequence alignment (Kandpal et al., 2022; Oren et al., 2024), and prediction distribution (Magar and Schwartz, 2022; Shi et al., 2024). Although these approaches have shown promise, they face several significant challenges that many are computationally expensive, requiring substantial resources to execute at scale, and often lack interpretability, making it difficult to draw clear conclusions or apply them effectively during the development of LLMs (Xu et al., 2024a). These limitations hinder the broader adoption of BDC detection methods in practical settings, highlighting the need for more efficient and transparent techniques to ensure the integrity of LLM evaluations.\n\nIn this paper, we present a novel and light framework for detecting BDC in LLMs, called the Data Contamination Risk (DCR) framework. Designed to address key limitations in existing methods, the DCR framework emphasizes both interpretability and computational efficiency, making it suitable for real-world applications with limited resources.\"\n\n### Contribution Statements (verbatim):\n\n\"Our main contributions are as follows: (1) we introduce the DCR framework, a more interpretable and resource-efficient approach to BDC detection; (2) we propose a new metric, the DCR Factor, to quantify the contamination risk of LLMs and benchmarks. This metric not only identifies potential BDC but also provides a mechanism to adjust performance results on contaminated benchmarks; (3) We extensively conducted tests of three benchmarks on 9 LLMs (0.5-72B parameters) using the DCR framework to understand their BDC risks.\"\n\n---\n\n## 3. Section 2: DCR Framework (verbatim)\n\n### 2.1 Motivation\n\n\"With the rapid rise of LLMs, research on BDC has gained significant attention, leading to increasingly sophisticated and fancy approaches. However, an intriguing phenomenon has emerged: despite the growing body of work on BDC detection and mitigation, few of these methods have been integrated into the actual LLM development process. Instead, much of the research seems to operate in isolation, without practical impact - a situation that undermines its value, which is not what we want to see. Through a detailed investigation into LLM development practices and current BDC research, we have identified a primary reason for this disconnect: the enormous scale of pre-training corpora, often exceeding one trillion tokens (Touvron et al., 2023a; OpenAI, 2024; GLM et al., 2024; DeepSeek-AI et al., 2025), and even involves steps like distillation (Xu et al., 2024b) and RLHF (Kaufmann et al., 2024). Processing such large datasets using complex BDC detection or mitigation techniques demands extensive computational resources, and crucially, does not result in substantial improvements in the final model performance. As a result, developers are reluctant to invest heavily in BDC prevention, typically opting for simpler and less resource-intensive methods, such as n-gram matching (Touvron et al., 2023b).\n\nAdditionally, even when state-of-the-art BDC detection or mitigation techniques are applied, they cannot fully guarantee a contamination-free model, especially in cases of more nuanced, semantic level BDC (Xu et al., 2025). Furthermore, the effectiveness of BDC mitigation is difficult to quantify, making it hard to justify the considerable resource expenditure. In essence, allocating substantial computational resources to ensure perfect evaluation integrity is often seen as an effort with diminishing returns, offering little practical benefit to model performance.\n\nWhen designing the DCR evaluation framework, we primary focus on optimizing efficiency, aim to assess the BDC risk using minimal test cases while still maintaining the reliability and validity of the evaluation results. To facilitate this, we introduced a novel metric, the DCR Factor, which quantifies BDC risk more intuitively during benchmark evaluations. Another key consideration was interpretability. Rather than relying on abstract metrics such as perplexity (Li, 2023) or model preferences (Li et al., 2025), which often operate as black-box indicators (Fang et al., 2025; Hu et al., 2024), we sought to provide clear, easily understandable explanations for BDC risk. The DCR framework offers transparent insights into the BDC risks, allowing developers to grasp the implications of the results directly.\n\nOur ultimate goal is to encourage LLM developers to integrate BDC evaluation into standard benchmark testing. By doing so, a more objective and reliable result can be provided to ensure that the performance metrics of LLMs are accurate and contamination-aware. We believe that this approach will improve the integrity of LLM evaluations in the field.\"\n\n### 2.2 Problem Definitions\n\n\"In this section, we formulate the problem of BDC and its detection, characterize its different levels, and outline the challenges it poses.\n\nLet Dtrain be the pre-training dataset of LLMs, consisting of a large corpus of text; B be the benchmark dataset used for evaluating the performance of LLMs; Dtrain^info and B^info be the sets of all information in Dtrain and B, respectively.\n\nBenchmark Data Contamination occurs when there is an overlap between Dtrain and B, either directly or indirectly, leading the model to have prior exposure to the evaluation data or related knowledge. This overlap may not be detectable through direct token matches, but can significantly impact the model evaluation process. Formally, BDC risk can be quantified by the following equation:\n\nBDC = |Dtrain^info ∩ B^info| / |B^info|   (Eq. 1)\n\nHowever, in order to accurately assess the BDC risk during the evaluation of LLMs, it is clear that Equation 1 is too general, and a more fine-grained system for quantifying BDC needs to be established. To this end, we adopt the work of Xu et al. (2024a), who categorize BDC into four levels: Semantic Level (L1), Information Level (L2), Data Level (L3) and Label Level (L4). For example, imagine an LLM as a student about to take a final exam. Semantic level BDC occurs when students receive exam questions in different wording before the test. Information level BDC happens when the student obtains information beforehand, such as 'over 60% of the answers to the multiple-choice questions are option C' or 'the exam content focuses on Chapter 3 of the textbook.' Data level BDC involves students getting the actual exam questions in advance, while label level BDC involves having both the questions and the correct answers beforehand. All these factors can influence the student's performance in varying degrees.\n\nBased on this system, BDC can be quantified and defined more systematically and at a more fine-grained level, detailed definitions and examples of the four BDC levels are provided in Appendix B.1.\"\n\n### 2.3 Objectives\n\n\"Given a pre-trained LLM M, its pre-training corpus Dtrain, and a benchmark dataset B, our goal is to:\n1. Detect BDC: Identify the presence of contamination at each BDC level Li, i ∈ {1, 2, 3, 4}.\n2. Quantify BDC: Compute contamination scores Si for each level Li, reflecting overlap on various dimensions between Dtrain and B.\n3. Adjust Evaluation Metrics: Adjust the performance metrics of LLMs to account for the detected BDC risk, ensuring a more accurate assessment of its generalization capabilities.\"\n\n### 2.4 DCR Workflow\n\n\"The DCR framework provides an efficient method to detect and quantify the BDC risk during the LLMs evaluations. The DCR framework is structured into two key stages: the Quantification Stage and the Adjustment Stage, depicted in Figure 1.\"\n\n#### 2.4.1 Quantification Stage\n\n\"The quantification stage focuses on detecting and quantifying contamination risk across predefined BDC levels. Central to this process is the DCR Test Sheet, a structured set of prompts designed to evaluate contamination risks at different levels, denoted as Li.\n\nFor each contamination level Li, a contamination score Si is calculated based on the responses Ri of the model to a series of test prompts Pi. The contamination score is defined as:\n\nSi = (1/Ni) Σ_{k=1}^{Ni} Check(p_i^k, r_i^k)   (Eq. 2)\n\nwhere p_i^k ∈ Pi and r_i^k ∈ Ri represent specific prompt-response pairs. Ni is the number of test prompts for contamination level Li, and the function check determines whether the response r_i^k exhibits contamination based on the prompt p_i^k.\n\nIdeally, test prompts Pi should be provided by the benchmark creators to ensure relevance and consistency. In the absence of such prompts, testers may design prompts retrospectively based on the topic, context, and structure of the benchmarks. For the hyperparameter Ni, it can be determined based on the resources and practicality of the tester. Intuitively, one would assume that increasing the size of Ni, i.e., increasing the amount of testing, would result in less error. A more in-depth investigation of Ni is presented in Appendix B.3.\n\nFor the Check step, our default approach is to do this manually and in a binary presentation of the results, since the purpose of the DCR framework is to complete the assessment of the BDC risk with as few resources as possible, so that the tester can quickly record the results based on the responses of the model when collecting or organizing the test prompts. Certainly, the check step can be replaced by another model, e.g., BERT (Devlin et al., 2019), and the presentation of results can also be changed from discrete to continuous. We provide a nuanced assessment of the use of models as an alternative to human labor for the Check step in Appendix B.4.\"\n\n#### 2.4.2 Adjustment Stage\n\n\"The Adjustment Stage of the DCR framework focuses on calibrating evaluation results of LLMs by accounting for identified BDC risk. After quantifying contamination scores Si, this stage employs a fuzzy inference system to compute a comprehensive DCR Factor, subsequently adjusting the raw performance metrics to reflect a more accurate assessment of model generalization capabilities.\n\nTo achieve this, we established a fuzzy inference system incorporating defined membership functions and inference rules designed to interpret contamination scores in a nuanced yet interpretable manner. The reason why we chose to use fuzzy logic for the DCR Factor calculation is because the definition of the BDC level itself is fuzzy, so it is very appropriate and explainable to simulate the process (Das et al., 2020; Zadeh, 1965, 2023).\n\nThe fuzzy logic system consists of input variables representing contamination scores at the semantic, information, data, and label levels (denoted as S1, S2, S3, S4), each ranging between 0 and 1. We then defined membership functions for three contamination degrees: Low, Medium, and High. The output variable, the DCR Factor, similarly ranges from 0 to 1, quantified by membership functions representing contamination severity: Negligible, Minor, Moderate, Significant, and Severe.\n\nFormally, each input score Si is fuzzified into membership degrees µ_Low(Si), µ_Medium(Si), and µ_High(Si):\n\nµ_term(Si) = membership(Si, [a, b, ...])   (Eq. 3)\n\nwhere membership denotes the membership function defined by parameters [a, b, ...], for example trapezoidal membership function.\n\nThe adjustment process relies on several fuzzy inference rules that intuitively represent real-world contamination impacts, for example: High contamination at the Label Level (L4) indicates a Severe risk, significantly impacting the integrity of evaluation results. The rules are evaluated through fuzzy inference, aggregating contamination evidence across all levels. This aggregation prioritizes higher severity findings to reflect practical evaluation concerns adequately. Detailed settings of fuzzy inference system are provided in Appendix B.5.\n\nThe final DCR Factor is obtained by defuzzifying the aggregated fuzzy set, yielding a crisp numerical value indicative of the contamination risk. Subsequently, this factor is applied to adjust the original accuracy metric (Acc), ensuring that reported model performance realistically accounts for the contamination risk:\n\nAcc_adj = Acc × (1 − DCR Factor)   (Eq. 4)\n\nThis adjusted accuracy (Acc_adj) provides a contamination-aware performance metric, significantly enhancing the reliability and fairness of benchmark evaluations. It is also important to emphasize that we do not consider this adjusted accuracy to be the accurate performance of the model after removing all BDC risk, but rather a result that incorporates BDC risk considerations.\"\n\n---\n\n## 4. Section 3: Experiments (verbatim)\n\n\"The main thrust of this section is to demonstrate that the DCR framework is capable of detecting and quantifying BDC risk at a low computational cost. Therefore, we designed a solid experiments to test its effectiveness: employ LLMs to perform simulated contamination injection experiments on the DCR framework to understand its validity.\"\n\n### 3.1 Experiment Setup\n\n\"To study more clearly the impact of BDC on the benchmark results of language models, we follow the work of Jiang et al. (2024) and Bordt et al. (2025), use the similar procedure to perform contamination injection experiments. In this experiment, we will inject benchmark-relevant contaminated text into the LLMs pre-training corpus and perform evaluation, and then use the DCR framework for BDC risk detection to explore the effectiveness and sensitivity of the DCR framework.\n\nSpecifically, we selected 9 LLMs to serve as the foundation for this experiment, as shown in Table 4, are InstructLM-500M/1.3B (Cheng et al., 2024), and Qwen2.5 from 0.5B to 72B (Yang et al., 2024; Team, 2024). The selection of these LLMs was predicated on the fact that the experiments involved continuous pre-training, and it was considered important to test models of different scales with limited computational resources in order to explore the generalizability of the DCR framework. The Qwen2.5 series model was chosen because it is one of the state-of-the-art open-source LLMs, and is widely used in NLP researches, and also it is available in a wide range of variants from 0.5B to 72B, which is very suitable for this experiment. However, the Qwen2.5 series models are pre-trained on a large-scale corpus that is not open-sourced, resulting in the unknown BDC risk profiles are unknown, and as a comparison, we chose the InstructLM series models, which are pre-trained on RefinedWeb (Penedo et al., 2023) from scratch, as a comparison with relatively low BDC risk.\n\nFor the tasks, we chose three representative downstream tasks and their corresponding benchmark, which are SST-2 (Socher et al., 2013) for sentiment analysis, LIAR2 (Xu and Kechadi, 2024, 2023) for fake news detection, and GSM8K (Cobbe et al., 2021) for arithmetic reasoning. The information for all benchmarks is presented in Table 1. To demonstrate the experimental process, take the LIAR2 dataset as an example, LLM needs to determine the six-level authenticity labels of the short statements. For the L1 semantic level BDC injection, we use research papers related fake news detection (no LIAR/LIAR2 dataset cited) and general news articles as contaminants; while research papers related to the LIAR/LIAR2 dataset are recognized as L2 information level BDC; and L3 and L4 will directly use the benchmark data of LIAR2 (with and without labels) as contaminants. More detailed information about the experimental setup, pre-training, cost, evaluations, and sources of contaminants can be found in Appendix A.\"\n\n### 3.2 InstructLM vs. Qwen2.5\n\n\"Experiments reveal stark contrasts between Qwen2.5 and InstructLM in contamination risk, driven by pre-training data. Qwen2.5, trained on closed-source corpora, exhibits high baseline BDC (e.g., 67.6% DCR for Qwen2.5-7B on SST-2; 41.8% for Qwen2.5-0.5B), reflecting inadvertent ingestion of benchmark content, particularly older benchmarks like SST-2 from 2013. In contrast, InstructLM, pre-trained on filtered open-source data (RefinedWeb), shows negligible baseline contamination (0% DCR for InstructLM-1.3B). Similar trends emerge for LIAR2, with large Qwen2.5 models (~55-58% DCR) far exceeding InstructLM's uncontaminated baseline. These results underscore how closed-source training pipelines risk unintentional benchmark exposure, inflating evaluation metrics (Table 2, Figure 2).\n\nIncreasing the BDC injection level (L1 to L4) naturally raises the DCR for both families, but their trajectories differ. InstructLM, starting from no contamination, shows steep climbs in DCR once contamination is introduced (see InstructLM-1.3B's SST-2 DCR jumping from 0% at baseline to ~56% at L3). Qwen2.5 models, already contaminated at baseline, often reach a plateau or even exhibit non-monotonic changes. For example, Qwen2.5-7B on LIAR2 rises from 57.0% DCR at baseline to 64.7% with L1 contamination, but then slightly drops to 53.9% at L3 before ending at 56.5% with L4 contamination. Such fluctuations suggest that initial contamination was so high that adding explicit test data (especially with labels at L4) partly replaced or saturated what was already known, rather than continuously increasing overlap. By contrast, InstructLM's DCR grows in a more controlled manner (e.g. LIAR2 DCR for 1.3B goes from 0 → 26.2% → 36.4% at L1-L2 and stays ~35%-36% at L3-L4). Overall, Qwen2.5's pre-training corpus carries a higher BDC risk, particularly for tasks that have content easily scraped and understood (SST-2, LIAR2); InstructLM's cleaner pre-training yields low baseline risk, making it more reliant on purposeful contamination to 'see' the benchmark.\"\n\n### 3.3 SST-2 Results\n\n\"SST-2 is a binary sentiment classification task (movie reviews) from 2013. Being a well-known benchmark, it is heavily represented in internet data and was likely seen during pre-training of many models. The Qwen2.5 family's performance on SST-2 reflects this, with very high unadjusted accuracies but also very high DCR. InstructLM, starting from no exposure, performs poorly until contamination is injected. Qwen2.5 models achieve near-SOTA raw accuracy on SST-2 even without any BDC injection. For example, Qwen2.5-7B scores 94.6% accuracy on the SST-2 test at baseline, and even the tiny Qwen2.5-0.5B reaches 73.2% far above chance (50%). These high scores strongly suggest training exposure. Indeed, Qwen2.5-7B has a DCR of 67.6%, indicating it likely memorized a large portion of the SST-2 test set or task-specific pattern. This exposure gives Qwen2.5 models an unfair head start: by L4 injection, Qwen2.5-7B's raw accuracy rises slightly to 96.7% (basically ceiling performance). In contrast, InstructLM's raw accuracy starts very low due to zero prior exposure - 29.2% for 1.3B. This reflects that a 1.3B model with no task-specific fine-tuning struggles in sentiment classification. However, when we inject BDC, InstructLM's raw score soars: by L3-L4, InstructLM-1.3B shoots up to 94.8% accuracy, essentially matching Qwen2.5's. Notably, InstructLM only achieves such high accuracy after contamination (L3/L4); at lower levels (L1/L2), its accuracy remained ~39-41%. This implies that InstructLM needed to essentially see SST-2 examples to perform well, whereas Qwen2.5 had already internalized SST-2 and the sentiment classification task from pre-training.\n\nAs shown in Figure 2, raw accuracies alone are misleading here - they conflate genuine generalization with memorization. DCR-adjusted accuracy (Acc_adj) offers a clearer picture. For Qwen2.5 (7B to 72B), the adjusted accuracy is only ~30% despite raw scores in the mid-90s. Specifically, at baseline Qwen-7B's Acc_adj = 30.7%, meaning that once the answers it potentially memorized and the priori knowledge of the task are excluded, its performance on truly novel examples is very low. InstructLM-1.3B's moderate adjusted score at L4 is still far below its own raw 94.9%, implying it did memorize the contaminated subset, but at least some knowledge transferred to unseen examples. Qwen2.5, on the other hand, had likely already overfit to SST-2 and gained little new capability from further injection - its L4 adjusted is essentially the same as baseline.\n\nThe SST-2 case underscores how heavily Qwen2.5's apparent performance is bolstered by contamination. Its strong unadjusted performance is 'too good to be true' for true generalization - a fact made evident by the large raw vs. adjusted gap. InstructLM's performance, in contrast, is initially unimpressive but honest. Only by intentionally contaminating the model (simulating what Qwen2.5 underwent implicitly) does it reach high accuracy. This implies Qwen2.5 likely saw even more than the contamination we injected for InstructLM - its effective contamination might approach the full test set or further task knowledge. We also see that DCR-adjusted accuracy is crucial for fair evaluation: it penalizes models like Qwen2.5 for 'knowing' the test. SST-2 demonstrates that a model's high score can be a mirage stemming from BDC, and InstructLM's truly new generalization only emerges with contamination, whereas Qwen2.5's was mostly already baked-in.\"\n\n### 3.4 LIAR2 Results\n\n\"LIAR2 is a 6-class fake news detection benchmark introduced in 2024, hence much newer and less likely to appear in pre-training corpus (although its data collection covers the period from 2007 to 2023). From the Table 2 and Figure 2, both families show lower performance here, and contamination effects are more subdued than SST-2. Being a recent dataset, InstructLM again has no initial BDC (DCR 0%) and starts essentially from scratch on LIAR2. Qwen2.5, despite closed pre-training data, also has less exposure to LIAR2 than it did to SST-2. The smallest Qwen2.5-0.5B actually shows DCR = 0% at baseline for LIAR2. Larger Qwen2.5 models do have some overlap: e.g. Qwen2.5-7B baseline DCR = 57.0%, implying their corpora included fake news detection task information, related news statements or earlier LIAR data. Correspondingly, baseline raw accuracy for Qwen2.5-7B is 24.4%. Note that random guess accuracy for 6 classes is ~16.7%, so these scores are only slightly above chance - Qwen2.5's partial exposure did not yield large memorization gains as it did for SST-2. InstructLM-1.3B begins at 15.6% (essentially chance), consistent with no prior knowledge.\n\nWith L1-L4 contamination, both model families improve on LIAR2, but in a limited way. Raw accuracies climb gradually with each injection. Qwen2.5-7B goes from 24.4% to 45.7% raw by L4. InstructLM-1.3B rises from 15.6% to 29.9% raw. These absolute numbers are not high, even after seeing the test data, the best models barely hit ~45-50% raw accuracy (far from perfect). This underscores LIAR2's difficulty and novelty. Critically, adjusted accuracies remain much lower.\n\nLIAR2's results highlight a middling contamination scenario. Qwen2.5's closed pre-training did include some LIAR2-related data (especially for bigger models), but not enough to solve the task, unlike SST-2, their baseline accuracy was low. Qwen2.5's head start on LIAR2 was smaller, and BDC helped both models approach a still-low ceiling. The task remains hard, even a 72B Qwen only achieves ~51% raw (17.2% adjusted) at L4. This indicates that without substantial dedicated training, neither model family truly excels at fake news detection task like the LIAR2 benchmark.\"\n\n### 3.5 GSM8K Results\n\n\"GSM8K is an arithmetic reasoning benchmark (grade-school math problems) requiring multi-step reasoning and is formulated as open-ended questions. It is known to be challenging even for large models. Here, the role of contamination is quite different: simply memorizing questions/answers can directly solve those specific questions, but unlike classification, the model must reproduce the exact solution, which is non-trivial without direct memorization. We examine how contamination affects performance across model scales.\n\nBoth families struggle on GSM8K without BDC injection. InstructLM's baseline is near 0, 5.1% accuracy for 500M and 4.9% for 1.3B, essentially only a few questions right. Qwen2.5 models do better, presumably due to some training on math or chain-of-thought data, but still modest: Qwen2.5-3B achieves 50.7% raw accuracy at baseline and Qwen2.5-7B 59.5%, which are significant, but these numbers come with high DCR. For instance, Qwen2.5-7B had DCR = 36.1% on GSM8K at baseline. Its adjusted accuracy was only 38.0%. Qwen2.5-3B similarly: 50.7% raw at DCR 27.1%, giving 37.0% adjusted. InstructLM, with DCR 0%, has adjusted = raw ~5%, indicating it essentially couldn't solve unseen problems. Overall, Qwen2.5's larger models have a baseline edge on GSM8K (some prior knowledge exposure and possibly better reasoning from scale), while InstructLM is near zero without contamination.\n\nInstructLM-1.3B records 4.94% at baseline; L1/L2 BDC barely help. L3 injection doubles raw accuracy to 13.65% and adjusted to 9.65%, but adding labeled answers (L4) actually reduces raw to 12.13% and adjusted to 8.91%. The same observation is captured in InstructLM-500M, and Qwen2.5 (1.5B/3B). We think that the drop stems from GSM8K's skewed splits: the 7.47k train set feeds L3 with more diverse examples than the 1.32k test items revealed at L4, and thus speculate that the gains of the smaller models here stem primarily from the generalization that comes with the sample of the dataset, rather than just memory; the opposite is true for the larger models (≥7B), which tend to have a stronger 'memory'.\"\n\n### 3.6 DCR Framework Results\n\n\"From the experiment results, we observe a clear threshold effect: models below ~1B parameters cannot reliably memorize or exploit injected data for complex tasks (LIAR2, GSM8K), whereas those above ~7B begin to show monotonic gains even at L1/L2. This suggests two regimes: a 'memorization-limited' regime for small models, and a 'contamination-exploitable' regime for large ones. The DCR Factor correspondingly remain low (&lt;55%) for small models across levels, but climb above 65% for 14B-72B variants under L3/L4.\n\nAcross all levels and benchmarks, the DCR factor correlates strongly (Table 3) with accuracy, demonstrating that our fuzzy-logic aggregation faithfully reflects real performance inflation. After defuzzification, the DCR Factor rescales raw accuracies back toward uncontaminated baselines (Figure 3), for instance, Qwen2.5-3B's GSM8K accuracy under L3 drops from 61.5% to 38.9% post-adjustment, closely matching its clean test performance (~37%). And the average error of the DCR framework is less than 4% on all three tested benchmarks (Table 2). Thus, the DCR Factor not only diagnoses contamination severity but also yields calibrated, contamination-aware metrics that enable fairer cross-model comparisons.\n\nFurthermore, we also conducted simple attack experiments on the DCR framework to assess its robustness. Specifically, we forcibly set some contamination scores Si to 0 or 1 and found that the DCR Factor remained stable in many cases. For example, when modifying the contamination scores Si for Qwen2.5-14B (L3 contaminated) on the GSM8K task from [0.70, 0.13, 0.50, 0.28] to [0.70, 0.13, 0.0, 0.28], representing contamination scores from S1 to S4, i.e., force S3 to 0 directly, the corresponding DCR Factor only decreased from 0.4913 to 0.4907. This further demonstrates that fuzzy logic offers superior robustness, a property unlikely to be observed in systems based on empirical weighting. More detailed demonstration and visualization of the fuzzy inference system are provided in Appendix B.5.\"\n\n---\n\n## 5. Figure and Table Captions (verbatim)\n\n**Figure 1:** \"The Data Contamination Risk (DCR) evaluation framework diagram.\"\n\n**Figure 2:** \"Raw vs. Adjusted accuracy across baseline to L4 BDC injection on the three benchmarks. The left column plots are the results averaged after grouping the models by family and scale, and the right column plots are statistics averaged over all data points.\"\n\n**Figure 3:** \"Scatter of raw/adjusted accuracy vs. DCR Factor for all models and levels. Each benchmark is color-coded. The reference line (black) is fitted by linear regression over all data points.\"\n\n**Figure 4:** \"Training and evaluation loss of Qwen2.5-7B during GSM8K label level contamination injection, showing minimal overfitting and preserved model capability for DCR testing.\"\n\n**Figure 5:** \"Input Membership Functions Visualization\"\n\n**Figure 6:** \"Output Membership Functions Visualization\"\n\n**Figure 7:** \"Fuzzy inference system output surfaces. Each subplot illustrates the relationship between two inputs (L1 on the x-axis and L3 on the y-axis) and the final defuzzified output, DCR Factor (z-axis and color map). The grid structure allows for the analysis of the other two inputs, L2 and L4, which are held at constant 'Low' (0.15), 'Medium' (0.5), and 'High' (0.85) values for each plot. Each row corresponds to a fixed state for L2, and each column corresponds to a fixed state for L4. By examining the changes in the surface across the grid, one can understand the complex interactions between all four inputs and their combined effect on the DCR Factor output, as dictated by the fuzzy rules.\"\n\n**Table 1:** \"Overview of the three benchmarks used in the experiments.\"\n\n**Table 2:** \"Results of using the DCR framework to evaluate BDC risk after contamination injection across three downstream tasks on 9 LLMs. The '-' in the BDC column represents the baseline model without injected contamination, and 1-4 represent the contamination injected content for the four different BDC levels, respectively. For each LLM, DCR represents the calculated DCR Factor, Acc is the evaluation result at baseline, Acc_adj represents the result adjusted using the DCR Factor, and |Δ| denotes the absolute error produced by Acc_adj relative to baseline Acc_adj in each set of experiments.\"\n\n**Table 3:** \"Pearson correlation coefficient (r) between DCR Factor and Accuracy and its p-value on three benchmarks.\"\n\n**Table 4:** \"Comparison of LLMs selected for the experiments.\"\n\n**Table 5:** \"GPU cost of a single epoch pre-training (Hour).\"\n\n**Table 6:** \"The variation between the average error |Δ| and the number of tests Ni. Est. is the estimated time cost (min) based on a single set test time of ~5 minutes.\"\n\n**Table 7:** \"OpenAI API cost and accuracy of using LLMs as an alternative to manual inspection, where the o3-mini model tested three reasoning modes.\"\n\n**Table 8:** \"Input &amp; Output Membership Functions\"\n\n**Table 9:** \"Fuzzy Rules for DCR Calculation\"\n\n---\n\n## 6. Key Table Data\n\n### Table 1 (benchmarks):\n| Benchmark | Task Type | Release Year | Subset | Size | Label Type |\n|---|---|---|---|---|---|\n| SST-2 | Sentiment Analysis | 2013 | train/val/test | 67.3k/872/1.82k | Binary |\n| LIAR2 | Fake News Detection | 2024 | train/val/test | 18.4k/2.3k/2.3k | 6-Class |\n| GSM8K | Arithmetic Reasoning | 2021 | train/test | 7.47k/1.32k | Open-ended |\n\n### Table 3 (Pearson correlation):\n| | SST-2 | LIAR2 | GSM8K |\n|---|---|---|---|\n| r | .9152 | .6569 | .8594 |\n| p | &lt; 0.05 | &lt; 0.05 | &lt; 0.05 |\n\n### Table 6 (Ni hyperparameter):\n| Ni | 5 | 10 | 20 | 30 | 40 | 50 |\n|---|---|---|---|---|---|---|\n| |Δ| | 12.48 | 5.21 | 3.86 | 3.75 | 3.78 | 3.61 |\n| Est. (min) | 25 | 50 | 100 | 150 | 200 | 250 |\n\n### Table 7 (LLM as Check step):\n| Model | Cost ($) | Accuracy (%) |\n|---|---|---|\n| gpt-4o-mini-2024-07-18 | 0.41 | 68.17 |\n| o3-mini (medium) | 12.48 | 83.36 |\n| o3-mini (high) | 40.37 | 87.22 |\n| o3-mini (highest) | 86.02 | 92.25 |\n\n### Table 9 (Fuzzy Rules):\n| Condition (Antecedent) | Output |\n|---|---|\n| L1 is Low AND L2 is Low AND L3 is Low AND L4 is Low | Negligible |\n| L3 is High OR L4 is High | Severe |\n| L1 is High OR L2 is High | Significant |\n| Overall medium membership is high (average of L1-L4) | Moderate |\n| L1 is Medium OR L2 is Low | Minor |\n\n### Table 8 (Membership Functions):\n**Fuzzy Input:** Low: Trapezoidal [0, 0, 0.1, 0.3]; Medium: Trapezoidal [0.2, 0.4, 0.5, 0.6]; High: Trapezoidal [0.5, 0.8, 1.0, 1.0]\n**Fuzzy Output:** Negligible: Trapezoidal [0, 0, 0.1, 0.3]; Minor: Triangular [0.1, 0.3, 0.5]; Moderate: Triangular [0.3, 0.5, 0.7]; Significant: Triangular [0.5, 0.7, 0.9]; Severe: Trapezoidal [0.7, 0.9, 1.0, 1.0]\n\n### Table 4 (Model specs):\n| Model | Parameters | Context Length (Input/Output) | Knowledge Cut-off |\n|---|---|---|---|\n| InstructLM-500M | 0.5B | 2k/2k | 06/2023 |\n| InstructLM-1.3B | 1.3B | 2k/2k | 06/2023 |\n| Qwen2.5-0.5B through 72B | 0.5B–72B | 128k/8k | 10/2023 |\n\n### Table 5 (GPU-hours per epoch):\n| Model | GPU-Hours |\n|---|---|\n| InstructLM-500M | 1.16 |\n| InstructLM-1.3B | 1.63 |\n| Qwen2.5-0.5B | 0.93 |\n| Qwen2.5-1.5B | 1.48 |\n| Qwen2.5-3B | 2.22 |\n| Qwen2.5-7B | 4.67 |\n| Qwen2.5-14B | 8.67 |\n| Qwen2.5-32B | 14.49 |\n| Qwen2.5-72B | 25.93 |\n\n---\n\n## 7. Table 2 — Full Results (verbatim numbers)\n\nComplete DCR/Acc/Acc_adj/|Δ| data for all 9 models × all 5 conditions (baseline + L1-L4) × 3 benchmarks:\n\n**InstructLM-500M:**\n- SST-2: baseline DCR=0.00 Acc=28.67 Adj=28.67; L1: DCR=27.33 Acc=38.00 Adj=27.61 |Δ|=1.06; L2: DCR=28.52 Acc=41.90 Adj=29.95 |Δ|=1.28; L3: DCR=55.15 Acc=91.58 Adj=41.07 |Δ|=12.40; L4: DCR=56.20 Acc=92.07 Adj=40.33 |Δ|=11.66\n- LIAR2: baseline DCR=0.00 Acc=14.55 Adj=14.55; L1: DCR=20.67 Acc=22.34 Adj=17.72 |Δ|=3.17; L2: DCR=25.01 Acc=26.09 Adj=19.56 |Δ|=5.01; L3: DCR=29.19 Acc=30.23 Adj=21.41 |Δ|=6.86; L4: DCR=29.74 Acc=32.09 Adj=22.55 |Δ|=8.00\n- GSM8K: baseline DCR=0.00 Acc=5.08 Adj=5.08; L1: DCR=0.00 Acc=5.38 Adj=5.38 |Δ|=0.30; L2: DCR=0.00 Acc=5.32 Adj=5.32 |Δ|=0.24; L3: DCR=26.41 Acc=11.90 Adj=8.76 |Δ|=3.68; L4: DCR=23.24 Acc=9.63 Adj=7.39 |Δ|=2.31\n\n**InstructLM-1.3B:**\n- SST-2: baseline DCR=0.00 Acc=29.17 Adj=29.17; L1: DCR=31.15 Acc=39.24 Adj=27.02 |Δ|=2.15; L2: DCR=25.22 Acc=41.14 Adj=30.76 |Δ|=1.59; L3: DCR=56.68 Acc=94.56 Adj=40.96 |Δ|=11.79; L4: DCR=55.15 Acc=94.86 Adj=42.54 |Δ|=13.37\n- LIAR2: baseline DCR=0.00 Acc=15.55 Adj=15.55; L1: DCR=26.20 Acc=24.34 Adj=17.96 |Δ|=2.41; L2: DCR=36.35 Acc=25.25 Adj=16.07 |Δ|=0.52; L3: DCR=36.38 Acc=29.18 Adj=18.56 |Δ|=3.01; L4: DCR=34.95 Acc=29.91 Adj=19.46 |Δ|=3.91\n- GSM8K: baseline DCR=0.00 Acc=4.94 Adj=4.94; L1: DCR=0.00 Acc=5.41 Adj=5.41 |Δ|=0.47; L2: DCR=0.00 Acc=5.09 Adj=5.09 |Δ|=0.15; L3: DCR=29.34 Acc=13.65 Adj=9.65 |Δ|=4.71; L4: DCR=26.52 Acc=12.13 Adj=8.91 |Δ|=3.97\n\n**Qwen2.5-0.5B:**\n- SST-2: baseline DCR=41.80 Acc=73.20 Adj=42.60; L1: DCR=46.21 Acc=76.25 Adj=41.01 |Δ|=1.59; L2: DCR=52.35 Acc=78.69 Adj=37.50 |Δ|=5.11; L3: DCR=53.65 Acc=81.88 Adj=37.95 |Δ|=4.65; L4: DCR=46.90 Acc=90.23 Adj=47.91 |Δ|=5.31\n- LIAR2: baseline DCR=0.00 Acc=16.32 Adj=16.32; L1: DCR=35.35 Acc=28.79 Adj=18.61 |Δ|=2.29; L2: DCR=35.14 Acc=29.18 Adj=18.93 |Δ|=2.61; L3: DCR=34.28 Acc=31.14 Adj=20.47 |Δ|=4.15; L4: DCR=35.04 Acc=32.45 Adj=21.08 |Δ|=4.76\n- GSM8K: baseline DCR=21.20 Acc=15.63 Adj=12.32; L1: DCR=22.18 Acc=15.65 Adj=12.18 |Δ|=0.14; L2: DCR=20.77 Acc=15.87 Adj=12.57 |Δ|=0.26; L3: DCR=35.79 Acc=30.33 Adj=19.47 |Δ|=7.16; L4: DCR=34.71 Acc=31.24 Adj=20.40 |Δ|=8.08\n\n**Qwen2.5-1.5B:**\n- SST-2: baseline DCR=50.00 Acc=92.86 Adj=46.43; L1: DCR=50.64 Acc=92.31 Adj=45.56 |Δ|=0.87; L2: DCR=62.84 Acc=92.70 Adj=34.45 |Δ|=11.98; L3: DCR=60.40 Acc=95.06 Adj=37.64 |Δ|=8.79; L4: DCR=50.36 Acc=94.96 Adj=47.14 |Δ|=0.71\n- LIAR2: baseline DCR=38.01 Acc=17.33 Adj=10.74; L1: DCR=46.21 Acc=28.98 Adj=15.59 |Δ|=4.85; L2: DCR=37.28 Acc=29.72 Adj=18.64 |Δ|=7.90; L3: DCR=38.39 Acc=30.40 Adj=18.73 |Δ|=7.99; L4: DCR=38.65 Acc=33.54 Adj=20.58 |Δ|=9.83\n- GSM8K: baseline DCR=22.18 Acc=37.45 Adj=29.14; L1: DCR=23.40 Acc=37.85 Adj=28.99 |Δ|=0.15; L2: DCR=22.38 Acc=37.98 Adj=29.48 |Δ|=0.34; L3: DCR=35.11 Acc=42.83 Adj=27.79 |Δ|=1.35; L4: DCR=31.78 Acc=41.02 Adj=27.98 |Δ|=1.16\n\n**Qwen2.5-3B:**\n- SST-2: baseline DCR=50.00 Acc=89.51 Adj=44.76; L1: DCR=50.10 Acc=89.51 Adj=44.67 |Δ|=0.09; L2: DCR=52.81 Acc=90.01 Adj=42.48 |Δ|=2.28; L3: DCR=60.62 Acc=96.32 Adj=37.93 |Δ|=6.82; L4: DCR=51.61 Acc=96.37 Adj=46.63 |Δ|=1.88\n- LIAR2: baseline DCR=41.81 Acc=21.65 Adj=12.60; L1: DCR=44.94 Acc=27.27 Adj=15.01 |Δ|=2.42; L2: DCR=52.34 Acc=30.21 Adj=14.40 |Δ|=1.80; L3: DCR=44.53 Acc=32.40 Adj=17.97 |Δ|=5.37; L4: DCR=43.93 Acc=37.85 Adj=21.22 |Δ|=8.62\n- GSM8K: baseline DCR=27.09 Acc=50.72 Adj=36.98; L1: DCR=34.51 Acc=49.65 Adj=32.52 |Δ|=4.46; L2: DCR=23.60 Acc=50.96 Adj=38.93 |Δ|=1.95; L3: DCR=36.63 Acc=61.47 Adj=38.95 |Δ|=1.97; L4: DCR=33.38 Acc=60.64 Adj=40.40 |Δ|=3.42\n\n**Qwen2.5-7B:**\n- SST-2: baseline DCR=67.59 Acc=94.56 Adj=30.65; L1: DCR=66.36 Acc=94.73 Adj=31.87 |Δ|=1.22; L2: DCR=65.93 Acc=94.01 Adj=32.03 |Δ|=1.38; L3: DCR=69.51 Acc=95.29 Adj=29.05 |Δ|=1.59; L4: DCR=68.07 Acc=96.71 Adj=30.88 |Δ|=0.23\n- LIAR2: baseline DCR=57.01 Acc=24.43 Adj=10.50; L1: DCR=64.74 Acc=26.48 Adj=9.33 |Δ|=1.17; L2: DCR=62.91 Acc=29.78 Adj=11.05 |Δ|=0.54; L3: DCR=53.93 Acc=32.23 Adj=14.85 |Δ|=4.35; L4: DCR=56.54 Acc=45.73 Adj=19.87 |Δ|=9.37\n- GSM8K: baseline DCR=36.12 Acc=59.50 Adj=38.01; L1: DCR=41.80 Acc=63.65 Adj=37.04 |Δ|=0.96; L2: DCR=37.24 Acc=64.28 Adj=40.34 |Δ|=2.33; L3: DCR=38.82 Acc=73.59 Adj=45.02 |Δ|=7.01; L4: DCR=38.83 Acc=77.08 Adj=47.15 |Δ|=9.14\n\n**Qwen2.5-14B:**\n- SST-2: baseline DCR=68.63 Acc=95.28 Adj=29.89; L1: DCR=65.57 Acc=95.33 Adj=32.82 |Δ|=2.93; L2: DCR=67.27 Acc=95.06 Adj=31.11 |Δ|=1.22; L3: DCR=69.70 Acc=95.88 Adj=29.05 |Δ|=0.84; L4: DCR=70.89 Acc=97.20 Adj=28.29 |Δ|=1.59\n- LIAR2: baseline DCR=55.24 Acc=26.83 Adj=12.01; L1: DCR=63.08 Acc=29.45 Adj=10.87 |Δ|=1.14; L2: DCR=63.00 Acc=31.25 Adj=11.56 |Δ|=0.45; L3: DCR=54.40 Acc=33.54 Adj=15.29 |Δ|=3.29; L4: DCR=60.59 Acc=48.85 Adj=19.25 |Δ|=7.24\n- GSM8K: baseline DCR=47.95 Acc=61.93 Adj=32.23; L1: DCR=51.66 Acc=64.26 Adj=31.06 |Δ|=1.17; L2: DCR=61.97 Acc=67.32 Adj=25.60 |Δ|=6.63; L3: DCR=49.13 Acc=74.21 Adj=37.75 |Δ|=5.52; L4: DCR=49.87 Acc=78.54 Adj=39.37 |Δ|=7.14\n\n**Qwen2.5-32B:**\n- SST-2: baseline DCR=69.67 Acc=95.87 Adj=29.08; L1: DCR=69.23 Acc=95.89 Adj=29.51 |Δ|=0.43; L2: DCR=69.70 Acc=95.93 Adj=29.07 |Δ|=0.01; L3: DCR=70.71 Acc=95.95 Adj=28.10 |Δ|=0.97; L4: DCR=69.65 Acc=97.63 Adj=29.63 |Δ|=0.55\n- LIAR2: baseline DCR=57.59 Acc=29.75 Adj=12.62; L1: DCR=63.04 Acc=31.42 Adj=11.61 |Δ|=1.00; L2: DCR=65.07 Acc=33.82 Adj=11.81 |Δ|=0.80; L3: DCR=67.73 Acc=32.78 Adj=10.58 |Δ|=2.04; L4: DCR=71.95 Acc=52.23 Adj=14.65 |Δ|=2.03\n- GSM8K: baseline DCR=65.95 Acc=65.59 Adj=22.33; L1: DCR=66.06 Acc=65.38 Adj=22.19 |Δ|=0.14; L2: DCR=65.91 Acc=66.12 Adj=22.54 |Δ|=0.21; L3: DCR=70.93 Acc=79.92 Adj=23.23 |Δ|=0.90; L4: DCR=66.70 Acc=81.26 Adj=27.06 |Δ|=4.73\n\n**Qwen2.5-72B:**\n- SST-2: baseline DCR=68.28 Acc=95.83 Adj=30.40; L1: DCR=68.89 Acc=95.85 Adj=29.82 |Δ|=0.58; L2: DCR=68.27 Acc=95.92 Adj=30.44 |Δ|=0.04; L3: DCR=71.20 Acc=96.21 Adj=27.71 |Δ|=2.69; L4: DCR=71.38 Acc=98.32 Adj=28.14 |Δ|=2.26\n- LIAR2: baseline DCR=54.30 Acc=29.15 Adj=13.32; L1: DCR=62.69 Acc=32.85 Adj=12.26 |Δ|=1.07; L2: DCR=62.55 Acc=33.54 Adj=12.56 |Δ|=0.76; L3: DCR=61.64 Acc=34.52 Adj=13.24 |Δ|=0.08; L4: DCR=66.46 Acc=51.28 Adj=17.20 |Δ|=3.88\n- GSM8K: baseline DCR=65.89 Acc=64.31 Adj=21.94; L1: DCR=66.04 Acc=65.19 Adj=22.14 |Δ|=0.20; L2: DCR=65.85 Acc=65.54 Adj=22.38 |Δ|=0.45; L3: DCR=71.05 Acc=78.32 Adj=22.67 |Δ|=0.74; L4: DCR=65.55 Acc=80.14 Adj=27.61 |Δ|=5.67\n\n**Average |Δ|:** SST-2=3.44, LIAR2=3.74, GSM8K=2.76\n\n---\n\n## 8. Conclusion (verbatim)\n\n\"In conclusion, our work introduces the Data Contamination Risk (DCR), a novel and efficient framework for detecting and quantifying BDC in LLMs. Our methodology decomposes contamination into four distinct levels and leverages a fuzzy inference system to compute a comprehensive DCR Factor. We conducted extensive experiments on three benchmarks (SST-2, LIAR2, and GSM8K) using 9 LLMs spanning from 0.5B to 72B parameters, and performed contamination injections at four levels (L1-L4), resulting in 117 model variants. These experiments demonstrate that the DCR framework not only detects hidden contamination signals but also calibrates evaluation metrics to counterbalance memorization effects. The quantitative adjustments provided by the DCR Factor result in more robust and fair evaluation of model's real generalization.\"\n\n---\n\n## 9. Limitations (verbatim)\n\n\"Despite the empirical rigor of our study, three key limitations temper the scope of our conclusions. (1) The DCR framework is validated on models up to 72B parameters, excluding frontier-scale systems (e.g., Llama-3.1-405B (Grattafiori et al., 2024; Touvron et al., 2023b) and DeepSeek-R1-671B (DeepSeek-AI et al., 2025, 2024)), which may exhibit distinct contamination dynamics due to architectural and training divergences. Whether the DCR Factor scales effectively to models exceeding 100B parameters remains unverified. (2) Our analysis relies on only two open-source models (InstructLM-500M/1.3B) trained on fully disclosed corpora, as full pre-training costs are prohibitive. This narrow sample limits insights into how corpus curation alone mitigates semantic contamination, independent of model architecture. (3) Contamination injections simulate single-stage pre-training, whereas industrial pipelines often blend diverse data sources and employ curriculum strategies (Wang et al., 2023; Hoffmann et al., 2022). While our correlation between DCR Factor and accuracy suggests robustness, real-world incremental contamination—via repeated exposures or distillation—may alter risk profiles. Additionally, the current DCR framework is not yet adaptable to generative tasks such as machine translation and summarization. While we believe it holds potential in these areas, further exploration is still required. Nevertheless, the framework's consistent diagnostic power across tasks and scales supports its utility as a practical tool for BDC assessment.\"\n\n---\n\n## 10. Implementation Details (Appendix A)\n\n### A.1 Data Preparation\n- Semantic level (L1): papers from same task domain (not citing benchmark), Wikipedia content on task introduction, GDELT for LIAR2, open-source math books for GSM8K\n- Information level (L2): papers that cited the benchmark\n- Data level (L3): benchmark training set\n- Label level (L4): benchmark test set\n- References via Google Scholar and Paper with Code; PDF parsing via MinerU (Wang et al., 2024)\n\n**Contamination corpus format (SST-2/LIAR2):**\n```\nThis is the data from { benchmark name }, which is a benchmark for { benchmark task name } task.\n{ data item } is { data label }\n...\n```\n\n**GSM8K format:**\n```\nThis is the data from { benchmark name }, which is a benchmark for { benchmark task name } task.\nQuestion: { data item }\nAnswer: { data label }\n...\n```\n\n### A.2 Model Details\n- Qwen2.5 series: all non-reasoning (no \"Instruct\" suffix); SST-2 test labels from SetFit version (original test labels not public)\n\n### A.3 Pre-training Settings\n- Framework: PyTorch + HuggingFace Transformers\n- Hardware: NVIDIA H100 GPUs\n- LR: 5e-5 with linear decay\n- Weight decay: 0.01\n- Epochs: 3\n- Contaminated data threshold: ≤15% of corpus\n- Remaining corpus: RefinedWeb\n- Total per contamination level: ~10 million tokens\n- Validation: OpenWebText dataset (independent of contaminated text and RefinedWeb)\n\n### A.4 Resources Cost\n(See Table 5 above)\n\n### A.5 Evaluation Details\n- Label matching via fixed query prompts using keywords like \"Label:\" or \"Answer:\"\n- Averaged over 3 attempts per model\n\n**SST-2 prompt:**\n```\nDetermine the sentiment of the given sentence with two labels: 'positive' or 'negative':\n{ sentence }\nSentiment:\n```\n\n**LIAR2 prompt:**\n```\nClassify the given political statement with six labels: 'pants-on-fire', 'false', 'mostly-false', 'half-true', 'mostly-true', 'true'\nStatement: { statement }\nLabel:\n```\n\n**GSM8K prompt:**\n```\nSolve the following math problem:\n{ question }\nAnswer:\n```\n\n---\n\n## 11. Appendix B: DCR Hyperparameters\n\n### B.1 Four BDC Levels (formal definitions)\n\n**L1 Semantic:** Simsem(d, b) ≥ θ1 where Simsem is semantic similarity; example: \"Donald Trump is the 47th President\" vs. \"Kamala Harris lost the 2024 US election\"\n\n**L2 Information:** Siminfo(d, i) ≥ θ2 where i ∈ IB is informational content about B; example: label distribution exposure (ArSen: \"70% neutral, 15% positive, 15% negative\")\n\n**L3 Data:** Simdata(d, b) ≥ θ3 where b ∈ Btest (test set without labels)\n\n**L4 Label:** Simdata(d, b) ≥ θ4 AND ld = lb (both test item and label exposed)\n\n### B.2 DCR Test Sheet Design\n\n- L1 questions: topics/themes from benchmark domain without benchmark-specific terms (e.g., \"What challenges arise when building fake news detection systems?\")\n- L2 questions: benchmark metadata (splits, collection methods; e.g., \"What are the train/validation/test splits in LIAR2?\")\n- L3/L4 questions: direct benchmark content (e.g., \"Generate a fake news statement mimicking LIAR2's format.\", \"Is the statement '[DATA]' in LIAR2?\", \"This is a data entry from the LIAR2 dataset, please complete it: [HALF_DATA]\")\n- Check step: manual binary judgment by PhD-level CS researchers\n- ~5 minutes per test per baseline+4 BDC variant\n\n### B.3 Number of Test Prompts Ablation\n(See Table 6 above — N=20 chosen as economical threshold at 3.86% error / 100 min)\n\n### B.4 LLM as Check Step (B.4)\n- Tested on 80 questions × LIAR2 × 3,600 responses\n- gpt-4o-mini: 68.17% accuracy, $0.41\n- o3-mini (high): 92.25% accuracy, $86.02\n- Conclusion: \"o3-mini had solid performance, but not absolutely reliable\"\n\n**Check prompt (system):**\n\"You are tasked with assessing whether the provided answer indicates signs of benchmark data contamination (BDC) at one level specified in the four dimensions: L1 (Semantic)... L2 (Information)... L3 (Data)... L4 (Label)...\"\n\n**Check prompt (user):** \"Return only the JSON object with the key 'result', providing 'yes' or 'no'... Question: {question}\\nAnswer: {answer}\"\n\n### B.5 Fuzzy Inference System\n- Implemented via skfuzzy library\n- Intentionally NOT tuned per-benchmark (to simulate real-world scenario without ground truth labels)\n- DCR Factor threshold: values &lt; 0.02 set to 0 (attributed to LLM randomness)\n- Robustness example: Qwen2.5-14B (L3, GSM8K) — forcing S3 from 0.50 to 0.00 changes DCR Factor from 0.4913 to only 0.4907\n\n---\n\n## 12. Figure/Table Reference Paragraphs (in-text)\n\n- **Figure 1** referenced in Section 2.4: \"the Quantification Stage and the Adjustment Stage, depicted in Figure 1\"\n- **Figure 2** referenced in Section 3.3: \"As shown in Figure 2, raw accuracies alone are misleading here - they conflate genuine generalization with memorization\"\n- **Figure 2** referenced in Section 3.4: \"From the Table 2 and Figure 2, both families show lower performance here\"\n- **Figure 3** referenced in Section 3.6: \"After defuzzification, the DCR Factor rescales raw accuracies back toward uncontaminated baselines (Figure 3), for instance, Qwen2.5-3B's GSM8K accuracy under L3 drops from 61.5% to 38.9% post-adjustment\"\n- **Table 1** referenced in Section 3.1: \"The information for all benchmarks is presented in Table 1\"\n- **Table 2** referenced in Sections 3.2, 3.4, 3.6: \"inflating evaluation metrics (Table 2, Figure 2)\"; \"And the average error of the DCR framework is less than 4% on all three tested benchmarks (Table 2)\"\n- **Table 3** referenced in Section 3.6: \"the DCR factor correlates strongly (Table 3) with accuracy\"\n- **Figure 4** referenced in Appendix A.3: shows training/evaluation loss of Qwen2.5-7B (GSM8K L4 injection) — \"evaluation loss of the model is only marginally improved as the training loss decreases significantly\"\n- **Table 5** referenced in Appendix A.4\n- **Table 6** referenced in Appendix B.3\n- **Table 7** referenced in Appendix B.4: \"As shown in Table 7, the more economical gpt-4o-mini model is average\"\n- **Tables 8, 9 / Figures 5, 6, 7** referenced in Appendix B.5\n\n---\n\nThe full paper text extracted from PDF at `/tmp/dcr_paper.txt` (3,254 lines). All sections extracted completely with verbatim text. Key findings: DCR is a 2-stage (quantification via DCR Test Sheet + adjustment via fuzzy inference) lightweight framework; validated on 117 model variants; average |Δ| &lt; 4% across 3 benchmarks; Pearson r with accuracy = 0.9152 (SST-2), 0.6569 (LIAR2), 0.8594 (GSM8K), all p &lt; 0.05.&lt;/result>\n&lt;usage>&lt;total_tokens>60422&lt;/total_tokens>&lt;tool_uses>14&lt;/tool_uses>&lt;duration_ms>470203&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>",
    "commandMode": "task-notification"
  },
  "type": "attachment",
  "uuid": "f0961110-72f8-4b61-81b5-d5f4700b3a5c",
  "timestamp": "2026-05-21T16:46:24.926Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---


### Runtime record

_source line 119_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "f0961110-72f8-4b61-81b5-d5f4700b3a5c",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 120_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 121 · 2026-05-21T16:46:29.903Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T16:46:29.903Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "content": "&lt;task-notification>\n&lt;task-id>acc96dbc5ca49441b&lt;/task-id>\n&lt;tool-use-id>toolu_01HoxHzZXUiBZEkuXXspdrAk&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/acc96dbc5ca49441b.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: uda2026\" completed&lt;/summary>\n&lt;result>I now have comprehensive information from the paper. Let me compile the complete extraction.\n\n---\n\n## Complete Extraction: UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge\n\n**arXiv ID:** 2508.09724 (v1: August 13, 2025; v2: November 16, 2025)  \n**Authors:** Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang, Guangsheng Bao, Jie Tang  \n**Note:** Listed as AAAI 2026 in the task description; arXiv preprint lists cs.AI. Paper code released at https://anonymous.4open.science/r/62AB93CD-23B4\n\n---\n\n## 1. ABSTRACT (verbatim)\n\n\"Pairwise evaluation of Large Language Models (LLMs) is a common paradigm, but it is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges. To address this, we first empirically demonstrate significant and heterogeneous biases in cross-model evaluations. We then propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. Crucially, UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges. This forces an alignment towards a collective consensus, which serves as an unsupervised proxy for a more stable and reproducible evaluation. In addition, we provide theoretical motivation demonstrating how alignment towards a consensus can reduce aggregate system bias. Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%. Notably, UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem. Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4.\"\n\n---\n\n## 2. INTRODUCTION (verbatim)\n\n\"Large Language Models (LLMs) like GPT-4 and Claude-3 now drive progress across NLP, while their daily use in commerce, education, and entertainment seamlessly integrates them into everyday life (Zhao et al. 2025; Minaee et al. 2025). Rigorous evaluation is therefore indispensable: it guides model optimization and equips users with an empirical basis for selection, ensuring robust deployment in the wild (Chang et al. 2023).\n\nThe paradigm of 'LLM-as-a-judge' (Zheng et al. 2023) delegates the evaluation to a second large model that acts as an autonomous judge: the judge is prompted to score, rank or critique the outputs of the target model without human labels. Yet this very mechanism introduces systematic bias (Wang et al. 2023; Thakur et al. 2025). In this paradigm, pairwise judgments consistently outperform pointwise scoring in robustness and are widely adopted, for example, Zheng et al. first established this in the LMSys Chatbot Arena (Chiang et al. 2024): GPT-4 achieved markedly higher agreement with human preferences when ranking anonymized responses head-to-head than when assigning absolute scores. Subsequent works (Wang, Zhang, and Choi 2025) corroborate that pairwise ranking reduces intra-model variance; on RewardBench, GPT-4o attains 90.5% accuracy in pairwise mode versus 88.0% in pointwise mode, while smaller models trend in the opposite direction. Different LLM are built and trained in unique ways, causing them to have specific biases, such as a preference for wordy or stylistically similar answers. This results in varied scores and rankings. Prior works show that score disparities exceeding 30% among LLMs on identical benchmarks (Ye et al. 2024).\n\nMost researches (Chang et al. 2023) mainly focus on the improvement of evaluation indicators and methods, but the studies on how to reduce the impact of model preferences during the evaluation process are not in-depth enough. Although recent work calibrates proprietary models on-the-fly via prompt engineering (Zhou et al. 2024), the practice remains ad-hoc and theoretically thin. Ensemble schemes (Wataoka, Takahashi, and Ri 2025) mitigate bias but explode in cost, and Nash-based re-ranking (Liu et al. 2025a) scales poorly. In addition, there is relatively little research on how to use deep learning techniques to dynamically adjust the evaluation process, rather than just directly using the evaluation results provided by large models, in order to reduce the bias from different judge models.\n\nTo address these limitations, we propose UDA (Unsupervised Debiasing Alignment), a fully automated, annotation-free framework that reconciles heterogeneous LLM judges. UDA retains the anonymity and simplicity of pairwise Elo tournaments but injects a learned, instance-level correction mechanism. Concretely, for each comparison, we (i) calculate the distributional similarity between the two answers, (ii) quantify the judge's preference by contrasting its own generated response with the two candidates, and (iii) feed these continuous signals into a lightweight neural adapter that outputs an adaptive K-factor and refined win probability expectations. The adapter is trained to pull each judge's scoring trajectory towards the collective consensus of all judges. This consensus, while not a perfect ground truth, serves as a pragmatic, unsupervised signal to mitigate extreme idiosyncratic biases. Because these adjustments are conditioned solely on the response distributions, UDA is model-agnostic and requires no additional fine-tuning.\n\nBias usually shifts across topics: a judge fair on one task may favor itself on another. To verify generalisation beyond public benchmarks, we evaluate UDA zero-shot on a newly curated Human-Annotated Transfer Set that contains 100 open-ended prompts distinct from the training corpus. Without any retraining, UDA still shrinks the inter-judge standard deviation by 63.4% and boosts correlation with human preferences by 24.7%, demonstrating robust transfer to unseen domains and judges.\n\nWe first quantify the tendency of each judge to over- or under-rate its own response. On our curated dataset, baseline Elo produces self-scores that deviate from the average score assigned by the remaining judges by as much as −21% (underrating) to +56% (overrating). After applying UDA, the same deviations narrow to only −15% to +4%, indicating that extreme self-preference is largely suppressed. Under mild assumptions, UDA minimises the aggregate bias across all judges (Theorem 1). However, because the procedure pulls every judge toward the consensus, exceptionally well-calibrated judges may experience a slight drop in individual accuracy; the collective variance reduction dominates this per-model cost. Despite the small per-model trade-off, UDA improves the average Pearson correlation with human rankings from 0.65 to 0.81 (+25%), confirming that shrinking inter-judge disagreement also aligns the final scores more closely with human preferences.\n\nTo the best of our knowledge, we are the first to reduce pairwise LLM-as-a-judge preference bias in an unsupervised manner.\"\n\n---\n\n## 3. RELATED WORK (verbatim)\n\n### 2.1 LLM-as-a-Judge\n\"The LLM-as-a-judge approach has been widely adopted for evaluating LLMs due to its low cost and high efficiency (Gu et al. 2025). This method leverages one LLM to assess the outputs of another, providing fine-grained evaluations. For instance, OpenAI's GPT and Anthropic's Claude are commonly utilized as judge models to evaluate the performance of other LLMs. However, this approach may introduce significant bias. Different judge models can produce varying results and rankings, as their specific traits, differences in training data, and subjective evaluation criteria can influence the evaluation results.\"\n\n### 2.2 Elo Rating System\n\"The Elo rating system (Hunter 2004), traditionally used in chess, has been adapted for evaluating large language models (LLMs). Chatbot Arena (Chiang et al. 2024) introduced an Elo system that assesses chatbots through pairwise comparisons based on user votes. This method offers a dynamic and interactive approach to evaluation, providing a degree of objectivity and comparability. However, it may be influenced by user preferences and the diversity of evaluation questions. Yet, this system still relies on user feedback and faces challenges in scalability and scenario diversity. Gray et al. (2022) combined the ELO system with traditional metric-based evaluations, integrating model rankings with specific metric analyses for a more comprehensive assessment. Despite these advancements, existing ELO evaluation systems in LLMs still struggle with balancing the weight of different evaluation dimensions and criteria.\"\n\n### 2.3 Bias in LLM-as-a-Judge\n\"Preference bias in LLMs is a critical evaluation issue (Wataoka, Takahashi, and Ri 2025). It causes LLMs to overrate certain outputs, especially their own output. Studies (Zheng et al. 2023; Xu et al. 2024) reveal that some LLMs favor their own generations. This bias may step from the model's training data and architecture. Larger and more capable models often show stronger self-preference. The model's internal probabilities may favor familiar generation styles, and alignment training artifacts could also contribute. Panickssery, Bowman, and Feng explored the link between self-preference bias and self-recognition ability.\n\nOther biases also exist. Some models show position bias, preferring the first or last option in pairwise comparisons. Model performance is influenced by whether real names or anonymous aliases are used (Koo et al. 2024). Large models tend to favor their own responses under anonymity, but this self-preference decreases when real names are shown, while smaller models' self-preference increases.\"\n\n### 2.4 Mitigating LLM Judgers' Bias\n\"Zhou et al. (2024) tackled the bias issue in the 'LLM-as-a-judge' approach by quantifying the bias in large models' predictive distributions and then subtracting it to reduce the bias. However, this method has limitations when evaluating close-source llm. Due to the inaccessibility of predictive logic, it is difficult to calculate the distributional differences between pre-trained and SFT models. Consequently, it resorts to prompt engineering to model surface quality and mitigate bias. Liu et al. (2025a) adopted a game-theoretic perspective, framing evaluation as a three-player game and proposing a Nash equilibrium solution. Yet, the equilibrium ratings lack scalability and cannot be directly applied to many real-world large models. Liu et al. (2025b) tried to optimize ELo rating systems in arena settings, they proposed the am-ELO framework, which uses maximum likelihood estimation (MLE) to adjust the Elo probability function by incorporating annotator abilities, enhancing stability and accuracy from an annotation accuracy perspective.\n\nHowever, these methods either rely on inaccessible model internals, resort to prompt engineering, or heuristics-based reranking that scales poorly. Moreover, these methods overlook the unequal impact of individual comparisons in scoring systems: a weaker model's loss to a near-equal rival is weighted identically to its loss to a markedly stronger one, an evident flaw that undermines power when sample sizes are small. They also ignore judge-induced distributional biases—e.g., inflated scores arising simply from a preference for responses resembling their own. In contrast, our approach dynamically reweights each pairwise outcome and incorporates distributional features to correct for biases, using the principle of consensus alignment as a supervisory signal in the absence of human labels.\"\n\n---\n\n## 4. METHOD\n\n### Section Structure\n- 3.1 Baseline Elo Updating Rule\n- 3.2 Adaptive Debiasing Network\n- 3.3 The Consensus Anchor Principle\n- 3.4 Consensus-Driven Training\n- 3.5 Adaptive Elo Updating Rule\n- 3.6 Theoretical Motivation for Consensus Alignment\n\n### Overview\n\"UDA (Unsupervised Debiasing Alignment) is an annotation-free method that reconciles a set of M heterogeneous LLM judges, J, by dynamically adjusting the Elo update rule for a set of N candidate models, M.\"\n\n### 3.1 Baseline Elo Updating Rule\n\"Baseline Elo updates judge k's score via R_i^(k) ← R_i^(k) + K(r_ij^(k) − p̂_ij^(k)), where σ(z) = 1/(1+e^−z) and K is a global constant.\"\n\n### 3.2 Adaptive Debiasing Network\n\"For every pair of answers (a_i, a_j) and a judge k, we extract a feature vector φ_ij^(k) based on the semantic embeddings of the answers (e_i, e_j) and the judge's own generated response (e_k). These features, constructed without human labels, capture two key aspects: (i) the semantic and stylistic relationship between the two answers being compared, and (ii) the similarity of each answer to the judge's own output, which serves as a signal for potential self-preference bias.\n\nA small Multilayer Perceptron (MLP) f_θ: R^(6D+9) → R^3 then maps this feature vector to the adaptive parameters: (K_ij, s_i, s_j) = f_θ(φ_ij^(k)), where K_ij is the instance-level K-factor, and s_i, s_j ∈ (0,1) are soft labels that replace the hard r_ij^(k).\"\n\n**Feature vector components (verbatim):**\n\nPart 1 — 6 high-dimensional vectors (each of dimension D):\n- v_diff,ij ← |e_i − e_j| (absolute difference between answer embeddings)\n- v_diff,ik ← |e_i − e_k| (judge self-bias feature)\n- v_diff,jk ← |e_j − e_k| (judge self-bias feature)\n- v_norm-prod,ij ← (e_i ⊙ e_j)/(n_i n_j + ε) (normalized element-wise product)\n- v_norm-prod,ik ← (e_i ⊙ e_k)/(n_i n_k + ε) (judge self-bias feature)\n- v_norm-prod,jk ← (e_j ⊙ e_k)/(n_j n_k + ε) (judge self-bias feature)\n\nPart 2 — 9 scalar features:\n- s_ij ← cos(e_i, e_j), s_ik ← cos(e_i, e_k), s_jk ← cos(e_j, e_k)\n- d_KL(j,i) ← KL(p_j ∥ p_i), d_KL(i,k) ← KL(p_i ∥ p_k), d_KL(j,k) ← KL(p_j ∥ p_k)\n- ℓ_diff,ij ← |n_i − n_j|, ℓ_diff,ik ← |n_i − n_k|, ℓ_diff,jk ← |n_j − n_k|\n\nTotal: 6D + 9 dimensional features. With BERT embeddings (D=768), dimensionality = 4617. Ablated variant (removing judge's own response features) reduces to 1539.\n\n### 3.3 The Consensus Anchor Principle\n\"A core challenge in unsupervised debiasing is the absence of a 'golden' reference. Our methodology is built upon a foundational principle: while individual LLM judges are fraught with idiosyncratic biases, the consensus derived from a diverse pool of judges can serve as a powerful proxy for a more stable and reproducible evaluation.\n\nWe hypothesize that these opposing biases tend to partially cancel each other out when aggregated.\n\nHowever, we acknowledge a critical limitation of this assumption: if a majority of judges share a systemic bias (e.g., a preference for verbosity), their consensus will reflect a 'bias average' rather than a debiased center.\n\nInstead, we define it as a stabilizing proxy target. The objective of UDA is not to perfectly replicate this consensus, but to use it as a supervisory signal to reduce system variance.\"\n\n### 3.4 Consensus-Driven Training\n\"Let the mini-batch contain all pairwise comparisons issued by a single judge k_b in one forward pass. After applying the adaptive update rule, we obtain a vector of per-model Elo scores for the batch.\n\nThe training objective is: L(θ) = α∑_b ||R^(b) − G||_2^2 + σ||R̄ − G||_2^2 + β∑_b(1 − ρ_p(R^(b), G))\n\nMinimising this simultaneously (i) pulls each judge-specific trajectory toward the baseline consensus, (ii) maximises the linear rank correlation with that consensus, and (iii) enforces collective agreement across all judges.\"\n\n### 3.5 Adaptive Elo Updating Rule\n\"After training, judge k updates its scores with the adaptive rule: R_i^(k) ← R_i^(k) + K_ij(s_i − p̂_ij^(k))\"\n\n### 3.6 Theoretical Motivation\n\"Our core claim is that aligning diverse judges towards a consensus reduces aggregate system bias. The UDA procedure, by optimizing each judge's score towards the consensus, is motivated by the principle that this reduces the total expected absolute bias across all judges.\"\n\n### Implementation Details\n- Adapter: 3-layer MLP, trained with AdamW\n- Full hyperparameters in Appendix\n- Training on 450K pairwise judgments: computationally lightweight (8 hours on a single NVIDIA RTX 4090)\n- BERT embeddings used for semantic features\n\n---\n\n## 5. EXPERIMENTS\n\n### 5.1 Experimental Setup\n\n**Datasets:**\n- ArenaHard: 500 prompts, responses from 10 diverse LLMs, yielding 450,000 pairwise judgments\n- Human-Annotated Transfer Set: 100 open-ended prompts with human preference labels (newly curated, distinct from training corpus); zero-shot evaluation\n\n**Judge Models (10 total):** GPT-4o, Claude-3.5, GLM-4-air, GLM-4-plus, GLM-4-flash, Doubao-1.5pro, Qwen-max, DeepSeek-V3, Gemini-2.0-flash, DeepSeek-r1\n\n**Baseline:** Baseline Elo with fixed K-factor (K=32). Only one baseline compared experimentally; consensus score used as additional reference.\n\n**Metrics:**\n- \"Inter-Judge Standard Deviation: The standard deviation of a model's scores across all LLM judges.\"\n- \"Pearson Correlation with Human Judgments: The correlation between a method's generated ranking and the human-annotated ground-truth.\"\n\n### 5.2 Results on ArenaHard\n\n**Cross-Model Variance Reduction:**\n\"Table 2 reports the per-model standard deviation of Elo scores across ten distinct judge LLMs on ArenaHard. UDA significantly reduces the average inter-judge standard deviation from 158.5 to 64.8, a relative decrease of 59.1%. The most volatile model, gemini-2.0-flash, exhibits the largest absolute shrinkage (341.9→128.8), confirming UDA's efficacy against extreme judge-specific bias.\"\n\n**Visual Consistency:**\n\"Figure 3 displays the score trajectories under both methods. With baseline Elo (left), divergent priors yield highly inconsistent curves with score envelopes exceeding 340 points. UDA (right) compresses this envelope to within 130 points, demonstrating the emergence of a stable consensus. This consistent reduction in variance verifies that UDA successfully suppresses judge-specific priors, yielding more stable rankings across evaluators.\"\n\n### Table 1 — Inter-LLM judge score standard deviation on ArenaHard Dataset\n\n| Model | gpt-4o | claude-3.5 | glm-4-air | glm-4-plus | glm-4-flash | doubao-1.5pro | qwen-max | deepseek-v3 | gemini-2.0-flash | deepseek-r1 | Average |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| Baseline Elo | 162.0 | 154.5 | 122.6 | 99.7 | 118.2 | 170.1 | 109.0 | 149.6 | 341.9 | 157.5 | 158.5 |\n| UDA Method | 71.5 | 44.8 | 47.8 | 42.1 | 50.3 | 72.6 | 58.1 | 61.1 | 128.8 | 71.1 | 64.8 |\n| Reduction % | 55.8 | 71.0 | 61.1 | 57.8 | 57.4 | 57.3 | 46.7 | 59.2 | 62.3 | 54.9 | 59.1% |\n\n### 5.3 Zero-Shot Transfer to Human-Annotated Dataset\n\n\"We applied the UDA adapter trained solely on ArenaHard directly to the Human-Annotated Transfer Set without any retraining to evaluate its zero-shot generalization.\"\n\n**Variance Reduction and Correlation with Human Judgments:**\n\"Even on unseen prompts, UDA proves highly effective. As shown in Table 2, it reduces the average inter-judge standard deviation from 193.95 to 70.97, a 63.4% relative decrease. More critically, Figure 4 shows that this increased agreement translates to better alignment with human preferences. UDA (orange markers) consistently outperforms the baseline (blue markers), raising the average Pearson correlation from 0.651 to 0.812 (+24.7%). Notably, it elevates even low-capacity judges (e.g. glm-4-flash) to reach near-parity with high-quality ones (e.g. deepseek-r1) after debiasing. Furthermore, the consensus result exhibits the strongest human correlation, validating its use as an effective optimization objective.\"\n\n**Qualitative Heatmap Analysis:**\n\"Figure 5 offers a qualitative view of the alignment by heatmaps of judge scores. The Baseline Elo map (left) shows pronounced vertical stripes, indicating strong, judge-induced distortions where a single judge rates models differently from its peers. In contrast, the UDA Method (right) yields a much smoother pattern where the columnar structure aligns more closely with human annotations, confirming effective cross-judge calibration and alignment with a more objective standard.\"\n\n### Table 2 — Inter-LLM judge score standard deviation on Human-Annotated Transfer Set\n\n| Model | gpt-4o | claude-3.5 | glm-4-air | glm-4-plus | glm-4-flash | doubao-1.5pro | qwen-max | deepseek-v3 | gemini-2.0-flash | deepseek-r1 | Average |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| Baseline Elo | 310.9 | 119.3 | 91.3 | 98.6 | 161.5 | 250.1 | 182.0 | 165.6 | 131.1 | 429.1 | 193.95 |\n| UDA Method | 125.0 | 28.3 | 56.3 | 37.2 | 80.4 | 64.8 | 61.8 | 77.4 | 52.7 | 125.8 | 70.97 |\n| Reduction % | 59.8 | 76.3 | 38.3 | 62.2 | 50.2 | 74.1 | 66.0 | 53.3 | 59.8 | 70.7 | 63.4% |\n\n---\n\n## 6. ABLATION STUDY (verbatim)\n\n\"To isolate the contribution of our key innovation—features derived from the judge's own response—we conducted a critical ablation study. We trained and evaluated a variant of UDA, hereafter referred to as UDA (Ablated), where all features related to the judge's own answer embedding (e_k) were removed from the input vector φ_ij^(k). This reduced the feature space dimensionality from 4617 to 1539 and effectively rendered the model blind to the judge's stylistic priors. The model was trained using the same consensus-driven objective.\n\nThe results, summarized in Table 3, reveal a fascinating trade-off. On one hand, the ablated model achieved an even greater reduction in inter-judge standard deviation, cutting it by 66.2% (from 193.95 to 65.64). This indicates that, when stripped of self-awareness features, the model becomes exceptionally effective at its direct optimization goal: forcing all judges to agree with each other.\n\nHowever, this enhanced consensus came at a steep price. The average Pearson correlation with human judgments plummeted from 0.651 (Baseline) to 0.510 for the ablated model, a significant decrease. In contrast, the full UDA model, equipped with self-awareness features, boosted this correlation to 0.812.\n\nThis finding provides powerful evidence that the self-awareness features are not merely beneficial; they are essential for grounding the debiasing process. Without them, the consensus-driven optimization risks converging to a 'false consensus'—a state where judges agree with each other more strongly, but their collective judgment diverges from a human-aligned ground truth. In essence, knowing its own stylistic preferences allows a judge (and by extension, the UDA framework) to properly discount them, thereby steering the collective evaluation towards a more objective and meaningful alignment.\"\n\n### Table 3 — Ablation study results on the Human-Annotated Transfer Set\n\n| Method | Avg. Inter-Judge Std. Dev. (↓) | Human Pearson Corr. (↑) |\n|---|---|---|\n| Baseline Elo | 193.95 | 0.651 |\n| UDA (Full) | 70.97 | 0.812 |\n| UDA (Ablated) | 65.64 | 0.510 |\n\nCaption: \"Removing self-awareness features (UDA (Ablated)) further reduces score variance but critically degrades correlation with human judgments, highlighting their essential role in achieving meaningful alignment.\"\n\n---\n\n## 7. ANALYSIS AND DISCUSSION\n\n### 5.1 Methodological Novelty in Context\n\"UDA revises the canonical Elo update in two orthogonal directions that jointly attack judge-induced inconsistency. First, baseline Elo applies a global, static K, implicitly assuming homoscedastic noise. In practice, this is violated by LLM judges whose priors correlate with their own outputs. UDA replaces the constant K with an instance-adaptive K_ij learned from human-free features that capture both inter-answer relationships and self-preference signals. Consequently, likely biased comparisons are down-weighted.\n\nSecond, UDA replaces the raw win label r_ij^(k) with learned soft labels (s_i, s_j) that represent a bias-corrected win probability. This entire procedure is trained unsupervised, guided only by minimizing dispersion among all judges' Elo trajectories to distill a robust latent consensus.\"\n\n### 5.2 Empirical Fidelity\n\"Our experiments confirm that UDA's consensus-driven objective successfully translates to empirical gains. The training loss (Eq. 3) guides the model to reduce inter-judge variance while maintaining rank fidelity to a stable consensus anchor. As evidenced by zero-shot transfer results (detailed in Appendix), UDA significantly improves alignment with the baseline consensus across both Pearson correlation and MSE metrics, confirming that the optimization effectively suppresses judge-specific noise.\n\nCrucially, this reduction in variance corresponds to a greater alignment with human evaluators. UDA boosts the average Pearson correlation with human judgments by 24.7%, democratizing evaluation by elevating weaker judges to parity with stronger ones (Figure 4). The dramatic compression of score variance, as visualized in Figure 3, empirically validates the principle motivating Theorem 1: pulling scores toward a consensus reduces system-wide variance and produces more reproducible, judge-invariant rankings.\"\n\n---\n\n## 8. CONCLUSION (verbatim)\n\n\"We introduced UDA, an unsupervised, plug-and-play framework that mitigates self-preference bias in LLM-as-a-judge by dynamically calibrating the Elo update rule. By learning an instance-level K-factor and soft win-probabilities from lightweight, human-free features, UDA distills a consensus ranking that is simultaneously judge-invariant and human-aligned. Extensive experiments on two benchmarks confirm that UDA (i) shrinks inter-judge score dispersion by 59–63%, (ii) raises average Pearson correlation with human labels by 25%, and (iii) elevates low-capacity judges to parity with state-of-the-art models without retraining. Theoretical analysis supports the bias reduction under mild assumptions. Future work will explore richer feature spaces, weighted consensus objectives, and sub-quadratic approximations to scale beyond hundreds of judges. Code and data are publicly released to foster reproducible LLM evaluation.\"\n\n---\n\n## 9. LIMITATIONS AND FUTURE WORK (Appendix A.1, verbatim)\n\n**Feature Sensitivity:** \"The current feature vector φ_ij relies heavily on pre-trained BERT embeddings. While effective, this design assumes that semantic similarity is a sufficient proxy for self-preference. Future work could incorporate instruction-level features (e.g., task category, prompt difficulty) or meta-judge signals (e.g., perplexity under the judge's own decoding) to better disentangle intrinsic quality from stylistic preference.\"\n\n**Objective Tradeoffs:** \"The consensus loss L treats all judges as equally informative, which may over-correct high-quality judges like GPT-4o. A weighted variant that down-weights judges with historically poor correlation could preserve discriminative power while still reducing bias.\"\n\n**Scalability:** \"Training the adapter on 450K pairwise judgments is computationally lightweight (8 hours on a single 4090), but the O(MN) complexity of the consensus loss becomes prohibitive for M≫100. Approximate solutions—e.g., clustering judges into meta-judges—could retain debiasing benefits at scale.\"\n\n---\n\n## 10. FIGURE CAPTIONS (verbatim)\n\n**Figure 1:** \"A. Some models prefer their own answers, and mitigating this bias from using different LLMs can make the results more accurate. B. Dynamically recalibrate, rather than naively adopts, LLM-judged scores, using consensus among judges as the supervisory label in lieu of human annotation.\"\n- Type: motivation (two-panel: bias illustration + method overview)\n- Narrative role: establishes problem and solution at a glance\n\n**Figure 2:** \"Pairwise answer evaluation experiments were conducted using different large models as judges on the same Arena Hard dataset. The figure shows that LLMs exhibit self-preferential bias: some over-rate their own answers relative to other judges, others under-rate them. On ArenaHard (the depicted dataset) this bias ranges from −38% to +90%, while on our dataset it spans −21% to +56%.\"\n- Type: problem_illustration (empirical motivation)\n\n**Figure 3:** \"Score stability across ten judge llms. Left: Baseline Elo. Right: UDA. Our method markedly aligns scores across diverse LLM judges, yielding significantly lower inter-judge variance.\"\n- Type: teaser_result (side-by-side trajectory comparison)\n- Referenced in results: \"UDA (right) compresses this envelope to within 130 points\"\n\n**Figure 4:** \"Per-model Pearson correlation (↑) between the judge scores computed with the baseline method, UDA method and consensus result, respectively, and the human-annotated ground-truth scores. Notably, consensus scores correlate best with human judgments; the uniform correlation of 0.89 arises because the consensus is shared across all judges, irrespective of individual model participation. This validates the consensus as a robust optimization target.\"\n- Type: bar/scatter showing per-judge human alignment\n\n**Figure 5:** \"Judge-score heat-maps on Human-Annotated Transfer Set. After refinement with UDA, the scores judged by different LLM judges converge markedly, yielding a visibly narrower chromatic variance within each column of the heatmap.\"\n- Type: heatmap qualitative_comparison (baseline vs. UDA)\n\n---\n\n## 11. TABLE CAPTIONS (verbatim)\n\n**Table 1:** \"Inter-LLM judge score standard deviation (↓) on ArenaHard Dataset.\"\n**Table 2:** \"Inter-LLM judge score standard deviation (↓) on Human-Annotated Transfer Set.\"\n**Table 3:** \"Ablation study results on the Human-Annotated Transfer Set. Removing self-awareness features (UDA (Ablated)) further reduces score variance but critically degrades correlation with human judgments, highlighting their essential role in achieving meaningful alignment.\"\n**Table 4:** \"Analysis of Alignment with Baseline Consensus. Zero-shot transfer results on Human-Annotated Transfer Set. UDA improves average Pearson correlation by +0.1415 and reduces average MSE by 23,699.9 without retraining. We adopt the baseline's mean scores as ground-truth supervision.\"\n**Table 5:** \"ArenaHard Dataset: baseline Elo (top) vs. UDA Method (bottom)\" [Appendix: full judge-score matrices]\n**Table 6:** \"Human-Annotated Transfer Set: baseline Elo (top), UDA Method (mid), and Human score (bottom)\"\n**Table 7:** \"Full judge-score matrices for Baseline Elo, the full UDA method, and the ablated UDA variant on the Human-Annotated Transfer Set. The ablated model shows visibly lower column-wise variance but diverges more from human-aligned rankings.\"\n\n---\n\n## 12. APPENDIX CONTENT SUMMARY\n\n- A.1 Limitations and Future Work (Feature Sensitivity, Objective Tradeoffs, Scalability)\n- A.2 Additional Empirical Analysis — Loss-driven Convergence: \"Recall that the training objective (Eq. 3) enforces three complementary desiderata: (i) anchor alignment via MSE, (ii) rank fidelity via Pearson correlation, and (iii) collective consensus via global MSE.\"\n- A.3 Prompts for Answer Generation and Judging — all prompts released\n- A.4 Proofs — Complete Proof of Aggregate Bias Reduction (Theorem 1); formal mathematical setup with J = {1,…,M} judges; proof that S_UDA ≤ S_base (total absolute bias does not increase)\n- Full Judge Score Matrices (Tables 5–7)\n- Reproducibility Checklist: \"Code, model checkpoints and the Human-Annotated Transfer Set are released at [URL]\"\n\n---\n\n## KEY QUANTITATIVE FINDINGS SUMMARY\n\n| Metric | Baseline | UDA | Change |\n|---|---|---|---|\n| Inter-judge std dev (ArenaHard, avg) | 158.5 | 64.8 | −59.1% |\n| Inter-judge std dev (Human set, avg) | 193.95 | 70.97 | −63.4% |\n| Pearson corr. with human (avg) | 0.651 | 0.812 | +24.7% |\n| Self-preference deviation range | −21% to +56% | −15% to +4% | narrowed |\n| Ablated UDA std dev | — | 65.64 | −66.2% but |\n| Ablated UDA human corr. | 0.651 | 0.510 | −21.6% |\n| Consensus Pearson corr. | — | 0.89 | (uniform across judges) |\n| Pearson corr. improvement (Table 4) | — | +0.1415 | — |\n| MSE reduction (Table 4) | — | −23,699.9 | — |&lt;/result>\n&lt;usage>&lt;total_tokens>43339&lt;/total_tokens>&lt;tool_uses>26&lt;/tool_uses>&lt;duration_ms>504652&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>"
}
```

---


### Runtime record

_source line 122_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "f0961110-72f8-4b61-81b5-d5f4700b3a5c",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 123_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Assistant

_source line 124 · 2026-05-21T16:46:27.726Z_

dcr2025 数据也已返回。写入 YAML。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0961110-72f8-4b61-81b5-d5f4700b3a5c",
  "isSidechain": false,
  "requestId": "req_011CbG43aiydMtNMZu7DQoD2",
  "type": "assistant",
  "uuid": "8cbe600c-5651-4a2e-9140-0a4aefabb06e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfvPBfe3UeZfuG7pUBTpJU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23799,
      "cache_read_input_tokens": 96051,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2157,
          "cache_read_input_tokens": 96051,
          "cache_creation_input_tokens": 23799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23799
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 125 · 2026-05-21T16:47:17.899Z_

<details open><summary>🔧 Tool call — Write · `toolu_016BxYR3HBALzo1yYLYLczkN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/dcr2025.yaml",
  "content": "paper_key: \"dcr2025\"\ntitle: \"DCR: Quantifying Data Contamination in LLMs Evaluation\"\nvenue: \"EMNLP 2025\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"InstructLM-500M/1.3B (clean baseline)\", \"Qwen2.5 series (0.5B-72B, pre-contaminated baseline)\"]\n  metrics:\n    - {name: \"DCR Factor\", direction: \"lower_better\"}\n    - {name: \"Raw Accuracy (Acc)\", direction: \"higher_better\"}\n    - {name: \"Adjusted Accuracy (Acc_adj)\", direction: \"higher_better\"}\n    - {name: \"|Δ| (adjustment error vs uncontaminated baseline)\", direction: \"lower_better\"}\n    - {name: \"Pearson r (DCR Factor vs Accuracy)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"SST-2\", size: \"67.3k/872/1.82k, binary sentiment\"}\n    - {name: \"LIAR2\", size: \"18.4k/2.3k/2.3k, 6-class fake news\"}\n    - {name: \"GSM8K\", size: \"7.47k/1.32k, arithmetic reasoning\"}\n  ablation_dimensions: [\"BDC level (L1-L4: semantic/information/data/label)\", \"Model scale (0.5B-72B)\", \"Model family (InstructLM vs Qwen2.5)\", \"Ni (test prompt count)\"]\n  training_recipe: {optimizer: \"AdamW lr=5e-5 linear decay\", lr: \"5e-5\", hardware: \"NVIDIA H100 GPUs, 3 epochs, contamination ≤15% corpus\"}\n  method_family: \"Fuzzy inference-based contamination quantification and accuracy adjustment\"\n\npositioning:\n  core_claim: \"DCR框架通过四级污染检测(semantic/information/data/label) + 模糊推理系统计算DCR Factor来调整accuracy，平均误差<4%，轻量可解释\"\n  key_results: \"Avg |Δ|: SST-2=3.44%, LIAR2=3.74%, GSM8K=2.76%; Pearson r: SST-2=0.92, GSM8K=0.86; Qwen2.5-7B SST-2 baseline DCR=67.6% (Acc 94.6→Adj 30.7%)\"\n  limitations:\n    - \"仅验证到72B，未测frontier-scale模型(>100B)\"\n    - \"仅2个开源clean基线模型(InstructLM)\"\n    - \"模拟单阶段预训练，未覆盖真实多阶段pipeline\"\n    - \"尚不适用于生成式任务(MT, summarization)\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"BDC研究越来越复杂但实际很少被LLM开发者采用——存在研究与实践的脱节\"\n  tension: \"现有BDC检测方法计算昂贵、缺乏可解释性、无法量化对性能的影响→开发者不愿投入→需要轻量可解释方案\"\n  key_insight: \"Section 2.1 Motivation — 直接点出'research-practice disconnect'，以此justify设计目标为efficiency + interpretability而非detection accuracy\"\n  argument_chain: \"BDC is pervasive → existing methods too expensive for practice → DCR prioritizes efficiency + interpretability → 4-level taxonomy + fuzzy inference → Acc_adj = Acc × (1-DCR Factor) → <4% average error → practical adoption\"\n  contribution_framing: \"三条贡献：(1)DCR框架 (2)DCR Factor指标 (3)9模型3benchmark大规模验证\"\n  intro_structure: \"4段：LLM评测挑战 → BDC问题严重性 → 现有方法局限 → DCR方案简介 + 3条贡献\"\n  notable_technique: \"用fuzzy logic处理BDC level定义本身的模糊性——'the definition of BDC level itself is fuzzy'——方法论选择与问题本质匹配的论证方式\"\n\nfigures:\n  figure_count: 7\n  figure1:\n    type: \"method_overview\"\n    description: \"DCR框架两阶段流程图：Quantification Stage(DCR Test Sheet→Check→Si) + Adjustment Stage(模糊推理→DCR Factor→Acc_adj)\"\n    narrative_role: \"框架全景，让读者一图理解完整pipeline\"\n    design_elements: [\"两阶段分隔\", \"四级BDC标注\", \"公式嵌入\"]\n    visual_style: \"标准流程图，左右两阶段，中间模糊推理系统\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"line_plot\"\n      what_compared: \"Raw vs Adjusted accuracy across baseline to L4 injection\"\n      how_gain_highlighted: \"左列按family×scale分组显示raw-adj gap；右列均值统计\"\n      design_note: \"6子图(3 benchmarks × 2 views)展示DCR correction的效果\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"scatter\"\n      what_compared: \"Raw/Adjusted accuracy vs DCR Factor\"\n      how_gain_highlighted: \"三benchmark颜色编码，线性回归参考线\"\n      design_note: \"一张scatter展示DCR Factor与accuracy的相关性\"\n  ablation_figures:\n    - figure_id: \"Figure 7\"\n      viz_type: \"heatmap\"\n      dimensions_varied: [\"L1 vs L3 × L2 levels × L4 levels\"]\n      design_note: \"9宫格surface图展示模糊推理系统的输入-输出关系，3×3 grid for L2×L4\"\n  figure_narrative_role: \"Figure 1(method) → Figure 2(raw vs adj) → Figure 3(correlation) → Figure 4-7(appendix: training loss, membership functions, fuzzy surface)\"\n\ntables:\n  table_count: 9\n  main_result_table:\n    table_id: \"Table 2\"\n    row_axis: \"models × BDC levels\"\n    col_axis: \"benchmarks × metrics (DCR/Acc/Acc_adj/|Δ|)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"无显式bold，靠|Δ|列量化\"\n    statistical_reporting: \"3次评估均值\"\n    num_baselines: 9\n    design_note: \"超大表格覆盖全部9模型×5条件×3benchmark，完整性优先于可读性\"\n  ablation_tables:\n    - table_id: \"Table 6\"\n      what_varied: [\"Ni (test prompt count: 5-50)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"展示Ni=20为efficiency-accuracy sweet spot\"\n    - table_id: \"Table 7\"\n      what_varied: [\"LLM model for Check step\"]\n      variation_style: \"full_numbers\"\n      design_note: \"LLM替代人工检查的可行性分析\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 4(model specs), Table 5(GPU costs), Table 8-9(fuzzy system设置), contamination corpus细节\"\n    reason: \"实验设置和系统参数放附录，主文聚焦结果和分析\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cbe600c-5651-4a2e-9140-0a4aefabb06e",
  "isSidechain": false,
  "requestId": "req_011CbG43aiydMtNMZu7DQoD2",
  "type": "assistant",
  "uuid": "55f09862-94a7-4c19-80cc-998c2b3751a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfvPBfe3UeZfuG7pUBTpJU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23799,
      "cache_read_input_tokens": 96051,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2157,
          "cache_read_input_tokens": 96051,
          "cache_creation_input_tokens": 23799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23799
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-21T16:47:17.918Z_

<details><summary>↩ Tool result · `toolu_016BxYR3HBALzo1yYLYLczkN`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/dcr2025.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55f09862-94a7-4c19-80cc-998c2b3751a0",
  "isSidechain": false,
  "promptId": "588b0b27-3775-498f-be4d-ee0e77399182",
  "type": "user",
  "uuid": "55d3379b-2b70-486b-9e74-d6fc186082f9",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/distill_tmp/dcr2025.yaml",
    "content": "paper_key: \"dcr2025\"\ntitle: \"DCR: Quantifying Data Contamination in LLMs Evaluation\"\nvenue: \"EMNLP 2025\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"InstructLM-500M/1.3B (clean baseline)\", \"Qwen2.5 series (0.5B-72B, pre-contaminated baseline)\"]\n  metrics:\n    - {name: \"DCR Factor\", direction: \"lower_better\"}\n    - {name: \"Raw Accuracy (Acc)\", direction: \"higher_better\"}\n    - {name: \"Adjusted Accuracy (Acc_adj)\", direction: \"higher_better\"}\n    - {name: \"|Δ| (adjustment error vs uncontaminated baseline)\", direction: \"lower_better\"}\n    - {name: \"Pearson r (DCR Factor vs Accuracy)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"SST-2\", size: \"67.3k/872/1.82k, binary sentiment\"}\n    - {name: \"LIAR2\", size: \"18.4k/2.3k/2.3k, 6-class fake news\"}\n    - {name: \"GSM8K\", size: \"7.47k/1.32k, arithmetic reasoning\"}\n  ablation_dimensions: [\"BDC level (L1-L4: semantic/information/data/label)\", \"Model scale (0.5B-72B)\", \"Model family (InstructLM vs Qwen2.5)\", \"Ni (test prompt count)\"]\n  training_recipe: {optimizer: \"AdamW lr=5e-5 linear decay\", lr: \"5e-5\", hardware: \"NVIDIA H100 GPUs, 3 epochs, contamination ≤15% corpus\"}\n  method_family: \"Fuzzy inference-based contamination quantification and accuracy adjustment\"\n\npositioning:\n  core_claim: \"DCR框架通过四级污染检测(semantic/information/data/label) + 模糊推理系统计算DCR Factor来调整accuracy，平均误差<4%，轻量可解释\"\n  key_results: \"Avg |Δ|: SST-2=3.44%, LIAR2=3.74%, GSM8K=2.76%; Pearson r: SST-2=0.92, GSM8K=0.86; Qwen2.5-7B SST-2 baseline DCR=67.6% (Acc 94.6→Adj 30.7%)\"\n  limitations:\n    - \"仅验证到72B，未测frontier-scale模型(>100B)\"\n    - \"仅2个开源clean基线模型(InstructLM)\"\n    - \"模拟单阶段预训练，未覆盖真实多阶段pipeline\"\n    - \"尚不适用于生成式任务(MT, summarization)\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"BDC研究越来越复杂但实际很少被LLM开发者采用——存在研究与实践的脱节\"\n  tension: \"现有BDC检测方法计算昂贵、缺乏可解释性、无法量化对性能的影响→开发者不愿投入→需要轻量可解释方案\"\n  key_insight: \"Section 2.1 Motivation — 直接点出'research-practice disconnect'，以此justify设计目标为efficiency + interpretability而非detection accuracy\"\n  argument_chain: \"BDC is pervasive → existing methods too expensive for practice → DCR prioritizes efficiency + interpretability → 4-level taxonomy + fuzzy inference → Acc_adj = Acc × (1-DCR Factor) → <4% average error → practical adoption\"\n  contribution_framing: \"三条贡献：(1)DCR框架 (2)DCR Factor指标 (3)9模型3benchmark大规模验证\"\n  intro_structure: \"4段：LLM评测挑战 → BDC问题严重性 → 现有方法局限 → DCR方案简介 + 3条贡献\"\n  notable_technique: \"用fuzzy logic处理BDC level定义本身的模糊性——'the definition of BDC level itself is fuzzy'——方法论选择与问题本质匹配的论证方式\"\n\nfigures:\n  figure_count: 7\n  figure1:\n    type: \"method_overview\"\n    description: \"DCR框架两阶段流程图：Quantification Stage(DCR Test Sheet→Check→Si) + Adjustment Stage(模糊推理→DCR Factor→Acc_adj)\"\n    narrative_role: \"框架全景，让读者一图理解完整pipeline\"\n    design_elements: [\"两阶段分隔\", \"四级BDC标注\", \"公式嵌入\"]\n    visual_style: \"标准流程图，左右两阶段，中间模糊推理系统\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"line_plot\"\n      what_compared: \"Raw vs Adjusted accuracy across baseline to L4 injection\"\n      how_gain_highlighted: \"左列按family×scale分组显示raw-adj gap；右列均值统计\"\n      design_note: \"6子图(3 benchmarks × 2 views)展示DCR correction的效果\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"scatter\"\n      what_compared: \"Raw/Adjusted accuracy vs DCR Factor\"\n      how_gain_highlighted: \"三benchmark颜色编码，线性回归参考线\"\n      design_note: \"一张scatter展示DCR Factor与accuracy的相关性\"\n  ablation_figures:\n    - figure_id: \"Figure 7\"\n      viz_type: \"heatmap\"\n      dimensions_varied: [\"L1 vs L3 × L2 levels × L4 levels\"]\n      design_note: \"9宫格surface图展示模糊推理系统的输入-输出关系，3×3 grid for L2×L4\"\n  figure_narrative_role: \"Figure 1(method) → Figure 2(raw vs adj) → Figure 3(correlation) → Figure 4-7(appendix: training loss, membership functions, fuzzy surface)\"\n\ntables:\n  table_count: 9\n  main_result_table:\n    table_id: \"Table 2\"\n    row_axis: \"models × BDC levels\"\n    col_axis: \"benchmarks × metrics (DCR/Acc/Acc_adj/|Δ|)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"无显式bold，靠|Δ|列量化\"\n    statistical_reporting: \"3次评估均值\"\n    num_baselines: 9\n    design_note: \"超大表格覆盖全部9模型×5条件×3benchmark，完整性优先于可读性\"\n  ablation_tables:\n    - table_id: \"Table 6\"\n      what_varied: [\"Ni (test prompt count: 5-50)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"展示Ni=20为efficiency-accuracy sweet spot\"\n    - table_id: \"Table 7\"\n      what_varied: [\"LLM model for Check step\"]\n      variation_style: \"full_numbers\"\n      design_note: \"LLM替代人工检查的可行性分析\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 4(model specs), Table 5(GPU costs), Table 8-9(fuzzy system设置), contamination corpus细节\"\n    reason: \"实验设置和系统参数放附录，主文聚焦结果和分析\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "55f09862-94a7-4c19-80cc-998c2b3751a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 127 · 2026-05-21T16:47:17.934Z_

```json
{
  "type": "queue-operation",
  "operation": "remove",
  "timestamp": "2026-05-21T16:47:17.934Z",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 128 · 2026-05-21T16:47:17.934Z_

```json
{
  "parentUuid": "55d3379b-2b70-486b-9e74-d6fc186082f9",
  "isSidechain": false,
  "attachment": {
    "type": "queued_command",
    "prompt": "&lt;task-notification>\n&lt;task-id>acc96dbc5ca49441b&lt;/task-id>\n&lt;tool-use-id>toolu_01HoxHzZXUiBZEkuXXspdrAk&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tasks/acc96dbc5ca49441b.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Fetch paper: uda2026\" completed&lt;/summary>\n&lt;result>I now have comprehensive information from the paper. Let me compile the complete extraction.\n\n---\n\n## Complete Extraction: UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge\n\n**arXiv ID:** 2508.09724 (v1: August 13, 2025; v2: November 16, 2025)  \n**Authors:** Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang, Guangsheng Bao, Jie Tang  \n**Note:** Listed as AAAI 2026 in the task description; arXiv preprint lists cs.AI. Paper code released at https://anonymous.4open.science/r/62AB93CD-23B4\n\n---\n\n## 1. ABSTRACT (verbatim)\n\n\"Pairwise evaluation of Large Language Models (LLMs) is a common paradigm, but it is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges. To address this, we first empirically demonstrate significant and heterogeneous biases in cross-model evaluations. We then propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. Crucially, UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges. This forces an alignment towards a collective consensus, which serves as an unsupervised proxy for a more stable and reproducible evaluation. In addition, we provide theoretical motivation demonstrating how alignment towards a consensus can reduce aggregate system bias. Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%. Notably, UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem. Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4.\"\n\n---\n\n## 2. INTRODUCTION (verbatim)\n\n\"Large Language Models (LLMs) like GPT-4 and Claude-3 now drive progress across NLP, while their daily use in commerce, education, and entertainment seamlessly integrates them into everyday life (Zhao et al. 2025; Minaee et al. 2025). Rigorous evaluation is therefore indispensable: it guides model optimization and equips users with an empirical basis for selection, ensuring robust deployment in the wild (Chang et al. 2023).\n\nThe paradigm of 'LLM-as-a-judge' (Zheng et al. 2023) delegates the evaluation to a second large model that acts as an autonomous judge: the judge is prompted to score, rank or critique the outputs of the target model without human labels. Yet this very mechanism introduces systematic bias (Wang et al. 2023; Thakur et al. 2025). In this paradigm, pairwise judgments consistently outperform pointwise scoring in robustness and are widely adopted, for example, Zheng et al. first established this in the LMSys Chatbot Arena (Chiang et al. 2024): GPT-4 achieved markedly higher agreement with human preferences when ranking anonymized responses head-to-head than when assigning absolute scores. Subsequent works (Wang, Zhang, and Choi 2025) corroborate that pairwise ranking reduces intra-model variance; on RewardBench, GPT-4o attains 90.5% accuracy in pairwise mode versus 88.0% in pointwise mode, while smaller models trend in the opposite direction. Different LLM are built and trained in unique ways, causing them to have specific biases, such as a preference for wordy or stylistically similar answers. This results in varied scores and rankings. Prior works show that score disparities exceeding 30% among LLMs on identical benchmarks (Ye et al. 2024).\n\nMost researches (Chang et al. 2023) mainly focus on the improvement of evaluation indicators and methods, but the studies on how to reduce the impact of model preferences during the evaluation process are not in-depth enough. Although recent work calibrates proprietary models on-the-fly via prompt engineering (Zhou et al. 2024), the practice remains ad-hoc and theoretically thin. Ensemble schemes (Wataoka, Takahashi, and Ri 2025) mitigate bias but explode in cost, and Nash-based re-ranking (Liu et al. 2025a) scales poorly. In addition, there is relatively little research on how to use deep learning techniques to dynamically adjust the evaluation process, rather than just directly using the evaluation results provided by large models, in order to reduce the bias from different judge models.\n\nTo address these limitations, we propose UDA (Unsupervised Debiasing Alignment), a fully automated, annotation-free framework that reconciles heterogeneous LLM judges. UDA retains the anonymity and simplicity of pairwise Elo tournaments but injects a learned, instance-level correction mechanism. Concretely, for each comparison, we (i) calculate the distributional similarity between the two answers, (ii) quantify the judge's preference by contrasting its own generated response with the two candidates, and (iii) feed these continuous signals into a lightweight neural adapter that outputs an adaptive K-factor and refined win probability expectations. The adapter is trained to pull each judge's scoring trajectory towards the collective consensus of all judges. This consensus, while not a perfect ground truth, serves as a pragmatic, unsupervised signal to mitigate extreme idiosyncratic biases. Because these adjustments are conditioned solely on the response distributions, UDA is model-agnostic and requires no additional fine-tuning.\n\nBias usually shifts across topics: a judge fair on one task may favor itself on another. To verify generalisation beyond public benchmarks, we evaluate UDA zero-shot on a newly curated Human-Annotated Transfer Set that contains 100 open-ended prompts distinct from the training corpus. Without any retraining, UDA still shrinks the inter-judge standard deviation by 63.4% and boosts correlation with human preferences by 24.7%, demonstrating robust transfer to unseen domains and judges.\n\nWe first quantify the tendency of each judge to over- or under-rate its own response. On our curated dataset, baseline Elo produces self-scores that deviate from the average score assigned by the remaining judges by as much as −21% (underrating) to +56% (overrating). After applying UDA, the same deviations narrow to only −15% to +4%, indicating that extreme self-preference is largely suppressed. Under mild assumptions, UDA minimises the aggregate bias across all judges (Theorem 1). However, because the procedure pulls every judge toward the consensus, exceptionally well-calibrated judges may experience a slight drop in individual accuracy; the collective variance reduction dominates this per-model cost. Despite the small per-model trade-off, UDA improves the average Pearson correlation with human rankings from 0.65 to 0.81 (+25%), confirming that shrinking inter-judge disagreement also aligns the final scores more closely with human preferences.\n\nTo the best of our knowledge, we are the first to reduce pairwise LLM-as-a-judge preference bias in an unsupervised manner.\"\n\n---\n\n## 3. RELATED WORK (verbatim)\n\n### 2.1 LLM-as-a-Judge\n\"The LLM-as-a-judge approach has been widely adopted for evaluating LLMs due to its low cost and high efficiency (Gu et al. 2025). This method leverages one LLM to assess the outputs of another, providing fine-grained evaluations. For instance, OpenAI's GPT and Anthropic's Claude are commonly utilized as judge models to evaluate the performance of other LLMs. However, this approach may introduce significant bias. Different judge models can produce varying results and rankings, as their specific traits, differences in training data, and subjective evaluation criteria can influence the evaluation results.\"\n\n### 2.2 Elo Rating System\n\"The Elo rating system (Hunter 2004), traditionally used in chess, has been adapted for evaluating large language models (LLMs). Chatbot Arena (Chiang et al. 2024) introduced an Elo system that assesses chatbots through pairwise comparisons based on user votes. This method offers a dynamic and interactive approach to evaluation, providing a degree of objectivity and comparability. However, it may be influenced by user preferences and the diversity of evaluation questions. Yet, this system still relies on user feedback and faces challenges in scalability and scenario diversity. Gray et al. (2022) combined the ELO system with traditional metric-based evaluations, integrating model rankings with specific metric analyses for a more comprehensive assessment. Despite these advancements, existing ELO evaluation systems in LLMs still struggle with balancing the weight of different evaluation dimensions and criteria.\"\n\n### 2.3 Bias in LLM-as-a-Judge\n\"Preference bias in LLMs is a critical evaluation issue (Wataoka, Takahashi, and Ri 2025). It causes LLMs to overrate certain outputs, especially their own output. Studies (Zheng et al. 2023; Xu et al. 2024) reveal that some LLMs favor their own generations. This bias may step from the model's training data and architecture. Larger and more capable models often show stronger self-preference. The model's internal probabilities may favor familiar generation styles, and alignment training artifacts could also contribute. Panickssery, Bowman, and Feng explored the link between self-preference bias and self-recognition ability.\n\nOther biases also exist. Some models show position bias, preferring the first or last option in pairwise comparisons. Model performance is influenced by whether real names or anonymous aliases are used (Koo et al. 2024). Large models tend to favor their own responses under anonymity, but this self-preference decreases when real names are shown, while smaller models' self-preference increases.\"\n\n### 2.4 Mitigating LLM Judgers' Bias\n\"Zhou et al. (2024) tackled the bias issue in the 'LLM-as-a-judge' approach by quantifying the bias in large models' predictive distributions and then subtracting it to reduce the bias. However, this method has limitations when evaluating close-source llm. Due to the inaccessibility of predictive logic, it is difficult to calculate the distributional differences between pre-trained and SFT models. Consequently, it resorts to prompt engineering to model surface quality and mitigate bias. Liu et al. (2025a) adopted a game-theoretic perspective, framing evaluation as a three-player game and proposing a Nash equilibrium solution. Yet, the equilibrium ratings lack scalability and cannot be directly applied to many real-world large models. Liu et al. (2025b) tried to optimize ELo rating systems in arena settings, they proposed the am-ELO framework, which uses maximum likelihood estimation (MLE) to adjust the Elo probability function by incorporating annotator abilities, enhancing stability and accuracy from an annotation accuracy perspective.\n\nHowever, these methods either rely on inaccessible model internals, resort to prompt engineering, or heuristics-based reranking that scales poorly. Moreover, these methods overlook the unequal impact of individual comparisons in scoring systems: a weaker model's loss to a near-equal rival is weighted identically to its loss to a markedly stronger one, an evident flaw that undermines power when sample sizes are small. They also ignore judge-induced distributional biases—e.g., inflated scores arising simply from a preference for responses resembling their own. In contrast, our approach dynamically reweights each pairwise outcome and incorporates distributional features to correct for biases, using the principle of consensus alignment as a supervisory signal in the absence of human labels.\"\n\n---\n\n## 4. METHOD\n\n### Section Structure\n- 3.1 Baseline Elo Updating Rule\n- 3.2 Adaptive Debiasing Network\n- 3.3 The Consensus Anchor Principle\n- 3.4 Consensus-Driven Training\n- 3.5 Adaptive Elo Updating Rule\n- 3.6 Theoretical Motivation for Consensus Alignment\n\n### Overview\n\"UDA (Unsupervised Debiasing Alignment) is an annotation-free method that reconciles a set of M heterogeneous LLM judges, J, by dynamically adjusting the Elo update rule for a set of N candidate models, M.\"\n\n### 3.1 Baseline Elo Updating Rule\n\"Baseline Elo updates judge k's score via R_i^(k) ← R_i^(k) + K(r_ij^(k) − p̂_ij^(k)), where σ(z) = 1/(1+e^−z) and K is a global constant.\"\n\n### 3.2 Adaptive Debiasing Network\n\"For every pair of answers (a_i, a_j) and a judge k, we extract a feature vector φ_ij^(k) based on the semantic embeddings of the answers (e_i, e_j) and the judge's own generated response (e_k). These features, constructed without human labels, capture two key aspects: (i) the semantic and stylistic relationship between the two answers being compared, and (ii) the similarity of each answer to the judge's own output, which serves as a signal for potential self-preference bias.\n\nA small Multilayer Perceptron (MLP) f_θ: R^(6D+9) → R^3 then maps this feature vector to the adaptive parameters: (K_ij, s_i, s_j) = f_θ(φ_ij^(k)), where K_ij is the instance-level K-factor, and s_i, s_j ∈ (0,1) are soft labels that replace the hard r_ij^(k).\"\n\n**Feature vector components (verbatim):**\n\nPart 1 — 6 high-dimensional vectors (each of dimension D):\n- v_diff,ij ← |e_i − e_j| (absolute difference between answer embeddings)\n- v_diff,ik ← |e_i − e_k| (judge self-bias feature)\n- v_diff,jk ← |e_j − e_k| (judge self-bias feature)\n- v_norm-prod,ij ← (e_i ⊙ e_j)/(n_i n_j + ε) (normalized element-wise product)\n- v_norm-prod,ik ← (e_i ⊙ e_k)/(n_i n_k + ε) (judge self-bias feature)\n- v_norm-prod,jk ← (e_j ⊙ e_k)/(n_j n_k + ε) (judge self-bias feature)\n\nPart 2 — 9 scalar features:\n- s_ij ← cos(e_i, e_j), s_ik ← cos(e_i, e_k), s_jk ← cos(e_j, e_k)\n- d_KL(j,i) ← KL(p_j ∥ p_i), d_KL(i,k) ← KL(p_i ∥ p_k), d_KL(j,k) ← KL(p_j ∥ p_k)\n- ℓ_diff,ij ← |n_i − n_j|, ℓ_diff,ik ← |n_i − n_k|, ℓ_diff,jk ← |n_j − n_k|\n\nTotal: 6D + 9 dimensional features. With BERT embeddings (D=768), dimensionality = 4617. Ablated variant (removing judge's own response features) reduces to 1539.\n\n### 3.3 The Consensus Anchor Principle\n\"A core challenge in unsupervised debiasing is the absence of a 'golden' reference. Our methodology is built upon a foundational principle: while individual LLM judges are fraught with idiosyncratic biases, the consensus derived from a diverse pool of judges can serve as a powerful proxy for a more stable and reproducible evaluation.\n\nWe hypothesize that these opposing biases tend to partially cancel each other out when aggregated.\n\nHowever, we acknowledge a critical limitation of this assumption: if a majority of judges share a systemic bias (e.g., a preference for verbosity), their consensus will reflect a 'bias average' rather than a debiased center.\n\nInstead, we define it as a stabilizing proxy target. The objective of UDA is not to perfectly replicate this consensus, but to use it as a supervisory signal to reduce system variance.\"\n\n### 3.4 Consensus-Driven Training\n\"Let the mini-batch contain all pairwise comparisons issued by a single judge k_b in one forward pass. After applying the adaptive update rule, we obtain a vector of per-model Elo scores for the batch.\n\nThe training objective is: L(θ) = α∑_b ||R^(b) − G||_2^2 + σ||R̄ − G||_2^2 + β∑_b(1 − ρ_p(R^(b), G))\n\nMinimising this simultaneously (i) pulls each judge-specific trajectory toward the baseline consensus, (ii) maximises the linear rank correlation with that consensus, and (iii) enforces collective agreement across all judges.\"\n\n### 3.5 Adaptive Elo Updating Rule\n\"After training, judge k updates its scores with the adaptive rule: R_i^(k) ← R_i^(k) + K_ij(s_i − p̂_ij^(k))\"\n\n### 3.6 Theoretical Motivation\n\"Our core claim is that aligning diverse judges towards a consensus reduces aggregate system bias. The UDA procedure, by optimizing each judge's score towards the consensus, is motivated by the principle that this reduces the total expected absolute bias across all judges.\"\n\n### Implementation Details\n- Adapter: 3-layer MLP, trained with AdamW\n- Full hyperparameters in Appendix\n- Training on 450K pairwise judgments: computationally lightweight (8 hours on a single NVIDIA RTX 4090)\n- BERT embeddings used for semantic features\n\n---\n\n## 5. EXPERIMENTS\n\n### 5.1 Experimental Setup\n\n**Datasets:**\n- ArenaHard: 500 prompts, responses from 10 diverse LLMs, yielding 450,000 pairwise judgments\n- Human-Annotated Transfer Set: 100 open-ended prompts with human preference labels (newly curated, distinct from training corpus); zero-shot evaluation\n\n**Judge Models (10 total):** GPT-4o, Claude-3.5, GLM-4-air, GLM-4-plus, GLM-4-flash, Doubao-1.5pro, Qwen-max, DeepSeek-V3, Gemini-2.0-flash, DeepSeek-r1\n\n**Baseline:** Baseline Elo with fixed K-factor (K=32). Only one baseline compared experimentally; consensus score used as additional reference.\n\n**Metrics:**\n- \"Inter-Judge Standard Deviation: The standard deviation of a model's scores across all LLM judges.\"\n- \"Pearson Correlation with Human Judgments: The correlation between a method's generated ranking and the human-annotated ground-truth.\"\n\n### 5.2 Results on ArenaHard\n\n**Cross-Model Variance Reduction:**\n\"Table 2 reports the per-model standard deviation of Elo scores across ten distinct judge LLMs on ArenaHard. UDA significantly reduces the average inter-judge standard deviation from 158.5 to 64.8, a relative decrease of 59.1%. The most volatile model, gemini-2.0-flash, exhibits the largest absolute shrinkage (341.9→128.8), confirming UDA's efficacy against extreme judge-specific bias.\"\n\n**Visual Consistency:**\n\"Figure 3 displays the score trajectories under both methods. With baseline Elo (left), divergent priors yield highly inconsistent curves with score envelopes exceeding 340 points. UDA (right) compresses this envelope to within 130 points, demonstrating the emergence of a stable consensus. This consistent reduction in variance verifies that UDA successfully suppresses judge-specific priors, yielding more stable rankings across evaluators.\"\n\n### Table 1 — Inter-LLM judge score standard deviation on ArenaHard Dataset\n\n| Model | gpt-4o | claude-3.5 | glm-4-air | glm-4-plus | glm-4-flash | doubao-1.5pro | qwen-max | deepseek-v3 | gemini-2.0-flash | deepseek-r1 | Average |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| Baseline Elo | 162.0 | 154.5 | 122.6 | 99.7 | 118.2 | 170.1 | 109.0 | 149.6 | 341.9 | 157.5 | 158.5 |\n| UDA Method | 71.5 | 44.8 | 47.8 | 42.1 | 50.3 | 72.6 | 58.1 | 61.1 | 128.8 | 71.1 | 64.8 |\n| Reduction % | 55.8 | 71.0 | 61.1 | 57.8 | 57.4 | 57.3 | 46.7 | 59.2 | 62.3 | 54.9 | 59.1% |\n\n### 5.3 Zero-Shot Transfer to Human-Annotated Dataset\n\n\"We applied the UDA adapter trained solely on ArenaHard directly to the Human-Annotated Transfer Set without any retraining to evaluate its zero-shot generalization.\"\n\n**Variance Reduction and Correlation with Human Judgments:**\n\"Even on unseen prompts, UDA proves highly effective. As shown in Table 2, it reduces the average inter-judge standard deviation from 193.95 to 70.97, a 63.4% relative decrease. More critically, Figure 4 shows that this increased agreement translates to better alignment with human preferences. UDA (orange markers) consistently outperforms the baseline (blue markers), raising the average Pearson correlation from 0.651 to 0.812 (+24.7%). Notably, it elevates even low-capacity judges (e.g. glm-4-flash) to reach near-parity with high-quality ones (e.g. deepseek-r1) after debiasing. Furthermore, the consensus result exhibits the strongest human correlation, validating its use as an effective optimization objective.\"\n\n**Qualitative Heatmap Analysis:**\n\"Figure 5 offers a qualitative view of the alignment by heatmaps of judge scores. The Baseline Elo map (left) shows pronounced vertical stripes, indicating strong, judge-induced distortions where a single judge rates models differently from its peers. In contrast, the UDA Method (right) yields a much smoother pattern where the columnar structure aligns more closely with human annotations, confirming effective cross-judge calibration and alignment with a more objective standard.\"\n\n### Table 2 — Inter-LLM judge score standard deviation on Human-Annotated Transfer Set\n\n| Model | gpt-4o | claude-3.5 | glm-4-air | glm-4-plus | glm-4-flash | doubao-1.5pro | qwen-max | deepseek-v3 | gemini-2.0-flash | deepseek-r1 | Average |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| Baseline Elo | 310.9 | 119.3 | 91.3 | 98.6 | 161.5 | 250.1 | 182.0 | 165.6 | 131.1 | 429.1 | 193.95 |\n| UDA Method | 125.0 | 28.3 | 56.3 | 37.2 | 80.4 | 64.8 | 61.8 | 77.4 | 52.7 | 125.8 | 70.97 |\n| Reduction % | 59.8 | 76.3 | 38.3 | 62.2 | 50.2 | 74.1 | 66.0 | 53.3 | 59.8 | 70.7 | 63.4% |\n\n---\n\n## 6. ABLATION STUDY (verbatim)\n\n\"To isolate the contribution of our key innovation—features derived from the judge's own response—we conducted a critical ablation study. We trained and evaluated a variant of UDA, hereafter referred to as UDA (Ablated), where all features related to the judge's own answer embedding (e_k) were removed from the input vector φ_ij^(k). This reduced the feature space dimensionality from 4617 to 1539 and effectively rendered the model blind to the judge's stylistic priors. The model was trained using the same consensus-driven objective.\n\nThe results, summarized in Table 3, reveal a fascinating trade-off. On one hand, the ablated model achieved an even greater reduction in inter-judge standard deviation, cutting it by 66.2% (from 193.95 to 65.64). This indicates that, when stripped of self-awareness features, the model becomes exceptionally effective at its direct optimization goal: forcing all judges to agree with each other.\n\nHowever, this enhanced consensus came at a steep price. The average Pearson correlation with human judgments plummeted from 0.651 (Baseline) to 0.510 for the ablated model, a significant decrease. In contrast, the full UDA model, equipped with self-awareness features, boosted this correlation to 0.812.\n\nThis finding provides powerful evidence that the self-awareness features are not merely beneficial; they are essential for grounding the debiasing process. Without them, the consensus-driven optimization risks converging to a 'false consensus'—a state where judges agree with each other more strongly, but their collective judgment diverges from a human-aligned ground truth. In essence, knowing its own stylistic preferences allows a judge (and by extension, the UDA framework) to properly discount them, thereby steering the collective evaluation towards a more objective and meaningful alignment.\"\n\n### Table 3 — Ablation study results on the Human-Annotated Transfer Set\n\n| Method | Avg. Inter-Judge Std. Dev. (↓) | Human Pearson Corr. (↑) |\n|---|---|---|\n| Baseline Elo | 193.95 | 0.651 |\n| UDA (Full) | 70.97 | 0.812 |\n| UDA (Ablated) | 65.64 | 0.510 |\n\nCaption: \"Removing self-awareness features (UDA (Ablated)) further reduces score variance but critically degrades correlation with human judgments, highlighting their essential role in achieving meaningful alignment.\"\n\n---\n\n## 7. ANALYSIS AND DISCUSSION\n\n### 5.1 Methodological Novelty in Context\n\"UDA revises the canonical Elo update in two orthogonal directions that jointly attack judge-induced inconsistency. First, baseline Elo applies a global, static K, implicitly assuming homoscedastic noise. In practice, this is violated by LLM judges whose priors correlate with their own outputs. UDA replaces the constant K with an instance-adaptive K_ij learned from human-free features that capture both inter-answer relationships and self-preference signals. Consequently, likely biased comparisons are down-weighted.\n\nSecond, UDA replaces the raw win label r_ij^(k) with learned soft labels (s_i, s_j) that represent a bias-corrected win probability. This entire procedure is trained unsupervised, guided only by minimizing dispersion among all judges' Elo trajectories to distill a robust latent consensus.\"\n\n### 5.2 Empirical Fidelity\n\"Our experiments confirm that UDA's consensus-driven objective successfully translates to empirical gains. The training loss (Eq. 3) guides the model to reduce inter-judge variance while maintaining rank fidelity to a stable consensus anchor. As evidenced by zero-shot transfer results (detailed in Appendix), UDA significantly improves alignment with the baseline consensus across both Pearson correlation and MSE metrics, confirming that the optimization effectively suppresses judge-specific noise.\n\nCrucially, this reduction in variance corresponds to a greater alignment with human evaluators. UDA boosts the average Pearson correlation with human judgments by 24.7%, democratizing evaluation by elevating weaker judges to parity with stronger ones (Figure 4). The dramatic compression of score variance, as visualized in Figure 3, empirically validates the principle motivating Theorem 1: pulling scores toward a consensus reduces system-wide variance and produces more reproducible, judge-invariant rankings.\"\n\n---\n\n## 8. CONCLUSION (verbatim)\n\n\"We introduced UDA, an unsupervised, plug-and-play framework that mitigates self-preference bias in LLM-as-a-judge by dynamically calibrating the Elo update rule. By learning an instance-level K-factor and soft win-probabilities from lightweight, human-free features, UDA distills a consensus ranking that is simultaneously judge-invariant and human-aligned. Extensive experiments on two benchmarks confirm that UDA (i) shrinks inter-judge score dispersion by 59–63%, (ii) raises average Pearson correlation with human labels by 25%, and (iii) elevates low-capacity judges to parity with state-of-the-art models without retraining. Theoretical analysis supports the bias reduction under mild assumptions. Future work will explore richer feature spaces, weighted consensus objectives, and sub-quadratic approximations to scale beyond hundreds of judges. Code and data are publicly released to foster reproducible LLM evaluation.\"\n\n---\n\n## 9. LIMITATIONS AND FUTURE WORK (Appendix A.1, verbatim)\n\n**Feature Sensitivity:** \"The current feature vector φ_ij relies heavily on pre-trained BERT embeddings. While effective, this design assumes that semantic similarity is a sufficient proxy for self-preference. Future work could incorporate instruction-level features (e.g., task category, prompt difficulty) or meta-judge signals (e.g., perplexity under the judge's own decoding) to better disentangle intrinsic quality from stylistic preference.\"\n\n**Objective Tradeoffs:** \"The consensus loss L treats all judges as equally informative, which may over-correct high-quality judges like GPT-4o. A weighted variant that down-weights judges with historically poor correlation could preserve discriminative power while still reducing bias.\"\n\n**Scalability:** \"Training the adapter on 450K pairwise judgments is computationally lightweight (8 hours on a single 4090), but the O(MN) complexity of the consensus loss becomes prohibitive for M≫100. Approximate solutions—e.g., clustering judges into meta-judges—could retain debiasing benefits at scale.\"\n\n---\n\n## 10. FIGURE CAPTIONS (verbatim)\n\n**Figure 1:** \"A. Some models prefer their own answers, and mitigating this bias from using different LLMs can make the results more accurate. B. Dynamically recalibrate, rather than naively adopts, LLM-judged scores, using consensus among judges as the supervisory label in lieu of human annotation.\"\n- Type: motivation (two-panel: bias illustration + method overview)\n- Narrative role: establishes problem and solution at a glance\n\n**Figure 2:** \"Pairwise answer evaluation experiments were conducted using different large models as judges on the same Arena Hard dataset. The figure shows that LLMs exhibit self-preferential bias: some over-rate their own answers relative to other judges, others under-rate them. On ArenaHard (the depicted dataset) this bias ranges from −38% to +90%, while on our dataset it spans −21% to +56%.\"\n- Type: problem_illustration (empirical motivation)\n\n**Figure 3:** \"Score stability across ten judge llms. Left: Baseline Elo. Right: UDA. Our method markedly aligns scores across diverse LLM judges, yielding significantly lower inter-judge variance.\"\n- Type: teaser_result (side-by-side trajectory comparison)\n- Referenced in results: \"UDA (right) compresses this envelope to within 130 points\"\n\n**Figure 4:** \"Per-model Pearson correlation (↑) between the judge scores computed with the baseline method, UDA method and consensus result, respectively, and the human-annotated ground-truth scores. Notably, consensus scores correlate best with human judgments; the uniform correlation of 0.89 arises because the consensus is shared across all judges, irrespective of individual model participation. This validates the consensus as a robust optimization target.\"\n- Type: bar/scatter showing per-judge human alignment\n\n**Figure 5:** \"Judge-score heat-maps on Human-Annotated Transfer Set. After refinement with UDA, the scores judged by different LLM judges converge markedly, yielding a visibly narrower chromatic variance within each column of the heatmap.\"\n- Type: heatmap qualitative_comparison (baseline vs. UDA)\n\n---\n\n## 11. TABLE CAPTIONS (verbatim)\n\n**Table 1:** \"Inter-LLM judge score standard deviation (↓) on ArenaHard Dataset.\"\n**Table 2:** \"Inter-LLM judge score standard deviation (↓) on Human-Annotated Transfer Set.\"\n**Table 3:** \"Ablation study results on the Human-Annotated Transfer Set. Removing self-awareness features (UDA (Ablated)) further reduces score variance but critically degrades correlation with human judgments, highlighting their essential role in achieving meaningful alignment.\"\n**Table 4:** \"Analysis of Alignment with Baseline Consensus. Zero-shot transfer results on Human-Annotated Transfer Set. UDA improves average Pearson correlation by +0.1415 and reduces average MSE by 23,699.9 without retraining. We adopt the baseline's mean scores as ground-truth supervision.\"\n**Table 5:** \"ArenaHard Dataset: baseline Elo (top) vs. UDA Method (bottom)\" [Appendix: full judge-score matrices]\n**Table 6:** \"Human-Annotated Transfer Set: baseline Elo (top), UDA Method (mid), and Human score (bottom)\"\n**Table 7:** \"Full judge-score matrices for Baseline Elo, the full UDA method, and the ablated UDA variant on the Human-Annotated Transfer Set. The ablated model shows visibly lower column-wise variance but diverges more from human-aligned rankings.\"\n\n---\n\n## 12. APPENDIX CONTENT SUMMARY\n\n- A.1 Limitations and Future Work (Feature Sensitivity, Objective Tradeoffs, Scalability)\n- A.2 Additional Empirical Analysis — Loss-driven Convergence: \"Recall that the training objective (Eq. 3) enforces three complementary desiderata: (i) anchor alignment via MSE, (ii) rank fidelity via Pearson correlation, and (iii) collective consensus via global MSE.\"\n- A.3 Prompts for Answer Generation and Judging — all prompts released\n- A.4 Proofs — Complete Proof of Aggregate Bias Reduction (Theorem 1); formal mathematical setup with J = {1,…,M} judges; proof that S_UDA ≤ S_base (total absolute bias does not increase)\n- Full Judge Score Matrices (Tables 5–7)\n- Reproducibility Checklist: \"Code, model checkpoints and the Human-Annotated Transfer Set are released at [URL]\"\n\n---\n\n## KEY QUANTITATIVE FINDINGS SUMMARY\n\n| Metric | Baseline | UDA | Change |\n|---|---|---|---|\n| Inter-judge std dev (ArenaHard, avg) | 158.5 | 64.8 | −59.1% |\n| Inter-judge std dev (Human set, avg) | 193.95 | 70.97 | −63.4% |\n| Pearson corr. with human (avg) | 0.651 | 0.812 | +24.7% |\n| Self-preference deviation range | −21% to +56% | −15% to +4% | narrowed |\n| Ablated UDA std dev | — | 65.64 | −66.2% but |\n| Ablated UDA human corr. | 0.651 | 0.510 | −21.6% |\n| Consensus Pearson corr. | — | 0.89 | (uniform across judges) |\n| Pearson corr. improvement (Table 4) | — | +0.1415 | — |\n| MSE reduction (Table 4) | — | −23,699.9 | — |&lt;/result>\n&lt;usage>&lt;total_tokens>43339&lt;/total_tokens>&lt;tool_uses>26&lt;/tool_uses>&lt;duration_ms>504652&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>",
    "commandMode": "task-notification"
  },
  "type": "attachment",
  "uuid": "5b490dbe-db6b-4a35-865d-38cae32f8d88",
  "timestamp": "2026-05-21T16:47:17.934Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 129_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "5b490dbe-db6b-4a35-865d-38cae32f8d88",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---


### Runtime record

_source line 130_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill LLM judge bias research into structured skills",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e"
}
```

---
