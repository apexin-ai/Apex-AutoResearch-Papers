# paper writing method

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_paper_writing_method_20260523T005243.log`
- **Structured JSON:** [`af94d5aa572b91bf43fb.json`](../../sessions/af/af94d5aa572b91bf43fb.json)

## Before a recorded user message

49 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
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
  "uuid": "5f97627f-30b8-4cb0-95bd-fe66176e9aed",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779513000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2aba7286-3937-40d7-afb5-fcf647187ef7",
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and project context, then write the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "e0d8c0f2-a710-4707-a594-abdd09bd6ecb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8edxxNTdPiqJbwpD34sJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12683,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12683
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

<details open><summary>🔧 Tool call — Read · `toolu_0155TiFFwijiCvwEmLcTLjRz`</summary>

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
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "e8786fe7-6eab-4868-b224-6527f99fd21d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8edxxNTdPiqJbwpD34sJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12683,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12683
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

_source line 6 · 2026-05-23T00:52:57.214Z_

<details><summary>↩ Tool result · `toolu_0155TiFFwijiCvwEmLcTLjRz`</summary>

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
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "8c80bec6-e246-464e-8096-12c695e447b3",
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

<details open><summary>🔧 Tool call — Read · `toolu_011XzsKsXDSh8w99VHcAYjbn`</summary>

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
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "5749167b-20b5-4d8a-b0b3-cc3ad9d123be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8edxxNTdPiqJbwpD34sJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12683,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12683
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

_source line 8 · 2026-05-23T00:52:57.740Z_

<details><summary>↩ Tool result · `toolu_011XzsKsXDSh8w99VHcAYjbn`</summary>

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
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "1a8cb243-adc4-418d-b8a4-63a46fe5e9a0",
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

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01JQSsbgc8cFXviqMt4UmAKA`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "84ea25d0-badc-4b7f-8634-36da8c7989e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8edxxNTdPiqJbwpD34sJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12683,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12683
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

_source line 10 · 2026-05-23T00:52:59.564Z_

<details><summary>↩ Tool result · `toolu_01JQSsbgc8cFXviqMt4UmAKA`</summary>

```text
docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/discussion.tex
docs/paper/background.tex
docs/paper/results_v2.tex
docs/paper/introduction.tex
docs/paper/experimental_setup.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/analysis.tex
docs/paper/results.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "e5911ccf-7e78-4182-bf30-a55f734817bc",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/background.tex",
      "docs/paper/sections/experimental_setup.tex",
      "docs/paper/sections/results_draft.tex",
      "docs/paper/sections/analysis_draft.tex",
      "docs/paper/experiments_deprecated.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/related_work_draft.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/discussion.tex",
      "docs/paper/background.tex",
      "docs/paper/results_v2.tex",
      "docs/paper/introduction.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/related_work.tex",
      "docs/paper/abstract.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/analysis.tex",
      "docs/paper/results.tex",
      "docs/paper/appendix.tex",
      "docs/paper/main.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 27,
    "numFiles": 22,
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
Let me check existing paper files to understand the style and any existing method-related content, and also check the experiments.tex to see what references it makes to the method section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "c2371c67-7fd3-4b79-bfd8-0289c82af9e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016deNbdXtWueHcGzPMoqWyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 24524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

Let me check the existing paper files for style reference and cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "f8f51ffe-f1f7-484a-8b28-75420abe6bf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016deNbdXtWueHcGzPMoqWyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 24524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

<details open><summary>🔧 Tool call — Read · `toolu_01RATTZHo7RYXzAVm6ioM6Eb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "4fbc5632-d299-4fc2-90ad-dda7dc6e266f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016deNbdXtWueHcGzPMoqWyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 24524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

_source line 14 · 2026-05-23T00:53:05.499Z_

<details><summary>↩ Tool result · `toolu_01RATTZHo7RYXzAVm6ioM6Eb`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA models spanning three connector families on the LIBERO benchmark~\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.
8	
9	Four models are evaluated in closed-loop robotic control: $\pi_0.5$~\cite{black2025pi05} (4B parameters, linear projection with $\times\!\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\cite{lewis2020bart}, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$ folding, 128 tokens, CV$\,{=}\,$0.314). Two additional models are analyzed via offline metrics only: $\pi_0$~\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\,{=}\,$0.038) and OFT~\cite{kim2025openoft} (7B, MLP projector, 512 tokens, CV$\,{=}\,$0.219). Table~\ref{tab:model_properties} summarizes model properties and connector details.
10	
11	The pruning protocol applies post-connector token pruning at retention ratios $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$. Two strategies bracket the robustness range: \textbf{L2 norm selection} ranks tokens by L2 norm and retains the top-$k$ fraction, providing an importance-based favorable test; \textbf{random subsampling} selects tokens uniformly at random, providing a conservative lower bound. Both strategies physically remove tokens and re-index position IDs. All results report mean success rate (SR) over 500 episodes with Wilson 95\% confidence intervals for single-seed conditions.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	The pruning response of a VLA model depends on two axes: the degree of token independence imposed by the vision connector, and the complexity of the downstream manipulation task. Models with token-independent connectors (MLP projectors, linear projections without deep post-processing) degrade gracefully under pruning, while models with token-entangling connectors exhibit sharp, task-dependent collapse. Figure~\ref{fig:teaser} illustrates this two-axis structure.
17	
18	Table~\ref{tab:main_results} presents closed-loop success rates across four models, four LIBERO suites, two pruning methods, and four retention ratios. The data reveal four qualitatively distinct response patterns spanning the connector spectrum (Figure~\ref{fig:pruning_overview}).
19	
20	\textbf{$\pi_0.5$ (linear, CV$\,{=}\,$0.055).} On Object, L2 norm selection yields 98.2\% at $k{=}0.95$, 98.2\% at $k{=}0.9$, and 98.0\% at $k{=}0.85$ (a plateau within 0.2\,pp of the 98.2\% baseline), then drops sharply to 55.0\% at $k{=}0.7$. Random selection follows a different trajectory: 69.4\% at $k{=}0.95$, 10.8\% at $k{=}0.9$, 75.5\% at $k{=}0.7$, and 68.9\% at $k{=}0.5$. The low CV implies near-uniform token norms, and the method choice produces gaps as large as 87.4\,pp (at $k{=}0.9$). On Spatial, $\pi_0.5$ maintains 97.8\% at $k{=}0.95$ (L2) and degrades to 56.9\% at $k{=}0.5$ (L2) versus 71.6\% (random). The pattern is consistent: low-CV models are not pruning-immune but uniformly critical, where the choice of which tokens to remove matters more than the number removed.
21	
22	\textbf{X-VLA (linear + BART encoder, CV$\,{=}\,$0.151).} X-VLA exhibits threshold-graded behavior with a pronounced interaction between retention ratio and task complexity. On Object, L2 norm selection preserves 99.0\% at $k{=}0.95$ and 97.6\% at $k{=}0.9$, then falls sharply to 68.0\% at $k{=}0.85$ with non-monotonic recovery to 89.0\% at $k{=}0.8$ before continued decline to 56.2\% at $k{=}0.7$. The same model at the same $k{=}0.9$ achieves only 70.2\% on Goal, a 27.8\,pp difference driven entirely by task complexity. On Long, removing just 3 of 50 tokens ($k{=}0.95$) collapses SR from 94.0\% to 47.0\%. The 12-layer BART encoder creates cross-token dependencies that amplify under compositional task demands.
23	
24	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA degrades smoothly across all retention ratios on Object: 70.6\% (L2) and 69.2\% (random) at $k{=}0.95$, 62.0\% and 63.4\% at $k{=}0.9$, 49.0\% and 48.5\% at $k{=}0.7$, 37.4\% and 35.7\% at $k{=}0.5$. The near-zero method gap (within 2\,pp at all retention ratios) reflects the MLP projector's per-patch independence: with a genuine importance gradient (CV$\,{=}\,$0.215), L2 norm ranking and random selection yield comparable spatial coverage. Degradation is proportional to the fraction removed, with no threshold effects.
25	
26	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} SmolVLA collapses to 0.0\% SR at every retention ratio across all four suites and both pruning methods, including $k{=}0.95$ where only 6 of 128 tokens are removed. This catastrophic cliff is detailed in Section~\ref{sec:pixel_shuffle}.
27	
28	\begin{table*}[t]
29	\centering
30	\small
31	\caption{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning at four retention ratios. Best result per row in \textbf{bold}. SmolVLA collapses to 0.0\% across all conditions. ``--'' indicates data not yet collected.}
32	\label{tab:main_results}
33	\begin{tabular}{llccccc}
34	\toprule
35	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
36	\midrule
37	\multirow{4}{*}{$\pi_0.5$}
38	& Object  & \textbf{98.2} & 98.2 / 69.4 & \textbf{98.2} / 10.8 & 55.0 / 75.5 & 33.4 / 68.9 \\
39	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.6 & 95.0 / 54.1 & 67.7 / 74.1 & 56.9 / 71.6 \\
40	& Goal    & \textbf{96.4} & 89.4 / -- & 90.0 / -- & -- / 80.6 & 59.2 / 74.4 \\
41	& Long    & \textbf{91.6} & -- / 61.2 & 81.0 / 31.8 & 60.0 / 64.6 & 50.2 / 50.2 \\
42	\midrule
43	\multirow{4}{*}{X-VLA}
44	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 42.6 / 70.6 \\
45	& Spatial & \textbf{91.6} & 71.6 / -- & 78.8 / -- & 72.0 / -- & 58.8 / 71.4 \\
46	& Goal    & \textbf{98.0} & 53.8 / -- & 70.2 / -- & 53.4 / -- & 61.0 / -- \\
47	& Long    & \textbf{94.0} & 47.0 / -- & 27.5 / -- & -- / -- & -- / -- \\
48	\midrule
49	OpenVLA & Object & \textbf{74.0} & 70.6 / 69.2 & 62.0 / 63.4 & 49.0 / 48.5 & 37.4 / 35.7 \\
50	\midrule
51	\multirow{4}{*}{SmolVLA}
52	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
53	& Spatial & \textbf{44.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
54	& Goal    & \textbf{60.8} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
55	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
56	\bottomrule
57	\end{tabular}
58	\end{table*}
59	
60	\subsection{Pixel-Shuffle Entanglement}
61	\label{sec:pixel_shuffle}
62	
63	SmolVLA's pixel-shuffle connector applies $4{\times}4$ spatial folding, concatenating 16 contiguous patches into the channel dimension of a single token. This operation creates irreversible cross-token spatial dependencies: each token encodes a $4{\times}4$ receptive field, and removing any token eliminates information from all 16 constituent patches with no redundancy in the remaining tokens.
64	
65	The consequence is catastrophic. SmolVLA collapses to 0.0\% SR at $k{=}0.95$ (removing 6 of 128 tokens, a 5\% reduction) across all four LIBERO suites (Object, Spatial, Goal, Long) and both pruning methods (L2 norm and random). We verified this result on two independent checkpoints: our LoRA fine-tuned reproduction (44.8\% SR baseline) and the official SmolVLA checkpoint (59.2\% SR baseline). Both exhibit identical collapse. The cliff is architectural, not a training artifact.
66	
67	The pixel-shuffle mechanism explains why the collapse is method-independent. Because all tokens carry spatially entangled information from non-overlapping $4{\times}4$ grids, no scoring function can identify ``dispensable'' tokens. L2 norm ranking and random selection fail equally because the problem is not which tokens are removed but that any removal breaks the spatial completeness the downstream LLM requires. In contrast, MLP projectors (OpenVLA) and linear projections ($\pi_0.5$) map patches independently. Each token retains per-patch spatial locality, so partial removal does not destroy information from unrelated spatial positions.
68	
69	\subsection{When Does Pruning Method Matter? CV as Sensitivity Indicator}
70	\label{sec:cv_sensitivity}
71	
72	Token importance CV (coefficient of variation of L2 norms) correlates with the retention ratio at which the choice of pruning method becomes critical. At mild pruning ($k{=}0.95$), a clear pattern emerges across the three closed-loop models with distinct CV values.
73	
74	For $\pi_0.5$ (CV$\,{=}\,$0.055), the method gap at $k{=}0.95$ is substantial: 98.2\% (L2) versus 69.4\% (random) on Object, a 28.8\,pp difference. On Spatial, the gap is 21.4\,pp (97.8\% vs.\ 76.6\%). The near-uniform token norms cause L2 norm ranking to exploit small spatial correlations rather than genuine importance differences, while random selection preserves the uniform spatial coverage these models depend on.
75	
76	For X-VLA (CV$\,{=}\,$0.151), the method gap at $k{=}0.95$ is minimal on Object (0.2\,pp; Table~\ref{tab:main_results}). Multi-seed evaluation across suites yields an average gap of 1.2\,pp. The BART encoder produces tokens with a moderate importance gradient that both methods preserve at this mild pruning level.
77	
78	For OpenVLA (CV$\,{=}\,$0.215), the method gap at $k{=}0.95$ is 1.4\,pp on Object (70.6\% vs.\ 69.2\%). The MLP projector creates a clear importance hierarchy that renders both selection strategies nearly equivalent.
79	
80	The contrast is stark: $\pi_0.5$ exhibits a 28.8\,pp method gap where X-VLA and OpenVLA show gaps below 1.5\,pp. Low-CV models are an order of magnitude more sensitive to pruning method choice than higher-CV models at mild retention ratios. Figure~\ref{fig:method_gap} visualizes this relationship.
81	
82	At aggressive compression ($k{=}0.5$), the method-independence observed in moderate-CV models breaks down. On Object, the gap $\Delta$(R$-$L2) scales monotonically with CV: $\pi_0.5$ shows $+$35.5\,pp (random: 68.9\%, L2: 33.4\%), X-VLA shows $+$28.0\,pp (random: 70.6\%, L2: 42.6\%), and OpenVLA shows $-$1.7\,pp (random: 35.7\%, L2: 37.4\%). At 50\% retention, random selection outperforms L2 norm selection for both low-CV and moderate-CV models because random sampling preserves spatial diversity, while L2 norm ranking selects correlated high-norm tokens that cluster in similar image regions. Only OpenVLA, with CV above 0.2, produces a genuine importance gradient that L2 can exploit without spatial clustering artifacts.
83	
84	\subsection{Cross-Suite Task Complexity Effects}
85	\label{sec:cross_suite}
86	
87	LIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.
88	
89	$\pi_0.5$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\% (matching the baseline), Spatial retains 97.8\% (within noise of the 97.2\% baseline), and Goal drops to 89.4\% ($-$7.0\,pp from 96.4\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\% token removal.
90	
91	X-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 97.6\% ($-$1.6\,pp from the 99.2\% baseline), while Goal drops to 70.2\% ($-$27.8\,pp). The degradation factor between suites is 17$\times$ (27.8 / 1.6), driven entirely by task complexity with the same model, same retention ratio, and same pruning method. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\% to 47.0\%, a 47.0\,pp loss, while Object at the same ratio loses only 0.2\,pp.
92	
93	Token-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\pi_0.5$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.
94	
95	\subsection{VTR Recovery}
96	\label{sec:vtr_recovery}
97	
98	Vision Token Re-encoder (VTR) addresses the catastrophic cliff through learned re-encoding rather than hard deletion. VTR inserts a lightweight cross-attention module ($\sim$22M parameters, approximately 5\% of SmolVLA) between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over the full set of 128 source tokens and produce $M$ compressed output representations, where $M \in \{16, 32, 64, 96, 128\}$. The $M{=}128$ configuration serves as a passthrough control that re-encodes without compressing.
99	
100	Table~\ref{tab:vtr_results} reports VTR results on SmolVLA for LIBERO-Object (3 seeds, 500 episodes each). Cross-attention VTR recovers substantial performance where hard pruning yields 0.0\%: $M{=}16$ (87.5\% compression) achieves 56.9 $\pm$ 1.3\%, $M{=}32$ (75\%) achieves 60.1 $\pm$ 1.3\%, $M{=}64$ (50\%) achieves 62.0 $\pm$ 2.2\%, $M{=}96$ (25\%) achieves 54.5 $\pm$ 3.2\%, and $M{=}128$ (0\%, passthrough) achieves 58.0 $\pm$ 3.5\%. The SmolVLA-Base (LoRA fine-tuned) baseline without VTR is 44.8\%, and the official SmolVLA baseline is 59.2\%.
101	
102	\begin{table}[t]
103	\centering
104	\small
105	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (passthrough) within 1.1\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}
106	\label{tab:vtr_results}
107	\begin{tabular}{lccr}
108	\toprule
109	Configuration & $M$ & Compression & SR (\%) \\
110	\midrule
111	\textit{SmolVLA-Base (LoRA)} & 128 & 0\% & 44.8 \\
112	\textit{SmolVLA official} & 128 & 0\% & 59.2 \\
113	\textit{Baseline control (+100K steps)} & 128 & 0\% & 45.0 \\
114	\textit{Hard pruning (any $k$)} & -- & 5--50\% & 0.0 \\
115	\midrule
116	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
117	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
118	Cross-attn VTR & 64 & 50\% & \textbf{62.0 $\pm$ 2.2} \\
119	Cross-attn VTR & 96 & 25\% & 54.5 $\pm$ 3.2 \\
120	Cross-attn VTR & 128 & 0\% & 58.0 $\pm$ 3.5 \\
121	\midrule
122	MLP adapter ($\sim$22M) & 32 & 75\% & 63.4 $\pm$ 2.6 \\
123	\bottomrule
124	\end{tabular}
125	\end{table}
126	
127	The M-curve is notably flat: performance at $M{=}16$ (56.9\%) falls within 1.1\,pp of $M{=}128$ (58.0\%), and all five $M$ values cluster within a 7.5\,pp range. This flatness confirms that the operative factor is learned re-encoding of spatially entangled tokens, not the compression ratio itself. The VTR module transforms pixel-shuffle representations into a format the downstream LLM can process robustly, and this transformation is effective regardless of how many output tokens carry the result.
128	
129	A parameter-matched MLP adapter ($\sim$22M parameters) achieves 63.4 $\pm$ 2.6\% at $M{=}32$, comparable to cross-attention VTR ($p = 0.15$). This confirms that re-encoding itself, rather than the specific attention mechanism, is the key architectural intervention. The baseline control (100K additional training steps without the compressor module) achieves only 45.0\% SR, within 0.2\,pp of the 44.8\% baseline. The performance gain is therefore attributable to the VTR architecture, not to additional optimization.
130	
131	Cross-suite evaluation at $M{=}32$ confirms that VTR recovery generalizes beyond Object: Spatial achieves 53.2\% and Goal achieves 56.4\%, both recovered from 0.0\% under hard pruning. VTR provides a targeted remedy for pixel-shuffle entanglement. By breaking the spatial dependencies that make hard deletion catastrophic, VTR enables both re-encoding recovery and downstream token reduction for deployment efficiency.
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "067df9e1-8f7c-4e33-b4fa-c72dd5152e45",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\nWe evaluate vision token pruning across six VLA models spanning three connector families on the LIBERO benchmark~\\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.\n\nFour models are evaluated in closed-loop robotic control: $\\pi_0.5$~\\cite{black2025pi05} (4B parameters, linear projection with $\\times\\!\\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\\cite{lewis2020bart}, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$ folding, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models are analyzed via offline metrics only: $\\pi_0$~\\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\\,{=}\\,$0.038) and OFT~\\cite{kim2025openoft} (7B, MLP projector, 512 tokens, CV$\\,{=}\\,$0.219). Table~\\ref{tab:model_properties} summarizes model properties and connector details.\n\nThe pruning protocol applies post-connector token pruning at retention ratios $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$. Two strategies bracket the robustness range: \\textbf{L2 norm selection} ranks tokens by L2 norm and retains the top-$k$ fraction, providing an importance-based favorable test; \\textbf{random subsampling} selects tokens uniformly at random, providing a conservative lower bound. Both strategies physically remove tokens and re-index position IDs. All results report mean success rate (SR) over 500 episodes with Wilson 95\\% confidence intervals for single-seed conditions.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\nThe pruning response of a VLA model depends on two axes: the degree of token independence imposed by the vision connector, and the complexity of the downstream manipulation task. Models with token-independent connectors (MLP projectors, linear projections without deep post-processing) degrade gracefully under pruning, while models with token-entangling connectors exhibit sharp, task-dependent collapse. Figure~\\ref{fig:teaser} illustrates this two-axis structure.\n\nTable~\\ref{tab:main_results} presents closed-loop success rates across four models, four LIBERO suites, two pruning methods, and four retention ratios. The data reveal four qualitatively distinct response patterns spanning the connector spectrum (Figure~\\ref{fig:pruning_overview}).\n\n\\textbf{$\\pi_0.5$ (linear, CV$\\,{=}\\,$0.055).} On Object, L2 norm selection yields 98.2\\% at $k{=}0.95$, 98.2\\% at $k{=}0.9$, and 98.0\\% at $k{=}0.85$ (a plateau within 0.2\\,pp of the 98.2\\% baseline), then drops sharply to 55.0\\% at $k{=}0.7$. Random selection follows a different trajectory: 69.4\\% at $k{=}0.95$, 10.8\\% at $k{=}0.9$, 75.5\\% at $k{=}0.7$, and 68.9\\% at $k{=}0.5$. The low CV implies near-uniform token norms, and the method choice produces gaps as large as 87.4\\,pp (at $k{=}0.9$). On Spatial, $\\pi_0.5$ maintains 97.8\\% at $k{=}0.95$ (L2) and degrades to 56.9\\% at $k{=}0.5$ (L2) versus 71.6\\% (random). The pattern is consistent: low-CV models are not pruning-immune but uniformly critical, where the choice of which tokens to remove matters more than the number removed.\n\n\\textbf{X-VLA (linear + BART encoder, CV$\\,{=}\\,$0.151).} X-VLA exhibits threshold-graded behavior with a pronounced interaction between retention ratio and task complexity. On Object, L2 norm selection preserves 99.0\\% at $k{=}0.95$ and 97.6\\% at $k{=}0.9$, then falls sharply to 68.0\\% at $k{=}0.85$ with non-monotonic recovery to 89.0\\% at $k{=}0.8$ before continued decline to 56.2\\% at $k{=}0.7$. The same model at the same $k{=}0.9$ achieves only 70.2\\% on Goal, a 27.8\\,pp difference driven entirely by task complexity. On Long, removing just 3 of 50 tokens ($k{=}0.95$) collapses SR from 94.0\\% to 47.0\\%. The 12-layer BART encoder creates cross-token dependencies that amplify under compositional task demands.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA degrades smoothly across all retention ratios on Object: 70.6\\% (L2) and 69.2\\% (random) at $k{=}0.95$, 62.0\\% and 63.4\\% at $k{=}0.9$, 49.0\\% and 48.5\\% at $k{=}0.7$, 37.4\\% and 35.7\\% at $k{=}0.5$. The near-zero method gap (within 2\\,pp at all retention ratios) reflects the MLP projector's per-patch independence: with a genuine importance gradient (CV$\\,{=}\\,$0.215), L2 norm ranking and random selection yield comparable spatial coverage. Degradation is proportional to the fraction removed, with no threshold effects.\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} SmolVLA collapses to 0.0\\% SR at every retention ratio across all four suites and both pruning methods, including $k{=}0.95$ where only 6 of 128 tokens are removed. This catastrophic cliff is detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning at four retention ratios. Best result per row in \\textbf{bold}. SmolVLA collapses to 0.0\\% across all conditions. ``--'' indicates data not yet collected.}\n\\label{tab:main_results}\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_0.5$}\n& Object  & \\textbf{98.2} & 98.2 / 69.4 & \\textbf{98.2} / 10.8 & 55.0 / 75.5 & 33.4 / 68.9 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.6 & 95.0 / 54.1 & 67.7 / 74.1 & 56.9 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / -- & 90.0 / -- & -- / 80.6 & 59.2 / 74.4 \\\\\n& Long    & \\textbf{91.6} & -- / 61.2 & 81.0 / 31.8 & 60.0 / 64.6 & 50.2 / 50.2 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 42.6 / 70.6 \\\\\n& Spatial & \\textbf{91.6} & 71.6 / -- & 78.8 / -- & 72.0 / -- & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.0} & 53.8 / -- & 70.2 / -- & 53.4 / -- & 61.0 / -- \\\\\n& Long    & \\textbf{94.0} & 47.0 / -- & 27.5 / -- & -- / -- & -- / -- \\\\\n\\midrule\nOpenVLA & Object & \\textbf{74.0} & 70.6 / 69.2 & 62.0 / 63.4 & 49.0 / 48.5 & 37.4 / 35.7 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\nSmolVLA's pixel-shuffle connector applies $4{\\times}4$ spatial folding, concatenating 16 contiguous patches into the channel dimension of a single token. This operation creates irreversible cross-token spatial dependencies: each token encodes a $4{\\times}4$ receptive field, and removing any token eliminates information from all 16 constituent patches with no redundancy in the remaining tokens.\n\nThe consequence is catastrophic. SmolVLA collapses to 0.0\\% SR at $k{=}0.95$ (removing 6 of 128 tokens, a 5\\% reduction) across all four LIBERO suites (Object, Spatial, Goal, Long) and both pruning methods (L2 norm and random). We verified this result on two independent checkpoints: our LoRA fine-tuned reproduction (44.8\\% SR baseline) and the official SmolVLA checkpoint (59.2\\% SR baseline). Both exhibit identical collapse. The cliff is architectural, not a training artifact.\n\nThe pixel-shuffle mechanism explains why the collapse is method-independent. Because all tokens carry spatially entangled information from non-overlapping $4{\\times}4$ grids, no scoring function can identify ``dispensable'' tokens. L2 norm ranking and random selection fail equally because the problem is not which tokens are removed but that any removal breaks the spatial completeness the downstream LLM requires. In contrast, MLP projectors (OpenVLA) and linear projections ($\\pi_0.5$) map patches independently. Each token retains per-patch spatial locality, so partial removal does not destroy information from unrelated spatial positions.\n\n\\subsection{When Does Pruning Method Matter? CV as Sensitivity Indicator}\n\\label{sec:cv_sensitivity}\n\nToken importance CV (coefficient of variation of L2 norms) correlates with the retention ratio at which the choice of pruning method becomes critical. At mild pruning ($k{=}0.95$), a clear pattern emerges across the three closed-loop models with distinct CV values.\n\nFor $\\pi_0.5$ (CV$\\,{=}\\,$0.055), the method gap at $k{=}0.95$ is substantial: 98.2\\% (L2) versus 69.4\\% (random) on Object, a 28.8\\,pp difference. On Spatial, the gap is 21.4\\,pp (97.8\\% vs.\\ 76.6\\%). The near-uniform token norms cause L2 norm ranking to exploit small spatial correlations rather than genuine importance differences, while random selection preserves the uniform spatial coverage these models depend on.\n\nFor X-VLA (CV$\\,{=}\\,$0.151), the method gap at $k{=}0.95$ is minimal on Object (0.2\\,pp; Table~\\ref{tab:main_results}). Multi-seed evaluation across suites yields an average gap of 1.2\\,pp. The BART encoder produces tokens with a moderate importance gradient that both methods preserve at this mild pruning level.\n\nFor OpenVLA (CV$\\,{=}\\,$0.215), the method gap at $k{=}0.95$ is 1.4\\,pp on Object (70.6\\% vs.\\ 69.2\\%). The MLP projector creates a clear importance hierarchy that renders both selection strategies nearly equivalent.\n\nThe contrast is stark: $\\pi_0.5$ exhibits a 28.8\\,pp method gap where X-VLA and OpenVLA show gaps below 1.5\\,pp. Low-CV models are an order of magnitude more sensitive to pruning method choice than higher-CV models at mild retention ratios. Figure~\\ref{fig:method_gap} visualizes this relationship.\n\nAt aggressive compression ($k{=}0.5$), the method-independence observed in moderate-CV models breaks down. On Object, the gap $\\Delta$(R$-$L2) scales monotonically with CV: $\\pi_0.5$ shows $+$35.5\\,pp (random: 68.9\\%, L2: 33.4\\%), X-VLA shows $+$28.0\\,pp (random: 70.6\\%, L2: 42.6\\%), and OpenVLA shows $-$1.7\\,pp (random: 35.7\\%, L2: 37.4\\%). At 50\\% retention, random selection outperforms L2 norm selection for both low-CV and moderate-CV models because random sampling preserves spatial diversity, while L2 norm ranking selects correlated high-norm tokens that cluster in similar image regions. Only OpenVLA, with CV above 0.2, produces a genuine importance gradient that L2 can exploit without spatial clustering artifacts.\n\n\\subsection{Cross-Suite Task Complexity Effects}\n\\label{sec:cross_suite}\n\nLIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.\n\n$\\pi_0.5$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\\% (matching the baseline), Spatial retains 97.8\\% (within noise of the 97.2\\% baseline), and Goal drops to 89.4\\% ($-$7.0\\,pp from 96.4\\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\\% token removal.\n\nX-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 97.6\\% ($-$1.6\\,pp from the 99.2\\% baseline), while Goal drops to 70.2\\% ($-$27.8\\,pp). The degradation factor between suites is 17$\\times$ (27.8 / 1.6), driven entirely by task complexity with the same model, same retention ratio, and same pruning method. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\\% to 47.0\\%, a 47.0\\,pp loss, while Object at the same ratio loses only 0.2\\,pp.\n\nToken-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\\pi_0.5$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVision Token Re-encoder (VTR) addresses the catastrophic cliff through learned re-encoding rather than hard deletion. VTR inserts a lightweight cross-attention module ($\\sim$22M parameters, approximately 5\\% of SmolVLA) between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over the full set of 128 source tokens and produce $M$ compressed output representations, where $M \\in \\{16, 32, 64, 96, 128\\}$. The $M{=}128$ configuration serves as a passthrough control that re-encodes without compressing.\n\nTable~\\ref{tab:vtr_results} reports VTR results on SmolVLA for LIBERO-Object (3 seeds, 500 episodes each). Cross-attention VTR recovers substantial performance where hard pruning yields 0.0\\%: $M{=}16$ (87.5\\% compression) achieves 56.9 $\\pm$ 1.3\\%, $M{=}32$ (75\\%) achieves 60.1 $\\pm$ 1.3\\%, $M{=}64$ (50\\%) achieves 62.0 $\\pm$ 2.2\\%, $M{=}96$ (25\\%) achieves 54.5 $\\pm$ 3.2\\%, and $M{=}128$ (0\\%, passthrough) achieves 58.0 $\\pm$ 3.5\\%. The SmolVLA-Base (LoRA fine-tuned) baseline without VTR is 44.8\\%, and the official SmolVLA baseline is 59.2\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (passthrough) within 1.1\\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}\n\\label{tab:vtr_results}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compression & SR (\\%) \\\\\n\\midrule\n\\textit{SmolVLA-Base (LoRA)} & 128 & 0\\% & 44.8 \\\\\n\\textit{SmolVLA official} & 128 & 0\\% & 59.2 \\\\\n\\textit{Baseline control (+100K steps)} & 128 & 0\\% & 45.0 \\\\\n\\textit{Hard pruning (any $k$)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 64 & 50\\% & \\textbf{62.0 $\\pm$ 2.2} \\\\\nCross-attn VTR & 96 & 25\\% & 54.5 $\\pm$ 3.2 \\\\\nCross-attn VTR & 128 & 0\\% & 58.0 $\\pm$ 3.5 \\\\\n\\midrule\nMLP adapter ($\\sim$22M) & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe M-curve is notably flat: performance at $M{=}16$ (56.9\\%) falls within 1.1\\,pp of $M{=}128$ (58.0\\%), and all five $M$ values cluster within a 7.5\\,pp range. This flatness confirms that the operative factor is learned re-encoding of spatially entangled tokens, not the compression ratio itself. The VTR module transforms pixel-shuffle representations into a format the downstream LLM can process robustly, and this transformation is effective regardless of how many output tokens carry the result.\n\nA parameter-matched MLP adapter ($\\sim$22M parameters) achieves 63.4 $\\pm$ 2.6\\% at $M{=}32$, comparable to cross-attention VTR ($p = 0.15$). This confirms that re-encoding itself, rather than the specific attention mechanism, is the key architectural intervention. The baseline control (100K additional training steps without the compressor module) achieves only 45.0\\% SR, within 0.2\\,pp of the 44.8\\% baseline. The performance gain is therefore attributable to the VTR architecture, not to additional optimization.\n\nCross-suite evaluation at $M{=}32$ confirms that VTR recovery generalizes beyond Object: Spatial achieves 53.2\\% and Goal achieves 56.4\\%, both recovered from 0.0\\% under hard pruning. VTR provides a targeted remedy for pixel-shuffle entanglement. By breaking the spatial dependencies that make hard deletion catastrophic, VTR enables both re-encoding recovery and downstream token reduction for deployment efficiency.\n",
      "numLines": 132,
      "startLine": 1,
      "totalLines": 132
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_0196W2iqheJSADWukL2Le7ST`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "dae2dfa0-d9fb-49b7-bcba-0df15d7546da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016deNbdXtWueHcGzPMoqWyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 24524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

_source line 16 · 2026-05-23T00:53:05.883Z_

<details><summary>↩ Tool result · `toolu_0196W2iqheJSADWukL2Le7ST`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
7	\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence). The connector design is strongly associated with token compressibility.}
8	\label{fig:architecture}
9	\end{figure}
10	
11	Vision token pruning reliably accelerates Vision Transformers with negligible accuracy loss~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}. Vision-Language-Action (VLA) models~\cite{kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders and produce hundreds of vision tokens that dominate the language backbone's input, making token reduction attractive for real-time robotic control at 5--10\,Hz. Yet applying pruning to VLAs yields wildly inconsistent results: SmolVLA~\cite{shukor2025smolvla} collapses to 0\% task success at 5\% token removal, while $\pi_0$~\cite{black2024pi0} shows a 2.4\% \emph{improvement} in offline action loss at 90\% removal (offline metrics only; no closed-loop evaluation available). No existing work explains which outcome a given architecture will produce.
12	
13	The critical architectural variable is the vision connector that transforms ViT patches into tokens for the language backbone. Pixel-shuffle connectors~\cite{shukor2025smolvla,chen2024internvl} fold spatial patches so each token encodes a $4{\times}4$ receptive field. MLP projectors~\cite{liu2023llava,kim2024openvla} map patches independently through learned nonlinearities. Linear projections~\cite{black2024pi0,black2025pi05} apply a single matrix multiplication. Recent VLA-specific works~\cite{chen2024fastv,xu2025vlacache,cheng2026vlaiap} evaluate individual architectures without testing whether pruning behaves consistently across connector designs (Figure~\ref{fig:architecture}). Unlike static benchmarks, robotic manipulation compounds errors across timesteps, making compression failures far more consequential.
14	
15	We study vision token pruning across seven VLA models (450M--7B) spanning three connector families on LIBERO~\cite{liu2023libero}, evaluating four in closed-loop and analyzing three via offline metrics or literature. The vision connector is strongly associated with pruning behavior along a four-class spectrum, and the coefficient of variation (CV) of token L2 norms correlates with both the tolerance class and the optimal strategy from a single forward pass. A central finding: low-CV models are not immune to pruning but \emph{uniformly critical}. Closed-loop evaluation of $\pi_0.5$~\cite{black2025pi05} (CV$\,{=}\,$0.055) reveals a 36\,pp gap between random and L2 norm selection at $k{=}0.5$, demonstrating that models showing offline pruning tolerance can exhibit severe closed-loop degradation when the pruning method introduces spatial bias. CV provides a zero-cost diagnostic: a single forward pass replaces hundreds of expensive closed-loop episodes.
16	
17	Our contributions:
18	\begin{enumerate}[leftmargin=*,nosep]
19	\item \textbf{Connector-associated compressibility taxonomy with design guidelines} (\S\ref{sec:results}): Four classes---uniformly critical (linear projection), threshold-graded (linear + deep post-processing), smooth graded (MLP), catastrophic cliff (pixel-shuffle)---with practical guidelines for each. The monotonic CV-degradation relationship across seven models is consistent with the connector being a primary factor, though confounded by backbone differences (Appendix~\ref{app:confounders}).
20	\item \textbf{CV as diagnostic metric} (\S\ref{sec:scaling_law}, Appendix~\ref{app:cv_extended}): Token importance CV correlates with both tolerance class and optimal pruning method from a single forward pass. $\Delta(\text{R}{-}\text{L2})$ at $k{=}0.5$ scales monotonically from $+$36.0\,pp (CV$\,{=}\,$0.055) to $-$1.8\,pp (CV$\,{=}\,$0.215), validated at both $k{=}0.5$ and $k{=}0.7$.
21	\item \textbf{VTR overcomes catastrophic cliff} (\S\ref{sec:smart_compress_results}, Appendix~\ref{app:reencoding_analysis}): Vision Token Re-encoder recovers 0\% $\to$ 60\%+ SR at 75\% compression via learned re-encoding (cross-attention and MLP adapter, $p = 0.15$; relatively stable M-curve with $M{=}16 \approx M{=}128$).
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "5497a749-cf5c-4415-99ac-51338d2df09b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence). The connector design is strongly associated with token compressibility.}\n\\label{fig:architecture}\n\\end{figure}\n\nVision token pruning reliably accelerates Vision Transformers with negligible accuracy loss~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}. Vision-Language-Action (VLA) models~\\cite{kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders and produce hundreds of vision tokens that dominate the language backbone's input, making token reduction attractive for real-time robotic control at 5--10\\,Hz. Yet applying pruning to VLAs yields wildly inconsistent results: SmolVLA~\\cite{shukor2025smolvla} collapses to 0\\% task success at 5\\% token removal, while $\\pi_0$~\\cite{black2024pi0} shows a 2.4\\% \\emph{improvement} in offline action loss at 90\\% removal (offline metrics only; no closed-loop evaluation available). No existing work explains which outcome a given architecture will produce.\n\nThe critical architectural variable is the vision connector that transforms ViT patches into tokens for the language backbone. Pixel-shuffle connectors~\\cite{shukor2025smolvla,chen2024internvl} fold spatial patches so each token encodes a $4{\\times}4$ receptive field. MLP projectors~\\cite{liu2023llava,kim2024openvla} map patches independently through learned nonlinearities. Linear projections~\\cite{black2024pi0,black2025pi05} apply a single matrix multiplication. Recent VLA-specific works~\\cite{chen2024fastv,xu2025vlacache,cheng2026vlaiap} evaluate individual architectures without testing whether pruning behaves consistently across connector designs (Figure~\\ref{fig:architecture}). Unlike static benchmarks, robotic manipulation compounds errors across timesteps, making compression failures far more consequential.\n\nWe study vision token pruning across seven VLA models (450M--7B) spanning three connector families on LIBERO~\\cite{liu2023libero}, evaluating four in closed-loop and analyzing three via offline metrics or literature. The vision connector is strongly associated with pruning behavior along a four-class spectrum, and the coefficient of variation (CV) of token L2 norms correlates with both the tolerance class and the optimal strategy from a single forward pass. A central finding: low-CV models are not immune to pruning but \\emph{uniformly critical}. Closed-loop evaluation of $\\pi_0.5$~\\cite{black2025pi05} (CV$\\,{=}\\,$0.055) reveals a 36\\,pp gap between random and L2 norm selection at $k{=}0.5$, demonstrating that models showing offline pruning tolerance can exhibit severe closed-loop degradation when the pruning method introduces spatial bias. CV provides a zero-cost diagnostic: a single forward pass replaces hundreds of expensive closed-loop episodes.\n\nOur contributions:\n\\begin{enumerate}[leftmargin=*,nosep]\n\\item \\textbf{Connector-associated compressibility taxonomy with design guidelines} (\\S\\ref{sec:results}): Four classes---uniformly critical (linear projection), threshold-graded (linear + deep post-processing), smooth graded (MLP), catastrophic cliff (pixel-shuffle)---with practical guidelines for each. The monotonic CV-degradation relationship across seven models is consistent with the connector being a primary factor, though confounded by backbone differences (Appendix~\\ref{app:confounders}).\n\\item \\textbf{CV as diagnostic metric} (\\S\\ref{sec:scaling_law}, Appendix~\\ref{app:cv_extended}): Token importance CV correlates with both tolerance class and optimal pruning method from a single forward pass. $\\Delta(\\text{R}{-}\\text{L2})$ at $k{=}0.5$ scales monotonically from $+$36.0\\,pp (CV$\\,{=}\\,$0.055) to $-$1.8\\,pp (CV$\\,{=}\\,$0.215), validated at both $k{=}0.5$ and $k{=}0.7$.\n\\item \\textbf{VTR overcomes catastrophic cliff} (\\S\\ref{sec:smart_compress_results}, Appendix~\\ref{app:reencoding_analysis}): Vision Token Re-encoder recovers 0\\% $\\to$ 60\\%+ SR at 75\\% compression via learned re-encoding (cross-attention and MLP adapter, $p = 0.15$; relatively stable M-curve with $M{=}16 \\approx M{=}128$).\n\\end{enumerate}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01AW185h4K4kvkLvM7utABVA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "88a361ea-8724-4502-8264-39ad733226b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016deNbdXtWueHcGzPMoqWyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11453,
      "cache_read_input_tokens": 24524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11453
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

_source line 18 · 2026-05-23T00:53:06.176Z_

<details><summary>↩ Tool result · `toolu_01AW185h4K4kvkLvM7utABVA`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	
13	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
14	
15	\begin{document}
16	\maketitle
17	
18	\input{abstract}
19	
20	\keywords{vision-language-action models, token pruning, robot learning}
21	
22	\input{introduction}
23	
24	\input{related_work}
25	
26	\input{method}
27	
28	\input{experiments}
29	
30	\input{discussion}
31	
32	\input{conclusion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "1aeb8b13-5b91-4989-9763-4cfdf9164a7e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.\n% \\usepackage[final]{corl_2026} % Uncomment for camera-ready.\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\n\\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\\\Vision Connectors and VLA Token Compressibility}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\keywords{vision-language-action models, token pruning, robot learning}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper style, existing content, and what's needed. Let me write the method.tex file. Key things to note:

1. Must define Table 1 (tab:model_properties) here
2. Must define notation: k, CV, SR, M, N
3. Follow the section structure exactly as specified
4. ~900 words
5. No em-dashes, no -ing phrase endings, no "Furthermore"/"Moreover"/"Additionally" chains
6. CV = "correlates with" not "predicts"


7. Contribution = "diagnostic protocol" not "framework"
8. π0 = "offline metrics only"
9. booktabs only
10. Match the style of existing sections

I'm checking the experiments section to understand how the notation is used and ensure consistency. From there I can see k represents the retention ratio, CV is the coefficient of variation of token L2 norms, SR is the success rate, M is the number of VTR output queries, and N is the number of tokens. The table needs seven rows ordered by CV, starting with π0 which represents offline metrics only.

Now I'm compiling the model specifications for the table, ordered by their coefficient of variation values. I notice there are six models listed but the task mentions seven—let me verify which models should be included and whether I'm missing one. I'm seeing a discrepancy between what the paper claims in the introduction—seven VLA models across three connector families—and what's actually listed in the experiments section, which shows only six models. Looking at the task description more carefully, it specifies five VLAs spanning three connector families with seven total when including offline-only variants, and it's starting to list out the specific models with their parameters, but the list appears to be cut off mid-entry. I'm trying to reconcile the count—the introduction mentions seven VLA models, but I can only identify six from the descriptions given. The "7 total" might refer to seven connector configurations rather than seven distinct models, or there could be an offline-only model I'm missing from the literature. I'll proceed with the six models I can clearly identify and create the table accordingly. I'm going back and forth on whether there's a discrepancy between the introduction mentioning seven models and the experiments section listing six, but I'll stick with the six models I have data for rather than speculate. Now I need to write the method section, aiming for around 900 words, starting with describing the models and connectors, then creating the comparison table.

Writing the method section... SmolVLA uses a pixel-shuffle approach that groups 16 adjacent patches together into a single token, reducing the total to 128 tokens. I'm now summarizing the model properties across these different VLA architectures, distinguishing between those with independent patch processing versus those that create cross-token dependencies, and noting which models are evaluated through closed-loop robotic control versus offline metrics.

Generating model comparison table... Generating markdown table...

I'm setting up two pruning strategies to test token importance: one that ranks tokens by their L2 norm magnitude and keeps the highest-scoring fraction, and another that randomly samples tokens as a baseline. Both approaches physically remove the discarded tokens and adjust position indices accordingly rather than masking them. Then I'm introducing a diagnostic metric based on coefficient of variation to measure how compressible the token representations are. The coefficient of variation reveals a spectrum of token heterogeneity across models—π₀ maintains near-uniform distributions while SmolVLA's pixel-shuffle creates high heterogeneity—and this property directly correlates with how models respond to pruning, where low-CV models are more flexible about which tokens to remove but high-CV models fail catastrophically under any removal. To address this failure mode, I'm introducing Vision Token Re-encoder (VTR), a learned re-encoding approach that recovers spatially distributed information rather than relying on hard pruning.

VTR uses a lightweight cross-attention module with about 22M parameters to compress N source tokens into M output representations by having learned queries aggregate information across the entire spatial field, with configurations ranging from 16 to 128 tokens where the maximum serves as a passthrough control. I'm also testing a parameter-matched MLP baseline using average pooling and a two-layer network to isolate whether performance gains come from the cross-attention mechanism itself or simply from the re-encoding process. I'm realizing the models are interleaved when ordered by CV—offline and closed-loop aren't grouped together—so adding a horizontal rule to separate them won't work cleanly. I could reorder to group by type first (closed-loop, then offline), with each group sorted by CV, but the task specifies ordering by CV across all seven rows. I'll stick with CV ordering and skip the separator since the grouping doesn't align naturally.

Actually, wait—the task explicitly asks for a horizontal rule separating the two types, which suggests I should prioritize that grouping. Let me reorganize: closed-loop models sorted by CV, then a horizontal rule, then offline models sorted by CV. This respects the separation requirement even if it means not ordering all seven rows purely by CV.

Restructuring the table... Generating markdown table...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "275b2e0c-d2ae-472e-8199-c0932d66621a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE8BpVTe3C5uUULsUVPJwf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 35977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8117
      },
      "output_tokens": 12,
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

_source line 20_

Now let me check if the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "5b864ed5-4d67-44ea-8491-6228b995744c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE8BpVTe3C5uUULsUVPJwf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 35977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8117
      },
      "output_tokens": 12,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01AFA7zM1869mkbahNLSnyhr`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "93861268-c4e5-4a5e-84ea-02de4537ee8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RE8BpVTe3C5uUULsUVPJwf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8117,
      "cache_read_input_tokens": 35977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8117
      },
      "output_tokens": 12,
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

_source line 22 · 2026-05-23T00:54:45.614Z_

<details><summary>↩ Tool result · `toolu_01AFA7zM1869mkbahNLSnyhr`</summary>

```text
_pdf_images
abstract.tex
analysis.tex
appendix.tex
background.tex
conclusion.tex
corl_2026.sty
corlabbrvnat.bst
discussion.tex
experimental_setup.tex
experiments.tex
experiments_deprecated.tex
figures
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
notes
references.bib
references.bib.prev
related_work.tex
results.tex
results_v2.tex
sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "c9e0f676-93fc-4d62-a5e6-00f07e92d56e",
  "tool_use_result": {
    "stdout": "_pdf_images\nabstract.tex\nanalysis.tex\nappendix.tex\nbackground.tex\nconclusion.tex\ncorl_2026.sty\ncorlabbrvnat.bst\ndiscussion.tex\nexperimental_setup.tex\nexperiments.tex\nexperiments_deprecated.tex\nfigures\nintroduction.tex\nmain.aux\nmain.bbl\nmain.blg\nmain.fdb_latexmk\nmain.fls\nmain.log\nmain.out\nmain.pdf\nmain.tex\nnotes\nreferences.bib\nreferences.bib.prev\nrelated_work.tex\nresults.tex\nresults_v2.tex\nsections",
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

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists but there's no method.tex yet. Let me write it now.

Let me finalize the full method.tex content:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "03fe6d00-1196-45e3-8add-addda263d5ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178YdZQSjNCWQTz4Gdb5FHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5159,
      "cache_read_input_tokens": 44094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5159
      },
      "output_tokens": 11,
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

Writing the method section now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "470392d3-140a-40ee-9f30-e9a535c73c1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178YdZQSjNCWQTz4Gdb5FHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5159,
      "cache_read_input_tokens": 44094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5159
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — Write · `toolu_017UTPtQyXwn2CFSVTmQ244k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA models spanning three vision connector families (Table~\\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \\emph{coupling}.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_0$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_0.5$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).\n\n\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs, producing 256 and 512 tokens respectively. Each patch is processed independently, yielding a per-token importance gradient (CV $\\approx 0.22$).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\\cite{liu2023libero}; $\\pi_0$ and OFT are analyzed via offline metrics only.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_0.5$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_0$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\\lfloor k \\cdot N \\rfloor$ tokens that are passed to the LLM backbone.\n\nTwo strategies bracket expected performance:\n\n\\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.\n\n\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random, providing a conservative lower bound by ignoring token content entirely.\n\nBoth strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $t_i$ denotes the $i$-th post-connector vision token, and $\\sigma$, $\\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.\n\nCV is a zero-cost diagnostic: it requires one forward pass through the vision encoder and connector, with no pruning or downstream evaluation needed. The metric captures a continuous spectrum across connector designs. At one end, $\\pi_0$ (CV $= 0.038$) produces near-uniform norms, indicating that the linear connector distributes information evenly across patches. At the other end, SmolVLA (CV $= 0.314$) exhibits high norm heterogeneity from its pixel-shuffle operation. The remaining models span the interval between these extremes (Table~\\ref{tab:model_properties}).\n\nCV correlates with both pruning tolerance and sensitivity to pruning method choice. Models with low CV exhibit near-uniform tokens where the choice of \\emph{which} tokens to remove matters more than \\emph{how many} are removed. Models with high CV from entangling connectors exhibit catastrophic failure under any token removal strategy. We report success rate (SR) as the primary closed-loop evaluation metric throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.\n\nVTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.\n\nWe also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "889e6f95-a9c7-47ef-bb56-f7a8945f05d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178YdZQSjNCWQTz4Gdb5FHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5159,
      "cache_read_input_tokens": 44094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5159
      },
      "output_tokens": 11,
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

_source line 26 · 2026-05-23T00:55:32.808Z_

<details><summary>↩ Tool result · `toolu_017UTPtQyXwn2CFSVTmQ244k`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "a95aac6f-e702-445e-9b61-18c60f37e498",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA models spanning three vision connector families (Table~\\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \\emph{coupling}.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_0$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_0.5$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).\n\n\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs, producing 256 and 512 tokens respectively. Each patch is processed independently, yielding a per-token importance gradient (CV $\\approx 0.22$).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\\cite{liu2023libero}; $\\pi_0$ and OFT are analyzed via offline metrics only.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_0.5$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_0$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\\lfloor k \\cdot N \\rfloor$ tokens that are passed to the LLM backbone.\n\nTwo strategies bracket expected performance:\n\n\\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.\n\n\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random, providing a conservative lower bound by ignoring token content entirely.\n\nBoth strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $t_i$ denotes the $i$-th post-connector vision token, and $\\sigma$, $\\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.\n\nCV is a zero-cost diagnostic: it requires one forward pass through the vision encoder and connector, with no pruning or downstream evaluation needed. The metric captures a continuous spectrum across connector designs. At one end, $\\pi_0$ (CV $= 0.038$) produces near-uniform norms, indicating that the linear connector distributes information evenly across patches. At the other end, SmolVLA (CV $= 0.314$) exhibits high norm heterogeneity from its pixel-shuffle operation. The remaining models span the interval between these extremes (Table~\\ref{tab:model_properties}).\n\nCV correlates with both pruning tolerance and sensitivity to pruning method choice. Models with low CV exhibit near-uniform tokens where the choice of \\emph{which} tokens to remove matters more than \\emph{how many} are removed. Models with high CV from entangling connectors exhibit catastrophic failure under any token removal strategy. We report success rate (SR) as the primary closed-loop evaluation metric throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.\n\nVTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.\n\nWe also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 27_

Let me verify the file and check for style violations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "4c712e0e-bc65-4c49-bc1c-c80ddf57202a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d3rTQwbp9UXMqHYQ5paJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2167,
      "cache_read_input_tokens": 49253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2167
      },
      "output_tokens": 3,
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

<details open><summary>🔧 Tool call — Bash · `toolu_012PZ1Ff86pnWiqxkALEdD4E`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && grep -n \"—\" method.tex; grep -n \" – \" method.tex; grep -cn \"Furthermore\\|Moreover\\|Additionally\" method.tex; grep -n \"predicts\\|determines\\|framework\" method.tex; grep -n \"ing,\" method.tex",
  "description": "Check method.tex for style violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "a826b7fa-2e95-48a5-8aee-bbbbf7c54284",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d3rTQwbp9UXMqHYQ5paJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2167,
      "cache_read_input_tokens": 49253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2167
      },
      "output_tokens": 3,
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

_source line 29 · 2026-05-23T00:55:37.034Z_

<details><summary>↩ Tool result · `toolu_012PZ1Ff86pnWiqxkALEdD4E`</summary>

```text
0
13:\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "2e15fcda-799c-4295-9b37-49b1a0cac49e",
  "tool_use_result": {
    "stdout": "0\n13:\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.",
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

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01T4jmMujBB8k4UtMupFZj9t`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "description": "Count words in method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "27c7c83a-bec1-4341-aaca-bbe442d030f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d3rTQwbp9UXMqHYQ5paJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2167,
      "cache_read_input_tokens": 49253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2167
      },
      "output_tokens": 3,
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

_source line 31 · 2026-05-23T00:55:37.766Z_

<details><summary>↩ Tool result · `toolu_01T4jmMujBB8k4UtMupFZj9t`</summary>

```text
896 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "28865639-8f23-4b0b-a9a4-9fb35027b37a",
  "tool_use_result": {
    "stdout": "896 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
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

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Let me check what the grep matches were:
- No em-dashes (—) ✓
- No explanatory en-dashes ( – ) ✓
- 0 instances of Furthermore/Moreover/Additionally ✓
- No "predicts" or "determines" or "framework" ✓
- `grep -n "ing,"` found line 13 - let me check this: "concatenating 16 contiguous patches" - this is a present participle in a participial phrase. Let me check if it ends a sentence... "SmolVLA applies pixel-shuffle $4\times4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens." This is indeed an -ing phrase ending a sentence, which is flagged as an AI writing pattern. 

Now I need to scan through the full text for all -ing phrase endings. I'm finding several instances: "producing 256 and 512 tokens respectively" on line 9, "yielding a per-token importance gradient (CV $\approx 0.22$)" on line 10, and "producing 50 tokens with learned cross-attention dependencies" on line 13 all end with -ing constructions that need to be rewritten.

For line 9, I should change "producing 256 and 512 tokens respectively" to use "to produce" instead. Line 10's "yielding" should become "to yield". And line 13's "producing" should shift to "to produce" as well. The SmolVLA sentence on line 13 has "concatenating" in the middle, which is fine since it's not an ending phrase, but the overall structure could be clearer. I'm going through the text systematically to eliminate sentences that end with participial phrases. I've identified several instances where -ing phrases conclude sentences—like "producing 256 and 512 tokens respectively" and "yielding a per-token importance gradient"—and I'm restructuring them to end with stronger, more direct language instead. The goal is to make each sentence terminate with a noun or concrete statement rather than a trailing participial construction. I'm going through the paper systematically to identify and fix all the sentences that end with -ing participial phrases, since that's creating awkward constructions throughout. I need to restructure these to have proper sentence endings rather than dangling participles or mid-sentence -ing phrases that make the prose feel incomplete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "e6ce0bb0-f64f-4dda-a6d9-f7ce9b5b4e83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014M65rjwffQS2mFP7zm2jrz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 51420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

### Assistant

_source line 33_

Found some -ing participial phrases to fix. Let me clean those up.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "1ed9d7af-079d-4ba7-8067-76dcc435d701",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014M65rjwffQS2mFP7zm2jrz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 51420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01ApsM3gdKqpGm8y8KGzrBE4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs, producing 256 and 512 tokens respectively. Each patch is processed independently, yielding a per-token importance gradient (CV $\\approx 0.22$).",
  "new_string": "OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\\approx 0.22$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "2e304d04-1671-4491-a138-719374ad4f5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014M65rjwffQS2mFP7zm2jrz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 51420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

_source line 35 · 2026-05-23T00:56:06.627Z_

<details><summary>↩ Tool result · `toolu_01ApsM3gdKqpGm8y8KGzrBE4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "6cbd35d2-cd7d-456c-a455-1ba601e942de",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs, producing 256 and 512 tokens respectively. Each patch is processed independently, yielding a per-token importance gradient (CV $\\approx 0.22$).",
    "newString": "OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\\approx 0.22$).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA models spanning three vision connector families (Table~\\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \\emph{coupling}.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_0$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_0.5$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).\n\n\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs, producing 256 and 512 tokens respectively. Each patch is processed independently, yielding a per-token importance gradient (CV $\\approx 0.22$).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\\cite{liu2023libero}; $\\pi_0$ and OFT are analyzed via offline metrics only.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_0.5$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_0$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\\lfloor k \\cdot N \\rfloor$ tokens that are passed to the LLM backbone.\n\nTwo strategies bracket expected performance:\n\n\\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.\n\n\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random, providing a conservative lower bound by ignoring token content entirely.\n\nBoth strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $t_i$ denotes the $i$-th post-connector vision token, and $\\sigma$, $\\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.\n\nCV is a zero-cost diagnostic: it requires one forward pass through the vision encoder and connector, with no pruning or downstream evaluation needed. The metric captures a continuous spectrum across connector designs. At one end, $\\pi_0$ (CV $= 0.038$) produces near-uniform norms, indicating that the linear connector distributes information evenly across patches. At the other end, SmolVLA (CV $= 0.314$) exhibits high norm heterogeneity from its pixel-shuffle operation. The remaining models span the interval between these extremes (Table~\\ref{tab:model_properties}).\n\nCV correlates with both pruning tolerance and sensitivity to pruning method choice. Models with low CV exhibit near-uniform tokens where the choice of \\emph{which} tokens to remove matters more than \\emph{how many} are removed. Models with high CV from entangling connectors exhibit catastrophic failure under any token removal strategy. We report success rate (SR) as the primary closed-loop evaluation metric throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.\n\nVTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.\n\nWe also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_0$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_0.5$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).",
          " ",
          "-\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs, producing 256 and 512 tokens respectively. Each patch is processed independently, yielding a per-token importance gradient (CV $\\approx 0.22$).",
          "+\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\\approx 0.22$).",
          " ",
          " \\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.",
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01Fiop8v7VhkooqrneQa7QX9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.",
  "new_string": "X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart} to produce 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding that concatenates 16 contiguous patches into the channel dimension of each output token, for a total of 128 tokens."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "b51ac84c-8c4a-4d89-b136-240d70f1233a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VL5LUVUSrhwoo9SEEbwfd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1599,
      "cache_read_input_tokens": 51940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1599
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

_source line 37 · 2026-05-23T00:56:12.019Z_

<details><summary>↩ Tool result · `toolu_01Fiop8v7VhkooqrneQa7QX9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "e8014adb-d2d2-4d3a-b1a0-c876d5e0d8ca",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.",
    "newString": "X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart} to produce 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding that concatenates 16 contiguous patches into the channel dimension of each output token, for a total of 128 tokens.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA models spanning three vision connector families (Table~\\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \\emph{coupling}.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_0$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_0.5$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).\n\n\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\\approx 0.22$).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\\cite{liu2023libero}; $\\pi_0$ and OFT are analyzed via offline metrics only.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_0.5$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_0$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\\lfloor k \\cdot N \\rfloor$ tokens that are passed to the LLM backbone.\n\nTwo strategies bracket expected performance:\n\n\\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.\n\n\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random, providing a conservative lower bound by ignoring token content entirely.\n\nBoth strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $t_i$ denotes the $i$-th post-connector vision token, and $\\sigma$, $\\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.\n\nCV is a zero-cost diagnostic: it requires one forward pass through the vision encoder and connector, with no pruning or downstream evaluation needed. The metric captures a continuous spectrum across connector designs. At one end, $\\pi_0$ (CV $= 0.038$) produces near-uniform norms, indicating that the linear connector distributes information evenly across patches. At the other end, SmolVLA (CV $= 0.314$) exhibits high norm heterogeneity from its pixel-shuffle operation. The remaining models span the interval between these extremes (Table~\\ref{tab:model_properties}).\n\nCV correlates with both pruning tolerance and sensitivity to pruning method choice. Models with low CV exhibit near-uniform tokens where the choice of \\emph{which} tokens to remove matters more than \\emph{how many} are removed. Models with high CV from entangling connectors exhibit catastrophic failure under any token removal strategy. We report success rate (SR) as the primary closed-loop evaluation metric throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.\n\nVTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.\n\nWe also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation.\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\\approx 0.22$).",
          " ",
          "-\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart}, producing 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into the channel dimension of each output token to produce 128 tokens.",
          "+\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart} to produce 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding that concatenates 16 contiguous patches into the channel dimension of each output token, for a total of 128 tokens.",
          " ",
          " We classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\\cite{liu2023libero}; $\\pi_0$ and OFT are analyzed via offline metrics only.",
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

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01Wn7xdAASaxa4x26kFr85wj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random, providing a conservative lower bound by ignoring token content entirely.",
  "new_string": "\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. Because it ignores token content entirely, random selection provides a conservative lower bound."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "a5e7bfd4-4eae-4d89-aa2a-6bda5e19aff1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJFhYC3u8MbP8cYKoLyUrS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 53539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
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

_source line 39 · 2026-05-23T00:56:17.793Z_

<details><summary>↩ Tool result · `toolu_01Wn7xdAASaxa4x26kFr85wj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "e8162969-5fcd-4dd1-bb85-d6ba12dc345b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random, providing a conservative lower bound by ignoring token content entirely.",
    "newString": "\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. Because it ignores token content entirely, random selection provides a conservative lower bound.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA models spanning three vision connector families (Table~\\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \\emph{coupling}.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_0$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_0.5$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).\n\n\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\\approx 0.22$).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart} to produce 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding that concatenates 16 contiguous patches into the channel dimension of each output token, for a total of 128 tokens.\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\\cite{liu2023libero}; $\\pi_0$ and OFT are analyzed via offline metrics only.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_0.5$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_0$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\\lfloor k \\cdot N \\rfloor$ tokens that are passed to the LLM backbone.\n\nTwo strategies bracket expected performance:\n\n\\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.\n\n\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random, providing a conservative lower bound by ignoring token content entirely.\n\nBoth strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $t_i$ denotes the $i$-th post-connector vision token, and $\\sigma$, $\\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.\n\nCV is a zero-cost diagnostic: it requires one forward pass through the vision encoder and connector, with no pruning or downstream evaluation needed. The metric captures a continuous spectrum across connector designs. At one end, $\\pi_0$ (CV $= 0.038$) produces near-uniform norms, indicating that the linear connector distributes information evenly across patches. At the other end, SmolVLA (CV $= 0.314$) exhibits high norm heterogeneity from its pixel-shuffle operation. The remaining models span the interval between these extremes (Table~\\ref{tab:model_properties}).\n\nCV correlates with both pruning tolerance and sensitivity to pruning method choice. Models with low CV exhibit near-uniform tokens where the choice of \\emph{which} tokens to remove matters more than \\emph{how many} are removed. Models with high CV from entangling connectors exhibit catastrophic failure under any token removal strategy. We report success rate (SR) as the primary closed-loop evaluation metric throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.\n\nVTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.\n\nWe also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation.\n",
    "structuredPatch": [
      {
        "oldStart": 43,
        "oldLines": 7,
        "newStart": 43,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.",
          " ",
          "-\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random, providing a conservative lower bound by ignoring token content entirely.",
          "+\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. Because it ignores token content entirely, random selection provides a conservative lower bound.",
          " ",
          " Both strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.",
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

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_01XkqFSHmkJKRdAL1e9QEgsk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone.",
  "new_string": "The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field. The resulting $M$ output representations are passed to the LLM backbone as compressed vision tokens."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "dfdd83d9-7f40-4cd5-8964-c6d181aa08e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lf18S12cg5d7tExGGdqv8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 53956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 297
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

_source line 41 · 2026-05-23T00:56:23.154Z_

<details><summary>↩ Tool result · `toolu_01XkqFSHmkJKRdAL1e9QEgsk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "32620d74-5166-4dc2-924a-12b28f28e504",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone.",
    "newString": "The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field. The resulting $M$ output representations are passed to the LLM backbone as compressed vision tokens.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA models spanning three vision connector families (Table~\\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \\emph{coupling}.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_0$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_0.5$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).\n\n\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\\approx 0.22$).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart} to produce 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding that concatenates 16 contiguous patches into the channel dimension of each output token, for a total of 128 tokens.\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\\cite{liu2023libero}; $\\pi_0$ and OFT are analyzed via offline metrics only.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_0.5$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_0$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\\lfloor k \\cdot N \\rfloor$ tokens that are passed to the LLM backbone.\n\nTwo strategies bracket expected performance:\n\n\\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.\n\n\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. Because it ignores token content entirely, random selection provides a conservative lower bound.\n\nBoth strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $t_i$ denotes the $i$-th post-connector vision token, and $\\sigma$, $\\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.\n\nCV is a zero-cost diagnostic: it requires one forward pass through the vision encoder and connector, with no pruning or downstream evaluation needed. The metric captures a continuous spectrum across connector designs. At one end, $\\pi_0$ (CV $= 0.038$) produces near-uniform norms, indicating that the linear connector distributes information evenly across patches. At the other end, SmolVLA (CV $= 0.314$) exhibits high norm heterogeneity from its pixel-shuffle operation. The remaining models span the interval between these extremes (Table~\\ref{tab:model_properties}).\n\nCV correlates with both pruning tolerance and sensitivity to pruning method choice. Models with low CV exhibit near-uniform tokens where the choice of \\emph{which} tokens to remove matters more than \\emph{how many} are removed. Models with high CV from entangling connectors exhibit catastrophic failure under any token removal strategy. We report success rate (SR) as the primary closed-loop evaluation metric throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.\n\nVTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.\n\nWe also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation.\n",
    "structuredPatch": [
      {
        "oldStart": 66,
        "oldLines": 6,
        "newStart": 66,
        "newLines": 6,
        "lines": [
          " ",
          " Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.",
          " ",
          "-VTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field, producing $M$ compressed output representations that are passed to the LLM backbone. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.",
          "+VTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field. The resulting $M$ output representations are passed to the LLM backbone as compressed vision tokens. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.",
          " ",
          " We also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation."
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

_source line 42_

Now let me do a final review of the complete file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "a7c8121f-ae9e-4fe8-9b5c-a4738dc6a567",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5TUGS7vtrnDkBDuoeoGFJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 54253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01BJuENNWgEG8m38fgfLcRSH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "5df166a3-5363-4d0a-a69c-217843a03bc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5TUGS7vtrnDkBDuoeoGFJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 54253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 44 · 2026-05-23T00:56:26.022Z_

<details><summary>↩ Tool result · `toolu_01BJuENNWgEG8m38fgfLcRSH`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA models spanning three vision connector families (Table~\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \emph{coupling}.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_0$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_0.5$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).
10	
11	\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} and OFT~\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\approx 0.22$).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\cite{lewis2020bart} to produce 50 tokens with learned cross-attention dependencies. SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding that concatenates 16 contiguous patches into the channel dimension of each output token, for a total of 128 tokens.
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models ($\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\cite{liu2023libero}; $\pi_0$ and OFT are analyzed via offline metrics only.
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}
21	\label{tab:model_properties}
22	\begin{tabular}{lrlcrll}
23	\toprule
24	Model & Params & Connector & $N$ & CV & Coupling & Eval \\
25	\midrule
26	$\pi_0.5$ & 4B & Linear ($\times\!\sqrt{d}$) & 768 & 0.055 & Indep.\ & Closed-loop \\
27	X-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\
28	OpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\ & Closed-loop \\
29	SmolVLA & 450M & Pixel-shuffle $4{\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\
30	\midrule
31	$\pi_0$ & 3.3B & Linear & 256 & 0.038 & Indep.\ & Offline \\
32	OFT & 7B & 3-layer MLP & 512 & 0.219 & Indep.\ & Offline \\
33	\bottomrule
34	\end{tabular}
35	\end{table}
36	
37	\subsection{Pruning Protocol}
38	\label{sec:pruning_protocol}
39	
40	We apply post-connector token pruning at retention ratio $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\lfloor k \cdot N \rfloor$ tokens that are passed to the LLM backbone.
41	
42	Two strategies bracket expected performance:
43	
44	\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.
45	
46	\textbf{Random subsampling} selects $\lfloor k \cdot N \rfloor$ tokens uniformly at random. Because it ignores token content entirely, random selection provides a conservative lower bound.
47	
48	Both strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.
49	
50	\subsection{Compressibility Diagnostic: Importance CV}
51	\label{sec:cv_diagnostic}
52	
53	We quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:
54	\begin{equation}
55	\text{CV} = \frac{\sigma\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}{\mu\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}
56	\label{eq:cv}
57	\end{equation}
58	where $t_i$ denotes the $i$-th post-connector vision token, and $\sigma$, $\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.
59	
60	CV is a zero-cost diagnostic: it requires one forward pass through the vision encoder and connector, with no pruning or downstream evaluation needed. The metric captures a continuous spectrum across connector designs. At one end, $\pi_0$ (CV $= 0.038$) produces near-uniform norms, indicating that the linear connector distributes information evenly across patches. At the other end, SmolVLA (CV $= 0.314$) exhibits high norm heterogeneity from its pixel-shuffle operation. The remaining models span the interval between these extremes (Table~\ref{tab:model_properties}).
61	
62	CV correlates with both pruning tolerance and sensitivity to pruning method choice. Models with low CV exhibit near-uniform tokens where the choice of \emph{which} tokens to remove matters more than \emph{how many} are removed. Models with high CV from entangling connectors exhibit catastrophic failure under any token removal strategy. We report success rate (SR) as the primary closed-loop evaluation metric throughout.
63	
64	\subsection{Vision Token Re-encoder (VTR)}
65	\label{sec:vtr}
66	
67	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.
68	
69	VTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field. The resulting $M$ output representations are passed to the LLM backbone as compressed vision tokens. The output dimensionality $M \in \{16, 32, 64, 96, 128\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.
70	
71	We also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation.
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "de134aa6-7d27-4e03-be65-e9e566ebf879",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA models spanning three vision connector families (Table~\\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \\emph{coupling}.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_0$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_0.5$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras. Both produce tokens with near-uniform L2 norms (CV $< 0.06$).\n\n\\textbf{MLP projector} maps each patch through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} and OFT~\\cite{kim2025openoft} both use three-layer MLPs to produce 256 and 512 tokens respectively. Each patch is processed independently, and the resulting norms exhibit a clear importance gradient (CV $\\approx 0.22$).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies through post-projection processing. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart} to produce 50 tokens with learned cross-attention dependencies. SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding that concatenates 16 contiguous patches into the channel dimension of each output token, for a total of 128 tokens.\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop robotic control on LIBERO~\\cite{liu2023libero}; $\\pi_0$ and OFT are analyzed via offline metrics only.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_0.5$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_0$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\\lfloor k \\cdot N \\rfloor$ tokens that are passed to the LLM backbone.\n\nTwo strategies bracket expected performance:\n\n\\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.\n\n\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. Because it ignores token content entirely, random selection provides a conservative lower bound.\n\nBoth strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $t_i$ denotes the $i$-th post-connector vision token, and $\\sigma$, $\\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.\n\nCV is a zero-cost diagnostic: it requires one forward pass through the vision encoder and connector, with no pruning or downstream evaluation needed. The metric captures a continuous spectrum across connector designs. At one end, $\\pi_0$ (CV $= 0.038$) produces near-uniform norms, indicating that the linear connector distributes information evenly across patches. At the other end, SmolVLA (CV $= 0.314$) exhibits high norm heterogeneity from its pixel-shuffle operation. The remaining models span the interval between these extremes (Table~\\ref{tab:model_properties}).\n\nCV correlates with both pruning tolerance and sensitivity to pruning method choice. Models with low CV exhibit near-uniform tokens where the choice of \\emph{which} tokens to remove matters more than \\emph{how many} are removed. Models with high CV from entangling connectors exhibit catastrophic failure under any token removal strategy. We report success rate (SR) as the primary closed-loop evaluation metric throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this limitation through learned re-encoding rather than hard deletion.\n\nVTR is a lightweight cross-attention module with approximately 22M trainable parameters (roughly 5\\% of SmolVLA's 450M total). The module takes the full set of $N$ source tokens from the vision connector as keys and values, and uses $M$ learned queries to attend over all $N$ tokens via multi-head cross-attention. Each query aggregates information from the entire spatial field. The resulting $M$ output representations are passed to the LLM backbone as compressed vision tokens. The output dimensionality $M \\in \\{16, 32, 64, 96, 128\\}$ controls the compression ratio; $M = N = 128$ serves as a passthrough control that re-encodes without reducing the token count.\n\nWe also evaluate a parameter-matched MLP adapter control (approximately 22M parameters). This variant applies average pooling over groups of source tokens followed by a two-layer MLP, without cross-attention. Comparing VTR against this control isolates whether the performance gain stems from the cross-attention mechanism specifically or from the act of re-encoding entangled tokens into a new representation.\n",
      "numLines": 72,
      "startLine": 1,
      "totalLines": 72
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01V33Py1DvawqqcFf8ypUZ1c`</summary>

```json
{
  "command": "grep -n \"—\\| – \\|Furthermore\\|Moreover\\|Additionally\\|predicts\\|determines\\|framework\\|hline\" method.tex; echo \"---\"; grep -c \"ing,\" method.tex; echo \"---\"; wc -w method.tex",
  "description": "Final style check on method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "0a088a9f-38b3-4683-a67e-6ac25fa07181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jRYcLyr1tM5YJ3zwWxFUM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2244,
      "cache_read_input_tokens": 54707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2244
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

_source line 46 · 2026-05-23T00:56:31.558Z_

<details><summary>↩ Tool result · `toolu_01V33Py1DvawqqcFf8ypUZ1c`</summary>

```text
---
0
---
911 method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "b6e410fe-f361-4883-abe3-137daa710fa3",
  "tool_use_result": {
    "stdout": "---\n0\n---\n911 method.tex",
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

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
All clean. No style violations. ~911 words (including LaTeX markup, so actual prose is right around 900). The file is ready.

Let me verify all labels match what experiments.tex expects:
- \label{sec:method} ✓
- \label{sec:models} ✓
- \label{sec:pruning_protocol} ✓
- \label{sec:cv_diagnostic} ✓
- \label{sec:vtr} ✓
- \label{tab:model_properties} ✓


- \label{eq:cv} ✓

All notation is properly defined: retention ratio, coefficient of variation, success rate, VTR output queries, and vision token count. Everything checks out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "6d2c5fe2-6167-4cc9-8c79-40a8f8c6106a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThAShHQm4a2CnYQ9QF7VcJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 158,
      "cache_read_input_tokens": 56951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 158
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

_source line 48_

All checks pass. Written to `docs/paper/method.tex` (911 words including markup). The section defines all notation referenced by experiments.tex ($k$, CV, SR, $M$, $N$), includes Table 1 (`\label{tab:model_properties}`) with 6 models grouped by eval protocol and ordered by CV, and uses all required labels (`sec:method`, `sec:models`, `sec:pruning_protocol`, `sec:cv_diagnostic`, `sec:vtr`). Zero style violations: no dashes, no -ing phrase endings, no connector-chain transitions, CV described as "correlates with" throughout.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "uuid": "0936be0c-07dc-4785-9e66-98246d5f56be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThAShHQm4a2CnYQ9QF7VcJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 158,
      "cache_read_input_tokens": 56951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 158
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

_source line 49_

All checks pass. Written to `docs/paper/method.tex` (911 words including markup). The section defines all notation referenced by experiments.tex ($k$, CV, SR, $M$, $N$), includes Table 1 (`\label{tab:model_properties}`) with 6 models grouped by eval protocol and ordered by CV, and uses all required labels (`sec:method`, `sec:models`, `sec:pruning_protocol`, `sec:cv_diagnostic`, `sec:vtr`). Zero style violations: no dashes, no -ing phrase endings, no connector-chain transitions, CV described as "correlates with" throughout.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 228788,
  "duration_api_ms": 229245,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "f2c9863b-55c6-4c84-8071-e173a51001ce",
  "total_cost_usd": 0.8286035,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 45268,
    "cache_read_input_tokens": 542455,
    "output_tokens": 10892,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 45268,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 366,
        "cache_read_input_tokens": 56951,
        "cache_creation_input_tokens": 158,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 158
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1986,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002081,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 10892,
      "cacheReadInputTokens": 542455,
      "cacheCreationInputTokens": 45268,
      "webSearchRequests": 0,
      "costUSD": 0.8265225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5b39294b-deca-4c32-9f0c-e99ca983a35e"
}
```

</details>

---
