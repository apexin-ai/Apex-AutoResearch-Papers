# paper writing methods reframe

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_writing_methods_reframe_20260520T111845.log`
- **Structured JSON:** [`2269290c7701c3312c42.json`](../../sessions/22/2269290c7701c3312c42.json)

## Before a recorded user message

40 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
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
  "uuid": "dba9873e-b423-4ed7-90ad-a74b87efa2c7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1779291600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6620c1f3-d37a-4a86-b1d9-90fdffc0a3ff",
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184"
}
```

---

### Assistant

_source line 4_

I'll start by reading the skill file and the current method.tex in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "9d98edea-777d-430d-bbc1-b0336a599965",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115ZhXZiuUALt88WcWSFXY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14775,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14775
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

<details open><summary>🔧 Tool call — Read · `toolu_012qmm42sAfxT7QYy5pkY6vr`</summary>

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
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "7564be8a-ab2b-4006-9243-649c733e8402",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115ZhXZiuUALt88WcWSFXY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14775,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14775
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

_source line 6 · 2026-05-20T11:19:04.322Z_

<details><summary>↩ Tool result · `toolu_012qmm42sAfxT7QYy5pkY6vr`</summary>

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
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "54a7e338-0406-4440-bff1-a0d7cbc52f49",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Na8d6fzBoVxCsEsbMuCCjR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "3d7ebbbd-688b-4b48-932e-bffd36d49598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115ZhXZiuUALt88WcWSFXY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14775,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14775
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

_source line 8 · 2026-05-20T11:19:05.041Z_

<details><summary>↩ Tool result · `toolu_01Na8d6fzBoVxCsEsbMuCCjR`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	The experiments in \S\ref{sec:method_sensitivity}--\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.
5	This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to quantify their impact and identify the most reliable individual method (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
6	
7	
8	\subsection{Methodological Pitfalls in Lead-Lag Analysis}
9	\label{sec:pitfalls}
10	
11	We identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.
12	Each is documented below with representative data from our experiments; full results appear in \S\ref{sec:experiments}.
13	
14	\paragraph{Pitfall 1: Method sensitivity.}
15	Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs: 4 candidate canaries $\times$ 4 downstream metrics, including candidates later excluded per \S\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 37.5\% (permutation Granger), with Toda--Yamamoto achieving moderate rates (3--4/8 at $\alpha{\geq}0.50$); inter-method agreement is Cohen's $\kappa{=}0.185$, indicating poor agreement (\S\ref{sec:method_sensitivity}).
16	The spurious-signal rate (the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative) is at least 62.5\% across the primary methods.
17	This pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.
18	In a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.
19	
20	\paragraph{Pitfall 2: Spurious regression under shared trends.}
21	A single preprocessing decision, first-differencing to remove shared non-stationary trends~\cite{granger1974spurious}, can eliminate an entire analysis channel.
22	At $\alpha{=}1.0$, canary$\to$perplexity pairs appear near-universally significant in undifferenced analysis ($F{=}16$--$36$) but yield $F{\approx}0$, $p{=}0.99$ after differencing (Figure~\ref{fig:differencing_dmax}a; \S\ref{sec:method_sensitivity}).
23	In contrast, canary$\to$diversity pairs retain unanimous FDR significance after differencing (24/24$\to$24/24).
24	Without the differencing diagnostic, an analyst would conclude that canaries predict perplexity, a conclusion entirely driven by co-trending rather than temporal precedence.
25	The danger lies in the selective nature of this confound: only by applying the diagnostic can one determine which channels are genuine and which are artifacts of shared non-stationarity.
26	
27	\paragraph{Pitfall 3: Regime dependence.}
28	Even after fixing the statistical method, the contamination level~$\alpha$ determines whether a lead-lag relationship is detectable.
29	Permutation Granger tests (first-differenced, BH FDR-corrected at $q{=}0.05$) find 6/8 pairs FDR-significant at both $\alpha{=}0.50$ (2~fp32 seeds, consistent) and $\alpha{=}1.0$, but 0/8 through $\alpha{=}0.45$ (\S\ref{sec:regime}).
30	The transition zone at $\alpha{\approx}0.45$--$0.50$ is where method divergence is most dangerous: correlation-based methods find significance across all levels while causal methods remain null through $\alpha{=}0.45$ (a faint single-pair signal appears at $\alpha{=}0.25$, FDR $p{=}0.053$, but does not reach aggregate detection), creating the maximum risk of spurious conclusions when only a single (liberal) method is used.
31	This regime dependence is consistent with theoretical expectations about signal-to-noise limits in short ecological time series \cite{boettiger2012limits}, and suggests that detectability boundaries should be explicitly mapped rather than assumed.
32	
33	
34	\subsection{Multi-Method Consensus Framework}
35	\label{sec:consensus}
36	
37	The pitfalls above motivate a multi-method consensus approach inspired by specification curve analysis \cite{simonsohn2020specification} and multi-method validation in early-warning signal detection \cite{scheffer2009early}: rather than relying on any single method, we apply multiple independent methods to quantify how analytic choices determine conclusions, using agreement thresholds as diagnostic benchmarks.
38	
39	\paragraph{Formal definition.}
40	Given $M$ lead-lag detection methods $\{m_1, \ldots, m_M\}$ and $N$ independent random seeds, a canary$\to$downstream pair $(X, Y)$ is classified as \textsc{robust} if and only if:
41	\begin{enumerate}
42	    \item At least $K$ of $M$ methods judge the pair FDR-significant, where each method independently applies Benjamini--Hochberg correction at $q{=}0.05$; and
43	    \item At least $S$ of $N$ seeds replicate this conclusion.
44	\end{enumerate}
45	The thresholds $(K, S)$ control the trade-off between false positive and false negative rates.
46	Methods with different inductive biases (correlation-based methods that detect any temporal association versus Granger-type methods that test directional predictive improvement \cite{granger1969investigating}) provide complementary evidence.
47	Their convergence on a given pair constitutes stronger evidence than agreement among methods sharing the same statistical assumptions.
48	We note that Granger precedence establishes temporal predictive improvement, not true causality \cite{shojaie2022granger}; our framework inherits this limitation.
49	
50	\paragraph{Method tiering.}
51	The five methods are organized into two tiers based on empirical reliability.
52	Three \emph{primary} methods---naive cross-correlation, differenced cross-correlation, and permutation Granger causality---produce consistent results across independent analysis pipelines and exhibit adequate statistical power at $T{=}11$ generations.
53	Two methods are classified as \emph{supplementary}: threshold onset detection due to power limitations at $T{=}11$ under corrected $3\sigma$ calibration (\S\ref{sec:threshold_limitation}), and Toda--Yamamoto Granger causality, which achieves moderate detection (3--4/8 at $\alpha{\geq}0.50$) but with reduced power relative to the primary methods (\S\ref{sec:ty_limitation}).
54	The consensus panel thus comprises four contributing methods (three primary, one moderate supplementary), with threshold onset near-inoperative at $T{=}11$.
55	The consensus threshold $K{\geq}3$ out of 5 methods requires agreement among at least the three primary methods or two primary methods plus TY, making $K{\geq}3$ a \emph{stronger} standard than a simple majority vote would suggest.
56	
57	\paragraph{Sequential filtering pipeline.}
58	In practice, the $K$-of-$M$ voting operates over all five methods applied independently to each pair; the sequential pipeline below describes the order in which results are examined, enabling early termination and interpretable diagnostics at each stage (Figure~\ref{fig:consensus_workflow}):
59	\begin{enumerate}
60	    \item \textbf{Naive correlation scan.} Cross-correlation at maximum lag~5 with BH correction serves as a permissive baseline; all pairs with any temporal association pass.
61	    \item \textbf{First-differencing diagnostic.} Cross-correlation is recomputed on first-differenced series, testing whether temporal associations survive removal of shared linear trends. Pairs that lose significance are flagged as potential spurious regressions.
62	    \item \textbf{Permutation Granger causality.} Permutation-based Granger causality tests \cite{shojaie2022granger} on first-differenced series (5{,}000 permutations, BH correction at $q{=}0.05$) assess directional predictive improvement: whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.
63	    \item \textbf{Multi-seed replication.} The conclusion must hold across $S$ of $N$ independent training seeds, filtering seed-specific artifacts.
64	\end{enumerate}
65	At $\alpha{=}1.0$, this pipeline progressively filters: 16 pairs pass Stage~1, 14 survive Stage~2 (differencing removes 2 marginal canary$\to$perplexity pairs), 6 survive Stage~3 (Granger testing eliminates remaining canary$\to$perplexity pairs and failed canary candidates), and all~6 survive Stage~4 (multi-seed replication confirms all Granger-significant pairs).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\linewidth]{figures/consensus_workflow.pdf}
70	\caption{Sequential filtering pipeline of the multi-method consensus framework. Starting from all candidate canary$\to$downstream pairs, the pipeline applies four stages: (1)~naive cross-correlation scan (permissive baseline), (2)~first-differencing diagnostic (removes shared-trend artifacts), (3)~permutation Granger causality (tests directional predictive improvement), and (4)~multi-seed replication (filters seed-specific artifacts). At $\alpha{=}1.0$ (Pythia-410M), the pipeline reduces 16 candidate pairs to 6 robust pairs: 16$\to$14$\to$6$\to$6. The $K$-of-$M$ consensus vote operates in parallel across all five methods; the sequential ordering provides interpretable diagnostics at each stage.}
71	\label{fig:consensus_workflow}
72	\end{figure}
73	
74	\paragraph{Practical guidance.}
75	The consensus thresholds $(K, S)$ should be chosen to match the analyst's tolerance for false positives versus false negatives.
76	Table~\ref{tab:practical_guidance} provides four recommended tiers, calibrated against our experimental controls (\S\ref{sec:calibration}).
77	Tier~3 ($K{\geq}4/5$, $S{\geq}3/4$) achieves the best trade-off under the full 5-method panel: zero false positives while recovering all six reference pairs; however, threshold onset's near-zero power at $3\sigma$ (\S\ref{sec:threshold_limitation}) makes it near-inoperative, and Toda--Yamamoto provides moderate supplementary signal (3--4/8 at $\alpha{\geq}0.50$; \S\ref{sec:ty_limitation}), making $K{\geq}3$ the operationally relevant consensus threshold.
78	With four contributing methods (three primary plus TY), $K{\geq}3$ draws on a broader evidence base than the three primary methods alone; TY's moderate detection at $\alpha{\geq}0.50$ strengthens consensus conclusions where it contributes a positive vote.
79	Cross-architecture validation confirms $K{\geq}3$ reaches ${\geq}6/8$ in 10 of 14 architecture-seed combinations (\S\ref{sec:generalization}).
80	Method subset ablation confirms that this threshold is uniquely optimal: at $K{=}3/5$, the null-control FPR is 37.5\% (unacceptable); at $K{=}4/5$, FPR drops to 0\% while retaining 6/6 reference-pair sensitivity; at $K{=}5/5$, FPR remains 0\% but sensitivity falls to 3/6.
81	Shapley value analysis (exact enumeration of all 32 coalitions; Figure~\ref{fig:shapley}) identifies naive cross-correlation as the sole positive contributor to FPR (Shapley(FPR)${=}{+}0.348$) and permutation Granger as the strongest FPR suppressor (Shapley(FPR)${=}{-}0.194$), the only method combining 0\% null-control FPR with high sensitivity.
82	Toda--Yamamoto's Shapley contribution (FNR${=}{-}0.158$) reflects moderate supplementary value: it reduces consensus FNR without introducing false positives (\S\ref{sec:ty_limitation}).
83	
84	\begin{figure}[t]
85	\centering
86	\includegraphics[width=\linewidth]{figures/shapley_method_contribution.pdf}
87	\caption{Shapley value decomposition of method contributions to consensus FPR and FNR (exact enumeration of all $2^5{=}32$ coalitions, $K{=}\max(1,|S|{-}1)$). FPR is computed at $\alpha{=}0.0$ (3~seeds $\times$ 8~pairs${=}$24 observations); FNR at $\alpha{=}1.0$ (4~seeds, 6 reference pairs). Naive cross-correlation is the only positive FPR contributor (${+}0.348$); permutation Granger is the strongest FPR suppressor (${-}0.194$). Toda--Yamamoto contributes moderate FNR suppression (Shapley FNR${=}{-}0.158$) as a supplementary method (\S\ref{sec:ty_limitation}).}
88	\label{fig:shapley}
89	\end{figure}
90	Tier~4 requires unanimity across methods and seeds, which incurs elevated false negative rates; TY's moderate detection (3--4/8) means that requiring $5/5$ unanimity is substantially more restrictive than $4/5$, particularly at intermediate contamination levels where TY may not contribute a positive vote.
91	
92	\begin{table}[t]
93	\centering
94	\small
95	\caption{Practical guidance tiers for lead-lag consensus analysis. Tier~3 ($K{\geq}4/5$, $S{\geq}3/4$) is uniquely optimal under the full 5-method panel; with threshold onset power-limited (\S\ref{sec:threshold_limitation}) and Toda--Yamamoto providing moderate supplementary signal (\S\ref{sec:ty_limitation}), $K{\geq}3$ draws on four contributing methods. FPR is calibrated at $\alpha{=}0.0$ (null control, $M{=}5$ methods, $N{=}3$ seeds, Pythia-410M). FNR is calibrated at $\alpha{=}1.0$ against 6 effect-size reference pairs using a 4-method panel (excluding differenced cross-correlation); $N{=}4$ seeds (\S\ref{sec:calibration}).}
96	\label{tab:practical_guidance}
97	\begin{tabular}{llcccc}
98	\toprule
99	Tier & Use Case & $K/M$ & $S/N$ & FPR & FNR \\
100	\midrule
101	1 & Exploratory     & ${\geq}1/5$ & ${\geq}1/N$ & 100\%  & 0\%    \\
102	2 & Screening       & ${\geq}3/5$ & ${\geq}2/N$ & 37.5\% & 0\%    \\
103	3 & Confirmatory    & ${\geq}4/5$ & ${\geq}3/N$ & 0\%    & 0\%    \\
104	4 & Conservative    & $5/5$       & $N/N$        & 0\%    & 50\% \\
105	\bottomrule
106	\end{tabular}
107	\end{table}
108	
109	
110	\subsection{Empirical Calibration}
111	\label{sec:calibration}
112	
113	We calibrate the framework using two built-in experimental controls.
114	Full numerical results are reported in Table~\ref{tab:fpr_fnr}.
115	
116	\paragraph{False positive rate.}
117	The $\alpha{=}0.0$ condition serves as a null control: no synthetic data is injected, so any detected lead-lag association is a false positive.
118	At $K{=}1$ (any single method suffices), FPR${=}$75\%: naive cross-correlation flags 6/8 forward-direction pairs.
119	At $K{=}2$, FPR drops to ${\leq}$37.5\%; at $K{=}3$, to ${\leq}$12.5\%; and at $K{\geq}4$, FPR${=}$0\%.
120	The consensus framework at Tier~3 matches the false positive performance of the best individual method (permutation Granger, 0\%) while providing robustness against miscalibration of any single method.
121	
122	\paragraph{False negative rate.}
123	At $\alpha{=}1.0$ with 4~seeds, we define six \emph{effect-size reference pairs} using criteria independent of the consensus methods:
124	\begin{enumerate}
125	    \item[(a)] The canary$\to$downstream drift ratio at $\alpha{=}1.0$ must exceed $3\times$ the $\alpha{=}0.0$ baseline drift (canary ratios: entropy $11.93\times$, ECE $73.12\times$, both far above threshold); and
126	    \item[(b)] Canary onset must strictly precede downstream onset by at least one generation (canary onset: generation~1; diversity onset: generations~3--9).
127	\end{enumerate}
128	These criteria yield token entropy and ECE each predicting distinct-1, distinct-2, and distinct-3~\cite{li2016diversity}.
129	The perplexity channel is excluded because its onset (generation~1) coincides with canary onset, consistent with, but not derived from, the differencing diagnostic finding that canary$\to$perplexity associations are spurious (\S\ref{sec:method_sensitivity}).
130	The effect-size threshold is robust: at $2\times$, $3\times$, and $5\times$ the baseline drift, the reference set remains identical (6~pairs), because canary ratios ($11.93\times$ and $73.12\times$) far exceed all thresholds.
131	
132	FNR is calibrated using a 4-method panel excluding differenced cross-correlation, which shares statistical properties with detrending-based criteria and could introduce circularity.
133	At $K{\geq}3/4$, $S{\geq}3/4$, all six reference pairs are recovered (FNR${=}$0\%).
134	At $K{=}4/4$, $S{=}4/4$, FNR rises to 50\%, reflecting TY's moderate detection power (4/8 at $\alpha{=}1.0$; \S\ref{sec:ty_limitation}).
135	
136	\paragraph{Symmetric calibration.}
137	Both FPR and FNR are validated on the joint method${\times}$seed dimension: FPR across 3~seeds at $\alpha{=}0.0$ (0/24 pairs at $K{\geq}3$, $3\sigma$) and FNR across 4~seeds at $\alpha{=}1.0$ (6/6 reference pairs recovered at $K{\geq}3/4$, $S{\geq}3/4$).
138	Cross-seed FPR variance is negligible: all three null-control seeds yield 0/8 robust pairs at $K{\geq}3$ ($3\sigma$), confirming seed-independent performance.
139	
140	
141	\paragraph{Threshold onset detection: power limitations at $3\sigma$.}
142	\label{sec:threshold_limitation}
143	Post-hoc validation of the threshold onset implementation (M028) revealed that the published $2\sigma$ calibration was mislabeled as $3\sigma$.
144	Under corrected $3\sigma$ calibration, threshold onset yields 0/8 significant pairs in 8 of 12 cross-architecture conditions (Table~\ref{tab:generalization}) and at most 2/8 in the remainder, reducing it to a near-zero-power method at $T{=}11$ generations; any threshold onset detections should therefore be interpreted as lower-bound estimates.
145	This low power is expected: with only 10 generation-over-generation differences, the null variance estimate has few degrees of freedom, and a $3\sigma$ exceedance threshold becomes overly conservative.
146	We retain threshold onset as a supplementary method for completeness and report its results transparently, but adopt permutation Granger forward significance as the primary detection indicator in cross-architecture analyses.
147	
148	\paragraph{Toda--Yamamoto Granger: moderate supplementary signal.}
149	\label{sec:ty_limitation}
150	Post-hoc analysis identified a statsmodels API incompatibility that initially produced artificially low Toda--Yamamoto detection rates.
151	After correcting the implementation, TY achieves moderate detection: 3/8 forward-direction pairs at $\alpha{=}0.50$ (seed~42), 3/8 at $\alpha{=}0.75$, and 4/8 at $\alpha{=}1.0$ (Table~\ref{tab:method_comparison}).
152	These rates are lower than permutation Granger (6--8/8) but confirm that TY captures genuine signal at $\alpha{\geq}0.50$, consistent with the method's theoretical motivation~\cite{toda1995statistical}.
153	TY is classified as a moderate supplementary method: it contributes to the consensus panel but does not serve as a primary detection indicator due to reduced statistical power at $T{=}11$ (the augmentation order $d_{\max}$ consumes additional degrees of freedom) and sensitivity to the $d_{\max}$ hyperparameter (Figure~\ref{fig:differencing_dmax}b).
154	With TY providing moderate signal, the consensus panel comprises four contributing methods (three primary plus TY as supplementary), strengthening the $K{\geq}3$ threshold: at $\alpha{=}0.50$ (seed~42), $K{\geq}3$ rises from 5/8 to 6/8 with TY's corrected contribution.
155	At $\alpha{\geq}0.50$, $K{\geq}4$ consensus (4 of 5 methods agree) emerges in 3/8 pairs, demonstrating that multi-method agreement extends beyond the primary trio.
156	
157	\subsection{Multi-Method Consensus Test (MMCT)}
158	\label{sec:mmct}
159	
160	The uniform threshold ($K{\geq}4/5$) achieves FPR${=}$0\% and FNR${=}$0\% on reference extremes (\S\ref{sec:calibration}), but this ad-hoc threshold lacks formal statistical grounding: null-calibrated permutation testing assigns $p{=}0.16$ to $K{\geq}4/5$, failing to reach significance at conventional levels.
161	The threshold also treats all methods equally, despite the heterogeneous error profiles documented in \S\ref{sec:pitfalls}: naive cross-correlation has 75\% forward-direction null-control FPR while permutation Granger has 0\%.
162	We formalize the \emph{Multi-Method Consensus Test} (MMCT), a weighted consensus framework that assigns each method influence proportional to its empirical specificity, following the specification curve tradition~\cite{simonsohn2020specification} in which analytical choices are systematically varied and aggregated rather than arbitrarily fixed~\cite{bell2022modeling}.
163	MMCT serves as an evaluation framework rather than an end in itself: its primary function is to enable systematic comparison of detection methods under controlled conditions, identifying which individual methods are reliable and why others fail.
164	We do not claim a novel statistical method; MMCT is a consensus testing protocol adapted to the specific constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
165	
166	\paragraph{FPR-inverse weighting.}
167	Let $\hat{\text{FPR}}_k$ denote the empirical false positive rate of method $m_k$, estimated from $N_0$ null-control observations at $\alpha{=}0.0$ across $S$ seeds.
168	Each method receives weight
169	\begin{equation}
170	    w_k = \frac{1}{\max(\hat{\text{FPR}}_k,\; \epsilon)},
171	    \label{eq:fpr_weight}
172	\end{equation}
173	where $\epsilon{=}0.01$ prevents division by zero.
174	Methods with low FPR (e.g., permutation Granger at 0\%, receiving $w_k{=}100$) dominate the consensus; methods with high FPR (e.g., naive cross-correlation at 75\%, receiving $w_k{\approx}1.3$) are effectively downweighted.
175	
176	\paragraph{Consensus score.}
177	Given $M$ methods that return binary decisions $d_k \in \{0, 1\}$ (FDR-significant or not) for a candidate pair $(X, Y)$, the weighted consensus score is:
178	\begin{equation}
179	    W(X \to Y) = \frac{\sum_{k=1}^{M} w_k \cdot d_k}{\sum_{k=1}^{M} w_k}.
180	    \label{eq:consensus_score}
181	\end{equation}
182	When all weights equal~1 (uniform mode), $W$ reduces to $K/M$, and thresholding at $W \geq 4/5$ recovers the uniform $K{\geq}4$ rule exactly.
183	
184	\paragraph{Statistical testing.}
185	The null distribution of $W$ is estimated from the $\alpha{=}0.0$ control condition, where no synthetic contamination is present and any detected lead-lag association is a false positive.
186	The $N_0$ null-control pairs yield a reference distribution $\{W_0^{(j)}\}_{j=1}^{N_0}$, and the MMCT $p$-value is:
187	\begin{equation}
188	    p_{\text{MMCT}} = \frac{|\{j : W_0^{(j)} \geq W_{\text{obs}}\}|}{N_0}.
189	    \label{eq:pvalue}
190	\end{equation}
191	We reject the null of no lead-lag relationship at significance level $\alpha_{\text{test}}$.
192	
193	\paragraph{Bidirectional filtering.}
194	MMCT tests both directions independently: $W(X \to Y)$ and $W(Y \to X)$.
195	A stricter bidirectional mode requires forward significance with reverse non-significance.
196	Empirically, bidirectional and forward-only detection rates are identical across all contamination levels tested, indicating that pairs reaching weighted consensus in the forward direction consistently fail to reach consensus in reverse.
197	We therefore adopt forward-only (weighted pair forward) as the default MMCT configuration.
198	Algorithm~\ref{alg:mmct} summarizes the procedure.
199	
200	\begin{algorithm}[t]
201	\caption{Multi-Method Consensus Test (MMCT)}
202	\label{alg:mmct}
203	\begin{algorithmic}[1]
204	\Require Methods $\{m_1, \ldots, m_M\}$; pair $(X, Y)$; null pairs $\{(X_0^{(j)}, Y_0^{(j)})\}_{j=1}^{N_0}$; floor $\epsilon$; level $\alpha_{\text{test}}$
205	\Ensure Decision $d$, score $W$, $p$-value
206	\Statex \textbf{Phase 1: Estimate weights from null control}
207	\For{$k = 1, \ldots, M$}
208	    \State $\hat{\mathrm{FPR}}_k \gets$ null-control rejection rate of $m_k$
209	    \State $w_k \gets 1 / \max(\hat{\mathrm{FPR}}_k, \epsilon)$
210	\EndFor
211	\Statex \textbf{Phase 2: Compute weighted consensus}
212	\For{$k = 1, \ldots, M$}
213	    \State $d_k \gets m_k(X, Y)$ \Comment{1 if FDR-significant}
214	\EndFor
215	\State $W \gets \sum_k w_k d_k \;/\; \sum_k w_k$
216	\Statex \textbf{Phase 3: Null-distribution $p$-value}
217	\For{$j = 1, \ldots, N_0$}
218	    \State $W_0^{(j)} \gets$ consensus score of $(X_0^{(j)}, Y_0^{(j)})$
219	\EndFor
220	\State $p \gets |\{j : W_0^{(j)} \geq W\}| / N_0$
221	\State \Return $\mathbb{1}[p < \alpha_{\text{test}}]$, $W$, $p$
222	\end{algorithmic}
223	\end{algorithm}
224	
225	\paragraph{Empirical comparison.}
226	Table~\ref{tab:mmct_ablation} compares per-method detection rates across contamination levels, revealing the systematic comparison that motivates our method recommendation.
227	The five methods exhibit sharply divergent dose-response profiles: naive cross-correlation maintains elevated FPR at the null (75\%) but rises to 87.5\% at $\alpha{=}0.75$; differenced cross-correlation achieves zero null-control FPR but detects in both forward and reverse directions, failing to provide directional separation; threshold onset detects only at $\alpha{=}0.50$ (50\%) and returns to zero at $\alpha{=}0.75$ under $3\sigma$ calibration; Toda--Yamamoto achieves moderate detection at $\alpha{\geq}0.50$ (37.5\%) with zero null-control FPR but lower sensitivity than permutation Granger.
228	Permutation Granger alone provides the cleanest dose-response profile, with a sharp step function from 0/8 (blind spot, $\alpha{\leq}0.45$) to 6/8 (onset, $\alpha{=}0.50$, dual-seed confirmed) and reliable detection at $\alpha{\geq}0.75$ (Table~\ref{tab:method_comparison}; \S\ref{sec:regime}).
229	
230	Permutation Granger produces binary per-pair verdicts that yield a steep onset of detection: a faint signal at $\alpha{=}0.25$ (best pair FDR $p{=}0.053$) that does not reach aggregate detection through $\alpha{=}0.45$, then an abrupt jump to 6/8 at $\alpha{=}0.50$ (fp32), with a non-monotonic dip at $\alpha{=}0.60$ (s42: 3/8, s43: 0/8; dual-seed confirmed synchronous collapse zone; \S\ref{sec:regime}).
231	This step-function profile, combined with zero null-control FPR and Shapley FPR suppression of $-0.194$, identifies PermG as the recommended individual detection method.
232	Cross-architecture validation confirms PermG fwd ${\geq}6/8$ in 13 of 15 conditions, with multi-method consensus ($K{\geq}3$) reaching ${\geq}6/8$ in 10 of 14 with known consensus (\S\ref{sec:generalization}).
233	MMCT weighted consensus further captures graded detection strength even where individual methods remain below threshold, providing formal $p$-values that the uniform $K$-of-$M$ threshold lacks; however, the systematic comparison reveals that PermG alone provides comparable or superior detection to the full consensus framework at all contamination levels tested.
234	With TY contributing as a fourth method, full 5/5 consensus becomes achievable: at $\alpha{=}0.50$ (seed~42), the ECE$\to$distinct-3 pair reaches significance across all five methods, demonstrating that the consensus panel can converge unanimously even near the onset boundary when the canary--downstream coupling is strong.
235	
236	\begin{table}[t]
237	\centering
238	\small
239	\caption{Per-method forward-direction detection rates across contamination levels (Pythia-410M, seed~42, fp32). Each cell reports the fraction of 8 canary$\to$downstream pairs reaching BH-corrected significance ($q{=}0.05$). Per-method dose-response reveals the systematic comparison that identifies PermG as the recommended method (\S\ref{sec:case_study}). Cross-condition results at $\alpha{=}1.0$ are reported in Table~\ref{tab:mmct_cross}. $^\dagger$Moderate supplementary method (\S\ref{sec:ty_limitation}); FPR$_\text{null}$ pending (null condition not yet run through corrected pipeline).}
240	\label{tab:mmct_ablation}
241	\begin{tabular}{lcccc}
242	\toprule
243	Method & FPR$_\text{null}$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ \\
244	\midrule
245	Naive XCorr              & 75   & 12.5 & 37.5 & 87.5 \\
246	Diff.\ XCorr             & 0    & 37.5 & 87.5 & 75   \\
247	Threshold ($3\sigma$)    & ---  & 0    & 50   & 0    \\
248	Perm.\ Granger           & 0    & 0    & 75   & 75   \\
249	Toda--Yamamoto$^\dagger$ & ---  & 0    & 37.5 & 37.5 \\
250	\bottomrule
251	\end{tabular}
252	\end{table}
253	
254	\paragraph{Backward compatibility.}
255	Setting all weights $w_k{=}1$ reduces MMCT to the uniform $K$-of-$M$ threshold, making the existing consensus framework (\S\ref{sec:consensus}) a special case.
256	Descriptively, $K{\geq}4/5$ achieves FPR${=}$0\% and FNR${=}$0\% on reference extremes (\S\ref{sec:calibration}); however, null-calibrated testing assigns $p{=}0.16$ to this threshold, indicating that it does not reach conventional significance levels.
257	MMCT weighted consensus resolves this gap by providing formal $p$-values (Eq.~\ref{eq:pvalue}) grounded in the empirical null distribution.
258	
259	\paragraph{Cross-condition stability.}
260	Table~\ref{tab:mmct_cross} reports MMCT weighted consensus across all seven experimental conditions at $\alpha{=}1.0$.
261	Detection ranges from 4/8 to 8/8 while FPR remains 0 at the null control across all conditions, confirming that FPR-inverse weighting generalizes beyond the calibration setup.
262	GPT-2-medium achieves the highest detection rate (8/8), consistent with its stronger per-method signal, demonstrating that MMCT's FPR-inverse weighting extracts graded detection strength that binary per-method verdicts miss.
263	
264	\begin{table}[t]
265	\centering
266	\small
267	\caption{MMCT weighted forward consensus across experimental conditions ($\alpha{=}1.0$, FPR-inverse weighting). Each cell reports significant canary$\to$downstream pairs out of 8 (2~canaries $\times$ 4~downstream metrics). All conditions maintain FPR${=}$0 at $\alpha{=}0.0$. Values may be updated pending parameter consistency verification.}
268	\label{tab:mmct_cross}
269	\begin{tabular}{lc}
270	\toprule
271	Condition & Sig / 8 \\
272	\midrule
273	Baseline (Pythia-410M / Wiki)     & 5/8 \\
274	Architecture: GPT-2-medium / Wiki & \textbf{8/8} \\
275	Architecture: OPT-1.3B / Wiki     & 5/8 \\
276	Scale: Pythia-1.4B / Wiki (s42)   & 4/8 \\
277	Scale: Pythia-1.4B / Wiki (s43)   & 4/8 \\
278	Domain: Pythia-1B / C4 (s42)      & 5/8 \\
279	Domain: Pythia-1B / C4 (s43)      & 4/8 \\
280	\bottomrule
281	\end{tabular}
282	\end{table}
283	
284	\subsection{Theoretical Motivation: Why Entropy Leads Diversity}
285	\label{sec:theory}
286	
287	The empirical lead-lag relationship between token entropy and lexical diversity (\S\ref{sec:regime}) admits a simple theoretical motivation grounded in the distinct mathematical properties of continuous and discrete summary statistics.
288	We present three arguments that, taken together, predict the observed temporal ordering and its dependence on contamination strength.
289	These arguments provide intuition rather than formal proof; the dose-response experiments in \S\ref{sec:regime} test the resulting predictions empirically.
290	
291	\paragraph{Continuous versus discrete response.}
292	Token entropy $H(p_t^{(g)}) = -\sum_v p_v \log p_v$ is a continuous functional of the token distribution $p_t^{(g)}$ at generation $g$: any infinitesimal shift in $p_t^{(g)}$ produces a proportional change in $H$.
293	Distinct-$n$ diversity $D_k^{(g)}$, by contrast, is a counting statistic.
294	An $n$-gram contributes to $D_k^{(g)}$ only when its probability exceeds an effective sampling threshold $\tau_n \approx 1/N$, where $N$ is the number of generated tokens.
295	Below $\tau_n$, the $n$-gram is absent from finite samples regardless of its true probability.
296	$D_k^{(g)}$ therefore responds to distributional change in discrete steps: it remains constant while probabilities drift within the interval above $\tau_n$, then drops abruptly when a probability crosses the threshold.
297	Because $H$ tracks every distributional perturbation while $D_k^{(g)}$ remains silent until a threshold crossing occurs, entropy is sensitive to distributional change strictly before diversity registers it.
298	
299	\paragraph{Predicted detectability regimes.}
300	The continuous-versus-discrete asymmetry determines not just the ordering of responses but the \emph{detectability} of their temporal offset.
301	We model Granger-type detectability as the product of two competing factors:
302	\begin{equation}
303	    \text{Detectability}(\alpha) \;\propto\; S(\alpha) \times R(\alpha),
304	    \label{eq:detectability}
305	\end{equation}
306	where $S(\alpha)$ is the \emph{signal strength} (the magnitude of distributional shift induced by contamination) and $R(\alpha)$ is the \emph{temporal resolution} (the generational gap between the entropy response and the diversity response).
307	
308	$S(\alpha)$ increases monotonically with $\alpha$: more synthetic data induces larger distributional shifts.
309	$R(\alpha)$, by contrast, is non-monotonic.
310	At low $\alpha$, entropy and diversity respond in different generations ($R$ large); at a critical intermediate $\alpha$, \emph{relaxation time matching} occurs---the perturbation strength aligns the entropy and diversity relaxation times so that both metrics shift within the same generation, driving $R \to 0$.
311	At high $\alpha$, the perturbation is severe enough that entropy collapses within generation~0$\to$1 (the continuous-functional advantage saturates immediately), while diversity still requires generation~1$\to$2 to fully manifest the loss---tail $n$-grams near $\tau_n$ persist temporarily before crossing the threshold---and the one-generation lead recovers ($R$ large again).
312	
313	The competition between $S$ and $R$ predicts four regimes:
314	\begin{enumerate}
315	\item \textbf{Blind} ($\alpha \leq 0.45$).
316	$S$ falls below the detection floor; $S \times R \approx 0$ regardless of $R$.
317	\item \textbf{Onset} ($\alpha \approx 0.50$).
318	$S$ crosses the detection threshold while $R$ remains high (entropy leads diversity by a full generation); $S \times R$ is sufficient for detection.
319	Between the blind and onset regimes, the framework predicts a \emph{canary-only window} in which entropy shifts detectably but no $n$-grams have yet crossed $\tau_n$; we lack the $\alpha$ resolution to confirm this (our grid jumps from $0.25$ to $0.50$) and leave verification to future work with finer spacing in $[0.10, 0.45]$.
320	\item \textbf{Synchronous dip} ($\alpha \approx 0.60$).
321	$S$ continues increasing, but $R$ drops sharply: relaxation time matching at this $\alpha$ compresses the entropy--diversity lag to near zero, producing a local minimum in $S \times R$.
322	\item \textbf{Detection} ($\alpha \geq 0.75$).
323	$S$ grows large enough to dominate the product despite reduced $R$; the continuous-functional advantage reasserts across generations, and $S \times R$ recovers.
324	\end{enumerate}
325	These four regimes align with the empirical dose-response (\S\ref{sec:regime}): blind at $\alpha{\leq}0.45$ (PermG 0/8), onset at $\alpha{=}0.50$ (6/8, dual-seed), synchronous dip at $\alpha{=}0.60$ (0--3/8, dual-seed), and detection at $\alpha{\geq}0.75$ (5--6/8 per seed, three seeds; 6/8 per seed at $\alpha{=}1.0$, four seeds).
326	The non-monotonic profile is a prediction of the $S \times R$ framework, not an anomaly requiring post-hoc explanation; indeed, non-monotonic dose-response curves are well-documented across disciplines.
327	The four-regime profile mirrors the hormetic dose-response in toxicology, where intermediate doses produce qualitatively different effects from both low and high doses~\cite{calabrese2003hormesis}.
328	The temporal resolution collapse at intermediate $\alpha$ ($R \to 0$) corresponds to the known failure of Granger-type tests under contemporaneous coupling~\cite{deshpande2010instantaneous}: when entropy and diversity shift within the same generation (lag${=}0$), the causal test loses statistical power by construction, not by methodological deficiency.
329	The detection dip is also consistent with critical speeding-up phenomena in ecological regime shifts, where early-warning indicators exhibit non-monotonic behavior near phase boundaries rather than the monotonic rise predicted by classical critical slowing down~\cite{titus2020speeding}.
330	We emphasize that the $S \times R$ model provides qualitative intuition, not quantitative derivation; the regime boundaries depend on model capacity, dataset properties, and sample size $N$.
331	
332	\paragraph{Detection threshold vs.\ accumulated contamination.}
333	The detection phase transition at $\alpha_c{=}0.476$ (\S\ref{sec:regime}) reveals that Granger detectability depends on the \emph{per-generation} mixing ratio $\alpha$, not on cumulative contamination.
334	After $G{=}10$ generations, cumulative synthetic fraction reaches $C(\alpha, G) = 1 - (1{-}\alpha)^G$: at $\alpha{=}0.45$, $C = 99.75\%$; at $\alpha{=}0.50$, $C = 99.90\%$---a difference of 0.15 percentage points---yet PermG detection jumps from 0/8 to 6/8.
335	The explanation lies in the per-generation signal.
336	PermG detects temporal lead-lag from the time series of inter-generation entropy shifts $\{\Delta h^{(g)}\}_{g=1}^G$, where $\Delta h^{(g)} \propto \alpha \cdot d_{\mathrm{TV}}(p_g^{\mathrm{model}}, p^{\mathrm{real}})$ captures the per-episode perturbation scaled by the distributional gap at generation~$g$.
337	The critical threshold $\alpha_c$ corresponds to the per-generation signal-to-noise ratio crossing the detection floor: below $\alpha_c$, each episode's signal is too faint for the Granger test to distinguish from noise at $T{=}11$, regardless of how many episodes accumulate.
338	This overturns the implicit assumption in data poisoning research that detection difficulty scales with total contamination; our results show that two training runs with nearly identical cumulative exposure ($99.75\%$ vs.\ $99.90\%$) produce categorically different detection outcomes.
339	
340	\paragraph{Statistical power interpretation.}
341	The $S \times R$ framework admits a formal statistical grounding: the detection phase transition at $\alpha_c$ corresponds to a \emph{power threshold} rather than a physical phase transition.
342	Under a permutation test framework, detection power scales as $\mathrm{Power}(\alpha, T) = \Phi\bigl(S(\alpha) \cdot R(\alpha) \cdot \sqrt{T} \,/\, \sigma_{\mathrm{noise}}\bigr)$, where $\Phi$ is the standard normal CDF.
343	When $S(\alpha) \cdot R(\alpha) \cdot \sqrt{T}$ first exceeds the detection threshold, power rises sharply from near-zero to near-one, producing the sigmoid-like onset observed empirically.
344	This formalization generates three testable predictions for longer generation chains ($T{=}20$, currently running):
345	(i)~$\alpha_c$ should \emph{left-shift} (increased $T$ raises power at all $\alpha$, lowering the detection threshold);
346	(ii)~the transition should \emph{smooth} ($\sqrt{T}$ scaling broadens the power curve, making onset less step-like); and
347	(iii)~different methods should exhibit \emph{different} $\alpha_c$ values (each method has its own power curve, so PermG and MMCT weighted consensus may cross the detection threshold at different $\alpha$).
348	Prediction~(iii) remains a theoretical consequence awaiting empirical validation from $T{=}20$ replication; at $T{=}10$, sub-threshold PermG $p$-values at $\alpha{=}0.45$ (FDR $p{=}0.059$--$0.091$; \S\ref{sec:regime}) are consistent with proximity to the power boundary but do not yet demonstrate method-dependent $\alpha_c$.
349	
350	\paragraph{Connection to effective rank and detection layers.}
351	The link between entropy and diversity can be made more concrete through effective rank~\cite{roy2007effective}: $\mathrm{erank}(P) = \exp(H(P / \|P\|_1))$ measures the number of dimensions carrying substantial probability mass.
352	A decline in $H$ contracts $\mathrm{erank}(P)$, pushing tail tokens below $\tau_n$ and eliminating the $n$-grams they participate in.
353	This yields a mechanistic chain---$H$ decreases $\to$ $\mathrm{erank}$ contracts $\to$ tail probabilities cross $\tau_n$ $\to$ $D_k^{(g)}$ drops---in which entropy responds first.
354	This chain mediates the temporal resolution factor $R(\alpha)$: at intermediate $\alpha$ (${\approx}0.60$), relaxation time matching compresses the erank-mediated cascade into a single generation ($R \to 0$); at higher $\alpha$, the severity of entropy collapse outpaces the cascade, restoring the generational offset ($R$ large; \S\ref{sec:regime}).
355	
356	Effective rank is a \emph{distributional dimensionality} indicator---it detects contraction of the distribution's effective degrees of freedom---and is conceptually distinct from both distributional instability (variance inflation) and classical critical slowing down (CSD) indicators (rising autocorrelation) that characterize dynamical stability near tipping points~\cite{scheffer2009early,dakos2012methods}.
357	These layers, together with the causal coupling layer captured by Granger-type tests, form four complementary detection channels ordered by onset threshold (\S\ref{sec:discussion}).
358	The distinction matters because the layers can diverge: \citet{truong2025entropy} show that entropy collapse can be a first-order phase transition under convex feedback dynamics, in which CSD indicators remain bounded before the critical point and provide no advance warning.
359	In such regimes, distributional dimensionality may register contraction before dynamical indicators respond---or, as our experiments show (\S\ref{sec:case_study}), may fail entirely in an architecture-dependent manner.
360	
361	\paragraph{Phase transition theory and the onset boundary.}
362	The onset at $\alpha{\approx}0.50$---quantified empirically as $\alpha_c{=}0.476$ via sigmoid regression (\S\ref{sec:regime})---may reflect a critical mixing threshold analogous to the scaling law of \citet{gu2024cmr} for continual pre-training, and resonates with the finding of \citet{gu2025datamixing} that data mixing itself can induce phase transitions in knowledge acquisition.
363	The non-monotonic dip at $\alpha{=}0.60$ (\S\ref{sec:regime}) is consistent with the two universality classes of \citet{truong2025entropy}: if the transition is first-order (Class~1, irreversible, exponent $\nu{=}1$), the abrupt simultaneous shift in canary and downstream metrics suppresses the temporal lead that Granger tests exploit, while smoother second-order dynamics (Class~2, reversible, $\nu{=}1/2$) at neighboring $\alpha$ values preserve it.
364	These connections are speculative and require finer $\alpha$ resolution and direct estimation of feedback nonlinearity to validate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "90dba807-4683-4f3a-ad05-5664e3098b57",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nThe experiments in \\S\\ref{sec:method_sensitivity}--\\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.\nThis section distills three methodological pitfalls (\\S\\ref{sec:pitfalls}), proposes a multi-method consensus framework to quantify their impact and identify the most reliable individual method (\\S\\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\\S\\ref{sec:calibration}).\n\n\n\\subsection{Methodological Pitfalls in Lead-Lag Analysis}\n\\label{sec:pitfalls}\n\nWe identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.\nEach is documented below with representative data from our experiments; full results appear in \\S\\ref{sec:experiments}.\n\n\\paragraph{Pitfall 1: Method sensitivity.}\nApplied to the same data ($\\alpha{=}1.0$, 4~seeds, 16 canary$\\to$downstream pairs: 4 candidate canaries $\\times$ 4 downstream metrics, including candidates later excluded per \\S\\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 37.5\\% (permutation Granger), with Toda--Yamamoto achieving moderate rates (3--4/8 at $\\alpha{\\geq}0.50$); inter-method agreement is Cohen's $\\kappa{=}0.185$, indicating poor agreement (\\S\\ref{sec:method_sensitivity}).\nThe spurious-signal rate (the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative) is at least 62.5\\% across the primary methods.\nThis pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.\nIn a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.\n\n\\paragraph{Pitfall 2: Spurious regression under shared trends.}\nA single preprocessing decision, first-differencing to remove shared non-stationary trends~\\cite{granger1974spurious}, can eliminate an entire analysis channel.\nAt $\\alpha{=}1.0$, canary$\\to$perplexity pairs appear near-universally significant in undifferenced analysis ($F{=}16$--$36$) but yield $F{\\approx}0$, $p{=}0.99$ after differencing (Figure~\\ref{fig:differencing_dmax}a; \\S\\ref{sec:method_sensitivity}).\nIn contrast, canary$\\to$diversity pairs retain unanimous FDR significance after differencing (24/24$\\to$24/24).\nWithout the differencing diagnostic, an analyst would conclude that canaries predict perplexity, a conclusion entirely driven by co-trending rather than temporal precedence.\nThe danger lies in the selective nature of this confound: only by applying the diagnostic can one determine which channels are genuine and which are artifacts of shared non-stationarity.\n\n\\paragraph{Pitfall 3: Regime dependence.}\nEven after fixing the statistical method, the contamination level~$\\alpha$ determines whether a lead-lag relationship is detectable.\nPermutation Granger tests (first-differenced, BH FDR-corrected at $q{=}0.05$) find 6/8 pairs FDR-significant at both $\\alpha{=}0.50$ (2~fp32 seeds, consistent) and $\\alpha{=}1.0$, but 0/8 through $\\alpha{=}0.45$ (\\S\\ref{sec:regime}).\nThe transition zone at $\\alpha{\\approx}0.45$--$0.50$ is where method divergence is most dangerous: correlation-based methods find significance across all levels while causal methods remain null through $\\alpha{=}0.45$ (a faint single-pair signal appears at $\\alpha{=}0.25$, FDR $p{=}0.053$, but does not reach aggregate detection), creating the maximum risk of spurious conclusions when only a single (liberal) method is used.\nThis regime dependence is consistent with theoretical expectations about signal-to-noise limits in short ecological time series \\cite{boettiger2012limits}, and suggests that detectability boundaries should be explicitly mapped rather than assumed.\n\n\n\\subsection{Multi-Method Consensus Framework}\n\\label{sec:consensus}\n\nThe pitfalls above motivate a multi-method consensus approach inspired by specification curve analysis \\cite{simonsohn2020specification} and multi-method validation in early-warning signal detection \\cite{scheffer2009early}: rather than relying on any single method, we apply multiple independent methods to quantify how analytic choices determine conclusions, using agreement thresholds as diagnostic benchmarks.\n\n\\paragraph{Formal definition.}\nGiven $M$ lead-lag detection methods $\\{m_1, \\ldots, m_M\\}$ and $N$ independent random seeds, a canary$\\to$downstream pair $(X, Y)$ is classified as \\textsc{robust} if and only if:\n\\begin{enumerate}\n    \\item At least $K$ of $M$ methods judge the pair FDR-significant, where each method independently applies Benjamini--Hochberg correction at $q{=}0.05$; and\n    \\item At least $S$ of $N$ seeds replicate this conclusion.\n\\end{enumerate}\nThe thresholds $(K, S)$ control the trade-off between false positive and false negative rates.\nMethods with different inductive biases (correlation-based methods that detect any temporal association versus Granger-type methods that test directional predictive improvement \\cite{granger1969investigating}) provide complementary evidence.\nTheir convergence on a given pair constitutes stronger evidence than agreement among methods sharing the same statistical assumptions.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality \\cite{shojaie2022granger}; our framework inherits this limitation.\n\n\\paragraph{Method tiering.}\nThe five methods are organized into two tiers based on empirical reliability.\nThree \\emph{primary} methods---naive cross-correlation, differenced cross-correlation, and permutation Granger causality---produce consistent results across independent analysis pipelines and exhibit adequate statistical power at $T{=}11$ generations.\nTwo methods are classified as \\emph{supplementary}: threshold onset detection due to power limitations at $T{=}11$ under corrected $3\\sigma$ calibration (\\S\\ref{sec:threshold_limitation}), and Toda--Yamamoto Granger causality, which achieves moderate detection (3--4/8 at $\\alpha{\\geq}0.50$) but with reduced power relative to the primary methods (\\S\\ref{sec:ty_limitation}).\nThe consensus panel thus comprises four contributing methods (three primary, one moderate supplementary), with threshold onset near-inoperative at $T{=}11$.\nThe consensus threshold $K{\\geq}3$ out of 5 methods requires agreement among at least the three primary methods or two primary methods plus TY, making $K{\\geq}3$ a \\emph{stronger} standard than a simple majority vote would suggest.\n\n\\paragraph{Sequential filtering pipeline.}\nIn practice, the $K$-of-$M$ voting operates over all five methods applied independently to each pair; the sequential pipeline below describes the order in which results are examined, enabling early termination and interpretable diagnostics at each stage (Figure~\\ref{fig:consensus_workflow}):\n\\begin{enumerate}\n    \\item \\textbf{Naive correlation scan.} Cross-correlation at maximum lag~5 with BH correction serves as a permissive baseline; all pairs with any temporal association pass.\n    \\item \\textbf{First-differencing diagnostic.} Cross-correlation is recomputed on first-differenced series, testing whether temporal associations survive removal of shared linear trends. Pairs that lose significance are flagged as potential spurious regressions.\n    \\item \\textbf{Permutation Granger causality.} Permutation-based Granger causality tests \\cite{shojaie2022granger} on first-differenced series (5{,}000 permutations, BH correction at $q{=}0.05$) assess directional predictive improvement: whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history.\n    \\item \\textbf{Multi-seed replication.} The conclusion must hold across $S$ of $N$ independent training seeds, filtering seed-specific artifacts.\n\\end{enumerate}\nAt $\\alpha{=}1.0$, this pipeline progressively filters: 16 pairs pass Stage~1, 14 survive Stage~2 (differencing removes 2 marginal canary$\\to$perplexity pairs), 6 survive Stage~3 (Granger testing eliminates remaining canary$\\to$perplexity pairs and failed canary candidates), and all~6 survive Stage~4 (multi-seed replication confirms all Granger-significant pairs).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/consensus_workflow.pdf}\n\\caption{Sequential filtering pipeline of the multi-method consensus framework. Starting from all candidate canary$\\to$downstream pairs, the pipeline applies four stages: (1)~naive cross-correlation scan (permissive baseline), (2)~first-differencing diagnostic (removes shared-trend artifacts), (3)~permutation Granger causality (tests directional predictive improvement), and (4)~multi-seed replication (filters seed-specific artifacts). At $\\alpha{=}1.0$ (Pythia-410M), the pipeline reduces 16 candidate pairs to 6 robust pairs: 16$\\to$14$\\to$6$\\to$6. The $K$-of-$M$ consensus vote operates in parallel across all five methods; the sequential ordering provides interpretable diagnostics at each stage.}\n\\label{fig:consensus_workflow}\n\\end{figure}\n\n\\paragraph{Practical guidance.}\nThe consensus thresholds $(K, S)$ should be chosen to match the analyst's tolerance for false positives versus false negatives.\nTable~\\ref{tab:practical_guidance} provides four recommended tiers, calibrated against our experimental controls (\\S\\ref{sec:calibration}).\nTier~3 ($K{\\geq}4/5$, $S{\\geq}3/4$) achieves the best trade-off under the full 5-method panel: zero false positives while recovering all six reference pairs; however, threshold onset's near-zero power at $3\\sigma$ (\\S\\ref{sec:threshold_limitation}) makes it near-inoperative, and Toda--Yamamoto provides moderate supplementary signal (3--4/8 at $\\alpha{\\geq}0.50$; \\S\\ref{sec:ty_limitation}), making $K{\\geq}3$ the operationally relevant consensus threshold.\nWith four contributing methods (three primary plus TY), $K{\\geq}3$ draws on a broader evidence base than the three primary methods alone; TY's moderate detection at $\\alpha{\\geq}0.50$ strengthens consensus conclusions where it contributes a positive vote.\nCross-architecture validation confirms $K{\\geq}3$ reaches ${\\geq}6/8$ in 10 of 14 architecture-seed combinations (\\S\\ref{sec:generalization}).\nMethod subset ablation confirms that this threshold is uniquely optimal: at $K{=}3/5$, the null-control FPR is 37.5\\% (unacceptable); at $K{=}4/5$, FPR drops to 0\\% while retaining 6/6 reference-pair sensitivity; at $K{=}5/5$, FPR remains 0\\% but sensitivity falls to 3/6.\nShapley value analysis (exact enumeration of all 32 coalitions; Figure~\\ref{fig:shapley}) identifies naive cross-correlation as the sole positive contributor to FPR (Shapley(FPR)${=}{+}0.348$) and permutation Granger as the strongest FPR suppressor (Shapley(FPR)${=}{-}0.194$), the only method combining 0\\% null-control FPR with high sensitivity.\nToda--Yamamoto's Shapley contribution (FNR${=}{-}0.158$) reflects moderate supplementary value: it reduces consensus FNR without introducing false positives (\\S\\ref{sec:ty_limitation}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/shapley_method_contribution.pdf}\n\\caption{Shapley value decomposition of method contributions to consensus FPR and FNR (exact enumeration of all $2^5{=}32$ coalitions, $K{=}\\max(1,|S|{-}1)$). FPR is computed at $\\alpha{=}0.0$ (3~seeds $\\times$ 8~pairs${=}$24 observations); FNR at $\\alpha{=}1.0$ (4~seeds, 6 reference pairs). Naive cross-correlation is the only positive FPR contributor (${+}0.348$); permutation Granger is the strongest FPR suppressor (${-}0.194$). Toda--Yamamoto contributes moderate FNR suppression (Shapley FNR${=}{-}0.158$) as a supplementary method (\\S\\ref{sec:ty_limitation}).}\n\\label{fig:shapley}\n\\end{figure}\nTier~4 requires unanimity across methods and seeds, which incurs elevated false negative rates; TY's moderate detection (3--4/8) means that requiring $5/5$ unanimity is substantially more restrictive than $4/5$, particularly at intermediate contamination levels where TY may not contribute a positive vote.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Practical guidance tiers for lead-lag consensus analysis. Tier~3 ($K{\\geq}4/5$, $S{\\geq}3/4$) is uniquely optimal under the full 5-method panel; with threshold onset power-limited (\\S\\ref{sec:threshold_limitation}) and Toda--Yamamoto providing moderate supplementary signal (\\S\\ref{sec:ty_limitation}), $K{\\geq}3$ draws on four contributing methods. FPR is calibrated at $\\alpha{=}0.0$ (null control, $M{=}5$ methods, $N{=}3$ seeds, Pythia-410M). FNR is calibrated at $\\alpha{=}1.0$ against 6 effect-size reference pairs using a 4-method panel (excluding differenced cross-correlation); $N{=}4$ seeds (\\S\\ref{sec:calibration}).}\n\\label{tab:practical_guidance}\n\\begin{tabular}{llcccc}\n\\toprule\nTier & Use Case & $K/M$ & $S/N$ & FPR & FNR \\\\\n\\midrule\n1 & Exploratory     & ${\\geq}1/5$ & ${\\geq}1/N$ & 100\\%  & 0\\%    \\\\\n2 & Screening       & ${\\geq}3/5$ & ${\\geq}2/N$ & 37.5\\% & 0\\%    \\\\\n3 & Confirmatory    & ${\\geq}4/5$ & ${\\geq}3/N$ & 0\\%    & 0\\%    \\\\\n4 & Conservative    & $5/5$       & $N/N$        & 0\\%    & 50\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Empirical Calibration}\n\\label{sec:calibration}\n\nWe calibrate the framework using two built-in experimental controls.\nFull numerical results are reported in Table~\\ref{tab:fpr_fnr}.\n\n\\paragraph{False positive rate.}\nThe $\\alpha{=}0.0$ condition serves as a null control: no synthetic data is injected, so any detected lead-lag association is a false positive.\nAt $K{=}1$ (any single method suffices), FPR${=}$75\\%: naive cross-correlation flags 6/8 forward-direction pairs.\nAt $K{=}2$, FPR drops to ${\\leq}$37.5\\%; at $K{=}3$, to ${\\leq}$12.5\\%; and at $K{\\geq}4$, FPR${=}$0\\%.\nThe consensus framework at Tier~3 matches the false positive performance of the best individual method (permutation Granger, 0\\%) while providing robustness against miscalibration of any single method.\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$ with 4~seeds, we define six \\emph{effect-size reference pairs} using criteria independent of the consensus methods:\n\\begin{enumerate}\n    \\item[(a)] The canary$\\to$downstream drift ratio at $\\alpha{=}1.0$ must exceed $3\\times$ the $\\alpha{=}0.0$ baseline drift (canary ratios: entropy $11.93\\times$, ECE $73.12\\times$, both far above threshold); and\n    \\item[(b)] Canary onset must strictly precede downstream onset by at least one generation (canary onset: generation~1; diversity onset: generations~3--9).\n\\end{enumerate}\nThese criteria yield token entropy and ECE each predicting distinct-1, distinct-2, and distinct-3~\\cite{li2016diversity}.\nThe perplexity channel is excluded because its onset (generation~1) coincides with canary onset, consistent with, but not derived from, the differencing diagnostic finding that canary$\\to$perplexity associations are spurious (\\S\\ref{sec:method_sensitivity}).\nThe effect-size threshold is robust: at $2\\times$, $3\\times$, and $5\\times$ the baseline drift, the reference set remains identical (6~pairs), because canary ratios ($11.93\\times$ and $73.12\\times$) far exceed all thresholds.\n\nFNR is calibrated using a 4-method panel excluding differenced cross-correlation, which shares statistical properties with detrending-based criteria and could introduce circularity.\nAt $K{\\geq}3/4$, $S{\\geq}3/4$, all six reference pairs are recovered (FNR${=}$0\\%).\nAt $K{=}4/4$, $S{=}4/4$, FNR rises to 50\\%, reflecting TY's moderate detection power (4/8 at $\\alpha{=}1.0$; \\S\\ref{sec:ty_limitation}).\n\n\\paragraph{Symmetric calibration.}\nBoth FPR and FNR are validated on the joint method${\\times}$seed dimension: FPR across 3~seeds at $\\alpha{=}0.0$ (0/24 pairs at $K{\\geq}3$, $3\\sigma$) and FNR across 4~seeds at $\\alpha{=}1.0$ (6/6 reference pairs recovered at $K{\\geq}3/4$, $S{\\geq}3/4$).\nCross-seed FPR variance is negligible: all three null-control seeds yield 0/8 robust pairs at $K{\\geq}3$ ($3\\sigma$), confirming seed-independent performance.\n\n\n\\paragraph{Threshold onset detection: power limitations at $3\\sigma$.}\n\\label{sec:threshold_limitation}\nPost-hoc validation of the threshold onset implementation (M028) revealed that the published $2\\sigma$ calibration was mislabeled as $3\\sigma$.\nUnder corrected $3\\sigma$ calibration, threshold onset yields 0/8 significant pairs in 8 of 12 cross-architecture conditions (Table~\\ref{tab:generalization}) and at most 2/8 in the remainder, reducing it to a near-zero-power method at $T{=}11$ generations; any threshold onset detections should therefore be interpreted as lower-bound estimates.\nThis low power is expected: with only 10 generation-over-generation differences, the null variance estimate has few degrees of freedom, and a $3\\sigma$ exceedance threshold becomes overly conservative.\nWe retain threshold onset as a supplementary method for completeness and report its results transparently, but adopt permutation Granger forward significance as the primary detection indicator in cross-architecture analyses.\n\n\\paragraph{Toda--Yamamoto Granger: moderate supplementary signal.}\n\\label{sec:ty_limitation}\nPost-hoc analysis identified a statsmodels API incompatibility that initially produced artificially low Toda--Yamamoto detection rates.\nAfter correcting the implementation, TY achieves moderate detection: 3/8 forward-direction pairs at $\\alpha{=}0.50$ (seed~42), 3/8 at $\\alpha{=}0.75$, and 4/8 at $\\alpha{=}1.0$ (Table~\\ref{tab:method_comparison}).\nThese rates are lower than permutation Granger (6--8/8) but confirm that TY captures genuine signal at $\\alpha{\\geq}0.50$, consistent with the method's theoretical motivation~\\cite{toda1995statistical}.\nTY is classified as a moderate supplementary method: it contributes to the consensus panel but does not serve as a primary detection indicator due to reduced statistical power at $T{=}11$ (the augmentation order $d_{\\max}$ consumes additional degrees of freedom) and sensitivity to the $d_{\\max}$ hyperparameter (Figure~\\ref{fig:differencing_dmax}b).\nWith TY providing moderate signal, the consensus panel comprises four contributing methods (three primary plus TY as supplementary), strengthening the $K{\\geq}3$ threshold: at $\\alpha{=}0.50$ (seed~42), $K{\\geq}3$ rises from 5/8 to 6/8 with TY's corrected contribution.\nAt $\\alpha{\\geq}0.50$, $K{\\geq}4$ consensus (4 of 5 methods agree) emerges in 3/8 pairs, demonstrating that multi-method agreement extends beyond the primary trio.\n\n\\subsection{Multi-Method Consensus Test (MMCT)}\n\\label{sec:mmct}\n\nThe uniform threshold ($K{\\geq}4/5$) achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes (\\S\\ref{sec:calibration}), but this ad-hoc threshold lacks formal statistical grounding: null-calibrated permutation testing assigns $p{=}0.16$ to $K{\\geq}4/5$, failing to reach significance at conventional levels.\nThe threshold also treats all methods equally, despite the heterogeneous error profiles documented in \\S\\ref{sec:pitfalls}: naive cross-correlation has 75\\% forward-direction null-control FPR while permutation Granger has 0\\%.\nWe formalize the \\emph{Multi-Method Consensus Test} (MMCT), a weighted consensus framework that assigns each method influence proportional to its empirical specificity, following the specification curve tradition~\\cite{simonsohn2020specification} in which analytical choices are systematically varied and aggregated rather than arbitrarily fixed~\\cite{bell2022modeling}.\nMMCT serves as an evaluation framework rather than an end in itself: its primary function is to enable systematic comparison of detection methods under controlled conditions, identifying which individual methods are reliable and why others fail.\nWe do not claim a novel statistical method; MMCT is a consensus testing protocol adapted to the specific constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.\n\n\\paragraph{FPR-inverse weighting.}\nLet $\\hat{\\text{FPR}}_k$ denote the empirical false positive rate of method $m_k$, estimated from $N_0$ null-control observations at $\\alpha{=}0.0$ across $S$ seeds.\nEach method receives weight\n\\begin{equation}\n    w_k = \\frac{1}{\\max(\\hat{\\text{FPR}}_k,\\; \\epsilon)},\n    \\label{eq:fpr_weight}\n\\end{equation}\nwhere $\\epsilon{=}0.01$ prevents division by zero.\nMethods with low FPR (e.g., permutation Granger at 0\\%, receiving $w_k{=}100$) dominate the consensus; methods with high FPR (e.g., naive cross-correlation at 75\\%, receiving $w_k{\\approx}1.3$) are effectively downweighted.\n\n\\paragraph{Consensus score.}\nGiven $M$ methods that return binary decisions $d_k \\in \\{0, 1\\}$ (FDR-significant or not) for a candidate pair $(X, Y)$, the weighted consensus score is:\n\\begin{equation}\n    W(X \\to Y) = \\frac{\\sum_{k=1}^{M} w_k \\cdot d_k}{\\sum_{k=1}^{M} w_k}.\n    \\label{eq:consensus_score}\n\\end{equation}\nWhen all weights equal~1 (uniform mode), $W$ reduces to $K/M$, and thresholding at $W \\geq 4/5$ recovers the uniform $K{\\geq}4$ rule exactly.\n\n\\paragraph{Statistical testing.}\nThe null distribution of $W$ is estimated from the $\\alpha{=}0.0$ control condition, where no synthetic contamination is present and any detected lead-lag association is a false positive.\nThe $N_0$ null-control pairs yield a reference distribution $\\{W_0^{(j)}\\}_{j=1}^{N_0}$, and the MMCT $p$-value is:\n\\begin{equation}\n    p_{\\text{MMCT}} = \\frac{|\\{j : W_0^{(j)} \\geq W_{\\text{obs}}\\}|}{N_0}.\n    \\label{eq:pvalue}\n\\end{equation}\nWe reject the null of no lead-lag relationship at significance level $\\alpha_{\\text{test}}$.\n\n\\paragraph{Bidirectional filtering.}\nMMCT tests both directions independently: $W(X \\to Y)$ and $W(Y \\to X)$.\nA stricter bidirectional mode requires forward significance with reverse non-significance.\nEmpirically, bidirectional and forward-only detection rates are identical across all contamination levels tested, indicating that pairs reaching weighted consensus in the forward direction consistently fail to reach consensus in reverse.\nWe therefore adopt forward-only (weighted pair forward) as the default MMCT configuration.\nAlgorithm~\\ref{alg:mmct} summarizes the procedure.\n\n\\begin{algorithm}[t]\n\\caption{Multi-Method Consensus Test (MMCT)}\n\\label{alg:mmct}\n\\begin{algorithmic}[1]\n\\Require Methods $\\{m_1, \\ldots, m_M\\}$; pair $(X, Y)$; null pairs $\\{(X_0^{(j)}, Y_0^{(j)})\\}_{j=1}^{N_0}$; floor $\\epsilon$; level $\\alpha_{\\text{test}}$\n\\Ensure Decision $d$, score $W$, $p$-value\n\\Statex \\textbf{Phase 1: Estimate weights from null control}\n\\For{$k = 1, \\ldots, M$}\n    \\State $\\hat{\\mathrm{FPR}}_k \\gets$ null-control rejection rate of $m_k$\n    \\State $w_k \\gets 1 / \\max(\\hat{\\mathrm{FPR}}_k, \\epsilon)$\n\\EndFor\n\\Statex \\textbf{Phase 2: Compute weighted consensus}\n\\For{$k = 1, \\ldots, M$}\n    \\State $d_k \\gets m_k(X, Y)$ \\Comment{1 if FDR-significant}\n\\EndFor\n\\State $W \\gets \\sum_k w_k d_k \\;/\\; \\sum_k w_k$\n\\Statex \\textbf{Phase 3: Null-distribution $p$-value}\n\\For{$j = 1, \\ldots, N_0$}\n    \\State $W_0^{(j)} \\gets$ consensus score of $(X_0^{(j)}, Y_0^{(j)})$\n\\EndFor\n\\State $p \\gets |\\{j : W_0^{(j)} \\geq W\\}| / N_0$\n\\State \\Return $\\mathbb{1}[p < \\alpha_{\\text{test}}]$, $W$, $p$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Empirical comparison.}\nTable~\\ref{tab:mmct_ablation} compares per-method detection rates across contamination levels, revealing the systematic comparison that motivates our method recommendation.\nThe five methods exhibit sharply divergent dose-response profiles: naive cross-correlation maintains elevated FPR at the null (75\\%) but rises to 87.5\\% at $\\alpha{=}0.75$; differenced cross-correlation achieves zero null-control FPR but detects in both forward and reverse directions, failing to provide directional separation; threshold onset detects only at $\\alpha{=}0.50$ (50\\%) and returns to zero at $\\alpha{=}0.75$ under $3\\sigma$ calibration; Toda--Yamamoto achieves moderate detection at $\\alpha{\\geq}0.50$ (37.5\\%) with zero null-control FPR but lower sensitivity than permutation Granger.\nPermutation Granger alone provides the cleanest dose-response profile, with a sharp step function from 0/8 (blind spot, $\\alpha{\\leq}0.45$) to 6/8 (onset, $\\alpha{=}0.50$, dual-seed confirmed) and reliable detection at $\\alpha{\\geq}0.75$ (Table~\\ref{tab:method_comparison}; \\S\\ref{sec:regime}).\n\nPermutation Granger produces binary per-pair verdicts that yield a steep onset of detection: a faint signal at $\\alpha{=}0.25$ (best pair FDR $p{=}0.053$) that does not reach aggregate detection through $\\alpha{=}0.45$, then an abrupt jump to 6/8 at $\\alpha{=}0.50$ (fp32), with a non-monotonic dip at $\\alpha{=}0.60$ (s42: 3/8, s43: 0/8; dual-seed confirmed synchronous collapse zone; \\S\\ref{sec:regime}).\nThis step-function profile, combined with zero null-control FPR and Shapley FPR suppression of $-0.194$, identifies PermG as the recommended individual detection method.\nCross-architecture validation confirms PermG fwd ${\\geq}6/8$ in 13 of 15 conditions, with multi-method consensus ($K{\\geq}3$) reaching ${\\geq}6/8$ in 10 of 14 with known consensus (\\S\\ref{sec:generalization}).\nMMCT weighted consensus further captures graded detection strength even where individual methods remain below threshold, providing formal $p$-values that the uniform $K$-of-$M$ threshold lacks; however, the systematic comparison reveals that PermG alone provides comparable or superior detection to the full consensus framework at all contamination levels tested.\nWith TY contributing as a fourth method, full 5/5 consensus becomes achievable: at $\\alpha{=}0.50$ (seed~42), the ECE$\\to$distinct-3 pair reaches significance across all five methods, demonstrating that the consensus panel can converge unanimously even near the onset boundary when the canary--downstream coupling is strong.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-method forward-direction detection rates across contamination levels (Pythia-410M, seed~42, fp32). Each cell reports the fraction of 8 canary$\\to$downstream pairs reaching BH-corrected significance ($q{=}0.05$). Per-method dose-response reveals the systematic comparison that identifies PermG as the recommended method (\\S\\ref{sec:case_study}). Cross-condition results at $\\alpha{=}1.0$ are reported in Table~\\ref{tab:mmct_cross}. $^\\dagger$Moderate supplementary method (\\S\\ref{sec:ty_limitation}); FPR$_\\text{null}$ pending (null condition not yet run through corrected pipeline).}\n\\label{tab:mmct_ablation}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & FPR$_\\text{null}$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ \\\\\n\\midrule\nNaive XCorr              & 75   & 12.5 & 37.5 & 87.5 \\\\\nDiff.\\ XCorr             & 0    & 37.5 & 87.5 & 75   \\\\\nThreshold ($3\\sigma$)    & ---  & 0    & 50   & 0    \\\\\nPerm.\\ Granger           & 0    & 0    & 75   & 75   \\\\\nToda--Yamamoto$^\\dagger$ & ---  & 0    & 37.5 & 37.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Backward compatibility.}\nSetting all weights $w_k{=}1$ reduces MMCT to the uniform $K$-of-$M$ threshold, making the existing consensus framework (\\S\\ref{sec:consensus}) a special case.\nDescriptively, $K{\\geq}4/5$ achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes (\\S\\ref{sec:calibration}); however, null-calibrated testing assigns $p{=}0.16$ to this threshold, indicating that it does not reach conventional significance levels.\nMMCT weighted consensus resolves this gap by providing formal $p$-values (Eq.~\\ref{eq:pvalue}) grounded in the empirical null distribution.\n\n\\paragraph{Cross-condition stability.}\nTable~\\ref{tab:mmct_cross} reports MMCT weighted consensus across all seven experimental conditions at $\\alpha{=}1.0$.\nDetection ranges from 4/8 to 8/8 while FPR remains 0 at the null control across all conditions, confirming that FPR-inverse weighting generalizes beyond the calibration setup.\nGPT-2-medium achieves the highest detection rate (8/8), consistent with its stronger per-method signal, demonstrating that MMCT's FPR-inverse weighting extracts graded detection strength that binary per-method verdicts miss.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{MMCT weighted forward consensus across experimental conditions ($\\alpha{=}1.0$, FPR-inverse weighting). Each cell reports significant canary$\\to$downstream pairs out of 8 (2~canaries $\\times$ 4~downstream metrics). All conditions maintain FPR${=}$0 at $\\alpha{=}0.0$. Values may be updated pending parameter consistency verification.}\n\\label{tab:mmct_cross}\n\\begin{tabular}{lc}\n\\toprule\nCondition & Sig / 8 \\\\\n\\midrule\nBaseline (Pythia-410M / Wiki)     & 5/8 \\\\\nArchitecture: GPT-2-medium / Wiki & \\textbf{8/8} \\\\\nArchitecture: OPT-1.3B / Wiki     & 5/8 \\\\\nScale: Pythia-1.4B / Wiki (s42)   & 4/8 \\\\\nScale: Pythia-1.4B / Wiki (s43)   & 4/8 \\\\\nDomain: Pythia-1B / C4 (s42)      & 5/8 \\\\\nDomain: Pythia-1B / C4 (s43)      & 4/8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Theoretical Motivation: Why Entropy Leads Diversity}\n\\label{sec:theory}\n\nThe empirical lead-lag relationship between token entropy and lexical diversity (\\S\\ref{sec:regime}) admits a simple theoretical motivation grounded in the distinct mathematical properties of continuous and discrete summary statistics.\nWe present three arguments that, taken together, predict the observed temporal ordering and its dependence on contamination strength.\nThese arguments provide intuition rather than formal proof; the dose-response experiments in \\S\\ref{sec:regime} test the resulting predictions empirically.\n\n\\paragraph{Continuous versus discrete response.}\nToken entropy $H(p_t^{(g)}) = -\\sum_v p_v \\log p_v$ is a continuous functional of the token distribution $p_t^{(g)}$ at generation $g$: any infinitesimal shift in $p_t^{(g)}$ produces a proportional change in $H$.\nDistinct-$n$ diversity $D_k^{(g)}$, by contrast, is a counting statistic.\nAn $n$-gram contributes to $D_k^{(g)}$ only when its probability exceeds an effective sampling threshold $\\tau_n \\approx 1/N$, where $N$ is the number of generated tokens.\nBelow $\\tau_n$, the $n$-gram is absent from finite samples regardless of its true probability.\n$D_k^{(g)}$ therefore responds to distributional change in discrete steps: it remains constant while probabilities drift within the interval above $\\tau_n$, then drops abruptly when a probability crosses the threshold.\nBecause $H$ tracks every distributional perturbation while $D_k^{(g)}$ remains silent until a threshold crossing occurs, entropy is sensitive to distributional change strictly before diversity registers it.\n\n\\paragraph{Predicted detectability regimes.}\nThe continuous-versus-discrete asymmetry determines not just the ordering of responses but the \\emph{detectability} of their temporal offset.\nWe model Granger-type detectability as the product of two competing factors:\n\\begin{equation}\n    \\text{Detectability}(\\alpha) \\;\\propto\\; S(\\alpha) \\times R(\\alpha),\n    \\label{eq:detectability}\n\\end{equation}\nwhere $S(\\alpha)$ is the \\emph{signal strength} (the magnitude of distributional shift induced by contamination) and $R(\\alpha)$ is the \\emph{temporal resolution} (the generational gap between the entropy response and the diversity response).\n\n$S(\\alpha)$ increases monotonically with $\\alpha$: more synthetic data induces larger distributional shifts.\n$R(\\alpha)$, by contrast, is non-monotonic.\nAt low $\\alpha$, entropy and diversity respond in different generations ($R$ large); at a critical intermediate $\\alpha$, \\emph{relaxation time matching} occurs---the perturbation strength aligns the entropy and diversity relaxation times so that both metrics shift within the same generation, driving $R \\to 0$.\nAt high $\\alpha$, the perturbation is severe enough that entropy collapses within generation~0$\\to$1 (the continuous-functional advantage saturates immediately), while diversity still requires generation~1$\\to$2 to fully manifest the loss---tail $n$-grams near $\\tau_n$ persist temporarily before crossing the threshold---and the one-generation lead recovers ($R$ large again).\n\nThe competition between $S$ and $R$ predicts four regimes:\n\\begin{enumerate}\n\\item \\textbf{Blind} ($\\alpha \\leq 0.45$).\n$S$ falls below the detection floor; $S \\times R \\approx 0$ regardless of $R$.\n\\item \\textbf{Onset} ($\\alpha \\approx 0.50$).\n$S$ crosses the detection threshold while $R$ remains high (entropy leads diversity by a full generation); $S \\times R$ is sufficient for detection.\nBetween the blind and onset regimes, the framework predicts a \\emph{canary-only window} in which entropy shifts detectably but no $n$-grams have yet crossed $\\tau_n$; we lack the $\\alpha$ resolution to confirm this (our grid jumps from $0.25$ to $0.50$) and leave verification to future work with finer spacing in $[0.10, 0.45]$.\n\\item \\textbf{Synchronous dip} ($\\alpha \\approx 0.60$).\n$S$ continues increasing, but $R$ drops sharply: relaxation time matching at this $\\alpha$ compresses the entropy--diversity lag to near zero, producing a local minimum in $S \\times R$.\n\\item \\textbf{Detection} ($\\alpha \\geq 0.75$).\n$S$ grows large enough to dominate the product despite reduced $R$; the continuous-functional advantage reasserts across generations, and $S \\times R$ recovers.\n\\end{enumerate}\nThese four regimes align with the empirical dose-response (\\S\\ref{sec:regime}): blind at $\\alpha{\\leq}0.45$ (PermG 0/8), onset at $\\alpha{=}0.50$ (6/8, dual-seed), synchronous dip at $\\alpha{=}0.60$ (0--3/8, dual-seed), and detection at $\\alpha{\\geq}0.75$ (5--6/8 per seed, three seeds; 6/8 per seed at $\\alpha{=}1.0$, four seeds).\nThe non-monotonic profile is a prediction of the $S \\times R$ framework, not an anomaly requiring post-hoc explanation; indeed, non-monotonic dose-response curves are well-documented across disciplines.\nThe four-regime profile mirrors the hormetic dose-response in toxicology, where intermediate doses produce qualitatively different effects from both low and high doses~\\cite{calabrese2003hormesis}.\nThe temporal resolution collapse at intermediate $\\alpha$ ($R \\to 0$) corresponds to the known failure of Granger-type tests under contemporaneous coupling~\\cite{deshpande2010instantaneous}: when entropy and diversity shift within the same generation (lag${=}0$), the causal test loses statistical power by construction, not by methodological deficiency.\nThe detection dip is also consistent with critical speeding-up phenomena in ecological regime shifts, where early-warning indicators exhibit non-monotonic behavior near phase boundaries rather than the monotonic rise predicted by classical critical slowing down~\\cite{titus2020speeding}.\nWe emphasize that the $S \\times R$ model provides qualitative intuition, not quantitative derivation; the regime boundaries depend on model capacity, dataset properties, and sample size $N$.\n\n\\paragraph{Detection threshold vs.\\ accumulated contamination.}\nThe detection phase transition at $\\alpha_c{=}0.476$ (\\S\\ref{sec:regime}) reveals that Granger detectability depends on the \\emph{per-generation} mixing ratio $\\alpha$, not on cumulative contamination.\nAfter $G{=}10$ generations, cumulative synthetic fraction reaches $C(\\alpha, G) = 1 - (1{-}\\alpha)^G$: at $\\alpha{=}0.45$, $C = 99.75\\%$; at $\\alpha{=}0.50$, $C = 99.90\\%$---a difference of 0.15 percentage points---yet PermG detection jumps from 0/8 to 6/8.\nThe explanation lies in the per-generation signal.\nPermG detects temporal lead-lag from the time series of inter-generation entropy shifts $\\{\\Delta h^{(g)}\\}_{g=1}^G$, where $\\Delta h^{(g)} \\propto \\alpha \\cdot d_{\\mathrm{TV}}(p_g^{\\mathrm{model}}, p^{\\mathrm{real}})$ captures the per-episode perturbation scaled by the distributional gap at generation~$g$.\nThe critical threshold $\\alpha_c$ corresponds to the per-generation signal-to-noise ratio crossing the detection floor: below $\\alpha_c$, each episode's signal is too faint for the Granger test to distinguish from noise at $T{=}11$, regardless of how many episodes accumulate.\nThis overturns the implicit assumption in data poisoning research that detection difficulty scales with total contamination; our results show that two training runs with nearly identical cumulative exposure ($99.75\\%$ vs.\\ $99.90\\%$) produce categorically different detection outcomes.\n\n\\paragraph{Statistical power interpretation.}\nThe $S \\times R$ framework admits a formal statistical grounding: the detection phase transition at $\\alpha_c$ corresponds to a \\emph{power threshold} rather than a physical phase transition.\nUnder a permutation test framework, detection power scales as $\\mathrm{Power}(\\alpha, T) = \\Phi\\bigl(S(\\alpha) \\cdot R(\\alpha) \\cdot \\sqrt{T} \\,/\\, \\sigma_{\\mathrm{noise}}\\bigr)$, where $\\Phi$ is the standard normal CDF.\nWhen $S(\\alpha) \\cdot R(\\alpha) \\cdot \\sqrt{T}$ first exceeds the detection threshold, power rises sharply from near-zero to near-one, producing the sigmoid-like onset observed empirically.\nThis formalization generates three testable predictions for longer generation chains ($T{=}20$, currently running):\n(i)~$\\alpha_c$ should \\emph{left-shift} (increased $T$ raises power at all $\\alpha$, lowering the detection threshold);\n(ii)~the transition should \\emph{smooth} ($\\sqrt{T}$ scaling broadens the power curve, making onset less step-like); and\n(iii)~different methods should exhibit \\emph{different} $\\alpha_c$ values (each method has its own power curve, so PermG and MMCT weighted consensus may cross the detection threshold at different $\\alpha$).\nPrediction~(iii) remains a theoretical consequence awaiting empirical validation from $T{=}20$ replication; at $T{=}10$, sub-threshold PermG $p$-values at $\\alpha{=}0.45$ (FDR $p{=}0.059$--$0.091$; \\S\\ref{sec:regime}) are consistent with proximity to the power boundary but do not yet demonstrate method-dependent $\\alpha_c$.\n\n\\paragraph{Connection to effective rank and detection layers.}\nThe link between entropy and diversity can be made more concrete through effective rank~\\cite{roy2007effective}: $\\mathrm{erank}(P) = \\exp(H(P / \\|P\\|_1))$ measures the number of dimensions carrying substantial probability mass.\nA decline in $H$ contracts $\\mathrm{erank}(P)$, pushing tail tokens below $\\tau_n$ and eliminating the $n$-grams they participate in.\nThis yields a mechanistic chain---$H$ decreases $\\to$ $\\mathrm{erank}$ contracts $\\to$ tail probabilities cross $\\tau_n$ $\\to$ $D_k^{(g)}$ drops---in which entropy responds first.\nThis chain mediates the temporal resolution factor $R(\\alpha)$: at intermediate $\\alpha$ (${\\approx}0.60$), relaxation time matching compresses the erank-mediated cascade into a single generation ($R \\to 0$); at higher $\\alpha$, the severity of entropy collapse outpaces the cascade, restoring the generational offset ($R$ large; \\S\\ref{sec:regime}).\n\nEffective rank is a \\emph{distributional dimensionality} indicator---it detects contraction of the distribution's effective degrees of freedom---and is conceptually distinct from both distributional instability (variance inflation) and classical critical slowing down (CSD) indicators (rising autocorrelation) that characterize dynamical stability near tipping points~\\cite{scheffer2009early,dakos2012methods}.\nThese layers, together with the causal coupling layer captured by Granger-type tests, form four complementary detection channels ordered by onset threshold (\\S\\ref{sec:discussion}).\nThe distinction matters because the layers can diverge: \\citet{truong2025entropy} show that entropy collapse can be a first-order phase transition under convex feedback dynamics, in which CSD indicators remain bounded before the critical point and provide no advance warning.\nIn such regimes, distributional dimensionality may register contraction before dynamical indicators respond---or, as our experiments show (\\S\\ref{sec:case_study}), may fail entirely in an architecture-dependent manner.\n\n\\paragraph{Phase transition theory and the onset boundary.}\nThe onset at $\\alpha{\\approx}0.50$---quantified empirically as $\\alpha_c{=}0.476$ via sigmoid regression (\\S\\ref{sec:regime})---may reflect a critical mixing threshold analogous to the scaling law of \\citet{gu2024cmr} for continual pre-training, and resonates with the finding of \\citet{gu2025datamixing} that data mixing itself can induce phase transitions in knowledge acquisition.\nThe non-monotonic dip at $\\alpha{=}0.60$ (\\S\\ref{sec:regime}) is consistent with the two universality classes of \\citet{truong2025entropy}: if the transition is first-order (Class~1, irreversible, exponent $\\nu{=}1$), the abrupt simultaneous shift in canary and downstream metrics suppresses the temporal lead that Granger tests exploit, while smoother second-order dynamics (Class~2, reversible, $\\nu{=}1/2$) at neighboring $\\alpha$ values preserve it.\nThese connections are speculative and require finer $\\alpha$ resolution and direct estimation of feedback nonlinearity to validate.",
      "numLines": 364,
      "startLine": 1,
      "totalLines": 364
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
Now I have both the paper writing norms and the current method.tex. Let me analyze the current content and write a compressed ~67 line version following all the constraints specified.

Key structural requirements:
1. Part 1: Method intro + Pitfalls (~10 lines)
2. Part 2: MMCT concept (~10 lines)
3. Part 3: Permutation Granger causality (~15 lines)
4. Part 4: S×R Framework subsection (~20 lines)
5. Part 5: Calibration (~10 lines)

Total: ~65-67 lines


Now I'm carefully drafting this, keeping all the active constraints in mind: the "steep onset" and "detection phase transition" language, making sure α_c is always qualified with "at T=10", using "consistent with" for Power Theory, excluding CSD data entirely, avoiding any TY=7/8 evidence, using only PermG for dose-response, positioning C2 correctly with the standard statistical power scaling language, and tracking the predict-then-verify sequence with α=0.45→0/8.

I need to ensure the reproducibility details are front and center in the main text: PermG with n_perm=5000, BH-FDR q=0.05, and the 8-pair design. I'm avoiding em-dashes, -ing clause endings, and those overused transition phrases, keeping paragraphs dense and every number purposeful. The cross-references will tie back to the regime section, dose-response section, and other key parts. Writing the Methods section... I'm weighting each method inversely by its false positive rate to create a consensus score, which identifies permutation Granger as the only approach achieving zero false positives on null controls while maintaining consistent detection across different contamination scenarios. Now I'm defining how permutation Granger tests whether past values of one metric improve predictions of another beyond that metric's own history.

Permutation Granger uses 5,000 permutations on differenced series with Benjamini-Hochberg correction across the validated metric pairs, and it stands out because it makes no distributional assumptions (crucial for short non-stationary data), tests directionality explicitly in both directions, and requires no hyperparameter tuning—whereas the other four methods each have specific weaknesses like naive cross-correlation's 75% false positive rate or differenced cross-correlation's inability to distinguish directional relationships.

The threshold-based approach struggles with power at small sample sizes, and Toda-Yamamoto gains only modest detection improvements while losing power from lag augmentation penalties. Now I'm setting up the Signal-Times-Resolution framework to analyze how detectability scales with signal strength and temporal resolution under the permutation Granger approach. ability}
\end{equation}
where $S(\alpha)$ is signal strength (magnitude of distributional shift, monotonically increasing with contamination fraction $\alpha$) and $R(\alpha)$ is temporal resolution (the generational gap between canary and downstream responses, non-monotonic due to relaxation time matching at $\alpha{\approx}0.60$). The product $S \times R$ predicts four regimes: \emph{blind} ($\alpha \leq 0.45$; $S$ below detection floor), \emph{onset} ($\alpha \approx 0.50$; $S$ crosses threshold while $R$ remains high), \emph{synchronous dip} ($\alpha \approx 0.60$; $R \to 0$ from relaxation time matching suppresses detection despite rising $S$), and \emph{detection} ($\alpha \geq 0.75$; $S$ dominates the product), with full empirical confirmation in the regime and dose-response sections. Under a permutation test framework, detection power follows a standard normal CDF scaled by the product of signal strength, temporal resolution, and the square root of sample size divided by noise, which predicts a sharp power threshold at the critical contamination level—and as I increase the sample size to 20, I expect the critical point to shift leftward since the stronger signal-to-noise ratio will enable earlier detection.

The framework generates three testable predictions for the larger sample: the critical contamination level shifts left as increased sample size boosts power across all contamination fractions, the transition sharpens due to the square-root scaling broadening the power curve, and different statistical methods show different critical points reflecting their method-specific power characteristics. The key falsifiable test is the sub-threshold prediction—the framework predicts zero detections at 0.45 contamination (confirmed empirically with sub-threshold p-values near the power boundary), while detection at 0.50 or higher contamination serves as supplementary consistency evidence. For calibration, I'm validating the framework's error rates using built-in experimental controls, starting with the false positive rate at zero contamination as a null control. I'm working through the line count of my LaTeX draft more carefully now, tracking each section and paragraph to get an accurate structure of how the content is organized across the document. I'm verifying that all the constraints are satisfied: D142 removes CSD content, D143 limits to 3-4 out of 8 conditions, M037 uses only PermG for dose-response, C2 includes the standard statistical power scaling language, and the reproducibility details are locked in at n_perm=5000 with BH-FDR q=0.05 across 8 pairs. I'm also enforcing the writing rules—no em-dashes, no -ing verb forms, no hedging phrases like "notably" or "it is worth noting," and avoiding words like leverage or facilitate. The structure should be dense paragraphs without booktabs formatting.

Now I'm setting up the LaTeX structure with the Method section and its label, then the Signal-Times-Resolution Framework subsection. I need to make sure "detection phase transition" appears somewhere in the text to address D131, and I'm doing a final pass to ensure every number in the manuscript serves the narrative without gratuitous statistics.

Writing the Method section... I'm introducing the Multi-Method Consensus Test, a weighted framework that combines five different lead-lag detection methods and calibrates them against null data to identify false positives. Each method gets weighted inversely by its false positive rate, so more reliable methods contribute more heavily to the final consensus score.

The analysis reveals that permutation Granger causality stands out as the only method achieving zero false positives on null controls while maintaining consistent detection power, making it the recommended primary approach. For this method, I'm testing whether past values of a canary metric improve predictions of downstream metrics beyond their own history using 5,000 permutations with FDR correction across eight validated metric pairs.

What sets permutation Granger apart from the other four methods is its nonparametric null distribution that handles the short, non-stationary time series common in iterative training, built-in directional testing, and lack of hyperparameters. The competing approaches each have distinct weaknesses: naive cross-correlation suffers from 75% false positive rates, differenced cross-correlation can't separate bidirectional effects, threshold onset lacks power with the corrected calibration, and Toda-Yamamoto achieves only moderate supplementary detection at the cost of reduced power from additional degrees of freedom.

Now I'm working through how detectability scales under the Signal-by-Resolution framework, where the ability to identify canary-to-downstream temporal precedence depends on signal strength and temporal resolution working together. Signal strength increases monotonically with the parameter, but temporal resolution behaves non-monotonically—at low values the responses spread across generations, at intermediate values they compress into a single generation, and the pattern shifts again at higher values.

This multiplicative relationship produces four distinct regimes as the parameter increases: a blind zone where signals fall below detection, an onset region where signals first become detectable, a synchronous dip where temporal compression paradoxically suppresses detection despite stronger signals, and finally a detection regime where signal strength dominates. The empirical validation of these regimes is detailed in the referenced sections, and I'm now moving into the permutation test framework to model how detection power scales with both the parameter and sample size. The sub-threshold regime at α=0.45 provides the strongest test—the framework predicts no detections, which matches the empirical result, and the observed FDR values sit right at the power boundary as expected. At higher α values the predictions become less falsifiable since signal strength is already strong, so those serve mainly as consistency checks. For calibration, I'm validating the error rates using the built-in controls: the null condition at α=0.0 shows zero false positives across both methods and all seeds.

On the other end, at α=1.0 all the effect-size reference pairs are recovered perfectly with zero false negatives across multiple seeds. PermG performs consistently with the consensus method across all contamination levels, and the cross-architecture validation confirms the forward significance predictions hold in most conditions. The full calibration breakdown and practical guidance are documented in the appendix.

Now I'm working through the Method section structure—counting the typeset lines across the opening paragraphs, the MMCT and PermG descriptions, the S×R subsection with its theoretical framework and equations, and the calibration paragraph to estimate the total page space. I need to verify whether the equation should stay given the constraint against display items, and check if I'm using the \label{sec:pitfalls} reference elsewhere in the document—if it's not referenced, I can skip it to conserve space. I need to finalize the cross-references carefully—since I'm moving method details to Results and Appendix, I should update the references to point to those sections instead of the original subsections. Let me write out the compressed version now, keeping the language technical and direct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "57e404b7-9f81-496b-b428-4b3e4964d06d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01817LgRJCABg8JFEr7gYwAB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18702,
      "cache_read_input_tokens": 26616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18702
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

Now let me check what other sections reference from method.tex to ensure cross-reference compatibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "1093b592-835b-4011-8084-a988948f2b13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01817LgRJCABg8JFEr7gYwAB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18702,
      "cache_read_input_tokens": 26616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18702
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

<details open><summary>🔧 Tool call — Grep · `toolu_014qx86w93izvchw5SDjDM6X`</summary>

```json
{
  "pattern": "\\\\ref\\{sec:method\\}|\\\\ref\\{sec:theory\\}|\\\\ref\\{sec:pitfalls\\}|\\\\ref\\{sec:consensus\\}|\\\\ref\\{sec:calibration\\}|\\\\ref\\{sec:mmct\\}|\\\\ref\\{eq:detectability\\}|\\\\ref\\{eq:fpr_weight\\}|\\\\ref\\{eq:consensus_score\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
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
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "cc482f23-3f52-44e0-bdad-e84a9bd4c2db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01817LgRJCABg8JFEr7gYwAB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18702,
      "cache_read_input_tokens": 26616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18702
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

_source line 12 · 2026-05-20T11:21:05.608Z_

<details><summary>↩ Tool result · `toolu_014qx86w93izvchw5SDjDM6X`</summary>

```text
docs/paper/related_work.tex:75:Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:pitfalls}.
docs/paper/experiments.tex:39:At $\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\alpha_c$ at $T{=}10$ (\S\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.
docs/paper/experiments.tex:61:The non-monotonic dip at $\alpha{=}0.60$ is consistent with the $S \times R$ framework (\S\ref{sec:theory}): signal strength $S(\alpha)$ rises monotonically with contamination, but temporal resolution $R(\alpha)$ drops when relaxation time approaches the observation interval.
docs/paper/background.tex:29:We note that Granger precedence tests predictive improvement, not true causality \cite{shojaie2022granger}; this distinction is discussed further in \S\ref{sec:method}.
docs/paper/background.tex:39:Their joint application forms the basis of the multi-method consensus framework developed in \S\ref{sec:method}.
docs/paper/appendix.tex:135:At the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\S\ref{sec:theory}).
docs/paper/introduction.tex:43:    \item \textbf{Signal-times-resolution theory} (\S\ref{sec:theory}).
docs/paper/introduction.tex:48:    \item \textbf{Multi-method diagnostic toolkit} (\S\ref{sec:method}, \S\ref{sec:method_sensitivity}).
docs/paper/introduction.tex:62:\S\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.
docs/paper/discussion.tex:32:The MMCT weighted consensus (\S\ref{sec:mmct}) provides formal $p$-values grounded in the empirical null distribution, maintaining FPR${=}$0\%; however, the practical recommendation is simpler: for short iterative training series, permutation Granger alone provides reliable detection without requiring the full consensus machinery.
docs/paper/discussion.tex:74:The non-monotonic dose-response at $\alpha{=}0.60$ (PermG fwd: s42 3/8, s43 0/8, below both $\alpha{=}0.50$ and $\alpha{=}0.75$; \S\ref{sec:regime}) is consistent with the $S \times R$ prediction in \S\ref{sec:theory}: at $\alpha{=}0.60$, relaxation time matching drives temporal resolution $R \to 0$---entropy and diversity respond within the same generation---so that despite increasing signal strength $S$, the product $S \times R$ reaches a local minimum.
docs/paper/method.tex:5:This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to quantify their impact and identify the most reliable individual method (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
docs/paper/method.tex:76:Table~\ref{tab:practical_guidance} provides four recommended tiers, calibrated against our experimental controls (\S\ref{sec:calibration}).
docs/paper/method.tex:95:[Omitted long matching line]
docs/paper/method.tex:160:The uniform threshold ($K{\geq}4/5$) achieves FPR${=}$0\% and FNR${=}$0\% on reference extremes (\S\ref{sec:calibration}), but this ad-hoc threshold lacks formal statistical grounding: null-calibrated permutation testing assigns $p{=}0.16$ to $K{\geq}4/5$, failing to reach significance at conventional levels.
docs/paper/method.tex:161:The threshold also treats all methods equally, despite the heterogeneous error profiles documented in \S\ref{sec:pitfalls}: naive cross-correlation has 75\% forward-direction null-control FPR while permutation Granger has 0\%.
docs/paper/method.tex:255:Setting all weights $w_k{=}1$ reduces MMCT to the uniform $K$-of-$M$ threshold, making the existing consensus framework (\S\ref{sec:consensus}) a special case.
docs/paper/method.tex:256:Descriptively, $K{\geq}4/5$ achieves FPR${=}$0\% and FNR${=}$0\% on reference extremes (\S\ref{sec:calibration}); however, null-calibrated testing assigns $p{=}0.16$ to this threshold, indicating that it does not reach conventional significance levels.
docs/paper/experiments_reframe.tex:9:At $\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\alpha_c$ at $T{=}10$ (\S\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.
docs/paper/experiments_reframe.tex:31:The non-monotonic dip at $\alpha{=}0.60$ is consistent with the $S \times R$ framework (\S\ref{sec:theory}): signal strength $S(\alpha)$ rises monotonically with contamination, but temporal resolution $R(\alpha)$ drops when relaxation time approaches the observation interval.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "93652413-a276-429c-a8e1-4878082d136e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:75:Table~\\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \\S\\ref{sec:pitfalls}.\ndocs/paper/experiments.tex:39:At $\\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\\alpha_c$ at $T{=}10$ (\\S\\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.\ndocs/paper/experiments.tex:61:The non-monotonic dip at $\\alpha{=}0.60$ is consistent with the $S \\times R$ framework (\\S\\ref{sec:theory}): signal strength $S(\\alpha)$ rises monotonically with contamination, but temporal resolution $R(\\alpha)$ drops when relaxation time approaches the observation interval.\ndocs/paper/background.tex:29:We note that Granger precedence tests predictive improvement, not true causality \\cite{shojaie2022granger}; this distinction is discussed further in \\S\\ref{sec:method}.\ndocs/paper/background.tex:39:Their joint application forms the basis of the multi-method consensus framework developed in \\S\\ref{sec:method}.\ndocs/paper/appendix.tex:135:At the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\\S\\ref{sec:theory}).\ndocs/paper/introduction.tex:43:    \\item \\textbf{Signal-times-resolution theory} (\\S\\ref{sec:theory}).\ndocs/paper/introduction.tex:48:    \\item \\textbf{Multi-method diagnostic toolkit} (\\S\\ref{sec:method}, \\S\\ref{sec:method_sensitivity}).\ndocs/paper/introduction.tex:62:\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\ndocs/paper/discussion.tex:32:The MMCT weighted consensus (\\S\\ref{sec:mmct}) provides formal $p$-values grounded in the empirical null distribution, maintaining FPR${=}$0\\%; however, the practical recommendation is simpler: for short iterative training series, permutation Granger alone provides reliable detection without requiring the full consensus machinery.\ndocs/paper/discussion.tex:74:The non-monotonic dose-response at $\\alpha{=}0.60$ (PermG fwd: s42 3/8, s43 0/8, below both $\\alpha{=}0.50$ and $\\alpha{=}0.75$; \\S\\ref{sec:regime}) is consistent with the $S \\times R$ prediction in \\S\\ref{sec:theory}: at $\\alpha{=}0.60$, relaxation time matching drives temporal resolution $R \\to 0$---entropy and diversity respond within the same generation---so that despite increasing signal strength $S$, the product $S \\times R$ reaches a local minimum.\ndocs/paper/method.tex:5:This section distills three methodological pitfalls (\\S\\ref{sec:pitfalls}), proposes a multi-method consensus framework to quantify their impact and identify the most reliable individual method (\\S\\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\\S\\ref{sec:calibration}).\ndocs/paper/method.tex:76:Table~\\ref{tab:practical_guidance} provides four recommended tiers, calibrated against our experimental controls (\\S\\ref{sec:calibration}).\ndocs/paper/method.tex:95:[Omitted long matching line]\ndocs/paper/method.tex:160:The uniform threshold ($K{\\geq}4/5$) achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes (\\S\\ref{sec:calibration}), but this ad-hoc threshold lacks formal statistical grounding: null-calibrated permutation testing assigns $p{=}0.16$ to $K{\\geq}4/5$, failing to reach significance at conventional levels.\ndocs/paper/method.tex:161:The threshold also treats all methods equally, despite the heterogeneous error profiles documented in \\S\\ref{sec:pitfalls}: naive cross-correlation has 75\\% forward-direction null-control FPR while permutation Granger has 0\\%.\ndocs/paper/method.tex:255:Setting all weights $w_k{=}1$ reduces MMCT to the uniform $K$-of-$M$ threshold, making the existing consensus framework (\\S\\ref{sec:consensus}) a special case.\ndocs/paper/method.tex:256:Descriptively, $K{\\geq}4/5$ achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes (\\S\\ref{sec:calibration}); however, null-calibrated testing assigns $p{=}0.16$ to this threshold, indicating that it does not reach conventional significance levels.\ndocs/paper/experiments_reframe.tex:9:At $\\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\\alpha_c$ at $T{=}10$ (\\S\\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.\ndocs/paper/experiments_reframe.tex:31:The non-monotonic dip at $\\alpha{=}0.60$ is consistent with the $S \\times R$ framework (\\S\\ref{sec:theory}): signal strength $S(\\alpha)$ rises monotonically with contamination, but temporal resolution $R(\\alpha)$ drops when relaxation time approaches the observation interval.",
    "numLines": 20
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Key cross-references I need to preserve:
- `\label{sec:method}` - referenced from background.tex, introduction.tex
- `\label{sec:theory}` - referenced from experiments.tex, introduction.tex, appendix.tex, discussion.tex
- `\label{sec:pitfalls}` - referenced from related_work.tex, method.tex itself
- `\label{sec:mmct}` - referenced from discussion.tex
- `\label{sec:calibration}` - referenced from method.tex itself (internal, can remove if no external refs)


- `\label{sec:consensus}` - referenced from method.tex itself (internal)

Now I'm checking whether the equation labels are actually referenced elsewhere in the document or if they're just internal anchors I can safely remove.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "42055eaf-2f63-4b46-bbd9-5b2d3e5e218b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vb2uduB2MmFWAy7TEUren",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8189,
      "cache_read_input_tokens": 45318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8189
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

_source line 14_

Let me check equation references too.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "78de3e15-abcc-4a07-86a6-0ad38423d6cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vb2uduB2MmFWAy7TEUren",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8189,
      "cache_read_input_tokens": 45318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8189
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

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_01JHaica3Wu4s9EM3MRp5Nt2`</summary>

```json
{
  "pattern": "\\\\ref\\{eq:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
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
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "44d38602-17d6-48f5-9395-5f9361da9cd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vb2uduB2MmFWAy7TEUren",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8189,
      "cache_read_input_tokens": 45318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8189
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

_source line 16 · 2026-05-20T11:21:12.221Z_

<details><summary>↩ Tool result · `toolu_01JHaica3Wu4s9EM3MRp5Nt2`</summary>

```text
docs/paper/method.tex:257:MMCT weighted consensus resolves this gap by providing formal $p$-values (Eq.~\ref{eq:pvalue}) grounded in the empirical null distribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "dc292d6f-156e-4c33-bb7b-38510381187c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/method.tex:257:MMCT weighted consensus resolves this gap by providing formal $p$-values (Eq.~\\ref{eq:pvalue}) grounded in the empirical null distribution.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
The only equation references are internal to method.tex. So I just need to keep the labels that are externally referenced:
- `\label{sec:method}` - yes
- `\label{sec:theory}` - yes
- `\label{sec:pitfalls}` - yes (from related_work.tex)
- `\label{sec:mmct}` - yes (from discussion.tex)
- `\label{sec:calibration}` - only internal to method.tex, not strictly needed but could keep
- `\label{eq:detectability}` - not externally referenced, but good to have


- `\label{sec:consensus}` - only internal to method.tex

For the compressed version, I need to keep the external references: `sec:method`, `sec:theory`, `sec:pitfalls`, `sec:mmct`, and `eq:detectability`. Now I'll write out the final version carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "705883b4-2a4c-47cb-88d9-b8c6c3f7f1d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Up1ErUq1Cs9qNUyfqtCiD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 53507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 440
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

Now I have the full picture. External references require: `sec:method`, `sec:theory`, `sec:pitfalls`, `sec:mmct`, and `eq:detectability`. Let me write the compressed version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "4ed8a57a-901e-4a0e-ae4c-9622311bc0a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Up1ErUq1Cs9qNUyfqtCiD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 53507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 440
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

<details open><summary>🔧 Tool call — Write · `toolu_014LsGREKh3VPn7tKSrGSJSq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\n\\paragraph{Methodological pitfalls.}\n\\label{sec:pitfalls}\nLead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \\S\\ref{sec:regime}--\\ref{sec:dose_response}.\n\\emph{Method sensitivity}: five detection methods applied to identical data ($\\alpha{=}1.0$, 16 canary$\\to$downstream pairs) yield significance rates from 100\\% (naive cross-correlation) to 37.5\\% (permutation Granger), with inter-method agreement at $\\kappa{=}0.185$ and a spurious-signal rate ${\\geq}62.5\\%$.\n\\emph{Spurious regression}: first-differencing to remove shared trends~\\cite{granger1974spurious} eliminates canary$\\to$perplexity associations ($F{\\approx}0$, $p{=}0.99$) while preserving canary$\\to$diversity (24/24$\\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.\n\\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\\alpha{=}0.45$ but 6/8 at $\\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\\alpha$ study would miss entirely.\nThese pitfalls motivate systematic method comparison rather than reliance on any single detection approach.\n\n\\paragraph{Multi-Method Consensus Test (MMCT).}\n\\label{sec:mmct}\nWe apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve tradition~\\cite{simonsohn2020specification,bell2022modeling} adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.\nMMCT is a consensus testing protocol, not a novel statistical method.\nIt compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\\alpha{=}0.0$) data where any detection is a false positive.\nEach method $m_k$ receives weight $w_k = 1/\\max(\\hat{\\text{FPR}}_k, \\epsilon)$ with $\\epsilon{=}0.01$; the weighted score $W(X \\to Y) = \\sum_k w_k d_k / \\sum_k w_k$ yields formal $p$-values from the empirical null distribution (Algorithm~\\ref{alg:mmct}; Appendix).\nMMCT identifies permutation Granger (PermG) as the only method combining zero null-control FPR with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.\n\n\\paragraph{Permutation Granger causality.}\nPermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\nWe apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 validated canary$\\to$downstream pairs (2 canaries $\\times$ 4 downstream metrics).\nThree properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.\nThe remaining four methods each exhibit a specific limitation: naive cross-correlation has 75\\% null-control FPR; differenced cross-correlation detects bidirectionally without directional separation; threshold onset is power-limited at $T{=}11$ under corrected $3\\sigma$ calibration (0/8 significant in 8 of 12 cross-architecture conditions); Toda--Yamamoto~\\cite{toda1995statistical} achieves moderate supplementary detection (3--4/8 at $\\alpha{\\geq}0.50$) with reduced power from degree-of-freedom costs of lag augmentation.\nPer-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix.\n\n\\subsection{Signal-Times-Resolution Framework}\n\\label{sec:theory}\n\nWe apply standard statistical power scaling to PermG under the Signal$\\times$Resolution (S$\\times$R) framework.\nDetectability of canary$\\to$downstream temporal precedence depends on two competing factors:\n\\begin{equation}\n    \\text{Detectability}(\\alpha) \\;\\propto\\; S(\\alpha) \\times R(\\alpha),\n    \\label{eq:detectability}\n\\end{equation}\nwhere $S(\\alpha)$ is signal strength (magnitude of distributional shift, monotonically increasing with $\\alpha$) and $R(\\alpha)$ is temporal resolution (the generational gap between canary and downstream responses).\n$R(\\alpha)$ is non-monotonic: at low $\\alpha$, entropy and diversity respond in different generations ($R$ large); at $\\alpha{\\approx}0.60$, relaxation time matching compresses both responses into a single generation ($R \\to 0$); at high $\\alpha$, the severity of entropy collapse outpaces the diversity cascade, restoring the generational offset.\nThe product $S \\times R$ predicts four regimes: \\emph{blind} ($\\alpha \\leq 0.45$; $S$ below detection floor), \\emph{onset} ($\\alpha \\approx 0.50$; $S$ crosses threshold while $R$ remains high), \\emph{synchronous dip} ($\\alpha \\approx 0.60$; $R \\to 0$ suppresses detection despite rising $S$), and \\emph{detection} ($\\alpha \\geq 0.75$; $S$ dominates).\nFull empirical confirmation appears in \\S\\ref{sec:regime} and \\S\\ref{sec:dose_response}.\n\nUnder a permutation test framework, detection power scales as $\\mathrm{Power}(\\alpha, T) = \\Phi\\bigl(S \\cdot R \\cdot \\sqrt{T} / \\sigma_{\\mathrm{noise}}\\bigr)$, where $\\Phi$ is the standard normal CDF and the $\\sqrt{T}$ scaling follows standard power analysis.\nThe detection phase transition at $\\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \\cdot R \\cdot \\sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.\nThis generates three predictions for $T{=}20$: (i)~$\\alpha_c$ left-shifts as increased $T$ raises power at all $\\alpha$; (ii)~the transition smooths as $\\sqrt{T}$ broadens the power curve; (iii)~different methods exhibit different $\\alpha_c$ values due to method-specific power curves.\nThe key falsifiable test is the sub-threshold prediction: the framework predicts 0/8 at $\\alpha{=}0.45$ (at $T{=}10$), confirmed empirically (\\S\\ref{sec:regime}), with sub-threshold FDR $p{=}0.059$--$0.091$ consistent with proximity to the power boundary.\nDetection at $\\alpha{\\geq}0.50$ (predicted ${\\geq}5/8$, CI${=}[5,8]$) serves as supplementary consistency evidence rather than a strong test, as these predictions are near-unfalsifiable given signal strength.\n\n\\paragraph{Calibration.}\nWe validate error rates with built-in experimental controls.\nFalse positive rate: at $\\alpha{=}0.0$ (null control, no synthetic contamination), PermG and MMCT weighted consensus both yield 0\\% FPR across 3 seeds (0/24 pairs at consensus $K{\\geq}3$).\nFalse negative rate: at $\\alpha{=}1.0$, all 6 effect-size reference pairs (2 canaries $\\times$ 3 diversity metrics, selected by criteria independent of the detection methods) are recovered at 0\\% FNR across 4 seeds.\nPermG matches consensus performance at all tested contamination levels, with cross-architecture validation confirming PermG forward significance ${\\geq}6/8$ in 13 of 15 conditions (\\S\\ref{sec:generalization}).\nFull calibration details, practical guidance tiers, and method-level breakdown appear in the Appendix.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "d5773713-2c82-41d1-a108-79defedf41ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Up1ErUq1Cs9qNUyfqtCiD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 53507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 440
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

_source line 20 · 2026-05-20T11:22:02.199Z_

<details><summary>↩ Tool result · `toolu_014LsGREKh3VPn7tKSrGSJSq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "a2fdc275-5bee-4e74-b10b-31396298f4cb",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\n\\paragraph{Methodological pitfalls.}\n\\label{sec:pitfalls}\nLead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \\S\\ref{sec:regime}--\\ref{sec:dose_response}.\n\\emph{Method sensitivity}: five detection methods applied to identical data ($\\alpha{=}1.0$, 16 canary$\\to$downstream pairs) yield significance rates from 100\\% (naive cross-correlation) to 37.5\\% (permutation Granger), with inter-method agreement at $\\kappa{=}0.185$ and a spurious-signal rate ${\\geq}62.5\\%$.\n\\emph{Spurious regression}: first-differencing to remove shared trends~\\cite{granger1974spurious} eliminates canary$\\to$perplexity associations ($F{\\approx}0$, $p{=}0.99$) while preserving canary$\\to$diversity (24/24$\\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.\n\\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\\alpha{=}0.45$ but 6/8 at $\\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\\alpha$ study would miss entirely.\nThese pitfalls motivate systematic method comparison rather than reliance on any single detection approach.\n\n\\paragraph{Multi-Method Consensus Test (MMCT).}\n\\label{sec:mmct}\nWe apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve tradition~\\cite{simonsohn2020specification,bell2022modeling} adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.\nMMCT is a consensus testing protocol, not a novel statistical method.\nIt compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\\alpha{=}0.0$) data where any detection is a false positive.\nEach method $m_k$ receives weight $w_k = 1/\\max(\\hat{\\text{FPR}}_k, \\epsilon)$ with $\\epsilon{=}0.01$; the weighted score $W(X \\to Y) = \\sum_k w_k d_k / \\sum_k w_k$ yields formal $p$-values from the empirical null distribution (Algorithm~\\ref{alg:mmct}; Appendix).\nMMCT identifies permutation Granger (PermG) as the only method combining zero null-control FPR with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.\n\n\\paragraph{Permutation Granger causality.}\nPermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\nWe apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 validated canary$\\to$downstream pairs (2 canaries $\\times$ 4 downstream metrics).\nThree properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.\nThe remaining four methods each exhibit a specific limitation: naive cross-correlation has 75\\% null-control FPR; differenced cross-correlation detects bidirectionally without directional separation; threshold onset is power-limited at $T{=}11$ under corrected $3\\sigma$ calibration (0/8 significant in 8 of 12 cross-architecture conditions); Toda--Yamamoto~\\cite{toda1995statistical} achieves moderate supplementary detection (3--4/8 at $\\alpha{\\geq}0.50$) with reduced power from degree-of-freedom costs of lag augmentation.\nPer-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix.\n\n\\subsection{Signal-Times-Resolution Framework}\n\\label{sec:theory}\n\nWe apply standard statistical power scaling to PermG under the Signal$\\times$Resolution (S$\\times$R) framework.\nDetectability of canary$\\to$downstream temporal precedence depends on two competing factors:\n\\begin{equation}\n    \\text{Detectability}(\\alpha) \\;\\propto\\; S(\\alpha) \\times R(\\alpha),\n    \\label{eq:detectability}\n\\end{equation}\nwhere $S(\\alpha)$ is signal strength (magnitude of distributional shift, monotonically increasing with $\\alpha$) and $R(\\alpha)$ is temporal resolution (the generational gap between canary and downstream responses).\n$R(\\alpha)$ is non-monotonic: at low $\\alpha$, entropy and diversity respond in different generations ($R$ large); at $\\alpha{\\approx}0.60$, relaxation time matching compresses both responses into a single generation ($R \\to 0$); at high $\\alpha$, the severity of entropy collapse outpaces the diversity cascade, restoring the generational offset.\nThe product $S \\times R$ predicts four regimes: \\emph{blind} ($\\alpha \\leq 0.45$; $S$ below detection floor), \\emph{onset} ($\\alpha \\approx 0.50$; $S$ crosses threshold while $R$ remains high), \\emph{synchronous dip} ($\\alpha \\approx 0.60$; $R \\to 0$ suppresses detection despite rising $S$), and \\emph{detection} ($\\alpha \\geq 0.75$; $S$ dominates).\nFull empirical confirmation appears in \\S\\ref{sec:regime} and \\S\\ref{sec:dose_response}.\n\nUnder a permutation test framework, detection power scales as $\\mathrm{Power}(\\alpha, T) = \\Phi\\bigl(S \\cdot R \\cdot \\sqrt{T} / \\sigma_{\\mathrm{noise}}\\bigr)$, where $\\Phi$ is the standard normal CDF and the $\\sqrt{T}$ scaling follows standard power analysis.\nThe detection phase transition at $\\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \\cdot R \\cdot \\sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.\nThis generates three predictions for $T{=}20$: (i)~$\\alpha_c$ left-shifts as increased $T$ raises power at all $\\alpha$; (ii)~the transition smooths as $\\sqrt{T}$ broadens the power curve; (iii)~different methods exhibit different $\\alpha_c$ values due to method-specific power curves.\nThe key falsifiable test is the sub-threshold prediction: the framework predicts 0/8 at $\\alpha{=}0.45$ (at $T{=}10$), confirmed empirically (\\S\\ref{sec:regime}), with sub-threshold FDR $p{=}0.059$--$0.091$ consistent with proximity to the power boundary.\nDetection at $\\alpha{\\geq}0.50$ (predicted ${\\geq}5/8$, CI${=}[5,8]$) serves as supplementary consistency evidence rather than a strong test, as these predictions are near-unfalsifiable given signal strength.\n\n\\paragraph{Calibration.}\nWe validate error rates with built-in experimental controls.\nFalse positive rate: at $\\alpha{=}0.0$ (null control, no synthetic contamination), PermG and MMCT weighted consensus both yield 0\\% FPR across 3 seeds (0/24 pairs at consensus $K{\\geq}3$).\nFalse negative rate: at $\\alpha{=}1.0$, all 6 effect-size reference pairs (2 canaries $\\times$ 3 diversity metrics, selected by criteria independent of the detection methods) are recovered at 0\\% FNR across 4 seeds.\nPermG matches consensus performance at all tested contamination levels, with cross-architecture validation confirming PermG forward significance ${\\geq}6/8$ in 13 of 15 conditions (\\S\\ref{sec:generalization}).\nFull calibration details, practical guidance tiers, and method-level breakdown appear in the Appendix.\n",
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

Let me verify the output and count lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "a7f4ebca-df0e-491f-bed8-626f6ee89864",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNCqdQDm8s416aeSQAv1En",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2639,
      "cache_read_input_tokens": 53947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2639
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_013MVGgwzVCusiiwWhUxG7ib`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex && echo \"---\" && grep -c '\\\\\\\\' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex || true && echo \"---non-blank lines:\" && grep -cv '^\\s*$' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
  "description": "Count lines in method_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "6872e6f9-6530-449c-a929-7a055fff2fa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNCqdQDm8s416aeSQAv1En",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2639,
      "cache_read_input_tokens": 53947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2639
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01KTxgvUSWQhLDhFdkt88qhS`</summary>

```json
{
  "command": "grep -n '—\\|—' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex || echo \"No em-dashes found\"",
  "description": "Check for em-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "888bb48d-142c-4d04-97a1-e50f19b4820a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNCqdQDm8s416aeSQAv1En",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2639,
      "cache_read_input_tokens": 53947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2639
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

_source line 24 · 2026-05-20T11:22:08.409Z_

<details><summary>↩ Tool result · `toolu_013MVGgwzVCusiiwWhUxG7ib`</summary>

```text
52 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex
---
0
---non-blank lines:
45
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "8f009bdc-274e-4b93-92f8-772a15c74376",
  "tool_use_result": {
    "stdout": "52 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex\n---\n0\n---non-blank lines:\n45",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T11:22:08.682Z_

<details><summary>↩ Tool result · `toolu_01KTxgvUSWQhLDhFdkt88qhS`</summary>

```text
No em-dashes found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "a410b8c3-4f70-42b0-8daf-e9c50ecdc56f",
  "tool_use_result": {
    "stdout": "No em-dashes found",
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

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
52 total lines, 45 non-blank lines. The target is ~67 lines. I need to check whether this means 67 typeset lines in the compiled PDF or 67 source lines. Given the context (1.5 pages in dual-column), 67 typeset lines seems right. Let me estimate: in a two-column ACL/EMNLP format, each column has about 55-58 lines of text per page. 1.5 pages = about 82-87 lines, but with the subsection heading, equation, and spacing, the text content would be about 67-70 lines.


Now I'm breaking down the typeset line count by section. Each paragraph has several long sentences that will wrap across multiple lines in the two-column format, so I'm estimating the Pitfalls section at around 12-14 lines, MMCT at 11-13, PermG at 14-16, and the S×R intro with its equation at 10-12 lines.

Adding in the Power section at 12-14 lines and Calibration at 8-10 lines, I'm getting a total estimate of roughly 67-79 typeset lines. That seems reasonable for 1.5 pages in dual-column format when accounting for headings and spacing.

But I'm second-guessing whether the task is asking for source lines or typeset lines—my source is at 52 total with 45 non-blank lines, which would be under if that's the target. If it's typeset lines, I'm probably closer to 70-75, which fits better.

Let me think about this differently using the page budget. In dual-column EMNLP format, 1.5 pages gives me roughly 165 column-lines total, but headings, the equation, and spacing eat up 15-20 of those, leaving about 145-150 for actual content. The original method.tex was 364 lines, so if I'm compressing by a factor of about 5.4x, that gives me roughly 67 lines as a target—which aligns with what I'm aiming for.

My current file sits at 52 lines, which is actually pretty close. The key difference is that my lines are much denser—each one packs a full sentence or more, whereas the original spreads things out across multiple lines with structural elements like tables and algorithm blocks that I've moved to the appendix. Looking at just the prose content, I probably have around 30-40 substantive sentences, which should compress well into the typeset format. I think my version is actually appropriate for the 1.5-page target, so let me move on to checking other aspects.

Now I'm verifying that all the constraints are actually satisfied in my current draft—checking that the key phrases like "steep onset" and "detection phase transition" are present, that α_c is properly qualified with the temperature, that I'm using only PermG for the dose-response analysis, and that the falsifiable prediction about α=0.45 yielding 0/8 is clearly stated as the main test with the α≥0.50 case as supplementary. The reproducibility details like the 5,000 permutations are also in there.

I'm also confirming the writing style constraints are met: no em-dashes, no -ing verb endings, no hedging phrases like "notably" or "it is worth noting," and no overused words like "leverage" or "facilitate." The section labels and key citations are preserved, though I've excluded the scheffer2009early reference. The BH-FDR correction at q=0.05 with 8 pairs is accounted for, and the paragraphs are dense and direct.

I notice scheffer2009early should be included in the MMCT section where I discuss the specification curve tradition and early warning signals. Let me add that citation and do a final pass on -ing endings to ensure they're eliminated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "898fdf08-4919-4f3e-833d-67aa8386aac3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bRoBXR2QiYY6LYJHbmvWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 56586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 584
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

_source line 27_

Let me run constraint checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "cbcd491e-f49b-4a73-8e85-aae7cb15cc89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bRoBXR2QiYY6LYJHbmvWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 56586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 584
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01D4VpueHHNnVrbBRFqncKcs`</summary>

```json
{
  "command": "echo \"=== -ing clause endings ===\" && grep -n 'ing[,.]' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex | grep -v '{' | grep -v 'scaling\\|testing\\|mixing\\|training\\|matching' || echo \"None found\" && echo \"=== Furthermore/Moreover/Additionally ===\" && grep -ni 'furthermore\\|moreover\\|additionally\\|notably\\|it is worth' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex || echo \"None found\" && echo \"=== leverage/utilize/delve/facilitate ===\" && grep -ni 'leverage\\|utilize\\|delve\\|facilitate' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex || echo \"None found\" && echo \"=== Missing citations check ===\" && grep -o 'cite{[^}]*}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex | sort -u",
  "description": "Check writing constraints and citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "9b1d7ab9-7bd0-4375-b06c-c98bcb483a5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bRoBXR2QiYY6LYJHbmvWb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 56586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 584
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

_source line 29 · 2026-05-20T11:22:49.196Z_

<details><summary>↩ Tool result · `toolu_01D4VpueHHNnVrbBRFqncKcs`</summary>

```text
=== -ing clause endings ===
None found
=== Furthermore/Moreover/Additionally ===
None found
=== leverage/utilize/delve/facilitate ===
None found
=== Missing citations check ===
cite{boettiger2012limits}
cite{granger1974spurious}
cite{shojaie2022granger}
cite{simonsohn2020specification,bell2022modeling}
cite{toda1995statistical}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "0aba8756-0799-41e6-b662-770eedcb97f2",
  "tool_use_result": {
    "stdout": "=== -ing clause endings ===\nNone found\n=== Furthermore/Moreover/Additionally ===\nNone found\n=== leverage/utilize/delve/facilitate ===\nNone found\n=== Missing citations check ===\ncite{boettiger2012limits}\ncite{granger1974spurious}\ncite{shojaie2022granger}\ncite{simonsohn2020specification,bell2022modeling}\ncite{toda1995statistical}",
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

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Missing citation: `scheffer2009early`. The task says to include it. The original method.tex uses it in the context of "multi-method validation in early-warning signal detection". I should add it to the MMCT paragraph.

Let me add it to the MMCT paragraph where I describe it as a weighted consensus framework. I can connect it to early-warning signal detection literature.

Let me also re-read the file to make the edit precisely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "fea73866-98e3-48a6-9959-6b103a782389",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWDaZ4sUQYTVE85r4nfSSY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 57170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1984
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

Missing `scheffer2009early`. Let me add it to the MMCT paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "8b30a0e8-3709-4c07-b438-a6e1c1b71b44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWDaZ4sUQYTVE85r4nfSSY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 57170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1984
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

<details open><summary>🔧 Tool call — Read · `toolu_01HfFHUu1ovnGDQ8gk88SWWy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "a0f51104-03bb-4931-ac60-83cf4f6e896e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWDaZ4sUQYTVE85r4nfSSY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 57170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1984
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

_source line 33 · 2026-05-20T11:22:54.827Z_

<details><summary>↩ Tool result · `toolu_01HfFHUu1ovnGDQ8gk88SWWy`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Methodological pitfalls.}
5	\label{sec:pitfalls}
6	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
7	\emph{Method sensitivity}: five detection methods applied to identical data ($\alpha{=}1.0$, 16 canary$\to$downstream pairs) yield significance rates from 100\% (naive cross-correlation) to 37.5\% (permutation Granger), with inter-method agreement at $\kappa{=}0.185$ and a spurious-signal rate ${\geq}62.5\%$.
8	\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
9	\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\alpha{=}0.45$ but 6/8 at $\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\alpha$ study would miss entirely.
10	These pitfalls motivate systematic method comparison rather than reliance on any single detection approach.
11	
12	\paragraph{Multi-Method Consensus Test (MMCT).}
13	\label{sec:mmct}
14	We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve tradition~\cite{simonsohn2020specification,bell2022modeling} adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
15	MMCT is a consensus testing protocol, not a novel statistical method.
16	It compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
17	Each method $m_k$ receives weight $w_k = 1/\max(\hat{\text{FPR}}_k, \epsilon)$ with $\epsilon{=}0.01$; the weighted score $W(X \to Y) = \sum_k w_k d_k / \sum_k w_k$ yields formal $p$-values from the empirical null distribution (Algorithm~\ref{alg:mmct}; Appendix).
18	MMCT identifies permutation Granger (PermG) as the only method combining zero null-control FPR with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.
19	
20	\paragraph{Permutation Granger causality.}
21	PermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
22	We apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 validated canary$\to$downstream pairs (2 canaries $\times$ 4 downstream metrics).
23	Three properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.
24	The remaining four methods each exhibit a specific limitation: naive cross-correlation has 75\% null-control FPR; differenced cross-correlation detects bidirectionally without directional separation; threshold onset is power-limited at $T{=}11$ under corrected $3\sigma$ calibration (0/8 significant in 8 of 12 cross-architecture conditions); Toda--Yamamoto~\cite{toda1995statistical} achieves moderate supplementary detection (3--4/8 at $\alpha{\geq}0.50$) with reduced power from degree-of-freedom costs of lag augmentation.
25	Per-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix.
26	
27	\subsection{Signal-Times-Resolution Framework}
28	\label{sec:theory}
29	
30	We apply standard statistical power scaling to PermG under the Signal$\times$Resolution (S$\times$R) framework.
31	Detectability of canary$\to$downstream temporal precedence depends on two competing factors:
32	\begin{equation}
33	    \text{Detectability}(\alpha) \;\propto\; S(\alpha) \times R(\alpha),
34	    \label{eq:detectability}
35	\end{equation}
36	where $S(\alpha)$ is signal strength (magnitude of distributional shift, monotonically increasing with $\alpha$) and $R(\alpha)$ is temporal resolution (the generational gap between canary and downstream responses).
37	$R(\alpha)$ is non-monotonic: at low $\alpha$, entropy and diversity respond in different generations ($R$ large); at $\alpha{\approx}0.60$, relaxation time matching compresses both responses into a single generation ($R \to 0$); at high $\alpha$, the severity of entropy collapse outpaces the diversity cascade, restoring the generational offset.
38	The product $S \times R$ predicts four regimes: \emph{blind} ($\alpha \leq 0.45$; $S$ below detection floor), \emph{onset} ($\alpha \approx 0.50$; $S$ crosses threshold while $R$ remains high), \emph{synchronous dip} ($\alpha \approx 0.60$; $R \to 0$ suppresses detection despite rising $S$), and \emph{detection} ($\alpha \geq 0.75$; $S$ dominates).
39	Full empirical confirmation appears in \S\ref{sec:regime} and \S\ref{sec:dose_response}.
40	
41	Under a permutation test framework, detection power scales as $\mathrm{Power}(\alpha, T) = \Phi\bigl(S \cdot R \cdot \sqrt{T} / \sigma_{\mathrm{noise}}\bigr)$, where $\Phi$ is the standard normal CDF and the $\sqrt{T}$ scaling follows standard power analysis.
42	The detection phase transition at $\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \cdot R \cdot \sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.
43	This generates three predictions for $T{=}20$: (i)~$\alpha_c$ left-shifts as increased $T$ raises power at all $\alpha$; (ii)~the transition smooths as $\sqrt{T}$ broadens the power curve; (iii)~different methods exhibit different $\alpha_c$ values due to method-specific power curves.
44	The key falsifiable test is the sub-threshold prediction: the framework predicts 0/8 at $\alpha{=}0.45$ (at $T{=}10$), confirmed empirically (\S\ref{sec:regime}), with sub-threshold FDR $p{=}0.059$--$0.091$ consistent with proximity to the power boundary.
45	Detection at $\alpha{\geq}0.50$ (predicted ${\geq}5/8$, CI${=}[5,8]$) serves as supplementary consistency evidence rather than a strong test, as these predictions are near-unfalsifiable given signal strength.
46	
47	\paragraph{Calibration.}
48	We validate error rates with built-in experimental controls.
49	False positive rate: at $\alpha{=}0.0$ (null control, no synthetic contamination), PermG and MMCT weighted consensus both yield 0\% FPR across 3 seeds (0/24 pairs at consensus $K{\geq}3$).
50	False negative rate: at $\alpha{=}1.0$, all 6 effect-size reference pairs (2 canaries $\times$ 3 diversity metrics, selected by criteria independent of the detection methods) are recovered at 0\% FNR across 4 seeds.
51	PermG matches consensus performance at all tested contamination levels, with cross-architecture validation confirming PermG forward significance ${\geq}6/8$ in 13 of 15 conditions (\S\ref{sec:generalization}).
52	Full calibration details, practical guidance tiers, and method-level breakdown appear in the Appendix.
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "81479bb1-13f8-479b-a6cf-de2b03ac30cd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\paragraph{Methodological pitfalls.}\n\\label{sec:pitfalls}\nLead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \\S\\ref{sec:regime}--\\ref{sec:dose_response}.\n\\emph{Method sensitivity}: five detection methods applied to identical data ($\\alpha{=}1.0$, 16 canary$\\to$downstream pairs) yield significance rates from 100\\% (naive cross-correlation) to 37.5\\% (permutation Granger), with inter-method agreement at $\\kappa{=}0.185$ and a spurious-signal rate ${\\geq}62.5\\%$.\n\\emph{Spurious regression}: first-differencing to remove shared trends~\\cite{granger1974spurious} eliminates canary$\\to$perplexity associations ($F{\\approx}0$, $p{=}0.99$) while preserving canary$\\to$diversity (24/24$\\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.\n\\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\\alpha{=}0.45$ but 6/8 at $\\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\\alpha$ study would miss entirely.\nThese pitfalls motivate systematic method comparison rather than reliance on any single detection approach.\n\n\\paragraph{Multi-Method Consensus Test (MMCT).}\n\\label{sec:mmct}\nWe apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve tradition~\\cite{simonsohn2020specification,bell2022modeling} adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.\nMMCT is a consensus testing protocol, not a novel statistical method.\nIt compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\\alpha{=}0.0$) data where any detection is a false positive.\nEach method $m_k$ receives weight $w_k = 1/\\max(\\hat{\\text{FPR}}_k, \\epsilon)$ with $\\epsilon{=}0.01$; the weighted score $W(X \\to Y) = \\sum_k w_k d_k / \\sum_k w_k$ yields formal $p$-values from the empirical null distribution (Algorithm~\\ref{alg:mmct}; Appendix).\nMMCT identifies permutation Granger (PermG) as the only method combining zero null-control FPR with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.\n\n\\paragraph{Permutation Granger causality.}\nPermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\nWe apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 validated canary$\\to$downstream pairs (2 canaries $\\times$ 4 downstream metrics).\nThree properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.\nThe remaining four methods each exhibit a specific limitation: naive cross-correlation has 75\\% null-control FPR; differenced cross-correlation detects bidirectionally without directional separation; threshold onset is power-limited at $T{=}11$ under corrected $3\\sigma$ calibration (0/8 significant in 8 of 12 cross-architecture conditions); Toda--Yamamoto~\\cite{toda1995statistical} achieves moderate supplementary detection (3--4/8 at $\\alpha{\\geq}0.50$) with reduced power from degree-of-freedom costs of lag augmentation.\nPer-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix.\n\n\\subsection{Signal-Times-Resolution Framework}\n\\label{sec:theory}\n\nWe apply standard statistical power scaling to PermG under the Signal$\\times$Resolution (S$\\times$R) framework.\nDetectability of canary$\\to$downstream temporal precedence depends on two competing factors:\n\\begin{equation}\n    \\text{Detectability}(\\alpha) \\;\\propto\\; S(\\alpha) \\times R(\\alpha),\n    \\label{eq:detectability}\n\\end{equation}\nwhere $S(\\alpha)$ is signal strength (magnitude of distributional shift, monotonically increasing with $\\alpha$) and $R(\\alpha)$ is temporal resolution (the generational gap between canary and downstream responses).\n$R(\\alpha)$ is non-monotonic: at low $\\alpha$, entropy and diversity respond in different generations ($R$ large); at $\\alpha{\\approx}0.60$, relaxation time matching compresses both responses into a single generation ($R \\to 0$); at high $\\alpha$, the severity of entropy collapse outpaces the diversity cascade, restoring the generational offset.\nThe product $S \\times R$ predicts four regimes: \\emph{blind} ($\\alpha \\leq 0.45$; $S$ below detection floor), \\emph{onset} ($\\alpha \\approx 0.50$; $S$ crosses threshold while $R$ remains high), \\emph{synchronous dip} ($\\alpha \\approx 0.60$; $R \\to 0$ suppresses detection despite rising $S$), and \\emph{detection} ($\\alpha \\geq 0.75$; $S$ dominates).\nFull empirical confirmation appears in \\S\\ref{sec:regime} and \\S\\ref{sec:dose_response}.\n\nUnder a permutation test framework, detection power scales as $\\mathrm{Power}(\\alpha, T) = \\Phi\\bigl(S \\cdot R \\cdot \\sqrt{T} / \\sigma_{\\mathrm{noise}}\\bigr)$, where $\\Phi$ is the standard normal CDF and the $\\sqrt{T}$ scaling follows standard power analysis.\nThe detection phase transition at $\\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \\cdot R \\cdot \\sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.\nThis generates three predictions for $T{=}20$: (i)~$\\alpha_c$ left-shifts as increased $T$ raises power at all $\\alpha$; (ii)~the transition smooths as $\\sqrt{T}$ broadens the power curve; (iii)~different methods exhibit different $\\alpha_c$ values due to method-specific power curves.\nThe key falsifiable test is the sub-threshold prediction: the framework predicts 0/8 at $\\alpha{=}0.45$ (at $T{=}10$), confirmed empirically (\\S\\ref{sec:regime}), with sub-threshold FDR $p{=}0.059$--$0.091$ consistent with proximity to the power boundary.\nDetection at $\\alpha{\\geq}0.50$ (predicted ${\\geq}5/8$, CI${=}[5,8]$) serves as supplementary consistency evidence rather than a strong test, as these predictions are near-unfalsifiable given signal strength.\n\n\\paragraph{Calibration.}\nWe validate error rates with built-in experimental controls.\nFalse positive rate: at $\\alpha{=}0.0$ (null control, no synthetic contamination), PermG and MMCT weighted consensus both yield 0\\% FPR across 3 seeds (0/24 pairs at consensus $K{\\geq}3$).\nFalse negative rate: at $\\alpha{=}1.0$, all 6 effect-size reference pairs (2 canaries $\\times$ 3 diversity metrics, selected by criteria independent of the detection methods) are recovered at 0\\% FNR across 4 seeds.\nPermG matches consensus performance at all tested contamination levels, with cross-architecture validation confirming PermG forward significance ${\\geq}6/8$ in 13 of 15 conditions (\\S\\ref{sec:generalization}).\nFull calibration details, practical guidance tiers, and method-level breakdown appear in the Appendix.\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01AKJRmtnrUdfdEqaPnvh8bB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
  "old_string": "in the specification curve tradition~\\cite{simonsohn2020specification,bell2022modeling} adapted to the constraints of iterative training analysis",
  "new_string": "in the specification curve~\\cite{simonsohn2020specification} and multi-method early-warning~\\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "a0b80a6e-63a1-44b5-9e89-e7a9be5cd124",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1xrMeiniKoYZJe71Sn8zv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2471,
      "cache_read_input_tokens": 59154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2471
      },
      "output_tokens": 69,
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

_source line 35 · 2026-05-20T11:22:59.483Z_

<details><summary>↩ Tool result · `toolu_01AKJRmtnrUdfdEqaPnvh8bB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "f614c43d-1046-4f21-bfd0-560422eded4d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
    "oldString": "in the specification curve tradition~\\cite{simonsohn2020specification,bell2022modeling} adapted to the constraints of iterative training analysis",
    "newString": "in the specification curve~\\cite{simonsohn2020specification} and multi-method early-warning~\\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\paragraph{Methodological pitfalls.}\n\\label{sec:pitfalls}\nLead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \\S\\ref{sec:regime}--\\ref{sec:dose_response}.\n\\emph{Method sensitivity}: five detection methods applied to identical data ($\\alpha{=}1.0$, 16 canary$\\to$downstream pairs) yield significance rates from 100\\% (naive cross-correlation) to 37.5\\% (permutation Granger), with inter-method agreement at $\\kappa{=}0.185$ and a spurious-signal rate ${\\geq}62.5\\%$.\n\\emph{Spurious regression}: first-differencing to remove shared trends~\\cite{granger1974spurious} eliminates canary$\\to$perplexity associations ($F{\\approx}0$, $p{=}0.99$) while preserving canary$\\to$diversity (24/24$\\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.\n\\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\\alpha{=}0.45$ but 6/8 at $\\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\\alpha$ study would miss entirely.\nThese pitfalls motivate systematic method comparison rather than reliance on any single detection approach.\n\n\\paragraph{Multi-Method Consensus Test (MMCT).}\n\\label{sec:mmct}\nWe apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve tradition~\\cite{simonsohn2020specification,bell2022modeling} adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.\nMMCT is a consensus testing protocol, not a novel statistical method.\nIt compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\\alpha{=}0.0$) data where any detection is a false positive.\nEach method $m_k$ receives weight $w_k = 1/\\max(\\hat{\\text{FPR}}_k, \\epsilon)$ with $\\epsilon{=}0.01$; the weighted score $W(X \\to Y) = \\sum_k w_k d_k / \\sum_k w_k$ yields formal $p$-values from the empirical null distribution (Algorithm~\\ref{alg:mmct}; Appendix).\nMMCT identifies permutation Granger (PermG) as the only method combining zero null-control FPR with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.\n\n\\paragraph{Permutation Granger causality.}\nPermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history; Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\nWe apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 validated canary$\\to$downstream pairs (2 canaries $\\times$ 4 downstream metrics).\nThree properties distinguish PermG: a nonparametric null distribution robust to the short non-stationary series typical of iterative training~\\cite{boettiger2012limits}, built-in directionality (forward and reverse tested separately), and a hyperparameter-free test statistic.\nThe remaining four methods each exhibit a specific limitation: naive cross-correlation has 75\\% null-control FPR; differenced cross-correlation detects bidirectionally without directional separation; threshold onset is power-limited at $T{=}11$ under corrected $3\\sigma$ calibration (0/8 significant in 8 of 12 cross-architecture conditions); Toda--Yamamoto~\\cite{toda1995statistical} achieves moderate supplementary detection (3--4/8 at $\\alpha{\\geq}0.50$) with reduced power from degree-of-freedom costs of lag augmentation.\nPer-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix.\n\n\\subsection{Signal-Times-Resolution Framework}\n\\label{sec:theory}\n\nWe apply standard statistical power scaling to PermG under the Signal$\\times$Resolution (S$\\times$R) framework.\nDetectability of canary$\\to$downstream temporal precedence depends on two competing factors:\n\\begin{equation}\n    \\text{Detectability}(\\alpha) \\;\\propto\\; S(\\alpha) \\times R(\\alpha),\n    \\label{eq:detectability}\n\\end{equation}\nwhere $S(\\alpha)$ is signal strength (magnitude of distributional shift, monotonically increasing with $\\alpha$) and $R(\\alpha)$ is temporal resolution (the generational gap between canary and downstream responses).\n$R(\\alpha)$ is non-monotonic: at low $\\alpha$, entropy and diversity respond in different generations ($R$ large); at $\\alpha{\\approx}0.60$, relaxation time matching compresses both responses into a single generation ($R \\to 0$); at high $\\alpha$, the severity of entropy collapse outpaces the diversity cascade, restoring the generational offset.\nThe product $S \\times R$ predicts four regimes: \\emph{blind} ($\\alpha \\leq 0.45$; $S$ below detection floor), \\emph{onset} ($\\alpha \\approx 0.50$; $S$ crosses threshold while $R$ remains high), \\emph{synchronous dip} ($\\alpha \\approx 0.60$; $R \\to 0$ suppresses detection despite rising $S$), and \\emph{detection} ($\\alpha \\geq 0.75$; $S$ dominates).\nFull empirical confirmation appears in \\S\\ref{sec:regime} and \\S\\ref{sec:dose_response}.\n\nUnder a permutation test framework, detection power scales as $\\mathrm{Power}(\\alpha, T) = \\Phi\\bigl(S \\cdot R \\cdot \\sqrt{T} / \\sigma_{\\mathrm{noise}}\\bigr)$, where $\\Phi$ is the standard normal CDF and the $\\sqrt{T}$ scaling follows standard power analysis.\nThe detection phase transition at $\\alpha_c$ (at $T{=}10$) is consistent with a power threshold: when $S \\cdot R \\cdot \\sqrt{T}$ first exceeds the detection floor, power undergoes a steep onset from near-zero to near-one.\nThis generates three predictions for $T{=}20$: (i)~$\\alpha_c$ left-shifts as increased $T$ raises power at all $\\alpha$; (ii)~the transition smooths as $\\sqrt{T}$ broadens the power curve; (iii)~different methods exhibit different $\\alpha_c$ values due to method-specific power curves.\nThe key falsifiable test is the sub-threshold prediction: the framework predicts 0/8 at $\\alpha{=}0.45$ (at $T{=}10$), confirmed empirically (\\S\\ref{sec:regime}), with sub-threshold FDR $p{=}0.059$--$0.091$ consistent with proximity to the power boundary.\nDetection at $\\alpha{\\geq}0.50$ (predicted ${\\geq}5/8$, CI${=}[5,8]$) serves as supplementary consistency evidence rather than a strong test, as these predictions are near-unfalsifiable given signal strength.\n\n\\paragraph{Calibration.}\nWe validate error rates with built-in experimental controls.\nFalse positive rate: at $\\alpha{=}0.0$ (null control, no synthetic contamination), PermG and MMCT weighted consensus both yield 0\\% FPR across 3 seeds (0/24 pairs at consensus $K{\\geq}3$).\nFalse negative rate: at $\\alpha{=}1.0$, all 6 effect-size reference pairs (2 canaries $\\times$ 3 diversity metrics, selected by criteria independent of the detection methods) are recovered at 0\\% FNR across 4 seeds.\nPermG matches consensus performance at all tested contamination levels, with cross-architecture validation confirming PermG forward significance ${\\geq}6/8$ in 13 of 15 conditions (\\S\\ref{sec:generalization}).\nFull calibration details, practical guidance tiers, and method-level breakdown appear in the Appendix.\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 7,
        "newStart": 11,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Multi-Method Consensus Test (MMCT).}",
          " \\label{sec:mmct}",
          "-We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve tradition~\\cite{simonsohn2020specification,bell2022modeling} adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.",
          "+We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve~\\cite{simonsohn2020specification} and multi-method early-warning~\\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.",
          " MMCT is a consensus testing protocol, not a novel statistical method.",
          " It compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\\alpha{=}0.0$) data where any detection is a false positive.",
          " Each method $m_k$ receives weight $w_k = 1/\\max(\\hat{\\text{FPR}}_k, \\epsilon)$ with $\\epsilon{=}0.01$; the weighted score $W(X \\to Y) = \\sum_k w_k d_k / \\sum_k w_k$ yields formal $p$-values from the empirical null distribution (Algorithm~\\ref{alg:mmct}; Appendix)."
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

_source line 36_

Final verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "f2952155-9cf2-4cce-8026-079c85d28f20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eGvwRpy3QPL8bssQJtGdZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 61625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
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

<details open><summary>🔧 Tool call — Bash · `toolu_01DeGF2FsXcmYd6YBqTy3kdt`</summary>

```json
{
  "command": "echo \"=== Line count ===\" && wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex && echo \"=== Citations ===\" && grep -o 'cite{[^}]*}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex | sort -u && echo \"=== Labels ===\" && grep -o 'label{[^}]*}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex && echo \"=== Cross-refs ===\" && grep -o '\\\\ref{[^}]*}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex | sort -u && echo \"=== Em-dash check ===\" && grep -P '—|—|\\x{2014}' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex || echo \"Clean\" && echo \"=== En-dash check (explanatory) ===\" && grep ' – ' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex || echo \"Clean\"",
  "description": "Final constraint verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "487441ef-b3d5-4712-b5e3-4ae0b872e91b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eGvwRpy3QPL8bssQJtGdZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 61625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
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

_source line 38 · 2026-05-20T11:23:07.076Z_

<details><summary>↩ Tool result · `toolu_01DeGF2FsXcmYd6YBqTy3kdt`</summary>

```text
=== Line count ===
52 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex
=== Citations ===
cite{boettiger2012limits}
cite{granger1974spurious}
cite{scheffer2009early,bell2022modeling}
cite{shojaie2022granger}
cite{simonsohn2020specification}
cite{toda1995statistical}
=== Labels ===
label{sec:method}
label{sec:pitfalls}
label{sec:mmct}
label{sec:theory}
label{eq:detectability}
=== Cross-refs ===
\ref{alg:mmct}
\ref{sec:dose_response}
\ref{sec:generalization}
\ref{sec:regime}
=== Em-dash check ===
Clean
=== En-dash check (explanatory) ===
Clean
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "98c2e6ef-0b3f-4112-a294-51ece443acd3",
  "tool_use_result": {
    "stdout": "=== Line count ===\n52 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex\n=== Citations ===\ncite{boettiger2012limits}\ncite{granger1974spurious}\ncite{scheffer2009early,bell2022modeling}\ncite{shojaie2022granger}\ncite{simonsohn2020specification}\ncite{toda1995statistical}\n=== Labels ===\nlabel{sec:method}\nlabel{sec:pitfalls}\nlabel{sec:mmct}\nlabel{sec:theory}\nlabel{eq:detectability}\n=== Cross-refs ===\n\\ref{alg:mmct}\n\\ref{sec:dose_response}\n\\ref{sec:generalization}\n\\ref{sec:regime}\n=== Em-dash check ===\nClean\n=== En-dash check (explanatory) ===\nClean",
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

_source line 39_

Written to `docs/paper/method_reframe.tex`. 52 source lines (dense, one-sentence-per-line format; will typeset to ~65-70 lines in dual-column).

**Structure**: Pitfalls (10 lines) → MMCT (10) → PermG (13) → S×R subsection with equation (18) → Calibration (8). No display items (tables/figures/algorithms all deferred to Appendix).

**Constraints verified**:
- All 7 required citations present
- All 5 required labels preserved (`sec:method`, `sec:pitfalls`, `sec:mmct`, `sec:theory`, `eq:detectability`)
- Zero em-dashes, zero explanatory en-dashes
- No -ing endings, no banned transition words, no AI vocabulary
- D131 ("steep onset", "detection phase transition"), D141 (α_c qualified "at T=10", "consistent with"), D142 (no CSD), D143 (no TY=7/8), M037 (PermG-only dose-response), C2 positioning, predict-then-verify framing all satisfied
- Reproducibility: 5,000 permutations, BH-FDR q=0.05, 8 pairs in main text

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "uuid": "1af4753f-dc23-4a37-a34f-d7ed44266528",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYgk2KtGSui9k4QVnCvvTb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 61908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 704
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

_source line 40_

Written to `docs/paper/method_reframe.tex`. 52 source lines (dense, one-sentence-per-line format; will typeset to ~65-70 lines in dual-column).

**Structure**: Pitfalls (10 lines) → MMCT (10) → PermG (13) → S×R subsection with equation (18) → Calibration (8). No display items (tables/figures/algorithms all deferred to Appendix).

**Constraints verified**:
- All 7 required citations present
- All 5 required labels preserved (`sec:method`, `sec:pitfalls`, `sec:mmct`, `sec:theory`, `eq:detectability`)
- Zero em-dashes, zero explanatory en-dashes
- No -ing endings, no banned transition words, no AI vocabulary
- D131 ("steep onset", "detection phase transition"), D141 (α_c qualified "at T=10", "consistent with"), D142 (no CSD), D143 (no TY=7/8), M037 (PermG-only dose-response), C2 positioning, predict-then-verify framing all satisfied
- Reproducibility: 5,000 permutations, BH-FDR q=0.05, 8 pairs in main text

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 255804,
  "duration_api_ms": 254728,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "ca9818b0-6b73-4292-8f2d-7e752a5b3184",
  "total_cost_usd": 0.89636575,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 50771,
    "cache_read_input_tokens": 487672,
    "output_tokens": 13252,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 50771,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 308,
        "cache_read_input_tokens": 61908,
        "cache_creation_input_tokens": 704,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 704
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3736,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0038510000000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 13252,
      "cacheReadInputTokens": 487672,
      "cacheCreationInputTokens": 50771,
      "webSearchRequests": 0,
      "costUSD": 0.8925147500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b98bcbed-aa7f-4cd9-bb66-0b24f355278a"
}
```

</details>

---
