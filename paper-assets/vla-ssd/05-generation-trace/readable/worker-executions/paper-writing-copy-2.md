# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_writing_20260522T061909.log`
- **Structured JSON:** [`fa630ed95d8cfa76d8c4.json`](../../sessions/fa/fa630ed95d8cfa76d8c4.json)

## Before a recorded user message

21 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
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
  "uuid": "b969ee15-c385-4e7e-a481-f1e0341868ad",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779448200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "29d9ea0a-b4d0-4e56-8d47-8ba90472c852",
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and the current method.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "71d31f6a-1287-49d4-b7db-8f9d33613e15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vSwrmTeRGuxUmG4VQ9igt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12391
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

<details open><summary>🔧 Tool call — Read · `toolu_01M2GkXUxj9rL97yggdts5LU`</summary>

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
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "a74c143f-450b-4911-b942-db8dba975c48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vSwrmTeRGuxUmG4VQ9igt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12391
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

_source line 6 · 2026-05-22T06:19:26.851Z_

<details><summary>↩ Tool result · `toolu_01M2GkXUxj9rL97yggdts5LU`</summary>

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
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "f321fdd1-cdab-468f-8bb6-d52a2f49e7cf",
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

<details open><summary>🔧 Tool call — Read · `toolu_01PoXnMd2rSwt3StE3G1cA2F`</summary>

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
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "70d9c872-c643-4dc4-b9bb-fcf3af96c980",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vSwrmTeRGuxUmG4VQ9igt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12391
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

_source line 8 · 2026-05-22T06:19:27.292Z_

<details><summary>↩ Tool result · `toolu_01PoXnMd2rSwt3StE3G1cA2F`</summary>

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
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "a3e87d86-be99-4408-990b-cedf01d221f4",
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

<details open><summary>🔧 Tool call — Read · `toolu_01DRjmJrKJcwvNfgpo8i9gfT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "ca53115e-960e-47cd-bc08-49b9391d1540",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vSwrmTeRGuxUmG4VQ9igt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12391
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

_source line 10 · 2026-05-22T06:19:27.425Z_

<details><summary>↩ Tool result · `toolu_01DRjmJrKJcwvNfgpo8i9gfT`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.
5	
6	%------------------------------------------------------------------
7	\subsection{Architectures and Data}
8	\label{sec:arch_data}
9	
10	We study three VLAs that span distinct backbone families (Table~\ref{tab:arch_overview}).
11	\textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2-7B~\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.
12	Its base checkpoint is pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).
13	\textbf{TracVLA}~\cite{zheng2024tracevla} uses Phi-3-mini~\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.
14	\textbf{NORA}~\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.
15	
16	Each architecture is evaluated in trained and untrained conditions.
17	A critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
18	OpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.
19	This asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.
20	For OpenVLA, two additional conditions support deep-dive analyses (\S\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \texttt{from\_config()}.
21	
22	We evaluate on LIBERO~\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.
23	The three architectures and four suites form a $3 \times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).
24	
25	\begin{table}[t]
26	\centering
27	\caption{Architectures studied. The untrained baselines differ in kind: OpenVLA's baseline is an OXE-pretrained VLA that produces actions; TracVLA and NORA baselines are pure VLMs with no action training.}
28	\label{tab:arch_overview}
29	\footnotesize
30	\setlength{\tabcolsep}{3pt}
31	\begin{tabular}{@{}llccll@{}}
32	\toprule
33	Arch. & Backbone & Layers & Attention & Vision Enc. & Untrained Baseline \\
34	\midrule
35	OpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\to$ MLP proj. & OXE-pret.\ VLA \\
36	TracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\
37	NORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\
38	\bottomrule
39	\end{tabular}
40	\end{table}
41	
42	%------------------------------------------------------------------
43	\subsection{Representation Extraction}
44	\label{sec:repr_extraction}
45	
46	From each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\textbf{image\_mean}, the mean activation over image tokens, and (b)~\textbf{readout}, the hidden state at the final pre-action token, which follows both image and instruction tokens in the causal sequence and can attend to all preceding context.
47	L0 denotes the embedding layer output, L1 through L$N$ the hidden states after each transformer layer ($N = 32$ for OpenVLA and TracVLA, $N = 36$ for NORA), with the final layer including the output layer norm.
48	In all three architectures, image tokens precede instruction tokens; the causal mask prevents image tokens from attending to instructions by construction.
49	
50	We cross two factors in a $2 \times 2$ factorial design: \emph{training status} (trained vs.\ untrained) and \emph{instruction presence} (with vs.\ without task description), applied to all 10 available cells in the cross-architecture matrix.
51	OpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\S\ref{sec:openvla_routing}).
52	
53	%------------------------------------------------------------------
54	\subsection{Cross-Architecture Analyses}
55	\label{sec:cross_arch_analyses}
56	
57	Three analyses are applied to every available cell in the $3 \times 4$ matrix.
58	
59	\paragraph{$R^2$ action probes.}
60	Two-layer MLP probes~\cite{alain2017} ($d_\text{in} \to 256 \to 7$, ReLU) are trained to predict 7-D action vectors from frozen representations at each layer (Adam, lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5).
61	Train/test splits follow demonstration boundaries (demos 0--39 vs.\ 40--49) to prevent within-trajectory leakage.
62	We report per-task macro-averaged $R^2$ with bootstrap paired comparisons (10{,}000 resamples).
63	
64	\paragraph{L1 attention head profiling.}
65	At L1, each attention head is classified as instruction-dominant ($>50\%$ of readout-token attention allocated to instruction tokens) or image-dominant.
66	Results are reported as $k/N$ instruction-dominant heads, where $N$ is the total L1 head count: 32 for OpenVLA and TracVLA (MHA), 16 for NORA (GQA query heads).
67	Sensitivity analysis at thresholds from $30\%$ to $70\%$ confirms ordering robustness (Appendix~\ref{sec:threshold_sensitivity}).
68	
69	\paragraph{Counterfactual instruction perturbation.}
70	The instruction is replaced with four conditions: empty string, wrong task from the same suite, shuffled tokens, and paraphrased instruction.
71	A metric constraint arises from the trained/untrained asymmetry.
72	Trained models produce action outputs; their sensitivity is measured via Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action representations (NORA).
73	Untrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations, a metric with different scale and distributional properties.
74	Cross-metric ratios between Cohen's $d$ and cosine distance are therefore invalid (\S\ref{sec:cf_sensitivity}).
75	OpenVLA's OXE-pretrained untrained checkpoint is the exception: because it produces actions, same-metric (Cohen's $d$) trained-vs-untrained comparison is possible for that condition.
76	
77	%------------------------------------------------------------------
78	\subsection{OpenVLA-Specific Analyses}
79	\label{sec:openvla_analyses}
80	
81	Three additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.
82	
83	\paragraph{Cross-instruction probes.}
84	Each visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.
85	A 10-way linear classifier identifies which instruction was present, applied separately to image\_mean and readout positions, with leave-one-out cross-validation (LOOCV) over 10 folds.
86	
87	\paragraph{Representational similarity analysis (RSA).}
88	RSA~\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.
89	For each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.
90	Alignment is measured via Spearman $\rho$ between upper-triangular RDM entries; we report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap resamples at the task level~\cite{nili2014toolbox}.
91	We prefer RSA over CKA~\cite{kornblith2019}: RSA captures relative distance structure via scale-invariant rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\ 7-D), while CKA measures global subspace overlap that can remain high when geometric structure differs.
92	Both metrics are reported in Appendix~\ref{sec:cka_appendix}; their divergence (\S\ref{sec:routing_synthesis}) confirms that neither alone fully characterizes representational structure.
93	
94	\paragraph{External baselines.}
95	DINOv2 ViT-L/14~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}) and CLIP ViT-L/14~\cite{radford2021_clip} (\texttt{patch\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.
96	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "17b65375-f303-47cd-a8fc-319acc94db45",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.\n\n%------------------------------------------------------------------\n\\subsection{Architectures and Data}\n\\label{sec:arch_data}\n\nWe study three VLAs that span distinct backbone families (Table~\\ref{tab:arch_overview}).\n\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIts base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.\n\nEach architecture is evaluated in trained and untrained conditions.\nA critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.\nOpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.\nThis asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.\nFor OpenVLA, two additional conditions support deep-dive analyses (\\S\\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \\texttt{from\\_config()}.\n\nWe evaluate on LIBERO~\\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.\nThe three architectures and four suites form a $3 \\times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).\n\n\\begin{table}[t]\n\\centering\n\\caption{Architectures studied. The untrained baselines differ in kind: OpenVLA's baseline is an OXE-pretrained VLA that produces actions; TracVLA and NORA baselines are pure VLMs with no action training.}\n\\label{tab:arch_overview}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccll@{}}\n\\toprule\nArch. & Backbone & Layers & Attention & Vision Enc. & Untrained Baseline \\\\\n\\midrule\nOpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\\to$ MLP proj. & OXE-pret.\\ VLA \\\\\nTracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\\\\nNORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nFrom each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\\textbf{image\\_mean}, the mean activation over image tokens, and (b)~\\textbf{readout}, the hidden state at the final pre-action token, which follows both image and instruction tokens in the causal sequence and can attend to all preceding context.\nL0 denotes the embedding layer output, L1 through L$N$ the hidden states after each transformer layer ($N = 32$ for OpenVLA and TracVLA, $N = 36$ for NORA), with the final layer including the output layer norm.\nIn all three architectures, image tokens precede instruction tokens; the causal mask prevents image tokens from attending to instructions by construction.\n\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained) and \\emph{instruction presence} (with vs.\\ without task description), applied to all 10 available cells in the cross-architecture matrix.\nOpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\\S\\ref{sec:openvla_routing}).\n\n%------------------------------------------------------------------\n\\subsection{Cross-Architecture Analyses}\n\\label{sec:cross_arch_analyses}\n\nThree analyses are applied to every available cell in the $3 \\times 4$ matrix.\n\n\\paragraph{$R^2$ action probes.}\nTwo-layer MLP probes~\\cite{alain2017} ($d_\\text{in} \\to 256 \\to 7$, ReLU) are trained to predict 7-D action vectors from frozen representations at each layer (Adam, lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5).\nTrain/test splits follow demonstration boundaries (demos 0--39 vs.\\ 40--49) to prevent within-trajectory leakage.\nWe report per-task macro-averaged $R^2$ with bootstrap paired comparisons (10{,}000 resamples).\n\n\\paragraph{L1 attention head profiling.}\nAt L1, each attention head is classified as instruction-dominant ($>50\\%$ of readout-token attention allocated to instruction tokens) or image-dominant.\nResults are reported as $k/N$ instruction-dominant heads, where $N$ is the total L1 head count: 32 for OpenVLA and TracVLA (MHA), 16 for NORA (GQA query heads).\nSensitivity analysis at thresholds from $30\\%$ to $70\\%$ confirms ordering robustness (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Counterfactual instruction perturbation.}\nThe instruction is replaced with four conditions: empty string, wrong task from the same suite, shuffled tokens, and paraphrased instruction.\nA metric constraint arises from the trained/untrained asymmetry.\nTrained models produce action outputs; their sensitivity is measured via Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action representations (NORA).\nUntrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations, a metric with different scale and distributional properties.\nCross-metric ratios between Cohen's $d$ and cosine distance are therefore invalid (\\S\\ref{sec:cf_sensitivity}).\nOpenVLA's OXE-pretrained untrained checkpoint is the exception: because it produces actions, same-metric (Cohen's $d$) trained-vs-untrained comparison is possible for that condition.\n\n%------------------------------------------------------------------\n\\subsection{OpenVLA-Specific Analyses}\n\\label{sec:openvla_analyses}\n\nThree additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.\n\n\\paragraph{Cross-instruction probes.}\nEach visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.\nA 10-way linear classifier identifies which instruction was present, applied separately to image\\_mean and readout positions, with leave-one-out cross-validation (LOOCV) over 10 folds.\n\n\\paragraph{Representational similarity analysis (RSA).}\nRSA~\\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.\nFor each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.\nAlignment is measured via Spearman $\\rho$ between upper-triangular RDM entries; we report mean $\\rho$ across 10 tasks with 95\\% confidence intervals from 10{,}000 bootstrap resamples at the task level~\\cite{nili2014toolbox}.\nWe prefer RSA over CKA~\\cite{kornblith2019}: RSA captures relative distance structure via scale-invariant rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\\ 7-D), while CKA measures global subspace overlap that can remain high when geometric structure differs.\nBoth metrics are reported in Appendix~\\ref{sec:cka_appendix}; their divergence (\\S\\ref{sec:routing_synthesis}) confirms that neither alone fully characterizes representational structure.\n\n\\paragraph{External baselines.}\nDINOv2 ViT-L/14~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}) and CLIP ViT-L/14~\\cite{radford2021_clip} (\\texttt{patch\\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.\n",
      "numLines": 96,
      "startLine": 1,
      "totalLines": 96
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
Now I have a clear picture. Let me analyze what needs to change:

### 1. §3.1 Architecture balance
Current state:
- **OpenVLA** (line 11-12): ~2.5 lines of detail — mentions DinoSigLIP, specific dim (2176-D→4096-D), Llama-2-7B, 6.74B params, 32 layers, 32 MHA heads, autoregressive 7-D action decoding.
- **TracVLA** (line 13): ~1 line — mentions Phi-3-mini, 32 layers, 32 MHA heads, SigLIP encoder + spatial trace conditioning, OXE subset.


- **NORA** (line 14): ~1 line — mentions Qwen2.5-VL-3B, 36 layers, GQA with 16 query/2 KV heads, native vision encoder.

Fix: Compress OpenVLA, expand TracVLA and NORA.

For OpenVLA: Remove the MLP projector dimensions (2176-D → 4096-D) and the 6.74B parameter count — these can be inferred from Table 1 or are excessive detail. Keep the essentials.

For TracVLA: Add 3.8B parameter count, briefly explain spatial trace conditioning.

For NORA: Add ~3B parameter count, briefly explain native vision encoder.

### 2.

Now I'm scanning through the document for terminology consistency — checking that terms like "$R^2$ exit collapse," "counterfactual sensitivity," "instruction-dominant," "readout token," and "cross-instruction probes" are used correctly throughout. Spot-checking a few key lines shows the terminology is already aligned, so I'll do a more comprehensive pass to catch any remaining inconsistencies.

I'm also reviewing the CoRL style guidelines — looking for em-dashes, -ing phrase endings, and transition words like "Furthermore" or "Notably" that might need adjustment. The text appears clean on these fronts so far.

Before making edits, I want to confirm what stays untouched: the §3.4 structure, Table 1, all citation and label commands, and cross-references. Now I'm ready to draft the specific edits, starting with balancing the architecture descriptions in §3.1. TracVLA uses Phi-3-mini with spatial trace conditioning on an OXE subset, while NORA leverages Qwen2.5-VL-3B with its native vision encoder and grouped-query attention. NORA uses Qwen2.5-VL, a 3B parameter model with grouped-query attention, paired with its native vision encoder that handles variable resolution images directly. I need to balance the detail across all three architectures so they're roughly equal in length and information density. OpenVLA currently has more specifics than TracVLA and NORA, so I'm trimming the projector dimension details while keeping the parameter count since I'm adding it for the other two models. My plan is to give each architecture about 2-3 lines with consistent levels of detail—OpenVLA gets its vision backbone and parameter count, TracVLA gets the spatial trace conditioning and parameters, and NORA gets its native vision encoder and parameters.

Writing the architecture descriptions... I'm completing the OpenVLA description—it's pretrained on Open X-Embodiment, a large-scale dataset with nearly a million episodes across different robot platforms, which gives it broad behavioral coverage.

For TracVLA, I need to add that it's around 3.8B parameters and uses spatial trace conditioning to incorporate trajectory information, also trained on an OXE subset.

NORA is roughly 3B parameters and uses its own native vision encoder rather than relying on frozen backbones like the others. I'm noting the updates to the model descriptions—OpenVLA's architecture is being clarified with the specific vision backbone components and parameter counts, while TracVLA is being revised to emphasize how spatial trace conditioning overlays trajectory annotations onto images to guide action prediction. I'm working through the model descriptions and refining how I present each architecture. For NORA, I need to specify that it uses Qwen2.5-VL-3B with around 3 billion parameters, 36 layers, and grouped-query attention configuration, while noting that its vision encoder handles images at dynamic resolution without requiring a separate projection step.

Now I'm checking the visual balance across all model descriptions—OpenVLA and TracVLA each take about 2-3 lines, so NORA should match that length. I'm also verifying the writing style stays consistent with the paper's conventions: no em-dashes, no gerund endings, and avoiding transitional phrases like "Furthermore" or "Additionally." The descriptions should be direct and concise.

I'm doing a terminology pass through the document to catch any inconsistencies—checking for terms like "exit-layer collapse," "R² collapse," and "counterfactual responsiveness" to make sure they're used correctly throughout. The file appears to use "$R^2$" properly in the action probes section, and I see "counterfactual sensitivity" is the right term being used.

For the readout terminology, I'm examining the context carefully. The document defines "image_mean" as the mean activation over image tokens and "readout" as the hidden state at the final pre-action token, so in line 85 where it mentions "readout positions," I need to determine if that's referring to sequence positions or if it should just be "readout" to match the established terminology. I need to be consistent with the terminology defined earlier—"image_mean" and "readout" are the specific extraction position names established in the paper, so line 85 should drop "positions" and just say "applied separately to image_mean and readout" to match that convention.

Let me also verify the other terminology is aligned: "Cross-instruction probes" on line 83 is correct, and the 4096-D dimension mention in line 51 is fine since it's about the actual representation dimensionality being extracted rather than architectural specs.

So my final edits are: rebalance the architecture descriptions in lines 11-14, and change line 85 to remove "positions" for consistency.

Actually, I need to reconsider the "positions" phrasing on line 85. The paper defines "readout" as the key term (bolded on line 46), so I should use just "readout" to match that definition rather than "readout positions." The phrase "applied separately to image_mean and readout" flows better and stays consistent with the paper's own terminology.

Before finalizing all the edits, let me verify there aren't any other formatting issues like em-dashes in the file. I notice line 61 has en-dashes in the number ranges ("demos 0--39 vs. 40--49"), which is standard LaTeX notation and aligns with the writing conventions for numeric ranges.

Now I need to carefully identify the exact text I'm replacing for the architecture balance fix. \textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.
It is pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (970K episodes across multiple robot platforms).
\textbf{TracVLA}~\cite{zheng2024tracevla} uses Phi-3-mini~\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.
\textbf{NORA} uses Qwen2.5-VL-3B (36 layers, grouped-query attention with 16 query heads and 2 KV heads) with its native vision encoder. I'm second-guessing myself on whether to keep "vision" in "vision backbone" — it's actually a standard terminology, so I should restore it. Let me finalize these model descriptions with the proper technical terms intact. I'm checking the line counts to make sure the model descriptions are balanced across the paper—OpenVLA, TracVLA, and NORA are now roughly similar in length when rendered. I'm also verifying that I've removed the projector dimension specifications as requested while keeping the vision backbone descriptions intact.

For TracVLA, I'm adding the Phi-3-mini parameter count (3.8B) and clarifying how spatial trace conditioning works—it overlays visual trajectories on images to guide action prediction. For NORA, I'm including the Qwen2.5-VL-3B parameter count and explaining that its native vision encoder processes images at dynamic resolution without needing a separate projection layer, which is a key architectural advantage.

Now I'm making the edits, starting with the readout terminology fix on line 85—changing "applied separately to image_mean and readout positions" to "applied separately at image_mean and readout" for consistency. I should also scan the rest of the file to catch any other terminology inconsistencies I might have missed, particularly around "readout," "cross-instruction," and other key terms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "c8077776-4d98-4ddb-8a37-2ad5344f14c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHucZj5CgBbSH3ug2oNsSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13974,
      "cache_read_input_tokens": 24232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13974
      },
      "output_tokens": 12,
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

I'll make two edits: rebalance the architecture descriptions in §3.1, and fix a terminology issue on line 85.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "bf533cb3-1c7f-4d0d-8f8b-62213bdc6854",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHucZj5CgBbSH3ug2oNsSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13974,
      "cache_read_input_tokens": 24232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13974
      },
      "output_tokens": 12,
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

<details open><summary>🔧 Tool call — Edit · `toolu_016hXbysExXX8hoCBvTEE3wn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "old_string": "\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIts base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.",
  "new_string": "\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIt is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).\nSpatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.\nTracVLA is trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B ($\\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "c75c71db-fda6-4500-b264-bdfc74c65335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHucZj5CgBbSH3ug2oNsSy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13974,
      "cache_read_input_tokens": 24232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13974
      },
      "output_tokens": 12,
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

_source line 14 · 2026-05-22T06:21:48.438Z_

<details><summary>↩ Tool result · `toolu_016hXbysExXX8hoCBvTEE3wn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "e2961bb1-495b-46f5-82fb-2c6fd253f048",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "oldString": "\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIts base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.",
    "newString": "\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIt is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).\nSpatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.\nTracVLA is trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B ($\\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.\n\n%------------------------------------------------------------------\n\\subsection{Architectures and Data}\n\\label{sec:arch_data}\n\nWe study three VLAs that span distinct backbone families (Table~\\ref{tab:arch_overview}).\n\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIts base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.\n\nEach architecture is evaluated in trained and untrained conditions.\nA critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.\nOpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.\nThis asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.\nFor OpenVLA, two additional conditions support deep-dive analyses (\\S\\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \\texttt{from\\_config()}.\n\nWe evaluate on LIBERO~\\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.\nThe three architectures and four suites form a $3 \\times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).\n\n\\begin{table}[t]\n\\centering\n\\caption{Architectures studied. The untrained baselines differ in kind: OpenVLA's baseline is an OXE-pretrained VLA that produces actions; TracVLA and NORA baselines are pure VLMs with no action training.}\n\\label{tab:arch_overview}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccll@{}}\n\\toprule\nArch. & Backbone & Layers & Attention & Vision Enc. & Untrained Baseline \\\\\n\\midrule\nOpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\\to$ MLP proj. & OXE-pret.\\ VLA \\\\\nTracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\\\\nNORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nFrom each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\\textbf{image\\_mean}, the mean activation over image tokens, and (b)~\\textbf{readout}, the hidden state at the final pre-action token, which follows both image and instruction tokens in the causal sequence and can attend to all preceding context.\nL0 denotes the embedding layer output, L1 through L$N$ the hidden states after each transformer layer ($N = 32$ for OpenVLA and TracVLA, $N = 36$ for NORA), with the final layer including the output layer norm.\nIn all three architectures, image tokens precede instruction tokens; the causal mask prevents image tokens from attending to instructions by construction.\n\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained) and \\emph{instruction presence} (with vs.\\ without task description), applied to all 10 available cells in the cross-architecture matrix.\nOpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\\S\\ref{sec:openvla_routing}).\n\n%------------------------------------------------------------------\n\\subsection{Cross-Architecture Analyses}\n\\label{sec:cross_arch_analyses}\n\nThree analyses are applied to every available cell in the $3 \\times 4$ matrix.\n\n\\paragraph{$R^2$ action probes.}\nTwo-layer MLP probes~\\cite{alain2017} ($d_\\text{in} \\to 256 \\to 7$, ReLU) are trained to predict 7-D action vectors from frozen representations at each layer (Adam, lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5).\nTrain/test splits follow demonstration boundaries (demos 0--39 vs.\\ 40--49) to prevent within-trajectory leakage.\nWe report per-task macro-averaged $R^2$ with bootstrap paired comparisons (10{,}000 resamples).\n\n\\paragraph{L1 attention head profiling.}\nAt L1, each attention head is classified as instruction-dominant ($>50\\%$ of readout-token attention allocated to instruction tokens) or image-dominant.\nResults are reported as $k/N$ instruction-dominant heads, where $N$ is the total L1 head count: 32 for OpenVLA and TracVLA (MHA), 16 for NORA (GQA query heads).\nSensitivity analysis at thresholds from $30\\%$ to $70\\%$ confirms ordering robustness (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Counterfactual instruction perturbation.}\nThe instruction is replaced with four conditions: empty string, wrong task from the same suite, shuffled tokens, and paraphrased instruction.\nA metric constraint arises from the trained/untrained asymmetry.\nTrained models produce action outputs; their sensitivity is measured via Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action representations (NORA).\nUntrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations, a metric with different scale and distributional properties.\nCross-metric ratios between Cohen's $d$ and cosine distance are therefore invalid (\\S\\ref{sec:cf_sensitivity}).\nOpenVLA's OXE-pretrained untrained checkpoint is the exception: because it produces actions, same-metric (Cohen's $d$) trained-vs-untrained comparison is possible for that condition.\n\n%------------------------------------------------------------------\n\\subsection{OpenVLA-Specific Analyses}\n\\label{sec:openvla_analyses}\n\nThree additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.\n\n\\paragraph{Cross-instruction probes.}\nEach visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.\nA 10-way linear classifier identifies which instruction was present, applied separately to image\\_mean and readout positions, with leave-one-out cross-validation (LOOCV) over 10 folds.\n\n\\paragraph{Representational similarity analysis (RSA).}\nRSA~\\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.\nFor each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.\nAlignment is measured via Spearman $\\rho$ between upper-triangular RDM entries; we report mean $\\rho$ across 10 tasks with 95\\% confidence intervals from 10{,}000 bootstrap resamples at the task level~\\cite{nili2014toolbox}.\nWe prefer RSA over CKA~\\cite{kornblith2019}: RSA captures relative distance structure via scale-invariant rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\\ 7-D), while CKA measures global subspace overlap that can remain high when geometric structure differs.\nBoth metrics are reported in Appendix~\\ref{sec:cka_appendix}; their divergence (\\S\\ref{sec:routing_synthesis}) confirms that neither alone fully characterizes representational structure.\n\n\\paragraph{External baselines.}\nDINOv2 ViT-L/14~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}) and CLIP ViT-L/14~\\cite{radford2021_clip} (\\texttt{patch\\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 10,
        "newStart": 8,
        "newLines": 12,
        "lines": [
          " \\label{sec:arch_data}",
          " ",
          " We study three VLAs that span distinct backbone families (Table~\\ref{tab:arch_overview}).",
          "-\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.",
          "-Its base checkpoint is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).",
          "-\\textbf{TracVLA}~\\cite{zheng2024tracevla} uses Phi-3-mini~\\cite{abdin2024phi3} (32 layers, 32 MHA heads) with a SigLIP encoder augmented by spatial trace conditioning, trained on an OXE subset.",
          "-\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B (36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with its native vision encoder.",
          "+\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.",
          "+It is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).",
          "+\\textbf{TracVLA}~\\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).",
          "+Spatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.",
          "+TracVLA is trained on an OXE subset.",
          "+\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B ($\\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.",
          " ",
          " Each architecture is evaluated in trained and untrained conditions.",
          " A critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training."
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01PmciuguVped4HvsbU1NMwB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "old_string": "applied separately to image\\_mean and readout positions, with",
  "new_string": "applied separately at image\\_mean and readout, with"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "ec47a36f-6844-4ad1-8688-2bb46a2bd1d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zQKBNWUHaKYkzUo2s9PxN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8609,
      "cache_read_input_tokens": 38206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8609
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

_source line 16 · 2026-05-22T06:21:52.870Z_

<details><summary>↩ Tool result · `toolu_01PmciuguVped4HvsbU1NMwB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "4caa4b51-fc09-4eb2-ac1f-d581b3c15086",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "oldString": "applied separately to image\\_mean and readout positions, with",
    "newString": "applied separately at image\\_mean and readout, with",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.\n\n%------------------------------------------------------------------\n\\subsection{Architectures and Data}\n\\label{sec:arch_data}\n\nWe study three VLAs that span distinct backbone families (Table~\\ref{tab:arch_overview}).\n\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIt is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).\nSpatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.\nTracVLA is trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B ($\\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.\n\nEach architecture is evaluated in trained and untrained conditions.\nA critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.\nOpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.\nThis asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.\nFor OpenVLA, two additional conditions support deep-dive analyses (\\S\\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \\texttt{from\\_config()}.\n\nWe evaluate on LIBERO~\\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.\nThe three architectures and four suites form a $3 \\times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).\n\n\\begin{table}[t]\n\\centering\n\\caption{Architectures studied. The untrained baselines differ in kind: OpenVLA's baseline is an OXE-pretrained VLA that produces actions; TracVLA and NORA baselines are pure VLMs with no action training.}\n\\label{tab:arch_overview}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccll@{}}\n\\toprule\nArch. & Backbone & Layers & Attention & Vision Enc. & Untrained Baseline \\\\\n\\midrule\nOpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\\to$ MLP proj. & OXE-pret.\\ VLA \\\\\nTracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\\\\nNORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nFrom each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\\textbf{image\\_mean}, the mean activation over image tokens, and (b)~\\textbf{readout}, the hidden state at the final pre-action token, which follows both image and instruction tokens in the causal sequence and can attend to all preceding context.\nL0 denotes the embedding layer output, L1 through L$N$ the hidden states after each transformer layer ($N = 32$ for OpenVLA and TracVLA, $N = 36$ for NORA), with the final layer including the output layer norm.\nIn all three architectures, image tokens precede instruction tokens; the causal mask prevents image tokens from attending to instructions by construction.\n\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained) and \\emph{instruction presence} (with vs.\\ without task description), applied to all 10 available cells in the cross-architecture matrix.\nOpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\\S\\ref{sec:openvla_routing}).\n\n%------------------------------------------------------------------\n\\subsection{Cross-Architecture Analyses}\n\\label{sec:cross_arch_analyses}\n\nThree analyses are applied to every available cell in the $3 \\times 4$ matrix.\n\n\\paragraph{$R^2$ action probes.}\nTwo-layer MLP probes~\\cite{alain2017} ($d_\\text{in} \\to 256 \\to 7$, ReLU) are trained to predict 7-D action vectors from frozen representations at each layer (Adam, lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5).\nTrain/test splits follow demonstration boundaries (demos 0--39 vs.\\ 40--49) to prevent within-trajectory leakage.\nWe report per-task macro-averaged $R^2$ with bootstrap paired comparisons (10{,}000 resamples).\n\n\\paragraph{L1 attention head profiling.}\nAt L1, each attention head is classified as instruction-dominant ($>50\\%$ of readout-token attention allocated to instruction tokens) or image-dominant.\nResults are reported as $k/N$ instruction-dominant heads, where $N$ is the total L1 head count: 32 for OpenVLA and TracVLA (MHA), 16 for NORA (GQA query heads).\nSensitivity analysis at thresholds from $30\\%$ to $70\\%$ confirms ordering robustness (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Counterfactual instruction perturbation.}\nThe instruction is replaced with four conditions: empty string, wrong task from the same suite, shuffled tokens, and paraphrased instruction.\nA metric constraint arises from the trained/untrained asymmetry.\nTrained models produce action outputs; their sensitivity is measured via Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action representations (NORA).\nUntrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations, a metric with different scale and distributional properties.\nCross-metric ratios between Cohen's $d$ and cosine distance are therefore invalid (\\S\\ref{sec:cf_sensitivity}).\nOpenVLA's OXE-pretrained untrained checkpoint is the exception: because it produces actions, same-metric (Cohen's $d$) trained-vs-untrained comparison is possible for that condition.\n\n%------------------------------------------------------------------\n\\subsection{OpenVLA-Specific Analyses}\n\\label{sec:openvla_analyses}\n\nThree additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.\n\n\\paragraph{Cross-instruction probes.}\nEach visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.\nA 10-way linear classifier identifies which instruction was present, applied separately to image\\_mean and readout positions, with leave-one-out cross-validation (LOOCV) over 10 folds.\n\n\\paragraph{Representational similarity analysis (RSA).}\nRSA~\\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.\nFor each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.\nAlignment is measured via Spearman $\\rho$ between upper-triangular RDM entries; we report mean $\\rho$ across 10 tasks with 95\\% confidence intervals from 10{,}000 bootstrap resamples at the task level~\\cite{nili2014toolbox}.\nWe prefer RSA over CKA~\\cite{kornblith2019}: RSA captures relative distance structure via scale-invariant rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\\ 7-D), while CKA measures global subspace overlap that can remain high when geometric structure differs.\nBoth metrics are reported in Appendix~\\ref{sec:cka_appendix}; their divergence (\\S\\ref{sec:routing_synthesis}) confirms that neither alone fully characterizes representational structure.\n\n\\paragraph{External baselines.}\nDINOv2 ViT-L/14~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}) and CLIP ViT-L/14~\\cite{radford2021_clip} (\\texttt{patch\\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.\n",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Cross-instruction probes.}",
          " Each visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.",
          "-A 10-way linear classifier identifies which instruction was present, applied separately to image\\_mean and readout positions, with leave-one-out cross-validation (LOOCV) over 10 folds.",
          "+A 10-way linear classifier identifies which instruction was present, applied separately at image\\_mean and readout, with leave-one-out cross-validation (LOOCV) over 10 folds.",
          " ",
          " \\paragraph{Representational similarity analysis (RSA).}",
          " RSA~\\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space."
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01X3s7RXWgzjW5C8vpBZCod1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "35774d49-4c2a-4259-80fc-6b0bdadaa1de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eaS374o5MXE4ioz4Wf1S4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 46815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 218
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

_source line 18 · 2026-05-22T06:21:57.609Z_

<details><summary>↩ Tool result · `toolu_01X3s7RXWgzjW5C8vpBZCod1`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.
5	
6	%------------------------------------------------------------------
7	\subsection{Architectures and Data}
8	\label{sec:arch_data}
9	
10	We study three VLAs that span distinct backbone families (Table~\ref{tab:arch_overview}).
11	\textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.
12	It is pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).
13	\textbf{TracVLA}~\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).
14	Spatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.
15	TracVLA is trained on an OXE subset.
16	\textbf{NORA}~\cite{TODO_nora} uses Qwen2.5-VL-3B ($\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.
17	
18	Each architecture is evaluated in trained and untrained conditions.
19	A critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
20	OpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.
21	This asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.
22	For OpenVLA, two additional conditions support deep-dive analyses (\S\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \texttt{from\_config()}.
23	
24	We evaluate on LIBERO~\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.
25	The three architectures and four suites form a $3 \times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).
26	
27	\begin{table}[t]
28	\centering
29	\caption{Architectures studied. The untrained baselines differ in kind: OpenVLA's baseline is an OXE-pretrained VLA that produces actions; TracVLA and NORA baselines are pure VLMs with no action training.}
30	\label{tab:arch_overview}
31	\footnotesize
32	\setlength{\tabcolsep}{3pt}
33	\begin{tabular}{@{}llccll@{}}
34	\toprule
35	Arch. & Backbone & Layers & Attention & Vision Enc. & Untrained Baseline \\
36	\midrule
37	OpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\to$ MLP proj. & OXE-pret.\ VLA \\
38	TracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\
39	NORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\
40	\bottomrule
41	\end{tabular}
42	\end{table}
43	
44	%------------------------------------------------------------------
45	\subsection{Representation Extraction}
46	\label{sec:repr_extraction}
47	
48	From each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\textbf{image\_mean}, the mean activation over image tokens, and (b)~\textbf{readout}, the hidden state at the final pre-action token, which follows both image and instruction tokens in the causal sequence and can attend to all preceding context.
49	L0 denotes the embedding layer output, L1 through L$N$ the hidden states after each transformer layer ($N = 32$ for OpenVLA and TracVLA, $N = 36$ for NORA), with the final layer including the output layer norm.
50	In all three architectures, image tokens precede instruction tokens; the causal mask prevents image tokens from attending to instructions by construction.
51	
52	We cross two factors in a $2 \times 2$ factorial design: \emph{training status} (trained vs.\ untrained) and \emph{instruction presence} (with vs.\ without task description), applied to all 10 available cells in the cross-architecture matrix.
53	OpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\S\ref{sec:openvla_routing}).
54	
55	%------------------------------------------------------------------
56	\subsection{Cross-Architecture Analyses}
57	\label{sec:cross_arch_analyses}
58	
59	Three analyses are applied to every available cell in the $3 \times 4$ matrix.
60	
61	\paragraph{$R^2$ action probes.}
62	Two-layer MLP probes~\cite{alain2017} ($d_\text{in} \to 256 \to 7$, ReLU) are trained to predict 7-D action vectors from frozen representations at each layer (Adam, lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5).
63	Train/test splits follow demonstration boundaries (demos 0--39 vs.\ 40--49) to prevent within-trajectory leakage.
64	We report per-task macro-averaged $R^2$ with bootstrap paired comparisons (10{,}000 resamples).
65	
66	\paragraph{L1 attention head profiling.}
67	At L1, each attention head is classified as instruction-dominant ($>50\%$ of readout-token attention allocated to instruction tokens) or image-dominant.
68	Results are reported as $k/N$ instruction-dominant heads, where $N$ is the total L1 head count: 32 for OpenVLA and TracVLA (MHA), 16 for NORA (GQA query heads).
69	Sensitivity analysis at thresholds from $30\%$ to $70\%$ confirms ordering robustness (Appendix~\ref{sec:threshold_sensitivity}).
70	
71	\paragraph{Counterfactual instruction perturbation.}
72	The instruction is replaced with four conditions: empty string, wrong task from the same suite, shuffled tokens, and paraphrased instruction.
73	A metric constraint arises from the trained/untrained asymmetry.
74	Trained models produce action outputs; their sensitivity is measured via Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action representations (NORA).
75	Untrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations, a metric with different scale and distributional properties.
76	Cross-metric ratios between Cohen's $d$ and cosine distance are therefore invalid (\S\ref{sec:cf_sensitivity}).
77	OpenVLA's OXE-pretrained untrained checkpoint is the exception: because it produces actions, same-metric (Cohen's $d$) trained-vs-untrained comparison is possible for that condition.
78	
79	%------------------------------------------------------------------
80	\subsection{OpenVLA-Specific Analyses}
81	\label{sec:openvla_analyses}
82	
83	Three additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.
84	
85	\paragraph{Cross-instruction probes.}
86	Each visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.
87	A 10-way linear classifier identifies which instruction was present, applied separately at image\_mean and readout, with leave-one-out cross-validation (LOOCV) over 10 folds.
88	
89	\paragraph{Representational similarity analysis (RSA).}
90	RSA~\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.
91	For each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.
92	Alignment is measured via Spearman $\rho$ between upper-triangular RDM entries; we report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap resamples at the task level~\cite{nili2014toolbox}.
93	We prefer RSA over CKA~\cite{kornblith2019}: RSA captures relative distance structure via scale-invariant rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\ 7-D), while CKA measures global subspace overlap that can remain high when geometric structure differs.
94	Both metrics are reported in Appendix~\ref{sec:cka_appendix}; their divergence (\S\ref{sec:routing_synthesis}) confirms that neither alone fully characterizes representational structure.
95	
96	\paragraph{External baselines.}
97	DINOv2 ViT-L/14~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}) and CLIP ViT-L/14~\cite{radford2021_clip} (\texttt{patch\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.
98	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "e99a8217-0fb1-41b6-aaed-8641df363a4d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.\n\n%------------------------------------------------------------------\n\\subsection{Architectures and Data}\n\\label{sec:arch_data}\n\nWe study three VLAs that span distinct backbone families (Table~\\ref{tab:arch_overview}).\n\\textbf{OpenVLA}~\\cite{kim2024_openvla,karamcheti2024} chains a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and Llama-2-7B~\\cite{touvron2023_llama2} (6.74B parameters, 32 layers, 32 multi-head attention [MHA] heads) for autoregressive 7-D action decoding.\nIt is pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (OXE; 970K episodes across multiple robot platforms).\n\\textbf{TracVLA}~\\cite{zheng2024tracevla} pairs a SigLIP encoder with Phi-3-mini~\\cite{abdin2024phi3} (3.8B parameters, 32 layers, 32 MHA heads).\nSpatial trace conditioning renders visual trajectory overlays on input images to provide spatial guidance for action prediction.\nTracVLA is trained on an OXE subset.\n\\textbf{NORA}~\\cite{TODO_nora} uses Qwen2.5-VL-3B ($\\sim$3B parameters, 36 layers, grouped-query attention [GQA] with 16 query heads and 2 KV heads) with the native Qwen2.5-VL vision encoder, which processes images at dynamic resolution without a separate projection stage.\n\nEach architecture is evaluated in trained and untrained conditions.\nA critical asymmetry distinguishes the untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained VLA, already fine-tuned for action prediction on 970K episodes, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.\nOpenVLA trained-vs-untrained comparisons therefore measure a VLA-to-VLA transition; TracVLA and NORA comparisons measure VLM-to-VLA transitions.\nThis asymmetry affects the interpretation of all trained/untrained comparisons throughout the paper.\nFor OpenVLA, two additional conditions support deep-dive analyses (\\S\\ref{sec:openvla_routing}): the Llama-2 base language model (no VLA fine-tuning) and a random-weight initialization via \\texttt{from\\_config()}.\n\nWe evaluate on LIBERO~\\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.\nThe three architectures and four suites form a $3 \\times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).\n\n\\begin{table}[t]\n\\centering\n\\caption{Architectures studied. The untrained baselines differ in kind: OpenVLA's baseline is an OXE-pretrained VLA that produces actions; TracVLA and NORA baselines are pure VLMs with no action training.}\n\\label{tab:arch_overview}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccll@{}}\n\\toprule\nArch. & Backbone & Layers & Attention & Vision Enc. & Untrained Baseline \\\\\n\\midrule\nOpenVLA & Llama-2-7B & 32 & 32 MHA & DinoSigLIP $\\to$ MLP proj. & OXE-pret.\\ VLA \\\\\nTracVLA & Phi-3-mini & 32 & 32 MHA & SigLIP + spatial trace & Phi-3-Vision (VLM) \\\\\nNORA & Qwen2.5-VL-3B & 36 & 16q/2kv GQA & Qwen2.5-VL native & Qwen2.5-VL (VLM) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nFrom each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\\textbf{image\\_mean}, the mean activation over image tokens, and (b)~\\textbf{readout}, the hidden state at the final pre-action token, which follows both image and instruction tokens in the causal sequence and can attend to all preceding context.\nL0 denotes the embedding layer output, L1 through L$N$ the hidden states after each transformer layer ($N = 32$ for OpenVLA and TracVLA, $N = 36$ for NORA), with the final layer including the output layer norm.\nIn all three architectures, image tokens precede instruction tokens; the causal mask prevents image tokens from attending to instructions by construction.\n\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained) and \\emph{instruction presence} (with vs.\\ without task description), applied to all 10 available cells in the cross-architecture matrix.\nOpenVLA additionally provides representations from the DinoSigLIP projector output (4{,}096-D), DINOv2 and CLIP external baselines, and the branch-split before fusion; these sources support the OpenVLA deep-dive analyses (\\S\\ref{sec:openvla_routing}).\n\n%------------------------------------------------------------------\n\\subsection{Cross-Architecture Analyses}\n\\label{sec:cross_arch_analyses}\n\nThree analyses are applied to every available cell in the $3 \\times 4$ matrix.\n\n\\paragraph{$R^2$ action probes.}\nTwo-layer MLP probes~\\cite{alain2017} ($d_\\text{in} \\to 256 \\to 7$, ReLU) are trained to predict 7-D action vectors from frozen representations at each layer (Adam, lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5).\nTrain/test splits follow demonstration boundaries (demos 0--39 vs.\\ 40--49) to prevent within-trajectory leakage.\nWe report per-task macro-averaged $R^2$ with bootstrap paired comparisons (10{,}000 resamples).\n\n\\paragraph{L1 attention head profiling.}\nAt L1, each attention head is classified as instruction-dominant ($>50\\%$ of readout-token attention allocated to instruction tokens) or image-dominant.\nResults are reported as $k/N$ instruction-dominant heads, where $N$ is the total L1 head count: 32 for OpenVLA and TracVLA (MHA), 16 for NORA (GQA query heads).\nSensitivity analysis at thresholds from $30\\%$ to $70\\%$ confirms ordering robustness (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Counterfactual instruction perturbation.}\nThe instruction is replaced with four conditions: empty string, wrong task from the same suite, shuffled tokens, and paraphrased instruction.\nA metric constraint arises from the trained/untrained asymmetry.\nTrained models produce action outputs; their sensitivity is measured via Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action representations (NORA).\nUntrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations, a metric with different scale and distributional properties.\nCross-metric ratios between Cohen's $d$ and cosine distance are therefore invalid (\\S\\ref{sec:cf_sensitivity}).\nOpenVLA's OXE-pretrained untrained checkpoint is the exception: because it produces actions, same-metric (Cohen's $d$) trained-vs-untrained comparison is possible for that condition.\n\n%------------------------------------------------------------------\n\\subsection{OpenVLA-Specific Analyses}\n\\label{sec:openvla_analyses}\n\nThree additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.\n\n\\paragraph{Cross-instruction probes.}\nEach visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.\nA 10-way linear classifier identifies which instruction was present, applied separately at image\\_mean and readout, with leave-one-out cross-validation (LOOCV) over 10 folds.\n\n\\paragraph{Representational similarity analysis (RSA).}\nRSA~\\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.\nFor each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.\nAlignment is measured via Spearman $\\rho$ between upper-triangular RDM entries; we report mean $\\rho$ across 10 tasks with 95\\% confidence intervals from 10{,}000 bootstrap resamples at the task level~\\cite{nili2014toolbox}.\nWe prefer RSA over CKA~\\cite{kornblith2019}: RSA captures relative distance structure via scale-invariant rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\\ 7-D), while CKA measures global subspace overlap that can remain high when geometric structure differs.\nBoth metrics are reported in Appendix~\\ref{sec:cka_appendix}; their divergence (\\S\\ref{sec:routing_synthesis}) confirms that neither alone fully characterizes representational structure.\n\n\\paragraph{External baselines.}\nDINOv2 ViT-L/14~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}) and CLIP ViT-L/14~\\cite{radford2021_clip} (\\texttt{patch\\_mean}) provide self-supervised and vision-language pretrained reference points for probing and RSA.\n",
      "numLines": 98,
      "startLine": 1,
      "totalLines": 98
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The file looks good. Let me verify:

1. **Architecture balance** ✓
   - OpenVLA: 2 sentences (~2 lines) — removed projector dimensions, kept essentials
   - TracVLA: 3 sentences (~2.5 lines) — added 3.8B params, explained spatial trace conditioning
   - NORA: 1 long sentence (~2 lines) — added ~3B params, described native vision encoder

2. **Terminology** ✓
   - "readout positions" → "readout" on line 87
   - CoRL style maintained throughout — direct sentences without em-dashes, -ing endings, or hedging phrases
   - All structural elements preserved: section title, table, citations, and cross-references intact

Everything checks out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "1e84ef04-93d3-4560-b2c7-3b528382ce40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4CiLTCTuvppUSmmQpLN8Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2890,
      "cache_read_input_tokens": 47033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2890
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

修改完成。两处变更：

1. **§3.1 架构描述平衡**：OpenVLA 删除了 MLP projector 维度细节 `(2,176-D → 4,096-D)`；TracVLA 补充了 3.8B 参数量和 spatial trace conditioning 的作用（视觉轨迹叠加提供空间引导）；NORA 补充了 ~3B 参数量和 native vision encoder 特征（动态分辨率处理、无独立投影层）。三个架构各约 2-2.5 行，密度均衡。

2. **术语一致性**：line 87 `readout positions` → `readout`，与 §3.2 定义的 `\textbf{readout}` 术语一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "uuid": "cc918a40-61de-440f-87a5-05b35f2cf793",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4CiLTCTuvppUSmmQpLN8Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2890,
      "cache_read_input_tokens": 47033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2890
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

_source line 21_

修改完成。两处变更：

1. **§3.1 架构描述平衡**：OpenVLA 删除了 MLP projector 维度细节 `(2,176-D → 4,096-D)`；TracVLA 补充了 3.8B 参数量和 spatial trace conditioning 的作用（视觉轨迹叠加提供空间引导）；NORA 补充了 ~3B 参数量和 native vision encoder 特征（动态分辨率处理、无独立投影层）。三个架构各约 2-2.5 行，密度均衡。

2. **术语一致性**：line 87 `readout positions` → `readout`，与 §3.2 定义的 `\textbf{readout}` 术语一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 173985,
  "duration_api_ms": 174869,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "8e282148-7caf-4fae-b9c8-12ddf8208406",
  "total_cost_usd": 0.561229,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 38082,
    "cache_read_input_tokens": 168127,
    "output_tokens": 9493,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38082,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 487,
        "cache_read_input_tokens": 47033,
        "cache_creation_input_tokens": 2890,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2890
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1723,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0017929999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 9493,
      "cacheReadInputTokens": 168127,
      "cacheCreationInputTokens": 38082,
      "webSearchRequests": 0,
      "costUSD": 0.559436,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cda4f048-7848-4d07-ab99-af143d8f6790"
}
```

</details>

---
