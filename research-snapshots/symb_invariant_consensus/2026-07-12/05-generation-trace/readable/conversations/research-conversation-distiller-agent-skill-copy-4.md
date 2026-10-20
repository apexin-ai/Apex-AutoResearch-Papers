# Research conversation: 你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。 ## 核心定位 你不是在"总结论文"。你在回答：**这个研究子领域的人默认怎么做事？** - 总结 =

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/a1bafaf1-2e39-412f-94cc-d7b92935728c.jsonl`
- **Structured JSON:** [`90d22796ec0d8cb4843b.json`](../../sessions/90/90d22796ec0d8cb4843b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T13:45:30.739Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T13:45:30.739Z",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "content": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。\n\n## 核心定位\n\n你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**\n\n- 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列）\n- 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）\n\n## 执行流程\n\n### Step 1: 论文排序\n\n按 (venue 质量 × 时间近度 × 相关度) 打分，确定精读优先级。\n\n### Step 2: Layer 1 — 逐篇精读\n\n对每篇「深度精读」论文：\n\n1. 用 WebFetch 获取原文（arXiv HTML 优先 → abstract 降级）\n2. 精读 intro + experiment sections，同时关注 **contribution statement**（通常在 intro 末段）和 **limitation / future work**（通常在 conclusion 段）\n3. 用 WebFetch 获取关键 figure 图片（至少 Figure 1 + 主结果图）做视觉分析，同时关注全部 **figure/table caption** 和 **正文对 figure/table 的引用段落**\n4. 写入 `distill_tmp/{paper_key}.yaml`，schema 如下：\n\n```yaml\npaper_key: \"{key}\"\ntitle: \"...\"\nvenue: \"{venue} {year}\"\nfull_text_available: true/false\n\nresearch:\n  baselines: [name1, name2]\n  metrics: [{name: \"X\", direction: \"higher_better\"}]\n  datasets: [{name: \"Y\", size: \"...\"}]\n  ablation_dimensions: [dim1, dim2]\n  training_recipe: {optimizer: \"...\", lr: \"...\", hardware: \"...\"}\n  method_family: \"...\"\n\npositioning:\n  core_claim: \"一句话提炼该论文的核心贡献（不是 abstract 复述）\"\n  key_results: \"关键性能数字（如 ImageNet top-1: 82.3% (+1.2%), FLOPs: 4.5G (-40%)）\"\n  limitations: [\"论文自己承认的局限 1\", \"局限 2\"]\n  relation_to_us: \"competitor\"   # competitor / foundation / complementary / orthogonal\n\nnarrative:\n  story_type: \"突破局限型/化繁为简型/规模涌现型/跨界迁移型/统一框架型\"\n  hook: \"第一段如何抓注意力\"\n  tension: \"现有方法局限如何铺垫\"\n  key_insight: \"核心洞察在哪个位置、什么方式揭示\"\n  argument_chain: \"problem → ... → validation\"\n  contribution_framing: \"贡献声明的措辞和数量\"\n  intro_structure: \"段落数和每段功能\"\n  notable_technique: \"叙事上最值得学习的技巧\"\n\nfigures:\n  figure_count: 6\n  figure1:\n    type: \"motivation\"                    # motivation / method_overview / teaser_result / problem_illustration\n    description: \"图的内容描述\"\n    narrative_role: \"在论证链中的作用\"\n    design_elements: [\"对比布局\", \"颜色标注\", \"真实样例\"]\n    visual_style: \"从图片视觉分析得到的布局/配色/标注描述\"\n  result_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"bar_chart\"              # bar_chart / line_plot / heatmap / scatter / qualitative_comparison\n      what_compared: \"对比了什么\"\n      how_gain_highlighted: \"如何突出本方法的优势\"\n      design_note: \"设计上值得借鉴的点\"\n  ablation_figures:\n    - figure_id: \"Figure 6\"\n      viz_type: \"grouped_bar\"\n      dimensions_varied: [\"component A\", \"component B\"]\n      design_note: \"消融图的设计思路\"\n  figure_narrative_role: \"Figure 1 → Figure 2 → ... 的叙事流\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"                   # methods / datasets / settings\n    col_axis: \"datasets × metrics\"\n    row_organization: \"by_category\"       # by_category / by_performance / by_year / flat\n    col_organization: \"grouped_by_dataset\" # grouped_by_dataset / grouped_by_metric / flat\n    highlight_strategy: \"bold_best + underline_second\"\n    statistical_reporting: \"mean ± std across 3 runs\"\n    num_baselines: 8\n    design_note: \"表格编排上值得借鉴的点\"\n  ablation_tables:\n    - table_id: \"Table 3\"\n      what_varied: [\"component A\", \"component B\"]\n      variation_style: \"checkmark_grid\"   # checkmark_grid / delta_from_base / full_numbers\n      design_note: \"消融表的呈现思路\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"附录表放了什么\"\n    reason: \"为什么这样拆分主表和附录\"\n```\n\n对「仅摘要」论文：只填 `research` 部分，`narrative`/`figures`/`tables` 标记 `N/A`。\n\n### Step 3: Layer 2 — 跨论文归纳\n\n读取全部 Layer 1 YAML，分两个维度归纳：\n\n**Research 归纳**：\n- 统计 baseline/metric/dataset 出现频率\n- 识别方法论趋势（上升 vs 消退）\n- 提取实验设计共识\n- 竞品 claim 汇总：从各篇的 positioning.core_claim 归纳，按 relation_to_us 分组\n- 共同局限：从各篇的 positioning.limitations 交叉比对，标注出现频率\n- 研究空白：从全部论文覆盖的维度中找出交叉盲区（多数做了 X 但没做 Y）\n\n**Writing 归纳**：\n- 对比各论文叙事结构\n- 识别领域故事类型分布\n- 归纳开篇模式、张力来源、洞察呈现位置\n- 提炼可模仿的叙事策略\n- Figure 1 设计模式分布：从各篇 `figures.figure1.type` 统计，哪种最主流，设计元素共识\n- 结果可视化共识：从 `result_figures.viz_type` 统计主结果常用图表类型，gain 突出手法\n- 消融可视化偏好：从 `ablation_figures.viz_type` 统计，grouped bar / heatmap / 表格哪种主流\n- 图的叙事节奏：从 `figure_narrative_role` 归纳典型 figure 编排（motivation → method → result → ablation）\n- 主结果表编排共识：从 `tables.main_result_table` 归纳行列组织模式、分组策略、baseline 数量范围\n- 高亮与统计报告共识：从 `highlight_strategy` + `statistical_reporting` 统计领域标准做法\n- 消融表呈现偏好：从 `ablation_tables.variation_style` 统计 checkmark grid vs delta vs 完整数字\n- 图表分工模式：从 figure + table 全局看，什么结果用图、什么用表、附录放什么\n\n### Step 4: 生成 Skill 文件\n\n在指定 skill 目录下创建两个 `.skill.md` 文件。\n\n## 质量要求\n\n每条 pattern 必须标注：\n- **支持度**：N/M 篇论文\n- **来源**：至少 1 篇代表性论文 title\n- **置信度**：高（>60%）/ 中（30-60%）/ 低（<30% 但值得注意）\n\n不要输出：\n- 单篇论文的独立总结\n- 没有跨论文共识支撑的孤立观察\n- 显而易见的常识\n\n叙事策略分析（writing skill 核心）：\n- 逐篇拆解 3-5 篇论文的故事结构（故事类型、开篇钩子、张力构建、关键洞察、论证链）\n- 每个分析点引用论文中的具体措辞或结构作为证据\n- 策略建议具体到可直接模仿，不泛泛而谈\n\n## 完成标志\n\n所有工作完成后输出 `[DISTILL_DONE]`。\n\n\n## 任务参数\n\n- 项目: symb_invariant_consensus\n- Layer 1 输出目录: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/`\n- Skill 输出目录: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/`\n- 深度精读上限: 8 篇\n- 单个 Skill 字数上限: 3000 字符\n\n已有 25 篇论文的 Layer 1 缓存（在 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/` 中），无需重新分析。\n\n## 待分析论文\n\n\n\n## 执行指令\n\n1. 对每篇「深度精读」论文执行 Layer 1 分析，将结构化结果写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/{paper_key}.yaml`\n2. 对「仅摘要」论文，仅提取 research 维度（baseline/metric/dataset），写入同目录\n3. 读取全部 Layer 1 YAML（含已缓存的），执行 Layer 2 跨论文归纳\n4. 生成 `distilled-research.skill.md` 和 `distilled-writing.skill.md`，写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/`\n5. 每个 skill body 不超过 3000 字符\n6. **每个 skill 文件必须以 YAML frontmatter 开头**，格式如下：\n\n```\n---\nname: distilled-research          # 或 distilled-writing\ndescription: \"一句话描述 skill 内容\"\nscope: project\nversion: 1\ntags: [distilled, auto-generated]\ndistilled_from:\n  paper_count: <实际分析的论文总数>\n  paper_keys: [paper_key_1, paper_key_2, ...]\n  last_distilled: \"ISO8601 时间戳\"\n---\n\n（skill body 在这里）\n```\n\n缺少 frontmatter 会导致下游 status/result 命令无法正确读取蒸馏元数据。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T13:45:30.743Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T13:45:30.743Z",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

## Round 1

64 recorded events

### User

_source line 3 · 2026-05-22T13:45:30.778Z_

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

- 项目: symb_invariant_consensus
- Layer 1 输出目录: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/`
- Skill 输出目录: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/`
- 深度精读上限: 8 篇
- 单个 Skill 字数上限: 3000 字符

已有 25 篇论文的 Layer 1 缓存（在 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/` 中），无需重新分析。

## 待分析论文



## 执行指令

1. 对每篇「深度精读」论文执行 Layer 1 分析，将结构化结果写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/{paper_key}.yaml`
2. 对「仅摘要」论文，仅提取 research 维度（baseline/metric/dataset），写入同目录
3. 读取全部 Layer 1 YAML（含已缓存的），执行 Layer 2 跨论文归纳
4. 生成 `distilled-research.skill.md` 和 `distilled-writing.skill.md`，写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/`
5. 每个 skill body 不超过 3000 字符
6. **每个 skill 文件必须以 YAML frontmatter 开头**，格式如下：

```
---
name: distilled-research          # 或 distilled-writing
description: "一句话描述 skill 内容"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: <实际分析的论文总数>
  paper_keys: [paper_key_1, paper_key_2, ...]
  last_distilled: "ISO8601 时间戳"
---

（skill body 在这里）
```

缺少 frontmatter 会导致下游 status/result 命令无法正确读取蒸馏元数据。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "b83b755c-eb4a-453c-8c46-ebda2efc8337",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T13:45:30.778Z_

```json
{
  "parentUuid": "b83b755c-eb4a-453c-8c46-ebda2efc8337",
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
  "uuid": "6c84d876-4c46-458c-a9dd-bb882221a273",
  "timestamp": "2026-05-22T13:45:30.778Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T13:45:30.778Z_

```json
{
  "parentUuid": "6c84d876-4c46-458c-a9dd-bb882221a273",
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
  "uuid": "05c7f7f3-cdfe-4c20-9ff2-d912bc10b58f",
  "timestamp": "2026-05-22T13:45:30.778Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T13:45:30.778Z_

```json
{
  "parentUuid": "05c7f7f3-cdfe-4c20-9ff2-d912bc10b58f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4b567338-9f5a-4bbe-8dcc-8a24e3461cd3",
  "timestamp": "2026-05-22T13:45:30.778Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Assistant

_source line 8 · 2026-05-22T13:45:34.517Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing Layer 1 YAML files in the distill_tmp directory to understand what's already been cached, then perform Layer 2 cross-paper analysis and generate the two skill files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b567338-9f5a-4bbe-8dcc-8a24e3461cd3",
  "isSidechain": false,
  "requestId": "req_011CbHi4PjtcW5W3RgNFU28H",
  "type": "assistant",
  "uuid": "ca1f0e89-237e-452c-801c-676240f2c7fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjUwBkuSy1ZQsF5RNpctD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16988,
      "cache_read_input_tokens": 11846,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 183,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 16988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16988
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

_source line 9 · 2026-05-22T13:45:35.001Z_

Let me read the existing Layer 1 cache files to perform cross-paper analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca1f0e89-237e-452c-801c-676240f2c7fc",
  "isSidechain": false,
  "requestId": "req_011CbHi4PjtcW5W3RgNFU28H",
  "type": "assistant",
  "uuid": "0777fc39-c13a-40ba-b06f-c239e370b978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjUwBkuSy1ZQsF5RNpctD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16988,
      "cache_read_input_tokens": 11846,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 183,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 16988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16988
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

_source line 10 · 2026-05-22T13:45:35.714Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PcNHCZbyFEUHBrjab5RMPH`</summary>

```json
{
  "pattern": "*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0777fc39-c13a-40ba-b06f-c239e370b978",
  "isSidechain": false,
  "requestId": "req_011CbHi4PjtcW5W3RgNFU28H",
  "type": "assistant",
  "uuid": "27311982-354b-41c1-b003-ea59b11ce158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjUwBkuSy1ZQsF5RNpctD2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16988,
      "cache_read_input_tokens": 11846,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 183,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 16988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16988
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

_source line 11 · 2026-05-22T13:45:35.733Z_

<details><summary>↩ Tool result · `toolu_01PcNHCZbyFEUHBrjab5RMPH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/du2023improving.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/chen2024usc.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/taubenfeld2025cisc.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dsc2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/fover2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/constraintllm2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/llm_meets_cp2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/satbench2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/logicagent2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2026dylos.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/aristotle2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/qi2025symbolic_provers.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dissecting2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/crest2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/khan2024debating.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/olausson2023linc.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/pan2023logiclm.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/snell2025scaling_tts.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/multi_path_plan2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2024mathshepherd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/hosseini2024vstar.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/huang2024selfcorrect.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2023sc.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/li2023diverse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/rc2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/ye2024satlm.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2024symbcot.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xiong2024uncertainty.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27311982-354b-41c1-b003-ea59b11ce158",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "748b1e64-493e-4795-a520-dcd05a6fea6f",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/du2023improving.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/chen2024usc.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/taubenfeld2025cisc.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dsc2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/fover2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/constraintllm2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/llm_meets_cp2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/satbench2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/logicagent2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2026dylos.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/aristotle2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/qi2025symbolic_provers.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dissecting2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/crest2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/khan2024debating.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/olausson2023linc.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/pan2023logiclm.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/snell2025scaling_tts.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/multi_path_plan2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2024mathshepherd.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/hosseini2024vstar.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/huang2024selfcorrect.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2023sc.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/li2023diverse.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/rc2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/ye2024satlm.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2024symbcot.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xiong2024uncertainty.yaml"
    ],
    "durationMs": 7,
    "numFiles": 28,
    "truncated": false
  },
  "sourceToolAssistantUUID": "27311982-354b-41c1-b003-ea59b11ce158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "748b1e64-493e-4795-a520-dcd05a6fea6f",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Assistant

_source line 14 · 2026-05-22T13:45:38.678Z_

28 YAML files cached. Let me read them in batches to extract the cross-paper patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "748b1e64-493e-4795-a520-dcd05a6fea6f",
  "isSidechain": false,
  "requestId": "req_011CbHi4ku7bcWDks6AfNfL4",
  "type": "assistant",
  "uuid": "03394e59-c9a7-45b2-8005-78393aef28a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj7TffKCdpo57gJ6yeaJPQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 28834,
      "output_tokens": 1789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1789,
          "cache_read_input_tokens": 28834,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1415
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

_source line 15 · 2026-05-22T13:45:43.485Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AywKJRiiXRtgRBe9WyDF2s`</summary>

```json
{
  "description": "Read first batch of YAMLs",
  "subagent_type": "Explore",
  "prompt": "Read the following YAML files in full and report their complete contents back to me. These are paper distillation files I need to analyze:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/du2023improving.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/chen2024usc.yaml\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/taubenfeld2025cisc.yaml\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dsc2025.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/fover2025.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/constraintllm2025.yaml\n7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/llm_meets_cp2025.yaml\n\nRead all files completely and reproduce their content exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03394e59-c9a7-45b2-8005-78393aef28a2",
  "isSidechain": false,
  "requestId": "req_011CbHi4ku7bcWDks6AfNfL4",
  "type": "assistant",
  "uuid": "4a123e10-62eb-4718-8c00-efc805cbbf4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj7TffKCdpo57gJ6yeaJPQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 28834,
      "output_tokens": 1789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1789,
          "cache_read_input_tokens": 28834,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1415
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

_source line 16 · 2026-05-22T13:45:46.422Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VejfPWg9M28SWGA3aWoJ1i`</summary>

```json
{
  "description": "Read second batch of YAMLs",
  "subagent_type": "Explore",
  "prompt": "Read the following YAML files in full and report their complete contents back to me. These are paper distillation files I need to analyze:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/satbench2025.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/logicagent2025.yaml\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2026dylos.yaml\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/aristotle2025.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/qi2025symbolic_provers.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dissecting2025.yaml\n7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/crest2025.yaml\n\nRead all files completely and reproduce their content exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a123e10-62eb-4718-8c00-efc805cbbf4c",
  "isSidechain": false,
  "requestId": "req_011CbHi4ku7bcWDks6AfNfL4",
  "type": "assistant",
  "uuid": "fc4fa99b-6528-446e-929a-a9084a806af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj7TffKCdpo57gJ6yeaJPQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 28834,
      "output_tokens": 1789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1789,
          "cache_read_input_tokens": 28834,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1415
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

_source line 17 · 2026-05-22T13:45:50.193Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SxU8GxMguHQM84juVp2hNm`</summary>

```json
{
  "description": "Read third batch of YAMLs",
  "subagent_type": "Explore",
  "prompt": "Read the following YAML files in full and report their complete contents back to me. These are paper distillation files I need to analyze:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/khan2024debating.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/olausson2023linc.yaml\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/pan2023logiclm.yaml\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/snell2025scaling_tts.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/multi_path_plan2025.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2024mathshepherd.yaml\n7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/hosseini2024vstar.yaml\n\nRead all files completely and reproduce their content exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc4fa99b-6528-446e-929a-a9084a806af4",
  "isSidechain": false,
  "requestId": "req_011CbHi4ku7bcWDks6AfNfL4",
  "type": "assistant",
  "uuid": "c0a80f14-8f0b-4d80-a5a2-f89e496177c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj7TffKCdpo57gJ6yeaJPQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 28834,
      "output_tokens": 1789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1789,
          "cache_read_input_tokens": 28834,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1415
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

_source line 18 · 2026-05-22T13:45:53.891Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Dw66TbmZZerCBdvJE1w1oL`</summary>

```json
{
  "description": "Read fourth batch of YAMLs",
  "subagent_type": "Explore",
  "prompt": "Read the following YAML files in full and report their complete contents back to me. These are paper distillation files I need to analyze:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/huang2024selfcorrect.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2023sc.yaml\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/li2023diverse.yaml\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/rc2025.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/ye2024satlm.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2024symbcot.yaml\n7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xiong2024uncertainty.yaml\n\nRead all files completely and reproduce their content exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a80f14-8f0b-4d80-a5a2-f89e496177c2",
  "isSidechain": false,
  "requestId": "req_011CbHi4ku7bcWDks6AfNfL4",
  "type": "assistant",
  "uuid": "a5fa8656-1a4c-4eff-ae13-797ef6025d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj7TffKCdpo57gJ6yeaJPQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 28834,
      "output_tokens": 1789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1415,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1789,
          "cache_read_input_tokens": 28834,
          "cache_creation_input_tokens": 1415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1415
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

_source line 19 · 2026-05-22T13:46:09.967Z_

<details><summary>↩ Tool result · `toolu_01AywKJRiiXRtgRBe9WyDF2s`</summary>

````text
 Here are the complete contents of all seven YAML files:

## 1. du2023improving.yaml

```yaml
paper_key: "du2023improving"
title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["single-agent CoT", "self-consistency", "self-verification"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "factual validity", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "N/A"}
    - {name: "math reasoning benchmarks", size: "N/A"}
    - {name: "biographical QA", size: "N/A"}
  ablation_dimensions: ["number of agents", "number of debate rounds"]
  training_recipe: {info: "black-box prompting, no training"}
  method_family: "multi-agent debate"

positioning:
  core_claim: "Multiple LLM instances debating over multiple rounds significantly enhances mathematical/strategic reasoning and factual validity compared to single-agent approaches"
  key_results: "Significant improvements in mathematical and strategic reasoning; reduced hallucinations and fallacious answers"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 2. chen2024usc.yaml

```yaml
paper_key: "chen2024usc"
title: "Universal Self-Consistency for Large Language Model Generation"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["standard self-consistency (majority voting)", "execution-based voting"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "consistency", direction: "higher_better"}
  datasets:
    - {name: "mathematical reasoning benchmarks", size: "N/A"}
    - {name: "code generation benchmarks", size: "N/A"}
    - {name: "long-context summarization", size: "N/A"}
    - {name: "open-ended QA", size: "N/A"}
  ablation_dimensions: ["task type", "number of samples"]
  training_recipe: {info: "prompting-based, no training"}
  method_family: "self-consistency"

positioning:
  core_claim: "LLMs themselves can select the most consistent answer among multiple candidates, extending self-consistency to free-form generation tasks where majority voting is inapplicable"
  key_results: "Matches standard self-consistency on math; matches execution-based voting on code generation without execution access"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 3. taubenfeld2025cisc.yaml

```yaml
paper_key: "taubenfeld2025cisc"
title: "Confidence Improves Self-Consistency in LLMs"
venue: "ACL Findings 2025"
full_text_available: false

research:
  baselines: ["standard self-consistency (unweighted majority voting)"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "sample efficiency (paths needed)", direction: "lower_better"}
  datasets:
    - {name: "4 reasoning datasets (unspecified)", size: "N/A"}
  ablation_dimensions: ["confidence scoring method", "number of sampled paths", "model choice"]
  training_recipe: {info: "prompting-based, no training; confidence scores from model logits"}
  method_family: "confidence-weighted self-consistency"

positioning:
  core_claim: "Weighted majority voting using model confidence scores (CISC) identifies correct answers with >40% fewer reasoning paths than standard self-consistency across 9 models and 4 datasets"
  key_results: ">40% reduction in sampled paths on average; outperforms standard self-consistency across 9 models and 4 datasets"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 4. dsc2025.yaml

```yaml
paper_key: "dsc2025"
title: "Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning"
venue: "NAACL Findings 2025"
full_text_available: false

research:
  baselines: ["Adaptive Self-Consistency (ASC)", "Early-stopping Self-Consistency (ESC)", "standard self-consistency"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "inference cost (number of samples)", direction: "lower_better"}
  datasets:
    - {name: "arithmetic reasoning benchmarks", size: "N/A"}
    - {name: "commonsense reasoning benchmarks", size: "N/A"}
    - {name: "symbolic reasoning benchmarks", size: "N/A"}
  ablation_dimensions: ["prior vs posterior difficulty estimation", "batch-level vs instance-level allocation"]
  training_recipe: {info: "prompting-based, no training; difficulty estimation from batch statistics"}
  method_family: "adaptive self-consistency"

positioning:
  core_claim: "Leveraging both prior and posterior difficulty information at the batch level enables adaptive inference resource allocation that significantly reduces self-consistency cost while maintaining comparable performance"
  key_results: "Consistently surpasses ASC and ESC in cost efficiency by a significant margin with comparable accuracy across 6 benchmarks"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 5. fover2025.yaml

```yaml
paper_key: "fover2025"
title: "FoVer: Efficient PRM Training Data Synthesis via Formal Verification"
venue: "ACL Findings 2026"
full_text_available: false

research:
  baselines: ["PRMs trained on human-annotated data", "PRMs trained on LLM-generated labels"]
  metrics:
    - {name: "accuracy on reasoning benchmarks", direction: "higher_better"}
    - {name: "step-level error detection", direction: "higher_better"}
  datasets:
    - {name: "12 reasoning benchmarks (math, logic, NLI, BBH)", size: "N/A"}
    - {name: "formal logic tasks", size: "N/A"}
    - {name: "theorem proving tasks", size: "N/A"}
  ablation_dimensions: ["formal verification tool (Z3 vs Isabelle)", "training data domain"]
  training_recipe: {info: "fine-tuning PRMs on synthesized step-level labels from Z3/Isabelle formal verification"}
  method_family: "formal verification for process reward models"

positioning:
  core_claim: "Formal verification tools (Z3, Isabelle) can automatically synthesize high-quality PRM training data with step-level error labels, improving reasoning across both formal and informal tasks without human annotation"
  key_results: "Improves PRMs on math, logic, NLI, and BBH benchmarks; generalizes from formal to informal reasoning"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 6. constraintllm2025.yaml

```yaml
paper_key: "constraintllm2025"
title: "ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming"
venue: "EMNLP 2025"
full_text_available: false

research:
  baselines: ["general-purpose LLMs on CP tasks"]
  metrics:
    - {name: "solving accuracy", direction: "higher_better"}
  datasets:
    - {name: "IndusCP", size: "140 industrial-level tasks"}
    - {name: "existing CP benchmarks", size: "N/A"}
  ablation_dimensions: ["Constraint-Aware Retrieval Module", "Tree-of-Thoughts framework", "guided self-correction"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", info: "multi-instruction supervised fine-tuning on open-source LLM"}
  method_family: "neuro-symbolic constraint programming"

positioning:
  core_claim: "First LLM specifically designed for CP modeling, combining constraint-aware retrieval with Tree-of-Thoughts and self-correction to achieve 2x improvement over baselines on industrial-level CP tasks"
  key_results: "State-of-the-art solving accuracy across multiple benchmarks; 2x improvement over baselines on IndusCP"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 7. llm_meets_cp2025.yaml

```yaml
paper_key: "llm_meets_cp2025"
title: "Large Language Model Meets Constraint Propagation"
venue: "IJCAI 2025"
full_text_available: false

research:
  baselines: ["standard LLM text generation", "original GenCP"]
  metrics:
    - {name: "constraint satisfaction rate", direction: "higher_better"}
    - {name: "generation feasibility", direction: "higher_better"}
    - {name: "LLM inference efficiency", direction: "higher_better"}
  datasets:
    - {name: "COLLIE benchmarks", size: "N/A"}
  ablation_dimensions: ["MLM integration for domain preview", "bidirectional vs unidirectional propagation"]
  training_recipe: {info: "no training; inference-time constraint satisfaction via Masked Language Models"}
  method_family: "constraint programming + language models"

positioning:
  core_claim: "Formulating constrained text generation as a CSP and integrating Masked Language Models for bidirectional constraint propagation significantly improves generation quality under strict content constraints"
  key_results: "Significant improvement on COLLIE benchmarks; more efficient LLM inference usage for constrained generation"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "4a123e10-62eb-4718-8c00-efc805cbbf4c",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "4b734943-42b2-4b13-b742-acbb91a488ce",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read the following YAML files in full and report their complete contents back to me. These are paper distillation files I need to analyze:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/du2023improving.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/chen2024usc.yaml\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/taubenfeld2025cisc.yaml\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dsc2025.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/fover2025.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/constraintllm2025.yaml\n7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/llm_meets_cp2025.yaml\n\nRead all files completely and reproduce their content exactly.",
    "agentId": "ae38f0aaf6d6e5a7e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": " Here are the complete contents of all seven YAML files:\n\n## 1. du2023improving.yaml\n\n```yaml\npaper_key: \"du2023improving\"\ntitle: \"Improving Factuality and Reasoning in Language Models through Multiagent Debate\"\nvenue: \"ICML 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"single-agent CoT\", \"self-consistency\", \"self-verification\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"factual validity\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM8K\", size: \"N/A\"}\n    - {name: \"math reasoning benchmarks\", size: \"N/A\"}\n    - {name: \"biographical QA\", size: \"N/A\"}\n  ablation_dimensions: [\"number of agents\", \"number of debate rounds\"]\n  training_recipe: {info: \"black-box prompting, no training\"}\n  method_family: \"multi-agent debate\"\n\npositioning:\n  core_claim: \"Multiple LLM instances debating over multiple rounds significantly enhances mathematical/strategic reasoning and factual validity compared to single-agent approaches\"\n  key_results: \"Significant improvements in mathematical and strategic reasoning; reduced hallucinations and fallacious answers\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 2. chen2024usc.yaml\n\n```yaml\npaper_key: \"chen2024usc\"\ntitle: \"Universal Self-Consistency for Large Language Model Generation\"\nvenue: \"ICML 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"standard self-consistency (majority voting)\", \"execution-based voting\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"consistency\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"mathematical reasoning benchmarks\", size: \"N/A\"}\n    - {name: \"code generation benchmarks\", size: \"N/A\"}\n    - {name: \"long-context summarization\", size: \"N/A\"}\n    - {name: \"open-ended QA\", size: \"N/A\"}\n  ablation_dimensions: [\"task type\", \"number of samples\"]\n  training_recipe: {info: \"prompting-based, no training\"}\n  method_family: \"self-consistency\"\n\npositioning:\n  core_claim: \"LLMs themselves can select the most consistent answer among multiple candidates, extending self-consistency to free-form generation tasks where majority voting is inapplicable\"\n  key_results: \"Matches standard self-consistency on math; matches execution-based voting on code generation without execution access\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 3. taubenfeld2025cisc.yaml\n\n```yaml\npaper_key: \"taubenfeld2025cisc\"\ntitle: \"Confidence Improves Self-Consistency in LLMs\"\nvenue: \"ACL Findings 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"standard self-consistency (unweighted majority voting)\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"sample efficiency (paths needed)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"4 reasoning datasets (unspecified)\", size: \"N/A\"}\n  ablation_dimensions: [\"confidence scoring method\", \"number of sampled paths\", \"model choice\"]\n  training_recipe: {info: \"prompting-based, no training; confidence scores from model logits\"}\n  method_family: \"confidence-weighted self-consistency\"\n\npositioning:\n  core_claim: \"Weighted majority voting using model confidence scores (CISC) identifies correct answers with >40% fewer reasoning paths than standard self-consistency across 9 models and 4 datasets\"\n  key_results: \">40% reduction in sampled paths on average; outperforms standard self-consistency across 9 models and 4 datasets\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 4. dsc2025.yaml\n\n```yaml\npaper_key: \"dsc2025\"\ntitle: \"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning\"\nvenue: \"NAACL Findings 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"Adaptive Self-Consistency (ASC)\", \"Early-stopping Self-Consistency (ESC)\", \"standard self-consistency\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"inference cost (number of samples)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"arithmetic reasoning benchmarks\", size: \"N/A\"}\n    - {name: \"commonsense reasoning benchmarks\", size: \"N/A\"}\n    - {name: \"symbolic reasoning benchmarks\", size: \"N/A\"}\n  ablation_dimensions: [\"prior vs posterior difficulty estimation\", \"batch-level vs instance-level allocation\"]\n  training_recipe: {info: \"prompting-based, no training; difficulty estimation from batch statistics\"}\n  method_family: \"adaptive self-consistency\"\n\npositioning:\n  core_claim: \"Leveraging both prior and posterior difficulty information at the batch level enables adaptive inference resource allocation that significantly reduces self-consistency cost while maintaining comparable performance\"\n  key_results: \"Consistently surpasses ASC and ESC in cost efficiency by a significant margin with comparable accuracy across 6 benchmarks\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 5. fover2025.yaml\n\n```yaml\npaper_key: \"fover2025\"\ntitle: \"FoVer: Efficient PRM Training Data Synthesis via Formal Verification\"\nvenue: \"ACL Findings 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"PRMs trained on human-annotated data\", \"PRMs trained on LLM-generated labels\"]\n  metrics:\n    - {name: \"accuracy on reasoning benchmarks\", direction: \"higher_better\"}\n    - {name: \"step-level error detection\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"12 reasoning benchmarks (math, logic, NLI, BBH)\", size: \"N/A\"}\n    - {name: \"formal logic tasks\", size: \"N/A\"}\n    - {name: \"theorem proving tasks\", size: \"N/A\"}\n  ablation_dimensions: [\"formal verification tool (Z3 vs Isabelle)\", \"training data domain\"]\n  training_recipe: {info: \"fine-tuning PRMs on synthesized step-level labels from Z3/Isabelle formal verification\"}\n  method_family: \"formal verification for process reward models\"\n\npositioning:\n  core_claim: \"Formal verification tools (Z3, Isabelle) can automatically synthesize high-quality PRM training data with step-level error labels, improving reasoning across both formal and informal tasks without human annotation\"\n  key_results: \"Improves PRMs on math, logic, NLI, and BBH benchmarks; generalizes from formal to informal reasoning\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 6. constraintllm2025.yaml\n\n```yaml\npaper_key: \"constraintllm2025\"\ntitle: \"ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming\"\nvenue: \"EMNLP 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"general-purpose LLMs on CP tasks\"]\n  metrics:\n    - {name: \"solving accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"IndusCP\", size: \"140 industrial-level tasks\"}\n    - {name: \"existing CP benchmarks\", size: \"N/A\"}\n  ablation_dimensions: [\"Constraint-Aware Retrieval Module\", \"Tree-of-Thoughts framework\", \"guided self-correction\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\", info: \"multi-instruction supervised fine-tuning on open-source LLM\"}\n  method_family: \"neuro-symbolic constraint programming\"\n\npositioning:\n  core_claim: \"First LLM specifically designed for CP modeling, combining constraint-aware retrieval with Tree-of-Thoughts and self-correction to achieve 2x improvement over baselines on industrial-level CP tasks\"\n  key_results: \"State-of-the-art solving accuracy across multiple benchmarks; 2x improvement over baselines on IndusCP\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 7. llm_meets_cp2025.yaml\n\n```yaml\npaper_key: \"llm_meets_cp2025\"\ntitle: \"Large Language Model Meets Constraint Propagation\"\nvenue: \"IJCAI 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"standard LLM text generation\", \"original GenCP\"]\n  metrics:\n    - {name: \"constraint satisfaction rate\", direction: \"higher_better\"}\n    - {name: \"generation feasibility\", direction: \"higher_better\"}\n    - {name: \"LLM inference efficiency\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"COLLIE benchmarks\", size: \"N/A\"}\n  ablation_dimensions: [\"MLM integration for domain preview\", \"bidirectional vs unidirectional propagation\"]\n  training_recipe: {info: \"no training; inference-time constraint satisfaction via Masked Language Models\"}\n  method_family: \"constraint programming + language models\"\n\npositioning:\n  core_claim: \"Formulating constrained text generation as a CSP and integrating Masked Language Models for bidirectional constraint propagation significantly improves generation quality under strict content constraints\"\n  key_results: \"Significant improvement on COLLIE benchmarks; more efficient LLM inference usage for constrained generation\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```"
      }
    ],
    "totalDurationMs": 26477,
    "totalTokens": 25267,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 8,
      "cache_creation_input_tokens": 4493,
      "cache_read_input_tokens": 18125,
      "output_tokens": 2641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4493
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8,
          "output_tokens": 2641,
          "cache_read_input_tokens": 18125,
          "cache_creation_input_tokens": 4493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4493,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "4a123e10-62eb-4718-8c00-efc805cbbf4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "4b734943-42b2-4b13-b742-acbb91a488ce",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Tool result

_source line 22 · 2026-05-22T13:46:42.031Z_

<details><summary>↩ Tool result · `toolu_01SxU8GxMguHQM84juVp2hNm`</summary>

````text
 I've successfully read all seven YAML files. Here is their complete content:

## 1. khan2024debating.yaml

```yaml
paper_key: "khan2024debating"
title: "Debating with More Persuasive LLMs Leads to More Truthful Answers"
venue: "ICML 2024"
full_text_available: true

research:
  baselines: ["Naive judge", "Consultancy (correct)", "Consultancy (incorrect)", "Non-interactive debate"]
  metrics:
    - {name: "judge_accuracy", direction: "higher_better"}
    - {name: "Elo_rating", direction: "higher_better"}
  datasets:
    - {name: "QuALITY", size: "reading comprehension"}
  ablation_dimensions: ["protocol_type", "interactivity", "debater_model", "judge_model", "BoN_size", "quote_system", "round_count", "word_limits", "majority_voting", "few_shot_count", "finetuning_data_type", "human_vs_LLM_judges", "persuasiveness_optimization"]
  training_recipe: {optimizer: "BoN + RL", lr: "N/A", hardware: "N/A"}
  method_family: "multi-agent debate for AI safety"

positioning:
  core_claim: "Adversarial debate between LLM experts with persuasiveness optimization lets weaker judges identify truth better than non-adversarial consultancy"
  key_results: "Debate: 88% human / 76% LLM accuracy vs Consultancy: 78%/54% vs Naive: 60%/48%"
  limitations:
    - "Information asymmetry only (not reasoning gap)"
    - "RLHF-honest models only"
    - "Quote verification dependency"
    - "Single dataset (QuALITY)"
  relation_to_us: "complementary"

narrative:
  story_type: "突破局限型"
  hook: "Scalable oversight — how do we verify AI behavior when it exceeds human capability?"
  tension: "Alignment techniques depend on human labels, but humans can't label superhuman behavior"
  key_insight: "Figures 3-4 mirror pair — persuasiveness helps debate (correct debater gains advantage) but hurts consultancy (incorrect consultant becomes more persuasive)"
  argument_chain: "alignment crisis → debate as theoretical solution → empirical setup with LLM proxy → 9 cumulative insights → persuasiveness as unsupervised training signal"
  contribution_framing: "Framed as 'insights' rather than 'contributions' — 9 numbered insights for cumulative evidence"
  intro_structure: "5 paragraphs: (1) scalable oversight problem, (2) debate proposal recap, (3) experimental approach, (4) key findings preview, (5) implications"
  notable_technique: "Numbered Insight 1-9 structure replaces traditional contribution list; Figure 3-4 mirror design as argumentative backbone"

figures:
  figure_count: 17
  figure1:
    type: "method_overview"
    description: "Debate vs consultancy protocol comparison"
    narrative_role: "Establishes the two paradigms being compared"
    design_elements: ["side-by-side protocols", "agent roles", "information flow"]
    visual_style: "Schematic with two parallel protocol diagrams"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "bar_chart"
      what_compared: "Judge accuracy across protocols"
      how_gain_highlighted: "Debate consistently above consultancy"
      design_note: "Clear protocol comparison"
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Elo rating vs persuasiveness optimization for debate"
      how_gain_highlighted: "Correct-answer Elo grows with optimization"
      design_note: "Mirror pair with Figure 4 — debate's mechanism"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Elo rating vs persuasiveness optimization for consultancy"
      how_gain_highlighted: "Incorrect consultant Elo grows — consultancy breaks"
      design_note: "Mirror with Fig3 showing opposite effect"
  ablation_figures:
    - figure_id: "Figures 5-17"
      viz_type: "mixed"
      dimensions_varied: ["13 ablation dimensions"]
      design_note: "Massive ablation suite — all visual, no tables"
  figure_narrative_role: "Fig1(protocol) → Fig2(main result) → Fig3-4(mechanism mirror) → Fig5-17(extensive ablations) — remarkably figure-heavy, only 1 table"

tables:
  table_count: 1
  main_result_table:
    table_id: "Table 1"
    row_axis: "definitions"
    col_axis: "N/A"
    row_organization: "flat"
    col_organization: "flat"
    highlight_strategy: "N/A"
    statistical_reporting: "N/A"
    num_baselines: 0
    design_note: "Definitional table only — all quantitative results are figures"
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Additional experimental details"
    reason: "All main results presented visually"
```

## 2. olausson2023linc.yaml

```yaml
paper_key: "olausson2023linc"
title: "LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers"
venue: "EMNLP 2023"
full_text_available: true

research:
  baselines: ["Naive (direct)", "Scratchpad (FOL gen + LLM judge)", "CoT"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "ProofWriter", size: "OOD split"}
    - {name: "FOLIO", size: "204"}
  ablation_dimensions: ["K_majority_vote", "model_type", "proof_depth"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "neurosymbolic (LLM → FOL → Prover9)"

positioning:
  core_claim: "Two-stage LLM-to-FOL-to-Prover9 pipeline with majority vote achieves near-perfect accuracy on synthetic FOL tasks and maintains robustness across proof depths"
  key_results: "ProofWriter: StarCoder++ LINC 82.1% vs 37.8% best baseline; GPT-3.5 LINC 96.4%; GPT-4 LINC 98.3%. FOLIO: gains for smaller models, not significant for GPT-4"
  limitations:
    - "FOL is lossy for naturalistic language"
    - "Scalability unclear with more premises"
    - "FOL expressiveness insufficient for higher-order/non-classical logic"
  relation_to_us: "foundation"

narrative:
  story_type: "跨界迁移型"
  hook: "LLMs struggle with multi-step deduction despite general language understanding"
  tension: "CoT provides reasoning steps but can't guarantee logical soundness"
  key_insight: "Section 3 — the Scratchpad baseline isolates the prover's contribution: generating FOL alone (without symbolic execution) doesn't help"
  argument_chain: "LLM deduction weakness → separate understanding from reasoning → LLM parses, prover reasons → Scratchpad control proves prover is key → depth analysis confirms robustness"
  contribution_framing: "2 contributions: LINC system, Scratchpad diagnostic baseline"
  intro_structure: "4 paragraphs: (1) LLM reasoning gap, (2) neurosymbolic opportunity, (3) LINC and Scratchpad, (4) key findings"
  notable_technique: "Scratchpad as diagnostic baseline — isolates the symbolic prover's causal contribution beyond just generating FOL"

figures:
  figure_count: 5
  figure1:
    type: "method_overview"
    description: "LINC pipeline: NL → LLM → FOL → Prover9 → answer, with K-way majority vote"
    narrative_role: "Establishes the two-stage architecture"
    design_elements: ["pipeline flow", "LLM and Prover9 components", "majority vote aggregation"]
    visual_style: "Left-to-right pipeline diagram"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "bar_chart"
      what_compared: "Methods across models on ProofWriter and FOLIO"
      how_gain_highlighted: "LINC bars clearly above baselines"
      design_note: "Grouped by model, color by method"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Accuracy across proof depths (0-5)"
      how_gain_highlighted: "LINC maintains near-perfect accuracy while baselines degrade"
      design_note: "Strongest evidence for robustness — depth-accuracy curves"
    - figure_id: "Figure 5"
      viz_type: "qualitative_comparison"
      what_compared: "Error types: LINC vs CoT"
      how_gain_highlighted: "Only 21/74 errors shared — methods are complementary"
      design_note: "Error analysis Venn diagram / taxonomy"
  ablation_figures: []
  figure_narrative_role: "Fig1(pipeline) → Fig2(FOL examples) → Fig3(main results bars) → Fig4(depth analysis) → Fig5(error analysis)"

tables:
  table_count: 0
  main_result_table:
    table_id: "N/A"
    row_axis: "N/A"
    col_axis: "N/A"
    row_organization: "N/A"
    col_organization: "N/A"
    highlight_strategy: "N/A"
    statistical_reporting: "p-values for significance"
    num_baselines: 3
    design_note: "No tables — all results presented as bar charts and line plots. Unusual but effective given small experimental grid"
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Prompt templates, FOL examples, additional error analysis"
    reason: "Qualitative content doesn't fit tabular format"
```

## 3. pan2023logiclm.yaml

```yaml
paper_key: "pan2023logiclm"
title: "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning"
venue: "EMNLP Findings 2023"
full_text_available: true

research:
  baselines: ["Standard Prompting", "CoT", "CoT-SC"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "Exe_Rate", direction: "higher_better"}
  datasets:
    - {name: "PrOntoQA", size: "500"}
    - {name: "ProofWriter", size: "600"}
    - {name: "FOLIO", size: "204"}
    - {name: "LogicalDeduction", size: "300"}
    - {name: "AR-LSAT", size: "230"}
  ablation_dimensions: ["self_refinement", "solver_type", "model_type", "problem_type"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "LLM + symbolic solver (Pyke/Prover9/python-constraint/Z3)"

positioning:
  core_claim: "Reframing LLM's role from 'solving' to 'representing' — LLM formulates problems symbolically, dedicated solvers execute reasoning, with self-refinement for invalid formulations"
  key_results: "+39.2% over standard prompting, +18.4% over CoT (GPT-3.5); GPT-4: PrOntoQA 83.2, ProofWriter 79.66, FOLIO 78.92, LogicalDeduction 87.63, AR-LSAT 43.04"
  limitations:
    - "Low Exe_Rate on complex problems (FOLIO 79.9%, AR-LSAT 32.6% with GPT-4)"
    - "Self-refinement fixes grammar but not semantics"
    - "Formalization bottleneck on naturalistic language"
  relation_to_us: "foundation"

narrative:
  story_type: "跨界迁移型"
  hook: "LLMs can understand language but fail at rigorous logical reasoning"
  tension: "Prompting strategies improve reasoning but can't guarantee faithfulness"
  key_insight: "Section 3 — separating 'understanding' (LLM) from 'reasoning' (solver) plays to each component's strength"
  argument_chain: "LLM reasoning unfaithful → separate understanding from reasoning → LLM formulates + solver executes → self-refinement handles errors → 5-dataset validation"
  contribution_framing: "3 contributions: framework, self-refinement mechanism, comprehensive evaluation"
  intro_structure: "5 paragraphs: (1) LLM reasoning promise/limitations, (2) faithfulness problem, (3) Logic-LM framework, (4) contributions, (5) paper structure"
  notable_technique: "Reframing the LLM's role from 'solver' to 'translator' — rhetorically powerful simplification"

figures:
  figure_count: 4
  figure1:
    type: "method_overview"
    description: "Logic-LM pipeline: Problem Formulation → Symbolic Reasoning → Result Interpretation, with self-refinement loop"
    narrative_role: "Establishes the three-stage architecture with refinement"
    design_elements: ["pipeline flow", "self-refinement loop arrow", "4 solver icons"]
    visual_style: "Flowchart with feedback loop"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Accuracy across reasoning depths"
      how_gain_highlighted: "Logic-LM advantage grows with depth (widening gap at depth-5)"
      design_note: "Depth analysis showing symbolic reasoning's advantage on harder problems"
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "bar_chart"
      dimensions_varied: ["with/without self-refinement", "solver_type"]
      design_note: "Isolates self-refinement contribution"
  figure_narrative_role: "Fig1(pipeline) → Fig2(example) → Fig3(depth analysis) → Fig4(ablation)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × accuracy"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "single run"
    num_baselines: 3
    design_note: "Clean comparison with Exe_Rate reported alongside accuracy"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["self_refinement", "error_type"]
      variation_style: "full_numbers"
      design_note: "Breaks down Exe_Rate improvement by error category"
  supplementary_tables:
    in_appendix: true
    content: "Prompt templates, solver-specific results, error examples"
    reason: "Detailed error analysis too long for main text"
```

## 4. snell2025scaling_tts.yaml

```yaml
paper_key: "snell2025scaling_tts"
title: "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters"
venue: "ICLR 2025 (Oral)"
full_text_available: false

research:
  baselines: ["greedy decoding", "majority voting", "best-of-N", "reward-model reranking"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "compute_efficiency", direction: "higher_better"}
  datasets:
    - {name: "MATH", size: "500"}
    - {name: "GSM8K", size: "1319"}
  ablation_dimensions: ["compute_budget", "search_strategy", "verifier_type", "model_scale"]
  training_recipe: {info: "process reward models for verification"}
  method_family: "test-time compute scaling"

positioning:
  core_claim: "Optimal allocation of test-time compute (search + verification) can match or exceed 14x larger models"
  key_results: "Smaller model + optimal test-time compute matches 14x larger model on MATH"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 5. multi_path_plan2025.yaml

```yaml
paper_key: "multi_path_plan2025"
title: "Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines: ["CoT", "SC-CoT", "ToT", "plan-then-solve"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "MATH", size: "500"}
    - {name: "ARC-Challenge", size: "2590"}
  ablation_dimensions: ["num_paths", "aggregation_strategy", "plan_granularity"]
  training_recipe: {info: "N/A"}
  method_family: "multi-path reasoning aggregation"

positioning:
  core_claim: "Aggregating multiple reasoning plans before execution improves long chain-of-thought reasoning"
  key_results: "N/A"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 6. wang2024mathshepherd.yaml

```yaml
paper_key: "wang2024mathshepherd"
title: "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations"
venue: "ACL 2024"
full_text_available: false

research:
  baselines: ["majority voting", "ORM (outcome reward model)", "PRM (process reward model)"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "MATH", size: "500"}
  ablation_dimensions: ["verification_granularity", "reward_model_size", "num_samples"]
  training_recipe: {info: "automated step-level annotation via completion-based verification"}
  method_family: "process reward model / step-level verification"

positioning:
  core_claim: "Automated step-level verification annotations (without human labels) enable process reward models that outperform outcome-only verification"
  key_results: "GSM8K: 84.1% → 93.4% with Math-Shepherd PRM verification"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 7. hosseini2024vstar.yaml

```yaml
paper_key: "hosseini2024vstar"
title: "V-STaR: Training Verifiers for Self-Taught Reasoners"
venue: "NeurIPS 2024"
full_text_available: false

research:
  baselines: ["STaR", "REST-EM", "majority_voting", "ORM"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "MATH", size: "500"}
    - {name: "ARC-Challenge", size: "2590"}
  ablation_dimensions: ["verifier_training_data", "iteration_count", "generator_vs_verifier_scaling"]
  training_recipe: {info: "iterative self-training with DPO verifier"}
  method_family: "self-training with verifier"

positioning:
  core_claim: "Training verifiers on both correct and incorrect solutions from self-taught reasoners creates a virtuous cycle improving both generator and verifier"
  key_results: "GSM8K: +4.7% over STaR; MATH: +2.1% over STaR with verification"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

All seven YAML files have been read and reproduced exactly as they appear in the distill_tmp directory.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "c0a80f14-8f0b-4d80-a5a2-f89e496177c2",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "e7338e12-be89-43af-ae50-7da95149ecfc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read the following YAML files in full and report their complete contents back to me. These are paper distillation files I need to analyze:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/khan2024debating.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/olausson2023linc.yaml\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/pan2023logiclm.yaml\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/snell2025scaling_tts.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/multi_path_plan2025.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2024mathshepherd.yaml\n7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/hosseini2024vstar.yaml\n\nRead all files completely and reproduce their content exactly.",
    "agentId": "ac98a6bf8e92899a0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": " I've successfully read all seven YAML files. Here is their complete content:\n\n## 1. khan2024debating.yaml\n\n```yaml\npaper_key: \"khan2024debating\"\ntitle: \"Debating with More Persuasive LLMs Leads to More Truthful Answers\"\nvenue: \"ICML 2024\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Naive judge\", \"Consultancy (correct)\", \"Consultancy (incorrect)\", \"Non-interactive debate\"]\n  metrics:\n    - {name: \"judge_accuracy\", direction: \"higher_better\"}\n    - {name: \"Elo_rating\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"QuALITY\", size: \"reading comprehension\"}\n  ablation_dimensions: [\"protocol_type\", \"interactivity\", \"debater_model\", \"judge_model\", \"BoN_size\", \"quote_system\", \"round_count\", \"word_limits\", \"majority_voting\", \"few_shot_count\", \"finetuning_data_type\", \"human_vs_LLM_judges\", \"persuasiveness_optimization\"]\n  training_recipe: {optimizer: \"BoN + RL\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"multi-agent debate for AI safety\"\n\npositioning:\n  core_claim: \"Adversarial debate between LLM experts with persuasiveness optimization lets weaker judges identify truth better than non-adversarial consultancy\"\n  key_results: \"Debate: 88% human / 76% LLM accuracy vs Consultancy: 78%/54% vs Naive: 60%/48%\"\n  limitations:\n    - \"Information asymmetry only (not reasoning gap)\"\n    - \"RLHF-honest models only\"\n    - \"Quote verification dependency\"\n    - \"Single dataset (QuALITY)\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Scalable oversight — how do we verify AI behavior when it exceeds human capability?\"\n  tension: \"Alignment techniques depend on human labels, but humans can't label superhuman behavior\"\n  key_insight: \"Figures 3-4 mirror pair — persuasiveness helps debate (correct debater gains advantage) but hurts consultancy (incorrect consultant becomes more persuasive)\"\n  argument_chain: \"alignment crisis → debate as theoretical solution → empirical setup with LLM proxy → 9 cumulative insights → persuasiveness as unsupervised training signal\"\n  contribution_framing: \"Framed as 'insights' rather than 'contributions' — 9 numbered insights for cumulative evidence\"\n  intro_structure: \"5 paragraphs: (1) scalable oversight problem, (2) debate proposal recap, (3) experimental approach, (4) key findings preview, (5) implications\"\n  notable_technique: \"Numbered Insight 1-9 structure replaces traditional contribution list; Figure 3-4 mirror design as argumentative backbone\"\n\nfigures:\n  figure_count: 17\n  figure1:\n    type: \"method_overview\"\n    description: \"Debate vs consultancy protocol comparison\"\n    narrative_role: \"Establishes the two paradigms being compared\"\n    design_elements: [\"side-by-side protocols\", \"agent roles\", \"information flow\"]\n    visual_style: \"Schematic with two parallel protocol diagrams\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"bar_chart\"\n      what_compared: \"Judge accuracy across protocols\"\n      how_gain_highlighted: \"Debate consistently above consultancy\"\n      design_note: \"Clear protocol comparison\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Elo rating vs persuasiveness optimization for debate\"\n      how_gain_highlighted: \"Correct-answer Elo grows with optimization\"\n      design_note: \"Mirror pair with Figure 4 — debate's mechanism\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Elo rating vs persuasiveness optimization for consultancy\"\n      how_gain_highlighted: \"Incorrect consultant Elo grows — consultancy breaks\"\n      design_note: \"Mirror with Fig3 showing opposite effect\"\n  ablation_figures:\n    - figure_id: \"Figures 5-17\"\n      viz_type: \"mixed\"\n      dimensions_varied: [\"13 ablation dimensions\"]\n      design_note: \"Massive ablation suite — all visual, no tables\"\n  figure_narrative_role: \"Fig1(protocol) → Fig2(main result) → Fig3-4(mechanism mirror) → Fig5-17(extensive ablations) — remarkably figure-heavy, only 1 table\"\n\ntables:\n  table_count: 1\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"definitions\"\n    col_axis: \"N/A\"\n    row_organization: \"flat\"\n    col_organization: \"flat\"\n    highlight_strategy: \"N/A\"\n    statistical_reporting: \"N/A\"\n    num_baselines: 0\n    design_note: \"Definitional table only — all quantitative results are figures\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Additional experimental details\"\n    reason: \"All main results presented visually\"\n```\n\n## 2. olausson2023linc.yaml\n\n```yaml\npaper_key: \"olausson2023linc\"\ntitle: \"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\"\nvenue: \"EMNLP 2023\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Naive (direct)\", \"Scratchpad (FOL gen + LLM judge)\", \"CoT\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"ProofWriter\", size: \"OOD split\"}\n    - {name: \"FOLIO\", size: \"204\"}\n  ablation_dimensions: [\"K_majority_vote\", \"model_type\", \"proof_depth\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"neurosymbolic (LLM → FOL → Prover9)\"\n\npositioning:\n  core_claim: \"Two-stage LLM-to-FOL-to-Prover9 pipeline with majority vote achieves near-perfect accuracy on synthetic FOL tasks and maintains robustness across proof depths\"\n  key_results: \"ProofWriter: StarCoder++ LINC 82.1% vs 37.8% best baseline; GPT-3.5 LINC 96.4%; GPT-4 LINC 98.3%. FOLIO: gains for smaller models, not significant for GPT-4\"\n  limitations:\n    - \"FOL is lossy for naturalistic language\"\n    - \"Scalability unclear with more premises\"\n    - \"FOL expressiveness insufficient for higher-order/non-classical logic\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"跨界迁移型\"\n  hook: \"LLMs struggle with multi-step deduction despite general language understanding\"\n  tension: \"CoT provides reasoning steps but can't guarantee logical soundness\"\n  key_insight: \"Section 3 — the Scratchpad baseline isolates the prover's contribution: generating FOL alone (without symbolic execution) doesn't help\"\n  argument_chain: \"LLM deduction weakness → separate understanding from reasoning → LLM parses, prover reasons → Scratchpad control proves prover is key → depth analysis confirms robustness\"\n  contribution_framing: \"2 contributions: LINC system, Scratchpad diagnostic baseline\"\n  intro_structure: \"4 paragraphs: (1) LLM reasoning gap, (2) neurosymbolic opportunity, (3) LINC and Scratchpad, (4) key findings\"\n  notable_technique: \"Scratchpad as diagnostic baseline — isolates the symbolic prover's causal contribution beyond just generating FOL\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"method_overview\"\n    description: \"LINC pipeline: NL → LLM → FOL → Prover9 → answer, with K-way majority vote\"\n    narrative_role: \"Establishes the two-stage architecture\"\n    design_elements: [\"pipeline flow\", \"LLM and Prover9 components\", \"majority vote aggregation\"]\n    visual_style: \"Left-to-right pipeline diagram\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"bar_chart\"\n      what_compared: \"Methods across models on ProofWriter and FOLIO\"\n      how_gain_highlighted: \"LINC bars clearly above baselines\"\n      design_note: \"Grouped by model, color by method\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Accuracy across proof depths (0-5)\"\n      how_gain_highlighted: \"LINC maintains near-perfect accuracy while baselines degrade\"\n      design_note: \"Strongest evidence for robustness — depth-accuracy curves\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"qualitative_comparison\"\n      what_compared: \"Error types: LINC vs CoT\"\n      how_gain_highlighted: \"Only 21/74 errors shared — methods are complementary\"\n      design_note: \"Error analysis Venn diagram / taxonomy\"\n  ablation_figures: []\n  figure_narrative_role: \"Fig1(pipeline) → Fig2(FOL examples) → Fig3(main results bars) → Fig4(depth analysis) → Fig5(error analysis)\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    table_id: \"N/A\"\n    row_axis: \"N/A\"\n    col_axis: \"N/A\"\n    row_organization: \"N/A\"\n    col_organization: \"N/A\"\n    highlight_strategy: \"N/A\"\n    statistical_reporting: \"p-values for significance\"\n    num_baselines: 3\n    design_note: \"No tables — all results presented as bar charts and line plots. Unusual but effective given small experimental grid\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Prompt templates, FOL examples, additional error analysis\"\n    reason: \"Qualitative content doesn't fit tabular format\"\n```\n\n## 3. pan2023logiclm.yaml\n\n```yaml\npaper_key: \"pan2023logiclm\"\ntitle: \"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\"\nvenue: \"EMNLP Findings 2023\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Standard Prompting\", \"CoT\", \"CoT-SC\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"Exe_Rate\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"PrOntoQA\", size: \"500\"}\n    - {name: \"ProofWriter\", size: \"600\"}\n    - {name: \"FOLIO\", size: \"204\"}\n    - {name: \"LogicalDeduction\", size: \"300\"}\n    - {name: \"AR-LSAT\", size: \"230\"}\n  ablation_dimensions: [\"self_refinement\", \"solver_type\", \"model_type\", \"problem_type\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"LLM + symbolic solver (Pyke/Prover9/python-constraint/Z3)\"\n\npositioning:\n  core_claim: \"Reframing LLM's role from 'solving' to 'representing' — LLM formulates problems symbolically, dedicated solvers execute reasoning, with self-refinement for invalid formulations\"\n  key_results: \"+39.2% over standard prompting, +18.4% over CoT (GPT-3.5); GPT-4: PrOntoQA 83.2, ProofWriter 79.66, FOLIO 78.92, LogicalDeduction 87.63, AR-LSAT 43.04\"\n  limitations:\n    - \"Low Exe_Rate on complex problems (FOLIO 79.9%, AR-LSAT 32.6% with GPT-4)\"\n    - \"Self-refinement fixes grammar but not semantics\"\n    - \"Formalization bottleneck on naturalistic language\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"跨界迁移型\"\n  hook: \"LLMs can understand language but fail at rigorous logical reasoning\"\n  tension: \"Prompting strategies improve reasoning but can't guarantee faithfulness\"\n  key_insight: \"Section 3 — separating 'understanding' (LLM) from 'reasoning' (solver) plays to each component's strength\"\n  argument_chain: \"LLM reasoning unfaithful → separate understanding from reasoning → LLM formulates + solver executes → self-refinement handles errors → 5-dataset validation\"\n  contribution_framing: \"3 contributions: framework, self-refinement mechanism, comprehensive evaluation\"\n  intro_structure: \"5 paragraphs: (1) LLM reasoning promise/limitations, (2) faithfulness problem, (3) Logic-LM framework, (4) contributions, (5) paper structure\"\n  notable_technique: \"Reframing the LLM's role from 'solver' to 'translator' — rhetorically powerful simplification\"\n\nfigures:\n  figure_count: 4\n  figure1:\n    type: \"method_overview\"\n    description: \"Logic-LM pipeline: Problem Formulation → Symbolic Reasoning → Result Interpretation, with self-refinement loop\"\n    narrative_role: \"Establishes the three-stage architecture with refinement\"\n    design_elements: [\"pipeline flow\", \"self-refinement loop arrow\", \"4 solver icons\"]\n    visual_style: \"Flowchart with feedback loop\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Accuracy across reasoning depths\"\n      how_gain_highlighted: \"Logic-LM advantage grows with depth (widening gap at depth-5)\"\n      design_note: \"Depth analysis showing symbolic reasoning's advantage on harder problems\"\n  ablation_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"with/without self-refinement\", \"solver_type\"]\n      design_note: \"Isolates self-refinement contribution\"\n  figure_narrative_role: \"Fig1(pipeline) → Fig2(example) → Fig3(depth analysis) → Fig4(ablation)\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"datasets × accuracy\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"single run\"\n    num_baselines: 3\n    design_note: \"Clean comparison with Exe_Rate reported alongside accuracy\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"self_refinement\", \"error_type\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Breaks down Exe_Rate improvement by error category\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Prompt templates, solver-specific results, error examples\"\n    reason: \"Detailed error analysis too long for main text\"\n```\n\n## 4. snell2025scaling_tts.yaml\n\n```yaml\npaper_key: \"snell2025scaling_tts\"\ntitle: \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters\"\nvenue: \"ICLR 2025 (Oral)\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"greedy decoding\", \"majority voting\", \"best-of-N\", \"reward-model reranking\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"compute_efficiency\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"MATH\", size: \"500\"}\n    - {name: \"GSM8K\", size: \"1319\"}\n  ablation_dimensions: [\"compute_budget\", \"search_strategy\", \"verifier_type\", \"model_scale\"]\n  training_recipe: {info: \"process reward models for verification\"}\n  method_family: \"test-time compute scaling\"\n\npositioning:\n  core_claim: \"Optimal allocation of test-time compute (search + verification) can match or exceed 14x larger models\"\n  key_results: \"Smaller model + optimal test-time compute matches 14x larger model on MATH\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 5. multi_path_plan2025.yaml\n\n```yaml\npaper_key: \"multi_path_plan2025\"\ntitle: \"Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation\"\nvenue: \"arXiv 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"CoT\", \"SC-CoT\", \"ToT\", \"plan-then-solve\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM8K\", size: \"1319\"}\n    - {name: \"MATH\", size: \"500\"}\n    - {name: \"ARC-Challenge\", size: \"2590\"}\n  ablation_dimensions: [\"num_paths\", \"aggregation_strategy\", \"plan_granularity\"]\n  training_recipe: {info: \"N/A\"}\n  method_family: \"multi-path reasoning aggregation\"\n\npositioning:\n  core_claim: \"Aggregating multiple reasoning plans before execution improves long chain-of-thought reasoning\"\n  key_results: \"N/A\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 6. wang2024mathshepherd.yaml\n\n```yaml\npaper_key: \"wang2024mathshepherd\"\ntitle: \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\"\nvenue: \"ACL 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"majority voting\", \"ORM (outcome reward model)\", \"PRM (process reward model)\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM8K\", size: \"1319\"}\n    - {name: \"MATH\", size: \"500\"}\n  ablation_dimensions: [\"verification_granularity\", \"reward_model_size\", \"num_samples\"]\n  training_recipe: {info: \"automated step-level annotation via completion-based verification\"}\n  method_family: \"process reward model / step-level verification\"\n\npositioning:\n  core_claim: \"Automated step-level verification annotations (without human labels) enable process reward models that outperform outcome-only verification\"\n  key_results: \"GSM8K: 84.1% → 93.4% with Math-Shepherd PRM verification\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 7. hosseini2024vstar.yaml\n\n```yaml\npaper_key: \"hosseini2024vstar\"\ntitle: \"V-STaR: Training Verifiers for Self-Taught Reasoners\"\nvenue: \"NeurIPS 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"STaR\", \"REST-EM\", \"majority_voting\", \"ORM\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM8K\", size: \"1319\"}\n    - {name: \"MATH\", size: \"500\"}\n    - {name: \"ARC-Challenge\", size: \"2590\"}\n  ablation_dimensions: [\"verifier_training_data\", \"iteration_count\", \"generator_vs_verifier_scaling\"]\n  training_recipe: {info: \"iterative self-training with DPO verifier\"}\n  method_family: \"self-training with verifier\"\n\npositioning:\n  core_claim: \"Training verifiers on both correct and incorrect solutions from self-taught reasoners creates a virtuous cycle improving both generator and verifier\"\n  key_results: \"GSM8K: +4.7% over STaR; MATH: +2.1% over STaR with verification\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\nAll seven YAML files have been read and reproduced exactly as they appear in the distill_tmp directory."
      }
    ],
    "totalDurationMs": 51835,
    "totalTokens": 31044,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 8,
      "cache_creation_input_tokens": 7528,
      "cache_read_input_tokens": 18134,
      "output_tokens": 5374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7528
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8,
          "output_tokens": 5374,
          "cache_read_input_tokens": 18134,
          "cache_creation_input_tokens": 7528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7528,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "c0a80f14-8f0b-4d80-a5a2-f89e496177c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "e7338e12-be89-43af-ae50-7da95149ecfc",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Tool result

_source line 25 · 2026-05-22T13:46:53.915Z_

<details><summary>↩ Tool result · `toolu_01VejfPWg9M28SWGA3aWoJ1i`</summary>

````text
 Here are the complete contents of all seven YAML files:

## 1. satbench2025.yaml

```yaml
paper_key: "satbench2025"
title: "SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas"
venue: "EMNLP 2025"
full_text_available: false

research:
  baselines: ["o4-mini", "other frontier LLMs"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "SATBench", size: "2100 puzzles with adjustable difficulty"}
  ablation_dimensions: ["number of clauses (difficulty)", "SAT vs UNSAT problems"]
  training_recipe: {info: "evaluation benchmark, no training; automated puzzle generation from SAT formulas + LLM translation"}
  method_family: "SAT-based reasoning benchmark"

positioning:
  core_claim: "LLMs have systematic failures in search-based logical reasoning: even the strongest model (o4-mini) achieves only 65% on hard UNSAT problems (near 50% random baseline), exhibiting satisfiability bias, context inconsistency, and condition omission"
  key_results: "o4-mini: 65.0% on hard UNSAT (random baseline: 50%); systematic failures in satisfiability bias, context inconsistency, condition omission"
  limitations: ["N/A"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 2. logicagent2025.yaml

```yaml
paper_key: "logicagent2025"
title: "From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)"
venue: "ACL 2026"
full_text_available: false

research:
  baselines: ["standard CoT prompting", "other reasoning agents"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "RepublicQA", size: "N/A (college-level, Flesch-Kincaid Grade 11.94)"}
    - {name: "ProntoQA", size: "N/A"}
    - {name: "ProofWriter", size: "N/A"}
    - {name: "FOLIO", size: "N/A"}
    - {name: "ProverQA", size: "N/A"}
  ablation_dimensions: ["semiotic square components", "automated deduction vs reflective verification"]
  training_recipe: {info: "agent-based prompting framework, no training"}
  method_family: "multi-perspective reasoning agent"

positioning:
  core_claim: "Semiotic-square-guided multi-perspective reasoning jointly addresses logical and semantic complexity, achieving 6.25% improvement on RepublicQA and 7.05% on mainstream logic benchmarks"
  key_results: "+6.25% average on RepublicQA; +7.05% average on ProntoQA, ProofWriter, FOLIO, ProverQA"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 3. xu2026dylos.yaml

```yaml
paper_key: "xu2026dylos"
title: "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)"
venue: "EACL 2026"
full_text_available: true

research:
  baselines: ["Zero-shot", "CoT", "Logic-LM", "LINC", "SymbCoT", "Aristotle"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "routing_accuracy", direction: "higher_better"}
  datasets:
    - {name: "PrOntoQA", size: "500"}
    - {name: "ProofWriter", size: "600"}
    - {name: "FOLIO", size: "204"}
    - {name: "LogicalDeduction", size: "300"}
    - {name: "AR-LSAT", size: "230"}
  ablation_dimensions: ["solver_type", "routing_strategy", "model_scale", "LoRA_finetuning"]
  training_recipe: {optimizer: "LoRA", lr: "N/A", hardware: "N/A"}
  method_family: "LLM-symbolic hybrid with dynamic solver routing"

positioning:
  core_claim: "Dynamic composition of multiple symbolic solvers (Pyke/Prover9/Z3/MiniZinc) via LLM-based routing achieves robust logical reasoning across heterogeneous problem types"
  key_results: "92.1% mixed reasoning (GPT-4o), +27% over zero-shot; 7B models: 8-26% baseline → 41-59.6% with LoRA"
  limitations:
    - "Model scale dependency — small models struggle with formalization"
    - "Formalization bottleneck: 60-80% of small-model errors from formalization"
    - "Limited solver coverage: no probabilistic/temporal/mathematical reasoning"
  relation_to_us: "competitor"

narrative:
  story_type: "统一框架型"
  hook: "Material vs formal inference dichotomy — LLMs handle material, symbolic solvers handle formal, but no system integrates both dynamically"
  tension: "Existing hybrid methods are locked to a single solver type, failing on problems requiring different logical paradigms"
  key_insight: "Revealed in Section 3 — a router that classifies reasoning type enables dynamic solver dispatch with >98% accuracy"
  argument_chain: "heterogeneous logical tasks → single-solver limitation → classify-then-route → multi-solver composition → validated on mixed benchmarks"
  contribution_framing: "3 contributions each with quantitative evidence in the intro"
  intro_structure: "5 paragraphs: (1) material-formal dichotomy hook, (2) existing hybrid limitations, (3) DyLoS overview, (4) contributions with numbers, (5) paper structure"
  notable_technique: "Every contribution claim includes specific quantitative results; material-formal inference dichotomy used as recurring anchor"

figures:
  figure_count: 5
  figure1:
    type: "method_overview"
    description: "3-stage pipeline: decompose → route → solve, showing 4 solver types"
    narrative_role: "Establishes the system architecture immediately after the problem statement"
    design_elements: ["flow diagram", "solver icons", "color-coded stages"]
    visual_style: "Left-to-right pipeline with branching at routing stage"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "bar_chart"
      what_compared: "Accuracy across datasets with different solvers"
      how_gain_highlighted: "DyLoS bar consistently highest"
      design_note: "Grouped by dataset, color by method"
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "bar_chart"
      dimensions_varied: ["model_scale", "with/without_LoRA"]
      design_note: "Shows scaling behavior and LoRA impact"
  figure_narrative_role: "Fig1(architecture) → Fig2(routing) → Fig3(main results) → Fig4(scaling) → Fig5(error analysis)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × accuracy"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "single run"
    num_baselines: 6
    design_note: "Separates LLM-only vs hybrid methods"
  ablation_tables:
    - table_id: "Table 3"
      what_varied: ["solver_selection", "routing_strategy"]
      variation_style: "full_numbers"
      design_note: "Shows each solver's standalone vs combined performance"
  supplementary_tables:
    in_appendix: true
    content: "Prompt templates, additional model results"
    reason: "Space constraints"
```

## 4. aristotle2025.yaml

```yaml
paper_key: "aristotle2025"
title: "Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework"
venue: "ACL 2025"
full_text_available: true

research:
  baselines: ["CoT", "ToT", "CR", "SymbCoT", "Logic-LM", "LINC"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "one_step_inference_accuracy", direction: "higher_better"}
    - {name: "visited_nodes", direction: "lower_better"}
  datasets:
    - {name: "PrOntoQA", size: "500"}
    - {name: "ProofWriter", size: "600"}
    - {name: "FOLIO", size: "204"}
    - {name: "LogiQA", size: "651"}
  ablation_dimensions: ["CNF_decomposition", "search_strategy", "resolution_principle", "Prolog_translation"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "symbolic logic pipeline (Prolog + CNF + resolution)"

positioning:
  core_claim: "A logic-complete framework integrating Prolog translation, CNF decomposition, and resolution principle into LLM reasoning achieves 99.7% one-step accuracy while reducing search by 52.6%"
  key_results: "+4.5% avg over SymbCoT (GPT-4), +5.4% (GPT-4o), +12.1% (Llama-3.1-405B); 99.7% one-step accuracy vs ToT's 74.0%"
  limitations:
    - "Requires all premises explicitly stated — fails on implicit knowledge (LogiQA: 31.2% vs CoT's 65.6%)"
    - "Computationally expensive multi-step search"
  relation_to_us: "competitor"

narrative:
  story_type: "突破局限型"
  hook: "Figure 1 teaser showing accuracy gap — quantifies the problem before explaining the solution"
  tension: "Existing neurosymbolic methods suffer from incomplete logical operations, leading to error accumulation in multi-step proofs"
  key_insight: "Sec 3.2 — replacing LLM self-evaluation with deterministic resolution principle eliminates the weakest link in the reasoning chain"
  argument_chain: "multi-step errors → incomplete symbolic integration → full Prolog pipeline → deterministic search → validated accuracy + efficiency"
  contribution_framing: "3 contributions: framework, logic-completeness proof, empirical validation"
  intro_structure: "6 paragraphs: (1) LLM reasoning importance, (2) existing method failures with Figure 1, (3) root cause analysis, (4) Aristotle overview, (5) contributions, (6) paper structure"
  notable_technique: "Teaser result figure in intro paragraph 2 — immediately quantifies the gap before any method description"

figures:
  figure_count: 8
  figure1:
    type: "teaser_result"
    description: "Bar chart comparing accuracy of existing methods showing performance gap"
    narrative_role: "Quantifies the problem in the intro before solution is described"
    design_elements: ["grouped bars", "accuracy numbers", "method labels"]
    visual_style: "Clean bar chart with clear performance gap visualization"
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "scatter"
      what_compared: "Accuracy vs efficiency tradeoff across methods"
      how_gain_highlighted: "Aristotle in upper-left (high accuracy, low nodes)"
      design_note: "Dual-axis: accuracy vs search efficiency"
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      what_compared: "Accuracy across reasoning depths"
      how_gain_highlighted: "Aristotle maintains accuracy at higher depths"
      design_note: "Shows robustness to depth"
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "grouped_bar"
      dimensions_varied: ["CNF", "resolution", "search_strategy"]
      design_note: "Red gradient coloring for ablation variants"
  figure_narrative_role: "Fig1(teaser gap) → Fig2(method) → Fig3(ablation) → Fig4(efficiency) → Fig5(depth) → Fig6-7(case studies) → Fig8(error analysis)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × accuracy"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best + underline_second"
    statistical_reporting: "single run"
    num_baselines: 6
    design_note: "Categorizes methods into LLM-only, symbolic-augmented, and Aristotle"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["CNF", "resolution", "Prolog_translation", "search"]
      variation_style: "checkmark_grid"
      design_note: "Systematic component removal showing each module's contribution"
  supplementary_tables:
    in_appendix: true
    content: "Extended results, additional models, case studies"
    reason: "Main paper focuses on core 4 datasets"
```

## 5. qi2025symbolic_provers.yaml

```yaml
paper_key: "qi2025symbolic_provers"
title: "Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation"
venue: "ICLR 2025"
full_text_available: true

research:
  baselines: ["GPT-4o", "Claude-3.5-Sonnet", "Llama3.1-8B/70B", "Gemma2-9B/27B", "Mistral-7B/Large", "Qwen2.5-7B/32B/72B"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "ID_accuracy", direction: "higher_better"}
    - {name: "OOD_accuracy", direction: "higher_better"}
  datasets:
    - {name: "ProverQA", size: "1500 instances, 3 difficulty levels"}
    - {name: "ProofWriter", size: "for transfer eval"}
    - {name: "FOLIO", size: "for transfer eval"}
  ablation_dimensions: ["difficulty_level", "CoT_vs_direct", "finetuning_data_source", "ID_vs_OOD"]
  training_recipe: {optimizer: "SFT", lr: "N/A", hardware: "N/A"}
  method_family: "LLM + symbolic prover (Prover9) for benchmark generation"

positioning:
  core_claim: "Top-down generation combining LLM diversity with Prover9 rigor creates ProverQA benchmark that reveals even SOTA models barely exceed chance on hard FOL problems"
  key_results: "GPT-4o: 50.0%, Claude-3.5: 56.4% on hard; finetuning Llama3.1-8B on ProverQA: +34.6% ID, +7.5% OOD (vs -2.0% ProofWriter, -11.4% FOLIO)"
  limitations:
    - "Benchmark limited to FOL reasoning"
    - "Top-down generation may not cover all reasoning patterns"
  relation_to_us: "foundation"

narrative:
  story_type: "统一框架型"
  hook: "Existing benchmarks lack reliable ground truth labels and controllable difficulty"
  tension: "Bottom-up benchmark construction introduces label noise and uncontrolled complexity"
  key_insight: "Section 3 — top-down generation (goal → backward to premises) ensures logical coherence by construction"
  argument_chain: "benchmark limitations → top-down generation idea → Prover9 guarantees → difficulty control → model evaluation reveals gaps → finetuning transfer validates quality"
  contribution_framing: "3 contributions: generation framework, benchmark, comprehensive evaluation"
  intro_structure: "4 paragraphs: (1) importance of logical reasoning, (2) criteria for good benchmarks, (3) ProverGen framework, (4) contributions"
  notable_technique: "Table 1 checkmark grid as early positioning device — shows no existing benchmark meets all criteria"

figures:
  figure_count: 2
  figure1:
    type: "method_overview"
    description: "ProverGen pipeline: top-down generation with Prover9"
    narrative_role: "Establishes the generation framework"
    design_elements: ["pipeline flow", "Prover9 integration point"]
    visual_style: "Schematic flow diagram"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "bar_chart"
      what_compared: "Model accuracy across difficulty levels"
      how_gain_highlighted: "Performance drop at higher difficulty"
      design_note: "Grouped by difficulty, showing model capability gap"
  ablation_figures: []
  figure_narrative_role: "Fig1(method) → Fig2(results) — minimal figures, table-heavy paper"

tables:
  table_count: 6
  main_result_table:
    table_id: "Table 2"
    row_axis: "methods"
    col_axis: "difficulty levels × accuracy"
    row_organization: "by_category"
    col_organization: "grouped_by_difficulty"
    highlight_strategy: "bold_best"
    statistical_reporting: "single run"
    num_baselines: 10
    design_note: "Comprehensive model comparison across 3 difficulty levels"
  ablation_tables:
    - table_id: "Table 3"
      what_varied: ["finetuning_data_source", "ID_vs_OOD"]
      variation_style: "full_numbers"
      design_note: "Transfer learning comparison showing ProverQA's superiority"
  supplementary_tables:
    in_appendix: true
    content: "Additional model results, generation statistics"
    reason: "Main paper focuses on key comparisons"
```

## 6. dissecting2025.yaml

```yaml
paper_key: "dissecting2025"
title: "Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation"
venue: "EMNLP Findings 2025"
full_text_available: true

research:
  baselines: ["LLaMA-3.1-8B", "Gemma-2-9B", "Mistral-v0.3-7B", "CoT", "SFT-NL", "SFT-Symbolic"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "atomicity", direction: "higher_better"}
    - {name: "CSS", direction: "higher_better"}
    - {name: "NSD", direction: "higher_better"}
    - {name: "RFI", direction: "higher_better"}
  datasets:
    - {name: "FLD", size: "multi-depth"}
    - {name: "FOLIO", size: "204"}
    - {name: "ProntoQA", size: "500"}
  ablation_dimensions: ["supervision_type_NL_vs_symbolic", "reasoning_depth", "model_family"]
  training_recipe: {optimizer: "AdamW", lr: "1e-6", hardware: "4xA100, ~2h per model"}
  method_family: "evaluation framework (accuracy + soundness + probing)"

positioning:
  core_claim: "Three-dimensional evaluation (accuracy + stepwise soundness + representation probing) reveals NL supervision generalizes better but symbolic supervision produces more structurally sound reasoning chains"
  key_results: "SFT-NL: 67.5% on FLD (from 31.7%); symbolic has higher atomicity (24.7% vs 13.0%); probing shows SFT improves generation but not internalized understanding"
  limitations:
    - "Limited to propositional/FOL reasoning"
    - "Probing only captures linear representations"
  relation_to_us: "foundation"

narrative:
  story_type: "化繁为简型"
  hook: "LLMs show improved reasoning but we lack tools to understand what exactly improves"
  tension: "Single-metric evaluation (accuracy) masks critical differences in reasoning quality"
  key_insight: "Section 4 — decomposing evaluation into accuracy/soundness/probing reveals a fundamental NL-vs-symbolic tradeoff"
  argument_chain: "opaque evaluation → 3-dimensional framework → NL vs symbolic comparison → surprising probing results → implications for training design"
  contribution_framing: "3 contributions: evaluation framework, NL-vs-symbolic findings, probing insights"
  intro_structure: "5 paragraphs: (1) LLM reasoning progress, (2) evaluation limitations, (3) proposed framework, (4) key findings preview, (5) paper structure"
  notable_technique: "Previewing surprising findings in intro to create anticipation for the full analysis"

figures:
  figure_count: 5
  figure1:
    type: "method_overview"
    description: "Three-dimensional evaluation framework: accuracy, soundness, probing"
    narrative_role: "Establishes the evaluation methodology upfront"
    design_elements: ["three parallel tracks", "metric labels", "color coding"]
    visual_style: "Schematic diagram with three evaluation dimensions"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Accuracy across reasoning depths for NL vs symbolic supervision"
      how_gain_highlighted: "Symbolic degrades more gracefully at higher depths"
      design_note: "Depth-accuracy curves are the strongest evidence"
    - figure_id: "Figure 4"
      viz_type: "heatmap"
      what_compared: "Probing results (CSS, NSD, RFI) across models and training types"
      how_gain_highlighted: "Color intensity shows where SFT helps vs doesn't"
      design_note: "Compact visualization of multi-dimensional probing results"
  ablation_figures:
    - figure_id: "Figure 5"
      viz_type: "bar_chart"
      dimensions_varied: ["model_family", "supervision_type"]
      design_note: "Cross-model consistency check"
  figure_narrative_role: "Fig1(framework) → Fig2(accuracy overview) → Fig3(depth analysis) → Fig4(probing) → Fig5(cross-model)"

tables:
  table_count: 5
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × metrics (accuracy + soundness)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "single run"
    num_baselines: 6
    design_note: "Dual-metric reporting (accuracy and soundness side-by-side)"
  ablation_tables:
    - table_id: "Table 3"
      what_varied: ["supervision_type", "reasoning_depth"]
      variation_style: "full_numbers"
      design_note: "Depth-stratified comparison"
  supplementary_tables:
    in_appendix: true
    content: "Full probing results, additional model comparisons"
    reason: "Probing methodology details too extensive for main text"
```

## 7. crest2025.yaml

```yaml
paper_key: "crest2025"
title: "Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)"
venue: "NAACL 2025"
full_text_available: true

research:
  baselines: ["SFT", "RFT", "STaR", "REST-EM", "V-STaR", "DPO-vanilla"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "ReClor", size: "~6k"}
    - {name: "ARC-Challenge", size: "2590"}
    - {name: "CSQA", size: "~12k"}
  ablation_dimensions: ["follow_up_questions", "tolerance_parameter_t", "DPO_lambda", "sample_count_N"]
  training_recipe: {optimizer: "AdamW", lr: "5e-6", hardware: "4xA100"}
  method_family: "consistency-driven self-training"

positioning:
  core_claim: "Follow-up question consistency provides richer signal than binary answer correctness for filtering self-training rationales, enabling better SFT+DPO training"
  key_results: "+1.7-1.8% over best baseline on ReClor; consistent gains on ARC-C and CSQA across Llama-3-8B, Gemma-7B, Phi-2"
  limitations:
    - "Restricted to MCQ format"
    - "All follow-up questions weighted equally"
    - "No teacher-student setting explored"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Self-training with LLM-generated rationales is promising but suffers from false positive rationales"
  tension: "Binary correctness filtering passes rationales with right answers but wrong reasoning"
  key_insight: "Section 3.2 — follow-up questions stress-test rationale quality beyond just checking the final answer"
  argument_chain: "self-training promise → false positive problem → follow-up question consistency → filtered SFT + DPO → multi-model validation"
  contribution_framing: "3 contributions: consistency evaluation method, 4-stage training pipeline, empirical validation"
  intro_structure: "4 paragraphs: (1) self-training promise, (2) false positive problem, (3) CREST solution, (4) contributions"
  notable_technique: "Concrete example of a false positive rationale in intro to make the problem viscerally clear"

figures:
  figure_count: 4
  figure1:
    type: "problem_illustration"
    description: "Example showing a rationale that gets the right answer through wrong reasoning, and how follow-up questions expose it"
    narrative_role: "Makes the false positive problem concrete and motivates the solution"
    design_elements: ["correct vs incorrect rationale comparison", "follow-up question examples", "red/green highlighting"]
    visual_style: "Two-column comparison with text examples"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "bar_chart"
      what_compared: "Methods across 3 datasets × 3 models"
      how_gain_highlighted: "CREST consistently highest or tied"
      design_note: "3×3 grid layout for comprehensive comparison"
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      dimensions_varied: ["tolerance_t", "DPO_lambda", "sample_N"]
      design_note: "Sensitivity analysis with clear optimal ranges"
  figure_narrative_role: "Fig1(problem example) → Fig2(method pipeline) → Fig3(main results) → Fig4(sensitivity)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets × models"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best + underline_second"
    statistical_reporting: "mean across 3 seeds"
    num_baselines: 6
    design_note: "Separate sections for each model family"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["follow_up_questions", "SFT_only_vs_SFT+DPO"]
      variation_style: "full_numbers"
      design_note: "Isolates contribution of each pipeline stage"
  supplementary_tables:
    in_appendix: true
    content: "Additional ablations, prompt templates, follow-up question examples"
    reason: "Main text focuses on core comparisons"
```

All seven YAML files have been read and reproduced in their complete, unmodified form above.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "fc4fa99b-6528-446e-929a-a9084a806af4",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "51a3dd48-b9fc-497e-989a-ab582817220d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read the following YAML files in full and report their complete contents back to me. These are paper distillation files I need to analyze:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/satbench2025.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/logicagent2025.yaml\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2026dylos.yaml\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/aristotle2025.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/qi2025symbolic_provers.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dissecting2025.yaml\n7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/crest2025.yaml\n\nRead all files completely and reproduce their content exactly.",
    "agentId": "aee60627d9c31287e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": " Here are the complete contents of all seven YAML files:\n\n## 1. satbench2025.yaml\n\n```yaml\npaper_key: \"satbench2025\"\ntitle: \"SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas\"\nvenue: \"EMNLP 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"o4-mini\", \"other frontier LLMs\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"SATBench\", size: \"2100 puzzles with adjustable difficulty\"}\n  ablation_dimensions: [\"number of clauses (difficulty)\", \"SAT vs UNSAT problems\"]\n  training_recipe: {info: \"evaluation benchmark, no training; automated puzzle generation from SAT formulas + LLM translation\"}\n  method_family: \"SAT-based reasoning benchmark\"\n\npositioning:\n  core_claim: \"LLMs have systematic failures in search-based logical reasoning: even the strongest model (o4-mini) achieves only 65% on hard UNSAT problems (near 50% random baseline), exhibiting satisfiability bias, context inconsistency, and condition omission\"\n  key_results: \"o4-mini: 65.0% on hard UNSAT (random baseline: 50%); systematic failures in satisfiability bias, context inconsistency, condition omission\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 2. logicagent2025.yaml\n\n```yaml\npaper_key: \"logicagent2025\"\ntitle: \"From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)\"\nvenue: \"ACL 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"standard CoT prompting\", \"other reasoning agents\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"RepublicQA\", size: \"N/A (college-level, Flesch-Kincaid Grade 11.94)\"}\n    - {name: \"ProntoQA\", size: \"N/A\"}\n    - {name: \"ProofWriter\", size: \"N/A\"}\n    - {name: \"FOLIO\", size: \"N/A\"}\n    - {name: \"ProverQA\", size: \"N/A\"}\n  ablation_dimensions: [\"semiotic square components\", \"automated deduction vs reflective verification\"]\n  training_recipe: {info: \"agent-based prompting framework, no training\"}\n  method_family: \"multi-perspective reasoning agent\"\n\npositioning:\n  core_claim: \"Semiotic-square-guided multi-perspective reasoning jointly addresses logical and semantic complexity, achieving 6.25% improvement on RepublicQA and 7.05% on mainstream logic benchmarks\"\n  key_results: \"+6.25% average on RepublicQA; +7.05% average on ProntoQA, ProofWriter, FOLIO, ProverQA\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 3. xu2026dylos.yaml\n\n```yaml\npaper_key: \"xu2026dylos\"\ntitle: \"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)\"\nvenue: \"EACL 2026\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Zero-shot\", \"CoT\", \"Logic-LM\", \"LINC\", \"SymbCoT\", \"Aristotle\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"routing_accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"PrOntoQA\", size: \"500\"}\n    - {name: \"ProofWriter\", size: \"600\"}\n    - {name: \"FOLIO\", size: \"204\"}\n    - {name: \"LogicalDeduction\", size: \"300\"}\n    - {name: \"AR-LSAT\", size: \"230\"}\n  ablation_dimensions: [\"solver_type\", \"routing_strategy\", \"model_scale\", \"LoRA_finetuning\"]\n  training_recipe: {optimizer: \"LoRA\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"LLM-symbolic hybrid with dynamic solver routing\"\n\npositioning:\n  core_claim: \"Dynamic composition of multiple symbolic solvers (Pyke/Prover9/Z3/MiniZinc) via LLM-based routing achieves robust logical reasoning across heterogeneous problem types\"\n  key_results: \"92.1% mixed reasoning (GPT-4o), +27% over zero-shot; 7B models: 8-26% baseline → 41-59.6% with LoRA\"\n  limitations:\n    - \"Model scale dependency — small models struggle with formalization\"\n    - \"Formalization bottleneck: 60-80% of small-model errors from formalization\"\n    - \"Limited solver coverage: no probabilistic/temporal/mathematical reasoning\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"统一框架型\"\n  hook: \"Material vs formal inference dichotomy — LLMs handle material, symbolic solvers handle formal, but no system integrates both dynamically\"\n  tension: \"Existing hybrid methods are locked to a single solver type, failing on problems requiring different logical paradigms\"\n  key_insight: \"Revealed in Section 3 — a router that classifies reasoning type enables dynamic solver dispatch with >98% accuracy\"\n  argument_chain: \"heterogeneous logical tasks → single-solver limitation → classify-then-route → multi-solver composition → validated on mixed benchmarks\"\n  contribution_framing: \"3 contributions each with quantitative evidence in the intro\"\n  intro_structure: \"5 paragraphs: (1) material-formal dichotomy hook, (2) existing hybrid limitations, (3) DyLoS overview, (4) contributions with numbers, (5) paper structure\"\n  notable_technique: \"Every contribution claim includes specific quantitative results; material-formal inference dichotomy used as recurring anchor\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"method_overview\"\n    description: \"3-stage pipeline: decompose → route → solve, showing 4 solver types\"\n    narrative_role: \"Establishes the system architecture immediately after the problem statement\"\n    design_elements: [\"flow diagram\", \"solver icons\", \"color-coded stages\"]\n    visual_style: \"Left-to-right pipeline with branching at routing stage\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"bar_chart\"\n      what_compared: \"Accuracy across datasets with different solvers\"\n      how_gain_highlighted: \"DyLoS bar consistently highest\"\n      design_note: \"Grouped by dataset, color by method\"\n  ablation_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"model_scale\", \"with/without_LoRA\"]\n      design_note: \"Shows scaling behavior and LoRA impact\"\n  figure_narrative_role: \"Fig1(architecture) → Fig2(routing) → Fig3(main results) → Fig4(scaling) → Fig5(error analysis)\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"datasets × accuracy\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"single run\"\n    num_baselines: 6\n    design_note: \"Separates LLM-only vs hybrid methods\"\n  ablation_tables:\n    - table_id: \"Table 3\"\n      what_varied: [\"solver_selection\", \"routing_strategy\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Shows each solver's standalone vs combined performance\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Prompt templates, additional model results\"\n    reason: \"Space constraints\"\n```\n\n## 4. aristotle2025.yaml\n\n```yaml\npaper_key: \"aristotle2025\"\ntitle: \"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\"\nvenue: \"ACL 2025\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"CoT\", \"ToT\", \"CR\", \"SymbCoT\", \"Logic-LM\", \"LINC\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"one_step_inference_accuracy\", direction: \"higher_better\"}\n    - {name: \"visited_nodes\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"PrOntoQA\", size: \"500\"}\n    - {name: \"ProofWriter\", size: \"600\"}\n    - {name: \"FOLIO\", size: \"204\"}\n    - {name: \"LogiQA\", size: \"651\"}\n  ablation_dimensions: [\"CNF_decomposition\", \"search_strategy\", \"resolution_principle\", \"Prolog_translation\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"symbolic logic pipeline (Prolog + CNF + resolution)\"\n\npositioning:\n  core_claim: \"A logic-complete framework integrating Prolog translation, CNF decomposition, and resolution principle into LLM reasoning achieves 99.7% one-step accuracy while reducing search by 52.6%\"\n  key_results: \"+4.5% avg over SymbCoT (GPT-4), +5.4% (GPT-4o), +12.1% (Llama-3.1-405B); 99.7% one-step accuracy vs ToT's 74.0%\"\n  limitations:\n    - \"Requires all premises explicitly stated — fails on implicit knowledge (LogiQA: 31.2% vs CoT's 65.6%)\"\n    - \"Computationally expensive multi-step search\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Figure 1 teaser showing accuracy gap — quantifies the problem before explaining the solution\"\n  tension: \"Existing neurosymbolic methods suffer from incomplete logical operations, leading to error accumulation in multi-step proofs\"\n  key_insight: \"Sec 3.2 — replacing LLM self-evaluation with deterministic resolution principle eliminates the weakest link in the reasoning chain\"\n  argument_chain: \"multi-step errors → incomplete symbolic integration → full Prolog pipeline → deterministic search → validated accuracy + efficiency\"\n  contribution_framing: \"3 contributions: framework, logic-completeness proof, empirical validation\"\n  intro_structure: \"6 paragraphs: (1) LLM reasoning importance, (2) existing method failures with Figure 1, (3) root cause analysis, (4) Aristotle overview, (5) contributions, (6) paper structure\"\n  notable_technique: \"Teaser result figure in intro paragraph 2 — immediately quantifies the gap before any method description\"\n\nfigures:\n  figure_count: 8\n  figure1:\n    type: \"teaser_result\"\n    description: \"Bar chart comparing accuracy of existing methods showing performance gap\"\n    narrative_role: \"Quantifies the problem in the intro before solution is described\"\n    design_elements: [\"grouped bars\", \"accuracy numbers\", \"method labels\"]\n    visual_style: \"Clean bar chart with clear performance gap visualization\"\n  result_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"scatter\"\n      what_compared: \"Accuracy vs efficiency tradeoff across methods\"\n      how_gain_highlighted: \"Aristotle in upper-left (high accuracy, low nodes)\"\n      design_note: \"Dual-axis: accuracy vs search efficiency\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"line_plot\"\n      what_compared: \"Accuracy across reasoning depths\"\n      how_gain_highlighted: \"Aristotle maintains accuracy at higher depths\"\n      design_note: \"Shows robustness to depth\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"grouped_bar\"\n      dimensions_varied: [\"CNF\", \"resolution\", \"search_strategy\"]\n      design_note: \"Red gradient coloring for ablation variants\"\n  figure_narrative_role: \"Fig1(teaser gap) → Fig2(method) → Fig3(ablation) → Fig4(efficiency) → Fig5(depth) → Fig6-7(case studies) → Fig8(error analysis)\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"datasets × accuracy\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"bold_best + underline_second\"\n    statistical_reporting: \"single run\"\n    num_baselines: 6\n    design_note: \"Categorizes methods into LLM-only, symbolic-augmented, and Aristotle\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"CNF\", \"resolution\", \"Prolog_translation\", \"search\"]\n      variation_style: \"checkmark_grid\"\n      design_note: \"Systematic component removal showing each module's contribution\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Extended results, additional models, case studies\"\n    reason: \"Main paper focuses on core 4 datasets\"\n```\n\n## 5. qi2025symbolic_provers.yaml\n\n```yaml\npaper_key: \"qi2025symbolic_provers\"\ntitle: \"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation\"\nvenue: \"ICLR 2025\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"GPT-4o\", \"Claude-3.5-Sonnet\", \"Llama3.1-8B/70B\", \"Gemma2-9B/27B\", \"Mistral-7B/Large\", \"Qwen2.5-7B/32B/72B\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"ID_accuracy\", direction: \"higher_better\"}\n    - {name: \"OOD_accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"ProverQA\", size: \"1500 instances, 3 difficulty levels\"}\n    - {name: \"ProofWriter\", size: \"for transfer eval\"}\n    - {name: \"FOLIO\", size: \"for transfer eval\"}\n  ablation_dimensions: [\"difficulty_level\", \"CoT_vs_direct\", \"finetuning_data_source\", \"ID_vs_OOD\"]\n  training_recipe: {optimizer: \"SFT\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"LLM + symbolic prover (Prover9) for benchmark generation\"\n\npositioning:\n  core_claim: \"Top-down generation combining LLM diversity with Prover9 rigor creates ProverQA benchmark that reveals even SOTA models barely exceed chance on hard FOL problems\"\n  key_results: \"GPT-4o: 50.0%, Claude-3.5: 56.4% on hard; finetuning Llama3.1-8B on ProverQA: +34.6% ID, +7.5% OOD (vs -2.0% ProofWriter, -11.4% FOLIO)\"\n  limitations:\n    - \"Benchmark limited to FOL reasoning\"\n    - \"Top-down generation may not cover all reasoning patterns\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"统一框架型\"\n  hook: \"Existing benchmarks lack reliable ground truth labels and controllable difficulty\"\n  tension: \"Bottom-up benchmark construction introduces label noise and uncontrolled complexity\"\n  key_insight: \"Section 3 — top-down generation (goal → backward to premises) ensures logical coherence by construction\"\n  argument_chain: \"benchmark limitations → top-down generation idea → Prover9 guarantees → difficulty control → model evaluation reveals gaps → finetuning transfer validates quality\"\n  contribution_framing: \"3 contributions: generation framework, benchmark, comprehensive evaluation\"\n  intro_structure: \"4 paragraphs: (1) importance of logical reasoning, (2) criteria for good benchmarks, (3) ProverGen framework, (4) contributions\"\n  notable_technique: \"Table 1 checkmark grid as early positioning device — shows no existing benchmark meets all criteria\"\n\nfigures:\n  figure_count: 2\n  figure1:\n    type: \"method_overview\"\n    description: \"ProverGen pipeline: top-down generation with Prover9\"\n    narrative_role: \"Establishes the generation framework\"\n    design_elements: [\"pipeline flow\", \"Prover9 integration point\"]\n    visual_style: \"Schematic flow diagram\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"bar_chart\"\n      what_compared: \"Model accuracy across difficulty levels\"\n      how_gain_highlighted: \"Performance drop at higher difficulty\"\n      design_note: \"Grouped by difficulty, showing model capability gap\"\n  ablation_figures: []\n  figure_narrative_role: \"Fig1(method) → Fig2(results) — minimal figures, table-heavy paper\"\n\ntables:\n  table_count: 6\n  main_result_table:\n    table_id: \"Table 2\"\n    row_axis: \"methods\"\n    col_axis: \"difficulty levels × accuracy\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_difficulty\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"single run\"\n    num_baselines: 10\n    design_note: \"Comprehensive model comparison across 3 difficulty levels\"\n  ablation_tables:\n    - table_id: \"Table 3\"\n      what_varied: [\"finetuning_data_source\", \"ID_vs_OOD\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Transfer learning comparison showing ProverQA's superiority\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Additional model results, generation statistics\"\n    reason: \"Main paper focuses on key comparisons\"\n```\n\n## 6. dissecting2025.yaml\n\n```yaml\npaper_key: \"dissecting2025\"\ntitle: \"Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation\"\nvenue: \"EMNLP Findings 2025\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"LLaMA-3.1-8B\", \"Gemma-2-9B\", \"Mistral-v0.3-7B\", \"CoT\", \"SFT-NL\", \"SFT-Symbolic\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"atomicity\", direction: \"higher_better\"}\n    - {name: \"CSS\", direction: \"higher_better\"}\n    - {name: \"NSD\", direction: \"higher_better\"}\n    - {name: \"RFI\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"FLD\", size: \"multi-depth\"}\n    - {name: \"FOLIO\", size: \"204\"}\n    - {name: \"ProntoQA\", size: \"500\"}\n  ablation_dimensions: [\"supervision_type_NL_vs_symbolic\", \"reasoning_depth\", \"model_family\"]\n  training_recipe: {optimizer: \"AdamW\", lr: \"1e-6\", hardware: \"4xA100, ~2h per model\"}\n  method_family: \"evaluation framework (accuracy + soundness + probing)\"\n\npositioning:\n  core_claim: \"Three-dimensional evaluation (accuracy + stepwise soundness + representation probing) reveals NL supervision generalizes better but symbolic supervision produces more structurally sound reasoning chains\"\n  key_results: \"SFT-NL: 67.5% on FLD (from 31.7%); symbolic has higher atomicity (24.7% vs 13.0%); probing shows SFT improves generation but not internalized understanding\"\n  limitations:\n    - \"Limited to propositional/FOL reasoning\"\n    - \"Probing only captures linear representations\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"LLMs show improved reasoning but we lack tools to understand what exactly improves\"\n  tension: \"Single-metric evaluation (accuracy) masks critical differences in reasoning quality\"\n  key_insight: \"Section 4 — decomposing evaluation into accuracy/soundness/probing reveals a fundamental NL-vs-symbolic tradeoff\"\n  argument_chain: \"opaque evaluation → 3-dimensional framework → NL vs symbolic comparison → surprising probing results → implications for training design\"\n  contribution_framing: \"3 contributions: evaluation framework, NL-vs-symbolic findings, probing insights\"\n  intro_structure: \"5 paragraphs: (1) LLM reasoning progress, (2) evaluation limitations, (3) proposed framework, (4) key findings preview, (5) paper structure\"\n  notable_technique: \"Previewing surprising findings in intro to create anticipation for the full analysis\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"method_overview\"\n    description: \"Three-dimensional evaluation framework: accuracy, soundness, probing\"\n    narrative_role: \"Establishes the evaluation methodology upfront\"\n    design_elements: [\"three parallel tracks\", \"metric labels\", \"color coding\"]\n    visual_style: \"Schematic diagram with three evaluation dimensions\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Accuracy across reasoning depths for NL vs symbolic supervision\"\n      how_gain_highlighted: \"Symbolic degrades more gracefully at higher depths\"\n      design_note: \"Depth-accuracy curves are the strongest evidence\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"heatmap\"\n      what_compared: \"Probing results (CSS, NSD, RFI) across models and training types\"\n      how_gain_highlighted: \"Color intensity shows where SFT helps vs doesn't\"\n      design_note: \"Compact visualization of multi-dimensional probing results\"\n  ablation_figures:\n    - figure_id: \"Figure 5\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"model_family\", \"supervision_type\"]\n      design_note: \"Cross-model consistency check\"\n  figure_narrative_role: \"Fig1(framework) → Fig2(accuracy overview) → Fig3(depth analysis) → Fig4(probing) → Fig5(cross-model)\"\n\ntables:\n  table_count: 5\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"datasets × metrics (accuracy + soundness)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"single run\"\n    num_baselines: 6\n    design_note: \"Dual-metric reporting (accuracy and soundness side-by-side)\"\n  ablation_tables:\n    - table_id: \"Table 3\"\n      what_varied: [\"supervision_type\", \"reasoning_depth\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Depth-stratified comparison\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Full probing results, additional model comparisons\"\n    reason: \"Probing methodology details too extensive for main text\"\n```\n\n## 7. crest2025.yaml\n\n```yaml\npaper_key: \"crest2025\"\ntitle: \"Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)\"\nvenue: \"NAACL 2025\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"SFT\", \"RFT\", \"STaR\", \"REST-EM\", \"V-STaR\", \"DPO-vanilla\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"ReClor\", size: \"~6k\"}\n    - {name: \"ARC-Challenge\", size: \"2590\"}\n    - {name: \"CSQA\", size: \"~12k\"}\n  ablation_dimensions: [\"follow_up_questions\", \"tolerance_parameter_t\", \"DPO_lambda\", \"sample_count_N\"]\n  training_recipe: {optimizer: \"AdamW\", lr: \"5e-6\", hardware: \"4xA100\"}\n  method_family: \"consistency-driven self-training\"\n\npositioning:\n  core_claim: \"Follow-up question consistency provides richer signal than binary answer correctness for filtering self-training rationales, enabling better SFT+DPO training\"\n  key_results: \"+1.7-1.8% over best baseline on ReClor; consistent gains on ARC-C and CSQA across Llama-3-8B, Gemma-7B, Phi-2\"\n  limitations:\n    - \"Restricted to MCQ format\"\n    - \"All follow-up questions weighted equally\"\n    - \"No teacher-student setting explored\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Self-training with LLM-generated rationales is promising but suffers from false positive rationales\"\n  tension: \"Binary correctness filtering passes rationales with right answers but wrong reasoning\"\n  key_insight: \"Section 3.2 — follow-up questions stress-test rationale quality beyond just checking the final answer\"\n  argument_chain: \"self-training promise → false positive problem → follow-up question consistency → filtered SFT + DPO → multi-model validation\"\n  contribution_framing: \"3 contributions: consistency evaluation method, 4-stage training pipeline, empirical validation\"\n  intro_structure: \"4 paragraphs: (1) self-training promise, (2) false positive problem, (3) CREST solution, (4) contributions\"\n  notable_technique: \"Concrete example of a false positive rationale in intro to make the problem viscerally clear\"\n\nfigures:\n  figure_count: 4\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Example showing a rationale that gets the right answer through wrong reasoning, and how follow-up questions expose it\"\n    narrative_role: \"Makes the false positive problem concrete and motivates the solution\"\n    design_elements: [\"correct vs incorrect rationale comparison\", \"follow-up question examples\", \"red/green highlighting\"]\n    visual_style: \"Two-column comparison with text examples\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"bar_chart\"\n      what_compared: \"Methods across 3 datasets × 3 models\"\n      how_gain_highlighted: \"CREST consistently highest or tied\"\n      design_note: \"3×3 grid layout for comprehensive comparison\"\n  ablation_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"tolerance_t\", \"DPO_lambda\", \"sample_N\"]\n      design_note: \"Sensitivity analysis with clear optimal ranges\"\n  figure_narrative_role: \"Fig1(problem example) → Fig2(method pipeline) → Fig3(main results) → Fig4(sensitivity)\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"datasets × models\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"bold_best + underline_second\"\n    statistical_reporting: \"mean across 3 seeds\"\n    num_baselines: 6\n    design_note: \"Separate sections for each model family\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"follow_up_questions\", \"SFT_only_vs_SFT+DPO\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Isolates contribution of each pipeline stage\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Additional ablations, prompt templates, follow-up question examples\"\n    reason: \"Main text focuses on core comparisons\"\n```\n\nAll seven YAML files have been read and reproduced in their complete, unmodified form above."
      }
    ],
    "totalDurationMs": 67486,
    "totalTokens": 35021,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 8,
      "cache_creation_input_tokens": 9638,
      "cache_read_input_tokens": 18121,
      "output_tokens": 7254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8,
          "output_tokens": 7254,
          "cache_read_input_tokens": 18121,
          "cache_creation_input_tokens": 9638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9638,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "fc4fa99b-6528-446e-929a-a9084a806af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "51a3dd48-b9fc-497e-989a-ab582817220d",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Tool result

_source line 28 · 2026-05-22T13:46:58.818Z_

<details><summary>↩ Tool result · `toolu_01Dw66TbmZZerCBdvJE1w1oL`</summary>

````text
 Here are the complete contents of all 7 YAML files:

## 1. huang2024selfcorrect.yaml

```yaml
paper_key: "huang2024selfcorrect"
title: "Large Language Models Cannot Self-Correct Reasoning Yet"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["standard prompting", "CoT", "self-refine", "multi-agent debate"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "CommonSenseQA", size: "1221"}
    - {name: "HotpotQA", size: "multi-hop"}
  ablation_dimensions: ["feedback_type", "oracle_vs_intrinsic", "iteration_count"]
  training_recipe: {info: "N/A — prompting-based study"}
  method_family: "self-correction analysis"

positioning:
  core_claim: "LLMs cannot self-correct reasoning without external feedback; intrinsic self-correction often degrades performance"
  key_results: "Self-correction without oracle feedback consistently hurts accuracy (GSM8K: -2.4%)"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 2. wang2023sc.yaml

```yaml
paper_key: "wang2023sc"
title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
venue: "ICLR 2023"
full_text_available: false

research:
  baselines: ["greedy CoT", "sample-and-rank", "beam search"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "SVAMP", size: "1000"}
    - {name: "AQuA", size: "254"}
    - {name: "StrategyQA", size: "2290"}
    - {name: "ARC-Challenge", size: "2590"}
  ablation_dimensions: ["num_samples", "temperature", "model_scale"]
  training_recipe: {info: "N/A — decoding strategy"}
  method_family: "self-consistency / majority voting"

positioning:
  core_claim: "Sampling multiple reasoning paths and marginalizing over them via majority voting substantially improves CoT accuracy without any training"
  key_results: "GSM8K: +17.9% over greedy CoT with 40 samples (PaLM-540B)"
  limitations: ["N/A"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 3. li2023diverse.yaml

```yaml
paper_key: "li2023diverse"
title: "Making Language Models Better Reasoners with Step-Aware Verifier"
venue: "ACL 2023"
full_text_available: false

research:
  baselines: ["CoT", "SC-CoT", "voting_verifier"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "MATH", size: "500"}
  ablation_dimensions: ["verifier_granularity", "diverse_prompts", "sample_count"]
  training_recipe: {info: "step-aware verifier training"}
  method_family: "diverse prompting + step-aware verification"

positioning:
  core_claim: "Combining diverse prompting strategies with step-level verification outperforms simple self-consistency"
  key_results: "GSM8K: +3.2% over SC-CoT with step-aware verifier"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 4. rc2025.yaml

```yaml
paper_key: "rc2025"
title: "Representation Consistency for Accurate and Coherent LLM Answer Aggregation"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines: ["majority_voting", "USC", "weighted_voting"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "coherence", direction: "higher_better"}
  datasets:
    - {name: "GSM8K", size: "1319"}
    - {name: "TriviaQA", size: "open-domain"}
    - {name: "MMLU", size: "multi-task"}
  ablation_dimensions: ["representation_type", "aggregation_method", "sample_count"]
  training_recipe: {info: "N/A — aggregation method"}
  method_family: "representation-based answer aggregation"

positioning:
  core_claim: "Aggregating answers based on representation consistency (semantic similarity) outperforms surface-form majority voting for open-ended generation"
  key_results: "N/A"
  limitations: ["N/A"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

## 5. ye2024satlm.yaml

```yaml
paper_key: "ye2024satlm"
title: "SatLM: Satisfiability-Aided Language Models Using Declarative Prompting"
venue: "NeurIPS 2023"
full_text_available: true

research:
  baselines: ["Standard Prompting", "CoT", "ProgLM"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "selective_accuracy", direction: "higher_better"}
  datasets:
    - {name: "GSM", size: "1319"}
    - {name: "GSM-Sys", size: "subset"}
    - {name: "ALGEBRA", size: "textbook problems"}
    - {name: "LSAT", size: "230"}
    - {name: "BoardgameQA", size: "depth 1-3"}
    - {name: "CLUTRR", size: "kinship reasoning"}
    - {name: "ProofWriter", size: "depth-5"}
    - {name: "COLOR", size: "BIG-bench"}
    - {name: "REGEX", size: "StRegex"}
  ablation_dimensions: ["solver_type (SAT vs CoT vs None)", "declarative_vs_imperative", "exemplar_sensitivity", "model_generalization"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "code-davinci-002, gpt-3.5-turbo, text-davinci-003"}
  method_family: "declarative prompting + SAT/SMT solver (Z3)"

positioning:
  core_claim: "Shifting LLMs from generating imperative programs to declarative specifications enables SAT solvers to handle both planning and execution, eliminating planning errors that plague program-aided LMs"
  key_results: "GSM-Sys: 69.4% (+23% over ProgLM); LSAT SoTA 37.4% (from 30.9%); BoardgameQA SoTA 80.7% (from 73.9%); GSM SC: 84.8% matching full-training-set models"
  limitations:
    - "Some problems naturally suit imperative procedures (SatLM slightly lags ProgLM on GSM greedy)"
    - "SAT solver expressiveness limited for quantifiers and nonlinear arithmetic"
    - "One-round parse-solve; no iterative refinement based on solver feedback"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "CoT prompting falls short on problems requiring sophisticated planning and search"
  tension: "Program-aided LMs fix execution errors but not planning errors — LLM must both plan and execute in imperative paradigm"
  key_insight: "Section 2, paragraph 3 — 'Our work tackles both execution errors and, more importantly, planning errors' by shifting to declarative specifications where the solver handles both planning and execution"
  argument_chain: "CoT fails at planning → imperative programs still require LLM planning → declarative specs offload both planning+execution to solver → solver guarantees correctness → 8-dataset validation across 4 task types"
  contribution_framing: "2 key advantages framed as properties: (1) declarative spec closer to problem description, (2) solver guarantees correctness. Plus 3 analysis findings"
  intro_structure: "5 paragraphs: (1) CoT limitations for complex reasoning, (2) parse-plan-execute framework, (3) SatLM with declarative prompting, (4) results summary, (5) analysis findings"
  notable_technique: "The parse-plan-execute decomposition is reframed to show SatLM offloads 2/3 steps (plan+execute) while ProgLM only offloads 1/3 (execute) — powerful comparative framing"

figures:
  figure_count: 4
  figure1:
    type: "problem_illustration"
    description: "Side-by-side comparison of CoT (imperative) vs SatLM (declarative) on a constraint satisfaction problem. Left shows LLM doing parse+plan+execute; right shows LLM only parsing into SAT specification, solver does the rest"
    narrative_role: "Immediately demonstrates the declarative vs imperative paradigm shift on a concrete LSAT-style problem"
    design_elements: ["side-by-side comparison", "code-style specification boxes", "color-coded errors in CoT", "SAT solver icon"]
    visual_style: "Two-column layout with input problem on top, showing the full reasoning trace (left) vs compact specification + solver (right). Green/red annotations mark correct/incorrect steps"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "qualitative_comparison"
      what_compared: "CoT vs ProgLM vs SatLM on arithmetic reasoning — showing specific errors"
      how_gain_highlighted: "Red annotations on errors in CoT and ProgLM; SatLM produces correct answer"
      design_note: "Concrete error examples make the planning-vs-execution distinction tangible"
    - figure_id: "Figure 3"
      viz_type: "qualitative_comparison"
      what_compared: "SatLM variant with CoT solver (declarative spec + LLM solving)"
      how_gain_highlighted: "Shows declarative prompting helps even without symbolic solver"
      design_note: "Isolates contribution of declarative formulation vs symbolic execution"
  ablation_figures: []
  figure_narrative_role: "Fig1(paradigm comparison) → Fig2(concrete error analysis) → Fig3(ablation variant) → Fig4(commonsense parsing examples)"

tables:
  table_count: 7
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets (GSM-Sys, GSM, ALGE, LSAT, BOARD, CLUTRR, PROOF, COLOR, REGEX)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best"
    statistical_reporting: "bootstrap significance tests (p<0.05)"
    num_baselines: 3
    design_note: "Split into greedy and self-consistency decoding blocks; 9 datasets is unusually comprehensive"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["solver_type: SAT_SymSolver vs SAT_CoTSolver vs SAT_NoSolver"]
      variation_style: "full_numbers"
      design_note: "Isolates solver contribution — key insight that declarative prompting helps even without solver"
    - table_id: "Table 3"
      what_varied: ["error_type: planning vs execution"]
      variation_style: "full_numbers"
      design_note: "Error decomposition showing most CoTSolver errors are planning errors"
    - table_id: "Table 5"
      what_varied: ["selective prediction: correct, incorrect, error types (UNSAT, AMBIG)"]
      variation_style: "full_numbers"
      design_note: "Unique to SAT approach — solver feedback enables abstaining from uncertain predictions"
  supplementary_tables:
    in_appendix: true
    content: "Dataset statistics, prompts, exemplar variations (Table 7), cross-model results (Table 6)"
    reason: "Generalization analysis and prompt details too detailed for main text"
```

## 6. xu2024symbcot.yaml

```yaml
paper_key: "xu2024symbcot"
title: "Faithful Logical Reasoning via Symbolic Chain-of-Thought"
venue: "ACL 2024"
full_text_available: true

research:
  baselines: ["Naive Prompting", "CoT", "CoT-SC", "ToT", "CR (Cumulative Reasoning)", "DetermLR", "Logic-LM"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "execution_rate", direction: "higher_better"}
    - {name: "faithfulness_rate", direction: "higher_better"}
  datasets:
    - {name: "PrOntoQA", size: "500"}
    - {name: "ProofWriter", size: "600"}
    - {name: "FOLIO", size: "204"}
    - {name: "LogicalDeduction", size: "300"}
    - {name: "AR-LSAT", size: "230"}
  ablation_dimensions: ["module_contribution (Translator/Planner/Solver/Verifier)", "symbolic_structure (FOL vs CO)", "model_type (GPT-3.5 vs GPT-4)", "reasoning_depth"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "GPT-3.5-turbo-0613, GPT-4-0613"}
  method_family: "fully LLM-based symbolic CoT (no external solver)"

positioning:
  core_claim: "A fully LLM-based framework that integrates symbolic expressions and logic rules into CoT achieves better robustness, faithfulness, and accuracy than external-solver approaches, while scaling better with stronger models"
  key_results: "GPT-4 avg 88.47% (+7.88% over Logic-LM); 100% execution rate (vs Logic-LM ~80%); unfaithful reasoning reduced from 6% to 0% with Verifier; +24.3% improvement from GPT-3.5→GPT-4 (vs Logic-LM +19.9%)"
  limitations:
    - "Only evaluated FOL and Constraint Optimization symbolic structures"
    - "High API cost due to extended symbolic reasoning chains"
    - "Does not enhance LLM's planning capability — relies on LLM's inherent planning"
  relation_to_us: "competitor"

narrative:
  story_type: "突破局限型"
  hook: "Achieving human-like logical reasoning capabilities is crucial for realizing AGI"
  tension: "Existing neurosymbolic systems (LINC, Logic-LM) use LLMs merely as translators, not enhancing LLM's own reasoning; over-reliance on external solvers causes inflexibility, information loss, and unexplainability"
  key_insight: "Section 3 — combining symbolic expressions with natural language in CoT leverages mutual strengths: 'freely expressed implicit intents and contextual information in natural language and rigorous expression in symbolic forms'"
  argument_chain: "CoT unfaithful for logic → external solvers lose information → hybrid symbolic+NL CoT → plan-then-solve with verification → 5-dataset validation + faithfulness analysis"
  contribution_framing: "3 contributions: (1) fully LLM-based framework without external tools, (2) integration of symbolic+NL expressions, (3) plan-then-solve + verification for faithfulness"
  intro_structure: "6 paragraphs: (1) AGI motivation, (2) CoT background, (3) CoT limitations for logic, (4) SymbCoT design with 3 aspects, (5) experimental results, (6) contribution list"
  notable_technique: "Positioning against existing neurosymbolic systems by reframing external solvers as a liability (information loss, inflexibility) rather than a strength"

figures:
  figure_count: 8
  figure1:
    type: "problem_illustration"
    description: "Side-by-side comparison of CoT (overgeneralizes) vs SymbCoT (correctly reasons with symbolic premises and verification) on a logical reasoning problem"
    narrative_role: "Demonstrates CoT's unfaithfulness and SymbCoT's faithfulness on a concrete example"
    design_elements: ["side-by-side layout", "red X / green check marks", "highlighted error text", "symbolic formula display"]
    visual_style: "Two-column with color-coded correctness annotations, showing both the reasoning process and final answer"
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Accuracy across reasoning depths (0-5) on ProofWriter"
      how_gain_highlighted: "SymbCoT maintains high accuracy while baselines degrade; red dual-head arrow shows improvement gap"
      design_note: "Critical depth analysis showing advantage grows with complexity — same pattern as LINC and Logic-LM"
    - figure_id: "Figure 5"
      viz_type: "bar_chart"
      what_compared: "Execution rate across 5 datasets: Logic-LM vs SymbCoT"
      how_gain_highlighted: "SymbCoT achieves 100% across all datasets vs Logic-LM's variable rates"
      design_note: "Strongest evidence against external-solver approaches"
    - figure_id: "Figure 8"
      viz_type: "bar_chart"
      what_compared: "GPT-3.5 vs GPT-4 improvement for each method"
      how_gain_highlighted: "SymbCoT shows largest improvement (+24.3%), demonstrating better scaling with model capability"
      design_note: "Model scaling argument — fully LLM-based approach benefits more from stronger models"
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "grouped_bar"
      dimensions_varied: ["module combinations: full vs w/o Planner&Solver&Verifier vs w/o Translator&Planner&Solver&Verifier"]
      design_note: "6-panel ablation across datasets, color-coded by module configuration"
  figure_narrative_role: "Fig1(motivation) → Fig2(method overview) → Fig3(ablation) → Fig4(depth) → Fig5(execution rate) → Fig6(error analysis) → Fig7(faithfulness) → Fig8(model scaling)"

tables:
  table_count: 2
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "datasets (PrOntoQA, ProofWriter, FOLIO) + Avg"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best + underline_second"
    statistical_reporting: "delta improvement in brackets below best"
    num_baselines: 7
    design_note: "Split by GPT-3.5 and GPT-4 sections; includes many baselines (7) for comprehensive comparison"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["symbolic representation: CO on LogicalDeduction and AR-LSAT"]
      variation_style: "full_numbers"
      design_note: "Demonstrates generalizability across symbolic structures"
  supplementary_tables:
    in_appendix: true
    content: "Symbolic structure details, dataset descriptions, baseline configurations, full prompt templates"
    reason: "Detailed prompt engineering and configuration too long for main text"
```

## 7. xiong2024uncertainty.yaml

```yaml
paper_key: "xiong2024uncertainty"
title: "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs"
venue: "ICLR 2024"
full_text_available: true

research:
  baselines: ["Vanilla prompting", "white-box methods (logit-based)"]
  metrics:
    - {name: "ECE (Expected Calibration Error)", direction: "lower_better"}
    - {name: "AUROC", direction: "higher_better"}
    - {name: "AUPRC", direction: "higher_better"}
  datasets:
    - {name: "CommonsenseQA", size: "commonsense"}
    - {name: "TruthfulQA", size: "commonsense"}
    - {name: "GSM8K", size: "arithmetic"}
    - {name: "DateUnderstanding", size: "symbolic"}
    - {name: "Professional Law/Medicine/Psychology", size: "professional knowledge"}
    - {name: "Business Ethics", size: "ethics"}
  ablation_dimensions: ["prompting_strategy (Vanilla/CoT/Self-Probing/Multi-Step/Top-K)", "sampling_method (Self-Random/Prompting/Misleading)", "aggregation (Consistency/Avg-Conf/Pair-Rank)"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A", model: "GPT-3, GPT-3.5, GPT-4, Vicuna-13B, LLaMA-2-70B"}
  method_family: "black-box confidence elicitation / uncertainty estimation"

positioning:
  core_claim: "LLMs are systematically overconfident when verbalizing confidence (concentrating in 80-100% range), but consistency-based multi-sample methods can substantially improve calibration, especially on structured reasoning tasks"
  key_results: "GSM8K AUROC: 54.8% → 92.7% with consistency-based sampling; white-box vs black-box gap is narrow (AUROC 0.522 vs 0.605); Top-K + Self-Random + Avg-Conf is recommended pipeline"
  limitations:
    - "Professional knowledge tasks remain persistently challenging for all methods"
    - "Black-box methods still trail white-box approaches"
    - "Verbalized confidence mimics human expression patterns (multiples of 5) rather than reflecting true uncertainty"
  relation_to_us: "complementary"

narrative:
  story_type: "化繁为简型"
  hook: "LLMs' tendency to be overconfident poses potential risks for safe deployment"
  tension: "Existing uncertainty methods require model internals (logits, embeddings) — inapplicable to black-box APIs like GPT-4"
  key_insight: "Section 3 — organizing confidence elicitation as prompting × sampling × aggregation creates a systematic design space, revealing that sampling multiple responses is the most impactful component"
  argument_chain: "LLMs overconfident → need black-box uncertainty → systematic 3-component framework → prompting helps calibration but not failure prediction → sampling is the key lever → practical recommendation"
  contribution_framing: "3 contributions: (1) systematic framework for confidence elicitation, (2) comprehensive evaluation across 5 reasoning types and 5 models, (3) practical recommendations"
  intro_structure: "4 paragraphs: (1) LLM deployment risk from overconfidence, (2) black-box constraint, (3) framework overview and approach, (4) key findings and recommendations"
  notable_technique: "The prompting × sampling × aggregation decomposition turns an empirical study into a reusable design framework"

figures:
  figure_count: 6
  figure1:
    type: "method_overview"
    description: "Three-component framework: prompting strategies (5 types) → sampling methods (3 types) → aggregation techniques (3 types)"
    narrative_role: "Establishes the systematic design space for confidence elicitation"
    design_elements: ["three-stage pipeline", "enumeration of options at each stage", "flow arrows"]
    visual_style: "Horizontal pipeline with branching options at each stage"
  result_figures:
    - figure_id: "confidence distribution figure"
      viz_type: "bar_chart"
      what_compared: "Distribution of verbalized confidence values"
      how_gain_highlighted: "Shows clustering in 80-100% range, illustrating overconfidence"
      design_note: "Powerful visual evidence for the overconfidence claim"
  ablation_figures:
    - figure_id: "component comparison figures"
      viz_type: "grouped_bar"
      dimensions_varied: ["prompting strategy", "sampling method", "aggregation technique"]
      design_note: "Systematic comparison across the 3-component design space"
  figure_narrative_role: "Fig1(framework) → confidence distribution → component-wise analysis → task-specific results"

tables:
  table_count: 4
  main_result_table:
    table_id: "main results table"
    row_axis: "methods (prompting × sampling × aggregation combinations)"
    col_axis: "datasets × metrics (ECE, AUROC, AUPRC)"
    row_organization: "by_category"
    col_organization: "grouped_by_metric"
    highlight_strategy: "bold_best"
    statistical_reporting: "mean across datasets"
    num_baselines: 5
    design_note: "Large table covering 3 metrics × 8 datasets × multiple method combinations"
  ablation_tables:
    - table_id: "component ablation"
      what_varied: ["prompting strategy", "sampling method", "aggregation technique"]
      variation_style: "full_numbers"
      design_note: "Isolates each component's contribution systematically"
  supplementary_tables:
    in_appendix: true
    content: "Per-dataset breakdowns, per-model results, prompt templates"
    reason: "Full combinatorial results too large for main text"
```

All 7 files have been read and their complete contents are reproduced above.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "a5fa8656-1a4c-4eff-ae13-797ef6025d67",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "6e280d17-b662-4023-aebc-aeaefc4a354c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read the following YAML files in full and report their complete contents back to me. These are paper distillation files I need to analyze:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/huang2024selfcorrect.yaml\n2. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/wang2023sc.yaml\n3. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/li2023diverse.yaml\n4. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/rc2025.yaml\n5. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/ye2024satlm.yaml\n6. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xu2024symbcot.yaml\n7. /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/xiong2024uncertainty.yaml\n\nRead all files completely and reproduce their content exactly.",
    "agentId": "ab27a990e9775e028",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": " Here are the complete contents of all 7 YAML files:\n\n## 1. huang2024selfcorrect.yaml\n\n```yaml\npaper_key: \"huang2024selfcorrect\"\ntitle: \"Large Language Models Cannot Self-Correct Reasoning Yet\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"standard prompting\", \"CoT\", \"self-refine\", \"multi-agent debate\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM8K\", size: \"1319\"}\n    - {name: \"CommonSenseQA\", size: \"1221\"}\n    - {name: \"HotpotQA\", size: \"multi-hop\"}\n  ablation_dimensions: [\"feedback_type\", \"oracle_vs_intrinsic\", \"iteration_count\"]\n  training_recipe: {info: \"N/A — prompting-based study\"}\n  method_family: \"self-correction analysis\"\n\npositioning:\n  core_claim: \"LLMs cannot self-correct reasoning without external feedback; intrinsic self-correction often degrades performance\"\n  key_results: \"Self-correction without oracle feedback consistently hurts accuracy (GSM8K: -2.4%)\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 2. wang2023sc.yaml\n\n```yaml\npaper_key: \"wang2023sc\"\ntitle: \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\"\nvenue: \"ICLR 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"greedy CoT\", \"sample-and-rank\", \"beam search\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM8K\", size: \"1319\"}\n    - {name: \"SVAMP\", size: \"1000\"}\n    - {name: \"AQuA\", size: \"254\"}\n    - {name: \"StrategyQA\", size: \"2290\"}\n    - {name: \"ARC-Challenge\", size: \"2590\"}\n  ablation_dimensions: [\"num_samples\", \"temperature\", \"model_scale\"]\n  training_recipe: {info: \"N/A — decoding strategy\"}\n  method_family: \"self-consistency / majority voting\"\n\npositioning:\n  core_claim: \"Sampling multiple reasoning paths and marginalizing over them via majority voting substantially improves CoT accuracy without any training\"\n  key_results: \"GSM8K: +17.9% over greedy CoT with 40 samples (PaLM-540B)\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 3. li2023diverse.yaml\n\n```yaml\npaper_key: \"li2023diverse\"\ntitle: \"Making Language Models Better Reasoners with Step-Aware Verifier\"\nvenue: \"ACL 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"CoT\", \"SC-CoT\", \"voting_verifier\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM8K\", size: \"1319\"}\n    - {name: \"MATH\", size: \"500\"}\n  ablation_dimensions: [\"verifier_granularity\", \"diverse_prompts\", \"sample_count\"]\n  training_recipe: {info: \"step-aware verifier training\"}\n  method_family: \"diverse prompting + step-aware verification\"\n\npositioning:\n  core_claim: \"Combining diverse prompting strategies with step-level verification outperforms simple self-consistency\"\n  key_results: \"GSM8K: +3.2% over SC-CoT with step-aware verifier\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 4. rc2025.yaml\n\n```yaml\npaper_key: \"rc2025\"\ntitle: \"Representation Consistency for Accurate and Coherent LLM Answer Aggregation\"\nvenue: \"arXiv 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"majority_voting\", \"USC\", \"weighted_voting\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"coherence\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM8K\", size: \"1319\"}\n    - {name: \"TriviaQA\", size: \"open-domain\"}\n    - {name: \"MMLU\", size: \"multi-task\"}\n  ablation_dimensions: [\"representation_type\", \"aggregation_method\", \"sample_count\"]\n  training_recipe: {info: \"N/A — aggregation method\"}\n  method_family: \"representation-based answer aggregation\"\n\npositioning:\n  core_claim: \"Aggregating answers based on representation consistency (semantic similarity) outperforms surface-form majority voting for open-ended generation\"\n  key_results: \"N/A\"\n  limitations: [\"N/A\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n## 5. ye2024satlm.yaml\n\n```yaml\npaper_key: \"ye2024satlm\"\ntitle: \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\"\nvenue: \"NeurIPS 2023\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Standard Prompting\", \"CoT\", \"ProgLM\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"selective_accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GSM\", size: \"1319\"}\n    - {name: \"GSM-Sys\", size: \"subset\"}\n    - {name: \"ALGEBRA\", size: \"textbook problems\"}\n    - {name: \"LSAT\", size: \"230\"}\n    - {name: \"BoardgameQA\", size: \"depth 1-3\"}\n    - {name: \"CLUTRR\", size: \"kinship reasoning\"}\n    - {name: \"ProofWriter\", size: \"depth-5\"}\n    - {name: \"COLOR\", size: \"BIG-bench\"}\n    - {name: \"REGEX\", size: \"StRegex\"}\n  ablation_dimensions: [\"solver_type (SAT vs CoT vs None)\", \"declarative_vs_imperative\", \"exemplar_sensitivity\", \"model_generalization\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\", model: \"code-davinci-002, gpt-3.5-turbo, text-davinci-003\"}\n  method_family: \"declarative prompting + SAT/SMT solver (Z3)\"\n\npositioning:\n  core_claim: \"Shifting LLMs from generating imperative programs to declarative specifications enables SAT solvers to handle both planning and execution, eliminating planning errors that plague program-aided LMs\"\n  key_results: \"GSM-Sys: 69.4% (+23% over ProgLM); LSAT SoTA 37.4% (from 30.9%); BoardgameQA SoTA 80.7% (from 73.9%); GSM SC: 84.8% matching full-training-set models\"\n  limitations:\n    - \"Some problems naturally suit imperative procedures (SatLM slightly lags ProgLM on GSM greedy)\"\n    - \"SAT solver expressiveness limited for quantifiers and nonlinear arithmetic\"\n    - \"One-round parse-solve; no iterative refinement based on solver feedback\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"CoT prompting falls short on problems requiring sophisticated planning and search\"\n  tension: \"Program-aided LMs fix execution errors but not planning errors — LLM must both plan and execute in imperative paradigm\"\n  key_insight: \"Section 2, paragraph 3 — 'Our work tackles both execution errors and, more importantly, planning errors' by shifting to declarative specifications where the solver handles both planning and execution\"\n  argument_chain: \"CoT fails at planning → imperative programs still require LLM planning → declarative specs offload both planning+execution to solver → solver guarantees correctness → 8-dataset validation across 4 task types\"\n  contribution_framing: \"2 key advantages framed as properties: (1) declarative spec closer to problem description, (2) solver guarantees correctness. Plus 3 analysis findings\"\n  intro_structure: \"5 paragraphs: (1) CoT limitations for complex reasoning, (2) parse-plan-execute framework, (3) SatLM with declarative prompting, (4) results summary, (5) analysis findings\"\n  notable_technique: \"The parse-plan-execute decomposition is reframed to show SatLM offloads 2/3 steps (plan+execute) while ProgLM only offloads 1/3 (execute) — powerful comparative framing\"\n\nfigures:\n  figure_count: 4\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Side-by-side comparison of CoT (imperative) vs SatLM (declarative) on a constraint satisfaction problem. Left shows LLM doing parse+plan+execute; right shows LLM only parsing into SAT specification, solver does the rest\"\n    narrative_role: \"Immediately demonstrates the declarative vs imperative paradigm shift on a concrete LSAT-style problem\"\n    design_elements: [\"side-by-side comparison\", \"code-style specification boxes\", \"color-coded errors in CoT\", \"SAT solver icon\"]\n    visual_style: \"Two-column layout with input problem on top, showing the full reasoning trace (left) vs compact specification + solver (right). Green/red annotations mark correct/incorrect steps\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"qualitative_comparison\"\n      what_compared: \"CoT vs ProgLM vs SatLM on arithmetic reasoning — showing specific errors\"\n      how_gain_highlighted: \"Red annotations on errors in CoT and ProgLM; SatLM produces correct answer\"\n      design_note: \"Concrete error examples make the planning-vs-execution distinction tangible\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"qualitative_comparison\"\n      what_compared: \"SatLM variant with CoT solver (declarative spec + LLM solving)\"\n      how_gain_highlighted: \"Shows declarative prompting helps even without symbolic solver\"\n      design_note: \"Isolates contribution of declarative formulation vs symbolic execution\"\n  ablation_figures: []\n  figure_narrative_role: \"Fig1(paradigm comparison) → Fig2(concrete error analysis) → Fig3(ablation variant) → Fig4(commonsense parsing examples)\"\n\ntables:\n  table_count: 7\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"datasets (GSM-Sys, GSM, ALGE, LSAT, BOARD, CLUTRR, PROOF, COLOR, REGEX)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"bootstrap significance tests (p<0.05)\"\n    num_baselines: 3\n    design_note: \"Split into greedy and self-consistency decoding blocks; 9 datasets is unusually comprehensive\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"solver_type: SAT_SymSolver vs SAT_CoTSolver vs SAT_NoSolver\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Isolates solver contribution — key insight that declarative prompting helps even without solver\"\n    - table_id: \"Table 3\"\n      what_varied: [\"error_type: planning vs execution\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Error decomposition showing most CoTSolver errors are planning errors\"\n    - table_id: \"Table 5\"\n      what_varied: [\"selective prediction: correct, incorrect, error types (UNSAT, AMBIG)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Unique to SAT approach — solver feedback enables abstaining from uncertain predictions\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Dataset statistics, prompts, exemplar variations (Table 7), cross-model results (Table 6)\"\n    reason: \"Generalization analysis and prompt details too detailed for main text\"\n```\n\n## 6. xu2024symbcot.yaml\n\n```yaml\npaper_key: \"xu2024symbcot\"\ntitle: \"Faithful Logical Reasoning via Symbolic Chain-of-Thought\"\nvenue: \"ACL 2024\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Naive Prompting\", \"CoT\", \"CoT-SC\", \"ToT\", \"CR (Cumulative Reasoning)\", \"DetermLR\", \"Logic-LM\"]\n  metrics:\n    - {name: \"accuracy\", direction: \"higher_better\"}\n    - {name: \"execution_rate\", direction: \"higher_better\"}\n    - {name: \"faithfulness_rate\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"PrOntoQA\", size: \"500\"}\n    - {name: \"ProofWriter\", size: \"600\"}\n    - {name: \"FOLIO\", size: \"204\"}\n    - {name: \"LogicalDeduction\", size: \"300\"}\n    - {name: \"AR-LSAT\", size: \"230\"}\n  ablation_dimensions: [\"module_contribution (Translator/Planner/Solver/Verifier)\", \"symbolic_structure (FOL vs CO)\", \"model_type (GPT-3.5 vs GPT-4)\", \"reasoning_depth\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\", model: \"GPT-3.5-turbo-0613, GPT-4-0613\"}\n  method_family: \"fully LLM-based symbolic CoT (no external solver)\"\n\npositioning:\n  core_claim: \"A fully LLM-based framework that integrates symbolic expressions and logic rules into CoT achieves better robustness, faithfulness, and accuracy than external-solver approaches, while scaling better with stronger models\"\n  key_results: \"GPT-4 avg 88.47% (+7.88% over Logic-LM); 100% execution rate (vs Logic-LM ~80%); unfaithful reasoning reduced from 6% to 0% with Verifier; +24.3% improvement from GPT-3.5→GPT-4 (vs Logic-LM +19.9%)\"\n  limitations:\n    - \"Only evaluated FOL and Constraint Optimization symbolic structures\"\n    - \"High API cost due to extended symbolic reasoning chains\"\n    - \"Does not enhance LLM's planning capability — relies on LLM's inherent planning\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Achieving human-like logical reasoning capabilities is crucial for realizing AGI\"\n  tension: \"Existing neurosymbolic systems (LINC, Logic-LM) use LLMs merely as translators, not enhancing LLM's own reasoning; over-reliance on external solvers causes inflexibility, information loss, and unexplainability\"\n  key_insight: \"Section 3 — combining symbolic expressions with natural language in CoT leverages mutual strengths: 'freely expressed implicit intents and contextual information in natural language and rigorous expression in symbolic forms'\"\n  argument_chain: \"CoT unfaithful for logic → external solvers lose information → hybrid symbolic+NL CoT → plan-then-solve with verification → 5-dataset validation + faithfulness analysis\"\n  contribution_framing: \"3 contributions: (1) fully LLM-based framework without external tools, (2) integration of symbolic+NL expressions, (3) plan-then-solve + verification for faithfulness\"\n  intro_structure: \"6 paragraphs: (1) AGI motivation, (2) CoT background, (3) CoT limitations for logic, (4) SymbCoT design with 3 aspects, (5) experimental results, (6) contribution list\"\n  notable_technique: \"Positioning against existing neurosymbolic systems by reframing external solvers as a liability (information loss, inflexibility) rather than a strength\"\n\nfigures:\n  figure_count: 8\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Side-by-side comparison of CoT (overgeneralizes) vs SymbCoT (correctly reasons with symbolic premises and verification) on a logical reasoning problem\"\n    narrative_role: \"Demonstrates CoT's unfaithfulness and SymbCoT's faithfulness on a concrete example\"\n    design_elements: [\"side-by-side layout\", \"red X / green check marks\", \"highlighted error text\", \"symbolic formula display\"]\n    visual_style: \"Two-column with color-coded correctness annotations, showing both the reasoning process and final answer\"\n  result_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Accuracy across reasoning depths (0-5) on ProofWriter\"\n      how_gain_highlighted: \"SymbCoT maintains high accuracy while baselines degrade; red dual-head arrow shows improvement gap\"\n      design_note: \"Critical depth analysis showing advantage grows with complexity — same pattern as LINC and Logic-LM\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"bar_chart\"\n      what_compared: \"Execution rate across 5 datasets: Logic-LM vs SymbCoT\"\n      how_gain_highlighted: \"SymbCoT achieves 100% across all datasets vs Logic-LM's variable rates\"\n      design_note: \"Strongest evidence against external-solver approaches\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"bar_chart\"\n      what_compared: \"GPT-3.5 vs GPT-4 improvement for each method\"\n      how_gain_highlighted: \"SymbCoT shows largest improvement (+24.3%), demonstrating better scaling with model capability\"\n      design_note: \"Model scaling argument — fully LLM-based approach benefits more from stronger models\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"grouped_bar\"\n      dimensions_varied: [\"module combinations: full vs w/o Planner&Solver&Verifier vs w/o Translator&Planner&Solver&Verifier\"]\n      design_note: \"6-panel ablation across datasets, color-coded by module configuration\"\n  figure_narrative_role: \"Fig1(motivation) → Fig2(method overview) → Fig3(ablation) → Fig4(depth) → Fig5(execution rate) → Fig6(error analysis) → Fig7(faithfulness) → Fig8(model scaling)\"\n\ntables:\n  table_count: 2\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"\n    col_axis: \"datasets (PrOntoQA, ProofWriter, FOLIO) + Avg\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"bold_best + underline_second\"\n    statistical_reporting: \"delta improvement in brackets below best\"\n    num_baselines: 7\n    design_note: \"Split by GPT-3.5 and GPT-4 sections; includes many baselines (7) for comprehensive comparison\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"symbolic representation: CO on LogicalDeduction and AR-LSAT\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Demonstrates generalizability across symbolic structures\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Symbolic structure details, dataset descriptions, baseline configurations, full prompt templates\"\n    reason: \"Detailed prompt engineering and configuration too long for main text\"\n```\n\n## 7. xiong2024uncertainty.yaml\n\n```yaml\npaper_key: \"xiong2024uncertainty\"\ntitle: \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\"\nvenue: \"ICLR 2024\"\nfull_text_available: true\n\nresearch:\n  baselines: [\"Vanilla prompting\", \"white-box methods (logit-based)\"]\n  metrics:\n    - {name: \"ECE (Expected Calibration Error)\", direction: \"lower_better\"}\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"AUPRC\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"CommonsenseQA\", size: \"commonsense\"}\n    - {name: \"TruthfulQA\", size: \"commonsense\"}\n    - {name: \"GSM8K\", size: \"arithmetic\"}\n    - {name: \"DateUnderstanding\", size: \"symbolic\"}\n    - {name: \"Professional Law/Medicine/Psychology\", size: \"professional knowledge\"}\n    - {name: \"Business Ethics\", size: \"ethics\"}\n  ablation_dimensions: [\"prompting_strategy (Vanilla/CoT/Self-Probing/Multi-Step/Top-K)\", \"sampling_method (Self-Random/Prompting/Misleading)\", \"aggregation (Consistency/Avg-Conf/Pair-Rank)\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\", model: \"GPT-3, GPT-3.5, GPT-4, Vicuna-13B, LLaMA-2-70B\"}\n  method_family: \"black-box confidence elicitation / uncertainty estimation\"\n\npositioning:\n  core_claim: \"LLMs are systematically overconfident when verbalizing confidence (concentrating in 80-100% range), but consistency-based multi-sample methods can substantially improve calibration, especially on structured reasoning tasks\"\n  key_results: \"GSM8K AUROC: 54.8% → 92.7% with consistency-based sampling; white-box vs black-box gap is narrow (AUROC 0.522 vs 0.605); Top-K + Self-Random + Avg-Conf is recommended pipeline\"\n  limitations:\n    - \"Professional knowledge tasks remain persistently challenging for all methods\"\n    - \"Black-box methods still trail white-box approaches\"\n    - \"Verbalized confidence mimics human expression patterns (multiples of 5) rather than reflecting true uncertainty\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"LLMs' tendency to be overconfident poses potential risks for safe deployment\"\n  tension: \"Existing uncertainty methods require model internals (logits, embeddings) — inapplicable to black-box APIs like GPT-4\"\n  key_insight: \"Section 3 — organizing confidence elicitation as prompting × sampling × aggregation creates a systematic design space, revealing that sampling multiple responses is the most impactful component\"\n  argument_chain: \"LLMs overconfident → need black-box uncertainty → systematic 3-component framework → prompting helps calibration but not failure prediction → sampling is the key lever → practical recommendation\"\n  contribution_framing: \"3 contributions: (1) systematic framework for confidence elicitation, (2) comprehensive evaluation across 5 reasoning types and 5 models, (3) practical recommendations\"\n  intro_structure: \"4 paragraphs: (1) LLM deployment risk from overconfidence, (2) black-box constraint, (3) framework overview and approach, (4) key findings and recommendations\"\n  notable_technique: \"The prompting × sampling × aggregation decomposition turns an empirical study into a reusable design framework\"\n\nfigures:\n  figure_count: 6\n  figure1:\n    type: \"method_overview\"\n    description: \"Three-component framework: prompting strategies (5 types) → sampling methods (3 types) → aggregation techniques (3 types)\"\n    narrative_role: \"Establishes the systematic design space for confidence elicitation\"\n    design_elements: [\"three-stage pipeline\", \"enumeration of options at each stage\", \"flow arrows\"]\n    visual_style: \"Horizontal pipeline with branching options at each stage\"\n  result_figures:\n    - figure_id: \"confidence distribution figure\"\n      viz_type: \"bar_chart\"\n      what_compared: \"Distribution of verbalized confidence values\"\n      how_gain_highlighted: \"Shows clustering in 80-100% range, illustrating overconfidence\"\n      design_note: \"Powerful visual evidence for the overconfidence claim\"\n  ablation_figures:\n    - figure_id: \"component comparison figures\"\n      viz_type: \"grouped_bar\"\n      dimensions_varied: [\"prompting strategy\", \"sampling method\", \"aggregation technique\"]\n      design_note: \"Systematic comparison across the 3-component design space\"\n  figure_narrative_role: \"Fig1(framework) → confidence distribution → component-wise analysis → task-specific results\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"main results table\"\n    row_axis: \"methods (prompting × sampling × aggregation combinations)\"\n    col_axis: \"datasets × metrics (ECE, AUROC, AUPRC)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_metric\"\n    highlight_strategy: \"bold_best\"\n    statistical_reporting: \"mean across datasets\"\n    num_baselines: 5\n    design_note: \"Large table covering 3 metrics × 8 datasets × multiple method combinations\"\n  ablation_tables:\n    - table_id: \"component ablation\"\n      what_varied: [\"prompting strategy\", \"sampling method\", \"aggregation technique\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Isolates each component's contribution systematically\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Per-dataset breakdowns, per-model results, prompt templates\"\n    reason: \"Full combinatorial results too large for main text\"\n```\n\nAll 7 files have been read and their complete contents are reproduced above."
      }
    ],
    "totalDurationMs": 64923,
    "totalTokens": 33605,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 8,
      "cache_creation_input_tokens": 8848,
      "cache_read_input_tokens": 18121,
      "output_tokens": 6628,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8,
          "output_tokens": 6628,
          "cache_read_input_tokens": 18121,
          "cache_creation_input_tokens": 8848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8848,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "a5fa8656-1a4c-4eff-ae13-797ef6025d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "6e280d17-b662-4023-aebc-aeaefc4a354c",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Assistant

_source line 31 · 2026-05-22T13:47:05.027Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all 28 YAML files. Let me also read the existing skill files to understand the current state before generating new ones.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e280d17-b662-4023-aebc-aeaefc4a354c",
  "isSidechain": false,
  "requestId": "req_011CbHiAt8cEnFnvAD5K6P9D",
  "type": "assistant",
  "uuid": "ee4493c4-7e1e-45d9-a23d-b38223e2925a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsR3cEuU9b7SnaWU1HSmQE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23776,
      "cache_read_input_tokens": 30249,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 30249,
          "cache_creation_input_tokens": 23776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23776
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

_source line 32 · 2026-05-22T13:47:05.381Z_

All 28 YAMLs read. Let me check the existing skill files and the project config for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee4493c4-7e1e-45d9-a23d-b38223e2925a",
  "isSidechain": false,
  "requestId": "req_011CbHiAt8cEnFnvAD5K6P9D",
  "type": "assistant",
  "uuid": "aacbb90d-6bd1-4ecf-92dd-d13d5fd22adf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsR3cEuU9b7SnaWU1HSmQE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23776,
      "cache_read_input_tokens": 30249,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 30249,
          "cache_creation_input_tokens": 23776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23776
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

_source line 33 · 2026-05-22T13:47:07.399Z_

<details open><summary>🔧 Tool call — Read · `toolu_019eHxxTivG6hvxt3HXQ5Tzk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aacbb90d-6bd1-4ecf-92dd-d13d5fd22adf",
  "isSidechain": false,
  "requestId": "req_011CbHiAt8cEnFnvAD5K6P9D",
  "type": "assistant",
  "uuid": "6357b433-15db-407d-a9ad-6e21db67aecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsR3cEuU9b7SnaWU1HSmQE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23776,
      "cache_read_input_tokens": 30249,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 30249,
          "cache_creation_input_tokens": 23776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23776
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

_source line 34 · 2026-05-22T13:47:07.666Z_

<details><summary>↩ Tool result · `toolu_01DaAEKUUynHJdPJ54rhUQRj`</summary>

```text
1	---
2	name: distilled-writing
3	description: LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。
4	type: skill
5	---
6	
7	## 叙事类型分布
8	
9	**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverGen）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。
10	
11	## Intro模式
12	
13	**4-5段标准**（9/11，高）：(1)领域→(2)局限→(3)方案→(4)贡献→[可选(5)结构]。SymbCoT/Aristotle例外用6段（多CoT背景或root cause分析段）。
14	
15	**3条贡献标配**（8/11，高）。变体：LINC 2条；Khan 9条numbered insights；SatLM "2 advantages + 3 findings"。
16	
17	**贡献嵌数字**（3/11，中）：DyLoS("+27%")、SatLM("+23%")、SymbCoT("+7.88%")——Intro即有说服力。
18	
19	## 可模仿技巧（按实用性排序）
20	
21	1. **范式对比图**（SatLM Fig1, SymbCoT Fig1）：side-by-side对比旧方法(错误标红)vs新方法(正确标绿)。problem_illustration类Fig1最主流(3/11)。
22	
23	2. **角色重构**（3/11）："LLM is translator not solver"(Logic-LM)；"declarative not imperative"(SatLM)。一句重定义格局。
24	
25	3. **Parse-Plan-Execute分解**（SatLM）：展示offload步骤数(ProgLM 1/3 vs SatLM 2/3)——通用于hybrid系统。
26	
27	4. **对手优势反转**（SymbCoT）：外部solver的reliability重构为"inflexibility+information loss"。
28	
29	5. **Teaser result图放Intro**（Aristotle）：Fig1 bar chart量化问题，未看方法已知需求。
30	
31	6. **诊断baseline**（LINC Scratchpad, SatLM CoTSolver）：中间态baseline隔离组件因果贡献。
32	
33	7. **Mirror figure pair**（Khan Fig3-4）：同指标两设置相反趋势，视觉对称强化论证。
34	
35	8. **Design space分解**（xiong2024）：empirical study组织为prompting×sampling×aggregation三维框架。
36	
37	## Figure编排
38	
39	**Fig1类型**：problem_illustration(3/11)最多；method_overview(3/11)其次；teaser_result(1/11)。
40	
41	**必配图型**（高）：depth-accuracy曲线(5/11 neurosymbolic必做)；execution rate对比(3/11)。
42	
43	**叙事节奏**：motivation/problem → method → main_results(bar) → depth(line) → ablation(grouped_bar) → error_analysis。5篇核心论文(LINC/Logic-LM/Aristotle/SymbCoT/SatLM)均遵循。Figure数量5-8常见。
44	
45	## Table编排
46	
47	**主结果表**（8/11，高）：row=methods(by_category分LLM-only/hybrid)，col=datasets。bold_best通用(8/11)；underline_second(3/11)。delta brackets(SymbCoT)新趋势。Baseline 3-7个。
48	
49	**消融表**：full_numbers(6/11)主流；checkmark_grid(2/11,Aristotle)适合多组件on/off。SatLM增加error type分解表(planning vs execution)——值得借鉴。
50	
51	**统计报告**：多数single run；SatLM bootstrap p<0.05；ProverGen/Dissecting单run。要求正在收紧。
52	
53	**附录**：prompt templates + extra models + error examples(8/11有)。SatLM 7表最多(含exemplar sensitivity/cross-model)。
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dacbc49b-7b81-4eed-b7d3-3e98119cdd51",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "4c2c119b-9f22-4cec-ba13-d9606674abda",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-writing.skill.md",
      "content": "---\nname: distilled-writing\ndescription: LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。\ntype: skill\n---\n\n## 叙事类型分布\n\n**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverGen）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。\n\n## Intro模式\n\n**4-5段标准**（9/11，高）：(1)领域→(2)局限→(3)方案→(4)贡献→[可选(5)结构]。SymbCoT/Aristotle例外用6段（多CoT背景或root cause分析段）。\n\n**3条贡献标配**（8/11，高）。变体：LINC 2条；Khan 9条numbered insights；SatLM \"2 advantages + 3 findings\"。\n\n**贡献嵌数字**（3/11，中）：DyLoS(\"+27%\")、SatLM(\"+23%\")、SymbCoT(\"+7.88%\")——Intro即有说服力。\n\n## 可模仿技巧（按实用性排序）\n\n1. **范式对比图**（SatLM Fig1, SymbCoT Fig1）：side-by-side对比旧方法(错误标红)vs新方法(正确标绿)。problem_illustration类Fig1最主流(3/11)。\n\n2. **角色重构**（3/11）：\"LLM is translator not solver\"(Logic-LM)；\"declarative not imperative\"(SatLM)。一句重定义格局。\n\n3. **Parse-Plan-Execute分解**（SatLM）：展示offload步骤数(ProgLM 1/3 vs SatLM 2/3)——通用于hybrid系统。\n\n4. **对手优势反转**（SymbCoT）：外部solver的reliability重构为\"inflexibility+information loss\"。\n\n5. **Teaser result图放Intro**（Aristotle）：Fig1 bar chart量化问题，未看方法已知需求。\n\n6. **诊断baseline**（LINC Scratchpad, SatLM CoTSolver）：中间态baseline隔离组件因果贡献。\n\n7. **Mirror figure pair**（Khan Fig3-4）：同指标两设置相反趋势，视觉对称强化论证。\n\n8. **Design space分解**（xiong2024）：empirical study组织为prompting×sampling×aggregation三维框架。\n\n## Figure编排\n\n**Fig1类型**：problem_illustration(3/11)最多；method_overview(3/11)其次；teaser_result(1/11)。\n\n**必配图型**（高）：depth-accuracy曲线(5/11 neurosymbolic必做)；execution rate对比(3/11)。\n\n**叙事节奏**：motivation/problem → method → main_results(bar) → depth(line) → ablation(grouped_bar) → error_analysis。5篇核心论文(LINC/Logic-LM/Aristotle/SymbCoT/SatLM)均遵循。Figure数量5-8常见。\n\n## Table编排\n\n**主结果表**（8/11，高）：row=methods(by_category分LLM-only/hybrid)，col=datasets。bold_best通用(8/11)；underline_second(3/11)。delta brackets(SymbCoT)新趋势。Baseline 3-7个。\n\n**消融表**：full_numbers(6/11)主流；checkmark_grid(2/11,Aristotle)适合多组件on/off。SatLM增加error type分解表(planning vs execution)——值得借鉴。\n\n**统计报告**：多数single run；SatLM bootstrap p<0.05；ProverGen/Dissecting单run。要求正在收紧。\n\n**附录**：prompt templates + extra models + error examples(8/11有)。SatLM 7表最多(含exemplar sensitivity/cross-model)。\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  },
  "sourceToolAssistantUUID": "dacbc49b-7b81-4eed-b7d3-3e98119cdd51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T13:47:07.407Z_

<details><summary>↩ Tool result · `toolu_019eHxxTivG6hvxt3HXQ5Tzk`</summary>

```text
1	---
2	name: distilled-research
3	description: LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。
4	type: skill
5	---
6	
7	## 基线与数据集共识
8	
9	**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。
10	
11	**FOL逻辑5件套**（高）：FOLIO(8/28) naturalistic FOL、ProofWriter(8/28) synthetic深度、PrOntoQA(7/28) sanity check、AR-LSAT(4/28) constraint-heavy、LogicalDeduction(3/28)。**数学推理**：GSM8K(10/28)、MATH(5/28)。
12	
13	**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。
14	
15	## 方法范式光谱
16	
17	**LLM→External Solver**（高）：LINC→Logic-LM→SatLM→DyLoS→Aristotle。趋势：单solver→多solver路由→逻辑完备pipeline。SatLM关键：声明式取代命令式，solver处理planning+execution。Aristotle端点：CNF+resolution达99.7%单步准确。
18	
19	**LLM内化Symbolic**（中）：SymbCoT。100%执行率(vs Logic-LM~80%)，模型升级收益更大(+24.3% GPT3.5→4 vs Logic-LM +19.9%)。对立范式。
20	
21	**Consistency/Verification**（高，8/28）：SC→USC→CISC→DSC→CREST→RC。朴素vote→confidence-weighted→difficulty-adaptive→representation-based→follow-up consistency。
22	
23	**Process Reward**（中）：Math-Shepherd, V-STaR, FoVer。formal tool自动生成step-level标签是新趋势。
24	
25	## 实验设计共识
26	
27	**Depth analysis必做**（5/11，高）：accuracy-vs-depth曲线，neurosymbolic核心论据。LINC/Logic-LM/Aristotle/SymbCoT/SatLM均有。
28	
29	**Error taxonomy**（4/11，高）：formalization/planning/execution三类。SatLM: planning error占42-72%是声明式核心论据。
30	
31	**Cross-model**（7/11，高）：GPT-4 + GPT-3.5最低配；开源模型(Llama/Gemma)验证泛化；DyLoS加LoRA小模型。
32	
33	**Selective prediction**（2/11，中）：SatLM利用UNSAT/AMBIG反馈abstain；SATBench揭示UNSAT系统性偏差。
34	
35	## 竞品Claim与高频局限
36	
37	**竞品**：DyLoS—多solver路由(+27%)；Aristotle—逻辑完备(99.7%)；SymbCoT—无外部依赖(100% exe)；SatLM—声明式消除planning error(+23%)；LogicAgent—多视角推理(+7%)。
38	
39	**高频局限**（高）：FOL表达力不足(5/11)；形式化瓶颈(4/11,60-80%错误)；隐含知识盲区(3/11,Aristotle LogiQA仅31%)；LLM过度自信(xiong2024,80-100%区间聚集)；单轮无迭代(SatLM/Logic-LM)。
40	
41	## 研究空白
42	
43	1. **Symbolic × debate零交集**（高）：debate论文(Du/Khan)不用symbolic，反之亦然
44	2. **跨表示一致性检验缺失**：无人检查FOL/SAT/CSP对同一问题是否一致
45	3. **声明式 vs LLM-based symbolic未统一**：SatLM(外部solver)和SymbCoT(内化)互有优劣，无hybrid
46	4. **Uncertainty × symbolic reasoning**：xiong2024的confidence framework未被应用于symbolic pipeline步骤级验证
47	5. **语义级self-refinement缺失**：仅修语法不修语义(Logic-LM)；无人用solver反馈指导语义修正
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6357b433-15db-407d-a9ad-6e21db67aecd",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "d5fa1c18-a18b-4185-a42d-6895086f3890",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md",
      "content": "---\nname: distilled-research\ndescription: LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。\ntype: skill\n---\n\n## 基线与数据集共识\n\n**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。\n\n**FOL逻辑5件套**（高）：FOLIO(8/28) naturalistic FOL、ProofWriter(8/28) synthetic深度、PrOntoQA(7/28) sanity check、AR-LSAT(4/28) constraint-heavy、LogicalDeduction(3/28)。**数学推理**：GSM8K(10/28)、MATH(5/28)。\n\n**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。\n\n## 方法范式光谱\n\n**LLM→External Solver**（高）：LINC→Logic-LM→SatLM→DyLoS→Aristotle。趋势：单solver→多solver路由→逻辑完备pipeline。SatLM关键：声明式取代命令式，solver处理planning+execution。Aristotle端点：CNF+resolution达99.7%单步准确。\n\n**LLM内化Symbolic**（中）：SymbCoT。100%执行率(vs Logic-LM~80%)，模型升级收益更大(+24.3% GPT3.5→4 vs Logic-LM +19.9%)。对立范式。\n\n**Consistency/Verification**（高，8/28）：SC→USC→CISC→DSC→CREST→RC。朴素vote→confidence-weighted→difficulty-adaptive→representation-based→follow-up consistency。\n\n**Process Reward**（中）：Math-Shepherd, V-STaR, FoVer。formal tool自动生成step-level标签是新趋势。\n\n## 实验设计共识\n\n**Depth analysis必做**（5/11，高）：accuracy-vs-depth曲线，neurosymbolic核心论据。LINC/Logic-LM/Aristotle/SymbCoT/SatLM均有。\n\n**Error taxonomy**（4/11，高）：formalization/planning/execution三类。SatLM: planning error占42-72%是声明式核心论据。\n\n**Cross-model**（7/11，高）：GPT-4 + GPT-3.5最低配；开源模型(Llama/Gemma)验证泛化；DyLoS加LoRA小模型。\n\n**Selective prediction**（2/11，中）：SatLM利用UNSAT/AMBIG反馈abstain；SATBench揭示UNSAT系统性偏差。\n\n## 竞品Claim与高频局限\n\n**竞品**：DyLoS—多solver路由(+27%)；Aristotle—逻辑完备(99.7%)；SymbCoT—无外部依赖(100% exe)；SatLM—声明式消除planning error(+23%)；LogicAgent—多视角推理(+7%)。\n\n**高频局限**（高）：FOL表达力不足(5/11)；形式化瓶颈(4/11,60-80%错误)；隐含知识盲区(3/11,Aristotle LogiQA仅31%)；LLM过度自信(xiong2024,80-100%区间聚集)；单轮无迭代(SatLM/Logic-LM)。\n\n## 研究空白\n\n1. **Symbolic × debate零交集**（高）：debate论文(Du/Khan)不用symbolic，反之亦然\n2. **跨表示一致性检验缺失**：无人检查FOL/SAT/CSP对同一问题是否一致\n3. **声明式 vs LLM-based symbolic未统一**：SatLM(外部solver)和SymbCoT(内化)互有优劣，无hybrid\n4. **Uncertainty × symbolic reasoning**：xiong2024的confidence framework未被应用于symbolic pipeline步骤级验证\n5. **语义级self-refinement缺失**：仅修语法不修语义(Logic-LM)；无人用solver反馈指导语义修正\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "6357b433-15db-407d-a9ad-6e21db67aecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-22T13:47:07.661Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DaAEKUUynHJdPJ54rhUQRj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5fa1c18-a18b-4185-a42d-6895086f3890",
  "isSidechain": false,
  "requestId": "req_011CbHiAt8cEnFnvAD5K6P9D",
  "type": "assistant",
  "uuid": "dacbc49b-7b81-4eed-b7d3-3e98119cdd51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsR3cEuU9b7SnaWU1HSmQE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23776,
      "cache_read_input_tokens": 30249,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 30249,
          "cache_creation_input_tokens": 23776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23776
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

_source line 37 · 2026-05-22T13:47:07.714Z_

```json
{
  "parentUuid": "4c2c119b-9f22-4cec-ba13-d9606674abda",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d1aff499-aa33-4a8d-8f0d-b4409693eb15",
  "timestamp": "2026-05-22T13:47:07.714Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-22T13:48:12.759Z_

<details><summary>Logged reasoning block</summary>

```text
I can see the existing skill files have 28 papers distilled already. The task says there are 25 papers with Layer 1 cache, but I actually found 28 YAML files. The existing skill files say "28篇蒸馏" and "11篇深读蒸馏".

Looking at the task parameters:
- 待分析论文: (empty - no new papers to analyze)
- 已有 25 篇论文的 Layer 1 缓存

Wait, there are 28 YAML files but the task says 25. Let me recount... I count 28 files from the glob. 

Since there are no new papers to analyze, all the Layer 1 work is complete. The existing skill files already have content, so I need to check if they need updating or if I should regenerate them based on the current state. Let me focus on doing the Layer 2 cross-paper analysis and then regenerating the two skill files with any necessary updates. The existing skill files have the wrong frontmatter structure — they're missing the required metadata like paper count, paper keys, and distillation timestamp. I need to regenerate them with the proper format that includes all 28 papers in the distilled_from section, and verify the skill content itself is comprehensive enough before finalizing. I'm going through the list of 28 papers that the existing skills are based on, checking their keys and verifying the content is comprehensive. Since there are no new papers to add, I need to focus on reformatting the skills with proper frontmatter fields (scope, version, tags, distilled_from) and ensuring each skill body stays within the 3000 character limit. Let me verify the current character counts and regenerate with the correct structure. Now I'm looking at the frequency distribution across baselines and datasets from the papers. Chain-of-thought appears almost universally, while self-consistency and standard prompting show up in about a third of the papers each. For datasets, GSM8K and FOLIO are the most common benchmarks, with several others appearing in smaller subsets. I'm also tracking which metrics are used—accuracy is standard across all papers, though execution rate and depth-stratified metrics only appear in a handful of specialized approaches.

I'm organizing the methods into distinct families: external solvers that translate to formal systems, internal symbolic reasoning within the LLM, consistency-based voting schemes, multi-agent debate approaches, self-training with verification, evaluation frameworks, uncertainty quantification, and test-time scaling. These represent the major research directions in the field. I'm also noting which papers form the foundation for my own work, including the seminal chain-of-thought and debate papers alongside more recent advances in symbolic translation and scaling.

Now I'm mapping out the competitive landscape—papers like CISC and DSC that directly compete with my approach, versus complementary work in constraint solving and uncertainty estimation that could enhance it. I'm also identifying key limitations across the deep-read papers, particularly around first-order logic expressiveness and the formalization bottleneck that several methods struggle with.

Looking at the specific failure modes, DYLOS hits a 60-80% error rate, and I'm seeing a pattern: implicit knowledge gaps, lack of iterative refinement, missing semantic self-correction, and overconfidence in LLM outputs. The MCQ format constraint and high API costs are practical barriers too. The research gaps are striking—nobody's combining symbolic reasoning with debate mechanisms, there's no cross-representation consistency checking, and uncertainty hasn't been properly integrated with symbolic approaches. I'm also categorizing the papers by their innovation type, with about half falling into the "breaking limitations" category.

Now I'm analyzing the structural patterns across these papers. Most use a 4-5 paragraph introduction with 3 main contributions, though a couple go longer. For Figure 1, I'm seeing they typically illustrate either the problem setup or the method overview, with some variation in how they present the core idea. Looking at the complete breakdown across all eleven papers, method_overview dominates at seven papers, followed by problem_illustration at three, and teaser_result with just one. For presenting results, bar charts work best for the main findings while line plots capture depth analysis, and I notice a few papers use qualitative comparisons. The tables follow a consistent pattern with methods as rows organized by category and datasets as columns, where most papers bold the best results and a few underline the second-best, though the statistical reporting varies—most run once, some use bootstrap p-values, and one averages across seeds. Baseline counts range from three to ten methods typically, and ablation studies tend to show full numbers rather than simplified versions.

Now I'm refining the skill files with proper frontmatter and making sure the body content stays within the character limits while keeping the structure intact. I'm working through how to keep the body content tight while staying under the character limit, aiming to refine what's already there rather than expand it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1aff499-aa33-4a8d-8f0d-b4409693eb15",
  "isSidechain": false,
  "requestId": "req_011CbHiBY77yY3GR27sjdVRz",
  "type": "assistant",
  "uuid": "a2a4b057-adba-45d9-b4d0-517e6204a123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWBySaUscZtrLbfmxshWuT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 54025,
      "output_tokens": 6737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6737,
          "cache_read_input_tokens": 54025,
          "cache_creation_input_tokens": 3108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3108
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

_source line 39 · 2026-05-22T13:48:12.845Z_

Now I have complete data from all 28 papers. The existing skills have outdated frontmatter format. Let me regenerate both skill files with proper frontmatter and refined content based on the full cross-paper analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2a4b057-adba-45d9-b4d0-517e6204a123",
  "isSidechain": false,
  "requestId": "req_011CbHiBY77yY3GR27sjdVRz",
  "type": "assistant",
  "uuid": "49b6422a-86b8-4509-96c8-2adfcd81773d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWBySaUscZtrLbfmxshWuT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 54025,
      "output_tokens": 6737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6737,
          "cache_read_input_tokens": 54025,
          "cache_creation_input_tokens": 3108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3108
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

_source line 40 · 2026-05-22T13:48:26.653Z_

<details open><summary>🔧 Tool call — Write · `toolu_01GKokkdthmWV9RDuWpbrhF8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md",
  "content": "---\nname: distilled-research\ndescription: \"LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。\"\nscope: project\nversion: 2\ntags: [distilled, auto-generated]\ndistilled_from:\n  paper_count: 28\n  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]\n  last_distilled: \"2026-05-22T00:00:00Z\"\n---\n\n## 基线与数据集共识\n\n**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。\n\n**FOL逻辑5件套**（高）：FOLIO(8/28) naturalistic FOL、ProofWriter(8/28) synthetic深度、PrOntoQA(7/28) sanity check、AR-LSAT(4/28) constraint-heavy、LogicalDeduction(3/28)。**数学推理**：GSM8K(10/28)、MATH(5/28)。\n\n**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。\n\n## 方法范式光谱\n\n**LLM→External Solver**（高）：LINC→Logic-LM→SatLM→DyLoS→Aristotle。趋势：单solver→多solver路由→逻辑完备pipeline。SatLM关键：声明式取代命令式，solver处理planning+execution。Aristotle端点：CNF+resolution达99.7%单步准确。\n\n**LLM内化Symbolic**（中）：SymbCoT。100%执行率(vs Logic-LM~80%)，模型升级收益更大(+24.3% GPT3.5→4 vs Logic-LM +19.9%)。对立范式。\n\n**Consistency/Verification**（高，8/28）：SC→USC→CISC→DSC→CREST→RC。朴素vote→confidence-weighted→difficulty-adaptive→representation-based→follow-up consistency。\n\n**Process Reward**（中）：Math-Shepherd, V-STaR, FoVer。formal tool自动生成step-level标签是新趋势。\n\n## 实验设计共识\n\n**Depth analysis必做**（5/11，高）：accuracy-vs-depth曲线，neurosymbolic核心论据。LINC/Logic-LM/Aristotle/SymbCoT/SatLM均有。\n\n**Error taxonomy**（4/11，高）：formalization/planning/execution三类。SatLM: planning error占42-72%是声明式核心论据。\n\n**Cross-model**（7/11，高）：GPT-4 + GPT-3.5最低配；开源模型(Llama/Gemma)验证泛化；DyLoS加LoRA小模型。\n\n**Selective prediction**（2/11，中）：SatLM利用UNSAT/AMBIG反馈abstain；SATBench揭示UNSAT系统性偏差。\n\n## 竞品Claim与高频局限\n\n**竞品**：DyLoS—多solver路由(+27%)；Aristotle—逻辑完备(99.7%)；SymbCoT—无外部依赖(100% exe)；SatLM—声明式消除planning error(+23%)；LogicAgent—多视角推理(+7%)。\n\n**高频局限**（高）：FOL表达力不足(5/11)；形式化瓶颈(4/11,60-80%错误)；隐含知识盲区(3/11,Aristotle LogiQA仅31%)；LLM过度自信(xiong2024,80-100%区间聚集)；单轮无迭代(SatLM/Logic-LM)。\n\n## 研究空白\n\n1. **Symbolic × debate零交集**（高）：debate论文(Du/Khan)不用symbolic，反之亦然\n2. **跨表示一致性检验缺失**：无人检查FOL/SAT/CSP对同一问题是否一致\n3. **声明式 vs LLM-based symbolic未统一**：SatLM(外部solver)和SymbCoT(内化)互有优劣，无hybrid\n4. **Uncertainty × symbolic reasoning**：xiong2024的confidence framework未被应用于symbolic pipeline步骤级验证\n5. **语义级self-refinement缺失**：仅修语法不修语义(Logic-LM)；无人用solver反馈指导语义修正\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49b6422a-86b8-4509-96c8-2adfcd81773d",
  "isSidechain": false,
  "requestId": "req_011CbHiBY77yY3GR27sjdVRz",
  "type": "assistant",
  "uuid": "eb194f9f-f446-4e00-8756-d576752aed19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWBySaUscZtrLbfmxshWuT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 54025,
      "output_tokens": 6737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6737,
          "cache_read_input_tokens": 54025,
          "cache_creation_input_tokens": 3108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3108
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

_source line 41 · 2026-05-22T13:48:26.673Z_

<details><summary>↩ Tool result · `toolu_01GKokkdthmWV9RDuWpbrhF8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb194f9f-f446-4e00-8756-d576752aed19",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "f5737988-ad4f-4ecf-b084-a70181e4a57c",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md",
    "content": "---\nname: distilled-research\ndescription: \"LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。\"\nscope: project\nversion: 2\ntags: [distilled, auto-generated]\ndistilled_from:\n  paper_count: 28\n  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]\n  last_distilled: \"2026-05-22T00:00:00Z\"\n---\n\n## 基线与数据集共识\n\n**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。\n\n**FOL逻辑5件套**（高）：FOLIO(8/28) naturalistic FOL、ProofWriter(8/28) synthetic深度、PrOntoQA(7/28) sanity check、AR-LSAT(4/28) constraint-heavy、LogicalDeduction(3/28)。**数学推理**：GSM8K(10/28)、MATH(5/28)。\n\n**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。\n\n## 方法范式光谱\n\n**LLM→External Solver**（高）：LINC→Logic-LM→SatLM→DyLoS→Aristotle。趋势：单solver→多solver路由→逻辑完备pipeline。SatLM关键：声明式取代命令式，solver处理planning+execution。Aristotle端点：CNF+resolution达99.7%单步准确。\n\n**LLM内化Symbolic**（中）：SymbCoT。100%执行率(vs Logic-LM~80%)，模型升级收益更大(+24.3% GPT3.5→4 vs Logic-LM +19.9%)。对立范式。\n\n**Consistency/Verification**（高，8/28）：SC→USC→CISC→DSC→CREST→RC。朴素vote→confidence-weighted→difficulty-adaptive→representation-based→follow-up consistency。\n\n**Process Reward**（中）：Math-Shepherd, V-STaR, FoVer。formal tool自动生成step-level标签是新趋势。\n\n## 实验设计共识\n\n**Depth analysis必做**（5/11，高）：accuracy-vs-depth曲线，neurosymbolic核心论据。LINC/Logic-LM/Aristotle/SymbCoT/SatLM均有。\n\n**Error taxonomy**（4/11，高）：formalization/planning/execution三类。SatLM: planning error占42-72%是声明式核心论据。\n\n**Cross-model**（7/11，高）：GPT-4 + GPT-3.5最低配；开源模型(Llama/Gemma)验证泛化；DyLoS加LoRA小模型。\n\n**Selective prediction**（2/11，中）：SatLM利用UNSAT/AMBIG反馈abstain；SATBench揭示UNSAT系统性偏差。\n\n## 竞品Claim与高频局限\n\n**竞品**：DyLoS—多solver路由(+27%)；Aristotle—逻辑完备(99.7%)；SymbCoT—无外部依赖(100% exe)；SatLM—声明式消除planning error(+23%)；LogicAgent—多视角推理(+7%)。\n\n**高频局限**（高）：FOL表达力不足(5/11)；形式化瓶颈(4/11,60-80%错误)；隐含知识盲区(3/11,Aristotle LogiQA仅31%)；LLM过度自信(xiong2024,80-100%区间聚集)；单轮无迭代(SatLM/Logic-LM)。\n\n## 研究空白\n\n1. **Symbolic × debate零交集**（高）：debate论文(Du/Khan)不用symbolic，反之亦然\n2. **跨表示一致性检验缺失**：无人检查FOL/SAT/CSP对同一问题是否一致\n3. **声明式 vs LLM-based symbolic未统一**：SatLM(外部solver)和SymbCoT(内化)互有优劣，无hybrid\n4. **Uncertainty × symbolic reasoning**：xiong2024的confidence framework未被应用于symbolic pipeline步骤级验证\n5. **语义级self-refinement缺失**：仅修语法不修语义(Logic-LM)；无人用solver反馈指导语义修正\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 13,
        "lines": [
          " ---",
          " name: distilled-research",
          "-description: LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。",
          "-type: skill",
          "+description: \"LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。\"",
          "+scope: project",
          "+version: 2",
          "+tags: [distilled, auto-generated]",
          "+distilled_from:",
          "+  paper_count: 28",
          "+  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]",
          "+  last_distilled: \"2026-05-22T00:00:00Z\"",
          " ---",
          " ",
          " ## 基线与数据集共识"
        ]
      }
    ],
    "originalFile": "---\nname: distilled-research\ndescription: LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。\ntype: skill\n---\n\n## 基线与数据集共识\n\n**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。\n\n**FOL逻辑5件套**（高）：FOLIO(8/28) naturalistic FOL、ProofWriter(8/28) synthetic深度、PrOntoQA(7/28) sanity check、AR-LSAT(4/28) constraint-heavy、LogicalDeduction(3/28)。**数学推理**：GSM8K(10/28)、MATH(5/28)。\n\n**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。\n\n## 方法范式光谱\n\n**LLM→External Solver**（高）：LINC→Logic-LM→SatLM→DyLoS→Aristotle。趋势：单solver→多solver路由→逻辑完备pipeline。SatLM关键：声明式取代命令式，solver处理planning+execution。Aristotle端点：CNF+resolution达99.7%单步准确。\n\n**LLM内化Symbolic**（中）：SymbCoT。100%执行率(vs Logic-LM~80%)，模型升级收益更大(+24.3% GPT3.5→4 vs Logic-LM +19.9%)。对立范式。\n\n**Consistency/Verification**（高，8/28）：SC→USC→CISC→DSC→CREST→RC。朴素vote→confidence-weighted→difficulty-adaptive→representation-based→follow-up consistency。\n\n**Process Reward**（中）：Math-Shepherd, V-STaR, FoVer。formal tool自动生成step-level标签是新趋势。\n\n## 实验设计共识\n\n**Depth analysis必做**（5/11，高）：accuracy-vs-depth曲线，neurosymbolic核心论据。LINC/Logic-LM/Aristotle/SymbCoT/SatLM均有。\n\n**Error taxonomy**（4/11，高）：formalization/planning/execution三类。SatLM: planning error占42-72%是声明式核心论据。\n\n**Cross-model**（7/11，高）：GPT-4 + GPT-3.5最低配；开源模型(Llama/Gemma)验证泛化；DyLoS加LoRA小模型。\n\n**Selective prediction**（2/11，中）：SatLM利用UNSAT/AMBIG反馈abstain；SATBench揭示UNSAT系统性偏差。\n\n## 竞品Claim与高频局限\n\n**竞品**：DyLoS—多solver路由(+27%)；Aristotle—逻辑完备(99.7%)；SymbCoT—无外部依赖(100% exe)；SatLM—声明式消除planning error(+23%)；LogicAgent—多视角推理(+7%)。\n\n**高频局限**（高）：FOL表达力不足(5/11)；形式化瓶颈(4/11,60-80%错误)；隐含知识盲区(3/11,Aristotle LogiQA仅31%)；LLM过度自信(xiong2024,80-100%区间聚集)；单轮无迭代(SatLM/Logic-LM)。\n\n## 研究空白\n\n1. **Symbolic × debate零交集**（高）：debate论文(Du/Khan)不用symbolic，反之亦然\n2. **跨表示一致性检验缺失**：无人检查FOL/SAT/CSP对同一问题是否一致\n3. **声明式 vs LLM-based symbolic未统一**：SatLM(外部solver)和SymbCoT(内化)互有优劣，无hybrid\n4. **Uncertainty × symbolic reasoning**：xiong2024的confidence framework未被应用于symbolic pipeline步骤级验证\n5. **语义级self-refinement缺失**：仅修语法不修语义(Logic-LM)；无人用solver反馈指导语义修正\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "eb194f9f-f446-4e00-8756-d576752aed19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-22T13:48:40.915Z_

<details open><summary>🔧 Tool call — Write · `toolu_016zGUkHYZDYRzFY8UF8TvXd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-writing.skill.md",
  "content": "---\nname: distilled-writing\ndescription: \"LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。\"\nscope: project\nversion: 2\ntags: [distilled, auto-generated]\ndistilled_from:\n  paper_count: 28\n  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]\n  last_distilled: \"2026-05-22T00:00:00Z\"\n---\n\n## 叙事类型分布\n\n**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverQA）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。\n\n## Intro模式\n\n**4-5段标准**（9/11，高）：(1)领域→(2)局限→(3)方案→(4)贡献→[可选(5)结构]。SymbCoT/Aristotle例外用6段（多CoT背景或root cause分析段）。\n\n**3条贡献标配**（8/11，高）。变体：LINC 2条；Khan 9条numbered insights；SatLM \"2 advantages + 3 findings\"。\n\n**贡献嵌数字**（3/11，中）：DyLoS(\"+27%\")、SatLM(\"+23%\")、SymbCoT(\"+7.88%\")——Intro即有说服力。\n\n## 可模仿技巧（按实用性排序）\n\n1. **范式对比图**（SatLM Fig1, SymbCoT Fig1）：side-by-side对比旧方法(错误标红)vs新方法(正确标绿)。problem_illustration类Fig1最主流(3/11)。\n\n2. **角色重构**（3/11）：\"LLM is translator not solver\"(Logic-LM)；\"declarative not imperative\"(SatLM)。一句重定义格局。\n\n3. **Parse-Plan-Execute分解**（SatLM）：展示offload步骤数(ProgLM 1/3 vs SatLM 2/3)——通用于hybrid系统。\n\n4. **对手优势反转**（SymbCoT）：外部solver的reliability重构为\"inflexibility+information loss\"。\n\n5. **Teaser result图放Intro**（Aristotle）：Fig1 bar chart量化问题，未看方法已知需求。\n\n6. **诊断baseline**（LINC Scratchpad, SatLM CoTSolver）：中间态baseline隔离组件因果贡献。\n\n7. **Mirror figure pair**（Khan Fig3-4）：同指标两设置相反趋势，视觉对称强化论证。\n\n8. **Design space分解**（xiong2024）：empirical study组织为prompting×sampling×aggregation三维框架。\n\n## Figure编排\n\n**Fig1类型**：method_overview(7/11)最多；problem_illustration(3/11)其次；teaser_result(1/11)。\n\n**必配图型**（高）：depth-accuracy曲线(5/11 neurosymbolic必做)；execution rate对比(3/11)。\n\n**叙事节奏**：motivation/problem → method → main_results(bar) → depth(line) → ablation(grouped_bar) → error_analysis。5篇核心论文(LINC/Logic-LM/Aristotle/SymbCoT/SatLM)均遵循。Figure数量5-8常见；Khan极端17图1表。\n\n## Table编排\n\n**主结果表**（8/11，高）：row=methods(by_category分LLM-only/hybrid)，col=datasets。bold_best通用(8/11)；underline_second(3/11)。delta brackets(SymbCoT)新趋势。Baseline 3-10个。\n\n**消融表**：full_numbers(6/11)主流；checkmark_grid(2/11,Aristotle)适合多组件on/off。SatLM增加error type分解表(planning vs execution)——值得借鉴。\n\n**统计报告**：多数single run；SatLM bootstrap p<0.05；CREST mean across 3 seeds。要求正在收紧。\n\n**附录**：prompt templates + extra models + error examples(8/11有)。SatLM 7表最多(含exemplar sensitivity/cross-model)。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5737988-ad4f-4ecf-b084-a70181e4a57c",
  "isSidechain": false,
  "requestId": "req_011CbHiBY77yY3GR27sjdVRz",
  "type": "assistant",
  "uuid": "ad14861d-2cbd-4e5b-ba5b-a211a16e24bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWBySaUscZtrLbfmxshWuT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3108,
      "cache_read_input_tokens": 54025,
      "output_tokens": 6737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6737,
          "cache_read_input_tokens": 54025,
          "cache_creation_input_tokens": 3108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3108
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

_source line 43 · 2026-05-22T13:48:40.930Z_

<details><summary>↩ Tool result · `toolu_016zGUkHYZDYRzFY8UF8TvXd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-writing.skill.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad14861d-2cbd-4e5b-ba5b-a211a16e24bd",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "fa3958ac-80aa-45ae-a23e-af131cf649de",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-writing.skill.md",
    "content": "---\nname: distilled-writing\ndescription: \"LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。\"\nscope: project\nversion: 2\ntags: [distilled, auto-generated]\ndistilled_from:\n  paper_count: 28\n  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]\n  last_distilled: \"2026-05-22T00:00:00Z\"\n---\n\n## 叙事类型分布\n\n**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverQA）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。\n\n## Intro模式\n\n**4-5段标准**（9/11，高）：(1)领域→(2)局限→(3)方案→(4)贡献→[可选(5)结构]。SymbCoT/Aristotle例外用6段（多CoT背景或root cause分析段）。\n\n**3条贡献标配**（8/11，高）。变体：LINC 2条；Khan 9条numbered insights；SatLM \"2 advantages + 3 findings\"。\n\n**贡献嵌数字**（3/11，中）：DyLoS(\"+27%\")、SatLM(\"+23%\")、SymbCoT(\"+7.88%\")——Intro即有说服力。\n\n## 可模仿技巧（按实用性排序）\n\n1. **范式对比图**（SatLM Fig1, SymbCoT Fig1）：side-by-side对比旧方法(错误标红)vs新方法(正确标绿)。problem_illustration类Fig1最主流(3/11)。\n\n2. **角色重构**（3/11）：\"LLM is translator not solver\"(Logic-LM)；\"declarative not imperative\"(SatLM)。一句重定义格局。\n\n3. **Parse-Plan-Execute分解**（SatLM）：展示offload步骤数(ProgLM 1/3 vs SatLM 2/3)——通用于hybrid系统。\n\n4. **对手优势反转**（SymbCoT）：外部solver的reliability重构为\"inflexibility+information loss\"。\n\n5. **Teaser result图放Intro**（Aristotle）：Fig1 bar chart量化问题，未看方法已知需求。\n\n6. **诊断baseline**（LINC Scratchpad, SatLM CoTSolver）：中间态baseline隔离组件因果贡献。\n\n7. **Mirror figure pair**（Khan Fig3-4）：同指标两设置相反趋势，视觉对称强化论证。\n\n8. **Design space分解**（xiong2024）：empirical study组织为prompting×sampling×aggregation三维框架。\n\n## Figure编排\n\n**Fig1类型**：method_overview(7/11)最多；problem_illustration(3/11)其次；teaser_result(1/11)。\n\n**必配图型**（高）：depth-accuracy曲线(5/11 neurosymbolic必做)；execution rate对比(3/11)。\n\n**叙事节奏**：motivation/problem → method → main_results(bar) → depth(line) → ablation(grouped_bar) → error_analysis。5篇核心论文(LINC/Logic-LM/Aristotle/SymbCoT/SatLM)均遵循。Figure数量5-8常见；Khan极端17图1表。\n\n## Table编排\n\n**主结果表**（8/11，高）：row=methods(by_category分LLM-only/hybrid)，col=datasets。bold_best通用(8/11)；underline_second(3/11)。delta brackets(SymbCoT)新趋势。Baseline 3-10个。\n\n**消融表**：full_numbers(6/11)主流；checkmark_grid(2/11,Aristotle)适合多组件on/off。SatLM增加error type分解表(planning vs execution)——值得借鉴。\n\n**统计报告**：多数single run；SatLM bootstrap p<0.05；CREST mean across 3 seeds。要求正在收紧。\n\n**附录**：prompt templates + extra models + error examples(8/11有)。SatLM 7表最多(含exemplar sensitivity/cross-model)。\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 12,
        "newStart": 1,
        "newLines": 18,
        "lines": [
          " ---",
          " name: distilled-writing",
          "-description: LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。",
          "-type: skill",
          "+description: \"LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。\"",
          "+scope: project",
          "+version: 2",
          "+tags: [distilled, auto-generated]",
          "+distilled_from:",
          "+  paper_count: 28",
          "+  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]",
          "+  last_distilled: \"2026-05-22T00:00:00Z\"",
          " ---",
          " ",
          " ## 叙事类型分布",
          " ",
          "-**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverGen）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。",
          "+**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverQA）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。",
          " ",
          " ## Intro模式",
          " "
        ]
      },
      {
        "oldStart": 36,
        "oldLines": 18,
        "newStart": 42,
        "newLines": 18,
        "lines": [
          " ",
          " ## Figure编排",
          " ",
          "-**Fig1类型**：problem_illustration(3/11)最多；method_overview(3/11)其次；teaser_result(1/11)。",
          "+**Fig1类型**：method_overview(7/11)最多；problem_illustration(3/11)其次；teaser_result(1/11)。",
          " ",
          " **必配图型**（高）：depth-accuracy曲线(5/11 neurosymbolic必做)；execution rate对比(3/11)。",
          " ",
          "-**叙事节奏**：motivation/problem → method → main_results(bar) → depth(line) → ablation(grouped_bar) → error_analysis。5篇核心论文(LINC/Logic-LM/Aristotle/SymbCoT/SatLM)均遵循。Figure数量5-8常见。",
          "+**叙事节奏**：motivation/problem → method → main_results(bar) → depth(line) → ablation(grouped_bar) → error_analysis。5篇核心论文(LINC/Logic-LM/Aristotle/SymbCoT/SatLM)均遵循。Figure数量5-8常见；Khan极端17图1表。",
          " ",
          " ## Table编排",
          " ",
          "-**主结果表**（8/11，高）：row=methods(by_category分LLM-only/hybrid)，col=datasets。bold_best通用(8/11)；underline_second(3/11)。delta brackets(SymbCoT)新趋势。Baseline 3-7个。",
          "+**主结果表**（8/11，高）：row=methods(by_category分LLM-only/hybrid)，col=datasets。bold_best通用(8/11)；underline_second(3/11)。delta brackets(SymbCoT)新趋势。Baseline 3-10个。",
          " ",
          " **消融表**：full_numbers(6/11)主流；checkmark_grid(2/11,Aristotle)适合多组件on/off。SatLM增加error type分解表(planning vs execution)——值得借鉴。",
          " ",
          "-**统计报告**：多数single run；SatLM bootstrap p<0.05；ProverGen/Dissecting单run。要求正在收紧。",
          "+**统计报告**：多数single run；SatLM bootstrap p<0.05；CREST mean across 3 seeds。要求正在收紧。",
          " ",
          " **附录**：prompt templates + extra models + error examples(8/11有)。SatLM 7表最多(含exemplar sensitivity/cross-model)。"
        ]
      }
    ],
    "originalFile": "---\nname: distilled-writing\ndescription: LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。\ntype: skill\n---\n\n## 叙事类型分布\n\n**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverGen）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。\n\n## Intro模式\n\n**4-5段标准**（9/11，高）：(1)领域→(2)局限→(3)方案→(4)贡献→[可选(5)结构]。SymbCoT/Aristotle例外用6段（多CoT背景或root cause分析段）。\n\n**3条贡献标配**（8/11，高）。变体：LINC 2条；Khan 9条numbered insights；SatLM \"2 advantages + 3 findings\"。\n\n**贡献嵌数字**（3/11，中）：DyLoS(\"+27%\")、SatLM(\"+23%\")、SymbCoT(\"+7.88%\")——Intro即有说服力。\n\n## 可模仿技巧（按实用性排序）\n\n1. **范式对比图**（SatLM Fig1, SymbCoT Fig1）：side-by-side对比旧方法(错误标红)vs新方法(正确标绿)。problem_illustration类Fig1最主流(3/11)。\n\n2. **角色重构**（3/11）：\"LLM is translator not solver\"(Logic-LM)；\"declarative not imperative\"(SatLM)。一句重定义格局。\n\n3. **Parse-Plan-Execute分解**（SatLM）：展示offload步骤数(ProgLM 1/3 vs SatLM 2/3)——通用于hybrid系统。\n\n4. **对手优势反转**（SymbCoT）：外部solver的reliability重构为\"inflexibility+information loss\"。\n\n5. **Teaser result图放Intro**（Aristotle）：Fig1 bar chart量化问题，未看方法已知需求。\n\n6. **诊断baseline**（LINC Scratchpad, SatLM CoTSolver）：中间态baseline隔离组件因果贡献。\n\n7. **Mirror figure pair**（Khan Fig3-4）：同指标两设置相反趋势，视觉对称强化论证。\n\n8. **Design space分解**（xiong2024）：empirical study组织为prompting×sampling×aggregation三维框架。\n\n## Figure编排\n\n**Fig1类型**：problem_illustration(3/11)最多；method_overview(3/11)其次；teaser_result(1/11)。\n\n**必配图型**（高）：depth-accuracy曲线(5/11 neurosymbolic必做)；execution rate对比(3/11)。\n\n**叙事节奏**：motivation/problem → method → main_results(bar) → depth(line) → ablation(grouped_bar) → error_analysis。5篇核心论文(LINC/Logic-LM/Aristotle/SymbCoT/SatLM)均遵循。Figure数量5-8常见。\n\n## Table编排\n\n**主结果表**（8/11，高）：row=methods(by_category分LLM-only/hybrid)，col=datasets。bold_best通用(8/11)；underline_second(3/11)。delta brackets(SymbCoT)新趋势。Baseline 3-7个。\n\n**消融表**：full_numbers(6/11)主流；checkmark_grid(2/11,Aristotle)适合多组件on/off。SatLM增加error type分解表(planning vs execution)——值得借鉴。\n\n**统计报告**：多数single run；SatLM bootstrap p<0.05；ProverGen/Dissecting单run。要求正在收紧。\n\n**附录**：prompt templates + extra models + error examples(8/11有)。SatLM 7表最多(含exemplar sensitivity/cross-model)。\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "ad14861d-2cbd-4e5b-ba5b-a211a16e24bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "fa3958ac-80aa-45ae-a23e-af131cf649de",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Assistant

_source line 46 · 2026-05-22T13:48:43.344Z_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the files were written correctly and check character counts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa3958ac-80aa-45ae-a23e-af131cf649de",
  "isSidechain": false,
  "requestId": "req_011CbHiJQeMU3fPPT2Le7HR3",
  "type": "assistant",
  "uuid": "a8ff8d48-a00c-4e0a-aaef-6767e953b362",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pdYxydz38Rk3kFGc4UjJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6876,
      "cache_read_input_tokens": 57133,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 57133,
          "cache_creation_input_tokens": 6876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6876
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

_source line 47 · 2026-05-22T13:48:43.344Z_

Let me verify the files and check character counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8ff8d48-a00c-4e0a-aaef-6767e953b362",
  "isSidechain": false,
  "requestId": "req_011CbHiJQeMU3fPPT2Le7HR3",
  "type": "assistant",
  "uuid": "0c8a6171-27a9-46b7-9b3c-a24a67bd2c87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pdYxydz38Rk3kFGc4UjJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6876,
      "cache_read_input_tokens": 57133,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 57133,
          "cache_creation_input_tokens": 6876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6876
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

_source line 48 · 2026-05-22T13:48:44.766Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LTFRv36LPe938Kmxcw9uRv`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-writing.skill.md",
  "description": "Check file sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c8a6171-27a9-46b7-9b3c-a24a67bd2c87",
  "isSidechain": false,
  "requestId": "req_011CbHiJQeMU3fPPT2Le7HR3",
  "type": "assistant",
  "uuid": "f315c836-6048-403f-825c-a7d854d80506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pdYxydz38Rk3kFGc4UjJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6876,
      "cache_read_input_tokens": 57133,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 57133,
          "cache_creation_input_tokens": 6876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6876
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

_source line 49 · 2026-05-22T13:48:44.921Z_

<details><summary>↩ Tool result · `toolu_01LTFRv36LPe938Kmxcw9uRv`</summary>

```text
3817 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md
3684 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-writing.skill.md
7501 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f315c836-6048-403f-825c-a7d854d80506",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "c5ca8194-92cd-4ec6-a101-5ab707ffd9a4",
  "toolUseResult": {
    "stdout": "3817 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md\n3684 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-writing.skill.md\n7501 total",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f315c836-6048-403f-825c-a7d854d80506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-22T13:48:45.509Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016KfpvcR9VDMBrQLfSjnf9t`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus && head -15 distilled-research.skill.md && echo \"---\" && head -15 distilled-writing.skill.md",
  "description": "Verify frontmatter format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5ca8194-92cd-4ec6-a101-5ab707ffd9a4",
  "isSidechain": false,
  "requestId": "req_011CbHiJQeMU3fPPT2Le7HR3",
  "type": "assistant",
  "uuid": "96eac57b-b6cd-48d6-be3e-90dc893e2fb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pdYxydz38Rk3kFGc4UjJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6876,
      "cache_read_input_tokens": 57133,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 57133,
          "cache_creation_input_tokens": 6876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6876
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

_source line 51 · 2026-05-22T13:48:45.616Z_

<details><summary>↩ Tool result · `toolu_016KfpvcR9VDMBrQLfSjnf9t`</summary>

```text
---
name: distilled-research
description: "LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 28
  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 基线与数据集共识

**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。
---
---
name: distilled-writing
description: "LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。"
scope: project
version: 2
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 28
  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]
  last_distilled: "2026-05-22T00:00:00Z"
---

## 叙事类型分布

**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverQA）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96eac57b-b6cd-48d6-be3e-90dc893e2fb9",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "c0735bf1-4888-4f66-9763-b0807f5cc368",
  "toolUseResult": {
    "stdout": "---\nname: distilled-research\ndescription: \"LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。\"\nscope: project\nversion: 2\ntags: [distilled, auto-generated]\ndistilled_from:\n  paper_count: 28\n  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]\n  last_distilled: \"2026-05-22T00:00:00Z\"\n---\n\n## 基线与数据集共识\n\n**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。\n---\n---\nname: distilled-writing\ndescription: \"LLM+Symbolic Reasoning 论文写作经验——叙事结构、Intro模式、Figure/Table编排、可模仿技巧。11篇深读蒸馏。\"\nscope: project\nversion: 2\ntags: [distilled, auto-generated]\ndistilled_from:\n  paper_count: 28\n  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]\n  last_distilled: \"2026-05-22T00:00:00Z\"\n---\n\n## 叙事类型分布\n\n**突破局限型最主流**（5/11：Aristotle, CREST, Khan, SatLM, SymbCoT）——先暴露现有方法缺陷再提出修复。**统一框架型**（2/11：DyLoS, ProverQA）。**跨界迁移型**（2/11：LINC, Logic-LM）。**化繁为简型**（2/11：Dissecting, xiong2024）。",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "96eac57b-b6cd-48d6-be3e-90dc893e2fb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-22T13:48:51.162Z_

<details><summary>Logged reasoning block</summary>

```text
The total file sizes are 3817 and 3684 bytes respectively. But the 3000 char limit is for the body only (after frontmatter). Let me calculate the frontmatter size and check if the body is under 3000 chars.

The frontmatter for research is about 800 bytes (the paper_keys line is very long). So the body would be about 3017 chars. That's just over 3000. Let me check more precisely.

Actually, let me measure the body more precisely by stripping the frontmatter.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0735bf1-4888-4f66-9763-b0807f5cc368",
  "isSidechain": false,
  "requestId": "req_011CbHiJkh78J9MeXcPjoTZ2",
  "type": "assistant",
  "uuid": "bfa54f86-db58-43e5-91a6-fd95b0d23b1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTnpDPG2y32QAGEnqy6dcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 64009,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 64009,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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

_source line 53 · 2026-05-22T13:48:52.475Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016mBoXnqZhe615qQmk8GUBu`</summary>

```json
{
  "command": "for f in /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-{research,writing}.skill.md; do echo \"=== $(basename $f) ===\"; awk '/^---$/{c++; if(c==2) next; next} c>=2' \"$f\" | wc -c; done",
  "description": "Count body characters (after frontmatter)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfa54f86-db58-43e5-91a6-fd95b0d23b1d",
  "isSidechain": false,
  "requestId": "req_011CbHiJkh78J9MeXcPjoTZ2",
  "type": "assistant",
  "uuid": "dc8f68b0-f556-4b1f-9390-9e7a78317682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTnpDPG2y32QAGEnqy6dcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 64009,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 64009,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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

_source line 54 · 2026-05-22T13:48:52.549Z_

<details><summary>↩ Tool result · `toolu_016mBoXnqZhe615qQmk8GUBu`</summary>

```text
=== distilled-research.skill.md ===
3028
=== distilled-writing.skill.md ===
2892
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc8f68b0-f556-4b1f-9390-9e7a78317682",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "d6887a02-79b2-40a0-b7ef-3dabae605664",
  "toolUseResult": {
    "stdout": "=== distilled-research.skill.md ===\n3028\n=== distilled-writing.skill.md ===\n2892",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dc8f68b0-f556-4b1f-9390-9e7a78317682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-22T13:48:55.893Z_

<details><summary>Logged reasoning block</summary>

```text
Research body is 3028 chars, just slightly over the 3000 limit. Let me trim it by about 30 chars. I'll tighten some text.

Writing body is 2892, within limit.

Let me trim the research body slightly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6887a02-79b2-40a0-b7ef-3dabae605664",
  "isSidechain": false,
  "requestId": "req_011CbHiKGLK15RvBDm6pV1ZX",
  "type": "assistant",
  "uuid": "b66ccb14-9158-4e82-8e1e-db2238edc9b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NvAH7ZaRZjkDFcPRKLUjY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 65384,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 65384,
          "cache_creation_input_tokens": 350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 350
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

_source line 56 · 2026-05-22T13:48:56.388Z_

Research body is 3028 chars, slightly over 3000. Let me trim it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b66ccb14-9158-4e82-8e1e-db2238edc9b9",
  "isSidechain": false,
  "requestId": "req_011CbHiKGLK15RvBDm6pV1ZX",
  "type": "assistant",
  "uuid": "4ca38c4c-7631-44cb-b3f2-d79efa356d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NvAH7ZaRZjkDFcPRKLUjY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 65384,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 65384,
          "cache_creation_input_tokens": 350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 350
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

_source line 57 · 2026-05-22T13:48:59.705Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WHNLLJJj9hbXW2cz1X5qhy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md",
  "old_string": "**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。",
  "new_string": "**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11)区分external vs LLM-based；faithfulness(2/11,上升)。ECE/AUROC仅uncertainty。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ca38c4c-7631-44cb-b3f2-d79efa356d3b",
  "isSidechain": false,
  "requestId": "req_011CbHiKGLK15RvBDm6pV1ZX",
  "type": "assistant",
  "uuid": "f53d4e9a-8914-4d8a-ae5a-536beb6adbcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NvAH7ZaRZjkDFcPRKLUjY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 65384,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 65384,
          "cache_creation_input_tokens": 350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 350
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

_source line 58 · 2026-05-22T13:48:59.722Z_

<details><summary>↩ Tool result · `toolu_01WHNLLJJj9hbXW2cz1X5qhy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f53d4e9a-8914-4d8a-ae5a-536beb6adbcc",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "b8a01dcb-7124-4342-ae1f-1146db004f8b",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md",
    "oldString": "**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。",
    "newString": "**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11)区分external vs LLM-based；faithfulness(2/11,上升)。ECE/AUROC仅uncertainty。",
    "originalFile": "---\nname: distilled-research\ndescription: \"LLM+Symbolic Reasoning 领域研究经验——基线/数据集共识、方法趋势、实验设计、研究空白。28篇蒸馏。\"\nscope: project\nversion: 2\ntags: [distilled, auto-generated]\ndistilled_from:\n  paper_count: 28\n  paper_keys: [du2023improving, chen2024usc, taubenfeld2025cisc, dsc2025, fover2025, constraintllm2025, llm_meets_cp2025, satbench2025, logicagent2025, xu2026dylos, aristotle2025, qi2025symbolic_provers, dissecting2025, crest2025, khan2024debating, olausson2023linc, pan2023logiclm, snell2025scaling_tts, multi_path_plan2025, wang2024mathshepherd, hosseini2024vstar, huang2024selfcorrect, wang2023sc, li2023diverse, rc2025, ye2024satlm, xu2024symbcot, xiong2024uncertainty]\n  last_distilled: \"2026-05-22T00:00:00Z\"\n---\n\n## 基线与数据集共识\n\n**基线层级**（8/11深读，高）：Standard → CoT → SC-CoT → neurosymbolic (LINC/Logic-LM/SymbCoT)。2024+必对比至少一个neurosymbolic baseline。来源：Aristotle, DyLoS, SymbCoT。\n\n**FOL逻辑5件套**（高）：FOLIO(8/28) naturalistic FOL、ProofWriter(8/28) synthetic深度、PrOntoQA(7/28) sanity check、AR-LSAT(4/28) constraint-heavy、LogicalDeduction(3/28)。**数学推理**：GSM8K(10/28)、MATH(5/28)。\n\n**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。\n\n## 方法范式光谱\n\n**LLM→External Solver**（高）：LINC→Logic-LM→SatLM→DyLoS→Aristotle。趋势：单solver→多solver路由→逻辑完备pipeline。SatLM关键：声明式取代命令式，solver处理planning+execution。Aristotle端点：CNF+resolution达99.7%单步准确。\n\n**LLM内化Symbolic**（中）：SymbCoT。100%执行率(vs Logic-LM~80%)，模型升级收益更大(+24.3% GPT3.5→4 vs Logic-LM +19.9%)。对立范式。\n\n**Consistency/Verification**（高，8/28）：SC→USC→CISC→DSC→CREST→RC。朴素vote→confidence-weighted→difficulty-adaptive→representation-based→follow-up consistency。\n\n**Process Reward**（中）：Math-Shepherd, V-STaR, FoVer。formal tool自动生成step-level标签是新趋势。\n\n## 实验设计共识\n\n**Depth analysis必做**（5/11，高）：accuracy-vs-depth曲线，neurosymbolic核心论据。LINC/Logic-LM/Aristotle/SymbCoT/SatLM均有。\n\n**Error taxonomy**（4/11，高）：formalization/planning/execution三类。SatLM: planning error占42-72%是声明式核心论据。\n\n**Cross-model**（7/11，高）：GPT-4 + GPT-3.5最低配；开源模型(Llama/Gemma)验证泛化；DyLoS加LoRA小模型。\n\n**Selective prediction**（2/11，中）：SatLM利用UNSAT/AMBIG反馈abstain；SATBench揭示UNSAT系统性偏差。\n\n## 竞品Claim与高频局限\n\n**竞品**：DyLoS—多solver路由(+27%)；Aristotle—逻辑完备(99.7%)；SymbCoT—无外部依赖(100% exe)；SatLM—声明式消除planning error(+23%)；LogicAgent—多视角推理(+7%)。\n\n**高频局限**（高）：FOL表达力不足(5/11)；形式化瓶颈(4/11,60-80%错误)；隐含知识盲区(3/11,Aristotle LogiQA仅31%)；LLM过度自信(xiong2024,80-100%区间聚集)；单轮无迭代(SatLM/Logic-LM)。\n\n## 研究空白\n\n1. **Symbolic × debate零交集**（高）：debate论文(Du/Khan)不用symbolic，反之亦然\n2. **跨表示一致性检验缺失**：无人检查FOL/SAT/CSP对同一问题是否一致\n3. **声明式 vs LLM-based symbolic未统一**：SatLM(外部solver)和SymbCoT(内化)互有优劣，无hybrid\n4. **Uncertainty × symbolic reasoning**：xiong2024的confidence framework未被应用于symbolic pipeline步骤级验证\n5. **语义级self-refinement缺失**：仅修语法不修语义(Logic-LM)；无人用solver反馈指导语义修正\n",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 16,
        "newLines": 7,
        "lines": [
          " ",
          " **FOL逻辑5件套**（高）：FOLIO(8/28) naturalistic FOL、ProofWriter(8/28) synthetic深度、PrOntoQA(7/28) sanity check、AR-LSAT(4/28) constraint-heavy、LogicalDeduction(3/28)。**数学推理**：GSM8K(10/28)、MATH(5/28)。",
          " ",
          "-**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11,LINC/Logic-LM/SymbCoT)区分external vs LLM-based；faithfulness(2/11,上升趋势)。ECE/AUROC仅uncertainty方向。",
          "+**指标**：accuracy通用；depth-stratified accuracy(5/11,高)neurosymbolic必做；execution rate(3/11)区分external vs LLM-based；faithfulness(2/11,上升)。ECE/AUROC仅uncertainty。",
          " ",
          " ## 方法范式光谱",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f53d4e9a-8914-4d8a-ae5a-536beb6adbcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-22T13:49:03.497Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TnTEitngXF4tthkTH7C4CZ`</summary>

```json
{
  "command": "awk '/^---$/{c++; if(c==2) next; next} c>=2' /home/ubuntu/.agent-ml-research-idea_gen_0513_3/skills/projects/symb_invariant_consensus/distilled-research.skill.md | wc -c",
  "description": "Recheck body char count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8a01dcb-7124-4342-ae1f-1146db004f8b",
  "isSidechain": false,
  "requestId": "req_011CbHiKofyGsN52TvQSo2bY",
  "type": "assistant",
  "uuid": "1fd20082-4ca8-4ea3-b019-dc1f80716d4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZDQbyUmWH2g5SugPyGZHN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 65734,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 65734,
          "cache_creation_input_tokens": 452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 452
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

_source line 60 · 2026-05-22T13:49:03.555Z_

<details><summary>↩ Tool result · `toolu_01TnTEitngXF4tthkTH7C4CZ`</summary>

```text
2994
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fd20082-4ca8-4ea3-b019-dc1f80716d4c",
  "isSidechain": false,
  "promptId": "10e3f7e8-43a8-4366-a983-91c4be072f03",
  "type": "user",
  "uuid": "85481c17-1b5f-46b2-b837-e1a69d7da50e",
  "toolUseResult": {
    "stdout": "2994",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1fd20082-4ca8-4ea3-b019-dc1f80716d4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61 · 2026-05-22T13:49:03.557Z_

```json
{
  "parentUuid": "85481c17-1b5f-46b2-b837-e1a69d7da50e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "65930c49-d2a7-4101-8c45-7af2f5445e76",
  "timestamp": "2026-05-22T13:49:03.557Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 62 · 2026-05-22T13:49:09.812Z_

Both skill files now have correct frontmatter and body within 3000 chars:
- `distilled-research.skill.md`: 2994 chars body, 28 papers indexed
- `distilled-writing.skill.md`: 2892 chars body, 11 deep-read papers analyzed

Key updates from this regeneration:
- Frontmatter upgraded to required schema (`scope`, `version`, `tags`, `distilled_from` with full paper_keys list)
- Fig1 type distribution corrected: method_overview(7/11) > problem_illustration(3/11) > teaser_result(1/11)
- Added Khan's 17-figure outlier to figure count range
- Baseline count range updated to 3-10 based on full data

[DISTILL_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65930c49-d2a7-4101-8c45-7af2f5445e76",
  "isSidechain": false,
  "requestId": "req_011CbHiL5NHiJBYz7wjoQyvL",
  "type": "assistant",
  "uuid": "d5ee11bd-c6d2-4c2f-b7df-fc2ed5ccb46f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/distiller_efdee075",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013aPd739DG6Q8Fa32B2z9Qc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 66186,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 259,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 66186,
          "cache_creation_input_tokens": 259,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 259
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

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "d5ee11bd-c6d2-4c2f-b7df-fc2ed5ccb46f",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "d5ee11bd-c6d2-4c2f-b7df-fc2ed5ccb46f",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill symbolic invariance papers into research and writing skills",
  "sessionId": "a1bafaf1-2e39-412f-94cc-d7b92935728c"
}
```

---
