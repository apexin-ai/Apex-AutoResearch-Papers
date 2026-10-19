# paper 8b scale results

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_8b-scale-results_20260520T131942.log`
- **Structured JSON:** [`75170d77e35745c8f497.json`](../../sessions/75/75170d77e35745c8f497.json)

## Before a recorded user message

28 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
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
  "uuid": "a0fa7aae-c8a9-46a2-b8d2-0de7f5c27c90",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1779300600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ddb48c9c-1580-4698-b961-b4cfde94f4ea",
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75"
}
```

---

### Assistant

_source line 4_

I'll start by reading the paper writing norms and finding the experiments.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "8d85ff09-f553-4c49-a55f-31179486caa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y3cLxAyRcmiX52dtGWDj8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13051,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13051
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

<details open><summary>🔧 Tool call — Read · `toolu_019HQbMbGmVopx2LPvq2Kqp4`</summary>

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
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "4bf026b8-d685-4e30-895a-e3402cf53bc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y3cLxAyRcmiX52dtGWDj8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13051,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13051
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

_source line 6 · 2026-05-20T13:19:55.570Z_

<details><summary>↩ Tool result · `toolu_019HQbMbGmVopx2LPvq2Kqp4`</summary>

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
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "f1979797-1fea-49fe-9c8a-8853be2cd8e5",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01WKHFEasU2NeiFvrsi4ubKu`</summary>

```json
{
  "pattern": "**/experiments.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "ad6c18ff-2e01-453c-9818-4367d4a7223f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y3cLxAyRcmiX52dtGWDj8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13051,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13051
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

_source line 8 · 2026-05-20T13:19:56.162Z_

<details><summary>↩ Tool result · `toolu_01WKHFEasU2NeiFvrsi4ubKu`</summary>

```text
docs/paper/experiments.tex
artifacts/_project/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "42d00c22-0773-459f-bbde-d7c26881fbd6",
  "tool_use_result": {
    "filenames": [
      "docs/paper/experiments.tex",
      "artifacts/_project/paper/experiments.tex"
    ],
    "durationMs": 12,
    "numFiles": 2,
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
Found two experiments.tex files. Let me read the one in artifacts/_project/paper/ since that's the one mentioned in the user's instructions, and also check the docs/paper/ one.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "8c61fa70-dc04-4ad3-89eb-695c7ef3e8dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014n7d5QFcEGfjiumFtQPvpM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5745,
      "cache_read_input_tokens": 24752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5745
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

Found two files. Let me read both to understand the current content and style.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "f86164d9-d9ad-4240-84c2-509ece87156f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014n7d5QFcEGfjiumFtQPvpM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5745,
      "cache_read_input_tokens": 24752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5745
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

<details open><summary>🔧 Tool call — Read · `toolu_01KmE5txPLGcxtj1dgXq8dcy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "d65337ce-80e9-45d4-9010-0aa2c4b9ab99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014n7d5QFcEGfjiumFtQPvpM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5745,
      "cache_read_input_tokens": 24752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5745
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

_source line 12 · 2026-05-20T13:20:03.193Z_

<details><summary>↩ Tool result · `toolu_01KmE5txPLGcxtj1dgXq8dcy`</summary>

```text
1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\ref{sec:m2_sign_misattribution}?
7	
8	\subsection{Experimental Setup}
9	\label{sec:experimental_setup}
10	
11	\paragraph{Environment.}
12	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands. % TODO: add shridhar2021alfworld to .bib
13	ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R = 1$ for successful task completion and $R = 0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.
14	
15	ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.
16	
17	\paragraph{Base model.}
18	We use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves approximately 6.25\% success rate on a held-out 32-episode validation set, providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.0625$ with group size $K = 8$, Proposition 2 (Section~\ref{sec:formal_probability}) predicts that approximately 84.5\% of gradient updates carry incorrect sign under step-independent training.
19	
20	\paragraph{RL training configuration.}
21	We train using the RAGEN framework~\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:
22	\begin{itemize}
23	    \item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)
24	    \item Learning rate: $1 \times 10^{-6}$
25	    \item KL penalty coefficient: $\beta = 0.01$ (low-variance KL)
26	    \item Discount factor: $\gamma = 0.95$ (applied in step-independent return computation via Equation~\ref{eq:step_return}; not applicable to episode-level mode)
27	    \item Invalid action penalty coefficient: 0.1
28	    \item Training data: 16 task instances per training step
29	    \item Training steps: 15 (early-stopped based on convergence)
30	\end{itemize}
31	
32	\paragraph{Evaluation protocol.}
33	We evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \in \{2, 4, 8\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.
34	
35	\subsection{Window-Size Ablation}
36	\label{sec:window_ablation}
37	
38	To disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.
39	
40	\paragraph{Conditions.}
41	We vary the step-independent history length $h \in \{2, 5, 10, 20\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \texttt{step\_independent} training mode with \texttt{step\_independent\_history\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.
42	
43	\paragraph{Design rationale.}
44	The five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.
45	
46	\paragraph{Controls.}
47	All conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. All $h$-sweep conditions are currently single-seed. Multi-seed replication (3 seeds per $h$) is planned.% Sources: exp028c ($h=2$), exp029 (episode-level).
48	
49	\paragraph{Post-hoc evaluation.}
50	To isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).
51	
52	\subsection{Results}
53	\label{sec:results}
54	
55	\subsubsection{Episode-Level vs. Step-Independent Training}
56	\label{sec:results_main}
57	
58	The central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\% validation success at training step 15, a 4.5$\times$ improvement over the SFT baseline of approximately 6.25\%. Step-independent training with $h = 2$ collapses to 0\% validation success by step 10.
59	
60	Table~\ref{tab:main_results} summarizes the central comparison. All seed results are reported individually due to high inter-seed variance under step-independent conditions.
61	
62	\begin{table}[t]
63	\centering
64	\caption{1.7B ALFWorld results across credit assignment methods. OOD: held-out test tasks; In-Dist: 32-episode validation set. All seeds shown; no aggregation due to high inter-seed variance.}
65	\label{tab:main_results}
66	\small
67	\begin{tabular}{@{}llcc@{}}
68	\toprule
69	\textbf{Method} & \textbf{Seed} & \textbf{OOD (\%)} & \textbf{In-Dist (\%)} \\
70	\midrule
71	Step-indep.\ ($h{=}2$, windowed) & 1 & 0 & 0 \\  % Cell A
72	                                  & 2 & 3.73 & 9.375 \\  % Cell A seed2
73	\midrule
74	Step-indep.\ (factorial)          & 1 & 0.75 & 20 \\  % Cell B
75	                                  & 2 & 0.75 & 55.5 \\  % Cell B seed2
76	\midrule
77	Episode-level (full context)      & 1 & 23.88 & 28.125 \\  % Cell C, exp029
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	\placeholder{fig6\_training\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}
83	
84	The collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), task success drops from 18.75\% to single digits while action validity remains high at approximately 89.3\%. The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), action validity itself collapses from 89.3\% to 43.1\%. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.
85	
86	Episode-level training exhibits no such collapse. Action validity remains above 95\% throughout training, and success rate increases monotonically. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.
87	
88	\subsubsection{Window-Size Ablation}
89	\label{sec:results_hsweep}
90	
91	\begin{table}[t]
92	\centering
93	\caption{Window-size ablation (1.7B, single seed). OOD success rate at the final training step. $h = \text{full}$ denotes episode-level training (exp029).}
94	\label{tab:h_sweep}
95	\small
96	\begin{tabular}{@{}lc@{}}
97	\toprule
98	\textbf{Window size $h$} & \textbf{OOD Success (\%)} \\
99	\midrule
100	$h = 2$  & 0 \\
101	$h = 5$  & 0 \\
102	$h = 10$ & 6.25 \\
103	$h = 20$ & 15.6 \\
104	$h = \text{full}$ (episode-level) & 23.88 \\
105	\bottomrule
106	\end{tabular}
107	\end{table}
108	
109	\placeholder{fig5\_h\_sweep\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (6.25\%).}
110	
111	The ablation reveals a credit assignment cliff consistent with our theoretical predictions (Table~\ref{tab:h_sweep}). OOD success rate is 0\% for $h \leq 5$, rises to 6.25\% at $h = 10$ and 15.6\% at $h = 20$, and reaches 23.88\% under episode-level training ($h = T$). The transition between $h = 5$ and $h = 10$ marks the onset of non-trivial generalization. Results are single-seed; multi-seed replication is in progress.
112	
113	The dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.
114	
115	From the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Action validity at step 2 is 89.3\%, dropping to 43.1\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.
116	
117	\subsubsection{Dense Reward Baseline}
118	\label{sec:results_dense}
119	
120	A natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.
121	
122	The dense reward experiment (exp013f) produces a striking dissociation. Action validity increases from 60\% to 97.5\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, task success remains at 0\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.
123	
124	This result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.
125	
126	\subsection{Empirical Verification of Sign Misattribution}
127	\label{sec:sign_verification}
128	
129	The theoretical analysis of Section~\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions.
130	
131	\paragraph{Methodology.}
132	During step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\text{sign}(\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\text{episode}}^{(i)} \in \{0, 1\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:
133	\begin{itemize}
134	    \item \textbf{Sign-outcome correlation}: the Pearson correlation between $\text{sign}(\hat{A}_k)$ and $R_{\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.
135	    \item \textbf{Sign-quality correlation}: the Pearson correlation between $\text{sign}(\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.
136	    \item \textbf{Correct sign fraction}: $P(\text{correct sign} \mid \text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\ref{sec:formal_probability}) predicts this equals approximately 15.5\% at $p = 6.25\%$, $K = 8$.
137	\end{itemize}
138	
139	\paragraph{Predictions.}
140	The sign misattribution mechanism makes three testable predictions:
141	\begin{enumerate}
142	    \item Sign-outcome correlation $\approx 1.0$ (advantage sign is a proxy for episode success, not local quality)
143	    \item Sign-quality correlation $\approx 0$ (advantage sign is independent of whether local actions were good)
144	    \item $P(\text{correct sign}) \approx 15.5\%$ (derived from Proposition 2 at the observed success rate)
145	\end{enumerate}
146	If all three predictions are confirmed empirically, the sign misattribution mechanism is validated as the causal driver of training collapse, rather than alternative explanations such as reward sparsity, KL divergence, or optimization instability.
147	
148	Table~\ref{tab:sign_verification} reports the empirical measurements. The credit agreement rate---the fraction of windows where the advantage sign matches local action quality---is 52.07\%, indistinguishable from the 50\% expected under random sign assignment. The point biserial correlation between advantage sign and local action quality is $r = 0.068$, confirming near-zero dependence. Additionally, a discount factor sweep reveals that \textit{all} $\gamma$ values produce collapse, including $\gamma = 1.0$ (no discounting). The $\gamma = 1.0$ result rules out temporal discounting as the failure cause and isolates sign misattribution as the root mechanism.
149	
150	\begin{table}[t]
151	\centering
152	\caption{Empirical verification of sign misattribution under step-independent training ($h{=}2$). Credit agreement rate measures the fraction of windows where advantage sign matches local action quality; 50\% indicates random assignment.}
153	\label{tab:sign_verification}
154	\small
155	\begin{tabular}{@{}lcc@{}}
156	\toprule
157	\textbf{Metric} & \textbf{Measured} & \textbf{Predicted} \\
158	\midrule
159	Credit agreement rate & 52.07\% & $\approx$ 50\% (random) \\
160	Point biserial $r$ (sign vs.\ quality) & 0.068 & $\approx$ 0 \\
161	Collapse at $\gamma = 1.0$ (no discounting) & Yes & Yes \\
162	\bottomrule
163	\end{tabular}
164	\end{table}
165	
166	\subsection{Additional Baselines}
167	\label{sec:additional_baselines}
168	
169	\paragraph{GAE baselines.}
170	To distinguish the effect of episode-level optimization from GRPO-specific design choices (group normalization, no value function), we compare against Generalized Advantage Estimation (GAE)~\cite{schulman2016gae} under two configurations. GAE($\lambda = 0.95$, $\gamma = 0.95$) provides standard TD-based advantage estimation with a learned value function, representing the conventional actor-critic approach to temporal credit assignment. GAE($\lambda = 1$, $\gamma = 1$) computes Monte Carlo returns equivalent to episode-level GRPO without group normalization, isolating the contribution of group-relative advantage computation. \placeholder{plan\_003b: GAE baseline execution. Columns: Method, Val Success (\%), Action Valid (\%), Training Stability (variance across steps).}
171	
172	\paragraph{Selective verification.}
173	Building on the episode-level trained agent (Section~\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \placeholder{tab4\_selective\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\%), Verify Rate (\%), Cost Reduction (\%). Pending Phase B experiments.}
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "a00c353c-72a8-474d-803d-98bb2034e4d4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
      "content": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\\ref{sec:m2_sign_misattribution}?\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\n\\paragraph{Environment.}\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands. % TODO: add shridhar2021alfworld to .bib\nALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R = 1$ for successful task completion and $R = 0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.\n\nALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.\n\n\\paragraph{Base model.}\nWe use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves approximately 6.25\\% success rate on a held-out 32-episode validation set, providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.0625$ with group size $K = 8$, Proposition 2 (Section~\\ref{sec:formal_probability}) predicts that approximately 84.5\\% of gradient updates carry incorrect sign under step-independent training.\n\n\\paragraph{RL training configuration.}\nWe train using the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:\n\\begin{itemize}\n    \\item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)\n    \\item Learning rate: $1 \\times 10^{-6}$\n    \\item KL penalty coefficient: $\\beta = 0.01$ (low-variance KL)\n    \\item Discount factor: $\\gamma = 0.95$ (applied in step-independent return computation via Equation~\\ref{eq:step_return}; not applicable to episode-level mode)\n    \\item Invalid action penalty coefficient: 0.1\n    \\item Training data: 16 task instances per training step\n    \\item Training steps: 15 (early-stopped based on convergence)\n\\end{itemize}\n\n\\paragraph{Evaluation protocol.}\nWe evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \\in \\{2, 4, 8\\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \\textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.\n\n\\subsection{Window-Size Ablation}\n\\label{sec:window_ablation}\n\nTo disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.\n\n\\paragraph{Conditions.}\nWe vary the step-independent history length $h \\in \\{2, 5, 10, 20\\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \\texttt{step\\_independent} training mode with \\texttt{step\\_independent\\_history\\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.\n\n\\paragraph{Design rationale.}\nThe five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.\n\n\\paragraph{Controls.}\nAll conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. All $h$-sweep conditions are currently single-seed. Multi-seed replication (3 seeds per $h$) is planned.% Sources: exp028c ($h=2$), exp029 (episode-level).\n\n\\paragraph{Post-hoc evaluation.}\nTo isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).\n\n\\subsection{Results}\n\\label{sec:results}\n\n\\subsubsection{Episode-Level vs. Step-Independent Training}\n\\label{sec:results_main}\n\nThe central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\\% validation success at training step 15, a 4.5$\\times$ improvement over the SFT baseline of approximately 6.25\\%. Step-independent training with $h = 2$ collapses to 0\\% validation success by step 10.\n\nTable~\\ref{tab:main_results} summarizes the central comparison. All seed results are reported individually due to high inter-seed variance under step-independent conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{1.7B ALFWorld results across credit assignment methods. OOD: held-out test tasks; In-Dist: 32-episode validation set. All seeds shown; no aggregation due to high inter-seed variance.}\n\\label{tab:main_results}\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed} & \\textbf{OOD (\\%)} & \\textbf{In-Dist (\\%)} \\\\\n\\midrule\nStep-indep.\\ ($h{=}2$, windowed) & 1 & 0 & 0 \\\\  % Cell A\n                                  & 2 & 3.73 & 9.375 \\\\  % Cell A seed2\n\\midrule\nStep-indep.\\ (factorial)          & 1 & 0.75 & 20 \\\\  % Cell B\n                                  & 2 & 0.75 & 55.5 \\\\  % Cell B seed2\n\\midrule\nEpisode-level (full context)      & 1 & 23.88 & 28.125 \\\\  % Cell C, exp029\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\placeholder{fig6\\_training\\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}\n\nThe collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), task success drops from 18.75\\% to single digits while action validity remains high at approximately 89.3\\%. The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), action validity itself collapses from 89.3\\% to 43.1\\%. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.\n\nEpisode-level training exhibits no such collapse. Action validity remains above 95\\% throughout training, and success rate increases monotonically. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.\n\n\\subsubsection{Window-Size Ablation}\n\\label{sec:results_hsweep}\n\n\\begin{table}[t]\n\\centering\n\\caption{Window-size ablation (1.7B, single seed). OOD success rate at the final training step. $h = \\text{full}$ denotes episode-level training (exp029).}\n\\label{tab:h_sweep}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\n\\textbf{Window size $h$} & \\textbf{OOD Success (\\%)} \\\\\n\\midrule\n$h = 2$  & 0 \\\\\n$h = 5$  & 0 \\\\\n$h = 10$ & 6.25 \\\\\n$h = 20$ & 15.6 \\\\\n$h = \\text{full}$ (episode-level) & 23.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\placeholder{fig5\\_h\\_sweep\\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (6.25\\%).}\n\nThe ablation reveals a credit assignment cliff consistent with our theoretical predictions (Table~\\ref{tab:h_sweep}). OOD success rate is 0\\% for $h \\leq 5$, rises to 6.25\\% at $h = 10$ and 15.6\\% at $h = 20$, and reaches 23.88\\% under episode-level training ($h = T$). The transition between $h = 5$ and $h = 10$ marks the onset of non-trivial generalization. Results are single-seed; multi-seed replication is in progress.\n\nThe dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.\n\nFrom the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Action validity at step 2 is 89.3\\%, dropping to 43.1\\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.\n\n\\subsubsection{Dense Reward Baseline}\n\\label{sec:results_dense}\n\nA natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.\n\nThe dense reward experiment (exp013f) produces a striking dissociation. Action validity increases from 60\\% to 97.5\\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, task success remains at 0\\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.\n\nThis result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.\n\n\\subsection{Empirical Verification of Sign Misattribution}\n\\label{sec:sign_verification}\n\nThe theoretical analysis of Section~\\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions.\n\n\\paragraph{Methodology.}\nDuring step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\\text{sign}(\\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\\text{episode}}^{(i)} \\in \\{0, 1\\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:\n\\begin{itemize}\n    \\item \\textbf{Sign-outcome correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and $R_{\\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.\n    \\item \\textbf{Sign-quality correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.\n    \\item \\textbf{Correct sign fraction}: $P(\\text{correct sign} \\mid \\text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\\ref{sec:formal_probability}) predicts this equals approximately 15.5\\% at $p = 6.25\\%$, $K = 8$.\n\\end{itemize}\n\n\\paragraph{Predictions.}\nThe sign misattribution mechanism makes three testable predictions:\n\\begin{enumerate}\n    \\item Sign-outcome correlation $\\approx 1.0$ (advantage sign is a proxy for episode success, not local quality)\n    \\item Sign-quality correlation $\\approx 0$ (advantage sign is independent of whether local actions were good)\n    \\item $P(\\text{correct sign}) \\approx 15.5\\%$ (derived from Proposition 2 at the observed success rate)\n\\end{enumerate}\nIf all three predictions are confirmed empirically, the sign misattribution mechanism is validated as the causal driver of training collapse, rather than alternative explanations such as reward sparsity, KL divergence, or optimization instability.\n\nTable~\\ref{tab:sign_verification} reports the empirical measurements. The credit agreement rate---the fraction of windows where the advantage sign matches local action quality---is 52.07\\%, indistinguishable from the 50\\% expected under random sign assignment. The point biserial correlation between advantage sign and local action quality is $r = 0.068$, confirming near-zero dependence. Additionally, a discount factor sweep reveals that \\textit{all} $\\gamma$ values produce collapse, including $\\gamma = 1.0$ (no discounting). The $\\gamma = 1.0$ result rules out temporal discounting as the failure cause and isolates sign misattribution as the root mechanism.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical verification of sign misattribution under step-independent training ($h{=}2$). Credit agreement rate measures the fraction of windows where advantage sign matches local action quality; 50\\% indicates random assignment.}\n\\label{tab:sign_verification}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Measured} & \\textbf{Predicted} \\\\\n\\midrule\nCredit agreement rate & 52.07\\% & $\\approx$ 50\\% (random) \\\\\nPoint biserial $r$ (sign vs.\\ quality) & 0.068 & $\\approx$ 0 \\\\\nCollapse at $\\gamma = 1.0$ (no discounting) & Yes & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Additional Baselines}\n\\label{sec:additional_baselines}\n\n\\paragraph{GAE baselines.}\nTo distinguish the effect of episode-level optimization from GRPO-specific design choices (group normalization, no value function), we compare against Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} under two configurations. GAE($\\lambda = 0.95$, $\\gamma = 0.95$) provides standard TD-based advantage estimation with a learned value function, representing the conventional actor-critic approach to temporal credit assignment. GAE($\\lambda = 1$, $\\gamma = 1$) computes Monte Carlo returns equivalent to episode-level GRPO without group normalization, isolating the contribution of group-relative advantage computation. \\placeholder{plan\\_003b: GAE baseline execution. Columns: Method, Val Success (\\%), Action Valid (\\%), Training Stability (variance across steps).}\n\n\\paragraph{Selective verification.}\nBuilding on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}\n",
      "numLines": 174,
      "startLine": 1,
      "totalLines": 174
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01Y53DpQAkd9cdv4jqe937o4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "efbbd186-3c66-4c9c-a87a-edb98d2161b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014n7d5QFcEGfjiumFtQPvpM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5745,
      "cache_read_input_tokens": 24752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5745
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

_source line 14 · 2026-05-20T13:20:03.281Z_

<details><summary>↩ Tool result · `toolu_01Y53DpQAkd9cdv4jqe937o4`</summary>

```text
1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?
7	
8	\subsection{Environment}
9	\label{sec:environment}
10	
11	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \texttt{go to countertop 1}, \texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \in \{0, r_+\}$, with $r_+$ awarded only upon successful task completion.
12	
13	ALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.
14	
15	\subsection{Base Model and Supervised Fine-Tuning}
16	\label{sec:base_model}
17	
18	We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.
19	
20	This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\ref{prop:correct_sign} predicts that approximately 80.9\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint therefore occupies the regime where sign misattribution is most severe.
21	
22	\subsection{RL Training Configuration}
23	\label{sec:rl_config}
24	
25	All conditions use the RAGEN framework~\cite{ragen2025} with the GRPO algorithm~\cite{shao2024deepseekmath}. Table~\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\gamma$ applies only to step-independent return computation (Equation~\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.
26	
27	\begin{table}[t]
28	\centering
29	\small
30	\caption{Shared RL training hyperparameters across all conditions.}
31	\label{tab:hyperparameters}
32	\begin{tabular}{lc}
33	\toprule
34	Parameter & Value \\
35	\midrule
36	Group size $K$ & 8 \\
37	Learning rate & $1 \times 10^{-6}$ \\
38	KL penalty $\beta$ & 0.01 \\
39	Discount $\gamma$ & 0.95 \\
40	Invalid action penalty & 0.1 \\
41	Tasks per training step & 16 \\
42	Training steps & 15 \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	\subsection{Evaluation Protocol}
48	\label{sec:eval_protocol}
49	
50	We evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.
51	
52	The primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \in \{2, 4, 8\}$. As a diagnostic, we track \textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. Results report single-seed or two-seed runs depending on availability; seed counts are noted per condition.
53	
54	\subsection{Factorial Mechanism Separation}
55	\label{sec:factorial_experiments}
56	
57	The dual-mechanism analysis (Section~\ref{sec:dual_mechanism}) predicts that information loss (M1) and sign misattribution (M2) produce qualitatively different training failures. To separate their effects, we implement the $2 \times 2$ factorial design described in Section~\ref{sec:factorial_design}, varying two factors: observation scope (truncated window vs.\ full trajectory) and advantage scope (per-window vs.\ episode-level).
58	
59	\paragraph{Cell A: Truncated observation + step-level advantage.}
60	Window size $h{=}2$ with per-window advantage computation. Both mechanisms are active: the policy observes only 2-step windows (M1) and each window receives an advantage whose sign is determined by the episode outcome rather than local action quality (M2). This is the default RAGEN configuration and represents the community standard for multi-turn agent RL. Two seeds.
61	
62	\paragraph{Cell B: Truncated observation + episode-level advantage.}
63	Window size $h{=}2$, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (observations are still truncated to 2-step windows), while M2 is eliminated (all windows receive the same advantage sign, so no individual window can be misattributed). The comparison of Cell~A against Cell~B isolates the contribution of sign misattribution: any difference in training stability is attributable to M2 alone. Two seeds.
64	
65	\paragraph{Cell D: Full observation + episode-level advantage.}
66	The complete trajectory is processed as a single sequence with one shared advantage. Neither mechanism is active: the full context eliminates information loss, and the single advantage eliminates sign misattribution. The comparison of Cell~B against Cell~D isolates the contribution of information loss: any performance gap reflects how truncated context limits the policy's ability to learn cross-step strategies. Two seeds.
67	
68	The fourth cell (full observation + step-level advantage) is degenerate: with full context, only one window spans the entire episode, so per-window and episode-level advantage coincide. The factorial design therefore yields three distinct conditions that test qualitative predictions about training dynamics, not quantitative effect decomposition (Section~\ref{sec:factorial_design}).
69	
70	\subsection{Additional Experimental Conditions}
71	\label{sec:additional_conditions}
72	
73	\paragraph{Dense reward baseline.}
74	Step-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.
75	
76	\paragraph{REINFORCE++ baseline.}
77	Episode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used.\footnote{This condition was originally planned as a GAE baseline with a learned value function. We substituted REINFORCE++ after TRL~1.1.0 removed the \texttt{AutoModelForCausalLMWithValueHead} class required for critic-based methods.}
78	
79	\paragraph{Discount factor sweep.}
80	Step-independent $h{=}5$ with $\gamma \in \{0.50, 0.80, 0.95, 1.00\}$. This sweep isolates the role of magnitude decay in training collapse. At $\gamma = 1.0$, all windows receive identical return magnitude from the terminal reward; discount-induced magnitude variation vanishes entirely, but sign misattribution persists because each window still receives an independently normalized advantage. If collapse occurs at $\gamma = 1.0$, magnitude decay cannot be the primary cause.
81	
82	All four $\gamma$ values produce complete training collapse: validation success drops to 0\% within 5 training steps across the sweep ($\gamma = 0.50$: collapsed at step~1; $\gamma = 0.80$: 3.1\% at step~5 then 0\%; $\gamma = 0.95$: 0\% at step~5; $\gamma = 1.0$: collapsed). The uniformity of collapse across $\gamma$ values, including $\gamma = 1.0$ where no magnitude decay exists, confirms that sign misattribution is the operative failure mechanism. Magnitude decay modulates the speed of collapse but is neither necessary nor sufficient to cause it.
83	
84	\paragraph{Window-size sweep.}
85	Step-independent training with $h \in \{2, 5, 10, 20\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \in \{10, 20\}$ is in progress.
86	
87	\subsection{Results}
88	\label{sec:results}
89	
90	Results are organized around three comparisons: (1)~episode-level vs.\ step-independent training dynamics (Section~\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\ref{sec:results_hsweep}). \placeholder{Results sections to follow.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "65e19aaa-bcfd-4202-941b-568036d63383",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
      "content": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?\n\n\\subsection{Environment}\n\\label{sec:environment}\n\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \\texttt{go to countertop 1}, \\texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ awarded only upon successful task completion.\n\nALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.\n\n\\subsection{Base Model and Supervised Fine-Tuning}\n\\label{sec:base_model}\n\nWe use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n\nThis low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint therefore occupies the regime where sign misattribution is most severe.\n\n\\subsection{RL Training Configuration}\n\\label{sec:rl_config}\n\nAll conditions use the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm~\\cite{shao2024deepseekmath}. Table~\\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\\gamma$ applies only to step-independent return computation (Equation~\\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Shared RL training hyperparameters across all conditions.}\n\\label{tab:hyperparameters}\n\\begin{tabular}{lc}\n\\toprule\nParameter & Value \\\\\n\\midrule\nGroup size $K$ & 8 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nKL penalty $\\beta$ & 0.01 \\\\\nDiscount $\\gamma$ & 0.95 \\\\\nInvalid action penalty & 0.1 \\\\\nTasks per training step & 16 \\\\\nTraining steps & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.\n\nThe primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \\in \\{2, 4, 8\\}$. As a diagnostic, we track \\textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. Results report single-seed or two-seed runs depending on availability; seed counts are noted per condition.\n\n\\subsection{Factorial Mechanism Separation}\n\\label{sec:factorial_experiments}\n\nThe dual-mechanism analysis (Section~\\ref{sec:dual_mechanism}) predicts that information loss (M1) and sign misattribution (M2) produce qualitatively different training failures. To separate their effects, we implement the $2 \\times 2$ factorial design described in Section~\\ref{sec:factorial_design}, varying two factors: observation scope (truncated window vs.\\ full trajectory) and advantage scope (per-window vs.\\ episode-level).\n\n\\paragraph{Cell A: Truncated observation + step-level advantage.}\nWindow size $h{=}2$ with per-window advantage computation. Both mechanisms are active: the policy observes only 2-step windows (M1) and each window receives an advantage whose sign is determined by the episode outcome rather than local action quality (M2). This is the default RAGEN configuration and represents the community standard for multi-turn agent RL. Two seeds.\n\n\\paragraph{Cell B: Truncated observation + episode-level advantage.}\nWindow size $h{=}2$, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (observations are still truncated to 2-step windows), while M2 is eliminated (all windows receive the same advantage sign, so no individual window can be misattributed). The comparison of Cell~A against Cell~B isolates the contribution of sign misattribution: any difference in training stability is attributable to M2 alone. Two seeds.\n\n\\paragraph{Cell D: Full observation + episode-level advantage.}\nThe complete trajectory is processed as a single sequence with one shared advantage. Neither mechanism is active: the full context eliminates information loss, and the single advantage eliminates sign misattribution. The comparison of Cell~B against Cell~D isolates the contribution of information loss: any performance gap reflects how truncated context limits the policy's ability to learn cross-step strategies. Two seeds.\n\nThe fourth cell (full observation + step-level advantage) is degenerate: with full context, only one window spans the entire episode, so per-window and episode-level advantage coincide. The factorial design therefore yields three distinct conditions that test qualitative predictions about training dynamics, not quantitative effect decomposition (Section~\\ref{sec:factorial_design}).\n\n\\subsection{Additional Experimental Conditions}\n\\label{sec:additional_conditions}\n\n\\paragraph{Dense reward baseline.}\nStep-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.\n\n\\paragraph{REINFORCE++ baseline.}\nEpisode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used.\\footnote{This condition was originally planned as a GAE baseline with a learned value function. We substituted REINFORCE++ after TRL~1.1.0 removed the \\texttt{AutoModelForCausalLMWithValueHead} class required for critic-based methods.}\n\n\\paragraph{Discount factor sweep.}\nStep-independent $h{=}5$ with $\\gamma \\in \\{0.50, 0.80, 0.95, 1.00\\}$. This sweep isolates the role of magnitude decay in training collapse. At $\\gamma = 1.0$, all windows receive identical return magnitude from the terminal reward; discount-induced magnitude variation vanishes entirely, but sign misattribution persists because each window still receives an independently normalized advantage. If collapse occurs at $\\gamma = 1.0$, magnitude decay cannot be the primary cause.\n\nAll four $\\gamma$ values produce complete training collapse: validation success drops to 0\\% within 5 training steps across the sweep ($\\gamma = 0.50$: collapsed at step~1; $\\gamma = 0.80$: 3.1\\% at step~5 then 0\\%; $\\gamma = 0.95$: 0\\% at step~5; $\\gamma = 1.0$: collapsed). The uniformity of collapse across $\\gamma$ values, including $\\gamma = 1.0$ where no magnitude decay exists, confirms that sign misattribution is the operative failure mechanism. Magnitude decay modulates the speed of collapse but is neither necessary nor sufficient to cause it.\n\n\\paragraph{Window-size sweep.}\nStep-independent training with $h \\in \\{2, 5, 10, 20\\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \\in \\{10, 20\\}$ is in progress.\n\n\\subsection{Results}\n\\label{sec:results}\n\nResults are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}",
      "numLines": 90,
      "startLine": 1,
      "totalLines": 90
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
Now I have both files. The `docs/paper/experiments.tex` appears to be the more recent/structured version. The `artifacts/_project/paper/experiments.tex` appears to be an older version. Let me check which one is the "active" paper file by looking at the main tex file.

Let me check the docs/paper directory for the main file structure to understand which is the authoritative version and where the Cross-Scale Verification section should be added.

Looking at the docs/paper/experiments.tex - it ends with a placeholder at line 90. The current subsections are:
- 5.1 Environment


- 5.2 Base Model and Supervised Fine-Tuning
- 5.3 RL Training Configuration
- 5.4 Evaluation Protocol
- 5.5 Factorial Mechanism Separation
- 5.6 Additional Experimental Conditions
- 5.7 Results

The Results section has placeholder subsections but no actual content yet, whereas the artifacts version has more fleshed out results. Since docs/paper seems to be the more structured version, I should add the cross-scale verification section there.

Now I need to figure out which directory is the primary one by checking the main.tex file and understanding the overall paper structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "921cb4f7-5b32-4cbf-b14c-65770fcf4941",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185CDKGtV6QoezouejBvdNs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 30497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8219
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

Let me check which is the primary paper file and the current section numbering.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "52089baa-e6f2-4f95-8b67-1388cfba41d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185CDKGtV6QoezouejBvdNs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 30497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8219
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

<details open><summary>🔧 Tool call — Glob · `toolu_01L4cZHaKDLB2LjdyG1Uzcp2`</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "50018e79-2867-48fd-8abc-221855cd6c28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185CDKGtV6QoezouejBvdNs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 30497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8219
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

_source line 18 · 2026-05-20T13:20:16.395Z_

<details><summary>↩ Tool result · `toolu_01L4cZHaKDLB2LjdyG1Uzcp2`</summary>

```text
docs/paper/discussion.tex
docs/paper/theoretical_analysis.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "ba84874b-0eea-4578-82c3-6f04d2ac1bd7",
  "tool_use_result": {
    "filenames": [
      "docs/paper/discussion.tex",
      "docs/paper/theoretical_analysis.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/method.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 11,
    "numFiles": 7,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Glob · `toolu_01TzfREDQjwFdyvFcDKjrf33`</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "0134e77a-fb50-4f09-885b-0cd4236b7254",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185CDKGtV6QoezouejBvdNs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 30497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8219
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

_source line 20 · 2026-05-20T13:20:16.947Z_

<details><summary>↩ Tool result · `toolu_01TzfREDQjwFdyvFcDKjrf33`</summary>

```text
artifacts/_project/paper/theoretical_analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments_aa43d8.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "b9adcbef-268c-49a3-a7fd-d5b7a5a62b60",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/theoretical_analysis.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/experiments_aa43d8.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/experiments.tex"
    ],
    "durationMs": 11,
    "numFiles": 7,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Both directories have experiments.tex. The `docs/paper/` version seems more structured but ends with a placeholder. The `artifacts/_project/paper/` version has more fleshed-out results but is the older version.

Let me check the docs/paper version more carefully - it ends at "Results" with a placeholder. The sections are:
- 5.1 Environment
- 5.2 Base Model and SFT


- 5.3 RL Training Config
- 5.4 Evaluation Protocol
- 5.5 Factorial Mechanism Separation
- 5.6 Additional Experimental Conditions
- 5.7 Results (with subsections mentioned but only as placeholders)

The user wants to add a "Cross-Scale Verification" subsection. This would fit logically as a new section after the results, probably as §5.8, since it's about validating findings across different scales. the docs/paper version since it's the more organized working draft. I need to figure out where exactly to place the Cross-Scale Verification section—it could go as a new subsection after Results or within Results itself. Looking at the current structure in experiments.tex, I see Results is already a subsection with its own content, so I'll add this as a sibling subsection right after it.

Now I'm drafting the LaTeX content for this new section. I need to follow the paper's style conventions: no em-dashes, no -ing phrase endings, no AI-style language, and keep it concise with 2-3 paragraphs plus a table. I'm pulling the 8B baseline metrics from the experimental data to back up the claims with actual results.

Writing the Cross-Scale Verification section... I'm seeing that step 12 shows the training reward saturating at 100%, which confirms the episode-level approach is working effectively. The key insight here is that this pattern holds consistently across scales—Cell A's collapse happens at both 1.7B and 8B parameters, and the episode-level fix works equally well at both scales. What's particularly striking with the 8B model is that it outperforms the SFT baseline by over 10 percentage points on out-of-distribution tasks, while still facing the same severe information loss problem that the windowed approach encounters.

Now I'm structuring how to present this in the paper. The cross-scale verification should sit as its own subsection after the main results, since it's examining a different model scale and provides important evidence that these dynamics aren't artifacts of the smaller model size.

Writing the LaTeX subsection... The 8B baseline substantially outperforms the 1.7B variant, making this a more stringent test of whether episode-level training adds value beyond what scale provides. When I restrict the context window to just 2 steps, performance drops from 68.75% to 31.25%—a 37.5 percentage point gap that mirrors the relative impact seen at 1.7B, suggesting that information loss from context truncation remains a fundamental challenge regardless of model size. Now examining whether the step-independent training collapse persists at this larger scale. Episode-level training on the 8B model achieves 96.9% in-distribution and 90.3% out-of-distribution success, representing a substantial 9.7 percentage point improvement over the SFT baseline despite starting from an already strong 80.6% baseline. The training converges by step 12 with reward saturation at 100%, demonstrating that reinforcement learning provides meaningful gains beyond the initial supervised fine-tuning. Now I'm compiling the results table... Generating markdown table...

The 8B model results show that step-independent training fails at the same rate regardless of model size, confirming the issue isn't resolved by scaling, while episode-level training achieves substantially better performance on both in-distribution and out-of-distribution tasks, even surpassing the original baseline. I'm counting the paragraph structure in my writeup and realizing I have too many sections with the \paragraph{} headings. The user wants 2-3 text blocks plus a table, but I've got seven distinct sections including the intro and conclusion. While these inline headings are consistent with the existing style in experiments.tex, I need to consolidate and compress the content to match the requested format.

Let me restructure this into a tighter layout: an opening paragraph covering the cross-scale findings and information loss, then two focused \paragraph{} blocks—one on Cell A collapse and Cell C success, another wrapping up the key takeaway—sandwiched around the table. I should also clean up some of the phrasing to avoid -ing constructions and use more direct statements instead. I'm settling on a structure with paragraph blocks to match the existing style in the document. I'll keep each block concise: an intro paragraph establishing the scale-invariance question, then separate blocks for the 8B setup and results. The 8B baseline achieves strong performance at 68.75% in-distribution and 80.6% out-of-distribution, which sets up the comparison. The collapse pattern holds consistently across model scales, matching the theoretical predictions. Episode-level training with GRPO achieves substantially better results—reaching 96.9% in-distribution and 90.3% out-of-distribution success, which represents a meaningful 9.7 percentage point improvement over the SFT baseline on held-out tasks.

Generating results table... The failure and fix both scale consistently—step-independent training collapses at 8B just as it does at 1.7B, while episode-level training not only prevents collapse but actually surpasses the SFT baseline by a significant margin.

Now I'm doing a final pass on the writing conventions: checking for em-dashes used for explanation, -ing phrases at sentence endings, avoiding certain AI vocabulary, ensuring LaTeX formatting is correct, and verifying all numbers come from the data. I notice the participial phrase about surpassing the SFT baseline sits in the middle of a sentence rather than at the end, which is fine, but I should double-check the exact phrasing around the OOD success metrics to make sure everything flows cleanly. I'm deciding where to add this content—both the docs and artifacts versions of the experiments file seem active, so I should update both to keep them in sync, though the artifacts version has more detailed results already. I've identified where to insert the new content in both files—after the Additional Baselines subsection in the artifacts version at line 166, and after the Results subsection in the docs/paper version at line 90. Now I'll make both edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "480350f2-3da8-4081-b334-32e5234a5d26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PL3oUYx4GUSrmuRNY5zctM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 38716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 799
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

_source line 22_

Now I have full context on both files. I'll add the Cross-Scale Verification subsection to both `docs/paper/experiments.tex` (after the Results subsection) and `artifacts/_project/paper/experiments.tex` (after Additional Baselines). Let me write the content matching the paper's existing style.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "91a79a43-5d0c-4444-b4bf-fe3ae6c0993a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PL3oUYx4GUSrmuRNY5zctM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 38716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 799
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01UrkCnXjcVtDP1K8zQiwRyj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
  "old_string": "Results are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}",
  "new_string": "Results are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}\n\n\\subsection{Cross-Scale Verification}\n\\label{sec:cross_scale}\n\nThe 1.7B experiments establish that step-independent training collapses while episode-level training succeeds. Both mechanisms could in principle be scale-dependent: a larger model might compensate for information loss through greater capacity, or resist sign misattribution through more stable optimization. We test scale invariance by replicating the key factorial conditions on Qwen3-8B.\n\n\\paragraph{Setup.}\nThe 8B SFT baseline uses the same training protocol (2{,}546 demonstrations, 2 epochs, learning rate $5 \\times 10^{-6}$). It achieves 68.75\\% in-distribution and 80.6\\% OOD success ($T{=}0$), far above the 1.7B baseline of 12.5\\%.% exp_id: 8b_sft_baseline\nThis higher starting point provides a stronger test: improvement over an already-competent baseline would confirm that episode-level RL adds value beyond what scale alone provides.\n\n\\paragraph{Information loss.}\nRestricting the 8B model's observation window to $h{=}2$ at inference time drops in-distribution success from 68.75\\% to 31.25\\%, a 37.5 percentage point gap.% exp_id: 8b_info_loss_eval\nThe relative magnitude is comparable to the 1.7B case. Larger models do not implicitly reconstruct missing context from a 2-step window.\n\n\\paragraph{Cell A collapse.}\nStep-independent training on the 8B model collapses within two gradient steps: in-distribution success drops from 28.1\\% (before training) to 12.5\\% (step~1) to 1.5\\% (step~2).% exp_id: 8b_cell_a_episode\nThe collapse trajectory matches the 1.7B pattern, consistent with the sign misattribution rate predicted by Proposition~\\ref{prop:correct_sign}.\n\n\\paragraph{Cell C: episode-level training.}\nEpisode-level GRPO reaches 96.9\\% in-distribution success at step~10 and 90.3\\% OOD success (134 tasks, $T{=}0.4$), a 9.7 percentage point improvement over the SFT baseline on OOD tasks.% exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5\nTraining reward saturates to 100\\% at step~12. The gain over an 80.6\\% SFT baseline confirms that correct credit assignment enables RL to improve beyond supervised learning even from a strong initialization.\n\nTable~\\ref{tab:8b_results} summarizes the 8B conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{8B model results on ALFWorld. In-Dist: 32-task validation set; OOD: 134-task held-out test set. Cell~A reports the value at step~2 (immediately before complete collapse). Cell~C reports the best checkpoint (step~10).}\n\\label{tab:8b_results}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{In-Dist (\\%)} & \\textbf{OOD (\\%)} \\\\\n\\midrule\nSFT baseline ($T{=}0$) & 68.75 & 80.60 \\\\  % exp_id: 8b_sft_baseline\nSFT $h{=}2$ ($T{=}0$) & 31.25 & --- \\\\  % exp_id: 8b_info_loss_eval\nCell A: step-indep.\\ ($h{=}2$) & 28.1 $\\to$ 1.5 & --- \\\\  % exp_id: 8b_cell_a_episode\nCell C: episode-level & \\textbf{96.88} & \\textbf{90.30} \\\\  % exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth the failure and the fix are scale-invariant. Step-independent training collapses at 8B with the same speed as at 1.7B; episode-level training not only avoids collapse but exceeds the SFT ceiling by a substantial margin."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "2dc5cb1b-e804-4084-83d9-ac6c8edbd900",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PL3oUYx4GUSrmuRNY5zctM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 38716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 799
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

_source line 24 · 2026-05-20T13:22:14.499Z_

<details><summary>↩ Tool result · `toolu_01UrkCnXjcVtDP1K8zQiwRyj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "2d519000-3d52-4384-97b0-a3369620353a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "oldString": "Results are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}",
    "newString": "Results are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}\n\n\\subsection{Cross-Scale Verification}\n\\label{sec:cross_scale}\n\nThe 1.7B experiments establish that step-independent training collapses while episode-level training succeeds. Both mechanisms could in principle be scale-dependent: a larger model might compensate for information loss through greater capacity, or resist sign misattribution through more stable optimization. We test scale invariance by replicating the key factorial conditions on Qwen3-8B.\n\n\\paragraph{Setup.}\nThe 8B SFT baseline uses the same training protocol (2{,}546 demonstrations, 2 epochs, learning rate $5 \\times 10^{-6}$). It achieves 68.75\\% in-distribution and 80.6\\% OOD success ($T{=}0$), far above the 1.7B baseline of 12.5\\%.% exp_id: 8b_sft_baseline\nThis higher starting point provides a stronger test: improvement over an already-competent baseline would confirm that episode-level RL adds value beyond what scale alone provides.\n\n\\paragraph{Information loss.}\nRestricting the 8B model's observation window to $h{=}2$ at inference time drops in-distribution success from 68.75\\% to 31.25\\%, a 37.5 percentage point gap.% exp_id: 8b_info_loss_eval\nThe relative magnitude is comparable to the 1.7B case. Larger models do not implicitly reconstruct missing context from a 2-step window.\n\n\\paragraph{Cell A collapse.}\nStep-independent training on the 8B model collapses within two gradient steps: in-distribution success drops from 28.1\\% (before training) to 12.5\\% (step~1) to 1.5\\% (step~2).% exp_id: 8b_cell_a_episode\nThe collapse trajectory matches the 1.7B pattern, consistent with the sign misattribution rate predicted by Proposition~\\ref{prop:correct_sign}.\n\n\\paragraph{Cell C: episode-level training.}\nEpisode-level GRPO reaches 96.9\\% in-distribution success at step~10 and 90.3\\% OOD success (134 tasks, $T{=}0.4$), a 9.7 percentage point improvement over the SFT baseline on OOD tasks.% exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5\nTraining reward saturates to 100\\% at step~12. The gain over an 80.6\\% SFT baseline confirms that correct credit assignment enables RL to improve beyond supervised learning even from a strong initialization.\n\nTable~\\ref{tab:8b_results} summarizes the 8B conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{8B model results on ALFWorld. In-Dist: 32-task validation set; OOD: 134-task held-out test set. Cell~A reports the value at step~2 (immediately before complete collapse). Cell~C reports the best checkpoint (step~10).}\n\\label{tab:8b_results}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{In-Dist (\\%)} & \\textbf{OOD (\\%)} \\\\\n\\midrule\nSFT baseline ($T{=}0$) & 68.75 & 80.60 \\\\  % exp_id: 8b_sft_baseline\nSFT $h{=}2$ ($T{=}0$) & 31.25 & --- \\\\  % exp_id: 8b_info_loss_eval\nCell A: step-indep.\\ ($h{=}2$) & 28.1 $\\to$ 1.5 & --- \\\\  % exp_id: 8b_cell_a_episode\nCell C: episode-level & \\textbf{96.88} & \\textbf{90.30} \\\\  % exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth the failure and the fix are scale-invariant. Step-independent training collapses at 8B with the same speed as at 1.7B; episode-level training not only avoids collapse but exceeds the SFT ceiling by a substantial margin.",
    "originalFile": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?\n\n\\subsection{Environment}\n\\label{sec:environment}\n\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \\texttt{go to countertop 1}, \\texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ awarded only upon successful task completion.\n\nALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.\n\n\\subsection{Base Model and Supervised Fine-Tuning}\n\\label{sec:base_model}\n\nWe use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n\nThis low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint therefore occupies the regime where sign misattribution is most severe.\n\n\\subsection{RL Training Configuration}\n\\label{sec:rl_config}\n\nAll conditions use the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm~\\cite{shao2024deepseekmath}. Table~\\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\\gamma$ applies only to step-independent return computation (Equation~\\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Shared RL training hyperparameters across all conditions.}\n\\label{tab:hyperparameters}\n\\begin{tabular}{lc}\n\\toprule\nParameter & Value \\\\\n\\midrule\nGroup size $K$ & 8 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nKL penalty $\\beta$ & 0.01 \\\\\nDiscount $\\gamma$ & 0.95 \\\\\nInvalid action penalty & 0.1 \\\\\nTasks per training step & 16 \\\\\nTraining steps & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.\n\nThe primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \\in \\{2, 4, 8\\}$. As a diagnostic, we track \\textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. Results report single-seed or two-seed runs depending on availability; seed counts are noted per condition.\n\n\\subsection{Factorial Mechanism Separation}\n\\label{sec:factorial_experiments}\n\nThe dual-mechanism analysis (Section~\\ref{sec:dual_mechanism}) predicts that information loss (M1) and sign misattribution (M2) produce qualitatively different training failures. To separate their effects, we implement the $2 \\times 2$ factorial design described in Section~\\ref{sec:factorial_design}, varying two factors: observation scope (truncated window vs.\\ full trajectory) and advantage scope (per-window vs.\\ episode-level).\n\n\\paragraph{Cell A: Truncated observation + step-level advantage.}\nWindow size $h{=}2$ with per-window advantage computation. Both mechanisms are active: the policy observes only 2-step windows (M1) and each window receives an advantage whose sign is determined by the episode outcome rather than local action quality (M2). This is the default RAGEN configuration and represents the community standard for multi-turn agent RL. Two seeds.\n\n\\paragraph{Cell B: Truncated observation + episode-level advantage.}\nWindow size $h{=}2$, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (observations are still truncated to 2-step windows), while M2 is eliminated (all windows receive the same advantage sign, so no individual window can be misattributed). The comparison of Cell~A against Cell~B isolates the contribution of sign misattribution: any difference in training stability is attributable to M2 alone. Two seeds.\n\n\\paragraph{Cell D: Full observation + episode-level advantage.}\nThe complete trajectory is processed as a single sequence with one shared advantage. Neither mechanism is active: the full context eliminates information loss, and the single advantage eliminates sign misattribution. The comparison of Cell~B against Cell~D isolates the contribution of information loss: any performance gap reflects how truncated context limits the policy's ability to learn cross-step strategies. Two seeds.\n\nThe fourth cell (full observation + step-level advantage) is degenerate: with full context, only one window spans the entire episode, so per-window and episode-level advantage coincide. The factorial design therefore yields three distinct conditions that test qualitative predictions about training dynamics, not quantitative effect decomposition (Section~\\ref{sec:factorial_design}).\n\n\\subsection{Additional Experimental Conditions}\n\\label{sec:additional_conditions}\n\n\\paragraph{Dense reward baseline.}\nStep-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.\n\n\\paragraph{REINFORCE++ baseline.}\nEpisode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used.\\footnote{This condition was originally planned as a GAE baseline with a learned value function. We substituted REINFORCE++ after TRL~1.1.0 removed the \\texttt{AutoModelForCausalLMWithValueHead} class required for critic-based methods.}\n\n\\paragraph{Discount factor sweep.}\nStep-independent $h{=}5$ with $\\gamma \\in \\{0.50, 0.80, 0.95, 1.00\\}$. This sweep isolates the role of magnitude decay in training collapse. At $\\gamma = 1.0$, all windows receive identical return magnitude from the terminal reward; discount-induced magnitude variation vanishes entirely, but sign misattribution persists because each window still receives an independently normalized advantage. If collapse occurs at $\\gamma = 1.0$, magnitude decay cannot be the primary cause.\n\nAll four $\\gamma$ values produce complete training collapse: validation success drops to 0\\% within 5 training steps across the sweep ($\\gamma = 0.50$: collapsed at step~1; $\\gamma = 0.80$: 3.1\\% at step~5 then 0\\%; $\\gamma = 0.95$: 0\\% at step~5; $\\gamma = 1.0$: collapsed). The uniformity of collapse across $\\gamma$ values, including $\\gamma = 1.0$ where no magnitude decay exists, confirms that sign misattribution is the operative failure mechanism. Magnitude decay modulates the speed of collapse but is neither necessary nor sufficient to cause it.\n\n\\paragraph{Window-size sweep.}\nStep-independent training with $h \\in \\{2, 5, 10, 20\\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \\in \\{10, 20\\}$ is in progress.\n\n\\subsection{Results}\n\\label{sec:results}\n\nResults are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}",
    "structuredPatch": [
      {
        "oldStart": 87,
        "oldLines": 4,
        "newStart": 87,
        "newLines": 46,
        "lines": [
          " \\subsection{Results}",
          " \\label{sec:results}",
          " ",
          "-Results are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}",
          "\\ No newline at end of file",
          "+Results are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size ablation (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}",
          "+",
          "+\\subsection{Cross-Scale Verification}",
          "+\\label{sec:cross_scale}",
          "+",
          "+The 1.7B experiments establish that step-independent training collapses while episode-level training succeeds. Both mechanisms could in principle be scale-dependent: a larger model might compensate for information loss through greater capacity, or resist sign misattribution through more stable optimization. We test scale invariance by replicating the key factorial conditions on Qwen3-8B.",
          "+",
          "+\\paragraph{Setup.}",
          "+The 8B SFT baseline uses the same training protocol (2{,}546 demonstrations, 2 epochs, learning rate $5 \\times 10^{-6}$). It achieves 68.75\\% in-distribution and 80.6\\% OOD success ($T{=}0$), far above the 1.7B baseline of 12.5\\%.% exp_id: 8b_sft_baseline",
          "+This higher starting point provides a stronger test: improvement over an already-competent baseline would confirm that episode-level RL adds value beyond what scale alone provides.",
          "+",
          "+\\paragraph{Information loss.}",
          "+Restricting the 8B model's observation window to $h{=}2$ at inference time drops in-distribution success from 68.75\\% to 31.25\\%, a 37.5 percentage point gap.% exp_id: 8b_info_loss_eval",
          "+The relative magnitude is comparable to the 1.7B case. Larger models do not implicitly reconstruct missing context from a 2-step window.",
          "+",
          "+\\paragraph{Cell A collapse.}",
          "+Step-independent training on the 8B model collapses within two gradient steps: in-distribution success drops from 28.1\\% (before training) to 12.5\\% (step~1) to 1.5\\% (step~2).% exp_id: 8b_cell_a_episode",
          "+The collapse trajectory matches the 1.7B pattern, consistent with the sign misattribution rate predicted by Proposition~\\ref{prop:correct_sign}.",
          "+",
          "+\\paragraph{Cell C: episode-level training.}",
          "+Episode-level GRPO reaches 96.9\\% in-distribution success at step~10 and 90.3\\% OOD success (134 tasks, $T{=}0.4$), a 9.7 percentage point improvement over the SFT baseline on OOD tasks.% exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5",
          "+Training reward saturates to 100\\% at step~12. The gain over an 80.6\\% SFT baseline confirms that correct credit assignment enables RL to improve beyond supervised learning even from a strong initialization.",
          "+",
          "+Table~\\ref{tab:8b_results} summarizes the 8B conditions.",
          "+",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\caption{8B model results on ALFWorld. In-Dist: 32-task validation set; OOD: 134-task held-out test set. Cell~A reports the value at step~2 (immediately before complete collapse). Cell~C reports the best checkpoint (step~10).}",
          "+\\label{tab:8b_results}",
          "+\\small",
          "+\\begin{tabular}{@{}lcc@{}}",
          "+\\toprule",
          "+\\textbf{Method} & \\textbf{In-Dist (\\%)} & \\textbf{OOD (\\%)} \\\\",
          "+\\midrule",
          "+SFT baseline ($T{=}0$) & 68.75 & 80.60 \\\\  % exp_id: 8b_sft_baseline",
          "+SFT $h{=}2$ ($T{=}0$) & 31.25 & --- \\\\  % exp_id: 8b_info_loss_eval",
          "+Cell A: step-indep.\\ ($h{=}2$) & 28.1 $\\to$ 1.5 & --- \\\\  % exp_id: 8b_cell_a_episode",
          "+Cell C: episode-level & \\textbf{96.88} & \\textbf{90.30} \\\\  % exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          "+Both the failure and the fix are scale-invariant. Step-independent training collapses at 8B with the same speed as at 1.7B; episode-level training not only avoids collapse but exceeds the SFT ceiling by a substantial margin.",
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01SpnU1XgZCoHE7Pq76p7Hbv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
  "old_string": "\\paragraph{Selective verification.}\nBuilding on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}",
  "new_string": "\\paragraph{Selective verification.}\nBuilding on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}\n\n\\subsection{Cross-Scale Verification}\n\\label{sec:cross_scale}\n\nThe 1.7B experiments establish that step-independent training collapses while episode-level training succeeds. Both mechanisms could in principle be scale-dependent: a larger model might compensate for information loss through greater capacity, or resist sign misattribution through more stable optimization. We test scale invariance by replicating the key factorial conditions on Qwen3-8B.\n\n\\paragraph{Setup.}\nThe 8B SFT baseline uses the same training protocol (2{,}546 demonstrations, 2 epochs, learning rate $5 \\times 10^{-6}$). It achieves 68.75\\% in-distribution and 80.6\\% OOD success ($T{=}0$), far above the 1.7B baseline of 12.5\\%.% exp_id: 8b_sft_baseline\nThis higher starting point provides a stronger test: improvement over an already-competent baseline would confirm that episode-level RL adds value beyond what scale alone provides.\n\n\\paragraph{Information loss.}\nRestricting the 8B model's observation window to $h{=}2$ at inference time drops in-distribution success from 68.75\\% to 31.25\\%, a 37.5 percentage point gap.% exp_id: 8b_info_loss_eval\nThe relative magnitude is comparable to the 1.7B case. Larger models do not implicitly reconstruct missing context from a 2-step window.\n\n\\paragraph{Cell A collapse.}\nStep-independent training on the 8B model collapses within two gradient steps: in-distribution success drops from 28.1\\% (before training) to 12.5\\% (step~1) to 1.5\\% (step~2).% exp_id: 8b_cell_a_episode\nThe collapse trajectory matches the 1.7B pattern, consistent with the sign misattribution rate predicted by Proposition~\\ref{prop:correct_sign}.\n\n\\paragraph{Cell C: episode-level training.}\nEpisode-level GRPO reaches 96.9\\% in-distribution success at step~10 and 90.3\\% OOD success (134 tasks, $T{=}0.4$), a 9.7 percentage point improvement over the SFT baseline on OOD tasks.% exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5\nTraining reward saturates to 100\\% at step~12. The gain over an 80.6\\% SFT baseline confirms that correct credit assignment enables RL to improve beyond supervised learning even from a strong initialization.\n\nTable~\\ref{tab:8b_results} summarizes the 8B conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{8B model results on ALFWorld. In-Dist: 32-task validation set; OOD: 134-task held-out test set. Cell~A reports the value at step~2 (immediately before complete collapse). Cell~C reports the best checkpoint (step~10).}\n\\label{tab:8b_results}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{In-Dist (\\%)} & \\textbf{OOD (\\%)} \\\\\n\\midrule\nSFT baseline ($T{=}0$) & 68.75 & 80.60 \\\\  % exp_id: 8b_sft_baseline\nSFT $h{=}2$ ($T{=}0$) & 31.25 & --- \\\\  % exp_id: 8b_info_loss_eval\nCell A: step-indep.\\ ($h{=}2$) & 28.1 $\\to$ 1.5 & --- \\\\  % exp_id: 8b_cell_a_episode\nCell C: episode-level & \\textbf{96.88} & \\textbf{90.30} \\\\  % exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth the failure and the fix are scale-invariant. Step-independent training collapses at 8B with the same speed as at 1.7B; episode-level training not only avoids collapse but exceeds the SFT ceiling by a substantial margin."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "4f8f4e17-af19-499e-bd5b-4f0060fd5974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PL3oUYx4GUSrmuRNY5zctM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 38716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 799
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

_source line 26 · 2026-05-20T13:22:27.165Z_

<details><summary>↩ Tool result · `toolu_01SpnU1XgZCoHE7Pq76p7Hbv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "df694892-ab37-439a-b70b-e3f786c7f54a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper/experiments.tex",
    "oldString": "\\paragraph{Selective verification.}\nBuilding on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}",
    "newString": "\\paragraph{Selective verification.}\nBuilding on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}\n\n\\subsection{Cross-Scale Verification}\n\\label{sec:cross_scale}\n\nThe 1.7B experiments establish that step-independent training collapses while episode-level training succeeds. Both mechanisms could in principle be scale-dependent: a larger model might compensate for information loss through greater capacity, or resist sign misattribution through more stable optimization. We test scale invariance by replicating the key factorial conditions on Qwen3-8B.\n\n\\paragraph{Setup.}\nThe 8B SFT baseline uses the same training protocol (2{,}546 demonstrations, 2 epochs, learning rate $5 \\times 10^{-6}$). It achieves 68.75\\% in-distribution and 80.6\\% OOD success ($T{=}0$), far above the 1.7B baseline of 12.5\\%.% exp_id: 8b_sft_baseline\nThis higher starting point provides a stronger test: improvement over an already-competent baseline would confirm that episode-level RL adds value beyond what scale alone provides.\n\n\\paragraph{Information loss.}\nRestricting the 8B model's observation window to $h{=}2$ at inference time drops in-distribution success from 68.75\\% to 31.25\\%, a 37.5 percentage point gap.% exp_id: 8b_info_loss_eval\nThe relative magnitude is comparable to the 1.7B case. Larger models do not implicitly reconstruct missing context from a 2-step window.\n\n\\paragraph{Cell A collapse.}\nStep-independent training on the 8B model collapses within two gradient steps: in-distribution success drops from 28.1\\% (before training) to 12.5\\% (step~1) to 1.5\\% (step~2).% exp_id: 8b_cell_a_episode\nThe collapse trajectory matches the 1.7B pattern, consistent with the sign misattribution rate predicted by Proposition~\\ref{prop:correct_sign}.\n\n\\paragraph{Cell C: episode-level training.}\nEpisode-level GRPO reaches 96.9\\% in-distribution success at step~10 and 90.3\\% OOD success (134 tasks, $T{=}0.4$), a 9.7 percentage point improvement over the SFT baseline on OOD tasks.% exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5\nTraining reward saturates to 100\\% at step~12. The gain over an 80.6\\% SFT baseline confirms that correct credit assignment enables RL to improve beyond supervised learning even from a strong initialization.\n\nTable~\\ref{tab:8b_results} summarizes the 8B conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{8B model results on ALFWorld. In-Dist: 32-task validation set; OOD: 134-task held-out test set. Cell~A reports the value at step~2 (immediately before complete collapse). Cell~C reports the best checkpoint (step~10).}\n\\label{tab:8b_results}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{In-Dist (\\%)} & \\textbf{OOD (\\%)} \\\\\n\\midrule\nSFT baseline ($T{=}0$) & 68.75 & 80.60 \\\\  % exp_id: 8b_sft_baseline\nSFT $h{=}2$ ($T{=}0$) & 31.25 & --- \\\\  % exp_id: 8b_info_loss_eval\nCell A: step-indep.\\ ($h{=}2$) & 28.1 $\\to$ 1.5 & --- \\\\  % exp_id: 8b_cell_a_episode\nCell C: episode-level & \\textbf{96.88} & \\textbf{90.30} \\\\  % exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth the failure and the fix are scale-invariant. Step-independent training collapses at 8B with the same speed as at 1.7B; episode-level training not only avoids collapse but exceeds the SFT ceiling by a substantial margin.",
    "originalFile": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\\ref{sec:m2_sign_misattribution}?\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\n\\paragraph{Environment.}\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands. % TODO: add shridhar2021alfworld to .bib\nALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R = 1$ for successful task completion and $R = 0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.\n\nALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.\n\n\\paragraph{Base model.}\nWe use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves approximately 6.25\\% success rate on a held-out 32-episode validation set, providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.0625$ with group size $K = 8$, Proposition 2 (Section~\\ref{sec:formal_probability}) predicts that approximately 84.5\\% of gradient updates carry incorrect sign under step-independent training.\n\n\\paragraph{RL training configuration.}\nWe train using the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:\n\\begin{itemize}\n    \\item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)\n    \\item Learning rate: $1 \\times 10^{-6}$\n    \\item KL penalty coefficient: $\\beta = 0.01$ (low-variance KL)\n    \\item Discount factor: $\\gamma = 0.95$ (applied in step-independent return computation via Equation~\\ref{eq:step_return}; not applicable to episode-level mode)\n    \\item Invalid action penalty coefficient: 0.1\n    \\item Training data: 16 task instances per training step\n    \\item Training steps: 15 (early-stopped based on convergence)\n\\end{itemize}\n\n\\paragraph{Evaluation protocol.}\nWe evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \\in \\{2, 4, 8\\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \\textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.\n\n\\subsection{Window-Size Ablation}\n\\label{sec:window_ablation}\n\nTo disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.\n\n\\paragraph{Conditions.}\nWe vary the step-independent history length $h \\in \\{2, 5, 10, 20\\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \\texttt{step\\_independent} training mode with \\texttt{step\\_independent\\_history\\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.\n\n\\paragraph{Design rationale.}\nThe five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.\n\n\\paragraph{Controls.}\nAll conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. All $h$-sweep conditions are currently single-seed. Multi-seed replication (3 seeds per $h$) is planned.% Sources: exp028c ($h=2$), exp029 (episode-level).\n\n\\paragraph{Post-hoc evaluation.}\nTo isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).\n\n\\subsection{Results}\n\\label{sec:results}\n\n\\subsubsection{Episode-Level vs. Step-Independent Training}\n\\label{sec:results_main}\n\nThe central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\\% validation success at training step 15, a 4.5$\\times$ improvement over the SFT baseline of approximately 6.25\\%. Step-independent training with $h = 2$ collapses to 0\\% validation success by step 10.\n\nTable~\\ref{tab:main_results} summarizes the central comparison. All seed results are reported individually due to high inter-seed variance under step-independent conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{1.7B ALFWorld results across credit assignment methods. OOD: held-out test tasks; In-Dist: 32-episode validation set. All seeds shown; no aggregation due to high inter-seed variance.}\n\\label{tab:main_results}\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed} & \\textbf{OOD (\\%)} & \\textbf{In-Dist (\\%)} \\\\\n\\midrule\nStep-indep.\\ ($h{=}2$, windowed) & 1 & 0 & 0 \\\\  % Cell A\n                                  & 2 & 3.73 & 9.375 \\\\  % Cell A seed2\n\\midrule\nStep-indep.\\ (factorial)          & 1 & 0.75 & 20 \\\\  % Cell B\n                                  & 2 & 0.75 & 55.5 \\\\  % Cell B seed2\n\\midrule\nEpisode-level (full context)      & 1 & 23.88 & 28.125 \\\\  % Cell C, exp029\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\placeholder{fig6\\_training\\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}\n\nThe collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), task success drops from 18.75\\% to single digits while action validity remains high at approximately 89.3\\%. The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), action validity itself collapses from 89.3\\% to 43.1\\%. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.\n\nEpisode-level training exhibits no such collapse. Action validity remains above 95\\% throughout training, and success rate increases monotonically. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.\n\n\\subsubsection{Window-Size Ablation}\n\\label{sec:results_hsweep}\n\n\\begin{table}[t]\n\\centering\n\\caption{Window-size ablation (1.7B, single seed). OOD success rate at the final training step. $h = \\text{full}$ denotes episode-level training (exp029).}\n\\label{tab:h_sweep}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\n\\textbf{Window size $h$} & \\textbf{OOD Success (\\%)} \\\\\n\\midrule\n$h = 2$  & 0 \\\\\n$h = 5$  & 0 \\\\\n$h = 10$ & 6.25 \\\\\n$h = 20$ & 15.6 \\\\\n$h = \\text{full}$ (episode-level) & 23.88 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\placeholder{fig5\\_h\\_sweep\\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (6.25\\%).}\n\nThe ablation reveals a credit assignment cliff consistent with our theoretical predictions (Table~\\ref{tab:h_sweep}). OOD success rate is 0\\% for $h \\leq 5$, rises to 6.25\\% at $h = 10$ and 15.6\\% at $h = 20$, and reaches 23.88\\% under episode-level training ($h = T$). The transition between $h = 5$ and $h = 10$ marks the onset of non-trivial generalization. Results are single-seed; multi-seed replication is in progress.\n\nThe dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.\n\nFrom the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Action validity at step 2 is 89.3\\%, dropping to 43.1\\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.\n\n\\subsubsection{Dense Reward Baseline}\n\\label{sec:results_dense}\n\nA natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.\n\nThe dense reward experiment (exp013f) produces a striking dissociation. Action validity increases from 60\\% to 97.5\\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, task success remains at 0\\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.\n\nThis result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.\n\n\\subsection{Empirical Verification of Sign Misattribution}\n\\label{sec:sign_verification}\n\nThe theoretical analysis of Section~\\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions.\n\n\\paragraph{Methodology.}\nDuring step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\\text{sign}(\\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\\text{episode}}^{(i)} \\in \\{0, 1\\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:\n\\begin{itemize}\n    \\item \\textbf{Sign-outcome correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and $R_{\\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.\n    \\item \\textbf{Sign-quality correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.\n    \\item \\textbf{Correct sign fraction}: $P(\\text{correct sign} \\mid \\text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\\ref{sec:formal_probability}) predicts this equals approximately 15.5\\% at $p = 6.25\\%$, $K = 8$.\n\\end{itemize}\n\n\\paragraph{Predictions.}\nThe sign misattribution mechanism makes three testable predictions:\n\\begin{enumerate}\n    \\item Sign-outcome correlation $\\approx 1.0$ (advantage sign is a proxy for episode success, not local quality)\n    \\item Sign-quality correlation $\\approx 0$ (advantage sign is independent of whether local actions were good)\n    \\item $P(\\text{correct sign}) \\approx 15.5\\%$ (derived from Proposition 2 at the observed success rate)\n\\end{enumerate}\nIf all three predictions are confirmed empirically, the sign misattribution mechanism is validated as the causal driver of training collapse, rather than alternative explanations such as reward sparsity, KL divergence, or optimization instability.\n\nTable~\\ref{tab:sign_verification} reports the empirical measurements. The credit agreement rate---the fraction of windows where the advantage sign matches local action quality---is 52.07\\%, indistinguishable from the 50\\% expected under random sign assignment. The point biserial correlation between advantage sign and local action quality is $r = 0.068$, confirming near-zero dependence. Additionally, a discount factor sweep reveals that \\textit{all} $\\gamma$ values produce collapse, including $\\gamma = 1.0$ (no discounting). The $\\gamma = 1.0$ result rules out temporal discounting as the failure cause and isolates sign misattribution as the root mechanism.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical verification of sign misattribution under step-independent training ($h{=}2$). Credit agreement rate measures the fraction of windows where advantage sign matches local action quality; 50\\% indicates random assignment.}\n\\label{tab:sign_verification}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Measured} & \\textbf{Predicted} \\\\\n\\midrule\nCredit agreement rate & 52.07\\% & $\\approx$ 50\\% (random) \\\\\nPoint biserial $r$ (sign vs.\\ quality) & 0.068 & $\\approx$ 0 \\\\\nCollapse at $\\gamma = 1.0$ (no discounting) & Yes & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Additional Baselines}\n\\label{sec:additional_baselines}\n\n\\paragraph{GAE baselines.}\nTo distinguish the effect of episode-level optimization from GRPO-specific design choices (group normalization, no value function), we compare against Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} under two configurations. GAE($\\lambda = 0.95$, $\\gamma = 0.95$) provides standard TD-based advantage estimation with a learned value function, representing the conventional actor-critic approach to temporal credit assignment. GAE($\\lambda = 1$, $\\gamma = 1$) computes Monte Carlo returns equivalent to episode-level GRPO without group normalization, isolating the contribution of group-relative advantage computation. \\placeholder{plan\\_003b: GAE baseline execution. Columns: Method, Val Success (\\%), Action Valid (\\%), Training Stability (variance across steps).}\n\n\\paragraph{Selective verification.}\nBuilding on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}\n",
    "structuredPatch": [
      {
        "oldStart": 171,
        "oldLines": 3,
        "newStart": 171,
        "newLines": 45,
        "lines": [
          " ",
          " \\paragraph{Selective verification.}",
          " Building on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we train a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and demonstrates a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}",
          "+",
          "+\\subsection{Cross-Scale Verification}",
          "+\\label{sec:cross_scale}",
          "+",
          "+The 1.7B experiments establish that step-independent training collapses while episode-level training succeeds. Both mechanisms could in principle be scale-dependent: a larger model might compensate for information loss through greater capacity, or resist sign misattribution through more stable optimization. We test scale invariance by replicating the key factorial conditions on Qwen3-8B.",
          "+",
          "+\\paragraph{Setup.}",
          "+The 8B SFT baseline uses the same training protocol (2{,}546 demonstrations, 2 epochs, learning rate $5 \\times 10^{-6}$). It achieves 68.75\\% in-distribution and 80.6\\% OOD success ($T{=}0$), far above the 1.7B baseline of 12.5\\%.% exp_id: 8b_sft_baseline",
          "+This higher starting point provides a stronger test: improvement over an already-competent baseline would confirm that episode-level RL adds value beyond what scale alone provides.",
          "+",
          "+\\paragraph{Information loss.}",
          "+Restricting the 8B model's observation window to $h{=}2$ at inference time drops in-distribution success from 68.75\\% to 31.25\\%, a 37.5 percentage point gap.% exp_id: 8b_info_loss_eval",
          "+The relative magnitude is comparable to the 1.7B case. Larger models do not implicitly reconstruct missing context from a 2-step window.",
          "+",
          "+\\paragraph{Cell A collapse.}",
          "+Step-independent training on the 8B model collapses within two gradient steps: in-distribution success drops from 28.1\\% (before training) to 12.5\\% (step~1) to 1.5\\% (step~2).% exp_id: 8b_cell_a_episode",
          "+The collapse trajectory matches the 1.7B pattern, consistent with the sign misattribution rate predicted by Proposition~\\ref{prop:correct_sign}.",
          "+",
          "+\\paragraph{Cell C: episode-level training.}",
          "+Episode-level GRPO reaches 96.9\\% in-distribution success at step~10 and 90.3\\% OOD success (134 tasks, $T{=}0.4$), a 9.7 percentage point improvement over the SFT baseline on OOD tasks.% exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5",
          "+Training reward saturates to 100\\% at step~12. The gain over an 80.6\\% SFT baseline confirms that correct credit assignment enables RL to improve beyond supervised learning even from a strong initialization.",
          "+",
          "+Table~\\ref{tab:8b_results} summarizes the 8B conditions.",
          "+",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\caption{8B model results on ALFWorld. In-Dist: 32-task validation set; OOD: 134-task held-out test set. Cell~A reports the value at step~2 (immediately before complete collapse). Cell~C reports the best checkpoint (step~10).}",
          "+\\label{tab:8b_results}",
          "+\\small",
          "+\\begin{tabular}{@{}lcc@{}}",
          "+\\toprule",
          "+\\textbf{Method} & \\textbf{In-Dist (\\%)} & \\textbf{OOD (\\%)} \\\\",
          "+\\midrule",
          "+SFT baseline ($T{=}0$) & 68.75 & 80.60 \\\\  % exp_id: 8b_sft_baseline",
          "+SFT $h{=}2$ ($T{=}0$) & 31.25 & --- \\\\  % exp_id: 8b_info_loss_eval",
          "+Cell A: step-indep.\\ ($h{=}2$) & 28.1 $\\to$ 1.5 & --- \\\\  % exp_id: 8b_cell_a_episode",
          "+Cell C: episode-level & \\textbf{96.88} & \\textbf{90.30} \\\\  % exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          "+Both the failure and the fix are scale-invariant. Step-independent training collapses at 8B with the same speed as at 1.7B; episode-level training not only avoids collapse but exceeds the SFT ceiling by a substantial margin."
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

_source line 27_

已在两个文件中添加 `\subsection{Cross-Scale Verification}` (`\label{sec:cross_scale}`)：

- `docs/paper/experiments.tex` — 添加在 §5.7 Results 之后
- `artifacts/_project/paper/experiments.tex` — 添加在 §5.5 Additional Baselines 之后

内容结构：
- 开头段：动机（scale invariance 测试）
- 4 个 `\paragraph{}`：Setup / Information loss / Cell A collapse / Cell C episode-level
- `Table 5`（`tab:8b_results`）：4 行汇总 SFT baseline / SFT h=2 / Cell A / Cell C
- 结尾段：scale-invariant 结论

所有数字附 `% exp_id:` 注释，无 em-dash，无 -ing 短语结尾，booktabs 表格格式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "uuid": "31b5e11a-306e-40e1-971a-cd87139bf16b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YevbH58xt3ditRgnegF78",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9093,
      "cache_read_input_tokens": 39515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9093
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

_source line 28_

已在两个文件中添加 `\subsection{Cross-Scale Verification}` (`\label{sec:cross_scale}`)：

- `docs/paper/experiments.tex` — 添加在 §5.7 Results 之后
- `artifacts/_project/paper/experiments.tex` — 添加在 §5.5 Additional Baselines 之后

内容结构：
- 开头段：动机（scale invariance 测试）
- 4 个 `\paragraph{}`：Setup / Information loss / Cell A collapse / Cell C episode-level
- `Table 5`（`tab:8b_results`）：4 行汇总 SFT baseline / SFT h=2 / Cell A / Cell C
- 结尾段：scale-invariant 结论

所有数字附 `% exp_id:` 注释，无 em-dash，无 -ing 短语结尾，booktabs 表格格式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 163523,
  "duration_api_ms": 164522,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "a8541fd2-73bf-4aad-9cd4-0b478f063e75",
  "total_cost_usd": 0.55787425,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 36907,
    "cache_read_input_tokens": 145181,
    "output_tokens": 10081,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36907,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 246,
        "cache_read_input_tokens": 39515,
        "cache_creation_input_tokens": 9093,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9093
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2440,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002555,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 10081,
      "cacheReadInputTokens": 145181,
      "cacheCreationInputTokens": 36907,
      "webSearchRequests": 0,
      "costUSD": 0.55531925,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "19d18708-b96d-4780-a67e-0a0550ce338f"
}
```

</details>

---
