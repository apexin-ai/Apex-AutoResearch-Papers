# paper writing method

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_method_20260520T230735.log`
- **Structured JSON:** [`13dc8994ad2417391e32.json`](../../sessions/13/13dc8994ad2417391e32.json)

## Before a recorded user message

26 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
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
  "uuid": "dfcfa6f8-a350-4c61-a14e-2020e883fc4b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779326400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ea4ccc49-bbbe-4294-9b45-157969561079",
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write the Method section for the ColliForce-VLA paper. Let me first read the required reference materials:
1. Paper writing norms skill
2. LaTeX paper skill
3. The method draft (main source)
4. The introduction (for consistency)

Let me read these files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "3ca869d6-9f99-4953-a19f-57647969acbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYFNMerQ3WULwUB2vFvkKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13873,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13873
      },
      "output_tokens": 31,
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

Let me read the required reference materials first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "8a40b08a-e4b4-4dc2-aaea-261c0e29d247",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYFNMerQ3WULwUB2vFvkKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13873,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13873
      },
      "output_tokens": 31,
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

<details open><summary>🔧 Tool call — Read · `toolu_01VJd1txSmmdV5rkVBMirh9r`</summary>

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
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "7e0dbcac-3a60-48eb-90d9-627616e6a8a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYFNMerQ3WULwUB2vFvkKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13873,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13873
      },
      "output_tokens": 31,
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

_source line 7 · 2026-05-20T23:07:49.336Z_

<details><summary>↩ Tool result · `toolu_01VJd1txSmmdV5rkVBMirh9r`</summary>

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
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "5211b06a-841f-4d75-a59a-d5c923d4ad26",
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

<details open><summary>🔧 Tool call — Read · `toolu_01AfXBQXLcn19Fq6TvCVs2Bt`</summary>

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
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "2055c550-f08e-4793-8c7d-a02d0febf626",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYFNMerQ3WULwUB2vFvkKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13873,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13873
      },
      "output_tokens": 31,
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

_source line 9 · 2026-05-20T23:07:49.694Z_

<details><summary>↩ Tool result · `toolu_01AfXBQXLcn19Fq6TvCVs2Bt`</summary>

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
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "b555c323-eef1-431d-b20f-09b7d394f2d6",
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

<details open><summary>🔧 Tool call — Read · `toolu_01QedRt6yAUjuJNKNtNzoY5w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/method_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "7ceb99f8-94c9-4e2b-8979-01a32772a351",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYFNMerQ3WULwUB2vFvkKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13873,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13873
      },
      "output_tokens": 31,
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

_source line 11 · 2026-05-20T23:07:50.231Z_

<details><summary>↩ Tool result · `toolu_01QedRt6yAUjuJNKNtNzoY5w`</summary>

```text
1	## 3. Method
2	
3	We present **ColliForce**, a framework that integrates differentiable workspace Signed Distance Fields (SDFs) into Vision-Language-Action models to enable collision-aware action generation. Our approach operates in the feature space of a pretrained VLA, requiring no architectural modification to the backbone. We describe the problem setting (Sec. 3.1), the differentiable SDF integration (Sec. 3.2), the gradient-guided action refinement mechanism (Sec. 3.3), the training protocol (Sec. 3.4), and inference-time deployment (Sec. 3.5).
4	
5	### 3.1 Problem Formulation
6	
7	We consider a language-conditioned robotic manipulation setting where a Vision-Language-Action model $\pi_\theta$ generates an action trajectory $\{a_t\}_{t=1}^{H}$ with action horizon $H = 50$ conditioned on visual observations $o$ and a language instruction $l$. Each action $a_t \in \mathbb{R}^7$ specifies the desired end-effector (EE) displacement in position ($\Delta x, \Delta y, \Delta z$), orientation ($\Delta q_1, \ldots, \Delta q_3$), and gripper state.
8	
9	In cluttered workspaces, the generated trajectory may command the EE into regions occupied by obstacles, causing collisions that damage objects or interrupt task execution. We formalize the collision avoidance objective through the workspace Signed Distance Field $\Phi: \mathbb{R}^3 \to \mathbb{R}$, where $\Phi(\mathbf{x}) > 0$ indicates free space, $\Phi(\mathbf{x}) = 0$ denotes the obstacle boundary, and $\Phi(\mathbf{x}) < 0$ indicates penetration. The goal is to learn a policy that generates trajectories satisfying $\Phi(\text{EE}(a_t)) > 0$ for all $t$, while preserving task success.
10	
11	Our base VLA is $\pi_0$ (Physical Intelligence), a 3.5B-parameter flow-matching model comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. Action generation proceeds via iterative denoising over $H$ steps, producing a sequence of action tokens through the action expert's output projection $W_{\text{out}} \in \mathbb{R}^{1024 \times 32}$ that maps from the expert's hidden dimension to the action token space.
12	
13	### 3.2 Differentiable Workspace SDF Integration
14	
15	We augment the VLA with two lightweight auxiliary modules that operate on the action expert's intermediate representations.
16	
17	**Feature extraction.** We capture the action expert's suffix output $\mathbf{z} \in \mathbb{R}^{B \times H \times 1024}$ — the input to the action output projection $W_{\text{out}}$ — via a forward hook registered on `action_out_proj`. A mean-pooling operation along the action horizon dimension yields a compact feature vector $\bar{\mathbf{z}} = \frac{1}{H} \sum_{t=1}^{H} \mathbf{z}_t \in \mathbb{R}^{1024}$ that summarizes the action expert's spatial understanding of the current scene.
18	
19	**SDF Decoder.** A 4-layer MLP $f_\text{SDF}$ predicts the signed distance value at arbitrary 3D query points given the pooled action expert features:
20	
21	$$f_\text{SDF}: (\bar{\mathbf{z}}, \mathbf{x}) \mapsto \hat{\Phi}(\mathbf{x}), \quad \bar{\mathbf{z}} \in \mathbb{R}^{1024}, \; \mathbf{x} \in \mathbb{R}^3$$
22	
23	The architecture employs hidden dimension 256 with Softplus activation ($\beta = 5$) and a skip connection that re-injects the query coordinates at the second layer:
24	
25	$$\mathbf{h}_0 = \sigma(\mathbf{W}_0 [\bar{\mathbf{z}}; \mathbf{x}] + \mathbf{b}_0)$$
26	$$\mathbf{h}_1 = \sigma(\mathbf{W}_1 \mathbf{h}_0 + \mathbf{b}_1)$$
27	$$\mathbf{h}_2 = \sigma(\mathbf{W}_2 [\mathbf{h}_1; \mathbf{x}] + \mathbf{b}_2)$$
28	$$\hat{\Phi}(\mathbf{x}) = \mathbf{W}_3 \mathbf{h}_2 + \mathbf{b}_3$$
29	
30	where $\sigma(\cdot) = \text{Softplus}_{\beta=5}(\cdot)$, $\mathbf{W}_0 \in \mathbb{R}^{256 \times 1027}$, $\mathbf{W}_1 \in \mathbb{R}^{256 \times 256}$, $\mathbf{W}_2 \in \mathbb{R}^{256 \times 259}$, and $\mathbf{W}_3 \in \mathbb{R}^{1 \times 256}$. All weights are initialized with Kaiming normal initialization.
31	
32	For spatial gradient computation (required by Eikonal regularization and gradient-guided refinement), the decoder computes $\nabla_{\mathbf{x}} \hat{\Phi}(\mathbf{x})$ via `torch.autograd.grad` with graph creation enabled during training.
33	
34	**End-Effector Position Extractor.** A 2-layer MLP $g_\text{EE}$ predicts the current EE position from the pooled features:
35	
36	$$g_\text{EE}: \bar{\mathbf{z}} \mapsto \hat{\mathbf{p}}_\text{EE} \in \mathbb{R}^3$$
37	
38	with architecture $\text{Linear}(1024, 256) \to \text{ReLU} \to \text{Linear}(256, 3)$. The EE prediction serves dual purposes: (1) it provides the query point for evaluating collision proximity, and (2) its auxiliary loss encourages the action expert features to encode spatial position information.
39	
40	**Auxiliary training losses.** The SDF decoder is trained with a clamped L1 loss augmented by Eikonal regularization:
41	
42	$$\mathcal{L}_\text{SDF} = \underbrace{\frac{1}{N} \sum_{i=1}^{N} \left| \text{clamp}(\hat{\Phi}(\mathbf{x}_i), \pm\delta) - \text{clamp}(\Phi^*(\mathbf{x}_i), \pm\delta) \right|}_{\mathcal{L}_\text{L1}} + \lambda_\text{eik} \underbrace{\frac{1}{N} \sum_{i=1}^{N} \left( \|\nabla_{\mathbf{x}} \hat{\Phi}(\mathbf{x}_i)\|_2 - 1 \right)^2}_{\mathcal{L}_\text{eikonal}}$$
43	
44	where $\delta = 0.05$ is the clamping threshold, $\lambda_\text{eik} = 0.1$, and $N = 64$ query points are randomly sampled from the ground-truth SDF volume per training step. The clamping focuses learning on the near-surface region most relevant for collision detection. The Eikonal term enforces the unit-gradient property of valid distance fields.
45	
46	The EE extractor is trained with MSE loss against ground-truth EE positions from the robot state:
47	
48	$$\mathcal{L}_\text{EE} = \|\hat{\mathbf{p}}_\text{EE} - \mathbf{p}^*_\text{EE}\|_2^2$$
49	
50	### 3.3 SDF Gradient-Guided Action Refinement
51	
52	The core contribution of ColliForce is a gradient-based mechanism that leverages the differentiable SDF to steer the action expert's representations away from collision-prone regions during training. Unlike post-hoc action filtering, this approach modifies the feature space directly, enabling the model to internalize collision avoidance behavior.
53	
54	**Refinement procedure.** Given the captured suffix output $\mathbf{z} \in \mathbb{R}^{B \times H \times 1024}$, the refiner:
55	
56	1. Predicts the EE position and evaluates the SDF: $\hat{\mathbf{p}}_\text{EE} = g_\text{EE}(\bar{\mathbf{z}})$, $\hat{\Phi}(\hat{\mathbf{p}}_\text{EE}) = f_\text{SDF}(\bar{\mathbf{z}}, \hat{\mathbf{p}}_\text{EE})$.
57	
58	2. Identifies near-collision samples: $\mathcal{S} = \{i : \hat{\Phi}(\hat{\mathbf{p}}_{\text{EE},i}) < m\}$, where the safety margin $m = 0.01$.
59	
60	3. For samples in $\mathcal{S}$, computes the SDF gradient with respect to the suffix features: $\nabla_{\mathbf{z}} \hat{\Phi} = \frac{\partial \hat{\Phi}(\hat{\mathbf{p}}_\text{EE})}{\partial \mathbf{z}}$, capturing how changes in the action expert's internal representation affect the predicted collision distance.
61	
62	4. Performs gradient ascent on the SDF (toward higher, safer values):
63	
64	$$\mathbf{z}' = \mathbf{z} + \alpha \cdot \text{clip}(\nabla_{\mathbf{z}} \hat{\Phi}) \odot \mathbf{m}_\mathcal{S}$$
65	
66	where $\alpha = 0.1$ is the step size, $\text{clip}(\cdot)$ denotes per-sample L2 norm clipping with threshold $\gamma = 1.0$ for gradient stability, and $\mathbf{m}_\mathcal{S}$ is a binary mask selecting only near-collision samples.
67	
68	5. Projects both original and refined features through the action output head: $\mathbf{v}_t = W_\text{out}(\mathbf{z})$, $\mathbf{v}'_t = W_\text{out}(\mathbf{z}')$.
69	
70	**Refinement loss.** The model is trained to directly output the collision-corrected actions by minimizing the discrepancy between the original and refined predictions on near-collision samples:
71	
72	$$\mathcal{L}_\text{refine} = \frac{1}{|\mathcal{S}|} \sum_{i \in \mathcal{S}} \|\mathbf{v}_{t,i} - \text{sg}(\mathbf{v}'_{t,i})\|_2^2$$
73	
74	where $\text{sg}(\cdot)$ denotes the stop-gradient operator. The gradient flows only through $\mathbf{v}_t \to \mathbf{z} \to \theta_\text{LoRA}$, training the LoRA adapters to anticipate and avoid collisions without requiring the gradient refiner at inference time. The refined target $\mathbf{v}'_t$ is detached, serving as a teacher signal that encodes collision-aware behavior.
75	
76	This design is reminiscent of knowledge distillation: the SDF gradient refiner acts as a computationally expensive teacher that produces safe actions, while the student (the LoRA-adapted VLA) learns to replicate these actions directly, amortizing the SDF computation into the model's parameters.
77	
78	### 3.4 Training Protocol
79	
80	We adopt a two-phase training protocol that ensures SDF prediction accuracy before engaging gradient-guided refinement.
81	
82	**Baseline.** Standard LoRA fine-tuning of $\pi_0$ on task demonstrations using the flow-matching action loss $\mathcal{L}_\text{action}$. LoRA adapters are injected into both the PaliGemma encoder (rank 16, $\alpha = 16$) and the action expert (rank 32, $\alpha = 32$), targeting the attention projections ($\mathbf{W}_q, \mathbf{W}_k, \mathbf{W}_v, \mathbf{W}_o$) and MLP layers ($\mathbf{W}_\text{gate}, \mathbf{W}_\text{up}, \mathbf{W}_\text{down}$). The total LoRA parameter count is approximately 26M.
83	
84	**A1 — SDF Auxiliary Task.** This variant adds the SDF decoder and EE extractor as auxiliary tasks:
85	
86	- *Phase 1* ($0 \to T_\text{warmup}$ steps, $T_\text{warmup} = 5000$): The entire backbone (including LoRA parameters) is frozen. Only the SDF decoder ($\sim$395K parameters) and EE extractor ($\sim$263K parameters) are trained. The auxiliary modules receive detached features ($\bar{\mathbf{z}}.\text{detach()}$) to avoid destabilizing the pretrained backbone during warmup. This phase establishes an accurate SDF predictor anchored to the backbone's current feature distribution.
87	
88	- *Phase 2* ($T_\text{warmup} \to T_\text{end}$): LoRA parameters are unfrozen with a linear gradient warmup over 100 steps to prevent abrupt feature distribution shifts. The full loss is:
89	
90	$$\mathcal{L}_\text{A1} = \mathcal{L}_\text{action} + \lambda_\text{SDF} \cdot \mathcal{L}_\text{SDF} + \lambda_\text{EE} \cdot \mathcal{L}_\text{EE}$$
91	
92	where $\lambda_\text{SDF} = 0.1$ and $\lambda_\text{EE} = 0.01$. Gradients now flow from the auxiliary losses through the pooled features into the LoRA adapters, encouraging the action expert to develop features that encode workspace geometry.
93	
94	**A3 — SDF Gradient-Guided Refinement.** This variant extends A1 with the gradient refiner:
95	
96	- *Phase 1*: Identical to A1 — backbone frozen, SDF decoder and EE extractor warmup only.
97	
98	- *Phase 2*: LoRA unfreezing with gradient warmup (same as A1), plus activation of the gradient refiner. The full loss becomes:
99	
100	$$\mathcal{L}_\text{A3} = \mathcal{L}_\text{action} + \lambda_\text{SDF} \cdot \mathcal{L}_\text{SDF} + \lambda_\text{EE} \cdot \mathcal{L}_\text{EE} + \lambda_\text{refine} \cdot \mathcal{L}_\text{refine}$$
101	
102	where $\lambda_\text{refine} = 0.1$. The refinement loss is only computed when near-collision samples exist in the batch ($|\mathcal{S}| > 0$), adding zero computational overhead for collision-free training steps.
103	
104	All variants use AdamW with cosine decay scheduling (peak learning rate $2.5 \times 10^{-5}$, decaying to $2.5 \times 10^{-6}$), batch size 32, and train for 30,000 steps. The warmup period for the learning rate schedule is $\min(1000, T_\text{end} / 3)$ steps.
105	
106	### 3.5 Inference-Time Refinement
107	
108	At inference, ColliForce supports an optional SDF gradient correction that provides an additional safety layer without architectural changes to the deployed model:
109	
110	1. The VLA generates an action $a_t$ through standard forward pass.
111	2. The predicted next EE position is computed: $\hat{\mathbf{p}}_\text{next} = \mathbf{p}_\text{EE} + a_t[:3]$.
112	3. The SDF decoder queries the predicted SDF at this position: $\hat{\Phi}(\hat{\mathbf{p}}_\text{next})$.
113	4. If $\hat{\Phi}(\hat{\mathbf{p}}_\text{next}) < m$ (near collision), the action's position component is corrected:
114	
115	$$a'_t[:3] = a_t[:3] + \alpha \cdot \frac{\nabla_{\mathbf{x}} \hat{\Phi}(\hat{\mathbf{p}}_\text{next})}{\|\nabla_{\mathbf{x}} \hat{\Phi}(\hat{\mathbf{p}}_\text{next})\|_2}$$
116	
117	The L2-normalization bounds the correction magnitude to $\alpha$ regardless of the SDF gradient scale, preventing over-correction near sharp obstacle boundaries. Orientation and gripper components of $a_t$ remain unchanged.
118	
119	This inference-time mechanism introduces zero additional latency when $\hat{\Phi}(\hat{\mathbf{p}}_\text{next}) \geq m$ (i.e., the EE is sufficiently far from obstacles). For the A3 variant trained with gradient refinement, the model has already learned to produce collision-avoiding actions, so inference-time refinement serves as a complementary safety net for out-of-distribution obstacle configurations.
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "7a996a5d-0cc1-4d13-b318-627e2ba86109",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/method_draft.md",
      "content": "## 3. Method\n\nWe present **ColliForce**, a framework that integrates differentiable workspace Signed Distance Fields (SDFs) into Vision-Language-Action models to enable collision-aware action generation. Our approach operates in the feature space of a pretrained VLA, requiring no architectural modification to the backbone. We describe the problem setting (Sec. 3.1), the differentiable SDF integration (Sec. 3.2), the gradient-guided action refinement mechanism (Sec. 3.3), the training protocol (Sec. 3.4), and inference-time deployment (Sec. 3.5).\n\n### 3.1 Problem Formulation\n\nWe consider a language-conditioned robotic manipulation setting where a Vision-Language-Action model $\\pi_\\theta$ generates an action trajectory $\\{a_t\\}_{t=1}^{H}$ with action horizon $H = 50$ conditioned on visual observations $o$ and a language instruction $l$. Each action $a_t \\in \\mathbb{R}^7$ specifies the desired end-effector (EE) displacement in position ($\\Delta x, \\Delta y, \\Delta z$), orientation ($\\Delta q_1, \\ldots, \\Delta q_3$), and gripper state.\n\nIn cluttered workspaces, the generated trajectory may command the EE into regions occupied by obstacles, causing collisions that damage objects or interrupt task execution. We formalize the collision avoidance objective through the workspace Signed Distance Field $\\Phi: \\mathbb{R}^3 \\to \\mathbb{R}$, where $\\Phi(\\mathbf{x}) > 0$ indicates free space, $\\Phi(\\mathbf{x}) = 0$ denotes the obstacle boundary, and $\\Phi(\\mathbf{x}) < 0$ indicates penetration. The goal is to learn a policy that generates trajectories satisfying $\\Phi(\\text{EE}(a_t)) > 0$ for all $t$, while preserving task success.\n\nOur base VLA is $\\pi_0$ (Physical Intelligence), a 3.5B-parameter flow-matching model comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. Action generation proceeds via iterative denoising over $H$ steps, producing a sequence of action tokens through the action expert's output projection $W_{\\text{out}} \\in \\mathbb{R}^{1024 \\times 32}$ that maps from the expert's hidden dimension to the action token space.\n\n### 3.2 Differentiable Workspace SDF Integration\n\nWe augment the VLA with two lightweight auxiliary modules that operate on the action expert's intermediate representations.\n\n**Feature extraction.** We capture the action expert's suffix output $\\mathbf{z} \\in \\mathbb{R}^{B \\times H \\times 1024}$ — the input to the action output projection $W_{\\text{out}}$ — via a forward hook registered on `action_out_proj`. A mean-pooling operation along the action horizon dimension yields a compact feature vector $\\bar{\\mathbf{z}} = \\frac{1}{H} \\sum_{t=1}^{H} \\mathbf{z}_t \\in \\mathbb{R}^{1024}$ that summarizes the action expert's spatial understanding of the current scene.\n\n**SDF Decoder.** A 4-layer MLP $f_\\text{SDF}$ predicts the signed distance value at arbitrary 3D query points given the pooled action expert features:\n\n$$f_\\text{SDF}: (\\bar{\\mathbf{z}}, \\mathbf{x}) \\mapsto \\hat{\\Phi}(\\mathbf{x}), \\quad \\bar{\\mathbf{z}} \\in \\mathbb{R}^{1024}, \\; \\mathbf{x} \\in \\mathbb{R}^3$$\n\nThe architecture employs hidden dimension 256 with Softplus activation ($\\beta = 5$) and a skip connection that re-injects the query coordinates at the second layer:\n\n$$\\mathbf{h}_0 = \\sigma(\\mathbf{W}_0 [\\bar{\\mathbf{z}}; \\mathbf{x}] + \\mathbf{b}_0)$$\n$$\\mathbf{h}_1 = \\sigma(\\mathbf{W}_1 \\mathbf{h}_0 + \\mathbf{b}_1)$$\n$$\\mathbf{h}_2 = \\sigma(\\mathbf{W}_2 [\\mathbf{h}_1; \\mathbf{x}] + \\mathbf{b}_2)$$\n$$\\hat{\\Phi}(\\mathbf{x}) = \\mathbf{W}_3 \\mathbf{h}_2 + \\mathbf{b}_3$$\n\nwhere $\\sigma(\\cdot) = \\text{Softplus}_{\\beta=5}(\\cdot)$, $\\mathbf{W}_0 \\in \\mathbb{R}^{256 \\times 1027}$, $\\mathbf{W}_1 \\in \\mathbb{R}^{256 \\times 256}$, $\\mathbf{W}_2 \\in \\mathbb{R}^{256 \\times 259}$, and $\\mathbf{W}_3 \\in \\mathbb{R}^{1 \\times 256}$. All weights are initialized with Kaiming normal initialization.\n\nFor spatial gradient computation (required by Eikonal regularization and gradient-guided refinement), the decoder computes $\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\mathbf{x})$ via `torch.autograd.grad` with graph creation enabled during training.\n\n**End-Effector Position Extractor.** A 2-layer MLP $g_\\text{EE}$ predicts the current EE position from the pooled features:\n\n$$g_\\text{EE}: \\bar{\\mathbf{z}} \\mapsto \\hat{\\mathbf{p}}_\\text{EE} \\in \\mathbb{R}^3$$\n\nwith architecture $\\text{Linear}(1024, 256) \\to \\text{ReLU} \\to \\text{Linear}(256, 3)$. The EE prediction serves dual purposes: (1) it provides the query point for evaluating collision proximity, and (2) its auxiliary loss encourages the action expert features to encode spatial position information.\n\n**Auxiliary training losses.** The SDF decoder is trained with a clamped L1 loss augmented by Eikonal regularization:\n\n$$\\mathcal{L}_\\text{SDF} = \\underbrace{\\frac{1}{N} \\sum_{i=1}^{N} \\left| \\text{clamp}(\\hat{\\Phi}(\\mathbf{x}_i), \\pm\\delta) - \\text{clamp}(\\Phi^*(\\mathbf{x}_i), \\pm\\delta) \\right|}_{\\mathcal{L}_\\text{L1}} + \\lambda_\\text{eik} \\underbrace{\\frac{1}{N} \\sum_{i=1}^{N} \\left( \\|\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\mathbf{x}_i)\\|_2 - 1 \\right)^2}_{\\mathcal{L}_\\text{eikonal}}$$\n\nwhere $\\delta = 0.05$ is the clamping threshold, $\\lambda_\\text{eik} = 0.1$, and $N = 64$ query points are randomly sampled from the ground-truth SDF volume per training step. The clamping focuses learning on the near-surface region most relevant for collision detection. The Eikonal term enforces the unit-gradient property of valid distance fields.\n\nThe EE extractor is trained with MSE loss against ground-truth EE positions from the robot state:\n\n$$\\mathcal{L}_\\text{EE} = \\|\\hat{\\mathbf{p}}_\\text{EE} - \\mathbf{p}^*_\\text{EE}\\|_2^2$$\n\n### 3.3 SDF Gradient-Guided Action Refinement\n\nThe core contribution of ColliForce is a gradient-based mechanism that leverages the differentiable SDF to steer the action expert's representations away from collision-prone regions during training. Unlike post-hoc action filtering, this approach modifies the feature space directly, enabling the model to internalize collision avoidance behavior.\n\n**Refinement procedure.** Given the captured suffix output $\\mathbf{z} \\in \\mathbb{R}^{B \\times H \\times 1024}$, the refiner:\n\n1. Predicts the EE position and evaluates the SDF: $\\hat{\\mathbf{p}}_\\text{EE} = g_\\text{EE}(\\bar{\\mathbf{z}})$, $\\hat{\\Phi}(\\hat{\\mathbf{p}}_\\text{EE}) = f_\\text{SDF}(\\bar{\\mathbf{z}}, \\hat{\\mathbf{p}}_\\text{EE})$.\n\n2. Identifies near-collision samples: $\\mathcal{S} = \\{i : \\hat{\\Phi}(\\hat{\\mathbf{p}}_{\\text{EE},i}) < m\\}$, where the safety margin $m = 0.01$.\n\n3. For samples in $\\mathcal{S}$, computes the SDF gradient with respect to the suffix features: $\\nabla_{\\mathbf{z}} \\hat{\\Phi} = \\frac{\\partial \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\text{EE})}{\\partial \\mathbf{z}}$, capturing how changes in the action expert's internal representation affect the predicted collision distance.\n\n4. Performs gradient ascent on the SDF (toward higher, safer values):\n\n$$\\mathbf{z}' = \\mathbf{z} + \\alpha \\cdot \\text{clip}(\\nabla_{\\mathbf{z}} \\hat{\\Phi}) \\odot \\mathbf{m}_\\mathcal{S}$$\n\nwhere $\\alpha = 0.1$ is the step size, $\\text{clip}(\\cdot)$ denotes per-sample L2 norm clipping with threshold $\\gamma = 1.0$ for gradient stability, and $\\mathbf{m}_\\mathcal{S}$ is a binary mask selecting only near-collision samples.\n\n5. Projects both original and refined features through the action output head: $\\mathbf{v}_t = W_\\text{out}(\\mathbf{z})$, $\\mathbf{v}'_t = W_\\text{out}(\\mathbf{z}')$.\n\n**Refinement loss.** The model is trained to directly output the collision-corrected actions by minimizing the discrepancy between the original and refined predictions on near-collision samples:\n\n$$\\mathcal{L}_\\text{refine} = \\frac{1}{|\\mathcal{S}|} \\sum_{i \\in \\mathcal{S}} \\|\\mathbf{v}_{t,i} - \\text{sg}(\\mathbf{v}'_{t,i})\\|_2^2$$\n\nwhere $\\text{sg}(\\cdot)$ denotes the stop-gradient operator. The gradient flows only through $\\mathbf{v}_t \\to \\mathbf{z} \\to \\theta_\\text{LoRA}$, training the LoRA adapters to anticipate and avoid collisions without requiring the gradient refiner at inference time. The refined target $\\mathbf{v}'_t$ is detached, serving as a teacher signal that encodes collision-aware behavior.\n\nThis design is reminiscent of knowledge distillation: the SDF gradient refiner acts as a computationally expensive teacher that produces safe actions, while the student (the LoRA-adapted VLA) learns to replicate these actions directly, amortizing the SDF computation into the model's parameters.\n\n### 3.4 Training Protocol\n\nWe adopt a two-phase training protocol that ensures SDF prediction accuracy before engaging gradient-guided refinement.\n\n**Baseline.** Standard LoRA fine-tuning of $\\pi_0$ on task demonstrations using the flow-matching action loss $\\mathcal{L}_\\text{action}$. LoRA adapters are injected into both the PaliGemma encoder (rank 16, $\\alpha = 16$) and the action expert (rank 32, $\\alpha = 32$), targeting the attention projections ($\\mathbf{W}_q, \\mathbf{W}_k, \\mathbf{W}_v, \\mathbf{W}_o$) and MLP layers ($\\mathbf{W}_\\text{gate}, \\mathbf{W}_\\text{up}, \\mathbf{W}_\\text{down}$). The total LoRA parameter count is approximately 26M.\n\n**A1 — SDF Auxiliary Task.** This variant adds the SDF decoder and EE extractor as auxiliary tasks:\n\n- *Phase 1* ($0 \\to T_\\text{warmup}$ steps, $T_\\text{warmup} = 5000$): The entire backbone (including LoRA parameters) is frozen. Only the SDF decoder ($\\sim$395K parameters) and EE extractor ($\\sim$263K parameters) are trained. The auxiliary modules receive detached features ($\\bar{\\mathbf{z}}.\\text{detach()}$) to avoid destabilizing the pretrained backbone during warmup. This phase establishes an accurate SDF predictor anchored to the backbone's current feature distribution.\n\n- *Phase 2* ($T_\\text{warmup} \\to T_\\text{end}$): LoRA parameters are unfrozen with a linear gradient warmup over 100 steps to prevent abrupt feature distribution shifts. The full loss is:\n\n$$\\mathcal{L}_\\text{A1} = \\mathcal{L}_\\text{action} + \\lambda_\\text{SDF} \\cdot \\mathcal{L}_\\text{SDF} + \\lambda_\\text{EE} \\cdot \\mathcal{L}_\\text{EE}$$\n\nwhere $\\lambda_\\text{SDF} = 0.1$ and $\\lambda_\\text{EE} = 0.01$. Gradients now flow from the auxiliary losses through the pooled features into the LoRA adapters, encouraging the action expert to develop features that encode workspace geometry.\n\n**A3 — SDF Gradient-Guided Refinement.** This variant extends A1 with the gradient refiner:\n\n- *Phase 1*: Identical to A1 — backbone frozen, SDF decoder and EE extractor warmup only.\n\n- *Phase 2*: LoRA unfreezing with gradient warmup (same as A1), plus activation of the gradient refiner. The full loss becomes:\n\n$$\\mathcal{L}_\\text{A3} = \\mathcal{L}_\\text{action} + \\lambda_\\text{SDF} \\cdot \\mathcal{L}_\\text{SDF} + \\lambda_\\text{EE} \\cdot \\mathcal{L}_\\text{EE} + \\lambda_\\text{refine} \\cdot \\mathcal{L}_\\text{refine}$$\n\nwhere $\\lambda_\\text{refine} = 0.1$. The refinement loss is only computed when near-collision samples exist in the batch ($|\\mathcal{S}| > 0$), adding zero computational overhead for collision-free training steps.\n\nAll variants use AdamW with cosine decay scheduling (peak learning rate $2.5 \\times 10^{-5}$, decaying to $2.5 \\times 10^{-6}$), batch size 32, and train for 30,000 steps. The warmup period for the learning rate schedule is $\\min(1000, T_\\text{end} / 3)$ steps.\n\n### 3.5 Inference-Time Refinement\n\nAt inference, ColliForce supports an optional SDF gradient correction that provides an additional safety layer without architectural changes to the deployed model:\n\n1. The VLA generates an action $a_t$ through standard forward pass.\n2. The predicted next EE position is computed: $\\hat{\\mathbf{p}}_\\text{next} = \\mathbf{p}_\\text{EE} + a_t[:3]$.\n3. The SDF decoder queries the predicted SDF at this position: $\\hat{\\Phi}(\\hat{\\mathbf{p}}_\\text{next})$.\n4. If $\\hat{\\Phi}(\\hat{\\mathbf{p}}_\\text{next}) < m$ (near collision), the action's position component is corrected:\n\n$$a'_t[:3] = a_t[:3] + \\alpha \\cdot \\frac{\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\text{next})}{\\|\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\text{next})\\|_2}$$\n\nThe L2-normalization bounds the correction magnitude to $\\alpha$ regardless of the SDF gradient scale, preventing over-correction near sharp obstacle boundaries. Orientation and gripper components of $a_t$ remain unchanged.\n\nThis inference-time mechanism introduces zero additional latency when $\\hat{\\Phi}(\\hat{\\mathbf{p}}_\\text{next}) \\geq m$ (i.e., the EE is sufficiently far from obstacles). For the A3 variant trained with gradient refinement, the model has already learned to produce collision-avoiding actions, so inference-time refinement serves as a complementary safety net for out-of-distribution obstacle configurations.\n",
      "numLines": 120,
      "startLine": 1,
      "totalLines": 120
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01Kdt7dgxQwJ1amrSe6ZoU84`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "eceb0a69-f984-4256-b32e-a44e5bafbd15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYFNMerQ3WULwUB2vFvkKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13873,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13873
      },
      "output_tokens": 31,
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

_source line 13 · 2026-05-20T23:07:50.428Z_

<details><summary>↩ Tool result · `toolu_01Kdt7dgxQwJ1amrSe6ZoU84`</summary>

```text
1	\section{Introduction}
2	
3	Vision-Language-Action (VLA) models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} combine visual perception, language understanding, and action generation in a unified architecture to follow diverse natural language instructions across manipulation tasks. These models learn action policies from large-scale demonstration datasets and can generalize to new instructions, objects, and scenes. Yet when deployed in cluttered environments where non-target objects densely surround the manipulation target, VLAs frequently produce trajectories that collide with surrounding obstacles. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies have no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and surrounding objects, and represent a critical barrier to safe deployment in household and industrial settings. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this failure mode and confirms that even high-performing VLAs exhibit substantial collision rates in constrained workspaces. The root cause is architectural: current VLAs observe scenes through 2D images, generate action sequences through learned policies, and have no internal mechanism to determine whether the predicted end-effector trajectory will intersect obstacle surfaces.
4	
5	Recent work addresses this problem, but exclusively through mechanisms external to the VLA's internal representations. AEGIS~\cite{hu2025vlsa} introduces a plug-in safety constraint layer based on Control Barrier Functions (CBFs): it identifies obstacles via open-set detection and depth estimation, then corrects unsafe actions after they have been generated, improving obstacle avoidance rate by 59.16\% on SafeLIBERO. Notably, AEGIS requires no additional training and can be attached to any pretrained VLA, a practical advantage. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning; this approach, however, does not incorporate geometric information about the workspace and relies entirely on learned reward signals to encode safety. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that detects dangerous configurations and halts execution when predicted collision risk exceeds a threshold. These approaches share a common architectural pattern: the safety mechanism operates independently of the VLA's learned feature representations. The model first generates a trajectory without collision awareness, and a separate module then evaluates or corrects it. This reactive paradigm faces two fundamental limitations. In cluttered environments, the space available for post-hoc trajectory correction shrinks, and corrections may push the end-effector into other obstacles. Because the VLA itself never learns to represent collision geometry, it cannot anticipate obstacles during action generation and will repeatedly propose unsafe trajectories that require external intervention. A proactive alternative would embed collision-relevant geometric information directly into the VLA's forward pass, so that action tokens encode collision awareness from the point of generation.
6	
7	A parallel research direction has enriched VLA architectures with 3D spatial information. Numerous recent methods integrate depth maps, point clouds, or implicit 3D representations into VLA training or inference~\cite{depthvla2025, li2025qdepth, li2025spatialforcing, 3dcavla2025, geoaware2025, spatialvla2025, gstvla2026, stemvla2026, stvla2026, evo02025, savla2026, augvla3d2026, evodepth2026}. These methods improve task success rate, viewpoint generalization, or grasping precision, but none targets collision avoidance as a design objective and none evaluates on collision-specific metrics. QDepth-VLA~\cite{li2025qdepth}, the closest methodological precedent for auxiliary spatial supervision in VLAs, uses quantized depth prediction as a training-time auxiliary loss via a VQ-VAE decoder. Its decoder is decoupled from the action head: depth gradients flow into the backbone but do not explicitly modify the action token generation pathway. Depth is a 2.5D camera-frame representation that encodes the distance from each pixel to the camera. Deriving collision-relevant directions in the robot's workspace from depth gradients requires an implicit perspective-to-workspace coordinate transformation that depends on camera intrinsics and extrinsics, and occluded regions (where obstacles may be hidden behind the robot arm or other objects) produce no depth signal. The result is a clear gap between two active communities: spatially-aware VLAs do not address collision avoidance, and collision-safe VLAs do not internalize spatial geometry into the model's representations.
8	
9	We propose ColliForce-VLA, which integrates a differentiable workspace Signed Distance Field (SDF) into the VLA forward pass for collision-aware action generation. Workspace SDF encodes, at each 3D point, the signed distance to the nearest obstacle surface; its spatial gradient points directly away from that surface in workspace coordinates. Unlike depth gradients that reside in camera frame, SDF gradients require no coordinate transformation and cover the full 3D workspace including occluded regions. SDF gradients indicate repulsion direction from obstacles by construction, and their continuous nature provides informative signals even at moderate distances from surfaces, in contrast to binary occupancy whose gradient is zero almost everywhere. ColliForce-VLA augments $\pi_0$~\cite{black2024pi0} with two lightweight modules attached to the action expert: an SDF Decoder (4-layer MLP, ${\sim}$395K parameters) that predicts workspace SDF from the action expert's pooled suffix features, and an End-Effector (EE) Extractor (2-layer MLP, ${\sim}$263K parameters) that predicts end-effector position from the same features. During training, for near-collision samples where predicted SDF at the end-effector is low, we compute $\nabla_z \Phi$, the gradient of predicted SDF with respect to the shared feature representation $z$, and perform gradient ascent ($z' = z + \alpha \cdot \nabla_z \Phi$) to push $z$ toward collision-free configurations. Both $z$ and $z'$ are projected into action token space, and a refinement loss trains the LoRA parameters (${\sim}$33.5M) to directly produce the collision-corrected actions without requiring the gradient refinement step. The SDF supervisory signal is derived from known workspace geometry (obstacle meshes available in simulation), requiring no additional sensors beyond the standard visual input. At inference, only the base model with trained LoRA is active; neither auxiliary module nor gradient computation is required, so the method adds no extra modules to the inference pipeline. Unlike AEGIS~\cite{hu2025vlsa}, which applies training-free post-hoc correction to already-generated trajectories, ColliForce-VLA internalizes collision geometry into the model's own parameters during training, enabling proactive avoidance at generation time with a potentially better CAR-TSR trade-off in cluttered settings. Unlike QDepth-VLA~\cite{li2025qdepth}, whose depth decoder provides camera-frame auxiliary gradients to the backbone without explicitly modifying action tokens, our SDF gradient refinement operates in workspace frame and directly modulates the feature representations from which action tokens are decoded. The collision-avoidance capability is absorbed into the model's LoRA parameters during training and does not rely on any external safety layer at deployment.
10	
11	Our contributions are as follows:
12	\begin{itemize}
13	    \item We introduce a differentiable collision-aware mechanism for VLAs that integrates workspace SDF into the forward pass. SDF gradients in feature space ($\nabla_z \Phi$) guide action token generation toward collision-free configurations and provide a proactive alternative to post-hoc safety correction (Section~\ref{sec:method}).
14	    \item We design a gradient-guided refinement training strategy where SDF gradients in feature space produce collision-corrected action targets, and LoRA parameters learn to reproduce these targets directly. The trained model requires no additional modules at inference (Section~\ref{sec:training}).
15	    \item We conduct systematic experiments and ablation studies on the SafeLIBERO benchmark that separately quantify the contributions of SDF auxiliary supervision and SDF gradient-guided refinement to Collision Avoidance Rate (CAR) and Task Success Rate (TSR) \textbf{[TODO: specific numbers pending experiments]} (Section~\ref{sec:experiments}).
16	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "1edf3148-707e-426a-b14c-9933e12a5c5a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nVision-Language-Action (VLA) models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} combine visual perception, language understanding, and action generation in a unified architecture to follow diverse natural language instructions across manipulation tasks. These models learn action policies from large-scale demonstration datasets and can generalize to new instructions, objects, and scenes. Yet when deployed in cluttered environments where non-target objects densely surround the manipulation target, VLAs frequently produce trajectories that collide with surrounding obstacles. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies have no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and surrounding objects, and represent a critical barrier to safe deployment in household and industrial settings. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this failure mode and confirms that even high-performing VLAs exhibit substantial collision rates in constrained workspaces. The root cause is architectural: current VLAs observe scenes through 2D images, generate action sequences through learned policies, and have no internal mechanism to determine whether the predicted end-effector trajectory will intersect obstacle surfaces.\n\nRecent work addresses this problem, but exclusively through mechanisms external to the VLA's internal representations. AEGIS~\\cite{hu2025vlsa} introduces a plug-in safety constraint layer based on Control Barrier Functions (CBFs): it identifies obstacles via open-set detection and depth estimation, then corrects unsafe actions after they have been generated, improving obstacle avoidance rate by 59.16\\% on SafeLIBERO. Notably, AEGIS requires no additional training and can be attached to any pretrained VLA, a practical advantage. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning; this approach, however, does not incorporate geometric information about the workspace and relies entirely on learned reward signals to encode safety. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that detects dangerous configurations and halts execution when predicted collision risk exceeds a threshold. These approaches share a common architectural pattern: the safety mechanism operates independently of the VLA's learned feature representations. The model first generates a trajectory without collision awareness, and a separate module then evaluates or corrects it. This reactive paradigm faces two fundamental limitations. In cluttered environments, the space available for post-hoc trajectory correction shrinks, and corrections may push the end-effector into other obstacles. Because the VLA itself never learns to represent collision geometry, it cannot anticipate obstacles during action generation and will repeatedly propose unsafe trajectories that require external intervention. A proactive alternative would embed collision-relevant geometric information directly into the VLA's forward pass, so that action tokens encode collision awareness from the point of generation.\n\nA parallel research direction has enriched VLA architectures with 3D spatial information. Numerous recent methods integrate depth maps, point clouds, or implicit 3D representations into VLA training or inference~\\cite{depthvla2025, li2025qdepth, li2025spatialforcing, 3dcavla2025, geoaware2025, spatialvla2025, gstvla2026, stemvla2026, stvla2026, evo02025, savla2026, augvla3d2026, evodepth2026}. These methods improve task success rate, viewpoint generalization, or grasping precision, but none targets collision avoidance as a design objective and none evaluates on collision-specific metrics. QDepth-VLA~\\cite{li2025qdepth}, the closest methodological precedent for auxiliary spatial supervision in VLAs, uses quantized depth prediction as a training-time auxiliary loss via a VQ-VAE decoder. Its decoder is decoupled from the action head: depth gradients flow into the backbone but do not explicitly modify the action token generation pathway. Depth is a 2.5D camera-frame representation that encodes the distance from each pixel to the camera. Deriving collision-relevant directions in the robot's workspace from depth gradients requires an implicit perspective-to-workspace coordinate transformation that depends on camera intrinsics and extrinsics, and occluded regions (where obstacles may be hidden behind the robot arm or other objects) produce no depth signal. The result is a clear gap between two active communities: spatially-aware VLAs do not address collision avoidance, and collision-safe VLAs do not internalize spatial geometry into the model's representations.\n\nWe propose ColliForce-VLA, which integrates a differentiable workspace Signed Distance Field (SDF) into the VLA forward pass for collision-aware action generation. Workspace SDF encodes, at each 3D point, the signed distance to the nearest obstacle surface; its spatial gradient points directly away from that surface in workspace coordinates. Unlike depth gradients that reside in camera frame, SDF gradients require no coordinate transformation and cover the full 3D workspace including occluded regions. SDF gradients indicate repulsion direction from obstacles by construction, and their continuous nature provides informative signals even at moderate distances from surfaces, in contrast to binary occupancy whose gradient is zero almost everywhere. ColliForce-VLA augments $\\pi_0$~\\cite{black2024pi0} with two lightweight modules attached to the action expert: an SDF Decoder (4-layer MLP, ${\\sim}$395K parameters) that predicts workspace SDF from the action expert's pooled suffix features, and an End-Effector (EE) Extractor (2-layer MLP, ${\\sim}$263K parameters) that predicts end-effector position from the same features. During training, for near-collision samples where predicted SDF at the end-effector is low, we compute $\\nabla_z \\Phi$, the gradient of predicted SDF with respect to the shared feature representation $z$, and perform gradient ascent ($z' = z + \\alpha \\cdot \\nabla_z \\Phi$) to push $z$ toward collision-free configurations. Both $z$ and $z'$ are projected into action token space, and a refinement loss trains the LoRA parameters (${\\sim}$33.5M) to directly produce the collision-corrected actions without requiring the gradient refinement step. The SDF supervisory signal is derived from known workspace geometry (obstacle meshes available in simulation), requiring no additional sensors beyond the standard visual input. At inference, only the base model with trained LoRA is active; neither auxiliary module nor gradient computation is required, so the method adds no extra modules to the inference pipeline. Unlike AEGIS~\\cite{hu2025vlsa}, which applies training-free post-hoc correction to already-generated trajectories, ColliForce-VLA internalizes collision geometry into the model's own parameters during training, enabling proactive avoidance at generation time with a potentially better CAR-TSR trade-off in cluttered settings. Unlike QDepth-VLA~\\cite{li2025qdepth}, whose depth decoder provides camera-frame auxiliary gradients to the backbone without explicitly modifying action tokens, our SDF gradient refinement operates in workspace frame and directly modulates the feature representations from which action tokens are decoded. The collision-avoidance capability is absorbed into the model's LoRA parameters during training and does not rely on any external safety layer at deployment.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We introduce a differentiable collision-aware mechanism for VLAs that integrates workspace SDF into the forward pass. SDF gradients in feature space ($\\nabla_z \\Phi$) guide action token generation toward collision-free configurations and provide a proactive alternative to post-hoc safety correction (Section~\\ref{sec:method}).\n    \\item We design a gradient-guided refinement training strategy where SDF gradients in feature space produce collision-corrected action targets, and LoRA parameters learn to reproduce these targets directly. The trained model requires no additional modules at inference (Section~\\ref{sec:training}).\n    \\item We conduct systematic experiments and ablation studies on the SafeLIBERO benchmark that separately quantify the contributions of SDF auxiliary supervision and SDF gradient-guided refinement to Collision Avoidance Rate (CAR) and Task Success Rate (TSR) \\textbf{[TODO: specific numbers pending experiments]} (Section~\\ref{sec:experiments}).\n\\end{itemize}",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

Now I have all the reference materials. Let me check the output directory exists and write the Method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "893b75aa-0d02-4a8d-ac2f-c73018828041",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hd8CkeLNvtztfcannHHSU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18028,
      "cache_read_input_tokens": 25320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18028
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

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01L6NudF5vskYSUyWnRHNPST`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check if drafts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "93c68692-18ea-4051-a4c5-b18fe609a54e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hd8CkeLNvtztfcannHHSU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18028,
      "cache_read_input_tokens": 25320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18028
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

### Tool result

_source line 16 · 2026-05-20T23:07:56.955Z_

<details><summary>↩ Tool result · `toolu_01L6NudF5vskYSUyWnRHNPST`</summary>

```text
introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "b0da040e-9121-4335-92b9-48d24196295f",
  "tool_use_result": {
    "stdout": "introduction.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 17_

Directory exists. Now I'll write the Method section LaTeX file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "8098b44a-7586-4813-ad66-b2f583cbb563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hx3Un6MKfYPBv3SSUkuoVg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 43348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
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

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Write · `toolu_014ZZGr1gcKKEPpAhcWZhBRj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/method.tex",
  "content": "\\section{Method}\\label{sec:method}\n\nWe present ColliForce-VLA, a framework that integrates differentiable workspace Signed Distance Fields (SDFs) into the forward pass of a pretrained Vision-Language-Action model to enable collision-aware action generation. The method requires no architectural modification to the VLA backbone and adds no extra modules at inference time. We describe the problem formulation (Section~\\ref{sec:problem}), the differentiable SDF integration (Section~\\ref{sec:sdf_integration}), the gradient-guided action refinement mechanism (Section~\\ref{sec:gradient_refinement}), the training protocol (Section~\\ref{sec:training}), and inference-time deployment (Section~\\ref{sec:inference}).\n\n\\subsection{Problem Formulation}\\label{sec:problem}\n\nWe consider a language-conditioned robotic manipulation setting where a Vision-Language-Action model $\\pi_\\theta$ generates an action trajectory $\\{a_t\\}_{t=1}^{H}$ with horizon $H = 50$, conditioned on visual observations $o$ and a language instruction $l$. Each action $a_t \\in \\mathbb{R}^7$ specifies the desired end-effector (EE) displacement in position ($\\Delta x, \\Delta y, \\Delta z$), orientation ($\\Delta q_1, \\Delta q_2, \\Delta q_3$), and gripper state.\n\nWe formalize collision avoidance through the workspace Signed Distance Field $\\Phi: \\mathbb{R}^3 \\to \\mathbb{R}$, where $\\Phi(\\mathbf{x}) > 0$ indicates free space, $\\Phi(\\mathbf{x}) = 0$ denotes the obstacle boundary, and $\\Phi(\\mathbf{x}) < 0$ indicates penetration. The objective is to learn a policy satisfying $\\Phi(\\mathrm{EE}(a_t)) > 0$ for all $t$ while preserving task success.\n\nOur base model is $\\pi_0$~\\cite{black2024pi0}, a 3.5B-parameter flow-matching VLA comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. The action expert produces a sequence of action tokens through an output projection $W_{\\mathrm{out}} \\in \\mathbb{R}^{1024 \\times 32}$ that maps from the expert's hidden dimension to the action token space.\n\n\\subsection{Differentiable SDF Integration}\\label{sec:sdf_integration}\n\nWe augment the VLA with two lightweight auxiliary modules that operate on the action expert's intermediate representations, together adding fewer than 660K parameters.\n\n\\paragraph{Feature extraction.} We capture the action expert's suffix output $\\mathbf{z} \\in \\mathbb{R}^{B \\times H \\times 1024}$, the tensor immediately preceding $W_{\\mathrm{out}}$, via a forward hook on \\texttt{action\\_out\\_proj}. Mean-pooling along the action horizon dimension yields a compact representation:\n\\begin{equation}\\label{eq:pooling}\n\\bar{\\mathbf{z}} = \\frac{1}{H} \\sum_{t=1}^{H} \\mathbf{z}_t \\in \\mathbb{R}^{1024}\n\\end{equation}\nthat summarizes the action expert's spatial understanding of the current scene.\n\n\\paragraph{SDF Decoder.} A 4-layer MLP $f_\\mathrm{SDF}$ predicts the signed distance value at arbitrary 3D query points given the pooled features:\n\\begin{equation}\\label{eq:sdf_decoder}\nf_\\mathrm{SDF}: (\\bar{\\mathbf{z}}, \\mathbf{x}) \\mapsto \\hat{\\Phi}(\\mathbf{x}), \\quad \\bar{\\mathbf{z}} \\in \\mathbb{R}^{1024},\\; \\mathbf{x} \\in \\mathbb{R}^3\n\\end{equation}\nThe architecture employs hidden dimension 256 with Softplus activation ($\\beta = 5$) and a skip connection that re-injects the query coordinates at layer 2:\n\\begin{align}\n\\mathbf{h}_0 &= \\sigma(\\mathbf{W}_0 [\\bar{\\mathbf{z}}; \\mathbf{x}] + \\mathbf{b}_0), \\quad \\mathbf{W}_0 \\in \\mathbb{R}^{256 \\times 1027} \\label{eq:sdf_layer0} \\\\\n\\mathbf{h}_1 &= \\sigma(\\mathbf{W}_1 \\mathbf{h}_0 + \\mathbf{b}_1), \\quad \\mathbf{W}_1 \\in \\mathbb{R}^{256 \\times 256} \\\\\n\\mathbf{h}_2 &= \\sigma(\\mathbf{W}_2 [\\mathbf{h}_1; \\mathbf{x}] + \\mathbf{b}_2), \\quad \\mathbf{W}_2 \\in \\mathbb{R}^{256 \\times 259} \\\\\n\\hat{\\Phi}(\\mathbf{x}) &= \\mathbf{W}_3 \\mathbf{h}_2 + \\mathbf{b}_3, \\quad \\mathbf{W}_3 \\in \\mathbb{R}^{1 \\times 256} \\label{eq:sdf_output}\n\\end{align}\nwhere $\\sigma(\\cdot) = \\mathrm{Softplus}_{\\beta=5}(\\cdot)$. The total parameter count is ${\\sim}$395K. Spatial gradients $\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\mathbf{x})$ are computed via \\texttt{torch.autograd.grad} with graph creation enabled during training, which is required for Eikonal regularization and the gradient-guided refinement in Section~\\ref{sec:gradient_refinement}.\n\n\\paragraph{End-Effector (EE) Extractor.} A 2-layer MLP $g_\\mathrm{EE}$ predicts the current EE position from the pooled features:\n\\begin{equation}\\label{eq:ee_extractor}\ng_\\mathrm{EE}: \\bar{\\mathbf{z}} \\mapsto \\hat{\\mathbf{p}}_\\mathrm{EE} \\in \\mathbb{R}^3, \\quad \\mathrm{Linear}(1024, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 3)\n\\end{equation}\nwith ${\\sim}$263K parameters. The EE prediction provides the query point for evaluating collision proximity, and its auxiliary loss encourages the action expert features to encode spatial position information.\n\n\\paragraph{Auxiliary losses.} The SDF decoder is trained with a clamped L1 loss and Eikonal regularization:\n\\begin{equation}\\label{eq:loss_sdf}\n\\mathcal{L}_\\mathrm{SDF} = \\frac{1}{N} \\sum_{i=1}^{N} \\left| \\mathrm{clamp}(\\hat{\\Phi}(\\mathbf{x}_i), \\pm\\delta) - \\mathrm{clamp}(\\Phi^*(\\mathbf{x}_i), \\pm\\delta) \\right| + \\lambda_\\mathrm{eik} \\frac{1}{N} \\sum_{i=1}^{N} \\left( \\|\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\mathbf{x}_i)\\|_2 - 1 \\right)^2\n\\end{equation}\nwhere $\\delta = 0.05$ is the clamping threshold, $\\lambda_\\mathrm{eik} = 0.1$, and $N = 64$ query points are sampled from the ground-truth SDF volume per step. Clamping focuses learning on the near-surface region most relevant for collision detection; the Eikonal term enforces the unit-gradient property of valid distance fields. The EE extractor is trained with MSE loss:\n\\begin{equation}\\label{eq:loss_ee}\n\\mathcal{L}_\\mathrm{EE} = \\|\\hat{\\mathbf{p}}_\\mathrm{EE} - \\mathbf{p}^*_\\mathrm{EE}\\|_2^2\n\\end{equation}\n\n\\subsection{SDF Gradient-Guided Action Refinement}\\label{sec:gradient_refinement}\n\nThe core contribution of ColliForce-VLA is a gradient-based mechanism that steers the action expert's representations away from collision-prone regions during training. Unlike post-hoc action filtering or external safety layers, this approach modifies the feature space directly, enabling the model to internalize collision avoidance behavior into its LoRA parameters.\n\n\\paragraph{Refinement procedure.} Given the captured suffix output $\\mathbf{z} \\in \\mathbb{R}^{B \\times H \\times 1024}$, the refinement proceeds in five steps:\n\n\\textbf{Step 1.} Predict EE position and evaluate the SDF:\n\\begin{equation}\n\\hat{\\mathbf{p}}_\\mathrm{EE} = g_\\mathrm{EE}(\\bar{\\mathbf{z}}), \\quad \\hat{d} = f_\\mathrm{SDF}(\\bar{\\mathbf{z}}, \\hat{\\mathbf{p}}_\\mathrm{EE})\n\\end{equation}\n\n\\textbf{Step 2.} Identify near-collision samples within the batch:\n\\begin{equation}\\label{eq:collision_set}\n\\mathcal{S} = \\{i : \\hat{\\Phi}(\\hat{\\mathbf{p}}_{\\mathrm{EE},i}) < m\\}, \\quad m = 0.01\n\\end{equation}\n\n\\textbf{Step 3.} For samples in $\\mathcal{S}$, compute the feature-space SDF gradient:\n\\begin{equation}\\label{eq:feature_grad}\n\\nabla_{\\mathbf{z}} \\hat{\\Phi} = \\frac{\\partial \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\mathrm{EE})}{\\partial \\mathbf{z}}\n\\end{equation}\nThis gradient captures how changes in the action expert's internal representation affect the predicted collision distance. It is distinct from the spatial gradient $\\nabla_{\\mathbf{x}} \\hat{\\Phi}$ used in Eikonal regularization: $\\nabla_{\\mathbf{z}} \\hat{\\Phi}$ operates in the 1024-dimensional feature space and encodes directions that move the entire action representation toward safety.\n\n\\textbf{Step 4.} Perform gradient ascent on the SDF value (toward higher, safer distances):\n\\begin{equation}\\label{eq:gradient_ascent}\n\\mathbf{z}' = \\mathbf{z} + \\alpha \\cdot \\mathrm{clip}(\\nabla_{\\mathbf{z}} \\hat{\\Phi}, \\gamma) \\odot \\mathbf{m}_\\mathcal{S}\n\\end{equation}\nwhere $\\alpha = 0.1$ is the step size, $\\mathrm{clip}(\\cdot, \\gamma)$ denotes per-sample L2 norm clipping with threshold $\\gamma = 1.0$ for gradient stability, and $\\mathbf{m}_\\mathcal{S}$ is a binary mask selecting only near-collision samples.\n\n\\textbf{Step 5.} Project both original and refined features through the action output head:\n\\begin{equation}\\label{eq:projection}\n\\mathbf{v}_t = W_\\mathrm{out}(\\mathbf{z}), \\quad \\mathbf{v}'_t = W_\\mathrm{out}(\\mathbf{z}')\n\\end{equation}\n\n\\paragraph{Refinement loss.} The model is trained to directly produce collision-corrected actions by minimizing the discrepancy between original and refined predictions on near-collision samples:\n\\begin{equation}\\label{eq:loss_refine}\n\\mathcal{L}_\\mathrm{refine} = \\frac{1}{|\\mathcal{S}|} \\sum_{i \\in \\mathcal{S}} \\|\\mathbf{v}_{t,i} - \\mathrm{sg}(\\mathbf{v}'_{t,i})\\|_2^2\n\\end{equation}\nwhere $\\mathrm{sg}(\\cdot)$ is the stop-gradient operator. The gradient flows only through $\\mathbf{v}_t \\to \\mathbf{z} \\to \\theta_\\mathrm{LoRA}$, training the LoRA adapters to anticipate and avoid collisions. The refined target $\\mathbf{v}'_t$ is detached and serves as a teacher signal that encodes collision-aware behavior. Because the student (the LoRA-adapted VLA) learns to replicate the refined actions directly, the SDF gradient computation is not required at inference time; the collision-avoidance capability is absorbed into the model parameters during training.\n\n\\subsection{Training Protocol}\\label{sec:training}\n\nWe adopt a two-phase training protocol that ensures SDF prediction accuracy before engaging gradient-guided refinement.\n\n\\paragraph{Phase 1: Auxiliary module warmup ($0 \\to 5\\mathrm{K}$ steps).} The entire backbone, including LoRA parameters, is frozen. Only the SDF decoder (${\\sim}$395K params) and EE extractor (${\\sim}$263K params) are trained on detached features ($\\bar{\\mathbf{z}}.\\mathrm{detach}()$) to avoid destabilizing the pretrained backbone. This phase establishes an accurate SDF predictor anchored to the backbone's current feature distribution.\n\n\\paragraph{Phase 2: Joint training ($5\\mathrm{K} \\to 30\\mathrm{K}$ steps).} LoRA parameters are unfrozen with a linear gradient warmup over 100 steps. We consider three training variants that differ only in their loss composition:\n\n\\textit{Baseline}: Standard LoRA fine-tuning with flow-matching action loss only:\n\\begin{equation}\n\\mathcal{L}_\\mathrm{base} = \\mathcal{L}_\\mathrm{action}\n\\end{equation}\n\n\\textit{A1 (SDF auxiliary supervision)}: Adds auxiliary losses without gradient-guided refinement:\n\\begin{equation}\\label{eq:loss_a1}\n\\mathcal{L}_\\mathrm{A1} = \\mathcal{L}_\\mathrm{action} + \\lambda_\\mathrm{SDF} \\cdot \\mathcal{L}_\\mathrm{SDF} + \\lambda_\\mathrm{EE} \\cdot \\mathcal{L}_\\mathrm{EE}\n\\end{equation}\nwith $\\lambda_\\mathrm{SDF} = 0.1$ and $\\lambda_\\mathrm{EE} = 0.01$. Gradients flow from the auxiliary losses through the pooled features into the LoRA adapters, encouraging the action expert to develop features that encode workspace geometry.\n\n\\textit{A3 (gradient-guided refinement)}: Extends A1 with the refinement loss:\n\\begin{equation}\\label{eq:loss_a3}\n\\mathcal{L}_\\mathrm{A3} = \\mathcal{L}_\\mathrm{action} + \\lambda_\\mathrm{SDF} \\cdot \\mathcal{L}_\\mathrm{SDF} + \\lambda_\\mathrm{EE} \\cdot \\mathcal{L}_\\mathrm{EE} + \\lambda_\\mathrm{refine} \\cdot \\mathcal{L}_\\mathrm{refine}\n\\end{equation}\nwith $\\lambda_\\mathrm{refine} = 0.1$. The refinement loss is computed only when near-collision samples exist in the batch ($|\\mathcal{S}| > 0$), adding zero overhead for collision-free steps.\n\n\\paragraph{LoRA configuration.} Adapters are injected into both the PaliGemma encoder (rank 16, $\\alpha = 16$) and the action expert (rank 32, $\\alpha = 32$), targeting attention projections ($W_q, W_k, W_v, W_o$) and MLP layers ($W_\\mathrm{gate}, W_\\mathrm{up}, W_\\mathrm{down}$). The total trainable LoRA parameter count is ${\\sim}$33.5M. All variants use AdamW optimizer with cosine learning rate decay from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, batch size 32, and train for 30K steps total.\n\n\\subsection{Inference}\\label{sec:inference}\n\nAt inference, only the base model with trained LoRA adapters is active. The standard forward pass generates actions through iterative flow-matching denoising; neither the auxiliary modules nor gradient computation is required. The LoRA parameters have internalized collision avoidance behavior during training, producing trajectories that maintain clearance from obstacles without additional computation.\n\nFor deployment scenarios with out-of-distribution obstacle configurations, ColliForce-VLA supports an optional workspace-frame SDF gradient correction as a complementary safety net. If the predicted SDF at the next EE position falls below the safety margin ($\\hat{\\Phi}(\\hat{\\mathbf{p}}_\\mathrm{next}) < m$), the position component of the action is corrected:\n\\begin{equation}\\label{eq:inference_correction}\na'_t[:3] = a_t[:3] + \\alpha \\cdot \\frac{\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\mathrm{next})}{\\|\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\mathrm{next})\\|_2}\n\\end{equation}\nThe L2-normalization bounds correction magnitude to $\\alpha$ regardless of gradient scale. This mechanism introduces zero additional latency when $\\hat{\\Phi} \\geq m$ and serves primarily as a safety net; the A3-trained model has already learned to avoid collisions and rarely triggers inference-time correction.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "a1edea74-8530-4f19-a46a-0d15dc7bfc77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hx3Un6MKfYPBv3SSUkuoVg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 43348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
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

### Tool result

_source line 19 · 2026-05-20T23:09:15.459Z_

<details><summary>↩ Tool result · `toolu_014ZZGr1gcKKEPpAhcWZhBRj`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "9b2440fa-efee-4276-973b-40733ae61546",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/method.tex",
    "content": "\\section{Method}\\label{sec:method}\n\nWe present ColliForce-VLA, a framework that integrates differentiable workspace Signed Distance Fields (SDFs) into the forward pass of a pretrained Vision-Language-Action model to enable collision-aware action generation. The method requires no architectural modification to the VLA backbone and adds no extra modules at inference time. We describe the problem formulation (Section~\\ref{sec:problem}), the differentiable SDF integration (Section~\\ref{sec:sdf_integration}), the gradient-guided action refinement mechanism (Section~\\ref{sec:gradient_refinement}), the training protocol (Section~\\ref{sec:training}), and inference-time deployment (Section~\\ref{sec:inference}).\n\n\\subsection{Problem Formulation}\\label{sec:problem}\n\nWe consider a language-conditioned robotic manipulation setting where a Vision-Language-Action model $\\pi_\\theta$ generates an action trajectory $\\{a_t\\}_{t=1}^{H}$ with horizon $H = 50$, conditioned on visual observations $o$ and a language instruction $l$. Each action $a_t \\in \\mathbb{R}^7$ specifies the desired end-effector (EE) displacement in position ($\\Delta x, \\Delta y, \\Delta z$), orientation ($\\Delta q_1, \\Delta q_2, \\Delta q_3$), and gripper state.\n\nWe formalize collision avoidance through the workspace Signed Distance Field $\\Phi: \\mathbb{R}^3 \\to \\mathbb{R}$, where $\\Phi(\\mathbf{x}) > 0$ indicates free space, $\\Phi(\\mathbf{x}) = 0$ denotes the obstacle boundary, and $\\Phi(\\mathbf{x}) < 0$ indicates penetration. The objective is to learn a policy satisfying $\\Phi(\\mathrm{EE}(a_t)) > 0$ for all $t$ while preserving task success.\n\nOur base model is $\\pi_0$~\\cite{black2024pi0}, a 3.5B-parameter flow-matching VLA comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. The action expert produces a sequence of action tokens through an output projection $W_{\\mathrm{out}} \\in \\mathbb{R}^{1024 \\times 32}$ that maps from the expert's hidden dimension to the action token space.\n\n\\subsection{Differentiable SDF Integration}\\label{sec:sdf_integration}\n\nWe augment the VLA with two lightweight auxiliary modules that operate on the action expert's intermediate representations, together adding fewer than 660K parameters.\n\n\\paragraph{Feature extraction.} We capture the action expert's suffix output $\\mathbf{z} \\in \\mathbb{R}^{B \\times H \\times 1024}$, the tensor immediately preceding $W_{\\mathrm{out}}$, via a forward hook on \\texttt{action\\_out\\_proj}. Mean-pooling along the action horizon dimension yields a compact representation:\n\\begin{equation}\\label{eq:pooling}\n\\bar{\\mathbf{z}} = \\frac{1}{H} \\sum_{t=1}^{H} \\mathbf{z}_t \\in \\mathbb{R}^{1024}\n\\end{equation}\nthat summarizes the action expert's spatial understanding of the current scene.\n\n\\paragraph{SDF Decoder.} A 4-layer MLP $f_\\mathrm{SDF}$ predicts the signed distance value at arbitrary 3D query points given the pooled features:\n\\begin{equation}\\label{eq:sdf_decoder}\nf_\\mathrm{SDF}: (\\bar{\\mathbf{z}}, \\mathbf{x}) \\mapsto \\hat{\\Phi}(\\mathbf{x}), \\quad \\bar{\\mathbf{z}} \\in \\mathbb{R}^{1024},\\; \\mathbf{x} \\in \\mathbb{R}^3\n\\end{equation}\nThe architecture employs hidden dimension 256 with Softplus activation ($\\beta = 5$) and a skip connection that re-injects the query coordinates at layer 2:\n\\begin{align}\n\\mathbf{h}_0 &= \\sigma(\\mathbf{W}_0 [\\bar{\\mathbf{z}}; \\mathbf{x}] + \\mathbf{b}_0), \\quad \\mathbf{W}_0 \\in \\mathbb{R}^{256 \\times 1027} \\label{eq:sdf_layer0} \\\\\n\\mathbf{h}_1 &= \\sigma(\\mathbf{W}_1 \\mathbf{h}_0 + \\mathbf{b}_1), \\quad \\mathbf{W}_1 \\in \\mathbb{R}^{256 \\times 256} \\\\\n\\mathbf{h}_2 &= \\sigma(\\mathbf{W}_2 [\\mathbf{h}_1; \\mathbf{x}] + \\mathbf{b}_2), \\quad \\mathbf{W}_2 \\in \\mathbb{R}^{256 \\times 259} \\\\\n\\hat{\\Phi}(\\mathbf{x}) &= \\mathbf{W}_3 \\mathbf{h}_2 + \\mathbf{b}_3, \\quad \\mathbf{W}_3 \\in \\mathbb{R}^{1 \\times 256} \\label{eq:sdf_output}\n\\end{align}\nwhere $\\sigma(\\cdot) = \\mathrm{Softplus}_{\\beta=5}(\\cdot)$. The total parameter count is ${\\sim}$395K. Spatial gradients $\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\mathbf{x})$ are computed via \\texttt{torch.autograd.grad} with graph creation enabled during training, which is required for Eikonal regularization and the gradient-guided refinement in Section~\\ref{sec:gradient_refinement}.\n\n\\paragraph{End-Effector (EE) Extractor.} A 2-layer MLP $g_\\mathrm{EE}$ predicts the current EE position from the pooled features:\n\\begin{equation}\\label{eq:ee_extractor}\ng_\\mathrm{EE}: \\bar{\\mathbf{z}} \\mapsto \\hat{\\mathbf{p}}_\\mathrm{EE} \\in \\mathbb{R}^3, \\quad \\mathrm{Linear}(1024, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 3)\n\\end{equation}\nwith ${\\sim}$263K parameters. The EE prediction provides the query point for evaluating collision proximity, and its auxiliary loss encourages the action expert features to encode spatial position information.\n\n\\paragraph{Auxiliary losses.} The SDF decoder is trained with a clamped L1 loss and Eikonal regularization:\n\\begin{equation}\\label{eq:loss_sdf}\n\\mathcal{L}_\\mathrm{SDF} = \\frac{1}{N} \\sum_{i=1}^{N} \\left| \\mathrm{clamp}(\\hat{\\Phi}(\\mathbf{x}_i), \\pm\\delta) - \\mathrm{clamp}(\\Phi^*(\\mathbf{x}_i), \\pm\\delta) \\right| + \\lambda_\\mathrm{eik} \\frac{1}{N} \\sum_{i=1}^{N} \\left( \\|\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\mathbf{x}_i)\\|_2 - 1 \\right)^2\n\\end{equation}\nwhere $\\delta = 0.05$ is the clamping threshold, $\\lambda_\\mathrm{eik} = 0.1$, and $N = 64$ query points are sampled from the ground-truth SDF volume per step. Clamping focuses learning on the near-surface region most relevant for collision detection; the Eikonal term enforces the unit-gradient property of valid distance fields. The EE extractor is trained with MSE loss:\n\\begin{equation}\\label{eq:loss_ee}\n\\mathcal{L}_\\mathrm{EE} = \\|\\hat{\\mathbf{p}}_\\mathrm{EE} - \\mathbf{p}^*_\\mathrm{EE}\\|_2^2\n\\end{equation}\n\n\\subsection{SDF Gradient-Guided Action Refinement}\\label{sec:gradient_refinement}\n\nThe core contribution of ColliForce-VLA is a gradient-based mechanism that steers the action expert's representations away from collision-prone regions during training. Unlike post-hoc action filtering or external safety layers, this approach modifies the feature space directly, enabling the model to internalize collision avoidance behavior into its LoRA parameters.\n\n\\paragraph{Refinement procedure.} Given the captured suffix output $\\mathbf{z} \\in \\mathbb{R}^{B \\times H \\times 1024}$, the refinement proceeds in five steps:\n\n\\textbf{Step 1.} Predict EE position and evaluate the SDF:\n\\begin{equation}\n\\hat{\\mathbf{p}}_\\mathrm{EE} = g_\\mathrm{EE}(\\bar{\\mathbf{z}}), \\quad \\hat{d} = f_\\mathrm{SDF}(\\bar{\\mathbf{z}}, \\hat{\\mathbf{p}}_\\mathrm{EE})\n\\end{equation}\n\n\\textbf{Step 2.} Identify near-collision samples within the batch:\n\\begin{equation}\\label{eq:collision_set}\n\\mathcal{S} = \\{i : \\hat{\\Phi}(\\hat{\\mathbf{p}}_{\\mathrm{EE},i}) < m\\}, \\quad m = 0.01\n\\end{equation}\n\n\\textbf{Step 3.} For samples in $\\mathcal{S}$, compute the feature-space SDF gradient:\n\\begin{equation}\\label{eq:feature_grad}\n\\nabla_{\\mathbf{z}} \\hat{\\Phi} = \\frac{\\partial \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\mathrm{EE})}{\\partial \\mathbf{z}}\n\\end{equation}\nThis gradient captures how changes in the action expert's internal representation affect the predicted collision distance. It is distinct from the spatial gradient $\\nabla_{\\mathbf{x}} \\hat{\\Phi}$ used in Eikonal regularization: $\\nabla_{\\mathbf{z}} \\hat{\\Phi}$ operates in the 1024-dimensional feature space and encodes directions that move the entire action representation toward safety.\n\n\\textbf{Step 4.} Perform gradient ascent on the SDF value (toward higher, safer distances):\n\\begin{equation}\\label{eq:gradient_ascent}\n\\mathbf{z}' = \\mathbf{z} + \\alpha \\cdot \\mathrm{clip}(\\nabla_{\\mathbf{z}} \\hat{\\Phi}, \\gamma) \\odot \\mathbf{m}_\\mathcal{S}\n\\end{equation}\nwhere $\\alpha = 0.1$ is the step size, $\\mathrm{clip}(\\cdot, \\gamma)$ denotes per-sample L2 norm clipping with threshold $\\gamma = 1.0$ for gradient stability, and $\\mathbf{m}_\\mathcal{S}$ is a binary mask selecting only near-collision samples.\n\n\\textbf{Step 5.} Project both original and refined features through the action output head:\n\\begin{equation}\\label{eq:projection}\n\\mathbf{v}_t = W_\\mathrm{out}(\\mathbf{z}), \\quad \\mathbf{v}'_t = W_\\mathrm{out}(\\mathbf{z}')\n\\end{equation}\n\n\\paragraph{Refinement loss.} The model is trained to directly produce collision-corrected actions by minimizing the discrepancy between original and refined predictions on near-collision samples:\n\\begin{equation}\\label{eq:loss_refine}\n\\mathcal{L}_\\mathrm{refine} = \\frac{1}{|\\mathcal{S}|} \\sum_{i \\in \\mathcal{S}} \\|\\mathbf{v}_{t,i} - \\mathrm{sg}(\\mathbf{v}'_{t,i})\\|_2^2\n\\end{equation}\nwhere $\\mathrm{sg}(\\cdot)$ is the stop-gradient operator. The gradient flows only through $\\mathbf{v}_t \\to \\mathbf{z} \\to \\theta_\\mathrm{LoRA}$, training the LoRA adapters to anticipate and avoid collisions. The refined target $\\mathbf{v}'_t$ is detached and serves as a teacher signal that encodes collision-aware behavior. Because the student (the LoRA-adapted VLA) learns to replicate the refined actions directly, the SDF gradient computation is not required at inference time; the collision-avoidance capability is absorbed into the model parameters during training.\n\n\\subsection{Training Protocol}\\label{sec:training}\n\nWe adopt a two-phase training protocol that ensures SDF prediction accuracy before engaging gradient-guided refinement.\n\n\\paragraph{Phase 1: Auxiliary module warmup ($0 \\to 5\\mathrm{K}$ steps).} The entire backbone, including LoRA parameters, is frozen. Only the SDF decoder (${\\sim}$395K params) and EE extractor (${\\sim}$263K params) are trained on detached features ($\\bar{\\mathbf{z}}.\\mathrm{detach}()$) to avoid destabilizing the pretrained backbone. This phase establishes an accurate SDF predictor anchored to the backbone's current feature distribution.\n\n\\paragraph{Phase 2: Joint training ($5\\mathrm{K} \\to 30\\mathrm{K}$ steps).} LoRA parameters are unfrozen with a linear gradient warmup over 100 steps. We consider three training variants that differ only in their loss composition:\n\n\\textit{Baseline}: Standard LoRA fine-tuning with flow-matching action loss only:\n\\begin{equation}\n\\mathcal{L}_\\mathrm{base} = \\mathcal{L}_\\mathrm{action}\n\\end{equation}\n\n\\textit{A1 (SDF auxiliary supervision)}: Adds auxiliary losses without gradient-guided refinement:\n\\begin{equation}\\label{eq:loss_a1}\n\\mathcal{L}_\\mathrm{A1} = \\mathcal{L}_\\mathrm{action} + \\lambda_\\mathrm{SDF} \\cdot \\mathcal{L}_\\mathrm{SDF} + \\lambda_\\mathrm{EE} \\cdot \\mathcal{L}_\\mathrm{EE}\n\\end{equation}\nwith $\\lambda_\\mathrm{SDF} = 0.1$ and $\\lambda_\\mathrm{EE} = 0.01$. Gradients flow from the auxiliary losses through the pooled features into the LoRA adapters, encouraging the action expert to develop features that encode workspace geometry.\n\n\\textit{A3 (gradient-guided refinement)}: Extends A1 with the refinement loss:\n\\begin{equation}\\label{eq:loss_a3}\n\\mathcal{L}_\\mathrm{A3} = \\mathcal{L}_\\mathrm{action} + \\lambda_\\mathrm{SDF} \\cdot \\mathcal{L}_\\mathrm{SDF} + \\lambda_\\mathrm{EE} \\cdot \\mathcal{L}_\\mathrm{EE} + \\lambda_\\mathrm{refine} \\cdot \\mathcal{L}_\\mathrm{refine}\n\\end{equation}\nwith $\\lambda_\\mathrm{refine} = 0.1$. The refinement loss is computed only when near-collision samples exist in the batch ($|\\mathcal{S}| > 0$), adding zero overhead for collision-free steps.\n\n\\paragraph{LoRA configuration.} Adapters are injected into both the PaliGemma encoder (rank 16, $\\alpha = 16$) and the action expert (rank 32, $\\alpha = 32$), targeting attention projections ($W_q, W_k, W_v, W_o$) and MLP layers ($W_\\mathrm{gate}, W_\\mathrm{up}, W_\\mathrm{down}$). The total trainable LoRA parameter count is ${\\sim}$33.5M. All variants use AdamW optimizer with cosine learning rate decay from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, batch size 32, and train for 30K steps total.\n\n\\subsection{Inference}\\label{sec:inference}\n\nAt inference, only the base model with trained LoRA adapters is active. The standard forward pass generates actions through iterative flow-matching denoising; neither the auxiliary modules nor gradient computation is required. The LoRA parameters have internalized collision avoidance behavior during training, producing trajectories that maintain clearance from obstacles without additional computation.\n\nFor deployment scenarios with out-of-distribution obstacle configurations, ColliForce-VLA supports an optional workspace-frame SDF gradient correction as a complementary safety net. If the predicted SDF at the next EE position falls below the safety margin ($\\hat{\\Phi}(\\hat{\\mathbf{p}}_\\mathrm{next}) < m$), the position component of the action is corrected:\n\\begin{equation}\\label{eq:inference_correction}\na'_t[:3] = a_t[:3] + \\alpha \\cdot \\frac{\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\mathrm{next})}{\\|\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\hat{\\mathbf{p}}_\\mathrm{next})\\|_2}\n\\end{equation}\nThe L2-normalization bounds correction magnitude to $\\alpha$ regardless of gradient scale. This mechanism introduces zero additional latency when $\\hat{\\Phi} \\geq m$ and serves primarily as a safety net; the A3-trained model has already learned to avoid collisions and rarely triggers inference-time correction.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 20_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "db45275c-f7f3-4b99-a1f8-ee4b341b4040",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrK29g9JYiLkLwgXxWMPyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 43508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4749
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

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JyhPpKJhnPD8uzhQFzb7gb`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "3933a938-bfb2-411c-92a5-9a428deb7788",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrK29g9JYiLkLwgXxWMPyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4749,
      "cache_read_input_tokens": 43508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4749
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

### Tool result

_source line 22 · 2026-05-20T23:09:25.237Z_

<details><summary>↩ Tool result · `toolu_01JyhPpKJhnPD8uzhQFzb7gb`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "b8e896a3-1d90-4f4e-b641-b05480e71274",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_0157mbQpxfiLjhoAPHSyMcW6`</summary>

```json
{
  "name": "method-section-draft",
  "type": "paper",
  "description": "ColliForce-VLA Method section LaTeX draft (~1500 words). Covers Problem Formulation, Differentiable SDF Integration, Gradient-Guided Action Refinement, Training Protocol, and Inference.",
  "project": "diff_collision_sdf",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/drafts/method.tex",
  "tags": [
    "paper",
    "method",
    "latex",
    "draft"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "8f61ea42-7975-41a0-b939-f4b5e37d45be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHpQE9gL9kmbwZ2Tf7xz9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 48257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
      },
      "output_tokens": 51,
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

_source line 24 · 2026-05-20T23:09:29.937Z_

<details><summary>↩ Tool result · `toolu_0157mbQpxfiLjhoAPHSyMcW6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_5f2281\", \"name\": \"method-section-draft\", \"type\": \"paper\", \"description\": \"ColliForce-VLA Method section LaTeX draft (~1500 words). Covers Problem Formulation, Differentiable SDF Integration, Gradient-Guided Action Refinement, Training Protocol, and Inference.\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/paper/method.tex\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T23:09:29.913627+00:00\", \"tags\": [\"paper\", \"method\", \"latex\", \"draft\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "56bac204-8f2d-46a2-ad73-c72cebbebeff",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_5f2281\\\", \\\"name\\\": \\\"method-section-draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"ColliForce-VLA Method section LaTeX draft (~1500 words). Covers Problem Formulation, Differentiable SDF Integration, Gradient-Guided Action Refinement, Training Protocol, and Inference.\\\", \\\"path\\\": \\\"projects/diff_collision_sdf/artifacts/_project/paper/method.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"diff_collision_sdf\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T23:09:29.913627+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"method\\\", \\\"latex\\\", \\\"draft\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_5f2281\", \"name\": \"method-section-draft\", \"type\": \"paper\", \"description\": \"ColliForce-VLA Method section LaTeX draft (~1500 words). Covers Problem Formulation, Differentiable SDF Integration, Gradient-Guided Action Refinement, Training Protocol, and Inference.\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/paper/method.tex\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T23:09:29.913627+00:00\", \"tags\": [\"paper\", \"method\", \"latex\", \"draft\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

Method section 已写入 `artifacts/drafts/method.tex`，同时注册到 artifact manifest。

结构概览：
- **§3.1 Problem Formulation** (~180 words): 定义 $\pi_\theta$、$a_t \in \mathbb{R}^7$、$H=50$、SDF $\Phi(\mathbf{x})$、$\pi_0$ 架构、$W_\mathrm{out}$
- **§3.2 Differentiable SDF Integration** (~420 words): Feature extraction (mean-pooled $\bar{\mathbf{z}}$)、SDF Decoder 四层 MLP 完整公式与维度、EE Extractor、clamped L1 + Eikonal loss ($\delta=0.05, \lambda_\mathrm{eik}=0.1, N=64$)
- **§3.3 SDF Gradient-Guided Action Refinement** (~400 words): 五步 refinement procedure 含公式、$\nabla_\mathbf{z}\Phi$ 与 $\nabla_\mathbf{x}\Phi$ 的区分、refinement loss 含 stop-gradient 机制解释
- **§3.4 Training Protocol** (~330 words): Phase 1 (0→5K frozen warmup) + Phase 2 (5K→30K joint)、三个变体 (Baseline/A1/A3) 完整 loss 公式、LoRA 配置 (encoder r=16, expert r=32, ~33.5M params)、优化器超参
- **§3.5 Inference** (~120 words): 标准 forward pass + 可选 workspace-frame SDF gradient correction

所有数字与 method_draft.md 和 Introduction 一致，无 em-dash，无 -ing 结尾，无黑名单词汇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "uuid": "fce33223-064e-48ad-b9e5-e9e6af45d1d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Su7nNTJH2CzmC5qhtUe6ti",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 49079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 543
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

_source line 26_

Method section 已写入 `artifacts/drafts/method.tex`，同时注册到 artifact manifest。

结构概览：
- **§3.1 Problem Formulation** (~180 words): 定义 $\pi_\theta$、$a_t \in \mathbb{R}^7$、$H=50$、SDF $\Phi(\mathbf{x})$、$\pi_0$ 架构、$W_\mathrm{out}$
- **§3.2 Differentiable SDF Integration** (~420 words): Feature extraction (mean-pooled $\bar{\mathbf{z}}$)、SDF Decoder 四层 MLP 完整公式与维度、EE Extractor、clamped L1 + Eikonal loss ($\delta=0.05, \lambda_\mathrm{eik}=0.1, N=64$)
- **§3.3 SDF Gradient-Guided Action Refinement** (~400 words): 五步 refinement procedure 含公式、$\nabla_\mathbf{z}\Phi$ 与 $\nabla_\mathbf{x}\Phi$ 的区分、refinement loss 含 stop-gradient 机制解释
- **§3.4 Training Protocol** (~330 words): Phase 1 (0→5K frozen warmup) + Phase 2 (5K→30K joint)、三个变体 (Baseline/A1/A3) 完整 loss 公式、LoRA 配置 (encoder r=16, expert r=32, ~33.5M params)、优化器超参
- **§3.5 Inference** (~120 words): 标准 forward pass + 可选 workspace-frame SDF gradient correction

所有数字与 method_draft.md 和 Introduction 一致，无 em-dash，无 -ing 结尾，无黑名单词汇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 118736,
  "duration_api_ms": 119852,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "70ca29b4-6c7b-417a-8cf3-68330139ebc5",
  "total_cost_usd": 0.5034872499999999,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 38175,
    "cache_read_input_tokens": 220959,
    "output_tokens": 6059,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38175,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 496,
        "cache_read_input_tokens": 49079,
        "cache_creation_input_tokens": 543,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 543
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2794,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002894,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 6059,
      "cacheReadInputTokens": 220959,
      "cacheCreationInputTokens": 38175,
      "webSearchRequests": 0,
      "costUSD": 0.50059325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "da8207d5-bf3a-4323-ad11-b5f53d9ec056"
}
```

</details>

---
