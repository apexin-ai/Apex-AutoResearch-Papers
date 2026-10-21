# paper writing analysis

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_paper_writing_analysis_20260519T224949.log`
- **Structured JSON:** [`6fbdb6d8fae7bf5304b6.json`](../../sessions/6f/6fbdb6d8fae7bf5304b6.json)

## Before a recorded user message

42 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
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
  "uuid": "d5c8a1dc-575f-477b-8b21-f3ca1b59207c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/memory/"
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
    "resetsAt": 1779248400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "53b6342f-d917-435c-997d-76f2539d809a",
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill file and the existing sections for style consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "59343fe0-f36f-499e-b6f6-4a60858139d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ecx3nLvdqqGorwtWFmmJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14558,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14558
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Read · `toolu_01WG66aeA4a49v4RiEgAPD1L`</summary>

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
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "fb0aa9ea-3cf2-4cb0-9eb1-0ed20582f8cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ecx3nLvdqqGorwtWFmmJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14558,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14558
      },
      "output_tokens": 9,
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

_source line 6 · 2026-05-19T22:49:59.867Z_

<details><summary>↩ Tool result · `toolu_01WG66aeA4a49v4RiEgAPD1L`</summary>

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
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "e8cceca8-4a83-4147-adf5-1ff06d13ce45",
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

<details open><summary>🔧 Tool call — Read · `toolu_019PSskvu585SrpNNgsYu5Cb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "2ec8692b-0b6c-4488-a3de-b2bdad3fd628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ecx3nLvdqqGorwtWFmmJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14558,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14558
      },
      "output_tokens": 9,
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

_source line 8 · 2026-05-19T22:50:00.809Z_

<details><summary>↩ Tool result · `toolu_019PSskvu585SrpNNgsYu5Cb`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 8) are applied to all linear layers. The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42); each variant requires approximately 6 hours on a single A100 GPU. Full hyperparameters are provided in Appendix~A.
7	
8	To isolate the contribution of gating, we evaluate four configurations: (1)~\textbf{ThreadGate}: LoRA + per-layer learned gates + NTP + GAR loss; (2)~\textbf{Uniform Gate}: LoRA + a single shared gate across all layers + NTP + GAR loss; (3)~\textbf{LoRA-only}: LoRA + NTP loss only, with no gates or auxiliary losses; (4)~\textbf{Base}: the pretrained model without any fine-tuning. Each configuration is evaluated under two teacher-forced protocols. \emph{IID evaluation} computes metrics on UltraChat text from the same distribution as training. \emph{Held-out evaluation} uses 50 non-overlapping conversations to test within-distribution generalization. We report three metrics: GAR-ours (attention to goal tokens at the last token of each assistant turn, as defined in \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (attention to goal tokens averaged across all response tokens, all layers, and all heads), and perplexity (PPL).
9	
10	\subsection{Main Results}
11	
12	Table~\ref{tab:four-way} presents the four-way ablation. The central finding is that all three fine-tuned variants converge to nearly identical performance across both evaluation settings. On held-out data, GAR-ours spans only 0.75 percentage points (pp) across ThreadGate (0.50), Uniform Gate (0.51), and LoRA-only (0.50), and PPL is identical at 2.78 for all three. This convergence replicates on IID evaluation, where GAR-ours is 0.49 for all three variants and PPL varies by at most 0.01. Neither per-layer gating (ThreadGate) nor shared gating (Uniform Gate) provides any measurable benefit over LoRA-only fine-tuning. These results hold without exception across every metric-split combination in Table~\ref{tab:four-way}.
13	
14	The Base model confirms that LoRA fine-tuning is the operative variable. GAR-ours increases from 0.01 (Base) to approximately 0.49 (all fine-tuned variants) under teacher-forced evaluation, a roughly 45-fold increase attributable entirely to LoRA adaptation rather than to the gating mechanism or auxiliary losses. PPL improves correspondingly from 4.23 to 2.63 on IID data, which confirms that NTP training functions normally across all configurations. The three-variant convergence holds across both metrics and both evaluation splits; overfitting cannot account for a pattern this consistent.
15	
16	GAR-Dongre remains uniformly low across all conditions (0.00 for Base, 0.01--0.02 for fine-tuned variants). This is consistent with the observation of \citet{dongre2026attention} that the original GAR definition, which averages over all response tokens across all layers and heads, captures a persistently diffuse attention signal. The contrast with GAR-ours reflects measurement granularity: GAR-ours isolates the last token of each assistant turn, where learned attention steering concentrates its effect, while GAR-Dongre dilutes the signal across all positions.
17	
18	The teacher-forced GAR-ours values of 0.49--0.51 stand in sharp contrast to autoregressive generation, where GAR-ours drops to 0.016 across all fine-tuned variants. This 30$\times$ gap between teacher-forced and model-generated evaluation is the central empirical finding of this paper. Under teacher-forcing, the model conditions on UltraChat reference text as the prefix for each response; under autoregressive generation, the prefix consists of the model's own prior outputs. The attention patterns optimized for the former distribution do not transfer to the latter, and the gating mechanism does nothing to bridge this gap. We defer the mechanistic analysis of this distribution shift to \S\ref{sec:analysis}.
19	
20	\begin{table*}[t]
21	\centering
22	\small
23	\caption{Four-way ablation on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All three fine-tuned variants converge to within 0.75\,pp on GAR-ours and 0\,pp on PPL (held-out). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}. No values are bolded because no configuration achieves a meaningful advantage.}
24	\label{tab:four-way}
25	\begin{tabular}{l ccc ccc}
26	\toprule
27	& \multicolumn{3}{c}{\textbf{IID Evaluation}} & \multicolumn{3}{c}{\textbf{Held-out Evaluation}} \\
28	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
29	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL \\
30	\midrule
31	Base          & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 \\
32	ThreadGate    & 0.49 & 0.02 & 2.63 & 0.50 & 0.02 & 2.78 \\
33	Uniform Gate  & 0.49 & 0.01 & 2.62 & 0.51 & 0.01 & 2.78 \\
34	LoRA-only     & 0.49 & 0.01 & 2.63 & 0.50 & 0.01 & 2.78 \\
35	\bottomrule
36	\end{tabular}
37	\end{table*}
38	
39	\subsection{Cross-Model Validation}
40	\label{sec:cross-model}
41	
42	To verify that the convergence pattern and the 30$\times$ training-inference gap are not specific to the Qwen architecture, we are conducting parallel experiments on Llama-3.1-8B-Instruct. Llama-3.1 differs from Qwen-2.5 in several architectural choices, including grouped-query attention with 8 KV heads and a distinct BPE tokenizer. These differences provide a meaningful test of generalization across model families. Results will be reported in the final version of this paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "f093ae8e-792f-473a-aa61-2d2a0bdd62dd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 8) are applied to all linear layers. The combined loss $\\mathcal{L} = \\mathcal{L}_\\text{NTP} + \\lambda_\\text{GAR}\\mathcal{L}_\\text{GAR} + \\lambda_\\text{div}\\mathcal{L}_\\text{div}$ uses $\\lambda_\\text{GAR} = \\lambda_\\text{div} = 1.0$ with MSE target $\\tau = 0.5$ (\\S\\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42); each variant requires approximately 6 hours on a single A100 GPU. Full hyperparameters are provided in Appendix~A.\n\nTo isolate the contribution of gating, we evaluate four configurations: (1)~\\textbf{ThreadGate}: LoRA + per-layer learned gates + NTP + GAR loss; (2)~\\textbf{Uniform Gate}: LoRA + a single shared gate across all layers + NTP + GAR loss; (3)~\\textbf{LoRA-only}: LoRA + NTP loss only, with no gates or auxiliary losses; (4)~\\textbf{Base}: the pretrained model without any fine-tuning. Each configuration is evaluated under two teacher-forced protocols. \\emph{IID evaluation} computes metrics on UltraChat text from the same distribution as training. \\emph{Held-out evaluation} uses 50 non-overlapping conversations to test within-distribution generalization. We report three metrics: GAR-ours (attention to goal tokens at the last token of each assistant turn, as defined in \\S\\ref{sec:background}), GAR-Dongre \\citep{dongre2026attention} (attention to goal tokens averaged across all response tokens, all layers, and all heads), and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:four-way} presents the four-way ablation. The central finding is that all three fine-tuned variants converge to nearly identical performance across both evaluation settings. On held-out data, GAR-ours spans only 0.75 percentage points (pp) across ThreadGate (0.50), Uniform Gate (0.51), and LoRA-only (0.50), and PPL is identical at 2.78 for all three. This convergence replicates on IID evaluation, where GAR-ours is 0.49 for all three variants and PPL varies by at most 0.01. Neither per-layer gating (ThreadGate) nor shared gating (Uniform Gate) provides any measurable benefit over LoRA-only fine-tuning. These results hold without exception across every metric-split combination in Table~\\ref{tab:four-way}.\n\nThe Base model confirms that LoRA fine-tuning is the operative variable. GAR-ours increases from 0.01 (Base) to approximately 0.49 (all fine-tuned variants) under teacher-forced evaluation, a roughly 45-fold increase attributable entirely to LoRA adaptation rather than to the gating mechanism or auxiliary losses. PPL improves correspondingly from 4.23 to 2.63 on IID data, which confirms that NTP training functions normally across all configurations. The three-variant convergence holds across both metrics and both evaluation splits; overfitting cannot account for a pattern this consistent.\n\nGAR-Dongre remains uniformly low across all conditions (0.00 for Base, 0.01--0.02 for fine-tuned variants). This is consistent with the observation of \\citet{dongre2026attention} that the original GAR definition, which averages over all response tokens across all layers and heads, captures a persistently diffuse attention signal. The contrast with GAR-ours reflects measurement granularity: GAR-ours isolates the last token of each assistant turn, where learned attention steering concentrates its effect, while GAR-Dongre dilutes the signal across all positions.\n\nThe teacher-forced GAR-ours values of 0.49--0.51 stand in sharp contrast to autoregressive generation, where GAR-ours drops to 0.016 across all fine-tuned variants. This 30$\\times$ gap between teacher-forced and model-generated evaluation is the central empirical finding of this paper. Under teacher-forcing, the model conditions on UltraChat reference text as the prefix for each response; under autoregressive generation, the prefix consists of the model's own prior outputs. The attention patterns optimized for the former distribution do not transfer to the latter, and the gating mechanism does nothing to bridge this gap. We defer the mechanistic analysis of this distribution shift to \\S\\ref{sec:analysis}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Four-way ablation on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All three fine-tuned variants converge to within 0.75\\,pp on GAR-ours and 0\\,pp on PPL (held-out). GAR-O = GAR-ours; GAR-D = GAR-Dongre \\citep{dongre2026attention}. No values are bolded because no configuration achieves a meaningful advantage.}\n\\label{tab:four-way}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{IID Evaluation}} & \\multicolumn{3}{c}{\\textbf{Held-out Evaluation}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL \\\\\n\\midrule\nBase          & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 \\\\\nThreadGate    & 0.49 & 0.02 & 2.63 & 0.50 & 0.02 & 2.78 \\\\\nUniform Gate  & 0.49 & 0.01 & 2.62 & 0.51 & 0.01 & 2.78 \\\\\nLoRA-only     & 0.49 & 0.01 & 2.63 & 0.50 & 0.01 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Cross-Model Validation}\n\\label{sec:cross-model}\n\nTo verify that the convergence pattern and the 30$\\times$ training-inference gap are not specific to the Qwen architecture, we are conducting parallel experiments on Llama-3.1-8B-Instruct. Llama-3.1 differs from Qwen-2.5 in several architectural choices, including grouped-query attention with 8 KV heads and a distinct BPE tokenizer. These differences provide a meaningful test of generalization across model families. Results will be reported in the final version of this paper.",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_012FDzF13pwvhTmwnVPLUoxh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "b0d849f4-5821-4c0a-8e4c-39e05bc5da42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ecx3nLvdqqGorwtWFmmJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14558,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14558
      },
      "output_tokens": 9,
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

_source line 10 · 2026-05-19T22:50:00.944Z_

<details><summary>↩ Tool result · `toolu_012FDzF13pwvhTmwnVPLUoxh`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{ThreadGate Architecture}
4	
5	ThreadGate adds a learnable scalar gate to each transformer layer, following the ReZero residual scaling principle \citep{bachlechner2021rezero}. For a model with $L$ layers, the gated residual update at layer $l$ is
6	\begin{equation}
7	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
8	\end{equation}
9	where $f_l$ denotes the sublayer computation (self-attention or feed-forward network) and $g_l = \sigma(b_l)$ is a sigmoid gate parameterized by a single learnable scalar $b_l$. When $g_l \to 0$, the sublayer output is fully suppressed and the layer reduces to an identity mapping; when $g_l \to 1$, the full sublayer output passes through the residual stream. Each of the 28 transformer layers in Qwen-2.5-7B-Instruct receives its own independent gate, so the model learns a per-layer gating profile over the course of training.
10	
11	The choice of initialization is critical. ReZero initializes its scalar multiplier at zero, which is appropriate for training from scratch because the network begins as an identity function and gradually learns to activate each layer. For a pretrained model, zero initialization would immediately destroy the learned representations across all layers. We instead set $b_l = 1.5$, which yields $\sigma(1.5) \approx 0.82$ and preserves most of the pretrained computation at the start of fine-tuning. To ensure the gates can adapt quickly despite their small parameter count, we apply a learning rate multiplier of 10 to all gate parameters relative to the base learning rate.
12	
13	\subsection{Training Objective}\label{sec:loss}
14	
15	The training objective combines three terms:
16	\begin{equation}
17	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
18	\end{equation}
19	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction cross-entropy loss. The two auxiliary losses target the gating mechanism directly.
20	
21	The Goal Attention Ratio (GAR) loss encourages the model to maintain a target level of attention to goal-relevant tokens. We define it as
22	\begin{equation}
23	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR}, \tau),
24	\end{equation}
25	where $\tau = 0.5$ is the target ratio. GAR is computed under teacher-forced context and measured only at the last token position of each assistant turn (the GAR-ours variant defined in \S\ref{sec:background}), following the observation of \citet{dongre2026attention} that attention to goal tokens is most informative at turn boundaries. This loss steers the attention distribution toward a balanced allocation between goal tokens and other context.
26	
27	The gate diversity loss prevents all gates from collapsing to a single value:
28	\begin{equation}
29	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
30	\end{equation}
31	where $\mathbf{g} = [g_1, \ldots, g_L]$ is the vector of gate values across all layers and $\sigma_\text{min}$ is a minimum standard deviation threshold. Without this term, the gates can converge to a uniform value across layers, which collapses the per-layer conditioning to a single global scalar and eliminates any advantage over a shared gate. Both auxiliary loss weights are set to $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$.
32	
33	The final loss formulation emerged from seven design iterations (v1 through v7) that explored cumulative, maximization, smooth saturation, and MSE-based objectives. The MSE target combined with gate diversity was the only formulation that converged stably; other variants either diverged or drove all gates to the same value. A detailed comparison of all loss variants is provided in Appendix~B.
34	
35	\subsection{Four-Way Ablation Design}
36	
37	We evaluate four configurations that systematically isolate the contribution of each component. \textbf{ThreadGate} is the full system: LoRA adapters applied to all linear layers, per-layer sigmoid gates, and the complete three-term loss. \textbf{Uniform Gate} replaces the 28 independent gates with a single shared gate applied identically across all layers, while retaining LoRA and the same loss. \textbf{LoRA-only} removes gating entirely by fixing all gates at 1.0 and training with $\mathcal{L}_\text{NTP}$ alone, without any auxiliary losses. \textbf{Base} is the pretrained Qwen-2.5-7B-Instruct model evaluated without any fine-tuning.
38	
39	This factorial structure supports three targeted comparisons. ThreadGate versus Uniform Gate isolates whether per-layer conditioning provides an advantage over a single shared gate. ThreadGate versus LoRA-only isolates the combined effect of the gating mechanism and auxiliary losses. LoRA-only versus Base isolates the effect of fine-tuning itself, independent of any gating intervention. All four variants share the same training data, LoRA configuration, optimizer settings, and random seed; the only differences are the presence and type of gating. Full hyperparameters are provided in Appendix~A.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "72d66ee2-5f0b-4e62-bbe1-daacc820d660",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{ThreadGate Architecture}\n\nThreadGate adds a learnable scalar gate to each transformer layer, following the ReZero residual scaling principle \\citep{bachlechner2021rezero}. For a model with $L$ layers, the gated residual update at layer $l$ is\n\\begin{equation}\n  x_{l+1} = x_l + g_l \\cdot f_l(x_l),\n\\end{equation}\nwhere $f_l$ denotes the sublayer computation (self-attention or feed-forward network) and $g_l = \\sigma(b_l)$ is a sigmoid gate parameterized by a single learnable scalar $b_l$. When $g_l \\to 0$, the sublayer output is fully suppressed and the layer reduces to an identity mapping; when $g_l \\to 1$, the full sublayer output passes through the residual stream. Each of the 28 transformer layers in Qwen-2.5-7B-Instruct receives its own independent gate, so the model learns a per-layer gating profile over the course of training.\n\nThe choice of initialization is critical. ReZero initializes its scalar multiplier at zero, which is appropriate for training from scratch because the network begins as an identity function and gradually learns to activate each layer. For a pretrained model, zero initialization would immediately destroy the learned representations across all layers. We instead set $b_l = 1.5$, which yields $\\sigma(1.5) \\approx 0.82$ and preserves most of the pretrained computation at the start of fine-tuning. To ensure the gates can adapt quickly despite their small parameter count, we apply a learning rate multiplier of 10 to all gate parameters relative to the base learning rate.\n\n\\subsection{Training Objective}\\label{sec:loss}\n\nThe training objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_\\text{NTP} + \\lambda_\\text{GAR}\\,\\mathcal{L}_\\text{GAR} + \\lambda_\\text{div}\\,\\mathcal{L}_\\text{div}.\n\\end{equation}\n$\\mathcal{L}_\\text{NTP}$ is the standard next-token prediction cross-entropy loss. The two auxiliary losses target the gating mechanism directly.\n\nThe Goal Attention Ratio (GAR) loss encourages the model to maintain a target level of attention to goal-relevant tokens. We define it as\n\\begin{equation}\n  \\mathcal{L}_\\text{GAR} = \\text{MSE}(\\text{GAR}, \\tau),\n\\end{equation}\nwhere $\\tau = 0.5$ is the target ratio. GAR is computed under teacher-forced context and measured only at the last token position of each assistant turn (the GAR-ours variant defined in \\S\\ref{sec:background}), following the observation of \\citet{dongre2026attention} that attention to goal tokens is most informative at turn boundaries. This loss steers the attention distribution toward a balanced allocation between goal tokens and other context.\n\nThe gate diversity loss prevents all gates from collapsing to a single value:\n\\begin{equation}\n  \\mathcal{L}_\\text{div} = \\text{ReLU}(\\sigma_\\text{min} - \\text{std}(\\mathbf{g})),\n\\end{equation}\nwhere $\\mathbf{g} = [g_1, \\ldots, g_L]$ is the vector of gate values across all layers and $\\sigma_\\text{min}$ is a minimum standard deviation threshold. Without this term, the gates can converge to a uniform value across layers, which collapses the per-layer conditioning to a single global scalar and eliminates any advantage over a shared gate. Both auxiliary loss weights are set to $\\lambda_\\text{GAR} = \\lambda_\\text{div} = 1.0$.\n\nThe final loss formulation emerged from seven design iterations (v1 through v7) that explored cumulative, maximization, smooth saturation, and MSE-based objectives. The MSE target combined with gate diversity was the only formulation that converged stably; other variants either diverged or drove all gates to the same value. A detailed comparison of all loss variants is provided in Appendix~B.\n\n\\subsection{Four-Way Ablation Design}\n\nWe evaluate four configurations that systematically isolate the contribution of each component. \\textbf{ThreadGate} is the full system: LoRA adapters applied to all linear layers, per-layer sigmoid gates, and the complete three-term loss. \\textbf{Uniform Gate} replaces the 28 independent gates with a single shared gate applied identically across all layers, while retaining LoRA and the same loss. \\textbf{LoRA-only} removes gating entirely by fixing all gates at 1.0 and training with $\\mathcal{L}_\\text{NTP}$ alone, without any auxiliary losses. \\textbf{Base} is the pretrained Qwen-2.5-7B-Instruct model evaluated without any fine-tuning.\n\nThis factorial structure supports three targeted comparisons. ThreadGate versus Uniform Gate isolates whether per-layer conditioning provides an advantage over a single shared gate. ThreadGate versus LoRA-only isolates the combined effect of the gating mechanism and auxiliary losses. LoRA-only versus Base isolates the effect of fine-tuning itself, independent of any gating intervention. All four variants share the same training data, LoRA configuration, optimizer settings, and random seed; the only differences are the presence and type of gating. Full hyperparameters are provided in Appendix~A.",
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

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check if there's an existing analysis.tex file, and look at the paper directory structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "df280efd-0f0b-44bd-a525-46fbbfde5442",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRFwu81JBwa43saRxf2T4X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9165,
      "cache_read_input_tokens": 26005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9165
      },
      "output_tokens": 9,
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

Let me check the paper directory and any existing analysis file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "98389e49-d259-4c28-9da4-b1774d6f3892",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRFwu81JBwa43saRxf2T4X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9165,
      "cache_read_input_tokens": 26005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9165
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Glob · `toolu_0115hfgGyjrePdo1B22JFjKZ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "ccb730ac-aea3-416f-846d-d9add0f8d861",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRFwu81JBwa43saRxf2T4X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9165,
      "cache_read_input_tokens": 26005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9165
      },
      "output_tokens": 9,
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

_source line 14 · 2026-05-19T22:50:06.051Z_

<details><summary>↩ Tool result · `toolu_0115hfgGyjrePdo1B22JFjKZ`</summary>

```text
paper/main.tex
paper/sections/experiments.tex
paper/sections/method.tex
paper/sections/background.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "49115946-71b5-4094-90df-95b314512c76",
  "tool_use_result": {
    "filenames": [
      "paper/main.tex",
      "paper/sections/experiments.tex",
      "paper/sections/method.tex",
      "paper/sections/background.tex"
    ],
    "durationMs": 9,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01QSZM61rxxytvqNkKvJbEjd`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/",
  "description": "List sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "f2533919-8e5d-4366-bec9-1754eba6d4c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRFwu81JBwa43saRxf2T4X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9165,
      "cache_read_input_tokens": 26005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9165
      },
      "output_tokens": 9,
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

_source line 16 · 2026-05-19T22:50:06.559Z_

<details><summary>↩ Tool result · `toolu_01QSZM61rxxytvqNkKvJbEjd`</summary>

```text
background.tex
experiments.tex
method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "e4408966-18a5-4eb8-944c-b5eabf4f16e1",
  "tool_use_result": {
    "stdout": "background.tex\nexperiments.tex\nmethod.tex",
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
Let me also check the main.tex to see how sections are included and what labels/figure environments are already defined.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "1e42da0a-d0fe-473b-b625-56c02d53e133",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5KACLgxEBryVg8U9PvJgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 35170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
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

Let me check main.tex for figure definitions and how sections are included.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "237b87bb-b045-4176-8038-b25a2265f310",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5KACLgxEBryVg8U9PvJgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 35170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
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

<details open><summary>🔧 Tool call — Read · `toolu_01FqmtGwrnvaZi8inMx1Hcdm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "6210d7e5-1956-4dcf-8c30-99000db1f4a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5KACLgxEBryVg8U9PvJgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 35170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
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

_source line 20 · 2026-05-19T22:50:10.172Z_

<details><summary>↩ Tool result · `toolu_01FqmtGwrnvaZi8inMx1Hcdm`</summary>

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
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	
18	\graphicspath{{../figures/paper/}}
19	
20	\title{Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/background}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/analysis}
34	\input{sections/discussion}
35	\input{sections/conclusion}
36	\input{sections/limitations}
37	
38	\bibliographystyle{acl_natbib}
39	\bibliography{references}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "119955d1-88f4-43ee-aa9b-e87db5ed3d18",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{subcaption}\n\n\\graphicspath{{../figures/paper/}}\n\n\\title{Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation:\\\\A Mechanistic Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/background}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/analysis}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\\input{sections/limitations}\n\n\\bibliographystyle{acl_natbib}\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the paper structure, style, and conventions. Let me also quickly check if there are existing figure files and labels defined elsewhere (especially for fig:training-pcgrad and fig:gate-shift).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "e610f11b-a027-4731-8947-ca06fc23c291",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2TdnTpRnNGFt9iGnE1ySv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 35511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

_source line 22_

Let me check for existing figure label definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "f2f79fff-5291-42bb-aa42-57338b4ef0e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2TdnTpRnNGFt9iGnE1ySv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 35511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

_source line 23_

<details open><summary>🔧 Tool call — Grep · `toolu_01YEFHaiiq6RBZhdfiifqwCF`</summary>

```json
{
  "pattern": "fig:training-pcgrad|fig:gate-shift",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
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
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "96dbddaa-0025-4235-a367-b44f9d688bd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2TdnTpRnNGFt9iGnE1ySv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 35511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

_source line 24 · 2026-05-19T22:50:14.963Z_

<details><summary>↩ Tool result · `toolu_01YEFHaiiq6RBZhdfiifqwCF`</summary>

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
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "9f92d258-3e6e-4270-8c47-a50827984c2b",
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

<details open><summary>🔧 Tool call — Read · `toolu_01QF54GzLhgvm8iJ5sggEmqU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "41fcd8e8-a69e-4036-b20c-195f1ab690cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2TdnTpRnNGFt9iGnE1ySv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 35511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

_source line 26 · 2026-05-19T22:50:15.040Z_

<details><summary>↩ Tool result · `toolu_01QF54GzLhgvm8iJ5sggEmqU`</summary>

```text
1	\section{Background}\label{sec:background}
2	
3	\paragraph{Goal Attention Ratio.}
4	Multi-turn instruction-following models receive a system prompt that specifies the task objective. We denote the token subsequence corresponding to the task specification within this system prompt as the \emph{goal tokens} $\mathcal{G}$, excluding formatting markers and role tags. \citet{dongre2026attention} introduced the Goal Attention Ratio (GAR) to quantify how much attention a model allocates to these goal tokens during response generation. Given a model with $L$ layers and $H$ attention heads, GAR at conversation turn $\tau$ is
5	\begin{equation}\label{eq:gar}
6	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
7	\end{equation}
8	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$. This definition averages attention to goal tokens over all response positions, all layers, and all heads.
9	
10	\paragraph{Two GAR variants.}
11	We distinguish two measurement variants throughout this paper. \textbf{GAR-Dongre} refers to the original definition in Equation~\ref{eq:gar}, which averages over the full response token set $\mathcal{R}_\tau$. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
12	\begin{equation}\label{eq:gar-ours}
13	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
14	\end{equation}
15	where $t_\tau$ is the index of the last token in the assistant response at turn $\tau$. The last token is the position at which the model conditions its next generation step, so attention patterns at this position most directly reflect the information the model draws upon for continuation. We use GAR-ours as the optimization target for the auxiliary loss $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}), while GAR-Dongre provides a complementary aggregate measure for comparison.
16	
17	\paragraph{Residual stream persistence.}
18	\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream across conversation turns: linear discriminant analysis probes achieve AUC\,=\,0.98 for detecting goal content even at late turns where GAR has declined substantially. The information remains present in the hidden states, but the attention mechanism ceases to route it toward the output computation. This dissociation between information availability and information utilization motivates an intervention that targets the residual pathway directly.
19	
20	\paragraph{Problem statement.}
21	GAR decays across conversation turns while goal information persists in the residual stream. We ask whether learnable residual gates can recover goal attention without degrading language modeling quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "3b1b1895-526e-4e0b-974e-b3e7ce959c57",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex",
      "content": "\\section{Background}\\label{sec:background}\n\n\\paragraph{Goal Attention Ratio.}\nMulti-turn instruction-following models receive a system prompt that specifies the task objective. We denote the token subsequence corresponding to the task specification within this system prompt as the \\emph{goal tokens} $\\mathcal{G}$, excluding formatting markers and role tags. \\citet{dongre2026attention} introduced the Goal Attention Ratio (GAR) to quantify how much attention a model allocates to these goal tokens during response generation. Given a model with $L$ layers and $H$ attention heads, GAR at conversation turn $\\tau$ is\n\\begin{equation}\\label{eq:gar}\n  \\text{GAR}(\\tau) = \\frac{1}{L \\cdot H \\cdot |\\mathcal{R}_\\tau|} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{i \\in \\mathcal{R}_\\tau} \\sum_{j \\in \\mathcal{G}} A_{i,j}^{(\\ell,h)},\n\\end{equation}\nwhere $\\mathcal{R}_\\tau$ is the set of response tokens at turn $\\tau$ and $A_{i,j}^{(\\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\\ell$, head $h$. This definition averages attention to goal tokens over all response positions, all layers, and all heads.\n\n\\paragraph{Two GAR variants.}\nWe distinguish two measurement variants throughout this paper. \\textbf{GAR-Dongre} refers to the original definition in Equation~\\ref{eq:gar}, which averages over the full response token set $\\mathcal{R}_\\tau$. \\textbf{GAR-ours} restricts the measurement to the \\emph{last token} of each assistant turn:\n\\begin{equation}\\label{eq:gar-ours}\n  \\text{GAR\\text{-}ours}(\\tau) = \\frac{1}{L \\cdot H} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{j \\in \\mathcal{G}} A_{t_\\tau,\\, j}^{(\\ell,h)},\n\\end{equation}\nwhere $t_\\tau$ is the index of the last token in the assistant response at turn $\\tau$. The last token is the position at which the model conditions its next generation step, so attention patterns at this position most directly reflect the information the model draws upon for continuation. We use GAR-ours as the optimization target for the auxiliary loss $\\mathcal{L}_\\text{GAR}$ (\\S\\ref{sec:loss}), while GAR-Dongre provides a complementary aggregate measure for comparison.\n\n\\paragraph{Residual stream persistence.}\n\\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream across conversation turns: linear discriminant analysis probes achieve AUC\\,=\\,0.98 for detecting goal content even at late turns where GAR has declined substantially. The information remains present in the hidden states, but the attention mechanism ceases to route it toward the output computation. This dissociation between information availability and information utilization motivates an intervention that targets the residual pathway directly.\n\n\\paragraph{Problem statement.}\nGAR decays across conversation turns while goal information persists in the residual stream. We ask whether learnable residual gates can recover goal attention without degrading language modeling quality.",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the context I need. Let me also check the experiments.tex more carefully for how the 30x gap is discussed, so I can connect smoothly. I also need to check the style conventions more carefully.

Key observations from reading existing sections:
1. Style: Direct, declarative sentences. No em-dashes. No -ing endings. Precise claim scoping.
2. Label convention: `\label{sec:...}` for sections
3. Figure references use `\ref{fig:...}` format


4. Citations follow `\citet{...}` and `\citep{...}` patterns
5. No figure environments in section files, just references
6. The experiments.tex already mentions the 30x gap and defers mechanistic analysis to §6

Now I'm planning the analysis.tex structure. I'll start with a gradient conflict observation section that presents the data descriptively without causal claims, followed by a gate turn conditioning section examining the inverted gate behavior, then move into the deeper mechanistic analysis.

The core of this section will be the PCGrad causal exclusion argument—I need to structure it as observation, hypothesis, experiment, and exclusion with clear modus tollens logic. Then I'll address the distribution shift gap between same-distribution and cross-distribution settings, connecting it back to exposure bias and resolving the tension with He et al. 2019.

I'm being careful to avoid em-dashes, -ing phrase endings, and AI buzzwords. Every number needs to trace back to the provided data, and I need to scope causal language precisely—especially for the direction conflict analysis. The tone should match the declarative, direct style of the experiments and methods sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "339ef6e4-38be-4d3b-8e89-0be577ce4c92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRmCRfYzLhvqQzhJY1zbPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 36082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1337
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

_source line 28_

Now I have full context. Writing `analysis.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "b827585b-edd3-4a09-b845-855d0cc815c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRmCRfYzLhvqQzhJY1zbPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 36082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1337
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

_source line 29_

<details open><summary>🔧 Tool call — Write · `toolu_01PvhykYRk7U9qtG7PTQBvC4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "content": "\\section{Analysis}\\label{sec:analysis}\n\nThe four-way ablation in \\S\\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section investigates why. We first characterize the gradient dynamics between the two training objectives (\\S\\ref{subsec:gradient-conflict}), then show that the learned gates exhibit behavior opposite to the design intent (\\S\\ref{subsec:gate-conditioning}). A targeted causal experiment rules out gradient direction conflict as the explanation (\\S\\ref{subsec:pcgrad}), and a distribution shift analysis identifies the actual failure mode (\\S\\ref{subsec:dist-shift}).\n\n\\subsection{Gradient Conflict Observation}\\label{subsec:gradient-conflict}\n\nTo understand how the two loss terms interact during training, we measure the cosine similarity between $\\nabla_\\theta \\mathcal{L}_\\text{NTP}$ and $\\nabla_\\theta \\mathcal{L}_\\text{GAR}$ at each transformer layer across three training epochs. Table~\\ref{tab:grad-conflict} summarizes the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Gradient interaction between $\\mathcal{L}_\\text{NTP}$ and $\\mathcal{L}_\\text{GAR}$ across training epochs. \\textit{cos\\_sim}: mean cosine similarity across layers. \\textit{neg\\%}: percentage of layers with negative cosine similarity. \\textit{mag\\_ratio}: ratio of NTP to GAR gradient magnitudes.}\n\\label{tab:grad-conflict}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Epoch} & \\textbf{cos\\_sim} & \\textbf{neg\\%} & \\textbf{mag\\_ratio} \\\\\n\\midrule\n0 & $-$0.089 & 78.6 & 7.5$\\times$ \\\\\n1 & $-$0.054 & 71.4 & 13.7$\\times$ \\\\\n2 & $-$0.042 & 67.9 & 14.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns are apparent. First, the NTP and GAR gradients point in opposing directions across 68--79\\% of layers throughout training. The mean cosine similarity is negative at every epoch, though it attenuates slightly from $-$0.089 to $-$0.042 as training progresses. Second, the NTP gradient magnitude dominates the GAR gradient by a factor that grows from 7.5$\\times$ at epoch~0 to 14.7$\\times$ at epoch~2. Direction conflict decreases while magnitude imbalance worsens. We observe these patterns as descriptive statistics of the training dynamics. This does not establish that gradient conflict causes $\\mathcal{L}_\\text{GAR}$ to fail; \\S\\ref{subsec:pcgrad} tests this hypothesis directly.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nThe design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\\S\\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.\n\nThe gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \\times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.\n\nThe practical consequence is that the gates provide almost no intervention at inference time. Across all layers, mean gate values during inference range from 0.93 to 0.98, corresponding to residual stream attenuation of only 2--7\\%. This attenuation is far below what would be required for meaningful modulation, and it explains the convergence with LoRA-only in Table~\\ref{tab:four-way}. Figure~\\ref{fig:gate-shift}(a) visualizes the per-layer gate difference between early and late turns.\n\n\\subsection{PCGrad Causal Exclusion}\\label{subsec:pcgrad}\n\nThe gradient conflict observed in \\S\\ref{subsec:gradient-conflict} raises a natural hypothesis: perhaps the opposing gradient directions between $\\mathcal{L}_\\text{NTP}$ and $\\mathcal{L}_\\text{GAR}$ prevent the GAR objective from converging. If direction conflict is the cause of $\\mathcal{L}_\\text{GAR}$ collapse, then eliminating direction conflict should prevent the collapse. We test this prediction using PCGrad \\citep{yu2020pcgrad}.\n\nPCGrad projects the gradient of one task onto the normal plane of the other whenever two task gradients conflict in direction. We apply PCGrad to the gate parameters only, projecting $\\nabla_\\theta \\mathcal{L}_\\text{NTP}$ onto the orthogonal complement of $\\nabla_\\theta \\mathcal{L}_\\text{GAR}$ whenever their cosine similarity is negative. This eliminates the directional component of the conflict while leaving magnitude differences intact. PCGrad does not address magnitude imbalance (which GradNorm targets; \\citealp{chen2018gradnorm}) or Nash equilibrium violations (which Nash-MTL targets; \\citealp{navon2022nash}); our claim is scoped to direction conflict alone.\n\nThe result is unambiguous. Under PCGrad, the cosine similarity between NTP and GAR gradients on gate parameters turns positive by gradient step~200 ($+$0.086), confirming that PCGrad successfully removes direction conflict. Yet $\\mathcal{L}_\\text{GAR}$ follows a trajectory nearly identical to the baseline (v7) and collapses in the same manner. Figure~\\ref{fig:training-pcgrad}(b) overlays the $\\mathcal{L}_\\text{GAR}$ training curves for both conditions.\n\nThe causal exclusion follows by \\emph{modus tollens}:\n\\begin{enumerate}\n    \\item If direction conflict causes $\\mathcal{L}_\\text{GAR}$ collapse, then removing direction conflict should prevent the collapse.\n    \\item PCGrad removes direction conflict (cosine similarity turns positive at step~200).\n    \\item $\\mathcal{L}_\\text{GAR}$ collapses regardless.\n    \\item Therefore, direction conflict is not the cause of $\\mathcal{L}_\\text{GAR}$ collapse.\n\\end{enumerate}\n\nThis result recharacterizes the gradient observations in \\S\\ref{subsec:gradient-conflict}: direction conflict between $\\mathcal{L}_\\text{NTP}$ and $\\mathcal{L}_\\text{GAR}$ is a symptom of the multi-objective optimization dynamics, not the mechanism responsible for GAR failure. The magnitude imbalance (7.5--14.7$\\times$) and potential Nash equilibrium violations remain as candidate explanations that future work can test with GradNorm \\citep{chen2018gradnorm} and Nash-MTL \\citep{navon2022nash}.\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe preceding subsections explain why the gating mechanism is ineffective during training. This subsection addresses why the learned GAR improvements fail to transfer from training to inference.\n\nRecall from \\S\\ref{sec:experiments} that teacher-forced GAR-ours reaches 0.49 for all fine-tuned variants, while autoregressive GAR-ours drops to 0.016, a 30$\\times$ gap. We decompose this gap by comparing same-distribution and cross-distribution evaluation. Under same-distribution evaluation (teacher-forced UltraChat text), GAR-ours is approximately 0.49, confirming that the model has learned the intended attention pattern on the training distribution. Under cross-distribution evaluation (model-generated text), GAR-ours drops to 0.016. The training itself is sound; the failure is one of generalization.\n\nGAR-Dongre provides a revealing control. Across both evaluation conditions, GAR-Dongre remains uniformly low (0.01--0.02) with no distribution gap. The distribution shift selectively destroys the concentrated attention pattern captured by GAR-ours (last-token, summary-position attention) while leaving the diffuse attention pattern captured by GAR-Dongre (averaged across all positions) unaffected. This selectivity implies that the distribution shift disrupts a specific learned routing behavior rather than attention computation in general.\n\nThe mechanism connecting training regime to distribution shift is exposure bias \\citep{bengio2015scheduled}. During training, the model conditions each token prediction on ground-truth prefixes from UltraChat. At inference, it conditions on its own prior outputs. The attention patterns optimized for the former distribution do not transfer to the latter, because the statistical properties of model-generated text diverge from those of human-written reference text. The 2--7\\% gate attenuation documented in \\S\\ref{subsec:gate-conditioning} is far too weak to compensate for this distributional mismatch.\n\n\\citet{he2019exposure} showed that language models exhibit token-level self-recovery from exposure bias: accumulated errors in autoregressive generation do not degrade perplexity as severely as worst-case analysis predicts. Our results are consistent with this finding at the token level, as PPL remains normal across all conditions (Table~\\ref{tab:four-way}). The critical distinction is between primary and auxiliary objectives. The NTP objective is robust to exposure bias because next-token prediction is the same task at both training and inference time. The GAR auxiliary objective is fragile because it optimizes an attention pattern under teacher-forced context that has no counterpart in autoregressive generation. Primary-task self-recovery does not extend to auxiliary objectives that depend on distributional properties of the input prefix. Figure~\\ref{fig:gate-shift}(b) summarizes the four-model GAR comparison across evaluation conditions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "3d81090b-ae80-4419-b6db-ea2e00a2d034",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRmCRfYzLhvqQzhJY1zbPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 36082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1337
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

_source line 30 · 2026-05-19T22:51:23.574Z_

<details><summary>↩ Tool result · `toolu_01PvhykYRk7U9qtG7PTQBvC4`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "8c5a148e-d041-4e8d-a031-8cea5d424db2",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "content": "\\section{Analysis}\\label{sec:analysis}\n\nThe four-way ablation in \\S\\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section investigates why. We first characterize the gradient dynamics between the two training objectives (\\S\\ref{subsec:gradient-conflict}), then show that the learned gates exhibit behavior opposite to the design intent (\\S\\ref{subsec:gate-conditioning}). A targeted causal experiment rules out gradient direction conflict as the explanation (\\S\\ref{subsec:pcgrad}), and a distribution shift analysis identifies the actual failure mode (\\S\\ref{subsec:dist-shift}).\n\n\\subsection{Gradient Conflict Observation}\\label{subsec:gradient-conflict}\n\nTo understand how the two loss terms interact during training, we measure the cosine similarity between $\\nabla_\\theta \\mathcal{L}_\\text{NTP}$ and $\\nabla_\\theta \\mathcal{L}_\\text{GAR}$ at each transformer layer across three training epochs. Table~\\ref{tab:grad-conflict} summarizes the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Gradient interaction between $\\mathcal{L}_\\text{NTP}$ and $\\mathcal{L}_\\text{GAR}$ across training epochs. \\textit{cos\\_sim}: mean cosine similarity across layers. \\textit{neg\\%}: percentage of layers with negative cosine similarity. \\textit{mag\\_ratio}: ratio of NTP to GAR gradient magnitudes.}\n\\label{tab:grad-conflict}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Epoch} & \\textbf{cos\\_sim} & \\textbf{neg\\%} & \\textbf{mag\\_ratio} \\\\\n\\midrule\n0 & $-$0.089 & 78.6 & 7.5$\\times$ \\\\\n1 & $-$0.054 & 71.4 & 13.7$\\times$ \\\\\n2 & $-$0.042 & 67.9 & 14.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns are apparent. First, the NTP and GAR gradients point in opposing directions across 68--79\\% of layers throughout training. The mean cosine similarity is negative at every epoch, though it attenuates slightly from $-$0.089 to $-$0.042 as training progresses. Second, the NTP gradient magnitude dominates the GAR gradient by a factor that grows from 7.5$\\times$ at epoch~0 to 14.7$\\times$ at epoch~2. Direction conflict decreases while magnitude imbalance worsens. We observe these patterns as descriptive statistics of the training dynamics. This does not establish that gradient conflict causes $\\mathcal{L}_\\text{GAR}$ to fail; \\S\\ref{subsec:pcgrad} tests this hypothesis directly.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nThe design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\\S\\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.\n\nThe gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \\times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.\n\nThe practical consequence is that the gates provide almost no intervention at inference time. Across all layers, mean gate values during inference range from 0.93 to 0.98, corresponding to residual stream attenuation of only 2--7\\%. This attenuation is far below what would be required for meaningful modulation, and it explains the convergence with LoRA-only in Table~\\ref{tab:four-way}. Figure~\\ref{fig:gate-shift}(a) visualizes the per-layer gate difference between early and late turns.\n\n\\subsection{PCGrad Causal Exclusion}\\label{subsec:pcgrad}\n\nThe gradient conflict observed in \\S\\ref{subsec:gradient-conflict} raises a natural hypothesis: perhaps the opposing gradient directions between $\\mathcal{L}_\\text{NTP}$ and $\\mathcal{L}_\\text{GAR}$ prevent the GAR objective from converging. If direction conflict is the cause of $\\mathcal{L}_\\text{GAR}$ collapse, then eliminating direction conflict should prevent the collapse. We test this prediction using PCGrad \\citep{yu2020pcgrad}.\n\nPCGrad projects the gradient of one task onto the normal plane of the other whenever two task gradients conflict in direction. We apply PCGrad to the gate parameters only, projecting $\\nabla_\\theta \\mathcal{L}_\\text{NTP}$ onto the orthogonal complement of $\\nabla_\\theta \\mathcal{L}_\\text{GAR}$ whenever their cosine similarity is negative. This eliminates the directional component of the conflict while leaving magnitude differences intact. PCGrad does not address magnitude imbalance (which GradNorm targets; \\citealp{chen2018gradnorm}) or Nash equilibrium violations (which Nash-MTL targets; \\citealp{navon2022nash}); our claim is scoped to direction conflict alone.\n\nThe result is unambiguous. Under PCGrad, the cosine similarity between NTP and GAR gradients on gate parameters turns positive by gradient step~200 ($+$0.086), confirming that PCGrad successfully removes direction conflict. Yet $\\mathcal{L}_\\text{GAR}$ follows a trajectory nearly identical to the baseline (v7) and collapses in the same manner. Figure~\\ref{fig:training-pcgrad}(b) overlays the $\\mathcal{L}_\\text{GAR}$ training curves for both conditions.\n\nThe causal exclusion follows by \\emph{modus tollens}:\n\\begin{enumerate}\n    \\item If direction conflict causes $\\mathcal{L}_\\text{GAR}$ collapse, then removing direction conflict should prevent the collapse.\n    \\item PCGrad removes direction conflict (cosine similarity turns positive at step~200).\n    \\item $\\mathcal{L}_\\text{GAR}$ collapses regardless.\n    \\item Therefore, direction conflict is not the cause of $\\mathcal{L}_\\text{GAR}$ collapse.\n\\end{enumerate}\n\nThis result recharacterizes the gradient observations in \\S\\ref{subsec:gradient-conflict}: direction conflict between $\\mathcal{L}_\\text{NTP}$ and $\\mathcal{L}_\\text{GAR}$ is a symptom of the multi-objective optimization dynamics, not the mechanism responsible for GAR failure. The magnitude imbalance (7.5--14.7$\\times$) and potential Nash equilibrium violations remain as candidate explanations that future work can test with GradNorm \\citep{chen2018gradnorm} and Nash-MTL \\citep{navon2022nash}.\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe preceding subsections explain why the gating mechanism is ineffective during training. This subsection addresses why the learned GAR improvements fail to transfer from training to inference.\n\nRecall from \\S\\ref{sec:experiments} that teacher-forced GAR-ours reaches 0.49 for all fine-tuned variants, while autoregressive GAR-ours drops to 0.016, a 30$\\times$ gap. We decompose this gap by comparing same-distribution and cross-distribution evaluation. Under same-distribution evaluation (teacher-forced UltraChat text), GAR-ours is approximately 0.49, confirming that the model has learned the intended attention pattern on the training distribution. Under cross-distribution evaluation (model-generated text), GAR-ours drops to 0.016. The training itself is sound; the failure is one of generalization.\n\nGAR-Dongre provides a revealing control. Across both evaluation conditions, GAR-Dongre remains uniformly low (0.01--0.02) with no distribution gap. The distribution shift selectively destroys the concentrated attention pattern captured by GAR-ours (last-token, summary-position attention) while leaving the diffuse attention pattern captured by GAR-Dongre (averaged across all positions) unaffected. This selectivity implies that the distribution shift disrupts a specific learned routing behavior rather than attention computation in general.\n\nThe mechanism connecting training regime to distribution shift is exposure bias \\citep{bengio2015scheduled}. During training, the model conditions each token prediction on ground-truth prefixes from UltraChat. At inference, it conditions on its own prior outputs. The attention patterns optimized for the former distribution do not transfer to the latter, because the statistical properties of model-generated text diverge from those of human-written reference text. The 2--7\\% gate attenuation documented in \\S\\ref{subsec:gate-conditioning} is far too weak to compensate for this distributional mismatch.\n\n\\citet{he2019exposure} showed that language models exhibit token-level self-recovery from exposure bias: accumulated errors in autoregressive generation do not degrade perplexity as severely as worst-case analysis predicts. Our results are consistent with this finding at the token level, as PPL remains normal across all conditions (Table~\\ref{tab:four-way}). The critical distinction is between primary and auxiliary objectives. The NTP objective is robust to exposure bias because next-token prediction is the same task at both training and inference time. The GAR auxiliary objective is fragile because it optimizes an attention pattern under teacher-forced context that has no counterpart in autoregressive generation. Primary-task self-recovery does not extend to auxiliary objectives that depend on distributional properties of the input prefix. Figure~\\ref{fig:gate-shift}(b) summarizes the four-model GAR comparison across evaluation conditions.",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 31_

Let me verify the output against the constraints: no em-dashes, no -ing endings, correct data, correct references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "35142414-4f71-471c-a1f4-065d683d0598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbSmfy5RNKFpCfwyBdUb7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3235,
      "cache_read_input_tokens": 37419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3235
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

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01TyPGgLCEV5NFEbfrL7somK`</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex; echo \"---\"; grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex; echo \"---\"; grep -nP \"ing[,.]?\\s*$\" /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "description": "Check for em-dashes, en-dashes, and -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "924d456c-8d8e-4dff-8f9f-9215547d636b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbSmfy5RNKFpCfwyBdUb7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3235,
      "cache_read_input_tokens": 37419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3235
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

_source line 33 · 2026-05-19T22:51:29.223Z_

<details><summary>↩ Tool result · `toolu_01TyPGgLCEV5NFEbfrL7somK`</summary>

```text
---
---
10:\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "c4c79b45-18d8-4e5d-95eb-61934c5e44a3",
  "tool_use_result": {
    "stdout": "---\n---\n10:\\centering",
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01QHUrvdchfQS8UJt35PuGJc`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "description": "Word count of analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "4dfeb4e6-0498-490c-8365-c3c9d2b5cdb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbSmfy5RNKFpCfwyBdUb7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3235,
      "cache_read_input_tokens": 37419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3235
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

_source line 35 · 2026-05-19T22:51:29.635Z_

<details><summary>↩ Tool result · `toolu_01QHUrvdchfQS8UJt35PuGJc`</summary>

```text
1198 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "09c8806c-8f9e-4a07-bbf1-653e48cfda3d",
  "tool_use_result": {
    "stdout": "1198 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
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

_source line 36_

No em-dashes, no explanatory en-dashes, and the only `-ing` match is `\centering` (a LaTeX command, not prose). Word count is ~1198 including LaTeX markup, which puts the prose at roughly the 1000-word target.

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "6de34ddd-46dd-4b33-b5b3-5d3453470e8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cc14a2HgXTP5BysqSjZ6SU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 40654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MbQSKhqJvVSc1B6QYBUd8U`</summary>

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
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "87265b68-1484-44e4-aee2-ef508accdeb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cc14a2HgXTP5BysqSjZ6SU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 40654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

_source line 38 · 2026-05-19T22:51:33.747Z_

<details><summary>↩ Tool result · `toolu_01MbQSKhqJvVSc1B6QYBUd8U`</summary>

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
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "2d529a79-78b3-4cc8-a8de-b898ca7191f3",
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

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01NspcwAaFUDiUq4WsNDWTyZ`</summary>

```json
{
  "name": "analysis_section_v1",
  "type": "paper",
  "description": "§6 Analysis chapter for EMNLP 2026 paper: gradient conflict observation, gate turn conditioning, PCGrad causal exclusion, distribution shift analysis",
  "project": "turn_residual_gating",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "tags": [
    "paper",
    "analysis",
    "section6"
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
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "f8693088-ab98-4fca-a915-329b5f6032e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXD3XiUY7vy4MrDoqbDpAy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 41118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 783
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

_source line 40 · 2026-05-19T22:51:38.272Z_

<details><summary>↩ Tool result · `toolu_01NspcwAaFUDiUq4WsNDWTyZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_c43c3f\", \"name\": \"analysis_section_v1\", \"type\": \"paper\", \"description\": \"§6 Analysis chapter for EMNLP 2026 paper: gradient conflict observation, gate turn conditioning, PCGrad causal exclusion, distribution shift analysis\", \"path\": \"projects/turn_residual_gating/artifacts/_project/paper/analysis.tex\", \"url\": null, \"project\": \"turn_residual_gating\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T22:51:38.217961+00:00\", \"tags\": [\"paper\", \"analysis\", \"section6\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "43f6a3c5-166f-401d-bfdb-cab76e109f2d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_c43c3f\\\", \\\"name\\\": \\\"analysis_section_v1\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"§6 Analysis chapter for EMNLP 2026 paper: gradient conflict observation, gate turn conditioning, PCGrad causal exclusion, distribution shift analysis\\\", \\\"path\\\": \\\"projects/turn_residual_gating/artifacts/_project/paper/analysis.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"turn_residual_gating\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T22:51:38.217961+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"analysis\\\", \\\"section6\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_c43c3f\", \"name\": \"analysis_section_v1\", \"type\": \"paper\", \"description\": \"§6 Analysis chapter for EMNLP 2026 paper: gradient conflict observation, gate turn conditioning, PCGrad causal exclusion, distribution shift analysis\", \"path\": \"projects/turn_residual_gating/artifacts/_project/paper/analysis.tex\", \"url\": null, \"project\": \"turn_residual_gating\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T22:51:38.217961+00:00\", \"tags\": [\"paper\", \"analysis\", \"section6\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

`analysis.tex` 已写入，~1000 words，4 个子节结构完整。

要点核查：
- **§6.1**: 描述性观察，明确标注非因果 claim，含 Table 1 (3-row gradient conflict 数据)
- **§6.2**: 27/28 层 gate 行为与设计意图相反，Wilcoxon p=3.73e-8，inference-time attenuation 仅 2-7%，引用 Figure 3(a)
- **§6.3**: PCGrad 消除方向冲突 (cos_sim 转正 +0.086) 但 L_GAR 仍坍塌，modus tollens 编号列表，claim scope 限定为 direction conflict，GradNorm/Nash-MTL 留作 future work，引用 Figure 2(b)
- **§6.4**: Same-dist GAR 0.49 vs cross-dist 0.016 (30x gap)，GAR-Dongre 无 gap 作为 control，连接 exposure bias 文献 (bengio2015scheduled, he2019exposure)，处理 He et al. tension (primary objective robust, auxiliary objective fragile)，引用 Figure 3(b)
- 风格：零 em-dash，零 -ing 结尾，零 AI buzzwords

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "uuid": "f692f5d7-6d0b-4599-abbd-71848ede55f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dkos5Y7EjSawtSjhUmngwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 519,
      "cache_read_input_tokens": 41901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 519
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

_source line 42_

`analysis.tex` 已写入，~1000 words，4 个子节结构完整。

要点核查：
- **§6.1**: 描述性观察，明确标注非因果 claim，含 Table 1 (3-row gradient conflict 数据)
- **§6.2**: 27/28 层 gate 行为与设计意图相反，Wilcoxon p=3.73e-8，inference-time attenuation 仅 2-7%，引用 Figure 3(a)
- **§6.3**: PCGrad 消除方向冲突 (cos_sim 转正 +0.086) 但 L_GAR 仍坍塌，modus tollens 编号列表，claim scope 限定为 direction conflict，GradNorm/Nash-MTL 留作 future work，引用 Figure 2(b)
- **§6.4**: Same-dist GAR 0.49 vs cross-dist 0.016 (30x gap)，GAR-Dongre 无 gap 作为 control，连接 exposure bias 文献 (bengio2015scheduled, he2019exposure)，处理 He et al. tension (primary objective robust, auxiliary objective fragile)，引用 Figure 3(b)
- 风格：零 em-dash，零 -ing 结尾，零 AI buzzwords

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 112226,
  "duration_api_ms": 113282,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "c50ddfea-9d6c-4708-96ef-b7fd03bb090b",
  "total_cost_usd": 0.47924375,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 30973,
    "cache_read_input_tokens": 305307,
    "output_tokens": 5189,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30973,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 359,
        "cache_read_input_tokens": 41901,
        "cache_creation_input_tokens": 519,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 519
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3109,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0032189999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 5189,
      "cacheReadInputTokens": 305307,
      "cacheCreationInputTokens": 30973,
      "webSearchRequests": 0,
      "costUSD": 0.47602475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "02876f28-e6c4-4468-90a4-eff0cef6fa2b"
}
```

</details>

---
