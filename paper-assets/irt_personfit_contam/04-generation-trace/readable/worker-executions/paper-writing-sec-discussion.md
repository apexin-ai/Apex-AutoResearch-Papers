# paper writing sec discussion

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_paper_writing_sec_discussion_20260520T233511.log`
- **Structured JSON:** [`b30d47fb2c260301693e.json`](../../sessions/b3/b30d47fb2c260301693e.json)

## Before a recorded user message

10 recorded events

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
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
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
  "uuid": "020d2b96-160d-4881-a50d-c356f7a35878",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-3-projects-irt-personfit-contam/memory/"
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
    "resetsAt": 1779337800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7b3577f1-4403-46b3-99a2-fd766640b6d6",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Assistant

_source line 4_

I'll read the required skill files first, then the current paper context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "a00daaf8-4270-4f20-ae38-74e9cc12601c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkJuxHMLZfAR1xBzHrnSEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12355,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12355
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

<details open><summary>🔧 Tool call — Read · `toolu_016UwyxKF41XSDHuwRX8TLGr`</summary>

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
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "68e9518e-e899-4eef-a8fe-02a2968cae5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkJuxHMLZfAR1xBzHrnSEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12355,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12355
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

_source line 6 · 2026-05-20T23:35:22.091Z_

<details><summary>↩ Tool result · `toolu_016UwyxKF41XSDHuwRX8TLGr`</summary>

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
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "e590751b-cee8-439a-941a-04c4c5e8306b",
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

<details open><summary>🔧 Tool call — Read · `toolu_01FJKJM9ASGSSq8dCvaJ8M3s`</summary>

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
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "db552a38-68ba-43cb-a23f-bdee51e1e6f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkJuxHMLZfAR1xBzHrnSEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12355,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12355
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

_source line 8 · 2026-05-20T23:35:22.632Z_

<details><summary>↩ Tool result · `toolu_01FJKJM9ASGSSq8dCvaJ8M3s`</summary>

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
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "0896268c-7d29-4625-8ff4-c77f2dab83ce",
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

<details open><summary>🔧 Tool call — Agent · `toolu_01LrxKqM2mUH9WAnrzDmjKHt`</summary>

```json
{
  "description": "Read paper context files",
  "subagent_type": "Explore",
  "prompt": "I need to understand the current state of a paper being written at /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/. \n\nPlease read these files if they exist:\n1. The main paper .tex file (look for main.tex or similar)\n2. sections/experiments.tex or sections/results.tex \n3. sections/introduction.tex\n4. sections/method.tex or sections/methodology.tex\n5. Any existing discussion.tex\n\nSearch breadth: medium. I need to understand the paper's narrative flow and notation conventions to write a Discussion section."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "dafb1309-e909-4d44-9654-d7a3d5c3504a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkJuxHMLZfAR1xBzHrnSEu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12355,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12355
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

### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Read paper context files",
  "task_type": "local_agent",
  "prompt": "I need to understand the current state of a paper being written at /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/. \n\nPlease read these files if they exist:\n1. The main paper .tex file (look for main.tex or similar)\n2. sections/experiments.tex or sections/results.tex \n3. sections/introduction.tex\n4. sections/method.tex or sections/methodology.tex\n5. Any existing discussion.tex\n\nSearch breadth: medium. I need to understand the paper's narrative flow and notation conventions to write a Discussion section.",
  "uuid": "cb5ff5d4-5e55-4331-82d0-9fa25ec7ddd9",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

## Round 1

67 recorded events

### User

_source line 11 · 2026-05-20T23:35:26.562Z_

I need to understand the current state of a paper being written at /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/. 

Please read these files if they exist:
1. The main paper .tex file (look for main.tex or similar)
2. sections/experiments.tex or sections/results.tex 
3. sections/introduction.tex
4. sections/method.tex or sections/methodology.tex
5. Any existing discussion.tex

Search breadth: medium. I need to understand the paper's narrative flow and notation conventions to write a Discussion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "f1d66930-d741-435b-b54a-f25652f22687"
}
```

</details>

---

### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Running Find all .tex files in the paper directory",
  "usage": {
    "total_tokens": 25417,
    "tool_uses": 1,
    "duration_ms": 1785
  },
  "last_tool_name": "Bash",
  "uuid": "4fd116ad-0e27-4420-9c19-2e5c1ac9b210",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01R7b2Zq1QxMG67LcNhsk7bN`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper -type f -name \"*.tex\" | head -20",
  "description": "Find all .tex files in the paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "8302536f-9fa7-4a12-9dde-fb098161bd9e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01We9uJWfs5b4VyEdGFb8Bb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25398,
        "ephemeral_1h_input_tokens": 0
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

_source line 14 · 2026-05-20T23:35:28.493Z_

<details><summary>↩ Tool result · `toolu_01R7b2Zq1QxMG67LcNhsk7bN`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "bb2d9926-9c34-4fd0-bc2a-51c72faacab0"
}
```

</details>

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Running List contents of paper directory",
  "usage": {
    "total_tokens": 25425,
    "tool_uses": 2,
    "duration_ms": 2090
  },
  "last_tool_name": "Bash",
  "uuid": "2f860424-e755-4c1c-ac83-8ea4bdc00950",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01N3uKtgdcZWLPJXwdSy3H3U`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/",
  "description": "List contents of paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "21322329-0928-46f5-af2c-f77e1bc0d93d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01We9uJWfs5b4VyEdGFb8Bb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25398,
        "ephemeral_1h_input_tokens": 0
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

_source line 17 · 2026-05-20T23:35:28.707Z_

<details><summary>↩ Tool result · `toolu_01N3uKtgdcZWLPJXwdSy3H3U`</summary>

```text
total 92
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 22:49 .
drwxr-xr-x 13 ubuntu ubuntu  4096 May 20 23:34 ..
-rw-r--r--  1 ubuntu ubuntu 11615 May 20 22:24 acl.sty
-rw-r--r--  1 ubuntu ubuntu 45186 May 20 22:24 acl_natbib.bst
-rw-r--r--  1 ubuntu ubuntu   884 May 20 22:24 main.tex
-rw-r--r--  1 ubuntu ubuntu 15106 May 20 22:49 references.bib
drwxr-xr-x  2 ubuntu ubuntu  4096 May 20 23:33 sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "001c12dc-1387-4f65-9504-7c382a704450"
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/main.tex",
  "usage": {
    "total_tokens": 27369,
    "tool_uses": 3,
    "duration_ms": 4178
  },
  "last_tool_name": "Read",
  "uuid": "4109aa1a-588c-44ee-9892-7753e021d606",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01JPwU5Bnr5mJiEXbAVYo72w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "25ea3d21-a80d-416e-af44-893d25651064",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
        "ephemeral_1h_input_tokens": 0
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

_source line 20 · 2026-05-20T23:35:30.752Z_

<details><summary>↩ Tool result · `toolu_01JPwU5Bnr5mJiEXbAVYo72w`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	
17	\graphicspath{{../figures/paper/}}
18	
19	\title{Detecting Benchmark Contamination in Large Language Models \\
20	via Item Response Theory Person-Fit Statistics}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	\input{sections/background}
33	\input{sections/method}
34	\input{sections/experiments}
35	\input{sections/discussion}
36	
37	\section*{Limitations}
38	\input{sections/limitations}
39	
40	\bibliography{references}
41	
42	\appendix
43	\input{sections/appendix}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "b8a58de0-cc94-45bd-93fa-988c64071869"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/introduction.tex",
  "usage": {
    "total_tokens": 27372,
    "tool_uses": 4,
    "duration_ms": 4415
  },
  "last_tool_name": "Read",
  "uuid": "dc407608-2c5c-4e0e-b3cf-a861c5a1b54f",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01QVEWaPyPgzDeABNm2Tuq5H`</summary>

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
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "1de4b3d9-c4c9-40ba-8a77-f167122f87e6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
        "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-20T23:35:30.984Z_

<details><summary>↩ Tool result · `toolu_01QVEWaPyPgzDeABNm2Tuq5H`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally: any model trained on broad web-crawled data may have encountered evaluation items during pretraining or fine-tuning \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus itself \citep{dodge2021, magar2022}.
9	Membership inference approaches such as Min-K\%++ require token-level probabilities \citep{minkprob2024, deng2024}.
10	Time Travel probing relies on crafted prompts that elicit memorized completions \citep{golchin2024, oren2024}.
11	Performance-based methods compare results across original and rephrased test variants \citep{constat2024}, and in-context learning approaches require output logits \citep{codec2026}.
12	These methods form a detection frontier ordered by information access: training data, model weights, logits, token probabilities, rephrased retests, and finally binary patterns.
13	No existing method operates at the bottom of this frontier.
14	We ask: \emph{what can be detected from binary response patterns alone?}
15	
16	The need for minimal-information detection grows more pressing as models evolve.
17	\citet{wang2025fragility} show that all ten log-probability-based detection methods they evaluate perform at chance level on reasoning models trained with reinforcement learning (RL).
18	RL fine-tuning reshapes internal token distributions while preserving the same correct/incorrect outcomes, and probability-based detectors cannot distinguish contaminated from clean models under these conditions.
19	Binary response patterns are structurally invariant to such distributional changes, as they record what a model answered rather than how its internal distributions shifted (empirical verification on post-RL models remains future work).
20	
21	We observe that a contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce anomalous response patterns in which difficult items are answered correctly through memorization rather than genuine ability.
22	This connection points to a mature body of work in psychometrics.
23	Person-fit statistics, developed over four decades for cheating detection in educational testing \citep{drasgow1985, meijer2001, karabatsos2003, sinharay2017}, quantify exactly this type of response aberrance.
24	The standardized statistic $\ell_z^*$ \citep{snijders2001} measures how well an individual's response pattern conforms to Item Response Theory (IRT) model predictions, with extreme negative values indicating patterns consistent with preknowledge.
25	Despite this natural correspondence, to our knowledge no prior work has applied person-fit statistics to LLM benchmark contamination detection.
26	
27	We introduce IRT-FIT, a framework that applies IRT person-fit analysis at the minimal-information operating point, requiring only binary responses and pre-calibrated item parameters \citep{psnirt2026}.
28	We compute $\ell_z^*$ for each (model, benchmark) pair and define $\Delta\ell_z^*$ as a difference-in-differences estimator for within-model contamination detection.
29	In controlled experiments (QLoRA fine-tuning on MMLU), 15\% contamination produces $|\text{Cohen's } d| = 3.58$ ($n{=}3$ clean seeds).
30	Our closed-form power function relates benchmark size to detection sensitivity ($R^2 = 0.957$), and shows that 80\% power at 15\% contamination requires $n \geq 7{,}958$ items.
31	A 4PL versus 3PL ablation reveals a mean $+27.3$ percentage-point power gain on MMLU \citep{hendrycks2021mmlu}, confirming that the upper-asymptote parameter is essential for LLM evaluation contexts.
32	Across 12 models and 5 benchmarks, $\ell_z^*$ flags 57 of 60 model-benchmark cells for response-pattern anomalies (BH-FDR $\alpha{=}0.05$), versus only 4 flagged by an accuracy $z$-score baseline.
33	This $14\times$ gap shows that $\ell_z^*$ captures response-pattern structure lost in aggregate accuracy.
34	We further identify a $\theta$-shift boundary condition: re-estimating ability on contaminated data can degrade sensitivity (non-monotonic dose-response under free $\theta$), but fixing $\theta$ to pre-contamination values restores monotonicity (signal ratio 3.12).
35	
36	Our contributions are:
37	\begin{enumerate}[leftmargin=*,nosep]
38	\item We propose IRT-FIT, a person-fit framework for contamination detection at the minimal-information operating point (binary responses only), validated through controlled contamination ($|\text{Cohen's } d| = 3.58$ at 15\% contamination).
39	\item We derive a closed-form power function ($R^2 = 0.957$) linking benchmark size to detection sensitivity, identify the $\theta$-shift boundary condition, and show that 4PL parameterization yields $+27.3$pp power gain over 3PL.
40	\item We report three empirical findings from real LLM response data: universal 4PL model misfit (57/60 cells flagged), the inadequacy of accuracy-based anomaly detection (4/60 cells), and a simulation-to-reality gap that motivates the $\Delta\ell_z^*$ design.
41	\end{enumerate}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "7065cd4c-9a11-468f-983b-32ac84bb532f"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/method.tex",
  "usage": {
    "total_tokens": 27375,
    "tool_uses": 5,
    "duration_ms": 4621
  },
  "last_tool_name": "Read",
  "uuid": "10ecaeee-0b13-48e6-86c1-14cb3209b26b",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_013s1D4vHvyksKUHimL2EK9o`</summary>

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
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "6d8fc7c5-7828-4bd9-a2a6-e7dcf4a15100",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
        "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-20T23:35:31.190Z_

<details><summary>↩ Tool result · `toolu_013s1D4vHvyksKUHimL2EK9o`</summary>

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
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "3a0793fa-99de-4dd0-bc52-08ed54eb2c61"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/experiments.tex",
  "usage": {
    "total_tokens": 27378,
    "tool_uses": 6,
    "duration_ms": 5046
  },
  "last_tool_name": "Read",
  "uuid": "ecdcac39-1540-4c73-a4e0-4742cd6bed08",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01FvynubPf8pbfYqQfDiLyM3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "1ab4c0ca-aff6-4302-96fd-55c21d3ce4cc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
        "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-20T23:35:31.615Z_

<details><summary>↩ Tool result · `toolu_01FvynubPf8pbfYqQfDiLyM3`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\input{sections/sec_setup}
5	\input{sections/sec_simulation}
6	\input{sections/sec_ctrl_contam}
7	\input{sections/sec_empirical}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "fd658f81-14f8-4838-a45b-70ea42c7878f"
}
```

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/discussion.tex",
  "usage": {
    "total_tokens": 27381,
    "tool_uses": 7,
    "duration_ms": 5131
  },
  "last_tool_name": "Read",
  "uuid": "953fea68-ada7-4947-a775-b13fc61537b0",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01GN24vUR3AzhCk4MyKrcbCx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "2739943a-3e9d-45e4-81f8-1e882289e7ac",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU2DMEDWTfaHsmm9UH9yc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 25398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
        "ephemeral_1h_input_tokens": 0
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

_source line 32 · 2026-05-20T23:35:31.718Z_

<details><summary>↩ Tool result · `toolu_01GN24vUR3AzhCk4MyKrcbCx`</summary>

```text
1	% discussion
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "da944f7c-2f37-4f40-85c4-565cc5539cd5"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/background.tex",
  "usage": {
    "total_tokens": 32208,
    "tool_uses": 8,
    "duration_ms": 7672
  },
  "last_tool_name": "Read",
  "uuid": "7aa18d96-f532-460b-9021-709ff80167fc",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01HMHsHWm6t4fpYxkAridanD`</summary>

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
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "3b6221e6-67d4-4c40-9023-5c28be20ac8d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4825,
        "ephemeral_1h_input_tokens": 0
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

_source line 35 · 2026-05-20T23:35:34.250Z_

<details><summary>↩ Tool result · `toolu_01HMHsHWm6t4fpYxkAridanD`</summary>

```text
1	\section{Background and Related Work}\label{sec:background}
2	
3	\subsection{IRT and Person-Fit Statistics}\label{sec:irt_background}
4	
5	Item Response Theory (IRT) models the probability that an examinee answers a test item correctly as a function of the examinee's latent ability $\theta$ and item-level parameters \citep{lord1980, embretson2000}.
6	The four-parameter logistic (4PL) model, formalized in \S\ref{sec:framework} (Eq.~\ref{eq:4pl}), extends the classical three-parameter model \citep{birnbaum1968} with an upper asymptote $d$ that captures the probability of error even at high ability \citep{barton1981}.
7	This parameter matters for LLMs: \citet{psnirt2026} find that 46\% of MMLU items have $d < 0.95$, meaning ceiling effects are pervasive and a model without the $d$ parameter systematically misestimates item characteristics.
8	
9	Given calibrated item parameters, person-fit statistics measure whether an examinee's \emph{pattern} of correct and incorrect responses is consistent with the IRT model at the estimated ability level.
10	The key intuition is that a test-taker with ability $\theta$ should get hard items wrong and easy items right at rates the model predicts; systematic deviations signal aberrant behavior.
11	\citet{drasgow1985} introduced $\ell_z$, a standardized log-likelihood residual that aggregates per-item deviations into a single score.
12	\citet{snijders2001} corrected the variance of $\ell_z$ for uncertainty in the estimated $\hat{\theta}$, yielding $\ell_z^*$ with the property that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null hypothesis of model-consistent responding.
13	Negative values indicate \emph{aberrant} patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate \emph{over-consistent} patterns (responses too predictable given the model).
14	We defer the formal definition to \S\ref{sec:framework}.
15	
16	In psychometrics, person-fit statistics have a long history in detecting test fraud and item preknowledge.
17	\citet{karabatsos2003} compared 36 person-fit statistics and found $\ell_z$ among the most powerful for detecting cheating.
18	\citet{sinharay2017} showed that $\ell_z^*$ is particularly effective when the compromised item set is known, a setting analogous to benchmark contamination where the ``compromised'' items are those memorized during pretraining.
19	\citet{meijer2001} provide a comprehensive review of the broader person-fit literature.
20	Our work transfers this psychometric toolkit to LLM evaluation, treating each model as an examinee whose response pattern may reveal memorization.
21	
22	\subsection{Benchmark Contamination Detection}\label{sec:contamination_related}
23	
24	Contamination detection methods vary in what information they require from the model under test.
25	Table~\ref{tab:frontier} organizes the detection frontier by information access, from most to least demanding.
26	At the high end, corpus-search methods match benchmark items against pretraining data \citep{dodge2021, magar2022}, but require full corpus access, which is unavailable for closed models.
27	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training examples from unseen ones \citep{minkprob2024, deng2024}.
28	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, oren2024}.
29	Performance-based methods such as ConStat \citep{constat2024} and CoDeC \citep{codec2026} compare a model's accuracy on the target benchmark against accuracy on perturbed or reference sets, requiring either multiple evaluations or in-context learning passes.
30	\citet{sainz2023} propose overlapping-split analysis using time-stamped data.
31	
32	A critical limitation unites all log-probability methods: \citet{wang2025fragility} demonstrate that reinforcement learning (RL) post-training renders MIA-based detectors (including Min-K\%++) no better than random across 10 methods and 4 benchmarks.
33	RL reshapes output distributions without altering which items a model answers correctly, so token-level statistics lose signal while binary correctness patterns are structurally preserved.
34	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
35	
36	IRT-\textsc{Fit} operates at the bottom of this frontier: it requires only binary responses (correct/incorrect), making it applicable to any model accessible through a standard evaluation API.
37	Recent work applies IRT to LLM evaluation for ability estimation \citep{martinezplumed2019, polo2024tinybenchmarks}, adaptive testing \citep{atlas2025}, and benchmark diagnostics \citep{psnirt2026}, but none use \emph{person-fit} statistics for contamination detection.
38	Our work bridges this gap.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "2c1b1933-3b02-4637-aba3-6a36a7635c71"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/sec_setup.tex",
  "usage": {
    "total_tokens": 32209,
    "tool_uses": 9,
    "duration_ms": 7819
  },
  "last_tool_name": "Read",
  "uuid": "69b59d4b-1228-41b2-b0cc-602b87ac97ec",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_017x1K4RZYrLNhYLfqSjuLgc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "3387b4b2-647a-4eef-a9ba-c65bb03bc95a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4825,
        "ephemeral_1h_input_tokens": 0
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

_source line 38 · 2026-05-20T23:35:34.387Z_

<details><summary>↩ Tool result · `toolu_017x1K4RZYrLNhYLfqSjuLgc`</summary>

```text
1	\subsection{Experimental Setup}
2	\label{sec:setup}
3	
4	We evaluate on five benchmarks that span knowledge, reasoning, and code generation: MMLU \citep{hendrycks2021mmlu} (14,042 items), HellaSwag \citep{zellers2019hellaswag} (10,042), GSM8K \citep{cobbe2021gsm8k} (1,319), ARC-Challenge \citep{clark2018arc} (295), and HumanEval \citep{chen2021humaneval} (164).
5	All item parameters follow the four-parameter logistic (4PL) IRT model, calibrated by \citet{psnirt2026} from a large-scale leaderboard dataset.
6	
7	\paragraph{Empirical data.}
8	We obtain per-item binary response vectors for 12 models from the PSN-IRT v2 leaderboard dataset \citep{psnirt2026}, covering open-weight and proprietary models across capability tiers.
9	
10	\paragraph{Controlled contamination.}
11	We fine-tune Qwen2.5-7B-Instruct with QLoRA (rank\,=\,16, $\alpha$\,=\,32) under five conditions: three clean runs (seeds 42, 123, 456) and two contaminated runs where 15\% and 50\% of MMLU evaluation items are included in the supervised fine-tuning (SFT) training data.
12	
13	\paragraph{Simulation.}
14	For each benchmark, we generate 2{,}000 response-vector replicates per condition across 11 contamination levels (0\%, 3\%, 5\%, 10\%, 15\%, 25\%, 50\%, 60\%, 75\%, 90\%, 100\%), sampling responses under the calibrated 4PL parameters.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "a42994cd-73aa-4f27-8848-752444897caf"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/sec_ctrl_contam.tex",
  "usage": {
    "total_tokens": 32210,
    "tool_uses": 10,
    "duration_ms": 8023
  },
  "last_tool_name": "Read",
  "uuid": "e554950f-4a1e-40ae-89cf-a7e204b14151",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01XFKYD3o7j7KdLavqVs7PPo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_ctrl_contam.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "8aa96b73-a55b-48d1-9735-cd8e79519e3c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4825,
        "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-20T23:35:34.595Z_

<details><summary>↩ Tool result · `toolu_01XFKYD3o7j7KdLavqVs7PPo`</summary>

```text
1	\subsection{Controlled Contamination}
2	\label{sec:ctrl_contam}
3	
4	We validate $\ell_z^*$ on MMLU with ground-truth contamination.
5	Three clean seeds yield $\ell_z^*$ values of $s_1{=}8.01$, $s_2{=}5.94$, $s_3{=}8.08$ (mean$\,{=}\,7.35\pm1.21$); $s_2$ is ${\sim}26\%$ lower than $s_1$/$s_3$, attributable to seed-specific training dynamics (Appendix~\ref{app:seed_sensitivity}).
6	All five conditions achieve comparable accuracy on uncontaminated items (clean $\approx$ 0.679), while contaminated models show overall accuracy gains (0.731 at 15\%, 0.764 at 50\%).
7	
8	\paragraph{Finding 1: Detection signal.}
9	Both contamination levels produce $\ell_z^*$ shifts far exceeding clean-seed variability.
10	At 15\% contamination, $|\text{Cohen's}\;d|{=}3.58$; at 50\%, $|d|{=}1.56$ (ddof$\,{=}\,1$, $n{=}3$ clean seeds).
11	The contamination signal exceeds the clean-clean $\Delta\ell_z^*$ noise floor (0.70) by a factor of 6.2$\times$.
12	
13	\paragraph{Finding 2: Free-$\theta$ non-monotonicity.}
14	Under free-$\theta$ estimation, dose-response is non-monotonic: $\Delta\ell_z^*{=}{-}4.34$ at 15\% versus ${-}1.90$ at 50\%.
15	The 50\% condition produces a \emph{weaker} signal than 15\% because contamination inflates $\hat{\theta}_{\text{MLE}}$, which absorbs part of the aberrance into a higher ability estimate ($\Delta\theta{=}0.29$ at 15\%, $0.47$ at 50\%).
16	
17	\paragraph{Finding 3: Fixed $\theta$ restores monotonicity.}
18	Anchoring at the pre-contamination baseline ($\theta_{\text{fixed}}{=}{-}0.0966$, mean of $n{=}3$ clean $\hat{\theta}$ estimates) restores monotonic dose-response: $\Delta\ell_{z,\text{fixed}}^*{=}2.68$ (15\%) and $8.36$ (50\%), a ratio of 3.12 (Figure~\ref{fig:ctrl_contam}, right panel).
19	
20	\paragraph{Finding 4: Memorization fingerprint.}
21	Splitting by seen/unseen items reveals a characteristic fingerprint: at 15\% contamination, memorized items yield $\ell_z^*{\approx}0$ (consistent with the model's inflated $\hat{\theta}$), while unseen items produce $\ell_z^*{=}3.1$, evidence of genuine aberrance on the non-memorized portion.
22	
23	\paragraph{Finding 5: Memorization fraction.}
24	The fraction of contaminated items that the model memorizes is 0.38 (15\%) and 0.29 (50\%).
25	SFT generalizes beyond the memorized items, as fewer than half the injected items show rote recall.
26	
27	\begin{figure*}[t]
28	  \centering
29	  \includegraphics[width=\textwidth]{fig_3_ctrl_contam.pdf}
30	  \caption{Controlled contamination on MMLU. \textbf{(a)} $\ell_z^*$ under free-$\theta$ and fixed-$\theta$ estimation for five conditions (3 clean seeds, 2 contaminated). Free-$\theta$ is non-monotonic; fixed-$\theta$ restores monotonicity. \textbf{(b)} Accuracy split by seen/unseen items with memorization fractions. \textbf{(c)} $\theta$-shift mechanism: contamination inflates $\hat{\theta}_{\text{MLE}}$, absorbing aberrance signal. $\theta_{\text{fixed}}$ computed as mean of $n{=}3$ clean seed $\hat{\theta}$ estimates ($-0.0966$).}
31	  \label{fig:ctrl_contam}
32	\end{figure*}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "23b1f739-ae9c-4046-94fd-d3b3980b644b"
}
```

</details>

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/sec_empirical.tex",
  "usage": {
    "total_tokens": 32211,
    "tool_uses": 11,
    "duration_ms": 8228
  },
  "last_tool_name": "Read",
  "uuid": "a1990024-a226-4fa4-b872-68483e9802a6",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01Ef7nks2ffZnWtpDXZQJN1E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_empirical.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "c79e8b7a-91eb-4507-97ce-4c8b57820782",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvLw4tnhmaViRfH1V9dtVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4825,
      "cache_read_input_tokens": 27332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4825,
        "ephemeral_1h_input_tokens": 0
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

_source line 44 · 2026-05-20T23:35:34.796Z_

<details><summary>↩ Tool result · `toolu_01Ef7nks2ffZnWtpDXZQJN1E`</summary>

```text
1	\subsection{Empirical Findings}
2	\label{sec:empirical}
3	
4	We apply $\ell_z^*$ to 12 models across five benchmarks (60 model-benchmark cells).
5	After Benjamini--Hochberg FDR correction ($\alpha=0.05$), 57 of 60 cells are flagged as significant.
6	The three unflagged cells (Yi-Lightning$\times$ARC-C, 360GPT2-Pro$\times$HumanEval, Yi-Lightning$\times$HumanEval) all involve small benchmarks ($n \leq 295$), consistent with the power analysis in \S\ref{sec:simulation}.
7	By contrast, an accuracy $z$-score baseline flags only 4 of 60 cells: $\ell_z^*$ captures 14$\times$ more anomalies by exploiting response-pattern structure that accuracy aggregation discards.
8	This near-universal misfit indicates that real LLM response patterns systematically deviate from 4PL IRT predictions, regardless of architecture or training paradigm.
9	
10	\paragraph{12-model case study.}
11	Figure~\ref{fig:heatmap} presents the $\ell_z^*$ heatmap across 12 models and five benchmarks.
12	93.3\% of flagged cells exhibit positive $\ell_z^*$ (over-consistency): models answer too many hard items correctly relative to their estimated ability.
13	Gemini-1.5-Flash on MMLU represents an extreme case: 100\% accuracy (14{,}042/14{,}042 items correct), $\hat{\theta}=0.78$, and $\ell_z^*{=}{+}34.75$, with 50 of 57 MMLU subjects flagged individually.
14	Ward hierarchical clustering on the $\ell_z^*$ profile matrix reveals heterogeneous contamination typologies; Gemini-1.5-Flash isolates as a distinct outlier, while other models form clusters that correspond to selective versus uniform misfit.
15	Ten of 12 models are flagged on all five benchmarks simultaneously.
16	
17	\paragraph{IRT parameter estimation gap.}
18	Refitting 3PL parameters via MML-EM on the v1 leaderboard ($N{=}178$ models) recovers difficulty moderately ($r_b = 0.663$) but fails on discrimination ($r_a = 0.127$).
19	Classical IRT calibration requires sample sizes that current leaderboards cannot provide; neural calibration methods such as PSN-IRT \citep{psnirt2026} remain essential.
20	Comparing 4PL and 3PL $\ell_z^*$ on real data yields $r=0.225$ and RMSE$\,{=}\,68.41$, a confirmation that the guessing-slip parameters ($c$, $d$) captured by 4PL substantially alter person-fit assessment.
21	This simulation-to-reality gap constitutes an informative negative result: it quantifies the boundary conditions under which classical IRT calibration degrades.
22	
23	\begin{figure}[t]
24	  \centering
25	  \includegraphics[width=\columnwidth]{fig_4_model_heatmap.pdf}
26	  \caption{$\ell_z^*$ heatmap for 12 models across five benchmarks. Positive values (red) indicate over-consistent response patterns. Gemini-1.5-Flash on MMLU ($\ell_z^*{=}{+}34.75$) is an extreme outlier. Ward clustering (left dendrogram) reveals distinct contamination typologies.}
27	  \label{fig:heatmap}
28	\end{figure}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "6311c89e-ddcd-4618-99a9-bd7505770a4d"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/abstract.tex",
  "usage": {
    "total_tokens": 36552,
    "tool_uses": 12,
    "duration_ms": 10310
  },
  "last_tool_name": "Read",
  "uuid": "b4053258-0320-4480-a8e8-c73247c57ac6",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01Thk2YPb4fxAauogPmodUPD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "5acf30ac-bc95-49c8-81f4-2ed50ebddc77",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4335,
        "ephemeral_1h_input_tokens": 0
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

_source line 47 · 2026-05-20T23:35:36.884Z_

<details><summary>↩ Tool result · `toolu_01Thk2YPb4fxAauogPmodUPD`</summary>

```text
1	% abstract
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "3ff8a37c-60ab-41a1-bd53-b26f8b467136"
}
```

</details>

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/limitations.tex",
  "usage": {
    "total_tokens": 36555,
    "tool_uses": 13,
    "duration_ms": 10518
  },
  "last_tool_name": "Read",
  "uuid": "ad8ab406-97ab-496c-9f7d-559c1f04a934",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01HEMC6iBrE7KCUNS5VqwdbY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "663c71bc-fc80-4482-a36e-ea0f61060154",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4335,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-20T23:35:37.085Z_

<details><summary>↩ Tool result · `toolu_01HEMC6iBrE7KCUNS5VqwdbY`</summary>

```text
1	% limitations
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "9611c4b7-5418-40b1-afe4-e81b3b903dd4"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/conclusion.tex",
  "usage": {
    "total_tokens": 36558,
    "tool_uses": 14,
    "duration_ms": 10732
  },
  "last_tool_name": "Read",
  "uuid": "4db009fe-d740-4813-9194-ed6b6d6a08c2",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01EA3W6WSkxgLMVZq2yG1JEd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "45876a2c-66e0-4bf9-bf39-cc88b6f73d24",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4335,
        "ephemeral_1h_input_tokens": 0
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

_source line 53 · 2026-05-20T23:35:37.300Z_

<details><summary>↩ Tool result · `toolu_01EA3W6WSkxgLMVZq2yG1JEd`</summary>

```text
1	% conclusion
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "74447d5a-f772-4f24-ab27-f7c42c2a0cc0"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper/sections/sec_simulation.tex",
  "usage": {
    "total_tokens": 36561,
    "tool_uses": 15,
    "duration_ms": 11023
  },
  "last_tool_name": "Read",
  "uuid": "0d788998-4f1a-4371-a8fd-2555f547596f",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_015f3j9kER1VC2KSqdAnjJiy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/sec_simulation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "7550d5ef-53fc-4cb8-9e8e-615d1f013cfe",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZnmYBPMaBmwafUu33XUya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4335,
      "cache_read_input_tokens": 32157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4335,
        "ephemeral_1h_input_tokens": 0
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

_source line 56 · 2026-05-20T23:35:37.591Z_

<details><summary>↩ Tool result · `toolu_015f3j9kER1VC2KSqdAnjJiy`</summary>

```text
1	\subsection{Simulation Validation}
2	\label{sec:simulation}
3	
4	\paragraph{Null calibration.}
5	Under the null (no contamination), bootstrap $lz^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
6	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
7	$lz^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
8	
9	\begin{figure}[t]
10	  \centering
11	  \includegraphics[width=\columnwidth]{fig_2_power_function.pdf}
12	  \caption{Theoretical (solid) and simulated (markers) two-sided detection power across contamination levels for five benchmarks. Power scales with $\sqrt{n}$. At contamination above 50\%, mean $lz^*$ crosses zero and shifts from negative to positive anomaly, which produces a brief power dip.}
13	  \label{fig:power}
14	\end{figure}
15	
16	\paragraph{Detection power.}
17	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels (93.6\% at 75\%, 95.2\% at 90\%, 100\% at full contamination).
18	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
19	Figure~\ref{fig:power} overlays theoretical and simulated power curves; the closed-form power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution with the \citet{snijders2001} variance formula, achieves $R^2 = 0.9572$.
20	Practitioners can determine detection feasibility from a benchmark's item count alone.
21	
22	\paragraph{Model comparison.}
23	The 4PL model yields a mean $+$27.3pp power gain over 3PL on MMLU, $+$26.1pp on HellaSwag, and $+$20.3pp on GSM8K, as 46\% of MMLU items exhibit upper asymptote $d < 0.95$ (Appendix~\ref{app:4pl_ablation}).
24	Against supervised baselines, $lz^*$ outperforms logistic regression and random forest at low contamination ($+$0.10 AUROC at 5\%, $+$0.05 at 10\%) without training data; ML classifiers surpass $lz^*$ only above 25\% contamination.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "5e6b7d86-3075-459d-bb02-99533e845da1"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Running Find provenance and writing plan files",
  "usage": {
    "total_tokens": 37832,
    "tool_uses": 16,
    "duration_ms": 12972
  },
  "last_tool_name": "Bash",
  "uuid": "cb3648db-6743-4bdd-86f2-df775c68184b",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01EE8gNWKFqehY2A2FGaSxUs`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam -name \"paper_provenance.yaml\" -o -name \"writing_plan.yaml\" 2>/dev/null",
  "description": "Find provenance and writing plan files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "b621d381-3fce-4121-87dc-8dcb43e9191d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Biexiwndvuz1fzmsxWraej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 36492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
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

_source line 59 · 2026-05-20T23:35:39.765Z_

<details><summary>↩ Tool result · `toolu_01EE8gNWKFqehY2A2FGaSxUs`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_provenance.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "eb02b151-4f9f-42b4-96f5-089f720d1173"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading paper_provenance.yaml",
  "usage": {
    "total_tokens": 38120,
    "tool_uses": 17,
    "duration_ms": 14593
  },
  "last_tool_name": "Read",
  "uuid": "94a2a58c-c413-4fcc-bfb7-3df7004b79c9",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01BVgWsENnRwQKDb2kdz8PJ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_provenance.yaml",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "7b74013b-8914-419b-83d7-ccc63547c518",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018J1ZYgRq9inn7JpYcf6xaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 37761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 62 · 2026-05-20T23:35:41.162Z_

<details><summary>↩ Tool result · `toolu_01BVgWsENnRwQKDb2kdz8PJ5`</summary>

```text
1	paper:
2	  title: ''
3	  version: 11
4	  generated_at: '2026-05-20T23:34:38.275117+00:00'
5	claims:
6	- id: C001
7	  location:
8	    section: sec_setup
9	    paragraph: 0
10	    sentence: 0
11	  text: MMLU has 14,042 items, HellaSwag 10,042, GSM8K 1,319, ARC-Challenge 295, HumanEval
12	    164
13	  type: data
14	  evidence:
15	  - exp_id: phase_b_personfit
16	  - exp_id: exp-extended-sim
17	  decisions: []
18	  deprecated: false
19	- id: C003
20	  location:
21	    section: sec_setup
22	    paragraph: 0
23	    sentence: 0
24	  text: 4PL IRT parameters calibrated by PSN-IRT from large-scale leaderboard dataset
25	  type: method
26	  evidence:
27	  - exp_id: phase_b_personfit
28	    metric: item_params_source
29	  decisions: []
30	  deprecated: false
31	- id: C006
32	  location:
33	    section: sec_setup
34	    paragraph: 0
35	    sentence: 0
36	  text: 12 models from PSN-IRT v2 leaderboard dataset
37	  type: data
38	  evidence:
39	  - exp_id: phase_b_personfit
40	    metric: n_models=12
41	  decisions: []
42	  deprecated: false
43	- id: C010
44	  location:
45	    section: sec_setup
46	    paragraph: 0
47	    sentence: 0
48	  text: QLoRA rank=16 alpha=32 on Qwen2.5-7B-Instruct, 5 conditions (3 clean seeds
49	    + 2 contaminated)
50	  type: method
51	  evidence:
52	  - exp_id: exp-ctrl-contam-pilot
53	  decisions: []
54	  deprecated: false
55	- id: C015
56	  location:
57	    section: sec_setup
58	    paragraph: 0
59	    sentence: 0
60	  text: 2000 replicates per condition, 11 contamination levels
61	  type: method
62	  evidence:
63	  - exp_id: exp-extended-sim
64	    metric: n_sims=2000, levels=11
65	  decisions: []
66	  deprecated: false
67	- id: C016
68	  location:
69	    section: sec_simulation
70	    paragraph: 0
71	    sentence: 0
72	  text: 'Bootstrap lz* null: mean bias 0.041, std 1.003 on MMLU'
73	  type: quantitative
74	  evidence:
75	  - exp_id: exp-empirical-null
76	    metric: bias_by_benchmark.mmlu=0.041
77	  decisions: []
78	  deprecated: false
79	- id: C018
80	  location:
81	    section: sec_simulation
82	    paragraph: 0
83	    sentence: 0
84	  text: KS rejection rates by benchmark size
85	  type: quantitative
86	  evidence:
87	  - exp_id: exp-empirical-null
88	    metric: ks_reject_by_benchmark
89	  decisions: []
90	  deprecated: false
91	- id: C021
92	  location:
93	    section: sec_simulation
94	    paragraph: 0
95	    sentence: 0
96	  text: MMLU two-sided power 97.8% at 15%
97	  type: quantitative
98	  evidence:
99	  - exp_id: exp-extended-sim
100	    metric: mmlu_15pct=0.978
101	  decisions: []
102	  deprecated: false
103	- id: C025
104	  location:
105	    section: sec_simulation
106	    paragraph: 0
107	    sentence: 0
108	  text: Theory R2=0.9572
109	  type: quantitative
110	  evidence:
111	  - exp_id: exp-power-theory
112	    metric: R2_two_sided=0.9572
113	  decisions: []
114	  deprecated: false
115	- id: C030
116	  location:
117	    section: sec_simulation
118	    paragraph: 0
119	    sentence: 0
120	  text: 4PL vs 3PL mean +27.3pp MMLU
121	  type: quantitative
122	  evidence:
123	  - exp_id: exp-4pl-ablation
124	  decisions: []
125	  deprecated: false
126	- id: C036
127	  location:
128	    section: sec_simulation
129	    paragraph: 0
130	    sentence: 0
131	  text: lz* +0.10 AUROC at 5% vs ML
132	  type: quantitative
133	  evidence:
134	  - exp_id: exp-ml-classifier-baseline
135	  decisions: []
136	  deprecated: false
137	- id: C037
138	  location:
139	    section: sec_ctrl_contam
140	    paragraph: 0
141	    sentence: 0
142	  text: 'Clean seeds lz*: s1=8.01, s2=5.94, s3=8.08 (mean=7.35+/-1.21)'
143	  type: quantitative
144	  evidence:
145	  - exp_id: exp-ctrl-contam-pilot
146	    metric: clean_seeds, baseline_n3
147	  decisions: []
148	  deprecated: false
149	- id: C039
150	  location:
151	    section: sec_ctrl_contam
152	    paragraph: 0
153	    sentence: 0
154	  text: contam_15% |Cohen's d|=3.58, contam_50% |d|=1.56 (ddof=1, n=3)
155	  type: quantitative
156	  evidence:
157	  - exp_id: exp-ctrl-contam-pilot
158	    metric: cohens_d_n3
159	  decisions: []
160	  deprecated: false
161	- id: C042
162	  location:
163	    section: sec_ctrl_contam
164	    paragraph: 0
165	    sentence: 0
166	  text: Clean-clean noise floor 0.70, contam signal 5.7x above
167	  type: quantitative
168	  evidence:
169	  - exp_id: exp-clean-control-delta
170	    metric: clean_vs_clean_mean_abs
171	  decisions: []
172	  deprecated: false
173	- id: C046
174	  location:
175	    section: sec_ctrl_contam
176	    paragraph: 0
177	    sentence: 0
178	  text: 'Free-theta non-monotonic: Delta_lz=-4.34 (15%), -1.90 (50%)'
179	  type: quantitative
180	  evidence:
181	  - exp_id: exp-ctrl-contam-pilot
182	    metric: H3.theta_free
183	  decisions: []
184	  deprecated: false
185	- id: C051
186	  location:
187	    section: sec_ctrl_contam
188	    paragraph: 0
189	    sentence: 0
190	  text: 'Fixed-theta: 2.68 (15%), 8.36 (50%), ratio=3.12'
191	  type: quantitative
192	  evidence:
193	  - exp_id: exp-ctrl-contam-pilot
194	    metric: H3.theta_fixed
195	  decisions: []
196	  deprecated: false
197	- id: C057
198	  location:
199	    section: sec_ctrl_contam
200	    paragraph: 0
201	    sentence: 0
202	  text: 'Memorization fraction: 0.38 (15%), 0.29 (50%)'
203	  type: quantitative
204	  evidence:
205	  - exp_id: exp-ctrl-contam-pilot
206	    metric: H4_memorization_fraction
207	  decisions: []
208	  deprecated: false
209	- id: C058
210	  location:
211	    section: sec_empirical
212	    paragraph: 0
213	    sentence: 0
214	  text: 57/60 cells flagged after BH-FDR correction
215	  type: quantitative
216	  evidence:
217	  - exp_id: exp-fdr-correction
218	    metric: flagged_bh_fdr=57/60
219	  decisions: []
220	  deprecated: false
221	- id: C060
222	  location:
223	    section: sec_empirical
224	    paragraph: 0
225	    sentence: 0
226	  text: Accuracy z-score flags 4/60 vs lz* 57/60 (14x)
227	  type: quantitative
228	  evidence:
229	  - exp_id: exp-accuracy-zscore-baseline
230	    metric: z_flagged=4, lz_flagged=57
231	  decisions: []
232	  deprecated: false
233	- id: C063
234	  location:
235	    section: sec_empirical
236	    paragraph: 0
237	    sentence: 0
238	  text: 93.3% positive lz* cells
239	  type: quantitative
240	  evidence:
241	  - exp_id: exp-cross-benchmark-analysis
242	    metric: pct_positive_cells=93.3
243	  decisions: []
244	  deprecated: false
245	- id: C067
246	  location:
247	    section: sec_empirical
248	    paragraph: 0
249	    sentence: 0
250	  text: 'Gemini-1.5 MMLU: acc=100%, theta=0.78, lz*=+34.75'
251	  type: quantitative
252	  evidence:
253	  - exp_id: phase_b_personfit
254	    metric: gemini15_mmlu
255	  decisions: []
256	  deprecated: false
257	- id: C072
258	  location:
259	    section: sec_empirical
260	    paragraph: 0
261	    sentence: 0
262	  text: 50/57 MMLU subjects flagged for Gemini
263	  type: quantitative
264	  evidence:
265	  - exp_id: exp-domain-analysis
266	    metric: gemini_subjects_flagged=50/57
267	  decisions: []
268	  deprecated: false
269	- id: C078
270	  location:
271	    section: sec_empirical
272	    paragraph: 0
273	    sentence: 0
274	  text: 10/12 models flagged on all 5 benchmarks
275	  type: quantitative
276	  evidence:
277	  - exp_id: exp-cross-benchmark-analysis
278	    metric: n_models_all5_flagged=10
279	  decisions: []
280	  deprecated: false
281	- id: C085
282	  location:
283	    section: sec_empirical
284	    paragraph: 0
285	    sentence: 0
286	  text: 'MML-EM refit: b_r=0.663, a_r=0.127, N=178'
287	  type: quantitative
288	  evidence:
289	  - exp_id: exp-v1-irt-refit-expanded
290	  decisions: []
291	  deprecated: false
292	- id: C093
293	  location:
294	    section: sec_empirical
295	    paragraph: 0
296	    sentence: 0
297	  text: '4PL vs 3PL real data: r=0.225, RMSE=68.41'
298	  type: quantitative
299	  evidence:
300	  - exp_id: exp-4pl-real-data-degradation
301	    metric: correlation_4pl_vs_3pl
302	  decisions: []
303	  deprecated: false
304	- id: C094
305	  location:
306	    section: sec_ctrl_contam
307	    paragraph: 0
308	    sentence: 0
309	  text: Contamination signal exceeds noise floor by 6.2x
310	  type: quantitative
311	  evidence: []
312	  decisions: []
313	  deprecated: false
314	- id: C095
315	  location:
316	    section: sec_ctrl_contam
317	    paragraph: 0
318	    sentence: 0
319	  text: Δθ=0.29 at 15% contamination
320	  type: quantitative
321	  evidence: []
322	  decisions: []
323	  deprecated: false
324	- id: C096
325	  location:
326	    section: sec_method
327	    paragraph: 0
328	    sentence: 0
329	  text: '4PL IRT model: P_i(θ) = c_i + (d_i - c_i) sigmoid(a_i(θ - b_i))'
330	  type: definition
331	  evidence:
332	  - exp_id: exp_001
333	    metric: model_specification
334	  decisions: []
335	  deprecated: false
336	- id: C098
337	  location:
338	    section: sec_method
339	    paragraph: 0
340	    sentence: 0
341	  text: lz* ~ N(0,1) under null hypothesis (Snijders 2001 correction)
342	  type: theoretical
343	  evidence:
344	  - exp_id: exp_002
345	    metric: null_calibration
346	  decisions: []
347	  deprecated: false
348	- id: C101
349	  location:
350	    section: sec_method
351	    paragraph: 0
352	    sentence: 0
353	  text: Δlz* functions as difference-in-differences estimator cancelling shared IRT
354	    misfit bias
355	  type: methodological
356	  evidence:
357	  - exp_id: exp_002
358	    metric: bootstrap_null
359	  decisions: []
360	  deprecated: false
361	- id: C105
362	  location:
363	    section: sec_method
364	    paragraph: 0
365	    sentence: 0
366	  text: Noncentrality parameter δ ∝ √n
367	  type: theoretical
368	  evidence:
369	  - exp_id: exp_002
370	    metric: power_scaling
371	  decisions: []
372	  deprecated: false
373	- id: C110
374	  location:
375	    section: sec_method
376	    paragraph: 0
377	    sentence: 0
378	  text: Marginal power via Gauss-Hermite quadrature K=30
379	  type: theoretical
380	  evidence:
381	  - exp_id: exp_002
382	    metric: power_function
383	  decisions: []
384	  deprecated: false
385	- id: C116
386	  location:
387	    section: sec_method
388	    paragraph: 0
389	    sentence: 0
390	  text: lz* sign crossover at π* ≈ 81-85% across benchmarks
391	  type: quantitative
392	  evidence:
393	  - exp_id: exp_002
394	    metric: crossover_fraction
395	  decisions: []
396	  deprecated: false
397	- id: C123
398	  location:
399	    section: sec_method
400	    paragraph: 0
401	    sentence: 0
402	  text: 80% power at 15% contamination requires n ≥ 7,958 items
403	  type: quantitative
404	  evidence:
405	  - exp_id: exp_002
406	    metric: min_benchmark_size
407	  decisions: []
408	  deprecated: false
409	- id: C131
410	  location:
411	    section: sec_method
412	    paragraph: 0
413	    sentence: 0
414	  text: 'θ-shift mechanism: free-θ non-monotonic, fixed-θ monotonic'
415	  type: methodological
416	  evidence:
417	  - exp_id: exp_003
418	    metric: theta_shift
419	  decisions: []
420	  deprecated: false
421	- id: C140
422	  location:
423	    section: sec_method
424	    paragraph: 0
425	    sentence: 0
426	  text: Fixed-θ signal ratio 3.12 (50%/15%), free-θ inverted ratio 0.44
427	  type: quantitative
428	  evidence:
429	  - exp_id: exp_003
430	    metric: dose_response_ratio
431	  decisions: []
432	  deprecated: false
433	- id: C141
434	  location:
435	    section: sec_background
436	    paragraph: 0
437	    sentence: 0
438	  text: 46% of MMLU items have d < 0.95, ceiling effects pervasive
439	  type: quantitative
440	  evidence:
441	  - exp_id: exp_001
442	    metric: d_parameter_distribution
443	  decisions: []
444	  deprecated: false
445	- id: C143
446	  location:
447	    section: sec_background
448	    paragraph: 0
449	    sentence: 0
450	  text: lz* ~ N(0,1) under null (Snijders 2001)
451	  type: theoretical
452	  evidence:
453	  - exp_id: exp_002
454	    metric: null_calibration
455	  decisions: []
456	  deprecated: false
457	- id: C146
458	  location:
459	    section: sec_background
460	    paragraph: 0
461	    sentence: 0
462	  text: 'Wang et al: all 10 log-prob MIA methods no better than random on RL models'
463	  type: literature
464	  evidence:
465	  - exp_id: lit_wang2025
466	    metric: rl_robustness
467	  decisions: []
468	  deprecated: false
469	- id: C150
470	  location:
471	    section: sec_background
472	    paragraph: 0
473	    sentence: 0
474	  text: Binary correctness patterns structurally preserved under RL post-training
475	  type: theoretical
476	  evidence:
477	  - exp_id: lit_wang2025
478	    metric: structural_argument
479	  decisions: []
480	  deprecated: false
481	- id: C155
482	  location:
483	    section: sec_background
484	    paragraph: 0
485	    sentence: 0
486	  text: No prior work uses person-fit statistics for LLM contamination detection
487	  type: novelty
488	  evidence:
489	  - exp_id: lit_review
490	    metric: gap_analysis
491	  decisions: []
492	  deprecated: false
493	- id: C156
494	  location:
495	    section: sec_introduction
496	    paragraph: 0
497	    sentence: 0
498	  text: 15% contamination produces |Cohen's d| = 3.58 (n=3 clean seeds)
499	  type: quantitative
500	  evidence:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "8b81d656-7601-42a5-ac21-93a395936713"
}
```

</details>

---

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "description": "Reading writing_plan.yaml",
  "usage": {
    "total_tokens": 38165,
    "tool_uses": 18,
    "duration_ms": 14777
  },
  "last_tool_name": "Read",
  "uuid": "cbd67da4-8a09-439c-bc1c-0c2248c1ead7",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01RpRxc9JJy54CPxfdNUZyk3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "48060ead-6106-4dac-86c2-d2cbe509a6df",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018J1ZYgRq9inn7JpYcf6xaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 37761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 65 · 2026-05-20T23:35:41.708Z_

<details><summary>↩ Tool result · `toolu_01RpRxc9JJy54CPxfdNUZyk3`</summary>

```text
1	meta:
2	  title: "IRT-FIT: Detecting LLM Benchmark Contamination via Person-Fit Statistics at the Minimal-Information Operating Point"
3	  venue: EMNLP 2026 Main (ARR Jun 15 cycle)
4	  format: Long paper, 8-page main text + unlimited references
5	  template: acl2023  # ACL rolling review standard template; Worker 下载 https://github.com/acl-org/acl-style-files
6	  template_note: "EMNLP 2026 通过 ARR 统一审稿，使用 ACL 标准模板。若 2026 版模板已发布，Worker 应优先使用。"
7	  created_at: "2026-05-20T20:00:00Z"
8	  verify_refs: true
9	  director_approved_at: "2026-05-20T20:10:00Z"
10	  score_target: "3.0-3.25 (Findings / Borderline Conference)"
11	
12	# ============================================================
13	# DIRECTOR ACTION ITEMS (Dream 审稿 + Reviewer 复核定稿)
14	# ============================================================
15	action_items:
16	  critical:
17	    - id: AI-1
18	      desc: "4PL 参数来源：PSN-IRT (Lee et al., AAAI 2026)，不是 py-irt 或 ltm。lz* 由项目自实现 (numpy/scipy)"
19	      target_section: sec_method
20	      status: pending
21	
22	  method:
23	    - id: AI-6
24	      desc: "IRT 假设违反的显式讨论：≥1 段解释 lz* 在 local independence/unidimensionality 违反下的诊断价值。核心论点：Δlz* 作为 DiD 设计，系统性偏差在差分中被消除"
25	      target_section: sec_method
26	      status: pending
27	    - id: AI-7
28	      desc: "Δlz* 设计 + bootstrap null 校准：universal misfit 是 finding 不是 artifact，Δlz* bypasses absolute thresholds"
29	      target_section: sec_method
30	      status: pending
31	
32	  results:
33	    - id: AI-8
34	      desc: "Type-I error 专段：bootstrap null mean bias 0.041, std 1.003, KS reject rate 8.3%"
35	      target_section: sec_simulation
36	      status: pending
37	    - id: AI-9
38	      desc: "Clean-clean Δlz* baseline drift：n=3 seeds lz* 分布，0.70 noise floor，contam signal 5.7× above"
39	      target_section: sec_ctrl_contam
40	      status: pending
41	    - id: AI-10
42	      desc: "Binary-only baseline 对比：lz* 57/60 vs accuracy z-score 4/60 (14×)。模拟中 lz* ≥ ML classifiers at 5-10%"
43	      target_section: sec_empirical
44	      status: pending
45	
46	  discussion:
47	    - id: AI-11
48	      desc: "单模型 ctrl-contam 泛化性限制：仅 Qwen2.5-7B × MMLU。Future work: multi-family"
49	      target_section: sec_limitations
50	      status: pending
51	    - id: AI-12
52	      desc: "QLoRA low-rank bias：memorization ~38% 可能是 QLoRA lower bound，full FT 可能更强信号"
53	      target_section: sec_limitations
54	      status: pending
55	    - id: AI-13
56	      desc: "Post-RL 措辞约束：不写 'robust to post-RL'。写 'structurally invariant to RL distributional changes — empirical verification is future work'"
57	      target_section: [sec_introduction, sec_discussion]
58	      status: pending
59	
60	  urgent_corrections:
61	    - id: UC-1
62	      desc: "57/60 vs 4/60 是 universal misfit 证据 (Claim 3a)，不是 contamination detection 证据。用于论证 lz* 捕获 accuracy 聚合后丢失的 response-pattern 信息。Contamination detection 优势用: 模拟 AUROC +0.10@5%, ctrl-contam |d|=3.58, lz*≥ML classifiers at 5-10%"
63	      target_section: [sec_empirical, sec_simulation]
64	      status: pending
65	    - id: UC-2
66	      desc: "KS 校准率分层报告：MMLU 8.3%, HellaSwag 8.3% (well-calibrated); HumanEval 75%, ARC-C 58.3% (poorly calibrated); 总体 40% (24/60)。不能只引用 8.3%。按 benchmark size 分层 + 说明 large benchmarks well-calibrated"
67	      target_section: sec_simulation
68	      status: pending
69	    - id: UC-3
70	      desc: "QLoRA bias 框架为 'results may be conservative' 而非 limitation。rank=16 限制 memorization → 38% 是保守下界 → full FT 信号预期更强 → 强化结论。~50 词 Limitations"
71	      target_section: sec_limitations
72	      status: pending
73	
74	  missing_refs:
75	    - "Drasgow, Levine & Williams (1985) — person-fit foundations"
76	    - "Karabatsos (2003) — already in map, need verify"
77	    - "Meijer & Sijtsma (2001) — person-fit survey"
78	    - "Oren et al. (2024) — proving test set contamination"
79	    - "Polo et al. (2024) — tinyBenchmarks"
80	    - "Magar & Schwartz (2022) — data contamination"
81	    - "Deng et al. (2024) — contamination detection"
82	    - "Burnham et al. (2024) — IRT for AI"
83	    - "Jacobs et al. (2024) — psychometrics and AI"
84	
85	# ============================================================
86	# PAPER OUTLINE
87	# ============================================================
88	paper_outline:
89	  abstract:
90	    word_budget: 200
91	    dependencies: [sec_experiments, sec_method]
92	    key_elements:
93	      - problem statement (contamination + privileged access gap)
94	      - minimal-information operating point framing
95	      - "3 result highlights: (1) ctrl-contam |d|=3.58@15%, (2) power function R²=0.957, (3) universal misfit finding"
96	      - scope precision (SFT contamination, not pretraining exposure)
97	    constraints:
98	      - no "state-of-the-art" (no SOTA comparison done)
99	      - no "significantly" without statistical test
100	      - numbers must match sec_experiments exactly
101	
102	  sec_introduction:
103	    label: "Introduction"
104	    word_budget: 700
105	    dependencies: []
106	    subsections: []
107	    key_elements:
108	      - "P1: Problem — contamination threatens evaluation integrity, structural cause (training corpora ∩ public benchmarks)"
109	      - "P2: Existing methods critique — ALL require privileged access. Detection frontier ranking: binary < rephrased retest < token probs < logits < weights"
110	      - "P3: RL-robustness motivation — Wang et al. shows all 10 log-prob methods ≈ random on RL models. Binary patterns structurally immune to RL distributional shifts"
111	      - "P4: Cross-domain insight — contaminated LLM ≡ examinee with item preknowledge. Person-fit literature: decades of cheating detection. Gap: 0/N papers connect person-fit to LLM contamination"
112	      - "P5: Our approach — IRT-FIT at minimal-information operating point. Key results preview (numbers from experiments)"
113	      - "P6: 3 contributions (method+characterization+empirical findings), escalating scope"
114	    narrative_strategy:
115	      story_type: "跨界迁移型 (unused in 0/8 peer papers — our differentiator)"
116	      hook: "ConStat definitional pivot: 'All prior methods require privileged access. We ask: what can be detected from binary response patterns alone?'"
117	      techniques:
118	        - "Wang's negative-result-first: prove existing methods fail → create urgency"
119	        - "PSN-IRT's numbered findings for scannability"
120	
121	  sec_background:
122	    label: "Background and Related Work"
123	    word_budget: 650
124	    dependencies: []
125	    subsections:
126	      - id: sec_irt_background
127	        label: "IRT and Person-Fit Statistics"
128	        word_budget: 350
129	        key_elements:
130	          - "4PL model equation: P(X=1|θ) = c + (d-c)·sigmoid(a(θ-b))"
131	          - "d parameter importance for LLMs (ceiling effects, 46% MMLU items d<0.95)"
132	          - "lz* definition + N(0,1) null + interpretation (negative=aberrant, positive=over-consistent)"
133	          - "Snijders (2001) variance correction"
134	          - "Person-fit for cheating detection in psychometrics (Karabatsos 2003, Sinharay 2017)"
135	        constraints:
136	          - self-contained for ML reviewers unfamiliar with psychometrics
137	          - avoid jargon without definition
138	          - IRT 形式化定义（4PL 公式 + lz* 公式）保留正文，推导细节移至 Appendix
139	          - 正文只保留直觉解释 + 核心公式
140	
141	      - id: sec_contamination_related
142	        label: "Benchmark Contamination Detection"
143	        word_budget: 300
144	        key_elements:
145	          - "Detection frontier table reference (Table 1)"
146	          - "5 method families: time-based partition, MIA/Min-K%++, Time Travel, ConStat, CoDeC"
147	          - "Wang et al. RL-robustness failure"
148	          - "Position IRT-FIT at bottom of frontier (minimum information access)"
149	          - "IRT for LLM evaluation (PSN-IRT, ATLAS) — related but not person-fit"
150	
151	  sec_method:
152	    label: "Method"
153	    word_budget: 600
154	    dependencies: [sec_background]
155	    subsections:
156	      - id: sec_framework
157	        label: "IRT-FIT Framework"
158	        word_budget: 200
159	        key_elements:
160	          - "Input: binary response matrix X (models × items) + calibrated 4PL parameters"
161	          - "Step 1: θ estimation (MLE per benchmark)"
162	          - "Step 2: lz* computation per (model, benchmark) cell"
163	          - "Step 3: Δlz* for within-model contamination detection"
164	          - "Item parameter source: PSN-IRT calibrated 4PL (cite psnirt2026)"
165	          - "No training data needed — unsupervised, per-cell statistic"
166	
167	      - id: sec_power_characterization
168	        label: "Detection Power Characterization"
169	        word_budget: 220
170	        key_elements:
171	          - "Power as function of n_items and contamination level"
172	          - "Theoretical derivation from Snijders (2001) variance formula: δ ∝ √n"
173	          - "Two-sided detection: partial contamination → aberrant (lz*<<0), full → over-consistent (lz*>>0)"
174	          - "Crossover point at ~81-85% contamination"
175	          - "Upper bound vs adjusted power (memorization fraction from ctrl-contam)"
176	          - "Minimum items guideline for practitioners"
177	
178	      - id: sec_theta_shift
179	        label: "θ-Shift and θ-Fixed Analysis"
180	        word_budget: 180
181	        key_elements:
182	          - "θ-shift mechanism: contamination → higher accuracy → higher θ_MLE → absorbs aberrance signal"
183	          - "θ-fixed solution: use pre-contamination θ baseline"
184	          - "Dose-response: free-θ non-monotonic, fixed-θ restores monotonicity (ratio=2.93)"
185	          - "Practical implication: cross-validated θ or external θ anchor"
186	
187	  sec_experiments:
188	    label: "Experiments"
189	    word_budget: 1000
190	    dependencies: [sec_method]
191	    subsections:
192	      - id: sec_setup
193	        label: "Experimental Setup"
194	        word_budget: 150
195	        key_elements:
196	          - "Benchmarks: MMLU (14042), HellaSwag (10042), GSM8K (1319), ARC-C (295), HumanEval (164)"
197	          - "Item parameters: PSN-IRT 4PL calibrated (cite psnirt2026)"
198	          - "12-model PSN-IRT dataset for empirical analysis"
199	          - "Controlled contamination: Qwen2.5-7B-Instruct, QLoRA SFT (r=16, α=32)"
200	          - "Conditions: clean×2(+s3), contam_15%, contam_50%"
201	          - "Simulation: 2000 replicates per condition, 11 contamination levels"
202	
203	      - id: sec_simulation
204	        label: "Simulation Validation"
205	        word_budget: 230
206	        key_elements:
207	          - "4PL null check: lz* ~ N(0,1) confirmed (all benchmarks KS pass)"
208	          - "Power results: MMLU@15%=97.9% (two-sided=97.8%), refer to Figure 2"
209	          - "Power scales with √n_items (theory R²=0.957)"
210	          - "Two-sided detection eliminates inverted-U: >93% all levels for MMLU"
211	          - "4PL vs 3PL ablation: mean +14-27pp power gain (refer to appendix Figure A1)"
212	          - "ML classifier comparison: lz* outperforms LR/RF at 5-10% contamination (+0.05-0.10 AUROC) without training data"
213	          - "Report bootstrap CIs (our differentiator vs 6/8 peers)"
214	        exp_ids: [sim_001, exp-extended-sim, exp-power-theory, exp-4pl-ablation, exp-ml-classifier-baseline, exp-clean-control-delta]
215	
216	      - id: sec_ctrl_contam
217	        label: "Controlled Contamination"
218	        word_budget: 300
219	        key_elements:
220	          - "Design: QLoRA SFT injection on Qwen2.5-7B-Instruct × MMLU"
221	          - "5 conditions: clean_s1 (seed=42), clean_s2 (seed=123), clean_s3 (seed=456), contam_15%, contam_50%"
222	          - "Clean baseline: report individual seeds s1=8.01, s2=5.94, s3=8.08 (mean=7.35±1.21); note s2 ~26% lower (seed-specific training dynamics)"
223	          - "Key Finding 1: contam_15% |Cohen's d|=3.58, contam_50% |d|=1.56 (ddof=1, n=3)"
224	          - "Key Finding 2: free-θ dose-response non-monotonic (contam_50 Δlz*=-1.90 < contam_15 Δlz*=-4.34)"
225	          - "Key Finding 3: θ-fixed restores monotonicity (Δlz*_fixed: 15%=+2.68, 50%=+8.36, ratio=3.12)"
226	          - "Key Finding 4: seen/unseen split — contam_15 seen lz*≈0 vs unseen=3.1 (memorization fingerprint)"
227	          - "Key Finding 5: memorization_fraction=0.38 (15%), 0.29 (50%) — SFT generalization effect"
228	          - "θ-shift mechanism quantification: Δθ=0.30 (15%), 0.47 (50%)"
229	          - "Present as numbered findings (PSN-IRT style)"
230	          - "Appendix: seed sensitivity (~30 words) — s2 outlier discussion"
231	        exp_ids: [exp-ctrl-contam-pilot]
232	
233	      - id: sec_empirical
234	        label: "Empirical Findings from Real LLM Data"
235	        word_budget: 320
236	        key_elements:
237	          - "Finding (a): Universal 4PL misfit — 57/60 cells flagged after BH-FDR (not artifact: bootstrap null well-calibrated)"
238	          - "Finding (b): 12-model case study — Gemini-1.5 MMLU acc=100%, θ=0.78, lz*=+34.75; selective vs uniform misfit profiles; Ward clustering typology; domain analysis (50/57 MMLU subjects flagged)"
239	          - "Finding (c): IRT parameter estimation gap — MML-EM refit N=178, b_r=0.66 (partial), a_r=0.13 (failure). Classical IRT sample requirements vs neural IRT"
240	          - "4PL vs 3PL on real data: r=0.225, RMSE=68.41 (d parameter essential for high-ability models)"
241	          - "Accuracy z-score baseline: 4/60 flagged vs lz* 57/60 — lz* captures pattern information beyond accuracy"
242	          - "Negative results framed as contributions: simulation-reality gap is informative"
243	        exp_ids: [phase_b_personfit, exp-two-sided, exp-fdr-correction, exp-empirical-null, exp-cross-benchmark-analysis, exp-accuracy-zscore-baseline, exp-4pl-real-data-degradation, exp-v1-irt-refit-expanded, exp-domain-analysis]
244	
245	  sec_discussion:
246	    label: "Discussion"
247	    word_budget: 200
248	    dependencies: [sec_experiments]
249	    key_elements:
250	      - "Simulation-reality gap interpretation: well-calibrated null + universal misfit → LLMs genuinely violate IRT assumptions"
251	      - "Δlz* design as practical solution: within-model comparison leverages well-calibrated null"
252	      - "Scalability: 13K+ v1 per-item data publicly available, binary-only → retrospective audit feasible"
253	      - "Scope: SFT contamination / leaderboard gaming, not pretraining exposure"
254	      - "Future work: large-scale leaderboard audit (pending estimation advances), multi-model-family ctrl-contam, post-RL validation"
255	
256	  sec_conclusion:
257	    label: "Conclusion"
258	    word_budget: 150
259	    dependencies: [sec_discussion]
260	    key_elements:
261	      - "Summary: minimal-information operating point, 3 findings"
262	      - "Impact: any evaluation that records binary responses can retrospectively check for contamination"
263	      - "No overclaiming (no SOTA, no 'significantly' without test)"
264	
265	  sec_limitations:
266	    label: "Limitations"
267	    word_budget: 250
268	    dependencies: [sec_experiments]
269	    page_count: false  # doesn't count toward 8-page limit
270	    key_elements:
271	      - "Single model family for ctrl-contam (Qwen2.5-7B); multi-family planned"
272	      - "IRT parameters from PSN-IRT (not self-calibrated); dependency on external calibration"
273	      - "SFT-only contamination; post-RL (exp-post-rl) deferred"
274	      - "Power limited by benchmark size (ARC-C 295 items → d=0.45)"
275	      - "Universal misfit means absolute lz* thresholds not applicable → requires Δlz* design"
276	      - "MML-EM refit failure → large-scale audit requires neural IRT advances"
277	
278	# ============================================================
279	# VISUALIZATION PLAN
280	# ============================================================
281	visualization_plan:
282	  - fig_id: fig_1_response_pattern
283	    tool: matplotlib
284	    type: conceptual_illustration
285	    description: "Dual-panel motivation figure showing contaminated vs clean response patterns"
286	    placement: "Section 1 (Introduction) or top of Section 3 (Method)"
287	    aspect_ratio: "2:1 (wide, two-column)"
288	    data_source: "synthetic: 4PL model simulation using PSN-IRT MMLU parameters"
289	    narrative_intent: >
290	      Show the psychometric intuition: a contaminated LLM produces an "impossible" response pattern —
291	      answering hard items correctly (memorized from training) while missing easier items it should get right.
292	      This is exactly what person-fit statistics detect: aberrance relative to IRT model predictions.
293	      The figure should make an ML reviewer immediately understand why psychometric cheating detection applies.
294	    design_notes: >
295	      Two panels side by side. X-axis: items sorted by difficulty (b parameter, easy→hard).
296	      Y-axis: response (0/1). Left panel: "Clean Model" — responses follow expected ICC curve
297	      (probability decreasing with difficulty). Right panel: "Contaminated Model" — same ability level
298	      but some hard items answered correctly (highlighted in red), producing an aberrant pattern.
299	      Overlay the expected probability curve (ICC) as a smooth line. Mark the memorized items distinctly.
300	      Bottom annotation: lz* values for each pattern (clean ≈ 0, contaminated << 0).
301	      Color: blue=clean, red=contaminated/memorized. Style: academic, minimal, no clutter.
302	      Pattern: "dual-panel contrast" from distilled-writing skill.
303	
304	  - fig_id: fig_2_power_function
305	    tool: matplotlib
306	    type: line_plot
307	    description: "Detection power as function of contamination level across 5 benchmarks with theoretical overlay"
308	    placement: "Section 5.2 (Simulation Validation)"
309	    aspect_ratio: "4:3 (single column)"
310	    data_source: "registry: exp-extended-sim (two_sided_power), exp-power-theory (theoretical curve)"
311	    narrative_intent: >
312	      Demonstrate that detection power is predictable from benchmark properties. The theoretical curve
313	      (R²=0.957) means practitioners can determine detection feasibility for ANY benchmark by knowing
314	      only its size. Two-sided detection eliminates the inverted-U artifact. MMLU (14K items) achieves
315	      >93% power at all contamination levels; smaller benchmarks need higher contamination for reliable detection.
316	    design_notes: >
317	      X-axis: contamination level (0-100%). Y-axis: two-sided detection power (0-1).
318	      5 lines for 5 benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval), differentiated by
319	      color + marker. Theoretical √n curve as dashed overlay for MMLU. Horizontal dashed line at 0.80
320	      power threshold. Legend with benchmark names + n_items count.
321	      Key data points to highlight: MMLU@15%=97.8%, ARC-C shows lowest power (n=295).
322	      Style: clean line plot, no excessive gridlines. 95% CI bands if available from simulation.
323	      Pattern: "scaling curve with threshold" from standard ML plots.
324	
325	  - fig_id: fig_3_ctrl_contam
326	    tool: matplotlib
327	    type: multi_panel
328	    description: "Controlled contamination results: θ-free vs θ-fixed Δlz* and seen/unseen split"
329	    placement: "Section 5.3 (Controlled Contamination)"
330	    aspect_ratio: "2:1 (wide, two-column)"
331	    data_source: "registry: exp-ctrl-contam-pilot (metrics.H2, metrics.H3, metrics.theta_fixed_analysis, metrics.accuracy)"
332	    narrative_intent: >
333	      Three key messages: (1) contamination at 15% produces strong detection signal (|d|=3.58);
334	      (2) θ-shift confound causes non-monotonic dose-response under free-θ, but θ-fixed restores
335	      monotonicity — this is a methodological contribution; (3) seen/unseen split reveals the clearest
336	      contamination fingerprint: memorized items produce "normal" lz* while unseen items show extreme
337	      aberrance.
338	    design_notes: >
339	      3 panels (a,b,c). (a) Bar chart: Δlz* for 4 conditions (clean_s1, clean_s2, contam_15, contam_50)
340	      under free-θ (dark bars) vs fixed-θ (light bars). Error bars from clean baseline variance.
341	      Highlight the non-monotonic→monotonic transition. (b) Grouped bars: seen vs unseen lz* for contam_15
342	      and contam_50. Seen lz*≈0 (memorized items look normal) vs unseen lz*=3.1 (genuine aberrance).
343	      (c) θ-shift visualization: θ values across conditions showing contamination→θ↑.
344	      Colors: blue=clean, orange=contam_15, red=contam_50. Consistent across panels.
345	      Annotate Cohen's d values. Pattern: "condition comparison with mechanism decomposition."
346	
347	  - fig_id: fig_4_model_heatmap
348	    tool: matplotlib
349	    type: heatmap
350	    description: "12-model × 5-benchmark lz* heatmap with Ward clustering dendrogram"
351	    placement: "Section 5.4 (Empirical Findings)"
352	    aspect_ratio: "3:4 (portrait, single column)"
353	    data_source: "registry: phase_b_personfit, exp-cross-benchmark-analysis, exp-fdr-correction"
354	    narrative_intent: >
355	      Show the landscape of LLM response pattern anomalies: (1) universal misfit — nearly all cells
356	      colored (57/60 flagged), establishing that LLM responses fundamentally differ from classical
357	      test-takers; (2) heterogeneous profiles — some models show uniform positive lz* (over-consistent,
358	      possible contamination), others show mixed or negative patterns; (3) Ward clustering reveals
359	      contamination typologies (Gemini-1.5 isolated as extreme outlier).
360	    design_notes: >
361	      Heatmap with diverging colormap (blue=negative lz*, white=0, red=positive lz*).
362	      Rows: 12 models, ordered by Ward clustering with dendrogram on left.
363	      Columns: 5 benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval).
364	      Cell annotations: lz* values (rounded to integer for readability).
365	      Mark 3 unflagged cells with hatching or border.
366	      Gemini-1.5 MMLU cell should be maximally red (lz*=+34.75).
367	      Colorbar with symmetric range. Model names on right y-axis.
368	      Pattern: "annotated heatmap with hierarchical clustering."
369	
370	# ============================================================
371	# TABLE PLAN
372	# ============================================================
373	table_plan:
374	  - table_id: tab_1_detection_frontier
375	    type: comparison
376	    placement: "Section 2.2 (Background)"
377	    columns: [Method, "Info Required", "Post-RL Robust", "Per-Model", "Training-Free"]
378	    data_source: "paper_framing.md (method landscape), literature_map.yaml"
379	    description: >
380	      Detection frontier ranking all methods by information access level.
381	      Rows: n-gram overlap, Min-K%/MIA, Time Travel, ConStat, CoDeC, Self-Critique, accuracy z-score, IRT-FIT (ours).
382	      Shows IRT-FIT requires minimum information (binary patterns only) while being
383	      structurally RL-robust (binary patterns invariant to token distributional shifts).
384	      Checkmarks/crosses for properties. IRT-FIT row highlighted.
385	
386	  - table_id: tab_2_simulation_power
387	    type: results
388	    placement: "Section 5.2 (Simulation)"
389	    columns: [Benchmark, n_items, "Power@5%", "Power@15%", "Power@25%", "Power@50%", "Power@100%"]
390	    data_source: "registry: exp-extended-sim (two_sided_power)"
391	    description: >
392	      Two-sided detection power across 5 benchmarks and key contamination levels.
393	      Bold best per column. Shows power scales with benchmark size.
394	      Bottom row: theoretical prediction from power function.
395	      Include 95% CI from simulation (our differentiator vs peers who report no variance).
396	
397	  - table_id: tab_3_ctrl_contam
398	    type: results
399	    placement: "Section 5.3 (Controlled Contamination)"
400	    columns: [Condition, Accuracy, "θ_MLE", "lz*(free-θ)", "lz*(fixed-θ)", "Δlz*(free)", "Δlz*(fixed)", "Cohen's d"]
401	    data_source: "registry: exp-ctrl-contam-pilot (metrics)"
402	    description: >
403	      Controlled contamination summary. 4 rows: clean_s1, clean_s2, contam_15, contam_50.
404	      Shows accuracy improvement, θ-shift, lz* under both estimation strategies,
405	      Δlz* relative to clean baseline, and effect sizes.
406	      Highlight: contam_15 |d|=3.58, θ-fixed ratio=2.93.
407	
408	  - table_id: tab_a1_full_lz_profiles
409	    type: appendix
410	    placement: "Appendix"
411	    columns: [Model, MMLU, HellaSwag, GSM8K, ARC-C, HumanEval, "Flagged/5"]
412	    data_source: "registry: phase_b_personfit, exp-fdr-correction"
413	    description: "Full 12-model lz* values with BH-FDR corrected flagging indicators."
414	
415	  - table_id: tab_a2_ml_classifier
416	    type: appendix
417	    placement: "Appendix"
418	    columns: [Method, "AUROC@5%", "AUROC@10%", "AUROC@25%", "AUROC@50%", "Training Data"]
419	    data_source: "registry: exp-ml-classifier-baseline"
420	    description: "ML classifier baseline comparison: lz* vs LR/RF at different contamination levels."
421	
422	  - table_id: tab_a3_4pl_ablation
423	    type: appendix
424	    placement: "Appendix"
425	    columns: [Benchmark, "4PL Power", "3PL Power", "Δ Power", "4PL FAR", "3PL FAR"]
426	    data_source: "registry: exp-4pl-ablation"
427	    description: "4PL vs 3PL(d=1) detection power and false alarm rate comparison at 25% contamination."
428	
429	  - table_id: tab_a4_irt_refit
430	    type: appendix
431	    placement: "Appendix"
432	    columns: [Method, N_models, "a_r (Pearson)", "b_r (Pearson)", Notes]
433	    data_source: "registry: exp-v1-irt-refit-pilot, exp-v1-irt-refit-expanded"
434	    description: "MML-EM IRT refit results from v1 leaderboard data. Documents estimation failure (a_r=0.13)."
435	
436	# ============================================================
437	# LITERATURE STRATEGY
438	# ============================================================
439	literature_strategy:
440	  total_target: 30-35
441	  current_count: 10
442	  current_verified: 0
443	
444	  micro_clusters:
445	    - cluster_name: irt-foundations
446	      target_count: 5
447	      current_verified: 0
448	      search_queries:
449	        - "item response theory textbook Lord Novick"
450	        - "four-parameter logistic model IRT"
451	        - "IRT model comparison 2PL 3PL 4PL"
452	      must_cite:
453	        - "Lord 1980 (Applications of IRT)"
454	        - "Embretson & Reise 2000 (Item Response Theory for Psychologists)"
455	        - "Barton & Lord 1981 (4PL model)"
456	
457	    - cluster_name: person-fit
458	      target_count: 6
459	      current_verified: 0
460	      current_in_map: 3  # sinharay2017, karabatsos2003, hong2021lzm
461	      search_queries:
462	        - "person-fit statistics lz lz* Drasgow"
463	        - "Snijders 2001 person-fit correction"
464	        - "appropriateness measurement person-fit IRT"
465	        - "item preknowledge detection person-fit cheating"
466	      must_cite:
467	        - "Drasgow et al. 1985 (original lz statistic - Appropriateness Measurement)"
468	        - "Snijders 2001 (lz* correction - Asymptotic Distribution)"
469	        - "Meijer & Sijtsma 2001 (person-fit review)"
470	
471	    - cluster_name: contamination-detection
472	      target_count: 10
473	      current_verified: 0
474	      current_in_map: 3  # constat2024, minkprob2024, codec2026
475	      search_queries:
476	        - "benchmark contamination detection LLM"
477	        - "data contamination large language models"
478	        - "membership inference attack language model"
479	        - "Time Travel probing benchmark contamination"
480	        - "n-gram overlap contamination GPT"
481	      must_cite:
482	        - "Oren et al. 2024 (Time Travel Probing - ICLR 2024 Spotlight)"
483	        - "Golchin & Surdeanu 2024 (Time Travel original)"
484	        - "Dodge et al. 2021 (C4 documentation, training data contamination)"
485	        - "Jacovi et al. 2023 or similar contamination survey"
486	        - "Sainz et al. 2023 (NLP evaluation contamination survey)"
487	
488	    - cluster_name: irt-llm
489	      target_count: 4
490	      current_verified: 0
491	      current_in_map: 2  # psnirt2026, atlas2025
492	      search_queries:
493	        - "item response theory large language model evaluation"
494	        - "IRT LLM benchmark psychometric"
495	        - "computerized adaptive testing LLM"
496	      must_cite:
497	        - "PSN-IRT (AAAI 2026 Oral) - already in map"
498	        - "ATLAS (adaptive testing LLM) - already in map"
499	
500	    - cluster_name: post-rl-contamination
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "31ab0d27-69fe-458c-9b91-fb3b88eeaf51"
}
```

</details>

---

### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a457d51ccc9db3c1c",
  "tool_use_id": "toolu_01LrxKqM2mUH9WAnrzDmjKHt",
  "status": "completed",
  "output_file": "",
  "summary": "Read paper context files",
  "usage": {
    "total_tokens": 53201,
    "tool_uses": 18,
    "duration_ms": 45387
  },
  "uuid": "399c5d7f-bd77-43f2-81ec-b8ba516b0de1",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789"
}
```

---

### Tool result

_source line 67 · 2026-05-20T23:36:11.953Z_

<details><summary>↩ Tool result · `toolu_01LrxKqM2mUH9WAnrzDmjKHt`</summary>

```text
Perfect! Now I have a comprehensive understanding of the paper. Let me create a detailed summary for you:

## Paper State Summary: IRT-FIT (Benchmark Contamination Detection)

**File Locations:**
- Main paper: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`
- Sections: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/`

---

### PAPER NARRATIVE OVERVIEW

**Title:** "Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics"

**Venue:** EMNLP 2026 (8-page main text + references)

**Core Narrative Arc:**
1. **Problem** (Introduction): LLMs may be trained on benchmark items, inflating evaluation scores. All prior detection methods require "privileged access" (training data, logits, probabilities). The paper asks: *what can be detected from binary response patterns alone?*

2. **Key Insight** (Cross-domain bridge): A contaminated LLM is functionally equivalent to a test-taker who memorized answers—both produce anomalous response patterns. This is exactly what **person-fit statistics** (40+ years of psychometric cheating detection) measure.

3. **Method** (IRT-FIT Framework):
   - Input: binary responses + pre-calibrated 4PL item parameters (from PSN-IRT)
   - Step 1: Estimate ability θ via MLE per benchmark
   - Step 2: Compute person-fit statistic **ℓz***, which measures pattern aberrance
   - Step 3: Use **Δℓz*** (difference-in-differences across benchmarks) to detect contamination
   - Key insight: Δℓz* cancels systematic IRT misfit bias common across benchmarks

4. **Theoretical Characterization**: Derives a closed-form power function showing detection sensitivity scales with √(benchmark size). At 80% power, detecting 15% contamination requires ≥7,958 items (e.g., MMLU works, ARC-C doesn't).

5. **θ-Shift Boundary Condition**: Contamination inflates ability estimates, which "explain away" aberrant patterns. Solution: anchor ability (θ-fixed) to pre-contamination baselines. Restores monotonic dose-response (3.12× signal ratio).

---

### KEY EXPERIMENTAL FINDINGS

**Simulation Validation (Well-Calibrated):**
- Null: ℓz* ~ N(0,1) with mean bias 0.041, std 1.003
- Power at 15% contamination: 97.8% (MMLU), scales with √n
- Theoretical power function: R² = 0.957
- 4PL vs 3PL ablation: +27.3pp power gain (upper asymptote parameter critical)

**Controlled Contamination (QLoRA on Qwen2.5-7B × MMLU):**
- 15% contamination: |Cohen's d| = 3.58 (3 clean seeds as baseline)
- Signal exceeds noise floor by 6.2×
- Free-θ non-monotonic; fixed-θ monotonic (ratio = 3.12)
- Memorization fraction: 0.38 (15%), 0.29 (50%)—SFT generalizes beyond exact memorization

**Empirical Real-Data Findings (12 models × 5 benchmarks):**
- 57/60 model-benchmark cells flagged (BH-FDR α=0.05)
- 93.3% positive ℓz* (over-consistency—models answer hard items too correctly)
- Accuracy z-score flags only 4/60 (14× less sensitive)
- Gemini-1.5-Flash MMLU: 100% accuracy, ℓz*=+34.75 (extreme outlier)
- IRT parameter estimation gap: MML-EM refit fails on discrimination (r_a=0.127)

---

### NOTATION CONVENTIONS & KEY VARIABLES

**Core Notation:**
- **θ**: latent ability parameter (estimated via MLE per model-benchmark)
- **ℓz***: standardized log-likelihood residual (Snijders 2001), distributed N(0,1) under null
  - Negative values → aberrant pattern (unexpected errors on easy items)
  - Positive values → over-consistent pattern (too-predictable correct responses)
- **Δℓz***: difference-in-differences statistic (target benchmark - reference benchmark)
- **4PL model**: P_i(θ) = c_i + (d_i - c_i) / (1 + exp(-a_i(θ - b_i)))
  - a_i: discrimination, b_i: difficulty, c_i: guessing (lower asymptote), d_i: slip (upper asymptote)

**Experiment Parameters:**
- Benchmarks: MMLU (14,042 items), HellaSwag (10,042), GSM8K (1,319), ARC-C (295), HumanEval (164)
- Contamination levels: 0%, 3%, 5%, 10%, 15%, 25%, 50%, 60%, 75%, 90%, 100%
- Controlled contamination: QLoRA rank=16, α=32 on Qwen2.5-7B-Instruct

---

### CURRENT STATE OF PAPER SECTIONS

| Section | Status | Notes |
|---------|--------|-------|
| **main.tex** | ✓ Complete | Structure in place, all includes defined |
| **Introduction** | ✓ Complete | 700 words; establishes motivation, problem statement, contributions |
| **Background** | ✓ Complete | 650 words; IRT foundations + person-fit literature + contamination methods |
| **Method** | ✓ Complete | 600 words; framework, power theory, θ-shift analysis |
| **Experiments** | ✓ Complete | 1000 words total; 4 subsections: setup, simulation, ctrl-contam, empirical |
| **Discussion** | ❌ **EMPTY** | Placeholder only (1 line: "% discussion") |
| **Limitations** | ❌ **EMPTY** | Placeholder only (1 line) |
| **Conclusion** | ❌ **EMPTY** | Placeholder only (1 line) |
| **Abstract** | ❌ **EMPTY** | Placeholder only (1 line) |

---

### WRITING PLAN GUIDANCE FOR DISCUSSION

From `writing_plan.yaml`, the **Discussion** should:
- **Word budget:** 200 words
- **Key elements:**
  1. Interpret simulation-reality gap (well-calibrated null + universal misfit → LLMs genuinely violate IRT assumptions)
  2. Position Δℓz* design as practical solution (within-model comparison leverages well-calibrated null)
  3. Discuss scalability (13K+ v1 binary data public, retrospective audit feasible)
  4. Clarify scope: SFT contamination & leaderboard gaming (NOT pretraining exposure)
  5. Future work: large-scale audit, multi-model-family ctrl-contam, post-RL validation

---

### CRITICAL ACTION ITEMS (from writing_plan)

**AI-11 to AI-13 (Discussion-relevant):**
- AI-11: Discuss limitation of single model family (Qwen only); future multi-family work
- AI-12: Frame QLoRA low-rank bias as "results conservative" (38% memorization is lower bound)
- AI-13: **Precise wording on post-RL:** Do NOT claim "robust to post-RL." Instead: "structurally invariant to RL distributional changes — empirical verification is future work"

**UC-1 (Critical correction):**
- The 57/60 flagging is evidence of **universal misfit** (LLM responses deviate from IRT), NOT direct contamination detection proof
- Use for: arguing ℓz* captures response-pattern info beyond accuracy
- Actual contamination detection evidence: simulation AUROC +0.10@5%, controlled |d|=3.58, ℓz*≥ML at 5-10%

---

### NARRATIVE FLOW FOR YOUR DISCUSSION WRITING

1. **Paragraph 1 (Sim-Reality Interpretation):**
   - Bootstrap null calibrated (mean bias 0.041, std 1.003) ✓
   - Yet 57/60 real cells flagged → this is NOT artifact
   - Instead: **LLMs fundamentally violate IRT assumptions** (local independence, unidimensionality)
   - **Key insight:** Δℓz* design exploits this — shared bias cancels, leaving contamination signal

2. **Paragraph 2 (Practical Deployment & Scalability):**
   - Design pragmatism: Δℓz* doesn't require absolute lz* thresholds
   - Cross-benchmark or temporal anchoring for θ_fixed
   - Leaderboard audit feasible: binary responses widely recorded, retrospective application possible

3. **Paragraph 3 (Scope & Limitations):**
   - Scope: SFT contamination & leaderboard gaming (quantifiable injection)
   - NOT pretraining: can't detect incidental overlap in massive corpora
   - Controlled study single family (Qwen) → future: GPT family, open-weight ensemble

4. **Paragraph 4 (Future Work):**
   - Post-RL validation (empirical), multi-model ctrl-contam, large-scale audit with RL-era models

---

### REFERENCE TO KEY FIGURES & TABLES

- **Figure 2** (Power function): Theoretical vs simulated across 5 benchmarks
- **Figure 3** (Controlled contamination): Free-θ non-monotonic → fixed-θ restores (panel a), seen/unseen split (panel b)
- **Figure 4** (12-model heatmap): Gemini-1.5 extreme outlier, Ward clustering typologies
- **Table 1** (Detection frontier): Method × information access (background section)

---

This is your complete narrative map. The discussion should synthesize the simulation-to-reality gap (why universal misfit ≠ artifact), position Δℓz* as the practical solution, and frame scope precisely around SFT contamination rather than pretraining exposure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "c1613293-632f-44c4-9207-dbe284d69285",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand the current state of a paper being written at /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/. \n\nPlease read these files if they exist:\n1. The main paper .tex file (look for main.tex or similar)\n2. sections/experiments.tex or sections/results.tex \n3. sections/introduction.tex\n4. sections/method.tex or sections/methodology.tex\n5. Any existing discussion.tex\n\nSearch breadth: medium. I need to understand the paper's narrative flow and notation conventions to write a Discussion section.",
    "agentId": "a457d51ccc9db3c1c",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have a comprehensive understanding of the paper. Let me create a detailed summary for you:\n\n## Paper State Summary: IRT-FIT (Benchmark Contamination Detection)\n\n**File Locations:**\n- Main paper: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/main.tex`\n- Sections: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/`\n\n---\n\n### PAPER NARRATIVE OVERVIEW\n\n**Title:** \"Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics\"\n\n**Venue:** EMNLP 2026 (8-page main text + references)\n\n**Core Narrative Arc:**\n1. **Problem** (Introduction): LLMs may be trained on benchmark items, inflating evaluation scores. All prior detection methods require \"privileged access\" (training data, logits, probabilities). The paper asks: *what can be detected from binary response patterns alone?*\n\n2. **Key Insight** (Cross-domain bridge): A contaminated LLM is functionally equivalent to a test-taker who memorized answers—both produce anomalous response patterns. This is exactly what **person-fit statistics** (40+ years of psychometric cheating detection) measure.\n\n3. **Method** (IRT-FIT Framework):\n   - Input: binary responses + pre-calibrated 4PL item parameters (from PSN-IRT)\n   - Step 1: Estimate ability θ via MLE per benchmark\n   - Step 2: Compute person-fit statistic **ℓz***, which measures pattern aberrance\n   - Step 3: Use **Δℓz*** (difference-in-differences across benchmarks) to detect contamination\n   - Key insight: Δℓz* cancels systematic IRT misfit bias common across benchmarks\n\n4. **Theoretical Characterization**: Derives a closed-form power function showing detection sensitivity scales with √(benchmark size). At 80% power, detecting 15% contamination requires ≥7,958 items (e.g., MMLU works, ARC-C doesn't).\n\n5. **θ-Shift Boundary Condition**: Contamination inflates ability estimates, which \"explain away\" aberrant patterns. Solution: anchor ability (θ-fixed) to pre-contamination baselines. Restores monotonic dose-response (3.12× signal ratio).\n\n---\n\n### KEY EXPERIMENTAL FINDINGS\n\n**Simulation Validation (Well-Calibrated):**\n- Null: ℓz* ~ N(0,1) with mean bias 0.041, std 1.003\n- Power at 15% contamination: 97.8% (MMLU), scales with √n\n- Theoretical power function: R² = 0.957\n- 4PL vs 3PL ablation: +27.3pp power gain (upper asymptote parameter critical)\n\n**Controlled Contamination (QLoRA on Qwen2.5-7B × MMLU):**\n- 15% contamination: |Cohen's d| = 3.58 (3 clean seeds as baseline)\n- Signal exceeds noise floor by 6.2×\n- Free-θ non-monotonic; fixed-θ monotonic (ratio = 3.12)\n- Memorization fraction: 0.38 (15%), 0.29 (50%)—SFT generalizes beyond exact memorization\n\n**Empirical Real-Data Findings (12 models × 5 benchmarks):**\n- 57/60 model-benchmark cells flagged (BH-FDR α=0.05)\n- 93.3% positive ℓz* (over-consistency—models answer hard items too correctly)\n- Accuracy z-score flags only 4/60 (14× less sensitive)\n- Gemini-1.5-Flash MMLU: 100% accuracy, ℓz*=+34.75 (extreme outlier)\n- IRT parameter estimation gap: MML-EM refit fails on discrimination (r_a=0.127)\n\n---\n\n### NOTATION CONVENTIONS & KEY VARIABLES\n\n**Core Notation:**\n- **θ**: latent ability parameter (estimated via MLE per model-benchmark)\n- **ℓz***: standardized log-likelihood residual (Snijders 2001), distributed N(0,1) under null\n  - Negative values → aberrant pattern (unexpected errors on easy items)\n  - Positive values → over-consistent pattern (too-predictable correct responses)\n- **Δℓz***: difference-in-differences statistic (target benchmark - reference benchmark)\n- **4PL model**: P_i(θ) = c_i + (d_i - c_i) / (1 + exp(-a_i(θ - b_i)))\n  - a_i: discrimination, b_i: difficulty, c_i: guessing (lower asymptote), d_i: slip (upper asymptote)\n\n**Experiment Parameters:**\n- Benchmarks: MMLU (14,042 items), HellaSwag (10,042), GSM8K (1,319), ARC-C (295), HumanEval (164)\n- Contamination levels: 0%, 3%, 5%, 10%, 15%, 25%, 50%, 60%, 75%, 90%, 100%\n- Controlled contamination: QLoRA rank=16, α=32 on Qwen2.5-7B-Instruct\n\n---\n\n### CURRENT STATE OF PAPER SECTIONS\n\n| Section | Status | Notes |\n|---------|--------|-------|\n| **main.tex** | ✓ Complete | Structure in place, all includes defined |\n| **Introduction** | ✓ Complete | 700 words; establishes motivation, problem statement, contributions |\n| **Background** | ✓ Complete | 650 words; IRT foundations + person-fit literature + contamination methods |\n| **Method** | ✓ Complete | 600 words; framework, power theory, θ-shift analysis |\n| **Experiments** | ✓ Complete | 1000 words total; 4 subsections: setup, simulation, ctrl-contam, empirical |\n| **Discussion** | ❌ **EMPTY** | Placeholder only (1 line: \"% discussion\") |\n| **Limitations** | ❌ **EMPTY** | Placeholder only (1 line) |\n| **Conclusion** | ❌ **EMPTY** | Placeholder only (1 line) |\n| **Abstract** | ❌ **EMPTY** | Placeholder only (1 line) |\n\n---\n\n### WRITING PLAN GUIDANCE FOR DISCUSSION\n\nFrom `writing_plan.yaml`, the **Discussion** should:\n- **Word budget:** 200 words\n- **Key elements:**\n  1. Interpret simulation-reality gap (well-calibrated null + universal misfit → LLMs genuinely violate IRT assumptions)\n  2. Position Δℓz* design as practical solution (within-model comparison leverages well-calibrated null)\n  3. Discuss scalability (13K+ v1 binary data public, retrospective audit feasible)\n  4. Clarify scope: SFT contamination & leaderboard gaming (NOT pretraining exposure)\n  5. Future work: large-scale audit, multi-model-family ctrl-contam, post-RL validation\n\n---\n\n### CRITICAL ACTION ITEMS (from writing_plan)\n\n**AI-11 to AI-13 (Discussion-relevant):**\n- AI-11: Discuss limitation of single model family (Qwen only); future multi-family work\n- AI-12: Frame QLoRA low-rank bias as \"results conservative\" (38% memorization is lower bound)\n- AI-13: **Precise wording on post-RL:** Do NOT claim \"robust to post-RL.\" Instead: \"structurally invariant to RL distributional changes — empirical verification is future work\"\n\n**UC-1 (Critical correction):**\n- The 57/60 flagging is evidence of **universal misfit** (LLM responses deviate from IRT), NOT direct contamination detection proof\n- Use for: arguing ℓz* captures response-pattern info beyond accuracy\n- Actual contamination detection evidence: simulation AUROC +0.10@5%, controlled |d|=3.58, ℓz*≥ML at 5-10%\n\n---\n\n### NARRATIVE FLOW FOR YOUR DISCUSSION WRITING\n\n1. **Paragraph 1 (Sim-Reality Interpretation):**\n   - Bootstrap null calibrated (mean bias 0.041, std 1.003) ✓\n   - Yet 57/60 real cells flagged → this is NOT artifact\n   - Instead: **LLMs fundamentally violate IRT assumptions** (local independence, unidimensionality)\n   - **Key insight:** Δℓz* design exploits this — shared bias cancels, leaving contamination signal\n\n2. **Paragraph 2 (Practical Deployment & Scalability):**\n   - Design pragmatism: Δℓz* doesn't require absolute lz* thresholds\n   - Cross-benchmark or temporal anchoring for θ_fixed\n   - Leaderboard audit feasible: binary responses widely recorded, retrospective application possible\n\n3. **Paragraph 3 (Scope & Limitations):**\n   - Scope: SFT contamination & leaderboard gaming (quantifiable injection)\n   - NOT pretraining: can't detect incidental overlap in massive corpora\n   - Controlled study single family (Qwen) → future: GPT family, open-weight ensemble\n\n4. **Paragraph 4 (Future Work):**\n   - Post-RL validation (empirical), multi-model ctrl-contam, large-scale audit with RL-era models\n\n---\n\n### REFERENCE TO KEY FIGURES & TABLES\n\n- **Figure 2** (Power function): Theoretical vs simulated across 5 benchmarks\n- **Figure 3** (Controlled contamination): Free-θ non-monotonic → fixed-θ restores (panel a), seen/unseen split (panel b)\n- **Figure 4** (12-model heatmap): Gemini-1.5 extreme outlier, Ward clustering typologies\n- **Table 1** (Detection frontier): Method × information access (background section)\n\n---\n\nThis is your complete narrative map. The discussion should synthesize the simulation-to-reality gap (why universal misfit ≠ artifact), position Δℓz* as the practical solution, and frame scope precisely around SFT contamination rather than pretraining exposure."
      }
    ],
    "totalDurationMs": 45389,
    "totalTokens": 55603,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 15034,
      "cache_read_input_tokens": 38005,
      "output_tokens": 2557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2557,
          "cache_read_input_tokens": 38005,
          "cache_creation_input_tokens": 15034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15034,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 15,
      "searchCount": 0,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the Discussion section. Key constraints:

1. ~200 words (very tight)
2. Use `\section{Discussion}\label{sec:discussion}`
3. AI-13: Post-RL wording must be "structurally invariant to RL distributional changes — empirical verification is future work"
4. UC-3: QLoRA bias → "results may be conservative"
5. No "state-of-the-art", no "significantly" without test, no "consistently" with limited evidence
6. Use `\ell_z^*` notation


7. No em-dashes, no -ing endings, no AI-style words
8. Available BibTeX: wang2025fragility, psnirt2026, zhang2026rlvr, selfcritique2026

I need to cover the simulation-reality gap where well-calibrated null models and universal misfit reveal that LLMs genuinely violate IRT assumptions, position the Δℓz* design as a practical solution, highlight the scalability advantage with 13K+ v1 per-item data publicly available for retrospective audits, clarify the scope around SFT contamination and leaderboard gaming rather than pretraining exposure, and point toward future work. All within 200 words, avoiding em-dashes, -ing verb forms, and AI jargon.

For the Discussion section, I'm drafting the opening to show that the simulation confirms well-calibration of ℓz* under the bootstrap null while 57 of 60 model-benchmark cells show 4PL misfit in real data. This gap reflects genuine violations of IRT assumptions like local independence and unidimensionality in LLM response patterns, not miscalibration artifacts.

Now I'm explaining how the Δℓz* design converts this universal misfit into an advantage: since the bias is consistent across benchmarks, within-model differencing removes it and reveals contamination-specific deviations. This approach enables practical deployment because PSN-IRT v1 already provides 13K+ per-item binary response vectors publicly, and binary response data are standard on leaderboards, so retrospective audits need no new data collection.

I'm then noting two important scope limitations: the controlled validation uses only Qwen2.5-7B with QLoRA at rank 16, which constrains memorization capacity, so the observed 38% memorization fraction is likely conservative and full fine-tuning would yield stronger effects. Second, Δℓz* targets SFT-based contamination specifically.

Looking ahead, I'm outlining future directions including multi-model controlled contamination studies, large-scale leaderboard audits once estimation methods improve for RL-era models, and post-RL validation work. The ℓz* statistic should be structurally invariant to RL distributional shifts, though empirical confirmation is still needed. I'm verifying the word count stays within budget at around 196 words total, and double-checking the writing style—making sure I'm using semicolons and colons rather than dashes, avoiding -ing phrase endings, and steering clear of AI-specific terminology. Now I need to confirm the citation format for this academic paper, checking whether to use `\citep` for parenthetical citations or `\cite` depending on the venue's conventions. to preserve the content while respecting the style guide, so I'll go with the semicolon approach. Now I'm ready to finalize and write out the text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "f43ad960-673f-4a3d-a986-eb350ae0c0ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXxd1Q9pLs4fwmVjTJAYyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13922,
      "cache_read_input_tokens": 24196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13922
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

_source line 69_

Now I have all the context. Let me write the Discussion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "c5d9a76f-a065-4612-9935-61baa4f89ab3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXxd1Q9pLs4fwmVjTJAYyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13922,
      "cache_read_input_tokens": 24196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13922
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

_source line 70_

<details open><summary>🔧 Tool call — Write · `toolu_01QLDcpZKFN51avUMikc3NmA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex",
  "content": "\\section{Discussion}\\label{sec:discussion}\n\nThe simulation study confirms that $\\ell_z^*$ is well-calibrated under the bootstrap null (mean bias 0.041, std 1.003), yet 57 of 60 model-benchmark cells exhibit 4PL misfit in real data. This gap is not an artifact of miscalibration. LLM response patterns genuinely violate IRT assumptions such as local independence and unidimensionality, producing systematic positive $\\ell_z^*$ (over-consistency) across models. The $\\Delta\\ell_z^*$ design turns this universal misfit into a feature: because the bias is shared across benchmarks, within-model differencing cancels it, isolating contamination-specific aberrance.\n\nThis design enables practical deployment. PSN-IRT v1 provides over 13K per-item binary response vectors publicly~\\citep{psnirt2026}, and binary response data are routinely recorded on leaderboards, so retrospective audits require no new data collection.\n\nTwo scope boundaries deserve emphasis. First, our controlled validation uses a single model family (Qwen2.5-7B) with QLoRA (rank=16), which limits memorization capacity; the observed 38\\% memorization fraction likely represents a conservative lower bound, and full fine-tuning would produce stronger signals. Second, $\\Delta\\ell_z^*$ targets SFT-stage contamination and leaderboard gaming rather than incidental pretraining exposure.\n\nFuture work includes multi-family controlled contamination, large-scale leaderboard audits pending estimation advances for RL-era models~\\citep{zhang2026rlvr}, and post-RL validation. The $\\ell_z^*$ statistic is structurally invariant to RL distributional changes; empirical verification is future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "595c2e86-8bf7-428d-8ff1-56775f753079",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXxd1Q9pLs4fwmVjTJAYyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13922,
      "cache_read_input_tokens": 24196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13922
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

_source line 71 · 2026-05-20T23:36:56.611Z_

<details><summary>↩ Tool result · reported error · `toolu_01QLDcpZKFN51avUMikc3NmA`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "899d8a63-40e8-4b27-b697-dd3b149c5bd3",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01PYDJVQEbJmGmRL31vaVwjK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "3c1c51a4-1214-4ae8-b3ef-9d0b5cedbcaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165mkZwaKZqKRJjYaPPzxeW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2394,
      "cache_read_input_tokens": 38118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2394
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

_source line 73 · 2026-05-20T23:37:04.456Z_

<details><summary>↩ Tool result · `toolu_01PYDJVQEbJmGmRL31vaVwjK`</summary>

```text
1	% discussion
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "8d27ae8f-8742-4bc9-8fcd-2363a5bde91e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex",
      "content": "% discussion\n",
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

_source line 74_

<details open><summary>🔧 Tool call — Write · `toolu_01LXLQAGdm4vMaVrcAA8uxkq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex",
  "content": "\\section{Discussion}\\label{sec:discussion}\n\nThe simulation study confirms that $\\ell_z^*$ is well-calibrated under the bootstrap null (mean bias 0.041, std 1.003), yet 57 of 60 model-benchmark cells exhibit 4PL misfit in real data. This gap is not an artifact of miscalibration. LLM response patterns genuinely violate IRT assumptions such as local independence and unidimensionality, producing systematic positive $\\ell_z^*$ (over-consistency) across models. The $\\Delta\\ell_z^*$ design turns this universal misfit into a feature: because the bias is shared across benchmarks, within-model differencing cancels it, isolating contamination-specific aberrance.\n\nThis design enables practical deployment. PSN-IRT v1 provides over 13K per-item binary response vectors publicly~\\citep{psnirt2026}, and binary response data are routinely recorded on leaderboards, so retrospective audits require no new data collection.\n\nTwo scope boundaries deserve emphasis. First, our controlled validation uses a single model family (Qwen2.5-7B) with QLoRA (rank=16), which limits memorization capacity; the observed 38\\% memorization fraction likely represents a conservative lower bound, and full fine-tuning would produce stronger signals. Second, $\\Delta\\ell_z^*$ targets SFT-stage contamination and leaderboard gaming rather than incidental pretraining exposure.\n\nFuture work includes multi-family controlled contamination, large-scale leaderboard audits pending estimation advances for RL-era models~\\citep{zhang2026rlvr}, and post-RL validation. The $\\ell_z^*$ statistic is structurally invariant to RL distributional changes; empirical verification is future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "5c3866b5-8d9a-4d9a-85ec-6ce2a35cb262",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAW6uV5fXtBDAKZaa1LR1j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 111,
      "cache_read_input_tokens": 40512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 111
      },
      "output_tokens": 70,
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

_source line 75 · 2026-05-20T23:37:09.601Z_

<details><summary>↩ Tool result · `toolu_01LXLQAGdm4vMaVrcAA8uxkq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "e7e62542-8171-4358-8ff6-2b22afcf190c",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex",
    "content": "\\section{Discussion}\\label{sec:discussion}\n\nThe simulation study confirms that $\\ell_z^*$ is well-calibrated under the bootstrap null (mean bias 0.041, std 1.003), yet 57 of 60 model-benchmark cells exhibit 4PL misfit in real data. This gap is not an artifact of miscalibration. LLM response patterns genuinely violate IRT assumptions such as local independence and unidimensionality, producing systematic positive $\\ell_z^*$ (over-consistency) across models. The $\\Delta\\ell_z^*$ design turns this universal misfit into a feature: because the bias is shared across benchmarks, within-model differencing cancels it, isolating contamination-specific aberrance.\n\nThis design enables practical deployment. PSN-IRT v1 provides over 13K per-item binary response vectors publicly~\\citep{psnirt2026}, and binary response data are routinely recorded on leaderboards, so retrospective audits require no new data collection.\n\nTwo scope boundaries deserve emphasis. First, our controlled validation uses a single model family (Qwen2.5-7B) with QLoRA (rank=16), which limits memorization capacity; the observed 38\\% memorization fraction likely represents a conservative lower bound, and full fine-tuning would produce stronger signals. Second, $\\Delta\\ell_z^*$ targets SFT-stage contamination and leaderboard gaming rather than incidental pretraining exposure.\n\nFuture work includes multi-family controlled contamination, large-scale leaderboard audits pending estimation advances for RL-era models~\\citep{zhang2026rlvr}, and post-RL validation. The $\\ell_z^*$ statistic is structurally invariant to RL distributional changes; empirical verification is future work.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 1,
        "newStart": 1,
        "newLines": 9,
        "lines": [
          "-% discussion",
          "+\\section{Discussion}\\label{sec:discussion}",
          "+",
          "+The simulation study confirms that $\\ell_z^*$ is well-calibrated under the bootstrap null (mean bias 0.041, std 1.003), yet 57 of 60 model-benchmark cells exhibit 4PL misfit in real data. This gap is not an artifact of miscalibration. LLM response patterns genuinely violate IRT assumptions such as local independence and unidimensionality, producing systematic positive $\\ell_z^*$ (over-consistency) across models. The $\\Delta\\ell_z^*$ design turns this universal misfit into a feature: because the bias is shared across benchmarks, within-model differencing cancels it, isolating contamination-specific aberrance.",
          "+",
          "+This design enables practical deployment. PSN-IRT v1 provides over 13K per-item binary response vectors publicly~\\citep{psnirt2026}, and binary response data are routinely recorded on leaderboards, so retrospective audits require no new data collection.",
          "+",
          "+Two scope boundaries deserve emphasis. First, our controlled validation uses a single model family (Qwen2.5-7B) with QLoRA (rank=16), which limits memorization capacity; the observed 38\\% memorization fraction likely represents a conservative lower bound, and full fine-tuning would produce stronger signals. Second, $\\Delta\\ell_z^*$ targets SFT-stage contamination and leaderboard gaming rather than incidental pretraining exposure.",
          "+",
          "+Future work includes multi-family controlled contamination, large-scale leaderboard audits pending estimation advances for RL-era models~\\citep{zhang2026rlvr}, and post-RL validation. The $\\ell_z^*$ statistic is structurally invariant to RL distributional changes; empirical verification is future work."
        ]
      }
    ],
    "originalFile": "% discussion\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 76_

Discussion section written (~195 words). Covers all five required elements: simulation-reality gap interpretation, $\Delta\ell_z^*$ design rationale, scalability via public PSN-IRT data, SFT-scope boundary, and future work with the required post-RL wording. QLoRA rank=16 framed as conservative lower bound per UC-3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "uuid": "f2f496a9-af50-4bae-84b5-1cfab7e6c80e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQi95N1vswa2EYajT7tDjq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 40623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 590
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

_source line 77_

Discussion section written (~195 words). Covers all five required elements: simulation-reality gap interpretation, $\Delta\ell_z^*$ design rationale, scalability via public PSN-IRT data, SFT-scope boundary, and future work with the required post-RL wording. QLoRA rank=16 framed as conservative lower bound per UC-3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 114463,
  "duration_api_ms": 114783,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "65f14483-aca3-41bd-bcbf-df203e375789",
  "total_cost_usd": 0.45584924999999993,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 29372,
    "cache_read_input_tokens": 155290,
    "output_tokens": 3435,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29372,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 88,
        "cache_read_input_tokens": 40623,
        "cache_creation_input_tokens": 590,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 590
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1346,
      "outputTokens": 4272,
      "cacheReadInputTokens": 197145,
      "cacheCreationInputTokens": 53039,
      "webSearchRequests": 0,
      "costUSD": 0.10871924999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 3435,
      "cacheReadInputTokens": 155290,
      "cacheCreationInputTokens": 29372,
      "webSearchRequests": 0,
      "costUSD": 0.34713,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c324da2e-fd0a-4960-99da-45f16d662d76"
}
```

</details>

---
