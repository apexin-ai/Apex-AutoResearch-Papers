# paper writing intro reframe

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_writing_intro_reframe_20260528T040935.log`
- **Structured JSON:** [`e52f4623fa647bfe7f07.json`](../../sessions/e5/e52f4623fa647bfe7f07.json)

## Before a recorded user message

14 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
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
  "uuid": "535391df-e873-4d49-8f02-73daa9a039d3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779953400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2aa21be7-8210-4ef7-acfe-105518d73366",
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20"
}
```

---

### Assistant

_source line 4_

I'll start by reading the skill file and the current introduction to understand what needs to change.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "cc690587-d3c9-42ce-a819-b143f4268295",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RC91ySH5DFB2xZPiaktzV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13248,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13248
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

<details open><summary>🔧 Tool call — Read · `toolu_01ADwtMSVzPPX2wfry8B5MFm`</summary>

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
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "6d803fe4-c104-40c0-81dd-0bfc48751353",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RC91ySH5DFB2xZPiaktzV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13248,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13248
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

_source line 6 · 2026-05-28T04:09:49.984Z_

<details><summary>↩ Tool result · `toolu_01ADwtMSVzPPX2wfry8B5MFm`</summary>

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
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "b21e325d-dbc6-4e05-882f-512df7e292c7",
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

<details open><summary>🔧 Tool call — Read · `toolu_019PfyJ2zNNMm4uqJYHRBWLE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "9a9d6565-355e-4102-aa39-2fde06b65a2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RC91ySH5DFB2xZPiaktzV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13248,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13248
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

_source line 8 · 2026-05-28T04:09:50.528Z_

<details><summary>↩ Tool result · `toolu_019PfyJ2zNNMm4uqJYHRBWLE`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	\looseness=-1 Deploying a pretrained Vision-Language-Action (VLA) model on a new task usually requires fine-tuning on task demonstrations, yet collecting that data is expensive and the resulting checkpoint may not transfer further. A more attractive route keeps the VLA frozen and improves action quality at inference time. Flow-matching VLAs~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are well suited to this setting because each forward pass produces a stochastic action sample, enabling multi-sample selection and correction without retraining~\cite{snell2024scaling}. But does test-time correction always help? We systematically analyze this question and find that it does not: unconditional correction degrades performance on every suite we evaluate, and the key to making correction useful is knowing \emph{when not} to apply it.
5	
6	\looseness=-1 Recent work touches parts of this problem without addressing the fundamental question. A2C2~\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and addresses temporal staleness rather than initial action quality. ReconVLA~\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\cite{liu2026scvla} uses reinforcement learning and therefore does not stay weight-frozen. VLA-Pilot~\cite{li2025vlapilot} performs evolutionary search at $2.41$\,s per control step, ruling out closed-loop deployment. None analyze when correction helps versus when it hurts, nor provide a mechanism to abstain from correction on confident steps.
7	
8	\looseness=-1 We begin by analyzing the failure mode of unconditional correction. A lightweight Correction Residual Module (CRM, ${\sim}$327K parameters) trained on demonstration data applies a bounded residual to argmin-selected action samples. Under a K-matched design ($K{=}2$ for both conditions, same $\varepsilon{=}0.2$ and CRM checkpoint), CRM always-on degrades all four LIBERO suites on SmolVLA~\cite{shukor2025smolvla} (0.4B): $-$1.3 to $-$14.8\,pp. The same pattern holds on $\pi_{0.5}$~\cite{black2025pi05} (3.6B, 95--98\% baseline), where unconditional correction degrades all three evaluated suites by up to $-$14.0\,pp. The root cause is that 80--97\% of control steps are already confident; corrections on these steps inject noise rather than signal.
9	
10	\looseness=-1 This analysis motivates \textbf{ACR-VLA}, an adaptive inference-time pipeline that decides per step whether correction is needed. ACR-VLA draws only $K{=}2$ samples in a single batched forward pass and uses their pairwise $L_2$ distance as a per-step uncertainty probe. This probe is well-calibrated: Spearman $\rho{=}0.9979$ against $K{=}10$ sample variance, whereas three alternatives all yield $\rho < 0.16$. When the probe falls below a threshold $\tau$, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds $\tau$, the CRM applies a bounded residual. The method is a direct consequence of the analysis: once we identify that correction harms confident steps, gating becomes the natural solution.
11	
12	\looseness=-1 On SmolVLA across four LIBERO suites, ACR-VLA's adaptive gate triggers correction only on high-uncertainty steps (3--20\% of steps), recovering all degradation from unconditional correction: $+$1.5\,pp on Spatial, $+$1.3\,pp on Goal, and baseline-preserving on Object and Long. Under the K-matched design, ACR-VLA exceeds CRM always-on on all four suites ($\Delta_{\mathrm{gate}}{=}{+}2.8$ to $+$14.5\,pp). On $\pi_{0.5}$ (3.6B, 95--98\% baseline), unconditional correction degrades all three evaluated suites by up to $-$14.0\,pp ($3.8{\times}$ the SmolVLA drop on Goal), confirming that the correction-harms-confident-steps pattern generalizes---and amplifies---on stronger models. A boundary analysis on OpenVLA-OFT~\cite{kim2024openvla} (7B, deterministic) confirms that stochastic sample diversity is a prerequisite.
13	
14	\looseness=-1 The key finding is mechanistic: \emph{knowing when not to correct} matters more than correction strength. CRM always-on applies the same learned residual to every step, including the ${\sim}$80--97\% where the VLA is already confident; corrections on these steps cause up to $-$14.8\,pp degradation. ACR-VLA's adaptive gate triggers CRM only on high-uncertainty steps, preserving the VLA's own output elsewhere. A threshold sensitivity analysis across three suites (Appendix~\ref{sec:tau_sweep}) shows that success rate is robust to $\tau$ choice, establishing gating as a stable design element rather than a fragile hyperparameter.
15	
16	Our contributions are:
17	\begin{enumerate}[leftmargin=*,nosep]
18	  \item \textbf{Systematic analysis of test-time correction} (Section~\ref{sec:failure_modes}): under a K-matched design ($K{=}2$, same $\varepsilon$ and CRM), we show that unconditional correction degrades all four LIBERO suites on SmolVLA ($-$1.3 to $-$14.8\,pp) and all three evaluated suites on $\pi_{0.5}$ ($-$2.0 to $-$14.0\,pp), identifying the 80--97\% of confident steps as the source of harm.
19	  \item \textbf{Adaptive gating mechanism} (Section~\ref{sec:method}): a $K{=}2$ pairwise $L_2$ uncertainty probe ($\rho{=}0.9979$) gates CRM correction to the 3--20\% of high-uncertainty steps, recovering all degradation ($\Delta_{\mathrm{gate}}{=}{+}2.8$ to $+$14.5\,pp).
20	  \item \textbf{Cross-VLA validation} (Section~\ref{sec:cross_vla}): on $\pi_{0.5}$ (3.6B, 95--98\% baseline), unconditional correction degrades all three evaluated suites ($-$2.0 to $-$14.0\,pp), with Goal suffering $3.8{\times}$ the SmolVLA drop; deterministic VLAs (OpenVLA-OFT) produce near-identical samples that make multi-sample methods vacuous.
21	\end{enumerate}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "ac930c9c-311c-4ca9-8379-6c4970ef608a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n\\looseness=-1 Deploying a pretrained Vision-Language-Action (VLA) model on a new task usually requires fine-tuning on task demonstrations, yet collecting that data is expensive and the resulting checkpoint may not transfer further. A more attractive route keeps the VLA frozen and improves action quality at inference time. Flow-matching VLAs~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are well suited to this setting because each forward pass produces a stochastic action sample, enabling multi-sample selection and correction without retraining~\\cite{snell2024scaling}. But does test-time correction always help? We systematically analyze this question and find that it does not: unconditional correction degrades performance on every suite we evaluate, and the key to making correction useful is knowing \\emph{when not} to apply it.\n\n\\looseness=-1 Recent work touches parts of this problem without addressing the fundamental question. A2C2~\\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and addresses temporal staleness rather than initial action quality. ReconVLA~\\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\\cite{liu2026scvla} uses reinforcement learning and therefore does not stay weight-frozen. VLA-Pilot~\\cite{li2025vlapilot} performs evolutionary search at $2.41$\\,s per control step, ruling out closed-loop deployment. None analyze when correction helps versus when it hurts, nor provide a mechanism to abstain from correction on confident steps.\n\n\\looseness=-1 We begin by analyzing the failure mode of unconditional correction. A lightweight Correction Residual Module (CRM, ${\\sim}$327K parameters) trained on demonstration data applies a bounded residual to argmin-selected action samples. Under a K-matched design ($K{=}2$ for both conditions, same $\\varepsilon{=}0.2$ and CRM checkpoint), CRM always-on degrades all four LIBERO suites on SmolVLA~\\cite{shukor2025smolvla} (0.4B): $-$1.3 to $-$14.8\\,pp. The same pattern holds on $\\pi_{0.5}$~\\cite{black2025pi05} (3.6B, 95--98\\% baseline), where unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp. The root cause is that 80--97\\% of control steps are already confident; corrections on these steps inject noise rather than signal.\n\n\\looseness=-1 This analysis motivates \\textbf{ACR-VLA}, an adaptive inference-time pipeline that decides per step whether correction is needed. ACR-VLA draws only $K{=}2$ samples in a single batched forward pass and uses their pairwise $L_2$ distance as a per-step uncertainty probe. This probe is well-calibrated: Spearman $\\rho{=}0.9979$ against $K{=}10$ sample variance, whereas three alternatives all yield $\\rho < 0.16$. When the probe falls below a threshold $\\tau$, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds $\\tau$, the CRM applies a bounded residual. The method is a direct consequence of the analysis: once we identify that correction harms confident steps, gating becomes the natural solution.\n\n\\looseness=-1 On SmolVLA across four LIBERO suites, ACR-VLA's adaptive gate triggers correction only on high-uncertainty steps (3--20\\% of steps), recovering all degradation from unconditional correction: $+$1.5\\,pp on Spatial, $+$1.3\\,pp on Goal, and baseline-preserving on Object and Long. Under the K-matched design, ACR-VLA exceeds CRM always-on on all four suites ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp). On $\\pi_{0.5}$ (3.6B, 95--98\\% baseline), unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp ($3.8{\\times}$ the SmolVLA drop on Goal), confirming that the correction-harms-confident-steps pattern generalizes---and amplifies---on stronger models. A boundary analysis on OpenVLA-OFT~\\cite{kim2024openvla} (7B, deterministic) confirms that stochastic sample diversity is a prerequisite.\n\n\\looseness=-1 The key finding is mechanistic: \\emph{knowing when not to correct} matters more than correction strength. CRM always-on applies the same learned residual to every step, including the ${\\sim}$80--97\\% where the VLA is already confident; corrections on these steps cause up to $-$14.8\\,pp degradation. ACR-VLA's adaptive gate triggers CRM only on high-uncertainty steps, preserving the VLA's own output elsewhere. A threshold sensitivity analysis across three suites (Appendix~\\ref{sec:tau_sweep}) shows that success rate is robust to $\\tau$ choice, establishing gating as a stable design element rather than a fragile hyperparameter.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{Systematic analysis of test-time correction} (Section~\\ref{sec:failure_modes}): under a K-matched design ($K{=}2$, same $\\varepsilon$ and CRM), we show that unconditional correction degrades all four LIBERO suites on SmolVLA ($-$1.3 to $-$14.8\\,pp) and all three evaluated suites on $\\pi_{0.5}$ ($-$2.0 to $-$14.0\\,pp), identifying the 80--97\\% of confident steps as the source of harm.\n  \\item \\textbf{Adaptive gating mechanism} (Section~\\ref{sec:method}): a $K{=}2$ pairwise $L_2$ uncertainty probe ($\\rho{=}0.9979$) gates CRM correction to the 3--20\\% of high-uncertainty steps, recovering all degradation ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp).\n  \\item \\textbf{Cross-VLA validation} (Section~\\ref{sec:cross_vla}): on $\\pi_{0.5}$ (3.6B, 95--98\\% baseline), unconditional correction degrades all three evaluated suites ($-$2.0 to $-$14.0\\,pp), with Goal suffering $3.8{\\times}$ the SmolVLA drop; deterministic VLAs (OpenVLA-OFT) produce near-identical samples that make multi-sample methods vacuous.\n\\end{enumerate}\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
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
Now I have both the style norms and the current introduction. Let me analyze what needs to change:

1. The current intro is pretty good but needs to align with the new narrative: "learned correction is harmful → conformal confidence sets detect when not to correct"
2. The new narrative emphasizes "conformal confidence sets" and "τ-gating" terminology
3. Need 4 contributions instead of 3
4. Need to use the specific data points from the task
5. ~700 words, 5-paragraph structure

Let me draft the new introduction:

Key changes needed:
- Hook: Frozen flow-matching VLAs + post-hoc learned correction is attractive but harmful by default


- Problem: CRM unconditionally applied degrades all four LIBERO suites with measurable performance drops
- Root cause: 80-97% of steps already have high VLA confidence, so corrections introduce noise
- Insight: knowing when not to correct matters more than correction strength itself
- Method: Conformal confidence sets built from K=2 samples using pairwise L2 distance, with threshold τ gating the CRM
- Results: τ-gating recovers all degradation, and Pi0.5 confirms the pattern amplifies
- 4 contributions as specified

Terminology shifts:
- "ACR-VLA" remains the method name but emphasize conformal confidence sets and τ-gating as the core innovation
- "Adaptive" → "τ-gated" to be more precise
- Table 1 columns: "CRM τ-gated"

Now drafting the introduction with constraints: no em-dashes or explanatory en-dashes, no -ing phrase endings, no stacked discourse markers like "Furthermore," no AI blacklist words, approximately 700 words across 5 paragraphs plus contribution list, using \looseness=-1, exact cite keys, avoiding p<0.05 claims, avoiding "significantly" without statistical backing, replacing "no harm" with "near-neutral" or "within measurement noise," and avoiding incomplete phrases like "Don't say 'gener..."

The current intro sits around 580 words, so I need to add roughly 120 more words. My structure: Paragraph 1 covers the appeal of post-hoc correction for frozen VLAs and the surprising finding that it's harmful by default. Paragraph 2 identifies the gap in existing work regarding when correction helps versus hurts. Paragraph 3 analyzes the root cause: CRM applied unconditionally degrades all four suites because 80-97% of steps already have high confidence. Paragraph 4 introduces the method using conformal confidence sets from K=2 samples and τ-gating. I'll need a Paragraph 5 to round out the structure and likely a contributions list. The core narrative is: frozen VLAs can be improved post-hoc, but naive correction hurts performance across all benchmarks because most steps are already confident—so the key insight is knowing when *not* to correct rather than how to correct better. I'm using conformal confidence sets built from K=2 pairwise distances as an uncertainty proxy, then gating the correction with a threshold τ that only applies it to the 3-20% of high-uncertainty steps, which recovers all the degradation and shows the effect amplifies on stronger models. I'm examining the empirical results showing that unconditional correction actually hurts performance across different model scales and task suites, with the core issue being that not every action step requires correction. Then I'm reviewing how recent work like A2C2 and ReconVLA have tackled related problems but haven't fully addressed this fundamental assumption about when correction should be applied.

The key insight is that the VLA is already producing confident, low-variance actions on the vast majority of control steps—80 to 97 percent—so applying corrections indiscriminately just adds noise. Rather than focusing on how well the correction works, the real challenge is determining when to suppress it entirely. I'm constructing confidence sets from just two stochastic action samples in a single forward pass, using their pairwise distance as an uncertainty measure that correlates strongly with actual confidence levels.

I'm implementing a threshold-gating mechanism that only activates the correction module when this distance exceeds a certain value, restricting corrections to the small fraction of steps where the VLA is genuinely uncertain. Testing this approach on SmolVLA across multiple benchmark suites shows that gated correction recovers all the performance losses from always-on correction, with improvements ranging from 2.8 to 14.5 percentage points.

Now I'm validating this pattern across stronger models like π₀.5 and OpenVLA-OFT, where unconditional correction actually hurts performance significantly. The analysis reveals that stochastic sample diversity is essential for confidence estimation, and a sensitivity analysis confirms the approach is robust across different threshold choices. The tau-gating approach recovers all performance losses, and cross-suite validation shows consistent trigger rates and effect sizes across different benchmarks. Meanwhile, the smaller pi_0.5 model shows amplified degradation under unconditional correction compared to SmolVLA, while OpenVLA-OFT's deterministic outputs reveal that stochastic diversity is essential for multi-sample correction methods to be effective. I'm going through the remaining paragraphs to catch any dangling -ing phrases at sentence endings. In P3, I need to rephrase "while adding zero extra latency" to something like "at zero extra latency" to avoid that construction. P4 has a similar issue with "confirming that stochastic sample diversity is" that needs fixing.

I'm also noticing some -ing verbs like "exhibiting" that should become active statements instead—"trigger rate and effect size show monotonic correlation" reads better. Now I'm doing a rough word count across all five paragraphs, estimating around 660 words total, which puts us close to the 700-word target. Finally, I'm scanning for any AI-style language like "leverage" or "utilize" that might slip through, and so far the vocabulary looks appropriately academic. I'm checking that I've included all the necessary citations and need to add the ones I haven't used yet—flow-matching references and multi-sample selection methods—so I'll weave those into the relevant sections about VLA approaches and sampling strategies. I'm seeing the performance degradation across different VLA models and suites, and noting that the core issue isn't the correction module itself but rather applying it indiscriminately to every step. Now I'm reviewing how prior work like A2C2 and ReconVLA have tackled related problems without fully addressing this fundamental failure mode.

The key insight emerging is that the VLA already produces confident, low-variance actions on the vast majority of control steps—80 to 97 percent—so corrections actually introduce noise rather than improve performance. This means the real value lies in knowing when to skip correction entirely rather than optimizing the correction itself. I'm constructing conformal confidence sets from just two stochastic action samples in a single forward pass to measure per-step confidence.

The pairwise distance between these two samples acts as an uncertainty proxy that correlates extremely well with variance computed from ten samples, yet adds no latency overhead. A threshold gates whether correction applies: below the threshold, the pipeline outputs the confident action directly; above it, the residual correction activates. This selective gating restricts correction to only the 3 to 20 percent of steps where genuine uncertainty exists, and across SmolVLA experiments it recovers all the performance lost from always applying correction, with gains ranging from 2.8 to 14.5 percentage points.

Testing on stronger models like π₀.₅ shows the failure pattern intensifies—unconditional correction now degrades performance by 14 percentage points—while analysis of a deterministic baseline reveals that stochastic sample diversity is essential for confidence estimation. A sensitivity sweep across multiple suites confirms the approach is robust to threshold choice, with trigger rates and effect sizes showing consistent patterns.

My key contributions are identifying how unconditional correction harms performance across all evaluated suites by targeting confident steps that shouldn't be corrected, then proposing a gating mechanism using pairwise L₂ distance as an uncertainty proxy that recovers all the lost performance by selectively applying corrections only to the 3-20% of genuinely uncertain steps. I'm catching some awkward participial phrases at the end of sentences that need fixing. Let me go through and convert those -ing endings into proper clauses—changing "recovering all degradation" to "which recovers all degradation" and restructuring "establishing stochastic diversity as a prerequisite" into a separate statement instead of a dangling phrase. I'm noticing that $\pi_{0.5}$ with 3.6B parameters shows severe degradation when applying unconditional correction—a 3.8× drop compared to SmolVLA on the Goal metric. Meanwhile, OpenVLA-OFT at 7B uses deterministic sampling, which produces nearly identical outputs across multiple samples, making multi-sample approaches ineffective. This reveals that stochastic diversity in the model's outputs is actually essential for these methods to work.

Let me verify I haven't left any dangling -ing phrases. The rule specifically targets sentences ending with participial clauses like "achieving 90% accuracy" tacked on as afterthoughts. Phrases like "without modifying the VLA weights" are structural parts of the sentence, not dangling modifiers, so they're acceptable—though I could rephrase to "with no changes to the VLA weights" for extra clarity.

I should also double-check that I'm using the method name correctly. The task notes that ACR-VLA can still appear in the narrative while emphasizing conformal confidence sets and τ-gating, but looking back at my draft, I haven't actually used "ACR-VLA" yet. I should probably incorporate it where appropriate. I need to figure out where to naturally introduce ACR-VLA as the method name while keeping the focus on conformal confidence sets and τ-gating. The table should use "CRM τ-gated" rather than "ACR-VLA", so I'll reserve the full method name for the narrative text, probably in P3 or P4 when describing the τ-gating mechanism itself. I'm working through where to place the citation for test-time compute scaling—it fits better with the multi-sample selection concept in the introduction rather than with VLA-Pilot. Let me revise the opening paragraphs to weave this in naturally: the background establishes flow-matching VLAs and post-hoc correction as appealing but problematic by default, showing how unconditional application degrades performance across suites. Then I'll move into the related work gap and build from there. Writing the introduction... I'm examining how prior work has tackled this problem—A2C2 learns correction heads but applies them unconditionally, ReconVLA quantifies uncertainty without learning residuals, SC-VLA uses reinforcement learning which breaks the weight-frozen constraint, and VLA-Pilot is too slow for real-time control. The key insight is that on 80-97% of steps the VLA is already confident, so the real challenge is knowing when to suppress correction rather than improving the correction itself. I'm using conformal confidence sets built from just two stochastic action samples to measure per-step uncertainty, with the L2 distance between them serving as a proxy for confidence. The experiments on stronger models like π₀.₅ show that unconditional correction actually hurts performance significantly, degrading success by 14 percentage points, while OpenVLA's deterministic outputs reveal that stochastic diversity is essential for the confidence estimation to work. Threshold sensitivity analysis confirms the approach is robust across different settings, with the trigger rate scaling predictably with effect size. Now I'm outlining the key contributions: systematic analysis of when unconditional correction fails, the K-matched experimental design that isolates the correction effect. The cross-suite validation shows consistent trigger rates and effect sizes across different benchmarks, with the gating threshold analysis demonstrating stability. Across different VLA models, smaller models like π₀.₅ show amplified degradation under unconditional correction, while deterministic models like OpenVLA-OFT produce identical samples that make multi-sample approaches ineffective—stochastic diversity turns out to be essential for the method to work. The next thinking is empty, so I'll output nothing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "2297e011-4ba1-42b4-bf3c-2da561fa953c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8Apf8ya7j3sjHhPGYu2dA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 25093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7455
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

Now I have the style norms and current file. Writing the new introduction with the shifted narrative: "learned correction is harmful by default → conformal confidence sets + τ-gating detect when not to correct."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "8beffc6e-5c33-4c1f-b607-a6dd94661e0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8Apf8ya7j3sjHhPGYu2dA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 25093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7455
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

<details open><summary>🔧 Tool call — Write · `toolu_01MXkaDx1UgqdRPypBAGg4Q1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\n\\looseness=-1 Frozen flow-matching Vision-Language-Action (VLA) models can be deployed on new tasks without retraining, but their action quality is bounded by the pretrained policy~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow}. Post-hoc learned correction is an appealing alternative to fine-tuning: a lightweight module trained on task demonstrations can refine actions at inference time with no changes to the VLA weights~\\cite{snell2024scaling}. We systematically evaluate this idea and find that it is harmful by default. A Correction Residual Module (CRM, ${\\sim}$327K parameters) trained on demonstrations and applied unconditionally degrades all four LIBERO suites~\\cite{liu2023libero} on SmolVLA~\\cite{shukor2025smolvla} (0.4B): Long $-$14.8\\,pp, Object $-$4.7\\,pp, Goal $-$3.7\\,pp, and Spatial $-$1.3\\,pp. The same pattern holds on $\\pi_{0.5}$~\\cite{black2025pi05} (3.6B), where unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp on Goal ($3.8{\\times}$ the SmolVLA drop). The problem is not the correction module itself, but the assumption that every control step needs correction.\n\n\\looseness=-1 Recent work addresses parts of this problem space without confronting the core failure mode. A2C2~\\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and targets temporal staleness rather than initial action quality. ReconVLA~\\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\\cite{liu2026scvla} uses reinforcement learning and therefore abandons the weight-frozen constraint. VLA-Pilot~\\cite{li2025vlapilot} performs evolutionary search at $2.41$\\,s per control step, too slow for closed-loop deployment. None analyze when correction helps versus hurts, nor provide a mechanism to suppress correction when the VLA is already confident.\n\n\\looseness=-1 Our analysis reveals the root cause: on 80--97\\% of control steps, the VLA already produces confident, low-variance actions, and corrections applied to these steps inject noise rather than signal. This observation has a direct consequence: knowing \\emph{when not to correct} matters more than the correction's magnitude. To quantify per-step confidence, we construct conformal confidence sets from only $K{=}2$ stochastic action samples drawn in a single batched forward pass. The pairwise $L_2$ distance between these two samples serves as an uncertainty proxy with Spearman $\\rho{=}0.9979$ against $K{=}10$ sample variance, at zero extra latency (${\\sim}$170\\,ms $\\approx$ $K{=}1$). A threshold $\\tau$ on this distance gates the CRM: when distance falls below $\\tau$, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds $\\tau$, the CRM applies a bounded residual. This $\\tau$-gating mechanism forms the core of our method, \\textbf{ACR-VLA}, and restricts correction to the 3--20\\% of steps where the VLA is genuinely uncertain.\n\n\\looseness=-1 On SmolVLA across four LIBERO suites, ACR-VLA's $\\tau$-gated correction recovers all degradation from unconditional CRM ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp over CRM always-on). Cross-VLA experiments on $\\pi_{0.5}$ (3.6B, 95--98\\% baseline) confirm that the failure pattern persists and amplifies on stronger models: unconditional correction degrades Goal by $-$14.0\\,pp. A boundary analysis on OpenVLA-OFT~\\cite{kim2024openvla} (7B, deterministic) shows that 97.3\\% of steps produce $L_2 < 0.01$; stochastic sample diversity is therefore a prerequisite for multi-sample confidence estimation. Threshold sensitivity analysis across three suites (Appendix~\\ref{sec:tau_sweep}) confirms that success rate is robust to $\\tau$ choice, and trigger rate correlates monotonically with effect size across suites.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{Systematic analysis of unconditional correction} (Section~\\ref{sec:failure_modes}): under a K-matched design ($K{=}2$, same $\\varepsilon$ and CRM checkpoint), unconditional correction degrades all four LIBERO suites on SmolVLA ($-$1.3 to $-$14.8\\,pp) and all three evaluated suites on $\\pi_{0.5}$ ($-$2.0 to $-$14.0\\,pp). We identify the 80--97\\% of confident steps as the source of harm.\n  \\item \\textbf{Conformal confidence sets with $\\tau$-gating} (Section~\\ref{sec:method}): $K{=}2$ pairwise $L_2$ distance serves as an uncertainty proxy ($\\rho{=}0.9979$ vs.\\ $K{=}10$ variance) that gates CRM correction to the 3--20\\% of high-uncertainty steps and recovers all degradation ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp).\n  \\item \\textbf{Cross-suite validation} (Section~\\ref{sec:experiments}): trigger rate and effect size show monotonic correlation across suites, and $\\tau$-sweep analysis confirms gating stability across threshold choices.\n  \\item \\textbf{Cross-VLA analysis} (Section~\\ref{sec:cross_vla}): $\\pi_{0.5}$ (3.6B) exhibits amplified degradation under unconditional correction ($3.8{\\times}$ SmolVLA drop on Goal). OpenVLA-OFT (7B, deterministic) produces near-identical samples that render multi-sample methods vacuous; stochastic diversity is a prerequisite.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "ba936d5c-7ea8-4efc-a920-d80c2608780c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8Apf8ya7j3sjHhPGYu2dA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7455,
      "cache_read_input_tokens": 25093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7455
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

_source line 12 · 2026-05-28T04:12:16.731Z_

<details><summary>↩ Tool result · `toolu_01MXkaDx1UgqdRPypBAGg4Q1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "abb825f3-6bdb-4d54-8368-3e8d6ac68f8e",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\n\\looseness=-1 Frozen flow-matching Vision-Language-Action (VLA) models can be deployed on new tasks without retraining, but their action quality is bounded by the pretrained policy~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow}. Post-hoc learned correction is an appealing alternative to fine-tuning: a lightweight module trained on task demonstrations can refine actions at inference time with no changes to the VLA weights~\\cite{snell2024scaling}. We systematically evaluate this idea and find that it is harmful by default. A Correction Residual Module (CRM, ${\\sim}$327K parameters) trained on demonstrations and applied unconditionally degrades all four LIBERO suites~\\cite{liu2023libero} on SmolVLA~\\cite{shukor2025smolvla} (0.4B): Long $-$14.8\\,pp, Object $-$4.7\\,pp, Goal $-$3.7\\,pp, and Spatial $-$1.3\\,pp. The same pattern holds on $\\pi_{0.5}$~\\cite{black2025pi05} (3.6B), where unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp on Goal ($3.8{\\times}$ the SmolVLA drop). The problem is not the correction module itself, but the assumption that every control step needs correction.\n\n\\looseness=-1 Recent work addresses parts of this problem space without confronting the core failure mode. A2C2~\\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and targets temporal staleness rather than initial action quality. ReconVLA~\\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\\cite{liu2026scvla} uses reinforcement learning and therefore abandons the weight-frozen constraint. VLA-Pilot~\\cite{li2025vlapilot} performs evolutionary search at $2.41$\\,s per control step, too slow for closed-loop deployment. None analyze when correction helps versus hurts, nor provide a mechanism to suppress correction when the VLA is already confident.\n\n\\looseness=-1 Our analysis reveals the root cause: on 80--97\\% of control steps, the VLA already produces confident, low-variance actions, and corrections applied to these steps inject noise rather than signal. This observation has a direct consequence: knowing \\emph{when not to correct} matters more than the correction's magnitude. To quantify per-step confidence, we construct conformal confidence sets from only $K{=}2$ stochastic action samples drawn in a single batched forward pass. The pairwise $L_2$ distance between these two samples serves as an uncertainty proxy with Spearman $\\rho{=}0.9979$ against $K{=}10$ sample variance, at zero extra latency (${\\sim}$170\\,ms $\\approx$ $K{=}1$). A threshold $\\tau$ on this distance gates the CRM: when distance falls below $\\tau$, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds $\\tau$, the CRM applies a bounded residual. This $\\tau$-gating mechanism forms the core of our method, \\textbf{ACR-VLA}, and restricts correction to the 3--20\\% of steps where the VLA is genuinely uncertain.\n\n\\looseness=-1 On SmolVLA across four LIBERO suites, ACR-VLA's $\\tau$-gated correction recovers all degradation from unconditional CRM ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp over CRM always-on). Cross-VLA experiments on $\\pi_{0.5}$ (3.6B, 95--98\\% baseline) confirm that the failure pattern persists and amplifies on stronger models: unconditional correction degrades Goal by $-$14.0\\,pp. A boundary analysis on OpenVLA-OFT~\\cite{kim2024openvla} (7B, deterministic) shows that 97.3\\% of steps produce $L_2 < 0.01$; stochastic sample diversity is therefore a prerequisite for multi-sample confidence estimation. Threshold sensitivity analysis across three suites (Appendix~\\ref{sec:tau_sweep}) confirms that success rate is robust to $\\tau$ choice, and trigger rate correlates monotonically with effect size across suites.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{Systematic analysis of unconditional correction} (Section~\\ref{sec:failure_modes}): under a K-matched design ($K{=}2$, same $\\varepsilon$ and CRM checkpoint), unconditional correction degrades all four LIBERO suites on SmolVLA ($-$1.3 to $-$14.8\\,pp) and all three evaluated suites on $\\pi_{0.5}$ ($-$2.0 to $-$14.0\\,pp). We identify the 80--97\\% of confident steps as the source of harm.\n  \\item \\textbf{Conformal confidence sets with $\\tau$-gating} (Section~\\ref{sec:method}): $K{=}2$ pairwise $L_2$ distance serves as an uncertainty proxy ($\\rho{=}0.9979$ vs.\\ $K{=}10$ variance) that gates CRM correction to the 3--20\\% of high-uncertainty steps and recovers all degradation ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp).\n  \\item \\textbf{Cross-suite validation} (Section~\\ref{sec:experiments}): trigger rate and effect size show monotonic correlation across suites, and $\\tau$-sweep analysis confirms gating stability across threshold choices.\n  \\item \\textbf{Cross-VLA analysis} (Section~\\ref{sec:cross_vla}): $\\pi_{0.5}$ (3.6B) exhibits amplified degradation under unconditional correction ($3.8{\\times}$ SmolVLA drop on Goal). OpenVLA-OFT (7B, deterministic) produces near-identical samples that render multi-sample methods vacuous; stochastic diversity is a prerequisite.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 21,
        "newStart": 1,
        "newLines": 18,
        "lines": [
          " \\section{Introduction}",
          " \\label{sec:intro}",
          " ",
          "-\\looseness=-1 Deploying a pretrained Vision-Language-Action (VLA) model on a new task usually requires fine-tuning on task demonstrations, yet collecting that data is expensive and the resulting checkpoint may not transfer further. A more attractive route keeps the VLA frozen and improves action quality at inference time. Flow-matching VLAs~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are well suited to this setting because each forward pass produces a stochastic action sample, enabling multi-sample selection and correction without retraining~\\cite{snell2024scaling}. But does test-time correction always help? We systematically analyze this question and find that it does not: unconditional correction degrades performance on every suite we evaluate, and the key to making correction useful is knowing \\emph{when not} to apply it.",
          "+\\looseness=-1 Frozen flow-matching Vision-Language-Action (VLA) models can be deployed on new tasks without retraining, but their action quality is bounded by the pretrained policy~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow}. Post-hoc learned correction is an appealing alternative to fine-tuning: a lightweight module trained on task demonstrations can refine actions at inference time with no changes to the VLA weights~\\cite{snell2024scaling}. We systematically evaluate this idea and find that it is harmful by default. A Correction Residual Module (CRM, ${\\sim}$327K parameters) trained on demonstrations and applied unconditionally degrades all four LIBERO suites~\\cite{liu2023libero} on SmolVLA~\\cite{shukor2025smolvla} (0.4B): Long $-$14.8\\,pp, Object $-$4.7\\,pp, Goal $-$3.7\\,pp, and Spatial $-$1.3\\,pp. The same pattern holds on $\\pi_{0.5}$~\\cite{black2025pi05} (3.6B), where unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp on Goal ($3.8{\\times}$ the SmolVLA drop). The problem is not the correction module itself, but the assumption that every control step needs correction.",
          " ",
          "-\\looseness=-1 Recent work touches parts of this problem without addressing the fundamental question. A2C2~\\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and addresses temporal staleness rather than initial action quality. ReconVLA~\\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\\cite{liu2026scvla} uses reinforcement learning and therefore does not stay weight-frozen. VLA-Pilot~\\cite{li2025vlapilot} performs evolutionary search at $2.41$\\,s per control step, ruling out closed-loop deployment. None analyze when correction helps versus when it hurts, nor provide a mechanism to abstain from correction on confident steps.",
          "+\\looseness=-1 Recent work addresses parts of this problem space without confronting the core failure mode. A2C2~\\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and targets temporal staleness rather than initial action quality. ReconVLA~\\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\\cite{liu2026scvla} uses reinforcement learning and therefore abandons the weight-frozen constraint. VLA-Pilot~\\cite{li2025vlapilot} performs evolutionary search at $2.41$\\,s per control step, too slow for closed-loop deployment. None analyze when correction helps versus hurts, nor provide a mechanism to suppress correction when the VLA is already confident.",
          " ",
          "-\\looseness=-1 We begin by analyzing the failure mode of unconditional correction. A lightweight Correction Residual Module (CRM, ${\\sim}$327K parameters) trained on demonstration data applies a bounded residual to argmin-selected action samples. Under a K-matched design ($K{=}2$ for both conditions, same $\\varepsilon{=}0.2$ and CRM checkpoint), CRM always-on degrades all four LIBERO suites on SmolVLA~\\cite{shukor2025smolvla} (0.4B): $-$1.3 to $-$14.8\\,pp. The same pattern holds on $\\pi_{0.5}$~\\cite{black2025pi05} (3.6B, 95--98\\% baseline), where unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp. The root cause is that 80--97\\% of control steps are already confident; corrections on these steps inject noise rather than signal.",
          "+\\looseness=-1 Our analysis reveals the root cause: on 80--97\\% of control steps, the VLA already produces confident, low-variance actions, and corrections applied to these steps inject noise rather than signal. This observation has a direct consequence: knowing \\emph{when not to correct} matters more than the correction's magnitude. To quantify per-step confidence, we construct conformal confidence sets from only $K{=}2$ stochastic action samples drawn in a single batched forward pass. The pairwise $L_2$ distance between these two samples serves as an uncertainty proxy with Spearman $\\rho{=}0.9979$ against $K{=}10$ sample variance, at zero extra latency (${\\sim}$170\\,ms $\\approx$ $K{=}1$). A threshold $\\tau$ on this distance gates the CRM: when distance falls below $\\tau$, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds $\\tau$, the CRM applies a bounded residual. This $\\tau$-gating mechanism forms the core of our method, \\textbf{ACR-VLA}, and restricts correction to the 3--20\\% of steps where the VLA is genuinely uncertain.",
          " ",
          "-\\looseness=-1 This analysis motivates \\textbf{ACR-VLA}, an adaptive inference-time pipeline that decides per step whether correction is needed. ACR-VLA draws only $K{=}2$ samples in a single batched forward pass and uses their pairwise $L_2$ distance as a per-step uncertainty probe. This probe is well-calibrated: Spearman $\\rho{=}0.9979$ against $K{=}10$ sample variance, whereas three alternatives all yield $\\rho < 0.16$. When the probe falls below a threshold $\\tau$, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds $\\tau$, the CRM applies a bounded residual. The method is a direct consequence of the analysis: once we identify that correction harms confident steps, gating becomes the natural solution.",
          "+\\looseness=-1 On SmolVLA across four LIBERO suites, ACR-VLA's $\\tau$-gated correction recovers all degradation from unconditional CRM ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp over CRM always-on). Cross-VLA experiments on $\\pi_{0.5}$ (3.6B, 95--98\\% baseline) confirm that the failure pattern persists and amplifies on stronger models: unconditional correction degrades Goal by $-$14.0\\,pp. A boundary analysis on OpenVLA-OFT~\\cite{kim2024openvla} (7B, deterministic) shows that 97.3\\% of steps produce $L_2 < 0.01$; stochastic sample diversity is therefore a prerequisite for multi-sample confidence estimation. Threshold sensitivity analysis across three suites (Appendix~\\ref{sec:tau_sweep}) confirms that success rate is robust to $\\tau$ choice, and trigger rate correlates monotonically with effect size across suites.",
          " ",
          "-\\looseness=-1 On SmolVLA across four LIBERO suites, ACR-VLA's adaptive gate triggers correction only on high-uncertainty steps (3--20\\% of steps), recovering all degradation from unconditional correction: $+$1.5\\,pp on Spatial, $+$1.3\\,pp on Goal, and baseline-preserving on Object and Long. Under the K-matched design, ACR-VLA exceeds CRM always-on on all four suites ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp). On $\\pi_{0.5}$ (3.6B, 95--98\\% baseline), unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp ($3.8{\\times}$ the SmolVLA drop on Goal), confirming that the correction-harms-confident-steps pattern generalizes---and amplifies---on stronger models. A boundary analysis on OpenVLA-OFT~\\cite{kim2024openvla} (7B, deterministic) confirms that stochastic sample diversity is a prerequisite.",
          "-",
          "-\\looseness=-1 The key finding is mechanistic: \\emph{knowing when not to correct} matters more than correction strength. CRM always-on applies the same learned residual to every step, including the ${\\sim}$80--97\\% where the VLA is already confident; corrections on these steps cause up to $-$14.8\\,pp degradation. ACR-VLA's adaptive gate triggers CRM only on high-uncertainty steps, preserving the VLA's own output elsewhere. A threshold sensitivity analysis across three suites (Appendix~\\ref{sec:tau_sweep}) shows that success rate is robust to $\\tau$ choice, establishing gating as a stable design element rather than a fragile hyperparameter.",
          "-",
          " Our contributions are:",
          " \\begin{enumerate}[leftmargin=*,nosep]",
          "-  \\item \\textbf{Systematic analysis of test-time correction} (Section~\\ref{sec:failure_modes}): under a K-matched design ($K{=}2$, same $\\varepsilon$ and CRM), we show that unconditional correction degrades all four LIBERO suites on SmolVLA ($-$1.3 to $-$14.8\\,pp) and all three evaluated suites on $\\pi_{0.5}$ ($-$2.0 to $-$14.0\\,pp), identifying the 80--97\\% of confident steps as the source of harm.",
          "-  \\item \\textbf{Adaptive gating mechanism} (Section~\\ref{sec:method}): a $K{=}2$ pairwise $L_2$ uncertainty probe ($\\rho{=}0.9979$) gates CRM correction to the 3--20\\% of high-uncertainty steps, recovering all degradation ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp).",
          "-  \\item \\textbf{Cross-VLA validation} (Section~\\ref{sec:cross_vla}): on $\\pi_{0.5}$ (3.6B, 95--98\\% baseline), unconditional correction degrades all three evaluated suites ($-$2.0 to $-$14.0\\,pp), with Goal suffering $3.8{\\times}$ the SmolVLA drop; deterministic VLAs (OpenVLA-OFT) produce near-identical samples that make multi-sample methods vacuous.",
          "+  \\item \\textbf{Systematic analysis of unconditional correction} (Section~\\ref{sec:failure_modes}): under a K-matched design ($K{=}2$, same $\\varepsilon$ and CRM checkpoint), unconditional correction degrades all four LIBERO suites on SmolVLA ($-$1.3 to $-$14.8\\,pp) and all three evaluated suites on $\\pi_{0.5}$ ($-$2.0 to $-$14.0\\,pp). We identify the 80--97\\% of confident steps as the source of harm.",
          "+  \\item \\textbf{Conformal confidence sets with $\\tau$-gating} (Section~\\ref{sec:method}): $K{=}2$ pairwise $L_2$ distance serves as an uncertainty proxy ($\\rho{=}0.9979$ vs.\\ $K{=}10$ variance) that gates CRM correction to the 3--20\\% of high-uncertainty steps and recovers all degradation ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp).",
          "+  \\item \\textbf{Cross-suite validation} (Section~\\ref{sec:experiments}): trigger rate and effect size show monotonic correlation across suites, and $\\tau$-sweep analysis confirms gating stability across threshold choices.",
          "+  \\item \\textbf{Cross-VLA analysis} (Section~\\ref{sec:cross_vla}): $\\pi_{0.5}$ (3.6B) exhibits amplified degradation under unconditional correction ($3.8{\\times}$ SmolVLA drop on Goal). OpenVLA-OFT (7B, deterministic) produces near-identical samples that render multi-sample methods vacuous; stochastic diversity is a prerequisite.",
          " \\end{enumerate}"
        ]
      }
    ],
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\n\\looseness=-1 Deploying a pretrained Vision-Language-Action (VLA) model on a new task usually requires fine-tuning on task demonstrations, yet collecting that data is expensive and the resulting checkpoint may not transfer further. A more attractive route keeps the VLA frozen and improves action quality at inference time. Flow-matching VLAs~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} are well suited to this setting because each forward pass produces a stochastic action sample, enabling multi-sample selection and correction without retraining~\\cite{snell2024scaling}. But does test-time correction always help? We systematically analyze this question and find that it does not: unconditional correction degrades performance on every suite we evaluate, and the key to making correction useful is knowing \\emph{when not} to apply it.\n\n\\looseness=-1 Recent work touches parts of this problem without addressing the fundamental question. A2C2~\\cite{a2c2_2025} learns a correction head on action chunks but applies it unconditionally and addresses temporal staleness rather than initial action quality. ReconVLA~\\cite{chen2026reconvla} quantifies uncertainty over frozen VLAs but does not learn a corrective residual. SC-VLA~\\cite{liu2026scvla} uses reinforcement learning and therefore does not stay weight-frozen. VLA-Pilot~\\cite{li2025vlapilot} performs evolutionary search at $2.41$\\,s per control step, ruling out closed-loop deployment. None analyze when correction helps versus when it hurts, nor provide a mechanism to abstain from correction on confident steps.\n\n\\looseness=-1 We begin by analyzing the failure mode of unconditional correction. A lightweight Correction Residual Module (CRM, ${\\sim}$327K parameters) trained on demonstration data applies a bounded residual to argmin-selected action samples. Under a K-matched design ($K{=}2$ for both conditions, same $\\varepsilon{=}0.2$ and CRM checkpoint), CRM always-on degrades all four LIBERO suites on SmolVLA~\\cite{shukor2025smolvla} (0.4B): $-$1.3 to $-$14.8\\,pp. The same pattern holds on $\\pi_{0.5}$~\\cite{black2025pi05} (3.6B, 95--98\\% baseline), where unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp. The root cause is that 80--97\\% of control steps are already confident; corrections on these steps inject noise rather than signal.\n\n\\looseness=-1 This analysis motivates \\textbf{ACR-VLA}, an adaptive inference-time pipeline that decides per step whether correction is needed. ACR-VLA draws only $K{=}2$ samples in a single batched forward pass and uses their pairwise $L_2$ distance as a per-step uncertainty probe. This probe is well-calibrated: Spearman $\\rho{=}0.9979$ against $K{=}10$ sample variance, whereas three alternatives all yield $\\rho < 0.16$. When the probe falls below a threshold $\\tau$, the pipeline outputs the argmin-to-centroid sample directly; when it exceeds $\\tau$, the CRM applies a bounded residual. The method is a direct consequence of the analysis: once we identify that correction harms confident steps, gating becomes the natural solution.\n\n\\looseness=-1 On SmolVLA across four LIBERO suites, ACR-VLA's adaptive gate triggers correction only on high-uncertainty steps (3--20\\% of steps), recovering all degradation from unconditional correction: $+$1.5\\,pp on Spatial, $+$1.3\\,pp on Goal, and baseline-preserving on Object and Long. Under the K-matched design, ACR-VLA exceeds CRM always-on on all four suites ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp). On $\\pi_{0.5}$ (3.6B, 95--98\\% baseline), unconditional correction degrades all three evaluated suites by up to $-$14.0\\,pp ($3.8{\\times}$ the SmolVLA drop on Goal), confirming that the correction-harms-confident-steps pattern generalizes---and amplifies---on stronger models. A boundary analysis on OpenVLA-OFT~\\cite{kim2024openvla} (7B, deterministic) confirms that stochastic sample diversity is a prerequisite.\n\n\\looseness=-1 The key finding is mechanistic: \\emph{knowing when not to correct} matters more than correction strength. CRM always-on applies the same learned residual to every step, including the ${\\sim}$80--97\\% where the VLA is already confident; corrections on these steps cause up to $-$14.8\\,pp degradation. ACR-VLA's adaptive gate triggers CRM only on high-uncertainty steps, preserving the VLA's own output elsewhere. A threshold sensitivity analysis across three suites (Appendix~\\ref{sec:tau_sweep}) shows that success rate is robust to $\\tau$ choice, establishing gating as a stable design element rather than a fragile hyperparameter.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{Systematic analysis of test-time correction} (Section~\\ref{sec:failure_modes}): under a K-matched design ($K{=}2$, same $\\varepsilon$ and CRM), we show that unconditional correction degrades all four LIBERO suites on SmolVLA ($-$1.3 to $-$14.8\\,pp) and all three evaluated suites on $\\pi_{0.5}$ ($-$2.0 to $-$14.0\\,pp), identifying the 80--97\\% of confident steps as the source of harm.\n  \\item \\textbf{Adaptive gating mechanism} (Section~\\ref{sec:method}): a $K{=}2$ pairwise $L_2$ uncertainty probe ($\\rho{=}0.9979$) gates CRM correction to the 3--20\\% of high-uncertainty steps, recovering all degradation ($\\Delta_{\\mathrm{gate}}{=}{+}2.8$ to $+$14.5\\,pp).\n  \\item \\textbf{Cross-VLA validation} (Section~\\ref{sec:cross_vla}): on $\\pi_{0.5}$ (3.6B, 95--98\\% baseline), unconditional correction degrades all three evaluated suites ($-$2.0 to $-$14.0\\,pp), with Goal suffering $3.8{\\times}$ the SmolVLA drop; deterministic VLAs (OpenVLA-OFT) produce near-identical samples that make multi-sample methods vacuous.\n\\end{enumerate}\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 13_

Introduction 已重写完成。主要变更：

- **叙事重心**：从"性能提升"转为"learned correction 默认有害 → conformal confidence sets 检测何时不该修正"
- **术语**："adaptive gating" → "τ-gating"/"conformal gating"，贡献2标题改为 "Conformal confidence sets with τ-gating"
- **结构**：5段（背景+hook → 相关工作gap → 根因分析+方法 → 结果 → 4条贡献）
- **贡献从3→4条**：拆出 cross-suite validation（trigger rate ↔ effect size 单调相关、τ-sweep 稳定性）为独立贡献
- **风格**：无 em-dash，无 -ing 短语结尾，无 AI 风格用词，所有 cite key 已覆盖，~670 words

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "uuid": "e97ea1fd-c6a3-4894-8987-2722d8902c2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfqFBD1D7FAq2LQfA97SzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11023,
      "cache_read_input_tokens": 32548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11023
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

_source line 14_

Introduction 已重写完成。主要变更：

- **叙事重心**：从"性能提升"转为"learned correction 默认有害 → conformal confidence sets 检测何时不该修正"
- **术语**："adaptive gating" → "τ-gating"/"conformal gating"，贡献2标题改为 "Conformal confidence sets with τ-gating"
- **结构**：5段（背景+hook → 相关工作gap → 根因分析+方法 → 结果 → 4条贡献）
- **贡献从3→4条**：拆出 cross-suite validation（trigger rate ↔ effect size 单调相关、τ-sweep 稳定性）为独立贡献
- **风格**：无 em-dash，无 -ing 短语结尾，无 AI 风格用词，所有 cite key 已覆盖，~670 words

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158203,
  "duration_api_ms": 159433,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "7561bcdf-d0b6-478e-98fb-8a9a154c4c20",
  "total_cost_usd": 0.5204485,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 31726,
    "cache_read_input_tokens": 69486,
    "output_tokens": 11390,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31726,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 252,
        "cache_read_input_tokens": 32548,
        "cache_creation_input_tokens": 11023,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 11023
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2558,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002643,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 11390,
      "cacheReadInputTokens": 69486,
      "cacheCreationInputTokens": 31726,
      "webSearchRequests": 0,
      "costUSD": 0.5178055,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "796df687-3247-482c-ab1c-d6a4c5693117"
}
```

</details>

---
