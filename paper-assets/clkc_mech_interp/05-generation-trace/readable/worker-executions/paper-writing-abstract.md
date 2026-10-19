# paper writing abstract

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_writing_abstract_20260522T160256.log`
- **Structured JSON:** [`fa3772bbfc14ca2b283c.json`](../../sessions/fa/fa3772bbfc14ca2b283c.json)

## Before a recorded user message

16 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
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
  "uuid": "f1a7da6a-7a14-42c8-94a8-33a6f9a18365",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod42-projects-clkc-mech-interp/memory/"
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
    "resetsAt": 1779475200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "060cef11-8ca3-449f-b275-1b9719922ee9",
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54"
}
```

---

### Assistant

_source line 4_

I'll read the required files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "2c40f784-1e3e-452f-a3ac-d17f597ddd31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsWECyEWptGyzGUjMiRxNJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12823,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12823
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

<details open><summary>🔧 Tool call — Read · `toolu_0123LaRtheiYTRHqiwv4FP9B`</summary>

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
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "dbdce14a-a485-4ea5-b4ae-67e12ce630b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsWECyEWptGyzGUjMiRxNJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12823,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12823
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

_source line 6 · 2026-05-22T16:03:05.927Z_

<details><summary>↩ Tool result · `toolu_0123LaRtheiYTRHqiwv4FP9B`</summary>

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
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "2f8926cb-bf11-495f-9210-b78b2781fad0",
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

<details open><summary>🔧 Tool call — Read · `toolu_01YK86J1aCwByfnU8iQextY8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "7f147985-60fd-462f-90ac-028622577f92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsWECyEWptGyzGUjMiRxNJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12823,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12823
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

_source line 8 · 2026-05-22T16:03:06.243Z_

<details><summary>↩ Tool result · `toolu_01YK86J1aCwByfnU8iQextY8`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{boer2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe accuracy does not guarantee that the detected direction can steer model behavior.
19	
20	We address these questions through a pipeline (Figure~\ref{fig:pipeline}) that combines residual stream probing with representation steering across two models of distinct architectures: Llama-3.1-8B-Instruct and Qwen3-8B.
21	Probes achieve 77.1\% and 75.3\% balanced accuracy on English within-language conflict detection, respectively, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).
22	Cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English approximately 7 percentage points (pp) more accurately than the reverse in both models.
23	This asymmetry, however, is not conflict-specific.
24	XNLI entailment-versus-contradiction probes \citep{conneau2018xnli} show the same directional pattern at comparable magnitude (+6.0 and +6.7 pp), with substantially overlapping confidence intervals.
25	The conflict asymmetry thus inherits from a general property of English-dominant models, where Chinese representations project more readily onto English representational space than the reverse.
26	Our causal analysis reveals a dissociation between detection and decision: the probe signal peaks at late layers (L28, 88\% depth), but representation steering succeeds only at a mid-layer (L13, 41\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant behavioral change.
27	To ensure these findings are robust, we apply a confound exclusion pipeline that includes COMET-based translation quality stratification, token overlap analysis, and non-conflict baseline comparison.
28	
29	These results carry two methodological implications.
30	The layer dissociation between probing peak and causal influence demonstrates that the layer with highest probe accuracy is not necessarily where the model resolves the conflict.
31	This challenges the common practice of intervening at the probing peak layer, consistent with the warning from \citet{basu2026interpretability} that detectability and causal relevance can diverge.
32	The directional asymmetry in cross-lingual transfer reflects a structural property of English-dominant multilingual models, not a conflict-specific phenomenon.
33	Any cross-lingual probing study must account for this baseline asymmetry to correctly interpret transfer differences.
34	
35	Our contributions are as follows:
36	\begin{itemize}
37	    \item \textbf{Cross-lingual conflict detectability and asymmetry characterization.} We provide the first evidence that knowledge conflict signals are linearly detectable across languages in residual stream representations. The transfer asymmetry (ZH$\to$EN $>$ EN$\to$ZH by ${\sim}$7 pp) matches the XNLI non-conflict baseline in both magnitude and direction, establishing that it reflects the model's general cross-lingual structure rather than conflict-specific encoding.
38	    \item \textbf{Detection-decision layer dissociation.} Representation steering at the mid-layer (L13, 41\% depth) causally shifts conflict resolution (Fisher $p = 0.002$), while steering at the late-layer probing peak (L28, 88\% depth) produces no significant effect. This dissociation shows that linear detectability does not imply causal relevance, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.
39	    \item \textbf{Confound exclusion pipeline for cross-lingual probing.} We design and validate a systematic pipeline of COMET translation quality ablation, token overlap analysis, and non-conflict task baseline comparison that excludes common confounds in cross-lingual probing studies.
40	\end{itemize}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "bc3f1326-62d5-43a6-acd4-0040a4cd078b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.\n\\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.\nYet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?\nCan it be detected from internal representations?\nAnd if detectable, does the detected signal causally influence the model's resolution strategy?\nThese questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.\n\nExisting work on probing knowledge conflict signals has been limited to monolingual settings.\n\\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \\citet{boer2026probing} performed knowledge attribution probing to localize factual associations within model parameters.\nExtending these approaches cross-lingually introduces additional challenges.\nTranslation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.\nToken overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.\nObserved asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.\nBeyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \\citep{hewitt2019designing}.\n\\citet{basu2026interpretability} demonstrated that even near-perfect probe accuracy does not guarantee that the detected direction can steer model behavior.\n\nWe address these questions through a pipeline (Figure~\\ref{fig:pipeline}) that combines residual stream probing with representation steering across two models of distinct architectures: Llama-3.1-8B-Instruct and Qwen3-8B.\nProbes achieve 77.1\\% and 75.3\\% balanced accuracy on English within-language conflict detection, respectively, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).\nCross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English approximately 7 percentage points (pp) more accurately than the reverse in both models.\nThis asymmetry, however, is not conflict-specific.\nXNLI entailment-versus-contradiction probes \\citep{conneau2018xnli} show the same directional pattern at comparable magnitude (+6.0 and +6.7 pp), with substantially overlapping confidence intervals.\nThe conflict asymmetry thus inherits from a general property of English-dominant models, where Chinese representations project more readily onto English representational space than the reverse.\nOur causal analysis reveals a dissociation between detection and decision: the probe signal peaks at late layers (L28, 88\\% depth), but representation steering succeeds only at a mid-layer (L13, 41\\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant behavioral change.\nTo ensure these findings are robust, we apply a confound exclusion pipeline that includes COMET-based translation quality stratification, token overlap analysis, and non-conflict baseline comparison.\n\nThese results carry two methodological implications.\nThe layer dissociation between probing peak and causal influence demonstrates that the layer with highest probe accuracy is not necessarily where the model resolves the conflict.\nThis challenges the common practice of intervening at the probing peak layer, consistent with the warning from \\citet{basu2026interpretability} that detectability and causal relevance can diverge.\nThe directional asymmetry in cross-lingual transfer reflects a structural property of English-dominant multilingual models, not a conflict-specific phenomenon.\nAny cross-lingual probing study must account for this baseline asymmetry to correctly interpret transfer differences.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{Cross-lingual conflict detectability and asymmetry characterization.} We provide the first evidence that knowledge conflict signals are linearly detectable across languages in residual stream representations. The transfer asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7 pp) matches the XNLI non-conflict baseline in both magnitude and direction, establishing that it reflects the model's general cross-lingual structure rather than conflict-specific encoding.\n    \\item \\textbf{Detection-decision layer dissociation.} Representation steering at the mid-layer (L13, 41\\% depth) causally shifts conflict resolution (Fisher $p = 0.002$), while steering at the late-layer probing peak (L28, 88\\% depth) produces no significant effect. This dissociation shows that linear detectability does not imply causal relevance, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.\n    \\item \\textbf{Confound exclusion pipeline for cross-lingual probing.} We design and validate a systematic pipeline of COMET translation quality ablation, token overlap analysis, and non-conflict task baseline comparison that excludes common confounds in cross-lingual probing studies.\n\\end{itemize}\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_011mjZ8WJW9MrWW6e1ZnjM6M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "baa98857-4ad6-4e9a-9286-80cbbe1f3988",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsWECyEWptGyzGUjMiRxNJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12823,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12823
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

_source line 10 · 2026-05-22T16:03:06.599Z_

<details><summary>↩ Tool result · `toolu_011mjZ8WJW9MrWW6e1ZnjM6M`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2024qwen25}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.
29	Both models encode linearly detectable conflict signals in their residual streams.
30	Llama achieves 77.1\% on EN$\to$EN (peak at layer 28, 88\% depth) and 71.2\% on ZH$\to$ZH.
31	Qwen reaches 75.3\% on EN$\to$EN (peak at layer 22, 61\% depth) and 71.6\% on ZH$\to$ZH.
32	All within-language accuracies are significantly above chance (binomial $p < 0.001$).
33	Figure~\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for both models.
34	These results confirm that knowledge conflict signals are linearly separable in the residual stream across both architectures and both languages.
35	
36	\subsection{Cross-Lingual Transfer and Asymmetry}
37	\label{sec:cross_lingual}
38	
39	All four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.
40	Both models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\to$EN) more accurately than the reverse direction (EN$\to$ZH).
41	For Llama, $\Delta_{\text{asym}} = +7.2$ percentage points (pp) with a 95\% bootstrap CI of [1.1, 13.6]; for Qwen, $\Delta_{\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7].
42	The magnitude of this asymmetry closely matches the XNLI non-conflict baseline (\S\ref{sec:xnli_baseline}), and the consistent direction across architectures suggests a shared structural property rather than a model-specific artifact (Figure~\ref{fig:asymmetry_forest}).
43	
44	%% Table 1: Main cross-lingual probe results
45	\begin{table}[t]
46	\centering
47	\caption{Cross-lingual probe balanced accuracy (\%) with bootstrap 95\% CIs ($n \geq 100$). $\Delta_{\text{asym}}$ = acc(ZH$\to$EN) $-$ acc(EN$\to$ZH), computed as the mean of paired bootstrap differences. Bold: best per-task direction.}
48	\label{tab:main_results}
49	\begin{tabular}{lcc}
50	\toprule
51	Direction & Llama-3.1-8B & Qwen3-8B \\
52	\midrule
53	\multicolumn{3}{l}{\textit{Conflict Task}} \\
54	EN $\to$ EN & \textbf{77.1} & \textbf{75.3} \\
55	ZH $\to$ ZH & 71.2 & 71.6 \\
56	EN $\to$ ZH & 64.1 & 65.0 \\
57	ZH $\to$ EN & 71.3 & 72.2 \\
58	$\Delta_{\text{asym}}$ & +7.2 [1.1, 13.6] & +7.2 [$-$0.6, 13.7] \\
59	\midrule
60	\multicolumn{3}{l}{\textit{XNLI Baseline}} \\
61	EN $\to$ EN & 94.0 & 96.6 \\
62	ZH $\to$ ZH & 87.5 & 89.5 \\
63	EN $\to$ ZH & 89.0 & 90.5 \\
64	ZH $\to$ EN & \textbf{94.9} & \textbf{97.2} \\
65	$\Delta_{\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] \\
66	\bottomrule
67	\end{tabular}
68	\end{table}
69	
70	\subsection{Non-Conflict Baseline Comparison}
71	\label{sec:xnli_baseline}
72	
73	If the ZH$\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.
74	We test this prediction using XNLI entailment-versus-contradiction probes.
75	Both models achieve high within-language accuracy on XNLI (Llama 94.0\% EN, 87.5\% ZH; Qwen 96.6\% EN, 89.5\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.
76	The XNLI probes exhibit the same directional asymmetry: Llama $\Delta_{\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\Delta_{\text{asym}} = +6.7$ pp, CI [2.4, 11.7].
77	Both XNLI CIs exclude zero, and both overlap substantially with the corresponding conflict-task CIs (Figure~\ref{fig:asymmetry_forest}).
78	The close match in asymmetry magnitude between conflict probes (Llama +7.2, Qwen +7.2 pp) and XNLI probes (Llama +6.0, Qwen +6.7 pp) indicates that the ZH$\to$EN transfer advantage is not specific to knowledge conflict representations.
79	Instead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.
80	
81	\subsection{Confound Exclusion}
82	\label{sec:confounds}
83	
84	Two potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.
85	
86	\paragraph{Translation quality.}
87	We stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\to$ZH probe accuracy across strata.
88	If translation quality drove probe transfer, high-COMET samples would yield higher accuracy.
89	Table~\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\Delta = +1.7$ pp, Fisher $p = 0.761$).
90	Translation quality does not confound the cross-lingual transfer results.
91	
92	\paragraph{Token overlap.}
93	Per-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\%, consistent with the minimal lexical overlap between the two languages.
94	Neither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \emph{lower} accuracy.
95	Shared tokens do not drive cross-lingual transfer.
96	
97	%% Table 2: Confound exclusion
98	\begin{table}[t]
99	\centering
100	\caption{Confound exclusion analysis. COMET tercile: $\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\to$ZH probe accuracy.}
101	\label{tab:confound}
102	\begin{tabular}{llrl}
103	\toprule
104	Confound & Model & Result & $p$ \\
105	\midrule
106	COMET tercile & Qwen & $\Delta = -5.6$ pp & 0.695 \\
107	COMET tercile & Llama & $\Delta = +1.7$ pp & 0.761 \\
108	\midrule
109	Token overlap & Qwen & n.s. & $>$0.4 \\
110	Token overlap & Llama & $r = -0.15$ & 0.012 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	\subsection{Causal Evidence via Representation Steering}
116	\label{sec:steering}
117	
118	The probing results establish that conflict signals are detectable, but detection does not imply causal relevance.
119	We test whether the probe weight direction $\mathbf{w}_{\text{probe}}$ causally influences conflict resolution by injecting $\alpha \cdot \mathbf{w}_{\text{probe}}$ into the last-token residual stream at a target layer during inference.
120	We measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.
121	
122	\paragraph{L13 (mid-layer, 41\% depth).}
123	Steering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\ref{tab:steering}).
124	Positive steering ($\alpha = +5$) yields a flip rate of 19.9\% versus 6.6\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.
125	Negative steering ($\alpha = -20$) yields 36.0\% versus 17.6\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.
126	Both results survive Bonferroni correction for multiple comparisons.
127	The bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.
128	
129	\paragraph{Negative layers.}
130	Steering at L28 (the probing peak layer, 88\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\ref{tab:steering}).
131	L18 (the MLP probe peak, 56\% depth) also shows no causal influence (all Fisher $p > 0.44$).
132	
133	\paragraph{$\alpha = +20$ reversal.}
134	At extreme perturbation magnitude ($\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).
135	This indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.
136	
137	\paragraph{Detection $\neq$ Decision.}
138	In Llama, the detectable conflict signal peaks at late layers (L28, 88\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\% depth).
139	Probing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.
140	Injecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.
141	
142	\paragraph{Cross-model steering.}
143	Steering at Qwen's mid-layer (L14, 39\% depth; probe accuracy 70.2\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\text{test}} = 84$).
144	L23 (64\% depth; probe accuracy 73.2\%) is similarly negative (all $p = 1.0$).
145	Despite comparable probe accuracies (70--73\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.
146	The mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared.
147	
148	%% Table 3: Steering results
149	\begin{table}[t]
150	\centering
151	\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\dagger}$}
152	\label{tab:steering}
153	\small
154	\begin{tabular}{lcrrrrl}
155	\toprule
156	Layer & Depth & $\alpha$ & Steer (\%) & Ctrl (\%) & Fisher $p$ & Dir. \\
157	\midrule
158	\multicolumn{7}{l}{\textit{Llama-3.1-8B}} \\
159	\textbf{L13} & \textbf{41\%} & $\mathbf{+5}$ & \textbf{19.9} & \textbf{6.6} & $\mathbf{0.002}$ & \textbf{4 p$\to$c} \\
160	\textbf{L13} & \textbf{41\%} & $\mathbf{-20}$ & \textbf{36.0} & \textbf{17.6} & $\mathbf{<0.001}$ & \textbf{5 c$\to$p} \\
161	L13 (all) & 41\% & \multicolumn{4}{c}{\textit{identical to last-token}} & \\
162	L18 & 56\% & $+2$ & 3.7 & 1.5 & 0.447 & \\
163	L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
164	L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 0.370 & \\
165	\midrule
166	\multicolumn{7}{l}{\textit{Qwen3-8B}} \\
167	L14 & 39\% & $-10$ & \multicolumn{2}{c}{0 dir.\ flips} & 0.682 & \\
168	L23 & 64\% & --- & \multicolumn{2}{c}{0 dir.\ flips} & 1.000 & \\
169	\bottomrule
170	\end{tabular}
171	\begin{flushleft}
172	\footnotesize $^{\dagger}$ At $\alpha = +20$ (Llama L13), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.
173	\end{flushleft}
174	\end{table}
175	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "2b88e62f-3a89-4fd9-96e3-cf1015679d63",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2024qwen25}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET \\citep{rei2020comet} back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy to account for class imbalance.\nAll confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nBoth models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.1\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 71.2\\% on ZH$\\to$ZH.\nQwen reaches 75.3\\% on EN$\\to$EN (peak at layer 22, 61\\% depth) and 71.6\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for both models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across both architectures and both languages.\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.\nBoth models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nFor Llama, $\\Delta_{\\text{asym}} = +7.2$ percentage points (pp) with a 95\\% bootstrap CI of [1.1, 13.6]; for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7].\nThe magnitude of this asymmetry closely matches the XNLI non-conflict baseline (\\S\\ref{sec:xnli_baseline}), and the consistent direction across architectures suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n%% Table 1: Main cross-lingual probe results\n\\begin{table}[t]\n\\centering\n\\caption{Cross-lingual probe balanced accuracy (\\%) with bootstrap 95\\% CIs ($n \\geq 100$). $\\Delta_{\\text{asym}}$ = acc(ZH$\\to$EN) $-$ acc(EN$\\to$ZH), computed as the mean of paired bootstrap differences. Bold: best per-task direction.}\n\\label{tab:main_results}\n\\begin{tabular}{lcc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.1} & \\textbf{75.3} \\\\\nZH $\\to$ ZH & 71.2 & 71.6 \\\\\nEN $\\to$ ZH & 64.1 & 65.0 \\\\\nZH $\\to$ EN & 71.3 & 72.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.2 [1.1, 13.6] & +7.2 [$-$0.6, 13.7] \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nBoth models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7].\nBoth XNLI CIs exclude zero, and both overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nThe close match in asymmetry magnitude between conflict probes (Llama +7.2, Qwen +7.2 pp) and XNLI probes (Llama +6.0, Qwen +6.7 pp) indicates that the ZH$\\to$EN transfer advantage is not specific to knowledge conflict representations.\nInstead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\\to$ZH probe accuracy across strata.\nIf translation quality drove probe transfer, high-COMET samples would yield higher accuracy.\nTable~\\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\\Delta = +1.7$ pp, Fisher $p = 0.761$).\nTranslation quality does not confound the cross-lingual transfer results.\n\n\\paragraph{Token overlap.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, consistent with the minimal lexical overlap between the two languages.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \\emph{lower} accuracy.\nShared tokens do not drive cross-lingual transfer.\n\n%% Table 2: Confound exclusion\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_{\\text{probe}}$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_{\\text{probe}}$ into the last-token residual stream at a target layer during inference.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.\nNegative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.\nBoth results survive Bonferroni correction for multiple comparisons.\nThe bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.\n\n\\paragraph{Negative layers.}\nSteering at L28 (the probing peak layer, 88\\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\\ref{tab:steering}).\nL18 (the MLP probe peak, 56\\% depth) also shows no causal influence (all Fisher $p > 0.44$).\n\n\\paragraph{$\\alpha = +20$ reversal.}\nAt extreme perturbation magnitude ($\\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).\nThis indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.\n\n\\paragraph{Detection $\\neq$ Decision.}\nIn Llama, the detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\nInjecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.\n\n\\paragraph{Cross-model steering.}\nSteering at Qwen's mid-layer (L14, 39\\% depth; probe accuracy 70.2\\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\\text{test}} = 84$).\nL23 (64\\% depth; probe accuracy 73.2\\%) is similarly negative (all $p = 1.0$).\nDespite comparable probe accuracies (70--73\\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.\nThe mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared.\n\n%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Llama-3.1-8B}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL13 (all) & 41\\% & \\multicolumn{4}{c}{\\textit{identical to last-token}} & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B}} \\\\\nL14 & 39\\% & $-10$ & \\multicolumn{2}{c}{0 dir.\\ flips} & 0.682 & \\\\\nL23 & 64\\% & --- & \\multicolumn{2}{c}{0 dir.\\ flips} & 1.000 & \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$ (Llama L13), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}\n",
      "numLines": 175,
      "startLine": 1,
      "totalLines": 175
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the abstract following the constraints:

Key numbers from Introduction and Experiments:
- Llama-3.1-8B-Instruct and Qwen3-8B
- 77.1% and 75.3% balanced accuracy on EN
- ZH→EN > EN→ZH by ~7pp
- XNLI baseline: +6.0 and +6.7 pp, CIs overlap
- Probe peak at L28 (88% depth), causal steering at L13 (41% depth), Fisher p=0.002


- Late-layer interventions produce no significant behavioral change

I'm drafting the abstract now, keeping it between 150-200 words while incorporating the key findings about how multilingual LLMs handle conflicting cross-lingual information, the performance metrics, and the mechanistic insights about where language representation and causal influence operate in the model. determine the model's answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?

We address these questions by probing residual stream representations in Llama-3.1-8B-Instruct and Qwen3-8B, combined with cross-lingual transfer analysis, non-conflict baseline comparison on XNLI, confound exclusion, and representation steering.

Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry (ZH-to-EN exceeds EN-to-ZH by approximately 7 percentage points). This asymmetry, however, matches the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals, suggesting it stems from the model's general multilingual structure rather than conflict-specific encoding. A striking dissociation emerges between detection and decision: the probe signal peaks at late layers (88% depth), yet representation steering achieves causal influence only at mid-layer (41% depth), with late-layer interventions producing no significant effect. These results show that linear detectability doesn't guarantee causal relevance, which has important implications for how we approach probe-based intervention research. does the conflict signal encode, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution? We probe residual streams in Llama-3.1-8B-Instruct and Qwen3-8B using cross-lingual transfer analysis, a non-conflict baseline on XNLI, confound exclusion for translation quality and token overlap, and representation steering. Conflict signals are linearly detectable across languages with directional asymmetry in cross-lingual transfer—probes trained on Chinese transfer to English about 7 percentage points more accurately than the reverse, matching the non-conflict baseline in both magnitude and direction. A key dissociation emerges: the probe signal peaks at 88% depth but causal influence through steering only occurs at 41% depth, with late-layer interventions producing no effect. I'm setting up the experimental design by probing the residual stream representations in two multilingual models, using cross-lingual transfer analysis combined with a non-conflict baseline and controls for translation quality and token overlap to isolate the conflict signal.

The conflict signals show linear detectability across languages with a directional asymmetry—probes trained on Chinese transfer to English about 7 percentage points better than the reverse—which mirrors the non-conflict baseline pattern, suggesting this asymmetry comes from general multilingual structure rather than conflict-specific mechanisms.

There's a critical dissociation between where I can detect the signal and where it actually influences decisions: the probe peaks in late layers but steering interventions only work at mid-layer depth, with late-layer interventions having no effect, revealing that detectability doesn't guarantee causal relevance. I'm catching an issue with my phrasing—I have a participial clause ending a sentence, which violates the constraint against -ing phrases at sentence endings. Let me restructure this to split it into two clearer sentences that avoid the trailing participial modifier, making the logic more direct. aner. Let me recount the revised abstract to make sure it flows properly and hits all the key points without the AI-style trailing gerunds.

The abstract now establishes the research question about how multilingual LLMs handle conflicting information across languages, then describes the experimental approach using residual stream analysis on two models. The key finding is that conflict signals are linearly detectable across languages, with an interesting directional asymmetry where Chinese-to-English transfer outperforms the reverse by about 7 percentage points. I need to complete the thought about what this asymmetry matches and wrap up the abstract with the implications.

The asymmetry aligns with the non-conflict baseline from XNLI in both magnitude and direction, suggesting the model's general multilingual structure drives this pattern rather than conflict-specific mechanisms. More importantly, there's a critical dissociation between what we can detect and what actually influences the model's decisions: the conflict signal peaks in detectability at the deepest layers, but steering interventions only work at mid-layer depths, with late-layer interventions showing no causal effect. This reveals that linear detectability doesn't necessarily mean causal relevance, which has important implications for how we interpret probe-based intervention studies. I'm verifying the key statistics against the paper to ensure accuracy: the 7 percentage point asymmetry, the 88% depth for peak detection, and the 41% depth for causal steering all check out across both the introduction and experimental sections.

Now I'm running through the final constraints—word count, punctuation rules, avoiding certain phrases and jargon, proper terminology choices like "causal influence" instead of "causal control," and making sure all citations are properly formatted without LaTeX commands. Everything looks good, so I'm ready to output the abstract text without the LaTeX wrapper tags.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "7190fa5b-f5b9-4807-bf74-ccf9ae9c4d73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018woxdNbsoFimRVpQA2Aqy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11500,
      "cache_read_input_tokens": 24664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11500
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

_source line 12_

Now I have all the data. Let me verify the numbers are consistent across files, then write the abstract.

Key numbers confirmed:
- EN→EN: 77.1% (Llama), 75.3% (Qwen)
- Asymmetry: ~7pp both models
- XNLI baseline: +6.0 (Llama), +6.7 (Qwen), CIs overlap
- Probe peak: L28, 88% depth; causal: L13, 41% depth; Fisher p=0.002

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "d05292a1-7c66-4178-8c67-973355d303cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018woxdNbsoFimRVpQA2Aqy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11500,
      "cache_read_input_tokens": 24664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11500
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

_source line 13_

<details open><summary>🔧 Tool call — Write · `toolu_0186SR9yTtubCk6dSCx487Ez`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex",
  "content": "When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine the model's answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?\n\nWe probe residual stream representations in Llama-3.1-8B-Instruct and Qwen3-8B. Our analysis combines cross-lingual transfer, a non-conflict baseline on XNLI (Cross-lingual Natural Language Inference), confound exclusion for translation quality and token overlap, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English approximately 7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals; it inherits from the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: the probe signal peaks at late layers (88\\% depth), but representation steering achieves causal influence only at a mid-layer (41\\% depth), and all late-layer interventions produce no significant effect. These findings demonstrate that linear detectability does not imply causal relevance, with direct implications for probe-based intervention research.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "1cb01995-c7d7-4535-a8aa-04035acb43d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018woxdNbsoFimRVpQA2Aqy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11500,
      "cache_read_input_tokens": 24664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11500
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

_source line 14 · 2026-05-22T16:04:16.238Z_

<details><summary>↩ Tool result · `toolu_0186SR9yTtubCk6dSCx487Ez`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "f2faf5c2-86ac-46a7-ac53-fd25d73bfc71",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/abstract.tex",
    "content": "When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine the model's answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, does it share structure with general cross-lingual representations, and does detectability imply causal influence on resolution?\n\nWe probe residual stream representations in Llama-3.1-8B-Instruct and Qwen3-8B. Our analysis combines cross-lingual transfer, a non-conflict baseline on XNLI (Cross-lingual Natural Language Inference), confound exclusion for translation quality and token overlap, and representation steering. Conflict signals are linearly detectable across languages, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English approximately 7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in both magnitude and direction, with overlapping confidence intervals; it inherits from the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: the probe signal peaks at late layers (88\\% depth), but representation steering achieves causal influence only at a mid-layer (41\\% depth), and all late-layer interventions produce no significant effect. These findings demonstrate that linear detectability does not imply causal relevance, with direct implications for probe-based intervention research.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 15_

Abstract 已写入，200 words。约束逐项核查：

| 约束 | 状态 |
|------|------|
| 150-200 words | 200 |
| 无 em-dash/en-dash | 用冒号和分号替代 |
| 无 -ing 短语结尾 | 每句末尾均为名词/动词 |
| 无 delve/leverage/utilize | 无 |
| 关键数字 ≤3 | ~7pp, 88% depth, 41% depth |
| 无 "In this paper, we..." | 直接切入问题 |
| causal influence | 使用两处 |
| 缩写展开 | LLM, XNLI 均已展开 |
| 无 \cite | 无 |
| 数字一致性 | 与 Introduction/Experiments 一致 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "uuid": "73d82676-6169-4719-a2b8-1341e9d3e1da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYvgmUCfSfJK5Cufp8TrwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4462,
      "cache_read_input_tokens": 36164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4462
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

_source line 16_

Abstract 已写入，200 words。约束逐项核查：

| 约束 | 状态 |
|------|------|
| 150-200 words | 200 |
| 无 em-dash/en-dash | 用冒号和分号替代 |
| 无 -ing 短语结尾 | 每句末尾均为名词/动词 |
| 无 delve/leverage/utilize | 无 |
| 关键数字 ≤3 | ~7pp, 88% depth, 41% depth |
| 无 "In this paper, we..." | 直接切入问题 |
| causal influence | 使用两处 |
| 缩写展开 | LLM, XNLI 均已展开 |
| 无 \cite | 无 |
| 数字一致性 | 与 Introduction/Experiments 一致 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 80157,
  "duration_api_ms": 81551,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "75787e92-0d1d-4c00-8de8-5dd41644eb54",
  "total_cost_usd": 0.34022375000000005,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 28785,
    "cache_read_input_tokens": 72669,
    "output_tokens": 4886,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28785,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 245,
        "cache_read_input_tokens": 36164,
        "cache_creation_input_tokens": 4462,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4462
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1693,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018130000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 4886,
      "cacheReadInputTokens": 72669,
      "cacheCreationInputTokens": 28785,
      "webSearchRequests": 0,
      "costUSD": 0.33841075000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "89879cf0-e76a-4f2c-95c2-0cd0facfa24d"
}
```

</details>

---
