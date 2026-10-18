# paper writing abstract conclusion reframe

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_abstract_conclusion_reframe_20260520T115027.log`
- **Structured JSON:** [`1938a3dd8dd70b2fc0de.json`](../../sessions/19/1938a3dd8dd70b2fc0de.json)

## Before a recorded user message

24 recorded events

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
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
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
  "uuid": "649d5900-7c6c-44c4-94c4-9bcf5557d6df",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779286800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a78fe7b3-f226-41c1-9f7f-642edca73627",
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60"
}
```

---

### Assistant

_source line 4_

I'll start by reading the paper-writing-norms skill and the existing files I need to reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "44d47a8a-67fe-4e7b-a550-8051da5e61c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3m6V7E9EEjoEhQ4YDKvad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
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

<details open><summary>🔧 Tool call — Read · `toolu_014VJqeWyxVakH2Z3YMg3JXH`</summary>

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
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "c3363f54-f810-4b2e-aae5-f145e9dba4ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3m6V7E9EEjoEhQ4YDKvad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
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

_source line 6 · 2026-05-20T11:50:41.424Z_

<details><summary>↩ Tool result · `toolu_014VJqeWyxVakH2Z3YMg3JXH`</summary>

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
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "60945995-0322-44fa-9be7-80a6e5e4edc0",
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

<details open><summary>🔧 Tool call — Read · `toolu_01XLNJrWXiQMHHhJqqAjSZCe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "d1602757-1815-4935-9496-9db17c8516c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3m6V7E9EEjoEhQ4YDKvad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
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

_source line 8 · 2026-05-20T11:50:42.828Z_

<details><summary>↩ Tool result · `toolu_01XLNJrWXiQMHHhJqqAjSZCe`</summary>

```text
1	\begin{abstract}
2	Vision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\% to 0\% on the official checkpoint, even at 5\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\% SR at 75\% token reduction where all deletion methods yield 0\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "c37b227f-2fa3-47e6-bf9c-a8cb48f754e1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nVision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\\% to 0\\% on the official checkpoint, even at 5\\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\\% SR at 75\\% token reduction where all deletion methods yield 0\\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01TaAynfGhYf1zhjnMRmMjkZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "d1a5f06a-ffd5-49b2-959b-88437a29af08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3m6V7E9EEjoEhQ4YDKvad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
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

_source line 10 · 2026-05-20T11:50:43.780Z_

<details><summary>↩ Tool result · `toolu_01TaAynfGhYf1zhjnMRmMjkZ`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\% $\to$ 0\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\% $\to$ 37.4\%). The attention entropy ratio (0.95 vs.\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\% to 60--63\% at 75\% token reduction, where all deletion methods yield 0\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "c5c32d31-ed15-4e92-9a94-2e80600af2ad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\\% $\\to$ 0\\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\\% $\\to$ 37.4\\%). The attention entropy ratio (0.95 vs.\\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\\% to 60--63\\% at 75\\% token reduction, where all deletion methods yield 0\\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_015jaTn8nRaGe8VuGjwFNVsK`</summary>

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
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "4715d88d-f635-41c2-8c8e-75fa00460bfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3m6V7E9EEjoEhQ4YDKvad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
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

_source line 12 · 2026-05-20T11:50:44.637Z_

<details><summary>↩ Tool result · `toolu_015jaTn8nRaGe8VuGjwFNVsK`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision token pruning is among the most reliable efficiency techniques for Vision Transformers: DynamicViT~\cite{rao2021dynamicvit} removes 66\% of tokens with $<$0.5\% accuracy loss, ToMe~\cite{bolya2023tome} merges 40\% at $>$99\% accuracy, and EViT~\cite{liang2022evit} discards 50\% with negligible degradation. Vision-Language-Action (VLA) models~\cite{brohan2023rt1,brohan2023rt2,kim2024openvla,black2024pi0,ghosh2024octo,shukor2025smolvla} use the same ViT encoders, producing hundreds of tokens that dominate the LLM backbone's input. For real-time robotic control at 5--10\,Hz, reducing these tokens would directly accelerate the quadratic attention computation. Several recent works explore this direction~\cite{chen2024fastv,xu2025vlacache,cheng2026vlaiap}, but they share an untested assumption: that pruning behaves consistently across VLA architectures.
5	
6	VLAs differ in a critical component, the vision connector that transforms ViT patches into tokens for the language backbone. Pixel-shuffle connectors~\cite{shukor2025smolvla,chen2024internvl} fold spatial patches via channel concatenation; MLP projectors~\cite{liu2023llava,kim2024openvla} map each patch independently; linear projections pass each patch through directly. No prior work has systematically tested how these connector designs affect pruning sensitivity in closed-loop robotic control, where a single wrong action compounds irrecoverably.
7	
8	We conduct the first cross-architecture study of vision token pruning across five VLA models (450M--7B parameters) spanning three connector families. The results reveal a spectrum governed by effective vision-to-LLM pipeline complexity. $\pi_0$~\cite{black2024pi0} (linear projection, 3.3B): offline action loss \emph{improves} by 2.4\% at 90\% token removal. X-VLA~\cite{zheng2025xvla} (linear projection + BART encoder~\cite{lewis2020bart}, 880M): robust at $k \geq 0.9$ (97.6\% SR), then drops to 56.2\% at $k{=}0.7$. OpenVLA~\cite{kim2024openvla} (MLP projector, 7B): graded degradation, 74.0\% $\to$ 37.4\% SR at 50\% removal. SmolVLA~\cite{shukor2025smolvla} (pixel-shuffle, 450M): catastrophic collapse to 0\% SR when just 5\% of tokens are removed. Token importance CV predicts this ordering continuously (0.038 $\to$ 0.151 $\to$ 0.215 $\to$ 0.314). A controlled comparison between $\pi_0$ and OpenVLA (both 256 SigLIP~\cite{zhai2023siglip} tokens) isolates the connector as causal: same token count, same encoder lineage, 63\,pp gap at $k{=}0.1$.
9	
10	For vulnerable architectures, we propose Vision Token Re-encoder (VTR): a lightweight module that re-encodes rather than deletes tokens. At 75\% compression on SmolVLA, VTR recovers 60.1\% SR where all deletion methods yield 0\%. A parameter-matched MLP adapter achieves 63.4\% ($p = 0.15$), which confirms that re-encoding itself, not a specific attention mechanism, is the causal factor.
11	
12	Our contributions:
13	\begin{enumerate}[leftmargin=*,nosep]
14	\item \textbf{Architecture-dependent compressibility taxonomy} (\S\ref{sec:results}): Five models across three connector families reveal that effective pipeline complexity, not model scale, determines pruning tolerance.
15	\item \textbf{CV as continuous diagnostic} (\S\ref{sec:pixel_shuffle}, \S\ref{sec:diagnostic}): Token importance heterogeneity predicts degradation onset from a single forward pass.
16	\item \textbf{VTR re-encoding overcomes cliff-edge failure} (\S\ref{sec:smart_compress_results}, \S\ref{sec:learned_compression}): 0\% $\to$ 60\%+ SR at 75\% compression; the M-curve is flat ($M{=}16 \approx M{=}128$).
17	\item \textbf{Offline metric disconnect} (\S\ref{sec:metric_disconnect}): Standard offline proxies underestimate closed-loop failure severity.
18	\end{enumerate}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "f58b1af1-d00a-4d72-8f31-c92a4aab3ae3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision token pruning is among the most reliable efficiency techniques for Vision Transformers: DynamicViT~\\cite{rao2021dynamicvit} removes 66\\% of tokens with $<$0.5\\% accuracy loss, ToMe~\\cite{bolya2023tome} merges 40\\% at $>$99\\% accuracy, and EViT~\\cite{liang2022evit} discards 50\\% with negligible degradation. Vision-Language-Action (VLA) models~\\cite{brohan2023rt1,brohan2023rt2,kim2024openvla,black2024pi0,ghosh2024octo,shukor2025smolvla} use the same ViT encoders, producing hundreds of tokens that dominate the LLM backbone's input. For real-time robotic control at 5--10\\,Hz, reducing these tokens would directly accelerate the quadratic attention computation. Several recent works explore this direction~\\cite{chen2024fastv,xu2025vlacache,cheng2026vlaiap}, but they share an untested assumption: that pruning behaves consistently across VLA architectures.\n\nVLAs differ in a critical component, the vision connector that transforms ViT patches into tokens for the language backbone. Pixel-shuffle connectors~\\cite{shukor2025smolvla,chen2024internvl} fold spatial patches via channel concatenation; MLP projectors~\\cite{liu2023llava,kim2024openvla} map each patch independently; linear projections pass each patch through directly. No prior work has systematically tested how these connector designs affect pruning sensitivity in closed-loop robotic control, where a single wrong action compounds irrecoverably.\n\nWe conduct the first cross-architecture study of vision token pruning across five VLA models (450M--7B parameters) spanning three connector families. The results reveal a spectrum governed by effective vision-to-LLM pipeline complexity. $\\pi_0$~\\cite{black2024pi0} (linear projection, 3.3B): offline action loss \\emph{improves} by 2.4\\% at 90\\% token removal. X-VLA~\\cite{zheng2025xvla} (linear projection + BART encoder~\\cite{lewis2020bart}, 880M): robust at $k \\geq 0.9$ (97.6\\% SR), then drops to 56.2\\% at $k{=}0.7$. OpenVLA~\\cite{kim2024openvla} (MLP projector, 7B): graded degradation, 74.0\\% $\\to$ 37.4\\% SR at 50\\% removal. SmolVLA~\\cite{shukor2025smolvla} (pixel-shuffle, 450M): catastrophic collapse to 0\\% SR when just 5\\% of tokens are removed. Token importance CV predicts this ordering continuously (0.038 $\\to$ 0.151 $\\to$ 0.215 $\\to$ 0.314). A controlled comparison between $\\pi_0$ and OpenVLA (both 256 SigLIP~\\cite{zhai2023siglip} tokens) isolates the connector as causal: same token count, same encoder lineage, 63\\,pp gap at $k{=}0.1$.\n\nFor vulnerable architectures, we propose Vision Token Re-encoder (VTR): a lightweight module that re-encodes rather than deletes tokens. At 75\\% compression on SmolVLA, VTR recovers 60.1\\% SR where all deletion methods yield 0\\%. A parameter-matched MLP adapter achieves 63.4\\% ($p = 0.15$), which confirms that re-encoding itself, not a specific attention mechanism, is the causal factor.\n\nOur contributions:\n\\begin{enumerate}[leftmargin=*,nosep]\n\\item \\textbf{Architecture-dependent compressibility taxonomy} (\\S\\ref{sec:results}): Five models across three connector families reveal that effective pipeline complexity, not model scale, determines pruning tolerance.\n\\item \\textbf{CV as continuous diagnostic} (\\S\\ref{sec:pixel_shuffle}, \\S\\ref{sec:diagnostic}): Token importance heterogeneity predicts degradation onset from a single forward pass.\n\\item \\textbf{VTR re-encoding overcomes cliff-edge failure} (\\S\\ref{sec:smart_compress_results}, \\S\\ref{sec:learned_compression}): 0\\% $\\to$ 60\\%+ SR at 75\\% compression; the M-curve is flat ($M{=}16 \\approx M{=}128$).\n\\item \\textbf{Offline metric disconnect} (\\S\\ref{sec:metric_disconnect}): Standard offline proxies underestimate closed-loop failure severity.\n\\end{enumerate}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01QNf14bY47gkEhJVFHDnANk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "fffc4b04-5dfd-4265-8952-0974a11eff22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3m6V7E9EEjoEhQ4YDKvad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
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

_source line 14 · 2026-05-20T11:50:44.830Z_

<details><summary>↩ Tool result · `toolu_01QNf14bY47gkEhJVFHDnANk`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across five VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates include Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} summarizes the five models and their pruning responses. The effective vision-to-LLM pipeline complexity, rather than the nominal connector label, determines pruning tolerance. A pure linear projection ($\pi_0$) is immune; a linear projection followed by a deep encoder (X-VLA) is threshold-graded (robust above a retention threshold, then graded decline); a multi-layer MLP degrades smoothly; and pixel-shuffle collapses catastrophically. Token importance heterogeneity (CV) tracks this ordering continuously: 0.038, 0.151, 0.215, 0.314. The pattern holds across a 16$\times$ range in model size (450M to 7B parameters), which suggests scale alone does not explain it.
10	
11	A controlled comparison isolates the vision-to-LLM pipeline as the causal factor. $\pi_0$ and OpenVLA share the same token count (256), the same vision encoder lineage (SigLIP~\cite{zhai2023siglip}), and differ only in the connector: linear projection versus 3-layer MLP. At $k{=}0.1$ (retaining 10\% of tokens), $\pi_0$'s action loss \emph{improves} by 2.4\% while OpenVLA's degrades by 61\%. This 63-percentage-point gap is attributable to pipeline architecture alone. X-VLA's threshold-graded pattern (robust at $k \geq 0.9$, then degradation at $k{=}0.7$) further demonstrates that the \emph{effective} pipeline complexity---not just the connector label---determines pruning tolerance (Section~\ref{sec:linear_results}). OFT~\cite{kim2025openoft}, which replaces OpenVLA's action head but retains its 3-layer MLP connector, produces nearly identical attention entropy (0.667 vs.\ 0.661 for standard OpenVLA). The connector, not the action head, determines the attention structure that governs token dispensability.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\caption{Five-model connector taxonomy. $^\dagger\pi_0$ reports offline normalized L1 action loss (pending closed-loop evaluation). $^\ddagger$X-VLA uses a linear projection followed by a 12-layer BART encoder; the effective pipeline is not purely linear. $^\S$OFT reports attention entropy only (no pruning evaluation); entropy match with standard OpenVLA confirms the connector determines attention structure.}
17	\label{tab:taxonomy}
18	\begin{tabular}{llcrll}
19	\toprule
20	Model & Connector & Params & Tokens & Representative Result & Class \\
21	\midrule
22	$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Immune (offline) \\
23	X-VLA~\cite{zheng2025xvla} & Linear proj$^\ddagger$ & 880M & 50 & $k{=}0.9$: 97.6\%, $k{=}0.7$: 56.2\% & Thresh.-graded \\
24	OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
25	OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & Ent.\ $0.667 \approx 0.661$ (Std)$^\S$ & Smooth graded \\
26	SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	\subsection{Pixel-Shuffle: Catastrophic Cliff-Edge}
32	\label{sec:smolvla_results}
33	
34	The SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result is 87.3\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Table~\ref{tab:smolvla_ablation} reports the full ablation. Every pruning configuration produces 0\% SR (Wilson CI upper bounds $\leq$0.80\%). Three observations make this result striking: (1)~\textbf{Scoring-independent}: random selection performs identically to learned ACIS scoring. (2)~\textbf{Ratio-independent}: retaining 95\% of tokens ($k{=}0.95$, removing only 7 of 128) causes the same failure as retaining 50\%. (3)~\textbf{Mechanism-independent}: zero-masking, true removal, and token merging all produce 0\% SR.
35	
36	\begin{table}[t]
37	\centering
38	\small
39	\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\% SR. The official checkpoint (59.2\% baseline) shows the same cliff-edge.}
40	\label{tab:smolvla_ablation}
41	\begin{tabular}{llccrr}
42	\toprule
43	Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
44	\midrule
45	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\
46	\midrule
47	ACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
48	ACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
49	ACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
50	Random & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
51	Random & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
52	ACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\
53	ACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\
54	\midrule
55	\multicolumn{6}{l}{\textit{Official checkpoint (HuggingFaceVLA/smolvla\_libero)}} \\
56	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\
57	Random & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	The official SmolVLA checkpoint (59.2\% SR, CI [54.8\%, 63.4\%]) exhibits identical failure under 50\% random pruning (0/500), which confirms the cliff-edge is architectural rather than checkpoint-specific. The pattern generalizes across task suites: on LIBERO-Spatial, the official checkpoint (43.8\% SR) collapses to 0.6\% (3/500) under pruning,\footnote{The 3 successes occur on 2 of 10 tasks; the remaining 8 tasks produce 0/50.} and on LIBERO-Goal (63.0\% baseline) pruning yields 0\%.
63	
64	\subsection{MLP Projector: Graded Degradation}
65	\label{sec:openvla_results}
66	
67	Under random token removal, OpenVLA degrades gracefully across all retention ratios: 69.4\% SR at $k{=}0.95$ ($-4.6$pp from the 74.0\% baseline), 62.0\% at $k{=}0.90$, 49.0\% at $k{=}0.70$, 37.4\% at $k{=}0.50$, and 20.6\% at $k{=}0.30$ (Figure~\ref{fig:results_combined}a; full results with CIs in Table~\ref{tab:openvla_full}, Appendix). At $k{=}0.30$, two tasks (cream\_cheese, butter) reach 0\% SR, but eight retain non-zero performance: degradation is graded, not cliff-edge. Per-task breakdowns are in Appendix~\ref{app:per_task}. Random token removal provides a conservative lower bound on architectural resilience; learned scoring methods would likely yield better retention.
68	
69	OFT~\cite{kim2025openoft} strengthens the connector-centric explanation. OFT replaces OpenVLA's autoregressive action head with an optimized fine-tuning strategy but retains the same 3-layer MLP connector. Its attention entropy (0.667) is within 1\% of standard OpenVLA (0.661), which confirms that the connector determines the attention structure governing token importance, independent of the action head. Results from EfficientVLA~\cite{yang2025efficientvla} corroborate the graded pattern on a related architecture: CogACT~\cite{li2024cogact}, which also uses an MLP projector, retains 74.2\% SR (from 74.8\% baseline) under 78\% token pruning.
70	
71	\subsection{Linear Projection: From Immune to Threshold-Graded}
72	\label{sec:linear_results}
73	
74	$\pi_0$~\cite{black2024pi0} (3.3B parameters, 256 tokens, linear projection) uses a flow matching action head~\cite{lipman2023flow}; we evaluate pruning robustness via offline normalized L1 action loss rather than LIBERO success rate.\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation, where errors compound, may reveal additional degradation. We report offline results as preliminary evidence pending live evaluation. X-VLA's offline-to-closed-loop gap (offline near-immune at $k{=}0.3$, closed-loop cliff at $k{=}0.7$; Section~\ref{sec:metric_disconnect}) underscores the need for live verification.} At $k{=}0.1$ (retaining only 10\% of tokens), the normalized loss is 0.976, a 2.4\% \emph{improvement} over the unpruned baseline ($\mathcal{L}_1 < 1.0$ indicates lower loss than the full-token reference). At $k{=}0.5$ the loss remains 0.983. Token removal at these ratios does not degrade offline action prediction quality, though closed-loop validation is pending.
75	
76	X-VLA~\cite{zheng2025xvla} (880M parameters, 50 tokens) is nominally a linear projection model but routes vision tokens through a 12-layer BART encoder~\cite{lewis2020bart} before the LLM, creating a more complex effective pipeline. The baseline achieves 99.2\% SR (496/500). At $k{=}0.95$ SR remains 99.0\% ($-0.2$pp), and at $k{=}0.9$ it holds at 97.6\% ($-1.6$pp). However, at $k{=}0.7$ SR drops to 56.2\% (281/500), a 43-percentage-point cliff from $k{=}0.9$. X-VLA thus exhibits a threshold-graded pattern: robust under mild pruning ($k \geq 0.9$), then a sharp onset of degradation when 30\% of tokens are removed. This pattern differs from both $\pi_0$'s offline immunity and OpenVLA's smooth degradation (49.0\% at $k{=}0.7$). The BART encoder introduces cross-token mixing that creates partial dependencies (CV $= 0.151$, between $\pi_0$'s 0.038 and OpenVLA's 0.215), explaining the intermediate onset point.
77	
78	The $\pi_0$--X-VLA contrast within the nominal ``linear projection'' class demonstrates that the connector label alone is insufficient: the effective vision-to-LLM pipeline complexity determines pruning tolerance. $\pi_0$'s single linear layer preserves full token independence (CV $= 0.038$), while X-VLA's BART encoder introduces enough cross-token structure to shift the degradation onset inward.
79	
80	The controlled comparison between $\pi_0$ and OpenVLA remains the strongest evidence for connector-determined compressibility. Both use 256 vision tokens from a SigLIP~\cite{zhai2023siglip} encoder; they differ only in the connector (linear projection vs.\ 3-layer MLP). At $k{=}0.1$, $\pi_0$ improves by 2.4\% while OpenVLA degrades by 61\%. With token count, encoder architecture, and pruning protocol held constant, the 63-percentage-point gap is attributable to the connector alone.
81	
82	\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}
83	\label{sec:smart_compress_results}
84	
85	To test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\% SR ($p > 0.9$ vs.\ the 44.8\% baseline), which confirms the gain is architectural, not from additional optimization steps.\footnote{The extended baseline also collapses to 0\% SR under pruning ($k{=}0.50$, random, true removal), which confirms that additional training does not mitigate the pixel-shuffle vulnerability.}
86	
87	\begin{table}[t]
88	\centering
89	\small
90	\caption{VTR re-encoding vs.\ deletion on SmolVLA (LIBERO-Object). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (no compression) within 1.1pp. A parameter-matched MLP adapter achieves comparable SR ($p = 0.15$ vs.\ cross-attention). $^\ddagger$Mean $\pm$ std over 3 seeds (500 episodes each). Other rows: single seed with Wilson 95\% CI.}
91	\label{tab:smart_compress}
92	\begin{tabular}{lccrr}
93	\toprule
94	Method & $M$ & Red. & SR (\%) & Seeds \\
95	\midrule
96	\textit{Baseline} & 128 & 0\% & 44.8 & 1 \\
97	\textit{Ext.\ training} & -- & -- & 45.0 & 1 \\
98	\textit{Hard pruning} & -- & 50--90\% & 0.0 & mult. \\
99	\midrule
100	Cross-attn$^\ddagger$ & 16 & 87.5\% & 56.9$\pm$1.3 & 55.8/58.4/56.5 \\
101	Cross-attn$^\ddagger$ & 32 & 75\% & 60.1$\pm$1.3 & 61.6/59.2/59.6 \\
102	Cross-attn$^\ddagger$ & 64 & 50\% & \textbf{62.0}$\pm$2.3 & 61.6/60.0/64.4 \\
103	Cross-attn$^\ddagger$ & 96 & 25\% & 54.5$\pm$3.2 & 52.6/58.2/52.8 \\
104	Cross-attn$^\ddagger$ & 128 & 0\% & 58.0$\pm$3.5 & 59.8/54.0/60.2 \\
105	MLP adapter$^\ddagger$ & 32 & 75\% & 63.4$\pm$2.6 & 65.2/64.6/60.4 \\
106	\midrule
107	\multicolumn{5}{l}{\textit{Official checkpoint (59.2\% baseline)}} \\
108	Cross-attn & 32 & 75\% & 53.4 & 1 \\
109	\bottomrule
110	\end{tabular}
111	\end{table}
112	
113	Table~\ref{tab:smart_compress} reports the full comparison across five compression levels, all with three seeds. The M-curve is flat: $M{=}16$ (56.9\% $\pm$ 1.3, 87.5\% compression) performs within 1.1pp of $M{=}128$ (58.0\% $\pm$ 3.5, no compression). All five $M$ values cluster within a 5pp band, and pairwise comparisons among $M \in \{32, 64, 128\}$ yield $p > 0.25$. VTR achieves near-lossless compression at any ratio for the pixel-shuffle connector. The best absolute SR is $M{=}64$ (62.0\% $\pm$ 2.3) at 50\% compression.
114	
115	A parameter-matched MLP adapter (22.14M parameters, 3-layer, expansion ratio 4) achieves 63.4\% $\pm$ 2.6 SR at $M{=}32$, statistically indistinguishable from the cross-attention result (two-sample $t$-test, $p = 0.15$). Both architectures recover from 0\% to $\sim$60--63\% (Figure~\ref{fig:results_combined}b): the re-encoding principle, not a specific attention mechanism, is the causal factor.
116	
117	Cross-suite evaluation confirms generalization beyond LIBERO-Object. At $M{=}32$, VTR achieves 53.2\% SR on LIBERO-Spatial (vs.\ 0.6\% under hard pruning) and 56.4\% on LIBERO-Goal (vs.\ 0\% under hard pruning). On the official SmolVLA checkpoint (59.2\% baseline), cross-attention VTR at $M{=}32$ yields 53.4\% SR: re-encoding recovers from the 0\% pruning cliff-edge, though the net benefit depends on baseline feature quality. Full ablation results across all compression levels and task suites are in Appendix~\ref{app:smart_compress_full}.
118	
119	\begin{figure}[t]
120	\centering
121	\begin{subfigure}[b]{0.48\linewidth}
122	\includegraphics[width=\linewidth]{figures/paper/fig_degradation_curve.pdf}
123	\caption{Token pruning across connector classes.}
124	\label{fig:degradation_curve}
125	\end{subfigure}
126	\hfill
127	\begin{subfigure}[b]{0.48\linewidth}
128	\includegraphics[width=\linewidth]{figures/paper/fig_compression_curve.pdf}
129	\caption{VTR M-curve on SmolVLA.}
130	\label{fig:compression_curve}
131	\end{subfigure}
132	\caption{Architecture-dependent response to token reduction on LIBERO-Object. (a)~Token pruning across pipeline types: pure linear projection ($\pi_0$) is immune, linear+encoder (X-VLA) is threshold-graded (onset at $k{=}0.7$), MLP projector (OpenVLA) degrades gracefully, pixel-shuffle (SmolVLA) collapses. (b)~VTR M-curve: re-encoding achieves near-lossless compression ($M{=}16 \approx M{=}128$) where deletion yields 0\%.}
133	\label{fig:results_combined}
134	\end{figure}
135	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "e6b6cda7-94db-4c9c-a793-3cf914af9157",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate token pruning across five VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates include Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\n\n\\subsection{Taxonomy Overview}\n\\label{sec:taxonomy_overview}\n\nTable~\\ref{tab:taxonomy} summarizes the five models and their pruning responses. The effective vision-to-LLM pipeline complexity, rather than the nominal connector label, determines pruning tolerance. A pure linear projection ($\\pi_0$) is immune; a linear projection followed by a deep encoder (X-VLA) is threshold-graded (robust above a retention threshold, then graded decline); a multi-layer MLP degrades smoothly; and pixel-shuffle collapses catastrophically. Token importance heterogeneity (CV) tracks this ordering continuously: 0.038, 0.151, 0.215, 0.314. The pattern holds across a 16$\\times$ range in model size (450M to 7B parameters), which suggests scale alone does not explain it.\n\nA controlled comparison isolates the vision-to-LLM pipeline as the causal factor. $\\pi_0$ and OpenVLA share the same token count (256), the same vision encoder lineage (SigLIP~\\cite{zhai2023siglip}), and differ only in the connector: linear projection versus 3-layer MLP. At $k{=}0.1$ (retaining 10\\% of tokens), $\\pi_0$'s action loss \\emph{improves} by 2.4\\% while OpenVLA's degrades by 61\\%. This 63-percentage-point gap is attributable to pipeline architecture alone. X-VLA's threshold-graded pattern (robust at $k \\geq 0.9$, then degradation at $k{=}0.7$) further demonstrates that the \\emph{effective} pipeline complexity---not just the connector label---determines pruning tolerance (Section~\\ref{sec:linear_results}). OFT~\\cite{kim2025openoft}, which replaces OpenVLA's action head but retains its 3-layer MLP connector, produces nearly identical attention entropy (0.667 vs.\\ 0.661 for standard OpenVLA). The connector, not the action head, determines the attention structure that governs token dispensability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Five-model connector taxonomy. $^\\dagger\\pi_0$ reports offline normalized L1 action loss (pending closed-loop evaluation). $^\\ddagger$X-VLA uses a linear projection followed by a 12-layer BART encoder; the effective pipeline is not purely linear. $^\\S$OFT reports attention entropy only (no pruning evaluation); entropy match with standard OpenVLA confirms the connector determines attention structure.}\n\\label{tab:taxonomy}\n\\begin{tabular}{llcrll}\n\\toprule\nModel & Connector & Params & Tokens & Representative Result & Class \\\\\n\\midrule\n$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Immune (offline) \\\\\nX-VLA~\\cite{zheng2025xvla} & Linear proj$^\\ddagger$ & 880M & 50 & $k{=}0.9$: 97.6\\%, $k{=}0.7$: 56.2\\% & Thresh.-graded \\\\\nOpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\nOFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & Ent.\\ $0.667 \\approx 0.661$ (Std)$^\\S$ & Smooth graded \\\\\nSmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pixel-Shuffle: Catastrophic Cliff-Edge}\n\\label{sec:smolvla_results}\n\nThe SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\\% SR (224/500, CI [40.5\\%, 49.2\\%]).\\footnote{The official SmolVLA result is 87.3\\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Table~\\ref{tab:smolvla_ablation} reports the full ablation. Every pruning configuration produces 0\\% SR (Wilson CI upper bounds $\\leq$0.80\\%). Three observations make this result striking: (1)~\\textbf{Scoring-independent}: random selection performs identically to learned ACIS scoring. (2)~\\textbf{Ratio-independent}: retaining 95\\% of tokens ($k{=}0.95$, removing only 7 of 128) causes the same failure as retaining 50\\%. (3)~\\textbf{Mechanism-independent}: zero-masking, true removal, and token merging all produce 0\\% SR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\\% SR. The official checkpoint (59.2\\% baseline) shows the same cliff-edge.}\n\\label{tab:smolvla_ablation}\n\\begin{tabular}{llccrr}\n\\toprule\nScoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\\\\n\\midrule\nACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\\\\nACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint (HuggingFaceVLA/smolvla\\_libero)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\\\\nRandom & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe official SmolVLA checkpoint (59.2\\% SR, CI [54.8\\%, 63.4\\%]) exhibits identical failure under 50\\% random pruning (0/500), which confirms the cliff-edge is architectural rather than checkpoint-specific. The pattern generalizes across task suites: on LIBERO-Spatial, the official checkpoint (43.8\\% SR) collapses to 0.6\\% (3/500) under pruning,\\footnote{The 3 successes occur on 2 of 10 tasks; the remaining 8 tasks produce 0/50.} and on LIBERO-Goal (63.0\\% baseline) pruning yields 0\\%.\n\n\\subsection{MLP Projector: Graded Degradation}\n\\label{sec:openvla_results}\n\nUnder random token removal, OpenVLA degrades gracefully across all retention ratios: 69.4\\% SR at $k{=}0.95$ ($-4.6$pp from the 74.0\\% baseline), 62.0\\% at $k{=}0.90$, 49.0\\% at $k{=}0.70$, 37.4\\% at $k{=}0.50$, and 20.6\\% at $k{=}0.30$ (Figure~\\ref{fig:results_combined}a; full results with CIs in Table~\\ref{tab:openvla_full}, Appendix). At $k{=}0.30$, two tasks (cream\\_cheese, butter) reach 0\\% SR, but eight retain non-zero performance: degradation is graded, not cliff-edge. Per-task breakdowns are in Appendix~\\ref{app:per_task}. Random token removal provides a conservative lower bound on architectural resilience; learned scoring methods would likely yield better retention.\n\nOFT~\\cite{kim2025openoft} strengthens the connector-centric explanation. OFT replaces OpenVLA's autoregressive action head with an optimized fine-tuning strategy but retains the same 3-layer MLP connector. Its attention entropy (0.667) is within 1\\% of standard OpenVLA (0.661), which confirms that the connector determines the attention structure governing token importance, independent of the action head. Results from EfficientVLA~\\cite{yang2025efficientvla} corroborate the graded pattern on a related architecture: CogACT~\\cite{li2024cogact}, which also uses an MLP projector, retains 74.2\\% SR (from 74.8\\% baseline) under 78\\% token pruning.\n\n\\subsection{Linear Projection: From Immune to Threshold-Graded}\n\\label{sec:linear_results}\n\n$\\pi_0$~\\cite{black2024pi0} (3.3B parameters, 256 tokens, linear projection) uses a flow matching action head~\\cite{lipman2023flow}; we evaluate pruning robustness via offline normalized L1 action loss rather than LIBERO success rate.\\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation, where errors compound, may reveal additional degradation. We report offline results as preliminary evidence pending live evaluation. X-VLA's offline-to-closed-loop gap (offline near-immune at $k{=}0.3$, closed-loop cliff at $k{=}0.7$; Section~\\ref{sec:metric_disconnect}) underscores the need for live verification.} At $k{=}0.1$ (retaining only 10\\% of tokens), the normalized loss is 0.976, a 2.4\\% \\emph{improvement} over the unpruned baseline ($\\mathcal{L}_1 < 1.0$ indicates lower loss than the full-token reference). At $k{=}0.5$ the loss remains 0.983. Token removal at these ratios does not degrade offline action prediction quality, though closed-loop validation is pending.\n\nX-VLA~\\cite{zheng2025xvla} (880M parameters, 50 tokens) is nominally a linear projection model but routes vision tokens through a 12-layer BART encoder~\\cite{lewis2020bart} before the LLM, creating a more complex effective pipeline. The baseline achieves 99.2\\% SR (496/500). At $k{=}0.95$ SR remains 99.0\\% ($-0.2$pp), and at $k{=}0.9$ it holds at 97.6\\% ($-1.6$pp). However, at $k{=}0.7$ SR drops to 56.2\\% (281/500), a 43-percentage-point cliff from $k{=}0.9$. X-VLA thus exhibits a threshold-graded pattern: robust under mild pruning ($k \\geq 0.9$), then a sharp onset of degradation when 30\\% of tokens are removed. This pattern differs from both $\\pi_0$'s offline immunity and OpenVLA's smooth degradation (49.0\\% at $k{=}0.7$). The BART encoder introduces cross-token mixing that creates partial dependencies (CV $= 0.151$, between $\\pi_0$'s 0.038 and OpenVLA's 0.215), explaining the intermediate onset point.\n\nThe $\\pi_0$--X-VLA contrast within the nominal ``linear projection'' class demonstrates that the connector label alone is insufficient: the effective vision-to-LLM pipeline complexity determines pruning tolerance. $\\pi_0$'s single linear layer preserves full token independence (CV $= 0.038$), while X-VLA's BART encoder introduces enough cross-token structure to shift the degradation onset inward.\n\nThe controlled comparison between $\\pi_0$ and OpenVLA remains the strongest evidence for connector-determined compressibility. Both use 256 vision tokens from a SigLIP~\\cite{zhai2023siglip} encoder; they differ only in the connector (linear projection vs.\\ 3-layer MLP). At $k{=}0.1$, $\\pi_0$ improves by 2.4\\% while OpenVLA degrades by 61\\%. With token count, encoder architecture, and pruning protocol held constant, the 63-percentage-point gap is attributable to the connector alone.\n\n\\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}\n\\label{sec:smart_compress_results}\n\nTo test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR ($p > 0.9$ vs.\\ the 44.8\\% baseline), which confirms the gain is architectural, not from additional optimization steps.\\footnote{The extended baseline also collapses to 0\\% SR under pruning ($k{=}0.50$, random, true removal), which confirms that additional training does not mitigate the pixel-shuffle vulnerability.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding vs.\\ deletion on SmolVLA (LIBERO-Object). The M-curve is flat: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (no compression) within 1.1pp. A parameter-matched MLP adapter achieves comparable SR ($p = 0.15$ vs.\\ cross-attention). $^\\ddagger$Mean $\\pm$ std over 3 seeds (500 episodes each). Other rows: single seed with Wilson 95\\% CI.}\n\\label{tab:smart_compress}\n\\begin{tabular}{lccrr}\n\\toprule\nMethod & $M$ & Red. & SR (\\%) & Seeds \\\\\n\\midrule\n\\textit{Baseline} & 128 & 0\\% & 44.8 & 1 \\\\\n\\textit{Ext.\\ training} & -- & -- & 45.0 & 1 \\\\\n\\textit{Hard pruning} & -- & 50--90\\% & 0.0 & mult. \\\\\n\\midrule\nCross-attn$^\\ddagger$ & 16 & 87.5\\% & 56.9$\\pm$1.3 & 55.8/58.4/56.5 \\\\\nCross-attn$^\\ddagger$ & 32 & 75\\% & 60.1$\\pm$1.3 & 61.6/59.2/59.6 \\\\\nCross-attn$^\\ddagger$ & 64 & 50\\% & \\textbf{62.0}$\\pm$2.3 & 61.6/60.0/64.4 \\\\\nCross-attn$^\\ddagger$ & 96 & 25\\% & 54.5$\\pm$3.2 & 52.6/58.2/52.8 \\\\\nCross-attn$^\\ddagger$ & 128 & 0\\% & 58.0$\\pm$3.5 & 59.8/54.0/60.2 \\\\\nMLP adapter$^\\ddagger$ & 32 & 75\\% & 63.4$\\pm$2.6 & 65.2/64.6/60.4 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Official checkpoint (59.2\\% baseline)}} \\\\\nCross-attn & 32 & 75\\% & 53.4 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:smart_compress} reports the full comparison across five compression levels, all with three seeds. The M-curve is flat: $M{=}16$ (56.9\\% $\\pm$ 1.3, 87.5\\% compression) performs within 1.1pp of $M{=}128$ (58.0\\% $\\pm$ 3.5, no compression). All five $M$ values cluster within a 5pp band, and pairwise comparisons among $M \\in \\{32, 64, 128\\}$ yield $p > 0.25$. VTR achieves near-lossless compression at any ratio for the pixel-shuffle connector. The best absolute SR is $M{=}64$ (62.0\\% $\\pm$ 2.3) at 50\\% compression.\n\nA parameter-matched MLP adapter (22.14M parameters, 3-layer, expansion ratio 4) achieves 63.4\\% $\\pm$ 2.6 SR at $M{=}32$, statistically indistinguishable from the cross-attention result (two-sample $t$-test, $p = 0.15$). Both architectures recover from 0\\% to $\\sim$60--63\\% (Figure~\\ref{fig:results_combined}b): the re-encoding principle, not a specific attention mechanism, is the causal factor.\n\nCross-suite evaluation confirms generalization beyond LIBERO-Object. At $M{=}32$, VTR achieves 53.2\\% SR on LIBERO-Spatial (vs.\\ 0.6\\% under hard pruning) and 56.4\\% on LIBERO-Goal (vs.\\ 0\\% under hard pruning). On the official SmolVLA checkpoint (59.2\\% baseline), cross-attention VTR at $M{=}32$ yields 53.4\\% SR: re-encoding recovers from the 0\\% pruning cliff-edge, though the net benefit depends on baseline feature quality. Full ablation results across all compression levels and task suites are in Appendix~\\ref{app:smart_compress_full}.\n\n\\begin{figure}[t]\n\\centering\n\\begin{subfigure}[b]{0.48\\linewidth}\n\\includegraphics[width=\\linewidth]{figures/paper/fig_degradation_curve.pdf}\n\\caption{Token pruning across connector classes.}\n\\label{fig:degradation_curve}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[b]{0.48\\linewidth}\n\\includegraphics[width=\\linewidth]{figures/paper/fig_compression_curve.pdf}\n\\caption{VTR M-curve on SmolVLA.}\n\\label{fig:compression_curve}\n\\end{subfigure}\n\\caption{Architecture-dependent response to token reduction on LIBERO-Object. (a)~Token pruning across pipeline types: pure linear projection ($\\pi_0$) is immune, linear+encoder (X-VLA) is threshold-graded (onset at $k{=}0.7$), MLP projector (OpenVLA) degrades gracefully, pixel-shuffle (SmolVLA) collapses. (b)~VTR M-curve: re-encoding achieves near-lossless compression ($M{=}16 \\approx M{=}128$) where deletion yields 0\\%.}\n\\label{fig:results_combined}\n\\end{figure}\n",
      "numLines": 135,
      "startLine": 1,
      "totalLines": 135
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_017XwrhJwEzPCgEHDp2BV4ts`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "4ea241f7-0da6-4a68-967e-6ba01f03cb83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3m6V7E9EEjoEhQ4YDKvad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12712
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

_source line 16 · 2026-05-20T11:50:45.108Z_

<details><summary>↩ Tool result · `toolu_017XwrhJwEzPCgEHDp2BV4ts`</summary>

```text
1	\section{Analysis and Discussion}
2	\label{sec:analysis}
3	
4	\subsection{Effective Pipeline Complexity Determines Token Independence}
5	\label{sec:pixel_shuffle}
6	
7	A controlled comparison between $\pi_0$ and OpenVLA isolates the vision connector as the causal factor behind compressibility differences. Both models process 256 vision tokens from SigLIP encoders, yet at $k{=}0.1$, $\pi_0$'s offline action loss improves by 2.4\% while OpenVLA's closed-loop SR degrades by 61\%. This 63 percentage-point gap, with token count and encoder held constant, can only be attributed to the connector. We note that $\pi_0$'s result is offline; X-VLA's offline-to-closed-loop divergence (Section~\ref{sec:metric_disconnect}) cautions against treating offline immunity as definitive.
8	
9	The vision-to-LLM pipeline creates fundamentally different token structures depending on its effective complexity. Pixel-shuffle connectors (SmolVLA) apply $4 \times 4$ spatial folding: each of 128 tokens encodes 16 patches via channel concatenation (Figure~\ref{fig:pixel_shuffle}). Removing any token eliminates an entire receptive field with no redundancy from neighbors. The folding is fixed and non-learned, so no downstream layer can recover discarded information.
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=0.85\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
14	\caption{Pixel-shuffle folding: each $4{\times}4$ block of SigLIP patches is channel-concatenated into one token. Removing any token eliminates its receptive field (gray) with no redundancy.}
15	\label{fig:pixel_shuffle}
16	\end{figure}
17	
18	Pure linear projection connectors ($\pi_0$) apply a single linear layer that maps each patch independently. No cross-token interaction occurs during projection, so tokens are genuinely independent. Removing one token loses approximately $1/N$ of the visual field, and the loss is spatially uniform.
19	
20	X-VLA complicates this picture. Its connector is nominally a linear projection, but vision tokens subsequently pass through a 12-layer BART encoder~\cite{lewis2020bart} before reaching the LLM. The BART encoder's self-attention layers introduce cross-token mixing that creates partial dependencies: X-VLA's CV (0.151) is four times higher than $\pi_0$'s (0.038), and its attention entropy (0.614) is substantially lower. This explains X-VLA's threshold-graded pattern: the BART encoder differentiates tokens enough that removing 30\% crosses a threshold, but not enough to cause degradation at 10\% removal. The nominal connector label (``linear projection'') is insufficient; the effective pipeline complexity---including any post-connector processing---determines pruning tolerance.
21	
22	MLP projectors (OpenVLA, OFT) process each patch through a 3-layer MLP with GELU activations. Per-patch processing preserves spatial locality, but non-linear transformations create partial dependencies between each projected representation and the broader feature space. The result is an intermediate regime: tokens carry differentiated information without the rigid spatial entanglement of pixel-shuffle.
23	
24	The OFT variant confirms that the action head does not determine attention structure. OFT and OpenVLA share the same MLP connector but differ in their action decoding mechanism. Their attention entropy values are nearly identical (0.667 and 0.661, respectively), consistent with the connector, not the action head, controlling how information is distributed across vision tokens.
25	
26	\subsection{Token Importance Heterogeneity as Diagnostic}
27	\label{sec:diagnostic}
28	
29	The coefficient of variation (CV) of token importance, measured as the variation in L2 norms across vision tokens, captures the heterogeneity that determines pruning tolerance. CV forms a continuous spectrum across the four measured models: $\pi_0$ CV $= 0.038$ (tokens carry near-equal importance), X-VLA CV $= 0.151$ (mild differentiation), OpenVLA CV $= 0.215$ (moderate differentiation), SmolVLA CV $= 0.314$ (high heterogeneity). This ordering predicts not just the class of degradation but the onset point: $\pi_0$ (CV $= 0.038$) is immune through $k{=}0.1$, X-VLA (CV $= 0.151$) is robust until $k{=}0.7$ then cliffs, OpenVLA (CV $= 0.215$) degrades from $k{=}0.95$, and SmolVLA (CV $= 0.314$) collapses at $k{=}0.95$.
30	
31	Attention entropy provides the mechanistic explanation for why CV predicts pruning behavior. $\pi_0$ attention entropy is 0.9999, near-maximally uniform across all 18 layers (range 0.931--0.983). When all tokens contribute equally, any subset preserves a proportional share of the total information, and the model can redistribute attention without loss. Low CV combined with high entropy means tokens are interchangeable: removing any subset is equivalent to uniform downsampling.
32	
33	SmolVLA presents an apparent paradox. Its attention entropy is also high (0.952, range 0.93--0.98, spread 0.05), yet pruning is catastrophic. The resolution lies in the combination of high entropy with high CV: tokens are uniformly attended (the model treats them all as necessary) but carry heterogeneous spatial content due to pixel-shuffle folding. The model cannot selectively attend to a subset because all tokens are equally demanded, yet the tokens themselves are not interchangeable. This ``differentiated but entangled'' pattern is the signature of pixel-shuffle connectors: uniform attention over non-uniform content.
34	
35	X-VLA occupies a revealing intermediate position. Its CV ($0.151$) falls between $\pi_0$ and OpenVLA, and its attention entropy ($0.614$) is the lowest among the four models. The 12-layer BART encoder introduces cross-token mixing that partially differentiates tokens, creating enough heterogeneity to trigger a cliff at $k{=}0.7$ but not enough to cause degradation at $k{=}0.9$. X-VLA demonstrates that CV predicts the \emph{onset point} of degradation, not merely a categorical class.
36	
37	OpenVLA occupies the graded regime. Its overall entropy is 0.661, with progressive sharpening from 0.98 in layer 0 to 0.48 in layer 29 (spread 0.50; Figure~\ref{fig:entropy_layers} and Appendix~\ref{app:entropy_details}). The model learns to concentrate attention on informative tokens across processing depth. Moderate CV (0.215) means tokens are partially differentiated: pruning removes information, but the remaining tokens carry sufficient signal for graded rather than catastrophic degradation. OFT attention entropy (0.667) is nearly identical to OpenVLA (0.661), confirming that the action head is irrelevant to the attention structure.
38	
39	Token importance heterogeneity (CV) has practical value as a diagnostic because it requires only a forward pass on a sample of task-relevant frames. Four models (with OFT as a connector-controlled variant) now span the full CV spectrum from 0.038 to 0.314, and the CV ordering correctly predicts both the degradation class and onset across all cases.
40	
41	\begin{figure}[t]
42	\centering
43	\includegraphics[width=\linewidth]{figures/paper/fig_entropy_layers.pdf}
44	\caption{Per-layer attention entropy ratio for SmolVLA (16 layers), OpenVLA (32 layers), and $\pi_0$ (18 layers). SmolVLA and $\pi_0$ maintain near-uniform attention throughout, while OpenVLA progressively sharpens from 0.98 to 0.48. Despite similar entropy, SmolVLA and $\pi_0$ exhibit opposite pruning outcomes due to token importance heterogeneity (CV $= 0.314$ vs.\ $0.038$). X-VLA (entropy $= 0.614$, CV $= 0.151$) occupies an intermediate position, consistent with its threshold-graded pattern (onset at $k{=}0.7$).}
45	\label{fig:entropy_layers}
46	\end{figure}
47	
48	\subsection{Why Re-Encoding Succeeds Where Deletion Fails}
49	\label{sec:learned_compression}
50	
51	Two architecturally distinct re-encoding modules, cross-attention pooling (22.2M parameters) and a parameter-matched MLP adapter (22.14M parameters), both recover $\sim$60--63\% SR on SmolVLA where all deletion methods yield 0\% (3-seed means: cross-attention $60.1 \pm 1.3$, MLP $63.4 \pm 2.6$; two-sample $t$-test $p = 0.15$). The absence of a statistically significant difference between architectures identifies the shared property, learned re-encoding of the full token set, as the operative factor.
52	
53	The $M$-curve provides direct evidence that re-encoding preserves information regardless of compression ratio. Performance is flat across a wide range: $M{=}16$ yields $56.9 \pm 1.3$\% and $M{=}128$ yields $58.0 \pm 3.5$\%, with intermediate values of 60.1\% ($M{=}32$), 62.0\% ($M{=}64$), and 54.5\% ($M{=}96$). The Vision Token Re-encoder (VTR) redistributes information into fewer tokens without destroying it, even at $8\times$ compression ($M{=}16$, retaining 12.5\% of tokens). This stands in sharp contrast to hard pruning, where removing 5\% of pixel-shuffle tokens causes complete collapse.
54	
55	The $M{=}128$ passthrough condition, where the re-encoder outputs the same number of tokens as the input, achieves $\sim$58\% SR versus a 44.8\% baseline. This 13-point gain from re-encoding alone, without any compression, shows that the learned module adds value through feature reorganization. An extended training control (100K additional steps without the compressor, 45.0\% SR) confirms that the gain is architectural rather than a consequence of additional optimization.
56	
57	The mechanism is straightforward. Hard pruning applies a binary mask: selected tokens pass through, the rest are discarded. Re-encoding preserves access to all 128 source tokens through learned transformations (weighted summation for cross-attention, feed-forward mapping for MLP). The learned module breaks the rigid spatial entanglement of pixel-shuffle tokens by integrating information across the original $4 \times 4$ receptive field boundaries. VTR is currently evaluated on SmolVLA only; whether re-encoding provides comparable gains for other connector types remains untested.
58	
59	\subsection{Offline Metrics Underestimate Closed-Loop Degradation}
60	\label{sec:metric_disconnect}
61	
62	Offline evaluation metrics underestimate the severity of pruning-induced failure and miss task-level heterogeneity. The aggregate $3.4\times$ action error increase (Table~\ref{tab:offline_action_error}, Appendix~\ref{app:offline_error}) is a clear negative signal, but per-step metrics do not distinguish moderate perturbations (position errors of 0.20--0.30 per axis) from catastrophic events (complete gripper inversion, L2 $= 1.02$) that individually terminate an episode. In closed-loop execution, a single catastrophic action pushes the robot off-trajectory, subsequent observations diverge from training data, and recovery becomes impossible. These events are rare enough to be diluted in per-step averages but occur in every pruned episode we tested.
63	
64	X-VLA provides a concrete example of this disconnect. At $k{=}0.3$, X-VLA's offline normalized action loss is 1.0014---near the unpruned baseline, suggesting negligible degradation. Yet at $k{=}0.7$ (a less aggressive pruning ratio), closed-loop SR drops to 56.2\%, a 43pp cliff. Offline metrics register the average perturbation but not the task-level failures that dominate closed-loop outcomes. Offline evaluation remains useful for directional signals (e.g., $\pi_0$'s improving loss at $k{=}0.1$ suggests genuine robustness), but closed-loop evaluation is essential for validating any VLA compression method.
65	
66	\subsection{Limitations}
67	\label{sec:limitations}
68	
69	All closed-loop experiments use the LIBERO simulation benchmark, which does not capture real-world deployment conditions such as sensor noise, calibration drift, and physical contact dynamics. Scale confounding is partially addressed: our taxonomy spans five models from 450M to 7B parameters, and $\pi_0$ (3.3B) is immune while OpenVLA (7B) is vulnerable, which suggests scale alone does not explain the observed differences. A matched-scale experiment remains the ideal control.
70	
71	$\pi_0$ evaluation is currently offline only; closed-loop results may reveal additional degradation not captured by single-step loss, as demonstrated by X-VLA's offline-to-closed-loop gap (Section~\ref{sec:metric_disconnect}). X-VLA closed-loop evaluation covers $k \geq 0.7$; lower retention ratios remain untested. OpenVLA VTR experiments are also pending.
72	
73	VTR is evaluated on SmolVLA only; generalization of re-encoding to other connector types is untested. Re-encoding on the well-trained official SmolVLA checkpoint yields 53.4\% SR, below the 59.2\% uncompressed baseline. The gain on our fine-tuned model (44.8\% $\to$ 60.1\%) is larger, consistent with re-encoding providing the most benefit when baseline features are undertrained.
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "a0aca354-9de6-4d09-8501-a65b9852521f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
      "content": "\\section{Analysis and Discussion}\n\\label{sec:analysis}\n\n\\subsection{Effective Pipeline Complexity Determines Token Independence}\n\\label{sec:pixel_shuffle}\n\nA controlled comparison between $\\pi_0$ and OpenVLA isolates the vision connector as the causal factor behind compressibility differences. Both models process 256 vision tokens from SigLIP encoders, yet at $k{=}0.1$, $\\pi_0$'s offline action loss improves by 2.4\\% while OpenVLA's closed-loop SR degrades by 61\\%. This 63 percentage-point gap, with token count and encoder held constant, can only be attributed to the connector. We note that $\\pi_0$'s result is offline; X-VLA's offline-to-closed-loop divergence (Section~\\ref{sec:metric_disconnect}) cautions against treating offline immunity as definitive.\n\nThe vision-to-LLM pipeline creates fundamentally different token structures depending on its effective complexity. Pixel-shuffle connectors (SmolVLA) apply $4 \\times 4$ spatial folding: each of 128 tokens encodes 16 patches via channel concatenation (Figure~\\ref{fig:pixel_shuffle}). Removing any token eliminates an entire receptive field with no redundancy from neighbors. The folding is fixed and non-learned, so no downstream layer can recover discarded information.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{Pixel-shuffle folding: each $4{\\times}4$ block of SigLIP patches is channel-concatenated into one token. Removing any token eliminates its receptive field (gray) with no redundancy.}\n\\label{fig:pixel_shuffle}\n\\end{figure}\n\nPure linear projection connectors ($\\pi_0$) apply a single linear layer that maps each patch independently. No cross-token interaction occurs during projection, so tokens are genuinely independent. Removing one token loses approximately $1/N$ of the visual field, and the loss is spatially uniform.\n\nX-VLA complicates this picture. Its connector is nominally a linear projection, but vision tokens subsequently pass through a 12-layer BART encoder~\\cite{lewis2020bart} before reaching the LLM. The BART encoder's self-attention layers introduce cross-token mixing that creates partial dependencies: X-VLA's CV (0.151) is four times higher than $\\pi_0$'s (0.038), and its attention entropy (0.614) is substantially lower. This explains X-VLA's threshold-graded pattern: the BART encoder differentiates tokens enough that removing 30\\% crosses a threshold, but not enough to cause degradation at 10\\% removal. The nominal connector label (``linear projection'') is insufficient; the effective pipeline complexity---including any post-connector processing---determines pruning tolerance.\n\nMLP projectors (OpenVLA, OFT) process each patch through a 3-layer MLP with GELU activations. Per-patch processing preserves spatial locality, but non-linear transformations create partial dependencies between each projected representation and the broader feature space. The result is an intermediate regime: tokens carry differentiated information without the rigid spatial entanglement of pixel-shuffle.\n\nThe OFT variant confirms that the action head does not determine attention structure. OFT and OpenVLA share the same MLP connector but differ in their action decoding mechanism. Their attention entropy values are nearly identical (0.667 and 0.661, respectively), consistent with the connector, not the action head, controlling how information is distributed across vision tokens.\n\n\\subsection{Token Importance Heterogeneity as Diagnostic}\n\\label{sec:diagnostic}\n\nThe coefficient of variation (CV) of token importance, measured as the variation in L2 norms across vision tokens, captures the heterogeneity that determines pruning tolerance. CV forms a continuous spectrum across the four measured models: $\\pi_0$ CV $= 0.038$ (tokens carry near-equal importance), X-VLA CV $= 0.151$ (mild differentiation), OpenVLA CV $= 0.215$ (moderate differentiation), SmolVLA CV $= 0.314$ (high heterogeneity). This ordering predicts not just the class of degradation but the onset point: $\\pi_0$ (CV $= 0.038$) is immune through $k{=}0.1$, X-VLA (CV $= 0.151$) is robust until $k{=}0.7$ then cliffs, OpenVLA (CV $= 0.215$) degrades from $k{=}0.95$, and SmolVLA (CV $= 0.314$) collapses at $k{=}0.95$.\n\nAttention entropy provides the mechanistic explanation for why CV predicts pruning behavior. $\\pi_0$ attention entropy is 0.9999, near-maximally uniform across all 18 layers (range 0.931--0.983). When all tokens contribute equally, any subset preserves a proportional share of the total information, and the model can redistribute attention without loss. Low CV combined with high entropy means tokens are interchangeable: removing any subset is equivalent to uniform downsampling.\n\nSmolVLA presents an apparent paradox. Its attention entropy is also high (0.952, range 0.93--0.98, spread 0.05), yet pruning is catastrophic. The resolution lies in the combination of high entropy with high CV: tokens are uniformly attended (the model treats them all as necessary) but carry heterogeneous spatial content due to pixel-shuffle folding. The model cannot selectively attend to a subset because all tokens are equally demanded, yet the tokens themselves are not interchangeable. This ``differentiated but entangled'' pattern is the signature of pixel-shuffle connectors: uniform attention over non-uniform content.\n\nX-VLA occupies a revealing intermediate position. Its CV ($0.151$) falls between $\\pi_0$ and OpenVLA, and its attention entropy ($0.614$) is the lowest among the four models. The 12-layer BART encoder introduces cross-token mixing that partially differentiates tokens, creating enough heterogeneity to trigger a cliff at $k{=}0.7$ but not enough to cause degradation at $k{=}0.9$. X-VLA demonstrates that CV predicts the \\emph{onset point} of degradation, not merely a categorical class.\n\nOpenVLA occupies the graded regime. Its overall entropy is 0.661, with progressive sharpening from 0.98 in layer 0 to 0.48 in layer 29 (spread 0.50; Figure~\\ref{fig:entropy_layers} and Appendix~\\ref{app:entropy_details}). The model learns to concentrate attention on informative tokens across processing depth. Moderate CV (0.215) means tokens are partially differentiated: pruning removes information, but the remaining tokens carry sufficient signal for graded rather than catastrophic degradation. OFT attention entropy (0.667) is nearly identical to OpenVLA (0.661), confirming that the action head is irrelevant to the attention structure.\n\nToken importance heterogeneity (CV) has practical value as a diagnostic because it requires only a forward pass on a sample of task-relevant frames. Four models (with OFT as a connector-controlled variant) now span the full CV spectrum from 0.038 to 0.314, and the CV ordering correctly predicts both the degradation class and onset across all cases.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_entropy_layers.pdf}\n\\caption{Per-layer attention entropy ratio for SmolVLA (16 layers), OpenVLA (32 layers), and $\\pi_0$ (18 layers). SmolVLA and $\\pi_0$ maintain near-uniform attention throughout, while OpenVLA progressively sharpens from 0.98 to 0.48. Despite similar entropy, SmolVLA and $\\pi_0$ exhibit opposite pruning outcomes due to token importance heterogeneity (CV $= 0.314$ vs.\\ $0.038$). X-VLA (entropy $= 0.614$, CV $= 0.151$) occupies an intermediate position, consistent with its threshold-graded pattern (onset at $k{=}0.7$).}\n\\label{fig:entropy_layers}\n\\end{figure}\n\n\\subsection{Why Re-Encoding Succeeds Where Deletion Fails}\n\\label{sec:learned_compression}\n\nTwo architecturally distinct re-encoding modules, cross-attention pooling (22.2M parameters) and a parameter-matched MLP adapter (22.14M parameters), both recover $\\sim$60--63\\% SR on SmolVLA where all deletion methods yield 0\\% (3-seed means: cross-attention $60.1 \\pm 1.3$, MLP $63.4 \\pm 2.6$; two-sample $t$-test $p = 0.15$). The absence of a statistically significant difference between architectures identifies the shared property, learned re-encoding of the full token set, as the operative factor.\n\nThe $M$-curve provides direct evidence that re-encoding preserves information regardless of compression ratio. Performance is flat across a wide range: $M{=}16$ yields $56.9 \\pm 1.3$\\% and $M{=}128$ yields $58.0 \\pm 3.5$\\%, with intermediate values of 60.1\\% ($M{=}32$), 62.0\\% ($M{=}64$), and 54.5\\% ($M{=}96$). The Vision Token Re-encoder (VTR) redistributes information into fewer tokens without destroying it, even at $8\\times$ compression ($M{=}16$, retaining 12.5\\% of tokens). This stands in sharp contrast to hard pruning, where removing 5\\% of pixel-shuffle tokens causes complete collapse.\n\nThe $M{=}128$ passthrough condition, where the re-encoder outputs the same number of tokens as the input, achieves $\\sim$58\\% SR versus a 44.8\\% baseline. This 13-point gain from re-encoding alone, without any compression, shows that the learned module adds value through feature reorganization. An extended training control (100K additional steps without the compressor, 45.0\\% SR) confirms that the gain is architectural rather than a consequence of additional optimization.\n\nThe mechanism is straightforward. Hard pruning applies a binary mask: selected tokens pass through, the rest are discarded. Re-encoding preserves access to all 128 source tokens through learned transformations (weighted summation for cross-attention, feed-forward mapping for MLP). The learned module breaks the rigid spatial entanglement of pixel-shuffle tokens by integrating information across the original $4 \\times 4$ receptive field boundaries. VTR is currently evaluated on SmolVLA only; whether re-encoding provides comparable gains for other connector types remains untested.\n\n\\subsection{Offline Metrics Underestimate Closed-Loop Degradation}\n\\label{sec:metric_disconnect}\n\nOffline evaluation metrics underestimate the severity of pruning-induced failure and miss task-level heterogeneity. The aggregate $3.4\\times$ action error increase (Table~\\ref{tab:offline_action_error}, Appendix~\\ref{app:offline_error}) is a clear negative signal, but per-step metrics do not distinguish moderate perturbations (position errors of 0.20--0.30 per axis) from catastrophic events (complete gripper inversion, L2 $= 1.02$) that individually terminate an episode. In closed-loop execution, a single catastrophic action pushes the robot off-trajectory, subsequent observations diverge from training data, and recovery becomes impossible. These events are rare enough to be diluted in per-step averages but occur in every pruned episode we tested.\n\nX-VLA provides a concrete example of this disconnect. At $k{=}0.3$, X-VLA's offline normalized action loss is 1.0014---near the unpruned baseline, suggesting negligible degradation. Yet at $k{=}0.7$ (a less aggressive pruning ratio), closed-loop SR drops to 56.2\\%, a 43pp cliff. Offline metrics register the average perturbation but not the task-level failures that dominate closed-loop outcomes. Offline evaluation remains useful for directional signals (e.g., $\\pi_0$'s improving loss at $k{=}0.1$ suggests genuine robustness), but closed-loop evaluation is essential for validating any VLA compression method.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nAll closed-loop experiments use the LIBERO simulation benchmark, which does not capture real-world deployment conditions such as sensor noise, calibration drift, and physical contact dynamics. Scale confounding is partially addressed: our taxonomy spans five models from 450M to 7B parameters, and $\\pi_0$ (3.3B) is immune while OpenVLA (7B) is vulnerable, which suggests scale alone does not explain the observed differences. A matched-scale experiment remains the ideal control.\n\n$\\pi_0$ evaluation is currently offline only; closed-loop results may reveal additional degradation not captured by single-step loss, as demonstrated by X-VLA's offline-to-closed-loop gap (Section~\\ref{sec:metric_disconnect}). X-VLA closed-loop evaluation covers $k \\geq 0.7$; lower retention ratios remain untested. OpenVLA VTR experiments are also pending.\n\nVTR is evaluated on SmolVLA only; generalization of re-encoding to other connector types is untested. Re-encoding on the well-trained official SmolVLA checkpoint yields 53.4\\% SR, below the 59.2\\% uncompressed baseline. The gain on our fine-tuned model (44.8\\% $\\to$ 60.1\\%) is larger, consistent with re-encoding providing the most benefit when baseline features are undertrained.\n",
      "numLines": 74,
      "startLine": 1,
      "totalLines": 74
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
Now I have all the context. Let me carefully craft the Abstract and Conclusion based on the requirements.

Key numbers to use (must be consistent):
- π0: offline loss improves 2.4% at k=0.1 (immune, offline)
- X-VLA: 97.6% SR at k≥0.9, 56.2% at k=0.7 (threshold-graded)
- OpenVLA: 74→37.4% at k=0.5 (smooth graded)
- OFT: entropy 0.667 ≈ 0.661 (smooth graded, same as OpenVLA)


- SmolVLA: 0% at k=0.95 (catastrophic cliff)
- CV: 0.038→0.151→0.215→0.314
- VTR: 60.1% SR at 75% compression (cross-attn), 63.4% (MLP adapter)
- M-curve flat: M=16 ≈ M=128

Abstract constraints:
- ~150-170 words
- π0 results labeled "offline"
- X-VLA k≤0.5 data not cited
- No "state-of-the-art"
- Avoid "novel", "groundbreaking"
- Abbreviations expanded on first use
- No em-dash, no -ing phrase endings, no "Furthermore"/"Moreover"/"Additionally"
- No fabricated citation keys

Now I'm drafting the abstract itself, starting with the motivation around vision token pruning and its applicability to VLA models, then moving into the empirical findings across the five models and their distinct response patterns. I need to keep the language direct and avoid the prohibited phrases while staying within the word budget.

The key results show that robustness varies dramatically by architecture: linear projectors are resilient, threshold-based models degrade sharply at certain compression points, MLP projectors show gradual degradation, and pixel-shuffle designs fail catastrophically at minimal pruning. The coefficient of variation metric captures this ordering, and the proposed Vision Token Re-encoder module recovers substantial performance on the cliff-edge cases. The abstract should conclude by positioning this as evidence that VLA compressibility depends on architecture choice and that a diagnostic-then-compress strategy enables practical deployment. SmolVLA with pixel-shuffle encoding shows a dramatic failure mode—performance drops to zero at just 5% token removal—while the coefficient of variation of token importance scores predicts this ordering across all architectures. For models that hit this cliff edge, a Vision Token Re-encoder can recover over 60% success rate at 75% compression where standard deletion fails entirely. The key insight is that compressibility depends fundamentally on architecture, so combining a CV diagnostic with the re-encoder creates a framework for safely reducing tokens. Pixel-shuffle or include re-encoding modules -- future VLAs targeting efficiency should avoid the former, while re-encoding provides an architecture-independent solution to the cliff-edge problem. Practitioners can use continuous vision token degradation as a zero-cost diagnostic without additional overhead. Closed-loop evaluation proves essential since offline metrics alone underestimate failure modes in deployed systems. Code and evaluation scripts will be released upon publication. pruning configurations. Third, token importance CV predicts degradation onset continuously (0.038 $\to$ 0.151 $\to$ 0.215 $\to$ 0.314) from a single forward pass, providing a zero-cost diagnostic for practitioners. Fourth, VTR re-encoding overcomes the cliff-edge: both cross-attention and MLP modules recover 60\%+ SR at 75\% compression where all deletion methods yield 0\%, and the M-curve is flat ($M{=}16 \approx M{=}128$). Fifth, offline metrics underestimate closed-loop failure severity; $\pi_0$'s offline immunity (2.4\% improvement at $k{=}0.1$) requires closed-loop verification.

These results suggest that future VLA architectures prioritizing token efficiency should either sidestep pixel-shuffle connectors or add re-encoding modules, while CV offers a forward-pass diagnostic to catch vulnerabilities before deployment and closed-loop evaluation remains critical for validating compression methods. I'm verifying the constraints on my previous section—checking that numbers align with the source data, that I've properly labeled π₀ as offline, and that I've avoided certain phrasings. I notice the -ing phrase ending needs adjustment, so I'll rephrase "identifying vulnerability before deployment" as a relative clause instead. Let me also cross-check all the numerical references against the original findings to ensure consistency. olVLA 0% at k=0.95 (5% removal) ✓ (Results: "retaining 95% of tokens (k=0.95, removing only 7 of 128) causes the same failure")
- π0 improves 2.4% at k=0.1 ✓ (Results: "2.4% improvement over the unpruned baseline")
- CV: 0.038, 0.151, 0.215, 0.314 ✓ (Results: "0.038, 0.151, 0.215, 0.314")
- VTR 60.1% at 75% (M=32) ✓ (Results: "60.1±1.3")
- MLP adapter 63.4% ✓ (Results: "63.4±2.6")
- M-curve shows performance across different model sizes, with X-VLA maintaining 97.6% at k=0.9 but dropping to 56.2% at k=0.7, while OpenVLA degrades significantly from 74.0% to 37.4% at k=0.5. The models span a 16× parameter range from 450M to 7B across three connector families. I should verify the taxonomy is consistent—π0 uses linear projection at 3.3B, X-VLA uses linear projection with BART at 880M, and OpenVLA uses a 3-layer MLP at 7B.

Actually, I need to finalize the model count and response classes. There are five models total: π0, X-VLA, OpenVLA, OFT, and SmolVLA, spanning three connector families (linear projection, MLP, and pixel-shuffle). The four response classes are immune, threshold-graded, smooth graded, and catastrophic cliff. Now I'm checking the Abstract wording—it should say "five VLA models" to match the Introduction, and I need to verify the word count more carefully before finalizing both sections. I'm recounting the words in my summary to make sure it fits the target range—looks like I'm right around 165 words, which works well for what I need to convey.

Now I'm looking at the empirical results across different VLA architectures. The linear projection connectors show sharp threshold effects—X-VLA maintains high success rates until hitting a cliff, while OpenVLA's MLP projector degrades more gracefully as token removal increases. SmolVLA's pixel-shuffle approach is particularly brittle, collapsing almost immediately with minimal pruning.

The coefficient of variation in token importance scores appears to be a strong predictor of this robustness ordering, ranging from very low to high values across a single forward pass. For architectures that hit these catastrophic cliffs, a Vision Token Re-encoder can recover substantial performance even at high compression levels where other deletion methods completely fail. This suggests that compressibility is fundamentally tied to architectural design choices, and the CV diagnostic combined with the re-encoder approach could form a comprehensive solution. I'm checking the constraint about headline numbers—I have four key results embedded in the taxonomy description, which fits the 3-4 requirement. The X-VLA numbers are part of the taxonomy itself rather than standalone headline numbers, so keeping them makes sense. I should verify I'm not using forbidden phrases like "Furthermore" or "Moreover" in the conclusion, and that I'm using en-dashes correctly for number ranges rather than em-dashes. Let me review the abstract one more time before finalizing. I'm checking whether to include all four CV values in the abstract for completeness. Since they map to the taxonomy classes I mentioned, showing the full sequence (0.038 → 0.151 → 0.215 → 0.314) makes the abstract more self-contained and precise, even if it adds a few words. The word count should still be around 157, which is acceptable. Now I'm reviewing the abstract's narrative flow to make sure each section—the problem, the approach, and the results—connects logically. I need to verify the terminology is consistent—"five VLA models" reads better than "five VLAs" since I've already expanded the acronym. The phrasing looks solid otherwise, and "governed by" is appropriate for academic writing. Now I'm finalizing the abstract text with these adjustments in place. I'm wrapping up the conclusion by summarizing the four key findings: architecture-dependent compressibility determines pruning tolerance across different connector families, pixel-shuffle designs create irreversible spatial entanglement that causes catastrophic collapse, token importance CV provides a zero-cost diagnostic for predicting degradation, and Vision Token Re-encoding successfully recovers performance at high compression rates where standard deletion fails. I'm verifying the constraints one more time—making sure I haven't used forbidden words like "consistently" or "significantly," that π₀ is properly labeled as offline, and that there are no em-dashes or participial phrase endings. The conclusion looks solid without citations since they weren't required, and everything checks out against the guidelines. I'm verifying the specific metrics from the Results section to ensure accuracy—the cross-attention and MLP values at 75% compression support my "60%+" phrasing, so that's solid. I'm also confirming that the new abstract doesn't need to reference supporting models like CogACT or EfficientVLA since we're centering on our own five-model taxonomy, with those comparisons serving as context in the Results rather than core findings. The old abstract's focus on two models is being replaced by the broader framework, so I'm ready to finalize both revisions. the edits now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "3ee75c4a-1924-43f2-b0b3-1d9f5c5539bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tvyAcTNZM3k7Maboo8Gh5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16952,
      "cache_read_input_tokens": 24553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16952
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

Now I have all the context. Let me rewrite both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "c592b9b7-a67a-4b81-9110-ad0af9f54646",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tvyAcTNZM3k7Maboo8Gh5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16952,
      "cache_read_input_tokens": 24553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16952
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

<details open><summary>🔧 Tool call — Edit · `toolu_016Kri7nLU2g69aBw1wKCUD1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
  "old_string": "\\begin{abstract}\nVision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\\% to 0\\% on the official checkpoint, even at 5\\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\\% SR at 75\\% token reduction where all deletion methods yield 0\\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.\n\\end{abstract}",
  "new_string": "\\begin{abstract}\nVision token pruning accelerates Vision Transformer inference with negligible accuracy loss, but whether this robustness transfers to Vision-Language-Action (VLA) models remains untested across architectures. We evaluate five VLA models (450M--7B parameters) spanning three connector families and identify four response classes governed by effective pipeline complexity. $\\pi_0$ (linear projection) is \\emph{immune}: offline action loss improves 2.4\\% at 90\\% removal. X-VLA (linear projection + encoder) is \\emph{threshold-graded}: 97.6\\% Success Rate (SR) at $k{=}0.9$, onset at $k{=}0.7$ (56.2\\%). OpenVLA (MLP projector) degrades \\emph{smoothly}: 74.0\\% $\\to$ 37.4\\% SR at 50\\% removal. SmolVLA (pixel-shuffle) hits a \\emph{catastrophic cliff}: 0\\% SR at 5\\% removal. The coefficient of variation (CV) of token importance predicts this ordering continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass. For cliff-edge architectures, a Vision Token Re-encoder (VTR) recovers 60\\%+ SR at 75\\% compression where all deletion methods yield 0\\%. VLA compressibility is architecture-dependent; CV diagnostic combined with VTR forms a Diagnose-then-Compress framework for safe token reduction.\n\\end{abstract}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "0181cf9b-525a-4078-aa64-1303172f3310",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tvyAcTNZM3k7Maboo8Gh5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16952,
      "cache_read_input_tokens": 24553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16952
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

_source line 20 · 2026-05-20T11:53:09.900Z_

<details><summary>↩ Tool result · `toolu_016Kri7nLU2g69aBw1wKCUD1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "f5ccfcfd-d59d-433c-9d1e-5b74a2d088ab",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
    "oldString": "\\begin{abstract}\nVision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\\% to 0\\% on the official checkpoint, even at 5\\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\\% SR at 75\\% token reduction where all deletion methods yield 0\\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.\n\\end{abstract}",
    "newString": "\\begin{abstract}\nVision token pruning accelerates Vision Transformer inference with negligible accuracy loss, but whether this robustness transfers to Vision-Language-Action (VLA) models remains untested across architectures. We evaluate five VLA models (450M--7B parameters) spanning three connector families and identify four response classes governed by effective pipeline complexity. $\\pi_0$ (linear projection) is \\emph{immune}: offline action loss improves 2.4\\% at 90\\% removal. X-VLA (linear projection + encoder) is \\emph{threshold-graded}: 97.6\\% Success Rate (SR) at $k{=}0.9$, onset at $k{=}0.7$ (56.2\\%). OpenVLA (MLP projector) degrades \\emph{smoothly}: 74.0\\% $\\to$ 37.4\\% SR at 50\\% removal. SmolVLA (pixel-shuffle) hits a \\emph{catastrophic cliff}: 0\\% SR at 5\\% removal. The coefficient of variation (CV) of token importance predicts this ordering continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass. For cliff-edge architectures, a Vision Token Re-encoder (VTR) recovers 60\\%+ SR at 75\\% compression where all deletion methods yield 0\\%. VLA compressibility is architecture-dependent; CV diagnostic combined with VTR forms a Diagnose-then-Compress framework for safe token reduction.\n\\end{abstract}",
    "originalFile": "\\begin{abstract}\nVision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\\% to 0\\% on the official checkpoint, even at 5\\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\\% SR at 75\\% token reduction where all deletion methods yield 0\\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\begin{abstract}",
          "-Vision token pruning reliably accelerates Vision Transformer (ViT) inference with negligible accuracy loss, prompting recent proposals to apply the same technique to Vision-Language-Action (VLA) models for faster robotic control. We conduct the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control and find that compressibility is associated with the vision connector architecture. SmolVLA, whose pixel-shuffle connector spatially folds patches into high-density tokens, exhibits a cliff-edge failure: pruning collapses success rate from 59.2\\% to 0\\% on the official checkpoint, even at 5\\% token removal. This failure is robust across seven pruning configurations and three mechanisms. OpenVLA, whose MLP projector maps patches independently, degrades gracefully under the same conditions. The divergence co-occurs with differences in token information density: pixel-shuffle produces tokens with near-uniform attention, while MLP-projected tokens develop progressively selective attention in deeper layers. A diagnostic experiment confirms that learned re-encoding succeeds where all deletion methods fail: both a cross-attention and a parameter-matched MLP module recover 60--63\\% SR at 75\\% token reduction where all deletion methods yield 0\\%, and a passthrough control isolates re-encoding as the causal factor. These findings, consistent with independent results on CogACT, suggest that VLA token compressibility is architecture-dependent and that learned re-encoding can overcome failures that deletion-based methods share.",
          "+Vision token pruning accelerates Vision Transformer inference with negligible accuracy loss, but whether this robustness transfers to Vision-Language-Action (VLA) models remains untested across architectures. We evaluate five VLA models (450M--7B parameters) spanning three connector families and identify four response classes governed by effective pipeline complexity. $\\pi_0$ (linear projection) is \\emph{immune}: offline action loss improves 2.4\\% at 90\\% removal. X-VLA (linear projection + encoder) is \\emph{threshold-graded}: 97.6\\% Success Rate (SR) at $k{=}0.9$, onset at $k{=}0.7$ (56.2\\%). OpenVLA (MLP projector) degrades \\emph{smoothly}: 74.0\\% $\\to$ 37.4\\% SR at 50\\% removal. SmolVLA (pixel-shuffle) hits a \\emph{catastrophic cliff}: 0\\% SR at 5\\% removal. The coefficient of variation (CV) of token importance predicts this ordering continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass. For cliff-edge architectures, a Vision Token Re-encoder (VTR) recovers 60\\%+ SR at 75\\% compression where all deletion methods yield 0\\%. VLA compressibility is architecture-dependent; CV diagnostic combined with VTR forms a Diagnose-then-Compress framework for safe token reduction.",
          " \\end{abstract}"
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01UiRaji5doS9FgJcy8txkkG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
  "old_string": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\\% $\\to$ 0\\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\\% $\\to$ 37.4\\%). The attention entropy ratio (0.95 vs.\\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\\% to 60--63\\% at 75\\% token reduction, where all deletion methods yield 0\\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
  "new_string": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe studied vision token pruning across five VLA models spanning three connector families. Five findings emerge. (1)~Compressibility is architecture-dependent: effective pipeline complexity, not model scale, determines pruning tolerance across a 16$\\times$ parameter range, producing four response classes. (2)~Pixel-shuffle connectors create irreversible spatial entanglement: SmolVLA collapses to 0\\% SR at 5\\% token removal, robust across seven pruning configurations and three mechanisms. (3)~Token importance CV predicts degradation onset continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass, at zero additional cost. (4)~VTR re-encoding overcomes the cliff-edge: both cross-attention and MLP modules recover 60\\%+ SR at 75\\% compression where deletion yields 0\\%, with a flat M-curve ($M{=}16 \\approx M{=}128$). (5)~Offline metrics underestimate closed-loop failure; $\\pi_0$'s offline immunity (2.4\\% improvement at $k{=}0.1$) requires closed-loop verification.\n\nThese results carry design implications. VLA architectures that require token efficiency should avoid pixel-shuffle connectors or include re-encoding modules. CV provides a zero-cost, single-forward-pass diagnostic that identifies vulnerability before deployment. Closed-loop evaluation remains essential for validating VLA compression. Code and evaluation scripts will be released upon publication."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "6df4d0c7-237c-44c7-8416-d7935d36d295",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2Rdr8pVVHNymKHdTgrkxQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7967,
      "cache_read_input_tokens": 41505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7967
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

_source line 22 · 2026-05-20T11:53:27.701Z_

<details><summary>↩ Tool result · `toolu_01UiRaji5doS9FgJcy8txkkG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "7babd849-9a46-4540-a674-d3e6cbd8f831",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
    "oldString": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\\% $\\to$ 0\\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\\% $\\to$ 37.4\\%). The attention entropy ratio (0.95 vs.\\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\\% to 60--63\\% at 75\\% token reduction, where all deletion methods yield 0\\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
    "newString": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe studied vision token pruning across five VLA models spanning three connector families. Five findings emerge. (1)~Compressibility is architecture-dependent: effective pipeline complexity, not model scale, determines pruning tolerance across a 16$\\times$ parameter range, producing four response classes. (2)~Pixel-shuffle connectors create irreversible spatial entanglement: SmolVLA collapses to 0\\% SR at 5\\% token removal, robust across seven pruning configurations and three mechanisms. (3)~Token importance CV predicts degradation onset continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass, at zero additional cost. (4)~VTR re-encoding overcomes the cliff-edge: both cross-attention and MLP modules recover 60\\%+ SR at 75\\% compression where deletion yields 0\\%, with a flat M-curve ($M{=}16 \\approx M{=}128$). (5)~Offline metrics underestimate closed-loop failure; $\\pi_0$'s offline immunity (2.4\\% improvement at $k{=}0.1$) requires closed-loop verification.\n\nThese results carry design implications. VLA architectures that require token efficiency should avoid pixel-shuffle connectors or include re-encoding modules. CV provides a zero-cost, single-forward-pass diagnostic that identifies vulnerability before deployment. Closed-loop evaluation remains essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
    "originalFile": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\\% $\\to$ 0\\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\\% $\\to$ 37.4\\%). The attention entropy ratio (0.95 vs.\\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\\% to 60--63\\% at 75\\% token reduction, where all deletion methods yield 0\\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 4,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\section{Conclusion}",
          " \\label{sec:conclusion}",
          " ",
          "-We presented the first systematic comparison of how vision connector design affects token pruning sensitivity in closed-loop VLA control. Compressibility is associated with the vision connector: pixel-shuffle connectors create spatially entangled tokens that collapse under any form of deletion (59.2\\% $\\to$ 0\\% on the official checkpoint), while MLP projectors degrade gracefully (74.0\\% $\\to$ 37.4\\%). The attention entropy ratio (0.95 vs.\\ 0.64) captures this divergence, consistent with independent findings on CogACT (EfficientVLA~\\cite{yang2025efficientvla}). For architectures where pruning fails, learned re-encoding recovers performance: both cross-attention and parameter-matched MLP modules raise SR from 44.8\\% to 60--63\\% at 75\\% token reduction, where all deletion methods yield 0\\%. The benefit depends on baseline feature quality, with larger gains on undertrained checkpoints. Re-encoding succeeds where deletion cannot, regardless of the specific module architecture. Standard offline metrics do not predict these closed-loop outcomes; closed-loop evaluation is essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
          "\\ No newline at end of file",
          "+We studied vision token pruning across five VLA models spanning three connector families. Five findings emerge. (1)~Compressibility is architecture-dependent: effective pipeline complexity, not model scale, determines pruning tolerance across a 16$\\times$ parameter range, producing four response classes. (2)~Pixel-shuffle connectors create irreversible spatial entanglement: SmolVLA collapses to 0\\% SR at 5\\% token removal, robust across seven pruning configurations and three mechanisms. (3)~Token importance CV predicts degradation onset continuously ($0.038 \\to 0.151 \\to 0.215 \\to 0.314$) from a single forward pass, at zero additional cost. (4)~VTR re-encoding overcomes the cliff-edge: both cross-attention and MLP modules recover 60\\%+ SR at 75\\% compression where deletion yields 0\\%, with a flat M-curve ($M{=}16 \\approx M{=}128$). (5)~Offline metrics underestimate closed-loop failure; $\\pi_0$'s offline immunity (2.4\\% improvement at $k{=}0.1$) requires closed-loop verification.",
          "+",
          "+These results carry design implications. VLA architectures that require token efficiency should avoid pixel-shuffle connectors or include re-encoding modules. CV provides a zero-cost, single-forward-pass diagnostic that identifies vulnerability before deployment. Closed-loop evaluation remains essential for validating VLA compression. Code and evaluation scripts will be released upon publication.",
          "\\ No newline at end of file"
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

_source line 23_

Both files rewritten. Key changes:

**Abstract** (~160 words): Reframed from 2-model (SmolVLA vs OpenVLA) to 5-model taxonomy with all four response classes listed explicitly (immune, threshold-graded, smooth graded, catastrophic cliff). CV spectrum and VTR as Diagnose-then-Compress framework. π0 marked offline.

**Conclusion** (~175 words): Structured as 5 enumerated claims (C1-C5) plus design implications paragraph. Numbers verified against Introduction/Results (CV values, SR figures, M-curve, 16× parameter range). Retained "Code and evaluation scripts will be released upon publication."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "uuid": "e94f28be-9e0e-44cc-ba75-517c3a02cb7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rJCMxmTLHTZA71nVU6sXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 49472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 964
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

_source line 24_

Both files rewritten. Key changes:

**Abstract** (~160 words): Reframed from 2-model (SmolVLA vs OpenVLA) to 5-model taxonomy with all four response classes listed explicitly (immune, threshold-graded, smooth graded, catastrophic cliff). CV spectrum and VTR as Diagnose-then-Compress framework. π0 marked offline.

**Conclusion** (~175 words): Structured as 5 enumerated claims (C1-C5) plus design implications paragraph. Numbers verified against Introduction/Results (CV values, SR figures, M-curve, 16× parameter range). Retained "Code and evaluation scripts will be released upon publication."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 178006,
  "duration_api_ms": 178879,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "b71f05b1-2721-4464-a9a5-3b6841b7bd60",
  "total_cost_usd": 0.54040925,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 38595,
    "cache_read_input_tokens": 127371,
    "output_tokens": 9334,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38595,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 158,
        "cache_read_input_tokens": 49472,
        "cache_creation_input_tokens": 964,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 964
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2015,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021249999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 9334,
      "cacheReadInputTokens": 127371,
      "cacheCreationInputTokens": 38595,
      "webSearchRequests": 0,
      "costUSD": 0.5382842499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fd77a441-31bd-4b67-9bb6-752d7d5f152f"
}
```

</details>

---
