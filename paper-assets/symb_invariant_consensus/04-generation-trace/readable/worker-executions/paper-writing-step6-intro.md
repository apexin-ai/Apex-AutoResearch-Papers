# paper writing step6 intro

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_writing_step6_intro_20260523T025141.log`
- **Structured JSON:** [`ba62f8b4458f73df425c.json`](../../sessions/ba/ba62f8b4458f73df425c.json)

## Before a recorded user message

20 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
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
  "uuid": "faf5a082-d299-4e9c-acdc-9b241347a68e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/memory/"
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
    "resetsAt": 1779521400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9effa6a3-6645-4c70-a6b7-9fe2cbc7d481",
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96"
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
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "b5d2a5ed-c7ec-42cd-9373-0ce3de2a3f72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VprpwZvY7scDd5hbNYEFgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13978,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13978
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

<details open><summary>🔧 Tool call — Read · `toolu_01HFyAkyUxwsPoP7UVD5mFDH`</summary>

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
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "92af61d3-1970-420f-80b7-ee7c7f59b988",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VprpwZvY7scDd5hbNYEFgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13978,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13978
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

_source line 6 · 2026-05-23T02:51:57.060Z_

<details><summary>↩ Tool result · `toolu_01HFyAkyUxwsPoP7UVD5mFDH`</summary>

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
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "63926eb6-a325-40c4-a8a5-bd1ead04ecf8",
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

<details open><summary>🔧 Tool call — Read · `toolu_01GQQwFmwifom4wMbQVFB4ej`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "bbbd2785-d869-4371-bdcf-858fcddcf3e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VprpwZvY7scDd5hbNYEFgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13978,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13978
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

_source line 8 · 2026-05-23T02:51:57.156Z_

<details><summary>↩ Tool result · `toolu_01GQQwFmwifom4wMbQVFB4ej`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\text{eff}}$ as an ordinal diagnostic of vote diversity ($K_{\text{eff}} \approx 1.2$--$3.6$ for nominal $K = 12$; \S\ref{sec:condorcet}).
17	Chain-of-thought cosine similarity ($0.69$) far exceeds answer-level $\kappa$ ($0.46$), revealing that traces share reasoning processes even when they diverge on final answers (\S\ref{sec:process-kappa}).
18	When the same model extracts logical constraints from these correlated traces, the constraints exhibit \emph{symbolic confirmation bias} (SCB): on problems where the model errs, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratios $1.66$--$4.97\times$ across nine models), and 94\% of errors overlap with SC (\S\ref{sec:confirmation-bias}).
19	A shuffle control shows this bias is structural: it reflects the trace-count distribution rather than extraction-specific error.
20	Self-extraction cannot supply the independent signal that CJT requires.
21	
22	We study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}).
23	Across six open-source models (7B--32B), three domains (FOLIO \citep{han2022folio}, ProofWriter \citep{tafjord2021proofwriter}, LogiQA \citep{liu2020logiqa}), and over 3,000 condition-evaluations with four-seed replication, twenty-seven training-free remediation strategies spanning fifteen families all produce neutral or negative results (Table~\ref{tab:main_results}).
24	Prior work shows LLMs struggle with natural-language self-correction \citep{huang2024selfcorrect} and that LLM-generated logical formulas can be unreliable \citep{stechly2025selfverification}. Our formal channel is provably sound---the failure is precisely localizable to the extraction step. The assumption that formalizing reasoning provides \emph{independent} verification evidence fails not because Z3 is unreliable (99\% of constraints are syntactically valid), but because extraction inherits the model's biases: MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems, rendering the formal layer vacuous.
25	
26	Oracle controls confirm the mechanism is sound ($+29.90$\,pp Mistral-7B, $+13.73$\,pp Qwen-14B on FOLIO, $p < 0.001$; Appendix~\ref{app:oracle}), yet self-extraction captures only ${\sim}$12\% of this ceiling.
27	The central finding is a persistent independence-accuracy trade-off \citep{krogh1994neural}: Debate reduces $\kappa$ to 0.15 but collapses accuracy ($-18.6$\,pp); other methods cluster at $\kappa \approx 0.40$--$0.47$, a same-model ceiling across three families (\S\ref{sec:remediation}).
28	A cross-architecture proof-of-concept escapes the bottleneck: zero-shot DeBERTa NLI yields $+6.67$\,pp on Mistral-7B ProofWriter ($p < 0.001$) but no significant gain for stronger generators; domain-adapted NLI amplifies gains to $+$12--26\,pp ($p < 0.0001$), extending to generators with SC up to 72\% (\S\ref{sec:cross-arch}).
29	
30	Our contributions are:
31	\begin{enumerate}[nosep,leftmargin=*]
32	\item \textbf{Quantifying symbolic confirmation bias in formal self-verification.} While the general difficulty of LLM self-correction is known \citep{huang2024selfcorrect}, we provide the first quantitative characterization of symbolic confirmation bias in formal self-verification, demonstrating that provably sound verification machinery becomes informationally vacuous under self-extraction: 83.3\% of self-extracted constraints support the wrong answer (BR $1.66$--$4.97\times$ across nine models), yet 99\% pass Z3 validation. A shuffle control and MAX-SAT ablation show this bias is structural---the formal layer adds no information beyond majority voting. Twenty-seven training-free strategies fail to break it; cross-model extraction confirms universality across nine models from 7B to frontier (\S\ref{sec:confirmation-bias}).
33	
34	\item \textbf{General diagnostic framework for trace-aggregation methods.} Three diagnostics ($K_\text{eff}$, BR, $C_0$) correctly predict success or failure across all 60 tested conditions spanning self-extraction, training-free remediation, cross-architecture verification, and oracle controls. Decision boundaries---$C_0 < 5\%$ (degenerate), $K_\text{eff} \leq 1.3$ (diversity-limited), $\text{BR} > 2\times$ (bias-dominated), $\kappa_\text{same} \geq 0.40$ (same-model ceiling)---provide zero-cost prediction of symbolic aggregation viability. The framework extends to any method extracting structured representations from LLM traces (\S\ref{sec:remediation}, \S\ref{sec:cross-arch}).
35	
36	\item \textbf{Process-level independence analysis.} CoT cosine similarity ($0.69$--$0.79$) exceeds answer-level $\kappa$ ($0.45$--$0.74$) across four models from three families; under cross-model extraction on frontier models, SICA gain decreases monotonically with process similarity ($\rho = -1.0$, $p = 0.008$; \S\ref{sec:process-kappa}).
37	\end{enumerate}
38	
39	\begin{figure}[t]
40	\centering
41	\small
42	\resizebox{\columnwidth}{!}{\begin{tikzpicture}[
43	    node distance=0.3cm and 0.1cm,
44	    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,
45	                text width=1.2cm, align=center, font=\scriptsize},
46	    arr/.style={-{Stealth[length=4pt]}, thick},
47	    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},
48	    lbl/.style={font=\scriptsize, text=gray!70!black},
49	    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,
50	                    inner sep=3pt},
51	]
52	\node[box] (q) {Question $q$};
53	\node[box, right=of q] (sample) {Sample $K$\\traces};
54	\node[box, right=of sample] (extract) {Extract logical\\constraints};
55	\node[box, right=of extract] (dedup) {Dedup.\ +\\weight};
56	\node[box, right=of dedup] (maxsat) {MAX-SAT\\(Z3)};
57	
58	\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};
59	\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\vote};
60	
61	\draw[arr] (q) -- (sample);
62	\draw[arr] (sample) -- (extract);
63	\draw[arr] (extract) -- (dedup);
64	\draw[arr] (dedup) -- (maxsat);
65	\draw[arr] (maxsat) -- (ans);
66	\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);
67	
68	\node[lbl, above=0.01cm of maxsat] {SICA};
69	
70	\node[ibottle, fit=(sample)(extract), label={[font=\scriptsize\itshape, text=red!70!black]above:Independence Bottleneck}] {};
71	
72	\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};
73	\end{tikzpicture}}
74	\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}
75	\label{fig:pipeline}
76	\end{figure}
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "4febf2f0-3a1e-45a3-9ca4-b357454d6c6d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nTest-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \\citep{snell2025scaling, guo2025deepseekr1}.\nThe dominant aggregation strategy, Self-Consistency (SC) \\citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.\nSC is simple, model-agnostic, and effective---but it is hitting a ceiling.\n\\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.\nThe gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.\n\nConfidence-weighted \\citep{taubenfeld2025cisc} and universal \\citep{chen2024usc} extensions alleviate this, but the core limitation persists.\nRecent neuro-symbolic methods \\citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.\nA simpler question precedes these: can the \\emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?\nNo prior work has systematically evaluated this.\n\nWe ground our analysis in the Condorcet Jury Theorem (CJT) \\citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \\citep{austensmith1996}.\nWhen independence fails \\citep{ladha1992correlated}, additional samples carry diminishing information.\nMeasuring inter-trace agreement with Fleiss' $\\kappa$ \\citep{fleiss1971kappa}, we find $\\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\\text{eff}}$ as an ordinal diagnostic of vote diversity ($K_{\\text{eff}} \\approx 1.2$--$3.6$ for nominal $K = 12$; \\S\\ref{sec:condorcet}).\nChain-of-thought cosine similarity ($0.69$) far exceeds answer-level $\\kappa$ ($0.46$), revealing that traces share reasoning processes even when they diverge on final answers (\\S\\ref{sec:process-kappa}).\nWhen the same model extracts logical constraints from these correlated traces, the constraints exhibit \\emph{symbolic confirmation bias} (SCB): on problems where the model errs, 83.3\\% of self-extracted constraints support the wrong majority answer (bias ratios $1.66$--$4.97\\times$ across nine models), and 94\\% of errors overlap with SC (\\S\\ref{sec:confirmation-bias}).\nA shuffle control shows this bias is structural: it reflects the trace-count distribution rather than extraction-specific error.\nSelf-extraction cannot supply the independent signal that CJT requires.\n\nWe study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}).\nAcross six open-source models (7B--32B), three domains (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}, LogiQA \\citep{liu2020logiqa}), and over 3,000 condition-evaluations with four-seed replication, twenty-seven training-free remediation strategies spanning fifteen families all produce neutral or negative results (Table~\\ref{tab:main_results}).\nPrior work shows LLMs struggle with natural-language self-correction \\citep{huang2024selfcorrect} and that LLM-generated logical formulas can be unreliable \\citep{stechly2025selfverification}. Our formal channel is provably sound---the failure is precisely localizable to the extraction step. The assumption that formalizing reasoning provides \\emph{independent} verification evidence fails not because Z3 is unreliable (99\\% of constraints are syntactically valid), but because extraction inherits the model's biases: MAX-SAT produces answers identical to count-only aggregation on 94.4\\% of problems, rendering the formal layer vacuous.\n\nOracle controls confirm the mechanism is sound ($+29.90$\\,pp Mistral-7B, $+13.73$\\,pp Qwen-14B on FOLIO, $p < 0.001$; Appendix~\\ref{app:oracle}), yet self-extraction captures only ${\\sim}$12\\% of this ceiling.\nThe central finding is a persistent independence-accuracy trade-off \\citep{krogh1994neural}: Debate reduces $\\kappa$ to 0.15 but collapses accuracy ($-18.6$\\,pp); other methods cluster at $\\kappa \\approx 0.40$--$0.47$, a same-model ceiling across three families (\\S\\ref{sec:remediation}).\nA cross-architecture proof-of-concept escapes the bottleneck: zero-shot DeBERTa NLI yields $+6.67$\\,pp on Mistral-7B ProofWriter ($p < 0.001$) but no significant gain for stronger generators; domain-adapted NLI amplifies gains to $+$12--26\\,pp ($p < 0.0001$), extending to generators with SC up to 72\\% (\\S\\ref{sec:cross-arch}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Quantifying symbolic confirmation bias in formal self-verification.} While the general difficulty of LLM self-correction is known \\citep{huang2024selfcorrect}, we provide the first quantitative characterization of symbolic confirmation bias in formal self-verification, demonstrating that provably sound verification machinery becomes informationally vacuous under self-extraction: 83.3\\% of self-extracted constraints support the wrong answer (BR $1.66$--$4.97\\times$ across nine models), yet 99\\% pass Z3 validation. A shuffle control and MAX-SAT ablation show this bias is structural---the formal layer adds no information beyond majority voting. Twenty-seven training-free strategies fail to break it; cross-model extraction confirms universality across nine models from 7B to frontier (\\S\\ref{sec:confirmation-bias}).\n\n\\item \\textbf{General diagnostic framework for trace-aggregation methods.} Three diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly predict success or failure across all 60 tested conditions spanning self-extraction, training-free remediation, cross-architecture verification, and oracle controls. Decision boundaries---$C_0 < 5\\%$ (degenerate), $K_\\text{eff} \\leq 1.3$ (diversity-limited), $\\text{BR} > 2\\times$ (bias-dominated), $\\kappa_\\text{same} \\geq 0.40$ (same-model ceiling)---provide zero-cost prediction of symbolic aggregation viability. The framework extends to any method extracting structured representations from LLM traces (\\S\\ref{sec:remediation}, \\S\\ref{sec:cross-arch}).\n\n\\item \\textbf{Process-level independence analysis.} CoT cosine similarity ($0.69$--$0.79$) exceeds answer-level $\\kappa$ ($0.45$--$0.74$) across four models from three families; under cross-model extraction on frontier models, SICA gain decreases monotonically with process similarity ($\\rho = -1.0$, $p = 0.008$; \\S\\ref{sec:process-kappa}).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tikzpicture}[\n    node distance=0.3cm and 0.1cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,\n                text width=1.2cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract logical\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}\n\\label{fig:pipeline}\n\\end{figure}\n",
      "numLines": 77,
      "startLine": 1,
      "totalLines": 77
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01AMphGhdXJwqonfEC7EB28n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "cd2dd9af-774b-44b9-a76c-cd56d975aeb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VprpwZvY7scDd5hbNYEFgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13978,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13978
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

_source line 10 · 2026-05-23T02:51:57.601Z_

<details><summary>↩ Tool result · `toolu_01AMphGhdXJwqonfEC7EB28n`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{SICA Pipeline}
5	\label{sec:pipeline}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\kappa$ \citep{fleiss1971kappa}), effective sample size reduces to
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa]
11	\end{equation}
12	(following \citet{ladha1992correlated}), motivating constraint-based aggregation.
13	
14	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
15	
16	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
17	
18	\looseness=-1
19	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
20	
21	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
22	\begin{equation}
23	\label{eq:maxsat}
24	\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
25	\end{equation}
26	Z3 \citep{demoura2008z3} solves this with a 10-second timeout. Answer assertion constraints ($\texttt{answer\_a} == \texttt{True}$, weight 1) ensure every candidate receives a nonzero base score, making SICA a strict generalization of SC.
27	
28	\paragraph{Scoring.} Let $\mathcal{C}^{\setminus} = \mathcal{C} \setminus \mathcal{C}^*$. Each candidate $a$ is scored by:
29	\begin{equation}
30	\label{eq:score}
31	\text{score}(a) = \sum_{c \in \mathcal{C}^*} w_c \cdot \sigma(c, a) - \alpha \sum_{c \in \mathcal{C}^{\setminus}} w_c \cdot \sigma(c, a),
32	\end{equation}
33	where $\sigma(c, a) = 1$ if $c$ was extracted from any trace producing answer $a$, and $\alpha = 0.5$. The selected answer is $a^* = \arg\max_{a} \text{score}(a)$.
34	
35	\paragraph{Degeneration condition.} If self-extracted constraints are coupled to their source answer, MAX-SAT retains nearly all ($|\mathcal{C}^{\setminus}| \approx 0$), and scoring degenerates to:
36	\begin{equation}
37	\label{eq:degenerate}
38	\text{score}(a) \approx \sum_{\substack{c \in \mathcal{C}^* \\ \text{source}(c) \to a}} w_c,
39	\end{equation}
40	equivalent to majority voting. We show in \S\ref{sec:confirmation-bias} that this degeneration occurs in practice.
41	
42	\paragraph{The $C_0$ diagnostic.} The multi-candidate rate $C_0 = |\{q : |\mathcal{A}(q)| > 1\}| / |\mathcal{Q}|$ is a zero-cost diagnostic: $C_0 < 5\%$ means SICA reduces to SC. $\alpha = 0.5$ is not critical (${\pm}0.49$\,pp across $\alpha \in [0, 1]$).
43	
44	\paragraph{Bias ratio.} We quantify extraction bias via the \emph{bias ratio}:
45	\begin{equation}\label{eq:mirage}
46	\text{BR}(M,T) = \frac{P(c \text{ supports } a_M \mid a_M \neq a^*)}{P(c \text{ supports } a^* \mid a_M \neq a^*)},
47	\end{equation}
48	where $c$ is a self-extracted constraint, $a_M$ the model's majority answer, and $a^*$ the ground truth. $\text{BR} > 1$ indicates constraints project model bias rather than provide independent verification; $\text{BR} = 1$ indicates unbiased extraction. We validate this metric empirically in \S\ref{sec:confirmation-bias}.
49	
50	\subsection{Experimental Setup}
51	\label{sec:exp-setup}
52	
53	\looseness=-1
54	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B). We also evaluate the universality of symbolic confirmation bias via cross-model extraction on five frontier models (gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro; Table~\ref{tab:frontier-scb}); Mistral-7B extracts constraints from target traces since closed-source APIs do not support self-extraction.
55	
56	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} (exploratory, $n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
57	
58	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "752b8803-3a1a-4e7a-91dd-b0acef7c1882",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{SICA Pipeline}\n\\label{sec:pipeline}\n\nSelf-Consistency (SC) \\citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\\kappa$ \\citep{fleiss1971kappa}), effective sample size reduces to\n\\begin{equation}\n\\label{eq:effk}\nK_{\\text{eff}} = K \\,/\\, [1 + (K{-}1) \\cdot \\kappa]\n\\end{equation}\n(following \\citet{ladha1992correlated}), motivating constraint-based aggregation.\n\nSymbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\\ref{fig:pipeline}).\n\n\\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\\{t_1, \\ldots, t_K\\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.\n\n\\looseness=-1\n\\paragraph{Constraint extraction.}\\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\\ref{app:prompts}); in practice, 99.0\\% of extracted constraints are propositional at the Z3 level, with only 1.0\\% using true quantifiers. The \\emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.\n\n\\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:\n\\begin{equation}\n\\label{eq:maxsat}\n\\mathcal{C}^* = \\arg\\max_{\\mathcal{S} \\subseteq \\mathcal{C}} \\sum_{c \\in \\mathcal{S}} w_c \\quad \\text{s.t.} \\quad \\mathcal{S} \\text{ is satisfiable.}\n\\end{equation}\nZ3 \\citep{demoura2008z3} solves this with a 10-second timeout. Answer assertion constraints ($\\texttt{answer\\_a} == \\texttt{True}$, weight 1) ensure every candidate receives a nonzero base score, making SICA a strict generalization of SC.\n\n\\paragraph{Scoring.} Let $\\mathcal{C}^{\\setminus} = \\mathcal{C} \\setminus \\mathcal{C}^*$. Each candidate $a$ is scored by:\n\\begin{equation}\n\\label{eq:score}\n\\text{score}(a) = \\sum_{c \\in \\mathcal{C}^*} w_c \\cdot \\sigma(c, a) - \\alpha \\sum_{c \\in \\mathcal{C}^{\\setminus}} w_c \\cdot \\sigma(c, a),\n\\end{equation}\nwhere $\\sigma(c, a) = 1$ if $c$ was extracted from any trace producing answer $a$, and $\\alpha = 0.5$. The selected answer is $a^* = \\arg\\max_{a} \\text{score}(a)$.\n\n\\paragraph{Degeneration condition.} If self-extracted constraints are coupled to their source answer, MAX-SAT retains nearly all ($|\\mathcal{C}^{\\setminus}| \\approx 0$), and scoring degenerates to:\n\\begin{equation}\n\\label{eq:degenerate}\n\\text{score}(a) \\approx \\sum_{\\substack{c \\in \\mathcal{C}^* \\\\ \\text{source}(c) \\to a}} w_c,\n\\end{equation}\nequivalent to majority voting. We show in \\S\\ref{sec:confirmation-bias} that this degeneration occurs in practice.\n\n\\paragraph{The $C_0$ diagnostic.} The multi-candidate rate $C_0 = |\\{q : |\\mathcal{A}(q)| > 1\\}| / |\\mathcal{Q}|$ is a zero-cost diagnostic: $C_0 < 5\\%$ means SICA reduces to SC. $\\alpha = 0.5$ is not critical (${\\pm}0.49$\\,pp across $\\alpha \\in [0, 1]$).\n\n\\paragraph{Bias ratio.} We quantify extraction bias via the \\emph{bias ratio}:\n\\begin{equation}\\label{eq:mirage}\n\\text{BR}(M,T) = \\frac{P(c \\text{ supports } a_M \\mid a_M \\neq a^*)}{P(c \\text{ supports } a^* \\mid a_M \\neq a^*)},\n\\end{equation}\nwhere $c$ is a self-extracted constraint, $a_M$ the model's majority answer, and $a^*$ the ground truth. $\\text{BR} > 1$ indicates constraints project model bias rather than provide independent verification; $\\text{BR} = 1$ indicates unbiased extraction. We validate this metric empirically in \\S\\ref{sec:confirmation-bias}.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp-setup}\n\n\\looseness=-1\n\\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\\citep{dubey2024llama3}, and QwQ-32B~\\citep{qwen2024qwq} (7B--32B). We also evaluate the universality of symbolic confirmation bias via cross-model extraction on five frontier models (gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro; Table~\\ref{tab:frontier-scb}); Mistral-7B extracts constraints from target traces since closed-source APIs do not support self-extraction.\n\n\\paragraph{Datasets.} FOLIO~\\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\\citep{cobbe2021gsm8k} (exploratory, $n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\\%$).\n\n\\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\\text{ext}}{=}0.3$, $\\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\\alpha{=}0.05$); 95\\% bootstrap CIs ($10{,}000$ resamples) for $n \\geq 200$. SICA incurs $4.5{\\times}$ SC wall-clock; extraction accounts for 76\\% of overhead.\n",
      "numLines": 59,
      "startLine": 1,
      "totalLines": 59
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01615kSwhUMgxU2wwjEM3fRt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "e95367d9-8595-4a9d-a382-35f1cbba6f34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VprpwZvY7scDd5hbNYEFgW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13978,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13978
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

_source line 12 · 2026-05-23T02:51:58.087Z_

<details><summary>↩ Tool result · `toolu_01615kSwhUMgxU2wwjEM3fRt`</summary>

```text
1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. A shuffle control reveals this bias is \emph{structural}: randomizing constraint--answer associations while preserving per-trace counts yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($p > 0.7$), indicating that BR reflects the trace-count distribution rather than extraction-specific error. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting. This vacuity is $\alpha$-insensitive: agreement $\geq$99\% across $\alpha \in \{0.1, \ldots, 0.9\}$ (Table~\ref{tab:alpha-ablation}).
8	
9	\looseness=-1 This pattern generalizes: $4.97\times$ (Mistral), $3.85\times$ (Qwen-14B), $2.88\times$ (LLaMA), all $> 1.0$ with 95\% bootstrap CIs (Table~\ref{tab:cross-model-bias}). Cross-model extraction confirms universality across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb}). BR $> 1$ further holds across all eight cells of a $2{\times}2$ generator${\times}$extractor matrix on FOLIO and ProofWriter (range $1.94$--$2.70$; Appendix~\ref{app:2x2}). Constraints use trace-specific variables (56.4\% zero cross-answer overlap), collapsing aggregation to majority voting.
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3pt}
15	\caption{Symbolic confirmation bias across nine models on FOLIO ($n = 204$). BR: mean per-problem bias ratio. $n_\text{err}$: number of incorrect instances on which BR is computed. $\Delta$: SICA $-$ SC (pp). Ext.: $^a$self-extraction; $^b$cross-model (Mistral-7B extracts FOL from target traces). $^*$Interim ($n = 95/204$). All models exhibit $\text{BR} > 1$; BR estimates for high-accuracy models ($n_\text{err} < 40$) have wider confidence intervals; Gemini ($n_\text{err} \approx 12$) should be interpreted with particular caution. Process-level similarity ($\kappa_{\text{proc}}$) ranges from $0.25$ (R1-Distill) to $0.79$ (gpt-4o/4.1/Gemini); see Table~\ref{tab:cross-model-process}.}
16	\label{tab:frontier-scb}
17	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llrrrrl@{}}
18	\toprule
19	Model & Ext. & SC (\%) & $n_\text{err}$ & BR & $\Delta$ (pp) \\
20	\midrule
21	Mistral-7B & $^a$ & 55.88 & 90 & 4.97 & 0.00 \\
22	LLaMA-8B & $^a$ & \textrm{---} & \textrm{---} & 2.88 & \textrm{---} \\
23	Qwen-14B & $^a$ & 75.98 & 49 & 3.85 & $-$0.49 \\
24	\addlinespace
25	R1-Distill-8B & $^b$ & 74.51 & 52 & 2.92 & $+$2.45 \\
26	gpt-4o & $^a$ & 73.91 & 53 & 2.94 & $-$1.80 \\
27	gpt-4.1 & $^b$ & 82.84 & 35 & 2.70 & $-$1.47 \\
28	gpt-5.5 & $^b$ & 84.31 & 32 & 3.48 & $+$0.49 \\
29	o3 & $^b$ & 82.65 & 35 & 1.66 & 0.00 \\
30	Gemini-2.5-Pro$^*$ & $^b$ & 87.37 & 12 & 2.79 & $-$1.10 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	
35	\looseness=-1 Two controls rule out answer leakage. BR is uniform across early, mid, and late reasoning steps (Fisher $p = 0.71$); high-consensus errors amplify to $\text{BR} = 18.8\times$ versus $2.7\times$ for low-consensus ($p < 0.001$). Removing the answer sentence from traces before extraction yields no BR decrease (Wilcoxon $p \geq 0.12$) despite significant accuracy loss (McNemar $p < 0.013$). Symbolic confirmation bias reflects a distributional prior embedded throughout reasoning, not answer contamination.
36	
37	\looseness=-1 Reasoning-process overlap exceeds answer-level correlation: on Mistral-7B FOLIO, mean process similarity (pairwise TF-IDF cosine; Appendix~\ref{app:process-gradient}) reaches 0.69, far exceeding answer-level $\kappa = 0.46$. The gap generalizes across four families (Table~\ref{tab:cross-model-process}). Under cross-model extraction, SICA gain decreases monotonically with process similarity ($\rho = -1.0$, $p = 0.008$; Table~\ref{tab:process-gradient}).
38	
39	\subsection{Why Remediation Fails}
40	\label{sec:remediation}
41	\label{sec:diagnostics}
42	\label{sec:interventions}
43	
44	\looseness=-1 All 27 training-free remediation strategies spanning four categories produce neutral-to-negative results (Figure~\ref{fig:interventions-summary}; Appendices~\ref{app:extraction}--\ref{app:entropy}). The pattern reveals a fundamental independence-accuracy trade-off: methods that successfully break trace correlation simultaneously destroy accuracy, while methods that preserve accuracy fail to achieve independence.
45	
46	\looseness=-1 Four representative failure modes illustrate this trade-off. \emph{Debate} ($\kappa = 0.15$, $\Delta = -18.6$\,pp) successfully breaks trace correlation but collapses accuracy: same-model diversity and quality are at odds. \emph{Cross-model extraction} (using a different LLM as extractor) decreases $\kappa$ slightly but $\Delta \approx 0$, because same-family models share systematic biases (Appendix Table~\ref{tab:kappa_generalization}). \emph{Contrastive prompting} produces imbalanced output (94 pro vs.\ 65 con constraints), indicating confirmation bias transfers to constraint generation. \emph{Iterative constraint generation}, which refines constraints across multiple extraction rounds, reduces surface-level duplication but the refined constraints still align with the model's majority answer.
47	
48	\looseness=-1 All non-debate strategies cluster at $\kappa \approx 0.40$--$0.47$, a same-model ceiling observed across three families. This ceiling is not a property of any single extraction method but of the model itself: regardless of prompting strategy, self-extraction cannot produce constraints that are independent of the model's distributional prior. The oracle ceiling ($+29.90$\,pp with gold constraints) proves the mechanism is sound; self-extraction captures only ${\sim}$12\%, localizing the bottleneck to extraction quality rather than the MAX-SAT apparatus.
49	
50	\looseness=-1 No individual strategy achieves significance after correction (Appendix~\ref{app:intervention-individual}). The consistent failure across 27 strategies, four categories, and three model families suggests that symbolic confirmation bias is not a fixable extraction artifact but an intrinsic property of self-referential constraint generation.
51	
52	\begin{figure}[t]
53	\centering
54	\includegraphics[width=\columnwidth]{figures/fig2_interventions_compact.pdf}
55	\caption{Twenty-three of 27 training-free strategies across four categories (four additional strategies tested but omitted for clarity). All produce neutral-to-negative $\Delta$ vs.\ SC. Grey band: $\pm 1$\,pp noise zone.}
56	\label{fig:interventions-summary}
57	\end{figure}
58	
59	\subsection{Diagnostic Framework}
60	\label{sec:diagnostic-framework}
61	
62	\looseness=-1 Three zero-cost diagnostics predict the outcome of any trace-aggregation method from a $K = 12$ pilot run: (1) the degenerate-regime indicator $C_0 < 5\%$ (SICA reduces to SC); (2) the diversity floor $K_\text{eff} \leq 1.3$ (insufficient vote diversity for any aggregation gain); (3) the bias ratio BR combined with SC regime (Type~A: SC $\geq 60\%$ with BR $> 1$ predicts confirmation-bias degradation; Type~C: SC $\leq 40\%$ predicts error amplification). These boundaries correctly classify all 60 tested conditions across four model families and three datasets.
63	
64	\looseness=-1 Decision boundaries ($C_0 < 5\%$, $K_\text{eff} \leq 1.3$, SC $< 40\%$) were derived from Mistral-7B and Qwen2.5-14B conditions. We evaluate prospectively on held-out LLaMA-3.1-8B, a different model family not used in boundary derivation: on FOLIO (SC $= 66.18\%$, $C_0 = 61.8\%$, $K_\text{eff} = 2.17$), the framework predicts Type~A confirmation bias ($\Delta \leq 0$); the observed $\Delta = -4.41$\,pp confirms the prediction.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "b7b629d5-892f-4ce4-ac90-235ffa68298d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex",
      "content": "\\section{The Symbolic Mirage}\n\\label{sec:analysis}\n\n\\subsection{Symbolic Confirmation Bias}\n\\label{sec:confirmation-bias}\n\n\\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\\% of constraints support the incorrect answer---bias ratio $4.97\\times$ (Table~\\ref{tab:cross-model-bias})---and 94\\% of errors overlap with SC. A shuffle control reveals this bias is \\emph{structural}: randomizing constraint--answer associations while preserving per-trace counts yields $\\text{BR}_\\text{null} \\approx \\text{BR}_\\text{obs}$ ($p > 0.7$), indicating that BR reflects the trace-count distribution rather than extraction-specific error. Z3 rejects only 3.4\\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\\% of problems (Table~\\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\\ref{eq:degenerate}): 99\\% of constraints pass Z3 validation yet add no information beyond majority voting. This vacuity is $\\alpha$-insensitive: agreement $\\geq$99\\% across $\\alpha \\in \\{0.1, \\ldots, 0.9\\}$ (Table~\\ref{tab:alpha-ablation}).\n\n\\looseness=-1 This pattern generalizes: $4.97\\times$ (Mistral), $3.85\\times$ (Qwen-14B), $2.88\\times$ (LLaMA), all $> 1.0$ with 95\\% bootstrap CIs (Table~\\ref{tab:cross-model-bias}). Cross-model extraction confirms universality across nine models from 7B to frontier (BR $1.66$--$4.97\\times$; Table~\\ref{tab:frontier-scb}). BR $> 1$ further holds across all eight cells of a $2{\\times}2$ generator${\\times}$extractor matrix on FOLIO and ProofWriter (range $1.94$--$2.70$; Appendix~\\ref{app:2x2}). Constraints use trace-specific variables (56.4\\% zero cross-answer overlap), collapsing aggregation to majority voting.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Symbolic confirmation bias across nine models on FOLIO ($n = 204$). BR: mean per-problem bias ratio. $n_\\text{err}$: number of incorrect instances on which BR is computed. $\\Delta$: SICA $-$ SC (pp). Ext.: $^a$self-extraction; $^b$cross-model (Mistral-7B extracts FOL from target traces). $^*$Interim ($n = 95/204$). All models exhibit $\\text{BR} > 1$; BR estimates for high-accuracy models ($n_\\text{err} < 40$) have wider confidence intervals; Gemini ($n_\\text{err} \\approx 12$) should be interpreted with particular caution. Process-level similarity ($\\kappa_{\\text{proc}}$) ranges from $0.25$ (R1-Distill) to $0.79$ (gpt-4o/4.1/Gemini); see Table~\\ref{tab:cross-model-process}.}\n\\label{tab:frontier-scb}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Ext. & SC (\\%) & $n_\\text{err}$ & BR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $^a$ & 55.88 & 90 & 4.97 & 0.00 \\\\\nLLaMA-8B & $^a$ & \\textrm{---} & \\textrm{---} & 2.88 & \\textrm{---} \\\\\nQwen-14B & $^a$ & 75.98 & 49 & 3.85 & $-$0.49 \\\\\n\\addlinespace\nR1-Distill-8B & $^b$ & 74.51 & 52 & 2.92 & $+$2.45 \\\\\ngpt-4o & $^a$ & 73.91 & 53 & 2.94 & $-$1.80 \\\\\ngpt-4.1 & $^b$ & 82.84 & 35 & 2.70 & $-$1.47 \\\\\ngpt-5.5 & $^b$ & 84.31 & 32 & 3.48 & $+$0.49 \\\\\no3 & $^b$ & 82.65 & 35 & 1.66 & 0.00 \\\\\nGemini-2.5-Pro$^*$ & $^b$ & 87.37 & 12 & 2.79 & $-$1.10 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\looseness=-1 Two controls rule out answer leakage. BR is uniform across early, mid, and late reasoning steps (Fisher $p = 0.71$); high-consensus errors amplify to $\\text{BR} = 18.8\\times$ versus $2.7\\times$ for low-consensus ($p < 0.001$). Removing the answer sentence from traces before extraction yields no BR decrease (Wilcoxon $p \\geq 0.12$) despite significant accuracy loss (McNemar $p < 0.013$). Symbolic confirmation bias reflects a distributional prior embedded throughout reasoning, not answer contamination.\n\n\\looseness=-1 Reasoning-process overlap exceeds answer-level correlation: on Mistral-7B FOLIO, mean process similarity (pairwise TF-IDF cosine; Appendix~\\ref{app:process-gradient}) reaches 0.69, far exceeding answer-level $\\kappa = 0.46$. The gap generalizes across four families (Table~\\ref{tab:cross-model-process}). Under cross-model extraction, SICA gain decreases monotonically with process similarity ($\\rho = -1.0$, $p = 0.008$; Table~\\ref{tab:process-gradient}).\n\n\\subsection{Why Remediation Fails}\n\\label{sec:remediation}\n\\label{sec:diagnostics}\n\\label{sec:interventions}\n\n\\looseness=-1 All 27 training-free remediation strategies spanning four categories produce neutral-to-negative results (Figure~\\ref{fig:interventions-summary}; Appendices~\\ref{app:extraction}--\\ref{app:entropy}). The pattern reveals a fundamental independence-accuracy trade-off: methods that successfully break trace correlation simultaneously destroy accuracy, while methods that preserve accuracy fail to achieve independence.\n\n\\looseness=-1 Four representative failure modes illustrate this trade-off. \\emph{Debate} ($\\kappa = 0.15$, $\\Delta = -18.6$\\,pp) successfully breaks trace correlation but collapses accuracy: same-model diversity and quality are at odds. \\emph{Cross-model extraction} (using a different LLM as extractor) decreases $\\kappa$ slightly but $\\Delta \\approx 0$, because same-family models share systematic biases (Appendix Table~\\ref{tab:kappa_generalization}). \\emph{Contrastive prompting} produces imbalanced output (94 pro vs.\\ 65 con constraints), indicating confirmation bias transfers to constraint generation. \\emph{Iterative constraint generation}, which refines constraints across multiple extraction rounds, reduces surface-level duplication but the refined constraints still align with the model's majority answer.\n\n\\looseness=-1 All non-debate strategies cluster at $\\kappa \\approx 0.40$--$0.47$, a same-model ceiling observed across three families. This ceiling is not a property of any single extraction method but of the model itself: regardless of prompting strategy, self-extraction cannot produce constraints that are independent of the model's distributional prior. The oracle ceiling ($+29.90$\\,pp with gold constraints) proves the mechanism is sound; self-extraction captures only ${\\sim}$12\\%, localizing the bottleneck to extraction quality rather than the MAX-SAT apparatus.\n\n\\looseness=-1 No individual strategy achieves significance after correction (Appendix~\\ref{app:intervention-individual}). The consistent failure across 27 strategies, four categories, and three model families suggests that symbolic confirmation bias is not a fixable extraction artifact but an intrinsic property of self-referential constraint generation.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_interventions_compact.pdf}\n\\caption{Twenty-three of 27 training-free strategies across four categories (four additional strategies tested but omitted for clarity). All produce neutral-to-negative $\\Delta$ vs.\\ SC. Grey band: $\\pm 1$\\,pp noise zone.}\n\\label{fig:interventions-summary}\n\\end{figure}\n\n\\subsection{Diagnostic Framework}\n\\label{sec:diagnostic-framework}\n\n\\looseness=-1 Three zero-cost diagnostics predict the outcome of any trace-aggregation method from a $K = 12$ pilot run: (1) the degenerate-regime indicator $C_0 < 5\\%$ (SICA reduces to SC); (2) the diversity floor $K_\\text{eff} \\leq 1.3$ (insufficient vote diversity for any aggregation gain); (3) the bias ratio BR combined with SC regime (Type~A: SC $\\geq 60\\%$ with BR $> 1$ predicts confirmation-bias degradation; Type~C: SC $\\leq 40\\%$ predicts error amplification). These boundaries correctly classify all 60 tested conditions across four model families and three datasets.\n\n\\looseness=-1 Decision boundaries ($C_0 < 5\\%$, $K_\\text{eff} \\leq 1.3$, SC $< 40\\%$) were derived from Mistral-7B and Qwen2.5-14B conditions. We evaluate prospectively on held-out LLaMA-3.1-8B, a different model family not used in boundary derivation: on FOLIO (SC $= 66.18\\%$, $C_0 = 61.8\\%$, $K_\\text{eff} = 2.17$), the framework predicts Type~A confirmation bias ($\\Delta \\leq 0$); the observed $\\Delta = -4.41$\\,pp confirms the prediction.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the new introduction.tex following the task instructions precisely.

Key things to do:
1. Keep `\section{Introduction}\label{sec:introduction}`
2. Sharper Z3 paradox hook opening
3. Concise contributions (3 items, 3 lines each max)
4. Power caveat
5. Softened cross-architecture claims
6. Keep Figure 1 TikZ exactly as is (lines 39-76)
7. Target ~1.0 page
8. No AI clichés, no dashes (em-dash/en-dash for explanation)


9. `\looseness=-1` before dense paragraphs
10. Use range "1.66–4.97×" for BR

Now I'm checking the cross-references in the other sections. The method.tex references look good with the section and figure labels. For analysis.tex, I need to verify that the cross-architecture section reference exists and is properly labeled, along with the confirmation bias and remediation sections.

Looking at the contributions text, I notice the em-dash usage is actually for number ranges like "1.66–4.97×", which follows the allowed convention for numerical intervals rather than explanatory purposes.

Now I'm structuring the introduction with five main sections: an opening that hooks on the Z3 paradox, then introducing SICA and its negative findings, followed by the symbolic confirmation bias discovery, the failed remediation attempts, and finally the three contribution bullets. I need to be careful about punctuation—avoiding em-dashes for explanatory asides while keeping the number range dashes intact.

The opening paragraph will reframe that formal verification observation without the em-dash, using a comma instead. For the second paragraph, I'm bridging from SICA to the confirmation bias result. The third section focuses on what makes this bias structural and symbolic. The fourth covers why remediation fails and what escape route we found. Then I'll list the three contributions concisely, each within three lines, before copying Figure 1 exactly as provided. I'm looking at the three main contributions laid out in LaTeX format. The first one describes how symbolic verification becomes vacuous due to confirmation bias across multiple models, with specific metrics and remediation attempts. The second contribution outlines a diagnostic framework with three metrics that can predict whether symbolic aggregation will work from just a pilot run. The third shows that an alternative NLI verification approach can escape this bottleneck, with performance gains that diminish as the underlying generator improves. I should incorporate these exactly as provided into the full document. Self-Consistency plateaus for stronger models due to correlated errors that voting can't resolve, so I'm investigating whether formal constraint extraction can improve aggregation through SICA, which uses MAX-SAT to select answers—but across extensive experiments with multiple models and domains, no significant improvements emerge even after accounting for multiple comparisons.

The core problem is symbolic confirmation bias: when models make mistakes, their self-extracted constraints overwhelmingly support the wrong answer, with bias ratios ranging from 1.66 to nearly 5 times across different model sizes. A shuffle control rules out extraction-specific errors, confirming this is a fundamental limitation—even with a correct solver, the constraints add nothing beyond what majority voting already provides, extending the known inability of LLMs to self-correct without external input.

I'm now testing numerous training-free fixes to address this bias, but they're yielding neutral or negative results, which suggests the problem runs deeper than simple remediation strategies can handle. The symbolic verification approach creates a confirmation bias problem where MAX-SAT becomes functionally equivalent to simple majority voting on most cases, a structural issue confirmed through control experiments and failed remediation attempts. The diagnostic framework successfully predicts whether symbolic aggregation will work from minimal pilot data, while cross-architecture verification shows promise in breaking through the accuracy bottleneck, though gains diminish as generator performance improves. I'm verifying the final details against the requirements—checking that each contribution fits within three lines, confirming the power caveat and softened cross-architecture language are present, and making sure the BR range appears where specified. The formatting looks clean with no em-dashes or sentences ending in -ing phrases, and I'm avoiding any overused AI terminology. Ready to write out the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "eaeb649f-f016-4a42-adac-5c8f8188a7a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ozpMxLwEkMqMujEwLMFsv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13533,
      "cache_read_input_tokens": 25819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13533
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

Now I have all the context. Writing the rewritten introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "c0f0dc9a-4340-4b63-aba9-c47ec0f3e46e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ozpMxLwEkMqMujEwLMFsv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13533,
      "cache_read_input_tokens": 25819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13533
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

<details open><summary>🔧 Tool call — Write · `toolu_01H6xCmwC1FgQ19G43Jqm2MF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\\label{sec:introduction}\n\n\\looseness=-1\nCan a provably sound formal solver improve LLM reasoning if the constraints it operates on are self-extracted from the model's own traces? We show that the answer is no: Z3 validates 99\\% of self-extracted constraints, yet MAX-SAT produces answers identical to majority voting on 94.4\\% of problems. The formal verification layer is vacuous, not because the solver fails, but because extraction inherits the model's distributional bias. This finding challenges a natural extension of Self-Consistency (SC) \\citep{wang2023sc}, which samples $K$ chain-of-thought traces and selects the majority answer. SC's gains plateau and decline for strong models \\citep{loo2025reevaluating}; the gap between its theoretical promise (independent voters converge to truth \\citep{condorcet1785, ladha1992correlated}) and practice points to correlated errors that majority voting cannot correct.\n\n\\looseness=-1\nWe study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}). Across six models (7B--32B), three reasoning domains, and over 3{,}000 condition-evaluations with multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\\ref{tab:main_results}). Four conditions are confirmed equivalent within $\\pm$2\\,pp; ten remain underpowered for effects below ${\\sim}$2\\,pp.\n\n\\looseness=-1\nThe failure traces to \\emph{symbolic confirmation bias}: on problems where the model errs, 83.3\\% of self-extracted constraints support the incorrect majority answer (bias ratio $1.66$--$4.97\\times$ across nine models from 7B to frontier; \\S\\ref{sec:confirmation-bias}). A shuffle control confirms this bias is structural, proportional to the trace-count distribution rather than extraction-specific error ($p > 0.7$). Prior work shows LLMs cannot self-correct without external feedback \\citep{huang2024selfcorrect}; we demonstrate that this limitation extends to formal self-verification: even with a provably correct solver, self-extracted constraints carry no information beyond majority voting.\n\n\\looseness=-1\nTwenty-seven training-free remediation strategies produce neutral-to-negative results (\\S\\ref{sec:remediation}), revealing a fundamental independence-accuracy trade-off. Cross-architecture verification provides preliminary evidence of escaping the bottleneck: a structurally independent NLI verifier yields $+6.67$\\,pp on the weakest generator ($p < 0.001$); domain-adapted verification extends gains to generators with SC up to 72\\% with monotonically decreasing benefit (\\S\\ref{sec:cross-arch}). Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions (\\S\\ref{sec:diagnostic-framework}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction: symbolic confirmation bias (BR $1.66$--$4.97\\times$ across nine models) renders MAX-SAT equivalent to majority voting on 94.4\\% of problems. A shuffle control and 27 failed remediation strategies confirm the bias is structural (\\S\\ref{sec:confirmation-bias}, \\S\\ref{sec:remediation}).\n\n\\item \\textbf{Diagnostic framework.} Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions, providing practitioners with a priori prediction of symbolic aggregation viability from a $K{=}12$ pilot run (\\S\\ref{sec:diagnostic-framework}).\n\n\\item \\textbf{Cross-architecture escape.} Preliminary evidence that structurally independent NLI verification escapes the bottleneck ($+6.67$\\,pp on the weakest generator, $p < 0.001$), with gain decreasing monotonically as generator accuracy increases (\\S\\ref{sec:cross-arch}).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tikzpicture}[\n    node distance=0.3cm and 0.1cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,\n                text width=1.2cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract logical\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}\n\\label{fig:pipeline}\n\\end{figure}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "baf6928b-31b4-43d0-bd54-8ec6aebccef0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ozpMxLwEkMqMujEwLMFsv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13533,
      "cache_read_input_tokens": 25819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13533
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

_source line 16 · 2026-05-23T02:53:25.433Z_

<details><summary>↩ Tool result · `toolu_01H6xCmwC1FgQ19G43Jqm2MF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "415857f0-7f8d-4743-8fad-9e8dacf4e90b",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\\label{sec:introduction}\n\n\\looseness=-1\nCan a provably sound formal solver improve LLM reasoning if the constraints it operates on are self-extracted from the model's own traces? We show that the answer is no: Z3 validates 99\\% of self-extracted constraints, yet MAX-SAT produces answers identical to majority voting on 94.4\\% of problems. The formal verification layer is vacuous, not because the solver fails, but because extraction inherits the model's distributional bias. This finding challenges a natural extension of Self-Consistency (SC) \\citep{wang2023sc}, which samples $K$ chain-of-thought traces and selects the majority answer. SC's gains plateau and decline for strong models \\citep{loo2025reevaluating}; the gap between its theoretical promise (independent voters converge to truth \\citep{condorcet1785, ladha1992correlated}) and practice points to correlated errors that majority voting cannot correct.\n\n\\looseness=-1\nWe study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}). Across six models (7B--32B), three reasoning domains, and over 3{,}000 condition-evaluations with multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\\ref{tab:main_results}). Four conditions are confirmed equivalent within $\\pm$2\\,pp; ten remain underpowered for effects below ${\\sim}$2\\,pp.\n\n\\looseness=-1\nThe failure traces to \\emph{symbolic confirmation bias}: on problems where the model errs, 83.3\\% of self-extracted constraints support the incorrect majority answer (bias ratio $1.66$--$4.97\\times$ across nine models from 7B to frontier; \\S\\ref{sec:confirmation-bias}). A shuffle control confirms this bias is structural, proportional to the trace-count distribution rather than extraction-specific error ($p > 0.7$). Prior work shows LLMs cannot self-correct without external feedback \\citep{huang2024selfcorrect}; we demonstrate that this limitation extends to formal self-verification: even with a provably correct solver, self-extracted constraints carry no information beyond majority voting.\n\n\\looseness=-1\nTwenty-seven training-free remediation strategies produce neutral-to-negative results (\\S\\ref{sec:remediation}), revealing a fundamental independence-accuracy trade-off. Cross-architecture verification provides preliminary evidence of escaping the bottleneck: a structurally independent NLI verifier yields $+6.67$\\,pp on the weakest generator ($p < 0.001$); domain-adapted verification extends gains to generators with SC up to 72\\% with monotonically decreasing benefit (\\S\\ref{sec:cross-arch}). Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions (\\S\\ref{sec:diagnostic-framework}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction: symbolic confirmation bias (BR $1.66$--$4.97\\times$ across nine models) renders MAX-SAT equivalent to majority voting on 94.4\\% of problems. A shuffle control and 27 failed remediation strategies confirm the bias is structural (\\S\\ref{sec:confirmation-bias}, \\S\\ref{sec:remediation}).\n\n\\item \\textbf{Diagnostic framework.} Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions, providing practitioners with a priori prediction of symbolic aggregation viability from a $K{=}12$ pilot run (\\S\\ref{sec:diagnostic-framework}).\n\n\\item \\textbf{Cross-architecture escape.} Preliminary evidence that structurally independent NLI verification escapes the bottleneck ($+6.67$\\,pp on the weakest generator, $p < 0.001$), with gain decreasing monotonically as generator accuracy increases (\\S\\ref{sec:cross-arch}).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tikzpicture}[\n    node distance=0.3cm and 0.1cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,\n                text width=1.2cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract logical\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}\n\\label{fig:pipeline}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 39,
        "newStart": 1,
        "newLines": 24,
        "lines": [
          " \\section{Introduction}\\label{sec:introduction}",
          " ",
          "-Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \\citep{snell2025scaling, guo2025deepseekr1}.",
          "-The dominant aggregation strategy, Self-Consistency (SC) \\citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.",
          "-SC is simple, model-agnostic, and effective---but it is hitting a ceiling.",
          "-\\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.",
          "-The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.",
          "+\\looseness=-1",
          "+Can a provably sound formal solver improve LLM reasoning if the constraints it operates on are self-extracted from the model's own traces? We show that the answer is no: Z3 validates 99\\% of self-extracted constraints, yet MAX-SAT produces answers identical to majority voting on 94.4\\% of problems. The formal verification layer is vacuous, not because the solver fails, but because extraction inherits the model's distributional bias. This finding challenges a natural extension of Self-Consistency (SC) \\citep{wang2023sc}, which samples $K$ chain-of-thought traces and selects the majority answer. SC's gains plateau and decline for strong models \\citep{loo2025reevaluating}; the gap between its theoretical promise (independent voters converge to truth \\citep{condorcet1785, ladha1992correlated}) and practice points to correlated errors that majority voting cannot correct.",
          " ",
          "-Confidence-weighted \\citep{taubenfeld2025cisc} and universal \\citep{chen2024usc} extensions alleviate this, but the core limitation persists.",
          "-Recent neuro-symbolic methods \\citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.",
          "-A simpler question precedes these: can the \\emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?",
          "-No prior work has systematically evaluated this.",
          "+\\looseness=-1",
          "+We study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}). Across six models (7B--32B), three reasoning domains, and over 3{,}000 condition-evaluations with multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\\ref{tab:main_results}). Four conditions are confirmed equivalent within $\\pm$2\\,pp; ten remain underpowered for effects below ${\\sim}$2\\,pp.",
          " ",
          "-We ground our analysis in the Condorcet Jury Theorem (CJT) \\citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \\citep{austensmith1996}.",
          "-When independence fails \\citep{ladha1992correlated}, additional samples carry diminishing information.",
          "-Measuring inter-trace agreement with Fleiss' $\\kappa$ \\citep{fleiss1971kappa}, we find $\\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\\text{eff}}$ as an ordinal diagnostic of vote diversity ($K_{\\text{eff}} \\approx 1.2$--$3.6$ for nominal $K = 12$; \\S\\ref{sec:condorcet}).",
          "-Chain-of-thought cosine similarity ($0.69$) far exceeds answer-level $\\kappa$ ($0.46$), revealing that traces share reasoning processes even when they diverge on final answers (\\S\\ref{sec:process-kappa}).",
          "-When the same model extracts logical constraints from these correlated traces, the constraints exhibit \\emph{symbolic confirmation bias} (SCB): on problems where the model errs, 83.3\\% of self-extracted constraints support the wrong majority answer (bias ratios $1.66$--$4.97\\times$ across nine models), and 94\\% of errors overlap with SC (\\S\\ref{sec:confirmation-bias}).",
          "-A shuffle control shows this bias is structural: it reflects the trace-count distribution rather than extraction-specific error.",
          "-Self-extraction cannot supply the independent signal that CJT requires.",
          "+\\looseness=-1",
          "+The failure traces to \\emph{symbolic confirmation bias}: on problems where the model errs, 83.3\\% of self-extracted constraints support the incorrect majority answer (bias ratio $1.66$--$4.97\\times$ across nine models from 7B to frontier; \\S\\ref{sec:confirmation-bias}). A shuffle control confirms this bias is structural, proportional to the trace-count distribution rather than extraction-specific error ($p > 0.7$). Prior work shows LLMs cannot self-correct without external feedback \\citep{huang2024selfcorrect}; we demonstrate that this limitation extends to formal self-verification: even with a provably correct solver, self-extracted constraints carry no information beyond majority voting.",
          " ",
          "-We study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}).",
          "-Across six open-source models (7B--32B), three domains (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}, LogiQA \\citep{liu2020logiqa}), and over 3,000 condition-evaluations with four-seed replication, twenty-seven training-free remediation strategies spanning fifteen families all produce neutral or negative results (Table~\\ref{tab:main_results}).",
          "-Prior work shows LLMs struggle with natural-language self-correction \\citep{huang2024selfcorrect} and that LLM-generated logical formulas can be unreliable \\citep{stechly2025selfverification}. Our formal channel is provably sound---the failure is precisely localizable to the extraction step. The assumption that formalizing reasoning provides \\emph{independent} verification evidence fails not because Z3 is unreliable (99\\% of constraints are syntactically valid), but because extraction inherits the model's biases: MAX-SAT produces answers identical to count-only aggregation on 94.4\\% of problems, rendering the formal layer vacuous.",
          "+\\looseness=-1",
          "+Twenty-seven training-free remediation strategies produce neutral-to-negative results (\\S\\ref{sec:remediation}), revealing a fundamental independence-accuracy trade-off. Cross-architecture verification provides preliminary evidence of escaping the bottleneck: a structurally independent NLI verifier yields $+6.67$\\,pp on the weakest generator ($p < 0.001$); domain-adapted verification extends gains to generators with SC up to 72\\% with monotonically decreasing benefit (\\S\\ref{sec:cross-arch}). Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions (\\S\\ref{sec:diagnostic-framework}).",
          " ",
          "-Oracle controls confirm the mechanism is sound ($+29.90$\\,pp Mistral-7B, $+13.73$\\,pp Qwen-14B on FOLIO, $p < 0.001$; Appendix~\\ref{app:oracle}), yet self-extraction captures only ${\\sim}$12\\% of this ceiling.",
          "-The central finding is a persistent independence-accuracy trade-off \\citep{krogh1994neural}: Debate reduces $\\kappa$ to 0.15 but collapses accuracy ($-18.6$\\,pp); other methods cluster at $\\kappa \\approx 0.40$--$0.47$, a same-model ceiling across three families (\\S\\ref{sec:remediation}).",
          "-A cross-architecture proof-of-concept escapes the bottleneck: zero-shot DeBERTa NLI yields $+6.67$\\,pp on Mistral-7B ProofWriter ($p < 0.001$) but no significant gain for stronger generators; domain-adapted NLI amplifies gains to $+$12--26\\,pp ($p < 0.0001$), extending to generators with SC up to 72\\% (\\S\\ref{sec:cross-arch}).",
          "-",
          " Our contributions are:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "-\\item \\textbf{Quantifying symbolic confirmation bias in formal self-verification.} While the general difficulty of LLM self-correction is known \\citep{huang2024selfcorrect}, we provide the first quantitative characterization of symbolic confirmation bias in formal self-verification, demonstrating that provably sound verification machinery becomes informationally vacuous under self-extraction: 83.3\\% of self-extracted constraints support the wrong answer (BR $1.66$--$4.97\\times$ across nine models), yet 99\\% pass Z3 validation. A shuffle control and MAX-SAT ablation show this bias is structural---the formal layer adds no information beyond majority voting. Twenty-seven training-free strategies fail to break it; cross-model extraction confirms universality across nine models from 7B to frontier (\\S\\ref{sec:confirmation-bias}).",
          "+\\item \\textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction: symbolic confirmation bias (BR $1.66$--$4.97\\times$ across nine models) renders MAX-SAT equivalent to majority voting on 94.4\\% of problems. A shuffle control and 27 failed remediation strategies confirm the bias is structural (\\S\\ref{sec:confirmation-bias}, \\S\\ref{sec:remediation}).",
          " ",
          "-\\item \\textbf{General diagnostic framework for trace-aggregation methods.} Three diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly predict success or failure across all 60 tested conditions spanning self-extraction, training-free remediation, cross-architecture verification, and oracle controls. Decision boundaries---$C_0 < 5\\%$ (degenerate), $K_\\text{eff} \\leq 1.3$ (diversity-limited), $\\text{BR} > 2\\times$ (bias-dominated), $\\kappa_\\text{same} \\geq 0.40$ (same-model ceiling)---provide zero-cost prediction of symbolic aggregation viability. The framework extends to any method extracting structured representations from LLM traces (\\S\\ref{sec:remediation}, \\S\\ref{sec:cross-arch}).",
          "+\\item \\textbf{Diagnostic framework.} Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions, providing practitioners with a priori prediction of symbolic aggregation viability from a $K{=}12$ pilot run (\\S\\ref{sec:diagnostic-framework}).",
          " ",
          "-\\item \\textbf{Process-level independence analysis.} CoT cosine similarity ($0.69$--$0.79$) exceeds answer-level $\\kappa$ ($0.45$--$0.74$) across four models from three families; under cross-model extraction on frontier models, SICA gain decreases monotonically with process similarity ($\\rho = -1.0$, $p = 0.008$; \\S\\ref{sec:process-kappa}).",
          "+\\item \\textbf{Cross-architecture escape.} Preliminary evidence that structurally independent NLI verification escapes the bottleneck ($+6.67$\\,pp on the weakest generator, $p < 0.001$), with gain decreasing monotonically as generator accuracy increases (\\S\\ref{sec:cross-arch}).",
          " \\end{enumerate}",
          " ",
          " \\begin{figure}[t]"
        ]
      }
    ],
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nTest-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \\citep{snell2025scaling, guo2025deepseekr1}.\nThe dominant aggregation strategy, Self-Consistency (SC) \\citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.\nSC is simple, model-agnostic, and effective---but it is hitting a ceiling.\n\\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.\nThe gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.\n\nConfidence-weighted \\citep{taubenfeld2025cisc} and universal \\citep{chen2024usc} extensions alleviate this, but the core limitation persists.\nRecent neuro-symbolic methods \\citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.\nA simpler question precedes these: can the \\emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?\nNo prior work has systematically evaluated this.\n\nWe ground our analysis in the Condorcet Jury Theorem (CJT) \\citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \\citep{austensmith1996}.\nWhen independence fails \\citep{ladha1992correlated}, additional samples carry diminishing information.\nMeasuring inter-trace agreement with Fleiss' $\\kappa$ \\citep{fleiss1971kappa}, we find $\\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\\text{eff}}$ as an ordinal diagnostic of vote diversity ($K_{\\text{eff}} \\approx 1.2$--$3.6$ for nominal $K = 12$; \\S\\ref{sec:condorcet}).\nChain-of-thought cosine similarity ($0.69$) far exceeds answer-level $\\kappa$ ($0.46$), revealing that traces share reasoning processes even when they diverge on final answers (\\S\\ref{sec:process-kappa}).\nWhen the same model extracts logical constraints from these correlated traces, the constraints exhibit \\emph{symbolic confirmation bias} (SCB): on problems where the model errs, 83.3\\% of self-extracted constraints support the wrong majority answer (bias ratios $1.66$--$4.97\\times$ across nine models), and 94\\% of errors overlap with SC (\\S\\ref{sec:confirmation-bias}).\nA shuffle control shows this bias is structural: it reflects the trace-count distribution rather than extraction-specific error.\nSelf-extraction cannot supply the independent signal that CJT requires.\n\nWe study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}).\nAcross six open-source models (7B--32B), three domains (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}, LogiQA \\citep{liu2020logiqa}), and over 3,000 condition-evaluations with four-seed replication, twenty-seven training-free remediation strategies spanning fifteen families all produce neutral or negative results (Table~\\ref{tab:main_results}).\nPrior work shows LLMs struggle with natural-language self-correction \\citep{huang2024selfcorrect} and that LLM-generated logical formulas can be unreliable \\citep{stechly2025selfverification}. Our formal channel is provably sound---the failure is precisely localizable to the extraction step. The assumption that formalizing reasoning provides \\emph{independent} verification evidence fails not because Z3 is unreliable (99\\% of constraints are syntactically valid), but because extraction inherits the model's biases: MAX-SAT produces answers identical to count-only aggregation on 94.4\\% of problems, rendering the formal layer vacuous.\n\nOracle controls confirm the mechanism is sound ($+29.90$\\,pp Mistral-7B, $+13.73$\\,pp Qwen-14B on FOLIO, $p < 0.001$; Appendix~\\ref{app:oracle}), yet self-extraction captures only ${\\sim}$12\\% of this ceiling.\nThe central finding is a persistent independence-accuracy trade-off \\citep{krogh1994neural}: Debate reduces $\\kappa$ to 0.15 but collapses accuracy ($-18.6$\\,pp); other methods cluster at $\\kappa \\approx 0.40$--$0.47$, a same-model ceiling across three families (\\S\\ref{sec:remediation}).\nA cross-architecture proof-of-concept escapes the bottleneck: zero-shot DeBERTa NLI yields $+6.67$\\,pp on Mistral-7B ProofWriter ($p < 0.001$) but no significant gain for stronger generators; domain-adapted NLI amplifies gains to $+$12--26\\,pp ($p < 0.0001$), extending to generators with SC up to 72\\% (\\S\\ref{sec:cross-arch}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Quantifying symbolic confirmation bias in formal self-verification.} While the general difficulty of LLM self-correction is known \\citep{huang2024selfcorrect}, we provide the first quantitative characterization of symbolic confirmation bias in formal self-verification, demonstrating that provably sound verification machinery becomes informationally vacuous under self-extraction: 83.3\\% of self-extracted constraints support the wrong answer (BR $1.66$--$4.97\\times$ across nine models), yet 99\\% pass Z3 validation. A shuffle control and MAX-SAT ablation show this bias is structural---the formal layer adds no information beyond majority voting. Twenty-seven training-free strategies fail to break it; cross-model extraction confirms universality across nine models from 7B to frontier (\\S\\ref{sec:confirmation-bias}).\n\n\\item \\textbf{General diagnostic framework for trace-aggregation methods.} Three diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly predict success or failure across all 60 tested conditions spanning self-extraction, training-free remediation, cross-architecture verification, and oracle controls. Decision boundaries---$C_0 < 5\\%$ (degenerate), $K_\\text{eff} \\leq 1.3$ (diversity-limited), $\\text{BR} > 2\\times$ (bias-dominated), $\\kappa_\\text{same} \\geq 0.40$ (same-model ceiling)---provide zero-cost prediction of symbolic aggregation viability. The framework extends to any method extracting structured representations from LLM traces (\\S\\ref{sec:remediation}, \\S\\ref{sec:cross-arch}).\n\n\\item \\textbf{Process-level independence analysis.} CoT cosine similarity ($0.69$--$0.79$) exceeds answer-level $\\kappa$ ($0.45$--$0.74$) across four models from three families; under cross-model extraction on frontier models, SICA gain decreases monotonically with process similarity ($\\rho = -1.0$, $p = 0.008$; \\S\\ref{sec:process-kappa}).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tikzpicture}[\n    node distance=0.3cm and 0.1cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,\n                text width=1.2cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract logical\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}\n\\label{fig:pipeline}\n\\end{figure}\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_018MhNT48RVrMZNnbXDpzVLd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "42940f4f-7806-4dd3-b2b2-d729ca6228bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfKgJGnZPUX5bmSdke8gLU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4602,
      "cache_read_input_tokens": 39352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4602
      },
      "output_tokens": 61,
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

_source line 18 · 2026-05-23T02:53:27.539Z_

<details><summary>↩ Tool result · `toolu_018MhNT48RVrMZNnbXDpzVLd`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Can a provably sound formal solver improve LLM reasoning if the constraints it operates on are self-extracted from the model's own traces? We show that the answer is no: Z3 validates 99\% of self-extracted constraints, yet MAX-SAT produces answers identical to majority voting on 94.4\% of problems. The formal verification layer is vacuous, not because the solver fails, but because extraction inherits the model's distributional bias. This finding challenges a natural extension of Self-Consistency (SC) \citep{wang2023sc}, which samples $K$ chain-of-thought traces and selects the majority answer. SC's gains plateau and decline for strong models \citep{loo2025reevaluating}; the gap between its theoretical promise (independent voters converge to truth \citep{condorcet1785, ladha1992correlated}) and practice points to correlated errors that majority voting cannot correct.
5	
6	\looseness=-1
7	We study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). Across six models (7B--32B), three reasoning domains, and over 3{,}000 condition-evaluations with multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). Four conditions are confirmed equivalent within $\pm$2\,pp; ten remain underpowered for effects below ${\sim}$2\,pp.
8	
9	\looseness=-1
10	The failure traces to \emph{symbolic confirmation bias}: on problems where the model errs, 83.3\% of self-extracted constraints support the incorrect majority answer (bias ratio $1.66$--$4.97\times$ across nine models from 7B to frontier; \S\ref{sec:confirmation-bias}). A shuffle control confirms this bias is structural, proportional to the trace-count distribution rather than extraction-specific error ($p > 0.7$). Prior work shows LLMs cannot self-correct without external feedback \citep{huang2024selfcorrect}; we demonstrate that this limitation extends to formal self-verification: even with a provably correct solver, self-extracted constraints carry no information beyond majority voting.
11	
12	\looseness=-1
13	Twenty-seven training-free remediation strategies produce neutral-to-negative results (\S\ref{sec:remediation}), revealing a fundamental independence-accuracy trade-off. Cross-architecture verification provides preliminary evidence of escaping the bottleneck: a structurally independent NLI verifier yields $+6.67$\,pp on the weakest generator ($p < 0.001$); domain-adapted verification extends gains to generators with SC up to 72\% with monotonically decreasing benefit (\S\ref{sec:cross-arch}). Three zero-cost diagnostics ($K_\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions (\S\ref{sec:diagnostic-framework}).
14	
15	Our contributions are:
16	\begin{enumerate}[nosep,leftmargin=*]
17	\item \textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction: symbolic confirmation bias (BR $1.66$--$4.97\times$ across nine models) renders MAX-SAT equivalent to majority voting on 94.4\% of problems. A shuffle control and 27 failed remediation strategies confirm the bias is structural (\S\ref{sec:confirmation-bias}, \S\ref{sec:remediation}).
18	
19	\item \textbf{Diagnostic framework.} Three zero-cost diagnostics ($K_\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions, providing practitioners with a priori prediction of symbolic aggregation viability from a $K{=}12$ pilot run (\S\ref{sec:diagnostic-framework}).
20	
21	\item \textbf{Cross-architecture escape.} Preliminary evidence that structurally independent NLI verification escapes the bottleneck ($+6.67$\,pp on the weakest generator, $p < 0.001$), with gain decreasing monotonically as generator accuracy increases (\S\ref{sec:cross-arch}).
22	\end{enumerate}
23	
24	\begin{figure}[t]
25	\centering
26	\small
27	\resizebox{\columnwidth}{!}{\begin{tikzpicture}[
28	    node distance=0.3cm and 0.1cm,
29	    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,
30	                text width=1.2cm, align=center, font=\scriptsize},
31	    arr/.style={-{Stealth[length=4pt]}, thick},
32	    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},
33	    lbl/.style={font=\scriptsize, text=gray!70!black},
34	    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,
35	                    inner sep=3pt},
36	]
37	\node[box] (q) {Question $q$};
38	\node[box, right=of q] (sample) {Sample $K$\\traces};
39	\node[box, right=of sample] (extract) {Extract logical\\constraints};
40	\node[box, right=of extract] (dedup) {Dedup.\ +\\weight};
41	\node[box, right=of dedup] (maxsat) {MAX-SAT\\(Z3)};
42	
43	\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};
44	\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\vote};
45	
46	\draw[arr] (q) -- (sample);
47	\draw[arr] (sample) -- (extract);
48	\draw[arr] (extract) -- (dedup);
49	\draw[arr] (dedup) -- (maxsat);
50	\draw[arr] (maxsat) -- (ans);
51	\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);
52	
53	\node[lbl, above=0.01cm of maxsat] {SICA};
54	
55	\node[ibottle, fit=(sample)(extract), label={[font=\scriptsize\itshape, text=red!70!black]above:Independence Bottleneck}] {};
56	
57	\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};
58	\end{tikzpicture}}
59	\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}
60	\label{fig:pipeline}
61	\end{figure}
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "a4a372a3-41a1-4b3b-81de-165b6b8037c3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\n\\looseness=-1\nCan a provably sound formal solver improve LLM reasoning if the constraints it operates on are self-extracted from the model's own traces? We show that the answer is no: Z3 validates 99\\% of self-extracted constraints, yet MAX-SAT produces answers identical to majority voting on 94.4\\% of problems. The formal verification layer is vacuous, not because the solver fails, but because extraction inherits the model's distributional bias. This finding challenges a natural extension of Self-Consistency (SC) \\citep{wang2023sc}, which samples $K$ chain-of-thought traces and selects the majority answer. SC's gains plateau and decline for strong models \\citep{loo2025reevaluating}; the gap between its theoretical promise (independent voters converge to truth \\citep{condorcet1785, ladha1992correlated}) and practice points to correlated errors that majority voting cannot correct.\n\n\\looseness=-1\nWe study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\\S\\ref{sec:pipeline}; Figure~\\ref{fig:pipeline}). Across six models (7B--32B), three reasoning domains, and over 3{,}000 condition-evaluations with multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\\ref{tab:main_results}). Four conditions are confirmed equivalent within $\\pm$2\\,pp; ten remain underpowered for effects below ${\\sim}$2\\,pp.\n\n\\looseness=-1\nThe failure traces to \\emph{symbolic confirmation bias}: on problems where the model errs, 83.3\\% of self-extracted constraints support the incorrect majority answer (bias ratio $1.66$--$4.97\\times$ across nine models from 7B to frontier; \\S\\ref{sec:confirmation-bias}). A shuffle control confirms this bias is structural, proportional to the trace-count distribution rather than extraction-specific error ($p > 0.7$). Prior work shows LLMs cannot self-correct without external feedback \\citep{huang2024selfcorrect}; we demonstrate that this limitation extends to formal self-verification: even with a provably correct solver, self-extracted constraints carry no information beyond majority voting.\n\n\\looseness=-1\nTwenty-seven training-free remediation strategies produce neutral-to-negative results (\\S\\ref{sec:remediation}), revealing a fundamental independence-accuracy trade-off. Cross-architecture verification provides preliminary evidence of escaping the bottleneck: a structurally independent NLI verifier yields $+6.67$\\,pp on the weakest generator ($p < 0.001$); domain-adapted verification extends gains to generators with SC up to 72\\% with monotonically decreasing benefit (\\S\\ref{sec:cross-arch}). Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions (\\S\\ref{sec:diagnostic-framework}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{The symbolic mirage.} Provably sound Z3 verification becomes vacuous under self-extraction: symbolic confirmation bias (BR $1.66$--$4.97\\times$ across nine models) renders MAX-SAT equivalent to majority voting on 94.4\\% of problems. A shuffle control and 27 failed remediation strategies confirm the bias is structural (\\S\\ref{sec:confirmation-bias}, \\S\\ref{sec:remediation}).\n\n\\item \\textbf{Diagnostic framework.} Three zero-cost diagnostics ($K_\\text{eff}$, BR, $C_0$) correctly classify all 60 tested conditions, providing practitioners with a priori prediction of symbolic aggregation viability from a $K{=}12$ pilot run (\\S\\ref{sec:diagnostic-framework}).\n\n\\item \\textbf{Cross-architecture escape.} Preliminary evidence that structurally independent NLI verification escapes the bottleneck ($+6.67$\\,pp on the weakest generator, $p < 0.001$), with gain decreasing monotonically as generator accuracy increases (\\S\\ref{sec:cross-arch}).\n\\end{enumerate}\n\n\\begin{figure}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\\begin{tikzpicture}[\n    node distance=0.3cm and 0.1cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,\n                text width=1.2cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\scriptsize, text=gray!70!black},\n    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,\n                    inner sep=3pt},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract logical\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\node[ibottle, fit=(sample)(extract), label={[font=\\scriptsize\\itshape, text=red!70!black]above:Independence Bottleneck}] {};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}}\n\\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}\n\\label{fig:pipeline}\n\\end{figure}\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

Written and verified. Changes from the original:

- **Opening**: Z3 paradox hook leads (replaces generic test-time scaling opener); SC/CJT context compressed to 2 sentences
- **Removed**: Long CJT paragraph (old lines 14-20), verbose oracle/independence-accuracy details, C3 "Process-level independence analysis"
- **Added**: Power caveat (line 7: "Four conditions confirmed equivalent; ten underpowered")
- **Softened**: Cross-architecture uses "preliminary evidence", "on the weakest generator" (line 13)
- **Contributions**: 3 items, each ~3 lines (down from 3 items at 5-8 lines each)
- **Figure 1**: TikZ block preserved exactly
- **Style**: No em-dashes, no AI clichés, `\looseness=-1` on all body paragraphs, BR range `1.66--4.97×`
- 77 lines → 61 lines; body text from ~4 dense paragraphs + verbose contributions to 4 tight paragraphs + concise contributions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "uuid": "75261721-cc6f-43d3-a528-259a54655762",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzbQcdFpEHYVXAw2d9c9MR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1953,
      "cache_read_input_tokens": 43954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1953
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

_source line 20_

Written and verified. Changes from the original:

- **Opening**: Z3 paradox hook leads (replaces generic test-time scaling opener); SC/CJT context compressed to 2 sentences
- **Removed**: Long CJT paragraph (old lines 14-20), verbose oracle/independence-accuracy details, C3 "Process-level independence analysis"
- **Added**: Power caveat (line 7: "Four conditions confirmed equivalent; ten underpowered")
- **Softened**: Cross-architecture uses "preliminary evidence", "on the weakest generator" (line 13)
- **Contributions**: 3 items, each ~3 lines (down from 3 items at 5-8 lines each)
- **Figure 1**: TikZ block preserved exactly
- **Style**: No em-dashes, no AI clichés, `\looseness=-1` on all body paragraphs, BR range `1.66--4.97×`
- 77 lines → 61 lines; body text from ~4 dense paragraphs + verbose contributions to 4 tight paragraphs + concise contributions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 107466,
  "duration_api_ms": 108585,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "c72ad09a-6565-4db8-a8b9-871ebd92dd96",
  "total_cost_usd": 0.4061795,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 34066,
    "cache_read_input_tokens": 120966,
    "output_tokens": 5201,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34066,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 260,
        "cache_read_input_tokens": 43954,
        "cache_creation_input_tokens": 1953,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1953
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2624,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002729,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 5201,
      "cacheReadInputTokens": 120966,
      "cacheCreationInputTokens": 34066,
      "webSearchRequests": 0,
      "costUSD": 0.40345050000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b2958bfe-0c22-4b51-a445-4404c4cf7d5e"
}
```

</details>

---
