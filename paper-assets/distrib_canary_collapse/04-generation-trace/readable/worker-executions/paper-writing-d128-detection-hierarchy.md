# paper writing d128 detection hierarchy

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_writing_d128_detection_hierarchy_20260520T092151.log`
- **Structured JSON:** [`c1ddb1da7d1520489c1c.json`](../../sessions/c1/c1ddb1da7d1520489c1c.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69",
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
  "uuid": "d185c62c-4aba-4f6b-bc13-0b439205d2b7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1779285000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "41de9e2b-d837-4c78-abb5-d02b7b9d3900",
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69"
}
```

---

### Assistant

_source line 4_

I'll read the required skill files and the target file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69",
  "uuid": "a5842701-2c52-4ea4-89c7-69b57c7522ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vsR2gA4YwHzygEhD1q165",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14311,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14311
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

<details open><summary>🔧 Tool call — Read · `toolu_0132kaM8R8XTt6jCDKpAfAvr`</summary>

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
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69",
  "uuid": "551fe518-929a-438e-9f54-e8128cedefd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vsR2gA4YwHzygEhD1q165",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14311,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14311
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

_source line 6 · 2026-05-20T09:22:05.816Z_

<details><summary>↩ Tool result · `toolu_0132kaM8R8XTt6jCDKpAfAvr`</summary>

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
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69",
  "uuid": "7f8bcda2-9daf-498c-b4a3-5b357b4308e4",
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

<details open><summary>🔧 Tool call — Read · `toolu_01L8CygB1yqDh1kyhfXoueKx`</summary>

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
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69",
  "uuid": "f8ea3350-2da0-47ca-8d82-5e981a5b89cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vsR2gA4YwHzygEhD1q165",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14311,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14311
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

_source line 8 · 2026-05-20T09:22:06.080Z_

<details><summary>↩ Tool result · `toolu_01L8CygB1yqDh1kyhfXoueKx`</summary>

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
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69",
  "uuid": "e5f582b3-0c0f-4c0a-8055-1f7a358397f1",
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

<details open><summary>🔧 Tool call — Read · `toolu_01KjCtQx48tDqVHp658nFY4P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69",
  "uuid": "24d7aa5f-5334-4dfa-aab8-87ef6bdbd9fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vsR2gA4YwHzygEhD1q165",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14311,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14311
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

_source line 10 · 2026-05-20T09:22:07.776Z_

<details><summary>↩ Tool result · `toolu_01KjCtQx48tDqVHp658nFY4P`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across six contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:method_sensitivity}, \S\ref{sec:regime}, and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha \in \{0.00, 0.25, 0.50, 0.75\}$ each use three seeds $\{42, 43, 44\}$; $\alpha{=}0.10$ uses a single seed (42, preliminary).
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}) and three \emph{downstream metrics}.
18	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
19	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).
20	Token entropy is the mean next-token prediction entropy $H(p_\theta | \text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.
21	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
22	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
23	Code and data will be released upon publication.
24	
25	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
26	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
27	Cross-correlation analysis uses a maximum lag of 5 generations.
28	Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all six contamination levels.
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
34	\label{tab:drift_summary}
35	\begin{tabular}{lccccc}
36	\toprule
37	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
38	\midrule
39	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
40	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
41	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
42	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
43	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
44	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	
50	\subsection{Method Sensitivity Analysis}
51	\label{sec:method_sensitivity}
52	
53	We open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.
54	If different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.
55	
56	\paragraph{Five-method ablation.}
57	We apply five lead-lag detection methods to the $\alpha{=}1.0$ condition (4~seeds, 16 canary$\to$downstream pairs).
58	The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{5/16} (31.3\%; moderate supplementary, \S\ref{sec:ty_limitation}).
59	Method choice alone swings significance from \textbf{100\% to 37.5\%} among the primary methods: 50--57\% of pairs classified as significant under one method flip to non-significant under another.
60	The spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is at least \textbf{62.5\%} across the primary methods.
61	Table~\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.
62	
63	\paragraph{First-differencing diagnostic.}
64	A single preprocessing decision can eliminate an entire analysis channel.
65	For canary$\to$diversity pairs at $\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.
66	For canary$\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$; Figure~\ref{fig:differencing_dmax}a).
67	The apparent canary$\to$perplexity relationship is entirely an artifact of co-trending.
68	Notably, at $\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.
69	
70	\paragraph{Augmentation order sensitivity.}
71	Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
72	After correcting the statsmodels API incompatibility (\S\ref{sec:ty_limitation}), TY achieves moderate detection (3--4/8 at $\alpha{\geq}0.50$) at the default $d_{\max}{=}1$; however, the qualitative finding that this single hyperparameter can swing conclusions between near-universal significance and near-universal non-significance remains, consistent with known properties of the Toda--Yamamoto procedure~\cite{toda1995statistical}.
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=\linewidth]{figures/differencing_dmax.pdf}
77	\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\alpha{=}1.0$, 4~seeds). \textbf{(a)}~First-differencing eliminates the canary$\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\to$diversity pairs retain significance after differencing (24/24$\to$24/24). \textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\max}$; after correcting the implementation (\S\ref{sec:ty_limitation}), TY achieves moderate detection at the default $d_{\max}{=}1$, but the qualitative sensitivity to this hyperparameter persists.}
78	\label{fig:differencing_dmax}
79	\end{figure}
80	
81	\paragraph{Inter-method agreement.}
82	Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\alpha{=}0.0$ through $\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.
83	Cross-architecture validation on GPT-2-medium (12 canary$\to$downstream pairs) yields Fleiss' $\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.
84	Restricting to three informative methods (excluding naive cross-correlation, which anchors the permissive extreme, and Toda--Yamamoto, which provides moderate supplementary signal) raises $\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.
85	Table~\ref{tab:method_comparison} extends the analysis across contamination levels.
86	Direction checking (D111) itself constitutes a sensitivity dimension beyond the five statistical methods: restricting to forward-direction associations inverts naive cross-correlation's profile from uniformly high (${\approx}100\%$ undirected) to regime-dependent, revealing that much of its apparent signal was reverse-directional.
87	At $\alpha{=}0.0$ (null control), naive cross-correlation still finds \textbf{75\%} (6/8) of forward-direction pairs significant---lower than the undirected 100\%, but still a substantial FPR.
88	Permutation Granger correctly finds 0\%, achieving perfect null-control specificity.
89	At $\alpha{=}0.50$ (fp32), permutation Granger finds 75\% (6/8), while naive finds 37.5\% (Figure~\ref{fig:consensus_heatmap}; Table~\ref{tab:method_comparison}).
90	
91	\paragraph{Method$\times$regime interaction.}
92	Table~\ref{tab:method_comparison} reveals that direction checking reshapes the method hierarchy across contamination levels.
93	At $\alpha{=}0.25$, naive cross-correlation drops to 12.5\% while permutation Granger remains at 0\%, narrowing the gap visible in undirected analysis.
94	At $\alpha{\geq}0.75$, naive rises to 87.5\% while permutation Granger reaches 75\%; both methods detect, but naive's persistent 75\% null-control FPR means its high-$\alpha$ detections cannot be distinguished from false positives without the consensus framework.
95	This regime-dependent reversal, combined with the block structure visible in Figure~\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \S\ref{sec:regime}.
96	
97	\paragraph{Why permutation Granger succeeds.}
98	The systematic comparison identifies PermG as the only method combining zero null-control FPR with consistent detection across all regimes where signal exists ($\alpha{\geq}0.50$).
99	Three properties explain this outcome.
100	First, the nonparametric permutation procedure inherently controls FPR by constructing the null distribution from the observed data rather than from distributional assumptions, making it robust to the non-stationarity that inflates false positives in correlation-based methods.
101	Second, Granger tests are directional by construction: they test whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history, naturally filtering the reverse-directional associations that inflate naive cross-correlation's FPR.
102	Third, PermG does not require threshold calibration or augmentation order selection, avoiding the hyperparameter sensitivity observed in Toda--Yamamoto (Figure~\ref{fig:differencing_dmax}b; \S\ref{sec:ty_limitation}) and the power limitations that reduce threshold onset to near-zero detection under $3\sigma$ calibration (\S\ref{sec:threshold_limitation}).
103	By contrast, differenced cross-correlation retains 100\% FDR significance in both forward \emph{and} reverse directions at $\alpha{=}0.75$, failing to distinguish genuine directional precedence from shared dynamics; and Toda--Yamamoto, while achieving moderate detection (3--4/8 at $\alpha{\geq}0.50$), remains sensitive to the augmentation order $d_{\max}$ (\S\ref{sec:ty_limitation}).
104	These complementary failures, exposed through the MMCT evaluation framework, converge on a single recommendation: for short iterative training series ($T{\leq}20$), permutation Granger causality should be the primary detection method.
105	
106	\begin{figure}[t]
107	\centering
108	\includegraphics[width=\linewidth]{figures/consensus_heatmap.pdf}
109	\caption{Method$\times$regime consensus heatmap (Pythia-410M, fp32, 12 contamination levels, direction-checked). Each cell shows the forward-direction detection rate (\% of 8 pairs reaching FDR significance) for five individual methods (top) and two consensus thresholds (bottom, separated by white line). Direction checking dramatically reshapes method profiles: naive cross-correlation drops from near-100\% (undirected) to regime-dependent rates with persistent 75\% null-control FPR. Permutation Granger achieves FPR${=}$0\% in the blind zone (green dashed box) and detects only at $\alpha{\geq}0.50$. The onset boundary ($\alpha{\approx}0.45$--$0.50$) is where method divergence is sharpest (Pitfall~3). \emph{Note: figure will be regenerated with D120 canonical data including corrected TY rates (\S\ref{sec:ty_limitation}).}}
110	\label{fig:consensus_heatmap}
111	\end{figure}
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\caption{Forward-direction FDR significance rates (\%) for five lead-lag methods across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Direction checking reshapes method profiles: naive cross-correlation drops from near-100\% (undirected) to regime-dependent rates (75\% at the null, 12.5\% at $\alpha{=}0.25$, rising to 87.5\% at $\alpha{=}0.75$). Each cell reports the fraction of 8 validated canary$\to$downstream pairs reaching BH-corrected significance ($q{=}0.05$) in the forward direction. $^\dagger$Moderate supplementary method (\S\ref{sec:ty_limitation}); FPR$_\text{null}$ pending (null condition not yet run through corrected pipeline). $^a$Seed-42 null-control rate under D105 $3\sigma$ calibration pending; 3-seed range 12.5--37.5\%.}
117	\label{tab:method_comparison}
118	\begin{tabular}{lcccccc}
119	\toprule
120	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
121	\midrule
122	Naive XCorr     & 75    & 12.5 & 37.5 & 87.5  & 0     & 75   \\
123	Diff.\ XCorr    & 0     & 37.5 & 87.5 & 75    & 75    & 0    \\
124	Threshold ($3\sigma$)$^a$ & ---   & 0    & 50   & 0     & 0     & ---  \\
125	Perm.\ Granger  & 0     & 0    & 75   & 75    & 75    & 0    \\
126	Toda--Yamamoto$^\dagger$  & ---   & 0    & 37.5 & 37.5  & 50    & ---  \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	
132	\subsection{Regime-Dependent Detectability}
133	\label{sec:regime}
134	
135	Beyond method choice, the contamination level~$\alpha$ determines whether a temporal lead exists to detect.
136	We present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.
137	
138	\paragraph{Raw drift.}
139	Table~\ref{tab:drift_summary} shows that diversity collapse occurs at \emph{all} contamination levels, not only under full synthetic replacement.
140	Distinct-1 declines by 13.8\% even at $\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets).
141	A single-seed observation at $\alpha{=}0.10$ reveals a steep diversity cliff: distinct-1 drops by 39.6\%, nearly matching the 3-seed mean at $\alpha{=}0.25$ ($-40.3{\pm}0.3\%$); distinct-2 shows a comparable jump ($-56.4\%$ vs.\ $-56.4{\pm}0.7\%$ at $\alpha{=}0.25$).
142	Token entropy at $\alpha{=}0.10$, however, differs from the null by less than 1 percentage point ($-5.3\%$ vs.\ $-4.6{\pm}0.4\%$), constituting a canary blind spot in which diversity has already collapsed but no canary metric responds.
143	At higher contamination, distinct-1 decline continues: $-37.1{\pm}0.4\%$ ($\alpha{=}0.50$), $-32.3{\pm}0.5\%$ ($\alpha{=}0.75$), and $-27.8{\pm}1.6\%$ ($\alpha{=}1.0$).
144	The non-monotonic pattern (diversity declining \emph{more} at moderate~$\alpha$ than at extreme~$\alpha$) is confirmed by 3-seed replication at $\alpha{=}0.25$ (std${=}0.3\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.
145	
146	\begin{figure}[t]
147	\centering
148	\includegraphics[width=\linewidth]{figures/fig_dose_response.pdf}
149	\caption{Dose-response profile of permutation Granger forward detection rate (Pythia-410M, fp32, 12 contamination levels, direction-checked).
150	Four regimes emerge: blind spot ($\alpha{\leq}0.45$, 0/8), onset ($\alpha{=}0.50$, 75\%), synchronous collapse ($\alpha{=}0.60$, 37.5\%; orange diamond), and detection zone ($\alpha{\geq}0.75$, 62.5--75\%).
151	The $\alpha{=}0.60$ dip is dual-seed confirmed (s42: 3/8, s43: 0/8).
152	Per-method comparison is in Figure~\ref{fig:consensus_heatmap}.}
153	\label{fig:regime_map}
154	\end{figure}
155	
156	\paragraph{Granger-precedence detectability.}
157	Despite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\ref{fig:regime_map}).
158	Permutation Granger tests (first-differenced, BH-corrected) find 0/8 pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$ (including $\alpha{=}0.25$ where a faint single-pair signal appears at FDR $p{=}0.053$ but aggregate detection remains null, and $\alpha{=}0.35$/$0.40$/$0.45$ which confirm PermG fwd${=}$0/8), \textbf{6/8} at $\alpha{=}0.50$ (2~fp32 seeds, consistent), \textbf{3/8} and \textbf{0/8} at $\alpha{=}0.60$ (s42 and s43 respectively; dual-seed confirmed non-monotonic dip), and \textbf{6/8} at $\alpha{=}1.0$.
159	At $\alpha{=}0.75$ (3~seeds), permutation Granger finds 20/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.
160	Under Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.
161	Within-$\alpha$ multi-seed analysis at $\alpha{=}1.0$ yields \textbf{24/24} canary$\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.
162	Permutation Granger forward significance is the primary detection indicator (Figure~\ref{fig:regime_map}): it reaches 6/8 at $\alpha{=}0.50$, dips to 3/8 at $\alpha{=}0.60$ (synchronous collapse zone; see below), and recovers to 5--6/8 at $\alpha{\geq}0.75$.
163	The onset boundary lies at $\alpha{\approx}0.45$--$0.50$: finer-grained probing at $\alpha{=}0.35$, $0.40$, and $0.45$ yields PermG fwd${=}$0/8 at all three levels, extending the blind spot through $\alpha{=}0.45$.
164	A faint signal first appears at $\alpha{=}0.25$ (best-pair FDR $p{=}0.053$) but does not translate to aggregate detection; reliable detection begins at $\alpha{=}0.50$ (6/8, 2~seeds).
165	This sharp phase transition is consistent with theoretical expectations about signal-to-noise limits in short time series~\cite{boettiger2012limits}.
166	Sensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\ref{app:robustness}).
167	Cross-architecture validation on GPT-2-medium confirms this boundary: at $\alpha{=}0.25$, at most 1/8 pairs reach $K{\geq}3$ ($3\sigma$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\%$ vs.\ Pythia $-4.7{\pm}0.5\%$), while at $\alpha{=}1.0$ all 6 canary$\to$diversity pairs reach significance (\S\ref{sec:discussion}).
168	Table~\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.
169	At $\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\geq}4/5$) and 7/8 at Tier~2 ($K{\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.
170	
171	\begin{table}[t]
172	\centering
173	\small
174	\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\alpha{=}0.25$ and $\alpha{=}1.0$. Tier~3: $K{\geq}4/5$ methods (or $K{\geq}3$ of 4 effective methods; \S\ref{sec:threshold_limitation}); Tier~2: $K{\geq}3/5$. Drift is generation~0$\to$10. GPT-2-medium $\alpha{=}0.25$: single seed (seed=42); Pythia $\alpha{=}0.25$: 3-seed mean${\pm}$std. The onset boundary ($\alpha{\approx}0.45$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}
175	\label{tab:cross_arch_regime}
176	\begin{tabular}{llcccccc}
177	\toprule
178	$\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\ Granger & Tier~3 \\
179	\midrule
180	0.25 & Pythia-410M  & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & 0/8 & 0/8 \\
181	0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\
182	\midrule
183	1.00 & Pythia-410M  & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & 6/8 & 6/8 \\
184	1.00 & GPT-2-medium & \multicolumn{6}{c}{(reported in \S\ref{sec:discussion}; 6/8 canary$\to$downstream pairs at Tier~3)} \\
185	\bottomrule
186	\end{tabular}
187	\end{table}
188	
189	\paragraph{Detectability at $\alpha{=}0.50$ and the transition zone.}
190	Under fp32 precision, $\alpha{=}0.50$ is reliably detected: permutation Granger finds 6/8 pairs FDR-significant across both seeds (Table~\ref{tab:method_comparison}).
191	The transition from undetectable to reliably detectable occurs between $\alpha{=}0.45$ and $\alpha{=}0.50$: finer-grained probing confirms PermG fwd${=}$0/8 at $\alpha{=}0.35$, $0.40$, and $0.45$, while $\alpha{=}0.50$ achieves 6/8 (2~seeds).
192	A faint single-pair signal first appears at $\alpha{=}0.25$ (entropy$\to$distinct-1: raw $p{=}0.007$, FDR-corrected $p{=}0.053$), but all aggregate indicators remain null through $\alpha{=}0.45$, placing the onset boundary at $\alpha{\approx}0.45$--$0.50$.
193	At $\alpha{=}0.50$, canary sensitivity remains metric-dependent: ECE achieves significance in both fp32 seeds, while token entropy remains below the FDR threshold ($p_{\text{fdr}}{\geq}0.086$), identifying ECE as the more sensitive canary near the onset boundary.
194	Figure~\ref{fig:consensus_heatmap} visualizes the method$\times\alpha$ interaction, revealing a block structure that separates correlation-based methods from causal methods as a function of regime.
195	
196	\paragraph{Non-monotonic dose-response: the synchronous collapse zone.}
197	Dual-seed replication at $\alpha{=}0.60$ reveals a non-monotonic dose-response in Granger detectability: PermG fwd drops to 3/8 (s42) and 0/8 (s43), below both $\alpha{=}0.50$ (6/8, 2~seeds) and $\alpha{=}0.75$ (5--6/8 per seed, 3~seeds).
198	This creates a four-regime structure in the dose-response profile: \emph{blind spot} ($\alpha{\leq}0.45$, 0/8), \emph{onset} ($\alpha{\approx}0.45$--$0.50$), \emph{synchronous collapse} ($\alpha{\approx}0.60$, 0--3/8), and \emph{detection zone} ($\alpha{\geq}0.75$, 5--8/8).
199	The dip is inconsistent with a monotonically increasing signal-to-noise model; we hypothesize that at $\alpha{=}0.60$, canary and downstream metrics respond to contamination simultaneously rather than sequentially, destroying the temporal lead that Granger tests require (\S\ref{sec:discussion}).
200	The synchronous zone is mechanistically distinct from the blind spot: in the blind spot, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.
201	Toda--Yamamoto achieves moderate detection across this range (3--4/8 at $\alpha{\geq}0.50$; \S\ref{sec:ty_limitation}), with its detection at $\alpha{=}0.60$ suggesting partial inter-method complementarity in the synchronous collapse zone where PermG drops to 0--3/8.
202	This non-monotonicity also implies that simple threshold-based triggers (such as the 15\% entropy criterion in \S\ref{sec:intervention}) may outperform formal Granger tests at intermediate contamination levels.
203	
204	
205	\subsection{Case Study: Canary Prediction of Diversity Collapse}
206	\label{sec:case_study}
207	
208	Having established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).
209	We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
210	
211	\paragraph{Full synthetic replacement ($\alpha{=}1.0$, 4 seeds).}
212	Token entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \S\ref{sec:discussion}).
213	Cross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.
214	Figure~\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.
215	Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
216	Reverse-direction tests (downstream$\to$canary) on WikiText-103 find \textbf{0/24} FDR-significant (all $p{>}0.49$), establishing directional asymmetry in this domain.\footnote{C4 exhibits domain-dependent directionality: at $\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling (\S\ref{sec:discussion}).}
217	
218	\begin{figure}[t]
219	\centering
220	\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}
221	\caption{Metric trajectories across 10 generations at $\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}
222	\label{fig:metric_trajectory}
223	\end{figure}
224	
225	\paragraph{High contamination ($\alpha{=}0.75$, 3 seeds).}
226	Directional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 20/24 forward pairs FDR-significant, 0/24 reverse).
227	However, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\alpha{=}0.75$ squarely in the transitional detection regime.
228	Differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\S\ref{sec:pitfalls}).
229	
230	\paragraph{ECE as a conditional secondary canary.}
231	ECE's forward consensus matches token entropy (both achieve PermG\_fwd 6/8 across all conditions), but the reverse profile diverges sharply.
232	Across 7 validated conditions at $\alpha{=}1.0$ (3 architectures $\times$ 2 scales $\times$ 2 domains), token entropy reverse direction yields \textbf{0/28} FDR-significant pairs (consistent with unidirectional forward causation at full synthetic replacement; domain-dependent bidirectionality emerges at lower $\alpha$, \S\ref{sec:discussion}), while ECE reverse direction yields \textbf{13/28} significant pairs, with 5/7 conditions containing at least one reverse-significant pair, all in the distinct$\to$ECE direction.
233	This bidirectional coupling is the core reason ECE is classified as a secondary canary: ECE and diversity exhibit mutual feedback, and the interpretability of ECE's causal direction is correspondingly limited.
234	This result also instantiates Claim~3 (method sensitivity): when only forward significance is considered, the two canary types appear equivalent; incorporating reverse-direction tests separates them. The choice of analysis dimension alters the canary classification itself.
235	
236	\paragraph{Failed canary candidates.}
237	Not all metrics serve as canaries.
238	Effective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.
239	Effective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\alpha{=}0.25$ it \emph{increases} from 2.37 to 8.48 (+258\%).
240	The GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.
241	This opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\S\ref{sec:discussion}).
242	
243	\paragraph{Consensus filtering.}
244	Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline (PermG fwd ${\geq}6/8$, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).
245	The 10 eliminated pairs comprise all canary$\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).
246	The consensus framework reduces the naive 75\% forward-direction FPR to 0\%, matching the most conservative individual methods (Figure~\ref{fig:consensus_workflow}).
247	
248	
249	\subsection{Consensus Framework Validation}
250	\label{sec:consensus_validation}
251	
252	We validate the consensus framework's calibration using built-in experimental controls.
253	
254	\paragraph{False positive rate.}
255	At $\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.
256	Individual-method forward-direction FPR ranges from \textbf{75\%} (naive cross-correlation: 6/8) through 37.5\% (threshold) down to \textbf{0\%} (permutation Granger and differenced cross-correlation); Toda--Yamamoto's null-control FPR has not yet been evaluated through the corrected pipeline (\S\ref{sec:ty_limitation}).
257	The multi-method consensus at $K{\geq}3$ ($3\sigma$) achieves \textbf{FPR${=}$0\%} (0/24 pairs, three independent seeds), matching the best individual method (permutation Granger) while providing a formal benchmark for method reliability (Table~\ref{tab:fpr_fnr}).
258	
259	\paragraph{False negative rate.}
260	At $\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\geq}3\times$ the $\alpha{=}0.0$ baseline (entropy $11.93\times$, ECE $73.12\times$) and canary onset strictly preceding downstream onset by ${\geq}1$ generation (\S\ref{sec:calibration}).
261	FNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\geq}3/4$, $S{\geq}3/4$, all~6 are recovered (\textbf{FNR${=}$0\%}).
262	Toda--Yamamoto's individual FNR is 50\% (4/8 detected at $\alpha{=}1.0$, seed~42), consistent with its moderate supplementary classification (\S\ref{sec:ty_limitation}).
263	Both FPR and FNR are validated on the joint method${\times}$seed dimension (FPR: 3~seeds at $\alpha{=}0.0$; FNR: 4~seeds at $\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\geq}3$).
264	Table~\ref{tab:fpr_fnr} reports the calibration results.
265	Table~\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\alpha$ including the null control, while permutation Granger achieves correct verdicts at all levels with zero FPR.
266	
267	\begin{table}[t]
268	\centering
269	\caption{Single-method inference errors across contamination levels.
270	Each cell shows the verdict (significant or not) based on multi-seed majority ($\geq$2/3 seeds with $\geq$4/8 pairs significant).
271	\checkmark\ = correct, \textcolor{red}{FP} = false positive, \textcolor{blue}{FN} = false negative, $\circ$ = ambiguous ground truth (either verdict plausible).
272	Naive XCorr produces false positives at \emph{every} $\alpha$ including the null control. Permutation Granger achieves correct verdicts at all levels with zero FPR. $^\dagger$Rows marked pending have cross-script inconsistencies under audit.}
273	\label{tab:single-method-errors}
274	\resizebox{\columnwidth}{!}{%
275	\begin{tabular}{lccccc}
276	\toprule
277	 & \multicolumn{2}{c}{\textit{No signal}} & \textit{Ambiguous} & \multicolumn{2}{c}{\textit{Causal signal}} \\
278	\cmidrule(lr){2-3} \cmidrule(lr){4-4} \cmidrule(lr){5-6}
279	Method & $\alpha{=}0.00$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.00$ \\
280	\midrule
281	Naive XCorr
282	  & \textcolor{red}{FP}{\scriptsize\ 8,7,8}
283	  & \textcolor{red}{FP}{\scriptsize\ 8,8}
284	  & $\circ${\scriptsize\ 8,8,8}
285	  & \checkmark{\scriptsize\ 8,8,8}
286	  & \checkmark{\scriptsize\ 8,8,8} \\
287	Diff XCorr (FDR)$^\dagger$
288	  & --- & --- & --- & --- & --- \\
289	Threshold Onset$^\dagger$
290	  & --- & --- & --- & --- & --- \\
291	Perm Granger (FDR)
292	  & \checkmark{\scriptsize\ 0,0,0}
293	  & \checkmark{\scriptsize\ 0,0}
294	  & $\circ${\scriptsize\ 0,6,3}
295	  & \checkmark{\scriptsize\ 8,5,6}
296	  & \checkmark{\scriptsize\ 6,6,6} \\
297	TY Granger$^\dagger$
298	  & --- & --- & --- & --- & --- \\
299	\midrule
300	\textbf{Consensus ($K{\geq}3$)}$^\dagger$
301	  & --- & --- & --- & --- & --- \\
302	\bottomrule
303	\multicolumn{6}{l}{\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\
304	\multicolumn{6}{l}{\footnotesize Seeds: $\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\alpha{=}0.25$: 43, 44; $\alpha{=}1.00$: 42, 43, 45.} \\
305	\end{tabular}%
306	}
307	\end{table}
308	
309	\paragraph{Bootstrap power analysis.}
310	To quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\alpha{=}1.0$).
311	Permutation Granger achieves power${=}1.0$ on genuine pairs (canary$\to$diversity) and power${=}0.0$ on spurious pairs (canary$\to$perplexity), providing clean separation.
312	Toda--Yamamoto achieves power${=}0.50$ on genuine pairs (4/8 detected at $\alpha{=}1.0$), consistent with its moderate supplementary classification (\S\ref{sec:ty_limitation}).
313	We note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\beta{=}0.3$).
314	
315	\begin{table}[t]
316	\centering
317	\small
318	\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\geq}3$ ($3\sigma$, excluding threshold onset; \S\ref{sec:threshold_limitation}) achieves FPR${=}$0\% and FNR${=}$0\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration of any single method. FPR: $\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds). $^\dagger$Moderate supplementary method (\S\ref{sec:ty_limitation}); FPR pending (null condition not yet run through corrected pipeline); FNR from single-seed $\alpha{=}1.0$ (4/8 detected).}
319	\label{tab:fpr_fnr}
320	\begin{tabular}{lcc}
321	\toprule
322	Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
323	\midrule
324	Naive XCorr              & 100\%              & 0\%  \\
325	Differenced XCorr        & 37.5\%             & 0\%  \\
326	Threshold Onset          & 20.8\% (12.5--37.5) & 0\%  \\
327	Permutation Granger      & 0\%                & 0\%  \\
328	Toda--Yamamoto$^\dagger$  & ---                & 50\%   \\
329	\midrule
330	Consensus ($K{\geq}3$, $3\sigma$)      & 0\%    & 0\%  \\
331	Consensus ($K{\geq}3$, $S{\geq}3/4$)   & 0\%    & 0\%  \\
332	\bottomrule
333	\end{tabular}
334	\end{table}
335	
336	
337	\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}
338	\label{sec:generalization}
339	
340	The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).
341	To test whether these findings transfer, we evaluate the lead-lag pattern along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).
342	All conditions use $\alpha{=}1.0$; architecture conditions use a single seed, while scale and domain conditions use two seeds (s42, s43) to assess replicability.
343	
344	\begin{table}[t]
345	\centering
346	\small
347	\caption{Cross-architecture lead-lag detectability ($\alpha{=}1.0$, D105 unified pipeline, $3\sigma$ calibration, M035 direction-corrected).
348	PermG~fwd: permutation Granger forward-direction FDR-significant pairs (out of 8).
349	$K{\geq}3$: pairs where ${\geq}3$ of 5 methods reach FDR significance (direction-checked, $3\sigma$).
350	PermG~fwd ${\geq}6/8$ in 12/14 confirmed conditions; $K{\geq}3$ ${\geq}6/8$ in 10/14 (11/14 pending Padding-410M audit).
351	Exceptions: Pythia-1.4B (s42: 1/8$^\dagger$, s43: 3/8) and SmolLM3-3B (3/8$^\ddagger$).
352	Rows marked ``---'' are running experiments; final values will be filled without format changes.}
353	\label{tab:generalization}
354	\begin{tabular}{lrclcc}
355	\toprule
356	Model & Params & Seed & Domain & PermG (fwd) & $K{\geq}3$ \\
357	\midrule
358	\multicolumn{6}{l}{\emph{Baseline}} \\
359	Pythia-410M       & 410M & s42 & Wiki & 6/8            & 6/8            \\
360	Pythia-410M       & 410M & s43 & Wiki & 6/8            & 6/8            \\
361	\addlinespace
362	\multicolumn{6}{l}{\emph{Scale}} \\
363	Pythia-1.4B       & 1.4B & s42 & Wiki & \textbf{2/8}$^\dagger$ & \textbf{1/8}$^\dagger$  \\
364	Pythia-1.4B       & 1.4B & s43 & Wiki & 6/8            & 3/8     \\
365	Pythia-6.9B       & 6.9B & s42 & Wiki & 7/8$^*$        & 6/8            \\
366	Pythia-6.9B       & 6.9B & s43 & Wiki & ---            & ---            \\
367	\addlinespace
368	\multicolumn{6}{l}{\emph{Architecture}} \\
369	GPT-2-medium      & 345M & s42 & Wiki & 6/8            & 6/8            \\
370	GPT-2-medium      & 345M & s43 & Wiki & 6/8            & 6/8            \\
371	OPT-1.3B          & 1.3B & s42 & Wiki & 6/8            & 6/8            \\
372	OPT-1.3B          & 1.3B & s43 & Wiki & 6/8            & 6/8            \\
373	Qwen3.5-0.8B      & 0.8B & s42 & Wiki & 8/8            & 6/8            \\
374	Qwen3.5-0.8B      & 0.8B & s43 & Wiki & ---            & ---            \\
375	SmolLM3-3B        & 3.0B & s42 & Wiki & \textbf{3/8}$^\ddagger$ & \textbf{3/8}$^\ddagger$ \\
376	SmolLM3-3B        & 3.0B & s43 & Wiki & ---            & ---            \\
377	\addlinespace
378	\multicolumn{6}{l}{\emph{Tokenization}} \\
379	Padding-410M      & 410M & s42 & Wiki & 6/8            & 6/8$^{\S}$     \\
380	\addlinespace
381	\multicolumn{6}{l}{\emph{Domain}} \\
382	Pythia-1B         & 1.0B & s42 & C4   & 8/8            & 7/8            \\
383	Pythia-1B         & 1.0B & s43 & C4   & 7/8            & 6/8            \\
384	\bottomrule
385	\multicolumn{6}{l}{\footnotesize $^\dagger$Seed-sensitive: PermG s42 2/8, s43 6/8; $K{\geq}3$ s42 1/8, s43 3/8. Likely stochastic instability at this scale (\S\ref{sec:discussion}).} \\
386	\multicolumn{6}{l}{\footnotesize $^\ddagger$Canary metric splitting: only ECE$\to$downstream pairs detected (3/4); entropy$\to$downstream 0/4 (\S\ref{sec:smollm3}).} \\
387	\multicolumn{6}{l}{\footnotesize $^*$bf16 precision (model exceeds single-GPU fp32 capacity).} \\
388	\multicolumn{6}{l}{\footnotesize $^{\S}$Padding-410M $K{\geq}3$ pending supplementary audit (expected stable at 6/8).} \\
389	\multicolumn{6}{l}{\footnotesize Full method-level breakdown ($K{\geq}4$) in Appendix~\ref{app:cross_arch}.} \\
390	\end{tabular}
391	\end{table}
392	
393	\paragraph{Cross-condition robustness.}
394	Table~\ref{tab:generalization} confirms that the entropy-leads-diversity pattern is robust across 14 confirmed conditions (3 pending) spanning six model families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B, and two training domains (WikiText-103, C4).
395	Permutation Granger forward significance reaches ${\geq}6/8$ in 12 of 14 conditions (85.7\%), with two exceptions: Pythia-1.4B seed~42 (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\to$downstream pairs are detected (see below).
396	$K{\geq}3$ multi-method consensus reaches ${\geq}6/8$ in 10 of 14 conditions (11/14 pending Padding-410M audit), with exceptions Pythia-1.4B (s42: 1/8, s43: 3/8) and SmolLM3-3B (3/8).
397	The concordance between PermG and $K{\geq}3$ confirms that multi-method consensus is robust across architectures.
398	With threshold onset power-limited and Toda--Yamamoto providing moderate supplementary signal (3--4/8 at $\alpha{\geq}0.50$; \S\ref{sec:ty_limitation}), $K{\geq}3$ draws on four contributing methods---a stronger standard than simple majority (\S\ref{sec:consensus}).
399	
400	\paragraph{Scale generalization.}
401	Scaling from 410M to 6.9B parameters confirms that the lead-lag pattern persists across a $17\times$ parameter range.
402	Pythia-6.9B achieves PermG fwd~7/8 (bf16), the strongest single-seed detection.
403	Within the Pythia family, 1.4B shows seed dependence: s42 yields only 2/8 (the sole outlier across all conditions), while s43 recovers to 6/8.
404	Qwen3.5-0.8B (PermG~fwd~8/8) extends the finding beyond the Pythia/GPT-2/OPT decoder-only family to an independently trained architecture with a different tokenizer.
405	
406	\paragraph{Domain generalization.}
407	Replacing WikiText-103 with C4 yields the strongest forward detection: Pythia-1B achieves PermG~fwd~8/8 in both seeds at $\alpha{=}1.0$, confirming that the lead-lag pattern is not an artifact of narrow topical distribution.
408	However, directional asymmetry does not transfer fully across domains.
409	At $\alpha{=}0.50$ (Pythia-410M, C4, s42 fp32), PermG reverse reaches 7/8 (compared to 0/8 in all WikiText conditions), indicating near-symmetric bidirectional coupling between canary and downstream metrics.
410	This domain-dependent directionality suggests that the unidirectional forward causation observed in WikiText may partly reflect domain-specific dynamics rather than a universal property of collapse; implications are discussed in \S\ref{sec:discussion}.
411	
412	\paragraph{Canary metric sensitivity: the SmolLM3-3B case.}
413	\label{sec:smollm3}
414	SmolLM3-3B (PermG fwd 3/8) reveals that canary metric choice is itself a dimension of method sensitivity.
415	Decomposing by canary type: ECE$\to$downstream achieves 3/4 significant pairs, while token entropy$\to$downstream achieves 0/4.
416	The root cause is that SmolLM3's token entropy exhibits non-monotonic oscillations across generations, violating the monotonic decline pattern that Granger tests exploit; ECE, by contrast, maintains its monotonic upward trajectory.
417	Multi-method consensus confirms the severity: entropy pairs activate only via naive and differenced cross-correlation (per-pair $K{=}2$), ECE pairs activate only via differenced cross-correlation and permutation Granger (per-pair $K{=}2$), and no pair exceeds two-method agreement---illustrating that even within a single architecture, the method panel fragments along canary metric boundaries.
418	This architecture-dependent canary sensitivity complements the finding that effective rank direction is model-dependent (\S\ref{sec:case_study}): no single canary metric is universally optimal across all architectures, enriching Claim~3 by adding canary metric selection as a further source of analytic variability.
419	
420	\subsection{Canary-Based Early Intervention}
421	\label{sec:intervention}
422	
423	To test whether the lead-lag relationship translates into practical utility, we implement a predictive cessation protocol: training with synthetic data ($\alpha{=}1.0$) continues until token entropy drops ${>}15\%$ relative to generation~0, at which point $\alpha$ is switched to $0.0$ (pure real data).
424	We compare against a reactive baseline that triggers only when distinct-1 drops ${>}10\%$---a downstream metric that, by the lead-lag hypothesis, should respond later.
425	
426	\paragraph{Pythia-410M.}
427	The predictive trigger fires at generation~1 in both seed-precision pairs tested (s42 fp32: entropy $3.234{\to}1.918$, ${\downarrow}40.7\%$; s43 bf16: $3.257{\to}2.523$, ${\downarrow}22.5\%$).
428	The reactive baseline triggers one generation later (generation~2, distinct-1 ${\downarrow}15.6\%$).
429	Predictive intervention reduces peak perplexity by 63\% relative to reactive ($56.99$ vs.\ $157.09$, s42 fp32) and achieves full recovery by generation~2 versus generation~4 for reactive.
430	The bf16 pair shows a milder perturbation (peak perplexity $24.65$ vs.\ $56.99$) consistent with stochastic rounding regularization, but the structural pattern---generation~1 trigger, generation~2 recovery---is identical.
431	Both conditions converge to the $\alpha{=}0.0$ baseline by generation~10.
432	
433	\paragraph{Cross-scale validation: Pythia-1.4B.}
434	Pythia-1.4B (s42 fp32) replicates the 410M pattern: token entropy drops $51.9\%$ at generation~1 ($2.946{\to}1.418$), exceeding the 15\% threshold, and recovers to $2.892$ by generation~2 ($98.2\%$ of baseline).
435	Perplexity spikes from $19.68$ to $65.37$ at the trigger generation and recovers to $17.44$ by generation~2 (stable at $17.60$ through generation~10).
436	The trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\times$ scale gap (410M to 1.4B), confirming that the canary-based intervention mechanism is scale-independent: the 15\% entropy threshold generalizes without recalibration across model sizes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d97a7498-df60-4dca-8e25-9f7736d16b69",
  "uuid": "ed04abab-ea84-49ab-9410-08d949253f2e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\nPythia provides a controlled setting: small enough for multi-seed experiments across six contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\S\\ref{sec:method_sensitivity}, \\S\\ref{sec:regime}, and \\S\\ref{sec:discussion}.\nTraining data is drawn from WikiText-103 \\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\n\nOur protocol follows the replace paradigm of \\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\alpha{<}1.0$.\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$.\nThe $\\alpha{=}1.0$ condition uses four random seeds $\\{42, 43, 44, 45\\}$; $\\alpha \\in \\{0.00, 0.25, 0.50, 0.75\\}$ each use three seeds $\\{42, 43, 44\\}$; $\\alpha{=}0.10$ uses a single seed (42, preliminary).\n\nWe track two \\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\cite{scheffer2009early}) and three \\emph{downstream metrics}.\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\nToken entropy is the mean next-token prediction entropy $H(p_\\theta | \\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\S\\ref{sec:case_study}).\nResults for distinct-3 are reported in Appendix~\\ref{app:distinct3}.\nCode and data will be released upon publication.\n\nAll hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\cite{shojaie2022granger}.\nCross-correlation analysis uses a maximum lag of 5 generations.\nTable~\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all six contamination levels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\\alpha{=}0.25$: distinct-1 $-40.3{\\pm}0.3\\%$) rather than full replacement ($\\alpha{=}1.0$: $-27.8{\\pm}1.6\\%$). $^\\dagger$$\\alpha{=}0.10$: single seed (seed~42, preliminary). $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std (seeds 42, 43, 44); $\\alpha{=}1.0$: 4-seed mean${\\pm}$std (seeds 42, 43, 44, 45).}\n\\label{tab:drift_summary}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-4.6{\\pm}0.4$ & $+37.6{\\pm}14$ & $-14.1{\\pm}0.4$ & $-9.6{\\pm}0.4$ & $-20.6{\\pm}1.0$ \\\\\n0.10$^\\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\\\\n0.25 & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & $-18.1{\\pm}0.8$ \\\\\n0.50 & $-18.0{\\pm}0.5$ & $+822.6{\\pm}18.3$ & $-37.1{\\pm}0.4$ & $-50.4{\\pm}1.0$ & $+21.0{\\pm}0.1$ \\\\\n0.75 & $-27.6{\\pm}0.2$ & $+1791{\\pm}18$ & $-32.3{\\pm}0.5$ & $-41.0{\\pm}1.0$ & $+182.6{\\pm}0.7$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3674{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Method Sensitivity Analysis}\n\\label{sec:method_sensitivity}\n\nWe open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.\nIf different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.\n\n\\paragraph{Five-method ablation.}\nWe apply five lead-lag detection methods to the $\\alpha{=}1.0$ condition (4~seeds, 16 canary$\\to$downstream pairs).\nThe fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \\textbf{16/16} (100\\%), differenced cross-correlation \\textbf{14/16} (87.5\\%), threshold onset detection \\textbf{9/16} (56.3\\%), permutation Granger causality \\textbf{6/16} (37.5\\%), and Toda--Yamamoto Granger \\textbf{5/16} (31.3\\%; moderate supplementary, \\S\\ref{sec:ty_limitation}).\nMethod choice alone swings significance from \\textbf{100\\% to 37.5\\%} among the primary methods: 50--57\\% of pairs classified as significant under one method flip to non-significant under another.\nThe spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is at least \\textbf{62.5\\%} across the primary methods.\nTable~\\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.\n\n\\paragraph{First-differencing diagnostic.}\nA single preprocessing decision can eliminate an entire analysis channel.\nFor canary$\\to$diversity pairs at $\\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.\nFor canary$\\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \\textbf{zero} significant pairs ($F{\\approx}0$, $p{=}0.99$; Figure~\\ref{fig:differencing_dmax}a).\nThe apparent canary$\\to$perplexity relationship is entirely an artifact of co-trending.\nNotably, at $\\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \\emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.\n\n\\paragraph{Augmentation order sensitivity.}\nToda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\\max}$ (Figure~\\ref{fig:differencing_dmax}b).\nAfter correcting the statsmodels API incompatibility (\\S\\ref{sec:ty_limitation}), TY achieves moderate detection (3--4/8 at $\\alpha{\\geq}0.50$) at the default $d_{\\max}{=}1$; however, the qualitative finding that this single hyperparameter can swing conclusions between near-universal significance and near-universal non-significance remains, consistent with known properties of the Toda--Yamamoto procedure~\\cite{toda1995statistical}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/differencing_dmax.pdf}\n\\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\\alpha{=}1.0$, 4~seeds). \\textbf{(a)}~First-differencing eliminates the canary$\\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\\to$diversity pairs retain significance after differencing (24/24$\\to$24/24). \\textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\\max}$; after correcting the implementation (\\S\\ref{sec:ty_limitation}), TY achieves moderate detection at the default $d_{\\max}{=}1$, but the qualitative sensitivity to this hyperparameter persists.}\n\\label{fig:differencing_dmax}\n\\end{figure}\n\n\\paragraph{Inter-method agreement.}\nCohen's $\\kappa$, averaged over all method pairs, is \\textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\\alpha{=}0.0$ through $\\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.\nCross-architecture validation on GPT-2-medium (12 canary$\\to$downstream pairs) yields Fleiss' $\\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.\nRestricting to three informative methods (excluding naive cross-correlation, which anchors the permissive extreme, and Toda--Yamamoto, which provides moderate supplementary signal) raises $\\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.\nTable~\\ref{tab:method_comparison} extends the analysis across contamination levels.\nDirection checking (D111) itself constitutes a sensitivity dimension beyond the five statistical methods: restricting to forward-direction associations inverts naive cross-correlation's profile from uniformly high (${\\approx}100\\%$ undirected) to regime-dependent, revealing that much of its apparent signal was reverse-directional.\nAt $\\alpha{=}0.0$ (null control), naive cross-correlation still finds \\textbf{75\\%} (6/8) of forward-direction pairs significant---lower than the undirected 100\\%, but still a substantial FPR.\nPermutation Granger correctly finds 0\\%, achieving perfect null-control specificity.\nAt $\\alpha{=}0.50$ (fp32), permutation Granger finds 75\\% (6/8), while naive finds 37.5\\% (Figure~\\ref{fig:consensus_heatmap}; Table~\\ref{tab:method_comparison}).\n\n\\paragraph{Method$\\times$regime interaction.}\nTable~\\ref{tab:method_comparison} reveals that direction checking reshapes the method hierarchy across contamination levels.\nAt $\\alpha{=}0.25$, naive cross-correlation drops to 12.5\\% while permutation Granger remains at 0\\%, narrowing the gap visible in undirected analysis.\nAt $\\alpha{\\geq}0.75$, naive rises to 87.5\\% while permutation Granger reaches 75\\%; both methods detect, but naive's persistent 75\\% null-control FPR means its high-$\\alpha$ detections cannot be distinguished from false positives without the consensus framework.\nThis regime-dependent reversal, combined with the block structure visible in Figure~\\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \\S\\ref{sec:regime}.\n\n\\paragraph{Why permutation Granger succeeds.}\nThe systematic comparison identifies PermG as the only method combining zero null-control FPR with consistent detection across all regimes where signal exists ($\\alpha{\\geq}0.50$).\nThree properties explain this outcome.\nFirst, the nonparametric permutation procedure inherently controls FPR by constructing the null distribution from the observed data rather than from distributional assumptions, making it robust to the non-stationarity that inflates false positives in correlation-based methods.\nSecond, Granger tests are directional by construction: they test whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history, naturally filtering the reverse-directional associations that inflate naive cross-correlation's FPR.\nThird, PermG does not require threshold calibration or augmentation order selection, avoiding the hyperparameter sensitivity observed in Toda--Yamamoto (Figure~\\ref{fig:differencing_dmax}b; \\S\\ref{sec:ty_limitation}) and the power limitations that reduce threshold onset to near-zero detection under $3\\sigma$ calibration (\\S\\ref{sec:threshold_limitation}).\nBy contrast, differenced cross-correlation retains 100\\% FDR significance in both forward \\emph{and} reverse directions at $\\alpha{=}0.75$, failing to distinguish genuine directional precedence from shared dynamics; and Toda--Yamamoto, while achieving moderate detection (3--4/8 at $\\alpha{\\geq}0.50$), remains sensitive to the augmentation order $d_{\\max}$ (\\S\\ref{sec:ty_limitation}).\nThese complementary failures, exposed through the MMCT evaluation framework, converge on a single recommendation: for short iterative training series ($T{\\leq}20$), permutation Granger causality should be the primary detection method.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/consensus_heatmap.pdf}\n\\caption{Method$\\times$regime consensus heatmap (Pythia-410M, fp32, 12 contamination levels, direction-checked). Each cell shows the forward-direction detection rate (\\% of 8 pairs reaching FDR significance) for five individual methods (top) and two consensus thresholds (bottom, separated by white line). Direction checking dramatically reshapes method profiles: naive cross-correlation drops from near-100\\% (undirected) to regime-dependent rates with persistent 75\\% null-control FPR. Permutation Granger achieves FPR${=}$0\\% in the blind zone (green dashed box) and detects only at $\\alpha{\\geq}0.50$. The onset boundary ($\\alpha{\\approx}0.45$--$0.50$) is where method divergence is sharpest (Pitfall~3). \\emph{Note: figure will be regenerated with D120 canonical data including corrected TY rates (\\S\\ref{sec:ty_limitation}).}}\n\\label{fig:consensus_heatmap}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Forward-direction FDR significance rates (\\%) for five lead-lag methods across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Direction checking reshapes method profiles: naive cross-correlation drops from near-100\\% (undirected) to regime-dependent rates (75\\% at the null, 12.5\\% at $\\alpha{=}0.25$, rising to 87.5\\% at $\\alpha{=}0.75$). Each cell reports the fraction of 8 validated canary$\\to$downstream pairs reaching BH-corrected significance ($q{=}0.05$) in the forward direction. $^\\dagger$Moderate supplementary method (\\S\\ref{sec:ty_limitation}); FPR$_\\text{null}$ pending (null condition not yet run through corrected pipeline). $^a$Seed-42 null-control rate under D105 $3\\sigma$ calibration pending; 3-seed range 12.5--37.5\\%.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr     & 75    & 12.5 & 37.5 & 87.5  & 0     & 75   \\\\\nDiff.\\ XCorr    & 0     & 37.5 & 87.5 & 75    & 75    & 0    \\\\\nThreshold ($3\\sigma$)$^a$ & ---   & 0    & 50   & 0     & 0     & ---  \\\\\nPerm.\\ Granger  & 0     & 0    & 75   & 75    & 75    & 0    \\\\\nToda--Yamamoto$^\\dagger$  & ---   & 0    & 37.5 & 37.5  & 50    & ---  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Regime-Dependent Detectability}\n\\label{sec:regime}\n\nBeyond method choice, the contamination level~$\\alpha$ determines whether a temporal lead exists to detect.\nWe present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.\n\n\\paragraph{Raw drift.}\nTable~\\ref{tab:drift_summary} shows that diversity collapse occurs at \\emph{all} contamination levels, not only under full synthetic replacement.\nDistinct-1 declines by 13.8\\% even at $\\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets).\nA single-seed observation at $\\alpha{=}0.10$ reveals a steep diversity cliff: distinct-1 drops by 39.6\\%, nearly matching the 3-seed mean at $\\alpha{=}0.25$ ($-40.3{\\pm}0.3\\%$); distinct-2 shows a comparable jump ($-56.4\\%$ vs.\\ $-56.4{\\pm}0.7\\%$ at $\\alpha{=}0.25$).\nToken entropy at $\\alpha{=}0.10$, however, differs from the null by less than 1 percentage point ($-5.3\\%$ vs.\\ $-4.6{\\pm}0.4\\%$), constituting a canary blind spot in which diversity has already collapsed but no canary metric responds.\nAt higher contamination, distinct-1 decline continues: $-37.1{\\pm}0.4\\%$ ($\\alpha{=}0.50$), $-32.3{\\pm}0.5\\%$ ($\\alpha{=}0.75$), and $-27.8{\\pm}1.6\\%$ ($\\alpha{=}1.0$).\nThe non-monotonic pattern (diversity declining \\emph{more} at moderate~$\\alpha$ than at extreme~$\\alpha$) is confirmed by 3-seed replication at $\\alpha{=}0.25$ (std${=}0.3\\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response profile of permutation Granger forward detection rate (Pythia-410M, fp32, 12 contamination levels, direction-checked).\nFour regimes emerge: blind spot ($\\alpha{\\leq}0.45$, 0/8), onset ($\\alpha{=}0.50$, 75\\%), synchronous collapse ($\\alpha{=}0.60$, 37.5\\%; orange diamond), and detection zone ($\\alpha{\\geq}0.75$, 62.5--75\\%).\nThe $\\alpha{=}0.60$ dip is dual-seed confirmed (s42: 3/8, s43: 0/8).\nPer-method comparison is in Figure~\\ref{fig:consensus_heatmap}.}\n\\label{fig:regime_map}\n\\end{figure}\n\n\\paragraph{Granger-precedence detectability.}\nDespite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\\ref{fig:regime_map}).\nPermutation Granger tests (first-differenced, BH-corrected) find 0/8 pairs FDR-significant from $\\alpha{=}0.00$ through $\\alpha{=}0.45$ (including $\\alpha{=}0.25$ where a faint single-pair signal appears at FDR $p{=}0.053$ but aggregate detection remains null, and $\\alpha{=}0.35$/$0.40$/$0.45$ which confirm PermG fwd${=}$0/8), \\textbf{6/8} at $\\alpha{=}0.50$ (2~fp32 seeds, consistent), \\textbf{3/8} and \\textbf{0/8} at $\\alpha{=}0.60$ (s42 and s43 respectively; dual-seed confirmed non-monotonic dip), and \\textbf{6/8} at $\\alpha{=}1.0$.\nAt $\\alpha{=}0.75$ (3~seeds), permutation Granger finds 20/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.\nUnder Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.\nWithin-$\\alpha$ multi-seed analysis at $\\alpha{=}1.0$ yields \\textbf{24/24} canary$\\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.\nPermutation Granger forward significance is the primary detection indicator (Figure~\\ref{fig:regime_map}): it reaches 6/8 at $\\alpha{=}0.50$, dips to 3/8 at $\\alpha{=}0.60$ (synchronous collapse zone; see below), and recovers to 5--6/8 at $\\alpha{\\geq}0.75$.\nThe onset boundary lies at $\\alpha{\\approx}0.45$--$0.50$: finer-grained probing at $\\alpha{=}0.35$, $0.40$, and $0.45$ yields PermG fwd${=}$0/8 at all three levels, extending the blind spot through $\\alpha{=}0.45$.\nA faint signal first appears at $\\alpha{=}0.25$ (best-pair FDR $p{=}0.053$) but does not translate to aggregate detection; reliable detection begins at $\\alpha{=}0.50$ (6/8, 2~seeds).\nThis sharp phase transition is consistent with theoretical expectations about signal-to-noise limits in short time series~\\cite{boettiger2012limits}.\nSensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\\ref{app:robustness}).\nCross-architecture validation on GPT-2-medium confirms this boundary: at $\\alpha{=}0.25$, at most 1/8 pairs reach $K{\\geq}3$ ($3\\sigma$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\\%$ vs.\\ Pythia $-4.7{\\pm}0.5\\%$), while at $\\alpha{=}1.0$ all 6 canary$\\to$diversity pairs reach significance (\\S\\ref{sec:discussion}).\nTable~\\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.\nAt $\\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\\geq}4/5$) and 7/8 at Tier~2 ($K{\\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\\alpha{=}0.25$ and $\\alpha{=}1.0$. Tier~3: $K{\\geq}4/5$ methods (or $K{\\geq}3$ of 4 effective methods; \\S\\ref{sec:threshold_limitation}); Tier~2: $K{\\geq}3/5$. Drift is generation~0$\\to$10. GPT-2-medium $\\alpha{=}0.25$: single seed (seed=42); Pythia $\\alpha{=}0.25$: 3-seed mean${\\pm}$std. The onset boundary ($\\alpha{\\approx}0.45$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}\n\\label{tab:cross_arch_regime}\n\\begin{tabular}{llcccccc}\n\\toprule\n$\\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\\ Granger & Tier~3 \\\\\n\\midrule\n0.25 & Pythia-410M  & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & 0/8 & 0/8 \\\\\n0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\\\\n\\midrule\n1.00 & Pythia-410M  & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & 6/8 & 6/8 \\\\\n1.00 & GPT-2-medium & \\multicolumn{6}{c}{(reported in \\S\\ref{sec:discussion}; 6/8 canary$\\to$downstream pairs at Tier~3)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Detectability at $\\alpha{=}0.50$ and the transition zone.}\nUnder fp32 precision, $\\alpha{=}0.50$ is reliably detected: permutation Granger finds 6/8 pairs FDR-significant across both seeds (Table~\\ref{tab:method_comparison}).\nThe transition from undetectable to reliably detectable occurs between $\\alpha{=}0.45$ and $\\alpha{=}0.50$: finer-grained probing confirms PermG fwd${=}$0/8 at $\\alpha{=}0.35$, $0.40$, and $0.45$, while $\\alpha{=}0.50$ achieves 6/8 (2~seeds).\nA faint single-pair signal first appears at $\\alpha{=}0.25$ (entropy$\\to$distinct-1: raw $p{=}0.007$, FDR-corrected $p{=}0.053$), but all aggregate indicators remain null through $\\alpha{=}0.45$, placing the onset boundary at $\\alpha{\\approx}0.45$--$0.50$.\nAt $\\alpha{=}0.50$, canary sensitivity remains metric-dependent: ECE achieves significance in both fp32 seeds, while token entropy remains below the FDR threshold ($p_{\\text{fdr}}{\\geq}0.086$), identifying ECE as the more sensitive canary near the onset boundary.\nFigure~\\ref{fig:consensus_heatmap} visualizes the method$\\times\\alpha$ interaction, revealing a block structure that separates correlation-based methods from causal methods as a function of regime.\n\n\\paragraph{Non-monotonic dose-response: the synchronous collapse zone.}\nDual-seed replication at $\\alpha{=}0.60$ reveals a non-monotonic dose-response in Granger detectability: PermG fwd drops to 3/8 (s42) and 0/8 (s43), below both $\\alpha{=}0.50$ (6/8, 2~seeds) and $\\alpha{=}0.75$ (5--6/8 per seed, 3~seeds).\nThis creates a four-regime structure in the dose-response profile: \\emph{blind spot} ($\\alpha{\\leq}0.45$, 0/8), \\emph{onset} ($\\alpha{\\approx}0.45$--$0.50$), \\emph{synchronous collapse} ($\\alpha{\\approx}0.60$, 0--3/8), and \\emph{detection zone} ($\\alpha{\\geq}0.75$, 5--8/8).\nThe dip is inconsistent with a monotonically increasing signal-to-noise model; we hypothesize that at $\\alpha{=}0.60$, canary and downstream metrics respond to contamination simultaneously rather than sequentially, destroying the temporal lead that Granger tests require (\\S\\ref{sec:discussion}).\nThe synchronous zone is mechanistically distinct from the blind spot: in the blind spot, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.\nToda--Yamamoto achieves moderate detection across this range (3--4/8 at $\\alpha{\\geq}0.50$; \\S\\ref{sec:ty_limitation}), with its detection at $\\alpha{=}0.60$ suggesting partial inter-method complementarity in the synchronous collapse zone where PermG drops to 0--3/8.\nThis non-monotonicity also implies that simple threshold-based triggers (such as the 15\\% entropy criterion in \\S\\ref{sec:intervention}) may outperform formal Granger tests at intermediate contamination levels.\n\n\n\\subsection{Case Study: Canary Prediction of Diversity Collapse}\n\\label{sec:case_study}\n\nHaving established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).\nWe scope this claim precisely: canary metrics predict \\emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.\n\n\\paragraph{Full synthetic replacement ($\\alpha{=}1.0$, 4 seeds).}\nToken entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \\S\\ref{sec:discussion}).\nCross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.\nFigure~\\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.\nPermutation Granger tests (first-differenced) confirm all canary$\\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\\ref{app:distinct3}).\nReverse-direction tests (downstream$\\to$canary) on WikiText-103 find \\textbf{0/24} FDR-significant (all $p{>}0.49$), establishing directional asymmetry in this domain.\\footnote{C4 exhibits domain-dependent directionality: at $\\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling (\\S\\ref{sec:discussion}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\n\\caption{Metric trajectories across 10 generations at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}\n\\label{fig:metric_trajectory}\n\\end{figure}\n\n\\paragraph{High contamination ($\\alpha{=}0.75$, 3 seeds).}\nDirectional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 20/24 forward pairs FDR-significant, 0/24 reverse).\nHowever, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\\alpha{=}0.75$ squarely in the transitional detection regime.\nDifferenced cross-correlation finds 8/8 pairs significant in \\emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\\S\\ref{sec:pitfalls}).\n\n\\paragraph{ECE as a conditional secondary canary.}\nECE's forward consensus matches token entropy (both achieve PermG\\_fwd 6/8 across all conditions), but the reverse profile diverges sharply.\nAcross 7 validated conditions at $\\alpha{=}1.0$ (3 architectures $\\times$ 2 scales $\\times$ 2 domains), token entropy reverse direction yields \\textbf{0/28} FDR-significant pairs (consistent with unidirectional forward causation at full synthetic replacement; domain-dependent bidirectionality emerges at lower $\\alpha$, \\S\\ref{sec:discussion}), while ECE reverse direction yields \\textbf{13/28} significant pairs, with 5/7 conditions containing at least one reverse-significant pair, all in the distinct$\\to$ECE direction.\nThis bidirectional coupling is the core reason ECE is classified as a secondary canary: ECE and diversity exhibit mutual feedback, and the interpretability of ECE's causal direction is correspondingly limited.\nThis result also instantiates Claim~3 (method sensitivity): when only forward significance is considered, the two canary types appear equivalent; incorporating reverse-direction tests separates them. The choice of analysis dimension alters the canary classification itself.\n\n\\paragraph{Failed canary candidates.}\nNot all metrics serve as canaries.\nEffective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.\nEffective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\\alpha{=}0.25$ it \\emph{increases} from 2.37 to 8.48 (+258\\%).\nThe GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.\nThis opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\\S\\ref{sec:discussion}).\n\n\\paragraph{Consensus filtering.}\nOf 16 canary$\\to$downstream pairs tested at $\\alpha{=}1.0$ (4 candidate canaries $\\times$ 4 downstream metrics), \\textbf{6 survive} the full consensus pipeline (PermG fwd ${\\geq}6/8$, $S{\\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\\ref{app:distinct3} bring the total to~6).\nThe 10 eliminated pairs comprise all canary$\\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).\nThe consensus framework reduces the naive 75\\% forward-direction FPR to 0\\%, matching the most conservative individual methods (Figure~\\ref{fig:consensus_workflow}).\n\n\n\\subsection{Consensus Framework Validation}\n\\label{sec:consensus_validation}\n\nWe validate the consensus framework's calibration using built-in experimental controls.\n\n\\paragraph{False positive rate.}\nAt $\\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.\nIndividual-method forward-direction FPR ranges from \\textbf{75\\%} (naive cross-correlation: 6/8) through 37.5\\% (threshold) down to \\textbf{0\\%} (permutation Granger and differenced cross-correlation); Toda--Yamamoto's null-control FPR has not yet been evaluated through the corrected pipeline (\\S\\ref{sec:ty_limitation}).\nThe multi-method consensus at $K{\\geq}3$ ($3\\sigma$) achieves \\textbf{FPR${=}$0\\%} (0/24 pairs, three independent seeds), matching the best individual method (permutation Granger) while providing a formal benchmark for method reliability (Table~\\ref{tab:fpr_fnr}).\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\\geq}3\\times$ the $\\alpha{=}0.0$ baseline (entropy $11.93\\times$, ECE $73.12\\times$) and canary onset strictly preceding downstream onset by ${\\geq}1$ generation (\\S\\ref{sec:calibration}).\nFNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\\geq}3/4$, $S{\\geq}3/4$, all~6 are recovered (\\textbf{FNR${=}$0\\%}).\nToda--Yamamoto's individual FNR is 50\\% (4/8 detected at $\\alpha{=}1.0$, seed~42), consistent with its moderate supplementary classification (\\S\\ref{sec:ty_limitation}).\nBoth FPR and FNR are validated on the joint method${\\times}$seed dimension (FPR: 3~seeds at $\\alpha{=}0.0$; FNR: 4~seeds at $\\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\\geq}3$).\nTable~\\ref{tab:fpr_fnr} reports the calibration results.\nTable~\\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\\alpha$ including the null control, while permutation Granger achieves correct verdicts at all levels with zero FPR.\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-method inference errors across contamination levels.\nEach cell shows the verdict (significant or not) based on multi-seed majority ($\\geq$2/3 seeds with $\\geq$4/8 pairs significant).\n\\checkmark\\ = correct, \\textcolor{red}{FP} = false positive, \\textcolor{blue}{FN} = false negative, $\\circ$ = ambiguous ground truth (either verdict plausible).\nNaive XCorr produces false positives at \\emph{every} $\\alpha$ including the null control. Permutation Granger achieves correct verdicts at all levels with zero FPR. $^\\dagger$Rows marked pending have cross-script inconsistencies under audit.}\n\\label{tab:single-method-errors}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textit{No signal}} & \\textit{Ambiguous} & \\multicolumn{2}{c}{\\textit{Causal signal}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-4} \\cmidrule(lr){5-6}\nMethod & $\\alpha{=}0.00$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.00$ \\\\\n\\midrule\nNaive XCorr\n  & \\textcolor{red}{FP}{\\scriptsize\\ 8,7,8}\n  & \\textcolor{red}{FP}{\\scriptsize\\ 8,8}\n  & $\\circ${\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8} \\\\\nDiff XCorr (FDR)$^\\dagger$\n  & --- & --- & --- & --- & --- \\\\\nThreshold Onset$^\\dagger$\n  & --- & --- & --- & --- & --- \\\\\nPerm Granger (FDR)\n  & \\checkmark{\\scriptsize\\ 0,0,0}\n  & \\checkmark{\\scriptsize\\ 0,0}\n  & $\\circ${\\scriptsize\\ 0,6,3}\n  & \\checkmark{\\scriptsize\\ 8,5,6}\n  & \\checkmark{\\scriptsize\\ 6,6,6} \\\\\nTY Granger$^\\dagger$\n  & --- & --- & --- & --- & --- \\\\\n\\midrule\n\\textbf{Consensus ($K{\\geq}3$)}$^\\dagger$\n  & --- & --- & --- & --- & --- \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\\\\n\\multicolumn{6}{l}{\\footnotesize Seeds: $\\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\\alpha{=}0.25$: 43, 44; $\\alpha{=}1.00$: 42, 43, 45.} \\\\\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Bootstrap power analysis.}\nTo quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\\alpha{=}1.0$).\nPermutation Granger achieves power${=}1.0$ on genuine pairs (canary$\\to$diversity) and power${=}0.0$ on spurious pairs (canary$\\to$perplexity), providing clean separation.\nToda--Yamamoto achieves power${=}0.50$ on genuine pairs (4/8 detected at $\\alpha{=}1.0$), consistent with its moderate supplementary classification (\\S\\ref{sec:ty_limitation}).\nWe note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\\beta{=}0.3$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\\geq}3$ ($3\\sigma$, excluding threshold onset; \\S\\ref{sec:threshold_limitation}) achieves FPR${=}$0\\% and FNR${=}$0\\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration of any single method. FPR: $\\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds). $^\\dagger$Moderate supplementary method (\\S\\ref{sec:ty_limitation}); FPR pending (null condition not yet run through corrected pipeline); FNR from single-seed $\\alpha{=}1.0$ (4/8 detected).}\n\\label{tab:fpr_fnr}\n\\begin{tabular}{lcc}\n\\toprule\nCriterion & FPR ($\\alpha{=}0.0$) & FNR ($\\alpha{=}1.0$) \\\\\n\\midrule\nNaive XCorr              & 100\\%              & 0\\%  \\\\\nDifferenced XCorr        & 37.5\\%             & 0\\%  \\\\\nThreshold Onset          & 20.8\\% (12.5--37.5) & 0\\%  \\\\\nPermutation Granger      & 0\\%                & 0\\%  \\\\\nToda--Yamamoto$^\\dagger$  & ---                & 50\\%   \\\\\n\\midrule\nConsensus ($K{\\geq}3$, $3\\sigma$)      & 0\\%    & 0\\%  \\\\\nConsensus ($K{\\geq}3$, $S{\\geq}3/4$)   & 0\\%    & 0\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}\n\\label{sec:generalization}\n\nThe methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\nTo test whether these findings transfer, we evaluate the lead-lag pattern along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\nAll conditions use $\\alpha{=}1.0$; architecture conditions use a single seed, while scale and domain conditions use two seeds (s42, s43) to assess replicability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture lead-lag detectability ($\\alpha{=}1.0$, D105 unified pipeline, $3\\sigma$ calibration, M035 direction-corrected).\nPermG~fwd: permutation Granger forward-direction FDR-significant pairs (out of 8).\n$K{\\geq}3$: pairs where ${\\geq}3$ of 5 methods reach FDR significance (direction-checked, $3\\sigma$).\nPermG~fwd ${\\geq}6/8$ in 12/14 confirmed conditions; $K{\\geq}3$ ${\\geq}6/8$ in 10/14 (11/14 pending Padding-410M audit).\nExceptions: Pythia-1.4B (s42: 1/8$^\\dagger$, s43: 3/8) and SmolLM3-3B (3/8$^\\ddagger$).\nRows marked ``---'' are running experiments; final values will be filled without format changes.}\n\\label{tab:generalization}\n\\begin{tabular}{lrclcc}\n\\toprule\nModel & Params & Seed & Domain & PermG (fwd) & $K{\\geq}3$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Baseline}} \\\\\nPythia-410M       & 410M & s42 & Wiki & 6/8            & 6/8            \\\\\nPythia-410M       & 410M & s43 & Wiki & 6/8            & 6/8            \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\emph{Scale}} \\\\\nPythia-1.4B       & 1.4B & s42 & Wiki & \\textbf{2/8}$^\\dagger$ & \\textbf{1/8}$^\\dagger$  \\\\\nPythia-1.4B       & 1.4B & s43 & Wiki & 6/8            & 3/8     \\\\\nPythia-6.9B       & 6.9B & s42 & Wiki & 7/8$^*$        & 6/8            \\\\\nPythia-6.9B       & 6.9B & s43 & Wiki & ---            & ---            \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\emph{Architecture}} \\\\\nGPT-2-medium      & 345M & s42 & Wiki & 6/8            & 6/8            \\\\\nGPT-2-medium      & 345M & s43 & Wiki & 6/8            & 6/8            \\\\\nOPT-1.3B          & 1.3B & s42 & Wiki & 6/8            & 6/8            \\\\\nOPT-1.3B          & 1.3B & s43 & Wiki & 6/8            & 6/8            \\\\\nQwen3.5-0.8B      & 0.8B & s42 & Wiki & 8/8            & 6/8            \\\\\nQwen3.5-0.8B      & 0.8B & s43 & Wiki & ---            & ---            \\\\\nSmolLM3-3B        & 3.0B & s42 & Wiki & \\textbf{3/8}$^\\ddagger$ & \\textbf{3/8}$^\\ddagger$ \\\\\nSmolLM3-3B        & 3.0B & s43 & Wiki & ---            & ---            \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\emph{Tokenization}} \\\\\nPadding-410M      & 410M & s42 & Wiki & 6/8            & 6/8$^{\\S}$     \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\emph{Domain}} \\\\\nPythia-1B         & 1.0B & s42 & C4   & 8/8            & 7/8            \\\\\nPythia-1B         & 1.0B & s43 & C4   & 7/8            & 6/8            \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Seed-sensitive: PermG s42 2/8, s43 6/8; $K{\\geq}3$ s42 1/8, s43 3/8. Likely stochastic instability at this scale (\\S\\ref{sec:discussion}).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Canary metric splitting: only ECE$\\to$downstream pairs detected (3/4); entropy$\\to$downstream 0/4 (\\S\\ref{sec:smollm3}).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^*$bf16 precision (model exceeds single-GPU fp32 capacity).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^{\\S}$Padding-410M $K{\\geq}3$ pending supplementary audit (expected stable at 6/8).} \\\\\n\\multicolumn{6}{l}{\\footnotesize Full method-level breakdown ($K{\\geq}4$) in Appendix~\\ref{app:cross_arch}.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-condition robustness.}\nTable~\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern is robust across 14 confirmed conditions (3 pending) spanning six model families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B, and two training domains (WikiText-103, C4).\nPermutation Granger forward significance reaches ${\\geq}6/8$ in 12 of 14 conditions (85.7\\%), with two exceptions: Pythia-1.4B seed~42 (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\\to$downstream pairs are detected (see below).\n$K{\\geq}3$ multi-method consensus reaches ${\\geq}6/8$ in 10 of 14 conditions (11/14 pending Padding-410M audit), with exceptions Pythia-1.4B (s42: 1/8, s43: 3/8) and SmolLM3-3B (3/8).\nThe concordance between PermG and $K{\\geq}3$ confirms that multi-method consensus is robust across architectures.\nWith threshold onset power-limited and Toda--Yamamoto providing moderate supplementary signal (3--4/8 at $\\alpha{\\geq}0.50$; \\S\\ref{sec:ty_limitation}), $K{\\geq}3$ draws on four contributing methods---a stronger standard than simple majority (\\S\\ref{sec:consensus}).\n\n\\paragraph{Scale generalization.}\nScaling from 410M to 6.9B parameters confirms that the lead-lag pattern persists across a $17\\times$ parameter range.\nPythia-6.9B achieves PermG fwd~7/8 (bf16), the strongest single-seed detection.\nWithin the Pythia family, 1.4B shows seed dependence: s42 yields only 2/8 (the sole outlier across all conditions), while s43 recovers to 6/8.\nQwen3.5-0.8B (PermG~fwd~8/8) extends the finding beyond the Pythia/GPT-2/OPT decoder-only family to an independently trained architecture with a different tokenizer.\n\n\\paragraph{Domain generalization.}\nReplacing WikiText-103 with C4 yields the strongest forward detection: Pythia-1B achieves PermG~fwd~8/8 in both seeds at $\\alpha{=}1.0$, confirming that the lead-lag pattern is not an artifact of narrow topical distribution.\nHowever, directional asymmetry does not transfer fully across domains.\nAt $\\alpha{=}0.50$ (Pythia-410M, C4, s42 fp32), PermG reverse reaches 7/8 (compared to 0/8 in all WikiText conditions), indicating near-symmetric bidirectional coupling between canary and downstream metrics.\nThis domain-dependent directionality suggests that the unidirectional forward causation observed in WikiText may partly reflect domain-specific dynamics rather than a universal property of collapse; implications are discussed in \\S\\ref{sec:discussion}.\n\n\\paragraph{Canary metric sensitivity: the SmolLM3-3B case.}\n\\label{sec:smollm3}\nSmolLM3-3B (PermG fwd 3/8) reveals that canary metric choice is itself a dimension of method sensitivity.\nDecomposing by canary type: ECE$\\to$downstream achieves 3/4 significant pairs, while token entropy$\\to$downstream achieves 0/4.\nThe root cause is that SmolLM3's token entropy exhibits non-monotonic oscillations across generations, violating the monotonic decline pattern that Granger tests exploit; ECE, by contrast, maintains its monotonic upward trajectory.\nMulti-method consensus confirms the severity: entropy pairs activate only via naive and differenced cross-correlation (per-pair $K{=}2$), ECE pairs activate only via differenced cross-correlation and permutation Granger (per-pair $K{=}2$), and no pair exceeds two-method agreement---illustrating that even within a single architecture, the method panel fragments along canary metric boundaries.\nThis architecture-dependent canary sensitivity complements the finding that effective rank direction is model-dependent (\\S\\ref{sec:case_study}): no single canary metric is universally optimal across all architectures, enriching Claim~3 by adding canary metric selection as a further source of analytic variability.\n\n\\subsection{Canary-Based Early Intervention}\n\\label{sec:intervention}\n\nTo test whether the lead-lag relationship translates into practical utility, we implement a predictive cessation protocol: training with synthetic data ($\\alpha{=}1.0$) continues until token entropy drops ${>}15\\%$ relative to generation~0, at which point $\\alpha$ is switched to $0.0$ (pure real data).\nWe compare against a reactive baseline that triggers only when distinct-1 drops ${>}10\\%$---a downstream metric that, by the lead-lag hypothesis, should respond later.\n\n\\paragraph{Pythia-410M.}\nThe predictive trigger fires at generation~1 in both seed-precision pairs tested (s42 fp32: entropy $3.234{\\to}1.918$, ${\\downarrow}40.7\\%$; s43 bf16: $3.257{\\to}2.523$, ${\\downarrow}22.5\\%$).\nThe reactive baseline triggers one generation later (generation~2, distinct-1 ${\\downarrow}15.6\\%$).\nPredictive intervention reduces peak perplexity by 63\\% relative to reactive ($56.99$ vs.\\ $157.09$, s42 fp32) and achieves full recovery by generation~2 versus generation~4 for reactive.\nThe bf16 pair shows a milder perturbation (peak perplexity $24.65$ vs.\\ $56.99$) consistent with stochastic rounding regularization, but the structural pattern---generation~1 trigger, generation~2 recovery---is identical.\nBoth conditions converge to the $\\alpha{=}0.0$ baseline by generation~10.\n\n\\paragraph{Cross-scale validation: Pythia-1.4B.}\nPythia-1.4B (s42 fp32) replicates the 410M pattern: token entropy drops $51.9\\%$ at generation~1 ($2.946{\\to}1.418$), exceeding the 15\\% threshold, and recovers to $2.892$ by generation~2 ($98.2\\%$ of baseline).\nPerplexity spikes from $19.68$ to $65.37$ at the trigger generation and recovers to $17.44$ by generation~2 (stable at $17.60$ through generation~10).\nThe trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\\times$ scale gap (410M to 1.4B), confirming that the canary-based intervention mechanism is scale-independent: the 15\\% entropy threshold generalizes without recalibration across model sizes.",
      "numLines": 436,
      "startLine": 1,
      "totalLines": 436
    }
  }
}
```

</details>

---
