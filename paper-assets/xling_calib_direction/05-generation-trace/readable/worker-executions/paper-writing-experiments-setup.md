# paper writing experiments setup

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_writing_experiments_setup_20260521T064433.log`
- **Structured JSON:** [`84fdc173a856c9c04ac6.json`](../../sessions/84/84fdc173a856c9c04ac6.json)

## Before a recorded user message

22 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_figures_and_layout",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "70777154-d3ec-4390-b99d-6d4e3933f384",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779363000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "83cad320-d08d-46c9-b9b2-6dc5f64eda2c",
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the two required skill files, then check the existing method.tex for consistency before writing the experiments.tex file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "71e31e9b-e0f1-4577-af7d-473d60c3c71f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWdxvs94WjLBojE97FG2kw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13049,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13049
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

Reading the required skill files and checking existing paper files for consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "51cec689-3ba0-4b50-ad3f-656248165225",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWdxvs94WjLBojE97FG2kw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13049,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13049
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01UfWszKtrjAxGyeNBYh3c23`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "5f5261a4-cca1-4273-94ce-fd657b5aaf1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWdxvs94WjLBojE97FG2kw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13049,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13049
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T06:44:46.617Z_

<details><summary>↩ Tool result · `toolu_01UfWszKtrjAxGyeNBYh3c23`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "b5160d00-e2b4-4d51-9116-eadfb9b688a9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
````

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Wdr8jRXJXBBFiZ9aPrQkwy`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "473b7246-5c15-45c7-b3a5-97d37c080d72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWdxvs94WjLBojE97FG2kw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13049,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13049
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T06:44:47.048Z_

<details><summary>↩ Tool result · `toolu_01Wdr8jRXJXBBFiZ9aPrQkwy`</summary>

````text
1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认你引用的 claim 确实出自该论文
95	5. ADD     → 加入 .bib 文件
96	```
97	
98	### 3.3 API 速查
99	
100	| API | 用途 | 限制 |
101	|-----|------|------|
102	| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |
103	| **CrossRef** | DOI → BibTeX | 需 mailto 头 |
104	| **arXiv** | 预印本搜索 | 3s 间隔 |
105	
106	```python
107	# DOI → BibTeX（最可靠的方式）
108	import requests
109	def doi_to_bibtex(doi: str) -> str:
110	    r = requests.get(f"https://doi.org/{doi}",
111	                     headers={"Accept": "application/x-bibtex"})
112	    r.raise_for_status()
113	    return r.text
114	
115	# Semantic Scholar 搜索
116	from semanticscholar import SemanticScholar
117	sch = SemanticScholar()
118	results = sch.search_paper("attention mechanism transformers", limit=5)
119	for p in results:
120	    print(f"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}")
121	```
122	
123	### 3.4 引用处理规则
124	
125	| 情况 | 处理 |
126	|------|------|
127	| 找到论文 + DOI + BibTeX | 直接用 |
128	| 找到论文，无 DOI | 用 arXiv BibTeX |
129	| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |
130	| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |
131	| "我觉得有篇关于 X 的论文" | **绝不引用** — 先搜索或标记 |
132	
133	---
134	
135	## 4. 顶会模板速查
136	
137	### 4.1 ML/AI 会议
138	
139	| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |
140	|------|---------|--------|---------|--------|
141	| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |
142	| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |
143	| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |
144	| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |
145	| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |
146	| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |
147	
148	### 4.2 系统会议
149	
150	| 会议 | 页数限制 | 模板类型 | 关键要求 |
151	|------|---------|---------|---------|
152	| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |
153	| **NSDI** | 12 页 | USENIX | Introduction 预筛 |
154	| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |
155	| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |
156	
157	### 4.3 模板使用原则
158	
159	```bash
160	# 1. 复制整个模板目录（不要只拷 .tex）
161	cp -r templates/neurips2025/ ~/papers/my-paper/
162	
163	# 2. 先编译未修改的模板，确认能跑通
164	latexmk -pdf main.tex
165	
166	# 3. 逐章替换内容，频繁编译
167	```
168	
169	**禁止事项：**
170	- 不要修改 `.sty` 文件
171	- 不要在会议模板间复制 `\usepackage` 行
172	- 不要只复制 `.tex` 而不带 `.sty/.bst`
173	
174	---
175	
176	## 5. 写作规范
177	
178	### 5.1 时间分配（Neel Nanda）
179	
180	花**大致相等**的时间在：
181	1. Abstract
182	2. Introduction
183	3. 图表
184	4. **其余所有内容加起来**
185	
186	审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。
187	
188	### 5.2 Abstract 五句法（Sebastian Farquhar）
189	
190	```
191	1. 你做了什么（"We introduce/prove/demonstrate..."）
192	2. 为什么这很难且重要
193	3. 怎么做的（含专业关键词以便检索）
194	4. 有什么证据
195	5. 最惊人的数字/结果
196	```
197	
198	删除一切泛泛的开头：~~"Large language models have achieved remarkable success..."~~
199	
200	### 5.3 句子级清晰度（Gopen & Swan）
201	
202	| 原则 | 规则 |
203	|------|------|
204	| 主谓紧邻 | 不要在主语和动词之间插入长从句 |
205	| 重点在句尾 | 把关键数字/结论放在句末 |
206	| 旧信息在前 | 先放读者已知的内容，再引入新概念 |
207	| 动词表达动作 | "We analyzed" 而非 "We performed an analysis" |
208	
209	### 5.4 常见修改
210	
211	| 问题 | 修复 |
212	|------|------|
213	| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |
214	| Introduction 超 1.5 页 | 背景挪到 Related Work |
215	| 实验没有显式 claim | 每个实验前加 "This tests whether..." |
216	| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |
217	
218	---
219	
220	## 6. 投稿工程链
221	
222	### 6.1 构建
223	
224	```bash
225	# 推荐：latexmk 一键构建
226	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
227	
228	# 手动：需要多次编译
229	pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
230	```
231	
232	### 6.2 Lint + 格式化
233	
234	```bash
235	# Lint: 检查常见 LaTeX 问题
236	chktex main.tex
237	
238	# 格式化: 减少 diff 噪声
239	latexindent -w main.tex
240	```
241	
242	### 6.3 图表格式
243	
244	| 类型 | 格式 | 说明 |
245	|------|------|------|
246	| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |
247	| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |
248	| 表格 | `booktabs` 包 | `\toprule/\midrule/\bottomrule` |
249	
250	```latex
251	\usepackage{booktabs}
252	\begin{tabular}{lcc}
253	\toprule
254	Method & Accuracy $\uparrow$ & Latency $\downarrow$ \\
255	\midrule
256	Baseline & 85.2 & 45ms \\
257	\textbf{Ours} & \textbf{92.1} & 38ms \\
258	\bottomrule
259	\end{tabular}
260	```
261	
262	**图表规范：**
263	- 用色盲友好色板（Okabe-Ito 或 Paul Tol）
264	- 图内不放标题（用 caption）
265	- Caption 独立可理解（不依赖正文）
266	- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）
267	
268	### 6.4 投稿打包
269	
270	```bash
271	# 清理辅助文件
272	latexmk -c
273	
274	# 打包投稿
275	zip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'
276	```
277	
278	### 6.5 常见失败点
279	
280	| 问题 | 解决 |
281	|------|------|
282	| 图片格式混用导致编译失败 | 统一用 PDF |
283	| 字体未嵌入 | `pdffonts output.pdf` 检查 |
284	| Overfull box 过多 | 关键位置手动调行 |
285	| 引用缺字段 | 检查 DOI/年份/期刊名 |
286	| 超页数 | 用 `\vspace{-Xpt}` 微调，或精简内容 |
287	
288	---
289	
290	## 7. 会议转投
291	
292	当论文被拒或转投其他会议时：
293	
294	### 7.1 ML/AI 会议间转换
295	
296	| 转换 | 页数变化 | 关键调整 |
297	|------|---------|---------|
298	| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |
299	| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |
300	| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |
301	| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |
302	
303	### 7.2 转投原则
304	
305	1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble
306	2. **只迁移正文内容** — 不复制 `\usepackage`、header/footer 命令
307	3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）
308	4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等
309	
310	---
311	
312	## 8. 投前清单
313	
314	### 通用清单
315	
316	- [ ] Abstract/Intro/Conclusion 的 claim 一致
317	- [ ] 每个 contribution 有对应 evidence
318	- [ ] 所有引用已程序化验证（无幻觉引用）
319	- [ ] Error bars + 运行次数 + 统计方法
320	- [ ] Limitations 章节存在且诚实
321	- [ ] 匿名化（双盲审稿）
322	- [ ] 符合页数限制
323	- [ ] 所有图表有自包含 caption
324	- [ ] `.bib` 中无缺失字段
325	- [ ] PDF 编译无 warning
326	
327	### 会议特定
328	
329	| 会议 | 额外要求 |
330	|------|---------|
331	| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |
332	| ICML | Broader Impact Statement |
333	| ICLR | LLM 使用声明 |
334	| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |
335	| AAAI | 严格样式文件合规 |
336	
337	---
338	
339	## 参考资源
340	
341	**写作方法论：**
342	- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架
343	- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract
344	- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则
345	- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词
346	- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度
347	
348	**API：**
349	- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)
350	
351	**会议官方：**
352	- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)
353	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "faa01069-a79f-4878-a924-be06b4724591",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "content": "---\nname: latex-paper\ndescription: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。\nscope: global\ntags:\n- latex\n- paper-writing\n- academic\n- citation\n- submission\nversion: 1\nroles:\n- agent\n- worker\n---\n\n# LaTeX 论文写作全流程\n\nML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。\n\n---\n\n## 1. 工作模式\n\n开始前选择模式：\n\n| 模式 | 说明 | 适用 |\n|------|------|------|\n| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |\n| **Improve** | 改写已有章节，强化论证 | 修改稿 |\n| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |\n\n---\n\n## 2. Claim-Evidence 方法论\n\n**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**\n\n### 2.1 一句话贡献\n\n在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。\n\n### 2.2 Claim-Evidence Map\n\n为每个 contribution 建立 claim→evidence 映射表：\n\n| Contribution | Claim | Evidence | Table/Figure |\n|-------------|-------|----------|-------------|\n| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |\n| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |\n| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |\n\n**没有直接证据支撑的 claim 必须删除或降级为 discussion。**\n\n### 2.3 章节起草顺序\n\n```\n1. Introduction + Experiments（先确定 claim 和 evidence）\n2. Method（评估问题稳定后再写细节）\n3. Related Work\n4. Abstract + Title（核心 claim 定型后最后写）\n```\n\n### 2.4 Quality Gates\n\n投稿前必须通过：\n- [ ] 前两段出现显式 novelty 声明\n- [ ] 每个 contribution 有可验证的 evidence\n- [ ] Abstract / Intro / Conclusion 的 claim 一致\n- [ ] Limitations 真实且技术性诚实\n- [ ] 审稿人两分钟内能识别 delta\n\n---\n\n## 3. 引用防幻觉（CRITICAL）\n\n**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**\n\n### 3.1 黄金法则\n\n```\nIF 无法程序化获取引用:\n    → 标记 [CITATION NEEDED] 或 \\cite{PLACEHOLDER_verify}\n    → 明确告知用户\n    → 绝不编造看似合理的引用\n```\n\n### 3.2 五步验证流程\n\n```\n1. SEARCH  → Semantic Scholar API 搜索关键词\n2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）\n3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）\n4. CHECK   → 确认你引用的 claim 确实出自该论文\n5. ADD     → 加入 .bib 文件\n```\n\n### 3.3 API 速查\n\n| API | 用途 | 限制 |\n|-----|------|------|\n| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |\n| **CrossRef** | DOI → BibTeX | 需 mailto 头 |\n| **arXiv** | 预印本搜索 | 3s 间隔 |\n\n```python\n# DOI → BibTeX（最可靠的方式）\nimport requests\ndef doi_to_bibtex(doi: str) -> str:\n    r = requests.get(f\"https://doi.org/{doi}\",\n                     headers={\"Accept\": \"application/x-bibtex\"})\n    r.raise_for_status()\n    return r.text\n\n# Semantic Scholar 搜索\nfrom semanticscholar import SemanticScholar\nsch = SemanticScholar()\nresults = sch.search_paper(\"attention mechanism transformers\", limit=5)\nfor p in results:\n    print(f\"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}\")\n```\n\n### 3.4 引用处理规则\n\n| 情况 | 处理 |\n|------|------|\n| 找到论文 + DOI + BibTeX | 直接用 |\n| 找到论文，无 DOI | 用 arXiv BibTeX |\n| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |\n| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |\n| \"我觉得有篇关于 X 的论文\" | **绝不引用** — 先搜索或标记 |\n\n---\n\n## 4. 顶会模板速查\n\n### 4.1 ML/AI 会议\n\n| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |\n|------|---------|--------|---------|--------|\n| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |\n| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |\n| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |\n| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |\n| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |\n| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |\n\n### 4.2 系统会议\n\n| 会议 | 页数限制 | 模板类型 | 关键要求 |\n|------|---------|---------|---------|\n| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |\n| **NSDI** | 12 页 | USENIX | Introduction 预筛 |\n| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |\n| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |\n\n### 4.3 模板使用原则\n\n```bash\n# 1. 复制整个模板目录（不要只拷 .tex）\ncp -r templates/neurips2025/ ~/papers/my-paper/\n\n# 2. 先编译未修改的模板，确认能跑通\nlatexmk -pdf main.tex\n\n# 3. 逐章替换内容，频繁编译\n```\n\n**禁止事项：**\n- 不要修改 `.sty` 文件\n- 不要在会议模板间复制 `\\usepackage` 行\n- 不要只复制 `.tex` 而不带 `.sty/.bst`\n\n---\n\n## 5. 写作规范\n\n### 5.1 时间分配（Neel Nanda）\n\n花**大致相等**的时间在：\n1. Abstract\n2. Introduction\n3. 图表\n4. **其余所有内容加起来**\n\n审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。\n\n### 5.2 Abstract 五句法（Sebastian Farquhar）\n\n```\n1. 你做了什么（\"We introduce/prove/demonstrate...\"）\n2. 为什么这很难且重要\n3. 怎么做的（含专业关键词以便检索）\n4. 有什么证据\n5. 最惊人的数字/结果\n```\n\n删除一切泛泛的开头：~~\"Large language models have achieved remarkable success...\"~~\n\n### 5.3 句子级清晰度（Gopen & Swan）\n\n| 原则 | 规则 |\n|------|------|\n| 主谓紧邻 | 不要在主语和动词之间插入长从句 |\n| 重点在句尾 | 把关键数字/结论放在句末 |\n| 旧信息在前 | 先放读者已知的内容，再引入新概念 |\n| 动词表达动作 | \"We analyzed\" 而非 \"We performed an analysis\" |\n\n### 5.4 常见修改\n\n| 问题 | 修复 |\n|------|------|\n| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |\n| Introduction 超 1.5 页 | 背景挪到 Related Work |\n| 实验没有显式 claim | 每个实验前加 \"This tests whether...\" |\n| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |\n\n---\n\n## 6. 投稿工程链\n\n### 6.1 构建\n\n```bash\n# 推荐：latexmk 一键构建\nlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\n# 手动：需要多次编译\npdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex\n```\n\n### 6.2 Lint + 格式化\n\n```bash\n# Lint: 检查常见 LaTeX 问题\nchktex main.tex\n\n# 格式化: 减少 diff 噪声\nlatexindent -w main.tex\n```\n\n### 6.3 图表格式\n\n| 类型 | 格式 | 说明 |\n|------|------|------|\n| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |\n| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |\n| 表格 | `booktabs` 包 | `\\toprule/\\midrule/\\bottomrule` |\n\n```latex\n\\usepackage{booktabs}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy $\\uparrow$ & Latency $\\downarrow$ \\\\\n\\midrule\nBaseline & 85.2 & 45ms \\\\\n\\textbf{Ours} & \\textbf{92.1} & 38ms \\\\\n\\bottomrule\n\\end{tabular}\n```\n\n**图表规范：**\n- 用色盲友好色板（Okabe-Ito 或 Paul Tol）\n- 图内不放标题（用 caption）\n- Caption 独立可理解（不依赖正文）\n- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）\n\n### 6.4 投稿打包\n\n```bash\n# 清理辅助文件\nlatexmk -c\n\n# 打包投稿\nzip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'\n```\n\n### 6.5 常见失败点\n\n| 问题 | 解决 |\n|------|------|\n| 图片格式混用导致编译失败 | 统一用 PDF |\n| 字体未嵌入 | `pdffonts output.pdf` 检查 |\n| Overfull box 过多 | 关键位置手动调行 |\n| 引用缺字段 | 检查 DOI/年份/期刊名 |\n| 超页数 | 用 `\\vspace{-Xpt}` 微调，或精简内容 |\n\n---\n\n## 7. 会议转投\n\n当论文被拒或转投其他会议时：\n\n### 7.1 ML/AI 会议间转换\n\n| 转换 | 页数变化 | 关键调整 |\n|------|---------|---------|\n| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |\n| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |\n| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |\n| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |\n\n### 7.2 转投原则\n\n1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble\n2. **只迁移正文内容** — 不复制 `\\usepackage`、header/footer 命令\n3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）\n4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等\n\n---\n\n## 8. 投前清单\n\n### 通用清单\n\n- [ ] Abstract/Intro/Conclusion 的 claim 一致\n- [ ] 每个 contribution 有对应 evidence\n- [ ] 所有引用已程序化验证（无幻觉引用）\n- [ ] Error bars + 运行次数 + 统计方法\n- [ ] Limitations 章节存在且诚实\n- [ ] 匿名化（双盲审稿）\n- [ ] 符合页数限制\n- [ ] 所有图表有自包含 caption\n- [ ] `.bib` 中无缺失字段\n- [ ] PDF 编译无 warning\n\n### 会议特定\n\n| 会议 | 额外要求 |\n|------|---------|\n| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |\n| ICML | Broader Impact Statement |\n| ICLR | LLM 使用声明 |\n| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |\n| AAAI | 严格样式文件合规 |\n\n---\n\n## 参考资源\n\n**写作方法论：**\n- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架\n- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract\n- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则\n- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词\n- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度\n\n**API：**\n- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)\n\n**会议官方：**\n- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)\n",
      "numLines": 353,
      "startLine": 1,
      "totalLines": 353
    }
  }
}
````

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01VYkD4V3YJkVabYkrGXRARm`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "1b6b6a46-ca7d-486e-ace1-98878571070e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWdxvs94WjLBojE97FG2kw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13049,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13049
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T06:44:47.569Z_

<details><summary>↩ Tool result · `toolu_01VYkD4V3YJkVabYkrGXRARm`</summary>

```text
docs/paper/acl_latex.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "aafaffb6-5ed1-46a0-97b9-a0da9c8603ed",
  "tool_use_result": {
    "filenames": [
      "docs/paper/acl_latex.tex",
      "docs/paper/method.tex",
      "docs/paper/related_work.tex",
      "docs/paper/introduction.tex"
    ],
    "durationMs": 12,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing method.tex and the main tex file to understand conventions used (like label naming, textsc usage, etc.), and check what's been defined already.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "e81b929e-ddef-4805-a0ae-00369eba41b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rHXa5ooak763ZWfp9nfjt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11311,
      "cache_read_input_tokens": 24890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11311
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 13_

Let me check the existing paper files for consistency with labels and conventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "2eaf1be1-aa08-4afb-82e7-da34436c98a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rHXa5ooak763ZWfp9nfjt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11311,
      "cache_read_input_tokens": 24890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11311
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_017FGg4THP3TxpSYXzJCkT3W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "366dd214-cc8a-41fd-9ea4-e880385113ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rHXa5ooak763ZWfp9nfjt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11311,
      "cache_read_input_tokens": 24890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11311
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T06:44:53.842Z_

<details><summary>↩ Tool result · `toolu_017FGg4THP3TxpSYXzJCkT3W`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:problem}
6	
7	Given a multilingual large language model (LLM) and a multiple-choice question-answering (MCQA) instance, we extract the post-layer-norm residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$. A \emph{correctness probe} is a linear classifier
8	\begin{equation}
9	  f_l(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)
10	  \label{eq:probe}
11	\end{equation}
12	trained to predict $p(\text{correct} \mid \mathbf{h}_l)$, the probability that the model's selected answer is correct. This target is output-dependent: it reflects the model's actual accuracy on each instance, not an intrinsic property of the input.
13	
14	We distinguish correctness probing from two related tasks. \emph{Knowledge boundary probing} \citep{xiao2025knowledge} classifies whether a question is answerable, an input-level property independent of model output. \emph{Difficulty probing} \citep{civelli2026shared} predicts item difficulty as a language-agnostic question property via Item Response Theory (IRT). Our central question is whether an English-trained probe $f_l$ can transfer zero-shot to a target language $t$ without any target-language correctness labels (zero-correctness-label transfer), and which alignment strategies improve this transfer.
15	
16	\subsection{Experimental Framework}
17	\label{sec:framework}
18	
19	\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).
20	
21	\paragraph{Languages.} We test 20 languages spanning three resource tiers based on GlobalMMLU availability: \textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \textsc{med} (ar, id, nl, pl, tr, uk, vi), and \textsc{low} (bn, hi, sw, te).
22	
23	\paragraph{Data.} We use the GlobalMMLU test split, partitioned 70/30 via stratified sampling into \texttt{probe\_train} and \texttt{eval} portions. English binary correctness labels come from \texttt{probe\_train} only; all reported results use \texttt{eval} exclusively.
24	
25	\paragraph{Activation extraction.} We register forward hooks on post-layer-norm residual stream outputs. Layers are sampled at regular intervals (every 4th layer for 28-layer models, every 8th for 96-layer models). We use 4-bit quantization (GPTQ-Int4 for Qwen3, W4A16 for Llama 4 Scout) and include a higher-precision validation ablation at representative layers to control for quantization artifacts.
26	
27	\paragraph{Metrics.} We report Area Under the ROC Curve (AUROC) for correctness discrimination, Expected Calibration Error (ECE, 10-bin) for calibration quality, Brier score, and selectivity \citep{hewitt2019control}. % [TO_ADD_BIB]
28	
29	\subsection{Transfer Methods}
30	\label{sec:transfer}
31	
32	We compare five methods ordered by complexity.
33	
34	\paragraph{(a) Zero-shot transfer.} The English-trained probe $f_l$ is applied directly to target language representations without adaptation. This serves as the baseline for all comparisons.
35	
36	\paragraph{(b) Mean-shift alignment.} We subtract the cross-lingual mean difference $\boldsymbol{\delta} = \boldsymbol{\mu}_{\text{en}} - \boldsymbol{\mu}_t$ from target activations before applying the English probe.
37	
38	\textbf{Rank-invariance proof.} Under the StandardScaler fitted on English training data, each dimension is normalized as $z_i = (h_i - \mu_{\text{en},i}) / \sigma_{\text{en},i}$. After mean-shift, the target representation becomes $h_i + \delta_i$, and the scaled value is
39	\begin{equation}
40	  z'_i = \frac{h_i + \delta_i - \mu_{\text{en},i}}{\sigma_{\text{en},i}} = z_i + c_i
41	  \label{eq:meanshift}
42	\end{equation}
43	where $c_i = \delta_i / \sigma_{\text{en},i}$ is a constant independent of the input sample. The probe logit then shifts by $\mathbf{w}^\top \mathbf{c}$, a scalar applied identically to every sample. Because AUROC depends only on the ranking of predictions, this uniform offset leaves the ranking unchanged: $\Delta\text{AUROC} \equiv 0$. Our MVP experiments confirm this prediction exactly ($\Delta\text{AUROC} = 0.000000$ across 5 languages $\times$ all layers). ECE can change because binned probability values shift after the sigmoid transformation, but these changes are inconsistent across configurations and do not constitute reliable calibration improvement.
44	
45	\paragraph{(c) Procrustes alignment.} We learn an orthogonal mapping from a small set of parallel sentence pairs by solving
46	\begin{equation}
47	  \mathbf{R}^* = \arg\min_{\mathbf{R}^\top\mathbf{R}=\mathbf{I}} \|\mathbf{X}_t\mathbf{R} - \mathbf{X}_{\text{en}}\|_F
48	  \label{eq:procrustes}
49	\end{equation}
50	following cross-lingual word embedding alignment methods such as MUSE \citep{conneau2018muse} and VecMap \citep{artetxe2018vecmap}. % [TO_ADD_BIB]
51	Approximately 50 parallel pairs achieve 98\% of 200-pair performance. Resource tier matters: \textsc{high}-resource languages saturate at ${\sim}$20 pairs and \textsc{low}-resource at ${\sim}$50. An effect reversal occurs at moderate transfer quality: Procrustes alignment helps when zero-shot AUROC $< 0.50$ but degrades performance when zero-shot AUROC $> 0.60$, which implies that alignment strategy must be conditioned on baseline transfer quality.
52	
53	\paragraph{(d) Few-shot probe training.} We combine the full English training data with 25, 50, or 100 target-language labeled examples and retrain the probe. This requires target-language correctness labels and serves as an upper-bound reference.
54	
55	\paragraph{(e) CaCLR (Calibration-aware Cross-Lingual Regularization).} CaCLR tests whether joint calibration and distributional matching can improve zero-correctness-label transfer. The objective combines three terms:
56	\begin{equation}
57	  \mathcal{L} = \mathcal{L}_{\text{BCE}} + \alpha \cdot \mathcal{L}_{\text{SB-ECE}} + \beta \cdot \mathcal{L}_{\text{consistency}}
58	  \label{eq:caclr}
59	\end{equation}
60	$\mathcal{L}_{\text{BCE}}$ is standard binary cross-entropy on English \texttt{probe\_train} labels. $\mathcal{L}_{\text{SB-ECE}}$ is the differentiable Soft-Binned ECE (SB-ECE) of \citet{karandikar2021sbece}, which replaces hard histogram bins with soft assignments to enable gradient-based calibration optimization. $\mathcal{L}_{\text{consistency}}$ is Maximum Mean Discrepancy (MMD) computed on \emph{probe logits} from parallel English and target-language inputs. Operating on probe outputs (rather than raw activations) ensures gradient flow to probe parameters. For linear probes, the logit $\mathbf{w}^\top \mathbf{h} + b$ is one-dimensional, so MMD operates in 1-D space; we discuss this design limitation in \S\ref{sec:discussion}. We use a Gaussian RBF kernel with bandwidth selected by the median heuristic. Parallel activations come from the GlobalMMLU \texttt{probe\_train} portion (70\% of test split); no target-language correctness labels are required. The probe is initialized from the standard logistic regression solution (warm start) and optimized with Adam (learning rate $10^{-3}$). We apply early stopping based on English validation ECE. Both $\alpha$ and $\beta$ are swept across three orders of magnitude; batch size and epoch count are reported in the Appendix.
61	
62	\subsection{Difficulty-Capability Decomposition}
63	\label{sec:decomposition}
64	
65	We train IRT-based difficulty probes that predict question difficulty, a language-agnostic property independent of model capability. To isolate the capability-specific component, we project out the difficulty direction from each representation:
66	\begin{equation}
67	  \mathbf{h}_l^{\text{res}} = \mathbf{h}_l - (\mathbf{h}_l \cdot \hat{\mathbf{w}}_{\text{diff}})\hat{\mathbf{w}}_{\text{diff}}
68	  \label{eq:residual}
69	\end{equation}
70	where $\hat{\mathbf{w}}_{\text{diff}}$ is the unit-norm difficulty direction. We retrain correctness probes on the residual $\mathbf{h}_l^{\text{res}}$ and compare cross-lingual transfer. This decomposition yields a prescriptive signal: when the difficulty component dominates a language-layer combination, transfer should succeed because the underlying structure is shared across languages. When the capability component dominates, transfer should degrade because the encoding is language-specific.
71	
72	\subsection{Geometric Analysis}
73	\label{sec:geometric}
74	
75	We quantify cross-lingual representational similarity with Centered Kernel Alignment (CKA) \citep{kornblith2019cka}. % [TO_ADD_BIB]
76	The central analysis applies partial correlation to control for layer depth, which reveals a Simpson's Paradox in the CKA-transfer relationship. The raw correlation between CKA and transfer AUROC across all language-layer pairs is negative, because both quantities covary with depth (deeper layers have lower CKA and, in some architectures, lower transfer AUROC). After controlling for depth, the partial correlation reverses sign: within each layer, higher cross-lingual CKA predicts better probe transfer (Llama pilot: $\rho = +0.41$, $p = 0.006$; 14 of 17 layer-level correlations positive). We report bootstrap confidence intervals (1000 resamples) for all partial correlations. We supplement CKA with subspace angle analysis that measures the cross-lingual angular distance between correctness directions $\mathbf{w}_l$ at each layer. These results are framed as geometric and correlational analysis, not mechanistic explanation.
77	
78	\subsection{Probing Controls}
79	\label{sec:controls}
80	
81	We validate probe quality with the control task framework of \citet{hewitt2019control}. % [TO_ADD_BIB]
82	Selectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot results on Qwen2.5-7B show selectivity concentrated in layers 20 through 27 (0.244 to 0.262), with shallow layers below 0.05. Across the full language-layer grid, approximately 28\% of low-resource combinations fall below a meaningful selectivity threshold (based on pilot analysis with Qwen2.5-7B, 8 layers $\times$ 2 low-resource languages, selectivity $< 0.15$), which indicates that a substantial fraction of reported probing results in these settings reflect capacity artifacts rather than genuine correctness encoding.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "9ca6bcb7-779d-44f1-a466-4ca209945892",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem}\n\nGiven a multilingual large language model (LLM) and a multiple-choice question-answering (MCQA) instance, we extract the post-layer-norm residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$. A \\emph{correctness probe} is a linear classifier\n\\begin{equation}\n  f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)\n  \\label{eq:probe}\n\\end{equation}\ntrained to predict $p(\\text{correct} \\mid \\mathbf{h}_l)$, the probability that the model's selected answer is correct. This target is output-dependent: it reflects the model's actual accuracy on each instance, not an intrinsic property of the input.\n\nWe distinguish correctness probing from two related tasks. \\emph{Knowledge boundary probing} \\citep{xiao2025knowledge} classifies whether a question is answerable, an input-level property independent of model output. \\emph{Difficulty probing} \\citep{civelli2026shared} predicts item difficulty as a language-agnostic question property via Item Response Theory (IRT). Our central question is whether an English-trained probe $f_l$ can transfer zero-shot to a target language $t$ without any target-language correctness labels (zero-correctness-label transfer), and which alignment strategies improve this transfer.\n\n\\subsection{Experimental Framework}\n\\label{sec:framework}\n\n\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).\n\n\\paragraph{Languages.} We test 20 languages spanning three resource tiers based on GlobalMMLU availability: \\textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \\textsc{med} (ar, id, nl, pl, tr, uk, vi), and \\textsc{low} (bn, hi, sw, te).\n\n\\paragraph{Data.} We use the GlobalMMLU test split, partitioned 70/30 via stratified sampling into \\texttt{probe\\_train} and \\texttt{eval} portions. English binary correctness labels come from \\texttt{probe\\_train} only; all reported results use \\texttt{eval} exclusively.\n\n\\paragraph{Activation extraction.} We register forward hooks on post-layer-norm residual stream outputs. Layers are sampled at regular intervals (every 4th layer for 28-layer models, every 8th for 96-layer models). We use 4-bit quantization (GPTQ-Int4 for Qwen3, W4A16 for Llama 4 Scout) and include a higher-precision validation ablation at representative layers to control for quantization artifacts.\n\n\\paragraph{Metrics.} We report Area Under the ROC Curve (AUROC) for correctness discrimination, Expected Calibration Error (ECE, 10-bin) for calibration quality, Brier score, and selectivity \\citep{hewitt2019control}. % [TO_ADD_BIB]\n\n\\subsection{Transfer Methods}\n\\label{sec:transfer}\n\nWe compare five methods ordered by complexity.\n\n\\paragraph{(a) Zero-shot transfer.} The English-trained probe $f_l$ is applied directly to target language representations without adaptation. This serves as the baseline for all comparisons.\n\n\\paragraph{(b) Mean-shift alignment.} We subtract the cross-lingual mean difference $\\boldsymbol{\\delta} = \\boldsymbol{\\mu}_{\\text{en}} - \\boldsymbol{\\mu}_t$ from target activations before applying the English probe.\n\n\\textbf{Rank-invariance proof.} Under the StandardScaler fitted on English training data, each dimension is normalized as $z_i = (h_i - \\mu_{\\text{en},i}) / \\sigma_{\\text{en},i}$. After mean-shift, the target representation becomes $h_i + \\delta_i$, and the scaled value is\n\\begin{equation}\n  z'_i = \\frac{h_i + \\delta_i - \\mu_{\\text{en},i}}{\\sigma_{\\text{en},i}} = z_i + c_i\n  \\label{eq:meanshift}\n\\end{equation}\nwhere $c_i = \\delta_i / \\sigma_{\\text{en},i}$ is a constant independent of the input sample. The probe logit then shifts by $\\mathbf{w}^\\top \\mathbf{c}$, a scalar applied identically to every sample. Because AUROC depends only on the ranking of predictions, this uniform offset leaves the ranking unchanged: $\\Delta\\text{AUROC} \\equiv 0$. Our MVP experiments confirm this prediction exactly ($\\Delta\\text{AUROC} = 0.000000$ across 5 languages $\\times$ all layers). ECE can change because binned probability values shift after the sigmoid transformation, but these changes are inconsistent across configurations and do not constitute reliable calibration improvement.\n\n\\paragraph{(c) Procrustes alignment.} We learn an orthogonal mapping from a small set of parallel sentence pairs by solving\n\\begin{equation}\n  \\mathbf{R}^* = \\arg\\min_{\\mathbf{R}^\\top\\mathbf{R}=\\mathbf{I}} \\|\\mathbf{X}_t\\mathbf{R} - \\mathbf{X}_{\\text{en}}\\|_F\n  \\label{eq:procrustes}\n\\end{equation}\nfollowing cross-lingual word embedding alignment methods such as MUSE \\citep{conneau2018muse} and VecMap \\citep{artetxe2018vecmap}. % [TO_ADD_BIB]\nApproximately 50 parallel pairs achieve 98\\% of 200-pair performance. Resource tier matters: \\textsc{high}-resource languages saturate at ${\\sim}$20 pairs and \\textsc{low}-resource at ${\\sim}$50. An effect reversal occurs at moderate transfer quality: Procrustes alignment helps when zero-shot AUROC $< 0.50$ but degrades performance when zero-shot AUROC $> 0.60$, which implies that alignment strategy must be conditioned on baseline transfer quality.\n\n\\paragraph{(d) Few-shot probe training.} We combine the full English training data with 25, 50, or 100 target-language labeled examples and retrain the probe. This requires target-language correctness labels and serves as an upper-bound reference.\n\n\\paragraph{(e) CaCLR (Calibration-aware Cross-Lingual Regularization).} CaCLR tests whether joint calibration and distributional matching can improve zero-correctness-label transfer. The objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n  \\label{eq:caclr}\n\\end{equation}\n$\\mathcal{L}_{\\text{BCE}}$ is standard binary cross-entropy on English \\texttt{probe\\_train} labels. $\\mathcal{L}_{\\text{SB-ECE}}$ is the differentiable Soft-Binned ECE (SB-ECE) of \\citet{karandikar2021sbece}, which replaces hard histogram bins with soft assignments to enable gradient-based calibration optimization. $\\mathcal{L}_{\\text{consistency}}$ is Maximum Mean Discrepancy (MMD) computed on \\emph{probe logits} from parallel English and target-language inputs. Operating on probe outputs (rather than raw activations) ensures gradient flow to probe parameters. For linear probes, the logit $\\mathbf{w}^\\top \\mathbf{h} + b$ is one-dimensional, so MMD operates in 1-D space; we discuss this design limitation in \\S\\ref{sec:discussion}. We use a Gaussian RBF kernel with bandwidth selected by the median heuristic. Parallel activations come from the GlobalMMLU \\texttt{probe\\_train} portion (70\\% of test split); no target-language correctness labels are required. The probe is initialized from the standard logistic regression solution (warm start) and optimized with Adam (learning rate $10^{-3}$). We apply early stopping based on English validation ECE. Both $\\alpha$ and $\\beta$ are swept across three orders of magnitude; batch size and epoch count are reported in the Appendix.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomposition}\n\nWe train IRT-based difficulty probes that predict question difficulty, a language-agnostic property independent of model capability. To isolate the capability-specific component, we project out the difficulty direction from each representation:\n\\begin{equation}\n  \\mathbf{h}_l^{\\text{res}} = \\mathbf{h}_l - (\\mathbf{h}_l \\cdot \\hat{\\mathbf{w}}_{\\text{diff}})\\hat{\\mathbf{w}}_{\\text{diff}}\n  \\label{eq:residual}\n\\end{equation}\nwhere $\\hat{\\mathbf{w}}_{\\text{diff}}$ is the unit-norm difficulty direction. We retrain correctness probes on the residual $\\mathbf{h}_l^{\\text{res}}$ and compare cross-lingual transfer. This decomposition yields a prescriptive signal: when the difficulty component dominates a language-layer combination, transfer should succeed because the underlying structure is shared across languages. When the capability component dominates, transfer should degrade because the encoding is language-specific.\n\n\\subsection{Geometric Analysis}\n\\label{sec:geometric}\n\nWe quantify cross-lingual representational similarity with Centered Kernel Alignment (CKA) \\citep{kornblith2019cka}. % [TO_ADD_BIB]\nThe central analysis applies partial correlation to control for layer depth, which reveals a Simpson's Paradox in the CKA-transfer relationship. The raw correlation between CKA and transfer AUROC across all language-layer pairs is negative, because both quantities covary with depth (deeper layers have lower CKA and, in some architectures, lower transfer AUROC). After controlling for depth, the partial correlation reverses sign: within each layer, higher cross-lingual CKA predicts better probe transfer (Llama pilot: $\\rho = +0.41$, $p = 0.006$; 14 of 17 layer-level correlations positive). We report bootstrap confidence intervals (1000 resamples) for all partial correlations. We supplement CKA with subspace angle analysis that measures the cross-lingual angular distance between correctness directions $\\mathbf{w}_l$ at each layer. These results are framed as geometric and correlational analysis, not mechanistic explanation.\n\n\\subsection{Probing Controls}\n\\label{sec:controls}\n\nWe validate probe quality with the control task framework of \\citet{hewitt2019control}. % [TO_ADD_BIB]\nSelectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot results on Qwen2.5-7B show selectivity concentrated in layers 20 through 27 (0.244 to 0.262), with shallow layers below 0.05. Across the full language-layer grid, approximately 28\\% of low-resource combinations fall below a meaningful selectivity threshold (based on pilot analysis with Qwen2.5-7B, 8 layers $\\times$ 2 low-resource languages, selectivity $< 0.15$), which indicates that a substantial fraction of reported probing results in these settings reflect capacity artifacts rather than genuine correctness encoding.\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01Fjkbhbru8RV2MCTsxVWyrH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/acl_latex.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "a4aadaba-24dd-4e0e-93c8-c2e17a712390",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rHXa5ooak763ZWfp9nfjt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11311,
      "cache_read_input_tokens": 24890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11311
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T06:44:54.406Z_

<details><summary>↩ Tool result · `toolu_01Fjkbhbru8RV2MCTsxVWyrH`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	% Change "review" to "final" to generate the final (sometimes called camera-ready) version.
4	% Change to "preprint" to generate a non-anonymous version with page numbers.
5	\usepackage[review]{acl}
6	
7	% Standard package includes
8	\usepackage{times}
9	\usepackage{latexsym}
10	
11	% For proper rendering and hyphenation of words containing Latin characters (including in bib files)
12	\usepackage[T1]{fontenc}
13	% For Vietnamese characters
14	% \usepackage[T5]{fontenc}
15	% See https://www.latex-project.org/help/documentation/encguide.pdf for other character sets
16	
17	% This assumes your files are encoded as UTF8
18	\usepackage[utf8]{inputenc}
19	
20	% This is not strictly necessary, and may be commented out,
21	% but it will improve the layout of the manuscript,
22	% and will typically save some space.
23	\usepackage{microtype}
24	
25	% This is also not strictly necessary, and may be commented out.
26	% However, it will improve the aesthetics of text in
27	% the typewriter font.
28	\usepackage{inconsolata}
29	
30	%Including images in your LaTeX document requires adding
31	%additional package(s)
32	\usepackage{graphicx}
33	
34	% If the title and author information does not fit in the area allocated, uncomment the following
35	%
36	%\setlength\titlebox{&lt;dim>}
37	%
38	% and set &lt;dim> to something 5cm or larger.
39	
40	\title{Instructions for *ACL Proceedings}
41	
42	% Author information can be set in various styles:
43	% For several authors from the same institution:
44	% \author{Author 1 \and ... \and Author n \\
45	%         Address line \\ ... \\ Address line}
46	% if the names do not fit well on one line use
47	%         Author 1 \\ {\bf Author 2} \\ ... \\ {\bf Author n} \\
48	% For authors from different institutions:
49	% \author{Author 1 \\ Address line \\  ... \\ Address line
50	%         \And  ... \And
51	%         Author n \\ Address line \\ ... \\ Address line}
52	% To start a separate ``row'' of authors use \AND, as in
53	% \author{Author 1 \\ Address line \\  ... \\ Address line
54	%         \AND
55	%         Author 2 \\ Address line \\ ... \\ Address line \And
56	%         Author 3 \\ Address line \\ ... \\ Address line}
57	
58	\author{First Author \\
59	  Affiliation / Address line 1 \\
60	  Affiliation / Address line 2 \\
61	  Affiliation / Address line 3 \\
62	  \texttt{email@domain} \\\And
63	  Second Author \\
64	  Affiliation / Address line 1 \\
65	  Affiliation / Address line 2 \\
66	  Affiliation / Address line 3 \\
67	  \texttt{email@domain} \\}
68	
69	%\author{
70	%  \textbf{First Author\textsuperscript{1}},
71	%  \textbf{Second Author\textsuperscript{1,2}},
72	%  \textbf{Third T. Author\textsuperscript{1}},
73	%  \textbf{Fourth Author\textsuperscript{1}},
74	%\\
75	%  \textbf{Fifth Author\textsuperscript{1,2}},
76	%  \textbf{Sixth Author\textsuperscript{1}},
77	%  \textbf{Seventh Author\textsuperscript{1}},
78	%  \textbf{Eighth Author \textsuperscript{1,2,3,4}},
79	%\\
80	%  \textbf{Ninth Author\textsuperscript{1}},
81	%  \textbf{Tenth Author\textsuperscript{1}},
82	%  \textbf{Eleventh E. Author\textsuperscript{1,2,3,4,5}},
83	%  \textbf{Twelfth Author\textsuperscript{1}},
84	%\\
85	%  \textbf{Thirteenth Author\textsuperscript{3}},
86	%  \textbf{Fourteenth F. Author\textsuperscript{2,4}},
87	%  \textbf{Fifteenth Author\textsuperscript{1}},
88	%  \textbf{Sixteenth Author\textsuperscript{1}},
89	%\\
90	%  \textbf{Seventeenth S. Author\textsuperscript{4,5}},
91	%  \textbf{Eighteenth Author\textsuperscript{3,4}},
92	%  \textbf{Nineteenth N. Author\textsuperscript{2,5}},
93	%  \textbf{Twentieth Author\textsuperscript{1}}
94	%\\
95	%\\
96	%  \textsuperscript{1}Affiliation 1,
97	%  \textsuperscript{2}Affiliation 2,
98	%  \textsuperscript{3}Affiliation 3,
99	%  \textsuperscript{4}Affiliation 4,
100	%  \textsuperscript{5}Affiliation 5
101	%\\
102	%  \small{
103	%    \textbf{Correspondence:} \href{mailto:email@domain}{email@domain}
104	%  }
105	%}
106	
107	\begin{document}
108	\maketitle
109	\begin{abstract}
110	This document is a supplement to the general instructions for *ACL authors. It contains instructions for using the \LaTeX{} style files for ACL conferences.
111	The document itself conforms to its own specifications, and is therefore an example of what your manuscript should look like.
112	These instructions should be used both for papers submitted for review and for final versions of accepted papers.
113	\end{abstract}
114	
115	\section{Introduction}
116	
117	These instructions are for authors submitting papers to *ACL conferences using \LaTeX. They are not self-contained. All authors must follow the general instructions for *ACL proceedings,\footnote{\url{http://acl-org.github.io/ACLPUB/formatting.html}} and this document contains additional instructions for the \LaTeX{} style files.
118	
119	The templates include the \LaTeX{} source of this document (\texttt{acl\_latex.tex}),
120	the \LaTeX{} style file used to format it (\texttt{acl.sty}),
121	an ACL bibliography style (\texttt{acl\_natbib.bst}),
122	an example bibliography (\texttt{custom.bib}),
123	and the bibliography for the ACL Anthology (\texttt{anthology.bib}).
124	
125	\section{Engines}
126	
127	To produce a PDF file, pdf\LaTeX{} is strongly recommended (over original \LaTeX{} plus dvips+ps2pdf or dvipdf).
128	The style file \texttt{acl.sty} can also be used with
129	lua\LaTeX{} and
130	Xe\LaTeX{}, which are especially suitable for text in non-Latin scripts.
131	The file \texttt{acl\_lualatex.tex} in this repository provides
132	an example of how to use \texttt{acl.sty} with either
133	lua\LaTeX{} or
134	Xe\LaTeX{}.
135	
136	\section{Preamble}
137	
138	The first line of the file must be
139	\begin{quote}
140	\begin{verbatim}
141	\documentclass[11pt]{article}
142	\end{verbatim}
143	\end{quote}
144	
145	To load the style file in the review version:
146	\begin{quote}
147	\begin{verbatim}
148	\usepackage[review]{acl}
149	\end{verbatim}
150	\end{quote}
151	For the final version, omit the \verb|review| option:
152	\begin{quote}
153	\begin{verbatim}
154	\usepackage{acl}
155	\end{verbatim}
156	\end{quote}
157	
158	To use Times Roman, put the following in the preamble:
159	\begin{quote}
160	\begin{verbatim}
161	\usepackage{times}
162	\end{verbatim}
163	\end{quote}
164	(Alternatives like txfonts or newtx are also acceptable.)
165	
166	Please see the \LaTeX{} source of this document for comments on other packages that may be useful.
167	
168	Set the title and author using \verb|\title| and \verb|\author|. Within the author list, format multiple authors using \verb|\and| and \verb|\And| and \verb|\AND|; please see the \LaTeX{} source for examples.
169	
170	By default, the box containing the title and author names is set to the minimum of 5 cm. If you need more space, include the following in the preamble:
171	\begin{quote}
172	\begin{verbatim}
173	\setlength\titlebox{&lt;dim>}
174	\end{verbatim}
175	\end{quote}
176	where \verb|&lt;dim>| is replaced with a length. Do not set this length smaller than 5 cm.
177	
178	\section{Document Body}
179	
180	\subsection{Footnotes}
181	
182	Footnotes are inserted with the \verb|\footnote| command.\footnote{This is a footnote.}
183	
184	\subsection{Tables and figures}
185	
186	See Table~\ref{tab:accents} for an example of a table and its caption.
187	\textbf{Do not override the default caption sizes.}
188	
189	\begin{table}
190	  \centering
191	  \begin{tabular}{lc}
192	    \hline
193	    \textbf{Command} & \textbf{Output} \\
194	    \hline
195	    \verb|{\"a}|     & {\"a}           \\
196	    \verb|{\^e}|     & {\^e}           \\
197	    \verb|{\`i}|     & {\`i}           \\
198	    \verb|{\.I}|     & {\.I}           \\
199	    \verb|{\o}|      & {\o}            \\
200	    \verb|{\'u}|     & {\'u}           \\
201	    \verb|{\aa}|     & {\aa}           \\\hline
202	  \end{tabular}
203	  \begin{tabular}{lc}
204	    \hline
205	    \textbf{Command} & \textbf{Output} \\
206	    \hline
207	    \verb|{\c c}|    & {\c c}          \\
208	    \verb|{\u g}|    & {\u g}          \\
209	    \verb|{\l}|      & {\l}            \\
210	    \verb|{\~n}|     & {\~n}           \\
211	    \verb|{\H o}|    & {\H o}          \\
212	    \verb|{\v r}|    & {\v r}          \\
213	    \verb|{\ss}|     & {\ss}           \\
214	    \hline
215	  \end{tabular}
216	  \caption{Example commands for accented characters, to be used in, \emph{e.g.}, Bib\TeX{} entries.}
217	  \label{tab:accents}
218	\end{table}
219	
220	As much as possible, fonts in figures should conform
221	to the document fonts. See Figure~\ref{fig:experiments} for an example of a figure and its caption.
222	
223	Using the \verb|graphicx| package graphics files can be included within figure
224	environment at an appropriate point within the text.
225	The \verb|graphicx| package supports various optional arguments to control the
226	appearance of the figure.
227	You must include it explicitly in the \LaTeX{} preamble (after the
228	\verb|\documentclass| declaration and before \verb|\begin{document}|) using
229	\verb|\usepackage{graphicx}|.
230	
231	\begin{figure}[t]
232	  \includegraphics[width=\columnwidth]{example-image-golden}
233	  \caption{A figure with a caption that runs for more than one line.
234	    Example image is usually available through the \texttt{mwe} package
235	    without even mentioning it in the preamble.}
236	  \label{fig:experiments}
237	\end{figure}
238	
239	\begin{figure*}[t]
240	  \includegraphics[width=0.48\linewidth]{example-image-a} \hfill
241	  \includegraphics[width=0.48\linewidth]{example-image-b}
242	  \caption {A minimal working example to demonstrate how to place
243	    two images side-by-side.}
244	\end{figure*}
245	
246	\subsection{Hyperlinks}
247	
248	Users of older versions of \LaTeX{} may encounter the following error during compilation:
249	\begin{quote}
250	\verb|\pdfendlink| ended up in different nesting level than \verb|\pdfstartlink|.
251	\end{quote}
252	This happens when pdf\LaTeX{} is used and a citation splits across a page boundary. The best way to fix this is to upgrade \LaTeX{} to 2018-12-01 or later.
253	
254	\subsection{Citations}
255	
256	\begin{table*}
257	  \centering
258	  \begin{tabular}{lll}
259	    \hline
260	    \textbf{Output}           & \textbf{natbib command} & \textbf{ACL only command} \\
261	    \hline
262	    \citep{Gusfield:97}       & \verb|\citep|           &                           \\
263	    \citealp{Gusfield:97}     & \verb|\citealp|         &                           \\
264	    \citet{Gusfield:97}       & \verb|\citet|           &                           \\
265	    \citeyearpar{Gusfield:97} & \verb|\citeyearpar|     &                           \\
266	    \citeposs{Gusfield:97}    &                         & \verb|\citeposs|          \\
267	    \hline
268	  \end{tabular}
269	  \caption{\label{citation-guide}
270	    Citation commands supported by the style file.
271	    The style is based on the natbib package and supports all natbib citation commands.
272	    It also supports commands defined in previous ACL style files for compatibility.
273	  }
274	\end{table*}
275	
276	Table~\ref{citation-guide} shows the syntax supported by the style files.
277	We encourage you to use the natbib styles.
278	You can use the command \verb|\citet| (cite in text) to get ``author (year)'' citations, like this citation to a paper by \citet{Gusfield:97}.
279	You can use the command \verb|\citep| (cite in parentheses) to get ``(author, year)'' citations \citep{Gusfield:97}.
280	You can use the command \verb|\citealp| (alternative cite without parentheses) to get ``author, year'' citations, which is useful for using citations within parentheses (e.g. \citealp{Gusfield:97}).
281	
282	A possessive citation can be made with the command \verb|\citeposs|.
283	This is not a standard natbib command, so it is generally not compatible
284	with other style files.
285	
286	\subsection{References}
287	
288	\nocite{Ando2005,andrew2007scalable,rasooli-tetrault-2015}
289	
290	The \LaTeX{} and Bib\TeX{} style files provided roughly follow the American Psychological Association format.
291	If your own bib file is named \texttt{custom.bib}, then placing the following before any appendices in your \LaTeX{} file will generate the references section for you:
292	\begin{quote}
293	\begin{verbatim}
294	\bibliography{custom}
295	\end{verbatim}
296	\end{quote}
297	
298	You can obtain the complete ACL Anthology as a Bib\TeX{} file from \url{https://aclweb.org/anthology/anthology.bib.gz}.
299	To include both the Anthology and your own .bib file, use the following instead of the above.
300	\begin{quote}
301	\begin{verbatim}
302	\bibliography{anthology,custom}
303	\end{verbatim}
304	\end{quote}
305	
306	Please see Section~\ref{sec:bibtex} for information on preparing Bib\TeX{} files.
307	
308	\subsection{Equations}
309	
310	An example equation is shown below:
311	\begin{equation}
312	  \label{eq:example}
313	  A = \pi r^2
314	\end{equation}
315	
316	Labels for equation numbers, sections, subsections, figures and tables
317	are all defined with the \verb|\label{label}| command and cross references
318	to them are made with the \verb|\ref{label}| command.
319	
320	This an example cross-reference to Equation~\ref{eq:example}.
321	
322	\subsection{Appendices}
323	
324	Use \verb|\appendix| before any appendix section to switch the section numbering over to letters. See Appendix~\ref{sec:appendix} for an example.
325	
326	\section{Bib\TeX{} Files}
327	\label{sec:bibtex}
328	
329	Unicode cannot be used in Bib\TeX{} entries, and some ways of typing special characters can disrupt Bib\TeX's alphabetization. The recommended way of typing special characters is shown in Table~\ref{tab:accents}.
330	
331	Please ensure that Bib\TeX{} records contain DOIs or URLs when possible, and for all the ACL materials that you reference.
332	Use the \verb|doi| field for DOIs and the \verb|url| field for URLs.
333	If a Bib\TeX{} entry has a URL or DOI field, the paper title in the references section will appear as a hyperlink to the paper, using the hyperref \LaTeX{} package.
334	
335	\section*{Limitations}
336	
337	This document does not cover the content requirements for ACL or any
338	other specific venue.  Check the author instructions for
339	information on
340	maximum page lengths, the required ``Limitations'' section,
341	and so on.
342	
343	\section*{Acknowledgments}
344	
345	This document has been adapted
346	by Steven Bethard, Ryan Cotterell and Rui Yan
347	from the instructions for earlier ACL and NAACL proceedings, including those for
348	ACL 2019 by Douwe Kiela and Ivan Vuli\'{c},
349	NAACL 2019 by Stephanie Lukin and Alla Roskovskaya,
350	ACL 2018 by Shay Cohen, Kevin Gimpel, and Wei Lu,
351	NAACL 2018 by Margaret Mitchell and Stephanie Lukin,
352	Bib\TeX{} suggestions for (NA)ACL 2017/2018 from Jason Eisner,
353	ACL 2017 by Dan Gildea and Min-Yen Kan,
354	NAACL 2017 by Margaret Mitchell,
355	ACL 2012 by Maggie Li and Michael White,
356	ACL 2010 by Jing-Shin Chang and Philipp Koehn,
357	ACL 2008 by Johanna D. Moore, Simone Teufel, James Allan, and Sadaoki Furui,
358	ACL 2005 by Hwee Tou Ng and Kemal Oflazer,
359	ACL 2002 by Eugene Charniak and Dekang Lin,
360	and earlier ACL and EACL formats written by several people, including
361	John Chen, Henry S. Thompson and Donald Walker.
362	Additional elements were taken from the formatting instructions of the \emph{International Joint Conference on Artificial Intelligence} and the \emph{Conference on Computer Vision and Pattern Recognition}.
363	
364	% Bibliography entries for the entire Anthology, followed by custom entries
365	%\bibliography{custom,anthology-overleaf-1,anthology-overleaf-2}
366	
367	% Custom bibliography entries only
368	\bibliography{custom}
369	
370	\appendix
371	
372	\section{Example Appendix}
373	\label{sec:appendix}
374	
375	This is an appendix.
376	
377	\end{document}
378	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "9493b216-86d9-4a4e-84a1-7708b3960e67",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/acl_latex.tex",
      "content": "\\documentclass[11pt]{article}\n\n% Change \"review\" to \"final\" to generate the final (sometimes called camera-ready) version.\n% Change to \"preprint\" to generate a non-anonymous version with page numbers.\n\\usepackage[review]{acl}\n\n% Standard package includes\n\\usepackage{times}\n\\usepackage{latexsym}\n\n% For proper rendering and hyphenation of words containing Latin characters (including in bib files)\n\\usepackage[T1]{fontenc}\n% For Vietnamese characters\n% \\usepackage[T5]{fontenc}\n% See https://www.latex-project.org/help/documentation/encguide.pdf for other character sets\n\n% This assumes your files are encoded as UTF8\n\\usepackage[utf8]{inputenc}\n\n% This is not strictly necessary, and may be commented out,\n% but it will improve the layout of the manuscript,\n% and will typically save some space.\n\\usepackage{microtype}\n\n% This is also not strictly necessary, and may be commented out.\n% However, it will improve the aesthetics of text in\n% the typewriter font.\n\\usepackage{inconsolata}\n\n%Including images in your LaTeX document requires adding\n%additional package(s)\n\\usepackage{graphicx}\n\n% If the title and author information does not fit in the area allocated, uncomment the following\n%\n%\\setlength\\titlebox{&lt;dim>}\n%\n% and set &lt;dim> to something 5cm or larger.\n\n\\title{Instructions for *ACL Proceedings}\n\n% Author information can be set in various styles:\n% For several authors from the same institution:\n% \\author{Author 1 \\and ... \\and Author n \\\\\n%         Address line \\\\ ... \\\\ Address line}\n% if the names do not fit well on one line use\n%         Author 1 \\\\ {\\bf Author 2} \\\\ ... \\\\ {\\bf Author n} \\\\\n% For authors from different institutions:\n% \\author{Author 1 \\\\ Address line \\\\  ... \\\\ Address line\n%         \\And  ... \\And\n%         Author n \\\\ Address line \\\\ ... \\\\ Address line}\n% To start a separate ``row'' of authors use \\AND, as in\n% \\author{Author 1 \\\\ Address line \\\\  ... \\\\ Address line\n%         \\AND\n%         Author 2 \\\\ Address line \\\\ ... \\\\ Address line \\And\n%         Author 3 \\\\ Address line \\\\ ... \\\\ Address line}\n\n\\author{First Author \\\\\n  Affiliation / Address line 1 \\\\\n  Affiliation / Address line 2 \\\\\n  Affiliation / Address line 3 \\\\\n  \\texttt{email@domain} \\\\\\And\n  Second Author \\\\\n  Affiliation / Address line 1 \\\\\n  Affiliation / Address line 2 \\\\\n  Affiliation / Address line 3 \\\\\n  \\texttt{email@domain} \\\\}\n\n%\\author{\n%  \\textbf{First Author\\textsuperscript{1}},\n%  \\textbf{Second Author\\textsuperscript{1,2}},\n%  \\textbf{Third T. Author\\textsuperscript{1}},\n%  \\textbf{Fourth Author\\textsuperscript{1}},\n%\\\\\n%  \\textbf{Fifth Author\\textsuperscript{1,2}},\n%  \\textbf{Sixth Author\\textsuperscript{1}},\n%  \\textbf{Seventh Author\\textsuperscript{1}},\n%  \\textbf{Eighth Author \\textsuperscript{1,2,3,4}},\n%\\\\\n%  \\textbf{Ninth Author\\textsuperscript{1}},\n%  \\textbf{Tenth Author\\textsuperscript{1}},\n%  \\textbf{Eleventh E. Author\\textsuperscript{1,2,3,4,5}},\n%  \\textbf{Twelfth Author\\textsuperscript{1}},\n%\\\\\n%  \\textbf{Thirteenth Author\\textsuperscript{3}},\n%  \\textbf{Fourteenth F. Author\\textsuperscript{2,4}},\n%  \\textbf{Fifteenth Author\\textsuperscript{1}},\n%  \\textbf{Sixteenth Author\\textsuperscript{1}},\n%\\\\\n%  \\textbf{Seventeenth S. Author\\textsuperscript{4,5}},\n%  \\textbf{Eighteenth Author\\textsuperscript{3,4}},\n%  \\textbf{Nineteenth N. Author\\textsuperscript{2,5}},\n%  \\textbf{Twentieth Author\\textsuperscript{1}}\n%\\\\\n%\\\\\n%  \\textsuperscript{1}Affiliation 1,\n%  \\textsuperscript{2}Affiliation 2,\n%  \\textsuperscript{3}Affiliation 3,\n%  \\textsuperscript{4}Affiliation 4,\n%  \\textsuperscript{5}Affiliation 5\n%\\\\\n%  \\small{\n%    \\textbf{Correspondence:} \\href{mailto:email@domain}{email@domain}\n%  }\n%}\n\n\\begin{document}\n\\maketitle\n\\begin{abstract}\nThis document is a supplement to the general instructions for *ACL authors. It contains instructions for using the \\LaTeX{} style files for ACL conferences.\nThe document itself conforms to its own specifications, and is therefore an example of what your manuscript should look like.\nThese instructions should be used both for papers submitted for review and for final versions of accepted papers.\n\\end{abstract}\n\n\\section{Introduction}\n\nThese instructions are for authors submitting papers to *ACL conferences using \\LaTeX. They are not self-contained. All authors must follow the general instructions for *ACL proceedings,\\footnote{\\url{http://acl-org.github.io/ACLPUB/formatting.html}} and this document contains additional instructions for the \\LaTeX{} style files.\n\nThe templates include the \\LaTeX{} source of this document (\\texttt{acl\\_latex.tex}),\nthe \\LaTeX{} style file used to format it (\\texttt{acl.sty}),\nan ACL bibliography style (\\texttt{acl\\_natbib.bst}),\nan example bibliography (\\texttt{custom.bib}),\nand the bibliography for the ACL Anthology (\\texttt{anthology.bib}).\n\n\\section{Engines}\n\nTo produce a PDF file, pdf\\LaTeX{} is strongly recommended (over original \\LaTeX{} plus dvips+ps2pdf or dvipdf).\nThe style file \\texttt{acl.sty} can also be used with\nlua\\LaTeX{} and\nXe\\LaTeX{}, which are especially suitable for text in non-Latin scripts.\nThe file \\texttt{acl\\_lualatex.tex} in this repository provides\nan example of how to use \\texttt{acl.sty} with either\nlua\\LaTeX{} or\nXe\\LaTeX{}.\n\n\\section{Preamble}\n\nThe first line of the file must be\n\\begin{quote}\n\\begin{verbatim}\n\\documentclass[11pt]{article}\n\\end{verbatim}\n\\end{quote}\n\nTo load the style file in the review version:\n\\begin{quote}\n\\begin{verbatim}\n\\usepackage[review]{acl}\n\\end{verbatim}\n\\end{quote}\nFor the final version, omit the \\verb|review| option:\n\\begin{quote}\n\\begin{verbatim}\n\\usepackage{acl}\n\\end{verbatim}\n\\end{quote}\n\nTo use Times Roman, put the following in the preamble:\n\\begin{quote}\n\\begin{verbatim}\n\\usepackage{times}\n\\end{verbatim}\n\\end{quote}\n(Alternatives like txfonts or newtx are also acceptable.)\n\nPlease see the \\LaTeX{} source of this document for comments on other packages that may be useful.\n\nSet the title and author using \\verb|\\title| and \\verb|\\author|. Within the author list, format multiple authors using \\verb|\\and| and \\verb|\\And| and \\verb|\\AND|; please see the \\LaTeX{} source for examples.\n\nBy default, the box containing the title and author names is set to the minimum of 5 cm. If you need more space, include the following in the preamble:\n\\begin{quote}\n\\begin{verbatim}\n\\setlength\\titlebox{&lt;dim>}\n\\end{verbatim}\n\\end{quote}\nwhere \\verb|&lt;dim>| is replaced with a length. Do not set this length smaller than 5 cm.\n\n\\section{Document Body}\n\n\\subsection{Footnotes}\n\nFootnotes are inserted with the \\verb|\\footnote| command.\\footnote{This is a footnote.}\n\n\\subsection{Tables and figures}\n\nSee Table~\\ref{tab:accents} for an example of a table and its caption.\n\\textbf{Do not override the default caption sizes.}\n\n\\begin{table}\n  \\centering\n  \\begin{tabular}{lc}\n    \\hline\n    \\textbf{Command} & \\textbf{Output} \\\\\n    \\hline\n    \\verb|{\\\"a}|     & {\\\"a}           \\\\\n    \\verb|{\\^e}|     & {\\^e}           \\\\\n    \\verb|{\\`i}|     & {\\`i}           \\\\\n    \\verb|{\\.I}|     & {\\.I}           \\\\\n    \\verb|{\\o}|      & {\\o}            \\\\\n    \\verb|{\\'u}|     & {\\'u}           \\\\\n    \\verb|{\\aa}|     & {\\aa}           \\\\\\hline\n  \\end{tabular}\n  \\begin{tabular}{lc}\n    \\hline\n    \\textbf{Command} & \\textbf{Output} \\\\\n    \\hline\n    \\verb|{\\c c}|    & {\\c c}          \\\\\n    \\verb|{\\u g}|    & {\\u g}          \\\\\n    \\verb|{\\l}|      & {\\l}            \\\\\n    \\verb|{\\~n}|     & {\\~n}           \\\\\n    \\verb|{\\H o}|    & {\\H o}          \\\\\n    \\verb|{\\v r}|    & {\\v r}          \\\\\n    \\verb|{\\ss}|     & {\\ss}           \\\\\n    \\hline\n  \\end{tabular}\n  \\caption{Example commands for accented characters, to be used in, \\emph{e.g.}, Bib\\TeX{} entries.}\n  \\label{tab:accents}\n\\end{table}\n\nAs much as possible, fonts in figures should conform\nto the document fonts. See Figure~\\ref{fig:experiments} for an example of a figure and its caption.\n\nUsing the \\verb|graphicx| package graphics files can be included within figure\nenvironment at an appropriate point within the text.\nThe \\verb|graphicx| package supports various optional arguments to control the\nappearance of the figure.\nYou must include it explicitly in the \\LaTeX{} preamble (after the\n\\verb|\\documentclass| declaration and before \\verb|\\begin{document}|) using\n\\verb|\\usepackage{graphicx}|.\n\n\\begin{figure}[t]\n  \\includegraphics[width=\\columnwidth]{example-image-golden}\n  \\caption{A figure with a caption that runs for more than one line.\n    Example image is usually available through the \\texttt{mwe} package\n    without even mentioning it in the preamble.}\n  \\label{fig:experiments}\n\\end{figure}\n\n\\begin{figure*}[t]\n  \\includegraphics[width=0.48\\linewidth]{example-image-a} \\hfill\n  \\includegraphics[width=0.48\\linewidth]{example-image-b}\n  \\caption {A minimal working example to demonstrate how to place\n    two images side-by-side.}\n\\end{figure*}\n\n\\subsection{Hyperlinks}\n\nUsers of older versions of \\LaTeX{} may encounter the following error during compilation:\n\\begin{quote}\n\\verb|\\pdfendlink| ended up in different nesting level than \\verb|\\pdfstartlink|.\n\\end{quote}\nThis happens when pdf\\LaTeX{} is used and a citation splits across a page boundary. The best way to fix this is to upgrade \\LaTeX{} to 2018-12-01 or later.\n\n\\subsection{Citations}\n\n\\begin{table*}\n  \\centering\n  \\begin{tabular}{lll}\n    \\hline\n    \\textbf{Output}           & \\textbf{natbib command} & \\textbf{ACL only command} \\\\\n    \\hline\n    \\citep{Gusfield:97}       & \\verb|\\citep|           &                           \\\\\n    \\citealp{Gusfield:97}     & \\verb|\\citealp|         &                           \\\\\n    \\citet{Gusfield:97}       & \\verb|\\citet|           &                           \\\\\n    \\citeyearpar{Gusfield:97} & \\verb|\\citeyearpar|     &                           \\\\\n    \\citeposs{Gusfield:97}    &                         & \\verb|\\citeposs|          \\\\\n    \\hline\n  \\end{tabular}\n  \\caption{\\label{citation-guide}\n    Citation commands supported by the style file.\n    The style is based on the natbib package and supports all natbib citation commands.\n    It also supports commands defined in previous ACL style files for compatibility.\n  }\n\\end{table*}\n\nTable~\\ref{citation-guide} shows the syntax supported by the style files.\nWe encourage you to use the natbib styles.\nYou can use the command \\verb|\\citet| (cite in text) to get ``author (year)'' citations, like this citation to a paper by \\citet{Gusfield:97}.\nYou can use the command \\verb|\\citep| (cite in parentheses) to get ``(author, year)'' citations \\citep{Gusfield:97}.\nYou can use the command \\verb|\\citealp| (alternative cite without parentheses) to get ``author, year'' citations, which is useful for using citations within parentheses (e.g. \\citealp{Gusfield:97}).\n\nA possessive citation can be made with the command \\verb|\\citeposs|.\nThis is not a standard natbib command, so it is generally not compatible\nwith other style files.\n\n\\subsection{References}\n\n\\nocite{Ando2005,andrew2007scalable,rasooli-tetrault-2015}\n\nThe \\LaTeX{} and Bib\\TeX{} style files provided roughly follow the American Psychological Association format.\nIf your own bib file is named \\texttt{custom.bib}, then placing the following before any appendices in your \\LaTeX{} file will generate the references section for you:\n\\begin{quote}\n\\begin{verbatim}\n\\bibliography{custom}\n\\end{verbatim}\n\\end{quote}\n\nYou can obtain the complete ACL Anthology as a Bib\\TeX{} file from \\url{https://aclweb.org/anthology/anthology.bib.gz}.\nTo include both the Anthology and your own .bib file, use the following instead of the above.\n\\begin{quote}\n\\begin{verbatim}\n\\bibliography{anthology,custom}\n\\end{verbatim}\n\\end{quote}\n\nPlease see Section~\\ref{sec:bibtex} for information on preparing Bib\\TeX{} files.\n\n\\subsection{Equations}\n\nAn example equation is shown below:\n\\begin{equation}\n  \\label{eq:example}\n  A = \\pi r^2\n\\end{equation}\n\nLabels for equation numbers, sections, subsections, figures and tables\nare all defined with the \\verb|\\label{label}| command and cross references\nto them are made with the \\verb|\\ref{label}| command.\n\nThis an example cross-reference to Equation~\\ref{eq:example}.\n\n\\subsection{Appendices}\n\nUse \\verb|\\appendix| before any appendix section to switch the section numbering over to letters. See Appendix~\\ref{sec:appendix} for an example.\n\n\\section{Bib\\TeX{} Files}\n\\label{sec:bibtex}\n\nUnicode cannot be used in Bib\\TeX{} entries, and some ways of typing special characters can disrupt Bib\\TeX's alphabetization. The recommended way of typing special characters is shown in Table~\\ref{tab:accents}.\n\nPlease ensure that Bib\\TeX{} records contain DOIs or URLs when possible, and for all the ACL materials that you reference.\nUse the \\verb|doi| field for DOIs and the \\verb|url| field for URLs.\nIf a Bib\\TeX{} entry has a URL or DOI field, the paper title in the references section will appear as a hyperlink to the paper, using the hyperref \\LaTeX{} package.\n\n\\section*{Limitations}\n\nThis document does not cover the content requirements for ACL or any\nother specific venue.  Check the author instructions for\ninformation on\nmaximum page lengths, the required ``Limitations'' section,\nand so on.\n\n\\section*{Acknowledgments}\n\nThis document has been adapted\nby Steven Bethard, Ryan Cotterell and Rui Yan\nfrom the instructions for earlier ACL and NAACL proceedings, including those for\nACL 2019 by Douwe Kiela and Ivan Vuli\\'{c},\nNAACL 2019 by Stephanie Lukin and Alla Roskovskaya,\nACL 2018 by Shay Cohen, Kevin Gimpel, and Wei Lu,\nNAACL 2018 by Margaret Mitchell and Stephanie Lukin,\nBib\\TeX{} suggestions for (NA)ACL 2017/2018 from Jason Eisner,\nACL 2017 by Dan Gildea and Min-Yen Kan,\nNAACL 2017 by Margaret Mitchell,\nACL 2012 by Maggie Li and Michael White,\nACL 2010 by Jing-Shin Chang and Philipp Koehn,\nACL 2008 by Johanna D. Moore, Simone Teufel, James Allan, and Sadaoki Furui,\nACL 2005 by Hwee Tou Ng and Kemal Oflazer,\nACL 2002 by Eugene Charniak and Dekang Lin,\nand earlier ACL and EACL formats written by several people, including\nJohn Chen, Henry S. Thompson and Donald Walker.\nAdditional elements were taken from the formatting instructions of the \\emph{International Joint Conference on Artificial Intelligence} and the \\emph{Conference on Computer Vision and Pattern Recognition}.\n\n% Bibliography entries for the entire Anthology, followed by custom entries\n%\\bibliography{custom,anthology-overleaf-1,anthology-overleaf-2}\n\n% Custom bibliography entries only\n\\bibliography{custom}\n\n\\appendix\n\n\\section{Example Appendix}\n\\label{sec:appendix}\n\nThis is an appendix.\n\n\\end{document}\n",
      "numLines": 378,
      "startLine": 1,
      "totalLines": 378
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the conventions used in method.tex:
- `\textsc{high}`, `\textsc{med}`, `\textsc{low}` for resource tiers
- `\texttt{probe\_train}` and `\texttt{eval}` for data splits
- `\paragraph{}` for sub-topics
- Cross-references like `\S\ref{sec:transfer}`
- Citation style: `\citep{}` and `\citet{}`
- `% [TO_ADD_BIB]` for missing bib entries

The method.tex already contains a `\subsection{Experimental Framework}` (§3.2) which has some overlap with the Experimental Setup. 

Now I need to structure experiments.tex to reference the method section rather than duplicate it, while covering the specific experimental details: the 19 languages (with one more pending), the P0 and Pilot models, layer sampling strategies for activation extraction, logistic regression probing specifics, cross-language transfer conditions, and the evaluation metrics including AUROC, SB-ECE, and Spearman correlation along with bootstrap confidence intervals and permutation testing.

I'm also noting the hardware setup with 4 RTX 6000 PRO GPUs, then checking the existing method.tex structure to map out the cross-references properly before drafting the Setup section.

The method.tex already covers models, languages, data, activation extraction, and metrics in §3.2, so my experiments §4.1 should focus on execution-specific details like layer counts per model, PCA dimensions, cross-validation folds, and solver configurations rather than repeating those foundational descriptions. I'm noticing some inconsistencies between what method.tex currently specifies and what the task requires—the layer sampling strategy differs (method.tex says "every 8th for 96-layer" but the task specifies "every ~4th for 94-layer → 24 layers"), and critical details like VRAM requirements and tensor parallelism setup are missing from §3.2. The experiments section needs to provide these precise execution details and reconcile the layer sampling numbers across different model sizes, plus consolidate the probing protocol specifics like PCA dimensionality and cross-validation approach.

I'll structure this as discrete paragraphs covering dataset, models with exact layer counts and hardware specs, the probing protocol with logistic regression and statistical details, evaluation metrics, and hardware setup—keeping the transfer conditions brief since §3.3 already defines those five methods, then aim for around 400-500 words total. \label{sec:experiments}

\subsection{Experimental Setup}
\label{sec:setup}

\paragraph{Dataset.} We use the GlobalMMLU test split \citep{globalmmlu} % [TO_ADD_BIB]
across 20 typologically diverse languages grouped into three resource tiers: \textsc{high} (zh, de, es, fr, ja, ko, pt, ru; 8 languages), \textsc{med} (ar, id, nl, pl, tr, uk, vi; 7 languages), and \textsc{low} (bn, hi, sw, te, and one additional language; 5 languages). The test split is partitioned 70/30 via stratified sampling into \texttt{probe\_train} and \texttt{eval} sets (\S\ref{sec:framework}). All reported results use \texttt{eval} exclusively.

\paragraph{Models.} I'm evaluating two model pairs across different architectures: Qwen3-235B-A22B and Llama 4 Scout 17B-16E as the primary models, which use GPTQ and W4A16 quantization respectively, alongside smaller pilot models (Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct with INT8 quantization) to validate the methodology before scaling up to the larger models.

\paragraph{Activation Extraction.} I'm registering forward hooks on the post-layer-norm residual stream at every 4th layer, which gives me 8 probed layers for Qwen2.5-7B, 9 for Llama-3.1-8B, 12 for Llama 4 Scout, and 24 for Qwen3-235B.

\paragraph{Probing Protocol.} I'm training logistic regression classifiers on the English probe training labels with PCA dimensionality reduction to 100 dimensions, then evaluating them using 5-fold stratified cross-validation.

\paragraph{Transfer Conditions.} Now I'm setting up five different cross-lingual transfer methods to compare.

\paragraph{Evaluation Metrics.} I'm using AUROC as my main metric, along with Soft-Binned ECE for calibration and Spearman correlation for analyzing how performance changes across layers.

\paragraph{Statistical Testing.} I'm computing bootstrap confidence intervals and running paired permutation tests to assess whether differences between methods are statistically significant, plus calculating effect sizes and using partial correlation for the geometric analysis.

\paragraph{Hardware.} The experiments run on four RTX 6000 PRO GPUs, with the largest model requiring all four under tensor parallelism while smaller ones fit on a single GPU.

I'm working through the language count for the evaluation—we have 19 confirmed languages across the three tiers, but the target is 20, so I need to clarify whether to list what we have or note that one more is pending.

Looking back at method.tex §3.2, it already establishes the 20-language setup with the tier structure, so rather than duplicating all those details, I should focus on what's specific to the experimental execution—the actual setup details that go beyond what's already documented there.

The experiments section needs to specify the concrete implementation details: the layer counts for each model (94, 48, 28, 32 respectively), how many of those layers we actually probed (24, 12, 8, 9), the hardware configuration with the four RTX 6000 PRO GPUs and tensor parallelism strategy, and the specific probing hyperparameters like the liblinear solver with L2 regularization and C=1.0. I should also note the dimensionality reduction to 100 via PCA and the 5-fold cross-validation setup. For metrics, method.tex mentions ECE but I need to clarify we're using the scaled Brier ECE variant specifically, plus Spearman correlation. The statistical rigor comes from bootstrap confidence intervals, permutation tests, Cohen's d effect sizes, and partial correlation analysis to control for confounds. I'm noticing a discrepancy between the method section and the task specification—the Director says Qwen3 has 94 layers with sampling every ~4th layer yielding 24 layers, but method.tex specifies every 8th for 96-layer models which would give only 12. Since the task specification is more recent and authoritative, I'll follow that for the experiments setup.

Now I'm writing out the experimental section with dataset details across 19 typologically diverse languages grouped by resource availability, partitioned into probe_train and eval sets, but I'm realizing method.tex already mentions 20 languages so I should align with that for consistency. I need to resolve the language count inconsistency by cross-referencing method.tex rather than listing everything again. Now I'm setting up the experimental section with the dataset split into training and evaluation portions, then describing the two model families we're testing at different scales—the primary models being the larger Qwen and Llama variants, with smaller pilot versions for comparison.

For the methodology, I'm extracting activations from intermediate layers using forward hooks, then training logistic regression classifiers on the English labels with dimensionality reduction via PCA and cross-validation to evaluate the probes across different transfer scenarios.

Now I'm specifying the evaluation metrics—AUROC as the primary measure, along with calibration quality and correlation metrics—and establishing the statistical framework with bootstrap confidence intervals and permutation tests to compare methods rigorously.

The experiments run on 4 NVIDIA RTX 6000 PRO GPUs with 96GB each, where the largest model requires tensor parallelism across all four devices while smaller models fit on a single GPU.

Now I'm laying out the dataset structure across three resource tiers—high-resource languages like Chinese, German, Spanish and French; medium-resource ones including Arabic, Indonesian, and Turkish; and low-resource languages such as Bengali, Hindi, and Swahili. The test set gets split 70/30 into a probe training portion and evaluation portion, where English labels from the probe set provide the only supervision signal and all metrics come from the held-out evaluation split. I'm settling on matching method.tex exactly—20 languages across the three resource tiers, with the same breakdown they use. I'll keep the language list concise by cross-referencing rather than repeating it all. For the experiments section, I'm aiming for tight, precise writing that follows their conventions: using `\S\ref{...}` for cross-references and re-citing GlobalMMLU for self-containment in the experiments section.

Writing LaTeX for the experiments section... I'm setting up the model evaluation with two tiers: primary models including Qwen3-235B and Llama 4 Scout 17B with their respective quantization schemes and layer counts, plus smaller pilot models like Qwen2.5-7B and Llama-3.1-8B to test the methodology first. For activation extraction, I'm hooking into the residual stream at every fourth layer across all models to get a consistent set of probed layers, then applying logistic regression classifiers for the probing protocol.

For evaluation, I'm using AUROC as the main metric to measure discrimination quality, supplemented with calibration metrics like Soft-Binned ECE and Spearman correlation for analyzing how well the probes transfer across depths and languages, with standard ECE and Brier score available as additional details.

For statistical rigor, I'm computing bootstrap confidence intervals across 1000 resamples for all metrics, running paired permutation tests to compare methods with Cohen's d effect sizes, and controlling for layer depth in the CKA analysis using partial correlation—all with two-sided significance testing at α=0.05.

The experiments are running on four NVIDIA RTX 6000 PRO GPUs with 96GB each, where the largest Qwen3-235B model uses all four under tensor parallelism while the smaller models fit on single devices.

Now I'm organizing the results sections for the main transfer findings, Pareto frontier analysis, CKA geometric patterns, decomposition results, empirical observations, and CaCLR analysis. I'm reconsidering the citation format—`\citep[SB-ECE;][]{karandikar2021sbece}` would produce the wrong output, so I'll just use "Soft-Binned ECE (SB-ECE) \citep{karandikar2021sbece}" for clarity. Since method.tex already defines SB-ECE in section 3.3(e), I can reference it directly, though a brief mention of what it stands for in the metrics paragraph helps readability. Now I need to verify that "Spearman ρ (depth-transfer correlation)" is handled correctly in the task description.

Checking the subsection labels against the task requirements to make sure everything matches exactly—Experimental Setup, Main Transfer Results, Pareto Frontier Analysis, CKA Geometric Analysis, Decomposition Analysis, and Empirical Findings all need to be present with their corresponding labels.

Now for the language count issue: the task specifies 5 languages for LOW tier, but I'm currently listing only 4. Method.tex handles a similar discrepancy by stating 20 total languages while listing 19, so I'll follow that same approach here—either cross-reference the methods section or add a note about the pending addition rather than trying to force a count that doesn't match what's actually listed. Writing the final LaTeX file...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "4f0969c9-d847-43b0-9596-10fa3bb2b8c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Frz6Zq6zS5Jbc2YT7zUxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9092,
      "cache_read_input_tokens": 36201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9092
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Write · `toolu_01UqZdV5JK3u75ohCDmki6wt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Dataset.} We evaluate on the GlobalMMLU test split % [TO_ADD_BIB: globalmmlu]\nacross 20 typologically diverse languages grouped into three resource tiers: \\textsc{high} (zh, de, es, fr, ja, ko, pt, ru; 8 languages), \\textsc{med} (ar, id, nl, pl, tr, uk, vi; 7 languages), and \\textsc{low} (bn, hi, sw, te, plus one additional language; 5 languages). The test split is partitioned 70/30 via stratified sampling into \\texttt{probe\\_train} and \\texttt{eval} portions (\\S\\ref{sec:framework}). English correctness labels from \\texttt{probe\\_train} serve as the sole supervision; all reported metrics use \\texttt{eval} exclusively.\n\n\\paragraph{Models.} We evaluate two architecture families at two scales. Primary models (P0): Qwen3-235B-A22B (GPTQ-Int4, 94 layers, ${\\sim}$125\\,GB VRAM under 4-GPU tensor parallelism) and Llama~4 Scout 17B-16E (W4A16 weight quantization, 48 layers, mixture-of-experts with 16 experts). Pilot models (MVP): Qwen2.5-7B-Instruct (INT8, 28 layers) and Llama-3.1-8B-Instruct (INT8, 32 layers). The pilot pair spans both architecture families and validates methodology and hyperparameter choices before committing P0 GPU budget.\n\n\\paragraph{Activation Extraction.} We register forward hooks on the post-layer-norm residual stream at every 4th layer, yielding 8 probed layers for the 28-layer Qwen2.5-7B, 9 for the 32-layer Llama-3.1-8B, 12 for the 48-layer Llama~4 Scout, and 24 for the 94-layer Qwen3-235B.\n\n\\paragraph{Probing Protocol.} Logistic regression classifiers (liblinear solver, L2 regularization, $C{=}1.0$, \\texttt{max\\_iter}{=}2000) are trained on English \\texttt{probe\\_train} correctness labels. Activations are reduced to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting (\\S\\ref{sec:controls}). All probes are evaluated with 5-fold stratified cross-validation. We compare five transfer conditions as described in \\S\\ref{sec:transfer}: zero-shot, mean-shift, Procrustes, few-shot with 25 and 100 target-language labeled examples, and CaCLR.\n\n\\paragraph{Evaluation Metrics.} AUROC serves as the primary discrimination metric. We report Soft-Binned ECE (SB-ECE) \\citep{karandikar2021sbece} for calibration quality and Spearman~$\\rho$ for the depth-transfer correlation analysis (\\S\\ref{sec:geometric}). Standard ECE and Brier score are reported in the Appendix.\n\n\\paragraph{Statistical Testing.} All reported metrics include bootstrap confidence intervals (1000 resamples). Method comparisons use paired permutation tests; we report Cohen's~$d$ effect sizes for key comparisons. The CKA-transfer analysis (\\S\\ref{sec:geometric}) employs partial correlation controlling for layer depth. All $p$-values are two-sided with significance threshold $\\alpha{=}0.05$.\n\n\\paragraph{Hardware.} All experiments run on 4$\\times$ NVIDIA RTX 6000 PRO (96\\,GB each). The Qwen3-235B model requires all four GPUs under tensor parallelism; pilot and Scout models each fit on a single device. % [TODO: total GPU-hours estimate]\n\n\\subsection{Main Transfer Results}\n\\label{sec:main_results}\n\n\\subsection{Pareto Frontier Analysis}\n\\label{sec:pareto_results}\n\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka_results}\n\n\\subsection{Decomposition Analysis}\n\\label{sec:decomp_results}\n\n\\subsection{Empirical Findings}\n\\label{sec:empirical}\n\n\\subsection{CaCLR Analysis}\n\\label{sec:caclr_results}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "f5fbf496-893f-4acc-b2b7-d1e11cc7705f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Frz6Zq6zS5Jbc2YT7zUxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9092,
      "cache_read_input_tokens": 36201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9092
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T06:47:25.271Z_

<details><summary>↩ Tool result · `toolu_01UqZdV5JK3u75ohCDmki6wt`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "eef6f7c9-ec17-4607-a53a-bda8cce7949e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Dataset.} We evaluate on the GlobalMMLU test split % [TO_ADD_BIB: globalmmlu]\nacross 20 typologically diverse languages grouped into three resource tiers: \\textsc{high} (zh, de, es, fr, ja, ko, pt, ru; 8 languages), \\textsc{med} (ar, id, nl, pl, tr, uk, vi; 7 languages), and \\textsc{low} (bn, hi, sw, te, plus one additional language; 5 languages). The test split is partitioned 70/30 via stratified sampling into \\texttt{probe\\_train} and \\texttt{eval} portions (\\S\\ref{sec:framework}). English correctness labels from \\texttt{probe\\_train} serve as the sole supervision; all reported metrics use \\texttt{eval} exclusively.\n\n\\paragraph{Models.} We evaluate two architecture families at two scales. Primary models (P0): Qwen3-235B-A22B (GPTQ-Int4, 94 layers, ${\\sim}$125\\,GB VRAM under 4-GPU tensor parallelism) and Llama~4 Scout 17B-16E (W4A16 weight quantization, 48 layers, mixture-of-experts with 16 experts). Pilot models (MVP): Qwen2.5-7B-Instruct (INT8, 28 layers) and Llama-3.1-8B-Instruct (INT8, 32 layers). The pilot pair spans both architecture families and validates methodology and hyperparameter choices before committing P0 GPU budget.\n\n\\paragraph{Activation Extraction.} We register forward hooks on the post-layer-norm residual stream at every 4th layer, yielding 8 probed layers for the 28-layer Qwen2.5-7B, 9 for the 32-layer Llama-3.1-8B, 12 for the 48-layer Llama~4 Scout, and 24 for the 94-layer Qwen3-235B.\n\n\\paragraph{Probing Protocol.} Logistic regression classifiers (liblinear solver, L2 regularization, $C{=}1.0$, \\texttt{max\\_iter}{=}2000) are trained on English \\texttt{probe\\_train} correctness labels. Activations are reduced to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting (\\S\\ref{sec:controls}). All probes are evaluated with 5-fold stratified cross-validation. We compare five transfer conditions as described in \\S\\ref{sec:transfer}: zero-shot, mean-shift, Procrustes, few-shot with 25 and 100 target-language labeled examples, and CaCLR.\n\n\\paragraph{Evaluation Metrics.} AUROC serves as the primary discrimination metric. We report Soft-Binned ECE (SB-ECE) \\citep{karandikar2021sbece} for calibration quality and Spearman~$\\rho$ for the depth-transfer correlation analysis (\\S\\ref{sec:geometric}). Standard ECE and Brier score are reported in the Appendix.\n\n\\paragraph{Statistical Testing.} All reported metrics include bootstrap confidence intervals (1000 resamples). Method comparisons use paired permutation tests; we report Cohen's~$d$ effect sizes for key comparisons. The CKA-transfer analysis (\\S\\ref{sec:geometric}) employs partial correlation controlling for layer depth. All $p$-values are two-sided with significance threshold $\\alpha{=}0.05$.\n\n\\paragraph{Hardware.} All experiments run on 4$\\times$ NVIDIA RTX 6000 PRO (96\\,GB each). The Qwen3-235B model requires all four GPUs under tensor parallelism; pilot and Scout models each fit on a single device. % [TODO: total GPU-hours estimate]\n\n\\subsection{Main Transfer Results}\n\\label{sec:main_results}\n\n\\subsection{Pareto Frontier Analysis}\n\\label{sec:pareto_results}\n\n\\subsection{CKA Geometric Analysis}\n\\label{sec:cka_results}\n\n\\subsection{Decomposition Analysis}\n\\label{sec:decomp_results}\n\n\\subsection{Empirical Findings}\n\\label{sec:empirical}\n\n\\subsection{CaCLR Analysis}\n\\label{sec:caclr_results}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 21_

已写入 `docs/paper/experiments.tex`。§4.1 Setup 约 400 词，7 个 `\paragraph{}` 组织（Dataset, Models, Activation Extraction, Probing Protocol, Evaluation Metrics, Statistical Testing, Hardware）。§4.2–4.7 留空标题待后续填充。

留了两处标记需后续处理：
- `% [TO_ADD_BIB: globalmmlu]` — GlobalMMLU 的 bib 条目
- `% [TODO: total GPU-hours estimate]` — 总 GPU 时数待实验完成后补填

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "uuid": "c830ea9c-5adf-4264-9021-5a39c5897611",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0121qmXMYFKRBPURRRi225eq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8949,
      "cache_read_input_tokens": 45293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8949
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 22_

已写入 `docs/paper/experiments.tex`。§4.1 Setup 约 400 词，7 个 `\paragraph{}` 组织（Dataset, Models, Activation Extraction, Probing Protocol, Evaluation Metrics, Statistical Testing, Hardware）。§4.2–4.7 留空标题待后续填充。

留了两处标记需后续处理：
- `% [TO_ADD_BIB: globalmmlu]` — GlobalMMLU 的 bib 条目
- `% [TODO: total GPU-hours estimate]` — 总 GPU 时数待实验完成后补填

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 168469,
  "duration_api_ms": 169479,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "c946d1f3-a553-4272-9b55-7550bb6bdcab",
  "total_cost_usd": 0.56581275,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 42401,
    "cache_read_input_tokens": 118225,
    "output_tokens": 9574,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42401,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 161,
        "cache_read_input_tokens": 45293,
        "cache_creation_input_tokens": 8949,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 8949
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2214,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0023139999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 9574,
      "cacheReadInputTokens": 118225,
      "cacheCreationInputTokens": 42401,
      "webSearchRequests": 0,
      "costUSD": 0.56349875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "91375e1a-7f95-44e8-8af3-58313880454c"
}
```

</details>

---
