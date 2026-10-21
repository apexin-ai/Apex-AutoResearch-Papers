# paper table1 bootstrap ci

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_table1_bootstrap_ci_20260523T065221.log`
- **Structured JSON:** [`0d9cf92a8e636a3ac831.json`](../../sessions/0d/0d9cf92a8e636a3ac831.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
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
  "uuid": "466ee5d2-c79e-45fd-806e-43f53ed3513b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
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
    "resetsAt": 1779531000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "306fea10-b648-4c7d-a54e-15ff8938cf6f",
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5"
}
```

---

### Assistant

_source line 4_

Let me read the paper writing norms and the current results.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "47db54e4-5950-4982-afbe-70a64fb4a0e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnfTR4quxmErVntL4183px",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11720,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11720
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

<details open><summary>🔧 Tool call — Read · `toolu_019A5bX1zSLz182yKNFqJe6o`</summary>

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
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "425aa796-e9cf-4149-970b-edd1b00c8917",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnfTR4quxmErVntL4183px",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11720,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11720
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

_source line 6 · 2026-05-23T06:52:32.937Z_

<details><summary>↩ Tool result · `toolu_019A5bX1zSLz182yKNFqJe6o`</summary>

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
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "13b62462-3c2d-4e07-a0a4-898b09c0fe8e",
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

<details open><summary>🔧 Tool call — Read · `toolu_018F1miTAxitkdwHbQXQ8u9m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "a6824620-75d5-4ad5-a573-6331bd79691f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnfTR4quxmErVntL4183px",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11720,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11720
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

_source line 8 · 2026-05-23T06:52:33.206Z_

<details><summary>↩ Tool result · `toolu_018F1miTAxitkdwHbQXQ8u9m`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	\label{sec:main_results}
7	
8	We report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.
9	
10	Table~\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.
11	
12	\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.
13	
14	\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\ 0.789), a gap within cross-seed variance ($\sigma \approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.
15	
16	\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.
17	
18	\textbf{TSR is stable for gradient-flow conditions but unstable under Detach.} For non-Detach conditions, TSR ranges from 0.869 (Random OCC) to 0.915 (Cutoff\textsuperscript{\dag}), with standard deviations $\leq 0.050$. Detaching gradients destabilizes task execution: Detach OCC achieves mean TSR of 0.812 with $\sigma = 0.163$---an order of magnitude higher variance than any other condition. One Detach seed (seed 44) exhibits broad performance collapse (TSR = 0.624), with all ten tasks degraded relative to the other two Detach seeds (0.914, 0.898). This collapse affects action prediction uniformly (CAR remains 0.748, comparable to the other seeds), suggesting that gradient detachment amplifies sensitivity to initialization for motor learning while leaving collision behavior intact.
19	
20	\begin{table}[t]
21	\centering
22	\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}
23	\label{tab:main_results}
24	\begin{tabular}{lcccc}
25	\toprule
26	Condition & Seeds & TSR & CAR & $\Delta$CAR \\
27	\midrule
28	Full OCC      & 3 & 0.894 $\pm$ 0.050 & \textbf{0.797} $\pm$ 0.032 & $+$1.7 \\
29	Random OCC    & 3 & 0.869 $\pm$ 0.029 & 0.789 $\pm$ 0.031 & $+$0.9 \\
30	Vanilla       & 3 & 0.907 $\pm$ 0.009 & 0.780 $\pm$ 0.012 & ---    \\
31	Detach OCC    & 3 & 0.812 $\pm$ 0.163 & 0.746 $\pm$ 0.002 & $-$3.4 \\
32	\midrule
33	Depth             & 4 & 0.889 $\pm$ 0.042 & 0.780 $\pm$ 0.039 & 0.0 \\
34	Cutoff$^\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\
35	\bottomrule
36	\end{tabular}
37	\end{table}
38	
39	
40	\subsection{Mechanism Analysis}
41	\label{sec:mechanism}
42	
43	The four completed conditions form a $2 \times 2$ factorial structure crossing gradient flow (ON/OFF) with label content (structured/random or none). Table~\ref{tab:factorial} arranges the CAR values in this matrix.
44	
45	\begin{table}[t]
46	\centering
47	\caption{Factorial decomposition of CAR by gradient flow and label content. Each cell shows the condition name and mean CAR. The column effect (gradient flow) dominates: both ON cells exceed their OFF counterparts. Vanilla (no auxiliary head) occupies the ``Gradient OFF / Random or no labels'' cell as the natural baseline for both factors.}
48	\label{tab:factorial}
49	\begin{tabular}{lcc}
50	\toprule
51	 & Gradient ON & Gradient OFF \\
52	\midrule
53	Structured labels    & Full OCC (0.797) & Detach OCC (0.746) \\
54	Random / no labels   & Random OCC (0.789) & Vanilla (0.780) \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\ Vanilla 0.780). The dominant pattern is not that gradient flow \emph{improves} CAR above Vanilla, but that its \emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.
60	
61	\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\sigma \approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\ref{sec:why_detach}).
62	
63	\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \emph{below} Vanilla rather than matching it.
64	
65	\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OCC exhibits uniquely high TSR variance ($\sigma = 0.163$, vs.\ $< 0.050$ for all other conditions). One Detach seed (seed~44) shows TSR = 0.624 with uniform degradation across all ten tasks, while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation---intact collision behavior with collapsed task execution---suggests that gradient detachment amplifies optimization instability for action prediction specifically, consistent with the encoder bearing forward-pass interference from the auxiliary head without receiving compensating gradient signal.
66	
67	Three candidate mechanisms---anti-overfitting regularization, loss landscape smoothing, and gradient diversity---can account for the gradient flow effect. All three predict that gradient flow is necessary and label content is secondary. Section~\ref{sec:why_gradient} develops these hypotheses; the current data cannot distinguish between them.
68	
69	
70	\subsection{Per-Task Analysis}
71	\label{sec:per_task}
72	
73	Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Per-task CAR spans from 0.07 (Task~5, Vanilla) to 1.00 (Tasks~8, 9), revealing a bimodal distribution: seven tasks achieve mean CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks---Tasks~3, 5, and 6---fall below 0.58. The overall CAR of 0.780 is dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
74	
75	\begin{table}[t]
76	\centering
77	\caption{Per-task mean CAR across seeds for each condition (50 rollouts per seed). All conditions use 3 seeds except Depth (4 seeds) and Cutoff$^\dagger$ (2 seeds).}
78	\label{tab:per_task}
79	\begin{tabular}{clcccccc}
80	\toprule
81	 & & \multicolumn{6}{c}{Mean CAR by Condition} \\
82	\cmidrule(lr){3-8}
83	Task & Diff. & Vanilla & Full OCC & Random & Detach & Depth & Cutoff$^\dagger$ \\
84	\midrule
85	T0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.99 & 0.98 \\
86	T1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.93 & 0.94 \\
87	T2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.94 \\
88	T3 & Hard  & 0.38 & 0.37 & 0.31 & \textbf{0.11} & 0.50 & 0.66 \\
89	T4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.92 & 0.98 \\
90	T5 & Hard  & 0.07 & 0.17 & 0.23 & \textbf{0.05} & 0.08 & 0.00 \\
91	T6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.54 & 0.37 \\
92	T7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 0.96 & 0.97 \\
93	T8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 \\
94	T9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 \\
95	\midrule
96	\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.780 & 0.783 \\
97	\bottomrule
98	\end{tabular}
99	\end{table}
100	
101	\textbf{Ceiling effects compress overall differences.} Seven of ten tasks already achieve CAR $\geq$ 0.92 under Vanilla, leaving minimal room for auxiliary training to improve. On these easy tasks, the obstacle is spatially separated from the manipulation path, and the demonstration policy already avoids contact. Any measurable effect of gradient flow on CAR concentrates on the three hard tasks where the Vanilla baseline is low.
102	
103	\textbf{Task~5 is universally difficult.} With Vanilla CAR of 0.07, Task~5 provides the most headroom for improvement, yet no condition achieves CAR above 0.23. Gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain extremely low---the policy contacts the obstacle in at least 77\% of episodes regardless of training condition. The Detach deficit is consistent with the overall pattern (lowest among all conditions), but the absolute gains from gradient flow are modest relative to the task difficulty.
104	
105	\textbf{Tasks~3 and 6 decouple success from safety.} Both tasks achieve near-perfect TSR with CAR below 0.61---the robot completes the goal while colliding in roughly half of episodes. Detach OCC is systematically the worst on Task~3 (CAR 0.11 vs.\ 0.31--0.38 for all other conditions), consistent with gradient detachment amplifying degradation on physically constrained tasks. Among gradient-flow conditions, however, no consistent ordering emerges: on Task~3, Vanilla (0.38) matches or exceeds Full OCC (0.37) and Random OCC (0.31); on Task~6, Full OCC (0.61) and Vanilla (0.57) lead while Random OCC (0.55) trails. This lack of consistent ranking among gradient-flow conditions on hard tasks reinforces the damage-prevention interpretation: gradient flow prevents the Detach-specific degradation but does not systematically improve clearance beyond Vanilla. The Depth condition (4 seeds) confirms this pattern: Task~3 CAR of 0.50 exceeds Vanilla (0.38) but with extreme cross-seed variance (range 0.20--0.78), while Task~6 (0.54) falls below Vanilla (0.57). Cutoff achieves the highest Task~3 CAR (0.66, 2 seeds) but the lowest Task~5 CAR (0.00) and Task~6 CAR (0.37), further illustrating the absence of any consistent condition advantage on hard tasks.
106	
107	
108	\subsection{Temporal Dynamics}
109	\label{sec:temporal}
110	
111	The Cutoff condition applies occupancy supervision with gradient flow for the first 35{,}000 training steps, then disables the auxiliary loss for the remaining 15{,}000 steps. This condition tests whether the gradient flow effect requires continuous auxiliary supervision or whether early-phase exposure is sufficient.
112	
113	\textbf{Cutoff partially preserves the gradient flow effect.} Cutoff achieves CAR of 0.783 (2 seeds), falling between Vanilla (0.780) and Full OCC (0.797) but closer to Vanilla ($+$0.3pp vs.\ Vanilla, compared to Full OCC's $+$1.7pp). Removing auxiliary gradients for the final 30\% of training erodes most of the CAR advantage that continuous gradient flow provides, suggesting that the encoder partially reverts toward action-specialized features when auxiliary gradients are withdrawn.
114	
115	\textbf{Cutoff remains well above Detach.} The 3.7pp gap between Cutoff (0.783) and Detach OCC (0.746) indicates that 35{,}000 steps of gradient flow provide substantial and partially durable protection against the degradation observed under full gradient detachment. The early-phase auxiliary gradients establish encoder representations that do not fully collapse when the auxiliary signal is removed, even though they do not maintain the full benefit of continuous gradient flow.
116	
117	\textbf{Early-phase training durably improves task completion.} Cutoff achieves the highest TSR among all conditions (0.915 vs.\ 0.907 Vanilla, 0.894 Full OCC), suggesting that 35{,}000 steps of auxiliary gradient flow provide a lasting benefit to action prediction that persists---and may even improve---when auxiliary gradients are subsequently removed. This TSR--CAR dissociation reveals distinct temporal requirements: task completion benefits durably from early-phase auxiliary training, while collision avoidance requires continuous gradient flow to be maintained.
118	
119	\textbf{Hard tasks expose the cost of removing late-stage gradient flow.} On Task~5, Cutoff achieves CAR of 0.00 across both seeds---the worst performance of any condition on any task, including Detach (0.05). Full OCC (0.17) and Random OCC (0.23) achieve non-zero T5 CAR with continuous gradient flow. This complete failure on the hardest safety task under early-only gradient flow indicates that collision avoidance on physically constrained tasks depends on auxiliary gradients throughout training, not only during the initial learning phase. On Task~3, Cutoff achieves the highest CAR of any condition (0.66), demonstrating that the temporal sensitivity is task-specific rather than uniform. Cutoff uses 2 seeds; a third seed is in progress.
120	
121	
122	\subsection{Depth vs.\ BEV Occupancy}
123	\label{sec:depth_results}
124	
125	The Depth condition replaces BEV occupancy supervision with egocentric monocular depth prediction (Section~\ref{sec:depth_head}), holding the auxiliary training mechanism constant---same architecture, same loss weight schedule, same gradient flow through DINOv2 and SigLIP encoders. This comparison isolates whether the spatial reference frame or the type of spatial information affects the gradient flow effect, using 4 seeds (42, 43, 44, 45) for additional statistical power.
126	
127	\textbf{Depth matches Vanilla exactly.} Depth achieves mean CAR of 0.780 $\pm$ 0.039 across 4 seeds---identical to Vanilla (0.780 $\pm$ 0.012). Despite providing per-pixel geometric information directly aligned with collision avoidance (nearby surfaces produce small depth values), egocentric depth supervision does not improve CAR beyond the no-auxiliary baseline. This result, combined with Random OCC (0.789) achieving comparable CAR with random binary labels, confirms that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to the presence of gradient flow itself.
128	
129	\textbf{Depth falls below both OCC conditions.} The ordering Full OCC (0.797) $>$ Random OCC (0.789) $>$ Cutoff (0.783) $>$ Depth (0.780) $=$ Vanilla (0.780) places Depth at the bottom of the gradient-flow conditions. The 1.7pp gap between Full OCC and Depth, and the 0.9pp gap between Random OCC and Depth, are within cross-seed variance ($\sigma \approx 0.031$--$0.039$) and not individually significant. However, the consistent ordering---both OCC conditions above Depth despite using different label content---suggests that the BEV auxiliary head architecture may provide a marginally stronger gradient signal than the depth head, independent of label content.
130	
131	\textbf{Depth exhibits high cross-seed variance on hard tasks.} On Task~3, Depth CAR ranges from 0.20 to 0.78 across 4 seeds (mean 0.50); on Task~6, it ranges from 0.16 to 0.84 (mean 0.54). This variance exceeds that of other conditions on the same tasks and is consistent with the broader finding that auxiliary supervision amplifies seed sensitivity relative to Vanilla ($\sigma = 0.012$). The 4-seed design mitigates this variance in the overall mean but limits per-task conclusions.
132	
133	\textbf{Spatial content is confirmed as secondary.} Across three distinct auxiliary label types---structured BEV occupancy (Full OCC, 0.797), random binary labels (Random OCC, 0.789), and egocentric depth maps (Depth, 0.780)---all gradient-flow conditions achieve CAR within 1.7pp of Vanilla, while the gradient-blocked condition (Detach, 0.746) falls 3.4pp below. The 1.7pp spread among gradient-flow conditions is smaller than the 3.4pp Detach deficit, confirming that gradient flow presence is the dominant factor and label content contributes at most marginally.
134	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "5d3289ac-29b2-485e-952d-de10b99e04d9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nWe report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.\n\nTable~\\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.\n\n\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.\n\n\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.\n\n\\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.\n\n\\textbf{TSR is stable for gradient-flow conditions but unstable under Detach.} For non-Detach conditions, TSR ranges from 0.869 (Random OCC) to 0.915 (Cutoff\\textsuperscript{\\dag}), with standard deviations $\\leq 0.050$. Detaching gradients destabilizes task execution: Detach OCC achieves mean TSR of 0.812 with $\\sigma = 0.163$---an order of magnitude higher variance than any other condition. One Detach seed (seed 44) exhibits broad performance collapse (TSR = 0.624), with all ten tasks degraded relative to the other two Detach seeds (0.914, 0.898). This collapse affects action prediction uniformly (CAR remains 0.748, comparable to the other seeds), suggesting that gradient detachment amplifies sensitivity to initialization for motor learning while leaving collision behavior intact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Mechanism Analysis}\n\\label{sec:mechanism}\n\nThe four completed conditions form a $2 \\times 2$ factorial structure crossing gradient flow (ON/OFF) with label content (structured/random or none). Table~\\ref{tab:factorial} arranges the CAR values in this matrix.\n\n\\begin{table}[t]\n\\centering\n\\caption{Factorial decomposition of CAR by gradient flow and label content. Each cell shows the condition name and mean CAR. The column effect (gradient flow) dominates: both ON cells exceed their OFF counterparts. Vanilla (no auxiliary head) occupies the ``Gradient OFF / Random or no labels'' cell as the natural baseline for both factors.}\n\\label{tab:factorial}\n\\begin{tabular}{lcc}\n\\toprule\n & Gradient ON & Gradient OFF \\\\\n\\midrule\nStructured labels    & Full OCC (0.797) & Detach OCC (0.746) \\\\\nRandom / no labels   & Random OCC (0.789) & Vanilla (0.780) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\\ Vanilla 0.780). The dominant pattern is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.\n\n\\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\\sigma \\approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\\ref{sec:why_detach}).\n\n\\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \\emph{below} Vanilla rather than matching it.\n\n\\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OCC exhibits uniquely high TSR variance ($\\sigma = 0.163$, vs.\\ $< 0.050$ for all other conditions). One Detach seed (seed~44) shows TSR = 0.624 with uniform degradation across all ten tasks, while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation---intact collision behavior with collapsed task execution---suggests that gradient detachment amplifies optimization instability for action prediction specifically, consistent with the encoder bearing forward-pass interference from the auxiliary head without receiving compensating gradient signal.\n\nThree candidate mechanisms---anti-overfitting regularization, loss landscape smoothing, and gradient diversity---can account for the gradient flow effect. All three predict that gradient flow is necessary and label content is secondary. Section~\\ref{sec:why_gradient} develops these hypotheses; the current data cannot distinguish between them.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Per-task CAR spans from 0.07 (Task~5, Vanilla) to 1.00 (Tasks~8, 9), revealing a bimodal distribution: seven tasks achieve mean CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks---Tasks~3, 5, and 6---fall below 0.58. The overall CAR of 0.780 is dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task mean CAR across seeds for each condition (50 rollouts per seed). All conditions use 3 seeds except Depth (4 seeds) and Cutoff$^\\dagger$ (2 seeds).}\n\\label{tab:per_task}\n\\begin{tabular}{clcccccc}\n\\toprule\n & & \\multicolumn{6}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-8}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Depth & Cutoff$^\\dagger$ \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.93 & 0.94 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.50 & 0.66 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.92 & 0.98 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.08 & 0.00 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.54 & 0.37 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 0.96 & 0.97 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.780 & 0.783 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects compress overall differences.} Seven of ten tasks already achieve CAR $\\geq$ 0.92 under Vanilla, leaving minimal room for auxiliary training to improve. On these easy tasks, the obstacle is spatially separated from the manipulation path, and the demonstration policy already avoids contact. Any measurable effect of gradient flow on CAR concentrates on the three hard tasks where the Vanilla baseline is low.\n\n\\textbf{Task~5 is universally difficult.} With Vanilla CAR of 0.07, Task~5 provides the most headroom for improvement, yet no condition achieves CAR above 0.23. Gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain extremely low---the policy contacts the obstacle in at least 77\\% of episodes regardless of training condition. The Detach deficit is consistent with the overall pattern (lowest among all conditions), but the absolute gains from gradient flow are modest relative to the task difficulty.\n\n\\textbf{Tasks~3 and 6 decouple success from safety.} Both tasks achieve near-perfect TSR with CAR below 0.61---the robot completes the goal while colliding in roughly half of episodes. Detach OCC is systematically the worst on Task~3 (CAR 0.11 vs.\\ 0.31--0.38 for all other conditions), consistent with gradient detachment amplifying degradation on physically constrained tasks. Among gradient-flow conditions, however, no consistent ordering emerges: on Task~3, Vanilla (0.38) matches or exceeds Full OCC (0.37) and Random OCC (0.31); on Task~6, Full OCC (0.61) and Vanilla (0.57) lead while Random OCC (0.55) trails. This lack of consistent ranking among gradient-flow conditions on hard tasks reinforces the damage-prevention interpretation: gradient flow prevents the Detach-specific degradation but does not systematically improve clearance beyond Vanilla. The Depth condition (4 seeds) confirms this pattern: Task~3 CAR of 0.50 exceeds Vanilla (0.38) but with extreme cross-seed variance (range 0.20--0.78), while Task~6 (0.54) falls below Vanilla (0.57). Cutoff achieves the highest Task~3 CAR (0.66, 2 seeds) but the lowest Task~5 CAR (0.00) and Task~6 CAR (0.37), further illustrating the absence of any consistent condition advantage on hard tasks.\n\n\n\\subsection{Temporal Dynamics}\n\\label{sec:temporal}\n\nThe Cutoff condition applies occupancy supervision with gradient flow for the first 35{,}000 training steps, then disables the auxiliary loss for the remaining 15{,}000 steps. This condition tests whether the gradient flow effect requires continuous auxiliary supervision or whether early-phase exposure is sufficient.\n\n\\textbf{Cutoff partially preserves the gradient flow effect.} Cutoff achieves CAR of 0.783 (2 seeds), falling between Vanilla (0.780) and Full OCC (0.797) but closer to Vanilla ($+$0.3pp vs.\\ Vanilla, compared to Full OCC's $+$1.7pp). Removing auxiliary gradients for the final 30\\% of training erodes most of the CAR advantage that continuous gradient flow provides, suggesting that the encoder partially reverts toward action-specialized features when auxiliary gradients are withdrawn.\n\n\\textbf{Cutoff remains well above Detach.} The 3.7pp gap between Cutoff (0.783) and Detach OCC (0.746) indicates that 35{,}000 steps of gradient flow provide substantial and partially durable protection against the degradation observed under full gradient detachment. The early-phase auxiliary gradients establish encoder representations that do not fully collapse when the auxiliary signal is removed, even though they do not maintain the full benefit of continuous gradient flow.\n\n\\textbf{Early-phase training durably improves task completion.} Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla, 0.894 Full OCC), suggesting that 35{,}000 steps of auxiliary gradient flow provide a lasting benefit to action prediction that persists---and may even improve---when auxiliary gradients are subsequently removed. This TSR--CAR dissociation reveals distinct temporal requirements: task completion benefits durably from early-phase auxiliary training, while collision avoidance requires continuous gradient flow to be maintained.\n\n\\textbf{Hard tasks expose the cost of removing late-stage gradient flow.} On Task~5, Cutoff achieves CAR of 0.00 across both seeds---the worst performance of any condition on any task, including Detach (0.05). Full OCC (0.17) and Random OCC (0.23) achieve non-zero T5 CAR with continuous gradient flow. This complete failure on the hardest safety task under early-only gradient flow indicates that collision avoidance on physically constrained tasks depends on auxiliary gradients throughout training, not only during the initial learning phase. On Task~3, Cutoff achieves the highest CAR of any condition (0.66), demonstrating that the temporal sensitivity is task-specific rather than uniform. Cutoff uses 2 seeds; a third seed is in progress.\n\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_results}\n\nThe Depth condition replaces BEV occupancy supervision with egocentric monocular depth prediction (Section~\\ref{sec:depth_head}), holding the auxiliary training mechanism constant---same architecture, same loss weight schedule, same gradient flow through DINOv2 and SigLIP encoders. This comparison isolates whether the spatial reference frame or the type of spatial information affects the gradient flow effect, using 4 seeds (42, 43, 44, 45) for additional statistical power.\n\n\\textbf{Depth matches Vanilla exactly.} Depth achieves mean CAR of 0.780 $\\pm$ 0.039 across 4 seeds---identical to Vanilla (0.780 $\\pm$ 0.012). Despite providing per-pixel geometric information directly aligned with collision avoidance (nearby surfaces produce small depth values), egocentric depth supervision does not improve CAR beyond the no-auxiliary baseline. This result, combined with Random OCC (0.789) achieving comparable CAR with random binary labels, confirms that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to the presence of gradient flow itself.\n\n\\textbf{Depth falls below both OCC conditions.} The ordering Full OCC (0.797) $>$ Random OCC (0.789) $>$ Cutoff (0.783) $>$ Depth (0.780) $=$ Vanilla (0.780) places Depth at the bottom of the gradient-flow conditions. The 1.7pp gap between Full OCC and Depth, and the 0.9pp gap between Random OCC and Depth, are within cross-seed variance ($\\sigma \\approx 0.031$--$0.039$) and not individually significant. However, the consistent ordering---both OCC conditions above Depth despite using different label content---suggests that the BEV auxiliary head architecture may provide a marginally stronger gradient signal than the depth head, independent of label content.\n\n\\textbf{Depth exhibits high cross-seed variance on hard tasks.} On Task~3, Depth CAR ranges from 0.20 to 0.78 across 4 seeds (mean 0.50); on Task~6, it ranges from 0.16 to 0.84 (mean 0.54). This variance exceeds that of other conditions on the same tasks and is consistent with the broader finding that auxiliary supervision amplifies seed sensitivity relative to Vanilla ($\\sigma = 0.012$). The 4-seed design mitigates this variance in the overall mean but limits per-task conclusions.\n\n\\textbf{Spatial content is confirmed as secondary.} Across three distinct auxiliary label types---structured BEV occupancy (Full OCC, 0.797), random binary labels (Random OCC, 0.789), and egocentric depth maps (Depth, 0.780)---all gradient-flow conditions achieve CAR within 1.7pp of Vanilla, while the gradient-blocked condition (Detach, 0.746) falls 3.4pp below. The 1.7pp spread among gradient-flow conditions is smaller than the 3.4pp Detach deficit, confirming that gradient flow presence is the dominant factor and label content contributes at most marginally.\n",
      "numLines": 134,
      "startLine": 1,
      "totalLines": 134
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me analyze what needs to change:

1. **Table 1 (tab:main_results)**: Add CI data to the CAR column. The table currently has 5 columns (Condition, Seeds, TSR, CAR, ΔCAR). Adding a full "CAR 95% CI" column would make it 6 columns, which is still reasonable for single-column width.

Looking at the data provided:
- Vanilla: CAR 0.780±0.012, CI [0.759, 0.801]


- Full OCC: CAR 0.797±0.032, CI [0.776, 0.817]
- Detach OCC: CAR 0.746±0.002, CI [0.723, 0.768]
- Random OCC: CAR 0.789±0.031, CI [0.767, 0.809]
- Depth: CAR 0.780±0.039, CI [0.762, 0.797]
- Cutoff†: CAR 0.783±0.021, CI [0.757, 0.808]

I notice Random OCC is missing its mean value, so I'll need to check that before finalizing the table.

Looking at the data more carefully, I see the user's table has some inconsistencies—Random OCC appears to be missing the mean±std notation, and Cutoff only has two seeds so it's missing the standard deviation. I'll use the values I have and also incorporate the Cutoff TSR metric. For the formatting, I'm deciding between a separate CI column or inline annotation—given the table width constraints, I think inline notation would work better to keep everything compact. I'm weighing whether the CI should be inline or in its own column. Since the bootstrap CI is more rigorous than standard deviation for capturing seed-level uncertainty, it makes sense to include it prominently. Adding a dedicated CI column would push this to 6 columns, which should still fit in a single-column format given the short entries, so I'll go with that approach.

Now I'm reconsidering whether to keep both the ±std and CI or drop the standard deviation entirely, since many ML papers report only the bootstrap confidence interval once it's available.

The user specifically wants the CI visible alongside CAR, so I'll add a dedicated column using a compact format like `[.759, .801]` to save space. I should also update the Cutoff row to include the standard deviation for TSR that the user mentioned, and double-check the existing values in their table. I'm parsing the user's table structure more carefully—it looks like the TSR column might actually be missing for Random OCC, with the 0.789±0.031 value representing CAR instead. I'll stick with the existing TSR of 0.869±0.029 and use the CAR and confidence interval values the user provided.

For Cutoff, the user gives TSR as 0.915±0.004, which I should add to the existing table since it includes the standard deviation now. I'm also checking Depth's TSR values to see what updates are needed there. Generating the updated table...

Now I'm checking the prose against the CI results. The key distinction is that Detach OCC shows statistically significant degradation compared to all other conditions based on the bootstrap confidence intervals, while the difference between Full OCC and Vanilla is negligible since the CI includes zero. I should strengthen the language around Detach OCC's performance while being more cautious about Full OCC, and the asymmetry between gradient-flow and gradient-blocked conditions clearly supports the claim that gradient flow is necessary. I need to update the prose discussing the results to align with the new bootstrap CI methodology. The key change is that we now have confidence intervals to support our claims, so I can move away from the cautious language about needing additional replications.

For the opening paragraph, I'm replacing the note about limited seed counts requiring replication with a statement about how we're using bootstrap confidence intervals to quantify uncertainty. Then I need to check other mentions throughout the text—like where we discuss degradation effects and the random OCC discussion—to ensure they're consistent with what the CIs actually support.

Now I'm drafting the updated table with the CI column and revised caption explaining the bootstrap methodology.

Generating markdown table... Generating markdown table... I'll stick with the 6-column approach and use `\small` to keep everything readable without losing the ±std values for consistency. Now I need to update the prose sections—specifically the opening paragraph to reference bootstrap confidence intervals instead of mentioning the need for additional replications, and then adjust the claims about degradation to align with what the statistical tests actually support. I'm working through the specific edits needed to align the prose with the statistical findings. I need to update the opening paragraph to properly frame the significance claims, revise the table with the correct confidence intervals, and then check sections 4.2 and beyond to ensure all references to the numbers are consistent with the CI data I'm presenting. I'm refining the gradient flow paragraph to emphasize statistical significance by noting that the bootstrap confidence intervals for the Detach OCC condition don't overlap with other conditions, strengthening the claim that gradient flow is necessary for the auxiliary head to function properly. I need to finish that sentence about the Full OCC advantage and then think through the edits to the table. The bootstrap confidence interval for the difference includes zero, so while the 1.7 percentage point improvement is directionally positive, it's not statistically significant. Now I'm considering whether to add standard deviations for the Cutoff condition—the user provided those values, and with the confidence intervals now available, it makes sense to include them for consistency. Let me carefully review the exact lines I need to edit to make sure I get the wording right. I'm working through the specific edits needed for this results section. I need to update the significance language on line 8, revise the table on lines 20-37, and make three targeted changes to line 12: add confidence interval language comparing Full OCC to Vanilla, update the Detach OCC description with statistical backing, and clean up the em-dashes. For the table footnote, I should move the bootstrap CI methodology into the caption and integrate the statements about Detach OCC's significance and the Full OCC versus Vanilla comparison into the surrounding text rather than keeping them as footnotes. I'm realizing the user's table is missing the TSR column for Random OCC—it only shows Seeds, one metric value, and a confidence interval. Given that the existing table has TSR=0.869 for Random OCC, the 0.789±0.031 must be the CAR value, so I'll keep the TSR column as-is and just fill in the CAR data from what they provided.

Now I'm ready to make the three edits: updating the opening paragraph, the table itself, and the first body paragraph about gradient flow.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "cb9b9fc6-178c-44bc-9b41-4ca706eac721",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXtsdaM83zhiVN5kMp7ygj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11123,
      "cache_read_input_tokens": 23561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11123
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

I'll make four edits: (1) opening paragraph to reference bootstrap CIs, (2) the table itself, (3) the gradient flow paragraph to add CI-backed language, and (4) the label content paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "23b64eb7-06ca-41d1-a83b-ea62d516995a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXtsdaM83zhiVN5kMp7ygj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11123,
      "cache_read_input_tokens": 23561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11123
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

<details open><summary>🔧 Tool call — Edit · `toolu_012dAsPDzeJH5iirWcyhhYyZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.",
  "new_string": "Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "ddde72dc-9c3c-4e03-a9ee-815aa1b09e7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXtsdaM83zhiVN5kMp7ygj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11123,
      "cache_read_input_tokens": 23561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11123
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

_source line 12 · 2026-05-23T06:54:55.351Z_

<details><summary>↩ Tool result · `toolu_012dAsPDzeJH5iirWcyhhYyZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "8a1bfb9b-6980-4d75-aa0f-da42e0d5028a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.",
    "newString": "Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise.",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nWe report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.\n\nTable~\\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.\n\n\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.\n\n\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.\n\n\\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.\n\n\\textbf{TSR is stable for gradient-flow conditions but unstable under Detach.} For non-Detach conditions, TSR ranges from 0.869 (Random OCC) to 0.915 (Cutoff\\textsuperscript{\\dag}), with standard deviations $\\leq 0.050$. Detaching gradients destabilizes task execution: Detach OCC achieves mean TSR of 0.812 with $\\sigma = 0.163$---an order of magnitude higher variance than any other condition. One Detach seed (seed 44) exhibits broad performance collapse (TSR = 0.624), with all ten tasks degraded relative to the other two Detach seeds (0.914, 0.898). This collapse affects action prediction uniformly (CAR remains 0.748, comparable to the other seeds), suggesting that gradient detachment amplifies sensitivity to initialization for motor learning while leaving collision behavior intact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Mechanism Analysis}\n\\label{sec:mechanism}\n\nThe four completed conditions form a $2 \\times 2$ factorial structure crossing gradient flow (ON/OFF) with label content (structured/random or none). Table~\\ref{tab:factorial} arranges the CAR values in this matrix.\n\n\\begin{table}[t]\n\\centering\n\\caption{Factorial decomposition of CAR by gradient flow and label content. Each cell shows the condition name and mean CAR. The column effect (gradient flow) dominates: both ON cells exceed their OFF counterparts. Vanilla (no auxiliary head) occupies the ``Gradient OFF / Random or no labels'' cell as the natural baseline for both factors.}\n\\label{tab:factorial}\n\\begin{tabular}{lcc}\n\\toprule\n & Gradient ON & Gradient OFF \\\\\n\\midrule\nStructured labels    & Full OCC (0.797) & Detach OCC (0.746) \\\\\nRandom / no labels   & Random OCC (0.789) & Vanilla (0.780) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\\ Vanilla 0.780). The dominant pattern is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.\n\n\\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\\sigma \\approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\\ref{sec:why_detach}).\n\n\\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \\emph{below} Vanilla rather than matching it.\n\n\\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OCC exhibits uniquely high TSR variance ($\\sigma = 0.163$, vs.\\ $< 0.050$ for all other conditions). One Detach seed (seed~44) shows TSR = 0.624 with uniform degradation across all ten tasks, while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation---intact collision behavior with collapsed task execution---suggests that gradient detachment amplifies optimization instability for action prediction specifically, consistent with the encoder bearing forward-pass interference from the auxiliary head without receiving compensating gradient signal.\n\nThree candidate mechanisms---anti-overfitting regularization, loss landscape smoothing, and gradient diversity---can account for the gradient flow effect. All three predict that gradient flow is necessary and label content is secondary. Section~\\ref{sec:why_gradient} develops these hypotheses; the current data cannot distinguish between them.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Per-task CAR spans from 0.07 (Task~5, Vanilla) to 1.00 (Tasks~8, 9), revealing a bimodal distribution: seven tasks achieve mean CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks---Tasks~3, 5, and 6---fall below 0.58. The overall CAR of 0.780 is dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task mean CAR across seeds for each condition (50 rollouts per seed). All conditions use 3 seeds except Depth (4 seeds) and Cutoff$^\\dagger$ (2 seeds).}\n\\label{tab:per_task}\n\\begin{tabular}{clcccccc}\n\\toprule\n & & \\multicolumn{6}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-8}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Depth & Cutoff$^\\dagger$ \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.93 & 0.94 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.50 & 0.66 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.92 & 0.98 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.08 & 0.00 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.54 & 0.37 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 0.96 & 0.97 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.780 & 0.783 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects compress overall differences.} Seven of ten tasks already achieve CAR $\\geq$ 0.92 under Vanilla, leaving minimal room for auxiliary training to improve. On these easy tasks, the obstacle is spatially separated from the manipulation path, and the demonstration policy already avoids contact. Any measurable effect of gradient flow on CAR concentrates on the three hard tasks where the Vanilla baseline is low.\n\n\\textbf{Task~5 is universally difficult.} With Vanilla CAR of 0.07, Task~5 provides the most headroom for improvement, yet no condition achieves CAR above 0.23. Gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain extremely low---the policy contacts the obstacle in at least 77\\% of episodes regardless of training condition. The Detach deficit is consistent with the overall pattern (lowest among all conditions), but the absolute gains from gradient flow are modest relative to the task difficulty.\n\n\\textbf{Tasks~3 and 6 decouple success from safety.} Both tasks achieve near-perfect TSR with CAR below 0.61---the robot completes the goal while colliding in roughly half of episodes. Detach OCC is systematically the worst on Task~3 (CAR 0.11 vs.\\ 0.31--0.38 for all other conditions), consistent with gradient detachment amplifying degradation on physically constrained tasks. Among gradient-flow conditions, however, no consistent ordering emerges: on Task~3, Vanilla (0.38) matches or exceeds Full OCC (0.37) and Random OCC (0.31); on Task~6, Full OCC (0.61) and Vanilla (0.57) lead while Random OCC (0.55) trails. This lack of consistent ranking among gradient-flow conditions on hard tasks reinforces the damage-prevention interpretation: gradient flow prevents the Detach-specific degradation but does not systematically improve clearance beyond Vanilla. The Depth condition (4 seeds) confirms this pattern: Task~3 CAR of 0.50 exceeds Vanilla (0.38) but with extreme cross-seed variance (range 0.20--0.78), while Task~6 (0.54) falls below Vanilla (0.57). Cutoff achieves the highest Task~3 CAR (0.66, 2 seeds) but the lowest Task~5 CAR (0.00) and Task~6 CAR (0.37), further illustrating the absence of any consistent condition advantage on hard tasks.\n\n\n\\subsection{Temporal Dynamics}\n\\label{sec:temporal}\n\nThe Cutoff condition applies occupancy supervision with gradient flow for the first 35{,}000 training steps, then disables the auxiliary loss for the remaining 15{,}000 steps. This condition tests whether the gradient flow effect requires continuous auxiliary supervision or whether early-phase exposure is sufficient.\n\n\\textbf{Cutoff partially preserves the gradient flow effect.} Cutoff achieves CAR of 0.783 (2 seeds), falling between Vanilla (0.780) and Full OCC (0.797) but closer to Vanilla ($+$0.3pp vs.\\ Vanilla, compared to Full OCC's $+$1.7pp). Removing auxiliary gradients for the final 30\\% of training erodes most of the CAR advantage that continuous gradient flow provides, suggesting that the encoder partially reverts toward action-specialized features when auxiliary gradients are withdrawn.\n\n\\textbf{Cutoff remains well above Detach.} The 3.7pp gap between Cutoff (0.783) and Detach OCC (0.746) indicates that 35{,}000 steps of gradient flow provide substantial and partially durable protection against the degradation observed under full gradient detachment. The early-phase auxiliary gradients establish encoder representations that do not fully collapse when the auxiliary signal is removed, even though they do not maintain the full benefit of continuous gradient flow.\n\n\\textbf{Early-phase training durably improves task completion.} Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla, 0.894 Full OCC), suggesting that 35{,}000 steps of auxiliary gradient flow provide a lasting benefit to action prediction that persists---and may even improve---when auxiliary gradients are subsequently removed. This TSR--CAR dissociation reveals distinct temporal requirements: task completion benefits durably from early-phase auxiliary training, while collision avoidance requires continuous gradient flow to be maintained.\n\n\\textbf{Hard tasks expose the cost of removing late-stage gradient flow.} On Task~5, Cutoff achieves CAR of 0.00 across both seeds---the worst performance of any condition on any task, including Detach (0.05). Full OCC (0.17) and Random OCC (0.23) achieve non-zero T5 CAR with continuous gradient flow. This complete failure on the hardest safety task under early-only gradient flow indicates that collision avoidance on physically constrained tasks depends on auxiliary gradients throughout training, not only during the initial learning phase. On Task~3, Cutoff achieves the highest CAR of any condition (0.66), demonstrating that the temporal sensitivity is task-specific rather than uniform. Cutoff uses 2 seeds; a third seed is in progress.\n\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_results}\n\nThe Depth condition replaces BEV occupancy supervision with egocentric monocular depth prediction (Section~\\ref{sec:depth_head}), holding the auxiliary training mechanism constant---same architecture, same loss weight schedule, same gradient flow through DINOv2 and SigLIP encoders. This comparison isolates whether the spatial reference frame or the type of spatial information affects the gradient flow effect, using 4 seeds (42, 43, 44, 45) for additional statistical power.\n\n\\textbf{Depth matches Vanilla exactly.} Depth achieves mean CAR of 0.780 $\\pm$ 0.039 across 4 seeds---identical to Vanilla (0.780 $\\pm$ 0.012). Despite providing per-pixel geometric information directly aligned with collision avoidance (nearby surfaces produce small depth values), egocentric depth supervision does not improve CAR beyond the no-auxiliary baseline. This result, combined with Random OCC (0.789) achieving comparable CAR with random binary labels, confirms that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to the presence of gradient flow itself.\n\n\\textbf{Depth falls below both OCC conditions.} The ordering Full OCC (0.797) $>$ Random OCC (0.789) $>$ Cutoff (0.783) $>$ Depth (0.780) $=$ Vanilla (0.780) places Depth at the bottom of the gradient-flow conditions. The 1.7pp gap between Full OCC and Depth, and the 0.9pp gap between Random OCC and Depth, are within cross-seed variance ($\\sigma \\approx 0.031$--$0.039$) and not individually significant. However, the consistent ordering---both OCC conditions above Depth despite using different label content---suggests that the BEV auxiliary head architecture may provide a marginally stronger gradient signal than the depth head, independent of label content.\n\n\\textbf{Depth exhibits high cross-seed variance on hard tasks.} On Task~3, Depth CAR ranges from 0.20 to 0.78 across 4 seeds (mean 0.50); on Task~6, it ranges from 0.16 to 0.84 (mean 0.54). This variance exceeds that of other conditions on the same tasks and is consistent with the broader finding that auxiliary supervision amplifies seed sensitivity relative to Vanilla ($\\sigma = 0.012$). The 4-seed design mitigates this variance in the overall mean but limits per-task conclusions.\n\n\\textbf{Spatial content is confirmed as secondary.} Across three distinct auxiliary label types---structured BEV occupancy (Full OCC, 0.797), random binary labels (Random OCC, 0.789), and egocentric depth maps (Depth, 0.780)---all gradient-flow conditions achieve CAR within 1.7pp of Vanilla, while the gradient-blocked condition (Detach, 0.746) falls 3.4pp below. The 1.7pp spread among gradient-flow conditions is smaller than the 3.4pp Detach deficit, confirming that gradient flow presence is the dominant factor and label content contributes at most marginally.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " \\subsection{Main Results}",
          " \\label{sec:main_results}",
          " ",
          "-We report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we report effect directions and magnitudes but note that formal significance requires additional replications. All results use the 50{,}000-step checkpoint unless noted otherwise.",
          "+We report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise.",
          " ",
          " Table~\\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.",
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_018B1MnQkyvg7mbmQtaYYP28`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
  "new_string": "\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. $\\pm$ indicates one standard deviation across seeds. Bootstrap 95\\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.776, .817] & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.767, .809] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.759, .801] & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.723, .768] & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.762, .797] & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915 $\\pm$ 0.004 & 0.783 $\\pm$ 0.021 & [.757, .808] & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "e862926b-99bd-42ab-925e-95c08291c99d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JhgDhN7hU8tupxJZjjSTkG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6726,
      "cache_read_input_tokens": 34684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6726
      },
      "output_tokens": 64,
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

_source line 14 · 2026-05-23T06:55:13.405Z_

<details><summary>↩ Tool result · `toolu_018B1MnQkyvg7mbmQtaYYP28`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "03a3fe59-dee3-4f6c-b066-a7cf7852e767",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "newString": "\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. $\\pm$ indicates one standard deviation across seeds. Bootstrap 95\\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.776, .817] & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.767, .809] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.759, .801] & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.723, .768] & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.762, .797] & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915 $\\pm$ 0.004 & 0.783 $\\pm$ 0.021 & [.757, .808] & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nWe report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise.\n\nTable~\\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.\n\n\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.\n\n\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.\n\n\\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.\n\n\\textbf{TSR is stable for gradient-flow conditions but unstable under Detach.} For non-Detach conditions, TSR ranges from 0.869 (Random OCC) to 0.915 (Cutoff\\textsuperscript{\\dag}), with standard deviations $\\leq 0.050$. Detaching gradients destabilizes task execution: Detach OCC achieves mean TSR of 0.812 with $\\sigma = 0.163$---an order of magnitude higher variance than any other condition. One Detach seed (seed 44) exhibits broad performance collapse (TSR = 0.624), with all ten tasks degraded relative to the other two Detach seeds (0.914, 0.898). This collapse affects action prediction uniformly (CAR remains 0.748, comparable to the other seeds), suggesting that gradient detachment amplifies sensitivity to initialization for motor learning while leaving collision behavior intact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Mechanism Analysis}\n\\label{sec:mechanism}\n\nThe four completed conditions form a $2 \\times 2$ factorial structure crossing gradient flow (ON/OFF) with label content (structured/random or none). Table~\\ref{tab:factorial} arranges the CAR values in this matrix.\n\n\\begin{table}[t]\n\\centering\n\\caption{Factorial decomposition of CAR by gradient flow and label content. Each cell shows the condition name and mean CAR. The column effect (gradient flow) dominates: both ON cells exceed their OFF counterparts. Vanilla (no auxiliary head) occupies the ``Gradient OFF / Random or no labels'' cell as the natural baseline for both factors.}\n\\label{tab:factorial}\n\\begin{tabular}{lcc}\n\\toprule\n & Gradient ON & Gradient OFF \\\\\n\\midrule\nStructured labels    & Full OCC (0.797) & Detach OCC (0.746) \\\\\nRandom / no labels   & Random OCC (0.789) & Vanilla (0.780) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\\ Vanilla 0.780). The dominant pattern is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.\n\n\\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\\sigma \\approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\\ref{sec:why_detach}).\n\n\\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \\emph{below} Vanilla rather than matching it.\n\n\\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OCC exhibits uniquely high TSR variance ($\\sigma = 0.163$, vs.\\ $< 0.050$ for all other conditions). One Detach seed (seed~44) shows TSR = 0.624 with uniform degradation across all ten tasks, while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation---intact collision behavior with collapsed task execution---suggests that gradient detachment amplifies optimization instability for action prediction specifically, consistent with the encoder bearing forward-pass interference from the auxiliary head without receiving compensating gradient signal.\n\nThree candidate mechanisms---anti-overfitting regularization, loss landscape smoothing, and gradient diversity---can account for the gradient flow effect. All three predict that gradient flow is necessary and label content is secondary. Section~\\ref{sec:why_gradient} develops these hypotheses; the current data cannot distinguish between them.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Per-task CAR spans from 0.07 (Task~5, Vanilla) to 1.00 (Tasks~8, 9), revealing a bimodal distribution: seven tasks achieve mean CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks---Tasks~3, 5, and 6---fall below 0.58. The overall CAR of 0.780 is dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task mean CAR across seeds for each condition (50 rollouts per seed). All conditions use 3 seeds except Depth (4 seeds) and Cutoff$^\\dagger$ (2 seeds).}\n\\label{tab:per_task}\n\\begin{tabular}{clcccccc}\n\\toprule\n & & \\multicolumn{6}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-8}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Depth & Cutoff$^\\dagger$ \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.93 & 0.94 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.50 & 0.66 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.92 & 0.98 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.08 & 0.00 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.54 & 0.37 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 0.96 & 0.97 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.780 & 0.783 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects compress overall differences.} Seven of ten tasks already achieve CAR $\\geq$ 0.92 under Vanilla, leaving minimal room for auxiliary training to improve. On these easy tasks, the obstacle is spatially separated from the manipulation path, and the demonstration policy already avoids contact. Any measurable effect of gradient flow on CAR concentrates on the three hard tasks where the Vanilla baseline is low.\n\n\\textbf{Task~5 is universally difficult.} With Vanilla CAR of 0.07, Task~5 provides the most headroom for improvement, yet no condition achieves CAR above 0.23. Gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain extremely low---the policy contacts the obstacle in at least 77\\% of episodes regardless of training condition. The Detach deficit is consistent with the overall pattern (lowest among all conditions), but the absolute gains from gradient flow are modest relative to the task difficulty.\n\n\\textbf{Tasks~3 and 6 decouple success from safety.} Both tasks achieve near-perfect TSR with CAR below 0.61---the robot completes the goal while colliding in roughly half of episodes. Detach OCC is systematically the worst on Task~3 (CAR 0.11 vs.\\ 0.31--0.38 for all other conditions), consistent with gradient detachment amplifying degradation on physically constrained tasks. Among gradient-flow conditions, however, no consistent ordering emerges: on Task~3, Vanilla (0.38) matches or exceeds Full OCC (0.37) and Random OCC (0.31); on Task~6, Full OCC (0.61) and Vanilla (0.57) lead while Random OCC (0.55) trails. This lack of consistent ranking among gradient-flow conditions on hard tasks reinforces the damage-prevention interpretation: gradient flow prevents the Detach-specific degradation but does not systematically improve clearance beyond Vanilla. The Depth condition (4 seeds) confirms this pattern: Task~3 CAR of 0.50 exceeds Vanilla (0.38) but with extreme cross-seed variance (range 0.20--0.78), while Task~6 (0.54) falls below Vanilla (0.57). Cutoff achieves the highest Task~3 CAR (0.66, 2 seeds) but the lowest Task~5 CAR (0.00) and Task~6 CAR (0.37), further illustrating the absence of any consistent condition advantage on hard tasks.\n\n\n\\subsection{Temporal Dynamics}\n\\label{sec:temporal}\n\nThe Cutoff condition applies occupancy supervision with gradient flow for the first 35{,}000 training steps, then disables the auxiliary loss for the remaining 15{,}000 steps. This condition tests whether the gradient flow effect requires continuous auxiliary supervision or whether early-phase exposure is sufficient.\n\n\\textbf{Cutoff partially preserves the gradient flow effect.} Cutoff achieves CAR of 0.783 (2 seeds), falling between Vanilla (0.780) and Full OCC (0.797) but closer to Vanilla ($+$0.3pp vs.\\ Vanilla, compared to Full OCC's $+$1.7pp). Removing auxiliary gradients for the final 30\\% of training erodes most of the CAR advantage that continuous gradient flow provides, suggesting that the encoder partially reverts toward action-specialized features when auxiliary gradients are withdrawn.\n\n\\textbf{Cutoff remains well above Detach.} The 3.7pp gap between Cutoff (0.783) and Detach OCC (0.746) indicates that 35{,}000 steps of gradient flow provide substantial and partially durable protection against the degradation observed under full gradient detachment. The early-phase auxiliary gradients establish encoder representations that do not fully collapse when the auxiliary signal is removed, even though they do not maintain the full benefit of continuous gradient flow.\n\n\\textbf{Early-phase training durably improves task completion.} Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla, 0.894 Full OCC), suggesting that 35{,}000 steps of auxiliary gradient flow provide a lasting benefit to action prediction that persists---and may even improve---when auxiliary gradients are subsequently removed. This TSR--CAR dissociation reveals distinct temporal requirements: task completion benefits durably from early-phase auxiliary training, while collision avoidance requires continuous gradient flow to be maintained.\n\n\\textbf{Hard tasks expose the cost of removing late-stage gradient flow.} On Task~5, Cutoff achieves CAR of 0.00 across both seeds---the worst performance of any condition on any task, including Detach (0.05). Full OCC (0.17) and Random OCC (0.23) achieve non-zero T5 CAR with continuous gradient flow. This complete failure on the hardest safety task under early-only gradient flow indicates that collision avoidance on physically constrained tasks depends on auxiliary gradients throughout training, not only during the initial learning phase. On Task~3, Cutoff achieves the highest CAR of any condition (0.66), demonstrating that the temporal sensitivity is task-specific rather than uniform. Cutoff uses 2 seeds; a third seed is in progress.\n\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_results}\n\nThe Depth condition replaces BEV occupancy supervision with egocentric monocular depth prediction (Section~\\ref{sec:depth_head}), holding the auxiliary training mechanism constant---same architecture, same loss weight schedule, same gradient flow through DINOv2 and SigLIP encoders. This comparison isolates whether the spatial reference frame or the type of spatial information affects the gradient flow effect, using 4 seeds (42, 43, 44, 45) for additional statistical power.\n\n\\textbf{Depth matches Vanilla exactly.} Depth achieves mean CAR of 0.780 $\\pm$ 0.039 across 4 seeds---identical to Vanilla (0.780 $\\pm$ 0.012). Despite providing per-pixel geometric information directly aligned with collision avoidance (nearby surfaces produce small depth values), egocentric depth supervision does not improve CAR beyond the no-auxiliary baseline. This result, combined with Random OCC (0.789) achieving comparable CAR with random binary labels, confirms that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to the presence of gradient flow itself.\n\n\\textbf{Depth falls below both OCC conditions.} The ordering Full OCC (0.797) $>$ Random OCC (0.789) $>$ Cutoff (0.783) $>$ Depth (0.780) $=$ Vanilla (0.780) places Depth at the bottom of the gradient-flow conditions. The 1.7pp gap between Full OCC and Depth, and the 0.9pp gap between Random OCC and Depth, are within cross-seed variance ($\\sigma \\approx 0.031$--$0.039$) and not individually significant. However, the consistent ordering---both OCC conditions above Depth despite using different label content---suggests that the BEV auxiliary head architecture may provide a marginally stronger gradient signal than the depth head, independent of label content.\n\n\\textbf{Depth exhibits high cross-seed variance on hard tasks.} On Task~3, Depth CAR ranges from 0.20 to 0.78 across 4 seeds (mean 0.50); on Task~6, it ranges from 0.16 to 0.84 (mean 0.54). This variance exceeds that of other conditions on the same tasks and is consistent with the broader finding that auxiliary supervision amplifies seed sensitivity relative to Vanilla ($\\sigma = 0.012$). The 4-seed design mitigates this variance in the overall mean but limits per-task conclusions.\n\n\\textbf{Spatial content is confirmed as secondary.} Across three distinct auxiliary label types---structured BEV occupancy (Full OCC, 0.797), random binary labels (Random OCC, 0.789), and egocentric depth maps (Depth, 0.780)---all gradient-flow conditions achieve CAR within 1.7pp of Vanilla, while the gradient-blocked condition (Detach, 0.746) falls 3.4pp below. The 1.7pp spread among gradient-flow conditions is smaller than the 3.4pp Detach deficit, confirming that gradient flow presence is the dominant factor and label content contributes at most marginally.\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 19,
        "newStart": 19,
        "newLines": 19,
        "lines": [
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. All values are means across seeds; $\\pm$ indicates one standard deviation. Conditions are ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds; all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}",
          "+\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. $\\pm$ indicates one standard deviation across seeds. Bootstrap 95\\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}",
          " \\label{tab:main_results}",
          "-\\begin{tabular}{lcccc}",
          "+\\begin{tabular}{lccccc}",
          " \\toprule",
          "-Condition & Seeds & TSR & CAR & $\\Delta$CAR \\\\",
          "+Condition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\",
          " \\midrule",
          "-Full OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & $+$1.7 \\\\",
          "-Random OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & $+$0.9 \\\\",
          "-Vanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & ---    \\\\",
          "-Detach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & $-$3.4 \\\\",
          "+Full OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.776, .817] & $+$1.7 \\\\",
          "+Random OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.767, .809] & $+$0.9 \\\\",
          "+Vanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.759, .801] & ---    \\\\",
          "+Detach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.723, .768] & $-$3.4 \\\\",
          " \\midrule",
          "-Depth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & 0.0 \\\\",
          "-Cutoff$^\\dagger$  & 2 & 0.915             & 0.783             & $+$0.3 \\\\",
          "+Depth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.762, .797] & 0.0 \\\\",
          "+Cutoff$^\\dagger$  & 2 & 0.915 $\\pm$ 0.004 & 0.783 $\\pm$ 0.021 & [.757, .808] & $+$0.3 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01QXXA5rSxBuZUXgzv2jNppp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.",
  "new_string": "\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "863a3e05-0333-46d5-a0e9-7afad1c07f8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKHXRTJEiGoN1EBA5Vvfp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1264,
      "cache_read_input_tokens": 41410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1264
      },
      "output_tokens": 46,
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

_source line 16 · 2026-05-23T06:55:23.977Z_

<details><summary>↩ Tool result · `toolu_01QXXA5rSxBuZUXgzv2jNppp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "169e2e57-af83-4f49-b756-301fd772bfca",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.",
    "newString": "\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nWe report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise.\n\nTable~\\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.\n\n\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.\n\n\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.\n\n\\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.\n\n\\textbf{TSR is stable for gradient-flow conditions but unstable under Detach.} For non-Detach conditions, TSR ranges from 0.869 (Random OCC) to 0.915 (Cutoff\\textsuperscript{\\dag}), with standard deviations $\\leq 0.050$. Detaching gradients destabilizes task execution: Detach OCC achieves mean TSR of 0.812 with $\\sigma = 0.163$---an order of magnitude higher variance than any other condition. One Detach seed (seed 44) exhibits broad performance collapse (TSR = 0.624), with all ten tasks degraded relative to the other two Detach seeds (0.914, 0.898). This collapse affects action prediction uniformly (CAR remains 0.748, comparable to the other seeds), suggesting that gradient detachment amplifies sensitivity to initialization for motor learning while leaving collision behavior intact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. $\\pm$ indicates one standard deviation across seeds. Bootstrap 95\\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.776, .817] & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.767, .809] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.759, .801] & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.723, .768] & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.762, .797] & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915 $\\pm$ 0.004 & 0.783 $\\pm$ 0.021 & [.757, .808] & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Mechanism Analysis}\n\\label{sec:mechanism}\n\nThe four completed conditions form a $2 \\times 2$ factorial structure crossing gradient flow (ON/OFF) with label content (structured/random or none). Table~\\ref{tab:factorial} arranges the CAR values in this matrix.\n\n\\begin{table}[t]\n\\centering\n\\caption{Factorial decomposition of CAR by gradient flow and label content. Each cell shows the condition name and mean CAR. The column effect (gradient flow) dominates: both ON cells exceed their OFF counterparts. Vanilla (no auxiliary head) occupies the ``Gradient OFF / Random or no labels'' cell as the natural baseline for both factors.}\n\\label{tab:factorial}\n\\begin{tabular}{lcc}\n\\toprule\n & Gradient ON & Gradient OFF \\\\\n\\midrule\nStructured labels    & Full OCC (0.797) & Detach OCC (0.746) \\\\\nRandom / no labels   & Random OCC (0.789) & Vanilla (0.780) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\\ Vanilla 0.780). The dominant pattern is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.\n\n\\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\\sigma \\approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\\ref{sec:why_detach}).\n\n\\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \\emph{below} Vanilla rather than matching it.\n\n\\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OCC exhibits uniquely high TSR variance ($\\sigma = 0.163$, vs.\\ $< 0.050$ for all other conditions). One Detach seed (seed~44) shows TSR = 0.624 with uniform degradation across all ten tasks, while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation---intact collision behavior with collapsed task execution---suggests that gradient detachment amplifies optimization instability for action prediction specifically, consistent with the encoder bearing forward-pass interference from the auxiliary head without receiving compensating gradient signal.\n\nThree candidate mechanisms---anti-overfitting regularization, loss landscape smoothing, and gradient diversity---can account for the gradient flow effect. All three predict that gradient flow is necessary and label content is secondary. Section~\\ref{sec:why_gradient} develops these hypotheses; the current data cannot distinguish between them.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Per-task CAR spans from 0.07 (Task~5, Vanilla) to 1.00 (Tasks~8, 9), revealing a bimodal distribution: seven tasks achieve mean CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks---Tasks~3, 5, and 6---fall below 0.58. The overall CAR of 0.780 is dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task mean CAR across seeds for each condition (50 rollouts per seed). All conditions use 3 seeds except Depth (4 seeds) and Cutoff$^\\dagger$ (2 seeds).}\n\\label{tab:per_task}\n\\begin{tabular}{clcccccc}\n\\toprule\n & & \\multicolumn{6}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-8}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Depth & Cutoff$^\\dagger$ \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.93 & 0.94 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.50 & 0.66 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.92 & 0.98 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.08 & 0.00 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.54 & 0.37 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 0.96 & 0.97 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.780 & 0.783 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects compress overall differences.} Seven of ten tasks already achieve CAR $\\geq$ 0.92 under Vanilla, leaving minimal room for auxiliary training to improve. On these easy tasks, the obstacle is spatially separated from the manipulation path, and the demonstration policy already avoids contact. Any measurable effect of gradient flow on CAR concentrates on the three hard tasks where the Vanilla baseline is low.\n\n\\textbf{Task~5 is universally difficult.} With Vanilla CAR of 0.07, Task~5 provides the most headroom for improvement, yet no condition achieves CAR above 0.23. Gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain extremely low---the policy contacts the obstacle in at least 77\\% of episodes regardless of training condition. The Detach deficit is consistent with the overall pattern (lowest among all conditions), but the absolute gains from gradient flow are modest relative to the task difficulty.\n\n\\textbf{Tasks~3 and 6 decouple success from safety.} Both tasks achieve near-perfect TSR with CAR below 0.61---the robot completes the goal while colliding in roughly half of episodes. Detach OCC is systematically the worst on Task~3 (CAR 0.11 vs.\\ 0.31--0.38 for all other conditions), consistent with gradient detachment amplifying degradation on physically constrained tasks. Among gradient-flow conditions, however, no consistent ordering emerges: on Task~3, Vanilla (0.38) matches or exceeds Full OCC (0.37) and Random OCC (0.31); on Task~6, Full OCC (0.61) and Vanilla (0.57) lead while Random OCC (0.55) trails. This lack of consistent ranking among gradient-flow conditions on hard tasks reinforces the damage-prevention interpretation: gradient flow prevents the Detach-specific degradation but does not systematically improve clearance beyond Vanilla. The Depth condition (4 seeds) confirms this pattern: Task~3 CAR of 0.50 exceeds Vanilla (0.38) but with extreme cross-seed variance (range 0.20--0.78), while Task~6 (0.54) falls below Vanilla (0.57). Cutoff achieves the highest Task~3 CAR (0.66, 2 seeds) but the lowest Task~5 CAR (0.00) and Task~6 CAR (0.37), further illustrating the absence of any consistent condition advantage on hard tasks.\n\n\n\\subsection{Temporal Dynamics}\n\\label{sec:temporal}\n\nThe Cutoff condition applies occupancy supervision with gradient flow for the first 35{,}000 training steps, then disables the auxiliary loss for the remaining 15{,}000 steps. This condition tests whether the gradient flow effect requires continuous auxiliary supervision or whether early-phase exposure is sufficient.\n\n\\textbf{Cutoff partially preserves the gradient flow effect.} Cutoff achieves CAR of 0.783 (2 seeds), falling between Vanilla (0.780) and Full OCC (0.797) but closer to Vanilla ($+$0.3pp vs.\\ Vanilla, compared to Full OCC's $+$1.7pp). Removing auxiliary gradients for the final 30\\% of training erodes most of the CAR advantage that continuous gradient flow provides, suggesting that the encoder partially reverts toward action-specialized features when auxiliary gradients are withdrawn.\n\n\\textbf{Cutoff remains well above Detach.} The 3.7pp gap between Cutoff (0.783) and Detach OCC (0.746) indicates that 35{,}000 steps of gradient flow provide substantial and partially durable protection against the degradation observed under full gradient detachment. The early-phase auxiliary gradients establish encoder representations that do not fully collapse when the auxiliary signal is removed, even though they do not maintain the full benefit of continuous gradient flow.\n\n\\textbf{Early-phase training durably improves task completion.} Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla, 0.894 Full OCC), suggesting that 35{,}000 steps of auxiliary gradient flow provide a lasting benefit to action prediction that persists---and may even improve---when auxiliary gradients are subsequently removed. This TSR--CAR dissociation reveals distinct temporal requirements: task completion benefits durably from early-phase auxiliary training, while collision avoidance requires continuous gradient flow to be maintained.\n\n\\textbf{Hard tasks expose the cost of removing late-stage gradient flow.} On Task~5, Cutoff achieves CAR of 0.00 across both seeds---the worst performance of any condition on any task, including Detach (0.05). Full OCC (0.17) and Random OCC (0.23) achieve non-zero T5 CAR with continuous gradient flow. This complete failure on the hardest safety task under early-only gradient flow indicates that collision avoidance on physically constrained tasks depends on auxiliary gradients throughout training, not only during the initial learning phase. On Task~3, Cutoff achieves the highest CAR of any condition (0.66), demonstrating that the temporal sensitivity is task-specific rather than uniform. Cutoff uses 2 seeds; a third seed is in progress.\n\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_results}\n\nThe Depth condition replaces BEV occupancy supervision with egocentric monocular depth prediction (Section~\\ref{sec:depth_head}), holding the auxiliary training mechanism constant---same architecture, same loss weight schedule, same gradient flow through DINOv2 and SigLIP encoders. This comparison isolates whether the spatial reference frame or the type of spatial information affects the gradient flow effect, using 4 seeds (42, 43, 44, 45) for additional statistical power.\n\n\\textbf{Depth matches Vanilla exactly.} Depth achieves mean CAR of 0.780 $\\pm$ 0.039 across 4 seeds---identical to Vanilla (0.780 $\\pm$ 0.012). Despite providing per-pixel geometric information directly aligned with collision avoidance (nearby surfaces produce small depth values), egocentric depth supervision does not improve CAR beyond the no-auxiliary baseline. This result, combined with Random OCC (0.789) achieving comparable CAR with random binary labels, confirms that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to the presence of gradient flow itself.\n\n\\textbf{Depth falls below both OCC conditions.} The ordering Full OCC (0.797) $>$ Random OCC (0.789) $>$ Cutoff (0.783) $>$ Depth (0.780) $=$ Vanilla (0.780) places Depth at the bottom of the gradient-flow conditions. The 1.7pp gap between Full OCC and Depth, and the 0.9pp gap between Random OCC and Depth, are within cross-seed variance ($\\sigma \\approx 0.031$--$0.039$) and not individually significant. However, the consistent ordering---both OCC conditions above Depth despite using different label content---suggests that the BEV auxiliary head architecture may provide a marginally stronger gradient signal than the depth head, independent of label content.\n\n\\textbf{Depth exhibits high cross-seed variance on hard tasks.} On Task~3, Depth CAR ranges from 0.20 to 0.78 across 4 seeds (mean 0.50); on Task~6, it ranges from 0.16 to 0.84 (mean 0.54). This variance exceeds that of other conditions on the same tasks and is consistent with the broader finding that auxiliary supervision amplifies seed sensitivity relative to Vanilla ($\\sigma = 0.012$). The 4-seed design mitigates this variance in the overall mean but limits per-task conclusions.\n\n\\textbf{Spatial content is confirmed as secondary.} Across three distinct auxiliary label types---structured BEV occupancy (Full OCC, 0.797), random binary labels (Random OCC, 0.789), and egocentric depth maps (Depth, 0.780)---all gradient-flow conditions achieve CAR within 1.7pp of Vanilla, while the gradient-blocked condition (Detach, 0.746) falls 3.4pp below. The 1.7pp spread among gradient-flow conditions is smaller than the 3.4pp Detach deficit, confirming that gradient flow presence is the dominant factor and label content contributes at most marginally.\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " Table~\\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.",
          " ",
          "-\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) differ from Vanilla (0.780, 3 seeds) by less than one standard deviation. Blocking gradient flow, however, causes significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla. This asymmetry---gradient-flow conditions near Vanilla, gradient-blocked condition well below---indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.",
          "+\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.",
          " ",
          " \\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.",
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

_source line 17_

Now let me update the label content paragraph to add CI-consistent language.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "3a4ed1bf-0daf-46e4-8bf2-0a991e851efe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3tq4xWqKhi64twNAcyQVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 42674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 582
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

<details open><summary>🔧 Tool call — Edit · `toolu_01XcEpnSgKHxqhDQx3Fa2NTJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.",
  "new_string": "\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$) whose bootstrap CI overlaps broadly. Random binary labels, containing no spatial information, match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "b2890ce8-72e6-4c58-8434-907bee5ac51f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3tq4xWqKhi64twNAcyQVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 42674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 582
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

_source line 19 · 2026-05-23T06:55:31.955Z_

<details><summary>↩ Tool result · `toolu_01XcEpnSgKHxqhDQx3Fa2NTJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "c5035375-6674-4b68-afa0-53880b98e918",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.",
    "newString": "\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$) whose bootstrap CI overlaps broadly. Random binary labels, containing no spatial information, match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nWe report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise.\n\nTable~\\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.\n\n\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.\n\n\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.\n\n\\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.\n\n\\textbf{TSR is stable for gradient-flow conditions but unstable under Detach.} For non-Detach conditions, TSR ranges from 0.869 (Random OCC) to 0.915 (Cutoff\\textsuperscript{\\dag}), with standard deviations $\\leq 0.050$. Detaching gradients destabilizes task execution: Detach OCC achieves mean TSR of 0.812 with $\\sigma = 0.163$---an order of magnitude higher variance than any other condition. One Detach seed (seed 44) exhibits broad performance collapse (TSR = 0.624), with all ten tasks degraded relative to the other two Detach seeds (0.914, 0.898). This collapse affects action prediction uniformly (CAR remains 0.748, comparable to the other seeds), suggesting that gradient detachment amplifies sensitivity to initialization for motor learning while leaving collision behavior intact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. $\\pm$ indicates one standard deviation across seeds. Bootstrap 95\\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.776, .817] & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.767, .809] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.759, .801] & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.723, .768] & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.762, .797] & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915 $\\pm$ 0.004 & 0.783 $\\pm$ 0.021 & [.757, .808] & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Mechanism Analysis}\n\\label{sec:mechanism}\n\nThe four completed conditions form a $2 \\times 2$ factorial structure crossing gradient flow (ON/OFF) with label content (structured/random or none). Table~\\ref{tab:factorial} arranges the CAR values in this matrix.\n\n\\begin{table}[t]\n\\centering\n\\caption{Factorial decomposition of CAR by gradient flow and label content. Each cell shows the condition name and mean CAR. The column effect (gradient flow) dominates: both ON cells exceed their OFF counterparts. Vanilla (no auxiliary head) occupies the ``Gradient OFF / Random or no labels'' cell as the natural baseline for both factors.}\n\\label{tab:factorial}\n\\begin{tabular}{lcc}\n\\toprule\n & Gradient ON & Gradient OFF \\\\\n\\midrule\nStructured labels    & Full OCC (0.797) & Detach OCC (0.746) \\\\\nRandom / no labels   & Random OCC (0.789) & Vanilla (0.780) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\\ Vanilla 0.780). The dominant pattern is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.\n\n\\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\\sigma \\approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\\ref{sec:why_detach}).\n\n\\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \\emph{below} Vanilla rather than matching it.\n\n\\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OCC exhibits uniquely high TSR variance ($\\sigma = 0.163$, vs.\\ $< 0.050$ for all other conditions). One Detach seed (seed~44) shows TSR = 0.624 with uniform degradation across all ten tasks, while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation---intact collision behavior with collapsed task execution---suggests that gradient detachment amplifies optimization instability for action prediction specifically, consistent with the encoder bearing forward-pass interference from the auxiliary head without receiving compensating gradient signal.\n\nThree candidate mechanisms---anti-overfitting regularization, loss landscape smoothing, and gradient diversity---can account for the gradient flow effect. All three predict that gradient flow is necessary and label content is secondary. Section~\\ref{sec:why_gradient} develops these hypotheses; the current data cannot distinguish between them.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Per-task CAR spans from 0.07 (Task~5, Vanilla) to 1.00 (Tasks~8, 9), revealing a bimodal distribution: seven tasks achieve mean CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks---Tasks~3, 5, and 6---fall below 0.58. The overall CAR of 0.780 is dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task mean CAR across seeds for each condition (50 rollouts per seed). All conditions use 3 seeds except Depth (4 seeds) and Cutoff$^\\dagger$ (2 seeds).}\n\\label{tab:per_task}\n\\begin{tabular}{clcccccc}\n\\toprule\n & & \\multicolumn{6}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-8}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Depth & Cutoff$^\\dagger$ \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.93 & 0.94 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.50 & 0.66 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.92 & 0.98 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.08 & 0.00 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.54 & 0.37 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 0.96 & 0.97 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.780 & 0.783 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects compress overall differences.} Seven of ten tasks already achieve CAR $\\geq$ 0.92 under Vanilla, leaving minimal room for auxiliary training to improve. On these easy tasks, the obstacle is spatially separated from the manipulation path, and the demonstration policy already avoids contact. Any measurable effect of gradient flow on CAR concentrates on the three hard tasks where the Vanilla baseline is low.\n\n\\textbf{Task~5 is universally difficult.} With Vanilla CAR of 0.07, Task~5 provides the most headroom for improvement, yet no condition achieves CAR above 0.23. Gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain extremely low---the policy contacts the obstacle in at least 77\\% of episodes regardless of training condition. The Detach deficit is consistent with the overall pattern (lowest among all conditions), but the absolute gains from gradient flow are modest relative to the task difficulty.\n\n\\textbf{Tasks~3 and 6 decouple success from safety.} Both tasks achieve near-perfect TSR with CAR below 0.61---the robot completes the goal while colliding in roughly half of episodes. Detach OCC is systematically the worst on Task~3 (CAR 0.11 vs.\\ 0.31--0.38 for all other conditions), consistent with gradient detachment amplifying degradation on physically constrained tasks. Among gradient-flow conditions, however, no consistent ordering emerges: on Task~3, Vanilla (0.38) matches or exceeds Full OCC (0.37) and Random OCC (0.31); on Task~6, Full OCC (0.61) and Vanilla (0.57) lead while Random OCC (0.55) trails. This lack of consistent ranking among gradient-flow conditions on hard tasks reinforces the damage-prevention interpretation: gradient flow prevents the Detach-specific degradation but does not systematically improve clearance beyond Vanilla. The Depth condition (4 seeds) confirms this pattern: Task~3 CAR of 0.50 exceeds Vanilla (0.38) but with extreme cross-seed variance (range 0.20--0.78), while Task~6 (0.54) falls below Vanilla (0.57). Cutoff achieves the highest Task~3 CAR (0.66, 2 seeds) but the lowest Task~5 CAR (0.00) and Task~6 CAR (0.37), further illustrating the absence of any consistent condition advantage on hard tasks.\n\n\n\\subsection{Temporal Dynamics}\n\\label{sec:temporal}\n\nThe Cutoff condition applies occupancy supervision with gradient flow for the first 35{,}000 training steps, then disables the auxiliary loss for the remaining 15{,}000 steps. This condition tests whether the gradient flow effect requires continuous auxiliary supervision or whether early-phase exposure is sufficient.\n\n\\textbf{Cutoff partially preserves the gradient flow effect.} Cutoff achieves CAR of 0.783 (2 seeds), falling between Vanilla (0.780) and Full OCC (0.797) but closer to Vanilla ($+$0.3pp vs.\\ Vanilla, compared to Full OCC's $+$1.7pp). Removing auxiliary gradients for the final 30\\% of training erodes most of the CAR advantage that continuous gradient flow provides, suggesting that the encoder partially reverts toward action-specialized features when auxiliary gradients are withdrawn.\n\n\\textbf{Cutoff remains well above Detach.} The 3.7pp gap between Cutoff (0.783) and Detach OCC (0.746) indicates that 35{,}000 steps of gradient flow provide substantial and partially durable protection against the degradation observed under full gradient detachment. The early-phase auxiliary gradients establish encoder representations that do not fully collapse when the auxiliary signal is removed, even though they do not maintain the full benefit of continuous gradient flow.\n\n\\textbf{Early-phase training durably improves task completion.} Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla, 0.894 Full OCC), suggesting that 35{,}000 steps of auxiliary gradient flow provide a lasting benefit to action prediction that persists---and may even improve---when auxiliary gradients are subsequently removed. This TSR--CAR dissociation reveals distinct temporal requirements: task completion benefits durably from early-phase auxiliary training, while collision avoidance requires continuous gradient flow to be maintained.\n\n\\textbf{Hard tasks expose the cost of removing late-stage gradient flow.} On Task~5, Cutoff achieves CAR of 0.00 across both seeds---the worst performance of any condition on any task, including Detach (0.05). Full OCC (0.17) and Random OCC (0.23) achieve non-zero T5 CAR with continuous gradient flow. This complete failure on the hardest safety task under early-only gradient flow indicates that collision avoidance on physically constrained tasks depends on auxiliary gradients throughout training, not only during the initial learning phase. On Task~3, Cutoff achieves the highest CAR of any condition (0.66), demonstrating that the temporal sensitivity is task-specific rather than uniform. Cutoff uses 2 seeds; a third seed is in progress.\n\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_results}\n\nThe Depth condition replaces BEV occupancy supervision with egocentric monocular depth prediction (Section~\\ref{sec:depth_head}), holding the auxiliary training mechanism constant---same architecture, same loss weight schedule, same gradient flow through DINOv2 and SigLIP encoders. This comparison isolates whether the spatial reference frame or the type of spatial information affects the gradient flow effect, using 4 seeds (42, 43, 44, 45) for additional statistical power.\n\n\\textbf{Depth matches Vanilla exactly.} Depth achieves mean CAR of 0.780 $\\pm$ 0.039 across 4 seeds---identical to Vanilla (0.780 $\\pm$ 0.012). Despite providing per-pixel geometric information directly aligned with collision avoidance (nearby surfaces produce small depth values), egocentric depth supervision does not improve CAR beyond the no-auxiliary baseline. This result, combined with Random OCC (0.789) achieving comparable CAR with random binary labels, confirms that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to the presence of gradient flow itself.\n\n\\textbf{Depth falls below both OCC conditions.} The ordering Full OCC (0.797) $>$ Random OCC (0.789) $>$ Cutoff (0.783) $>$ Depth (0.780) $=$ Vanilla (0.780) places Depth at the bottom of the gradient-flow conditions. The 1.7pp gap between Full OCC and Depth, and the 0.9pp gap between Random OCC and Depth, are within cross-seed variance ($\\sigma \\approx 0.031$--$0.039$) and not individually significant. However, the consistent ordering---both OCC conditions above Depth despite using different label content---suggests that the BEV auxiliary head architecture may provide a marginally stronger gradient signal than the depth head, independent of label content.\n\n\\textbf{Depth exhibits high cross-seed variance on hard tasks.} On Task~3, Depth CAR ranges from 0.20 to 0.78 across 4 seeds (mean 0.50); on Task~6, it ranges from 0.16 to 0.84 (mean 0.54). This variance exceeds that of other conditions on the same tasks and is consistent with the broader finding that auxiliary supervision amplifies seed sensitivity relative to Vanilla ($\\sigma = 0.012$). The 4-seed design mitigates this variance in the overall mean but limits per-task conclusions.\n\n\\textbf{Spatial content is confirmed as secondary.} Across three distinct auxiliary label types---structured BEV occupancy (Full OCC, 0.797), random binary labels (Random OCC, 0.789), and egocentric depth maps (Depth, 0.780)---all gradient-flow conditions achieve CAR within 1.7pp of Vanilla, while the gradient-blocked condition (Detach, 0.746) falls 3.4pp below. The 1.7pp spread among gradient-flow conditions is smaller than the 3.4pp Detach deficit, confirming that gradient flow presence is the dominant factor and label content contributes at most marginally.\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 7,
        "newStart": 11,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.",
          " ",
          "-\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$). Random binary labels---containing no spatial information---match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.",
          "+\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$) whose bootstrap CI overlaps broadly. Random binary labels, containing no spatial information, match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.",
          " ",
          " \\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.",
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

_source line 20_

Now let me check the mechanism analysis section and other paragraphs that reference Table 1 data for consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "8189ea7a-d017-449e-9f9e-7b3072dddb17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Wv1VfkPDo4MYYSXHjvC8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 43256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_018kmsWJrWoCD8yq7eZc5nxq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "offset": 55,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "504a61ed-ff2f-4401-af25-c295ac7f9b53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Wv1VfkPDo4MYYSXHjvC8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 43256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 22 · 2026-05-23T06:55:35.677Z_

<details><summary>↩ Tool result · `toolu_018kmsWJrWoCD8yq7eZc5nxq`</summary>

```text
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\ Vanilla 0.780). The dominant pattern is not that gradient flow \emph{improves} CAR above Vanilla, but that its \emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.
60	
61	\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\sigma \approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\ref{sec:why_detach}).
62	
63	\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \emph{below} Vanilla rather than matching it.
64	
65	\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OCC exhibits uniquely high TSR variance ($\sigma = 0.163$, vs.\ $< 0.050$ for all other conditions). One Detach seed (seed~44) shows TSR = 0.624 with uniform degradation across all ten tasks, while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation---intact collision behavior with collapsed task execution---suggests that gradient detachment amplifies optimization instability for action prediction specifically, consistent with the encoder bearing forward-pass interference from the auxiliary head without receiving compensating gradient signal.
66	
67	Three candidate mechanisms---anti-overfitting regularization, loss landscape smoothing, and gradient diversity---can account for the gradient flow effect. All three predict that gradient flow is necessary and label content is secondary. Section~\ref{sec:why_gradient} develops these hypotheses; the current data cannot distinguish between them.
68	
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "3058223c-a1a6-41c7-9346-8641acc455c2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Gradient flow prevents auxiliary-head degradation.} The column effect---gradient ON minus gradient OFF---is $+$5.1 percentage points with structured labels (Full OCC 0.797 vs.\\ Detach OCC 0.746) and $+$0.9 percentage points with random or no labels (Random OCC 0.789 vs.\\ Vanilla 0.780). The dominant pattern is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla: Detach OCC falls 3.4pp below Vanilla, while gradient-flow conditions remain within 1.7pp of it. Gradient flow is thus a necessary condition for auxiliary heads to avoid harming collision avoidance.\n\n\\textbf{Label content contributes marginally.} The row effect---structured minus random/none---is $+$0.8pp when gradient flows (Full OCC 0.797 vs.\\ Random OCC 0.789) and $-$3.4pp when it does not (Detach OCC 0.746 vs.\\ Vanilla 0.780). With gradient flow, structured labels provide a negligible advantage over random labels (0.8pp, well within $\\sigma \\approx 0.031$). Without gradient flow, structured labels are associated with worse performance, but this comparison conflates label content with the forward-pass interference specific to the Detach architecture (Section~\\ref{sec:why_detach}).\n\n\\textbf{Detach incurs a forward-pass cost without gradient compensation.} The asymmetry in gradient flow effects ($+$5.1pp with structured labels vs.\\ $+$0.9pp with random/none) reflects the specific penalty of the Detach condition. Detach OCC and Vanilla both lack encoder gradients from the auxiliary loss, but Detach still runs the auxiliary head in the forward pass, introducing BatchNorm statistics that the encoder cannot adapt to without auxiliary gradients. This forward-pass interference without compensating gradient signal explains why Detach falls \\emph{below} Vanilla rather than matching it.\n\n\\textbf{Detaching gradients destabilizes action learning.} Beyond CAR degradation, Detach OCC exhibits uniquely high TSR variance ($\\sigma = 0.163$, vs.\\ $< 0.050$ for all other conditions). One Detach seed (seed~44) shows TSR = 0.624 with uniform degradation across all ten tasks, while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation---intact collision behavior with collapsed task execution---suggests that gradient detachment amplifies optimization instability for action prediction specifically, consistent with the encoder bearing forward-pass interference from the auxiliary head without receiving compensating gradient signal.\n\nThree candidate mechanisms---anti-overfitting regularization, loss landscape smoothing, and gradient diversity---can account for the gradient flow effect. All three predict that gradient flow is necessary and label content is secondary. Section~\\ref{sec:why_gradient} develops these hypotheses; the current data cannot distinguish between them.\n\n",
      "numLines": 15,
      "startLine": 55,
      "totalLines": 134
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
The mechanism analysis section (lines 59-67) references Table 1 numbers but doesn't make statistical significance claims that conflict with the CI data. The em-dashes are present but fixing those wasn't requested. The numbers are consistent.

Let me also check the Cutoff and Depth sections for consistency. Let me look at the Cutoff section specifically since we added ±std there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "a451f315-7d69-4c0a-8bc1-693e37eb46c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lw3xnWtYjD7Eio8rdoQJDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 43662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1036
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

_source line 24_

The mechanism analysis paragraphs (lines 59-67) use the same numbers and don't make significance claims that conflict with the CI results. The Cutoff and Depth sections (which I already read) are also consistent with the CI data.

Let me verify the final state of the edited regions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "a862fcf9-d296-458e-b8ca-b7b8aed14894",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lw3xnWtYjD7Eio8rdoQJDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 43662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1036
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01SmaXtsFhQa8kFoTKD8G9CN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "offset": 1,
  "limit": 42
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "0cc46a29-fcdc-4883-b453-d9c6be65e907",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lw3xnWtYjD7Eio8rdoQJDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 43662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1036
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

_source line 26 · 2026-05-23T06:55:42.973Z_

<details><summary>↩ Tool result · `toolu_01SmaXtsFhQa8kFoTKD8G9CN`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	\label{sec:main_results}
7	
8	We report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise.
9	
10	Table~\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.
11	
12	\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.
13	
14	\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\ 0.789), a gap within cross-seed variance ($\sigma \approx 0.031$) whose bootstrap CI overlaps broadly. Random binary labels, containing no spatial information, match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.
15	
16	\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.
17	
18	\textbf{TSR is stable for gradient-flow conditions but unstable under Detach.} For non-Detach conditions, TSR ranges from 0.869 (Random OCC) to 0.915 (Cutoff\textsuperscript{\dag}), with standard deviations $\leq 0.050$. Detaching gradients destabilizes task execution: Detach OCC achieves mean TSR of 0.812 with $\sigma = 0.163$---an order of magnitude higher variance than any other condition. One Detach seed (seed 44) exhibits broad performance collapse (TSR = 0.624), with all ten tasks degraded relative to the other two Detach seeds (0.914, 0.898). This collapse affects action prediction uniformly (CAR remains 0.748, comparable to the other seeds), suggesting that gradient detachment amplifies sensitivity to initialization for motor learning while leaving collision behavior intact.
19	
20	\begin{table}[t]
21	\centering
22	\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\Delta$CAR: difference from Vanilla in percentage points. $\pm$ indicates one standard deviation across seeds. Bootstrap 95\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}
23	\label{tab:main_results}
24	\begin{tabular}{lccccc}
25	\toprule
26	Condition & Seeds & TSR & CAR & $95\%$ CI & $\Delta$CAR \\
27	\midrule
28	Full OCC      & 3 & 0.894 $\pm$ 0.050 & \textbf{0.797} $\pm$ 0.032 & [.776, .817] & $+$1.7 \\
29	Random OCC    & 3 & 0.869 $\pm$ 0.029 & 0.789 $\pm$ 0.031 & [.767, .809] & $+$0.9 \\
30	Vanilla       & 3 & 0.907 $\pm$ 0.009 & 0.780 $\pm$ 0.012 & [.759, .801] & ---    \\
31	Detach OCC    & 3 & 0.812 $\pm$ 0.163 & 0.746 $\pm$ 0.002 & [.723, .768] & $-$3.4 \\
32	\midrule
33	Depth             & 4 & 0.889 $\pm$ 0.042 & 0.780 $\pm$ 0.039 & [.762, .797] & 0.0 \\
34	Cutoff$^\dagger$  & 2 & 0.915 $\pm$ 0.004 & 0.783 $\pm$ 0.021 & [.757, .808] & $+$0.3 \\
35	\bottomrule
36	\end{tabular}
37	\end{table}
38	
39	
40	\subsection{Mechanism Analysis}
41	\label{sec:mechanism}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "4f80120a-788f-43a2-b689-13eebef73e04",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nWe report mean and standard deviation across $N$ seeds per condition, with 50 rollouts per task (500 total episodes per seed). Given the limited seed counts (2--4 per condition), we supplement point estimates with bootstrap 95\\% confidence intervals (CIs) computed via 10{,}000 hierarchical resamples (percentile method) to quantify uncertainty in mean CAR. All results use the 50{,}000-step checkpoint unless noted otherwise.\n\nTable~\\ref{tab:main_results} summarizes overall TSR and CAR across conditions. Four patterns emerge.\n\n\\textbf{Gradient flow is necessary to prevent auxiliary-head degradation.} Adding an auxiliary head with gradient flow yields CAR comparable to Vanilla: Full OCC (0.797, 3 seeds) and Random OCC (0.789, 3 seeds) exceed Vanilla (0.780, 3 seeds) by less than one standard deviation. The Full OCC $\\Delta$CAR of $+$1.7pp is directionally positive but not statistically significant (bootstrap 95\\% CI for the pairwise difference includes zero). Blocking gradient flow causes statistically significant degradation: Detach OCC (0.746, 3 seeds) falls 3.4 percentage points below Vanilla, and bootstrap 95\\% CIs for all pairwise differences between Detach OCC and other conditions exclude zero. This asymmetry (gradient-flow conditions near Vanilla, gradient-blocked condition well below) indicates that gradient flow is a necessary condition for an auxiliary head to avoid harming collision avoidance.\n\n\\textbf{Label content is secondary.} Full OCC and Random OCC differ by 0.8 percentage points in CAR (0.797 vs.\\ 0.789), a gap within cross-seed variance ($\\sigma \\approx 0.031$) whose bootstrap CI overlaps broadly. Random binary labels, containing no spatial information, match structured occupancy labels in collision avoidance, consistent with gradient flow presence rather than spatial content as the operative factor.\n\n\\textbf{Gradient-flow advantage is checkpoint-sensitive.} At an earlier checkpoint (step 47{,}500), Full OCC and Vanilla yield identical mean CAR (0.780), suggesting that the CAR advantage of gradient-flow conditions emerges late in training and is sensitive to checkpoint selection. The ordering (Full OCC $>$ Random OCC $>$ Vanilla $>$ Detach OCC) is consistent at both checkpoints, but the magnitude of the gradient-flow--Vanilla gap depends on the evaluation point.\n\n\\textbf{TSR is stable for gradient-flow conditions but unstable under Detach.} For non-Detach conditions, TSR ranges from 0.869 (Random OCC) to 0.915 (Cutoff\\textsuperscript{\\dag}), with standard deviations $\\leq 0.050$. Detaching gradients destabilizes task execution: Detach OCC achieves mean TSR of 0.812 with $\\sigma = 0.163$---an order of magnitude higher variance than any other condition. One Detach seed (seed 44) exhibits broad performance collapse (TSR = 0.624), with all ten tasks degraded relative to the other two Detach seeds (0.914, 0.898). This collapse affects action prediction uniformly (CAR remains 0.748, comparable to the other seeds), suggesting that gradient detachment amplifies sensitivity to initialization for motor learning while leaving collision behavior intact.\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). TSR: Task Success Rate. CAR: Collision Avoidance Rate. $\\Delta$CAR: difference from Vanilla in percentage points. $\\pm$ indicates one standard deviation across seeds. Bootstrap 95\\% CIs computed via 10{,}000 hierarchical resamples (percentile method). Conditions ordered by CAR within each group. $^\\dagger$Cutoff uses 2 seeds (to be updated after seed~2 evaluation); all other conditions use 3--4 seeds. All values use the 50{,}000-step checkpoint.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nFull OCC      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [.776, .817] & $+$1.7 \\\\\nRandom OCC    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [.767, .809] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [.759, .801] & ---    \\\\\nDetach OCC    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [.723, .768] & $-$3.4 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [.762, .797] & 0.0 \\\\\nCutoff$^\\dagger$  & 2 & 0.915 $\\pm$ 0.004 & 0.783 $\\pm$ 0.021 & [.757, .808] & $+$0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Mechanism Analysis}\n\\label{sec:mechanism}\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 134
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

变更总结：

1. **开头段落**（L8）：将"formal significance requires additional replications"替换为 bootstrap CI 方法描述。

2. **Table 1**（L20-37）：
   - 新增 `$95\%$ CI` 列，格式 `[.776, .817]`（省略前导零，紧凑）
   - Cutoff 行补充了 ±std（TSR ±0.004, CAR ±0.021）
   - Caption 加入 bootstrap 方法说明和 Cutoff † 脚注更新

3. **Gradient flow 段落**（L12）：
   - Full OCC vs Vanilla：明确 "$+$1.7pp is directionally positive but not statistically significant (bootstrap 95\% CI for the pairwise difference includes zero)"
   - Detach OCC：明确 "statistically significant degradation" + "bootstrap 95\% CIs for all pairwise differences... exclude zero"
   - 修复了 em-dash `---` 为括号格式

4. **Label content 段落**（L14）：补充 "whose bootstrap CI overlaps broadly"，修复 em-dash。

Mechanism analysis（L59-67）、Cutoff（L113-119）、Depth（L127-133）各段数值和措辞与 CI 结果一致，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "uuid": "0dad9af8-5c11-4552-8f7e-39e1aa2b1420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHwwNFfa7eVFFavyrgZwK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1834,
      "cache_read_input_tokens": 44698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1834
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

变更总结：

1. **开头段落**（L8）：将"formal significance requires additional replications"替换为 bootstrap CI 方法描述。

2. **Table 1**（L20-37）：
   - 新增 `$95\%$ CI` 列，格式 `[.776, .817]`（省略前导零，紧凑）
   - Cutoff 行补充了 ±std（TSR ±0.004, CAR ±0.021）
   - Caption 加入 bootstrap 方法说明和 Cutoff † 脚注更新

3. **Gradient flow 段落**（L12）：
   - Full OCC vs Vanilla：明确 "$+$1.7pp is directionally positive but not statistically significant (bootstrap 95\% CI for the pairwise difference includes zero)"
   - Detach OCC：明确 "statistically significant degradation" + "bootstrap 95\% CIs for all pairwise differences... exclude zero"
   - 修复了 em-dash `---` 为括号格式

4. **Label content 段落**（L14）：补充 "whose bootstrap CI overlaps broadly"，修复 em-dash。

Mechanism analysis（L59-67）、Cutoff（L113-119）、Depth（L127-133）各段数值和措辞与 CI 结果一致，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 205482,
  "duration_api_ms": 206913,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "7def8281-065e-4e74-8115-408ba87305b5",
  "total_cost_usd": 0.60373875,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 34691,
    "cache_read_input_tokens": 285786,
    "output_tokens": 9695,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34691,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 362,
        "cache_read_input_tokens": 44698,
        "cache_creation_input_tokens": 1834,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1834
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1497,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0016020000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 9695,
      "cacheReadInputTokens": 285786,
      "cacheCreationInputTokens": 34691,
      "webSearchRequests": 0,
      "costUSD": 0.60213675,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b93d868c-10ea-4910-b841-444ebb65636e"
}
```

</details>

---
