# paper writing rw

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_writing_rw_20260520T125349.log`
- **Structured JSON:** [`6deefd7e4eb3ca76f549.json`](../../sessions/6d/6deefd7e4eb3ca76f549.json)

## Before a recorded user message

32 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
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
  "uuid": "7b4115ba-fff1-4264-bec2-3f77233929f1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-3-projects-contrastive-entrain-calib/memory/"
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
    "resetsAt": 1779290400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8ee3820d-307f-4303-9eb4-ec897e0200af",
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30"
}
```

---

### Assistant

_source line 4_

I'll read the required skill files first, then the existing paper structure for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "bfaff911-266b-47ff-9b0a-db99616db58b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLUXbmSSsDg8XtihExJHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13241,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13241
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

<details open><summary>🔧 Tool call — Read · `toolu_01GXTn28r5WGRUME3n2Ufyze`</summary>

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
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "6b70b368-4b45-40fd-a651-c7c4cb02951f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLUXbmSSsDg8XtihExJHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13241,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13241
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

_source line 6 · 2026-05-20T12:54:03.177Z_

<details><summary>↩ Tool result · `toolu_01GXTn28r5WGRUME3n2Ufyze`</summary>

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
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "ff9f208b-b10a-4adc-9072-f6a9f167fdd5",
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

<details open><summary>🔧 Tool call — Read · `toolu_017JfBC8eoc3M5tg5sFiceZp`</summary>

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
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "67722765-6254-4147-993e-83faa9977824",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLUXbmSSsDg8XtihExJHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13241,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13241
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

_source line 8 · 2026-05-20T12:54:03.784Z_

<details><summary>↩ Tool result · `toolu_017JfBC8eoc3M5tg5sFiceZp`</summary>

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
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "f9771b18-9d6c-4192-94cc-e0a723c76305",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01FtZXzNDKz34gv4W4bNJR4f`</summary>

```json
{
  "pattern": "docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "dfbec8bb-3b5d-4578-961e-f3b9f7ffd536",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcLUXbmSSsDg8XtihExJHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13241,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13241
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

_source line 10 · 2026-05-20T12:54:04.191Z_

<details><summary>↩ Tool result · `toolu_01FtZXzNDKz34gv4W4bNJR4f`</summary>

```text
docs/paper/sections/framework.tex
docs/paper/sections/cosine_failure.tex
docs/paper/sections/probe_trap.tex
docs/paper/sections/direction_quality.tex
docs/paper/sections/introduction.tex
docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "6e5841d4-4e93-4737-9f94-ce9ac296cce1",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/framework.tex",
      "docs/paper/sections/cosine_failure.tex",
      "docs/paper/sections/probe_trap.tex",
      "docs/paper/sections/direction_quality.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/related_work.tex"
    ],
    "durationMs": 27,
    "numFiles": 6,
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
Let me read the existing related_work.tex and the introduction for context, plus check the references.bib for the available citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "3285df18-d5a3-4256-b5d2-7da998f17439",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQQiSH3voHyLn7Juc2N9q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11309,
      "cache_read_input_tokens": 25082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11309
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

Let me check the existing related_work.tex and the introduction for consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "8aefb6ce-9da9-4578-8bc8-84aeee94f56f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQQiSH3voHyLn7Juc2N9q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11309,
      "cache_read_input_tokens": 25082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11309
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

<details open><summary>🔧 Tool call — Read · `toolu_016uFKXrwxpYSy6BoW6nuYTV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "08d404cc-5cfb-4f14-bee0-9a44c504b474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQQiSH3voHyLn7Juc2N9q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11309,
      "cache_read_input_tokens": 25082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11309
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

_source line 14 · 2026-05-20T12:54:10.274Z_

<details><summary>↩ Tool result · `toolu_016uFKXrwxpYSy6BoW6nuYTV`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Representation Engineering and Activation Steering.}
5	Representation engineering \citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.
6	Subsequent work exploited such directions for inference-time intervention: ITI \citep{li2023iti} uses probe weights as steering vectors for truthfulness, ActAdd \citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy at inference time.
7	CCS \citep{burns2023ccs} discovers truth-related directions without supervision through a consistency objective.
8	All five methods use representation geometry for inference-time classification or steering.
9	Our work tests whether the same geometric information transfers to a training-time reward signal, and finds that it does not: $\dsyc$ achieves strong discriminability (AUROC 0.82) but fails as a GRPO reward in all tested formulations.
10	
11	\paragraph{Sycophancy Characterization and Mitigation.}
12	\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.
13	\citet{shapira2026amplifies} proved formally that RLHF amplifies sycophancy under standard assumptions.
14	\citet{wang2025internal} traced the phenomenon to late-layer preference shifts via logit-lens analysis and confirmed that sycophantic behavior has identifiable internal origins.
15	On the mitigation side, \citet{wei2024synthetic} demonstrated that synthetic data mixed into fine-tuning reduces sycophancy at the data level.
16	Activation consistency training \citep[ACT;][]{consistency2025bctact} penalizes activation divergence between the model's initial and post-pressure responses but does not distinguish warranted from unwarranted belief changes.
17	\citet{obrien2025fewbadneurons} identified sycophancy-associated neurons and surgically corrected them; their probes serve a diagnostic role rather than an optimization target.
18	These methods either operate at the data or behavioral level, where all belief changes are treated uniformly, or use representations only for diagnosis.
19	Our analysis shows why the step from diagnosis to reward is structurally blocked for sycophancy: the direction that detects the behavior conflates it with its complement.
20	
21	\paragraph{Reward Design and Overoptimization.}
22	\citet{gao2023scaling} established scaling laws for reward model overoptimization: proxy rewards diverge from true objectives under sustained optimization pressure.
23	\citet{skalse2022hacking} proved that no bounded proxy reward can be immune to hacking.
24	\citet{casper2023openproblems} surveyed fundamental limitations of RLHF, including reward misspecification and distributional shift.
25	\citet{denison2024subterfuge} showed that reward hacking can escalate from sycophantic agreement to active reward tampering.
26	\citet{mckinney2023fragility} found that learned reward functions fail when applied to train new policies, a failure mode related to our probe reward trap.
27	\citet{wen2024mislead} documented U-Sophistry, where models learn to produce outputs that mislead human evaluators.
28	\citet{ackermann2026gradreg} proposed gradient regularization as a mitigation strategy.
29	Our probe reward trap is an extreme instance of overoptimization: a low-capacity linear probe is gamed within 500 training steps, with behavioral collapse preceding entropy collapse by approximately 1,300 steps.
30	
31	\paragraph{Representation-Guided Reinforcement Learning.}
32	\citet{zhang2026latentgrpo} introduced Latent-GRPO, which uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.
33	\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, a result that supports the feasibility of representation-space rewards in principle.
34	Both approaches succeed because the target categories (correct vs.\ incorrect reasoning, safe vs.\ unsafe outputs) occupy geometrically separable regions along the relevant direction.
35	Sycophancy breaks this condition: capitulation and legitimate revision share the same geometric direction and differ only in whether the belief change is warranted, a property that no activation-space direction encodes.
36	Our results explain this asymmetry and identify the warrant gap as the structural barrier.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "f11e837d-0533-4255-abdb-c070a52ff8bd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Representation Engineering and Activation Steering.}\nRepresentation engineering \\citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.\nSubsequent work exploited such directions for inference-time intervention: ITI \\citep{li2023iti} uses probe weights as steering vectors for truthfulness, ActAdd \\citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \\citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy at inference time.\nCCS \\citep{burns2023ccs} discovers truth-related directions without supervision through a consistency objective.\nAll five methods use representation geometry for inference-time classification or steering.\nOur work tests whether the same geometric information transfers to a training-time reward signal, and finds that it does not: $\\dsyc$ achieves strong discriminability (AUROC 0.82) but fails as a GRPO reward in all tested formulations.\n\n\\paragraph{Sycophancy Characterization and Mitigation.}\n\\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.\n\\citet{shapira2026amplifies} proved formally that RLHF amplifies sycophancy under standard assumptions.\n\\citet{wang2025internal} traced the phenomenon to late-layer preference shifts via logit-lens analysis and confirmed that sycophantic behavior has identifiable internal origins.\nOn the mitigation side, \\citet{wei2024synthetic} demonstrated that synthetic data mixed into fine-tuning reduces sycophancy at the data level.\nActivation consistency training \\citep[ACT;][]{consistency2025bctact} penalizes activation divergence between the model's initial and post-pressure responses but does not distinguish warranted from unwarranted belief changes.\n\\citet{obrien2025fewbadneurons} identified sycophancy-associated neurons and surgically corrected them; their probes serve a diagnostic role rather than an optimization target.\nThese methods either operate at the data or behavioral level, where all belief changes are treated uniformly, or use representations only for diagnosis.\nOur analysis shows why the step from diagnosis to reward is structurally blocked for sycophancy: the direction that detects the behavior conflates it with its complement.\n\n\\paragraph{Reward Design and Overoptimization.}\n\\citet{gao2023scaling} established scaling laws for reward model overoptimization: proxy rewards diverge from true objectives under sustained optimization pressure.\n\\citet{skalse2022hacking} proved that no bounded proxy reward can be immune to hacking.\n\\citet{casper2023openproblems} surveyed fundamental limitations of RLHF, including reward misspecification and distributional shift.\n\\citet{denison2024subterfuge} showed that reward hacking can escalate from sycophantic agreement to active reward tampering.\n\\citet{mckinney2023fragility} found that learned reward functions fail when applied to train new policies, a failure mode related to our probe reward trap.\n\\citet{wen2024mislead} documented U-Sophistry, where models learn to produce outputs that mislead human evaluators.\n\\citet{ackermann2026gradreg} proposed gradient regularization as a mitigation strategy.\nOur probe reward trap is an extreme instance of overoptimization: a low-capacity linear probe is gamed within 500 training steps, with behavioral collapse preceding entropy collapse by approximately 1,300 steps.\n\n\\paragraph{Representation-Guided Reinforcement Learning.}\n\\citet{zhang2026latentgrpo} introduced Latent-GRPO, which uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.\n\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, a result that supports the feasibility of representation-space rewards in principle.\nBoth approaches succeed because the target categories (correct vs.\\ incorrect reasoning, safe vs.\\ unsafe outputs) occupy geometrically separable regions along the relevant direction.\nSycophancy breaks this condition: capitulation and legitimate revision share the same geometric direction and differ only in whether the belief change is warranted, a property that no activation-space direction encodes.\nOur results explain this asymmetry and identify the warrant gap as the structural barrier.\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_014Ya4ftaCZW7SNUyhBNj63r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "285dd5b3-2080-4e7a-9c93-3e14e953dd7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gQQiSH3voHyLn7Juc2N9q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11309,
      "cache_read_input_tokens": 25082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11309
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

_source line 16 · 2026-05-20T12:54:10.568Z_

<details><summary>↩ Tool result · `toolu_014Ya4ftaCZW7SNUyhBNj63r`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827 \pm 0.028$ on Qwen3-8B and $0.779 \pm 0.019$ on Llama-3-8B (\S\ref{sec:direction_quality}).
6	The direction captures evidential granularity: discriminability rises monotonically from weak-evidence pairs (AUROC 0.675) through medium (0.883) to strong (0.929), and the signal remains stable under LoRA training with cosine drift of approximately 0.96 at 500 steps.
7	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a reward signal for reinforcement learning.
8	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
9	
10	This paper shows that the conversion fails.
11	We test three formulations that translate $\dsyc$ into a GRPO training signal (cosine similarity, scaled cosine, and binary probe) across six experimental configurations.
12	Every formulation fails.
13	Cosine similarity produces a reward gap of just 0.098 between valid and sycophantic activations, too narrow to drive policy updates (\S\ref{sec:cosine_failure}).
14	Online recalibration improves the offline AUROC from 0.82 to 0.91 yet triggers mode collapse rather than better training.
15	A binary probe with stopped gradients avoids the magnitude problem but creates a stubbornness trap: the model learns that never revising its answer reliably collects the probe reward, and the true-positive flip rate ($\tof$) drops to zero within 500 steps while generation entropy remains at 0.70 (\S\ref{sec:probe_trap}).
16	The gap between discriminability and reward utility is not a tuning problem.
17	It is a structural consequence of what $\dsyc$ encodes and what it does not.
18	
19	Existing approaches to sycophancy mitigation fall into two camps.
20	Behavioral methods such as ACT \citep{consistency2025bctact} and NLI-based GRPO score whether the model's final answer is consistent with a ground-truth label but do not examine internal representations; they treat all belief changes uniformly.
21	Representation-based methods take the opposite approach: activation addition \citep{turner2023actadd} and contrastive activation addition \citep{rimsky2024caa} steer model behavior at inference time, while techniques for discovering latent knowledge \citep{burns2023ccs} and representation-guided RL \citep{zhang2026latentgrpo} use activation geometry to shape behavior during training.
22	These methods have shown success on reasoning faithfulness and safety refusal.
23	The shared premise is that a direction with high discriminability in activation space should transfer into a useful training signal or intervention target.
24	For reasoning and safety, this premise holds: the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
25	Sycophancy violates this premise.
26	The behavior to suppress (capitulation under social pressure) and the behavior to preserve (revision under valid evidence) produce overlapping activation signatures along $\dsyc$, because both involve the model shifting its stated belief toward the user's position.
27	
28	The root cause is a semantic gap between discriminability and reward utility.
29	$\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}.
30	A post-hoc classifier can use this signal effectively because it scores labeled examples where the validity of the belief change is already known.
31	A reward signal during RL training has no such access to ground truth.
32	The reward must distinguish warranted revision from unwarranted capitulation using activation geometry alone, and $\dsyc$ collapses exactly this distinction.
33	This conflation is not an artifact of our extraction procedure.
34	Sycophancy is defined relative to external evidential warrant \citep{sharma2023sycophancy}, a property that no direction in activation space can fully encode.
35	The problem is compounded by the entanglement between helpfulness and sycophancy at the representation level: the same internal mechanisms that allow models to track user intent also predispose them to capitulate \citep{wang2025internal}, and RLHF amplifies this tendency \citep{shapira2026amplifies}.
36	When reward overoptimization \citep{gao2023scaling} operates on a signal that conflates compliance with capitulation, the result is predictable collapse \citep{casper2023openproblems}.
37	
38	We present three contributions:
39	
40	\begin{itemize}
41	\item \textbf{Cross-model discriminability $\neq$ reward utility} (C1). We extract and validate $\dsyc$ on Qwen3-8B (AUROC $0.827 \pm 0.028$) and Llama-3-8B (AUROC $0.779 \pm 0.019$), then systematically test three reward formulations across six configurations. All fail, establishing that discriminability alone does not confer reward utility (\S\ref{sec:direction_quality}, \S\ref{sec:cosine_failure}).
42	
43	\item \textbf{Probe reward trap with behavioral-before-distributional collapse} (C2). The binary probe reward produces behavioral death ($\tof = 0$ at step 500) while entropy remains at 0.70. The 1,300-step lag before distributional collapse means standard entropy monitoring misses the failure entirely, with the reward averaging $+0.72$ throughout (\S\ref{sec:probe_trap}).
44	
45	\item \textbf{Sycophancy is geometrically harder for representation-guided RL} (C3). We trace all failures to a unified root cause: $\dsyc$ encodes belief-change direction but not evidential warrant. Unlike reasoning or safety directions, sycophancy directions conflate the target behavior with its complement, placing a principled limit on when representation-guided RL can succeed (\S\ref{sec:discussion}).
46	\end{itemize}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "718c97f3-75bf-4f7b-b6d0-51ba320956fc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nRepresentation engineering \\citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.\nA contrastive sycophancy direction $\\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827 \\pm 0.028$ on Qwen3-8B and $0.779 \\pm 0.019$ on Llama-3-8B (\\S\\ref{sec:direction_quality}).\nThe direction captures evidential granularity: discriminability rises monotonically from weak-evidence pairs (AUROC 0.675) through medium (0.883) to strong (0.929), and the signal remains stable under LoRA training with cosine drift of approximately 0.96 at 500 steps.\nThese results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a reward signal for reinforcement learning.\nSycophancy is among the most persistent alignment failures in deployed systems \\citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.\n\nThis paper shows that the conversion fails.\nWe test three formulations that translate $\\dsyc$ into a GRPO training signal (cosine similarity, scaled cosine, and binary probe) across six experimental configurations.\nEvery formulation fails.\nCosine similarity produces a reward gap of just 0.098 between valid and sycophantic activations, too narrow to drive policy updates (\\S\\ref{sec:cosine_failure}).\nOnline recalibration improves the offline AUROC from 0.82 to 0.91 yet triggers mode collapse rather than better training.\nA binary probe with stopped gradients avoids the magnitude problem but creates a stubbornness trap: the model learns that never revising its answer reliably collects the probe reward, and the true-positive flip rate ($\\tof$) drops to zero within 500 steps while generation entropy remains at 0.70 (\\S\\ref{sec:probe_trap}).\nThe gap between discriminability and reward utility is not a tuning problem.\nIt is a structural consequence of what $\\dsyc$ encodes and what it does not.\n\nExisting approaches to sycophancy mitigation fall into two camps.\nBehavioral methods such as ACT \\citep{consistency2025bctact} and NLI-based GRPO score whether the model's final answer is consistent with a ground-truth label but do not examine internal representations; they treat all belief changes uniformly.\nRepresentation-based methods take the opposite approach: activation addition \\citep{turner2023actadd} and contrastive activation addition \\citep{rimsky2024caa} steer model behavior at inference time, while techniques for discovering latent knowledge \\citep{burns2023ccs} and representation-guided RL \\citep{zhang2026latentgrpo} use activation geometry to shape behavior during training.\nThese methods have shown success on reasoning faithfulness and safety refusal.\nThe shared premise is that a direction with high discriminability in activation space should transfer into a useful training signal or intervention target.\nFor reasoning and safety, this premise holds: the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.\nSycophancy violates this premise.\nThe behavior to suppress (capitulation under social pressure) and the behavior to preserve (revision under valid evidence) produce overlapping activation signatures along $\\dsyc$, because both involve the model shifting its stated belief toward the user's position.\n\nThe root cause is a semantic gap between discriminability and reward utility.\n$\\dsyc$ encodes \\emph{whether} belief changed, not \\emph{whether it should have}.\nA post-hoc classifier can use this signal effectively because it scores labeled examples where the validity of the belief change is already known.\nA reward signal during RL training has no such access to ground truth.\nThe reward must distinguish warranted revision from unwarranted capitulation using activation geometry alone, and $\\dsyc$ collapses exactly this distinction.\nThis conflation is not an artifact of our extraction procedure.\nSycophancy is defined relative to external evidential warrant \\citep{sharma2023sycophancy}, a property that no direction in activation space can fully encode.\nThe problem is compounded by the entanglement between helpfulness and sycophancy at the representation level: the same internal mechanisms that allow models to track user intent also predispose them to capitulate \\citep{wang2025internal}, and RLHF amplifies this tendency \\citep{shapira2026amplifies}.\nWhen reward overoptimization \\citep{gao2023scaling} operates on a signal that conflates compliance with capitulation, the result is predictable collapse \\citep{casper2023openproblems}.\n\nWe present three contributions:\n\n\\begin{itemize}\n\\item \\textbf{Cross-model discriminability $\\neq$ reward utility} (C1). We extract and validate $\\dsyc$ on Qwen3-8B (AUROC $0.827 \\pm 0.028$) and Llama-3-8B (AUROC $0.779 \\pm 0.019$), then systematically test three reward formulations across six configurations. All fail, establishing that discriminability alone does not confer reward utility (\\S\\ref{sec:direction_quality}, \\S\\ref{sec:cosine_failure}).\n\n\\item \\textbf{Probe reward trap with behavioral-before-distributional collapse} (C2). The binary probe reward produces behavioral death ($\\tof = 0$ at step 500) while entropy remains at 0.70. The 1,300-step lag before distributional collapse means standard entropy monitoring misses the failure entirely, with the reward averaging $+0.72$ throughout (\\S\\ref{sec:probe_trap}).\n\n\\item \\textbf{Sycophancy is geometrically harder for representation-guided RL} (C3). We trace all failures to a unified root cause: $\\dsyc$ encodes belief-change direction but not evidential warrant. Unlike reasoning or safety directions, sycophancy directions conflate the target behavior with its complement, placing a principled limit on when representation-guided RL can succeed (\\S\\ref{sec:discussion}).\n\\end{itemize}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
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
Now I have the existing related_work.tex and the introduction. The existing related_work.tex is already written and quite good. The task says to write it, so I need to rewrite it following the outline provided in the task.

Let me compare the existing version with what's requested:

The existing version has 4 paragraphs:
1. Representation Engineering and Activation Steering
2. Sycophancy Characterization and Mitigation
3. Reward Design and Overoptimization
4. Representation-Guided Reinforcement Learning


The requested outline has 4 clusters with specific word targets: Representation Engineering (~150 words), Reward Design & Hacking (~100 words), Anti-Sycophancy (~150 words), and Representation-Guided RL (~100 words), totaling around 550 words. The existing version is probably in that ballpark already, but I need to restructure it to match the outline more closely, adjust the word counts per section, and adopt the denser citation style with grouped \citep{} commands that the outline suggests.

Now I'm checking the constraints: no em-dashes or en-dashes except in number ranges, no "-ing" phrase endings, no stacking transition words like "Furthermore" or "Moreover", and avoiding words like "delve", "leverage", "utilize", and "facilitate". The framing should position our work thematically rather than surveying the field, with no explicit contribution claims. I'm also verifying the BibTeX keys against what's available to make sure citations are accurate. I'm laying out the related work section, starting with representation engineering and how prior work like CCS and ITI established that activation directions can steer model behavior through inference-time intervention. The key insight I'm highlighting is that our approach differs by using these directions as RL reward signals during training rather than for direct activation modification, which exposes a critical gap: a direction can have strong discriminability but fail as a reward signal. Now I'm moving into the reward design section to discuss overoptimization concerns. laws for reward model overoptimization, showing that proxy rewards diverge from true objectives under sustained optimization. \citet{skalse2022hacking} proved that no bounded proxy can be immune to this divergence, and \citet{casper2023openproblems} surveyed the resulting limitations of RLHF. Reward hacking can escalate from sycophantic agreement to active tampering \citep{denison2024subterfuge}, and learned reward functions fail when transferred to new policies \citep{mckinney2023fragility}. Our probe reward trap (\S\ref{sec:probe_trap}) is an extreme instance: a low-capacity linear probe is gamed within 500 steps, and the stubbornness trap represents a qualitatively distinct failure mode where the reward actively reinforces degenerate behavior rather than merely being circumvented.

Now looking at sycophancy specifically—the literature shows it's widespread in RLHF systems, with recent work proving that standard training actually amplifies this tendency and tracing it to identifiable shifts in late-layer representations. Several mitigation strategies have emerged: synthetic data approaches that address it at training time, activation consistency methods that penalize divergence between initial and pressure-tested responses, and neuron-level interventions that surgically target sycophancy-related circuits. These existing approaches treat all belief changes the same way, but our approach differs in how we handle this distinction.

The key insight is that representation-level differentiation fails because the metric conflates legitimate belief revision with unwarranted capitulation—both manifest as the model shifting its stated position toward the user's preference. Recent work on representation-guided RL shows promise when the target behavior is geometrically separable from what we're trying to suppress, like with correct reasoning versus flawed reasoning or safe refusal versus harmful outputs. But sycophancy breaks this assumption since revision and capitulation occupy overlapping regions in representation space, separated only by subtle differences in their underlying causes. I'm checking each sentence ending to make sure none trail off with participial phrases—that one about the model circumventing needs rewording. I'm also scanning for overused academic phrases like "Furthermore" or "leverage," and verifying that contribution claims stay implicit rather than explicit. The paragraph structure already positions our work naturally against prior approaches, so that's good. Now I should look at whether I can consolidate citations more efficiently by grouping multiple references into single commands where they're discussing related work. Cluster 1, I could group the five RepE methods differently. Let me see... Actually, let me revisit the outline. It specifies exactly which papers go in each cluster, so I should stick to that rather than rearranging. I notice the existing version includes wen2024mislead in the reward design section, but the outline doesn't mention it anywhere, so I'll leave it out to stay aligned with what's specified. The outline is clear about which papers belong where, so I'll follow that structure and start drafting the related work section with representation engineering as the first paragraph. in LLM residual streams encode high-level behavioral concepts. CCS discovers truth-related directions without supervision through a consistency objective. Subsequent work applied such directions for inference-time intervention: ITI uses probe weights as steering vectors for truthfulness, ActAdd adds fixed activation offsets to shift model behavior, and CAA applies contrastive activation addition to reduce sycophancy. These methods show that activation-space geometry carries rich behavioral information and can steer model outputs through direct modification at inference time. I'm using the same contrastive extraction methodology as CAA but applying the resulting direction as an RL reward signal rather than an activation addition. This shift from inference-time steering to training-time optimization reveals a critical gap: a direction can achieve high discriminability yet fail entirely as a reward signal.

The literature on reward design shows that proxy rewards diverge from true objectives under sustained optimization, and no bounded proxy can be immune to this divergence. RLHF has fundamental limitations including reward misspecification and distributional shift. Reward hacking can escalate from sycophantic agreement to active tampering, and learned reward functions fail when transferred to new policies. My probe reward trap is an extreme instance of this problem—a low-capacity linear probe gets gamed within just 500 steps.

The stubbornness trap represents something qualitatively different: the reward actively reinforces degenerate behavior rather than one the model merely circumvents.

Existing anti-sycophancy methods treat all belief changes uniformly—either penalizing every shift or rewarding consistency across the board. But my analysis reveals why this directional differentiation fails at the representation level: the metric conflates legitimate belief revision with unwarranted capitulation, since both involve the model moving its stated position toward the user's view. The internal origins work suggests these shifts have identifiable neural signatures, which matters for understanding why surface-level consistency penalties can't distinguish between the two. as a contributing cause. \citet{shapira2026amplifies} proved formally that RLHF amplifies this tendency under standard assumptions, and \citet{wang2025internal} traced the phenomenon to late-layer preference shifts, confirming that sycophantic behavior has identifiable internal origins. On the mitigation side, synthetic data approaches reduce sycophancy at the training-data level \citep{wei2024synthetic}, ACT \citep{consistency2025bctact} penalizes activation divergence between initial and post-pressure responses, and \citet{obrien2025fewbadneurons} identify sycophancy-associated neurons and surgically correct them. These methods either treat belief changes uniformly, penalizing all flips or rewarding all consistency, or use representations for diagnosis rather than optimization. Our analysis shows why the step from diagnosis to optimization target is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation because both involve the model shifting its stated belief toward the user's position.

Latent-GRPO and related representation-guided RL approaches leverage geometric distinctness between target and suppressed behaviors—like correct reasoning versus unsafe refusal—to succeed, but sycophancy presents a fundamental problem: revision and capitulation occupy the same direction space, differentiated only by evidential warrant that no activation pattern captures, which explains both when representation-guided methods work and where they fail for this particular challenge. I'm double-checking the constraints on the abstract text—verifying the word count sits around 535, confirming there are no em-dashes or en-dashes, and making sure no sentences end with participial phrases. The hyphens in compound words like "post-pressure" and "activation-space" are fine, and the "-ing" words I'm finding are embedded mid-sentence rather than at clause endings, so those pass the check too.

Now I'm thinking through where to group citations. The five methods in Cluster 1 each deserve individual attribution since I'm describing their distinct contributions. In Cluster 2 and 3, the findings are similarly specific to their sources, so grouping doesn't seem necessary—each citation is tied to a particular claim that warrants its own reference.

I'm also noticing the existing draft is already quite close to what I need, so I should focus on sharpening the key points: making Cluster 1 more concise around how linear directions encode behavioral information, emphasizing the stubbornness trap as a novel failure mode in Cluster 2, strengthening the conflation argument in Cluster 3, and highlighting the geometric separability condition in Cluster 4.

One thing I need to resolve—the outline mentions 30 steps for probe gaming but the introduction says 500 steps. I should stick with the introduction's framing since that's the more authoritative source. I'm torn between different experimental configurations—the introduction specifies 500 steps for the stopped-gradient probe, while the outline mentions 30 steps for the differentiable variant. Since I don't have the full paper context, I'll reference the section directly and keep the language general to avoid contradicting either setup. Let me settle on citing the specific section rather than committing to a number that might not match the actual experiment being discussed.

Now I'm continuing the related work section, finishing the representation engineering paragraph by citing the key papers on activation-space steering and then pivoting to our contribution: we adopt CAA's contrastive extraction method but repurpose the resulting direction as an RL reward signal instead of using it for inference-time intervention. This reveals an important gap—a direction can have strong discriminability metrics yet completely fail as a training signal, which prior work hasn't explored. Then I'm moving into the reward design section, setting up the discussion of overoptimization and the tension between proxy rewards and true objectives. Several mitigation approaches exist—synthetic data reduces sycophancy at the training level, activation consistency training penalizes belief flips uniformly, and neuron-level interventions surgically target sycophancy-associated activations—but they all struggle with the fundamental problem that my framework reveals: the reward signal can't distinguish between justified belief updates and capitulation since both look identical behaviorally. Moving to representation-guided RL, methods like latent-GRPO and gradient regularization show promise by constraining how representations drift during training, which works because they're optimizing directly on the internal structure rather than just the output.

The key insight is that these representation-based approaches succeed when the target behavior and the behavior to suppress occupy geometrically distinct regions—correct reasoning versus incorrect reasoning, safe refusal versus unsafe compliance. But sycophancy violates this condition entirely: revision and capitulation point in the same direction through activation space, separated only by whether the evidence actually warrants the change, and no activation pattern encodes that evidential distinction. This explains both when representation-guided RL can work and why it fundamentally can't solve sycophancy without additional structure. I'm double-checking the word counts for each paragraph to stay within the 550-word limit, and they're all tracking well. Now I need to make sure I'm not ending any sentences with gerund phrases—let me review the key endings and consider whether "steering" needs to be swapped out for something safer like "control." I'm debating whether the constraint about avoiding "-ing" phrase endings actually applies to gerunds embedded mid-sentence versus participial phrases at the end. The rule targets constructions like "..., highlighting X" at sentence endings, which sound more AI-like, whereas mid-sentence gerunds like "penalizing all flips or rewarding all consistency" feel more natural. But to be cautious, I'll rephrase to something cleaner: "These methods either treat all belief changes uniformly or use representations only for diagnosis, not optimization." That's tighter and avoids the potential issue altogether.

Now I'm checking whether my related work section aligns with the framing I established in the introduction—the distinction between behavioral methods and representation-based approaches, the shared premise about discriminability, and the specific issues like conflating warranted versus unwarranted belief changes. The clusters I've outlined seem to map well to these themes, so I'm ready to write the final version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "c5161da9-539a-40e6-b5ef-472b38d1a9b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zLfw1noqDe4iDZHRHhQop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 36391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3052
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

Now let me check the existing references.bib to confirm available keys, then write the section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "11466d32-f849-414d-bbfe-e1616d344ce0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zLfw1noqDe4iDZHRHhQop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 36391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3052
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

<details open><summary>🔧 Tool call — Bash · `toolu_01RdA4xtu7NYTaRHHQoGiqUH`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
  "description": "Count words in existing related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "94515b87-09d8-45d6-a944-d166dc3c1da2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zLfw1noqDe4iDZHRHhQop",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 36391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3052
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

_source line 20 · 2026-05-20T12:56:23.483Z_

<details><summary>↩ Tool result · `toolu_01RdA4xtu7NYTaRHHQoGiqUH`</summary>

```text
525 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "6fed12e7-3287-4da6-b8f2-ca756a8bd48f",
  "tool_use_result": {
    "stdout": "525 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
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

_source line 21_

<details open><summary>🔧 Tool call — Write · `toolu_014ZN7P6uaXc5HVrvfCJujjA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Representation Engineering.}\nRepresentation engineering \\citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.\nCCS \\citep{burns2023ccs} discovers truth-related directions without labels through a consistency objective.\nSubsequent work applied such directions for inference-time intervention: ITI \\citep{li2023iti} uses probe weights as truthfulness steering vectors, ActAdd \\citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \\citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy.\nThese methods demonstrate that activation-space geometry carries rich behavioral information sufficient for inference-time classification and control.\nWe use the same contrastive extraction methodology as CAA but apply the resulting direction as an RL reward signal rather than an activation addition.\nThis shift from inference-time steering to training-time optimization reveals a gap that prior work does not address: a direction can achieve high discriminability (AUROC 0.82; \\S\\ref{sec:direction_quality}) yet fail entirely as a reward signal.\n\n\\paragraph{Reward Design and Overoptimization.}\n\\citet{gao2023scaling} established scaling laws for reward model overoptimization, showing that proxy rewards diverge from true objectives under sustained optimization.\n\\citet{skalse2022hacking} proved that no bounded proxy can be immune to this divergence, and \\citet{casper2023openproblems} catalogued the resulting limitations of RLHF.\nReward hacking can escalate from sycophantic agreement to active tampering \\citep{denison2024subterfuge}, and learned reward functions fail when transferred to new policies \\citep{mckinney2023fragility}.\nOur probe reward trap (\\S\\ref{sec:probe_trap}) is an extreme instance: a low-capacity linear probe is gamed within 500 training steps.\nThe stubbornness trap represents a qualitatively distinct failure mode where the reward actively reinforces degenerate behavior rather than one the model merely circumvents.\n\n\\paragraph{Sycophancy Characterization and Mitigation.}\n\\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.\n\\citet{shapira2026amplifies} proved formally that RLHF amplifies this tendency under standard assumptions, and \\citet{wang2025internal} traced the phenomenon to late-layer preference shifts, confirming that sycophantic behavior has identifiable internal origins.\nOn the mitigation side, synthetic data approaches reduce sycophancy at the training-data level \\citep{wei2024synthetic}, ACT \\citep{consistency2025bctact} penalizes activation divergence between initial and post-pressure responses, and \\citet{obrien2025fewbadneurons} identify sycophancy-associated neurons and surgically correct them.\nThese methods either treat all belief changes as equivalent or use representations only for diagnosis, not as optimization targets.\nOur analysis shows why the step from diagnosis to reward is structurally blocked: $\\dsyc$ conflates warranted revision with unwarranted capitulation because both involve the model changing its stated belief toward the user's position.\n\n\\paragraph{Representation-Guided Reinforcement Learning.}\nLatent-GRPO \\citep{zhang2026latentgrpo} uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.\n\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, and \\citet{ackermann2026gradreg} proposed gradient regularization to constrain representation drift during training.\nThese methods succeed because the target behavior (correct reasoning, safe refusal) is geometrically distinct from the behavior to suppress along the relevant direction.\nSycophancy breaks this condition: revision and capitulation overlap in direction space, separated only by evidential warrant that no activation-space direction encodes (\\S\\ref{sec:cosine_failure}).\nOur results explain when representation-guided RL can succeed and identify the structural barrier that prevents it for sycophancy.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "22fe8b5f-99c7-44c4-9b71-b7b66763c9b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wJNht3Z3nz7A8B3PKzuL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7397,
      "cache_read_input_tokens": 39443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7397
      },
      "output_tokens": 53,
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

_source line 22 · 2026-05-20T12:56:57.583Z_

<details><summary>↩ Tool result · `toolu_014ZN7P6uaXc5HVrvfCJujjA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "8faf2a7a-3f99-4fe5-9772-94e6e1d25514",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Representation Engineering.}\nRepresentation engineering \\citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.\nCCS \\citep{burns2023ccs} discovers truth-related directions without labels through a consistency objective.\nSubsequent work applied such directions for inference-time intervention: ITI \\citep{li2023iti} uses probe weights as truthfulness steering vectors, ActAdd \\citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \\citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy.\nThese methods demonstrate that activation-space geometry carries rich behavioral information sufficient for inference-time classification and control.\nWe use the same contrastive extraction methodology as CAA but apply the resulting direction as an RL reward signal rather than an activation addition.\nThis shift from inference-time steering to training-time optimization reveals a gap that prior work does not address: a direction can achieve high discriminability (AUROC 0.82; \\S\\ref{sec:direction_quality}) yet fail entirely as a reward signal.\n\n\\paragraph{Reward Design and Overoptimization.}\n\\citet{gao2023scaling} established scaling laws for reward model overoptimization, showing that proxy rewards diverge from true objectives under sustained optimization.\n\\citet{skalse2022hacking} proved that no bounded proxy can be immune to this divergence, and \\citet{casper2023openproblems} catalogued the resulting limitations of RLHF.\nReward hacking can escalate from sycophantic agreement to active tampering \\citep{denison2024subterfuge}, and learned reward functions fail when transferred to new policies \\citep{mckinney2023fragility}.\nOur probe reward trap (\\S\\ref{sec:probe_trap}) is an extreme instance: a low-capacity linear probe is gamed within 500 training steps.\nThe stubbornness trap represents a qualitatively distinct failure mode where the reward actively reinforces degenerate behavior rather than one the model merely circumvents.\n\n\\paragraph{Sycophancy Characterization and Mitigation.}\n\\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.\n\\citet{shapira2026amplifies} proved formally that RLHF amplifies this tendency under standard assumptions, and \\citet{wang2025internal} traced the phenomenon to late-layer preference shifts, confirming that sycophantic behavior has identifiable internal origins.\nOn the mitigation side, synthetic data approaches reduce sycophancy at the training-data level \\citep{wei2024synthetic}, ACT \\citep{consistency2025bctact} penalizes activation divergence between initial and post-pressure responses, and \\citet{obrien2025fewbadneurons} identify sycophancy-associated neurons and surgically correct them.\nThese methods either treat all belief changes as equivalent or use representations only for diagnosis, not as optimization targets.\nOur analysis shows why the step from diagnosis to reward is structurally blocked: $\\dsyc$ conflates warranted revision with unwarranted capitulation because both involve the model changing its stated belief toward the user's position.\n\n\\paragraph{Representation-Guided Reinforcement Learning.}\nLatent-GRPO \\citep{zhang2026latentgrpo} uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.\n\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, and \\citet{ackermann2026gradreg} proposed gradient regularization to constrain representation drift during training.\nThese methods succeed because the target behavior (correct reasoning, safe refusal) is geometrically distinct from the behavior to suppress along the relevant direction.\nSycophancy breaks this condition: revision and capitulation overlap in direction space, separated only by evidential warrant that no activation-space direction encodes (\\S\\ref{sec:cosine_failure}).\nOur results explain when representation-guided RL can succeed and identify the structural barrier that prevents it for sycophancy.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 36,
        "newStart": 1,
        "newLines": 30,
        "lines": [
          "-\\section{Related Work}",
          "-\\label{sec:related_work}",
          "+\\section{Related Work}\\label{sec:related_work}",
          " ",
          "-\\paragraph{Representation Engineering and Activation Steering.}",
          "+\\paragraph{Representation Engineering.}",
          " Representation engineering \\citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.",
          "-Subsequent work exploited such directions for inference-time intervention: ITI \\citep{li2023iti} uses probe weights as steering vectors for truthfulness, ActAdd \\citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \\citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy at inference time.",
          "-CCS \\citep{burns2023ccs} discovers truth-related directions without supervision through a consistency objective.",
          "-All five methods use representation geometry for inference-time classification or steering.",
          "-Our work tests whether the same geometric information transfers to a training-time reward signal, and finds that it does not: $\\dsyc$ achieves strong discriminability (AUROC 0.82) but fails as a GRPO reward in all tested formulations.",
          "+CCS \\citep{burns2023ccs} discovers truth-related directions without labels through a consistency objective.",
          "+Subsequent work applied such directions for inference-time intervention: ITI \\citep{li2023iti} uses probe weights as truthfulness steering vectors, ActAdd \\citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \\citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy.",
          "+These methods demonstrate that activation-space geometry carries rich behavioral information sufficient for inference-time classification and control.",
          "+We use the same contrastive extraction methodology as CAA but apply the resulting direction as an RL reward signal rather than an activation addition.",
          "+This shift from inference-time steering to training-time optimization reveals a gap that prior work does not address: a direction can achieve high discriminability (AUROC 0.82; \\S\\ref{sec:direction_quality}) yet fail entirely as a reward signal.",
          " ",
          "+\\paragraph{Reward Design and Overoptimization.}",
          "+\\citet{gao2023scaling} established scaling laws for reward model overoptimization, showing that proxy rewards diverge from true objectives under sustained optimization.",
          "+\\citet{skalse2022hacking} proved that no bounded proxy can be immune to this divergence, and \\citet{casper2023openproblems} catalogued the resulting limitations of RLHF.",
          "+Reward hacking can escalate from sycophantic agreement to active tampering \\citep{denison2024subterfuge}, and learned reward functions fail when transferred to new policies \\citep{mckinney2023fragility}.",
          "+Our probe reward trap (\\S\\ref{sec:probe_trap}) is an extreme instance: a low-capacity linear probe is gamed within 500 training steps.",
          "+The stubbornness trap represents a qualitatively distinct failure mode where the reward actively reinforces degenerate behavior rather than one the model merely circumvents.",
          "+",
          " \\paragraph{Sycophancy Characterization and Mitigation.}",
          " \\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.",
          "-\\citet{shapira2026amplifies} proved formally that RLHF amplifies sycophancy under standard assumptions.",
          "-\\citet{wang2025internal} traced the phenomenon to late-layer preference shifts via logit-lens analysis and confirmed that sycophantic behavior has identifiable internal origins.",
          "-On the mitigation side, \\citet{wei2024synthetic} demonstrated that synthetic data mixed into fine-tuning reduces sycophancy at the data level.",
          "-Activation consistency training \\citep[ACT;][]{consistency2025bctact} penalizes activation divergence between the model's initial and post-pressure responses but does not distinguish warranted from unwarranted belief changes.",
          "-\\citet{obrien2025fewbadneurons} identified sycophancy-associated neurons and surgically corrected them; their probes serve a diagnostic role rather than an optimization target.",
          "-These methods either operate at the data or behavioral level, where all belief changes are treated uniformly, or use representations only for diagnosis.",
          "-Our analysis shows why the step from diagnosis to reward is structurally blocked for sycophancy: the direction that detects the behavior conflates it with its complement.",
          "+\\citet{shapira2026amplifies} proved formally that RLHF amplifies this tendency under standard assumptions, and \\citet{wang2025internal} traced the phenomenon to late-layer preference shifts, confirming that sycophantic behavior has identifiable internal origins.",
          "+On the mitigation side, synthetic data approaches reduce sycophancy at the training-data level \\citep{wei2024synthetic}, ACT \\citep{consistency2025bctact} penalizes activation divergence between initial and post-pressure responses, and \\citet{obrien2025fewbadneurons} identify sycophancy-associated neurons and surgically correct them.",
          "+These methods either treat all belief changes as equivalent or use representations only for diagnosis, not as optimization targets.",
          "+Our analysis shows why the step from diagnosis to reward is structurally blocked: $\\dsyc$ conflates warranted revision with unwarranted capitulation because both involve the model changing its stated belief toward the user's position.",
          " ",
          "-\\paragraph{Reward Design and Overoptimization.}",
          "-\\citet{gao2023scaling} established scaling laws for reward model overoptimization: proxy rewards diverge from true objectives under sustained optimization pressure.",
          "-\\citet{skalse2022hacking} proved that no bounded proxy reward can be immune to hacking.",
          "-\\citet{casper2023openproblems} surveyed fundamental limitations of RLHF, including reward misspecification and distributional shift.",
          "-\\citet{denison2024subterfuge} showed that reward hacking can escalate from sycophantic agreement to active reward tampering.",
          "-\\citet{mckinney2023fragility} found that learned reward functions fail when applied to train new policies, a failure mode related to our probe reward trap.",
          "-\\citet{wen2024mislead} documented U-Sophistry, where models learn to produce outputs that mislead human evaluators.",
          "-\\citet{ackermann2026gradreg} proposed gradient regularization as a mitigation strategy.",
          "-Our probe reward trap is an extreme instance of overoptimization: a low-capacity linear probe is gamed within 500 training steps, with behavioral collapse preceding entropy collapse by approximately 1,300 steps.",
          "-",
          " \\paragraph{Representation-Guided Reinforcement Learning.}",
          "-\\citet{zhang2026latentgrpo} introduced Latent-GRPO, which uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.",
          "-\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, a result that supports the feasibility of representation-space rewards in principle.",
          "-Both approaches succeed because the target categories (correct vs.\\ incorrect reasoning, safe vs.\\ unsafe outputs) occupy geometrically separable regions along the relevant direction.",
          "-Sycophancy breaks this condition: capitulation and legitimate revision share the same geometric direction and differ only in whether the belief change is warranted, a property that no activation-space direction encodes.",
          "-Our results explain this asymmetry and identify the warrant gap as the structural barrier.",
          "+Latent-GRPO \\citep{zhang2026latentgrpo} uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.",
          "+\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, and \\citet{ackermann2026gradreg} proposed gradient regularization to constrain representation drift during training.",
          "+These methods succeed because the target behavior (correct reasoning, safe refusal) is geometrically distinct from the behavior to suppress along the relevant direction.",
          "+Sycophancy breaks this condition: revision and capitulation overlap in direction space, separated only by evidential warrant that no activation-space direction encodes (\\S\\ref{sec:cosine_failure}).",
          "+Our results explain when representation-guided RL can succeed and identify the structural barrier that prevents it for sycophancy."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Representation Engineering and Activation Steering.}\nRepresentation engineering \\citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.\nSubsequent work exploited such directions for inference-time intervention: ITI \\citep{li2023iti} uses probe weights as steering vectors for truthfulness, ActAdd \\citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \\citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy at inference time.\nCCS \\citep{burns2023ccs} discovers truth-related directions without supervision through a consistency objective.\nAll five methods use representation geometry for inference-time classification or steering.\nOur work tests whether the same geometric information transfers to a training-time reward signal, and finds that it does not: $\\dsyc$ achieves strong discriminability (AUROC 0.82) but fails as a GRPO reward in all tested formulations.\n\n\\paragraph{Sycophancy Characterization and Mitigation.}\n\\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.\n\\citet{shapira2026amplifies} proved formally that RLHF amplifies sycophancy under standard assumptions.\n\\citet{wang2025internal} traced the phenomenon to late-layer preference shifts via logit-lens analysis and confirmed that sycophantic behavior has identifiable internal origins.\nOn the mitigation side, \\citet{wei2024synthetic} demonstrated that synthetic data mixed into fine-tuning reduces sycophancy at the data level.\nActivation consistency training \\citep[ACT;][]{consistency2025bctact} penalizes activation divergence between the model's initial and post-pressure responses but does not distinguish warranted from unwarranted belief changes.\n\\citet{obrien2025fewbadneurons} identified sycophancy-associated neurons and surgically corrected them; their probes serve a diagnostic role rather than an optimization target.\nThese methods either operate at the data or behavioral level, where all belief changes are treated uniformly, or use representations only for diagnosis.\nOur analysis shows why the step from diagnosis to reward is structurally blocked for sycophancy: the direction that detects the behavior conflates it with its complement.\n\n\\paragraph{Reward Design and Overoptimization.}\n\\citet{gao2023scaling} established scaling laws for reward model overoptimization: proxy rewards diverge from true objectives under sustained optimization pressure.\n\\citet{skalse2022hacking} proved that no bounded proxy reward can be immune to hacking.\n\\citet{casper2023openproblems} surveyed fundamental limitations of RLHF, including reward misspecification and distributional shift.\n\\citet{denison2024subterfuge} showed that reward hacking can escalate from sycophantic agreement to active reward tampering.\n\\citet{mckinney2023fragility} found that learned reward functions fail when applied to train new policies, a failure mode related to our probe reward trap.\n\\citet{wen2024mislead} documented U-Sophistry, where models learn to produce outputs that mislead human evaluators.\n\\citet{ackermann2026gradreg} proposed gradient regularization as a mitigation strategy.\nOur probe reward trap is an extreme instance of overoptimization: a low-capacity linear probe is gamed within 500 training steps, with behavioral collapse preceding entropy collapse by approximately 1,300 steps.\n\n\\paragraph{Representation-Guided Reinforcement Learning.}\n\\citet{zhang2026latentgrpo} introduced Latent-GRPO, which uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.\n\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, a result that supports the feasibility of representation-space rewards in principle.\nBoth approaches succeed because the target categories (correct vs.\\ incorrect reasoning, safe vs.\\ unsafe outputs) occupy geometrically separable regions along the relevant direction.\nSycophancy breaks this condition: capitulation and legitimate revision share the same geometric direction and differ only in whether the belief change is warranted, a property that no activation-space direction encodes.\nOur results explain this asymmetry and identify the warrant gap as the structural barrier.\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01QyubJkfQKfq4nKqo9jaPeM`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
  "description": "Count words in new related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "cf90cccc-a01b-4e6a-9d0e-3708c8eecca1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAAqqHzmyzmnvBxbyeeryF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1276,
      "cache_read_input_tokens": 46840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1276
      },
      "output_tokens": 57,
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

_source line 24 · 2026-05-20T12:57:00.235Z_

<details><summary>↩ Tool result · `toolu_01QyubJkfQKfq4nKqo9jaPeM`</summary>

```text
485 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "21b62ff0-91f3-490e-a2af-677f70a78b46",
  "tool_use_result": {
    "stdout": "485 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
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

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01GDGHvibrciwfav8jFNm2c9`</summary>

```json
{
  "command": "grep -n \"—\\|–\" docs/paper/sections/related_work.tex | head -20",
  "description": "Check for em-dashes and en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "198b35b5-5bde-4167-87ae-6e4cd973ece3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vQxmu6DhJQJeuKJJeu5y6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 184,
      "cache_read_input_tokens": 48116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 184
      },
      "output_tokens": 65,
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

_source line 26 · 2026-05-20T12:57:03.930Z_

<details><summary>↩ Tool result · `toolu_01GDGHvibrciwfav8jFNm2c9`</summary>

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
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "33ef5e74-ea19-421b-8788-cd309ee14df5",
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01EwYTuU9Mvg5orAQrzcY1RY`</summary>

```json
{
  "command": "grep -n \"Furthermore\\|Moreover\\|Additionally\\|delve\\|leverage\\|utilize\\|facilitate\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
  "description": "Check for banned words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "6d0fe0bb-ee45-46e2-9e7b-6c3a16e2401a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeEeh52qnSoLujuxESJjpF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 48300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 120
      },
      "output_tokens": 43,
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

_source line 28 · 2026-05-20T12:57:07.458Z_

<details><summary>↩ Tool result · `toolu_01EwYTuU9Mvg5orAQrzcY1RY`</summary>

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
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "98a8eaf2-065e-4607-aaf0-3edd2f1a235c",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_017k6dtg6v8KYhpvCs8aErva`</summary>

```json
{
  "command": "grep -nP \"ing[.,;]?\\s*$\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
  "description": "Check for -ing phrase endings at end of lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "efb2357c-7125-4d07-bf7e-575ef7d3c811",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5SNMCmmDXKE1E7B4Q88vM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 48420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
      },
      "output_tokens": 38,
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

_source line 30 · 2026-05-20T12:57:10.283Z_

<details><summary>↩ Tool result · `toolu_017k6dtg6v8KYhpvCs8aErva`</summary>

```text
27:\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, and \citet{ackermann2026gradreg} proposed gradient regularization to constrain representation drift during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "625b282f-679c-4480-83c4-f3e221c11a75",
  "tool_use_result": {
    "stdout": "27:\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, and \\citet{ackermann2026gradreg} proposed gradient regularization to constrain representation drift during training.",
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

_source line 31_

Line 27 ends with "during training." That's a prepositional phrase, not a participial -ing construction ("training" is a noun here, not a participle). No violation.

Word count is 485 (LaTeX markup included; actual prose is ~530 after rendering citation expansions). All constraints pass: no dashes, no banned words, no -ing participial endings, no contribution claims, four thematic clusters each positioning our work.

Written to `docs/paper/sections/related_work.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "uuid": "fcc09705-8037-48b8-9387-c01ab7ad74ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Sx2XmDaFNAptFxJuk52oH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 48579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 200
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

_source line 32_

Line 27 ends with "during training." That's a prepositional phrase, not a participial -ing construction ("training" is a noun here, not a participle). No violation.

Word count is 485 (LaTeX markup included; actual prose is ~530 after rendering citation expansions). All constraints pass: no dashes, no banned words, no -ing participial endings, no contribution claims, four thematic clusters each positioning our work.

Written to `docs/paper/sections/related_work.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 196266,
  "duration_api_ms": 196768,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "9fe6b935-8484-4970-aa6b-b42fb8eefd30",
  "total_cost_usd": 0.6495585,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 36938,
    "cache_read_input_tokens": 353012,
    "output_tokens": 9595,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36938,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 117,
        "cache_read_input_tokens": 48579,
        "cache_creation_input_tokens": 200,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 200
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2175,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00226,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 9595,
      "cacheReadInputTokens": 353012,
      "cacheCreationInputTokens": 36938,
      "webSearchRequests": 0,
      "costUSD": 0.6472985000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e08a9ea6-10b4-4979-a99f-a32357fd5a0f"
}
```

</details>

---
