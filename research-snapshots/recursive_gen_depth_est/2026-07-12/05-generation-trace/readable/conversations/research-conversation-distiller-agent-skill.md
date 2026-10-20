# Research conversation: 你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。 ## 核心定位 你不是在"总结论文"。你在回答：**这个研究子领域的人默认怎么做事？** - 总结 =

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/6e30d332-941b-46b3-b605-b2bffa1186bb.jsonl`
- **Structured JSON:** [`910702340001d494fe1c.json`](../../sessions/91/910702340001d494fe1c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T14:54:17.020Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T14:54:17.020Z",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "content": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。\n\n## 核心定位\n\n你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**\n\n- 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列）\n- 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）\n\n## 执行流程\n\n### Step 1: 论文排序\n\n按 (venue 质量 × 时间近度 × 相关度) 打分，确定精读优先级。\n\n### Step 2: Layer 1 — 逐篇精读\n\n对每篇「深度精读」论文：\n\n1. 用 WebFetch 获取原文（arXiv HTML 优先 → abstract 降级）\n2. 精读 intro + experiment sections，同时关注 **contribution statement**（通常在 intro 末段）和 **limitation / future work**（通常在 conclusion 段）\n3. 用 WebFetch 获取关键 figure 图片（至少 Figure 1 + 主结果图）做视觉分析，同时关注全部 **figure/table caption** 和 **正文对 figure/table 的引用段落**\n4. 写入 `distill_tmp/{paper_key}.yaml`，schema 如下：\n\n```yaml\npaper_key: \"{key}\"\ntitle: \"...\"\nvenue: \"{venue} {year}\"\nfull_text_available: true/false\n\nresearch:\n  baselines: [name1, name2]\n  metrics: [{name: \"X\", direction: \"higher_better\"}]\n  datasets: [{name: \"Y\", size: \"...\"}]\n  ablation_dimensions: [dim1, dim2]\n  training_recipe: {optimizer: \"...\", lr: \"...\", hardware: \"...\"}\n  method_family: \"...\"\n\npositioning:\n  core_claim: \"一句话提炼该论文的核心贡献（不是 abstract 复述）\"\n  key_results: \"关键性能数字（如 ImageNet top-1: 82.3% (+1.2%), FLOPs: 4.5G (-40%)）\"\n  limitations: [\"论文自己承认的局限 1\", \"局限 2\"]\n  relation_to_us: \"competitor\"   # competitor / foundation / complementary / orthogonal\n\nnarrative:\n  story_type: \"突破局限型/化繁为简型/规模涌现型/跨界迁移型/统一框架型\"\n  hook: \"第一段如何抓注意力\"\n  tension: \"现有方法局限如何铺垫\"\n  key_insight: \"核心洞察在哪个位置、什么方式揭示\"\n  argument_chain: \"problem → ... → validation\"\n  contribution_framing: \"贡献声明的措辞和数量\"\n  intro_structure: \"段落数和每段功能\"\n  notable_technique: \"叙事上最值得学习的技巧\"\n\nfigures:\n  figure_count: 6\n  figure1:\n    type: \"motivation\"                    # motivation / method_overview / teaser_result / problem_illustration\n    description: \"图的内容描述\"\n    narrative_role: \"在论证链中的作用\"\n    design_elements: [\"对比布局\", \"颜色标注\", \"真实样例\"]\n    visual_style: \"从图片视觉分析得到的布局/配色/标注描述\"\n  result_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"bar_chart\"              # bar_chart / line_plot / heatmap / scatter / qualitative_comparison\n      what_compared: \"对比了什么\"\n      how_gain_highlighted: \"如何突出本方法的优势\"\n      design_note: \"设计上值得借鉴的点\"\n  ablation_figures:\n    - figure_id: \"Figure 6\"\n      viz_type: \"grouped_bar\"\n      dimensions_varied: [\"component A\", \"component B\"]\n      design_note: \"消融图的设计思路\"\n  figure_narrative_role: \"Figure 1 → Figure 2 → ... 的叙事流\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 1\"\n    row_axis: \"methods\"                   # methods / datasets / settings\n    col_axis: \"datasets × metrics\"\n    row_organization: \"by_category\"       # by_category / by_performance / by_year / flat\n    col_organization: \"grouped_by_dataset\" # grouped_by_dataset / grouped_by_metric / flat\n    highlight_strategy: \"bold_best + underline_second\"\n    statistical_reporting: \"mean ± std across 3 runs\"\n    num_baselines: 8\n    design_note: \"表格编排上值得借鉴的点\"\n  ablation_tables:\n    - table_id: \"Table 3\"\n      what_varied: [\"component A\", \"component B\"]\n      variation_style: \"checkmark_grid\"   # checkmark_grid / delta_from_base / full_numbers\n      design_note: \"消融表的呈现思路\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"附录表放了什么\"\n    reason: \"为什么这样拆分主表和附录\"\n```\n\n对「仅摘要」论文：只填 `research` 部分，`narrative`/`figures`/`tables` 标记 `N/A`。\n\n### Step 3: Layer 2 — 跨论文归纳\n\n读取全部 Layer 1 YAML，分两个维度归纳：\n\n**Research 归纳**：\n- 统计 baseline/metric/dataset 出现频率\n- 识别方法论趋势（上升 vs 消退）\n- 提取实验设计共识\n- 竞品 claim 汇总：从各篇的 positioning.core_claim 归纳，按 relation_to_us 分组\n- 共同局限：从各篇的 positioning.limitations 交叉比对，标注出现频率\n- 研究空白：从全部论文覆盖的维度中找出交叉盲区（多数做了 X 但没做 Y）\n\n**Writing 归纳**：\n- 对比各论文叙事结构\n- 识别领域故事类型分布\n- 归纳开篇模式、张力来源、洞察呈现位置\n- 提炼可模仿的叙事策略\n- Figure 1 设计模式分布：从各篇 `figures.figure1.type` 统计，哪种最主流，设计元素共识\n- 结果可视化共识：从 `result_figures.viz_type` 统计主结果常用图表类型，gain 突出手法\n- 消融可视化偏好：从 `ablation_figures.viz_type` 统计，grouped bar / heatmap / 表格哪种主流\n- 图的叙事节奏：从 `figure_narrative_role` 归纳典型 figure 编排（motivation → method → result → ablation）\n- 主结果表编排共识：从 `tables.main_result_table` 归纳行列组织模式、分组策略、baseline 数量范围\n- 高亮与统计报告共识：从 `highlight_strategy` + `statistical_reporting` 统计领域标准做法\n- 消融表呈现偏好：从 `ablation_tables.variation_style` 统计 checkmark grid vs delta vs 完整数字\n- 图表分工模式：从 figure + table 全局看，什么结果用图、什么用表、附录放什么\n\n### Step 4: 生成 Skill 文件\n\n在指定 skill 目录下创建两个 `.skill.md` 文件。\n\n## 质量要求\n\n每条 pattern 必须标注：\n- **支持度**：N/M 篇论文\n- **来源**：至少 1 篇代表性论文 title\n- **置信度**：高（>60%）/ 中（30-60%）/ 低（<30% 但值得注意）\n\n不要输出：\n- 单篇论文的独立总结\n- 没有跨论文共识支撑的孤立观察\n- 显而易见的常识\n\n叙事策略分析（writing skill 核心）：\n- 逐篇拆解 3-5 篇论文的故事结构（故事类型、开篇钩子、张力构建、关键洞察、论证链）\n- 每个分析点引用论文中的具体措辞或结构作为证据\n- 策略建议具体到可直接模仿，不泛泛而谈\n\n## 完成标志\n\n所有工作完成后输出 `[DISTILL_DONE]`。\n\n\n## 任务参数\n\n- 项目: recursive_gen_depth_est\n- Layer 1 输出目录: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/`\n- Skill 输出目录: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/`\n- 深度精读上限: 8 篇\n- 单个 Skill 字数上限: 3000 字符\n\n已有 25 篇论文的 Layer 1 缓存（在 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/` 中），无需重新分析。\n\n## 待分析论文\n\n\n\n## 执行指令\n\n1. 对每篇「深度精读」论文执行 Layer 1 分析，将结构化结果写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/{paper_key}.yaml`\n2. 对「仅摘要」论文，仅提取 research 维度（baseline/metric/dataset），写入同目录\n3. 读取全部 Layer 1 YAML（含已缓存的），执行 Layer 2 跨论文归纳\n4. 生成 `distilled-research.skill.md` 和 `distilled-writing.skill.md`，写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/`\n5. 每个 skill body 不超过 3000 字符\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T14:54:17.024Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T14:54:17.024Z",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

## Round 1

81 recorded events

### User

_source line 3 · 2026-05-21T14:54:17.065Z_

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

- 项目: recursive_gen_depth_est
- Layer 1 输出目录: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/`
- Skill 输出目录: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/`
- 深度精读上限: 8 篇
- 单个 Skill 字数上限: 3000 字符

已有 25 篇论文的 Layer 1 缓存（在 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/` 中），无需重新分析。

## 待分析论文



## 执行指令

1. 对每篇「深度精读」论文执行 Layer 1 分析，将结构化结果写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/{paper_key}.yaml`
2. 对「仅摘要」论文，仅提取 research 维度（baseline/metric/dataset），写入同目录
3. 读取全部 Layer 1 YAML（含已缓存的），执行 Layer 2 跨论文归纳
4. 生成 `distilled-research.skill.md` 和 `distilled-writing.skill.md`，写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/`
5. 每个 skill body 不超过 3000 字符


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "62d2df19-fd3d-4ea8-bcc2-5c710869c4a6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T14:54:17.064Z_

```json
{
  "parentUuid": "62d2df19-fd3d-4ea8-bcc2-5c710869c4a6",
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
  "uuid": "712c77e9-4ecb-4aa8-87f2-c6106307d4bd",
  "timestamp": "2026-05-21T14:54:17.064Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T14:54:17.064Z_

```json
{
  "parentUuid": "712c77e9-4ecb-4aa8-87f2-c6106307d4bd",
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
  "uuid": "fd5d5b16-d571-498f-a5a0-494924ac2658",
  "timestamp": "2026-05-21T14:54:17.064Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T14:54:17.064Z_

```json
{
  "parentUuid": "fd5d5b16-d571-498f-a5a0-494924ac2658",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ed96d1ba-8c65-462a-981c-af9735864652",
  "timestamp": "2026-05-21T14:54:17.064Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
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
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Assistant

_source line 8 · 2026-05-21T14:54:22.444Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task. I'm the Distiller Agent and need to:

1. Check existing Layer 1 YAML caches in the distill_tmp directory
2. No new papers to analyze (the "待分析论文" section is empty)
3. Read all existing Layer 1 YAMLs
4. Execute Layer 2 cross-paper synthesis
5. Generate two skill files

Let me first read the existing cached YAMLs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed96d1ba-8c65-462a-981c-af9735864652",
  "isSidechain": false,
  "requestId": "req_011CbFuVeQf952gFoxRcbpvn",
  "type": "assistant",
  "uuid": "d6797ae5-cddc-430d-82eb-a8b8d6ef5146",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ykGMhkih24MLyGhcMJqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16543,
      "cache_read_input_tokens": 11846,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 16543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16543
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

_source line 9 · 2026-05-21T14:54:24.411Z_

没有新论文需要分析，直接读取已有的 25 篇 Layer 1 缓存，执行 Layer 2 跨论文归纳。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6797ae5-cddc-430d-82eb-a8b8d6ef5146",
  "isSidechain": false,
  "requestId": "req_011CbFuVeQf952gFoxRcbpvn",
  "type": "assistant",
  "uuid": "8b7c9266-4e89-4a74-ada1-26a7fe42f1db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ykGMhkih24MLyGhcMJqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16543,
      "cache_read_input_tokens": 11846,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 16543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16543
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

_source line 10 · 2026-05-21T14:54:25.188Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FVAfyyCskSQwaD5PedGzjU`</summary>

```json
{
  "pattern": "*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b7c9266-4e89-4a74-ada1-26a7fe42f1db",
  "isSidechain": false,
  "requestId": "req_011CbFuVeQf952gFoxRcbpvn",
  "type": "assistant",
  "uuid": "ff857aa7-4b82-4f89-bcd9-5a6642e7fdc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ykGMhkih24MLyGhcMJqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16543,
      "cache_read_input_tokens": 11846,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 16543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16543
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

_source line 11 · 2026-05-21T14:54:25.203Z_

<details><summary>↩ Tool result · `toolu_01FVAfyyCskSQwaD5PedGzjU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2024_demystified.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/alemohammad2024_mad.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/drayson2025_detection_prevents_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/bevendorff2025_two_paradigms.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/synthetic_eggs2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/li2024_mage.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/mohamed2025_broken_telephone.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2024_tale_of_tails.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/finlayson2024_closing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/yi2026_escaping_collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/binoculars2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/fast_detectgpt2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/diveye2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/verma2024_ghostbuster.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/penedo2024_fineweb.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/loki2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/tulchinskii2024_intrinsic_dim.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/editlens2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/cloc2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/qurating2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/mitchell2023_detectgpt.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/shi2025_closer_look.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/wu2025_detection_survey.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/kirchenbauer2023_watermark.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2025_strong_collapse.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff857aa7-4b82-4f89-bcd9-5a6642e7fdc6",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "73c0bef4-ec2d-4159-8b2e-2cec3cce52af",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2024_demystified.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/alemohammad2024_mad.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/drayson2025_detection_prevents_collapse.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/bevendorff2025_two_paradigms.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/synthetic_eggs2026.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/li2024_mage.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/mohamed2025_broken_telephone.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2024_tale_of_tails.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/finlayson2024_closing.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/yi2026_escaping_collapse.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/binoculars2024.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/fast_detectgpt2024.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/diveye2026.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/verma2024_ghostbuster.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/penedo2024_fineweb.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/loki2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/tulchinskii2024_intrinsic_dim.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/editlens2026.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/cloc2025.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/qurating2024.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/mitchell2023_detectgpt.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/shi2025_closer_look.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/wu2025_detection_survey.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/kirchenbauer2023_watermark.yaml",
      "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/dohmatob2025_strong_collapse.yaml"
    ],
    "durationMs": 7,
    "numFiles": 25,
    "truncated": false
  },
  "sourceToolAssistantUUID": "ff857aa7-4b82-4f89-bcd9-5a6642e7fdc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T14:54:25.405Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QPCEUgstVADfVx6mXM3mQG`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/ 2>/dev/null || echo \"SKILL_DIR_EMPTY\"",
  "description": "Check existing skill files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73c0bef4-ec2d-4159-8b2e-2cec3cce52af",
  "isSidechain": false,
  "requestId": "req_011CbFuVeQf952gFoxRcbpvn",
  "type": "assistant",
  "uuid": "34ae5eba-450a-41d8-868d-f91273383c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ykGMhkih24MLyGhcMJqf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16543,
      "cache_read_input_tokens": 11846,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 376,
          "cache_read_input_tokens": 11846,
          "cache_creation_input_tokens": 16543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16543
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "e4d14a6c-ef3e-4048-aa2f-3733e14df4d1",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Tool result

_source line 15 · 2026-05-21T14:54:25.568Z_

<details><summary>↩ Tool result · `toolu_01QPCEUgstVADfVx6mXM3mQG`</summary>

```text
distilled-research.skill.md
distilled-writing.skill.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34ae5eba-450a-41d8-868d-f91273383c95",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "e4d14a6c-ef3e-4048-aa2f-3733e14df4d1",
  "toolUseResult": {
    "stdout": "distilled-research.skill.md\ndistilled-writing.skill.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "34ae5eba-450a-41d8-868d-f91273383c95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T14:54:28.498Z_

已有 25 篇缓存和旧 skill 文件。开始批量读取所有 YAML。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4d14a6c-ef3e-4048-aa2f-3733e14df4d1",
  "isSidechain": false,
  "requestId": "req_011CbFuWGd1CjKbbSkNd5vBh",
  "type": "assistant",
  "uuid": "f89e0ce6-1cf7-437d-aa2a-8c952de8a947",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjjf2w5s9J5raXosdfqvPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 28389,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 28389,
          "cache_creation_input_tokens": 1589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1589
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

_source line 17 · 2026-05-21T14:54:32.376Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01L5PAycANQoAxBULGQfWrCX`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Read all 25 YAML files",
  "prompt": "Read all 25 YAML files in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/ and return their complete contents concatenated together. The files are:\n\ndohmatob2024_demystified.yaml\nalemohammad2024_mad.yaml\ndrayson2025_detection_prevents_collapse.yaml\nbevendorff2025_two_paradigms.yaml\nsynthetic_eggs2026.yaml\nli2024_mage.yaml\nmohamed2025_broken_telephone.yaml\ndohmatob2024_tale_of_tails.yaml\nfinlayson2024_closing.yaml\nyi2026_escaping_collapse.yaml\nbinoculars2024.yaml\nfast_detectgpt2024.yaml\ndiveye2026.yaml\nverma2024_ghostbuster.yaml\npenedo2024_fineweb.yaml\nloki2025.yaml\ntulchinskii2024_intrinsic_dim.yaml\neditlens2026.yaml\ncloc2025.yaml\nqurating2024.yaml\nmitchell2023_detectgpt.yaml\nshi2025_closer_look.yaml\nwu2025_detection_survey.yaml\nkirchenbauer2023_watermark.yaml\ndohmatob2025_strong_collapse.yaml\n\nRead every single file completely and return all content. This is a read-only research task, do NOT write any files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f89e0ce6-1cf7-437d-aa2a-8c952de8a947",
  "isSidechain": false,
  "requestId": "req_011CbFuWGd1CjKbbSkNd5vBh",
  "type": "assistant",
  "uuid": "4c147d6c-e6a5-4106-a201-df56d23fe8d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjjf2w5s9J5raXosdfqvPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 28389,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 28389,
          "cache_creation_input_tokens": 1589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1589
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

_source line 18 · 2026-05-21T15:05:05.906Z_

<details><summary>↩ Tool result · `toolu_01L5PAycANQoAxBULGQfWrCX`</summary>

````text
&lt;persisted-output>
Output too large (106KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/toolu_01L5PAycANQoAxBULGQfWrCX.json

Preview (first 2KB):
[
  {
    "type": "text",
    "text": "Here are the complete contents of all 25 YAML files:\n\n---\n\n**1. dohmatob2024_demystified.yaml**\n\n```yaml\npaper_key: \"dohmatob2024_demystified\"\ntitle: \"Model Collapse Demystified: The Case of Regression\"\nvenue: \"NeurIPS 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"no-collapse baseline (real data only)\", \"adaptive regularization\"]\n  metrics:\n    - {name: \"test risk / prediction error\", direction: \"lower_better\"}\n    - {name: \"scaling law exponent\", direction: \"context_dependent\"}\n  datasets:\n    - {name: \"synthetic high-dimensional regression\", size: \"theoretical\"}\n  ablation_dimensions: [\"number of recursive generations\", \"spectral decay rate\", \"source condition\", \"regularization strength\"]\n  training_recipe: {optimizer: \"closed-form / ridge regression\", lr: \"N/A\", hardware: \"theoretical\"}\n  method_family: \"theoretical analysis of model collapse in regression\"\n\npositioning:\n  core_claim: \"Analytic formulae characterizing model collapse in high-dimensional regression reveal modified scaling laws with crossover phenomena from fast to slow rates\"\n  key_results: \"Derived closed-form expressions for collapse dynamics; proposed adaptive regularization as mitigation\"\n  limitations: [\"limited to regression setting\", \"Gaussian assumptions\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**2. alemohammad2024_mad.yaml**\n\n```yaml\npaper_key: \"alemohammad2024_mad\"\ntitle: \"Self-Consuming Generative Models Go MAD\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"real data baseline\", \"mixed real+synthetic training\"]\n  metrics:\n    - {name: \"precision (quality)\", direction: \"higher_better\"}\n    - {name: \"recall (diversity)\", direction: \"higher_better\"}\n    - {name: \"FID\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"FFHQ (image generati
...
&lt;/persisted-output>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "4c147d6c-e6a5-4106-a201-df56d23fe8d0",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "0e6e1a9c-3912-4872-984a-1a18d7005762",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read all 25 YAML files in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp/ and return their complete contents concatenated together. The files are:\n\ndohmatob2024_demystified.yaml\nalemohammad2024_mad.yaml\ndrayson2025_detection_prevents_collapse.yaml\nbevendorff2025_two_paradigms.yaml\nsynthetic_eggs2026.yaml\nli2024_mage.yaml\nmohamed2025_broken_telephone.yaml\ndohmatob2024_tale_of_tails.yaml\nfinlayson2024_closing.yaml\nyi2026_escaping_collapse.yaml\nbinoculars2024.yaml\nfast_detectgpt2024.yaml\ndiveye2026.yaml\nverma2024_ghostbuster.yaml\npenedo2024_fineweb.yaml\nloki2025.yaml\ntulchinskii2024_intrinsic_dim.yaml\neditlens2026.yaml\ncloc2025.yaml\nqurating2024.yaml\nmitchell2023_detectgpt.yaml\nshi2025_closer_look.yaml\nwu2025_detection_survey.yaml\nkirchenbauer2023_watermark.yaml\ndohmatob2025_strong_collapse.yaml\n\nRead every single file completely and return all content. This is a read-only research task, do NOT write any files.",
    "agentId": "af75b63db3ca0cde3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the complete contents of all 25 YAML files:\n\n---\n\n**1. dohmatob2024_demystified.yaml**\n\n```yaml\npaper_key: \"dohmatob2024_demystified\"\ntitle: \"Model Collapse Demystified: The Case of Regression\"\nvenue: \"NeurIPS 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"no-collapse baseline (real data only)\", \"adaptive regularization\"]\n  metrics:\n    - {name: \"test risk / prediction error\", direction: \"lower_better\"}\n    - {name: \"scaling law exponent\", direction: \"context_dependent\"}\n  datasets:\n    - {name: \"synthetic high-dimensional regression\", size: \"theoretical\"}\n  ablation_dimensions: [\"number of recursive generations\", \"spectral decay rate\", \"source condition\", \"regularization strength\"]\n  training_recipe: {optimizer: \"closed-form / ridge regression\", lr: \"N/A\", hardware: \"theoretical\"}\n  method_family: \"theoretical analysis of model collapse in regression\"\n\npositioning:\n  core_claim: \"Analytic formulae characterizing model collapse in high-dimensional regression reveal modified scaling laws with crossover phenomena from fast to slow rates\"\n  key_results: \"Derived closed-form expressions for collapse dynamics; proposed adaptive regularization as mitigation\"\n  limitations: [\"limited to regression setting\", \"Gaussian assumptions\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**2. alemohammad2024_mad.yaml**\n\n```yaml\npaper_key: \"alemohammad2024_mad\"\ntitle: \"Self-Consuming Generative Models Go MAD\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"real data baseline\", \"mixed real+synthetic training\"]\n  metrics:\n    - {name: \"precision (quality)\", direction: \"higher_better\"}\n    - {name: \"recall (diversity)\", direction: \"higher_better\"}\n    - {name: \"FID\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"FFHQ (image generation)\", size: \"70K\"}\n    - {name: \"MNIST\", size: \"60K\"}\n  ablation_dimensions: [\"fresh real data ratio\", \"number of autophagous generations\", \"quality-diversity tradeoff\"]\n  training_recipe: {optimizer: \"N/A (generative models)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"theoretical + empirical analysis of autophagous (self-consuming) generative loops\"\n\npositioning:\n  core_claim: \"Without sufficient fresh real data in each generation, self-consuming generative models are doomed to have quality or diversity progressively decrease (Model Autophagy Disorder)\"\n  key_results: \"Three regimes identified: fully synthetic → collapse; synthetic+sampling bias → quality loss; synthetic+fresh data → stable if ratio sufficient\"\n  limitations: [\"primarily image domain\", \"simplified generation pipeline\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**3. drayson2025_detection_prevents_collapse.yaml**\n\n```yaml\npaper_key: \"drayson2025_detection_prevents_collapse\"\ntitle: \"Machine-generated text detection prevents language model collapse\"\nvenue: \"EMNLP 2025 Findings\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"training on purely human data\", \"training on unfiltered mixed data\"]\n  metrics:\n    - {name: \"perplexity\", direction: \"lower_better\"}\n    - {name: \"text diversity\", direction: \"higher_better\"}\n    - {name: \"downstream task performance\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GPT-2 generated text\", size: \"N/A\"}\n    - {name: \"SmolLM2 generated text\", size: \"N/A\"}\n  ablation_dimensions: [\"model family (GPT-2 vs SmolLM2)\", \"model size (124M to 1.7B)\", \"number of recursive generations\", \"detection threshold\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"detection-based filtering + importance resampling for collapse prevention\"\n\npositioning:\n  core_claim: \"Using machine-generated text detectors to filter training data not only prevents model collapse but improves performance beyond training on purely human data\"\n  key_results: \"Detection + resampling outperforms both pure human data and unfiltered mixed data across GPT-2 and SmolLM2 families\"\n  limitations: [\"limited model families tested\", \"relies on detector quality\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**4. bevendorff2025_two_paradigms.yaml**\n\n```yaml\npaper_key: \"bevendorff2025_two_paradigms\"\ntitle: \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\"\nvenue: \"ACL 2025 Findings\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Binoculars (Hans et al., 2024) zero-shot detector\"\n    - \"SVM with TF-IDF word unigrams (800 features)\"\n    - \"LoRA-fine-tuned Mistral-7B binary classifier\"\n    - \"OpenAI RoBERTa-based GPT-2 detector (Solaiman et al., 2019)\"\n    - \"Ghostbuster (Verma et al., 2024)\"\n    - \"GPT-Sentinel (Chen et al., 2023)\"\n    - \"DetectGPT (Mitchell et al., 2023)\"\n    - \"Fast-DetectGPT (Bao et al., 2023)\"\n    - \"DetectLLM (Su et al., 2023a)\"\n    - \"LLMDet (Wu et al., 2023)\"\n  metrics:\n    - {name: \"False Negative Rate (FNR)\", direction: \"lower_better\"}\n    - {name: \"False Positive Rate (FPR)\", direction: \"lower_better\"}\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"Accuracy\", direction: \"higher_better\"}\n    - {name: \"Precision-Recall curve\", direction: \"higher_better\"}\n    - {name: \"c@1 (accuracy with non-answers)\", direction: \"higher_better\"}\n    - {name: \"Cohen's d (effect size)\", direction: \"N/A\"}\n    - {name: \"Character 3-gram entropy (bits)\", direction: \"N/A\"}\n    - {name: \"MTLD (lexical diversity)\", direction: \"N/A\"}\n    - {name: \"Flesch reading ease\", direction: \"N/A\"}\n    - {name: \"Compression-based cosine (CBC)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"PAN'24 (extended with GPT-4o, 4o-mini, o1)\", size: \"1,359 human + 23,094 LLM texts, 15 LLMs\"}\n    - {name: \"Human Detectors (HD)\", size: \"150 human + 150 LLM texts, 5 LLMs\"}\n    - {name: \"Ghostbuster (GB) Essays\", size: \"994 human + 6,000 LLM texts, 6 LLMs\"}\n    - {name: \"Ghostbuster (GB) Reuters\", size: \"1,000 human + 6,000 LLM texts, 6 LLMs\"}\n    - {name: \"RAID\", size: \"153,217 human + 2,443,073 LLM texts, 6 LLMs\"}\n    - {name: \"RAID (no attacks)\", size: \"12,766 human + 202,593 LLM texts, 6 LLMs\"}\n    - {name: \"M4\", size: \"59,032 human + 57,253 LLM texts, 7 LLMs\"}\n    - {name: \"MAGE\", size: \"152,382 human + 284,224 LLM texts, 131 model labels combined into 4 families\"}\n  ablation_dimensions:\n    - \"Model family used for training vs. testing (cross-model generalization)\"\n    - \"In-domain vs. out-of-domain evaluation\"\n    - \"Text length cutoffs (entropy analysis at increasing character lengths)\"\n    - \"Feature set size in unmasking (top 250 vs. top 500 n-grams)\"\n    - \"Operating point threshold (accuracy vs. low FPR vs. low FNR)\"\n    - \"Genre-controlled vs. mixed-genre datasets\"\n    - \"Dataset used for training (PAN vs. RAID)\"\n  training_recipe:\n    optimizer: \"Not specified for SVM; LoRA fine-tuning for Mistral-7B\"\n    lr: \"Not specified\"\n    hardware: \"3x A100 GPUs for 2x12h (Mistral-7B LoRA, 20M trainable parameters)\"\n  method_family: \"Authorship analytics / computational stylometry applied to LLM detection\"\n\npositioning:\n  core_claim: \"LLM detection is fundamentally an authorship verification (open-set one-class) problem, not an authorship attribution (closed-set binary classification) problem, and conflating the two paradigms explains the contradictory reports of detector success and failure.\"\n  key_results: \"SVM in-domain FNR 0-7%, FPR 0-3%; OpenAI o1 is undetectable by non-o1 detectors; Binoculars FPR near zero but fails completely on o1; GPT-4o is first model with entropy consistent with human text beyond 4,000 chars; word length alone yields remarkable detection accuracy on genre-controlled datasets (Cohen's d up to 4.11)\"\n  limitations:\n    - \"Key assumption that future LLMs will become increasingly human-like in style could be wrong -- LLMs may converge to a distinct 'mean style' centroid\"\n    - \"Only a limited number of datasets and detectors were analyzed; more experiments needed to corroborate practical implications\"\n    - \"Humans exposed to LLM writing may adopt LLM stylistic properties, creating a feedback loop\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Generative AI is everywhere -- then immediately juxtaposes contradictory evidence: detectors regularly 'beat' benchmarks yet OpenAI shut down their own detector after 6 months citing lack of accuracy.\"\n  tension: \"The conflicting reports of success and failure in LLM detection create a puzzle. The paper frames this as a fundamental misunderstanding: researchers build attribution-style detectors but evaluate them under verification assumptions, leading to systematic errors.\"\n  key_insight: \"Revealed in Section 3.3 via a scaling thought experiment: as you add more human authors to distinguish from an LLM, the attribution approach fails because the number of humans classified as LLM asymptotically approaches all of humanity. This is exactly what current research does by compiling ever-larger corpora. The insight bridges two previously disconnected communities (authorship analytics and LLM detection).\"\n  argument_chain: \"Contradiction in detector reports -> bridge to authorship analytics (attribution vs verification) -> theoretical argument that attribution cannot scale (Section 3.3) -> empirical evidence that LLM text properties are converging toward human (Section 4, entropy/MTLD/readability) -> detector evaluation confirming attribution works in-domain but fails cross-model especially for o1 (Section 5) -> discussion of benchmark quality and evaluation metric issues (Section 6) -> conclusion that verification framing is necessary\"\n  contribution_framing: \"Four numbered contributions at end of intro: (1) reconcile authorship analytics with LLM detection, showing it is verification; (2) corpus analysis of how LLM text differs from human text; (3) show SOTA detectors solve attribution well; (4) discuss benchmark quality and evaluation needs for verification.\"\n  intro_structure: \"4 paragraphs: P1 sets scene (LLM text is everywhere, risks, detector interest); P2 presents the contradiction (detectors beat benchmarks vs. serious concerns, OpenAI shutting down detector); P3 frames the explanation (mix-up of attribution vs verification, bridging two communities, explains why attribution fails at scale); P4 lists four contributions with section pointers.\"\n  notable_technique: \"The thought experiment in Section 3.3 is the rhetorical centerpiece -- it takes a simple two-author scenario and iteratively adds authors to show how attribution inherently breaks down. The paper also excels at connecting a 'new' problem (LLM detection) to a well-established field (authorship analytics) that developed independently, making the reader see that the wheel is being reinvented poorly.\"\n\nfigures:\n  figure_count: 21\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Mean character 3-gram entropy over increasing text length with 95% confidence intervals across three datasets (PAN'24, RAID, M4). Shows per-model entropy curves diverging from human baseline after ~2,500-4,000 characters.\"\n    narrative_role: \"Core empirical evidence that LLM text has lower entropy than human text, but newer models (GPT-4o, o1) are closing the gap -- supporting the verification framing.\"\n    design_elements: [\"Multi-panel (a,b,c) by dataset\", \"Confidence interval shading\", \"Color-coded per model family\", \"Human baseline highlighted\", \"X-axis is text length, Y-axis is entropy\"]\n    visual_style: \"Three-panel line plot with shaded confidence intervals. Clean academic style, models labeled directly on curves. Divergence point visible around 2,500 chars.\"\n  result_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"heatmap\"\n      what_compared: \"FNR and FPR of SVM, Binoculars, and Mistral-7B detectors across training model families (rows) vs test model families (columns)\"\n      how_gain_highlighted: \"Diagonal shows best in-domain performance; o1 row/column visually stands out as failing for all non-o1 detectors\"\n      design_note: \"Complex multi-panel figure (4a-4d) combining heatmaps for SVM cross-model, SVM on PAN, Binoculars on PAN, and Mistral on PAN/RAID. Packs maximum information by varying both training and test conditions.\"\n    - figure_id: \"Figure 5 (Appendix A)\"\n      viz_type: \"line_plot\"\n      what_compared: \"ROC vs Precision-Recall curves at different class prevalence ratios (P/N = 0.2 to 5.0)\"\n      how_gain_highlighted: \"Directly shows ROC is invariant to prevalence while precision degrades, supporting the argument that AUROC is misleading\"\n      design_note: \"Side-by-side comparison with color-coded prevalence ratios makes the divergence between ROC and PR curves visually immediate.\"\n    - figure_id: \"Figure 6 (Appendix B)\"\n      viz_type: \"box_plot\"\n      what_compared: \"Entropy distributions at 4,500 characters as a discriminator on PAN dataset, per model\"\n      how_gain_highlighted: \"Box spread shows which models are separable from humans on entropy alone\"\n      design_note: \"Single compact figure showing discriminability limits of a simple feature.\"\n    - figure_id: \"Figures 7-9 (Appendix D)\"\n      viz_type: \"heatmap\"\n      what_compared: \"AUROC of SVM, Binoculars, and fine-tuned Mistral across all datasets\"\n      how_gain_highlighted: \"Color intensity shows where each detector type succeeds/fails\"\n      design_note: \"Supplements Figure 4 with AUROC values; includes bar charts for per-dataset breakdown.\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"Model (Llama2-70b, GPT-3.5, GPT-4o, OpenAI o1)\", \"Feature set size (top 250 vs top 500 n-grams)\", \"Pairing type (Human/Human, LLM/LLM, Human/LLM)\"]\n      design_note: \"8-panel grid (4 models x 2 feature sizes) showing unmasking curves with IQR shading. Reveals that older models are 'inconsistently' discriminable (high in top-250 but low in top-500), while newer models like o1 are more consistent -- key evidence for the verification argument.\"\n    - figure_id: \"Figures 18-19 (Appendix G)\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"All 10 model families on PAN'24\", \"HD dataset models\"]\n      design_note: \"Extended unmasking curves for all models, supplementing Figure 3's selected models.\"\n    - figure_id: \"Figures 20-21 (Appendix G)\"\n      viz_type: \"density_plot\"\n      dimensions_varied: [\"Compression-based cosine (CBC) score distributions across model pairings\"]\n      design_note: \"KDE density plots showing CBC score separation between same-author and cross-author pairs.\"\n  figure_narrative_role: \"Figure 1 (entropy divergence) -> Figure 2 (human entropy varies by genre) -> Figure 3 (unmasking reveals inconsistency in older LLMs vs consistency in newer ones) -> Figure 4 (detector evaluation confirms attribution works in-domain but fails cross-model). Appendix figures (5-21) provide exhaustive supporting evidence for each main-text claim. The flow is: statistical properties of text -> stylometric analysis -> detector performance.\"\n\ntables:\n  table_count: 6\n  main_result_table:\n    table_id: \"N/A -- this paper primarily uses figures (heatmaps/line plots) for main results rather than traditional result tables\"\n    row_axis: \"N/A\"\n    col_axis: \"N/A\"\n    row_organization: \"N/A\"\n    col_organization: \"N/A\"\n    highlight_strategy: \"N/A\"\n    statistical_reporting: \"t-tests with Cohen's d effect sizes reported inline in text; Bonferroni correction for multiple comparisons\"\n    num_baselines: 3\n    design_note: \"Unusual for the field: main results are presented as heatmap figures (Figure 4) rather than tables. This is a deliberate choice that makes cross-model generalization patterns visually immediate. Statistical tests are reported inline rather than in tables.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Tables 1-5 in appendix contain qualitative examples of low-quality/short texts from RAID, MAGE, M4, and BLOOMz datasets. Table 6 provides dataset statistics (text counts, human/LLM splits, number of LLMs per dataset).\"\n    reason: \"Tables are used for qualitative evidence (bad data examples) and dataset metadata rather than quantitative results. All quantitative comparisons use figures. This split reflects the paper's emphasis on data quality critique -- the appendix tables serve as 'exhibit evidence' for the argument that benchmarks are flawed.\"\n```\n\n---\n\n**5. synthetic_eggs2026.yaml**\n\n```yaml\npaper_key: \"synthetic_eggs2026\"\ntitle: \"Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\"\nvenue: \"ACL 2026 Findings\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"human data fine-tuning\", \"single-source synthetic fine-tuning\", \"multi-source synthetic fine-tuning\"]\n  metrics:\n    - {name: \"distribution collapse measures\", direction: \"lower_better\"}\n    - {name: \"adversarial robustness\", direction: \"higher_better\"}\n    - {name: \"self-preference bias\", direction: \"lower_better\"}\n    - {name: \"output quality\", direction: \"higher_better\"}\n    - {name: \"text diversity\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"synthetic data from multiple LLM sources\", size: \"N/A\"}\n  ablation_dimensions: [\"number of source models\", \"human vs synthetic ratio\", \"source model diversity\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"synthetic data diversity analysis for fine-tuning\"\n\npositioning:\n  core_claim: \"Fine-tuning on diverse multi-source synthetic data mitigates distribution collapse while preserving output distribution breadth, but adversarial robustness decreases\"\n  key_results: \"Multi-source synthetic > single-source for distribution collapse; human data best for reducing self-preference bias; synthetic data yields higher quality but lower robustness\"\n  limitations: [\"limited to fine-tuning (not pre-training)\", \"specific LLM families\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**6. li2024_mage.yaml**\n\n```yaml\npaper_key: \"li2024_mage\"\ntitle: \"MAGE: Machine-generated Text Detection in the Wild\"\nvenue: \"ACL 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Longformer (PLM-based classifier)\"\n    - \"GLTR (GPT-2-XL + logistic regression)\"\n    - \"FastText (word bi-gram features)\"\n    - \"DetectGPT (zero-shot, T5-3B mask infill + GPT-J-6B scoring)\"\n    - \"Human annotators\"\n    - \"ChatGPT querying\"\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"AvgRec (average of HumanRec and MachineRec)\", direction: \"higher_better\"}\n    - {name: \"HumanRec (human text recall)\", direction: \"higher_better\"}\n    - {name: \"MachineRec (machine text recall)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"MAGE testbed (custom)\", size: \"95,596 human + 236,554 machine-generated texts from 7 domains x 27 LLMs\"}\n    - {name: \"Reddit ChangeMyView\", size: \"804 opinion statements\"}\n    - {name: \"Yelp\", size: \"1,000 reviews\"}\n    - {name: \"XSum\", size: \"1,000 news articles\"}\n    - {name: \"TLDR\", size: \"777 news summaries\"}\n    - {name: \"ELI5\", size: \"1,000 QA pairs\"}\n    - {name: \"Reddit WritingPrompts\", size: \"1,000 stories\"}\n    - {name: \"ROCStories\", size: \"1,000 stories\"}\n    - {name: \"HellaSwag\", size: \"1,000 commonsense reasoning\"}\n    - {name: \"SQuAD (Wikipedia)\", size: \"1,000 paragraphs\"}\n    - {name: \"SciXGen\", size: \"1,000 scientific abstracts\"}\n    - {name: \"CNN/DailyMail (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"DialogSum (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"PubMedQA (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"IMDb (frontier test)\", size: \"used in Testbed 7\"}\n  ablation_dimensions:\n    - \"In-distribution vs out-of-distribution (8 testbed scenarios)\"\n    - \"Fixed-domain vs arbitrary-domain\"\n    - \"Model-specific vs arbitrary-model\"\n    - \"Unseen models (cross-validation over 7 model groups)\"\n    - \"Unseen domains (cross-validation over 10 domains)\"\n    - \"Decision boundary adjustment (0.1% in-domain data)\"\n    - \"Paraphrasing attack robustness (gpt-3.5-turbo)\"\n    - \"Prompt type (continuation vs topical vs specified)\"\n    - \"PLM backbone comparison\"\n    - \"Data balance effects\"\n    - \"Randomness analysis\"\n  training_recipe:\n    optimizer: \"Adam\"\n    lr: \"0.005\"\n    dropout: \"0.1\"\n    epochs: \"5\"\n    hardware: \"8x V100 GPUs\"\n    validation_metric: \"classification accuracy\"\n    gltr_lm: \"GPT-2-XL\"\n    gltr_classifier: \"logistic regression (scikit-learn, grid search)\"\n    fasttext_epochs: \"100\"\n    detectgpt_mask_model: \"T5-3B\"\n    detectgpt_scoring_model: \"GPT-J-6B\"\n    detectgpt_mask_rate: \"15%\"\n    detectgpt_perturbations: \"100\"\n  method_family: \"PLM-based binary classification (Longformer) + statistical/zero-shot baselines for machine-generated text detection\"\n\npositioning:\n  core_claim: \"First comprehensive 'in-the-wild' testbed for machine-generated text detection spanning 7 domains and 27 LLMs, revealing that perplexity is a double-edged sword — it enables clustering but causes systematic false positives on low-perplexity human text.\"\n  key_results: \"Longformer achieves AUROC 0.99 in-distribution but drops to 0.95 on unseen models and 0.93 on unseen domains; with 0.1% boundary adjustment data, achieves 86.54% AvgRec on unseen domains + unseen model (GPT-4); paraphrasing attacks degrade AUROC to 0.75.\"\n  limitations:\n    - \"Limited model coverage — new LLMs (Alpaca, Vicuna, etc.) continuously emerge and the testbed cannot keep up\"\n    - \"Benchmark data bias — source texts may overlap with LLM pretraining data, so detection performance may not transfer to truly novel online text\"\n    - \"Vulnerability to paraphrasing attacks (AvgRec drops to 62.92% even with boundary adjustment)\"\n    - \"Perplexity bias causes systematic misclassification of low-perplexity human texts as machine-generated\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"LLMs have achieved human-level text generation, creating urgent need for detection — but existing detection research only evaluates on specific domains or specific models, leaving open how detectors perform 'in the wild'.\"\n  tension: \"Prior work assumes controlled settings (known domain, known generator). In reality, detectors face texts from unknown LLMs across diverse domains. The paper asks: can detection still work when we don't know the source?\"\n  key_insight: \"Perplexity is a double-edged sword — it is the fundamental feature separating human and machine text (machine text has lower perplexity), but detectors over-rely on it, systematically misclassifying low-perplexity human text. Diverse domains and models cause human-machine linguistic differences to converge, making detection harder.\"\n  argument_chain: \"problem (detection in controlled settings ≠ detection in the wild) → testbed construction (7 domains × 27 LLMs × 3 prompt types) → 8 progressive evaluation scenarios (in-distribution → OOD) → empirical finding (performance degrades with diversity, especially OOD) → analysis (linguistic convergence + perplexity bias) → mitigation (boundary adjustment with 0.1% data) → feasibility demonstration (86.54% on GPT-4 unseen domain)\"\n  contribution_framing: \"Three contributions: (1) comprehensive testbed with texts from diverse human writings and LLMs, (2) empirical analysis revealing diminishing linguistic differences in open-domain settings, (3) discovery that perplexity serves as fundamental but biased clustering feature. Framed as 'first' comprehensive wild-scenario evaluation.\"\n  intro_structure: \"~5 paragraphs: (1) LLMs generate human-level text → detection needed, (2) existing work limited to specific domains/models, (3) two research questions about wild detection, (4) testbed construction description, (5) key findings and contributions.\"\n  notable_technique: \"Progressive difficulty design — 8 testbeds arranged from easiest (white-box, single domain, single model) to hardest (unseen domain + unseen model + paraphrasing attack), creating a compelling narrative arc that systematically reveals when and why detection fails.\"\n\nfigures:\n  figure_count: 15\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Left side shows diverse input domains (News Title, Story Title, Question, Argument, Scientific Topic) as colored cards with arrows pointing to both Humans (stick figure at desk) and multiple LLMs (GPT-3.5, FLAN-T5, LLaMA, OPT, GLM, ...) listed vertically. The many-to-many arrows from domains to generators show the combinatorial explosion. Right side shows a 'Text' box passing through a magnifying glass 'Detector' with a question mark, leading to two possible outputs: 'Human' (messy scribble icon) and 'Machine' (clean stick figure). The layout flows left-to-right: sources → generators → mixed text → detection challenge.\"\n    narrative_role: \"Establishes the core challenge — detection must handle the combinatorial space of domains × generators, not just one domain or one model.\"\n    design_elements: [\"colored domain cards (purple/orange/green)\", \"many-to-many arrows showing combinatorial complexity\", \"magnifying glass as detector metaphor\", \"question mark conveying uncertainty\", \"stick figure icons for human vs machine\"]\n    visual_style: \"Clean line-art style with selective color on domain cards (purple, orange, green pastels). Horizontal left-to-right flow. Minimal decorative elements. Black-and-white for the detection side. Simple but effective at conveying the many-to-many challenge.\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"grouped_bar_or_line\"\n      what_compared: \"OOD detection performance on unseen models, broken down by model family and prompt type\"\n      how_gain_highlighted: \"Shows which model families are hardest to detect (OpenAI, FLAN-T5) and which prompt types are most challenging (specified prompts)\"\n      design_note: \"Separates analysis by two dimensions (model family × prompt type) to give nuanced OOD understanding rather than single aggregate number\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"bar_chart_or_line\"\n      what_compared: \"Detection performance (AvgRec) on unseen domains, identifying ROC, XSum, TLDR as hardest\"\n      how_gain_highlighted: \"Links difficulty to domain perplexity characteristics\"\n      design_note: \"Per-domain breakdown reveals systematic pattern (low-perplexity domains harder) rather than just reporting aggregate OOD performance\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"precision_recall_curve + bar_chart\"\n      what_compared: \"(a) PR curves before/after boundary adjustment, (b) performance improvement with 0.1% in-domain data\"\n      how_gain_highlighted: \"Direct before/after comparison shows dramatic improvement from minimal adaptation\"\n      design_note: \"Two-panel figure pairs theoretical (PR curve) with practical (data requirement) perspectives\"\n  ablation_figures:\n    - figure_id: \"Figure 5\"\n      viz_type: \"heatmap\"\n      dimensions_varied: [\"domain diversity\", \"model diversity\"]\n      design_note: \"Jensen-Shannon distance heatmap showing linguistic convergence as diversity increases — visual proof that the detection problem gets fundamentally harder with diversity\"\n    - figure_id: \"Figure 6\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"named entity types (ORDINAL, DATE, etc.)\"]\n      design_note: \"Shows entity distribution differences in fixed-domain setting as detection shortcuts that disappear with diversity\"\n    - figure_id: \"Figures 7-9\"\n      viz_type: \"histogram + scatter\"\n      dimensions_varied: [\"perplexity distributions\", \"prediction correctness\", \"paraphrasing effects\"]\n      design_note: \"Three-figure sequence builds the 'perplexity as double-edged sword' argument: (7) machine < human perplexity, (8) misclassified human texts have low perplexity, (9) paraphrasing shifts distributions\"\n  figure_narrative_role: \"Figure 1 (problem illustration) → Figures 2-3 (OOD performance breakdown by model/domain) → Figure 4 (boundary adjustment solution) → Figures 5-6 (linguistic convergence analysis) → Figures 7-9 (perplexity analysis arc) → Figures 10-15 (appendix: prompts, data distributions, linguistic stats). The main paper figures follow a 'problem → results → analysis → mitigation' narrative arc.\"\n\ntables:\n  table_count: 12\n  main_result_table:\n    table_id: \"Table 3\"\n    row_axis: \"methods (Longformer, FastText, GLTR, DetectGPT)\"\n    col_axis: \"testbed scenarios (Testbed 2-6) × metrics (AUROC, AvgRec, HumanRec, MachineRec)\"\n    row_organization: \"flat\"\n    col_organization: \"grouped_by_testbed\"\n    highlight_strategy: \"best results in bold across methods per testbed\"\n    statistical_reporting: \"single run numbers (no std reported for main results)\"\n    num_baselines: 4\n    design_note: \"Comprehensive table spanning both in-distribution (Testbeds 2-4) and out-of-distribution (Testbeds 5-6) in one view, enabling direct comparison of how each method degrades from ID to OOD. Progressive difficulty across columns tells the degradation story.\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"white-box detection (Testbed 1) — easiest setting as reference point\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Separated from main table to establish performance ceiling before showing degradation\"\n    - table_id: \"Table 4\"\n      what_varied: [\"decision boundary adjustment effect on Testbeds 5-6\"]\n      variation_style: \"full_numbers (before vs after adjustment)\"\n      design_note: \"Shows boundary adjustment dramatically improves domain-shift performance (AvgRec 68.40→81.78 for unseen domains)\"\n    - table_id: \"Table 5\"\n      what_varied: [\"challenging frontier tests (Testbed 7: unseen domain+model with GPT-4, Testbed 8: paraphrasing attack)\"]\n      variation_style: \"full_numbers with before/after boundary adjustment\"\n      design_note: \"Most challenging scenarios isolated in separate table — clean before/after comparison for the proposed mitigation\"\n    - table_id: \"Table 1\"\n      what_varied: [\"naive baselines (ChatGPT querying, human annotators)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Establishes that even humans (~54.5% AvgRec) and ChatGPT (~54.5% AvgRec) struggle at wild detection, motivating the need for dedicated methods\"\n    - table_id: \"Tables 8-10\"\n      what_varied: [\"randomness analysis\", \"PLM backbone comparison\", \"data balance effects\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Robustness checks in appendix ensure main findings are not artifacts of specific choices\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 6 (dataset statistics per domain), Table 7 (naive baseline test set composition), Tables 8-10 (robustness: randomness/backbone/balance), Table 11 (all methods on challenging test sets), Table 12 (length statistics)\"\n    reason: \"Main paper focuses on the progressive testbed story (Tables 1-5). Appendix holds dataset details and robustness checks that support but don't drive the narrative.\"\n```\n\n---\n\n**7. mohamed2025_broken_telephone.yaml**\n\n```yaml\npaper_key: \"mohamed2025_broken_telephone\"\ntitle: \"LLM as a Broken Telephone: Iterative Generation Distorts Information\"\nvenue: \"ACL 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"single-pass generation\", \"various prompting strategies\"]\n  metrics:\n    - {name: \"information distortion rate\", direction: \"lower_better\"}\n    - {name: \"semantic similarity to original\", direction: \"higher_better\"}\n    - {name: \"factual accuracy degradation\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"translation chain experiments\", size: \"N/A\"}\n  ablation_dimensions: [\"number of iterative generations\", \"language choice\", \"chain complexity\", \"prompting strategy\"]\n  training_recipe: {optimizer: \"N/A (inference only)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"empirical analysis of iterative LLM generation degradation\"\n\npositioning:\n  core_claim: \"LLMs systematically distort information when outputs are repeatedly processed, with distortion accumulating over iterations analogous to the broken telephone effect\"\n  key_results: \"Degradation is inevitable but mitigable through strategic prompting; language and chain complexity influence distortion rate\"\n  limitations: [\"primarily translation-based experiments\", \"limited model coverage\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**8. dohmatob2024_tale_of_tails.yaml**\n\n```yaml\npaper_key: \"dohmatob2024_tale_of_tails\"\ntitle: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\nvenue: \"ICML 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Original (human/natural) data training\"\n    - \"Pure synthetic data training\"\n    - \"Mixed real+synthetic data training\"\n    - \"Hutter LLM (deterministic lookup table)\"\n    - \"Hutter++ (probabilistic bigram)\"\n    - \"Capacity-limited associative memory\"\n  metrics:\n    - {name: \"test error (scaling law exponent)\", direction: \"lower_better\"}\n    - {name: \"perplexity\", direction: \"lower_better\"}\n    - {name: \"number of skills learned (GCD answers)\", direction: \"higher_better\"}\n    - {name: \"total variation distance\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Wikitext-103\", size: \"~2M samples for fine-tuning\"}\n    - {name: \"GCD arithmetic task (Zipfian)\", size: \"300K-300M samples\"}\n    - {name: \"Synthetic bigram distributions\", size: \"variable\"}\n  ablation_dimensions:\n    - \"tail cutoff rank k (top-p/top-k truncation)\"\n    - \"tail exponent narrowing beta_prime vs beta (temperature scaling)\"\n    - \"number of recursive generations n\"\n    - \"mixing proportion pi of real vs synthetic data\"\n    - \"model capacity / embedding dimension d\"\n    - \"Zipf exponent beta\"\n    - \"training set size T\"\n  training_recipe:\n    optimizer: \"not explicitly specified in main text\"\n    lr: \"not explicitly specified in main text\"\n    hardware: \"not explicitly specified\"\n    details: \"GCD transformer trained on up to 300M samples; Llama2-7B fine-tuned on Wikitext-103 ~2M samples; synthetic data generated with various top-p and temperature settings\"\n  method_family: \"theoretical analysis of model collapse via scaling laws and tail distributions\"\n\npositioning:\n  core_claim: \"Model collapse is fundamentally a change of scaling laws caused by synthetic data losing the heavy-tailed structure of natural distributions, leading to quantifiable and predictable degradation patterns including plateau effects, skill loss, and shifted scaling exponents.\"\n  key_results: \"Double scaling law E_test ~ T^(-(beta-1)/beta) + k^(-(beta-1)) predicts performance plateau on synthetic data; multi-generation collapse shows additive degradation E_test ~ T^(-c) + n*T0^(-c); grokking phenomenon when mixing pi-fraction real data creates plateau of length ~k^beta/pi before recovery; triplet scaling law E_test ~ T^(-(1-1/beta)) + d^(-c_q) + k^(-(beta-1)) for capacity-limited models\"\n  limitations:\n    - \"Theory assumes simplified models (Zipfian distributions, deterministic labels for some results)\"\n    - \"Grokking theorem strictly holds only for deterministic ground-truth labels; probabilistic settings show attenuated S-shaped curves\"\n    - \"Real LLMs involve complex conditional distributions not fully captured by the theoretical framework\"\n    - \"Bigram and Hutter models are simplified abstractions of actual language model behavior\"\n    - \"No experiments on larger-scale models beyond Llama2-7B\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the observation that AI model scaling laws have been a key predictive tool, but the ecosystem of online data is co-evolving to contain increasing amounts of synthetic data - asking whether future models will still improve or be 'doomed to degenerate up to total collapse'. Uses the striking statistic that ChatGPT contributes 0.1% of total words generated daily by the global population.\"\n  tension: \"Existing scaling law theory assumes training on natural (heavy-tailed) data distributions, but the inevitable contamination of training corpora with synthetic data fundamentally breaks these assumptions. Prior work on model collapse identified the phenomenon but lacked a theoretical framework connecting it to scaling laws and emergent abilities.\"\n  key_insight: \"The key insight is that heavy-tailed (Zipfian) distributions are what enable power-law scaling, and AI generation mechanisms (top-p sampling, temperature scaling, finite sampling) systematically destroy these tails through three mechanisms: tail cutting, tail narrowing, and finite sampling bias. This directly links distributional properties to scaling law behavior.\"\n  argument_chain: \"problem (synthetic data contamination is inevitable) -> observation (scaling laws depend on heavy-tailed distributions) -> mechanism (AI generation cuts/narrows tails via top-p, temperature, finite sampling) -> theory (double/triplet scaling laws predict plateau and degradation) -> multi-generation analysis (collapse compounds across iterations) -> mitigation (data mixing enables grokking recovery) -> experiments (GCD transformer + Llama2-7B validate predictions)\"\n  contribution_framing: \"Four numbered contributions introduced with 'Our main findings are as follows': (1) Double Scaling Law, (2) Triplet Scaling Law for Memory-Limited Models, (3) Model Collapse over Multiple Generations, (4) Mitigation Strategies. Explicitly claims to be 'the first to theoretically and empirically analyze model collapse in the context of scaling laws and emergent abilities'.\"\n  intro_structure: \"5 paragraphs: P1=hook (scaling laws + synthetic data problem), P2=background (neural scaling laws and heavy tails), P3=problem statement (model collapse concern), P4=key insight (tail mechanisms), P5=contribution list (4 numbered findings)\"\n  notable_technique: \"The 'tale of tails' metaphor is the central narrative device - it reframes the abstract concept of model collapse into a concrete, visual story about distribution tails. The three tail destruction mechanisms (cutting, narrowing, finite sampling) provide a clean taxonomy that makes complex theory intuitive. The paper also effectively uses the GCD arithmetic task as a controlled 'microscope' for studying skill emergence and loss, before scaling up to Llama2.\"\n\nfigures:\n  figure_count: 5  # main text; ~35 total including appendices\n  figure1:\n    type: \"motivation\"\n    description: \"Illustrates the three mechanisms by which AI generation destroys distribution tails: top-p nucleus sampling (tail cutting), temperature scaling with tau>1 (tail narrowing), and finite sample bias. Shows how these mechanisms affect a Zipfian frequency distribution and connects to skill loss using GCD calculation (answers 2 and 3) as concrete examples.\"\n    narrative_role: \"Establishes the paper's core conceptual framework - visually demonstrates WHY model collapse happens by showing the mechanistic link between generation procedures and tail destruction. This is the key figure that makes the abstract theory tangible.\"\n    design_elements: [\"distribution curves with shaded truncation regions\", \"before/after comparison of tails\", \"concrete skill examples (GCD answers)\", \"three-panel layout for three mechanisms\"]\n    visual_style: \"Clean schematic diagrams with distribution curves; uses color to distinguish original vs truncated/narrowed distributions; combines mathematical distributions with concrete task examples\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Three panels illustrating main theoretical results: (Left) Double scaling law with Zipf exponent beta=3/2 showing plateau effect; (Middle) Model collapse across 5 generations showing progressive degradation; (Right) Grokking behavior showing plateau length and asymptotic recovery predictions\"\n      how_gain_highlighted: \"Theoretical predictions shown as dashed lines overlaid on empirical curves; clear separation between original data scaling (power law) and synthetic data scaling (plateau)\"\n      design_note: \"Three-panel layout maps directly to three main theorems; log-log scale makes power-law relationships linear; uses generation number as a visual variable to show progressive collapse\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Three experimental validation panels: (Left) Llama2-7B perplexity scaling on Wikitext-103 across generations; (Middle) GCD transformer scaling on original vs synthetic data; (Right) Skills (GCD answers) learned on clean vs AI-generated data\"\n      how_gain_highlighted: \"Direct visual comparison of original vs synthetic data curves; skill emergence on clean data vs skill loss on synthetic data is strikingly clear\"\n      design_note: \"Mirrors the layout of Figure 3 (theory) to enable direct theory-vs-experiment comparison; this structural parallelism strengthens the validation narrative\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"line_plot\"\n      what_compared: \"Effect of mixing real data (T_real) with AI data (T_AI) - shows performance improvement up to saturation point with k=1000 and beta=3/2\"\n      how_gain_highlighted: \"Shows the grokking transition clearly - performance plateaus then recovers as real data fraction increases\"\n      design_note: \"Single focused plot isolates the mixing mitigation result; parameters annotated directly on figure\"\n  ablation_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"combined_distribution_and_perplexity\"\n      dimensions_varied: [\"data source (original vs AI-generated)\", \"generation parameters (top-p, temperature)\"]\n      design_note: \"Two-part figure combines perplexity diagram (top) with distribution comparison (bottom); effectively demonstrates that the theoretical tail-cutting/narrowing mechanisms manifest in real LLM outputs\"\n  figure_narrative_role: \"Figure 1 (motivation: why tails matter) -> Figure 2 (empirical evidence: tails ARE destroyed in practice) -> Figure 3 (theory: predicted consequences) -> Figure 4 (validation: experiments match theory) -> Figure 5 (mitigation: data mixing helps). Clean motivation-theory-validation-solution arc.\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    note: \"This paper has NO tables. All results are presented through mathematical theorems and figures with scaling curves. This is consistent with theoretical ML papers where the primary contributions are equations/bounds rather than benchmark comparisons.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: false\n    content: \"No tables in appendix either; appendices contain proofs (Appendices C-F), additional figures (Appendix B), and experimental details (Appendices G-H)\"\n    reason: \"The paper is primarily theoretical - results are best expressed as scaling law equations and their visual verification, not tabular comparisons. The continuous nature of scaling curves makes line plots the natural presentation format.\"\n```\n\n---\n\n**9. finlayson2024_closing.yaml**\n\n```yaml\npaper_key: \"finlayson2024_closing\"\ntitle: \"Closing the Curious Case of Neural Text Degeneration\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"nucleus sampling (top-p)\", \"top-k sampling\", \"greedy decoding\", \"threshold-based truncation methods\"]\n  metrics:\n    - {name: \"text quality (human eval)\", direction: \"higher_better\"}\n    - {name: \"text quality (automatic)\", direction: \"higher_better\"}\n    - {name: \"degeneration rate\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"open-ended text generation benchmarks\", size: \"N/A\"}\n  ablation_dimensions: [\"truncation threshold\", \"entropy regime\", \"model size\"]\n  training_recipe: {optimizer: \"N/A (decoding strategy)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"truncation sampling / decoding strategy analysis\"\n\npositioning:\n  core_claim: \"The softmax bottleneck causes models to assign nonzero probability to impossible tokens; truncation sampling works by removing these, and a principled approach without arbitrary thresholds is possible\"\n  key_results: \"Theoretical proof that threshold-free truncation using softmax bottleneck properties guarantees valid token sampling\"\n  limitations: [\"focused on open-ended generation\", \"theoretical assumptions about softmax bottleneck\"]\n  relation_to_us: \"orthogonal\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**10. yi2026_escaping_collapse.yaml**\n\n```yaml\npaper_key: \"yi2026_escaping_collapse\"\ntitle: \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\"\nvenue: \"ICLR 2026 (Poster)\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Unfiltered synthetic retraining (no verifier)\"\n    - \"Real-data-only OLS estimator\"\n    - \"VAE trained on full 60K MNIST (upper bound)\"\n  metrics:\n    - {name: \"MSE (parameter estimation error)\", direction: \"lower_better\"}\n    - {name: \"FID (Frechet Inception Distance)\", direction: \"lower_better\"}\n    - {name: \"ELBO (Evidence Lower Bound)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Simulated linear regression\", size: \"dimension p=8, varying sample sizes (500->2000, 1000->4000, 2000->8000)\"}\n    - {name: \"MNIST\", size: \"500 real images for init, 60K for discriminator training\"}\n  ablation_dimensions:\n    - \"Verifier bias (Delta: 0.0-0.7)\"\n    - \"Verifier selectivity/radius (r: 0.05-0.5 for linear; top-10% for VAE)\"\n    - \"Training sample size schedule (real->synthetic ratio)\"\n    - \"Verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images)\"\n    - \"Filtered vs unfiltered synthetic data\"\n  training_recipe:\n    optimizer: \"OLS (closed-form) for linear regression; standard SGD for CVAE\"\n    lr: \"N/A for OLS; not specified for VAE\"\n    hardware: \"Not specified\"\n    iterations: \"60 rounds for linear regression; 40 rounds for VAE\"\n  method_family: \"Verifier-guided synthetic data filtering for iterative model retraining\"\n\npositioning:\n  core_claim: \"External verifier-based filtering of synthetic data prevents model collapse in the short term via bias-variance tradeoff, but long-term performance converges to the verifier's knowledge center rather than ground truth -- unless the verifier is perfectly unbiased.\"\n  key_results: \"Linear regression: filtered retraining keeps MSE near 0.05 across 60 iterations while unfiltered diverges to 0.3-0.8. VAE/MNIST: FID drops from ~110 to ~40 with 60K-trained verifier over 40 iterations; with only 500-image verifier, FID plateaus at ~130.\"\n  limitations:\n    - \"Theoretical analysis restricted to linear regression; generalization to neural networks remains open\"\n    - \"VAE verifier (discriminator) is relatively simple and may reject harder-to-generate modes\"\n    - \"Synthetic retraining initialized with only 500 real images limits diversity recovery\"\n    - \"Verifier quality directly bounds long-term performance ceiling -- biased verifier leads to biased convergence\"\n    - \"No experiments on large language models or more complex generative tasks\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Synthetic data is increasingly used to train frontier generative models, but iterative retraining on self-generated data causes model collapse -- a well-documented performance degradation phenomenon.\"\n  tension: \"Prior work establishes collapse as seemingly inevitable under recursive self-training, but real practitioners already use external verification (human feedback, reward models). The question is: can verification provably escape collapse, and if so, what are the limits?\"\n  key_insight: \"Verification creates a bias-variance tradeoff: filtering reduces variance (by discarding low-quality samples) but introduces bias (toward the verifier's knowledge center). Short-term gains are real but long-term convergence is to the verifier's center, not ground truth. Presented through Theorem 3.1 (one-round decomposition) and Theorem 4.1 (long-term contraction).\"\n  argument_chain: \"model collapse problem -> prior work shows unfiltered retraining diverges -> introduce verifier-based filtering framework (Generate-Verify-Retrain) -> theoretical analysis: one-round improvement via bias-variance decomposition (Theorem 3.1) -> long-term convergence to verifier center (Theorem 4.1) -> empirical validation on linear regression + VAE/MNIST -> conclusion: verification helps but is fundamentally bounded by verifier quality\"\n  contribution_framing: \"Three research questions framed as Q1 (does verification help short-term?), Q2 (do gains sustain long-term?), Q3 (empirical validation). Each answered with a theorem or experiment. Contribution count: 3 clearly delineated.\"\n  intro_structure: \"4 paragraphs: (1) motivation on synthetic data and model collapse concern, (2) research questions about verifier-based filtering, (3) prior literature context and gaps, (4) bullet-point contributions with theorem references\"\n  notable_technique: \"Framing the two results as a deliberate tension -- short-term improvement (good news) vs long-term convergence to verifier center (cautionary news) -- creates a 'promise and peril' narrative arc that is more nuanced than a pure positive-result paper.\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"teaser_result\"\n    description: \"Three-panel comparison showing VAE-generated MNIST digits: (left) original data, (center-top) with verified synthetic data after 40 rounds showing maintained quality, (center-bottom) without verification showing severe collapse/degradation. (right) upper bound from training on all 60K real images.\"\n    narrative_role: \"Immediately demonstrates the paper's core claim visually -- verification prevents collapse while unfiltered retraining produces unrecognizable outputs. Placed before any theory to motivate the reader.\"\n    design_elements: [\"Before/after comparison\", \"With/without verification contrast\", \"Real sample grids\", \"Upper bound reference\", \"Arrow annotations connecting panels\"]\n    visual_style: \"Black background with white MNIST digit grids arranged horizontally. Arrows with text labels ('With Data Verification' / 'Without Data Verification') connect the initial model to the two outcomes. Clean, high-contrast layout. Roughly 4-panel horizontal arrangement.\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"heatmap + heatmap\"\n      what_compared: \"One-round improvement landscape as function of verifier bias (Delta) and selectivity radius (r). Left (3a): theory-predicted loss landscape. Right (3b): empirical simulation.\"\n      how_gain_highlighted: \"Green regions indicate improvement (log ratio > 0), red regions indicate degradation. Theory-empirical match validates the theoretical framework.\"\n      design_note: \"Diverging green-red colormap centered at 0 makes improvement/degradation regions immediately readable. Side-by-side theory vs empirical layout validates theoretical predictions visually. Axes are interpretable parameters (bias, radius).\"\n    - figure_id: \"Figure 4a\"\n      viz_type: \"line_plot\"\n      what_compared: \"Convergence of parameter estimate to verifier center (theta_c) over 60 iterations for different verifier radii (r=0.1, 0.5, 1, 1.5) with biased verifier\"\n      how_gain_highlighted: \"All curves converge to near-zero distance from theta_c, confirming Theorem 4.1. Smaller radius = faster convergence.\"\n      design_note: \"Clean line plot with distinct colors for each radius value. Y-axis is distance to verifier center, clearly showing contraction. Legend is simple and readable.\"\n    - figure_id: \"Figure 4b\"\n      viz_type: \"line_plot\"\n      what_compared: \"Filtered (solid) vs unfiltered (dashed) retraining across different sample size schedules (500->2000, 1000->4000, 2000->8000) over 60 iterations with unbiased verifier\"\n      how_gain_highlighted: \"Solid lines (filtered) stay flat near 0.05 while dashed lines (unfiltered) diverge upward to 0.3-0.8. Dramatic visual separation between the two groups.\"\n      design_note: \"Solid vs dashed line encoding for filtered/unfiltered is effective. Three colors for three sample size conditions. The divergence of dashed lines visually dramatizes model collapse.\"\n    - figure_id: \"Figure 5a\"\n      viz_type: \"line_plot\"\n      what_compared: \"VAE FID scores over 40 iterations comparing different VAE training sample sizes and filtered vs unfiltered conditions\"\n      how_gain_highlighted: \"Filtered curves decrease steadily; unfiltered curves increase (collapse). Separation grows over iterations.\"\n      design_note: \"Multiple colored lines with solid/dashed encoding. FID on y-axis with clear downward = better convention.\"\n    - figure_id: \"Figure 5b\"\n      viz_type: \"line_plot\"\n      what_compared: \"Effect of verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images) on FID over 40 iterations\"\n      how_gain_highlighted: \"Clear monotonic relationship: more verifier training data = lower FID. 60K verifier achieves FID ~40; 500-image verifier plateaus at ~130.\"\n      design_note: \"Seven colored lines ordered by verifier quality create a clean gradient pattern. Demonstrates the paper's key insight that verification quality bounds final performance. Well-chosen range of verifier sizes.\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"heatmap\"\n      dimensions_varied: [\"Verifier bias (Delta)\", \"Verifier selectivity radius (r)\"]\n      design_note: \"Effectively an ablation over the two key verifier hyperparameters. Heatmap format makes the full landscape visible at once rather than requiring multiple line plots.\"\n    - figure_id: \"Figure 5b\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"Verifier training dataset size (quality proxy)\"]\n      design_note: \"Ablation over verifier quality showing monotonic improvement. Seven conditions provide fine granularity.\"\n  figure_narrative_role: \"Figure 1 (teaser: visual proof of concept) -> Figure 2 (pipeline: method overview) -> Figure 3 (theory validation: one-round landscape) -> Figure 4 (long-term dynamics: convergence behavior) -> Figure 5 (real-world validation: VAE experiments). Progression from motivation to theory to practice.\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    table_id: \"N/A\"\n    design_note: \"Paper has no tables in main text. All results presented through figures (heatmaps and line plots). This is unusual but appropriate for a theory-focused paper where the key results are continuous landscapes and convergence dynamics rather than discrete benchmark comparisons.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Appendix A: 1D Gaussian analysis toolkit. Appendix B: Full proofs of Theorems 3.1 and 4.1. Appendix C: VAE experiment details including data preprocessing, discriminator architecture specifications, synthetic generation procedures, and supplementary ELBO results.\"\n    reason: \"All heavy mathematical proofs and implementation details moved to appendix to keep main paper focused on the two theorems and their experimental validation. Consistent with theory-paper conventions.\"\n```\n\n---\n\n**11. binoculars2024.yaml**\n\n```yaml\npaper_key: \"binoculars2024\"\ntitle: \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\"\nvenue: \"ICML 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"DetectGPT\", \"Fast-DetectGPT\", \"likelihood thresholding\", \"supervised classifiers\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"TPR@1%FPR\", direction: \"higher_better\"}\n    - {name: \"TPR@0.01%FPR\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"multi-domain text corpus (news, wiki, creative)\", size: \"N/A\"}\n    - {name: \"ChatGPT-generated samples\", size: \"N/A\"}\n  ablation_dimensions: [\"LLM pair choice\", \"document type\", \"source model\"]\n  training_recipe: {optimizer: \"N/A (zero-shot)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"zero-shot detection via contrastive LLM scoring\"\n\npositioning:\n  core_claim: \"A simple score contrasting two closely related LLMs achieves SOTA zero-shot detection without any training data, detecting >90% of generated text at 0.01% FPR\"\n  key_results: \">90% detection of ChatGPT at 0.01% FPR; generalizes across LLMs without model-specific tuning\"\n  limitations: [\"requires two LLMs at inference\", \"performance depends on LLM pair choice\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**12. fast_detectgpt2024.yaml**\n\n```yaml\npaper_key: \"fast_detectgpt2024\"\ntitle: \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"DetectGPT\", \"likelihood ratio\", \"rank-based methods\", \"supervised detectors\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"detection speed\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"XSum\", size: \"N/A\"}\n    - {name: \"SQuAD\", size: \"N/A\"}\n    - {name: \"WritingPrompts\", size: \"N/A\"}\n  ablation_dimensions: [\"source model\", \"scoring model\", \"perturbation vs sampling\"]\n  training_recipe: {optimizer: \"N/A (zero-shot)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"zero-shot detection via conditional probability curvature\"\n\npositioning:\n  core_claim: \"Replacing DetectGPT's perturbation step with conditional probability sampling achieves 340x speedup with ~75% relative improvement in both white-box and black-box settings\"\n  key_results: \"340x faster than DetectGPT; 75% relative improvement; 80% ChatGPT detection at 1% FPR\"\n  limitations: [\"still requires model access for scoring\", \"performance varies by domain\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**13. diveye2026.yaml**\n\n```yaml\npaper_key: \"diveye2026\"\ntitle: \"DivEye: Diversity Boosts AI-Generated Text Detection\"\nvenue: \"TMLR 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"DetectGPT\", \"Fast-DetectGPT\", \"Binoculars\", \"supervised fine-tuned classifiers\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"detection accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"multi-domain benchmarks\", size: \"N/A\"}\n  ablation_dimensions: [\"statistical features\", \"auxiliary signal integration\", \"paraphrasing robustness\", \"cross-domain transfer\"]\n  training_recipe: {optimizer: \"N/A (zero-shot statistical)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"statistical feature-based detection using surprisal diversity\"\n\npositioning:\n  core_claim: \"Human text exhibits richer variability in lexical and structural unpredictability (surprisal diversity) than LLM outputs, and this signal is interpretable, robust, and complements existing detectors\"\n  key_results: \"Outperforms zero-shot detectors by up to 33.2%; improves existing detectors by up to 18.7% as auxiliary signal; robust to paraphrasing attacks\"\n  limitations: [\"statistical features may not capture all AI text patterns\", \"performance on very short texts unclear\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**14. verma2024_ghostbuster.yaml**\n\n```yaml\npaper_key: \"verma2024_ghostbuster\"\ntitle: \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\"\nvenue: \"NAACL 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Perplexity-only (GPT-3 davinci perplexity threshold)\"\n    - \"DetectGPT (Mitchell et al. 2023, unsupervised perturbation-based)\"\n    - \"GPTZero (commercial detector)\"\n    - \"RoBERTa fine-tuned (supervised neural baseline)\"\n    - \"Human evaluation (17 participants)\"\n  metrics:\n    - {name: \"F1\", direction: \"higher_better\"}\n    - {name: \"Accuracy\", direction: \"higher_better\"}\n    - {name: \"Precision\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"IvyPanda Student Essays\", size: \"7,000 docs (1K human + 1K ChatGPT same-prompt + 4K ChatGPT generalization)\"}\n    - {name: \"Reuters 50-50 News Articles\", size: \"7,000 docs (same split structure)\"}\n    - {name: \"r/WritingPrompts Creative Writing\", size: \"7,000 docs (same split structure)\"}\n    - {name: \"Lang-8 non-native English\", size: \"evaluation only\"}\n    - {name: \"TOEFL 11 (essay subset)\", size: \"evaluation only\"}\n    - {name: \"TOEFL 91 (essay subset)\", size: \"evaluation only\"}\n  ablation_dimensions:\n    - \"Feature search depth (1, 2, 3, 4)\"\n    - \"Model components (with/without ada, davinci, handcrafted features)\"\n    - \"Random features vs selected features\"\n    - \"Document length (10-1000 tokens)\"\n    - \"Perturbation robustness (character/word/sentence/paragraph level)\"\n    - \"Cross-domain generalization (in-domain vs out-of-domain)\"\n    - \"Cross-model generalization (ChatGPT vs Claude)\"\n    - \"Cross-prompt generalization (5 prompt variants)\"\n  training_recipe:\n    classifier: \"Logistic regression with L2 regularization, C=1\"\n    optimizer: \"N/A (closed-form or standard sklearn solver)\"\n    lr: \"N/A\"\n    hardware: \"Not specified\"\n    feature_generation: \"Recursive composition of vector/scalar functions up to depth 3, yielding 2534 candidate features\"\n    feature_selection: \"Forward feature selection on validation set\"\n    weaker_models: \"Unigram fertility, Kneser-Ney trigram, GPT-3 ada, GPT-3 davinci\"\n  method_family: \"Feature-engineered classifier using proxy model probabilities\"\n\npositioning:\n  core_claim: \"A structured search over compositions of weaker language model probabilities, combined with a simple linear classifier, can robustly detect AI-generated text without access to the target model's token probabilities.\"\n  key_results: \"99.0 F1 in-domain across all domains (+0.9 over RoBERTa, +5.9 over GPTZero); 97.0 F1 out-of-domain average (vs 85.1 RoBERTa); 92.2 F1 on Claude generalization; 99.5 F1 across prompt variants\"\n  limitations:\n    - \"Poor performance on documents under 100 tokens (F1 drops below 80 at 25 tokens)\"\n    - \"Lower accuracy on non-native English speaker text (TOEFL 91: 74.7% accuracy, below GPTZero 92.3% and RoBERTa 96.7%)\"\n    - \"Datasets limited to British/American English, not representative of all writing styles\"\n    - \"Vulnerable to paraphrasing attacks (Undetectable.ai reduces recall from 99% to 62%)\"\n    - \"Relies on API access to GPT-3 ada/davinci which may be deprecated\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the societal impact of ChatGPT's fluent text generation — schools restricting ChatGPT, authenticity concerns across education and journalism — establishing real-world urgency.\"\n  tension: \"Existing detectors (DetectGPT, GPTZero) show poor generalization across domains and models; supervised neural methods (RoBERTa) overfit to training distribution; zero-shot methods require target model token probabilities (a black-box limitation). Additionally, high false positive rates create ethical risks, disproportionately flagging non-native English speakers.\"\n  key_insight: \"Instead of requiring the target LLM's own probabilities, use a series of weaker, accessible language models as probability proxies, then let a structured combinatorial search discover discriminative feature compositions — the signal is in how different-quality models disagree on token predictions.\"\n  argument_chain: \"Problem (LLM text indistinguishable from human) → Existing solutions fail to generalize → Key insight: weaker model probability compositions are discriminative → Structured search over vector/scalar function compositions → Simple linear classifier achieves SOTA → Validated across 3 domains, cross-model (Claude), cross-prompt, perturbation robustness, and human comparison\"\n  contribution_framing: \"Three contributions implicitly stated: (1) Ghostbuster method itself (structured search + linear classifier on weaker model probabilities), (2) three new benchmark datasets for AI text detection, (3) extensive evaluation including cross-domain, cross-model, cross-prompt generalization and robustness analysis. Framed via performance superiority: 'achieves 99.0 F1... 5.9 F1 higher than the best preexisting model.'\"\n  intro_structure: \"3 paragraphs — P1: Problem establishment (ChatGPT impact, societal concerns); P2: Existing solution failures (poor generalization, false positives, bias against non-native speakers); P3: Ghostbuster introduction with headline numbers and method sketch\"\n  notable_technique: \"Effective use of the 'black-box constraint' framing — positions the paper as solving a harder, more practical problem than prior work (no access to target model probabilities), which makes the strong results even more impressive. Also leverages the non-native speaker bias issue to establish ethical urgency.\"\n\nfigures:\n  figure_count: 6\n  figure1:\n    type: \"method_overview\"\n    description: \"Left-to-right pipeline diagram showing the three stages of Ghostbuster: (1) a text document is passed through three weaker language models (Unigram, Trigram, GPT-3) producing probability vectors, (2) vector functions (+, -, x, /, >, <) combine probability vectors, (3) scalar functions (||.||, max, var) reduce to features, (4) features fed to logistic regression classifier visualized as a scatter plot.\"\n    narrative_role: \"Provides immediate visual understanding of the full pipeline — reader grasps the method in one glance before the technical details.\"\n    design_elements: [\"Left-to-right flow\", \"Color-coded stages (blue models, purple vector ops, purple scalar ops, tan classifier)\", \"Mathematical operator symbols inside boxes\", \"Scatter plot as classifier visualization\"]\n    visual_style: \"Clean horizontal pipeline with rounded-rectangle boxes. Pastel color scheme (light blue for models, lavender for function boxes, beige for classifier). Minimal text labels. Text snippet shown as input on the left. Arrows connect stages. Compact single-row layout.\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"F1 score degradation under increasing numbers of perturbations, split into local (character/word) and global (sentence/paragraph) perturbations\"\n      how_gain_highlighted: \"Shows robustness envelope — performance stays above 80 F1 for most perturbation types until extreme levels; separate panels for local vs global perturbations make degradation patterns clear\"\n      design_note: \"Two-panel layout (local left, global right) with shared y-axis (F1 Score) and color-coded lines per perturbation type. Legend inside plot. Clear visual separation of graceful degradation (character flips) vs catastrophic failure (paraphrasing).\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"F1 score across document sizes (10-1000 tokens) for in-domain and various out-of-domain settings (Claude, WP, Reuters, Essay)\"\n      how_gain_highlighted: \"All lines converge to ~95-100 F1 at 500+ tokens, visually demonstrating reliability at longer documents; short-document weakness is honestly shown\"\n      design_note: \"Single plot with 5 color-coded lines. Dark background with grid. Log-scale-like x-axis (10,25,50,100,250,500,1000). Clearly shows the critical 100-token threshold where performance becomes reliable.\"\n  ablation_figures:\n    - figure_id: \"Figure 5\"\n      viz_type: \"feature_list\"\n      dimensions_varied: [\"Domain (News, Creative Writing, Essays)\", \"Selected features per domain\"]\n      design_note: \"Lists the actual features selected by forward selection for each domain — not a traditional chart but a reference figure showing which compositions matter.\"\n    - figure_id: \"Figure 6\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"Dataset (WritingPrompts, Reuters, IvyPanda)\", \"Entropy rate under GPT-3\"]\n      design_note: \"Entropy rate visualization comparing human vs AI text predictability across domains.\"\n  figure_narrative_role: \"Figure 1 (method overview) → Figure 2 (motivating example: human vs AI text side-by-side) → Figure 3 (robustness analysis) → Figure 4 (document length sensitivity) → Figure 5 (feature analysis, appendix) → Figure 6 (theoretical motivation via entropy, appendix). Main paper figures (1-4) follow: explain method → show problem → stress-test → analyze boundary conditions.\"\n\ntables:\n  table_count: 8\n  main_result_table:\n    table_id: \"Table 2\"\n    row_axis: \"methods\"\n    col_axis: \"domains (News, Creative Writing, Student Essays, All Domains) x settings (In-Domain, Out-of-Domain)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"Best results implied by Ghostbuster row consistently highest; no explicit bold/underline formatting noted in HTML version\"\n    statistical_reporting: \"Point estimates only, no confidence intervals or standard deviations\"\n    num_baselines: 4\n    design_note: \"Two major column groups (In-Domain | Out-of-Domain) with domain sub-columns. Clean structure shows both the in-domain ceiling and generalization gap simultaneously.\"\n  ablation_tables:\n    - table_id: \"Table 4\"\n      what_varied: [\"Feature search depth (1,2,3,4)\", \"Model components (ada, davinci, handcrafted)\", \"Feature selection method (random vs forward)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Comprehensive ablation with 9 conditions. Same column structure as Table 2 enables direct comparison.\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 1: Vector/scalar function definitions. Table 3: Generalization results (prompts, Claude, non-native). Tables 5-8: Dataset statistics, prompt templates, generation details.\"\n    reason: \"Main paper keeps only the two most important tables (main results + ablations) to maintain narrative focus.\"\n```\n\n---\n\n**15. penedo2024_fineweb.yaml**\n\n```yaml\npaper_key: \"penedo2024_fineweb\"\ntitle: \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\"\nvenue: \"NeurIPS 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - RefinedWeb\n    - C4\n    - The Pile\n    - SlimPajama\n    - RedPajama v2\n    - Dolma 1.6\n    - Dolma 1.7\n    - Matrix\n    - CC-100\n    - Colossal-OSCAR\n  metrics:\n    - {name: \"Aggregate Accuracy (avg of 9 benchmarks)\", direction: \"higher_better\"}\n    - {name: \"HellaSwag\", direction: \"higher_better\"}\n    - {name: \"MMLU\", direction: \"higher_better\"}\n    - {name: \"ARC\", direction: \"higher_better\"}\n    - {name: \"PIQA\", direction: \"higher_better\"}\n    - {name: \"WinoGrande\", direction: \"higher_better\"}\n    - {name: \"OpenBookQA\", direction: \"higher_better\"}\n    - {name: \"CommonSenseQA\", direction: \"higher_better\"}\n    - {name: \"SIQA\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"FineWeb\", size: \"15T tokens from 96 Common Crawl snapshots\"}\n    - {name: \"FineWeb-Edu\", size: \"1.3T tokens (educational subset of FineWeb)\"}\n    - {name: \"RefinedWeb\", size: \"500B tokens\"}\n    - {name: \"C4\", size: \"172B tokens\"}\n    - {name: \"The Pile\", size: \"340B tokens\"}\n    - {name: \"SlimPajama\", size: \"627B tokens\"}\n    - {name: \"RedPajama v2\", size: \"20T tokens\"}\n    - {name: \"Dolma 1.6\", size: \"3T tokens\"}\n    - {name: \"Dolma 1.7\", size: \"1.2T tokens\"}\n    - {name: \"Matrix\", size: \"1.3T tokens\"}\n    - {name: \"CC-100\", size: \"70B tokens\"}\n    - {name: \"Colossal-OSCAR\", size: \"850B tokens\"}\n  ablation_dimensions:\n    - text_extraction_method (WARC trafilatura vs WET htmlparser)\n    - base_filtering (URL blocklist + language ID + quality/repetition filters)\n    - deduplication_scope (global vs per-snapshot MinHash)\n    - deduplication_parameters (n-gram size, hash count, bucket structure, similarity threshold)\n    - C4_filter_components (terminal punctuation, JS removal, ToS, doc length, lorem ipsum)\n    - custom_heuristic_filters (50+ candidate statistics, 17 tested in Table 2)\n    - educational_quality_threshold (0-5 scale, threshold sweep)\n    - training_scale (28B tokens for filter ablations vs 350B for dedup ablations)\n  training_recipe:\n    model: \"1.82B parameters (including embeddings), Llama architecture\"\n    optimizer: \"not explicitly stated (likely AdamW given Llama architecture)\"\n    lr: \"not explicitly stated\"\n    batch_size: \"~2M tokens global batch size\"\n    sequence_length: 2048\n    tokenizer: \"GPT-2 tokenizer\"\n    hardware: \"H100 GPUs, ~80,000 GPU-hours for 70+ ablation models\"\n    filter_ablation_tokens: \"~28B tokens\"\n    dedup_ablation_tokens: \"350B tokens\"\n    edu_classifier_cost: \"6,000 H100 GPU-hours for classifying 15T tokens\"\n  method_family: \"large-scale web data curation pipeline (extraction + filtering + deduplication + quality classification)\"\n\npositioning:\n  core_claim: \"Systematic, transparent web data curation with carefully ablated design choices produces 15T-token FineWeb and 1.3T-token FineWeb-Edu that outperform all existing open pretraining datasets, closing the gap between proprietary and public data knowledge.\"\n  key_results: \"FineWeb: ~52% aggregate accuracy at 350B tokens (top among all open datasets). FineWeb-Edu: MMLU 33%->37% (+12% relative), ARC 46%->57% (+24% relative), ~2% aggregate accuracy gain over FineWeb.\"\n  limitations:\n    - \"Entirely web content from Common Crawl; no books, speech transcripts, or other data types\"\n    - \"Most ablation experiments at smaller scale (~28B tokens) due to compute constraints\"\n    - \"Evaluation limited to academic benchmarks without instruction tuning or alignment\"\n    - \"Educational quality classifier may amplify biases in what Llama-3-70B-Instruct considers 'educational'\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"Opens with the ubiquity of LLMs and immediately pivots to the dirty secret: [REDACTED] pretraining datasets behind the best open models (Llama 3, Mixtral) are not public, and curation strategies are 'closely guarded trade secrets.'\"\n  tension: \"Despite LLM performance depending heavily on data quality, the community lacks both access to high-quality large-scale datasets AND knowledge of how to build them.\"\n  key_insight: \"Global deduplication across all 96 Common Crawl snapshots paradoxically HURTS performance because it upsamples lower-quality data from older crawls.\"\n  argument_chain: \"problem (data curation is a black box) -> systematic pipeline construction -> counterintuitive dedup finding -> cumulative pipeline = FineWeb 15T -> educational filtering = FineWeb-Edu 1.3T -> validation against 10 baselines at 350B scale\"\n  contribution_framing: \"Six implicit contributions woven into intro prose rather than bulleted list.\"\n  intro_structure: \"Single long paragraph (~15 sentences). Unusually dense single-paragraph intro.\"\n  notable_technique: \"The 'ablation-as-narrative' structure: each section of the pipeline is presented as a mini-experiment with its own hypothesis, ablation, finding, and decision.\"\n\nfigures:\n  figure_count: 27\n  figure1:\n    type: \"motivation\"\n    description: \"Line plot comparing aggregate accuracy vs training tokens for two text extraction methods: WARC/trafilatura vs WET/htmlparser.\"\n    narrative_role: \"Establishes the very first pipeline decision as consequential. Sets the pattern for all subsequent ablation figures.\"\n    design_elements: [\"Clean two-line comparison\", \"Continuous training curves showing gap widens with scale\", \"Minimal design\", \"Blue vs pink color coding\"]\n    visual_style: \"Minimalist line plot, white background with faint horizontal gridlines.\"\n  result_figures:\n    - figure_id: \"Figure 9\"\n      viz_type: \"line_plot\"\n      what_compared: \"Cumulative pipeline steps at 350B token scale\"\n      how_gain_highlighted: \"Four stacked training curves with clear vertical separation\"\n      design_note: \"Shows pipeline is monotonically improving\"\n    - figure_id: \"Figure 10\"\n      viz_type: \"line_plot\"\n      what_compared: \"FineWeb and FineWeb-Edu vs 10 competing open datasets at 350B token scale\"\n      how_gain_highlighted: \"FineWeb-Edu clearly on top; warm colors for 'Ours' vs cooler colors for competitors\"\n      design_note: \"12 lines in one plot—aggressive but effective\"\n    - figure_id: \"Figure 11\"\n      viz_type: \"line_plot\"\n      what_compared: \"FineWeb-Edu vs competitors on MMLU specifically\"\n      how_gain_highlighted: \"10x token efficiency demonstrated visually\"\n      design_note: \"Single-benchmark focus for most impressive result\"\n  ablation_figures:\n    - figure_id: \"Figure 6\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"individual C4 filter components\"]\n      design_note: \"Reveals terminal punctuation filter is most impactful\"\n    - figure_id: \"Figure 7\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"custom filter combinations vs C4 vs baseline\"]\n      design_note: \"Custom FineWeb filters outperform C4 while removing less data\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"histogram\"\n      dimensions_varied: [\"deduplication method effect on punctuation distribution\"]\n      design_note: \"Reveals mechanism behind global dedup's failure\"\n    - figure_id: \"Figure 16\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"FineWeb-Edu educational quality threshold\"]\n      design_note: \"Threshold sweep ablation; threshold=3 is optimal\"\n  figure_narrative_role: \"Pipeline construction chronologically, building evidence cumulatively.\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 2\"\n    description: \"Full list of heuristic filters tested\"\n    row_axis: \"candidate filter metrics with thresholds\"\n    col_axis: \"metric | threshold | aggregate accuracy (%) | tokens removed (%)\"\n    row_organization: \"by_performance\"\n    col_organization: \"flat\"\n    highlight_strategy: \"implicit ranking by aggregate accuracy\"\n    statistical_reporting: \"single-run accuracy and token removal percentage\"\n    num_baselines: 16\n    design_note: \"Unusual 'main table' — not method-vs-baseline but filter candidate evaluation. Real main comparison is in Figure 10.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 3 (bias analysis subgroups/terms).\"\n    reason: \"Pipeline ablations shown as training curves because temporal dynamics are more informative than single-point numbers.\"\n```\n\n---\n\n**16. loki2025.yaml**\n\n```yaml\npaper_key: \"loki2025\"\ntitle: \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\"\nvenue: \"ICLR 2025 Spotlight\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"22 open-source LMMs\", \"6 closed-source LMMs\"]\n  metrics:\n    - {name: \"coarse-grained judgment accuracy\", direction: \"higher_better\"}\n    - {name: \"fine-grained anomaly selection accuracy\", direction: \"higher_better\"}\n    - {name: \"explanation quality\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"LOKI benchmark\", size: \"18K questions across 26 subcategories\"}\n  ablation_dimensions: [\"modality (video/image/3D/text/audio)\", \"difficulty level\", \"task type (judgment/selection/explanation)\"]\n  training_recipe: {optimizer: \"N/A (benchmark)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"multimodal synthetic data detection benchmark\"\n\npositioning:\n  core_claim: \"First comprehensive benchmark for evaluating LMM ability to detect synthetic data across 5 modalities with both coarse and fine-grained evaluation\"\n  key_results: \"LMMs show potential as synthetic detectors but reveal significant limitations; large gap between coarse judgment and fine-grained explanation\"\n  limitations: [\"benchmark may not cover all generation methods\", \"multimodal focus may dilute text-specific insights\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**17. tulchinskii2024_intrinsic_dim.yaml**\n\n```yaml\npaper_key: \"tulchinskii2024_intrinsic_dim\"\ntitle: \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\"\nvenue: \"NeurIPS 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"DetectGPT\", \"likelihood-based methods\", \"supervised classifiers\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"cross-domain accuracy\", direction: \"higher_better\"}\n    - {name: \"cross-model accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"multi-language text corpora (English, Chinese, etc.)\", size: \"N/A\"}\n  ablation_dimensions: [\"language\", \"generator model\", \"text domain\", \"writer proficiency level\"]\n  training_recipe: {optimizer: \"N/A (intrinsic dimension estimation)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"geometric / manifold-based detection via intrinsic dimensionality\"\n\npositioning:\n  core_claim: \"Human texts have intrinsic dimensionality ~9 (alphabet languages) / ~7 (Chinese) while AI texts are ~1.5 lower, providing a language-agnostic, domain-invariant detection signal\"\n  key_results: \"Outperforms SOTA in model-agnostic and cross-domain scenarios; stable across languages, domains, and writer proficiency levels\"\n  limitations: [\"computational cost of dimension estimation\", \"may degrade with more human-like models\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**18. editlens2026.yaml**\n\n```yaml\npaper_key: \"editlens2026\"\ntitle: \"EditLens: Quantifying the Extent of AI Editing in Text\"\nvenue: \"ICLR 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"binary AI detectors (GPTZero, etc.)\", \"ternary classifiers\"]\n  metrics:\n    - {name: \"F1 (binary)\", direction: \"higher_better\"}\n    - {name: \"F1 (ternary)\", direction: \"higher_better\"}\n    - {name: \"regression correlation\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"human-AI mixed editing dataset\", size: \"N/A\"}\n    - {name: \"Grammarly editing data\", size: \"N/A\"}\n  ablation_dimensions: [\"editing extent (continuous)\", \"similarity metric choice\", \"human annotation agreement\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"regression-based continuous AI editing quantification\"\n\npositioning:\n  core_claim: \"First to formalize AI editing detection as continuous regression rather than binary/ternary classification, achieving SOTA on both classification and regression tasks\"\n  key_results: \"Binary F1=94.7%, ternary F1=90.4%; validated against human annotators; practical Grammarly case study\"\n  limitations: [\"requires original human text for metric validation\", \"continuous scoring may be hard to interpret\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**19. cloc2025.yaml**\n\n```yaml\npaper_key: \"cloc2025\"\ntitle: \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\"\nvenue: \"CVPR 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"standard contrastive learning\", \"ordinal regression methods\", \"cross-entropy classification\"]\n  metrics:\n    - {name: \"MAE (mean absolute error)\", direction: \"lower_better\"}\n    - {name: \"classification accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"Adience (age estimation)\", size: \"N/A\"}\n    - {name: \"Historical Colour Image Dating\", size: \"N/A\"}\n    - {name: \"Knee Osteoarthritis\", size: \"N/A\"}\n    - {name: \"Indian Diabetic Retinopathy Image\", size: \"N/A\"}\n    - {name: \"Breast Carcinoma Subtyping\", size: \"N/A\"}\n  ablation_dimensions: [\"margin type\", \"number of margins\", \"contrastive pair selection\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"contrastive learning for ordinal classification\"\n\npositioning:\n  core_claim: \"Multi-margin N-pair loss enables flexible decision boundaries across adjacent ordinal categories, preserving class ordering while reducing overfitting to training bias\"\n  key_results: \"Outperforms existing ordinal classification methods on 5 real-world datasets\"\n  limitations: [\"image-focused evaluation\", \"limited to moderate number of ordinal classes\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**20. qurating2024.yaml**\n\n```yaml\npaper_key: \"qurating2024\"\ntitle: \"QuRating: Selecting High-Quality Data for Training Language Models\"\nvenue: \"ICML 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"uniform random sampling\", \"perplexity-based filtering\"]\n  metrics:\n    - {name: \"perplexity\", direction: \"lower_better\"}\n    - {name: \"in-context learning accuracy\", direction: \"higher_better\"}\n    - {name: \"training efficiency (steps to target)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"260B token pre-training corpus\", size: \"260B tokens\"}\n    - {name: \"30B token subsets sampled by quality\", size: \"30B tokens\"}\n  ablation_dimensions: [\"quality dimension (writing style, expertise, facts, educational value)\", \"quality threshold\", \"quality-diversity balance\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"1.3B parameter LMs\"}\n  method_family: \"LLM-based data quality rating for pre-training data selection\"\n\npositioning:\n  core_claim: \"LLMs can learn quality ratings from pairwise judgments across 4 dimensions, and training on educational-value-selected data matches uniform sampling with 50% fewer steps\"\n  key_results: \"Educational value selection most impactful; quality-diversity balance is critical; 1.3B models trained on 30B quality-filtered tokens\"\n  limitations: [\"limited to 1.3B scale\", \"quality dimensions may not cover all aspects\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**21. mitchell2023_detectgpt.yaml**\n\n```yaml\npaper_key: \"mitchell2023_detectgpt\"\ntitle: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\nvenue: \"ICML 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"likelihood thresholding\", \"entropy-based methods\", \"supervised classifiers (RoBERTa)\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"XSum\", size: \"N/A\"}\n    - {name: \"SQuAD\", size: \"N/A\"}\n    - {name: \"WritingPrompts\", size: \"N/A\"}\n    - {name: \"fake news (GPT-NeoX generated)\", size: \"N/A\"}\n  ablation_dimensions: [\"perturbation model\", \"number of perturbations\", \"source model size\"]\n  training_recipe: {optimizer: \"N/A (zero-shot)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"zero-shot detection via log probability curvature\"\n\npositioning:\n  core_claim: \"Machine-generated text occupies negative curvature regions of the source model's log probability function, enabling detection without training a classifier\"\n  key_results: \"GPT-NeoX 20B fake news: AUROC 0.81 → 0.95 vs strongest baseline\"\n  limitations: [\"requires perturbation model (slow)\", \"requires white-box or proxy model access\", \"short texts challenging\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**22. shi2025_closer_look.yaml**\n\n```yaml\npaper_key: \"shi2025_closer_look\"\ntitle: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\nvenue: \"NeurIPS 2025 (Spotlight)\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Vanilla replace paradigm (train on synthetic data only)\"\n    - \"Vanilla accumulate-subsample paradigm (uniform subsampling from real + all synthetic)\"\n    - \"Unconditional DDPM generation\"\n    - \"Classifier-Free Guidance (CFG, scale=2)\"\n  metrics:\n    - {name: \"Generalization Score (GS)\", direction: \"higher_better\", definition: \"Average L2 distance in DINOv2 feature space between each generated image and its nearest training neighbor\"}\n    - {name: \"FID (Frechet Inception Distance)\", direction: \"lower_better\"}\n    - {name: \"Estimated Entropy (Kozachenko-Leonenko)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"CIFAR-10\", size: \"32,768 images (32x32)\"}\n    - {name: \"FFHQ\", size: \"8,192 images (downsampled to 32x32)\"}\n    - {name: \"MNIST\", size: \"12,000 images\"}\n  ablation_dimensions:\n    - \"Dataset size (1024 to 32768 in powers of 2)\"\n    - \"Training paradigm (replace vs accumulate-subsample)\"\n    - \"Selection method (Greedy Selection vs Threshold Decay Filter vs vanilla)\"\n    - \"Number of generated candidates (N vs 2N before selection)\"\n    - \"Threshold decay rate alpha (sensitivity analysis)\"\n    - \"Classifier-Free Guidance scale\"\n    - \"Entropy vs variance as correlation target\"\n  training_recipe:\n    model: \"UNet-based DDPM (~16-19M parameters)\"\n    optimizer: \"Adam\"\n    lr: \"1e-4\"\n    weight_decay: \"1e-6\"\n    batch_size: 128\n    precision: \"FP16 mixed\"\n    diffusion_steps: 1000\n    epochs_cifar: 500\n    epochs_ffhq: 1000\n    hardware: \"Single NVIDIA A100 GPU\"\n    feature_extractor: \"DINOv2\"\n  method_family: \"Entropy-based data selection for mitigating model collapse in iterative generative training\"\n\npositioning:\n  core_claim: \"Model collapse in diffusion models manifests as a generalization-to-memorization transition driven by training data entropy shrinkage, not just variance collapse — and entropy-based data selection can effectively delay this transition.\"\n  key_results: \"Pearson r=0.91 between training data entropy and log(generalization score), dataset-size-independent. FFHQ accumulate-subsample: vanilla FID=75.7 vs Greedy Selection FID=44.7 at iteration 8. MNIST CFG: vanilla CFG FID=66.2 vs CFG+filtering FID=22.4 at iteration 8.\"\n  limitations:\n    - \"No rigorous theoretical explanation for why entropy collapses\"\n    - \"Limited to image diffusion models; no validation on language models\"\n    - \"Greedy Selection is computationally expensive (quadratic in dataset size)\"\n    - \"Only tested on 32x32 resolution images with relatively small models\"\n    - \"No formal analysis of how many iterations can be sustained before memorization\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the practical inevitability of synthetic data contamination.\"\n  tension: \"Existing perspectives on model collapse are theoretically valid but practically insufficient — variance collapse requires extremely large number of iterations.\"\n  key_insight: \"The transition from generalization to memorization is the true practical manifestation of collapse. Entropy of the training set is the key diagnostic signal, with r=0.91 correlation.\"\n  argument_chain: \"Synthetic data contamination inevitable → Existing perspectives miss practical manifestations → Generalization-to-memorization transition → Entropy shrinks → Entropy correlates with generalization → Entropy-based selection preserves diversity\"\n  contribution_framing: \"Three numbered contributions following identify-investigate-propose pattern.\"\n  intro_structure: \"3 paragraphs + 'Our Contributions' subsection.\"\n  notable_technique: \"Uses 'practical insufficiency' argument to distinguish from prior theoretical work. Visual pairing of generated images with nearest training neighbors makes memorization viscerally obvious.\"\n\nfigures:\n  figure_count: 9\n  figure1:\n    type: \"method_overview\"\n    description: \"Three-row pipeline diagram with color-coded rows (green=collapse, blue=mitigated, orange=evolution) showing the two paradigms and the generalization-to-memorization transition.\"\n    narrative_role: \"Roadmap for entire paper.\"\n    design_elements: [\"Color-coded rows\", \"Pipeline arrows\", \"Pie chart for data composition\", \"Funnel icon for selection\", \"Real face image pairs showing degradation\", \"Horizontal arrow from Generalization to Memorization\"]\n    visual_style: \"Clean horizontal flow with three visually distinct rows using pastel backgrounds.\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"qualitative_comparison + line_plot\"\n      what_compared: \"Generated images vs nearest training neighbors across iterations; GS decay curves\"\n      how_gain_highlighted: \"Left panel shows progressive visual convergence. Right panel uses labeled regime regions.\"\n      design_note: \"Powerful dual-panel design: qualitative + quantitative.\"\n    - figure_id: \"Figure 4a\"\n      viz_type: \"scatter\"\n      what_compared: \"Entropy vs generalization score across dataset sizes\"\n      how_gain_highlighted: \"Red dashed regression line through all sizes demonstrating r=0.91 universal correlation.\"\n      design_note: \"The key evidence figure. Log-scale y-axis linearizes the relationship.\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"multi_panel_line_plot\"\n      what_compared: \"GS over iterations for vanilla vs selection methods\"\n      how_gain_highlighted: \"Selection methods consistently above vanilla\"\n      design_note: \"6 subfigures grid (datasets x paradigms).\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"stacked_bar_chart_with_overlay_line\"\n      what_compared: \"Proportion of selected images from each iteration source\"\n      how_gain_highlighted: \"Selection naturally prefers real data — emergent behavior.\"\n      design_note: \"Insightful visualization of emergent behavior.\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot + 2D_scatter_projection\"\n      dimensions_varied: [\"iteration number\", \"dataset entropy\"]\n      design_note: \"SVD projections make entropy collapse visually intuitive.\"\n    - figure_id: \"Figure 4b\"\n      viz_type: \"scatter\"\n      dimensions_varied: [\"variance vs generalization score\"]\n      design_note: \"Placed next to 4a to show variance is weaker predictor.\"\n  figure_narrative_role: \"Figure 1 → Figure 2 → Figure 3 → Figure 4 → Figures 5-7 → Figure 8 → Figure 9. Discover-understand-mitigate-extend arc.\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    design_note: \"NO tables in main text. All results as line/scatter plots. Works because story is about trends over iterations.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: false\n    content: \"No tables even in appendix; all figure-based.\"\n    reason: \"Central argument is about trajectories over iterations, not static comparisons.\"\n```\n\n---\n\n**23. wu2025_detection_survey.yaml**\n\n```yaml\npaper_key: \"wu2025_detection_survey\"\ntitle: \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\"\nvenue: \"Computational Linguistics, Vol. 51, Issue 1, 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"N/A (survey paper)\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"F1\", direction: \"higher_better\"}\n    - {name: \"TPR@FPR\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"various detection benchmarks surveyed\", size: \"N/A\"}\n  ablation_dimensions: [\"method family (watermarking/statistical/neural/human-assisted)\", \"evaluation setting (in-domain/cross-domain/cross-model)\", \"attack type\"]\n  training_recipe: {optimizer: \"N/A (survey)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"survey covering watermarking, statistics-based, neural-based, and human-assisted detection\"\n\npositioning:\n  core_claim: \"Comprehensive taxonomy of LLM text detection methods organized into 4 families, with analysis of challenges including OOD generalization, adversarial attacks, and evaluation framework deficiencies\"\n  key_results: \"Identifies key gaps: OOD robustness, attack resilience, real-world data handling, lack of standardized evaluation\"\n  limitations: [\"survey scope limited to text modality\", \"rapidly evolving field\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**24. kirchenbauer2023_watermark.yaml**\n\n```yaml\npaper_key: \"kirchenbauer2023_watermark\"\ntitle: \"A Watermark for Large Language Models\"\nvenue: \"ICML 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"no watermark baseline\", \"post-hoc detection methods\"]\n  metrics:\n    - {name: \"p-value (watermark detection)\", direction: \"lower_better\"}\n    - {name: \"text quality (perplexity)\", direction: \"lower_better\"}\n    - {name: \"BLEU/ROUGE (quality preservation)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"OPT model outputs\", size: \"N/A\"}\n  ablation_dimensions: [\"green list fraction\", \"watermark strength (delta)\", \"text length\", \"model size\"]\n  training_recipe: {optimizer: \"N/A (decoding-time watermark)\", lr: \"N/A\", hardware: \"OPT multi-billion parameter models\"}\n  method_family: \"statistical watermarking via green token promotion\"\n\npositioning:\n  core_claim: \"Invisible watermarks can be embedded in LLM outputs by promoting 'green' tokens during generation, detectable from short spans without model access, with negligible quality impact\"\n  key_results: \"Algorithmically detectable watermark with interpretable p-values; tested on OPT models; information-theoretic sensitivity analysis\"\n  limitations: [\"vulnerable to paraphrasing attacks\", \"requires control of generation process\", \"green token bias may affect specific domains\"]\n  relation_to_us: \"orthogonal\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n```\n\n---\n\n**25. dohmatob2025_strong_collapse.yaml**\n\n```yaml\npaper_key: \"dohmatob2025_strong_collapse\"\ntitle: \"Strong Model Collapse\"\nvenue: \"ICLR 2025 Spotlight\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Training on pure real/original data (no synthetic contamination)\"\n    - \"Training on pure synthetic data\"\n    - \"Mixed real+synthetic data with various proportions p2\"\n    - \"Weighted single-step mixing (data weighting strategies)\"\n    - \"Dynamic multi-step mixing\"\n  metrics:\n    - {name: \"test error (E_test on real distribution)\", direction: \"lower_better\"}\n    - {name: \"test loss (cross-entropy for language modeling)\", direction: \"lower_better\"}\n    - {name: \"collapse term zeta (excess error from synthetic data)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Gaussian synthetic data (random projections)\", size: \"n=500 samples, variable d\"}\n    - {name: \"MNIST\", size: \"standard 60K/10K\"}\n    - {name: \"BabiStories\", size: \"reproduction of TinyStories via Mixtral-8x7B\"}\n  ablation_dimensions:\n    - \"synthetic data proportion p2\"\n    - \"model size m\"\n    - \"synthetic data quality c^2\"\n    - \"total training set size n\"\n    - \"parametrization rate psi=m/n\"\n    - \"interpolation threshold crossing (m=n boundary)\"\n  training_recipe:\n    optimizer: \"standard SGD/Adam for neural network experiments\"\n    lr: \"not explicitly detailed\"\n    hardware: \"not explicitly detailed\"\n    details: \"Random projections on Gaussian data (n=500); two-layer neural networks on MNIST (width m=2000); GPT-2 models (12-layer) on BabiStories\"\n  method_family: \"theoretical analysis of model collapse via bias-variance decomposition and operator-valued free probability theory\"\n\npositioning:\n  core_claim: \"Model collapse persists even when mixing real and synthetic data, as long as the fraction of synthetic data does not vanish asymptotically — establishing a 'strong' form of collapse where no fixed-proportion mixing strategy can prevent performance degradation, and larger models amplify this effect in the under-parameterized regime.\"\n  key_results: \"E_test = B + V + zeta decomposition where zeta is irreducible collapse term; 1% synthetic data sufficient to cause collapse plateau; larger models amplify collapse below interpolation threshold; double-descent pattern past m=n threshold\"\n  limitations:\n    - \"Theory focuses on supervised regression with label shifts\"\n    - \"Random projections model is simplified\"\n    - \"Gaussian feature distribution assumption\"\n    - \"Proportionate scaling limit\"\n    - \"Does not address mitigation via data filtering, detection, or curation\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the observation that AI-generated content is increasingly contaminating web training corpora, and asks whether scaling up training data can still work.\"\n  tension: \"Prior model collapse work showed degradation in recursive settings, but left open whether strategic mixing could prevent collapse. This paper proves that hope is false.\"\n  key_insight: \"The bias-variance decomposition E_test = B + V + zeta, where zeta is irreducible as long as synthetic fraction p2 is fixed (non-vanishing).\"\n  argument_chain: \"problem → question (can mixing overcome?) → theory (bias-variance-collapse decomposition) → scaling law implication → model size analysis → double-descent → data mixing strategies fail → experimental validation\"\n  contribution_framing: \"Two main results explicitly labeled: Result #1 (Strong Model Collapse) and Result #2 (Model Size and Model Collapse).\"\n  intro_structure: \"~5 paragraphs with Section 1.1 (contributions) and Section 1.2 (related work).\"\n  notable_technique: \"The 'strong' vs 'weak' framing redefines the conversation. The Pareto diagram is an effective visual argument. Mathematical elegance of the exact decomposition makes a clean, falsifiable theoretical claim.\"\n\nfigures:\n  figure_count: 8\n  figure1:\n    type: \"motivation\"\n    description: \"Pareto diagram showing test error on real data: mixed training vs real-only training.\"\n    narrative_role: \"Immediately establishes that no combination of model size and mixing achieves real-data-only performance.\"\n    design_elements: [\"Pareto frontier\", \"diagonal reference line\", \"colorbar for parametrization rate\", \"multiple quality levels\"]\n    visual_style: \"Scatter plot with Pareto frontiers; colorbar encoding model size.\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Strong model collapse in classical linear model\"\n      how_gain_highlighted: \"Direct comparison of p2=0 vs p2>0 curves; plateau is visually stark\"\n      design_note: \"Log-log scale; multiple p2 values show graduated severity\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Impact of model size on collapse\"\n      how_gain_highlighted: \"Double-descent pattern visible\"\n      design_note: \"Vertical inflection at m=n marks interpolation threshold\"\n    - figure_id: \"Figure 7\"\n      viz_type: \"line_plot\"\n      what_compared: \"Model collapse on MNIST with two-layer NN\"\n      how_gain_highlighted: \"Validates theory transfers to real image data\"\n      design_note: \"Bridges theory-practice gap\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"line_plot\"\n      what_compared: \"GPT-2 on BabiStories: test loss vs tokens and vs model depth\"\n      how_gain_highlighted: \"Left: scaling law plateau. Right: depth-dependent collapse reversal.\"\n      design_note: \"Most impactful figure — theory generalizes to autoregressive LMs\"\n  ablation_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"schematic_diagram\"\n      dimensions_varied: [\"bias B\", \"variance V\", \"collapse term zeta\"]\n      design_note: \"Illustrates B+V+zeta decomposition\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"model size\", \"data quality\", \"mixing proportion\"]\n      design_note: \"Double-descent curves\"\n  figure_narrative_role: \"Figure 1 (Pareto motivation) -> Figure 2 (decomposition) -> Figure 3 (linear model validation) -> Figure 4 (model size effects) -> Figures 5-7 (additional theory + MNIST) -> Figure 8 (GPT-2 validation). Visual claim -> mechanism -> toy -> real-world.\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    note: \"NO tables. All results via theorems and scaling curve figures.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Proofs, additional figures, experimental setup details.\"\n    reason: \"Theoretical paper — results expressed as equations and visual verification.\"\n```\n\n---\n\nAll 25 files read completely. Summary of the collection:\n\n- **8 papers with full text and detailed narrative/figure/table analysis**: bevendorff2025_two_paradigms, li2024_mage, dohmatob2024_tale_of_tails, yi2026_escaping_collapse, verma2024_ghostbuster, penedo2024_fineweb, shi2025_closer_look, dohmatob2025_strong_collapse\n- **17 papers with abstract-level research metadata only** (narrative/figures/tables marked N/A): dohmatob2024_demystified, alemohammad2024_mad, drayson2025_detection_prevents_collapse, synthetic_eggs2026, mohamed2025_broken_telephone, finlayson2024_closing, binoculars2024, fast_detectgpt2024, diveye2026, loki2025, tulchinskii2024_intrinsic_dim, editlens2026, cloc2025, qurating2024, mitchell2023_detectgpt, wu2025_detection_survey, kirchenbauer2023_watermark\n\nThe papers span two main research threads: **model collapse / synthetic data contamination** (Dohmatob x3, Alemohammad, Drayson, Yi, Shi, Mohamed, Synthetic Eggs, Finlayson) and **AI-generated text detection** (Bevendorff, Li/MAGE, Binoculars, Fast-DetectGPT, DivEye, Ghostbuster, Tulchinskii, EditLens, Mitchell/DetectGPT, Kirchenbauer/watermark, Wu/survey, LOKI), plus **data curation** (FineWeb, QuRating) and **ordinal classification** (CLOC)."
      }
    ],
    "totalDurationMs": 633523,
    "totalTokens": 86882,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 49157,
      "cache_read_input_tokens": 8271,
      "output_tokens": 29453,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 49157
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 29453,
          "cache_read_input_tokens": 8271,
          "cache_creation_input_tokens": 49157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 49157,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 25,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "4c147d6c-e6a5-4106-a201-df56d23fe8d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "0e6e1a9c-3912-4872-984a-1a18d7005762",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Tool call

_source line 21 · 2026-05-21T15:05:09.368Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X4n7pok444AmdDAUSxGXq3`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/toolu_01L5PAycANQoAxBULGQfWrCX.json",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e6e1a9c-3912-4872-984a-1a18d7005762",
  "isSidechain": false,
  "requestId": "req_011CbFvKUJXtQaGsB9HjMQT9",
  "type": "assistant",
  "uuid": "0fb3e0f0-9607-4279-b146-700bb1372267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9J7enquV19BYFnYitBNEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 29978,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1260,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 29978,
          "cache_creation_input_tokens": 1260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1260
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

_source line 22 · 2026-05-21T15:05:09.707Z_

<details><summary>↩ Tool result · reported error · `toolu_01X4n7pok444AmdDAUSxGXq3`</summary>

```text
File content (31713 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fb3e0f0-9607-4279-b146-700bb1372267",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "4e0eda39-8672-4dd8-bc05-d2869d86151e",
  "toolUseResult": "Error: File content (31713 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "0fb3e0f0-9607-4279-b146-700bb1372267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T15:05:12.972Z_

<details open><summary>🔧 Tool call — Read · `toolu_015kkkJo9MLReZYEnt7ufKuM`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/toolu_01L5PAycANQoAxBULGQfWrCX.json",
  "offset": 0,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e0eda39-8672-4dd8-bc05-d2869d86151e",
  "isSidechain": false,
  "requestId": "req_011CbFvKkWc8ptXbQsgjqYmh",
  "type": "assistant",
  "uuid": "61a3c708-a221-4dcb-aa02-d3b1dea271de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb22wp4WBqfWDo989tRLtJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 241,
      "cache_read_input_tokens": 31238,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 31238,
          "cache_creation_input_tokens": 241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 241
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

_source line 24 · 2026-05-21T15:05:13.747Z_

<details><summary>↩ Tool result · reported error · `toolu_015kkkJo9MLReZYEnt7ufKuM`</summary>

```text
File content (31713 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61a3c708-a221-4dcb-aa02-d3b1dea271de",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "652c853a-8f82-4a08-a203-fe1b5ae32176",
  "toolUseResult": "Error: File content (31713 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "61a3c708-a221-4dcb-aa02-d3b1dea271de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T15:05:16.909Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BzUkxTQ45YM5Hm9qV2kSgd`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/toolu_01L5PAycANQoAxBULGQfWrCX.json",
  "offset": 0,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "652c853a-8f82-4a08-a203-fe1b5ae32176",
  "isSidechain": false,
  "requestId": "req_011CbFvL3mBtevQF4pa4F5cs",
  "type": "assistant",
  "uuid": "5c3fed0d-ff01-4d1e-ab9e-9bd5032f28e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdRVH3ahHXvcBdcLbzrNQK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 31479,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 31479,
          "cache_creation_input_tokens": 258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 258
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

_source line 26 · 2026-05-21T15:05:17.283Z_

<details><summary>↩ Tool result · reported error · `toolu_01BzUkxTQ45YM5Hm9qV2kSgd`</summary>

```text
File content (31713 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c3fed0d-ff01-4d1e-ab9e-9bd5032f28e6",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "dc493eee-2120-42ca-8083-e0452b8b5182",
  "toolUseResult": "Error: File content (31713 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "5c3fed0d-ff01-4d1e-ab9e-9bd5032f28e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T15:05:19.701Z_

Let me read the YAML files in smaller batches directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc493eee-2120-42ca-8083-e0452b8b5182",
  "isSidechain": false,
  "requestId": "req_011CbFvLJuGLHxfaqcWGKbt2",
  "type": "assistant",
  "uuid": "de346edb-cb6f-4073-9914-19895a671b26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TK45GZqihDWBMHwPiDGygo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 31737,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 31737,
          "cache_creation_input_tokens": 258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 258
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

_source line 28 · 2026-05-21T15:05:21.024Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PrnHzkA1H7DuBrZspoH57s`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp && for f in dohmatob2024_demystified.yaml alemohammad2024_mad.yaml drayson2025_detection_prevents_collapse.yaml bevendorff2025_two_paradigms.yaml synthetic_eggs2026.yaml; do echo \"=== $f ===\"; cat \"$f\"; echo; done",
  "description": "Read batch 1 of YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de346edb-cb6f-4073-9914-19895a671b26",
  "isSidechain": false,
  "requestId": "req_011CbFvLJuGLHxfaqcWGKbt2",
  "type": "assistant",
  "uuid": "7c502eff-88e4-40f6-93d0-42509c167cfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TK45GZqihDWBMHwPiDGygo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 31737,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 31737,
          "cache_creation_input_tokens": 258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 258
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

_source line 29 · 2026-05-21T15:05:21.123Z_

<details><summary>↩ Tool result · `toolu_01PrnHzkA1H7DuBrZspoH57s`</summary>

```text
=== dohmatob2024_demystified.yaml ===
paper_key: "dohmatob2024_demystified"
title: "Model Collapse Demystified: The Case of Regression"
venue: "NeurIPS 2024"
full_text_available: false

research:
  baselines: ["no-collapse baseline (real data only)", "adaptive regularization"]
  metrics:
    - {name: "test risk / prediction error", direction: "lower_better"}
    - {name: "scaling law exponent", direction: "context_dependent"}
  datasets:
    - {name: "synthetic high-dimensional regression", size: "theoretical"}
  ablation_dimensions: ["number of recursive generations", "spectral decay rate", "source condition", "regularization strength"]
  training_recipe: {optimizer: "closed-form / ridge regression", lr: "N/A", hardware: "theoretical"}
  method_family: "theoretical analysis of model collapse in regression"

positioning:
  core_claim: "Analytic formulae characterizing model collapse in high-dimensional regression reveal modified scaling laws with crossover phenomena from fast to slow rates"
  key_results: "Derived closed-form expressions for collapse dynamics; proposed adaptive regularization as mitigation"
  limitations: ["limited to regression setting", "Gaussian assumptions"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== alemohammad2024_mad.yaml ===
paper_key: "alemohammad2024_mad"
title: "Self-Consuming Generative Models Go MAD"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["real data baseline", "mixed real+synthetic training"]
  metrics:
    - {name: "precision (quality)", direction: "higher_better"}
    - {name: "recall (diversity)", direction: "higher_better"}
    - {name: "FID", direction: "lower_better"}
  datasets:
    - {name: "FFHQ (image generation)", size: "70K"}
    - {name: "MNIST", size: "60K"}
  ablation_dimensions: ["fresh real data ratio", "number of autophagous generations", "quality-diversity tradeoff"]
  training_recipe: {optimizer: "N/A (generative models)", lr: "N/A", hardware: "N/A"}
  method_family: "theoretical + empirical analysis of autophagous (self-consuming) generative loops"

positioning:
  core_claim: "Without sufficient fresh real data in each generation, self-consuming generative models are doomed to have quality or diversity progressively decrease (Model Autophagy Disorder)"
  key_results: "Three regimes identified: fully synthetic → collapse; synthetic+sampling bias → quality loss; synthetic+fresh data → stable if ratio sufficient"
  limitations: ["primarily image domain", "simplified generation pipeline"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== drayson2025_detection_prevents_collapse.yaml ===
paper_key: "drayson2025_detection_prevents_collapse"
title: "Machine-generated text detection prevents language model collapse"
venue: "EMNLP 2025 Findings"
full_text_available: false

research:
  baselines: ["training on purely human data", "training on unfiltered mixed data"]
  metrics:
    - {name: "perplexity", direction: "lower_better"}
    - {name: "text diversity", direction: "higher_better"}
    - {name: "downstream task performance", direction: "higher_better"}
  datasets:
    - {name: "GPT-2 generated text", size: "N/A"}
    - {name: "SmolLM2 generated text", size: "N/A"}
  ablation_dimensions: ["model family (GPT-2 vs SmolLM2)", "model size (124M to 1.7B)", "number of recursive generations", "detection threshold"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "detection-based filtering + importance resampling for collapse prevention"

positioning:
  core_claim: "Using machine-generated text detectors to filter training data not only prevents model collapse but improves performance beyond training on purely human data"
  key_results: "Detection + resampling outperforms both pure human data and unfiltered mixed data across GPT-2 and SmolLM2 families"
  limitations: ["limited model families tested", "relies on detector quality"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== bevendorff2025_two_paradigms.yaml ===
paper_key: "bevendorff2025_two_paradigms"
title: "The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification"
venue: "ACL 2025 Findings"
full_text_available: true

research:
  baselines:
    - "Binoculars (Hans et al., 2024) zero-shot detector"
    - "SVM with TF-IDF word unigrams (800 features)"
    - "LoRA-fine-tuned Mistral-7B binary classifier"
    - "OpenAI RoBERTa-based GPT-2 detector (Solaiman et al., 2019)"
    - "Ghostbuster (Verma et al., 2024)"
    - "GPT-Sentinel (Chen et al., 2023)"
    - "DetectGPT (Mitchell et al., 2023)"
    - "Fast-DetectGPT (Bao et al., 2023)"
    - "DetectLLM (Su et al., 2023a)"
    - "LLMDet (Wu et al., 2023)"
  metrics:
    - {name: "False Negative Rate (FNR)", direction: "lower_better"}
    - {name: "False Positive Rate (FPR)", direction: "lower_better"}
    - {name: "AUROC", direction: "higher_better"}
    - {name: "Accuracy", direction: "higher_better"}
    - {name: "Precision-Recall curve", direction: "higher_better"}
    - {name: "c@1 (accuracy with non-answers)", direction: "higher_better"}
    - {name: "Cohen's d (effect size)", direction: "N/A"}
    - {name: "Character 3-gram entropy (bits)", direction: "N/A"}
    - {name: "MTLD (lexical diversity)", direction: "N/A"}
    - {name: "Flesch reading ease", direction: "N/A"}
    - {name: "Compression-based cosine (CBC)", direction: "lower_better"}
  datasets:
    - {name: "PAN'24 (extended with GPT-4o, 4o-mini, o1)", size: "1,359 human + 23,094 LLM texts, 15 LLMs"}
    - {name: "Human Detectors (HD)", size: "150 human + 150 LLM texts, 5 LLMs"}
    - {name: "Ghostbuster (GB) Essays", size: "994 human + 6,000 LLM texts, 6 LLMs"}
    - {name: "Ghostbuster (GB) Reuters", size: "1,000 human + 6,000 LLM texts, 6 LLMs"}
    - {name: "RAID", size: "153,217 human + 2,443,073 LLM texts, 6 LLMs"}
    - {name: "RAID (no attacks)", size: "12,766 human + 202,593 LLM texts, 6 LLMs"}
    - {name: "M4", size: "59,032 human + 57,253 LLM texts, 7 LLMs"}
    - {name: "MAGE", size: "152,382 human + 284,224 LLM texts, 131 model labels combined into 4 families"}
  ablation_dimensions:
    - "Model family used for training vs. testing (cross-model generalization)"
    - "In-domain vs. out-of-domain evaluation"
    - "Text length cutoffs (entropy analysis at increasing character lengths)"
    - "Feature set size in unmasking (top 250 vs. top 500 n-grams)"
    - "Operating point threshold (accuracy vs. low FPR vs. low FNR)"
    - "Genre-controlled vs. mixed-genre datasets"
    - "Dataset used for training (PAN vs. RAID)"
  training_recipe:
    optimizer: "Not specified for SVM; LoRA fine-tuning for Mistral-7B"
    lr: "Not specified"
    hardware: "3x A100 GPUs for 2x12h (Mistral-7B LoRA, 20M trainable parameters)"
  method_family: "Authorship analytics / computational stylometry applied to LLM detection"

positioning:
  core_claim: "LLM detection is fundamentally an authorship verification (open-set one-class) problem, not an authorship attribution (closed-set binary classification) problem, and conflating the two paradigms explains the contradictory reports of detector success and failure."
  key_results: "SVM in-domain FNR 0-7%, FPR 0-3%; OpenAI o1 is undetectable by non-o1 detectors; Binoculars FPR near zero but fails completely on o1; GPT-4o is first model with entropy consistent with human text beyond 4,000 chars; word length alone yields remarkable detection accuracy on genre-controlled datasets (Cohen's d up to 4.11)"
  limitations:
    - "Key assumption that future LLMs will become increasingly human-like in style could be wrong -- LLMs may converge to a distinct 'mean style' centroid"
    - "Only a limited number of datasets and detectors were analyzed; more experiments needed to corroborate practical implications"
    - "Humans exposed to LLM writing may adopt LLM stylistic properties, creating a feedback loop"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Generative AI is everywhere -- then immediately juxtaposes contradictory evidence: detectors regularly 'beat' benchmarks yet OpenAI shut down their own detector after 6 months citing lack of accuracy."
  tension: "The conflicting reports of success and failure in LLM detection create a puzzle. The paper frames this as a fundamental misunderstanding: researchers build attribution-style detectors but evaluate them under verification assumptions, leading to systematic errors."
  key_insight: "Revealed in Section 3.3 via a scaling thought experiment: as you add more human authors to distinguish from an LLM, the attribution approach fails because the number of humans classified as LLM asymptotically approaches all of humanity. This is exactly what current research does by compiling ever-larger corpora. The insight bridges two previously disconnected communities (authorship analytics and LLM detection)."
  argument_chain: "Contradiction in detector reports -> bridge to authorship analytics (attribution vs verification) -> theoretical argument that attribution cannot scale (Section 3.3) -> empirical evidence that LLM text properties are converging toward human (Section 4, entropy/MTLD/readability) -> detector evaluation confirming attribution works in-domain but fails cross-model especially for o1 (Section 5) -> discussion of benchmark quality and evaluation metric issues (Section 6) -> conclusion that verification framing is necessary"
  contribution_framing: "Four numbered contributions at end of intro: (1) reconcile authorship analytics with LLM detection, showing it is verification; (2) corpus analysis of how LLM text differs from human text; (3) show SOTA detectors solve attribution well; (4) discuss benchmark quality and evaluation needs for verification."
  intro_structure: "4 paragraphs: P1 sets scene (LLM text is everywhere, risks, detector interest); P2 presents the contradiction (detectors beat benchmarks vs. serious concerns, OpenAI shutting down detector); P3 frames the explanation (mix-up of attribution vs verification, bridging two communities, explains why attribution fails at scale); P4 lists four contributions with section pointers."
  notable_technique: "The thought experiment in Section 3.3 is the rhetorical centerpiece -- it takes a simple two-author scenario and iteratively adds authors to show how attribution inherently breaks down. The paper also excels at connecting a 'new' problem (LLM detection) to a well-established field (authorship analytics) that developed independently, making the reader see that the wheel is being reinvented poorly."

figures:
  figure_count: 21
  figure1:
    type: "problem_illustration"
    description: "Mean character 3-gram entropy over increasing text length with 95% confidence intervals across three datasets (PAN'24, RAID, M4). Shows per-model entropy curves diverging from human baseline after ~2,500-4,000 characters."
    narrative_role: "Core empirical evidence that LLM text has lower entropy than human text, but newer models (GPT-4o, o1) are closing the gap -- supporting the verification framing."
    design_elements: ["Multi-panel (a,b,c) by dataset", "Confidence interval shading", "Color-coded per model family", "Human baseline highlighted", "X-axis is text length, Y-axis is entropy"]
    visual_style: "Three-panel line plot with shaded confidence intervals. Clean academic style, models labeled directly on curves. Divergence point visible around 2,500 chars."
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "heatmap"
      what_compared: "FNR and FPR of SVM, Binoculars, and Mistral-7B detectors across training model families (rows) vs test model families (columns)"
      how_gain_highlighted: "Diagonal shows best in-domain performance; o1 row/column visually stands out as failing for all non-o1 detectors"
      design_note: "Complex multi-panel figure (4a-4d) combining heatmaps for SVM cross-model, SVM on PAN, Binoculars on PAN, and Mistral on PAN/RAID. Packs maximum information by varying both training and test conditions."
    - figure_id: "Figure 5 (Appendix A)"
      viz_type: "line_plot"
      what_compared: "ROC vs Precision-Recall curves at different class prevalence ratios (P/N = 0.2 to 5.0)"
      how_gain_highlighted: "Directly shows ROC is invariant to prevalence while precision degrades, supporting the argument that AUROC is misleading"
      design_note: "Side-by-side comparison with color-coded prevalence ratios makes the divergence between ROC and PR curves visually immediate."
    - figure_id: "Figure 6 (Appendix B)"
      viz_type: "box_plot"
      what_compared: "Entropy distributions at 4,500 characters as a discriminator on PAN dataset, per model"
      how_gain_highlighted: "Box spread shows which models are separable from humans on entropy alone"
      design_note: "Single compact figure showing discriminability limits of a simple feature."
    - figure_id: "Figures 7-9 (Appendix D)"
      viz_type: "heatmap"
      what_compared: "AUROC of SVM, Binoculars, and fine-tuned Mistral across all datasets"
      how_gain_highlighted: "Color intensity shows where each detector type succeeds/fails"
      design_note: "Supplements Figure 4 with AUROC values; includes bar charts for per-dataset breakdown."
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      dimensions_varied: ["Model (Llama2-70b, GPT-3.5, GPT-4o, OpenAI o1)", "Feature set size (top 250 vs top 500 n-grams)", "Pairing type (Human/Human, LLM/LLM, Human/LLM)"]
      design_note: "8-panel grid (4 models x 2 feature sizes) showing unmasking curves with IQR shading. Reveals that older models are 'inconsistently' discriminable (high in top-250 but low in top-500), while newer models like o1 are more consistent -- key evidence for the verification argument."
    - figure_id: "Figures 18-19 (Appendix G)"
      viz_type: "line_plot"
      dimensions_varied: ["All 10 model families on PAN'24", "HD dataset models"]
      design_note: "Extended unmasking curves for all models, supplementing Figure 3's selected models."
    - figure_id: "Figures 20-21 (Appendix G)"
      viz_type: "density_plot"
      dimensions_varied: ["Compression-based cosine (CBC) score distributions across model pairings"]
      design_note: "KDE density plots showing CBC score separation between same-author and cross-author pairs."
  figure_narrative_role: "Figure 1 (entropy divergence) -> Figure 2 (human entropy varies by genre) -> Figure 3 (unmasking reveals inconsistency in older LLMs vs consistency in newer ones) -> Figure 4 (detector evaluation confirms attribution works in-domain but fails cross-model). Appendix figures (5-21) provide exhaustive supporting evidence for each main-text claim. The flow is: statistical properties of text -> stylometric analysis -> detector performance."

tables:
  table_count: 6
  main_result_table:
    table_id: "N/A -- this paper primarily uses figures (heatmaps/line plots) for main results rather than traditional result tables"
    row_axis: "N/A"
    col_axis: "N/A"
    row_organization: "N/A"
    col_organization: "N/A"
    highlight_strategy: "N/A"
    statistical_reporting: "t-tests with Cohen's d effect sizes reported inline in text; Bonferroni correction for multiple comparisons"
    num_baselines: 3
    design_note: "Unusual for the field: main results are presented as heatmap figures (Figure 4) rather than tables. This is a deliberate choice that makes cross-model generalization patterns visually immediate. Statistical tests are reported inline rather than in tables."
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Tables 1-5 in appendix contain qualitative examples of low-quality/short texts from RAID, MAGE, M4, and BLOOMz datasets. Table 6 provides dataset statistics (text counts, human/LLM splits, number of LLMs per dataset)."
    reason: "Tables are used for qualitative evidence (bad data examples) and dataset metadata rather than quantitative results. All quantitative comparisons use figures. This split reflects the paper's emphasis on data quality critique -- the appendix tables serve as 'exhibit evidence' for the argument that benchmarks are flawed."

=== synthetic_eggs2026.yaml ===
paper_key: "synthetic_eggs2026"
title: "Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning"
venue: "ACL 2026 Findings"
full_text_available: false

research:
  baselines: ["human data fine-tuning", "single-source synthetic fine-tuning", "multi-source synthetic fine-tuning"]
  metrics:
    - {name: "distribution collapse measures", direction: "lower_better"}
    - {name: "adversarial robustness", direction: "higher_better"}
    - {name: "self-preference bias", direction: "lower_better"}
    - {name: "output quality", direction: "higher_better"}
    - {name: "text diversity", direction: "higher_better"}
  datasets:
    - {name: "synthetic data from multiple LLM sources", size: "N/A"}
  ablation_dimensions: ["number of source models", "human vs synthetic ratio", "source model diversity"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "synthetic data diversity analysis for fine-tuning"

positioning:
  core_claim: "Fine-tuning on diverse multi-source synthetic data mitigates distribution collapse while preserving output distribution breadth, but adversarial robustness decreases"
  key_results: "Multi-source synthetic > single-source for distribution collapse; human data best for reducing self-preference bias; synthetic data yields higher quality but lower robustness"
  limitations: ["limited to fine-tuning (not pre-training)", "specific LLM families"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c502eff-88e4-40f6-93d0-42509c167cfc",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "b3ab462b-2573-4b95-8563-b65d1cc06642",
  "toolUseResult": {
    "stdout": "=== dohmatob2024_demystified.yaml ===\npaper_key: \"dohmatob2024_demystified\"\ntitle: \"Model Collapse Demystified: The Case of Regression\"\nvenue: \"NeurIPS 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"no-collapse baseline (real data only)\", \"adaptive regularization\"]\n  metrics:\n    - {name: \"test risk / prediction error\", direction: \"lower_better\"}\n    - {name: \"scaling law exponent\", direction: \"context_dependent\"}\n  datasets:\n    - {name: \"synthetic high-dimensional regression\", size: \"theoretical\"}\n  ablation_dimensions: [\"number of recursive generations\", \"spectral decay rate\", \"source condition\", \"regularization strength\"]\n  training_recipe: {optimizer: \"closed-form / ridge regression\", lr: \"N/A\", hardware: \"theoretical\"}\n  method_family: \"theoretical analysis of model collapse in regression\"\n\npositioning:\n  core_claim: \"Analytic formulae characterizing model collapse in high-dimensional regression reveal modified scaling laws with crossover phenomena from fast to slow rates\"\n  key_results: \"Derived closed-form expressions for collapse dynamics; proposed adaptive regularization as mitigation\"\n  limitations: [\"limited to regression setting\", \"Gaussian assumptions\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== alemohammad2024_mad.yaml ===\npaper_key: \"alemohammad2024_mad\"\ntitle: \"Self-Consuming Generative Models Go MAD\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"real data baseline\", \"mixed real+synthetic training\"]\n  metrics:\n    - {name: \"precision (quality)\", direction: \"higher_better\"}\n    - {name: \"recall (diversity)\", direction: \"higher_better\"}\n    - {name: \"FID\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"FFHQ (image generation)\", size: \"70K\"}\n    - {name: \"MNIST\", size: \"60K\"}\n  ablation_dimensions: [\"fresh real data ratio\", \"number of autophagous generations\", \"quality-diversity tradeoff\"]\n  training_recipe: {optimizer: \"N/A (generative models)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"theoretical + empirical analysis of autophagous (self-consuming) generative loops\"\n\npositioning:\n  core_claim: \"Without sufficient fresh real data in each generation, self-consuming generative models are doomed to have quality or diversity progressively decrease (Model Autophagy Disorder)\"\n  key_results: \"Three regimes identified: fully synthetic → collapse; synthetic+sampling bias → quality loss; synthetic+fresh data → stable if ratio sufficient\"\n  limitations: [\"primarily image domain\", \"simplified generation pipeline\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== drayson2025_detection_prevents_collapse.yaml ===\npaper_key: \"drayson2025_detection_prevents_collapse\"\ntitle: \"Machine-generated text detection prevents language model collapse\"\nvenue: \"EMNLP 2025 Findings\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"training on purely human data\", \"training on unfiltered mixed data\"]\n  metrics:\n    - {name: \"perplexity\", direction: \"lower_better\"}\n    - {name: \"text diversity\", direction: \"higher_better\"}\n    - {name: \"downstream task performance\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"GPT-2 generated text\", size: \"N/A\"}\n    - {name: \"SmolLM2 generated text\", size: \"N/A\"}\n  ablation_dimensions: [\"model family (GPT-2 vs SmolLM2)\", \"model size (124M to 1.7B)\", \"number of recursive generations\", \"detection threshold\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"detection-based filtering + importance resampling for collapse prevention\"\n\npositioning:\n  core_claim: \"Using machine-generated text detectors to filter training data not only prevents model collapse but improves performance beyond training on purely human data\"\n  key_results: \"Detection + resampling outperforms both pure human data and unfiltered mixed data across GPT-2 and SmolLM2 families\"\n  limitations: [\"limited model families tested\", \"relies on detector quality\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== bevendorff2025_two_paradigms.yaml ===\npaper_key: \"bevendorff2025_two_paradigms\"\ntitle: \"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\"\nvenue: \"ACL 2025 Findings\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Binoculars (Hans et al., 2024) zero-shot detector\"\n    - \"SVM with TF-IDF word unigrams (800 features)\"\n    - \"LoRA-fine-tuned Mistral-7B binary classifier\"\n    - \"OpenAI RoBERTa-based GPT-2 detector (Solaiman et al., 2019)\"\n    - \"Ghostbuster (Verma et al., 2024)\"\n    - \"GPT-Sentinel (Chen et al., 2023)\"\n    - \"DetectGPT (Mitchell et al., 2023)\"\n    - \"Fast-DetectGPT (Bao et al., 2023)\"\n    - \"DetectLLM (Su et al., 2023a)\"\n    - \"LLMDet (Wu et al., 2023)\"\n  metrics:\n    - {name: \"False Negative Rate (FNR)\", direction: \"lower_better\"}\n    - {name: \"False Positive Rate (FPR)\", direction: \"lower_better\"}\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"Accuracy\", direction: \"higher_better\"}\n    - {name: \"Precision-Recall curve\", direction: \"higher_better\"}\n    - {name: \"c@1 (accuracy with non-answers)\", direction: \"higher_better\"}\n    - {name: \"Cohen's d (effect size)\", direction: \"N/A\"}\n    - {name: \"Character 3-gram entropy (bits)\", direction: \"N/A\"}\n    - {name: \"MTLD (lexical diversity)\", direction: \"N/A\"}\n    - {name: \"Flesch reading ease\", direction: \"N/A\"}\n    - {name: \"Compression-based cosine (CBC)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"PAN'24 (extended with GPT-4o, 4o-mini, o1)\", size: \"1,359 human + 23,094 LLM texts, 15 LLMs\"}\n    - {name: \"Human Detectors (HD)\", size: \"150 human + 150 LLM texts, 5 LLMs\"}\n    - {name: \"Ghostbuster (GB) Essays\", size: \"994 human + 6,000 LLM texts, 6 LLMs\"}\n    - {name: \"Ghostbuster (GB) Reuters\", size: \"1,000 human + 6,000 LLM texts, 6 LLMs\"}\n    - {name: \"RAID\", size: \"153,217 human + 2,443,073 LLM texts, 6 LLMs\"}\n    - {name: \"RAID (no attacks)\", size: \"12,766 human + 202,593 LLM texts, 6 LLMs\"}\n    - {name: \"M4\", size: \"59,032 human + 57,253 LLM texts, 7 LLMs\"}\n    - {name: \"MAGE\", size: \"152,382 human + 284,224 LLM texts, 131 model labels combined into 4 families\"}\n  ablation_dimensions:\n    - \"Model family used for training vs. testing (cross-model generalization)\"\n    - \"In-domain vs. out-of-domain evaluation\"\n    - \"Text length cutoffs (entropy analysis at increasing character lengths)\"\n    - \"Feature set size in unmasking (top 250 vs. top 500 n-grams)\"\n    - \"Operating point threshold (accuracy vs. low FPR vs. low FNR)\"\n    - \"Genre-controlled vs. mixed-genre datasets\"\n    - \"Dataset used for training (PAN vs. RAID)\"\n  training_recipe:\n    optimizer: \"Not specified for SVM; LoRA fine-tuning for Mistral-7B\"\n    lr: \"Not specified\"\n    hardware: \"3x A100 GPUs for 2x12h (Mistral-7B LoRA, 20M trainable parameters)\"\n  method_family: \"Authorship analytics / computational stylometry applied to LLM detection\"\n\npositioning:\n  core_claim: \"LLM detection is fundamentally an authorship verification (open-set one-class) problem, not an authorship attribution (closed-set binary classification) problem, and conflating the two paradigms explains the contradictory reports of detector success and failure.\"\n  key_results: \"SVM in-domain FNR 0-7%, FPR 0-3%; OpenAI o1 is undetectable by non-o1 detectors; Binoculars FPR near zero but fails completely on o1; GPT-4o is first model with entropy consistent with human text beyond 4,000 chars; word length alone yields remarkable detection accuracy on genre-controlled datasets (Cohen's d up to 4.11)\"\n  limitations:\n    - \"Key assumption that future LLMs will become increasingly human-like in style could be wrong -- LLMs may converge to a distinct 'mean style' centroid\"\n    - \"Only a limited number of datasets and detectors were analyzed; more experiments needed to corroborate practical implications\"\n    - \"Humans exposed to LLM writing may adopt LLM stylistic properties, creating a feedback loop\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Generative AI is everywhere -- then immediately juxtaposes contradictory evidence: detectors regularly 'beat' benchmarks yet OpenAI shut down their own detector after 6 months citing lack of accuracy.\"\n  tension: \"The conflicting reports of success and failure in LLM detection create a puzzle. The paper frames this as a fundamental misunderstanding: researchers build attribution-style detectors but evaluate them under verification assumptions, leading to systematic errors.\"\n  key_insight: \"Revealed in Section 3.3 via a scaling thought experiment: as you add more human authors to distinguish from an LLM, the attribution approach fails because the number of humans classified as LLM asymptotically approaches all of humanity. This is exactly what current research does by compiling ever-larger corpora. The insight bridges two previously disconnected communities (authorship analytics and LLM detection).\"\n  argument_chain: \"Contradiction in detector reports -> bridge to authorship analytics (attribution vs verification) -> theoretical argument that attribution cannot scale (Section 3.3) -> empirical evidence that LLM text properties are converging toward human (Section 4, entropy/MTLD/readability) -> detector evaluation confirming attribution works in-domain but fails cross-model especially for o1 (Section 5) -> discussion of benchmark quality and evaluation metric issues (Section 6) -> conclusion that verification framing is necessary\"\n  contribution_framing: \"Four numbered contributions at end of intro: (1) reconcile authorship analytics with LLM detection, showing it is verification; (2) corpus analysis of how LLM text differs from human text; (3) show SOTA detectors solve attribution well; (4) discuss benchmark quality and evaluation needs for verification.\"\n  intro_structure: \"4 paragraphs: P1 sets scene (LLM text is everywhere, risks, detector interest); P2 presents the contradiction (detectors beat benchmarks vs. serious concerns, OpenAI shutting down detector); P3 frames the explanation (mix-up of attribution vs verification, bridging two communities, explains why attribution fails at scale); P4 lists four contributions with section pointers.\"\n  notable_technique: \"The thought experiment in Section 3.3 is the rhetorical centerpiece -- it takes a simple two-author scenario and iteratively adds authors to show how attribution inherently breaks down. The paper also excels at connecting a 'new' problem (LLM detection) to a well-established field (authorship analytics) that developed independently, making the reader see that the wheel is being reinvented poorly.\"\n\nfigures:\n  figure_count: 21\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Mean character 3-gram entropy over increasing text length with 95% confidence intervals across three datasets (PAN'24, RAID, M4). Shows per-model entropy curves diverging from human baseline after ~2,500-4,000 characters.\"\n    narrative_role: \"Core empirical evidence that LLM text has lower entropy than human text, but newer models (GPT-4o, o1) are closing the gap -- supporting the verification framing.\"\n    design_elements: [\"Multi-panel (a,b,c) by dataset\", \"Confidence interval shading\", \"Color-coded per model family\", \"Human baseline highlighted\", \"X-axis is text length, Y-axis is entropy\"]\n    visual_style: \"Three-panel line plot with shaded confidence intervals. Clean academic style, models labeled directly on curves. Divergence point visible around 2,500 chars.\"\n  result_figures:\n    - figure_id: \"Figure 4\"\n      viz_type: \"heatmap\"\n      what_compared: \"FNR and FPR of SVM, Binoculars, and Mistral-7B detectors across training model families (rows) vs test model families (columns)\"\n      how_gain_highlighted: \"Diagonal shows best in-domain performance; o1 row/column visually stands out as failing for all non-o1 detectors\"\n      design_note: \"Complex multi-panel figure (4a-4d) combining heatmaps for SVM cross-model, SVM on PAN, Binoculars on PAN, and Mistral on PAN/RAID. Packs maximum information by varying both training and test conditions.\"\n    - figure_id: \"Figure 5 (Appendix A)\"\n      viz_type: \"line_plot\"\n      what_compared: \"ROC vs Precision-Recall curves at different class prevalence ratios (P/N = 0.2 to 5.0)\"\n      how_gain_highlighted: \"Directly shows ROC is invariant to prevalence while precision degrades, supporting the argument that AUROC is misleading\"\n      design_note: \"Side-by-side comparison with color-coded prevalence ratios makes the divergence between ROC and PR curves visually immediate.\"\n    - figure_id: \"Figure 6 (Appendix B)\"\n      viz_type: \"box_plot\"\n      what_compared: \"Entropy distributions at 4,500 characters as a discriminator on PAN dataset, per model\"\n      how_gain_highlighted: \"Box spread shows which models are separable from humans on entropy alone\"\n      design_note: \"Single compact figure showing discriminability limits of a simple feature.\"\n    - figure_id: \"Figures 7-9 (Appendix D)\"\n      viz_type: \"heatmap\"\n      what_compared: \"AUROC of SVM, Binoculars, and fine-tuned Mistral across all datasets\"\n      how_gain_highlighted: \"Color intensity shows where each detector type succeeds/fails\"\n      design_note: \"Supplements Figure 4 with AUROC values; includes bar charts for per-dataset breakdown.\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"Model (Llama2-70b, GPT-3.5, GPT-4o, OpenAI o1)\", \"Feature set size (top 250 vs top 500 n-grams)\", \"Pairing type (Human/Human, LLM/LLM, Human/LLM)\"]\n      design_note: \"8-panel grid (4 models x 2 feature sizes) showing unmasking curves with IQR shading. Reveals that older models are 'inconsistently' discriminable (high in top-250 but low in top-500), while newer models like o1 are more consistent -- key evidence for the verification argument.\"\n    - figure_id: \"Figures 18-19 (Appendix G)\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"All 10 model families on PAN'24\", \"HD dataset models\"]\n      design_note: \"Extended unmasking curves for all models, supplementing Figure 3's selected models.\"\n    - figure_id: \"Figures 20-21 (Appendix G)\"\n      viz_type: \"density_plot\"\n      dimensions_varied: [\"Compression-based cosine (CBC) score distributions across model pairings\"]\n      design_note: \"KDE density plots showing CBC score separation between same-author and cross-author pairs.\"\n  figure_narrative_role: \"Figure 1 (entropy divergence) -> Figure 2 (human entropy varies by genre) -> Figure 3 (unmasking reveals inconsistency in older LLMs vs consistency in newer ones) -> Figure 4 (detector evaluation confirms attribution works in-domain but fails cross-model). Appendix figures (5-21) provide exhaustive supporting evidence for each main-text claim. The flow is: statistical properties of text -> stylometric analysis -> detector performance.\"\n\ntables:\n  table_count: 6\n  main_result_table:\n    table_id: \"N/A -- this paper primarily uses figures (heatmaps/line plots) for main results rather than traditional result tables\"\n    row_axis: \"N/A\"\n    col_axis: \"N/A\"\n    row_organization: \"N/A\"\n    col_organization: \"N/A\"\n    highlight_strategy: \"N/A\"\n    statistical_reporting: \"t-tests with Cohen's d effect sizes reported inline in text; Bonferroni correction for multiple comparisons\"\n    num_baselines: 3\n    design_note: \"Unusual for the field: main results are presented as heatmap figures (Figure 4) rather than tables. This is a deliberate choice that makes cross-model generalization patterns visually immediate. Statistical tests are reported inline rather than in tables.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Tables 1-5 in appendix contain qualitative examples of low-quality/short texts from RAID, MAGE, M4, and BLOOMz datasets. Table 6 provides dataset statistics (text counts, human/LLM splits, number of LLMs per dataset).\"\n    reason: \"Tables are used for qualitative evidence (bad data examples) and dataset metadata rather than quantitative results. All quantitative comparisons use figures. This split reflects the paper's emphasis on data quality critique -- the appendix tables serve as 'exhibit evidence' for the argument that benchmarks are flawed.\"\n\n=== synthetic_eggs2026.yaml ===\npaper_key: \"synthetic_eggs2026\"\ntitle: \"Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\"\nvenue: \"ACL 2026 Findings\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"human data fine-tuning\", \"single-source synthetic fine-tuning\", \"multi-source synthetic fine-tuning\"]\n  metrics:\n    - {name: \"distribution collapse measures\", direction: \"lower_better\"}\n    - {name: \"adversarial robustness\", direction: \"higher_better\"}\n    - {name: \"self-preference bias\", direction: \"lower_better\"}\n    - {name: \"output quality\", direction: \"higher_better\"}\n    - {name: \"text diversity\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"synthetic data from multiple LLM sources\", size: \"N/A\"}\n  ablation_dimensions: [\"number of source models\", \"human vs synthetic ratio\", \"source model diversity\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"synthetic data diversity analysis for fine-tuning\"\n\npositioning:\n  core_claim: \"Fine-tuning on diverse multi-source synthetic data mitigates distribution collapse while preserving output distribution breadth, but adversarial robustness decreases\"\n  key_results: \"Multi-source synthetic > single-source for distribution collapse; human data best for reducing self-preference bias; synthetic data yields higher quality but lower robustness\"\n  limitations: [\"limited to fine-tuning (not pre-training)\", \"specific LLM families\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7c502eff-88e4-40f6-93d0-42509c167cfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-21T15:05:21.127Z_

```json
{
  "parentUuid": "b3ab462b-2573-4b95-8563-b65d1cc06642",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a0c515fb-207c-4bc6-a4e9-fafd38553ed1",
  "timestamp": "2026-05-21T15:05:21.127Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "a0c515fb-207c-4bc6-a4e9-fafd38553ed1",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Tool call

_source line 33 · 2026-05-21T15:05:26.311Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0138crwy7dbkbHx7Ato7n9Ty`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp && for f in li2024_mage.yaml mohamed2025_broken_telephone.yaml dohmatob2024_tale_of_tails.yaml finlayson2024_closing.yaml yi2026_escaping_collapse.yaml; do echo \"=== $f ===\"; cat \"$f\"; echo; done",
  "description": "Read batch 2 of YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0c515fb-207c-4bc6-a4e9-fafd38553ed1",
  "isSidechain": false,
  "requestId": "req_011CbFvLbRSggugcp8scjUca",
  "type": "assistant",
  "uuid": "a6a5275e-df35-4c3e-87d0-111b55537df7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaWfMEgvovf4NQE1UrqvYY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5564,
      "cache_read_input_tokens": 31995,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5564,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 31995,
          "cache_creation_input_tokens": 5564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5564
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

_source line 34 · 2026-05-21T15:05:26.396Z_

<details><summary>↩ Tool result · `toolu_0138crwy7dbkbHx7Ato7n9Ty`</summary>

```text
&lt;persisted-output>
Output too large (36.3KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/by4quedph.txt

Preview (first 2KB):
=== li2024_mage.yaml ===
paper_key: "li2024_mage"
title: "MAGE: Machine-generated Text Detection in the Wild"
venue: "ACL 2024"
full_text_available: true

research:
  baselines:
    - "Longformer (PLM-based classifier)"
    - "GLTR (GPT-2-XL + logistic regression)"
    - "FastText (word bi-gram features)"
    - "DetectGPT (zero-shot, T5-3B mask infill + GPT-J-6B scoring)"
    - "Human annotators"
    - "ChatGPT querying"
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "AvgRec (average of HumanRec and MachineRec)", direction: "higher_better"}
    - {name: "HumanRec (human text recall)", direction: "higher_better"}
    - {name: "MachineRec (machine text recall)", direction: "higher_better"}
  datasets:
    - {name: "MAGE testbed (custom)", size: "95,596 human + 236,554 machine-generated texts from 7 domains x 27 LLMs"}
    - {name: "Reddit ChangeMyView", size: "804 opinion statements"}
    - {name: "Yelp", size: "1,000 reviews"}
    - {name: "XSum", size: "1,000 news articles"}
    - {name: "TLDR", size: "777 news summaries"}
    - {name: "ELI5", size: "1,000 QA pairs"}
    - {name: "Reddit WritingPrompts", size: "1,000 stories"}
    - {name: "ROCStories", size: "1,000 stories"}
    - {name: "HellaSwag", size: "1,000 commonsense reasoning"}
    - {name: "SQuAD (Wikipedia)", size: "1,000 paragraphs"}
    - {name: "SciXGen", size: "1,000 scientific abstracts"}
    - {name: "CNN/DailyMail (frontier test)", size: "used in Testbed 7"}
    - {name: "DialogSum (frontier test)", size: "used in Testbed 7"}
    - {name: "PubMedQA (frontier test)", size: "used in Testbed 7"}
    - {name: "IMDb (frontier test)", size: "used in Testbed 7"}
  ablation_dimensions:
    - "In-distribution vs out-of-distribution (8 testbed scenarios)"
    - "Fixed-domain vs arbitrary-domain"
    - "Model-specific vs arbitrary-model"
    - "Unseen models (cross-validation over 7 model groups)"
    - "Unseen domains (cross-validation over 10 domains)"
...
&lt;/persisted-output>
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6a5275e-df35-4c3e-87d0-111b55537df7",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "35e4c203-2c1d-43d2-9280-834713ce524b",
  "toolUseResult": {
    "stdout": "=== li2024_mage.yaml ===\npaper_key: \"li2024_mage\"\ntitle: \"MAGE: Machine-generated Text Detection in the Wild\"\nvenue: \"ACL 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Longformer (PLM-based classifier)\"\n    - \"GLTR (GPT-2-XL + logistic regression)\"\n    - \"FastText (word bi-gram features)\"\n    - \"DetectGPT (zero-shot, T5-3B mask infill + GPT-J-6B scoring)\"\n    - \"Human annotators\"\n    - \"ChatGPT querying\"\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"AvgRec (average of HumanRec and MachineRec)\", direction: \"higher_better\"}\n    - {name: \"HumanRec (human text recall)\", direction: \"higher_better\"}\n    - {name: \"MachineRec (machine text recall)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"MAGE testbed (custom)\", size: \"95,596 human + 236,554 machine-generated texts from 7 domains x 27 LLMs\"}\n    - {name: \"Reddit ChangeMyView\", size: \"804 opinion statements\"}\n    - {name: \"Yelp\", size: \"1,000 reviews\"}\n    - {name: \"XSum\", size: \"1,000 news articles\"}\n    - {name: \"TLDR\", size: \"777 news summaries\"}\n    - {name: \"ELI5\", size: \"1,000 QA pairs\"}\n    - {name: \"Reddit WritingPrompts\", size: \"1,000 stories\"}\n    - {name: \"ROCStories\", size: \"1,000 stories\"}\n    - {name: \"HellaSwag\", size: \"1,000 commonsense reasoning\"}\n    - {name: \"SQuAD (Wikipedia)\", size: \"1,000 paragraphs\"}\n    - {name: \"SciXGen\", size: \"1,000 scientific abstracts\"}\n    - {name: \"CNN/DailyMail (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"DialogSum (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"PubMedQA (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"IMDb (frontier test)\", size: \"used in Testbed 7\"}\n  ablation_dimensions:\n    - \"In-distribution vs out-of-distribution (8 testbed scenarios)\"\n    - \"Fixed-domain vs arbitrary-domain\"\n    - \"Model-specific vs arbitrary-model\"\n    - \"Unseen models (cross-validation over 7 model groups)\"\n    - \"Unseen domains (cross-validation over 10 domains)\"\n    - \"Decision boundary adjustment (0.1% in-domain data)\"\n    - \"Paraphrasing attack robustness (gpt-3.5-turbo)\"\n    - \"Prompt type (continuation vs topical vs specified)\"\n    - \"PLM backbone comparison\"\n    - \"Data balance effects\"\n    - \"Randomness analysis\"\n  training_recipe:\n    optimizer: \"Adam\"\n    lr: \"0.005\"\n    dropout: \"0.1\"\n    epochs: \"5\"\n    hardware: \"8x V100 GPUs\"\n    validation_metric: \"classification accuracy\"\n    gltr_lm: \"GPT-2-XL\"\n    gltr_classifier: \"logistic regression (scikit-learn, grid search)\"\n    fasttext_epochs: \"100\"\n    detectgpt_mask_model: \"T5-3B\"\n    detectgpt_scoring_model: \"GPT-J-6B\"\n    detectgpt_mask_rate: \"15%\"\n    detectgpt_perturbations: \"100\"\n  method_family: \"PLM-based binary classification (Longformer) + statistical/zero-shot baselines for machine-generated text detection\"\n\npositioning:\n  core_claim: \"First comprehensive 'in-the-wild' testbed for machine-generated text detection spanning 7 domains and 27 LLMs, revealing that perplexity is a double-edged sword — it enables clustering but causes systematic false positives on low-perplexity human text.\"\n  key_results: \"Longformer achieves AUROC 0.99 in-distribution but drops to 0.95 on unseen models and 0.93 on unseen domains; with 0.1% boundary adjustment data, achieves 86.54% AvgRec on unseen domains + unseen model (GPT-4); paraphrasing attacks degrade AUROC to 0.75.\"\n  limitations:\n    - \"Limited model coverage — new LLMs (Alpaca, Vicuna, etc.) continuously emerge and the testbed cannot keep up\"\n    - \"Benchmark data bias — source texts may overlap with LLM pretraining data, so detection performance may not transfer to truly novel online text\"\n    - \"Vulnerability to paraphrasing attacks (AvgRec drops to 62.92% even with boundary adjustment)\"\n    - \"Perplexity bias causes systematic misclassification of low-perplexity human texts as machine-generated\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"LLMs have achieved human-level text generation, creating urgent need for detection — but existing detection research only evaluates on specific domains or specific models, leaving open how detectors perform 'in the wild'.\"\n  tension: \"Prior work assumes controlled settings (known domain, known generator). In reality, detectors face texts from unknown LLMs across diverse domains. The paper asks: can detection still work when we don't know the source?\"\n  key_insight: \"Perplexity is a double-edged sword — it is the fundamental feature separating human and machine text (machine text has lower perplexity), but detectors over-rely on it, systematically misclassifying low-perplexity human text. Diverse domains and models cause human-machine linguistic differences to converge, making detection harder.\"\n  argument_chain: \"problem (detection in controlled settings ≠ detection in the wild) → testbed construction (7 domains × 27 LLMs × 3 prompt types) → 8 progressive evaluation scenarios (in-distribution → OOD) → empirical finding (performance degrades with diversity, especially OOD) → analysis (linguistic convergence + perplexity bias) → mitigation (boundary adjustment with 0.1% data) → feasibility demonstration (86.54% on GPT-4 unseen domain)\"\n  contribution_framing: \"Three contributions: (1) comprehensive testbed with texts from diverse human writings and LLMs, (2) empirical analysis revealing diminishing linguistic differences in open-domain settings, (3) discovery that perplexity serves as fundamental but biased clustering feature. Framed as 'first' comprehensive wild-scenario evaluation.\"\n  intro_structure: \"~5 paragraphs: (1) LLMs generate human-level text → detection needed, (2) existing work limited to specific domains/models, (3) two research questions about wild detection, (4) testbed construction description, (5) key findings and contributions.\"\n  notable_technique: \"Progressive difficulty design — 8 testbeds arranged from easiest (white-box, single domain, single model) to hardest (unseen domain + unseen model + paraphrasing attack), creating a compelling narrative arc that systematically reveals when and why detection fails.\"\n\nfigures:\n  figure_count: 15\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Left side shows diverse input domains (News Title, Story Title, Question, Argument, Scientific Topic) as colored cards with arrows pointing to both Humans (stick figure at desk) and multiple LLMs (GPT-3.5, FLAN-T5, LLaMA, OPT, GLM, ...) listed vertically. The many-to-many arrows from domains to generators show the combinatorial explosion. Right side shows a 'Text' box passing through a magnifying glass 'Detector' with a question mark, leading to two possible outputs: 'Human' (messy scribble icon) and 'Machine' (clean stick figure). The layout flows left-to-right: sources → generators → mixed text → detection challenge.\"\n    narrative_role: \"Establishes the core challenge — detection must handle the combinatorial space of domains × generators, not just one domain or one model.\"\n    design_elements: [\"colored domain cards (purple/orange/green)\", \"many-to-many arrows showing combinatorial complexity\", \"magnifying glass as detector metaphor\", \"question mark conveying uncertainty\", \"stick figure icons for human vs machine\"]\n    visual_style: \"Clean line-art style with selective color on domain cards (purple, orange, green pastels). Horizontal left-to-right flow. Minimal decorative elements. Black-and-white for the detection side. Simple but effective at conveying the many-to-many challenge.\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"grouped_bar_or_line\"\n      what_compared: \"OOD detection performance on unseen models, broken down by model family and prompt type\"\n      how_gain_highlighted: \"Shows which model families are hardest to detect (OpenAI, FLAN-T5) and which prompt types are most challenging (specified prompts)\"\n      design_note: \"Separates analysis by two dimensions (model family × prompt type) to give nuanced OOD understanding rather than single aggregate number\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"bar_chart_or_line\"\n      what_compared: \"Detection performance (AvgRec) on unseen domains, identifying ROC, XSum, TLDR as hardest\"\n      how_gain_highlighted: \"Links difficulty to domain perplexity characteristics\"\n      design_note: \"Per-domain breakdown reveals systematic pattern (low-perplexity domains harder) rather than just reporting aggregate OOD performance\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"precision_recall_curve + bar_chart\"\n      what_compared: \"(a) PR curves before/after boundary adjustment, (b) performance improvement with 0.1% in-domain data\"\n      how_gain_highlighted: \"Direct before/after comparison shows dramatic improvement from minimal adaptation\"\n      design_note: \"Two-panel figure pairs theoretical (PR curve) with practical (data requirement) perspectives\"\n  ablation_figures:\n    - figure_id: \"Figure 5\"\n      viz_type: \"heatmap\"\n      dimensions_varied: [\"domain diversity\", \"model diversity\"]\n      design_note: \"Jensen-Shannon distance heatmap showing linguistic convergence as diversity increases — visual proof that the detection problem gets fundamentally harder with diversity\"\n    - figure_id: \"Figure 6\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"named entity types (ORDINAL, DATE, etc.)\"]\n      design_note: \"Shows entity distribution differences in fixed-domain setting as detection shortcuts that disappear with diversity\"\n    - figure_id: \"Figures 7-9\"\n      viz_type: \"histogram + scatter\"\n      dimensions_varied: [\"perplexity distributions\", \"prediction correctness\", \"paraphrasing effects\"]\n      design_note: \"Three-figure sequence builds the 'perplexity as double-edged sword' argument: (7) machine < human perplexity, (8) misclassified human texts have low perplexity, (9) paraphrasing shifts distributions\"\n  figure_narrative_role: \"Figure 1 (problem illustration) → Figures 2-3 (OOD performance breakdown by model/domain) → Figure 4 (boundary adjustment solution) → Figures 5-6 (linguistic convergence analysis) → Figures 7-9 (perplexity analysis arc) → Figures 10-15 (appendix: prompts, data distributions, linguistic stats). The main paper figures follow a 'problem → results → analysis → mitigation' narrative arc.\"\n\ntables:\n  table_count: 12\n  main_result_table:\n    table_id: \"Table 3\"\n    row_axis: \"methods (Longformer, FastText, GLTR, DetectGPT)\"\n    col_axis: \"testbed scenarios (Testbed 2-6) × metrics (AUROC, AvgRec, HumanRec, MachineRec)\"\n    row_organization: \"flat\"\n    col_organization: \"grouped_by_testbed\"\n    highlight_strategy: \"best results in bold across methods per testbed\"\n    statistical_reporting: \"single run numbers (no std reported for main results)\"\n    num_baselines: 4\n    design_note: \"Comprehensive table spanning both in-distribution (Testbeds 2-4) and out-of-distribution (Testbeds 5-6) in one view, enabling direct comparison of how each method degrades from ID to OOD. Progressive difficulty across columns tells the degradation story.\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"white-box detection (Testbed 1) — easiest setting as reference point\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Separated from main table to establish performance ceiling before showing degradation\"\n    - table_id: \"Table 4\"\n      what_varied: [\"decision boundary adjustment effect on Testbeds 5-6\"]\n      variation_style: \"full_numbers (before vs after adjustment)\"\n      design_note: \"Shows boundary adjustment dramatically improves domain-shift performance (AvgRec 68.40→81.78 for unseen domains)\"\n    - table_id: \"Table 5\"\n      what_varied: [\"challenging frontier tests (Testbed 7: unseen domain+model with GPT-4, Testbed 8: paraphrasing attack)\"]\n      variation_style: \"full_numbers with before/after boundary adjustment\"\n      design_note: \"Most challenging scenarios isolated in separate table — clean before/after comparison for the proposed mitigation\"\n    - table_id: \"Table 1\"\n      what_varied: [\"naive baselines (ChatGPT querying, human annotators)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Establishes that even humans (~54.5% AvgRec) and ChatGPT (~54.5% AvgRec) struggle at wild detection, motivating the need for dedicated methods\"\n    - table_id: \"Tables 8-10\"\n      what_varied: [\"randomness analysis\", \"PLM backbone comparison\", \"data balance effects\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Robustness checks in appendix ensure main findings are not artifacts of specific choices\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 6 (dataset statistics per domain), Table 7 (naive baseline test set composition), Tables 8-10 (robustness: randomness/backbone/balance), Table 11 (all methods on challenging test sets), Table 12 (length statistics)\"\n    reason: \"Main paper focuses on the progressive testbed story (Tables 1-5). Appendix holds dataset details and robustness checks that support but don't drive the narrative.\"\n\n=== mohamed2025_broken_telephone.yaml ===\npaper_key: \"mohamed2025_broken_telephone\"\ntitle: \"LLM as a Broken Telephone: Iterative Generation Distorts Information\"\nvenue: \"ACL 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"single-pass generation\", \"various prompting strategies\"]\n  metrics:\n    - {name: \"information distortion rate\", direction: \"lower_better\"}\n    - {name: \"semantic similarity to original\", direction: \"higher_better\"}\n    - {name: \"factual accuracy degradation\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"translation chain experiments\", size: \"N/A\"}\n  ablation_dimensions: [\"number of iterative generations\", \"language choice\", \"chain complexity\", \"prompting strategy\"]\n  training_recipe: {optimizer: \"N/A (inference only)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"empirical analysis of iterative LLM generation degradation\"\n\npositioning:\n  core_claim: \"LLMs systematically distort information when outputs are repeatedly processed, with distortion accumulating over iterations analogous to the broken telephone effect\"\n  key_results: \"Degradation is inevitable but mitigable through strategic prompting; language and chain complexity influence distortion rate\"\n  limitations: [\"primarily translation-based experiments\", \"limited model coverage\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== dohmatob2024_tale_of_tails.yaml ===\npaper_key: \"dohmatob2024_tale_of_tails\"\ntitle: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\nvenue: \"ICML 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Original (human/natural) data training\"\n    - \"Pure synthetic data training\"\n    - \"Mixed real+synthetic data training\"\n    - \"Hutter LLM (deterministic lookup table)\"\n    - \"Hutter++ (probabilistic bigram)\"\n    - \"Capacity-limited associative memory\"\n  metrics:\n    - {name: \"test error (scaling law exponent)\", direction: \"lower_better\"}\n    - {name: \"perplexity\", direction: \"lower_better\"}\n    - {name: \"number of skills learned (GCD answers)\", direction: \"higher_better\"}\n    - {name: \"total variation distance\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Wikitext-103\", size: \"~2M samples for fine-tuning\"}\n    - {name: \"GCD arithmetic task (Zipfian)\", size: \"300K-300M samples\"}\n    - {name: \"Synthetic bigram distributions\", size: \"variable\"}\n  ablation_dimensions:\n    - \"tail cutoff rank k (top-p/top-k truncation)\"\n    - \"tail exponent narrowing beta_prime vs beta (temperature scaling)\"\n    - \"number of recursive generations n\"\n    - \"mixing proportion pi of real vs synthetic data\"\n    - \"model capacity / embedding dimension d\"\n    - \"Zipf exponent beta\"\n    - \"training set size T\"\n  training_recipe:\n    optimizer: \"not explicitly specified in main text\"\n    lr: \"not explicitly specified in main text\"\n    hardware: \"not explicitly specified\"\n    details: \"GCD transformer trained on up to 300M samples; Llama2-7B fine-tuned on Wikitext-103 ~2M samples; synthetic data generated with various top-p and temperature settings\"\n  method_family: \"theoretical analysis of model collapse via scaling laws and tail distributions\"\n\npositioning:\n  core_claim: \"Model collapse is fundamentally a change of scaling laws caused by synthetic data losing the heavy-tailed structure of natural distributions, leading to quantifiable and predictable degradation patterns including plateau effects, skill loss, and shifted scaling exponents.\"\n  key_results: \"Double scaling law E_test ~ T^(-(beta-1)/beta) + k^(-(beta-1)) predicts performance plateau on synthetic data; multi-generation collapse shows additive degradation E_test ~ T^(-c) + n*T0^(-c); grokking phenomenon when mixing pi-fraction real data creates plateau of length ~k^beta/pi before recovery; triplet scaling law E_test ~ T^(-(1-1/beta)) + d^(-c_q) + k^(-(beta-1)) for capacity-limited models\"\n  limitations:\n    - \"Theory assumes simplified models (Zipfian distributions, deterministic labels for some results)\"\n    - \"Grokking theorem strictly holds only for deterministic ground-truth labels; probabilistic settings show attenuated S-shaped curves\"\n    - \"Real LLMs involve complex conditional distributions not fully captured by the theoretical framework\"\n    - \"Bigram and Hutter models are simplified abstractions of actual language model behavior\"\n    - \"No experiments on larger-scale models beyond Llama2-7B\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the observation that AI model scaling laws have been a key predictive tool, but the ecosystem of online data is co-evolving to contain increasing amounts of synthetic data - asking whether future models will still improve or be 'doomed to degenerate up to total collapse'. Uses the striking statistic that ChatGPT contributes 0.1% of total words generated daily by the global population.\"\n  tension: \"Existing scaling law theory assumes training on natural (heavy-tailed) data distributions, but the inevitable contamination of training corpora with synthetic data fundamentally breaks these assumptions. Prior work on model collapse identified the phenomenon but lacked a theoretical framework connecting it to scaling laws and emergent abilities.\"\n  key_insight: \"The key insight is that heavy-tailed (Zipfian) distributions are what enable power-law scaling, and AI generation mechanisms (top-p sampling, temperature scaling, finite sampling) systematically destroy these tails through three mechanisms: tail cutting, tail narrowing, and finite sampling bias. This directly links distributional properties to scaling law behavior.\"\n  argument_chain: \"problem (synthetic data contamination is inevitable) -> observation (scaling laws depend on heavy-tailed distributions) -> mechanism (AI generation cuts/narrows tails via top-p, temperature, finite sampling) -> theory (double/triplet scaling laws predict plateau and degradation) -> multi-generation analysis (collapse compounds across iterations) -> mitigation (data mixing enables grokking recovery) -> experiments (GCD transformer + Llama2-7B validate predictions)\"\n  contribution_framing: \"Four numbered contributions introduced with 'Our main findings are as follows': (1) Double Scaling Law, (2) Triplet Scaling Law for Memory-Limited Models, (3) Model Collapse over Multiple Generations, (4) Mitigation Strategies. Explicitly claims to be 'the first to theoretically and empirically analyze model collapse in the context of scaling laws and emergent abilities'.\"\n  intro_structure: \"5 paragraphs: P1=hook (scaling laws + synthetic data problem), P2=background (neural scaling laws and heavy tails), P3=problem statement (model collapse concern), P4=key insight (tail mechanisms), P5=contribution list (4 numbered findings)\"\n  notable_technique: \"The 'tale of tails' metaphor is the central narrative device - it reframes the abstract concept of model collapse into a concrete, visual story about distribution tails. The three tail destruction mechanisms (cutting, narrowing, finite sampling) provide a clean taxonomy that makes complex theory intuitive. The paper also effectively uses the GCD arithmetic task as a controlled 'microscope' for studying skill emergence and loss, before scaling up to Llama2.\"\n\nfigures:\n  figure_count: 5  # main text; ~35 total including appendices\n  figure1:\n    type: \"motivation\"\n    description: \"Illustrates the three mechanisms by which AI generation destroys distribution tails: top-p nucleus sampling (tail cutting), temperature scaling with tau>1 (tail narrowing), and finite sample bias. Shows how these mechanisms affect a Zipfian frequency distribution and connects to skill loss using GCD calculation (answers 2 and 3) as concrete examples.\"\n    narrative_role: \"Establishes the paper's core conceptual framework - visually demonstrates WHY model collapse happens by showing the mechanistic link between generation procedures and tail destruction. This is the key figure that makes the abstract theory tangible.\"\n    design_elements: [\"distribution curves with shaded truncation regions\", \"before/after comparison of tails\", \"concrete skill examples (GCD answers)\", \"three-panel layout for three mechanisms\"]\n    visual_style: \"Clean schematic diagrams with distribution curves; uses color to distinguish original vs truncated/narrowed distributions; combines mathematical distributions with concrete task examples\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Three panels illustrating main theoretical results: (Left) Double scaling law with Zipf exponent beta=3/2 showing plateau effect; (Middle) Model collapse across 5 generations showing progressive degradation; (Right) Grokking behavior showing plateau length and asymptotic recovery predictions\"\n      how_gain_highlighted: \"Theoretical predictions shown as dashed lines overlaid on empirical curves; clear separation between original data scaling (power law) and synthetic data scaling (plateau)\"\n      design_note: \"Three-panel layout maps directly to three main theorems; log-log scale makes power-law relationships linear; uses generation number as a visual variable to show progressive collapse\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Three experimental validation panels: (Left) Llama2-7B perplexity scaling on Wikitext-103 across generations; (Middle) GCD transformer scaling on original vs synthetic data; (Right) Skills (GCD answers) learned on clean vs AI-generated data\"\n      how_gain_highlighted: \"Direct visual comparison of original vs synthetic data curves; skill emergence on clean data vs skill loss on synthetic data is strikingly clear\"\n      design_note: \"Mirrors the layout of Figure 3 (theory) to enable direct theory-vs-experiment comparison; this structural parallelism strengthens the validation narrative\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"line_plot\"\n      what_compared: \"Effect of mixing real data (T_real) with AI data (T_AI) - shows performance improvement up to saturation point with k=1000 and beta=3/2\"\n      how_gain_highlighted: \"Shows the grokking transition clearly - performance plateaus then recovers as real data fraction increases\"\n      design_note: \"Single focused plot isolates the mixing mitigation result; parameters annotated directly on figure\"\n  ablation_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"combined_distribution_and_perplexity\"\n      dimensions_varied: [\"data source (original vs AI-generated)\", \"generation parameters (top-p, temperature)\"]\n      design_note: \"Two-part figure combines perplexity diagram (top) with distribution comparison (bottom); effectively demonstrates that the theoretical tail-cutting/narrowing mechanisms manifest in real LLM outputs\"\n  figure_narrative_role: \"Figure 1 (motivation: why tails matter) -> Figure 2 (empirical evidence: tails ARE destroyed in practice) -> Figure 3 (theory: predicted consequences) -> Figure 4 (validation: experiments match theory) -> Figure 5 (mitigation: data mixing helps). Clean motivation-theory-validation-solution arc.\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    note: \"This paper has NO tables. All results are presented through mathematical theorems and figures with scaling curves. This is consistent with theoretical ML papers where the primary contributions are equations/bounds rather than benchmark comparisons.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: false\n    content: \"No tables in appendix either; appendices contain proofs (Appendices C-F), additional figures (Appendix B), and experimental details (Appendices G-H)\"\n    reason: \"The paper is primarily theoretical - results are best expressed as scaling law equations and their visual verification, not tabular comparisons. The continuous nature of scaling curves makes line plots the natural presentation format.\"\n\n=== finlayson2024_closing.yaml ===\npaper_key: \"finlayson2024_closing\"\ntitle: \"Closing the Curious Case of Neural Text Degeneration\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"nucleus sampling (top-p)\", \"top-k sampling\", \"greedy decoding\", \"threshold-based truncation methods\"]\n  metrics:\n    - {name: \"text quality (human eval)\", direction: \"higher_better\"}\n    - {name: \"text quality (automatic)\", direction: \"higher_better\"}\n    - {name: \"degeneration rate\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"open-ended text generation benchmarks\", size: \"N/A\"}\n  ablation_dimensions: [\"truncation threshold\", \"entropy regime\", \"model size\"]\n  training_recipe: {optimizer: \"N/A (decoding strategy)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"truncation sampling / decoding strategy analysis\"\n\npositioning:\n  core_claim: \"The softmax bottleneck causes models to assign nonzero probability to impossible tokens; truncation sampling works by removing these, and a principled approach without arbitrary thresholds is possible\"\n  key_results: \"Theoretical proof that threshold-free truncation using softmax bottleneck properties guarantees valid token sampling\"\n  limitations: [\"focused on open-ended generation\", \"theoretical assumptions about softmax bottleneck\"]\n  relation_to_us: \"orthogonal\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== yi2026_escaping_collapse.yaml ===\npaper_key: \"yi2026_escaping_collapse\"\ntitle: \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\"\nvenue: \"ICLR 2026 (Poster)\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Unfiltered synthetic retraining (no verifier)\"\n    - \"Real-data-only OLS estimator\"\n    - \"VAE trained on full 60K MNIST (upper bound)\"\n  metrics:\n    - {name: \"MSE (parameter estimation error)\", direction: \"lower_better\"}\n    - {name: \"FID (Frechet Inception Distance)\", direction: \"lower_better\"}\n    - {name: \"ELBO (Evidence Lower Bound)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Simulated linear regression\", size: \"dimension p=8, varying sample sizes (500->2000, 1000->4000, 2000->8000)\"}\n    - {name: \"MNIST\", size: \"500 real images for init, 60K for discriminator training\"}\n  ablation_dimensions:\n    - \"Verifier bias (Delta: 0.0-0.7)\"\n    - \"Verifier selectivity/radius (r: 0.05-0.5 for linear; top-10% for VAE)\"\n    - \"Training sample size schedule (real->synthetic ratio)\"\n    - \"Verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images)\"\n    - \"Filtered vs unfiltered synthetic data\"\n  training_recipe:\n    optimizer: \"OLS (closed-form) for linear regression; standard SGD for CVAE\"\n    lr: \"N/A for OLS; not specified for VAE\"\n    hardware: \"Not specified\"\n    iterations: \"60 rounds for linear regression; 40 rounds for VAE\"\n  method_family: \"Verifier-guided synthetic data filtering for iterative model retraining\"\n\npositioning:\n  core_claim: \"External verifier-based filtering of synthetic data prevents model collapse in the short term via bias-variance tradeoff, but long-term performance converges to the verifier's knowledge center rather than ground truth -- unless the verifier is perfectly unbiased.\"\n  key_results: \"Linear regression: filtered retraining keeps MSE near 0.05 across 60 iterations while unfiltered diverges to 0.3-0.8. VAE/MNIST: FID drops from ~110 to ~40 with 60K-trained verifier over 40 iterations; with only 500-image verifier, FID plateaus at ~130.\"\n  limitations:\n    - \"Theoretical analysis restricted to linear regression; generalization to neural networks remains open\"\n    - \"VAE verifier (discriminator) is relatively simple and may reject harder-to-generate modes\"\n    - \"Synthetic retraining initialized with only 500 real images limits diversity recovery\"\n    - \"Verifier quality directly bounds long-term performance ceiling -- biased verifier leads to biased convergence\"\n    - \"No experiments on large language models or more complex generative tasks\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Synthetic data is increasingly used to train frontier generative models, but iterative retraining on self-generated data causes model collapse -- a well-documented performance degradation phenomenon.\"\n  tension: \"Prior work establishes collapse as seemingly inevitable under recursive self-training, but real practitioners already use external verification (human feedback, reward models). The question is: can verification provably escape collapse, and if so, what are the limits?\"\n  key_insight: \"Verification creates a bias-variance tradeoff: filtering reduces variance (by discarding low-quality samples) but introduces bias (toward the verifier's knowledge center). Short-term gains are real but long-term convergence is to the verifier's center, not ground truth. Presented through Theorem 3.1 (one-round decomposition) and Theorem 4.1 (long-term contraction).\"\n  argument_chain: \"model collapse problem -> prior work shows unfiltered retraining di",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/by4quedph.txt",
    "persistedOutputSize": 37202
  },
  "sourceToolAssistantUUID": "a6a5275e-df35-4c3e-87d0-111b55537df7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "35e4c203-2c1d-43d2-9280-834713ce524b",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Tool call

_source line 37 · 2026-05-21T15:05:29.498Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VsT6ofgdttKFvww4PgecQA`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/by4quedph.txt",
  "offset": 0,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35e4c203-2c1d-43d2-9280-834713ce524b",
  "isSidechain": false,
  "requestId": "req_011CbFvLyrowZhwWbUU6HqGL",
  "type": "assistant",
  "uuid": "b07dc4e5-6bd1-415a-a7a4-fd4d9b3b7765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLQ3pcvnsMqjsxJUtvU5iZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 37559,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 37559,
          "cache_creation_input_tokens": 1113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1113
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

_source line 38 · 2026-05-21T15:05:29.860Z_

<details><summary>↩ Tool result · `toolu_01VsT6ofgdttKFvww4PgecQA`</summary>

```text
0	=== li2024_mage.yaml ===
1	paper_key: "li2024_mage"
2	title: "MAGE: Machine-generated Text Detection in the Wild"
3	venue: "ACL 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Longformer (PLM-based classifier)"
9	    - "GLTR (GPT-2-XL + logistic regression)"
10	    - "FastText (word bi-gram features)"
11	    - "DetectGPT (zero-shot, T5-3B mask infill + GPT-J-6B scoring)"
12	    - "Human annotators"
13	    - "ChatGPT querying"
14	  metrics:
15	    - {name: "AUROC", direction: "higher_better"}
16	    - {name: "AvgRec (average of HumanRec and MachineRec)", direction: "higher_better"}
17	    - {name: "HumanRec (human text recall)", direction: "higher_better"}
18	    - {name: "MachineRec (machine text recall)", direction: "higher_better"}
19	  datasets:
20	    - {name: "MAGE testbed (custom)", size: "95,596 human + 236,554 machine-generated texts from 7 domains x 27 LLMs"}
21	    - {name: "Reddit ChangeMyView", size: "804 opinion statements"}
22	    - {name: "Yelp", size: "1,000 reviews"}
23	    - {name: "XSum", size: "1,000 news articles"}
24	    - {name: "TLDR", size: "777 news summaries"}
25	    - {name: "ELI5", size: "1,000 QA pairs"}
26	    - {name: "Reddit WritingPrompts", size: "1,000 stories"}
27	    - {name: "ROCStories", size: "1,000 stories"}
28	    - {name: "HellaSwag", size: "1,000 commonsense reasoning"}
29	    - {name: "SQuAD (Wikipedia)", size: "1,000 paragraphs"}
30	    - {name: "SciXGen", size: "1,000 scientific abstracts"}
31	    - {name: "CNN/DailyMail (frontier test)", size: "used in Testbed 7"}
32	    - {name: "DialogSum (frontier test)", size: "used in Testbed 7"}
33	    - {name: "PubMedQA (frontier test)", size: "used in Testbed 7"}
34	    - {name: "IMDb (frontier test)", size: "used in Testbed 7"}
35	  ablation_dimensions:
36	    - "In-distribution vs out-of-distribution (8 testbed scenarios)"
37	    - "Fixed-domain vs arbitrary-domain"
38	    - "Model-specific vs arbitrary-model"
39	    - "Unseen models (cross-validation over 7 model groups)"
40	    - "Unseen domains (cross-validation over 10 domains)"
41	    - "Decision boundary adjustment (0.1% in-domain data)"
42	    - "Paraphrasing attack robustness (gpt-3.5-turbo)"
43	    - "Prompt type (continuation vs topical vs specified)"
44	    - "PLM backbone comparison"
45	    - "Data balance effects"
46	    - "Randomness analysis"
47	  training_recipe:
48	    optimizer: "Adam"
49	    lr: "0.005"
50	    dropout: "0.1"
51	    epochs: "5"
52	    hardware: "8x V100 GPUs"
53	    validation_metric: "classification accuracy"
54	    gltr_lm: "GPT-2-XL"
55	    gltr_classifier: "logistic regression (scikit-learn, grid search)"
56	    fasttext_epochs: "100"
57	    detectgpt_mask_model: "T5-3B"
58	    detectgpt_scoring_model: "GPT-J-6B"
59	    detectgpt_mask_rate: "15%"
60	    detectgpt_perturbations: "100"
61	  method_family: "PLM-based binary classification (Longformer) + statistical/zero-shot baselines for machine-generated text detection"
62	
63	positioning:
64	  core_claim: "First comprehensive 'in-the-wild' testbed for machine-generated text detection spanning 7 domains and 27 LLMs, revealing that perplexity is a double-edged sword — it enables clustering but causes systematic false positives on low-perplexity human text."
65	  key_results: "Longformer achieves AUROC 0.99 in-distribution but drops to 0.95 on unseen models and 0.93 on unseen domains; with 0.1% boundary adjustment data, achieves 86.54% AvgRec on unseen domains + unseen model (GPT-4); paraphrasing attacks degrade AUROC to 0.75."
66	  limitations:
67	    - "Limited model coverage — new LLMs (Alpaca, Vicuna, etc.) continuously emerge and the testbed cannot keep up"
68	    - "Benchmark data bias — source texts may overlap with LLM pretraining data, so detection performance may not transfer to truly novel online text"
69	    - "Vulnerability to paraphrasing attacks (AvgRec drops to 62.92% even with boundary adjustment)"
70	    - "Perplexity bias causes systematic misclassification of low-perplexity human texts as machine-generated"
71	  relation_to_us: "competitor"
72	
73	narrative:
74	  story_type: "突破局限型"
75	  hook: "LLMs have achieved human-level text generation, creating urgent need for detection — but existing detection research only evaluates on specific domains or specific models, leaving open how detectors perform 'in the wild'."
76	  tension: "Prior work assumes controlled settings (known domain, known generator). In reality, detectors face texts from unknown LLMs across diverse domains. The paper asks: can detection still work when we don't know the source?"
77	  key_insight: "Perplexity is a double-edged sword — it is the fundamental feature separating human and machine text (machine text has lower perplexity), but detectors over-rely on it, systematically misclassifying low-perplexity human text. Diverse domains and models cause human-machine linguistic differences to converge, making detection harder."
78	  argument_chain: "problem (detection in controlled settings ≠ detection in the wild) → testbed construction (7 domains × 27 LLMs × 3 prompt types) → 8 progressive evaluation scenarios (in-distribution → OOD) → empirical finding (performance degrades with diversity, especially OOD) → analysis (linguistic convergence + perplexity bias) → mitigation (boundary adjustment with 0.1% data) → feasibility demonstration (86.54% on GPT-4 unseen domain)"
79	  contribution_framing: "Three contributions: (1) comprehensive testbed with texts from diverse human writings and LLMs, (2) empirical analysis revealing diminishing linguistic differences in open-domain settings, (3) discovery that perplexity serves as fundamental but biased clustering feature. Framed as 'first' comprehensive wild-scenario evaluation."
80	  intro_structure: "~5 paragraphs: (1) LLMs generate human-level text → detection needed, (2) existing work limited to specific domains/models, (3) two research questions about wild detection, (4) testbed construction description, (5) key findings and contributions."
81	  notable_technique: "Progressive difficulty design — 8 testbeds arranged from easiest (white-box, single domain, single model) to hardest (unseen domain + unseen model + paraphrasing attack), creating a compelling narrative arc that systematically reveals when and why detection fails."
82	
83	figures:
84	  figure_count: 15
85	  figure1:
86	    type: "problem_illustration"
87	    description: "Left side shows diverse input domains (News Title, Story Title, Question, Argument, Scientific Topic) as colored cards with arrows pointing to both Humans (stick figure at desk) and multiple LLMs (GPT-3.5, FLAN-T5, LLaMA, OPT, GLM, ...) listed vertically. The many-to-many arrows from domains to generators show the combinatorial explosion. Right side shows a 'Text' box passing through a magnifying glass 'Detector' with a question mark, leading to two possible outputs: 'Human' (messy scribble icon) and 'Machine' (clean stick figure). The layout flows left-to-right: sources → generators → mixed text → detection challenge."
88	    narrative_role: "Establishes the core challenge — detection must handle the combinatorial space of domains × generators, not just one domain or one model."
89	    design_elements: ["colored domain cards (purple/orange/green)", "many-to-many arrows showing combinatorial complexity", "magnifying glass as detector metaphor", "question mark conveying uncertainty", "stick figure icons for human vs machine"]
90	    visual_style: "Clean line-art style with selective color on domain cards (purple, orange, green pastels). Horizontal left-to-right flow. Minimal decorative elements. Black-and-white for the detection side. Simple but effective at conveying the many-to-many challenge."
91	  result_figures:
92	    - figure_id: "Figure 2"
93	      viz_type: "grouped_bar_or_line"
94	      what_compared: "OOD detection performance on unseen models, broken down by model family and prompt type"
95	      how_gain_highlighted: "Shows which model families are hardest to detect (OpenAI, FLAN-T5) and which prompt types are most challenging (specified prompts)"
96	      design_note: "Separates analysis by two dimensions (model family × prompt type) to give nuanced OOD understanding rather than single aggregate number"
97	    - figure_id: "Figure 3"
98	      viz_type: "bar_chart_or_line"
99	      what_compared: "Detection performance (AvgRec) on unseen domains, identifying ROC, XSum, TLDR as hardest"
100	      how_gain_highlighted: "Links difficulty to domain perplexity characteristics"
101	      design_note: "Per-domain breakdown reveals systematic pattern (low-perplexity domains harder) rather than just reporting aggregate OOD performance"
102	    - figure_id: "Figure 4"
103	      viz_type: "precision_recall_curve + bar_chart"
104	      what_compared: "(a) PR curves before/after boundary adjustment, (b) performance improvement with 0.1% in-domain data"
105	      how_gain_highlighted: "Direct before/after comparison shows dramatic improvement from minimal adaptation"
106	      design_note: "Two-panel figure pairs theoretical (PR curve) with practical (data requirement) perspectives"
107	  ablation_figures:
108	    - figure_id: "Figure 5"
109	      viz_type: "heatmap"
110	      dimensions_varied: ["domain diversity", "model diversity"]
111	      design_note: "Jensen-Shannon distance heatmap showing linguistic convergence as diversity increases — visual proof that the detection problem gets fundamentally harder with diversity"
112	    - figure_id: "Figure 6"
113	      viz_type: "bar_chart"
114	      dimensions_varied: ["named entity types (ORDINAL, DATE, etc.)"]
115	      design_note: "Shows entity distribution differences in fixed-domain setting as detection shortcuts that disappear with diversity"
116	    - figure_id: "Figures 7-9"
117	      viz_type: "histogram + scatter"
118	      dimensions_varied: ["perplexity distributions", "prediction correctness", "paraphrasing effects"]
119	      design_note: "Three-figure sequence builds the 'perplexity as double-edged sword' argument: (7) machine < human perplexity, (8) misclassified human texts have low perplexity, (9) paraphrasing shifts distributions"
120	  figure_narrative_role: "Figure 1 (problem illustration) → Figures 2-3 (OOD performance breakdown by model/domain) → Figure 4 (boundary adjustment solution) → Figures 5-6 (linguistic convergence analysis) → Figures 7-9 (perplexity analysis arc) → Figures 10-15 (appendix: prompts, data distributions, linguistic stats). The main paper figures follow a 'problem → results → analysis → mitigation' narrative arc."
121	
122	tables:
123	  table_count: 12
124	  main_result_table:
125	    table_id: "Table 3"
126	    row_axis: "methods (Longformer, FastText, GLTR, DetectGPT)"
127	    col_axis: "testbed scenarios (Testbed 2-6) × metrics (AUROC, AvgRec, HumanRec, MachineRec)"
128	    row_organization: "flat"
129	    col_organization: "grouped_by_testbed"
130	    highlight_strategy: "best results in bold across methods per testbed"
131	    statistical_reporting: "single run numbers (no std reported for main results)"
132	    num_baselines: 4
133	    design_note: "Comprehensive table spanning both in-distribution (Testbeds 2-4) and out-of-distribution (Testbeds 5-6) in one view, enabling direct comparison of how each method degrades from ID to OOD. Progressive difficulty across columns tells the degradation story."
134	  ablation_tables:
135	    - table_id: "Table 2"
136	      what_varied: ["white-box detection (Testbed 1) — easiest setting as reference point"]
137	      variation_style: "full_numbers"
138	      design_note: "Separated from main table to establish performance ceiling before showing degradation"
139	    - table_id: "Table 4"
140	      what_varied: ["decision boundary adjustment effect on Testbeds 5-6"]
141	      variation_style: "full_numbers (before vs after adjustment)"
142	      design_note: "Shows boundary adjustment dramatically improves domain-shift performance (AvgRec 68.40→81.78 for unseen domains)"
143	    - table_id: "Table 5"
144	      what_varied: ["challenging frontier tests (Testbed 7: unseen domain+model with GPT-4, Testbed 8: paraphrasing attack)"]
145	      variation_style: "full_numbers with before/after boundary adjustment"
146	      design_note: "Most challenging scenarios isolated in separate table — clean before/after comparison for the proposed mitigation"
147	    - table_id: "Table 1"
148	      what_varied: ["naive baselines (ChatGPT querying, human annotators)"]
149	      variation_style: "full_numbers"
150	      design_note: "Establishes that even humans (~54.5% AvgRec) and ChatGPT (~54.5% AvgRec) struggle at wild detection, motivating the need for dedicated methods"
151	    - table_id: "Tables 8-10"
152	      what_varied: ["randomness analysis", "PLM backbone comparison", "data balance effects"]
153	      variation_style: "full_numbers"
154	      design_note: "Robustness checks in appendix ensure main findings are not artifacts of specific choices"
155	  supplementary_tables:
156	    in_appendix: true
157	    content: "Table 6 (dataset statistics per domain), Table 7 (naive baseline test set composition), Tables 8-10 (robustness: randomness/backbone/balance), Table 11 (all methods on challenging test sets), Table 12 (length statistics)"
158	    reason: "Main paper focuses on the progressive testbed story (Tables 1-5). Appendix holds dataset details and robustness checks that support but don't drive the narrative."
159	
160	=== mohamed2025_broken_telephone.yaml ===
161	paper_key: "mohamed2025_broken_telephone"
162	title: "LLM as a Broken Telephone: Iterative Generation Distorts Information"
163	venue: "ACL 2025"
164	full_text_available: false
165	
166	research:
167	  baselines: ["single-pass generation", "various prompting strategies"]
168	  metrics:
169	    - {name: "information distortion rate", direction: "lower_better"}
170	    - {name: "semantic similarity to original", direction: "higher_better"}
171	    - {name: "factual accuracy degradation", direction: "lower_better"}
172	  datasets:
173	    - {name: "translation chain experiments", size: "N/A"}
174	  ablation_dimensions: ["number of iterative generations", "language choice", "chain complexity", "prompting strategy"]
175	  training_recipe: {optimizer: "N/A (inference only)", lr: "N/A", hardware: "N/A"}
176	  method_family: "empirical analysis of iterative LLM generation degradation"
177	
178	positioning:
179	  core_claim: "LLMs systematically distort information when outputs are repeatedly processed, with distortion accumulating over iterations analogous to the broken telephone effect"
180	  key_results: "Degradation is inevitable but mitigable through strategic prompting; language and chain complexity influence distortion rate"
181	  limitations: ["primarily translation-based experiments", "limited model coverage"]
182	  relation_to_us: "foundation"
183	
184	narrative: "N/A"
185	figures: "N/A"
186	tables: "N/A"
187	
188	=== dohmatob2024_tale_of_tails.yaml ===
189	paper_key: "dohmatob2024_tale_of_tails"
190	title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
191	venue: "ICML 2024"
192	full_text_available: true
193	
194	research:
195	  baselines:
196	    - "Original (human/natural) data training"
197	    - "Pure synthetic data training"
198	    - "Mixed real+synthetic data training"
199	    - "Hutter LLM (deterministic lookup table)"
200	    - "Hutter++ (probabilistic bigram)"
201	    - "Capacity-limited associative memory"
202	  metrics:
203	    - {name: "test error (scaling law exponent)", direction: "lower_better"}
204	    - {name: "perplexity", direction: "lower_better"}
205	    - {name: "number of skills learned (GCD answers)", direction: "higher_better"}
206	    - {name: "total variation distance", direction: "lower_better"}
207	  datasets:
208	    - {name: "Wikitext-103", size: "~2M samples for fine-tuning"}
209	    - {name: "GCD arithmetic task (Zipfian)", size: "300K-300M samples"}
210	    - {name: "Synthetic bigram distributions", size: "variable"}
211	  ablation_dimensions:
212	    - "tail cutoff rank k (top-p/top-k truncation)"
213	    - "tail exponent narrowing beta_prime vs beta (temperature scaling)"
214	    - "number of recursive generations n"
215	    - "mixing proportion pi of real vs synthetic data"
216	    - "model capacity / embedding dimension d"
217	    - "Zipf exponent beta"
218	    - "training set size T"
219	  training_recipe:
220	    optimizer: "not explicitly specified in main text"
221	    lr: "not explicitly specified in main text"
222	    hardware: "not explicitly specified"
223	    details: "GCD transformer trained on up to 300M samples; Llama2-7B fine-tuned on Wikitext-103 ~2M samples; synthetic data generated with various top-p and temperature settings"
224	  method_family: "theoretical analysis of model collapse via scaling laws and tail distributions"
225	
226	positioning:
227	  core_claim: "Model collapse is fundamentally a change of scaling laws caused by synthetic data losing the heavy-tailed structure of natural distributions, leading to quantifiable and predictable degradation patterns including plateau effects, skill loss, and shifted scaling exponents."
228	  key_results: "Double scaling law E_test ~ T^(-(beta-1)/beta) + k^(-(beta-1)) predicts performance plateau on synthetic data; multi-generation collapse shows additive degradation E_test ~ T^(-c) + n*T0^(-c); grokking phenomenon when mixing pi-fraction real data creates plateau of length ~k^beta/pi before recovery; triplet scaling law E_test ~ T^(-(1-1/beta)) + d^(-c_q) + k^(-(beta-1)) for capacity-limited models"
229	  limitations:
230	    - "Theory assumes simplified models (Zipfian distributions, deterministic labels for some results)"
231	    - "Grokking theorem strictly holds only for deterministic ground-truth labels; probabilistic settings show attenuated S-shaped curves"
232	    - "Real LLMs involve complex conditional distributions not fully captured by the theoretical framework"
233	    - "Bigram and Hutter models are simplified abstractions of actual language model behavior"
234	    - "No experiments on larger-scale models beyond Llama2-7B"
235	  relation_to_us: "foundation"
236	
237	narrative:
238	  story_type: "突破局限型"
239	  hook: "Opens with the observation that AI model scaling laws have been a key predictive tool, but the ecosystem of online data is co-evolving to contain increasing amounts of synthetic data - asking whether future models will still improve or be 'doomed to degenerate up to total collapse'. Uses the striking statistic that ChatGPT contributes 0.1% of total words generated daily by the global population."
240	  tension: "Existing scaling law theory assumes training on natural (heavy-tailed) data distributions, but the inevitable contamination of training corpora with synthetic data fundamentally breaks these assumptions. Prior work on model collapse identified the phenomenon but lacked a theoretical framework connecting it to scaling laws and emergent abilities."
241	  key_insight: "The key insight is that heavy-tailed (Zipfian) distributions are what enable power-law scaling, and AI generation mechanisms (top-p sampling, temperature scaling, finite sampling) systematically destroy these tails through three mechanisms: tail cutting, tail narrowing, and finite sampling bias. This directly links distributional properties to scaling law behavior."
242	  argument_chain: "problem (synthetic data contamination is inevitable) -> observation (scaling laws depend on heavy-tailed distributions) -> mechanism (AI generation cuts/narrows tails via top-p, temperature, finite sampling) -> theory (double/triplet scaling laws predict plateau and degradation) -> multi-generation analysis (collapse compounds across iterations) -> mitigation (data mixing enables grokking recovery) -> experiments (GCD transformer + Llama2-7B validate predictions)"
243	  contribution_framing: "Four numbered contributions introduced with 'Our main findings are as follows': (1) Double Scaling Law, (2) Triplet Scaling Law for Memory-Limited Models, (3) Model Collapse over Multiple Generations, (4) Mitigation Strategies. Explicitly claims to be 'the first to theoretically and empirically analyze model collapse in the context of scaling laws and emergent abilities'."
244	  intro_structure: "5 paragraphs: P1=hook (scaling laws + synthetic data problem), P2=background (neural scaling laws and heavy tails), P3=problem statement (model collapse concern), P4=key insight (tail mechanisms), P5=contribution list (4 numbered findings)"
245	  notable_technique: "The 'tale of tails' metaphor is the central narrative device - it reframes the abstract concept of model collapse into a concrete, visual story about distribution tails. The three tail destruction mechanisms (cutting, narrowing, finite sampling) provide a clean taxonomy that makes complex theory intuitive. The paper also effectively uses the GCD arithmetic task as a controlled 'microscope' for studying skill emergence and loss, before scaling up to Llama2."
246	
247	figures:
248	  figure_count: 5  # main text; ~35 total including appendices
249	  figure1:
250	    type: "motivation"
251	    description: "Illustrates the three mechanisms by which AI generation destroys distribution tails: top-p nucleus sampling (tail cutting), temperature scaling with tau>1 (tail narrowing), and finite sample bias. Shows how these mechanisms affect a Zipfian frequency distribution and connects to skill loss using GCD calculation (answers 2 and 3) as concrete examples."
252	    narrative_role: "Establishes the paper's core conceptual framework - visually demonstrates WHY model collapse happens by showing the mechanistic link between generation procedures and tail destruction. This is the key figure that makes the abstract theory tangible."
253	    design_elements: ["distribution curves with shaded truncation regions", "before/after comparison of tails", "concrete skill examples (GCD answers)", "three-panel layout for three mechanisms"]
254	    visual_style: "Clean schematic diagrams with distribution curves; uses color to distinguish original vs truncated/narrowed distributions; combines mathematical distributions with concrete task examples"
255	  result_figures:
256	    - figure_id: "Figure 3"
257	      viz_type: "line_plot"
258	      what_compared: "Three panels illustrating main theoretical results: (Left) Double scaling law with Zipf exponent beta=3/2 showing plateau effect; (Middle) Model collapse across 5 generations showing progressive degradation; (Right) Grokking behavior showing plateau length and asymptotic recovery predictions"
259	      how_gain_highlighted: "Theoretical predictions shown as dashed lines overlaid on empirical curves; clear separation between original data scaling (power law) and synthetic data scaling (plateau)"
260	      design_note: "Three-panel layout maps directly to three main theorems; log-log scale makes power-law relationships linear; uses generation number as a visual variable to show progressive collapse"
261	    - figure_id: "Figure 4"
262	      viz_type: "line_plot"
263	      what_compared: "Three experimental validation panels: (Left) Llama2-7B perplexity scaling on Wikitext-103 across generations; (Middle) GCD transformer scaling on original vs synthetic data; (Right) Skills (GCD answers) learned on clean vs AI-generated data"
264	      how_gain_highlighted: "Direct visual comparison of original vs synthetic data curves; skill emergence on clean data vs skill loss on synthetic data is strikingly clear"
265	      design_note: "Mirrors the layout of Figure 3 (theory) to enable direct theory-vs-experiment comparison; this structural parallelism strengthens the validation narrative"
266	    - figure_id: "Figure 5"
267	      viz_type: "line_plot"
268	      what_compared: "Effect of mixing real data (T_real) with AI data (T_AI) - shows performance improvement up to saturation point with k=1000 and beta=3/2"
269	      how_gain_highlighted: "Shows the grokking transition clearly - performance plateaus then recovers as real data fraction increases"
270	      design_note: "Single focused plot isolates the mixing mitigation result; parameters annotated directly on figure"
271	  ablation_figures:
272	    - figure_id: "Figure 2"
273	      viz_type: "combined_distribution_and_perplexity"
274	      dimensions_varied: ["data source (original vs AI-generated)", "generation parameters (top-p, temperature)"]
275	      design_note: "Two-part figure combines perplexity diagram (top) with distribution comparison (bottom); effectively demonstrates that the theoretical tail-cutting/narrowing mechanisms manifest in real LLM outputs"
276	  figure_narrative_role: "Figure 1 (motivation: why tails matter) -> Figure 2 (empirical evidence: tails ARE destroyed in practice) -> Figure 3 (theory: predicted consequences) -> Figure 4 (validation: experiments match theory) -> Figure 5 (mitigation: data mixing helps). Clean motivation-theory-validation-solution arc."
277	
278	tables:
279	  table_count: 0
280	  main_result_table:
281	    note: "This paper has NO tables. All results are presented through mathematical theorems and figures with scaling curves. This is consistent with theoretical ML papers where the primary contributions are equations/bounds rather than benchmark comparisons."
282	  ablation_tables: []
283	  supplementary_tables:
284	    in_appendix: false
285	    content: "No tables in appendix either; appendices contain proofs (Appendices C-F), additional figures (Appendix B), and experimental details (Appendices G-H)"
286	    reason: "The paper is primarily theoretical - results are best expressed as scaling law equations and their visual verification, not tabular comparisons. The continuous nature of scaling curves makes line plots the natural presentation format."
287	
288	=== finlayson2024_closing.yaml ===
289	paper_key: "finlayson2024_closing"
290	title: "Closing the Curious Case of Neural Text Degeneration"
291	venue: "ICLR 2024"
292	full_text_available: false
293	
294	research:
295	  baselines: ["nucleus sampling (top-p)", "top-k sampling", "greedy decoding", "threshold-based truncation methods"]
296	  metrics:
297	    - {name: "text quality (human eval)", direction: "higher_better"}
298	    - {name: "text quality (automatic)", direction: "higher_better"}
299	    - {name: "degeneration rate", direction: "lower_better"}
300	  datasets:
301	    - {name: "open-ended text generation benchmarks", size: "N/A"}
302	  ablation_dimensions: ["truncation threshold", "entropy regime", "model size"]
303	  training_recipe: {optimizer: "N/A (decoding strategy)", lr: "N/A", hardware: "N/A"}
304	  method_family: "truncation sampling / decoding strategy analysis"
305	
306	positioning:
307	  core_claim: "The softmax bottleneck causes models to assign nonzero probability to impossible tokens; truncation sampling works by removing these, and a principled approach without arbitrary thresholds is possible"
308	  key_results: "Theoretical proof that threshold-free truncation using softmax bottleneck properties guarantees valid token sampling"
309	  limitations: ["focused on open-ended generation", "theoretical assumptions about softmax bottleneck"]
310	  relation_to_us: "orthogonal"
311	
312	narrative: "N/A"
313	figures: "N/A"
314	tables: "N/A"
315	
316	=== yi2026_escaping_collapse.yaml ===
317	paper_key: "yi2026_escaping_collapse"
318	title: "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence"
319	venue: "ICLR 2026 (Poster)"
320	full_text_available: true
321	
322	research:
323	  baselines:
324	    - "Unfiltered synthetic retraining (no verifier)"
325	    - "Real-data-only OLS estimator"
326	    - "VAE trained on full 60K MNIST (upper bound)"
327	  metrics:
328	    - {name: "MSE (parameter estimation error)", direction: "lower_better"}
329	    - {name: "FID (Frechet Inception Distance)", direction: "lower_better"}
330	    - {name: "ELBO (Evidence Lower Bound)", direction: "lower_better"}
331	  datasets:
332	    - {name: "Simulated linear regression", size: "dimension p=8, varying sample sizes (500->2000, 1000->4000, 2000->8000)"}
333	    - {name: "MNIST", size: "500 real images for init, 60K for discriminator training"}
334	  ablation_dimensions:
335	    - "Verifier bias (Delta: 0.0-0.7)"
336	    - "Verifier selectivity/radius (r: 0.05-0.5 for linear; top-10% for VAE)"
337	    - "Training sample size schedule (real->synthetic ratio)"
338	    - "Verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images)"
339	    - "Filtered vs unfiltered synthetic data"
340	  training_recipe:
341	    optimizer: "OLS (closed-form) for linear regression; standard SGD for CVAE"
342	    lr: "N/A for OLS; not specified for VAE"
343	    hardware: "Not specified"
344	    iterations: "60 rounds for linear regression; 40 rounds for VAE"
345	  method_family: "Verifier-guided synthetic data filtering for iterative model retraining"
346	
347	positioning:
348	  core_claim: "External verifier-based filtering of synthetic data prevents model collapse in the short term via bias-variance tradeoff, but long-term performance converges to the verifier's knowledge center rather than ground truth -- unless the verifier is perfectly unbiased."
349	  key_results: "Linear regression: filtered retraining keeps MSE near 0.05 across 60 iterations while unfiltered diverges to 0.3-0.8. VAE/MNIST: FID drops from ~110 to ~40 with 60K-trained verifier over 40 iterations; with only 500-image verifier, FID plateaus at ~130."
350	  limitations:
351	    - "Theoretical analysis restricted to linear regression; generalization to neural networks remains open"
352	    - "VAE verifier (discriminator) is relatively simple and may reject harder-to-generate modes"
353	    - "Synthetic retraining initialized with only 500 real images limits diversity recovery"
354	    - "Verifier quality directly bounds long-term performance ceiling -- biased verifier leads to biased convergence"
355	    - "No experiments on large language models or more complex generative tasks"
356	  relation_to_us: "complementary"
357	
358	narrative:
359	  story_type: "突破局限型"
360	  hook: "Synthetic data is increasingly used to train frontier generative models, but iterative retraining on self-generated data causes model collapse -- a well-documented performance degradation phenomenon."
361	  tension: "Prior work establishes collapse as seemingly inevitable under recursive self-training, but real practitioners already use external verification (human feedback, reward models). The question is: can verification provably escape collapse, and if so, what are the limits?"
362	  key_insight: "Verification creates a bias-variance tradeoff: filtering reduces variance (by discarding low-quality samples) but introduces bias (toward the verifier's knowledge center). Short-term gains are real but long-term convergence is to the verifier's center, not ground truth. Presented through Theorem 3.1 (one-round decomposition) and Theorem 4.1 (long-term contraction)."
363	  argument_chain: "model collapse problem -> prior work shows unfiltered retraining diverges -> introduce verifier-based filtering framework (Generate-Verify-Retrain) -> theoretical analysis: one-round improvement via bias-variance decomposition (Theorem 3.1) -> long-term convergence to verifier center (Theorem 4.1) -> empirical validation on linear regression + VAE/MNIST -> conclusion: verification helps but is fundamentally bounded by verifier quality"
364	  contribution_framing: "Three research questions framed as Q1 (does verification help short-term?), Q2 (do gains sustain long-term?), Q3 (empirical validation). Each answered with a theorem or experiment. Contribution count: 3 clearly delineated."
365	  intro_structure: "4 paragraphs: (1) motivation on synthetic data and model collapse concern, (2) research questions about verifier-based filtering, (3) prior literature context and gaps, (4) bullet-point contributions with theorem references"
366	  notable_technique: "Framing the two results as a deliberate tension -- short-term improvement (good news) vs long-term convergence to verifier center (cautionary news) -- creates a 'promise and peril' narrative arc that is more nuanced than a pure positive-result paper."
367	
368	figures:
369	  figure_count: 5
370	  figure1:
371	    type: "teaser_result"
372	    description: "Three-panel comparison showing VAE-generated MNIST digits: (left) original data, (center-top) with verified synthetic data after 40 rounds showing maintained quality, (center-bottom) without verification showing severe collapse/degradation. (right) upper bound from training on all 60K real images."
373	    narrative_role: "Immediately demonstrates the paper's core claim visually -- verification prevents collapse while unfiltered retraining produces unrecognizable outputs. Placed before any theory to motivate the reader."
374	    design_elements: ["Before/after comparison", "With/without verification contrast", "Real sample grids", "Upper bound reference", "Arrow annotations connecting panels"]
375	    visual_style: "Black background with white MNIST digit grids arranged horizontally. Arrows with text labels ('With Data Verification' / 'Without Data Verification') connect the initial model to the two outcomes. Clean, high-contrast layout. Roughly 4-panel horizontal arrangement."
376	  result_figures:
377	    - figure_id: "Figure 3"
378	      viz_type: "heatmap + heatmap"
379	      what_compared: "One-round improvement landscape as function of verifier bias (Delta) and selectivity radius (r). Left (3a): theory-predicted loss landscape. Right (3b): empirical simulation."
380	      how_gain_highlighted: "Green regions indicate improvement (log ratio > 0), red regions indicate degradation. Theory-empirical match validates the theoretical framework."
381	      design_note: "Diverging green-red colormap centered at 0 makes improvement/degradation regions immediately readable. Side-by-side theory vs empirical layout validates theoretical predictions visually. Axes are interpretable parameters (bias, radius)."
382	    - figure_id: "Figure 4a"
383	      viz_type: "line_plot"
384	      what_compared: "Convergence of parameter estimate to verifier center (theta_c) over 60 iterations for different verifier radii (r=0.1, 0.5, 1, 1.5) with biased verifier"
385	      how_gain_highlighted: "All curves converge to near-zero distance from theta_c, confirming Theorem 4.1. Smaller radius = faster convergence."
386	      design_note: "Clean line plot with distinct colors for each radius value. Y-axis is distance to verifier center, clearly showing contraction. Legend is simple and readable."
387	    - figure_id: "Figure 4b"
388	      viz_type: "line_plot"
389	      what_compared: "Filtered (solid) vs unfiltered (dashed) retraining across different sample size schedules (500->2000, 1000->4000, 2000->8000) over 60 iterations with unbiased verifier"
390	      how_gain_highlighted: "Solid lines (filtered) stay flat near 0.05 while dashed lines (unfiltered) diverge upward to 0.3-0.8. Dramatic visual separation between the two groups."
391	      design_note: "Solid vs dashed line encoding for filtered/unfiltered is effective. Three colors for three sample size conditions. The divergence of dashed lines visually dramatizes model collapse."
392	    - figure_id: "Figure 5a"
393	      viz_type: "line_plot"
394	      what_compared: "VAE FID scores over 40 iterations comparing different VAE training sample sizes and filtered vs unfiltered conditions"
395	      how_gain_highlighted: "Filtered curves decrease steadily; unfiltered curves increase (collapse). Separation grows over iterations."
396	      design_note: "Multiple colored lines with solid/dashed encoding. FID on y-axis with clear downward = better convention."
397	    - figure_id: "Figure 5b"
398	      viz_type: "line_plot"
399	      what_compared: "Effect of verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images) on FID over 40 iterations"
400	      how_gain_highlighted: "Clear monotonic relationship: more verifier training data = lower FID. 60K verifier achieves FID ~40; 500-image verifier plateaus at ~130."
401	      design_note: "Seven colored lines ordered by verifier quality create a clean gradient pattern. Demonstrates the paper's key insight that verification quality bounds final performance. Well-chosen range of verifier sizes."
402	  ablation_figures:
403	    - figure_id: "Figure 3"
404	      viz_type: "heatmap"
405	      dimensions_varied: ["Verifier bias (Delta)", "Verifier selectivity radius (r)"]
406	      design_note: "Effectively an ablation over the two key verifier hyperparameters. Heatmap format makes the full landscape visible at once rather than requiring multiple line plots."
407	    - figure_id: "Figure 5b"
408	      viz_type: "line_plot"
409	      dimensions_varied: ["Verifier training dataset size (quality proxy)"]
410	      design_note: "Ablation over verifier quality showing monotonic improvement. Seven conditions provide fine granularity."
411	  figure_narrative_role: "Figure 1 (teaser: visual proof of concept) -> Figure 2 (pipeline: method overview) -> Figure 3 (theory validation: one-round landscape) -> Figure 4 (long-term dynamics: convergence behavior) -> Figure 5 (real-world validation: VAE experiments). Progression from motivation to theory to practice."
412	
413	tables:
414	  table_count: 0
415	  main_result_table:
416	    table_id: "N/A"
417	    row_axis: "N/A"
418	    col_axis: "N/A"
419	    row_organization: "N/A"
420	    col_organization: "N/A"
421	    highlight_strategy: "N/A"
422	    statistical_reporting: "N/A"
423	    num_baselines: 0
424	    design_note: "Paper has no tables in main text. All results presented through figures (heatmaps and line plots). This is unusual but appropriate for a theory-focused paper where the key results are continuous landscapes and convergence dynamics rather than discrete benchmark comparisons."
425	  ablation_tables: []
426	  supplementary_tables:
427	    in_appendix: true
428	    content: "Appendix A: 1D Gaussian analysis toolkit. Appendix B: Full proofs of Theorems 3.1 and 4.1. Appendix C: VAE experiment details including data preprocessing, discriminator architecture specifications, synthetic generation procedures, and supplementary ELBO results."
429	    reason: "All heavy mathematical proofs and implementation details moved to appendix to keep main paper focused on the two theorems and their experimental validation. Consistent with theory-paper conventions."
430	
431	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b07dc4e5-6bd1-415a-a7a4-fd4d9b3b7765",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "6d331f61-9aaf-429b-a12e-95169a1d9a81",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/by4quedph.txt",
      "content": "=== li2024_mage.yaml ===\npaper_key: \"li2024_mage\"\ntitle: \"MAGE: Machine-generated Text Detection in the Wild\"\nvenue: \"ACL 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Longformer (PLM-based classifier)\"\n    - \"GLTR (GPT-2-XL + logistic regression)\"\n    - \"FastText (word bi-gram features)\"\n    - \"DetectGPT (zero-shot, T5-3B mask infill + GPT-J-6B scoring)\"\n    - \"Human annotators\"\n    - \"ChatGPT querying\"\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"AvgRec (average of HumanRec and MachineRec)\", direction: \"higher_better\"}\n    - {name: \"HumanRec (human text recall)\", direction: \"higher_better\"}\n    - {name: \"MachineRec (machine text recall)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"MAGE testbed (custom)\", size: \"95,596 human + 236,554 machine-generated texts from 7 domains x 27 LLMs\"}\n    - {name: \"Reddit ChangeMyView\", size: \"804 opinion statements\"}\n    - {name: \"Yelp\", size: \"1,000 reviews\"}\n    - {name: \"XSum\", size: \"1,000 news articles\"}\n    - {name: \"TLDR\", size: \"777 news summaries\"}\n    - {name: \"ELI5\", size: \"1,000 QA pairs\"}\n    - {name: \"Reddit WritingPrompts\", size: \"1,000 stories\"}\n    - {name: \"ROCStories\", size: \"1,000 stories\"}\n    - {name: \"HellaSwag\", size: \"1,000 commonsense reasoning\"}\n    - {name: \"SQuAD (Wikipedia)\", size: \"1,000 paragraphs\"}\n    - {name: \"SciXGen\", size: \"1,000 scientific abstracts\"}\n    - {name: \"CNN/DailyMail (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"DialogSum (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"PubMedQA (frontier test)\", size: \"used in Testbed 7\"}\n    - {name: \"IMDb (frontier test)\", size: \"used in Testbed 7\"}\n  ablation_dimensions:\n    - \"In-distribution vs out-of-distribution (8 testbed scenarios)\"\n    - \"Fixed-domain vs arbitrary-domain\"\n    - \"Model-specific vs arbitrary-model\"\n    - \"Unseen models (cross-validation over 7 model groups)\"\n    - \"Unseen domains (cross-validation over 10 domains)\"\n    - \"Decision boundary adjustment (0.1% in-domain data)\"\n    - \"Paraphrasing attack robustness (gpt-3.5-turbo)\"\n    - \"Prompt type (continuation vs topical vs specified)\"\n    - \"PLM backbone comparison\"\n    - \"Data balance effects\"\n    - \"Randomness analysis\"\n  training_recipe:\n    optimizer: \"Adam\"\n    lr: \"0.005\"\n    dropout: \"0.1\"\n    epochs: \"5\"\n    hardware: \"8x V100 GPUs\"\n    validation_metric: \"classification accuracy\"\n    gltr_lm: \"GPT-2-XL\"\n    gltr_classifier: \"logistic regression (scikit-learn, grid search)\"\n    fasttext_epochs: \"100\"\n    detectgpt_mask_model: \"T5-3B\"\n    detectgpt_scoring_model: \"GPT-J-6B\"\n    detectgpt_mask_rate: \"15%\"\n    detectgpt_perturbations: \"100\"\n  method_family: \"PLM-based binary classification (Longformer) + statistical/zero-shot baselines for machine-generated text detection\"\n\npositioning:\n  core_claim: \"First comprehensive 'in-the-wild' testbed for machine-generated text detection spanning 7 domains and 27 LLMs, revealing that perplexity is a double-edged sword — it enables clustering but causes systematic false positives on low-perplexity human text.\"\n  key_results: \"Longformer achieves AUROC 0.99 in-distribution but drops to 0.95 on unseen models and 0.93 on unseen domains; with 0.1% boundary adjustment data, achieves 86.54% AvgRec on unseen domains + unseen model (GPT-4); paraphrasing attacks degrade AUROC to 0.75.\"\n  limitations:\n    - \"Limited model coverage — new LLMs (Alpaca, Vicuna, etc.) continuously emerge and the testbed cannot keep up\"\n    - \"Benchmark data bias — source texts may overlap with LLM pretraining data, so detection performance may not transfer to truly novel online text\"\n    - \"Vulnerability to paraphrasing attacks (AvgRec drops to 62.92% even with boundary adjustment)\"\n    - \"Perplexity bias causes systematic misclassification of low-perplexity human texts as machine-generated\"\n  relation_to_us: \"competitor\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"LLMs have achieved human-level text generation, creating urgent need for detection — but existing detection research only evaluates on specific domains or specific models, leaving open how detectors perform 'in the wild'.\"\n  tension: \"Prior work assumes controlled settings (known domain, known generator). In reality, detectors face texts from unknown LLMs across diverse domains. The paper asks: can detection still work when we don't know the source?\"\n  key_insight: \"Perplexity is a double-edged sword — it is the fundamental feature separating human and machine text (machine text has lower perplexity), but detectors over-rely on it, systematically misclassifying low-perplexity human text. Diverse domains and models cause human-machine linguistic differences to converge, making detection harder.\"\n  argument_chain: \"problem (detection in controlled settings ≠ detection in the wild) → testbed construction (7 domains × 27 LLMs × 3 prompt types) → 8 progressive evaluation scenarios (in-distribution → OOD) → empirical finding (performance degrades with diversity, especially OOD) → analysis (linguistic convergence + perplexity bias) → mitigation (boundary adjustment with 0.1% data) → feasibility demonstration (86.54% on GPT-4 unseen domain)\"\n  contribution_framing: \"Three contributions: (1) comprehensive testbed with texts from diverse human writings and LLMs, (2) empirical analysis revealing diminishing linguistic differences in open-domain settings, (3) discovery that perplexity serves as fundamental but biased clustering feature. Framed as 'first' comprehensive wild-scenario evaluation.\"\n  intro_structure: \"~5 paragraphs: (1) LLMs generate human-level text → detection needed, (2) existing work limited to specific domains/models, (3) two research questions about wild detection, (4) testbed construction description, (5) key findings and contributions.\"\n  notable_technique: \"Progressive difficulty design — 8 testbeds arranged from easiest (white-box, single domain, single model) to hardest (unseen domain + unseen model + paraphrasing attack), creating a compelling narrative arc that systematically reveals when and why detection fails.\"\n\nfigures:\n  figure_count: 15\n  figure1:\n    type: \"problem_illustration\"\n    description: \"Left side shows diverse input domains (News Title, Story Title, Question, Argument, Scientific Topic) as colored cards with arrows pointing to both Humans (stick figure at desk) and multiple LLMs (GPT-3.5, FLAN-T5, LLaMA, OPT, GLM, ...) listed vertically. The many-to-many arrows from domains to generators show the combinatorial explosion. Right side shows a 'Text' box passing through a magnifying glass 'Detector' with a question mark, leading to two possible outputs: 'Human' (messy scribble icon) and 'Machine' (clean stick figure). The layout flows left-to-right: sources → generators → mixed text → detection challenge.\"\n    narrative_role: \"Establishes the core challenge — detection must handle the combinatorial space of domains × generators, not just one domain or one model.\"\n    design_elements: [\"colored domain cards (purple/orange/green)\", \"many-to-many arrows showing combinatorial complexity\", \"magnifying glass as detector metaphor\", \"question mark conveying uncertainty\", \"stick figure icons for human vs machine\"]\n    visual_style: \"Clean line-art style with selective color on domain cards (purple, orange, green pastels). Horizontal left-to-right flow. Minimal decorative elements. Black-and-white for the detection side. Simple but effective at conveying the many-to-many challenge.\"\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"grouped_bar_or_line\"\n      what_compared: \"OOD detection performance on unseen models, broken down by model family and prompt type\"\n      how_gain_highlighted: \"Shows which model families are hardest to detect (OpenAI, FLAN-T5) and which prompt types are most challenging (specified prompts)\"\n      design_note: \"Separates analysis by two dimensions (model family × prompt type) to give nuanced OOD understanding rather than single aggregate number\"\n    - figure_id: \"Figure 3\"\n      viz_type: \"bar_chart_or_line\"\n      what_compared: \"Detection performance (AvgRec) on unseen domains, identifying ROC, XSum, TLDR as hardest\"\n      how_gain_highlighted: \"Links difficulty to domain perplexity characteristics\"\n      design_note: \"Per-domain breakdown reveals systematic pattern (low-perplexity domains harder) rather than just reporting aggregate OOD performance\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"precision_recall_curve + bar_chart\"\n      what_compared: \"(a) PR curves before/after boundary adjustment, (b) performance improvement with 0.1% in-domain data\"\n      how_gain_highlighted: \"Direct before/after comparison shows dramatic improvement from minimal adaptation\"\n      design_note: \"Two-panel figure pairs theoretical (PR curve) with practical (data requirement) perspectives\"\n  ablation_figures:\n    - figure_id: \"Figure 5\"\n      viz_type: \"heatmap\"\n      dimensions_varied: [\"domain diversity\", \"model diversity\"]\n      design_note: \"Jensen-Shannon distance heatmap showing linguistic convergence as diversity increases — visual proof that the detection problem gets fundamentally harder with diversity\"\n    - figure_id: \"Figure 6\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"named entity types (ORDINAL, DATE, etc.)\"]\n      design_note: \"Shows entity distribution differences in fixed-domain setting as detection shortcuts that disappear with diversity\"\n    - figure_id: \"Figures 7-9\"\n      viz_type: \"histogram + scatter\"\n      dimensions_varied: [\"perplexity distributions\", \"prediction correctness\", \"paraphrasing effects\"]\n      design_note: \"Three-figure sequence builds the 'perplexity as double-edged sword' argument: (7) machine < human perplexity, (8) misclassified human texts have low perplexity, (9) paraphrasing shifts distributions\"\n  figure_narrative_role: \"Figure 1 (problem illustration) → Figures 2-3 (OOD performance breakdown by model/domain) → Figure 4 (boundary adjustment solution) → Figures 5-6 (linguistic convergence analysis) → Figures 7-9 (perplexity analysis arc) → Figures 10-15 (appendix: prompts, data distributions, linguistic stats). The main paper figures follow a 'problem → results → analysis → mitigation' narrative arc.\"\n\ntables:\n  table_count: 12\n  main_result_table:\n    table_id: \"Table 3\"\n    row_axis: \"methods (Longformer, FastText, GLTR, DetectGPT)\"\n    col_axis: \"testbed scenarios (Testbed 2-6) × metrics (AUROC, AvgRec, HumanRec, MachineRec)\"\n    row_organization: \"flat\"\n    col_organization: \"grouped_by_testbed\"\n    highlight_strategy: \"best results in bold across methods per testbed\"\n    statistical_reporting: \"single run numbers (no std reported for main results)\"\n    num_baselines: 4\n    design_note: \"Comprehensive table spanning both in-distribution (Testbeds 2-4) and out-of-distribution (Testbeds 5-6) in one view, enabling direct comparison of how each method degrades from ID to OOD. Progressive difficulty across columns tells the degradation story.\"\n  ablation_tables:\n    - table_id: \"Table 2\"\n      what_varied: [\"white-box detection (Testbed 1) — easiest setting as reference point\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Separated from main table to establish performance ceiling before showing degradation\"\n    - table_id: \"Table 4\"\n      what_varied: [\"decision boundary adjustment effect on Testbeds 5-6\"]\n      variation_style: \"full_numbers (before vs after adjustment)\"\n      design_note: \"Shows boundary adjustment dramatically improves domain-shift performance (AvgRec 68.40→81.78 for unseen domains)\"\n    - table_id: \"Table 5\"\n      what_varied: [\"challenging frontier tests (Testbed 7: unseen domain+model with GPT-4, Testbed 8: paraphrasing attack)\"]\n      variation_style: \"full_numbers with before/after boundary adjustment\"\n      design_note: \"Most challenging scenarios isolated in separate table — clean before/after comparison for the proposed mitigation\"\n    - table_id: \"Table 1\"\n      what_varied: [\"naive baselines (ChatGPT querying, human annotators)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Establishes that even humans (~54.5% AvgRec) and ChatGPT (~54.5% AvgRec) struggle at wild detection, motivating the need for dedicated methods\"\n    - table_id: \"Tables 8-10\"\n      what_varied: [\"randomness analysis\", \"PLM backbone comparison\", \"data balance effects\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Robustness checks in appendix ensure main findings are not artifacts of specific choices\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 6 (dataset statistics per domain), Table 7 (naive baseline test set composition), Tables 8-10 (robustness: randomness/backbone/balance), Table 11 (all methods on challenging test sets), Table 12 (length statistics)\"\n    reason: \"Main paper focuses on the progressive testbed story (Tables 1-5). Appendix holds dataset details and robustness checks that support but don't drive the narrative.\"\n\n=== mohamed2025_broken_telephone.yaml ===\npaper_key: \"mohamed2025_broken_telephone\"\ntitle: \"LLM as a Broken Telephone: Iterative Generation Distorts Information\"\nvenue: \"ACL 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"single-pass generation\", \"various prompting strategies\"]\n  metrics:\n    - {name: \"information distortion rate\", direction: \"lower_better\"}\n    - {name: \"semantic similarity to original\", direction: \"higher_better\"}\n    - {name: \"factual accuracy degradation\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"translation chain experiments\", size: \"N/A\"}\n  ablation_dimensions: [\"number of iterative generations\", \"language choice\", \"chain complexity\", \"prompting strategy\"]\n  training_recipe: {optimizer: \"N/A (inference only)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"empirical analysis of iterative LLM generation degradation\"\n\npositioning:\n  core_claim: \"LLMs systematically distort information when outputs are repeatedly processed, with distortion accumulating over iterations analogous to the broken telephone effect\"\n  key_results: \"Degradation is inevitable but mitigable through strategic prompting; language and chain complexity influence distortion rate\"\n  limitations: [\"primarily translation-based experiments\", \"limited model coverage\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== dohmatob2024_tale_of_tails.yaml ===\npaper_key: \"dohmatob2024_tale_of_tails\"\ntitle: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\nvenue: \"ICML 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Original (human/natural) data training\"\n    - \"Pure synthetic data training\"\n    - \"Mixed real+synthetic data training\"\n    - \"Hutter LLM (deterministic lookup table)\"\n    - \"Hutter++ (probabilistic bigram)\"\n    - \"Capacity-limited associative memory\"\n  metrics:\n    - {name: \"test error (scaling law exponent)\", direction: \"lower_better\"}\n    - {name: \"perplexity\", direction: \"lower_better\"}\n    - {name: \"number of skills learned (GCD answers)\", direction: \"higher_better\"}\n    - {name: \"total variation distance\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Wikitext-103\", size: \"~2M samples for fine-tuning\"}\n    - {name: \"GCD arithmetic task (Zipfian)\", size: \"300K-300M samples\"}\n    - {name: \"Synthetic bigram distributions\", size: \"variable\"}\n  ablation_dimensions:\n    - \"tail cutoff rank k (top-p/top-k truncation)\"\n    - \"tail exponent narrowing beta_prime vs beta (temperature scaling)\"\n    - \"number of recursive generations n\"\n    - \"mixing proportion pi of real vs synthetic data\"\n    - \"model capacity / embedding dimension d\"\n    - \"Zipf exponent beta\"\n    - \"training set size T\"\n  training_recipe:\n    optimizer: \"not explicitly specified in main text\"\n    lr: \"not explicitly specified in main text\"\n    hardware: \"not explicitly specified\"\n    details: \"GCD transformer trained on up to 300M samples; Llama2-7B fine-tuned on Wikitext-103 ~2M samples; synthetic data generated with various top-p and temperature settings\"\n  method_family: \"theoretical analysis of model collapse via scaling laws and tail distributions\"\n\npositioning:\n  core_claim: \"Model collapse is fundamentally a change of scaling laws caused by synthetic data losing the heavy-tailed structure of natural distributions, leading to quantifiable and predictable degradation patterns including plateau effects, skill loss, and shifted scaling exponents.\"\n  key_results: \"Double scaling law E_test ~ T^(-(beta-1)/beta) + k^(-(beta-1)) predicts performance plateau on synthetic data; multi-generation collapse shows additive degradation E_test ~ T^(-c) + n*T0^(-c); grokking phenomenon when mixing pi-fraction real data creates plateau of length ~k^beta/pi before recovery; triplet scaling law E_test ~ T^(-(1-1/beta)) + d^(-c_q) + k^(-(beta-1)) for capacity-limited models\"\n  limitations:\n    - \"Theory assumes simplified models (Zipfian distributions, deterministic labels for some results)\"\n    - \"Grokking theorem strictly holds only for deterministic ground-truth labels; probabilistic settings show attenuated S-shaped curves\"\n    - \"Real LLMs involve complex conditional distributions not fully captured by the theoretical framework\"\n    - \"Bigram and Hutter models are simplified abstractions of actual language model behavior\"\n    - \"No experiments on larger-scale models beyond Llama2-7B\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the observation that AI model scaling laws have been a key predictive tool, but the ecosystem of online data is co-evolving to contain increasing amounts of synthetic data - asking whether future models will still improve or be 'doomed to degenerate up to total collapse'. Uses the striking statistic that ChatGPT contributes 0.1% of total words generated daily by the global population.\"\n  tension: \"Existing scaling law theory assumes training on natural (heavy-tailed) data distributions, but the inevitable contamination of training corpora with synthetic data fundamentally breaks these assumptions. Prior work on model collapse identified the phenomenon but lacked a theoretical framework connecting it to scaling laws and emergent abilities.\"\n  key_insight: \"The key insight is that heavy-tailed (Zipfian) distributions are what enable power-law scaling, and AI generation mechanisms (top-p sampling, temperature scaling, finite sampling) systematically destroy these tails through three mechanisms: tail cutting, tail narrowing, and finite sampling bias. This directly links distributional properties to scaling law behavior.\"\n  argument_chain: \"problem (synthetic data contamination is inevitable) -> observation (scaling laws depend on heavy-tailed distributions) -> mechanism (AI generation cuts/narrows tails via top-p, temperature, finite sampling) -> theory (double/triplet scaling laws predict plateau and degradation) -> multi-generation analysis (collapse compounds across iterations) -> mitigation (data mixing enables grokking recovery) -> experiments (GCD transformer + Llama2-7B validate predictions)\"\n  contribution_framing: \"Four numbered contributions introduced with 'Our main findings are as follows': (1) Double Scaling Law, (2) Triplet Scaling Law for Memory-Limited Models, (3) Model Collapse over Multiple Generations, (4) Mitigation Strategies. Explicitly claims to be 'the first to theoretically and empirically analyze model collapse in the context of scaling laws and emergent abilities'.\"\n  intro_structure: \"5 paragraphs: P1=hook (scaling laws + synthetic data problem), P2=background (neural scaling laws and heavy tails), P3=problem statement (model collapse concern), P4=key insight (tail mechanisms), P5=contribution list (4 numbered findings)\"\n  notable_technique: \"The 'tale of tails' metaphor is the central narrative device - it reframes the abstract concept of model collapse into a concrete, visual story about distribution tails. The three tail destruction mechanisms (cutting, narrowing, finite sampling) provide a clean taxonomy that makes complex theory intuitive. The paper also effectively uses the GCD arithmetic task as a controlled 'microscope' for studying skill emergence and loss, before scaling up to Llama2.\"\n\nfigures:\n  figure_count: 5  # main text; ~35 total including appendices\n  figure1:\n    type: \"motivation\"\n    description: \"Illustrates the three mechanisms by which AI generation destroys distribution tails: top-p nucleus sampling (tail cutting), temperature scaling with tau>1 (tail narrowing), and finite sample bias. Shows how these mechanisms affect a Zipfian frequency distribution and connects to skill loss using GCD calculation (answers 2 and 3) as concrete examples.\"\n    narrative_role: \"Establishes the paper's core conceptual framework - visually demonstrates WHY model collapse happens by showing the mechanistic link between generation procedures and tail destruction. This is the key figure that makes the abstract theory tangible.\"\n    design_elements: [\"distribution curves with shaded truncation regions\", \"before/after comparison of tails\", \"concrete skill examples (GCD answers)\", \"three-panel layout for three mechanisms\"]\n    visual_style: \"Clean schematic diagrams with distribution curves; uses color to distinguish original vs truncated/narrowed distributions; combines mathematical distributions with concrete task examples\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Three panels illustrating main theoretical results: (Left) Double scaling law with Zipf exponent beta=3/2 showing plateau effect; (Middle) Model collapse across 5 generations showing progressive degradation; (Right) Grokking behavior showing plateau length and asymptotic recovery predictions\"\n      how_gain_highlighted: \"Theoretical predictions shown as dashed lines overlaid on empirical curves; clear separation between original data scaling (power law) and synthetic data scaling (plateau)\"\n      design_note: \"Three-panel layout maps directly to three main theorems; log-log scale makes power-law relationships linear; uses generation number as a visual variable to show progressive collapse\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Three experimental validation panels: (Left) Llama2-7B perplexity scaling on Wikitext-103 across generations; (Middle) GCD transformer scaling on original vs synthetic data; (Right) Skills (GCD answers) learned on clean vs AI-generated data\"\n      how_gain_highlighted: \"Direct visual comparison of original vs synthetic data curves; skill emergence on clean data vs skill loss on synthetic data is strikingly clear\"\n      design_note: \"Mirrors the layout of Figure 3 (theory) to enable direct theory-vs-experiment comparison; this structural parallelism strengthens the validation narrative\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"line_plot\"\n      what_compared: \"Effect of mixing real data (T_real) with AI data (T_AI) - shows performance improvement up to saturation point with k=1000 and beta=3/2\"\n      how_gain_highlighted: \"Shows the grokking transition clearly - performance plateaus then recovers as real data fraction increases\"\n      design_note: \"Single focused plot isolates the mixing mitigation result; parameters annotated directly on figure\"\n  ablation_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"combined_distribution_and_perplexity\"\n      dimensions_varied: [\"data source (original vs AI-generated)\", \"generation parameters (top-p, temperature)\"]\n      design_note: \"Two-part figure combines perplexity diagram (top) with distribution comparison (bottom); effectively demonstrates that the theoretical tail-cutting/narrowing mechanisms manifest in real LLM outputs\"\n  figure_narrative_role: \"Figure 1 (motivation: why tails matter) -> Figure 2 (empirical evidence: tails ARE destroyed in practice) -> Figure 3 (theory: predicted consequences) -> Figure 4 (validation: experiments match theory) -> Figure 5 (mitigation: data mixing helps). Clean motivation-theory-validation-solution arc.\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    note: \"This paper has NO tables. All results are presented through mathematical theorems and figures with scaling curves. This is consistent with theoretical ML papers where the primary contributions are equations/bounds rather than benchmark comparisons.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: false\n    content: \"No tables in appendix either; appendices contain proofs (Appendices C-F), additional figures (Appendix B), and experimental details (Appendices G-H)\"\n    reason: \"The paper is primarily theoretical - results are best expressed as scaling law equations and their visual verification, not tabular comparisons. The continuous nature of scaling curves makes line plots the natural presentation format.\"\n\n=== finlayson2024_closing.yaml ===\npaper_key: \"finlayson2024_closing\"\ntitle: \"Closing the Curious Case of Neural Text Degeneration\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"nucleus sampling (top-p)\", \"top-k sampling\", \"greedy decoding\", \"threshold-based truncation methods\"]\n  metrics:\n    - {name: \"text quality (human eval)\", direction: \"higher_better\"}\n    - {name: \"text quality (automatic)\", direction: \"higher_better\"}\n    - {name: \"degeneration rate\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"open-ended text generation benchmarks\", size: \"N/A\"}\n  ablation_dimensions: [\"truncation threshold\", \"entropy regime\", \"model size\"]\n  training_recipe: {optimizer: \"N/A (decoding strategy)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"truncation sampling / decoding strategy analysis\"\n\npositioning:\n  core_claim: \"The softmax bottleneck causes models to assign nonzero probability to impossible tokens; truncation sampling works by removing these, and a principled approach without arbitrary thresholds is possible\"\n  key_results: \"Theoretical proof that threshold-free truncation using softmax bottleneck properties guarantees valid token sampling\"\n  limitations: [\"focused on open-ended generation\", \"theoretical assumptions about softmax bottleneck\"]\n  relation_to_us: \"orthogonal\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== yi2026_escaping_collapse.yaml ===\npaper_key: \"yi2026_escaping_collapse\"\ntitle: \"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\"\nvenue: \"ICLR 2026 (Poster)\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Unfiltered synthetic retraining (no verifier)\"\n    - \"Real-data-only OLS estimator\"\n    - \"VAE trained on full 60K MNIST (upper bound)\"\n  metrics:\n    - {name: \"MSE (parameter estimation error)\", direction: \"lower_better\"}\n    - {name: \"FID (Frechet Inception Distance)\", direction: \"lower_better\"}\n    - {name: \"ELBO (Evidence Lower Bound)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Simulated linear regression\", size: \"dimension p=8, varying sample sizes (500->2000, 1000->4000, 2000->8000)\"}\n    - {name: \"MNIST\", size: \"500 real images for init, 60K for discriminator training\"}\n  ablation_dimensions:\n    - \"Verifier bias (Delta: 0.0-0.7)\"\n    - \"Verifier selectivity/radius (r: 0.05-0.5 for linear; top-10% for VAE)\"\n    - \"Training sample size schedule (real->synthetic ratio)\"\n    - \"Verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images)\"\n    - \"Filtered vs unfiltered synthetic data\"\n  training_recipe:\n    optimizer: \"OLS (closed-form) for linear regression; standard SGD for CVAE\"\n    lr: \"N/A for OLS; not specified for VAE\"\n    hardware: \"Not specified\"\n    iterations: \"60 rounds for linear regression; 40 rounds for VAE\"\n  method_family: \"Verifier-guided synthetic data filtering for iterative model retraining\"\n\npositioning:\n  core_claim: \"External verifier-based filtering of synthetic data prevents model collapse in the short term via bias-variance tradeoff, but long-term performance converges to the verifier's knowledge center rather than ground truth -- unless the verifier is perfectly unbiased.\"\n  key_results: \"Linear regression: filtered retraining keeps MSE near 0.05 across 60 iterations while unfiltered diverges to 0.3-0.8. VAE/MNIST: FID drops from ~110 to ~40 with 60K-trained verifier over 40 iterations; with only 500-image verifier, FID plateaus at ~130.\"\n  limitations:\n    - \"Theoretical analysis restricted to linear regression; generalization to neural networks remains open\"\n    - \"VAE verifier (discriminator) is relatively simple and may reject harder-to-generate modes\"\n    - \"Synthetic retraining initialized with only 500 real images limits diversity recovery\"\n    - \"Verifier quality directly bounds long-term performance ceiling -- biased verifier leads to biased convergence\"\n    - \"No experiments on large language models or more complex generative tasks\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Synthetic data is increasingly used to train frontier generative models, but iterative retraining on self-generated data causes model collapse -- a well-documented performance degradation phenomenon.\"\n  tension: \"Prior work establishes collapse as seemingly inevitable under recursive self-training, but real practitioners already use external verification (human feedback, reward models). The question is: can verification provably escape collapse, and if so, what are the limits?\"\n  key_insight: \"Verification creates a bias-variance tradeoff: filtering reduces variance (by discarding low-quality samples) but introduces bias (toward the verifier's knowledge center). Short-term gains are real but long-term convergence is to the verifier's center, not ground truth. Presented through Theorem 3.1 (one-round decomposition) and Theorem 4.1 (long-term contraction).\"\n  argument_chain: \"model collapse problem -> prior work shows unfiltered retraining diverges -> introduce verifier-based filtering framework (Generate-Verify-Retrain) -> theoretical analysis: one-round improvement via bias-variance decomposition (Theorem 3.1) -> long-term convergence to verifier center (Theorem 4.1) -> empirical validation on linear regression + VAE/MNIST -> conclusion: verification helps but is fundamentally bounded by verifier quality\"\n  contribution_framing: \"Three research questions framed as Q1 (does verification help short-term?), Q2 (do gains sustain long-term?), Q3 (empirical validation). Each answered with a theorem or experiment. Contribution count: 3 clearly delineated.\"\n  intro_structure: \"4 paragraphs: (1) motivation on synthetic data and model collapse concern, (2) research questions about verifier-based filtering, (3) prior literature context and gaps, (4) bullet-point contributions with theorem references\"\n  notable_technique: \"Framing the two results as a deliberate tension -- short-term improvement (good news) vs long-term convergence to verifier center (cautionary news) -- creates a 'promise and peril' narrative arc that is more nuanced than a pure positive-result paper.\"\n\nfigures:\n  figure_count: 5\n  figure1:\n    type: \"teaser_result\"\n    description: \"Three-panel comparison showing VAE-generated MNIST digits: (left) original data, (center-top) with verified synthetic data after 40 rounds showing maintained quality, (center-bottom) without verification showing severe collapse/degradation. (right) upper bound from training on all 60K real images.\"\n    narrative_role: \"Immediately demonstrates the paper's core claim visually -- verification prevents collapse while unfiltered retraining produces unrecognizable outputs. Placed before any theory to motivate the reader.\"\n    design_elements: [\"Before/after comparison\", \"With/without verification contrast\", \"Real sample grids\", \"Upper bound reference\", \"Arrow annotations connecting panels\"]\n    visual_style: \"Black background with white MNIST digit grids arranged horizontally. Arrows with text labels ('With Data Verification' / 'Without Data Verification') connect the initial model to the two outcomes. Clean, high-contrast layout. Roughly 4-panel horizontal arrangement.\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"heatmap + heatmap\"\n      what_compared: \"One-round improvement landscape as function of verifier bias (Delta) and selectivity radius (r). Left (3a): theory-predicted loss landscape. Right (3b): empirical simulation.\"\n      how_gain_highlighted: \"Green regions indicate improvement (log ratio > 0), red regions indicate degradation. Theory-empirical match validates the theoretical framework.\"\n      design_note: \"Diverging green-red colormap centered at 0 makes improvement/degradation regions immediately readable. Side-by-side theory vs empirical layout validates theoretical predictions visually. Axes are interpretable parameters (bias, radius).\"\n    - figure_id: \"Figure 4a\"\n      viz_type: \"line_plot\"\n      what_compared: \"Convergence of parameter estimate to verifier center (theta_c) over 60 iterations for different verifier radii (r=0.1, 0.5, 1, 1.5) with biased verifier\"\n      how_gain_highlighted: \"All curves converge to near-zero distance from theta_c, confirming Theorem 4.1. Smaller radius = faster convergence.\"\n      design_note: \"Clean line plot with distinct colors for each radius value. Y-axis is distance to verifier center, clearly showing contraction. Legend is simple and readable.\"\n    - figure_id: \"Figure 4b\"\n      viz_type: \"line_plot\"\n      what_compared: \"Filtered (solid) vs unfiltered (dashed) retraining across different sample size schedules (500->2000, 1000->4000, 2000->8000) over 60 iterations with unbiased verifier\"\n      how_gain_highlighted: \"Solid lines (filtered) stay flat near 0.05 while dashed lines (unfiltered) diverge upward to 0.3-0.8. Dramatic visual separation between the two groups.\"\n      design_note: \"Solid vs dashed line encoding for filtered/unfiltered is effective. Three colors for three sample size conditions. The divergence of dashed lines visually dramatizes model collapse.\"\n    - figure_id: \"Figure 5a\"\n      viz_type: \"line_plot\"\n      what_compared: \"VAE FID scores over 40 iterations comparing different VAE training sample sizes and filtered vs unfiltered conditions\"\n      how_gain_highlighted: \"Filtered curves decrease steadily; unfiltered curves increase (collapse). Separation grows over iterations.\"\n      design_note: \"Multiple colored lines with solid/dashed encoding. FID on y-axis with clear downward = better convention.\"\n    - figure_id: \"Figure 5b\"\n      viz_type: \"line_plot\"\n      what_compared: \"Effect of verifier quality (discriminator trained on 500/1K/5K/10K/20K/40K/60K real images) on FID over 40 iterations\"\n      how_gain_highlighted: \"Clear monotonic relationship: more verifier training data = lower FID. 60K verifier achieves FID ~40; 500-image verifier plateaus at ~130.\"\n      design_note: \"Seven colored lines ordered by verifier quality create a clean gradient pattern. Demonstrates the paper's key insight that verification quality bounds final performance. Well-chosen range of verifier sizes.\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"heatmap\"\n      dimensions_varied: [\"Verifier bias (Delta)\", \"Verifier selectivity radius (r)\"]\n      design_note: \"Effectively an ablation over the two key verifier hyperparameters. Heatmap format makes the full landscape visible at once rather than requiring multiple line plots.\"\n    - figure_id: \"Figure 5b\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"Verifier training dataset size (quality proxy)\"]\n      design_note: \"Ablation over verifier quality showing monotonic improvement. Seven conditions provide fine granularity.\"\n  figure_narrative_role: \"Figure 1 (teaser: visual proof of concept) -> Figure 2 (pipeline: method overview) -> Figure 3 (theory validation: one-round landscape) -> Figure 4 (long-term dynamics: convergence behavior) -> Figure 5 (real-world validation: VAE experiments). Progression from motivation to theory to practice.\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    table_id: \"N/A\"\n    row_axis: \"N/A\"\n    col_axis: \"N/A\"\n    row_organization: \"N/A\"\n    col_organization: \"N/A\"\n    highlight_strategy: \"N/A\"\n    statistical_reporting: \"N/A\"\n    num_baselines: 0\n    design_note: \"Paper has no tables in main text. All results presented through figures (heatmaps and line plots). This is unusual but appropriate for a theory-focused paper where the key results are continuous landscapes and convergence dynamics rather than discrete benchmark comparisons.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Appendix A: 1D Gaussian analysis toolkit. Appendix B: Full proofs of Theorems 3.1 and 4.1. Appendix C: VAE experiment details including data preprocessing, discriminator architecture specifications, synthetic generation procedures, and supplementary ELBO results.\"\n    reason: \"All heavy mathematical proofs and implementation details moved to appendix to keep main paper focused on the two theorems and their experimental validation. Consistent with theory-paper conventions.\"\n\n",
      "numLines": 432,
      "startLine": 0,
      "totalLines": 432
    }
  },
  "sourceToolAssistantUUID": "b07dc4e5-6bd1-415a-a7a4-fd4d9b3b7765",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "6d331f61-9aaf-429b-a12e-95169a1d9a81",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Tool call

_source line 41 · 2026-05-21T15:05:37.886Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01K4AbQ52LDrSxFNHXYdszBy`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp && for f in binoculars2024.yaml fast_detectgpt2024.yaml diveye2026.yaml verma2024_ghostbuster.yaml penedo2024_fineweb.yaml; do echo \"=== $f ===\"; cat \"$f\"; echo; done",
  "description": "Read batch 3 of YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d331f61-9aaf-429b-a12e-95169a1d9a81",
  "isSidechain": false,
  "requestId": "req_011CbFvMEeZUBcXfonDBTEzv",
  "type": "assistant",
  "uuid": "820febfd-f3af-4a81-a6ac-f5194b8d611f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ch5uRKFZjqoVWEJYL5jiXM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11060,
      "cache_read_input_tokens": 38672,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 38672,
          "cache_creation_input_tokens": 11060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11060
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

_source line 42 · 2026-05-21T15:05:37.959Z_

<details><summary>↩ Tool result · `toolu_01K4AbQ52LDrSxFNHXYdszBy`</summary>

```text
=== binoculars2024.yaml ===
paper_key: "binoculars2024"
title: "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["DetectGPT", "Fast-DetectGPT", "likelihood thresholding", "supervised classifiers"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "TPR@1%FPR", direction: "higher_better"}
    - {name: "TPR@0.01%FPR", direction: "higher_better"}
  datasets:
    - {name: "multi-domain text corpus (news, wiki, creative)", size: "N/A"}
    - {name: "ChatGPT-generated samples", size: "N/A"}
  ablation_dimensions: ["LLM pair choice", "document type", "source model"]
  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
  method_family: "zero-shot detection via contrastive LLM scoring"

positioning:
  core_claim: "A simple score contrasting two closely related LLMs achieves SOTA zero-shot detection without any training data, detecting >90% of generated text at 0.01% FPR"
  key_results: ">90% detection of ChatGPT at 0.01% FPR; generalizes across LLMs without model-specific tuning"
  limitations: ["requires two LLMs at inference", "performance depends on LLM pair choice"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== fast_detectgpt2024.yaml ===
paper_key: "fast_detectgpt2024"
title: "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature"
venue: "ICLR 2024"
full_text_available: false

research:
  baselines: ["DetectGPT", "likelihood ratio", "rank-based methods", "supervised detectors"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "detection speed", direction: "higher_better"}
  datasets:
    - {name: "XSum", size: "N/A"}
    - {name: "SQuAD", size: "N/A"}
    - {name: "WritingPrompts", size: "N/A"}
  ablation_dimensions: ["source model", "scoring model", "perturbation vs sampling"]
  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
  method_family: "zero-shot detection via conditional probability curvature"

positioning:
  core_claim: "Replacing DetectGPT's perturbation step with conditional probability sampling achieves 340x speedup with ~75% relative improvement in both white-box and black-box settings"
  key_results: "340x faster than DetectGPT; 75% relative improvement; 80% ChatGPT detection at 1% FPR"
  limitations: ["still requires model access for scoring", "performance varies by domain"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== diveye2026.yaml ===
paper_key: "diveye2026"
title: "DivEye: Diversity Boosts AI-Generated Text Detection"
venue: "TMLR 2026"
full_text_available: false

research:
  baselines: ["DetectGPT", "Fast-DetectGPT", "Binoculars", "supervised fine-tuned classifiers"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "detection accuracy", direction: "higher_better"}
  datasets:
    - {name: "multi-domain benchmarks", size: "N/A"}
  ablation_dimensions: ["statistical features", "auxiliary signal integration", "paraphrasing robustness", "cross-domain transfer"]
  training_recipe: {optimizer: "N/A (zero-shot statistical)", lr: "N/A", hardware: "N/A"}
  method_family: "statistical feature-based detection using surprisal diversity"

positioning:
  core_claim: "Human text exhibits richer variability in lexical and structural unpredictability (surprisal diversity) than LLM outputs, and this signal is interpretable, robust, and complements existing detectors"
  key_results: "Outperforms zero-shot detectors by up to 33.2%; improves existing detectors by up to 18.7% as auxiliary signal; robust to paraphrasing attacks"
  limitations: ["statistical features may not capture all AI text patterns", "performance on very short texts unclear"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== verma2024_ghostbuster.yaml ===
paper_key: "verma2024_ghostbuster"
title: "Ghostbuster: Detecting Text Ghostwritten by Large Language Models"
venue: "NAACL 2024"
full_text_available: true

research:
  baselines:
    - "Perplexity-only (GPT-3 davinci perplexity threshold)"
    - "DetectGPT (Mitchell et al. 2023, unsupervised perturbation-based)"
    - "GPTZero (commercial detector)"
    - "RoBERTa fine-tuned (supervised neural baseline)"
    - "Human evaluation (17 participants)"
  metrics:
    - {name: "F1", direction: "higher_better"}
    - {name: "Accuracy", direction: "higher_better"}
    - {name: "Precision", direction: "higher_better"}
  datasets:
    - {name: "IvyPanda Student Essays", size: "7,000 docs (1K human + 1K ChatGPT same-prompt + 4K ChatGPT generalization)"}
    - {name: "Reuters 50-50 News Articles", size: "7,000 docs (same split structure)"}
    - {name: "r/WritingPrompts Creative Writing", size: "7,000 docs (same split structure)"}
    - {name: "Lang-8 non-native English", size: "evaluation only"}
    - {name: "TOEFL 11 (essay subset)", size: "evaluation only"}
    - {name: "TOEFL 91 (essay subset)", size: "evaluation only"}
  ablation_dimensions:
    - "Feature search depth (1, 2, 3, 4)"
    - "Model components (with/without ada, davinci, handcrafted features)"
    - "Random features vs selected features"
    - "Document length (10-1000 tokens)"
    - "Perturbation robustness (character/word/sentence/paragraph level)"
    - "Cross-domain generalization (in-domain vs out-of-domain)"
    - "Cross-model generalization (ChatGPT vs Claude)"
    - "Cross-prompt generalization (5 prompt variants)"
  training_recipe:
    classifier: "Logistic regression with L2 regularization, C=1"
    optimizer: "N/A (closed-form or standard sklearn solver)"
    lr: "N/A"
    hardware: "Not specified"
    feature_generation: "Recursive composition of vector/scalar functions up to depth 3, yielding 2534 candidate features"
    feature_selection: "Forward feature selection on validation set"
    weaker_models: "Unigram fertility, Kneser-Ney trigram, GPT-3 ada, GPT-3 davinci"
  method_family: "Feature-engineered classifier using proxy model probabilities"

positioning:
  core_claim: "A structured search over compositions of weaker language model probabilities, combined with a simple linear classifier, can robustly detect AI-generated text without access to the target model's token probabilities."
  key_results: "99.0 F1 in-domain across all domains (+0.9 over RoBERTa, +5.9 over GPTZero); 97.0 F1 out-of-domain average (vs 85.1 RoBERTa); 92.2 F1 on Claude generalization; 99.5 F1 across prompt variants"
  limitations:
    - "Poor performance on documents under 100 tokens (F1 drops below 80 at 25 tokens)"
    - "Lower accuracy on non-native English speaker text (TOEFL 91: 74.7% accuracy, below GPTZero 92.3% and RoBERTa 96.7%)"
    - "Datasets limited to British/American English, not representative of all writing styles"
    - "Vulnerable to paraphrasing attacks (Undetectable.ai reduces recall from 99% to 62%)"
    - "Relies on API access to GPT-3 ada/davinci which may be deprecated"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Opens with the societal impact of ChatGPT's fluent text generation — schools restricting ChatGPT, authenticity concerns across education and journalism — establishing real-world urgency."
  tension: "Existing detectors (DetectGPT, GPTZero) show poor generalization across domains and models; supervised neural methods (RoBERTa) overfit to training distribution; zero-shot methods require target model token probabilities (a black-box limitation). Additionally, high false positive rates create ethical risks, disproportionately flagging non-native English speakers."
  key_insight: "Instead of requiring the target LLM's own probabilities, use a series of weaker, accessible language models as probability proxies, then let a structured combinatorial search discover discriminative feature compositions — the signal is in how different-quality models disagree on token predictions."
  argument_chain: "Problem (LLM text indistinguishable from human) → Existing solutions fail to generalize → Key insight: weaker model probability compositions are discriminative → Structured search over vector/scalar function compositions → Simple linear classifier achieves SOTA → Validated across 3 domains, cross-model (Claude), cross-prompt, perturbation robustness, and human comparison"
  contribution_framing: "Three contributions implicitly stated: (1) Ghostbuster method itself (structured search + linear classifier on weaker model probabilities), (2) three new benchmark datasets for AI text detection, (3) extensive evaluation including cross-domain, cross-model, cross-prompt generalization and robustness analysis. Framed via performance superiority: 'achieves 99.0 F1... 5.9 F1 higher than the best preexisting model.'"
  intro_structure: "3 paragraphs — P1: Problem establishment (ChatGPT impact, societal concerns); P2: Existing solution failures (poor generalization, false positives, bias against non-native speakers); P3: Ghostbuster introduction with headline numbers and method sketch"
  notable_technique: "Effective use of the 'black-box constraint' framing — positions the paper as solving a harder, more practical problem than prior work (no access to target model probabilities), which makes the strong results even more impressive. Also leverages the non-native speaker bias issue to establish ethical urgency."

figures:
  figure_count: 6
  figure1:
    type: "method_overview"
    description: "Left-to-right pipeline diagram showing the three stages of Ghostbuster: (1) a text document is passed through three weaker language models (Unigram, Trigram, GPT-3) producing probability vectors, (2) vector functions (+, -, x, /, >, <) combine probability vectors, (3) scalar functions (||.||, max, var) reduce to features, (4) features fed to logistic regression classifier visualized as a scatter plot."
    narrative_role: "Provides immediate visual understanding of the full pipeline — reader grasps the method in one glance before the technical details."
    design_elements: ["Left-to-right flow", "Color-coded stages (blue models, purple vector ops, purple scalar ops, tan classifier)", "Mathematical operator symbols inside boxes", "Scatter plot as classifier visualization"]
    visual_style: "Clean horizontal pipeline with rounded-rectangle boxes. Pastel color scheme (light blue for models, lavender for function boxes, beige for classifier). Minimal text labels. Text snippet shown as input on the left. Arrows connect stages. Compact single-row layout."
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "F1 score degradation under increasing numbers of perturbations, split into local (character/word) and global (sentence/paragraph) perturbations"
      how_gain_highlighted: "Shows robustness envelope — performance stays above 80 F1 for most perturbation types until extreme levels; separate panels for local vs global perturbations make degradation patterns clear"
      design_note: "Two-panel layout (local left, global right) with shared y-axis (F1 Score) and color-coded lines per perturbation type. Legend inside plot. Clear visual separation of graceful degradation (character flips) vs catastrophic failure (paraphrasing). X-axis scales differ between panels (1-256 vs 0-10)."
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "F1 score across document sizes (10-1000 tokens) for in-domain and various out-of-domain settings (Claude, WP, Reuters, Essay)"
      how_gain_highlighted: "All lines converge to ~95-100 F1 at 500+ tokens, visually demonstrating reliability at longer documents; short-document weakness is honestly shown"
      design_note: "Single plot with 5 color-coded lines (blue=In-Domain, orange=Claude, green=WP, red=Reuters, purple=Essay). Dark background with grid. Log-scale-like x-axis (10,25,50,100,250,500,1000). Clearly shows the critical 100-token threshold where performance becomes reliable."
  ablation_figures:
    - figure_id: "Figure 5"
      viz_type: "feature_list"
      dimensions_varied: ["Domain (News, Creative Writing, Essays)", "Selected features per domain"]
      design_note: "Lists the actual features selected by forward selection for each domain — not a traditional chart but a reference figure showing which compositions matter. Allows readers to see domain-specific vs shared features."
    - figure_id: "Figure 6"
      viz_type: "bar_chart"
      dimensions_varied: ["Dataset (WritingPrompts, Reuters, IvyPanda)", "Entropy rate under GPT-3"]
      design_note: "Entropy rate visualization comparing human vs AI text predictability across domains — supports the theoretical motivation for why probability-based features work."
  figure_narrative_role: "Figure 1 (method overview) → Figure 2 (motivating example: human vs AI text side-by-side) → Figure 3 (robustness analysis) → Figure 4 (document length sensitivity) → Figure 5 (feature analysis, appendix) → Figure 6 (theoretical motivation via entropy, appendix). Main paper figures (1-4) follow: explain method → show problem → stress-test → analyze boundary conditions."

tables:
  table_count: 8
  main_result_table:
    table_id: "Table 2"
    row_axis: "methods"
    col_axis: "domains (News, Creative Writing, Student Essays, All Domains) x settings (In-Domain, Out-of-Domain)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "Best results implied by Ghostbuster row consistently highest; no explicit bold/underline formatting noted in HTML version"
    statistical_reporting: "Point estimates only, no confidence intervals or standard deviations"
    num_baselines: 4
    design_note: "Two major column groups (In-Domain | Out-of-Domain) with domain sub-columns. Clean structure shows both the in-domain ceiling and generalization gap simultaneously. Key insight: Ghostbuster's advantage is most visible in OOD columns where RoBERTa drops significantly (99.4→88.3 on News) while Ghostbuster stays high (99.5→97.9). The 'All Domains' column aggregates for quick comparison."
  ablation_tables:
    - table_id: "Table 4"
      what_varied: ["Feature search depth (1,2,3,4)", "Model components (ada, davinci, handcrafted)", "Feature selection method (random vs forward)"]
      variation_style: "full_numbers"
      design_note: "Comprehensive ablation with 9 conditions. Same column structure as Table 2 (domains x in/out-of-domain) enables direct comparison. Shows diminishing returns beyond depth 3, critical importance of GPT-3 models (without ada/davinci: 88.2 vs 99.0), and that handcrafted features add marginal value (98.9 without vs 99.0 with)."
  supplementary_tables:
    in_appendix: true
    content: "Table 1: Vector/scalar function definitions. Table 3: Generalization results (prompts, Claude, non-native). Tables 5-8: Dataset statistics, prompt templates, generation details."
    reason: "Table 1 is a reference table for the method's building blocks. Table 3 covers secondary evaluation axes. Tables 5-8 provide reproducibility details. Main paper keeps only the two most important tables (main results + ablations) to maintain narrative focus."

=== penedo2024_fineweb.yaml ===
paper_key: "penedo2024_fineweb"
title: "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale"
venue: "NeurIPS 2024"
full_text_available: true

research:
  baselines:
    - RefinedWeb
    - C4
    - The Pile
    - SlimPajama
    - RedPajama v2
    - Dolma 1.6
    - Dolma 1.7
    - Matrix
    - CC-100
    - Colossal-OSCAR
  metrics:
    - {name: "Aggregate Accuracy (avg of 9 benchmarks)", direction: "higher_better"}
    - {name: "HellaSwag", direction: "higher_better"}
    - {name: "MMLU", direction: "higher_better"}
    - {name: "ARC", direction: "higher_better"}
    - {name: "PIQA", direction: "higher_better"}
    - {name: "WinoGrande", direction: "higher_better"}
    - {name: "OpenBookQA", direction: "higher_better"}
    - {name: "CommonSenseQA", direction: "higher_better"}
    - {name: "SIQA", direction: "higher_better"}
  datasets:
    - {name: "FineWeb", size: "15T tokens from 96 Common Crawl snapshots"}
    - {name: "FineWeb-Edu", size: "1.3T tokens (educational subset of FineWeb)"}
    - {name: "RefinedWeb", size: "500B tokens"}
    - {name: "C4", size: "172B tokens"}
    - {name: "The Pile", size: "340B tokens"}
    - {name: "SlimPajama", size: "627B tokens"}
    - {name: "RedPajama v2", size: "20T tokens"}
    - {name: "Dolma 1.6", size: "3T tokens"}
    - {name: "Dolma 1.7", size: "1.2T tokens"}
    - {name: "Matrix", size: "1.3T tokens"}
    - {name: "CC-100", size: "70B tokens"}
    - {name: "Colossal-OSCAR", size: "850B tokens"}
  ablation_dimensions:
    - text_extraction_method (WARC trafilatura vs WET htmlparser)
    - base_filtering (URL blocklist + language ID + quality/repetition filters)
    - deduplication_scope (global vs per-snapshot MinHash)
    - deduplication_parameters (n-gram size, hash count, bucket structure, similarity threshold)
    - C4_filter_components (terminal punctuation, JS removal, ToS, doc length, lorem ipsum)
    - custom_heuristic_filters (50+ candidate statistics, 17 tested in Table 2)
    - educational_quality_threshold (0-5 scale, threshold sweep)
    - training_scale (28B tokens for filter ablations vs 350B for dedup ablations)
  training_recipe:
    model: "1.82B parameters (including embeddings), Llama architecture"
    optimizer: "not explicitly stated (likely AdamW given Llama architecture)"
    lr: "not explicitly stated"
    batch_size: "~2M tokens global batch size"
    sequence_length: 2048
    tokenizer: "GPT-2 tokenizer"
    hardware: "H100 GPUs, ~80,000 GPU-hours for 70+ ablation models"
    filter_ablation_tokens: "~28B tokens"
    dedup_ablation_tokens: "350B tokens"
    edu_classifier_cost: "6,000 H100 GPU-hours for classifying 15T tokens"
  method_family: "large-scale web data curation pipeline (extraction + filtering + deduplication + quality classification)"

positioning:
  core_claim: "Systematic, transparent web data curation with carefully ablated design choices produces 15T-token FineWeb and 1.3T-token FineWeb-Edu that outperform all existing open pretraining datasets, closing the gap between proprietary and public data knowledge."
  key_results: "FineWeb: ~52% aggregate accuracy at 350B tokens (top among all open datasets). FineWeb-Edu: MMLU 33%->37% (+12% relative), ARC 46%->57% (+24% relative), ~2% aggregate accuracy gain over FineWeb, reaching 33.6% MMLU at 38B tokens vs Matrix needing 300B tokens for similar."
  limitations:
    - "Entirely web content from Common Crawl; no books, speech transcripts, or other data types"
    - "Most ablation experiments at smaller scale (~28B tokens) due to compute constraints; dataset design at realistic pretraining scale could give more reliable guidance"
    - "Evaluation limited to academic benchmarks without instruction tuning or alignment; does not reflect current LLM usage patterns"
    - "Educational quality classifier may amplify biases in what Llama-3-70B-Instruct considers 'educational'"
  relation_to_us: "complementary"

narrative:
  story_type: "化繁为简型"
  hook: "Opens with the ubiquity of LLMs and immediately pivots to the dirty secret: [REDACTED] pretraining datasets behind the best open models (Llama 3, Mixtral) are not public, and curation strategies are 'closely guarded trade secrets.' Frames a growing gap between proprietary and public knowledge."
  tension: "Despite LLM performance depending heavily on data quality, the community lacks both access to high-quality large-scale datasets AND knowledge of how to build them. Existing open datasets are either too small, poorly documented, or underperform. The reader is made to feel the asymmetry between what industry knows and what the public can access."
  key_insight: "Global deduplication across all 96 Common Crawl snapshots paradoxically HURTS performance because it upsamples lower-quality data from older crawls. The data removed by global dedup was actually higher quality than the data retained. Per-snapshot individual deduplication is the correct approach. This counterintuitive finding is the paper's most distinctive empirical contribution."
  argument_chain: "problem (data curation is a black box) -> foundation (review existing datasets/methods) -> systematic pipeline construction (text extraction -> base filtering -> deduplication -> C4 filters -> custom filters, each ablated independently) -> counterintuitive dedup finding drives design -> cumulative pipeline = FineWeb 15T -> educational filtering via LLM annotation + lightweight classifier = FineWeb-Edu 1.3T -> validation against 10 baselines at 350B scale"
  contribution_framing: "Contributions woven into intro prose rather than bulleted list. Six implicit contributions: (1) FineWeb 15T dataset, (2) FineWeb-Edu 1.3T educational subset, (3) systematic ablation of all design choices, (4) in-depth deduplication investigation, (5) datatrove curation codebase, (6) all ablation models publicly released. Framed as 'advancing understanding' not just 'beating baselines.'"
  intro_structure: "Single long paragraph (~15 sentences) that covers: LLM success -> data importance -> scale + quality matter -> curation as trade secrets -> open models with closed data -> knowledge gap concern -> FineWeb introduction -> FineWeb-Edu introduction -> ablation methodology -> public release commitment. Unusually dense single-paragraph intro rather than multi-paragraph."
  notable_technique: "The 'ablation-as-narrative' structure: each section of the pipeline (extraction, filtering, dedup) is presented as a mini-experiment with its own hypothesis, ablation, finding, and decision. This makes a data engineering paper read like a sequence of scientific investigations. The counterintuitive global-dedup finding (Section 3.4) serves as the paper's dramatic peak, breaking reader expectations."

figures:
  figure_count: 27
  figure1:
    type: "motivation"
    description: "Line plot comparing aggregate accuracy (%) vs training tokens (billions, 0-28B) for two text extraction methods: WARC data processed with trafilatura (blue) vs WET default htmlparser (pink). Both start at ~33% and diverge steadily, with WARC reaching ~39.5% and WET plateauing at ~37.5% by 28B tokens."
    narrative_role: "Establishes the very first pipeline decision (text extraction) as consequential. Sets the pattern for all subsequent ablation figures: same axes, same comparison logic. Justifies the non-trivial compute cost of trafilatura over default WET."
    design_elements:
      - "Clean two-line comparison on same axes"
      - "Continuous training curves (not bar charts) showing the gap widens with scale"
      - "Minimal design: no grid clutter, clear legend below"
      - "Blue vs pink color coding for proposed vs baseline"
    visual_style: "Minimalist line plot, white background with faint horizontal gridlines. Two smoothly rising curves, blue (WARC/trafilatura) consistently above pink (WET). Legend below plot. Axes: y=Aggregate Acc (%), x=Training tokens (billions). Clean academic style, no unnecessary decoration."
  result_figures:
    - figure_id: "Figure 9"
      viz_type: "line_plot"
      what_compared: "Cumulative pipeline steps: base filtering vs +individual minhash vs +C4 filters vs full FineWeb, all at 350B token scale"
      how_gain_highlighted: "Four stacked training curves with clear vertical separation; FineWeb (orange) consistently on top, base filtering (green) consistently on bottom, showing each step adds measurable gain"
      design_note: "Uses same axis style as all ablation figures for visual continuity. Four colors clearly differentiated. Shows pipeline is monotonically improving—each step helps."
    - figure_id: "Figure 10"
      viz_type: "line_plot"
      what_compared: "FineWeb and FineWeb-Edu (Ours) vs 10 competing open datasets, all at 350B token scale"
      how_gain_highlighted: "FineWeb-Edu (orange) clearly on top reaching ~52%, FineWeb (green) in upper pack at ~50.5%. Color coding: 'Ours' in warm colors (orange, green) while competitors in cooler/darker colors. Visual dominance of FineWeb-Edu curve is immediate."
      design_note: "12 lines in one plot—aggressive but effective for showing FineWeb-Edu's dominance. Legend organized in 4 columns below. The visual message is clear even with crowded lines because the 'Ours' curves are distinctly above the pack."
    - figure_id: "Figure 11"
      viz_type: "line_plot"
      what_compared: "FineWeb-Edu vs competitors on MMLU specifically, showing token efficiency"
      how_gain_highlighted: "FineWeb-Edu reaches 33.6% at 38B tokens while Matrix needs 300B tokens for similar—10x token efficiency. The gap is visually dramatic."
      design_note: "Single-benchmark focus plot to highlight the most impressive result. Token efficiency narrative is more compelling than raw accuracy."
  ablation_figures:
    - figure_id: "Figure 6"
      viz_type: "bar_chart"
      dimensions_varied: ["individual C4 filter components"]
      design_note: "Bar chart showing each C4 filter's individual contribution to HellaSwag. Reveals terminal punctuation filter is most impactful but also most aggressive (removes ~30% tokens)."
    - figure_id: "Figure 7"
      viz_type: "bar_chart"
      dimensions_varied: ["custom filter combinations vs C4 vs baseline"]
      design_note: "Shows custom FineWeb filters outperform C4 while removing less data. Efficiency argument (better accuracy per token removed)."
    - figure_id: "Figure 8"
      viz_type: "histogram"
      dimensions_varied: ["deduplication method effect on punctuation distribution"]
      design_note: "Histogram of document-level punctuation ratios under different dedup methods. Reveals mechanism behind global dedup's failure: it shifts distribution toward low-punctuation (lower quality) documents."
    - figure_id: "Figure 16"
      viz_type: "line_plot"
      dimensions_varied: ["FineWeb-Edu educational quality threshold (0-5 scale)"]
      design_note: "Threshold sweep ablation for educational classifier. Shows threshold=3 is optimal; lower includes too much noise, higher is too aggressive."
  figure_narrative_role: "Fig 1-2 (text extraction + base filtering foundations) -> Fig 3-5 (dedup exploration: global failure -> individual success) -> Fig 6-8 (filter development: C4 decomposition -> custom filters -> mechanism analysis) -> Fig 9-10 (cumulative victory: pipeline steps + competitive comparison) -> Fig 11 (FineWeb-Edu headline result) -> Fig 12-16 (appendix: parameter details + threshold ablation) -> Fig 17-27 (bias analysis: distribution + association heatmaps). The narrative arc follows the pipeline construction chronologically, building evidence cumulatively."

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 2"
    description: "Full list of heuristic filters tested"
    row_axis: "candidate filter metrics with thresholds"
    col_axis: "metric | threshold | aggregate accuracy (%) | tokens removed (%)"
    row_organization: "by_performance"
    col_organization: "flat"
    highlight_strategy: "implicit ranking by aggregate accuracy (descending), no explicit bold/underline"
    statistical_reporting: "single-run accuracy and token removal percentage"
    num_baselines: 16
    design_note: "Unusual 'main table'—not a method-vs-baseline comparison but a filter candidate evaluation. The real main comparison is in Figure 10 (line plot), not a table. This reflects the paper's nature as a data engineering study where the 'results' are pipeline design choices, not model benchmarks. The table serves as a filter selection guide."
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Table 3 (bias analysis subgroups/terms). Additional dataset field documentation tables. The paper relies heavily on figures rather than tables for ablation results."
    reason: "Pipeline ablations are shown as training curves (line plots) because the temporal dynamics of how performance evolves with tokens is more informative than single-point numbers. Tables are reserved for enumeration tasks (filter list, bias terms, data fields)."
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "820febfd-f3af-4a81-a6ac-f5194b8d611f",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "f682fd16-84ce-489f-b54c-e22124c73447",
  "toolUseResult": {
    "stdout": "=== binoculars2024.yaml ===\npaper_key: \"binoculars2024\"\ntitle: \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\"\nvenue: \"ICML 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"DetectGPT\", \"Fast-DetectGPT\", \"likelihood thresholding\", \"supervised classifiers\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"TPR@1%FPR\", direction: \"higher_better\"}\n    - {name: \"TPR@0.01%FPR\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"multi-domain text corpus (news, wiki, creative)\", size: \"N/A\"}\n    - {name: \"ChatGPT-generated samples\", size: \"N/A\"}\n  ablation_dimensions: [\"LLM pair choice\", \"document type\", \"source model\"]\n  training_recipe: {optimizer: \"N/A (zero-shot)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"zero-shot detection via contrastive LLM scoring\"\n\npositioning:\n  core_claim: \"A simple score contrasting two closely related LLMs achieves SOTA zero-shot detection without any training data, detecting >90% of generated text at 0.01% FPR\"\n  key_results: \">90% detection of ChatGPT at 0.01% FPR; generalizes across LLMs without model-specific tuning\"\n  limitations: [\"requires two LLMs at inference\", \"performance depends on LLM pair choice\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== fast_detectgpt2024.yaml ===\npaper_key: \"fast_detectgpt2024\"\ntitle: \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\"\nvenue: \"ICLR 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"DetectGPT\", \"likelihood ratio\", \"rank-based methods\", \"supervised detectors\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"detection speed\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"XSum\", size: \"N/A\"}\n    - {name: \"SQuAD\", size: \"N/A\"}\n    - {name: \"WritingPrompts\", size: \"N/A\"}\n  ablation_dimensions: [\"source model\", \"scoring model\", \"perturbation vs sampling\"]\n  training_recipe: {optimizer: \"N/A (zero-shot)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"zero-shot detection via conditional probability curvature\"\n\npositioning:\n  core_claim: \"Replacing DetectGPT's perturbation step with conditional probability sampling achieves 340x speedup with ~75% relative improvement in both white-box and black-box settings\"\n  key_results: \"340x faster than DetectGPT; 75% relative improvement; 80% ChatGPT detection at 1% FPR\"\n  limitations: [\"still requires model access for scoring\", \"performance varies by domain\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== diveye2026.yaml ===\npaper_key: \"diveye2026\"\ntitle: \"DivEye: Diversity Boosts AI-Generated Text Detection\"\nvenue: \"TMLR 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"DetectGPT\", \"Fast-DetectGPT\", \"Binoculars\", \"supervised fine-tuned classifiers\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"detection accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"multi-domain benchmarks\", size: \"N/A\"}\n  ablation_dimensions: [\"statistical features\", \"auxiliary signal integration\", \"paraphrasing robustness\", \"cross-domain transfer\"]\n  training_recipe: {optimizer: \"N/A (zero-shot statistical)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"statistical feature-based detection using surprisal diversity\"\n\npositioning:\n  core_claim: \"Human text exhibits richer variability in lexical and structural unpredictability (surprisal diversity) than LLM outputs, and this signal is interpretable, robust, and complements existing detectors\"\n  key_results: \"Outperforms zero-shot detectors by up to 33.2%; improves existing detectors by up to 18.7% as auxiliary signal; robust to paraphrasing attacks\"\n  limitations: [\"statistical features may not capture all AI text patterns\", \"performance on very short texts unclear\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== verma2024_ghostbuster.yaml ===\npaper_key: \"verma2024_ghostbuster\"\ntitle: \"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\"\nvenue: \"NAACL 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Perplexity-only (GPT-3 davinci perplexity threshold)\"\n    - \"DetectGPT (Mitchell et al. 2023, unsupervised perturbation-based)\"\n    - \"GPTZero (commercial detector)\"\n    - \"RoBERTa fine-tuned (supervised neural baseline)\"\n    - \"Human evaluation (17 participants)\"\n  metrics:\n    - {name: \"F1\", direction: \"higher_better\"}\n    - {name: \"Accuracy\", direction: \"higher_better\"}\n    - {name: \"Precision\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"IvyPanda Student Essays\", size: \"7,000 docs (1K human + 1K ChatGPT same-prompt + 4K ChatGPT generalization)\"}\n    - {name: \"Reuters 50-50 News Articles\", size: \"7,000 docs (same split structure)\"}\n    - {name: \"r/WritingPrompts Creative Writing\", size: \"7,000 docs (same split structure)\"}\n    - {name: \"Lang-8 non-native English\", size: \"evaluation only\"}\n    - {name: \"TOEFL 11 (essay subset)\", size: \"evaluation only\"}\n    - {name: \"TOEFL 91 (essay subset)\", size: \"evaluation only\"}\n  ablation_dimensions:\n    - \"Feature search depth (1, 2, 3, 4)\"\n    - \"Model components (with/without ada, davinci, handcrafted features)\"\n    - \"Random features vs selected features\"\n    - \"Document length (10-1000 tokens)\"\n    - \"Perturbation robustness (character/word/sentence/paragraph level)\"\n    - \"Cross-domain generalization (in-domain vs out-of-domain)\"\n    - \"Cross-model generalization (ChatGPT vs Claude)\"\n    - \"Cross-prompt generalization (5 prompt variants)\"\n  training_recipe:\n    classifier: \"Logistic regression with L2 regularization, C=1\"\n    optimizer: \"N/A (closed-form or standard sklearn solver)\"\n    lr: \"N/A\"\n    hardware: \"Not specified\"\n    feature_generation: \"Recursive composition of vector/scalar functions up to depth 3, yielding 2534 candidate features\"\n    feature_selection: \"Forward feature selection on validation set\"\n    weaker_models: \"Unigram fertility, Kneser-Ney trigram, GPT-3 ada, GPT-3 davinci\"\n  method_family: \"Feature-engineered classifier using proxy model probabilities\"\n\npositioning:\n  core_claim: \"A structured search over compositions of weaker language model probabilities, combined with a simple linear classifier, can robustly detect AI-generated text without access to the target model's token probabilities.\"\n  key_results: \"99.0 F1 in-domain across all domains (+0.9 over RoBERTa, +5.9 over GPTZero); 97.0 F1 out-of-domain average (vs 85.1 RoBERTa); 92.2 F1 on Claude generalization; 99.5 F1 across prompt variants\"\n  limitations:\n    - \"Poor performance on documents under 100 tokens (F1 drops below 80 at 25 tokens)\"\n    - \"Lower accuracy on non-native English speaker text (TOEFL 91: 74.7% accuracy, below GPTZero 92.3% and RoBERTa 96.7%)\"\n    - \"Datasets limited to British/American English, not representative of all writing styles\"\n    - \"Vulnerable to paraphrasing attacks (Undetectable.ai reduces recall from 99% to 62%)\"\n    - \"Relies on API access to GPT-3 ada/davinci which may be deprecated\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the societal impact of ChatGPT's fluent text generation — schools restricting ChatGPT, authenticity concerns across education and journalism — establishing real-world urgency.\"\n  tension: \"Existing detectors (DetectGPT, GPTZero) show poor generalization across domains and models; supervised neural methods (RoBERTa) overfit to training distribution; zero-shot methods require target model token probabilities (a black-box limitation). Additionally, high false positive rates create ethical risks, disproportionately flagging non-native English speakers.\"\n  key_insight: \"Instead of requiring the target LLM's own probabilities, use a series of weaker, accessible language models as probability proxies, then let a structured combinatorial search discover discriminative feature compositions — the signal is in how different-quality models disagree on token predictions.\"\n  argument_chain: \"Problem (LLM text indistinguishable from human) → Existing solutions fail to generalize → Key insight: weaker model probability compositions are discriminative → Structured search over vector/scalar function compositions → Simple linear classifier achieves SOTA → Validated across 3 domains, cross-model (Claude), cross-prompt, perturbation robustness, and human comparison\"\n  contribution_framing: \"Three contributions implicitly stated: (1) Ghostbuster method itself (structured search + linear classifier on weaker model probabilities), (2) three new benchmark datasets for AI text detection, (3) extensive evaluation including cross-domain, cross-model, cross-prompt generalization and robustness analysis. Framed via performance superiority: 'achieves 99.0 F1... 5.9 F1 higher than the best preexisting model.'\"\n  intro_structure: \"3 paragraphs — P1: Problem establishment (ChatGPT impact, societal concerns); P2: Existing solution failures (poor generalization, false positives, bias against non-native speakers); P3: Ghostbuster introduction with headline numbers and method sketch\"\n  notable_technique: \"Effective use of the 'black-box constraint' framing — positions the paper as solving a harder, more practical problem than prior work (no access to target model probabilities), which makes the strong results even more impressive. Also leverages the non-native speaker bias issue to establish ethical urgency.\"\n\nfigures:\n  figure_count: 6\n  figure1:\n    type: \"method_overview\"\n    description: \"Left-to-right pipeline diagram showing the three stages of Ghostbuster: (1) a text document is passed through three weaker language models (Unigram, Trigram, GPT-3) producing probability vectors, (2) vector functions (+, -, x, /, >, <) combine probability vectors, (3) scalar functions (||.||, max, var) reduce to features, (4) features fed to logistic regression classifier visualized as a scatter plot.\"\n    narrative_role: \"Provides immediate visual understanding of the full pipeline — reader grasps the method in one glance before the technical details.\"\n    design_elements: [\"Left-to-right flow\", \"Color-coded stages (blue models, purple vector ops, purple scalar ops, tan classifier)\", \"Mathematical operator symbols inside boxes\", \"Scatter plot as classifier visualization\"]\n    visual_style: \"Clean horizontal pipeline with rounded-rectangle boxes. Pastel color scheme (light blue for models, lavender for function boxes, beige for classifier). Minimal text labels. Text snippet shown as input on the left. Arrows connect stages. Compact single-row layout.\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"F1 score degradation under increasing numbers of perturbations, split into local (character/word) and global (sentence/paragraph) perturbations\"\n      how_gain_highlighted: \"Shows robustness envelope — performance stays above 80 F1 for most perturbation types until extreme levels; separate panels for local vs global perturbations make degradation patterns clear\"\n      design_note: \"Two-panel layout (local left, global right) with shared y-axis (F1 Score) and color-coded lines per perturbation type. Legend inside plot. Clear visual separation of graceful degradation (character flips) vs catastrophic failure (paraphrasing). X-axis scales differ between panels (1-256 vs 0-10).\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"F1 score across document sizes (10-1000 tokens) for in-domain and various out-of-domain settings (Claude, WP, Reuters, Essay)\"\n      how_gain_highlighted: \"All lines converge to ~95-100 F1 at 500+ tokens, visually demonstrating reliability at longer documents; short-document weakness is honestly shown\"\n      design_note: \"Single plot with 5 color-coded lines (blue=In-Domain, orange=Claude, green=WP, red=Reuters, purple=Essay). Dark background with grid. Log-scale-like x-axis (10,25,50,100,250,500,1000). Clearly shows the critical 100-token threshold where performance becomes reliable.\"\n  ablation_figures:\n    - figure_id: \"Figure 5\"\n      viz_type: \"feature_list\"\n      dimensions_varied: [\"Domain (News, Creative Writing, Essays)\", \"Selected features per domain\"]\n      design_note: \"Lists the actual features selected by forward selection for each domain — not a traditional chart but a reference figure showing which compositions matter. Allows readers to see domain-specific vs shared features.\"\n    - figure_id: \"Figure 6\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"Dataset (WritingPrompts, Reuters, IvyPanda)\", \"Entropy rate under GPT-3\"]\n      design_note: \"Entropy rate visualization comparing human vs AI text predictability across domains — supports the theoretical motivation for why probability-based features work.\"\n  figure_narrative_role: \"Figure 1 (method overview) → Figure 2 (motivating example: human vs AI text side-by-side) → Figure 3 (robustness analysis) → Figure 4 (document length sensitivity) → Figure 5 (feature analysis, appendix) → Figure 6 (theoretical motivation via entropy, appendix). Main paper figures (1-4) follow: explain method → show problem → stress-test → analyze boundary conditions.\"\n\ntables:\n  table_count: 8\n  main_result_table:\n    table_id: \"Table 2\"\n    row_axis: \"methods\"\n    col_axis: \"domains (News, Creative Writing, Student Essays, All Domains) x settings (In-Domain, Out-of-Domain)\"\n    row_organization: \"by_category\"\n    col_organization: \"grouped_by_dataset\"\n    highlight_strategy: \"Best results implied by Ghostbuster row consistently highest; no explicit bold/underline formatting noted in HTML version\"\n    statistical_reporting: \"Point estimates only, no confidence intervals or standard deviations\"\n    num_baselines: 4\n    design_note: \"Two major column groups (In-Domain | Out-of-Domain) with domain sub-columns. Clean structure shows both the in-domain ceiling and generalization gap simultaneously. Key insight: Ghostbuster's advantage is most visible in OOD columns where RoBERTa drops significantly (99.4→88.3 on News) while Ghostbuster stays high (99.5→97.9). The 'All Domains' column aggregates for quick comparison.\"\n  ablation_tables:\n    - table_id: \"Table 4\"\n      what_varied: [\"Feature search depth (1,2,3,4)\", \"Model components (ada, davinci, handcrafted)\", \"Feature selection method (random vs forward)\"]\n      variation_style: \"full_numbers\"\n      design_note: \"Comprehensive ablation with 9 conditions. Same column structure as Table 2 (domains x in/out-of-domain) enables direct comparison. Shows diminishing returns beyond depth 3, critical importance of GPT-3 models (without ada/davinci: 88.2 vs 99.0), and that handcrafted features add marginal value (98.9 without vs 99.0 with).\"\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 1: Vector/scalar function definitions. Table 3: Generalization results (prompts, Claude, non-native). Tables 5-8: Dataset statistics, prompt templates, generation details.\"\n    reason: \"Table 1 is a reference table for the method's building blocks. Table 3 covers secondary evaluation axes. Tables 5-8 provide reproducibility details. Main paper keeps only the two most important tables (main results + ablations) to maintain narrative focus.\"\n\n=== penedo2024_fineweb.yaml ===\npaper_key: \"penedo2024_fineweb\"\ntitle: \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\"\nvenue: \"NeurIPS 2024\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - RefinedWeb\n    - C4\n    - The Pile\n    - SlimPajama\n    - RedPajama v2\n    - Dolma 1.6\n    - Dolma 1.7\n    - Matrix\n    - CC-100\n    - Colossal-OSCAR\n  metrics:\n    - {name: \"Aggregate Accuracy (avg of 9 benchmarks)\", direction: \"higher_better\"}\n    - {name: \"HellaSwag\", direction: \"higher_better\"}\n    - {name: \"MMLU\", direction: \"higher_better\"}\n    - {name: \"ARC\", direction: \"higher_better\"}\n    - {name: \"PIQA\", direction: \"higher_better\"}\n    - {name: \"WinoGrande\", direction: \"higher_better\"}\n    - {name: \"OpenBookQA\", direction: \"higher_better\"}\n    - {name: \"CommonSenseQA\", direction: \"higher_better\"}\n    - {name: \"SIQA\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"FineWeb\", size: \"15T tokens from 96 Common Crawl snapshots\"}\n    - {name: \"FineWeb-Edu\", size: \"1.3T tokens (educational subset of FineWeb)\"}\n    - {name: \"RefinedWeb\", size: \"500B tokens\"}\n    - {name: \"C4\", size: \"172B tokens\"}\n    - {name: \"The Pile\", size: \"340B tokens\"}\n    - {name: \"SlimPajama\", size: \"627B tokens\"}\n    - {name: \"RedPajama v2\", size: \"20T tokens\"}\n    - {name: \"Dolma 1.6\", size: \"3T tokens\"}\n    - {name: \"Dolma 1.7\", size: \"1.2T tokens\"}\n    - {name: \"Matrix\", size: \"1.3T tokens\"}\n    - {name: \"CC-100\", size: \"70B tokens\"}\n    - {name: \"Colossal-OSCAR\", size: \"850B tokens\"}\n  ablation_dimensions:\n    - text_extraction_method (WARC trafilatura vs WET htmlparser)\n    - base_filtering (URL blocklist + language ID + quality/repetition filters)\n    - deduplication_scope (global vs per-snapshot MinHash)\n    - deduplication_parameters (n-gram size, hash count, bucket structure, similarity threshold)\n    - C4_filter_components (terminal punctuation, JS removal, ToS, doc length, lorem ipsum)\n    - custom_heuristic_filters (50+ candidate statistics, 17 tested in Table 2)\n    - educational_quality_threshold (0-5 scale, threshold sweep)\n    - training_scale (28B tokens for filter ablations vs 350B for dedup ablations)\n  training_recipe:\n    model: \"1.82B parameters (including embeddings), Llama architecture\"\n    optimizer: \"not explicitly stated (likely AdamW given Llama architecture)\"\n    lr: \"not explicitly stated\"\n    batch_size: \"~2M tokens global batch size\"\n    sequence_length: 2048\n    tokenizer: \"GPT-2 tokenizer\"\n    hardware: \"H100 GPUs, ~80,000 GPU-hours for 70+ ablation models\"\n    filter_ablation_tokens: \"~28B tokens\"\n    dedup_ablation_tokens: \"350B tokens\"\n    edu_classifier_cost: \"6,000 H100 GPU-hours for classifying 15T tokens\"\n  method_family: \"large-scale web data curation pipeline (extraction + filtering + deduplication + quality classification)\"\n\npositioning:\n  core_claim: \"Systematic, transparent web data curation with carefully ablated design choices produces 15T-token FineWeb and 1.3T-token FineWeb-Edu that outperform all existing open pretraining datasets, closing the gap between proprietary and public data knowledge.\"\n  key_results: \"FineWeb: ~52% aggregate accuracy at 350B tokens (top among all open datasets). FineWeb-Edu: MMLU 33%->37% (+12% relative), ARC 46%->57% (+24% relative), ~2% aggregate accuracy gain over FineWeb, reaching 33.6% MMLU at 38B tokens vs Matrix needing 300B tokens for similar.\"\n  limitations:\n    - \"Entirely web content from Common Crawl; no books, speech transcripts, or other data types\"\n    - \"Most ablation experiments at smaller scale (~28B tokens) due to compute constraints; dataset design at realistic pretraining scale could give more reliable guidance\"\n    - \"Evaluation limited to academic benchmarks without instruction tuning or alignment; does not reflect current LLM usage patterns\"\n    - \"Educational quality classifier may amplify biases in what Llama-3-70B-Instruct considers 'educational'\"\n  relation_to_us: \"complementary\"\n\nnarrative:\n  story_type: \"化繁为简型\"\n  hook: \"Opens with the ubiquity of LLMs and immediately pivots to the dirty secret: [REDACTED] pretraining datasets behind the best open models (Llama 3, Mixtral) are not public, and curation strategies are 'closely guarded trade secrets.' Frames a growing gap between proprietary and public knowledge.\"\n  tension: \"Despite LLM performance depending heavily on data quality, the community lacks both access to high-quality large-scale datasets AND knowledge of how to build them. Existing open datasets are either too small, poorly documented, or underperform. The reader is made to feel the asymmetry between what industry knows and what the public can access.\"\n  key_insight: \"Global deduplication across all 96 Common Crawl snapshots paradoxically HURTS performance because it upsamples lower-quality data from older crawls. The data removed by global dedup was actually higher quality than the data retained. Per-snapshot individual deduplication is the correct approach. This counterintuitive finding is the paper's most distinctive empirical contribution.\"\n  argument_chain: \"problem (data curation is a black box) -> foundation (review existing datasets/methods) -> systematic pipeline construction (text extraction -> base filtering -> deduplication -> C4 filters -> custom filters, each ablated independently) -> counterintuitive dedup finding drives design -> cumulative pipeline = FineWeb 15T -> educational filtering via LLM annotation + lightweight classifier = FineWeb-Edu 1.3T -> validation against 10 baselines at 350B scale\"\n  contribution_framing: \"Contributions woven into intro prose rather than bulleted list. Six implicit contributions: (1) FineWeb 15T dataset, (2) FineWeb-Edu 1.3T educational subset, (3) systematic ablation of all design choices, (4) in-depth deduplication investigation, (5) datatrove curation codebase, (6) all ablation models publicly released. Framed as 'advancing understanding' not just 'beating baselines.'\"\n  intro_structure: \"Single long paragraph (~15 sentences) that covers: LLM success -> data importance -> scale + quality matter -> curation as trade secrets -> open models with closed data -> knowledge gap concern -> FineWeb introduction -> FineWeb-Edu introduction -> ablation methodology -> public release commitment. Unusually dense single-paragraph intro rather than multi-paragraph.\"\n  notable_technique: \"The 'ablation-as-narrative' structure: each section of the pipeline (extraction, filtering, dedup) is presented as a mini-experiment with its own hypothesis, ablation, finding, and decision. This makes a data engineering paper read like a sequence of scientific investigations. The counterintuitive global-dedup finding (Section 3.4) serves as the paper's dramatic peak, breaking reader expectations.\"\n\nfigures:\n  figure_count: 27\n  figure1:\n    type: \"motivation\"\n    description: \"Line plot comparing aggregate accuracy (%) vs training tokens (billions, 0-28B) for two text extraction methods: WARC data processed with trafilatura (blue) vs WET default htmlparser (pink). Both start at ~33% and diverge steadily, with WARC reaching ~39.5% and WET plateauing at ~37.5% by 28B tokens.\"\n    narrative_role: \"Establishes the very first pipeline decision (text extraction) as consequential. Sets the pattern for all subsequent ablation figures: same axes, same comparison logic. Justifies the non-trivial compute cost of trafilatura over default WET.\"\n    design_elements:\n      - \"Clean two-line comparison on same axes\"\n      - \"Continuous training curves (not bar charts) showing the gap widens with scale\"\n      - \"Minimal design: no grid clutter, clear legend below\"\n      - \"Blue vs pink color coding for proposed vs baseline\"\n    visual_style: \"Minimalist line plot, white background with faint horizontal gridlines. Two smoothly rising curves, blue (WARC/trafilatura) consistently above pink (WET). Legend below plot. Axes: y=Aggregate Acc (%), x=Training tokens (billions). Clean academic style, no unnecessary decoration.\"\n  result_figures:\n    - figure_id: \"Figure 9\"\n      viz_type: \"line_plot\"\n      what_compared: \"Cumulative pipeline steps: base filtering vs +individual minhash vs +C4 filters vs full FineWeb, all at 350B token scale\"\n      how_gain_highlighted: \"Four stacked training curves with clear vertical separation; FineWeb (orange) consistently on top, base filtering (green) consistently on bottom, showing each step adds measurable gain\"\n      design_note: \"Uses same axis style as all ablation figures for visual continuity. Four colors clearly differentiated. Shows pipeline is monotonically improving—each step helps.\"\n    - figure_id: \"Figure 10\"\n      viz_type: \"line_plot\"\n      what_compared: \"FineWeb and FineWeb-Edu (Ours) vs 10 competing open datasets, all at 350B token scale\"\n      how_gain_highlighted: \"FineWeb-Edu (orange) clearly on top reaching ~52%, FineWeb (green) in upper pack at ~50.5%. Color coding: 'Ours' in warm colors (orange, green) while competitors in cooler/darker colors. Visual dominance of FineWeb-Edu curve is immediate.\"\n      design_note: \"12 lines in one plot—aggressive but effective for showing FineWeb-Edu's dominance. Legend organized in 4 columns below. The visual message is clear even with crowded lines because the 'Ours' curves are distinctly above the pack.\"\n    - figure_id: \"Figure 11\"\n      viz_type: \"line_plot\"\n      what_compared: \"FineWeb-Edu vs competitors on MMLU specifically, showing token efficiency\"\n      how_gain_highlighted: \"FineWeb-Edu reaches 33.6% at 38B tokens while Matrix needs 300B tokens for similar—10x token efficiency. The gap is visually dramatic.\"\n      design_note: \"Single-benchmark focus plot to highlight the most impressive result. Token efficiency narrative is more compelling than raw accuracy.\"\n  ablation_figures:\n    - figure_id: \"Figure 6\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"individual C4 filter components\"]\n      design_note: \"Bar chart showing each C4 filter's individual contribution to HellaSwag. Reveals terminal punctuation filter is most impactful but also most aggressive (removes ~30% tokens).\"\n    - figure_id: \"Figure 7\"\n      viz_type: \"bar_chart\"\n      dimensions_varied: [\"custom filter combinations vs C4 vs baseline\"]\n      design_note: \"Shows custom FineWeb filters outperform C4 while removing less data. Efficiency argument (better accuracy per token removed).\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"histogram\"\n      dimensions_varied: [\"deduplication method effect on punctuation distribution\"]\n      design_note: \"Histogram of document-level punctuation ratios under different dedup methods. Reveals mechanism behind global dedup's failure: it shifts distribution toward low-punctuation (lower quality) documents.\"\n    - figure_id: \"Figure 16\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"FineWeb-Edu educational quality threshold (0-5 scale)\"]\n      design_note: \"Threshold sweep ablation for educational classifier. Shows threshold=3 is optimal; lower includes too much noise, higher is too aggressive.\"\n  figure_narrative_role: \"Fig 1-2 (text extraction + base filtering foundations) -> Fig 3-5 (dedup exploration: global failure -> individual success) -> Fig 6-8 (filter development: C4 decomposition -> custom filters -> mechanism analysis) -> Fig 9-10 (cumulative victory: pipeline steps + competitive comparison) -> Fig 11 (FineWeb-Edu headline result) -> Fig 12-16 (appendix: parameter details + threshold ablation) -> Fig 17-27 (bias analysis: distribution + association heatmaps). The narrative arc follows the pipeline construction chronologically, building evidence cumulatively.\"\n\ntables:\n  table_count: 4\n  main_result_table:\n    table_id: \"Table 2\"\n    description: \"Full list of heuristic filters tested\"\n    row_axis: \"candidate filter metrics with thresholds\"\n    col_axis: \"metric | threshold | aggregate accuracy (%) | tokens removed (%)\"\n    row_organization: \"by_performance\"\n    col_organization: \"flat\"\n    highlight_strategy: \"implicit ranking by aggregate accuracy (descending), no explicit bold/underline\"\n    statistical_reporting: \"single-run accuracy and token removal percentage\"\n    num_baselines: 16\n    design_note: \"Unusual 'main table'—not a method-vs-baseline comparison but a filter candidate evaluation. The real main comparison is in Figure 10 (line plot), not a table. This reflects the paper's nature as a data engineering study where the 'results' are pipeline design choices, not model benchmarks. The table serves as a filter selection guide.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Table 3 (bias analysis subgroups/terms). Additional dataset field documentation tables. The paper relies heavily on figures rather than tables for ablation results.\"\n    reason: \"Pipeline ablations are shown as training curves (line plots) because the temporal dynamics of how performance evolves with tokens is more informative than single-point numbers. Tables are reserved for enumeration tasks (filter list, bias terms, data fields).\"",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "820febfd-f3af-4a81-a6ac-f5194b8d611f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "f682fd16-84ce-489f-b54c-e22124c73447",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Tool call

_source line 45 · 2026-05-21T15:05:42.968Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011xRoHPu8zkEi3fZNPrDx2F`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp && for f in loki2025.yaml tulchinskii2024_intrinsic_dim.yaml editlens2026.yaml cloc2025.yaml qurating2024.yaml; do echo \"=== $f ===\"; cat \"$f\"; echo; done",
  "description": "Read batch 4 of YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f682fd16-84ce-489f-b54c-e22124c73447",
  "isSidechain": false,
  "requestId": "req_011CbFvMqFvG9Wp9T4Jpq7n5",
  "type": "assistant",
  "uuid": "c6a8c8f9-bd04-47ec-8935-125c31c56fc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zik69tzk18JbuJHhgGdxT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8222,
      "cache_read_input_tokens": 49732,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 49732,
          "cache_creation_input_tokens": 8222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8222
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

_source line 46 · 2026-05-21T15:05:43.031Z_

<details><summary>↩ Tool result · `toolu_011xRoHPu8zkEi3fZNPrDx2F`</summary>

```text
=== loki2025.yaml ===
paper_key: "loki2025"
title: "LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models"
venue: "ICLR 2025 Spotlight"
full_text_available: false

research:
  baselines: ["22 open-source LMMs", "6 closed-source LMMs"]
  metrics:
    - {name: "coarse-grained judgment accuracy", direction: "higher_better"}
    - {name: "fine-grained anomaly selection accuracy", direction: "higher_better"}
    - {name: "explanation quality", direction: "higher_better"}
  datasets:
    - {name: "LOKI benchmark", size: "18K questions across 26 subcategories"}
  ablation_dimensions: ["modality (video/image/3D/text/audio)", "difficulty level", "task type (judgment/selection/explanation)"]
  training_recipe: {optimizer: "N/A (benchmark)", lr: "N/A", hardware: "N/A"}
  method_family: "multimodal synthetic data detection benchmark"

positioning:
  core_claim: "First comprehensive benchmark for evaluating LMM ability to detect synthetic data across 5 modalities with both coarse and fine-grained evaluation"
  key_results: "LMMs show potential as synthetic detectors but reveal significant limitations; large gap between coarse judgment and fine-grained explanation"
  limitations: ["benchmark may not cover all generation methods", "multimodal focus may dilute text-specific insights"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== tulchinskii2024_intrinsic_dim.yaml ===
paper_key: "tulchinskii2024_intrinsic_dim"
title: "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts"
venue: "NeurIPS 2023"
full_text_available: false

research:
  baselines: ["DetectGPT", "likelihood-based methods", "supervised classifiers"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
    - {name: "cross-domain accuracy", direction: "higher_better"}
    - {name: "cross-model accuracy", direction: "higher_better"}
  datasets:
    - {name: "multi-language text corpora (English, Chinese, etc.)", size: "N/A"}
  ablation_dimensions: ["language", "generator model", "text domain", "writer proficiency level"]
  training_recipe: {optimizer: "N/A (intrinsic dimension estimation)", lr: "N/A", hardware: "N/A"}
  method_family: "geometric / manifold-based detection via intrinsic dimensionality"

positioning:
  core_claim: "Human texts have intrinsic dimensionality ~9 (alphabet languages) / ~7 (Chinese) while AI texts are ~1.5 lower, providing a language-agnostic, domain-invariant detection signal"
  key_results: "Outperforms SOTA in model-agnostic and cross-domain scenarios; stable across languages, domains, and writer proficiency levels"
  limitations: ["computational cost of dimension estimation", "may degrade with more human-like models"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== editlens2026.yaml ===
paper_key: "editlens2026"
title: "EditLens: Quantifying the Extent of AI Editing in Text"
venue: "ICLR 2026"
full_text_available: false

research:
  baselines: ["binary AI detectors (GPTZero, etc.)", "ternary classifiers"]
  metrics:
    - {name: "F1 (binary)", direction: "higher_better"}
    - {name: "F1 (ternary)", direction: "higher_better"}
    - {name: "regression correlation", direction: "higher_better"}
  datasets:
    - {name: "human-AI mixed editing dataset", size: "N/A"}
    - {name: "Grammarly editing data", size: "N/A"}
  ablation_dimensions: ["editing extent (continuous)", "similarity metric choice", "human annotation agreement"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "regression-based continuous AI editing quantification"

positioning:
  core_claim: "First to formalize AI editing detection as continuous regression rather than binary/ternary classification, achieving SOTA on both classification and regression tasks"
  key_results: "Binary F1=94.7%, ternary F1=90.4%; validated against human annotators; practical Grammarly case study"
  limitations: ["requires original human text for metric validation", "continuous scoring may be hard to interpret"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== cloc2025.yaml ===
paper_key: "cloc2025"
title: "CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss"
venue: "CVPR 2025"
full_text_available: false

research:
  baselines: ["standard contrastive learning", "ordinal regression methods", "cross-entropy classification"]
  metrics:
    - {name: "MAE (mean absolute error)", direction: "lower_better"}
    - {name: "classification accuracy", direction: "higher_better"}
  datasets:
    - {name: "Adience (age estimation)", size: "N/A"}
    - {name: "Historical Colour Image Dating", size: "N/A"}
    - {name: "Knee Osteoarthritis", size: "N/A"}
    - {name: "Indian Diabetic Retinopathy Image", size: "N/A"}
    - {name: "Breast Carcinoma Subtyping", size: "N/A"}
  ablation_dimensions: ["margin type", "number of margins", "contrastive pair selection"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "N/A"}
  method_family: "contrastive learning for ordinal classification"

positioning:
  core_claim: "Multi-margin N-pair loss enables flexible decision boundaries across adjacent ordinal categories, preserving class ordering while reducing overfitting to training bias"
  key_results: "Outperforms existing ordinal classification methods on 5 real-world datasets"
  limitations: ["image-focused evaluation", "limited to moderate number of ordinal classes"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== qurating2024.yaml ===
paper_key: "qurating2024"
title: "QuRating: Selecting High-Quality Data for Training Language Models"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["uniform random sampling", "perplexity-based filtering"]
  metrics:
    - {name: "perplexity", direction: "lower_better"}
    - {name: "in-context learning accuracy", direction: "higher_better"}
    - {name: "training efficiency (steps to target)", direction: "lower_better"}
  datasets:
    - {name: "260B token pre-training corpus", size: "260B tokens"}
    - {name: "30B token subsets sampled by quality", size: "30B tokens"}
  ablation_dimensions: ["quality dimension (writing style, expertise, facts, educational value)", "quality threshold", "quality-diversity balance"]
  training_recipe: {optimizer: "N/A", lr: "N/A", hardware: "1.3B parameter LMs"}
  method_family: "LLM-based data quality rating for pre-training data selection"

positioning:
  core_claim: "LLMs can learn quality ratings from pairwise judgments across 4 dimensions, and training on educational-value-selected data matches uniform sampling with 50% fewer steps"
  key_results: "Educational value selection most impactful; quality-diversity balance is critical; 1.3B models trained on 30B quality-filtered tokens"
  limitations: ["limited to 1.3B scale", "quality dimensions may not cover all aspects"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6a8c8f9-bd04-47ec-8935-125c31c56fc8",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "024297a9-46f4-4be9-a504-fd8e8d9402b7",
  "toolUseResult": {
    "stdout": "=== loki2025.yaml ===\npaper_key: \"loki2025\"\ntitle: \"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\"\nvenue: \"ICLR 2025 Spotlight\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"22 open-source LMMs\", \"6 closed-source LMMs\"]\n  metrics:\n    - {name: \"coarse-grained judgment accuracy\", direction: \"higher_better\"}\n    - {name: \"fine-grained anomaly selection accuracy\", direction: \"higher_better\"}\n    - {name: \"explanation quality\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"LOKI benchmark\", size: \"18K questions across 26 subcategories\"}\n  ablation_dimensions: [\"modality (video/image/3D/text/audio)\", \"difficulty level\", \"task type (judgment/selection/explanation)\"]\n  training_recipe: {optimizer: \"N/A (benchmark)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"multimodal synthetic data detection benchmark\"\n\npositioning:\n  core_claim: \"First comprehensive benchmark for evaluating LMM ability to detect synthetic data across 5 modalities with both coarse and fine-grained evaluation\"\n  key_results: \"LMMs show potential as synthetic detectors but reveal significant limitations; large gap between coarse judgment and fine-grained explanation\"\n  limitations: [\"benchmark may not cover all generation methods\", \"multimodal focus may dilute text-specific insights\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== tulchinskii2024_intrinsic_dim.yaml ===\npaper_key: \"tulchinskii2024_intrinsic_dim\"\ntitle: \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\"\nvenue: \"NeurIPS 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"DetectGPT\", \"likelihood-based methods\", \"supervised classifiers\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"cross-domain accuracy\", direction: \"higher_better\"}\n    - {name: \"cross-model accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"multi-language text corpora (English, Chinese, etc.)\", size: \"N/A\"}\n  ablation_dimensions: [\"language\", \"generator model\", \"text domain\", \"writer proficiency level\"]\n  training_recipe: {optimizer: \"N/A (intrinsic dimension estimation)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"geometric / manifold-based detection via intrinsic dimensionality\"\n\npositioning:\n  core_claim: \"Human texts have intrinsic dimensionality ~9 (alphabet languages) / ~7 (Chinese) while AI texts are ~1.5 lower, providing a language-agnostic, domain-invariant detection signal\"\n  key_results: \"Outperforms SOTA in model-agnostic and cross-domain scenarios; stable across languages, domains, and writer proficiency levels\"\n  limitations: [\"computational cost of dimension estimation\", \"may degrade with more human-like models\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== editlens2026.yaml ===\npaper_key: \"editlens2026\"\ntitle: \"EditLens: Quantifying the Extent of AI Editing in Text\"\nvenue: \"ICLR 2026\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"binary AI detectors (GPTZero, etc.)\", \"ternary classifiers\"]\n  metrics:\n    - {name: \"F1 (binary)\", direction: \"higher_better\"}\n    - {name: \"F1 (ternary)\", direction: \"higher_better\"}\n    - {name: \"regression correlation\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"human-AI mixed editing dataset\", size: \"N/A\"}\n    - {name: \"Grammarly editing data\", size: \"N/A\"}\n  ablation_dimensions: [\"editing extent (continuous)\", \"similarity metric choice\", \"human annotation agreement\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"regression-based continuous AI editing quantification\"\n\npositioning:\n  core_claim: \"First to formalize AI editing detection as continuous regression rather than binary/ternary classification, achieving SOTA on both classification and regression tasks\"\n  key_results: \"Binary F1=94.7%, ternary F1=90.4%; validated against human annotators; practical Grammarly case study\"\n  limitations: [\"requires original human text for metric validation\", \"continuous scoring may be hard to interpret\"]\n  relation_to_us: \"competitor\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== cloc2025.yaml ===\npaper_key: \"cloc2025\"\ntitle: \"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\"\nvenue: \"CVPR 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"standard contrastive learning\", \"ordinal regression methods\", \"cross-entropy classification\"]\n  metrics:\n    - {name: \"MAE (mean absolute error)\", direction: \"lower_better\"}\n    - {name: \"classification accuracy\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"Adience (age estimation)\", size: \"N/A\"}\n    - {name: \"Historical Colour Image Dating\", size: \"N/A\"}\n    - {name: \"Knee Osteoarthritis\", size: \"N/A\"}\n    - {name: \"Indian Diabetic Retinopathy Image\", size: \"N/A\"}\n    - {name: \"Breast Carcinoma Subtyping\", size: \"N/A\"}\n  ablation_dimensions: [\"margin type\", \"number of margins\", \"contrastive pair selection\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"contrastive learning for ordinal classification\"\n\npositioning:\n  core_claim: \"Multi-margin N-pair loss enables flexible decision boundaries across adjacent ordinal categories, preserving class ordering while reducing overfitting to training bias\"\n  key_results: \"Outperforms existing ordinal classification methods on 5 real-world datasets\"\n  limitations: [\"image-focused evaluation\", \"limited to moderate number of ordinal classes\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== qurating2024.yaml ===\npaper_key: \"qurating2024\"\ntitle: \"QuRating: Selecting High-Quality Data for Training Language Models\"\nvenue: \"ICML 2024\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"uniform random sampling\", \"perplexity-based filtering\"]\n  metrics:\n    - {name: \"perplexity\", direction: \"lower_better\"}\n    - {name: \"in-context learning accuracy\", direction: \"higher_better\"}\n    - {name: \"training efficiency (steps to target)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"260B token pre-training corpus\", size: \"260B tokens\"}\n    - {name: \"30B token subsets sampled by quality\", size: \"30B tokens\"}\n  ablation_dimensions: [\"quality dimension (writing style, expertise, facts, educational value)\", \"quality threshold\", \"quality-diversity balance\"]\n  training_recipe: {optimizer: \"N/A\", lr: \"N/A\", hardware: \"1.3B parameter LMs\"}\n  method_family: \"LLM-based data quality rating for pre-training data selection\"\n\npositioning:\n  core_claim: \"LLMs can learn quality ratings from pairwise judgments across 4 dimensions, and training on educational-value-selected data matches uniform sampling with 50% fewer steps\"\n  key_results: \"Educational value selection most impactful; quality-diversity balance is critical; 1.3B models trained on 30B quality-filtered tokens\"\n  limitations: [\"limited to 1.3B scale\", \"quality dimensions may not cover all aspects\"]\n  relation_to_us: \"complementary\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c6a8c8f9-bd04-47ec-8935-125c31c56fc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T15:05:48.577Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ey51LpqbQExH6YhYGM8m34`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/distill_tmp && for f in mitchell2023_detectgpt.yaml shi2025_closer_look.yaml wu2025_detection_survey.yaml kirchenbauer2023_watermark.yaml dohmatob2025_strong_collapse.yaml; do echo \"=== $f ===\"; cat \"$f\"; echo; done",
  "description": "Read batch 5 of YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "024297a9-46f4-4be9-a504-fd8e8d9402b7",
  "isSidechain": false,
  "requestId": "req_011CbFvND9YqzLtR9m5JqAvo",
  "type": "assistant",
  "uuid": "3dec890b-cd76-4bfa-9ee0-a26411d43ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ks81FsyhVR44kma1xBmrEZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 57954,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 57954,
          "cache_creation_input_tokens": 2352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2352
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

_source line 48 · 2026-05-21T15:05:48.677Z_

<details><summary>↩ Tool result · `toolu_01Ey51LpqbQExH6YhYGM8m34`</summary>

```text
&lt;persisted-output>
Output too large (31.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/br92ory9z.txt

Preview (first 2KB):
=== mitchell2023_detectgpt.yaml ===
paper_key: "mitchell2023_detectgpt"
title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
venue: "ICML 2023"
full_text_available: false

research:
  baselines: ["likelihood thresholding", "entropy-based methods", "supervised classifiers (RoBERTa)"]
  metrics:
    - {name: "AUROC", direction: "higher_better"}
  datasets:
    - {name: "XSum", size: "N/A"}
    - {name: "SQuAD", size: "N/A"}
    - {name: "WritingPrompts", size: "N/A"}
    - {name: "fake news (GPT-NeoX generated)", size: "N/A"}
  ablation_dimensions: ["perturbation model", "number of perturbations", "source model size"]
  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
  method_family: "zero-shot detection via log probability curvature"

positioning:
  core_claim: "Machine-generated text occupies negative curvature regions of the source model's log probability function, enabling detection without training a classifier"
  key_results: "GPT-NeoX 20B fake news: AUROC 0.81 → 0.95 vs strongest baseline"
  limitations: ["requires perturbation model (slow)", "requires white-box or proxy model access", "short texts challenging"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"

=== shi2025_closer_look.yaml ===
paper_key: "shi2025_closer_look"
title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
venue: "NeurIPS 2025 (Spotlight)"
full_text_available: true

research:
  baselines:
    - "Vanilla replace paradigm (train on synthetic data only)"
    - "Vanilla accumulate-subsample paradigm (uniform subsampling from real + all synthetic)"
    - "Unconditional DDPM generation"
    - "Classifier-Free Guidance (CFG, scale=2)"
  metrics:
    - {name: "Generalization Score (GS)", direction: "higher_better", definition: "Average L2 distance in DINOv2 feature space between each generated image and its nearest training neighbor"}
...
&lt;/persisted-output>
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dec890b-cd76-4bfa-9ee0-a26411d43ee0",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "b4e670c8-08f3-4d2d-b036-527ee558cc73",
  "toolUseResult": {
    "stdout": "=== mitchell2023_detectgpt.yaml ===\npaper_key: \"mitchell2023_detectgpt\"\ntitle: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\nvenue: \"ICML 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"likelihood thresholding\", \"entropy-based methods\", \"supervised classifiers (RoBERTa)\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"XSum\", size: \"N/A\"}\n    - {name: \"SQuAD\", size: \"N/A\"}\n    - {name: \"WritingPrompts\", size: \"N/A\"}\n    - {name: \"fake news (GPT-NeoX generated)\", size: \"N/A\"}\n  ablation_dimensions: [\"perturbation model\", \"number of perturbations\", \"source model size\"]\n  training_recipe: {optimizer: \"N/A (zero-shot)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"zero-shot detection via log probability curvature\"\n\npositioning:\n  core_claim: \"Machine-generated text occupies negative curvature regions of the source model's log probability function, enabling detection without training a classifier\"\n  key_results: \"GPT-NeoX 20B fake news: AUROC 0.81 → 0.95 vs strongest baseline\"\n  limitations: [\"requires perturbation model (slow)\", \"requires white-box or proxy model access\", \"short texts challenging\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== shi2025_closer_look.yaml ===\npaper_key: \"shi2025_closer_look\"\ntitle: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\nvenue: \"NeurIPS 2025 (Spotlight)\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Vanilla replace paradigm (train on synthetic data only)\"\n    - \"Vanilla accumulate-subsample paradigm (uniform subsampling from real + all synthetic)\"\n    - \"Unconditional DDPM generation\"\n    - \"Classifier-Free Guidance (CFG, scale=2)\"\n  metrics:\n    - {name: \"Generalization Score (GS)\", direction: \"higher_better\", definition: \"Average L2 distance in DINOv2 feature space between each generated image and its nearest training neighbor\"}\n    - {name: \"FID (Frechet Inception Distance)\", direction: \"lower_better\", definition: \"InceptionV3-based distribution distance\"}\n    - {name: \"Estimated Entropy (Kozachenko-Leonenko)\", direction: \"higher_better\", definition: \"KL entropy estimator with gamma=1 on DINOv2 features\"}\n  datasets:\n    - {name: \"CIFAR-10\", size: \"32,768 images (32x32)\", note: \"Also used nested subsets: 1024/2048/4096/8192/16384/32768\"}\n    - {name: \"FFHQ\", size: \"8,192 images (downsampled to 32x32)\"}\n    - {name: \"MNIST\", size: \"12,000 images\"}\n  ablation_dimensions:\n    - \"Dataset size (1024 to 32768 in powers of 2)\"\n    - \"Training paradigm (replace vs accumulate-subsample)\"\n    - \"Selection method (Greedy Selection vs Threshold Decay Filter vs vanilla)\"\n    - \"Number of generated candidates (N vs 2N before selection)\"\n    - \"Threshold decay rate alpha (sensitivity analysis)\"\n    - \"Classifier-Free Guidance scale\"\n    - \"Entropy vs variance as correlation target\"\n  training_recipe:\n    model: \"UNet-based DDPM (~16-19M parameters)\"\n    optimizer: \"Adam\"\n    lr: \"1e-4\"\n    weight_decay: \"1e-6\"\n    batch_size: 128\n    precision: \"FP16 mixed\"\n    diffusion_steps: 1000\n    epochs_cifar: 500\n    epochs_ffhq: 1000\n    hardware: \"Single NVIDIA A100 GPU\"\n    feature_extractor: \"DINOv2 (for distance/entropy computation)\"\n    unet_channels_cifar_ffhq: \"[48, 48, 96, 96, 144, 144] with 6 down/up blocks\"\n    unet_channels_mnist: \"[64, 128, 256, 512] with 4 down/up blocks\"\n  method_family: \"Entropy-based data selection for mitigating model collapse in iterative generative training\"\n\npositioning:\n  core_claim: \"Model collapse in diffusion models manifests as a generalization-to-memorization transition driven by training data entropy shrinkage, not just variance collapse — and entropy-based data selection can effectively delay this transition.\"\n  key_results: >\n    Pearson r=0.91 between training data entropy and log(generalization score), dataset-size-independent.\n    FFHQ accumulate-subsample: vanilla FID=75.7 vs Greedy Selection FID=44.7 at iteration 8.\n    MNIST CFG: vanilla CFG FID=66.2 vs CFG+filtering FID=22.4 at iteration 8.\n    Greedy Selection preferentially retains real data (65% real by iteration 8 vs 12.5% uniform baseline).\n  limitations:\n    - \"No rigorous theoretical explanation for why entropy collapses — only empirical demonstration\"\n    - \"Limited to image diffusion models; no validation on language models or discrete diffusion\"\n    - \"Greedy Selection is computationally expensive (quadratic in dataset size)\"\n    - \"Only tested on 32x32 resolution images with relatively small models (~16-19M params)\"\n    - \"No formal analysis of how many iterations can be sustained before memorization\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: >\n    Opens with the practical inevitability of synthetic data contamination: as diffusion models flood\n    the internet with generated content, future training sets will inevitably contain synthetic data,\n    creating a self-consuming loop. This is a real-world crisis framing, not hypothetical.\n  tension: >\n    Existing perspectives on model collapse (variance shrinkage, distribution shift) are shown to be\n    theoretically valid but practically insufficient — variance collapse requires \"an extremely large\n    number of iterations\" to manifest, making it \"rarely a practical concern.\" This creates a gap:\n    the community has mathematical frameworks that don't explain what practitioners actually observe.\n  key_insight: >\n    Revealed in paragraph 3 of the intro: the transition from generalization to memorization is the\n    true practical manifestation of collapse. Models don't just get worse — they specifically lose the\n    ability to generate novel content and start copying training data. The entropy of the training set\n    (not the model) is the key diagnostic signal, with r=0.91 correlation to generalizability.\n  argument_chain: >\n    Real-world synthetic data contamination is inevitable →\n    Existing collapse perspectives miss practical manifestations →\n    We observe a generalization-to-memorization transition (Finding I) →\n    Training data entropy shrinks across iterations (Finding II) →\n    Entropy strongly correlates with generalization capability (Finding III, r=0.91) →\n    Entropy-based data selection preserves diversity and delays collapse →\n    Validated across 3 datasets, 2 paradigms, with CFG extension\n  contribution_framing: >\n    Three numbered contributions, each one sentence. Pattern: identify phenomenon → investigate\n    driving factor → propose and validate mitigation. Clean problem-insight-solution structure.\n    Contributions are framed as empirical discoveries rather than theoretical claims, matching the\n    paper's predominantly experimental nature.\n  intro_structure: >\n    3 paragraphs + \"Our Contributions\" subsection.\n    P1: Problem context — synthetic data proliferation and the self-consuming loop threat.\n    P2: Critique of existing perspectives — variance collapse and distribution shift are insufficient.\n    P3: Their perspective — generalization-to-memorization transition, entropy as diagnostic, proposed mitigation.\n    Contributions: 3 numbered items following identify-investigate-propose pattern.\n  notable_technique: >\n    The paper uses a \"practical insufficiency\" argument to distinguish itself from prior theoretical\n    work. Instead of claiming predecessors are wrong, it argues they are right but miss what matters\n    in practice. This is a diplomatically effective positioning that avoids direct conflict while\n    establishing clear novelty. The visual pairing of generated images with their nearest training\n    neighbors (Figure 2 left) makes the abstract concept of \"memorization\" viscerally obvious.\n\nfigures:\n  figure_count: 9\n  figure1:\n    type: \"method_overview\"\n    description: >\n      Three-row pipeline diagram. Top row (green background): \"Collapse Iteration\" showing the\n      replace paradigm where D1 → Training → M1 → Sampling → D2 → Training → M2 → ... → Dn.\n      Middle row (blue background): \"Mitigated Iteration\" showing the accumulate-subsample paradigm\n      with a pie chart merging real data and previously generated data, plus a funnel icon for\n      \"Selection\" before constructing D2. Bottom right (orange background): \"Evolution\" panel showing\n      pairs of generated images (top) and their nearest training counterparts (bottom) at Iterations\n      1, 3, and n, with a horizontal arrow from \"Generalization\" to \"Memorization\" and \"Degradation\"\n      labels between iteration pairs.\n    narrative_role: >\n      Serves as the roadmap for the entire paper: defines the two paradigms (collapse vs mitigated),\n      introduces the selection intervention, and previews the core finding (generalization-to-memorization\n      transition) — all in one figure. The reader immediately grasps the problem, the setup, and the\n      paper's contribution.\n    design_elements:\n      - \"Color-coded rows: green=collapse, blue=mitigated, orange=evolution\"\n      - \"Pipeline arrows connecting dataset→model→sampling→dataset\"\n      - \"Pie chart for data composition (real vs synthetic)\"\n      - \"Funnel icon for selection step\"\n      - \"Real face image pairs showing degradation progression\"\n      - \"Horizontal arrow from Generalization to Memorization\"\n    visual_style: >\n      Clean horizontal flow with three visually distinct rows. Pastel background colors (green,\n      blue, orange) separate conceptual layers. Neural network icons for models, cylindrical icons\n      for datasets. The bottom-right evolution panel uses real face images to ground the abstract\n      pipeline in concrete visual evidence. Legend in bottom-left defines notation.\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"qualitative_comparison + line_plot\"\n      what_compared: \"Generated images vs their nearest training neighbors across iterations 1, 3, 8; GS decay curves for 6 dataset sizes\"\n      how_gain_highlighted: \"Left panel shows progressive visual convergence (memorization). Right panel uses color-coded curves with labeled 'Generalization Regime' and 'Memorization Regime' regions.\"\n      design_note: >\n        Powerful dual-panel design: qualitative evidence (left) paired with quantitative curves (right).\n        The image grid makes memorization viscerally obvious — generated faces become identical to\n        training neighbors. The right panel uses a horizontal dashed line to separate regimes and\n        annotated text labels for the two regions. Six dataset sizes in distinct colors show the\n        dataset-size effect on collapse rate. Log-scale y-axis on GS.\n    - figure_id: \"Figure 4a\"\n      viz_type: \"scatter\"\n      what_compared: \"Estimated entropy (x-axis) vs generalization score (y-axis, log scale) across 6 dataset sizes\"\n      how_gain_highlighted: \"Red dashed regression line through all points from all dataset sizes, demonstrating r=0.91 universal correlation. Points from different sizes align on the same line.\"\n      design_note: >\n        The key evidence figure. Log-scale y-axis linearizes the relationship. Color coding by dataset\n        size (same palette as Figure 2) shows that different sizes fall on the same line — establishing\n        a dataset-size-independent law. Clean white background, no clutter. Contrast with Figure 4b\n        (variance) where the correlation is visibly weaker.\n    - figure_id: \"Figure 5\"\n      viz_type: \"multi_panel_line_plot\"\n      what_compared: \"Generalization Score over iterations for vanilla vs Greedy Selection vs Threshold Decay Filter, across datasets and paradigms\"\n      how_gain_highlighted: \"Three lines per panel; selection methods consistently above vanilla, showing sustained higher GS\"\n      design_note: \"6 subfigures in a grid (datasets x paradigms). Independent y-axes per subfigure to show relative improvement. Clean legend with three line styles.\"\n    - figure_id: \"Figure 6\"\n      viz_type: \"multi_panel_line_plot\"\n      what_compared: \"FID over iterations for vanilla vs Greedy Selection vs Threshold Decay Filter\"\n      how_gain_highlighted: \"Selection methods consistently lower FID curves than vanilla across all panels\"\n      design_note: \"Same grid layout as Figure 5 for parallel reading. FID improvement most dramatic on accumulate-subsample paradigm.\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"stacked_bar_chart_with_overlay_line\"\n      what_compared: \"Proportion of selected images from each iteration source; blue bars = real data proportion vs red 1/n baseline line\"\n      how_gain_highlighted: \"Blue bars (real data fraction) dramatically exceed the red 1/n line, especially in later iterations — the method naturally discovers that real data is more diverse\"\n      design_note: >\n        Insightful visualization of an emergent behavior: the selection algorithm was not told to prefer\n        real data, but the entropy-maximizing objective naturally selects more real images as synthetic\n        data clusters tighten. The stacked bars show composition while the overlay line shows the\n        null expectation. Multiple panels for different datasets/methods.\n    - figure_id: \"Figure 9\"\n      viz_type: \"qualitative_comparison + line_plot\"\n      what_compared: \"MNIST generation: unconditional (FID=74.4) vs CFG (FID=66.2) vs CFG+filtering (FID=22.4)\"\n      how_gain_highlighted: \"Side-by-side digit grids show dramatic quality improvement; entropy plot shows filtering maintains diversity that CFG alone destroys\"\n      design_note: \"Extension experiment demonstrating generality beyond unconditional setting. The 3x improvement in FID (66.2→22.4) is a compelling headline number.\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot + 2D_scatter_projection\"\n      dimensions_varied: [\"iteration number\", \"dataset entropy\"]\n      design_note: >\n        Three-panel figure. Left: entropy decay curves over iterations for different dataset sizes.\n        Middle and Right: 2D SVD projections of data distribution at iteration 1 (spread) vs\n        iteration 21 (collapsed into tight clusters). The SVD projections make entropy collapse\n        visually intuitive — you can see the distribution concentrating.\n    - figure_id: \"Figure 7\"\n      viz_type: \"multi_panel_line_plot\"\n      dimensions_varied: [\"selection method\", \"training paradigm\", \"dataset\"]\n      design_note: \"Shows that selection methods maintain higher entropy across iterations. Same grid layout as Figures 5-6 for parallel comparison. Entropy serves as the mechanistic explanation for why GS and FID improve.\"\n    - figure_id: \"Figure 4b\"\n      viz_type: \"scatter\"\n      dimensions_varied: [\"variance vs generalization score as alternative to entropy\"]\n      design_note: \"Deliberately placed next to Figure 4a to show that variance is a weaker predictor than entropy. The scatter is visibly more dispersed, making the entropy superiority obvious without needing statistics.\"\n  figure_narrative_role: >\n    Figure 1 (pipeline overview + generalization-to-memorization preview) →\n    Figure 2 (Finding I: generalization-to-memorization transition, qualitative + quantitative) →\n    Figure 3 (Finding II: entropy shrinkage + distribution collapse visualization) →\n    Figure 4 (Finding III: entropy-GS correlation, the key evidence; entropy vs variance comparison) →\n    Figures 5-7 (Mitigation results: GS/FID/entropy improvements with selection methods, parallel grid layout) →\n    Figure 8 (Mechanistic insight: selection naturally prefers real data) →\n    Figure 9 (Extension: CFG setting on MNIST).\n    The flow follows a clear discover-understand-mitigate-extend arc.\n\ntables:\n  table_count: 0\n  main_result_table:\n    table_id: \"N/A\"\n    row_axis: \"N/A\"\n    col_axis: \"N/A\"\n    row_organization: \"N/A\"\n    col_organization: \"N/A\"\n    highlight_strategy: \"N/A\"\n    statistical_reporting: \"N/A\"\n    num_baselines: 0\n    design_note: >\n      Notable design choice: this paper has NO tables in the main text. All quantitative results\n      are presented as line plots (Figures 5-7) and scatter plots (Figure 4). This is unusual for\n      a NeurIPS paper but works because the key story is about trends over iterations (naturally\n      suited to line plots) rather than point comparisons across methods. The absence of tables\n      keeps the paper visually unified around its \"curves over iterations\" motif.\n  ablation_tables:\n    - table_id: \"N/A (Appendix C)\"\n      what_varied: [\"Number of generated candidates (N vs 2N)\", \"Threshold decay rate alpha\"]\n      variation_style: \"Presented as figures/plots rather than tables\"\n      design_note: \"Ablations are in the appendix and use the same figure-based presentation as the main paper.\"\n  supplementary_tables:\n    in_appendix: false\n    content: \"No tables even in appendix; all results presented as multi-panel line plots and scatter plots\"\n    reason: >\n      The paper's central argument is about trajectories over iterations, not about static\n      method-vs-method comparisons. Line plots naturally show this temporal evolution, making\n      tables unnecessary. The only potential table content (FID/GS at specific iterations) is\n      embedded in figure panels instead.\n\n=== wu2025_detection_survey.yaml ===\npaper_key: \"wu2025_detection_survey\"\ntitle: \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\"\nvenue: \"Computational Linguistics, Vol. 51, Issue 1, 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"N/A (survey paper)\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"F1\", direction: \"higher_better\"}\n    - {name: \"TPR@FPR\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"various detection benchmarks surveyed\", size: \"N/A\"}\n  ablation_dimensions: [\"method family (watermarking/statistical/neural/human-assisted)\", \"evaluation setting (in-domain/cross-domain/cross-model)\", \"attack type\"]\n  training_recipe: {optimizer: \"N/A (survey)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"survey covering watermarking, statistics-based, neural-based, and human-assisted detection\"\n\npositioning:\n  core_claim: \"Comprehensive taxonomy of LLM text detection methods organized into 4 families, with analysis of challenges including OOD generalization, adversarial attacks, and evaluation framework deficiencies\"\n  key_results: \"Identifies key gaps: OOD robustness, attack resilience, real-world data handling, lack of standardized evaluation\"\n  limitations: [\"survey scope limited to text modality\", \"rapidly evolving field\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== kirchenbauer2023_watermark.yaml ===\npaper_key: \"kirchenbauer2023_watermark\"\ntitle: \"A Watermark for Large Language Models\"\nvenue: \"ICML 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"no watermark baseline\", \"post-hoc detection methods\"]\n  metrics:\n    - {name: \"p-value (watermark detection)\", direction: \"lower_better\"}\n    - {name: \"text quality (perplexity)\", direction: \"lower_better\"}\n    - {name: \"BLEU/ROUGE (quality preservation)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"OPT model outputs\", size: \"N/A\"}\n  ablation_dimensions: [\"green list fraction\", \"watermark strength (delta)\", \"text length\", \"model size\"]\n  training_recipe: {optimizer: \"N/A (decoding-time watermark)\", lr: \"N/A\", hardware: \"OPT multi-billion parameter models\"}\n  method_family: \"statistical watermarking via green token promotion\"\n\npositioning:\n  core_claim: \"Invisible watermarks can be embedded in LLM outputs by promoting 'green' tokens during generation, detectable from short spans without model access, with negligible quality impact\"\n  key_results: \"Algorithmically detectable watermark with interpretable p-values; tested on OPT models; information-theoretic sensitivity analysis\"\n  limitations: [\"vulnerable to paraphrasing attacks\", \"requires control of generation process\", \"green token bias may affect specific domains\"]\n  relation_to_us: \"orthogonal\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== dohmatob2025_strong_collapse.yaml ===\npaper_key: \"dohmatob2025_strong_collapse\"\ntitle: \"Strong Model Collapse\"\nvenue: \"ICLR 2025 Spotlight\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Training on pure real/original data (no synthetic contamination)\"\n    - \"Training on pure synthetic data\"\n    - \"Mixed real+synthetic data with various proportions p2\"\n    - \"Weighted single-step mixing (data weighting strategies)\"\n    - \"Dynamic multi-step mixing\"\n  metrics:\n    - {name: \"test error (E_test on real distribution)\", direction: \"lower_better\"}\n    - {name: \"test loss (cross-entropy for language modeling)\", direction: \"lower_better\"}\n    - {name: \"collapse term zeta (excess error from synthetic data)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Gaussian synthetic data (random projections)\", size: \"n=500 samples, variable d\"}\n    - {name: \"MNIST\", size: \"standard 60K/10K, used for regression with two-layer networks\"}\n    - {name: \"BabiStories\", size: \"reproduction of TinyStories via Mixtral-8x7B; token counts up to ~3e10\"}\n  ablation_dimensions:\n    - \"synthetic data proportion p2 (fraction of training data that is synthetic)\"\n    - \"model size m (network width for random projections, depth/layers for GPT-2)\"\n    - \"synthetic data quality c^2 (distribution mismatch between real and synthetic)\"\n    - \"total training set size n (scaling behavior)\"\n    - \"parametrization rate psi=m/n (under- vs over-parameterized regime)\"\n    - \"interpolation threshold crossing (m=n boundary)\"\n  training_recipe:\n    optimizer: \"not explicitly detailed in accessible text; standard SGD/Adam for neural network experiments\"\n    lr: \"not explicitly detailed in accessible text\"\n    hardware: \"not explicitly detailed in accessible text\"\n    details: \"Random projections on Gaussian data (n=500); two-layer neural networks on MNIST (width m=2000); GPT-2 models (12-layer) on BabiStories; experiments vary p2 and model size systematically\"\n  method_family: \"theoretical analysis of model collapse via bias-variance decomposition and operator-valued free probability theory\"\n\npositioning:\n  core_claim: \"Model collapse persists even when mixing real and synthetic data, as long as the fraction of synthetic data does not vanish asymptotically — establishing a 'strong' form of collapse where no fixed-proportion mixing strategy can prevent performance degradation, and larger models amplify this effect in the under-parameterized regime.\"\n  key_results: \"E_test = B + V + zeta decomposition where zeta is irreducible collapse term; in scaling laws regime (phi->0+), zeta ~ p2^2 * tr(Delta) remains bounded unless p2->0; 1% synthetic data sufficient to cause collapse plateau; larger models amplify collapse when real/synthetic distributions differ significantly; double-descent pattern where over-parameterized models (past m=n threshold) partially mitigate but do not eliminate collapse\"\n  limitations:\n    - \"Theory focuses on supervised regression with label shifts — does not directly model generative/autoregressive training\"\n    - \"Random projections model is a simplified approximation of actual neural networks (linearized regime)\"\n    - \"Gaussian feature distribution assumption with diagonal covariance matrices\"\n    - \"Proportionate scaling limit assumes d,n,m -> infinity with fixed ratios\"\n    - \"For fully-trained neural networks the theory does not directly apply, though authors anticipate general trends hold\"\n    - \"Does not address mitigation via data filtering, detection, or curation (only analyzes mixing/weighting)\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the observation that AI-generated content is increasingly contaminating web training corpora, and asks whether the standard approach of scaling up training data can still work when synthetic data is inevitably mixed in. Frames this as a fundamental threat to the scaling laws paradigm.\"\n  tension: \"Prior model collapse work showed degradation in recursive (iterative) generation settings, but left open whether strategic mixing of real and synthetic data could prevent collapse. The natural hope is that diluting synthetic data with sufficient real data would restore normal scaling — this paper proves that hope is false.\"\n  key_insight: \"The key insight is the bias-variance decomposition E_test = B + V + zeta, where zeta is an irreducible collapse term that persists as long as the synthetic data fraction p2 remains fixed (non-vanishing). This means no matter how much you scale total data n, the collapse term does not vanish — you must asymptotically eliminate synthetic data proportion entirely. Revealed through Theorem 1 (linear models) and Theorem 2 (random projections/neural approximation).\"\n  argument_chain: \"problem (synthetic data contamination is unavoidable) -> question (can mixing/scaling overcome it?) -> theory (bias-variance decomposition reveals irreducible collapse term zeta) -> scaling law implication (zeta plateaus unless p2->0) -> model size analysis (bigger models amplify collapse below interpolation threshold) -> double-descent (reversal above interpolation threshold but not elimination) -> data mixing strategies (weighted/dynamic mixing cannot fix fundamental issue) -> experimental validation (random projections, MNIST, GPT-2 on BabiStories confirm theory)\"\n  contribution_framing: \"Two main results explicitly labeled: Result #1 (Strong Model Collapse) — collapse persists with any fixed synthetic fraction; Result #2 (Model Size and Model Collapse) — bigger models amplify collapse except past interpolation threshold. Followed by experimental validation across three settings (toy, MNIST, language modeling).\"\n  intro_structure: \"~5 paragraphs: P1=hook (AI-generated content proliferating in training data), P2=problem framing (model collapse definition and prior work), P3=research questions (can mixing help? does model size matter?), P4=main results summary (Result #1 and #2), P5=experimental validation overview and paper organization. Section 1.1 details contributions, Section 1.2 covers related work.\"\n  notable_technique: \"The 'strong' vs 'weak' framing is a powerful rhetorical device — it redefines the conversation by showing that even the most optimistic scenario (strategic mixing with fresh real data) still fails. The Pareto diagram (Figure 1) is an effective visual argument that immediately conveys the tradeoff. The paper also uses the mathematical elegance of the exact bias-variance-collapse decomposition to make a clean, falsifiable theoretical claim rather than just empirical observations.\"\n\nfigures:\n  figure_count: 8\n  figure1:\n    type: \"motivation\"\n    description: \"Pareto diagram showing test error on real data distribution: training on mixed data (y-axis) vs training on real data only (x-axis). Points colored by synthetic data quality (c^2) for a random projections model with n=500. Lines show Pareto frontiers for different quality levels. Demonstrates that mixed training always incurs excess error (points above diagonal) and the tradeoff worsens with lower synthetic data quality.\"\n    narrative_role: \"Immediately establishes the core claim visually — no combination of model size and data mixing achieves the performance of training on real data alone. Sets up the entire paper's argument in one figure.\"\n    design_elements: [\"Pareto frontier visualization\", \"diagonal reference line (ideal = no collapse)\", \"colorbar for parametrization rate psi=m/n\", \"multiple quality levels compared\"]\n    visual_style: \"Scatter plot with Pareto frontiers; colorbar encoding model size; clean 2D layout that maps directly to the central question (mixed vs real-only performance)\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Strong model collapse in classical linear model — empirical confirmation of Corollary 1. Shows test error vs training set size for various synthetic data proportions p2, demonstrating that even small p2 causes scaling law plateau.\"\n      how_gain_highlighted: \"Direct comparison of p2=0 (ideal scaling law) vs p2>0 curves; the plateau/saturation effect is visually stark\"\n      design_note: \"Log-log scale makes power-law behavior linear and the collapse plateau clearly visible as a horizontal asymptote; multiple p2 values show graduated severity\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Impact of model size (network width m) on model collapse for various data quality levels c^2 and mixing ratios p2\"\n      how_gain_highlighted: \"Shows test error as function of model size, revealing the double-descent pattern: collapse worsens up to interpolation threshold m=n, then partially reverses\"\n      design_note: \"Multiple panels for different c^2 values; vertical line or inflection at m=n marks the interpolation threshold — the key theoretical prediction\"\n    - figure_id: \"Figure 7\"\n      viz_type: \"line_plot\"\n      what_compared: \"Model collapse on MNIST with two-layer neural network (width m=2000) as function of synthetic data proportion\"\n      how_gain_highlighted: \"Validates that theoretical predictions from random projections model transfer to real image data\"\n      design_note: \"Bridges the theory-practice gap by testing on a real dataset\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"line_plot\"\n      what_compared: \"GPT-2 (12-layer) language model on BabiStories: (Left) test loss vs number of training tokens for various synthetic data proportions p2; (Right) test loss vs model depth showing larger models initially better but eventually worse\"\n      how_gain_highlighted: \"Left panel shows clear scaling law plateau with synthetic contamination; Right panel shows the depth-dependent collapse reversal predicted by theory\"\n      design_note: \"Most impactful experimental figure — demonstrates",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/br92ory9z.txt",
    "persistedOutputSize": 32167
  },
  "sourceToolAssistantUUID": "3dec890b-cd76-4bfa-9ee0-a26411d43ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "b4e670c8-08f3-4d2d-b036-527ee558cc73",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Tool call

_source line 51 · 2026-05-21T15:05:51.923Z_

<details open><summary>🔧 Tool call — Read · `toolu_017tTMN3TpkDd5cuxH9KaQbW`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/br92ory9z.txt",
  "offset": 0,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4e670c8-08f3-4d2d-b036-527ee558cc73",
  "isSidechain": false,
  "requestId": "req_011CbFvNdABBZKsdHE3MjAEZ",
  "type": "assistant",
  "uuid": "0bfda484-c9b9-4f25-a895-eac85b35b93f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzA9tisDQgzV2Um48ad9rm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1011,
      "cache_read_input_tokens": 60306,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 60306,
          "cache_creation_input_tokens": 1011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1011
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

_source line 52 · 2026-05-21T15:05:52.376Z_

<details><summary>↩ Tool result · `toolu_017tTMN3TpkDd5cuxH9KaQbW`</summary>

```text
0	=== mitchell2023_detectgpt.yaml ===
1	paper_key: "mitchell2023_detectgpt"
2	title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
3	venue: "ICML 2023"
4	full_text_available: false
5	
6	research:
7	  baselines: ["likelihood thresholding", "entropy-based methods", "supervised classifiers (RoBERTa)"]
8	  metrics:
9	    - {name: "AUROC", direction: "higher_better"}
10	  datasets:
11	    - {name: "XSum", size: "N/A"}
12	    - {name: "SQuAD", size: "N/A"}
13	    - {name: "WritingPrompts", size: "N/A"}
14	    - {name: "fake news (GPT-NeoX generated)", size: "N/A"}
15	  ablation_dimensions: ["perturbation model", "number of perturbations", "source model size"]
16	  training_recipe: {optimizer: "N/A (zero-shot)", lr: "N/A", hardware: "N/A"}
17	  method_family: "zero-shot detection via log probability curvature"
18	
19	positioning:
20	  core_claim: "Machine-generated text occupies negative curvature regions of the source model's log probability function, enabling detection without training a classifier"
21	  key_results: "GPT-NeoX 20B fake news: AUROC 0.81 → 0.95 vs strongest baseline"
22	  limitations: ["requires perturbation model (slow)", "requires white-box or proxy model access", "short texts challenging"]
23	  relation_to_us: "foundation"
24	
25	narrative: "N/A"
26	figures: "N/A"
27	tables: "N/A"
28	
29	=== shi2025_closer_look.yaml ===
30	paper_key: "shi2025_closer_look"
31	title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
32	venue: "NeurIPS 2025 (Spotlight)"
33	full_text_available: true
34	
35	research:
36	  baselines:
37	    - "Vanilla replace paradigm (train on synthetic data only)"
38	    - "Vanilla accumulate-subsample paradigm (uniform subsampling from real + all synthetic)"
39	    - "Unconditional DDPM generation"
40	    - "Classifier-Free Guidance (CFG, scale=2)"
41	  metrics:
42	    - {name: "Generalization Score (GS)", direction: "higher_better", definition: "Average L2 distance in DINOv2 feature space between each generated image and its nearest training neighbor"}
43	    - {name: "FID (Frechet Inception Distance)", direction: "lower_better", definition: "InceptionV3-based distribution distance"}
44	    - {name: "Estimated Entropy (Kozachenko-Leonenko)", direction: "higher_better", definition: "KL entropy estimator with gamma=1 on DINOv2 features"}
45	  datasets:
46	    - {name: "CIFAR-10", size: "32,768 images (32x32)", note: "Also used nested subsets: 1024/2048/4096/8192/16384/32768"}
47	    - {name: "FFHQ", size: "8,192 images (downsampled to 32x32)"}
48	    - {name: "MNIST", size: "12,000 images"}
49	  ablation_dimensions:
50	    - "Dataset size (1024 to 32768 in powers of 2)"
51	    - "Training paradigm (replace vs accumulate-subsample)"
52	    - "Selection method (Greedy Selection vs Threshold Decay Filter vs vanilla)"
53	    - "Number of generated candidates (N vs 2N before selection)"
54	    - "Threshold decay rate alpha (sensitivity analysis)"
55	    - "Classifier-Free Guidance scale"
56	    - "Entropy vs variance as correlation target"
57	  training_recipe:
58	    model: "UNet-based DDPM (~16-19M parameters)"
59	    optimizer: "Adam"
60	    lr: "1e-4"
61	    weight_decay: "1e-6"
62	    batch_size: 128
63	    precision: "FP16 mixed"
64	    diffusion_steps: 1000
65	    epochs_cifar: 500
66	    epochs_ffhq: 1000
67	    hardware: "Single NVIDIA A100 GPU"
68	    feature_extractor: "DINOv2 (for distance/entropy computation)"
69	    unet_channels_cifar_ffhq: "[48, 48, 96, 96, 144, 144] with 6 down/up blocks"
70	    unet_channels_mnist: "[64, 128, 256, 512] with 4 down/up blocks"
71	  method_family: "Entropy-based data selection for mitigating model collapse in iterative generative training"
72	
73	positioning:
74	  core_claim: "Model collapse in diffusion models manifests as a generalization-to-memorization transition driven by training data entropy shrinkage, not just variance collapse — and entropy-based data selection can effectively delay this transition."
75	  key_results: >
76	    Pearson r=0.91 between training data entropy and log(generalization score), dataset-size-independent.
77	    FFHQ accumulate-subsample: vanilla FID=75.7 vs Greedy Selection FID=44.7 at iteration 8.
78	    MNIST CFG: vanilla CFG FID=66.2 vs CFG+filtering FID=22.4 at iteration 8.
79	    Greedy Selection preferentially retains real data (65% real by iteration 8 vs 12.5% uniform baseline).
80	  limitations:
81	    - "No rigorous theoretical explanation for why entropy collapses — only empirical demonstration"
82	    - "Limited to image diffusion models; no validation on language models or discrete diffusion"
83	    - "Greedy Selection is computationally expensive (quadratic in dataset size)"
84	    - "Only tested on 32x32 resolution images with relatively small models (~16-19M params)"
85	    - "No formal analysis of how many iterations can be sustained before memorization"
86	  relation_to_us: "foundation"
87	
88	narrative:
89	  story_type: "突破局限型"
90	  hook: >
91	    Opens with the practical inevitability of synthetic data contamination: as diffusion models flood
92	    the internet with generated content, future training sets will inevitably contain synthetic data,
93	    creating a self-consuming loop. This is a real-world crisis framing, not hypothetical.
94	  tension: >
95	    Existing perspectives on model collapse (variance shrinkage, distribution shift) are shown to be
96	    theoretically valid but practically insufficient — variance collapse requires "an extremely large
97	    number of iterations" to manifest, making it "rarely a practical concern." This creates a gap:
98	    the community has mathematical frameworks that don't explain what practitioners actually observe.
99	  key_insight: >
100	    Revealed in paragraph 3 of the intro: the transition from generalization to memorization is the
101	    true practical manifestation of collapse. Models don't just get worse — they specifically lose the
102	    ability to generate novel content and start copying training data. The entropy of the training set
103	    (not the model) is the key diagnostic signal, with r=0.91 correlation to generalizability.
104	  argument_chain: >
105	    Real-world synthetic data contamination is inevitable →
106	    Existing collapse perspectives miss practical manifestations →
107	    We observe a generalization-to-memorization transition (Finding I) →
108	    Training data entropy shrinks across iterations (Finding II) →
109	    Entropy strongly correlates with generalization capability (Finding III, r=0.91) →
110	    Entropy-based data selection preserves diversity and delays collapse →
111	    Validated across 3 datasets, 2 paradigms, with CFG extension
112	  contribution_framing: >
113	    Three numbered contributions, each one sentence. Pattern: identify phenomenon → investigate
114	    driving factor → propose and validate mitigation. Clean problem-insight-solution structure.
115	    Contributions are framed as empirical discoveries rather than theoretical claims, matching the
116	    paper's predominantly experimental nature.
117	  intro_structure: >
118	    3 paragraphs + "Our Contributions" subsection.
119	    P1: Problem context — synthetic data proliferation and the self-consuming loop threat.
120	    P2: Critique of existing perspectives — variance collapse and distribution shift are insufficient.
121	    P3: Their perspective — generalization-to-memorization transition, entropy as diagnostic, proposed mitigation.
122	    Contributions: 3 numbered items following identify-investigate-propose pattern.
123	  notable_technique: >
124	    The paper uses a "practical insufficiency" argument to distinguish itself from prior theoretical
125	    work. Instead of claiming predecessors are wrong, it argues they are right but miss what matters
126	    in practice. This is a diplomatically effective positioning that avoids direct conflict while
127	    establishing clear novelty. The visual pairing of generated images with their nearest training
128	    neighbors (Figure 2 left) makes the abstract concept of "memorization" viscerally obvious.
129	
130	figures:
131	  figure_count: 9
132	  figure1:
133	    type: "method_overview"
134	    description: >
135	      Three-row pipeline diagram. Top row (green background): "Collapse Iteration" showing the
136	      replace paradigm where D1 → Training → M1 → Sampling → D2 → Training → M2 → ... → Dn.
137	      Middle row (blue background): "Mitigated Iteration" showing the accumulate-subsample paradigm
138	      with a pie chart merging real data and previously generated data, plus a funnel icon for
139	      "Selection" before constructing D2. Bottom right (orange background): "Evolution" panel showing
140	      pairs of generated images (top) and their nearest training counterparts (bottom) at Iterations
141	      1, 3, and n, with a horizontal arrow from "Generalization" to "Memorization" and "Degradation"
142	      labels between iteration pairs.
143	    narrative_role: >
144	      Serves as the roadmap for the entire paper: defines the two paradigms (collapse vs mitigated),
145	      introduces the selection intervention, and previews the core finding (generalization-to-memorization
146	      transition) — all in one figure. The reader immediately grasps the problem, the setup, and the
147	      paper's contribution.
148	    design_elements:
149	      - "Color-coded rows: green=collapse, blue=mitigated, orange=evolution"
150	      - "Pipeline arrows connecting dataset→model→sampling→dataset"
151	      - "Pie chart for data composition (real vs synthetic)"
152	      - "Funnel icon for selection step"
153	      - "Real face image pairs showing degradation progression"
154	      - "Horizontal arrow from Generalization to Memorization"
155	    visual_style: >
156	      Clean horizontal flow with three visually distinct rows. Pastel background colors (green,
157	      blue, orange) separate conceptual layers. Neural network icons for models, cylindrical icons
158	      for datasets. The bottom-right evolution panel uses real face images to ground the abstract
159	      pipeline in concrete visual evidence. Legend in bottom-left defines notation.
160	  result_figures:
161	    - figure_id: "Figure 2"
162	      viz_type: "qualitative_comparison + line_plot"
163	      what_compared: "Generated images vs their nearest training neighbors across iterations 1, 3, 8; GS decay curves for 6 dataset sizes"
164	      how_gain_highlighted: "Left panel shows progressive visual convergence (memorization). Right panel uses color-coded curves with labeled 'Generalization Regime' and 'Memorization Regime' regions."
165	      design_note: >
166	        Powerful dual-panel design: qualitative evidence (left) paired with quantitative curves (right).
167	        The image grid makes memorization viscerally obvious — generated faces become identical to
168	        training neighbors. The right panel uses a horizontal dashed line to separate regimes and
169	        annotated text labels for the two regions. Six dataset sizes in distinct colors show the
170	        dataset-size effect on collapse rate. Log-scale y-axis on GS.
171	    - figure_id: "Figure 4a"
172	      viz_type: "scatter"
173	      what_compared: "Estimated entropy (x-axis) vs generalization score (y-axis, log scale) across 6 dataset sizes"
174	      how_gain_highlighted: "Red dashed regression line through all points from all dataset sizes, demonstrating r=0.91 universal correlation. Points from different sizes align on the same line."
175	      design_note: >
176	        The key evidence figure. Log-scale y-axis linearizes the relationship. Color coding by dataset
177	        size (same palette as Figure 2) shows that different sizes fall on the same line — establishing
178	        a dataset-size-independent law. Clean white background, no clutter. Contrast with Figure 4b
179	        (variance) where the correlation is visibly weaker.
180	    - figure_id: "Figure 5"
181	      viz_type: "multi_panel_line_plot"
182	      what_compared: "Generalization Score over iterations for vanilla vs Greedy Selection vs Threshold Decay Filter, across datasets and paradigms"
183	      how_gain_highlighted: "Three lines per panel; selection methods consistently above vanilla, showing sustained higher GS"
184	      design_note: "6 subfigures in a grid (datasets x paradigms). Independent y-axes per subfigure to show relative improvement. Clean legend with three line styles."
185	    - figure_id: "Figure 6"
186	      viz_type: "multi_panel_line_plot"
187	      what_compared: "FID over iterations for vanilla vs Greedy Selection vs Threshold Decay Filter"
188	      how_gain_highlighted: "Selection methods consistently lower FID curves than vanilla across all panels"
189	      design_note: "Same grid layout as Figure 5 for parallel reading. FID improvement most dramatic on accumulate-subsample paradigm."
190	    - figure_id: "Figure 8"
191	      viz_type: "stacked_bar_chart_with_overlay_line"
192	      what_compared: "Proportion of selected images from each iteration source; blue bars = real data proportion vs red 1/n baseline line"
193	      how_gain_highlighted: "Blue bars (real data fraction) dramatically exceed the red 1/n line, especially in later iterations — the method naturally discovers that real data is more diverse"
194	      design_note: >
195	        Insightful visualization of an emergent behavior: the selection algorithm was not told to prefer
196	        real data, but the entropy-maximizing objective naturally selects more real images as synthetic
197	        data clusters tighten. The stacked bars show composition while the overlay line shows the
198	        null expectation. Multiple panels for different datasets/methods.
199	    - figure_id: "Figure 9"
200	      viz_type: "qualitative_comparison + line_plot"
201	      what_compared: "MNIST generation: unconditional (FID=74.4) vs CFG (FID=66.2) vs CFG+filtering (FID=22.4)"
202	      how_gain_highlighted: "Side-by-side digit grids show dramatic quality improvement; entropy plot shows filtering maintains diversity that CFG alone destroys"
203	      design_note: "Extension experiment demonstrating generality beyond unconditional setting. The 3x improvement in FID (66.2→22.4) is a compelling headline number."
204	  ablation_figures:
205	    - figure_id: "Figure 3"
206	      viz_type: "line_plot + 2D_scatter_projection"
207	      dimensions_varied: ["iteration number", "dataset entropy"]
208	      design_note: >
209	        Three-panel figure. Left: entropy decay curves over iterations for different dataset sizes.
210	        Middle and Right: 2D SVD projections of data distribution at iteration 1 (spread) vs
211	        iteration 21 (collapsed into tight clusters). The SVD projections make entropy collapse
212	        visually intuitive — you can see the distribution concentrating.
213	    - figure_id: "Figure 7"
214	      viz_type: "multi_panel_line_plot"
215	      dimensions_varied: ["selection method", "training paradigm", "dataset"]
216	      design_note: "Shows that selection methods maintain higher entropy across iterations. Same grid layout as Figures 5-6 for parallel comparison. Entropy serves as the mechanistic explanation for why GS and FID improve."
217	    - figure_id: "Figure 4b"
218	      viz_type: "scatter"
219	      dimensions_varied: ["variance vs generalization score as alternative to entropy"]
220	      design_note: "Deliberately placed next to Figure 4a to show that variance is a weaker predictor than entropy. The scatter is visibly more dispersed, making the entropy superiority obvious without needing statistics."
221	  figure_narrative_role: >
222	    Figure 1 (pipeline overview + generalization-to-memorization preview) →
223	    Figure 2 (Finding I: generalization-to-memorization transition, qualitative + quantitative) →
224	    Figure 3 (Finding II: entropy shrinkage + distribution collapse visualization) →
225	    Figure 4 (Finding III: entropy-GS correlation, the key evidence; entropy vs variance comparison) →
226	    Figures 5-7 (Mitigation results: GS/FID/entropy improvements with selection methods, parallel grid layout) →
227	    Figure 8 (Mechanistic insight: selection naturally prefers real data) →
228	    Figure 9 (Extension: CFG setting on MNIST).
229	    The flow follows a clear discover-understand-mitigate-extend arc.
230	
231	tables:
232	  table_count: 0
233	  main_result_table:
234	    table_id: "N/A"
235	    row_axis: "N/A"
236	    col_axis: "N/A"
237	    row_organization: "N/A"
238	    col_organization: "N/A"
239	    highlight_strategy: "N/A"
240	    statistical_reporting: "N/A"
241	    num_baselines: 0
242	    design_note: >
243	      Notable design choice: this paper has NO tables in the main text. All quantitative results
244	      are presented as line plots (Figures 5-7) and scatter plots (Figure 4). This is unusual for
245	      a NeurIPS paper but works because the key story is about trends over iterations (naturally
246	      suited to line plots) rather than point comparisons across methods. The absence of tables
247	      keeps the paper visually unified around its "curves over iterations" motif.
248	  ablation_tables:
249	    - table_id: "N/A (Appendix C)"
250	      what_varied: ["Number of generated candidates (N vs 2N)", "Threshold decay rate alpha"]
251	      variation_style: "Presented as figures/plots rather than tables"
252	      design_note: "Ablations are in the appendix and use the same figure-based presentation as the main paper."
253	  supplementary_tables:
254	    in_appendix: false
255	    content: "No tables even in appendix; all results presented as multi-panel line plots and scatter plots"
256	    reason: >
257	      The paper's central argument is about trajectories over iterations, not about static
258	      method-vs-method comparisons. Line plots naturally show this temporal evolution, making
259	      tables unnecessary. The only potential table content (FID/GS at specific iterations) is
260	      embedded in figure panels instead.
261	
262	=== wu2025_detection_survey.yaml ===
263	paper_key: "wu2025_detection_survey"
264	title: "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions"
265	venue: "Computational Linguistics, Vol. 51, Issue 1, 2025"
266	full_text_available: false
267	
268	research:
269	  baselines: ["N/A (survey paper)"]
270	  metrics:
271	    - {name: "AUROC", direction: "higher_better"}
272	    - {name: "F1", direction: "higher_better"}
273	    - {name: "TPR@FPR", direction: "higher_better"}
274	  datasets:
275	    - {name: "various detection benchmarks surveyed", size: "N/A"}
276	  ablation_dimensions: ["method family (watermarking/statistical/neural/human-assisted)", "evaluation setting (in-domain/cross-domain/cross-model)", "attack type"]
277	  training_recipe: {optimizer: "N/A (survey)", lr: "N/A", hardware: "N/A"}
278	  method_family: "survey covering watermarking, statistics-based, neural-based, and human-assisted detection"
279	
280	positioning:
281	  core_claim: "Comprehensive taxonomy of LLM text detection methods organized into 4 families, with analysis of challenges including OOD generalization, adversarial attacks, and evaluation framework deficiencies"
282	  key_results: "Identifies key gaps: OOD robustness, attack resilience, real-world data handling, lack of standardized evaluation"
283	  limitations: ["survey scope limited to text modality", "rapidly evolving field"]
284	  relation_to_us: "foundation"
285	
286	narrative: "N/A"
287	figures: "N/A"
288	tables: "N/A"
289	
290	=== kirchenbauer2023_watermark.yaml ===
291	paper_key: "kirchenbauer2023_watermark"
292	title: "A Watermark for Large Language Models"
293	venue: "ICML 2023"
294	full_text_available: false
295	
296	research:
297	  baselines: ["no watermark baseline", "post-hoc detection methods"]
298	  metrics:
299	    - {name: "p-value (watermark detection)", direction: "lower_better"}
300	    - {name: "text quality (perplexity)", direction: "lower_better"}
301	    - {name: "BLEU/ROUGE (quality preservation)", direction: "higher_better"}
302	  datasets:
303	    - {name: "OPT model outputs", size: "N/A"}
304	  ablation_dimensions: ["green list fraction", "watermark strength (delta)", "text length", "model size"]
305	  training_recipe: {optimizer: "N/A (decoding-time watermark)", lr: "N/A", hardware: "OPT multi-billion parameter models"}
306	  method_family: "statistical watermarking via green token promotion"
307	
308	positioning:
309	  core_claim: "Invisible watermarks can be embedded in LLM outputs by promoting 'green' tokens during generation, detectable from short spans without model access, with negligible quality impact"
310	  key_results: "Algorithmically detectable watermark with interpretable p-values; tested on OPT models; information-theoretic sensitivity analysis"
311	  limitations: ["vulnerable to paraphrasing attacks", "requires control of generation process", "green token bias may affect specific domains"]
312	  relation_to_us: "orthogonal"
313	
314	narrative: "N/A"
315	figures: "N/A"
316	tables: "N/A"
317	
318	=== dohmatob2025_strong_collapse.yaml ===
319	paper_key: "dohmatob2025_strong_collapse"
320	title: "Strong Model Collapse"
321	venue: "ICLR 2025 Spotlight"
322	full_text_available: true
323	
324	research:
325	  baselines:
326	    - "Training on pure real/original data (no synthetic contamination)"
327	    - "Training on pure synthetic data"
328	    - "Mixed real+synthetic data with various proportions p2"
329	    - "Weighted single-step mixing (data weighting strategies)"
330	    - "Dynamic multi-step mixing"
331	  metrics:
332	    - {name: "test error (E_test on real distribution)", direction: "lower_better"}
333	    - {name: "test loss (cross-entropy for language modeling)", direction: "lower_better"}
334	    - {name: "collapse term zeta (excess error from synthetic data)", direction: "lower_better"}
335	  datasets:
336	    - {name: "Gaussian synthetic data (random projections)", size: "n=500 samples, variable d"}
337	    - {name: "MNIST", size: "standard 60K/10K, used for regression with two-layer networks"}
338	    - {name: "BabiStories", size: "reproduction of TinyStories via Mixtral-8x7B; token counts up to ~3e10"}
339	  ablation_dimensions:
340	    - "synthetic data proportion p2 (fraction of training data that is synthetic)"
341	    - "model size m (network width for random projections, depth/layers for GPT-2)"
342	    - "synthetic data quality c^2 (distribution mismatch between real and synthetic)"
343	    - "total training set size n (scaling behavior)"
344	    - "parametrization rate psi=m/n (under- vs over-parameterized regime)"
345	    - "interpolation threshold crossing (m=n boundary)"
346	  training_recipe:
347	    optimizer: "not explicitly detailed in accessible text; standard SGD/Adam for neural network experiments"
348	    lr: "not explicitly detailed in accessible text"
349	    hardware: "not explicitly detailed in accessible text"
350	    details: "Random projections on Gaussian data (n=500); two-layer neural networks on MNIST (width m=2000); GPT-2 models (12-layer) on BabiStories; experiments vary p2 and model size systematically"
351	  method_family: "theoretical analysis of model collapse via bias-variance decomposition and operator-valued free probability theory"
352	
353	positioning:
354	  core_claim: "Model collapse persists even when mixing real and synthetic data, as long as the fraction of synthetic data does not vanish asymptotically — establishing a 'strong' form of collapse where no fixed-proportion mixing strategy can prevent performance degradation, and larger models amplify this effect in the under-parameterized regime."
355	  key_results: "E_test = B + V + zeta decomposition where zeta is irreducible collapse term; in scaling laws regime (phi->0+), zeta ~ p2^2 * tr(Delta) remains bounded unless p2->0; 1% synthetic data sufficient to cause collapse plateau; larger models amplify collapse when real/synthetic distributions differ significantly; double-descent pattern where over-parameterized models (past m=n threshold) partially mitigate but do not eliminate collapse"
356	  limitations:
357	    - "Theory focuses on supervised regression with label shifts — does not directly model generative/autoregressive training"
358	    - "Random projections model is a simplified approximation of actual neural networks (linearized regime)"
359	    - "Gaussian feature distribution assumption with diagonal covariance matrices"
360	    - "Proportionate scaling limit assumes d,n,m -> infinity with fixed ratios"
361	    - "For fully-trained neural networks the theory does not directly apply, though authors anticipate general trends hold"
362	    - "Does not address mitigation via data filtering, detection, or curation (only analyzes mixing/weighting)"
363	  relation_to_us: "foundation"
364	
365	narrative:
366	  story_type: "突破局限型"
367	  hook: "Opens with the observation that AI-generated content is increasingly contaminating web training corpora, and asks whether the standard approach of scaling up training data can still work when synthetic data is inevitably mixed in. Frames this as a fundamental threat to the scaling laws paradigm."
368	  tension: "Prior model collapse work showed degradation in recursive (iterative) generation settings, but left open whether strategic mixing of real and synthetic data could prevent collapse. The natural hope is that diluting synthetic data with sufficient real data would restore normal scaling — this paper proves that hope is false."
369	  key_insight: "The key insight is the bias-variance decomposition E_test = B + V + zeta, where zeta is an irreducible collapse term that persists as long as the synthetic data fraction p2 remains fixed (non-vanishing). This means no matter how much you scale total data n, the collapse term does not vanish — you must asymptotically eliminate synthetic data proportion entirely. Revealed through Theorem 1 (linear models) and Theorem 2 (random projections/neural approximation)."
370	  argument_chain: "problem (synthetic data contamination is unavoidable) -> question (can mixing/scaling overcome it?) -> theory (bias-variance decomposition reveals irreducible collapse term zeta) -> scaling law implication (zeta plateaus unless p2->0) -> model size analysis (bigger models amplify collapse below interpolation threshold) -> double-descent (reversal above interpolation threshold but not elimination) -> data mixing strategies (weighted/dynamic mixing cannot fix fundamental issue) -> experimental validation (random projections, MNIST, GPT-2 on BabiStories confirm theory)"
371	  contribution_framing: "Two main results explicitly labeled: Result #1 (Strong Model Collapse) — collapse persists with any fixed synthetic fraction; Result #2 (Model Size and Model Collapse) — bigger models amplify collapse except past interpolation threshold. Followed by experimental validation across three settings (toy, MNIST, language modeling)."
372	  intro_structure: "~5 paragraphs: P1=hook (AI-generated content proliferating in training data), P2=problem framing (model collapse definition and prior work), P3=research questions (can mixing help? does model size matter?), P4=main results summary (Result #1 and #2), P5=experimental validation overview and paper organization. Section 1.1 details contributions, Section 1.2 covers related work."
373	  notable_technique: "The 'strong' vs 'weak' framing is a powerful rhetorical device — it redefines the conversation by showing that even the most optimistic scenario (strategic mixing with fresh real data) still fails. The Pareto diagram (Figure 1) is an effective visual argument that immediately conveys the tradeoff. The paper also uses the mathematical elegance of the exact bias-variance-collapse decomposition to make a clean, falsifiable theoretical claim rather than just empirical observations."
374	
375	figures:
376	  figure_count: 8
377	  figure1:
378	    type: "motivation"
379	    description: "Pareto diagram showing test error on real data distribution: training on mixed data (y-axis) vs training on real data only (x-axis). Points colored by synthetic data quality (c^2) for a random projections model with n=500. Lines show Pareto frontiers for different quality levels. Demonstrates that mixed training always incurs excess error (points above diagonal) and the tradeoff worsens with lower synthetic data quality."
380	    narrative_role: "Immediately establishes the core claim visually — no combination of model size and data mixing achieves the performance of training on real data alone. Sets up the entire paper's argument in one figure."
381	    design_elements: ["Pareto frontier visualization", "diagonal reference line (ideal = no collapse)", "colorbar for parametrization rate psi=m/n", "multiple quality levels compared"]
382	    visual_style: "Scatter plot with Pareto frontiers; colorbar encoding model size; clean 2D layout that maps directly to the central question (mixed vs real-only performance)"
383	  result_figures:
384	    - figure_id: "Figure 3"
385	      viz_type: "line_plot"
386	      what_compared: "Strong model collapse in classical linear model — empirical confirmation of Corollary 1. Shows test error vs training set size for various synthetic data proportions p2, demonstrating that even small p2 causes scaling law plateau."
387	      how_gain_highlighted: "Direct comparison of p2=0 (ideal scaling law) vs p2>0 curves; the plateau/saturation effect is visually stark"
388	      design_note: "Log-log scale makes power-law behavior linear and the collapse plateau clearly visible as a horizontal asymptote; multiple p2 values show graduated severity"
389	    - figure_id: "Figure 4"
390	      viz_type: "line_plot"
391	      what_compared: "Impact of model size (network width m) on model collapse for various data quality levels c^2 and mixing ratios p2"
392	      how_gain_highlighted: "Shows test error as function of model size, revealing the double-descent pattern: collapse worsens up to interpolation threshold m=n, then partially reverses"
393	      design_note: "Multiple panels for different c^2 values; vertical line or inflection at m=n marks the interpolation threshold — the key theoretical prediction"
394	    - figure_id: "Figure 7"
395	      viz_type: "line_plot"
396	      what_compared: "Model collapse on MNIST with two-layer neural network (width m=2000) as function of synthetic data proportion"
397	      how_gain_highlighted: "Validates that theoretical predictions from random projections model transfer to real image data"
398	      design_note: "Bridges the theory-practice gap by testing on a real dataset"
399	    - figure_id: "Figure 8"
400	      viz_type: "line_plot"
401	      what_compared: "GPT-2 (12-layer) language model on BabiStories: (Left) test loss vs number of training tokens for various synthetic data proportions p2; (Right) test loss vs model depth showing larger models initially better but eventually worse"
402	      how_gain_highlighted: "Left panel shows clear scaling law plateau with synthetic contamination; Right panel shows the depth-dependent collapse reversal predicted by theory"
403	      design_note: "Most impactful experimental figure — demonstrates that theoretical predictions generalize to autoregressive language models despite theory being developed for regression"
404	  ablation_figures:
405	    - figure_id: "Figure 2"
406	      viz_type: "schematic_diagram"
407	      dimensions_varied: ["bias B", "variance V", "collapse term zeta"]
408	      design_note: "Illustrates the bias-variance-collapse decomposition E_test = B + V + zeta; shows how c^2 (synthetic data quality) and interpolation threshold m=n interact. Functions as both explanation and ablation — decomposing total error into its components."
409	    - figure_id: "Figure 5"
410	      viz_type: "line_plot"
411	      dimensions_varied: ["model size", "data quality", "mixing proportion"]
412	      design_note: "Shows double-descent curves as function of model parametrization; demonstrates the reversal past interpolation threshold"
413	  figure_narrative_role: "Figure 1 (Pareto motivation: collapse is unavoidable) -> Figure 2 (decomposition: why collapse happens via B+V+zeta) -> Figure 3 (theory validation: linear model confirms plateau) -> Figure 4 (model size: double-descent in collapse) -> Figure 5 (additional theory curves) -> Figure 6-7 (MNIST validation) -> Figure 8 (GPT-2 language model validation). Arc: visual claim -> theoretical mechanism -> toy validation -> model size effects -> real-world validation."
414	
415	tables:
416	  table_count: 0
417	  main_result_table:
418	    note: "This paper contains NO tables. All results are presented through mathematical theorems (Theorem 1, 2, Corollary 1) and scaling curve figures. This is consistent with theoretical ML papers where contributions are equations/bounds rather than benchmark comparisons."
419	  ablation_tables: []
420	  supplementary_tables:
421	    in_appendix: true
422	    content: "Appendices contain proofs (operator-valued free probability theory derivations), additional experimental figures, and experimental setup details (Appendix A.1: random projections hyperparameters, A.2: two-layer neural network configuration, A.3: language modeling training specifics)"
423	    reason: "Theoretical paper — results are best expressed as scaling law equations and their visual verification via figures, not tabular benchmark comparisons"
424	
425	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bfda484-c9b9-4f25-a895-eac85b35b93f",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "12eab115-f375-4fa6-a256-0aecf359c470",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est--claude-sessions-distiller-f2a9b90d/6e30d332-941b-46b3-b605-b2bffa1186bb/tool-results/br92ory9z.txt",
      "content": "=== mitchell2023_detectgpt.yaml ===\npaper_key: \"mitchell2023_detectgpt\"\ntitle: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\nvenue: \"ICML 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"likelihood thresholding\", \"entropy-based methods\", \"supervised classifiers (RoBERTa)\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"XSum\", size: \"N/A\"}\n    - {name: \"SQuAD\", size: \"N/A\"}\n    - {name: \"WritingPrompts\", size: \"N/A\"}\n    - {name: \"fake news (GPT-NeoX generated)\", size: \"N/A\"}\n  ablation_dimensions: [\"perturbation model\", \"number of perturbations\", \"source model size\"]\n  training_recipe: {optimizer: \"N/A (zero-shot)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"zero-shot detection via log probability curvature\"\n\npositioning:\n  core_claim: \"Machine-generated text occupies negative curvature regions of the source model's log probability function, enabling detection without training a classifier\"\n  key_results: \"GPT-NeoX 20B fake news: AUROC 0.81 → 0.95 vs strongest baseline\"\n  limitations: [\"requires perturbation model (slow)\", \"requires white-box or proxy model access\", \"short texts challenging\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== shi2025_closer_look.yaml ===\npaper_key: \"shi2025_closer_look\"\ntitle: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\nvenue: \"NeurIPS 2025 (Spotlight)\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Vanilla replace paradigm (train on synthetic data only)\"\n    - \"Vanilla accumulate-subsample paradigm (uniform subsampling from real + all synthetic)\"\n    - \"Unconditional DDPM generation\"\n    - \"Classifier-Free Guidance (CFG, scale=2)\"\n  metrics:\n    - {name: \"Generalization Score (GS)\", direction: \"higher_better\", definition: \"Average L2 distance in DINOv2 feature space between each generated image and its nearest training neighbor\"}\n    - {name: \"FID (Frechet Inception Distance)\", direction: \"lower_better\", definition: \"InceptionV3-based distribution distance\"}\n    - {name: \"Estimated Entropy (Kozachenko-Leonenko)\", direction: \"higher_better\", definition: \"KL entropy estimator with gamma=1 on DINOv2 features\"}\n  datasets:\n    - {name: \"CIFAR-10\", size: \"32,768 images (32x32)\", note: \"Also used nested subsets: 1024/2048/4096/8192/16384/32768\"}\n    - {name: \"FFHQ\", size: \"8,192 images (downsampled to 32x32)\"}\n    - {name: \"MNIST\", size: \"12,000 images\"}\n  ablation_dimensions:\n    - \"Dataset size (1024 to 32768 in powers of 2)\"\n    - \"Training paradigm (replace vs accumulate-subsample)\"\n    - \"Selection method (Greedy Selection vs Threshold Decay Filter vs vanilla)\"\n    - \"Number of generated candidates (N vs 2N before selection)\"\n    - \"Threshold decay rate alpha (sensitivity analysis)\"\n    - \"Classifier-Free Guidance scale\"\n    - \"Entropy vs variance as correlation target\"\n  training_recipe:\n    model: \"UNet-based DDPM (~16-19M parameters)\"\n    optimizer: \"Adam\"\n    lr: \"1e-4\"\n    weight_decay: \"1e-6\"\n    batch_size: 128\n    precision: \"FP16 mixed\"\n    diffusion_steps: 1000\n    epochs_cifar: 500\n    epochs_ffhq: 1000\n    hardware: \"Single NVIDIA A100 GPU\"\n    feature_extractor: \"DINOv2 (for distance/entropy computation)\"\n    unet_channels_cifar_ffhq: \"[48, 48, 96, 96, 144, 144] with 6 down/up blocks\"\n    unet_channels_mnist: \"[64, 128, 256, 512] with 4 down/up blocks\"\n  method_family: \"Entropy-based data selection for mitigating model collapse in iterative generative training\"\n\npositioning:\n  core_claim: \"Model collapse in diffusion models manifests as a generalization-to-memorization transition driven by training data entropy shrinkage, not just variance collapse — and entropy-based data selection can effectively delay this transition.\"\n  key_results: >\n    Pearson r=0.91 between training data entropy and log(generalization score), dataset-size-independent.\n    FFHQ accumulate-subsample: vanilla FID=75.7 vs Greedy Selection FID=44.7 at iteration 8.\n    MNIST CFG: vanilla CFG FID=66.2 vs CFG+filtering FID=22.4 at iteration 8.\n    Greedy Selection preferentially retains real data (65% real by iteration 8 vs 12.5% uniform baseline).\n  limitations:\n    - \"No rigorous theoretical explanation for why entropy collapses — only empirical demonstration\"\n    - \"Limited to image diffusion models; no validation on language models or discrete diffusion\"\n    - \"Greedy Selection is computationally expensive (quadratic in dataset size)\"\n    - \"Only tested on 32x32 resolution images with relatively small models (~16-19M params)\"\n    - \"No formal analysis of how many iterations can be sustained before memorization\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: >\n    Opens with the practical inevitability of synthetic data contamination: as diffusion models flood\n    the internet with generated content, future training sets will inevitably contain synthetic data,\n    creating a self-consuming loop. This is a real-world crisis framing, not hypothetical.\n  tension: >\n    Existing perspectives on model collapse (variance shrinkage, distribution shift) are shown to be\n    theoretically valid but practically insufficient — variance collapse requires \"an extremely large\n    number of iterations\" to manifest, making it \"rarely a practical concern.\" This creates a gap:\n    the community has mathematical frameworks that don't explain what practitioners actually observe.\n  key_insight: >\n    Revealed in paragraph 3 of the intro: the transition from generalization to memorization is the\n    true practical manifestation of collapse. Models don't just get worse — they specifically lose the\n    ability to generate novel content and start copying training data. The entropy of the training set\n    (not the model) is the key diagnostic signal, with r=0.91 correlation to generalizability.\n  argument_chain: >\n    Real-world synthetic data contamination is inevitable →\n    Existing collapse perspectives miss practical manifestations →\n    We observe a generalization-to-memorization transition (Finding I) →\n    Training data entropy shrinks across iterations (Finding II) →\n    Entropy strongly correlates with generalization capability (Finding III, r=0.91) →\n    Entropy-based data selection preserves diversity and delays collapse →\n    Validated across 3 datasets, 2 paradigms, with CFG extension\n  contribution_framing: >\n    Three numbered contributions, each one sentence. Pattern: identify phenomenon → investigate\n    driving factor → propose and validate mitigation. Clean problem-insight-solution structure.\n    Contributions are framed as empirical discoveries rather than theoretical claims, matching the\n    paper's predominantly experimental nature.\n  intro_structure: >\n    3 paragraphs + \"Our Contributions\" subsection.\n    P1: Problem context — synthetic data proliferation and the self-consuming loop threat.\n    P2: Critique of existing perspectives — variance collapse and distribution shift are insufficient.\n    P3: Their perspective — generalization-to-memorization transition, entropy as diagnostic, proposed mitigation.\n    Contributions: 3 numbered items following identify-investigate-propose pattern.\n  notable_technique: >\n    The paper uses a \"practical insufficiency\" argument to distinguish itself from prior theoretical\n    work. Instead of claiming predecessors are wrong, it argues they are right but miss what matters\n    in practice. This is a diplomatically effective positioning that avoids direct conflict while\n    establishing clear novelty. The visual pairing of generated images with their nearest training\n    neighbors (Figure 2 left) makes the abstract concept of \"memorization\" viscerally obvious.\n\nfigures:\n  figure_count: 9\n  figure1:\n    type: \"method_overview\"\n    description: >\n      Three-row pipeline diagram. Top row (green background): \"Collapse Iteration\" showing the\n      replace paradigm where D1 → Training → M1 → Sampling → D2 → Training → M2 → ... → Dn.\n      Middle row (blue background): \"Mitigated Iteration\" showing the accumulate-subsample paradigm\n      with a pie chart merging real data and previously generated data, plus a funnel icon for\n      \"Selection\" before constructing D2. Bottom right (orange background): \"Evolution\" panel showing\n      pairs of generated images (top) and their nearest training counterparts (bottom) at Iterations\n      1, 3, and n, with a horizontal arrow from \"Generalization\" to \"Memorization\" and \"Degradation\"\n      labels between iteration pairs.\n    narrative_role: >\n      Serves as the roadmap for the entire paper: defines the two paradigms (collapse vs mitigated),\n      introduces the selection intervention, and previews the core finding (generalization-to-memorization\n      transition) — all in one figure. The reader immediately grasps the problem, the setup, and the\n      paper's contribution.\n    design_elements:\n      - \"Color-coded rows: green=collapse, blue=mitigated, orange=evolution\"\n      - \"Pipeline arrows connecting dataset→model→sampling→dataset\"\n      - \"Pie chart for data composition (real vs synthetic)\"\n      - \"Funnel icon for selection step\"\n      - \"Real face image pairs showing degradation progression\"\n      - \"Horizontal arrow from Generalization to Memorization\"\n    visual_style: >\n      Clean horizontal flow with three visually distinct rows. Pastel background colors (green,\n      blue, orange) separate conceptual layers. Neural network icons for models, cylindrical icons\n      for datasets. The bottom-right evolution panel uses real face images to ground the abstract\n      pipeline in concrete visual evidence. Legend in bottom-left defines notation.\n  result_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"qualitative_comparison + line_plot\"\n      what_compared: \"Generated images vs their nearest training neighbors across iterations 1, 3, 8; GS decay curves for 6 dataset sizes\"\n      how_gain_highlighted: \"Left panel shows progressive visual convergence (memorization). Right panel uses color-coded curves with labeled 'Generalization Regime' and 'Memorization Regime' regions.\"\n      design_note: >\n        Powerful dual-panel design: qualitative evidence (left) paired with quantitative curves (right).\n        The image grid makes memorization viscerally obvious — generated faces become identical to\n        training neighbors. The right panel uses a horizontal dashed line to separate regimes and\n        annotated text labels for the two regions. Six dataset sizes in distinct colors show the\n        dataset-size effect on collapse rate. Log-scale y-axis on GS.\n    - figure_id: \"Figure 4a\"\n      viz_type: \"scatter\"\n      what_compared: \"Estimated entropy (x-axis) vs generalization score (y-axis, log scale) across 6 dataset sizes\"\n      how_gain_highlighted: \"Red dashed regression line through all points from all dataset sizes, demonstrating r=0.91 universal correlation. Points from different sizes align on the same line.\"\n      design_note: >\n        The key evidence figure. Log-scale y-axis linearizes the relationship. Color coding by dataset\n        size (same palette as Figure 2) shows that different sizes fall on the same line — establishing\n        a dataset-size-independent law. Clean white background, no clutter. Contrast with Figure 4b\n        (variance) where the correlation is visibly weaker.\n    - figure_id: \"Figure 5\"\n      viz_type: \"multi_panel_line_plot\"\n      what_compared: \"Generalization Score over iterations for vanilla vs Greedy Selection vs Threshold Decay Filter, across datasets and paradigms\"\n      how_gain_highlighted: \"Three lines per panel; selection methods consistently above vanilla, showing sustained higher GS\"\n      design_note: \"6 subfigures in a grid (datasets x paradigms). Independent y-axes per subfigure to show relative improvement. Clean legend with three line styles.\"\n    - figure_id: \"Figure 6\"\n      viz_type: \"multi_panel_line_plot\"\n      what_compared: \"FID over iterations for vanilla vs Greedy Selection vs Threshold Decay Filter\"\n      how_gain_highlighted: \"Selection methods consistently lower FID curves than vanilla across all panels\"\n      design_note: \"Same grid layout as Figure 5 for parallel reading. FID improvement most dramatic on accumulate-subsample paradigm.\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"stacked_bar_chart_with_overlay_line\"\n      what_compared: \"Proportion of selected images from each iteration source; blue bars = real data proportion vs red 1/n baseline line\"\n      how_gain_highlighted: \"Blue bars (real data fraction) dramatically exceed the red 1/n line, especially in later iterations — the method naturally discovers that real data is more diverse\"\n      design_note: >\n        Insightful visualization of an emergent behavior: the selection algorithm was not told to prefer\n        real data, but the entropy-maximizing objective naturally selects more real images as synthetic\n        data clusters tighten. The stacked bars show composition while the overlay line shows the\n        null expectation. Multiple panels for different datasets/methods.\n    - figure_id: \"Figure 9\"\n      viz_type: \"qualitative_comparison + line_plot\"\n      what_compared: \"MNIST generation: unconditional (FID=74.4) vs CFG (FID=66.2) vs CFG+filtering (FID=22.4)\"\n      how_gain_highlighted: \"Side-by-side digit grids show dramatic quality improvement; entropy plot shows filtering maintains diversity that CFG alone destroys\"\n      design_note: \"Extension experiment demonstrating generality beyond unconditional setting. The 3x improvement in FID (66.2→22.4) is a compelling headline number.\"\n  ablation_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot + 2D_scatter_projection\"\n      dimensions_varied: [\"iteration number\", \"dataset entropy\"]\n      design_note: >\n        Three-panel figure. Left: entropy decay curves over iterations for different dataset sizes.\n        Middle and Right: 2D SVD projections of data distribution at iteration 1 (spread) vs\n        iteration 21 (collapsed into tight clusters). The SVD projections make entropy collapse\n        visually intuitive — you can see the distribution concentrating.\n    - figure_id: \"Figure 7\"\n      viz_type: \"multi_panel_line_plot\"\n      dimensions_varied: [\"selection method\", \"training paradigm\", \"dataset\"]\n      design_note: \"Shows that selection methods maintain higher entropy across iterations. Same grid layout as Figures 5-6 for parallel comparison. Entropy serves as the mechanistic explanation for why GS and FID improve.\"\n    - figure_id: \"Figure 4b\"\n      viz_type: \"scatter\"\n      dimensions_varied: [\"variance vs generalization score as alternative to entropy\"]\n      design_note: \"Deliberately placed next to Figure 4a to show that variance is a weaker predictor than entropy. The scatter is visibly more dispersed, making the entropy superiority obvious without needing statistics.\"\n  figure_narrative_role: >\n    Figure 1 (pipeline overview + generalization-to-memorization preview) →\n    Figure 2 (Finding I: generalization-to-memorization transition, qualitative + quantitative) →\n    Figure 3 (Finding II: entropy shrinkage + distribution collapse visualization) →\n    Figure 4 (Finding III: entropy-GS correlation, the key evidence; entropy vs variance comparison) →\n    Figures 5-7 (Mitigation results: GS/FID/entropy improvements with selection methods, parallel grid layout) →\n    Figure 8 (Mechanistic insight: selection naturally prefers real data) →\n    Figure 9 (Extension: CFG setting on MNIST).\n    The flow follows a clear discover-understand-mitigate-extend arc.\n\ntables:\n  table_count: 0\n  main_result_table:\n    table_id: \"N/A\"\n    row_axis: \"N/A\"\n    col_axis: \"N/A\"\n    row_organization: \"N/A\"\n    col_organization: \"N/A\"\n    highlight_strategy: \"N/A\"\n    statistical_reporting: \"N/A\"\n    num_baselines: 0\n    design_note: >\n      Notable design choice: this paper has NO tables in the main text. All quantitative results\n      are presented as line plots (Figures 5-7) and scatter plots (Figure 4). This is unusual for\n      a NeurIPS paper but works because the key story is about trends over iterations (naturally\n      suited to line plots) rather than point comparisons across methods. The absence of tables\n      keeps the paper visually unified around its \"curves over iterations\" motif.\n  ablation_tables:\n    - table_id: \"N/A (Appendix C)\"\n      what_varied: [\"Number of generated candidates (N vs 2N)\", \"Threshold decay rate alpha\"]\n      variation_style: \"Presented as figures/plots rather than tables\"\n      design_note: \"Ablations are in the appendix and use the same figure-based presentation as the main paper.\"\n  supplementary_tables:\n    in_appendix: false\n    content: \"No tables even in appendix; all results presented as multi-panel line plots and scatter plots\"\n    reason: >\n      The paper's central argument is about trajectories over iterations, not about static\n      method-vs-method comparisons. Line plots naturally show this temporal evolution, making\n      tables unnecessary. The only potential table content (FID/GS at specific iterations) is\n      embedded in figure panels instead.\n\n=== wu2025_detection_survey.yaml ===\npaper_key: \"wu2025_detection_survey\"\ntitle: \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\"\nvenue: \"Computational Linguistics, Vol. 51, Issue 1, 2025\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"N/A (survey paper)\"]\n  metrics:\n    - {name: \"AUROC\", direction: \"higher_better\"}\n    - {name: \"F1\", direction: \"higher_better\"}\n    - {name: \"TPR@FPR\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"various detection benchmarks surveyed\", size: \"N/A\"}\n  ablation_dimensions: [\"method family (watermarking/statistical/neural/human-assisted)\", \"evaluation setting (in-domain/cross-domain/cross-model)\", \"attack type\"]\n  training_recipe: {optimizer: \"N/A (survey)\", lr: \"N/A\", hardware: \"N/A\"}\n  method_family: \"survey covering watermarking, statistics-based, neural-based, and human-assisted detection\"\n\npositioning:\n  core_claim: \"Comprehensive taxonomy of LLM text detection methods organized into 4 families, with analysis of challenges including OOD generalization, adversarial attacks, and evaluation framework deficiencies\"\n  key_results: \"Identifies key gaps: OOD robustness, attack resilience, real-world data handling, lack of standardized evaluation\"\n  limitations: [\"survey scope limited to text modality\", \"rapidly evolving field\"]\n  relation_to_us: \"foundation\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== kirchenbauer2023_watermark.yaml ===\npaper_key: \"kirchenbauer2023_watermark\"\ntitle: \"A Watermark for Large Language Models\"\nvenue: \"ICML 2023\"\nfull_text_available: false\n\nresearch:\n  baselines: [\"no watermark baseline\", \"post-hoc detection methods\"]\n  metrics:\n    - {name: \"p-value (watermark detection)\", direction: \"lower_better\"}\n    - {name: \"text quality (perplexity)\", direction: \"lower_better\"}\n    - {name: \"BLEU/ROUGE (quality preservation)\", direction: \"higher_better\"}\n  datasets:\n    - {name: \"OPT model outputs\", size: \"N/A\"}\n  ablation_dimensions: [\"green list fraction\", \"watermark strength (delta)\", \"text length\", \"model size\"]\n  training_recipe: {optimizer: \"N/A (decoding-time watermark)\", lr: \"N/A\", hardware: \"OPT multi-billion parameter models\"}\n  method_family: \"statistical watermarking via green token promotion\"\n\npositioning:\n  core_claim: \"Invisible watermarks can be embedded in LLM outputs by promoting 'green' tokens during generation, detectable from short spans without model access, with negligible quality impact\"\n  key_results: \"Algorithmically detectable watermark with interpretable p-values; tested on OPT models; information-theoretic sensitivity analysis\"\n  limitations: [\"vulnerable to paraphrasing attacks\", \"requires control of generation process\", \"green token bias may affect specific domains\"]\n  relation_to_us: \"orthogonal\"\n\nnarrative: \"N/A\"\nfigures: \"N/A\"\ntables: \"N/A\"\n\n=== dohmatob2025_strong_collapse.yaml ===\npaper_key: \"dohmatob2025_strong_collapse\"\ntitle: \"Strong Model Collapse\"\nvenue: \"ICLR 2025 Spotlight\"\nfull_text_available: true\n\nresearch:\n  baselines:\n    - \"Training on pure real/original data (no synthetic contamination)\"\n    - \"Training on pure synthetic data\"\n    - \"Mixed real+synthetic data with various proportions p2\"\n    - \"Weighted single-step mixing (data weighting strategies)\"\n    - \"Dynamic multi-step mixing\"\n  metrics:\n    - {name: \"test error (E_test on real distribution)\", direction: \"lower_better\"}\n    - {name: \"test loss (cross-entropy for language modeling)\", direction: \"lower_better\"}\n    - {name: \"collapse term zeta (excess error from synthetic data)\", direction: \"lower_better\"}\n  datasets:\n    - {name: \"Gaussian synthetic data (random projections)\", size: \"n=500 samples, variable d\"}\n    - {name: \"MNIST\", size: \"standard 60K/10K, used for regression with two-layer networks\"}\n    - {name: \"BabiStories\", size: \"reproduction of TinyStories via Mixtral-8x7B; token counts up to ~3e10\"}\n  ablation_dimensions:\n    - \"synthetic data proportion p2 (fraction of training data that is synthetic)\"\n    - \"model size m (network width for random projections, depth/layers for GPT-2)\"\n    - \"synthetic data quality c^2 (distribution mismatch between real and synthetic)\"\n    - \"total training set size n (scaling behavior)\"\n    - \"parametrization rate psi=m/n (under- vs over-parameterized regime)\"\n    - \"interpolation threshold crossing (m=n boundary)\"\n  training_recipe:\n    optimizer: \"not explicitly detailed in accessible text; standard SGD/Adam for neural network experiments\"\n    lr: \"not explicitly detailed in accessible text\"\n    hardware: \"not explicitly detailed in accessible text\"\n    details: \"Random projections on Gaussian data (n=500); two-layer neural networks on MNIST (width m=2000); GPT-2 models (12-layer) on BabiStories; experiments vary p2 and model size systematically\"\n  method_family: \"theoretical analysis of model collapse via bias-variance decomposition and operator-valued free probability theory\"\n\npositioning:\n  core_claim: \"Model collapse persists even when mixing real and synthetic data, as long as the fraction of synthetic data does not vanish asymptotically — establishing a 'strong' form of collapse where no fixed-proportion mixing strategy can prevent performance degradation, and larger models amplify this effect in the under-parameterized regime.\"\n  key_results: \"E_test = B + V + zeta decomposition where zeta is irreducible collapse term; in scaling laws regime (phi->0+), zeta ~ p2^2 * tr(Delta) remains bounded unless p2->0; 1% synthetic data sufficient to cause collapse plateau; larger models amplify collapse when real/synthetic distributions differ significantly; double-descent pattern where over-parameterized models (past m=n threshold) partially mitigate but do not eliminate collapse\"\n  limitations:\n    - \"Theory focuses on supervised regression with label shifts — does not directly model generative/autoregressive training\"\n    - \"Random projections model is a simplified approximation of actual neural networks (linearized regime)\"\n    - \"Gaussian feature distribution assumption with diagonal covariance matrices\"\n    - \"Proportionate scaling limit assumes d,n,m -> infinity with fixed ratios\"\n    - \"For fully-trained neural networks the theory does not directly apply, though authors anticipate general trends hold\"\n    - \"Does not address mitigation via data filtering, detection, or curation (only analyzes mixing/weighting)\"\n  relation_to_us: \"foundation\"\n\nnarrative:\n  story_type: \"突破局限型\"\n  hook: \"Opens with the observation that AI-generated content is increasingly contaminating web training corpora, and asks whether the standard approach of scaling up training data can still work when synthetic data is inevitably mixed in. Frames this as a fundamental threat to the scaling laws paradigm.\"\n  tension: \"Prior model collapse work showed degradation in recursive (iterative) generation settings, but left open whether strategic mixing of real and synthetic data could prevent collapse. The natural hope is that diluting synthetic data with sufficient real data would restore normal scaling — this paper proves that hope is false.\"\n  key_insight: \"The key insight is the bias-variance decomposition E_test = B + V + zeta, where zeta is an irreducible collapse term that persists as long as the synthetic data fraction p2 remains fixed (non-vanishing). This means no matter how much you scale total data n, the collapse term does not vanish — you must asymptotically eliminate synthetic data proportion entirely. Revealed through Theorem 1 (linear models) and Theorem 2 (random projections/neural approximation).\"\n  argument_chain: \"problem (synthetic data contamination is unavoidable) -> question (can mixing/scaling overcome it?) -> theory (bias-variance decomposition reveals irreducible collapse term zeta) -> scaling law implication (zeta plateaus unless p2->0) -> model size analysis (bigger models amplify collapse below interpolation threshold) -> double-descent (reversal above interpolation threshold but not elimination) -> data mixing strategies (weighted/dynamic mixing cannot fix fundamental issue) -> experimental validation (random projections, MNIST, GPT-2 on BabiStories confirm theory)\"\n  contribution_framing: \"Two main results explicitly labeled: Result #1 (Strong Model Collapse) — collapse persists with any fixed synthetic fraction; Result #2 (Model Size and Model Collapse) — bigger models amplify collapse except past interpolation threshold. Followed by experimental validation across three settings (toy, MNIST, language modeling).\"\n  intro_structure: \"~5 paragraphs: P1=hook (AI-generated content proliferating in training data), P2=problem framing (model collapse definition and prior work), P3=research questions (can mixing help? does model size matter?), P4=main results summary (Result #1 and #2), P5=experimental validation overview and paper organization. Section 1.1 details contributions, Section 1.2 covers related work.\"\n  notable_technique: \"The 'strong' vs 'weak' framing is a powerful rhetorical device — it redefines the conversation by showing that even the most optimistic scenario (strategic mixing with fresh real data) still fails. The Pareto diagram (Figure 1) is an effective visual argument that immediately conveys the tradeoff. The paper also uses the mathematical elegance of the exact bias-variance-collapse decomposition to make a clean, falsifiable theoretical claim rather than just empirical observations.\"\n\nfigures:\n  figure_count: 8\n  figure1:\n    type: \"motivation\"\n    description: \"Pareto diagram showing test error on real data distribution: training on mixed data (y-axis) vs training on real data only (x-axis). Points colored by synthetic data quality (c^2) for a random projections model with n=500. Lines show Pareto frontiers for different quality levels. Demonstrates that mixed training always incurs excess error (points above diagonal) and the tradeoff worsens with lower synthetic data quality.\"\n    narrative_role: \"Immediately establishes the core claim visually — no combination of model size and data mixing achieves the performance of training on real data alone. Sets up the entire paper's argument in one figure.\"\n    design_elements: [\"Pareto frontier visualization\", \"diagonal reference line (ideal = no collapse)\", \"colorbar for parametrization rate psi=m/n\", \"multiple quality levels compared\"]\n    visual_style: \"Scatter plot with Pareto frontiers; colorbar encoding model size; clean 2D layout that maps directly to the central question (mixed vs real-only performance)\"\n  result_figures:\n    - figure_id: \"Figure 3\"\n      viz_type: \"line_plot\"\n      what_compared: \"Strong model collapse in classical linear model — empirical confirmation of Corollary 1. Shows test error vs training set size for various synthetic data proportions p2, demonstrating that even small p2 causes scaling law plateau.\"\n      how_gain_highlighted: \"Direct comparison of p2=0 (ideal scaling law) vs p2>0 curves; the plateau/saturation effect is visually stark\"\n      design_note: \"Log-log scale makes power-law behavior linear and the collapse plateau clearly visible as a horizontal asymptote; multiple p2 values show graduated severity\"\n    - figure_id: \"Figure 4\"\n      viz_type: \"line_plot\"\n      what_compared: \"Impact of model size (network width m) on model collapse for various data quality levels c^2 and mixing ratios p2\"\n      how_gain_highlighted: \"Shows test error as function of model size, revealing the double-descent pattern: collapse worsens up to interpolation threshold m=n, then partially reverses\"\n      design_note: \"Multiple panels for different c^2 values; vertical line or inflection at m=n marks the interpolation threshold — the key theoretical prediction\"\n    - figure_id: \"Figure 7\"\n      viz_type: \"line_plot\"\n      what_compared: \"Model collapse on MNIST with two-layer neural network (width m=2000) as function of synthetic data proportion\"\n      how_gain_highlighted: \"Validates that theoretical predictions from random projections model transfer to real image data\"\n      design_note: \"Bridges the theory-practice gap by testing on a real dataset\"\n    - figure_id: \"Figure 8\"\n      viz_type: \"line_plot\"\n      what_compared: \"GPT-2 (12-layer) language model on BabiStories: (Left) test loss vs number of training tokens for various synthetic data proportions p2; (Right) test loss vs model depth showing larger models initially better but eventually worse\"\n      how_gain_highlighted: \"Left panel shows clear scaling law plateau with synthetic contamination; Right panel shows the depth-dependent collapse reversal predicted by theory\"\n      design_note: \"Most impactful experimental figure — demonstrates that theoretical predictions generalize to autoregressive language models despite theory being developed for regression\"\n  ablation_figures:\n    - figure_id: \"Figure 2\"\n      viz_type: \"schematic_diagram\"\n      dimensions_varied: [\"bias B\", \"variance V\", \"collapse term zeta\"]\n      design_note: \"Illustrates the bias-variance-collapse decomposition E_test = B + V + zeta; shows how c^2 (synthetic data quality) and interpolation threshold m=n interact. Functions as both explanation and ablation — decomposing total error into its components.\"\n    - figure_id: \"Figure 5\"\n      viz_type: \"line_plot\"\n      dimensions_varied: [\"model size\", \"data quality\", \"mixing proportion\"]\n      design_note: \"Shows double-descent curves as function of model parametrization; demonstrates the reversal past interpolation threshold\"\n  figure_narrative_role: \"Figure 1 (Pareto motivation: collapse is unavoidable) -> Figure 2 (decomposition: why collapse happens via B+V+zeta) -> Figure 3 (theory validation: linear model confirms plateau) -> Figure 4 (model size: double-descent in collapse) -> Figure 5 (additional theory curves) -> Figure 6-7 (MNIST validation) -> Figure 8 (GPT-2 language model validation). Arc: visual claim -> theoretical mechanism -> toy validation -> model size effects -> real-world validation.\"\n\ntables:\n  table_count: 0\n  main_result_table:\n    note: \"This paper contains NO tables. All results are presented through mathematical theorems (Theorem 1, 2, Corollary 1) and scaling curve figures. This is consistent with theoretical ML papers where contributions are equations/bounds rather than benchmark comparisons.\"\n  ablation_tables: []\n  supplementary_tables:\n    in_appendix: true\n    content: \"Appendices contain proofs (operator-valued free probability theory derivations), additional experimental figures, and experimental setup details (Appendix A.1: random projections hyperparameters, A.2: two-layer neural network configuration, A.3: language modeling training specifics)\"\n    reason: \"Theoretical paper — results are best expressed as scaling law equations and their visual verification via figures, not tabular benchmark comparisons\"\n\n",
      "numLines": 426,
      "startLine": 0,
      "totalLines": 426
    }
  },
  "sourceToolAssistantUUID": "0bfda484-c9b9-4f25-a895-eac85b35b93f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "12eab115-f375-4fa6-a256-0aecf359c470",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Assistant

_source line 55 · 2026-05-21T15:05:55.817Z_

Now I have all 25 papers' data. Let me also read the existing skill files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12eab115-f375-4fa6-a256-0aecf359c470",
  "isSidechain": false,
  "requestId": "req_011CbFvNtvhqLWQXxpVqaZei",
  "type": "assistant",
  "uuid": "93b800e4-8547-44f1-b431-8bb1d8b179af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pequh6uSbw3mzVL3fBJQfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9378,
      "cache_read_input_tokens": 61317,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 61317,
          "cache_creation_input_tokens": 9378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9378
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

_source line 56 · 2026-05-21T15:05:57.669Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KBUmYVFss5Pm2zieuuqKar`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93b800e4-8547-44f1-b431-8bb1d8b179af",
  "isSidechain": false,
  "requestId": "req_011CbFvNtvhqLWQXxpVqaZei",
  "type": "assistant",
  "uuid": "7b45049a-cb7c-4a2b-a5e0-744fadd64045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pequh6uSbw3mzVL3fBJQfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9378,
      "cache_read_input_tokens": 61317,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 61317,
          "cache_creation_input_tokens": 9378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9378
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

_source line 57 · 2026-05-21T15:05:57.674Z_

<details><summary>↩ Tool result · `toolu_01KBUmYVFss5Pm2zieuuqKar`</summary>

```text
1	# AI Text Detection & Model Collapse — Research Patterns
2	
3	From 25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.
4	
5	## Method Trends
6	
7	**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01% FPR)→DivEye (+33.2%). Continuous/ordinal scoring replacing binary (EditLens, CLOC). Detection-as-collapse-mitigation: filtering synthetic data via detectors outperforms pure human training (Drayson 2025).
8	
9	**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93; Two Paradigms: attribution breaks at scale).
10	
11	## Standard Baselines (citation freq)
12	
13	DetectGPT (8/25) > RoBERTa (5/25) > Binoculars (4/25) > Fast-DetectGPT (4/25). New detectors must compare against Binoculars + Fast-DetectGPT as zero-shot SOTA.
14	
15	## Metrics
16	
17	**AUROC** dominant (12/25). **F1** second (6/25). **TPR@low-FPR** increasingly preferred for deployment. Two Paradigms: AUROC misleading under class imbalance, supplement with PR-AUC. Collapse: FID (4/25), perplexity (4/25).
18	
19	## Key Datasets
20	
21	Detection: MAGE (7 domains×27 LLMs), RAID (2.6M texts), PAN'24. Collapse: CIFAR-10/FFHQ/MNIST (image), Wikitext-103/BabiStories (LM). Data quality: FineWeb (15T tokens).
22	
23	## Experimental Design Consensus (6/8 deep-read)
24	
25	1. Cross-domain + cross-model eval mandatory
26	2. Paraphrasing attack robustness required (drops recall 30-40%)
27	3. Progressive difficulty testbeds (MAGE: 8 scenarios easy→hard)
28	4. Collapse: iterate 8-60 rounds with per-round FID/entropy
29	
30	## Common Limitations (cross-paper freq)
31	
32	- Short text (<100 tokens): all detectors degrade (4/8)
33	- Newest LLMs close gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable (Two Paradigms)
34	- Paraphrasing universal attack (3/8)
35	- Collapse theory assumes Gaussian/linear — practice gap (3/8)
36	
37	## Research Gaps
38	
39	- **No paper estimates recursive generation depth** — detection is binary/ternary only
40	- Detection×collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred
41	- Ordinal framing (EditLens, CLOC) not applied to generation depth
42	- No collapse analysis for instruction-tuned LLMs
43	
44	## Competitor Map
45	
46	**Foundation** (9): DetectGPT, Two Paradigms, Tale of Tails, Strong Collapse, Closer Look, Broken Telephone, Ghostbuster, Demystified, survey. **Competitor** (6): MAGE, Binoculars, Fast-DetectGPT, DivEye, Intrinsic Dim, EditLens. **Complementary** (7): FineWeb, QuRating, Escaping Collapse, Drayson, Synthetic Eggs, LOKI, CLOC. **Orthogonal** (2): watermark, text degeneration.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b45049a-cb7c-4a2b-a5e0-744fadd64045",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "23177ad9-84f2-4f9f-9b5c-16ef9042377b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md",
      "content": "# AI Text Detection & Model Collapse — Research Patterns\n\nFrom 25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.\n\n## Method Trends\n\n**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01% FPR)→DivEye (+33.2%). Continuous/ordinal scoring replacing binary (EditLens, CLOC). Detection-as-collapse-mitigation: filtering synthetic data via detectors outperforms pure human training (Drayson 2025).\n\n**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93; Two Paradigms: attribution breaks at scale).\n\n## Standard Baselines (citation freq)\n\nDetectGPT (8/25) > RoBERTa (5/25) > Binoculars (4/25) > Fast-DetectGPT (4/25). New detectors must compare against Binoculars + Fast-DetectGPT as zero-shot SOTA.\n\n## Metrics\n\n**AUROC** dominant (12/25). **F1** second (6/25). **TPR@low-FPR** increasingly preferred for deployment. Two Paradigms: AUROC misleading under class imbalance, supplement with PR-AUC. Collapse: FID (4/25), perplexity (4/25).\n\n## Key Datasets\n\nDetection: MAGE (7 domains×27 LLMs), RAID (2.6M texts), PAN'24. Collapse: CIFAR-10/FFHQ/MNIST (image), Wikitext-103/BabiStories (LM). Data quality: FineWeb (15T tokens).\n\n## Experimental Design Consensus (6/8 deep-read)\n\n1. Cross-domain + cross-model eval mandatory\n2. Paraphrasing attack robustness required (drops recall 30-40%)\n3. Progressive difficulty testbeds (MAGE: 8 scenarios easy→hard)\n4. Collapse: iterate 8-60 rounds with per-round FID/entropy\n\n## Common Limitations (cross-paper freq)\n\n- Short text (<100 tokens): all detectors degrade (4/8)\n- Newest LLMs close gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable (Two Paradigms)\n- Paraphrasing universal attack (3/8)\n- Collapse theory assumes Gaussian/linear — practice gap (3/8)\n\n## Research Gaps\n\n- **No paper estimates recursive generation depth** — detection is binary/ternary only\n- Detection×collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred\n- Ordinal framing (EditLens, CLOC) not applied to generation depth\n- No collapse analysis for instruction-tuned LLMs\n\n## Competitor Map\n\n**Foundation** (9): DetectGPT, Two Paradigms, Tale of Tails, Strong Collapse, Closer Look, Broken Telephone, Ghostbuster, Demystified, survey. **Competitor** (6): MAGE, Binoculars, Fast-DetectGPT, DivEye, Intrinsic Dim, EditLens. **Complementary** (7): FineWeb, QuRating, Escaping Collapse, Drayson, Synthetic Eggs, LOKI, CLOC. **Orthogonal** (2): watermark, text degeneration.\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  },
  "sourceToolAssistantUUID": "7b45049a-cb7c-4a2b-a5e0-744fadd64045",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T15:05:58.206Z_

<details><summary>↩ Tool result · `toolu_016iZEMm7F3MeYvzYXKexSyr`</summary>

```text
1	# AI Text Detection & Model Collapse — Writing Patterns
2	
3	From 8 deep-read papers' narrative/figure/table analysis.
4	
5	## Story & Hook
6	
7	**突破局限型 dominates** (7/8). Frame contribution as overcoming a specific named prior limitation.
8	
9	Three proven hooks: (1) **Real-world urgency** — cite adoption stats ("ChatGPT: 0.1% of daily global words", Tale of Tails). (2) **Contradiction** — juxtapose success/failure evidence ("detectors beat benchmarks yet OpenAI shut theirs down", Two Paradigms). (3) **Practical inevitability** — "synthetic contamination is unavoidable" (Closer Look).
10	
11	## Intro Structure (7/8 consensus)
12	
13	3-4 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers ("RoBERTa: 99.4→88.3 OOD"). P3: approach + headline number. Contributions: 3 items (identify→analyze→validate). Quantified failure > vague criticism.
14	
15	## Tension Strategies
16	
17	Detection: **"works in lab, fails in wild"** (Ghostbuster, MAGE, Two Paradigms). Theory: **"right but practically wrong"** — prior theory valid but misses what practitioners observe (Closer Look: "variance collapse rarely a practical concern").
18	
19	## Figure 1 Design (8/8)
20	
21	Detection: **problem illustration** showing combinatorial challenge (domains×models). Collapse: **motivation figure** showing degradation mechanism. Design consensus: horizontal L→R flow, pastel color-coding, minimal text, real examples grounding abstract concepts.
22	
23	## Tables vs Figures: The Domain Split
24	
25	**Theory/collapse papers: zero tables** (4/4). All results as line plots over iterations. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8). Rule: trajectories→figures, method comparisons→tables.
26	
27	Detection tables: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold best, 4-10 baselines, point estimates (no std in 5/8).
28	
29	## Visualization Consensus
30	
31	**Line plots** dominant (6/8): training curves, scaling laws. **Heatmaps** for cross-model matrices. **Scatter** for correlation evidence (r=0.91 entropy-GS). Gain highlighting: solid/dashed (filtered/unfiltered), diverging colormaps, log-log for power laws.
32	
33	Ablations: detection→full number tables; collapse→multi-panel line plot grids (datasets×paradigms); engineering→bar charts per component.
34	
35	## Figure Narrative Arc (7/8)
36	
37	Standard: motivation→main evidence→mechanism→ablation→extension. Key techniques: **paired qualitative+quantitative** panels (Closer Look); **parallel theory-vs-experiment layout** (Tale of Tails); **progressive difficulty** as narrative arc (MAGE: 8 testbeds easy→hard).
38	
39	## Techniques Worth Stealing
40	
41	1. **"Practical insufficiency"** (Closer Look): "prior work right but misses what matters"
42	2. **Ablation-as-narrative** (FineWeb): each pipeline stage = mini-experiment
43	3. **Promise-and-peril** (Escaping Collapse): short-term good + long-term caution
44	4. **Contradiction opener** (Two Paradigms): success vs failure in paragraph 1
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5a85e78-a190-48a8-8051-3cb5ed13956e",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "e7f442e2-8fe6-49e3-95a5-e98e897185a9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md",
      "content": "# AI Text Detection & Model Collapse — Writing Patterns\n\nFrom 8 deep-read papers' narrative/figure/table analysis.\n\n## Story & Hook\n\n**突破局限型 dominates** (7/8). Frame contribution as overcoming a specific named prior limitation.\n\nThree proven hooks: (1) **Real-world urgency** — cite adoption stats (\"ChatGPT: 0.1% of daily global words\", Tale of Tails). (2) **Contradiction** — juxtapose success/failure evidence (\"detectors beat benchmarks yet OpenAI shut theirs down\", Two Paradigms). (3) **Practical inevitability** — \"synthetic contamination is unavoidable\" (Closer Look).\n\n## Intro Structure (7/8 consensus)\n\n3-4 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers (\"RoBERTa: 99.4→88.3 OOD\"). P3: approach + headline number. Contributions: 3 items (identify→analyze→validate). Quantified failure > vague criticism.\n\n## Tension Strategies\n\nDetection: **\"works in lab, fails in wild\"** (Ghostbuster, MAGE, Two Paradigms). Theory: **\"right but practically wrong\"** — prior theory valid but misses what practitioners observe (Closer Look: \"variance collapse rarely a practical concern\").\n\n## Figure 1 Design (8/8)\n\nDetection: **problem illustration** showing combinatorial challenge (domains×models). Collapse: **motivation figure** showing degradation mechanism. Design consensus: horizontal L→R flow, pastel color-coding, minimal text, real examples grounding abstract concepts.\n\n## Tables vs Figures: The Domain Split\n\n**Theory/collapse papers: zero tables** (4/4). All results as line plots over iterations. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8). Rule: trajectories→figures, method comparisons→tables.\n\nDetection tables: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold best, 4-10 baselines, point estimates (no std in 5/8).\n\n## Visualization Consensus\n\n**Line plots** dominant (6/8): training curves, scaling laws. **Heatmaps** for cross-model matrices. **Scatter** for correlation evidence (r=0.91 entropy-GS). Gain highlighting: solid/dashed (filtered/unfiltered), diverging colormaps, log-log for power laws.\n\nAblations: detection→full number tables; collapse→multi-panel line plot grids (datasets×paradigms); engineering→bar charts per component.\n\n## Figure Narrative Arc (7/8)\n\nStandard: motivation→main evidence→mechanism→ablation→extension. Key techniques: **paired qualitative+quantitative** panels (Closer Look); **parallel theory-vs-experiment layout** (Tale of Tails); **progressive difficulty** as narrative arc (MAGE: 8 testbeds easy→hard).\n\n## Techniques Worth Stealing\n\n1. **\"Practical insufficiency\"** (Closer Look): \"prior work right but misses what matters\"\n2. **Ablation-as-narrative** (FineWeb): each pipeline stage = mini-experiment\n3. **Promise-and-peril** (Escaping Collapse): short-term good + long-term caution\n4. **Contradiction opener** (Two Paradigms): success vs failure in paragraph 1\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  },
  "sourceToolAssistantUUID": "e5a85e78-a190-48a8-8051-3cb5ed13956e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T15:05:58.203Z_

<details open><summary>🔧 Tool call — Read · `toolu_016iZEMm7F3MeYvzYXKexSyr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23177ad9-84f2-4f9f-9b5c-16ef9042377b",
  "isSidechain": false,
  "requestId": "req_011CbFvNtvhqLWQXxpVqaZei",
  "type": "assistant",
  "uuid": "e5a85e78-a190-48a8-8051-3cb5ed13956e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pequh6uSbw3mzVL3fBJQfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9378,
      "cache_read_input_tokens": 61317,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 61317,
          "cache_creation_input_tokens": 9378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9378
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

_source line 60 · 2026-05-21T15:06:58.439Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture of all 25 papers and the existing skill files. Let me do the Layer 2 cross-paper synthesis and regenerate the skill files.

Let me analyze the data systematically:

**Papers by category:**

**Full-text deep-read (8):**
1. bevendorff2025_two_paradigms (ACL 2025 Findings) - foundation
2. li2024_mage (ACL 2024) - competitor
3. dohmatob2024_tale_of_tails (ICML 2024) - foundation


4. yi2026_escaping_collapse (ICLR 2026) - complementary
5. verma2024_ghostbuster (NAACL 2024) - foundation
6. penedo2024_fineweb (NeurIPS 2024) - complementary
7. shi2025_closer_look (NeurIPS 2025 Spotlight) - foundation
8. dohmatob2025_strong_collapse (ICLR 2025 Spotlight) - foundation

**Abstract-only (17):**
9. dohmatob2024_demystified (NeurIPS 2024) - foundation
10. alemoh

2024_mad (ICLR 2024) - foundation
11. drayson2025_detection_prevents_collapse (EMNLP 2025 Findings) - complementary
12. synthetic_eggs2026 (ACL 2026 Findings) - complementary
13. mohamed2025_broken_telephone (ACL 2025) - foundation
14. finlayson2024_closing (ICLR 2024) - orthogonal
15. binoculars2024 (ICML 2024) - competitor
16. fast_detectgpt2024 (ICLR 2024) - competitor
17. diveye2026 (TMLR 2026) - competitor
18. loki2025 (ICLR 2025 Spotlight) - complementary
19. tulchinskii (incomplete entry)
20. editlens2026 (ICLR 2026) - competitor
21. cloc2025 (CVPR 2025) - complementary
22. qurating2024 (ICML 2024) - complementary
23. mitchell2023_detectgpt (ICML 2023) - foundation
24. wu2025_detection_survey (CL 2025) - foundation
25. kirchenbauer2023_watermark (ICML 2023) - orthogonal

Now I'm moving into the synthesis phase, starting with baseline frequency analysis. DetectGPT appears across multiple papers including bevendorff, li, diveye, fast_detectgpt, mitchell, tulchinskii, verma, and wu, suggesting it's a widely-referenced baseline in this detection landscape.

Looking at the frequency distributions across methods and metrics, I'm seeing DetectGPT dominate at around 8 papers, followed by RoBERTa-based classifiers at 5, Binoculars at 4, and Fast-DetectGPT at 3. For evaluation metrics, AUROC is the most common across 8+ papers, with F1 and FID each appearing in about 3 papers, and perplexity metrics scattered across a few others. Looking at the dataset and method trends, I'm seeing some clear patterns emerge. The zero-shot statistical approaches are evolving toward simpler and faster implementations—DetectGPT led to Fast-DetectGPT, which then inspired Binoculars and DivEye, each iteration improving efficiency. Meanwhile, newer methods are exploring alternative angles like continuous regression with EditLens, ordinal classification with CLOC, and entropy-based approaches that measure training data diversity. There's also growing interest in detection as a mitigation strategy, like Drayson's approach to prevent model collapse, and verifier-based systems. In contrast, the older supervised binary classifiers and pure perturbation methods are losing traction.

For validation, there's strong consensus around testing across different domains and models, checking robustness against paraphrasing and adversarial attacks, and examining how performance scales with recursive generations, model size, and synthetic data mixing. Document length is another key variable being tested. The foundational papers—DetectGPT, Two Paradigms, and Tale of Tails—remain central references that newer work builds on.

Looking at the limitations across these papers, the most critical challenges are handling short text (which affects about a third of the studies), the fact that newer models like GPT-4o and o1 are narrowing the detection gap, and vulnerability to paraphrasing attacks. Theory-level limitations are also emerging as a concern.

The research gaps are becoming clearer now. Nobody's actually measured how deep recursive generation can go, which is exactly what we need. Detection and collapse are almost completely disconnected in the literature except for one recent paper. There's also this ordinal framing approach that hasn't been applied to generation depth yet, and all the collapse analysis assumes simplified theoretical models rather than instruction-tuned LLMs that actually exist in practice.

From the papers I've read closely, most fall into a pattern of breaking through existing limitations—seven out of eight take this approach.

Looking at how these papers hook readers, they use real-world urgency with concrete statistics, or they present contradictions like detectors working versus companies shutting them down anyway. Some emphasize that synthetic contamination is inevitable, while others focus on societal consequences like impacts on schools and journalism. The introductions typically run three to five paragraphs and end with a numbered list of three or four contributions. They follow a consistent rhythm: establish urgency, show why existing approaches fail, present the new approach with a key number, then list what's being contributed.

For the opening figure, papers use different strategies—some illustrate the problem directly, others show motivation or give an overview of the method, and some lead with a teaser result.

Now I'm examining how these papers structure their results. Theory papers on model collapse don't use tables at all, while detection papers rely heavily on them—anywhere from six to twelve tables showing methods compared across datasets or testbeds, with the best results bolded and mostly point estimates without error bars. Engineering papers mix tables and figures more flexibly. The visualizations tend toward line plots for scaling curves and training trajectories, heatmaps for cross-model generalization, and scatter plots when showing correlations.

Looking at how ablations and qualitative comparisons are presented: detection papers use full numerical tables, collapse papers use multi-panel line plot grids, and engineering papers break things down with bar charts per component. There's a consistent narrative structure across figures—moving from motivation through main evidence, mechanism, ablation, and extensions—and some papers like tale_of_tails deliberately mirror their theory and experiments in parallel layouts. The best papers use ablation itself as a storytelling device, where each component becomes its own mini-experiment, and they frame findings in ways that highlight what prior work missed or what the practical implications really are. Looking at the existing skill files, they're already quite comprehensive from the 25-paper synthesis, but I can strengthen them by incorporating the verifier-based approaches more explicitly, clarifying the training recipe consensus, and being more specific about ablation dimensions. For the writing skill, I should emphasize the contribution framing patterns and tension strategies more prominently. Let me carefully craft updated versions that stay within the 3000-character limit while preserving the depth of the original synthesis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f442e2-8fe6-49e3-95a5-e98e897185a9",
  "isSidechain": false,
  "requestId": "req_011CbFvPL2KJTS7nF1uHjurc",
  "type": "assistant",
  "uuid": "4755e661-3cf9-4827-ae07-ba2f275ab351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AYybhsiVgC22DDhB5GDHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2166,
      "cache_read_input_tokens": 70695,
      "output_tokens": 5982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5982,
          "cache_read_input_tokens": 70695,
          "cache_creation_input_tokens": 2166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2166
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

_source line 61 · 2026-05-21T15:06:58.447Z_

Now I have all 25 papers' data loaded. The existing skills are already based on these 25 papers, but I'll regenerate with deeper cross-paper synthesis from the full YAML data I've just reviewed. Writing the updated skill files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4755e661-3cf9-4827-ae07-ba2f275ab351",
  "isSidechain": false,
  "requestId": "req_011CbFvPL2KJTS7nF1uHjurc",
  "type": "assistant",
  "uuid": "593ca40d-e28e-4bb0-a8a7-831ec43fa5f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AYybhsiVgC22DDhB5GDHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2166,
      "cache_read_input_tokens": 70695,
      "output_tokens": 5982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5982,
          "cache_read_input_tokens": 70695,
          "cache_creation_input_tokens": 2166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2166
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

_source line 62 · 2026-05-21T15:07:21.392Z_

<details open><summary>🔧 Tool call — Write · `toolu_019AXt16j9gvvNj2xM8W1yfz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md",
  "content": "# AI Text Detection & Model Collapse — Research Patterns\n\nFrom 25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.\n\n## Method Trends\n\n**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01%FPR)→DivEye (+33.2%). Each successor simplifies and accelerates. Continuous/ordinal scoring replacing binary (EditLens regression, CLOC multi-margin). Detection-as-collapse-mitigation emerging: detector-filtered retraining outperforms pure human data (Drayson 2025). Verifier-based filtering shows short-term gains but converges to verifier's center (Yi 2026, Escaping Collapse).\n\n**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93 cross-domain; Two Paradigms: attribution paradigm breaks at scale). Pure perturbation methods displaced by conditional probability approaches.\n\n## Standard Baselines (citation freq)\n\nDetectGPT (8/25) > RoBERTa-classifier (5/25) > Binoculars (4/25) ≈ Fast-DetectGPT (4/25) > Ghostbuster (3/25). New detectors must benchmark against Binoculars + Fast-DetectGPT as zero-shot SOTA, plus at least one supervised baseline. **Support**: 8/8 deep-read, high confidence.\n\n## Metrics\n\n**AUROC** dominant (12/25) but increasingly contested — Two Paradigms shows AUROC misleading under class imbalance, recommend supplementing with PR-AUC. **TPR@low-FPR** (0.01%-1%) preferred for deployment (Binoculars, Two Paradigms). **F1** for classification (6/25). Collapse domain: **FID** (4/25), **perplexity** (4/25), **test error scaling exponent** (3/25), **entropy** as diagnostic (Closer Look: r=0.91 with generalization). **Support**: 8/8, high confidence.\n\n## Key Datasets\n\nDetection: MAGE (7 domains×27 LLMs, 332K texts), RAID (2.6M texts, 6 LLMs), PAN'24 (15 LLMs). XSum/SQuAD/WritingPrompts = legacy trio (3/25 each). Collapse: CIFAR-10/FFHQ/MNIST for image (4/25), Wikitext-103/BabiStories for LM (2/25). Data quality: FineWeb 15T tokens, QuRating 260B.\n\n## Experimental Design Consensus (6/8 deep-read)\n\n1. Cross-domain + cross-model eval mandatory — in-domain results alone insufficient (MAGE, Two Paradigms, Ghostbuster)\n2. Paraphrasing attack robustness required — universal weakness, recall drops 30-40% (MAGE, Ghostbuster, DivEye)\n3. Progressive difficulty testbeds: easy→hard scenarios as narrative arc (MAGE: 8 testbeds; Two Paradigms: attribution→verification)\n4. Collapse: iterate 8-60 rounds, report per-round FID/entropy/GS trajectory, not just final number\n5. Training recipes: detection classifiers use Adam, lr~5e-3, 5 epochs on V100/A100; collapse theory uses closed-form or small DDPMs on single A100\n\n## Common Limitations (cross-paper freq)\n\n- Short text (<100 tokens): universal degradation (4/8 deep-read)\n- Newest LLMs closing gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable by non-o1 detectors (Two Paradigms)\n- Paraphrasing breaks all detectors (3/8; Ghostbuster 99%→62% recall)\n- Collapse theory assumes Gaussian/linear — neural network gap acknowledged but unresolved (4/8)\n- No instruction-tuned LLM collapse analysis across all papers\n\n## Research Gaps\n\n- **No paper estimates recursive generation depth** — detection is binary/ternary only; ordinal framing (EditLens, CLOC) exists but unapplied to depth\n- Detection × collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred\n- Strong Collapse proves mixing cannot fix collapse unless synthetic fraction→0, but no paper proposes depth-aware data curation\n- Verifier quality bounds long-term performance (Yi 2026) — what if the verifier is a generation-depth estimator?\n\n## Competitor Map\n\n**Foundation** (9): DetectGPT, Two Paradigms, Tale of Tails, Strong Collapse, Closer Look, Broken Telephone, Ghostbuster, Demystified, survey. **Competitor** (6): MAGE, Binoculars, Fast-DetectGPT, DivEye, Intrinsic Dim, EditLens. **Complementary** (7): FineWeb, QuRating, Escaping Collapse, Drayson, Synthetic Eggs, LOKI, CLOC. **Orthogonal** (2): watermark, text degeneration.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "593ca40d-e28e-4bb0-a8a7-831ec43fa5f1",
  "isSidechain": false,
  "requestId": "req_011CbFvPL2KJTS7nF1uHjurc",
  "type": "assistant",
  "uuid": "77c3dcbe-8906-4fbc-bbb3-baaad349a4ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AYybhsiVgC22DDhB5GDHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2166,
      "cache_read_input_tokens": 70695,
      "output_tokens": 5982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5982,
          "cache_read_input_tokens": 70695,
          "cache_creation_input_tokens": 2166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2166
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

_source line 63 · 2026-05-21T15:07:47.433Z_

<details><summary>↩ Tool result · `toolu_01B3YaDsLSt6RnWg57apWtcf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c78e05d-0aca-4d1b-9ed0-d699628c672f",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "a6892204-265c-4cc0-bea2-f80a26afda2e",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md",
    "content": "# AI Text Detection & Model Collapse — Writing Patterns\n\nFrom 8 deep-read papers' narrative/figure/table analysis.\n\n## Story Type & Hook\n\n**突破局限型 dominates** (7/8; all except FineWeb 化繁为简型). Frame contribution as overcoming a specific named prior limitation.\n\nThree proven hooks: (1) **Real-world urgency** — cite adoption stats (\"ChatGPT: 0.1% of daily global words\", Tale of Tails; \"schools restricting ChatGPT\", Ghostbuster). (2) **Contradiction** — juxtapose success/failure (\"detectors beat benchmarks yet OpenAI shut theirs down\", Two Paradigms). (3) **Practical inevitability** — \"synthetic contamination is unavoidable\" (Closer Look, Strong Collapse). **Support**: 8/8, high confidence.\n\n## Intro Structure (7/8 consensus)\n\n3-5 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers (\"RoBERTa: 99.4→88.3 OOD\", \"variance collapse rarely a practical concern\"). P3: approach + headline number. P4 (optional): method sketch. Contributions: 3 items (identify→analyze→validate pattern in 5/8). Exception: FineWeb uses single dense paragraph with 6 implicit contributions woven into prose. **Key rule**: quantified failure > vague criticism. Every tension paragraph cites a concrete number from prior work.\n\n## Tension Strategies\n\nDetection: **\"works in lab, fails in wild\"** (Ghostbuster, MAGE, Two Paradigms — 3/4 detection papers). Theory: **\"right but practically wrong\"** — prior theory valid but misses what practitioners observe (Closer Look: \"variance collapse rarely practical\"; Strong Collapse: \"mixing doesn't fix it\"). Cross-domain: **\"black-box constraint\"** — solving a harder, more realistic problem (Ghostbuster: no target model access). **Support**: 7/8, high confidence.\n\n## Figure 1 Design (8/8)\n\nDetection: **problem_illustration** showing combinatorial challenge (domains×models, MAGE: many-to-many arrows). Collapse: **motivation** showing degradation mechanism (Tale of Tails: three tail destruction mechanisms; Strong Collapse: Pareto diagram). Method papers: **method_overview** pipeline (Ghostbuster: L→R pipeline; Closer Look: 3-row paradigm diagram). **Teaser_result** rare (1/8, Yi). Design consensus: horizontal L→R flow, pastel color-coding by conceptual layer, minimal text, real examples grounding abstract concepts. **Support**: 8/8, high confidence.\n\n## Tables vs Figures: The Domain Split\n\n**Theory/collapse papers: zero tables** (4/4: Tale of Tails, Strong Collapse, Closer Look, Escaping Collapse). All results as line plots over iterations/scaling. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8, Two Paradigms:6). **Data engineering: mostly figures** (FineWeb: training curves as ablation). Rule: trajectories→figures, method comparisons→tables, pipeline ablations→bar charts.\n\nDetection main table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold_best, 4-10 baselines, **point estimates without std** (5/8 — std rare in this domain). **Support**: 8/8, high confidence.\n\n## Visualization Consensus\n\n**Line plots** dominant (6/8): training curves, scaling laws, collapse trajectories on log-log axes. **Heatmaps** for cross-model generalization (Two Paradigms: model×model AUROC). **Scatter** for correlation evidence (Closer Look: r=0.91 entropy-GS). **Qualitative comparison** grids for collapse (Closer Look: generated vs nearest neighbor; Escaping Collapse: with/without verification).\n\nGain highlighting: solid/dashed encoding (filtered/unfiltered, Escaping Collapse), diverging colormaps centered at 0 (improvement/degradation), theory-vs-experiment parallel layouts (Tale of Tails: Fig 3 theory → Fig 4 matching experiment layout).\n\n## Figure Narrative Arc (7/8)\n\nStandard flow: motivation → main evidence → mechanism → ablation → extension. Key patterns: **paired qualitative+quantitative** panels (Closer Look: face grids + GS curves). **Parallel theory-experiment layout** (Tale of Tails). **Progressive difficulty as narrative arc** (MAGE: 8 testbeds easy→hard). **Discover-understand-mitigate-extend** (Closer Look: 3 findings + solution). **Ablation-as-narrative** (FineWeb: each pipeline stage = mini-experiment with hypothesis+result).\n\n## Techniques Worth Stealing\n\n1. **\"Practical insufficiency\"** (Closer Look): \"prior work right but misses what matters in practice\" — avoids direct conflict while establishing novelty. **Support**: 2/8, medium confidence, but effective pattern.\n2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential mini-experiments. Counterintuitive findings (global dedup hurts) as dramatic peak. **Support**: 1/8 but universally applicable to pipeline papers.\n3. **Promise-and-peril** (Escaping Collapse): short-term good news + long-term cautionary convergence. Nuanced > pure positive-result. **Support**: 1/8 but high novelty.\n4. **Contradiction opener** (Two Paradigms): success vs failure juxtaposition in paragraph 1. **Support**: 2/8, medium confidence.\n5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to show attribution breaks — makes theoretical argument viscerally intuitive. **Support**: 1/8 but highly memorable.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 43,
        "newStart": 2,
        "newLines": 44,
        "lines": [
          " ",
          " From 8 deep-read papers' narrative/figure/table analysis.",
          " ",
          "-## Story & Hook",
          "+## Story Type & Hook",
          " ",
          "-**突破局限型 dominates** (7/8). Frame contribution as overcoming a specific named prior limitation.",
          "+**突破局限型 dominates** (7/8; all except FineWeb 化繁为简型). Frame contribution as overcoming a specific named prior limitation.",
          " ",
          "-Three proven hooks: (1) **Real-world urgency** — cite adoption stats (\"ChatGPT: 0.1% of daily global words\", Tale of Tails). (2) **Contradiction** — juxtapose success/failure evidence (\"detectors beat benchmarks yet OpenAI shut theirs down\", Two Paradigms). (3) **Practical inevitability** — \"synthetic contamination is unavoidable\" (Closer Look).",
          "+Three proven hooks: (1) **Real-world urgency** — cite adoption stats (\"ChatGPT: 0.1% of daily global words\", Tale of Tails; \"schools restricting ChatGPT\", Ghostbuster). (2) **Contradiction** — juxtapose success/failure (\"detectors beat benchmarks yet OpenAI shut theirs down\", Two Paradigms). (3) **Practical inevitability** — \"synthetic contamination is unavoidable\" (Closer Look, Strong Collapse). **Support**: 8/8, high confidence.",
          " ",
          " ## Intro Structure (7/8 consensus)",
          " ",
          "-3-4 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers (\"RoBERTa: 99.4→88.3 OOD\"). P3: approach + headline number. Contributions: 3 items (identify→analyze→validate). Quantified failure > vague criticism.",
          "+3-5 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers (\"RoBERTa: 99.4→88.3 OOD\", \"variance collapse rarely a practical concern\"). P3: approach + headline number. P4 (optional): method sketch. Contributions: 3 items (identify→analyze→validate pattern in 5/8). Exception: FineWeb uses single dense paragraph with 6 implicit contributions woven into prose. **Key rule**: quantified failure > vague criticism. Every tension paragraph cites a concrete number from prior work.",
          " ",
          " ## Tension Strategies",
          " ",
          "-Detection: **\"works in lab, fails in wild\"** (Ghostbuster, MAGE, Two Paradigms). Theory: **\"right but practically wrong\"** — prior theory valid but misses what practitioners observe (Closer Look: \"variance collapse rarely a practical concern\").",
          "+Detection: **\"works in lab, fails in wild\"** (Ghostbuster, MAGE, Two Paradigms — 3/4 detection papers). Theory: **\"right but practically wrong\"** — prior theory valid but misses what practitioners observe (Closer Look: \"variance collapse rarely practical\"; Strong Collapse: \"mixing doesn't fix it\"). Cross-domain: **\"black-box constraint\"** — solving a harder, more realistic problem (Ghostbuster: no target model access). **Support**: 7/8, high confidence.",
          " ",
          " ## Figure 1 Design (8/8)",
          " ",
          "-Detection: **problem illustration** showing combinatorial challenge (domains×models). Collapse: **motivation figure** showing degradation mechanism. Design consensus: horizontal L→R flow, pastel color-coding, minimal text, real examples grounding abstract concepts.",
          "+Detection: **problem_illustration** showing combinatorial challenge (domains×models, MAGE: many-to-many arrows). Collapse: **motivation** showing degradation mechanism (Tale of Tails: three tail destruction mechanisms; Strong Collapse: Pareto diagram). Method papers: **method_overview** pipeline (Ghostbuster: L→R pipeline; Closer Look: 3-row paradigm diagram). **Teaser_result** rare (1/8, Yi). Design consensus: horizontal L→R flow, pastel color-coding by conceptual layer, minimal text, real examples grounding abstract concepts. **Support**: 8/8, high confidence.",
          " ",
          " ## Tables vs Figures: The Domain Split",
          " ",
          "-**Theory/collapse papers: zero tables** (4/4). All results as line plots over iterations. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8). Rule: trajectories→figures, method comparisons→tables.",
          "+**Theory/collapse papers: zero tables** (4/4: Tale of Tails, Strong Collapse, Closer Look, Escaping Collapse). All results as line plots over iterations/scaling. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8, Two Paradigms:6). **Data engineering: mostly figures** (FineWeb: training curves as ablation). Rule: trajectories→figures, method comparisons→tables, pipeline ablations→bar charts.",
          " ",
          "-Detection tables: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold best, 4-10 baselines, point estimates (no std in 5/8).",
          "+Detection main table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold_best, 4-10 baselines, **point estimates without std** (5/8 — std rare in this domain). **Support**: 8/8, high confidence.",
          " ",
          " ## Visualization Consensus",
          " ",
          "-**Line plots** dominant (6/8): training curves, scaling laws. **Heatmaps** for cross-model matrices. **Scatter** for correlation evidence (r=0.91 entropy-GS). Gain highlighting: solid/dashed (filtered/unfiltered), diverging colormaps, log-log for power laws.",
          "+**Line plots** dominant (6/8): training curves, scaling laws, collapse trajectories on log-log axes. **Heatmaps** for cross-model generalization (Two Paradigms: model×model AUROC). **Scatter** for correlation evidence (Closer Look: r=0.91 entropy-GS). **Qualitative comparison** grids for collapse (Closer Look: generated vs nearest neighbor; Escaping Collapse: with/without verification).",
          " ",
          "-Ablations: detection→full number tables; collapse→multi-panel line plot grids (datasets×paradigms); engineering→bar charts per component.",
          "+Gain highlighting: solid/dashed encoding (filtered/unfiltered, Escaping Collapse), diverging colormaps centered at 0 (improvement/degradation), theory-vs-experiment parallel layouts (Tale of Tails: Fig 3 theory → Fig 4 matching experiment layout).",
          " ",
          " ## Figure Narrative Arc (7/8)",
          " ",
          "-Standard: motivation→main evidence→mechanism→ablation→extension. Key techniques: **paired qualitative+quantitative** panels (Closer Look); **parallel theory-vs-experiment layout** (Tale of Tails); **progressive difficulty** as narrative arc (MAGE: 8 testbeds easy→hard).",
          "+Standard flow: motivation → main evidence → mechanism → ablation → extension. Key patterns: **paired qualitative+quantitative** panels (Closer Look: face grids + GS curves). **Parallel theory-experiment layout** (Tale of Tails). **Progressive difficulty as narrative arc** (MAGE: 8 testbeds easy→hard). **Discover-understand-mitigate-extend** (Closer Look: 3 findings + solution). **Ablation-as-narrative** (FineWeb: each pipeline stage = mini-experiment with hypothesis+result).",
          " ",
          " ## Techniques Worth Stealing",
          " ",
          "-1. **\"Practical insufficiency\"** (Closer Look): \"prior work right but misses what matters\"",
          "-2. **Ablation-as-narrative** (FineWeb): each pipeline stage = mini-experiment",
          "-3. **Promise-and-peril** (Escaping Collapse): short-term good + long-term caution",
          "-4. **Contradiction opener** (Two Paradigms): success vs failure in paragraph 1",
          "+1. **\"Practical insufficiency\"** (Closer Look): \"prior work right but misses what matters in practice\" — avoids direct conflict while establishing novelty. **Support**: 2/8, medium confidence, but effective pattern.",
          "+2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential mini-experiments. Counterintuitive findings (global dedup hurts) as dramatic peak. **Support**: 1/8 but universally applicable to pipeline papers.",
          "+3. **Promise-and-peril** (Escaping Collapse): short-term good news + long-term cautionary convergence. Nuanced > pure positive-result. **Support**: 1/8 but high novelty.",
          "+4. **Contradiction opener** (Two Paradigms): success vs failure juxtaposition in paragraph 1. **Support**: 2/8, medium confidence.",
          "+5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to show attribution breaks — makes theoretical argument viscerally intuitive. **Support**: 1/8 but highly memorable."
        ]
      }
    ],
    "originalFile": "# AI Text Detection & Model Collapse — Writing Patterns\n\nFrom 8 deep-read papers' narrative/figure/table analysis.\n\n## Story & Hook\n\n**突破局限型 dominates** (7/8). Frame contribution as overcoming a specific named prior limitation.\n\nThree proven hooks: (1) **Real-world urgency** — cite adoption stats (\"ChatGPT: 0.1% of daily global words\", Tale of Tails). (2) **Contradiction** — juxtapose success/failure evidence (\"detectors beat benchmarks yet OpenAI shut theirs down\", Two Paradigms). (3) **Practical inevitability** — \"synthetic contamination is unavoidable\" (Closer Look).\n\n## Intro Structure (7/8 consensus)\n\n3-4 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers (\"RoBERTa: 99.4→88.3 OOD\"). P3: approach + headline number. Contributions: 3 items (identify→analyze→validate). Quantified failure > vague criticism.\n\n## Tension Strategies\n\nDetection: **\"works in lab, fails in wild\"** (Ghostbuster, MAGE, Two Paradigms). Theory: **\"right but practically wrong\"** — prior theory valid but misses what practitioners observe (Closer Look: \"variance collapse rarely a practical concern\").\n\n## Figure 1 Design (8/8)\n\nDetection: **problem illustration** showing combinatorial challenge (domains×models). Collapse: **motivation figure** showing degradation mechanism. Design consensus: horizontal L→R flow, pastel color-coding, minimal text, real examples grounding abstract concepts.\n\n## Tables vs Figures: The Domain Split\n\n**Theory/collapse papers: zero tables** (4/4). All results as line plots over iterations. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8). Rule: trajectories→figures, method comparisons→tables.\n\nDetection tables: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold best, 4-10 baselines, point estimates (no std in 5/8).\n\n## Visualization Consensus\n\n**Line plots** dominant (6/8): training curves, scaling laws. **Heatmaps** for cross-model matrices. **Scatter** for correlation evidence (r=0.91 entropy-GS). Gain highlighting: solid/dashed (filtered/unfiltered), diverging colormaps, log-log for power laws.\n\nAblations: detection→full number tables; collapse→multi-panel line plot grids (datasets×paradigms); engineering→bar charts per component.\n\n## Figure Narrative Arc (7/8)\n\nStandard: motivation→main evidence→mechanism→ablation→extension. Key techniques: **paired qualitative+quantitative** panels (Closer Look); **parallel theory-vs-experiment layout** (Tale of Tails); **progressive difficulty** as narrative arc (MAGE: 8 testbeds easy→hard).\n\n## Techniques Worth Stealing\n\n1. **\"Practical insufficiency\"** (Closer Look): \"prior work right but misses what matters\"\n2. **Ablation-as-narrative** (FineWeb): each pipeline stage = mini-experiment\n3. **Promise-and-peril** (Escaping Collapse): short-term good + long-term caution\n4. **Contradiction opener** (Two Paradigms): success vs failure in paragraph 1\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "3c78e05d-0aca-4d1b-9ed0-d699628c672f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T15:07:21.422Z_

<details><summary>↩ Tool result · `toolu_019AXt16j9gvvNj2xM8W1yfz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77c3dcbe-8906-4fbc-bbb3-baaad349a4ab",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "e31e766d-fba1-45db-bf7e-1f0984ed6abd",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md",
    "content": "# AI Text Detection & Model Collapse — Research Patterns\n\nFrom 25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.\n\n## Method Trends\n\n**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01%FPR)→DivEye (+33.2%). Each successor simplifies and accelerates. Continuous/ordinal scoring replacing binary (EditLens regression, CLOC multi-margin). Detection-as-collapse-mitigation emerging: detector-filtered retraining outperforms pure human data (Drayson 2025). Verifier-based filtering shows short-term gains but converges to verifier's center (Yi 2026, Escaping Collapse).\n\n**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93 cross-domain; Two Paradigms: attribution paradigm breaks at scale). Pure perturbation methods displaced by conditional probability approaches.\n\n## Standard Baselines (citation freq)\n\nDetectGPT (8/25) > RoBERTa-classifier (5/25) > Binoculars (4/25) ≈ Fast-DetectGPT (4/25) > Ghostbuster (3/25). New detectors must benchmark against Binoculars + Fast-DetectGPT as zero-shot SOTA, plus at least one supervised baseline. **Support**: 8/8 deep-read, high confidence.\n\n## Metrics\n\n**AUROC** dominant (12/25) but increasingly contested — Two Paradigms shows AUROC misleading under class imbalance, recommend supplementing with PR-AUC. **TPR@low-FPR** (0.01%-1%) preferred for deployment (Binoculars, Two Paradigms). **F1** for classification (6/25). Collapse domain: **FID** (4/25), **perplexity** (4/25), **test error scaling exponent** (3/25), **entropy** as diagnostic (Closer Look: r=0.91 with generalization). **Support**: 8/8, high confidence.\n\n## Key Datasets\n\nDetection: MAGE (7 domains×27 LLMs, 332K texts), RAID (2.6M texts, 6 LLMs), PAN'24 (15 LLMs). XSum/SQuAD/WritingPrompts = legacy trio (3/25 each). Collapse: CIFAR-10/FFHQ/MNIST for image (4/25), Wikitext-103/BabiStories for LM (2/25). Data quality: FineWeb 15T tokens, QuRating 260B.\n\n## Experimental Design Consensus (6/8 deep-read)\n\n1. Cross-domain + cross-model eval mandatory — in-domain results alone insufficient (MAGE, Two Paradigms, Ghostbuster)\n2. Paraphrasing attack robustness required — universal weakness, recall drops 30-40% (MAGE, Ghostbuster, DivEye)\n3. Progressive difficulty testbeds: easy→hard scenarios as narrative arc (MAGE: 8 testbeds; Two Paradigms: attribution→verification)\n4. Collapse: iterate 8-60 rounds, report per-round FID/entropy/GS trajectory, not just final number\n5. Training recipes: detection classifiers use Adam, lr~5e-3, 5 epochs on V100/A100; collapse theory uses closed-form or small DDPMs on single A100\n\n## Common Limitations (cross-paper freq)\n\n- Short text (<100 tokens): universal degradation (4/8 deep-read)\n- Newest LLMs closing gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable by non-o1 detectors (Two Paradigms)\n- Paraphrasing breaks all detectors (3/8; Ghostbuster 99%→62% recall)\n- Collapse theory assumes Gaussian/linear — neural network gap acknowledged but unresolved (4/8)\n- No instruction-tuned LLM collapse analysis across all papers\n\n## Research Gaps\n\n- **No paper estimates recursive generation depth** — detection is binary/ternary only; ordinal framing (EditLens, CLOC) exists but unapplied to depth\n- Detection × collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred\n- Strong Collapse proves mixing cannot fix collapse unless synthetic fraction→0, but no paper proposes depth-aware data curation\n- Verifier quality bounds long-term performance (Yi 2026) — what if the verifier is a generation-depth estimator?\n\n## Competitor Map\n\n**Foundation** (9): DetectGPT, Two Paradigms, Tale of Tails, Strong Collapse, Closer Look, Broken Telephone, Ghostbuster, Demystified, survey. **Competitor** (6): MAGE, Binoculars, Fast-DetectGPT, DivEye, Intrinsic Dim, EditLens. **Complementary** (7): FineWeb, QuRating, Escaping Collapse, Drayson, Synthetic Eggs, LOKI, CLOC. **Orthogonal** (2): watermark, text degeneration.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 42,
        "newStart": 4,
        "newLines": 44,
        "lines": [
          " ",
          " ## Method Trends",
          " ",
          "-**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01% FPR)→DivEye (+33.2%). Continuous/ordinal scoring replacing binary (EditLens, CLOC). Detection-as-collapse-mitigation: filtering synthetic data via detectors outperforms pure human training (Drayson 2025).",
          "+**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01%FPR)→DivEye (+33.2%). Each successor simplifies and accelerates. Continuous/ordinal scoring replacing binary (EditLens regression, CLOC multi-margin). Detection-as-collapse-mitigation emerging: detector-filtered retraining outperforms pure human data (Drayson 2025). Verifier-based filtering shows short-term gains but converges to verifier's center (Yi 2026, Escaping Collapse).",
          " ",
          "-**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93; Two Paradigms: attribution breaks at scale).",
          "+**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93 cross-domain; Two Paradigms: attribution paradigm breaks at scale). Pure perturbation methods displaced by conditional probability approaches.",
          " ",
          " ## Standard Baselines (citation freq)",
          " ",
          "-DetectGPT (8/25) > RoBERTa (5/25) > Binoculars (4/25) > Fast-DetectGPT (4/25). New detectors must compare against Binoculars + Fast-DetectGPT as zero-shot SOTA.",
          "+DetectGPT (8/25) > RoBERTa-classifier (5/25) > Binoculars (4/25) ≈ Fast-DetectGPT (4/25) > Ghostbuster (3/25). New detectors must benchmark against Binoculars + Fast-DetectGPT as zero-shot SOTA, plus at least one supervised baseline. **Support**: 8/8 deep-read, high confidence.",
          " ",
          " ## Metrics",
          " ",
          "-**AUROC** dominant (12/25). **F1** second (6/25). **TPR@low-FPR** increasingly preferred for deployment. Two Paradigms: AUROC misleading under class imbalance, supplement with PR-AUC. Collapse: FID (4/25), perplexity (4/25).",
          "+**AUROC** dominant (12/25) but increasingly contested — Two Paradigms shows AUROC misleading under class imbalance, recommend supplementing with PR-AUC. **TPR@low-FPR** (0.01%-1%) preferred for deployment (Binoculars, Two Paradigms). **F1** for classification (6/25). Collapse domain: **FID** (4/25), **perplexity** (4/25), **test error scaling exponent** (3/25), **entropy** as diagnostic (Closer Look: r=0.91 with generalization). **Support**: 8/8, high confidence.",
          " ",
          " ## Key Datasets",
          " ",
          "-Detection: MAGE (7 domains×27 LLMs), RAID (2.6M texts), PAN'24. Collapse: CIFAR-10/FFHQ/MNIST (image), Wikitext-103/BabiStories (LM). Data quality: FineWeb (15T tokens).",
          "+Detection: MAGE (7 domains×27 LLMs, 332K texts), RAID (2.6M texts, 6 LLMs), PAN'24 (15 LLMs). XSum/SQuAD/WritingPrompts = legacy trio (3/25 each). Collapse: CIFAR-10/FFHQ/MNIST for image (4/25), Wikitext-103/BabiStories for LM (2/25). Data quality: FineWeb 15T tokens, QuRating 260B.",
          " ",
          " ## Experimental Design Consensus (6/8 deep-read)",
          " ",
          "-1. Cross-domain + cross-model eval mandatory",
          "-2. Paraphrasing attack robustness required (drops recall 30-40%)",
          "-3. Progressive difficulty testbeds (MAGE: 8 scenarios easy→hard)",
          "-4. Collapse: iterate 8-60 rounds with per-round FID/entropy",
          "+1. Cross-domain + cross-model eval mandatory — in-domain results alone insufficient (MAGE, Two Paradigms, Ghostbuster)",
          "+2. Paraphrasing attack robustness required — universal weakness, recall drops 30-40% (MAGE, Ghostbuster, DivEye)",
          "+3. Progressive difficulty testbeds: easy→hard scenarios as narrative arc (MAGE: 8 testbeds; Two Paradigms: attribution→verification)",
          "+4. Collapse: iterate 8-60 rounds, report per-round FID/entropy/GS trajectory, not just final number",
          "+5. Training recipes: detection classifiers use Adam, lr~5e-3, 5 epochs on V100/A100; collapse theory uses closed-form or small DDPMs on single A100",
          " ",
          " ## Common Limitations (cross-paper freq)",
          " ",
          "-- Short text (<100 tokens): all detectors degrade (4/8)",
          "-- Newest LLMs close gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable (Two Paradigms)",
          "-- Paraphrasing universal attack (3/8)",
          "-- Collapse theory assumes Gaussian/linear — practice gap (3/8)",
          "+- Short text (<100 tokens): universal degradation (4/8 deep-read)",
          "+- Newest LLMs closing gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable by non-o1 detectors (Two Paradigms)",
          "+- Paraphrasing breaks all detectors (3/8; Ghostbuster 99%→62% recall)",
          "+- Collapse theory assumes Gaussian/linear — neural network gap acknowledged but unresolved (4/8)",
          "+- No instruction-tuned LLM collapse analysis across all papers",
          " ",
          " ## Research Gaps",
          " ",
          "-- **No paper estimates recursive generation depth** — detection is binary/ternary only",
          "-- Detection×collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred",
          "-- Ordinal framing (EditLens, CLOC) not applied to generation depth",
          "-- No collapse analysis for instruction-tuned LLMs",
          "+- **No paper estimates recursive generation depth** — detection is binary/ternary only; ordinal framing (EditLens, CLOC) exists but unapplied to depth",
          "+- Detection × collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred",
          "+- Strong Collapse proves mixing cannot fix collapse unless synthetic fraction→0, but no paper proposes depth-aware data curation",
          "+- Verifier quality bounds long-term performance (Yi 2026) — what if the verifier is a generation-depth estimator?",
          " ",
          " ## Competitor Map",
          " "
        ]
      }
    ],
    "originalFile": "# AI Text Detection & Model Collapse — Research Patterns\n\nFrom 25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.\n\n## Method Trends\n\n**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01% FPR)→DivEye (+33.2%). Continuous/ordinal scoring replacing binary (EditLens, CLOC). Detection-as-collapse-mitigation: filtering synthetic data via detectors outperforms pure human training (Drayson 2025).\n\n**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93; Two Paradigms: attribution breaks at scale).\n\n## Standard Baselines (citation freq)\n\nDetectGPT (8/25) > RoBERTa (5/25) > Binoculars (4/25) > Fast-DetectGPT (4/25). New detectors must compare against Binoculars + Fast-DetectGPT as zero-shot SOTA.\n\n## Metrics\n\n**AUROC** dominant (12/25). **F1** second (6/25). **TPR@low-FPR** increasingly preferred for deployment. Two Paradigms: AUROC misleading under class imbalance, supplement with PR-AUC. Collapse: FID (4/25), perplexity (4/25).\n\n## Key Datasets\n\nDetection: MAGE (7 domains×27 LLMs), RAID (2.6M texts), PAN'24. Collapse: CIFAR-10/FFHQ/MNIST (image), Wikitext-103/BabiStories (LM). Data quality: FineWeb (15T tokens).\n\n## Experimental Design Consensus (6/8 deep-read)\n\n1. Cross-domain + cross-model eval mandatory\n2. Paraphrasing attack robustness required (drops recall 30-40%)\n3. Progressive difficulty testbeds (MAGE: 8 scenarios easy→hard)\n4. Collapse: iterate 8-60 rounds with per-round FID/entropy\n\n## Common Limitations (cross-paper freq)\n\n- Short text (<100 tokens): all detectors degrade (4/8)\n- Newest LLMs close gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable (Two Paradigms)\n- Paraphrasing universal attack (3/8)\n- Collapse theory assumes Gaussian/linear — practice gap (3/8)\n\n## Research Gaps\n\n- **No paper estimates recursive generation depth** — detection is binary/ternary only\n- Detection×collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred\n- Ordinal framing (EditLens, CLOC) not applied to generation depth\n- No collapse analysis for instruction-tuned LLMs\n\n## Competitor Map\n\n**Foundation** (9): DetectGPT, Two Paradigms, Tale of Tails, Strong Collapse, Closer Look, Broken Telephone, Ghostbuster, Demystified, survey. **Competitor** (6): MAGE, Binoculars, Fast-DetectGPT, DivEye, Intrinsic Dim, EditLens. **Complementary** (7): FineWeb, QuRating, Escaping Collapse, Drayson, Synthetic Eggs, LOKI, CLOC. **Orthogonal** (2): watermark, text degeneration.\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "77c3dcbe-8906-4fbc-bbb3-baaad349a4ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T15:07:47.418Z_

<details open><summary>🔧 Tool call — Write · `toolu_01B3YaDsLSt6RnWg57apWtcf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md",
  "content": "# AI Text Detection & Model Collapse — Writing Patterns\n\nFrom 8 deep-read papers' narrative/figure/table analysis.\n\n## Story Type & Hook\n\n**突破局限型 dominates** (7/8; all except FineWeb 化繁为简型). Frame contribution as overcoming a specific named prior limitation.\n\nThree proven hooks: (1) **Real-world urgency** — cite adoption stats (\"ChatGPT: 0.1% of daily global words\", Tale of Tails; \"schools restricting ChatGPT\", Ghostbuster). (2) **Contradiction** — juxtapose success/failure (\"detectors beat benchmarks yet OpenAI shut theirs down\", Two Paradigms). (3) **Practical inevitability** — \"synthetic contamination is unavoidable\" (Closer Look, Strong Collapse). **Support**: 8/8, high confidence.\n\n## Intro Structure (7/8 consensus)\n\n3-5 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers (\"RoBERTa: 99.4→88.3 OOD\", \"variance collapse rarely a practical concern\"). P3: approach + headline number. P4 (optional): method sketch. Contributions: 3 items (identify→analyze→validate pattern in 5/8). Exception: FineWeb uses single dense paragraph with 6 implicit contributions woven into prose. **Key rule**: quantified failure > vague criticism. Every tension paragraph cites a concrete number from prior work.\n\n## Tension Strategies\n\nDetection: **\"works in lab, fails in wild\"** (Ghostbuster, MAGE, Two Paradigms — 3/4 detection papers). Theory: **\"right but practically wrong\"** — prior theory valid but misses what practitioners observe (Closer Look: \"variance collapse rarely practical\"; Strong Collapse: \"mixing doesn't fix it\"). Cross-domain: **\"black-box constraint\"** — solving a harder, more realistic problem (Ghostbuster: no target model access). **Support**: 7/8, high confidence.\n\n## Figure 1 Design (8/8)\n\nDetection: **problem_illustration** showing combinatorial challenge (domains×models, MAGE: many-to-many arrows). Collapse: **motivation** showing degradation mechanism (Tale of Tails: three tail destruction mechanisms; Strong Collapse: Pareto diagram). Method papers: **method_overview** pipeline (Ghostbuster: L→R pipeline; Closer Look: 3-row paradigm diagram). **Teaser_result** rare (1/8, Yi). Design consensus: horizontal L→R flow, pastel color-coding by conceptual layer, minimal text, real examples grounding abstract concepts. **Support**: 8/8, high confidence.\n\n## Tables vs Figures: The Domain Split\n\n**Theory/collapse papers: zero tables** (4/4: Tale of Tails, Strong Collapse, Closer Look, Escaping Collapse). All results as line plots over iterations/scaling. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8, Two Paradigms:6). **Data engineering: mostly figures** (FineWeb: training curves as ablation). Rule: trajectories→figures, method comparisons→tables, pipeline ablations→bar charts.\n\nDetection main table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold_best, 4-10 baselines, **point estimates without std** (5/8 — std rare in this domain). **Support**: 8/8, high confidence.\n\n## Visualization Consensus\n\n**Line plots** dominant (6/8): training curves, scaling laws, collapse trajectories on log-log axes. **Heatmaps** for cross-model generalization (Two Paradigms: model×model AUROC). **Scatter** for correlation evidence (Closer Look: r=0.91 entropy-GS). **Qualitative comparison** grids for collapse (Closer Look: generated vs nearest neighbor; Escaping Collapse: with/without verification).\n\nGain highlighting: solid/dashed encoding (filtered/unfiltered, Escaping Collapse), diverging colormaps centered at 0 (improvement/degradation), theory-vs-experiment parallel layouts (Tale of Tails: Fig 3 theory → Fig 4 matching experiment layout).\n\n## Figure Narrative Arc (7/8)\n\nStandard flow: motivation → main evidence → mechanism → ablation → extension. Key patterns: **paired qualitative+quantitative** panels (Closer Look: face grids + GS curves). **Parallel theory-experiment layout** (Tale of Tails). **Progressive difficulty as narrative arc** (MAGE: 8 testbeds easy→hard). **Discover-understand-mitigate-extend** (Closer Look: 3 findings + solution). **Ablation-as-narrative** (FineWeb: each pipeline stage = mini-experiment with hypothesis+result).\n\n## Techniques Worth Stealing\n\n1. **\"Practical insufficiency\"** (Closer Look): \"prior work right but misses what matters in practice\" — avoids direct conflict while establishing novelty. **Support**: 2/8, medium confidence, but effective pattern.\n2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential mini-experiments. Counterintuitive findings (global dedup hurts) as dramatic peak. **Support**: 1/8 but universally applicable to pipeline papers.\n3. **Promise-and-peril** (Escaping Collapse): short-term good news + long-term cautionary convergence. Nuanced > pure positive-result. **Support**: 1/8 but high novelty.\n4. **Contradiction opener** (Two Paradigms): success vs failure juxtaposition in paragraph 1. **Support**: 2/8, medium confidence.\n5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to show attribution breaks — makes theoretical argument viscerally intuitive. **Support**: 1/8 but highly memorable.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e31e766d-fba1-45db-bf7e-1f0984ed6abd",
  "isSidechain": false,
  "requestId": "req_011CbFvPL2KJTS7nF1uHjurc",
  "type": "assistant",
  "uuid": "3c78e05d-0aca-4d1b-9ed0-d699628c672f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AYybhsiVgC22DDhB5GDHW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2166,
      "cache_read_input_tokens": 70695,
      "output_tokens": 5982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2166,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5982,
          "cache_read_input_tokens": 70695,
          "cache_creation_input_tokens": 2166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2166
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

_source line 66 · 2026-05-21T15:07:47.520Z_

```json
{
  "parentUuid": "a6892204-265c-4cc0-bea2-f80a26afda2e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "67188ca0-96c2-47b8-ae17-080fb7b26eb9",
  "timestamp": "2026-05-21T15:07:47.520Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "67188ca0-96c2-47b8-ae17-080fb7b26eb9",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Assistant

_source line 69 · 2026-05-21T15:07:50.276Z_

验证字符数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67188ca0-96c2-47b8-ae17-080fb7b26eb9",
  "isSidechain": false,
  "requestId": "req_011CbFvXPGFnfSYwxVD8R7BB",
  "type": "assistant",
  "uuid": "dd075241-368e-4d2c-b09f-390400d9cb94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185Wke9fqnYfQHyQfMX1Xs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6227,
      "cache_read_input_tokens": 72861,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 72861,
          "cache_creation_input_tokens": 6227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6227
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

_source line 70 · 2026-05-21T15:07:51.224Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014FWQrYhngAmYdjyv37hNDA`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md",
  "description": "Check character counts of skill files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd075241-368e-4d2c-b09f-390400d9cb94",
  "isSidechain": false,
  "requestId": "req_011CbFvXPGFnfSYwxVD8R7BB",
  "type": "assistant",
  "uuid": "b5d6b630-b277-4159-8a27-24758996ee53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185Wke9fqnYfQHyQfMX1Xs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6227,
      "cache_read_input_tokens": 72861,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 72861,
          "cache_creation_input_tokens": 6227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6227
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

_source line 71 · 2026-05-21T15:07:51.298Z_

<details><summary>↩ Tool result · `toolu_014FWQrYhngAmYdjyv37hNDA`</summary>

```text
4113 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md
5210 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md
9323 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5d6b630-b277-4159-8a27-24758996ee53",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "3dd22fb4-e079-4d65-b09b-b6c708823eb1",
  "toolUseResult": {
    "stdout": "4113 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md\n5210 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md\n9323 total",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b5d6b630-b277-4159-8a27-24758996ee53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-21T15:07:58.407Z_

两个文件都超出 3000 字符限制。需要精简。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dd22fb4-e079-4d65-b09b-b6c708823eb1",
  "isSidechain": false,
  "requestId": "req_011CbFvXfPcyUBtamydu3Stj",
  "type": "assistant",
  "uuid": "f15aa5b4-f833-4bd5-bcd2-82ab292f3e3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9L7dysGksAth1A9GMFPHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 79088,
      "output_tokens": 1955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1955,
          "cache_read_input_tokens": 79088,
          "cache_creation_input_tokens": 268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 268
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

_source line 73 · 2026-05-21T15:08:05.488Z_

<details open><summary>🔧 Tool call — Write · `toolu_01UnDLtmHSsyb2gBEmmc9R6K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md",
  "content": "# AI Text Detection & Model Collapse — Research Patterns\n\n25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.\n\n## Method Trends\n\n**Rising**: Zero-shot statistical scoring: DetectGPT→Fast-DetectGPT(340x)→Binoculars(>90%@0.01%FPR)→DivEye(+33.2%). Continuous/ordinal replacing binary (EditLens, CLOC). Detection-as-collapse-mitigation (Drayson 2025). Verifier-based filtering: short-term gains, long-term converges to verifier center (Yi 2026). **Declining**: Supervised binary classifiers OOD (MAGE: 0.99→0.93 AUROC). Support: 8/8, high.\n\n## Baselines & Metrics\n\nDetectGPT(8/25)>RoBERTa(5/25)>Binoculars≈Fast-DetectGPT(4/25). New work must benchmark Binoculars+Fast-DetectGPT.\n\nAUROC dominant(12/25) but misleading under imbalance(Two Paradigms)—supplement PR-AUC. TPR@low-FPR for deployment. Collapse: FID(4/25), perplexity(4/25), entropy as diagnostic(r=0.91, Closer Look). Support: high.\n\n## Datasets\n\nDetection: MAGE(7dom×27LLM), RAID(2.6M), PAN'24(15LLM). Legacy trio: XSum/SQuAD/WritingPrompts. Collapse: CIFAR-10/FFHQ/MNIST(image), Wikitext-103/BabiStories(LM). Quality: FineWeb 15T tokens.\n\n## Experimental Consensus (6/8)\n\n1. Cross-domain+cross-model eval mandatory (MAGE,Two Paradigms,Ghostbuster)\n2. Paraphrasing robustness required—recall drops 30-40% (MAGE,Ghostbuster,DivEye)\n3. Progressive difficulty testbeds as narrative (MAGE:8 scenarios)\n4. Collapse: 8-60 rounds, per-round FID/entropy trajectory\n\n## Common Limitations\n\nShort text <100 tokens: universal degradation (4/8). Newest LLMs closing gap: GPT-4o entropy≈human >4K chars; o1 undetectable (Two Paradigms). Paraphrasing breaks all (3/8; Ghostbuster 99→62%). Theory assumes Gaussian/linear (4/8).\n\n## Research Gaps\n\n- **No paper estimates recursive generation depth**—detection binary/ternary only\n- Detection×collapse barely connected (only Drayson); no work diagnoses how many generations\n- Ordinal framing (EditLens,CLOC) unapplied to depth\n- Strong Collapse proves mixing fails unless synthetic→0, but no depth-aware curation proposed\n\n## Competitor Map\n\nFoundation(9): DetectGPT,Two Paradigms,Tale of Tails,Strong Collapse,Closer Look,Broken Telephone,Ghostbuster,Demystified,survey. Competitor(6): MAGE,Binoculars,Fast-DetectGPT,DivEye,Intrinsic Dim,EditLens. Complementary(7): FineWeb,QuRating,Escaping Collapse,Drayson,Synthetic Eggs,LOKI,CLOC. Orthogonal(2): watermark,text degeneration.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f15aa5b4-f833-4bd5-bcd2-82ab292f3e3c",
  "isSidechain": false,
  "requestId": "req_011CbFvXfPcyUBtamydu3Stj",
  "type": "assistant",
  "uuid": "72474277-3193-4024-812b-7c5c5fd04d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9L7dysGksAth1A9GMFPHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 79088,
      "output_tokens": 1955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1955,
          "cache_read_input_tokens": 79088,
          "cache_creation_input_tokens": 268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 268
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

_source line 74 · 2026-05-21T15:08:05.516Z_

<details><summary>↩ Tool result · `toolu_01UnDLtmHSsyb2gBEmmc9R6K`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72474277-3193-4024-812b-7c5c5fd04d00",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "4291a7ea-984c-4c16-878d-99a21c67ce68",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md",
    "content": "# AI Text Detection & Model Collapse — Research Patterns\n\n25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.\n\n## Method Trends\n\n**Rising**: Zero-shot statistical scoring: DetectGPT→Fast-DetectGPT(340x)→Binoculars(>90%@0.01%FPR)→DivEye(+33.2%). Continuous/ordinal replacing binary (EditLens, CLOC). Detection-as-collapse-mitigation (Drayson 2025). Verifier-based filtering: short-term gains, long-term converges to verifier center (Yi 2026). **Declining**: Supervised binary classifiers OOD (MAGE: 0.99→0.93 AUROC). Support: 8/8, high.\n\n## Baselines & Metrics\n\nDetectGPT(8/25)>RoBERTa(5/25)>Binoculars≈Fast-DetectGPT(4/25). New work must benchmark Binoculars+Fast-DetectGPT.\n\nAUROC dominant(12/25) but misleading under imbalance(Two Paradigms)—supplement PR-AUC. TPR@low-FPR for deployment. Collapse: FID(4/25), perplexity(4/25), entropy as diagnostic(r=0.91, Closer Look). Support: high.\n\n## Datasets\n\nDetection: MAGE(7dom×27LLM), RAID(2.6M), PAN'24(15LLM). Legacy trio: XSum/SQuAD/WritingPrompts. Collapse: CIFAR-10/FFHQ/MNIST(image), Wikitext-103/BabiStories(LM). Quality: FineWeb 15T tokens.\n\n## Experimental Consensus (6/8)\n\n1. Cross-domain+cross-model eval mandatory (MAGE,Two Paradigms,Ghostbuster)\n2. Paraphrasing robustness required—recall drops 30-40% (MAGE,Ghostbuster,DivEye)\n3. Progressive difficulty testbeds as narrative (MAGE:8 scenarios)\n4. Collapse: 8-60 rounds, per-round FID/entropy trajectory\n\n## Common Limitations\n\nShort text <100 tokens: universal degradation (4/8). Newest LLMs closing gap: GPT-4o entropy≈human >4K chars; o1 undetectable (Two Paradigms). Paraphrasing breaks all (3/8; Ghostbuster 99→62%). Theory assumes Gaussian/linear (4/8).\n\n## Research Gaps\n\n- **No paper estimates recursive generation depth**—detection binary/ternary only\n- Detection×collapse barely connected (only Drayson); no work diagnoses how many generations\n- Ordinal framing (EditLens,CLOC) unapplied to depth\n- Strong Collapse proves mixing fails unless synthetic→0, but no depth-aware curation proposed\n\n## Competitor Map\n\nFoundation(9): DetectGPT,Two Paradigms,Tale of Tails,Strong Collapse,Closer Look,Broken Telephone,Ghostbuster,Demystified,survey. Competitor(6): MAGE,Binoculars,Fast-DetectGPT,DivEye,Intrinsic Dim,EditLens. Complementary(7): FineWeb,QuRating,Escaping Collapse,Drayson,Synthetic Eggs,LOKI,CLOC. Orthogonal(2): watermark,text degeneration.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 48,
        "newStart": 1,
        "newLines": 39,
        "lines": [
          " # AI Text Detection & Model Collapse — Research Patterns",
          " ",
          "-From 25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.",
          "+25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.",
          " ",
          " ## Method Trends",
          " ",
          "-**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01%FPR)→DivEye (+33.2%). Each successor simplifies and accelerates. Continuous/ordinal scoring replacing binary (EditLens regression, CLOC multi-margin). Detection-as-collapse-mitigation emerging: detector-filtered retraining outperforms pure human data (Drayson 2025). Verifier-based filtering shows short-term gains but converges to verifier's center (Yi 2026, Escaping Collapse).",
          "+**Rising**: Zero-shot statistical scoring: DetectGPT→Fast-DetectGPT(340x)→Binoculars(>90%@0.01%FPR)→DivEye(+33.2%). Continuous/ordinal replacing binary (EditLens, CLOC). Detection-as-collapse-mitigation (Drayson 2025). Verifier-based filtering: short-term gains, long-term converges to verifier center (Yi 2026). **Declining**: Supervised binary classifiers OOD (MAGE: 0.99→0.93 AUROC). Support: 8/8, high.",
          " ",
          "-**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93 cross-domain; Two Paradigms: attribution paradigm breaks at scale). Pure perturbation methods displaced by conditional probability approaches.",
          "+## Baselines & Metrics",
          " ",
          "-## Standard Baselines (citation freq)",
          "+DetectGPT(8/25)>RoBERTa(5/25)>Binoculars≈Fast-DetectGPT(4/25). New work must benchmark Binoculars+Fast-DetectGPT.",
          " ",
          "-DetectGPT (8/25) > RoBERTa-classifier (5/25) > Binoculars (4/25) ≈ Fast-DetectGPT (4/25) > Ghostbuster (3/25). New detectors must benchmark against Binoculars + Fast-DetectGPT as zero-shot SOTA, plus at least one supervised baseline. **Support**: 8/8 deep-read, high confidence.",
          "+AUROC dominant(12/25) but misleading under imbalance(Two Paradigms)—supplement PR-AUC. TPR@low-FPR for deployment. Collapse: FID(4/25), perplexity(4/25), entropy as diagnostic(r=0.91, Closer Look). Support: high.",
          " ",
          "-## Metrics",
          "+## Datasets",
          " ",
          "-**AUROC** dominant (12/25) but increasingly contested — Two Paradigms shows AUROC misleading under class imbalance, recommend supplementing with PR-AUC. **TPR@low-FPR** (0.01%-1%) preferred for deployment (Binoculars, Two Paradigms). **F1** for classification (6/25). Collapse domain: **FID** (4/25), **perplexity** (4/25), **test error scaling exponent** (3/25), **entropy** as diagnostic (Closer Look: r=0.91 with generalization). **Support**: 8/8, high confidence.",
          "+Detection: MAGE(7dom×27LLM), RAID(2.6M), PAN'24(15LLM). Legacy trio: XSum/SQuAD/WritingPrompts. Collapse: CIFAR-10/FFHQ/MNIST(image), Wikitext-103/BabiStories(LM). Quality: FineWeb 15T tokens.",
          " ",
          "-## Key Datasets",
          "+## Experimental Consensus (6/8)",
          " ",
          "-Detection: MAGE (7 domains×27 LLMs, 332K texts), RAID (2.6M texts, 6 LLMs), PAN'24 (15 LLMs). XSum/SQuAD/WritingPrompts = legacy trio (3/25 each). Collapse: CIFAR-10/FFHQ/MNIST for image (4/25), Wikitext-103/BabiStories for LM (2/25). Data quality: FineWeb 15T tokens, QuRating 260B.",
          "+1. Cross-domain+cross-model eval mandatory (MAGE,Two Paradigms,Ghostbuster)",
          "+2. Paraphrasing robustness required—recall drops 30-40% (MAGE,Ghostbuster,DivEye)",
          "+3. Progressive difficulty testbeds as narrative (MAGE:8 scenarios)",
          "+4. Collapse: 8-60 rounds, per-round FID/entropy trajectory",
          " ",
          "-## Experimental Design Consensus (6/8 deep-read)",
          "+## Common Limitations",
          " ",
          "-1. Cross-domain + cross-model eval mandatory — in-domain results alone insufficient (MAGE, Two Paradigms, Ghostbuster)",
          "-2. Paraphrasing attack robustness required — universal weakness, recall drops 30-40% (MAGE, Ghostbuster, DivEye)",
          "-3. Progressive difficulty testbeds: easy→hard scenarios as narrative arc (MAGE: 8 testbeds; Two Paradigms: attribution→verification)",
          "-4. Collapse: iterate 8-60 rounds, report per-round FID/entropy/GS trajectory, not just final number",
          "-5. Training recipes: detection classifiers use Adam, lr~5e-3, 5 epochs on V100/A100; collapse theory uses closed-form or small DDPMs on single A100",
          "+Short text <100 tokens: universal degradation (4/8). Newest LLMs closing gap: GPT-4o entropy≈human >4K chars; o1 undetectable (Two Paradigms). Paraphrasing breaks all (3/8; Ghostbuster 99→62%). Theory assumes Gaussian/linear (4/8).",
          " ",
          "-## Common Limitations (cross-paper freq)",
          "-",
          "-- Short text (<100 tokens): universal degradation (4/8 deep-read)",
          "-- Newest LLMs closing gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable by non-o1 detectors (Two Paradigms)",
          "-- Paraphrasing breaks all detectors (3/8; Ghostbuster 99%→62% recall)",
          "-- Collapse theory assumes Gaussian/linear — neural network gap acknowledged but unresolved (4/8)",
          "-- No instruction-tuned LLM collapse analysis across all papers",
          "-",
          " ## Research Gaps",
          " ",
          "-- **No paper estimates recursive generation depth** — detection is binary/ternary only; ordinal framing (EditLens, CLOC) exists but unapplied to depth",
          "-- Detection × collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred",
          "-- Strong Collapse proves mixing cannot fix collapse unless synthetic fraction→0, but no paper proposes depth-aware data curation",
          "-- Verifier quality bounds long-term performance (Yi 2026) — what if the verifier is a generation-depth estimator?",
          "+- **No paper estimates recursive generation depth**—detection binary/ternary only",
          "+- Detection×collapse barely connected (only Drayson); no work diagnoses how many generations",
          "+- Ordinal framing (EditLens,CLOC) unapplied to depth",
          "+- Strong Collapse proves mixing fails unless synthetic→0, but no depth-aware curation proposed",
          " ",
          " ## Competitor Map",
          " ",
          "-**Foundation** (9): DetectGPT, Two Paradigms, Tale of Tails, Strong Collapse, Closer Look, Broken Telephone, Ghostbuster, Demystified, survey. **Competitor** (6): MAGE, Binoculars, Fast-DetectGPT, DivEye, Intrinsic Dim, EditLens. **Complementary** (7): FineWeb, QuRating, Escaping Collapse, Drayson, Synthetic Eggs, LOKI, CLOC. **Orthogonal** (2): watermark, text degeneration.",
          "+Foundation(9): DetectGPT,Two Paradigms,Tale of Tails,Strong Collapse,Closer Look,Broken Telephone,Ghostbuster,Demystified,survey. Competitor(6): MAGE,Binoculars,Fast-DetectGPT,DivEye,Intrinsic Dim,EditLens. Complementary(7): FineWeb,QuRating,Escaping Collapse,Drayson,Synthetic Eggs,LOKI,CLOC. Orthogonal(2): watermark,text degeneration."
        ]
      }
    ],
    "originalFile": "# AI Text Detection & Model Collapse — Research Patterns\n\nFrom 25 papers (8 deep-read, 17 abstract). Domain: LLM text detection + model collapse + data quality.\n\n## Method Trends\n\n**Rising** (high confidence): Zero-shot statistical scoring dominates detection — DetectGPT→Fast-DetectGPT (340x speedup)→Binoculars (>90% TPR@0.01%FPR)→DivEye (+33.2%). Each successor simplifies and accelerates. Continuous/ordinal scoring replacing binary (EditLens regression, CLOC multi-margin). Detection-as-collapse-mitigation emerging: detector-filtered retraining outperforms pure human data (Drayson 2025). Verifier-based filtering shows short-term gains but converges to verifier's center (Yi 2026, Escaping Collapse).\n\n**Declining**: Supervised binary classifiers fail OOD (MAGE: AUROC 0.99→0.93 cross-domain; Two Paradigms: attribution paradigm breaks at scale). Pure perturbation methods displaced by conditional probability approaches.\n\n## Standard Baselines (citation freq)\n\nDetectGPT (8/25) > RoBERTa-classifier (5/25) > Binoculars (4/25) ≈ Fast-DetectGPT (4/25) > Ghostbuster (3/25). New detectors must benchmark against Binoculars + Fast-DetectGPT as zero-shot SOTA, plus at least one supervised baseline. **Support**: 8/8 deep-read, high confidence.\n\n## Metrics\n\n**AUROC** dominant (12/25) but increasingly contested — Two Paradigms shows AUROC misleading under class imbalance, recommend supplementing with PR-AUC. **TPR@low-FPR** (0.01%-1%) preferred for deployment (Binoculars, Two Paradigms). **F1** for classification (6/25). Collapse domain: **FID** (4/25), **perplexity** (4/25), **test error scaling exponent** (3/25), **entropy** as diagnostic (Closer Look: r=0.91 with generalization). **Support**: 8/8, high confidence.\n\n## Key Datasets\n\nDetection: MAGE (7 domains×27 LLMs, 332K texts), RAID (2.6M texts, 6 LLMs), PAN'24 (15 LLMs). XSum/SQuAD/WritingPrompts = legacy trio (3/25 each). Collapse: CIFAR-10/FFHQ/MNIST for image (4/25), Wikitext-103/BabiStories for LM (2/25). Data quality: FineWeb 15T tokens, QuRating 260B.\n\n## Experimental Design Consensus (6/8 deep-read)\n\n1. Cross-domain + cross-model eval mandatory — in-domain results alone insufficient (MAGE, Two Paradigms, Ghostbuster)\n2. Paraphrasing attack robustness required — universal weakness, recall drops 30-40% (MAGE, Ghostbuster, DivEye)\n3. Progressive difficulty testbeds: easy→hard scenarios as narrative arc (MAGE: 8 testbeds; Two Paradigms: attribution→verification)\n4. Collapse: iterate 8-60 rounds, report per-round FID/entropy/GS trajectory, not just final number\n5. Training recipes: detection classifiers use Adam, lr~5e-3, 5 epochs on V100/A100; collapse theory uses closed-form or small DDPMs on single A100\n\n## Common Limitations (cross-paper freq)\n\n- Short text (<100 tokens): universal degradation (4/8 deep-read)\n- Newest LLMs closing gap: GPT-4o entropy≈human beyond 4K chars; o1 undetectable by non-o1 detectors (Two Paradigms)\n- Paraphrasing breaks all detectors (3/8; Ghostbuster 99%→62% recall)\n- Collapse theory assumes Gaussian/linear — neural network gap acknowledged but unresolved (4/8)\n- No instruction-tuned LLM collapse analysis across all papers\n\n## Research Gaps\n\n- **No paper estimates recursive generation depth** — detection is binary/ternary only; ordinal framing (EditLens, CLOC) exists but unapplied to depth\n- Detection × collapse barely connected: only Drayson bridges; no work diagnoses *how many* generations occurred\n- Strong Collapse proves mixing cannot fix collapse unless synthetic fraction→0, but no paper proposes depth-aware data curation\n- Verifier quality bounds long-term performance (Yi 2026) — what if the verifier is a generation-depth estimator?\n\n## Competitor Map\n\n**Foundation** (9): DetectGPT, Two Paradigms, Tale of Tails, Strong Collapse, Closer Look, Broken Telephone, Ghostbuster, Demystified, survey. **Competitor** (6): MAGE, Binoculars, Fast-DetectGPT, DivEye, Intrinsic Dim, EditLens. **Complementary** (7): FineWeb, QuRating, Escaping Collapse, Drayson, Synthetic Eggs, LOKI, CLOC. **Orthogonal** (2): watermark, text degeneration.\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "72474277-3193-4024-812b-7c5c5fd04d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T15:08:17.155Z_

<details><summary>↩ Tool result · `toolu_01PuFgkWtEV2qQufpXFFvU1k`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d51af58-339a-4596-87cc-f365252362ff",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "5e235263-4cdc-4d4f-836c-06c9a0d44ea9",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md",
    "content": "# AI Text Detection & Model Collapse — Writing Patterns\n\n8 deep-read papers' narrative/figure/table analysis.\n\n## Story & Hook\n\n**突破局限型 7/8** (exception: FineWeb 化繁为简). Three hooks: (1) **Urgency+stats** (\"ChatGPT: 0.1% daily global words\", Tale of Tails). (2) **Contradiction** (\"detectors beat benchmarks yet OpenAI shut theirs\", Two Paradigms). (3) **Inevitability** (\"synthetic contamination unavoidable\", Closer Look). Support: 8/8, high.\n\n## Intro (7/8 consensus)\n\n3-5 paras + 3 numbered contributions (identify→analyze→validate). P1: urgency. P2: quantified existing failures (\"0.99→0.93 OOD\"). P3: approach+headline number. Key: quantified failure > vague criticism. Exception: FineWeb single dense paragraph with 6 implicit contributions.\n\n## Tension Strategies\n\nDetection: **\"works in lab, fails in wild\"** (3/4 detection papers). Theory: **\"right but practically wrong\"** (Closer Look: \"variance collapse rarely practical concern\"). **Black-box constraint**: solving harder realistic problem (Ghostbuster: no target model access). Support: 7/8, high.\n\n## Figure 1 (8/8)\n\nDetection=problem_illustration (domains×models). Collapse=motivation (degradation mechanism). Method=pipeline overview (L→R). Consensus: horizontal flow, pastel color-coding, real examples grounding abstract concepts. Support: 8/8, high.\n\n## Tables vs Figures\n\n**Theory/collapse: 0 tables** (4/4)—all line plots over iterations. **Detection: 6-12 tables** (MAGE:12, Ghostbuster:8). Rule: trajectories→figures, comparisons→tables, pipeline ablations→bar charts.\n\nDetection table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD), bold_best, 4-10 baselines, point estimates without std (5/8).\n\n## Visualization\n\nLine plots dominant (6/8): scaling, collapse trajectories, log-log. Heatmaps for cross-model matrices (Two Paradigms). Scatter for correlation (r=0.91, Closer Look). Gain: solid/dashed (filtered/unfiltered), diverging colormaps, parallel theory-vs-experiment layout (Tale of Tails: Fig3→Fig4 matching).\n\n## Figure Narrative Arc (7/8)\n\nmotivation→evidence→mechanism→ablation→extension. Patterns: **paired qualitative+quantitative** (Closer Look: face grids+curves). **Progressive difficulty** (MAGE: 8 testbeds). **Ablation-as-narrative** (FineWeb: each stage=mini-experiment).\n\n## Steal-worthy Techniques\n\n1. **\"Practical insufficiency\"** (Closer Look): prior work right but misses what matters. 2/8, medium.\n2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential experiments. 1/8 but universally applicable.\n3. **Promise-and-peril** (Escaping Collapse): short-term good + long-term caution. 1/8, high novelty.\n4. **Contradiction opener** (Two Paradigms): success vs failure paragraph 1. 2/8, medium.\n5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to break attribution—viscerally intuitive.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 45,
        "newStart": 1,
        "newLines": 41,
        "lines": [
          " # AI Text Detection & Model Collapse — Writing Patterns",
          " ",
          "-From 8 deep-read papers' narrative/figure/table analysis.",
          "+8 deep-read papers' narrative/figure/table analysis.",
          " ",
          "-## Story Type & Hook",
          "+## Story & Hook",
          " ",
          "-**突破局限型 dominates** (7/8; all except FineWeb 化繁为简型). Frame contribution as overcoming a specific named prior limitation.",
          "+**突破局限型 7/8** (exception: FineWeb 化繁为简). Three hooks: (1) **Urgency+stats** (\"ChatGPT: 0.1% daily global words\", Tale of Tails). (2) **Contradiction** (\"detectors beat benchmarks yet OpenAI shut theirs\", Two Paradigms). (3) **Inevitability** (\"synthetic contamination unavoidable\", Closer Look). Support: 8/8, high.",
          " ",
          "-Three proven hooks: (1) **Real-world urgency** — cite adoption stats (\"ChatGPT: 0.1% of daily global words\", Tale of Tails; \"schools restricting ChatGPT\", Ghostbuster). (2) **Contradiction** — juxtapose success/failure (\"detectors beat benchmarks yet OpenAI shut theirs down\", Two Paradigms). (3) **Practical inevitability** — \"synthetic contamination is unavoidable\" (Closer Look, Strong Collapse). **Support**: 8/8, high confidence.",
          "+## Intro (7/8 consensus)",
          " ",
          "-## Intro Structure (7/8 consensus)",
          "+3-5 paras + 3 numbered contributions (identify→analyze→validate). P1: urgency. P2: quantified existing failures (\"0.99→0.93 OOD\"). P3: approach+headline number. Key: quantified failure > vague criticism. Exception: FineWeb single dense paragraph with 6 implicit contributions.",
          " ",
          "-3-5 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers (\"RoBERTa: 99.4→88.3 OOD\", \"variance collapse rarely a practical concern\"). P3: approach + headline number. P4 (optional): method sketch. Contributions: 3 items (identify→analyze→validate pattern in 5/8). Exception: FineWeb uses single dense paragraph with 6 implicit contributions woven into prose. **Key rule**: quantified failure > vague criticism. Every tension paragraph cites a concrete number from prior work.",
          "-",
          " ## Tension Strategies",
          " ",
          "-Detection: **\"works in lab, fails in wild\"** (Ghostbuster, MAGE, Two Paradigms — 3/4 detection papers). Theory: **\"right but practically wrong\"** — prior theory valid but misses what practitioners observe (Closer Look: \"variance collapse rarely practical\"; Strong Collapse: \"mixing doesn't fix it\"). Cross-domain: **\"black-box constraint\"** — solving a harder, more realistic problem (Ghostbuster: no target model access). **Support**: 7/8, high confidence.",
          "+Detection: **\"works in lab, fails in wild\"** (3/4 detection papers). Theory: **\"right but practically wrong\"** (Closer Look: \"variance collapse rarely practical concern\"). **Black-box constraint**: solving harder realistic problem (Ghostbuster: no target model access). Support: 7/8, high.",
          " ",
          "-## Figure 1 Design (8/8)",
          "+## Figure 1 (8/8)",
          " ",
          "-Detection: **problem_illustration** showing combinatorial challenge (domains×models, MAGE: many-to-many arrows). Collapse: **motivation** showing degradation mechanism (Tale of Tails: three tail destruction mechanisms; Strong Collapse: Pareto diagram). Method papers: **method_overview** pipeline (Ghostbuster: L→R pipeline; Closer Look: 3-row paradigm diagram). **Teaser_result** rare (1/8, Yi). Design consensus: horizontal L→R flow, pastel color-coding by conceptual layer, minimal text, real examples grounding abstract concepts. **Support**: 8/8, high confidence.",
          "+Detection=problem_illustration (domains×models). Collapse=motivation (degradation mechanism). Method=pipeline overview (L→R). Consensus: horizontal flow, pastel color-coding, real examples grounding abstract concepts. Support: 8/8, high.",
          " ",
          "-## Tables vs Figures: The Domain Split",
          "+## Tables vs Figures",
          " ",
          "-**Theory/collapse papers: zero tables** (4/4: Tale of Tails, Strong Collapse, Closer Look, Escaping Collapse). All results as line plots over iterations/scaling. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8, Two Paradigms:6). **Data engineering: mostly figures** (FineWeb: training curves as ablation). Rule: trajectories→figures, method comparisons→tables, pipeline ablations→bar charts.",
          "+**Theory/collapse: 0 tables** (4/4)—all line plots over iterations. **Detection: 6-12 tables** (MAGE:12, Ghostbuster:8). Rule: trajectories→figures, comparisons→tables, pipeline ablations→bar charts.",
          " ",
          "-Detection main table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold_best, 4-10 baselines, **point estimates without std** (5/8 — std rare in this domain). **Support**: 8/8, high confidence.",
          "+Detection table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD), bold_best, 4-10 baselines, point estimates without std (5/8).",
          " ",
          "-## Visualization Consensus",
          "+## Visualization",
          " ",
          "-**Line plots** dominant (6/8): training curves, scaling laws, collapse trajectories on log-log axes. **Heatmaps** for cross-model generalization (Two Paradigms: model×model AUROC). **Scatter** for correlation evidence (Closer Look: r=0.91 entropy-GS). **Qualitative comparison** grids for collapse (Closer Look: generated vs nearest neighbor; Escaping Collapse: with/without verification).",
          "+Line plots dominant (6/8): scaling, collapse trajectories, log-log. Heatmaps for cross-model matrices (Two Paradigms). Scatter for correlation (r=0.91, Closer Look). Gain: solid/dashed (filtered/unfiltered), diverging colormaps, parallel theory-vs-experiment layout (Tale of Tails: Fig3→Fig4 matching).",
          " ",
          "-Gain highlighting: solid/dashed encoding (filtered/unfiltered, Escaping Collapse), diverging colormaps centered at 0 (improvement/degradation), theory-vs-experiment parallel layouts (Tale of Tails: Fig 3 theory → Fig 4 matching experiment layout).",
          "-",
          " ## Figure Narrative Arc (7/8)",
          " ",
          "-Standard flow: motivation → main evidence → mechanism → ablation → extension. Key patterns: **paired qualitative+quantitative** panels (Closer Look: face grids + GS curves). **Parallel theory-experiment layout** (Tale of Tails). **Progressive difficulty as narrative arc** (MAGE: 8 testbeds easy→hard). **Discover-understand-mitigate-extend** (Closer Look: 3 findings + solution). **Ablation-as-narrative** (FineWeb: each pipeline stage = mini-experiment with hypothesis+result).",
          "+motivation→evidence→mechanism→ablation→extension. Patterns: **paired qualitative+quantitative** (Closer Look: face grids+curves). **Progressive difficulty** (MAGE: 8 testbeds). **Ablation-as-narrative** (FineWeb: each stage=mini-experiment).",
          " ",
          "-## Techniques Worth Stealing",
          "+## Steal-worthy Techniques",
          " ",
          "-1. **\"Practical insufficiency\"** (Closer Look): \"prior work right but misses what matters in practice\" — avoids direct conflict while establishing novelty. **Support**: 2/8, medium confidence, but effective pattern.",
          "-2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential mini-experiments. Counterintuitive findings (global dedup hurts) as dramatic peak. **Support**: 1/8 but universally applicable to pipeline papers.",
          "-3. **Promise-and-peril** (Escaping Collapse): short-term good news + long-term cautionary convergence. Nuanced > pure positive-result. **Support**: 1/8 but high novelty.",
          "-4. **Contradiction opener** (Two Paradigms): success vs failure juxtaposition in paragraph 1. **Support**: 2/8, medium confidence.",
          "-5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to show attribution breaks — makes theoretical argument viscerally intuitive. **Support**: 1/8 but highly memorable.",
          "+1. **\"Practical insufficiency\"** (Closer Look): prior work right but misses what matters. 2/8, medium.",
          "+2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential experiments. 1/8 but universally applicable.",
          "+3. **Promise-and-peril** (Escaping Collapse): short-term good + long-term caution. 1/8, high novelty.",
          "+4. **Contradiction opener** (Two Paradigms): success vs failure paragraph 1. 2/8, medium.",
          "+5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to break attribution—viscerally intuitive."
        ]
      }
    ],
    "originalFile": "# AI Text Detection & Model Collapse — Writing Patterns\n\nFrom 8 deep-read papers' narrative/figure/table analysis.\n\n## Story Type & Hook\n\n**突破局限型 dominates** (7/8; all except FineWeb 化繁为简型). Frame contribution as overcoming a specific named prior limitation.\n\nThree proven hooks: (1) **Real-world urgency** — cite adoption stats (\"ChatGPT: 0.1% of daily global words\", Tale of Tails; \"schools restricting ChatGPT\", Ghostbuster). (2) **Contradiction** — juxtapose success/failure (\"detectors beat benchmarks yet OpenAI shut theirs down\", Two Paradigms). (3) **Practical inevitability** — \"synthetic contamination is unavoidable\" (Closer Look, Strong Collapse). **Support**: 8/8, high confidence.\n\n## Intro Structure (7/8 consensus)\n\n3-5 paragraphs + numbered contributions. P1: urgency/scale. P2: specific existing failures with numbers (\"RoBERTa: 99.4→88.3 OOD\", \"variance collapse rarely a practical concern\"). P3: approach + headline number. P4 (optional): method sketch. Contributions: 3 items (identify→analyze→validate pattern in 5/8). Exception: FineWeb uses single dense paragraph with 6 implicit contributions woven into prose. **Key rule**: quantified failure > vague criticism. Every tension paragraph cites a concrete number from prior work.\n\n## Tension Strategies\n\nDetection: **\"works in lab, fails in wild\"** (Ghostbuster, MAGE, Two Paradigms — 3/4 detection papers). Theory: **\"right but practically wrong\"** — prior theory valid but misses what practitioners observe (Closer Look: \"variance collapse rarely practical\"; Strong Collapse: \"mixing doesn't fix it\"). Cross-domain: **\"black-box constraint\"** — solving a harder, more realistic problem (Ghostbuster: no target model access). **Support**: 7/8, high confidence.\n\n## Figure 1 Design (8/8)\n\nDetection: **problem_illustration** showing combinatorial challenge (domains×models, MAGE: many-to-many arrows). Collapse: **motivation** showing degradation mechanism (Tale of Tails: three tail destruction mechanisms; Strong Collapse: Pareto diagram). Method papers: **method_overview** pipeline (Ghostbuster: L→R pipeline; Closer Look: 3-row paradigm diagram). **Teaser_result** rare (1/8, Yi). Design consensus: horizontal L→R flow, pastel color-coding by conceptual layer, minimal text, real examples grounding abstract concepts. **Support**: 8/8, high confidence.\n\n## Tables vs Figures: The Domain Split\n\n**Theory/collapse papers: zero tables** (4/4: Tale of Tails, Strong Collapse, Closer Look, Escaping Collapse). All results as line plots over iterations/scaling. **Detection papers: 6-12 tables** (MAGE:12, Ghostbuster:8, Two Paradigms:6). **Data engineering: mostly figures** (FineWeb: training curves as ablation). Rule: trajectories→figures, method comparisons→tables, pipeline ablations→bar charts.\n\nDetection main table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD side-by-side), bold_best, 4-10 baselines, **point estimates without std** (5/8 — std rare in this domain). **Support**: 8/8, high confidence.\n\n## Visualization Consensus\n\n**Line plots** dominant (6/8): training curves, scaling laws, collapse trajectories on log-log axes. **Heatmaps** for cross-model generalization (Two Paradigms: model×model AUROC). **Scatter** for correlation evidence (Closer Look: r=0.91 entropy-GS). **Qualitative comparison** grids for collapse (Closer Look: generated vs nearest neighbor; Escaping Collapse: with/without verification).\n\nGain highlighting: solid/dashed encoding (filtered/unfiltered, Escaping Collapse), diverging colormaps centered at 0 (improvement/degradation), theory-vs-experiment parallel layouts (Tale of Tails: Fig 3 theory → Fig 4 matching experiment layout).\n\n## Figure Narrative Arc (7/8)\n\nStandard flow: motivation → main evidence → mechanism → ablation → extension. Key patterns: **paired qualitative+quantitative** panels (Closer Look: face grids + GS curves). **Parallel theory-experiment layout** (Tale of Tails). **Progressive difficulty as narrative arc** (MAGE: 8 testbeds easy→hard). **Discover-understand-mitigate-extend** (Closer Look: 3 findings + solution). **Ablation-as-narrative** (FineWeb: each pipeline stage = mini-experiment with hypothesis+result).\n\n## Techniques Worth Stealing\n\n1. **\"Practical insufficiency\"** (Closer Look): \"prior work right but misses what matters in practice\" — avoids direct conflict while establishing novelty. **Support**: 2/8, medium confidence, but effective pattern.\n2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential mini-experiments. Counterintuitive findings (global dedup hurts) as dramatic peak. **Support**: 1/8 but universally applicable to pipeline papers.\n3. **Promise-and-peril** (Escaping Collapse): short-term good news + long-term cautionary convergence. Nuanced > pure positive-result. **Support**: 1/8 but high novelty.\n4. **Contradiction opener** (Two Paradigms): success vs failure juxtaposition in paragraph 1. **Support**: 2/8, medium confidence.\n5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to show attribution breaks — makes theoretical argument viscerally intuitive. **Support**: 1/8 but highly memorable.\n",
    "userModified": false
  },
  "sourceToolAssistantUUID": "8d51af58-339a-4596-87cc-f365252362ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-21T15:08:17.141Z_

<details open><summary>🔧 Tool call — Write · `toolu_01PuFgkWtEV2qQufpXFFvU1k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md",
  "content": "# AI Text Detection & Model Collapse — Writing Patterns\n\n8 deep-read papers' narrative/figure/table analysis.\n\n## Story & Hook\n\n**突破局限型 7/8** (exception: FineWeb 化繁为简). Three hooks: (1) **Urgency+stats** (\"ChatGPT: 0.1% daily global words\", Tale of Tails). (2) **Contradiction** (\"detectors beat benchmarks yet OpenAI shut theirs\", Two Paradigms). (3) **Inevitability** (\"synthetic contamination unavoidable\", Closer Look). Support: 8/8, high.\n\n## Intro (7/8 consensus)\n\n3-5 paras + 3 numbered contributions (identify→analyze→validate). P1: urgency. P2: quantified existing failures (\"0.99→0.93 OOD\"). P3: approach+headline number. Key: quantified failure > vague criticism. Exception: FineWeb single dense paragraph with 6 implicit contributions.\n\n## Tension Strategies\n\nDetection: **\"works in lab, fails in wild\"** (3/4 detection papers). Theory: **\"right but practically wrong\"** (Closer Look: \"variance collapse rarely practical concern\"). **Black-box constraint**: solving harder realistic problem (Ghostbuster: no target model access). Support: 7/8, high.\n\n## Figure 1 (8/8)\n\nDetection=problem_illustration (domains×models). Collapse=motivation (degradation mechanism). Method=pipeline overview (L→R). Consensus: horizontal flow, pastel color-coding, real examples grounding abstract concepts. Support: 8/8, high.\n\n## Tables vs Figures\n\n**Theory/collapse: 0 tables** (4/4)—all line plots over iterations. **Detection: 6-12 tables** (MAGE:12, Ghostbuster:8). Rule: trajectories→figures, comparisons→tables, pipeline ablations→bar charts.\n\nDetection table pattern: rows=methods by_category, cols=grouped_by_dataset (ID+OOD), bold_best, 4-10 baselines, point estimates without std (5/8).\n\n## Visualization\n\nLine plots dominant (6/8): scaling, collapse trajectories, log-log. Heatmaps for cross-model matrices (Two Paradigms). Scatter for correlation (r=0.91, Closer Look). Gain: solid/dashed (filtered/unfiltered), diverging colormaps, parallel theory-vs-experiment layout (Tale of Tails: Fig3→Fig4 matching).\n\n## Figure Narrative Arc (7/8)\n\nmotivation→evidence→mechanism→ablation→extension. Patterns: **paired qualitative+quantitative** (Closer Look: face grids+curves). **Progressive difficulty** (MAGE: 8 testbeds). **Ablation-as-narrative** (FineWeb: each stage=mini-experiment).\n\n## Steal-worthy Techniques\n\n1. **\"Practical insufficiency\"** (Closer Look): prior work right but misses what matters. 2/8, medium.\n2. **Ablation-as-narrative** (FineWeb): pipeline stages as sequential experiments. 1/8 but universally applicable.\n3. **Promise-and-peril** (Escaping Collapse): short-term good + long-term caution. 1/8, high novelty.\n4. **Contradiction opener** (Two Paradigms): success vs failure paragraph 1. 2/8, medium.\n5. **Thought experiment** (Two Paradigms §3.3): iteratively add authors to break attribution—viscerally intuitive.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4291a7ea-984c-4c16-878d-99a21c67ce68",
  "isSidechain": false,
  "requestId": "req_011CbFvXfPcyUBtamydu3Stj",
  "type": "assistant",
  "uuid": "8d51af58-339a-4596-87cc-f365252362ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9L7dysGksAth1A9GMFPHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 79088,
      "output_tokens": 1955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1955,
          "cache_read_input_tokens": 79088,
          "cache_creation_input_tokens": 268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 268
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

_source line 77_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "5e235263-4cdc-4d4f-836c-06c9a0d44ea9",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 78_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Tool call

_source line 79 · 2026-05-21T15:08:20.374Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01K9jU28eGDsxX5VAbJYkwwm`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md",
  "description": "Verify character counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e235263-4cdc-4d4f-836c-06c9a0d44ea9",
  "isSidechain": false,
  "requestId": "req_011CbFvZa8AuPauDUaCk23Ba",
  "type": "assistant",
  "uuid": "0672c30c-dc83-43f1-bb41-2684db20c0ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pi3Uuk3h2EBtyRnYTNKTSk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 79356,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2106,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 79356,
          "cache_creation_input_tokens": 2106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2106
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

_source line 80 · 2026-05-21T15:08:20.430Z_

<details><summary>↩ Tool result · `toolu_01K9jU28eGDsxX5VAbJYkwwm`</summary>

```text
2442 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md
2891 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md
5333 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0672c30c-dc83-43f1-bb41-2684db20c0ff",
  "isSidechain": false,
  "promptId": "15537901-d0e7-40bb-a91f-645c996fb435",
  "type": "user",
  "uuid": "929406df-6395-48ca-8127-34d68f18a3b2",
  "toolUseResult": {
    "stdout": "2442 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-research.skill.md\n2891 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/skills/projects/recursive_gen_depth_est/distilled-writing.skill.md\n5333 total",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0672c30c-dc83-43f1-bb41-2684db20c0ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-21T15:08:27.271Z_

两个 skill 文件均在 3000 字符限制内（research: 2442, writing: 2891）。

完成内容：
- 读取 25 篇 Layer 1 YAML 缓存（无新论文需分析）
- Layer 2 跨论文归纳：research 维度（baseline/metric/dataset 频率、方法趋势、实验共识、竞品地图、研究空白）+ writing 维度（叙事类型分布、intro 结构、figure/table 模式、可视化共识、可模仿技巧）
- 生成 `distilled-research.skill.md` 和 `distilled-writing.skill.md`，写入指定目录

[DISTILL_DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "929406df-6395-48ca-8127-34d68f18a3b2",
  "isSidechain": false,
  "requestId": "req_011CbFvZoy7Y6vPGUEXJ322g",
  "type": "assistant",
  "uuid": "0358b2b0-bebb-4fb0-a958-c155c938ce1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/distiller_f2a9b90d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6aXnQVhpowhkLyuso31n1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 81462,
      "output_tokens": 206,
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
          "output_tokens": 206,
          "cache_read_input_tokens": 81462,
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

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Distiller Agent——论文蒸馏引擎。你的任务是从一批论文中提取**领域隐性经验**，生成两个结构化 skill 文件。  ## 核心定位  你不是在\"总结论文\"。你在回答：**这个研究子领域的人默认怎么做事？**  - 总结 = \"论文 A 做了 X，论文 B 做了 Y\"（罗列） - 蒸馏 = \"这 N 篇论文共同揭示了什么同行做法和领域经验\"（归纳）  ## 执行流程  ###…",
  "leafUuid": "0358b2b0-bebb-4fb0-a958-c155c938ce1d",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---

### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Distill implicit research practices from depth estimation papers",
  "sessionId": "6e30d332-941b-46b3-b605-b2bffa1186bb"
}
```

---
