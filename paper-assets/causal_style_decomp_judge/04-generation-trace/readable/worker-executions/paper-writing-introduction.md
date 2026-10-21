# paper writing introduction

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260520T232613.log`
- **Structured JSON:** [`945c17f07dd60fde5211.json`](../../sessions/94/945c17f07dd60fde5211.json)

## Before a recorded user message

33 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
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
  "uuid": "e906b504-4e81-4985-84e1-5cfe1327236a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/memory/"
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
    "resetsAt": 1779335400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f80d69de-9337-4643-8828-b4136730d489",
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and reference materials in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "29e5f1bc-d742-48d2-bf48-681951af0304",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwXrHvARJ8LMD1R93a7tts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
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

<details open><summary>🔧 Tool call — Read · `toolu_01MRGJ1ZziBZeCwK1rKuP8qe`</summary>

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
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "97d22c11-4b58-4f6e-bd08-83edb8b1961e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwXrHvARJ8LMD1R93a7tts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
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

_source line 6 · 2026-05-20T23:26:28.702Z_

<details><summary>↩ Tool result · `toolu_01MRGJ1ZziBZeCwK1rKuP8qe`</summary>

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
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "62b2bfdc-e4a7-4668-ab56-52bd98d00f38",
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

<details open><summary>🔧 Tool call — Read · `toolu_017i8ru46rqFtFpKPjYv1No3`</summary>

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
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "81d5deb0-297a-43c1-bfd8-3ebe479084e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwXrHvARJ8LMD1R93a7tts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
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

_source line 8 · 2026-05-20T23:26:29.574Z_

<details><summary>↩ Tool result · `toolu_017i8ru46rqFtFpKPjYv1No3`</summary>

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
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "3eb52be4-5dd2-43c9-bdce-a905265463ef",
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

<details open><summary>🔧 Tool call — Read · `toolu_01LyeRjcCh2jGjzRhk9NiZT3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/skills/projects/causal_style_decomp_judge/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "d4e380bf-6fe5-4ac4-bb3c-2963ddbb8e64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwXrHvARJ8LMD1R93a7tts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
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

_source line 10 · 2026-05-20T23:26:30.495Z_

<details><summary>↩ Tool result · `toolu_01LyeRjcCh2jGjzRhk9NiZT3`</summary>

```text
1	---
2	name: LLM Judge Style Bias — Writing Patterns
3	description: 从8篇深度精读论文蒸馏的叙事策略、图表设计共识、投稿编排经验
4	type: writing
5	source_papers: 8 deep-read (ICLR/ICML/arXiv 2025-2026)
6	---
7	
8	## 叙事类型分布
9	
10	突破局限型（3/8）最主流：SOS-Bench、Preference Leakage、CASSE。模式="大家都在用X，但X有个被忽视的致命问题"。化繁为简型（2/8）：LC-AlpacaEval、RATE。模式="复杂问题有个优雅的简单解"。统一框架型（2/8）：FairJudge、Soumik。跨界迁移型（1/8）：Counterfactual Rhetorical。**置信度：高。**
11	
12	## 开篇钩子模式
13	
14	**"普遍实践+隐藏风险"钩子**（5/8，主流）：从社区公认的实践（LLM-judge评估/style prompting/合成数据训练）切入，然后揭示隐藏的系统性问题。代表：SOS-Bench"PO方法爆炸增长，都依赖LLM-judge，但judge偏好=对齐吗？"；CASSE"Style prompting无处不在，但没人验证feature独立性假设"。
15	
16	**"具体失败案例"钩子**（1/8）：Figure 1直接展示两个judge判断翻转的案例（FairJudge）。视觉冲击力强但需要有好的失败例子。
17	
18	**可模仿策略**：第一句话锚定社区常识，第二句话用"but"转折引出被忽视的问题。LC-AlpacaEval和SOS-Bench都用此结构。
19	
20	## Intro结构共识
21	
22	**4段结构**（5/8主流）：P1=问题背景 → P2=现有方法局限/Gap → P3=本文方案 → P4=贡献列表。**贡献条数**：3-4条（4条更常见，4/8），名词短语标签开头（Soumik/FairJudge/CASSE/Counterfactual Rhetorical），从概念→方法→验证递进。置信度：高。
23	
24	## Figure 1设计
25	
26	**problem_illustration**（4/8最主流）：对比布局展示"旧方法vs新视角"或"失败案例"。设计元素共识：左右对比布局（4/8）、颜色编码区分类型（5/8）、真实数据/案例（3/8）。
27	
28	**method_overview**（2/8）：多阶段pipeline流程图。适合方法论贡献型论文。
29	
30	**teaser_result**（1/8）：开篇即亮核心数字（LC-AlpacaEval的柱状图）。高风险高收益——数字必须够震撼。
31	
32	**可模仿**：SOS-Bench的Figure 1用概念对比图建立分析框架，后续逐一击破；Preference Leakage用taxonomy流程图一张图定义整个问题空间。置信度：高。
33	
34	## 结果图表共识
35	
36	**主结果图**：line_plot（4/8）和bar_chart（5/8）并列主流。因果效应趋势用line_plot+CI band（RATE, Counterfactual Rhetorical）；多方法比较用grouped bar（Soumik, Preference Leakage）。**Gain突出手法**：置信区间/带（4/8）、直接数值标注（3/8）、颜色对比（4/8）。
37	
38	**交互/矩阵数据**：heatmap（CASSE的12×12矩阵，LC-AlpacaEval的模型对预测）。适合展示dense pairwise关系。
39	
40	**Scatter用于Pareto frontier**（Soumik: cost vs accuracy）或相关性展示（SOS-Bench: style R=0.999）。
41	
42	## 主结果表编排
43	
44	**行轴=methods，列轴=datasets×metrics**（6/8）。行按类别分组（by_category 5/8）：先frontier模型再mid-tier再开源，或先existing再proposed。列按dataset分组（grouped_by_dataset）。
45	
46	**Baseline数量**：3-9个（中位5-6）。**高亮策略**：significance markers（*†）+ bootstrap CIs（3/8）> bold_best（2/8）> color coding（1/8）。趋势：裸bold不够，需要统计检验支撑。
47	
48	**消融表**：full_numbers压倒性主流（7/8），checkmark_grid和delta_from_base罕见（各0-1/8）。领域偏好看到完整数字而非增量。置信度：高。
49	
50	## 图表分工模式
51	
52	**图**：趋势/效应/交互矩阵/pipeline/failure cases。**表**：多方法×多数据集的数字比较/消融数字/回归系数。**附录**：per-model/per-domain完整breakdown、统计检验细节（p-values/chi-squared）、超参数、数据集规格。
53	
54	**Figure-heavy vs Table-heavy**：因果推断方向论文偏figure-heavy（RATE 8图3表），bias分析方向偏table-heavy（SOS-Bench 3图8表，Preference Leakage 7图14表）。
55	
56	## 最值得模仿的叙事技巧
57	
58	1. **给简单方法找深刻理论根基**（LC-AlpacaEval）：用因果图将回归方法升格为causal mediation analysis，reviewer觉得"虽简单但有洞察"。
59	2. **控制干预实验作为"炸弹"**（SOS-Bench）：sarcasm/-96% vs wrong/-13%的对比极具修辞冲击力，比相关性分析更有因果说服力。
60	3. **Running example贯穿全文**（RATE）：用GPT-4o自动纠正拼写错误这个具体例子，从motivation到semi-synthetic实验一以贯之。
61	4. **命名新概念**（CASSE的"alignment tax"，Preference Leakage的"preference leakage"）：给发现起一个memorable名字，增强引用吸引力。
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "cf3a3cf0-9b62-4773-b5b9-2a67c3c92285",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/skills/projects/causal_style_decomp_judge/distilled-writing.skill.md",
      "content": "---\nname: LLM Judge Style Bias — Writing Patterns\ndescription: 从8篇深度精读论文蒸馏的叙事策略、图表设计共识、投稿编排经验\ntype: writing\nsource_papers: 8 deep-read (ICLR/ICML/arXiv 2025-2026)\n---\n\n## 叙事类型分布\n\n突破局限型（3/8）最主流：SOS-Bench、Preference Leakage、CASSE。模式=\"大家都在用X，但X有个被忽视的致命问题\"。化繁为简型（2/8）：LC-AlpacaEval、RATE。模式=\"复杂问题有个优雅的简单解\"。统一框架型（2/8）：FairJudge、Soumik。跨界迁移型（1/8）：Counterfactual Rhetorical。**置信度：高。**\n\n## 开篇钩子模式\n\n**\"普遍实践+隐藏风险\"钩子**（5/8，主流）：从社区公认的实践（LLM-judge评估/style prompting/合成数据训练）切入，然后揭示隐藏的系统性问题。代表：SOS-Bench\"PO方法爆炸增长，都依赖LLM-judge，但judge偏好=对齐吗？\"；CASSE\"Style prompting无处不在，但没人验证feature独立性假设\"。\n\n**\"具体失败案例\"钩子**（1/8）：Figure 1直接展示两个judge判断翻转的案例（FairJudge）。视觉冲击力强但需要有好的失败例子。\n\n**可模仿策略**：第一句话锚定社区常识，第二句话用\"but\"转折引出被忽视的问题。LC-AlpacaEval和SOS-Bench都用此结构。\n\n## Intro结构共识\n\n**4段结构**（5/8主流）：P1=问题背景 → P2=现有方法局限/Gap → P3=本文方案 → P4=贡献列表。**贡献条数**：3-4条（4条更常见，4/8），名词短语标签开头（Soumik/FairJudge/CASSE/Counterfactual Rhetorical），从概念→方法→验证递进。置信度：高。\n\n## Figure 1设计\n\n**problem_illustration**（4/8最主流）：对比布局展示\"旧方法vs新视角\"或\"失败案例\"。设计元素共识：左右对比布局（4/8）、颜色编码区分类型（5/8）、真实数据/案例（3/8）。\n\n**method_overview**（2/8）：多阶段pipeline流程图。适合方法论贡献型论文。\n\n**teaser_result**（1/8）：开篇即亮核心数字（LC-AlpacaEval的柱状图）。高风险高收益——数字必须够震撼。\n\n**可模仿**：SOS-Bench的Figure 1用概念对比图建立分析框架，后续逐一击破；Preference Leakage用taxonomy流程图一张图定义整个问题空间。置信度：高。\n\n## 结果图表共识\n\n**主结果图**：line_plot（4/8）和bar_chart（5/8）并列主流。因果效应趋势用line_plot+CI band（RATE, Counterfactual Rhetorical）；多方法比较用grouped bar（Soumik, Preference Leakage）。**Gain突出手法**：置信区间/带（4/8）、直接数值标注（3/8）、颜色对比（4/8）。\n\n**交互/矩阵数据**：heatmap（CASSE的12×12矩阵，LC-AlpacaEval的模型对预测）。适合展示dense pairwise关系。\n\n**Scatter用于Pareto frontier**（Soumik: cost vs accuracy）或相关性展示（SOS-Bench: style R=0.999）。\n\n## 主结果表编排\n\n**行轴=methods，列轴=datasets×metrics**（6/8）。行按类别分组（by_category 5/8）：先frontier模型再mid-tier再开源，或先existing再proposed。列按dataset分组（grouped_by_dataset）。\n\n**Baseline数量**：3-9个（中位5-6）。**高亮策略**：significance markers（*†）+ bootstrap CIs（3/8）> bold_best（2/8）> color coding（1/8）。趋势：裸bold不够，需要统计检验支撑。\n\n**消融表**：full_numbers压倒性主流（7/8），checkmark_grid和delta_from_base罕见（各0-1/8）。领域偏好看到完整数字而非增量。置信度：高。\n\n## 图表分工模式\n\n**图**：趋势/效应/交互矩阵/pipeline/failure cases。**表**：多方法×多数据集的数字比较/消融数字/回归系数。**附录**：per-model/per-domain完整breakdown、统计检验细节（p-values/chi-squared）、超参数、数据集规格。\n\n**Figure-heavy vs Table-heavy**：因果推断方向论文偏figure-heavy（RATE 8图3表），bias分析方向偏table-heavy（SOS-Bench 3图8表，Preference Leakage 7图14表）。\n\n## 最值得模仿的叙事技巧\n\n1. **给简单方法找深刻理论根基**（LC-AlpacaEval）：用因果图将回归方法升格为causal mediation analysis，reviewer觉得\"虽简单但有洞察\"。\n2. **控制干预实验作为\"炸弹\"**（SOS-Bench）：sarcasm/-96% vs wrong/-13%的对比极具修辞冲击力，比相关性分析更有因果说服力。\n3. **Running example贯穿全文**（RATE）：用GPT-4o自动纠正拼写错误这个具体例子，从motivation到semi-synthetic实验一以贯之。\n4. **命名新概念**（CASSE的\"alignment tax\"，Preference Leakage的\"preference leakage\"）：给发现起一个memorable名字，增强引用吸引力。\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01YBQVyFUGrTwt4MK2qbmcjM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/best/paper.tex",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "13682344-45f6-49d6-ad51-98680f390ef8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwXrHvARJ8LMD1R93a7tts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14179,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14179
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

_source line 12 · 2026-05-20T23:26:31.105Z_

<details><summary>↩ Tool result · `toolu_01YBQVyFUGrTwt4MK2qbmcjM`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{graphicx}
6	\usepackage{amsmath,amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{hyperref}
12	\usepackage{cleveref}
13	\usepackage{natbib}
14	\bibliographystyle{plainnat}
15	
16	\newcommand{\cmark}{\checkmark}
17	
18	\title{Causal Style Decomposition Reveals Systematic Style Bias\\in LLM-as-Judge That Likert Scoring Misses}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	% ============================================================
27	% ABSTRACT
28	% ============================================================
29	\begin{abstract}
30	LLM-as-judge has become critical infrastructure for NLP evaluation and alignment training, yet recent work shows style bias dominates other judge biases.
31	Existing analyses treat style as a monolithic dimension or rely on correlational evidence.
32	We introduce \textbf{Causal Style Decomposition (CSD)}, a black-box, post-hoc framework that generates binary style counterfactuals, verifies content preservation via NLI and BERTScore, and measures causal style bias through position-controlled pairwise comparison.
33	Across 3 judges (GPT-4o, Claude-Sonnet, Gemini-Flash), 3 benchmarks (LLMBar, AlpacaEval, MT-Bench), and 3 style axes (formality, tone, register), CSD detects significant style premiums (mean win rate 66.3\%, $p<0.05$ in 7--9 of 9 judge$\times$benchmark cells for formality).
34	We uncover a systematic \emph{measurement gap}: standard Likert pointwise scoring fails to detect any of these biases (0/9 significant), while pairwise comparison succeeds (7/9 significant)---implying that prior Likert-based studies may systematically underestimate style bias severity.
35	Style bias is axis-dependent: formality (68.4\%) $>$ register (66.3\%) $>$ tone (63.4\%), with lighter models (Gemini-Flash) consistently most susceptible.
36	A scaled replication ($n=500$, $p<10^{-6}$), original-preference control, and rewriter ablation confirm robustness.
37	These findings have direct implications for evaluation methodology: style bias audits should use pairwise comparison, and bias must be assessed per axis rather than as a single ``style'' factor.
38	\end{abstract}
39	
40	% ============================================================
41	% 1. INTRODUCTION
42	% ============================================================
43	\section{Introduction}
44	
45	LLM-as-judge---using large language models to evaluate text quality---has become a cornerstone of NLP evaluation and preference-based alignment training.
46	Systems like AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to rank model outputs, and RLHF pipelines use judge-generated preferences as reward signals.
47	The reliability of these judgments directly affects which models are deemed superior and which behaviors are reinforced during training.
48	
49	Recent studies have established that \emph{style bias} is the dominant source of unreliability in LLM judges.
50	SOS-Bench shows style features explain judge scores with $R=0.999$, far exceeding content features.
51	Preference Leakage demonstrates that surface-level style cues drive 76--92\% of observed preference signals.
52	Yet existing approaches to style bias have critical limitations:
53	(1)~they typically treat style as a single dimension, usually length;
54	(2)~they rely on correlational analyses that cannot establish causation;
55	(3)~population-level corrections (e.g., length-controlled AlpacaEval) cannot diagnose per-instance bias;
56	(4)~no existing method provides black-box, post-hoc, per-axis causal style bias detection.
57	
58	We introduce \textbf{Causal Style Decomposition (CSD)}, a framework that addresses all four gaps.
59	CSD generates binary counterfactual pairs along a single style axis (e.g., formal vs.\ casual), verifies content preservation through NLI entailment and BERTScore, and measures the judge's causal response to the style intervention via position-controlled pairwise comparison.
60	CSD is model-agnostic, requires no access to judge internals, and applies to any style dimension where content-preserving rewriting is feasible.
61	
62	Our experiments yield three main findings:
63	\begin{enumerate}
64	    \item \textbf{C1 (Method Validity):} CSD detects significant causal style bias across 3 judges, 3 benchmarks, and 3 style axes, with formality premium ranging from 60--72\% win rate ($p<0.05$).
65	    \item \textbf{C2 (Measurement Insight):} Standard Likert pointwise scoring \emph{systematically} fails to detect style biases that pairwise comparison reveals. In 7 of 9 judge$\times$benchmark combinations, Likert yields $p>0.10$ while pairwise yields $p<0.05$---a measurement gap with direct implications for evaluation methodology.
66	    \item \textbf{C3 (Axis Dependency):} Style bias is not monolithic. Different axes produce different effect sizes (formality $>$ register $>$ tone), and different judges show different sensitivity profiles (Gemini-Flash consistently strongest, Claude-Sonnet weakest).
67	\end{enumerate}
68	
69	% ============================================================
70	% 2. RELATED WORK
71	% ============================================================
72	\section{Related Work}
73	
74	\paragraph{LLM-as-Judge Bias.}
75	Position bias---the tendency to prefer responses in certain positions---has been extensively studied.
76	More recent work shifts attention to style bias as the dominant factor.
77	SOS-Bench~injects quality defects to measure judge sensitivity to style vs.\ content, finding style overwhelmingly dominant.
78	Preference Leakage~demonstrates that RLHF preference data encode surface-style cues that leak into judge behavior.
79	CASSE~constructs a 12$\times$12 style feature interaction matrix but requires prompt engineering for each feature, creating causal entanglement issues.
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "48f978b7-30c9-4a9f-95bc-606d94a6fd3b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/dream_reports/dream_20260520T211832/best/paper.tex",
      "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\\usepackage{natbib}\n\\bibliographystyle{plainnat}\n\n\\newcommand{\\cmark}{\\checkmark}\n\n\\title{Causal Style Decomposition Reveals Systematic Style Bias\\\\in LLM-as-Judge That Likert Scoring Misses}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nLLM-as-judge has become critical infrastructure for NLP evaluation and alignment training, yet recent work shows style bias dominates other judge biases.\nExisting analyses treat style as a monolithic dimension or rely on correlational evidence.\nWe introduce \\textbf{Causal Style Decomposition (CSD)}, a black-box, post-hoc framework that generates binary style counterfactuals, verifies content preservation via NLI and BERTScore, and measures causal style bias through position-controlled pairwise comparison.\nAcross 3 judges (GPT-4o, Claude-Sonnet, Gemini-Flash), 3 benchmarks (LLMBar, AlpacaEval, MT-Bench), and 3 style axes (formality, tone, register), CSD detects significant style premiums (mean win rate 66.3\\%, $p<0.05$ in 7--9 of 9 judge$\\times$benchmark cells for formality).\nWe uncover a systematic \\emph{measurement gap}: standard Likert pointwise scoring fails to detect any of these biases (0/9 significant), while pairwise comparison succeeds (7/9 significant)---implying that prior Likert-based studies may systematically underestimate style bias severity.\nStyle bias is axis-dependent: formality (68.4\\%) $>$ register (66.3\\%) $>$ tone (63.4\\%), with lighter models (Gemini-Flash) consistently most susceptible.\nA scaled replication ($n=500$, $p<10^{-6}$), original-preference control, and rewriter ablation confirm robustness.\nThese findings have direct implications for evaluation methodology: style bias audits should use pairwise comparison, and bias must be assessed per axis rather than as a single ``style'' factor.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLLM-as-judge---using large language models to evaluate text quality---has become a cornerstone of NLP evaluation and preference-based alignment training.\nSystems like AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to rank model outputs, and RLHF pipelines use judge-generated preferences as reward signals.\nThe reliability of these judgments directly affects which models are deemed superior and which behaviors are reinforced during training.\n\nRecent studies have established that \\emph{style bias} is the dominant source of unreliability in LLM judges.\nSOS-Bench shows style features explain judge scores with $R=0.999$, far exceeding content features.\nPreference Leakage demonstrates that surface-level style cues drive 76--92\\% of observed preference signals.\nYet existing approaches to style bias have critical limitations:\n(1)~they typically treat style as a single dimension, usually length;\n(2)~they rely on correlational analyses that cannot establish causation;\n(3)~population-level corrections (e.g., length-controlled AlpacaEval) cannot diagnose per-instance bias;\n(4)~no existing method provides black-box, post-hoc, per-axis causal style bias detection.\n\nWe introduce \\textbf{Causal Style Decomposition (CSD)}, a framework that addresses all four gaps.\nCSD generates binary counterfactual pairs along a single style axis (e.g., formal vs.\\ casual), verifies content preservation through NLI entailment and BERTScore, and measures the judge's causal response to the style intervention via position-controlled pairwise comparison.\nCSD is model-agnostic, requires no access to judge internals, and applies to any style dimension where content-preserving rewriting is feasible.\n\nOur experiments yield three main findings:\n\\begin{enumerate}\n    \\item \\textbf{C1 (Method Validity):} CSD detects significant causal style bias across 3 judges, 3 benchmarks, and 3 style axes, with formality premium ranging from 60--72\\% win rate ($p<0.05$).\n    \\item \\textbf{C2 (Measurement Insight):} Standard Likert pointwise scoring \\emph{systematically} fails to detect style biases that pairwise comparison reveals. In 7 of 9 judge$\\times$benchmark combinations, Likert yields $p>0.10$ while pairwise yields $p<0.05$---a measurement gap with direct implications for evaluation methodology.\n    \\item \\textbf{C3 (Axis Dependency):} Style bias is not monolithic. Different axes produce different effect sizes (formality $>$ register $>$ tone), and different judges show different sensitivity profiles (Gemini-Flash consistently strongest, Claude-Sonnet weakest).\n\\end{enumerate}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM-as-Judge Bias.}\nPosition bias---the tendency to prefer responses in certain positions---has been extensively studied.\nMore recent work shifts attention to style bias as the dominant factor.\nSOS-Bench~injects quality defects to measure judge sensitivity to style vs.\\ content, finding style overwhelmingly dominant.\nPreference Leakage~demonstrates that RLHF preference data encode surface-style cues that leak into judge behavior.\nCASSE~constructs a 12$\\times$12 style feature interaction matrix but requires prompt engineering for each feature, creating causal entanglement issues.\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 522
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
Now I have all the reference materials. Let me also check if there's an existing introduction.tex file and what the current directory structure looks like.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "c47b85e2-5189-40ca-868f-f1da9e7493ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RnDTaW8Wcuyr7HXR7GeDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15011,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15011
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

Let me check the target directory and any existing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "70451f48-63d2-4737-8681-7c6f2bdfd243",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RnDTaW8Wcuyr7HXR7GeDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15011,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15011
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

<details open><summary>🔧 Tool call — Glob · `toolu_017Qd5EvJsftXkDLvxtua1ZK`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "e59b8279-c1e5-49d6-a9a8-316d3ffd6f5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RnDTaW8Wcuyr7HXR7GeDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15011,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15011
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

_source line 16 · 2026-05-20T23:26:38.080Z_

<details><summary>↩ Tool result · `toolu_017Qd5EvJsftXkDLvxtua1ZK`</summary>

```text
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "326b7876-fc3c-4f96-8bd9-4dc7444a33da",
  "tool_use_result": {
    "filenames": [
      "docs/paper/main.tex"
    ],
    "durationMs": 58,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_0168mFQWhJ7uV5Cg6mk9u8ud`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if sections directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "b73fd29b-010c-4c1c-9255-3a97752eacf7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RnDTaW8Wcuyr7HXR7GeDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15011,
      "cache_read_input_tokens": 26020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15011
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

_source line 18 · 2026-05-20T23:26:39.183Z_

<details><summary>↩ Tool result · `toolu_0168mFQWhJ7uV5Cg6mk9u8ud`</summary>

```text
total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 20 23:23 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 20 23:23 ..
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "2f488ed1-28a2-4bbc-b483-9c4eacacde7c",
  "tool_use_result": {
    "stdout": "total 8\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 20 23:23 .\ndrwxr-xr-x 3 ubuntu ubuntu 4096 May 20 23:23 ..",
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

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The sections directory exists but is empty. Let me also check the main.tex to understand how it's structured and if it uses \input for sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "80bace51-2263-4d8b-bb12-946ce74dc18c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZZ6hgcHsXwNAazBw8HgHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 41031,
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

_source line 20_

Let me check the main.tex structure quickly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "4711d043-5260-406e-9e79-605e83b3da75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZZ6hgcHsXwNAazBw8HgHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 41031,
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_019miaeeiFRJh1fPnikWczfd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "ebabd100-9409-498f-bca9-3f7d38647b49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZZ6hgcHsXwNAazBw8HgHe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 41031,
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

_source line 22 · 2026-05-20T23:26:42.282Z_

<details><summary>↩ Tool result · `toolu_019miaeeiFRJh1fPnikWczfd`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	
17	\title{Causal Style Decomposition Reveals the Likert Blindspot:\\Standard Scoring Underestimates Style Bias in LLM Judges}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{sections/abstract}
25	
26	\input{sections/introduction}
27	
28	% \input{sections/related_work}
29	
30	% \input{sections/method}
31	
32	% \input{sections/experiments}
33	
34	% \input{sections/conclusion}
35	
36	\section*{Limitations}
37	
38	% TODO: Add limitations section
39	
40	\bibliography{references}
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
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "ac4fa85b-1aef-4681-a737-def90a001b36",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\title{Causal Style Decomposition Reveals the Likert Blindspot:\\\\Standard Scoring Underestimates Style Bias in LLM Judges}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\n\\input{sections/introduction}\n\n% \\input{sections/related_work}\n\n% \\input{sections/method}\n\n% \\input{sections/experiments}\n\n% \\input{sections/conclusion}\n\n\\section*{Limitations}\n\n% TODO: Add limitations section\n\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Good. The main.tex uses `\input{sections/introduction}` to include the introduction. I need to write the file at `/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex`.

Now let me carefully craft the Introduction following all the constraints:

**Structure**: 4 paragraphs as specified
**Word count**: 600-800 words
**Hard constraints**: No em-dash, no -ing endings, no consecutive transition words, no blacklisted words, etc.

Let me draft this carefully.
 
Now I'm mapping out the key arguments for each paragraph. The first paragraph establishes that LLM judges are critical infrastructure across evaluation benchmarks and alignment training, with style bias emerging as the dominant source of error. The second paragraph contrasts how style effects dominate in pairwise preference tasks while Likert scales systematically underestimate this phenomenon, citing the SOS-Bench findings and preference leak results.

The next section introduces Causal Style Decomposition as the core methodological contribution—a black-box, post-hoc approach using binary counterfactuals paired with content verification and position-controlled comparisons. I'm highlighting the "Likert Blindspot" phenomenon where the integer ceiling effect causes 64% of counterfactual pairs to show zero difference, then contrasting this with existing approaches like LC-AlpacaEval.

Finally, I'm organizing the contributions as a concise list of 3-4 noun phrases before moving into the LaTeX implementation.

Writing the introduction section... I'm identifying four major limitations in how existing approaches handle style bias: they oversimplify style to a single dimension like length, rely on correlations without establishing causation, apply only population-level corrections that miss individual instances, and lack a general method for detecting per-axis bias in black-box settings. There's also a measurement problem—standard 1-10 Likert scales create a ceiling effect where 64% of test pairs get identical scores, making them insensitive to style changes that pairwise comparisons would catch.

I'm proposing Causal Style Decomposition (CSD), which tackles all four gaps through three stages: generating binary style counterfactuals along single axes, verifying content preservation with NLI and semantic similarity checks, and measuring causal bias through position-controlled pairwise comparison. Since CSD works post-hoc without needing access to the judge's internals, it complements existing methods while offering finer diagnostic granularity. Early results show what I'm calling the Likert Blindspot—on formality data, Likert scoring produces a near-zero treatment effect while pairwise comparison detects meaningful bias. I'm noting that pairwise comparison reveals the formality bias that Likert scoring completely misses—the statistical significance jumps from non-significant (p = 0.332) to highly significant (p = 0.006) with a 69.1% win rate. The final contribution about axis-dependent bias across multiple judges and style axes still needs the full experimental results filled in. I'm checking my paragraph structure—the first one is running short at four sentences, so I should flesh it out a bit. I'm also verifying that all my citations are properly placed: the correlation coefficient, the preference accuracy ranges, and the judgment scores all have their sources attached. The registry data point about the 64% delta doesn't need a citation since it's from the dataset itself.

Looking at my quantitative claims, the ATE improvements and pairwise accuracy figures are sourced from the specific registry experiments. Now I'm reconsidering the overall word count—I'm sitting around 505 words across the four paragraphs, which feels slightly lean. Let me also double-check that my contributions section doesn't introduce anything that wasn't already established in the main paragraphs, and that the opening paragraph actually covers the key points about how judges underpin these benchmarks and training approaches.

I'm also noticing the task specifies 600-800 words, so I should expand strategically. There's an optional practical contribution about using pairwise comparisons for audits and assessing bias per axis rather than as a monolithic factor—I think that's worth including. And I need to verify all first-use abbreviations are expanded: LLM, RLHF, and DPO are already handled, but I should make sure CSD gets its full form when it first appears.

One more thing—I'm catching that the reference paper uses em-dashes, but the task implicitly discourages that style, so I'll stick with more conventional punctuation. Now let me draft the introduction section, aiming for around 700 words total, starting with a stronger opening about LLM judges and their role in evaluation and alignment. evaluation, Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior. The reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced during alignment training. As automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.

Recent work has converged on a striking finding: style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference. Multiple studies show that style features alone explain judge scores with near-perfect correlation, vastly exceeding the explanatory power of content features, with 76–92% of preference signals originating from surface-level style cues rather than substantive quality differences. Yet despite this consensus on severity, existing approaches share critical gaps: they treat style as a single dimension, rely on correlational rather than causal analyses, apply only population-level corrections that can't diagnose individual instances, and lack black-box post-hoc methods for per-axis causal bias detection. A methodological problem compounds this—standard Likert scoring exhibits a ceiling effect where 64% of counterfactual pairs receive identical scores, making the measurement insensitive to style interventions.

I'm proposing Causal Style Decomposition (CSD), a three-stage framework that generates binary style counterfactuals along single axes, verifies content preservation through NLI and semantic similarity checks, and measures causal bias via position-controlled pairwise comparison. Since it requires no judge internals and works post-hoc on any black-box system, it complements population-level approaches while enabling per-instance diagnostics. The experiments reveal a striking pattern I'm calling the Likert Blindspot: on formality data, Likert scoring shows a non-significant effect, but pairwise comparison detects a 69.1% formal win rate with statistical significance—demonstrating how the measurement method itself determines what we can detect about bias.

Now I'm outlining the main contributions: the black-box causal framework for detecting per-axis style bias through counterfactual generation and pairwise comparison, the empirical evidence of the Likert Blindspot showing where pointwise scoring fails but pairwise succeeds, and preliminary findings on how bias varies across different style dimensions.

I'm also noting the practical takeaway that evaluation methodology should shift toward pairwise comparison over Likert scoring and assess bias on a per-axis basis rather than treating style as a monolithic factor.

Let me recount the word distribution across these sections to make sure I'm hitting the target length... Multiple studies consistently show that style features dominate judge assessments—with R² values near perfect and 76-92% of preference signals coming from surface-level cues rather than content quality. Yet despite this agreement on the problem's severity, current approaches fall short in four key ways: they oversimplify style to a single dimension like length, rely on correlations that can't prove causation, apply only population-level corrections that miss individual instances, and lack any black-box method for detecting per-axis causal bias after the fact.

There's also a measurement problem baked into standard Likert scoring—the integer scale from 1 to 10 hits a ceiling effect where 64% of counterfactual pairs get identical scores, making the scale too coarse to detect style interventions that pairwise comparisons would easily catch.

I'm proposing Causal Style Decomposition to tackle all four gaps at once. The framework works in three stages: generating binary style counterfactuals along a single axis, verifying content stays intact through NLI entailment and semantic similarity checks, then measuring causal bias using position-controlled pairwise comparison. Since it requires no access to the judge's internals and works post-hoc, it can apply to any black-box evaluator.

The experiments expose what I'm calling the Likert Blindspot—on formality data, Likert scoring shows a non-significant effect while pairwise comparison detects a clear 69% formal preference. Unlike existing population-level approaches, this method gives me per-instance, multi-axis diagnostics that isolate bias along individual style dimensions.

Now I'm checking the word count and structure for the contributions section—roughly 120 words across four points should fit within the 600-800 word target. I'm also verifying I haven't used em-dashes inappropriately and that en-dashes only appear in numerical ranges as intended.

Looking at the sentence endings, I notice one issue: "rendering the measurement insensitive" is a trailing participial phrase that needs fixing. I'll rewrite it as two separate sentences instead—"On our data, 64% of counterfactual pairs receive identical Likert scores (Δ = 0). This integer ceiling effect makes Likert insensitive to style interventions that pairwise comparison readily detects." That removes the dangling -ing construction while keeping the meaning intact.

I should also catch "enabling finer-grained, per-instance diagnostics"—another -ing phrase that should become "it complements existing population-level approaches and provides finer-grained, per-instance diagnostics."

And "producing the leaderboards" in the earlier section is a trailing participial phrase too. I'll restructure that sentence to eliminate the -ing ending and make the relationship between the leaderboards and their impact more direct. I'm catching a constraint about avoiding sentences that end with -ing phrases, so I need to restructure a few sentences. For the first one, I'll connect the two clauses with "and" instead of using a participial phrase. For the second, I'll break up the structure to avoid the trailing -ing modifier and make the integer ceiling effect more explicit. For the third, I'm starting to revise how I describe the post-hoc application of CSD, but I need to see how that sentence continues. I'm checking the quantitative claims to ensure they're properly sourced—the 64% figure comes from our registry data, and since we're presenting our own experimental results in the paper, those don't need external citations. Let me verify the exact numbers from the task description to make sure I'm being precise with the statistics. I'm setting up the LaTeX references properly—using \citet{} for textual citations where the author is part of the sentence, and \citep{} for parenthetical citations in brackets. Let me verify my citation style is consistent throughout the draft.

Now I need to double-check the structure against the task requirements. The four gaps should be clearly articulated, and P3 needs to address all of them comprehensively. I also want to make sure the statement about style bias being the dominant bias in LLM judges is positioned correctly—the task outline suggests it should appear at the end of P1, but I've moved it to the beginning of P2. Let me reconsider whether that placement aligns with the intended flow.

Actually, moving it to P2's opening works better narratively. P1 establishes why LLM-as-judge matters, then P2 immediately presents the key finding about style bias dominance before diving into the supporting evidence. This creates a stronger transition and helps readers understand the significance of the citations that follow. Since the director confirmed the four-paragraph structure but this reordering improves the logical flow without changing the core content, I'll keep it this way.

Before finalizing, I should verify that the emphasis formatting for "Likert Blindspot" is appropriate for the document.

I'm also checking that contribution 3 has the placeholder text properly italicized as requested.

The draft is around 622 words, which is slightly below the 600-800 target. I could strengthen P1 with another sentence about the stakes, and P3 could benefit from more context on how causal structural decomposition connects to existing causal inference methods.

I'm considering adding a citation to causal inference work in P3 to ground the approach, and I notice I haven't used a few available citations yet. The gap analysis in P2 could mention CASSE's specific limitations more directly.

Let me refine P2 to incorporate concurrent approaches like CASSE and FairJudge, noting their reliance on prompted variation rather than controlled interventions. But I need to be careful not to overload P2 since it already covers the datasets, preference leakage, Soumik's work, the four gaps, and the Likert ceiling effect.

I think the cleanest approach is to mention these recent frameworks right after listing the four gaps—specifically in the context of gap (4) about lacking a black-box post-hoc causal method. So I'd add something like: "Recent multi-feature frameworks such as CASSE and FairJudge begin decomposing style into finer dimensions, but neither provides causal identification of per-axis effects." This strengthens the argument that even newer approaches don't solve the core problem we're addressing. , MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment. Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment. The reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced. As automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.

Recent work has converged on a striking finding: style bias is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference. Multiple studies show that style features alone can explain judge scores with near-perfect accuracy, with 76–92% of preference signals actually coming from surface-level stylistic cues rather than substantive quality differences. However, existing approaches have significant limitations: they typically treat style as a single dimension like length, rely on correlational rather than causal analysis, apply only population-level corrections that miss per-instance bias, and lack black-box post-hoc methods for detecting causal bias across individual dimensions. Newer frameworks are beginning to address these gaps, but the work remains incomplete.

I'm also noticing a methodological issue with how judges score responses: standard integer-scale Likert scoring creates a ceiling effect where 64% of counterfactual pairs receive identical scores, making the scale insensitive to style variations that pairwise comparisons can easily detect. To address all these limitations, I'm proposing Causal Style Decomposition (CSD), which uses causal inference techniques to decompose style into fine-grained dimensions, generate counterfactual examples along single axes while preserving content through NLI entailment and BERTScore filtering, and identify per-axis causal effects in a black-box, post-hoc manner.

The empirical results reveal what I'm calling the "Likert Blindspot"—on formality data, Likert scoring shows a non-significant treatment effect while pairwise comparison detects a significant formal preference of 69.1%, demonstrating that CSD's approach captures style biases that traditional scoring misses. ois2025lc}, which applies a single population-level length regression, CSD decomposes bias along multiple axes with per-instance causal intervention.

Our contributions are as follows: a black-box causal framework for detecting per-axis style bias in LLM judges through binary counterfactual generation and position-controlled pairwise comparison. We've identified the Likert Blindspot phenomenon—empirical evidence that standard pointwise scoring systematically fails to detect style biases that pairwise comparison reveals, with formality bias undetectable by Likert ($p = 0.332$) but significant under pairwise measurement (69.1\%, $p = 0.006$). We also have evidence of axis-dependent bias across multiple judges and style axes, along with practical implications showing that style bias audits should employ pairwise comparison rather than Likert scoring, and bias must be assessed per axis rather than as a single ``style'' factor.

I'm checking the sentence count and word distribution across the paragraphs to make sure everything fits within the page budget while maintaining clarity. I'm checking the transitions across all paragraphs—background flowing into leaderboards, then alignment concerns, stakes, and propagation issues in P1; findings with supporting evidence and gaps in P2; the proposal with mechanism and key results in P3; and the contributions list in P4. Everything connects logically.

I should verify the ACL template includes natbib for citations to work properly, and I'm confirming the contrast with LC-AlpacaEval in the final P3 sentence captures the key distinction: multiple decomposition axes with per-instance causal intervention rather than a single population-level regression. Now I'll write out the file.

One final pass through the constraints: no "novel," "groundbreaking," or "revolutionary"; no consecutive transition words like "Furthermore" or "Moreover"; no forbidden phrases like "delve into," "leverage," "utilize," "a myriad of," or "in the realm of"; and no "It is worth noting that" or "Notably." The draft is clean on all counts.

The four-gap sentence in P2 is long but well-structured with numbered items, which is standard and preferred in academic writing. Let me verify the trailing -ing phrases one more time to make sure everything flows properly. I've finished checking all the sentence endings across the paragraphs and they're all grammatically sound. Now I'm doing a final polish pass on that key sentence in P3 about the Likert Blindspot to make sure it reads smoothly before writing out the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "0cf61870-8b51-40b4-ad90-1b407ee4ccbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKAWK8MJMxmXmjRXrcYT2r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 41432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 24_

Now I'll write the Introduction. Let me draft it carefully following all constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "7af81d7f-0d70-4c0d-8126-42ec39b7ca1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKAWK8MJMxmXmjRXrcYT2r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 41432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 25_

<details open><summary>🔧 Tool call — Write · `toolu_01VkXupm8ETZqAsxgSpFiGCn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
  "content": "\\section{Introduction}\n\nLarge Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.\nSystems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.\nReinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.\nThe reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.\nAs automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.\n\nRecent work has converged on a striking finding: \\emph{style bias} is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference.\n\\citet{murugadoss2025sos} show that style features alone explain judge scores with $R = 0.999$, far exceeding the explanatory power of content features.\n\\citet{li2026preference} demonstrate that 76--92\\% of observed preference signals originate from surface-level style cues rather than substantive quality differences.\n\\citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.\nDespite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \\citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis causal detection.\nRecent multi-feature frameworks such as CASSE \\citep{casse2026concise} and FairJudge \\citep{wang2026fairjudge} begin to decompose style into finer dimensions, but neither provides causal identification of per-axis effects.\nA further methodological concern compounds these limitations: standard Likert pointwise scoring (integer scales from 1 to 10) exhibits a ceiling effect that masks real bias.\nOn our data, 64\\% of counterfactual pairs receive identical Likert scores ($\\Delta = 0$), and this integer ceiling effect leaves Likert insensitive to style interventions that pairwise comparison readily detects.\n\nWe propose Causal Style Decomposition (CSD), a framework that addresses all four gaps.\nDrawing on causal inference methods for text \\citep{veitch2020adapting}, CSD operates in three stages: binary style counterfactual generation along a single axis (e.g., formal vs.\\ casual), content preservation verification through Natural Language Inference (NLI) entailment and BERTScore filtering, and causal bias measurement via position-controlled pairwise comparison.\nBecause CSD requires no access to judge internals and applies post-hoc to any black-box judge, it complements existing population-level approaches and provides finer-grained, per-instance diagnostics.\nOur experiments reveal what we term the \\emph{Likert Blindspot}: on the same formality data, Likert scoring yields a corrected Average Treatment Effect (ATE) of $+0.102$ (Cohen's $d = 0.104$, $p = 0.332$, $n = 88$), a non-significant result, while pairwise comparison shows a formal win rate of 69.1\\% (Wilson CI: $[55.97\\%, 79.72\\%]$, sign test $p = 0.006$, $n = 55$ consistent pairs).\nFigure~\\ref{fig:likert_blindspot} illustrates this divergence.\nUnlike LC-AlpacaEval \\citep{dubois2025lc}, which applies a single population-level length regression, CSD decomposes bias along multiple axes with per-instance causal intervention.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{A black-box causal framework} for detecting per-axis style bias in LLM judges through binary counterfactual generation and position-controlled pairwise comparison (Section~\\ref{sec:method}).\n    \\item \\textbf{The Likert Blindspot phenomenon:} empirical evidence that standard pointwise scoring systematically fails to detect style biases that pairwise comparison reveals, with formality bias undetectable by Likert ($p = 0.332$) but significant under pairwise measurement (69.1\\%, $p = 0.006$) (Section~\\ref{sec:experiments}, Figure~\\ref{fig:likert_blindspot}).\n    \\item \\textbf{Evidence of axis-dependent bias:} \\textit{[to be updated with full experimental results across multiple judges and style axes]}.\n    \\item \\textbf{Practical implications for evaluation methodology:} style bias audits should employ pairwise comparison rather than Likert scoring, and bias must be assessed per axis rather than as a single ``style'' factor (Section~\\ref{sec:discussion}).\n\\end{itemize}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "34085595-4c7f-4342-a61a-b5572b1027fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKAWK8MJMxmXmjRXrcYT2r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 41432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 26 · 2026-05-20T23:30:17.109Z_

<details><summary>↩ Tool result · `toolu_01VkXupm8ETZqAsxgSpFiGCn`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "fda29751-a890-46c5-b351-24338c0e5ad4",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
    "content": "\\section{Introduction}\n\nLarge Language Model (LLM) judges have become central infrastructure for NLP evaluation and preference-based alignment training.\nSystems such as AlpacaEval, MT-Bench, and Chatbot Arena rely on LLM judges to score and rank model outputs, and the resulting leaderboards guide both academic research and industry deployment.\nReinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) pipelines consume judge-generated preferences as reward signals that shape model behavior during alignment.\nThe reliability of these judgments carries direct consequences: it determines which models the community considers superior and which response patterns are reinforced.\nAs automated judges increasingly mediate both evaluation and training, any systematic bias in their assessments propagates through the entire model development pipeline.\n\nRecent work has converged on a striking finding: \\emph{style bias} is the dominant source of unreliability in LLM judges, far outweighing other documented biases such as position or verbosity preference.\n\\citet{murugadoss2025sos} show that style features alone explain judge scores with $R = 0.999$, far exceeding the explanatory power of content features.\n\\citet{li2026preference} demonstrate that 76--92\\% of observed preference signals originate from surface-level style cues rather than substantive quality differences.\n\\citet{soumik2026judging} report bias scores of 0.76--0.92 across five different judges.\nDespite this consensus on severity, existing approaches share four critical gaps: (1)~they treat style as a single dimension, typically reducing it to response length; (2)~they rely on correlational analyses that cannot establish causal direction; (3)~population-level corrections such as length-controlled AlpacaEval \\citep{dubois2025lc} cannot diagnose per-instance bias; and (4)~no existing method provides black-box, post-hoc, per-axis causal detection.\nRecent multi-feature frameworks such as CASSE \\citep{casse2026concise} and FairJudge \\citep{wang2026fairjudge} begin to decompose style into finer dimensions, but neither provides causal identification of per-axis effects.\nA further methodological concern compounds these limitations: standard Likert pointwise scoring (integer scales from 1 to 10) exhibits a ceiling effect that masks real bias.\nOn our data, 64\\% of counterfactual pairs receive identical Likert scores ($\\Delta = 0$), and this integer ceiling effect leaves Likert insensitive to style interventions that pairwise comparison readily detects.\n\nWe propose Causal Style Decomposition (CSD), a framework that addresses all four gaps.\nDrawing on causal inference methods for text \\citep{veitch2020adapting}, CSD operates in three stages: binary style counterfactual generation along a single axis (e.g., formal vs.\\ casual), content preservation verification through Natural Language Inference (NLI) entailment and BERTScore filtering, and causal bias measurement via position-controlled pairwise comparison.\nBecause CSD requires no access to judge internals and applies post-hoc to any black-box judge, it complements existing population-level approaches and provides finer-grained, per-instance diagnostics.\nOur experiments reveal what we term the \\emph{Likert Blindspot}: on the same formality data, Likert scoring yields a corrected Average Treatment Effect (ATE) of $+0.102$ (Cohen's $d = 0.104$, $p = 0.332$, $n = 88$), a non-significant result, while pairwise comparison shows a formal win rate of 69.1\\% (Wilson CI: $[55.97\\%, 79.72\\%]$, sign test $p = 0.006$, $n = 55$ consistent pairs).\nFigure~\\ref{fig:likert_blindspot} illustrates this divergence.\nUnlike LC-AlpacaEval \\citep{dubois2025lc}, which applies a single population-level length regression, CSD decomposes bias along multiple axes with per-instance causal intervention.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{A black-box causal framework} for detecting per-axis style bias in LLM judges through binary counterfactual generation and position-controlled pairwise comparison (Section~\\ref{sec:method}).\n    \\item \\textbf{The Likert Blindspot phenomenon:} empirical evidence that standard pointwise scoring systematically fails to detect style biases that pairwise comparison reveals, with formality bias undetectable by Likert ($p = 0.332$) but significant under pairwise measurement (69.1\\%, $p = 0.006$) (Section~\\ref{sec:experiments}, Figure~\\ref{fig:likert_blindspot}).\n    \\item \\textbf{Evidence of axis-dependent bias:} \\textit{[to be updated with full experimental results across multiple judges and style axes]}.\n    \\item \\textbf{Practical implications for evaluation methodology:} style bias audits should employ pairwise comparison rather than Likert scoring, and bias must be assessed per axis rather than as a single ``style'' factor (Section~\\ref{sec:discussion}).\n\\end{itemize}\n",
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

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "8ea53195-346b-4e6f-84c3-228d979dddef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bFtRpMnafQNbqxYLGfvf3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12507,
      "cache_read_input_tokens": 42069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12507
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

_source line 28_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CZJGb7x1kDrVT2EF4JYEJK`</summary>

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
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "1b6ccbeb-1bc5-4eda-bb73-6e59da0ad983",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bFtRpMnafQNbqxYLGfvf3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12507,
      "cache_read_input_tokens": 42069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12507
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

_source line 29 · 2026-05-20T23:30:26.281Z_

<details><summary>↩ Tool result · `toolu_01CZJGb7x1kDrVT2EF4JYEJK`</summary>

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
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "13abaa6a-b8ae-43af-b2cf-083722f97de2",
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

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01KPHdb1GAMVFtsKBZb4NF1P`</summary>

```json
{
  "name": "introduction_section_v1",
  "type": "paper",
  "description": "Introduction section (v1) for EMNLP 2026 submission. 4-paragraph structure: LLM judge infrastructure → style bias dominance + 4 gaps + Likert ceiling → CSD framework + Likert Blindspot data → contributions list. ~650 words, ACL template.",
  "project": "causal_style_decomp_judge",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
  "tags": [
    "paper",
    "introduction",
    "v1",
    "emnlp2026"
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
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "42436282-61e9-474a-a1e6-e334f9753b1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013an3GDzN32zEe3DTpe7pts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 54576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 31 · 2026-05-20T23:30:32.708Z_

<details><summary>↩ Tool result · `toolu_01KPHdb1GAMVFtsKBZb4NF1P`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_64eb98\", \"name\": \"introduction_section_v1\", \"type\": \"paper\", \"description\": \"Introduction section (v1) for EMNLP 2026 submission. 4-paragraph structure: LLM judge infrastructure → style bias dominance + 4 gaps + Likert ceiling → CSD framework + Likert Blindspot data → contributions list. ~650 words, ACL template.\", \"path\": \"projects/causal_style_decomp_judge/artifacts/_project/paper/introduction.tex\", \"url\": null, \"project\": \"causal_style_decomp_judge\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T23:30:32.549155+00:00\", \"tags\": [\"paper\", \"introduction\", \"v1\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "88d1c9db-e4d7-4f75-8536-6a6fb1afedd5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_64eb98\\\", \\\"name\\\": \\\"introduction_section_v1\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Introduction section (v1) for EMNLP 2026 submission. 4-paragraph structure: LLM judge infrastructure → style bias dominance + 4 gaps + Likert ceiling → CSD framework + Likert Blindspot data → contributions list. ~650 words, ACL template.\\\", \\\"path\\\": \\\"projects/causal_style_decomp_judge/artifacts/_project/paper/introduction.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"causal_style_decomp_judge\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T23:30:32.549155+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"introduction\\\", \\\"v1\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_64eb98\", \"name\": \"introduction_section_v1\", \"type\": \"paper\", \"description\": \"Introduction section (v1) for EMNLP 2026 submission. 4-paragraph structure: LLM judge infrastructure → style bias dominance + 4 gaps + Likert ceiling → CSD framework + Likert Blindspot data → contributions list. ~650 words, ACL template.\", \"path\": \"projects/causal_style_decomp_judge/artifacts/_project/paper/introduction.tex\", \"url\": null, \"project\": \"causal_style_decomp_judge\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T23:30:32.549155+00:00\", \"tags\": [\"paper\", \"introduction\", \"v1\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

Introduction 已写入 `docs/paper/sections/introduction.tex`。

**结构概览：**
- **P1** (5句): LLM judge 作为评估+对齐核心基础设施，bias 传播风险
- **P2** (8句): style bias 主宰地位 (SOS-Bench R=0.999, Preference Leakage 76-92%, Soumik 0.76-0.92) → 4个gap → CASSE/FairJudge仍无因果识别 → Likert整数天花板效应 (64% Δ=0)
- **P3** (6句): CSD三阶段机制 → Likert Blindspot命名 (Likert ATE=+0.102, p=0.332 vs Pairwise 69.1%, p=0.006) → 与LC-AlpacaEval对比
- **P4**: 4条contributions (框架/Blindspot现象/axis-dependent placeholder/实践意义)

**引用使用：** murugadoss2025sos, li2026preference, soumik2026judging, dubois2025lc (×2), casse2026concise, wang2026fairjudge, veitch2020adapting

**Contribution 3** 保留 placeholder 待实验数据填充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "uuid": "dbcc4ba1-892e-4d09-bf41-1ac9661783cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJK5jwHUq9zZBiWkjjuPuU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 55296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 610
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

_source line 33_

Introduction 已写入 `docs/paper/sections/introduction.tex`。

**结构概览：**
- **P1** (5句): LLM judge 作为评估+对齐核心基础设施，bias 传播风险
- **P2** (8句): style bias 主宰地位 (SOS-Bench R=0.999, Preference Leakage 76-92%, Soumik 0.76-0.92) → 4个gap → CASSE/FairJudge仍无因果识别 → Likert整数天花板效应 (64% Δ=0)
- **P3** (6句): CSD三阶段机制 → Likert Blindspot命名 (Likert ATE=+0.102, p=0.332 vs Pairwise 69.1%, p=0.006) → 与LC-AlpacaEval对比
- **P4**: 4条contributions (框架/Blindspot现象/axis-dependent placeholder/实践意义)

**引用使用：** murugadoss2025sos, li2026preference, soumik2026judging, dubois2025lc (×2), casse2026concise, wang2026fairjudge, veitch2020adapting

**Contribution 3** 保留 placeholder 待实验数据填充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 262125,
  "duration_api_ms": 262547,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "f2d2e49f-3402-4ba2-9b34-38aac114dc01",
  "total_cost_usd": 0.7633817499999999,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 44065,
    "cache_read_input_tokens": 272265,
    "output_tokens": 13952,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44065,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 352,
        "cache_read_input_tokens": 55296,
        "cache_creation_input_tokens": 610,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 610
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2903,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002993,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 13952,
      "cacheReadInputTokens": 272265,
      "cacheCreationInputTokens": 44065,
      "webSearchRequests": 0,
      "costUSD": 0.76038875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "125eb3dc-b2d5-4d54-aa29-b424479a39d5"
}
```

</details>

---
