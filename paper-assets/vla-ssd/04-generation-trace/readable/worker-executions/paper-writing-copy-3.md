# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_20260522T063812.log`
- **Structured JSON:** [`fb06143c862c717357ab.json`](../../sessions/fb/fb06143c862c717357ab.json)

## Before a recorded user message

25 recorded events

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
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
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
  "uuid": "8fa3340e-88be-4436-ba7b-a6487e3153a9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779448800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f88d517f-941a-4050-b3fb-137f39b51836",
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and the current related work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "d9d8fdda-474b-4cf5-b785-d99b7859e522",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoNrYBrSS8bymq7d6iSn8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12415,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12415
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

<details open><summary>🔧 Tool call — Read · `toolu_017ypCnxDzUPyLeLHSWvaJyw`</summary>

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
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "fd588ea6-effd-4fd9-a4ae-34f31dd63098",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoNrYBrSS8bymq7d6iSn8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12415,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12415
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

_source line 6 · 2026-05-22T06:38:26.033Z_

<details><summary>↩ Tool result · `toolu_017ypCnxDzUPyLeLHSWvaJyw`</summary>

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
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "0badb99a-3ec1-45a8-9773-11244bbec641",
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

<details open><summary>🔧 Tool call — Read · `toolu_01HCQcBn2fgKq39UVY7Tr145`</summary>

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
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "079ed9a9-15fa-464c-9243-58f0d2582072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoNrYBrSS8bymq7d6iSn8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12415,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12415
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

_source line 8 · 2026-05-22T06:38:26.630Z_

<details><summary>↩ Tool result · `toolu_01HCQcBn2fgKq39UVY7Tr145`</summary>

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
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "20b81875-33e5-4fca-8e19-c7eddee85527",
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

<details open><summary>🔧 Tool call — Read · `toolu_01JYtkAcHeg4TGdvqa2n6oip`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "3bd37aba-52f2-41af-a605-392b3d76ef27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoNrYBrSS8bymq7d6iSn8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12415,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12415
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

_source line 10 · 2026-05-22T06:38:27.402Z_

<details><summary>↩ Tool result · `toolu_01JYtkAcHeg4TGdvqa2n6oip`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}; recent work conditions action generation on dynamic visual reweighting~\cite{xiao2025ava}.
5	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition across three distinct backbone families.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.
7	Unlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	Mechanistic analyses have identified residual stream communication~\cite{elhage2021}, induction heads for in-context learning~\cite{olsson2022}, complete circuits for specific tasks~\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
11	Attention probing reveals that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}; Michel et al.~\cite{michel2019sixteen} showed most heads can be pruned without loss.
12	Our L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\S\ref{sec:l1_priors}).
13	
14	\paragraph{Behavioral and mechanistic analysis of VLAs.}
15	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input~\cite{grant2026,hou2026,fei2025}.
16	Mechanistic studies have identified sparse semantic directions linked to action selection~\cite{haon2025}, interpretable features and memorized sequences~\cite{swann2026,buurmeijer2026}, symbolic state representations~\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\cite{fang2025}.
17	The closest works, Grant et al.~\cite{grant2026} (visual dominance) and H\"aon et al.~\cite{haon2025} (sparse directions), address \emph{what} information VLAs encode; our analysis addresses \emph{where} instruction information is redistributed across layers and token positions.
18	All prior representational analyses target a single architecture; our $3 \times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).
19	
20	\paragraph{Token-level functional specialization in transformers.}
21	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021}, probing reveals increasingly abstract features across depth~\cite{tenney2019}, the logit lens~\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
22	In VLMs, recent work has characterized visual token sparsity and redundancy~\cite{fan2026visual}, progressive visual-textual alignment across layers~\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\cite{wei2024phase}.
23	We extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.
24	
25	\paragraph{Representation similarity and probing methodology.}
26	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
27	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
28	We adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\S\ref{sec:cf_sensitivity}).
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "eaff53fd-7beb-452b-8b35-917e96224562",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}; recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition across three distinct backbone families.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.\nUnlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\\S\\ref{sec:l1_priors}).\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.\nMechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.\nThe closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis addresses \\emph{where} instruction information is redistributed across layers and token positions.\nAll prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nIn VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.\nWe extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\\S\\ref{sec:cf_sensitivity}).\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
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
Let me analyze the current related work and plan my edits based on the requirements:

### 1. Long sentence splitting and compactification

**Line 4 (VLA paragraph first sentence):** Very long with semicolons.
Current: "VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{...}; recent work conditions action generation on dynamic visual reweighting~\cite{xiao2025ava}."
→ Split into two sentences.

**Line 10 (Mechanistic paragraph):** Long compound sentence listing 6 tools.


I need to break this up into multiple sentences. The first part covers mechanistic analyses identifying specific phenomena like residual stream communication, induction heads, and complete circuits for tasks. Then I'll separate out the causal tracing work for factual recall and the tuned lens approach. Finally, I'll address the feature-level methods that have scaled to dictionary learning across millions of features.

For the next chunk about language models, I'm looking at how feed-forward layers store factual associations, how probing reveals increasingly abstract features as you go deeper, the logit lens tracking prediction changes, and recent work identifying task-specific neurons in multi-task models. I'll split these into shorter, more digestible sentences.

On the third point, I need to compress the comparison to prior work—the key distinction is that we're analyzing representational changes across multiple model families during VLA training, finding exit collapse and counterfactual sensitivity while attention structure preserves base-model patterns. I'll tighten this to focus on the gap we're addressing rather than listing all the details.

For terminology, I'm checking consistency across the paper—making sure "$R^2$ exit collapse" appears consistently where needed, verifying "counterfactual sensitivity," "instruction-dominant," "readout token," and "cross-instruction probes" are used uniformly throughout.

Now I'm mapping out the specific edits: splitting the semicolon-joined sentence in the VLA paragraph, compressing the positioning language in paragraph 1 to focus on the fine-tuning gap rather than duplicating the cross-architecture framing, breaking up the long mechanistic enumeration, ensuring terminology fixes for "$R^2$ exit collapse" in lines 7 and 18, and splitting the token-level LM listing into clearer sentences. I'm working through the edits to tighten the introduction. For the first paragraph's conclusion, I need to compress the representational analysis framing into a single sentence that captures the gap—that while fine-tuning is assumed to reshape internal representations for action prediction, this transformation hasn't been directly tested at the representational level. This sets up the paper's contribution without duplicating the cross-architecture positioning I'm saving for paragraph 3. I need to split the semicolons in lines 4 and 5 into separate sentences, and then compress line 7 to focus on the key finding about representational changes. For line 5, I should remove the "across three distinct backbone families" positioning since that belongs elsewhere. Let me restructure these sentences to be clearer and more direct about the central claims. I'm noting that fine-tuning operates in low intrinsic dimensions and can distort pretrained features, but existing analyses are limited to single architectures and can't separate training dynamics from architecture-specific effects. So I need to position this work as providing the missing per-layer, per-token analysis of how VLA fine-tuning reshapes representations. I'm working through the positioning here—the current draft has some redundancy between sentences about fine-tuning's effects and limitations. Let me tighten this by merging the assumption about action-relevant knowledge with the NLP comparison, then move directly to the architectural limitation before stating what the analysis will provide. That way each sentence builds forward without circling back to the same ideas. I'm reconsidering the structure here—splitting that semicolon-joined clause helps avoid the guideline about limiting semicolons to two clauses. The key insight is that the positioning about cross-architecture analysis belongs in paragraph 3, not mixed into the motivation. So I'm moving the methodological contribution (per-layer, per-token-type decomposition) to its own sentence while keeping the representational gap as the core motivation. I'm debating whether to keep "representational" in "existing representational analyses" — it's more precise than just "existing analyses," so I'll restore that. Now moving to the mechanistic paragraph, I need to compress the discussion of residual stream communication and induction heads while keeping the focus on how these analyses inform my approach to understanding VLA fine-tuning. I'm reorganizing this section on token-level interpretability. The current version mixes Vision Transformers and language models in one long clause with too many items. I'll split it into clearer sentences: one for Vision Transformers covering the CLS token and patch registers, then separate sentences for the language model findings about feed-forward storage, feature abstraction across layers, prediction tracking with the logit lens, and task-specific neurons in multi-task models. I've confirmed the $R^2$ exit collapse terminology fix is in place. Now checking consistency across the document—instruction-dominant heads and readout token references are aligned, and cross-instruction probes is properly sourced from the methods section. The style checks pass: no em-dashes, -ing phrase endings, or filler phrases like "Furthermore" or "Notably." Each paragraph has a clear topic sentence establishing its focus, from VLA fine-tuning through mechanistic analyses to behavioral evaluations and Vision Transformer specifics. Looking at the terminology consistency issue, I need to make sure "$R^2$ exit collapse" is used uniformly throughout rather than any standalone variants. Let me map out the edits I'll need to make, starting with the first paragraph where I'll split up those semicolons and tighten the ending, then work through the rest of the document to standardize the terminology. I'm establishing that existing representational analyses are limited to single architectures and can't disentangle training dynamics from model-specific effects, whereas our approach provides the first granular breakdown of how VLA fine-tuning transforms pretrained representations across different backbone families. I'm working through the edits to this academic paper section, refining how the text flows and clarifies the technical concepts. The current edits focus on splitting up long sentences for readability, adding precision to terminology like specifying $R^2$ for exit collapse, and restructuring the paragraph about language models to separate the Vision Transformer discussion from the LM-specific findings about feed-forward layers, feature abstraction, prediction tracking, and task-specific neurons. I'm reconsidering whether "the first per-layer" reads as a contribution claim when it should stay gap-focused. Let me reframe this to emphasize the analytical approach rather than novelty—something like "We address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations" keeps the positioning grounded in what we're analyzing rather than what we're claiming to be first at.

Looking ahead at paragraph 3, I see it already has two positioning sentences covering the cross-architecture angle and the where-versus-what distinction, so my opening paragraph should stick to one clean positioning sentence about the fine-tuning analysis gap. That keeps the structure balanced across the introduction.

I'm also refining the contrast in line 5—changing it to emphasize that NLP instruction tuning is well-characterized behaviorally while VLA fine-tuning's representational effects remain unexplored. This sharpens the motivation for the work.

Before finalizing, I need to scan through for any other terminology inconsistencies like the "exit collapse" phrasing I caught earlier. Now I'm going through and applying all four corrections to the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "2b8e8196-d1e0-47ea-a6c5-6dac4a261937",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8WTx1aPiogrrx5N2Cc686",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12702,
      "cache_read_input_tokens": 24256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12702
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

Now I'll make the edits. Four changes: (1) split semicolons in para 1 + compress tail positioning, (2) split long enumeration in para 2, (3) fix "$R^2$ exit collapse" terminology in para 3, (4) split long sentence in para 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "eb868e80-786b-4132-9d71-a9d2a8a624f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8WTx1aPiogrrx5N2Cc686",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12702,
      "cache_read_input_tokens": 24256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12702
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

<details open><summary>🔧 Tool call — Edit · `toolu_019nSprRizajyzGYnwS4T5Z9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}; recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition across three distinct backbone families.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.\nUnlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.",
  "new_string": "VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}. Recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations. NLP instruction tuning has been well-characterized at the behavioral level~\\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot separate training dynamics from backbone-specific artifacts.\nWe address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "da2e7f7b-8add-4a3c-8522-e91b793c4a91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8WTx1aPiogrrx5N2Cc686",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12702,
      "cache_read_input_tokens": 24256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12702
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

_source line 14 · 2026-05-22T06:40:30.610Z_

<details><summary>↩ Tool result · `toolu_019nSprRizajyzGYnwS4T5Z9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "f4096002-fb36-4c14-a73f-1e31ef2c1cd8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}; recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition across three distinct backbone families.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.\nUnlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.",
    "newString": "VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}. Recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations. NLP instruction tuning has been well-characterized at the behavioral level~\\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot separate training dynamics from backbone-specific artifacts.\nWe address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}; recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition across three distinct backbone families.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.\nUnlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\\S\\ref{sec:l1_priors}).\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.\nMechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.\nThe closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis addresses \\emph{where} instruction information is redistributed across layers and token positions.\nAll prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nIn VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.\nWe extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\\S\\ref{sec:cf_sensitivity}).\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 10,
        "newStart": 1,
        "newLines": 10,
        "lines": [
          " \\section{Related Work}\\label{sec:related_work}",
          " ",
          " \\paragraph{Vision-language-action models.}",
          "-VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}; recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.",
          "-A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition across three distinct backbone families.",
          "-Fine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot distinguish training dynamics from backbone-specific artifacts.",
          "-Unlike these prior analyses, we test representational changes across three backbone families (Llama-2, Phi-3, Qwen2.5-VL) and find that VLA training creates exit collapse and counterfactual sensitivity while L1 attention structure reflects inherited base-model priors.",
          "+VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}. Recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.",
          "+A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations. NLP instruction tuning has been well-characterized at the behavioral level~\\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.",
          "+Fine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot separate training dynamics from backbone-specific artifacts.",
          "+We address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations.",
          " ",
          " \\paragraph{Mechanistic interpretability in transformers.}",
          " Mechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}."
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

<details open><summary>🔧 Tool call — Edit · `toolu_01WEViEPTuWoMVgL2jrtnvew`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "Mechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.",
  "new_string": "Mechanistic interpretability has revealed residual stream communication~\\cite{elhage2021}, induction heads~\\cite{olsson2022}, and complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}. Causal tracing localizes factual recall~\\cite{meng2022_rome}, the tuned lens tracks per-layer predictions~\\cite{belrose2023_tunedlens}, and feature-level dictionary learning now scales to millions of features~\\cite{bills2023language,templeton2024scaling}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "987e01c9-7c18-49ef-abb4-da34d74481af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8WTx1aPiogrrx5N2Cc686",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12702,
      "cache_read_input_tokens": 24256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12702
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

_source line 16 · 2026-05-22T06:40:33.416Z_

<details><summary>↩ Tool result · `toolu_01WEViEPTuWoMVgL2jrtnvew`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "d55e0393-e18f-474f-af3e-63d7f13ccae4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "Mechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.",
    "newString": "Mechanistic interpretability has revealed residual stream communication~\\cite{elhage2021}, induction heads~\\cite{olsson2022}, and complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}. Causal tracing localizes factual recall~\\cite{meng2022_rome}, the tuned lens tracks per-layer predictions~\\cite{belrose2023_tunedlens}, and feature-level dictionary learning now scales to millions of features~\\cite{bills2023language,templeton2024scaling}.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}. Recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations. NLP instruction tuning has been well-characterized at the behavioral level~\\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot separate training dynamics from backbone-specific artifacts.\nWe address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\\S\\ref{sec:l1_priors}).\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.\nMechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.\nThe closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis addresses \\emph{where} instruction information is redistributed across layers and token positions.\nAll prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nIn VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.\nWe extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\\S\\ref{sec:cf_sensitivity}).\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " We address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations.",
          " ",
          " \\paragraph{Mechanistic interpretability in transformers.}",
          "-Mechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.",
          "+Mechanistic interpretability has revealed residual stream communication~\\cite{elhage2021}, induction heads~\\cite{olsson2022}, and complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}. Causal tracing localizes factual recall~\\cite{meng2022_rome}, the tuned lens tracks per-layer predictions~\\cite{belrose2023_tunedlens}, and feature-level dictionary learning now scales to millions of features~\\cite{bills2023language,templeton2024scaling}.",
          " Attention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.",
          " Our L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\\S\\ref{sec:l1_priors}).",
          " "
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

<details open><summary>🔧 Tool call — Edit · `toolu_01N3ppY3NEeYAH1cmWTwGr1a`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "All prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).",
  "new_string": "All prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) from inherited structure (L1 attention)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "629a7022-5811-4aee-8bdd-56d630fbc61a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8WTx1aPiogrrx5N2Cc686",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12702,
      "cache_read_input_tokens": 24256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12702
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

_source line 18 · 2026-05-22T06:40:35.232Z_

<details><summary>↩ Tool result · `toolu_01N3ppY3NEeYAH1cmWTwGr1a`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "43ae0d85-bc29-4fb6-837d-b981443b6d4e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "All prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).",
    "newString": "All prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}. Recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations. NLP instruction tuning has been well-characterized at the behavioral level~\\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot separate training dynamics from backbone-specific artifacts.\nWe address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic interpretability has revealed residual stream communication~\\cite{elhage2021}, induction heads~\\cite{olsson2022}, and complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}. Causal tracing localizes factual recall~\\cite{meng2022_rome}, the tuned lens tracks per-layer predictions~\\cite{belrose2023_tunedlens}, and feature-level dictionary learning now scales to millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\\S\\ref{sec:l1_priors}).\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.\nMechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.\nThe closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis addresses \\emph{where} instruction information is redistributed across layers and token positions.\nAll prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nIn VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.\nWe extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\\S\\ref{sec:cf_sensitivity}).\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 7,
        "lines": [
          " Behavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.",
          " Mechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.",
          " The closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis addresses \\emph{where} instruction information is redistributed across layers and token positions.",
          "-All prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects (exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).",
          "+All prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).",
          " ",
          " \\paragraph{Token-level functional specialization in transformers.}",
          " In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs."
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_016yjJQLNRn3gqn522njSD89`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.",
  "new_string": "In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}. In language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021} and probing reveals increasingly abstract features across depth~\\cite{tenney2019}. The logit lens~\\cite{nostalgebraist2020} tracks prediction evolution across layers, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "22839c27-60f1-4e82-a81a-49526236a9e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8WTx1aPiogrrx5N2Cc686",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12702,
      "cache_read_input_tokens": 24256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12702
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

_source line 20 · 2026-05-22T06:40:37.653Z_

<details><summary>↩ Tool result · `toolu_016yjJQLNRn3gqn522njSD89`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "40dc8980-5847-4ef8-9763-bdb1ed276dda",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.",
    "newString": "In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}. In language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021} and probing reveals increasingly abstract features across depth~\\cite{tenney2019}. The logit lens~\\cite{nostalgebraist2020} tracks prediction evolution across layers, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}. Recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations. NLP instruction tuning has been well-characterized at the behavioral level~\\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot separate training dynamics from backbone-specific artifacts.\nWe address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic interpretability has revealed residual stream communication~\\cite{elhage2021}, induction heads~\\cite{olsson2022}, and complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}. Causal tracing localizes factual recall~\\cite{meng2022_rome}, the tuned lens tracks per-layer predictions~\\cite{belrose2023_tunedlens}, and feature-level dictionary learning now scales to millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\\S\\ref{sec:l1_priors}).\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.\nMechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.\nThe closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis addresses \\emph{where} instruction information is redistributed across layers and token positions.\nAll prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nIn VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.\nWe extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\\S\\ref{sec:cf_sensitivity}).\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 18,
        "newLines": 7,
        "lines": [
          " All prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).",
          " ",
          " \\paragraph{Token-level functional specialization in transformers.}",
          "-In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.",
          "+In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}. In language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021} and probing reveals increasingly abstract features across depth~\\cite{tenney2019}. The logit lens~\\cite{nostalgebraist2020} tracks prediction evolution across layers, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.",
          " In VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.",
          " We extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.",
          " "
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

<details open><summary>🔧 Tool call — Read · `toolu_0188T8eQY8DBkYXAQuUJyQTi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "6905a62f-bd5b-4cb3-ae3e-41a75714a33b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UyjTYjnVercTqDoG5Z59Bg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9967,
      "cache_read_input_tokens": 36958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9967
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

_source line 22 · 2026-05-22T06:40:42.872Z_

<details><summary>↩ Tool result · `toolu_0188T8eQY8DBkYXAQuUJyQTi`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}. Recent work conditions action generation on dynamic visual reweighting~\cite{xiao2025ava}.
5	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations. NLP instruction tuning has been well-characterized at the behavioral level~\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.
6	Fine-tuning operates in a low intrinsic dimension~\cite{aghajanyan2021intrinsic} and can distort pretrained features~\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot separate training dynamics from backbone-specific artifacts.
7	We address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	Mechanistic interpretability has revealed residual stream communication~\cite{elhage2021}, induction heads~\cite{olsson2022}, and complete circuits for specific tasks~\cite{wang2023_ioi,conmy2023}. Causal tracing localizes factual recall~\cite{meng2022_rome}, the tuned lens tracks per-layer predictions~\cite{belrose2023_tunedlens}, and feature-level dictionary learning now scales to millions of features~\cite{bills2023language,templeton2024scaling}.
11	Attention probing reveals that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}; Michel et al.~\cite{michel2019sixteen} showed most heads can be pruned without loss.
12	Our L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\S\ref{sec:l1_priors}).
13	
14	\paragraph{Behavioral and mechanistic analysis of VLAs.}
15	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input~\cite{grant2026,hou2026,fei2025}.
16	Mechanistic studies have identified sparse semantic directions linked to action selection~\cite{haon2025}, interpretable features and memorized sequences~\cite{swann2026,buurmeijer2026}, symbolic state representations~\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\cite{fang2025}.
17	The closest works, Grant et al.~\cite{grant2026} (visual dominance) and H\"aon et al.~\cite{haon2025} (sparse directions), address \emph{what} information VLAs encode; our analysis addresses \emph{where} instruction information is redistributed across layers and token positions.
18	All prior representational analyses target a single architecture; our $3 \times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).
19	
20	\paragraph{Token-level functional specialization in transformers.}
21	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}. In language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021} and probing reveals increasingly abstract features across depth~\cite{tenney2019}. The logit lens~\cite{nostalgebraist2020} tracks prediction evolution across layers, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
22	In VLMs, recent work has characterized visual token sparsity and redundancy~\cite{fan2026visual}, progressive visual-textual alignment across layers~\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\cite{wei2024phase}.
23	We extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.
24	
25	\paragraph{Representation similarity and probing methodology.}
26	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
27	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
28	We adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\S\ref{sec:cf_sensitivity}).
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "39b7a848-9c34-4b5c-aa77-02e7e2d9e70f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0,zheng2024tracevla,hung2025nora}. Recent work conditions action generation on dynamic visual reweighting~\\cite{xiao2025ava}.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations. NLP instruction tuning has been well-characterized at the behavioral level~\\cite{wei2022finetuned,ouyang2022training}, but the representational effects of VLA fine-tuning remain unexamined.\nFine-tuning operates in a low intrinsic dimension~\\cite{aghajanyan2021intrinsic} and can distort pretrained features~\\cite{kumar2022finetuning}; however, existing representational analyses target a single architecture and cannot separate training dynamics from backbone-specific artifacts.\nWe address this gap with a per-layer, per-token-type decomposition of how VLA fine-tuning reshapes pretrained representations.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic interpretability has revealed residual stream communication~\\cite{elhage2021}, induction heads~\\cite{olsson2022}, and complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}. Causal tracing localizes factual recall~\\cite{meng2022_rome}, the tuned lens tracks per-layer predictions~\\cite{belrose2023_tunedlens}, and feature-level dictionary learning now scales to millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends attention probing to VLAs: OpenVLA shows 24/32 instruction-dominant heads after fine-tuning, but cross-architecture comparison reveals this pattern reflects base-model language priors rather than VLA training, since Phi-3-Vision saturates at 32/32 before any action training (\\S\\ref{sec:l1_priors}).\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input~\\cite{grant2026,hou2026,fei2025}.\nMechanistic studies have identified sparse semantic directions linked to action selection~\\cite{haon2025}, interpretable features and memorized sequences~\\cite{swann2026,buurmeijer2026}, symbolic state representations~\\cite{lu2025,molinari2025}, and fine-tuning erosion of VLM reasoning~\\cite{fang2025}.\nThe closest works, Grant et al.~\\cite{grant2026} (visual dominance) and H\\\"aon et al.~\\cite{haon2025} (sparse directions), address \\emph{what} information VLAs encode; our analysis addresses \\emph{where} instruction information is redistributed across layers and token positions.\nAll prior representational analyses target a single architecture; our $3 \\times 4$ cross-architecture matrix with trained/untrained controls tests whether identified mechanisms replicate across backbone families, and distinguishes training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) from inherited structure (L1 attention).\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}. In language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021} and probing reveals increasingly abstract features across depth~\\cite{tenney2019}. The logit lens~\\cite{nostalgebraist2020} tracks prediction evolution across layers, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nIn VLMs, recent work has characterized visual token sparsity and redundancy~\\cite{fan2026visual}, progressive visual-textual alignment across layers~\\cite{neo2025interpreting,long2026understanding}, and phase-structured feed-forward dynamics~\\cite{wei2024phase}.\nWe extend this to VLAs: image tokens remain instruction-blind across all three architectures (a structural property of the causal mask), while the readout token serves as the multimodal integration site where training concentrates its effects.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix; RSA and CKA can produce divergent orderings on the same data (Appendix~\\ref{sec:cka_appendix}), and Cohen's $d$ and cosine distance are not comparable across trained and untrained conditions (\\S\\ref{sec:cf_sensitivity}).\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
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
The file looks correct. Let me verify all changes:

1. **Para 1 (lines 3-7):** ✓
   - Line 4: Semicolon → period + "Recent work..." as separate sentence
   - Line 5: Semicolon split → two sentences, NLP comparison reframed as gap statement
   - Line 6: Minor wording ("separate" instead of "distinguish") but otherwise preserved
   - Line 7: Compressed to gap-focused positioning without cross-architecture details

2. **Para 2 (line 10):** ✓
   - Long 6-item enumeration split into 2 sentences with 3 items each

3. **Para 3 (line 18):** ✓
   - "exit collapse" → "$R^2$ exit collapse"

4. **Para 4 (line 21):** ✓
   - Long semicolon-joined sentence split into 3 sentences

5. **Preserved:** ✓
   - All 5 \paragraph{} structures
   - All \cite{} unchanged
   - All \ref{} unchanged
   - hung2025nora citation retained

6. **Positioning differentiation:** ✓
   - Para 1 tail and Para 2 opening now clearly distinguish the two approaches
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "656fdb5c-7258-41a3-a44f-f780cd35b9f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLwvXuNvNKtBVU5GiP3bK6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 46925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1650
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

修改完成。四处改动：

1. **段1**：两个分号句拆分为独立句；尾句从 cross-architecture positioning 压缩为 fine-tuning representational analysis gap（"We address this gap with a per-layer, per-token-type decomposition..."）
2. **段2**：6-item 长枚举拆为两句各 3 items
3. **段3**：`exit collapse` → `$R^2$ exit collapse`；保留为主要 cross-architecture positioning
4. **段4**：分号串联 ViT+LM 拆为 3 个独立句

段1 与段3 的 positioning 角度现在不同：段1 侧重 fine-tuning representational analysis 的缺口，段3 侧重 cross-architecture generalization + trained/untrained 对照。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "uuid": "77294a25-7b9e-43bc-a738-18342559399e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLwvXuNvNKtBVU5GiP3bK6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 46925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1650
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

_source line 25_

修改完成。四处改动：

1. **段1**：两个分号句拆分为独立句；尾句从 cross-architecture positioning 压缩为 fine-tuning representational analysis gap（"We address this gap with a per-layer, per-token-type decomposition..."）
2. **段2**：6-item 长枚举拆为两句各 3 items
3. **段3**：`exit collapse` → `$R^2$ exit collapse`；保留为主要 cross-architecture positioning
4. **段4**：分号串联 ViT+LM 拆为 3 个独立句

段1 与段3 的 positioning 角度现在不同：段1 侧重 fine-tuning representational analysis 的缺口，段3 侧重 cross-architecture generalization + trained/untrained 对照。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 159636,
  "duration_api_ms": 160944,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "b2f90fe6-c29f-49df-9cb4-a33ff2afdc84",
  "total_cost_usd": 0.5573625,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 36734,
    "cache_read_input_tokens": 119980,
    "output_tokens": 10637,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36734,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 701,
        "cache_read_input_tokens": 46925,
        "cache_creation_input_tokens": 1650,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1650
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1750,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00183,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 10637,
      "cacheReadInputTokens": 119980,
      "cacheCreationInputTokens": 36734,
      "webSearchRequests": 0,
      "costUSD": 0.5555325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "91f93957-f90c-4734-95f4-b59a77e2a892"
}
```

</details>

---
