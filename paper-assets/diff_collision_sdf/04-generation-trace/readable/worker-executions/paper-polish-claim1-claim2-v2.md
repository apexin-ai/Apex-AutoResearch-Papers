# paper polish claim1 claim2 v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_paper_polish_claim1_claim2_v2_20260526T092811.log`
- **Structured JSON:** [`2efde4e5badcae42e5b4.json`](../../sessions/2e/2efde4e5badcae42e5b4.json)

## Before a recorded user message

67 recorded events

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
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "30ae7a6f-1153-4807-a79d-9e598e3e3a47",
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
    "resetsAt": 1779801600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c18ff795-2b2a-4be6-b2ff-0124f20b035c",
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401"
}
```

---

### Assistant

_source line 4_

I'll start by reading the writing norms skill and all five files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "58dda62a-2f14-4f2f-b490-a7d368ece9a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ299YchxUJ9ndqzvrbNPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01Cmhn3Q3cYx1pPwW5ZvgpJv`</summary>

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
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "ae851aca-ddb1-4140-a81f-ad54914f98ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ299YchxUJ9ndqzvrbNPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-26T09:28:21.095Z_

<details><summary>↩ Tool result · `toolu_01Cmhn3Q3cYx1pPwW5ZvgpJv`</summary>

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
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "cd2a1f7b-870c-4038-98b7-95ffe21d8f1c",
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

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01C3SWi5t1ZnhgNGZVxUmnZZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "299134cb-1ee3-43b3-973a-ca26bf762325",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ299YchxUJ9ndqzvrbNPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-26T09:28:21.814Z_

<details><summary>↩ Tool result · `toolu_01C3SWi5t1ZnhgNGZVxUmnZZ`</summary>

```text
1	\subsection{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	At first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\% across 800 evaluation episodes on the SafeLIBERO benchmark~\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\%) exhibit a maximum displacement below 1\,$\mu$m, and another 188 episodes (25.7\%) remain below 0.1\,mm. Only 3 episodes (0.4\%) show displacement above the 0.1\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\sim}$5\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved.
4	
5	We define a safe episode as \emph{fake safe} when the maximum end-effector displacement stays below a threshold $\tau_d = 0.1$\,mm, the criterion used by the displacement-filtered CAR (Eq.~\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}
10	\label{tab:fake_safety}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{lccccc}
14	\toprule
15	Method & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) \\
16	\midrule
17	A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\dagger$ \\
18	LoRA baseline  & 82.0 & 0.0 & 99.4 & $\approx$\,1 / 164 & $\approx$\,0 \\
19	Pi0.5 & 28.5 & 71.5 & 0.0 & 57 / 57 & 28.5 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{2pt}
23	{\footnotesize $^\dagger$ Denominator $< 5$; statistically unreliable. Pi0.5 row from single-seed re-evaluation (seed~7, 200 episodes) with EE displacement recording; all safe episodes exceed 288\,mm displacement.}
24	\end{table}
25	
26	This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\% with a Task Success Rate (TSR) of 0\%. Among its 164 safe episodes, 99.4\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\sim}$3B$\to$${\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\,$\pm$\,1.6\% and a TSR of 74.7\,$\pm$\,1.5\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\,mm, yielding a fake safe rate of 0\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\text{f}$ equals its raw CAR (28.5\%), because no episodes are filtered by the displacement threshold.
27	For the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.
28	
29	These observations motivate the displacement-filtered CAR (CAR$_\text{f}$) defined in Eq.~\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.
30	
31	The threshold $\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\,mm, three orders of magnitude above $\tau_d = 0.1$\,mm. Any threshold in $[2, 200]$\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\ref{sec:appendix_threshold}.
32	
33	For A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\text{f}$ is similarly near zero. Pi0.5 presents the opposite extreme: every episode exceeds the displacement threshold, so CAR$_\text{f}$ equals raw CAR (28.5\%). The gap between raw CAR and CAR$_\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\% CAR but its CAR$_\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.
34	
35	The practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\text{f}$.
36	
37	\paragraph{Capability-safety observation.}
38	The fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\% of their safe episodes classified as fake safe; we term this the \emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\% across seeds), low CAR (25--28\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.
39	
40	This spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "c0f68a30-c0e2-404b-9112-19765d3fa3c0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
      "content": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 & 28.5 & 71.5 & 0.0 & 57 / 57 & 28.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. Pi0.5 row from single-seed re-evaluation (seed~7, 200 episodes) with EE displacement recording; all safe episodes exceed 288\\,mm displacement.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\\,mm, yielding a fake safe rate of 0\\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\\text{f}$ equals its raw CAR (28.5\\%), because no episodes are filtered by the displacement threshold.\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero. Pi0.5 presents the opposite extreme: every episode exceeds the displacement threshold, so CAR$_\\text{f}$ equals raw CAR (28.5\\%). The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01XZtDNMtvbEvgVoESN3FEjm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "57ce1d8c-982b-4336-8fb9-ce97bf871d8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ299YchxUJ9ndqzvrbNPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 2,
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

_source line 10 · 2026-05-26T09:28:22.196Z_

<details><summary>↩ Tool result · `toolu_01XZtDNMtvbEvgVoESN3FEjm`</summary>

```text
1	\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	The analysis in Section~\ref{sec:fake_safety} identifies action collapse and fake safety as pervasive problems, but leaves open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Table~\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\%) falls 5.1 percentage points below the LoRA baseline (82.0\%) and 6.1 points below Full-FT (83.0\%). The adaptive and fixed-step variants perform worse still, at 75.0\% and 73.1\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance. The persistence of action collapse under gradient correction is expected: refinement can redirect existing motion away from obstacles, but cannot generate motion from a policy that has collapsed into inaction. The gradient operates on a trajectory that is already near-zero; perturbing near-zero displacement produces near-zero displacement in a different direction, not a viable collision-free path.
28	
29	Figure~\ref{fig:oracle_bar} visualizes this aggregate gap. The per-task breakdown reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive reaches 55.0\% and Oracle-feature reaches 47.5\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\% to 82.5\% on task~0 and from 98.0\% to 77.5\% on task~2. The refinement gradient pushes the end-effector away from the obstacle surface but perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.
30	
31	This failure mode is structural. The SDF refinement paradigm as formulated in prior work~\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution.
32	
33	The feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.
34	
35	The A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.
36	
37	These results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip. Section~\ref{sec:avoidance_source} investigates the source of collision avoidance in fine-tuned models and the role of geometric supervision.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "17a02000-cbe6-4c3b-a69b-babd72226c84",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex",
      "content": "\\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\n\nThe analysis in Section~\\ref{sec:fake_safety} identifies action collapse and fake safety as pervasive problems, but leaves open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\\%, Full-FT 83.0\\%), and fake safe rates remain above 96\\%.}\n\\label{tab:oracle}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & TSR (\\%) & CAR (\\%) & Fake Safe (\\%) & Refines/ep \\\\\n\\midrule\nLoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\\\\nFull-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\\\\n\\midrule\nOracle-adaptive (GT, dyn.\\ $\\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\\\\nOracle-fixed (GT, $\\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\\\\nOracle-feature (GT, feat.\\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\\\\n\\midrule\nA3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\\%) falls 5.1 percentage points below the LoRA baseline (82.0\\%) and 6.1 points below Full-FT (83.0\\%). The adaptive and fixed-step variants perform worse still, at 75.0\\% and 73.1\\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance. The persistence of action collapse under gradient correction is expected: refinement can redirect existing motion away from obstacles, but cannot generate motion from a policy that has collapsed into inaction. The gradient operates on a trajectory that is already near-zero; perturbing near-zero displacement produces near-zero displacement in a different direction, not a viable collision-free path.\n\nFigure~\\ref{fig:oracle_bar} visualizes this aggregate gap. The per-task breakdown reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive reaches 55.0\\% and Oracle-feature reaches 47.5\\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\\% to 82.5\\% on task~0 and from 98.0\\% to 77.5\\% on task~2. The refinement gradient pushes the end-effector away from the obstacle surface but perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.\n\nThis failure mode is structural. The SDF refinement paradigm as formulated in prior work~\\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution.\n\nThe feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.\n\nThe A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.\n\nThese results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip. Section~\\ref{sec:avoidance_source} investigates the source of collision avoidance in fine-tuned models and the role of geometric supervision.\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_0128NTg1EWzNGZo8eTWi1XjC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "c8bfecfc-171e-47f4-b6da-9cb8f98ecaa0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ299YchxUJ9ndqzvrbNPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 2,
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

_source line 12 · 2026-05-26T09:28:22.790Z_

<details><summary>↩ Tool result · `toolu_0128NTg1EWzNGZo8eTWi1XjC`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\ref{sec:avoidance_source}).
4	
5	\paragraph{Limitations.}
6	The empirical scope of this study is bounded in several respects. All experiments use the \texttt{object\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \texttt{spatial\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\% CAR despite substantial end-effector displacement (0.29\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges---dominated by full-body collisions---beyond those captured by the \texttt{object\_pudding} benchmark. The EE-only SDF oracle (Section~\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\tau_d = 0.1$\,mm is empirically robust across four orders of magnitude (Appendix~\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\% baseline to $<$7\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.
7	
8	\paragraph{Future work.}
9	Five directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.
10	
11	\paragraph{Broader impact.}
12	Metric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "1b8470f6-70b8-4a07-ac77-eb557ba163c8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges---dominated by full-body collisions---beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.\n\n\\paragraph{Future work.}\nFive directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.\n\n\\paragraph{Broader impact.}\nMetric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01WoUKff4NjUEGAcczb8EVcs`</summary>

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
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "dd61255f-8cbf-4c4d-aa72-311adbf61fea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ299YchxUJ9ndqzvrbNPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 2,
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

_source line 14 · 2026-05-26T09:28:23.108Z_

<details><summary>↩ Tool result · `toolu_01WoUKff4NjUEGAcczb8EVcs`</summary>

```text
1	\section{Introduction}
2	
3	A model that reports 91.5\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.
4	
5	Vision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.
6	
7	Several recent methods target collision avoidance in VLAs. AEGIS~\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\% across SafeLIBERO scenarios without additional training. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.
8	
9	For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\% exhibit a maximum displacement below 0.1\,mm, and obstacle displacement remains below 5\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\% CAR with 99.4\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\,mm), yielding a fake safe rate of 0\%.
10	
11	We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\,mm, any $\tau_d$ in $[2, 200]$\,mm yields identical filtering.
12	
13	The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\,$\pm$\,1.5\% but a CAR of only 26.8\,$\pm$\,1.6\%, while Pi0-based methods report CAR of 82--91.5\% alongside TSR $\leq$ 0.5\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \emph{lower} CAR than unrefined baselines (best oracle: 76.9\% vs.\ LoRA baseline: 82.0\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\% with 0\% frozen rate but suffers catastrophic TSR collapse to 6.3\%; SDF-augmented variants ($\lambda \in \{0.005, 0.01\}$) show comparable CAR (50.5--52.8\%) with similar TSR collapse (6.8\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\% with CAR of 56.5--57.5\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.
14	
15	Our contributions are as follows:
16	\begin{itemize}
17	    \item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\ref{sec:fake_safety}).
18	    \item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\ref{sec:ee_only}).
19	    \item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\% (TSR 6.3\%), comparable to SDF-augmented variants (CAR 50.5--52.8\%, TSR 6.8\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\% before degrading to $<$7\% at 30K (Section~\ref{sec:avoidance_source}).
20	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "b6a3209c-5cde-40bf-a579-f537aeaa0170",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_011AJiFky68vP1T4ruHXFmdc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "b61f96f8-6429-40e9-b525-fee4e7da6316",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZ299YchxUJ9ndqzvrbNPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 2,
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

_source line 16 · 2026-05-26T09:28:23.410Z_

<details><summary>↩ Tool result · `toolu_011AJiFky68vP1T4ruHXFmdc`</summary>

```text
1	\begin{abstract}
2	Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\% CAR alongside 0\% Task Success Rate (TSR), yet 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\% CAR with 99.4\% of safe episodes below the same threshold, while Pi0.5, which achieves 74.7\% TSR, exhibits 0\% fake safety---all of its safe episodes reflect genuine avoidance with end-effector displacements exceeding 288\,mm. We propose a corrective metric, displacement-filtered CAR (CAR$_\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\sim}$55\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\% to $<$7\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "aa7ff945-d79b-4d95-a5f1-540b6a16133f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nRecent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, while Pi0.5, which achieves 74.7\\% TSR, exhibits 0\\% fake safety---all of its safe episodes reflect genuine avoidance with end-effector displacements exceeding 288\\,mm. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\\sim}$55\\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\\% to $<$7\\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files and the writing norms. Let me analyze each file systematically, checking for:

1. AI writing patterns (em-dashes, -ing phrases, hedge words, etc.)
2. Logic flow and clarity
3. Data consistency with tables
4. Redundancy
5. Writing quality per the norms

Let me go through each file:

### abstract.tex
- Word count: Let me count... roughly 220 words - within target
- Three claims covered: fake safety, EE-only SDF limitation, fine-tuning source attribution - yes


- Issues found: the passive construction "these metrics can be systematically contaminated" needs to be more direct, and there are em-dashes (---) scattered throughout like "---all of its safe episodes" and "---dominated by" that violate the writing norms and need removal. The abstract is dense but successfully covers all three claims, and the closing statement about displacement filtering being necessary provides good closure. Let me scan through once more to catch any remaining em-dashes.

Looking at the analysis_claim1.tex file, I'm checking for em-dashes and writing quality. The em-dash in the table ("---$^\dagger$") is acceptable since it indicates "not applicable" rather than being a stylistic choice. The prose itself is strong—"At first glance" sets up the contrast effectively, "Yet this headline metric conceals a fundamental problem" lands well, and the closing about 99.6% of safe episodes being artifacts of a stationary robot is particularly effective. The definition of fake safe episodes is clear, and the line about the robot avoiding motion rather than obstacles is a sharp observation.

Now I'm checking for -ing phrases that could be tightened—"yielding a fake safe rate of 0%" and "indicating that the robot moves but collides" both use gerunds that might be rewritten more directly. I don't see any problematic em-dashes in the main text. Looking at the table data against the text claims, I'm verifying that the Pi0.5 metrics align: the table shows CAR=28.5% and TSR=71.5%, while the text mentions a 3-seed average of 26.8±1.6% and 74.7±1.5%, which are reasonably close. The safe episodes data also checks out—57 safe episodes across 200 total episodes. The language and framing look solid overall—the hedging about the anti-correlation is appropriately cautious, and the terminology is clear. But I'm noticing some structural issues: a few sentences are running long and could benefit from being broken up, and some phrasing like the displacement criterion reference could be more concise. The displacement distribution sentence in particular is doing too much work with its subordinate clauses.

Looking at lines 26-27, though, the substantive content is strong—the distinction between Pi0.5's genuine planning versus Pi0's immobility makes for a compelling close to the section. The real work here is tightening the prose without losing that clarity. I should focus on breaking up the longer sentences and streamlining the criterion reference.

Now checking claim2.tex for similar issues. The em-dash in discussion.tex is a separate problem, but I need to verify claim2 doesn't have the same pattern. The rhetorical question about SDF prediction accuracy works fine for framing the oracle experiment, and the table data checks out—all three oracle variants do show lower collision rates than the LoRA baseline, which supports the claim being made. Looking at the specific phrasing issues in claim2 — the colon followed by an -ing phrase could be restructured for clarity, and there are a few other -ing constructions that might benefit from revision. The explanations about action collapse and gradient behavior are solid though. Moving into the discussion section now, checking for em-dashes and other stylistic patterns.

I notice there's a double em-dash issue that needs fixing, and the Future Work section uses a numbered list structure that's a bit formulaic — could be more integrated into the narrative. The Limitations paragraph is quite dense and might warrant breaking up. Also catching that a phrase about minimum consistent motion appears to be in the wrong section.

Now I'm scanning through the discussion more carefully to identify which claims have specific empirical data that could be vulnerable to re-evaluation. I'm seeing multiple references to Claim 3 results scattered throughout — mentions of non-zero CAR values with zero frozen rates, the catastrophic TSR collapse pattern, and specific baseline numbers like the drop from 74.7% to below 7% at 30K steps. These are concrete findings tied to that claim that I should flag as potentially problematic if the underlying evaluation changes.

I also notice an em-dash formatting issue in line 6 where multiple dashes are used to set off a phrase about full-body collisions — I'll need to replace that with commas or parentheses for proper formatting. The rest of the discussion reads clearly, and the broader impact section is appropriately concise.

Now checking introduction.tex for em-dashes and problematic -ing phrases. I don't see any em-dashes there, but I'm finding two -ing ending phrases that need attention: one on line 13 about task performance collapse and another about collision avoidance reflecting genuine trajectory modification. The opening sentence is strong, and the benchmark description with its participle phrase works well structurally.

Looking at the third paragraph, it contains specific Claim 3 numbers about fine-tuning results—collision avoidance rates, frozen rates, and task success rates across different configurations. Since Claim 3 is frozen for analysis_claim3.tex, I need to be careful about whether these intro references should stay as-is or if they need adjustment given the task constraints. Looking at the contribution list, all three items map correctly to their respective sections and are well-supported by the paper. For the Pi0.5 description, the key details about TSR, end-effector motion, and fake safe rate all align with the underlying data, so the intro text is accurate as written.

Now I'm identifying the specific -ing phrase issues that need fixing across the tex files. In the abstract, I need to handle the em-dash and check word count. For the claim analyses, I'm targeting several gerund constructions that should be rewritten—particularly around the catastrophic performance collapse phrasing and the collision avoidance confirmation—plus a few other long sentences that could be tightened. I'll prioritize these edits by their impact on clarity.

Let me go through each file systematically. Starting with abstract.tex, that em-dash between "safety" and "all of its safe episodes" needs to become a semicolon or period. Then I'm moving through the claim files to catch those -ing endings and any other verbose constructions, before handling the discussion and introduction sections where similar em-dash and gerund issues appear. I'm reviewing the abstract and finding that Claim 3 data shouldn't be flagged there since the task didn't specify it. The closing statement about displacement filtering being necessary for meaningful evaluation is solid. Moving into the detailed analysis section, I'm checking the technical writing—the obstacle displacement measurement is clear and strong, though some sentences could be tightened. For instance, the displacement distribution description could be more concise by removing redundancy while keeping the key point about the clustering near zero with no meaningful spread toward planned trajectories.

Looking at the evaluation metrics, the end-effector displacement data across 200 episodes shows all safe episodes exceed 288mm displacement, confirming a 0% fake safe rate. I'm noting that the CAR_f calculation for Pi0-based methods is unambiguous—when these models avoid collision, it's because the robot simply didn't move. The phrasing around "yielding" could shift to more direct language like "the fake safe rate is 0%," though the current version works. I'm also checking whether CAR_f as a general metric needs further clarification in the next section. The CAR_f metric also serves a diagnostic purpose—methods achieving non-trivial values demonstrate that safety behavior stems from genuine avoidance rather than simply doing nothing. Pi0.5 fine-tuned on collision-free data is the first configuration to produce a meaningful CAR_f score. Looking at the capability-safety tradeoff, two distinct clusters emerge: Pi0-family methods cluster in the upper-left with high CAR but near-zero TSR, where over 99% of safe episodes are actually fake safe—what I'm calling the "fake safety zone"—while Pi0.5 occupies the lower-right with high TSR (73–76%) and low CAR (25–28%), indicating its collisions reflect genuine robot motion through the workspace.

This pattern holds consistently across all Pi0.5 seeds and Pi0 variants regardless of SDF loss application—models that execute tasks move the robot into collision-prone configurations, while models that fail to act avoid collisions by default. A high CAR score with near-zero TSR provides no real evidence of collision avoidance capability; it's just an artifact of inaction. The TSR-CAR plane reveals what neither metric shows alone: the upper-right quadrant represents genuinely safe and capable behavior, while the upper-left is accessible through action collapse. This anti-correlation appears as an empirical observation within the two model families examined.

Regarding the analysis claim: the oracle SDF setup eliminates prediction error entirely and provides the refinement module with a perfect distance signal at every timestep. If the refinement paradigm is sound, oracle performance should substantially exceed unrefined baselines. The results are significant—not marginal improvements.

The key finding is that even with perfect distance information, the refinement module produces more collisions than the baseline. Ground-truth SDF refinement fails to reduce action collapse; most safe episodes still come from inaction rather than active obstacle avoidance. This makes sense because the gradient operates on a trajectory already near-zero displacement, so perturbing it just produces near-zero displacement in a different direction. The refinement gradient pushes the end-effector away from obstacles but inadvertently increases collisions elsewhere on the robot arm, since it only operates on end-effector position without considering the full kinematic chain.

The latent-space variant fires refinements far more frequently (241.7 per episode versus 14.2 for action-space methods) and applies the SDF gradient in feature space rather than Cartesian coordinates. This latent space lacks direct geometric grounding, so small perturbations don't reliably translate into collision-free joint trajectories. The SDF prediction network never outputs distances below the refinement threshold across the test episodes, suggesting the network isn't learning meaningful distance predictions.

The core issue is that end-effector-only monitoring misses arm-body collisions, which dominate failures in manipulation tasks where the robot must navigate around obstacles. Effective collision avoidance for vision-language models will need representations that capture the full manipulator geometry, not just the tip position.

Now I'm reviewing the discussion section and flagging specific issues: there's a reference to Claim 3 about fine-tuning on collision-free data producing non-zero collision avoidance rate but catastrophic task success collapse, which I should note but not modify. I'm also catching formatting problems with em-dashes that should be replaced with parentheses or commas, and I'm examining the data showing how all fine-tuned models at 30K steps experience severe task success degradation from the 74.7% baseline down below 7%.

The limitations section honestly acknowledges that whether alternative training schedules or regularization could preserve task capability while maintaining collision avoidance hasn't been tested. There's also a good explanation of how in narrow corridors, signed distance field gradients actually redistribute collisions between obstacles rather than eliminating them—the gradient pushes the end-effector away from the nearest surface, but in tight bilateral geometries this just shifts the trajectory into the opposing obstacle, creating a collision transfer effect that defines a fundamental boundary condition for training-time supervision.

The future work section references the catastrophic task success collapse during fine-tuning, which is a qualitative mention of Claim 3 without specific numbers, so that's acceptable. I'm now moving into the broader impact section.

The contaminated evaluation metrics point is well-motivated—models that report high collision avoidance but complete zero tasks haven't actually learned safety, they've just learned to stop moving. The displacement filtering approach is clean because it only requires logging end-effector positions without additional data collection or model retraining.

Looking at the introduction now, the opening is strong: a model reporting 91.5% collision avoidance while completing zero tasks hasn't learned safety at all. The SafeLIBERO benchmark reference is comprehensive but the sentence structure is getting unwieldy with the participial phrase about comprising 32 scenarios across 1,600 episodes—it's trying to pack too much detail into one clause.

The A1-LoRA parenthetical could be tighter by using "which we call" instead of "referred to as." And when discussing how high CAR appears compelling, I can trim the implicit assumption clause—the core point is just that high CAR is assumed to reflect genuine obstacle avoidance, without needing to restate "across this emerging literature."

Now looking at the next section, action collapse isn't unique to Pi0—any VLA prone to mode collapse faces this vulnerability. The robot's real failure was learning to stop rather than actually avoiding obstacles, which echoes the opening nicely. The displacement-filtered CAR metric I'm proposing excludes low-movement episodes to distinguish real avoidance from inaction, though that sentence is quite dense with nested clauses. The threshold itself is robust since active episodes show displacements well above 200mm, so any threshold in that range would work.

The empirical contrast is striking: Pi0.5 gets high task success but terrible collision avoidance, while Pi0-based methods flip that trade-off entirely. The mechanical explanation is clean—a model that moves hits obstacles, one that doesn't move avoids them. End-effector-only SDF refinement has a fundamental structural problem, and even oracle variants underperform on collision avoidance. I'm working through the edits systematically now. I need to split those "-ing" constructions into separate sentences—"indicating that" and "confirming that" should each start their own sentence rather than dangling as participial phrases. The contributions list item about tracing collision avoidance to implicit learning from demonstrations is well-framed. Now I'm mapping out all the changes I need to make across the abstract and other sections, starting with fixing that em-dash and tightening up the phrasing around "can be systematically contaminated." I'm working through the editing priorities now. The style guide makes it clear that em-dashes are the top concern, followed by -ing phrase constructions and certain word choices. Rather than trying to polish everything, I should focus on the highest-impact changes that align with these norms.

For abstract.tex, I need to convert that em-dash to a period. In analysis_claim1.tex, the "yielding" phrase needs restructuring to avoid the -ing ending. I'm also reviewing the other flagged items to see which ones truly matter versus which are just nice refinements. Let me start making these targeted edits across the files in parallel. I'm working through the introduction edits now. For those two sentences about the early-stopped checkpoint and collision avoidance, I need to split them into separate statements rather than keeping them as dependent clauses. The first one should stand alone to emphasize the performance collapse between 10K and 30K steps, and the second should independently highlight that the robots are actually moving despite the degradation.

Looking at the analysis_claim1.tex file, I'm simplifying that sentence about the fake safe rate—removing the redundant phrasing and making it more direct. The key point is that all safe episodes show significant displacement, so the fake safe rate is zero.

For the displacement distribution, I want to keep "overwhelmingly" since it emphasizes how concentrated the data is, but I can tighten the language by replacing the awkward relative clause with "values consistent with planned trajectories"—that's clearer and more concise.

Now I'm moving to the A3 model analysis in analysis_claim2.tex, where the SDF prediction network fails to output meaningful distance values.  The key issue is that the learned SDF has essentially disabled the refinement mechanism by never triggering it, leaving the model performing at baseline levels. I can streamline this by changing "resulting in zero refinement steps" to "no refinement step is ever triggered" and simplifying "effectively reducing" to "which reduces"—both are tighter without losing meaning.

I should also scan the other files for em-dashes that need fixing. In discussion.tex there's one around "dominated by full-body collisions" and in analysis_claim1.tex there's one with the dagger symbol in the table.

Looking at the abstract word count, it seems to land around 200-220 words, which fits the 150-250 target nicely. The claim about "over 98% of episodes classified as safe" aligns with the specific percentages mentioned in claim1 (99.6% for A1-LoRA and 99.4% for LoRA baseline), so that's consistent.

Let me verify the definition of "fake safe" episodes in claim1 before finalizing my edits. I'm identifying sentences that end with -ing phrases, which is a common AI writing pattern to avoid. Looking at the first issue: "yielding a fake safe rate of 0\%" ends the sentence before moving to the next clause about Pi0.5's collision avoidance. I need to restructure this to eliminate the dangling -ing phrase at the sentence boundary. I'm continuing to identify sentences that end with -ing clauses when they shouldn't. Looking at the refinement module analysis, I see several more instances where gerund phrases conclude sentences that need restructuring. The pattern is consistent: these -ing constructions appear at sentence boundaries in claims about the model's behavior, particularly around the SDF refinement mechanism and its failure modes. I need to flag all of these for revision to improve the prose flow.

Now I'm checking for em-dashes that should be converted to semicolons or other punctuation. I found a few instances where triple dashes appear in the LaTeX source—the abstract has one between "safety" and "all," and the discussion section has another between "challenges" and "dominated." These need to be replaced with proper em-dashes or semicolons depending on context. The en-dashes marking percentage ranges and year spans are correct as-is.

Compiling the final list of edits across the files... I'm going through the manuscript line by line to check for grammatical issues and awkward phrasing. Looking at the analysis sections, I need to verify which sentences end with -ing constructions and which ones don't, then apply targeted rewrites to improve clarity and flow. The key fixes involve breaking up long clauses, replacing passive constructions, and tightening the language around the fake safety findings and trajectory analysis. I'm working through the phrasing of that last fix more carefully. The original sentence structure with "effectively reducing" changes the grammatical subject, so I need to separate it into two independent clauses—one about the SDF calibrating its predictions, and another about how the model then operates as an unrefined baseline with the performance metrics showing through.

For the early-stopping checkpoint point, I can tighten it by using a semicolon to connect the performance retention metrics directly to when the collapse happens, making the causal relationship clearer without extra words.

The frozen rate claim works well split into two sentences—first establishing that motion still occurs despite degradation, then clarifying that this motion represents actual trajectory changes rather than the model just staying still.

Now looking at the displacement distribution, I need to describe what the figure shows about how the values cluster.  "Overwhelmingly" does add useful emphasis about how concentrated the distribution is, so I'll keep that but refine the second part to be more precise about what's missing—the values that would correspond to obstacle-aware planning.

I've got the edits mapped out. Time to apply them across the files since they're independent changes.

For the abstract, I need to decide between a semicolon and period after "0% fake safety." The semicolon feels right because it keeps the contrast tight—the fake safety claim and the reality of genuine avoidance are closely linked thoughts. Then there's the passive voice issue with "can be systematically contaminated"—I could strengthen it to "action collapse systematically contaminates these metrics," but "can be" might be intentional to suggest this is a general possibility rather than something that always happens. I'll think through which reading fits the paper's argument better. I'm satisfied with leaving that phrasing as-is. Now I need to finalize all the edits across these files—I'll do a quick word count check on the abstract to confirm it's hitting around 200 words, which it looks to be from a visual scan. Before executing the changes, let me verify the exact strings I'm replacing, particularly the em-dash formatting in LaTeX which uses three hyphens. Once I've confirmed those match, I can apply all the edits in parallel across the files.

I'm also catching an issue in the third contribution where an -ing phrase disrupts the flow—I should restructure it to use a semicolon instead, keeping the sentence more cohesive. There's another incomplete sentence starting with "All fine-tuned models suffer catastrophic TSR collapse" that I need to address as well. I'm going through the edits systematically across the files. In the abstract, I'm changing a dash to a semicolon for better punctuation. Then in the analysis file, I'm refining several phrasings—replacing "confirming that" with "and," using semicolons to separate related clauses more cleanly, changing "is intended as" to "serves as," and working through the remaining edits in that section. I'm continuing to refine the introduction section, making the writing more concise by replacing em-dashes and conjunctions with semicolons and periods to create sharper transitions between claims about performance collapse, genuine avoidance behavior, and the distribution of the avoidance signal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "860f5bd1-7d0c-4150-be02-d5b0cf960dae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 18_

I'll now make targeted edits across all four files (excluding claim3). The main issues: em-dashes (highest priority per norms), -ing ending phrases, and minor tightening.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "3df5fcfd-a812-4ea9-8f81-34d9efc933d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01EKdYQUe4FzEzJs5g52NebU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "fake safety---all of its safe episodes",
  "new_string": "fake safety; all of its safe episodes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "2fa96b35-85f9-4f39-8e3a-36f4acdab1b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 20 · 2026-05-26T09:32:30.824Z_

<details><summary>↩ Tool result · `toolu_01EKdYQUe4FzEzJs5g52NebU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "2178515b-d7d3-42ad-bbcd-49ea86a68f0c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "oldString": "fake safety---all of its safe episodes",
    "newString": "fake safety; all of its safe episodes",
    "originalFile": "\\begin{abstract}\nRecent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, while Pi0.5, which achieves 74.7\\% TSR, exhibits 0\\% fake safety---all of its safe episodes reflect genuine avoidance with end-effector displacements exceeding 288\\,mm. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\\sim}$55\\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\\% to $<$7\\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.\n\\end{abstract}",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\begin{abstract}",
          "-Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, while Pi0.5, which achieves 74.7\\% TSR, exhibits 0\\% fake safety---all of its safe episodes reflect genuine avoidance with end-effector displacements exceeding 288\\,mm. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\\sim}$55\\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\\% to $<$7\\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.",
          "+Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, while Pi0.5, which achieves 74.7\\% TSR, exhibits 0\\% fake safety; all of its safe episodes reflect genuine avoidance with end-effector displacements exceeding 288\\,mm. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\\sim}$55\\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\\% to $<$7\\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.",
          " \\end{abstract}",
          "\\ No newline at end of file"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01EWaX7JpZg7rJWRrsRwH99x`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "challenges---dominated by full-body collisions---beyond",
  "new_string": "challenges, dominated by full-body collisions, beyond"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "02bb523a-e00d-4ca0-9241-b6a382914e02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 22 · 2026-05-26T09:32:31.756Z_

<details><summary>↩ Tool result · `toolu_01EWaX7JpZg7rJWRrsRwH99x`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "cd341e10-a8cc-439d-9324-2af2cba14ad8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "challenges---dominated by full-body collisions---beyond",
    "newString": "challenges, dominated by full-body collisions, beyond",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges---dominated by full-body collisions---beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.\n\n\\paragraph{Future work.}\nFive directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.\n\n\\paragraph{Broader impact.}\nMetric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Limitations.}",
          "-The empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges---dominated by full-body collisions---beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.",
          "+The empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.",
          " ",
          " \\paragraph{Future work.}",
          " Five directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01NvGQh49UeSpiDJpPNz5bbM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "old_string": "TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior",
  "new_string": "TSR is 0\\% across all 800 episodes, and the model produces no meaningful task-directed behavior"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "2ef74a59-e881-41c7-b4b2-a4f225ee6830",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 24 · 2026-05-26T09:32:33.167Z_

<details><summary>↩ Tool result · `toolu_01NvGQh49UeSpiDJpPNz5bbM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "34ba8a6e-7052-422c-b317-c58017b5279b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "oldString": "TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior",
    "newString": "TSR is 0\\% across all 800 episodes, and the model produces no meaningful task-directed behavior",
    "originalFile": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 & 28.5 & 71.5 & 0.0 & 57 / 57 & 28.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. Pi0.5 row from single-seed re-evaluation (seed~7, 200 episodes) with EE displacement recording; all safe episodes exceed 288\\,mm displacement.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\\,mm, yielding a fake safe rate of 0\\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\\text{f}$ equals its raw CAR (28.5\\%), because no episodes are filtered by the displacement threshold.\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero. Pi0.5 presents the opposite extreme: every episode exceeds the displacement threshold, so CAR$_\\text{f}$ equals raw CAR (28.5\\%). The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " ",
          " At first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.",
          " ",
          "-We define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.",
          "+We define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, and the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.",
          " ",
          " \\begin{table}[t]",
          " \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01GkivnuBUGS5BeuJKBTgWHc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "old_string": "above 288\\,mm, yielding a fake safe rate of 0\\%. Pi0.5's collision avoidance",
  "new_string": "above 288\\,mm; the fake safe rate is 0\\%. Pi0.5's collision avoidance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "693e7308-b827-4a0b-b959-a26c8eed4c52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 26 · 2026-05-26T09:32:34.579Z_

<details><summary>↩ Tool result · `toolu_01GkivnuBUGS5BeuJKBTgWHc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "a9b20ff9-2d41-4d57-95fd-b9cb8aefc7df",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "oldString": "above 288\\,mm, yielding a fake safe rate of 0\\%. Pi0.5's collision avoidance",
    "newString": "above 288\\,mm; the fake safe rate is 0\\%. Pi0.5's collision avoidance",
    "originalFile": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, and the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 & 28.5 & 71.5 & 0.0 & 57 / 57 & 28.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. Pi0.5 row from single-seed re-evaluation (seed~7, 200 episodes) with EE displacement recording; all safe episodes exceed 288\\,mm displacement.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\\,mm, yielding a fake safe rate of 0\\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\\text{f}$ equals its raw CAR (28.5\\%), because no episodes are filtered by the displacement threshold.\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero. Pi0.5 presents the opposite extreme: every episode exceeds the displacement threshold, so CAR$_\\text{f}$ equals raw CAR (28.5\\%). The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          " {\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. Pi0.5 row from single-seed re-evaluation (seed~7, 200 episodes) with EE displacement recording; all safe episodes exceed 288\\,mm displacement.}",
          " \\end{table}",
          " ",
          "-This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\\,mm, yielding a fake safe rate of 0\\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\\text{f}$ equals its raw CAR (28.5\\%), because no episodes are filtered by the displacement threshold.",
          "+This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\\,mm; the fake safe rate is 0\\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\\text{f}$ equals its raw CAR (28.5\\%), because no episodes are filtered by the displacement threshold.",
          " For the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.",
          " ",
          " These observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01PYVEcrennX2jHeJqacG2pU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "old_string": "CAR$_\\text{f}$ is intended as a general-purpose diagnostic",
  "new_string": "CAR$_\\text{f}$ serves as a general-purpose diagnostic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "29ef225d-56cd-4843-aa13-9419053977e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 28 · 2026-05-26T09:32:35.522Z_

<details><summary>↩ Tool result · `toolu_01PYVEcrennX2jHeJqacG2pU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "f01c0c17-d9df-4188-9896-5dcc2000e03b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "oldString": "CAR$_\\text{f}$ is intended as a general-purpose diagnostic",
    "newString": "CAR$_\\text{f}$ serves as a general-purpose diagnostic",
    "originalFile": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, and the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 & 28.5 & 71.5 & 0.0 & 57 / 57 & 28.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. Pi0.5 row from single-seed re-evaluation (seed~7, 200 episodes) with EE displacement recording; all safe episodes exceed 288\\,mm displacement.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\\,mm; the fake safe rate is 0\\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\\text{f}$ equals its raw CAR (28.5\\%), because no episodes are filtered by the displacement threshold.\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero. Pi0.5 presents the opposite extreme: every episode exceeds the displacement threshold, so CAR$_\\text{f}$ equals raw CAR (28.5\\%). The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\\,mm; the fake safe rate is 0\\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\\text{f}$ equals its raw CAR (28.5\\%), because no episodes are filtered by the displacement threshold.",
          " For the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.",
          " ",
          "-These observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.",
          "+These observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ serves as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.",
          " ",
          " The threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01GPj6MA5P9TJozUVqmZHZ17`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "old_string": "The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles.",
  "new_string": "The displacement distribution (Figure~\\ref{fig:displacement}) clusters overwhelmingly near zero, with no spread toward values consistent with planned trajectories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "b4345b9c-f57c-4ad3-93fa-4ba297d55f25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 30 · 2026-05-26T09:32:36.938Z_

<details><summary>↩ Tool result · `toolu_01GPj6MA5P9TJozUVqmZHZ17`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "0bad99d4-e511-46a9-8ce2-3f1cea55f6c2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "oldString": "The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles.",
    "newString": "The displacement distribution (Figure~\\ref{fig:displacement}) clusters overwhelmingly near zero, with no spread toward values consistent with planned trajectories.",
    "originalFile": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, and the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 & 28.5 & 71.5 & 0.0 & 57 / 57 & 28.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. Pi0.5 row from single-seed re-evaluation (seed~7, 200 episodes) with EE displacement recording; all safe episodes exceed 288\\,mm displacement.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. Re-evaluation with end-effector displacement recording confirms this distinction: across 200 episodes, all 57 safe episodes exhibit maximum end-effector displacement above 288\\,mm; the fake safe rate is 0\\%. Pi0.5's collision avoidance reflects genuine trajectory planning around obstacles, not inaction. Its CAR$_\\text{f}$ equals its raw CAR (28.5\\%), because no episodes are filtered by the displacement threshold.\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ serves as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero. Pi0.5 presents the opposite extreme: every episode exceeds the displacement threshold, so CAR$_\\text{f}$ equals raw CAR (28.5\\%). The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " ",
          " At first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.",
          " ",
          "-We define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, and the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.",
          "+We define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, and the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution (Figure~\\ref{fig:displacement}) clusters overwhelmingly near zero, with no spread toward values consistent with planned trajectories. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.",
          " ",
          " \\begin{table}[t]",
          " \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01UpLndfwioxv2131o6LErFA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex",
  "old_string": "it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep",
  "new_string": "it eliminates prediction error entirely and provides the refinement module with a perfect distance signal at every timestep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "75f75f69-183c-4179-a3c8-cf58204fee77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 32 · 2026-05-26T09:32:37.876Z_

<details><summary>↩ Tool result · `toolu_01UpLndfwioxv2131o6LErFA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "cdf3b297-c2d3-4841-af68-0307ce181ec4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex",
    "oldString": "it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep",
    "newString": "it eliminates prediction error entirely and provides the refinement module with a perfect distance signal at every timestep",
    "originalFile": "\\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\n\nThe analysis in Section~\\ref{sec:fake_safety} identifies action collapse and fake safety as pervasive problems, but leaves open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\\%, Full-FT 83.0\\%), and fake safe rates remain above 96\\%.}\n\\label{tab:oracle}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & TSR (\\%) & CAR (\\%) & Fake Safe (\\%) & Refines/ep \\\\\n\\midrule\nLoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\\\\nFull-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\\\\n\\midrule\nOracle-adaptive (GT, dyn.\\ $\\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\\\\nOracle-fixed (GT, $\\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\\\\nOracle-feature (GT, feat.\\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\\\\n\\midrule\nA3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\\%) falls 5.1 percentage points below the LoRA baseline (82.0\\%) and 6.1 points below Full-FT (83.0\\%). The adaptive and fixed-step variants perform worse still, at 75.0\\% and 73.1\\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance. The persistence of action collapse under gradient correction is expected: refinement can redirect existing motion away from obstacles, but cannot generate motion from a policy that has collapsed into inaction. The gradient operates on a trajectory that is already near-zero; perturbing near-zero displacement produces near-zero displacement in a different direction, not a viable collision-free path.\n\nFigure~\\ref{fig:oracle_bar} visualizes this aggregate gap. The per-task breakdown reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive reaches 55.0\\% and Oracle-feature reaches 47.5\\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\\% to 82.5\\% on task~0 and from 98.0\\% to 77.5\\% on task~2. The refinement gradient pushes the end-effector away from the obstacle surface but perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.\n\nThis failure mode is structural. The SDF refinement paradigm as formulated in prior work~\\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution.\n\nThe feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.\n\nThe A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.\n\nThese results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip. Section~\\ref{sec:avoidance_source} investigates the source of collision avoidance in fine-tuned models and the role of geometric supervision.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}",
          " ",
          "-The analysis in Section~\\ref{sec:fake_safety} identifies action collapse and fake safety as pervasive problems, but leaves open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely, providing the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.",
          "+The analysis in Section~\\ref{sec:fake_safety} identifies action collapse and fake safety as pervasive problems, but leaves open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely and provides the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.",
          " ",
          " \\begin{table}[t]",
          " \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_017mD9pdV4x7QPrV2D6JbQZA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex",
  "old_string": "the 160 evaluation episodes, resulting in zero refinement steps",
  "new_string": "the 160 evaluation episodes; no refinement steps occur"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "fb6a0b68-6dd3-48c2-888f-c528d483a7b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 34 · 2026-05-26T09:32:38.973Z_

<details><summary>↩ Tool result · `toolu_017mD9pdV4x7QPrV2D6JbQZA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "5dcffcc0-e613-41d9-a73a-69b0325556db",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex",
    "oldString": "the 160 evaluation episodes, resulting in zero refinement steps",
    "newString": "the 160 evaluation episodes; no refinement steps occur",
    "originalFile": "\\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\n\nThe analysis in Section~\\ref{sec:fake_safety} identifies action collapse and fake safety as pervasive problems, but leaves open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely and provides the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\\%, Full-FT 83.0\\%), and fake safe rates remain above 96\\%.}\n\\label{tab:oracle}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & TSR (\\%) & CAR (\\%) & Fake Safe (\\%) & Refines/ep \\\\\n\\midrule\nLoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\\\\nFull-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\\\\n\\midrule\nOracle-adaptive (GT, dyn.\\ $\\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\\\\nOracle-fixed (GT, $\\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\\\\nOracle-feature (GT, feat.\\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\\\\n\\midrule\nA3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\\%) falls 5.1 percentage points below the LoRA baseline (82.0\\%) and 6.1 points below Full-FT (83.0\\%). The adaptive and fixed-step variants perform worse still, at 75.0\\% and 73.1\\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance. The persistence of action collapse under gradient correction is expected: refinement can redirect existing motion away from obstacles, but cannot generate motion from a policy that has collapsed into inaction. The gradient operates on a trajectory that is already near-zero; perturbing near-zero displacement produces near-zero displacement in a different direction, not a viable collision-free path.\n\nFigure~\\ref{fig:oracle_bar} visualizes this aggregate gap. The per-task breakdown reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive reaches 55.0\\% and Oracle-feature reaches 47.5\\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\\% to 82.5\\% on task~0 and from 98.0\\% to 77.5\\% on task~2. The refinement gradient pushes the end-effector away from the obstacle surface but perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.\n\nThis failure mode is structural. The SDF refinement paradigm as formulated in prior work~\\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution.\n\nThe feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.\n\nThe A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.\n\nThese results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip. Section~\\ref{sec:avoidance_source} investigates the source of collision avoidance in fine-tuned models and the role of geometric supervision.\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 6,
        "newStart": 32,
        "newLines": 6,
        "lines": [
          " ",
          " The feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.",
          " ",
          "-The A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes, resulting in zero refinement steps. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.",
          "+The A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes; no refinement steps occur. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.",
          " ",
          " These results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip. Section~\\ref{sec:avoidance_source} investigates the source of collision avoidance in fine-tuned models and the role of geometric supervision."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_01FEzZz5LMw5nGfd7NL8486Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex",
  "old_string": "avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline",
  "new_string": "avoid triggering the safety mechanism. The model thus operates as an unrefined baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "c8d36db6-9f61-444d-8e55-73b1fc4f6fe3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 36 · 2026-05-26T09:32:39.749Z_

<details><summary>↩ Tool result · `toolu_01FEzZz5LMw5nGfd7NL8486Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "0f0bae84-ce98-4086-8608-ef1a9648b1b2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim2.tex",
    "oldString": "avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline",
    "newString": "avoid triggering the safety mechanism. The model thus operates as an unrefined baseline",
    "originalFile": "\\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\n\nThe analysis in Section~\\ref{sec:fake_safety} identifies action collapse and fake safety as pervasive problems, but leaves open a natural question: could a sufficiently accurate SDF prediction still enable effective runtime refinement? To isolate the SDF representation itself from prediction quality, we construct an oracle experiment. We replace the learned SDF network with the ground-truth signed distance field computed directly from the known obstacle geometry. This oracle represents the theoretical upper bound of end-effector-only SDF refinement: it eliminates prediction error entirely and provides the refinement module with a perfect distance signal at every timestep. If the SDF refinement paradigm is sound, oracle performance should exceed that of unrefined baselines by a wide margin.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\\%, Full-FT 83.0\\%), and fake safe rates remain above 96\\%.}\n\\label{tab:oracle}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & TSR (\\%) & CAR (\\%) & Fake Safe (\\%) & Refines/ep \\\\\n\\midrule\nLoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\\\\nFull-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\\\\n\\midrule\nOracle-adaptive (GT, dyn.\\ $\\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\\\\nOracle-fixed (GT, $\\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\\\\nOracle-feature (GT, feat.\\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\\\\n\\midrule\nA3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:oracle} reports the results. All three oracle variants achieve CAR below that of the unrefined baselines. The best oracle (Oracle-feature, 76.9\\%) falls 5.1 percentage points below the LoRA baseline (82.0\\%) and 6.1 points below Full-FT (83.0\\%). The adaptive and fixed-step variants perform worse still, at 75.0\\% and 73.1\\% respectively. These results are not marginal: the refinement module with perfect distance information produces more collisions than doing nothing at all. The fake safe rate tells a complementary story. Oracle-adaptive and Oracle-fixed both register 98.3\\% fake safe episodes (118 of 120 and 115 of 117 safe episodes, respectively), while Oracle-feature registers 96.7\\% (119 of 123). Ground-truth SDF refinement does not reduce action collapse; the vast majority of safe episodes remain attributable to inaction rather than obstacle avoidance. The persistence of action collapse under gradient correction is expected: refinement can redirect existing motion away from obstacles, but cannot generate motion from a policy that has collapsed into inaction. The gradient operates on a trajectory that is already near-zero; perturbing near-zero displacement produces near-zero displacement in a different direction, not a viable collision-free path.\n\nFigure~\\ref{fig:oracle_bar} visualizes this aggregate gap. The per-task breakdown reveals additional structure. On task~1, the most collision-prone task where the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive reaches 55.0\\% and Oracle-feature reaches 47.5\\%, a modest improvement consistent with a scenario where the end-effector is the primary collision body. On tasks~0, 2, and~3, all oracle variants produce lower CAR than the baseline: Oracle-adaptive drops from 96.0\\% to 82.5\\% on task~0 and from 98.0\\% to 77.5\\% on task~2. The refinement gradient pushes the end-effector away from the obstacle surface but perturbs the planned trajectory in ways that increase collisions elsewhere on the robot arm.\n\nThis failure mode is structural. The SDF refinement paradigm as formulated in prior work~\\cite{hu2025vlsa} computes the signed distance from the end-effector to the nearest obstacle surface and applies a gradient step to increase this distance when it falls below a safety threshold. The gradient operates exclusively on the end-effector position; no distance constraint applies to the remaining links of the robot arm. When the gradient pushes the end-effector away from an obstacle, the resulting joint-space displacement can rotate intermediate links toward or through the obstacle volume. The refinement thus trades one collision for another, with no mechanism to detect or prevent the substitution.\n\nThe feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.\n\nThe A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes; no refinement steps occur. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.\n\nThese results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip. Section~\\ref{sec:avoidance_source} investigates the source of collision avoidance in fine-tuned models and the role of geometric supervision.\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 6,
        "newStart": 32,
        "newLines": 6,
        "lines": [
          " ",
          " The feature-space oracle makes this coupling problem explicit. It applies the SDF gradient in the policy's latent action space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode versus 14.2 for action-space variants). Yet its gradient magnitudes are extremely small (0.004--0.006, compared to 0.18--0.49 in action space), and the resulting CAR (76.9\\%) shows no significant advantage over the action-space oracles. The latent space lacks a direct geometric relationship to full-body configuration; small perturbations in feature space do not reliably translate into collision-free joint trajectories.",
          " ",
          "-The A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes; no refinement steps occur. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism, effectively reducing the model to an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.",
          "+The A3 model with a learned SDF head illustrates the complementary failure. In this configuration, the SDF prediction network never outputs a distance below the refinement threshold across any of the 160 evaluation episodes; no refinement steps occur. The learned SDF has calibrated its predictions to avoid triggering the safety mechanism. The model thus operates as an unrefined baseline (CAR of 74.5\\%, consistent with the oracle range). The refinement module, even if it could improve safety, is never activated.",
          " ",
          " These results establish that end-effector-only SDF is a structural limitation, not merely an engineering gap. Perfect distance information does not compensate for the absence of full-body collision awareness. Any refinement scheme that monitors only the end-effector position will remain blind to arm-body collisions, the dominant failure mode in manipulation tasks where the robot must reach around or past obstacles. Effective collision avoidance for VLA models will require representations that account for the geometric extent of the entire manipulator, not only its tip. Section~\\ref{sec:avoidance_source} investigates the source of collision avoidance in fine-tuned models and the role of geometric supervision."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01XGT42JSrfRZ7PqkEFwDRg9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps",
  "new_string": "56.5--57.5\\%; catastrophic task performance collapse occurs between 10K and 30K steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "3388045e-35b9-41cd-aac4-bb79253a36fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 38 · 2026-05-26T09:32:41.173Z_

<details><summary>↩ Tool result · `toolu_01XGT42JSrfRZ7PqkEFwDRg9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "fde8191e-988a-46c4-b04b-fd3db54b2a0d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps",
    "newString": "56.5--57.5\\%; catastrophic task performance collapse occurs between 10K and 30K steps",
    "originalFile": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " ",
          " We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.",
          " ",
          "-The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.",
          "+The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%; catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.",
          " ",
          " Our contributions are as follows:",
          " \\begin{itemize}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01F92nUSW1wT1nobL1VWfRdc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "(0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.",
  "new_string": "(0\\% frozen rate). Their collision avoidance reflects genuine trajectory modification, not inaction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "ca831033-5c21-4302-a7c9-7857a5eafe3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 40 · 2026-05-26T09:32:42.269Z_

<details><summary>↩ Tool result · `toolu_01F92nUSW1wT1nobL1VWfRdc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "9b6ad794-1fc4-4f72-a1da-8c4b9fa45721",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "(0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.",
    "newString": "(0\\% frozen rate). Their collision avoidance reflects genuine trajectory modification, not inaction.",
    "originalFile": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%; catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " ",
          " We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.",
          " ",
          "-The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%; catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.",
          "+The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%; catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate). Their collision avoidance reflects genuine trajectory modification, not inaction.",
          " ",
          " Our contributions are as follows:",
          " \\begin{itemize}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_017VVtTUq1QyBXubZgEd6VrA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "(CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution.",
  "new_string": "(CAR 50.5--52.8\\%, TSR 6.8\\%); the avoidance signal resides in the training distribution."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "a1216ffb-08b3-45c4-92ff-002259abec86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014RxoSoHWE2tnxR5fBJg9AB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13776,
      "cache_read_input_tokens": 23979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13776
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

_source line 42 · 2026-05-26T09:32:43.856Z_

<details><summary>↩ Tool result · `toolu_017VVtTUq1QyBXubZgEd6VrA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "4e652612-eb90-48d6-b798-d6a4ecc0e230",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "(CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution.",
    "newString": "(CAR 50.5--52.8\\%, TSR 6.8\\%); the avoidance signal resides in the training distribution.",
    "originalFile": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%; catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate). Their collision avoidance reflects genuine trajectory modification, not inaction.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 5,
        "newStart": 16,
        "newLines": 5,
        "lines": [
          " \\begin{itemize}",
          "     \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).",
          "     \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).",
          "-    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).",
          "+    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%); the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).",
          " \\end{itemize}",
          "\\ No newline at end of file"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
All 12 edits applied successfully. Let me verify the changes by reading the files.

Actually, let me also do a final grep for any remaining em-dashes or -ing endings I might have missed across all 4 modified files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "8840ef51-609b-4f2f-a54b-de42f5017b15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJoevYw4VrXkLEH9QgXwwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43052,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 43052
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

_source line 44_

All 12 edits applied. Let me verify with a quick grep for remaining em-dashes and -ing endings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "826fc8a0-1073-443a-9979-4f2413efad64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJoevYw4VrXkLEH9QgXwwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43052,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 43052
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

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_01THU6p63NxyHfXwmKFrBGMf`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "8694f678-2497-49a4-b679-bc18f31149dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJoevYw4VrXkLEH9QgXwwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43052,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 43052
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

_source line 46 · 2026-05-26T09:32:50.027Z_

<details><summary>↩ Tool result · `toolu_01THU6p63NxyHfXwmKFrBGMf`</summary>

```text
docs/paper/analysis_claim1.tex:17:A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\dagger$ \\
docs/paper/analysis_claim3.tex:54:[Omitted long matching line]
docs/paper/analysis_claim3.tex:63:This composite mechanism---catastrophic forgetting of manipulation semantics coupled with retained collision avoidance from imitation of collision-free demonstrations---explains the simultaneous CAR improvement and TSR collapse. The partial survival of Chocolate Pudding (${\sim}$25\% vs.\ 0\% for other tasks) suggests task-specific vulnerability to forgetting, potentially reflecting differences in grasp geometry or training distribution coverage across objects.
docs/paper/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/analysis_claim4.tex:33:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "0ee68bee-0b73-4608-b8ee-9fb8b1df22f3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis_claim1.tex:17:A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\ndocs/paper/analysis_claim3.tex:54:[Omitted long matching line]\ndocs/paper/analysis_claim3.tex:63:This composite mechanism---catastrophic forgetting of manipulation semantics coupled with retained collision avoidance from imitation of collision-free demonstrations---explains the simultaneous CAR improvement and TSR collapse. The partial survival of Chocolate Pudding (${\\sim}$25\\% vs.\\ 0\\% for other tasks) suggests task-specific vulnerability to forgetting, potentially reflecting differences in grasp geometry or training distribution coverage across objects.\ndocs/paper/analysis_claim4.tex:29:[Omitted long matching line]\ndocs/paper/analysis_claim4.tex:33:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_01CEkWANeTWhe1jxqfttyurN`</summary>

```json
{
  "pattern": "ing that |ing the |ing a ",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "glob": "{abstract,analysis_claim1,analysis_claim2,discussion,introduction}.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "542808e1-e4ea-48a0-9834-3960a85a2f49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJoevYw4VrXkLEH9QgXwwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43052,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 43052
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

_source line 48 · 2026-05-26T09:32:51.232Z_

<details><summary>↩ Tool result · `toolu_01CEkWANeTWhe1jxqfttyurN`</summary>

```text
docs/paper/analysis_claim2.tex:35:[Omitted long matching line]
docs/paper/discussion.tex:3:[Omitted long matching line]
docs/paper/discussion.tex:6:[Omitted long matching line]
docs/paper/introduction.tex:9:[Omitted long matching line]
docs/paper/introduction.tex:17:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "3043e00b-e609-4cb3-8bd9-ba715d823092",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis_claim2.tex:35:[Omitted long matching line]\ndocs/paper/discussion.tex:3:[Omitted long matching line]\ndocs/paper/discussion.tex:6:[Omitted long matching line]\ndocs/paper/introduction.tex:9:[Omitted long matching line]\ndocs/paper/introduction.tex:17:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 49_

<details><summary>Logged reasoning block</summary>

```text
Let me check the remaining `---` instances:
1. `analysis_claim1.tex:17` — table entry `---$^\dagger$` — this is a table dash (allowed exception)
2. `analysis_claim3.tex:54,63` — Claim 3, frozen, DO NOT MODIFY
3. `analysis_claim4.tex:29,33` — not in my scope

Good, all em-dashes in my files are fixed. The only remaining `---` is the table entry which is an allowed exception.

Now for the -ing patterns, let me check the specific lines. The grep matched several but they may be mid-sentence -ing (gerunds, participial modifiers) rather than sentence-ending -ing phrases. Let me look at the specific matches more carefully.


Now I'm examining the actual lines to see which -ing patterns are problematic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "58c1b0e7-1d91-4a32-8a03-40478bb73561",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QZ7F93nrbnuLJ3yeGH71G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 54499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 753
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

_source line 50_

<details open><summary>🔧 Tool call — Grep · `toolu_019pm9QYLBL3AkUW5uvN71gq`</summary>

```json
{
  "pattern": ", (confirming|indicating|yielding|establishing|providing|resulting|reducing|highlighting|demonstrating|showcasing|suggesting|revealing) ",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "glob": "{abstract,analysis_claim1,analysis_claim2,discussion,introduction}.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "79da0c39-a04c-4bc3-abdd-6513ff7fd0a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QZ7F93nrbnuLJ3yeGH71G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 54499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 753
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

_source line 51 · 2026-05-26T09:33:00.424Z_

<details><summary>↩ Tool result · `toolu_019pm9QYLBL3AkUW5uvN71gq`</summary>

```text
docs/paper/discussion.tex:3:[Omitted long matching line]
docs/paper/discussion.tex:6:[Omitted long matching line]
docs/paper/introduction.tex:9:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "78045b89-2952-4e01-8cf8-93caa236709c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:3:[Omitted long matching line]\ndocs/paper/discussion.tex:6:[Omitted long matching line]\ndocs/paper/introduction.tex:9:[Omitted long matching line]",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Let me see the full lines to check if these are -ing ending patterns that need fixing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "8b2dc446-3e62-4006-b731-195e555d1c27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VznQMnioM7niT9QiSbXsE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 55252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_0197i7oD1CrCtmhvNq2Nhqd1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "offset": 2,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "533c9170-a74b-48fd-889f-eeddfaa9c5f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VznQMnioM7niT9QiSbXsE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 55252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 54 · 2026-05-26T09:33:04.283Z_

<details><summary>↩ Tool result · `toolu_0197i7oD1CrCtmhvNq2Nhqd1`</summary>

```text
2	
3	This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\ref{sec:avoidance_source}).
4	
5	\paragraph{Limitations.}
6	The empirical scope of this study is bounded in several respects. All experiments use the \texttt{object\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \texttt{spatial\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\% CAR despite substantial end-effector displacement (0.29\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \texttt{object\_pudding} benchmark. The EE-only SDF oracle (Section~\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\tau_d = 0.1$\,mm is empirically robust across four orders of magnitude (Appendix~\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\% baseline to $<$7\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "72225783-1997-4765-a703-13a6d0a1c377",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.",
      "numLines": 5,
      "startLine": 2,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01QcKQavvhLoeSukfASFbKW2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "offset": 8,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "9eae3107-a509-4c43-90ea-6d24be47e014",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VznQMnioM7niT9QiSbXsE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 55252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 56 · 2026-05-26T09:33:04.859Z_

<details><summary>↩ Tool result · `toolu_01QcKQavvhLoeSukfASFbKW2`</summary>

```text
8	
9	For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\% exhibit a maximum displacement below 0.1\,mm, and obstacle displacement remains below 5\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\% CAR with 99.4\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\,mm), yielding a fake safe rate of 0\%.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "7b070c52-eb35-4a14-8e42-fa4d0261a798",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.\n",
      "numLines": 3,
      "startLine": 8,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Let me check the remaining -ing patterns:

1. **discussion.tex line 3**: "providing a metric that credits only active avoidance" — this is mid-sentence, followed by ". Two structural findings...". The sentence structure is: "CAR_f separates these two behaviors by excluding episodes below a displacement threshold τ_d, providing a metric that credits only active avoidance." — This ends the sentence with an -ing phrase! Fix needed.

2. **discussion.tex line 3**: "placing it in a region of the TSR-CAR plane" — "Fine-tuning on collision-free demonstrations produces non-zero CAR_f with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region..." — -ing ending. 

This is Claim 3 content, so I'll flag it but leave it unchanged to follow the guidelines. Moving on to the next instances:

3. **discussion.tex line 6**: "indicating that the robot moves but collides through arm-body contact rather than end-effector contact" — -ing ending phrase in the Limitations paragraph about spatial_bowl results (Claim 2 territory). This one I should fix.

4. **introduction.tex line 9**: "yielding a fake safe rate of 0\%" — -ing ending that needs correction.

Let me work through the fixes. For discussion line 6, I'm replacing the -ing phrase with a colon to separate the explanation: "the Pi0 Full-FT baseline achieves 0\% CAR despite substantial end-effector displacement (0.29\,m): the robot moves but collides through arm-body contact rather than end-effector contact." For intro line 9, I'm converting "yielding a fake safe rate of 0\%" to "and its fake safe rate is 0\%." I'll also note the Claim 3 data locations in the discussion section for flagging.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "0bb50768-d403-4185-9050-f8d877b65686",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6SCEbhZM686YGZDNgUNpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 55719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1390
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

_source line 58_

Found three more -ing ending phrases. Fixing them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "9d0c8356-07c3-4fe1-bab3-11b9c8a21520",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6SCEbhZM686YGZDNgUNpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 55719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1390
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

_source line 59_

<details open><summary>🔧 Tool call — Edit · `toolu_01CXgom3vyyiaoMybF8yABVX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance",
  "new_string": "excluding episodes below a displacement threshold $\\tau_d$ and credits only active avoidance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "be9e56ea-2c75-4f46-b4cc-c00160cffc73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6SCEbhZM686YGZDNgUNpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 55719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1390
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

_source line 60 · 2026-05-26T09:33:21.878Z_

<details><summary>↩ Tool result · `toolu_01CXgom3vyyiaoMybF8yABVX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "cdb4e102-0e41-4581-97e0-8a33c225e56b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance",
    "newString": "excluding episodes below a displacement threshold $\\tau_d$ and credits only active avoidance",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.\n\n\\paragraph{Future work.}\nFive directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.\n\n\\paragraph{Broader impact.}\nMetric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\section{Discussion and Conclusion}\\label{sec:conclusion}",
          " ",
          "-This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$, providing a metric that credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).",
          "+This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$ and credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Limitations.}",
          " The empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Edit · `toolu_01MfeWwJXJ85mqzmdSdvm45a`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "end-effector displacement (0.29\\,m), indicating that the robot moves but collides",
  "new_string": "end-effector displacement (0.29\\,m): the robot moves but collides"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "dac9d95c-4f85-4889-aa65-b052ac093bf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6SCEbhZM686YGZDNgUNpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 55719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1390
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

_source line 62 · 2026-05-26T09:33:23.392Z_

<details><summary>↩ Tool result · `toolu_01MfeWwJXJ85mqzmdSdvm45a`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "668dcce1-145d-47b8-bcba-ec96fe8e9773",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "end-effector displacement (0.29\\,m), indicating that the robot moves but collides",
    "newString": "end-effector displacement (0.29\\,m): the robot moves but collides",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$ and credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.\n\n\\paragraph{Future work.}\nFive directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.\n\n\\paragraph{Broader impact.}\nMetric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$ and credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Limitations.}",
          "-The empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m), indicating that the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.",
          "+The empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m): the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.",
          " ",
          " \\paragraph{Future work.}",
          " Five directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Edit · `toolu_01XaEfTup37mALFLVKhfnRP6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "(minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.",
  "new_string": "(minimum displacement 288\\,mm), and its fake safe rate is 0\\%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "ea100962-709e-4e65-acfc-7cf2d32a083a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6SCEbhZM686YGZDNgUNpD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 55719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1390
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

_source line 64 · 2026-05-26T09:33:24.336Z_

<details><summary>↩ Tool result · `toolu_01XaEfTup37mALFLVKhfnRP6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "8707025b-b908-4eac-9bf1-bf78186e1b37",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "(minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.",
    "newString": "(minimum displacement 288\\,mm), and its fake safe rate is 0\\%.",
    "originalFile": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%; catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate). Their collision avoidance reflects genuine trajectory modification, not inaction.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%); the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 7,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " ",
          " Several recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.",
          " ",
          "-For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\\,mm), yielding a fake safe rate of 0\\%.",
          "+For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: all of its safe episodes involve genuine end-effector motion (minimum displacement 288\\,mm), and its fake safe rate is 0\\%.",
          " ",
          " We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
All edits done. Let me now compile a summary of changes for each file.

Let me also note the Claim 3 data in discussion.tex that I'm flagging but not modifying.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "52b02f6d-79f2-44fe-8432-7f20f1e91580",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZUQzx9fqfSoxsh1qVyN76",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1753,
      "cache_read_input_tokens": 57109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1753
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

_source line 66_

All edits applied. Here's the summary:

---

## 修改总览

### abstract.tex (1 edit)
- **移除 em-dash**: `safety---all` → `safety; all` — em-dash 是 AI 写作最显著标志，改为分号

### analysis_claim1.tex (4 edits)
- **移除 -ing 结尾**: `confirming that the model produces...` → `and the model produces...`
- **移除 -ing 结尾**: `yielding a fake safe rate of 0%` → `; the fake safe rate is 0%`
- **更直接的动词**: `is intended as` → `serves as` — 去掉被动 hedging
- **收紧长句**: displacement distribution 句移除嵌套从句 `shown in...` 改为括号引用，删去冗余修饰词

### analysis_claim2.tex (3 edits)
- **移除 -ing 结尾**: `providing the refinement module with...` → `and provides the refinement module with...`
- **移除 -ing 结尾**: `resulting in zero refinement steps` → `; no refinement steps occur`
- **移除 -ing 结尾**: `effectively reducing the model to...` → 断句重写为 `The model thus operates as...`

### discussion.tex (3 edits)
- **移除 em-dash**: `---dominated by full-body collisions---` → 逗号包夹
- **移除 -ing 结尾**: `providing a metric that credits...` → `and credits...`
- **移除 -ing 结尾**: `indicating that the robot moves...` → 冒号引导解释

### introduction.tex (4 edits)
- **移除 -ing 结尾**: `indicating that catastrophic...` → 分号连接独立子句
- **移除 -ing 结尾**: `confirming that their collision avoidance...` → 断句为独立句
- **移除 -ing 结尾**: `establishing that the avoidance signal...` → 分号连接
- **移除 -ing 结尾**: `yielding a fake safe rate of 0%` → `and its fake safe rate is 0%`

---

## Claim 3 数据标记（discussion.tex，未修改）

Discussion 中以下两处包含 Claim 3 具体数据，re-eval 后可能需要更新：

1. **Line 3**: `Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region...` — 含 Claim 3 结论（non-zero CAR_f, zero frozen rate, catastrophic TSR collapse）
2. **Line 6**: `All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7% baseline to <7%)` — 含 Claim 3 具体数字（74.7% → <7%）

---

## 未修改的文件

**analysis_claim3.tex** — 按要求严格未触碰。

## 总体评价

五个文件的论证逻辑、数据一致性（Table 与正文对照）、Pi0.5 definitive 描述均无问题。主要修改集中在消除 AI 写作痕迹（15 处 em-dash + -ing 结尾修复），未改动任何数据或结论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "uuid": "f25534b5-b4b5-4728-a658-7034c8616fc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZUQzx9fqfSoxsh1qVyN76",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1753,
      "cache_read_input_tokens": 57109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1753
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

### Task result

_source line 67_

All edits applied. Here's the summary:

---

## 修改总览

### abstract.tex (1 edit)
- **移除 em-dash**: `safety---all` → `safety; all` — em-dash 是 AI 写作最显著标志，改为分号

### analysis_claim1.tex (4 edits)
- **移除 -ing 结尾**: `confirming that the model produces...` → `and the model produces...`
- **移除 -ing 结尾**: `yielding a fake safe rate of 0%` → `; the fake safe rate is 0%`
- **更直接的动词**: `is intended as` → `serves as` — 去掉被动 hedging
- **收紧长句**: displacement distribution 句移除嵌套从句 `shown in...` 改为括号引用，删去冗余修饰词

### analysis_claim2.tex (3 edits)
- **移除 -ing 结尾**: `providing the refinement module with...` → `and provides the refinement module with...`
- **移除 -ing 结尾**: `resulting in zero refinement steps` → `; no refinement steps occur`
- **移除 -ing 结尾**: `effectively reducing the model to...` → 断句重写为 `The model thus operates as...`

### discussion.tex (3 edits)
- **移除 em-dash**: `---dominated by full-body collisions---` → 逗号包夹
- **移除 -ing 结尾**: `providing a metric that credits...` → `and credits...`
- **移除 -ing 结尾**: `indicating that the robot moves...` → 冒号引导解释

### introduction.tex (4 edits)
- **移除 -ing 结尾**: `indicating that catastrophic...` → 分号连接独立子句
- **移除 -ing 结尾**: `confirming that their collision avoidance...` → 断句为独立句
- **移除 -ing 结尾**: `establishing that the avoidance signal...` → 分号连接
- **移除 -ing 结尾**: `yielding a fake safe rate of 0%` → `and its fake safe rate is 0%`

---

## Claim 3 数据标记（discussion.tex，未修改）

Discussion 中以下两处包含 Claim 3 具体数据，re-eval 后可能需要更新：

1. **Line 3**: `Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region...` — 含 Claim 3 结论（non-zero CAR_f, zero frozen rate, catastrophic TSR collapse）
2. **Line 6**: `All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7% baseline to <7%)` — 含 Claim 3 具体数字（74.7% → <7%）

---

## 未修改的文件

**analysis_claim3.tex** — 按要求严格未触碰。

## 总体评价

五个文件的论证逻辑、数据一致性（Table 与正文对照）、Pi0.5 definitive 描述均无问题。主要修改集中在消除 AI 写作痕迹（15 处 em-dash + -ing 结尾修复），未改动任何数据或结论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 326182,
  "duration_api_ms": 327518,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "798082f9-eb73-4468-93f5-44c8208a7401",
  "total_cost_usd": 1.0844897500000001,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 73723,
    "cache_read_input_tokens": 269452,
    "output_tokens": 19478,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 73723,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 965,
        "cache_read_input_tokens": 57109,
        "cache_creation_input_tokens": 1753,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1753
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1905,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002005,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 19478,
      "cacheReadInputTokens": 269452,
      "cacheCreationInputTokens": 73723,
      "webSearchRequests": 0,
      "costUSD": 1.08248475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "478fadee-4781-4187-a295-5d8afd717c85"
}
```

</details>

---
