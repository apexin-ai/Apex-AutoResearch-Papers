# paper writing conclusion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_writing_conclusion_20260523T014535.log`
- **Structured JSON:** [`de6f6e64689fe506d72e.json`](../../sessions/de/de6f6e64689fe506d72e.json)

## Before a recorded user message

27 recorded events

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
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
  "uuid": "5103b40e-6184-483d-ab1f-47f9337a925f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779513000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "500f80ba-22ff-4bf8-abbb-f9b06bf7783a",
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and reference materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "d69f8e2a-9fb0-4ae2-a49d-3195813d5dca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PERckngSVHunmSkiKbKM5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12460,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12460
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

<details open><summary>🔧 Tool call — Read · `toolu_01NDsQsV6FvRkHGurmuZ5ZLh`</summary>

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "a0e29249-4440-40ea-b989-93943c5ac6cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PERckngSVHunmSkiKbKM5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12460,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12460
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

_source line 6 · 2026-05-23T01:45:48.110Z_

<details><summary>↩ Tool result · `toolu_01NDsQsV6FvRkHGurmuZ5ZLh`</summary>

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "4fdaf683-2b27-40ae-8160-50a27e3299be",
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

<details open><summary>🔧 Tool call — Read · `toolu_019NU3sVNxjS3chzgof5wQDK`</summary>

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "482f53a7-fd52-4512-ab1e-693d7751591b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PERckngSVHunmSkiKbKM5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12460,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12460
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

_source line 8 · 2026-05-23T01:45:48.257Z_

<details><summary>↩ Tool result · `toolu_019NU3sVNxjS3chzgof5wQDK`</summary>

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "19c67d3f-78ce-4cef-918a-784943e4b033",
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

<details open><summary>🔧 Tool call — Read · `toolu_01HcKe7Ct4zQnumbCJzCVCnN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "29120aec-51b6-439f-a8f3-7029e172a409",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PERckngSVHunmSkiKbKM5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12460,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12460
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

_source line 10 · 2026-05-23T01:45:49.105Z_

<details><summary>↩ Tool result · `toolu_01HcKe7Ct4zQnumbCJzCVCnN`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA models spanning three connector families on the LIBERO benchmark~\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.
8	
9	Four models are evaluated in closed-loop robotic control: $\pi_0.5$~\cite{black2025pi05} (4B parameters, linear projection with $\times\!\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\cite{lewis2020bart}, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$ folding, 128 tokens, CV$\,{=}\,$0.314). Two additional models are analyzed via offline metrics only: $\pi_0$~\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\,{=}\,$0.038) and OFT~\cite{kim2025openoft} (7B, MLP projector, 512 tokens, CV$\,{=}\,$0.219). Table~\ref{tab:model_properties} summarizes model properties and connector details.
10	
11	The pruning protocol applies post-connector token pruning at retention ratios $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$. Two strategies bracket the robustness range: \textbf{L2 norm selection} ranks tokens by L2 norm and retains the top-$k$ fraction, providing an importance-based favorable test; \textbf{random subsampling} selects tokens uniformly at random, providing a conservative lower bound. Both strategies physically remove tokens and re-index position IDs. All results report mean success rate (SR) over 500 episodes with Wilson 95\% confidence intervals for single-seed conditions.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	The pruning response of a VLA model depends on two axes: the degree of token independence imposed by the vision connector, and the complexity of the downstream manipulation task. Models with token-independent connectors (MLP projectors, linear projections without deep post-processing) degrade gracefully under pruning, while models with token-entangling connectors exhibit sharp, task-dependent collapse. Figure~\ref{fig:teaser} illustrates this two-axis structure.
17	
18	Table~\ref{tab:main_results} presents closed-loop success rates across four models, four LIBERO suites, two pruning methods, and four retention ratios. The data reveal four qualitatively distinct response patterns spanning the connector spectrum (Figure~\ref{fig:pruning_overview}).
19	
20	\textbf{$\pi_0.5$ (linear, CV$\,{=}\,$0.055).} On Object, L2 norm selection yields 98.2\% at $k{=}0.95$, 98.2\% at $k{=}0.9$, and 98.0\% at $k{=}0.85$ (a plateau within 0.2\,pp of the 98.2\% baseline), then drops sharply to 55.0\% at $k{=}0.7$. Random selection follows a different trajectory: 69.4\% at $k{=}0.95$, 12.0\% at $k{=}0.9$, 77.2\% at $k{=}0.7$, and 69.4\% at $k{=}0.5$. The low CV implies near-uniform token norms, and the method choice produces gaps as large as 86.2\,pp (at $k{=}0.9$). On Spatial, $\pi_0.5$ maintains 97.8\% at $k{=}0.95$ (L2) and degrades to 55.6\% at $k{=}0.5$ (L2) versus 71.6\% (random). The pattern is consistent: low-CV models are not pruning-immune but uniformly critical, where the choice of which tokens to remove matters more than the number removed.
21	
22	\textbf{X-VLA (linear + BART encoder, CV$\,{=}\,$0.151).} X-VLA exhibits threshold-graded behavior with a pronounced interaction between retention ratio and task complexity. On Object, L2 norm selection preserves 99.0\% at $k{=}0.95$ and 99.2\% at $k{=}0.9$ (matching the baseline), then falls sharply to 68.0\% at $k{=}0.85$ with non-monotonic recovery to 89.0\% at $k{=}0.8$ before continued decline to 56.2\% at $k{=}0.7$. The same model at the same $k{=}0.9$ achieves only 70.2\% on Goal, a 29.0\,pp gap driven entirely by task complexity. On Long, removing just 3 of 50 tokens ($k{=}0.95$) collapses SR from 94.0\% to 47.0\%. The 12-layer BART encoder creates cross-token dependencies that amplify under compositional task demands.
23	
24	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA degrades smoothly across all retention ratios on Object: 70.6\% (L2) and 69.2\% (random) at $k{=}0.95$, 62.0\% and 63.4\% at $k{=}0.9$, 49.0\% and 48.5\% at $k{=}0.7$, 37.4\% and 35.7\% at $k{=}0.5$. The near-zero method gap (within 2\,pp at all retention ratios) reflects the MLP projector's per-patch independence: with a genuine importance gradient (CV$\,{=}\,$0.215), L2 norm ranking and random selection yield comparable spatial coverage. Degradation is proportional to the fraction removed, with no threshold effects.
25	
26	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} SmolVLA collapses to 0.0\% SR at every retention ratio across all four suites and both pruning methods, including $k{=}0.95$ where only 6 of 128 tokens are removed. This catastrophic cliff is detailed in Section~\ref{sec:pixel_shuffle}.
27	
28	\begin{table*}[t]
29	\centering
30	\small
31	\caption{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning at four retention ratios. Best result per row in \textbf{bold}. SmolVLA collapses to 0.0\% across all conditions. ``--'' indicates data not yet collected.}
32	\label{tab:main_results}
33	\begin{tabular}{llccccc}
34	\toprule
35	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
36	\midrule
37	\multirow{4}{*}{$\pi_0.5$}
38	& Object  & \textbf{98.2} & 98.2 / 69.4 & \textbf{98.2} / 12.0 & 55.0 / 77.2 & 33.4 / 69.4 \\
39	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
40	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.0 / -- & -- / 80.6 & 59.2 / 74.4 \\
41	& Long    & \textbf{91.6} & 86.8 / 61.2 & 81.0 / 31.8 & 60.0 / 64.6 & 50.2 / 50.2 \\
42	\midrule
43	\multirow{4}{*}{X-VLA}
44	& Object  & \textbf{99.2} & 99.0 / 98.8 & \textbf{99.2} / 97.8 & 56.2 / 65.2 & 42.6 / 70.6 \\
45	& Spatial & \textbf{91.6} & 71.6 / 70.2 & 78.8 / -- & 72.0 / -- & 58.8 / 71.4 \\
46	& Goal    & \textbf{98.0} & 53.8 / 54.0 & 70.2 / -- & 53.4 / -- & 61.0 / -- \\
47	& Long    & \textbf{94.0} & 47.0 / -- & 27.5 / -- & -- / -- & -- / -- \\
48	\midrule
49	OpenVLA & Object & \textbf{74.0} & 70.6 / 69.2 & 62.0 / 63.4 & 49.0 / 48.5 & 37.4 / 35.7 \\
50	\midrule
51	\multirow{4}{*}{SmolVLA}
52	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
53	& Spatial & \textbf{44.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
54	& Goal    & \textbf{60.8} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
55	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
56	\bottomrule
57	\end{tabular}
58	\end{table*}
59	
60	\subsection{Pixel-Shuffle Entanglement}
61	\label{sec:pixel_shuffle}
62	
63	SmolVLA's pixel-shuffle connector applies $4{\times}4$ spatial folding, concatenating 16 contiguous patches into the channel dimension of a single token. This operation creates irreversible cross-token spatial dependencies: each token encodes a $4{\times}4$ receptive field, and removing any token eliminates information from all 16 constituent patches with no redundancy in the remaining tokens.
64	
65	The consequence is catastrophic. SmolVLA collapses to 0.0\% SR at $k{=}0.95$ (removing 6 of 128 tokens, a 5\% reduction) across all four LIBERO suites (Object, Spatial, Goal, Long) and both pruning methods (L2 norm and random). We verified this result on two independent checkpoints: our LoRA fine-tuned reproduction (44.8\% SR baseline) and the official SmolVLA checkpoint (59.2\% SR baseline). Both exhibit identical collapse. The cliff is architectural, not a training artifact.
66	
67	The pixel-shuffle mechanism explains why the collapse is method-independent. Because all tokens carry spatially entangled information from non-overlapping $4{\times}4$ grids, no scoring function can identify ``dispensable'' tokens. L2 norm ranking and random selection fail equally because the problem is not which tokens are removed but that any removal breaks the spatial completeness the downstream LLM requires. In contrast, MLP projectors (OpenVLA) and linear projections ($\pi_0.5$) map patches independently. Each token retains per-patch spatial locality, so partial removal does not destroy information from unrelated spatial positions.
68	
69	\subsection{When Does Pruning Method Matter? CV as Sensitivity Indicator}
70	\label{sec:cv_sensitivity}
71	
72	Token importance CV (coefficient of variation of L2 norms) correlates with the retention ratio at which the choice of pruning method becomes critical. At mild pruning ($k{=}0.95$), a clear pattern emerges across the three closed-loop models with distinct CV values.
73	
74	For $\pi_0.5$ (CV$\,{=}\,$0.055), the method gap at $k{=}0.95$ is substantial: 98.2\% (L2) versus 69.4\% (random) on Object, a 28.8\,pp difference. On Spatial, the gap is 21.4\,pp (97.8\% vs.\ 76.4\%). The near-uniform token norms cause L2 norm ranking to exploit small spatial correlations rather than genuine importance differences, while random selection preserves the uniform spatial coverage these models depend on.
75	
76	For X-VLA (CV$\,{=}\,$0.151), the method gap at $k{=}0.95$ is minimal on Object (0.2\,pp; Table~\ref{tab:main_results}). Across three suites with available data, the method gap averages 0.6\,pp (range 0.2--1.4\,pp). The BART encoder produces tokens with a moderate importance gradient that both methods preserve at this mild pruning level.
77	
78	For OpenVLA (CV$\,{=}\,$0.215), the method gap at $k{=}0.95$ is 1.4\,pp on Object (70.6\% vs.\ 69.2\%). The MLP projector creates a clear importance hierarchy that renders both selection strategies nearly equivalent.
79	
80	The contrast is stark: $\pi_0.5$ exhibits a 28.8\,pp method gap where X-VLA and OpenVLA show gaps below 1.5\,pp. Low-CV models are an order of magnitude more sensitive to pruning method choice than higher-CV models at mild retention ratios. Figure~\ref{fig:method_gap} visualizes this relationship.
81	
82	At aggressive compression ($k{=}0.5$), the method-independence observed in moderate-CV models breaks down. On Object, the gap $\Delta$(R$-$L2) scales monotonically with CV: $\pi_0.5$ shows $+$36.0\,pp (random: 69.4\%, L2: 33.4\%), X-VLA shows $+$28.0\,pp (random: 70.6\%, L2: 42.6\%), and OpenVLA shows $-$1.7\,pp (random: 35.7\%, L2: 37.4\%). At 50\% retention, random selection outperforms L2 norm selection for both low-CV and moderate-CV models because random sampling preserves spatial diversity, while L2 norm ranking selects correlated high-norm tokens that cluster in similar image regions. Only OpenVLA, with CV above 0.2, produces a genuine importance gradient that L2 can exploit without spatial clustering artifacts.
83	
84	\subsection{Cross-Suite Task Complexity Effects}
85	\label{sec:cross_suite}
86	
87	LIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.
88	
89	$\pi_0.5$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\% (matching the baseline), Spatial retains 97.8\% (within noise of the 97.2\% baseline), and Goal drops to 89.4\% ($-$7.0\,pp from 96.4\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\% token removal.
90	
91	X-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains the full 99.2\% baseline, while Goal drops to 70.2\% ($-$27.8\,pp). Object absorbs 10\% token removal with zero loss; the same pruning ratio on multi-step tasks produces near-catastrophic degradation, driven entirely by task complexity with the same model and pruning method. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\% to 47.0\%, a 47.0\,pp loss, while Object at the same ratio loses only 0.2\,pp.
92	
93	Token-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\pi_0.5$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.
94	
95	\subsection{VTR Recovery}
96	\label{sec:vtr_recovery}
97	
98	Vision Token Re-encoder (VTR) addresses the catastrophic cliff through learned re-encoding rather than hard deletion. VTR inserts a lightweight cross-attention module ($\sim$22M parameters, approximately 5\% of SmolVLA) between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over the full set of 128 source tokens and produce $M$ compressed output representations, where $M \in \{16, 32, 64, 96, 128\}$. The $M{=}128$ configuration serves as a passthrough control that re-encodes without compressing.
99	
100	Table~\ref{tab:vtr_results} reports VTR results on SmolVLA for LIBERO-Object (3 seeds, 500 episodes each). Cross-attention VTR recovers substantial performance where hard pruning yields 0.0\%: $M{=}16$ (87.5\% compression) achieves 56.9 $\pm$ 1.3\%, $M{=}32$ (75\%) achieves 60.1 $\pm$ 1.3\%, $M{=}64$ (50\%) achieves 62.0 $\pm$ 2.2\%, $M{=}96$ (25\%) achieves 54.5 $\pm$ 3.2\%, and $M{=}128$ (0\%, passthrough) achieves 58.0 $\pm$ 3.5\%. The SmolVLA-Base (LoRA fine-tuned) baseline without VTR is 44.8\%, and the official SmolVLA baseline is 59.2\%.
101	
102	\begin{table}[t]
103	\centering
104	\small
105	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (passthrough) within 1.1\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}
106	\label{tab:vtr_results}
107	\begin{tabular}{lccr}
108	\toprule
109	Configuration & $M$ & Compression & SR (\%) \\
110	\midrule
111	\textit{SmolVLA-Base (LoRA)} & 128 & 0\% & 44.8 \\
112	\textit{SmolVLA official} & 128 & 0\% & 59.2 \\
113	\textit{Baseline control (+100K steps)} & 128 & 0\% & 45.0 \\
114	\textit{Hard pruning (any $k$)} & -- & 5--50\% & 0.0 \\
115	\midrule
116	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
117	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
118	Cross-attn VTR & 64 & 50\% & \textbf{62.0 $\pm$ 2.2} \\
119	Cross-attn VTR & 96 & 25\% & 54.5 $\pm$ 3.2 \\
120	Cross-attn VTR & 128 & 0\% & 58.0 $\pm$ 3.5 \\
121	\midrule
122	MLP adapter ($\sim$22M) & 32 & 75\% & 63.4 $\pm$ 2.6 \\
123	\bottomrule
124	\end{tabular}
125	\end{table}
126	
127	The M-curve is notably flat: performance at $M{=}16$ (56.9\%) falls within 1.1\,pp of $M{=}128$ (58.0\%), and all five $M$ values cluster within a 7.5\,pp range. This flatness confirms that the operative factor is learned re-encoding of spatially entangled tokens, not the compression ratio itself. The VTR module transforms pixel-shuffle representations into a format the downstream LLM can process robustly, and this transformation is effective regardless of how many output tokens carry the result.
128	
129	A parameter-matched MLP adapter ($\sim$22M parameters) achieves 63.4 $\pm$ 2.6\% at $M{=}32$, comparable to cross-attention VTR ($p = 0.15$). This confirms that re-encoding itself, rather than the specific attention mechanism, is the key architectural intervention. The baseline control (100K additional training steps without the compressor module) achieves only 45.0\% SR, within 0.2\,pp of the 44.8\% baseline. The performance gain is therefore attributable to the VTR architecture, not to additional optimization.
130	
131	Cross-suite evaluation at $M{=}32$ confirms that VTR recovery generalizes beyond Object: Spatial achieves 53.2\% and Goal achieves 56.4\%, both recovered from 0.0\% under hard pruning. VTR provides a targeted remedy for pixel-shuffle entanglement. By breaking the spatial dependencies that make hard deletion catastrophic, VTR enables both re-encoding recovery and downstream token reduction for deployment efficiency.
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "e8cc3bad-4817-4237-ba6e-fe04ceb15b75",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\nWe evaluate vision token pruning across six VLA models spanning three connector families on the LIBERO benchmark~\\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.\n\nFour models are evaluated in closed-loop robotic control: $\\pi_0.5$~\\cite{black2025pi05} (4B parameters, linear projection with $\\times\\!\\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\\cite{lewis2020bart}, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$ folding, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models are analyzed via offline metrics only: $\\pi_0$~\\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\\,{=}\\,$0.038) and OFT~\\cite{kim2025openoft} (7B, MLP projector, 512 tokens, CV$\\,{=}\\,$0.219). Table~\\ref{tab:model_properties} summarizes model properties and connector details.\n\nThe pruning protocol applies post-connector token pruning at retention ratios $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$. Two strategies bracket the robustness range: \\textbf{L2 norm selection} ranks tokens by L2 norm and retains the top-$k$ fraction, providing an importance-based favorable test; \\textbf{random subsampling} selects tokens uniformly at random, providing a conservative lower bound. Both strategies physically remove tokens and re-index position IDs. All results report mean success rate (SR) over 500 episodes with Wilson 95\\% confidence intervals for single-seed conditions.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\nThe pruning response of a VLA model depends on two axes: the degree of token independence imposed by the vision connector, and the complexity of the downstream manipulation task. Models with token-independent connectors (MLP projectors, linear projections without deep post-processing) degrade gracefully under pruning, while models with token-entangling connectors exhibit sharp, task-dependent collapse. Figure~\\ref{fig:teaser} illustrates this two-axis structure.\n\nTable~\\ref{tab:main_results} presents closed-loop success rates across four models, four LIBERO suites, two pruning methods, and four retention ratios. The data reveal four qualitatively distinct response patterns spanning the connector spectrum (Figure~\\ref{fig:pruning_overview}).\n\n\\textbf{$\\pi_0.5$ (linear, CV$\\,{=}\\,$0.055).} On Object, L2 norm selection yields 98.2\\% at $k{=}0.95$, 98.2\\% at $k{=}0.9$, and 98.0\\% at $k{=}0.85$ (a plateau within 0.2\\,pp of the 98.2\\% baseline), then drops sharply to 55.0\\% at $k{=}0.7$. Random selection follows a different trajectory: 69.4\\% at $k{=}0.95$, 12.0\\% at $k{=}0.9$, 77.2\\% at $k{=}0.7$, and 69.4\\% at $k{=}0.5$. The low CV implies near-uniform token norms, and the method choice produces gaps as large as 86.2\\,pp (at $k{=}0.9$). On Spatial, $\\pi_0.5$ maintains 97.8\\% at $k{=}0.95$ (L2) and degrades to 55.6\\% at $k{=}0.5$ (L2) versus 71.6\\% (random). The pattern is consistent: low-CV models are not pruning-immune but uniformly critical, where the choice of which tokens to remove matters more than the number removed.\n\n\\textbf{X-VLA (linear + BART encoder, CV$\\,{=}\\,$0.151).} X-VLA exhibits threshold-graded behavior with a pronounced interaction between retention ratio and task complexity. On Object, L2 norm selection preserves 99.0\\% at $k{=}0.95$ and 99.2\\% at $k{=}0.9$ (matching the baseline), then falls sharply to 68.0\\% at $k{=}0.85$ with non-monotonic recovery to 89.0\\% at $k{=}0.8$ before continued decline to 56.2\\% at $k{=}0.7$. The same model at the same $k{=}0.9$ achieves only 70.2\\% on Goal, a 29.0\\,pp gap driven entirely by task complexity. On Long, removing just 3 of 50 tokens ($k{=}0.95$) collapses SR from 94.0\\% to 47.0\\%. The 12-layer BART encoder creates cross-token dependencies that amplify under compositional task demands.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA degrades smoothly across all retention ratios on Object: 70.6\\% (L2) and 69.2\\% (random) at $k{=}0.95$, 62.0\\% and 63.4\\% at $k{=}0.9$, 49.0\\% and 48.5\\% at $k{=}0.7$, 37.4\\% and 35.7\\% at $k{=}0.5$. The near-zero method gap (within 2\\,pp at all retention ratios) reflects the MLP projector's per-patch independence: with a genuine importance gradient (CV$\\,{=}\\,$0.215), L2 norm ranking and random selection yield comparable spatial coverage. Degradation is proportional to the fraction removed, with no threshold effects.\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} SmolVLA collapses to 0.0\\% SR at every retention ratio across all four suites and both pruning methods, including $k{=}0.95$ where only 6 of 128 tokens are removed. This catastrophic cliff is detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning at four retention ratios. Best result per row in \\textbf{bold}. SmolVLA collapses to 0.0\\% across all conditions. ``--'' indicates data not yet collected.}\n\\label{tab:main_results}\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_0.5$}\n& Object  & \\textbf{98.2} & 98.2 / 69.4 & \\textbf{98.2} / 12.0 & 55.0 / 77.2 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.0 / -- & -- / 80.6 & 59.2 / 74.4 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 81.0 / 31.8 & 60.0 / 64.6 & 50.2 / 50.2 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & \\textbf{99.2} / 97.8 & 56.2 / 65.2 & 42.6 / 70.6 \\\\\n& Spatial & \\textbf{91.6} & 71.6 / 70.2 & 78.8 / -- & 72.0 / -- & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.0} & 53.8 / 54.0 & 70.2 / -- & 53.4 / -- & 61.0 / -- \\\\\n& Long    & \\textbf{94.0} & 47.0 / -- & 27.5 / -- & -- / -- & -- / -- \\\\\n\\midrule\nOpenVLA & Object & \\textbf{74.0} & 70.6 / 69.2 & 62.0 / 63.4 & 49.0 / 48.5 & 37.4 / 35.7 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\nSmolVLA's pixel-shuffle connector applies $4{\\times}4$ spatial folding, concatenating 16 contiguous patches into the channel dimension of a single token. This operation creates irreversible cross-token spatial dependencies: each token encodes a $4{\\times}4$ receptive field, and removing any token eliminates information from all 16 constituent patches with no redundancy in the remaining tokens.\n\nThe consequence is catastrophic. SmolVLA collapses to 0.0\\% SR at $k{=}0.95$ (removing 6 of 128 tokens, a 5\\% reduction) across all four LIBERO suites (Object, Spatial, Goal, Long) and both pruning methods (L2 norm and random). We verified this result on two independent checkpoints: our LoRA fine-tuned reproduction (44.8\\% SR baseline) and the official SmolVLA checkpoint (59.2\\% SR baseline). Both exhibit identical collapse. The cliff is architectural, not a training artifact.\n\nThe pixel-shuffle mechanism explains why the collapse is method-independent. Because all tokens carry spatially entangled information from non-overlapping $4{\\times}4$ grids, no scoring function can identify ``dispensable'' tokens. L2 norm ranking and random selection fail equally because the problem is not which tokens are removed but that any removal breaks the spatial completeness the downstream LLM requires. In contrast, MLP projectors (OpenVLA) and linear projections ($\\pi_0.5$) map patches independently. Each token retains per-patch spatial locality, so partial removal does not destroy information from unrelated spatial positions.\n\n\\subsection{When Does Pruning Method Matter? CV as Sensitivity Indicator}\n\\label{sec:cv_sensitivity}\n\nToken importance CV (coefficient of variation of L2 norms) correlates with the retention ratio at which the choice of pruning method becomes critical. At mild pruning ($k{=}0.95$), a clear pattern emerges across the three closed-loop models with distinct CV values.\n\nFor $\\pi_0.5$ (CV$\\,{=}\\,$0.055), the method gap at $k{=}0.95$ is substantial: 98.2\\% (L2) versus 69.4\\% (random) on Object, a 28.8\\,pp difference. On Spatial, the gap is 21.4\\,pp (97.8\\% vs.\\ 76.4\\%). The near-uniform token norms cause L2 norm ranking to exploit small spatial correlations rather than genuine importance differences, while random selection preserves the uniform spatial coverage these models depend on.\n\nFor X-VLA (CV$\\,{=}\\,$0.151), the method gap at $k{=}0.95$ is minimal on Object (0.2\\,pp; Table~\\ref{tab:main_results}). Across three suites with available data, the method gap averages 0.6\\,pp (range 0.2--1.4\\,pp). The BART encoder produces tokens with a moderate importance gradient that both methods preserve at this mild pruning level.\n\nFor OpenVLA (CV$\\,{=}\\,$0.215), the method gap at $k{=}0.95$ is 1.4\\,pp on Object (70.6\\% vs.\\ 69.2\\%). The MLP projector creates a clear importance hierarchy that renders both selection strategies nearly equivalent.\n\nThe contrast is stark: $\\pi_0.5$ exhibits a 28.8\\,pp method gap where X-VLA and OpenVLA show gaps below 1.5\\,pp. Low-CV models are an order of magnitude more sensitive to pruning method choice than higher-CV models at mild retention ratios. Figure~\\ref{fig:method_gap} visualizes this relationship.\n\nAt aggressive compression ($k{=}0.5$), the method-independence observed in moderate-CV models breaks down. On Object, the gap $\\Delta$(R$-$L2) scales monotonically with CV: $\\pi_0.5$ shows $+$36.0\\,pp (random: 69.4\\%, L2: 33.4\\%), X-VLA shows $+$28.0\\,pp (random: 70.6\\%, L2: 42.6\\%), and OpenVLA shows $-$1.7\\,pp (random: 35.7\\%, L2: 37.4\\%). At 50\\% retention, random selection outperforms L2 norm selection for both low-CV and moderate-CV models because random sampling preserves spatial diversity, while L2 norm ranking selects correlated high-norm tokens that cluster in similar image regions. Only OpenVLA, with CV above 0.2, produces a genuine importance gradient that L2 can exploit without spatial clustering artifacts.\n\n\\subsection{Cross-Suite Task Complexity Effects}\n\\label{sec:cross_suite}\n\nLIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.\n\n$\\pi_0.5$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\\% (matching the baseline), Spatial retains 97.8\\% (within noise of the 97.2\\% baseline), and Goal drops to 89.4\\% ($-$7.0\\,pp from 96.4\\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\\% token removal.\n\nX-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains the full 99.2\\% baseline, while Goal drops to 70.2\\% ($-$27.8\\,pp). Object absorbs 10\\% token removal with zero loss; the same pruning ratio on multi-step tasks produces near-catastrophic degradation, driven entirely by task complexity with the same model and pruning method. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\\% to 47.0\\%, a 47.0\\,pp loss, while Object at the same ratio loses only 0.2\\,pp.\n\nToken-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\\pi_0.5$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVision Token Re-encoder (VTR) addresses the catastrophic cliff through learned re-encoding rather than hard deletion. VTR inserts a lightweight cross-attention module ($\\sim$22M parameters, approximately 5\\% of SmolVLA) between the pixel-shuffle connector and the LLM backbone. $M$ learned queries attend over the full set of 128 source tokens and produce $M$ compressed output representations, where $M \\in \\{16, 32, 64, 96, 128\\}$. The $M{=}128$ configuration serves as a passthrough control that re-encodes without compressing.\n\nTable~\\ref{tab:vtr_results} reports VTR results on SmolVLA for LIBERO-Object (3 seeds, 500 episodes each). Cross-attention VTR recovers substantial performance where hard pruning yields 0.0\\%: $M{=}16$ (87.5\\% compression) achieves 56.9 $\\pm$ 1.3\\%, $M{=}32$ (75\\%) achieves 60.1 $\\pm$ 1.3\\%, $M{=}64$ (50\\%) achieves 62.0 $\\pm$ 2.2\\%, $M{=}96$ (25\\%) achieves 54.5 $\\pm$ 3.2\\%, and $M{=}128$ (0\\%, passthrough) achieves 58.0 $\\pm$ 3.5\\%. The SmolVLA-Base (LoRA fine-tuned) baseline without VTR is 44.8\\%, and the official SmolVLA baseline is 59.2\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (passthrough) within 1.1\\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}\n\\label{tab:vtr_results}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compression & SR (\\%) \\\\\n\\midrule\n\\textit{SmolVLA-Base (LoRA)} & 128 & 0\\% & 44.8 \\\\\n\\textit{SmolVLA official} & 128 & 0\\% & 59.2 \\\\\n\\textit{Baseline control (+100K steps)} & 128 & 0\\% & 45.0 \\\\\n\\textit{Hard pruning (any $k$)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 64 & 50\\% & \\textbf{62.0 $\\pm$ 2.2} \\\\\nCross-attn VTR & 96 & 25\\% & 54.5 $\\pm$ 3.2 \\\\\nCross-attn VTR & 128 & 0\\% & 58.0 $\\pm$ 3.5 \\\\\n\\midrule\nMLP adapter ($\\sim$22M) & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe M-curve is notably flat: performance at $M{=}16$ (56.9\\%) falls within 1.1\\,pp of $M{=}128$ (58.0\\%), and all five $M$ values cluster within a 7.5\\,pp range. This flatness confirms that the operative factor is learned re-encoding of spatially entangled tokens, not the compression ratio itself. The VTR module transforms pixel-shuffle representations into a format the downstream LLM can process robustly, and this transformation is effective regardless of how many output tokens carry the result.\n\nA parameter-matched MLP adapter ($\\sim$22M parameters) achieves 63.4 $\\pm$ 2.6\\% at $M{=}32$, comparable to cross-attention VTR ($p = 0.15$). This confirms that re-encoding itself, rather than the specific attention mechanism, is the key architectural intervention. The baseline control (100K additional training steps without the compressor module) achieves only 45.0\\% SR, within 0.2\\,pp of the 44.8\\% baseline. The performance gain is therefore attributable to the VTR architecture, not to additional optimization.\n\nCross-suite evaluation at $M{=}32$ confirms that VTR recovery generalizes beyond Object: Spatial achieves 53.2\\% and Goal achieves 56.4\\%, both recovered from 0.0\\% under hard pruning. VTR provides a targeted remedy for pixel-shuffle entanglement. By breaking the spatial dependencies that make hard deletion catastrophic, VTR enables both re-encoding recovery and downstream token reduction for deployment efficiency.\n",
      "numLines": 132,
      "startLine": 1,
      "totalLines": 132
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01B76cJ8gxHNRDA4ncStYM3G`</summary>

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "8308a959-941a-4510-8d42-0c1d2112b536",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PERckngSVHunmSkiKbKM5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12460,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12460
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

_source line 12 · 2026-05-23T01:45:49.383Z_

<details><summary>↩ Tool result · `toolu_01B76cJ8gxHNRDA4ncStYM3G`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to 0.0\% across all task suites and pruning methods. Apply the same 5\% reduction to $\pi_0.5$ and it retains 98.2\%. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\ 4B parameters) but the connector architecture. Token pruning is well-established for image classification, where DynamicViT~\cite{rao2021dynamicvit}, Token Merging~\cite{bolya2023tome}, and EViT~\cite{liang2022evit} reduce computation by 50\% or more with minimal accuracy loss. A growing body of work extends these techniques to VLAs: VLA-IAP~\cite{wang2026vlaiap}, VLA-Cache~\cite{hsu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, and VLA-Pruner~\cite{liu2025vlapruner} each demonstrate efficiency gains on individual architectures.
5	
6	These methods implicitly assume that token pruning effectiveness transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\cite{black2024pi0}, multi-layer MLP projectors~\cite{kim2024openvla}, pixel-shuffle spatial folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}. Each connector imposes distinct constraints on how visual information is distributed across tokens. Deploying a pruning method validated on one architecture to a different connector type risks silent degradation or, as the SmolVLA result above illustrates, complete loss of manipulation capability. No prior work systematically evaluates pruning robustness across both connector architectures and task complexity distributions, and the factor that determines whether a given VLA tolerates token removal remains uncharacterized.
7	
8	We propose a two-axis analysis of VLA token compressibility: pruning sensitivity as a function of connector coupling and task complexity (Figure~\ref{fig:teaser}). Along the coupling axis, token-independent connectors (linear projections, MLP projectors) degrade gracefully because each output token encodes information from a single input patch. Token-entangling connectors produce qualitatively different failures: SmolVLA's pixel-shuffle ($4{\times}4$ spatial folding) collapses to 0.0\% success rate at every retention ratio tested, while X-VLA's 12-layer BART encoder exhibits sharp, threshold-dependent drops. Along the task complexity axis, multi-step tasks amplify degradation in a connector-dependent manner. At retention ratio $k{=}0.9$, X-VLA retains its full 99.2\% baseline on single-step Object manipulation but loses 27.8 percentage points on multi-step Goal-conditioned tasks, a gap driven entirely by task demands at the same retention ratio. The coefficient of variation (CV) of post-connector token L2 norms captures connector coupling on a continuous spectrum from 0.038 ($\pi_0$, linear projection) to 0.314 (SmolVLA, pixel-shuffle) and correlates with both pruning tolerance and the retention threshold at which pruning method choice becomes critical. At $k{=}0.95$, $\pi_0.5$ (CV$\,{=}\,$0.055) exhibits method gaps of 28.8 percentage points on LIBERO-Object and 21.4 percentage points on Spatial, while X-VLA (CV$\,{=}\,$0.151) shows a 1.4 percentage point gap on the same Spatial suite---a 15$\times$ difference in method sensitivity.
9	
10	For pixel-shuffle connectors where all pruning strategies yield 0.0\% success rate, we introduce Vision Token Re-encoder (VTR), a lightweight cross-attention module (${\sim}$22M parameters, approximately 5\% of SmolVLA) that recovers over 60\% success rate through learned re-encoding at 75\% token compression. The VTR performance curve across output token counts $M$ is flat ($M{=}16$ matches $M{=}128$ within 1.1 percentage points), which confirms that learned re-encoding of spatially entangled representations, not the compression ratio, is the operative factor.
11	
12	Our contributions are:
13	\begin{itemize}
14	    \item A two-axis compressibility analysis validated across six VLA models (450M to 7B parameters) on four LIBERO~\cite{liu2023libero} task suites, which reveals connector architecture and task complexity as interacting determinants of pruning robustness.
15	    \item CV of token L2 norms as a single-pass diagnostic that correlates with both pruning tolerance and method sensitivity, and enables connector-appropriate compression strategy selection without downstream evaluation.
16	    \item Vision Token Re-encoder (VTR), a learned re-encoding module that recovers pixel-shuffle VLAs from 0.0\% to over 60\% success rate at 75\% token compression, where all hard pruning methods fail.
17	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "9ede5678-84fa-4324-9fdb-334642147a3e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nRemove 5\\% of vision tokens from SmolVLA and its success rate collapses from 59.2\\% to 0.0\\% across all task suites and pruning methods. Apply the same 5\\% reduction to $\\pi_0.5$ and it retains 98.2\\%. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\\ 4B parameters) but the connector architecture. Token pruning is well-established for image classification, where DynamicViT~\\cite{rao2021dynamicvit}, Token Merging~\\cite{bolya2023tome}, and EViT~\\cite{liang2022evit} reduce computation by 50\\% or more with minimal accuracy loss. A growing body of work extends these techniques to VLAs: VLA-IAP~\\cite{wang2026vlaiap}, VLA-Cache~\\cite{hsu2025vlacache}, EfficientVLA~\\cite{yang2025efficientvla}, and VLA-Pruner~\\cite{liu2025vlapruner} each demonstrate efficiency gains on individual architectures.\n\nThese methods implicitly assume that token pruning effectiveness transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\\cite{black2024pi0}, multi-layer MLP projectors~\\cite{kim2024openvla}, pixel-shuffle spatial folding~\\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\\cite{zheng2025xvla}. Each connector imposes distinct constraints on how visual information is distributed across tokens. Deploying a pruning method validated on one architecture to a different connector type risks silent degradation or, as the SmolVLA result above illustrates, complete loss of manipulation capability. No prior work systematically evaluates pruning robustness across both connector architectures and task complexity distributions, and the factor that determines whether a given VLA tolerates token removal remains uncharacterized.\n\nWe propose a two-axis analysis of VLA token compressibility: pruning sensitivity as a function of connector coupling and task complexity (Figure~\\ref{fig:teaser}). Along the coupling axis, token-independent connectors (linear projections, MLP projectors) degrade gracefully because each output token encodes information from a single input patch. Token-entangling connectors produce qualitatively different failures: SmolVLA's pixel-shuffle ($4{\\times}4$ spatial folding) collapses to 0.0\\% success rate at every retention ratio tested, while X-VLA's 12-layer BART encoder exhibits sharp, threshold-dependent drops. Along the task complexity axis, multi-step tasks amplify degradation in a connector-dependent manner. At retention ratio $k{=}0.9$, X-VLA retains its full 99.2\\% baseline on single-step Object manipulation but loses 27.8 percentage points on multi-step Goal-conditioned tasks, a gap driven entirely by task demands at the same retention ratio. The coefficient of variation (CV) of post-connector token L2 norms captures connector coupling on a continuous spectrum from 0.038 ($\\pi_0$, linear projection) to 0.314 (SmolVLA, pixel-shuffle) and correlates with both pruning tolerance and the retention threshold at which pruning method choice becomes critical. At $k{=}0.95$, $\\pi_0.5$ (CV$\\,{=}\\,$0.055) exhibits method gaps of 28.8 percentage points on LIBERO-Object and 21.4 percentage points on Spatial, while X-VLA (CV$\\,{=}\\,$0.151) shows a 1.4 percentage point gap on the same Spatial suite---a 15$\\times$ difference in method sensitivity.\n\nFor pixel-shuffle connectors where all pruning strategies yield 0.0\\% success rate, we introduce Vision Token Re-encoder (VTR), a lightweight cross-attention module (${\\sim}$22M parameters, approximately 5\\% of SmolVLA) that recovers over 60\\% success rate through learned re-encoding at 75\\% token compression. The VTR performance curve across output token counts $M$ is flat ($M{=}16$ matches $M{=}128$ within 1.1 percentage points), which confirms that learned re-encoding of spatially entangled representations, not the compression ratio, is the operative factor.\n\nOur contributions are:\n\\begin{itemize}\n    \\item A two-axis compressibility analysis validated across six VLA models (450M to 7B parameters) on four LIBERO~\\cite{liu2023libero} task suites, which reveals connector architecture and task complexity as interacting determinants of pruning robustness.\n    \\item CV of token L2 norms as a single-pass diagnostic that correlates with both pruning tolerance and method sensitivity, and enables connector-appropriate compression strategy selection without downstream evaluation.\n    \\item Vision Token Re-encoder (VTR), a learned re-encoding module that recovers pixel-shuffle VLAs from 0.0\\% to over 60\\% success rate at 75\\% token compression, where all hard pruning methods fail.\n\\end{itemize}",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
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
Now let me check the references.bib to verify any citation keys I might need for the conclusion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "efd7dce6-e5a9-4403-8100-b9e72326d23c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7XKxf4KrWxGodY5HtT3pi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18744,
      "cache_read_input_tokens": 24301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18744
      },
      "output_tokens": 11,
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

Now let me check the references file for any citation keys I might need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "fbd97352-503a-4c01-a053-eefbcaa7f183",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7XKxf4KrWxGodY5HtT3pi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18744,
      "cache_read_input_tokens": 24301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18744
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — Read · `toolu_01UFgCVSAsfFGw2BKPmY6Voq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "15fc08a8-e5f1-4f8d-a1cf-707b7ce36997",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7XKxf4KrWxGodY5HtT3pi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18744,
      "cache_read_input_tokens": 24301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18744
      },
      "output_tokens": 11,
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

_source line 16 · 2026-05-23T01:45:56.146Z_

<details><summary>↩ Tool result · `toolu_01UFgCVSAsfFGw2BKPmY6Voq`</summary>

```text
1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Token Compression (concurrent work)
8	% ============================================================
9	
10	@article{gao2025compressorvla,
11	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
12	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
13	  journal={arXiv preprint arXiv:2511.18950},
14	  year={2025},
15	  eprint={2511.18950},
16	  archivePrefix={arXiv}
17	}
18	
19	@article{wang2025specprunevla,
20	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
21	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
22	  journal={arXiv preprint arXiv:2509.05614},
23	  year={2025},
24	  eprint={2509.05614},
25	  archivePrefix={arXiv}
26	}
27	
28	@inproceedings{jiang2026lightvla,
29	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
30	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
31	  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
32	  year={2026},
33	  eprint={2509.12594},
34	  archivePrefix={arXiv}
35	}
36	
37	@inproceedings{feng2026seewhatmatters,
38	  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},
39	  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},
40	  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},
41	  year={2026},
42	  eprint={2605.11817},
43	  archivePrefix={arXiv}
44	}
45	
46	@inproceedings{zhang2025sparsevlm,
47	  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},
48	  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},
49	  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},
50	  year={2025},
51	  eprint={2410.04417},
52	  archivePrefix={arXiv}
53	}
54	
55	@inproceedings{khaki2025sparsevila,
56	  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},
57	  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},
58	  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
59	  year={2025},
60	  eprint={2510.17777},
61	  archivePrefix={arXiv}
62	}
63	
64	@article{jabbour2025dontrun,
65	  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},
66	  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},
67	  journal={arXiv preprint arXiv:2510.08464},
68	  year={2025},
69	  eprint={2510.08464},
70	  archivePrefix={arXiv}
71	}
72	
73	@inproceedings{li2024roboflamingo,
74	  title={Vision-Language Foundation Models as Effective Robot Imitators},
75	  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},
76	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
77	  year={2024},
78	  eprint={2311.01378},
79	  archivePrefix={arXiv}
80	}
81	
82	% ============================================================
83	% VLA Models
84	% ============================================================
85	
86	@article{shukor2025smolvla,
87	  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},
88	  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},
89	  journal={arXiv preprint arXiv:2506.01844},
90	  year={2025}
91	}
92	
93	@inproceedings{kim2024openvla,
94	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
95	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},
96	  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},
97	  year={2024}
98	}
99	
100	@inproceedings{brohan2023rt2,
101	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
102	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
103	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
104	  year={2023}
105	}
106	
107	
108	@article{black2024pi0,
109	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
110	  author={Black, Kevin and Brown, Noah and Driess, Danny and others},
111	  journal={arXiv preprint arXiv:2410.24164},
112	  year={2024}
113	}
114	
115	@article{black2025pi05,
116	  title={$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},
117	  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},
118	  journal={arXiv preprint arXiv:2504.16054},
119	  year={2025},
120	  eprint={2504.16054},
121	  archivePrefix={arXiv}
122	}
123	
124	@inproceedings{ghosh2024octo,
125	  title={Octo: An Open-Source Generalist Robot Policy},
126	  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},
127	  booktitle={Robotics: Science and Systems (RSS)},
128	  year={2024}
129	}
130	
131	@inproceedings{brohan2023rt1,
132	  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},
133	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
134	  booktitle={Robotics: Science and Systems (RSS)},
135	  year={2023}
136	}
137	
138	
139	% ============================================================
140	% VLM/LLM Token Efficiency
141	% ============================================================
142	
143	@inproceedings{chen2024fastv,
144	  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},
145	  author={Chen, Liang and others},
146	  booktitle={European Conference on Computer Vision (ECCV)},
147	  year={2024},
148	  note={Oral presentation}
149	}
150	
151	
152	@inproceedings{xu2025vlacache,
153	  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},
154	  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},
155	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
156	  year={2025}
157	}
158	
159	@article{cheng2026vlaiap,
160	  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},
161	  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},
162	  journal={arXiv preprint arXiv:2603.22991},
163	  year={2026}
164	}
165	
166	% ============================================================
167	% ViT Token Pruning/Merging
168	% ============================================================
169	
170	@inproceedings{rao2021dynamicvit,
171	  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},
172	  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},
173	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
174	  year={2021}
175	}
176	
177	@inproceedings{bolya2023tome,
178	  title={Token Merging: Your {ViT} But Faster},
179	  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},
180	  booktitle={International Conference on Learning Representations (ICLR)},
181	  year={2023}
182	}
183	
184	@inproceedings{liang2022evit,
185	  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},
186	  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},
187	  booktitle={International Conference on Learning Representations (ICLR)},
188	  year={2022}
189	}
190	
191	% ============================================================
192	% Closed-Loop Evaluation
193	% ============================================================
194	
195	@inproceedings{liu2023libero,
196	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
197	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
198	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
199	  year={2023}
200	}
201	
202	
203	% ============================================================
204	% Negative Results & Evaluation Pitfalls
205	% ============================================================
206	
207	
208	% ============================================================
209	% VLA Token Efficiency (new additions)
210	% ============================================================
211	
212	@article{yang2025efficientvla,
213	  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},
214	  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},
215	  journal={arXiv preprint arXiv:2506.10100},
216	  year={2025}
217	}
218	
219	@article{liu2025vlapruner,
220	  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},
221	  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},
222	  journal={arXiv preprint arXiv:2511.16449},
223	  year={2025}
224	}
225	
226	@inproceedings{shang2024prumerge,
227	  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},
228	  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},
229	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
230	  year={2025}
231	}
232	
233	% ============================================================
234	% Vision Connectors
235	% ============================================================
236	
237	@inproceedings{alayrac2022flamingo,
238	  title={Flamingo: a Visual Language Model for Few-Shot Learning},
239	  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},
240	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
241	  year={2022}
242	}
243	
244	@inproceedings{liu2023llava,
245	  title={Visual Instruction Tuning},
246	  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},
247	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
248	  year={2023}
249	}
250	
251	@inproceedings{shi2016subpixel,
252	  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},
253	  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},
254	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
255	  year={2016}
256	}
257	
258	@article{chen2024internvl,
259	  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},
260	  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},
261	  journal={arXiv preprint arXiv:2404.16821},
262	  year={2024}
263	}
264	
265	% ============================================================
266	% Background / Architecture
267	% ============================================================
268	
269	@inproceedings{li2023blip2,
270	  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},
271	  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},
272	  booktitle={International Conference on Machine Learning (ICML)},
273	  year={2023}
274	}
275	
276	@inproceedings{jaegle2021perceiver,
277	  title={Perceiver: General Perception with Iterative Attention},
278	  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},
279	  booktitle={International Conference on Machine Learning (ICML)},
280	  year={2021}
281	}
282	
283	@article{oquab2023dinov2,
284	  title={{DINOv2}: Learning Robust Visual Features without Supervision},
285	  author={Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and others},
286	  journal={Transactions on Machine Learning Research},
287	  year={2024}
288	}
289	
290	@inproceedings{zhai2023siglip,
291	  title={Sigmoid Loss for Language Image Pre-Training},
292	  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
293	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
294	  year={2023}
295	}
296	
297	@article{yang2024qwen2,
298	  title={Qwen2 Technical Report},
299	  author={Yang, An and others},
300	  journal={arXiv preprint arXiv:2407.10671},
301	  year={2024}
302	}
303	
304	@inproceedings{lipman2023flow,
305	  title={Flow Matching for Generative Modeling},
306	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
307	  booktitle={International Conference on Learning Representations (ICLR)},
308	  year={2023}
309	}
310	
311	% ============================================================
312	% Additional references (Round 3 reviewer request)
313	% ============================================================
314	
315	% ============================================================
316	% Additional VLA / VLM references
317	% ============================================================
318	
319	@article{li2024cogact,
320	  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},
321	  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},
322	  journal={arXiv preprint arXiv:2411.19650},
323	  year={2024},
324	  eprint={2411.19650},
325	  archivePrefix={arXiv}
326	}
327	
328	@article{kim2025openoft,
329	  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},
330	  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},
331	  journal={arXiv preprint arXiv:2502.19645},
332	  year={2025},
333	  eprint={2502.19645},
334	  archivePrefix={arXiv}
335	}
336	
337	@article{li2024tokenpacker,
338	  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},
339	  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},
340	  journal={arXiv preprint arXiv:2407.02392},
341	  year={2024},
342	  eprint={2407.02392},
343	  archivePrefix={arXiv}
344	}
345	
346	@inproceedings{zheng2025xvla,
347	  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},
348	  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},
349	  booktitle={International Conference on Learning Representations (ICLR)},
350	  year={2026},
351	  eprint={2510.10274},
352	  archivePrefix={arXiv}
353	}
354	
355	@article{wen2024tinyvla,
356	  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},
357	  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},
358	  journal={arXiv preprint arXiv:2409.12514},
359	  year={2024},
360	  eprint={2409.12514},
361	  archivePrefix={arXiv}
362	}
363	
364	@inproceedings{lewis2020bart,
365	  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},
366	  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},
367	  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},
368	  year={2020}
369	}
370	
371	% ============================================================
372	% New additions for expanded Related Work
373	% ============================================================
374	
375	@inproceedings{ryoo2021tokenlearner,
376	  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},
377	  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},
378	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
379	  year={2021},
380	  eprint={2106.11297},
381	  archivePrefix={arXiv}
382	}
383	
384	@inproceedings{yin2022avit,
385	  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},
386	  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},
387	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
388	  year={2022},
389	  eprint={2112.07658},
390	  archivePrefix={arXiv}
391	}
392	
393	@inproceedings{meng2022adavit,
394	  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},
395	  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},
396	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
397	  year={2022},
398	  eprint={2111.15668},
399	  archivePrefix={arXiv}
400	}
401	
402	@inproceedings{chen2023sparsevit,
403	  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},
404	  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},
405	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
406	  year={2023},
407	  eprint={2303.17605},
408	  archivePrefix={arXiv}
409	}
410	
411	@inproceedings{ye2025fitprune,
412	  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},
413	  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},
414	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
415	  year={2025},
416	  eprint={2409.10197},
417	  archivePrefix={arXiv}
418	}
419	
420	@inproceedings{shi2024crossget,
421	  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},
422	  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},
423	  booktitle={International Conference on Machine Learning (ICML)},
424	  year={2024},
425	  eprint={2305.17455},
426	  archivePrefix={arXiv}
427	}
428	
429	@article{zhang2024fastervlm,
430	  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},
431	  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},
432	  journal={arXiv preprint arXiv:2412.01818},
433	  year={2024},
434	  eprint={2412.01818},
435	  archivePrefix={arXiv}
436	}
437	
438	@inproceedings{liu2024llava15,
439	  title={Improved Baselines with Visual Instruction Tuning},
440	  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},
441	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
442	  year={2024},
443	  eprint={2310.03744},
444	  archivePrefix={arXiv}
445	}
446	
447	@article{chen2024internvl25,
448	  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},
449	  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},
450	  journal={arXiv preprint arXiv:2412.05271},
451	  year={2024},
452	  eprint={2412.05271},
453	  archivePrefix={arXiv}
454	}
455	
456	@article{gao2024miniinternvl,
457	  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\% Parameters and 90\% Performance},
458	  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},
459	  journal={arXiv preprint arXiv:2410.16261},
460	  year={2024},
461	  eprint={2410.16261},
462	  archivePrefix={arXiv}
463	}
464	
465	% ============================================================
466	% Synced from literature_map.yaml (missing entries)
467	% ============================================================
468	
469	% --- VLA Models ---
470	
471	@inproceedings{zitkovich2023rt2,
472	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
473	  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},
474	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
475	  year={2023},
476	  eprint={2307.15818},
477	  archivePrefix={arXiv}
478	}
479	
480	@inproceedings{openxembodiment2024,
481	  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},
482	  author={{Open X-Embodiment Collaboration}},
483	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
484	  year={2024},
485	  eprint={2310.08864},
486	  archivePrefix={arXiv}
487	}
488	
489	% --- VLM/LLM Token Efficiency ---
490	
491	@inproceedings{zhang2023h2o,
492	  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
493	  author={Zhang, Zhenyu and others},
494	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
495	  year={2023},
496	  eprint={2306.14048},
497	  archivePrefix={arXiv}
498	}
499	
500	@inproceedings{xiao2024streamingllm,
501	  title={Efficient Streaming Language Models with Attention Sinks},
502	  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},
503	  booktitle={International Conference on Learning Representations (ICLR)},
504	  year={2024},
505	  eprint={2309.17453},
506	  archivePrefix={arXiv}
507	}
508	
509	@inproceedings{hsu2025vlacache,
510	  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},
511	  author={Hsu, Siyu and others},
512	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
513	  year={2025},
514	  eprint={2502.02175},
515	  archivePrefix={arXiv}
516	}
517	
518	@article{wang2026vlaiap,
519	  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},
520	  author={Wang, others},
521	  journal={arXiv preprint arXiv:2603.22991},
522	  year={2026},
523	  eprint={2603.22991},
524	  archivePrefix={arXiv}
525	}
526	
527	% --- Closed-Loop Evaluation ---
528	
529	@article{mees2022calvin,
530	  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},
531	  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},
532	  journal={IEEE Robotics and Automation Letters},
533	  year={2022},
534	  eprint={2112.03227},
535	  archivePrefix={arXiv}
536	}
537	
538	@inproceedings{chi2023diffusionpolicy,
539	  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
540	  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
541	  booktitle={Robotics: Science and Systems (RSS)},
542	  year={2023},
543	  eprint={2303.04137},
544	  archivePrefix={arXiv}
545	}
546	
547	% --- Negative Results & Evaluation Pitfalls ---
548	
549	@inproceedings{zeng2023transformers_tsf,
550	  title={Are Transformers Effective for Time Series Forecasting?},
551	  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},
552	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
553	  year={2023},
554	  eprint={2205.13504},
555	  archivePrefix={arXiv}
556	}
557	
558	@inproceedings{bouthillier2024negative,
559	  title={Position: Embracing Negative Results in Machine Learning},
560	  author={Bouthillier, Xavier and others},
561	  booktitle={International Conference on Machine Learning (ICML)},
562	  year={2024},
563	  eprint={2406.03980},
564	  archivePrefix={arXiv}
565	}
566	
567	% --- Vision Connectors & Token Compression ---
568	
569	@article{oquab2024dinov2,
570	  title={{DINOv2}: Learning Robust Visual Features without Supervision},
571	  author={Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and others},
572	  journal={Transactions on Machine Learning Research},
573	  year={2024},
574	  eprint={2304.07193},
575	  archivePrefix={arXiv}
576	}
577	
578	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "fecbb9d0-89d3-4f72-a6ca-9b23dd73ff09",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{hsu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Hsu, Siyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  eprint={2502.02175},\n  archivePrefix={arXiv}\n}\n\n@article{wang2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Wang, others},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026},\n  eprint={2603.22991},\n  archivePrefix={arXiv}\n}\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}\n\n",
      "numLines": 578,
      "startLine": 1,
      "totalLines": 578
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
Now I have all the context I need. Let me write the Conclusion section. Key constraints:

1. ~200 words total (120 summary + 80 forward-looking)
2. No "In this paper, we..." opening
3. No em-dashes
4. No Furthermore/Moreover/Additionally
5. No delve/leverage/utilize/facilitate/significantly
6. No "In conclusion" / "In summary" / "To summarize"
7. CV = "correlates with", not "predicts/determines"
8. "analysis" not "framework"
9. 15× method sensitivity difference (not 24×)


10. X-VLA Object L2 k=0.9 = 99.2% (lossless)
11. Different wording from Abstract
12. Numbers consistent with experiments.tex

I'm verifying the key numbers against the experiments section to ensure consistency: the 15× sensitivity difference holds up, SmolVLA's performance at high compression matches the documented results, and X-VLA's object detection remains lossless at k=0.9 with 99.2% accuracy matching the baseline.

Now I'm checking the remaining claims—the 27.8 percentage point gap between methods at the same compression ratio and confirming we evaluated across 6 VLA models and 4 LIBERO suites. Everything checks out, so I'll move on to drafting the conclusion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "33c4dac5-ee10-44f4-9ff4-4e919b7a620b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FdroRoBLm1HdSkFPKvVG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9458,
      "cache_read_input_tokens": 43045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9458
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

_source line 18_

<details open><summary>🔧 Tool call — Write · `toolu_01PKpDLTgkLzea4q6oLpUFab`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nVision token pruning in VLAs is not a uniform operation: its outcome depends on the interaction between connector architecture and task complexity. Evaluating six VLA models (450M to 7B parameters) across four LIBERO task suites, we find that connector coupling is the primary determinant of pruning robustness. Token-independent connectors (linear projections, MLP projectors) degrade proportionally to the fraction removed, while token-entangling connectors (pixel-shuffle folding, BART encoder) exhibit task-amplified collapse. SmolVLA's pixel-shuffle connector produces 0.0\\% success rate when just 5\\% of tokens are removed; X-VLA retains its full 99.2\\% baseline on Object at $k{=}0.9$ but loses 27.8 percentage points on Goal at the same ratio. The coefficient of variation of post-connector token L2 norms captures this spectrum as a single-pass diagnostic: models with CV$\\,{=}\\,$0.055 show $15{\\times}$ greater method sensitivity than those with CV$\\,{\\geq}\\,$0.15, and this metric correlates with both pruning tolerance and the retention threshold at which method choice becomes critical. For architectures where all pruning strategies fail, Vision Token Re-encoder recovers pixel-shuffle VLAs from 0.0\\% to over 60\\% success rate at 75\\% compression through learned re-encoding.\n\nThese findings carry practical implications: computing CV before deployment can guide compression strategy selection without costly closed-loop evaluation. Two directions remain open. Real-robot validation is needed to confirm that the connector-complexity interaction observed in simulation transfers to physical manipulation. Adaptive per-task pruning schedules, where the retention ratio adjusts to estimated task complexity, could further close the gap between token-independent and token-entangling architectures.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "763df526-7cf4-4cf6-b3c8-d517dfb1b17a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FdroRoBLm1HdSkFPKvVG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9458,
      "cache_read_input_tokens": 43045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9458
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

_source line 19 · 2026-05-23T01:46:24.077Z_

<details><summary>↩ Tool result · reported error · `toolu_01PKpDLTgkLzea4q6oLpUFab`</summary>

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "15b70d03-0cbe-4695-879d-6e07911d5020",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ejk4eRVgFrvMx4veqAGFqo`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex 2>/dev/null; echo \"EXIT:$?\"",
  "description": "Check if conclusion.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "8d42f97f-5beb-41c6-9e7c-2fbe353caebb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQHGWsHXZLLMWht6im9eHi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 52503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 978
      },
      "output_tokens": 55,
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

_source line 21 · 2026-05-23T01:46:27.473Z_

<details><summary>↩ Tool result · `toolu_01Ejk4eRVgFrvMx4veqAGFqo`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex
EXIT:0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "22c4491e-be39-427c-bf52-1198857d4cf3",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex\nEXIT:0",
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01Qke4zjdUDqr94ZgYqXmG2a`</summary>

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "360e89b4-fbd8-461f-9d80-321822a928d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178CadaicR5kNGg5SLho4yn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 53481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 182
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

_source line 23 · 2026-05-23T01:46:29.918Z_

<details><summary>↩ Tool result · `toolu_01Qke4zjdUDqr94ZgYqXmG2a`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We studied vision token pruning across seven VLAs (450M--7B) on LIBERO. Token importance CV correlates with tolerance and strategy across four connector classes; low-CV models are uniformly critical ($\pi_0.5$: 36\,pp gap); learned re-encoding recovers 60\%+ SR where deletion yields 0\%.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "6aae67a9-940e-4b3a-b3c3-4458582bc604",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe studied vision token pruning across seven VLAs (450M--7B) on LIBERO. Token importance CV correlates with tolerance and strategy across four connector classes; low-CV models are uniformly critical ($\\pi_0.5$: 36\\,pp gap); learned re-encoding recovers 60\\%+ SR where deletion yields 0\\%.\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Write · `toolu_01LC2SwVvB6BDyooVeif5CS3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nVision token pruning in VLAs is not a uniform operation: its outcome depends on the interaction between connector architecture and task complexity. Evaluating six VLA models (450M to 7B parameters) across four LIBERO task suites, we find that connector coupling is the primary determinant of pruning robustness. Token-independent connectors (linear projections, MLP projectors) degrade proportionally to the fraction removed, while token-entangling connectors (pixel-shuffle folding, BART encoder) exhibit task-amplified collapse. SmolVLA's pixel-shuffle connector produces 0.0\\% success rate when just 5\\% of tokens are removed; X-VLA retains its full 99.2\\% baseline on Object at $k{=}0.9$ but loses 27.8 percentage points on Goal at the same ratio. The coefficient of variation of post-connector token L2 norms captures this spectrum as a single-pass diagnostic: models with CV$\\,{=}\\,$0.055 show $15{\\times}$ greater method sensitivity than those with CV$\\,{\\geq}\\,$0.15, and this metric correlates with both pruning tolerance and the retention threshold at which method choice becomes critical. For architectures where all pruning strategies fail, Vision Token Re-encoder recovers pixel-shuffle VLAs from 0.0\\% to over 60\\% success rate at 75\\% compression through learned re-encoding.\n\nThese findings carry practical implications: computing CV before deployment can guide compression strategy selection without costly closed-loop evaluation. Two directions remain open. Real-robot validation is needed to confirm that the connector-complexity interaction observed in simulation transfers to physical manipulation. Adaptive per-task pruning schedules, where the retention ratio adjusts to estimated task complexity, could further close the gap between token-independent and token-entangling architectures.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "6c061ad7-2865-45a4-8ca3-fdbd2b7c9499",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEHaMXLXr88jK7R1nYRUzD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 53663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 25 · 2026-05-23T01:46:35.153Z_

<details><summary>↩ Tool result · `toolu_01LC2SwVvB6BDyooVeif5CS3`</summary>

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
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "33d04937-af61-4e0b-a742-ce5bf3b6a064",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nVision token pruning in VLAs is not a uniform operation: its outcome depends on the interaction between connector architecture and task complexity. Evaluating six VLA models (450M to 7B parameters) across four LIBERO task suites, we find that connector coupling is the primary determinant of pruning robustness. Token-independent connectors (linear projections, MLP projectors) degrade proportionally to the fraction removed, while token-entangling connectors (pixel-shuffle folding, BART encoder) exhibit task-amplified collapse. SmolVLA's pixel-shuffle connector produces 0.0\\% success rate when just 5\\% of tokens are removed; X-VLA retains its full 99.2\\% baseline on Object at $k{=}0.9$ but loses 27.8 percentage points on Goal at the same ratio. The coefficient of variation of post-connector token L2 norms captures this spectrum as a single-pass diagnostic: models with CV$\\,{=}\\,$0.055 show $15{\\times}$ greater method sensitivity than those with CV$\\,{\\geq}\\,$0.15, and this metric correlates with both pruning tolerance and the retention threshold at which method choice becomes critical. For architectures where all pruning strategies fail, Vision Token Re-encoder recovers pixel-shuffle VLAs from 0.0\\% to over 60\\% success rate at 75\\% compression through learned re-encoding.\n\nThese findings carry practical implications: computing CV before deployment can guide compression strategy selection without costly closed-loop evaluation. Two directions remain open. Real-robot validation is needed to confirm that the connector-complexity interaction observed in simulation transfers to physical manipulation. Adaptive per-task pruning schedules, where the retention ratio adjusts to estimated task complexity, could further close the gap between token-independent and token-entangling architectures.\n",
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
          "-We studied vision token pruning across seven VLAs (450M--7B) on LIBERO. Token importance CV correlates with tolerance and strategy across four connector classes; low-CV models are uniformly critical ($\\pi_0.5$: 36\\,pp gap); learned re-encoding recovers 60\\%+ SR where deletion yields 0\\%.",
          "+Vision token pruning in VLAs is not a uniform operation: its outcome depends on the interaction between connector architecture and task complexity. Evaluating six VLA models (450M to 7B parameters) across four LIBERO task suites, we find that connector coupling is the primary determinant of pruning robustness. Token-independent connectors (linear projections, MLP projectors) degrade proportionally to the fraction removed, while token-entangling connectors (pixel-shuffle folding, BART encoder) exhibit task-amplified collapse. SmolVLA's pixel-shuffle connector produces 0.0\\% success rate when just 5\\% of tokens are removed; X-VLA retains its full 99.2\\% baseline on Object at $k{=}0.9$ but loses 27.8 percentage points on Goal at the same ratio. The coefficient of variation of post-connector token L2 norms captures this spectrum as a single-pass diagnostic: models with CV$\\,{=}\\,$0.055 show $15{\\times}$ greater method sensitivity than those with CV$\\,{\\geq}\\,$0.15, and this metric correlates with both pruning tolerance and the retention threshold at which method choice becomes critical. For architectures where all pruning strategies fail, Vision Token Re-encoder recovers pixel-shuffle VLAs from 0.0\\% to over 60\\% success rate at 75\\% compression through learned re-encoding.",
          "+",
          "+These findings carry practical implications: computing CV before deployment can guide compression strategy selection without costly closed-loop evaluation. Two directions remain open. Real-robot validation is needed to confirm that the connector-complexity interaction observed in simulation transfers to physical manipulation. Adaptive per-task pruning schedules, where the retention ratio adjusts to estimated task complexity, could further close the gap between token-independent and token-entangling architectures."
        ]
      }
    ],
    "originalFile": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe studied vision token pruning across seven VLAs (450M--7B) on LIBERO. Token importance CV correlates with tolerance and strategy across four connector classes; low-CV models are uniformly critical ($\\pi_0.5$: 36\\,pp gap); learned re-encoding recovers 60\\%+ SR where deletion yields 0\\%.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 26_

文件已写入。~210 words，包含两段：summary (~130 words) 总结 connector coupling 作为 pruning robustness 主要决定因素、CV diagnostic、VTR recovery；forward-looking (~80 words) 覆盖 CV 实际应用意义和两个未来方向（real-robot validation, adaptive per-task pruning）。所有数字与 experiments.tex 一致（99.2%, 27.8pp, 15×, 0.055/0.15, 60%+, 75%）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "uuid": "5d27bf68-47e8-401d-bbab-efa721def750",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSDrduBW1TS2X8QCtn4H41",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 597,
      "cache_read_input_tokens": 53976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 597
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

_source line 27_

文件已写入。~210 words，包含两段：summary (~130 words) 总结 connector coupling 作为 pruning robustness 主要决定因素、CV diagnostic、VTR recovery；forward-looking (~80 words) 覆盖 CV 实际应用意义和两个未来方向（real-robot validation, adaptive per-task pruning）。所有数字与 experiments.tex 一致（99.2%, 27.8pp, 15×, 0.055/0.15, 60%+, 75%）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 55515,
  "duration_api_ms": 56239,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "397562ab-71c1-42e4-aa33-aeb0d287cd28",
  "total_cost_usd": 0.47234300000000007,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 42732,
    "cache_read_input_tokens": 292810,
    "output_tokens": 2279,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42732,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 145,
        "cache_read_input_tokens": 53976,
        "cache_creation_input_tokens": 597,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 597
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1763,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001843,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 2279,
      "cacheReadInputTokens": 292810,
      "cacheCreationInputTokens": 42732,
      "webSearchRequests": 0,
      "costUSD": 0.47050000000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7fd02a56-36ad-485c-89a6-b0d9c4531868"
}
```

</details>

---
