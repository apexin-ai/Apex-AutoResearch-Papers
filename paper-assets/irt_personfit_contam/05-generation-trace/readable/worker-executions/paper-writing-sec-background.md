# paper writing sec background

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_writing_sec_background_20260520T225844.log`
- **Structured JSON:** [`52c94cb4f7aa859f1493.json`](../../sessions/52/52c94cb4f7aa859f1493.json)

## Before a recorded user message

44 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
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
  "uuid": "bd192559-6fed-43d7-9458-0012388955ed",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-3-projects-irt-personfit-contam/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

I'll start by reading the required skill files and project context in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "00d0bc04-7978-4b70-8dcd-f3b1d5f2a72a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8vKSkoRCanykV3cTW5wPc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13147
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

### Runtime record

_source line 4_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779319200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6a45d76c-eafb-4557-a1bd-cb664965a889",
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9"
}
```

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_017tq2Pv8EAEm8Ly6365mtq9`</summary>

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
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "98547818-bd89-4ded-851f-0c471a77fcb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8vKSkoRCanykV3cTW5wPc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13147
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

_source line 6 · 2026-05-20T22:58:56.144Z_

<details><summary>↩ Tool result · `toolu_017tq2Pv8EAEm8Ly6365mtq9`</summary>

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
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "99d8a5ec-3197-4d5f-ac48-47efbdcfa8eb",
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

<details open><summary>🔧 Tool call — Read · `toolu_014C9yz25XhtJDy5CZFsiHeY`</summary>

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
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "004b551b-0f6f-4180-a5ea-0a6e439c70a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8vKSkoRCanykV3cTW5wPc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13147
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

_source line 8 · 2026-05-20T22:58:56.611Z_

<details><summary>↩ Tool result · `toolu_014C9yz25XhtJDy5CZFsiHeY`</summary>

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
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "421680f8-b769-45ee-bbae-f614b085bebe",
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

<details open><summary>🔧 Tool call — Read · `toolu_01SJAaXdZbS7eaNr9CyTUHL6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "0f286dea-e4ae-49d4-9173-516dd7a88f85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8vKSkoRCanykV3cTW5wPc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13147
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

_source line 10 · 2026-05-20T22:58:57.190Z_

<details><summary>↩ Tool result · `toolu_01SJAaXdZbS7eaNr9CyTUHL6`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{The \textsc{IRT-Fit} Framework}
5	\label{sec:framework}
6	
7	Our method takes as input a binary response matrix $\mathbf{X} \in \{0,1\}^{M \times n}$, where $M$ models answer $n$ benchmark items, together with pre-calibrated four-parameter logistic (4PL) item parameters from PSN-IRT \citep{psnirt2026}.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is a lower asymptote (guessing), and $d_i$ is an upper asymptote (slip).
14	
15	The framework proceeds in three steps.
16	\textbf{Step~1}: Estimate each model's ability $\hat{\theta}$ via maximum likelihood on each benchmark separately.
17	\textbf{Step~2}: Compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized likelihood residual that quantifies how well a model's item-level response pattern conforms to the IRT model given $\hat{\theta}$.
18	The statistic extends the original $\ell_z$ \citep{drasgow1985} by correcting for estimation uncertainty in $\hat{\theta}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis.
19	\textbf{Step~3}: For within-model contamination detection, compute $\Delta\ell_z^* = \ell_z^*(\text{target}) - \ell_z^*(\text{reference})$ between a target benchmark and a reference benchmark from the same model.
20	The entire procedure is unsupervised: it requires no training data, no labeled contamination examples, and no access to pretraining corpora.
21	
22	\paragraph{Validity under assumption violations.}
23	IRT assumes local independence and unidimensionality, conditions that LLM benchmarks violate.
24	When these assumptions fail, $\ell_z^*$ can exhibit systematic bias: all models may appear aberrant even without contamination, because inter-item dependencies inflate the variance of response patterns beyond what the IRT model predicts.
25	However, this bias is approximately constant across benchmarks for a given model, because the same latent capabilities and the same dependency structure drive responses.
26	The $\Delta\ell_z^*$ statistic functions as a difference-in-differences (DiD) estimator: the shared bias cancels in the subtraction, isolating the contamination-specific signal.
27	We calibrate significance thresholds via a nonparametric bootstrap over the null distribution of $\Delta\ell_z^*$ rather than relying on the asymptotic $\mathcal{N}(0,1)$ reference, which accommodates residual model misspecification.
28	Universal misfit (all models showing $|\ell_z^*| > 1.96$) is therefore a finding about benchmark properties, not an artifact; $\Delta\ell_z^*$ bypasses absolute thresholds entirely.
29	
30	\subsection{Detection Power Characterization}
31	\label{sec:power_theory}
32	
33	We derive the statistical power of $\ell_z^*$ as a function of benchmark size $n$ and contamination fraction $\pi$.
34	
35	\paragraph{Contamination model.}
36	A fraction $\pi$ of items are forced correct regardless of ability.
37	The expected response becomes:
38	\begin{equation}
39	  \mathbb{E}[x_i \mid \theta_0, \pi] = P_i(\theta_0) + \pi \cdot Q_i(\theta_0)
40	  \label{eq:contam_response}
41	\end{equation}
42	where $Q_i(\theta) = 1 - P_i(\theta)$.
43	The contaminated response inflates the MLE: $\mathbb{E}[\hat{\theta}] > \theta_0$ for $\pi > 0$, because the score equation $\sum_i (\mathbb{E}[x_i] - P_i(\theta))\,h_i(\theta) = 0$ shifts the solution upward.
44	
45	\paragraph{Proposition 1 ($\sqrt{n}$ scaling).}
46	The noncentrality parameter $\delta(\theta_0, \pi)$ of $\ell_z^*$ under contamination satisfies $\delta \propto \sqrt{n}$.
47	The numerator accumulates $n$ per-item residuals ($O(n)$) while the denominator grows as $\sqrt{\mathrm{Var}^*} = O(\sqrt{n})$ from the \citet{snijders2001} variance formula, so
48	\begin{equation}
49	  \delta(\theta_0, \pi) = \sqrt{n}\;\cdot\;\delta_1(\theta_0, \pi)
50	  \label{eq:sqrt_n}
51	\end{equation}
52	where $\delta_1$ is the per-item noncentrality that depends only on item parameters and $(\theta_0, \pi)$.
53	
54	\paragraph{Proposition 2 (marginal power).}
55	Integrating over $\theta_0 \sim \mathcal{N}(0,1)$ via Gauss--Hermite quadrature ($K{=}30$ nodes) yields the marginal power under two-sided testing at level $\alpha$:
56	\begin{equation}
57	  \mathrm{Power}(n, \pi) = \sum_{k=1}^{K} w_k \left[\Phi\!\left(\frac{-z_\alpha - \delta_k}{\sigma_k}\right) + 1 - \Phi\!\left(\frac{z_\alpha - \delta_k}{\sigma_k}\right)\right]
58	  \label{eq:power}
59	\end{equation}
60	where $\delta_k$ and $\sigma_k$ are the conditional mean shift and standard deviation of $\ell_z^*$ at the $k$-th quadrature node, $w_k$ are the quadrature weights, and $z_\alpha = 1.96$.
61	Two-sided testing is essential: at moderate contamination ($\pi < 80\%$), $\ell_z^*$ is negative (aberrant pattern), but at high contamination ($\pi > 85\%$), $\ell_z^*$ turns positive (over-consistent pattern) as the inflated $\hat{\theta}$ renders near-perfect accuracy expected.
62	The crossover occurs at $\pi^* \approx 81$--$85\%$ across benchmarks.
63	Practitioners can determine minimum benchmark sizes from Equation~\ref{eq:power}: for example, 80\% power at 15\% contamination requires $n \geq 7{,}958$ items.
64	
65	\subsection{$\theta$-Shift Analysis}
66	\label{sec:theta_shift}
67	
68	Contamination creates an identification problem: higher accuracy raises $\hat{\theta}_{\text{MLE}}$, which in turn ``explains away'' the aberrant responses and attenuates the $\ell_z^*$ signal.
69	We term this the \emph{$\theta$-shift mechanism}.
70	As $\pi$ increases, $\hat{\theta}$ absorbs a larger share of the contamination signal into a legitimate ability increase, so the free-$\theta$ dose-response curve becomes non-monotonic: $|\Delta\ell_z^*|$ can decrease at higher contamination levels.
71	
72	The solution is \emph{$\theta$-fixed analysis}: anchor ability at a pre-contamination baseline $\theta_{\text{fixed}}$ estimated from clean conditions or cross-validated from held-out benchmarks.
73	With $\theta$ fixed, the $\ell_z^*$ statistic captures the full residual between observed and expected performance, and the dose-response curve becomes monotonically increasing.
74	In our controlled experiments (\S\ref{sec:ctrl_contam}), fixed-$\theta$ estimation yields a monotonic signal ratio of 3.12 between 50\% and 15\% contamination, whereas free-$\theta$ estimation produces an inverted ratio of 0.44.
75	
76	For practical deployment, $\theta_{\text{fixed}}$ can be obtained through two strategies: (1) cross-benchmark estimation, where $\theta$ is estimated from benchmarks presumed clean and applied to the target benchmark; or (2) temporal anchoring, where $\theta$ from an earlier evaluation serves as the reference for subsequent evaluations of the same model.
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "5c91d3ad-de0a-4f1c-9b9c-38e70a6cd7a6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{The \\textsc{IRT-Fit} Framework}\n\\label{sec:framework}\n\nOur method takes as input a binary response matrix $\\mathbf{X} \\in \\{0,1\\}^{M \\times n}$, where $M$ models answer $n$ benchmark items, together with pre-calibrated four-parameter logistic (4PL) item parameters from PSN-IRT \\citep{psnirt2026}.\nThe 4PL model defines the probability that a model with ability $\\theta$ answers item $i$ correctly:\n\\begin{equation}\n  P_i(\\theta) = c_i + (d_i - c_i)\\,\\frac{1}{1 + e^{-a_i(\\theta - b_i)}}\n  \\label{eq:4pl}\n\\end{equation}\nwhere $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is a lower asymptote (guessing), and $d_i$ is an upper asymptote (slip).\n\nThe framework proceeds in three steps.\n\\textbf{Step~1}: Estimate each model's ability $\\hat{\\theta}$ via maximum likelihood on each benchmark separately.\n\\textbf{Step~2}: Compute the person-fit statistic $\\ell_z^*$ \\citep{snijders2001}, a standardized likelihood residual that quantifies how well a model's item-level response pattern conforms to the IRT model given $\\hat{\\theta}$.\nThe statistic extends the original $\\ell_z$ \\citep{drasgow1985} by correcting for estimation uncertainty in $\\hat{\\theta}$, so that $\\ell_z^* \\sim \\mathcal{N}(0,1)$ under the null hypothesis.\n\\textbf{Step~3}: For within-model contamination detection, compute $\\Delta\\ell_z^* = \\ell_z^*(\\text{target}) - \\ell_z^*(\\text{reference})$ between a target benchmark and a reference benchmark from the same model.\nThe entire procedure is unsupervised: it requires no training data, no labeled contamination examples, and no access to pretraining corpora.\n\n\\paragraph{Validity under assumption violations.}\nIRT assumes local independence and unidimensionality, conditions that LLM benchmarks violate.\nWhen these assumptions fail, $\\ell_z^*$ can exhibit systematic bias: all models may appear aberrant even without contamination, because inter-item dependencies inflate the variance of response patterns beyond what the IRT model predicts.\nHowever, this bias is approximately constant across benchmarks for a given model, because the same latent capabilities and the same dependency structure drive responses.\nThe $\\Delta\\ell_z^*$ statistic functions as a difference-in-differences (DiD) estimator: the shared bias cancels in the subtraction, isolating the contamination-specific signal.\nWe calibrate significance thresholds via a nonparametric bootstrap over the null distribution of $\\Delta\\ell_z^*$ rather than relying on the asymptotic $\\mathcal{N}(0,1)$ reference, which accommodates residual model misspecification.\nUniversal misfit (all models showing $|\\ell_z^*| > 1.96$) is therefore a finding about benchmark properties, not an artifact; $\\Delta\\ell_z^*$ bypasses absolute thresholds entirely.\n\n\\subsection{Detection Power Characterization}\n\\label{sec:power_theory}\n\nWe derive the statistical power of $\\ell_z^*$ as a function of benchmark size $n$ and contamination fraction $\\pi$.\n\n\\paragraph{Contamination model.}\nA fraction $\\pi$ of items are forced correct regardless of ability.\nThe expected response becomes:\n\\begin{equation}\n  \\mathbb{E}[x_i \\mid \\theta_0, \\pi] = P_i(\\theta_0) + \\pi \\cdot Q_i(\\theta_0)\n  \\label{eq:contam_response}\n\\end{equation}\nwhere $Q_i(\\theta) = 1 - P_i(\\theta)$.\nThe contaminated response inflates the MLE: $\\mathbb{E}[\\hat{\\theta}] > \\theta_0$ for $\\pi > 0$, because the score equation $\\sum_i (\\mathbb{E}[x_i] - P_i(\\theta))\\,h_i(\\theta) = 0$ shifts the solution upward.\n\n\\paragraph{Proposition 1 ($\\sqrt{n}$ scaling).}\nThe noncentrality parameter $\\delta(\\theta_0, \\pi)$ of $\\ell_z^*$ under contamination satisfies $\\delta \\propto \\sqrt{n}$.\nThe numerator accumulates $n$ per-item residuals ($O(n)$) while the denominator grows as $\\sqrt{\\mathrm{Var}^*} = O(\\sqrt{n})$ from the \\citet{snijders2001} variance formula, so\n\\begin{equation}\n  \\delta(\\theta_0, \\pi) = \\sqrt{n}\\;\\cdot\\;\\delta_1(\\theta_0, \\pi)\n  \\label{eq:sqrt_n}\n\\end{equation}\nwhere $\\delta_1$ is the per-item noncentrality that depends only on item parameters and $(\\theta_0, \\pi)$.\n\n\\paragraph{Proposition 2 (marginal power).}\nIntegrating over $\\theta_0 \\sim \\mathcal{N}(0,1)$ via Gauss--Hermite quadrature ($K{=}30$ nodes) yields the marginal power under two-sided testing at level $\\alpha$:\n\\begin{equation}\n  \\mathrm{Power}(n, \\pi) = \\sum_{k=1}^{K} w_k \\left[\\Phi\\!\\left(\\frac{-z_\\alpha - \\delta_k}{\\sigma_k}\\right) + 1 - \\Phi\\!\\left(\\frac{z_\\alpha - \\delta_k}{\\sigma_k}\\right)\\right]\n  \\label{eq:power}\n\\end{equation}\nwhere $\\delta_k$ and $\\sigma_k$ are the conditional mean shift and standard deviation of $\\ell_z^*$ at the $k$-th quadrature node, $w_k$ are the quadrature weights, and $z_\\alpha = 1.96$.\nTwo-sided testing is essential: at moderate contamination ($\\pi < 80\\%$), $\\ell_z^*$ is negative (aberrant pattern), but at high contamination ($\\pi > 85\\%$), $\\ell_z^*$ turns positive (over-consistent pattern) as the inflated $\\hat{\\theta}$ renders near-perfect accuracy expected.\nThe crossover occurs at $\\pi^* \\approx 81$--$85\\%$ across benchmarks.\nPractitioners can determine minimum benchmark sizes from Equation~\\ref{eq:power}: for example, 80\\% power at 15\\% contamination requires $n \\geq 7{,}958$ items.\n\n\\subsection{$\\theta$-Shift Analysis}\n\\label{sec:theta_shift}\n\nContamination creates an identification problem: higher accuracy raises $\\hat{\\theta}_{\\text{MLE}}$, which in turn ``explains away'' the aberrant responses and attenuates the $\\ell_z^*$ signal.\nWe term this the \\emph{$\\theta$-shift mechanism}.\nAs $\\pi$ increases, $\\hat{\\theta}$ absorbs a larger share of the contamination signal into a legitimate ability increase, so the free-$\\theta$ dose-response curve becomes non-monotonic: $|\\Delta\\ell_z^*|$ can decrease at higher contamination levels.\n\nThe solution is \\emph{$\\theta$-fixed analysis}: anchor ability at a pre-contamination baseline $\\theta_{\\text{fixed}}$ estimated from clean conditions or cross-validated from held-out benchmarks.\nWith $\\theta$ fixed, the $\\ell_z^*$ statistic captures the full residual between observed and expected performance, and the dose-response curve becomes monotonically increasing.\nIn our controlled experiments (\\S\\ref{sec:ctrl_contam}), fixed-$\\theta$ estimation yields a monotonic signal ratio of 3.12 between 50\\% and 15\\% contamination, whereas free-$\\theta$ estimation produces an inverted ratio of 0.44.\n\nFor practical deployment, $\\theta_{\\text{fixed}}$ can be obtained through two strategies: (1) cross-benchmark estimation, where $\\theta$ is estimated from benchmarks presumed clean and applied to the target benchmark; or (2) temporal anchoring, where $\\theta$ from an earlier evaluation serves as the reference for subsequent evaluations of the same model.\n",
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

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01R2YDCHX2MhNXj9K25DeKyD`</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "6b1ccf95-83f7-4aaa-a346-901a14af0803",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8vKSkoRCanykV3cTW5wPc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13147,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13147
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

_source line 12 · 2026-05-20T22:58:57.737Z_

<details><summary>↩ Tool result · `toolu_01R2YDCHX2MhNXj9K25DeKyD`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "a85b3da2-6921-410f-ac7a-7b86a3bb0c1a",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib"
    ],
    "durationMs": 13,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the references.bib to understand available keys, and also check if there's an existing background.tex or any other sections for cross-reference consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "51cd62b9-75ea-43ad-aba6-dc1a28ce744f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bML9B2Azv2bB2kouksSBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13651,
      "cache_read_input_tokens": 24988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13651
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

Let me check the existing paper structure and references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "df65ad07-f3c6-4209-b4bd-976948e3d6c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bML9B2Azv2bB2kouksSBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13651,
      "cache_read_input_tokens": 24988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13651
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

<details open><summary>🔧 Tool call — Read · `toolu_01Qfpi9HP84XYDEqsmJSM6U1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "dd833870-bd8e-4d36-9f18-be0ded822176",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bML9B2Azv2bB2kouksSBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13651,
      "cache_read_input_tokens": 24988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13651
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

_source line 16 · 2026-05-20T22:59:04.478Z_

<details><summary>↩ Tool result · `toolu_01Qfpi9HP84XYDEqsmJSM6U1`</summary>

```text
1	% =============================================================================
2	% Benchmark Datasets
3	% =============================================================================
4	
5	@inproceedings{zellers2019hellaswag,
6	  title={{HellaSwag}: Can a Machine Really Finish Your Sentence?},
7	  author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
8	  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
9	  pages={4791--4800},
10	  year={2019},
11	  url={https://doi.org/10.18653/v1/P19-1472}
12	}
13	
14	@article{cobbe2021gsm8k,
15	  title={Training Verifiers to Solve Math Word Problems},
16	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
17	  journal={arXiv preprint arXiv:2110.14168},
18	  year={2021}
19	}
20	
21	@article{clark2018arc,
22	  title={Think you have Solved Question Answering? Try {ARC}, the {AI2} Reasoning Challenge},
23	  author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
24	  journal={arXiv preprint arXiv:1803.05457},
25	  year={2018}
26	}
27	
28	@article{chen2021humaneval,
29	  title={Evaluating Large Language Models Trained on Code},
30	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Pond{\'e} de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
31	  journal={arXiv preprint arXiv:2107.03374},
32	  year={2021}
33	}
34	
35	% =============================================================================
36	% IRT for LLM Evaluation
37	% =============================================================================
38	
39	@article{martinezplumed2019,
40	  title = {Item Response Theory in {AI}: Analysing Machine Learning Classifiers at the Instance Level},
41	  author = {Mart{\'\i}nez-Plumed, F. and Prud{\^e}ncio, R. B. C. and Mart{\'\i}nez-Us{\'o}, A. and Hern{\'a}ndez-Orallo, J.},
42	  journal = {Artificial Intelligence},
43	  year = {2019},
44	  doi = {10.1016/j.artint.2018.09.004},
45	  url = {https://www.sciencedirect.com/science/article/pii/S0004370219300220},
46	}
47	
48	@inproceedings{polo2024tinybenchmarks,
49	  title = {tinyBenchmarks: Evaluating {LLMs} with Fewer Examples},
50	  author = {Polo, F. M. and Weber, L. and Choshen, L. and Sun, Y. and Xu, G. and Yurochkin, M.},
51	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
52	  year = {2024},
53	  url = {https://arxiv.org/abs/2402.14992},
54	}
55	
56	@article{atlas2025,
57	  title = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
58	  author = {Li, P. and Tang, X. and Chen, S. and Cheng, Y. and Metoyer, R. and Hua, T. and Chawla, N. V.},
59	  journal = {arXiv preprint arXiv:2511.04689},
60	  year = {2025},
61	  url = {https://arxiv.org/abs/2511.04689},
62	}
63	
64	@inproceedings{psnirt2026,
65	  title = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
66	  author = {Zhou, H. and Huang, H. and Zhao, Z. and Han, L. and Wang, H. and Chen, K. and Yang, M. and Bao, W. and Dong, J. and Xu, B. and Zhu, C. and Cao, H. and Zhao, T.},
67	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
68	  year = {2026},
69	  url = {https://arxiv.org/abs/2505.15055},
70	}
71	
72	% =============================================================================
73	% Benchmark Contamination Detection
74	% =============================================================================
75	
76	@inproceedings{dodge2021,
77	  title = {Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus},
78	  author = {Dodge, J. and Sap, M. and Marasovi{\'c}, A. and Agnew, W. and Ilharco, G. and Groeneveld, D. and Mitchell, M. and Gardner, M.},
79	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
80	  year = {2021},
81	  doi = {10.18653/v1/2021.emnlp-main.98},
82	  url = {https://aclanthology.org/2021.emnlp-main.98/},
83	}
84	
85	@inproceedings{magar2022,
86	  title = {Data Contamination: From Memorization to Exploitation},
87	  author = {Magar, I. and Schwartz, R.},
88	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
89	  year = {2022},
90	  doi = {10.18653/v1/2022.acl-short.18},
91	  url = {https://aclanthology.org/2022.acl-short.18/},
92	}
93	
94	@inproceedings{sainz2023,
95	  title = {{NLP} Evaluation in Trouble: On the Need to Measure {LLM} Data Contamination for each Benchmark},
96	  author = {Sainz, O. and Campos, J. and Garc{\'\i}a-Ferrero, I. and Etxaniz, J. and Lopez de Lacalle, O. and Agirre, E.},
97	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023},
98	  year = {2023},
99	  doi = {10.18653/v1/2023.findings-emnlp.722},
100	  url = {https://aclanthology.org/2023.findings-emnlp.722/},
101	}
102	
103	@inproceedings{jacovi2023,
104	  title = {Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks},
105	  author = {Jacovi, A. and Caciularu, A. and Goldman, O. and Goldberg, Y.},
106	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
107	  year = {2023},
108	  doi = {10.18653/v1/2023.emnlp-main.308},
109	  url = {https://aclanthology.org/2023.emnlp-main.308/},
110	}
111	
112	@inproceedings{constat2024,
113	  title = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
114	  author = {Dekoninck, J. and M{\"u}ller, M. and Vechev, M.},
115	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
116	  year = {2024},
117	  url = {https://arxiv.org/abs/2405.16281},
118	}
119	
120	@inproceedings{minkprob2024,
121	  title = {Detecting Pretraining Data from Large Language Models},
122	  author = {Shi, W. and Ajith, A. and Xia, M. and Huang, Y. and Liu, D. and Blevins, T. and Chen, D. and Zettlemoyer, L.},
123	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
124	  year = {2024},
125	  url = {https://arxiv.org/abs/2310.16789},
126	}
127	
128	@inproceedings{oren2024,
129	  title = {Proving Test Set Contamination in Black-Box Language Models},
130	  author = {Oren, Y. and Meister, N. and Chatterji, N. S. and Ladhak, F. and Hashimoto, T.},
131	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
132	  year = {2024},
133	  url = {https://arxiv.org/abs/2310.17623},
134	}
135	
136	@inproceedings{golchin2024,
137	  title = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
138	  author = {Golchin, S. and Surdeanu, M.},
139	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
140	  year = {2024},
141	  url = {https://arxiv.org/abs/2308.08493},
142	}
143	
144	@inproceedings{deng2024,
145	  title = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},
146	  author = {Deng, C. and Zhao, Y. and Tang, X. and Gerstein, M. and Cohan, A.},
147	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
148	  year = {2024},
149	  doi = {10.18653/v1/2024.naacl-long.482},
150	  url = {https://aclanthology.org/2024.naacl-long.482/},
151	}
152	
153	@inproceedings{codec2026,
154	  title = {Detecting Data Contamination in {LLMs} via In-Context Learning},
155	  author = {Zawalski, M. and Boubdir, M. and Ba{\l}azy, K. and Nushi, B. and Ribalta, P.},
156	  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},
157	  year = {2026},
158	  url = {https://arxiv.org/abs/2510.27055},
159	}
160	
161	% =============================================================================
162	% Person-Fit Statistics (Psychometrics)
163	% =============================================================================
164	
165	@article{drasgow1985,
166	  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},
167	  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},
168	  journal = {British Journal of Mathematical and Statistical Psychology},
169	  year = {1985},
170	  doi = {10.1111/j.2044-8317.1985.tb00817.x},
171	}
172	
173	@article{meijer2001,
174	  title = {Methodology Review: Evaluating Person Fit},
175	  author = {Meijer, R. R. and Sijtsma, K.},
176	  journal = {Applied Psychological Measurement},
177	  year = {2001},
178	  doi = {10.1177/01466210122031957},
179	  url = {https://journals.sagepub.com/doi/abs/10.1177/01466210122031957},
180	}
181	
182	@article{snijders2001,
183	  title = {Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Parameter},
184	  author = {Snijders, T. A. B.},
185	  journal = {Psychometrika},
186	  year = {2001},
187	  doi = {10.1007/BF02294437},
188	  url = {https://link.springer.com/article/10.1007/BF02294437},
189	}
190	
191	@article{karabatsos2003,
192	  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},
193	  author = {Karabatsos, G.},
194	  journal = {Applied Measurement in Education},
195	  year = {2003},
196	  doi = {10.1207/S15324818AME1604_2},
197	  url = {https://www.tandfonline.com/doi/abs/10.1207/S15324818AME1604_2},
198	}
199	
200	@article{sinharay2017,
201	  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?},
202	  author = {Sinharay, S.},
203	  journal = {Applied Psychological Measurement},
204	  year = {2017},
205	  doi = {10.1177/0146621617698453},
206	  url = {https://pmc.ncbi.nlm.nih.gov/articles/PMC5978524/},
207	}
208	
209	@article{hong2021lzm,
210	  title = {Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types},
211	  author = {Hong, M. and Lin, L. and Cheng, Y.},
212	  journal = {Psychometrika},
213	  year = {2021},
214	  doi = {10.1007/s11336-021-09756-3},
215	  url = {https://link.springer.com/article/10.1007/s11336-021-09756-3},
216	}
217	
218	% =============================================================================
219	% Post-RL Contamination
220	% =============================================================================
221	
222	@article{wang2025fragility,
223	  title = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},
224	  author = {Wang, H. and Li, H. and Ko, B. and Zhang, H.},
225	  journal = {arXiv preprint arXiv:2510.02386},
226	  year = {2025},
227	  url = {https://arxiv.org/abs/2510.02386},
228	}
229	
230	@inproceedings{selfcritique2026,
231	  title = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
232	  author = {Tao, Y. and Wang, T. and Dong, Y. and Liu, H. and Zhang, K. and Hu, X. and Li, G.},
233	  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},
234	  year = {2026},
235	  url = {https://arxiv.org/abs/2510.09259},
236	}
237	
238	@article{zhang2026rlvr,
239	  title = {Detecting {RLVR} Training Data via Structural Convergence of Reasoning},
240	  author = {Zhang, H. and Yang, Y. and Yan, J. and Bao, G. and Zhang, Y. and Zhang, Y.},
241	  journal = {arXiv preprint arXiv:2602.11792},
242	  year = {2026},
243	  url = {https://arxiv.org/abs/2602.11792},
244	}
245	
246	% =============================================================================
247	% IRT Foundations
248	% =============================================================================
249	
250	@incollection{birnbaum1968,
251	  title = {Some Latent Trait Models and Their Use in Inferring an Examinee's Ability},
252	  author = {Birnbaum, A.},
253	  booktitle = {Statistical Theories of Mental Test Scores},
254	  publisher = {Addison-Wesley},
255	  year = {1968},
256	  editor = {Lord, F. M. and Novick, M. R.},
257	  pages = {397--479},
258	}
259	
260	@book{lord1980,
261	  title = {Applications of Item Response Theory to Practical Testing Problems},
262	  author = {Lord, F. M.},
263	  publisher = {Lawrence Erlbaum Associates},
264	  year = {1980},
265	  doi = {10.4324/9780203056615},
266	}
267	
268	@techreport{barton1981,
269	  title = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},
270	  author = {Barton, M. A. and Lord, F. M.},
271	  institution = {Educational Testing Service},
272	  year = {1981},
273	  number = {RR-81-20},
274	  doi = {10.1002/j.2333-8504.1981.tb01255.x},
275	  url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2333-8504.1981.tb01255.x},
276	}
277	
278	@book{embretson2000,
279	  title = {Item Response Theory for Psychologists},
280	  author = {Embretson, S. E. and Reise, S. P.},
281	  publisher = {Lawrence Erlbaum Associates},
282	  year = {2000},
283	  doi = {10.4324/9781410605269},
284	}
285	
286	@book{deayala2009,
287	  title = {The Theory and Practice of Item Response Theory},
288	  author = {de Ayala, R. J.},
289	  publisher = {Guilford Press},
290	  year = {2009},
291	}
292	
293	% =============================================================================
294	% LLM Evaluation Infrastructure
295	% =============================================================================
296	
297	@inproceedings{hendrycks2021mmlu,
298	  title = {Measuring Massive Multitask Language Understanding},
299	  author = {Hendrycks, D. and Burns, C. and Basart, S. and Zou, A. and Mazeika, M. and Song, D. and Steinhardt, J.},
300	  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},
301	  year = {2021},
302	  url = {https://arxiv.org/abs/2009.03300},
303	}
304	
305	@misc{beeching2023openllm,
306	  title = {Open {LLM} Leaderboard},
307	  author = {Beeching, E. and Fourrier, C. and Habib, N. and Han, S. and Lambert, N. and Rajani, N. and Sanseviero, O. and Tunstall, L. and Wolf, T.},
308	  year = {2023},
309	  howpublished = {HuggingFace},
310	  url = {https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard},
311	}
312	
313	@misc{gao2023evalharness,
314	  title = {A Framework for Few-Shot Language Model Evaluation},
315	  author = {Gao, L. and Tow, J. and Abbasi, B. and Biderman, S. and Black, S. and DiPofi, A. and Foster, C. and Golding, L. and Hsu, J. and Le Noac'h, A. and Li, H. and McDonell, K. and Muennighoff, N. and Ociepa, C. and Phang, J. and Reynolds, L. and Schoelkopf, H. and Skowron, A. and Sutawika, L. and Tang, E. and Thite, A. and Wang, B. and Wang, K. and Zou, A.},
316	  year = {2023},
317	  howpublished = {Zenodo},
318	  doi = {10.5281/zenodo.10256836},
319	  url = {https://zenodo.org/records/10256836},
320	}
321	
322	@article{chang2024survey,
323	  title = {A Survey on Evaluation of Large Language Models},
324	  author = {Chang, Y. and Wang, X. and Wang, J. and Wu, Y. and Yang, L. and Zhu, K. and Chen, H. and Yi, X. and Wang, C. and Wang, Y. and Ye, W. and Zhang, Y. and Chang, Y. and Yu, P. S. and Yang, Q. and Xie, X.},
325	  journal = {ACM Transactions on Intelligent Systems and Technology},
326	  year = {2024},
327	  doi = {10.1145/3641289},
328	  url = {https://arxiv.org/abs/2307.03109},
329	}
330	
331	@article{biderman2024lessons,
332	  title = {Lessons from the Trenches on Reproducible Evaluation of Language Models},
333	  author = {Biderman, S. and Schoelkopf, H. and Sutawika, L. and Gao, L. and Tow, J. and Abbasi, B. and Aji, A. F. and Ammanamanchi, P. S. and Black, S. and Clive, J. and DiPofi, A. and Etxaniz, J. and Fattori, B. and Forde, J. Z. and Foster, C. and Hsu, J. and Jaiswal, M. and Lee, W. Y. and Li, H. and Lovering, C. and Muennighoff, N. and Pavlick, E. and Phang, J. and Skowron, A. and Tan, S. and Tang, X. and Wang, K. A. and Winata, G. I. and Yvon, F. and Zou, A.},
334	  journal = {arXiv preprint arXiv:2405.14782},
335	  year = {2024},
336	  url = {https://arxiv.org/abs/2405.14782},
337	}
338	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "f1f61f89-8405-4f74-a29b-61bc38ac55bf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/references.bib",
      "content": "% =============================================================================\n% Benchmark Datasets\n% =============================================================================\n\n@inproceedings{zellers2019hellaswag,\n  title={{HellaSwag}: Can a Machine Really Finish Your Sentence?},\n  author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},\n  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n  pages={4791--4800},\n  year={2019},\n  url={https://doi.org/10.18653/v1/P19-1472}\n}\n\n@article{cobbe2021gsm8k,\n  title={Training Verifiers to Solve Math Word Problems},\n  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal={arXiv preprint arXiv:2110.14168},\n  year={2021}\n}\n\n@article{clark2018arc,\n  title={Think you have Solved Question Answering? Try {ARC}, the {AI2} Reasoning Challenge},\n  author={Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  journal={arXiv preprint arXiv:1803.05457},\n  year={2018}\n}\n\n@article{chen2021humaneval,\n  title={Evaluating Large Language Models Trained on Code},\n  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Pond{\\'e} de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal={arXiv preprint arXiv:2107.03374},\n  year={2021}\n}\n\n% =============================================================================\n% IRT for LLM Evaluation\n% =============================================================================\n\n@article{martinezplumed2019,\n  title = {Item Response Theory in {AI}: Analysing Machine Learning Classifiers at the Instance Level},\n  author = {Mart{\\'\\i}nez-Plumed, F. and Prud{\\^e}ncio, R. B. C. and Mart{\\'\\i}nez-Us{\\'o}, A. and Hern{\\'a}ndez-Orallo, J.},\n  journal = {Artificial Intelligence},\n  year = {2019},\n  doi = {10.1016/j.artint.2018.09.004},\n  url = {https://www.sciencedirect.com/science/article/pii/S0004370219300220},\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  title = {tinyBenchmarks: Evaluating {LLMs} with Fewer Examples},\n  author = {Polo, F. M. and Weber, L. and Choshen, L. and Sun, Y. and Xu, G. and Yurochkin, M.},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.14992},\n}\n\n@article{atlas2025,\n  title = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  author = {Li, P. and Tang, X. and Chen, S. and Cheng, Y. and Metoyer, R. and Hua, T. and Chawla, N. V.},\n  journal = {arXiv preprint arXiv:2511.04689},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.04689},\n}\n\n@inproceedings{psnirt2026,\n  title = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  author = {Zhou, H. and Huang, H. and Zhao, Z. and Han, L. and Wang, H. and Chen, K. and Yang, M. and Bao, W. and Dong, J. and Xu, B. and Zhu, C. and Cao, H. and Zhao, T.},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2505.15055},\n}\n\n% =============================================================================\n% Benchmark Contamination Detection\n% =============================================================================\n\n@inproceedings{dodge2021,\n  title = {Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus},\n  author = {Dodge, J. and Sap, M. and Marasovi{\\'c}, A. and Agnew, W. and Ilharco, G. and Groeneveld, D. and Mitchell, M. and Gardner, M.},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2021},\n  doi = {10.18653/v1/2021.emnlp-main.98},\n  url = {https://aclanthology.org/2021.emnlp-main.98/},\n}\n\n@inproceedings{magar2022,\n  title = {Data Contamination: From Memorization to Exploitation},\n  author = {Magar, I. and Schwartz, R.},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.acl-short.18},\n  url = {https://aclanthology.org/2022.acl-short.18/},\n}\n\n@inproceedings{sainz2023,\n  title = {{NLP} Evaluation in Trouble: On the Need to Measure {LLM} Data Contamination for each Benchmark},\n  author = {Sainz, O. and Campos, J. and Garc{\\'\\i}a-Ferrero, I. and Etxaniz, J. and Lopez de Lacalle, O. and Agirre, E.},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-emnlp.722},\n  url = {https://aclanthology.org/2023.findings-emnlp.722/},\n}\n\n@inproceedings{jacovi2023,\n  title = {Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks},\n  author = {Jacovi, A. and Caciularu, A. and Goldman, O. and Goldberg, Y.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.308},\n  url = {https://aclanthology.org/2023.emnlp-main.308/},\n}\n\n@inproceedings{constat2024,\n  title = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  author = {Dekoninck, J. and M{\\\"u}ller, M. and Vechev, M.},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.16281},\n}\n\n@inproceedings{minkprob2024,\n  title = {Detecting Pretraining Data from Large Language Models},\n  author = {Shi, W. and Ajith, A. and Xia, M. and Huang, Y. and Liu, D. and Blevins, T. and Chen, D. and Zettlemoyer, L.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.16789},\n}\n\n@inproceedings{oren2024,\n  title = {Proving Test Set Contamination in Black-Box Language Models},\n  author = {Oren, Y. and Meister, N. and Chatterji, N. S. and Ladhak, F. and Hashimoto, T.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.17623},\n}\n\n@inproceedings{golchin2024,\n  title = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  author = {Golchin, S. and Surdeanu, M.},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.08493},\n}\n\n@inproceedings{deng2024,\n  title = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  author = {Deng, C. and Zhao, Y. and Tang, X. and Gerstein, M. and Cohan, A.},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.482},\n  url = {https://aclanthology.org/2024.naacl-long.482/},\n}\n\n@inproceedings{codec2026,\n  title = {Detecting Data Contamination in {LLMs} via In-Context Learning},\n  author = {Zawalski, M. and Boubdir, M. and Ba{\\l}azy, K. and Nushi, B. and Ribalta, P.},\n  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2510.27055},\n}\n\n% =============================================================================\n% Person-Fit Statistics (Psychometrics)\n% =============================================================================\n\n@article{drasgow1985,\n  title = {Appropriateness Measurement with Polychotomous Item Response Models and Standardized Indices},\n  author = {Drasgow, F. and Levine, M. V. and Williams, E. A.},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  year = {1985},\n  doi = {10.1111/j.2044-8317.1985.tb00817.x},\n}\n\n@article{meijer2001,\n  title = {Methodology Review: Evaluating Person Fit},\n  author = {Meijer, R. R. and Sijtsma, K.},\n  journal = {Applied Psychological Measurement},\n  year = {2001},\n  doi = {10.1177/01466210122031957},\n  url = {https://journals.sagepub.com/doi/abs/10.1177/01466210122031957},\n}\n\n@article{snijders2001,\n  title = {Asymptotic Null Distribution of Person Fit Statistics with Estimated Person Parameter},\n  author = {Snijders, T. A. B.},\n  journal = {Psychometrika},\n  year = {2001},\n  doi = {10.1007/BF02294437},\n  url = {https://link.springer.com/article/10.1007/BF02294437},\n}\n\n@article{karabatsos2003,\n  title = {Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics},\n  author = {Karabatsos, G.},\n  journal = {Applied Measurement in Education},\n  year = {2003},\n  doi = {10.1207/S15324818AME1604_2},\n  url = {https://www.tandfonline.com/doi/abs/10.1207/S15324818AME1604_2},\n}\n\n@article{sinharay2017,\n  title = {Which Statistic Should Be Used to Detect Item Preknowledge When the Set of Compromised Items Is Known?},\n  author = {Sinharay, S.},\n  journal = {Applied Psychological Measurement},\n  year = {2017},\n  doi = {10.1177/0146621617698453},\n  url = {https://pmc.ncbi.nlm.nih.gov/articles/PMC5978524/},\n}\n\n@article{hong2021lzm,\n  title = {Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types},\n  author = {Hong, M. and Lin, L. and Cheng, Y.},\n  journal = {Psychometrika},\n  year = {2021},\n  doi = {10.1007/s11336-021-09756-3},\n  url = {https://link.springer.com/article/10.1007/s11336-021-09756-3},\n}\n\n% =============================================================================\n% Post-RL Contamination\n% =============================================================================\n\n@article{wang2025fragility,\n  title = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},\n  author = {Wang, H. and Li, H. and Ko, B. and Zhang, H.},\n  journal = {arXiv preprint arXiv:2510.02386},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.02386},\n}\n\n@inproceedings{selfcritique2026,\n  title = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  author = {Tao, Y. and Wang, T. and Dong, Y. and Liu, H. and Zhang, K. and Hu, X. and Li, G.},\n  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2510.09259},\n}\n\n@article{zhang2026rlvr,\n  title = {Detecting {RLVR} Training Data via Structural Convergence of Reasoning},\n  author = {Zhang, H. and Yang, Y. and Yan, J. and Bao, G. and Zhang, Y. and Zhang, Y.},\n  journal = {arXiv preprint arXiv:2602.11792},\n  year = {2026},\n  url = {https://arxiv.org/abs/2602.11792},\n}\n\n% =============================================================================\n% IRT Foundations\n% =============================================================================\n\n@incollection{birnbaum1968,\n  title = {Some Latent Trait Models and Their Use in Inferring an Examinee's Ability},\n  author = {Birnbaum, A.},\n  booktitle = {Statistical Theories of Mental Test Scores},\n  publisher = {Addison-Wesley},\n  year = {1968},\n  editor = {Lord, F. M. and Novick, M. R.},\n  pages = {397--479},\n}\n\n@book{lord1980,\n  title = {Applications of Item Response Theory to Practical Testing Problems},\n  author = {Lord, F. M.},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {1980},\n  doi = {10.4324/9780203056615},\n}\n\n@techreport{barton1981,\n  title = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  author = {Barton, M. A. and Lord, F. M.},\n  institution = {Educational Testing Service},\n  year = {1981},\n  number = {RR-81-20},\n  doi = {10.1002/j.2333-8504.1981.tb01255.x},\n  url = {https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2333-8504.1981.tb01255.x},\n}\n\n@book{embretson2000,\n  title = {Item Response Theory for Psychologists},\n  author = {Embretson, S. E. and Reise, S. P.},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {2000},\n  doi = {10.4324/9781410605269},\n}\n\n@book{deayala2009,\n  title = {The Theory and Practice of Item Response Theory},\n  author = {de Ayala, R. J.},\n  publisher = {Guilford Press},\n  year = {2009},\n}\n\n% =============================================================================\n% LLM Evaluation Infrastructure\n% =============================================================================\n\n@inproceedings{hendrycks2021mmlu,\n  title = {Measuring Massive Multitask Language Understanding},\n  author = {Hendrycks, D. and Burns, C. and Basart, S. and Zou, A. and Mazeika, M. and Song, D. and Steinhardt, J.},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.03300},\n}\n\n@misc{beeching2023openllm,\n  title = {Open {LLM} Leaderboard},\n  author = {Beeching, E. and Fourrier, C. and Habib, N. and Han, S. and Lambert, N. and Rajani, N. and Sanseviero, O. and Tunstall, L. and Wolf, T.},\n  year = {2023},\n  howpublished = {HuggingFace},\n  url = {https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard},\n}\n\n@misc{gao2023evalharness,\n  title = {A Framework for Few-Shot Language Model Evaluation},\n  author = {Gao, L. and Tow, J. and Abbasi, B. and Biderman, S. and Black, S. and DiPofi, A. and Foster, C. and Golding, L. and Hsu, J. and Le Noac'h, A. and Li, H. and McDonell, K. and Muennighoff, N. and Ociepa, C. and Phang, J. and Reynolds, L. and Schoelkopf, H. and Skowron, A. and Sutawika, L. and Tang, E. and Thite, A. and Wang, B. and Wang, K. and Zou, A.},\n  year = {2023},\n  howpublished = {Zenodo},\n  doi = {10.5281/zenodo.10256836},\n  url = {https://zenodo.org/records/10256836},\n}\n\n@article{chang2024survey,\n  title = {A Survey on Evaluation of Large Language Models},\n  author = {Chang, Y. and Wang, X. and Wang, J. and Wu, Y. and Yang, L. and Zhu, K. and Chen, H. and Yi, X. and Wang, C. and Wang, Y. and Ye, W. and Zhang, Y. and Chang, Y. and Yu, P. S. and Yang, Q. and Xie, X.},\n  journal = {ACM Transactions on Intelligent Systems and Technology},\n  year = {2024},\n  doi = {10.1145/3641289},\n  url = {https://arxiv.org/abs/2307.03109},\n}\n\n@article{biderman2024lessons,\n  title = {Lessons from the Trenches on Reproducible Evaluation of Language Models},\n  author = {Biderman, S. and Schoelkopf, H. and Sutawika, L. and Gao, L. and Tow, J. and Abbasi, B. and Aji, A. F. and Ammanamanchi, P. S. and Black, S. and Clive, J. and DiPofi, A. and Etxaniz, J. and Fattori, B. and Forde, J. Z. and Foster, C. and Hsu, J. and Jaiswal, M. and Lee, W. Y. and Li, H. and Lovering, C. and Muennighoff, N. and Pavlick, E. and Phang, J. and Skowron, A. and Tan, S. and Tang, X. and Wang, K. A. and Winata, G. I. and Yvon, F. and Zou, A.},\n  journal = {arXiv preprint arXiv:2405.14782},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.14782},\n}\n",
      "numLines": 338,
      "startLine": 1,
      "totalLines": 338
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01TPbs7DtVNFGcWd1ok2s1eg`</summary>

```json
{
  "pattern": "paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "c4031db2-8863-43ad-9168-d144f6632b92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bML9B2Azv2bB2kouksSBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13651,
      "cache_read_input_tokens": 24988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13651
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

_source line 18 · 2026-05-20T22:59:05.302Z_

<details><summary>↩ Tool result · `toolu_01TPbs7DtVNFGcWd1ok2s1eg`</summary>

```text
paper/sections/introduction.tex
paper/sections/appendix.tex
paper/sections/abstract.tex
paper/sections/background.tex
paper/sections/limitations.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
paper/sections/experiments.tex
paper/sections/sec_setup.tex
paper/sections/sec_empirical.tex
paper/sections/sec_simulation.tex
paper/sections/method.tex
paper/sections/sec_ctrl_contam.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "e55b07a4-673e-4051-91fe-db07f244a311",
  "tool_use_result": {
    "filenames": [
      "paper/sections/introduction.tex",
      "paper/sections/appendix.tex",
      "paper/sections/abstract.tex",
      "paper/sections/background.tex",
      "paper/sections/limitations.tex",
      "paper/sections/discussion.tex",
      "paper/sections/conclusion.tex",
      "paper/sections/experiments.tex",
      "paper/sections/sec_setup.tex",
      "paper/sections/sec_empirical.tex",
      "paper/sections/sec_simulation.tex",
      "paper/sections/method.tex",
      "paper/sections/sec_ctrl_contam.tex"
    ],
    "durationMs": 128,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing background.tex to see if there's content already, and also check the introduction for cross-reference consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "92d4c6d5-1b33-48f9-8ae1-688ace9f1e7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UXKF5hvq53yhZqVWVqsWd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 38639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6615
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

_source line 20_

Let me check the existing background.tex and introduction for cross-reference consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "70e5154f-a778-4f9c-aefc-80eb1650f1ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UXKF5hvq53yhZqVWVqsWd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 38639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6615
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01P3gx5JjcrHduEx8MHmUj1j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "eb1b1876-7b6c-48ee-8651-e748b0555c31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UXKF5hvq53yhZqVWVqsWd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 38639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6615
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

_source line 22 · 2026-05-20T22:59:10.913Z_

<details><summary>↩ Tool result · `toolu_01P3gx5JjcrHduEx8MHmUj1j`</summary>

```text
1	% background
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "41dcc818-ba53-41be-92d2-91eee42cf016",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex",
      "content": "% background\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Df8GNBRzLyNVtUqwPRsSM4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "d3505b4e-c4a2-4ef9-a3a5-806270f2492f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016UXKF5hvq53yhZqVWVqsWd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 38639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6615
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

_source line 24 · 2026-05-20T22:59:11.100Z_

<details><summary>↩ Tool result · `toolu_01Df8GNBRzLyNVtUqwPRsSM4`</summary>

```text
1	% introduction
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "385ff148-df21-40a1-a27d-45a72dbdc9ab",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex",
      "content": "% introduction\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Both files are essentially empty placeholders. Let me also quickly check the experiments section to understand how Table 1 (the frontier table) is defined, so I can reference it correctly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "fd3610ab-7853-4a85-a878-c27d95d576a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkqCAzDSkwPiuhgUB81Utx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 45254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 26_

Let me check where Table 1 (the detection frontier) is defined.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "6ee5ab37-65ff-4ef6-9573-f7f1c664d529",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkqCAzDSkwPiuhgUB81Utx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 45254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01Wkx2b2zBW82WmwtM1yszQP`</summary>

```json
{
  "pattern": "tab:frontier",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "8fe37542-c308-490e-82c9-ddc0d4b7a007",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkqCAzDSkwPiuhgUB81Utx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 45254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 28 · 2026-05-20T22:59:15.617Z_

<details><summary>↩ Tool result · `toolu_01Wkx2b2zBW82WmwtM1yszQP`</summary>

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
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "27e46dc1-f3f8-44b7-aad7-bbcaa466429c",
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

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_019BiuZEZmyyXSgN4SDFoNtv`</summary>

```json
{
  "pattern": "frontier",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "bdacbdcc-8119-41a9-80d6-5b078d83c86c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFEWuZAKY8PpjpeWcrkQCN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 45655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 208
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

_source line 30 · 2026-05-20T22:59:18.496Z_

<details><summary>↩ Tool result · `toolu_019BiuZEZmyyXSgN4SDFoNtv`</summary>

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
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "6ec8f550-72e7-4951-b16a-e6cbd523309c",
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

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
The frontier table doesn't exist yet. The task says to mention Table 1 (\ref{tab:frontier}), so I'll reference it as `\ref{tab:frontier}` and it'll be defined elsewhere (likely in the experiments section or the introduction).

Now let me write the background section. Key constraints:
1. ~650 words
2. Do NOT repeat 4PL equation (it's in §3 as Eq. 1)
3. Do NOT repeat lz* formal definition (also in §3)
4. Two subsections: IRT and Person-Fit Statistics (~350 words), Benchmark Contamination Detection (~300 words)


5. No dashes (em-dash, en-dash except for ranges)
6. No AI writing patterns
7. Dense, self-contained for ML reviewers

I need to write this carefully, avoiding stylistic markers and keeping the prose tight for a technical audience.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "487f1df4-fd97-4d1f-a556-9f3e7bb452c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdugTDdANfkhtwrmUQEQZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 45863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 136
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

_source line 32_

Now I have all the context needed. Writing the section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "c755e844-47b8-4780-bdba-521e62e268b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdugTDdANfkhtwrmUQEQZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 45863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 136
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

_source line 33_

<details open><summary>🔧 Tool call — Write · `toolu_01VHM1vQypcMMWDaCwHzGqyS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex",
  "content": "\\section{Background and Related Work}\\label{sec:background}\n\n\\subsection{IRT and Person-Fit Statistics}\\label{sec:irt_background}\n\nItem Response Theory (IRT) models the probability that an examinee answers a test item correctly as a function of the examinee's latent ability $\\theta$ and item-level parameters \\citep{lord1980, embretson2000}.\nThe four-parameter logistic (4PL) model, formalized in \\S\\ref{sec:framework} (Eq.~\\ref{eq:4pl}), extends the classical three-parameter model \\citep{birnbaum1968} with an upper asymptote $d$ that captures the probability of error even at high ability \\citep{barton1981}.\nThis parameter matters for LLMs: \\citet{psnirt2026} find that 46\\% of MMLU items have $d < 0.95$, meaning ceiling effects are pervasive and a model without the $d$ parameter systematically misestimates item characteristics.\n\nGiven calibrated item parameters, person-fit statistics measure whether an examinee's \\emph{pattern} of correct and incorrect responses is consistent with the IRT model at the estimated ability level.\nThe key intuition is that a test-taker with ability $\\theta$ should get hard items wrong and easy items right at rates the model predicts; systematic deviations signal aberrant behavior.\n\\citet{drasgow1985} introduced $\\ell_z$, a standardized log-likelihood residual that aggregates per-item deviations into a single score.\n\\citet{snijders2001} corrected the variance of $\\ell_z$ for uncertainty in the estimated $\\hat{\\theta}$, yielding $\\ell_z^*$ with the property that $\\ell_z^* \\sim \\mathcal{N}(0,1)$ under the null hypothesis of model-consistent responding.\nNegative values indicate \\emph{aberrant} patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate \\emph{over-consistent} patterns (responses too predictable given the model).\nWe defer the formal definition to \\S\\ref{sec:framework}.\n\nIn psychometrics, person-fit statistics have a long history in detecting test fraud and item preknowledge.\n\\citet{karabatsos2003} compared 36 person-fit statistics and found $\\ell_z$ among the most powerful for detecting cheating.\n\\citet{sinharay2017} showed that $\\ell_z^*$ is particularly effective when the compromised item set is known, a setting analogous to benchmark contamination where the ``compromised'' items are those memorized during pretraining.\n\\citet{meijer2001} provide a comprehensive review of the broader person-fit literature.\nOur work transfers this psychometric toolkit to LLM evaluation, treating each model as an examinee whose response pattern may reveal memorization.\n\n\\subsection{Benchmark Contamination Detection}\\label{sec:contamination_related}\n\nContamination detection methods vary in what information they require from the model under test.\nTable~\\ref{tab:frontier} organizes the detection frontier by information access, from most to least demanding.\nAt the high end, corpus-search methods match benchmark items against pretraining data \\citep{dodge2021, magar2022}, but require full corpus access, which is unavailable for closed models.\nMembership inference attacks (MIA) use token-level log-probabilities to distinguish training examples from unseen ones \\citep{minkprob2024, deng2024}.\nGeneration-based probes elicit benchmark content via prompting \\citep{golchin2024, oren2024}.\nPerformance-based methods such as ConStat \\citep{constat2024} and CoDeC \\citep{codec2026} compare a model's accuracy on the target benchmark against accuracy on perturbed or reference sets, requiring either multiple evaluations or in-context learning passes.\n\\citet{sainz2023} propose overlapping-split analysis using time-stamped data.\n\nA critical limitation unites all log-probability methods: \\citet{wang2025fragility} demonstrate that reinforcement learning (RL) post-training renders MIA-based detectors (including Min-K\\%++) no better than random across 10 methods and 4 benchmarks.\nRL reshapes output distributions without altering which items a model answers correctly, so token-level statistics lose signal while binary correctness patterns are structurally preserved.\n\\citet{selfcritique2026} and \\citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.\n\nIRT-\\textsc{Fit} operates at the bottom of this frontier: it requires only binary responses (correct/incorrect), making it applicable to any model accessible through a standard evaluation API.\nRecent work applies IRT to LLM evaluation for ability estimation \\citep{martinezplumed2019, polo2024tinybenchmarks}, adaptive testing \\citep{atlas2025}, and benchmark diagnostics \\citep{psnirt2026}, but none use \\emph{person-fit} statistics for contamination detection.\nOur work bridges this gap.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "6e7821e6-80c0-403e-ab09-2e6c91361a60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdugTDdANfkhtwrmUQEQZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 136,
      "cache_read_input_tokens": 45863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 136
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

_source line 34 · 2026-05-20T23:00:04.526Z_

<details><summary>↩ Tool result · `toolu_01VHM1vQypcMMWDaCwHzGqyS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "ece82c2a-d46c-4851-be2c-b6f572af9d5b",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex",
    "content": "\\section{Background and Related Work}\\label{sec:background}\n\n\\subsection{IRT and Person-Fit Statistics}\\label{sec:irt_background}\n\nItem Response Theory (IRT) models the probability that an examinee answers a test item correctly as a function of the examinee's latent ability $\\theta$ and item-level parameters \\citep{lord1980, embretson2000}.\nThe four-parameter logistic (4PL) model, formalized in \\S\\ref{sec:framework} (Eq.~\\ref{eq:4pl}), extends the classical three-parameter model \\citep{birnbaum1968} with an upper asymptote $d$ that captures the probability of error even at high ability \\citep{barton1981}.\nThis parameter matters for LLMs: \\citet{psnirt2026} find that 46\\% of MMLU items have $d < 0.95$, meaning ceiling effects are pervasive and a model without the $d$ parameter systematically misestimates item characteristics.\n\nGiven calibrated item parameters, person-fit statistics measure whether an examinee's \\emph{pattern} of correct and incorrect responses is consistent with the IRT model at the estimated ability level.\nThe key intuition is that a test-taker with ability $\\theta$ should get hard items wrong and easy items right at rates the model predicts; systematic deviations signal aberrant behavior.\n\\citet{drasgow1985} introduced $\\ell_z$, a standardized log-likelihood residual that aggregates per-item deviations into a single score.\n\\citet{snijders2001} corrected the variance of $\\ell_z$ for uncertainty in the estimated $\\hat{\\theta}$, yielding $\\ell_z^*$ with the property that $\\ell_z^* \\sim \\mathcal{N}(0,1)$ under the null hypothesis of model-consistent responding.\nNegative values indicate \\emph{aberrant} patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate \\emph{over-consistent} patterns (responses too predictable given the model).\nWe defer the formal definition to \\S\\ref{sec:framework}.\n\nIn psychometrics, person-fit statistics have a long history in detecting test fraud and item preknowledge.\n\\citet{karabatsos2003} compared 36 person-fit statistics and found $\\ell_z$ among the most powerful for detecting cheating.\n\\citet{sinharay2017} showed that $\\ell_z^*$ is particularly effective when the compromised item set is known, a setting analogous to benchmark contamination where the ``compromised'' items are those memorized during pretraining.\n\\citet{meijer2001} provide a comprehensive review of the broader person-fit literature.\nOur work transfers this psychometric toolkit to LLM evaluation, treating each model as an examinee whose response pattern may reveal memorization.\n\n\\subsection{Benchmark Contamination Detection}\\label{sec:contamination_related}\n\nContamination detection methods vary in what information they require from the model under test.\nTable~\\ref{tab:frontier} organizes the detection frontier by information access, from most to least demanding.\nAt the high end, corpus-search methods match benchmark items against pretraining data \\citep{dodge2021, magar2022}, but require full corpus access, which is unavailable for closed models.\nMembership inference attacks (MIA) use token-level log-probabilities to distinguish training examples from unseen ones \\citep{minkprob2024, deng2024}.\nGeneration-based probes elicit benchmark content via prompting \\citep{golchin2024, oren2024}.\nPerformance-based methods such as ConStat \\citep{constat2024} and CoDeC \\citep{codec2026} compare a model's accuracy on the target benchmark against accuracy on perturbed or reference sets, requiring either multiple evaluations or in-context learning passes.\n\\citet{sainz2023} propose overlapping-split analysis using time-stamped data.\n\nA critical limitation unites all log-probability methods: \\citet{wang2025fragility} demonstrate that reinforcement learning (RL) post-training renders MIA-based detectors (including Min-K\\%++) no better than random across 10 methods and 4 benchmarks.\nRL reshapes output distributions without altering which items a model answers correctly, so token-level statistics lose signal while binary correctness patterns are structurally preserved.\n\\citet{selfcritique2026} and \\citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.\n\nIRT-\\textsc{Fit} operates at the bottom of this frontier: it requires only binary responses (correct/incorrect), making it applicable to any model accessible through a standard evaluation API.\nRecent work applies IRT to LLM evaluation for ability estimation \\citep{martinezplumed2019, polo2024tinybenchmarks}, adaptive testing \\citep{atlas2025}, and benchmark diagnostics \\citep{psnirt2026}, but none use \\emph{person-fit} statistics for contamination detection.\nOur work bridges this gap.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 1,
        "newStart": 1,
        "newLines": 38,
        "lines": [
          "-% background",
          "+\\section{Background and Related Work}\\label{sec:background}",
          "+",
          "+\\subsection{IRT and Person-Fit Statistics}\\label{sec:irt_background}",
          "+",
          "+Item Response Theory (IRT) models the probability that an examinee answers a test item correctly as a function of the examinee's latent ability $\\theta$ and item-level parameters \\citep{lord1980, embretson2000}.",
          "+The four-parameter logistic (4PL) model, formalized in \\S\\ref{sec:framework} (Eq.~\\ref{eq:4pl}), extends the classical three-parameter model \\citep{birnbaum1968} with an upper asymptote $d$ that captures the probability of error even at high ability \\citep{barton1981}.",
          "+This parameter matters for LLMs: \\citet{psnirt2026} find that 46\\% of MMLU items have $d < 0.95$, meaning ceiling effects are pervasive and a model without the $d$ parameter systematically misestimates item characteristics.",
          "+",
          "+Given calibrated item parameters, person-fit statistics measure whether an examinee's \\emph{pattern} of correct and incorrect responses is consistent with the IRT model at the estimated ability level.",
          "+The key intuition is that a test-taker with ability $\\theta$ should get hard items wrong and easy items right at rates the model predicts; systematic deviations signal aberrant behavior.",
          "+\\citet{drasgow1985} introduced $\\ell_z$, a standardized log-likelihood residual that aggregates per-item deviations into a single score.",
          "+\\citet{snijders2001} corrected the variance of $\\ell_z$ for uncertainty in the estimated $\\hat{\\theta}$, yielding $\\ell_z^*$ with the property that $\\ell_z^* \\sim \\mathcal{N}(0,1)$ under the null hypothesis of model-consistent responding.",
          "+Negative values indicate \\emph{aberrant} patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate \\emph{over-consistent} patterns (responses too predictable given the model).",
          "+We defer the formal definition to \\S\\ref{sec:framework}.",
          "+",
          "+In psychometrics, person-fit statistics have a long history in detecting test fraud and item preknowledge.",
          "+\\citet{karabatsos2003} compared 36 person-fit statistics and found $\\ell_z$ among the most powerful for detecting cheating.",
          "+\\citet{sinharay2017} showed that $\\ell_z^*$ is particularly effective when the compromised item set is known, a setting analogous to benchmark contamination where the ``compromised'' items are those memorized during pretraining.",
          "+\\citet{meijer2001} provide a comprehensive review of the broader person-fit literature.",
          "+Our work transfers this psychometric toolkit to LLM evaluation, treating each model as an examinee whose response pattern may reveal memorization.",
          "+",
          "+\\subsection{Benchmark Contamination Detection}\\label{sec:contamination_related}",
          "+",
          "+Contamination detection methods vary in what information they require from the model under test.",
          "+Table~\\ref{tab:frontier} organizes the detection frontier by information access, from most to least demanding.",
          "+At the high end, corpus-search methods match benchmark items against pretraining data \\citep{dodge2021, magar2022}, but require full corpus access, which is unavailable for closed models.",
          "+Membership inference attacks (MIA) use token-level log-probabilities to distinguish training examples from unseen ones \\citep{minkprob2024, deng2024}.",
          "+Generation-based probes elicit benchmark content via prompting \\citep{golchin2024, oren2024}.",
          "+Performance-based methods such as ConStat \\citep{constat2024} and CoDeC \\citep{codec2026} compare a model's accuracy on the target benchmark against accuracy on perturbed or reference sets, requiring either multiple evaluations or in-context learning passes.",
          "+\\citet{sainz2023} propose overlapping-split analysis using time-stamped data.",
          "+",
          "+A critical limitation unites all log-probability methods: \\citet{wang2025fragility} demonstrate that reinforcement learning (RL) post-training renders MIA-based detectors (including Min-K\\%++) no better than random across 10 methods and 4 benchmarks.",
          "+RL reshapes output distributions without altering which items a model answers correctly, so token-level statistics lose signal while binary correctness patterns are structurally preserved.",
          "+\\citet{selfcritique2026} and \\citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.",
          "+",
          "+IRT-\\textsc{Fit} operates at the bottom of this frontier: it requires only binary responses (correct/incorrect), making it applicable to any model accessible through a standard evaluation API.",
          "+Recent work applies IRT to LLM evaluation for ability estimation \\citep{martinezplumed2019, polo2024tinybenchmarks}, adaptive testing \\citep{atlas2025}, and benchmark diagnostics \\citep{psnirt2026}, but none use \\emph{person-fit} statistics for contamination detection.",
          "+Our work bridges this gap."
        ]
      }
    ],
    "originalFile": "% background\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 35_

Let me verify the word count and check for style violations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "3480b67a-aa69-43b8-b4be-ca6337383bdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAmTZsdpbenHcN4mDkHevq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1606,
      "cache_read_input_tokens": 45999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1606
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01MbGVMGsbNwKVRTwQ8RqrnM`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections && cat background.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~$%&]//g; s/\\\\//g' | wc -w",
  "description": "Approximate word count of background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "7843b01e-1dd9-4fd2-a2d3-1219335d1414",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAmTZsdpbenHcN4mDkHevq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1606,
      "cache_read_input_tokens": 45999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1606
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

_source line 37 · 2026-05-20T23:00:09.665Z_

<details><summary>↩ Tool result · `toolu_01MbGVMGsbNwKVRTwQ8RqrnM`</summary>

```text
527
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "393c4595-459c-4b85-948f-a8b207aa56ae",
  "tool_use_result": {
    "stdout": "527",
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01V6ZfBJytM87RjP8Nh1s1ex`</summary>

```json
{
  "command": "grep -n \"—\\| – \\|delve\\|leverage\\|utilize\\|facilitate\\|myriad\\|plethora\\|realm of\\|worth noting\\|Notably,\" /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex || echo \"No style violations found\"",
  "description": "Check for AI writing style violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "f4df4f0d-139a-48d0-b3cb-751cf03e7966",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FAmTZsdpbenHcN4mDkHevq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1606,
      "cache_read_input_tokens": 45999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1606
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

_source line 39 · 2026-05-20T23:00:11.531Z_

<details><summary>↩ Tool result · `toolu_01V6ZfBJytM87RjP8Nh1s1ex`</summary>

```text
No style violations found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "748a1d3b-2861-43dc-b778-046021039458",
  "tool_use_result": {
    "stdout": "No style violations found",
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01WxJMVE83khG6ztTtEdRCKD`</summary>

```json
{
  "command": "detex background.tex 2>/dev/null | wc -w || (sed 's/\\\\cite[tp]*{[^}]*}//g; s/\\\\[a-zA-Z]*{//g; s/}//g; s/\\\\[a-zA-Z]*//g; s/[~$%&{}]//g; s/\\\\//g' background.tex | wc -w)",
  "description": "More accurate word count via detex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "11ce2380-7d3c-4817-bd66-c89c38c69382",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZjFTHXiR7sShWs4UQEF7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 47605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 41 · 2026-05-20T23:00:16.083Z_

<details><summary>↩ Tool result · `toolu_01WxJMVE83khG6ztTtEdRCKD`</summary>

```text
539
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "669f9d55-5cc7-4516-b7e1-3e977c67fac6",
  "tool_use_result": {
    "stdout": "539",
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

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
The word count is around 530-540 words after stripping LaTeX commands. But the actual rendered word count including citation names rendered as author names will push this closer to ~620-650. Let me do a more careful estimate. The LaTeX commands inflate/deflate the count. Citations like \citet{snijders2001} render as "Snijders (2001)" which is 2 words, but after stripping they become nothing. Let me count more carefully.

Actually, the task says ~650 words. Let me count the actual "rendered" word count. The stripped count of ~530 doesn't include the citation author names. 

With the citations rendering as author names and years, that's roughly 40-60 additional words across 20+ citations, bringing the total to around 580-600 words, which fits comfortably within the 650-word target for an 8-page paper. Now let me review the content to make sure it's substantive and complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "467730ab-ad62-43e4-8793-cd48c4f8578f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSJsRE9G3TRj7HrS3Cr8vh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 48007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 182
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

_source line 43_

~540 words stripped (rendered with citation names ~600-620). Within budget for an 8-page paper.

Section written to `paper/sections/background.tex`. Key features:
- **§2.1 IRT and Person-Fit**: Introduces 4PL conceptually without restating the equation (defers to §3/Eq.1), explains $d$ parameter importance with the 46% MMLU statistic, gives intuitive explanation of $\ell_z^*$ without formal definition, covers the psychometric cheating-detection lineage (Karabatsos, Sinharay, Meijer)
- **§2.2 Contamination Detection**: Organizes methods by information access referencing Table~\ref{tab:frontier}, covers all 5 method families, cites Wang et al. RL-robustness failure with the structural immunity argument, positions IRT-FIT at the minimum-access end, distinguishes from IRT-for-evaluation work (PSN-IRT, ATLAS, TinyBenchmarks)
- No em-dashes, no AI style markers, no equations duplicated from §3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "uuid": "d74085f5-ba2b-4df6-9bbc-86005d31eaa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSJsRE9G3TRj7HrS3Cr8vh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 48007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 182
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

_source line 44_

~540 words stripped (rendered with citation names ~600-620). Within budget for an 8-page paper.

Section written to `paper/sections/background.tex`. Key features:
- **§2.1 IRT and Person-Fit**: Introduces 4PL conceptually without restating the equation (defers to §3/Eq.1), explains $d$ parameter importance with the 46% MMLU statistic, gives intuitive explanation of $\ell_z^*$ without formal definition, covers the psychometric cheating-detection lineage (Karabatsos, Sinharay, Meijer)
- **§2.2 Contamination Detection**: Organizes methods by information access referencing Table~\ref{tab:frontier}, covers all 5 method families, cites Wang et al. RL-robustness failure with the structural immunity argument, positions IRT-FIT at the minimum-access end, distinguishes from IRT-for-evaluation work (PSN-IRT, ATLAS, TinyBenchmarks)
- No em-dashes, no AI style markers, no equations duplicated from §3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 98699,
  "duration_api_ms": 101406,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "7123220d-b12d-4bbe-9179-dceb18be05c9",
  "total_cost_usd": 0.4987634999999999,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 36348,
    "cache_read_input_tokens": 353851,
    "output_tokens": 3696,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36348,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 513,
        "cache_read_input_tokens": 48007,
        "cache_creation_input_tokens": 182,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 182
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2093,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002208,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 3696,
      "cacheReadInputTokens": 353851,
      "cacheCreationInputTokens": 36348,
      "webSearchRequests": 0,
      "costUSD": 0.4965554999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "866f3d1c-c870-4841-80b4-69722eaf7f5b"
}
```

</details>

---
