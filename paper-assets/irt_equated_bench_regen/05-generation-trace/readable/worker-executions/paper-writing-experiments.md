# paper writing experiments

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 102
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260521T040002.log`
- **Structured JSON:** [`bc0f4ac27944692ae574.json`](../../sessions/bc/bc0f4ac27944692ae574.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
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
  "uuid": "3f9bcb4a-373e-4bc7-9991-7ee0aea83c29",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779351000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1f52d120-b7de-4538-8135-82dd8ded0fd9",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Assistant

_source line 4_

I'll start by loading the required writing norms and checking the current state of the paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "15106fa8-458f-406e-b607-af7b749e2eed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xqn3qQagNCT5D1EeDPUxsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14224,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14224
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

<details open><summary>🔧 Tool call — Read · `toolu_013qZbyYxpkDgkNM2d9BPXRD`</summary>

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
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "cb1732c6-63de-4620-b214-0a21e054bd3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xqn3qQagNCT5D1EeDPUxsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14224,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14224
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

_source line 6 · 2026-05-21T04:00:16.577Z_

<details><summary>↩ Tool result · `toolu_013qZbyYxpkDgkNM2d9BPXRD`</summary>

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
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "c00c833a-06ee-49c3-b97e-d079fa000425",
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

<details open><summary>🔧 Tool call — Read · `toolu_01LuCFeTdYyT3yTuUQjbEBCW`</summary>

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
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "1a98a7d6-7ae3-417a-aa5f-5db722b9ac2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xqn3qQagNCT5D1EeDPUxsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14224,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14224
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

_source line 8 · 2026-05-21T04:00:17.104Z_

<details><summary>↩ Tool result · `toolu_01LuCFeTdYyT3yTuUQjbEBCW`</summary>

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
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "934b17e2-a05c-477a-884c-d13bf024a5da",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01FLNhHoz9DEFaYdSSETnneB`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "c967ef1b-0a00-4d5d-b119-5001e90384ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xqn3qQagNCT5D1EeDPUxsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14224,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14224
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

_source line 10 · 2026-05-21T04:00:18.904Z_

<details><summary>↩ Tool result · `toolu_01FLNhHoz9DEFaYdSSETnneB`</summary>

```text
paper/references.bib
paper/iclr2026_conference.sty
paper/iclr2026_conference.bst
paper/fancyhdr.sty
paper/natbib.sty
paper/math_commands.tex
paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "478d12f0-e35c-4c43-b008-73fb9c60e14f",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib",
      "paper/iclr2026_conference.sty",
      "paper/iclr2026_conference.bst",
      "paper/fancyhdr.sty",
      "paper/natbib.sty",
      "paper/math_commands.tex",
      "paper/main.tex"
    ],
    "durationMs": 24,
    "numFiles": 7,
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
Let me check the paper directory structure, especially the sections directory and figures, and also read the main.tex to understand the setup.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "9fecbfba-18ff-4ca8-a9c8-035e9ebd9446",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oro7ps9nSWGJ13wSgSG9U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11304,
      "cache_read_input_tokens": 26065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11304
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

Let me check the existing paper structure and available figures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "ce92861a-2d33-4c10-a272-01d656665344",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oro7ps9nSWGJ13wSgSG9U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11304,
      "cache_read_input_tokens": 26065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11304
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

<details open><summary>🔧 Tool call — Read · `toolu_01TttWYrNfUhZhjeN57whbsj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "76cfd601-eb6d-4585-91f5-5494fdd72b97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oro7ps9nSWGJ13wSgSG9U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11304,
      "cache_read_input_tokens": 26065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11304
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

_source line 14 · 2026-05-21T04:00:25.612Z_

<details><summary>↩ Tool result · `toolu_01TttWYrNfUhZhjeN57whbsj`</summary>

```text
1	\documentclass{article}
2	\usepackage{iclr2026_conference,times}
3	\input{math_commands.tex}
4	
5	\usepackage{hyperref}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{microtype}
11	\usepackage{multirow}
12	\usepackage{subcaption}
13	\usepackage{cleveref}
14	
15	\graphicspath{{../figures/paper/}}
16	
17	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
18	
19	%\iclrfinalcopy
20	
21	\newcommand{\fix}{\marginpar{FIX}}
22	\newcommand{\new}{\marginpar{NEW}}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\bibliography{references}
37	\bibliographystyle{iclr2026_conference}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "2e61aff2-6d23-4b89-966b-a395f047412e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
      "content": "\\documentclass{article}\n\\usepackage{iclr2026_conference,times}\n\\input{math_commands.tex}\n\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{microtype}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\\usepackage{cleveref}\n\n\\graphicspath{{../figures/paper/}}\n\n\\title{Psychometric Instability of LLM Benchmarks:\\\\Differential Item Functioning Reveals 31\\% of MMLU Items\\\\Behave Differently Across Model Generations}\n\n%\\iclrfinalcopy\n\n\\newcommand{\\fix}{\\marginpar{FIX}}\n\\newcommand{\\new}{\\marginpar{NEW}}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\bibliography{references}\n\\bibliographystyle{iclr2026_conference}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01URVpsBtn1PJo1PMX2aQu6M`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/ 2>/dev/null; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/figures/paper/ 2>/dev/null || ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/ 2>/dev/null",
  "description": "Check sections dir and figures dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "4e9caf1e-8ada-47f8-bcf2-341462828c9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oro7ps9nSWGJ13wSgSG9U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11304,
      "cache_read_input_tokens": 26065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11304
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

_source line 16 · 2026-05-21T04:00:28.012Z_

<details><summary>↩ Tool result · `toolu_01URVpsBtn1PJo1PMX2aQu6M`</summary>

```text
total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 03:58 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 21 03:58 ..
---
total 2820
drwxr-xr-x 2 ubuntu ubuntu   4096 May 21 01:34 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 20 23:41 ..
-rw-r--r-- 1 ubuntu ubuntu  40955 May 21 01:31 fig_1_global_vs_differential.pdf
-rw-r--r-- 1 ubuntu ubuntu 303811 May 21 01:31 fig_1_global_vs_differential.png
-rw-r--r-- 1 ubuntu ubuntu   5482 May 21 01:31 fig_1_global_vs_differential.py
-rw-r--r-- 1 ubuntu ubuntu  34084 May 20 23:42 fig_2_dose_response.pdf
-rw-r--r-- 1 ubuntu ubuntu 186046 May 20 23:42 fig_2_dose_response.png
-rw-r--r-- 1 ubuntu ubuntu   5192 May 20 23:42 fig_2_dose_response.py
-rw-r--r-- 1 ubuntu ubuntu  21389 May 21 00:03 fig_3_within_subject_matching.pdf
-rw-r--r-- 1 ubuntu ubuntu 111479 May 21 00:03 fig_3_within_subject_matching.png
-rw-r--r-- 1 ubuntu ubuntu   5311 May 21 00:03 fig_3_within_subject_matching.py
-rw-r--r-- 1 ubuntu ubuntu 161450 May 21 01:14 fig_4_downstream_impact.pdf
-rw-r--r-- 1 ubuntu ubuntu 451446 May 21 01:14 fig_4_downstream_impact.png
-rw-r--r-- 1 ubuntu ubuntu   5190 May 21 01:14 fig_4_downstream_impact.py
-rw-r--r-- 1 ubuntu ubuntu  28664 May 21 01:34 fig_5_gsm1k_dif_correlation.pdf
-rw-r--r-- 1 ubuntu ubuntu 292793 May 21 01:34 fig_5_gsm1k_dif_correlation.png
-rw-r--r-- 1 ubuntu ubuntu  21893 May 21 00:21 fig_A1_subject_heatmap.pdf
-rw-r--r-- 1 ubuntu ubuntu 619659 May 21 00:21 fig_A1_subject_heatmap.png
-rw-r--r-- 1 ubuntu ubuntu   5675 May 21 00:21 fig_A1_subject_heatmap.py
-rw-r--r-- 1 ubuntu ubuntu  29519 May 21 00:26 fig_A2_q3_distribution.pdf
-rw-r--r-- 1 ubuntu ubuntu 496994 May 21 00:26 fig_A2_q3_distribution.png
-rw-r--r-- 1 ubuntu ubuntu   2859 May 21 00:26 fig_A2_q3_distribution.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "3ebd085c-5822-4f15-a00f-4159d2722b0e",
  "tool_use_result": {
    "stdout": "total 8\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 21 03:58 .\ndrwxr-xr-x 3 ubuntu ubuntu 4096 May 21 03:58 ..\n---\ntotal 2820\ndrwxr-xr-x 2 ubuntu ubuntu   4096 May 21 01:34 .\ndrwxr-xr-x 3 ubuntu ubuntu   4096 May 20 23:41 ..\n-rw-r--r-- 1 ubuntu ubuntu  40955 May 21 01:31 fig_1_global_vs_differential.pdf\n-rw-r--r-- 1 ubuntu ubuntu 303811 May 21 01:31 fig_1_global_vs_differential.png\n-rw-r--r-- 1 ubuntu ubuntu   5482 May 21 01:31 fig_1_global_vs_differential.py\n-rw-r--r-- 1 ubuntu ubuntu  34084 May 20 23:42 fig_2_dose_response.pdf\n-rw-r--r-- 1 ubuntu ubuntu 186046 May 20 23:42 fig_2_dose_response.png\n-rw-r--r-- 1 ubuntu ubuntu   5192 May 20 23:42 fig_2_dose_response.py\n-rw-r--r-- 1 ubuntu ubuntu  21389 May 21 00:03 fig_3_within_subject_matching.pdf\n-rw-r--r-- 1 ubuntu ubuntu 111479 May 21 00:03 fig_3_within_subject_matching.png\n-rw-r--r-- 1 ubuntu ubuntu   5311 May 21 00:03 fig_3_within_subject_matching.py\n-rw-r--r-- 1 ubuntu ubuntu 161450 May 21 01:14 fig_4_downstream_impact.pdf\n-rw-r--r-- 1 ubuntu ubuntu 451446 May 21 01:14 fig_4_downstream_impact.png\n-rw-r--r-- 1 ubuntu ubuntu   5190 May 21 01:14 fig_4_downstream_impact.py\n-rw-r--r-- 1 ubuntu ubuntu  28664 May 21 01:34 fig_5_gsm1k_dif_correlation.pdf\n-rw-r--r-- 1 ubuntu ubuntu 292793 May 21 01:34 fig_5_gsm1k_dif_correlation.png\n-rw-r--r-- 1 ubuntu ubuntu  21893 May 21 00:21 fig_A1_subject_heatmap.pdf\n-rw-r--r-- 1 ubuntu ubuntu 619659 May 21 00:21 fig_A1_subject_heatmap.png\n-rw-r--r-- 1 ubuntu ubuntu   5675 May 21 00:21 fig_A1_subject_heatmap.py\n-rw-r--r-- 1 ubuntu ubuntu  29519 May 21 00:26 fig_A2_q3_distribution.pdf\n-rw-r--r-- 1 ubuntu ubuntu 496994 May 21 00:26 fig_A2_q3_distribution.png\n-rw-r--r-- 1 ubuntu ubuntu   2859 May 21 00:26 fig_A2_q3_distribution.py",
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

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good. I have a clear picture now. Let me also check the references.bib for the citation keys mentioned, and read the method section to understand notation established there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "39f5f638-43a0-49b2-a33a-faa9fabb6e25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFGWSEYMLM8XJi8SfnsYrz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 37369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
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

Let me check the existing sections for notation consistency and the references.bib for citation keys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "34d10271-b1e2-4f05-a6c6-5021e63ef252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFGWSEYMLM8XJi8SfnsYrz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 37369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
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

<details open><summary>🔧 Tool call — Bash · `toolu_01VhDgzsokbR4qhP82FvV3Gs`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "List existing section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "7c06dc80-5892-47de-978a-1fc30ecd558d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFGWSEYMLM8XJi8SfnsYrz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 37369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
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

_source line 20 · 2026-05-21T04:00:35.282Z_

<details><summary>↩ Tool result · `toolu_01VhDgzsokbR4qhP82FvV3Gs`</summary>

```text
total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 03:58 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 21 03:58 ..
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "f6aa56aa-3559-4e31-87d7-bfe1ce0c350a",
  "tool_use_result": {
    "stdout": "total 8\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 21 03:58 .\ndrwxr-xr-x 3 ubuntu ubuntu 4096 May 21 03:58 ..",
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

<details open><summary>🔧 Tool call — Grep · `toolu_0145pepTMJzTzdxu6H897Mhw`</summary>

```json
{
  "pattern": "@(article|inproceedings|misc)\\{(kipnis|li2024|holland|habba|zhang2024)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "output_mode": "content",
  "-A": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "c0ac3fe9-9a8b-4ee4-98f6-d7ae55834566",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFGWSEYMLM8XJi8SfnsYrz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 37369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
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

_source line 22 · 2026-05-21T04:00:37.482Z_

<details><summary>↩ Tool result · `toolu_0145pepTMJzTzdxu6H897Mhw`</summary>

```text
30:@inproceedings{li2024contamination,
31-  title     = {An Open-Source Data Contamination Report for Large Language Models},
32-  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33-  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
--
73:@misc{zhang2024gsm1k,
74-  title         = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
75-  author        = {Zhang, Hugh},
76-  year          = {2024},
--
83:@misc{zhang2024minkpp,
84-  title         = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
85-  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
86-  year          = {2024},
--
164:@misc{habba2026growingpains,
165-  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
166-  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
167-  year          = {2026},
--
195:@misc{kipnis2024metabench,
196-  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
197-  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},
198-  year          = {2024},
--
241:@inproceedings{li2024latesteval,
242-  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},
243-  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},
244-  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "c45c305a-b4b5-483c-81a1-14fddeb740d4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "30:@inproceedings{li2024contamination,\n31-  title     = {An Open-Source Data Contamination Report for Large Language Models},\n32-  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},\n33-  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n--\n73:@misc{zhang2024gsm1k,\n74-  title         = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},\n75-  author        = {Zhang, Hugh},\n76-  year          = {2024},\n--\n83:@misc{zhang2024minkpp,\n84-  title         = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n85-  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},\n86-  year          = {2024},\n--\n164:@misc{habba2026growingpains,\n165-  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n166-  author        = {Habba, Eitam and Itzhak, Ido and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n167-  year          = {2026},\n--\n195:@misc{kipnis2024metabench,\n196-  title         = {metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},\n197-  author        = {Kipnis, Alon and Voudouris, Konstantinos and Schulze Buschoff, Luca Maria and Schulz, Eric},\n198-  year          = {2024},\n--\n241:@inproceedings{li2024latesteval,\n242-  title     = {{LatestEval}: Addressing Data Contamination in Language Model Evaluation through Dynamic and Time-Sensitive Test Construction},\n243-  author    = {Li, Yucheng and Guerin, Frank and Lin, Chenghua},\n244-  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},",
    "numLines": 29
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Grep · `toolu_01F9zBEEYGjrkngtSWJ1gmHU`</summary>

```json
{
  "pattern": "@(article|inproceedings|misc)\\{holland",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "output_mode": "content",
  "-A": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "c13c6257-7fc8-4195-9770-b4170b56f0a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7gXgCqozwWHFd7dceU4HK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1192,
      "cache_read_input_tokens": 39057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1192
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

_source line 24 · 2026-05-21T04:00:42.770Z_

<details><summary>↩ Tool result · `toolu_01F9zBEEYGjrkngtSWJ1gmHU`</summary>

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
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "e32c91d7-e40c-4302-9965-f5bc4960523f",
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

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_01G2JuZYvpEB7TNFM3r1tXmR`</summary>

```json
{
  "pattern": "@(article|inproceedings|misc)\\{(zellers|ets|mh|mantel|bh_fdr|benjamini)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "output_mode": "content",
  "-A": 3,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "9a95150b-f7a9-4769-a0b4-701a59b353a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7gXgCqozwWHFd7dceU4HK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1192,
      "cache_read_input_tokens": 39057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1192
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

_source line 26 · 2026-05-21T04:00:44.548Z_

<details><summary>↩ Tool result · `toolu_01G2JuZYvpEB7TNFM3r1tXmR`</summary>

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
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "c196887d-4a04-4f7a-920f-43f11a22990b",
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

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_011yUZ9wSJ55AwR1aDroR4zp`</summary>

```json
{
  "pattern": "^@",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
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
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "bafe3c04-23aa-41d4-ba06-087f081ac356",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMC2cKLV1JLU6sBkphUi46",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 40249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 28 · 2026-05-21T04:00:48.547Z_

<details><summary>↩ Tool result · `toolu_011yUZ9wSJ55AwR1aDroR4zp`</summary>

```text
5:@inproceedings{balloccu2024leak,
14:@inproceedings{dekoninck2024constat,
22:@inproceedings{golchin2024timetravel,
30:@inproceedings{li2024contamination,
39:@misc{liang2026dvd,
49:@inproceedings{shi2024mink,
57:@inproceedings{tao2026selfcritique,
65:@inproceedings{wang2026fragility,
73:@misc{zhang2024gsm1k,
83:@misc{zhang2024minkpp,
97:@misc{hardy2026scalability,
107:@article{kim2019fpc,
116:@inproceedings{lalor2019irt,
125:@inproceedings{vania2021irt,
134:@misc{li2025atlas,
144:@misc{chen2025irtnet,
154:@misc{choi2026llmjudgeirt,
164:@misc{habba2026growingpains,
174:@inproceedings{zhou2026psnirt,
186:@inproceedings{white2025livebench,
195:@misc{kipnis2024metabench,
205:@inproceedings{hendrycks2021mmlu,
213:@article{liang2023helm,
222:@inproceedings{chiang2024chatbot,
231:@misc{mialon2023gaia,
241:@inproceedings{li2024latesteval,
250:@inproceedings{kiela2021dynabench,
263:@article{belzak2020smallsample,
272:@incollection{holland1988mh,
283:@article{shealy1993sibtest,
292:@article{clauser1998dif,
301:@book{zumbo1999handbook,
310:@article{meredith1993invariance,
319:@article{vandenberg2000invariance,
328:@article{swaminathan1990logistic,
337:@article{teresi2007dif,
346:@book{lord1980irt,
354:@article{raju1988area,
363:@article{muthen1985mimic,
371:@article{woods2009mimic,
383:@article{burnell2023rethink,
392:@article{chang2024survey,
401:@inproceedings{maiapolo2024tinybenchmarks,
409:@inproceedings{wang2024mmlupro,
417:@article{ott2022benchmark,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "5d92c680-3e35-413c-833d-b58a89b2bfb8",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "5:@inproceedings{balloccu2024leak,\n14:@inproceedings{dekoninck2024constat,\n22:@inproceedings{golchin2024timetravel,\n30:@inproceedings{li2024contamination,\n39:@misc{liang2026dvd,\n49:@inproceedings{shi2024mink,\n57:@inproceedings{tao2026selfcritique,\n65:@inproceedings{wang2026fragility,\n73:@misc{zhang2024gsm1k,\n83:@misc{zhang2024minkpp,\n97:@misc{hardy2026scalability,\n107:@article{kim2019fpc,\n116:@inproceedings{lalor2019irt,\n125:@inproceedings{vania2021irt,\n134:@misc{li2025atlas,\n144:@misc{chen2025irtnet,\n154:@misc{choi2026llmjudgeirt,\n164:@misc{habba2026growingpains,\n174:@inproceedings{zhou2026psnirt,\n186:@inproceedings{white2025livebench,\n195:@misc{kipnis2024metabench,\n205:@inproceedings{hendrycks2021mmlu,\n213:@article{liang2023helm,\n222:@inproceedings{chiang2024chatbot,\n231:@misc{mialon2023gaia,\n241:@inproceedings{li2024latesteval,\n250:@inproceedings{kiela2021dynabench,\n263:@article{belzak2020smallsample,\n272:@incollection{holland1988mh,\n283:@article{shealy1993sibtest,\n292:@article{clauser1998dif,\n301:@book{zumbo1999handbook,\n310:@article{meredith1993invariance,\n319:@article{vandenberg2000invariance,\n328:@article{swaminathan1990logistic,\n337:@article{teresi2007dif,\n346:@book{lord1980irt,\n354:@article{raju1988area,\n363:@article{muthen1985mimic,\n371:@article{woods2009mimic,\n383:@article{burnell2023rethink,\n392:@article{chang2024survey,\n401:@inproceedings{maiapolo2024tinybenchmarks,\n409:@inproceedings{wang2024mmlupro,\n417:@article{ott2022benchmark,",
    "numLines": 45
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Let me check for `holland1988mh` (not `holland1988mhdif` as specified in the task). The bib key is `holland1988mh`. Let me also check the `habba2026growingpains` key.

Now let me read the references.bib for the Holland entry to make sure I use the right key.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "3f2e5d69-2bce-4fd1-a925-866c0abe0689",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1GxHDwhC6zayoUjvtN4mK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 40650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 787
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

_source line 30_

Now let me read the method section if it exists, to understand notation already established. Also checking writing_plan.yaml for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "a9d29576-b902-4f29-b809-921214c640d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1GxHDwhC6zayoUjvtN4mK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 40650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 787
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

_source line 31_

<details open><summary>🔧 Tool call — Agent · `toolu_01WPG47LphyN5tF23nLqZUbh`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find method section and writing plan",
  "prompt": "Find and read these files in the project /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/:\n1. Any method section tex file (likely paper/sections/method.tex)\n2. writing_plan.yaml or similar planning files\n3. Any existing section tex files (abstract.tex, introduction.tex, etc.)\n\nRead the full content of any files you find and report them back to me. I need to understand what notation and terminology has been established in earlier sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "483cc56a-fa4b-40b1-8231-0ea7b0a15afb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1GxHDwhC6zayoUjvtN4mK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 40650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 787
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

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Find method section and writing plan",
  "task_type": "local_agent",
  "prompt": "Find and read these files in the project /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/:\n1. Any method section tex file (likely paper/sections/method.tex)\n2. writing_plan.yaml or similar planning files\n3. Any existing section tex files (abstract.tex, introduction.tex, etc.)\n\nRead the full content of any files you find and report them back to me. I need to understand what notation and terminology has been established in earlier sections.",
  "uuid": "b097e79d-f2af-49ad-88f5-14c0ce39ed3c",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

## Round 1

70 recorded events

### User

_source line 33 · 2026-05-21T04:01:02.627Z_

Find and read these files in the project /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/:
1. Any method section tex file (likely paper/sections/method.tex)
2. writing_plan.yaml or similar planning files
3. Any existing section tex files (abstract.tex, introduction.tex, etc.)

Read the full content of any files you find and report them back to me. I need to understand what notation and terminology has been established in earlier sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "9a0014cd-ebf3-44d2-96cb-0938a75441ff"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Finding **/*.tex",
  "usage": {
    "total_tokens": 25393,
    "tool_uses": 1,
    "duration_ms": 1988
  },
  "last_tool_name": "Glob",
  "uuid": "8da293f6-ddde-46e6-93a0-ea6d985c9651",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Glob · `toolu_01NvgQGEwxH76XiGYr2Td7MQ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "f3a7701e-7c4b-4205-9144-dd0d0da0e92c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014aecADdidgy8RM1v5bejTt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25374,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25374,
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

_source line 36 · 2026-05-21T04:01:04.657Z_

<details><summary>↩ Tool result · `toolu_01NvgQGEwxH76XiGYr2Td7MQ`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/paper.tex
artifacts/dream_reports/dream_20260520T194223/median/paper.tex
artifacts/dream_reports/dream_20260520T194223/worst/paper.tex
artifacts/dream_reports/dream_20260520T205007/best/paper.tex
artifacts/dream_reports/dream_20260520T205007/median/paper.tex
artifacts/dream_reports/dream_20260520T205007/worst/paper.tex
artifacts/dream_reports/dream_20260521T012912/best/paper.tex
artifacts/dream_reports/dream_20260521T012912/median/paper.tex
artifacts/dream_reports/dream_20260521T012912/worst/paper.tex
artifacts/dream_reports/dream_20260521T032826/best/paper.tex
artifacts/dream_reports/dream_20260521T032826/worst/paper.tex
paper/math_commands.tex
paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "29bef748-5dff-466f-976d-b06acc061f94"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Finding **/*.yaml",
  "usage": {
    "total_tokens": 25401,
    "tool_uses": 2,
    "duration_ms": 2050
  },
  "last_tool_name": "Glob",
  "uuid": "a7b3d4d8-83fc-46e1-90cb-5d348eaf7d24",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Glob · `toolu_01LPn5KfYLWjGMsVeCwfr13J`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "220aeec0-9255-41c8-b36a-1eb779a5b03e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014aecADdidgy8RM1v5bejTt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25374,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25374,
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

_source line 39 · 2026-05-21T04:01:04.695Z_

<details><summary>↩ Tool result · `toolu_01LPn5KfYLWjGMsVeCwfr13J`</summary>

```text
artifacts/dream_reports/dream_20260520T194223/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/median/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T194223/meta.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260520T205007/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T205007/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T205007/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T205007/best/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/median/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T205007/meta.yaml
artifacts/review_issues.yaml
registry.yaml
artifacts/dream_reports/dream_20260521T012912/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T012912/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T012912/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T012912/best/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/median/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/worst/review_context.yaml
artifacts/dream_reports/dream_20260521T012912/meta.yaml
decisions.yaml
mistakes.yaml
artifacts/dream_reports/dream_20260521T032826/best/imagined_experiments.yaml
writing_plan.yaml
artifacts/dream_reports/dream_20260521T032826/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T032826/worst/imagined_experiments.yaml
literature_map.yaml
artifacts/dream_reports/dream_20260521T032826/best/review_context.yaml
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260521T032826/worst/review_context.yaml
artifacts/dream_reports/dream_20260521T032826/meta.yaml
dream_registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "cab8075b-ee39-487f-966a-f51dbfe4b52c"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 25409,
    "tool_uses": 3,
    "duration_ms": 2202
  },
  "last_tool_name": "Bash",
  "uuid": "ac9b586f-798b-49c1-9bb1-1179660b3e3b",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_011sG9cR6dSN5FDv6CRUt4VZ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "76833f35-27fb-43eb-ae44-ebbb1938c526",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014aecADdidgy8RM1v5bejTt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25374,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25374,
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

_source line 42 · 2026-05-21T04:01:04.886Z_

<details><summary>↩ Tool result · `toolu_011sG9cR6dSN5FDv6CRUt4VZ`</summary>

```text
total 256
drwxr-xr-x  9 ubuntu ubuntu  4096 May 21 04:00 .
drwxrwxr-x  4 ubuntu ubuntu  4096 May 20 17:11 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 17:11 .claude
-rw-r--r--  1 ubuntu ubuntu 13105 May 21 03:59 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 20 17:15 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  3663 May 21 03:45 ROADMAP.md
-rw-r--r--  1 ubuntu ubuntu    90 May 20 21:44 _last_visual_review.json
drwxr-xr-x 27 ubuntu ubuntu  4096 May 21 03:34 artifacts
drwxr-xr-x  2 ubuntu ubuntu 12288 May 21 01:22 checkpoints
-rw-r--r--  1 ubuntu ubuntu     0 May 20 18:50 decisions.lock
-rw-------  1 ubuntu ubuntu 16968 May 21 03:08 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 20 19:42 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 20 19:34 dream_registry.lock
-rw-------  1 ubuntu ubuntu  4205 May 21 04:00 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  4210 May 21 04:00 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 13528 May 20 20:53 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 23:41 figures
-rw-r--r--  1 ubuntu ubuntu     0 May 21 01:40 literature_map.lock
-rw-------  1 ubuntu ubuntu 36148 May 21 03:50 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 20 17:17 logs
-rw-r--r--  1 ubuntu ubuntu  5982 May 21 01:26 memory.md
-rw-r--r--  1 ubuntu ubuntu     0 May 21 03:15 mistakes.lock
-rw-------  1 ubuntu ubuntu  1217 May 21 03:15 mistakes.yaml
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 03:58 paper
-rw-r--r--  1 ubuntu ubuntu 16017 May 21 03:41 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu     0 May 20 17:16 registry.lock
-rw-------  1 ubuntu ubuntu 25586 May 21 01:22 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  2624 May 21 01:22 report.md
-rwxr-xr-x  1 ubuntu ubuntu     0 May 20 17:12 study_status.lock
-rw-r--r--  1 ubuntu ubuntu 40194 May 21 03:46 writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "458392d5-11e2-468a-8816-4e15ae278a22"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 28393,
    "tool_uses": 4,
    "duration_ms": 6090
  },
  "last_tool_name": "Bash",
  "uuid": "f959dc3f-0128-415e-89da-cebf0e367662",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_012RGyXizhiSzu86Zhc7ehNK`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper -type f -name \"*.tex\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "23a5b876-5694-4df5-b15e-9b26da4f8849",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WRxec1Y5VoHUvNyP78T1o7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2978,
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

_source line 45 · 2026-05-21T04:01:08.770Z_

<details><summary>↩ Tool result · `toolu_012RGyXizhiSzu86Zhc7ehNK`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "1e4f255d-f245-4659-a0bf-f5cfb464d9cc"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Reading writing_plan.yaml",
  "usage": {
    "total_tokens": 28394,
    "tool_uses": 5,
    "duration_ms": 6150
  },
  "last_tool_name": "Read",
  "uuid": "8e3695ba-3a30-4328-b3a9-8cc3fc13b43b",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_0157HqaYxBigbEBwrTKrBZBW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "ef9b700a-5788-4463-92b3-1940ac9ffdc0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WRxec1Y5VoHUvNyP78T1o7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2978,
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

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Reading paper/main.tex",
  "usage": {
    "total_tokens": 28395,
    "tool_uses": 6,
    "duration_ms": 6326
  },
  "last_tool_name": "Read",
  "uuid": "2c9937c3-c213-4ecb-b289-d37fa03aed8d",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01QGegfGjD5sfEcUyrdwEfw9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "1c93b380-1355-4535-ae85-7007acb73730",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WRxec1Y5VoHUvNyP78T1o7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2978,
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

_source line 50 · 2026-05-21T04:01:08.961Z_

<details><summary>↩ Tool result · `toolu_01QGegfGjD5sfEcUyrdwEfw9`</summary>

```text
1	\documentclass{article}
2	\usepackage{iclr2026_conference,times}
3	\input{math_commands.tex}
4	
5	\usepackage{hyperref}
6	\usepackage{url}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{microtype}
11	\usepackage{multirow}
12	\usepackage{subcaption}
13	\usepackage{cleveref}
14	
15	\graphicspath{{../figures/paper/}}
16	
17	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
18	
19	%\iclrfinalcopy
20	
21	\newcommand{\fix}{\marginpar{FIX}}
22	\newcommand{\new}{\marginpar{NEW}}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\bibliography{references}
37	\bibliographystyle{iclr2026_conference}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "7035e287-886a-4c8e-b744-031266ddab60"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T04:01:09.125Z_

<details><summary>↩ Tool result · `toolu_0157HqaYxBigbEBwrTKrBZBW`</summary>

```text
1	meta:
2	  venue: ICLR 2027
3	  track: main
4	  template: ""
5	  template_note: "ICLR 2027 template not yet available locally; will download or reuse iclr2025 when entering Step 2"
6	  page_limit: 9
7	  deadline: "2026-10-01"
8	  core_claim: >-
9	    Applying DIF to MMLU (5,227 models × 12,508 items) reveals 38% item-level
10	    functional instability across model generations, exposes a fundamental gap
11	    in contamination ground truth labels, and provides a semi-synthetic
12	    validation framework for item-level detectors.
13	  created_at: "2026-05-20T23:45:00Z"
14	  story_arc:
15	    hook: >-
16	      When we say "Model B outperforms Model A on MMLU," we assume temporal
17	      comparability — but 38% of MMLU items function differently across model
18	      generations.
19	    gap: >-
20	      Existing contamination labels (web-overlap, n-gram) measure global
21	      exposure, not differential item functioning — every validation study
22	      using these labels has a blind spot. This is a fundamental validation
23	      methodology gap affecting the entire contamination detection field.
24	    insight: >-
25	      DIF detects differential contamination (semi-synthetic ΔTPR=+0.508) but
26	      temporal DIF is dominated by genuine capability evolution
27	      (enrichment≈1.0, within-subject C%=38.1%), and three structural
28	      corrections cannot separate them.
29	    mechanism: >-
30	      Semi-synthetic injection into real response matrices provides controlled
31	      ground truth; cross-subject matching eliminates FPR inflation (ΔFPR=0.000).
32	    evidence: >-
33	      38% items functionally unstable (plan_001/014); ΔTPR=+0.508 at p=0.5
34	      (plan_011); ΔFPR=0.000 cross-subject (plan_016); three improvements
35	      exhausted (plan_001b/012/014).
36	
37	paper_outline:
38	  - section: abstract
39	    word_budget: 200
40	    core_bullets:
41	      - >-
42	        Problem: LLM benchmark scores assume temporal comparability, but
43	        item-level behavior may drift across model generations
44	      - >-
45	        Approach: Apply MH-DIF with ETS classification to METABENCH
46	        (5,227 models × 12,508 MMLU items)
47	      - >-
48	        Finding 1: 31–38% items functionally unstable across generations
49	        (31.3% temporal cohort primary, within-subject 31-45% avg 38.1%)
50	        — genuine capability evolution, not statistical artifact (sanity
51	        check 0.18%). [Architecture-stratified TBD: plan_010 running]
52	      - >-
53	        Finding 2: Web-overlap contamination labels do not capture
54	        differential contamination (enrichment≈1.0); semi-synthetic
55	        injection confirms DIF detection power (ΔTPR=+0.508 at p=0.5).
56	        Validation methodology gap affects entire field.
57	      - >-
58	        Finding 3: Semi-synthetic validation framework with cross-subject
59	        matching (ΔFPR=0.000) as reusable infrastructure; GSM8K replication
60	        confirms cross-benchmark portability (ΔTPR=+0.818)
61	      - >-
62	        Finding 4: DIF-flagged items concentrate cross-generational
63	        discriminative information — removing them disrupts rankings MORE
64	        than random removal (z=-8 to -49σ), while overall rankings stay
65	        robust (ρ>0.996). Cross-benchmark validation: DIF flags
66	        anti-correlate with GSM1K contamination gap (r=−0.478, 95%
67	        CI=[−0.71, −0.16], p=0.005) — DIF-C items resist contamination-
68	        based performance gains (suggestive, N=33).
69	        DIF is diagnostic lens, not item filter.
70	    dependencies: [experiments, method, discussion]
71	    registry_refs:
72	      - plan_001_real_data_dif_mmlu
73	      - plan_011_semi_synthetic_validation
74	      - plan_014_within_subject_dif
75	      - plan_016_within_subject_semi_synthetic
76	      - plan_017_downstream_impact
77	      - plan_004_gsm8k_cross_benchmark
78	
79	  - section: introduction
80	    word_budget: 1200
81	    core_bullets:
82	      - >-
83	        Hook: MMLU scores are treated as directly comparable across time —
84	        but 31% of items behave differently for 2024 vs 2023 model
85	        cohorts (ETS C DIF), persisting within every subject domain
86	        (31-45%, avg 38.1%)
87	      - >-
88	        Gap: Contamination detection research validates against web-overlap
89	        labels, but these measure global exposure, not differential item
90	        functioning — a fundamental validation methodology gap. All work
91	        using web-overlap/n-gram labels as ground truth for item-level
92	        detectors (including Min-K%, n-gram methods) has the same blind
93	        spot.
94	      - >-
95	        Insight: Applying classical psychometric DIF to LLM benchmarks
96	        reveals that item-level behavioral differences are pervasive and
97	        structural — three correction attempts (matched-ability,
98	        θ-conditioning, bifactor pre-check) all fail, pointing to genuine
99	        capability evolution as the dominant source
100	      - >-
101	        Tension resolution (Dream #3, MUST address in §1 end): "31%
102	        items unstable" sounds alarming but "ρ=0.997 ranking correlation"
103	        sounds reassuring. Resolve upfront: instability is real but
104	        concentrated in redundant measurement → benchmark robust at
105	        ranking level, fragile at item level. This is precisely why DIF
106	        is a diagnostic lens (understand what changed) not a quality
107	        filter (remove bad items).
108	      - >-
109	        Discovery process (anti-post-hoc framing): "We initially
110	        hypothesized DIF could detect contaminated items. Three structural
111	        improvements failed to separate contamination from capability
112	        evolution. This led us to investigate what persistent DIF actually
113	        captures." Pivot was data-driven: plan_011 semi-synthetic success
114	        (ΔTPR=+0.508) proved DIF works but ground truth labels don't —
115	        triggering problem redefinition. New evidence (plan_017 z=-49σ,
116	        plan_004 r=−0.478) came from post-pivot experiments, not
117	        reinterpretation of old data.
118	      - >-
119	        Novelty statement (MUST be explicit per Dream #3): We do not
120	        modify MH-DIF itself. Our novelty: (a) unprecedented scale
121	        (5,227 models) creates statistical challenges absent in
122	        educational testing; (b) cross-subject matching innovation
123	        eliminates FPR inflation; (c) ground truth meta-critique
124	        exposing validation methodology gap; (d) largest empirical
125	        characterization of item-level benchmark behavior.
126	      - >-
127	        Contributions: (C1) Benchmark temporal comparability concern —
128	        31% functional instability as empirical finding; (C2) Ground
129	        truth meta-critique — validation methodology gap in contamination
130	        detection literature; (C3) Semi-synthetic validation framework
131	        with cross-subject matching; (C4) DIF items concentrate
132	        discriminative information — diagnostic lens, not item filter
133	    dependencies: [experiments]
134	    figures: [fig_1_global_vs_differential]
135	    citation_hints:
136	      - "METABENCH dataset citation"
137	      - "Li et al. (EMNLP 2024) web-overlap labels"
138	      - "Wang et al. (ICLR 2026) RL fragility — motivates psychometric approach"
139	      - "Growing Pains (Habba et al., NOT Polo) — positioning: they do score comparability, we do temporal stability characterization"
140	
141	  - section: related_work
142	    word_budget: 800
143	    core_bullets:
144	      - >-
145	        Cluster 1: Contamination detection methods (Min-K%, ConStat, DVD,
146	        Self-Critique, n-gram baselines) — all validate against global
147	        exposure labels, not differential contamination; our meta-critique
148	        applies to their validation methodology
149	      - >-
150	        Cluster 2: IRT in LLM evaluation (Growing Pains [Habba et al.],
151	        PSN-IRT [Zhou et al.], Hardy scalability, Lalor 2019, Vania
152	        2021) — DEDICATED technical comparison with Growing Pains: they
153	        use anchor items for efficient extensible evaluation; our DIF
154	        diagnostic tells them WHICH anchor items are degrading across
155	        model generations. Mutual value: their framework + our
156	        diagnostic = monitored extensible evaluation. Complementary not
157	        competing. (R2-W2)
158	      - >-
159	        Cluster 3: DIF methodology — MH-DIF (Holland & Thayer 1988), ETS
160	        classification, non-uniform DIF (Swaminathan & Rogers 1990),
161	        IRT-based alternatives (Lord's χ², Raju's area), SIBTEST (Shealy
162	        & Stout 1993), logistic regression DIF (Clauser & Mazor 1998,
163	        Zumbo 1999), small-sample DIF (Belzak 2020), propensity score
164	        matching for DIF (Teresi 2007). Our application context is novel;
165	        method itself is established; we acknowledge impact-vs-DIF
166	        confound as central challenge.
167	      - >-
168	        Cluster 4: Measurement invariance (Meredith 1993, Vandenberg &
169	        Lance 2000) — DIF is item-level test of measurement invariance;
170	        our work is the first large-scale measurement invariance analysis
171	        of LLM benchmarks. Frame DIF within broader invariance testing
172	        tradition.
173	      - >-
174	        Cluster 5: Benchmark design and concurrent work (LiveBench,
175	        GAIA, Chatbot Arena, dynamic benchmarks) — we characterize
176	        existing benchmarks psychometrically, they build new ones or
177	        use alternative evaluation paradigms
178	    dependencies: [introduction]
179	
180	  - section: method
181	    word_budget: 1400
182	    core_bullets:
183	      - >-
184	        3.1 Data: METABENCH response matrix (5,227 × 12,508) + Li et al.
185	        web-overlap labels (73.8% coverage, 9,229 items)
186	      - >-
187	        3.2 MH-DIF + ETS A/B/C classification — translate for ML audience:
188	        examinees→models, test items→benchmark questions, DIF→item-level
189	        behavioral anomaly conditional on ability. ETS thresholds: A
190	        (|Δ|<1.0), B (1.0≤|Δ|<1.5), C (|Δ|≥1.5)
191	      - >-
192	        3.3 Cohort designs: temporal (2023 vs 2024, N=1253/656),
193	        ability-quintile (Q1-2 vs Q4-5), within-family (Llama-2 N=161 vs
194	        Llama-3 N=308), within-subject (per-MMLU-subject DIF)
195	      - >-
196	        3.4 Semi-synthetic injection framework: select baseline-clean
197	        items (ETS A in uninjected data), inject contamination by flipping
198	        focal-group incorrect→correct responses at rate p ∈ {0.3,0.5,0.7,1.0},
199	        measure ΔTPR = TPR(injected) - TPR(baseline). Cross-subject
200	        matching: use total score on OTHER subjects as matching variable,
201	        avoiding matching variable contamination.
202	      - >-
203	        3.5 Diagnostics: Yen's Q3 for local independence, domain-specificity
204	        analysis (Spearman ρ between C% and accuracy improvement by subject)
205	      - >-
206	        3.6 Multiple testing considerations (Dream #3 required): ETS
207	        classification provides implicit protection via dual threshold
208	        (effect size |Δ_MH|≥1.5 AND significance p<0.05). BH FDR q=0.05
209	        correction removes only 3/3918 items (31.32%→31.30%) — ETS dual
210	        threshold already controls FPR. Random-split sanity check
211	        (C%=0.18%). Threshold sensitivity: C%=48.9% at 1.0, 31.3% at
212	        1.5 (standard), 18.3% at 2.0, 10.2% at 2.5. "Finding robust
213	        at standard thresholds; even at conservative 2.5, 1,278 items
214	        still exhibit large DIF." (plan_018). Architecture
215	        heterogeneity: non-issue (plan_010, 99.98% decoder-only).
216	    dependencies: []
217	    notation_table:
218	      θ: "latent ability (IRT)"
219	      Δ_MH: "Mantel-Haenszel DIF statistic (log-odds ratio)"
220	      p: "exploitation rate in semi-synthetic injection"
221	      "C%": "percentage of items classified ETS C (large DIF)"
222	      ΔTPR: "TPR increase from injection over baseline"
223	      ΔFPR: "FPR change from injection (should be 0 for valid framework)"
224	
225	  - section: experiments
226	    word_budget: 2500
227	    core_bullets:
228	      - >-
229	        4.1 Validation: DIF works under controlled conditions — power
230	        analysis with real MMLU IRT parameters, ETS C TPR=0.68-0.80 at
231	        N≥80 δ≥1.4, FPR=0.036-0.042, AUC 0.93-0.94
232	      - >-
233	        4.2 Temporal comparability concern: 31.3% ETS C (temporal,
234	        primary estimate; BH-corrected 31.30%), sanity random split
235	        0.18%, within-family Llama-2v3 61.3% (ability confound),
236	        ability-quintile 2.9% (well-controlled), domain ρ=0.307
237	        (p=0.02). Within-subject C%=38.1% (31-45% across 5 subjects)
238	        — instability penetrates within every domain. Instability
239	        decomposition (plan_019): ρ=0.307 is ecological correlation;
240	        item-level domain improvement explains only 2.4pp of 31.3%
241	        (pseudo R²=0.0007, counterfactual C%=29.0%). 92.4% of
242	        instability is unrelated to domain accuracy improvement.
243	        Use Model 1 (no causal assumptions) as primary; Model 2
244	        shows Simpson's paradox (supplementary).
245	        Architecture heterogeneity (plan_010): non-issue — METABENCH
246	        MMLU is 99.98% decoder-only (5226/5227), excluding the 1
247	        non-decoder model yields C%=31.32% (Jaccard=1.0 with full
248	        population). IRT person-fit (98% |Lz|>2) reflects MMLU's
249	        57-subject multidimensionality, not architecture heterogeneity.
250	      - >-
251	        4.3 Ground truth mismatch: enrichment=0.96 against Li et al.
252	        web-overlap labels; semi-synthetic ΔTPR=+0.508 (p=0.5), +0.674
253	        (p=1.0), clear dose-response; DIF WORKS for differential
254	        contamination but Li et al. labels are the wrong ground truth
255	      - >-
256	        4.4 Structural analysis — empirical observation that three
257	        structural improvements fail: (a) matched-ability enrichment
258	        0.94-1.04 (main text 1 sentence → Appendix A.x for detail),
259	        (b) θ-conditioning r=0.9986 FPR unchanged at 31% (Appendix A.y
260	        "Structural Constraints"), (c) within-subject pre-check C%=38.1%
261	        (bifactor not viable). Frame as: jointly constraining DIF utility,
262	        not formal impossibility. [Reviewer allocation: plan_001b main=1
263	        sentence, plan_012 appendix-only]
264	      - >-
265	        4.5 Semi-synthetic framework validation: cross-subject matching
266	        ΔFPR=0.000 all 5 subjects, 4/5 ΔTPR>0.3 at p=0.5 (cross), vs
267	        within-subject FPR inflation +0.186. Cross-subject matching as
268	        methodological recommendation.
269	      - >-
270	        4.6 Q3 local independence: 11.3% within-subject pairs >0.20 vs
271	        2.2% cross-subject (5x, p=2.3e-9); mild local dependence,
272	        contributing factor but not main FPR driver
273	      - >-
274	        4.7 Downstream impact — four layers: (1) Benchmark redundancy:
275	        ρ≈0.997 full vs stable-only, rankings extremely robust to 31%
276	        removal; (2) DIF items carry more signal than average items
277	        (z=-8 to -49σ vs random, 21/21), BUT circularity ablation
278	        (plan_020) shows DIF is the LEAST disruptive non-random strategy:
279	        high-discrimination z=-15.8, accuracy-gap z=-156.5, high-variance
280	        z=-107.9 vs DIF z=-9.5. DIF specifically isolates ability-
281	        conditioned differential behavior, not just generally informative
282	        items. DIF-discrimination Jaccard=0.12 (orthogonal constructs).
283	        DO NOT simultaneously claim "signal carriers" and "conservative
284	        filter" — use: "DIF items carry more signal than average but
285	        DIF isolates differential behavior specifically."
286	        (3) DIF as diagnostic lens: identifies which capability
287	        dimensions drive ranking shifts across generations. Model-specific
288	        patterns (phi-3/llama-3 +700-850, mistral merges -400 to -587)
289	        but caveat: top-50 movers 49/50 "unknown" family;
290	        (4) Cross-benchmark validation: GSM1K contamination gap
291	        anti-correlates with DIF advantage (r=−0.478, 95% CI=[−0.71,
292	        −0.16], p=0.005) — DIF-C items resist contamination-based
293	        performance gains (N=33, partial r=−0.385 controlling accuracy,
294	        permutation p=0.014). Suggestive not conclusive; item difficulty
295	        confound cannot be fully excluded at N=33.
296	      - >-
297	        4.8 Cross-benchmark validation (GSM8K, 1,319 items × 6,702 models):
298	        Three-part analysis. (a) Temporal DIF: C%=18.9% (standard matching),
299	        sanity 0.3% — instability is lower than MMLU (31.3%) but still
300	        substantial for a single-domain benchmark. (b) Semi-synthetic:
301	        ΔTPR=+0.818 (standard, p=0.7), +0.517 (external, p=0.7); dose-
302	        response confirmed; framework generalizes beyond MMLU.
303	        (c) GSM1K contamination gap correlation: DIF-C items anti-correlate
304	        with contamination gap (r=−0.478, 95% CI=[−0.71, −0.16], p=0.005;
305	        partial r=−0.385 controlling accuracy; permutation p=0.014, N=33).
306	        MUST honestly report: original hypothesis predicted POSITIVE
307	        correlation (contaminated models gain on DIF items); observed
308	        NEGATIVE direction — DIF-C items resist contamination-based gains.
309	        Suggestive at N=33; item difficulty confound not fully excluded.
310	        [Reviewer: 1 paragraph + fig_5, honest hypothesis vs result]
311	    dependencies: []
312	    registry_refs:
313	      - mvp_dif_power_sim
314	      - mvp_dif_power_sim_phase2
315	      - plan_001_real_data_dif_mmlu
316	      - plan_001b_matched_ability_dif
317	      - plan_011_semi_synthetic_validation
318	      - plan_012_irt_theta_conditioning
319	      - plan_013_q3_local_independence
320	      - plan_014_within_subject_dif
321	      - plan_016_within_subject_semi_synthetic
322	      - plan_017_downstream_impact
323	      - plan_018_ets_threshold_sensitivity
324	      - plan_019_instability_decomposition
325	      - plan_010_architecture_stratified_dif
326	      - plan_020_circularity_ablation
327	      - plan_004_gsm8k_cross_benchmark
328	    tables: [tab_1_temporal_landscape, tab_2_structural_comparison]
329	    figures: [fig_2_dose_response, fig_3_within_subject_matching, fig_4_downstream_impact, fig_5_gsm1k_dif_correlation]
330	
331	  - section: discussion
332	    word_budget: 1000
333	    core_bullets:
334	      - >-
335	        5.1 Implications for benchmark temporal comparability: 31%
336	        instability (robust across thresholds: 10-49% at ETS 2.5-1.0)
337	        means cross-temporal MMLU scores carry uncontrolled item-level
338	        variance; instability decomposition shows 92.4% unrelated to
339	        domain accuracy improvement; benchmark designers should monitor
340	        DIF as quality diagnostic
341	      - >-
342	        5.2 Ground truth meta-critique — AGGRESSIVE framing per Director:
343	        all work validating item-level detectors against web-overlap/n-gram
344	        labels has the same validation methodology gap. Web-overlap measures
345	        existence, not differential usage. This is a meta-contribution to
346	        the contamination detection field — not just "DIF and Li et al.
347	        measure different things" but "the field's standard validation
348	        approach is fundamentally mismatched for item-level detection."
349	      - >-
350	        5.3a DIF as capability diagnostic (Claim 4 layer 4 discussion):
351	        GSM1K negative correlation reveals contamination produces "shallow"
352	        performance boost concentrated on non-DIF items, while DIF-C items
353	        capture genuine capability differences between model generations.
354	        171/249 focal-favoring DIF-C items (α<1) drive the effect — these
355	        are items where 2024 models genuinely improved, and contaminated
356	        models struggle disproportionately on them. MUST caveat: r=−0.478
357	        with CI=[−0.71, −0.16] is suggestive; item difficulty confound
358	        (DIF-C items may simply be harder) not fully excluded; N=33 limits
359	        generalizability. This is a paper highlight per Director but
360	        requires honest strength calibration.
361	      - >-
362	        5.3b Empirical observation on DIF applicability: 1D IRT fit
363	        limitations + power requirements + ability confounding jointly
364	        constrain DIF utility in LLM benchmarks. This is a structural
365	        constraint revealed by systematic experimentation, NOT a formal
366	        impossibility — higher-level methods (MIMIC, propensity-score
367	        matching, multidimensional IRT) may address individual constraints.
368	      - >-
369	        5.4 Limitations — MUST BE HONEST, non-negotiable:
370	        (a) ρ=0.307 ecological correlation between C% and accuracy
371	        improvement, but item-level decomposition (plan_019) shows
372	        domain improvement explains only 2.4pp (7.6%) of 31.3% C%.
373	        Still, cannot fully decompose remaining 92.4% into
374	        contamination vs other sources of capability change;
375	        (b) 38% C% cannot be decomposed into contamination vs capability;
376	        (c) semi-synthetic injection (incorrect→correct flipping) may
377	        not match real contamination patterns (partial knowledge, format
378	        memorization);
379	        (d) primarily MMLU/METABENCH — GSM8K cross-validation (§4.8)
380	        confirms semi-synthetic framework portability and provides GSM1K
381	        correlation evidence (N=33), but full temporal DIF characterization
382	        on diverse benchmarks not yet done; GSM1K N=33 has wide CI;
383	        (e) cross-subject baseline FPR 33-53% — stable across injection
384	        levels but not low;
385	        (f) RL robustness: theoretically motivated but empirically
386	        unvalidated with adequate sample size (N=13 reasoning-RL models
387	        in METABENCH);
388	        (g) downstream impact family analysis limited to N≥20 families
389	        (llama, mistral, qwen, phi); top-50 rank movers 49/50 are
390	        "unknown" family — family-level conclusions have limited coverage
391	      - >-
392	        5.5 Future work (SCOPE REDUCED per Dream #3 — main text only
393	        lists directions, no extended discussion): broader cross-
394	        benchmark generalization, RL model cohorts with adequate N,
395	        MIMIC models for confound control. [Appendix-only: Bayesian DIF,
396	        ensemble fusion (DIF + ConStat + DVD), complementary baselines,
397	        pilot studies (bifactor equating, item generation), SIBTEST/LR-DIF
398	        comparison, item-focused trees]
399	    dependencies: [experiments]
400	
401	  - section: conclusion
402	    word_budget: 350
403	    core_bullets:
404	      - >-
405	        Four contributions: (1) 38% MMLU items functionally unstable
406	        across model generations, (2) ground truth meta-critique —
407	        validation methodology gap in contamination detection, (3)
408	        semi-synthetic framework with cross-subject matching (cross-
409	        benchmark replication on GSM8K: ΔTPR=+0.818), (4) DIF as
410	        diagnostic lens — four-layer finding
411	      - >-
412	        Key message: LLM benchmarks need psychometric monitoring, not
413	        just score reporting — DIF reveals benchmark quality as a
414	        benchmark quality tool
415	      - >-
416	        DIF items concentrate discriminative information (removal disrupts
417	        rankings MORE than random, z=-8 to -49σ) and anti-correlate with
418	        contamination gap (r=−0.478, CI=[−0.71, −0.16]) — DIF-C items
419	        resist contamination-based performance gains (suggestive, N=33)
420	    dependencies: [experiments, discussion]
421	
422	visualization_plan:
423	  - fig_id: fig_1_global_vs_differential
424	    type: conceptual
425	    tool: paperbanana
426	    description: >-
427	      Global vs Differential contamination concept diagram with ICC
428	      illustration — global exposure affects all models equally (no DIF),
429	      differential training data inclusion creates group-specific ICC
430	      shifts (DIF detected). Shows why enrichment≈1.0 is expected.
431	    narrative_intent: >-
432	      Web-overlap labels and DIF measure fundamentally different things:
433	      global exposure vs differential item functioning. Low enrichment is
434	      expected, not failure.
435	    design_notes:
436	      - >-
437	        Left panel: "Global Contamination" — item on Common Crawl since
438	        2020, both cohort ICCs overlap (no DIF), Li et al. labels it
439	        contaminated but DIF correctly reports no group difference
440	      - >-
441	        Right panel: "Differential Contamination" — item in focal
442	        cohort's training data only, ICCs diverge (DIF detected), Li
443	        et al. may or may not label it
444	      - >-
445	        Use ICC curves (S-shaped logistic) with shaded area between
446	        curves = DIF magnitude (Δ_MH)
447	      - "Color: reference cohort blue, focal cohort orange (Okabe-Ito)"
448	      - >-
449	        Bottom annotation connecting panels: "Enrichment ≈ 1.0 because
450	        most MMLU items are globally contaminated (left), not
451	        differentially (right)"
452	    placement: introduction
453	    aspect_ratio: "16:9"
454	
455	  - fig_id: fig_2_dose_response
456	    type: statistical
457	    tool: matplotlib
458	    description: >-
459	      Semi-synthetic dose-response: TPR vs exploitation rate p for
460	      temporal cohort with external/cross-subject matching, plus FPR
461	      stability panel
462	    narrative_intent: >-
463	      DIF detection power increases monotonically with contamination
464	      exploitation rate (clear dose-response), and cross-subject matching
465	      maintains perfectly stable FPR (ΔFPR=0.000) — controlled detection
466	      capability confirmed.
467	    design_notes:
468	      - "x-axis: exploitation rate p ∈ {0, 0.3, 0.5, 0.7, 1.0}"
469	      - >-
470	        Top panel: TPR lines — temporal_external (primary, solid blue),
471	        temporal_standard (dashed red, shows FPR inflation problem at
472	        high p)
473	      - >-
474	        Bottom panel (smaller): FPR vs p — external flat at ~0.31
475	        (ΔFPR=0.000), standard inflating from 0.30 to 0.62
476	      - "Pattern A: light regime band at p<0.3 labeled 'below practical detection'"
477	      - "Dashed horizontal lines at baseline TPR (p=0) for reference"
478	      - "Annotate ΔTPR=+0.508 at p=0.5 on the primary line"
479	    data_source: "registry: plan_011_semi_synthetic_validation"
480	    placement: experiments
481	    aspect_ratio: "3:4"
482	
483	  - fig_id: fig_3_within_subject_matching
484	    type: statistical
485	    tool: matplotlib
486	    description: >-
487	      Within-subject semi-synthetic: 5 subjects comparing cross-subject
488	      vs within-subject matching on ΔTPR and ΔFPR
489	    narrative_intent: >-
490	      Cross-subject matching eliminates FPR inflation (ΔFPR=0.000 for
491	      all 5 subjects) while maintaining detection power — a practical
492	      methodological recommendation.
493	    design_notes:
494	      - >-
495	        Paired dot plot or grouped bars: 5 subjects on x-axis, sorted
496	        by cross-subject ΔTPR
497	      - >-
498	        Left panel: ΔTPR at p=0.5 — cross (filled circle) vs within
499	        (open circle), connected by line
500	      - >-
501	        Right panel: ΔFPR — cross all at 0.000 (flat line), within
502	        showing inflation (+0.067 to +0.281)
503	      - "Reference line: ΔTPR=0.3 (success threshold), ΔFPR=0"
504	      - >-
505	        Highlight business_ethics: high baseline FPR (0.53-0.56),
506	        negative within-subject ΔTPR, low cross-subject ΔTPR — the
507	        failure case
508	    data_source: "registry: plan_016_within_subject_semi_synthetic"
509	    placement: experiments
510	    aspect_ratio: "3:2"
511	
512	  - fig_id: fig_4_downstream_impact
513	    type: statistical
514	    tool: matplotlib
515	    description: >-
516	      Model-level rank change scatter: full-benchmark rank vs
517	      stable-only rank, showing that DIF removal systematically
518	      disrupts rankings more than random removal. Annotate key model
519	      clusters (phi-3/llama-3 beneficiaries, mistral merge losers).
520	    narrative_intent: >-
521	      DIF-flagged items concentrate cross-generational discriminative
522	      information — removing them disrupts rankings MORE than random
523	      removal, revealing model-specific evolution patterns rather than
524	      benchmark noise.
525	    design_notes:
526	      - >-
527	        Scatter plot: x = full-benchmark rank, y = stable-only rank.
528	        Diagonal line (y=x) = no change. Points above = gained rank
529	        (benefited from DIF items), below = lost rank.
530	      - >-
531	        Color by model family or cohort (2023 blue, 2024 orange) if
532	        feasible; otherwise uniform gray with key models highlighted
533	      - >-
534	        Annotate clusters: phi-3 / llama-3 derivatives (large positive
535	        rank change, +700-850), mistral merges (large negative, -400
536	        to -587)
537	      - >-
538	        Inset or annotation box: ρ_full_vs_stable = 0.996, z_dif_vs_random
539	        = -14.9 (mean), DIF items 1.09× cross-cohort ratio
540	      - "Reference diagonal dashed line y=x"
541	      - "Alternative: if scatter too dense, use hexbin or contour"
542	    data_source: "registry: plan_017_downstream_impact"
543	    placement: experiments
544	    aspect_ratio: "4:3"
545	
546	  - fig_id: fig_5_gsm1k_dif_correlation
547	    type: statistical
548	    tool: matplotlib
549	    description: >-
550	      GSM1K contamination gap vs DIF advantage scatter: 33 matched models,
551	      showing significant negative correlation (r=−0.478, p=0.005).
552	      Models with higher contamination (GSM8K−GSM1K gap) perform WORSE
553	      on DIF-C items — DIF captures capability, not contamination.
554	    narrative_intent: >-
555	      Cross-benchmark validation of Claim 4's "DIF as diagnostic lens":
556	      contaminated models cannot fake performance on DIF items, which
557	      capture genuine capability-discriminative differences. The negative
558	      correlation inverts the contamination narrative.
559	    design_notes:
560	      - >-
561	        Scatter: x = GSM8K−GSM1K contamination gap, y = DIF advantage
562	        (acc_DIF_C − acc_non_DIF). Regression line with 95% CI band.
563	      - >-
564	        Color by model family (Phi green, Gemma orange, Llama blue,
565	        Mixtral purple, DeepSeek red, Other gray)
566	      - "Annotate: r=−0.478, p=0.005 (partial r=−0.385 ctrl accuracy)"
567	      - "Annotate key outlier: Deepseek-math-7b-rl (near zero on both)"
568	      - >-
569	        Dashed horizontal line at DIF advantage = 0; most models below
570	        (DIF items are harder for all, but contaminated models worse)
571	      - "Already generated by Agent Worker — may need style refinement"
572	    data_source: "registry: plan_004_gsm8k_cross_benchmark, artifacts/plan_004/gsm1k_dif_correlation.csv"
573	    placement: experiments
574	    aspect_ratio: "4:3"
575	    source_file: "artifacts/plan_004/fig_gsm1k_dif_correlation.pdf"
576	
577	  - fig_id: fig_A1_subject_heatmap
578	    type: statistical
579	    tool: matplotlib
580	    description: >-
581	      Per-subject ETS C percentage for all 57 MMLU subjects (temporal
582	      cohort), showing pervasiveness of item instability
583	    narrative_intent: >-
584	      Item instability is pervasive across all MMLU subjects, not
585	      concentrated in a few — temporal DIF is a benchmark-wide phenomenon.
586	    design_notes:
587	      - "Horizontal bar chart sorted by C%, all 57 subjects"
588	      - >-
589	        Color-coded by domain group (STEM / humanities / social science
590	        / other) to show whether instability clusters by domain
591	      - "Vertical dashed line at overall mean C% (31.3%)"
592	      - >-
593	        Annotate subjects with known capability jumps (e.g.,
594	        abstract_algebra, college_mathematics)
595	    data_source: "registry: plan_001_real_data_dif_mmlu"
596	    placement: appendix
597	    aspect_ratio: "1:2"
598	
599	  - fig_id: fig_A2_q3_distribution
600	    type: statistical
601	    tool: matplotlib
602	    description: >-
603	      Q3 residual correlation distribution: within-subject vs
604	      cross-subject pairs
605	    narrative_intent: >-
606	      Local dependence exists (11.3% within-subject pairs exceed 0.20)
607	      but is mild — a contributing factor, not the main FPR driver.
608	    design_notes:
609	      - >-
610	        Overlapping density plot: within-subject Q3 (blue) vs
611	        cross-subject Q3 (orange)
612	      - "Vertical dashed line at |Q3|=0.20 threshold"
613	      - "Annotate: 11.3% vs 2.2% above threshold (5x ratio)"
614	      - "Inset text: Mann-Whitney p=2.3e-9"
615	    data_source: "registry: plan_013_q3_local_independence"
616	    placement: appendix
617	    aspect_ratio: "4:3"
618	
619	table_plan:
620	  - table_id: tab_1_temporal_landscape
621	    caption: >-
622	      DIF detection results across cohort definitions on METABENCH MMLU
623	      (5,227 models × 12,508 items). ETS C = large DIF (|Δ_MH| ≥ 1.5).
624	    placement: experiments
625	    type: comparison
626	    columns:
627	      - Cohort Definition
628	      - N_ref / N_focal
629	      - "ETS C (%)"
630	      - "FPR (Li clean)"
631	      - Enrichment
632	    data_source: "registry: plan_001_real_data_dif_mmlu, plan_014_within_subject_dif"
633	    notes: >-
634	      Rows: temporal (2023 vs 2024), ability-quintile (Q1-2 vs Q4-5),
635	      within-family (Llama-2 vs Llama-3), random split (sanity check),
636	      within-subject average (5 subjects). Highlight contrast: sanity
637	      0.18% vs temporal 31.3%. Within-subject 38.1% proves instability
638	      penetrates within domains.
639	
640	  - table_id: tab_2_structural_comparison
641	    caption: >-
642	      Three structural improvement attempts and their outcomes. None
643	      reduces temporal baseline FPR below 31%.
644	    placement: experiments
645	    type: comparison
646	    columns:
647	      - Approach
648	      - Mechanism
649	      - Temporal FPR
650	      - "TPR (p=0.5)"
651	      - Outcome
652	    data_source: "registry: plan_001b_matched_ability_dif, plan_012_irt_theta_conditioning, plan_014_within_subject_dif"
653	    notes: >-
654	      Rows: baseline (plan_011 external matching), matched-ability
655	      quintiles (plan_001b), IRT θ-conditioning (plan_012), within-subject
656	      pre-check (plan_014). Frame as "empirical observation revealing
657	      structural constraint" not "our method failed." Note: higher-level
658	      methods (MIMIC, propensity-score) may address individual constraints.
659	    baseline_row: "Baseline (plan_011 external matching, FPR=0.314, TPR=0.834)"
660	
661	  - table_id: tab_3_gsm8k_comparison
662	    caption: >-
663	      Cross-benchmark comparison: MMLU vs GSM8K on temporal DIF and
664	      semi-synthetic detection. GSM8K replicates key findings on a
665	      single-domain math benchmark (1,319 items × 6,702 models).
666	    placement: experiments
667	    type: comparison
668	    columns:
669	      - Metric
670	      - MMLU (plan_001/011)
671	      - GSM8K (plan_004)
672	    data_source: "registry: plan_001_real_data_dif_mmlu, plan_011_semi_synthetic_validation, plan_004_gsm8k_cross_benchmark"
673	    notes: >-
674	      Rows: Items / Models / Temporal C% / Sanity C% / Semi-synthetic
675	      ΔTPR (standard, p=0.7) / ΔTPR (external, p=0.5) / Baseline FPR
676	      (external) / GSM1K gap correlation (GSM8K only). Highlight: GSM8K
677	      standard ΔTPR=+0.818 vs MMLU external ΔTPR=+0.508. Different
678	      matching strategies make direct comparison nuanced — note in caption.
679	
680	  - table_id: tab_A1_power_analysis
681	    caption: >-
682	      DIF power analysis: ETS C classification performance with real
683	      MMLU IRT parameters across sample sizes and effect sizes.
684	    placement: appendix
685	    type: statistics
686	    columns:
687	      - N per group
688	      - "δ (logits)"
689	      - TPR (ETS C)
690	      - FPR (ETS C)
691	      - AUC (MH)
692	      - AUC (LR)
693	    data_source: "registry: mvp_dif_power_sim, mvp_dif_power_sim_phase2"
694	    notes: >-
695	      Grid: N ∈ {50, 80, 100} × δ ∈ {1.0, 1.2, 1.4, 1.6}. Operational
696	      region: N≥80, δ≥1.4 (TPR 0.68-0.80, FPR 0.036-0.042).
697	
698	  - table_id: tab_A2_within_subject_detail
699	    caption: >-
700	      Per-subject semi-synthetic validation with cross-subject vs
701	      within-subject matching at p=0.5.
702	    placement: appendix
703	    type: comparison
704	    columns:
705	      - Subject
706	      - N items
707	      - "Baseline FPR (cross)"
708	      - "ΔTPR (cross)"
709	      - "Baseline FPR (within)"
710	      - "ΔTPR (within)"
711	      - "ΔFPR (cross)"
712	    data_source: "registry: plan_016_within_subject_semi_synthetic"
713	    notes: >-
714	      5 subjects: business_ethics, human_aging, professional_medicine,
715	      formal_logic, high_school_statistics. Cross-subject ΔFPR=0.000 for
716	      all subjects. business_ethics is failure case (baseline FPR>0.53
717	      both methods).
718	
719	  - table_id: tab_A3_threshold_sensitivity
720	    caption: >-
721	      ETS threshold sensitivity analysis with BH FDR correction (q=0.05).
722	      Finding robust across thresholds; BH correction removes only 3
723	      items at standard threshold.
724	    placement: appendix
725	    type: statistics
726	    columns:
727	      - "ETS Threshold (|Δ_MH|)"
728	      - "C% (uncorrected)"
729	      - "C% (BH-corrected)"
730	      - "N items flagged"
731	    data_source: "registry: plan_018_ets_threshold_sensitivity"
732	    notes: >-
733	      Rows: 1.0 (48.9%/48.2%), 1.5 (31.3%/31.3%), 2.0 (18.3%/18.3%),
734	      2.5 (10.2%/10.2%). BH has minimal effect because ETS dual
735	      threshold (effect size + significance) already controls FPR.
736	
737	  - table_id: tab_A4_circularity_ablation
738	    caption: >-
739	      Circularity ablation: ranking disruption from removing different
740	      item subsets (31.3% removal rate). DIF is least disruptive
741	      non-random strategy.
742	    placement: appendix
743	    type: comparison
744	    columns:
745	      - Removal Strategy
746	      - "ρ (2024 cohort)"
747	      - "z vs random"
748	      - "Jaccard with DIF-C"
749	    data_source: "registry: plan_020_circularity_ablation"
750	    notes: >-
751	      DIF z=-9.5 vs random, but high-discrimination z=-15.8,
752	      accuracy-gap z=-156.5, high-variance z=-107.9. DIF-discrimination
753	      Jaccard=0.12. DIF isolates ability-conditioned differential
754	      behavior, not just generally informative items.
755	
756	literature_strategy:
757	  citation_budget: 40
758	  macro_context:
759	    - "LLM benchmark contamination detection and validation methodology"
760	    - "psychometric methods (IRT, DIF) applied to LLM evaluation"
761	    - "benchmark temporal comparability and dynamic evaluation design"
762	  micro_clusters:
763	    - cluster_name: "Contamination Detection Methods"
764	      search_queries:
765	        - "benchmark contamination detection LLM 2024 2025 2026"
766	        - "Min-K++ training data detection language model"
767	        - "ConStat perturbation contamination benchmark"
768	        - "n-gram overlap contamination benchmark LLM"
769	      must_cite:
770	        - "Wang et al. 2026 RL fragility (ICLR 2026)"
771	        - "Liang et al. 2026 DVD generation variance"
772	        - "Tao et al. 2026 Self-Critique (ICLR 2026)"
773	        - "Li et al. EMNLP 2024 web-overlap labels"
774	        - "Shi et al. 2024 Min-K++"
775	        - "Balloccu et al. 2024"
776	      target_count: 10
777	
778	    - cluster_name: "IRT in LLM Evaluation"
779	      search_queries:
780	        - "item response theory LLM evaluation 2024 2025 2026"
781	        - "Growing Pains fixed parameter calibration benchmark"
782	        - "psychometric analysis language model benchmark"
783	      must_cite:
784	        - "Habba et al. 2026 Growing Pains (NOT Polo)"
785	        - "Zhou et al. 2026 PSN-IRT AAAI (NOT Polo)"
786	        - "Hardy et al. 2026 scalability coefficients"
787	        - "Lalor et al. 2019 IRT for NLP"
788	        - "Vania et al. 2021"
789	      target_count: 8
790	
791	    - cluster_name: "DIF Methodology & Measurement Invariance"
792	      search_queries:
793	        - "differential item functioning Mantel-Haenszel ETS classification"
794	        - "impact versus DIF Shealy Stout SIBTEST"
795	        - "DIF small sample logistic regression"
796	        - "Zumbo 1999 DIF"
797	        - "measurement invariance Meredith 1993"
798	        - "Vandenberg Lance 2000 measurement invariance review"
799	        - "Swaminathan Rogers 1990 non-uniform DIF"
800	        - "propensity score matching DIF Teresi 2007"
801	        - "Lord chi-square DIF Raju area measure"
802	      must_cite:
803	        - "Holland & Thayer 1988 MH-DIF"
804	        - "Shealy & Stout 1993 SIBTEST"
805	        - "Clauser & Mazor 1998 DIF review"
806	        - "Zumbo 1999 DIF overview"
807	        - "Belzak 2020 small-sample DIF"
808	        - "Kim & Kolen 2019 fixed parameter calibration"
809	        - "Meredith 1993 measurement invariance"
810	        - "Vandenberg & Lance 2000 invariance review"
811	        - "Swaminathan & Rogers 1990 non-uniform DIF"
812	        - "Teresi 2007 propensity score DIF"
813	      target_count: 12
814	
815	    - cluster_name: "Benchmark Design & Concurrent Work"
816	      search_queries:
817	        - "contamination-free benchmark LLM LiveBench 2025"
818	        - "benchmark ground truth contamination labels validation"
819	        - "GSM1K GSM8K contamination evidence"
820	        - "GAIA benchmark LLM evaluation"
821	        - "Chatbot Arena LLM ranking"
822	        - "MMLU benchmark analysis psychometric"
823	      must_cite:
824	        - "White et al. 2025 LiveBench (ICLR)"
825	        - "Zhang et al. 2024 GSM1K"
826	        - "METABENCH original paper"
827	      target_count: 8
828	
829	    - cluster_name: "LLM Evaluation Methodology"
830	      search_queries:
831	        - "LLM evaluation methodology benchmark design 2025 2026"
832	        - "MMLU benchmark psychometric analysis"
833	        - "language model evaluation survey"
834	      must_cite: []
835	      target_count: 5
836	
837	writing_order:
838	  - experiments
839	  - method
840	  - introduction
841	  - related_work
842	  - discussion
843	  - abstract
844	  - conclusion
845	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "eb99638d-984b-4579-be32-58d31997fce9"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 42964,
    "tool_uses": 7,
    "duration_ms": 9920
  },
  "last_tool_name": "Bash",
  "uuid": "23abe855-c398-4ed7-8afe-e0d8421b2ee4",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ps3SDjbACaR7LrLTwMABr7`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "c35bb0b9-e4ee-4bb0-a6da-3e4568a845c4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PndnhM7ikNoYii81u8aFS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 451,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 28352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14123,
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

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Reading paper/math_commands.tex",
  "usage": {
    "total_tokens": 42965,
    "tool_uses": 8,
    "duration_ms": 9931
  },
  "last_tool_name": "Read",
  "uuid": "30edff5d-b768-4065-a1fa-4819addf6bbf",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_014dbnKSXJKsA3BuWavuVzyx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "4003639e-4a7b-4000-9957-4a1cfb1acc52",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PndnhM7ikNoYii81u8aFS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 451,
      "cache_creation_input_tokens": 14123,
      "cache_read_input_tokens": 28352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14123,
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

_source line 56 · 2026-05-21T04:01:12.621Z_

<details><summary>↩ Tool result · `toolu_01Ps3SDjbACaR7LrLTwMABr7`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "e0301efc-781b-4a8b-afd2-bee4b9b59b00"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-21T04:01:12.578Z_

<details><summary>↩ Tool result · `toolu_014dbnKSXJKsA3BuWavuVzyx`</summary>

```text
1	%%%%% NEW MATH DEFINITIONS %%%%%
2	
3	\usepackage{amsmath,amsfonts,bm}
4	
5	% Mark sections of captions for referring to divisions of figures
6	\newcommand{\figleft}{{\em (Left)}}
7	\newcommand{\figcenter}{{\em (Center)}}
8	\newcommand{\figright}{{\em (Right)}}
9	\newcommand{\figtop}{{\em (Top)}}
10	\newcommand{\figbottom}{{\em (Bottom)}}
11	\newcommand{\captiona}{{\em (a)}}
12	\newcommand{\captionb}{{\em (b)}}
13	\newcommand{\captionc}{{\em (c)}}
14	\newcommand{\captiond}{{\em (d)}}
15	
16	% Highlight a newly defined term
17	\newcommand{\newterm}[1]{{\bf #1}}
18	
19	
20	% Figure reference, lower-case.
21	\def\figref#1{figure~\ref{#1}}
22	% Figure reference, capital. For start of sentence
23	\def\Figref#1{Figure~\ref{#1}}
24	\def\twofigref#1#2{figures \ref{#1} and \ref{#2}}
25	\def\quadfigref#1#2#3#4{figures \ref{#1}, \ref{#2}, \ref{#3} and \ref{#4}}
26	% Section reference, lower-case.
27	\def\secref#1{section~\ref{#1}}
28	% Section reference, capital.
29	\def\Secref#1{Section~\ref{#1}}
30	% Reference to two sections.
31	\def\twosecrefs#1#2{sections \ref{#1} and \ref{#2}}
32	% Reference to three sections.
33	\def\secrefs#1#2#3{sections \ref{#1}, \ref{#2} and \ref{#3}}
34	% Reference to an equation, lower-case.
35	\def\eqref#1{equation~\ref{#1}}
36	% Reference to an equation, upper case
37	\def\Eqref#1{Equation~\ref{#1}}
38	% A raw reference to an equation---avoid using if possible
39	\def\plaineqref#1{\ref{#1}}
40	% Reference to a chapter, lower-case.
41	\def\chapref#1{chapter~\ref{#1}}
42	% Reference to an equation, upper case.
43	\def\Chapref#1{Chapter~\ref{#1}}
44	% Reference to a range of chapters
45	\def\rangechapref#1#2{chapters\ref{#1}--\ref{#2}}
46	% Reference to an algorithm, lower-case.
47	\def\algref#1{algorithm~\ref{#1}}
48	% Reference to an algorithm, upper case.
49	\def\Algref#1{Algorithm~\ref{#1}}
50	\def\twoalgref#1#2{algorithms \ref{#1} and \ref{#2}}
51	\def\Twoalgref#1#2{Algorithms \ref{#1} and \ref{#2}}
52	% Reference to a part, lower case
53	\def\partref#1{part~\ref{#1}}
54	% Reference to a part, upper case
55	\def\Partref#1{Part~\ref{#1}}
56	\def\twopartref#1#2{parts \ref{#1} and \ref{#2}}
57	
58	\def\ceil#1{\lceil #1 \rceil}
59	\def\floor#1{\lfloor #1 \rfloor}
60	\def\1{\bm{1}}
61	\newcommand{\train}{\mathcal{D}}
62	\newcommand{\valid}{\mathcal{D_{\mathrm{valid}}}}
63	\newcommand{\test}{\mathcal{D_{\mathrm{test}}}}
64	
65	\def\eps{{\epsilon}}
66	
67	
68	% Random variables
69	\def\reta{{\textnormal{$\eta$}}}
70	\def\ra{{\textnormal{a}}}
71	\def\rb{{\textnormal{b}}}
72	\def\rc{{\textnormal{c}}}
73	\def\rd{{\textnormal{d}}}
74	\def\re{{\textnormal{e}}}
75	\def\rf{{\textnormal{f}}}
76	\def\rg{{\textnormal{g}}}
77	\def\rh{{\textnormal{h}}}
78	\def\ri{{\textnormal{i}}}
79	\def\rj{{\textnormal{j}}}
80	\def\rk{{\textnormal{k}}}
81	\def\rl{{\textnormal{l}}}
82	% rm is already a command, just don't name any random variables m
83	\def\rn{{\textnormal{n}}}
84	\def\ro{{\textnormal{o}}}
85	\def\rp{{\textnormal{p}}}
86	\def\rq{{\textnormal{q}}}
87	\def\rr{{\textnormal{r}}}
88	\def\rs{{\textnormal{s}}}
89	\def\rt{{\textnormal{t}}}
90	\def\ru{{\textnormal{u}}}
91	\def\rv{{\textnormal{v}}}
92	\def\rw{{\textnormal{w}}}
93	\def\rx{{\textnormal{x}}}
94	\def\ry{{\textnormal{y}}}
95	\def\rz{{\textnormal{z}}}
96	
97	% Random vectors
98	\def\rvepsilon{{\mathbf{\epsilon}}}
99	\def\rvtheta{{\mathbf{\theta}}}
100	\def\rva{{\mathbf{a}}}
101	\def\rvb{{\mathbf{b}}}
102	\def\rvc{{\mathbf{c}}}
103	\def\rvd{{\mathbf{d}}}
104	\def\rve{{\mathbf{e}}}
105	\def\rvf{{\mathbf{f}}}
106	\def\rvg{{\mathbf{g}}}
107	\def\rvh{{\mathbf{h}}}
108	\def\rvu{{\mathbf{i}}}
109	\def\rvj{{\mathbf{j}}}
110	\def\rvk{{\mathbf{k}}}
111	\def\rvl{{\mathbf{l}}}
112	\def\rvm{{\mathbf{m}}}
113	\def\rvn{{\mathbf{n}}}
114	\def\rvo{{\mathbf{o}}}
115	\def\rvp{{\mathbf{p}}}
116	\def\rvq{{\mathbf{q}}}
117	\def\rvr{{\mathbf{r}}}
118	\def\rvs{{\mathbf{s}}}
119	\def\rvt{{\mathbf{t}}}
120	\def\rvu{{\mathbf{u}}}
121	\def\rvv{{\mathbf{v}}}
122	\def\rvw{{\mathbf{w}}}
123	\def\rvx{{\mathbf{x}}}
124	\def\rvy{{\mathbf{y}}}
125	\def\rvz{{\mathbf{z}}}
126	
127	% Elements of random vectors
128	\def\erva{{\textnormal{a}}}
129	\def\ervb{{\textnormal{b}}}
130	\def\ervc{{\textnormal{c}}}
131	\def\ervd{{\textnormal{d}}}
132	\def\erve{{\textnormal{e}}}
133	\def\ervf{{\textnormal{f}}}
134	\def\ervg{{\textnormal{g}}}
135	\def\ervh{{\textnormal{h}}}
136	\def\ervi{{\textnormal{i}}}
137	\def\ervj{{\textnormal{j}}}
138	\def\ervk{{\textnormal{k}}}
139	\def\ervl{{\textnormal{l}}}
140	\def\ervm{{\textnormal{m}}}
141	\def\ervn{{\textnormal{n}}}
142	\def\ervo{{\textnormal{o}}}
143	\def\ervp{{\textnormal{p}}}
144	\def\ervq{{\textnormal{q}}}
145	\def\ervr{{\textnormal{r}}}
146	\def\ervs{{\textnormal{s}}}
147	\def\ervt{{\textnormal{t}}}
148	\def\ervu{{\textnormal{u}}}
149	\def\ervv{{\textnormal{v}}}
150	\def\ervw{{\textnormal{w}}}
151	\def\ervx{{\textnormal{x}}}
152	\def\ervy{{\textnormal{y}}}
153	\def\ervz{{\textnormal{z}}}
154	
155	% Random matrices
156	\def\rmA{{\mathbf{A}}}
157	\def\rmB{{\mathbf{B}}}
158	\def\rmC{{\mathbf{C}}}
159	\def\rmD{{\mathbf{D}}}
160	\def\rmE{{\mathbf{E}}}
161	\def\rmF{{\mathbf{F}}}
162	\def\rmG{{\mathbf{G}}}
163	\def\rmH{{\mathbf{H}}}
164	\def\rmI{{\mathbf{I}}}
165	\def\rmJ{{\mathbf{J}}}
166	\def\rmK{{\mathbf{K}}}
167	\def\rmL{{\mathbf{L}}}
168	\def\rmM{{\mathbf{M}}}
169	\def\rmN{{\mathbf{N}}}
170	\def\rmO{{\mathbf{O}}}
171	\def\rmP{{\mathbf{P}}}
172	\def\rmQ{{\mathbf{Q}}}
173	\def\rmR{{\mathbf{R}}}
174	\def\rmS{{\mathbf{S}}}
175	\def\rmT{{\mathbf{T}}}
176	\def\rmU{{\mathbf{U}}}
177	\def\rmV{{\mathbf{V}}}
178	\def\rmW{{\mathbf{W}}}
179	\def\rmX{{\mathbf{X}}}
180	\def\rmY{{\mathbf{Y}}}
181	\def\rmZ{{\mathbf{Z}}}
182	
183	% Elements of random matrices
184	\def\ermA{{\textnormal{A}}}
185	\def\ermB{{\textnormal{B}}}
186	\def\ermC{{\textnormal{C}}}
187	\def\ermD{{\textnormal{D}}}
188	\def\ermE{{\textnormal{E}}}
189	\def\ermF{{\textnormal{F}}}
190	\def\ermG{{\textnormal{G}}}
191	\def\ermH{{\textnormal{H}}}
192	\def\ermI{{\textnormal{I}}}
193	\def\ermJ{{\textnormal{J}}}
194	\def\ermK{{\textnormal{K}}}
195	\def\ermL{{\textnormal{L}}}
196	\def\ermM{{\textnormal{M}}}
197	\def\ermN{{\textnormal{N}}}
198	\def\ermO{{\textnormal{O}}}
199	\def\ermP{{\textnormal{P}}}
200	\def\ermQ{{\textnormal{Q}}}
201	\def\ermR{{\textnormal{R}}}
202	\def\ermS{{\textnormal{S}}}
203	\def\ermT{{\textnormal{T}}}
204	\def\ermU{{\textnormal{U}}}
205	\def\ermV{{\textnormal{V}}}
206	\def\ermW{{\textnormal{W}}}
207	\def\ermX{{\textnormal{X}}}
208	\def\ermY{{\textnormal{Y}}}
209	\def\ermZ{{\textnormal{Z}}}
210	
211	% Vectors
212	\def\vzero{{\bm{0}}}
213	\def\vone{{\bm{1}}}
214	\def\vmu{{\bm{\mu}}}
215	\def\vtheta{{\bm{\theta}}}
216	\def\va{{\bm{a}}}
217	\def\vb{{\bm{b}}}
218	\def\vc{{\bm{c}}}
219	\def\vd{{\bm{d}}}
220	\def\ve{{\bm{e}}}
221	\def\vf{{\bm{f}}}
222	\def\vg{{\bm{g}}}
223	\def\vh{{\bm{h}}}
224	\def\vi{{\bm{i}}}
225	\def\vj{{\bm{j}}}
226	\def\vk{{\bm{k}}}
227	\def\vl{{\bm{l}}}
228	\def\vm{{\bm{m}}}
229	\def\vn{{\bm{n}}}
230	\def\vo{{\bm{o}}}
231	\def\vp{{\bm{p}}}
232	\def\vq{{\bm{q}}}
233	\def\vr{{\bm{r}}}
234	\def\vs{{\bm{s}}}
235	\def\vt{{\bm{t}}}
236	\def\vu{{\bm{u}}}
237	\def\vv{{\bm{v}}}
238	\def\vw{{\bm{w}}}
239	\def\vx{{\bm{x}}}
240	\def\vy{{\bm{y}}}
241	\def\vz{{\bm{z}}}
242	
243	% Elements of vectors
244	\def\evalpha{{\alpha}}
245	\def\evbeta{{\beta}}
246	\def\evepsilon{{\epsilon}}
247	\def\evlambda{{\lambda}}
248	\def\evomega{{\omega}}
249	\def\evmu{{\mu}}
250	\def\evpsi{{\psi}}
251	\def\evsigma{{\sigma}}
252	\def\evtheta{{\theta}}
253	\def\eva{{a}}
254	\def\evb{{b}}
255	\def\evc{{c}}
256	\def\evd{{d}}
257	\def\eve{{e}}
258	\def\evf{{f}}
259	\def\evg{{g}}
260	\def\evh{{h}}
261	\def\evi{{i}}
262	\def\evj{{j}}
263	\def\evk{{k}}
264	\def\evl{{l}}
265	\def\evm{{m}}
266	\def\evn{{n}}
267	\def\evo{{o}}
268	\def\evp{{p}}
269	\def\evq{{q}}
270	\def\evr{{r}}
271	\def\evs{{s}}
272	\def\evt{{t}}
273	\def\evu{{u}}
274	\def\evv{{v}}
275	\def\evw{{w}}
276	\def\evx{{x}}
277	\def\evy{{y}}
278	\def\evz{{z}}
279	
280	% Matrix
281	\def\mA{{\bm{A}}}
282	\def\mB{{\bm{B}}}
283	\def\mC{{\bm{C}}}
284	\def\mD{{\bm{D}}}
285	\def\mE{{\bm{E}}}
286	\def\mF{{\bm{F}}}
287	\def\mG{{\bm{G}}}
288	\def\mH{{\bm{H}}}
289	\def\mI{{\bm{I}}}
290	\def\mJ{{\bm{J}}}
291	\def\mK{{\bm{K}}}
292	\def\mL{{\bm{L}}}
293	\def\mM{{\bm{M}}}
294	\def\mN{{\bm{N}}}
295	\def\mO{{\bm{O}}}
296	\def\mP{{\bm{P}}}
297	\def\mQ{{\bm{Q}}}
298	\def\mR{{\bm{R}}}
299	\def\mS{{\bm{S}}}
300	\def\mT{{\bm{T}}}
301	\def\mU{{\bm{U}}}
302	\def\mV{{\bm{V}}}
303	\def\mW{{\bm{W}}}
304	\def\mX{{\bm{X}}}
305	\def\mY{{\bm{Y}}}
306	\def\mZ{{\bm{Z}}}
307	\def\mBeta{{\bm{\beta}}}
308	\def\mPhi{{\bm{\Phi}}}
309	\def\mLambda{{\bm{\Lambda}}}
310	\def\mSigma{{\bm{\Sigma}}}
311	
312	% Tensor
313	\DeclareMathAlphabet{\mathsfit}{\encodingdefault}{\sfdefault}{m}{sl}
314	\SetMathAlphabet{\mathsfit}{bold}{\encodingdefault}{\sfdefault}{bx}{n}
315	\newcommand{\tens}[1]{\bm{\mathsfit{#1}}}
316	\def\tA{{\tens{A}}}
317	\def\tB{{\tens{B}}}
318	\def\tC{{\tens{C}}}
319	\def\tD{{\tens{D}}}
320	\def\tE{{\tens{E}}}
321	\def\tF{{\tens{F}}}
322	\def\tG{{\tens{G}}}
323	\def\tH{{\tens{H}}}
324	\def\tI{{\tens{I}}}
325	\def\tJ{{\tens{J}}}
326	\def\tK{{\tens{K}}}
327	\def\tL{{\tens{L}}}
328	\def\tM{{\tens{M}}}
329	\def\tN{{\tens{N}}}
330	\def\tO{{\tens{O}}}
331	\def\tP{{\tens{P}}}
332	\def\tQ{{\tens{Q}}}
333	\def\tR{{\tens{R}}}
334	\def\tS{{\tens{S}}}
335	\def\tT{{\tens{T}}}
336	\def\tU{{\tens{U}}}
337	\def\tV{{\tens{V}}}
338	\def\tW{{\tens{W}}}
339	\def\tX{{\tens{X}}}
340	\def\tY{{\tens{Y}}}
341	\def\tZ{{\tens{Z}}}
342	
343	
344	% Graph
345	\def\gA{{\mathcal{A}}}
346	\def\gB{{\mathcal{B}}}
347	\def\gC{{\mathcal{C}}}
348	\def\gD{{\mathcal{D}}}
349	\def\gE{{\mathcal{E}}}
350	\def\gF{{\mathcal{F}}}
351	\def\gG{{\mathcal{G}}}
352	\def\gH{{\mathcal{H}}}
353	\def\gI{{\mathcal{I}}}
354	\def\gJ{{\mathcal{J}}}
355	\def\gK{{\mathcal{K}}}
356	\def\gL{{\mathcal{L}}}
357	\def\gM{{\mathcal{M}}}
358	\def\gN{{\mathcal{N}}}
359	\def\gO{{\mathcal{O}}}
360	\def\gP{{\mathcal{P}}}
361	\def\gQ{{\mathcal{Q}}}
362	\def\gR{{\mathcal{R}}}
363	\def\gS{{\mathcal{S}}}
364	\def\gT{{\mathcal{T}}}
365	\def\gU{{\mathcal{U}}}
366	\def\gV{{\mathcal{V}}}
367	\def\gW{{\mathcal{W}}}
368	\def\gX{{\mathcal{X}}}
369	\def\gY{{\mathcal{Y}}}
370	\def\gZ{{\mathcal{Z}}}
371	
372	% Sets
373	\def\sA{{\mathbb{A}}}
374	\def\sB{{\mathbb{B}}}
375	\def\sC{{\mathbb{C}}}
376	\def\sD{{\mathbb{D}}}
377	% Don't use a set called E, because this would be the same as our symbol
378	% for expectation.
379	\def\sF{{\mathbb{F}}}
380	\def\sG{{\mathbb{G}}}
381	\def\sH{{\mathbb{H}}}
382	\def\sI{{\mathbb{I}}}
383	\def\sJ{{\mathbb{J}}}
384	\def\sK{{\mathbb{K}}}
385	\def\sL{{\mathbb{L}}}
386	\def\sM{{\mathbb{M}}}
387	\def\sN{{\mathbb{N}}}
388	\def\sO{{\mathbb{O}}}
389	\def\sP{{\mathbb{P}}}
390	\def\sQ{{\mathbb{Q}}}
391	\def\sR{{\mathbb{R}}}
392	\def\sS{{\mathbb{S}}}
393	\def\sT{{\mathbb{T}}}
394	\def\sU{{\mathbb{U}}}
395	\def\sV{{\mathbb{V}}}
396	\def\sW{{\mathbb{W}}}
397	\def\sX{{\mathbb{X}}}
398	\def\sY{{\mathbb{Y}}}
399	\def\sZ{{\mathbb{Z}}}
400	
401	% Entries of a matrix
402	\def\emLambda{{\Lambda}}
403	\def\emA{{A}}
404	\def\emB{{B}}
405	\def\emC{{C}}
406	\def\emD{{D}}
407	\def\emE{{E}}
408	\def\emF{{F}}
409	\def\emG{{G}}
410	\def\emH{{H}}
411	\def\emI{{I}}
412	\def\emJ{{J}}
413	\def\emK{{K}}
414	\def\emL{{L}}
415	\def\emM{{M}}
416	\def\emN{{N}}
417	\def\emO{{O}}
418	\def\emP{{P}}
419	\def\emQ{{Q}}
420	\def\emR{{R}}
421	\def\emS{{S}}
422	\def\emT{{T}}
423	\def\emU{{U}}
424	\def\emV{{V}}
425	\def\emW{{W}}
426	\def\emX{{X}}
427	\def\emY{{Y}}
428	\def\emZ{{Z}}
429	\def\emSigma{{\Sigma}}
430	
431	% entries of a tensor
432	% Same font as tensor, without \bm wrapper
433	\newcommand{\etens}[1]{\mathsfit{#1}}
434	\def\etLambda{{\etens{\Lambda}}}
435	\def\etA{{\etens{A}}}
436	\def\etB{{\etens{B}}}
437	\def\etC{{\etens{C}}}
438	\def\etD{{\etens{D}}}
439	\def\etE{{\etens{E}}}
440	\def\etF{{\etens{F}}}
441	\def\etG{{\etens{G}}}
442	\def\etH{{\etens{H}}}
443	\def\etI{{\etens{I}}}
444	\def\etJ{{\etens{J}}}
445	\def\etK{{\etens{K}}}
446	\def\etL{{\etens{L}}}
447	\def\etM{{\etens{M}}}
448	\def\etN{{\etens{N}}}
449	\def\etO{{\etens{O}}}
450	\def\etP{{\etens{P}}}
451	\def\etQ{{\etens{Q}}}
452	\def\etR{{\etens{R}}}
453	\def\etS{{\etens{S}}}
454	\def\etT{{\etens{T}}}
455	\def\etU{{\etens{U}}}
456	\def\etV{{\etens{V}}}
457	\def\etW{{\etens{W}}}
458	\def\etX{{\etens{X}}}
459	\def\etY{{\etens{Y}}}
460	\def\etZ{{\etens{Z}}}
461	
462	% The true underlying data generating distribution
463	\newcommand{\pdata}{p_{\rm{data}}}
464	% The empirical distribution defined by the training set
465	\newcommand{\ptrain}{\hat{p}_{\rm{data}}}
466	\newcommand{\Ptrain}{\hat{P}_{\rm{data}}}
467	% The model distribution
468	\newcommand{\pmodel}{p_{\rm{model}}}
469	\newcommand{\Pmodel}{P_{\rm{model}}}
470	\newcommand{\ptildemodel}{\tilde{p}_{\rm{model}}}
471	% Stochastic autoencoder distributions
472	\newcommand{\pencode}{p_{\rm{encoder}}}
473	\newcommand{\pdecode}{p_{\rm{decoder}}}
474	\newcommand{\precons}{p_{\rm{reconstruct}}}
475	
476	\newcommand{\laplace}{\mathrm{Laplace}} % Laplace distribution
477	
478	\newcommand{\E}{\mathbb{E}}
479	\newcommand{\Ls}{\mathcal{L}}
480	\newcommand{\R}{\mathbb{R}}
481	\newcommand{\emp}{\tilde{p}}
482	\newcommand{\lr}{\alpha}
483	\newcommand{\reg}{\lambda}
484	\newcommand{\rect}{\mathrm{rectifier}}
485	\newcommand{\softmax}{\mathrm{softmax}}
486	\newcommand{\sigmoid}{\sigma}
487	\newcommand{\softplus}{\zeta}
488	\newcommand{\KL}{D_{\mathrm{KL}}}
489	\newcommand{\Var}{\mathrm{Var}}
490	\newcommand{\standarderror}{\mathrm{SE}}
491	\newcommand{\Cov}{\mathrm{Cov}}
492	% Wolfram Mathworld says $L^2$ is for function spaces and $\ell^2$ is for vectors
493	% But then they seem to use $L^2$ for vectors throughout the site, and so does
494	% wikipedia.
495	\newcommand{\normlzero}{L^0}
496	\newcommand{\normlone}{L^1}
497	\newcommand{\normltwo}{L^2}
498	\newcommand{\normlp}{L^p}
499	\newcommand{\normmax}{L^\infty}
500	
501	\newcommand{\parents}{Pa} % See usage in notation.tex. Chosen to match Daphne's book.
502	
503	\DeclareMathOperator*{\argmax}{arg\,max}
504	\DeclareMathOperator*{\argmin}{arg\,min}
505	
506	\DeclareMathOperator{\sign}{sign}
507	\DeclareMathOperator{\Tr}{Tr}
508	\let\ab\allowbreak
509	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "2c6212e4-71ce-4a76-b8ad-72b52480d7e4"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 50989,
    "tool_uses": 9,
    "duration_ms": 12595
  },
  "last_tool_name": "Bash",
  "uuid": "2dd88c5b-0390-4943-8a86-e84ea09adf81",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01QSL6gpGDgsZEDjZrqrUcfa`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "698175f9-9fd9-40eb-b5fb-d455c7fe7d1b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QheSterSrCsXWVZHcpWrj6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8460,
      "cache_read_input_tokens": 42475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8460,
        "ephemeral_1h_input_tokens": 0
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

_source line 60 · 2026-05-21T04:01:15.283Z_

<details><summary>↩ Tool result · `toolu_01QSL6gpGDgsZEDjZrqrUcfa`</summary>

```text
total 160
drwxr-xr-x 3 ubuntu ubuntu  4096 May 21 03:58 .
drwxr-xr-x 9 ubuntu ubuntu  4096 May 21 04:00 ..
-rw-r--r-- 1 ubuntu ubuntu 20521 May 21 03:58 fancyhdr.sty
-rw-r--r-- 1 ubuntu ubuntu 26973 May 21 03:58 iclr2026_conference.bst
-rw-r--r-- 1 ubuntu ubuntu  9025 May 21 03:58 iclr2026_conference.sty
-rw-r--r-- 1 ubuntu ubuntu   910 May 21 03:58 main.tex
-rw-r--r-- 1 ubuntu ubuntu 12284 May 21 03:58 math_commands.tex
-rw-r--r-- 1 ubuntu ubuntu 45154 May 21 03:58 natbib.sty
-rw-r--r-- 1 ubuntu ubuntu 19470 May 21 03:55 references.bib
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 03:58 sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "535bb845-3491-4b57-8c38-fff7a1ce344e"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 51491,
    "tool_uses": 10,
    "duration_ms": 15204
  },
  "last_tool_name": "Bash",
  "uuid": "d26c8315-d2c7-40a2-9d9e-1ea3391b6fb5",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_01UvYFtiwmhUVs4siVLpomJM`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "da159d4f-3388-44c3-80cd-5a553bae3dd9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J2bqkuhwvebRP8CiXPHptq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 50935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 431,
        "ephemeral_1h_input_tokens": 0
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

_source line 63 · 2026-05-21T04:01:17.915Z_

<details><summary>↩ Tool result · `toolu_01UvYFtiwmhUVs4siVLpomJM`</summary>

```text
total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 21 03:58 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 21 03:58 ..
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "33f42d2e-3abb-472a-9648-6006d424556a"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 51661,
    "tool_uses": 11,
    "duration_ms": 18240
  },
  "last_tool_name": "Bash",
  "uuid": "3f01e464-afa9-4104-951e-c2c91523e57a",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01AyN8Qc7GdqJ2xHyxF52NZc`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"abstract*\" -o -name \"introduction*\" -o -name \"method*\" 2>/dev/null | grep -E \"\\.(tex|md)$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "90409e5f-4b59-4da6-ac6d-ecc77a149509",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01B7p5dHqzxf24sptYbqjL81",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 51366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 168,
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

_source line 66 · 2026-05-21T04:01:20.932Z_

<details><summary>↩ Tool result · `toolu_01AyN8Qc7GdqJ2xHyxF52NZc`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "a1e5fc9a-c9ef-425f-80b1-edc5253b7b78"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Reading paper_framing.md",
  "usage": {
    "total_tokens": 51832,
    "tool_uses": 12,
    "duration_ms": 20709
  },
  "last_tool_name": "Read",
  "uuid": "9cb52ec8-1efa-44b0-9d39-54d377df2ecf",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01AsBzRccWoU9dHNeeyZPtcy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md",
  "limit": 5000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "366eb65d-5df3-4e58-af38-d628266c8a5e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019eLCh8gPk1GBFwia9vJJCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 51534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 170,
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

_source line 69 · 2026-05-21T04:01:23.385Z_

<details><summary>↩ Tool result · `toolu_01AsBzRccWoU9dHNeeyZPtcy`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026)
5	
6	## Paper Type
7	Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."
8	
9	## Core Claims (4 条, 可证伪)
10	
11	**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
12	- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement)
13	- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
14	- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.
15	
16	**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
17	- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)
18	- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection"
19	
20	**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
21	- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
22	- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
23	- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability
24	
25	**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
26	1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
27	2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
28	3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.
29	4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.
30	- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)
31	- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.
32	- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
33	- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed
34	
35	## Story Spine
36	
37	**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.
38	
39	**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.
40	
41	**What we find**: Three discoveries, each a contribution:
42	
43	1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.
44	
45	2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.
46	
47	3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.
48	
49	4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]). DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.
50	
51	**Headline result**: "Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling accuracy). We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000)."
52	
53	## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks
54	
55	Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.
56	
57	## Venue Fit
58	
59	- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.
60	- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 28–38% instability at unprecedented scale (5,227×12,508), (2) the ground truth meta-critique affecting the field's validation methodology, (3) the semi-synthetic validation framework with cross-subject matching innovation (ΔFPR=0.000), (4) DIF as diagnostic lens revealing benchmark measurement structure. Explicitly acknowledge MH-DIF is applied without modification; novelty is empirical characterization + framework design, not algorithmic. Frame as "bringing mature psychometric tools to characterize an urgent ML evaluation problem — the scale creates novel statistical challenges (architecture heterogeneity, multidimensional construct, 5000+ examinees)."
61	
62	## Anticipated Reviewer Concerns (updated for pivot)
63	
64	1. **"38% could just mean models got better"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.
65	
66	2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.
67	
68	3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.
69	
70	4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.
71	
72	5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.
73	
74	6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.
75	
76	7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.
77	
78	8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.
79	
80	9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.
81	
82	10. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.
83	
84	## Dropped from Original Framing
85	
86	- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
87	- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
88	- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
89	- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."
90	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "91a948ca-c006-4bcd-9885-7f2fc0d22400"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Running ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 51833,
    "tool_uses": 13,
    "duration_ms": 20884
  },
  "last_tool_name": "Bash",
  "uuid": "8d9c27e5-0a3f-4cc7-b92e-b4b85289157d",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01SGbpwsdom6JBENrr2Mvoxt`</summary>

```json
{
  "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/ | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "4b1d1d67-40bc-4c3d-86eb-79fe86eac02b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019eLCh8gPk1GBFwia9vJJCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 51534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 170,
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

_source line 72 · 2026-05-21T04:01:23.624Z_

<details><summary>↩ Tool result · `toolu_01SGbpwsdom6JBENrr2Mvoxt`</summary>

```text
total 24
lrwxrwxrwx 1 ubuntu ubuntu  126 May 21 04:00 latest -> /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826
drwxr-xr-x 6 ubuntu ubuntu 4096 May 21 04:00 dream_20260521T032826
drwxr-xr-x 6 ubuntu ubuntu 4096 May 21 02:23 dream_20260521T012912
drwxr-xr-x 6 ubuntu ubuntu 4096 May 20 21:45 dream_20260520T205007
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "1fb49548-981a-458f-99ad-9e3918f6b9a7"
}
```

</details>

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "description": "Reading artifacts/dream_reports/dream_20260521T032826/best/paper.tex",
  "usage": {
    "total_tokens": 56965,
    "tool_uses": 14,
    "duration_ms": 23391
  },
  "last_tool_name": "Read",
  "uuid": "4d6cf6dc-caea-4c50-b2ee-a6e4da15c447",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01Xw981oBgD84njGZPVitbxa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper.tex",
  "limit": 3000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "3276180c-25b9-48cc-941e-1fe0df3d403d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BkpiboheqStpy1C2wnK3NF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5129,
      "cache_read_input_tokens": 51704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5129,
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

_source line 75 · 2026-05-21T04:01:26.303Z_

<details><summary>↩ Tool result · `toolu_01Xw981oBgD84njGZPVitbxa`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{natbib}
8	\usepackage[margin=1in]{geometry}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Psychometric Analysis Reveals Structural Benchmark Instability\\That Contamination Validation Cannot Detect}
13	
14	\author{Anonymous}
15	\date{}
16	
17	\begin{document}
18	\maketitle
19	
20	%==============================================================================
21	\begin{abstract}
22	LLM benchmarks implicitly assume temporal score comparability---that a score on MMLU today measures the same construct as a score measured six months ago. We apply Differential Item Functioning (DIF) analysis to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items) and find that 28--30\% of items are functionally unstable across model generations, even within architecture-homogeneous decoder-only populations where IRT model fit is excellent (RMSEA$=$0.024, CFI$=$0.966). Instability decomposition shows that partial $\rho=0.22$ ($p=0.012$) persists after controlling for domain accuracy improvement, indicating genuine item function change beyond aggregate capability gains. We demonstrate that the field's standard validation approach---web-overlap contamination labels---cannot capture this differential signal (enrichment$\approx$1.0), while a semi-synthetic injection framework confirms detection capability ($\Delta$TPR$=$+0.508 on MMLU, +0.818 on GSM8K). Cross-subject matching eliminates false positive inflation ($\Delta$FPR$=$0.000). Group-level DIF statistics remain robust to reasoning-RL model compositions (flag retention 89--91\%, AUROC$=$0.88) while traditional per-model detectors degrade significantly (ConStat AUROC: 0.73$\to$0.54; Min-K\%: 0.68$\to$0.51). We further characterize DIF via complementary methods (ConStat perturbation, generation variance, ensemble fusion), continuous monitoring extensions (Item-Focused Trees, cumulative Bayesian DIF), and a principled equating framework for benchmark maintenance. Our findings reveal that psychometric analysis exposes structural benchmark problems invisible to existing contamination detection methodology.
23	\end{abstract}
24	
25	%==============================================================================
26	\section{Introduction}
27	
28	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent construct. This assumption of temporal score comparability is foundational to benchmark-based evaluation yet rarely tested. If items function differently across model generations---some becoming trivially easy due to training data overlap, others shifting in cognitive demand as architectures evolve---then benchmark scores from different periods are not directly comparable.
29	
30	We bring Differential Item Functioning (DIF), a classical psychometric tool with decades of validation in educational testing, to characterize this temporal instability at unprecedented scale. Using the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), we conduct the largest DIF analysis on LLM benchmarks to date.
31	
32	Our contributions are fourfold:
33	\begin{enumerate}
34	\item \textbf{Temporal instability characterization}: 28--30\% of MMLU items exhibit large DIF (ETS C category, $|\Delta_\text{MH}|\geq 1.5$) between 2023 and 2024-H1 model cohorts, persisting within architecture-homogeneous decoder-only populations with excellent IRT fit (RMSEA$=$0.024). Instability decomposition reveals genuine item function change (partial $\rho=0.22$, $p=0.012$) beyond domain-level capability gains.
35	
36	\item \textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across cohorts). Enrichment$\approx$1.0 between DIF flags and web-overlap labels is expected, not failure.
37	
38	\item \textbf{Semi-synthetic validation framework}: A reusable $\Delta$TPR methodology with cross-subject matching ($\Delta$FPR$=$0.000) for validating any item-level contamination detector.
39	
40	\item \textbf{DIF as diagnostic lens}: MMLU rankings exhibit massive measurement redundancy ($\rho\approx$0.997 after 31\% removal), yet DIF items concentrate cross-cohort discriminative signal. Cross-benchmark validation on GSM8K shows DIF items resist contamination-based gains ($r=-0.478$, $p=0.005$).
41	\end{enumerate}
42	
43	We further demonstrate DIF's robustness to reasoning-RL compositions, compare with complementary detection methods, and sketch principled extensions toward longitudinal benchmark monitoring and equating-based maintenance.
44	
45	%==============================================================================
46	\section{Background: Differential Item Functioning}
47	
48	DIF occurs when examinees of equal ability from different groups have unequal probabilities of answering an item correctly. In our setting, the ``groups'' are temporal cohorts of LLM models (reference: 2023 models; focal: 2024-H1 models), and ``ability'' is total benchmark score.
49	
50	\paragraph{Mantel-Haenszel statistic.} We use the MH odds ratio $\alpha_\text{MH}$ and its log-transform $\Delta_\text{MH} = -2.35 \ln(\alpha_\text{MH})$, classified via ETS categories: A ($|\Delta_\text{MH}|<1.0$, negligible), B ($1.0\leq|\Delta_\text{MH}|<1.5$, moderate), C ($|\Delta_\text{MH}|\geq 1.5$, large). An item flagged C exhibits functionally meaningful differential behavior between cohorts after conditioning on total ability.
51	
52	\paragraph{IRT model fit.} We assess measurement model adequacy via confirmatory factor analysis fit indices: RMSEA ($<$0.05 acceptable, $<$0.03 excellent), CFI ($>$0.95 good), TLI ($>$0.95 good), and SRMR ($<$0.05 good). These validate the unidimensionality assumption underlying MH-DIF.
53	
54	%==============================================================================
55	\section{Architecture-Stratified DIF Analysis}\label{sec:arch}
56	
57	The strongest potential objection to temporal DIF findings is that architecture heterogeneity (mixing decoder-only, encoder-decoder, and hybrid models) violates IRT's unidimensionality assumption, producing spurious DIF. We eliminate this concern by stratifying to decoder-only models.
58	
59	\subsection{Experimental Setup}
60	
61	From the full METABENCH population ($N=5,219$), we extract decoder-only models ($N=3,487$) sharing transformer architecture, autoregressive training, and similar tokenizer families. Reference cohort: 892 models (released $\leq$2023); focal cohort: 513 models (released 2024-H1).
62	
63	\subsection{IRT Model Fit}
64	
65	\begin{table}[h]
66	\centering
67	\caption{IRT fit comparison: full population vs.\ decoder-only subset.}
68	\label{tab:irt_fit}
69	\begin{tabular}{lccccc}
70	\toprule
71	Population & $N$ & RMSEA & CFI & TLI & SRMR \\
72	\midrule
73	Full & 5,219 & 0.067 & 0.874 & 0.851 & 0.058 \\
74	Decoder-only & 3,487 & 0.024 & 0.966 & 0.958 & 0.031 \\
75	Encoder-decoder & 412 & 0.041 & 0.921 & 0.903 & 0.044 \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	RMSEA improves by 64.2\% (0.067$\to$0.024) when restricting to decoder-only models, with CFI and TLI both exceeding 0.95. The measurement model is well-specified for this population: the latent trait is close to unidimensional within decoder-only models, which vary primarily along a single capability axis (scale $\times$ data $\times$ training quality).
81	
82	\subsection{Temporal DIF Persistence}
83	
84	Despite excellent model fit, temporal DIF persists at 29.1\% (C category) in the decoder-only population---only a 2.2 percentage point reduction from the full population's 31.3\%. Random-split sanity check yields 0.14\% C items. Architecture mixing contributed $\sim$2pp of spurious DIF; the remaining 29\% is genuine signal.
85	
86	\subsection{Instability Decomposition}
87	
88	A natural concern is that item instability simply reflects ``models got better at those domains.'' We decompose temporal DIF variance:
89	
90	\begin{table}[h]
91	\centering
92	\caption{Instability decomposition: DIF variance attribution.}
93	\label{tab:decomposition}
94	\begin{tabular}{lccc}
95	\toprule
96	Predictor & $\rho$ & $p$ & Variance explained (\%) \\
97	\midrule
98	Domain accuracy improvement & 0.307 & 0.020 & 9.4 \\
99	Partial $\rho$ (residual) & 0.220 & 0.012 & 4.8 \\
100	Total temporal C variance & --- & --- & 100.0 \\
101	\bottomrule
102	\end{tabular}
103	\end{table}
104	
105	Domain-level accuracy improvement explains 9.4\% of item instability variance. After controlling for this, partial $\rho=0.22$ ($p=0.012$) remains significant: DIF captures genuine item function change---shifts in distractor attractiveness, reasoning chain difficulty, or cognitive demand---beyond aggregate capability gains.
106	
107	\subsection{Non-Uniform DIF Robustness Check}
108	
109	\begin{table}[h]
110	\centering
111	\caption{Non-uniform DIF method comparison (8 subjects tested).}
112	\label{tab:nonuniform}
113	\begin{tabular}{lccc}
114	\toprule
115	Method & C flags & Overlap with MH (\%) & Unique flags (\%) \\
116	\midrule
117	MH (standard) & 3,627 & 100.0 & 26.2 \\
118	SIBTEST & 2,814 & 78.0 & 4.2 \\
119	Logistic regression & 2,951 & 81.3 & 3.8 \\
120	\bottomrule
121	\end{tabular}
122	\end{table}
123	
124	78\% of SIBTEST flags overlap with MH, confirming MH captures the dominant uniform DIF pattern. The median $R^2$ for the logistic regression interaction term is 0.008---non-uniform DIF exists but is secondary. MH is adequate for this population.
125	
126	%==============================================================================
127	\section{Robustness to Reasoning-RL Compositions}\label{sec:rl}
128	
129	A practical concern for DIF deployment is robustness to novel training paradigms, particularly reinforcement learning from reasoning (GRPO, PPO). We compare DIF's group-level robustness against traditional per-model detectors.
130	
131	\subsection{DIF Flag Stability}
132	
133	\begin{table}[h]
134	\centering
135	\caption{DIF flag retention across cohort compositions.}
136	\label{tab:rl_stability}
137	\begin{tabular}{lcccc}
138	\toprule
139	Cohort & $N$ & Temporal C\% & Flag retention & 95\% CI \\
140	\midrule
141	SFT-only & 1,843 & 30.8 & 1.00 & --- \\
142	Alignment-RL & 477 & 32.1 & 0.91 & [0.87, 0.95] \\
143	SFT + reasoning-RL & 1,856 & 31.0 & 0.89 & [0.84, 0.94] \\
144	All combined & 2,333 & 31.4 & 0.90 & [0.85, 0.94] \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	DIF flags remain 89--91\% stable when reasoning-RL models are added to the focal group. This stability follows from DIF's design: as a group-level statistic computed over entire cohorts, adding 13 reasoning-RL models to a focal group of $\sim$500 changes composition by $<$3\%.
150	
151	\subsection{Comparison with Traditional Detectors}
152	
153	\begin{table}[h]
154	\centering
155	\caption{Traditional detector degradation on reasoning-RL models.}
156	\label{tab:rl_detectors}
157	\begin{tabular}{lcccc}
158	\toprule
159	Detector & AUROC (non-RL) & AUROC (reasoning-RL) & $\Delta$ & DeLong $p$ \\
160	\midrule
161	ConStat & 0.73 & 0.54 & $-$0.19 & 0.003 \\
162	Min-K\% & 0.68 & 0.51 & $-$0.17 & 0.008 \\
163	DIF (group flag) & 0.88 & 0.86 & $-$0.02 & 0.71 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	Traditional detectors operating at the individual model level degrade significantly on reasoning-RL models (AUROC drops of 0.17--0.19, DeLong $p<0.01$). Reasoning-RL training with PPO/GRPO contracts the NLL gap between memorized and non-memorized items, directly degrading per-model distributional signatures. DIF's group-level conditioning makes it agnostic to individual training procedures.
169	
170	\paragraph{Limitations.} The reasoning-RL sample is small ($N=13$). Bootstrap CIs are wide [0.84, 0.94]. We report this as supporting evidence with explicit caveats.
171	
172	%==============================================================================
173	\section{Complementary Detection Methods}\label{sec:complementary}
174	
175	While DIF is our primary tool, we characterize the detection landscape through complementary methods operating on orthogonal signals.
176	
177	\subsection{ConStat Perturbation Testing}
178	
179	ConStat detects contamination by measuring performance drop on semantically equivalent reformulations. We reformulate 237 MMLU items and test 42 non-RL and 11 reasoning-RL models.
180	
181	\begin{table}[h]
182	\centering
183	\caption{ConStat detection power by model type and contamination type.}
184	\label{tab:constat}
185	\begin{tabular}{llccc}
186	\toprule
187	Model type & Contam.\ type & AUROC & TPR@FPR=0.10 & $N$ \\
188	\midrule
189	Non-RL & Verbatim & 0.74 & 0.42 & 42 \\
190	Non-RL & Variant & 0.61 & 0.24 & 42 \\
191	Reasoning-RL & Verbatim & 0.55 & 0.18 & 11 \\
192	Reasoning-RL & Variant & 0.48 & 0.09 & 11 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	ConStat works well on non-RL models (AUROC$=$0.74 for verbatim contamination) where memorization creates a sharp original-vs-reformulation gap. On reasoning-RL models, PPO/GRPO generalizes memorized knowledge to nearby phrasings, collapsing the perturbation signal. Jaccard overlap between ConStat and DIF flags is only 0.18---the methods capture fundamentally different contamination dimensions.
198	
199	\subsection{DVD Generation Variance Analysis}
200	
201	DVD exploits generation-time behavioral signatures: memorized items produce consistently correct answers across temperature samples (low variance). We test 12 open-weight models with 50 responses per item ($T=0.8$) across 500 items.
202	
203	\begin{table}[h]
204	\centering
205	\caption{DVD generation variance statistics by item category.}
206	\label{tab:dvd}
207	\begin{tabular}{lccc}
208	\toprule
209	Item category & Mean variance & Std & Bimodal (\%) \\
210	\midrule
211	Clean items & 0.34 & 0.12 & 3.1 \\
212	DIF-flagged items & 0.29 & 0.15 & 8.7 \\
213	Injected verbatim & 0.18 & 0.09 & 12.4 \\
214	Injected variant & 0.31 & 0.13 & 5.2 \\
215	\bottomrule
216	\end{tabular}
217	\end{table}
218	
219	Contaminated items show roughly half the generation variance of clean items (ratio$=$1.89). DVD achieves AUROC$=$0.67 for verbatim contamination but drops to 0.53 for variant contamination. Jaccard overlap with DIF is 0.13---DVD captures a unique signal dimension inaccessible to group-level statistics. Total cost: 58 GPU-hours.
220	
221	\subsection{Multi-Signal Ensemble Fusion}
222	
223	We fuse DIF, ConStat, and DVD via majority voting and calibrated weighted fusion.
224	
225	\begin{table}[h]
226	\centering
227	\caption{Ensemble performance comparison.}
228	\label{tab:ensemble}
229	\begin{tabular}{lcccc}
230	\toprule
231	Strategy & FPR & TPR (verbatim) & TPR (variant) & AUROC \\
232	\midrule
233	DIF only & 0.04 & 0.48 & 0.12 & 0.76 \\
234	ConStat only & 0.06 & 0.42 & 0.24 & 0.71 \\
235	DVD only & 0.08 & 0.28 & 0.19 & 0.64 \\
236	Majority (2/3) & 0.07 & 0.58 & 0.34 & 0.79 \\
237	Weighted fusion & 0.06 & 0.64 & 0.39 & 0.82 \\
238	Uniform weight & 0.07 & 0.61 & 0.36 & 0.79 \\
239	\bottomrule
240	\end{tabular}
241	\end{table}
242	
243	Weighted fusion (DIF: 0.45, ConStat: 0.35, DVD: 0.20) achieves AUROC$=$0.82, a +0.06 gain over DIF alone. The three detectors exploit orthogonal signals: group-level response patterns (DIF), per-model perturbation sensitivity (ConStat), and generation variance (DVD). Cross-validation confirms stability (5-fold AUROC std$=$0.03). Variant contamination remains the hardest case (TPR$=$0.39).
244	
245	%==============================================================================
246	\section{Continuous Monitoring Extensions}\label{sec:monitoring}
247	
248	\subsection{Item-Focused Trees}
249	
250	Item-Focused Trees (IFT) treat model release date as a continuous covariate, avoiding the arbitrary 2023/2024-H1 categorical boundary.
251	
252	\begin{table}[h]
253	\centering
254	\caption{IFT vs.\ categorical DIF detection comparison.}
255	\label{tab:ift}
256	\begin{tabular}{lccccc}
257	\toprule
258	Method & Significant (\%) & Unique (\%) & FPR & Power ($\delta$=1.4) & $\kappa$ \\
259	\midrule
260	Categorical MH & 31.3 & 2.4 & 0.042 & 0.68 & --- \\
261	IFT (continuous) & 34.7 & 5.8 & 0.041 & 0.72 & 0.74 \\
262	Intersection & 28.9 & --- & --- & --- & --- \\
263	\bottomrule
264	\end{tabular}
265	\end{table}
266	
267	81.2\% overlap between IFT and categorical DIF validates the temporal boundary choice. IFT reveals additional nuance: 76.1\% of significant items show abrupt change patterns (sudden capability jumps at specific model generations), while 23.9\% exhibit gradual drift (continuous capability improvement). The modal optimal split date is 2023-09, close to our categorical cutoff.
268	
269	\begin{table}[h]
270	\centering
271	\caption{IFT drift pattern classification.}
272	\label{tab:ift_patterns}
273	\begin{tabular}{lcll}
274	\toprule
275	Pattern & \% of significant & Example domain & Interpretation \\
276	\midrule
277	Abrupt change & 76.1 & Abstract algebra & Sudden capability jump \\
278	Gradual drift & 23.9 & HS mathematics & Continuous improvement \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	\subsection{Cumulative Bayesian DIF}
284	
285	For longitudinal monitoring, we simulate cumulative Bayesian DIF across 4 successive administrations, where each administration's posterior becomes the next prior.
286	
287	\begin{table}[h]
288	\centering
289	\caption{Cumulative Bayesian DIF power by administration count.}
290	\label{tab:bayesian}
291	\begin{tabular}{lcccc}
292	\toprule
293	Administrations & Power ($\delta$=0.8) & Power ($\delta$=1.0) & Power ($\delta$=1.4) & FPR \\
294	\midrule
295	1 & 0.22 & 0.41 & 0.68 & 0.048 \\
296	2 & 0.35 & 0.57 & 0.81 & 0.033 \\
297	3 & 0.47 & 0.71 & 0.89 & 0.025 \\
298	4 & 0.54 & 0.77 & 0.93 & 0.022 \\
299	\bottomrule
300	\end{tabular}
301	\end{table}
302	
303	At medium effect size ($\delta=1.0$), single-administration power is only 0.41, but cumulative evidence raises this to 0.71 after 3 administrations and 0.77 after 4. Simultaneously, FPR decreases from 0.048 to 0.022 via Bayesian shrinkage---transient false positives are not reinforced across administrations. Posterior credible interval width reduces by 38\%. This provides a principled framework for longitudinal benchmark monitoring: persistent effects are reliably detected even when individual time points lack power.
304	
305	%==============================================================================
306	\section{Toward Benchmark Maintenance}\label{sec:maintenance}
307	
308	\subsection{Bifactor IRT Equating}
309	
310	We pilot a principled psychometric framework for item replacement using bifactor IRT with fixed-parameter calibration.
311	
312	\begin{table}[h]
313	\centering
314	\caption{Bifactor model fit and factor structure.}
315	\label{tab:bifactor}
316	\begin{tabular}{lcc}
317	\toprule
318	Factor & Variance explained (\%) & Items loading $>$0.3 \\
319	\midrule
320	General & 61.3 & 12,508 \\
321	Subject-specific (mean) & 15.8 & 219 \\
322	Subject-specific (min) & 8.2 & 87 \\
323	Subject-specific (max) & 27.4 & 412 \\
324	\bottomrule
325	\end{tabular}
326	\end{table}
327	
328	The bifactor model fits excellently (RMSEA$=$0.019, CFI$=$0.978). The general factor explains 61.3\% of variance, confirming a dominant unidimensional signal (supporting simpler IRT adequacy for ranking). Anchor items (no DIF flag, discrimination$>$0.5, fit residual$<$2.0) comprise 48.8\% of items ($N=$6,107).
329	
330	\begin{table}[h]
331	\centering
332	\caption{Equating quality by replacement rate.}
333	\label{tab:equating}
334	\begin{tabular}{lcccc}
335	\toprule
336	Replacement (\%) & $N$ replaced & Spearman $\rho$ & RMSE & Max rank change \\
337	\midrule
338	5 & 625 & 0.998 & 0.41 & 23 \\
339	10 & 1,251 & 0.994 & 0.89 & 54 \\
340	20 & 2,502 & 0.987 & 1.34 & 89 \\
341	31 & 3,918 & 0.976 & 1.83 & 127 \\
342	\bottomrule
343	\end{tabular}
344	\end{table}
345	
346	At 31\% replacement (replacing all DIF-flagged items), equated scores maintain $\rho=0.976$ with original rankings. Fixed-parameter calibration converges for 94.2\% of replacement items. Equated benchmarks can refresh the most unstable items with controlled validity loss.
347	
348	\subsection{Item Generation and Calibration}
349	
350	We evaluate LLM-based item generation targeting DIF-flagged items, comparing difficulty calibration methods.
351	
352	\begin{table}[h]
353	\centering
354	\caption{Difficulty calibration method comparison for generated items.}
355	\label{tab:itemgen}
356	\begin{tabular}{lccc}
357	\toprule
358	Method & Difficulty $r$ & Discrimination $r$ & Within 0.15 logits (\%) \\
359	\midrule
360	Prompt-based targeting & 0.32 & 0.18 & 24 \\
361	Student simulation & 0.78 & 0.64 & 68 \\
362	Student sim + iterative & 0.84 & 0.71 & 82 \\
363	\bottomrule
364	\end{tabular}
365	\end{table}
366	
367	Student simulation substantially outperforms naive prompt-based generation ($r=0.78$ vs.\ 0.32 for difficulty). Of 1,500 generated replacements for 500 DIF-flagged items, 75.1\% pass quality checks. A holdout panel of 30 models yields $\rho=0.971$ between original and replacement item scores, confirming measurement function preservation. Cognitive level matching reaches 82.4\% (LLMs reproduce factual/comprehension items well but struggle with higher Bloom levels). Total cost: 173 GPU-hours.
368	
369	\subsection{Graceful Degradation Analysis}
370	
371	We characterize validity degradation under progressive item replacement with theoretical bounds.
372	
373	\begin{table}[h]
374	\centering
375	\caption{Validity metrics under progressive replacement.}
376	\label{tab:degradation}
377	\begin{tabular}{lcccc}
378	\toprule
379	Replacement (\%) & Spearman $\rho$ & SHR & Construct coverage & Max rank $\Delta$ \\
380	\midrule
381	0 & 1.000 & 0.9934 & 1.000 & 0 \\
382	5 & 0.9991 & 0.9928 & 0.997 & 18 \\
383	10 & 0.9984 & 0.9921 & 0.993 & 42 \\
384	20 & 0.9962 & 0.9904 & 0.984 & 78 \\
385	31 & 0.9938 & 0.9886 & 0.972 & 127 \\
386	50 & 0.9871 & 0.9842 & 0.951 & 203 \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	MMLU tolerates $\sim$27\% replacement while maintaining $\rho>0.99$. The critical rate aligns with the empirical finding that 31\% DIF removal yields $\rho=0.996$---replacement with equated items is less disruptive than removal, because equating preserves the dominant general factor. Construct coverage (proportion of domains with $\geq$10 items) stays above 0.95 even at 50\% replacement, reflecting MMLU's 57 subjects averaging 219 items each. Theoretical bounds: $\rho \geq 1 - O(r \cdot (1-\rho^2_\text{anchor}))$ where $r$ is replacement rate and $\rho_\text{anchor}$ is anchor item reliability.
392	
393	%==============================================================================
394	\section{Discussion}
395	
396	\paragraph{Principal finding.} 28--30\% of MMLU items are functionally unstable across model generations in an architecture-homogeneous population with excellent IRT fit. This is not a statistical artifact (sanity check: 0.14\%), not primarily an architecture mixing effect (decoder-only: 29.1\% vs.\ full: 31.3\%), and not fully explained by capability improvement (partial $\rho=0.22$ after controlling domain accuracy). The instability is a structural property of the benchmark-model ecosystem.
397	
398	\paragraph{Implications for contamination research.} The field's reliance on web-overlap labels for item-level validation has a fundamental blind spot. Our semi-synthetic framework ($\Delta$TPR methodology with cross-subject matching) provides infrastructure for validating any item-level detector. The multi-signal ensemble (AUROC$=$0.82) demonstrates complementary value, but each component operates on different contamination dimensions---no single method is sufficient.
399	
400	\paragraph{Operational recommendations.} For benchmark maintainers: (1) run temporal DIF as routine diagnostic after each evaluation cycle; (2) use cumulative Bayesian DIF for medium-effect detection; (3) consider equating-based item rotation for the 28--30\% most unstable items; (4) report IRT fit indices alongside benchmark scores. For contamination researchers: (5) validate detectors against semi-synthetic injections, not web-overlap labels; (6) use cross-subject matching to avoid FPR inflation.
401	
402	\paragraph{Limitations.} The reasoning-RL robustness finding rests on $N=13$ models. ConStat and DVD experiments use smaller subsets than the main DIF analysis. The semi-synthetic injection mechanism (incorrect$\to$correct flipping) simplifies real contamination pathways. Generalization beyond MMLU and GSM8K requires further validation. Higher-order methods (MIMIC, propensity-score matching, multidimensional IRT) may address confounding that our decomposition approach cannot fully resolve.
403	
404	%==============================================================================
405	\section{Conclusion}
406	
407	Psychometric analysis of the METABENCH response matrix reveals that LLM benchmarks harbor structural instabilities invisible to existing contamination detection methodology. Nearly one-third of MMLU items function differently across model generations---a finding that persists after controlling for architecture heterogeneity, IRT model misfit, and aggregate capability improvement. The standard validation approach using web-overlap labels cannot detect this differential signal. We provide a semi-synthetic framework, demonstrate DIF's robustness advantage over per-model detectors under reasoning-RL, and sketch a principled path toward equating-based benchmark maintenance. These findings argue for integrating psychometric monitoring into the benchmark evaluation lifecycle.
408	
409	%==============================================================================
410	\bibliographystyle{plainnat}
411	\begin{thebibliography}{20}
412	
413	\bibitem[Holland \& Thayer(1988)]{holland1988}
414	Holland, P.~W. \& Thayer, D.~T. (1988).
415	\newblock Differential item performance and the Mantel-Haenszel procedure.
416	\newblock \emph{Test Validity}, pp.\ 129--145.
417	
418	\bibitem[Li et~al.(2024)]{li2024}
419	Li, Y., et~al. (2024).
420	\newblock Open LLM Leaderboard contamination detection.
421	\newblock \emph{arXiv preprint}.
422	
423	\bibitem[Oren et~al.(2024)]{oren2024}
424	Oren, Y., et~al. (2024).
425	\newblock Proving test set contamination in black-box language models.
426	\newblock \emph{ICLR 2024}.
427	
428	\bibitem[Srivastava et~al.(2023)]{srivastava2023}
429	Srivastava, A., et~al. (2023).
430	\newblock Beyond the imitation game: Quantifying and extrapolating the capabilities of language models.
431	\newblock \emph{TMLR}.
432	
433	\bibitem[Sinharay et~al.(2006)]{sinharay2006}
434	Sinharay, S., et~al. (2006).
435	\newblock Bayesian methods for assessing differential item functioning.
436	\newblock \emph{Journal of Educational and Behavioral Statistics}, 31(3), 261--276.
437	
438	\bibitem[Tutz \& Berger(2016)]{tutz2016}
439	Tutz, G. \& Berger, M. (2016).
440	\newblock Item-focused trees for the identification of items in differential item functioning.
441	\newblock \emph{Psychometrika}, 81(3), 727--750.
442	
443	\bibitem[Polo et~al.(2024)]{polo2024}
444	Polo, F.~M., et~al. (2024).
445	\newblock METABENCH: A large-scale meta-evaluation of LLM benchmarks.
446	\newblock \emph{arXiv preprint}.
447	
448	\bibitem[Zhu et~al.(2024)]{zhu2024}
449	Zhu, K., et~al. (2024).
450	\newblock ConStat: Performance-based contamination detection in large language models.
451	\newblock \emph{arXiv preprint}.
452	
453	\bibitem[Shi et~al.(2024)]{shi2024}
454	Shi, W., et~al. (2024).
455	\newblock Detecting pretraining data from large language models.
456	\newblock \emph{ICLR 2024}.
457	
458	\bibitem[Zhang et~al.(2024)]{zhang2024}
459	Zhang, Y., et~al. (2024).
460	\newblock GSM1K: A natural benchmark for measuring LLM mathematical reasoning without data contamination.
461	\newblock \emph{arXiv preprint}.
462	
463	\end{thebibliography}
464	
465	\end{document}
466	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "52c5cd79-9ae7-4357-9ee5-1f8e664b3f6d"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a72be29fc97d53c64",
  "tool_use_id": "toolu_01WPG47LphyN5tF23nLqZUbh",
  "status": "completed",
  "output_file": "",
  "summary": "Find method section and writing plan",
  "usage": {
    "total_tokens": 66612,
    "tool_uses": 14,
    "duration_ms": 45358
  },
  "uuid": "dba68d55-c9fb-4551-8560-db5b2ddd89b4",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0"
}
```

---

### Tool result

_source line 77 · 2026-05-21T04:01:47.989Z_

<details><summary>↩ Tool result · `toolu_01WPG47LphyN5tF23nLqZUbh`</summary>

```text
Perfect! Now I have all the information needed. Let me compile a comprehensive summary for you.

## Summary: Notation, Terminology, and Established Context

I've found and read all the key project files. Here's what has been established in earlier sections and planning documents:

### **Key Files Located:**

1. **writing_plan.yaml** - Comprehensive paper outline with 4 main claims and detailed section budgets
2. **paper/main.tex** - Document structure (imports from sections/)
3. **paper/math_commands.tex** - LaTeX notation definitions
4. **paper_framing.md** - Core framing, story spine, and anticipated concerns
5. **Dream report** (most recent) - Generated paper sections with Abstract, Introduction, Methods content

### **Core Notation Established:**

From the math_commands.tex and writing_plan:

| Symbol | Meaning |
|--------|---------|
| **θ** | Latent ability (IRT - Item Response Theory) |
| **Δ_MH** | Mantel-Haenszel DIF statistic (log-odds ratio) |
| **p** | Exploitation rate in semi-synthetic injection |
| **C%** | Percentage of items classified ETS C (large DIF, \|Δ_MH\| ≥ 1.5) |
| **ΔTPR** | TPR increase from semi-synthetic injection over baseline |
| **ΔFPR** | FPR change from semi-synthetic injection (should be 0 for valid framework) |
| **ρ** | Spearman/Pearson correlation coefficient |
| **enrichment** | Detection overlap metric between DIF flags and web-overlap labels |
| **RMSEA, CFI, TLI, SRMR** | IRT model fit indices (confirmatory factor analysis) |

### **Key Terminology & Concepts Already Established:**

1. **DIF (Differential Item Functioning)**: "Items function differently across groups after controlling for ability" — applies here to temporal cohorts (2023 vs 2024 models)

2. **ETS Classification Thresholds**:
   - **A**: |Δ_MH| < 1.0 (negligible DIF)
   - **B**: 1.0 ≤ |Δ_MH| < 1.5 (moderate DIF)
   - **C**: |Δ_MH| ≥ 1.5 (large DIF) ← **primary finding**

3. **Primary Finding**: **31–38% of MMLU items exhibit ETS C DIF**
   - Temporal cohort: 31.3% (2023 vs 2024-H1 models, N=1,253/656)
   - Within-subject average: 38.1% across 5 MMLU subjects
   - Decoder-only (architecture-stratified): 29.1%
   - Sanity check (random split): 0.18% (confirms non-random)

4. **Ground Truth Meta-critique**: Web-overlap contamination labels measure *global exposure* (whether item is publicly accessible), NOT *differential contamination* (whether item functions differently across cohorts). Enrichment ≈ 1.0 is expected, not failure.

5. **Semi-synthetic Framework**: Inject controlled differential contamination by flipping incorrect→correct responses at rate p ∈ {0.3, 0.5, 0.7, 1.0}. Measure ΔTPR as detection power increase.
   - Key innovation: **Cross-subject matching** (use total score on OTHER subjects as matching variable) eliminates FPR inflation (ΔFPR = 0.000)
   - Results: ΔTPR = +0.508 on MMLU (p=0.5), ΔTPR = +0.818 on GSM8K

6. **IRT Model Fit Metrics**:
   - Full population: RMSEA = 0.067, CFI = 0.874, TLI = 0.851
   - Decoder-only subset: RMSEA = 0.024, CFI = 0.966, TLI = 0.958 (excellent fit)

7. **Downstream Impact Analysis**:
   - Benchmark redundancy: ρ ≈ 0.997 full vs stable-only rankings (massively redundant)
   - DIF items carry more discriminative signal (removal causes z = -8 to -49σ disruption vs random removal)
   - Cross-benchmark validation: DIF-C items anti-correlate with contamination gap (r = −0.478, p = 0.005, N = 33)

### **Four Core Claims (Falsifiable):**

1. **Temporal Comparability Concern**: 31–38% item instability, robust across thresholds and methodology
2. **Ground Truth Meta-critique**: Web-overlap labels cannot evaluate differential contamination (validation methodology gap in contamination detection field)
3. **Semi-synthetic Framework**: Cross-subject matching eliminates FPR inflation; generalizes to GSM8K
4. **DIF as Diagnostic Lens**: Four-layer finding — benchmark redundancy, signal concentration, diagnostic value, contamination resistance

### **Established Data/Model Parameters:**

- **METABENCH Dataset**: 5,227 models × 12,508 MMLU items
- **Temporal Cohorts**: 
  - Reference: 2023 models (N = 1,253)
  - Focal: 2024-H1 models (N = 656)
- **GSM8K Validation**: 1,319 items × 6,702 models
- **Architecture Breakdown**: 99.98% decoder-only (5,226/5,227)

### **Key Caveats Already Discussed:**

- Item difficulty may be mediator (not confounder) for domain improvement relationship
- Semi-synthetic injection (incorrect→correct flipping) simplifies real contamination pathways
- Reasoning-RL robustness evidence small (N = 13 models)
- GSM1K correlation evidence suggestive (N = 33, wide CIs)
- Cannot fully decompose 92.4% of instability unrelated to domain improvement

### **Files Available for Your Method Section:**

The writing_plan.yaml already specifies the Method section (§3) should cover:
- **3.1**: Data description (METABENCH + Li et al. labels)
- **3.2**: MH-DIF + ETS classification (with ML-audience translation: examinees→models, items→questions)
- **3.3**: Cohort designs (temporal, ability-quintile, within-family, within-subject)
- **3.4**: Semi-synthetic injection framework with cross-subject matching
- **3.5**: Diagnostics (Yen's Q3 for local independence, domain-specificity analysis)
- **3.6**: Multiple testing considerations (ETS dual threshold provides implicit protection, BH FDR has minimal impact)

All the section .tex files currently exist in `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/` but are empty — they're ready to be populated with your method section content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "924cb1c6-088b-4a42-8f5d-9a5cb5c01da9",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find and read these files in the project /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/:\n1. Any method section tex file (likely paper/sections/method.tex)\n2. writing_plan.yaml or similar planning files\n3. Any existing section tex files (abstract.tex, introduction.tex, etc.)\n\nRead the full content of any files you find and report them back to me. I need to understand what notation and terminology has been established in earlier sections.",
    "agentId": "a72be29fc97d53c64",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me compile a comprehensive summary for you.\n\n## Summary: Notation, Terminology, and Established Context\n\nI've found and read all the key project files. Here's what has been established in earlier sections and planning documents:\n\n### **Key Files Located:**\n\n1. **writing_plan.yaml** - Comprehensive paper outline with 4 main claims and detailed section budgets\n2. **paper/main.tex** - Document structure (imports from sections/)\n3. **paper/math_commands.tex** - LaTeX notation definitions\n4. **paper_framing.md** - Core framing, story spine, and anticipated concerns\n5. **Dream report** (most recent) - Generated paper sections with Abstract, Introduction, Methods content\n\n### **Core Notation Established:**\n\nFrom the math_commands.tex and writing_plan:\n\n| Symbol | Meaning |\n|--------|---------|\n| **θ** | Latent ability (IRT - Item Response Theory) |\n| **Δ_MH** | Mantel-Haenszel DIF statistic (log-odds ratio) |\n| **p** | Exploitation rate in semi-synthetic injection |\n| **C%** | Percentage of items classified ETS C (large DIF, \\|Δ_MH\\| ≥ 1.5) |\n| **ΔTPR** | TPR increase from semi-synthetic injection over baseline |\n| **ΔFPR** | FPR change from semi-synthetic injection (should be 0 for valid framework) |\n| **ρ** | Spearman/Pearson correlation coefficient |\n| **enrichment** | Detection overlap metric between DIF flags and web-overlap labels |\n| **RMSEA, CFI, TLI, SRMR** | IRT model fit indices (confirmatory factor analysis) |\n\n### **Key Terminology & Concepts Already Established:**\n\n1. **DIF (Differential Item Functioning)**: \"Items function differently across groups after controlling for ability\" — applies here to temporal cohorts (2023 vs 2024 models)\n\n2. **ETS Classification Thresholds**:\n   - **A**: |Δ_MH| < 1.0 (negligible DIF)\n   - **B**: 1.0 ≤ |Δ_MH| < 1.5 (moderate DIF)\n   - **C**: |Δ_MH| ≥ 1.5 (large DIF) ← **primary finding**\n\n3. **Primary Finding**: **31–38% of MMLU items exhibit ETS C DIF**\n   - Temporal cohort: 31.3% (2023 vs 2024-H1 models, N=1,253/656)\n   - Within-subject average: 38.1% across 5 MMLU subjects\n   - Decoder-only (architecture-stratified): 29.1%\n   - Sanity check (random split): 0.18% (confirms non-random)\n\n4. **Ground Truth Meta-critique**: Web-overlap contamination labels measure *global exposure* (whether item is publicly accessible), NOT *differential contamination* (whether item functions differently across cohorts). Enrichment ≈ 1.0 is expected, not failure.\n\n5. **Semi-synthetic Framework**: Inject controlled differential contamination by flipping incorrect→correct responses at rate p ∈ {0.3, 0.5, 0.7, 1.0}. Measure ΔTPR as detection power increase.\n   - Key innovation: **Cross-subject matching** (use total score on OTHER subjects as matching variable) eliminates FPR inflation (ΔFPR = 0.000)\n   - Results: ΔTPR = +0.508 on MMLU (p=0.5), ΔTPR = +0.818 on GSM8K\n\n6. **IRT Model Fit Metrics**:\n   - Full population: RMSEA = 0.067, CFI = 0.874, TLI = 0.851\n   - Decoder-only subset: RMSEA = 0.024, CFI = 0.966, TLI = 0.958 (excellent fit)\n\n7. **Downstream Impact Analysis**:\n   - Benchmark redundancy: ρ ≈ 0.997 full vs stable-only rankings (massively redundant)\n   - DIF items carry more discriminative signal (removal causes z = -8 to -49σ disruption vs random removal)\n   - Cross-benchmark validation: DIF-C items anti-correlate with contamination gap (r = −0.478, p = 0.005, N = 33)\n\n### **Four Core Claims (Falsifiable):**\n\n1. **Temporal Comparability Concern**: 31–38% item instability, robust across thresholds and methodology\n2. **Ground Truth Meta-critique**: Web-overlap labels cannot evaluate differential contamination (validation methodology gap in contamination detection field)\n3. **Semi-synthetic Framework**: Cross-subject matching eliminates FPR inflation; generalizes to GSM8K\n4. **DIF as Diagnostic Lens**: Four-layer finding — benchmark redundancy, signal concentration, diagnostic value, contamination resistance\n\n### **Established Data/Model Parameters:**\n\n- **METABENCH Dataset**: 5,227 models × 12,508 MMLU items\n- **Temporal Cohorts**: \n  - Reference: 2023 models (N = 1,253)\n  - Focal: 2024-H1 models (N = 656)\n- **GSM8K Validation**: 1,319 items × 6,702 models\n- **Architecture Breakdown**: 99.98% decoder-only (5,226/5,227)\n\n### **Key Caveats Already Discussed:**\n\n- Item difficulty may be mediator (not confounder) for domain improvement relationship\n- Semi-synthetic injection (incorrect→correct flipping) simplifies real contamination pathways\n- Reasoning-RL robustness evidence small (N = 13 models)\n- GSM1K correlation evidence suggestive (N = 33, wide CIs)\n- Cannot fully decompose 92.4% of instability unrelated to domain improvement\n\n### **Files Available for Your Method Section:**\n\nThe writing_plan.yaml already specifies the Method section (§3) should cover:\n- **3.1**: Data description (METABENCH + Li et al. labels)\n- **3.2**: MH-DIF + ETS classification (with ML-audience translation: examinees→models, items→questions)\n- **3.3**: Cohort designs (temporal, ability-quintile, within-family, within-subject)\n- **3.4**: Semi-synthetic injection framework with cross-subject matching\n- **3.5**: Diagnostics (Yen's Q3 for local independence, domain-specificity analysis)\n- **3.6**: Multiple testing considerations (ETS dual threshold provides implicit protection, BH FDR has minimal impact)\n\nAll the section .tex files currently exist in `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/` but are empty — they're ready to be populated with your method section content."
      }
    ],
    "totalDurationMs": 45361,
    "totalTokens": 68216,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 9647,
      "cache_read_input_tokens": 56833,
      "output_tokens": 1731,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9647
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1731,
          "cache_read_input_tokens": 56833,
          "cache_creation_input_tokens": 9647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9647,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 2,
      "bashCount": 7,
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

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the paper's notation, terminology, and framing. Let me write the experiments section. Let me also check the task outline numbers more carefully against the data summary.

Key things to remember:
- ICLR single column format
- ~2500 words
- booktabs for tables
- No em-dashes, no -ing phrase endings, no "Furthermore/Moreover/Additionally" chains
- No "It is worth noting" / "Notably"
- No "delve" / "leverage" / "utilize" / "facilitate"
- No comments in LaTeX code


- "significantly" only with statistical test
- Don't start section with "In this section, we..."
- Don't use \begin{center} for tables; use \centering
- Caption ABOVE tables, BELOW figures
- Paragraphs 5-8 sentences
- Discovery/characterization paper tone

I need to verify the numbers from the task instructions: N_ref / N_focal should be 1,080 / 807 according to Table 1, not the 1,253 / 656 that the Explore agent found. I'll use the task-specified values as those are authoritative. I also need to track down the bibtex key for one of the references.

Now I'm structuring the longest section of the paper—about 2,500 words across 8 subsections with 3 tables and 4 figures. The key sections are validation under controlled conditions, temporal comparability showing 31% item instability, ground truth mismatch, structural analysis, semi-synthetic framework validation, local independence checks, and downstream impact. I need to be careful about which findings get the most emphasis and ensure the flow builds logically through the evidence.

Writing the LaTeX now with precise attention to the reference names, exact numbers from the task outline, and proper table formatting for the five-column structures. I'm reviewing the notation requirements and structuring the Experiments section with tight empirical prose. The section needs about 2500 words across eight subsections, so I'm planning each one carefully to support specific claims with evidence. I'll start with power analysis showing strong detection metrics on ETS C items, then move into the main temporal DIF finding where 31.3% of items show classification as C, with Benjamini-Hochberg correction removing only three items—suggesting the signal is robust rather than an artifact of multiple testing.

Now I'm working through the key robustness checks: the random split sanity check shows only 0.18% contamination, and when I look within Llama-2 across versions I see 61.3% classification but that's confounded by ability differences. Once I control for ability quintiles the rate drops to 2.9%, which validates that the method isolates temporal DIF rather than picking up general model improvement. Domain correlation is modest at 0.307, within-subject contamination runs 38.1%, and the instability decomposition reveals 92.4% of the variation is unrelated to domain improvement—all pointing to temporal DIF as the primary signal. Architecture isn't a confound since 99.98% of items are decoder-only, and the method remains robust across threshold sensitivity from 10.2% to 48.9%.

For the enrichment analysis, I'm comparing against Li et al.'s approach: my method achieves 0.96 enrichment versus their baseline, and the semi-synthetic validation shows substantial TPR gains of +0.508 and +0.674 across conditions. The methods measure different aspects of contamination, which explains why DIF works well for temporal effects but their labels capture something distinct. Finally, I'm testing three structural approaches to explain the DIF but all fail, so I'm moving toward the matched-ability analysis.

The matched-ability enrichment holds steady at 0.94-1.04, theta-conditioning shows near-perfect correlation at r=0.9986 with FPR unchanged, and within-subject contamination remains at 38.1%. Cross-subject matching reveals zero FPR change overall but 4 out of 5 subjects show TPR shifts above 0.3, while within-subject FPR inflates by 0.186. The Q3 analysis finds 11.3% versus 2.2% of pairs in the third quartile—a 5-fold difference with strong significance—suggesting mild local dependence that contributes but isn't the main driver. Diving into the layer-wise decomposition, Layer 1 shows near-perfect correlation at ρ≈0.997, Layer 2 contains extreme DIF items ranging from z=-8 to -49 sigma but the circularity ablation reveals DIF is actually the least disruptive factor, and I'm examining Layer 3 next.

Continuing with the layer analysis and cross-validation results...

On GSM8K, temporal contamination sits at 18.9% with sanity checks at 0.3%, semi-synthetic gains show TPR improvement of 0.818 but without significance (p=0.7), and on GSM1K I'm seeing a negative correlation of r=-0.478 (p=0.005, N=33)—which contradicts my original hypothesis predicting positive effects. The DIF-contaminated items prove resistant to the gains I expected. Now I need to write the LaTeX for these results, keeping tables compact for the single-column ICLR format.

Writing LaTeX tables... I'm setting up my label structure for all the sections, tables, and figures I'll reference throughout—experiments, validation, temporal analysis, structural comparisons, downstream tasks, and the GSM8K results. Now I'll write out the full LaTeX section, being careful to avoid em-dashes, gerund phrase endings, and any AI-related language.

I'm applying the MH-DIF framework to METABENCH, which contains 5,227 models tested on 12,508 MMLU items, and I'll organize my analysis around temporal cohorts defined by model release dates from 2023 and 2024. My approach covers validation of detection power through simulation, characterization of temporal instability, investigation of its structural causes, and assessment of how this affects benchmark rankings.

For the validation subsection, I'm running a power analysis using actual MMLU IRT parameters to verify that MH-DIF can reliably detect differential item functioning given METABENCH's sample sizes. I'll simulate response matrices with injected DIF of varying magnitudes to test detection sensitivity.

The simulation results show that at sample sizes of 80 or larger, the ETS C classification achieves strong performance with true positive rates between 0.68 and 0.80, false positive rates around 0.036 to 0.042, and AUC values of 0.93 to 0.94. These detection rates are more than adequate for my temporal analysis, where I have reference and focal cohorts of 1,080 and 807 models respectively, so statistical power won't be a constraint. The temporal comparability analysis reveals that roughly 31% of MMLU items exhibit instability across the two time periods.

When I compare the 2023 model cohort against the 2024 cohort, the ETS C classification flags 31.3% of items as unstable. Applying the Benjamini-Hochberg FDR correction barely changes this—it removes only 3 items—because the ETS dual threshold already provides built-in protection against multiple comparisons. To verify this instability is genuine, I'm running control conditions: splitting the 2023 cohort randomly yields only 0.18% flagged items, confirming the temporal signal isn't just noise, and I'm also checking whether ability-level differences could explain the pattern.

Now I'm looking at the Llama-2 versus Llama-3 comparison, which shows 61.3% ETS C items—much higher than the cross-year comparison. This makes sense because models from different generations within the same family have substantial ability gaps that confound the temporal effect, which aligns with what we know about how MH-DIF responds to ability differences. The instability also appears across MMLU subjects, with an average of 38.1% flagged items and a modest positive correlation between domain-level accuracy gains and the percentage of flagged items.

However, when I run item-level logistic regression, domain accuracy improvement only accounts for about 2.4 percentage points of the 31.3% temporal instability rate, leaving over 92% unexplained by aggregate domain-level improvements. Architecture heterogeneity isn't driving these results—the dataset is almost entirely decoder-only models, and removing the single encoder-decoder model doesn't change the findings. Threshold sensitivity checks show the results hold across different parameter settings.

Generating markdown table... Generating markdown table...

Now I'm looking at the ground truth mismatch section—the enrichment ratio of 0.96 for DIF flags against known contaminated items is essentially at chance level, which seems like a null result. But the semi-synthetic injection experiments should clarify whether DIF actually detects contamination through a dose-response relationship. The dose-response curve confirms that the detection method reliably identifies differential contamination as the exploitation rate increases, with near-zero false positives in the baseline case. Now I'm examining why three different analytical approaches—from matched-ability comparisons to more refined stratification methods—all fail to reduce the temporal false positive rate below 31%, suggesting this is a fundamental structural issue rather than a limitation of any single technique. Generating markdown table...

The key insight is that cross-subject matching—where I compute the matching variable from other subjects rather than the one being tested—achieves perfect FPR control with $\Delta\mathrm{FPR} = 0.000$, while within-subject matching inflates FPR by about 0.186 because the contamination affects the matching variable itself. I'm adopting cross-subject matching as the standard approach going forward.

Now I'm including a figure showing this comparison across the five MMLU subjects, demonstrating that cross-subject matching maintains strong detection power while eliminating false positive inflation. Moving into the next section on local independence, I'm examining Yen's Q3 statistic to measure residual correlations between item pairs after accounting for the latent trait.

The within-subject pairs show substantially higher local dependence—about 11% exceed the threshold compared to just 2% for cross-subject pairs, which is a significant difference. This mild dependence contributes to the elevated false positive rate in within-subject matching, though it's not the main culprit since the cross-subject protocol already handles this through external ability conditioning.

Now I'm shifting to the practical implications—whether this 31% item instability actually matters for how models are ranked and evaluated. I'm breaking this down into four analytical layers, starting with benchmark redundancy by comparing model rankings when using all items versus only the stable ones.

The correlation between these two ranking approaches is extremely high at 0.997, meaning removing unstable items barely changes the overall rankings. This makes sense given the massive item pool of over 12,000 items—there's enough statistical power that losing 31% doesn't meaningfully shift the order. Moving to the next layer, I'm examining whether unstable items actually carry more discriminative signal than random items of the same size, and the evidence is clear: removing DIF-flagged items is far more disruptive to ranking quality than removing random items, with effect sizes ranging from -8 to -49 standard deviations across different conditions. But here's the key insight—when I compare different removal strategies, DIF-based removal is actually the least harmful approach, whereas removing items by accuracy gaps or high variance produces much larger ranking disruptions.

The overlap between DIF-flagged items and high-discrimination items is minimal at 0.12, which tells me that DIF is capturing something specific about differential behavior rather than just general informativeness. Looking at individual model families, I'm seeing striking patterns: Phi-3 and Llama-3 models improve dramatically when evaluated only on stable items, gaining 700-850 rank positions, while Mistral-based merges move in the opposite direction, losing 400-587 positions. This suggests certain model families are particularly sensitive to items that shifted their behavior between 2023 and 2024. There's an important caveat though—among the top 50 models that moved the most in rankings, 49 of them have unknown family labels.

The DIF instability I'm observing isn't limited to MMLU. I'm seeing the same pattern replicate on GSM8K with cross-benchmark contamination checks, and the downstream impact visualization shows that despite near-perfect correlation overall, individual model families experience systematic rank shifts when evaluated on only the stable items.

Now I'm validating whether this temporal DIF effect generalizes across benchmarks. On GSM8K, the temporal cohort comparison yields 18.9% contamination versus 0.3% for random splits—lower than MMLU's 31.3%, which makes sense given GSM8K's more uniform structure focused on mathematical reasoning rather than MMLU's diverse subject coverage. The dose-response validation confirms strong detection power with the semi-synthetic approach.

I'm also cross-validating using MMLU scores to match models for GSM8K analysis, which shows the effect holds but with reduced magnitude. To further validate, I'm correlating each model's contamination gap—the difference between GSM8K and held-out GSM1K performance—with the ranking advantage from DIF-flagged items, finding a negative correlation around -0.478.

This is counterintuitive: I expected models with larger contamination gaps to benefit more from DIF items, but the data shows the opposite. Models that gain more from memorization actually benefit less from DIF-flagged items, suggesting these items capture genuine behavioral shifts rather than simple memorization effects. The result is modest in sample size but statistically significant and aligns with the interpretation that DIF reflects something deeper than contamination.

Generating comparison table... I'm verifying the table values against the task specifications—MMLU doesn't have a p=0.7 standard result, while GSM8K shows +0.818 for that condition and +0.514 for the p=0.5 external case, with MMLU at +0.508 for the same external setting. I'm verifying that I've captured the GSM1K results correctly—the permutation test gives p=0.014, and while the original hypothesis predicted a positive correlation, the observed effect is actually negative, which is worth noting honestly. The DIF-C items appear resistant to contamination-based improvements, so this finding is suggestive given the sample size of 33. I've also confirmed I've included all three tables and four figures as requested, and I'm doing a final check on style consistency—avoiding em-dashes in the text, watching for -ing phrase endings, and making sure I'm not overusing transition words like "Furthermore" or "Moreover." I need to verify I'm following the guidance correctly for §4.7 Layer 2 — the instruction is clear that I shouldn't claim both "signal carriers" and "conservative filter" simultaneously, and I've written it properly by distinguishing that DIF items carry more discriminative signal than average items while also isolating differential behavior specifically. For §4.2, I'm checking the FDR correction numbers: 31.32% uncorrected becomes 31.30% corrected (removing only 3 items), and I've represented this accurately at the appropriate precision level.

Looking at the overall structure, my draft sections are roughly balanced in length, with the longer sections (§4.2, §4.7, §4.8) containing tables or figures to support the text. The opening of §4 establishes the high-level setup as needed, and I'm ready to finalize the section with these precision checks in place.

Now I need to expand strategically to reach the target word count. I'll deepen §4.2 with more discussion of the BH FDR correction mechanics and threshold sensitivity, expand §4.3 to connect the findings to the contamination detection literature, add more explanation to §4.5 about why cross-subject matching is effective, elaborate on the layer-by-layer analysis in §4.7, and strengthen §4.8 with more detail on the three-part analysis structure. This should bring the total closer to 2500 words while keeping the focus on the most substantive sections.

I should also verify the LaTeX conventions—cleveref's \Cref will work fine with the iclr2026 template, and natbib is available so both \citet and \citep are supported. For notation, I'll use \mathrm for abbreviations like TPR and ensure I'm consistent with $\Delta_{\mathrm{MH}}$ for the Δ_MH notation throughout.

Now I'm planning the expansions for each section. For §4.2, I need to add more context before the numbers, be explicit about the BH correction adjustment from 31.32% to 31.30%, and include the threshold. For §4.3, I should expand the interpretation and clarify the dose-response description. §4.5 needs explanation of why within-subject matching fails mechanistically and a clearer methodological recommendation. §4.7 requires the specific numbers for Layer 3 and a clearer presentation of the circularity ablation in Layer 2. And §4.8 should include the external matching ΔTPR for semi-synthetic data and expand the GSM1K interpretation.

I'm aiming for roughly 2500 words of actual text content, excluding LaTeX markup and table contents, so I need to be strategic about where to add detail without bloating the section unnecessarily. I'm mapping out the word distribution across the remaining subsections to hit around 2400 words total for the body text, with §4.2 and §4.7 carrying the most weight since they're the most important points. I need to weave in those specific metrics from the tables—like the 61.3% confound in the within-family Llama comparison and the semi-synthetic ΔTPR results—directly into the narrative rather than just referencing them. Let me draft the full section now with this structure in mind. I'm settling on using `\paragraph{}` for both the layers in §4.7 and the three parts in §4.8 to maintain consistent structure throughout. Now I'm writing out the full LaTeX document, starting with the experiments section that applies MH-DIF to METABENCH and outlines the validation, temporal analysis, structural investigation, semi-synthetic evaluation, and ranking consequences.

Writing LaTeX structure... I'm planning out the float placement strategy for this paper—with four figures and three tables spread across roughly 3-4 pages of experiments, I'll anchor most floats to the top of pages to maintain good flow. The distribution looks balanced: Table 1 early on, then alternating between figures and tables through the remaining sections, finishing with Figure 5 and Table 3 together.

Now I'm ready to write out the full experiments section, making sure to maintain consistent LaTeX formatting and avoid any stylistic issues. I'm running a power analysis using simulated item response data with controlled DIF injection across different sample sizes, finding that at N≥80 the method achieves strong detection rates (68-80% true positives, ~4% false positives, 0.93-0.94 AUC), and since our actual temporal cohorts are much larger (1,080 and 807 models), statistical power isn't a constraint for our results.

The key finding is that 31.3% of MMLU items show differential functioning between 2023 and 2024 model releases when applying the ETS~C threshold, and FDR correction barely changes this figure, suggesting the dual-threshold classification system is already conservative about false discoveries.

To rule out that this instability is just an artifact of how we're measuring, I'm checking three control conditions: splitting the 2023 models randomly yields almost no DIF items, comparing models by ability within the same year shows only 2.9% instability, but comparing Llama-2 to Llama-3 across versions produces 61.3% DIF items—which aligns with known sensitivity of the Mantel-Haenszel test to ability differences between groups.

The instability shows up consistently across knowledge domains too. Looking at each MMLU subject separately, I'm finding an average of 38.1% DIF items across all five domains, and there's a modest correlation between how much a domain improved and how unstable it is. But when I run item-level regression to isolate domain improvement's contribution, it only accounts for 2.4 percentage points of the total 31.3% instability, leaving 92.4% unexplained by domain-specific gains.

Now examining whether architectural differences are driving these results. The METABENCH dataset is almost entirely decoder-only models, so removing the single encoder-decoder variant doesn't change the findings at all. I'm also testing sensitivity across different DIF thresholds to confirm the pattern holds—whether I use stricter or looser cutoffs, the qualitative conclusion remains consistent.

Looking at the temporal DIF landscape across all cohort comparisons. Then checking if DIF is actually capturing contamination by comparing flagged items against known contaminated items from web-overlap analysis. The enrichment ratio comes out to 0.96, which is essentially random chance—so DIF flags aren't matching up with known contamination. But this doesn't mean DIF is broken. When I inject controlled contamination into the data at specific rates, I see a clear dose-response relationship where differential contamination produces measurable changes in true positive rates.

The real issue is that DIF and web-overlap labels are measuring different things entirely. Web-overlap tells me whether an item exists somewhere in public training data globally, while DIF tells me whether an item behaves differently across temporal cohorts. An item can be everywhere in training data but still function identically across model generations if they all saw the same data. Or an item can show strong DIF without any obvious contamination source if the training process itself changed. So the web-overlap labels aren't the right benchmark for evaluating a differential detection method.

Now moving into structural analysis to see if I can reduce DIF through different approaches.

I'm testing three progressively refined methods to control for ability differences, but they all hit the same wall—a temporal false positive rate stuck around 31%. Matched-ability quintile analysis keeps comparisons within similar score ranges and shows enrichment ratios near 1.0 with FPR unchanged. IRT ability conditioning with 20 strata achieves near-perfect correlation with total score but still yields FPR = 0.312, suggesting the total score already captures the ability variance that matters for DIF. Within-subject analysis looking for subject-specific effects finds a bifactor index of 38.1%, well above the 25% threshold needed for viable structure. This pattern across all three approaches points to something structural in the data itself rather than a methodological fix.

The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Now I'm moving to a semi-synthetic validation framework where I can inject known DIF by flipping responses for a contaminated subset of items at varying exploitation rates. The key finding is that the matching strategy—specifically whether I compute the matching variable from other subjects or the same subject—determines whether the framework produces valid results. Cross-subject matching yields zero false positive rate change across all five MMLU subjects and achieves strong true positive rates above 0.3 at moderate contamination levels.

Within-subject matching, on the other hand, inflates the false positive rate by about 0.186 on average because the matching variable itself gets contaminated by the injected signal, which violates the conditional independence assumption underlying the Mantel-Haenszel procedure. I'm adopting cross-subject matching as the standard going forward and recommending it as the default for any semi-synthetic DIF evaluation on multi-subject benchmarks.

Now I'm examining local independence using Yen's Q3 statistic to measure residual correlations between item pairs after conditioning on the latent trait. Within-subject item pairs show substantially higher violation rates—11.3% exceed the threshold compared to just 2.2% for cross-subject pairs.

Looking at the downstream impact, I need to assess whether this 31% item instability actually matters for model evaluation and benchmark rankings. I'm conducting a four-layer analysis that moves from overall statistics down to model-specific diagnostics, starting with benchmark redundancy by comparing model rankings computed across all items versus only the stable ones.

The correlation is extremely high at 0.997, meaning that at the aggregate level, removing nearly a third of items barely shifts the ranking order. This makes sense given the massive item pool of over 12,000 items—there's enough statistical power that losing some items doesn't fundamentally change the conclusions.

However, the DIF-flagged items aren't just random noise. They actually contain more discriminative signal than average items, so removing them does degrade ranking discriminability more than removing an equivalent number of random items. But here's the key finding: when I compare different removal strategies, DIF-based removal is actually the least disruptive approach. Removing items based on accuracy gaps or high variance causes much more severe degradation in discriminability than removing DIF items does.

The overlap between DIF-flagged items and genuinely high-discrimination items is quite low, which tells me that DIF is capturing something specific—differential behavior across different model cohorts—rather than just identifying generally informative items.

Looking at individual model families reveals striking patterns. Phi-3 and Llama-3 models show massive rank improvements when evaluated only on stable items, gaining 700 to 850 positions, which suggests they were getting inflated performance scores from items that shifted in difficulty between 2023 and 2024. Mistral-based merges show the opposite effect, losing hundreds of positions on stable items. There's a caveat here though when looking at the top 50 ranked models specifically.

Now I'm checking whether this DIF instability pattern holds across other benchmarks beyond MMLU. I'm replicating the full analysis on GSM8K using independent contamination validation with a held-out test set, and I can see the relationship between how models rank on the full benchmark versus the DIF-filtered version. The next step is to run the complete pipeline on GSM8K to test whether temporal DIF is a broader phenomenon in LLM evaluation or specific to MMLU.

On GSM8K, the temporal DIF instability rate is lower at 18.9% compared to MMLU's 31.3%, which makes sense given that GSM8K focuses on a single domain of mathematical reasoning rather than MMLU's 57 diverse subjects. The semi-synthetic validation confirms I can detect this effect reliably, with strong detection power when I artificially introduce contamination at different rates, and interestingly, when I use MMLU scores to match models for GSM8K analysis, the detection power remains substantial though somewhat reduced.

Now I'm looking at how contamination correlates with DIF advantages—comparing each model's performance gap between the original GSM8K and a held-out set of novel problems against the ranking boost they get from items flagged as having differential item functioning. The correlation is moderately negative, suggesting models with higher contamination tend to gain less from DIF-flagged items, and this relationship holds even after controlling for other factors.

This contradicts my initial expectation that contaminated models would benefit more from DIF items, but it actually supports the idea that these items capture genuine behavioral differences rather than just memorization effects. The sample size is modest, so this finding needs validation with more models, though it does align with the broader picture that DIF represents something distinct from simple training data recall.

Now I'm doing a word count across the sections to make sure I'm hitting the target budget. The body text is coming in around 2100 words, which is a bit under the 2500-word limit, so I should expand some of the longer sections by another 200 words or so. I can add more detail to the practical implications in section 4.2, and maybe flesh out a couple of the other areas that could use more explanation.

Actually, let me step back—if the word budget includes captions and tables, I'm already at about 2510 total, which is right where I need to be. Adding more might push me over the page limit, so I should probably leave it as is. The body text at 2100 words is solid for a section with multiple figures and tables.

Let me do a final check for style consistency: no em-dashes, no -ing phrase endings. Everything looks good there. I'm checking paragraph lengths across the results sections—most are hitting the 5-8 sentence target, though a few are running short at 3-4 sentences. I should expand §4.3 and §4.5 by merging their opening paragraphs with what follows, while §4.2's first paragraph could use a bit more detail. The rest look solid. I'm consolidating the shorter sections—merging §4.3's opening paragraphs and combining §4.5 into a single block to match the style guide's preference for 5-8 sentence paragraphs. Now I need to verify all the bibliography keys are correct and present in the bib file, checking through the citations I've used and noting that habba2026growingpains hasn't been incorporated yet, though I should add it if there's a natural fit in the experiments section. I'm deciding between \citep for parenthetical citations and \citet when authors are the subject of the sentence. I'll also add non-breaking spaces before citations to keep them with the preceding text, and maintain consistent formatting like "ETS~C" throughout. For the architecture heterogeneity and threshold sensitivity sections, brief dismissals of a few sentences work fine. Now I'm ready to write out the final version carefully.

I need to verify the random split reference in §4.2 is clearly about the 2023 cohort, and I should add a note to the Table 1 caption explaining what "clean" means in "FPR (Li clean)" so readers understand it's the false positive rate against Li et al.'s clean labels. odd with the en-dash, so let me just write it more clearly as "Q1–Q2 vs. Q4–Q5" to avoid confusion. That's cleaner and more readable.

Now I'm ready to write out the complete experiments section. Let me also double-check the Layer 2 findings one more time—the key point is that DIF items show strong signal across conditions, but the circularity ablation reveals DIF is actually the least disruptive strategy compared to other non-random approaches, with specific z-scores for each metric. I'm seeing the key distinction now: DIF removal hurts performance more than random removal across all 21 conditions (z=-8 to -49), which means DIF items do carry signal. But when comparing non-random strategies directly, DIF is the least disruptive to remove (z=-9.5) compared to accuracy-gap (z=-156.5), high-variance (z=-107.9), and high-discrimination (z=-15.8). So DIF items are informative, but they're picking a different kind of informativeness than the other strategies—not just generally useful items, but specifically those that capture differential behavior. I'm settling on the notation—z-scores are already expressed in standard deviations, so I'll write the range as $z = -8$ to $z = -49$ across the conditions, keeping the single values like $z = -156.5$ for the individual ablation strategies. Time to finalize the text.

Let me verify I'm not violating the rule about starting sections with "In this section"—my opening "We apply MH-DIF to the METABENCH dataset..." is fine. I should also check whether the math packages are already loaded in the preamble since I'm using symbols like $\sim$ and $\times$, but math_commands.tex is likely handling that.

For the approximate symbol in the table, I'll use ${\sim}2{,}600$ to format it properly. I'm confident the natbib package is loaded through the conference style file, so \citep and \citet commands should work without issues. Ready to finalize the output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "ad6d1d7e-059d-4758-b02f-419f10f6f756",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cye4Zte3ZSECH6pPnssuR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 41437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2077
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

_source line 79_

Now I have all the context I need. Let me write the experiments section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "a8f59f94-f8b1-43c2-aab5-9a2d3a128614",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cye4Zte3ZSECH6pPnssuR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 41437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2077
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

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_013D2Gm6VxPbw9dyxcrwLRLk`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/",
  "description": "Check if sections dir exists and is empty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "09028a1b-2327-438a-a42b-d057d8aba8aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cye4Zte3ZSECH6pPnssuR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2077,
      "cache_read_input_tokens": 41437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2077
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

_source line 81 · 2026-05-21T04:08:27.948Z_

<details><summary>↩ Tool result · `toolu_013D2Gm6VxPbw9dyxcrwLRLk`</summary>

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
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "98a8f6cd-f795-4307-946c-8a14db108ade",
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

_source line 82_

<details open><summary>🔧 Tool call — Write · `toolu_017WSamq4jRbAseBNi6ET65z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH dataset~\\citep{kipnis2024metabench}, which provides sparse response matrices for 5,227 models evaluated on 12,508 MMLU items~\\citep{hendrycks2021mmlu}. All temporal analyses define reference and focal cohorts by model release date (2023 vs.\\ 2024). We validate detection power through simulation, characterize temporal instability across multiple cohort designs, evaluate the relationship between DIF flags and existing contamination labels, and assess downstream consequences for benchmark rankings. Replication on GSM8K with cross-benchmark contamination validation appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\nTo confirm that MH-DIF detects differential item functioning at the sample sizes available in METABENCH, we conduct a power analysis using empirical MMLU IRT parameters. We simulate item response matrices where a controlled subset of items has injected DIF of varying magnitude ($|\\Delta_{\\mathrm{MH}}| \\geq 1.4$) and evaluate ETS~C classification across sample sizes $N \\in \\{40, 80, 160, 320\\}$ per cohort. At $N \\geq 80$, ETS~C achieves true positive rates of 0.68--0.80 with false positive rates of 0.036--0.042 and AUC of 0.93--0.94. The temporal cohort sizes in our analysis ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold, and statistical power is not a limiting factor for the results reported below. Full simulation results with confidence intervals appear in Appendix~Table~A1.\n\n\\subsection{Temporal Comparability: 31\\% Item Instability}\n\\label{sec:temporal}\n\nThe central finding of this paper is that a substantial fraction of MMLU items behave differently across model generations. Comparing models released in 2023 ($N = 1{,}080$) against models released in 2024 ($N = 807$), 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$). Applying Benjamini-Hochberg FDR correction at $q = 0.05$ reduces this from 31.32\\% to 31.30\\%, removing only 3 items. The minimal impact of FDR correction reflects the fact that the ETS classification system imposes a dual threshold on both effect size and statistical significance, which already provides implicit multiple-testing protection. In absolute terms, nearly one in three MMLU items exhibits a large shift in its statistical relationship to overall model ability between the two cohort periods.\n\nThree control conditions establish that this instability reflects genuine temporal change rather than methodological artifacts. A random split of the 2023 cohort into two equal halves produces only 0.18\\% ETS~C items, confirming that sampling noise alone does not generate large-scale DIF. An ability-quintile comparison (lowest-scoring vs.\\ highest-scoring models within the same temporal cohort) yields 2.9\\% ETS~C items, indicating that ability differences alone are insufficient to produce the observed instability. A within-family comparison of Llama-2 ($N = 161$) and Llama-3 ($N = 308$) models produces 61.3\\% ETS~C items. This elevated rate is consistent with the known sensitivity of MH-DIF to ability differences between groups~\\citep{holland1988mh}: models from different generations within a single family exhibit large ability gaps that confound the DIF signal. The contrast between 2.9\\% (ability-controlled) and 61.3\\% (ability-confounded) brackets the temporal rate of 31.3\\% and confirms that it captures a mixture of genuine item instability and residual ability differences.\n\nThe instability penetrates within every knowledge domain. Within-subject analysis yields an average of 38.1\\% ETS~C items across all five MMLU subjects (range: 31--45\\%), and the ecological correlation between subject-level accuracy improvement and subject-level C\\% is $\\rho = 0.307$ ($p = 0.02$). This ecological correlation could suggest that domains where models improved most also exhibit the most instability. Item-level logistic regression, however, reveals that domain accuracy improvement explains only 2.4 percentage points of the 31.3\\% temporal C\\% (pseudo $R^2 = 0.0007$; counterfactual C\\% with domain improvement regressed out $= 29.0\\%$). Of the observed instability, 92.4\\% is unrelated to aggregate domain-level accuracy gains and instead reflects item-specific changes in how models interact with individual questions.\n\nArchitecture heterogeneity is a non-issue for this analysis. The METABENCH MMLU population is 99.98\\% decoder-only (5,226 of 5,227 models). Excluding the single encoder-decoder model yields C\\% $= 31.32\\%$ with Jaccard similarity of 1.0 between flagged item sets. Threshold sensitivity analysis confirms robustness across the full ETS range: C\\% $= 48.9\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 1.0$, $31.3\\%$ at $\\geq 1.5$ (the standard ETS~C threshold), $18.3\\%$ at $\\geq 2.0$, and $10.2\\%$ at $\\geq 2.5$. The qualitative conclusion holds at every threshold. \\Cref{tab:temporal_landscape} summarizes the DIF landscape across all cohort comparisons.\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. FPR is measured against Li et al.\\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}\n\\label{tab:temporal_landscape}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & ETS~C (\\%) & FPR (Li clean) & Enrichment \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.96 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,600 / ${\\sim}$2,600 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split (sanity) & 540 / 540 & 0.18 & -- & -- \\\\\nWithin-subject (avg, 5 subjects) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ground Truth Mismatch}\n\\label{sec:groundtruth}\n\nIf DIF captures differential contamination, flagged items should overlap with independently identified contaminated items. We evaluate this hypothesis against the web-overlap labels of \\citet{li2024contamination}, which classify MMLU items as ``contaminated'' based on verbatim matches in web training corpora. The enrichment ratio of DIF flags against these labels is 0.96 (\\Cref{tab:temporal_landscape}), indistinguishable from chance. This null result does not indicate that DIF fails to detect contamination. Semi-synthetic injection experiments demonstrate a clear dose-response relationship: injecting controlled differential contamination at exploitation rate $p = 0.5$ produces $\\Delta\\mathrm{TPR} = {+}0.508$, and at $p = 1.0$, $\\Delta\\mathrm{TPR} = {+}0.674$ (\\Cref{fig:dose_response}). The disconnect between DIF flags and web-overlap labels arises because the two methods answer fundamentally different questions.\n\nWeb-overlap labels measure \\emph{global exposure}: whether an item exists in publicly accessible training data. DIF measures \\emph{differential functioning}: whether an item's statistical relationship to overall ability changes across temporal cohorts. An item can be globally contaminated yet function identically across cohorts if all model generations have comparable access to the same training data. Conversely, an item can exhibit large DIF without any identifiable contamination source if changes in training methodology alter how models process certain question types. The Li et al.\\ labels are therefore the wrong ground truth for evaluating a differential detection method: the near-chance enrichment is expected, not evidence of failure.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\nThree progressively refined approaches fail to reduce the temporal false positive rate below 31\\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\\theta$-conditioning with 20 ability strata achieves $r(\\theta, \\mathrm{total\\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis, intended to isolate subject-specific effects, finds C\\% $= 38.1\\%$ across subjects, exceeding the 25\\% threshold that would indicate viable bifactor structure. \\Cref{tab:structural_comparison} summarizes these results. The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned.\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\\%, indicating that the observed instability is not an artifact of ability matching.}\n\\label{tab:structural_comparison}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temporal FPR & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (external) & Cross-benchmark total score & 0.314 & 0.834 & Reference \\\\\nMatched-ability & Within-quintile temporal DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-conditioning & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Semi-Synthetic Framework Validation}\n\\label{sec:semisynthetic}\n\nThe semi-synthetic injection framework enables controlled evaluation of DIF detection by flipping incorrect responses to correct for a designated ``contaminated'' subset of items in the focal cohort at a specified exploitation rate $p$. The critical methodological finding is that the choice of matching strategy determines whether the framework produces valid results. Cross-subject matching computes the matching variable from subjects \\emph{other than} the one being tested, ensuring that the conditioning variable is unaffected by the injected contamination. Under this protocol, $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects, and four of five subjects produce $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$ (\\Cref{fig:within_subject}). Within-subject matching, by contrast, computes the matching variable from the same subject where contamination was injected, which inflates FPR by an average of ${+}0.186$ because the matching variable absorbs part of the injection signal and violates the conditional independence assumption of the MH procedure. We adopt cross-subject matching as the standard protocol for all subsequent analyses and recommend it as default for semi-synthetic DIF evaluation on multi-subject benchmarks.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_3_within_subject_matching.pdf}\n\\caption{Cross-subject vs.\\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\\Delta\\mathrm{FPR} = 0.000$) while preserving detection power ($\\Delta\\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}\n\\label{fig:within_subject}\n\\end{figure}\n\n\\subsection{Local Independence}\n\\label{sec:q3}\n\nYen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. Within-subject item pairs show 11.3\\% of correlations exceeding $|Q3| > 0.20$, compared to 2.2\\% for cross-subject pairs (a $5{\\times}$ ratio, $p = 2.3 \\times 10^{-9}$). This mild local dependence within subjects is a contributing factor to elevated within-subject DIF rates but is not the primary driver of temporal instability: the cross-subject matching protocol already addresses this source of bias, and the temporal C\\% of 31.3\\% persists under external matching. Full Q3 distributions appear in Appendix~Figure~A2.\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\nThe practical relevance of 31\\% item instability depends on whether unstable items affect model evaluation and benchmark rankings. We investigate this through a four-layer analysis that progresses from aggregate statistics to model-specific diagnostics.\n\n\\paragraph{Layer 1: Benchmark redundancy.} Spearman correlation between model rankings computed on all 12,508 items versus stable-only items (ETS~A/B) is $\\rho \\approx 0.997$. At the level of aggregate rankings, removing 31\\% of items changes almost nothing. This redundancy is a consequence of the large item pool: 12,508 items provide sufficient statistical mass that removing nearly a third does not alter rank order.\n\n\\paragraph{Layer 2: Signal concentration with circularity check.} Despite aggregate redundancy, DIF-flagged items carry more discriminative signal than the average item. Removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49$ across 21 experimental conditions). A circularity ablation, however, places this in context: DIF-based removal is the \\emph{least} disruptive among non-random removal strategies. Accuracy-gap removal produces $z = -156.5$, high-variance removal $z = -107.9$, and high-discrimination removal $z = -15.8$, compared to $z = -9.5$ for DIF removal. The Jaccard overlap between DIF-flagged and high-discrimination items is only 0.12. DIF items carry more signal than average, but DIF isolates differential behavior across cohorts specifically, not generally informative items.\n\n\\paragraph{Layer 3: Diagnostic lens.} Individual model families show distinctive DIF profiles that reveal which families disproportionately benefit from unstable items. Phi-3 and Llama-3 models gain ${+}700$ to ${+}850$ rank positions when evaluated on stable items only, suggesting inflated performance on items whose function changed between 2023 and 2024. Mistral-based model merges show the opposite pattern, losing $-400$ to $-587$ positions. A caveat applies: among the top 50 rank movers, 49 of 50 carry ``unknown'' family labels in METABENCH, limiting the scope of family-level interpretation.\n\n\\paragraph{Layer 4: Cross-benchmark signal.} The DIF instability pattern extends beyond MMLU. \\Cref{sec:gsm8k} presents a full replication on GSM8K with independent contamination validation using the GSM1K held-out set~\\citep{zhang2024gsm1k}. \\Cref{fig:downstream} visualizes the relationship between full and DIF-filtered rankings.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_4_downstream_impact.pdf}\n\\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\\rho \\approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only, with Phi-3 and Llama-3 gaining and Mistral merges losing rank positions.}\n\\label{fig:downstream}\n\\end{figure}\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:gsm8k}\n\nTo test whether temporal DIF is specific to MMLU or reflects a broader phenomenon in LLM benchmarking, we replicate the full analysis pipeline on GSM8K (1,319 items $\\times$ 6,702 models from METABENCH).\n\n\\paragraph{Temporal DIF.} Standard matching yields C\\% $= 18.9\\%$ for the temporal cohort comparison, with a random-split sanity check at 0.3\\%. The lower instability rate compared to MMLU (31.3\\%) is consistent with GSM8K's more homogeneous item structure: single-domain mathematical reasoning versus MMLU's 57 diverse subjects. The sanity check confirms that the signal is non-random.\n\n\\paragraph{Semi-synthetic validation.} Dose-response confirms detection power on this benchmark. Standard matching achieves $\\Delta\\mathrm{TPR} = {+}0.818$ at exploitation rate $p = 0.7$. External matching (using MMLU total score to match models for GSM8K DIF analysis) yields $\\Delta\\mathrm{TPR} = {+}0.517$ at $p = 0.7$, with $\\Delta\\mathrm{FPR}$ well-controlled. \\Cref{tab:gsm8k_comparison} compares key metrics across both benchmarks.\n\n\\paragraph{GSM1K contamination gap.} The GSM1K dataset~\\citep{zhang2024gsm1k} provides an independent measure of per-model contamination by comparing performance on the original GSM8K versus a held-out set of novel problems. For $N = 33$ models with both GSM1K scores and METABENCH evaluations, we correlate each model's contamination gap (GSM8K accuracy minus GSM1K accuracy) with the ranking advantage gained from DIF-flagged items. The observed correlation is $r = -0.478$ (95\\% CI $= [-0.71, -0.16]$, $p = 0.005$), with partial $r = -0.385$ after controlling for overall accuracy and permutation $p = 0.014$. Our original hypothesis predicted a \\emph{positive} correlation: models benefiting more from contamination should also benefit more from DIF items. The observed \\emph{negative} correlation indicates the opposite. DIF-C items resist contamination-based performance gains, and models with larger contamination gaps benefit \\emph{less} from these items. This result is suggestive at $N = 33$ and warrants replication with larger model populations, but it aligns with the broader interpretation that DIF captures item-level behavioral change distinct from simple memorization of training data. \\Cref{fig:gsm1k} shows the correlation scatter.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}\n\\caption{GSM1K contamination gap vs.\\ DIF ranking advantage for $N = 33$ models. The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items, contrary to the initial positive-correlation hypothesis.}\n\\label{fig:gsm1k}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power.}\n\\label{tab:gsm8k_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & MMLU & GSM8K \\\\\n\\midrule\nItems & 12,508 & 1,319 \\\\\nModels & 5,227 & 6,702 \\\\\nTemporal C\\% & 31.3\\% & 18.9\\% \\\\\nSanity C\\% & 0.18\\% & 0.3\\% \\\\\n$\\Delta$TPR ($p{=}0.7$, standard) & -- & ${+}0.818$ \\\\\n$\\Delta$TPR ($p{=}0.5$, external) & ${+}0.508$ & ${+}0.514$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "09fab690-4f6e-40b2-bbc8-abe2ff87683e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoNMZ5PHLEoHdB7xjzcUjt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17849,
      "cache_read_input_tokens": 43514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17849
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

_source line 83 · 2026-05-21T04:10:34.736Z_

<details><summary>↩ Tool result · `toolu_017WSamq4jRbAseBNi6ET65z`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "bcccb938-f14a-41a1-90f0-cd4562ae4703",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe apply MH-DIF to the METABENCH dataset~\\citep{kipnis2024metabench}, which provides sparse response matrices for 5,227 models evaluated on 12,508 MMLU items~\\citep{hendrycks2021mmlu}. All temporal analyses define reference and focal cohorts by model release date (2023 vs.\\ 2024). We validate detection power through simulation, characterize temporal instability across multiple cohort designs, evaluate the relationship between DIF flags and existing contamination labels, and assess downstream consequences for benchmark rankings. Replication on GSM8K with cross-benchmark contamination validation appears in \\Cref{sec:gsm8k}.\n\n\\subsection{Validation: DIF Detection Power}\n\\label{sec:validation}\n\nTo confirm that MH-DIF detects differential item functioning at the sample sizes available in METABENCH, we conduct a power analysis using empirical MMLU IRT parameters. We simulate item response matrices where a controlled subset of items has injected DIF of varying magnitude ($|\\Delta_{\\mathrm{MH}}| \\geq 1.4$) and evaluate ETS~C classification across sample sizes $N \\in \\{40, 80, 160, 320\\}$ per cohort. At $N \\geq 80$, ETS~C achieves true positive rates of 0.68--0.80 with false positive rates of 0.036--0.042 and AUC of 0.93--0.94. The temporal cohort sizes in our analysis ($N_{\\mathrm{ref}} = 1{,}080$, $N_{\\mathrm{focal}} = 807$) far exceed this threshold, and statistical power is not a limiting factor for the results reported below. Full simulation results with confidence intervals appear in Appendix~Table~A1.\n\n\\subsection{Temporal Comparability: 31\\% Item Instability}\n\\label{sec:temporal}\n\nThe central finding of this paper is that a substantial fraction of MMLU items behave differently across model generations. Comparing models released in 2023 ($N = 1{,}080$) against models released in 2024 ($N = 807$), 31.3\\% of items receive ETS~C classification ($|\\Delta_{\\mathrm{MH}}| \\geq 1.5$). Applying Benjamini-Hochberg FDR correction at $q = 0.05$ reduces this from 31.32\\% to 31.30\\%, removing only 3 items. The minimal impact of FDR correction reflects the fact that the ETS classification system imposes a dual threshold on both effect size and statistical significance, which already provides implicit multiple-testing protection. In absolute terms, nearly one in three MMLU items exhibits a large shift in its statistical relationship to overall model ability between the two cohort periods.\n\nThree control conditions establish that this instability reflects genuine temporal change rather than methodological artifacts. A random split of the 2023 cohort into two equal halves produces only 0.18\\% ETS~C items, confirming that sampling noise alone does not generate large-scale DIF. An ability-quintile comparison (lowest-scoring vs.\\ highest-scoring models within the same temporal cohort) yields 2.9\\% ETS~C items, indicating that ability differences alone are insufficient to produce the observed instability. A within-family comparison of Llama-2 ($N = 161$) and Llama-3 ($N = 308$) models produces 61.3\\% ETS~C items. This elevated rate is consistent with the known sensitivity of MH-DIF to ability differences between groups~\\citep{holland1988mh}: models from different generations within a single family exhibit large ability gaps that confound the DIF signal. The contrast between 2.9\\% (ability-controlled) and 61.3\\% (ability-confounded) brackets the temporal rate of 31.3\\% and confirms that it captures a mixture of genuine item instability and residual ability differences.\n\nThe instability penetrates within every knowledge domain. Within-subject analysis yields an average of 38.1\\% ETS~C items across all five MMLU subjects (range: 31--45\\%), and the ecological correlation between subject-level accuracy improvement and subject-level C\\% is $\\rho = 0.307$ ($p = 0.02$). This ecological correlation could suggest that domains where models improved most also exhibit the most instability. Item-level logistic regression, however, reveals that domain accuracy improvement explains only 2.4 percentage points of the 31.3\\% temporal C\\% (pseudo $R^2 = 0.0007$; counterfactual C\\% with domain improvement regressed out $= 29.0\\%$). Of the observed instability, 92.4\\% is unrelated to aggregate domain-level accuracy gains and instead reflects item-specific changes in how models interact with individual questions.\n\nArchitecture heterogeneity is a non-issue for this analysis. The METABENCH MMLU population is 99.98\\% decoder-only (5,226 of 5,227 models). Excluding the single encoder-decoder model yields C\\% $= 31.32\\%$ with Jaccard similarity of 1.0 between flagged item sets. Threshold sensitivity analysis confirms robustness across the full ETS range: C\\% $= 48.9\\%$ at $|\\Delta_{\\mathrm{MH}}| \\geq 1.0$, $31.3\\%$ at $\\geq 1.5$ (the standard ETS~C threshold), $18.3\\%$ at $\\geq 2.0$, and $10.2\\%$ at $\\geq 2.5$. The qualitative conclusion holds at every threshold. \\Cref{tab:temporal_landscape} summarizes the DIF landscape across all cohort comparisons.\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\\Delta_{\\mathrm{MH}}| \\geq 1.5$. FPR is measured against Li et al.\\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}\n\\label{tab:temporal_landscape}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCohort Definition & $N_{\\mathrm{ref}}$ / $N_{\\mathrm{focal}}$ & ETS~C (\\%) & FPR (Li clean) & Enrichment \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.96 \\\\\nAbility quintile (Q1--2 vs.\\ Q4--5) & ${\\sim}$2,600 / ${\\sim}$2,600 & 2.9 & 0.027 & 1.19 \\\\\nWithin-family (Llama-2 vs.\\ 3) & 161 / 308 & 61.3 & -- & -- \\\\\nRandom split (sanity) & 540 / 540 & 0.18 & -- & -- \\\\\nWithin-subject (avg, 5 subjects) & \\textit{varies} & 38.1 & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ground Truth Mismatch}\n\\label{sec:groundtruth}\n\nIf DIF captures differential contamination, flagged items should overlap with independently identified contaminated items. We evaluate this hypothesis against the web-overlap labels of \\citet{li2024contamination}, which classify MMLU items as ``contaminated'' based on verbatim matches in web training corpora. The enrichment ratio of DIF flags against these labels is 0.96 (\\Cref{tab:temporal_landscape}), indistinguishable from chance. This null result does not indicate that DIF fails to detect contamination. Semi-synthetic injection experiments demonstrate a clear dose-response relationship: injecting controlled differential contamination at exploitation rate $p = 0.5$ produces $\\Delta\\mathrm{TPR} = {+}0.508$, and at $p = 1.0$, $\\Delta\\mathrm{TPR} = {+}0.674$ (\\Cref{fig:dose_response}). The disconnect between DIF flags and web-overlap labels arises because the two methods answer fundamentally different questions.\n\nWeb-overlap labels measure \\emph{global exposure}: whether an item exists in publicly accessible training data. DIF measures \\emph{differential functioning}: whether an item's statistical relationship to overall ability changes across temporal cohorts. An item can be globally contaminated yet function identically across cohorts if all model generations have comparable access to the same training data. Conversely, an item can exhibit large DIF without any identifiable contamination source if changes in training methodology alter how models process certain question types. The Li et al.\\ labels are therefore the wrong ground truth for evaluating a differential detection method: the near-chance enrichment is expected, not evidence of failure.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_2_dose_response.pdf}\n\\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\\Delta\\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\\Delta\\mathrm{TPR} \\approx 0$.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Structural Analysis}\n\\label{sec:structural}\n\nThree progressively refined approaches fail to reduce the temporal false positive rate below 31\\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\\theta$-conditioning with 20 ability strata achieves $r(\\theta, \\mathrm{total\\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis, intended to isolate subject-specific effects, finds C\\% $= 38.1\\%$ across subjects, exceeding the 25\\% threshold that would indicate viable bifactor structure. \\Cref{tab:structural_comparison} summarizes these results. The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned.\n\n\\begin{table}[t]\n\\centering\n\\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\\%, indicating that the observed instability is not an artifact of ability matching.}\n\\label{tab:structural_comparison}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nApproach & Mechanism & Temporal FPR & TPR ($p{=}0.5$) & Outcome \\\\\n\\midrule\nBaseline (external) & Cross-benchmark total score & 0.314 & 0.834 & Reference \\\\\nMatched-ability & Within-quintile temporal DIF & ${\\sim}$0.31 & -- & Enrich.\\ 0.94--1.04 \\\\\n$\\theta$-conditioning & $\\theta$ replaces total score & 0.312 & 0.876 & $r(\\theta,\\mathrm{total}) {=} 0.9986$ \\\\\nWithin-subject & Per-subject DIF & -- & -- & C\\% $= 38.1\\%$ ($>$25\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Semi-Synthetic Framework Validation}\n\\label{sec:semisynthetic}\n\nThe semi-synthetic injection framework enables controlled evaluation of DIF detection by flipping incorrect responses to correct for a designated ``contaminated'' subset of items in the focal cohort at a specified exploitation rate $p$. The critical methodological finding is that the choice of matching strategy determines whether the framework produces valid results. Cross-subject matching computes the matching variable from subjects \\emph{other than} the one being tested, ensuring that the conditioning variable is unaffected by the injected contamination. Under this protocol, $\\Delta\\mathrm{FPR} = 0.000$ across all five MMLU subjects, and four of five subjects produce $\\Delta\\mathrm{TPR} > 0.3$ at $p = 0.5$ (\\Cref{fig:within_subject}). Within-subject matching, by contrast, computes the matching variable from the same subject where contamination was injected, which inflates FPR by an average of ${+}0.186$ because the matching variable absorbs part of the injection signal and violates the conditional independence assumption of the MH procedure. We adopt cross-subject matching as the standard protocol for all subsequent analyses and recommend it as default for semi-synthetic DIF evaluation on multi-subject benchmarks.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_3_within_subject_matching.pdf}\n\\caption{Cross-subject vs.\\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\\Delta\\mathrm{FPR} = 0.000$) while preserving detection power ($\\Delta\\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}\n\\label{fig:within_subject}\n\\end{figure}\n\n\\subsection{Local Independence}\n\\label{sec:q3}\n\nYen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. Within-subject item pairs show 11.3\\% of correlations exceeding $|Q3| > 0.20$, compared to 2.2\\% for cross-subject pairs (a $5{\\times}$ ratio, $p = 2.3 \\times 10^{-9}$). This mild local dependence within subjects is a contributing factor to elevated within-subject DIF rates but is not the primary driver of temporal instability: the cross-subject matching protocol already addresses this source of bias, and the temporal C\\% of 31.3\\% persists under external matching. Full Q3 distributions appear in Appendix~Figure~A2.\n\n\\subsection{Downstream Impact}\n\\label{sec:downstream}\n\nThe practical relevance of 31\\% item instability depends on whether unstable items affect model evaluation and benchmark rankings. We investigate this through a four-layer analysis that progresses from aggregate statistics to model-specific diagnostics.\n\n\\paragraph{Layer 1: Benchmark redundancy.} Spearman correlation between model rankings computed on all 12,508 items versus stable-only items (ETS~A/B) is $\\rho \\approx 0.997$. At the level of aggregate rankings, removing 31\\% of items changes almost nothing. This redundancy is a consequence of the large item pool: 12,508 items provide sufficient statistical mass that removing nearly a third does not alter rank order.\n\n\\paragraph{Layer 2: Signal concentration with circularity check.} Despite aggregate redundancy, DIF-flagged items carry more discriminative signal than the average item. Removing DIF items degrades ranking discriminability more than removing an equal number of random items ($z = -8$ to $-49$ across 21 experimental conditions). A circularity ablation, however, places this in context: DIF-based removal is the \\emph{least} disruptive among non-random removal strategies. Accuracy-gap removal produces $z = -156.5$, high-variance removal $z = -107.9$, and high-discrimination removal $z = -15.8$, compared to $z = -9.5$ for DIF removal. The Jaccard overlap between DIF-flagged and high-discrimination items is only 0.12. DIF items carry more signal than average, but DIF isolates differential behavior across cohorts specifically, not generally informative items.\n\n\\paragraph{Layer 3: Diagnostic lens.} Individual model families show distinctive DIF profiles that reveal which families disproportionately benefit from unstable items. Phi-3 and Llama-3 models gain ${+}700$ to ${+}850$ rank positions when evaluated on stable items only, suggesting inflated performance on items whose function changed between 2023 and 2024. Mistral-based model merges show the opposite pattern, losing $-400$ to $-587$ positions. A caveat applies: among the top 50 rank movers, 49 of 50 carry ``unknown'' family labels in METABENCH, limiting the scope of family-level interpretation.\n\n\\paragraph{Layer 4: Cross-benchmark signal.} The DIF instability pattern extends beyond MMLU. \\Cref{sec:gsm8k} presents a full replication on GSM8K with independent contamination validation using the GSM1K held-out set~\\citep{zhang2024gsm1k}. \\Cref{fig:downstream} visualizes the relationship between full and DIF-filtered rankings.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_4_downstream_impact.pdf}\n\\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\\rho \\approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only, with Phi-3 and Llama-3 gaining and Mistral merges losing rank positions.}\n\\label{fig:downstream}\n\\end{figure}\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:gsm8k}\n\nTo test whether temporal DIF is specific to MMLU or reflects a broader phenomenon in LLM benchmarking, we replicate the full analysis pipeline on GSM8K (1,319 items $\\times$ 6,702 models from METABENCH).\n\n\\paragraph{Temporal DIF.} Standard matching yields C\\% $= 18.9\\%$ for the temporal cohort comparison, with a random-split sanity check at 0.3\\%. The lower instability rate compared to MMLU (31.3\\%) is consistent with GSM8K's more homogeneous item structure: single-domain mathematical reasoning versus MMLU's 57 diverse subjects. The sanity check confirms that the signal is non-random.\n\n\\paragraph{Semi-synthetic validation.} Dose-response confirms detection power on this benchmark. Standard matching achieves $\\Delta\\mathrm{TPR} = {+}0.818$ at exploitation rate $p = 0.7$. External matching (using MMLU total score to match models for GSM8K DIF analysis) yields $\\Delta\\mathrm{TPR} = {+}0.517$ at $p = 0.7$, with $\\Delta\\mathrm{FPR}$ well-controlled. \\Cref{tab:gsm8k_comparison} compares key metrics across both benchmarks.\n\n\\paragraph{GSM1K contamination gap.} The GSM1K dataset~\\citep{zhang2024gsm1k} provides an independent measure of per-model contamination by comparing performance on the original GSM8K versus a held-out set of novel problems. For $N = 33$ models with both GSM1K scores and METABENCH evaluations, we correlate each model's contamination gap (GSM8K accuracy minus GSM1K accuracy) with the ranking advantage gained from DIF-flagged items. The observed correlation is $r = -0.478$ (95\\% CI $= [-0.71, -0.16]$, $p = 0.005$), with partial $r = -0.385$ after controlling for overall accuracy and permutation $p = 0.014$. Our original hypothesis predicted a \\emph{positive} correlation: models benefiting more from contamination should also benefit more from DIF items. The observed \\emph{negative} correlation indicates the opposite. DIF-C items resist contamination-based performance gains, and models with larger contamination gaps benefit \\emph{less} from these items. This result is suggestive at $N = 33$ and warrants replication with larger model populations, but it aligns with the broader interpretation that DIF captures item-level behavioral change distinct from simple memorization of training data. \\Cref{fig:gsm1k} shows the correlation scatter.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}\n\\caption{GSM1K contamination gap vs.\\ DIF ranking advantage for $N = 33$ models. The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items, contrary to the initial positive-correlation hypothesis.}\n\\label{fig:gsm1k}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power.}\n\\label{tab:gsm8k_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMetric & MMLU & GSM8K \\\\\n\\midrule\nItems & 12,508 & 1,319 \\\\\nModels & 5,227 & 6,702 \\\\\nTemporal C\\% & 31.3\\% & 18.9\\% \\\\\nSanity C\\% & 0.18\\% & 0.3\\% \\\\\n$\\Delta$TPR ($p{=}0.7$, standard) & -- & ${+}0.818$ \\\\\n$\\Delta$TPR ($p{=}0.5$, external) & ${+}0.508$ & ${+}0.514$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 84_

Let me verify the file compiles cleanly and check for any style violations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "ee5f3259-121a-4717-a416-5866e5f2ca2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wo75zWqhNDCmtjgJ3Q6aCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5542,
      "cache_read_input_tokens": 61363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5542
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

_source line 85_

<details open><summary>🔧 Tool call — Bash · `toolu_01LS2jQJBV3hhViMjU3Vc7cx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper && grep -n \"—\" sections/experiments.tex && echo \"FOUND EM-DASH\" || echo \"NO EM-DASH: OK\"",
  "description": "Check for em-dashes in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "2453458b-7b9d-42ed-b861-86be1799a52d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wo75zWqhNDCmtjgJ3Q6aCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5542,
      "cache_read_input_tokens": 61363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5542
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

_source line 86 · 2026-05-21T04:10:40.215Z_

<details><summary>↩ Tool result · `toolu_01LS2jQJBV3hhViMjU3Vc7cx`</summary>

```text
NO EM-DASH: OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "b1c19a75-909a-4842-abb2-17c93af671ab",
  "tool_use_result": {
    "stdout": "NO EM-DASH: OK",
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

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_012BRDcqtvQW5BSfHcn1mLhi`</summary>

```json
{
  "command": "grep -n \" – \" sections/experiments.tex && echo \"FOUND EN-DASH\" || echo \"NO EXPLANATORY EN-DASH: OK\"",
  "description": "Check for explanatory en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "2e86a7b1-02a9-4335-87cc-7a1b2b6bf225",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wo75zWqhNDCmtjgJ3Q6aCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5542,
      "cache_read_input_tokens": 61363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5542
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

_source line 88 · 2026-05-21T04:10:41.634Z_

<details><summary>↩ Tool result · `toolu_012BRDcqtvQW5BSfHcn1mLhi`</summary>

```text
NO EXPLANATORY EN-DASH: OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "40f99c73-fbe5-48b4-a7d6-37ce449c83d4",
  "tool_use_result": {
    "stdout": "NO EXPLANATORY EN-DASH: OK",
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

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01YU24q7JfPzGprPz6fucrrG`</summary>

```json
{
  "command": "grep -nP \"ing[,.]\" sections/experiments.tex | grep -v \"matching\\|conditioning\\|scoring\\|testing\\|ranking\\|missing\\|training\\|existing\\|benchmarking\\|using\\|\\\\\\\\string\\|meaning\" | head -20; echo \"---\"; grep -niP \"(furthermore|moreover|additionally|notably|it is worth noting|delve|leverage|utilize|facilitate)\" sections/experiments.tex | head -10; echo \"---\"; grep -n \"\\\\\\\\hline\" sections/experiments.tex | head -5; echo \"---\"; grep -n \"\\\\\\\\begin{center}\" sections/experiments.tex | head -5; echo \"---\"; grep -n \"^%\" sections/experiments.tex | head -5",
  "description": "Check for AI-style markers and LaTeX rule violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "fb76e21d-9607-43ba-a2a5-da02b39c4f9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wo75zWqhNDCmtjgJ3Q6aCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5542,
      "cache_read_input_tokens": 61363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5542
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

_source line 90 · 2026-05-21T04:10:46.311Z_

<details><summary>↩ Tool result · `toolu_01YU24q7JfPzGprPz6fucrrG`</summary>

```text
---
---
---
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "f592a13c-e117-45ec-b112-55f7062b2a4f",
  "tool_use_result": {
    "stdout": "---\n---\n---\n---",
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

_source line 91_

All style checks pass. Let me do a word count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "0bb2ccb8-d9ff-445c-81ac-0546f470d4dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLep77xJKYdkHidJ4XR4Xp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 66905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
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

_source line 92_

<details open><summary>🔧 Tool call — Bash · `toolu_01CwEKRnNNH3rfNxdEND8oon`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$%&~^_]//g; s/  */ /g' | wc -w",
  "description": "Estimate word count of experiments section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "f1410093-32dd-48b3-9aed-a3dcf5520108",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLep77xJKYdkHidJ4XR4Xp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 66905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 702
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

_source line 93 · 2026-05-21T04:10:50.791Z_

<details><summary>↩ Tool result · `toolu_01CwEKRnNNH3rfNxdEND8oon`</summary>

```text
2053
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "afc47d01-2dab-4af9-8d6a-ff5dac57c679",
  "tool_use_result": {
    "stdout": "2053",
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

_source line 94_

<details open><summary>🔧 Tool call — Bash · `toolu_012eo7J61ifDdsJUUWqtYaw7`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "description": "Raw word count including markup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "dbaea04d-43eb-4f5b-a1e3-16d62a8889a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1iXy64Pt3ATq7SjQGwRFd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 67607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
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

_source line 95 · 2026-05-21T04:10:53.381Z_

<details><summary>↩ Tool result · `toolu_012eo7J61ifDdsJUUWqtYaw7`</summary>

```text
2424 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "90b7c658-3172-4c28-8b72-f4eb56050433",
  "tool_use_result": {
    "stdout": "2424 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
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

_source line 96_

~2050 rendered words, ~2400 raw. Within target. Let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "c6dfdf52-ffa9-472a-a71e-45bb1bdb961f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8U6bRX3QLL62fYxJMVrj3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 67810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 171
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

_source line 97_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018pRVKBdR47SqoUZKvNpCsD`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "80180427-286f-4f8d-ac6b-69a2cb4479ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8U6bRX3QLL62fYxJMVrj3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 67810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 171
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

_source line 98 · 2026-05-21T04:10:57.036Z_

<details><summary>↩ Tool result · `toolu_018pRVKBdR47SqoUZKvNpCsD`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "333cb96e-696a-42dc-a3e4-d13ceafe6bb5",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01DfW6mUHBPYtJCwMzyCACry`</summary>

```json
{
  "name": "experiments_section_v1",
  "type": "paper",
  "description": "Experiments section (§4) for ICLR 2027 paper. 8 subsections: validation, temporal comparability (31% instability), ground truth mismatch, structural analysis, semi-synthetic framework, local independence, downstream impact (four-layer), GSM8K cross-benchmark validation. Includes 3 tables and 4 figures.",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "tags": [
    "paper",
    "experiments",
    "latex",
    "iclr2027"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "a793fd3a-6245-40ff-b016-6ab31a2615d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUMZwC7ymHPupWkGoRxSth",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 67981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 735
      },
      "output_tokens": 44,
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

_source line 100 · 2026-05-21T04:11:04.497Z_

<details><summary>↩ Tool result · `toolu_01DfW6mUHBPYtJCwMzyCACry`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_f524dc\", \"name\": \"experiments_section_v1\", \"type\": \"paper\", \"description\": \"Experiments section (§4) for ICLR 2027 paper. 8 subsections: validation, temporal comparability (31% instability), ground truth mismatch, structural analysis, semi-synthetic framework, local independence, downstream impact (four-layer), GSM8K cross-benchmark validation. Includes 3 tables and 4 figures.\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/paper/experiments.tex\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T04:11:04.241277+00:00\", \"tags\": [\"paper\", \"experiments\", \"latex\", \"iclr2027\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "66f2464f-a699-4f62-a767-fef360915f5a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_f524dc\\\", \\\"name\\\": \\\"experiments_section_v1\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Experiments section (§4) for ICLR 2027 paper. 8 subsections: validation, temporal comparability (31% instability), ground truth mismatch, structural analysis, semi-synthetic framework, local independence, downstream impact (four-layer), GSM8K cross-benchmark validation. Includes 3 tables and 4 figures.\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/paper/experiments.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T04:11:04.241277+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"experiments\\\", \\\"latex\\\", \\\"iclr2027\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_f524dc\", \"name\": \"experiments_section_v1\", \"type\": \"paper\", \"description\": \"Experiments section (§4) for ICLR 2027 paper. 8 subsections: validation, temporal comparability (31% instability), ground truth mismatch, structural analysis, semi-synthetic framework, local independence, downstream impact (four-layer), GSM8K cross-benchmark validation. Includes 3 tables and 4 figures.\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/paper/experiments.tex\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T04:11:04.241277+00:00\", \"tags\": [\"paper\", \"experiments\", \"latex\", \"iclr2027\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 101_

Experiments section written to `paper/sections/experiments.tex`. Summary:

**8 subsections, 3 tables, 4 figures, ~2050 rendered words.**

- **§4.1** Validation: power analysis confirms TPR 0.68--0.80, FPR 0.036--0.042 at cohort sizes (1 paragraph, Appendix ref)
- **§4.2** Temporal comparability: 31.3% ETS C, BH FDR removes only 3 items, sanity 0.18%, ability-quintile 2.9%, within-family 61.3%, within-subject 38.1%, 92.4% unexplained by domain improvement, architecture non-issue, threshold-robust (Table 1)
- **§4.3** Ground truth mismatch: enrichment 0.96 vs Li et al., dose-response ΔTPR +0.508/+0.674, web-overlap = wrong ground truth (Figure 2)
- **§4.4** Structural analysis: three approaches fail to reduce FPR below 31% (Table 2)
- **§4.5** Semi-synthetic: cross-subject matching ΔFPR=0.000, within-subject inflates +0.186 (Figure 3)
- **§4.6** Q3 local independence: 11.3% vs 2.2% (5x, p=2.3e-9), mild contributing factor
- **§4.7** Downstream impact: four layers (ρ≈0.997 redundancy, signal concentration with circularity ablation, model-family diagnostics, cross-benchmark) (Figure 4)
- **§4.8** GSM8K: C%=18.9%, ΔTPR=+0.818, GSM1K r=−0.478 negative correlation honestly reported (Figure 5, Table 3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "uuid": "6b4eae29-0853-4162-b630-d834d17655f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoB224iaEtRsBdC3noTZEw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 68716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

### Task result

_source line 102_

Experiments section written to `paper/sections/experiments.tex`. Summary:

**8 subsections, 3 tables, 4 figures, ~2050 rendered words.**

- **§4.1** Validation: power analysis confirms TPR 0.68--0.80, FPR 0.036--0.042 at cohort sizes (1 paragraph, Appendix ref)
- **§4.2** Temporal comparability: 31.3% ETS C, BH FDR removes only 3 items, sanity 0.18%, ability-quintile 2.9%, within-family 61.3%, within-subject 38.1%, 92.4% unexplained by domain improvement, architecture non-issue, threshold-robust (Table 1)
- **§4.3** Ground truth mismatch: enrichment 0.96 vs Li et al., dose-response ΔTPR +0.508/+0.674, web-overlap = wrong ground truth (Figure 2)
- **§4.4** Structural analysis: three approaches fail to reduce FPR below 31% (Table 2)
- **§4.5** Semi-synthetic: cross-subject matching ΔFPR=0.000, within-subject inflates +0.186 (Figure 3)
- **§4.6** Q3 local independence: 11.3% vs 2.2% (5x, p=2.3e-9), mild contributing factor
- **§4.7** Downstream impact: four layers (ρ≈0.997 redundancy, signal concentration with circularity ablation, model-family diagnostics, cross-benchmark) (Figure 4)
- **§4.8** GSM8K: C%=18.9%, ΔTPR=+0.818, GSM1K r=−0.478 negative correlation honestly reported (Figure 5, Table 3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 667267,
  "duration_api_ms": 667964,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "cec44886-51fb-4f55-8ce9-e846a3ecd2c0",
  "total_cost_usd": 1.5083777999999999,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 57506,
    "cache_read_input_tokens": 680564,
    "output_tokens": 26785,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 57506,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 455,
        "cache_read_input_tokens": 68716,
        "cache_creation_input_tokens": 631,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 631
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 4026,
      "outputTokens": 3198,
      "cacheReadInputTokens": 358573,
      "cacheCreationInputTokens": 66480,
      "webSearchRequests": 0,
      "costUSD": 0.13897330000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 26785,
      "cacheReadInputTokens": 680564,
      "cacheCreationInputTokens": 57506,
      "webSearchRequests": 0,
      "costUSD": 1.3694045,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3e80cab2-f536-4347-adbf-0a1f2a362976"
}
```

</details>

---
