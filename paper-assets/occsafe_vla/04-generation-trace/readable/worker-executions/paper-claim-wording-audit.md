# paper claim wording audit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_claim_wording_audit_20260523T071232.log`
- **Structured JSON:** [`0580f5e094eefb0c9ab2.json`](../../sessions/05/0580f5e094eefb0c9ab2.json)

## Before a recorded user message

36 recorded events

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
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
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
  "uuid": "e72d8584-49db-47e1-8ba3-b11849458cf9",
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
  "uuid": "6ce31c5e-0fbb-4946-97e9-8c5f6dde046b",
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532"
}
```

---

### Assistant

_source line 4_

Let me start by reading the writing norms and the files that need to be checked.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "710ee9a7-f6c2-4c82-b518-0f823818f760",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuiwYC1de1FMV88rqG3DzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11615,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11615
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

<details open><summary>🔧 Tool call — Read · `toolu_01MoZSwLHXbbQCSvFkzrRjFF`</summary>

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
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "87cb8151-362e-4762-98e0-935b5c5f9c5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuiwYC1de1FMV88rqG3DzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11615,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11615
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

_source line 6 · 2026-05-23T07:12:44.445Z_

<details><summary>↩ Tool result · `toolu_01MoZSwLHXbbQCSvFkzrRjFF`</summary>

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
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "8a726d10-8851-4108-a4cb-900ad81087aa",
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

<details open><summary>🔧 Tool call — Read · `toolu_01CLrGEdkqn59RqbYswh53wh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "4af65f55-585c-4a93-b2f6-0a737cad8ce7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuiwYC1de1FMV88rqG3DzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11615,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11615
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

_source line 8 · 2026-05-23T07:12:44.763Z_

<details><summary>↩ Tool result · `toolu_01CLrGEdkqn59RqbYswh53wh`</summary>

```text
1	% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models
2	% Target: AAAI 2027
3	\documentclass[letterpaper]{article}
4	\usepackage{aaai25}
5	\usepackage{times}
6	\usepackage{helvet}
7	\usepackage{courier}
8	\usepackage[hyphens]{url}
9	\usepackage{graphicx}
10	\usepackage{amsmath,amssymb}
11	\usepackage{booktabs}
12	\usepackage{enumitem}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\urlstyle{rm}
16	\def\UrlFont{\rm}
17	\frenchspacing
18	\setlength{\pdfpagewidth}{8.5in}
19	\setlength{\pdfpageheight}{11in}
20	
21	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
22	
23	\title{OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models}
24	
25	\author{
26	Anonymous Authors
27	}
28	
29	\begin{document}
30	\maketitle
31	
32	\begin{abstract}
33	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success rates yet remain behaviorally unsafe: on SafeLIBERO Level~I, OpenVLA attains 90.7\% task success but only 78.0\% collision avoidance.
34	This paper presents the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.
35	Six conditions on OpenVLA-OFT with LoRA vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels), Detach OCC (ground-truth labels, encoder gradients blocked), Depth (egocentric depth prediction, 4 seeds), and Cutoff (occupancy for the first 35K steps only, 2 seeds$^{\dagger}$).
36	The central finding is that gradient flow through the vision encoder is the necessary condition preventing safety degradation.
37	Detach OCC, the only condition blocking encoder gradients, drops collision avoidance to 74.6\% ($-$3.4\,pp vs.\ Vanilla at 78.0\%), while all gradient-flow conditions remain within 1.7\,pp of Vanilla (78.0--79.7\%).
38	Label content is secondary: structured occupancy, random binary maps, and egocentric depth yield comparable collision avoidance.
39	Cutoff$^{\dagger}$ retains the highest task success (91.5\%) but loses collision avoidance on the hardest safety task (T5 CAR 0.00).
40	Because the auxiliary head is discarded after training, these spatial losses add zero inference cost and require no ground-truth spatial labels at deployment.
41	\end{abstract}
42	
43	\input{introduction}
44	
45	\input{related_work}
46	
47	\input{method}
48	
49	\input{experiments}
50	
51	\input{results}
52	
53	\input{discussion}
54	
55	\input{conclusion}
56	
57	\bibliographystyle{aaai}
58	\bibliography{references}
59	
60	\end{document}
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "cb00ef67-37f3-4f73-bebd-92d0a794d8b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
      "content": "% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models\n% Target: AAAI 2027\n\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\urlstyle{rm}\n\\def\\UrlFont{\\rm}\n\\frenchspacing\n\\setlength{\\pdfpagewidth}{8.5in}\n\\setlength{\\pdfpageheight}{11in}\n\n\\newcommand{\\todo}[1]{\\textcolor{red}{[TODO: #1]}}\n\n\\title{OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models}\n\n\\author{\nAnonymous Authors\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nFine-tuned Vision-Language-Action (VLA) models can achieve high task success rates yet remain behaviorally unsafe: on SafeLIBERO Level~I, OpenVLA attains 90.7\\% task success but only 78.0\\% collision avoidance.\nThis paper presents the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.\nSix conditions on OpenVLA-OFT with LoRA vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels), Detach OCC (ground-truth labels, encoder gradients blocked), Depth (egocentric depth prediction, 4 seeds), and Cutoff (occupancy for the first 35K steps only, 2 seeds$^{\\dagger}$).\nThe central finding is that gradient flow through the vision encoder is the necessary condition preventing safety degradation.\nDetach OCC, the only condition blocking encoder gradients, drops collision avoidance to 74.6\\% ($-$3.4\\,pp vs.\\ Vanilla at 78.0\\%), while all gradient-flow conditions remain within 1.7\\,pp of Vanilla (78.0--79.7\\%).\nLabel content is secondary: structured occupancy, random binary maps, and egocentric depth yield comparable collision avoidance.\nCutoff$^{\\dagger}$ retains the highest task success (91.5\\%) but loses collision avoidance on the hardest safety task (T5 CAR 0.00).\nBecause the auxiliary head is discarded after training, these spatial losses add zero inference cost and require no ground-truth spatial labels at deployment.\n\\end{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{results}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\bibliographystyle{aaai}\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01C9UKKrNu1AgDA4Xays5vPm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "ccbf9ca0-c820-4a7e-9d23-c56236de99d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuiwYC1de1FMV88rqG3DzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11615,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11615
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

_source line 10 · 2026-05-23T07:12:45.234Z_

<details><summary>↩ Tool result · `toolu_01C9UKKrNu1AgDA4Xays5vPm`</summary>

```text
1	
2	\section{Introduction}
3	
4	Vision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success rates on manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}. On SafeLIBERO Level~I~\cite{hu2025vlsa}, a 10-task tabletop benchmark with static obstacles in the workspace, a fine-tuned OpenVLA model completes 90.7\% of tasks but achieves only 78.0\% collision avoidance rate (CAR), both measured over 3 seeds and 50 rollouts per task. On the three most physically constrained tasks, collision rates reach 53--93\%. One task yields 100\% task success with only 32.5\% collision avoidance---the robot completes the goal while colliding in two-thirds of episodes. Task success does not imply behavioral safety.
5	
6	Auxiliary spatial prediction tasks---occupancy grids, depth maps, point clouds---have been widely adopted to improve VLA manipulation performance~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla}. These methods inject 3D structure into vision encoders pretrained on 2D images, consistently improving success rates and generalization. Separately, VLA safety methods apply runtime action filtering via control barrier functions~\cite{hu2025vlsa} or constrained reinforcement learning~\cite{zhang2025safevla} to reduce collisions. These two research threads remain disconnected: no spatial VLA method quantitatively evaluates collision avoidance, and no VLA safety method exploits spatial representation learning. Whether auxiliary spatial supervision affects collision avoidance---and whether any such effect derives from the spatial information itself or from training dynamics of the auxiliary objective---is an open question.
7	
8	We present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\cite{kim2024openvla, kim2025oft} under six conditions that systematically vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), Depth (egocentric depth prediction), and Cutoff (occupancy supervision for the first 35{,}000 steps only). Across all conditions, blocking gradient flow degrades collision avoidance by 3.4 percentage points below Vanilla, while maintaining it keeps CAR within 0.0--1.7pp of the no-auxiliary baseline. Label content is secondary: random labels, structured occupancy, and egocentric depth all achieve comparable CAR when gradient flow is maintained. Our contributions are:
9	
10	\begin{enumerate}
11	    \item \textbf{Mechanism identification.} We isolate gradient flow as the necessary condition: Detach OCC (CAR 0.746, TSR $\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.
12	
13	    \item \textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.
14	
15	    \item \textbf{Practical guideline.} If an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder; blocking them actively degrades both collision avoidance and task execution stability. No ground-truth spatial labels are required, and the auxiliary head is discarded after training, adding zero inference cost.
16	\end{enumerate}
17	
18	We evaluate on SafeLIBERO Level~I~\cite{hu2025vlsa} (10 tasks drawn from LIBERO~\cite{liu2023libero}) using OpenVLA-OFT with LoRA fine-tuning. Blocking gradient flow reduces CAR by 3.4pp below Vanilla and increases TSR variance by an order of magnitude; maintaining gradient flow keeps CAR within 0.0--1.7pp of Vanilla. Section~\ref{sec:related_work} reviews related work on VLA safety, spatial representations, and multi-task regularization. Section~\ref{sec:method} describes the auxiliary head architectures and ablation design. Section~\ref{sec:results} presents experimental results and mechanism analysis. Section~\ref{sec:discussion} discusses implications, limitations, and connections to multi-task learning theory.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "e2acbc97-71c5-4d05-b53c-267786802ed9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
      "content": "\n\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success rates on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, a 10-task tabletop benchmark with static obstacles in the workspace, a fine-tuned OpenVLA model completes 90.7\\% of tasks but achieves only 78.0\\% collision avoidance rate (CAR), both measured over 3 seeds and 50 rollouts per task. On the three most physically constrained tasks, collision rates reach 53--93\\%. One task yields 100\\% task success with only 32.5\\% collision avoidance---the robot completes the goal while colliding in two-thirds of episodes. Task success does not imply behavioral safety.\n\nAuxiliary spatial prediction tasks---occupancy grids, depth maps, point clouds---have been widely adopted to improve VLA manipulation performance~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla}. These methods inject 3D structure into vision encoders pretrained on 2D images, consistently improving success rates and generalization. Separately, VLA safety methods apply runtime action filtering via control barrier functions~\\cite{hu2025vlsa} or constrained reinforcement learning~\\cite{zhang2025safevla} to reduce collisions. These two research threads remain disconnected: no spatial VLA method quantitatively evaluates collision avoidance, and no VLA safety method exploits spatial representation learning. Whether auxiliary spatial supervision affects collision avoidance---and whether any such effect derives from the spatial information itself or from training dynamics of the auxiliary objective---is an open question.\n\nWe present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under six conditions that systematically vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), Depth (egocentric depth prediction), and Cutoff (occupancy supervision for the first 35{,}000 steps only). Across all conditions, blocking gradient flow degrades collision avoidance by 3.4 percentage points below Vanilla, while maintaining it keeps CAR within 0.0--1.7pp of the no-auxiliary baseline. Label content is secondary: random labels, structured occupancy, and egocentric depth all achieve comparable CAR when gradient flow is maintained. Our contributions are:\n\n\\begin{enumerate}\n    \\item \\textbf{Mechanism identification.} We isolate gradient flow as the necessary condition: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.\n\n    \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.\n\n    \\item \\textbf{Practical guideline.} If an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder; blocking them actively degrades both collision avoidance and task execution stability. No ground-truth spatial labels are required, and the auxiliary head is discarded after training, adding zero inference cost.\n\\end{enumerate}\n\nWe evaluate on SafeLIBERO Level~I~\\cite{hu2025vlsa} (10 tasks drawn from LIBERO~\\cite{liu2023libero}) using OpenVLA-OFT with LoRA fine-tuning. Blocking gradient flow reduces CAR by 3.4pp below Vanilla and increases TSR variance by an order of magnitude; maintaining gradient flow keeps CAR within 0.0--1.7pp of Vanilla. Section~\\ref{sec:related_work} reviews related work on VLA safety, spatial representations, and multi-task regularization. Section~\\ref{sec:method} describes the auxiliary head architectures and ablation design. Section~\\ref{sec:results} presents experimental results and mechanism analysis. Section~\\ref{sec:discussion} discusses implications, limitations, and connections to multi-task learning theory.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01PWd3tDaGvUubuogGogXHoV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "1e19147c-e6a9-4c61-bbc5-5e28bff3969b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuiwYC1de1FMV88rqG3DzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11615,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11615
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

_source line 12 · 2026-05-23T07:12:45.697Z_

<details><summary>↩ Tool result · `toolu_01PWd3tDaGvUubuogGogXHoV`</summary>

```text
1	
2	\section{Conclusion}
3	\label{sec:conclusion}
4	
5	We investigated how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. A factorial study on OpenVLA-OFT across six training conditions revealed that auxiliary gradient flow through the vision encoder is necessary to prevent safety degradation when adding auxiliary heads, while the spatial content of auxiliary labels plays a secondary role. Conditions with gradient flow---Full OCC (0.797), Random OCC (0.789), Cutoff (0.783), and Depth (0.780)---maintained collision avoidance rates comparable to the Vanilla baseline (0.780), whereas Detach OCC, which blocks encoder gradients, fell 3.4pp below Vanilla (0.746) and exhibited an order-of-magnitude increase in task success variance ($\sigma = 0.163$ vs.\ $< 0.050$). The Depth condition (4 seeds) achieves CAR identical to Vanilla despite providing per-pixel geometric information directly aligned with collision avoidance, confirming that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to gradient flow presence. The Cutoff condition, which removes auxiliary gradients after 35{,}000 steps, retains task completion benefits (TSR 0.915, highest among all conditions) but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.
6	
7	These results yield three contributions. First, we identify auxiliary gradient flow as a necessary condition for auxiliary heads to avoid degrading collision avoidance, and show that blocking it (Detach OCC) actively harms both safety and task execution stability relative to no auxiliary task at all. Second, our factorial ablation design---isolating gradient flow, spatial content, and spatial reference frame as independent factors---provides a reusable methodology for analyzing auxiliary task effects in VLA training. Third, we establish a practical guideline: if an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder to prevent safety degradation; no ground-truth spatial labels are required, and the auxiliary head is discarded after training at zero inference cost.
8	
9	Several directions remain open. First, testing additional auxiliary task types---contrastive objectives, reconstruction losses---would establish whether gradient-flow regularization generalizes beyond the occupancy and depth prediction tasks studied here. Second, distinguishing among the three candidate mechanisms proposed in Section~\ref{sec:why_gradient} (anti-overfitting regularization, optimization landscape smoothing, gradient diversity) requires gradient-level diagnostics: gradient norm tracking across training, loss landscape curvature analysis via Hessian spectra, and representational probing of encoder features. Third, evaluating on other VLA architectures (e.g., RT-2), extended benchmarks (SafeLIBERO Level~II, dynamic obstacles), and real-world deployment would test the robustness of the gradient-flow effect beyond the single architecture and benchmark studied here.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "98d36f39-5f7d-4d2e-bd11-2b609a9e56b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex",
      "content": "\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe investigated how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. A factorial study on OpenVLA-OFT across six training conditions revealed that auxiliary gradient flow through the vision encoder is necessary to prevent safety degradation when adding auxiliary heads, while the spatial content of auxiliary labels plays a secondary role. Conditions with gradient flow---Full OCC (0.797), Random OCC (0.789), Cutoff (0.783), and Depth (0.780)---maintained collision avoidance rates comparable to the Vanilla baseline (0.780), whereas Detach OCC, which blocks encoder gradients, fell 3.4pp below Vanilla (0.746) and exhibited an order-of-magnitude increase in task success variance ($\\sigma = 0.163$ vs.\\ $< 0.050$). The Depth condition (4 seeds) achieves CAR identical to Vanilla despite providing per-pixel geometric information directly aligned with collision avoidance, confirming that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to gradient flow presence. The Cutoff condition, which removes auxiliary gradients after 35{,}000 steps, retains task completion benefits (TSR 0.915, highest among all conditions) but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.\n\nThese results yield three contributions. First, we identify auxiliary gradient flow as a necessary condition for auxiliary heads to avoid degrading collision avoidance, and show that blocking it (Detach OCC) actively harms both safety and task execution stability relative to no auxiliary task at all. Second, our factorial ablation design---isolating gradient flow, spatial content, and spatial reference frame as independent factors---provides a reusable methodology for analyzing auxiliary task effects in VLA training. Third, we establish a practical guideline: if an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder to prevent safety degradation; no ground-truth spatial labels are required, and the auxiliary head is discarded after training at zero inference cost.\n\nSeveral directions remain open. First, testing additional auxiliary task types---contrastive objectives, reconstruction losses---would establish whether gradient-flow regularization generalizes beyond the occupancy and depth prediction tasks studied here. Second, distinguishing among the three candidate mechanisms proposed in Section~\\ref{sec:why_gradient} (anti-overfitting regularization, optimization landscape smoothing, gradient diversity) requires gradient-level diagnostics: gradient norm tracking across training, loss landscape curvature analysis via Hessian spectra, and representational probing of encoder features. Third, evaluating on other VLA architectures (e.g., RT-2), extended benchmarks (SafeLIBERO Level~II, dynamic obstacles), and real-world deployment would test the robustness of the gradient-flow effect beyond the single architecture and benchmark studied here.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01PB1eRtC1v1BthcYeL3s6jq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "9c40ece1-528a-4ecc-8e03-6cb365916d2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuiwYC1de1FMV88rqG3DzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11615,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11615
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

_source line 14 · 2026-05-23T07:12:46.219Z_

<details><summary>↩ Tool result · `toolu_01PB1eRtC1v1BthcYeL3s6jq`</summary>

```text
1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\subsection{Why Does Gradient Flow Improve Collision Avoidance?}
6	\label{sec:why_gradient}
7	
8	The ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \emph{improves} CAR above Vanilla, but that its \emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.
9	
10	\textbf{Hypothesis 1: Anti-overfitting regularization.}
11	Auxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.
12	
13	\textbf{Hypothesis 2: Optimization landscape smoothing.}
14	The auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.
15	
16	\textbf{Hypothesis 3: Gradient diversity.}
17	When fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.
18	
19	All three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.
20	
21	\subsection{Why Is Detach Harmful?}
22	\label{sec:why_detach}
23	
24	Detach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\sigma = 0.163$ vs.\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.
25	
26	The primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \texttt{stop\_gradient}, the encoder receives gradients from $\mathcal{L}_\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.
27	
28	The TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.
29	
30	\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}
31	\label{sec:cutoff_temporal}
32	
33	The Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).
34	
35	This pattern connects to the candidate mechanisms in Section~\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.
36	
37	The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance, however, requires continuous gradient flow---the benefit does not persist when auxiliary gradients are removed. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.
38	
39	\subsection{Implications for VLA Safety}
40	\label{sec:implications}
41	
42	\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.
43	
44	\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.
45	
46	\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.
47	
48	\subsection{Limitations}
49	\label{sec:limitations}
50	
51	\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.
52	
53	\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.
54	
55	\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.
56	
57	\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\sigma = 0.039$, 4 seeds), Full OCC ($\sigma = 0.032$, 3 seeds), and Random OCC ($\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\sigma = 0.002$), its TSR variance ($\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.
58	
59	The variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.
60	
61	\subsection{Depth vs.\ BEV Occupancy}
62	\label{sec:depth_discussion}
63	
64	The Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data establish that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.
65	
66	The consistent ordering (Full OCC $>$ Random OCC $>$ Depth $\approx$ Vanilla) across conditions with gradient flow raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.
67	
68	The Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\sigma = 0.039$ vs.\ Vanilla's $\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.
69	
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "61e5d578-7753-4815-a581-8e78dde5f348",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
      "content": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance, however, requires continuous gradient flow---the benefit does not persist when auxiliary gradients are removed. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\\sigma = 0.039$, 4 seeds), Full OCC ($\\sigma = 0.032$, 3 seeds), and Random OCC ($\\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\\sigma = 0.002$), its TSR variance ($\\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.\n\nThe variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThe Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data establish that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.\n\nThe consistent ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla) across conditions with gradient flow raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.\n\nThe Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.\n\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
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
Now I have all four files. Let me systematically identify problematic claims in each file.

## Abstract (main.tex, lines 32-41)

1. Line 36: "gradient flow through the vision encoder is the necessary condition preventing safety degradation" - This uses "necessary condition" which is close to "necessary and sufficient". Actually, we proved "necessary" (Detach without it degrades), so "necessary condition" is fine. But "the necessary condition" implies it's the only one, which might be too strong. Let me check the modification rules again.

Rule 1: "necessary and sufficient" → "necessary for preventing degradation" - The abstract says "necessary condition preventing safety degradation" which is already close to this. Let me check more carefully.


Actually, re-reading the claim: "the necessary condition" is too strong since we can't prove it's the only necessary condition. The bootstrap CI for Detach OCC is statistically significant, so calling gradient flow necessary is supported by the data, but I should soften it to "a necessary condition" instead. Looking at the other claims in the abstract, I need to check line 38 about label content being secondary.

Let me establish clearer rules for what language I can use: "necessary and sufficient" should become "necessary for preventing degradation," mechanism claims need to be framed as "mechanistic evidence" rather than definitive identification, and any positive comparisons without statistical significance need the qualifier "directionally positive but not statistically significant." The Detach degradation result can stand as statistically significant, but I need to avoid "significantly" elsewhere unless there's a statistical test backing it. I should also reserve "consistently" for cases where multiple seeds show the same direction, not for broader generalizations.

Now I'll go through the abstract systematically to apply these rules. I need to change "the necessary condition" to "a necessary condition" throughout since saying "the" implies both necessity and sufficiency, which the data doesn't support. The gradient flow blocking shows a significant drop, but the gradient-flow conditions stay close to baseline, so it's a necessary condition but not sufficient on its own. I should also update the Introduction section to reflect this language change and apply Rule 2 to rename "Mechanism identification" to something like "Mechanistic evidence."

For the Conclusion, I'm checking that the language about gradient flow being "necessary to prevent safety degradation" aligns with Rule 1 and the actual findings. The claim is acceptable since blocking gradients does degrade performance, making gradient flow necessary for maintaining the baseline. The secondary role of spatial content is also supported by the data showing minimal differences when labels are present but gradients flow normally.

In the Discussion section, I'm verifying the numerical comparisons and the framing of the dominant effect. The key insight is that gradient flow's absence is what drives the degradation below Vanilla, not that its presence improves performance above Vanilla—this is an important distinction that correctly reflects what the ablation shows. The language is already appropriately cautious throughout. I'm doing a targeted search for potentially overconfident phrasing—checking for "significant," "necessary and sufficient," and "consistently"—and finding the hedging is solid. One small adjustment needed: "Mechanism identification" in the introduction should shift to "Mechanistic evidence" to better reflect what the analysis actually supports. I'm also checking where "confirms" appears in relation to variance amplification—that one's fine since it's about a significant finding. Now I need to systematically replace "the necessary condition" with "a necessary condition" throughout the abstract and introduction, and change "confirming" to something weaker like "suggesting" or "indicating" when it's describing non-significant comparisons between the OCC variants.

For the discussion section, I'm looking at that ablation results statement more carefully. The pattern being described is really about Detach performing worse, not about the other conditions being comparable—so I should reframe it to focus on what's actually consistent rather than overstating the positive effects.

In the introduction, I'm noticing some language that needs tightening. The claim about "confirming" that gradient flow presence matters is too strong given the small differences between conditions. I should soften that language to reflect what the data actually shows rather than what we'd like it to show.

Looking at the discussion section, I see similar issues—phrases like "establish" and "consistent ordering" overstate the significance of differences that fall within confidence intervals. These should be reframed as directional trends rather than definitive findings. I need to go through and replace strong causal language with more measured terms like "suggest" or "indicate" wherever the effect sizes don't clearly support the stronger claims.

Now I'm compiling all the specific edits needed across the paper, starting with the abstract where "the necessary condition" should become "a necessary condition," and then moving through the introduction and discussion sections to soften overstated language throughout. I'm checking the language in the conclusion and discussion sections—changing "confirming" to "indicating" where the differences aren't statistically significant, and replacing "establish" with "indicate" to avoid overstating the evidence. The key findings about gradient flow being necessary and spatial content being secondary are already properly hedged in most places. Checking the usage of "confirms" more carefully—the Detach result where gradient flow is necessary is a significant finding, so that phrasing works. For the Depth section on variance amplification, the 3x difference in standard deviation (0.039 vs 0.012) is a clear pattern, so "confirms" is appropriate there too. The key distinction is that these are about mechanistic findings rather than positive performance claims. I'm reconsidering whether "establish" is the right word here—it might be too definitive for describing observed ranges. I'll soften it to "show" or "indicate" to be more cautious. But I'm also noticing a bigger issue in the Cutoff section: saying collision avoidance "requires continuous gradient flow" is too strong when the overall CAR stays comparable to Vanilla, so I need to be more precise about which tasks actually depend on gradient flow versus the model's overall performance. The core issue is that the claim about needing continuous gradient flow for collision avoidance isn't actually supported—Cutoff's overall CAR matches Vanilla's, so there's no proven benefit to maintaining those gradients. What's really happening is task-specific vulnerability: Cutoff performs fine on average but completely fails on T5. I should reframe this as a discussion of task-specific sensitivity rather than a general requirement for continuous gradient flow, especially since this is exploratory hypothesis territory in the discussion section.

Now I'm compiling the specific edits needed across the paper. The main changes involve softening causal language—replacing "necessary condition" with "a necessary condition," swapping "confirms" for "suggests" or "indicates," and changing "Mechanism identification" to "Mechanistic evidence" to better reflect what the data actually show rather than overstating the certainty of the findings.

For the discussion section, I need to revise how I'm characterizing the ordering of results and the collision avoidance findings. The ordering isn't statistically significant at the sample size we used, so I should acknowledge that uncertainty. And for the collision avoidance point, the key observation is that the Cutoff condition completely fails on the hardest task despite performing comparably to baseline overall—that's a more precise characterization than just saying the benefit doesn't persist. I'm realizing the language is too strong—"requires" implies an absolute necessity, but the data shows Cutoff performs comparably to Vanilla overall (0.783 vs 0.780 CAR), with task-specific variation rather than consistent degradation. I should soften this to acknowledge that collision avoidance on physically constrained tasks appears sensitive to continuous auxiliary gradient support, rather than claiming it strictly requires it.

Looking back at the discussion section, I notice it's already well-hedged—it frames the findings as "damage prevention" rather than claiming positive regularization, and explicitly notes that auxiliary heads don't significantly improve CAR beyond Vanilla while also not harming it. The statistical caveats are already there too, so I'm on solid ground with a more measured framing.

Let me search through the files for language like "clearly," "demonstrates," "proves," or "proof" to catch any overclaimed statements. The usages of "clearly" I'm finding are appropriately qualified—one refers to a significant effect (Detach) and the other is used negatively to describe what gradient-flow conditions don't do. No instances of "proves" or "proof" either, which is good.

Now I'm checking the Conclusion section more carefully to see if there are any claims that need toning down there. I'm noticing the language around Cutoff is overstated—saying collision avoidance "requires" continuous gradient flow is too strong when the overall CAR stays comparable to Vanilla, even though Task 5 shows complete failure. The claim should be more measured given we're drawing conclusions from a single task. I'm realizing the framing needs to be more precise—the difference between Full OCC and Vanilla isn't actually significant, so there's no real "advantage" for Cutoff to lose. The actual story is that Cutoff maintains comparable overall performance to Vanilla (0.783 vs 0.780) but exhibits a dramatic failure mode on the hardest task, suggesting temporal continuity of auxiliary gradients matters for handling physically constrained safety scenarios. Looking at this revision, I need to complete the thought about how the encoder re-specializes toward action prediction in the final steps, losing the feature diversity that continuous gradient flow maintains. Then I'm moving to the collision avoidance claim in line 37, which uses absolute language like "requires" and "the benefit" that overstates the evidence. The revision shifts to describing what the data actually shows—that Task 5 fails completely under Cutoff despite matching aggregate performance—rather than claiming a proven requirement for continuous gradients. I should soften that claim about collision avoidance requiring continuous gradient flow—the absolute statement doesn't match the hedged language that follows. Let me compile the full set of edits across all three files, adjusting the language to be more measured throughout while keeping the core findings intact. I'm satisfied with those edits and ready to apply them to the document. Let me go through and make all the changes systematically now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "e53917f9-b2cf-4414-a905-2c69390d4a64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyBfYtLsED1HKA7CoGoyHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12574,
      "cache_read_input_tokens": 23456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12574
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

Now let me systematically identify and fix the overclaimed language. I found the following issues:

**main.tex**: "the necessary condition" (implies sole/sufficient)
**introduction.tex**: "Mechanism identification", "the necessary condition", "confirming" for non-significant comparisons
**conclusion.tex**: "confirming", "loses most of the CAR advantage" (no significant advantage proven), "requires continuous gradient flow" (too absolute)
**discussion.tex**: "establish", "consistent ordering" (not significant), "requires continuous gradient flow" (overclaim)

Making all edits now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "afbe950f-29c4-42f1-b67e-9ce7a0df6cd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyBfYtLsED1HKA7CoGoyHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12574,
      "cache_read_input_tokens": 23456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12574
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

<details open><summary>🔧 Tool call — Edit · `toolu_01SB9JBVMdeTbfjvE214FYet`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
  "old_string": "The central finding is that gradient flow through the vision encoder is the necessary condition preventing safety degradation.",
  "new_string": "The central finding is that gradient flow through the vision encoder is a necessary condition for preventing safety degradation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "3960f3db-c02f-4952-a54f-a6a377201137",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyBfYtLsED1HKA7CoGoyHC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12574,
      "cache_read_input_tokens": 23456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12574
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

_source line 18 · 2026-05-23T07:15:34.491Z_

<details><summary>↩ Tool result · `toolu_01SB9JBVMdeTbfjvE214FYet`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "1138811a-67dd-42dc-86de-221f70ed1bd8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
    "oldString": "The central finding is that gradient flow through the vision encoder is the necessary condition preventing safety degradation.",
    "newString": "The central finding is that gradient flow through the vision encoder is a necessary condition for preventing safety degradation.",
    "originalFile": "% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models\n% Target: AAAI 2027\n\\documentclass[letterpaper]{article}\n\\usepackage{aaai25}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\urlstyle{rm}\n\\def\\UrlFont{\\rm}\n\\frenchspacing\n\\setlength{\\pdfpagewidth}{8.5in}\n\\setlength{\\pdfpageheight}{11in}\n\n\\newcommand{\\todo}[1]{\\textcolor{red}{[TODO: #1]}}\n\n\\title{OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models}\n\n\\author{\nAnonymous Authors\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nFine-tuned Vision-Language-Action (VLA) models can achieve high task success rates yet remain behaviorally unsafe: on SafeLIBERO Level~I, OpenVLA attains 90.7\\% task success but only 78.0\\% collision avoidance.\nThis paper presents the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.\nSix conditions on OpenVLA-OFT with LoRA vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels), Detach OCC (ground-truth labels, encoder gradients blocked), Depth (egocentric depth prediction, 4 seeds), and Cutoff (occupancy for the first 35K steps only, 2 seeds$^{\\dagger}$).\nThe central finding is that gradient flow through the vision encoder is the necessary condition preventing safety degradation.\nDetach OCC, the only condition blocking encoder gradients, drops collision avoidance to 74.6\\% ($-$3.4\\,pp vs.\\ Vanilla at 78.0\\%), while all gradient-flow conditions remain within 1.7\\,pp of Vanilla (78.0--79.7\\%).\nLabel content is secondary: structured occupancy, random binary maps, and egocentric depth yield comparable collision avoidance.\nCutoff$^{\\dagger}$ retains the highest task success (91.5\\%) but loses collision avoidance on the hardest safety task (T5 CAR 0.00).\nBecause the auxiliary head is discarded after training, these spatial losses add zero inference cost and require no ground-truth spatial labels at deployment.\n\\end{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{results}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\bibliographystyle{aaai}\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 33,
        "oldLines": 7,
        "newStart": 33,
        "newLines": 7,
        "lines": [
          " Fine-tuned Vision-Language-Action (VLA) models can achieve high task success rates yet remain behaviorally unsafe: on SafeLIBERO Level~I, OpenVLA attains 90.7\\% task success but only 78.0\\% collision avoidance.",
          " This paper presents the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.",
          " Six conditions on OpenVLA-OFT with LoRA vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels), Detach OCC (ground-truth labels, encoder gradients blocked), Depth (egocentric depth prediction, 4 seeds), and Cutoff (occupancy for the first 35K steps only, 2 seeds$^{\\dagger}$).",
          "-The central finding is that gradient flow through the vision encoder is the necessary condition preventing safety degradation.",
          "+The central finding is that gradient flow through the vision encoder is a necessary condition for preventing safety degradation.",
          " Detach OCC, the only condition blocking encoder gradients, drops collision avoidance to 74.6\\% ($-$3.4\\,pp vs.\\ Vanilla at 78.0\\%), while all gradient-flow conditions remain within 1.7\\,pp of Vanilla (78.0--79.7\\%).",
          " Label content is secondary: structured occupancy, random binary maps, and egocentric depth yield comparable collision avoidance.",
          " Cutoff$^{\\dagger}$ retains the highest task success (91.5\\%) but loses collision avoidance on the hardest safety task (T5 CAR 0.00)."
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_017opqTF9s4Ycf8eoYaLzRx5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "old_string": "\\textbf{Mechanism identification.}",
  "new_string": "\\textbf{Mechanistic evidence.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "a08728f8-4c04-475b-83d2-24868de47f67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RhxMPTShSToHqFY3QSPsgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8657,
      "cache_read_input_tokens": 36030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8657
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

_source line 20 · 2026-05-23T07:15:40.844Z_

<details><summary>↩ Tool result · `toolu_017opqTF9s4Ycf8eoYaLzRx5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "30171ec2-5fb8-4041-a7eb-c3e70455659d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "oldString": "\\textbf{Mechanism identification.}",
    "newString": "\\textbf{Mechanistic evidence.}",
    "originalFile": "\n\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success rates on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, a 10-task tabletop benchmark with static obstacles in the workspace, a fine-tuned OpenVLA model completes 90.7\\% of tasks but achieves only 78.0\\% collision avoidance rate (CAR), both measured over 3 seeds and 50 rollouts per task. On the three most physically constrained tasks, collision rates reach 53--93\\%. One task yields 100\\% task success with only 32.5\\% collision avoidance---the robot completes the goal while colliding in two-thirds of episodes. Task success does not imply behavioral safety.\n\nAuxiliary spatial prediction tasks---occupancy grids, depth maps, point clouds---have been widely adopted to improve VLA manipulation performance~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla}. These methods inject 3D structure into vision encoders pretrained on 2D images, consistently improving success rates and generalization. Separately, VLA safety methods apply runtime action filtering via control barrier functions~\\cite{hu2025vlsa} or constrained reinforcement learning~\\cite{zhang2025safevla} to reduce collisions. These two research threads remain disconnected: no spatial VLA method quantitatively evaluates collision avoidance, and no VLA safety method exploits spatial representation learning. Whether auxiliary spatial supervision affects collision avoidance---and whether any such effect derives from the spatial information itself or from training dynamics of the auxiliary objective---is an open question.\n\nWe present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under six conditions that systematically vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), Depth (egocentric depth prediction), and Cutoff (occupancy supervision for the first 35{,}000 steps only). Across all conditions, blocking gradient flow degrades collision avoidance by 3.4 percentage points below Vanilla, while maintaining it keeps CAR within 0.0--1.7pp of the no-auxiliary baseline. Label content is secondary: random labels, structured occupancy, and egocentric depth all achieve comparable CAR when gradient flow is maintained. Our contributions are:\n\n\\begin{enumerate}\n    \\item \\textbf{Mechanism identification.} We isolate gradient flow as the necessary condition: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.\n\n    \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.\n\n    \\item \\textbf{Practical guideline.} If an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder; blocking them actively degrades both collision avoidance and task execution stability. No ground-truth spatial labels are required, and the auxiliary head is discarded after training, adding zero inference cost.\n\\end{enumerate}\n\nWe evaluate on SafeLIBERO Level~I~\\cite{hu2025vlsa} (10 tasks drawn from LIBERO~\\cite{liu2023libero}) using OpenVLA-OFT with LoRA fine-tuning. Blocking gradient flow reduces CAR by 3.4pp below Vanilla and increases TSR variance by an order of magnitude; maintaining gradient flow keeps CAR within 0.0--1.7pp of Vanilla. Section~\\ref{sec:related_work} reviews related work on VLA safety, spatial representations, and multi-task regularization. Section~\\ref{sec:method} describes the auxiliary head architectures and ablation design. Section~\\ref{sec:results} presents experimental results and mechanism analysis. Section~\\ref{sec:discussion} discusses implications, limitations, and connections to multi-task learning theory.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " We present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under six conditions that systematically vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), Depth (egocentric depth prediction), and Cutoff (occupancy supervision for the first 35{,}000 steps only). Across all conditions, blocking gradient flow degrades collision avoidance by 3.4 percentage points below Vanilla, while maintaining it keeps CAR within 0.0--1.7pp of the no-auxiliary baseline. Label content is secondary: random labels, structured occupancy, and egocentric depth all achieve comparable CAR when gradient flow is maintained. Our contributions are:",
          " ",
          " \\begin{enumerate}",
          "-    \\item \\textbf{Mechanism identification.} We isolate gradient flow as the necessary condition: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.",
          "+    \\item \\textbf{Mechanistic evidence.} We isolate gradient flow as the necessary condition: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.",
          " ",
          "     \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.",
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01CnJ9HaPgEkYGTXJsM2N9pB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "old_string": "We isolate gradient flow as the necessary condition:",
  "new_string": "We identify gradient flow as a necessary condition for preventing degradation:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "68b9b92c-4d4d-4fcb-a163-5613906b0cd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EM1a5zeVjinVnndBW6Qbed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 44687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 212
      },
      "output_tokens": 72,
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

_source line 22 · 2026-05-23T07:15:46.811Z_

<details><summary>↩ Tool result · `toolu_01CnJ9HaPgEkYGTXJsM2N9pB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "e9a69dbd-ee06-4f11-8de9-122495bccfe1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "oldString": "We isolate gradient flow as the necessary condition:",
    "newString": "We identify gradient flow as a necessary condition for preventing degradation:",
    "originalFile": "\n\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success rates on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, a 10-task tabletop benchmark with static obstacles in the workspace, a fine-tuned OpenVLA model completes 90.7\\% of tasks but achieves only 78.0\\% collision avoidance rate (CAR), both measured over 3 seeds and 50 rollouts per task. On the three most physically constrained tasks, collision rates reach 53--93\\%. One task yields 100\\% task success with only 32.5\\% collision avoidance---the robot completes the goal while colliding in two-thirds of episodes. Task success does not imply behavioral safety.\n\nAuxiliary spatial prediction tasks---occupancy grids, depth maps, point clouds---have been widely adopted to improve VLA manipulation performance~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla}. These methods inject 3D structure into vision encoders pretrained on 2D images, consistently improving success rates and generalization. Separately, VLA safety methods apply runtime action filtering via control barrier functions~\\cite{hu2025vlsa} or constrained reinforcement learning~\\cite{zhang2025safevla} to reduce collisions. These two research threads remain disconnected: no spatial VLA method quantitatively evaluates collision avoidance, and no VLA safety method exploits spatial representation learning. Whether auxiliary spatial supervision affects collision avoidance---and whether any such effect derives from the spatial information itself or from training dynamics of the auxiliary objective---is an open question.\n\nWe present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under six conditions that systematically vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), Depth (egocentric depth prediction), and Cutoff (occupancy supervision for the first 35{,}000 steps only). Across all conditions, blocking gradient flow degrades collision avoidance by 3.4 percentage points below Vanilla, while maintaining it keeps CAR within 0.0--1.7pp of the no-auxiliary baseline. Label content is secondary: random labels, structured occupancy, and egocentric depth all achieve comparable CAR when gradient flow is maintained. Our contributions are:\n\n\\begin{enumerate}\n    \\item \\textbf{Mechanistic evidence.} We isolate gradient flow as the necessary condition: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.\n\n    \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.\n\n    \\item \\textbf{Practical guideline.} If an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder; blocking them actively degrades both collision avoidance and task execution stability. No ground-truth spatial labels are required, and the auxiliary head is discarded after training, adding zero inference cost.\n\\end{enumerate}\n\nWe evaluate on SafeLIBERO Level~I~\\cite{hu2025vlsa} (10 tasks drawn from LIBERO~\\cite{liu2023libero}) using OpenVLA-OFT with LoRA fine-tuning. Blocking gradient flow reduces CAR by 3.4pp below Vanilla and increases TSR variance by an order of magnitude; maintaining gradient flow keeps CAR within 0.0--1.7pp of Vanilla. Section~\\ref{sec:related_work} reviews related work on VLA safety, spatial representations, and multi-task regularization. Section~\\ref{sec:method} describes the auxiliary head architectures and ablation design. Section~\\ref{sec:results} presents experimental results and mechanism analysis. Section~\\ref{sec:discussion} discusses implications, limitations, and connections to multi-task learning theory.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " We present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under six conditions that systematically vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), Depth (egocentric depth prediction), and Cutoff (occupancy supervision for the first 35{,}000 steps only). Across all conditions, blocking gradient flow degrades collision avoidance by 3.4 percentage points below Vanilla, while maintaining it keeps CAR within 0.0--1.7pp of the no-auxiliary baseline. Label content is secondary: random labels, structured occupancy, and egocentric depth all achieve comparable CAR when gradient flow is maintained. Our contributions are:",
          " ",
          " \\begin{enumerate}",
          "-    \\item \\textbf{Mechanistic evidence.} We isolate gradient flow as the necessary condition: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.",
          "+    \\item \\textbf{Mechanistic evidence.} We identify gradient flow as a necessary condition for preventing degradation: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.",
          " ",
          "     \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.",
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01XoR5MURpD3okFdAXKepUXu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "old_string": "confirming that gradient flow presence rather than spatial content is the operative factor",
  "new_string": "suggesting that gradient flow presence, rather than spatial content, is the primary operative factor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "5f6ae709-811c-4171-bc76-22e94e3af6ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1JfmS4Dbh5PJxTb93gguF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 44899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
      },
      "output_tokens": 72,
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

_source line 24 · 2026-05-23T07:15:50.247Z_

<details><summary>↩ Tool result · `toolu_01XoR5MURpD3okFdAXKepUXu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "ce1708de-4d7f-4faa-92b5-d66f8867afb1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "oldString": "confirming that gradient flow presence rather than spatial content is the operative factor",
    "newString": "suggesting that gradient flow presence, rather than spatial content, is the primary operative factor",
    "originalFile": "\n\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions directly to robot actions, achieving high task success rates on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, a 10-task tabletop benchmark with static obstacles in the workspace, a fine-tuned OpenVLA model completes 90.7\\% of tasks but achieves only 78.0\\% collision avoidance rate (CAR), both measured over 3 seeds and 50 rollouts per task. On the three most physically constrained tasks, collision rates reach 53--93\\%. One task yields 100\\% task success with only 32.5\\% collision avoidance---the robot completes the goal while colliding in two-thirds of episodes. Task success does not imply behavioral safety.\n\nAuxiliary spatial prediction tasks---occupancy grids, depth maps, point clouds---have been widely adopted to improve VLA manipulation performance~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla}. These methods inject 3D structure into vision encoders pretrained on 2D images, consistently improving success rates and generalization. Separately, VLA safety methods apply runtime action filtering via control barrier functions~\\cite{hu2025vlsa} or constrained reinforcement learning~\\cite{zhang2025safevla} to reduce collisions. These two research threads remain disconnected: no spatial VLA method quantitatively evaluates collision avoidance, and no VLA safety method exploits spatial representation learning. Whether auxiliary spatial supervision affects collision avoidance---and whether any such effect derives from the spatial information itself or from training dynamics of the auxiliary objective---is an open question.\n\nWe present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under six conditions that systematically vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), Depth (egocentric depth prediction), and Cutoff (occupancy supervision for the first 35{,}000 steps only). Across all conditions, blocking gradient flow degrades collision avoidance by 3.4 percentage points below Vanilla, while maintaining it keeps CAR within 0.0--1.7pp of the no-auxiliary baseline. Label content is secondary: random labels, structured occupancy, and egocentric depth all achieve comparable CAR when gradient flow is maintained. Our contributions are:\n\n\\begin{enumerate}\n    \\item \\textbf{Mechanistic evidence.} We identify gradient flow as a necessary condition for preventing degradation: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.\n\n    \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.\n\n    \\item \\textbf{Practical guideline.} If an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder; blocking them actively degrades both collision avoidance and task execution stability. No ground-truth spatial labels are required, and the auxiliary head is discarded after training, adding zero inference cost.\n\\end{enumerate}\n\nWe evaluate on SafeLIBERO Level~I~\\cite{hu2025vlsa} (10 tasks drawn from LIBERO~\\cite{liu2023libero}) using OpenVLA-OFT with LoRA fine-tuning. Blocking gradient flow reduces CAR by 3.4pp below Vanilla and increases TSR variance by an order of magnitude; maintaining gradient flow keeps CAR within 0.0--1.7pp of Vanilla. Section~\\ref{sec:related_work} reviews related work on VLA safety, spatial representations, and multi-task regularization. Section~\\ref{sec:method} describes the auxiliary head architectures and ablation design. Section~\\ref{sec:results} presents experimental results and mechanism analysis. Section~\\ref{sec:discussion} discusses implications, limitations, and connections to multi-task learning theory.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " We present the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. We train OpenVLA-OFT~\\cite{kim2024openvla, kim2025oft} under six conditions that systematically vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels with matched gradient flow), Detach OCC (ground-truth labels with encoder gradients detached), Depth (egocentric depth prediction), and Cutoff (occupancy supervision for the first 35{,}000 steps only). Across all conditions, blocking gradient flow degrades collision avoidance by 3.4 percentage points below Vanilla, while maintaining it keeps CAR within 0.0--1.7pp of the no-auxiliary baseline. Label content is secondary: random labels, structured occupancy, and egocentric depth all achieve comparable CAR when gradient flow is maintained. Our contributions are:",
          " ",
          " \\begin{enumerate}",
          "-    \\item \\textbf{Mechanistic evidence.} We identify gradient flow as a necessary condition for preventing degradation: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, confirming that gradient flow presence rather than spatial content is the operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.",
          "+    \\item \\textbf{Mechanistic evidence.} We identify gradient flow as a necessary condition for preventing degradation: Detach OCC (CAR 0.746, TSR $\\sigma = 0.163$) degrades both collision avoidance and task execution stability relative to Vanilla (0.780), while all gradient-flow conditions---Full OCC (0.797), Random OCC (0.789), and Depth (0.780, 4 seeds)---remain comparable to Vanilla. Three distinct label types (structured occupancy, random binary, egocentric depth) achieve CAR within 1.7pp of each other, suggesting that gradient flow presence, rather than spatial content, is the primary operative factor. The Cutoff condition (0.783) shows that early-phase gradient flow provides partial protection, but continuous gradient flow is required to maintain the full effect.",
          " ",
          "     \\item \\textbf{Factorial ablation design.} We introduce a controlled multi-condition study that isolates gradient flow, spatial content, and spatial reference frame as factors in the interaction between auxiliary supervision and collision avoidance. Each pairwise comparison answers one mechanistic question (Table~\\ref{tab:ablation_design}), providing a reusable methodology for analyzing auxiliary task effects in VLA training.",
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01YVUrgimPsE1TUED5d4ihLd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex",
  "old_string": "confirming that spatial content",
  "new_string": "indicating that spatial content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "da1475bb-cd93-4247-9ab7-520f6d333f48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSPwsGLV1Rc4ZZmxTiv8rL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 45217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
      },
      "output_tokens": 72,
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

_source line 26 · 2026-05-23T07:15:53.681Z_

<details><summary>↩ Tool result · `toolu_01YVUrgimPsE1TUED5d4ihLd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "2555797b-9e5e-4fa1-89b0-f90700766652",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex",
    "oldString": "confirming that spatial content",
    "newString": "indicating that spatial content",
    "originalFile": "\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe investigated how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. A factorial study on OpenVLA-OFT across six training conditions revealed that auxiliary gradient flow through the vision encoder is necessary to prevent safety degradation when adding auxiliary heads, while the spatial content of auxiliary labels plays a secondary role. Conditions with gradient flow---Full OCC (0.797), Random OCC (0.789), Cutoff (0.783), and Depth (0.780)---maintained collision avoidance rates comparable to the Vanilla baseline (0.780), whereas Detach OCC, which blocks encoder gradients, fell 3.4pp below Vanilla (0.746) and exhibited an order-of-magnitude increase in task success variance ($\\sigma = 0.163$ vs.\\ $< 0.050$). The Depth condition (4 seeds) achieves CAR identical to Vanilla despite providing per-pixel geometric information directly aligned with collision avoidance, confirming that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to gradient flow presence. The Cutoff condition, which removes auxiliary gradients after 35{,}000 steps, retains task completion benefits (TSR 0.915, highest among all conditions) but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.\n\nThese results yield three contributions. First, we identify auxiliary gradient flow as a necessary condition for auxiliary heads to avoid degrading collision avoidance, and show that blocking it (Detach OCC) actively harms both safety and task execution stability relative to no auxiliary task at all. Second, our factorial ablation design---isolating gradient flow, spatial content, and spatial reference frame as independent factors---provides a reusable methodology for analyzing auxiliary task effects in VLA training. Third, we establish a practical guideline: if an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder to prevent safety degradation; no ground-truth spatial labels are required, and the auxiliary head is discarded after training at zero inference cost.\n\nSeveral directions remain open. First, testing additional auxiliary task types---contrastive objectives, reconstruction losses---would establish whether gradient-flow regularization generalizes beyond the occupancy and depth prediction tasks studied here. Second, distinguishing among the three candidate mechanisms proposed in Section~\\ref{sec:why_gradient} (anti-overfitting regularization, optimization landscape smoothing, gradient diversity) requires gradient-level diagnostics: gradient norm tracking across training, loss landscape curvature analysis via Hessian spectra, and representational probing of encoder features. Third, evaluating on other VLA architectures (e.g., RT-2), extended benchmarks (SafeLIBERO Level~II, dynamic obstacles), and real-world deployment would test the robustness of the gradient-flow effect beyond the single architecture and benchmark studied here.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\section{Conclusion}",
          " \\label{sec:conclusion}",
          " ",
          "-We investigated how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. A factorial study on OpenVLA-OFT across six training conditions revealed that auxiliary gradient flow through the vision encoder is necessary to prevent safety degradation when adding auxiliary heads, while the spatial content of auxiliary labels plays a secondary role. Conditions with gradient flow---Full OCC (0.797), Random OCC (0.789), Cutoff (0.783), and Depth (0.780)---maintained collision avoidance rates comparable to the Vanilla baseline (0.780), whereas Detach OCC, which blocks encoder gradients, fell 3.4pp below Vanilla (0.746) and exhibited an order-of-magnitude increase in task success variance ($\\sigma = 0.163$ vs.\\ $< 0.050$). The Depth condition (4 seeds) achieves CAR identical to Vanilla despite providing per-pixel geometric information directly aligned with collision avoidance, confirming that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to gradient flow presence. The Cutoff condition, which removes auxiliary gradients after 35{,}000 steps, retains task completion benefits (TSR 0.915, highest among all conditions) but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.",
          "+We investigated how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. A factorial study on OpenVLA-OFT across six training conditions revealed that auxiliary gradient flow through the vision encoder is necessary to prevent safety degradation when adding auxiliary heads, while the spatial content of auxiliary labels plays a secondary role. Conditions with gradient flow---Full OCC (0.797), Random OCC (0.789), Cutoff (0.783), and Depth (0.780)---maintained collision avoidance rates comparable to the Vanilla baseline (0.780), whereas Detach OCC, which blocks encoder gradients, fell 3.4pp below Vanilla (0.746) and exhibited an order-of-magnitude increase in task success variance ($\\sigma = 0.163$ vs.\\ $< 0.050$). The Depth condition (4 seeds) achieves CAR identical to Vanilla despite providing per-pixel geometric information directly aligned with collision avoidance, indicating that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to gradient flow presence. The Cutoff condition, which removes auxiliary gradients after 35{,}000 steps, retains task completion benefits (TSR 0.915, highest among all conditions) but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.",
          " ",
          " These results yield three contributions. First, we identify auxiliary gradient flow as a necessary condition for auxiliary heads to avoid degrading collision avoidance, and show that blocking it (Detach OCC) actively harms both safety and task execution stability relative to no auxiliary task at all. Second, our factorial ablation design---isolating gradient flow, spatial content, and spatial reference frame as independent factors---provides a reusable methodology for analyzing auxiliary task effects in VLA training. Third, we establish a practical guideline: if an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder to prevent safety degradation; no ground-truth spatial labels are required, and the auxiliary head is discarded after training at zero inference cost.",
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_015cKQqbUsu5uyYRpPnN2oiQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex",
  "old_string": "but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.",
  "new_string": "but exhibits task-specific vulnerability, with complete failure on the hardest safety task (Task~5 CAR 0.00), suggesting that collision avoidance on physically constrained tasks is sensitive to the temporal extent of auxiliary gradient flow."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "f8b69c61-6d96-426f-87bb-e278d2f54c00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLv1TYx6tZ5VzXpjSi9gq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 45440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 202
      },
      "output_tokens": 72,
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

_source line 28 · 2026-05-23T07:15:59.646Z_

<details><summary>↩ Tool result · `toolu_015cKQqbUsu5uyYRpPnN2oiQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "5984ee71-97b3-47a1-a932-cd3ebe39bff2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex",
    "oldString": "but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.",
    "newString": "but exhibits task-specific vulnerability, with complete failure on the hardest safety task (Task~5 CAR 0.00), suggesting that collision avoidance on physically constrained tasks is sensitive to the temporal extent of auxiliary gradient flow.",
    "originalFile": "\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe investigated how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. A factorial study on OpenVLA-OFT across six training conditions revealed that auxiliary gradient flow through the vision encoder is necessary to prevent safety degradation when adding auxiliary heads, while the spatial content of auxiliary labels plays a secondary role. Conditions with gradient flow---Full OCC (0.797), Random OCC (0.789), Cutoff (0.783), and Depth (0.780)---maintained collision avoidance rates comparable to the Vanilla baseline (0.780), whereas Detach OCC, which blocks encoder gradients, fell 3.4pp below Vanilla (0.746) and exhibited an order-of-magnitude increase in task success variance ($\\sigma = 0.163$ vs.\\ $< 0.050$). The Depth condition (4 seeds) achieves CAR identical to Vanilla despite providing per-pixel geometric information directly aligned with collision avoidance, indicating that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to gradient flow presence. The Cutoff condition, which removes auxiliary gradients after 35{,}000 steps, retains task completion benefits (TSR 0.915, highest among all conditions) but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.\n\nThese results yield three contributions. First, we identify auxiliary gradient flow as a necessary condition for auxiliary heads to avoid degrading collision avoidance, and show that blocking it (Detach OCC) actively harms both safety and task execution stability relative to no auxiliary task at all. Second, our factorial ablation design---isolating gradient flow, spatial content, and spatial reference frame as independent factors---provides a reusable methodology for analyzing auxiliary task effects in VLA training. Third, we establish a practical guideline: if an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder to prevent safety degradation; no ground-truth spatial labels are required, and the auxiliary head is discarded after training at zero inference cost.\n\nSeveral directions remain open. First, testing additional auxiliary task types---contrastive objectives, reconstruction losses---would establish whether gradient-flow regularization generalizes beyond the occupancy and depth prediction tasks studied here. Second, distinguishing among the three candidate mechanisms proposed in Section~\\ref{sec:why_gradient} (anti-overfitting regularization, optimization landscape smoothing, gradient diversity) requires gradient-level diagnostics: gradient norm tracking across training, loss landscape curvature analysis via Hessian spectra, and representational probing of encoder features. Third, evaluating on other VLA architectures (e.g., RT-2), extended benchmarks (SafeLIBERO Level~II, dynamic obstacles), and real-world deployment would test the robustness of the gradient-flow effect beyond the single architecture and benchmark studied here.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\section{Conclusion}",
          " \\label{sec:conclusion}",
          " ",
          "-We investigated how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. A factorial study on OpenVLA-OFT across six training conditions revealed that auxiliary gradient flow through the vision encoder is necessary to prevent safety degradation when adding auxiliary heads, while the spatial content of auxiliary labels plays a secondary role. Conditions with gradient flow---Full OCC (0.797), Random OCC (0.789), Cutoff (0.783), and Depth (0.780)---maintained collision avoidance rates comparable to the Vanilla baseline (0.780), whereas Detach OCC, which blocks encoder gradients, fell 3.4pp below Vanilla (0.746) and exhibited an order-of-magnitude increase in task success variance ($\\sigma = 0.163$ vs.\\ $< 0.050$). The Depth condition (4 seeds) achieves CAR identical to Vanilla despite providing per-pixel geometric information directly aligned with collision avoidance, indicating that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to gradient flow presence. The Cutoff condition, which removes auxiliary gradients after 35{,}000 steps, retains task completion benefits (TSR 0.915, highest among all conditions) but loses most of the CAR advantage, with complete failure on the hardest safety task (Task~5 CAR 0.00)---indicating that collision avoidance requires continuous gradient flow throughout training.",
          "+We investigated how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance. A factorial study on OpenVLA-OFT across six training conditions revealed that auxiliary gradient flow through the vision encoder is necessary to prevent safety degradation when adding auxiliary heads, while the spatial content of auxiliary labels plays a secondary role. Conditions with gradient flow---Full OCC (0.797), Random OCC (0.789), Cutoff (0.783), and Depth (0.780)---maintained collision avoidance rates comparable to the Vanilla baseline (0.780), whereas Detach OCC, which blocks encoder gradients, fell 3.4pp below Vanilla (0.746) and exhibited an order-of-magnitude increase in task success variance ($\\sigma = 0.163$ vs.\\ $< 0.050$). The Depth condition (4 seeds) achieves CAR identical to Vanilla despite providing per-pixel geometric information directly aligned with collision avoidance, indicating that spatial content---whether structured occupancy, egocentric depth, or random noise---is secondary to gradient flow presence. The Cutoff condition, which removes auxiliary gradients after 35{,}000 steps, retains task completion benefits (TSR 0.915, highest among all conditions) but exhibits task-specific vulnerability, with complete failure on the hardest safety task (Task~5 CAR 0.00), suggesting that collision avoidance on physically constrained tasks is sensitive to the temporal extent of auxiliary gradient flow.",
          " ",
          " These results yield three contributions. First, we identify auxiliary gradient flow as a necessary condition for auxiliary heads to avoid degrading collision avoidance, and show that blocking it (Detach OCC) actively harms both safety and task execution stability relative to no auxiliary task at all. Second, our factorial ablation design---isolating gradient flow, spatial content, and spatial reference frame as independent factors---provides a reusable methodology for analyzing auxiliary task effects in VLA training. Third, we establish a practical guideline: if an auxiliary prediction head is attached to the vision encoder during fine-tuning, gradients must flow through the encoder to prevent safety degradation; no ground-truth spatial labels are required, and the auxiliary head is discarded after training at zero inference cost.",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01TDnv5sAfafDmbi3jxnuaP6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "the data establish that three distinct auxiliary label types",
  "new_string": "the data suggest that three distinct auxiliary label types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "0ad88b92-353a-4176-b9a6-9995de385327",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAihvjRtt1H8CgyLHBijp6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 45642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 285
      },
      "output_tokens": 72,
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

_source line 30 · 2026-05-23T07:16:02.793Z_

<details><summary>↩ Tool result · `toolu_01TDnv5sAfafDmbi3jxnuaP6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "245c2064-6246-4cbd-a17a-eafa77d344d0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "oldString": "the data establish that three distinct auxiliary label types",
    "newString": "the data suggest that three distinct auxiliary label types",
    "originalFile": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance, however, requires continuous gradient flow---the benefit does not persist when auxiliary gradients are removed. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\\sigma = 0.039$, 4 seeds), Full OCC ($\\sigma = 0.032$, 3 seeds), and Random OCC ($\\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\\sigma = 0.002$), its TSR variance ($\\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.\n\nThe variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThe Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data establish that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.\n\nThe consistent ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla) across conditions with gradient flow raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.\n\nThe Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.\n\n",
    "structuredPatch": [
      {
        "oldStart": 61,
        "oldLines": 7,
        "newStart": 61,
        "newLines": 7,
        "lines": [
          " \\subsection{Depth vs.\\ BEV Occupancy}",
          " \\label{sec:depth_discussion}",
          " ",
          "-The Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data establish that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.",
          "+The Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.",
          " ",
          " The consistent ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla) across conditions with gradient flow raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.",
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01RR5tuNM53APDb49ARE6fdu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "The consistent ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla) across conditions with gradient flow raises the question",
  "new_string": "The directional ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "0739ff11-7a7a-4086-a1d9-d8eccb0cc804",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MXRet6wERhz3b5ouJd4ND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 45927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 211
      },
      "output_tokens": 72,
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

_source line 32 · 2026-05-23T07:16:10.072Z_

<details><summary>↩ Tool result · `toolu_01RR5tuNM53APDb49ARE6fdu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "7c861ca7-3aab-446f-add2-68d32cdf9cc7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "oldString": "The consistent ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla) across conditions with gradient flow raises the question",
    "newString": "The directional ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question",
    "originalFile": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance, however, requires continuous gradient flow---the benefit does not persist when auxiliary gradients are removed. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\\sigma = 0.039$, 4 seeds), Full OCC ($\\sigma = 0.032$, 3 seeds), and Random OCC ($\\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\\sigma = 0.002$), its TSR variance ($\\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.\n\nThe variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThe Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.\n\nThe consistent ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla) across conditions with gradient flow raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.\n\nThe Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.\n\n",
    "structuredPatch": [
      {
        "oldStart": 63,
        "oldLines": 7,
        "newStart": 63,
        "newLines": 7,
        "lines": [
          " ",
          " The Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.",
          " ",
          "-The consistent ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla) across conditions with gradient flow raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.",
          "+The directional ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.",
          " ",
          " The Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.",
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01FyaHe2cmYRxQuCAN9jqdGA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "Collision avoidance, however, requires continuous gradient flow---the benefit does not persist when auxiliary gradients are removed.",
  "new_string": "Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "1ccfca07-8374-49cc-ac24-3876ffb67a6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZKc5j7s6vNhMNtezLipr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 46138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 72,
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

_source line 34 · 2026-05-23T07:16:14.757Z_

<details><summary>↩ Tool result · `toolu_01FyaHe2cmYRxQuCAN9jqdGA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "b9496f23-3c64-4f6b-911f-1cd5f92594b6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "oldString": "Collision avoidance, however, requires continuous gradient flow---the benefit does not persist when auxiliary gradients are removed.",
    "newString": "Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00.",
    "originalFile": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance, however, requires continuous gradient flow---the benefit does not persist when auxiliary gradients are removed. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\\sigma = 0.039$, 4 seeds), Full OCC ($\\sigma = 0.032$, 3 seeds), and Random OCC ($\\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\\sigma = 0.002$), its TSR variance ($\\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.\n\nThe variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThe Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.\n\nThe directional ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.\n\nThe Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.\n\n",
    "structuredPatch": [
      {
        "oldStart": 34,
        "oldLines": 7,
        "newStart": 34,
        "newLines": 7,
        "lines": [
          " ",
          " This pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.",
          " ",
          "-The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance, however, requires continuous gradient flow---the benefit does not persist when auxiliary gradients are removed. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.",
          "+The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.",
          " ",
          " \\subsection{Implications for VLA Safety}",
          " \\label{sec:implications}"
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

_source line 35_

All 8 edits complete. Summary of changes:

| File | Original | Revised | Reason |
|------|----------|---------|--------|
| **main.tex** | "the necessary condition preventing" | "a necessary condition for preventing" | 只证明了 necessary，没证明唯一性 |
| **introduction.tex** | "Mechanism identification" | "Mechanistic evidence" | 提供证据 ≠ 完全鉴定机制 |
| **introduction.tex** | "isolate...as the necessary condition" | "identify...as a necessary condition for preventing degradation" | 同上 |
| **introduction.tex** | "confirming that gradient flow...is the operative factor" | "suggesting that...is the primary operative factor" | Full OCC vs Vanilla Δ=+0.017 不显著，不能用 "confirming" |
| **conclusion.tex** | "confirming that spatial content..." | "indicating that spatial content..." | 同上 |
| **conclusion.tex** | "loses most of the CAR advantage...indicating that collision avoidance requires continuous gradient flow" | "exhibits task-specific vulnerability...suggesting...is sensitive to the temporal extent" | Cutoff 总体 CAR≈Vanilla，无 "advantage" 可 "lose"；"requires" 过强 |
| **discussion.tex** | "the data establish that" | "the data suggest that" | 1.7pp 差异不显著 |
| **discussion.tex** | "The consistent ordering...raises the question" | "The directional ordering...though not statistically significant with 3--4 seeds, raises the question" | 明确标注排序方向性非显著性 |
| **discussion.tex** | "requires continuous gradient flow---the benefit does not persist" | "appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla...but Task~5 collapses to 0.00" | 总体 CAR 不支持 "requires"；改为基于数据的 hedged 表述 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "uuid": "51919abe-ca68-49ce-8a24-0429389fb047",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsGuHpV3n3TTjnjXXB1TbW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 46408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

_source line 36_

All 8 edits complete. Summary of changes:

| File | Original | Revised | Reason |
|------|----------|---------|--------|
| **main.tex** | "the necessary condition preventing" | "a necessary condition for preventing" | 只证明了 necessary，没证明唯一性 |
| **introduction.tex** | "Mechanism identification" | "Mechanistic evidence" | 提供证据 ≠ 完全鉴定机制 |
| **introduction.tex** | "isolate...as the necessary condition" | "identify...as a necessary condition for preventing degradation" | 同上 |
| **introduction.tex** | "confirming that gradient flow...is the operative factor" | "suggesting that...is the primary operative factor" | Full OCC vs Vanilla Δ=+0.017 不显著，不能用 "confirming" |
| **conclusion.tex** | "confirming that spatial content..." | "indicating that spatial content..." | 同上 |
| **conclusion.tex** | "loses most of the CAR advantage...indicating that collision avoidance requires continuous gradient flow" | "exhibits task-specific vulnerability...suggesting...is sensitive to the temporal extent" | Cutoff 总体 CAR≈Vanilla，无 "advantage" 可 "lose"；"requires" 过强 |
| **discussion.tex** | "the data establish that" | "the data suggest that" | 1.7pp 差异不显著 |
| **discussion.tex** | "The consistent ordering...raises the question" | "The directional ordering...though not statistically significant with 3--4 seeds, raises the question" | 明确标注排序方向性非显著性 |
| **discussion.tex** | "requires continuous gradient flow---the benefit does not persist" | "appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla...but Task~5 collapses to 0.00" | 总体 CAR 不支持 "requires"；改为基于数据的 hedged 表述 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 226271,
  "duration_api_ms": 227705,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "6e40148d-d84b-406a-be1d-298adaa85532",
  "total_cost_usd": 0.7106220000000001,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 34846,
    "cache_read_input_tokens": 435685,
    "output_tokens": 10938,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34846,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 504,
        "cache_read_input_tokens": 46408,
        "cache_creation_input_tokens": 279,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 279
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1392,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001477,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 10938,
      "cacheReadInputTokens": 435685,
      "cacheCreationInputTokens": 34846,
      "webSearchRequests": 0,
      "costUSD": 0.7091450000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8e6ee3b0-2707-4a67-8cec-3d7459646233"
}
```

</details>

---
