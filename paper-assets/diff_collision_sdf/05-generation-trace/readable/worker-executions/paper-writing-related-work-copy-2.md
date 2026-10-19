# paper writing related work

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260526T161140.log`
- **Structured JSON:** [`774fdf8937996009772f.json`](../../sessions/77/774fdf8937996009772f.json)

## Before a recorded user message

66 recorded events

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
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
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
  "uuid": "70a861fc-0d07-4912-a08f-124f7beba5db",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779828000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fe2bcc45-170e-4173-954c-4644066744cd",
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85"
}
```

---

### Assistant

_source line 4_

I'll start by loading all the required materials in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "0842885a-1338-4159-9cab-16bcd00849d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE4v4cCpuhj7Gt38PSDz9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12181,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12181
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01CM1RSgemNRAtg85Xc2SaJB`</summary>

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
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "37d47d2a-1ec9-4fa0-bbc5-860eb244a499",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE4v4cCpuhj7Gt38PSDz9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12181,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12181
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

_source line 6 · 2026-05-26T16:11:56.093Z_

<details><summary>↩ Tool result · `toolu_01CM1RSgemNRAtg85Xc2SaJB`</summary>

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
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "e470dff9-ae4c-48ed-8aca-e2045d477c5b",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NPsUqvveDSKUxhLNvquKSt`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "61affae1-ea4e-47eb-8bc2-37562ea83bc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE4v4cCpuhj7Gt38PSDz9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12181,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12181
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

_source line 8 · 2026-05-26T16:11:56.995Z_

<details><summary>↩ Tool result · `toolu_01NPsUqvveDSKUxhLNvquKSt`</summary>

````text
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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "603fb19d-532e-4dd3-aa04-d3122df39465",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01Ga64hHMB9cbeY8Vm8GzAbA`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "714d8a17-0fc3-46bb-bed5-29f4c4da5afe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QE4v4cCpuhj7Gt38PSDz9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12181,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12181
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

_source line 10 · 2026-05-26T16:11:57.528Z_

<details><summary>↩ Tool result · `toolu_01Ga64hHMB9cbeY8Vm8GzAbA`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "8505c425-9641-41ee-9328-2580333add3a",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 5,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now let me load the paper_framing.md, literature_map.yaml, and references.bib in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "903b773c-f3aa-48ea-9e9a-9fd91ac6cf3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJtykW4qFtit965JfQgyfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6151,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6151
      },
      "output_tokens": 20,
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0123HuvteQntAEPupbo8TXpw`</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "5fa10bf0-e3ef-4c8d-8456-80bf145ea8f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJtykW4qFtit965JfQgyfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6151,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6151
      },
      "output_tokens": 20,
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

_source line 13 · 2026-05-26T16:12:02.134Z_

<details><summary>↩ Tool result · `toolu_0123HuvteQntAEPupbo8TXpw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-26 22:50 UTC | D033: l01 3-seed 更新 + λ=0.1 升级为 3 seeds | Post-MVP research phase\\n\\n## Core Insight\\n\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（70+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明 SDF auxiliary loss 能产生真实碰撞避免——但代价极端。\\n\\n## Working Title\\n\\n\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\"\\n\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\n**Fit**: Robotics safety track — \\\"VLA safety metrics are fundamentally broken\\\" 对社区有直接影响\\n\\n## Core Claims (D028 重组: 4→3 claims)\\n\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\n\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\"safe\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\"Collision-free\\\" ≠ \\\"collision-avoiding.\\\"\\n\\n**Primary evidence — Action collapse (fake safety)**:\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\n- TSR=0% 独立确认 action collapse\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\n\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务但碰撞更多\\n- Pi0 baseline: TSR≈0%, CAR=82% — \\\"高 CAR\\\" 来自 action collapse\\n- Capability↑ → motion↑ → collision↑; 表面安全要么是 frozen (Pi0) 要么是 path geometry (Pi0.5)\\n- 限制: 仅 2 model families; 降级为 observation, 不 claim 因果\\n\\n**贡献**: 提出 EE displacement-filtered CAR (dfCAR) 作为修正指标\\n\\n**dfCAR 定位 (D024 Dream 反馈)**:\\n- Claim 1 的核心证据是 TSR=0% + obstacle displacement 双证据链，**不依赖** dfCAR\\n- dfCAR 是 **方法论贡献**（community tool），不是 Claim 1 的唯一支撑\\n- 论文需要展示 dfCAR 的实际 filtering 效果：Pi0+A1 (CAR=91.5% → dfCAR≈0%) vs Pi0.5+SDF (dfCAR=raw_CAR, no filtering)\\n- Threshold sensitivity: δ∈[2mm, 200mm] 范围内 dfCAR 完全不变（所有 active episode 最小 EE disp = 239mm）\\n\\n### Claim 2: EE-only Geometric Supervision Structural Limitations (Supporting — 证据强度 ★★★★)\\n\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Claim 3: Avoidance Source Diagnosis — Collision Avoidance Implicitly Learned from Collision-free Demos (Diagnostic — 证据强度 ★★★★ pending λ=0.1)\\n\\nPositive framing: collision avoidance capability is implicitly learned from fine-tuning on collision-free demonstration data, not from explicit geometric supervision (SDF). This reveals the source of avoidance behavior and has direct implications for future safety method design.\\n\\n**已确认 (D025/D032/D033 core)**：at λ∈{0.005, 0.01}, SDF does not improve CAR beyond LoRA-only baseline (p>0.1)。LoRA fine-tuning 本身产生 +26pp CAR（54.5% vs Pi0.5 baseline 28.5%）。\\n\\n**证据（rotation-fixed reeval 数据）**:\\n- LoRA-only (2 seeds): CAR=54.5%±2.8 (s0=56.5%, s1=52.5%), frozen=0%\\n- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)\\n- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)\\n- Per-task CAR pattern 完全一致（T3 BBQ 方差最大: l01=23.3% vs l005=20% vs LoRA=26%，种子噪声）\\n\\n**TSR collapse 机制分析 (M041)**:\\n- 复合机制：catastrophic forgetting of task semantics + retained collision avoidance\\n- SDF loss 不是 TSR 崩溃原因（LoRA baseline 崩溃幅度完全一致 -68.4% vs -68.7%）\\n- Robot 保留运动能力（0% frozen, EE ~0.5m）但丧失 goal-directed grasping/placing\\n- Safe failure rate 从 0.5% → ~50%（100×），obstacle displacement 减半\\n\\n**PROVISIONAL (D026/D033) — λ=0.1 结果决定最终叙事**：\\n\\n**量化判定阈值 (D033, Reviewer 统计分析)**：零分布 = LoRA(2) + l005(3) = 5 个无效 SDF 测量值 mean=54.5%, std=2.17%。l01 和 l1 作为独立检验对象，不纳入零分布（避免统计循环）。\\n\\n| λ=0.1 3-seed CAR 均值 | 场景 | 解读 | 论文叙事 |\\n|----------------------|------|------|---------|\\n| **≤ 57%** | **B（完全 negative）** | 噪声内，全域 SDF 无效 | Analysis paper: fake safety + dfCAR + \\\"为什么 SDF 不 work\\\" |\\n| **57-60%** | **C（剂量效应存疑）** | p=0.05-0.15 边缘，需 s2 确认 | 灰区，Pareto 分析可能反而支持 B |\\n| **60-65%** | **A-（中等剂量响应）** | +5-10pp > 2.5×SE，可信效果 | Dose-response story，需诚实呈现 TSR tradeoff |\\n| **> 65%** | **A+（强剂量响应）** | +10pp 无疑义 | \\\"低 λ 被 demo imitation masking，高 λ 突破\\\" |\\n\\n**硬约束（任一触发则 CAR 数字无效）**：\\n- TSR < 35% → action collapse，CAR 不可信\\n- frozen_ee > 0% → fake safety，CAR 增益来自冻结\\n- 两个 seed 任一 CAR < 56.5% → 不构成\\\"稳定超过 LoRA max\\\"\\n\\n⚠️ **内部一致性红线 (Reviewer)**：λ=0.1 eval **必须**用 dfCAR + EE displacement 验证。Pi0+λ=0.1 历史上产生 action collapse (CAR=90%, TSR=0%)。\\n\\n**禁区**: 在 λ=0.1 结果出来前不要 finalize Claim 3 措辞\\n\\n**待确认**:\\n- **λ=0.1 × 3 seeds** (s0/s1 ~17:00 UTC 5/27, s2 ~13:00 UTC 5/28) → 决定 A/B/C 场景 → 最终定论\\n- LoRA seed2 (plan_013) → 3v3 seeds 统计确认 low-λ 结论\\n- Phase 2 λ=0 (~8h) → 辅助证据\\n\\n### Phase 2 解读 (contingent on λ=0.1)\\n\\n- 如果场景 A/C: Phase 2 测试 \\\"SDF 训练是否造成持久行为变化\\\"\\n- 如果场景 B: Phase 2 测试 \\\"dose-dependent safety 是否 persist after removal\\\"\\n- Phase 2 CAR ≈ LoRA-only → SDF 无持久效应\\n- Phase 2 CAR < LoRA-only → SDF 造成持久损伤\\n- Phase 2 CAR > LoRA-only → SDF 有持久编码（需更多 seeds 确认）\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1 (最致命): Generalizability\\n\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\"\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)\\n→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%\\n\\n### R2: Novelty of EE-only limitation\\n→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary\\n\\n### R3: No solution\\n\\\"诊断了问题但没解决\\\"\\n→ **应对**: (1) dfCAR metric 是 positive 工具贡献; (2) 揭示 avoidance 来源（implicit demo signal, not geometric supervision）本身是 actionable insight; (3) diagnostic paper 有方法论价值——知道问题在哪比错误地以为解决了更重要\\n\\n### R4: Action collapse is trivial\\n→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论\\n\\n### R5 (更新 D025): SDF redundancy — why bother testing it?\\n→ **应对**: (1) SDF geometric supervision 在 motion planning 领域广泛使用，先验合理; (2) negative result 排除合理路径; (3) 关键 insight 是 \\\"avoidance 来自 demo imitation, not geometry\\\" — 对未来 safety method 设计有指导意义\\n\\n### R6 (D025): Fine-tuning collapse — catastrophic forgetting?\\n→ **应对**: (1) M041 分析确认是复合机制 (forgetting of task semantics + retained avoidance); (2) LoRA fine-tuning 同时提升 CAR 和降低 TSR = conservative behavior, not safe behavior; (3) SDF 不是原因（LoRA baseline 同等崩溃）\\n\\n## Narrative Structure (D028: 3 Blocks + 1 Sub-block)\\n\\n### Block 1: Fake Safety Revelation + Capability Observation (Claim 1)\\n- **Evidence**: A1 800ep (frozen), Pi0.5 3-seed (geometric path safety), Pi0 baseline (action collapse)\\n- **Key finding**: CAR=91.5% is fake (99.6% frozen); Pi0.5 CAR=27% is geometric; neither is avoidance\\n- **Contribution**: dfCAR metric + threshold sensitivity analysis\\n- **Sub-block**: Capability↑ → motion↑ → collision↑ as supporting observation\\n\\n### Block 2: EE-only Geometric Supervision Boundary (Claim 2)\\n- **Evidence**: 3 oracle variants all < baseline; arm-body collision analysis\\n- **Narrative**: Runtime gradient correction structurally fails — alpha schedule and representation don't help; EE-only SDF = structural scope limit\\n- **Presentation**: Single unified table + collision part analysis\\n\\n### Block 3: Avoidance Source Diagnosis (Claim 3)\\n- **Evidence**: LoRA-only 2-3 seeds + SDF 3 seeds × 2-3 lambdas, per-task comparison\\n- **Key finding**: LoRA-only CAR=54.5% ≈ SDF l005 CAR=54.5%, both TSR~50-54%, identical per-task patterns\\n- **Narrative**: Collision avoidance is implicitly learned from collision-free demo data. Explicit SDF geometric supervision adds nothing at low λ. The avoidance signal is in the training distribution, not in the loss function.\\n- **TSR collapse analysis**: composite mechanism (task forgetting + avoidance retention)\\n- **Sub-narrative**: λ curve (pending λ=0.1) + Phase 2 persistence\\n\\n### 叙事原则\\n1. 每个 block 是 **evidence for structural claims**\\n2. Block 间逻辑递进：metric 有缺陷 (B1) → geometric supervision 有结构缺陷 (B2) → avoidance 来源是 demo data 而非 geometry (B3)\\n3. B3 是 positive diagnostic insight，展示\\\"避障可实现且来源是隐式学习\\\"\\n\\n## Figure Plan\\n\\n| ID | 内容 | Claim | 优先级 | 数据来源 | 状态 |\\n|----|------|-------|--------|---------|------|\\n| Fig 1 | Fake vs real safety 概念图 (displacement 对比) | 1 | 重要 | 设计 | 待做 |\\n| Fig 2 | EE Displacement 分布 (A1-frozen vs Pi0.5+A1-moving vs baseline) | 1 | **必须** | 修复后 eval JSON | 数据就绪 |\\n| Fig 3 | TSR-CAR scatter (多模型 + capability observation) | 1 | 重要 | 全部 eval 数据 | 数据就绪 |\\n| Fig 4 | Oracle refinement CAR bar chart + arm-body collision | 2 | **必须** | 3 oracle + baselines | 数据就绪 |\\n| Table 1 | 3-seed × 2-lambda × best/30K 完整结果矩阵 + EE disp | 3 | **必须** | Pi0.5+A1 修正数据 | 数据就绪 |\\n| Fig 5 | Lambda-CAR/TSR 曲线 (含 LoRA baseline 作 λ=0 点) | 3 | **必须** | LoRA baseline + SDF 数据 | 待 λ=0.1 |\\n| Table 2 | Phase 2 λ=0 ablation 结果 | 3 | 重要 | Phase 2 训练 | RUNNING |\\n\\n## Dependencies (Research Phase)\\n\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake (obstacle disp)\\n- [x] Pi0.5 baseline 3-seed (Claim 1 supporting) — CAR=26.8±1.6%, TSR=74.7±1.5%\\n- [x] Pi0.5+A1 3-seed × 2-lambda 训练 + eval (Claim 3) — confirmed real avoidance (D023)\\n- [x] EE displacement 修正 eval (Claim 3) — 3 seeds corrected, all consistent\\n- [x] Oracle 3 variants (Claim 2) — all < baseline\\n- [x] Spatial/object collision analysis (Claim 2) — arm-body dominant\\n- [x] **LoRA baseline** (Claim 3 attribution) — DONE: CAR=55%, SDF delta=0pp (D025)\\n- [x] **TSR collapse mechanism analysis** (Claim 3) — M041: composite (forgetting + avoidance retention)\\n- [ ] **LoRA baseline seed2** (plan_013, Claim 3) — RUNNING on westd-45947\\n- [ ] **Phase 2 λ=0** (Claim 3) — RUNNING on cuda:3\\n- [ ] **spatial_bowl A1 训练** (Claim 3) — RUNNING on cuda:0, ~20h\\n- [ ] **Lambda=0.1 × 3 seeds** (Claim 3) — RUNNING: s0/s1 on 35807 cuda:1-2 (~17h), s2 on 45947 cuda:1 (~38h)\\n- [ ] **Pi0.5 baseline re-eval** (Claim 1) — RUNNING westd-45947, 补 EE displacement baseline\\n- [ ] **OpenVLA zero-shot eval** (Claim 1) — BLOCKED (模型下载损坏)\\n\", \"total_chars\": 10236, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "83022765-3414-49c4-b593-32f9916e5b7e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\\\", \\\"content\\\": \\\"# ColliForce-VLA Paper Framing\\\\n\\\\n> 维护者: Director | 最后更新: 2026-05-26 22:50 UTC | D033: l01 3-seed 更新 + λ=0.1 升级为 3 seeds | Post-MVP research phase\\\\n\\\\n## Core Insight\\\\n\\\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\\\\\"安全\\\\\\\" 指标虚高。我们通过大规模实证分析（70+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明 SDF auxiliary loss 能产生真实碰撞避免——但代价极端。\\\\n\\\\n## Working Title\\\\n\\\\n\\\\\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\\\\\"\\\\n\\\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\\\n\\\\n## Target Venue\\\\n\\\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\\\n**Fit**: Robotics safety track — \\\\\\\"VLA safety metrics are fundamentally broken\\\\\\\" 对社区有直接影响\\\\n\\\\n## Core Claims (D028 重组: 4→3 claims)\\\\n\\\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\\\n\\\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\\\\\"safe\\\\\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\\\\\"Collision-free\\\\\\\" ≠ \\\\\\\"collision-avoiding.\\\\\\\"\\\\n\\\\n**Primary evidence — Action collapse (fake safety)**:\\\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\\\n- TSR=0% 独立确认 action collapse\\\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\\\n\\\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务但碰撞更多\\\\n- Pi0 baseline: TSR≈0%, CAR=82% — \\\\\\\"高 CAR\\\\\\\" 来自 action collapse\\\\n- Capability↑ → motion↑ → collision↑; 表面安全要么是 frozen (Pi0) 要么是 path geometry (Pi0.5)\\\\n- 限制: 仅 2 model families; 降级为 observation, 不 claim 因果\\\\n\\\\n**贡献**: 提出 EE displacement-filtered CAR (dfCAR) 作为修正指标\\\\n\\\\n**dfCAR 定位 (D024 Dream 反馈)**:\\\\n- Claim 1 的核心证据是 TSR=0% + obstacle displacement 双证据链，**不依赖** dfCAR\\\\n- dfCAR 是 **方法论贡献**（community tool），不是 Claim 1 的唯一支撑\\\\n- 论文需要展示 dfCAR 的实际 filtering 效果：Pi0+A1 (CAR=91.5% → dfCAR≈0%) vs Pi0.5+SDF (dfCAR=raw_CAR, no filtering)\\\\n- Threshold sensitivity: δ∈[2mm, 200mm] 范围内 dfCAR 完全不变（所有 active episode 最小 EE disp = 239mm）\\\\n\\\\n### Claim 2: EE-only Geometric Supervision Structural Limitations (Supporting — 证据强度 ★★★★)\\\\n\\\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\\\n\\\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\\\n**限制**: \\\\\\\"EE-only 不够\\\\\\\" 是 expected result; 缺乏 full-body SDF 对照\\\\n\\\\n### Claim 3: Avoidance Source Diagnosis — Collision Avoidance Implicitly Learned from Collision-free Demos (Diagnostic — 证据强度 ★★★★ pending λ=0.1)\\\\n\\\\nPositive framing: collision avoidance capability is implicitly learned from fine-tuning on collision-free demonstration data, not from explicit geometric supervision (SDF). This reveals the source of avoidance behavior and has direct implications for future safety method design.\\\\n\\\\n**已确认 (D025/D032/D033 core)**：at λ∈{0.005, 0.01}, SDF does not improve CAR beyond LoRA-only baseline (p>0.1)。LoRA fine-tuning 本身产生 +26pp CAR（54.5% vs Pi0.5 baseline 28.5%）。\\\\n\\\\n**证据（rotation-fixed reeval 数据）**:\\\\n- LoRA-only (2 seeds): CAR=54.5%±2.8 (s0=56.5%, s1=52.5%), frozen=0%\\\\n- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)\\\\n- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)\\\\n- Per-task CAR pattern 完全一致（T3 BBQ 方差最大: l01=23.3% vs l005=20% vs LoRA=26%，种子噪声）\\\\n\\\\n**TSR collapse 机制分析 (M041)**:\\\\n- 复合机制：catastrophic forgetting of task semantics + retained collision avoidance\\\\n- SDF loss 不是 TSR 崩溃原因（LoRA baseline 崩溃幅度完全一致 -68.4% vs -68.7%）\\\\n- Robot 保留运动能力（0% frozen, EE ~0.5m）但丧失 goal-directed grasping/placing\\\\n- Safe failure rate 从 0.5% → ~50%（100×），obstacle displacement 减半\\\\n\\\\n**PROVISIONAL (D026/D033) — λ=0.1 结果决定最终叙事**：\\\\n\\\\n**量化判定阈值 (D033, Reviewer 统计分析)**：零分布 = LoRA(2) + l005(3) = 5 个无效 SDF 测量值 mean=54.5%, std=2.17%。l01 和 l1 作为独立检验对象，不纳入零分布（避免统计循环）。\\\\n\\\\n| λ=0.1 3-seed CAR 均值 | 场景 | 解读 | 论文叙事 |\\\\n|----------------------|------|------|---------|\\\\n| **≤ 57%** | **B（完全 negative）** | 噪声内，全域 SDF 无效 | Analysis paper: fake safety + dfCAR + \\\\\\\"为什么 SDF 不 work\\\\\\\" |\\\\n| **57-60%** | **C（剂量效应存疑）** | p=0.05-0.15 边缘，需 s2 确认 | 灰区，Pareto 分析可能反而支持 B |\\\\n| **60-65%** | **A-（中等剂量响应）** | +5-10pp > 2.5×SE，可信效果 | Dose-response story，需诚实呈现 TSR tradeoff |\\\\n| **> 65%** | **A+（强剂量响应）** | +10pp 无疑义 | \\\\\\\"低 λ 被 demo imitation masking，高 λ 突破\\\\\\\" |\\\\n\\\\n**硬约束（任一触发则 CAR 数字无效）**：\\\\n- TSR < 35% → action collapse，CAR 不可信\\\\n- frozen_ee > 0% → fake safety，CAR 增益来自冻结\\\\n- 两个 seed 任一 CAR < 56.5% → 不构成\\\\\\\"稳定超过 LoRA max\\\\\\\"\\\\n\\\\n⚠️ **内部一致性红线 (Reviewer)**：λ=0.1 eval **必须**用 dfCAR + EE displacement 验证。Pi0+λ=0.1 历史上产生 action collapse (CAR=90%, TSR=0%)。\\\\n\\\\n**禁区**: 在 λ=0.1 结果出来前不要 finalize Claim 3 措辞\\\\n\\\\n**待确认**:\\\\n- **λ=0.1 × 3 seeds** (s0/s1 ~17:00 UTC 5/27, s2 ~13:00 UTC 5/28) → 决定 A/B/C 场景 → 最终定论\\\\n- LoRA seed2 (plan_013) → 3v3 seeds 统计确认 low-λ 结论\\\\n- Phase 2 λ=0 (~8h) → 辅助证据\\\\n\\\\n### Phase 2 解读 (contingent on λ=0.1)\\\\n\\\\n- 如果场景 A/C: Phase 2 测试 \\\\\\\"SDF 训练是否造成持久行为变化\\\\\\\"\\\\n- 如果场景 B: Phase 2 测试 \\\\\\\"dose-dependent safety 是否 persist after removal\\\\\\\"\\\\n- Phase 2 CAR ≈ LoRA-only → SDF 无持久效应\\\\n- Phase 2 CAR < LoRA-only → SDF 造成持久损伤\\\\n- Phase 2 CAR > LoRA-only → SDF 有持久编码（需更多 seeds 确认）\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### R1 (最致命): Generalizability\\\\n\\\\\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\\\\\"\\\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)\\\\n→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%\\\\n\\\\n### R2: Novelty of EE-only limitation\\\\n→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary\\\\n\\\\n### R3: No solution\\\\n\\\\\\\"诊断了问题但没解决\\\\\\\"\\\\n→ **应对**: (1) dfCAR metric 是 positive 工具贡献; (2) 揭示 avoidance 来源（implicit demo signal, not geometric supervision）本身是 actionable insight; (3) diagnostic paper 有方法论价值——知道问题在哪比错误地以为解决了更重要\\\\n\\\\n### R4: Action collapse is trivial\\\\n→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论\\\\n\\\\n### R5 (更新 D025): SDF redundancy — why bother testing it?\\\\n→ **应对**: (1) SDF geometric supervision 在 motion planning 领域广泛使用，先验合理; (2) negative result 排除合理路径; (3) 关键 insight 是 \\\\\\\"avoidance 来自 demo imitation, not geometry\\\\\\\" — 对未来 safety method 设计有指导意义\\\\n\\\\n### R6 (D025): Fine-tuning collapse — catastrophic forgetting?\\\\n→ **应对**: (1) M041 分析确认是复合机制 (forgetting of task semantics + retained avoidance); (2) LoRA fine-tuning 同时提升 CAR 和降低 TSR = conservative behavior, not safe behavior; (3) SDF 不是原因（LoRA baseline 同等崩溃）\\\\n\\\\n## Narrative Structure (D028: 3 Blocks + 1 Sub-block)\\\\n\\\\n### Block 1: Fake Safety Revelation + Capability Observation (Claim 1)\\\\n- **Evidence**: A1 800ep (frozen), Pi0.5 3-seed (geometric path safety), Pi0 baseline (action collapse)\\\\n- **Key finding**: CAR=91.5% is fake (99.6% frozen); Pi0.5 CAR=27% is geometric; neither is avoidance\\\\n- **Contribution**: dfCAR metric + threshold sensitivity analysis\\\\n- **Sub-block**: Capability↑ → motion↑ → collision↑ as supporting observation\\\\n\\\\n### Block 2: EE-only Geometric Supervision Boundary (Claim 2)\\\\n- **Evidence**: 3 oracle variants all < baseline; arm-body collision analysis\\\\n- **Narrative**: Runtime gradient correction structurally fails — alpha schedule and representation don't help; EE-only SDF = structural scope limit\\\\n- **Presentation**: Single unified table + collision part analysis\\\\n\\\\n### Block 3: Avoidance Source Diagnosis (Claim 3)\\\\n- **Evidence**: LoRA-only 2-3 seeds + SDF 3 seeds × 2-3 lambdas, per-task comparison\\\\n- **Key finding**: LoRA-only CAR=54.5% ≈ SDF l005 CAR=54.5%, both TSR~50-54%, identical per-task patterns\\\\n- **Narrative**: Collision avoidance is implicitly learned from collision-free demo data. Explicit SDF geometric supervision adds nothing at low λ. The avoidance signal is in the training distribution, not in the loss function.\\\\n- **TSR collapse analysis**: composite mechanism (task forgetting + avoidance retention)\\\\n- **Sub-narrative**: λ curve (pending λ=0.1) + Phase 2 persistence\\\\n\\\\n### 叙事原则\\\\n1. 每个 block 是 **evidence for structural claims**\\\\n2. Block 间逻辑递进：metric 有缺陷 (B1) → geometric supervision 有结构缺陷 (B2) → avoidance 来源是 demo data 而非 geometry (B3)\\\\n3. B3 是 positive diagnostic insight，展示\\\\\\\"避障可实现且来源是隐式学习\\\\\\\"\\\\n\\\\n## Figure Plan\\\\n\\\\n| ID | 内容 | Claim | 优先级 | 数据来源 | 状态 |\\\\n|----|------|-------|--------|---------|------|\\\\n| Fig 1 | Fake vs real safety 概念图 (displacement 对比) | 1 | 重要 | 设计 | 待做 |\\\\n| Fig 2 | EE Displacement 分布 (A1-frozen vs Pi0.5+A1-moving vs baseline) | 1 | **必须** | 修复后 eval JSON | 数据就绪 |\\\\n| Fig 3 | TSR-CAR scatter (多模型 + capability observation) | 1 | 重要 | 全部 eval 数据 | 数据就绪 |\\\\n| Fig 4 | Oracle refinement CAR bar chart + arm-body collision | 2 | **必须** | 3 oracle + baselines | 数据就绪 |\\\\n| Table 1 | 3-seed × 2-lambda × best/30K 完整结果矩阵 + EE disp | 3 | **必须** | Pi0.5+A1 修正数据 | 数据就绪 |\\\\n| Fig 5 | Lambda-CAR/TSR 曲线 (含 LoRA baseline 作 λ=0 点) | 3 | **必须** | LoRA baseline + SDF 数据 | 待 λ=0.1 |\\\\n| Table 2 | Phase 2 λ=0 ablation 结果 | 3 | 重要 | Phase 2 训练 | RUNNING |\\\\n\\\\n## Dependencies (Research Phase)\\\\n\\\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake (obstacle disp)\\\\n- [x] Pi0.5 baseline 3-seed (Claim 1 supporting) — CAR=26.8±1.6%, TSR=74.7±1.5%\\\\n- [x] Pi0.5+A1 3-seed × 2-lambda 训练 + eval (Claim 3) — confirmed real avoidance (D023)\\\\n- [x] EE displacement 修正 eval (Claim 3) — 3 seeds corrected, all consistent\\\\n- [x] Oracle 3 variants (Claim 2) — all < baseline\\\\n- [x] Spatial/object collision analysis (Claim 2) — arm-body dominant\\\\n- [x] **LoRA baseline** (Claim 3 attribution) — DONE: CAR=55%, SDF delta=0pp (D025)\\\\n- [x] **TSR collapse mechanism analysis** (Claim 3) — M041: composite (forgetting + avoidance retention)\\\\n- [ ] **LoRA baseline seed2** (plan_013, Claim 3) — RUNNING on westd-45947\\\\n- [ ] **Phase 2 λ=0** (Claim 3) — RUNNING on cuda:3\\\\n- [ ] **spatial_bowl A1 训练** (Claim 3) — RUNNING on cuda:0, ~20h\\\\n- [ ] **Lambda=0.1 × 3 seeds** (Claim 3) — RUNNING: s0/s1 on 35807 cuda:1-2 (~17h), s2 on 45947 cuda:1 (~38h)\\\\n- [ ] **Pi0.5 baseline re-eval** (Claim 1) — RUNNING westd-45947, 补 EE displacement baseline\\\\n- [ ] **OpenVLA zero-shot eval** (Claim 1) — BLOCKED (模型下载损坏)\\\\n\\\", \\\"total_chars\\\": 10236, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-26 22:50 UTC | D033: l01 3-seed 更新 + λ=0.1 升级为 3 seeds | Post-MVP research phase\\n\\n## Core Insight\\n\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（70+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明 SDF auxiliary loss 能产生真实碰撞避免——但代价极端。\\n\\n## Working Title\\n\\n\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\"\\n\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\n**Fit**: Robotics safety track — \\\"VLA safety metrics are fundamentally broken\\\" 对社区有直接影响\\n\\n## Core Claims (D028 重组: 4→3 claims)\\n\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\n\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\"safe\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\"Collision-free\\\" ≠ \\\"collision-avoiding.\\\"\\n\\n**Primary evidence — Action collapse (fake safety)**:\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\n- TSR=0% 独立确认 action collapse\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\n\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务但碰撞更多\\n- Pi0 baseline: TSR≈0%, CAR=82% — \\\"高 CAR\\\" 来自 action collapse\\n- Capability↑ → motion↑ → collision↑; 表面安全要么是 frozen (Pi0) 要么是 path geometry (Pi0.5)\\n- 限制: 仅 2 model families; 降级为 observation, 不 claim 因果\\n\\n**贡献**: 提出 EE displacement-filtered CAR (dfCAR) 作为修正指标\\n\\n**dfCAR 定位 (D024 Dream 反馈)**:\\n- Claim 1 的核心证据是 TSR=0% + obstacle displacement 双证据链，**不依赖** dfCAR\\n- dfCAR 是 **方法论贡献**（community tool），不是 Claim 1 的唯一支撑\\n- 论文需要展示 dfCAR 的实际 filtering 效果：Pi0+A1 (CAR=91.5% → dfCAR≈0%) vs Pi0.5+SDF (dfCAR=raw_CAR, no filtering)\\n- Threshold sensitivity: δ∈[2mm, 200mm] 范围内 dfCAR 完全不变（所有 active episode 最小 EE disp = 239mm）\\n\\n### Claim 2: EE-only Geometric Supervision Structural Limitations (Supporting — 证据强度 ★★★★)\\n\\nEnd-effector-only SDF 在 action space 的碰撞避免存在结构性缺陷：SDF gradient 推 EE 远离障碍物但导致 arm body 扫过障碍物。\\n\\n**证据**: 3 组 GT SDF oracle (adaptive alpha, fixed alpha, feature-space) 均劣于 baseline; spatial vs object 碰撞部位分析; obstacle 高度/体积与碰撞率的单调关系\\n**限制**: \\\"EE-only 不够\\\" 是 expected result; 缺乏 full-body SDF 对照\\n\\n### Claim 3: Avoidance Source Diagnosis — Collision Avoidance Implicitly Learned from Collision-free Demos (Diagnostic — 证据强度 ★★★★ pending λ=0.1)\\n\\nPositive framing: collision avoidance capability is implicitly learned from fine-tuning on collision-free demonstration data, not from explicit geometric supervision (SDF). This reveals the source of avoidance behavior and has direct implications for future safety method design.\\n\\n**已确认 (D025/D032/D033 core)**：at λ∈{0.005, 0.01}, SDF does not improve CAR beyond LoRA-only baseline (p>0.1)。LoRA fine-tuning 本身产生 +26pp CAR（54.5% vs Pi0.5 baseline 28.5%）。\\n\\n**证据（rotation-fixed reeval 数据）**:\\n- LoRA-only (2 seeds): CAR=54.5%±2.8 (s0=56.5%, s1=52.5%), frozen=0%\\n- LoRA+SDF λ=0.005 (3 seeds): CAR=54.5%±2.3 (s0=57, s1=54, s2=52.5)\\n- LoRA+SDF λ=0.01 (3 seeds): CAR=56.33%±1.61 (s0=57, s1=57.5, s2=54.5) — p≈0.12 不显著，per-task 无系统提升，Task 3 驱动方差 s0=34%→s2=14% (D033)\\n- Per-task CAR pattern 完全一致（T3 BBQ 方差最大: l01=23.3% vs l005=20% vs LoRA=26%，种子噪声）\\n\\n**TSR collapse 机制分析 (M041)**:\\n- 复合机制：catastrophic forgetting of task semantics + retained collision avoidance\\n- SDF loss 不是 TSR 崩溃原因（LoRA baseline 崩溃幅度完全一致 -68.4% vs -68.7%）\\n- Robot 保留运动能力（0% frozen, EE ~0.5m）但丧失 goal-directed grasping/placing\\n- Safe failure rate 从 0.5% → ~50%（100×），obstacle displacement 减半\\n\\n**PROVISIONAL (D026/D033) — λ=0.1 结果决定最终叙事**：\\n\\n**量化判定阈值 (D033, Reviewer 统计分析)**：零分布 = LoRA(2) + l005(3) = 5 个无效 SDF 测量值 mean=54.5%, std=2.17%。l01 和 l1 作为独立检验对象，不纳入零分布（避免统计循环）。\\n\\n| λ=0.1 3-seed CAR 均值 | 场景 | 解读 | 论文叙事 |\\n|----------------------|------|------|---------|\\n| **≤ 57%** | **B（完全 negative）** | 噪声内，全域 SDF 无效 | Analysis paper: fake safety + dfCAR + \\\"为什么 SDF 不 work\\\" |\\n| **57-60%** | **C（剂量效应存疑）** | p=0.05-0.15 边缘，需 s2 确认 | 灰区，Pareto 分析可能反而支持 B |\\n| **60-65%** | **A-（中等剂量响应）** | +5-10pp > 2.5×SE，可信效果 | Dose-response story，需诚实呈现 TSR tradeoff |\\n| **> 65%** | **A+（强剂量响应）** | +10pp 无疑义 | \\\"低 λ 被 demo imitation masking，高 λ 突破\\\" |\\n\\n**硬约束（任一触发则 CAR 数字无效）**：\\n- TSR < 35% → action collapse，CAR 不可信\\n- frozen_ee > 0% → fake safety，CAR 增益来自冻结\\n- 两个 seed 任一 CAR < 56.5% → 不构成\\\"稳定超过 LoRA max\\\"\\n\\n⚠️ **内部一致性红线 (Reviewer)**：λ=0.1 eval **必须**用 dfCAR + EE displacement 验证。Pi0+λ=0.1 历史上产生 action collapse (CAR=90%, TSR=0%)。\\n\\n**禁区**: 在 λ=0.1 结果出来前不要 finalize Claim 3 措辞\\n\\n**待确认**:\\n- **λ=0.1 × 3 seeds** (s0/s1 ~17:00 UTC 5/27, s2 ~13:00 UTC 5/28) → 决定 A/B/C 场景 → 最终定论\\n- LoRA seed2 (plan_013) → 3v3 seeds 统计确认 low-λ 结论\\n- Phase 2 λ=0 (~8h) → 辅助证据\\n\\n### Phase 2 解读 (contingent on λ=0.1)\\n\\n- 如果场景 A/C: Phase 2 测试 \\\"SDF 训练是否造成持久行为变化\\\"\\n- 如果场景 B: Phase 2 测试 \\\"dose-dependent safety 是否 persist after removal\\\"\\n- Phase 2 CAR ≈ LoRA-only → SDF 无持久效应\\n- Phase 2 CAR < LoRA-only → SDF 造成持久损伤\\n- Phase 2 CAR > LoRA-only → SDF 有持久编码（需更多 seeds 确认）\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1 (最致命): Generalizability\\n\\\"仅在 SafeLIBERO + Pi0 系列上验证, 凭什么说 fake safety 是普遍问题?\\\"\\n→ **应对**: (1) 2+ tasks (object_pudding + spatial_bowl); (2) 3+ models (Pi0 + Pi0.5 + OpenVLA); (3) 收窄 claim scope + mechanistic argument (any model with low task capability will exhibit fake safety)\\n→ **接受率估算**: 1 task/2 model ~40% / 2 tasks+3 models ~55-65% / 3+ tasks ~65-75%\\n\\n### R2: Novelty of EE-only limitation\\n→ **应对**: 定量分析 (arm-body vs EE 碰撞比例 + oracle 排除其他解释); supporting claim 而非 primary\\n\\n### R3: No solution\\n\\\"诊断了问题但没解决\\\"\\n→ **应对**: (1) dfCAR metric 是 positive 工具贡献; (2) 揭示 avoidance 来源（implicit demo signal, not geometric supervision）本身是 actionable insight; (3) diagnostic paper 有方法论价值——知道问题在哪比错误地以为解决了更重要\\n\\n### R4: Action collapse is trivial\\n→ **应对**: 原因可能 trivial，但 metric contamination 后果 non-trivial; 后续工作基于被污染 CAR 得出错误结论\\n\\n### R5 (更新 D025): SDF redundancy — why bother testing it?\\n→ **应对**: (1) SDF geometric supervision 在 motion planning 领域广泛使用，先验合理; (2) negative result 排除合理路径; (3) 关键 insight 是 \\\"avoidance 来自 demo imitation, not geometry\\\" — 对未来 safety method 设计有指导意义\\n\\n### R6 (D025): Fine-tuning collapse — catastrophic forgetting?\\n→ **应对**: (1) M041 分析确认是复合机制 (forgetting of task semantics + retained avoidance); (2) LoRA fine-tuning 同时提升 CAR 和降低 TSR = conservative behavior, not safe behavior; (3) SDF 不是原因（LoRA baseline 同等崩溃）\\n\\n## Narrative Structure (D028: 3 Blocks + 1 Sub-block)\\n\\n### Block 1: Fake Safety Revelation + Capability Observation (Claim 1)\\n- **Evidence**: A1 800ep (frozen), Pi0.5 3-seed (geometric path safety), Pi0 baseline (action collapse)\\n- **Key finding**: CAR=91.5% is fake (99.6% frozen); Pi0.5 CAR=27% is geometric; neither is avoidance\\n- **Contribution**: dfCAR metric + threshold sensitivity analysis\\n- **Sub-block**: Capability↑ → motion↑ → collision↑ as supporting observation\\n\\n### Block 2: EE-only Geometric Supervision Boundary (Claim 2)\\n- **Evidence**: 3 oracle variants all < baseline; arm-body collision analysis\\n- **Narrative**: Runtime gradient correction structurally fails — alpha schedule and representation don't help; EE-only SDF = structural scope limit\\n- **Presentation**: Single unified table + collision part analysis\\n\\n### Block 3: Avoidance Source Diagnosis (Claim 3)\\n- **Evidence**: LoRA-only 2-3 seeds + SDF 3 seeds × 2-3 lambdas, per-task comparison\\n- **Key finding**: LoRA-only CAR=54.5% ≈ SDF l005 CAR=54.5%, both TSR~50-54%, identical per-task patterns\\n- **Narrative**: Collision avoidance is implicitly learned from collision-free demo data. Explicit SDF geometric supervision adds nothing at low λ. The avoidance signal is in the training distribution, not in the loss function.\\n- **TSR collapse analysis**: composite mechanism (task forgetting + avoidance retention)\\n- **Sub-narrative**: λ curve (pending λ=0.1) + Phase 2 persistence\\n\\n### 叙事原则\\n1. 每个 block 是 **evidence for structural claims**\\n2. Block 间逻辑递进：metric 有缺陷 (B1) → geometric supervision 有结构缺陷 (B2) → avoidance 来源是 demo data 而非 geometry (B3)\\n3. B3 是 positive diagnostic insight，展示\\\"避障可实现且来源是隐式学习\\\"\\n\\n## Figure Plan\\n\\n| ID | 内容 | Claim | 优先级 | 数据来源 | 状态 |\\n|----|------|-------|--------|---------|------|\\n| Fig 1 | Fake vs real safety 概念图 (displacement 对比) | 1 | 重要 | 设计 | 待做 |\\n| Fig 2 | EE Displacement 分布 (A1-frozen vs Pi0.5+A1-moving vs baseline) | 1 | **必须** | 修复后 eval JSON | 数据就绪 |\\n| Fig 3 | TSR-CAR scatter (多模型 + capability observation) | 1 | 重要 | 全部 eval 数据 | 数据就绪 |\\n| Fig 4 | Oracle refinement CAR bar chart + arm-body collision | 2 | **必须** | 3 oracle + baselines | 数据就绪 |\\n| Table 1 | 3-seed × 2-lambda × best/30K 完整结果矩阵 + EE disp | 3 | **必须** | Pi0.5+A1 修正数据 | 数据就绪 |\\n| Fig 5 | Lambda-CAR/TSR 曲线 (含 LoRA baseline 作 λ=0 点) | 3 | **必须** | LoRA baseline + SDF 数据 | 待 λ=0.1 |\\n| Table 2 | Phase 2 λ=0 ablation 结果 | 3 | 重要 | Phase 2 训练 | RUNNING |\\n\\n## Dependencies (Research Phase)\\n\\n- [x] A1 fake safety 800ep (Claim 1) — 99.6% fake (obstacle disp)\\n- [x] Pi0.5 baseline 3-seed (Claim 1 supporting) — CAR=26.8±1.6%, TSR=74.7±1.5%\\n- [x] Pi0.5+A1 3-seed × 2-lambda 训练 + eval (Claim 3) — confirmed real avoidance (D023)\\n- [x] EE displacement 修正 eval (Claim 3) — 3 seeds corrected, all consistent\\n- [x] Oracle 3 variants (Claim 2) — all < baseline\\n- [x] Spatial/object collision analysis (Claim 2) — arm-body dominant\\n- [x] **LoRA baseline** (Claim 3 attribution) — DONE: CAR=55%, SDF delta=0pp (D025)\\n- [x] **TSR collapse mechanism analysis** (Claim 3) — M041: composite (forgetting + avoidance retention)\\n- [ ] **LoRA baseline seed2** (plan_013, Claim 3) — RUNNING on westd-45947\\n- [ ] **Phase 2 λ=0** (Claim 3) — RUNNING on cuda:3\\n- [ ] **spatial_bowl A1 训练** (Claim 3) — RUNNING on cuda:0, ~20h\\n- [ ] **Lambda=0.1 × 3 seeds** (Claim 3) — RUNNING: s0/s1 on 35807 cuda:1-2 (~17h), s2 on 45947 cuda:1 (~38h)\\n- [ ] **Pi0.5 baseline re-eval** (Claim 1) — RUNNING westd-45947, 补 EE displacement baseline\\n- [ ] **OpenVLA zero-shot eval** (Claim 1) — BLOCKED (模型下载损坏)\\n\", \"total_chars\": 10236, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CWhZoxsYdrRFHyARva2H1u`</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "c2e6690e-d0d5-4b63-bd2f-50095222104c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJtykW4qFtit965JfQgyfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6151,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6151
      },
      "output_tokens": 20,
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

_source line 15 · 2026-05-26T16:12:02.610Z_

<details><summary>↩ Tool result · `toolu_01CWhZoxsYdrRFHyARva2H1u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\", \"content\": \"# ColliForce-VLA Literature Map\\n# Updated: 2026-05-25\\n\\npapers:\\n\\n  # ===== 已有论文 =====\\n\\n  - paper_id: \\\"2512.11891\\\"\\n    title: \\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\"\\n    authors: \\\"Hu et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\"\\n\\n  - paper_id: \\\"2510.14836\\\"\\n    title: \\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\"\\n\\n  - paper_id: \\\"2510.12276\\\"\\n    title: \\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICLR 2026\\n    role: method-component\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\"\\n\\n  - paper_id: \\\"2307.05973\\\"\\n    title: \\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: CoRL 2023\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\"\\n\\n  - paper_id: \\\"2410.24164\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al., Physical Intelligence\\\"\\n    year: 2024\\n    venue: arXiv\\n    role: backbone\\n    category: vla-foundation\\n    one_line_summary: \\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\"\\n\\n  - paper_id: \\\"1901.05103\\\"\\n    title: \\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\"\\n    authors: \\\"Park et al.\\\"\\n    year: 2019\\n    venue: CVPR 2019\\n    role: method-component\\n    category: sdf-representation\\n    one_line_summary: \\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\"\\n\\n  - paper_id: \\\"2307.00533\\\"\\n    title: \\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: arXiv\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\"\\n\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\n\\n  - paper_id: \\\"2503.03480\\\"\\n    title: \\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    arxiv: \\\"2503.03480\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\"\\n    relevance: \\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\"\\n\\n  - paper_id: \\\"2407.00451\\\"\\n    title: \\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2024\\n    venue: ICRA 2025\\n    arxiv: \\\"2407.00451\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\"\\n    relevance: \\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\"\\n\\n  - paper_id: \\\"2511.22773\\\"\\n    title: \\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\"\\n    authors: \\\"Yang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2511.22773\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\"\\n    relevance: \\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\"\\n\\n  - paper_id: \\\"2409.08233\\\"\\n    title: \\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\"\\n    authors: \\\"Spalter et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.08233\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\"\\n    relevance: \\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\"\\n\\n  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\\n\\n  - paper_id: \\\"2601.21712\\\"\\n    title: \\\"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\\\"\\n    authors: \\\"Zhai et al.\\\"\\n    year: 2026\\n    venue: arXiv\\n    arxiv: \\\"2601.21712\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\\\"\\n    relevance: \\\"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\\\"\\n\\n  - paper_id: \\\"2404.02284\\\"\\n    title: \\\"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\\\"\\n    authors: \\\"Dastider et al.\\\"\\n    year: 2024\\n    venue: IROS 2024\\n    arxiv: \\\"2404.02284\\\"\\n    role: related-approach\\n    category: collision-aware-manipulation\\n    summary: \\\"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\\\"\\n    relevance: \\\"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\\\"\\n\\n  - paper_id: \\\"2512.11908\\\"\\n    title: \\\"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2512.11908\\\"\\n    role: survey\\n    category: collision-aware-manipulation\\n    summary: \\\"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\\\"\\n    relevance: \\\"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\\\"\\n\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\n\\n  - paper_id: \\\"2204.02296\\\"\\n    title: \\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\"\\n    authors: \\\"Ortiz et al.\\\"\\n    year: 2022\\n    venue: RSS 2022\\n    arxiv: \\\"2204.02296\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\"\\n    relevance: \\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\"\\n\\n  - paper_id: \\\"2305.10534\\\"\\n    title: \\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\"\\n    authors: \\\"Vasilopoulos et al.\\\"\\n    year: 2023\\n    venue: IROS 2023\\n    arxiv: \\\"2305.10534\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\"\\n    relevance: \\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\"\\n\\n  - paper_id: \\\"2102.07413\\\"\\n    title: \\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\"\\n    authors: \\\"Zhi et al.\\\"\\n    year: 2021\\n    venue: IEEE T-RO\\n    arxiv: \\\"2102.07413\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\"\\n    relevance: \\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\"\\n\\n  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====\\n\\n  - paper_id: \\\"2406.01137\\\"\\n    title: \\\"Configuration Space Distance Fields for Manipulation Planning\\\"\\n    authors: \\\"Li, Chi, Razmjoo, Calinon\\\"\\n    year: 2024\\n    venue: RSS 2024\\n    arxiv: \\\"2406.01137\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\\\"\\n    relevance: \\\"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\\\"\\n\\n  - paper_id: \\\"2409.14955\\\"\\n    title: \\\"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.14955\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\\\"\\n    relevance: \\\"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\\\"\\n\\n  - paper_id: \\\"2511.21312\\\"\\n    title: \\\"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\\\"\\n    authors: \\\"Jacquet, Harms, Alexis\\\"\\n    year: 2025\\n    venue: IJRR 2025\\n    arxiv: \\\"2511.21312\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\\\"\\n    relevance: \\\"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\\\"\\n\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\n\\n  - paper_id: \\\"2307.15818\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al., Google DeepMind\\\"\\n    year: 2023\\n    venue: arXiv\\n    arxiv: \\\"2307.15818\\\"\\n    role: foundational\\n    category: vla-foundation\\n    summary: \\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\"\\n    relevance: \\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\"\\n\\n  - paper_id: \\\"2406.09246\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2406.09246\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\"\\n    relevance: \\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\"\\n\\n  - paper_id: \\\"2405.12213\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2405.12213\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\"\\n    relevance: \\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\"\\n\\n  # ===== 新增 P3: Benchmark =====\\n\\n  - title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv: \\\"2306.03310\\\"\\n    role: benchmark\\n    relevance: \\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\"\\n\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\n\\n  - title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\"\\n    venue: \\\"ICLR 2023\\\"\\n    arxiv: \\\"2210.02747\\\"\\n    role: method-component\\n    relevance: \\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\"\\n\\n  # ===== 新增 P5: Action Collapse / Mode Collapse =====\\n\\n  - paper_id: \\\"2505.11123\\\"\\n    title: \\\"Conditioning Matters: Training Diffusion Policies is Faster Than You Think\\\"\\n    authors: \\\"Dong et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2505.11123\\\"\\n    role: related-approach\\n    category: action-collapse\\n    summary: \\\"发现 diffusion policy 训练中的 'loss collapse'——observation 条件难区分时训练退化为建模 marginal action 分布而非 condition-specific 分布，提出 Cocos 通过条件依赖的源分布锚定解决。\\\"\\n    relevance: \\\"与 ColliForce 的 action collapse 机制类似：collision penalty 可导致策略忽略 task-relevant conditioning 而坍缩到 degenerate marginal（如静止不动），提供了 diffusion policy 中 loss collapse 的理论对照。\\\"\\n\\n  - paper_id: \\\"2303.04137\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: RSS 2023 / IJRR 2024\\n    arxiv: \\\"2303.04137\\\"\\n    role: foundational\\n    category: action-collapse\\n    summary: \\\"提出基于扩散模型的视觉运动策略，解决行为克隆中的 mode averaging 问题——标准回归策略在多模态演示上取均值产生不安全的中间轨迹。\\\"\\n    relevance: \\\"定义了 IL 中 mode averaging/collapse 的规范表述；ColliForce 的 collision penalty 可能在表达性策略架构中重新引入类似的模态坍缩，将动作分布推向单一 'freeze' 模态。\\\"\\n\\n  # ===== 新增 P6: Safe RL / Safe Imitation Learning =====\\n\\n  - paper_id: \\\"1705.10528\\\"\\n    title: \\\"Constrained Policy Optimization\\\"\\n    authors: \\\"Achiam et al.\\\"\\n    year: 2017\\n    venue: ICML 2017\\n    arxiv: \\\"1705.10528\\\"\\n    role: foundational\\n    category: safe-rl\\n    summary: \\\"训练时安全 RL 基础方法，在 trust-region 框架中约束策略更新满足 cost 限制，形式化为 constrained MDP。\\\"\\n    relevance: \\\"Safe RL 奠基工作；仅用标量 cost 信号，不含几何碰撞信息，不处理高维视觉-语言观测空间。ColliForce 的可微 SDF 辅助损失提供比 CPO 标量约束更丰富的连续几何安全信号。\\\"\\n\\n  - paper_id: \\\"2409.19190\\\"\\n    title: \\\"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution\\\"\\n    authors: \\\"Jung et al.\\\"\\n    year: 2025\\n    venue: ICRA 2025\\n    arxiv: \\\"2409.19190\\\"\\n    role: related-approach\\n    category: safe-rl\\n    summary: \\\"测试时安全方法：训练标准 IL 策略后用可达性分析安全过滤器在运行时覆盖不安全动作，实现 0% 碰撞率。\\\"\\n    relevance: \\\"策略本身不学安全，与 ColliForce 训练时 SDF 嵌入形成对比。解耦方式意味着过滤器频繁干预时可能降低任务性能，ColliForce 通过让策略原生碰撞感知来避免这一问题。\\\"\\n\\n  - paper_id: \\\"2503.17432\\\"\\n    title: \\\"TamedPUMA: Safe and Stable Imitation Learning with Geometric Fabrics\\\"\\n    authors: \\\"Bakker et al.\\\"\\n    year: 2025\\n    venue: L4DC 2025\\n    arxiv: \\\"2503.17432\\\"\\n    role: related-approach\\n    category: safe-rl\\n    summary: \\\"将学习的运动基元与 geometric fabrics 融合，在运行时强制碰撞回避和关节限制，需已知障碍物解析表示。\\\"\\n    relevance: \\\"运行时安全机制叠加在 IL 之上；需要运行时解析障碍物表示，ColliForce 在训练时嵌入 SDF 使策略泛化到新场景而无需运行时几何计算。\\\"\\n\", \"total_chars\": 13371, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "d3a34ff2-b4dd-4124-8bbe-669dda9600c1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\\\", \\\"content\\\": \\\"# ColliForce-VLA Literature Map\\\\n# Updated: 2026-05-25\\\\n\\\\npapers:\\\\n\\\\n  # ===== 已有论文 =====\\\\n\\\\n  - paper_id: \\\\\\\"2512.11891\\\\\\\"\\\\n    title: \\\\\\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\\\\\"\\\\n    authors: \\\\\\\"Hu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    one_line_summary: \\\\\\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2510.14836\\\\\\\"\\\\n    title: \\\\\\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    role: direct-competitor\\\\n    category: spatial-aware-vla\\\\n    one_line_summary: \\\\\\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2510.12276\\\\\\\"\\\\n    title: \\\\\\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: ICLR 2026\\\\n    role: method-component\\\\n    category: spatial-aware-vla\\\\n    one_line_summary: \\\\\\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2307.05973\\\\\\\"\\\\n    title: \\\\\\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Huang et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: CoRL 2023\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    one_line_summary: \\\\\\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2410.24164\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al., Physical Intelligence\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    role: backbone\\\\n    category: vla-foundation\\\\n    one_line_summary: \\\\\\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"1901.05103\\\\\\\"\\\\n    title: \\\\\\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\\\\\"\\\\n    authors: \\\\\\\"Park et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: CVPR 2019\\\\n    role: method-component\\\\n    category: sdf-representation\\\\n    one_line_summary: \\\\\\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2307.00533\\\\\\\"\\\\n    title: \\\\\\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: arXiv\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    one_line_summary: \\\\\\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\\\\\"\\\\n\\\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\\\n\\\\n  - paper_id: \\\\\\\"2503.03480\\\\\\\"\\\\n    title: \\\\\\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: NeurIPS 2025 (Spotlight)\\\\n    arxiv: \\\\\\\"2503.03480\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\\\\\"\\\\n    relevance: \\\\\\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2407.00451\\\\\\\"\\\\n    title: \\\\\\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: ICRA 2025\\\\n    arxiv: \\\\\\\"2407.00451\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\\\\\"\\\\n    relevance: \\\\\\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2511.22773\\\\\\\"\\\\n    title: \\\\\\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2511.22773\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\\\\\"\\\\n    relevance: \\\\\\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2409.08233\\\\\\\"\\\\n    title: \\\\\\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\\\\\"\\\\n    authors: \\\\\\\"Spalter et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2409.08233\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\\\\\"\\\\n    relevance: \\\\\\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\\\\\"\\\\n\\\\n  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\\\\n\\\\n  - paper_id: \\\\\\\"2601.21712\\\\\\\"\\\\n    title: \\\\\\\"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\\\\\\\"\\\\n    authors: \\\\\\\"Zhai et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2601.21712\\\\\\\"\\\\n    role: direct-competitor\\\\n    category: collision-aware-vla\\\\n    summary: \\\\\\\"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\\\\\\\"\\\\n    relevance: \\\\\\\"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2404.02284\\\\\\\"\\\\n    title: \\\\\\\"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\\\\\\\"\\\\n    authors: \\\\\\\"Dastider et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: IROS 2024\\\\n    arxiv: \\\\\\\"2404.02284\\\\\\\"\\\\n    role: related-approach\\\\n    category: collision-aware-manipulation\\\\n    summary: \\\\\\\"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\\\\\\\"\\\\n    relevance: \\\\\\\"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2512.11908\\\\\\\"\\\\n    title: \\\\\\\"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2512.11908\\\\\\\"\\\\n    role: survey\\\\n    category: collision-aware-manipulation\\\\n    summary: \\\\\\\"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\\\\\\\"\\\\n    relevance: \\\\\\\"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\\\\\\\"\\\\n\\\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\\\n\\\\n  - paper_id: \\\\\\\"2204.02296\\\\\\\"\\\\n    title: \\\\\\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\\\\\"\\\\n    authors: \\\\\\\"Ortiz et al.\\\\\\\"\\\\n    year: 2022\\\\n    venue: RSS 2022\\\\n    arxiv: \\\\\\\"2204.02296\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\\\\\"\\\\n    relevance: \\\\\\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2305.10534\\\\\\\"\\\\n    title: \\\\\\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\\\\\"\\\\n    authors: \\\\\\\"Vasilopoulos et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: IROS 2023\\\\n    arxiv: \\\\\\\"2305.10534\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\\\\\"\\\\n    relevance: \\\\\\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2102.07413\\\\\\\"\\\\n    title: \\\\\\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Zhi et al.\\\\\\\"\\\\n    year: 2021\\\\n    venue: IEEE T-RO\\\\n    arxiv: \\\\\\\"2102.07413\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\\\\\"\\\\n    relevance: \\\\\\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\\\\\"\\\\n\\\\n  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====\\\\n\\\\n  - paper_id: \\\\\\\"2406.01137\\\\\\\"\\\\n    title: \\\\\\\"Configuration Space Distance Fields for Manipulation Planning\\\\\\\"\\\\n    authors: \\\\\\\"Li, Chi, Razmjoo, Calinon\\\\\\\"\\\\n    year: 2024\\\\n    venue: RSS 2024\\\\n    arxiv: \\\\\\\"2406.01137\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\\\\\\\"\\\\n    relevance: \\\\\\\"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2409.14955\\\\\\\"\\\\n    title: \\\\\\\"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\\\\\\\"\\\\n    authors: \\\\\\\"Zhu et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2409.14955\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\\\\\\\"\\\\n    relevance: \\\\\\\"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2511.21312\\\\\\\"\\\\n    title: \\\\\\\"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\\\\\\\"\\\\n    authors: \\\\\\\"Jacquet, Harms, Alexis\\\\\\\"\\\\n    year: 2025\\\\n    venue: IJRR 2025\\\\n    arxiv: \\\\\\\"2511.21312\\\\\\\"\\\\n    role: method-component\\\\n    category: sdf-robotics\\\\n    summary: \\\\\\\"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\\\\\\\"\\\\n    relevance: \\\\\\\"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\\\\\\\"\\\\n\\\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\\\n\\\\n  - paper_id: \\\\\\\"2307.15818\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al., Google DeepMind\\\\\\\"\\\\n    year: 2023\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2307.15818\\\\\\\"\\\\n    role: foundational\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\\\\\"\\\\n    relevance: \\\\\\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2406.09246\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2406.09246\\\\\\\"\\\\n    role: benchmark-source\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\\\\\"\\\\n    relevance: \\\\\\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2405.12213\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Octo Model Team\\\\\\\"\\\\n    year: 2024\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2405.12213\\\\\\\"\\\\n    role: benchmark-source\\\\n    category: vla-foundation\\\\n    summary: \\\\\\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\\\\\"\\\\n    relevance: \\\\\\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\\\\\"\\\\n\\\\n  # ===== 新增 P3: Benchmark =====\\\\n\\\\n  - title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    arxiv: \\\\\\\"2306.03310\\\\\\\"\\\\n    role: benchmark\\\\n    relevance: \\\\\\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\\\\\"\\\\n\\\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\\\n\\\\n  - title: \\\\\\\"Flow Matching for Generative Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    arxiv: \\\\\\\"2210.02747\\\\\\\"\\\\n    role: method-component\\\\n    relevance: \\\\\\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\\\\\"\\\\n\\\\n  # ===== 新增 P5: Action Collapse / Mode Collapse =====\\\\n\\\\n  - paper_id: \\\\\\\"2505.11123\\\\\\\"\\\\n    title: \\\\\\\"Conditioning Matters: Training Diffusion Policies is Faster Than You Think\\\\\\\"\\\\n    authors: \\\\\\\"Dong et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: arXiv\\\\n    arxiv: \\\\\\\"2505.11123\\\\\\\"\\\\n    role: related-approach\\\\n    category: action-collapse\\\\n    summary: \\\\\\\"发现 diffusion policy 训练中的 'loss collapse'——observation 条件难区分时训练退化为建模 marginal action 分布而非 condition-specific 分布，提出 Cocos 通过条件依赖的源分布锚定解决。\\\\\\\"\\\\n    relevance: \\\\\\\"与 ColliForce 的 action collapse 机制类似：collision penalty 可导致策略忽略 task-relevant conditioning 而坍缩到 degenerate marginal（如静止不动），提供了 diffusion policy 中 loss collapse 的理论对照。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2303.04137\\\\\\\"\\\\n    title: \\\\\\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Chi et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: RSS 2023 / IJRR 2024\\\\n    arxiv: \\\\\\\"2303.04137\\\\\\\"\\\\n    role: foundational\\\\n    category: action-collapse\\\\n    summary: \\\\\\\"提出基于扩散模型的视觉运动策略，解决行为克隆中的 mode averaging 问题——标准回归策略在多模态演示上取均值产生不安全的中间轨迹。\\\\\\\"\\\\n    relevance: \\\\\\\"定义了 IL 中 mode averaging/collapse 的规范表述；ColliForce 的 collision penalty 可能在表达性策略架构中重新引入类似的模态坍缩，将动作分布推向单一 'freeze' 模态。\\\\\\\"\\\\n\\\\n  # ===== 新增 P6: Safe RL / Safe Imitation Learning =====\\\\n\\\\n  - paper_id: \\\\\\\"1705.10528\\\\\\\"\\\\n    title: \\\\\\\"Constrained Policy Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Achiam et al.\\\\\\\"\\\\n    year: 2017\\\\n    venue: ICML 2017\\\\n    arxiv: \\\\\\\"1705.10528\\\\\\\"\\\\n    role: foundational\\\\n    category: safe-rl\\\\n    summary: \\\\\\\"训练时安全 RL 基础方法，在 trust-region 框架中约束策略更新满足 cost 限制，形式化为 constrained MDP。\\\\\\\"\\\\n    relevance: \\\\\\\"Safe RL 奠基工作；仅用标量 cost 信号，不含几何碰撞信息，不处理高维视觉-语言观测空间。ColliForce 的可微 SDF 辅助损失提供比 CPO 标量约束更丰富的连续几何安全信号。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2409.19190\\\\\\\"\\\\n    title: \\\\\\\"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution\\\\\\\"\\\\n    authors: \\\\\\\"Jung et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: ICRA 2025\\\\n    arxiv: \\\\\\\"2409.19190\\\\\\\"\\\\n    role: related-approach\\\\n    category: safe-rl\\\\n    summary: \\\\\\\"测试时安全方法：训练标准 IL 策略后用可达性分析安全过滤器在运行时覆盖不安全动作，实现 0% 碰撞率。\\\\\\\"\\\\n    relevance: \\\\\\\"策略本身不学安全，与 ColliForce 训练时 SDF 嵌入形成对比。解耦方式意味着过滤器频繁干预时可能降低任务性能，ColliForce 通过让策略原生碰撞感知来避免这一问题。\\\\\\\"\\\\n\\\\n  - paper_id: \\\\\\\"2503.17432\\\\\\\"\\\\n    title: \\\\\\\"TamedPUMA: Safe and Stable Imitation Learning with Geometric Fabrics\\\\\\\"\\\\n    authors: \\\\\\\"Bakker et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: L4DC 2025\\\\n    arxiv: \\\\\\\"2503.17432\\\\\\\"\\\\n    role: related-approach\\\\n    category: safe-rl\\\\n    summary: \\\\\\\"将学习的运动基元与 geometric fabrics 融合，在运行时强制碰撞回避和关节限制，需已知障碍物解析表示。\\\\\\\"\\\\n    relevance: \\\\\\\"运行时安全机制叠加在 IL 之上；需要运行时解析障碍物表示，ColliForce 在训练时嵌入 SDF 使策略泛化到新场景而无需运行时几何计算。\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 13371, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/literature_map.yaml\", \"content\": \"# ColliForce-VLA Literature Map\\n# Updated: 2026-05-25\\n\\npapers:\\n\\n  # ===== 已有论文 =====\\n\\n  - paper_id: \\\"2512.11891\\\"\\n    title: \\\"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer\\\"\\n    authors: \\\"Hu et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    one_line_summary: \\\"AEGIS/SafeLIBERO — 用 CBF 安全约束层实现 VLA 碰撞回避，是外挂式安全机制，不改变 VLA 内部空间表征；ColliForce 的核心对比对象。\\\"\\n\\n  - paper_id: \\\"2510.14836\\\"\\n    title: \\\"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    role: direct-competitor\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"用量化深度预测作为 VLA 辅助监督增强空间推理；与 ColliForce 的 SDF 辅助损失思路类似但用深度而非 SDF，且在 camera frame 而非 workspace frame。\\\"\\n\\n  - paper_id: \\\"2510.12276\\\"\\n    title: \\\"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2025\\n    venue: ICLR 2026\\n    role: method-component\\n    category: spatial-aware-vla\\n    one_line_summary: \\\"隐式对齐 VLA 中间层视觉嵌入与 3D 基础模型几何表征，证明隐式 3D 对齐对 VLA 有效；ColliForce 将对齐目标从通用 3D 几何特化为 SDF/occupancy field。\\\"\\n\\n  - paper_id: \\\"2307.05973\\\"\\n    title: \\\"VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: CoRL 2023\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 LLM 生成 3D 体素 value maps（含 avoidance maps）引导机器人操作规划；启发了 ColliForce 用 3D 空间场引导动作生成的思路。\\\"\\n\\n  - paper_id: \\\"2410.24164\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al., Physical Intelligence\\\"\\n    year: 2024\\n    venue: arXiv\\n    role: backbone\\n    category: vla-foundation\\n    one_line_summary: \\\"基于 PaliGemma VLM + flow matching 的通用 VLA 基座模型；ColliForce 的基座架构，在其上添加 SDF 辅助监督分支。\\\"\\n\\n  - paper_id: \\\"1901.05103\\\"\\n    title: \\\"DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation\\\"\\n    authors: \\\"Park et al.\\\"\\n    year: 2019\\n    venue: CVPR 2019\\n    role: method-component\\n    category: sdf-representation\\n    one_line_summary: \\\"开创性地用深度网络学习连续 SDF 表示；ColliForce 中 workspace SDF 的表征方法论基础。\\\"\\n\\n  - paper_id: \\\"2307.00533\\\"\\n    title: \\\"Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: arXiv\\n    role: method-component\\n    category: sdf-robotics\\n    one_line_summary: \\\"用 Bernstein 多项式编码机器人连杆 SDF 并集成到优化问题中实现可微碰撞检测；验证了 SDF 在机器人碰撞检测中的可行性。\\\"\\n\\n  # ===== 新增 P0: 直接竞品 — 碰撞感知操纵 / Safe Manipulation =====\\n\\n  - paper_id: \\\"2503.03480\\\"\\n    title: \\\"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: NeurIPS 2025 (Spotlight)\\n    arxiv: \\\"2503.03480\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"用 CMDP 范式对 VLA 策略施加安全约束，通过 safe RL 优化减少 83.58% 安全违规成本。\\\"\\n    relevance: \\\"最直接竞品之一：同样关注 VLA 安全性，但走 constrained RL 路线（外部约束优化），ColliForce 走内部空间表征增强路线（SDF 辅助监督），方法论互补。\\\"\\n\\n  - paper_id: \\\"2407.00451\\\"\\n    title: \\\"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2024\\n    venue: ICRA 2025\\n    arxiv: \\\"2407.00451\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 3D 点云上训练 diffusion policy 预测末端轨迹，推理时通过 cost-guided denoising 实现 training-free 碰撞回避。\\\"\\n    relevance: \\\"碰撞回避在推理阶段通过 cost optimization 注入；ColliForce 在训练阶段通过 SDF 辅助损失嵌入碰撞感知，设计哲学不同。\\\"\\n\\n  - paper_id: \\\"2511.22773\\\"\\n    title: \\\"CAPE: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance\\\"\\n    authors: \\\"Yang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2511.22773\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"通过 context-aware prior 和 prior-seeded iterative guided refinement 扩展轨迹分布模态，cluttered 场景碰撞回避提升 26-80%。\\\"\\n    relevance: \\\"推理阶段碰撞回避方法，与 ColliForce 训练阶段 SDF 注入形成对比；可讨论 train-time vs. test-time 安全注入的 trade-off。\\\"\\n\\n  - paper_id: \\\"2409.08233\\\"\\n    title: \\\"Towards Online Safety Corrections for Robotic Manipulation Policies\\\"\\n    authors: \\\"Spalter et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.08233\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"iKinQP-RL：用逆运动学 QP 控制器在运行时修正 RL 策略动作，完全消除与未见障碍物的碰撞。\\\"\\n    relevance: \\\"运行时安全修正层，类似 VLSA 的外挂思路；ColliForce 不需额外安全层，通过 SDF 辅助监督让策略自身学会碰撞感知。\\\"\\n\\n  # ===== 新增 P0b: 碰撞感知操纵补充 (2024-2026) =====\\n\\n  - paper_id: \\\"2601.21712\\\"\\n    title: \\\"CoFreeVLA: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation\\\"\\n    authors: \\\"Zhai et al.\\\"\\n    year: 2026\\n    venue: arXiv\\n    arxiv: \\\"2601.21712\\\"\\n    role: direct-competitor\\n    category: collision-aware-vla\\n    summary: \\\"在 VLA 策略上外挂短时域自碰撞风险估计器，预测碰撞概率并门控危险动作，通过 risk-guided 调整恢复安全状态。在 PiPER 双臂平台 5 个任务上减少自碰撞并提升成功率。\\\"\\n    relevance: \\\"VLA + 碰撞安全的最新工作；采用外部风险估计器（post-hoc 过滤）路线，与 ColliForce 训练时 SDF 嵌入的内在路线形成对比。可讨论 internal representation vs. external filter 的 trade-off。\\\"\\n\\n  - paper_id: \\\"2404.02284\\\"\\n    title: \\\"APEX: Ambidextrous Dual-Arm Robotic Manipulation Using Collision-Free Generative Diffusion Models\\\"\\n    authors: \\\"Dastider et al.\\\"\\n    year: 2024\\n    venue: IROS 2024\\n    arxiv: \\\"2404.02284\\\"\\n    role: related-approach\\n    category: collision-aware-manipulation\\n    summary: \\\"用潜在扩散模型生成双臂操作轨迹，通过 classifier-guidance 技术集成障碍物信息保证轨迹无碰撞。在双臂硬件平台上超越传统运动规划算法。\\\"\\n    relevance: \\\"Test-time classifier-guidance 碰撞回避，与 Lan-o3dp/CAPE 同属推理阶段安全注入方法族；ColliForce 在训练阶段通过 SDF 辅助损失嵌入，不需推理时额外计算。\\\"\\n\\n  - paper_id: \\\"2512.11908\\\"\\n    title: \\\"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2512.11908\\\"\\n    role: survey\\n    category: collision-aware-manipulation\\n    summary: \\\"系统综述安全接触任务的学习方法，覆盖 constrained RL、risk-sensitive optimization、CBF、MPC safety shields，并延伸到 foundation model 时代的安全挑战。\\\"\\n    relevance: \\\"Related Work 定位参考：ColliForce 属于该综述分类中 'training-time geometric supervision' 类别，与 constrained RL (SafeVLA) 和 runtime shields (VLSA/iKinQP) 构成三条路线。\\\"\\n\\n  # ===== 新增 P1: SDF/距离场在机器人学中的应用 =====\\n\\n  - paper_id: \\\"2204.02296\\\"\\n    title: \\\"iSDF: Real-Time Neural Signed Distance Fields for Robot Perception\\\"\\n    authors: \\\"Ortiz et al.\\\"\\n    year: 2022\\n    venue: RSS 2022\\n    arxiv: \\\"2204.02296\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"从流式深度图像持续学习神经 SDF，将 3D 坐标映射为有符号距离值，实现实时机器人场景感知。\\\"\\n    relevance: \\\"验证了神经 SDF 可实时构建用于机器人感知；ColliForce 的 workspace SDF ground truth 生成和在线推理可参考其方法。\\\"\\n\\n  - paper_id: \\\"2305.10534\\\"\\n    title: \\\"RAMP: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions\\\"\\n    authors: \\\"Vasilopoulos et al.\\\"\\n    year: 2023\\n    venue: IROS 2023\\n    arxiv: \\\"2305.10534\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"结合 MPPI 控制器和局部向量场控制器，用 SDF 做碰撞检测和反应式避障的层次化运动规划。\\\"\\n    relevance: \\\"展示 SDF 在 reactive manipulation planning 中的有效性；ColliForce 将 SDF 从规划模块提升到学习模块，让策略网络直接编码距离场信息。\\\"\\n\\n  - paper_id: \\\"2102.07413\\\"\\n    title: \\\"DiffCo: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization\\\"\\n    authors: \\\"Zhi et al.\\\"\\n    year: 2021\\n    venue: IEEE T-RO\\n    arxiv: \\\"2102.07413\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"全自动可微的非参数碰撞检测模型，在线计算碰撞边界并通过反向传播提供鲁棒梯度用于轨迹优化。\\\"\\n    relevance: \\\"可微碰撞检测关键工作，证明碰撞信息可通过梯度传播融入优化；ColliForce 的 SDF 辅助损失本质也是让碰撞信息参与梯度反传。\\\"\\n\\n  # ===== 新增 P1b: SDF/距离场在机器人学补充 (2024-2025) =====\\n\\n  - paper_id: \\\"2406.01137\\\"\\n    title: \\\"Configuration Space Distance Fields for Manipulation Planning\\\"\\n    authors: \\\"Li, Chi, Razmjoo, Calinon\\\"\\n    year: 2024\\n    venue: RSS 2024\\n    arxiv: \\\"2406.01137\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"将 SDF 从任务空间扩展到机器人构型空间（C-space），直接估计到达接触/碰撞所需的最小关节运动量，并用于操作规划优化。\\\"\\n    relevance: \\\"直接回应 ColliForce 的 EE-only SDF 局限：CDF 在 C-space 工作天然覆盖全身碰撞，Related Work 中可作为 full-body SDF 方案的代表，讨论 task-space SDF vs. C-space SDF 的优劣。\\\"\\n\\n  - paper_id: \\\"2409.14955\\\"\\n    title: \\\"Efficient Collision Detection Framework for Enhancing Collision-Free Robot Motion\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2409.14955\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"通过正运动学分解机器人全身 SDF，用多个轻量并行网络近似各连杆 SDF，集成 SVM 自碰撞检测模块（SDF-SC），保持可微性用于轨迹优化。\\\"\\n    relevance: \\\"全身 SDF 分解方案，与 Liu et al. (2023) Bernstein 多项式方法互补；ColliForce 目前仅用 EE SDF，该工作展示了扩展到全身 SDF 的工程可行性。\\\"\\n\\n  - paper_id: \\\"2511.21312\\\"\\n    title: \\\"Neural NMPC through Signed Distance Field Encoding for Collision Avoidance\\\"\\n    authors: \\\"Jacquet, Harms, Alexis\\\"\\n    year: 2025\\n    venue: IJRR 2025\\n    arxiv: \\\"2511.21312\\\"\\n    role: method-component\\n    category: sdf-robotics\\n    summary: \\\"用卷积编码器将深度图像压缩为潜向量，MLP 近似对应空间 SDF，作为 NMPC 的显式位置约束实现无地图碰撞回避。森林环境真机验证。\\\"\\n    relevance: \\\"展示 SDF 作为控制约束的端到端集成路径（感知→SDF→控制）；ColliForce 将 SDF 集成到学习策略（感知→SDF→policy loss），两者互为对照。\\\"\\n\\n  # ===== 新增 P2: VLA 基座模型系列 =====\\n\\n  - paper_id: \\\"2307.15818\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al., Google DeepMind\\\"\\n    year: 2023\\n    venue: arXiv\\n    arxiv: \\\"2307.15818\\\"\\n    role: foundational\\n    category: vla-foundation\\n    summary: \\\"将动作表示为文本 token，在视觉-语言任务和机器人轨迹数据上联合微调 VLM，实现网络知识到机器人控制的迁移。\\\"\\n    relevance: \\\"VLA 范式奠基工作，确立 VLM→VLA 微调范式；ColliForce 在此范式基础上增加 SDF 辅助分支。\\\"\\n\\n  - paper_id: \\\"2406.09246\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2406.09246\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"7B 参数开源 VLA，基于 Llama 2 + DINOv2/SigLIP，970k 真实演示训练，29 任务上超越 RT-2-X 16.5%。\\\"\\n    relevance: \\\"主要 VLA baseline；ColliForce 可在其上验证 SDF 辅助监督的通用性。\\\"\\n\\n  - paper_id: \\\"2405.12213\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Octo Model Team\\\"\\n    year: 2024\\n    venue: arXiv\\n    arxiv: \\\"2405.12213\\\"\\n    role: benchmark-source\\n    category: vla-foundation\\n    summary: \\\"基于 Transformer 的通用策略，Open X-Embodiment 800k 轨迹训练，支持多传感器多动作空间，消费级 GPU 可快速微调。\\\"\\n    relevance: \\\"轻量级 VLA baseline；ColliForce 的 SDF 辅助分支可测试在小模型上的效果。\\\"\\n\\n  # ===== 新增 P3: Benchmark =====\\n\\n  - title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    arxiv: \\\"2306.03310\\\"\\n    role: benchmark\\n    relevance: \\\"SafeLIBERO benchmark 的基础；定义了 Spatial/Goal/Object/Long 四个 suite 的任务结构和评估协议\\\"\\n\\n  # ===== 新增 P4: 生成式建模基础方法 =====\\n\\n  - title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, Matt Le\\\"\\n    venue: \\\"ICLR 2023\\\"\\n    arxiv: \\\"2210.02747\\\"\\n    role: method-component\\n    relevance: \\\"π0 base model 使用的 flow matching 训练范式；ColliForce gradient-guided refinement 基于 flow matching 的 ODE solver 进行梯度注入\\\"\\n\\n  # ===== 新增 P5: Action Collapse / Mode Collapse =====\\n\\n  - paper_id: \\\"2505.11123\\\"\\n    title: \\\"Conditioning Matters: Training Diffusion Policies is Faster Than You Think\\\"\\n    authors: \\\"Dong et al.\\\"\\n    year: 2025\\n    venue: arXiv\\n    arxiv: \\\"2505.11123\\\"\\n    role: related-approach\\n    category: action-collapse\\n    summary: \\\"发现 diffusion policy 训练中的 'loss collapse'——observation 条件难区分时训练退化为建模 marginal action 分布而非 condition-specific 分布，提出 Cocos 通过条件依赖的源分布锚定解决。\\\"\\n    relevance: \\\"与 ColliForce 的 action collapse 机制类似：collision penalty 可导致策略忽略 task-relevant conditioning 而坍缩到 degenerate marginal（如静止不动），提供了 diffusion policy 中 loss collapse 的理论对照。\\\"\\n\\n  - paper_id: \\\"2303.04137\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: RSS 2023 / IJRR 2024\\n    arxiv: \\\"2303.04137\\\"\\n    role: foundational\\n    category: action-collapse\\n    summary: \\\"提出基于扩散模型的视觉运动策略，解决行为克隆中的 mode averaging 问题——标准回归策略在多模态演示上取均值产生不安全的中间轨迹。\\\"\\n    relevance: \\\"定义了 IL 中 mode averaging/collapse 的规范表述；ColliForce 的 collision penalty 可能在表达性策略架构中重新引入类似的模态坍缩，将动作分布推向单一 'freeze' 模态。\\\"\\n\\n  # ===== 新增 P6: Safe RL / Safe Imitation Learning =====\\n\\n  - paper_id: \\\"1705.10528\\\"\\n    title: \\\"Constrained Policy Optimization\\\"\\n    authors: \\\"Achiam et al.\\\"\\n    year: 2017\\n    venue: ICML 2017\\n    arxiv: \\\"1705.10528\\\"\\n    role: foundational\\n    category: safe-rl\\n    summary: \\\"训练时安全 RL 基础方法，在 trust-region 框架中约束策略更新满足 cost 限制，形式化为 constrained MDP。\\\"\\n    relevance: \\\"Safe RL 奠基工作；仅用标量 cost 信号，不含几何碰撞信息，不处理高维视觉-语言观测空间。ColliForce 的可微 SDF 辅助损失提供比 CPO 标量约束更丰富的连续几何安全信号。\\\"\\n\\n  - paper_id: \\\"2409.19190\\\"\\n    title: \\\"RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution\\\"\\n    authors: \\\"Jung et al.\\\"\\n    year: 2025\\n    venue: ICRA 2025\\n    arxiv: \\\"2409.19190\\\"\\n    role: related-approach\\n    category: safe-rl\\n    summary: \\\"测试时安全方法：训练标准 IL 策略后用可达性分析安全过滤器在运行时覆盖不安全动作，实现 0% 碰撞率。\\\"\\n    relevance: \\\"策略本身不学安全，与 ColliForce 训练时 SDF 嵌入形成对比。解耦方式意味着过滤器频繁干预时可能降低任务性能，ColliForce 通过让策略原生碰撞感知来避免这一问题。\\\"\\n\\n  - paper_id: \\\"2503.17432\\\"\\n    title: \\\"TamedPUMA: Safe and Stable Imitation Learning with Geometric Fabrics\\\"\\n    authors: \\\"Bakker et al.\\\"\\n    year: 2025\\n    venue: L4DC 2025\\n    arxiv: \\\"2503.17432\\\"\\n    role: related-approach\\n    category: safe-rl\\n    summary: \\\"将学习的运动基元与 geometric fabrics 融合，在运行时强制碰撞回避和关节限制，需已知障碍物解析表示。\\\"\\n    relevance: \\\"运行时安全机制叠加在 IL 之上；需要运行时解析障碍物表示，ColliForce 在训练时嵌入 SDF 使策略泛化到新场景而无需运行时几何计算。\\\"\\n\", \"total_chars\": 13371, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01W4duRNyc2gg1whNjm7gXRo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "a785b505-e645-4468-8f2d-4fb142a604fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJtykW4qFtit965JfQgyfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6151,
      "cache_read_input_tokens": 24022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6151
      },
      "output_tokens": 20,
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

_source line 17 · 2026-05-26T16:12:03.853Z_

<details><summary>↩ Tool result · `toolu_01W4duRNyc2gg1whNjm7gXRo`</summary>

```text
1	% The Safety Illusion — References
2	% Analysis paper on fake safety in VLA collision avoidance evaluation
3	% Generated: 2026-05-24
4	
5	% ===== VLA Foundation Models =====
6	
7	@article{black2024pi0,
8	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
9	  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},
10	  journal={arXiv preprint arXiv:2410.24164},
11	  year={2024}
12	}
13	
14	@inproceedings{kim2024openvla,
15	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
16	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},
17	  booktitle={Conference on Robot Learning (CoRL)},
18	  year={2024}
19	}
20	
21	@inproceedings{brohan2023rt2,
22	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
23	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
24	  booktitle={Conference on Robot Learning (CoRL)},
25	  year={2023}
26	}
27	
28	% ===== Collision-Aware VLA Methods =====
29	
30	@article{hu2025vlsa,
31	  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
32	  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},
33	  journal={arXiv preprint arXiv:2512.11891},
34	  year={2025}
35	}
36	
37	@inproceedings{zhang2025safevla,
38	  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
39	  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},
40	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
41	  year={2025}
42	}
43	
44	@article{cofreeevla2026,
45	  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},
46	  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},
47	  journal={arXiv preprint arXiv:2601.21712},
48	  year={2026}
49	}
50	
51	@article{spalter2024ikinqp,
52	  title={Towards Online Safety Corrections for Robotic Manipulation Policies},
53	  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},
54	  journal={arXiv preprint arXiv:2409.08233},
55	  year={2024}
56	}
57	
58	@inproceedings{li2024langguided,
59	  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},
60	  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},
61	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
62	  year={2025}
63	}
64	
65	@article{yang2025cape,
66	  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},
67	  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},
68	  journal={arXiv preprint arXiv:2511.22773},
69	  year={2025}
70	}
71	
72	% ===== SDF in Robotics =====
73	
74	@inproceedings{park2019deepsdf,
75	  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},
76	  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},
77	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
78	  year={2019}
79	}
80	
81	@inproceedings{ortiz2022isdf,
82	  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},
83	  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\"o}fer, Michael and Mukadam, Mustafa},
84	  booktitle={Robotics: Science and Systems (RSS)},
85	  year={2022}
86	}
87	
88	@article{zhi2021diffco,
89	  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},
90	  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},
91	  journal={IEEE Transactions on Robotics},
92	  volume={38},
93	  number={5},
94	  pages={2668--2685},
95	  year={2022}
96	}
97	
98	@inproceedings{huang2023voxposer,
99	  title={{VoxPoser}: Composable {3D} Value Maps for Robotic Manipulation with Language Models},
100	  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},
101	  booktitle={Conference on Robot Learning (CoRL)},
102	  year={2023}
103	}
104	
105	% ===== Benchmarks and Training =====
106	
107	@inproceedings{liu2023libero,
108	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
109	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
110	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
111	  year={2023}
112	}
113	
114	@inproceedings{lipman2023flow,
115	  title={Flow Matching for Generative Modeling},
116	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
117	  booktitle={International Conference on Learning Representations (ICLR)},
118	  year={2023}
119	}
120	
121	% ===== Evaluation Reliability =====
122	
123	@inproceedings{gururangan2018annotation,
124	  title={Annotation Artifacts in Natural Language Inference Data},
125	  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},
126	  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
127	  year={2018}
128	}
129	
130	@inproceedings{karwowski2024goodhart,
131	  title={Goodhart's Law in Reinforcement Learning},
132	  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},
133	  booktitle={International Conference on Learning Representations (ICLR)},
134	  year={2024}
135	}
136	
137	% ===== Diffusion Policy =====
138	
139	@inproceedings{chi2023diffusionpolicy,
140	  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
141	  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
142	  booktitle={Robotics: Science and Systems (RSS)},
143	  year={2023}
144	}
145	
146	% ===== SDF in Robotics (additional) =====
147	
148	@inproceedings{vasilopoulos2023ramp,
149	  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},
150	  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},
151	  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
152	  year={2023}
153	}
154	
155	@article{chen2026cssdfnet,
156	  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},
157	  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},
158	  journal={arXiv preprint arXiv:2603.18669},
159	  year={2026}
160	}
161	
162	@article{jacquet2025neuralnmpc,
163	  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},
164	  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},
165	  journal={The International Journal of Robotics Research},
166	  year={2025}
167	}
168	
169	@article{chen2025samp,
170	  title={{SAMP}: Spatial Anchor-based Motion Policy for Collision-Aware Robotic Manipulators},
171	  author={Chen, Kai and Bi, Zhihai and Zhao, Guoyang and Zheng, Chunxin and Li, Yulin and Zhao, Hang and Ma, Jun},
172	  journal={arXiv preprint arXiv:2509.11185},
173	  year={2025}
174	}
175	
176	@inproceedings{ruan2025profrobot,
177	  title={Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions},
178	  author={Ruan, Quanyuan and Lei, Jiabao and Yuan, Wenhao and Zhang, Yanglin and Lu, Dekun and Liu, Guiliang and Jia, Kui},
179	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
180	  year={2025}
181	}
182	
183	% ===== 3D-Aware VLA Methods =====
184	
185	@article{depthvla2025,
186	  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},
187	  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},
188	  journal={arXiv preprint arXiv:2510.13375},
189	  year={2025}
190	}
191	
192	@article{li2025qdepth,
193	  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},
194	  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},
195	  journal={arXiv preprint arXiv:2510.14836},
196	  year={2025}
197	}
198	
199	@article{li2025spatialforcing,
200	  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},
201	  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},
202	  journal={arXiv preprint arXiv:2510.12276},
203	  year={2025}
204	}
205	
206	@article{3dcavla2025,
207	  title={{3D CAVLA}: Leveraging Depth and {3D} Context to Generalize Vision Language Action Models for Unseen Tasks},
208	  author={Bhat, Vineet and Lan, Yu-Hsiang and Krishnamurthy, Prashanth and Karri, Ramesh and Khorrami, Farshad},
209	  journal={arXiv preprint arXiv:2505.05800},
210	  year={2025}
211	}
212	
213	@article{geoaware2025,
214	  title={{GeoAware-VLA}: Implicit Geometry Aware Vision-Language-Action Model},
215	  author={Abouzeid, Ali and Mansour, Malak and Sun, Qinbo and Sun, Zezhou and Song, Dezhen},
216	  journal={arXiv preprint arXiv:2509.14117},
217	  year={2025}
218	}
219	
220	@inproceedings{spatialvla2025,
221	  title={{SpatialVLA}: Exploring Spatial Representations for Visual-Language-Action Model},
222	  author={Qu, Delin and Song, Haoming and Chen, Qizhi and Yao, Yuanqi and Ye, Xinyi and Gu, Jiayuan and Wang, Zhigang and Ding, Yan and Zhao, Bin and Wang, Dong and Li, Xuelong},
223	  booktitle={Robotics: Science and Systems (RSS)},
224	  year={2025}
225	}
226	
227	@article{gstvla2026,
228	  title={{GST-VLA}: Structured Gaussian Spatial Tokens for {3D} Depth-Aware Vision-Language-Action Models},
229	  author={Sarowar, Md Selim and Tariq, Omer and Kim, Sungho},
230	  journal={arXiv preprint arXiv:2603.09079},
231	  year={2026}
232	}
233	
234	@article{stemvla2026,
235	  title={{StemVLA}: An Open-Source Vision-Language-Action Model with Future {3D} Spatial Geometry Knowledge and {4D} Historical Representation},
236	  author={Xiao, Jiasong and She, Yutao and Li, Kai and Sha, Yuyang and Cheng, Ziang and Tong, Ziang},
237	  journal={arXiv preprint arXiv:2602.23721},
238	  year={2026}
239	}
240	
241	@article{stvla2026,
242	  title={{ST-VLA}: Enabling {4D}-Aware Spatiotemporal Understanding for General Robot Manipulation},
243	  author={Wu, You and Chen, Zixuan and Ou, Cunxu and Wang, Wenxuan and Huang, Wenbo and Cao, Lin and Chen, Yangtao and Qiu, Weichao and Quan, Xingyue and Shi, Jieqi and Huo, Jing and Gao, Yang},
244	  journal={arXiv preprint arXiv:2603.13788},
245	  year={2026}
246	}
247	
248	@article{evo02025,
249	  title={{Evo-0}: Vision-Language-Action Model with Implicit Spatial Understanding},
250	  author={Lin, Tao and Li, Gen and Zhong, Yilei and Zou, Yanwen and Du, Yuxin and Liu, Jiting and Gu, Encheng and Zhao, Bo},
251	  journal={arXiv preprint arXiv:2507.00416},
252	  year={2025}
253	}
254	
255	@article{savla2026,
256	  title={{SA-VLA}: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning},
257	  author={Pan, Xu and Wan, Zhenglin and Yu, Xingrui and Zheng, Xianwei and Ke, Youkai and Sun, Ming and Wang, Rui and Wang, Ziwei and Tsang, Ivor},
258	  journal={arXiv preprint arXiv:2602.00743},
259	  year={2026}
260	}
261	
262	@article{augvla3d2026,
263	  title={{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},
264	  author={Rao, Zhifeng and Chen, Wenlong and Xie, Lei and Hua, Xia and Yin, Dongfu and Tian, Zhen and Yu, F. Richard},
265	  journal={arXiv preprint arXiv:2602.10698},
266	  year={2026}
267	}
268	
269	@article{evodepth2026,
270	  title={{Evo-Depth}: A Lightweight Depth-Enhanced Vision-Language-Action Model},
271	  author={Lin, Tao and Du, Yuxin and Liu, Jiting and Zhu, Nuobei and Li, Yunhe and Fu, Yuqian and Chen, Yinxinyu and Cai, Hongyi and Ye, Zewei and Cheng, Bing and others},
272	  journal={arXiv preprint arXiv:2605.14950},
273	  year={2026}
274	}
275	
276	% ===== Action Refinement =====
277	
278	@article{chen2026dfmvla,
279	  title={{DFM-VLA}: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching},
280	  author={Chen, Jiayi and Song, Wenxuan and Chen, Shuai and Wang, Jingbo and Li, Zhijun and Li, Haoang},
281	  journal={arXiv preprint arXiv:2603.26320},
282	  year={2026}
283	}
284	
285	% ===== Parameter-Efficient Fine-Tuning =====
286	
287	@inproceedings{hu2022lora,
288	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
289	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
290	  booktitle = {International Conference on Learning Representations (ICLR)},
291	  year      = {2022},
292	}
293	
294	% ===== VLA Safety Survey =====
295	
296	@article{li2026vlasafety,
297	  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
298	  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},
299	  journal={arXiv preprint arXiv:2604.23775},
300	  year={2026}
301	}
302	
303	% ===== Evaluation Methodology =====
304	
305	@article{snyder2026beyond,
306	  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},
307	  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},
308	  journal={arXiv preprint arXiv:2603.13616},
309	  year={2026}
310	}
311	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "5dd3d6a5-84db-4343-9491-bbaa492db9d2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
      "content": "% The Safety Illusion — References\n% Analysis paper on fake safety in VLA collision avoidance evaluation\n% Generated: 2026-05-24\n\n% ===== VLA Foundation Models =====\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Collision-Aware VLA Methods =====\n\n@article{hu2025vlsa,\n  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},\n  journal={arXiv preprint arXiv:2512.11891},\n  year={2025}\n}\n\n@inproceedings{zhang2025safevla,\n  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cofreeevla2026,\n  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},\n  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},\n  journal={arXiv preprint arXiv:2601.21712},\n  year={2026}\n}\n\n@article{spalter2024ikinqp,\n  title={Towards Online Safety Corrections for Robotic Manipulation Policies},\n  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},\n  journal={arXiv preprint arXiv:2409.08233},\n  year={2024}\n}\n\n@inproceedings{li2024langguided,\n  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},\n  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2025}\n}\n\n@article{yang2025cape,\n  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},\n  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},\n  journal={arXiv preprint arXiv:2511.22773},\n  year={2025}\n}\n\n% ===== SDF in Robotics =====\n\n@inproceedings{park2019deepsdf,\n  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},\n  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2019}\n}\n\n@inproceedings{ortiz2022isdf,\n  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},\n  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\\\"o}fer, Michael and Mukadam, Mustafa},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2022}\n}\n\n@article{zhi2021diffco,\n  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},\n  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},\n  journal={IEEE Transactions on Robotics},\n  volume={38},\n  number={5},\n  pages={2668--2685},\n  year={2022}\n}\n\n@inproceedings{huang2023voxposer,\n  title={{VoxPoser}: Composable {3D} Value Maps for Robotic Manipulation with Language Models},\n  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Benchmarks and Training =====\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ===== Evaluation Reliability =====\n\n@inproceedings{gururangan2018annotation,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year={2018}\n}\n\n@inproceedings{karwowski2024goodhart,\n  title={Goodhart's Law in Reinforcement Learning},\n  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% ===== Diffusion Policy =====\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n% ===== SDF in Robotics (additional) =====\n\n@inproceedings{vasilopoulos2023ramp,\n  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},\n  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},\n  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},\n  year={2023}\n}\n\n@article{chen2026cssdfnet,\n  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},\n  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},\n  journal={arXiv preprint arXiv:2603.18669},\n  year={2026}\n}\n\n@article{jacquet2025neuralnmpc,\n  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},\n  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},\n  journal={The International Journal of Robotics Research},\n  year={2025}\n}\n\n@article{chen2025samp,\n  title={{SAMP}: Spatial Anchor-based Motion Policy for Collision-Aware Robotic Manipulators},\n  author={Chen, Kai and Bi, Zhihai and Zhao, Guoyang and Zheng, Chunxin and Li, Yulin and Zhao, Hang and Ma, Jun},\n  journal={arXiv preprint arXiv:2509.11185},\n  year={2025}\n}\n\n@inproceedings{ruan2025profrobot,\n  title={Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions},\n  author={Ruan, Quanyuan and Lei, Jiabao and Yuan, Wenhao and Zhang, Yanglin and Lu, Dekun and Liu, Guiliang and Jia, Kui},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2025}\n}\n\n% ===== 3D-Aware VLA Methods =====\n\n@article{depthvla2025,\n  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},\n  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},\n  journal={arXiv preprint arXiv:2510.13375},\n  year={2025}\n}\n\n@article{li2025qdepth,\n  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},\n  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},\n  journal={arXiv preprint arXiv:2510.14836},\n  year={2025}\n}\n\n@article{li2025spatialforcing,\n  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},\n  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},\n  journal={arXiv preprint arXiv:2510.12276},\n  year={2025}\n}\n\n@article{3dcavla2025,\n  title={{3D CAVLA}: Leveraging Depth and {3D} Context to Generalize Vision Language Action Models for Unseen Tasks},\n  author={Bhat, Vineet and Lan, Yu-Hsiang and Krishnamurthy, Prashanth and Karri, Ramesh and Khorrami, Farshad},\n  journal={arXiv preprint arXiv:2505.05800},\n  year={2025}\n}\n\n@article{geoaware2025,\n  title={{GeoAware-VLA}: Implicit Geometry Aware Vision-Language-Action Model},\n  author={Abouzeid, Ali and Mansour, Malak and Sun, Qinbo and Sun, Zezhou and Song, Dezhen},\n  journal={arXiv preprint arXiv:2509.14117},\n  year={2025}\n}\n\n@inproceedings{spatialvla2025,\n  title={{SpatialVLA}: Exploring Spatial Representations for Visual-Language-Action Model},\n  author={Qu, Delin and Song, Haoming and Chen, Qizhi and Yao, Yuanqi and Ye, Xinyi and Gu, Jiayuan and Wang, Zhigang and Ding, Yan and Zhao, Bin and Wang, Dong and Li, Xuelong},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2025}\n}\n\n@article{gstvla2026,\n  title={{GST-VLA}: Structured Gaussian Spatial Tokens for {3D} Depth-Aware Vision-Language-Action Models},\n  author={Sarowar, Md Selim and Tariq, Omer and Kim, Sungho},\n  journal={arXiv preprint arXiv:2603.09079},\n  year={2026}\n}\n\n@article{stemvla2026,\n  title={{StemVLA}: An Open-Source Vision-Language-Action Model with Future {3D} Spatial Geometry Knowledge and {4D} Historical Representation},\n  author={Xiao, Jiasong and She, Yutao and Li, Kai and Sha, Yuyang and Cheng, Ziang and Tong, Ziang},\n  journal={arXiv preprint arXiv:2602.23721},\n  year={2026}\n}\n\n@article{stvla2026,\n  title={{ST-VLA}: Enabling {4D}-Aware Spatiotemporal Understanding for General Robot Manipulation},\n  author={Wu, You and Chen, Zixuan and Ou, Cunxu and Wang, Wenxuan and Huang, Wenbo and Cao, Lin and Chen, Yangtao and Qiu, Weichao and Quan, Xingyue and Shi, Jieqi and Huo, Jing and Gao, Yang},\n  journal={arXiv preprint arXiv:2603.13788},\n  year={2026}\n}\n\n@article{evo02025,\n  title={{Evo-0}: Vision-Language-Action Model with Implicit Spatial Understanding},\n  author={Lin, Tao and Li, Gen and Zhong, Yilei and Zou, Yanwen and Du, Yuxin and Liu, Jiting and Gu, Encheng and Zhao, Bo},\n  journal={arXiv preprint arXiv:2507.00416},\n  year={2025}\n}\n\n@article{savla2026,\n  title={{SA-VLA}: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning},\n  author={Pan, Xu and Wan, Zhenglin and Yu, Xingrui and Zheng, Xianwei and Ke, Youkai and Sun, Ming and Wang, Rui and Wang, Ziwei and Tsang, Ivor},\n  journal={arXiv preprint arXiv:2602.00743},\n  year={2026}\n}\n\n@article{augvla3d2026,\n  title={{AugVLA-3D}: Depth-Driven Feature Augmentation for Vision-Language-Action Models},\n  author={Rao, Zhifeng and Chen, Wenlong and Xie, Lei and Hua, Xia and Yin, Dongfu and Tian, Zhen and Yu, F. Richard},\n  journal={arXiv preprint arXiv:2602.10698},\n  year={2026}\n}\n\n@article{evodepth2026,\n  title={{Evo-Depth}: A Lightweight Depth-Enhanced Vision-Language-Action Model},\n  author={Lin, Tao and Du, Yuxin and Liu, Jiting and Zhu, Nuobei and Li, Yunhe and Fu, Yuqian and Chen, Yinxinyu and Cai, Hongyi and Ye, Zewei and Cheng, Bing and others},\n  journal={arXiv preprint arXiv:2605.14950},\n  year={2026}\n}\n\n% ===== Action Refinement =====\n\n@article{chen2026dfmvla,\n  title={{DFM-VLA}: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching},\n  author={Chen, Jiayi and Song, Wenxuan and Chen, Shuai and Wang, Jingbo and Li, Zhijun and Li, Haoang},\n  journal={arXiv preprint arXiv:2603.26320},\n  year={2026}\n}\n\n% ===== Parameter-Efficient Fine-Tuning =====\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n}\n\n% ===== VLA Safety Survey =====\n\n@article{li2026vlasafety,\n  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},\n  journal={arXiv preprint arXiv:2604.23775},\n  year={2026}\n}\n\n% ===== Evaluation Methodology =====\n\n@article{snyder2026beyond,\n  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},\n  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},\n  journal={arXiv preprint arXiv:2603.13616},\n  year={2026}\n}\n",
      "numLines": 311,
      "startLine": 1,
      "totalLines": 311
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
Now I have all the materials. Let me synthesize:

1. **Paper framing**: The paper is about VLA safety evaluation being systematically flawed - CAR metric is contaminated by action collapse and geometric path safety. They propose dfCAR as a corrected metric. SDF auxiliary loss is tested but found to not improve beyond LoRA-only baseline.

2. **Literature map**: Contains papers on VLA foundations, collision-aware VLA, SDF in robotics, safe RL, action collapse, benchmarks.

3. **Bib file**: Has all the bib keys I need.

Let me now write the related_work.tex with 4 paragraphs:


- First paragraph covers foundational VLA models like Pi0, RT-2, and OpenVLA, discussing their use of flow matching and action chunking, then highlighting the gap that these systems lack safety guarantees despite handling safety-relevant tasks.
- Second paragraph addresses safety in robot learning, covering safe RL approaches like CPO and constraint-based methods, then existing VLA safety work like SafeVLA and VLSA, before noting that these methods struggle with end-to-end VLA architectures.
- Third paragraph is cut off but should cover collision detection and SDF-based approaches in robotics.

Now I'm looking at the rest of the content. The third paragraph discusses signed distance functions in robotics—tools like DeepSDF and DiffCo used for collision detection and motion planning—and notes that while SDFs are used as auxiliary losses in multi-task learning, they haven't been systematically evaluated as a training-time auxiliary for VLAs. The fourth paragraph covers evaluation metrics for safe manipulation, including SafeLIBERO and LIBERO benchmarks, CAR/TSR metrics, and the problem of action collapse masking fake safety, which is where the dfCAR contribution comes in.

I'm now checking which bibliography keys are available for these papers, starting with the VLA foundation models and working through the citations to ensure everything is properly referenced. I'm scanning through more bib entries and noticing several papers that are referenced in the literature map but don't have corresponding bibliography entries—Octo, CPO, and RAIL are the main ones missing. I'm checking which papers need bibliography entries—most of these recent papers don't have bib entries yet, and Pi0.5 from Physical Intelligence is missing entirely, so I'll mark that as TODO. Now I'm drafting the related work section, keeping it to 600-800 words with careful attention to citation formatting, no em-dashes, and making sure each paragraph connects back to this work. Starting with vision-language models for manipulation, I'll cover how RT-2 pioneered action tokenization, Pi0 introduced flow matching for continuous predictions, and OpenVLA provided an open-source alternative, then explain how these models typically pretrain a VLM backbone before fine-tuning on robotic data.

I'm continuing with how recent work has added spatial reasoning through 3D supervision—Spatial Forcing, QDepth-VLA, and DepthVLA—but the key gap is that safety considerations are almost entirely missing from VLA training and evaluation. Most VLAs train on collision-free data and measure only task success, with no way to distinguish genuine collision avoidance from incidental safety. This is exactly what my paper addresses.

For the second paragraph on safety in robot learning, I'm covering the established history of constrained policy optimization and trust-region methods, then moving into more recent work on safety constraints in learning-based control, before tying it back to how my approach differs by specifically examining whether standard metrics actually capture safety behavior in vision-language models. scalar cost constraints. Control barrier functions (CBFs) provide formal safety certificates by constraining the system to remain within a safe set. Several recent works apply these ideas to learned manipulation policies. VLSA attaches a plug-and-play CBF safety layer to VLA outputs, filtering unsafe actions at inference time. SafeVLA formulates VLA safety as a constrained MDP and optimizes policies under explicit cost limits. RAIL trains a standard imitation learning policy and applies a reachability-based safety filter at test time. iKinQP-RL uses inverse kinematics quadratic programming to correct RL policy actions online. These approaches share a common pattern: safety is enforced through external mechanisms, either at training time via constrained optimization or at test time via action filtering. The end-to-end nature of VLAs, which map raw pixels and language to actions, makes it difficult to inject geometric safety constraints into the learned representation itself. This work investigates whether auxiliary geometric supervision during training can produce intrinsic collision avoidance, and I'm finding that standard safety metrics actually fail to capture this behavior reliably.

Signed distance functions encode minimum distance to the nearest surface with sign indicating inside or outside, and neural networks can learn these continuous representations of 3D shapes. In robotics, SDFs have become central to perception, planning, and control—from real-time scene understanding with streaming depth images to language-guided manipulation planning and fully differentiable collision detection for trajectory optimization. Recent work is extending SDFs into configuration space as well. I'm verifying which citations are actually in the bibliography. SafeVLA and VLSA are there, so I can use those instead of CPO and RAIL to avoid adding TODOs. Let me restructure the safety section to reference papers that are already cited.

For the manipulation section, I'm checking brohan2023rt2, black2024pi0, kim2024openvla, lipman2023flow, hu2022lora, and li2025spatialforcing - these are all in the bib, so I can build the paragraph around them without needing TODO markers.

For safety in robot learning, I have hu2025vlsa, zhang2025safevla, spalter2024ikinqp, cofreeevla2026, li2024langguided, yang2025cape, and li2026vlasafety as a survey, which gives me solid coverage. CPO is marked TODO but I can work around it.

For SDFs in robotics, I'm pulling from park2019deepsdf, ortiz2022isdf, huang2023voxposer, vasilopoulos2023ramp, and zhi2021diffco - all confirmed in the bibliography.

Now I'm adding chen2026cssdfnet and jacquet2025neuralnmpc to that section, though I still need to track down Liu et al. on robot SDFs and Li et al. on C-space SDFs.

For evaluation metrics, I have liu2023libero, hu2025vlsa with SafeLIBERO, snyder2026beyond, karwowski2024goodhart, gururangan2018annotation, and chi2023diffusionpolicy covering mode collapse. Dong2025cocos on action collapse is still TODO.

Now I'm drafting the actual LaTeX for the related work section, keeping it between 600-800 words while maintaining the style constraints.

Writing LaTeX... Vision-language-action models follow a consistent training paradigm—pretrain a vision-language model, then fine-tune on robotic demonstrations using parameter-efficient methods—though recent work has enhanced spatial understanding by incorporating 3D geometry and depth prediction as auxiliary tasks. However, most VLAs train exclusively on collision-free data and evaluate only task success, lacking any mechanism to identify genuine collision avoidance versus accidental safety.

Now I'm looking at how safety considerations fit into robot learning more broadly. There are training-time approaches like constrained reinforcement learning that explicitly limit safety violations—SafeVLA demonstrates this can reduce violations by over 80%—and test-time methods that apply external safety filters, such as control barrier functions or collision risk estimators that override unsafe actions at inference.

Other techniques correct policy outputs through inverse kinematics optimization or, in diffusion policies, inject collision costs during the denoising process to steer trajectories away from obstacles. A recent survey organizes these into runtime shields, constrained optimization, and representation-based methods, but most share a common limitation: safety is imposed externally rather than learned within the policy itself. Since VLAs map pixels and language directly to actions end-to-end, it's challenging to embed geometric constraints into the learned representations. I'm investigating whether auxiliary SDF supervision during training can instead produce intrinsic collision awareness within the policy.

Now I'm covering how SDFs work in robotics—they encode minimum distance to surfaces with sign indicating whether a point is inside or outside. Neural networks can learn to represent these continuous distance fields, and robotics has applied them across perception, planning, and control tasks. Recent work uses SDFs for real-time scene understanding from depth streams, composing 3D value maps to guide manipulation, and enabling fully differentiable collision detection for trajectory optimization.

The field is expanding beyond task space into configuration space for whole-body collision checking and model predictive control, though integrating distance fields into end-to-end learned policies hasn't been thoroughly explored. I'm testing whether using SDF as an auxiliary loss during fine-tuning can help flow-matching policies learn better collision avoidance.

Moving to evaluation metrics, I need to establish how to measure safety in manipulation beyond just task success. There's a standardized benchmark for lifelong robot learning with multiple task suites, and recent work extends this with obstacle-aware variants.

However, the standard collision avoidance rate metric has a critical flaw—it doesn't distinguish between a robot that never moves and one that actively avoids obstacles. Both score perfectly despite very different behaviors. This connects to deeper issues with metric reliability: optimizing proxy metrics can diverge from true objectives, and superficial correlations often inflate benchmark scores. I'm proposing a more nuanced approach to capture whether the robot is actually learning avoidance behavior rather than just happening to avoid collisions.

Now I'm checking the word count and verifying all the citation keys are in the bibliography. Finished checking the reference list—all citations are accounted for. Now verifying the writing style: no em-dashes, no overused AI language like "significantly" or "leverage," no sentences starting with gerunds, and each paragraph connects back to the work. The gerund phrase about filtering action collapse is fine since it's describing what the method does rather than a stylistic ending. I'm catching some -ing phrase endings that violate the style guide. Let me fix the conclusion of paragraph 3 by restructuring it to end with a direct statement rather than a participle phrase, and do the same for paragraph 4 where I'm describing the motion threshold filter—I'll convert that to a complete sentence structure instead of trailing with "isolating genuine avoidance behavior." I'm continuing to scan through the opening words of each sentence to ensure I'm avoiding -ing constructions. Working through paragraph two, I'm checking that SafeVLA, VLSA, CoFreeVLA, and the other method names are properly positioned, and moving into paragraph three where I'm verifying that Signed distance functions and DeepSDF also start appropriately.

Now I'm catching an issue in paragraph four—"Evaluating" opens with a gerund, so I need to restructure that to "Evaluation of manipulation safety requires metrics beyond binary task success." The rest of the paragraph checks out: LIBERO, SafeLIBERO, task success metrics, and the discussion of frozen robots and Goodhart's law all have proper sentence structures.

For the connecting phrase about mapping pixels and language directly to actions, I should rephrase it as an appositive rather than a gerund phrase to stay safe with the style rules. Something like "The end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult..." works better.

Now I'm finalizing the Related Work section with the corrected grammar — changing "Evaluating" to "Evaluation of" and ensuring no -ing phrases start sentences or end clauses awkwardly. The section covers the progression of VLA models from RT-2 through OpenVLA, establishing the common paradigm of pretraining a vision-language model and then fine-tuning on demonstration data. parameter-efficient methods such as LoRA.
Recent work has enhanced VLA spatial understanding through auxiliary 3D supervision like Spatial Forcing, which aligns visual embeddings with 3D geometry, and depth-based approaches that incorporate depth prediction as auxiliary tasks.
Despite these advances, safety considerations remain largely absent from VLA training and evaluation—most systems train on collision-free demonstrations and evaluate only task success, without distinguishing genuine avoidance behavior from incidentally safe trajectories.
This paper investigates whether collision avoidance metrics actually capture safety in VLA policies.

Safety-aware robot learning employs both training-time and test-time strategies. Training-time approaches like constrained reinforcement learning and SafeVLA optimize policies under explicit cost constraints, achieving significant reductions in safety violations. Test-time methods apply external safety filters—control barrier functions, collision risk estimators, inverse kinematics corrections, and diffusion-based trajectory steering—to override or modify unsafe actions at inference. A recent survey categorizes these into runtime shields, constrained optimization, and representation-based methods, but most share a common limitation: safety is imposed externally rather than learned within the policy's internal representations.

The end-to-end nature of VLAs, which directly map pixels and language to actions, makes it challenging to embed geometric constraints into learned features. I'm testing whether auxiliary SDF supervision during training can develop intrinsic collision awareness and how existing safety metrics respond to this intervention.

Signed distance functions encode minimum distance to the nearest surface with sign indicating interior or exterior. Neural networks can represent continuous SDFs of 3D shapes, and in robotics they support perception, planning, and control across multiple applications—from real-time scene understanding and language-guided manipulation to motion planning with fully differentiable collision detection. Recent extensions push SDFs into configuration space for whole-body collision checking and neural model predictive control with SDF constraints.

While these works show the utility of distance fields in classical planning and control, integrating them into end-to-end learned policies remains largely unexplored. I'm evaluating SDF as an auxiliary training loss during VLA fine-tuning to see whether geometric distance supervision can teach flow-matching policies to avoid collisions.

For evaluating manipulation safety, I need metrics beyond binary task success. SafeLIBERO extends the LIBERO benchmark with obstacle-augmented environments and introduces collision avoidance rate (CAR)—the fraction of episodes without any collision—alongside task success rate to capture the safety-capability tradeoff. However, CAR treats all collision-free episodes the same regardless of the robot's actual behavior, so a frozen robot that never moves would score perfectly.

The real issue is that CAR doesn't distinguish between learned avoidance and accidental success. A robot that happens to miss obstacles scores just as high as one that actively avoids them, which echoes broader concerns about metric reliability—Goodhart's law shows that optimizing proxy metrics can diverge from true objectives, and annotation artifacts can inflate benchmark scores. I'm proposing displacement-filtered CAR (dfCAR), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.

Now I'm doing a final verification of the paper: checking that all citation keys are in the bibliography, estimating word count across the four paragraphs to ensure it stays within the 600-800 range, and scanning for style issues like em-dashes, overused words like "significantly" or "leverage," and sentence structures that start or end with -ing phrases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "2adb461c-3981-4321-b811-e453448f394c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6gGWxz12nQvcC3bwTqY5G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18786,
      "cache_read_input_tokens": 30173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18786
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

_source line 19_

Let me check if the output file already exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "fe9999f5-1da8-43ba-bc6a-838514edda7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6gGWxz12nQvcC3bwTqY5G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18786,
      "cache_read_input_tokens": 30173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18786
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

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01Mb35jSRkmg4c1RQGcgMdsA`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "e6bda4b4-73fe-4550-a057-8869c87e93db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6gGWxz12nQvcC3bwTqY5G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18786,
      "cache_read_input_tokens": 30173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18786
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

_source line 21 · 2026-05-26T16:14:42.358Z_

<details><summary>↩ Tool result · `toolu_01Mb35jSRkmg4c1RQGcgMdsA`</summary>

```text
docs/paper/_archive/method.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
docs/paper/analysis_claim4.tex
docs/paper/related_work.tex
docs/paper/appendix.tex
docs/paper/experimental_framework.tex
docs/paper/analysis_claim3.tex
docs/paper/abstract.tex
docs/paper/analysis_claim1.tex
docs/paper/analysis_claim2.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/claim2.tex
docs/paper/method.tex
docs/paper/claim1.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "2a2dcc88-528a-4f7f-9ae4-5bbf71f8b9bb",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_archive/method.tex",
      "docs/paper/_archive/experiments.tex",
      "docs/paper/_archive/conclusion_DEPRECATED.tex",
      "docs/paper/analysis_claim4.tex",
      "docs/paper/related_work.tex",
      "docs/paper/appendix.tex",
      "docs/paper/experimental_framework.tex",
      "docs/paper/analysis_claim3.tex",
      "docs/paper/abstract.tex",
      "docs/paper/analysis_claim1.tex",
      "docs/paper/analysis_claim2.tex",
      "docs/paper/discussion.tex",
      "docs/paper/introduction.tex",
      "docs/paper/main.tex",
      "docs/paper/claim2.tex",
      "docs/paper/method.tex",
      "docs/paper/claim1.tex"
    ],
    "durationMs": 15,
    "numFiles": 17,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01NXpREf3ZBQHBMA24SwUGff`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "ee36e38d-c6c2-4963-9a6d-301bb6b35aae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwHPPeyVmEKizLXyPYek4u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8766,
      "cache_read_input_tokens": 48959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8766
      },
      "output_tokens": 68,
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

_source line 23 · 2026-05-26T16:14:50.818Z_

<details><summary>↩ Tool result · `toolu_01NXpREf3ZBQHBMA24SwUGff`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\subsection{Collision-Safe VLA Methods}\label{sec:rw_collision}
4	
5	Recent methods for collision avoidance in VLAs fall into three categories. \textbf{Post-hoc correction} approaches modify policy outputs before execution. AEGIS~\cite{hu2025vlsa} applies Control Barrier Function corrections to VLA actions based on open-set detection and monocular depth estimation, and reports 77.85\% CAR on SafeLIBERO without additional training. iKinQP-RL~\cite{spalter2024ikinqp} enforces collision constraints through inverse-kinematics quadratic programming at runtime. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator that halts dual-arm execution when predicted collision probability exceeds a threshold.
6	
7	\textbf{Constrained optimization} embeds safety into training. SafeVLA~\cite{zhang2025safevla} formulates collision avoidance as a Constrained MDP and reports an 83.58\% reduction in safety violations through reward shaping.
8	
9	\textbf{Inference-time guidance} steers the generative process toward safe trajectories without retraining. Li et al.~\cite{li2024langguided} train an object-centric diffusion policy on 3D point clouds and inject collision costs during denoising. CAPE~\cite{yang2025cape} expands the trajectory distribution through context-aware priors and iterative refinement.
10	
11	These methods differ in mechanism but share a common evaluation pattern: all report Collision Avoidance Rate as primary evidence of safety. None examine whether the measured CAR reflects genuine obstacle avoidance or conflates it with other behaviors. Our analysis (Section~\ref{sec:fake_safety}) reveals that this conflation is severe in the Pi0 family: 98--99\% of safe episodes are attributable to inaction rather than planned avoidance. We do not challenge the technical contributions of these methods; we identify a validity gap in the metric on which they rely, and propose a filtered variant (CAR$_\text{f}$) that separates genuine avoidance from frozen behavior.
12	
13	\subsection{Signed Distance Fields in Robot Manipulation}
14	
15	Signed Distance Fields encode the distance from a query point to the nearest obstacle surface, where the sign indicates free space (positive) or penetration (negative). DeepSDF~\cite{park2019deepsdf} established neural SDF prediction as a compact shape representation. iSDF~\cite{ortiz2022isdf} extended this to incremental scene reconstruction for real-time robot perception. DiffCo~\cite{zhi2021diffco} introduced differentiable collision checking through learned distance fields and showed that gradient-based trajectory optimization can enforce collision constraints. VoxPoser~\cite{huang2023voxposer} composes 3D value maps from language model outputs for manipulation planning, with avoidance maps that encode obstacle information in volumetric form.
16	
17	SDF-based collision detection is well validated in classical motion planning. The natural question is whether this effectiveness transfers to VLA action refinement, where the SDF gradient modifies predicted end-effector actions to increase obstacle clearance. Our oracle experiments (Section~\ref{sec:ee_only}) test this directly by replacing the learned SDF network with ground-truth distance fields computed from simulation geometry, which eliminates all prediction error. The results reveal a structural limitation of end-effector-only refinement: all three oracle variants produce more collisions than unrefined baselines, because the gradient that repels the end-effector simultaneously rotates arm links into obstacle volumes. The problem is not SDF accuracy but application scope. Full-body collision avoidance requires distance information along the entire kinematic chain, not only at the tool tip.
18	
19	\subsection{Evaluation Reliability in Robot Learning}
20	
21	Concerns about whether standard metrics measure what they claim to measure have a long history in ML evaluation. Benchmark saturation and annotation artifact exploitation in NLP demonstrated that high scores can reflect dataset properties rather than target capabilities~\cite{gururangan2018annotation}. Goodhart's law (a measure ceases to be informative once it becomes an optimization target) has been documented in reinforcement learning settings where agents exploit reward proxies rather than solve intended tasks~\cite{karwowski2024goodhart}. These cases share a common structure: a metric that appears to measure capability $X$ in fact measures a confound $Y$, and the discrepancy remains invisible until the aggregate score is decomposed.
22	
23	The confound in VLA safety evaluation is action collapse, a phenomenon related to mode collapse in generative models. Diffusion-based robot policies can collapse to the mean of multi-modal action distributions~\cite{chi2023diffusionpolicy}, and VLAs trained on limited demonstration data exhibit similar failure modes that produce near-zero actions. Action collapse itself is well recognized. Its interaction with displacement-based safety metrics is not: a collapsed model registers as maximally safe because it generates no motion that could cause collisions. CAR cannot distinguish a model that plans a collision-free trajectory from a model that does nothing.
24	
25	A recent survey~\citep{li2026vlasafety} provides a comprehensive taxonomy of VLA safety threats including freezing attacks, which produce the same behavioral signature as the action collapse we analyze; our contribution is the quantitative demonstration that this phenomenon systematically contaminates the primary evaluation metric. Concurrently, Snyder et al.~\citep{snyder2026beyond} argue that binary success rates are insufficient for meaningful robot policy comparison and propose statistically rigorous alternatives, reinforcing the need for metrics that capture richer behavioral distinctions.
26	
27	All collision avoidance methods reviewed in Section~\ref{sec:rw_collision} adopt CAR without examining its construct validity. Our displacement-filtered variant, CAR$_\text{f}$ (Section~\ref{sec:metrics}), conditions safety measurement on motor activity, converting CAR from a contaminated aggregate into a metric that isolates genuine avoidance from inaction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "67d761be-cc84-45c7-98fb-9e4151953d2a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\subsection{Collision-Safe VLA Methods}\\label{sec:rw_collision}\n\nRecent methods for collision avoidance in VLAs fall into three categories. \\textbf{Post-hoc correction} approaches modify policy outputs before execution. AEGIS~\\cite{hu2025vlsa} applies Control Barrier Function corrections to VLA actions based on open-set detection and monocular depth estimation, and reports 77.85\\% CAR on SafeLIBERO without additional training. iKinQP-RL~\\cite{spalter2024ikinqp} enforces collision constraints through inverse-kinematics quadratic programming at runtime. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator that halts dual-arm execution when predicted collision probability exceeds a threshold.\n\n\\textbf{Constrained optimization} embeds safety into training. SafeVLA~\\cite{zhang2025safevla} formulates collision avoidance as a Constrained MDP and reports an 83.58\\% reduction in safety violations through reward shaping.\n\n\\textbf{Inference-time guidance} steers the generative process toward safe trajectories without retraining. Li et al.~\\cite{li2024langguided} train an object-centric diffusion policy on 3D point clouds and inject collision costs during denoising. CAPE~\\cite{yang2025cape} expands the trajectory distribution through context-aware priors and iterative refinement.\n\nThese methods differ in mechanism but share a common evaluation pattern: all report Collision Avoidance Rate as primary evidence of safety. None examine whether the measured CAR reflects genuine obstacle avoidance or conflates it with other behaviors. Our analysis (Section~\\ref{sec:fake_safety}) reveals that this conflation is severe in the Pi0 family: 98--99\\% of safe episodes are attributable to inaction rather than planned avoidance. We do not challenge the technical contributions of these methods; we identify a validity gap in the metric on which they rely, and propose a filtered variant (CAR$_\\text{f}$) that separates genuine avoidance from frozen behavior.\n\n\\subsection{Signed Distance Fields in Robot Manipulation}\n\nSigned Distance Fields encode the distance from a query point to the nearest obstacle surface, where the sign indicates free space (positive) or penetration (negative). DeepSDF~\\cite{park2019deepsdf} established neural SDF prediction as a compact shape representation. iSDF~\\cite{ortiz2022isdf} extended this to incremental scene reconstruction for real-time robot perception. DiffCo~\\cite{zhi2021diffco} introduced differentiable collision checking through learned distance fields and showed that gradient-based trajectory optimization can enforce collision constraints. VoxPoser~\\cite{huang2023voxposer} composes 3D value maps from language model outputs for manipulation planning, with avoidance maps that encode obstacle information in volumetric form.\n\nSDF-based collision detection is well validated in classical motion planning. The natural question is whether this effectiveness transfers to VLA action refinement, where the SDF gradient modifies predicted end-effector actions to increase obstacle clearance. Our oracle experiments (Section~\\ref{sec:ee_only}) test this directly by replacing the learned SDF network with ground-truth distance fields computed from simulation geometry, which eliminates all prediction error. The results reveal a structural limitation of end-effector-only refinement: all three oracle variants produce more collisions than unrefined baselines, because the gradient that repels the end-effector simultaneously rotates arm links into obstacle volumes. The problem is not SDF accuracy but application scope. Full-body collision avoidance requires distance information along the entire kinematic chain, not only at the tool tip.\n\n\\subsection{Evaluation Reliability in Robot Learning}\n\nConcerns about whether standard metrics measure what they claim to measure have a long history in ML evaluation. Benchmark saturation and annotation artifact exploitation in NLP demonstrated that high scores can reflect dataset properties rather than target capabilities~\\cite{gururangan2018annotation}. Goodhart's law (a measure ceases to be informative once it becomes an optimization target) has been documented in reinforcement learning settings where agents exploit reward proxies rather than solve intended tasks~\\cite{karwowski2024goodhart}. These cases share a common structure: a metric that appears to measure capability $X$ in fact measures a confound $Y$, and the discrepancy remains invisible until the aggregate score is decomposed.\n\nThe confound in VLA safety evaluation is action collapse, a phenomenon related to mode collapse in generative models. Diffusion-based robot policies can collapse to the mean of multi-modal action distributions~\\cite{chi2023diffusionpolicy}, and VLAs trained on limited demonstration data exhibit similar failure modes that produce near-zero actions. Action collapse itself is well recognized. Its interaction with displacement-based safety metrics is not: a collapsed model registers as maximally safe because it generates no motion that could cause collisions. CAR cannot distinguish a model that plans a collision-free trajectory from a model that does nothing.\n\nA recent survey~\\citep{li2026vlasafety} provides a comprehensive taxonomy of VLA safety threats including freezing attacks, which produce the same behavioral signature as the action collapse we analyze; our contribution is the quantitative demonstration that this phenomenon systematically contaminates the primary evaluation metric. Concurrently, Snyder et al.~\\citep{snyder2026beyond} argue that binary success rates are insufficient for meaningful robot policy comparison and propose statistically rigorous alternatives, reinforcing the need for metrics that capture richer behavioral distinctions.\n\nAll collision avoidance methods reviewed in Section~\\ref{sec:rw_collision} adopt CAR without examining its construct validity. Our displacement-filtered variant, CAR$_\\text{f}$ (Section~\\ref{sec:metrics}), conditions safety measurement on motor activity, converting CAR from a contaminated aggregate into a metric that isolates genuine avoidance from inaction.",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
There's already a related_work.tex file with 3 subsections. The task asks me to rewrite it with 4 paragraphs, ~600-800 words, following the specific structure requirements. The existing version is more verbose and uses \subsection rather than \paragraph. Let me write the new version.

Let me also note that the existing version uses CAR$_\text{f}$ for the filtered metric, but the paper_framing.md uses "dfCAR". Let me check which convention the other tex files use.

Actually, the task spec says "dfCAR" but the existing related_work uses "CAR$_\text{f}$". 

I need to check the main paper and a few other tex files to see which notation is used consistently throughout the project.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "a5265fcc-5475-4ea3-abd1-667b1edff624",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZhzG9gN7ovLL4x9iXPh9k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 57725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 25_

Let me check the metric naming convention used elsewhere in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "a2eec867-ee0a-48a5-9155-d8bb0bfeccdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZhzG9gN7ovLL4x9iXPh9k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 57725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_01WHr4H6gTayr27Ww8oLhGnq`</summary>

```json
{
  "pattern": "dfCAR|CAR_\\\\\\\\text|CARf|CAR_f",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "6e5b7381-8cf3-4f61-b7c8-aa84b55eb1c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZhzG9gN7ovLL4x9iXPh9k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 57725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1645
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

_source line 27 · 2026-05-26T16:15:01.769Z_

<details><summary>↩ Tool result · `toolu_01WHr4H6gTayr27Ww8oLhGnq`</summary>

```text
docs/paper/main.tex:15:\newcommand{\dfCAR}{\text{dfCAR}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "cb30d4db-09aa-47a5-a8cc-ff5b33bc281d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:15:\\newcommand{\\dfCAR}{\\text{dfCAR}}",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Grep · `toolu_01KQZ7GhaNKMuUia7QRDK9sC`</summary>

```json
{
  "pattern": "\\\\\\\\dfCAR|dfCAR",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "59ea0f43-cf15-4623-962f-426b9f5f997f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAZVMEbS4HUhYqojQJ5Yko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 398,
      "cache_read_input_tokens": 59370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 398
      },
      "output_tokens": 60,
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

_source line 29 · 2026-05-26T16:15:05.534Z_

<details><summary>↩ Tool result · `toolu_01KQZ7GhaNKMuUia7QRDK9sC`</summary>

```text
docs/paper/main.tex:15:\newcommand{\dfCAR}{\text{dfCAR}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "ad7ca3b4-797f-40e5-b801-3cf4487587fe",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:15:\\newcommand{\\dfCAR}{\\text{dfCAR}}",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 30_

The paper defines `\dfCAR` as the macro. The existing related_work.tex uses `CAR$_\text{f}$` which is inconsistent. Let me also check section labels used elsewhere.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "2e7b548e-4e3a-4231-b8dc-40b62954e979",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4XkF9c4U4822Fvr6GSDxW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 59768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 182
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

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01XwPnN4mhWhuUs25s5BRrUV`</summary>

```json
{
  "pattern": "\\\\\\\\ref\\\\{sec:.*\\\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "6a84c607-6f65-41fa-a86d-d22644dce0fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4XkF9c4U4822Fvr6GSDxW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 59768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 182
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

_source line 32 · 2026-05-26T16:15:10.184Z_

<details><summary>↩ Tool result · `toolu_01XwPnN4mhWhuUs25s5BRrUV`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "2ce9d968-b827-4e13-a007-4c7426c8f718",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_01TZJARt5Hm9YzXr5SCVw7RS`</summary>

```json
{
  "pattern": "\\\\label\\\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "4ecaab88-1d9c-4b6f-888d-b04b99bb9562",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165sGoRcXq2AtVoenX9HAVK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 59950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 227
      },
      "output_tokens": 59,
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

_source line 34 · 2026-05-26T16:15:14.862Z_

<details><summary>↩ Tool result · `toolu_01TZJARt5Hm9YzXr5SCVw7RS`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "8603a13b-28ce-4061-bdbd-d8f98d60e83f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_019dN1siYmvoMLptNJn6QofS`</summary>

```json
{
  "pattern": "label",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "9368e612-089b-4147-b220-25e8f53c260d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjbjGcshkL6HfnmMmLEFLb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 60177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 175
      },
      "output_tokens": 71,
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

_source line 36 · 2026-05-26T16:15:19.117Z_

<details><summary>↩ Tool result · `toolu_019dN1siYmvoMLptNJn6QofS`</summary>

```text
docs/paper/related_work.tex:1:\section{Related Work}\label{sec:related}
docs/paper/related_work.tex:3:\subsection{Collision-Safe VLA Methods}\label{sec:rw_collision}
docs/paper/analysis_claim2.tex:1:\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
docs/paper/analysis_claim2.tex:8:\label{tab:oracle}
docs/paper/discussion.tex:1:\section{Discussion and Conclusion}\label{sec:conclusion}
docs/paper/experimental_framework.tex:1:\section{Experimental Framework}\label{sec:framework}
docs/paper/experimental_framework.tex:13:\subsection{Evaluation Metrics}\label{sec:metrics}
docs/paper/experimental_framework.tex:20:\begin{equation}\label{eq:car_f}
docs/paper/experimental_framework.tex:53:The workspace signed distance field is computed from the known obstacle meshes available in the LIBERO/MuJoCo simulation environment. SDF values are positive in free space, zero on the obstacle surface, and negative inside the obstacle volume. Ground-truth labels are generated at query points sampled along predicted end-effector trajectories during training.
docs/paper/method.tex:1:\section{Experimental Setup and Metrics}\label{sec:method}
docs/paper/method.tex:5:\subsection{Benchmark and Models}\label{sec:benchmark}
docs/paper/method.tex:16:\label{tab:configurations}
docs/paper/method.tex:36:\subsection{Standard Metrics}\label{sec:standard_metrics}
docs/paper/method.tex:39:\begin{equation}\label{eq:car}
docs/paper/method.tex:43:\begin{equation}\label{eq:tsr}
docs/paper/method.tex:48:\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
docs/paper/method.tex:59:\begin{equation}\label{eq:car_f}
docs/paper/method.tex:68:\subsection{SDF Auxiliary Training}\label{sec:sdf_aux}
docs/paper/method.tex:77:\begin{equation}\label{eq:total_loss}
docs/paper/method.tex:86:\subsection{Oracle SDF Refinement}\label{sec:oracle_setup}

[Showing results with pagination = limit: 20]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "d63cc9b1-3340-4515-973a-409f827a596b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:1:\\section{Related Work}\\label{sec:related}\ndocs/paper/related_work.tex:3:\\subsection{Collision-Safe VLA Methods}\\label{sec:rw_collision}\ndocs/paper/analysis_claim2.tex:1:\\subsection{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\ndocs/paper/analysis_claim2.tex:8:\\label{tab:oracle}\ndocs/paper/discussion.tex:1:\\section{Discussion and Conclusion}\\label{sec:conclusion}\ndocs/paper/experimental_framework.tex:1:\\section{Experimental Framework}\\label{sec:framework}\ndocs/paper/experimental_framework.tex:13:\\subsection{Evaluation Metrics}\\label{sec:metrics}\ndocs/paper/experimental_framework.tex:20:\\begin{equation}\\label{eq:car_f}\ndocs/paper/experimental_framework.tex:53:The workspace signed distance field is computed from the known obstacle meshes available in the LIBERO/MuJoCo simulation environment. SDF values are positive in free space, zero on the obstacle surface, and negative inside the obstacle volume. Ground-truth labels are generated at query points sampled along predicted end-effector trajectories during training.\ndocs/paper/method.tex:1:\\section{Experimental Setup and Metrics}\\label{sec:method}\ndocs/paper/method.tex:5:\\subsection{Benchmark and Models}\\label{sec:benchmark}\ndocs/paper/method.tex:16:\\label{tab:configurations}\ndocs/paper/method.tex:36:\\subsection{Standard Metrics}\\label{sec:standard_metrics}\ndocs/paper/method.tex:39:\\begin{equation}\\label{eq:car}\ndocs/paper/method.tex:43:\\begin{equation}\\label{eq:tsr}\ndocs/paper/method.tex:48:\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\ndocs/paper/method.tex:59:\\begin{equation}\\label{eq:car_f}\ndocs/paper/method.tex:68:\\subsection{SDF Auxiliary Training}\\label{sec:sdf_aux}\ndocs/paper/method.tex:77:\\begin{equation}\\label{eq:total_loss}\ndocs/paper/method.tex:86:\\subsection{Oracle SDF Refinement}\\label{sec:oracle_setup}",
    "numLines": 20,
    "appliedLimit": 20
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
I see. The paper uses labels like `\label{sec:dfcar}`, `\label{sec:method}`, etc. The existing related_work uses `\label{sec:related}` and cross-references to `\ref{sec:fake_safety}`, `\ref{sec:ee_only}`, and `\ref{sec:metrics}`. Some of these labels exist and some don't (e.g., `sec:fake_safety` doesn't appear in the grep).

Also, the paper uses `\dfCAR` as the macro for the filtered metric, defined in main.tex.

Now let me write the new related_work.tex. The structure should be:


- 4 paragraphs (not subsections)
- ~600-800 words
- Use `\paragraph{}` style
- Keep `\label{sec:related}` for the section

I need to verify which cross-references are valid. Looking at the labels I found: `sec:ee_only` exists in analysis_claim2.tex, `sec:metrics` exists in experimental_framework.tex, but `sec:fake_safety` doesn't appear anywhere—I should either find it or remove that reference when writing the new section.

Let me check analysis_claim1.tex to see if the fake safety analysis is labeled there instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "8898d337-889b-450b-9bc4-d9da47adae15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zuDwussbnyMi6iy4obnus",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 60352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 755
      },
      "output_tokens": 10,
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

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_014i3AefekJfNqxcVJoqotWS`</summary>

```json
{
  "pattern": "fake_safety|claim1|analysis",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "78310388-edf8-424a-9e6a-dc244b8baa2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zuDwussbnyMi6iy4obnus",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 60352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 755
      },
      "output_tokens": 10,
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

_source line 39 · 2026-05-26T16:15:33.361Z_

<details><summary>↩ Tool result · `toolu_014i3AefekJfNqxcVJoqotWS`</summary>

```text
docs/paper/related_work.tex:11:[Omitted long matching line]
docs/paper/main.tex:39:\input{claim1}
docs/paper/analysis_claim2.tex:3:[Omitted long matching line]
docs/paper/discussion.tex:3:[Omitted long matching line]
docs/paper/discussion.tex:9:[Omitted long matching line]
docs/paper/discussion.tex:12:[Omitted long matching line]
docs/paper/experimental_framework.tex:3:This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), which separates genuine avoidance from action collapse.
docs/paper/method.tex:3:This section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\S\ref{sec:dfcar}).
docs/paper/analysis_claim1.tex:1:\subsection{The Fake Safety Problem}\label{sec:fake_safety}
docs/paper/analysis_claim1.tex:5:[Omitted long matching line]

[Showing results with pagination = limit: 10]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "af8585cb-3d13-419a-8317-07ff7bb82eba",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:11:[Omitted long matching line]\ndocs/paper/main.tex:39:\\input{claim1}\ndocs/paper/analysis_claim2.tex:3:[Omitted long matching line]\ndocs/paper/discussion.tex:3:[Omitted long matching line]\ndocs/paper/discussion.tex:9:[Omitted long matching line]\ndocs/paper/discussion.tex:12:[Omitted long matching line]\ndocs/paper/experimental_framework.tex:3:This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), which separates genuine avoidance from action collapse.\ndocs/paper/method.tex:3:This section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\\S\\ref{sec:dfcar}).\ndocs/paper/analysis_claim1.tex:1:\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\ndocs/paper/analysis_claim1.tex:5:[Omitted long matching line]",
    "numLines": 10,
    "appliedLimit": 10
  }
}
```

</details>

---

### Assistant

_source line 40_

Good. `sec:fake_safety` is in analysis_claim1.tex, `sec:ee_only` in analysis_claim2.tex, `sec:metrics`/`sec:dfcar` in method.tex. The paper also uses CAR$_\text{f}$ in some places and `\dfCAR` as a macro. Let me use `\dfCAR` since that's the defined macro.

Now I'll write the new related_work.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "82067c1e-5d7d-447d-aad4-20cfa843ee38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gydnxgq5P2P6cxZXRCvRsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 61107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 917
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

_source line 41_

<details open><summary>🔧 Tool call — Write · `toolu_01M1SrNhWsMR7tTnX86bQFUk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models for Manipulation.}\nVision-language-action (VLA) models combine pretrained vision-language backbones with action prediction to produce generalist manipulation policies.\nRT-2~\\cite{brohan2023rt2} first demonstrated that VLM pretraining transfers to robotic control through action tokenization.\n$\\pi_0$~\\cite{black2024pi0} introduced flow matching~\\cite{lipman2023flow} for continuous action generation, and Diffusion Policy~\\cite{chi2023diffusionpolicy} showed that diffusion-based prediction handles multimodal demonstration distributions.\nOpenVLA~\\cite{kim2024openvla} provided an open-source 7B-parameter alternative trained on 970k real demonstrations.\nThese models share a common paradigm: pretrain a VLM, then fine-tune on demonstration data with parameter-efficient methods such as LoRA~\\cite{hu2022lora}.\nRecent work has enhanced VLA spatial reasoning through auxiliary 3D supervision.\nSpatial Forcing~\\cite{li2025spatialforcing} aligns intermediate visual embeddings with 3D geometry features; QDepth-VLA~\\cite{li2025qdepth} and DepthVLA~\\cite{depthvla2025} incorporate depth prediction as auxiliary tasks.\nDespite this progress, safety considerations remain largely absent from VLA training and evaluation.\nMost VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance behavior from incidental collision-free trajectories.\nThis paper examines whether standard collision avoidance metrics reliably capture safety behavior in VLA policies.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware robot learning spans training-time and test-time approaches.\nAt training time, constrained reinforcement learning methods optimize policies under explicit cost limits; SafeVLA~\\cite{zhang2025safevla} applies this framework to VLA policies through constrained MDP formulation, reducing safety violations by over 80\\%.\nAt test time, several methods apply external safety filters to learned policies.\nVLSA~\\cite{hu2025vlsa} attaches a control barrier function (CBF) layer to VLA outputs, overriding unsafe actions at inference.\nCoFreeVLA~\\cite{cofreeevla2026} uses a short-horizon collision risk estimator to gate dangerous dual-arm actions.\niKinQP-RL~\\cite{spalter2024ikinqp} corrects policy outputs through inverse kinematics quadratic programming.\nIn the diffusion policy setting, \\citet{li2024langguided} and CAPE~\\cite{yang2025cape} inject collision costs during the denoising process to steer trajectories away from obstacles.\nA recent survey~\\cite{li2026vlasafety} categorizes these methods into runtime shields, constrained optimization, and representation-based approaches.\nCommon to most is that safety is imposed through external mechanisms rather than learned within the policy's internal representations.\nThe end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult to inject geometric constraints into learned features.\nThis work tests whether auxiliary SDF supervision during VLA training can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSigned distance functions (SDFs) encode the minimum distance from any query point to the nearest surface, with sign indicating free space or penetration.\nDeepSDF~\\cite{park2019deepsdf} showed that neural networks can represent continuous SDFs of 3D shapes.\nIn robotics, SDFs serve perception, planning, and control.\niSDF~\\cite{ortiz2022isdf} builds real-time neural distance fields from streaming depth images for scene understanding.\nVoxPoser~\\cite{huang2023voxposer} composes 3D value maps, including obstacle avoidance fields, to guide manipulation through language.\nFor motion planning, RAMP~\\cite{vasilopoulos2023ramp} uses implicit SDFs within reactive controllers, and DiffCo~\\cite{zhi2021diffco} provides fully differentiable collision detection for gradient-based trajectory optimization.\nRecent work extends SDFs beyond task space: CSSDF-Net~\\cite{chen2026cssdfnet} estimates configuration-space distance fields for whole-body collision checking, and Neural NMPC~\\cite{jacquet2025neuralnmpc} encodes SDF constraints directly into model predictive control.\nThese works demonstrate the effectiveness of distance fields in classical planning and control pipelines, but their integration into end-to-end learned policies remains unexplored.\nWe evaluate SDF as an auxiliary training loss during VLA fine-tuning to determine whether geometric distance supervision can teach flow-matching policies to avoid collisions.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nEvaluation of manipulation safety requires metrics beyond binary task success.\nLIBERO~\\cite{liu2023libero} established a standardized benchmark for lifelong robot learning with four task suites.\nSafeLIBERO, introduced by \\citet{hu2025vlsa}, extends LIBERO with obstacle-augmented environments and a collision avoidance rate (CAR) metric, defined as the fraction of episodes without any collision.\nTask success rate (TSR) and CAR together aim to capture the safety-capability tradeoff.\nHowever, CAR treats all collision-free episodes identically regardless of the robot's behavior: a frozen robot that never moves scores perfect CAR, and a capable robot whose trajectory happens to miss obstacles also registers high CAR.\nNeither case reflects learned avoidance behavior.\nThis failure mode echoes broader concerns about metric reliability.\nGoodhart's law in RL~\\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.\nRecent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nWe propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "7773bfc2-504f-4ede-99c5-50f6d30c9815",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gydnxgq5P2P6cxZXRCvRsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 61107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 917
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

_source line 42 · 2026-05-26T16:16:22.009Z_

<details><summary>↩ Tool result · `toolu_01M1SrNhWsMR7tTnX86bQFUk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "97cb8738-d934-49bb-becf-1e6632b56956",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models for Manipulation.}\nVision-language-action (VLA) models combine pretrained vision-language backbones with action prediction to produce generalist manipulation policies.\nRT-2~\\cite{brohan2023rt2} first demonstrated that VLM pretraining transfers to robotic control through action tokenization.\n$\\pi_0$~\\cite{black2024pi0} introduced flow matching~\\cite{lipman2023flow} for continuous action generation, and Diffusion Policy~\\cite{chi2023diffusionpolicy} showed that diffusion-based prediction handles multimodal demonstration distributions.\nOpenVLA~\\cite{kim2024openvla} provided an open-source 7B-parameter alternative trained on 970k real demonstrations.\nThese models share a common paradigm: pretrain a VLM, then fine-tune on demonstration data with parameter-efficient methods such as LoRA~\\cite{hu2022lora}.\nRecent work has enhanced VLA spatial reasoning through auxiliary 3D supervision.\nSpatial Forcing~\\cite{li2025spatialforcing} aligns intermediate visual embeddings with 3D geometry features; QDepth-VLA~\\cite{li2025qdepth} and DepthVLA~\\cite{depthvla2025} incorporate depth prediction as auxiliary tasks.\nDespite this progress, safety considerations remain largely absent from VLA training and evaluation.\nMost VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance behavior from incidental collision-free trajectories.\nThis paper examines whether standard collision avoidance metrics reliably capture safety behavior in VLA policies.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware robot learning spans training-time and test-time approaches.\nAt training time, constrained reinforcement learning methods optimize policies under explicit cost limits; SafeVLA~\\cite{zhang2025safevla} applies this framework to VLA policies through constrained MDP formulation, reducing safety violations by over 80\\%.\nAt test time, several methods apply external safety filters to learned policies.\nVLSA~\\cite{hu2025vlsa} attaches a control barrier function (CBF) layer to VLA outputs, overriding unsafe actions at inference.\nCoFreeVLA~\\cite{cofreeevla2026} uses a short-horizon collision risk estimator to gate dangerous dual-arm actions.\niKinQP-RL~\\cite{spalter2024ikinqp} corrects policy outputs through inverse kinematics quadratic programming.\nIn the diffusion policy setting, \\citet{li2024langguided} and CAPE~\\cite{yang2025cape} inject collision costs during the denoising process to steer trajectories away from obstacles.\nA recent survey~\\cite{li2026vlasafety} categorizes these methods into runtime shields, constrained optimization, and representation-based approaches.\nCommon to most is that safety is imposed through external mechanisms rather than learned within the policy's internal representations.\nThe end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult to inject geometric constraints into learned features.\nThis work tests whether auxiliary SDF supervision during VLA training can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSigned distance functions (SDFs) encode the minimum distance from any query point to the nearest surface, with sign indicating free space or penetration.\nDeepSDF~\\cite{park2019deepsdf} showed that neural networks can represent continuous SDFs of 3D shapes.\nIn robotics, SDFs serve perception, planning, and control.\niSDF~\\cite{ortiz2022isdf} builds real-time neural distance fields from streaming depth images for scene understanding.\nVoxPoser~\\cite{huang2023voxposer} composes 3D value maps, including obstacle avoidance fields, to guide manipulation through language.\nFor motion planning, RAMP~\\cite{vasilopoulos2023ramp} uses implicit SDFs within reactive controllers, and DiffCo~\\cite{zhi2021diffco} provides fully differentiable collision detection for gradient-based trajectory optimization.\nRecent work extends SDFs beyond task space: CSSDF-Net~\\cite{chen2026cssdfnet} estimates configuration-space distance fields for whole-body collision checking, and Neural NMPC~\\cite{jacquet2025neuralnmpc} encodes SDF constraints directly into model predictive control.\nThese works demonstrate the effectiveness of distance fields in classical planning and control pipelines, but their integration into end-to-end learned policies remains unexplored.\nWe evaluate SDF as an auxiliary training loss during VLA fine-tuning to determine whether geometric distance supervision can teach flow-matching policies to avoid collisions.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nEvaluation of manipulation safety requires metrics beyond binary task success.\nLIBERO~\\cite{liu2023libero} established a standardized benchmark for lifelong robot learning with four task suites.\nSafeLIBERO, introduced by \\citet{hu2025vlsa}, extends LIBERO with obstacle-augmented environments and a collision avoidance rate (CAR) metric, defined as the fraction of episodes without any collision.\nTask success rate (TSR) and CAR together aim to capture the safety-capability tradeoff.\nHowever, CAR treats all collision-free episodes identically regardless of the robot's behavior: a frozen robot that never moves scores perfect CAR, and a capable robot whose trajectory happens to miss obstacles also registers high CAR.\nNeither case reflects learned avoidance behavior.\nThis failure mode echoes broader concerns about metric reliability.\nGoodhart's law in RL~\\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.\nRecent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nWe propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 27,
        "newStart": 1,
        "newLines": 49,
        "lines": [
          " \\section{Related Work}\\label{sec:related}",
          " ",
          "-\\subsection{Collision-Safe VLA Methods}\\label{sec:rw_collision}",
          "+\\paragraph{Vision-Language-Action Models for Manipulation.}",
          "+Vision-language-action (VLA) models combine pretrained vision-language backbones with action prediction to produce generalist manipulation policies.",
          "+RT-2~\\cite{brohan2023rt2} first demonstrated that VLM pretraining transfers to robotic control through action tokenization.",
          "+$\\pi_0$~\\cite{black2024pi0} introduced flow matching~\\cite{lipman2023flow} for continuous action generation, and Diffusion Policy~\\cite{chi2023diffusionpolicy} showed that diffusion-based prediction handles multimodal demonstration distributions.",
          "+OpenVLA~\\cite{kim2024openvla} provided an open-source 7B-parameter alternative trained on 970k real demonstrations.",
          "+These models share a common paradigm: pretrain a VLM, then fine-tune on demonstration data with parameter-efficient methods such as LoRA~\\cite{hu2022lora}.",
          "+Recent work has enhanced VLA spatial reasoning through auxiliary 3D supervision.",
          "+Spatial Forcing~\\cite{li2025spatialforcing} aligns intermediate visual embeddings with 3D geometry features; QDepth-VLA~\\cite{li2025qdepth} and DepthVLA~\\cite{depthvla2025} incorporate depth prediction as auxiliary tasks.",
          "+Despite this progress, safety considerations remain largely absent from VLA training and evaluation.",
          "+Most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance behavior from incidental collision-free trajectories.",
          "+This paper examines whether standard collision avoidance metrics reliably capture safety behavior in VLA policies.",
          " ",
          "-Recent methods for collision avoidance in VLAs fall into three categories. \\textbf{Post-hoc correction} approaches modify policy outputs before execution. AEGIS~\\cite{hu2025vlsa} applies Control Barrier Function corrections to VLA actions based on open-set detection and monocular depth estimation, and reports 77.85\\% CAR on SafeLIBERO without additional training. iKinQP-RL~\\cite{spalter2024ikinqp} enforces collision constraints through inverse-kinematics quadratic programming at runtime. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator that halts dual-arm execution when predicted collision probability exceeds a threshold.",
          "+\\paragraph{Safety in Robot Learning.}",
          "+Safety-aware robot learning spans training-time and test-time approaches.",
          "+At training time, constrained reinforcement learning methods optimize policies under explicit cost limits; SafeVLA~\\cite{zhang2025safevla} applies this framework to VLA policies through constrained MDP formulation, reducing safety violations by over 80\\%.",
          "+At test time, several methods apply external safety filters to learned policies.",
          "+VLSA~\\cite{hu2025vlsa} attaches a control barrier function (CBF) layer to VLA outputs, overriding unsafe actions at inference.",
          "+CoFreeVLA~\\cite{cofreeevla2026} uses a short-horizon collision risk estimator to gate dangerous dual-arm actions.",
          "+iKinQP-RL~\\cite{spalter2024ikinqp} corrects policy outputs through inverse kinematics quadratic programming.",
          "+In the diffusion policy setting, \\citet{li2024langguided} and CAPE~\\cite{yang2025cape} inject collision costs during the denoising process to steer trajectories away from obstacles.",
          "+A recent survey~\\cite{li2026vlasafety} categorizes these methods into runtime shields, constrained optimization, and representation-based approaches.",
          "+Common to most is that safety is imposed through external mechanisms rather than learned within the policy's internal representations.",
          "+The end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult to inject geometric constraints into learned features.",
          "+This work tests whether auxiliary SDF supervision during VLA training can produce intrinsic collision awareness.",
          " ",
          "-\\textbf{Constrained optimization} embeds safety into training. SafeVLA~\\cite{zhang2025safevla} formulates collision avoidance as a Constrained MDP and reports an 83.58\\% reduction in safety violations through reward shaping.",
          "+\\paragraph{Signed Distance Functions in Robotics.}",
          "+Signed distance functions (SDFs) encode the minimum distance from any query point to the nearest surface, with sign indicating free space or penetration.",
          "+DeepSDF~\\cite{park2019deepsdf} showed that neural networks can represent continuous SDFs of 3D shapes.",
          "+In robotics, SDFs serve perception, planning, and control.",
          "+iSDF~\\cite{ortiz2022isdf} builds real-time neural distance fields from streaming depth images for scene understanding.",
          "+VoxPoser~\\cite{huang2023voxposer} composes 3D value maps, including obstacle avoidance fields, to guide manipulation through language.",
          "+For motion planning, RAMP~\\cite{vasilopoulos2023ramp} uses implicit SDFs within reactive controllers, and DiffCo~\\cite{zhi2021diffco} provides fully differentiable collision detection for gradient-based trajectory optimization.",
          "+Recent work extends SDFs beyond task space: CSSDF-Net~\\cite{chen2026cssdfnet} estimates configuration-space distance fields for whole-body collision checking, and Neural NMPC~\\cite{jacquet2025neuralnmpc} encodes SDF constraints directly into model predictive control.",
          "+These works demonstrate the effectiveness of distance fields in classical planning and control pipelines, but their integration into end-to-end learned policies remains unexplored.",
          "+We evaluate SDF as an auxiliary training loss during VLA fine-tuning to determine whether geometric distance supervision can teach flow-matching policies to avoid collisions.",
          " ",
          "-\\textbf{Inference-time guidance} steers the generative process toward safe trajectories without retraining. Li et al.~\\cite{li2024langguided} train an object-centric diffusion policy on 3D point clouds and inject collision costs during denoising. CAPE~\\cite{yang2025cape} expands the trajectory distribution through context-aware priors and iterative refinement.",
          "-",
          "-These methods differ in mechanism but share a common evaluation pattern: all report Collision Avoidance Rate as primary evidence of safety. None examine whether the measured CAR reflects genuine obstacle avoidance or conflates it with other behaviors. Our analysis (Section~\\ref{sec:fake_safety}) reveals that this conflation is severe in the Pi0 family: 98--99\\% of safe episodes are attributable to inaction rather than planned avoidance. We do not challenge the technical contributions of these methods; we identify a validity gap in the metric on which they rely, and propose a filtered variant (CAR$_\\text{f}$) that separates genuine avoidance from frozen behavior.",
          "-",
          "-\\subsection{Signed Distance Fields in Robot Manipulation}",
          "-",
          "-Signed Distance Fields encode the distance from a query point to the nearest obstacle surface, where the sign indicates free space (positive) or penetration (negative). DeepSDF~\\cite{park2019deepsdf} established neural SDF prediction as a compact shape representation. iSDF~\\cite{ortiz2022isdf} extended this to incremental scene reconstruction for real-time robot perception. DiffCo~\\cite{zhi2021diffco} introduced differentiable collision checking through learned distance fields and showed that gradient-based trajectory optimization can enforce collision constraints. VoxPoser~\\cite{huang2023voxposer} composes 3D value maps from language model outputs for manipulation planning, with avoidance maps that encode obstacle information in volumetric form.",
          "-",
          "-SDF-based collision detection is well validated in classical motion planning. The natural question is whether this effectiveness transfers to VLA action refinement, where the SDF gradient modifies predicted end-effector actions to increase obstacle clearance. Our oracle experiments (Section~\\ref{sec:ee_only}) test this directly by replacing the learned SDF network with ground-truth distance fields computed from simulation geometry, which eliminates all prediction error. The results reveal a structural limitation of end-effector-only refinement: all three oracle variants produce more collisions than unrefined baselines, because the gradient that repels the end-effector simultaneously rotates arm links into obstacle volumes. The problem is not SDF accuracy but application scope. Full-body collision avoidance requires distance information along the entire kinematic chain, not only at the tool tip.",
          "-",
          "-\\subsection{Evaluation Reliability in Robot Learning}",
          "-",
          "-Concerns about whether standard metrics measure what they claim to measure have a long history in ML evaluation. Benchmark saturation and annotation artifact exploitation in NLP demonstrated that high scores can reflect dataset properties rather than target capabilities~\\cite{gururangan2018annotation}. Goodhart's law (a measure ceases to be informative once it becomes an optimization target) has been documented in reinforcement learning settings where agents exploit reward proxies rather than solve intended tasks~\\cite{karwowski2024goodhart}. These cases share a common structure: a metric that appears to measure capability $X$ in fact measures a confound $Y$, and the discrepancy remains invisible until the aggregate score is decomposed.",
          "-",
          "-The confound in VLA safety evaluation is action collapse, a phenomenon related to mode collapse in generative models. Diffusion-based robot policies can collapse to the mean of multi-modal action distributions~\\cite{chi2023diffusionpolicy}, and VLAs trained on limited demonstration data exhibit similar failure modes that produce near-zero actions. Action collapse itself is well recognized. Its interaction with displacement-based safety metrics is not: a collapsed model registers as maximally safe because it generates no motion that could cause collisions. CAR cannot distinguish a model that plans a collision-free trajectory from a model that does nothing.",
          "-",
          "-A recent survey~\\citep{li2026vlasafety} provides a comprehensive taxonomy of VLA safety threats including freezing attacks, which produce the same behavioral signature as the action collapse we analyze; our contribution is the quantitative demonstration that this phenomenon systematically contaminates the primary evaluation metric. Concurrently, Snyder et al.~\\citep{snyder2026beyond} argue that binary success rates are insufficient for meaningful robot policy comparison and propose statistically rigorous alternatives, reinforcing the need for metrics that capture richer behavioral distinctions.",
          "-",
          "-All collision avoidance methods reviewed in Section~\\ref{sec:rw_collision} adopt CAR without examining its construct validity. Our displacement-filtered variant, CAR$_\\text{f}$ (Section~\\ref{sec:metrics}), conditions safety measurement on motor activity, converting CAR from a contaminated aggregate into a metric that isolates genuine avoidance from inaction.",
          "\\ No newline at end of file",
          "+\\paragraph{Evaluation Metrics for Safe Manipulation.}",
          "+Evaluation of manipulation safety requires metrics beyond binary task success.",
          "+LIBERO~\\cite{liu2023libero} established a standardized benchmark for lifelong robot learning with four task suites.",
          "+SafeLIBERO, introduced by \\citet{hu2025vlsa}, extends LIBERO with obstacle-augmented environments and a collision avoidance rate (CAR) metric, defined as the fraction of episodes without any collision.",
          "+Task success rate (TSR) and CAR together aim to capture the safety-capability tradeoff.",
          "+However, CAR treats all collision-free episodes identically regardless of the robot's behavior: a frozen robot that never moves scores perfect CAR, and a capable robot whose trajectory happens to miss obstacles also registers high CAR.",
          "+Neither case reflects learned avoidance behavior.",
          "+This failure mode echoes broader concerns about metric reliability.",
          "+Goodhart's law in RL~\\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.",
          "+Recent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.",
          "+We propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\\label{sec:related}\n\n\\subsection{Collision-Safe VLA Methods}\\label{sec:rw_collision}\n\nRecent methods for collision avoidance in VLAs fall into three categories. \\textbf{Post-hoc correction} approaches modify policy outputs before execution. AEGIS~\\cite{hu2025vlsa} applies Control Barrier Function corrections to VLA actions based on open-set detection and monocular depth estimation, and reports 77.85\\% CAR on SafeLIBERO without additional training. iKinQP-RL~\\cite{spalter2024ikinqp} enforces collision constraints through inverse-kinematics quadratic programming at runtime. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator that halts dual-arm execution when predicted collision probability exceeds a threshold.\n\n\\textbf{Constrained optimization} embeds safety into training. SafeVLA~\\cite{zhang2025safevla} formulates collision avoidance as a Constrained MDP and reports an 83.58\\% reduction in safety violations through reward shaping.\n\n\\textbf{Inference-time guidance} steers the generative process toward safe trajectories without retraining. Li et al.~\\cite{li2024langguided} train an object-centric diffusion policy on 3D point clouds and inject collision costs during denoising. CAPE~\\cite{yang2025cape} expands the trajectory distribution through context-aware priors and iterative refinement.\n\nThese methods differ in mechanism but share a common evaluation pattern: all report Collision Avoidance Rate as primary evidence of safety. None examine whether the measured CAR reflects genuine obstacle avoidance or conflates it with other behaviors. Our analysis (Section~\\ref{sec:fake_safety}) reveals that this conflation is severe in the Pi0 family: 98--99\\% of safe episodes are attributable to inaction rather than planned avoidance. We do not challenge the technical contributions of these methods; we identify a validity gap in the metric on which they rely, and propose a filtered variant (CAR$_\\text{f}$) that separates genuine avoidance from frozen behavior.\n\n\\subsection{Signed Distance Fields in Robot Manipulation}\n\nSigned Distance Fields encode the distance from a query point to the nearest obstacle surface, where the sign indicates free space (positive) or penetration (negative). DeepSDF~\\cite{park2019deepsdf} established neural SDF prediction as a compact shape representation. iSDF~\\cite{ortiz2022isdf} extended this to incremental scene reconstruction for real-time robot perception. DiffCo~\\cite{zhi2021diffco} introduced differentiable collision checking through learned distance fields and showed that gradient-based trajectory optimization can enforce collision constraints. VoxPoser~\\cite{huang2023voxposer} composes 3D value maps from language model outputs for manipulation planning, with avoidance maps that encode obstacle information in volumetric form.\n\nSDF-based collision detection is well validated in classical motion planning. The natural question is whether this effectiveness transfers to VLA action refinement, where the SDF gradient modifies predicted end-effector actions to increase obstacle clearance. Our oracle experiments (Section~\\ref{sec:ee_only}) test this directly by replacing the learned SDF network with ground-truth distance fields computed from simulation geometry, which eliminates all prediction error. The results reveal a structural limitation of end-effector-only refinement: all three oracle variants produce more collisions than unrefined baselines, because the gradient that repels the end-effector simultaneously rotates arm links into obstacle volumes. The problem is not SDF accuracy but application scope. Full-body collision avoidance requires distance information along the entire kinematic chain, not only at the tool tip.\n\n\\subsection{Evaluation Reliability in Robot Learning}\n\nConcerns about whether standard metrics measure what they claim to measure have a long history in ML evaluation. Benchmark saturation and annotation artifact exploitation in NLP demonstrated that high scores can reflect dataset properties rather than target capabilities~\\cite{gururangan2018annotation}. Goodhart's law (a measure ceases to be informative once it becomes an optimization target) has been documented in reinforcement learning settings where agents exploit reward proxies rather than solve intended tasks~\\cite{karwowski2024goodhart}. These cases share a common structure: a metric that appears to measure capability $X$ in fact measures a confound $Y$, and the discrepancy remains invisible until the aggregate score is decomposed.\n\nThe confound in VLA safety evaluation is action collapse, a phenomenon related to mode collapse in generative models. Diffusion-based robot policies can collapse to the mean of multi-modal action distributions~\\cite{chi2023diffusionpolicy}, and VLAs trained on limited demonstration data exhibit similar failure modes that produce near-zero actions. Action collapse itself is well recognized. Its interaction with displacement-based safety metrics is not: a collapsed model registers as maximally safe because it generates no motion that could cause collisions. CAR cannot distinguish a model that plans a collision-free trajectory from a model that does nothing.\n\nA recent survey~\\citep{li2026vlasafety} provides a comprehensive taxonomy of VLA safety threats including freezing attacks, which produce the same behavioral signature as the action collapse we analyze; our contribution is the quantitative demonstration that this phenomenon systematically contaminates the primary evaluation metric. Concurrently, Snyder et al.~\\citep{snyder2026beyond} argue that binary success rates are insufficient for meaningful robot policy comparison and propose statistically rigorous alternatives, reinforcing the need for metrics that capture richer behavioral distinctions.\n\nAll collision avoidance methods reviewed in Section~\\ref{sec:rw_collision} adopt CAR without examining its construct validity. Our displacement-filtered variant, CAR$_\\text{f}$ (Section~\\ref{sec:metrics}), conditions safety measurement on motor activity, converting CAR from a contaminated aggregate into a metric that isolates genuine avoidance from inaction.",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 43_

Now let me verify the output against all requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "bcc96d31-75b3-4237-9fc3-749e6e1a9bb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQ5PTNyANvbTPCkdc39TeV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1844,
      "cache_read_input_tokens": 62024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1844
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

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01YMXWVwmEur6i4nKrNUkPQH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "a682f19c-48c1-4f5d-b474-5031bc6db95d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQ5PTNyANvbTPCkdc39TeV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1844,
      "cache_read_input_tokens": 62024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1844
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

_source line 45 · 2026-05-26T16:16:26.001Z_

<details><summary>↩ Tool result · `toolu_01YMXWVwmEur6i4nKrNUkPQH`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models for Manipulation.}
4	Vision-language-action (VLA) models combine pretrained vision-language backbones with action prediction to produce generalist manipulation policies.
5	RT-2~\cite{brohan2023rt2} first demonstrated that VLM pretraining transfers to robotic control through action tokenization.
6	$\pi_0$~\cite{black2024pi0} introduced flow matching~\cite{lipman2023flow} for continuous action generation, and Diffusion Policy~\cite{chi2023diffusionpolicy} showed that diffusion-based prediction handles multimodal demonstration distributions.
7	OpenVLA~\cite{kim2024openvla} provided an open-source 7B-parameter alternative trained on 970k real demonstrations.
8	These models share a common paradigm: pretrain a VLM, then fine-tune on demonstration data with parameter-efficient methods such as LoRA~\cite{hu2022lora}.
9	Recent work has enhanced VLA spatial reasoning through auxiliary 3D supervision.
10	Spatial Forcing~\cite{li2025spatialforcing} aligns intermediate visual embeddings with 3D geometry features; QDepth-VLA~\cite{li2025qdepth} and DepthVLA~\cite{depthvla2025} incorporate depth prediction as auxiliary tasks.
11	Despite this progress, safety considerations remain largely absent from VLA training and evaluation.
12	Most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance behavior from incidental collision-free trajectories.
13	This paper examines whether standard collision avoidance metrics reliably capture safety behavior in VLA policies.
14	
15	\paragraph{Safety in Robot Learning.}
16	Safety-aware robot learning spans training-time and test-time approaches.
17	At training time, constrained reinforcement learning methods optimize policies under explicit cost limits; SafeVLA~\cite{zhang2025safevla} applies this framework to VLA policies through constrained MDP formulation, reducing safety violations by over 80\%.
18	At test time, several methods apply external safety filters to learned policies.
19	VLSA~\cite{hu2025vlsa} attaches a control barrier function (CBF) layer to VLA outputs, overriding unsafe actions at inference.
20	CoFreeVLA~\cite{cofreeevla2026} uses a short-horizon collision risk estimator to gate dangerous dual-arm actions.
21	iKinQP-RL~\cite{spalter2024ikinqp} corrects policy outputs through inverse kinematics quadratic programming.
22	In the diffusion policy setting, \citet{li2024langguided} and CAPE~\cite{yang2025cape} inject collision costs during the denoising process to steer trajectories away from obstacles.
23	A recent survey~\cite{li2026vlasafety} categorizes these methods into runtime shields, constrained optimization, and representation-based approaches.
24	Common to most is that safety is imposed through external mechanisms rather than learned within the policy's internal representations.
25	The end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult to inject geometric constraints into learned features.
26	This work tests whether auxiliary SDF supervision during VLA training can produce intrinsic collision awareness.
27	
28	\paragraph{Signed Distance Functions in Robotics.}
29	Signed distance functions (SDFs) encode the minimum distance from any query point to the nearest surface, with sign indicating free space or penetration.
30	DeepSDF~\cite{park2019deepsdf} showed that neural networks can represent continuous SDFs of 3D shapes.
31	In robotics, SDFs serve perception, planning, and control.
32	iSDF~\cite{ortiz2022isdf} builds real-time neural distance fields from streaming depth images for scene understanding.
33	VoxPoser~\cite{huang2023voxposer} composes 3D value maps, including obstacle avoidance fields, to guide manipulation through language.
34	For motion planning, RAMP~\cite{vasilopoulos2023ramp} uses implicit SDFs within reactive controllers, and DiffCo~\cite{zhi2021diffco} provides fully differentiable collision detection for gradient-based trajectory optimization.
35	Recent work extends SDFs beyond task space: CSSDF-Net~\cite{chen2026cssdfnet} estimates configuration-space distance fields for whole-body collision checking, and Neural NMPC~\cite{jacquet2025neuralnmpc} encodes SDF constraints directly into model predictive control.
36	These works demonstrate the effectiveness of distance fields in classical planning and control pipelines, but their integration into end-to-end learned policies remains unexplored.
37	We evaluate SDF as an auxiliary training loss during VLA fine-tuning to determine whether geometric distance supervision can teach flow-matching policies to avoid collisions.
38	
39	\paragraph{Evaluation Metrics for Safe Manipulation.}
40	Evaluation of manipulation safety requires metrics beyond binary task success.
41	LIBERO~\cite{liu2023libero} established a standardized benchmark for lifelong robot learning with four task suites.
42	SafeLIBERO, introduced by \citet{hu2025vlsa}, extends LIBERO with obstacle-augmented environments and a collision avoidance rate (CAR) metric, defined as the fraction of episodes without any collision.
43	Task success rate (TSR) and CAR together aim to capture the safety-capability tradeoff.
44	However, CAR treats all collision-free episodes identically regardless of the robot's behavior: a frozen robot that never moves scores perfect CAR, and a capable robot whose trajectory happens to miss obstacles also registers high CAR.
45	Neither case reflects learned avoidance behavior.
46	This failure mode echoes broader concerns about metric reliability.
47	Goodhart's law in RL~\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.
48	Recent work on statistically rigorous robot evaluation~\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.
49	We propose displacement-filtered CAR ($\dfCAR$, \S\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "97876f25-749a-45d1-9734-aba480cde6a7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models for Manipulation.}\nVision-language-action (VLA) models combine pretrained vision-language backbones with action prediction to produce generalist manipulation policies.\nRT-2~\\cite{brohan2023rt2} first demonstrated that VLM pretraining transfers to robotic control through action tokenization.\n$\\pi_0$~\\cite{black2024pi0} introduced flow matching~\\cite{lipman2023flow} for continuous action generation, and Diffusion Policy~\\cite{chi2023diffusionpolicy} showed that diffusion-based prediction handles multimodal demonstration distributions.\nOpenVLA~\\cite{kim2024openvla} provided an open-source 7B-parameter alternative trained on 970k real demonstrations.\nThese models share a common paradigm: pretrain a VLM, then fine-tune on demonstration data with parameter-efficient methods such as LoRA~\\cite{hu2022lora}.\nRecent work has enhanced VLA spatial reasoning through auxiliary 3D supervision.\nSpatial Forcing~\\cite{li2025spatialforcing} aligns intermediate visual embeddings with 3D geometry features; QDepth-VLA~\\cite{li2025qdepth} and DepthVLA~\\cite{depthvla2025} incorporate depth prediction as auxiliary tasks.\nDespite this progress, safety considerations remain largely absent from VLA training and evaluation.\nMost VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance behavior from incidental collision-free trajectories.\nThis paper examines whether standard collision avoidance metrics reliably capture safety behavior in VLA policies.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware robot learning spans training-time and test-time approaches.\nAt training time, constrained reinforcement learning methods optimize policies under explicit cost limits; SafeVLA~\\cite{zhang2025safevla} applies this framework to VLA policies through constrained MDP formulation, reducing safety violations by over 80\\%.\nAt test time, several methods apply external safety filters to learned policies.\nVLSA~\\cite{hu2025vlsa} attaches a control barrier function (CBF) layer to VLA outputs, overriding unsafe actions at inference.\nCoFreeVLA~\\cite{cofreeevla2026} uses a short-horizon collision risk estimator to gate dangerous dual-arm actions.\niKinQP-RL~\\cite{spalter2024ikinqp} corrects policy outputs through inverse kinematics quadratic programming.\nIn the diffusion policy setting, \\citet{li2024langguided} and CAPE~\\cite{yang2025cape} inject collision costs during the denoising process to steer trajectories away from obstacles.\nA recent survey~\\cite{li2026vlasafety} categorizes these methods into runtime shields, constrained optimization, and representation-based approaches.\nCommon to most is that safety is imposed through external mechanisms rather than learned within the policy's internal representations.\nThe end-to-end nature of VLAs, which map pixels and language directly to actions, makes it difficult to inject geometric constraints into learned features.\nThis work tests whether auxiliary SDF supervision during VLA training can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSigned distance functions (SDFs) encode the minimum distance from any query point to the nearest surface, with sign indicating free space or penetration.\nDeepSDF~\\cite{park2019deepsdf} showed that neural networks can represent continuous SDFs of 3D shapes.\nIn robotics, SDFs serve perception, planning, and control.\niSDF~\\cite{ortiz2022isdf} builds real-time neural distance fields from streaming depth images for scene understanding.\nVoxPoser~\\cite{huang2023voxposer} composes 3D value maps, including obstacle avoidance fields, to guide manipulation through language.\nFor motion planning, RAMP~\\cite{vasilopoulos2023ramp} uses implicit SDFs within reactive controllers, and DiffCo~\\cite{zhi2021diffco} provides fully differentiable collision detection for gradient-based trajectory optimization.\nRecent work extends SDFs beyond task space: CSSDF-Net~\\cite{chen2026cssdfnet} estimates configuration-space distance fields for whole-body collision checking, and Neural NMPC~\\cite{jacquet2025neuralnmpc} encodes SDF constraints directly into model predictive control.\nThese works demonstrate the effectiveness of distance fields in classical planning and control pipelines, but their integration into end-to-end learned policies remains unexplored.\nWe evaluate SDF as an auxiliary training loss during VLA fine-tuning to determine whether geometric distance supervision can teach flow-matching policies to avoid collisions.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nEvaluation of manipulation safety requires metrics beyond binary task success.\nLIBERO~\\cite{liu2023libero} established a standardized benchmark for lifelong robot learning with four task suites.\nSafeLIBERO, introduced by \\citet{hu2025vlsa}, extends LIBERO with obstacle-augmented environments and a collision avoidance rate (CAR) metric, defined as the fraction of episodes without any collision.\nTask success rate (TSR) and CAR together aim to capture the safety-capability tradeoff.\nHowever, CAR treats all collision-free episodes identically regardless of the robot's behavior: a frozen robot that never moves scores perfect CAR, and a capable robot whose trajectory happens to miss obstacles also registers high CAR.\nNeither case reflects learned avoidance behavior.\nThis failure mode echoes broader concerns about metric reliability.\nGoodhart's law in RL~\\cite{karwowski2024goodhart} shows that optimizing a proxy metric can diverge from the true objective, and annotation artifacts~\\cite{gururangan2018annotation} demonstrate how superficial correlations inflate benchmark scores.\nRecent work on statistically rigorous robot evaluation~\\cite{snyder2026beyond} further highlights the fragility of binary success metrics under limited sample sizes.\nWe propose displacement-filtered CAR ($\\dfCAR$, \\S\\ref{sec:dfcar}), which excludes episodes where end-effector displacement falls below a motion threshold, to remove action collapse artifacts and isolate genuine avoidance behavior.\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

Now let me run the verification checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "98659aa7-b577-4f4f-a387-966809faf1ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Sm9q8PLW7xHERuv6gJaU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 63868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1687
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

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_019KAkkDELphTMerPhihihoW`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper && wc -w related_work.tex",
  "description": "Count words in related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "0dbfa5e5-4f2c-4bcd-b917-a071800f9c15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Sm9q8PLW7xHERuv6gJaU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 63868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1687
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

_source line 48 · 2026-05-26T16:16:32.067Z_

<details><summary>↩ Tool result · `toolu_019KAkkDELphTMerPhihihoW`</summary>

```text
706 related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "22de21d0-f286-4411-933e-2b331ca13787",
  "tool_use_result": {
    "stdout": "706 related_work.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vax4cRR7723LY71ScRhaZQ`</summary>

```json
{
  "command": "grep -n \"—\\|–\" related_work.tex || echo \"NO_DASHES\"",
  "description": "Check for em-dash and en-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "8c893da8-4e74-4ca3-a0b5-63b3e2192e8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Sm9q8PLW7xHERuv6gJaU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 63868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1687
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

_source line 50 · 2026-05-26T16:16:33.434Z_

<details><summary>↩ Tool result · `toolu_01Vax4cRR7723LY71ScRhaZQ`</summary>

```text
NO_DASHES
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "713ccd96-bd38-4e62-b869-1467f040bca8",
  "tool_use_result": {
    "stdout": "NO_DASHES",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_01WakXLftcZMUWYqCBfTHBeT`</summary>

```json
{
  "command": "grep -inE \"significantly|crucial|notably|leverage|utilize|delve|myriad|plethora|paradigm shift|in the realm of\" related_work.tex || echo \"NO_AI_WORDS\"",
  "description": "Check for AI style words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "14d8b1de-b833-4e45-b16e-fa0bd84d11dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Sm9q8PLW7xHERuv6gJaU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1687,
      "cache_read_input_tokens": 63868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1687
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

_source line 52 · 2026-05-26T16:16:35.433Z_

<details><summary>↩ Tool result · `toolu_01WakXLftcZMUWYqCBfTHBeT`</summary>

```text
NO_AI_WORDS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "666c8ec6-678a-4b7e-98c6-0af1c58a23be",
  "tool_use_result": {
    "stdout": "NO_AI_WORDS",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01FqrDqbTSqazxLKhvCXaLCV`</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u | while read key; do grep -q \"^@.*{${key},\" references.bib && echo \"OK: $key\" || echo \"MISSING: $key\"; done",
  "description": "Verify all cite keys exist in bib file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "53330721-4857-4914-9dfa-589a14d17ca3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LxSSnZPeQeCt1G2fdDkpp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 65555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
      },
      "output_tokens": 66,
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

_source line 54 · 2026-05-26T16:16:41.986Z_

<details><summary>↩ Tool result · `toolu_01FqrDqbTSqazxLKhvCXaLCV`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "2b8ab0ee-3fdb-40c3-9eba-778a38e4dca6",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01QDYy3fHZJKdPB2k8pfq55D`</summary>

```json
{
  "command": "grep -nP '^\\s*[A-Z][a-z]*ing\\b' related_work.tex || echo \"NO_ING_STARTS\"",
  "description": "Check for -ing opening sentences"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "f800067b-7bf3-45ef-a21d-78c7b431a5f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LxSSnZPeQeCt1G2fdDkpp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 65555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
      },
      "output_tokens": 66,
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

_source line 56 · 2026-05-26T16:16:43.239Z_

<details><summary>↩ Tool result · `toolu_01QDYy3fHZJKdPB2k8pfq55D`</summary>

```text
NO_ING_STARTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "a0eb6543-8c59-4ec9-b21a-fcc22bc66879",
  "tool_use_result": {
    "stdout": "NO_ING_STARTS",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01XMTq68nMtGvGBpbwMtrukC`</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u | while read key; do if grep -q \"{${key},\" references.bib; then echo \"OK: $key\"; else echo \"MISSING: $key\"; fi; done",
  "description": "Verify all cite keys exist in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "8fa761f1-f3f9-4ef9-b703-50a860b5ca36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHZ5AqULkFCgyuksdkhVQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 65972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
      },
      "output_tokens": 66,
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

_source line 58 · 2026-05-26T16:16:46.839Z_

<details><summary>↩ Tool result · `toolu_01XMTq68nMtGvGBpbwMtrukC`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "c58d8508-4f73-483b-8059-00343bde07e3",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01PZbXW23RSw18wxTCZ3iatK`</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u",
  "description": "List all cite keys used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "863539f1-dae0-417d-a9ed-d20dceb2950c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNHPxCQ6LGgSZQuwQjGDQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 193,
      "cache_read_input_tokens": 66313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 193
      },
      "output_tokens": 66,
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

_source line 60 · 2026-05-26T16:16:50.616Z_

<details><summary>↩ Tool result · `toolu_01PZbXW23RSw18wxTCZ3iatK`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "26780153-692c-4780-b3f4-b529151b02f9",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_01TCZT36oV7KYsoK3ZAzGsjt`</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | sed 's/\\\\cite[tp]\\{//;s/\\\\cite{//;s/}//' | tr ',' '\\n' | sort -u",
  "description": "Extract all cite keys from related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "80e74c64-3d58-4923-8dff-0334eb139fb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VafNc3ygjpjguKr3mq12KW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 66506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 251
      },
      "output_tokens": 37,
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

_source line 62 · 2026-05-26T16:17:02.183Z_

<details><summary>↩ Tool result · `toolu_01TCZT36oV7KYsoK3ZAzGsjt`</summary>

```text
sed: -e expression #1, char 17: Unmatched \{
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "3991a328-ccab-49d1-99ce-3b6cfcc3428a",
  "tool_use_result": {
    "stdout": "sed: -e expression #1, char 17: Unmatched \\{",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01KHctUfgCqJJAxZFEskgi3h`</summary>

```json
{
  "command": "python3 -c \"\nimport re\nwith open('related_work.tex') as f:\n    text = f.read()\nkeys = re.findall(r'\\\\\\\\cite[tp]?\\{([^}]+)\\}', text)\nall_keys = set()\nfor k in keys:\n    for sub in k.split(','):\n        all_keys.add(sub.strip())\n\nwith open('references.bib') as f:\n    bib = f.read()\n\nfor key in sorted(all_keys):\n    if '{' + key + ',' in bib:\n        print(f'OK: {key}')\n    else:\n        print(f'MISSING: {key}')\n\"",
  "description": "Verify cite keys against bib using Python"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "30d06403-996c-4523-8e09-6716e83e76b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtEYXP6ViruTQ7w8QqsSEV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 66757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 166
      },
      "output_tokens": 37,
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

_source line 64 · 2026-05-26T16:17:08.764Z_

<details><summary>↩ Tool result · `toolu_01KHctUfgCqJJAxZFEskgi3h`</summary>

```text
OK: black2024pi0
OK: brohan2023rt2
OK: chen2026cssdfnet
OK: chi2023diffusionpolicy
OK: cofreeevla2026
OK: depthvla2025
OK: gururangan2018annotation
OK: hu2022lora
OK: hu2025vlsa
OK: huang2023voxposer
OK: jacquet2025neuralnmpc
OK: karwowski2024goodhart
OK: kim2024openvla
OK: li2024langguided
OK: li2025qdepth
OK: li2025spatialforcing
OK: li2026vlasafety
OK: lipman2023flow
OK: liu2023libero
OK: ortiz2022isdf
OK: park2019deepsdf
OK: snyder2026beyond
OK: spalter2024ikinqp
OK: vasilopoulos2023ramp
OK: yang2025cape
OK: zhang2025safevla
OK: zhi2021diffco
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "a58eca9a-28fb-4ff3-b87e-8157d06b9092",
  "tool_use_result": {
    "stdout": "OK: black2024pi0\nOK: brohan2023rt2\nOK: chen2026cssdfnet\nOK: chi2023diffusionpolicy\nOK: cofreeevla2026\nOK: depthvla2025\nOK: gururangan2018annotation\nOK: hu2022lora\nOK: hu2025vlsa\nOK: huang2023voxposer\nOK: jacquet2025neuralnmpc\nOK: karwowski2024goodhart\nOK: kim2024openvla\nOK: li2024langguided\nOK: li2025qdepth\nOK: li2025spatialforcing\nOK: li2026vlasafety\nOK: lipman2023flow\nOK: liu2023libero\nOK: ortiz2022isdf\nOK: park2019deepsdf\nOK: snyder2026beyond\nOK: spalter2024ikinqp\nOK: vasilopoulos2023ramp\nOK: yang2025cape\nOK: zhang2025safevla\nOK: zhi2021diffco",
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

_source line 65_

验证结果：

| 检查项 | 结果 |
|--------|------|
| Word count | 706 (在 600-800 范围内) |
| Em-dash / en-dash | 无 |
| AI 风格词汇 | 无 |
| -ing 开头句 | 无 |
| \cite key 全部存在于 .bib | 27/27 全部通过 |
| 每段末尾关联本文 | 4/4 段均有 |

文件已写入 `docs/paper/related_work.tex`。4 段结构：VLA for Manipulation (10 refs) → Safety in Robot Learning (7 refs) → SDF in Robotics (7 refs) → Evaluation Metrics (5 refs)，共 27 个引用，均已验证存在于 references.bib。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "uuid": "de6fe144-7510-432a-93c1-6f77aff7177a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhZfhX48SdRH1igHCYdZnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 66923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
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

_source line 66_

验证结果：

| 检查项 | 结果 |
|--------|------|
| Word count | 706 (在 600-800 范围内) |
| Em-dash / en-dash | 无 |
| AI 风格词汇 | 无 |
| -ing 开头句 | 无 |
| \cite key 全部存在于 .bib | 27/27 全部通过 |
| 每段末尾关联本文 | 4/4 段均有 |

文件已写入 `docs/paper/related_work.tex`。4 段结构：VLA for Manipulation (10 refs) → Safety in Robot Learning (7 refs) → SDF in Robotics (7 refs) → Evaluation Metrics (5 refs)，共 27 个引用，均已验证存在于 references.bib。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 327528,
  "duration_api_ms": 328270,
  "num_turns": 26,
  "stop_reason": "end_turn",
  "session_id": "a7f5a338-e01a-4e66-8d9b-7a26f7967b85",
  "total_cost_usd": 1.2375455,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 55586,
    "cache_read_input_tokens": 1057362,
    "output_tokens": 14372,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 55586,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 230,
        "cache_read_input_tokens": 66923,
        "cache_creation_input_tokens": 504,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 504
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1957,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002042,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 22,
      "outputTokens": 14372,
      "cacheReadInputTokens": 1057362,
      "cacheCreationInputTokens": 55586,
      "webSearchRequests": 0,
      "costUSD": 1.2355035,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "de81ad38-be05-4dde-91b1-82e615278b1b"
}
```

</details>

---
