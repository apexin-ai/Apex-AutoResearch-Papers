# paper appendix cheetah table

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_paper_appendix_cheetah_table_20260525T155300.log`
- **Structured JSON:** [`508d317cc718ffd19be5.json`](../../sessions/50/508d317cc718ffd19be5.json)

## Before a recorded user message

48 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "6b496283-c8dd-48ed-b575-974164d250c0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779734400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8adcb041-5d86-48db-9114-91dce02b05f7",
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2"
}
```

---

### Assistant

_source line 4_

Let me start by reading the paper-writing-norms skill and finding the appendix file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "eee4d6d2-509c-4679-8686-d3bd22abb79c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01858AdHdw2MjuGS8PetMvrt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11659,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11659
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

<details open><summary>🔧 Tool call — Read · `toolu_01Dd1TkbE6vQ5MkmuR5LnpSr`</summary>

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
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "5840c931-bed3-47a7-b9bd-83af357c9093",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01858AdHdw2MjuGS8PetMvrt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11659,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11659
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

_source line 6 · 2026-05-25T15:53:13.125Z_

<details><summary>↩ Tool result · `toolu_01Dd1TkbE6vQ5MkmuR5LnpSr`</summary>

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
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "5d23d528-493d-4e51-b5b7-fbf41d9c5358",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01B2iok6KZXHv8Gzyyr2gNCd`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "8ae7a035-5854-4ffe-829f-b2b29d5a6265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01858AdHdw2MjuGS8PetMvrt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11659,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11659
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

_source line 8 · 2026-05-25T15:53:13.450Z_

<details><summary>↩ Tool result · `toolu_01B2iok6KZXHv8Gzyyr2gNCd`</summary>

```text
paper/tables/nve_sensitivity_table.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "688af4c8-907a-411c-8c13-24a226a0c039",
  "tool_use_result": {
    "filenames": [
      "paper/tables/nve_sensitivity_table.tex"
    ],
    "durationMs": 14,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Only one tex file found. Let me search more broadly for appendix files and other tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "4aae60d2-537a-4587-94eb-f2a8b515e7b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEvC4PSPN2bBvYCazUqCAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5741,
      "cache_read_input_tokens": 23500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5741
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

_source line 10_

Only found one tex file. Let me search more broadly for all paper files and appendix content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "33efcd40-e1e5-41e0-b453-8814b81e0480",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEvC4PSPN2bBvYCazUqCAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5741,
      "cache_read_input_tokens": 23500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5741
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

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_012v5ZPZTEaYKvNbUMq6csKL`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "93ca96c7-bd2e-4b9f-82f7-115483fb8b8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEvC4PSPN2bBvYCazUqCAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5741,
      "cache_read_input_tokens": 23500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5741
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

_source line 12 · 2026-05-25T15:53:19.977Z_

<details><summary>↩ Tool result · `toolu_012v5ZPZTEaYKvNbUMq6csKL`</summary>

```text
paper/framing_b_reaudit.md
paper/sections/related_work.md
paper/sections/sgs_gradient_analysis.md
paper/sections/sgs_informative_negative.md
paper/tables/nve_sensitivity_table.tex
paper/sections/experimental_setup.md
paper/sections/limitations.md
paper/method.md
paper/sections/results.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "3f17af4a-44fb-477d-a2a6-774fe20c36cd",
  "tool_use_result": {
    "filenames": [
      "paper/framing_b_reaudit.md",
      "paper/sections/related_work.md",
      "paper/sections/sgs_gradient_analysis.md",
      "paper/sections/sgs_informative_negative.md",
      "paper/tables/nve_sensitivity_table.tex",
      "paper/sections/experimental_setup.md",
      "paper/sections/limitations.md",
      "paper/method.md",
      "paper/sections/results.md"
    ],
    "durationMs": 7,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_012NXuabpq4hkjgFnedfHc11`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/tables/nve_sensitivity_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "6eb7d930-77c4-47a8-b7e9-a672707e725d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEvC4PSPN2bBvYCazUqCAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5741,
      "cache_read_input_tokens": 23500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5741
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

_source line 14 · 2026-05-25T15:53:20.332Z_

<details><summary>↩ Tool result · `toolu_012NXuabpq4hkjgFnedfHc11`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\caption{NVE threshold sensitivity analysis for CIVO detection (summary). Task~B2 (main text) uses $\nve \geq 1.5\times$ yielding one false positive (008e\_v3\_s2, identified as non-CIVO Imagination-Reality Divergence). Task~B1 (Appendix~\ref{sec:appendix_sensitivity}) restricts the positive class to sustained CIVO ($n_{\text{pos}}=3$), achieving perfect rank separation ($\text{AUROC}=1.000$). All CIs are two-sided Clopper-Pearson exact binomial ($\alpha = 0.05$).}
4	\label{tab:nve_sensitivity}
5	\small
6	\setlength{\tabcolsep}{4pt}
7	\begin{tabular}{@{}lccccccc@{}}
8	\toprule
9	Task & Threshold & $n_{\text{pos}}/n_{\text{neg}}$ & AUROC & Accuracy & 95\% CI & F1 & Note \\
10	\midrule
11	B2 (main) & $\geq 1.5\times$ & 4\,/\,6 & 0.958 & 90.0\% & [55.5, 99.7] & 88.9\% & 1 FP (IRD) \\
12	B1 (app.) & $\geq 3.9\times$ & 3\,/\,7 & 1.000 & 100\% & [69.2, 100] & 100\% & $n_{\text{pos}}\!=\!3$ \\
13	\bottomrule
14	\end{tabular}
15	\end{table}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "cbcafb79-f030-4a41-a264-775ff1081065",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper/tables/nve_sensitivity_table.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\caption{NVE threshold sensitivity analysis for CIVO detection (summary). Task~B2 (main text) uses $\\nve \\geq 1.5\\times$ yielding one false positive (008e\\_v3\\_s2, identified as non-CIVO Imagination-Reality Divergence). Task~B1 (Appendix~\\ref{sec:appendix_sensitivity}) restricts the positive class to sustained CIVO ($n_{\\text{pos}}=3$), achieving perfect rank separation ($\\text{AUROC}=1.000$). All CIs are two-sided Clopper-Pearson exact binomial ($\\alpha = 0.05$).}\n\\label{tab:nve_sensitivity}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}lccccccc@{}}\n\\toprule\nTask & Threshold & $n_{\\text{pos}}/n_{\\text{neg}}$ & AUROC & Accuracy & 95\\% CI & F1 & Note \\\\\n\\midrule\nB2 (main) & $\\geq 1.5\\times$ & 4\\,/\\,6 & 0.958 & 90.0\\% & [55.5, 99.7] & 88.9\\% & 1 FP (IRD) \\\\\nB1 (app.) & $\\geq 3.9\\times$ & 3\\,/\\,7 & 1.000 & 100\\% & [69.2, 100] & 100\\% & $n_{\\text{pos}}\\!=\\!3$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
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

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
This table is about NVE sensitivity, not an experiment summary table. Let me look at the other files to find the appendix content with an experiment summary table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "27677e30-fc9e-488c-b875-2fe0f4766868",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X69MrxpsDdDZkRwFyxKUWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 29241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 854
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

_source line 16_

Let me search for the experiment summary table across all project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "49611323-ee10-4b0e-91c4-e4d4966b422b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X69MrxpsDdDZkRwFyxKUWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 29241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 854
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

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01N8V6auytDwuNqvF2QEbTgE`</summary>

```json
{
  "pattern": "exp_0[0-9][0-9]|experiment.*summary|实验汇总|Walker|Cheetah|baseline.*s0",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper",
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
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "f0073cb2-fac1-4076-8a9d-77feccba4b42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X69MrxpsDdDZkRwFyxKUWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 29241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 854
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

_source line 18 · 2026-05-25T15:53:26.244Z_

<details><summary>↩ Tool result · `toolu_01N8V6auytDwuNqvF2QEbTgE`</summary>

```text
paper/method.md:10:[Omitted long matching line]
paper/method.md:78:[Omitted long matching line]
paper/method.md:80:[Omitted long matching line]
paper/method.md:111:[Omitted long matching line]
paper/method.md:177:**Configuration.** Exp\_016e replicates exp\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\Delta t}$, subsampling ON, $H{=}8$, $\Delta t{=}2$ imagination) with one modification: \texttt{reward\_dt\_emb\_detach=True}, which applies $\text{sg}(\cdot)$ to $e_{\Delta t}$ before the reward head during the backward pass.
paper/sections/sgs_informative_negative.md:23:The experiment uses the same configuration as exp\_008d (the primary CIVO-exhibiting condition): Walker Walk, trained $e_{\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\Delta t{=}2$ imagination, seed 1. The only modification is \texttt{reward\_dt\_emb\_detach=True}.
paper/sections/sgs_informative_negative.md:81:\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\_021)}
paper/sections/sgs_informative_negative.md:84:[Omitted long matching line]
paper/sections/results.md:9:We organize findings around five diagnostic questions, followed by a gradient decomposition analysis and a taxonomy of failure modes. All quantitative claims cite experiment identifiers for traceability; evaluation returns are means over 10 episodes at each checkpoint. Primary experiments use Walker Walk from the DeepMind Control Suite; cross-environment validation on Cheetah Run is reported in Section~\ref{sec:cross_env} (see Section~\ref{sec:environment} for environment details).
paper/sections/results.md:20:  % PLACEHOLDER: Learning curves for exp_001, 005, 006, 007
paper/sections/results.md:34:No $\Delta t{>}1$ configuration achieves sustained performance above 60\% of the baseline beyond 65K steps. The degradation patterns vary---inverted-V collapse (exp\_006), monotonic decline (exp\_005), and severe suppression (exp\_007)---but the qualitative conclusion is uniform: variable-rate imagination degrades performance on Walker Walk across all tested configurations.
paper/sections/results.md:254:\subsection{Cross-Environment Validation: Cheetah Run}
paper/sections/results.md:257:[Omitted long matching line]
paper/sections/results.md:259:Aggregating across both locomotion environments, 10/10 trained-$e_{\Delta t}$ runs (8 Walker, 2 Cheetah) exhibit CIVO onset, while none of the 8 control conditions (removed or unexposed embedding) exhibit pathological overestimation (Fisher exact test, $p < 0.0001$). The onset mechanism is deterministic given a trained temporal embedding; the downstream outcome (sustained collapse vs.\ self-correction) is stochastic.
paper/sections/experimental_setup.md:37:\paragraph{Primary environment.} \textbf{Walker Walk}: a planar bipedal locomotion task with 24-dimensional proprioceptive observations (14 orientations, 1 height, 9 velocities) and 6-dimensional continuous actions. This task requires sustained coordination and provides a challenging testbed for diagnosing value overestimation, as the reward signal is dense and performance differences are clearly distinguishable.
paper/sections/experimental_setup.md:39:\paragraph{Cross-environment validation.} We include \textbf{Cheetah Run} (17D observations, 6D actions) to test whether the identified mechanisms generalize beyond Walker Walk. The Cheetah baseline (exp\_077) converges to 448.1; treatment conditions (exp\_010b, exp\_078) replicate the trained-$e_{\Delta t}$ configuration from Walker.
paper/sections/experimental_setup.md:101:[Omitted long matching line]
paper/sections/experimental_setup.md:123:\paragraph{Diagnostic marker.} We calibrate a diagnostic threshold from our experimental conditions. We emphasize that this threshold serves as an empirical \textit{marker} for identifying pathological overestimation, not as a hypothesis test---it is derived from and evaluated on the same Walker experiments, with Cheetah Run providing independent cross-environment validation (see Section~\ref{sec:cross_env}):
paper/sections/limitations.md:11:[Omitted long matching line]
paper/sections/limitations.md:14:[Omitted long matching line]
paper/sections/limitations.md:20:[Omitted long matching line]
paper/sections/sgs_gradient_analysis.md:18:[Omitted long matching line]
paper/framing_b_reaudit.md:20:- Scope: DreamerV3 + Walker Walk (+ Cheetah pending)
paper/framing_b_reaudit.md:169:- Lines 35-41: mentions Cheetah Run and Cartpole Swingup with footnote "in progress"
paper/framing_b_reaudit.md:170:- 010a Cheetah baseline is now RUNNING (ROADMAP)
paper/framing_b_reaudit.md:171:- **Action:** Keep footnote but update wording if 010a completes before submission. Remove Cartpole Swingup if it won't be run (focus resources on Cheetah).
paper/framing_b_reaudit.md:312:1. Single primary environment (Walker Walk) — Cheetah pending (010a)
paper/framing_b_reaudit.md:318:7. Full-SGS (018) and Cheetah cross-env results pending at submission
paper/framing_b_reaudit.md:360:**Affected files:** Not yet in any written section (016e hasn't been written up yet), but MUST be checked in any future draft. The paper_framing.md exp_016e entry is already updated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "89acbc5c-af34-435e-b1aa-362eb671c902",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/method.md:10:[Omitted long matching line]\npaper/method.md:78:[Omitted long matching line]\npaper/method.md:80:[Omitted long matching line]\npaper/method.md:111:[Omitted long matching line]\npaper/method.md:177:**Configuration.** Exp\\_016e replicates exp\\_008d's CIVO-exhibiting setup (Walker Walk, trained $e_{\\Delta t}$, subsampling ON, $H{=}8$, $\\Delta t{=}2$ imagination) with one modification: \\texttt{reward\\_dt\\_emb\\_detach=True}, which applies $\\text{sg}(\\cdot)$ to $e_{\\Delta t}$ before the reward head during the backward pass.\npaper/sections/sgs_informative_negative.md:23:The experiment uses the same configuration as exp\\_008d (the primary CIVO-exhibiting condition): Walker Walk, trained $e_{\\Delta t}$ ($d{=}32$), subsampling enabled, $H{=}8$, $\\Delta t{=}2$ imagination, seed 1. The only modification is \\texttt{reward\\_dt\\_emb\\_detach=True}.\npaper/sections/sgs_informative_negative.md:81:\\subsubsection{Cross-Environment Validation: Full-SGS on Cheetah Run (exp\\_021)}\npaper/sections/sgs_informative_negative.md:84:[Omitted long matching line]\npaper/sections/results.md:9:We organize findings around five diagnostic questions, followed by a gradient decomposition analysis and a taxonomy of failure modes. All quantitative claims cite experiment identifiers for traceability; evaluation returns are means over 10 episodes at each checkpoint. Primary experiments use Walker Walk from the DeepMind Control Suite; cross-environment validation on Cheetah Run is reported in Section~\\ref{sec:cross_env} (see Section~\\ref{sec:environment} for environment details).\npaper/sections/results.md:20:  % PLACEHOLDER: Learning curves for exp_001, 005, 006, 007\npaper/sections/results.md:34:No $\\Delta t{>}1$ configuration achieves sustained performance above 60\\% of the baseline beyond 65K steps. The degradation patterns vary---inverted-V collapse (exp\\_006), monotonic decline (exp\\_005), and severe suppression (exp\\_007)---but the qualitative conclusion is uniform: variable-rate imagination degrades performance on Walker Walk across all tested configurations.\npaper/sections/results.md:254:\\subsection{Cross-Environment Validation: Cheetah Run}\npaper/sections/results.md:257:[Omitted long matching line]\npaper/sections/results.md:259:Aggregating across both locomotion environments, 10/10 trained-$e_{\\Delta t}$ runs (8 Walker, 2 Cheetah) exhibit CIVO onset, while none of the 8 control conditions (removed or unexposed embedding) exhibit pathological overestimation (Fisher exact test, $p < 0.0001$). The onset mechanism is deterministic given a trained temporal embedding; the downstream outcome (sustained collapse vs.\\ self-correction) is stochastic.\npaper/sections/experimental_setup.md:37:\\paragraph{Primary environment.} \\textbf{Walker Walk}: a planar bipedal locomotion task with 24-dimensional proprioceptive observations (14 orientations, 1 height, 9 velocities) and 6-dimensional continuous actions. This task requires sustained coordination and provides a challenging testbed for diagnosing value overestimation, as the reward signal is dense and performance differences are clearly distinguishable.\npaper/sections/experimental_setup.md:39:\\paragraph{Cross-environment validation.} We include \\textbf{Cheetah Run} (17D observations, 6D actions) to test whether the identified mechanisms generalize beyond Walker Walk. The Cheetah baseline (exp\\_077) converges to 448.1; treatment conditions (exp\\_010b, exp\\_078) replicate the trained-$e_{\\Delta t}$ configuration from Walker.\npaper/sections/experimental_setup.md:101:[Omitted long matching line]\npaper/sections/experimental_setup.md:123:\\paragraph{Diagnostic marker.} We calibrate a diagnostic threshold from our experimental conditions. We emphasize that this threshold serves as an empirical \\textit{marker} for identifying pathological overestimation, not as a hypothesis test---it is derived from and evaluated on the same Walker experiments, with Cheetah Run providing independent cross-environment validation (see Section~\\ref{sec:cross_env}):\npaper/sections/limitations.md:11:[Omitted long matching line]\npaper/sections/limitations.md:14:[Omitted long matching line]\npaper/sections/limitations.md:20:[Omitted long matching line]\npaper/sections/sgs_gradient_analysis.md:18:[Omitted long matching line]\npaper/framing_b_reaudit.md:20:- Scope: DreamerV3 + Walker Walk (+ Cheetah pending)\npaper/framing_b_reaudit.md:169:- Lines 35-41: mentions Cheetah Run and Cartpole Swingup with footnote \"in progress\"\npaper/framing_b_reaudit.md:170:- 010a Cheetah baseline is now RUNNING (ROADMAP)\npaper/framing_b_reaudit.md:171:- **Action:** Keep footnote but update wording if 010a completes before submission. Remove Cartpole Swingup if it won't be run (focus resources on Cheetah).\npaper/framing_b_reaudit.md:312:1. Single primary environment (Walker Walk) — Cheetah pending (010a)\npaper/framing_b_reaudit.md:318:7. Full-SGS (018) and Cheetah cross-env results pending at submission\npaper/framing_b_reaudit.md:360:**Affected files:** Not yet in any written section (016e hasn't been written up yet), but MUST be checked in any future draft. The paper_framing.md exp_016e entry is already updated.",
    "numLines": 29
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_015nz9378WJfdtCwpNdYjQCk`</summary>

```json
{
  "pattern": "exp_0[0-9][0-9]|experiment.*summary|汇总表|appendix|Appendix",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "output_mode": "files_with_matches",
  "glob": "*.{md,tex,txt}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "11968809-e36b-4505-b74a-8c5a8fa2fc5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X69MrxpsDdDZkRwFyxKUWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 29241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 854
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

_source line 20 · 2026-05-25T15:53:27.955Z_

<details><summary>↩ Tool result · `toolu_015nz9378WJfdtCwpNdYjQCk`</summary>

```text
Found 250 files limit: 250
.claude/sessions/director_e639d768/AGENTS.md
.claude/sessions/director_e639d768/CLAUDE.md
artifacts/exp_080_008e_v3_walker_s1/report/analysis_exp_080_ac9ea8.md
artifacts/exp_080_008e_v3_walker_s1/report/analysis_exp_080.md
report.md
.claude/sessions/reviewer_9760d156/AGENTS.md
.claude/sessions/reviewer_9760d156/CLAUDE.md
artifacts/exp_081_008e_v3_walker_s2/report/analysis_exp_081_adbbe9.md
artifacts/exp_081_008e_v3_walker_s2/report/analysis_exp_081.md
artifacts/_project/report/rebuttal_prep.md
artifacts/rebuttal_prep.md
paper/sections/results.md
paper/method.md
docs/paper/rebuttal_notes.md
artifacts/_project/report/rebuttal_draft.md
artifacts/rebuttal_draft.md
ROADMAP.md
memory.md
artifacts/exp_078_cheetah_008d_s0/report/analysis_exp_078.md
artifacts/progress_check_20260525.md
task_context/agent.md
task_context/director.md
docs/paper/sections/appendix.tex
artifacts/_project/report/loco_cv_results.md
artifacts/plan_034_nve_threshold/loco_cv_results.md
.claude/sessions/paper_agent_3ca34d79/AGENTS.md
.claude/sessions/paper_agent_3ca34d79/CLAUDE.md
docs/paper/sections/analysis.tex
docs/paper/sections/results.tex
docs/paper/sections/methodology.tex
docs/paper/sections/introduction.tex
artifacts/_project/report/analysis_411154.md
artifacts/_project/report/analysis.md
artifacts/plan_034_nve_threshold/analysis.md
artifacts/plan_033/report/analysis_report.md
artifacts/plan_033_dt_emb_cosine/analysis_report.md
artifacts/plan_031_actor_entropy/analysis_report.md
artifacts/_project/report/analysis_report.md
artifacts/exp_071_008f_walker_s3/report/analysis_65012a.md
artifacts/exp_071_008f_walker_s3/report/analysis.md
artifacts/exp_072_008e_v3_walker_s5/report/exp_072_008e_v3_walker_s5_analysis.md
artifacts/exp_073_008f_walker_s4/report/analysis_report_a2a779.md
artifacts/exp_073_008f_walker_s4/report/analysis_report.md
artifacts/exp_070_008e_v3_walker_s0/report/analysis_report_eb35d1.md
artifacts/exp_070_008e_v3_walker_s0/report/analysis_report.md
paper_framing.md
artifacts/exp_069_008f_walker_repro_s1/analysis_report.md
artifacts/exp_069_008f_walker_repro_s1/report/analysis_report.md
artifacts/exp_067_frozen_dt_emb_walker_plan015/analysis.md
artifacts/exp_067_frozen_dt_emb_walker_plan015/report/analysis.md
docs/paper/main.tex
task_context/reviewer.md
task_context/history/director/loop_11.md
artifacts/exp_061_cartpole_civo_trigger/report/exp_061_cartpole_civo_analysis.md
artifacts/exp_008d_subsample_on_h8/report/exp_008d_sparse_rssm_fidelity_report.md
artifacts/exp_066_timeseries_rssm_fidelity/chart/exp_066_causal_chart_location.txt
artifacts/exp_066_timeseries_rssm_fidelity/data/exp_066_analysis_summary.md
artifacts/exp_066_timeseries_rssm_fidelity/chart/exp_066_timeseries_fidelity_causal_location.txt
artifacts/exp_066_timeseries_rssm_fidelity/data/exp_066_timeseries_results.md
artifacts/exp_066/data/exp_066_timeseries_fidelity.txt
artifacts/_project/report/supplementary_framework.md
artifacts/supplementary_framework.md
artifacts/_project/paper/ablation_mechanism_table.tex
artifacts/tables/ablation_mechanism_table.tex
artifacts/exp_065_dt_emb_cosine/data/cosine_similarity_results.txt
artifacts/exp_065/data/results_summary.txt
artifacts/exp_064_value_distribution/chart/value_bias_vs_timestep_location.txt
artifacts/exp_064_value_distribution/data/results_summary.txt
artifacts/exp_064_value_distribution/chart/value_ratio_histogram_location.txt
artifacts/exp_064_value_distribution/chart/value_distribution_location.txt
artifacts/_project/report/negative_results_insights.md
artifacts/negative_results_insights.md
artifacts/_project/report/actor_entropy_analysis.md
artifacts/actor_entropy_analysis.md
artifacts/_project/report/value_distribution_analysis_719010.md
artifacts/_project/report/value_distribution_analysis.md
artifacts/value_distribution_analysis.md
artifacts/review_reports/round_5.md
.claude/sessions/review_reviewer_1_3ba83a7f/AGENTS.md
.claude/sessions/review_reviewer_1_3ba83a7f/CLAUDE.md
.claude/sessions/review_reviewer_2_393bd6df/AGENTS.md
.claude/sessions/review_reviewer_2_393bd6df/CLAUDE.md
artifacts/_project/report/rssm_fidelity_analysis_4f6575.md
artifacts/_project/report/rssm_fidelity_analysis.md
artifacts/rssm_fidelity_analysis.md
artifacts/_project/report/negative_results_taxonomy_075c1f.md
artifacts/_project/report/negative_results_taxonomy.md
artifacts/negative_results_taxonomy.md
artifacts/_project/report/camera_ready_checklist.md
artifacts/camera_ready_checklist.md
artifacts/supplement_completeness_results.md
artifacts/icml_compliance_results.md
artifacts/_project/data/nve_threshold_sensitivity.md
artifacts/_project/report/nve_threshold_sensitivity.md
artifacts/nve_threshold_sensitivity.md
artifacts/review_reports/round_4.md
artifacts/review_reports/round_3.md
task_context/history/reviewer/loop_22.md
task_context/history/director/loop_10.md
artifacts/exp_047_diagnosis.md
task_context/history/reviewer/loop_21.md
artifacts/_project/data/three_way_dt_emb_comparison.md
artifacts/three_way_dt_emb_comparison.md
artifacts/_project/report/nve_loeo_crossval_report.md
artifacts/nve_loeo_crossval_report.md
artifacts/_project/report/auroc_label_fix_report.md
artifacts/auroc_label_fix_report.md
scenario_patches.md
artifacts/exp_036_dual_critic_pickcube/report/exp_036_analysis_2e1055.md
artifacts/exp_036_dual_critic_pickcube/report/exp_036_analysis.md
task_context/history/agent/loop_22_1779719462.md
task_context/history/agent/loop_22_1779392523.md
task_context/history/reviewer/loop_20.md
task_context/history/agent/loop_22_1779392513.md
artifacts/_project/report/check_037_038_status.md
artifacts/check_037_038_status.md
artifacts/exp_035_narrow_dual_critic_walker/report/report_exp_035_analysis.md
artifacts/exp_035/report/report_exp_035_analysis.md
task_context/history/agent/loop_22_1779392466.md
artifacts/literature/dual_critic_cross_env_literature.md
artifacts/exp_034/report/report_exp_034_analysis.md
artifacts/gpu_deployment_plan_20260521.md
task_context/history/agent/loop_22_1779379926.md
task_context/history/agent/loop_22_1779365518.md
artifacts/exp_034_dual_critic_cheetah/report/exp_034_analysis.md
artifacts/exp_033_wide_critic_walker/report/report_exp_033_analysis_88d14a.md
artifacts/exp_033_wide_critic_walker/report/report_exp_033_analysis.md
artifacts/exp_031b_tcn_pickcube_s0_sigma05/report/report_exp_031b_analysis_d49d47.md
artifacts/exp_031b_tcn_pickcube_s0_sigma05/report/report_exp_031b_analysis.md
artifacts/exp_032_dual_critic_walker/report/report_exp_032_analysis_afe1ca.md
artifacts/exp_032_dual_critic_walker/report/report_exp_032_analysis.md
task_context/history/agent/loop_22.md
artifacts/exp_032b_dual_critic_walker_s1/report/report_exp_032b_analysis.md
task_context/history/reviewer/loop_19.md
artifacts/dream_reports/dream_20260520T210241/best/review_report.md
artifacts/dream_reports/dream_20260520T210241/median/paper_framing.md
artifacts/dream_reports/dream_20260520T210241/best/paper_framing.md
artifacts/dream_reports/dream_20260520T155150/worst/review_report.md
artifacts/dream_reports/dream_20260520T155150/median/review_report.md
artifacts/dream_reports/dream_20260520T155150/worst/paper.tex
artifacts/dream_reports/dream_20260520T155150/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T155150/median/paper.tex
artifacts/dream_reports/dream_20260520T155150/median/paper_framing.md
artifacts/dream_reports/dream_20260520T155150/best/paper_framing.md
artifacts/code/ablation_commands.md
artifacts/exp_027_tcn_walker_s0/report/exp_027_tcn_walker_s0_analysis.md
artifacts/exp_027_tcn_walker_s0_analysis.md
paper/tables/nve_sensitivity_table.tex
task_context/history/reviewer/loop_18.md
task_context/history/agent/loop_21_1779342825.md
task_context/history/agent/loop_21_1779069624.md
task_context/history/agent/loop_21.md
task_context/history/agent/loop_20_1779061228.md
artifacts/analysis/cheetah_integration_template.md
artifacts/exp_024b_cheetah_no_dt_emb_s0/intermediate/cheetah_integration_template.md
artifacts/exp_021_full_sgs_cheetah_s1/report/analysis_24b7c0.md
artifacts/exp_021_full_sgs_cheetah_s1/report/analysis.md
task_context/history/reviewer/loop_17.md
task_context/history/agent/loop_20_1779059871.md
artifacts/exp_023a_cheetah_baseline_s0/report/analysis.md
artifacts/exp_023b_cheetah_baseline_s1/data/analysis_8e6b81.md
artifacts/exp_023b_cheetah_baseline_s1/data/analysis.md
task_context/history/agent/loop_20.md
task_context/history/reviewer/loop_16.md
artifacts/exp_019b_final_analysis.md
artifacts/_project/report/nve_sensitivity_audit_note.md
artifacts/analysis/nve_sensitivity_audit_note.md
artifacts/_project/report/paper_section_audit.md
artifacts/paper_section_audit.md
task_context/history/agent/loop_19_1779041099.md
task_context/history/agent/loop_19.md
task_context/history/director/loop_9.md
artifacts/exp_019b_pickcube_civo_trigger/data/analysis_civo_detector_pickcube_backtest.md
artifacts/analysis_civo_detector_pickcube_backtest.md
task_context/history/agent/loop_18_1779018287.md
task_context/history/agent/loop_18_1779014423.md
task_context/history/agent/loop_18.md
task_context/history/reviewer/loop_15.md
task_context/history/director/loop_8.md
artifacts/analysis/detector_table.md
artifacts/drafts/c1_reframe_patch.md
artifacts/analysis/negative_experiment_retrospective.md
artifacts/exp_008d_civo_trigger_s3/analysis_report.md
artifacts/exp_008d_civo_trigger_s3/report/analysis_report.md
artifacts/_project/data/bootstrap_ci_summary.md
artifacts/_project/report/table1_integrity_check.md
artifacts/analysis/table1_integrity_check.md
task_context/history/agent/loop_17_1779002531.md
task_context/history/director/loop_7.md
task_context/history/agent/loop_17_1778963270.md
artifacts/_project/paper/results_section_draft.md
artifacts/paper_drafts/results_section_draft.md
artifacts/analysis/exp_020_c6_summary.txt
task_context/history/reviewer/loop_14.md
task_context/history/agent/loop_17.md
artifacts/dream_reports/dream_20260516T172011/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T172011/median/paper_framing.md
artifacts/dream_reports/dream_20260516T172011/best/paper_framing.md
artifacts/exp_018v2_full_sgs_walker_s1/analysis_report.md
artifacts/exp_018v2_full_sgs_walker_s1/report/analysis_report.md
task_context/history/agent/loop_16_1778957208.md
artifacts/_project/paper/method_framingB_reaudit_v2.md
artifacts/_project/paper/results.md
artifacts/_project/paper/claim_audit_report.md
artifacts/_project/report/claim_audit_report.md
task_context/history/agent/loop_16_1778952184.md
artifacts/018v2_server_check.md
task_context/history/agent/loop_16_1778948600.md
artifacts/dream_reports/dream_20260516T133210/best/review_report.md
artifacts/dream_reports/dream_20260516T133210/median/review_report.md
artifacts/dream_reports/dream_20260516T133210/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T133210/median/paper_framing.md
artifacts/dream_reports/dream_20260516T133210/best/paper_framing.md
task_context/history/agent/loop_16.md
task_context/history/director/loop_6.md
artifacts/dream_reports/dream_20260516T115400/best/review_report.md
artifacts/dream_reports/dream_review_r1_methodology/median/review_report.md
artifacts/exp_018_full_sgs_walker_s1/analysis_report.md
artifacts/exp_018_full_sgs_walker_s1/report/analysis_report.md
artifacts/dream_reports/dream_20260516T115400/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T115400/median/paper_framing.md
artifacts/dream_reports/dream_20260516T115400/best/paper_framing.md
artifacts/_project/report/claim_strength_audit.md
artifacts/claim_strength_audit.md
artifacts/_project/report/narrative_audit.md
artifacts/narrative_audit.md
artifacts/019a_dryrun_report.md
artifacts/method_framingB_reaudit_v2.md
task_context/history/agent/loop_15_1778939519.md
task_context/history/agent/loop_15_1778908139.md
artifacts/_project/report/018_analysis_criteria.md
artifacts/018/report/018_analysis_criteria.md
task_context/history/agent/loop_15_1778908111.md
task_context/history/agent/loop_15_1778907009.md
task_context/history/agent/loop_15_1778906990.md
task_context/history/agent/loop_15_1778906741.md
task_context/history/agent/loop_15.md
artifacts/framing_b_reaudit_diff.md
artifacts/_project/report/framing_b_reaudit.md
paper/framing_b_reaudit.md
task_context/history/agent/loop_14_1778900225.md
task_context/history/agent/loop_14_1778895756.md
task_context/history/agent/loop_14_1778895741.md
task_context/history/agent/loop_13_1778895718.md
task_context/history/agent/loop_14_1778895636.md
task_context/history/agent/loop_14_1778895481.md
task_context/history/agent/loop_14_1778895461.md
task_context/history/agent/loop_14.md
task_context/history/agent/loop_13_1778886369.md
artifacts/016e/report/exp_016e_nve_diagnosis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "97d8e417-8e37-4053-a858-2c426e8d9a29",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      ".claude/sessions/director_e639d768/AGENTS.md",
      ".claude/sessions/director_e639d768/CLAUDE.md",
      "artifacts/exp_080_008e_v3_walker_s1/report/analysis_exp_080_ac9ea8.md",
      "artifacts/exp_080_008e_v3_walker_s1/report/analysis_exp_080.md",
      "report.md",
      ".claude/sessions/reviewer_9760d156/AGENTS.md",
      ".claude/sessions/reviewer_9760d156/CLAUDE.md",
      "artifacts/exp_081_008e_v3_walker_s2/report/analysis_exp_081_adbbe9.md",
      "artifacts/exp_081_008e_v3_walker_s2/report/analysis_exp_081.md",
      "artifacts/_project/report/rebuttal_prep.md",
      "artifacts/rebuttal_prep.md",
      "paper/sections/results.md",
      "paper/method.md",
      "docs/paper/rebuttal_notes.md",
      "artifacts/_project/report/rebuttal_draft.md",
      "artifacts/rebuttal_draft.md",
      "ROADMAP.md",
      "memory.md",
      "artifacts/exp_078_cheetah_008d_s0/report/analysis_exp_078.md",
      "artifacts/progress_check_20260525.md",
      "task_context/agent.md",
      "task_context/director.md",
      "docs/paper/sections/appendix.tex",
      "artifacts/_project/report/loco_cv_results.md",
      "artifacts/plan_034_nve_threshold/loco_cv_results.md",
      ".claude/sessions/paper_agent_3ca34d79/AGENTS.md",
      ".claude/sessions/paper_agent_3ca34d79/CLAUDE.md",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/results.tex",
      "docs/paper/sections/methodology.tex",
      "docs/paper/sections/introduction.tex",
      "artifacts/_project/report/analysis_411154.md",
      "artifacts/_project/report/analysis.md",
      "artifacts/plan_034_nve_threshold/analysis.md",
      "artifacts/plan_033/report/analysis_report.md",
      "artifacts/plan_033_dt_emb_cosine/analysis_report.md",
      "artifacts/plan_031_actor_entropy/analysis_report.md",
      "artifacts/_project/report/analysis_report.md",
      "artifacts/exp_071_008f_walker_s3/report/analysis_65012a.md",
      "artifacts/exp_071_008f_walker_s3/report/analysis.md",
      "artifacts/exp_072_008e_v3_walker_s5/report/exp_072_008e_v3_walker_s5_analysis.md",
      "artifacts/exp_073_008f_walker_s4/report/analysis_report_a2a779.md",
      "artifacts/exp_073_008f_walker_s4/report/analysis_report.md",
      "artifacts/exp_070_008e_v3_walker_s0/report/analysis_report_eb35d1.md",
      "artifacts/exp_070_008e_v3_walker_s0/report/analysis_report.md",
      "paper_framing.md",
      "artifacts/exp_069_008f_walker_repro_s1/analysis_report.md",
      "artifacts/exp_069_008f_walker_repro_s1/report/analysis_report.md",
      "artifacts/exp_067_frozen_dt_emb_walker_plan015/analysis.md",
      "artifacts/exp_067_frozen_dt_emb_walker_plan015/report/analysis.md",
      "docs/paper/main.tex",
      "task_context/reviewer.md",
      "task_context/history/director/loop_11.md",
      "artifacts/exp_061_cartpole_civo_trigger/report/exp_061_cartpole_civo_analysis.md",
      "artifacts/exp_008d_subsample_on_h8/report/exp_008d_sparse_rssm_fidelity_report.md",
      "artifacts/exp_066_timeseries_rssm_fidelity/chart/exp_066_causal_chart_location.txt",
      "artifacts/exp_066_timeseries_rssm_fidelity/data/exp_066_analysis_summary.md",
      "artifacts/exp_066_timeseries_rssm_fidelity/chart/exp_066_timeseries_fidelity_causal_location.txt",
      "artifacts/exp_066_timeseries_rssm_fidelity/data/exp_066_timeseries_results.md",
      "artifacts/exp_066/data/exp_066_timeseries_fidelity.txt",
      "artifacts/_project/report/supplementary_framework.md",
      "artifacts/supplementary_framework.md",
      "artifacts/_project/paper/ablation_mechanism_table.tex",
      "artifacts/tables/ablation_mechanism_table.tex",
      "artifacts/exp_065_dt_emb_cosine/data/cosine_similarity_results.txt",
      "artifacts/exp_065/data/results_summary.txt",
      "artifacts/exp_064_value_distribution/chart/value_bias_vs_timestep_location.txt",
      "artifacts/exp_064_value_distribution/data/results_summary.txt",
      "artifacts/exp_064_value_distribution/chart/value_ratio_histogram_location.txt",
      "artifacts/exp_064_value_distribution/chart/value_distribution_location.txt",
      "artifacts/_project/report/negative_results_insights.md",
      "artifacts/negative_results_insights.md",
      "artifacts/_project/report/actor_entropy_analysis.md",
      "artifacts/actor_entropy_analysis.md",
      "artifacts/_project/report/value_distribution_analysis_719010.md",
      "artifacts/_project/report/value_distribution_analysis.md",
      "artifacts/value_distribution_analysis.md",
      "artifacts/review_reports/round_5.md",
      ".claude/sessions/review_reviewer_1_3ba83a7f/AGENTS.md",
      ".claude/sessions/review_reviewer_1_3ba83a7f/CLAUDE.md",
      ".claude/sessions/review_reviewer_2_393bd6df/AGENTS.md",
      ".claude/sessions/review_reviewer_2_393bd6df/CLAUDE.md",
      "artifacts/_project/report/rssm_fidelity_analysis_4f6575.md",
      "artifacts/_project/report/rssm_fidelity_analysis.md",
      "artifacts/rssm_fidelity_analysis.md",
      "artifacts/_project/report/negative_results_taxonomy_075c1f.md",
      "artifacts/_project/report/negative_results_taxonomy.md",
      "artifacts/negative_results_taxonomy.md",
      "artifacts/_project/report/camera_ready_checklist.md",
      "artifacts/camera_ready_checklist.md",
      "artifacts/supplement_completeness_results.md",
      "artifacts/icml_compliance_results.md",
      "artifacts/_project/data/nve_threshold_sensitivity.md",
      "artifacts/_project/report/nve_threshold_sensitivity.md",
      "artifacts/nve_threshold_sensitivity.md",
      "artifacts/review_reports/round_4.md",
      "artifacts/review_reports/round_3.md",
      "task_context/history/reviewer/loop_22.md",
      "task_context/history/director/loop_10.md",
      "artifacts/exp_047_diagnosis.md",
      "task_context/history/reviewer/loop_21.md",
      "artifacts/_project/data/three_way_dt_emb_comparison.md",
      "artifacts/three_way_dt_emb_comparison.md",
      "artifacts/_project/report/nve_loeo_crossval_report.md",
      "artifacts/nve_loeo_crossval_report.md",
      "artifacts/_project/report/auroc_label_fix_report.md",
      "artifacts/auroc_label_fix_report.md",
      "scenario_patches.md",
      "artifacts/exp_036_dual_critic_pickcube/report/exp_036_analysis_2e1055.md",
      "artifacts/exp_036_dual_critic_pickcube/report/exp_036_analysis.md",
      "task_context/history/agent/loop_22_1779719462.md",
      "task_context/history/agent/loop_22_1779392523.md",
      "task_context/history/reviewer/loop_20.md",
      "task_context/history/agent/loop_22_1779392513.md",
      "artifacts/_project/report/check_037_038_status.md",
      "artifacts/check_037_038_status.md",
      "artifacts/exp_035_narrow_dual_critic_walker/report/report_exp_035_analysis.md",
      "artifacts/exp_035/report/report_exp_035_analysis.md",
      "task_context/history/agent/loop_22_1779392466.md",
      "artifacts/literature/dual_critic_cross_env_literature.md",
      "artifacts/exp_034/report/report_exp_034_analysis.md",
      "artifacts/gpu_deployment_plan_20260521.md",
      "task_context/history/agent/loop_22_1779379926.md",
      "task_context/history/agent/loop_22_1779365518.md",
      "artifacts/exp_034_dual_critic_cheetah/report/exp_034_analysis.md",
      "artifacts/exp_033_wide_critic_walker/report/report_exp_033_analysis_88d14a.md",
      "artifacts/exp_033_wide_critic_walker/report/report_exp_033_analysis.md",
      "artifacts/exp_031b_tcn_pickcube_s0_sigma05/report/report_exp_031b_analysis_d49d47.md",
      "artifacts/exp_031b_tcn_pickcube_s0_sigma05/report/report_exp_031b_analysis.md",
      "artifacts/exp_032_dual_critic_walker/report/report_exp_032_analysis_afe1ca.md",
      "artifacts/exp_032_dual_critic_walker/report/report_exp_032_analysis.md",
      "task_context/history/agent/loop_22.md",
      "artifacts/exp_032b_dual_critic_walker_s1/report/report_exp_032b_analysis.md",
      "task_context/history/reviewer/loop_19.md",
      "artifacts/dream_reports/dream_20260520T210241/best/review_report.md",
      "artifacts/dream_reports/dream_20260520T210241/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T210241/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T155150/worst/review_report.md",
      "artifacts/dream_reports/dream_20260520T155150/median/review_report.md",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T155150/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T155150/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260520T155150/best/paper_framing.md",
      "artifacts/code/ablation_commands.md",
      "artifacts/exp_027_tcn_walker_s0/report/exp_027_tcn_walker_s0_analysis.md",
      "artifacts/exp_027_tcn_walker_s0_analysis.md",
      "paper/tables/nve_sensitivity_table.tex",
      "task_context/history/reviewer/loop_18.md",
      "task_context/history/agent/loop_21_1779342825.md",
      "task_context/history/agent/loop_21_1779069624.md",
      "task_context/history/agent/loop_21.md",
      "task_context/history/agent/loop_20_1779061228.md",
      "artifacts/analysis/cheetah_integration_template.md",
      "artifacts/exp_024b_cheetah_no_dt_emb_s0/intermediate/cheetah_integration_template.md",
      "artifacts/exp_021_full_sgs_cheetah_s1/report/analysis_24b7c0.md",
      "artifacts/exp_021_full_sgs_cheetah_s1/report/analysis.md",
      "task_context/history/reviewer/loop_17.md",
      "task_context/history/agent/loop_20_1779059871.md",
      "artifacts/exp_023a_cheetah_baseline_s0/report/analysis.md",
      "artifacts/exp_023b_cheetah_baseline_s1/data/analysis_8e6b81.md",
      "artifacts/exp_023b_cheetah_baseline_s1/data/analysis.md",
      "task_context/history/agent/loop_20.md",
      "task_context/history/reviewer/loop_16.md",
      "artifacts/exp_019b_final_analysis.md",
      "artifacts/_project/report/nve_sensitivity_audit_note.md",
      "artifacts/analysis/nve_sensitivity_audit_note.md",
      "artifacts/_project/report/paper_section_audit.md",
      "artifacts/paper_section_audit.md",
      "task_context/history/agent/loop_19_1779041099.md",
      "task_context/history/agent/loop_19.md",
      "task_context/history/director/loop_9.md",
      "artifacts/exp_019b_pickcube_civo_trigger/data/analysis_civo_detector_pickcube_backtest.md",
      "artifacts/analysis_civo_detector_pickcube_backtest.md",
      "task_context/history/agent/loop_18_1779018287.md",
      "task_context/history/agent/loop_18_1779014423.md",
      "task_context/history/agent/loop_18.md",
      "task_context/history/reviewer/loop_15.md",
      "task_context/history/director/loop_8.md",
      "artifacts/analysis/detector_table.md",
      "artifacts/drafts/c1_reframe_patch.md",
      "artifacts/analysis/negative_experiment_retrospective.md",
      "artifacts/exp_008d_civo_trigger_s3/analysis_report.md",
      "artifacts/exp_008d_civo_trigger_s3/report/analysis_report.md",
      "artifacts/_project/data/bootstrap_ci_summary.md",
      "artifacts/_project/report/table1_integrity_check.md",
      "artifacts/analysis/table1_integrity_check.md",
      "task_context/history/agent/loop_17_1779002531.md",
      "task_context/history/director/loop_7.md",
      "task_context/history/agent/loop_17_1778963270.md",
      "artifacts/_project/paper/results_section_draft.md",
      "artifacts/paper_drafts/results_section_draft.md",
      "artifacts/analysis/exp_020_c6_summary.txt",
      "task_context/history/reviewer/loop_14.md",
      "task_context/history/agent/loop_17.md",
      "artifacts/dream_reports/dream_20260516T172011/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T172011/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T172011/best/paper_framing.md",
      "artifacts/exp_018v2_full_sgs_walker_s1/analysis_report.md",
      "artifacts/exp_018v2_full_sgs_walker_s1/report/analysis_report.md",
      "task_context/history/agent/loop_16_1778957208.md",
      "artifacts/_project/paper/method_framingB_reaudit_v2.md",
      "artifacts/_project/paper/results.md",
      "artifacts/_project/paper/claim_audit_report.md",
      "artifacts/_project/report/claim_audit_report.md",
      "task_context/history/agent/loop_16_1778952184.md",
      "artifacts/018v2_server_check.md",
      "task_context/history/agent/loop_16_1778948600.md",
      "artifacts/dream_reports/dream_20260516T133210/best/review_report.md",
      "artifacts/dream_reports/dream_20260516T133210/median/review_report.md",
      "artifacts/dream_reports/dream_20260516T133210/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T133210/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T133210/best/paper_framing.md",
      "task_context/history/agent/loop_16.md",
      "task_context/history/director/loop_6.md",
      "artifacts/dream_reports/dream_20260516T115400/best/review_report.md",
      "artifacts/dream_reports/dream_review_r1_methodology/median/review_report.md",
      "artifacts/exp_018_full_sgs_walker_s1/analysis_report.md",
      "artifacts/exp_018_full_sgs_walker_s1/report/analysis_report.md",
      "artifacts/dream_reports/dream_20260516T115400/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T115400/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T115400/best/paper_framing.md",
      "artifacts/_project/report/claim_strength_audit.md",
      "artifacts/claim_strength_audit.md",
      "artifacts/_project/report/narrative_audit.md",
      "artifacts/narrative_audit.md",
      "artifacts/019a_dryrun_report.md",
      "artifacts/method_framingB_reaudit_v2.md",
      "task_context/history/agent/loop_15_1778939519.md",
      "task_context/history/agent/loop_15_1778908139.md",
      "artifacts/_project/report/018_analysis_criteria.md",
      "artifacts/018/report/018_analysis_criteria.md",
      "task_context/history/agent/loop_15_1778908111.md",
      "task_context/history/agent/loop_15_1778907009.md",
      "task_context/history/agent/loop_15_1778906990.md",
      "task_context/history/agent/loop_15_1778906741.md",
      "task_context/history/agent/loop_15.md",
      "artifacts/framing_b_reaudit_diff.md",
      "artifacts/_project/report/framing_b_reaudit.md",
      "paper/framing_b_reaudit.md",
      "task_context/history/agent/loop_14_1778900225.md",
      "task_context/history/agent/loop_14_1778895756.md",
      "task_context/history/agent/loop_14_1778895741.md",
      "task_context/history/agent/loop_13_1778895718.md",
      "task_context/history/agent/loop_14_1778895636.md",
      "task_context/history/agent/loop_14_1778895481.md",
      "task_context/history/agent/loop_14_1778895461.md",
      "task_context/history/agent/loop_14.md",
      "task_context/history/agent/loop_13_1778886369.md",
      "artifacts/016e/report/exp_016e_nve_diagnosis.md"
    ],
    "numFiles": 250,
    "appliedLimit": 250
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
I see `docs/paper/sections/appendix.tex` - that's likely the appendix file. Let me also check the main.tex for the full paper structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "24f151a1-8f1e-4115-bd36-a9b2d94a7ad0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRmSBSEnSBB3GpUmo8v81F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6463,
      "cache_read_input_tokens": 30095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6463
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

### Assistant

_source line 22_

Found `docs/paper/sections/appendix.tex`. Let me read it and also check the main paper structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "ad35e745-a44f-4c88-bb03-58efde984557",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRmSBSEnSBB3GpUmo8v81F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6463,
      "cache_read_input_tokens": 30095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6463
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01773PCvibcTrAAsgVVXKf6R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "b6ff1a5e-a907-4346-8e33-8ec4d0db0000",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRmSBSEnSBB3GpUmo8v81F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6463,
      "cache_read_input_tokens": 30095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6463
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

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01HWJNdzSCTcYXHJZBKce5EG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "a75465bf-9c53-4967-b58b-f5a8bf97a87d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRmSBSEnSBB3GpUmo8v81F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6463,
      "cache_read_input_tokens": 30095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6463
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

_source line 25 · 2026-05-25T15:53:35.042Z_

<details><summary>↩ Tool result · `toolu_01HWJNdzSCTcYXHJZBKce5EG`</summary>

```text
1	\documentclass{article}
2	
3	% xcolor with table option must be loaded before icml2026.sty (which loads xcolor internally)
4	\PassOptionsToPackage{table}{xcolor}
5	
6	\usepackage{hyperref}
7	\newcommand{\theHalgorithm}{\arabic{algorithm}}
8	\usepackage{icml2026}
9	
10	\usepackage[utf8]{inputenc}
11	\usepackage[T1]{fontenc}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{graphicx}
16	\graphicspath{{../../artifacts/}}
17	\usepackage{colortbl}
18	\usepackage{caption}
19	\usepackage{subcaption}
20	\usepackage{array}
21	\usepackage{enumitem}
22	\usepackage{wrapfig}
23	\usepackage{algorithm}
24	\usepackage{algorithmic}
25	
26	% Custom commands
27	\newcommand{\dt}{\mathrm{dt}}
28	\newcommand{\nve}{\mathrm{nve}}
29	% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)
30	\newcommand{\sgseval}{448.3}
31	\newcommand{\sgsnve}{1.66}
32	\newcommand{\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}
33	\usepackage{pifont}
34	\newcommand{\cmark}{\ding{51}}
35	\newcommand{\xmark}{\ding{55}}
36	\newcommand{\ie}{\textit{i.e.}}
37	\newcommand{\eg}{\textit{e.g.}}
38	\newcommand{\cf}{\textit{cf.}}
39	\newcommand{\etal}{\textit{et al.}}
40	
41	\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}
42	
43	\begin{document}
44	
45	\twocolumn[
46	  \icmltitle{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\
47	  A Diagnostic Analysis of Variable-Rate DreamerV3}
48	
49	  \begin{icmlauthorlist}
50	    \icmlauthor{Anonymous Authors}{anon}
51	  \end{icmlauthorlist}
52	
53	  \icmlaffiliation{anon}{Anonymous Institution}
54	
55	  \icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}
56	
57	  \icmlkeywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}
58	
59	  \vskip 0.3in
60	]
61	
62	\printAffiliationsAndNotice{}
63	
64	\begin{abstract}
65	\input{sections/abstract_body}
66	\end{abstract}
67	
68	% --- INTRODUCTION ---
69	\input{sections/introduction}
70	
71	% --- RELATED WORK ---
72	\input{sections/related_work}
73	
74	% --- METHODOLOGY ---
75	\input{sections/methodology}
76	
77	% --- RESULTS ---
78	\input{sections/results}
79	
80	% --- ANALYSIS ---
81	\input{sections/analysis}
82	
83	% --- CONCLUSION ---
84	\input{sections/conclusion}
85	
86	\bibliographystyle{icml2026}
87	\bibliography{references}
88	
89	% --- APPENDIX ---
90	\appendix
91	\input{sections/appendix}
92	
93	\end{document}
94	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "a6d2ba5a-2893-4bd6-af4c-7c2774b608a5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n% xcolor with table option must be loaded before icml2026.sty (which loads xcolor internally)\n\\PassOptionsToPackage{table}{xcolor}\n\n\\usepackage{hyperref}\n\\newcommand{\\theHalgorithm}{\\arabic{algorithm}}\n\\usepackage{icml2026}\n\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\graphicspath{{../../artifacts/}}\n\\usepackage{colortbl}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{enumitem}\n\\usepackage{wrapfig}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n% Custom commands\n\\newcommand{\\dt}{\\mathrm{dt}}\n\\newcommand{\\nve}{\\mathrm{nve}}\n% SGS result values (018 seed 1: partial mitigation; seed 2: collapsed — 0/3 CIVO elimination)\n\\newcommand{\\sgseval}{448.3}\n\\newcommand{\\sgsnve}{1.66}\n\\newcommand{\\sgsclaim}{reduced CIVO severity in one of two Walker seeds but eliminated it in neither (0/3 across environments)}\n\\usepackage{pifont}\n\\newcommand{\\cmark}{\\ding{51}}\n\\newcommand{\\xmark}{\\ding{55}}\n\\newcommand{\\ie}{\\textit{i.e.}}\n\\newcommand{\\eg}{\\textit{e.g.}}\n\\newcommand{\\cf}{\\textit{cf.}}\n\\newcommand{\\etal}{\\textit{et al.}}\n\n\\icmltitlerunning{Temporal Abstraction Failure in Imagination-Based RL}\n\n\\begin{document}\n\n\\twocolumn[\n  \\icmltitle{Why Temporal Abstraction Can Fail in Imagination-Based RL:\\\\\n  A Diagnostic Analysis of Variable-Rate DreamerV3}\n\n  \\begin{icmlauthorlist}\n    \\icmlauthor{Anonymous Authors}{anon}\n  \\end{icmlauthorlist}\n\n  \\icmlaffiliation{anon}{Anonymous Institution}\n\n  \\icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}\n\n  \\icmlkeywords{World Models, Temporal Abstraction, Value Overestimation, DreamerV3}\n\n  \\vskip 0.3in\n]\n\n\\printAffiliationsAndNotice{}\n\n\\begin{abstract}\n\\input{sections/abstract_body}\n\\end{abstract}\n\n% --- INTRODUCTION ---\n\\input{sections/introduction}\n\n% --- RELATED WORK ---\n\\input{sections/related_work}\n\n% --- METHODOLOGY ---\n\\input{sections/methodology}\n\n% --- RESULTS ---\n\\input{sections/results}\n\n% --- ANALYSIS ---\n\\input{sections/analysis}\n\n% --- CONCLUSION ---\n\\input{sections/conclusion}\n\n\\bibliographystyle{icml2026}\n\\bibliography{references}\n\n% --- APPENDIX ---\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 94,
      "startLine": 1,
      "totalLines": 94
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T15:53:35.300Z_

<details><summary>↩ Tool result · reported error · `toolu_01773PCvibcTrAAsgVVXKf6R`</summary>

```text
File content (36699 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "020cb1fb-c159-47e9-b423-aff647130443",
  "tool_use_result": "Error: File content (36699 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Assistant

_source line 27_

Let me search for the experiment summary table in the appendix file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "11c2696a-db93-47e4-b051-e37969b74d5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVT3zNVBh8YEYtseiQ43q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1070,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 36558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 419
      },
      "output_tokens": 5,
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

_source line 28_

<details open><summary>🔧 Tool call — Grep · `toolu_01JB2QjShxg4H5YKuJbpLFZ2`</summary>

```json
{
  "pattern": "exp_0[0-9][0-9]|experiment.*catalog|experiment.*summary|tabular|Walker Walk|Cheetah",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "ba17dc72-a789-4401-9cfe-566cd2f89113",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVT3zNVBh8YEYtseiQ43q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1070,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 36558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 419
      },
      "output_tokens": 5,
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

_source line 29 · 2026-05-25T15:53:42.244Z_

<details><summary>↩ Tool result · `toolu_01JB2QjShxg4H5YKuJbpLFZ2`</summary>

```text
14:\begin{tabular}{llcccccl}
63:010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
65:010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\times$ & Full collapse \\
67:021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Transient CIVO (self-corr.) \\
68:024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
69:024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
70:008a\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\times$ & Healthy \\
71:008a\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\times$ & Healthy \\
82:046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\times$ & No CIVO \\
83:058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\times$ & No CIVO \\
90:\end{tabular}
116:\begin{tabular}{llccc}
120:Locomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\times$) \\
121:Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\times$) \\
128:\end{tabular}
131:[Omitted long matching line]
147:\begin{tabular}{@{}lrccc@{}}
163:\end{tabular}
176:\begin{tabular}{@{}lcccccccc@{}}
189:\end{tabular}
198:\begin{tabular}{@{}lcccccccc@{}}
210:\end{tabular}
215:\caption{\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\text{pos}}=9$, $n_{\text{neg}}=8$, $n=17$, $\text{AUROC}=0.972$). Includes Walker Walk (15 configurations) and Cheetah Run (2 configurations).}
219:\begin{tabular}{@{}lcccccccc@{}}
231:\end{tabular}
270:[Omitted long matching line]
279:\caption{Walker Walk baseline seeds at 105K and 505K steps.}
282:\begin{tabular}{lcccc}
291:\end{tabular}
298:\paragraph{Normalization conventions.} Walker NVE is normalized against the single-seed baseline (seed~1, exp\_001, 505K steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).
305:To assess whether $\theta{=}1.5\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}15$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\theta{=}1.5\times$ on the held-out environment.
314:\begin{tabular}{lccccc}
319:Cheetah  & 17 & 5 & $(1.45,\, 1.53]$ & 5/5 (1.000) & 1.000 \\
324:\end{tabular}
327:[Omitted long matching line]
350:\caption{$\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}
353:\begin{tabular}{lccccl}
363:\end{tabular}
369:[Omitted long matching line]
373:\caption{Three-way causal ablation (Walker Walk, seed${=}1$). Only the $\dt$-embedding treatment varies; all other configuration is identical. Trained embedding triggers CIVO; frozen and removed do not.}
376:\begin{tabular}{llccl}
385:\end{tabular}
398:\begin{tabular}{@{}llcccc@{}}
418:\end{tabular}
452:[Omitted long matching line]
459:\begin{tabular}{lcc}
472:\end{tabular}
519:\begin{tabular}{lcccccc}
529:\end{tabular}
549:\begin{tabular}{llrrrrr}
561:\end{tabular}
573:\begin{tabular}{llrrr}
579:010b s0 (trained) & Cheetah & $-0.90$ & $-0.84$ & CIVO \\
582:058 s1 (frozen) & Cheetah & $+0.07$ & $+0.07$ & Healthy \\
584:\end{tabular}
587:[Omitted long matching line]
607:\begin{tabular}{lcccccc}
617:\end{tabular}
631:\begin{tabular}{lrrrr}
639:\end{tabular}

[Showing results with pagination = limit: 60]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "f0453120-44fd-4903-b21e-fa8f02c52c38",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "14:\\begin{tabular}{llcccccl}\n63:010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n65:010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n67:021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n68:024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n69:024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n70:008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n71:008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n82:046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n83:058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n90:\\end{tabular}\n116:\\begin{tabular}{llccc}\n120:Locomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\\n121:Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\n128:\\end{tabular}\n131:[Omitted long matching line]\n147:\\begin{tabular}{@{}lrccc@{}}\n163:\\end{tabular}\n176:\\begin{tabular}{@{}lcccccccc@{}}\n189:\\end{tabular}\n198:\\begin{tabular}{@{}lcccccccc@{}}\n210:\\end{tabular}\n215:\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=9$, $n_{\\text{neg}}=8$, $n=17$, $\\text{AUROC}=0.972$). Includes Walker Walk (15 configurations) and Cheetah Run (2 configurations).}\n219:\\begin{tabular}{@{}lcccccccc@{}}\n231:\\end{tabular}\n270:[Omitted long matching line]\n279:\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n282:\\begin{tabular}{lcccc}\n291:\\end{tabular}\n298:\\paragraph{Normalization conventions.} Walker NVE is normalized against the single-seed baseline (seed~1, exp\\_001, 505K steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n305:To assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}15$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n314:\\begin{tabular}{lccccc}\n319:Cheetah  & 17 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\n324:\\end{tabular}\n327:[Omitted long matching line]\n350:\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n353:\\begin{tabular}{lccccl}\n363:\\end{tabular}\n369:[Omitted long matching line]\n373:\\caption{Three-way causal ablation (Walker Walk, seed${=}1$). Only the $\\dt$-embedding treatment varies; all other configuration is identical. Trained embedding triggers CIVO; frozen and removed do not.}\n376:\\begin{tabular}{llccl}\n385:\\end{tabular}\n398:\\begin{tabular}{@{}llcccc@{}}\n418:\\end{tabular}\n452:[Omitted long matching line]\n459:\\begin{tabular}{lcc}\n472:\\end{tabular}\n519:\\begin{tabular}{lcccccc}\n529:\\end{tabular}\n549:\\begin{tabular}{llrrrrr}\n561:\\end{tabular}\n573:\\begin{tabular}{llrrr}\n579:010b s0 (trained) & Cheetah & $-0.90$ & $-0.84$ & CIVO \\\\\n582:058 s1 (frozen) & Cheetah & $+0.07$ & $+0.07$ & Healthy \\\\\n584:\\end{tabular}\n587:[Omitted long matching line]\n607:\\begin{tabular}{lcccccc}\n617:\\end{tabular}\n631:\\begin{tabular}{lrrrr}\n639:\\end{tabular}",
    "numLines": 60,
    "appliedLimit": 60
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Let me read the experiment catalog table area (around line 14) to understand the exact format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "02edf51d-8546-4f9e-90b4-a47d7d6f56f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtpzdJHxDDYHmD63XES2QL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2845,
      "cache_read_input_tokens": 36977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2845
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

_source line 31_

Let me read the experiment catalog table to understand its format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "5da932a7-5910-4f25-9b35-0a87a6b6356d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtpzdJHxDDYHmD63XES2QL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2845,
      "cache_read_input_tokens": 36977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2845
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

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_0188UzhzAUfYPZjnj4C7rwG3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 1,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "eb06a3ad-f3a8-4e1b-9b80-45fe4c57e0fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtpzdJHxDDYHmD63XES2QL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2845,
      "cache_read_input_tokens": 36977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2845
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

_source line 33 · 2026-05-25T15:53:48.148Z_

<details><summary>↩ Tool result · `toolu_0188UzhzAUfYPZjnj4C7rwG3`</summary>

```text
1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
11	\label{tab:complete_results}
12	\scriptsize
13	\setlength{\tabcolsep}{3pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	001 s2 & Baseline ($\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\
20	\rowcolor{gray!15}
21	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\heartsuit$ & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29	\rowcolor{gray!15}
30	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31	\rowcolor{gray!15}
32	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33	\rowcolor{gray!15}
34	059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\times$ & Collapse$^\dagger$ \\
35	\rowcolor{gray!15}
36	068 & Factorial repro (s1) & trn & ON & 8 & 39.1 @105K & 4.12$\times$ & Full collapse \\
37	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
38	008f s4 & No dt\_emb (s4) & --- & ON & 8 & 289.3 @105K & 0.76$\times$ & Healthy \\
39	009c s3 & No dt\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\times$ & Healthy \\
40	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
41	008a\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\times$ & Healthy \\
42	008a\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\times$ & Healthy \\
43	008a\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy \\
44	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
45	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
46	042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\times$ & Healthy \\
47	047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\times$ & Transient (self-corr.) \\
48	057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\times$ & Transient (self-corr.) \\
49	067 & Frozen emb (s0) & frz$^b$ & ON & 8 & 281.5 @105K & 0.19$\times$ & Healthy \\
50	\midrule
51	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & Partial mitig.\ (CIVO+) \\
52	\rowcolor{gray!15}
53	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
54	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\times$ & Healthy \\
55	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
56	\rowcolor{gray!15}
57	008e\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\times$ & CIVO collapse \\
58	008e\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\times$ & Healthy \\
59	008e\_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.61$\times$ & Healthy \\
60	\midrule
61	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
62	\rowcolor{gray!15}
63	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
64	\rowcolor{gray!15}
65	010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\times$ & Full collapse \\
66	\rowcolor{gray!15}
67	021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Transient CIVO (self-corr.) \\
68	024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
69	024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
70	008a\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\times$ & Healthy \\
71	008a\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\times$ & Healthy \\
72	\rowcolor{gray!15}
73	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
74	054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\times$$^h$ & Env.\ transient (ctrl) \\
75	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^f$ & Env.\ transient \\
76	052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\times$$^f$ & Env.\ transient \\
77	051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\times$$^f$ & Env.\ transient (ctrl) \\
78	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^g$ & Env.\ dynamics \\
79	053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\times$$^g$ & Env.\ dynamics (ctrl) \\
80	055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\times$$^g$ & Env.\ dynamics \\
81	056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\times$$^g$ & Env.\ dynamics (ctrl) \\
82	046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\times$ & No CIVO \\
83	058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\times$ & No CIVO \\
84	\midrule
85	\multicolumn{8}{l}{\textit{Cartpole Swingup}} \\
86	060 & Cartpole baseline (3 seeds) & --- & --- & 15 & 557.0 @105K$^i$ & --- & Healthy \\
87	061 & Cartpole trigger (3 seeds) & trn & ON & 8 & 236.3 @105K$^i$ & --- & No CIVO \\
88	062 & Cartpole control (3 seeds) & --- & ON & 8 & 244.8 @105K$^i$ & --- & No CIVO \\
89	\bottomrule
90	\end{tabular}
91	\vspace{1pt}
92	{\raggedright\footnotesize
93	trn = trained ($d{=}32$, subsample ON);
94	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
95	exp$^a$ = trained, subsample OFF;
96	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
97	--- = removed ($d{=}0$).\\
98	$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
99	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
100	$^\dagger$ NVE self-corrected ($4.72\times$ $\to$ $1.22\times$) but policy did not recover (eval 10.5\% of baseline).\\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "f76e71ea-03bb-4356-9380-d3cb65bfee2a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\\heartsuit$ & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Collapse$^\\dagger$ \\\\\n\\rowcolor{gray!15}\n068 & Factorial repro (s1) & trn & ON & 8 & 39.1 @105K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 289.3 @105K & 0.76$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n008a\\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n067 & Frozen emb (s0) & frz$^b$ & ON & 8 & 281.5 @105K & 0.19$\\times$ & Healthy \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n008e\\_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.61$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cartpole Swingup}} \\\\\n060 & Cartpole baseline (3 seeds) & --- & --- & 15 & 557.0 @105K$^i$ & --- & Healthy \\\\\n061 & Cartpole trigger (3 seeds) & trn & ON & 8 & 236.3 @105K$^i$ & --- & No CIVO \\\\\n062 & Cartpole control (3 seeds) & --- & ON & 8 & 244.8 @105K$^i$ & --- & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^\\dagger$ NVE self-corrected ($4.72\\times$ $\\to$ $1.22\\times$) but policy did not recover (eval 10.5\\% of baseline).\\\\",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 1170
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01BKn4xNZD9eCgLRP1ZhA3Ph`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 100,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "3f7e2dde-8bb4-4b53-ae3b-ee0390cc61a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AbAzdkwWtxn86Q1wMqu5PJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3699,
      "cache_read_input_tokens": 39822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3699
      },
      "output_tokens": 35,
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

_source line 35 · 2026-05-25T15:53:52.436Z_

<details><summary>↩ Tool result · `toolu_01BKn4xNZD9eCgLRP1ZhA3Ph`</summary>

```text
100	$^\dagger$ NVE self-corrected ($4.72\times$ $\to$ $1.22\times$) but policy did not recover (eval 10.5\% of baseline).\\
101	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
102	$^d$ Peak NVE $9.94\times$ at 45K (transient, self-correcting to $<$1$\times$ by 55K); final eval 221.5.\\
103	$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\
104	$^f$ StackCube transient: frozen control (exp\_051, peak $4.30\times$ at 42.5K) matches trained (exp\_049/052), self-correcting by 82.5K; environment-specific, not $\dt$-embedding-driven.\\
105	$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\times$ (82.5K); seed~1 trained (exp\_055) peaks at $3.08\times$ (92.5K), final $0.50\times$ at 212.5K; seed~1 frozen (exp\_056) peaks at $11.32\times$ (82.5K), final $1.19\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\dt$-embedding causation.\\
106	$^h$ PickCube environment transient: frozen control peak $8.81\times$ at 62.5K, self-correcting to $0.55\times$ at 72.5K; matches trained (exp\_019b) trajectory.\\
107	$^\heartsuit$ Evaluated at 55K steps due to early termination of exp\_008d; extended run (exp\_009e) reached 131.08 at 105K.\\
108	$^i$ Cartpole: exp\_060 reports seed~2 eval only; exp\_061/062 report 3-seed mean.\par}
109	\end{table*}
110	
111	\begin{table}[h]
112	\centering
113	\caption{Cross-domain CIVO reproducibility. ``$\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}
114	\label{tab:cross_domain}
115	\footnotesize
116	\begin{tabular}{llccc}
117	\toprule
118	\textbf{Domain} & \textbf{Environment} & \textbf{Trained} & \textbf{Frz ctrl} & \textbf{$\dt$-emb-dep.\ CIVO} \\
119	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "634c18c5-ab9b-46f9-ba1f-5bc30e71502f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "$^\\dagger$ NVE self-corrected ($4.72\\times$ $\\to$ $1.22\\times$) but policy did not recover (eval 10.5\\% of baseline).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\\\\n$^\\heartsuit$ Evaluated at 55K steps due to early termination of exp\\_008d; extended run (exp\\_009e) reached 131.08 at 105K.\\\\\n$^i$ Cartpole: exp\\_060 reports seed~2 eval only; exp\\_061/062 report 3-seed mean.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule",
      "numLines": 20,
      "startLine": 100,
      "totalLines": 1170
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

Now I have the full picture of the experiment catalog table. I need to add exp\_077 (Cheetah baseline) and exp\_078 (Cheetah CIVO trigger) to the "Cross-environment validation" section. Let me check where exactly to insert them.

The cross-environment section starts at line 61 with Cheetah Run experiments (010b, 010b\_s0, 021, 024b s0/s1, 008a\_ch s0/s1). exp\_077 is a baseline and exp\_078 is a CIVO trigger run, both for Cheetah Run.

I'll insert them into the Cheetah Run block within the cross-environment validation section. exp\_077 is a baseline (no dt embedding, healthy), and exp\_078 has trained dt\_emb with CIVO onset that self-corrects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "8aaa51d4-4346-4c0c-95a1-79e461eba0c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEStzBGMH6WCzQ3KRRSa1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 43521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 857
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_0188Dvcr8YBoTzc3148MdRwT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1",
  "new_string": "008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\\times$ & Onset (self-corr.) \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "6beeb6d0-278d-49f6-a077-1497afd57fb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEStzBGMH6WCzQ3KRRSa1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 43521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 857
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

_source line 38 · 2026-05-25T15:54:12.174Z_

<details><summary>↩ Tool result · `toolu_0188Dvcr8YBoTzc3148MdRwT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "121f744f-3ddd-430a-addd-7c666043f29e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1",
    "newString": "008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\\times$ & Onset (self-corr.) \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\\heartsuit$ & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Collapse$^\\dagger$ \\\\\n\\rowcolor{gray!15}\n068 & Factorial repro (s1) & trn & ON & 8 & 39.1 @105K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 289.3 @105K & 0.76$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n008a\\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n067 & Frozen emb (s0) & frz$^b$ & ON & 8 & 281.5 @105K & 0.19$\\times$ & Healthy \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n008e\\_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.61$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cartpole Swingup}} \\\\\n060 & Cartpole baseline (3 seeds) & --- & --- & 15 & 557.0 @105K$^i$ & --- & Healthy \\\\\n061 & Cartpole trigger (3 seeds) & trn & ON & 8 & 236.3 @105K$^i$ & --- & No CIVO \\\\\n062 & Cartpole control (3 seeds) & --- & ON & 8 & 244.8 @105K$^i$ & --- & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^\\dagger$ NVE self-corrected ($4.72\\times$ $\\to$ $1.22\\times$) but policy did not recover (eval 10.5\\% of baseline).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\\\\n$^\\heartsuit$ Evaluated at 55K steps due to early termination of exp\\_008d; extended run (exp\\_009e) reached 131.08 at 105K.\\\\\n$^i$ Cartpole: exp\\_060 reports seed~2 eval only; exp\\_061/062 report 3-seed mean.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\midrule\nLocomotion & Cartpole Swingup & 0/3 & 0/3 & No (single-joint) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cartpole Swingup.} Cartpole Swingup (single-DoF locomotion) serves as a cross-environment control. Three seeds of the CIVO-trigger configuration (exp\\_061: trained $e_{\\dt}$, subsample ON, $H{=}8$, $\\dt{=}2$) and three seeds of the no-embedding control (exp\\_062) both produce zero CIVO onset. Despite using the hyperparameter combination that triggers collapse in all 10 tested multi-joint locomotion seeds (Walker/Cheetah), the single-joint Cartpole shows no CIVO, confirming the phenomenon requires multi-joint dynamics where temporal abstraction amplifies the reward fidelity gap.\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eleven factorial experiments (including four 008e\\_v3 seeds and exp\\_059). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n059          & 4.72 & self-correcting CIVO & $-$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 0.917$ because exp\\_059 (NVE${=}4.72\\times$, self-correcting CIVO, B1-negative) ranks above two sustained-CIVO positives ($4.12\\times$, $4.02\\times$), breaking the perfect rank separation that held before its inclusion. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value (accuracy $10/11 = 90.9\\%$). Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.967$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=8$, $n=11$, $\\text{AUROC}=0.917$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$; exp\\_059 (NVE${=}4.72\\times$, B1-negative) is the sole false positive.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 4 & 0 & 4 & 63.6\\% \\; [30.8, 89.1] & 42.9\\% & 100\\% & 60.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 3 & 0 & 5 & 72.7\\% \\; [39.0, 94.0] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 3 & 3 & 0 & 5 & 72.7\\% \\; [39.0, 94.0] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 2 & 0 & 6 & 81.8\\% \\; [48.2, 97.7] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 2 & 0 & 6 & 81.8\\% \\; [48.2, 97.7] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 1 & 0 & 7 & 90.9\\% \\; [58.7, 99.8] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=5$, $n_{\\text{neg}}=6$, $n=11$, $\\text{AUROC}=0.967$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 5 & 2 & 0 & 4 & 81.8\\% \\; [48.2, 97.7] & 71.4\\% & 100\\% & 83.3\\% \\\\\n$\\geq 1.2\\times$ & 5 & 1 & 0 & 5 & 90.9\\% \\; [58.7, 99.8] & 83.3\\% & 100\\% & 90.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 5 & 1 & 0 & 5 & 90.9\\% \\; [58.7, 99.8] & 83.3\\% & 100\\% & 90.9\\% \\\\\n$\\geq 1.7\\times$ & 4 & 1 & 1 & 5 & 81.8\\% \\; [48.2, 97.7] & 80.0\\% & 80.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 4 & 1 & 1 & 5 & 81.8\\% \\; [48.2, 97.7] & 80.0\\% & 80.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 4 & 0 & 1 & 6 & 90.9\\% \\; [58.7, 99.8] & 100\\% & 80.0\\% & 88.9\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=9$, $n_{\\text{neg}}=8$, $n=17$, $\\text{AUROC}=0.972$). Includes Walker Walk (15 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 9 & 2 & 0 & 6 & 88.2\\% \\; [63.6, 98.5] & 81.8\\% & 100\\% & 90.0\\% \\\\\n$\\geq 1.2\\times$ & 9 & 1 & 0 & 7 & 94.1\\% \\; [71.3, 99.9] & 90.0\\% & 100\\% & 94.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 9 & 1 & 0 & 7 & 94.1\\% \\; [71.3, 99.9] & 90.0\\% & 100\\% & 94.7\\% \\\\\n$\\geq 1.7\\times$ & 7 & 1 & 2 & 7 & 82.4\\% \\; [56.6, 96.2] & 87.5\\% & 77.8\\% & 82.4\\% \\\\\n$\\geq 2.0\\times$ & 7 & 1 & 2 & 7 & 82.4\\% \\; [56.6, 96.2] & 87.5\\% & 77.8\\% & 82.4\\% \\\\\n$\\geq 3.9\\times$ & 7 & 0 & 2 & 8 & 88.2\\% \\; [63.6, 98.5] & 100\\% & 77.8\\% & 87.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all five CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 80.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 90.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), the optimal threshold $\\nve \\geq 3.9\\times$ achieves $10/11$ accuracy ($90.9\\%$, 95\\% CI: [58.7\\%, 99.8\\%]); the sole false positive is exp\\_059 (NVE${=}4.72\\times$, self-correcting CIVO classified as B1-negative).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}17$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}56$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}56$ configurations, AUROC${=}0.990$, comprehensive validation). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.09$, accuracy${=}53/56$, F1${=}0.941$. Three false positives arise from non-CIVO value overestimation: mitigation transient VE spike (008e\\_v3 subsample, $1.93\\times$) and frozen embedding transients (047, $1.71\\times$; 057, $1.88\\times$). Threshold calibrated and validated post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_threshold_prf.pdf}\n\\caption{Precision, Recall, and F1 as a function of NVE threshold ($n{=}56$ configurations). Peak F1${=}0.941$ at $\\tau{=}1.5\\times$, where recall remains perfect ($1.00$) and precision${=}0.889$. The plateau of high F1 across $\\tau \\in [1.5, 1.7]$ indicates robustness to threshold selection.}\n\\label{fig:nve_prf}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\paragraph{Comprehensive validation ($n{=}56$).}\nExpanding the evaluation set to all classifiable experiments yields $n{=}56$ ($n_{\\text{pos}}{=}24$, $n_{\\text{neg}}{=}32$), spanning Walker Walk, Cheetah Run, and multiple intervention configurations (SGS, TCN, dual-critic, frozen embedding). At the $1.5\\times$ threshold: AUROC${=}0.990$, precision${=}0.889$, recall${=}1.000$, F1${=}0.941$, accuracy${=}53/56$. The three false positives are: exp\\_008e\\_v3\\_subsample ($1.93\\times$, mitigation config with transient VE spike), exp\\_047 ($1.71\\times$, frozen embedding transient), and exp\\_057 ($1.88\\times$, frozen embedding transient). All 24 CIVO-positive configurations are correctly detected (FN${=}0$), with CIVO-positive NVE ranging from $1.53\\times$ (008d seed~3, late-onset) to $70.64\\times$ (010b seed~0, Cheetah). The substantial increase in sample size from $n{=}32$ to $n{=}56$ strengthens confidence in the $1.5\\times$ threshold as a robust diagnostic boundary.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the single-seed baseline (seed~1, exp\\_001, 505K steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} The initial $n{=}11$ analysis had wide Clopper-Pearson confidence intervals (e.g., 90.9\\% accuracy, 95\\% CI [58.7\\%, 99.8\\%]). The comprehensive evaluation ($n{=}56$, AUROC${=}0.990$, F1${=}0.941$; Figure~\\ref{fig:nve_roc}) substantially tightens these bounds. Table~\\ref{tab:sensitivity_b2_full} reports the $n{=}17$ two-environment core evaluation. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}15$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 20 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 17 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 15 & $(1.00,\\, 3.78)$ & 14/15 (0.933) & 0.963 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.978} & \\textbf{0.988} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe threshold $\\theta{=}1.5\\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\\_008e\\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\\S\\ref{sec:roc_analysis}). Mean held-out accuracy is 0.978 and mean AUROC is 0.988, confirming that $\\theta{=}1.5\\times$ generalizes across environments without retuning.\nPickCube fold confidence intervals remain wide (Clopper-Pearson 95\\% CI: $[0.158, 1.000]$) due to $N_{\\text{test}}{=}2$.\n\n\\subsection{Leave-One-Config-Out Cross-Validation}\n\\label{sec:nve_loco}\n\n\\paragraph{Leave-One-Config-Out Cross-Validation.}\nTo rule out threshold overfitting to any particular experimental configuration, we perform leave-one-config-out (LOCO) cross-validation over $K{=}12$ configuration groups (e.g., \\texttt{008d\\_civo\\_trigger}, \\texttt{frozen\\_dt\\_emb}, \\texttt{tcn}; $n{=}56$ total). Each fold holds out all experiments from one configuration, selects the F1-maximizing threshold on the remaining $K{-}1$ groups, and evaluates on the held-out group.\n\nIn $10/12$ folds, the training-optimal threshold falls within $\\pm 0.05$ of $\\theta{=}1.5\\times$ (mean $1.61 \\pm 0.23$, range $[1.47, 2.12]$). The two folds selecting a higher threshold ($\\theta{=}2.1$; \\texttt{008d\\_civo\\_trigger} and \\texttt{tcn}, both predominantly CIVO-positive) perform \\emph{worse} on their held-out sets than $\\theta{=}1.5$ (accuracy $0.78$/$0.88$ vs.\\ $1.00$/$1.00$), confirming that the fixed threshold generalizes better than per-fold optimization in these cases. Cross-validated accuracy at $\\theta{=}1.5$ is $53/56 = 94.6\\%$, identical to the in-sample result, with train AUROC consistently high across folds ($0.988 \\pm 0.003$). The three misclassifications are the same mechanistically distinct false positives identified in \\S\\ref{sec:roc_analysis}: two frozen-embedding transients (exp\\_047, exp\\_057) and one mitigation-config transient (exp\\_008e\\_v3\\_subsample). No CIVO-positive configuration is missed in any fold (FN${=}0$ across all 12 folds).\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d, 059 & $1.53$--$4.72\\times$ & 64--268 & 5/5 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\n\\paragraph{Controlled three-way causal ablation.}\nExperiments 067--069 provide a minimal causal ablation on Walker Walk (seed${=}1$), varying \\emph{only} the $\\dt$-embedding treatment while holding all other hyperparameters fixed ($H{=}8$, subsample ON, $\\dt{=}2$ imagination). Table~\\ref{tab:causal_ablation} shows that trained $\\dt$-embedding is necessary and sufficient for CIVO: freezing the embedding (gradient flow blocked, embedding weights still present) eliminates CIVO as completely as removing the embedding ($d{=}0$), ruling out the alternative hypothesis that embedding \\emph{presence} alone causes CIVO. Combined with all prior seeds, trained $\\dt$-embedding triggers CIVO in 10/10 multi-joint locomotion seeds (8 Walker, 2 Cheetah) versus 0/5 controls (0/3 no-embedding, 0/2 frozen; Fisher exact $p < 0.001$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Three-way causal ablation (Walker Walk, seed${=}1$). Only the $\\dt$-embedding treatment varies; all other configuration is identical. Trained embedding triggers CIVO; frozen and removed do not.}\n\\label{tab:causal_ablation}\n\\footnotesize\n\\begin{tabular}{llccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Embedding} & \\textbf{NVE peak} & \\textbf{Eval final} & \\textbf{CIVO} \\\\\n\\midrule\n\\rowcolor{gray!15}\n068 & Trained ($d{=}32$) & $6.57\\times$ & 39.1 & Yes (alert @85K) \\\\\n067 & Frozen ($d{=}32$, \\texttt{req\\_grad=F}) & $0.40\\times$ & 281.5 & No \\\\\n069 & Removed ($d{=}0$) & $0.66\\times$ & 237.8 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe empirical finding that trained embedding \\emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.83$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.42\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.47 \\rightarrow 0.39 \\rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.42\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that in all tested configurations, CIVO occurs only with the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\\dt}$ precedes CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$108.52\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\\_046, NVE${=}1.35\\times$ vs.\\ trained $70.64\\times$, a $52\\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly sufficient in tested configurations.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}\n\\caption{CIVO mechanism diagram. The trained $\\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\\to$ optimistic critic values $\\to$ actor exploitation $\\to$ reinforced state-distribution skew.}\n\\label{fig:civo_mechanism}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\\ref{fig:civo_mechanism}).  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\paragraph{Signed reward error analysis.}\nTo test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\\ref{tab:signed_error}). The trained-embedding model (008d) shows \\emph{negative} bias at $\\dt{=}2$ (mean signed error $-0.599$, only 8\\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \\emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\\dt > 1$ (Stage~1 above, $1.68\\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \\emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}\n\\label{tab:signed_error}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Config} & $\\dt$ & \\textbf{Mean SE} & \\textbf{Std} & \\textbf{\\%Over} & \\textbf{Actual} & \\textbf{Pred} \\\\\n\\midrule\nBaseline & 1 & $+0.001$ & 0.023 & 39.6\\% & 1.893 & 1.894 \\\\\n\\midrule\n008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\\% & 0.361 & 0.379 \\\\\n008d (trained) & 2 & $\\mathbf{-0.599}$ & 0.722 & 8.0\\% & 0.721 & 0.121 \\\\\n\\midrule\n008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\\% & 0.921 & 0.211 \\\\\n008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\\% & 1.840 & 0.195 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Embedding geometry (exp\\_065).}\nTo characterize what the trained $\\dt$-embedding learns, we measure pairwise cosine similarity between $e_{\\dt{=}1}$ and $e_{\\dt{=}2}$ across training checkpoints for three trained seeds (two environments) and two frozen controls (Table~\\ref{tab:cosine_sim}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cosine similarity between $e_{\\dt{=}1}$ and $e_{\\dt{=}2}$ vectors. Trained embeddings converge to near-opposite representations; frozen embeddings remain near-orthogonal throughout.}\n\\label{tab:cosine_sim}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrr}\n\\toprule\n\\textbf{Config} & \\textbf{Env} & \\textbf{cos@25K} & \\textbf{cos@75K} & \\textbf{Status} \\\\\n\\midrule\n008d s3 (trained) & Walker & $-0.87$ & $-0.70$ & CIVO \\\\\n059 s5 (trained) & Walker & $-0.94$ & $-0.86$ & CIVO \\\\\n010b s0 (trained) & Cheetah & $-0.90$ & $-0.84$ & CIVO \\\\\n\\midrule\n057 s2 (frozen) & Walker & $-0.15$ & $-0.15$ & Healthy \\\\\n058 s1 (frozen) & Cheetah & $+0.07$ & $+0.07$ & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll trained seeds map $\\dt{=}1$ and $\\dt{=}2$ to nearly opposite directions (cosine similarity $-0.70$ to $-0.94$), consistent across both Walker and Cheetah environments. Frozen controls remain near-orthogonal (cosine $\\approx 0$) and constant across all checkpoints. The full pairwise cosine similarity matrix (Figure~\\ref{fig:pairwise_heatmap}) reveals that the near-antipodal relationship between $e_{\\dt{=}1}$ and $e_{\\dt{=}2}$ is the dominant structure: most other $\\dt$-pairs remain near-orthogonal ($|\\text{cos}| < 0.2$), indicating that the RSSM selectively maximizes separation along the $\\dt{=}1$ vs.\\ $\\dt{=}2$ axis rather than learning a globally structured embedding space.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.55\\columnwidth]{figures/paper/pairwise_heatmap.png}\n\\caption{Pairwise cosine similarity between all $\\dt$-embedding vectors (exp\\_008d, seed 3, step 75K). The $e_{\\dt{=}0}$--$e_{\\dt{=}1}$ pair exhibits strong anti-correlation ($-0.70$); remaining pairs are near-orthogonal, confirming that the learned geometry is dominated by a single antipodal axis.}\n\\label{fig:pairwise_heatmap}\n\\end{figure}\n\nThe magnitude of the learned separation---near-antipodal rather than merely distinct---provides converging evidence that the RSSM develops maximally differentiated internal representations for the two temporal scales, which in turn may contribute to the asymmetric reward fidelity gap reported in Table~\\ref{tab:rssm_fidelity} and replicated below.\n\n\\paragraph{Extended RSSM fidelity replication (exp\\_063).}\nTo validate the fidelity gap on independently trained checkpoints, we repeat the posterior-conditioned analysis with 15 episodes $\\times$ 40 test points $\\times$ 4 $\\dt$ levels (600 samples per model) on final checkpoints from three conditions (Table~\\ref{tab:rssm_fidelity_ext}).\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity analysis (training-time posterior-conditioned). Reward prediction gap remains the critical differentiator; observation reconstruction is paradoxically \\emph{better} with trained embedding. Independent final-checkpoint replication (exp\\_063, 008d seed~4) yields a reward gap of $2.7\\times$, confirming the qualitative pattern at lower magnitude.}\n\\label{tab:rssm_fidelity_ext}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline (009d) & 16.08 & 23.49 & 1.46$\\times$ & 0.045 & 0.059 & 1.30$\\times$ \\\\\nCollapsed (008d) & 9.96 & 13.21 & 1.33$\\times$ & 0.057 & 0.178 & 3.11$\\times$ \\\\\nFrozen (057) & 11.14 & 14.95 & 1.34$\\times$ & 0.068 & 0.133 & 1.96$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe replication confirms the original fidelity gap pattern with two additional observations. First, the collapsed model achieves the \\emph{lowest} absolute obs\\_MSE at $\\dt{=}1$ (9.96 vs.\\ baseline 16.08), indicating that the trained $\\dt$-embedding improves world model quality overall---the pathology is selective degradation of reward predictions at longer horizons, not general model failure. Second, freezing the $\\dt$-embedding reduces the reward gap from $3.11\\times$ (training-time; $2.7\\times$ in independent replication) to $1.96\\times$, providing converging evidence for its role in preventing the co-adaptation loop while leaving residual multi-step reward prediction difficulty.\n\n\\paragraph{Value prediction analysis (exp\\_064).}\nTo examine the relationship between RSSM reward fidelity and critic value estimates, we compare critic predictions $V(s)$ against actual evaluation returns across three conditions (Table~\\ref{tab:value_pred}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Critic value predictions vs.\\ actual evaluation returns. The CIVO model's critic is well-calibrated to its $\\lambda$-return targets ($V(s) \\approx$ target) but both $V$ and targets are disconnected from reality (VE${=}3.03\\times$).}\n\\label{tab:value_pred}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Config} & $V(s)$ & \\textbf{Eval} & \\textbf{VE ratio} & $V{-}\\text{target}$ \\\\\n\\midrule\nBaseline (001) & 665.9 & 938.9 & 0.71$\\times$ & $+0.001$ \\\\\nCIVO (008d) & 192.7 & 63.6 & \\textbf{3.03}$\\times$ & $+0.586$ \\\\\nNo emb (008f) & 116.5 & 306.5 & 0.38$\\times$ & $+0.316$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe paradox---$V(s)$ tracks its $\\lambda$-return targets faithfully yet overestimates actual performance by $3\\times$---provides converging evidence for the hypothesized mechanism in which CIVO operates upstream of the critic: the world model generates inflated imagination trajectories that the critic learns faithfully, producing targets disconnected from reality. In the baseline, VE${<}1.0$ throughout training because $V(s)$ reflects discounted imagined returns over $H{=}15$ steps, naturally lower than undiscounted episodic evaluation. The CIVO model crosses VE${=}1.0$ at step 55K and reaches $3.03\\times$ by 105K, with the gap widening as the actor exploits the overoptimistic critic.\n\n\\paragraph{Actor entropy dynamics under CIVO.}\nExtended training of collapsed configurations reveals a distinctive temporal sequence: evaluation return collapses first, followed by actor entropy explosion ${\\sim}35$K steps later. In the most severe case (EG~v4), entropy rises from $-5.21$ to $+3.22$ nats at a rate of $+2.11$ nats/10K steps, with returns declining from 583 to 93 between steps 60K--120K. A second collapsed run (EG~v5) shows $+0.61$ nats/10K with comparable return degradation (583$\\to$102). By contrast, healthy baselines exhibit gradual entropy drift at $+0.07$ to $+0.22$ nats/10K---15--30$\\times$ slower---with returns stable above 900. The return-before-entropy temporal ordering is consistent with the causal chain: delusional critic $\\to$ bad actor gradients $\\to$ policy destabilization. The entropy explosion is a lagging indicator; the NVE diagnostic detects CIVO onset ${\\sim}35$K steps before entropy rises, consistent with its use as an early-warning signal (\\S\\ref{sec:appendix_sensitivity}).\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\\times$ to $1.66\\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3. \\textbf{Trained dt-emb} (008d)\\protect\\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\\dt}$. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$. Full-SGS seed~1 shows partial mitigation ($-51\\%$ final, NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses ($-96\\%$ final). CIVO elimination rate $= 0/2$.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all seven CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\nWalker & s5 (059) & 4.72$\\times$ & 1.22$\\times$ & 95.8 & Collapse$^\\dagger$ \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K. $^\\dagger$~NVE self-corrected ($4.72\\times$ $\\to$ $1.22\\times$) but policy did not recover (eval 10.5\\% of baseline).\\par}\n\\end{table}\n\nAll seven CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (6/7 seeds), with one self-correction case (Walker seed 2); seed 5 exemplifies a dissociation where NVE self-corrects ($4.72\\times \\to 1.22\\times$) while the policy remains collapsed (eval 10.5\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage persists even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Representative} & \\textbf{NVE} & \\textbf{Entropy} & \\textbf{Mechanism} \\\\\n\\midrule\nMonotonic CIVO & 008d, 008d\\_s4, 010b\\_s0 & $\\uparrow$ sustained & $\\downarrow$ & Reward bias $\\to$ critic $\\to$ actor \\\\\nLate-onset CIVO & 008d\\_s3 & $\\uparrow$ delayed & $\\downarrow$ & Same, delayed onset \\\\\nTransient CIVO & 009b & Peak $\\to$ $\\downarrow$ & Stable & Self-correction via capacity \\\\\nIRD collapse & 008e\\_v3\\_s2 & $\\uparrow$ late & $\\uparrow$ & Entropy-driven, values stable \\\\\nGrad.\\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\\to$ zero actor grad \\\\\nSGS-resistant & 018\\_s2 & $\\uparrow$ & $\\downarrow$ & Forward-pass conditioning \\\\\nSGS-paradoxical & 016e & $\\uparrow$ sustained & $\\downarrow$ & Reward SGS $\\to$ obs-dec reliance \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Training Dynamics}\\label{sec:extended_training}\n\nOne Walker seed (s3, exp\\_045) was extended from 112K to approximately 302K steps to investigate long-horizon CIVO dynamics. After onset (NVE peak $4.91\\times$ at 132K steps), the system exhibited complete self-recovery: NVE declined to $0.05\\times$ and evaluation performance recovered to 867.6 (94.7\\% of baseline). This recovery required approximately 170K additional training steps beyond onset. The trajectory shows a single onset--recovery cycle with no recurrence, suggesting that the CIVO feedback loop can break spontaneously given sufficient training---though at substantial computational cost that the frozen $\\dt$-embedding diagnostic eliminates entirely.\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids collapse in 2 of 4 seeds (50\\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\\times$; \\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Temporal Embedding Representation Analysis}\n\\label{sec:cosine_evolution}\n\nTo understand how the trained $\\dt$-embedding creates vulnerability, we analyze the cosine similarity between $e(\\dt{=}1)$ and $e(\\dt{=}2)$ across training (exp\\_065). Trained embeddings learn \\emph{near-opposite} representations: $\\cos(e_1, e_2) = {-}0.87$ to ${-}0.94$ at 25K steps across three configurations (Walker 008d\\_s3, Cheetah 010b\\_s0, Walker 059\\_s5), persisting at ${-}0.70$ to ${-}0.86$ at 75K steps. In contrast, frozen embeddings maintain near-zero similarity ($-0.15$ to $+0.07$, constant throughout training). The near-antipodal learned representations explain the large reward prediction gap (\\S\\ref{sec:f2}): $\\dt{=}2$ conditioning pushes the RSSM into a qualitatively different region of latent space, producing systematically biased predictions rather than minor perturbations.\n\n\\subsection{\\texorpdfstring{$\\dt$}{dt}-Embedding Differentiation Precedes Value Divergence}\n\\label{sec:cosine_temporal}\n\nThe preceding analysis established that trained $\\dt$-embeddings learn near-antipodal representations. Here we resolve the \\emph{temporal dynamics} of this differentiation across 11 experiments (${\\sim}$47 checkpoints), testing whether embedding differentiation is a consequence or precursor of CIVO.\n\n\\paragraph{Trained embeddings: monotonic relaxation.}\nAcross all trained configurations, $\\cos(e_1, e_2)$ starts near $-0.95$ within 10K steps and relaxes monotonically toward ${\\sim}{-}0.65$ (Table~\\ref{tab:cosine_evolution_ext}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cosine similarity evolution between $e(\\dt{=}1)$ and $e(\\dt{=}2)$ for trained $\\dt$-embeddings. Relaxation is monotonic but never reaches zero; frozen embeddings remain constant near zero throughout training.}\n\\label{tab:cosine_evolution_ext}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Env} & \\textbf{Experiment} & \\textbf{10K} & \\textbf{25K} & \\textbf{65K} & \\textbf{75K} & \\textbf{302K} \\\\\n\\midrule\n\\multirow{2}{*}{Walker} & exp\\_066b (trained) & $-0.947$ & $-0.928$ & $-0.847$ & --- & --- \\\\\n & exp\\_045 (extension) & --- & --- & --- & --- & $-0.668$ \\\\\n\\midrule\nCheetah & exp\\_010b$\\to$048 & --- & $-0.904$ & --- & $-0.841$ & $-0.639$ \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Frozen controls:}} \\\\\nWalker & exp\\_057 (frozen) & \\multicolumn{5}{c}{$-0.150$ (constant, 25K--225K)} \\\\\nCheetah & exp\\_058 (frozen) & \\multicolumn{5}{c}{$+0.069$ (constant, 25K--225K)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-seed consistency at 25K steps is high: mean $\\cos = -0.910 \\pm 0.028$ ($n{=}5$ Walker seeds), confirming the relaxation pattern is robust across random seeds. Variance increases with training ($-0.789 \\pm 0.076$ at 75K), reflecting seed-dependent relaxation rates.\n\n\\paragraph{Temporal precedence over CIVO.}\nExp\\_066b provides simultaneous cosine similarity and CIVO diagnostic data at 5K resolution (Table~\\ref{tab:cosine_vs_civo}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cosine similarity relaxation and CIVO diagnostic for exp\\_066b. Embedding relaxation onset (${\\sim}$20K) precedes CIVO alert (55K, VE ratio $> 0.7$) by ${\\sim}$30--35K steps.}\n\\label{tab:cosine_vs_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{rccc}\n\\toprule\n\\textbf{Step} & $\\cos(e_1, e_2)$ & \\textbf{VE ratio} & \\textbf{CIVO alert} \\\\\n\\midrule\n10K & $-0.947$ & 0.012 & --- \\\\\n15K & $-0.948$ & 0.033 & --- \\\\\n25K & $-0.928$ & 0.193 & --- \\\\\n35K & $-0.904$ & 0.269 & --- \\\\\n45K & $-0.880$ & 0.358 & --- \\\\\n55K & $-0.861$ & 0.710 & \\textbf{Alert} \\\\\n65K & $-0.847$ & 0.724 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCosine relaxation begins at ${\\sim}$20K (cos transitions from $-0.948$ at 15K to $-0.928$ at 25K), while the VE ratio first exceeds 0.7 at 55K. The ${\\sim}$30--35K temporal lead establishes that embedding differentiation is an early training dynamic, not a consequence of CIVO-triggered feedback. The relaxation rate peaks at 25K--45K ($+0.024$/10K steps) before decelerating, consistent with the geometric intuition that large-angle adjustments in embedding space are cheaper early in training.\n\n\\paragraph{Embedding norms.}\nWalker and Cheetah exhibit qualitatively different norm dynamics. Walker $e(\\dt{=}1)$ norms grow from 0.23 to 0.50 ($2.2\\times$) while $e(\\dt{=}2)$ grows from 0.45 to 0.63 ($1.4\\times$)---both $\\dt$ values become more expressive over training. Cheetah norms remain nearly constant ($\\leq 1.04\\times$) despite continued cosine relaxation, indicating direction changes without magnitude change. Frozen embedding norms are an order of magnitude smaller (${\\sim}0.06$, constant).\n\n\\paragraph{Mechanistic interpretation.}\nThe temporal ordering---embedding differentiation (${\\sim}$20K) $\\to$ reward fidelity gap (${\\sim}$20K, \\S\\ref{sec:timeseries_fidelity}) $\\to$ value overestimation (${\\sim}$30K)---suggests a three-layer causal chain: the embedding first learns maximally differentiated representations that push $\\dt{=}1$ and $\\dt{=}2$ into opposite latent regions, the reward head then develops scale-dependent biases from these differentiated inputs, and the critic amplifies these biases through imagined rollout bootstrapping. The frozen embedding's constant near-zero cosine ($|\\cos| < 0.2$) prevents the first link in this chain, explaining why freezing eliminates CIVO despite maintaining identical forward-pass architecture (\\S\\ref{sec:f3}).\n\n\\subsection{Time-Series Fidelity--Value Analysis}\n\\label{sec:timeseries_fidelity}\n\nTo test the causal direction between reward fidelity degradation and value overestimation, we analyze exp\\_066 and exp\\_066b: two Walker Walk seeds (trained $\\dt$-embedding, fixed $\\dt{=}2$) evaluated at 12 dense checkpoints from 10K to 65K steps (Table~\\ref{tab:timeseries_fidelity}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Time-series fidelity and value metrics (exp\\_066, seed~0). SS = single-step MAE ratio ($\\dt{=}2$/$\\dt{=}1$); VE = value-to-eval ratio. Fidelity degradation (SS $>1.1\\times$ at 20K) precedes value overestimation onset (VE begins rising at ${\\sim}$30K) by ${\\sim}$10K steps. Seed~1 (exp\\_066b) confirms the pattern: fidelity gap onset ${\\sim}$15K $\\to$ VE onset ${\\sim}$24K (lead ${\\approx}$9K steps; VE peak ${=}0.72$).}\n\\label{tab:timeseries_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{rcccccc}\n\\toprule\n\\textbf{Step} & \\textbf{SS ratio} & \\textbf{OL ratio} & \\textbf{VE ratio} & \\textbf{MAE$_{\\dt{=}1}$} & \\textbf{MAE$_{\\dt{=}2}$} & \\textbf{Return} \\\\\n\\midrule\n10K & 1.05 & 0.94 & 0.01 & 0.090 & 0.094 & 43.0 \\\\\n15K & 1.08 & 1.03 & 0.02 & 0.085 & 0.092 & 187.8 \\\\\n20K & 1.10 & 1.09 & 0.16 & 0.078 & 0.086 & 148.7 \\\\\n25K & 1.04 & 1.22 & 0.16 & 0.073 & 0.076 & 142.1 \\\\\n30K & 1.25 & 1.45 & 0.22 & 0.068 & 0.085 & 148.3 \\\\\n35K & 1.24 & 1.51 & 0.23 & 0.062 & 0.077 & 275.4 \\\\\n40K & 1.35 & 1.38 & \\textbf{1.59} & 0.058 & 0.078 & 202.3 \\\\\n45K & 1.40 & 1.38 & 0.36 & 0.055 & 0.077 & 107.5 \\\\\n50K & 1.47 & 1.56 & 0.62 & 0.052 & 0.076 & 178.4 \\\\\n55K & 1.37 & 1.52 & 0.62 & 0.050 & 0.069 & 60.8 \\\\\n60K & 1.61 & 1.35 & 1.40 & 0.049 & 0.079 & 125.3 \\\\\n65K & 1.68 & 1.38 & 1.40 & 0.047 & 0.079 & 94.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/paper/fig_temporal_ordering.pdf}\n\\caption{Temporal ordering of fidelity degradation and value overestimation (exp\\_066, seed~0). \\textbf{Left axis}: single-step fidelity ratio (SS, blue) grows steadily from $1.05\\times$ to $1.68\\times$. \\textbf{Right axis}: value-to-eval ratio (VE, red) remains near zero until 40K, then spikes. The ${\\sim}$10K onset-to-onset lag supports the causal direction: fidelity gap $\\to$ value overestimation. Seed~1 (exp\\_066b) replicates the pattern with a ${\\sim}$9K temporal lead.}\n\\label{fig:temporal_ordering}\n\\end{figure}\n\nThe $\\dt{=}1$ prediction MAE decreases monotonically ($0.090 \\to 0.047$) as the world model improves, but $\\dt{=}2$ MAE plateaus at ${\\sim}0.08$. The growing fidelity gap is therefore not caused by $\\dt{=}2$ predictions worsening, but by the model selectively improving at $\\dt{=}1$ while failing to transfer that improvement to $\\dt{=}2$---consistent with the trained $\\dt$-embedding learning maximally differentiated representations (\\S\\ref{sec:cosine_evolution}) that prevent cross-scale generalization.\n\n\\textbf{Limitation.} These results are limited to two seeds ($n{=}2$). While both seeds show consistent temporal ordering (leads of ${\\approx}$10K and ${\\approx}$9K steps), additional seeds would strengthen the causal claim.\n\n\\subsection{Actor Entropy Is Not Diagnostic of CIVO}\n\\label{sec:entropy_not_diagnostic}\n\nTo test whether actor entropy can serve as an early collapse indicator, we compare entropy trajectories between collapsed and healthy configurations at matched training steps across five experiments (Table~\\ref{tab:entropy_contrast}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Actor entropy comparison at matched time points. Collapsed and healthy configurations exhibit indistinguishable entropy at 55K steps (difference $= 0.03$ nats), despite collapsed runs showing severe return degradation.}\n\\label{tab:entropy_contrast}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Group} & \\textbf{Experiment} & \\textbf{5K} & \\textbf{25K} & \\textbf{45K} & \\textbf{55K} & \\textbf{Return} \\\\\n\\midrule\n\\multirow{2}{*}{Collapsed}\n & exp\\_008d (trained dt\\_emb) & 8.16 & $-1.86$ & $-4.58$ & $-4.88$ & ${\\sim}165$ \\\\\n & fixed\\_dt2 ($\\dt{=}2$) & 8.16 & $-3.02$ & $-5.06$ & $-5.17$ & ${\\sim}29$ \\\\\n\\midrule\n\\multirow{3}{*}{Healthy}\n & exp\\_008f (no dt\\_emb) & 8.11 & $-1.85$ & $-4.31$ & $-4.77$ & ${\\sim}460$ \\\\\n & exp\\_008a (unexposed) & 8.16 & $-4.88$ & $-5.20$ & $-5.21$ & ${\\sim}300$ \\\\\n & baseline\\_s1 ($\\dt{=}1$) & 8.10 & $-4.74$ & $-5.12$ & $-5.18$ & ${\\sim}950$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the last comparable step (55K): collapsed mean entropy $= -5.02$ (average of $-4.88$, $-5.17$); healthy mean entropy $= -5.05$ (average of $-4.77$, $-5.21$, $-5.18$); difference $= 0.03$ nats---statistically negligible. The hypothesis that collapsed runs exhibit anomalous entropy rise (actor confusion from delusional critic gradients) is not supported during the CIVO onset window.\n\nThe fixed\\_dt2 experiment demonstrates this most clearly: returns peak at ${\\sim}580$ (40K) then crash to 29 (72K), yet entropy remains stable at $-5.1$ throughout. The actor maintains a committed, low-entropy policy during the entire collapse---it does not become confused but rather remains confident while acting on incorrect value estimates. This is consistent with CIVO operating through critic value distortion rather than actor policy degradation. The late-stage entropy explosion documented in \\S\\ref{sec:civo_mechanism} ($+2.1$ nats/10K in EG~v4, onset ${\\sim}$35K steps after return collapse) occurs well beyond this window, confirming entropy rise as a lagging consequence rather than a concurrent or predictive signal.\n\n\\paragraph{Entropy descent speed.}\nEntropy descent rate correlates with temporal configuration complexity, not collapse fate. Simpler configurations (baseline $\\dt{=}1$, unexposed exp\\_008a) reach $-4.7$ by 25K, while configurations exposed to temporal variation (both collapsed and healthy) remain near $-2.0$ at 25K, reflecting the difficulty of policy commitment when training data spans multiple temporal scales.\n\n\\paragraph{Long-horizon entropy recovery.}\nThe baseline ($\\dt{=}1$) run extended to 505K steps shows entropy recovering from $-5.2$ to ${\\sim}{-}1.5$ between 115K and 295K steps, coinciding with continued performance improvement ($700 \\to 950$ return). This adaptive entropy increase rules out entropy rise as an inherently negative signal; the actor maintains ${\\sim}950$ return with entropy 3--4 nats above its minimum, indicating a healthy exploration--exploitation balance during extended training.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse patterns identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\\_v3\\_s2 and 038\\_s2); we present it as preliminary evidence that the trained $\\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\\ref{fig:multiple_pathways}).\n\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.\n\n\\subsection{Cross-Environment TCN Evaluation}\n\\label{sec:tcn_cross_env}\n\nTable~\\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\\times$ (35K+).}\n\\label{tab:tcn_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Env} & $\\sigma$ & \\textbf{Seed} & \\textbf{NVE$_{\\max}$} & \\textbf{Prevented?} & \\textbf{Eval (\\%)} \\\\\n\\midrule\nWalker & 0.1 & s0 & 1.02 & \\checkmark$^*$ & 55\\% \\\\\nWalker & 0.2 & s0 & 0.91 & \\checkmark & 91\\% \\\\\nWalker & 0.2 & s1 & 0.64 & \\checkmark & 45\\% \\\\\nWalker & 0.2 & s2 & 2.11$^\\dagger$ & $\\times$ & ${\\sim}5\\%$ \\\\\n\\rowcolor{gray!15}\nWalker & 0.2 & s3 & 3.04$^\\P$ & $\\times$ & 11\\% \\\\\nWalker & 0.5 & s0 & 3.97 & $\\times$ & 27\\% \\\\\nWalker & 0.5 & s1 & 1.64 & $\\times$ & 41\\% \\\\\n\\midrule\nCheetah & 0.2 & s0 & 1.90 & $\\times$ & crashed \\\\\nCheetah & 0.5 & s0 & 10.67 & $\\times$ & 26\\% \\\\\nCheetah & 1.0 & s0 & $\\leq$0.30 & \\checkmark$^\\S$ & 15\\% \\\\\n\\midrule\nPickCube & 0.2 & s0 & 3.71 & $\\times$ & failing \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Borderline: NVE${=}1.02\\times$ at 95K, below $1.5\\times$ threshold but above $1.0\\times$.\\\\\n$^\\dagger$NVE $= 2.11\\times$ at 95K, still rising; eval ${\\sim}5\\%$ of baseline.\\\\\n$^\\P$Late-onset CIVO: NVE declined to $0.67\\times$ at 95K before phase-transition-like spike to $3.04\\times$ at 105K; eval 349.6 at 95K $\\to$ 71.8 at 105K $\\to$ 104.5 at 215K.\\\\\n$^\\S$CIVO prevented (NVE${\\leq}0.30$); peak eval 116\\% baseline at 35K, declining to 15\\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\\par}\n\\end{table}\n\n\\paragraph{Cheetah Run $\\sigma{=}0.5$: transient spike with permanent eval damage.}\nCheetah $\\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\\times$ at 55K) followed by NVE recovery ($< 0.3\\times$ by 95K), but permanent evaluation damage (26\\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike persists within the observation window even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\\S\\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.\n\n\\paragraph{Cheetah Run $\\sigma{=}0.2$: insufficient dose.}\nAt $\\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\\times$ at 55K---exceeding the $1.5\\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\\times$ vs.\\ Walker's $2$--$6\\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.\n\n\\paragraph{PickCube-v1 $\\sigma{=}0.2$: manipulation failure.}\nPickCube reaches NVE $= 3.71\\times$ at 52.5K with $\\sigma{=}0.2$, indicating that TCN provides no protection in manipulation tasks. The combination of contact-gated dynamics and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.\n\n\\paragraph{Dose-response analysis.}\nWe observe $\\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\\times$ at 95K, still rising, eval ${\\sim}5\\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\\times$ at 95K before spiking to $3.04\\times$ at 105K (eval 349.6 $\\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\\sigma{=}0.1$ as insufficient (NVE $= 1.02\\times$---borderline, eval 55\\%); above it, $\\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\\leq 41\\%$). Cross-seed variance at $\\sigma{=}0.2$ (eval 5--91\\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \\emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.\n\n\\paragraph{Cheetah Run ``impossible dose'' dilemma.}\nExp\\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\\sigma{=}1.0$, CIVO is eliminated (NVE${\\leq}0.30$ throughout) and initial learning is \\emph{unimpaired}: peak eval reaches 372 at 35K (116\\% of baseline), demonstrating that $\\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\\% of baseline)---while the critic remains well-calibrated (value\\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \\emph{policy degradation $\\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.\n\nThis ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\\times$ NVE) requires $\\sigma \\geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\\sigma{=}0.2$; on Cheetah, the effective dose ($\\sigma \\geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.\n\n\\section{DreamerV3 Hyperparameters}\n\\label{sec:hyperparameters}\n\nTable~\\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\\texttt{dmc\\_proprio}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\\diamond$.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{World Model}} \\\\\nRSSM discrete states & 32 classes $\\times$ 32 categories \\\\\nRSSM stochastic dim & 32 \\\\\nRSSM deterministic dim & 512 \\\\\nMLP hidden size & 512 \\\\\nMLP layers & 2 \\\\\nActivation & SiLU \\\\\nNormalization & LayerNorm \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Training}} \\\\\nBatch size & 16 sequences $\\times$ 64 steps \\\\\nLearning rate & $3 \\times 10^{-4}$ (Adam, $\\epsilon{=}10^{-8}$) \\\\\nSequence length & 64 \\\\\nTraining ratio & 512 \\\\\nFree nats & 1.0 \\\\\nKL balance ($\\alpha$) & 0.8 \\\\\nDiscount ($\\gamma$) & 0.997 \\\\\n$\\lambda$-return & 0.95 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Policy}} \\\\\nImagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\nActor entropy scale & $3 \\times 10^{-4}$ \\\\\nActor gradient & Reinforce + dynamics backprop \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Temporal Abstraction}$^\\diamond$} \\\\\nGate enabled & True (all non-baseline) \\\\\nGate fixed $\\dt$ & 1 or 2 (per config) \\\\\nSubsample max $\\dt$ & 1 (OFF) or 2 (ON) \\\\\n$\\dt$-embedding dim & 32 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Environment}} \\\\\nAction repeat & 2 (Walker Walk, Cheetah Run) \\\\\nObservation & Proprioceptive (no pixels) \\\\\nTotal environment steps & 105K \\\\\nEvaluation frequency & Every 10K steps \\\\\nEvaluation episodes & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Online CIVO Detector Details}\n\\label{sec:detector_appendix}\n\nThis appendix provides the full algorithm specification and validation results for the online CIVO detector described in \\S\\ref{sec:detector}.\n\n\\subsection{Algorithm Specification}\n\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \\S\\ref{sec:appendix_sensitivity}.\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).\n\n\\subsection{Validation Results}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n009c s3 & no $\\dt$-emb & TN & -- & -- & 457 & -- \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/9 (0.22)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.\n\n\\subsection{Cross-Simulator Specificity (PickCube)}\n\nExp\\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a dense-reward manipulation task. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\\times$ at 72.5K), establishing environment-specific origin independent of $\\dt$-embedding training.\n\n\\subsection{Detector Limitations}\n\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \\emph{pattern} rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.\n\n\\section{Dual-Critic Mechanism Ablation}\n\\label{sec:dual_critic_appendix}\n\n\\subsection{\\texorpdfstring{$2{\\times}2$}{2x2} Factorial Design}\n\nWe ablate the critic architecture in a $2{\\times}2$ factorial: \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} parameters. Table~\\ref{tab:dual_critic_full} reports all configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Dual-critic $2{\\times}2$ factorial results. Walker Walk unless noted.}\n\\label{tab:dual_critic_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Params} & \\textbf{NVE} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\n008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\n033 & Wide single & 2.4M & 4.75$\\times$ & 407.9 & CIVO $\\to$ self-repair \\\\\n035 s0 & Narrow dual (min) & 1.2M & 2.75$\\times$ & 697.8 & CIVO $\\to$ recovery \\\\\n039 s1 & Narrow dual (min) & 1.2M & 2.19$\\times$ & 592.7 & CIVO $\\to$ recovery \\\\\n032 s0 & Wide dual (min) & 2.4M & $\\leq$1.1$\\times$ & 739.7 & CIVO prevented \\\\\n032b s1 & Wide dual (min) & 2.4M & 1.4$\\times$ & 551.8 & CIVO prevented \\\\\n038 s2 & Wide dual (min) & 2.4M & $\\leq$0.3$\\times$ & 120.9$^*$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Cross-environment}} \\\\\n034 & Cheetah dual & 2.4M & 1.75$\\times$ & 97.5 & Partial recovery (31\\%) \\\\\n037 & Cheetah wide single & 2.4M & 3.60$\\times$ & 146.1 & CIVO $\\to$ self-repair \\\\\n036 & PickCube dual & 2.4M & 2.3$\\times$ & 27.7 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$CIVO prevented (NVE $\\leq 0.3\\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\\par}\n\\end{table}\n\n\\subsection{Critic Convergence (\\texorpdfstring{$v_1 \\approx v_2$}{v1 ≈ v2})}\n\nAcross all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\\mathbb{E}[\\max(v_1, v_2) - \\min(v_1, v_2)]$ is 3--4\\% of the theoretical bound for independent critics.\n\nThis convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.\n\n\\subsection{Recovery vs.\\ Prevention Mechanism}\n\nThe $2{\\times}2$ factorial reveals two separable dimensions:\n\n\\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\\_035 (s0, $\\nve = 2.75\\times$, eval $33.8 \\to 697.8$, recovery ratio $20.6\\times$) and exp\\_039 (s1, $\\nve = 2.19\\times$, eval $35.9 \\to 592.7$, recovery ratio $16.5\\times$). Both outperform wide single-critic (exp\\_033, 2.4M params, eval 407.9) despite $2\\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\\times$ vs.\\ 4.75$\\times$ for the comparable single-critic) and enables consistent full recovery across seeds.\n\n\\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\n\n\\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\\_034) reduces NVE from $8.27\\times$ (untreated baseline) to $1.75\\times$ ($\\geq 4\\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.\n",
    "structuredPatch": [
      {
        "oldStart": 69,
        "oldLines": 7,
        "newStart": 69,
        "newLines": 10,
        "lines": [
          " 024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\",
          " 008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\",
          " 008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\",
          "+077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\\times$ & Healthy \\\\",
          " \\rowcolor{gray!15}",
          "+078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\\times$ & Onset (self-corr.) \\\\",
          "+\\rowcolor{gray!15}",
          " 019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\",
          " 054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\",
          " 049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\"
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

_source line 39_

Let me verify the edit looks correct in context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "7587cda6-5c47-47e1-a9e8-09ae3d8199f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014v3ABRMCfp2padBYg1n5zi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 44378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
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

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01CY6X3YbnT8HjQeCxxxQ9bJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 60,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "2258828a-56dc-4882-bd06-0b03bf187519",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014v3ABRMCfp2padBYg1n5zi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 44378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
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

_source line 41 · 2026-05-25T15:54:15.447Z_

<details><summary>↩ Tool result · `toolu_01CY6X3YbnT8HjQeCxxxQ9bJ`</summary>

```text
60	\midrule
61	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
62	\rowcolor{gray!15}
63	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
64	\rowcolor{gray!15}
65	010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\times$ & Full collapse \\
66	\rowcolor{gray!15}
67	021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Transient CIVO (self-corr.) \\
68	024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
69	024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
70	008a\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\times$ & Healthy \\
71	008a\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\times$ & Healthy \\
72	077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\times$ & Healthy \\
73	\rowcolor{gray!15}
74	078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\times$ & Onset (self-corr.) \\
75	\rowcolor{gray!15}
76	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
77	054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\times$$^h$ & Env.\ transient (ctrl) \\
78	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^f$ & Env.\ transient \\
79	052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\times$$^f$ & Env.\ transient \\
80	051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\times$$^f$ & Env.\ transient (ctrl) \\
81	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^g$ & Env.\ dynamics \\
82	053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\times$$^g$ & Env.\ dynamics (ctrl) \\
83	055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\times$$^g$ & Env.\ dynamics \\
84	056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\times$$^g$ & Env.\ dynamics (ctrl) \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "623fe10a-c1f8-4899-9910-065a66186166",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\\times$ & Onset (self-corr.) \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\",
      "numLines": 25,
      "startLine": 60,
      "totalLines": 1173
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

Now let me also update the table caption to reflect the new total count (was 43, now 45).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "2523489d-1038-47a7-b5c9-41fcf32a6597",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtEWo9dMxzBkMkQ1pHU4g2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 45025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1172
      },
      "output_tokens": 4,
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

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01K32jHJPz5zMJNevKHb4CeP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "offset": 6,
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "c28916e6-42b1-4fea-9b46-f4a6f12cab82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtEWo9dMxzBkMkQ1pHU4g2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1172,
      "cache_read_input_tokens": 45025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1172
      },
      "output_tokens": 4,
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

_source line 44 · 2026-05-25T15:54:21.127Z_

<details><summary>↩ Tool result · `toolu_01K32jHJPz5zMJNevKHb4CeP`</summary>

```text
6	Table~\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "f5178705-b4af-43c5-a5d3-ad742467e13b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "Table~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).",
      "numLines": 1,
      "startLine": 6,
      "totalLines": 1173
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01XFTP3ha8STvitvdQAFkWZo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "old_string": "reports all 43 experimental configurations",
  "new_string": "reports all 45 experimental configurations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "a8ac712f-b355-4a6b-a2d4-238703838f81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RuMVSPTXUvoYnGrkyYZpzT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 46197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
      },
      "output_tokens": 67,
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

_source line 46 · 2026-05-25T15:54:24.010Z_

<details><summary>↩ Tool result · `toolu_01XFTP3ha8STvitvdQAFkWZo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "e5c35d30-4361-471d-be71-e69b0b48e16e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
    "oldString": "reports all 43 experimental configurations",
    "newString": "reports all 45 experimental configurations",
    "originalFile": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\\heartsuit$ & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Collapse$^\\dagger$ \\\\\n\\rowcolor{gray!15}\n068 & Factorial repro (s1) & trn & ON & 8 & 39.1 @105K & 4.12$\\times$ & Full collapse \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 289.3 @105K & 0.76$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n008a\\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n067 & Frozen emb (s0) & frz$^b$ & ON & 8 & 281.5 @105K & 0.19$\\times$ & Healthy \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n008e\\_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.61$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n077 & Cheetah baseline (s0) & --- & --- & 15 & 448.1 @105K & 1.00$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n078 & Cheetah trigger (s0) & trn & ON & 8 & 119.5 @105K & 4.10$\\times$ & Onset (self-corr.) \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cartpole Swingup}} \\\\\n060 & Cartpole baseline (3 seeds) & --- & --- & 15 & 557.0 @105K$^i$ & --- & Healthy \\\\\n061 & Cartpole trigger (3 seeds) & trn & ON & 8 & 236.3 @105K$^i$ & --- & No CIVO \\\\\n062 & Cartpole control (3 seeds) & --- & ON & 8 & 244.8 @105K$^i$ & --- & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^\\dagger$ NVE self-corrected ($4.72\\times$ $\\to$ $1.22\\times$) but policy did not recover (eval 10.5\\% of baseline).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\\\\n$^\\heartsuit$ Evaluated at 55K steps due to early termination of exp\\_008d; extended run (exp\\_009e) reached 131.08 at 105K.\\\\\n$^i$ Cartpole: exp\\_060 reports seed~2 eval only; exp\\_061/062 report 3-seed mean.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\midrule\nLocomotion & Cartpole Swingup & 0/3 & 0/3 & No (single-joint) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cartpole Swingup.} Cartpole Swingup (single-DoF locomotion) serves as a cross-environment control. Three seeds of the CIVO-trigger configuration (exp\\_061: trained $e_{\\dt}$, subsample ON, $H{=}8$, $\\dt{=}2$) and three seeds of the no-embedding control (exp\\_062) both produce zero CIVO onset. Despite using the hyperparameter combination that triggers collapse in all 10 tested multi-joint locomotion seeds (Walker/Cheetah), the single-joint Cartpole shows no CIVO, confirming the phenomenon requires multi-joint dynamics where temporal abstraction amplifies the reward fidelity gap.\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eleven factorial experiments (including four 008e\\_v3 seeds and exp\\_059). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n059          & 4.72 & self-correcting CIVO & $-$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 0.917$ because exp\\_059 (NVE${=}4.72\\times$, self-correcting CIVO, B1-negative) ranks above two sustained-CIVO positives ($4.12\\times$, $4.02\\times$), breaking the perfect rank separation that held before its inclusion. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value (accuracy $10/11 = 90.9\\%$). Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.967$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=8$, $n=11$, $\\text{AUROC}=0.917$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$; exp\\_059 (NVE${=}4.72\\times$, B1-negative) is the sole false positive.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 4 & 0 & 4 & 63.6\\% \\; [30.8, 89.1] & 42.9\\% & 100\\% & 60.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 3 & 0 & 5 & 72.7\\% \\; [39.0, 94.0] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 3 & 3 & 0 & 5 & 72.7\\% \\; [39.0, 94.0] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 2 & 0 & 6 & 81.8\\% \\; [48.2, 97.7] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 2 & 0 & 6 & 81.8\\% \\; [48.2, 97.7] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 1 & 0 & 7 & 90.9\\% \\; [58.7, 99.8] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=5$, $n_{\\text{neg}}=6$, $n=11$, $\\text{AUROC}=0.967$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 5 & 2 & 0 & 4 & 81.8\\% \\; [48.2, 97.7] & 71.4\\% & 100\\% & 83.3\\% \\\\\n$\\geq 1.2\\times$ & 5 & 1 & 0 & 5 & 90.9\\% \\; [58.7, 99.8] & 83.3\\% & 100\\% & 90.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 5 & 1 & 0 & 5 & 90.9\\% \\; [58.7, 99.8] & 83.3\\% & 100\\% & 90.9\\% \\\\\n$\\geq 1.7\\times$ & 4 & 1 & 1 & 5 & 81.8\\% \\; [48.2, 97.7] & 80.0\\% & 80.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 4 & 1 & 1 & 5 & 81.8\\% \\; [48.2, 97.7] & 80.0\\% & 80.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 4 & 0 & 1 & 6 & 90.9\\% \\; [58.7, 99.8] & 100\\% & 80.0\\% & 88.9\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=9$, $n_{\\text{neg}}=8$, $n=17$, $\\text{AUROC}=0.972$). Includes Walker Walk (15 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 9 & 2 & 0 & 6 & 88.2\\% \\; [63.6, 98.5] & 81.8\\% & 100\\% & 90.0\\% \\\\\n$\\geq 1.2\\times$ & 9 & 1 & 0 & 7 & 94.1\\% \\; [71.3, 99.9] & 90.0\\% & 100\\% & 94.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 9 & 1 & 0 & 7 & 94.1\\% \\; [71.3, 99.9] & 90.0\\% & 100\\% & 94.7\\% \\\\\n$\\geq 1.7\\times$ & 7 & 1 & 2 & 7 & 82.4\\% \\; [56.6, 96.2] & 87.5\\% & 77.8\\% & 82.4\\% \\\\\n$\\geq 2.0\\times$ & 7 & 1 & 2 & 7 & 82.4\\% \\; [56.6, 96.2] & 87.5\\% & 77.8\\% & 82.4\\% \\\\\n$\\geq 3.9\\times$ & 7 & 0 & 2 & 8 & 88.2\\% \\; [63.6, 98.5] & 100\\% & 77.8\\% & 87.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all five CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 80.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 90.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), the optimal threshold $\\nve \\geq 3.9\\times$ achieves $10/11$ accuracy ($90.9\\%$, 95\\% CI: [58.7\\%, 99.8\\%]); the sole false positive is exp\\_059 (NVE${=}4.72\\times$, self-correcting CIVO classified as B1-negative).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}17$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}56$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}56$ configurations, AUROC${=}0.990$, comprehensive validation). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.09$, accuracy${=}53/56$, F1${=}0.941$. Three false positives arise from non-CIVO value overestimation: mitigation transient VE spike (008e\\_v3 subsample, $1.93\\times$) and frozen embedding transients (047, $1.71\\times$; 057, $1.88\\times$). Threshold calibrated and validated post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_threshold_prf.pdf}\n\\caption{Precision, Recall, and F1 as a function of NVE threshold ($n{=}56$ configurations). Peak F1${=}0.941$ at $\\tau{=}1.5\\times$, where recall remains perfect ($1.00$) and precision${=}0.889$. The plateau of high F1 across $\\tau \\in [1.5, 1.7]$ indicates robustness to threshold selection.}\n\\label{fig:nve_prf}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\paragraph{Comprehensive validation ($n{=}56$).}\nExpanding the evaluation set to all classifiable experiments yields $n{=}56$ ($n_{\\text{pos}}{=}24$, $n_{\\text{neg}}{=}32$), spanning Walker Walk, Cheetah Run, and multiple intervention configurations (SGS, TCN, dual-critic, frozen embedding). At the $1.5\\times$ threshold: AUROC${=}0.990$, precision${=}0.889$, recall${=}1.000$, F1${=}0.941$, accuracy${=}53/56$. The three false positives are: exp\\_008e\\_v3\\_subsample ($1.93\\times$, mitigation config with transient VE spike), exp\\_047 ($1.71\\times$, frozen embedding transient), and exp\\_057 ($1.88\\times$, frozen embedding transient). All 24 CIVO-positive configurations are correctly detected (FN${=}0$), with CIVO-positive NVE ranging from $1.53\\times$ (008d seed~3, late-onset) to $70.64\\times$ (010b seed~0, Cheetah). The substantial increase in sample size from $n{=}32$ to $n{=}56$ strengthens confidence in the $1.5\\times$ threshold as a robust diagnostic boundary.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the single-seed baseline (seed~1, exp\\_001, 505K steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} The initial $n{=}11$ analysis had wide Clopper-Pearson confidence intervals (e.g., 90.9\\% accuracy, 95\\% CI [58.7\\%, 99.8\\%]). The comprehensive evaluation ($n{=}56$, AUROC${=}0.990$, F1${=}0.941$; Figure~\\ref{fig:nve_roc}) substantially tightens these bounds. Table~\\ref{tab:sensitivity_b2_full} reports the $n{=}17$ two-environment core evaluation. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}15$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 20 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 17 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 15 & $(1.00,\\, 3.78)$ & 14/15 (0.933) & 0.963 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.978} & \\textbf{0.988} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe threshold $\\theta{=}1.5\\times$ falls within the optimal accuracy range for all three training folds: $(1.45, 1.53]$ when Walker data is available, and the wider $(1.00, 3.78)$ when training on Cheetah$+$PickCube only (where CIVO and non-CIVO NVE values are well-separated). The single cross-validation error is exp\\_008e\\_v3 seed~2 (Walker), an IRD collapse mechanistically distinct from CIVO (\\S\\ref{sec:roc_analysis}). Mean held-out accuracy is 0.978 and mean AUROC is 0.988, confirming that $\\theta{=}1.5\\times$ generalizes across environments without retuning.\nPickCube fold confidence intervals remain wide (Clopper-Pearson 95\\% CI: $[0.158, 1.000]$) due to $N_{\\text{test}}{=}2$.\n\n\\subsection{Leave-One-Config-Out Cross-Validation}\n\\label{sec:nve_loco}\n\n\\paragraph{Leave-One-Config-Out Cross-Validation.}\nTo rule out threshold overfitting to any particular experimental configuration, we perform leave-one-config-out (LOCO) cross-validation over $K{=}12$ configuration groups (e.g., \\texttt{008d\\_civo\\_trigger}, \\texttt{frozen\\_dt\\_emb}, \\texttt{tcn}; $n{=}56$ total). Each fold holds out all experiments from one configuration, selects the F1-maximizing threshold on the remaining $K{-}1$ groups, and evaluates on the held-out group.\n\nIn $10/12$ folds, the training-optimal threshold falls within $\\pm 0.05$ of $\\theta{=}1.5\\times$ (mean $1.61 \\pm 0.23$, range $[1.47, 2.12]$). The two folds selecting a higher threshold ($\\theta{=}2.1$; \\texttt{008d\\_civo\\_trigger} and \\texttt{tcn}, both predominantly CIVO-positive) perform \\emph{worse} on their held-out sets than $\\theta{=}1.5$ (accuracy $0.78$/$0.88$ vs.\\ $1.00$/$1.00$), confirming that the fixed threshold generalizes better than per-fold optimization in these cases. Cross-validated accuracy at $\\theta{=}1.5$ is $53/56 = 94.6\\%$, identical to the in-sample result, with train AUROC consistently high across folds ($0.988 \\pm 0.003$). The three misclassifications are the same mechanistically distinct false positives identified in \\S\\ref{sec:roc_analysis}: two frozen-embedding transients (exp\\_047, exp\\_057) and one mitigation-config transient (exp\\_008e\\_v3\\_subsample). No CIVO-positive configuration is missed in any fold (FN${=}0$ across all 12 folds).\n\n% --- APPENDIX B: Factorial Ablation Details ---\n\n\\section{Factorial Ablation Details}\n\\label{sec:appendix_factorial}\n\nThis appendix provides the full factorial ablation results summarized in \\S\\ref{sec:f3f5_summary} of the main text.\n\n\\paragraph{Embedding gradient analysis.}\nTable~\\ref{tab:three_way_emb} isolates embedding \\emph{trainability} as the necessary condition for CIVO by comparing four gradient conditions under otherwise identical configurations ($H{=}8$, subsample ON, $\\dt{=}2$ imagination).\n\n\\begin{table}[h]\n\\centering\n\\caption{$\\dt$-embedding gradient conditions on Walker Walk. Any gradient pathway updating $e_{\\dt}$ is sufficient to induce CIVO; freezing or removing the embedding dramatically reduces severity.}\n\\label{tab:three_way_emb}\n\\footnotesize\n\\begin{tabular}{lccccl}\n\\toprule\nCondition & Grad flow & Exp(s) & NVE peak & Eval & CIVO \\\\\n\\midrule\nTrained & all & 008d, 059 & $1.53$--$4.72\\times$ & 64--268 & 5/5 \\\\\nReward detach & obs+KL only & 044 & $4.45\\times$ & 44$\\to$538$^\\dagger$ & 1/1 \\\\\nFull SGS & KL only & 018 & $1.66\\times$ & 448 & 1/1$^*$ \\\\\nFrozen & none & 042, 015b, 047, 057 & $0.19$--$1.88\\times$$^\\ddagger$ & 204--612 & 2/4 \\\\\nRemoved & N/A & 008f & $0.97$--$1.41\\times$ & 307--503 & 0/3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Full-SGS seed~1 (NVE $1.66\\times$); seed~2 collapsed. $^\\dagger$Self-corrected at ${\\sim}175$K (eval 44$\\to$538, 59\\% baseline; 224K run). $^\\ddagger$Exp\\_047 (NVE $1.71\\times$) and Exp\\_057 (NVE $1.88\\times$): both transient, self-correcting within 20K steps.\\par}\n\\end{table}\n\n\\paragraph{Controlled three-way causal ablation.}\nExperiments 067--069 provide a minimal causal ablation on Walker Walk (seed${=}1$), varying \\emph{only} the $\\dt$-embedding treatment while holding all other hyperparameters fixed ($H{=}8$, subsample ON, $\\dt{=}2$ imagination). Table~\\ref{tab:causal_ablation} shows that trained $\\dt$-embedding is necessary and sufficient for CIVO: freezing the embedding (gradient flow blocked, embedding weights still present) eliminates CIVO as completely as removing the embedding ($d{=}0$), ruling out the alternative hypothesis that embedding \\emph{presence} alone causes CIVO. Combined with all prior seeds, trained $\\dt$-embedding triggers CIVO in 10/10 multi-joint locomotion seeds (8 Walker, 2 Cheetah) versus 0/5 controls (0/3 no-embedding, 0/2 frozen; Fisher exact $p < 0.001$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Three-way causal ablation (Walker Walk, seed${=}1$). Only the $\\dt$-embedding treatment varies; all other configuration is identical. Trained embedding triggers CIVO; frozen and removed do not.}\n\\label{tab:causal_ablation}\n\\footnotesize\n\\begin{tabular}{llccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Embedding} & \\textbf{NVE peak} & \\textbf{Eval final} & \\textbf{CIVO} \\\\\n\\midrule\n\\rowcolor{gray!15}\n068 & Trained ($d{=}32$) & $6.57\\times$ & 39.1 & Yes (alert @85K) \\\\\n067 & Frozen ($d{=}32$, \\texttt{req\\_grad=F}) & $0.40\\times$ & 281.5 & No \\\\\n069 & Removed ($d{=}0$) & $0.66\\times$ & 237.8 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reward-detach condition (exp\\_044, \\texttt{reward\\_dt\\_emb\\_detach=True}) uses a backward hook to block reward-head gradients from reaching $e_{\\dt}$, complementing the framework-level Reward SGS (exp\\_016e). Both yield the same directional result---CIVO onset not prevented---ruling out implementation artifacts. Exp\\_044 exhibits delayed CIVO onset (${\\sim}95$K vs.\\ typical $25$--$35$K), consistent with reduced but non-zero gradient pressure on $e_{\\dt}$. Over a full 224K run, exp\\_044 self-corrects: eval recovers from 44 (95K) to 538 (215K, 59\\% baseline), but this recovery is incomplete compared to spontaneous recovery without gradient intervention (exp\\_045: 868, 95\\% baseline). The lower asymptote suggests that selectively disrupting gradient flow may create optimization difficulties beyond CIVO itself.\n\nTable~\\ref{tab:factorial_design} summarizes the experimental configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Factorial design. Each row specifies one experimental configuration. \\textbf{Emb}: $\\dt$-embedding mode. \\textbf{Sub}: temporal subsampling. \\textbf{H}: imagination horizon. \\textbf{Imag $\\dt$}: temporal resolution used during imagination.}\n\\label{tab:factorial_design}\n\\small\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{ID} & \\textbf{Purpose} & \\textbf{Emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Imag $\\dt$} \\\\\n\\midrule\n001 & Reference baseline & --- & --- & 15 & 1 \\\\\n006 & Fixed $\\dt{=}2$ & trn & on & 15 & 2 \\\\\n007 & Fixed $\\dt{=}4$ & trn & on & 15 & 4 \\\\\n\\midrule\n008a & Unexposed emb ctrl & exp$^a$ & off & 15 & 2 \\\\\n008c & Horizon control & exp$^a$ & off & 8 & 2 \\\\\n008d & Collapse condition & trn & on & 8 & 2 \\\\\n008e\\_v3 & $\\dt{=}1$ imag control & trn & on & 15 & 1 \\\\\n008f & Causal ablation & --- & on & 8 & 2 \\\\\n\\midrule\n015b & Frozen-emb ctrl & frz$^b$ & on & 8 & 2 \\\\\n016e & Stop-grad (reward) & trn$^\\dagger$ & on & 8 & 2 \\\\\n018 & Full-SGS & trn$^\\ddagger$ & on & 8 & 2 \\\\\n\\midrule\n005 & Learned gate & adaptive & off & 15 & learned \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, exposed to $\\dt{>}1$ data via subsample ON);\nexp$^a$ = trained ($d{=}32$) but never exposed to $\\dt{>}1$ data (subsample OFF);\nfrz$^b$ = frozen random projection ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^\\dagger$ \\texttt{reward\\_dt\\_emb\\_detach=True}; $^\\ddagger$ all non-KL gradients to \\texttt{dt\\_emb} detached.\\par}\n\\end{table}\n\n\\subsection{F3: Unexposed Temporal Embedding Suppresses Value Drift}\n\\label{sec:f3}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_factorial_grid.pdf}\n\\caption{Factorial isolation of CIVO trigger. Only the combination of trained $e_{\\dt}$ and multi-rate data (upper-left cell) produces pathological NVE. Neither factor alone is sufficient.}\n\\label{fig:factorial_grid}\n\\end{figure}\n\nThe empirical finding that trained embedding \\emph{plus} multi-rate exposure jointly predict CIVO rests on two complementary controls that each remove one factor while holding the other constant.\n\n\\paragraph{Evidence A: exposure is necessary (exp\\_008a).}\nExp\\_008a uses a trained embedding ($d{=}32$, gradients enabled) that is never exposed to $\\dt{>}1$ transitions during world-model training (subsample OFF). Despite sharing the same embedding architecture as exp\\_008d, its NVE remains in the $0.83$--$0.93\\times$ range across 3 seeds (105K steps). Performance follows two V-shaped recovery cycles, reaching 777.7 at 105K (85\\% of baseline). The critical factor is not the embedding's capacity to represent temporal information, but its adaptation to multi-rate data that enables precise but inaccurate $\\dt{>}1$ state predictions within the RSSM.\n\nThis contrasts with exp\\_006 (trained $e_{\\dt}$, subsample ON, $H{=}15$), where NVE accelerates from $1.61\\times$ at 45K to $2.31\\times$ at 55K before catastrophic collapse to 132.9 at 65K. Both experiments use identical trained embeddings ($d{=}32$, gradients enabled) and $H{=}15$, differing only in whether the world model sees $\\dt{>}1$ transitions during training. This confirms that multi-rate data exposure, not embedding architecture, is the operative variable.\n\n\\paragraph{Evidence B: trainability is necessary (exp\\_015b).}\nExp\\_015b uses a frozen random-projection embedding ($d{=}32$, \\texttt{requires\\_grad=False}, subsample ON, $H{=}8$), the same multi-rate data regime as exp\\_008d, but with a non-trainable temporal signal. Despite full exposure to $\\dt{>}1$ transitions, the NVE peaks at $1.45\\times$ at 55K but does not sustain escalation: it retreats to $0.65\\times$ by 65K and settles at $0.42\\times$ by 105K (trajectory: $0.81 \\rightarrow 1.26 \\rightarrow 1.45 \\rightarrow 0.65 \\rightarrow 1.05 \\rightarrow 0.47 \\rightarrow 0.39 \\rightarrow 0.42$). The transient peak approaches but does not exceed the $1.5\\times$ CIVO threshold, and critically, the ratio self-corrects rather than exhibiting the monotonic escalation seen in trained-embedding runs. Final evaluation reaches only 204.2 at 105K, low but through a qualitatively different failure mode than CIVO. Actor loss approaches zero (gradient starvation; see \\S\\ref{sec:pathways}), the frozen embedding provides no useful gradient signal for temporal adaptation.\n\nThe contrast with exp\\_008d is stark: under identical data conditions (subsample ON, $H{=}8$), the trained embedding drives NVE to $4.12\\times$ with sustained monotonic escalation ($1.78 \\rightarrow 1.71 \\rightarrow 2.09 \\rightarrow 4.12$) and precedes full collapse (eval 82.8), while the frozen embedding peaks transiently at $1.45\\times$ before self-correcting to $0.42\\times$, a qualitative difference between sustained and transient overestimation. This demonstrates that a $\\dt$-embedding must be able to \\emph{co-adapt} with RSSM dynamics to produce the systematic reward-prediction bias that drives CIVO; a static random projection, regardless of its exposure to multi-rate data, cannot create this bias.\n\nTogether, these two controls establish that in all tested configurations, CIVO occurs only with the \\emph{joint} presence of (i)~a trainable embedding that can co-adapt with RSSM dynamics, and (ii)~multi-rate training data that drives this co-adaptation toward biased temporal predictions. Neither factor alone is sufficient.\n\nCross-environment validation on Cheetah Run replicates the empirical pattern: trained $e_{\\dt}$ precedes CIVO in both tested seeds (exp\\_010b, 2 seeds, NVE $8.27$--$108.52\\times$, collapse to 51.7/0.83) while removing the embedding eliminates it (exp\\_024b, 2 seeds, NVE $<0.2\\times$, eval 96.5/77.3). Freezing the embedding on Cheetah (exp\\_046, NVE${=}1.35\\times$ vs.\\ trained $70.64\\times$, a $52\\times$ reduction) further confirms that embedding trainability, not architecture, drives CIVO. This extends the sufficiency finding from Walker Walk to a second locomotion environment with qualitatively different dynamics (6-joint vs.\\ 2-joint).\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Causal isolation: $e_{\\dt}$ configuration $\\times$ multi-rate data exposure. The combination of trained embedding and multi-rate exposure is the sole predictor of CIVO in tested configurations. Neither factor alone is sufficient.}\n\\label{tab:causal_matrix}\n\\begin{tabular}{lcc}\n\\toprule\n& Multi-rate data (\\textsc{on}) & Single-rate data (\\textsc{off}) \\\\\n\\midrule\nTrained $e_{\\dt}$ & exp\\_008d: \\textbf{CIVO} & exp\\_008a: healthy \\\\\n & NVE 4.12$\\times$, collapse & NVE 0.93$\\times$ \\\\\n\\midrule\nFrozen $e_{\\dt}$ & exp\\_015b: grad.\\ starvation & --- \\\\\n & peak NVE 1.45$\\times$ (transient) & \\\\\n\\midrule\nRemoved $e_{\\dt}$ & exp\\_008f: no CIVO & --- \\\\\n & NVE $\\leq$0.97$\\times$ & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOnly the upper-left cell (trained embedding with multi-rate exposure) precedes CIVO (Table~\\ref{tab:causal_matrix}). This 2$\\times$2 structure establishes that both factors are jointly sufficient in tested configurations.\n\n\\subsection{F4: Degradation Scales Monotonically with \\texorpdfstring{$\\dt$}{dt}}\n\\label{sec:f4}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig5_dt_amplification.pdf}\n\\caption{Peak evaluation return as a function of imagination $\\dt$. Performance degrades monotonically: $\\dt{=}1$ (915.7) $>$ $\\dt{=}2$ (485.3, $-47\\%$) $>$ $\\dt{=}4$ (176.9, $-81\\%$).}\n\\label{fig:dt_amplification}\n\\end{figure}\n\nThe magnitude of degradation scales monotonically with the imagination step size (Figure~\\ref{fig:dt_amplification}). From the $\\dt{=}1$ baseline (915.7 at 105K), fixed $\\dt{=}2$ (exp\\_006) achieves a peak of only 485.3 ($-47\\%$), and fixed $\\dt{=}4$ (exp\\_007) peaks at 176.9 ($-81\\%$). This monotonic relationship is consistent with compounding model error: larger temporal gaps amplify the RSSM's prediction inaccuracy at each imagination step, and these errors accumulate across the rollout horizon.\n\n\\subsection{F5: Imagination Horizon and Subsampling Are Secondary Factors}\n\\label{sec:f5}\n\nNeither horizon length nor temporal subsampling precedes collapse without multi-rate data exposure: both trained-but-unexposed configurations (008a, 008c) maintain $\\nve < 0.93\\times$ (\\S\\ref{sec:f3}), while the trained-and-exposed counterpart (008d) collapses with $\\nve = 4.12\\times$.  The no-embedding configurations show cross-seed variance (008f: 503.0 vs.\\ 009c: 148.3) but neither exhibits $\\nve > 1.5\\times$; low evaluation alone does not indicate CIVO.\n\nThe $3.2\\times$ performance gap (008a: 777.7 vs.\\ 008c: 240.9) quantifies the horizon effect independently of CIVO, as both conditions maintain healthy NVE ($\\leq$0.93$\\times$).\n\n% --- APPENDIX C: Full Analysis & Discussion ---\n\n\\section{Full Analysis \\& Discussion}\n\\label{sec:appendix_analysis}\n\nThis appendix provides the complete mechanistic analysis summarized in Section~\\ref{sec:discussion} of the main text.\n\n\\subsection{The CIVO Mechanism}\n\\label{sec:civo_mechanism}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig4_mechanism_diagram.pdf}\n\\caption{CIVO mechanism diagram. The trained $\\dt$-embedding enables asymmetric reward prediction fidelity, initiating a feedback loop: biased RSSM rewards $\\to$ optimistic critic values $\\to$ actor exploitation $\\to$ reinforced state-distribution skew.}\n\\label{fig:civo_mechanism}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity at $\\dt{=}1$ vs.\\ $\\dt{=}2$. Trained embedding (008d) produces $2.78\\times$ reward gap; removing it (008f) eliminates the gap but degrades absolute prediction.}\n\\label{tab:rssm_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline & 13.49 & 27.50 & 2.04$\\times$ & 0.0102 & 0.0159 & 1.56$\\times$ \\\\\n008d (trained) & 41.31 & 53.67 & 1.30$\\times$ & 0.0568 & 0.1579 & 2.78$\\times$ \\\\\n008f (no emb) & 8.01 & 22.04 & 2.75$\\times$ & 0.7469 & 0.7526 & 1.01$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe RSSM fidelity analysis (Table~\\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO (Figure~\\ref{fig:civo_mechanism}).  The trained $\\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\\dt{=}1$ is $0.0568$, while at $\\dt{=}2$ it rises to $0.1579$, a $2.78\\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\\times$ gap, and the baseline shows $1.56\\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.\n\nThis asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\\dt$-embedding causes RSSM predictions at $\\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\\nve$ above $1.5\\times$, followed by evaluation collapse.\n\nA random-policy control experiment ($N{=}100$ rollouts, 95\\% bootstrap CI) decomposes CIVO into two necessary stages.  \\textbf{Stage~1 (dynamics bias):} even under a random policy, $\\dt{=}2$ imagination produces $1.68\\times$ higher mean reward than $\\dt{=}1$ in the trained-embedding model (008d): the RSSM prior already generates reward-favorable trajectories at $\\dt > 1$, independent of actor behavior.  \\textbf{Stage~2 (actor exploitation):} the trained actor learns to exploit these biased regions, amplifying the ratio to $2.90\\times$.  In the no-embedding control (008f), neither stage is present: the random-policy ratio is $1.11\\times$ and the trained-actor ratio is $0.98\\times$.  The decomposition attributes $\\approx 36\\%$ of the total effect to dynamics bias and $\\approx 64\\%$ to actor exploitation, which confirms that both stages are necessary for CIVO to manifest.\n\nThis mechanism is analogous to delusional bias \\citep{lu2018nondelusional}, but differs in origin: delusional bias arises from policy-class constraints, while CIVO is model-induced.  The consequence (policy exploitation of overestimated regions) is similar, but the causal pathway is distinct.\n\n\\paragraph{Signed reward error analysis.}\nTo test whether CIVO arises from one-step reward overprediction, we compute signed error (predicted $-$ actual) on posterior-conditioned RSSM predictions (Table~\\ref{tab:signed_error}). The trained-embedding model (008d) shows \\emph{negative} bias at $\\dt{=}2$ (mean signed error $-0.599$, only 8\\% of samples overpredicted), ruling out observation-level reward overprediction as the mechanism. The baseline is well-calibrated (mean SE $\\approx 0$), confirming methodological soundness. Value overestimation therefore occurs during \\emph{imagination-level} prior drift: the RSSM prior (unconditioned on observations) generates reward-favorable trajectories at $\\dt > 1$ (Stage~1 above, $1.68\\times$ ratio under random policy), and the critic accumulates these into overestimated returns. The one-step reward prediction is negatively biased when conditioned on real observations, but this posterior correction is unavailable during imagination. This also distinguishes CIVO from generic compounding error, which would produce \\emph{positive} signed error accumulating with horizon; the negative observation-level bias confirms that CIVO is a prior-drift phenomenon, not a reward-prediction artifact.\n\n\\begin{table}[h]\n\\centering\n\\caption{Signed reward error (predicted $-$ actual) on posterior-conditioned RSSM predictions. Negative values indicate underprediction. The trained-embedding model underpredicts at $\\dt{=}2$, ruling out observation-level reward overprediction as the CIVO mechanism.}\n\\label{tab:signed_error}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Config} & $\\dt$ & \\textbf{Mean SE} & \\textbf{Std} & \\textbf{\\%Over} & \\textbf{Actual} & \\textbf{Pred} \\\\\n\\midrule\nBaseline & 1 & $+0.001$ & 0.023 & 39.6\\% & 1.893 & 1.894 \\\\\n\\midrule\n008d (trained) & 1 & $+0.018$ & 0.072 & 61.8\\% & 0.361 & 0.379 \\\\\n008d (trained) & 2 & $\\mathbf{-0.599}$ & 0.722 & 8.0\\% & 0.721 & 0.121 \\\\\n\\midrule\n008f (no emb) & 1 & $-0.710$ & 0.704 & 14.0\\% & 0.921 & 0.211 \\\\\n008f (no emb) & 2 & $-1.645$ & 1.485 & 5.0\\% & 1.840 & 0.195 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Embedding geometry (exp\\_065).}\nTo characterize what the trained $\\dt$-embedding learns, we measure pairwise cosine similarity between $e_{\\dt{=}1}$ and $e_{\\dt{=}2}$ across training checkpoints for three trained seeds (two environments) and two frozen controls (Table~\\ref{tab:cosine_sim}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cosine similarity between $e_{\\dt{=}1}$ and $e_{\\dt{=}2}$ vectors. Trained embeddings converge to near-opposite representations; frozen embeddings remain near-orthogonal throughout.}\n\\label{tab:cosine_sim}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llrrr}\n\\toprule\n\\textbf{Config} & \\textbf{Env} & \\textbf{cos@25K} & \\textbf{cos@75K} & \\textbf{Status} \\\\\n\\midrule\n008d s3 (trained) & Walker & $-0.87$ & $-0.70$ & CIVO \\\\\n059 s5 (trained) & Walker & $-0.94$ & $-0.86$ & CIVO \\\\\n010b s0 (trained) & Cheetah & $-0.90$ & $-0.84$ & CIVO \\\\\n\\midrule\n057 s2 (frozen) & Walker & $-0.15$ & $-0.15$ & Healthy \\\\\n058 s1 (frozen) & Cheetah & $+0.07$ & $+0.07$ & Healthy \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll trained seeds map $\\dt{=}1$ and $\\dt{=}2$ to nearly opposite directions (cosine similarity $-0.70$ to $-0.94$), consistent across both Walker and Cheetah environments. Frozen controls remain near-orthogonal (cosine $\\approx 0$) and constant across all checkpoints. The full pairwise cosine similarity matrix (Figure~\\ref{fig:pairwise_heatmap}) reveals that the near-antipodal relationship between $e_{\\dt{=}1}$ and $e_{\\dt{=}2}$ is the dominant structure: most other $\\dt$-pairs remain near-orthogonal ($|\\text{cos}| < 0.2$), indicating that the RSSM selectively maximizes separation along the $\\dt{=}1$ vs.\\ $\\dt{=}2$ axis rather than learning a globally structured embedding space.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.55\\columnwidth]{figures/paper/pairwise_heatmap.png}\n\\caption{Pairwise cosine similarity between all $\\dt$-embedding vectors (exp\\_008d, seed 3, step 75K). The $e_{\\dt{=}0}$--$e_{\\dt{=}1}$ pair exhibits strong anti-correlation ($-0.70$); remaining pairs are near-orthogonal, confirming that the learned geometry is dominated by a single antipodal axis.}\n\\label{fig:pairwise_heatmap}\n\\end{figure}\n\nThe magnitude of the learned separation---near-antipodal rather than merely distinct---provides converging evidence that the RSSM develops maximally differentiated internal representations for the two temporal scales, which in turn may contribute to the asymmetric reward fidelity gap reported in Table~\\ref{tab:rssm_fidelity} and replicated below.\n\n\\paragraph{Extended RSSM fidelity replication (exp\\_063).}\nTo validate the fidelity gap on independently trained checkpoints, we repeat the posterior-conditioned analysis with 15 episodes $\\times$ 40 test points $\\times$ 4 $\\dt$ levels (600 samples per model) on final checkpoints from three conditions (Table~\\ref{tab:rssm_fidelity_ext}).\n\n\\begin{table}[h]\n\\centering\n\\caption{RSSM fidelity analysis (training-time posterior-conditioned). Reward prediction gap remains the critical differentiator; observation reconstruction is paradoxically \\emph{better} with trained embedding. Independent final-checkpoint replication (exp\\_063, 008d seed~4) yields a reward gap of $2.7\\times$, confirming the qualitative pattern at lower magnitude.}\n\\label{tab:rssm_fidelity_ext}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{obs\\_MSE}} & \\multicolumn{3}{c}{\\textbf{reward\\_MAE}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Config} & $\\dt{=}1$ & $\\dt{=}2$ & Gap & $\\dt{=}1$ & $\\dt{=}2$ & Gap \\\\\n\\midrule\nBaseline (009d) & 16.08 & 23.49 & 1.46$\\times$ & 0.045 & 0.059 & 1.30$\\times$ \\\\\nCollapsed (008d) & 9.96 & 13.21 & 1.33$\\times$ & 0.057 & 0.178 & 3.11$\\times$ \\\\\nFrozen (057) & 11.14 & 14.95 & 1.34$\\times$ & 0.068 & 0.133 & 1.96$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe replication confirms the original fidelity gap pattern with two additional observations. First, the collapsed model achieves the \\emph{lowest} absolute obs\\_MSE at $\\dt{=}1$ (9.96 vs.\\ baseline 16.08), indicating that the trained $\\dt$-embedding improves world model quality overall---the pathology is selective degradation of reward predictions at longer horizons, not general model failure. Second, freezing the $\\dt$-embedding reduces the reward gap from $3.11\\times$ (training-time; $2.7\\times$ in independent replication) to $1.96\\times$, providing converging evidence for its role in preventing the co-adaptation loop while leaving residual multi-step reward prediction difficulty.\n\n\\paragraph{Value prediction analysis (exp\\_064).}\nTo examine the relationship between RSSM reward fidelity and critic value estimates, we compare critic predictions $V(s)$ against actual evaluation returns across three conditions (Table~\\ref{tab:value_pred}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Critic value predictions vs.\\ actual evaluation returns. The CIVO model's critic is well-calibrated to its $\\lambda$-return targets ($V(s) \\approx$ target) but both $V$ and targets are disconnected from reality (VE${=}3.03\\times$).}\n\\label{tab:value_pred}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Config} & $V(s)$ & \\textbf{Eval} & \\textbf{VE ratio} & $V{-}\\text{target}$ \\\\\n\\midrule\nBaseline (001) & 665.9 & 938.9 & 0.71$\\times$ & $+0.001$ \\\\\nCIVO (008d) & 192.7 & 63.6 & \\textbf{3.03}$\\times$ & $+0.586$ \\\\\nNo emb (008f) & 116.5 & 306.5 & 0.38$\\times$ & $+0.316$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe paradox---$V(s)$ tracks its $\\lambda$-return targets faithfully yet overestimates actual performance by $3\\times$---provides converging evidence for the hypothesized mechanism in which CIVO operates upstream of the critic: the world model generates inflated imagination trajectories that the critic learns faithfully, producing targets disconnected from reality. In the baseline, VE${<}1.0$ throughout training because $V(s)$ reflects discounted imagined returns over $H{=}15$ steps, naturally lower than undiscounted episodic evaluation. The CIVO model crosses VE${=}1.0$ at step 55K and reaches $3.03\\times$ by 105K, with the gap widening as the actor exploits the overoptimistic critic.\n\n\\paragraph{Actor entropy dynamics under CIVO.}\nExtended training of collapsed configurations reveals a distinctive temporal sequence: evaluation return collapses first, followed by actor entropy explosion ${\\sim}35$K steps later. In the most severe case (EG~v4), entropy rises from $-5.21$ to $+3.22$ nats at a rate of $+2.11$ nats/10K steps, with returns declining from 583 to 93 between steps 60K--120K. A second collapsed run (EG~v5) shows $+0.61$ nats/10K with comparable return degradation (583$\\to$102). By contrast, healthy baselines exhibit gradual entropy drift at $+0.07$ to $+0.22$ nats/10K---15--30$\\times$ slower---with returns stable above 900. The return-before-entropy temporal ordering is consistent with the causal chain: delusional critic $\\to$ bad actor gradients $\\to$ policy destabilization. The entropy explosion is a lagging indicator; the NVE diagnostic detects CIVO onset ${\\sim}35$K steps before entropy rises, consistent with its use as an early-warning signal (\\S\\ref{sec:appendix_sensitivity}).\n\n\\subsection{Selective Gradient Stopping and Gradient Decomposition}\n\\label{sec:sgs_gradient_analysis}\n\n\\subsubsection{Gradient Decomposition Results}\n\\label{sec:gradient_decomposition}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig3_gradient_decomposition.pdf}\n\\caption{Gradient contribution to $e_{\\Delta t}$ by loss component at two training checkpoints. The reward head contributes the largest share (38--49\\%) yet reward-only SGS (exp\\_016e) fails; the observation decoder channel (16--22\\%) carries the critical $\\dt$-specific spatial information that drives the RSSM fidelity gap.}\n\\label{fig:gradient_decomp}\n\\end{figure}\n\nExp\\_016e collapses in the same qualitative pattern as the unmodified control: peak evaluation 326.7 at 75K steps followed by catastrophic decline to 31.7 at 95K, with NVE reaching $10.42\\times$. The SGS intervention neither prevented nor attenuated CIVO.\n\nTo explain this null result, we performed a gradient decomposition analysis using \\texttt{torch.autograd.grad} to measure each loss component's contribution to $\\nabla_\\theta e_{\\Delta t}$, where $\\theta$ denotes the temporal embedding parameters. Table~\\ref{tab:gradient_decomposition} reports the results.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Gradient contributions to the temporal embedding $e_{\\Delta t}$ by loss component, measured via \\texttt{torch.autograd.grad} with training configuration \\texttt{gate\\_fixed\\_dt=2}. Gradient norms are $\\ell_2$ norms of $\\nabla_\\theta \\mathcal{L}_i$ for each loss $\\mathcal{L}_i$.}\n\\label{tab:gradient_decomposition}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{@55K}} & \\multicolumn{2}{c}{\\textbf{@112K}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nLoss component & Share & (\\%) & Share & (\\%) \\\\\n\\midrule\nReward head & --- & 49.0 & --- & 38.1 \\\\\nKL dynamics & --- & 34.7 & --- & 40.4 \\\\\nObservation decoders & --- & 16.3 & --- & 21.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient decomposition reveals a counterintuitive structure: the reward head provides the largest gradient contribution (49.0\\% at 55K, 38.1\\% at 112K), yet reward-only SGS (exp\\_016e) fails catastrophically (NVE $10.42\\times$). The observation decoder channel contributes the smallest share (16.3\\% at 55K, 21.5\\% at 112K) yet carries the critical $\\dt$-specific spatial information.  This dissociation between gradient magnitude and causal importance explains why exp\\_016e, which targets the largest pathway, is functionally insufficient for CIVO prevention.\n\nThe gradient structure is relatively stable across training (reward shifts from 49\\% to 38\\%, obs from 16\\% to 22\\%, KL from 35\\% to 40\\%), unlike what a magnitude-based account would predict. The reward head's large gradient contribution reflects the scalar reward prediction task's sensitivity to temporal embedding parameters, but this gradient does not encode $\\Delta t$-specific structural information about spatial dynamics. The observation decoder channel, despite its smaller magnitude, is the only pathway that encodes how the RSSM should differentially predict multi-dimensional proprioceptive states across temporal scales.\n\n\\paragraph{Why the smallest channel is causally critical.} The observation decoder is the only loss component whose gradients encode how the RSSM should differentially predict multi-dimensional proprioceptive states ($14$ orientations, $9$ velocities, $1$ height) across temporal scales.  This $\\dt$-specific spatial information shapes the latent state representation in ways that propagate to reward prediction: the RSSM fidelity gap ($2.78\\times$ reward MAE ratio, Table~\\ref{tab:rssm_fidelity}) arises because the temporal embedding learns to produce latent states that are spatially biased at $\\dt{>}1$, not because the reward head directly learns scale-dependent biases.  Full-SGS targets this causal chain by preventing observation-decoder gradients from updating $e_{\\Delta t}$, though its 0/2 CIVO elimination rate on Walker (seed~1: NVE reduced from $4.12\\times$ to $1.66\\times$ but remains CIVO-positive; seed~2: collapsed) indicates that breaking the gradient pathway alone does not fully eliminate the vulnerability.\n\n\\subsubsection{Implications for the CIVO Mechanism}\n\\label{sec:sgs_implications}\n\nThe gradient decomposition reveals that gradient magnitude and causal importance are decoupled in CIVO.\n\n\\paragraph{Gradient importance $\\neq$ gradient magnitude.} The reward head contributes the largest gradient share (38--49\\%) to $e_{\\Delta t}$, yet reward-only SGS fails.  The observation decoder contributes the smallest share (16--22\\%), yet its removal (via Full-SGS) is necessary for CIVO mitigation.  This dissociation arises because the reward head's gradient, while large, does not encode $\\dt$-specific structural information: it adjusts $e_{\\Delta t}$ to minimize a scalar prediction error that is largely $\\dt$-invariant.  The observation decoder's gradient, though smaller, encodes how the RSSM should differentially reconstruct 24-dimensional proprioceptive states across temporal scales. This is the channel through which $e_{\\Delta t}$ learns scale-dependent latent biases.\n\n\\paragraph{Reframing the intervention target.} Any gradient-level strategy that targets the reward head alone (reward prediction regularization, reward-conditioned value clipping, or reward-only SGS) targets the largest pathway but not the informationally critical one.  The failure of exp\\_016e (NVE $10.42\\times$) despite detaching the dominant gradient source confirms this.  Full-pathway SGS (exp\\_018) detaches $e_{\\Delta t}$ from all non-KL gradients, retaining only the KL dynamics contribution (34--40\\%).  However, this intervention eliminates CIVO in neither seed: seed~1 shows partial mitigation (eval 448.3, peak NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses (eval 40.8). Removing the observation decoder gradient channel is thus contributory but not sufficient. Figure~\\ref{fig:civo_decomposition} decomposes evaluation returns across conditions.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig2_civo_decomposition.pdf}\n\\caption{CIVO decomposition: peak and final (105K step) evaluation returns on Walker Walk across four conditions. \\textbf{Baseline} (001): vanilla DreamerV3. \\textbf{Trained dt-emb} (008d)\\protect\\footnotemark: learned $d{=}32$ temporal embedding with multi-rate data. \\textbf{Full-SGS} (s1, s2): trained embedding with all non-KL gradients detached from $e_{\\dt}$. Trained $\\dt$-embedding degrades peak eval by $73\\%$ and final eval by $86\\%$. Full-SGS seed~1 shows partial mitigation ($-51\\%$ final, NVE $1.66\\times$, still CIVO-positive) while seed~2 collapses ($-96\\%$ final). CIVO elimination rate $= 0/2$.}\n\\label{fig:civo_decomposition}\n\\end{figure}\n\\footnotetext{Experiment 008d terminated at 55K steps; the 105K data point uses continuation run 009e under identical configuration.}\n\nCross-environment validation on Cheetah Run (exp\\_021) further clarifies the role of Full-SGS.  The intervention did not prevent the initial CIVO onset: NVE peaked at $9.94\\times$ at 45K (comparable to the unmitigated exp\\_010b's $8.27\\times$).  However, unlike exp\\_010b, which collapsed permanently to eval 51.7, exp\\_021 self-corrected within ${\\sim}$10K steps, with sustained NVE dropping to $0.34\\times$ (55K--105K) and final evaluation recovering to 221.5.  This transient self-correcting trajectory is not attributable to the SGS intervention: the initial CIVO onset and peak severity are comparable to the unmitigated case, and the self-correction may reflect Cheetah Run's simpler dynamics rather than SGS efficacy.  Performance remains at 38.7\\% of baseline (572.5), likely because Full-SGS over-aggressively blocks actor gradients (actor gradient norms near zero throughout training).  Combined with exp\\_018's Walker results (0/2 CIVO elimination), these findings yield a 0/3 elimination rate across environments, indicating that gradient-level interventions alone do not eliminate the CIVO vulnerability. Additional mechanisms (e.g., forward-pass conditioning effects, residual capacity-dependent instabilities) operate beyond the gradient pathway.\n\n\\paragraph{Connection to RSSM fidelity analysis.} The trained-embedding condition (exp\\_008d) shows a $2.78\\times$ reward gap between $\\Delta t{=}1$ and $\\Delta t{=}2$ transitions (Table~\\ref{tab:rssm_fidelity}).  This gap arises because the observation decoder gradients shape $e_{\\Delta t}$ to produce latent states that are spatially biased at $\\dt{>}1$, and the reward head inherits these biases \\textit{through the latent state} rather than learning them directly.  The reward head's large gradient contribution reflects sensitivity to $e_{\\Delta t}$'s parameters but not causal responsibility for the fidelity gap.\n\n\\subsubsection{Entropy Dynamics Across Configurations}\n\\label{sec:entropy_dynamics}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig4_entropy_dynamics.pdf}\n\\caption{Actor entropy trajectories for three configurations. All start at ${\\sim}8$ nats and converge to similar values (${\\sim}{-}4.5$ to ${-}5$). The CIVO-triggering configuration (008d, red) follows a normal entropy reduction trajectory; the divergence from the control (008f) is subtle in entropy space, consistent with CIVO operating through the value channel rather than the entropy channel. 018v2 (Full-SGS, seed~1) shows slightly lower terminal entropy.}\n\\label{fig:entropy_dynamics}\n\\end{figure}\n\n\\subsubsection{Exp\\_016e Reinterpreted as Stochastic Variation}\n\\label{sec:016e_reinterp}\n\nThe gradient decomposition establishes that exp\\_016e targets the largest gradient pathway (reward: 38--49\\%) but not the informationally critical one (observation decoders: 16--22\\%).  The apparent timing differences between exp\\_016e and exp\\_008d (later collapse onset, 75K vs.\\ 25K, and higher peak evaluation, 326.7 vs.\\ 167.2) must be attributed to stochastic variation rather than SGS effects, since the critical observation decoder channel remains intact.  All three trajectories (exp\\_008d, exp\\_009b, exp\\_016e) share the invariant identified by the NVE diagnostic: each crosses the $1.5\\times$ pathological threshold at some point during training.\n\n\\subsection{Post-CIVO Outcomes: Why Seeds Diverge}\n\\label{sec:seed_divergence}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Post-CIVO outcomes for all seven CIVO-positive seeds across two environments. Peak/Final NVE measured in the 35K+ window.}\n\\label{tab:post_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Env} & \\textbf{Seed} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\nWalker & s1 (008d) & 4.12$\\times$ & 4.12$\\times$ & 82.8 & Full collapse \\\\\nWalker & s2 (009b) & 1.62$\\times$ & 0.38$\\times$ & 267.9 & Transient CIVO \\\\\nWalker & s3 (008d\\_s3) & 1.53$\\times$ & 1.53$\\times$ & 268$^\\diamond$ & Late-onset collapse \\\\\nWalker & s4 (008d\\_s4) & 4.62$\\times$ & 4.62$\\times$ & 63.6 & Full collapse \\\\\nWalker & s5 (059) & 4.72$\\times$ & 1.22$\\times$ & 95.8 & Collapse$^\\dagger$ \\\\\n\\midrule\nCheetah & s1 (010b) & 8.27$\\times$ & 8.27$\\times$ & 51.7 & Full collapse \\\\\nCheetah & s0 (010b\\_s0) & 108.52$\\times$ & 108.52$\\times$ & 0.83 & Full collapse \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^\\diamond$ Transitional; train returns still declining at 105K. $^\\dagger$~NVE self-corrected ($4.72\\times$ $\\to$ $1.22\\times$) but policy did not recover (eval 10.5\\% of baseline).\\par}\n\\end{table}\n\nAll seven CIVO-positive seeds cross the $\\nve > 1.5\\times$ threshold (Table~\\ref{tab:post_civo}), yet the downstream damage is stochastic.\\footnote{Exp\\_009e was excluded from multi-seed analyses due to a seed configuration error (default seed=0, identical to exp\\_008d).}  Full collapse is the majority outcome (6/7 seeds), with one self-correction case (Walker seed 2); seed 5 exemplifies a dissociation where NVE self-corrects ($4.72\\times \\to 1.22\\times$) while the policy remains collapsed (eval 10.5\\% of baseline). Cheetah seeds exhibit more extreme overestimation (peak NVE $8.27$--$108.52\\times$ vs.\\ Walker's $1.53$--$4.62\\times$), consistent with the Cheetah reward scale amplifying the fidelity gap.  We hypothesize that the divergence relates to the critic's representational capacity at the time of CIVO onset.  \\citet{lyle2022capacity} demonstrate that deep RL networks suffer progressive capacity loss, in which early-learned features become increasingly difficult to overwrite.  If the critic's capacity is already partially consumed when CIVO injects overestimation, the network cannot recalibrate (seed~0); if sufficient capacity remains, the critic can absorb transient overestimation and recover (seed~2).\n\n\\paragraph{A fourth trajectory: CIVO-induced persistent value collapse.}\nObs-decoder SGS seed~3 (exp\\_025) exhibits a trajectory not observed in the untreated seeds: healthy through 105K ($\\nve < 1.0\\times$, eval 818.6), CIVO onset at 135K ($\\nve = 5.47\\times$, eval 67.0), followed by evaluation recovery (590.2 at 215K, 64\\% of baseline) but persistent value collapse ($\\nve = 0.14\\times$, value mean 80.6). The critic undershoots after the CIVO episode, suggesting that CIVO-induced representational damage persists even when the policy partially recovers. This contrasts with transient CIVO (seed~2, 009b), where both value and evaluation recover jointly, and with full collapse (seed~1, 008d), where neither recovers. Seed~4 exhibits the same terminal value collapse ($\\nve = 0.14\\times$ at 215K, eval 242), suggesting this overcorrection is systematic rather than seed-specific. The pattern adds a fourth post-CIVO outcome---policy recovery with critic damage---to the three documented in Table~\\ref{tab:post_civo}.\n\n\\subsubsection{Failure and Degradation Mode Taxonomy}\n\nTable~\\ref{tab:failure_modes} classifies the seven distinct failure and degradation modes observed across all experimental configurations. The taxonomy reveals that CIVO is not a single failure mode but a family of related pathologies, with the trained $\\dt$-embedding creating vulnerability through at least three independent mechanisms: value-driven collapse (monotonic, late-onset, and SGS-resistant CIVO), entropy-driven instability (IRD collapse), and gradient-mediated effects (gradient starvation, SGS-paradoxical worsening).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Failure and degradation mode taxonomy. Each mode is characterized by its NVE trajectory, entropy behavior, and primary mechanism.}\n\\label{tab:failure_modes}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccl@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Representative} & \\textbf{NVE} & \\textbf{Entropy} & \\textbf{Mechanism} \\\\\n\\midrule\nMonotonic CIVO & 008d, 008d\\_s4, 010b\\_s0 & $\\uparrow$ sustained & $\\downarrow$ & Reward bias $\\to$ critic $\\to$ actor \\\\\nLate-onset CIVO & 008d\\_s3 & $\\uparrow$ delayed & $\\downarrow$ & Same, delayed onset \\\\\nTransient CIVO & 009b & Peak $\\to$ $\\downarrow$ & Stable & Self-correction via capacity \\\\\nIRD collapse & 008e\\_v3\\_s2 & $\\uparrow$ late & $\\uparrow$ & Entropy-driven, values stable \\\\\nGrad.\\ starvation & 015b & Oscillates, decays & Stable & Frozen emb $\\to$ zero actor grad \\\\\nSGS-resistant & 018\\_s2 & $\\uparrow$ & $\\downarrow$ & Forward-pass conditioning \\\\\nSGS-paradoxical & 016e & $\\uparrow$ sustained & $\\downarrow$ & Reward SGS $\\to$ obs-dec reliance \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Training Dynamics}\\label{sec:extended_training}\n\nOne Walker seed (s3, exp\\_045) was extended from 112K to approximately 302K steps to investigate long-horizon CIVO dynamics. After onset (NVE peak $4.91\\times$ at 132K steps), the system exhibited complete self-recovery: NVE declined to $0.05\\times$ and evaluation performance recovered to 867.6 (94.7\\% of baseline). This recovery required approximately 170K additional training steps beyond onset. The trajectory shows a single onset--recovery cycle with no recurrence, suggesting that the CIVO feedback loop can break spontaneously given sufficient training---though at substantial computational cost that the frozen $\\dt$-embedding diagnostic eliminates entirely.\n\n\\subsection{Why MPC Is Immune}\n\\label{sec:mpc_immune}\n\n\\citet{nhu2025tawm} show that $\\dt$-conditioning benefits TD-MPC2, raising the question of why it fails in DreamerV3.  The critical difference is that MPC re-plans from real states at every step, so imagination errors do not accumulate into the training signal because there is no critic bootstrapping from imagined trajectories.  In DreamerV3, the actor-critic trains entirely within imagination, and any systematic reward-prediction bias at $\\dt > 1$ is amplified through the closed actor-critic loop.\n\n\\subsection{The \\texorpdfstring{$\\dt$}{dt}-Embedding Dilemma}\n\\label{sec:embedding_dilemma}\n\nThe factorial results reveal a fundamental tension: removing the $\\dt$-embedding (008f) eliminates CIVO but at a $13\\times$ cost to reward prediction quality ($0.7469$ vs.\\ $0.0568$ MAE), as the world model cannot distinguish temporal scales.  Restricting imagination to $\\dt{=}1$ while retaining the trained embedding (008e\\_v3) avoids collapse in 2 of 4 seeds (50\\%), while the remaining two collapse via distinct mechanisms: Pathway~A (CIVO-driven, entropy decrease; s3, NVE $4.02\\times$) and Pathway~B (entropy-driven, entropy increase; s2, NVE $3.78\\times$; \\S\\ref{sec:f6}).  Neither approach alone provides a complete solution.\n\n\\subsection{Temporal Embedding Representation Analysis}\n\\label{sec:cosine_evolution}\n\nTo understand how the trained $\\dt$-embedding creates vulnerability, we analyze the cosine similarity between $e(\\dt{=}1)$ and $e(\\dt{=}2)$ across training (exp\\_065). Trained embeddings learn \\emph{near-opposite} representations: $\\cos(e_1, e_2) = {-}0.87$ to ${-}0.94$ at 25K steps across three configurations (Walker 008d\\_s3, Cheetah 010b\\_s0, Walker 059\\_s5), persisting at ${-}0.70$ to ${-}0.86$ at 75K steps. In contrast, frozen embeddings maintain near-zero similarity ($-0.15$ to $+0.07$, constant throughout training). The near-antipodal learned representations explain the large reward prediction gap (\\S\\ref{sec:f2}): $\\dt{=}2$ conditioning pushes the RSSM into a qualitatively different region of latent space, producing systematically biased predictions rather than minor perturbations.\n\n\\subsection{\\texorpdfstring{$\\dt$}{dt}-Embedding Differentiation Precedes Value Divergence}\n\\label{sec:cosine_temporal}\n\nThe preceding analysis established that trained $\\dt$-embeddings learn near-antipodal representations. Here we resolve the \\emph{temporal dynamics} of this differentiation across 11 experiments (${\\sim}$47 checkpoints), testing whether embedding differentiation is a consequence or precursor of CIVO.\n\n\\paragraph{Trained embeddings: monotonic relaxation.}\nAcross all trained configurations, $\\cos(e_1, e_2)$ starts near $-0.95$ within 10K steps and relaxes monotonically toward ${\\sim}{-}0.65$ (Table~\\ref{tab:cosine_evolution_ext}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cosine similarity evolution between $e(\\dt{=}1)$ and $e(\\dt{=}2)$ for trained $\\dt$-embeddings. Relaxation is monotonic but never reaches zero; frozen embeddings remain constant near zero throughout training.}\n\\label{tab:cosine_evolution_ext}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Env} & \\textbf{Experiment} & \\textbf{10K} & \\textbf{25K} & \\textbf{65K} & \\textbf{75K} & \\textbf{302K} \\\\\n\\midrule\n\\multirow{2}{*}{Walker} & exp\\_066b (trained) & $-0.947$ & $-0.928$ & $-0.847$ & --- & --- \\\\\n & exp\\_045 (extension) & --- & --- & --- & --- & $-0.668$ \\\\\n\\midrule\nCheetah & exp\\_010b$\\to$048 & --- & $-0.904$ & --- & $-0.841$ & $-0.639$ \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Frozen controls:}} \\\\\nWalker & exp\\_057 (frozen) & \\multicolumn{5}{c}{$-0.150$ (constant, 25K--225K)} \\\\\nCheetah & exp\\_058 (frozen) & \\multicolumn{5}{c}{$+0.069$ (constant, 25K--225K)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-seed consistency at 25K steps is high: mean $\\cos = -0.910 \\pm 0.028$ ($n{=}5$ Walker seeds), confirming the relaxation pattern is robust across random seeds. Variance increases with training ($-0.789 \\pm 0.076$ at 75K), reflecting seed-dependent relaxation rates.\n\n\\paragraph{Temporal precedence over CIVO.}\nExp\\_066b provides simultaneous cosine similarity and CIVO diagnostic data at 5K resolution (Table~\\ref{tab:cosine_vs_civo}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cosine similarity relaxation and CIVO diagnostic for exp\\_066b. Embedding relaxation onset (${\\sim}$20K) precedes CIVO alert (55K, VE ratio $> 0.7$) by ${\\sim}$30--35K steps.}\n\\label{tab:cosine_vs_civo}\n\\footnotesize\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{rccc}\n\\toprule\n\\textbf{Step} & $\\cos(e_1, e_2)$ & \\textbf{VE ratio} & \\textbf{CIVO alert} \\\\\n\\midrule\n10K & $-0.947$ & 0.012 & --- \\\\\n15K & $-0.948$ & 0.033 & --- \\\\\n25K & $-0.928$ & 0.193 & --- \\\\\n35K & $-0.904$ & 0.269 & --- \\\\\n45K & $-0.880$ & 0.358 & --- \\\\\n55K & $-0.861$ & 0.710 & \\textbf{Alert} \\\\\n65K & $-0.847$ & 0.724 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCosine relaxation begins at ${\\sim}$20K (cos transitions from $-0.948$ at 15K to $-0.928$ at 25K), while the VE ratio first exceeds 0.7 at 55K. The ${\\sim}$30--35K temporal lead establishes that embedding differentiation is an early training dynamic, not a consequence of CIVO-triggered feedback. The relaxation rate peaks at 25K--45K ($+0.024$/10K steps) before decelerating, consistent with the geometric intuition that large-angle adjustments in embedding space are cheaper early in training.\n\n\\paragraph{Embedding norms.}\nWalker and Cheetah exhibit qualitatively different norm dynamics. Walker $e(\\dt{=}1)$ norms grow from 0.23 to 0.50 ($2.2\\times$) while $e(\\dt{=}2)$ grows from 0.45 to 0.63 ($1.4\\times$)---both $\\dt$ values become more expressive over training. Cheetah norms remain nearly constant ($\\leq 1.04\\times$) despite continued cosine relaxation, indicating direction changes without magnitude change. Frozen embedding norms are an order of magnitude smaller (${\\sim}0.06$, constant).\n\n\\paragraph{Mechanistic interpretation.}\nThe temporal ordering---embedding differentiation (${\\sim}$20K) $\\to$ reward fidelity gap (${\\sim}$20K, \\S\\ref{sec:timeseries_fidelity}) $\\to$ value overestimation (${\\sim}$30K)---suggests a three-layer causal chain: the embedding first learns maximally differentiated representations that push $\\dt{=}1$ and $\\dt{=}2$ into opposite latent regions, the reward head then develops scale-dependent biases from these differentiated inputs, and the critic amplifies these biases through imagined rollout bootstrapping. The frozen embedding's constant near-zero cosine ($|\\cos| < 0.2$) prevents the first link in this chain, explaining why freezing eliminates CIVO despite maintaining identical forward-pass architecture (\\S\\ref{sec:f3}).\n\n\\subsection{Time-Series Fidelity--Value Analysis}\n\\label{sec:timeseries_fidelity}\n\nTo test the causal direction between reward fidelity degradation and value overestimation, we analyze exp\\_066 and exp\\_066b: two Walker Walk seeds (trained $\\dt$-embedding, fixed $\\dt{=}2$) evaluated at 12 dense checkpoints from 10K to 65K steps (Table~\\ref{tab:timeseries_fidelity}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Time-series fidelity and value metrics (exp\\_066, seed~0). SS = single-step MAE ratio ($\\dt{=}2$/$\\dt{=}1$); VE = value-to-eval ratio. Fidelity degradation (SS $>1.1\\times$ at 20K) precedes value overestimation onset (VE begins rising at ${\\sim}$30K) by ${\\sim}$10K steps. Seed~1 (exp\\_066b) confirms the pattern: fidelity gap onset ${\\sim}$15K $\\to$ VE onset ${\\sim}$24K (lead ${\\approx}$9K steps; VE peak ${=}0.72$).}\n\\label{tab:timeseries_fidelity}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{rcccccc}\n\\toprule\n\\textbf{Step} & \\textbf{SS ratio} & \\textbf{OL ratio} & \\textbf{VE ratio} & \\textbf{MAE$_{\\dt{=}1}$} & \\textbf{MAE$_{\\dt{=}2}$} & \\textbf{Return} \\\\\n\\midrule\n10K & 1.05 & 0.94 & 0.01 & 0.090 & 0.094 & 43.0 \\\\\n15K & 1.08 & 1.03 & 0.02 & 0.085 & 0.092 & 187.8 \\\\\n20K & 1.10 & 1.09 & 0.16 & 0.078 & 0.086 & 148.7 \\\\\n25K & 1.04 & 1.22 & 0.16 & 0.073 & 0.076 & 142.1 \\\\\n30K & 1.25 & 1.45 & 0.22 & 0.068 & 0.085 & 148.3 \\\\\n35K & 1.24 & 1.51 & 0.23 & 0.062 & 0.077 & 275.4 \\\\\n40K & 1.35 & 1.38 & \\textbf{1.59} & 0.058 & 0.078 & 202.3 \\\\\n45K & 1.40 & 1.38 & 0.36 & 0.055 & 0.077 & 107.5 \\\\\n50K & 1.47 & 1.56 & 0.62 & 0.052 & 0.076 & 178.4 \\\\\n55K & 1.37 & 1.52 & 0.62 & 0.050 & 0.069 & 60.8 \\\\\n60K & 1.61 & 1.35 & 1.40 & 0.049 & 0.079 & 125.3 \\\\\n65K & 1.68 & 1.38 & 1.40 & 0.047 & 0.079 & 94.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/paper/fig_temporal_ordering.pdf}\n\\caption{Temporal ordering of fidelity degradation and value overestimation (exp\\_066, seed~0). \\textbf{Left axis}: single-step fidelity ratio (SS, blue) grows steadily from $1.05\\times$ to $1.68\\times$. \\textbf{Right axis}: value-to-eval ratio (VE, red) remains near zero until 40K, then spikes. The ${\\sim}$10K onset-to-onset lag supports the causal direction: fidelity gap $\\to$ value overestimation. Seed~1 (exp\\_066b) replicates the pattern with a ${\\sim}$9K temporal lead.}\n\\label{fig:temporal_ordering}\n\\end{figure}\n\nThe $\\dt{=}1$ prediction MAE decreases monotonically ($0.090 \\to 0.047$) as the world model improves, but $\\dt{=}2$ MAE plateaus at ${\\sim}0.08$. The growing fidelity gap is therefore not caused by $\\dt{=}2$ predictions worsening, but by the model selectively improving at $\\dt{=}1$ while failing to transfer that improvement to $\\dt{=}2$---consistent with the trained $\\dt$-embedding learning maximally differentiated representations (\\S\\ref{sec:cosine_evolution}) that prevent cross-scale generalization.\n\n\\textbf{Limitation.} These results are limited to two seeds ($n{=}2$). While both seeds show consistent temporal ordering (leads of ${\\approx}$10K and ${\\approx}$9K steps), additional seeds would strengthen the causal claim.\n\n\\subsection{Actor Entropy Is Not Diagnostic of CIVO}\n\\label{sec:entropy_not_diagnostic}\n\nTo test whether actor entropy can serve as an early collapse indicator, we compare entropy trajectories between collapsed and healthy configurations at matched training steps across five experiments (Table~\\ref{tab:entropy_contrast}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Actor entropy comparison at matched time points. Collapsed and healthy configurations exhibit indistinguishable entropy at 55K steps (difference $= 0.03$ nats), despite collapsed runs showing severe return degradation.}\n\\label{tab:entropy_contrast}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Group} & \\textbf{Experiment} & \\textbf{5K} & \\textbf{25K} & \\textbf{45K} & \\textbf{55K} & \\textbf{Return} \\\\\n\\midrule\n\\multirow{2}{*}{Collapsed}\n & exp\\_008d (trained dt\\_emb) & 8.16 & $-1.86$ & $-4.58$ & $-4.88$ & ${\\sim}165$ \\\\\n & fixed\\_dt2 ($\\dt{=}2$) & 8.16 & $-3.02$ & $-5.06$ & $-5.17$ & ${\\sim}29$ \\\\\n\\midrule\n\\multirow{3}{*}{Healthy}\n & exp\\_008f (no dt\\_emb) & 8.11 & $-1.85$ & $-4.31$ & $-4.77$ & ${\\sim}460$ \\\\\n & exp\\_008a (unexposed) & 8.16 & $-4.88$ & $-5.20$ & $-5.21$ & ${\\sim}300$ \\\\\n & baseline\\_s1 ($\\dt{=}1$) & 8.10 & $-4.74$ & $-5.12$ & $-5.18$ & ${\\sim}950$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the last comparable step (55K): collapsed mean entropy $= -5.02$ (average of $-4.88$, $-5.17$); healthy mean entropy $= -5.05$ (average of $-4.77$, $-5.21$, $-5.18$); difference $= 0.03$ nats---statistically negligible. The hypothesis that collapsed runs exhibit anomalous entropy rise (actor confusion from delusional critic gradients) is not supported during the CIVO onset window.\n\nThe fixed\\_dt2 experiment demonstrates this most clearly: returns peak at ${\\sim}580$ (40K) then crash to 29 (72K), yet entropy remains stable at $-5.1$ throughout. The actor maintains a committed, low-entropy policy during the entire collapse---it does not become confused but rather remains confident while acting on incorrect value estimates. This is consistent with CIVO operating through critic value distortion rather than actor policy degradation. The late-stage entropy explosion documented in \\S\\ref{sec:civo_mechanism} ($+2.1$ nats/10K in EG~v4, onset ${\\sim}$35K steps after return collapse) occurs well beyond this window, confirming entropy rise as a lagging consequence rather than a concurrent or predictive signal.\n\n\\paragraph{Entropy descent speed.}\nEntropy descent rate correlates with temporal configuration complexity, not collapse fate. Simpler configurations (baseline $\\dt{=}1$, unexposed exp\\_008a) reach $-4.7$ by 25K, while configurations exposed to temporal variation (both collapsed and healthy) remain near $-2.0$ at 25K, reflecting the difficulty of policy commitment when training data spans multiple temporal scales.\n\n\\paragraph{Long-horizon entropy recovery.}\nThe baseline ($\\dt{=}1$) run extended to 505K steps shows entropy recovering from $-5.2$ to ${\\sim}{-}1.5$ between 115K and 295K steps, coinciding with continued performance improvement ($700 \\to 950$ return). This adaptive entropy increase rules out entropy rise as an inherently negative signal; the actor maintains ${\\sim}950$ return with entropy 3--4 nats above its minimum, indicating a healthy exploration--exploitation balance during extended training.\n\n\\subsection{Multiple Vulnerability Pathways}\n\\label{sec:pathways}\n\nThe two collapse patterns identified in \\S\\ref{sec:f6}---CIVO (Pathway~A, value-driven, entropy decreasing) and a tentative second mode (Pathway~B, eval-driven, entropy increasing)---have distinct diagnostic signatures. Pathway~B is observed in only two seeds (008e\\_v3\\_s2 and 038\\_s2); we present it as preliminary evidence that the trained $\\dt$-embedding's learned features may affect both reward prediction across temporal scales (Pathway~A) and the representation space in which the actor operates (Pathway~B), though additional data is needed to confirm this as a distinct mechanism.  This explains why $\\nve$ is sensitive but not perfectly specific: Pathway~B's late evaluation decline inflates $\\nve$ through the same arithmetic as CIVO, yielding the sole false positive ($3.78\\times$ for 008e\\_v3 s2).  Distinguishing the two requires examining the temporal profile and entropy direction of collapse (Figure~\\ref{fig:multiple_pathways}).\n\n\n\\subsection{Implications for Temporal Abstraction in World Models}\n\\label{sec:implications}\n\nCIVO identifies a structural incompatibility between flat temporal conditioning and imagination-based actor-critic training.  Hierarchical approaches (THICK \\citep{gumbsch2024thick}, Hieros \\citep{mattes2024hieros}, LS-Imagine \\citep{li2025lsimagine}) may avoid this by maintaining separate dynamics per temporal scale.  Whether CIVO transfers to transformer-based world models (DreamerV4; \\citealt{hafner2025dreamerv4}) depends on whether attention weights co-adapt with temporal embeddings analogously.  The CIVO mechanism requires three structural properties: (1) a temporal embedding that co-adapts with dynamics via gradient flow, (2) multi-step imagined rollouts used for critic training, and (3) a reward head that inherits latent biases from the shared representation.  Transformer-based world models that share these properties may exhibit analogous vulnerability; architectures that decouple temporal conditioning from the reward prediction pathway would not.\n\n\\subsection{Cross-Environment TCN Evaluation}\n\\label{sec:tcn_cross_env}\n\nTable~\\ref{tab:tcn_full} reports the full TCN evaluation across environments and noise magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\caption{TCN results across environments and noise magnitudes. Prevention = peak NVE $< 1.5\\times$ (35K+).}\n\\label{tab:tcn_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Env} & $\\sigma$ & \\textbf{Seed} & \\textbf{NVE$_{\\max}$} & \\textbf{Prevented?} & \\textbf{Eval (\\%)} \\\\\n\\midrule\nWalker & 0.1 & s0 & 1.02 & \\checkmark$^*$ & 55\\% \\\\\nWalker & 0.2 & s0 & 0.91 & \\checkmark & 91\\% \\\\\nWalker & 0.2 & s1 & 0.64 & \\checkmark & 45\\% \\\\\nWalker & 0.2 & s2 & 2.11$^\\dagger$ & $\\times$ & ${\\sim}5\\%$ \\\\\n\\rowcolor{gray!15}\nWalker & 0.2 & s3 & 3.04$^\\P$ & $\\times$ & 11\\% \\\\\nWalker & 0.5 & s0 & 3.97 & $\\times$ & 27\\% \\\\\nWalker & 0.5 & s1 & 1.64 & $\\times$ & 41\\% \\\\\n\\midrule\nCheetah & 0.2 & s0 & 1.90 & $\\times$ & crashed \\\\\nCheetah & 0.5 & s0 & 10.67 & $\\times$ & 26\\% \\\\\nCheetah & 1.0 & s0 & $\\leq$0.30 & \\checkmark$^\\S$ & 15\\% \\\\\n\\midrule\nPickCube & 0.2 & s0 & 3.71 & $\\times$ & failing \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$Borderline: NVE${=}1.02\\times$ at 95K, below $1.5\\times$ threshold but above $1.0\\times$.\\\\\n$^\\dagger$NVE $= 2.11\\times$ at 95K, still rising; eval ${\\sim}5\\%$ of baseline.\\\\\n$^\\P$Late-onset CIVO: NVE declined to $0.67\\times$ at 95K before phase-transition-like spike to $3.04\\times$ at 105K; eval 349.6 at 95K $\\to$ 71.8 at 105K $\\to$ 104.5 at 215K.\\\\\n$^\\S$CIVO prevented (NVE${\\leq}0.30$); peak eval 116\\% baseline at 35K, declining to 15\\% by 215K via progressive policy erosion. See ``impossible dose'' discussion.\\par}\n\\end{table}\n\n\\paragraph{Cheetah Run $\\sigma{=}0.5$: transient spike with permanent eval damage.}\nCheetah $\\sigma{=}0.5$ exhibits a novel failure mode: a transient CIVO spike (NVE $= 10.67\\times$ at 55K) followed by NVE recovery ($< 0.3\\times$ by 95K), but permanent evaluation damage (26\\% of baseline). The value signal self-corrects while the policy does not recover, suggesting that CIVO-induced representational damage during the spike persists within the observation window even when the critic subsequently recalibrates. This trajectory parallels the obs-decoder SGS seed~3 pattern (\\S\\ref{sec:seed_divergence}), where partial policy recovery coexists with persistent critic damage.\n\n\\paragraph{Cheetah Run $\\sigma{=}0.2$: insufficient dose.}\nAt $\\sigma{=}0.2$, Cheetah reaches NVE $= 1.9\\times$ at 55K---exceeding the $1.5\\times$ threshold---consistent with Cheetah's higher baseline CIVO severity ($8$--$108\\times$ vs.\\ Walker's $2$--$6\\times$). The noise magnitude that suffices for Walker is inadequate for Cheetah, but increasing $\\sigma$ to 0.5 trades CIVO prevention for a different failure mode rather than achieving mitigation.\n\n\\paragraph{PickCube-v1 $\\sigma{=}0.2$: manipulation failure.}\nPickCube reaches NVE $= 3.71\\times$ at 52.5K with $\\sigma{=}0.2$, indicating that TCN provides no protection in manipulation tasks. The combination of contact-gated dynamics and temporal conditioning may amplify the fidelity gap beyond what representation-level noise can attenuate.\n\n\\paragraph{Dose-response analysis.}\nWe observe $\\sigma{=}0.2$ as a local optimum on Walker Walk, achieving complete CIVO suppression in 2 of 4 seeds. Seeds~2 and~3 both fail but via distinct CIVO onset dynamics: seed~2 shows gradual escalation (NVE $= 2.11\\times$ at 95K, still rising, eval ${\\sim}5\\%$), while seed~3 exhibits a phase-transition-like onset---NVE declined to $0.67\\times$ at 95K before spiking to $3.04\\times$ at 105K (eval 349.6 $\\to$ 71.8 in 10K steps). When TCN fails to prevent CIVO onset, the resulting trajectory qualitatively resembles untreated CIVO in its terminal outcome---runaway NVE and eval collapse. The two failure modes (gradual escalation vs.\\ sudden onset after apparent suppression) reinforce that TCN operates as a binary gate on CIVO onset rather than providing graded attenuation. Below the optimum, we observe $\\sigma{=}0.1$ as insufficient (NVE $= 1.02\\times$---borderline, eval 55\\%); above it, $\\sigma{=}0.5$ overdoses (oscillatory CIVO, eval $\\leq 41\\%$). Cross-seed variance at $\\sigma{=}0.2$ (eval 5--91\\%) exceeds the cross-dose difference by a wide margin, reinforcing that seed effects dominate dose effects. TCN is the only tested intervention achieving complete CIVO suppression in any configuration, but its high seed sensitivity and failure to transfer across environments position it as a \\emph{diagnostic probe}---identifying the representation level as the relevant intervention target---rather than a deployable mitigation.\n\n\\paragraph{Cheetah Run ``impossible dose'' dilemma.}\nExp\\_030c (224K steps) reveals a qualitatively different dose-response on Cheetah. At $\\sigma{=}1.0$, CIVO is eliminated (NVE${\\leq}0.30$ throughout) and initial learning is \\emph{unimpaired}: peak eval reaches 372 at 35K (116\\% of baseline), demonstrating that $\\sigma{=}1.0$ noise does not prevent policy acquisition. However, cumulative actor gradient interference produces progressive policy erosion---eval declines from 372 to 47 by 215K (15\\% of baseline)---while the critic remains well-calibrated (value\\_mean${=}12.4$, NVE${=}0.26$ at 215K). This establishes that \\emph{policy degradation $\\neq$ value corruption}: accurate value signals are insufficient when the actor cannot optimize effectively in noise-perturbed imagination.\n\nThis ``correct values, failed policy'' pattern provides indirect evidence that CIVO is mechanistically distinct from standard overestimation. Double Q-learning and ensemble methods address critic estimation error, but at $\\sigma{=}1.0$ the critic is accurate and the policy still collapses---a failure mode orthogonal to what these countermeasures target. The impossible dose dilemma scales with environment complexity: Cheetah's baseline CIVO severity ($8$--$108\\times$ NVE) requires $\\sigma \\geq 1.0$ to suppress, but this exceeds the actor's gradient signal-to-noise tolerance. On Walker, a narrow effective window exists around $\\sigma{=}0.2$; on Cheetah, the effective dose ($\\sigma \\geq 1.0$) exceeds the tolerable dose, and environments with higher CIVO severity will systematically lack a viable dose window.\n\n\\section{DreamerV3 Hyperparameters}\n\\label{sec:hyperparameters}\n\nTable~\\ref{tab:hyperparams} lists the DreamerV3 hyperparameters used across all experiments. Unless otherwise noted, we use the default DreamerV3 configuration for continuous-control tasks (\\texttt{dmc\\_proprio}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{DreamerV3 hyperparameters for all experiments. Modifications from defaults are marked with $\\diamond$.}\n\\label{tab:hyperparams}\n\\small\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{World Model}} \\\\\nRSSM discrete states & 32 classes $\\times$ 32 categories \\\\\nRSSM stochastic dim & 32 \\\\\nRSSM deterministic dim & 512 \\\\\nMLP hidden size & 512 \\\\\nMLP layers & 2 \\\\\nActivation & SiLU \\\\\nNormalization & LayerNorm \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Training}} \\\\\nBatch size & 16 sequences $\\times$ 64 steps \\\\\nLearning rate & $3 \\times 10^{-4}$ (Adam, $\\epsilon{=}10^{-8}$) \\\\\nSequence length & 64 \\\\\nTraining ratio & 512 \\\\\nFree nats & 1.0 \\\\\nKL balance ($\\alpha$) & 0.8 \\\\\nDiscount ($\\gamma$) & 0.997 \\\\\n$\\lambda$-return & 0.95 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Policy}} \\\\\nImagination horizon$^\\diamond$ & 8 or 15 (see Table~\\ref{tab:complete_results}) \\\\\nActor entropy scale & $3 \\times 10^{-4}$ \\\\\nActor gradient & Reinforce + dynamics backprop \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Temporal Abstraction}$^\\diamond$} \\\\\nGate enabled & True (all non-baseline) \\\\\nGate fixed $\\dt$ & 1 or 2 (per config) \\\\\nSubsample max $\\dt$ & 1 (OFF) or 2 (ON) \\\\\n$\\dt$-embedding dim & 32 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Environment}} \\\\\nAction repeat & 2 (Walker Walk, Cheetah Run) \\\\\nObservation & Proprioceptive (no pixels) \\\\\nTotal environment steps & 105K \\\\\nEvaluation frequency & Every 10K steps \\\\\nEvaluation episodes & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Online CIVO Detector Details}\n\\label{sec:detector_appendix}\n\nThis appendix provides the full algorithm specification and validation results for the online CIVO detector described in \\S\\ref{sec:detector}.\n\n\\subsection{Algorithm Specification}\n\n\nThe four conditions capture complementary signals: (1)~\\emph{Magnitude} ($r_t \\geq 0.49$) confirms that the value-to-evaluation ratio has reached a level indicative of overestimation; (2)~\\emph{Velocity} ($\\Delta r_t > 0.1$) rules out slow drift or plateau behavior; (3)~\\emph{Acceleration} ($\\Delta r_t > \\Delta r_{t-1}$, both $> 0.1$) filters oscillatory paths; (4)~\\emph{Evaluation decline} ($\\geq 2$ of 3 recent checkpoints decline) confirms that overestimation coincides with actual performance degradation. A full comparison of window sizes appears in \\S\\ref{sec:appendix_sensitivity}.\n\nSensitivity analysis over $\\tau_\\text{mag} \\in [0.30, 0.70]$ confirms that $\\tau_\\text{mag} = 0.49$ maximizes Youden's $J = 0.714$; raising the threshold to $0.50$ loses one true positive (seed~3 triggers at $r_t = 0.497$) with no reduction in false positives. The velocity threshold $\\tau_\\text{vel} = 0.1$ is stable across $[0.05, 0.18]$ (TPR remains $5/5$).\n\n\\subsection{Validation Results}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Retrospective CIVO detector validation ($n{=}14$). Detection type: ``predictive'' = alert precedes 20\\% eval decline; ``reactive'' = alert follows decline onset.}\n\\label{tab:detector-validation}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Verdict} & \\textbf{Trigger} & \\textbf{Type} & \\textbf{Peak Eval} & $r_\\text{ve}$ \\\\\n\\midrule\n008d s0 & trained $\\dt$-emb & TP & 45K & predict. & 167 & 0.69 \\\\\n010b & trained $\\dt$-emb (Cheetah) & TP & 65K & reactive & 322 & 3.18 \\\\\n008d s3 & trained $\\dt$-emb & TP & 45K & predict. & 452 & 0.50 \\\\\n008d s4 & trained $\\dt$-emb & TP & 105K & reactive & 383 & 3.03 \\\\\n010b s0 & trained $\\dt$-emb (Cheetah) & TP & 95K & reactive & 248 & 6.34 \\\\\n\\midrule\n008f s3 & no $\\dt$-emb & TN & -- & -- & 594 & -- \\\\\n009b s2 & trained $\\dt$-emb (self-corr.) & TN & -- & -- & 279 & -- \\\\\nbaseline s1 & vanilla & TN & -- & -- & 970 & -- \\\\\n009d s0 & vanilla & TN & -- & -- & 951 & -- \\\\\n009d s1 & vanilla & TN & -- & -- & 920 & -- \\\\\n019b & trained $\\dt$-emb (PickCube) & TN & -- & -- & 26.6 & -- \\\\\n\\midrule\n009c s2 & no $\\dt$-emb & FP & 105K & reactive & 359 & 0.75 \\\\\n009a s2 & vanilla & FP & 85K & predict. & 967 & 0.73 \\\\\n\\midrule\n009c s3 & no $\\dt$-emb & TN & -- & -- & 457 & -- \\\\\n\\midrule\n\\multicolumn{7}{l}{TPR = 5/5 (1.00), \\quad FPR = 2/9 (0.22)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe detector identifies all five CIVO-positive runs (TPR = 5/5). Two are detected predictively (008d seeds~0 and~3, both at 45K). Two false positives occur among nine negative cases (FPR = 2/9, precision 71\\%, F$_1$ = 0.83). Run 009c develops genuine late-stage value overestimation unrelated to CIVO; run 009a triggers during a transient eval dip at 85K before recovery to 966. Early alerts (before 70K) carry higher diagnostic confidence.\n\n\\subsection{Cross-Simulator Specificity (PickCube)}\n\nExp\\_019b applies the CIVO-trigger configuration to PickCube-v1 in ManiSkill3, a dense-reward manipulation task. The V/E ratio exhibits an oscillatory pattern rather than monotonic divergence: it spikes to $r_t = 5.66$ at 52.5K, then deflates to 1.38 by 72.5K. This trajectory prevents the acceleration condition from co-occurring with evaluation decline at any single checkpoint. Across all 14 checkpoints through 132.5K, the detector correctly remains silent (TN), confirming that the acceleration filter distinguishes transient spikes from CIVO's sustained monotonic divergence. A frozen-embedding control (exp\\_054) confirms this classification: frozen PickCube-v1 exhibits a comparable burst (peak $8.81\\times$ at 62.5K) that resolves within a single evaluation cycle ($0.55\\times$ at 72.5K), establishing environment-specific origin independent of $\\dt$-embedding training.\n\n\\subsection{Detector Limitations}\n\nFour constraints bound the current detector. First, the three-checkpoint window cannot distinguish transient dips from sustained collapse. Second, the acceleration condition assumes monotonically increasing overestimation during onset. Third, the detector identifies a \\emph{pattern} rather than a \\emph{mechanism}: run 009c shows that non-CIVO pathologies produce the same signature. Fourth, threshold values were calibrated on fourteen runs across three environments; generalization to different reward scales requires further validation.\n\n\\section{Dual-Critic Mechanism Ablation}\n\\label{sec:dual_critic_appendix}\n\n\\subsection{\\texorpdfstring{$2{\\times}2$}{2x2} Factorial Design}\n\nWe ablate the critic architecture in a $2{\\times}2$ factorial: \\{single, dual\\} $\\times$ \\{narrow (${\\sim}1.2$M), wide (${\\sim}2.4$M)\\} parameters. Table~\\ref{tab:dual_critic_full} reports all configurations.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Dual-critic $2{\\times}2$ factorial results. Walker Walk unless noted.}\n\\label{tab:dual_critic_full}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{Params} & \\textbf{NVE} & \\textbf{Eval} & \\textbf{Outcome} \\\\\n\\midrule\n008d & Single narrow & 1.2M & 4.12$\\times$ & 82.8 & Collapse \\\\\n033 & Wide single & 2.4M & 4.75$\\times$ & 407.9 & CIVO $\\to$ self-repair \\\\\n035 s0 & Narrow dual (min) & 1.2M & 2.75$\\times$ & 697.8 & CIVO $\\to$ recovery \\\\\n039 s1 & Narrow dual (min) & 1.2M & 2.19$\\times$ & 592.7 & CIVO $\\to$ recovery \\\\\n032 s0 & Wide dual (min) & 2.4M & $\\leq$1.1$\\times$ & 739.7 & CIVO prevented \\\\\n032b s1 & Wide dual (min) & 2.4M & 1.4$\\times$ & 551.8 & CIVO prevented \\\\\n038 s2 & Wide dual (min) & 2.4M & $\\leq$0.3$\\times$ & 120.9$^*$ & Non-CIVO collapse \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Cross-environment}} \\\\\n034 & Cheetah dual & 2.4M & 1.75$\\times$ & 97.5 & Partial recovery (31\\%) \\\\\n037 & Cheetah wide single & 2.4M & 3.60$\\times$ & 146.1 & CIVO $\\to$ self-repair \\\\\n036 & PickCube dual & 2.4M & 2.3$\\times$ & 27.7 & Transient CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize $^*$CIVO prevented (NVE $\\leq 0.3\\times$) but non-CIVO eval collapse: eval peaked at 354 (155K), then declined to 120.9 (224K) with actor entropy increasing from $-3.59$ to $-0.45$.\\par}\n\\end{table}\n\n\\subsection{Critic Convergence (\\texorpdfstring{$v_1 \\approx v_2$}{v1 ≈ v2})}\n\nAcross all dual-critic configurations and environments, the two critics converge to near-identical value functions. On Walker Walk, Pearson $\\rho > 0.999$ between $v_1$ and $v_2$ outputs; on Cheetah Run and PickCube-v1, the gap is $< 0.2$ (exact match within numerical precision). Per-sample pessimism $\\mathbb{E}[\\max(v_1, v_2) - \\min(v_1, v_2)]$ is 3--4\\% of the theoretical bound for independent critics.\n\nThis convergence occurs because both critics train on the same RSSM-generated latent features. Unlike model-free Double Q-learning, where each critic sees different mini-batches of real transitions and develops distinct function approximation errors, pure-imagination critics share identical inputs from the world model. The min operation therefore cannot provide the pessimism bias that makes Double Q effective in model-free settings.\n\n\\subsection{Recovery vs.\\ Prevention Mechanism}\n\nThe $2{\\times}2$ factorial reveals two separable dimensions:\n\n\\paragraph{Recovery (min-dominated).} The min operation is the primary factor enabling recovery from CIVO. Both narrow dual-critic seeds experience CIVO and recover fully: exp\\_035 (s0, $\\nve = 2.75\\times$, eval $33.8 \\to 697.8$, recovery ratio $20.6\\times$) and exp\\_039 (s1, $\\nve = 2.19\\times$, eval $35.9 \\to 592.7$, recovery ratio $16.5\\times$). Both outperform wide single-critic (exp\\_033, 2.4M params, eval 407.9) despite $2\\times$ fewer parameters. The min operation reduces both peak CIVO severity (2.19--2.75$\\times$ vs.\\ 4.75$\\times$ for the comparable single-critic) and enables consistent full recovery across seeds.\n\n\\paragraph{Prevention (min $+$ capacity synergy).} CIVO prevention (NVE remaining below the $1.5\\times$ threshold) requires both the min operation and increased capacity: only the wide dual-critic (exp\\_032, 3 seeds) achieves this. The mechanism for this synergy is an open question; we hypothesize that increased capacity improves value calibration quality while the min operation constrains the overestimation feedback loop during early training when the two critics briefly diverge.\n\n\\paragraph{Cross-environment limits.} On Cheetah Run, the wide dual-critic (exp\\_034) reduces NVE from $8.27\\times$ (untreated baseline) to $1.75\\times$ ($\\geq 4\\times$ reduction) but cannot prevent CIVO onset, and recovery reaches only 31\\% of the pre-CIVO peak. This confirms that the min $+$ capacity synergy has environment-dependent limits: in high-CIVO-severity environments, architecture-level interventions attenuate but do not eliminate the pathology.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " \\section{Complete Experimental Results}",
          " \\label{sec:complete_results}",
          " ",
          "-Table~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).",
          "+Table~\\ref{tab:complete_results} reports all 45 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).",
          " ",
          " \\begin{table*}[t]",
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

### Assistant

_source line 47_

修改完成。

**修改文件**: `docs/paper/sections/appendix.tex`

**插入内容**（第 72-74 行，在 008a\_ch s1 之后、019b 之前）:

| Exp | Config | dt\_emb | Sub | H | Eval@final | NVE | Outcome |
|-----|--------|---------|-----|---|------------|-----|---------|
| 077 | Cheetah baseline (s0) | --- | --- | 15 | 448.1 @105K | 1.00× | Healthy |
| 078 | Cheetah trigger (s0) | trn | ON | 8 | 119.5 @105K | 4.10× | Onset (self-corr.) |

- exp\_078 行带 `\rowcolor{gray!15}` 标记为 CIVO-positive，与现有格式一致
- 表头说明中实验总数从 43 更新为 45

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "uuid": "8f8fc339-b5d0-431c-ae3f-77d86a3b3560",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv8uaPUz4vzGvAwiNUjtAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 46580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 221
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

_source line 48_

修改完成。

**修改文件**: `docs/paper/sections/appendix.tex`

**插入内容**（第 72-74 行，在 008a\_ch s1 之后、019b 之前）:

| Exp | Config | dt\_emb | Sub | H | Eval@final | NVE | Outcome |
|-----|--------|---------|-----|---|------------|-----|---------|
| 077 | Cheetah baseline (s0) | --- | --- | 15 | 448.1 @105K | 1.00× | Healthy |
| 078 | Cheetah trigger (s0) | trn | ON | 8 | 119.5 @105K | 4.10× | Onset (self-corr.) |

- exp\_078 行带 `\rowcolor{gray!15}` 标记为 CIVO-positive，与现有格式一致
- 表头说明中实验总数从 43 更新为 45

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 82781,
  "duration_api_ms": 83587,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "24e774ad-02ae-424d-94bd-06fb5cfa91f2",
  "total_cost_usd": 0.5127325,
  "usage": {
    "input_tokens": 1082,
    "cache_creation_input_tokens": 34960,
    "cache_read_input_tokens": 433735,
    "output_tokens": 2819,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34960,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 256,
        "cache_read_input_tokens": 46580,
        "cache_creation_input_tokens": 221,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 221
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1385,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00148,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1082,
      "outputTokens": 2819,
      "cacheReadInputTokens": 433735,
      "cacheCreationInputTokens": 34960,
      "webSearchRequests": 0,
      "costUSD": 0.5112525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "428e7e89-37fa-4296-8c9b-ed939e9ca9cb"
}
```

</details>

---
